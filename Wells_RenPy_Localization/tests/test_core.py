import tempfile
import unittest
import os
from pathlib import Path

from Wells_RenPy_Localization.core import RenPyToolsError, build_command, expected_outputs


class CommandBuilderTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.root = Path(self.temp.name)
        self.sdk = self.root / "sdk"
        self.sdk.mkdir()
        (self.sdk / ("renpy.exe" if os.name == "nt" else "renpy.sh")).touch()
        self.project = self.root / "game-project"
        (self.project / "game").mkdir(parents=True)

    def tearDown(self):
        self.temp.cleanup()

    def test_generation_matches_sdk_command_and_empty_flag(self):
        command = build_command(self.sdk, self.project, "generate", "brazil", empty_strings=True)
        self.assertEqual(command[-3:], ("translate", "brazil", "--empty"))

    def test_generation_can_leave_strings_uninitialized(self):
        command = build_command(self.sdk, self.project, "generate", "brazil", empty_strings=False)
        self.assertEqual(command[-2:], ("translate", "brazil"))

    def test_dialogue_options_keep_sdk_flag_names(self):
        command = build_command(
            self.sdk, self.project, "extract", "None", dialogue_format="txt",
            include_strings=True, strip_tags=True, escape_special=True,
        )
        self.assertEqual(command[-5:], ("None", "--text", "--strings", "--notags", "--escape"))

    def test_paths_are_required(self):
        with self.assertRaises(RenPyToolsError):
            build_command(self.sdk, self.root, "extract", "None")

    def test_output_contract(self):
        self.assertEqual(expected_outputs(self.project, "extract", "None", "tab"),
                         (self.project / "dialogue.tab",))
        self.assertEqual(expected_outputs(self.project, "generate", "brazil"),
                         (self.project / "game" / "tl" / "brazil",))


if __name__ == "__main__":
    unittest.main()
