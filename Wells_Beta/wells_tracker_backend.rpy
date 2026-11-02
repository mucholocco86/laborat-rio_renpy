## Wells visual checkpoint — independent JSON route recorder/rebuilder.
## Choice values are collected from Ren'Py's native menu return values.
## This module does not import URM or Timeline code.

default wells_tracker_choices = []
default wells_tracker_replay = None

default wells_tracker_notice = None

init -100 python:
    import io
    import json
    import os
    import time

    WELLS_TRACKER_DIR = os.path.join(renpy.config.gamedir, "saves", "wells_tracker")
    WELLS_TRACKER_PENDING = os.path.join(WELLS_TRACKER_DIR, "pending_load.txt")
    WELLS_TRACKER_VERSION = 3
    WELLS_TRACKER_MAX_DEPTH = 8
    WELLS_TRACKER_MAX_ITEMS = 1000

    try:
        if not os.path.isdir(WELLS_TRACKER_DIR):
            os.makedirs(WELLS_TRACKER_DIR)
    except Exception:
        pass

    try:
        WELLS_TRACKER_STRING_TYPES = (basestring,)
    except NameError:
        WELLS_TRACKER_STRING_TYPES = (str,)

    try:
        WELLS_TRACKER_INTEGER_TYPES = (int, long)
    except NameError:
        WELLS_TRACKER_INTEGER_TYPES = (int,)

    WELLS_TRACKER_SCALAR_TYPES = WELLS_TRACKER_STRING_TYPES + WELLS_TRACKER_INTEGER_TYPES + (float, bool, type(None))

    def _wells_tracker_text(value):
        try:
            if isinstance(value, unicode):
                return value
        except NameError:
            pass
        try:
            return str(value)
        except Exception:
            return ""

    def _wells_tracker_is_valid_game_script(filename):
        """Accept original game scripts only; never treat TL or Wells modules as game source."""
        if not isinstance(filename, WELLS_TRACKER_STRING_TYPES):
            return False
        try:
            path = os.path.normpath(_wells_tracker_text(filename)).replace("\\", "/").lower()
            parts = [part for part in path.split("/") if part]
            game_indexes = [index for index, part in enumerate(parts) if part == "game"]
            if not game_indexes:
                return False
            relative = parts[game_indexes[-1] + 1:]
            if not relative or relative[0] in ("tl", "wells"):
                return False
            if "tl" in relative:
                return False
            return relative[-1].endswith((".rpy", ".rpyc"))
        except Exception:
            return False

    def _wells_tracker_json_value(value, depth=0):
        """Copy only plain JSON data; never pickle or inspect arbitrary objects."""
        if isinstance(value, WELLS_TRACKER_SCALAR_TYPES):
            return value
        if depth >= WELLS_TRACKER_MAX_DEPTH:
            return None
        if isinstance(value, (list, tuple)):
            result = []
            for item in value[:WELLS_TRACKER_MAX_ITEMS]:
                clean = _wells_tracker_json_value(item, depth + 1)
                if clean is not None or item is None:
                    result.append(clean)
                else:
                    return None
            return result
        if isinstance(value, dict):
            result = {}
            count = 0
            try:
                for key, item in value.items():
                    count += 1
                    if count > WELLS_TRACKER_MAX_ITEMS:
                        return None
                    if not isinstance(key, WELLS_TRACKER_STRING_TYPES + WELLS_TRACKER_INTEGER_TYPES):
                        return None
                    clean = _wells_tracker_json_value(item, depth + 1)
                    if clean is None and item is not None:
                        return None
                    result[_wells_tracker_text(key)] = clean
            except Exception:
                return None
            return result
        return None

    def _wells_tracker_image_name(entry):
        name = getattr(entry, "name", None)
        if not name:
            try:
                name = entry[5]
            except Exception:
                name = None
        if isinstance(name, (list, tuple)):
            return " ".join([_wells_tracker_text(part) for part in name])
        return _wells_tracker_text(name) if name else None

    def _wells_tracker_current_entry():
        try:
            context = renpy.game.context()
            entries = getattr(getattr(context, "scene_lists", None), "layers", {}).get("master", [])
            latest = None
            latest_time = None
            for entry in entries:
                if not _wells_tracker_image_name(entry):
                    continue
                shown_at = getattr(entry, "show_time", None)
                if latest is None or shown_at is None or latest_time is None or shown_at >= latest_time:
                    latest = entry
                    latest_time = shown_at
            return latest
        except Exception:
            return None

    def _wells_tracker_asset(entry):
        """Resolve a file path from the active displayable when Ren'Py exposes one."""
        extensions = (".png", ".jpg", ".jpeg", ".webp", ".webm", ".avif")
        queue = []
        try:
            displayable = getattr(entry, "displayable", None)
            if displayable is not None:
                queue.append(displayable)
                try:
                    name = getattr(entry, "name", None)
                    registered = renpy.get_registered_image(name) if name else None
                    if registered is not None:
                        queue.append(registered)
                except Exception:
                    pass
        except Exception:
            pass

        seen = set()
        while queue:
            current = queue.pop(0)
            if current is None or id(current) in seen or len(seen) >= 80:
                continue
            seen.add(id(current))
            for attr in ("filename", "fn", "file"):
                try:
                    value = getattr(current, attr, None)
                    if isinstance(value, WELLS_TRACKER_STRING_TYPES) and value.lower().endswith(extensions):
                        return _wells_tracker_text(value)
                except Exception:
                    pass
            for attr in ("target", "child", "image", "d", "displayable"):
                try:
                    child = getattr(current, attr, None)
                    if child is not None and child is not current:
                        queue.append(child)
                except Exception:
                    pass
        return None

    def _wells_tracker_current_node():
        """Return script location as a diagnostic/secondary image-anchor clue."""
        candidates = []
        try:
            context = renpy.game.context()
            candidates.append(getattr(context, "current", None))
        except Exception:
            pass
        try:
            current = getattr(renpy.game.log, "current", None)
            rollback_context = getattr(current, "context", None)
            candidates.append(getattr(rollback_context, "current", None))
        except Exception:
            pass
        for node in candidates:
            if node is None:
                continue
            if not getattr(node, "filename", None):
                try:
                    node = renpy.game.script.lookup(node)
                except Exception:
                    continue
            filename = getattr(node, "filename", None)
            linenumber = getattr(node, "linenumber", None)
            if filename and _wells_tracker_is_valid_game_script(filename):
                return {
                    "file": _wells_tracker_text(filename),
                    "line": linenumber,
                    "name": _wells_tracker_json_value(getattr(node, "name", None)),
                }
        return None

    def _wells_tracker_current_anchor():
        entry = _wells_tracker_current_entry()
        if entry is None:
            return None
        image_name = _wells_tracker_image_name(entry)
        if not image_name:
            return None
        return {
            "image_name": image_name,
            "asset_file": _wells_tracker_asset(entry),
            "script_node": _wells_tracker_current_node(),
        }

    def _wells_tracker_read_json(filename):
        path = os.path.join(WELLS_TRACKER_DIR, filename)
        with io.open(path, "r", encoding="utf-8") as stream:
            return json.load(stream)

    def _wells_tracker_write_json(filename, payload):
        path = os.path.join(WELLS_TRACKER_DIR, filename)
        temp_path = path + ".tmp"
        serialized = json.dumps(payload, ensure_ascii=False, indent=2, sort_keys=True)
        try:
            if not isinstance(serialized, unicode):
                serialized = serialized.decode("utf-8")
        except NameError:
            pass
        with io.open(temp_path, "w", encoding="utf-8") as stream:
            stream.write(serialized)
        if os.path.exists(path):
            os.remove(path)
        os.rename(temp_path, path)

    def _wells_tracker_changed_roots():
        """Read Ren'Py's native changed-root set; never scan dir(store)."""
        roots = None
        try:
            getter = getattr(renpy.game.log, "get_roots", None)
            if callable(getter):
                roots = getter()
        except Exception:
            roots = None

        if roots is None:
            roots = {}
            try:
                for store_name, store_dict in renpy.python.store_dicts.items():
                    changed = getattr(store_dict, "ever_been_changed", ())
                    for name in changed:
                        if name in store_dict:
                            roots[store_name + "." + name] = store_dict[name]
            except Exception:
                pass
        return roots

    def wells_tracker_collect_variables():
        """Serialize public, changed gameplay roots that can safely cross JSON."""
        result = {}
        try:
            roots = _wells_tracker_changed_roots()
            for full_name, value in roots.items():
                if not isinstance(full_name, WELLS_TRACKER_STRING_TYPES):
                    continue
                if not full_name.startswith("store."):
                    continue
                name = full_name[6:]
                if not name or name.startswith("_") or name.startswith("wells_"):
                    continue
                if name in ("config", "persistent", "renpy", "gui", "style", "store"):
                    continue
                clean = _wells_tracker_json_value(value)
                if clean is not None or value is None:
                    result[name] = clean
        except Exception:
            pass
        return result

    def wells_tracker_list_records():
        records = []
        try:
            names = os.listdir(WELLS_TRACKER_DIR)
        except Exception:
            return records
        for filename in names:
            if not (filename.startswith("checkpoint_") and filename.endswith(".json")):
                continue
            try:
                payload = _wells_tracker_read_json(filename)
                records.append({
                    "filename": filename,
                    "timestamp": payload.get("timestamp", 0),
                    "image_name": payload.get("checkpoint_image"),
                    "asset_file": payload.get("checkpoint_asset"),
                    "version": payload.get("version", 1),
                })
            except Exception:
                records.append({"filename": filename, "timestamp": 0, "image_name": None, "asset_file": None, "version": 0})
        records.sort(key=lambda item: (item.get("timestamp", 0), item["filename"]), reverse=True)
        return records

    def wells_tracker_format_time(timestamp):
        try:
            return time.strftime("%d.%m.%Y - %H:%M", time.localtime(int(timestamp)))
        except Exception:
            return _wells_tracker_text(timestamp)

    def _wells_tracker_value(action):
        """ChoiceReturn is an Action; its .value is the AST menu branch index."""
        try:
            return action.value
        except Exception:
            return action

    def _wells_tracker_option_data(items):
        options = []
        for item in items:
            try:
                label = _wells_tracker_text(item[0])
                value = _wells_tracker_value(item[1])
                clean = _wells_tracker_json_value(value)
                if clean is None and value is not None:
                    clean = _wells_tracker_text(value)
                options.append({"label": label, "value": clean})
            except Exception:
                continue
        return options

    def _wells_tracker_source_file():
        node = _wells_tracker_current_node()
        return node.get("file") if isinstance(node, dict) else None

    def _wells_tracker_native_forward():
        """Read the choice payload Ren'Py attached to its current rollback entry."""
        try:
            current = getattr(renpy.game.log, "current", None)
            return getattr(current, "forward", None)
        except Exception:
            return None

    def _wells_tracker_choice_record(items, result):
        options = _wells_tracker_option_data(items)
        selected = _wells_tracker_json_value(result)
        if selected is None and result is not None:
            selected = _wells_tracker_text(result)
        selected_index = None
        selected_label = None
        for index, option in enumerate(options):
            if option.get("value") == selected:
                selected_index = index
                selected_label = option.get("label")
                break
        return {
            "choice_value": selected,
            "selected_index": selected_index,
            "selected_label": selected_label,
            "options": options,
            "source_file": _wells_tracker_source_file(),
            "rollback_forward": _wells_tracker_json_value(_wells_tracker_native_forward()),
        }

    def _wells_tracker_options_match(saved, current):
        old = saved.get("options", []) if hasattr(saved, "get") else []
        if len(old) != len(current):
            return False
        for old_item, new_item in zip(old, current):
            if not hasattr(old_item, "get"):
                return False
            if old_item.get("label") != new_item.get("label"):
                return False
            if old_item.get("value") != new_item.get("value"):
                return False
        saved_file = saved.get("source_file")
        current_file = _wells_tracker_source_file()
        if saved_file and current_file and saved_file.replace("\\", "/").lower() != current_file.replace("\\", "/").lower():
            return False
        return True

    def _wells_tracker_checkpoint_value(result):
        try:
            renpy.checkpoint(result)
        except Exception:
            pass

    def _wells_tracker_auto_choice(items, saved):
        current = _wells_tracker_option_data(items)
        if not _wells_tracker_options_match(saved, current):
            return (False, None)
        wanted = saved.get("choice_value")
        for item in items:
            try:
                action = item[1]
                value = _wells_tracker_value(action)
                if _wells_tracker_json_value(value) != wanted:
                    continue
                result = action() if callable(action) else value
                _wells_tracker_checkpoint_value(result)
                return (True, result)
            except Exception:
                return (False, None)
        return (False, None)

    def _wells_tracker_finish_replay(message):
        replay = getattr(store, "wells_tracker_replay", None)
        store.wells_tracker_replay = None
        try:
            renpy.config.skipping = replay.get("previous_skipping") if isinstance(replay, dict) else None
        except Exception:
            pass
        try:
            preferences = renpy.game.preferences
            if isinstance(replay, dict):
                if "previous_skip_unseen" in replay:
                    preferences.skip_unseen = replay.get("previous_skip_unseen")
                if "previous_skip_after_choices" in replay:
                    preferences.skip_after_choices = replay.get("previous_skip_after_choices")
        except Exception:
            pass
        try:
            if os.path.isfile(WELLS_TRACKER_PENDING):
                os.remove(WELLS_TRACKER_PENDING)
        except Exception:
            pass
        if message:
            renpy.notify(message)

    def _wells_tracker_restore_variables(replay):
        values = replay.get("variables", {}) if isinstance(replay, dict) else {}
        restored = 0
        for name, value in values.items():
            if not isinstance(name, WELLS_TRACKER_STRING_TYPES):
                continue
            if not name or name.startswith("_") or name.startswith("wells_"):
                continue
            try:
                setattr(store, name, value)
                restored += 1
            except Exception:
                pass
        return restored

    def _wells_tracker_anchor_matches(replay):
        # The displayed image is the checkpoint anchor. Script nodes are kept
        # as diagnostics only: their exact location can differ between SDKs,
        # versions, and the statement callback timing after a clean restart.
        target = replay.get("anchor", {}) if isinstance(replay, dict) else {}
        current = _wells_tracker_current_anchor()
        if not current or not target:
            return False
        target_name = target.get("image_name")
        if target_name and current.get("image_name") != target_name:
            return False
        target_asset = target.get("asset_file")
        current_asset = current.get("asset_file")
        if target_asset and current_asset:
            if target_asset.replace("\\", "/").lower() != current_asset.replace("\\", "/").lower():
                return False
        return True

    def _wells_tracker_try_finish_at_anchor():
        replay = getattr(store, "wells_tracker_replay", None)
        if not isinstance(replay, dict):
            return False
        if replay.get("cursor", 0) < len(replay.get("choices", [])):
            return False
        if not _wells_tracker_anchor_matches(replay):
            return False
        restored = _wells_tracker_restore_variables(replay)
        _wells_tracker_finish_replay("Checkpoint reconstruído. {} variáveis restauradas.".format(restored))
        return True

    def wells_salvar_checkpoint():
        anchor = _wells_tracker_current_anchor()
        if not anchor:
            renpy.notify("Wells: não consegui identificar a imagem ativa da cena.")
            return
        try:
            timestamp = int(time.time())
            filename = "checkpoint_{}.json".format(timestamp)
            while os.path.exists(os.path.join(WELLS_TRACKER_DIR, filename)):
                timestamp += 1
                filename = "checkpoint_{}.json".format(timestamp)

            choices = []
            for item in getattr(store, "wells_tracker_choices", []):
                if isinstance(item, dict):
                    choices.append(_wells_tracker_json_value(item))

            payload = {
                "version": WELLS_TRACKER_VERSION,
                "timestamp": timestamp,
                "game_name": _wells_tracker_text(getattr(renpy.config, "name", "Ren'Py game")),
                "checkpoint_image": anchor.get("image_name"),
                "checkpoint_asset": anchor.get("asset_file"),
                "script_node": anchor.get("script_node"),
                "choices": choices,
                "variables": wells_tracker_collect_variables(),
            }
            _wells_tracker_write_json(filename, payload)
            renpy.notify("Checkpoint registrado.")
            renpy.restart_interaction()
        except Exception as error:
            renpy.notify("Wells: erro ao gravar checkpoint: " + _wells_tracker_text(error))

    def wells_tracker_preview(image_name, asset_file=None):
        try:
            if image_name:
                registered = renpy.get_registered_image(tuple(image_name.split()))
                if registered is not None:
                    return registered
        except Exception:
            pass
        try:
            if asset_file:
                return Image(asset_file)
        except Exception:
            pass
        return None

    def wells_tracker_delete(filename):
        if not filename or os.path.basename(filename) != filename:
            renpy.notify("Nome de checkpoint inválido.")
            return
        try:
            path = os.path.join(WELLS_TRACKER_DIR, filename)
            if os.path.isfile(path):
                os.remove(path)
            renpy.notify("Checkpoint removido.")
            renpy.restart_interaction()
        except Exception as error:
            renpy.notify("Wells: não foi possível remover o checkpoint: " + _wells_tracker_text(error))

    def _wells_tracker_write_pending(filename):
        pending_filename = filename
        try:
            if not isinstance(pending_filename, unicode):
                pending_filename = pending_filename.decode("utf-8")
        except NameError:
            pass
        with io.open(WELLS_TRACKER_PENDING, "w", encoding="utf-8") as stream:
            stream.write(pending_filename)

    def wells_tracker_request_load(filename):
        if not filename or os.path.basename(filename) != filename:
            renpy.notify("Nome de checkpoint inválido.")
            return
        try:
            payload = _wells_tracker_read_json(filename)
        except Exception as error:
            renpy.notify("Wells: não consegui ler o checkpoint: " + _wells_tracker_text(error))
            return
        if payload.get("version") != WELLS_TRACKER_VERSION:
            renpy.notify("Este checkpoint foi criado por outro formato. Registre um novo.")
            return
        if not payload.get("checkpoint_image"):
            renpy.notify("Este checkpoint não tem uma imagem de referência válida.")
            return
        if not isinstance(payload.get("choices"), list) or not isinstance(payload.get("variables"), dict):
            renpy.notify("O arquivo de checkpoint está incompleto.")
            return
        try:
            _wells_tracker_write_pending(filename)
        except Exception as error:
            try:
                if os.path.exists(WELLS_TRACKER_PENDING):
                    os.remove(WELLS_TRACKER_PENDING)
            except Exception:
                pass
            renpy.notify("Wells: não foi possível reiniciar para reconstruir: " + _wells_tracker_text(error))
            return
        # Let Ren'Py's FullRestartException travel through the engine unchanged.
        renpy.full_restart(label="_wells_tracker_bootstrap", target="_main_menu")

    def _wells_tracker_activate_pending_load():
        if not os.path.isfile(WELLS_TRACKER_PENDING):
            return False
        try:
            with io.open(WELLS_TRACKER_PENDING, "r", encoding="utf-8") as stream:
                filename = stream.read().strip()
            if not filename or os.path.basename(filename) != filename:
                raise ValueError("Nome de arquivo inválido")
            payload = _wells_tracker_read_json(filename)
            if payload.get("version") != WELLS_TRACKER_VERSION:
                raise ValueError("Formato de checkpoint incompatível")
            store.wells_tracker_choices = []
            preferences = renpy.game.preferences
            store.wells_tracker_replay = {
                "filename": filename,
                "choices": payload.get("choices", []),
                "cursor": 0,
                "anchor": {
                    "image_name": payload.get("checkpoint_image"),
                    "asset_file": payload.get("checkpoint_asset"),
                    "script_node": payload.get("script_node"),
                },
                "variables": payload.get("variables", {}),
                "previous_skipping": getattr(renpy.config, "skipping", None),
                "previous_skip_unseen": getattr(preferences, "skip_unseen", False),
                "previous_skip_after_choices": getattr(preferences, "skip_after_choices", False),
            }
            preferences.skip_unseen = True
            if hasattr(preferences, "skip_after_choices"):
                preferences.skip_after_choices = True
            renpy.config.skipping = "fast"
            return True
        except Exception as error:
            _wells_tracker_finish_replay(None)
            renpy.notify("Wells: não consegui preparar o checkpoint: " + _wells_tracker_text(error))
            return False

    def _wells_tracker_statement_callback(statement_name):
        replay = getattr(store, "wells_tracker_replay", None)
        if not isinstance(replay, dict):
            return
        if _wells_tracker_try_finish_at_anchor():
            return
        if replay.get("cursor", 0) >= len(replay.get("choices", [])):
            steps = replay.get("steps_after_route", 0) + 1
            new_replay = dict(replay)
            new_replay["steps_after_route"] = steps
            store.wells_tracker_replay = new_replay
            if steps >= 5000:
                _wells_tracker_finish_replay("A imagem salva não foi localizada. A reconstrução foi interrompida.")

    WELLS_TRACKER_ORIGINAL_MENUS = {}

    def _wells_tracker_make_menu_wrapper(original, menu_name):
        def _wrapper(items, *args, **kwargs):
            replay = getattr(store, "wells_tracker_replay", None)
            if isinstance(replay, dict):
                cursor = replay.get("cursor", 0)
                choices = replay.get("choices", [])
                if cursor < len(choices):
                    selected, result = _wells_tracker_auto_choice(items, choices[cursor])
                    if selected:
                        new_replay = dict(replay)
                        new_replay["cursor"] = cursor + 1
                        store.wells_tracker_replay = new_replay
                        try:
                            record = _wells_tracker_choice_record(items, result)
                            store.wells_tracker_choices = list(getattr(store, "wells_tracker_choices", [])) + [record]
                        except Exception:
                            pass
                        return result
                    _wells_tracker_finish_replay("A rota mudou nesta versão. A escolha atual ficou para você.")
                else:
                    if _wells_tracker_try_finish_at_anchor():
                        return original(items, *args, **kwargs)
                    _wells_tracker_finish_replay("A imagem de referência não foi encontrada antes da próxima escolha.")

            result = original(items, *args, **kwargs)
            if result is not None:
                try:
                    record = _wells_tracker_choice_record(items, result)
                    store.wells_tracker_choices = list(getattr(store, "wells_tracker_choices", [])) + [record]
                except Exception:
                    pass
            return result
        _wrapper._wells_tracker_hook = True
        _wrapper._wells_tracker_menu_name = menu_name
        return _wrapper

    def _wells_tracker_install_menu_hooks():
        for menu_name in ("menu", "nvl_menu"):
            current = getattr(store, menu_name, None)
            if current is None or getattr(current, "_wells_tracker_hook", False):
                continue
            WELLS_TRACKER_ORIGINAL_MENUS[menu_name] = current
            setattr(store, menu_name, _wells_tracker_make_menu_wrapper(current, menu_name))

    try:
        config.statement_callbacks.append(_wells_tracker_statement_callback)
    except Exception:
        pass
    _wells_tracker_install_menu_hooks()

init 10000 python:
    _wells_tracker_install_menu_hooks()

label _wells_tracker_bootstrap:
    $ _wells_tracker_activate_pending_load()
    jump start
