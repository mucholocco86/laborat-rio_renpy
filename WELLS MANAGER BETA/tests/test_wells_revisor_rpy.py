# -*- coding: utf-8 -*-
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
RPY_DIR = ROOT / "Wells_Revisor"
if str(RPY_DIR) not in sys.path:
    sys.path.insert(0, str(RPY_DIR))

from wells_revisor_core import (
    review_text, review_file, diagnosticar_texto,
    _correct_source_anchored_structures,
)
from wells_guia_ptbr import validar_revisao
from wells_isolador_renpy import segmentar


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


    def test_corpus_real_diagnostica_sem_reescrever_parentesco_ambiguo(self):
        casos = {
            "Seu Mãe O nome de é Vivian Wells.": {"concordancia_possessivo", "ordem_nome_quebrada"},
            "Você é dela Filho e você se dirigirá a ela como Mãe.": {"parentesco_pos_pronome"},
            "O nome dela é Ariel Ela é sua filha mais nova. Irmã E você é mais velho que ela. Irmão.": {"fragmento_parentesco"},
        }
        for original, esperados in casos.items():
            with self.subTest(original=original):
                codigos = {x["code"] for x in diagnosticar_texto(original)}
                self.assertTrue(esperados.issubset(codigos))
                out, _, _ = review_text(original)
                self.assertEqual(out, original)

    def test_diagnostico_nao_marca_parentesco_normal(self):
        self.assertEqual(diagnosticar_texto("Sua mãe se chama Vivian Wells."), [])
        self.assertEqual(diagnosticar_texto("Você é filho dela."), [])

    def test_review_file_reporta_alertas_sem_forcar_correcao(self):
        with tempfile.TemporaryDirectory() as td:
            root = Path(td)
            p = root / "traduzido.txt"
            original = '"Seu Mãe O nome de é Vivian Wells."\n"Você é filho dela."\n'
            p.write_text(original, encoding="utf-8")
            result = review_file(p, RPY_DIR)
            codigos = {x["code"] for x in result["linguistic_issues"]}
            self.assertIn("concordancia_possessivo", codigos)
            self.assertIn("ordem_nome_quebrada", codigos)
            self.assertEqual(len(result["linguistic_issues"]), 2)
            self.assertIn('"Você é filho dela."', p.read_text(encoding="utf-8"))

    def test_concordancia_moralidade_leve_com_tags(self):
        native = "{b}{color=#87e1fa}Light Morality{/color}{/b} increased by {size=+3}{b}{color=#2bff8b}3{/color}{/b}{/size}."
        translated = "{b}{color=#87e1fa}Moralidade Leve{/color}{/b} aumentado por {size=+3}{b}{color=#2bff8b}3{/color}{/b}{/size}."
        actual, changes = _correct_source_anchored_structures(native, translated)
        self.assertEqual(
            actual,
            "{b}{color=#87e1fa}Moralidade Leve{/color}{/b} aumentada por {size=+3}{b}{color=#2bff8b}3{/color}{/b}{/size}.",
        )
        self.assertEqual(changes, 1)
        self.assertEqual(
            [s.valor for s in segmentar(native) if s.tipo == "protegido"],
            [s.valor for s in segmentar(actual) if s.tipo == "protegido"],
        )

    def test_placeholder_possessivo_reordenado_com_base_no_old(self):
        native = "Looks like it's settled then, I agree with [mc]'s plan."
        translated = "Parece que está resolvido então, concordo com [mc] o plano de."
        actual, changes = _correct_source_anchored_structures(native, translated)
        self.assertEqual(actual, "Parece que está resolvido então, concordo com o plano de [mc].")
        self.assertEqual(changes, 1)

    def test_placeholder_possessivo_aceita_adjetivo_e_outro_nome(self):
        native = "I agree with [Pearl]'s detailed plan."
        translated = "concordo com [Pearl] o plano detalhado de."
        actual, changes = _correct_source_anchored_structures(native, translated)
        self.assertEqual(actual, "concordo com o plano detalhado de [Pearl].")
        self.assertEqual(changes, 1)

    def test_placeholder_nao_muda_sem_possessivo_no_original(self):
        native = "I agree with [mc] about the plan."
        translated = "concordo com [mc] o plano de."
        actual, changes = _correct_source_anchored_structures(native, translated)
        self.assertEqual(actual, translated)
        self.assertEqual(changes, 0)

    def test_moralidade_ja_feminina_permanece_igual(self):
        native = "Light Morality increased."
        translated = "Moralidade Leve{/color}{/b} aumentada."
        actual, changes = _correct_source_anchored_structures(native, translated)
        self.assertEqual(actual, translated)
        self.assertEqual(changes, 0)

    def test_idioma_dependente_da_cena_nao_e_reescrito(self):
        native = "The girls submit to your command, you succeeded in ordering them."
        translated = "As garotas se submetem às suas ordens, você conseguiu dar-lhes um jeito."
        actual, changes = _correct_source_anchored_structures(native, translated)
        self.assertEqual(actual, translated)
        self.assertEqual(changes, 0)

if __name__ == "__main__":
    unittest.main()
