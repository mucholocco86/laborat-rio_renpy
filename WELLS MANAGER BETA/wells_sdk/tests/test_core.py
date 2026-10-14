import tempfile
import unittest
from pathlib import Path
from types import SimpleNamespace

from wells_sdk.core import WellsSdkError, build_command, run_operation


class CoreTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.root = Path(self.temp.name)
        self.runtime = self.root / "runtime"
        (self.runtime / "renpy").mkdir(parents=True)
        (self.runtime / "lib" / "python3.12").mkdir(parents=True)
        (self.runtime / "lib" / "py3-windows-x86_64").mkdir(parents=True)
        for item in (
            self.runtime / "renpy.exe",
            self.runtime / "renpy.py",
            self.runtime / "renpy" / "bootstrap.py",
            self.runtime / "lib" / "py3-windows-x86_64" / "librenpython.dll",
        ):
            item.touch()
        self.project = self.root / "game_project"
        (self.project / "game").mkdir(parents=True)

    def tearDown(self):
        self.temp.cleanup()

    def test_generate_uses_empty_flag_by_default(self):
        command = build_command(self.project, "generate", "english", runtime_root=self.runtime)
        self.assertEqual(command[2:], ("translate", "english", "--empty"))

    def test_generate_respects_empty_checkbox_and_special_language(self):
        no_empty = build_command(self.project, "generate", "english", runtime_root=self.runtime,
                                 empty_strings=False)
        rot13 = build_command(self.project, "generate", "rot13", runtime_root=self.runtime)
        self.assertEqual(no_empty[-2:], ("translate", "english"))
        self.assertEqual(rot13[-2:], ("rot13", "--rot13"))

    def test_extract_builds_launcher_equivalent_arguments(self):
        command = build_command(
            self.project, "extract", "None", runtime_root=self.runtime,
            dialogue_format="txt", include_strings=True, strip_tags=True, escape_special=True,
        )
        self.assertEqual(
            command[2:],
            ("dialogue", "None", "--text", "--strings", "--notags", "--escape"),
        )

    def test_extract_blank_language_uses_default_language(self):
        command = build_command(self.project, "extract", "", runtime_root=self.runtime)
        self.assertEqual(command[2:], ("dialogue", "None"))

    def test_run_operation_reports_command_result_and_output(self):
        calls = []

        def fake_runner(command, **kwargs):
            calls.append((command, kwargs))
            return SimpleNamespace(returncode=0, stdout="ok", stderr="")

        result = run_operation(self.project, "extract", "None", runtime_root=self.runtime,
                               runner=fake_runner)
        self.assertEqual(result.returncode, 0)
        self.assertEqual(result.stdout, "ok")
        self.assertEqual(result.output_path, self.project / "dialogue.tab")
        self.assertEqual(calls[0][0], result.command)
        self.assertEqual(calls[0][1]["cwd"], str(self.runtime.resolve()))

    def test_invalid_project_and_format_fail_before_running(self):
        with self.assertRaises(WellsSdkError):
            build_command(self.root, "extract", "None", runtime_root=self.runtime)
        with self.assertRaises(WellsSdkError):
            build_command(self.project, "extract", "None", runtime_root=self.runtime,
                          dialogue_format="csv")


if __name__ == "__main__":
    unittest.main()

