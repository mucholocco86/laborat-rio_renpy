################################################################################
## Discord Rich Presence — BlueFox.au v1.2.0
################################################################################
##
## This file implements Discord Rich Presence integration for Intertwined. It
## allows the game to display the current episode, scene, and other relevant
## information on the player's Discord profile while they play.
##
################################################################################

default persistent.discord_rpc_enabled = True

init -10 python:

    import os, sys, re, json, time, uuid, struct, socket, threading

    class _IntertwinedDiscordRPC(object):

        CLIENT_ID = "803695561370763284"
        TICK = 15
        RECONNECT_DELAY = 30

        _DAY_NAMES = {
            _("Monday"), _("Tuesday"), _("Wednesday"), _("Thursday"),
            _("Friday"), _("Saturday"), _("Sunday"), _("Weekend"),
        }
        _PHASES = {
            _("Morning"), _("Lunch"), _("School"), _("Afternoon"),
            _("Evening"), _("Night"), _("Beach"),
        }
        _WEEK_RE = re.compile(r"^Week(\d+)_([A-Za-z]+)(?:_([A-Za-z]+))?")
        _EP_RE = re.compile(r"episode_(\d+)", re.IGNORECASE)
        _POINTS_RE = re.compile(r"^([A-Z][A-Za-z]+)_Points$")

        def __init__(self):
            self._sock = None
            self._win = (sys.platform == "win32")
            self._start = int(time.time())
            self._stop = threading.Event()
            self._thread = None
            self._last_sent = None
            self._label = None
            self._episode = None
            self._rotation = 0
            self._li_index = 0
            self._max_episodes = None
            self._gallery_cache = None

        def _path(self, n):
            if self._win:
                return r"\\.\pipe\discord-ipc-" + str(n)
            base = (os.environ.get("XDG_RUNTIME_DIR") or os.environ.get("TMPDIR")
                    or os.environ.get("TMP") or os.environ.get("TEMP") or "/tmp")
            return os.path.join(base, "discord-ipc-" + str(n))

        def _open(self):
            for n in range(10):
                try:
                    if self._win:
                        return open(self._path(n), "r+b", buffering=0)
                    s = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
                    s.connect(self._path(n))
                    return s
                except Exception:
                    pass
            return None

        def _write(self, data):
            if self._win:
                self._sock.write(data); self._sock.flush()
            else:
                self._sock.sendall(data)

        def _read(self, n):
            buf = b""
            while len(buf) < n:
                chunk = (self._sock.read(n - len(buf)) if self._win
                    else self._sock.recv(n - len(buf)))
                if not chunk:
                    return None
                buf += chunk
            return buf

        def _send(self, op, payload):
            data = json.dumps(payload).encode("utf-8")
            self._write(struct.pack("<II", op, len(data)) + data)

        def _recv(self):
            h = self._read(8)
            if h is None:
                return False
            _op, length = struct.unpack("<II", h)
            return length == 0 or self._read(length) is not None

        def _close(self):
            if self._sock is not None:
                try: self._sock.close()
                except Exception: pass
            self._sock = None
            self._last_sent = None

        def _connect(self):
            self._sock = self._open()
            if self._sock is None:
                return False
            try:
                self._send(0, {"v": 1, "client_id": self.CLIENT_ID})
                if not self._recv():
                    self._close(); return False
                return True
            except Exception:
                self._close(); return False

        def _on_label(self, name, abnormal):
            self._label = name
            try:
                node = renpy.game.script.lookup(name)
                m = self._EP_RE.search(node.filename or "")
                if m:
                    self._episode = int(m.group(1))
            except Exception:
                pass

        def _scene(self):
            try:
                if renpy.get_screen("main_menu"):
                    return __("Main Menu")
            except Exception:
                pass
            gal = self._gallery()
            if gal:
                return gal
            label = self._label or ""
            m = self._WEEK_RE.match(label)
            if m and m.group(2) in self._DAY_NAMES:
                base = __("Week") + " " + m.group(1) + " - " + m.group(2)
                phase = m.group(3)
                if phase and phase in self._PHASES:
                    base += " (" + __(phase) + ")"
                return base
            ep = self._current_episode()
            if ep is not None:
                return __("Episode") + " " + str(ep)
            return __("In Game")

        def _current_episode(self):
            try:
                filename, _ = renpy.get_filename_line()
                m = self._EP_RE.search(filename or "")
                if m:
                    return int(m.group(1))
            except Exception:
                pass
            return self._episode

        def _gallery(self):
            try:
                if renpy.get_screen("girls_gallery"):
                    return __("Browsing Gallery")
                for name in self._gallery_names():
                    if renpy.get_screen(name + "_gallery"):
                        return __("Browsing") + " " + name.capitalize() + __("'s Gallery")
            except Exception:
                pass
            return None

        def _gallery_names(self):
            if self._gallery_cache is not None:
                return self._gallery_cache
            names = []
            try:
                seen = set()
                for key in renpy.display.screen.screens:
                    sn = key[0] if isinstance(key, tuple) else key
                    if (sn.endswith("_gallery")
                            and sn != "girls_gallery"
                            and sn not in seen):
                        seen.add(sn)
                        names.append(sn[:-len("_gallery")])
                names.sort()
            except Exception:
                pass
            self._gallery_cache = names
            return names

        def _top_li(self):
            lis = []
            try:
                store_attrs = dir(renpy.store)
            except Exception:
                store_attrs = []
            for attr in store_attrs:
                m = self._POINTS_RE.match(attr)
                if not m:
                    continue
                try:
                    score = int(getattr(renpy.store, attr, 0) or 0)
                except Exception:
                    continue
                if score > 0:
                    lis.append((m.group(1), score))
            if not lis:
                return None, 0
            lis.sort(key=lambda x: x[0])
            name, score = lis[self._li_index % len(lis)]
            self._li_index = (self._li_index + 1) % len(lis)
            return name, score

        def _gallery_progress(self):
            try:
                labels = getattr(renpy.store, "GALLERY_LABELS", None) or []
                if not labels:
                    return None
                seen = sum(1 for lbl in labels if renpy.seen_label(lbl))
                return (__("Gallery Unlocks"), seen, len(labels))
            except Exception:
                return None

        def _story_progress(self):
            ep = self._current_episode()
            total = self._max_episode_count()
            if ep is None or not total:
                return None
            return (__("Story Progress"), ep, total)

        def _max_episode_count(self):
            if self._max_episodes is not None:
                return self._max_episodes
            eps = set()
            try:
                for f in renpy.list_files():
                    m = self._EP_RE.search(f)
                    if m:
                        eps.add(int(m.group(1)))
            except Exception:
                pass
            self._max_episodes = max(eps) if eps else 0
            return self._max_episodes

        def _counter(self):
            options = [
                self._story_progress(),
                self._gallery_progress(),
            ]
            options = [o for o in options if o is not None]
            if not options:
                return None
            choice = options[self._rotation % len(options)]
            self._rotation = (self._rotation + 1) % max(len(options), 1)
            return choice

        def _activity(self):
            ep = self._current_episode()
            top_name, top_score = self._top_li()
            counter = self._counter()

            large_text = "Intertwined " + __("Episode") + " " + str(ep) if ep else "Intertwined"
            try:
                mc_name = getattr(renpy.store, "name", None)
            except Exception:
                mc_name = None
            if mc_name:
                large_text += " - " + __("Playing as") + " " + str(mc_name)

            a = {
                "details": self._scene(),
                "timestamps": {"start": self._start},
                "assets": {
                    "large_image": "intertwined",
                    "large_text": large_text,
                },
                "buttons": [
                    {"label": __("Join Discord"),
                    "url": "https://discord.valerianyx.com"},
                    {"label": __("Website"),
                    "url": "https://valerianyx.com"}
                ],
            }
            if counter:
                label, cur, total = counter
                a["state"] = label
                a["party"] = {"id": "intertwined-progress",
                                "size": [int(cur), int(total)]}
            if top_name:
                a["assets"]["small_image"] = top_name.lower()
                a["assets"]["small_text"] = top_name + " " + __("Points") + " (" + str(top_score) + ")"
            return a

        def _set_activity(self, a):
            self._send(1, {"cmd": "SET_ACTIVITY",
                            "args": {"pid": os.getpid(), "activity": a},
                            "nonce": str(uuid.uuid4())})
            self._recv()

        def _loop(self):
            while not self._stop.is_set():
                try:
                    if self._sock is None and not self._connect():
                        self._stop.wait(self.RECONNECT_DELAY); continue
                    a = self._activity()
                    if a != self._last_sent:
                        self._set_activity(a)
                        self._last_sent = a
                except Exception:
                    self._close()
                self._stop.wait(self.TICK)

        def start(self):
            if self._thread and self._thread.is_alive():
                return
            if self._on_label not in config.label_callbacks:
                config.label_callbacks.append(self._on_label)
            self._stop.clear()
            self._thread = threading.Thread(target=self._loop, name="DiscordRPC")
            self._thread.daemon = True
            self._thread.start()

        def stop(self):
            self._stop.set()
            self._close()

    discord_rpc = _IntertwinedDiscordRPC()
    config.quit_callbacks.append(discord_rpc.stop)
    if persistent.discord_rpc_enabled is not False:
        discord_rpc.start()

    class ToggleDiscordRPC(Action):
        
        def get_selected(self):
            return persistent.discord_rpc_enabled is not False

        def __call__(self):
            persistent.discord_rpc_enabled = not self.get_selected()
            if persistent.discord_rpc_enabled:
                discord_rpc.start()
            else:
                discord_rpc.stop()
            renpy.restart_interaction()
