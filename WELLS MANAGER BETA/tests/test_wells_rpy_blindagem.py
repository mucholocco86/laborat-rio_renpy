import json
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'Wells_Revisor'))
from wells_revisor_core import review_file
from wells_blindagem import salvar_listas
from Wells_Translator.wells_translator_core import (
    export_full, export_blocks, export_full_docx, export_blocks_docx,
    inject_translations, inject_docx_translations,
)

class RpyBlindagemTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.config = self.root / 'blindagem.txt'
        salvar_listas(self.config, {
            'NOMES_BLINDADOS': ['Dalen', 'Gaius', 'Pearl', 'Kira', 'Geskir', 'General Geskir'],
            'NOMES_TRADUZIVEIS': ['Commander', 'and'],
        })

    def run_pair(self, native, translated):
        old = self.root / 'old.txt'
        new = self.root / 'new.txt'
        old.write_text('\n'.join(json.dumps(x, ensure_ascii=False) for x in native)+'\n')
        new.write_text('\n'.join(json.dumps(x, ensure_ascii=False) for x in translated)+'\n')
        before = old.read_bytes()
        stats = review_file(new, ROOT/'Wells_Revisor', native_path=old, blindagem_path=self.config)
        self.assertEqual(old.read_bytes(), before)
        return [json.loads(x) for x in new.read_text().splitlines()], stats

    def test_names_and_ambiguous_dialogue(self):
        out, stats = self.run_pair(
            ['Dalen', 'Commander Gaius', 'Pearl and Kira', 'Commander Gaius arrives'],
            ['O Vale', 'Comandante Caio', 'Pérola e Kira', 'Comandante Caio chega'])
        self.assertEqual(out, ['Dalen', 'Comandante Gaius', 'Pearl e Kira', 'Comandante Caio chega'])
        self.assertEqual(stats['reconstructed_names'], 3)
        self.assertEqual(len(stats['unresolved_names']), 1)

    def test_overlapping_names_do_not_report_false_missing(self):
        out, stats = self.run_pair(['General Geskir'], ['General Geskir'])
        self.assertEqual(out, ['General Geskir'])
        self.assertEqual(stats['unresolved_names'], [])

    def test_renpy_identifiers_remain_unchanged(self):
        out, _ = self.run_pair(['Gaius [gaius] {i}'], ['gaius [gaius] {i}'])
        self.assertEqual(out, ['Gaius [gaius] {i}'])

    def test_mismatched_counts_do_not_write(self):
        old=self.root/'old.txt'; new=self.root/'new.txt'
        old.write_text('"Dalen"\n');new.write_text('"O Vale"\n"Extra"\n')
        before=new.read_bytes()
        with self.assertRaises(ValueError):
            review_file(new, ROOT/'Wells_Revisor', native_path=old, blindagem_path=self.config)
        self.assertEqual(new.read_bytes(),before)

    def test_invalid_record_do_not_write(self):
        old=self.root/'old.txt';new=self.root/'new.txt'
        old.write_text('"Dalen"\n');new.write_text('"unterminated\n')
        before=new.read_bytes()
        with self.assertRaises(ValueError):
            review_file(new,ROOT/'Wells_Revisor',native_path=old,blindagem_path=self.config)
        self.assertEqual(new.read_bytes(),before)

    def test_empty_lists_do_not_restore(self):
        salvar_listas(self.config, {})
        out, stats=self.run_pair(['Dalen'],['O Vale'])
        self.assertEqual(out,['O Vale'])
        self.assertEqual(stats['protected_names'],0)

    def test_conflict_is_reported_without_priority(self):
        salvar_listas(self.config, {'NOMES_BLINDADOS':['Dalen'],'NOMES_TRADUZIVEIS':['Dalen']})
        out, stats=self.run_pair(['Dalen'],['O Vale'])
        self.assertEqual(out,['O Vale'])
        self.assertEqual(stats['conflict_records'],1)

    def test_pipeline_txt_docx_full_and_blocks(self):
        for fmt, blocks in [('txt',False),('txt',True),('docx',False),('docx',True)]:
            with self.subTest(fmt=fmt,blocks=blocks):
                tl=self.root/(fmt+str(blocks));tl.mkdir()
                script=tl/'strings.rpy'
                source='translate brazil strings:\n    old "Dalen"\n    new "O Vale"\n    old "Commander Gaius"\n    new "Comandante Caio"\n'
                script.write_text(source)
                work=tl/'work';work.mkdir()
                if fmt=='txt':
                    result=(export_blocks(tl,work,max_bytes=10,return_session=True) if blocks else export_full(tl,work,return_session=True))
                else:
                    result=(export_blocks_docx(tl,work,max_file_bytes=1,return_session=True) if blocks else export_full_docx(tl,work,return_session=True))
                for new in work.glob('new*.'+fmt):
                    old=new.with_name('old'+new.name[3:]);before=old.read_bytes()
                    review_file(new,ROOT/'Wells_Revisor',native_path=old,blindagem_path=self.config)
                    self.assertEqual(old.read_bytes(),before)
                injector=inject_translations if fmt=='txt' else inject_docx_translations
                injector(tl,work,session=result[-1])
                actual=script.read_text()
                self.assertEqual(actual,source.replace('new "O Vale"','new "Dalen"').replace('new "Comandante Caio"','new "Comandante Gaius"'))

if __name__=='__main__':
    unittest.main()
