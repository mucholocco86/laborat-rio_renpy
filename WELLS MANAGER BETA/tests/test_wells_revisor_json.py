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

    def test_blindado_exato_e_restaurado_quando_sobrevive(self):
        td, result, before, after, lines = self._pair(
            ["Christine"], ["christine"], blindados=["Christine"]
        )
        self.addCleanup(td.cleanup)
        self.assertEqual(lines, ['"Christine"'])
        self.assertEqual(result["protected_names"], 1)
        self.assertEqual(result["unresolved_names"], [])
        self.assertEqual(before, after)

    def test_blindagem_age_dentro_de_registro_composto_sem_congelar_unidade(self):
        td, result, before, after, lines = self._pair(
            ["Princess Christine"], ["Princesa christine"],
            blindados=["Christine"]
        )
        self.addCleanup(td.cleanup)
        self.assertEqual(lines, ['"Princesa Christine"'])
        self.assertEqual(result["protected_records"], 1)
        self.assertEqual(result["protected_names"], 1)
        self.assertEqual(before, after)

    def test_termo_maior_nao_casa_com_parte_de_outra_palavra(self):
        td, result, before, after, lines = self._pair(
            ["Princess Dalenor"], ["Princesa dalenor"],
            blindados=["Dalen"]
        )
        self.addCleanup(td.cleanup)
        self.assertEqual(lines, ['"Princesa dalenor"'])
        self.assertEqual(result["protected_names"], 0)
        self.assertEqual(result["unresolved_names"], [])
        self.assertEqual(before, after)

    def test_nome_destruido_em_registro_integral_e_restaurado(self):
        td, result, before, after, lines = self._pair(
            ["Dalen"], ["O Vale"], blindados=["Dalen"]
        )
        self.addCleanup(td.cleanup)
        self.assertEqual(lines, ['"Dalen"'])
        self.assertEqual(result["protected_names"], 1)
        self.assertEqual(result["reconstructed_names"], 1)
        self.assertEqual(result["unresolved_names"], [])
        self.assertEqual(before, after)

    def test_nome_destruido_em_registro_composto_fica_pendente(self):
        td, result, before, after, lines = self._pair(
            ["Commander Gaius"], ["Comandante Go"],
            blindados=["Gaius"], traduziveis=["Commander"]
        )
        self.addCleanup(td.cleanup)
        self.assertEqual(lines, ['"Comandante Go"'])
        self.assertEqual(result["protected_names"], 0)
        self.assertEqual(result["reconstructed_names"], 0)
        self.assertEqual(len(result["unresolved_names"]), 1)
        self.assertEqual(result["unresolved_names"][0]["term"], "Gaius")
        self.assertEqual(before, after)

    def test_lista_vazia_nao_cria_protecao_implicita(self):
        td, result, before, after, lines = self._pair(
            ["Dalen"], ["O Vale"]
        )
        self.addCleanup(td.cleanup)
        self.assertEqual(lines, ['"O Vale"'])
        self.assertEqual(result["protected_names"], 0)
        self.assertEqual(result["unresolved_names"], [])
        self.assertEqual(before, after)

    def test_conflito_nao_recebe_prioridade_automatica(self):
        td, result, before, after, lines = self._pair(
            ["Princess Christine"], ["Princesa Cristina"],
            blindados=["Christine"], traduziveis=["Christine"]
        )
        self.addCleanup(td.cleanup)
        self.assertEqual(lines, ['"Princesa Cristina"'])
        self.assertEqual(result["protected_names"], 0)
        self.assertEqual(result["conflict_records"], 1)
        self.assertEqual(before, after)


if __name__ == "__main__":
    unittest.main()
