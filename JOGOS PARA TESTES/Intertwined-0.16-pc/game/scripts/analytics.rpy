################################################################################
## Analytics / Telemetry — BlueFox.au v1.2.0
################################################################################
##
## This file implements anonymous analytics and telemetry collection for Intertwined.
## It allows the game to collect usage data, session information, and other relevant
## metrics to improve the game experience while respecting user privacy.
##
################################################################################

define ANALYTICS_AVAILABLE = True
default persistent.analytics_opt_out = False
default persistent.analytics_notice_shown = False
default persistent.analytics_id = None
default persistent.analytics_active_session = None
default persistent.analytics_last_version = None
default persistent.analytics_save_count = 0

init -10 python:

    import os, sys, json, time, uuid, platform, threading, builtins as _builtins, traceback as _traceback

    try:
        import ssl as _ssl
    except Exception:
        _ssl = None

    try:
        import certifi as _certifi
        _CA_FILE = _certifi.where()
    except Exception:
        _certifi = None
        _CA_FILE = None

    try:
        import urllib.request as _urlrequest
        import urllib.error as _urlerror
    except Exception:
        _urlrequest = None
        _urlerror = None

    class _IntertwinedAnalytics(object):
        ENDPOINT = "https://analytics.valerianyx.com/collect/"
        PRIVACY_URL = "https://valerianyx.com/privacy"

        FLUSH_INTERVAL = 30
        FLUSH_THRESHOLD = 25
        QUEUE_CAP = 500
        BATCH_SIZE = 100
        TIMEOUT = 5

        _POINTS_RE = None

        def __init__(self):
            self._queue = []
            self._lock = threading.Lock()
            self._stop = threading.Event()
            self._thread = None
            self._dirty = False
            self._queue_file = None
            self._session_id = uuid.uuid4().hex
            self._start = time.time()
            self._max_episodes = None
            self._episode = None
            self._episode_started_at = None
            self._episode_active_time = 0.0
            self._episode_skip_time = 0.0
            self._episode_label_count = 0
            self._episode_choice_count = 0
            self._episode_start_label = None
            self._was_skipping = False
            self._skip_started_at = None
            self._skip_started_episode = None
            self._skip_started_label = None
            self._screen_opens = {}
            self._tracked_screens = set([
                "save", "load", "preferences", "main_menu", "navigation",
                "about", "help",
            ])
            self._tracked_screen_suffixes = ("_gallery",)
            self._current_language = getattr(renpy.store._preferences, "language", None)

        def _client_id(self):
            if hasattr(self, "_cached_cid"):
                return self._cached_cid

            method = "legacy"
            old_id = None

            try:
                cid = persistent.analytics_id
            except Exception:
                cid = None

            anchor_path = None
            anchor_cid = None
            try:
                anchor_path = os.path.join(os.path.dirname(self._queue_path()), ".anchor")
                if os.path.exists(anchor_path):
                    with open(anchor_path, "r") as f:
                        anchor_cid = f.read().strip()
            except Exception:
                pass

            hw_cid = None
            try:
                machine_node = str(uuid.getnode())
                hw_cid = uuid.uuid5(uuid.NAMESPACE_DNS, machine_node).hex
            except Exception:
                pass

            # --- ID RESOLUTION & UPGRADE LOGIC ---
            if cid and not anchor_cid:
                if hw_cid:
                    old_id = cid
                    cid = hw_cid
                    method = "upgraded_to_hardware"
                else:
                    method = "legacy_anchored"

            elif not cid and anchor_cid:
                cid = anchor_cid
                method = "recovered_anchor"

            elif not cid:
                if hw_cid:
                    cid = hw_cid
                    method = "hardware_hash"
                else:
                    cid = uuid.uuid4().hex
                    method = "random_uuid"

            else:
                method = "existing_anchored"

            # --- SYNCING ---

            if anchor_path:
                try:
                    with open(anchor_path, "w") as f:
                        f.write(cid)
                except Exception:
                    pass

            try:
                if persistent.analytics_id != cid:
                    persistent.analytics_id = cid
                    renpy.save_persistent()
            except Exception:
                pass

            self._cached_cid = cid
            self._id_source = method
            if old_id:
                self._legacy_id_to_migrate = old_id

            return cid

        def _debug_log(self, msg):
            return

        def _enabled(self):
            try:
                return not bool(persistent.analytics_opt_out)
            except Exception:
                return True

        def _queue_path(self):
            if self._queue_file:
                return self._queue_file
            base = None
            try:
                if renpy.android:
                    base = os.path.join(renpy.config.savedir, "analytics")
                elif sys.platform == "win32":
                    base = os.environ.get("LOCALAPPDATA") \
                        or os.path.join(os.path.expanduser("~"), "AppData", "Local")
                    base = os.path.join(base, "Intertwined", "analytics")
                elif sys.platform == "darwin":
                    base = os.path.join(os.path.expanduser("~"),
                                        "Library", "Caches", "Intertwined", "analytics")
                else:
                    xdg = os.environ.get("XDG_CACHE_HOME") \
                        or os.path.join(os.path.expanduser("~"), ".cache")
                    base = os.path.join(xdg, "intertwined", "analytics")
            except Exception:
                base = None
            if not base:
                base = os.path.join(os.path.expanduser("~"), ".intertwined", "analytics")
            try:
                if not os.path.isdir(base):
                    os.makedirs(base)
            except Exception:
                pass
            try:
                old_base = renpy.config.savedir
                if old_base:
                    legacy = os.path.join(old_base, "analytics_queue.json")
                    new = os.path.join(base, "analytics_queue.json")
                    if os.path.exists(legacy) and not os.path.exists(new):
                        try:
                            os.replace(legacy, new)
                        except Exception:
                            pass
                    stale_log = os.path.join(old_base, "analytics_debug.log")
                    if os.path.exists(stale_log):
                        try:
                            os.remove(stale_log)
                        except Exception:
                            pass
            except Exception:
                pass
            self._queue_file = os.path.join(base, "analytics_queue.json")
            return self._queue_file

        def _load_queue(self):
            path = self._queue_path()
            try:
                if os.path.exists(path):
                    with open(path, "r") as f:
                        data = json.load(f)
                    if isinstance(data, _builtins.list):
                        with self._lock:
                            self._queue = data[-self.QUEUE_CAP:]
            except Exception:
                pass

        def _save_queue(self):
            path = self._queue_path()
            try:
                with self._lock:
                    snapshot = list(self._queue)
                    self._dirty = False
                tmp = path + ".tmp"
                with open(tmp, "w") as f:
                    json.dump(snapshot, f)
                os.replace(tmp, path)
            except Exception:
                with self._lock:
                    self._dirty = True

        def enqueue(self, event_type, data=None):
            if not self._enabled():
                return

            active_lang = getattr(renpy.store._preferences, "language", None)
            lang_str = str(active_lang) if active_lang is not None else "primary"

            event = {
                "type": event_type,
                "t": time.time(),
                "session_t": round(time.time() - self._start, 3),
                "lang": lang_str
            }
            if data:
                try:
                    event["data"] = data
                except Exception:
                    pass
            with self._lock:
                self._queue.append(event)
                if len(self._queue) > self.QUEUE_CAP:
                    self._queue = self._queue[-self.QUEUE_CAP:]
                self._dirty = True
                count = len(self._queue)
            if event_type in ("crash", "audio_error", "image_error", "script_error", "session_end"):
                self._save_queue()
            if count >= self.FLUSH_THRESHOLD:
                self._wake()

        def _wake(self):
            if hasattr(self, "_stop_wait_event"):
                self._stop_wait_event.set()

        def _post(self, batch):
            if _urlrequest is None:
                return False
            payload = {
                "client": "intertwined",
                "schema": 1,
                "game_version": self._game_version(),
                "analytics_id": self._client_id(),
                "session_id": self._session_id,
                "sent_at": time.time(),
                "events": batch,
            }
            try:
                body = json.dumps(payload).encode("utf-8")
            except Exception:
                return False
            req = _urlrequest.Request(
                self.ENDPOINT,
                data=body,
                headers={
                    "Content-Type": "application/json",
                    "User-Agent": "Intertwined-Analytics/1",
                },
                method="POST",
            )
            ctx = None
            if _ssl is not None:
                try:
                    if _CA_FILE:
                        ctx = _ssl.create_default_context(cafile=_CA_FILE)
                    else:
                        ctx = _ssl.create_default_context()
                except Exception:
                    ctx = None
            try:
                resp = _urlrequest.urlopen(req, timeout=self.TIMEOUT, context=ctx)
                try:
                    code = resp.getcode()
                finally:
                    resp.close()
                ok = code is not None and 200 <= code < 300
                self._debug_log("POST %s -> %s (%d events)" % (self.ENDPOINT, code, len(batch)))
                return ok
            except Exception as e:
                self._debug_log("POST FAILED %s: %s: %s" % (
                    self.ENDPOINT, type(e).__name__, str(e)[:300]))
                return False

        def _flush(self):
            if not self._enabled():
                return
            with self._lock:
                if not self._queue:
                    return
                batch = self._queue[:self.BATCH_SIZE]
            if not batch:
                return
            if self._post(batch):
                with self._lock:
                    self._queue = self._queue[len(batch):]
                    self._dirty = True
                self._save_queue()

        def _loop(self):
            while not self._stop.is_set():
                try:
                    self._flush()
                except Exception:
                    pass
                try:
                    with self._lock:
                        dirty = self._dirty
                    if dirty:
                        self._save_queue()
                except Exception:
                    pass
                self._stop_wait_event.clear()
                self._stop_wait_event.wait(self.FLUSH_INTERVAL)

        def start(self):
            if self._thread and self._thread.is_alive():
                return
            self._stop_wait_event = threading.Event()
            self._load_queue()
            self._register_hooks()
            self._emit_lifecycle_events()
            self.enqueue("session_start", self._system_info())
            self._mark_active_session()
            self._stop.clear()
            self._thread = threading.Thread(target=self._loop, name="Analytics")
            self._thread.daemon = True
            self._thread.start()

        def _detect_distribution(self):
            flags = {
                "save_dir": getattr(config, "save_directory", "unknown"),
                "in_steamapps": False
            }

            try:
                base = str(config.basedir).lower()
                if "steamapps" in base or "steam library" in base:
                    flags["in_steamapps"] = True
            except Exception:
                pass

            return flags

        def _emit_lifecycle_events(self):
            try:
                had_id = bool(persistent.analytics_id)
            except Exception:
                had_id = True
            try:
                prev_active = persistent.analytics_active_session
            except Exception:
                prev_active = None
            try:
                prev_version = persistent.analytics_last_version
            except Exception:
                prev_version = None

            current_version = self._game_version()

            self._client_id()

            if hasattr(self, "_legacy_id_to_migrate"):
                self.enqueue("id_migrated", {
                    "old_id": getattr(self, "_legacy_id_to_migrate"),
                    "new_id": self._cached_cid
                })

            if not had_id:
                self.enqueue("install", {
                    "game_version": current_version,
                    "anchor_type": getattr(self, "_id_source", "unknown")
                })
            elif prev_version and current_version and prev_version != current_version:
                self.enqueue("version_upgrade", {
                    "from": prev_version,
                    "to": current_version,
                })

            if isinstance(prev_active, _builtins.dict):
                self.enqueue("session_recovered", {
                    "previous_session_id": prev_active.get("session_id"),
                    "previous_started_at": prev_active.get("started_at"),
                    "previous_game_version": prev_active.get("game_version"),
                    "previous_episode": prev_active.get("episode"),
                    "previous_label": prev_active.get("label"),
                })

            try:
                persistent.analytics_last_version = current_version
            except Exception:
                pass

        def _mark_active_session(self):
            try:
                persistent.analytics_active_session = {
                    "session_id": self._session_id,
                    "started_at": self._start,
                    "game_version": self._game_version(),
                    "episode": self._episode,
                    "label": None,
                }
            except Exception:
                pass
            self._save_persistent()

        def _update_active_session(self):
            try:
                state = persistent.analytics_active_session
                if not isinstance(state, _builtins.dict):
                    return
                state["episode"] = self._episode
                try:
                    state["label"] = self._current_label()
                except Exception:
                    pass
                persistent.analytics_active_session = state
            except Exception:
                pass

        def _clear_active_session(self):
            try:
                persistent.analytics_active_session = None
            except Exception:
                pass
            self._save_persistent()

        def _save_persistent(self):
            try:
                renpy.save_persistent()
            except Exception:
                pass

        def stop(self):
            try:
                if self._was_skipping and self._skip_started_at is not None:
                    duration = max(0.0, time.time() - self._skip_started_at)
                    self._episode_skip_time += duration
                    self._was_skipping = False
                    self._skip_started_at = None
                self._end_current_episode()
            except Exception:
                pass
            try:
                self.enqueue("session_end", {
                    "duration": round(time.time() - self._start, 3),
                })
            except Exception:
                pass
            self._clear_active_session()
            self._stop.set()
            if hasattr(self, "_stop_wait_event"):
                self._stop_wait_event.set()
            try:
                self._flush()
            except Exception:
                pass
            try:
                self._save_queue()
            except Exception:
                pass

        def _register_hooks(self):
            try:
                if self._on_label not in config.label_callbacks:
                    config.label_callbacks.append(self._on_label)
            except Exception:
                pass
            try:
                if self._on_after_load not in config.after_load_callbacks:
                    config.after_load_callbacks.append(self._on_after_load)
            except Exception:
                pass
            try:
                if self._periodic not in config.periodic_callbacks:
                    config.periodic_callbacks.append(self._periodic)
            except Exception:
                pass
            try:
                prev = config.exception_handler
                if getattr(prev, "_analytics_wrapped", False):
                    pass
                else:
                    def handler(short, full, traceback_fn, _prev=prev):
                        try:
                            self._on_exception(short, full, traceback_fn)
                        except Exception:
                            pass
                        if _prev is not None:
                            try:
                                return _prev(short, full, traceback_fn)
                            except Exception:
                                return False
                        return False
                    handler._analytics_wrapped = True
                    config.exception_handler = handler
            except Exception:
                pass
            try:
                prev_menu = renpy.store.menu
                if getattr(prev_menu, "_analytics_wrapped", False):
                    pass
                else:
                    def menu(items, *args, **kwargs):
                        result = prev_menu(items, *args, **kwargs)
                        try:
                            self._on_menu(items, result)
                        except Exception:
                            pass
                        return result
                    menu._analytics_wrapped = True
                    renpy.store.menu = menu
            except Exception:
                pass
            try:
                prev_save = renpy.save
                if not getattr(prev_save, "_analytics_wrapped", False):
                    def save(slotname, *args, **kwargs):
                        import errno
                        try:
                            rv = prev_save(slotname, *args, **kwargs)
                        except OSError as e:
                            if e.errno == errno.ENOSPC:
                                renpy.notify(__("Failed to save: Not enough disk space."))
                                return False
                            else:
                                raise
                        except TypeError as e:
                            ## Pickling failure detection
                            notes = getattr(e, "__notes__", None) or []
                            culprit = " | ".join(str(n) for n in notes)[:500]
                            try:
                                self.enqueue("save_pickle_error", {
                                    "summary": str(e)[:500],
                                    "culprit": culprit or None,
                                    "slot": str(slotname),
                                    "label": self._current_label(),
                                    "episode": self._current_episode(),
                                })
                                self._save_queue()
                            except Exception:
                                pass
                            if culprit and culprit not in str(e):
                                e.args = (str(e) + " (" + culprit + ")",) + e.args[1:]
                            raise

                        try:
                            self._on_save(slotname)
                        except Exception:
                            pass

                        return rv
                    save._analytics_wrapped = True
                    renpy.save = save
            except Exception:
                pass
            try:
                prev_rb = renpy.rollback
                if not getattr(prev_rb, "_analytics_wrapped", False):
                    def rollback(*args, **kwargs):
                        checkpoints = kwargs.get("checkpoints", None)
                        if checkpoints is None and len(args) >= 2:
                            checkpoints = args[1]
                        if checkpoints is None:
                            checkpoints = 1
                        rv = prev_rb(*args, **kwargs)
                        try:
                            self._on_rollback(int(checkpoints))
                        except Exception:
                            pass
                        return rv
                    rollback._analytics_wrapped = True
                    renpy.rollback = rollback
            except Exception:
                pass
            try:
                prev_show = renpy.show_screen
                if not getattr(prev_show, "_analytics_wrapped", False):
                    def show_screen(_screen_name, *args, **kwargs):
                        rv = prev_show(_screen_name, *args, **kwargs)
                        try:
                            self._on_screen_show(_screen_name, kwargs)
                        except Exception:
                            pass
                        return rv
                    show_screen._analytics_wrapped = True
                    renpy.show_screen = show_screen
            except Exception:
                pass
            try:
                prev_missing_label = config.missing_label_callback
                if not getattr(prev_missing_label, "_analytics_wrapped", False):
                    def missing_label(label, _prev=prev_missing_label):
                        try:
                            self._on_missing_label(label)
                        except Exception:
                            pass
                        if _prev is not None:
                            try:
                                return _prev(label)
                            except Exception:
                                return None
                        return None
                    missing_label._analytics_wrapped = True
                    config.missing_label_callback = missing_label
            except Exception:
                pass
            try:
                prev_missing_image = config.missing_image_callback
                if not getattr(prev_missing_image, "_analytics_wrapped", False):
                    def missing_image(name, _prev=prev_missing_image):
                        try:
                            self._on_missing_image(name)
                        except Exception:
                            pass
                        if _prev is not None:
                            try:
                                return _prev(name)
                            except Exception:
                                return None
                        return None
                    missing_image._analytics_wrapped = True
                    config.missing_image_callback = missing_image
            except Exception:
                pass

        def _on_label(self, name, abnormal):
            try:
                ep = self._current_episode()
                if ep != self._episode:
                    self._end_current_episode()
                    if ep is not None:
                        self._begin_episode(ep, str(name))
                else:
                    self._episode_label_count += 1
                self.enqueue("scene", {
                    "label": str(name),
                    "episode": ep,
                    "abnormal": bool(abnormal),
                })
                self._update_active_session()
            except Exception:
                pass

        def _on_after_load(self):
            try:
                self.enqueue("load", {
                    "episode": self._current_episode(),
                })
            except Exception:
                pass

        def _on_exception(self, short, full, traceback_fn):
            short_s = str(short)[:500]
            full_s = str(full)[:8000]
            kind = "crash"
            blob = (short_s + "\n" + full_s).lower()
            if "local object" in blob or "cannot pickle" in blob or "can't pickle" in blob:
                kind = "mod_error"
            elif "renpy.audio" in blob or "audio.audio" in blob or "no such audio file" in blob or "pygame_sdl2.mixer" in blob:
                kind = "audio_error"
            elif "renpy.display.im" in blob or "no such image" in blob or "could not load image" in blob:
                kind = "image_error"
            elif "scriptdecoder" in blob or "renpy.parser" in blob or "syntax error" in blob:
                kind = "script_error"
            self.enqueue(kind, {
                "summary": short_s,
                "traceback": full_s,
                "label": self._current_label(),
                "episode": self._current_episode(),
            })
            try:
                if hasattr(self, "_stop_wait_event"):
                    self._stop_wait_event.set()
            except Exception:
                pass

        def _on_menu(self, items, result):
            caption = None
            options = []
            chosen = None
            for entry in items:
                try:
                    label, value = entry[0], entry[1]
                except Exception:
                    continue
                if value is None:
                    if caption is None and label:
                        caption = str(label)
                    continue
                raw = getattr(value, "value", value)
                options.append(str(label))
                if chosen is None and raw == result:
                    chosen = str(label)
            self.enqueue("choice", {
                "prompt": caption,
                "options": options,
                "chosen": chosen,
                "label": self._current_label(),
                "episode": self._current_episode(),
                "points": self._points(),
            })
            try:
                self._episode_choice_count += 1
            except Exception:
                pass

        def _begin_episode(self, episode, start_label):
            self._episode = episode
            self._episode_started_at = time.time()
            self._episode_active_time = 0.0
            self._episode_skip_time = 0.0
            self._episode_label_count = 1
            self._episode_choice_count = 0
            self._episode_start_label = start_label
            self.enqueue("episode_start", {
                "episode": episode,
                "label": start_label,
                "points": self._points(),
            })

        def _end_current_episode(self):
            if self._episode is None or self._episode_started_at is None:
                self._episode = None
                self._episode_started_at = None
                return
            now = time.time()
            if self._was_skipping and self._skip_started_at is not None:
                self._episode_skip_time += max(0.0, now - self._skip_started_at)
                self._skip_started_at = now
            duration = max(0.0, now - self._episode_started_at)
            self.enqueue("episode_end", {
                "episode": self._episode,
                "duration": round(duration, 3),
                "skip_seconds": round(self._episode_skip_time, 3),
                "active_seconds": round(max(0.0, duration - self._episode_skip_time), 3),
                "labels_visited": int(self._episode_label_count),
                "choices_made": int(self._episode_choice_count),
                "start_label": self._episode_start_label,
                "end_label": self._current_label(),
                "points": self._points(),
            })
            self._episode = None
            self._episode_started_at = None
            self._episode_active_time = 0.0
            self._episode_skip_time = 0.0
            self._episode_label_count = 0
            self._episode_choice_count = 0
            self._episode_start_label = None

        def _periodic(self):
            # ---- Language Change
            live_lang = getattr(renpy.store._preferences, "language", None)
            if live_lang != self._current_language:
                self.enqueue("language_changed", {
                    "from": str(self._current_language) if self._current_language is not None else "primary",
                    "to": str(live_lang) if live_lang is not None else "primary"
                })
                self._current_language = live_lang

            # ---- Skipping
            try:
                skipping = bool(renpy.is_skipping())
            except Exception:
                skipping = False
            if skipping == self._was_skipping:
                return
            now = time.time()
            if skipping:
                self._skip_started_at = now
                try:
                    self._skip_started_episode = self._current_episode()
                except Exception:
                    self._skip_started_episode = None
                try:
                    self._skip_started_label = self._current_label()
                except Exception:
                    self._skip_started_label = None
                try:
                    mode = renpy.get_skipping()
                except Exception:
                    mode = None
                self.enqueue("skip_start", {
                    "mode": mode,
                    "episode": self._skip_started_episode,
                    "label": self._skip_started_label,
                })
            else:
                duration = 0.0
                if self._skip_started_at is not None:
                    duration = max(0.0, now - self._skip_started_at)
                    self._episode_skip_time += duration
                end_label = None
                try:
                    end_label = self._current_label()
                except Exception:
                    pass
                self.enqueue("skip_end", {
                    "duration": round(duration, 3),
                    "start_episode": self._skip_started_episode,
                    "start_label": self._skip_started_label,
                    "end_episode": self._current_episode(),
                    "end_label": end_label,
                })
                self._skip_started_at = None
                self._skip_started_episode = None
                self._skip_started_label = None
            self._was_skipping = skipping

        def _on_save(self, slotname):
            try:
                persistent.analytics_save_count = int(persistent.analytics_save_count or 0) + 1
            except Exception:
                pass
            slot = str(slotname) if slotname is not None else None
            kind = "manual"
            if slot:
                low = slot.lower()
                if low.startswith("auto-") or low == "auto":
                    kind = "auto"
                elif low.startswith("quick-") or low == "quick":
                    kind = "quick"
            self.enqueue("save", {
                "slot": slot,
                "kind": kind,
                "total_saves": int(persistent.analytics_save_count or 0),
                "episode": self._current_episode(),
                "label": self._current_label(),
            })

        def _on_rollback(self, checkpoints):
            try:
                ck = int(checkpoints)
            except Exception:
                ck = 1
            if ck < 3:
                return
            self.enqueue("rollback", {
                "checkpoints": ck,
                "episode": self._current_episode(),
                "label": self._current_label(),
            })

        def _on_screen_show(self, screen_name, kwargs):
            name = str(screen_name) if screen_name is not None else None
            if not name:
                return
            if name not in self._tracked_screens and not name.endswith(self._tracked_screen_suffixes):
                return
            count = self._screen_opens.get(name, 0) + 1
            self._screen_opens[name] = count
            self.enqueue("screen_open", {
                "screen": name,
                "open_count": count,
                "episode": self._current_episode(),
                "label": self._current_label(),
            })

        def _on_missing_label(self, label):
            self.enqueue("script_missing", {
                "kind": "label",
                "name": str(label) if label is not None else None,
                "episode": self._current_episode(),
                "label_context": self._current_label(),
            })

        def _on_missing_image(self, name):
            try:
                if isinstance(name, (_builtins.list, tuple)):
                    name_str = " ".join(str(p) for p in name)
                else:
                    name_str = str(name)
            except Exception:
                name_str = None
            if name_str:
                low = name_str.lower()
                if low.startswith("gui/") or low.startswith("gui ") or low == "gui":
                    return
            self.enqueue("asset_missing", {
                "kind": "image",
                "name": name_str,
                "episode": self._current_episode(),
                "label_context": self._current_label(),
            })

        def track_ending(self, title=None):
            self.enqueue("ending_reached", {
                "title": str(title) if title is not None else None,
                "episode": self._current_episode(),
                "label": self._current_label(),
                "points": self._points(),
                "session_duration": round(time.time() - self._start, 3),
            })

        def _game_version(self):
            base_version = str(getattr(config, "version", "unknown"))
            try:
                raw_version = "v1.2.0"
                if raw_version:
                    return "{} - {}".format(base_version, raw_version)
                return base_version
            except Exception:
                return base_version

        def _current_label(self):
            try:
                node = renpy.game.context().current
                if node:
                    return str(node)
            except Exception:
                pass
            return None

        def _current_episode(self):
            import re
            try:
                filename, _ = renpy.get_filename_line()
                m = re.search(r"episode_(\d+)", filename or "", re.IGNORECASE)
                if m:
                    return int(m.group(1))
            except Exception:
                pass
            return None

        def _points(self):
            import re
            if self._POINTS_RE is None:
                self._POINTS_RE = re.compile(r"^([A-Z][A-Za-z]+)_Points$")
            out = {}
            try:
                attrs = dir(renpy.store)
            except Exception:
                attrs = []
            for attr in attrs:
                m = self._POINTS_RE.match(attr)
                if not m:
                    continue
                try:
                    out[m.group(1)] = int(getattr(renpy.store, attr, 0) or 0)
                except Exception:
                    pass
            return out or None

        def _gallery_progress(self):
            try:
                labels = getattr(renpy.store, "GALLERY_LABELS", None) or []
                if not labels:
                    return None
                seen = sum(1 for lbl in labels if renpy.seen_label(lbl))
                return {"seen": seen, "total": len(labels)}
            except Exception:
                return None

        def _detect_modded_archives(self):
            try:
                if config.archives:
                    return [str(arch) + ".rpa" for arch in config.archives]
            except Exception:
                pass
            return []

        def _detect_loose_scripts(self):
            base_whitelist = {
                "achievements", "analytics", "animate", "choice_tracker",
                "discord_rpc", "ending", "flag_defaults", "gallery",
                "gui", "options", "player_name", "playthrough_stats",
                "preferences", "save_browser", "save_recovery", "screens",
                "script", "warning"
            }

            suspicious_files = []
            try:
                gamedir = config.gamedir
                if os.path.isdir(gamedir):
                    for f in os.listdir(gamedir):
                        if f.endswith(".rpy") or f.endswith(".rpyc"):
                            base_name = f
                            if base_name.endswith(".rpyc"):
                                base_name = base_name[:-5]
                            elif base_name.endswith(".rpy"):
                                base_name = base_name[:-4]

                            if base_name in base_whitelist:
                                continue

                            if base_name.startswith("episode_"):
                                suffix = base_name[8:]
                                if suffix.isdigit():
                                    continue

                            suspicious_files.append(f)
            except Exception:
                pass

            return suspicious_files

        def _system_info(self):
            info = {}
            try:
                info["os"] = "Android" if renpy.android else platform.system()
                info["os_release"] = platform.release()
            except Exception:
                pass
            try:
                info["arch"] = platform.machine()
            except Exception:
                pass
            try:
                info["renpy_version"] = ".".join(str(x) for x in renpy.version_tuple[:3])
            except Exception:
                pass
            try:
                info["game_version"] = self._game_version()
            except Exception:
                pass
            try:
                info["language"] = str(renpy.store._preferences.language)
            except Exception:
                pass
            try:
                w, h = renpy.get_physical_size()
                info["resolution"] = [int(w), int(h)]
            except Exception:
                pass
            try:
                info["gallery"] = self._gallery_progress()
            except Exception:
                pass
            try:
                info["renderer"] = self._renderer_info()
            except Exception:
                pass
            try:
                detected_languages = list(renpy.known_languages())
                info["installed_languages"] = detected_languages
                info["is_translation_modded"] = len(detected_languages) > 0
            except Exception:
                pass
            try:
                modded_archives = self._detect_modded_archives()
                loose_scripts = self._detect_loose_scripts()

                info["modded_archives"] = modded_archives
                info["suspicious_scripts"] = loose_scripts
                info["is_modded"] = bool(modded_archives) or bool(loose_scripts)
            except Exception:
                pass
            try:
                info["total_saves"] = int(persistent.analytics_save_count or 0)
            except Exception:
                pass
            try:
                info["distribution"] = self._detect_distribution()
            except Exception:
                pass
            return info

        def _renderer_info(self):
            out = {}
            try:
                ri = renpy.get_renderer_info() or {}
                for key in ("renderer", "model", "resizable", "additive", "renderer_info"):
                    if key in ri:
                        try:
                            out[key] = ri[key] if isinstance(ri[key], (str, int, float, bool)) else str(ri[key])
                        except Exception:
                            pass
            except Exception:
                pass
            try:
                draw = getattr(renpy.display, "draw", None)
                if draw is not None:
                    info = getattr(draw, "info", None)
                    if isinstance(info, _builtins.dict):
                        for key in ("renderer", "model", "vendor", "version"):
                            if key in info and key not in out:
                                try:
                                    out[key] = str(info[key])[:200]
                                except Exception:
                                    pass
            except Exception:
                pass
            try:
                out["fullscreen"] = bool(renpy.store._preferences.fullscreen)
            except Exception:
                pass
            try:
                w, h = renpy.get_physical_size()
                out["physical_size"] = [int(w), int(h)]
            except Exception:
                pass
            try:
                out["virtual_size"] = [int(config.screen_width), int(config.screen_height)]
            except Exception:
                pass
            return out or None

    analytics = _IntertwinedAnalytics()
    config.quit_callbacks.append(analytics.stop)
    analytics.start()

screen analytics_notice():
    modal True
    zorder 200
    style_prefix "confirm"

    add "gui/overlay/confirm.png"

    frame:

        vbox:
            xalign .5
            yalign .5
            spacing 45

            label _("Anonymous Analytics"):
                style "confirm_prompt"
                xalign 0.5

            text _("To help improve the game, Intertwined collects anonymous gameplay data (scenes viewed, choices made, progress, and crash reports). No personal information and no name you enter are ever sent.\n\nThis is enabled by default. You can turn it off at any time in Preferences. See our privacy policy for details."):
                style "confirm_prompt"
                xalign 0.5

            hbox:
                xalign 0.5
                spacing 150

                textbutton _("OK") action [SetField(persistent, "analytics_notice_shown", True), Hide("analytics_notice")]

                textbutton _("Privacy Policy") action OpenURL(analytics.PRIVACY_URL)
