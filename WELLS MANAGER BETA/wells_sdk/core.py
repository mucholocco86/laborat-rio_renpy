"""Shared adapter for the two Ren'Py 8.5.3 commands used by Wells SDK."""

from __future__ import annotations

import os
import re
import subprocess
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Callable, Optional


class WellsSdkError(RuntimeError):
    """A runtime, game-folder, or command validation error."""


@dataclass(frozen=True)
class OperationResult:
    operation: str
    command: tuple[str, ...]
    returncode: int
    stdout: str
    stderr: str
    output_path: Path


def bundled_runtime_root() -> Path:
    """Locate the curated SDK runtime in source and PyInstaller builds."""
    if getattr(sys, "frozen", False):
        return Path(sys._MEIPASS) / "wells_sdk" / "runtime"
    return Path(__file__).resolve().parent / "runtime"


def resolve_engine(runtime_root: os.PathLike | str | None = None) -> Path:
    root = Path(runtime_root) if runtime_root is not None else bundled_runtime_root()
    root = root.expanduser().resolve()
    engine = root / "renpy.exe"
    required = (
        engine,
        root / "renpy.py",
        root / "renpy" / "bootstrap.py",
        root / "lib" / "python3.12",
        root / "lib" / "py3-windows-x86_64" / "librenpython.dll",
    )
    missing = [str(path) for path in required if not path.exists()]
    if missing:
        raise WellsSdkError(
            "O runtime Ren'Py 8.5.3 empacotado está incompleto. Faltam: "
            + ", ".join(missing)
        )
    return engine


def validate_project(project_dir: os.PathLike | str) -> Path:
    project = Path(project_dir).expanduser().resolve()
    if not project.is_dir() or not (project / "game").is_dir():
        raise WellsSdkError("Selecione a pasta raiz do jogo, que deve conter 'game'.")
    return project


def _validate_language(language: str, *, allow_none: bool) -> str:
    value = (language or "").strip()
    if allow_none and (not value or value.lower() == "none"):
        return "None"
    if not value or not re.fullmatch(r"[A-Za-z0-9_]+", value):
        raise WellsSdkError("Informe um idioma válido usando letras, números e '_'.")
    return value


def build_command(
    project_dir: os.PathLike | str,
    operation: str,
    language: str,
    *,
    runtime_root: os.PathLike | str | None = None,
    empty_strings: bool = True,
    dialogue_format: str = "tab",
    include_strings: bool = False,
    strip_tags: bool = False,
    escape_special: bool = False,
) -> tuple[str, ...]:
    """Build the CLI call corresponding to the Ren'Py launcher controls."""
    engine = resolve_engine(runtime_root)
    project = validate_project(project_dir)

    if operation == "generate":
        language = _validate_language(language, allow_none=False)
        args = [str(engine), str(project), "translate", language]
        if language == "rot13":
            args.append("--rot13")
        elif language == "piglatin":
            args.append("--piglatin")
        elif empty_strings:
            args.append("--empty")
        return tuple(args)

    if operation == "extract":
        language = _validate_language(language, allow_none=True)
        if dialogue_format not in {"tab", "txt"}:
            raise WellsSdkError("Escolha dialogue.tab ou dialogue.txt.")
        args = [str(engine), str(project), "dialogue", language]
        if dialogue_format == "txt":
            args.append("--text")
        if include_strings:
            args.append("--strings")
        if strip_tags:
            args.append("--notags")
        if escape_special:
            args.append("--escape")
        return tuple(args)

    raise WellsSdkError("Operação desconhecida. Use 'generate' ou 'extract'.")


def expected_output(project_dir: os.PathLike | str, operation: str,
                    language: str, dialogue_format: str = "tab") -> Path:
    project = Path(project_dir).expanduser().resolve()
    if operation == "extract":
        return project / ("dialogue.txt" if dialogue_format == "txt" else "dialogue.tab")
    return project / "game" / "tl" / language


def run_operation(
    project_dir: os.PathLike | str,
    operation: str,
    language: str,
    *,
    runtime_root: os.PathLike | str | None = None,
    empty_strings: bool = True,
    dialogue_format: str = "tab",
    include_strings: bool = False,
    strip_tags: bool = False,
    escape_special: bool = False,
    timeout: Optional[float] = None,
    runner: Callable = subprocess.run,
) -> OperationResult:
    """Run an embedded Ren'Py command without a shell or launcher UI."""
    command = build_command(
        project_dir,
        operation,
        language,
        runtime_root=runtime_root,
        empty_strings=empty_strings,
        dialogue_format=dialogue_format,
        include_strings=include_strings,
        strip_tags=strip_tags,
        escape_special=escape_special,
    )
    engine = Path(command[0])
    kwargs = {
        "cwd": str(engine.parent),
        "text": True,
        "stdout": subprocess.PIPE,
        "stderr": subprocess.PIPE,
        "timeout": timeout,
        "check": False,
    }
    if os.name == "nt":
        kwargs["creationflags"] = getattr(subprocess, "CREATE_NO_WINDOW", 0)
    try:
        completed = runner(command, **kwargs)
    except (OSError, subprocess.TimeoutExpired) as exc:
        raise WellsSdkError(f"Não foi possível iniciar o Ren'Py: {exc}") from exc

    return OperationResult(
        operation=operation,
        command=command,
        returncode=completed.returncode,
        stdout=completed.stdout or "",
        stderr=completed.stderr or "",
        output_path=expected_output(project_dir, operation, language, dialogue_format),
    )

