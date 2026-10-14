# Executado a partir de WELLS MANAGER BETA:
# python -m PyInstaller --clean --noconfirm Wells_RenPy_Localization/Wells_RenPy_Localization.spec
from PyInstaller.utils.hooks import collect_submodules

hiddenimports = collect_submodules("Wells_RenPy_Localization")
a = Analysis(
    ["Wells_RenPy_Localization/standalone.py"],
    pathex=["."],
    binaries=[],
    datas=[],
    hiddenimports=hiddenimports,
    hookspath=[], hooksconfig={}, runtime_hooks=[], excludes=[],
    noarchive=False, optimize=0,
)
pyz = PYZ(a.pure)
exe = EXE(
    pyz, a.scripts, a.binaries, a.datas, [],
    name="Wells_RenPy_Localization", console=False,
    disable_windowed_traceback=False,
    argv_emulation=False, target_arch=None, codesign_identity=None,
    entitlements_file=None,
)
