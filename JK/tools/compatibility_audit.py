#!/usr/bin/env python3
"""Read-only heuristic inventory of Ren'Py API expressions used by JK."""
from __future__ import annotations
import argparse
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
SDK_VERSIONS = {
    "6.99.4": ROOT / "renpy-6.99.4-sdk" / "renpy",
    "7.4.11": ROOT / "renpy-7.4.11-sdk" / "renpy",
    "8.5.3": ROOT / "renpy-8.5.3-sdk" / "renpy",
}
CHAIN = re.compile(r"\brenpy(?:\.[A-Za-z_]\w*)+")
TARGETS = re.compile(r"^\s*(?:async\s+)?(?:def|class)\s+(load|save|loads|dump|unfreeze|freeze|complete|rollback|get_changes|scan_saved_game|save_persistent|RollbackLog|Context|StoreDict)\b")
CORE = ("loadsave.py", "python.py", "rollback.py", "game.py", "exports.py", "config.py")

def py_files(path):
    return sorted(p for p in path.rglob("*.py") if "__pycache__" not in p.parts) if path.exists() else []

def module_exists(package, dotted):
    base = package.joinpath(*dotted.split("."))
    return base.with_suffix(".py").is_file() or (base / "__init__.py").is_file() or base.is_dir()

def collect(files):
    refs = {}
    for path in files:
        source = path.read_text(encoding="utf-8", errors="replace")
        for match in CHAIN.finditer(source):
            refs.setdefault(match.group(0), set()).add(path.relative_to(ROOT).as_posix())
    return refs

def resolve(package, expression):
    parts = expression.split(".")[1:]
    for count in range(len(parts), 0, -1):
        candidate = ".".join(parts[:count])
        if module_exists(package, candidate):
            rest = ".".join(parts[count:])
            file = package.joinpath(*candidate.split(".")).with_suffix(".py")
            if not file.is_file():
                file = package.joinpath(*candidate.split("."), "__init__.py")
            token = rest.split(".")[0] if rest else None
            found = None
            if token and file.is_file():
                found = bool(re.search(r"\b" + re.escape(token) + r"\b", file.read_text(encoding="utf-8", errors="replace")))
            return {"kind": "module", "module": candidate, "attribute_chain": rest,
                    "attribute_token_found_in_module_source": found,
                    "evidence_file": file.relative_to(package).as_posix() if file.is_file() else None}
    return {"kind": "root_or_dynamic_namespace", "module": "renpy",
            "attribute_chain": ".".join(parts), "attribute_token_found_in_module_source": None,
            "evidence_file": None}

def core_inventory(package, filename):
    path = package / filename
    if not path.is_file():
        return {"present": False, "definitions": []}
    found = []
    for number, line in enumerate(path.read_text(encoding="utf-8", errors="replace").splitlines(), 1):
        if TARGETS.search(line):
            found.append({"line": number, "signature": line.strip()})
    return {"present": True, "definitions": found}

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", default="jk-compatibility-report")
    args = parser.parse_args()
    jk_files = sorted(p for p in (ROOT / "JK").rglob("*.rpy") if p.is_file())
    refs = collect(jk_files)
    sdk_files = {v: py_files(p) for v, p in SDK_VERSIONS.items()}
    report = {"scope": "read-only heuristic static inventory; not proof of runtime compatibility",
              "jk_files_scanned": len(jk_files), "unique_renpy_expressions": len(refs),
              "sdks": {}, "api_expressions": [], "warnings": []}
    for version, package in SDK_VERSIONS.items():
        report["sdks"][version] = {
            "package_present": package.is_dir(), "python_source_files": len(sdk_files[version]),
            "core_api_inventory": {name: core_inventory(package, name) for name in CORE}}
        if not package.is_dir():
            report["warnings"].append("SDK " + version + ": Ren'Py source directory not found.")
    for expression, origins in sorted(refs.items()):
        report["api_expressions"].append({
            "expression": expression, "used_by": sorted(origins),
            "sdk_status": {v: resolve(p, expression) for v, p in SDK_VERSIONS.items()}})
    out = ROOT / args.output
    out.mkdir(parents=True, exist_ok=True)
    (out / "api-compatibility.json").write_text(json.dumps(report, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    lines = ["# JK — inventário estático de compatibilidade", "",
             "> Scanner heurístico: correspondência textual não comprova compatibilidade em execução.", "",
             "- Arquivos RPY analisados: **" + str(len(jk_files)) + "**",
             "- Expressões Ren'Py únicas identificadas: **" + str(len(refs)) + "**", "",
             "## Cobertura dos SDKs", "", "| SDK | Diretório Ren'Py | Arquivos Python indexados |",
             "|---|---:|---:|"]
    for v, d in report["sdks"].items():
        lines.append("| " + v + " | " + ("sim" if d["package_present"] else "não") + " | " + str(d["python_source_files"]) + " |")
    lines += ["", "## Expressões Ren'Py", "", "| Expressão | 6.99.4 | 7.4.11 | 8.5.3 |", "|---|---|---|---|"]
    for row in report["api_expressions"]:
        status = []
        for v in SDK_VERSIONS:
            item = row["sdk_status"][v]
            if item["kind"] == "root_or_dynamic_namespace":
                status.append("namespace raiz/dinâmico")
            else:
                status.append(item["module"] + " — " + ("token localizado" if item["attribute_token_found_in_module_source"] else "token não localizado"))
        lines.append("| " + row["expression"] + " | " + " | ".join(status) + " |")
    lines += ["", "## Inventário load/save/rollback", ""]
    for v, d in report["sdks"].items():
        lines += ["### Ren'Py " + v, ""]
        for filename, item in d["core_api_inventory"].items():
            if not item["present"]:
                lines.append("- " + filename + ": ausente")
            else:
                lines.append("- " + filename + ":")
                for definition in item["definitions"]:
                    lines.append("  - linha " + str(definition["line"]) + ": " + definition["signature"])
        lines.append("")
    lines += ["## Limitações", "",
              "- O scanner não executa jogos nem inicializa os SDKs.",
              "- Ocorrências em comentários ou strings também podem ser identificadas.",
              "- Nomes dinâmicos e aliases exportados no namespace raiz não são resolvidos por caminho de arquivo.",
              "- A presença de um token não comprova assinatura nem comportamento.",
              "- Testes dinâmicos isolados de load/save/rollback continuam necessários.", ""]
    (out / "api-compatibility.md").write_text("\n".join(lines), encoding="utf-8")
    print("JK files scanned:", len(jk_files))
    print("Unique Ren'Py expressions indexed:", len(refs))
    print("Report:", out / "api-compatibility.md")

if __name__ == "__main__":
    main()
