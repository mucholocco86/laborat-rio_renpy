# -*- coding: utf-8 -*-
import ast
import json
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
sys.path.insert(0, str(ROOT / "Wells_Revisor"))

from Wells_Translator.wells_translator_core import (
    MAP_FILENAME, _collect_txt_pair, _collect_docx_pair, _read_txt_records,
    _read_docx_records, _write_txt_records, _write_docx_records,
    export_full, export_blocks, export_full_docx, export_blocks_docx,
    inject_translations, inject_docx_translations, scan_tl,
)
from wells_revisor_core import review_file


SOURCE = '''translate brazil strings:
    old "Welcome, \\"Traveler\\"! [name]\\nNext line"
    new "Bem-vindo, \\"Viajante\\"! [name]\\nPróxima linha"

translate brazil dialogue_001:
    # e "He said, \\"go\\", [player]!"
    e "Ele disse, \\"vá\\", [player]!"
'''


class WellsTranslatorPlainMapTests(unittest.TestCase):
    def make_project(self, root):
        game = root / "game"
        tl = game / "tl" / "brazil"
        tl.mkdir(parents=True)
        (game / "script.rpy").write_text('label start:\\n    "untouched"\\n', encoding="utf-8")
        source = tl / "common.rpy"
        source.write_text(SOURCE, encoding="utf-8")
        return game, tl, source

    def test_txt_full_export_and_injection_rebuilds_renpy_strings(self):
        with tempfile.TemporaryDirectory() as td:
            root = Path(td)
            game, tl, source = self.make_project(root)
            untouched = (game / "script.rpy").read_bytes()
            out = root / "work"
            out.mkdir()
            export_full(tl, out)
            self.assertTrue((out / MAP_FILENAME).is_file())
            old, new, _ = _collect_txt_pair(out)
            self.assertEqual(len(old), 2)
            self.assertEqual(old[0], r'Welcome, "Traveler"! [name]\nNext line')
            self.assertFalse(old[0].startswith('"'))
            new[0] = r'Bem-vindo, "Viajante"! [name]\nLinha final'
            new[1] = 'Ele disse, "vá" para [player]!'
            _write_txt_records(out / "new.txt", new)

            count, _ = inject_translations(tl, out)
            self.assertEqual(count, 2)
            self.assertEqual((game / "script.rpy").read_bytes(), untouched)
            result = (source.read_text(encoding="utf-8"))
            self.assertIn(r'new "Bem-vindo, \"Viajante\"! [name]\nLinha final"', result)
            self.assertIn(r'e "Ele disse, \"vá\" para [player]!"', result)
            self.assertEqual(len(scan_tl(tl)[1]), 2)

    def test_plain_records_inject_without_sidecar_map(self):
        with tempfile.TemporaryDirectory() as td:
            root = Path(td)
            _, tl, source = self.make_project(root)
            out = root / "work"
            out.mkdir()
            export_full(tl, out)
            (out / MAP_FILENAME).unlink()

            old, new, _ = _collect_txt_pair(out)
            self.assertFalse(old[0].startswith('"'))
            new[0] = r'Bem-vindo, "Viajante"! [name] e \\n'
            new[1] = 'Ele disse, "vá" para [player]!'
            _write_txt_records(out / "new.txt", new)

            count, _ = inject_translations(tl, out)
            self.assertEqual(count, 2)
            result = source.read_text(encoding="utf-8")
            self.assertIn(r'new "Bem-vindo, \\"Viajante\\"! [name] e \\\\n"', result)
            self.assertIn(r'e "Ele disse, \\"vá\\" para [player]!"', result)

    def test_docx_blocks_and_txt_blocks_share_the_same_plain_records(self):
        for exporter, collector, injector in (
            (export_blocks, _collect_txt_pair, inject_translations),
            (export_blocks_docx, _collect_docx_pair, inject_docx_translations),
        ):
            with self.subTest(exporter=exporter.__name__), tempfile.TemporaryDirectory() as td:
                root = Path(td)
                _, tl, source = self.make_project(root)
                out = root / "work"
                out.mkdir()
                if exporter is export_blocks:
                    exporter(tl, out, max_bytes=1)
                else:
                    exporter(tl, out, max_file_bytes=1)
                old, new, _ = collector(out)
                self.assertEqual(len(old), 2)
                self.assertEqual(len(new), 2)
                self.assertTrue(all(not line.startswith('"') for line in old))
                self.assertTrue((out / MAP_FILENAME).is_file())
                new[0] = 'Nova fala com "aspas" e [name]'
                new[1] = "Outra fala para [player]"
                paths = sorted(out.glob("new_*.txt" if collector is _collect_txt_pair else "new_*.docx"),
                               key=lambda p: int(p.stem.split("_")[1]))
                split = 0
                for path in paths:
                    records = (_read_txt_records(path) if collector is _collect_txt_pair else _read_docx_records(path))
                    updated = new[split:split + len(records)]
                    split += len(records)
                    if collector is _collect_txt_pair:
                        _write_txt_records(path, updated)
                    else:
                        _write_docx_records(path, updated)
                self.assertEqual(injector(tl, out)[0], 2)
                self.assertIn(r'\"aspas\"', source.read_text(encoding="utf-8"))

    def test_changed_tl_or_old_record_cancels_before_injection(self):
        with tempfile.TemporaryDirectory() as td:
            root = Path(td)
            _, tl, source = self.make_project(root)
            out = root / "work"
            out.mkdir()
            export_full(tl, out)
            old, new, _ = _collect_txt_pair(out)
            old[0] += " adulterado"
            _write_txt_records(out / "old.txt", old)
            with self.assertRaisesRegex(ValueError, "OLD divergente"):
                inject_translations(tl, out)
            old[0] = old[0].replace(" adulterado", "")
            _write_txt_records(out / "old.txt", old)
            before = source.read_bytes()
            source.write_text(SOURCE + "# changed\\n", encoding="utf-8")
            changed = source.read_bytes()
            with self.assertRaisesRegex(ValueError, "mudou desde a extração"):
                inject_translations(tl, out)
            self.assertEqual(source.read_bytes(), changed)
            self.assertNotEqual(before, changed)

    def test_revisor_accepts_plain_old_new_pair_and_keeps_it_plain(self):
        for suffix, writer, reader in (
            ("txt", _write_txt_records, _read_txt_records),
            ("docx", _write_docx_records, _read_docx_records),
        ):
            with self.subTest(format=suffix), tempfile.TemporaryDirectory() as td:
                root = Path(td)
                old = root / f"old.{suffix}"
                new = root / f"new.{suffix}"
                writer(old, ["Hello [name]!"])
                writer(new, ["Olá , [name]!"])
                result = review_file(new, ROOT / "Wells_Revisor", native_path=old, plain_records=True)
                self.assertEqual(result["records"], 1)
                reviewed = reader(new)
                self.assertEqual(reviewed, ["Olá, [name]!"])
                self.assertFalse(reviewed[0].startswith('"'))


if __name__ == "__main__":
    unittest.main()

