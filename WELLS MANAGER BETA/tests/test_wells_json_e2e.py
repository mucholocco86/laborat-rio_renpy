# -*- coding: utf-8 -*-
"""E2E do fluxo JSON real: extrair -> revisar par -> reinjetar."""
import json
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
JSON_REVISOR = ROOT / "Wells_Revisor_JSON"
TRANSLATOR = ROOT / "Wells_Translator"
for p in (JSON_REVISOR, TRANSLATOR):
    if str(p) not in sys.path:
        sys.path.insert(0, str(p))

from wells_blindagem_json import LISTA_BLINDADOS, LISTA_TRADUZIVEIS, salvar_listas
from wells_revisor_json_core import review_json_pair
from wells_json_core import (
    export_json_full_txt, export_json_blocks_txt,
    export_json_full_docx, export_json_blocks_docx,
    inject_json_translations,
)


class WellsJsonEndToEndTests(unittest.TestCase):
    PAIRS = [
        ("Dalen", "O Vale"),
        ("Commander Gaius", "Comandante Go"),
        ("Commander Gaius arrives", "Comandante Go chega"),
        ("Commander [player] Gaius {b}", "Comandante [player] gaius {b}"),
        ("Plain line", "Linha normal"),
    ]

    def _run_pipeline(self, fmt, blocks):
        td = tempfile.TemporaryDirectory()
        self.addCleanup(td.cleanup)
        root = Path(td.name)
        source = root / "strings.json"
        work = root / "work"
        work.mkdir()
        blindagem = root / "blindagem.txt"

        source.write_text(
            "{" + ",".join(
                json.dumps(k, ensure_ascii=False) + ":" + json.dumps(v, ensure_ascii=False)
                for k, v in self.PAIRS
            ) + "}\n",
            encoding="utf-8",
        )
        salvar_listas(blindagem, {
            LISTA_BLINDADOS: ["Dalen", "Gaius"],
            LISTA_TRADUZIVEIS: ["Commander"],
        })

        if fmt == "txt" and not blocks:
            result = export_json_full_txt(source, work, return_session=True)
        elif fmt == "txt":
            result = export_json_blocks_txt(source, work, max_bytes=70, return_session=True)
        elif not blocks:
            result = export_json_full_docx(source, work, return_session=True)
        else:
            result = export_json_blocks_docx(
                source, work, max_file_bytes=37000, return_session=True
            )
        session = result[-1]

        native_files = sorted(work.glob(f"nativo*.{fmt}"))
        translated_files = sorted(work.glob(f"traduzido*.{fmt}"))
        self.assertEqual(len(native_files), len(translated_files))
        self.assertGreater(len(native_files), 0)
        if blocks:
            self.assertGreater(len(native_files), 1)

        native_before = {p.name: p.read_bytes() for p in native_files}
        totals = {"reconstructed": 0, "unresolved": [], "protected": 0}
        for native, translated in zip(native_files, translated_files):
            stats = review_json_pair(
                native, translated, JSON_REVISOR, blindagem_path=blindagem
            )
            totals["reconstructed"] += stats["reconstructed_names"]
            totals["unresolved"].extend(stats["unresolved_names"])
            totals["protected"] += stats["protected_names"]

        for p in native_files:
            self.assertEqual(p.read_bytes(), native_before[p.name])

        count, mode = inject_json_translations(
            source, work, fmt, session=session
        )
        self.assertEqual(count, len(self.PAIRS))
        self.assertEqual(mode, "blocks" if blocks else "full")

        final_pairs = json.loads(
            source.read_text(encoding="utf-8"),
            object_pairs_hook=lambda pairs: pairs,
        )
        self.assertEqual([k for k, _ in final_pairs], [k for k, _ in self.PAIRS])
        expected_values = [
            "Dalen",
            "Comandante Gaius",
            "Comandante Go chega",
            "Comandante [player] Gaius {b}",
            "Linha normal",
        ]
        self.assertEqual([v for _, v in final_pairs], expected_values)
        self.assertEqual(totals["reconstructed"], 2)
        self.assertEqual(len(totals["unresolved"]), 1)
        self.assertEqual(totals["unresolved"][0]["term"], "Gaius")
        self.assertGreaterEqual(totals["protected"], 3)

    def test_e2e_txt_completo(self):
        self._run_pipeline("txt", False)

    def test_e2e_txt_blocos(self):
        self._run_pipeline("txt", True)

    def test_e2e_docx_completo(self):
        self._run_pipeline("docx", False)

    def test_e2e_docx_blocos(self):
        self._run_pipeline("docx", True)


if __name__ == "__main__":
    unittest.main()
