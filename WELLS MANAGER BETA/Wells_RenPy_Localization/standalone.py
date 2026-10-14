"""Direct Python entry point for the individual application."""

from pathlib import Path
import sys

parent = str(Path(__file__).resolve().parent.parent)
if parent not in sys.path:
    sys.path.insert(0, parent)

from Wells_RenPy_Localization.ui import run_standalone


if __name__ == "__main__":
    run_standalone()
