################################################################################
## Achievements — BlueFox.au v1.2.0
################################################################################
##
## Tracks the "complex" achievements that depend on multiple story flags
## or on having seen every gallery scene.
##
################################################################################

init -5 python:
    import re as _re

    _SEX_COUNTER_RE = _re.compile(r'\$\s*SexCounter_(\w+)\s*=')
    _EPISODE_START_RE = _re.compile(r'^Episode_(\d+)_Start$')

    def _achievement_gallery_labels():
        # GALLERY_DATA is defined later in init (gallery.rpy), so read it at check time.
        data = getattr(store, "GALLERY_DATA", None) or {}
        return [item[1] for info in data.values() for item in info.get("items", [])]

    def _load_sex_counter_girls():
        try:
            f = renpy.file("scripts/script.rpy")
        except Exception:
            return []
        try:
            data = f.read()
        finally:
            f.close()
        if isinstance(data, bytes):
            data = data.decode("utf-8", "replace")
        seen = set()
        girls = []
        for match in _SEX_COUNTER_RE.finditer(data):
            name = match.group(1)
            if name == "MC" or name in seen:
                continue
            seen.add(name)
            girls.append(name)
        return girls

    SEX_COUNTER_GIRLS = _load_sex_counter_girls()

    # ------------------------------------------------------------------
    # Achievement checkers
    # ------------------------------------------------------------------
    def _count(name):
        try:
            return int(getattr(store, name, 0) or 0)
        except (TypeError, ValueError):
            return 0

    def _get_flag(name):
        try:
            return bool(getattr(store, name, False))
        except (TypeError, ValueError):
            return False

    def check_keep_it_in_the_family():
        """Granted once the MC has slept with Lakeyn, Alexis and Layla."""
        if achievement.has("ACHIEVEMENT_KEEP_IT_IN_THE_FAMILY"):
            return
        if (_count("SexCounter_Alexis") > 0
                and _count("SexCounter_Lakeyn") > 0
                and _count("SexCounter_Layla") > 0):
            achievement.grant("ACHIEVEMENT_KEEP_IT_IN_THE_FAMILY")
            achievement.sync()

    def check_cherry_picker():
        """Granted once the MC has slept with Cara and Layla."""
        if achievement.has("ACHIEVEMENT_CHERRY_PICKER"):
            return
        if (_count("SexCounter_Cara") > 0
                and _count("SexCounter_Layla") > 0):
            achievement.grant("ACHIEVEMENT_CHERRY_PICKER")
            achievement.sync()

    def check_julia_mira():
        """Granted once the MC has slept with Julia and Mira."""
        if achievement.has("ACHIEVEMENT_JULIA_MIRA"):
            return
        if (_count("SexCounter_Julia") > 0
                and _count("SexCounter_Mira") > 0):
            achievement.grant("ACHIEVEMENT_JULIA_MIRA")
            achievement.sync()

    def check_try_before_you_buy():
        """Granted once the MC has slept with at least five different girls."""
        if achievement.has("ACHIEVEMENT_TRY_BEFORE_YOU_BUY"):
            return
        distinct = sum(
            1 for girl in SEX_COUNTER_GIRLS
            if _count("SexCounter_" + girl) > 0
        )
        if distinct >= 5:
            achievement.grant("ACHIEVEMENT_TRY_BEFORE_YOU_BUY")
            achievement.sync()

    def check_coaching_time():
        """Granted once the MC has watched Coach Mike with Natasha and Haley."""
        if achievement.has("ACHIEVEMENT_COACHING_TIME"):
            return
        if (_count("Natasha_Week2_Tuesday_MikeSex") > 0
                and _count("Haley_Week5_Saturday_SexWatch") > 0):
            achievement.grant("ACHIEVEMENT_COACHING_TIME")
            achievement.sync()

    def check_intertwined():
        """Granted once every gallery scene has been seen at least once."""
        if achievement.has("ACHIEVEMENT_INTERTWINED"):
            return
        labels = _achievement_gallery_labels()
        if not labels:
            return
        for label in labels:
            if not renpy.seen_label(label):
                return
        achievement.grant("ACHIEVEMENT_INTERTWINED")
        achievement.sync()

    def check_all_achievements(*args, **kwargs):
        check_keep_it_in_the_family()
        check_cherry_picker()
        check_julia_mira()
        check_try_before_you_buy()
        check_coaching_time()
        check_intertwined()

    config.start_callbacks.append(check_all_achievements)
    config.after_load_callbacks.append(check_all_achievements)

    _previous_label_callback = config.label_callback

    def _achievements_label_callback(name, abnormal):
        if _previous_label_callback is not None:
            _previous_label_callback(name, abnormal)
        check_all_achievements()

    config.label_callback = _achievements_label_callback
