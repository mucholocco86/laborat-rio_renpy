# Wells SDK — Ren'Py 8.5.3

This package exposes only two Ren'Py operations through a Wells interface:

- **Generate Translations** (`translate <language>`, with optional `--empty`).
- **Extract Dialogue** (`dialogue <language>`, with tab/text output and the SDK's string, tag, and escape options).

The same `core.py` is used by the standalone application and by Wells Manager. The application runs the curated Windows Ren'Py runtime bundled under `runtime/`; it does not ask the user to install or select an SDK.

## Current state

The runtime directory is assembled from Ren'Py 8.5.3 files. Keep the runtime's upstream license and applicable third-party notices alongside the packaged files. The launcher, documentation, tutorial games, updater, mobile build tools, and other SDK workflows are not part of the Wells interface.

## Development

From `WELLS MANAGER BETA`:

```text
python -m wells_sdk
python -m unittest discover -s wells_sdk/tests -p "test_*.py" -v
```

The standalone PyInstaller spec is `wells_sdk/Wells_SDK.spec`. The integrated Wells Manager build uses `Wells_Manager.spec` and includes the same `wells_sdk` package.

The Ren'Py engine is responsible for reading project scripts and their translation state. This package intentionally invokes the Ren'Py command line in the embedded runtime instead of duplicating the engine's parser or translation-generation logic.

