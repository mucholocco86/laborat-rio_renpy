import json
import sys
import tempfile
import unittest
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
for folder in ('Wells_Revisor','Wells_Revisor_JSON'):
 sys.path.insert(0,str(ROOT/folder))
from wells_revisor_core import review_file
from wells_revisor_json_core import review_json_pair
from wells_blindagem import salvar_listas

class NameCaseTests(unittest.TestCase):
 def check_pair(self, native, translated, expected):
  for engine in ('rpy','json'):
   with self.subTest(engine=engine), tempfile.TemporaryDirectory() as td:
    p=Path(td); old=p/'old.txt';new=p/'new.txt';config=p/'blindagem.txt'
    old.write_text(json.dumps(native,ensure_ascii=False)+'\n',encoding='utf-8')
    new.write_text(json.dumps(translated,ensure_ascii=False)+'\n',encoding='utf-8')
    salvar_listas(config,{'NOMES_BLINDADOS':['Pearl','Eliza','Gaius','Rosá'], 'NOMES_TRADUZIVEIS':['Commander']})
    before=old.read_bytes()
    def run():
     if engine=='rpy':return review_file(new,ROOT/'Wells_Revisor',native_path=old,blindagem_path=config)
     return review_json_pair(old,new,ROOT/'Wells_Revisor_JSON',blindagem_path=config)
    run()
    self.assertEqual(json.loads(new.read_text()),expected)
    self.assertEqual(old.read_bytes(),before)
    run()
    self.assertEqual(json.loads(new.read_text()),expected)
 def test_existing_shout_tags(self):self.check_pair('{b}ELIZA!!{/b}','{b}ELIZA!!{/b}','{b}ELIZA!!{/b}')
 def test_normal_name(self):self.check_pair('Pearl','Pérola','Pearl')
 def test_native_shout(self):self.check_pair('PEARL','Pérola','PEARL')
 def test_translated_shout(self):self.check_pair('Pearl','PÉROLA','PEARL')
 def test_composite_shout(self):self.check_pair('Commander GAIUS!','Comandante CAIO!','Comandante GAIUS!')
 def test_normal_composite(self):self.check_pair('Commander Gaius','Comandante Caio','Comandante Gaius')
 def test_accented_existing(self):self.check_pair('{b}ROSÁ!{/b}','{b}ROSÁ!{/b}','{b}ROSÁ!{/b}')
 def test_mixed_occurrences(self):self.check_pair('Pearl, PEARL!', 'Pearl, PEARL!', 'Pearl, PEARL!')
