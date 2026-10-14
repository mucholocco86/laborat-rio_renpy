# -*- mode: python ; coding: utf-8 -*-
from pathlib import Path

root = Path.cwd().resolve()

a = Analysis(
    [str(root / "wells_sdk" / "standalone.py")],
    pathex=[str(root)],
    binaries=[],
    datas=[
        (str(root / "wells_sdk" / "runtime"), "wells_sdk/runtime"),
        (str(root / "wells.ico"), "."),
    ],
    hiddenimports=[],
    hookspath=[], hooksconfig={}, runtime_hooks=[], excludes=[],
    noarchive=False, optimize=0,
)
pyz = PYZ(a.pure)
exe = EXE(
    pyz, a.scripts, a.binaries, a.datas, [],
    name="Wells_SDK", debug=False, bootloader_ignore_signals=False,
    strip=False, upx=False, console=False, icon=str(root / "wells.ico"),
)

