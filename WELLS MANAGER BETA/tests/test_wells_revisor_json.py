# -*- coding: utf-8 -*-
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
JSON_DIR = ROOT / "Wells_Revisor_JSON"
if str(JSON_DIR) not in sys.path:
    sys.path.insert(0, str(JSON_DIR))

from wells_blindagem_json import (
    LISTA_BLINDADOS, LISTA_TRADUZIVEIS, salvar_listas
)
from wells_revisor_json_core import review_json_pair


class RevisorJsonIndependenteTests(unittest.TestCase):
    def _pair(self, native, translated, blindados=(), traduziveis=()):
        td = tempfile.TemporaryDirectory()
        root = Path(td.name)
        n = root / "nativo.txt"
        t = root / "traduzido.txt"
        b = root / "blindagem.txt"
        n.write_text("\n".join(f'"{x}"' for x in native) + "\n", encoding="utf-8")
        t.write_text("\n".join(f'"{x}"' for x in translated) + "\n", encoding="utf-8")
        salvar_listas(b, {
            LISTA_BLINDADOS: list(blindados),
            LISTA_TRADUZIVEIS: list(traduziveis),
        })
        before = n.read_bytes()
        result = review_json_pair(n, t, root, b)
        after = n.read_bytes()
        lines = t.read_text(encoding="utf-8").splitlines()
        return td, result, before, after, lines

    def test_blindagem_exata_restaura_registro_nativo(self):
        td, result, before, after, lines = self._pair(
            ["Christine"], ["Cristina"], blindados=["Christine"]
        )
        self.addCleanup(td.cleanup)
        self.assertEqual(lines, ['"Christine"'])
        self.assertEqual(result["protected_records"], 1)
        self.assertEqual(before, after)

    def test_blindagem_nao_age_como_substring(self):
        td, result, before, after, lines = self._pair(
            ["Princess Christine"], ["Princesa Cristina"], blindados=["Christine"]
        )
        self.addCleanup(td.cleanup)
        self.assertEqual(lines, ['"Princesa Cristina"'])
        self.assertEqual(result["protected_records"], 0)
        self.assertEqual(before, after)

    def test_registro_composto_precisa_ser_cadastrado_exatamente(self):
        td, result, before, after, lines = self._pair(
            ["Princess Christine"], ["Princesa Cristina"],
            blindados=["Princess Christine"]
        )
        self.addCleanup(td.cleanup)
        self.assertEqual(lines, ['"Princess Christine"'])
        self.assertEqual(result["protected_records"], 1)
        self.assertEqual(before, after)

    def test_conflito_nao_recebe_prioridade_automatica(self):
        td, result, before, after, lines = self._pair(
            ["Christine"], ["Cristina"],
            blindados=["Christine"], traduziveis=["Christine"]
        )
        self.addCleanup(td.cleanup)
        self.assertEqual(lines, ['"Cristina"'])
        self.assertEqual(result["protected_records"], 0)
        self.assertEqual(result["conflict_records"], 1)
        self.assertEqual(before, after)


if __name__ == "__main__":
    unittest.main()
