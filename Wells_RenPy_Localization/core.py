"""Shared command adapter for Ren'Py 8.5.3 localization tools.

The extraction and generation algorithms remain Ren'Py's own registered CLI
commands. This module deliberately calls the engine without opening the SDK
launcher UI, so both Wells frontends use the same behavior and output format.
"""

from __future__ import annotations

import os
import platform
import re
import subprocess
from dataclasses import dataclass
from pathlib import Path
from typing import Callable, Optional


class RenPyToolsError(RuntimeError):
    """Raised when the SDK, project, or command is not usable."""


@dataclass(frozen=True)
class OperationResult:
    operation: str
    command: tuple[str, ...]
    returncode: int
    stdout: str
    stderr: str
    outputs: tuple[Path, ...]


def resolve_engine(sdk_or_engine: os.PathLike | str) -> Path:
    """Resolve an SDK directory or an explicit Ren'Py executable/script."""
    selected = Path(sdk_or_engine).expanduser().resolve()
    if selected.is_file():
        return selected
    if not selected.is_dir():
        raise RenPyToolsError("Selecione a pasta do SDK Ren'Py ou o executável do engine.")

    candidates = []
    if os.name == "nt":
        candidates = [selected / "renpy.exe", selected / "lib" / "py3-windows-x86_64" / "renpy.exe"]
    elif platform.system() == "Darwin":
        candidates = [selected / "renpy.app" / "Contents" / "MacOS" / "renpy", selected / "renpy.sh"]
    else:
        candidates = [selected / "renpy.sh", selected / "renpy"]

    for candidate in candidates:
        if candidate.is_file():
            return candidate.resolve()
    raise RenPyToolsError("Não encontrei o executável do Ren'Py nesta pasta do SDK.")


def validate_project(project_dir: os.PathLike | str) -> Path:
    project = Path(project_dir).expanduser().resolve()
    if not project.is_dir():
        raise RenPyToolsError("Selecione a pasta raiz do jogo Ren'Py.")
    if not (project / "game").is_dir():
        raise RenPyToolsError("A pasta selecionada precisa conter uma subpasta 'game'.")
    return project


def build_command(engine: os.PathLike | str, project_dir: os.PathLike | str,
                  operation: str, language: str, *, empty_strings: bool = True,
                  dialogue_format: str = "tab", include_strings: bool = False,
                  strip_tags: bool = False, escape_special: bool = False) -> tuple[str, ...]:
    """Build the exact CLI arguments used by the SDK launcher for these tasks."""
    engine_path = resolve_engine(engine)
    project = validate_project(project_dir)
    language = (language or "").strip()
    if operation == "extract" and language.lower() == "none":
        language = "None"
    if not language:
        raise RenPyToolsError("Informe o idioma/localização, por exemplo: brazil.")
    if language != "None" and not re.fullmatch(r"[a-z0-9_]+", language):
        raise RenPyToolsError("Use somente letras minúsculas, números e sublinhados no idioma.")

    args = [str(engine_path), str(project)]
    if operation == "generate":
        args += ["translate", language]
        if language == "rot13":
            args.append("--rot13")
        elif language == "piglatin":
            args.append("--piglatin")
        elif empty_strings:
            args.append("--empty")
    elif operation == "extract":
        if dialogue_format not in {"tab", "txt"}:
            raise RenPyToolsError("Formato de extração inválido.")
        args += ["dialogue", language]
        if dialogue_format == "txt":
            args.append("--text")
        if include_strings:
            args.append("--strings")
        if strip_tags:
            args.append("--notags")
        if escape_special:
            args.append("--escape")
    else:
        raise RenPyToolsError("Operação Ren'Py desconhecida.")
    return tuple(args)


def expected_outputs(project_dir: os.PathLike | str, operation: str,
                     language: str, dialogue_format: str = "tab") -> tuple[Path, ...]:
    project = Path(project_dir).expanduser().resolve()
    if operation == "extract":
        return (project / ("dialogue.txt" if dialogue_format == "txt" else "dialogue.tab"),)
    # Ren'Py may distribute the generated scripts across subdirectories under
    # this locale. Returning the locale folder avoids guessing the file list.
    return (project / "game" / "tl" / language,)


def run_operation(engine: os.PathLike | str, project_dir: os.PathLike | str,
                  operation: str, language: str, *, empty_strings: bool = True,
                  dialogue_format: str = "tab", include_strings: bool = False,
                  strip_tags: bool = False, escape_special: bool = False,
                  timeout: Optional[float] = None,
                  on_output: Optional[Callable[[str], None]] = None) -> OperationResult:
    """Run Ren'Py's headless command; never invokes a shell or edits .rpy files."""
    cmd = build_command(
        engine, project_dir, operation, language,
        empty_strings=empty_strings, dialogue_format=dialogue_format,
        include_strings=include_strings, strip_tags=strip_tags,
        escape_special=escape_special,
    )
    engine_path = Path(cmd[0])
    try:
        completed = subprocess.run(
            cmd, cwd=str(engine_path.parent), text=True,
            stdout=subprocess.PIPE, stderr=subprocess.PIPE,
            timeout=timeout, check=False,
        )
    except (OSError, subprocess.TimeoutExpired) as exc:
        raise RenPyToolsError(f"Não foi possível executar o Ren'Py: {exc}") from exc
    if on_output:
        if completed.stdout:
            on_output(completed.stdout)
        if completed.stderr:
            on_output(completed.stderr)
    return OperationResult(
        operation=operation,
        command=cmd,
        returncode=completed.returncode,
        stdout=completed.stdout,
        stderr=completed.stderr,
        outputs=expected_outputs(project_dir, operation, language, dialogue_format),
    )
