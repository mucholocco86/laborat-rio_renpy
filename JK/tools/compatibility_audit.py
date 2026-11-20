#!/usr/bin/env python3
"""Read-only static inventory of Ren'Py API references used by JK."""
from __future__ import annotations
import argparse, json, re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
SDK_VERSIONS = {
    "6.99.4": ROOT / "renpy-6.99.4-sdk" / "renpy",
    "7.4.11": ROOT / "renpy-7.4.11-sdk" / "renpy",
    "8.5.3": ROOT / "renpy-8.5.3-sdk" / "renpy",
}
RENpy_REF = re.compile(r"\brenpy((?:\.[A-Za-z_]\w*){1,4})")
IMPORT_REF = re.compile(r"^\s*(?:from\s+renpy(?:\.([A-Za-z_]\w*(?:\.[A-Za-z_]\w*)*))?\s+import\s+([^\n#]+)|import\s+renpy\.([A-Za-z_]\w*(?:\.[A-Za-z_]\w*))*)", re.M)
TARGETS = re.compile(r"^\s*(?:async\s+)?(?:def|class)\s+(load|save|loads|dump|unfreeze|freeze|complete|rollback|get_changes|scan_saved_game|save_persistent|RollbackLog|Context|StoreDict)\b")

def py_files(directory):
    return sorted(p for p in directory.rglob("*.py") if "__pycache__" not in p.parts) if directory.exists() else []

def module_exists(package, module):
    base = package.joinpath(*module.split("."))
    return base.with_suffix(".py").is_file() or (base / "__init__.py").is_file() or base.is_dir()

def collect_refs(files):
    refs = {}
    for path in files:
        content = path.read_text(encoding="utf-8", errors="replace")
        for match in RENpy_REF.finditer(content):
            parts = match.group(1).lstrip(".").split(".")
            if len(parts) >= 2:
                refs.setdefault((".".join(parts[:-1]), parts[-1]), set()).add(path.relative_to(ROOT).as_posix())
        for match in IMPORT_REF.finditer(content):
            module = match.group(1) or match.group(3)
            if module:
                refs.setdefault((module, "<module-import>"), set()).add(path.relative_to(ROOT).as_posix())
    return refs

def inventory(package, filename):
    path = package / filename
    if not path.is_file():
        return {"present": False, "definitions": []}
    definitions = []
    for number, line in enumerate(path.read_text(encoding="utf-8", errors="replace").splitlines(), 1):
        if TARGETS.search(line):
            definitions.append({"line": number, "signature": line.strip()})
    return {"present": True, "definitions": definitions}

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", default="jk-compatibility-report")
    args = parser.parse_args()
    jk_files = sorted(p for p in (ROOT / "JK").rglob("*.rpy") if p.is_file())
    refs = collect_refs(jk_files)
    report = {
        "scope": "read-only static inventory; not proof of runtime compatibility",
        "jk_files_scanned": len(jk_files),
        "api_reference_count": len(refs),
        "sdks": {},
        "api_references": [],
        "warnings": [],
    }
    packages = {}
    for version, package in SDK_VERSIONS.items():
        files = py_files(package)
        packages[version] = files
        report["sdks"][version] = {
            "package_present": package.is_dir(),
            "python_source_files": len(files),
            "core_api_inventory": {name: inventory(package, name) for name in
                ("loadsave.py", "python.py", "rollback.py", "game.py", "exports.py", "config.py")},
        }
        if not package.is_dir():
            report["warnings"].append(f"SDK {version}: Ren'Py source directory not found.")
    for (module, symbol), origins in sorted(refs.items()):
        row = {"module": module, "symbol": symbol, "used_by": sorted(origins), "sdk_status": {}}
        for version, package in SDK_VERSIONS.items():
            files = packages[version]
            exists = module_exists(package, module)
            if symbol == "<module-import>":
                row["sdk_status"][version] = {"module_path_found": exists}
            else:
                hits = [p.relative_to(package).as_posix() for p in files
                        if re.search(r"\b" + re.escape(symbol) + r"\b",
                                     p.read_text(encoding="utf-8", errors="replace"))]
                row["sdk_status"][version] = {
                    "module_path_found": exists,
                    "symbol_text_found_in_package": bool(hits),
                    "evidence_files": hits[:12],
                }
        report["api_references"].append(row)
    out = ROOT / args.output
    out.mkdir(parents=True, exist_ok=True)
    (out / "api-compatibility.json").write_text(json.dumps(report, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    lines = [
        "# JK — inventário estático de compatibilidade", "",
        "> Correspondência textual não comprova compatibilidade em execução.", "",
        f"- Arquivos RPY analisados: **{len(jk_files)}**",
        f"- Pares módulo/símbolo identificados: **{len(refs)}**", "",
        "## Cobertura dos SDKs", "",
        "| SDK | Diretório Ren'Py | Arquivos Python indexados |",
        "|---|---:|---:|",
    ]
    for version, data in report["sdks"].items():
        lines.append(f"| {version} | {'sim' if data['package_present'] else 'não'} | {data['python_source_files']} |")
    lines += ["", "## Referências de API", "", "| Referência | 6.99.4 | 7.4.11 | 8.5.3 |", "|---|---|---|---|"]
    for row in report["api_references"]:
        label = row["module"] if row["symbol"] == "<module-import>" else row["module"] + "." + row["symbol"]
        statuses = []
        for version in SDK_VERSIONS:
            status = row["sdk_status"][version]
            if row["symbol"] == "<module-import>":
                statuses.append("encontrado" if status["module_path_found"] else "não localizado")
            elif not status["module_path_found"]:
                statuses.append("módulo não localizado")
            else:
                statuses.append("texto localizado" if status["symbol_text_found_in_package"] else "não localizado")
        lines.append(f"| {label} | {statuses[0]} | {statuses[1]} | {statuses[2]} |")
    lines += ["", "## Inventário load/save/rollback", ""]
    for version, data in report["sdks"].items():
        lines += [f"### Ren'Py {version}", ""]
        for filename, details in data["core_api_inventory"].items():
            if not details["present"]:
                lines.append(f"- {filename}: ausente")
            else:
                lines.append(f"- {filename}:")
                for definition in details["definitions"]:
                    lines.append(f"  - linha {definition['line']}: {definition['signature']}")
        lines.append("")
    if report["warnings"]:
        lines += ["## Avisos", ""] + ["- " + item for item in report["warnings"]]
    lines += ["", "## Limitações", "",
        "- O scanner não executa jogos nem inicializa os SDKs.",
        "- Uma ocorrência textual pode ser comentário, importação indireta ou símbolo não exposto publicamente.",
        "- Ausência de ocorrência textual não prova ausência em runtime.",
        "- Testes dinâmicos de load/save/rollback ainda serão necessários.", ""]
    (out / "api-compatibility.md").write_text("\n".join(lines), encoding="utf-8")
    print(f"JK files scanned: {len(jk_files)}")
    print(f"API references indexed: {len(refs)}")
    print(f"Report: {out / 'api-compatibility.md'}")

if __name__ == "__main__":
    main()
