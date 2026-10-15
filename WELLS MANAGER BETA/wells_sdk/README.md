# Wells SDK — Ren'Py 8.5.3

This package exposes only two Ren'Py operations through a Wells interface:

- **Generate Translations** (`translate <language>`, with optional `--empty`).
- **Extract Dialogue** (`dialogue <language>`, with tab/text output and the SDK's string, tag, and escape options).

The same `core.py` is used by the standalone application and by Wells Manager. The application runs the curated Windows Ren'Py runtime bundled under `runtime/`; it does not ask the user to install or select an SDK.

## Current state

The runtime directory is assembled from Ren'Py 8.5.3 files. Keep the runtime's upstream license and applicable third-party notices alongside the packaged files. The launcher, documentation, tutorial games, updater, mobile build tools, and other SDK workflows are not part of the Wells interface.

## Current validation status

Verified in GitHub Actions on Windows (`windows-latest`, Python 3.11): six Wells SDK unit tests pass; the embedded Ren'Py 8.5.3 runtime produces the same generated `.rpy` files and `dialogue.tab` as the full SDK on the bundled `the_question` fixture; original `.rpy` scripts remain unchanged; standalone and integrated executables build successfully.

Manual Windows tests reported by the user: the integrated Wells Manager generated translation files for two games (one made with Ren'Py 8.5.3 and one with 7.4.11; the user did not specify which game used each version), extracted `dialogue.tab` and `dialogue.txt` from the Nephilim game, and the standalone `Wells_SDK.exe` also worked well. Extraction-option comparisons and selected-language extraction were also tested on the user's game.

Status: the two interfaces and both operations are working in the cases tested. This is not a universal compatibility guarantee for every Ren'Py project/version. The latest Windows build and comparison are recorded in [GitHub Actions run 38649626606](https://github.com/mucholocco86/laborat-rio_renpy/actions/runs/38649626606).

## Development

From `WELLS MANAGER BETA`:

```text
python -m wells_sdk
python -m unittest discover -s wells_sdk/tests -p "test_*.py" -v
```

The standalone PyInstaller spec is `wells_sdk/Wells_SDK.spec`. The integrated Wells Manager build uses `Wells_Manager.spec` and includes the same `wells_sdk` package.

The Ren'Py engine is responsible for reading project scripts and their translation state. This package intentionally invokes the Ren'Py command line in the embedded runtime instead of duplicating the engine's parser or translation-generation logic.

