# -*- coding: utf-8 -*-
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
RPY_DIR = ROOT / "Wells_Revisor"
if str(RPY_DIR) not in sys.path:
    sys.path.insert(0, str(RPY_DIR))

from wells_revisor_core import review_text, review_file
from wells_guia_ptbr import validar_revisao


class RevisorRpyLinguisticaTests(unittest.TestCase):
    def test_remove_espaco_antes_de_pontuacao(self):
        out, changes, _ = review_text("Olá , tudo bem ?")
        self.assertEqual(out, "Olá, tudo bem?")
        self.assertGreater(changes, 0)

    def test_adiciona_espaco_depois_de_pontuacao(self):
        out, changes, _ = review_text("Sim,claro!")
        self.assertEqual(out, "Sim, claro!")
        self.assertGreater(changes, 0)

    def test_desde_com_oracao_recebe_que(self):
        out, changes, _ = review_text("desde [player] nasceu")
        self.assertEqual(out, "desde que [player] nasceu")
        self.assertGreater(changes, 0)

    def test_parentesco_com_token_reordena_construcao_literal(self):
        out, changes, _ = review_text("a mãe [player] de")
        self.assertEqual(out, "a mãe de [player]")
        self.assertGreater(changes, 0)

    def test_token_renpy_permanece_byte_identico(self):
        original = "Olá, [player_name]! {i}Tudo bem?{/i}"
        out, _, tokens = review_text(original)
        self.assertEqual(out, original)
        self.assertEqual(tokens, 3)

    def test_token_interno_nao_e_revisado_como_portugues(self):
        original = "desde [nasceu] chegou"
        out, _, _ = review_text(original)
        self.assertIn("[nasceu]", out)

    def test_guia_rejeita_troca_local_de_genero(self):
        ok, motivo = validar_revisao("amigo fiel", "amiga fiel")
        self.assertFalse(ok)
        self.assertIn("gênero/número", motivo)

    def test_repeticao_de_dialogo_nao_e_apagada(self):
        original = "não não, espere!"
        out, _, _ = review_text(original)
        self.assertEqual(out, original)

    def test_nome_com_apostrofo_nao_sofre_contracao_cega(self):
        original = "Eu falei de A'nai."
        out, _, _ = review_text(original)
        self.assertEqual(out, original)

    def test_arquivo_txt_preserva_registros_e_tokens(self):
        with tempfile.TemporaryDirectory() as td:
            root = Path(td)
            p = root / "traduzido.txt"
            p.write_text(
                '"Olá , [player]!"\n"desde [player] nasceu"\n"não não, espere!"\n',
                encoding="utf-8",
            )
            before_count = len(p.read_text(encoding="utf-8").splitlines())
            result = review_file(p, RPY_DIR)
            lines = p.read_text(encoding="utf-8").splitlines()
            self.assertEqual(len(lines), before_count)
            self.assertEqual(lines[0], '"Olá, [player]!"')
            self.assertEqual(lines[1], '"desde que [player] nasceu"')
            self.assertEqual(lines[2], '"não não, espere!"')
            self.assertEqual(result["records"], 3)
            self.assertGreaterEqual(result["tokens"], 2)


if __name__ == "__main__":
    unittest.main()
