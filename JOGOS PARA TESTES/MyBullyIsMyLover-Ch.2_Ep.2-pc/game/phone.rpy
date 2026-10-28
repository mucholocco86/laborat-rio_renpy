default channel_view_offset = {}
default phone_saved_range = 0
default phone_saved_value = 0
default phone_scroll_needs_fix = False
default phone_load_chunk = 50
default phone_visible_limit = 50
default channel_pending_anim = {}
default phone_scroll_adj_by_channel = {}
default channel_typing = {}
default channel_typing_global = False

define phone_mode = False

init -1 python:
    import re
    import renpy.store as store
    from datetime import datetime, timedelta

    def get_phone_yadj(channel_name):
        adj = store.phone_scroll_adj_by_channel.get(channel_name, None)
        if adj is None:
            adj = ui.adjustment()
            store.phone_scroll_adj_by_channel[channel_name] = adj
        return adj

    def _typing_dots(st, at):
        n = int(st * 3.0) % 3 + 1
        return renpy.text.text.Text(
            "." * n,
            size=int(phone_config["message_font_size"] * 0.85),
            color="#AAAAAADD",
            outlines=[]
        ), 0.12

    # story clock
    try:
        phone_clock
    except NameError:
        phone_clock = datetime.now()

    def phone_time_set(dt=None, *, year=None, month=None, day=None, hour=None, minute=None):
        """Set the story clock."""
        global phone_clock
        if dt is not None:
            phone_clock = dt
        else:
            now = datetime.now()
            phone_clock = datetime(year or now.year, month or now.month, day or now.day, hour or 0, minute or 0)

    def phone_time_add(*, days=0, hours=0, minutes=0):
        """Advance the story clock."""
        global phone_clock
        phone_clock += timedelta(days=days, hours=hours, minutes=minutes)
        renpy.restart_interaction()

    # --- DYNAMIC TIMESTAMPS ---
    def phone_stamp_abs(channel_name, fmt="%I:%M %p", do_pause=False):
        send_phone_message("", "", channel_name, message_kind=1,
                        summary_alt=("abs", phone_clock, fmt), do_pause=do_pause)

    def phone_stamp_rel(channel_name, *, back_years=0, back_months=0, back_days=0, back_hours=0, back_minutes=0, do_pause=False):
        year = phone_clock.year - back_years
        month = phone_clock.month - back_months
        day = phone_clock.day
        hour = phone_clock.hour
        minute = phone_clock.minute

        while month <= 0:
            month += 12
            year -= 1

        import calendar
        max_day = calendar.monthrange(year, month)[1]
        if day > max_day:
            day = max_day

        base_dt = datetime(year, month, day, hour, minute)

        base_dt -= timedelta(days=back_days, hours=back_hours, minutes=back_minutes)

        send_phone_message("", "", channel_name, message_kind=1,
                        summary_alt=("rel", base_dt), do_pause=do_pause)

    def phone_stamp_at(channel_name, *, year=None, month=None, day=None, hour=0, minute=0, do_pause=False):
        base_dt = datetime(
            year or phone_clock.year,
            month or phone_clock.month,
            day or phone_clock.day,
            hour, minute
        )
        
        send_phone_message("", "", channel_name, message_kind=1,
                        summary_alt=("rel", base_dt), do_pause=do_pause)

    phone_config = {
        # Sound Configuration
        "play_sound_send": True,
        "play_sound_receive": True,
        "no_sound_current_chat": False,
        # String Configurations
        "preview_no_message": "Empty chat...",
        "channels_title": "Messages",
        "history_timestamp_prefix": "Time:",
        "phone_player_name": "Me",
        "group_added": "{adder} added {participant} to the group.",
        "group_joined": "{participant} joined the group.",
        "group_left": "{participant} left the group.",
        # UI Configurations
        "message_font_size": 24,
        "choice_font_size": 24,
        "timestamp_font_size": 20,
        "auto_scroll": True,
        "show_sender_in_preview": True,
        "default_icon": "phone/icon.png",
        "user_colour": "#FFFFFF",
        "character_colour": "#FFFFFF",
        "timestamp_colour": "#FFFFFF",
        "sort_channels_by_latest": True,
        "message_padding": 0.025,
        "preview_max_length": 25,
        "emojis": {
            "size": 32,
        },
        "phone_theme": "light",  # default theme
        "light": {
            # colours for light mode
            "message_player_text_colour": "#FFFFFF",
            "message_character_text_colour": "#ffffff",
            "timestamp_text_colour": "#bdbdbd",
            "header_text_colour": "#FFFFFF",
            "channel_name_text_colour": "#FFFFFF",
            "channel_preview_text_colour": "#FFFFFF",
            "sender_name_text_colour": "#FFFFFF",
            "channel_divider_colour": "#bdbdbd",
            "channel_button_hover_background": "#a7a7a7",
            "empty_channel_text_colour": "#FFFFFF",
            # images for light mode
            "screen_background_image": "phone/screen.png",
            "header_background_image": "phone/header.png",
            "base_background_image": "phone/base.png",
            "back_button_idle_image": "phone/back.png",
            "back_button_hover_image": "phone/back_hover.png",
            "back_button_notif_image": "phone/back_notif.png",
            "notification_dot_image": "phone/notif.png",
            "player_bubble_image": "phone/player_bubble.png",
            "player_bubble_hover_image": "phone/player_bubble_hover.png",
            "character_bubble_image": "phone/character_bubble.png",
        },
        "dark": { 
            # colours for dark mode
            "message_player_text_colour": "#FFFFFF",
            "message_character_text_colour": "#FFFFFF",
            "timestamp_text_colour": "#AAAAAA",
            "header_text_colour": "#FFFFFF",
            "channel_name_text_colour": "#FFFFFF",
            "channel_preview_text_colour": "#BBBBBB",
            "sender_name_text_colour": "#AAAAAA",
            "channel_divider_colour": "#444444",
            "channel_button_hover_background": "#333333",
            "empty_channel_text_colour": "#FFFFFF",
            # dark mode images
            "screen_background_image": "phone/skins/dark_mode/screen.png",
            "header_background_image": "phone/skins/dark_mode/header.png",
            "base_background_image": "phone/skins/dark_mode/base.png",
            "back_button_idle_image": "phone/skins/dark_mode/back.png",
            "back_button_notif_image": "phone/skins/dark_mode/back_notif.png",
            "notification_dot_image": "phone/skins/dark_mode/notif.png",
            "player_bubble_image": "phone/skins/dark_mode/player_bubble.png",
            "player_bubble_hover_image": "phone/skins/dark_mode/player_bubble_hover.png",
            "character_bubble_image": "phone/skins/dark_mode/character_bubble.png",
        },
        "flip": {
            # colours for flip phone mode
            "message_player_text_colour": "#FFFFFF",
            "message_character_text_colour": "#000000",
            "timestamp_text_colour": "#000000",
            "header_text_colour": "#000000",
            "channel_name_text_colour": "#000000",
            "channel_preview_text_colour": "#555555",
            "sender_name_text_colour": "#666666",
            "channel_divider_colour": "#E0E0E0",
            "channel_button_hover_background": "#EFEFEF",
            "empty_channel_text_colour": "#000000",
            # images for flip phone mode
            "screen_background_image": "phone/skins/flip_phone/screen.png",
            "header_background_image": "phone/header.png",
            "base_background_image": "phone/skins/flip_phone/base.png",
            "back_button_idle_image": "phone/back.png",
            "back_button_notif_image": "phone/back_notif.png",
            "notification_dot_image": "phone/notif.png",
            "player_bubble_image": "phone/player_bubble.png",
            "player_bubble_hover_image": "phone/player_bubble_hover.png",
            "character_bubble_image": "phone/character_bubble.png",
        },
        "status_bar": {
            # colours for status bar phone mode
            "message_player_text_colour": "#FFFFFF",
            "message_character_text_colour": "#000000",
            "timestamp_text_colour": "#000000",
            "header_text_colour": "#000000",
            "channel_name_text_colour": "#000000",
            "channel_preview_text_colour": "#555555",
            "sender_name_text_colour": "#666666",
            "channel_divider_colour": "#E0E0E0",
            "channel_button_hover_background": "#EFEFEF",
            "empty_channel_text_colour": "#000000",
            # images for status bar phone mode
            "screen_background_image": "phone/screen.png",
            "header_background_image": "phone/skins/status_bar/header.png",
            "base_background_image": "phone/base.png",
            "back_button_idle_image": "phone/back.png",
            "back_button_notif_image": "phone/back_notif.png",
            "notification_dot_image": "phone/notif.png",
            "player_bubble_image": "phone/player_bubble.png",
            "player_bubble_hover_image": "phone/player_bubble_hover.png",
            "character_bubble_image": "phone/character_bubble.png",
        },
        # Gameplay Configurations
        "pause": { # no pause = messages will not wait for user time or user input before sending the next one
            "do_pause": True, # should we wait for a click to send the next message? like traditional dialogue
            "pause_time": False, # if we want to pause, should we auto-continue after a set amount of time? if false, just wait for a click
            "pause_length": 1.0 # if using pause_time, how long do we wait?
        }
    }

    # variables to hold the phone data
    phone_channel_data = {} # {channel_name: {"display_name": "...", "icon": "...", "participants": [], "is_group": False}}
    phone_channels = {}  # {channel_name: [(id, sender, message_string, kind, ...), ...]}
    channel_last_message_id = {} # {channel_name: last_id}
    channel_seen_latest = {} # {channel_name: seen_status}
    channel_notifs = {} # {channel_name: notification_status} (True/False)
    channel_visible = {} # {channel_name: visible_status} (True/False)
    current_phone_view = "channel_list"
    disable_phone_menu_switch = False
    phone_choice_options = [] # current active choices
    phone_choice_channel = None
    channel_latest_global_id = {} # latest global channel id
    _phone_global_message_counter = 0  # latest global message counter

    # replace inline images natively
    def replace_emojis(text):
        def sub(match):
            name = match.group(1)
            return "{image=%s}" % name
        return re.sub(r"<([A-Za-z0-9_]+)>", sub, text)

    # creates a new phone channel
    def create_phone_channel(channel_id, display_name, participants, icon_path, is_group=False):
        global phone_channel_data, phone_channels, channel_last_message_id, channel_notifs, channel_seen_latest, channel_visible
        if channel_id not in phone_channel_data:
            phone_channel_data[channel_id] = {
                "display_name": display_name,
                "icon": icon_path,
                "participants": participants,
                "is_group": is_group
            }
            phone_channels[channel_id] = []
            channel_last_message_id[channel_id] = 0
            channel_notifs[channel_id] = False
            channel_seen_latest[channel_id] = True
            channel_visible[channel_id] = True
            channel_latest_global_id[channel_id] = 0

    # add messages to a channel in the phone
    def send_phone_message(sender, message_text, channel_name, message_kind=0, summary_alt="none", image_x=320, image_y=320, do_pause=True, log_to_history=True, do_restart=True):
        global _phone_global_message_counter, current_global_id
        if channel_name not in phone_channels:
            renpy.log("Tried to send message to non-existent channel: " + channel_name)
            return
        # sound logic (except timestamps)
        if message_kind != 1:
            if sender == phone_config["phone_player_name"]:
                if phone_config.get("play_sound_send", False):
                    renpy.sound.play("audio/phone/send.mp3", channel="sound9")
            else:
                play_the_sound = True
                if phone_config.get("no_sound_current_chat", False):
                    if current_phone_view == channel_name:
                        play_the_sound = False
                if phone_config.get("play_sound_receive", False) and play_the_sound:
                    renpy.sound.play("audio/phone/receive.mp3", channel="sound9")

        _phone_global_message_counter += 1
        current_global_id = _phone_global_message_counter
        channel_latest_global_id[channel_name] = current_global_id

        last_id = channel_last_message_id.get(channel_name, 0)
        current_id = last_id + 1
        channel_last_message_id[channel_name] = current_id

        # Queue this message id for animation (animate ALL new messages)
        cur = store.channel_pending_anim.get(channel_name, None)
        if not isinstance(cur, list):
            store.channel_pending_anim[channel_name] = []
        store.channel_pending_anim[channel_name].append(current_id)

        message_data = (current_id, sender, message_text, message_kind, current_global_id, summary_alt, image_x, image_y)
        phone_channels[channel_name].append(message_data)

        if current_phone_view != channel_name:
            channel_notifs[channel_name] = True
            channel_seen_latest[channel_name] = False
        else:
            channel_notifs[channel_name] = False
            channel_seen_latest[channel_name] = True

        store.phone_force_scroll_bottom = True

        if do_restart:
            renpy.restart_interaction()


        if log_to_history:
            if message_kind == 0:
                narrator.add_history(kind="adv", who=sender, what=message_text)
            elif message_kind == 1:
                narrator.add_history(kind="adv", who=phone_config["history_timestamp_prefix"], what=message_text)
            elif message_kind == 2:
                narrator.add_history(kind="adv", who=sender, what="Sent a photo.")
        if do_pause and phone_config["pause"]["do_pause"]:
            if phone_config["pause"]["pause_time"]:
                renpy.pause(phone_config["pause"]["pause_length"])
            else:
                renpy.pause()

    # clear notifs / mark as read for all
    def clear_notifications():
        global channel_notifs, channel_seen_latest
        for channel_name in phone_channel_data.keys():
            if channel_name in channel_notifs:
                channel_notifs[channel_name] = False
            if channel_name in channel_seen_latest:
                channel_seen_latest[channel_name] = True
        renpy.restart_interaction()
    
    # reset the phone data
    def reset_phone_data():
        global current_phone_view, phone_channels, channel_last_message_id, channel_notifs, channel_seen_latest, channel_visible, phone_channel_data
        global channel_latest_global_id, _phone_global_message_counter
        phone_channel_data = {}
        phone_channels = {}
        channel_last_message_id = {}
        channel_notifs = {}
        channel_seen_latest = {}
        channel_visible = {}
        channel_latest_global_id = {}
        _phone_global_message_counter = 0
        current_phone_view = "channel_list"
        clear_notifications()
        renpy.restart_interaction()

        ##### AINE #####
        create_phone_channel("aine_dm", "Aine", ["Aine", phone_config["phone_player_name"]], "phone/icons/aine.png")

        ##### FREYA #####
        create_phone_channel("freya_dm", "Freya", ["Freya", phone_config["phone_player_name"]], "phone/icons/freya.png")

        ##### MOON #####
        create_phone_channel("moon_dm", "Moon", ["Moon", phone_config["phone_player_name"]], "phone/icons/moon.png")

        ##### EMMA #####
        create_phone_channel("emma_dm", "Emma", ["Emma", phone_config["phone_player_name"]], "phone/icons/emma.png")

        ##### GWEN #####
        create_phone_channel("gwen_dm", "Gwen", ["Gwen", phone_config["phone_player_name"]], "phone/icons/gwen.png")

        ##### SKY #####
        create_phone_channel("sky_dm", "Sky", ["Sky", phone_config["phone_player_name"]], "phone/icons/sky.png")

        ##### NAOMI #####
        create_phone_channel("naomi_dm", "Naomi", ["Naomi", phone_config["phone_player_name"]], "phone/icons/naomi.png")

        ##### KLARA #####
        create_phone_channel("klara_dm", "Klara", ["Klara", phone_config["phone_player_name"]], "phone/icons/klara.png")

        ##### SHU #####
        create_phone_channel("shu_dm", "Shu", ["Shu", phone_config["phone_player_name"]], "phone/icons/shu.png")

        ##### JUNE #####
        create_phone_channel("june_dm", "June", ["June", phone_config["phone_player_name"]], "phone/icons/june.png")

        ##### CLAIRE #####
        create_phone_channel("claire_dm", "Claire", ["Claire", phone_config["phone_player_name"]], "phone/icons/claire.png")

        ##### JESS #####
        create_phone_channel("jess_dm", "Jess", ["Jess", phone_config["phone_player_name"]], "phone/icons/jess.png")

        ##### LILY #####
        create_phone_channel("lily_dm", "Lily", ["Lily", phone_config["phone_player_name"]], "phone/icons/lily.png")


        ##### AINE #####
        ## 13 months ago ##
        phone_stamp_rel("aine_dm", back_months=13, do_pause=False)
        send_phone_message("Aine", "[mc]...", "aine_dm", do_pause=False, log_to_history=False, do_restart=False)
        send_phone_message("Aine", "I know you're trying to distract yourself, but going back to work this soon isn't the way.", "aine_dm", do_pause=False, log_to_history=False, do_restart=False)
        send_phone_message("Aine", "Your body just went through hell. You have to let it catch up before you start pretending you're okay again.", "aine_dm", do_pause=False, log_to_history=False, do_restart=False)
        send_phone_message("Aine", "Please... give yourself a little room to breathe.", "aine_dm", do_pause=False, log_to_history=False, do_restart=False)
        send_phone_message(phone_config["phone_player_name"], "I'm fine, Aine. Really.", "aine_dm", do_pause=False, log_to_history=False, do_restart=False)
        send_phone_message(phone_config["phone_player_name"], "Lying around all day is driving me insane. I need to move before my brain starts eating itself alive.", "aine_dm", do_pause=False, log_to_history=False, do_restart=False)
        if aineroute:
            send_phone_message("Aine", "Needing something to keep you occupied isn't the same as being okay.", "aine_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message("Aine", "I just... don't want you passing out somewhere I can't reach you.", "aine_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message("Aine", "You scared me once. That's already more than I can handle.", "aine_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message(phone_config["phone_player_name"], "Alright. Two more days of rest. No arguments.", "aine_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message("Aine", "Still not enough... but I'll take the win while I can.", "aine_dm", do_pause=False, log_to_history=False, do_restart=False)

        if allornothingroute:
            phone_stamp_rel("aine_dm", back_months=13, do_pause=False)
            send_phone_message("Aine", "Freya just sent me a photo...", "aine_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message("Aine", "...", "aine_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message("Aine", "......", "aine_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message(phone_config["phone_player_name"], "What? What's going on?", "aine_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message("Aine", "images/ch2ep1_1042.jpg", "aine_dm", 2, do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message("Aine", "😏", "aine_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message(phone_config["phone_player_name"], "Fuck...", "aine_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message("Aine", "She said I wouldn't have the guts to send you something like that.", "aine_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message("Aine", "As if I'm still the prude sister you two love teasing.", "aine_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message("Aine", "Guess I proved her wrong.", "aine_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message(phone_config["phone_player_name"], "Aine... holy! This is... GOD.", "aine_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message("Aine", "Pfft. 😝", "aine_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message("Aine", "Exactly the reaction I pictured.", "aine_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message(phone_config["phone_player_name"], "I came.", "aine_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message("Aine", "Huh?!", "aine_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message("Aine", "You—", "aine_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message("Aine", "[mc]... it hasn't even been a full minute.", "aine_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message(phone_config["phone_player_name"], "You sent me a photo like {b}that{/b}. What did you expect?", "aine_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message("Aine", "Maybe a gasp. A flustered keyboard smash. Not—", "aine_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message("Aine", "... that.", "aine_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message(phone_config["phone_player_name"], "Blame yourself for being so fucking hot. Honestly? A public safety hazard.", "aine_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message("Aine", "If I'm a hazard, you're hopeless. And I'm not even a little sorry.", "aine_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message("Aine", "I love you, though! 😊😘", "aine_dm", do_pause=False, log_to_history=False, do_restart=False)

        ## 12 months ago ##
        phone_stamp_rel("aine_dm", back_months=12, do_pause=False)
        send_phone_message("Aine", "Oh my god—I'm so sorry. I didn't think before I said that. 😭", "aine_dm", do_pause=False, log_to_history=False, do_restart=False)

        send_phone_message(phone_config["phone_player_name"], "Someone was bound to mention him sooner or later.", "aine_dm", do_pause=False, log_to_history=False, do_restart=False)
        send_phone_message(phone_config["phone_player_name"], "Even I'm surprised she kept it in for as long as she did.", "aine_dm", do_pause=False, log_to_history=False, do_restart=False)
        if aineroute:
            send_phone_message("Aine", "Can we talk...? I suddenly feel dizzy. It brought back things I wasn't ready to feel.", "aine_dm", 3, do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message(phone_config["phone_player_name"], "Stay where you are. I'm coming.", "aine_dm", do_pause=False, log_to_history=False, do_restart=False)

        if aineroute:
            phone_stamp_rel("aine_dm", back_months=12, do_pause=False)
            send_phone_message(phone_config["phone_player_name"], "Hey, I was thinking...", "aine_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message(phone_config["phone_player_name"], "Should we... I don't know... have pet names or something?", "aine_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message("Aine", "...", "aine_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message("Aine", "[mc], no.", "aine_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message("Aine", "Pet names never felt real to me.", "aine_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message("Aine", "Anyone can say \"baby\" or \"honey.\" It doesn't make the feeling behind it true.", "aine_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message("Aine", "And to be honest, after everything I put you through back then, I don't feel like I've earned anything beyond your actual name.", "aine_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message("Aine", "Labels don't prove love. What I do for you now does.", "aine_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message(phone_config["phone_player_name"], "I wasn't trying to force anything. Just thought maybe you'd want one.", "aine_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message("Aine", "I know. And it's sweet that you asked.", "aine_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message("Aine", "But I like your name. It feels honest. Honest hits deeper than cute.", "aine_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message("Aine", "And you can keep calling me Aine. That's enough for me.", "aine_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message(phone_config["phone_player_name"], "You really gotta let go of the past, though.", "aine_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message(phone_config["phone_player_name"], "I have. You can, too.", "aine_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message("Aine", "I'm trying. It's just... not that simple.", "aine_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message("Aine", "You do remember I used to pick on you, right?", "aine_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message("Aine", "Most people wouldn't forgive their childhood tormentor so easily.", "aine_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message(phone_config["phone_player_name"], "Yeah, well... I'm not most people.", "aine_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message(phone_config["phone_player_name"], "And you're not that girl anymore.", "aine_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message("Aine", "Maybe.", "aine_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message("Aine", "But sometimes I look at you and think, \"Do I really deserve this?\"", "aine_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message(phone_config["phone_player_name"], "Oh, trust me. I remember every shove, every glare, every sarcastic hit-and-run.", "aine_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message(phone_config["phone_player_name"], "And now look at you—apologizing every other day. Life's hilarious.", "aine_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message("Aine", "I'm trying to be better, okay?", "aine_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message("Aine", "And for the record, you were impossible to leave alone. You were adorable when you got annoyed.", "aine_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message(phone_config["phone_player_name"], "So bullying me was your love language?", "aine_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message("Aine", "... Don't say it like that.", "aine_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message("Aine", "It sounds way worse when you make it sound that cute.", "aine_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message(phone_config["phone_player_name"], "Too late. I'm keeping it.", "aine_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message(phone_config["phone_player_name"], "Besides, if I didn't forgive you, I wouldn't have the upgraded version of you now.", "aine_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message("Aine", "Upgraded? Really?", "aine_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message("Aine", "What am I, a software patch?", "aine_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message(phone_config["phone_player_name"], "A very sexy one.", "aine_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message("Aine", "... You're ridiculous.", "aine_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message("Aine", "But fine. I'll try to stop letting the past hover over us.", "aine_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message("Aine", "Just don't expect me to stop apologizing overnight.", "aine_dm", do_pause=False, log_to_history=False, do_restart=False)

        ## 11 months ago ##
        phone_stamp_rel("aine_dm", back_months=11, do_pause=False)
        send_phone_message("Aine", "[mc]...", "aine_dm", do_pause=False, log_to_history=False, do_restart=False)
        send_phone_message("Aine", "I know you're probably acting like you forgot, but I didn't.", "aine_dm", do_pause=False, log_to_history=False, do_restart=False)
        send_phone_message("Aine", "Happy birthday.", "aine_dm", do_pause=False, log_to_history=False, do_restart=False)
        send_phone_message("Aine", "I hope today feels a little lighter than the rest. You deserve at least that much.", "aine_dm", do_pause=False, log_to_history=False, do_restart=False)
        send_phone_message(phone_config["phone_player_name"], "You remembered.", "aine_dm", do_pause=False, log_to_history=False, do_restart=False)
        send_phone_message("Aine", "Yeah. Of course I remembered.", "aine_dm", do_pause=False, log_to_history=False, do_restart=False)
        send_phone_message("Aine", "I've always known the date. Don't ask how. My brain just hoards information when it comes to you.", "aine_dm", do_pause=False, log_to_history=False, do_restart=False)
        send_phone_message("Aine", "Anyway... I hope you're doing something for yourself today.", "aine_dm", do_pause=False, log_to_history=False, do_restart=False)
        if (aineroute and ainepoint == 17):
            send_phone_message(phone_config["phone_player_name"], "Wasn't planning anything special. Haven't really felt like celebrating my birthday lately. Not sure why.", "aine_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message("Aine", "...", "aine_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message("Aine", "That doesn't sound like you.", "aine_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message("Aine", "So what are you up to, hm? Trying to squeeze a reaction out of me?", "aine_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message("Aine", "Do you want someone to spoil you? Tell you you've been a very good boy today?", "aine_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message(phone_config["phone_player_name"], "You really do know me.", "aine_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message(phone_config["phone_player_name"], "Where are you?", "aine_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message("Aine", "In the supermarket.", "aine_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message(phone_config["phone_player_name"], "On my way.", "aine_dm", do_pause=False, log_to_history=False, do_restart=False)
        else:
            send_phone_message(phone_config["phone_player_name"], "Thanks, Aine.", "aine_dm", do_pause=False, log_to_history=False, do_restart=False)

        if (aineroute and ainepoint == 17):
            phone_stamp_rel("aine_dm", back_months=11, do_pause=False)
            send_phone_message(phone_config["phone_player_name"], "images/ch2ep1_1041.jpg", "aine_dm", 2, do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message(phone_config["phone_player_name"], "Look who I stole from the supermarket.", "aine_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message("Aine", "...", "aine_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message("Aine", "You did NOT just send that!", "aine_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message("Aine", "My legs are still shaking and you're out here sending photographic evidence?", "aine_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message("Aine", "[mc]...", "aine_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message("Aine", "Delete it before I spontaneously combust.", "aine_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message("Aine", "I look—", "aine_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message("Aine", "God, I can't even finish that sentence.", "aine_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message(phone_config["phone_player_name"], "You look perfect.", "aine_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message("Aine", "Stop.", "aine_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message("Aine", "I'm already red and you're making it worse.", "aine_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message("Aine", "You drag me into a hotel and then decide to immortalize the moment... unbelievable.", "aine_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message("Aine", "... But don't you dare send that to anyone else.", "aine_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message("Aine", "That's for your eyes only.", "aine_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message("Aine", "Also, while we're on the subject.", "aine_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message("Aine", "A hotel, [mc]? For a {b}few hours{/b}?", "aine_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message("Aine", "Do you have any idea how absurd that is?", "aine_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message(phone_config["phone_player_name"], "It was worth it.", "aine_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message("Aine", "That's not the point.", "aine_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message("Aine", "You dropped that much money just because you felt like dragging me upstairs?", "aine_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message("Aine", "You could've at least *pretended* to compare prices first.", "aine_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message(phone_config["phone_player_name"], "I wasn't really thinking about prices, you know?", "aine_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message("Aine", "Yeah, I know.", "aine_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message("Aine", "You were thinking with something else entirely.", "aine_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message("Aine", "Still, don't make a habit of this. Please.", "aine_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message(phone_config["phone_player_name"], "You sound like you're lecturing me in the afterglow.", "aine_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message("Aine", "Because I {b}am{/b}.", "aine_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message("Aine", "I'm not letting you go broke because you can't control yourself around me.", "aine_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message(phone_config["phone_player_name"], "Really, I don't regret it.", "aine_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message("Aine", "You should at least regret the receipt.", "aine_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message("Aine", "I swear... of all the things to splurge on...", "aine_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message("Aine", "Next time, warn me. I would've booked something cheaper.", "aine_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message(phone_config["phone_player_name"], "You'd really do that?", "aine_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message("Aine", "Yes. Because one of us has to think with their actual brain.", "aine_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message("Aine", "And clearly... it's not going to be you. Aren't you supposed to be saving money for something?", "aine_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message(phone_config["phone_player_name"], "I keep forgetting how practical you are. Okay—no more reckless spending. Promise.", "aine_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message("Aine", "Good.", "aine_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message("Aine", "But... we're talking about the moment itself? Yeah. It was worth it. Thank you, [mc].", "aine_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message("Aine", "You made me feel really special. And you know how much that means to me.", "aine_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message(phone_config["phone_player_name"], "See? Told you it was worth it.", "aine_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message("Aine", "Still! I was supposed to give {b}you{/b} something for your birthday.", "aine_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message("Aine", "Not end up being... {b}that{/b}.", "aine_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message(phone_config["phone_player_name"], "You gave me a ride. Or three.", "aine_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message(phone_config["phone_player_name"], "Really {b}grinded{/b} out that last one.", "aine_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message("Aine", "😳😒", "aine_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message(phone_config["phone_player_name"], "Maybe next time we book a flight to Vegas. Really make things extra special.", "aine_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message("Aine", "For God's sake! NO!", "aine_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message("Aine", "I'm still recovering from the hotel receipt. Don't you dare escalate.", "aine_dm", do_pause=False, log_to_history=False, do_restart=False)

        phone_stamp_rel("aine_dm", back_months=11, do_pause=False)
        send_phone_message("Aine", "Are you free later? I need an extra pair of hands.", "aine_dm", do_pause=False, log_to_history=False, do_restart=False)
        send_phone_message("Aine", "Sky ordered equipment again. Heavy ones. She apparently thinks I have the physique of a forklift. HELP. 😫", "aine_dm", do_pause=False, log_to_history=False, do_restart=False)
        send_phone_message(phone_config["phone_player_name"], "So you thought of me.", "aine_dm", do_pause=False, log_to_history=False, do_restart=False)
        send_phone_message("Aine", "You're the strongest option available!", "aine_dm", do_pause=False, log_to_history=False, do_restart=False)
        send_phone_message("Aine", "And the least likely to complain while doing it...", "aine_dm", do_pause=False, log_to_history=False, do_restart=False)
        send_phone_message(phone_config["phone_player_name"], "Am I really that convenient?", "aine_dm", do_pause=False, log_to_history=False, do_restart=False)
        send_phone_message("Aine", "If the shoe fits.", "aine_dm", do_pause=False, log_to_history=False, do_restart=False)
        send_phone_message("Aine", "But... yes. I could really use your help. PRETTY PLEASE? 😭", "aine_dm", do_pause=False, log_to_history=False, do_restart=False)
        send_phone_message(phone_config["phone_player_name"], "Time?", "aine_dm", do_pause=False, log_to_history=False, do_restart=False)
        send_phone_message("Aine", "Anytime after lunch. Sky will \"supervise,\" which means she'll point at things and sound like a strict principal.", "aine_dm", do_pause=False, log_to_history=False, do_restart=False)
        send_phone_message(phone_config["phone_player_name"], "So I'm the actual labor and she's management. Got it.", "aine_dm", do_pause=False, log_to_history=False, do_restart=False)
        send_phone_message("Aine", "Welcome to my daily suffering.", "aine_dm", do_pause=False, log_to_history=False, do_restart=False)
        send_phone_message("Aine", "At least you help without making me feel like I owe you my firstborn.", "aine_dm", do_pause=False, log_to_history=False, do_restart=False)
        send_phone_message(phone_config["phone_player_name"], "What do I get, then?", "aine_dm", do_pause=False, log_to_history=False, do_restart=False)
        send_phone_message("Aine", "My gratitude. Extremely rare, very precious.", "aine_dm", do_pause=False, log_to_history=False, do_restart=False)
        send_phone_message(phone_config["phone_player_name"], "I'll take it.", "aine_dm", do_pause=False, log_to_history=False, do_restart=False)
        send_phone_message("Aine", "Phew! Thank you.", "aine_dm", do_pause=False, log_to_history=False, do_restart=False)
        send_phone_message(phone_config["phone_player_name"], "You sure you just need help lifting things?", "aine_dm", do_pause=False, log_to_history=False, do_restart=False)
        send_phone_message("Aine", "Don't read into it.", "aine_dm", do_pause=False, log_to_history=False, do_restart=False)
        if aineroute:
            send_phone_message("Aine", "... for now.", "aine_dm", do_pause=False, log_to_history=False, do_restart=False)
        send_phone_message("Aine", "But I'll see you later!", "aine_dm", do_pause=False, log_to_history=False, do_restart=False)

        ## 10 months ago ##
        if aineroute:
            phone_stamp_rel("aine_dm", back_months=10, do_pause=False)
            send_phone_message("Aine", "How was today's shift?", "aine_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message(phone_config["phone_player_name"], "Damn, Aine. It's 11 PM.", "aine_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message("Aine", "I know. I just... can't sleep for some reason.", "aine_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message("Aine", "So... how was it?", "aine_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message(phone_config["phone_player_name"], "How was it, huh...", "aine_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message(phone_config["phone_player_name"], "Long.", "aine_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message(phone_config["phone_player_name"], "Loud.", "aine_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message(phone_config["phone_player_name"], "And my feet hate me.", "aine_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message("Aine", "You say that every week...", "aine_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message("Aine", "Try resting instead of pretending you're made of steel.", "aine_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message(phone_config["phone_player_name"], "Here you go with the nagging again.", "aine_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message("Aine", "Just checking on you.", "aine_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message("Aine", "I can stop caring if you want me to.", "aine_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message(phone_config["phone_player_name"], "Didn't say that.", "aine_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message(phone_config["phone_player_name"], "Customers were extra fun today.", "aine_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message(phone_config["phone_player_name"], "Had a guy argue with me about the size of his drink for ten minutes.", "aine_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message("Aine", "Let me guess... Freya stepped in and actually fought with him?", "aine_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message(phone_config["phone_player_name"], "How did you know that?", "aine_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message("Aine", "I don't know. Maybe because we crawled out of the same hole? 😑", "aine_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message(phone_config["phone_player_name"], "LMAO! 🤣", "aine_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message("Aine", "We both have the fighting spirit. She just swings it faster.", "aine_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message(phone_config["phone_player_name"], "Yeah, I've noticed.", "aine_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message(phone_config["phone_player_name"], "How's the online teaching thing going? You haven't talked about it lately.", "aine_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message("Aine", "The kids were out for blood today.", "aine_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message(phone_config["phone_player_name"], "Rough class?", "aine_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message("Aine", "One of them learned how to screen-share memes.", "aine_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message("Aine", "In the middle of reading time.", "aine_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message("Aine", "Fifteen tiny faces laughing at a dancing potato.", "aine_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message(phone_config["phone_player_name"], "And what did you do?", "aine_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message("Aine", "Pretended I wasn't dying inside.", "aine_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message("Aine", "Then bribed them with stickers so they'd behave.", "aine_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message(phone_config["phone_player_name"], "Sounds like you. Cold exterior, marshmallow core.", "aine_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message("Aine", "Don't start.", "aine_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message("Aine", "I'm only a marshmallow for one person, and he knows who he is.", "aine_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message(phone_config["phone_player_name"], "If he's smart, he won't take that for granted.", "aine_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message("Aine", "Good thing he's smarter than he looks. 😘", "aine_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message(phone_config["phone_player_name"], "Wanna hang out by the pool? I've got beer in the fridge. Might help you sleep.", "aine_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message("Aine", "Yeah, sure!", "aine_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message(phone_config["phone_player_name"], "I'll be waiting there.", "aine_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message("Aine", "Give me a minute. Need to put on PJs.", "aine_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message("Aine", "I'm only in panties right now, and I'm not walking out like that.", "aine_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message(phone_config["phone_player_name"], "No, don't!", "aine_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message("Aine", "... Of course that's your first reaction.", "aine_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message(phone_config["phone_player_name"], "You can't just drop \"only in panties\" and expect me to behave.", "aine_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message("Aine", "Too bad. I'm choosing warmth and dignity.", "aine_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message(phone_config["phone_player_name"], "Killjoy...", "aine_dm", do_pause=False, log_to_history=False, do_restart=False)

            # LATER THAT NIGHT
            phone_stamp_rel("aine_dm", back_months=10, do_pause=False)
            send_phone_message("Aine", "images/ch2ep1_1043.jpg", "aine_dm", 2, do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message("Aine", "Good night, [mc]. Thanks for the company.", "aine_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message("Aine", "And... I love you. Just in case I didn't say it enough.", "aine_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message(phone_config["phone_player_name"], "I love you too, Aine. Sleep well.", "aine_dm", do_pause=False, log_to_history=False, do_restart=False)

        ## 9 months ago ##
        phone_stamp_rel("aine_dm", back_months=9, do_pause=False)
        send_phone_message("Aine", "You said you had something important to tell me?", "aine_dm", do_pause=False, log_to_history=False, do_restart=False)
        send_phone_message(phone_config["phone_player_name"], "Yeah. I finally made a decision about the group.", "aine_dm", do_pause=False, log_to_history=False, do_restart=False)
        send_phone_message("Aine", "Really? You're sure you're not rushing this? Because that sounds... big.", "aine_dm", do_pause=False, log_to_history=False, do_restart=False)
        send_phone_message(phone_config["phone_player_name"], "Yeah. I've made up my mind. We're not running it like a mafia anymore.", "aine_dm", do_pause=False, log_to_history=False, do_restart=False)
        send_phone_message(phone_config["phone_player_name"], "We're turning everything into a charity foundation. Just like Hera wanted.", "aine_dm", do_pause=False, log_to_history=False, do_restart=False)
        send_phone_message("Aine", "...", "aine_dm", do_pause=False, log_to_history=False, do_restart=False)
        send_phone_message("Aine", "You're serious?", "aine_dm", do_pause=False, log_to_history=False, do_restart=False)
        send_phone_message(phone_config["phone_player_name"], "I wouldn't have said it if I wasn't.", "aine_dm", do_pause=False, log_to_history=False, do_restart=False)
        send_phone_message("Aine", "As strange as it is to say... she'd be proud of you.", "aine_dm", do_pause=False, log_to_history=False, do_restart=False)
        send_phone_message("Aine", "More than you think.", "aine_dm", do_pause=False, log_to_history=False, do_restart=False)
        send_phone_message(phone_config["phone_player_name"], "You think so?", "aine_dm", do_pause=False, log_to_history=False, do_restart=False)
        send_phone_message("Aine", "I know so.", "aine_dm", do_pause=False, log_to_history=False, do_restart=False)
        send_phone_message("Aine", "Mother wanted to build something good. Something that gave back.", "aine_dm", do_pause=False, log_to_history=False, do_restart=False)
        send_phone_message("Aine", "And you're choosing to finish what she started.", "aine_dm", do_pause=False, log_to_history=False, do_restart=False)
        send_phone_message(phone_config["phone_player_name"], "Feels strange.", "aine_dm", do_pause=False, log_to_history=False, do_restart=False)
        send_phone_message(phone_config["phone_player_name"], "Like I'm rewriting something that was meant to stay dark.", "aine_dm", do_pause=False, log_to_history=False, do_restart=False)
        send_phone_message("Aine", "Dark doesn't have to stay dark.", "aine_dm", do_pause=False, log_to_history=False, do_restart=False)
        send_phone_message("Aine", "The moment someone refuses to let it swallow them, it changes.", "aine_dm", do_pause=False, log_to_history=False, do_restart=False)
        send_phone_message("Aine", "That's what you're doing.", "aine_dm", do_pause=False, log_to_history=False, do_restart=False)
        send_phone_message(phone_config["phone_player_name"], "I'm trying. I just... don't feel like I should be leading this organization at all.", "aine_dm", do_pause=False, log_to_history=False, do_restart=False)
        send_phone_message("Aine", "Trying is enough.", "aine_dm", do_pause=False, log_to_history=False, do_restart=False)
        send_phone_message("Aine", "And you're not doing it alone. You have me.", "aine_dm", do_pause=False, log_to_history=False, do_restart=False)
        send_phone_message("Aine", "Also...", "aine_dm", do_pause=False, log_to_history=False, do_restart=False)
        send_phone_message("Aine", "I'm genuinely glad it's you stepping up.", "aine_dm", do_pause=False, log_to_history=False, do_restart=False)
        send_phone_message("Aine", "Because we both know I have no idea what to do with that kind of power.", "aine_dm", do_pause=False, log_to_history=False, do_restart=False)
        send_phone_message("Aine", "So if you're feeling lost... remember I'm right there with you.", "aine_dm", do_pause=False, log_to_history=False, do_restart=False)
        send_phone_message(phone_config["phone_player_name"], "Good. Hearing that makes it feel a little less heavy.", "aine_dm", do_pause=False, log_to_history=False, do_restart=False)
        send_phone_message("Aine", "We should talk about this in person. Not through a screen.", "aine_dm", do_pause=False, log_to_history=False, do_restart=False)
        send_phone_message("Aine", "If you're not too tired later... meet me by the pool?", "aine_dm", do_pause=False, log_to_history=False, do_restart=False)
        send_phone_message("Aine", "I'll bring the beer.", "aine_dm", do_pause=False, log_to_history=False, do_restart=False)
        send_phone_message(phone_config["phone_player_name"], "Sounds good.", "aine_dm", do_pause=False, log_to_history=False, do_restart=False)
        send_phone_message("Aine", "Then I'll see you later.", "aine_dm", do_pause=False, log_to_history=False, do_restart=False)

        phone_stamp_rel("aine_dm", back_months=9, do_pause=False)
        send_phone_message("Aine", "[mc], where are you?", "aine_dm", do_pause=False, log_to_history=False, do_restart=False)
        send_phone_message(phone_config["phone_player_name"], "Shit! Sorry, my shift schedule got moved again.", "aine_dm", do_pause=False, log_to_history=False, do_restart=False)
        send_phone_message("Aine", "I see. It's okay.", "aine_dm", do_pause=False, log_to_history=False, do_restart=False)
        send_phone_message("Aine", "So I went through the documents Hera left behind.", "aine_dm", do_pause=False, log_to_history=False, do_restart=False)
        send_phone_message("Aine", "There's a lot more to this whole \"charity reform\" than we thought.", "aine_dm", do_pause=False, log_to_history=False, do_restart=False)
        send_phone_message(phone_config["phone_player_name"], "Yeah? What's the damage?", "aine_dm", do_pause=False, log_to_history=False, do_restart=False)
        send_phone_message("Aine", "First: we have to dissolve the shell companies. All of them.", "aine_dm", do_pause=False, log_to_history=False, do_restart=False)
        send_phone_message("Aine", "Then re-register the entire organization as a legal foundation.", "aine_dm", do_pause=False, log_to_history=False, do_restart=False)
        send_phone_message("Aine", "And don't even get me started on the tax documentation.", "aine_dm", do_pause=False, log_to_history=False, do_restart=False)
        send_phone_message(phone_config["phone_player_name"], "Sounds fun.", "aine_dm", do_pause=False, log_to_history=False, do_restart=False)
        send_phone_message("Aine", "Don't joke. This is serious.", "aine_dm", do_pause=False, log_to_history=False, do_restart=False)
        send_phone_message("Aine", "We can't build a charity with questionable money floating around.", "aine_dm", do_pause=False, log_to_history=False, do_restart=False)
        send_phone_message(phone_config["phone_player_name"], "Relax. I'm calling Sicae Agency to help us handle the paperwork.", "aine_dm", do_pause=False, log_to_history=False, do_restart=False)
        if aineroute:
            send_phone_message("Aine", "... Already?", "aine_dm", do_pause=False)
            send_phone_message("Aine", "You didn't even ask me first.", "aine_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message(phone_config["phone_player_name"], "I thought you'd want things done fast.", "aine_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message("Aine", "Yes, but I also want to know who's sticking their hands into our documents.", "aine_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message("Aine", "What if they mess something up?", "aine_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message(phone_config["phone_player_name"], "They won't. Sicae handles corporate conversions all the time.", "aine_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message(phone_config["phone_player_name"], "They can manage everything, and I trust them.", "aine_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message("Aine", "Tch. That makes one of us.", "aine_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message(phone_config["phone_player_name"], "You're not a fan of them?", "aine_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message("Aine", "It's not that I dislike them. I just need them {b}not{/b} to screw us over.", "aine_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message(phone_config["phone_player_name"], "You're so dramatic.", "aine_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message("Aine", "I'm being realistic here!", "aine_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message("Aine", "You're the one who thinks every problem can be fixed with charm and one deep breath.", "aine_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message(phone_config["phone_player_name"], "It works most of the time.", "aine_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message("Aine", "Not with the government, it doesn't.", "aine_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message(phone_config["phone_player_name"], "Okay, okay. How about this...", "aine_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message(phone_config["phone_player_name"], "You handle reviewing the legitimacy reports, and I'll let Sicae deal with the dirty history.", "aine_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message("Aine", "... So I get the boring parts?", "aine_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message(phone_config["phone_player_name"], "You get the parts you're better at.", "aine_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message("Aine", "Hmph.", "aine_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message("Aine", "Fine.", "aine_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message("Aine", "But if your agency screws up even one line, I'm blaming you personally.", "aine_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message(phone_config["phone_player_name"], "Noted. I'll take the hit like a man.", "aine_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message("Aine", "Good to know.", "aine_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message("Aine", "Because despite all this arguing... I'm excited.", "aine_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message("Aine", "We're actually doing it, [mc].", "aine_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message(phone_config["phone_player_name"], "Yeah. We are.", "aine_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message(phone_config["phone_player_name"], "Let's talk more later, alright?", "aine_dm", do_pause=False, log_to_history=False, do_restart=False)
        else:
            send_phone_message("Aine", "Then as long as you trust them.", "aine_dm", do_pause=False, log_to_history=False, do_restart=False)

        ## 8 months ago ##
        phone_stamp_rel("aine_dm", back_months=8, do_pause=False)
        send_phone_message("Aine", "[mc]. You up?", "aine_dm", do_pause=False, log_to_history=False, do_restart=False)
        send_phone_message(phone_config["phone_player_name"], "Yeah. What's going on?", "aine_dm", do_pause=False, log_to_history=False, do_restart=False)
        send_phone_message("Aine", "We actually did it.", "aine_dm", do_pause=False, log_to_history=False, do_restart=False)
        send_phone_message("Aine", "The papers went through. The foundation is officially recognized.", "aine_dm", do_pause=False, log_to_history=False, do_restart=False)
        send_phone_message("Aine", "I'm... still processing.", "aine_dm", do_pause=False, log_to_history=False, do_restart=False)
        send_phone_message(phone_config["phone_player_name"], "No more mafia. Just a charity now.", "aine_dm", do_pause=False, log_to_history=False, do_restart=False)
        send_phone_message(phone_config["phone_player_name"], "Feels surreal.", "aine_dm", do_pause=False, log_to_history=False, do_restart=False)
        send_phone_message("Aine", "Surreal is one word.", "aine_dm", do_pause=False, log_to_history=False, do_restart=False)
        send_phone_message("Aine", "Terrifying works too.", "aine_dm", do_pause=False, log_to_history=False, do_restart=False)
        send_phone_message("Aine", "But mostly... good. Really good.", "aine_dm", do_pause=False, log_to_history=False, do_restart=False)
        if (aineroute and ainepoint == 17):
            send_phone_message(phone_config["phone_player_name"], "You wanna celebrate?", "aine_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message("Aine", "By the pool?", "aine_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message("Aine", "With beer?", "aine_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message(phone_config["phone_player_name"], "Obviously.", "aine_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message("Aine", "Alright. Give me five minutes.", "aine_dm", do_pause=False, log_to_history=False, do_restart=False)

            # LATER THAT NIGHT — AINE TEXTS FIRST
            phone_stamp_rel("aine_dm", back_months=8, do_pause=False)
            send_phone_message("Aine", "Okay. I'm here.", "aine_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message("Aine", "The water looks cleaner than usual. Weird.", "aine_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message(phone_config["phone_player_name"], "I cleaned it. Already anticipated this.", "aine_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message(phone_config["phone_player_name"], "I was basically standing next to a huge steaming bowl of foreshadowing.", "aine_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message("Aine", "LOL! 😂", "aine_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message("Aine", "I... didn't think we'd get this far.", "aine_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message("Aine", "Part of me kept waiting for something to fall apart.", "aine_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message(phone_config["phone_player_name"], "But it didn't, right?", "aine_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message(phone_config["phone_player_name"], "That's because you did good, Aine.", "aine_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message("Aine", "Stop...", "aine_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message("Aine", "You're going to make me weirdly emotional.", "aine_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message(phone_config["phone_player_name"], "Come on, it's a big night. You're allowed.", "aine_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message("Aine", "It still feels strange hearing praise from you. The headpats and everything.", "aine_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message("Aine", "I'm used to being the one scolding you about money, and pretty much... everything.", "aine_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message(phone_config["phone_player_name"], "We can switch roles tonight if you want.", "aine_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message("Aine", "Ha. Sure.", "aine_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message("Aine", "You couldn't scold me if your life depended on it.", "aine_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message(phone_config["phone_player_name"], "Maybe I just like it when you're soft.", "aine_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message(phone_config["phone_player_name"], "And I like those {b}soft{/b} parts of yours. Especially the one that gets wet when you hear my voice.", "aine_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message("Aine", "Don't... I'm already holding a beer.", "aine_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message(phone_config["phone_player_name"], "That doesn't sound like you're telling me to stop.", "aine_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message("Aine", "You're impossible...", "aine_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message("Aine", "Well? I'm waiting.", "aine_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message("Aine", "And so goddamn ready...", "aine_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message(phone_config["phone_player_name"], "I can hear that sultry voice from up here.", "aine_dm", do_pause=False, log_to_history=False, do_restart=False)

            phone_stamp_rel("aine_dm", back_months=8, do_pause=False)
            send_phone_message(phone_config["phone_player_name"], "{b}\"1 Night in Aine\"{/b}", "aine_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message(phone_config["phone_player_name"], "images/ch2ep1_1044.jpg", "aine_dm", 2, do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message(phone_config["phone_player_name"], "images/ch2ep1_1045.jpg", "aine_dm", 2, do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message(phone_config["phone_player_name"], "images/ch2ep1_1046.jpg", "aine_dm", 2, do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message("Aine", "Oh my god... I look so...", "aine_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message(phone_config["phone_player_name"], "You look so...?", "aine_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message("Aine", "Horny and... needy...", "aine_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message("Aine", "Like I wasn't thinking straight. As if I didn't care if anyone else sees us.", "aine_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message("Aine", "Not sure if it's the alcohol, but I didn't know I could look that open.", "aine_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message(phone_config["phone_player_name"], "Look at you. My daring little show-off.", "aine_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message("Aine", "[mc]! I'm actually liking this, and I'm sober! What have you done to me?!", "aine_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message(phone_config["phone_player_name"], "I don't know. You were the one so eager to do it outside. I was just enjoying the adventure.", "aine_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message(phone_config["phone_player_name"], "But glad to know you can finally articulate what you feel. I'm so proud of you.", "aine_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message("Aine", "😳😖", "aine_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message("Aine", "Uhm... Can I save these?", "aine_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message("Aine", "Yes, I know, I know! Not for research purposes!", "aine_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message(phone_config["phone_player_name"], "All yours, my lady.", "aine_dm", do_pause=False, log_to_history=False, do_restart=False)

        ## 7 months ago ##
        phone_stamp_rel("aine_dm", back_months=7, do_pause=False)
        send_phone_message("Aine", "Emma seemed tired today. You too.", "aine_dm", do_pause=False, log_to_history=False, do_restart=False)
        send_phone_message(phone_config["phone_player_name"], "Long week.", "aine_dm", do_pause=False, log_to_history=False, do_restart=False)
        send_phone_message("Aine", "What have you two been up to?", "aine_dm", do_pause=False, log_to_history=False, do_restart=False)
        send_phone_message(phone_config["phone_player_name"], "Well... kind of a long story.", "aine_dm", do_pause=False, log_to_history=False, do_restart=False)
        send_phone_message(phone_config["phone_player_name"], "She asked for some help.", "aine_dm", do_pause=False, log_to_history=False, do_restart=False)
        send_phone_message("Aine", "Help with what?", "aine_dm", do_pause=False, log_to_history=False, do_restart=False)
        send_phone_message(phone_config["phone_player_name"], "She's got a new case. Complicated one.", "aine_dm", do_pause=False, log_to_history=False, do_restart=False)
        send_phone_message(phone_config["phone_player_name"], "I offered Sicae's hand to lighten the load.", "aine_dm", do_pause=False, log_to_history=False, do_restart=False)
        send_phone_message("Aine", "They know what they're doing.", "aine_dm", do_pause=False, log_to_history=False, do_restart=False)
        send_phone_message("Aine", "If Sicae's involved, I'm not worried.", "aine_dm", do_pause=False, log_to_history=False, do_restart=False)
        send_phone_message(phone_config["phone_player_name"], "Glad to know you trust them now.", "aine_dm", do_pause=False, log_to_history=False, do_restart=False)

        if aineroute:
            phone_stamp_rel("aine_dm", back_months=7, do_pause=False)
            send_phone_message(phone_config["phone_player_name"], "Guess who just got scolded.", "aine_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message("Aine", "What did you do this time?", "aine_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message(phone_config["phone_player_name"], "Apparently I \"overshared\" her case with you.", "aine_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message(phone_config["phone_player_name"], "Which is funny, because I didn't even tell you anything.", "aine_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message("Aine", "... Oh no.", "aine_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message("Aine", "Emma scolded you?", "aine_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message(phone_config["phone_player_name"], "Yes.", "aine_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message(phone_config["phone_player_name"], "Yes she did.", "aine_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message("Aine", "Pffft!", "aine_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message("Aine", "Sorry. I shouldn't laugh.", "aine_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message("Aine", "But I'm absolutely laughing. LOL! 🤣", "aine_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message(phone_config["phone_player_name"], "Wow. Thanks for the emotional support.", "aine_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message("Aine", "Hey, I get it. Emma's terrifying when she goes serious.", "aine_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message("Aine", "But watching her scold you for something you didn't even do? That's comedy gold.", "aine_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message(phone_config["phone_player_name"], "Do we entertain you? 😒", "aine_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message("Aine", "Maybe...?", "aine_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message("Aine", "But if it makes you feel better...", "aine_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message("Aine", "I already forgot half of what you told me anyway.", "aine_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message(phone_config["phone_player_name"], "That somehow makes it worse.", "aine_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message("Aine", "😝", "aine_dm", do_pause=False, log_to_history=False, do_restart=False)

        ## 6 months ago ##
        if (aineroute and ainepoint == 17):
            phone_stamp_rel("aine_dm", back_months=6, do_pause=False)
            send_phone_message("Aine", "Hey, [mc]? You there?", "aine_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message(phone_config["phone_player_name"], "Yeah?", "aine_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message("Aine", "You know... I've been thinking.", "aine_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message(phone_config["phone_player_name"], "Uh-huh?", "aine_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message("Aine", "Or more like... looking.", "aine_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message(phone_config["phone_player_name"], "Aine... if you're this flustered, I know it's something sex-adjacent.", "aine_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message(phone_config["phone_player_name"], "Just say it.", "aine_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message("Aine", "I'm looking at the photos you sent me and...", "aine_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message(phone_config["phone_player_name"], "And...?", "aine_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message("Aine", "[mc], I want more...", "aine_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message(phone_config["phone_player_name"], "Not \"kinda\" more? Not \"maybe\" more?", "aine_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message(phone_config["phone_player_name"], "You mean you {b}definitely{/b} want more? More sex?", "aine_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message("Aine", "No, not just the sex itself...", "aine_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message("Aine", "I want you to look at me more.", "aine_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message("Aine", "images/ch2ep1_1047.jpg", "aine_dm", 2, do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message(phone_config["phone_player_name"], "HOLY SHIET!", "aine_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message("Aine", "You like that...? 🫣", "aine_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message(phone_config["phone_player_name"], "Do you even have to ask?", "aine_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message("Aine", "Remember the first photo I sent you months ago?", "aine_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message("Aine", "And you said you...", "aine_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message(phone_config["phone_player_name"], "Let's just say I didn't exactly look at it once and move on.", "aine_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message("Aine", "Haha!", "aine_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message("Aine", "Yeah... that felt good to hear. REALLY good.", "aine_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message(phone_config["phone_player_name"], "If you want to do this more often from now on, I am {b}absolutely{/b} not complaining.", "aine_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message(phone_config["phone_player_name"], "Not even a little. NO, MA'AM.", "aine_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message("Aine", "So... is that a yes?", "aine_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message(phone_config["phone_player_name"], "YES. Hell yes.", "aine_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message("Aine", "Phew... oh my god. That took a lot out of me.", "aine_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message(phone_config["phone_player_name"], "You did great, you know.", "aine_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message(phone_config["phone_player_name"], "Actually saying what you want? I love that.", "aine_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message("Aine", "Please don't make me shy now...", "aine_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message("Aine", "But... thank you for liking my newfound... glory. 😋", "aine_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message(phone_config["phone_player_name"], "LMAO. Always liked that band.", "aine_dm", do_pause=False, log_to_history=False, do_restart=False)

        if (aineroute and ainepoint == 17):
            phone_stamp_rel("aine_dm", back_months=6, do_pause=False)
            send_phone_message("Aine", "On my way home.", "aine_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message("Aine", "Also... I took something for you.", "aine_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message("Aine", "images/ch2ep1_1048.jpg", "aine_dm", 2, do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message(phone_config["phone_player_name"], "HOOOOOOOOO! God bless boobs!", "aine_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message(phone_config["phone_player_name"], "I should've known the moment you said \"something for you.\"", "aine_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message("Aine", "You surprised?", "aine_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message(phone_config["phone_player_name"], "Not really. I always knew you had it in you.", "aine_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message(phone_config["phone_player_name"], "Just trying to figure out when exactly my fiancée turned into a public menace.", "aine_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message("Aine", "You like it, though?", "aine_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message(phone_config["phone_player_name"], "Yeah, and that's the problem.", "aine_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message(phone_config["phone_player_name"], "You drop stuff like this and expect my brain to function normally. 😵‍💫", "aine_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message("Aine", "It's motivating me, at least. 😊", "aine_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message(phone_config["phone_player_name"], "Just be careful. I love the adventure, but I swear, if someone else even touches... 😤", "aine_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message("Aine", "Relax. I'm being careful.", "aine_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message("Aine", "No one even saw anything. I checked. Promise.", "aine_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message("Aine", "I'm just for you.", "aine_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message(phone_config["phone_player_name"], "You know exactly how to make my day. Or night...", "aine_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message("Aine", "I'm getting off in a few stops.", "aine_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message("Aine", "Try not to melt before I get there.", "aine_dm", do_pause=False, log_to_history=False, do_restart=False)

        ## 5 months ago ##
        if (aineroute and ainepoint == 17):
            phone_stamp_rel("aine_dm", back_months=5, do_pause=False)
            send_phone_message("Aine", "I... might've taken another one today. Or two.", "aine_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message("Aine", "You should probably be somewhere private before opening it.", "aine_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message("Aine", "images/ch2ep1_1049.jpg", "aine_dm", 2, do_pause=False)
            send_phone_message("Aine", "images/ch2ep1_1050.jpg", "aine_dm", 2, do_pause=False)
            send_phone_message(phone_config["phone_player_name"], "😱👅💦", "aine_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message(phone_config["phone_player_name"], "Aine, what am I supposed to do with myself after seeing this?", "aine_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message("Aine", "Uhh... appreciate it quietly? Tell me it turns you on?", "aine_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message(phone_config["phone_player_name"], "Quietly is not happening. I want to lick every drop off you. 😜", "aine_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message(phone_config["phone_player_name"], "You look unreal. And very aware of what you're doing to me.", "aine_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message("Aine", "Good. Then the lighting wasn't a waste.", "aine_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message(phone_config["phone_player_name"], "Lighting? You planned this?", "aine_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message("Aine", "Hey, I'm not half-assing our tradition.", "aine_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message("Aine", "If I'm sending you something, it should be worth the heart attack.", "aine_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message(phone_config["phone_player_name"], "Mission accomplished. I'm still processing.", "aine_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message("Aine", "... You okay?", "aine_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message(phone_config["phone_player_name"], "Don't worry about me. Just wiped my phone. Got wet.", "aine_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message("Aine", "Got wet with WHAT?!", "aine_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message(phone_config["phone_player_name"], "😏😏😏", "aine_dm", do_pause=False, log_to_history=False, do_restart=False)

        ## 4 months ago ##
        if (aineroute and ainepoint == 17):
            phone_stamp_rel("aine_dm", back_months=4, do_pause=False)
            send_phone_message("Aine", "[mc].", "aine_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message("Aine", "We need to talk.", "aine_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message(phone_config["phone_player_name"], "Yeah. I felt the storm coming.", "aine_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message("Aine", "You went ahead with the expansion plan without me.", "aine_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message("Aine", "AGAIN!", "aine_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message(phone_config["phone_player_name"], "It wasn't a power move. We needed to act, Aine.", "aine_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message("Aine", "Bullshit!", "aine_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message("Aine", "Fast is fine. But I'm NOT an afterthought, [mc]!", "aine_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message("Aine", "We're supposed to be leading this together!", "aine_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message(phone_config["phone_player_name"], "We've been stuck for weeks because we can't agree on anything!", "aine_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message(phone_config["phone_player_name"], "I made a call to keep things moving. That's it.", "aine_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message("Aine", "No. You made {b}your{/b} call and decided to skip the part where I exist!", "aine_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message("Aine", "You can't run a charity like that! And you sure as hell can't run {b}me{/b} like that!", "aine_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message(phone_config["phone_player_name"], "What the hell, Aine? I'm not \"running\" you!", "aine_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message(phone_config["phone_player_name"], "How the hell am I supposed to keep this thing alive if you shoot down everything I suggest?", "aine_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message("Aine", "I shoot them down because half of them are reckless! Why can't you see that?!", "aine_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message("Aine", "But sure, blame me for being the one thinking past tomorrow.", "aine_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message(phone_config["phone_player_name"], "Oh, right. Because you're the only one with a brain, is that it?", "aine_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message("Aine", "I didn't say that!", "aine_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message("Aine", "But if that's how you want to twist it—fine. I'm done trying.", "aine_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message(phone_config["phone_player_name"], "Wow. Just... wow.", "aine_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message(phone_config["phone_player_name"], "For someone who keeps saying we're partners, you talk like you don't trust me at all.", "aine_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message("Aine", "Because you're making it really hard to!", "aine_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message("Aine", "You keep making decisions behind my back and then... what? I'm supposed to nod and applaud?", "aine_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message(phone_config["phone_player_name"], "So what do you want from me, Aine?", "aine_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message(phone_config["phone_player_name"], "Tell me what I'm supposed to do so you'll finally stop acting like I'm shutting you out!", "aine_dm", do_pause=False, log_to_history=False, do_restart=False)

            phone_stamp_rel("aine_dm", back_months=4, do_pause=False)
            send_phone_message(phone_config["phone_player_name"], "Aine! Where are you?! Pick up your damn phone!", "aine_dm", do_pause=False, log_to_history=False, do_restart=False)

            phone_stamp_rel("aine_dm", back_months=4, do_pause=False)
            send_phone_message(phone_config["phone_player_name"], "AINE!", "aine_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message("Aine", "LEAVE ME ALONE!", "aine_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message(phone_config["phone_player_name"], "Where are you?!", "aine_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message("Aine", "I said...", "aine_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message("Aine", "LEAVE.", "aine_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message("Aine", "ME.", "aine_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message("Aine", "ALONE!", "aine_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message(phone_config["phone_player_name"], "No. I'm not backing off until you tell me where you are.", "aine_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message("Aine", "... You know where I am.", "aine_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message("Aine", "You just don't see me anymore.", "aine_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message("Aine", "Somewhere along the way, you forgot everything we had...", "aine_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message("Aine", "You stopped looking at me... and it hurts.", "aine_dm", do_pause=False, log_to_history=False, do_restart=False)

            phone_stamp_rel("aine_dm", back_months=4, do_pause=False)
            send_phone_message(phone_config["phone_player_name"], "There you are.", "aine_dm", do_pause=False, log_to_history=False, do_restart=False)

            phone_stamp_rel("aine_dm", back_months=4, do_pause=False)
            send_phone_message("Aine", "images/ch2ep1_1051.jpg", "aine_dm", 2, do_pause=False)
            send_phone_message("Aine", "I CAN'T with you!", "aine_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message("Aine", "I still hate you! 😡", "aine_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message(phone_config["phone_player_name"], "You didn't sound like that the other night.", "aine_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message("Aine", "😓😓😓", "aine_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message("Aine", "Stop bringing that up... I'm still sore all over.", "aine_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message(phone_config["phone_player_name"], "Surely you're not complaining about not being able to walk straight or sit like a normal person? Should I have been gentler? 🤨", "aine_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message("Aine", "Ugh, have I told you I hate you?", "aine_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message("Aine", "But... no, don't you dare. 😈", "aine_dm", do_pause=False, log_to_history=False, do_restart=False)

            phone_stamp_rel("aine_dm", back_months=4, do_pause=False)
            send_phone_message("Aine", "images/ch2ep1_1052.jpg", "aine_dm", 2, do_pause=False)
            send_phone_message(phone_config["phone_player_name"], "Roses? All I see is an axilla that smells sweeter than any flower.", "aine_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message(phone_config["phone_player_name"], "I could bury my nose there and lick you all day...", "aine_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message("Aine", "[mc]... what is wrong with you? I'm so offended.", "aine_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message("Aine", "All day? Why not all week? 😘", "aine_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message(phone_config["phone_player_name"], "😳", "aine_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message(phone_config["phone_player_name"], "Noted for next time...", "aine_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message("Aine", "...You really are impossible, you know that? 😌", "aine_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message("Aine", "God, they smell sooooo good, [mc].", "aine_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message("Aine", "Thank you. 🥰", "aine_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message(phone_config["phone_player_name"], "This means we're good, right?", "aine_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message("Aine", "It means I'm willing to talk without screaming.", "aine_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message("Aine", "I love you. 😘", "aine_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message(phone_config["phone_player_name"], "I love you too, Aine.", "aine_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message(phone_config["phone_player_name"], "Now go get some sleep.", "aine_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message("Aine", "YOU get some sleep. 😁", "aine_dm", do_pause=False, log_to_history=False, do_restart=False)

        ## 3 months ago ##
        phone_stamp_rel("aine_dm", back_months=3, do_pause=False)
        send_phone_message("Aine", "[mc]?", "aine_dm", do_pause=False, log_to_history=False, do_restart=False)
        send_phone_message("Aine", "Just left the office. The volunteers wouldn't let me go unless I promised I'd eat something.", "aine_dm", do_pause=False, log_to_history=False, do_restart=False)
        send_phone_message(phone_config["phone_player_name"], "Did you?", "aine_dm", do_pause=False, log_to_history=False, do_restart=False)
        send_phone_message("Aine", "Half a sandwich. I don't really feel like eating.", "aine_dm", do_pause=False, log_to_history=False, do_restart=False)
        send_phone_message(phone_config["phone_player_name"], "Aine...", "aine_dm", do_pause=False, log_to_history=False, do_restart=False)
        send_phone_message("Aine", "Anyway... are you set for later?", "aine_dm", do_pause=False, log_to_history=False, do_restart=False)
        send_phone_message("Aine", "The food drive, I mean.", "aine_dm", do_pause=False, log_to_history=False, do_restart=False)
        send_phone_message(phone_config["phone_player_name"], "Almost. Still waiting on the delivery from the shelter.", "aine_dm", do_pause=False, log_to_history=False, do_restart=False)
        send_phone_message("Aine", "God... I just want today to go right. Please let it go right.", "aine_dm", do_pause=False, log_to_history=False, do_restart=False)
        send_phone_message("Aine", "Feels like we need a win after last month's disasters.", "aine_dm", do_pause=False, log_to_history=False, do_restart=False)
        if aineroute:
            send_phone_message(phone_config["phone_player_name"], "Oh, trust me, we will. If there's anything I know about you, it's that your hard work always pays off.", "aine_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message(phone_config["phone_player_name"], "We're still learning, but this time? I'm sure it's a success.", "aine_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message("Aine", "Pep-talking me?", "aine_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message(phone_config["phone_player_name"], "1% pep talk, 99% truth.", "aine_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message(phone_config["phone_player_name"], "Want me to pick you up? The delivery just arrived.", "aine_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message("Aine", "Oh, good idea!", "aine_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message("Aine", "images/ch2ep1_1056.jpg", "aine_dm", 2, do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message(phone_config["phone_player_name"], "Well, well, well... someone went commando today?", "aine_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message(phone_config["phone_player_name"], "Cumming!", "aine_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message(phone_config["phone_player_name"], "*Coming.", "aine_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message("Aine", "Pfft! Food drive first! 🤪", "aine_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message(phone_config["phone_player_name"], "Yes, ma'am!", "aine_dm", do_pause=False, log_to_history=False, do_restart=False)

        ## 2 months ago ##
        phone_stamp_rel("aine_dm", back_months=3, do_pause=False)
        send_phone_message(phone_config["phone_player_name"], "Can I ask you something personal?", "aine_dm", do_pause=False, log_to_history=False, do_restart=False)
        send_phone_message("Aine", "It's not like you to ask permission from me... What's this about?", "aine_dm", do_pause=False, log_to_history=False, do_restart=False)
        send_phone_message(phone_config["phone_player_name"], "It's about Hera.", "aine_dm", do_pause=False, log_to_history=False, do_restart=False)
        send_phone_message("Aine", "...", "aine_dm", do_pause=False, log_to_history=False, do_restart=False)
        send_phone_message("Aine", "Alright. What about her?", "aine_dm", do_pause=False, log_to_history=False, do_restart=False)
        send_phone_message(phone_config["phone_player_name"], "Do you ever plan on looking for her?", "aine_dm", do_pause=False, log_to_history=False, do_restart=False)
        send_phone_message(phone_config["phone_player_name"], "We've turned the whole organization around. She'd want to know that, right?", "aine_dm", do_pause=False, log_to_history=False, do_restart=False)
        send_phone_message("Aine", "I've thought about it.", "aine_dm", do_pause=False, log_to_history=False, do_restart=False)
        send_phone_message(phone_config["phone_player_name"], "Then why haven't you?", "aine_dm", do_pause=False, log_to_history=False, do_restart=False)
        send_phone_message("Aine", "Because I don't know if she wants to be found.", "aine_dm", do_pause=False, log_to_history=False, do_restart=False)
        send_phone_message("Aine", "She left before everything with you happened.", "aine_dm", do_pause=False, log_to_history=False, do_restart=False)
        send_phone_message("Aine", "And she didn't leave a trace. Not a single one.", "aine_dm", do_pause=False, log_to_history=False, do_restart=False)
        send_phone_message(phone_config["phone_player_name"], "It's been months.", "aine_dm", do_pause=False, log_to_history=False, do_restart=False)
        send_phone_message("Aine", "Exactly.", "aine_dm", do_pause=False, log_to_history=False, do_restart=False)
        send_phone_message("Aine", "If she wanted to come back, she would've by now.", "aine_dm", do_pause=False, log_to_history=False, do_restart=False)
        send_phone_message(phone_config["phone_player_name"], "You don't sound angry. Kinda surprised.", "aine_dm", do_pause=False, log_to_history=False, do_restart=False)
        send_phone_message("Aine", "I'm not.", "aine_dm", do_pause=False, log_to_history=False, do_restart=False)
        send_phone_message("Aine", "I'm just tired of expecting things from her.", "aine_dm", do_pause=False, log_to_history=False, do_restart=False)
        send_phone_message(phone_config["phone_player_name"], "Aine.", "aine_dm", do_pause=False, log_to_history=False, do_restart=False)
        send_phone_message("Aine", "Anyway.", "aine_dm", do_pause=False, log_to_history=False, do_restart=False)
        send_phone_message("Aine", "We've done a lot without her.", "aine_dm", do_pause=False, log_to_history=False, do_restart=False)
        send_phone_message("Aine", "We cleared the assets. Cut off the old connections. Rebuilt the structure from the ground up.", "aine_dm", do_pause=False, log_to_history=False, do_restart=False)
        send_phone_message("Aine", "We've opened three community programs already—kids, food distribution, and legal assistance.", "aine_dm", do_pause=False, log_to_history=False, do_restart=False)
        send_phone_message("Aine", "And every time something works, I think, \"She would've liked this.\"", "aine_dm", do_pause=False, log_to_history=False, do_restart=False)
        send_phone_message("Aine", "Deep inside, I want her to be proud of me.", "aine_dm", do_pause=False, log_to_history=False, do_restart=False)
        send_phone_message("Aine", "But I'm stuck between wanting that and actually chasing her down.", "aine_dm", do_pause=False, log_to_history=False, do_restart=False)
        send_phone_message("Aine", "What if I find her and she doesn't want any of this?", "aine_dm", do_pause=False, log_to_history=False, do_restart=False)
        send_phone_message("Aine", "What if she feels free... and I ruin it?", "aine_dm", do_pause=False, log_to_history=False, do_restart=False)
        send_phone_message(phone_config["phone_player_name"], "Let me tell you something...", "aine_dm", do_pause=False, log_to_history=False, do_restart=False)
        send_phone_message(phone_config["phone_player_name"], "What if she misses you just as much?", "aine_dm", do_pause=False, log_to_history=False, do_restart=False)
        send_phone_message("Aine", "... She never misses me. And probably never will.", "aine_dm", do_pause=False, log_to_history=False, do_restart=False)
        send_phone_message("Aine", "That's a hard truth she hammered into me growing up.", "aine_dm", do_pause=False, log_to_history=False, do_restart=False)
        send_phone_message("Aine", "But... thank you for asking.", "aine_dm", do_pause=False, log_to_history=False, do_restart=False)
        send_phone_message(phone_config["phone_player_name"], "For what it's worth... I think she'd be proud of you too.", "aine_dm", do_pause=False, log_to_history=False, do_restart=False)
        send_phone_message("Aine", "I'll pretend I didn't read that.", "aine_dm", do_pause=False, log_to_history=False, do_restart=False)
        send_phone_message("Aine", "Good night, [mc].", "aine_dm", do_pause=False, log_to_history=False, do_restart=False)
        if aineroute:
            send_phone_message(phone_config["phone_player_name"], "Where are you?", "aine_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message("Aine", "In my room. Why?", "aine_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message(phone_config["phone_player_name"], "I'm coming over.", "aine_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message("Aine", "For what?", "aine_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message(phone_config["phone_player_name"], "To make sure you're not crying alone.", "aine_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message("Aine", "😢", "aine_dm", do_pause=False, log_to_history=False, do_restart=False)

        ## 1 months ago ##
        phone_stamp_rel("aine_dm", back_months=1, do_pause=False)
        send_phone_message("Aine", "[mc], I updated the soft copies. Check the last page before you head out.", "aine_dm", do_pause=False, log_to_history=False, do_restart=False)
        if aineroute:
            send_phone_message(phone_config["phone_player_name"], "On it.", "aine_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message(phone_config["phone_player_name"], "Also... did you eat anything yet? You sounded awful this morning.", "aine_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message(phone_config["phone_player_name"], "Your fever won't drop if you keep skipping meals.", "aine_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message("Aine", "Stop, stop, stop.", "aine_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message("Aine", "I'm not dying, okay?", "aine_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message("Aine", "I'll eat. I'll rest. Just don't give me another dissertation on nutrition.", "aine_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message(phone_config["phone_player_name"], "I did {b}not{/b} write a dissertation... 😒", "aine_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message("Aine", "You were halfway through Chapter 2, I just can't prove it... 🙄", "aine_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message("Aine", "Anyway... you take care. 😘", "aine_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message(phone_config["phone_player_name"], "YOU take care. 😡", "aine_dm", do_pause=False, log_to_history=False, do_restart=False)
        else:
            send_phone_message(phone_config["phone_player_name"], "On it.", "aine_dm", do_pause=False, log_to_history=False, do_restart=False)

        ## Present ##
        phone_stamp_rel("aine_dm", back_minutes=34, do_pause=False)
        send_phone_message(phone_config["phone_player_name"], "Are you guys still at home? Any update on her?", "aine_dm", do_pause=False, log_to_history=False, do_restart=False)






        ##### KLARA #####
        ## 13 months ago ##
        ## 12 months ago ##
        phone_stamp_rel("klara_dm", back_months=12, do_pause=False)
        send_phone_message("Klara", "when you pass by the store later,", "klara_dm", do_pause=False, log_to_history=False, do_restart=False)
        send_phone_message("Klara", "buy a box of hair dye.", "klara_dm", do_pause=False, log_to_history=False, do_restart=False)
        send_phone_message("Klara", "the dark one.", "klara_dm", do_pause=False, log_to_history=False, do_restart=False)
        send_phone_message("Klara", "you know which.", "klara_dm", do_pause=False, log_to_history=False, do_restart=False)
        send_phone_message("Klara", "i want things back to how they should be.", "klara_dm", do_pause=False, log_to_history=False, do_restart=False)
        send_phone_message(phone_config["phone_player_name"], "Sure.{#1}", "klara_dm", do_pause=False, log_to_history=False, do_restart=False)

        ## 11 months ago ##
        ## 10 months ago ##
        ## 9 months ago ##
        ## 8 months ago ##
        ## 7 months ago ##
        ## 6 months ago ##
        ## 5 months ago ##
        ## 4 months ago ##
        ## 3 months ago ##
        ## 2 months ago ##
        ## 1 months ago ##



        ##### LILY #####
        ## 13 months ago ##
        ## 12 months ago ##
        ## 11 months ago ##
        phone_stamp_rel("lily_dm", back_months=11, do_pause=False)
        send_phone_message("Lily", "hey, [mc]! 🌼", "lily_dm", do_pause=False, log_to_history=False, do_restart=False)
        send_phone_message("Lily", "i know it's been a while. i hope that's okay.", "lily_dm", do_pause=False, log_to_history=False, do_restart=False)
        send_phone_message("Lily", "i just wanted to say hi while i still have the luxury.", "lily_dm", do_pause=False, log_to_history=False, do_restart=False)
        send_phone_message("Lily", "i remembered today's your birthday.", "lily_dm", do_pause=False, log_to_history=False, do_restart=False)
        send_phone_message("Lily", "happy birthday, [mc]!", "lily_dm", do_pause=False, log_to_history=False, do_restart=False)
        send_phone_message("Lily", "i hope you're doing okay.", "lily_dm", do_pause=False, log_to_history=False, do_restart=False)
        send_phone_message("Lily", "and that you and freya are taking care of each other. 🤍", "lily_dm", do_pause=False, log_to_history=False, do_restart=False)

        phone_stamp_rel("lily_dm", back_months=11, do_pause=False)
        send_phone_message(phone_config["phone_player_name"], "Forget my birthday! Holy hell, Lily!", "lily_dm", do_pause=False, log_to_history=False, do_restart=False)
        send_phone_message(phone_config["phone_player_name"], "Jesus. How long has it been?", "lily_dm", do_pause=False, log_to_history=False, do_restart=False)
        send_phone_message(phone_config["phone_player_name"], "How are you?", "lily_dm", do_pause=False, log_to_history=False, do_restart=False)
        send_phone_message("Lily", "actually, pretty great!", "lily_dm", do_pause=False, log_to_history=False, do_restart=False)
        send_phone_message("Lily", "i mean, kinda?", "lily_dm", do_pause=False, log_to_history=False, do_restart=False)
        send_phone_message("Lily", "today's my first day at a new job.", "lily_dm", do_pause=False, log_to_history=False, do_restart=False)
        send_phone_message("Lily", "i'm pretty nervous.", "lily_dm", do_pause=False, log_to_history=False, do_restart=False)
        send_phone_message("Lily", "but i think i'll manage.", "lily_dm", do_pause=False, log_to_history=False, do_restart=False)
        send_phone_message("Lily", "look!", "lily_dm", do_pause=False, log_to_history=False, do_restart=False)
        send_phone_message("Lily", "images/ch2ep1_1066.jpg", "lily_dm", 2, do_pause=False, log_to_history=False, do_restart=False)
        send_phone_message(phone_config["phone_player_name"], "Wait... seriously?", "lily_dm", do_pause=False, log_to_history=False, do_restart=False)
        send_phone_message("Lily", "seriously.", "lily_dm", do_pause=False, log_to_history=False, do_restart=False)
        send_phone_message("Lily", "i'm training high school students.", "lily_dm", do_pause=False, log_to_history=False, do_restart=False)
        send_phone_message(phone_config["phone_player_name"], "Damn... that's nostalgic.", "lily_dm", do_pause=False, log_to_history=False, do_restart=False)
        send_phone_message("Lily", "yeah. i didn't expect this, honestly.", "lily_dm", do_pause=False, log_to_history=False, do_restart=False)
        send_phone_message("Lily", "it's way bigger than what i thought i'd ever get.", "lily_dm", do_pause=False, log_to_history=False, do_restart=False)
        send_phone_message("Lily", "i figured i'd end up as a water girl or something.", "lily_dm", do_pause=False, log_to_history=False, do_restart=False)
        send_phone_message("Lily", "guess all that experience paid off. 😁", "lily_dm", do_pause=False, log_to_history=False, do_restart=False)
        send_phone_message(phone_config["phone_player_name"], "But do you love it?", "lily_dm", do_pause=False, log_to_history=False, do_restart=False)
        send_phone_message("Lily", "i do!", "lily_dm", do_pause=False, log_to_history=False, do_restart=False)
        send_phone_message("Lily", "it's close enough to my dream that i'm happy.", "lily_dm", do_pause=False, log_to_history=False, do_restart=False)
        send_phone_message(phone_config["phone_player_name"], "Then that's what counts.", "lily_dm", do_pause=False, log_to_history=False, do_restart=False)
        send_phone_message("Lily", "what about you?", "lily_dm", do_pause=False, log_to_history=False, do_restart=False)
        send_phone_message("Lily", "still at the burger shack?", "lily_dm", do_pause=False, log_to_history=False, do_restart=False)
        send_phone_message(phone_config["phone_player_name"], "Ouch.", "lily_dm", do_pause=False, log_to_history=False, do_restart=False)
        send_phone_message("Lily", "oh! no, i didn't mean it like that.", "lily_dm", do_pause=False, log_to_history=False, do_restart=False)
        send_phone_message(phone_config["phone_player_name"], "Relax. I know.", "lily_dm", do_pause=False, log_to_history=False, do_restart=False)
        send_phone_message(phone_config["phone_player_name"], "Yeah, I'm still there.", "lily_dm", do_pause=False, log_to_history=False, do_restart=False)
        send_phone_message(phone_config["phone_player_name"], "But I'm working on something new, too.", "lily_dm", do_pause=False, log_to_history=False, do_restart=False)
        send_phone_message(phone_config["phone_player_name"], "Not a dream job... but it's something.", "lily_dm", do_pause=False, log_to_history=False, do_restart=False)
        send_phone_message("Lily", "then what's your dream job?", "lily_dm", do_pause=False, log_to_history=False, do_restart=False)
        send_phone_message(phone_config["phone_player_name"], "Honestly?", "lily_dm", do_pause=False, log_to_history=False, do_restart=False)
        send_phone_message(phone_config["phone_player_name"], "I don't really know anymore.", "lily_dm", do_pause=False, log_to_history=False, do_restart=False)
        send_phone_message("Lily", "huh? why?", "lily_dm", do_pause=False, log_to_history=False, do_restart=False)
        send_phone_message(phone_config["phone_player_name"], "Things have been off since you left.", "lily_dm", do_pause=False, log_to_history=False, do_restart=False)
        send_phone_message(phone_config["phone_player_name"], "I wish I could explain everything.", "lily_dm", do_pause=False, log_to_history=False, do_restart=False)
        send_phone_message(phone_config["phone_player_name"], "But I can't.", "lily_dm", do_pause=False, log_to_history=False, do_restart=False)
        send_phone_message("Lily", "that's okay.", "lily_dm", do_pause=False, log_to_history=False, do_restart=False)
        send_phone_message("Lily", "maybe one day. 😁", "lily_dm", do_pause=False, log_to_history=False, do_restart=False)
        send_phone_message(phone_config["phone_player_name"], "Yeah. One day.", "lily_dm", do_pause=False, log_to_history=False, do_restart=False)
        send_phone_message("Lily", "images/ch2ep1_1067.jpg", "lily_dm", 2, do_pause=False, log_to_history=False, do_restart=False)
        send_phone_message("Lily", "the students are here.", "lily_dm", do_pause=False, log_to_history=False, do_restart=False)
        send_phone_message("Lily", "i'll text you some other time, [mc].", "lily_dm", do_pause=False, log_to_history=False, do_restart=False)
        send_phone_message("Lily", "tell freya to take care of herself for me, please?", "lily_dm", do_pause=False, log_to_history=False, do_restart=False)
        send_phone_message("Lily", "she was kinda mad i can't facetime much anymore.", "lily_dm", do_pause=False, log_to_history=False, do_restart=False)
        send_phone_message(phone_config["phone_player_name"], "I will. And good luck out there.", "lily_dm", do_pause=False, log_to_history=False, do_restart=False)
        send_phone_message("Lily", "you too, [mc].", "lily_dm", do_pause=False, log_to_history=False, do_restart=False)

        ## 10 months ago ##
        ## 9 months ago ##
        ## 8 months ago ##
        ## 7 months ago ##
        ## 6 months ago ##
        ## 5 months ago ##
        ## 4 months ago ##
        ## 3 months ago ##
        ## 2 months ago ##
        ## 1 months ago ##







        ##### NAOMI #####
        ## 13 months ago ##
        if naomiroute:
            phone_stamp_rel("naomi_dm", back_months=13, do_pause=False)
            send_phone_message("Naomi", "So, how you holding up?", "naomi_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message(phone_config["phone_player_name"], "Better by the day. Finally walking without feeling like every step's a chastisement.", "naomi_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message(phone_config["phone_player_name"], "Thanks again for visiting, even though I was technically a corpse with a pulse.", "naomi_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message("Naomi", "All good. You'd do the same for me.", "naomi_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message("Naomi", "So, when're you coming over so I can make good on my promise?", "naomi_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message(phone_config["phone_player_name"], "The what now? What could you possibly owe me?", "naomi_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message("Naomi", "Cracking open a cold one to celebrate you no longer being a log stuck in a hospital bed. Or regular bed, for that matter.", "naomi_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message(phone_config["phone_player_name"], "Right, that. How's tomorrow night?", "naomi_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message("Naomi", "Sweet. Got a beer preference?", "naomi_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message(phone_config["phone_player_name"], "Something proudly \"Advance Cesa Fair\". Maybe Foster's.", "naomi_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message("Naomi", "Yeah nah.", "naomi_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message("Naomi", "Bye.", "naomi_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message(phone_config["phone_player_name"], "What? What did I say?", "naomi_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message("Naomi", "Mate, if you reckon Foster's is Cesa beer, you might as well drink straight from the dunny.", "naomi_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message("Naomi", "Clearly your brain's still booting up, but no stress, Naomi's got you covered.", "naomi_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message("Naomi", "You want something crisp, bright, proper flavour? Stuff that actually tastes like beer, not regret?", "naomi_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message(phone_config["phone_player_name"], "I thought your dad was Mr. Scott, not Mr. Mays.", "naomi_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message("Naomi", "Fair call. You'll see when you get here.", "naomi_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message(phone_config["phone_player_name"], "Can't wait. See you tomorrow, Naomi.", "naomi_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message("Naomi", "Catch you then.", "naomi_dm", do_pause=False, log_to_history=False, do_restart=False)

        if naomiroute:
            phone_stamp_rel("naomi_dm", back_months=13, do_pause=False)
            send_phone_message(phone_config["phone_player_name"], "Here's Johnny...", "naomi_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message("Naomi", "Huh? What are you on about?", "naomi_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message(phone_config["phone_player_name"], "Movie reference. Anyway, I'm in your driveway.", "naomi_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message(phone_config["phone_player_name"], "Where are you?", "naomi_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message("Naomi", "Out back. Working on another beauty.", "naomi_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message(phone_config["phone_player_name"], "Moved your makeup to your shed? 😉", "naomi_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message("Naomi", "Ease up, Casanova. Keep it up and I might actually let you take her for a spin.", "naomi_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message(phone_config["phone_player_name"], "Which one?", "naomi_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message("Naomi", "Where's the fun in telling you? 😜", "naomi_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message("Naomi", "Quit stuffing around and get in here. Beer's not staying cold for you.", "naomi_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message(phone_config["phone_player_name"], "Heading over now.", "naomi_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message(phone_config["phone_player_name"], "Actually, where's your shed again?", "naomi_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message("Naomi", "LMAO.", "naomi_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message("Naomi", "You're something else. Now seriously, get in here or I'm nicking your beer", "naomi_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message(phone_config["phone_player_name"], "Ha... right...", "naomi_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message("Naomi", "... You're actually serious.", "naomi_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message(phone_config["phone_player_name"], "Afraid so. 😬", "naomi_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message("Naomi", "Bloody hell. Backyard, left side. Follow the dirt track and you can't miss it.", "naomi_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message("Naomi", "Wait, what driveway are you even parked on?", "naomi_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message(phone_config["phone_player_name"], "The back one.", "naomi_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message("Naomi", "You muppet. Should've used the front like you used to.", "naomi_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message(phone_config["phone_player_name"], "Noted for next time. Be there soon.", "naomi_dm", do_pause=False, log_to_history=False, do_restart=False)

        if naomiroute:
            phone_stamp_rel("naomi_dm", back_months=13, do_pause=False)
            send_phone_message(phone_config["phone_player_name"], "G'day, you beauty.", "naomi_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message("Naomi", "☺️", "naomi_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message("Naomi", "Good timing, was just about to message you.", "naomi_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message(phone_config["phone_player_name"], "Oh yeah?", "naomi_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message("Naomi", "Was thinking of getting back into my restoration project next week. Been putting it off long enough.", "naomi_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message(phone_config["phone_player_name"], "Your SRT Demon?", "naomi_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message("Naomi", "Yep. Poor girl's been sitting there collecting dust like some forgotten museum piece.", "naomi_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message("Naomi", "Truth is... I wanted to finish it with you. Then you went completely off the grid and, well, kinda killed the rhythm.", "naomi_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message("Naomi", "Figured I'd wait till you were back on your feet before I laid a finger on her again.", "naomi_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message(phone_config["phone_player_name"], "You just want to see me more often, don't you?", "naomi_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message("Naomi", "Was gonna say that next, smartass. 😉", "naomi_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message("Naomi", "But hey, I know you've got your day job, so just swing by whenever you're free. No pressure.", "naomi_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message(phone_config["phone_player_name"], "Next week, right? How about Monday after my shift?", "naomi_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message("Naomi", "Works for me!", "naomi_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message("Naomi", "Just rock up. No need to call or text. Gate's always open for you.", "naomi_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message(phone_config["phone_player_name"], "Gotcha.", "naomi_dm", do_pause=False, log_to_history=False, do_restart=False)

        ## 12 months ago ##
        if naomiroute:
            phone_stamp_rel("naomi_dm", back_months=11, do_pause=False)
            send_phone_message("Naomi", "Today was fun, [mc]. Unplanned, but fun. 😂", "naomi_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message(phone_config["phone_player_name"], "I promise I'll wash the dishes.", "naomi_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message(phone_config["phone_player_name"], "Vacuum the house.", "naomi_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message(phone_config["phone_player_name"], "Clean the bathroom.", "naomi_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message(phone_config["phone_player_name"], "Pick up the garbage.", "naomi_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message(phone_config["phone_player_name"], "Make the sandwich.", "naomi_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message(phone_config["phone_player_name"], "Do the laundry.", "naomi_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message(phone_config["phone_player_name"], "Cook the dinner.", "naomi_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message(phone_config["phone_player_name"], "Walk the dogs.", "naomi_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message(phone_config["phone_player_name"], "Cut the grass.", "naomi_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message(phone_config["phone_player_name"], "Pay the bills", "naomi_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message(phone_config["phone_player_name"], "Wash the car", "naomi_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message("Naomi", "LOL! 🤣", "naomi_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message("Naomi", "That wasn't meant to be a threat!", "naomi_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message(phone_config["phone_player_name"], "I'm pregnant! 🥵", "naomi_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message("Naomi", "Alright, nope. Stop it. 😅", "naomi_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message("Naomi", "Tomorrow. Same time?", "naomi_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message(phone_config["phone_player_name"], "Wouldn't miss it.", "naomi_dm", do_pause=False, log_to_history=False, do_restart=False)

        ## 11 months ago ##
        if naomiroute:
            phone_stamp_rel("naomi_dm", back_months=11, do_pause=False)
            send_phone_message(phone_config["phone_player_name"], "Naomi. What on earth happened last night?", "naomi_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message("", "Message Undeliverable", "naomi_dm", 1, do_pause=False, log_to_history=False, do_restart=False)

        ## 10 months ago ##
        ## 9 months ago ##
        ## 8 months ago ##
        ## 7 months ago ##
        ## 6 months ago ##
        ## 5 months ago ##
        ## 4 months ago ##
        ## 3 months ago ##
        ## 2 months ago ##
        ## 1 months ago ##


        




        ##### SKY #####
        ## 13 months ago ##
        if skyroute:
            phone_stamp_rel("sky_dm", back_months=13, do_pause=False)
            send_phone_message(phone_config["phone_player_name"], "Sky.", "sky_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message(phone_config["phone_player_name"], "About our practice.", "sky_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message("Sky", "told u already. call.", "sky_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message("Sky", "hate txt. 😑", "sky_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message(phone_config["phone_player_name"], "I know. I'm in the middle of a meeting right now.", "sky_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message(phone_config["phone_player_name"], "Just wanted to give you a heads-up about later.", "sky_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message("Sky", "call after.", "sky_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message(phone_config["phone_player_name"], "... Alright.", "sky_dm", do_pause=False, log_to_history=False, do_restart=False)
        ## 12 months ago ##
        ## 11 months ago ##
        ## 10 months ago ##
        ## 9 months ago ##
        ## 8 months ago ##
        ## 7 months ago ##
        ## 6 months ago ##
        ## 5 months ago ##
        ## 4 months ago ##
        ## 3 months ago ##
        ## 2 months ago ##
        ## 1 months ago ##






        ##### JUNE #####
        ## 13 months ago ##
        phone_stamp_rel("june_dm", back_months=13, do_pause=False)
        send_phone_message(phone_config["phone_player_name"], "Come outside.", "june_dm", do_pause=False, log_to_history=False, do_restart=False)
        send_phone_message("June", "what? i'm not even home", "june_dm", do_pause=False, log_to_history=False, do_restart=False)
        send_phone_message(phone_config["phone_player_name"], "You are.", "june_dm", do_pause=False, log_to_history=False, do_restart=False)
        send_phone_message(phone_config["phone_player_name"], "I can see that busted-ass toupee from the window.", "june_dm", do_pause=False, log_to_history=False, do_restart=False)
        send_phone_message("June", "bro", "june_dm", do_pause=False, log_to_history=False, do_restart=False)
        send_phone_message("June", "you could've just called me", "june_dm", do_pause=False, log_to_history=False, do_restart=False)
        send_phone_message("June", "or knocked", "june_dm", do_pause=False, log_to_history=False, do_restart=False)
        send_phone_message("June", "there's literally a door", "june_dm", do_pause=False, log_to_history=False, do_restart=False)
        send_phone_message("June", "you blind fuck", "june_dm", do_pause=False, log_to_history=False, do_restart=False)
        send_phone_message(phone_config["phone_player_name"], "If you don't wanna see me just say so. I'll dip.", "june_dm", do_pause=False, log_to_history=False, do_restart=False)
        send_phone_message("June", "oh get the hell outta here", "june_dm", do_pause=False, log_to_history=False, do_restart=False)
        send_phone_message("June", "you really pulled the guilt card on me?", "june_dm", do_pause=False, log_to_history=False, do_restart=False)

        phone_stamp_rel("june_dm", back_months=13, do_pause=False)
        send_phone_message(phone_config["phone_player_name"], "See?", "june_dm", do_pause=False, log_to_history=False, do_restart=False)
        send_phone_message(phone_config["phone_player_name"], "Wasn't that hard.", "june_dm", do_pause=False, log_to_history=False, do_restart=False)
        send_phone_message("June", "yeah yeah yeah", "june_dm", do_pause=False, log_to_history=False, do_restart=False)
        send_phone_message("June", "you looked like shit warmed up", "june_dm", do_pause=False, log_to_history=False, do_restart=False)
        send_phone_message("June", "but good to see you too", "june_dm", do_pause=False, log_to_history=False, do_restart=False)
        send_phone_message(phone_config["phone_player_name"], "🤛😁", "june_dm", do_pause=False, log_to_history=False, do_restart=False)
        send_phone_message("June", "🤪🤜", "june_dm", do_pause=False, log_to_history=False, do_restart=False)

        ## 12 months ago ##
        ## 11 months ago ##
        ## 10 months ago ##
        ## 9 months ago ##
        phone_stamp_rel("june_dm", back_months=9, do_pause=False)
        send_phone_message(phone_config["phone_player_name"], "Hello, valued customer. We've been trying to reach you about your car's extended warranty. This is your {b}final{/b} notice.", "june_dm", do_pause=False, log_to_history=False, do_restart=False)
        send_phone_message("June", "...", "june_dm", do_pause=False, log_to_history=False, do_restart=False)
        send_phone_message("June", "if shu's there, go fuck yourselves", "june_dm", do_pause=False, log_to_history=False, do_restart=False)

        ## 8 months ago ##
        ## 7 months ago ##
        phone_stamp_rel("june_dm", back_months=7, do_pause=False)
        send_phone_message("June", "what the hell was that?", "june_dm", do_pause=False, log_to_history=False, do_restart=False)
        send_phone_message("June", "i work with DFCS", "june_dm", do_pause=False, log_to_history=False, do_restart=False)
        send_phone_message("June", "not an engineer, you walking protein shake.", "june_dm", do_pause=False, log_to_history=False, do_restart=False)
        send_phone_message(phone_config["phone_player_name"], "You can work DFCS {b}and{/b} be an engineer, bite-size.", "june_dm", do_pause=False, log_to_history=False, do_restart=False)
        send_phone_message("June", "ugh", "june_dm", do_pause=False, log_to_history=False, do_restart=False)
        send_phone_message("June", "whatever", "june_dm", do_pause=False, log_to_history=False, do_restart=False)
        send_phone_message("June", "i really don't wanna have another dumb, circular fight with you two", "june_dm", do_pause=False, log_to_history=False, do_restart=False)
        send_phone_message(phone_config["phone_player_name"], "🤣", "june_dm", do_pause=False, log_to_history=False, do_restart=False)
        send_phone_message(phone_config["phone_player_name"], "You say that like you don't sprint straight into it every time.", "june_dm", do_pause=False, log_to_history=False, do_restart=False)
        send_phone_message("June", "🙄", "june_dm", do_pause=False, log_to_history=False, do_restart=False)

        ## 6 months ago ##
        ## 5 months ago ##
        ## 4 months ago ##
        ## 3 months ago ##
        ## 2 months ago ##
        ## 1 months ago ##





        ##### SHU #####
        ## 13 months ago ##
        ## 12 months ago ##
        ## 11 months ago ##
        ## 10 months ago ##
        ## 9 months ago ##
        ## 8 months ago ##
        ## 7 months ago ##
        ## 6 months ago ##
        ## 5 months ago ##
        ## 4 months ago ##
        phone_stamp_rel("shu_dm", back_months=4, do_pause=False)
        send_phone_message("Shu", "images/ch2ep1_1065.jpg", "shu_dm", 2, do_pause=False, log_to_history=False, do_restart=False)
        send_phone_message("Shu", "ah fck! THAT was from my private stash.", "shu_dm", do_pause=False, log_to_history=False, do_restart=False)
        send_phone_message("Shu", "how do u unsend", "shu_dm", do_pause=False, log_to_history=False, do_restart=False)
        send_phone_message("Shu", "UNSEND!!!", "shu_dm", do_pause=False, log_to_history=False, do_restart=False)
        send_phone_message(phone_config["phone_player_name"], "Why the hell do you have pics of your naked femboy ass on your phone?", "shu_dm", do_pause=False, log_to_history=False, do_restart=False)
        send_phone_message("Shu", "bcuz i'm sexy af and the ladies deserve a sneak peek at the Shuper goods.", "shu_dm", do_pause=False, log_to_history=False, do_restart=False)
        send_phone_message(phone_config["phone_player_name"], "... You did not just say that.", "shu_dm", do_pause=False, log_to_history=False, do_restart=False)
        send_phone_message("Shu", "no, dumbass.", "shu_dm", do_pause=False, log_to_history=False, do_restart=False)
        send_phone_message("Shu", "i {b}texted{/b} it. duh.", "shu_dm", do_pause=False, log_to_history=False, do_restart=False)
        send_phone_message(phone_config["phone_player_name"], "images/memes/right.png", "shu_dm", 2, do_pause=False, log_to_history=False, do_restart=False)
        send_phone_message("Shu", "😂🫵", "shu_dm", do_pause=False, log_to_history=False, do_restart=False)

        ## 3 months ago ##
        ## 2 months ago ##
        ## 1 months ago ##





        ##### GWEN #####
        ## 13 months ago ##
        phone_stamp_rel("gwen_dm", back_months=13, do_pause=False)
        send_phone_message("Gwen", "Heard you're back at work already.", "gwen_dm", do_pause=False, log_to_history=False, do_restart=False)
        send_phone_message("Gwen", "You do realize you were kidnapped, right?", "gwen_dm", do_pause=False, log_to_history=False, do_restart=False)
        send_phone_message(phone_config["phone_player_name"], "You and Aine...", "gwen_dm", do_pause=False, log_to_history=False, do_restart=False)
        send_phone_message(phone_config["phone_player_name"], "I'm fine, Gwen. Can't stay on bedrest forever.", "gwen_dm", do_pause=False, log_to_history=False, do_restart=False)
        send_phone_message("Gwen", "Yeah? Looks more like you're trying to speedrun a relapse.", "gwen_dm", do_pause=False, log_to_history=False, do_restart=False)
        send_phone_message("Gwen", "You don't have to prove you're unbreakable. Nobody's giving out medals for it.", "gwen_dm", do_pause=False, log_to_history=False, do_restart=False)
        send_phone_message(phone_config["phone_player_name"], "I'm not proving anything. Just doing my job.", "gwen_dm", do_pause=False, log_to_history=False, do_restart=False)
        if gwenroute:
            send_phone_message("Gwen", "Uh-huh. Sure. Anyway...", "gwen_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message("Gwen", "Have you had lunch?", "gwen_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message(phone_config["phone_player_name"], "Define lunch.", "gwen_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message("Gwen", "No.{#3}", "gwen_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message("Gwen", "I'm not playing that game with you.", "gwen_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message("Gwen", "Stay where you are. I'm coming to get you.", "gwen_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message(phone_config["phone_player_name"], "Gwen...", "gwen_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message("Gwen", "[mc]. You nearly died.", "gwen_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message("Gwen", "You're eating a real meal today not whatever \"technically counts\" as lunch in that disaster of a food pyramid you call a cup of coffee.", "gwen_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message("Gwen", "Be outside in fifteen.", "gwen_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message(phone_config["phone_player_name"], "... Yes, ma'am.", "gwen_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message("Gwen", "Freya's with you, right? Bring her. We'll feed both of you.", "gwen_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message(phone_config["phone_player_name"], "Then you better take us to a Korean resto. She's been craving kimchi stew like a pregnant woman.", "gwen_dm", do_pause=False, log_to_history=False, do_restart=False)
            if allornothingroute:
                send_phone_message("Gwen", "You sure you haven't accidentally started a family with her yet? 😏", "gwen_dm", do_pause=False, log_to_history=False, do_restart=False)
                send_phone_message(phone_config["phone_player_name"], "WHAT? NO?!", "gwen_dm", do_pause=False, log_to_history=False, do_restart=False)

        ## 12 months ago ##
        if gwenroute:
            phone_stamp_rel("gwen_dm", back_months=12, do_pause=False)
            send_phone_message("Gwen", "Emergency question.", "gwen_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message("Gwen", "Black skirt or jeans?", "gwen_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message(phone_config["phone_player_name"], "Skirt. No contest.", "gwen_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message("Gwen", "It fits. But if anyone stares, that's on YOU. 😉", "gwen_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message(phone_config["phone_player_name"], "What if {b}I{/b} wanna look?", "gwen_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message("Gwen", "Then you better start running, my love. Because I won't be gentle when I catch you.", "gwen_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message(phone_config["phone_player_name"], "...", "gwen_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message("Gwen", "Alright, alright...", "gwen_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message("Gwen", "Not exactly my style, but...", "gwen_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message("Gwen", "images/ch2ep1_1057.jpg", "gwen_dm", 2, do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message("Gwen", "There. You happy now?", "gwen_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message(phone_config["phone_player_name"], "Holy peaches, Gwen. This is... wow. Smoking hot.", "gwen_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message(phone_config["phone_player_name"], "Thinking about it... you never actually send me stuff like this. Why now?", "gwen_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message("Gwen", "For the record, I prefer barging into your room and shoving my ass in your face directly.", "gwen_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message("Gwen", "But just this once, I will indulge you. 😁", "gwen_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message(phone_config["phone_player_name"], "Gwen... you don't go out of character for no reason.", "gwen_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message(phone_config["phone_player_name"], "Is there something I should know?", "gwen_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message("Gwen", "Yeah. But like I said, if we're talking, it's face-to-face. Not over text. Not over calls.", "gwen_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message("Gwen", "Lunch?", "gwen_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message(phone_config["phone_player_name"], "Oh hell yeah. I'm not turning that down.", "gwen_dm", do_pause=False, log_to_history=False, do_restart=False)

            phone_stamp_rel("gwen_dm", back_months=12, do_pause=False)
            send_phone_message("Gwen", "images/ch2ep1_1058.jpg", "gwen_dm", 2, do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message("Gwen", "You look so... sad! ROFL! 🤣", "gwen_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message(phone_config["phone_player_name"], "I {b}am{/b} sad! Stop laughing at me!", "gwen_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message("Gwen", "There, there... It's not like I'm disappearing forever.", "gwen_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message(phone_config["phone_player_name"], "\"I don't know when I can come back.\" What do you think I'm supposed to feel?", "gwen_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message("Gwen", "It's still three months away. We've got time, you know?", "gwen_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message("Gwen", "And hey, I'll still be here for your birthday.", "gwen_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message(phone_config["phone_player_name"], "Fair... 😔", "gwen_dm", do_pause=False, log_to_history=False, do_restart=False)

        ## 11 months ago ##
        phone_stamp_rel("gwen_dm", back_months=11, do_pause=False)
        send_phone_message("Gwen", "I'm at the mall right now.", "gwen_dm", do_pause=False, log_to_history=False, do_restart=False)
        send_phone_message("Gwen", "Birthday boy, tell me if there's anything you want.", "gwen_dm", do_pause=False, log_to_history=False, do_restart=False)
        send_phone_message(phone_config["phone_player_name"], "I don't know, Gwen.", "gwen_dm", do_pause=False, log_to_history=False, do_restart=False)
        send_phone_message(phone_config["phone_player_name"], "I don't really feel like celebrating my birthdays anymore.", "gwen_dm", do_pause=False, log_to_history=False, do_restart=False)
        send_phone_message("Gwen", "The fuck? 🤨", "gwen_dm", do_pause=False, log_to_history=False, do_restart=False)
        if (gwenroute and gwenpoint == 9):
            send_phone_message("Gwen", "Alright then. Go wait in my room.", "gwen_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message("Gwen", "If you're not celebrating, I'll do it for you.", "gwen_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message("Gwen", "Don't argue. Just be there.", "gwen_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message(phone_config["phone_player_name"], "😈😈😈", "gwen_dm", do_pause=False, log_to_history=False, do_restart=False)

            phone_stamp_rel("gwen_dm", back_months=11, do_pause=False)
            send_phone_message("Gwen", "images/ch2ep1_1059.jpg", "gwen_dm", 2, do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message("Gwen", "Gwen - 1, [mc] - 0.", "gwen_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message("Gwen", "Looks like your master plan didn't work. Next time, maybe don't tell me you \"don't feel like celebrating.\"", "gwen_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message(phone_config["phone_player_name"], "Damn it, Gwen.", "gwen_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message(phone_config["phone_player_name"], "Six rounds was insane. You didn't even let me breathe between them. 😫", "gwen_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message("Gwen", "Birthday cardio. You're welcome.", "gwen_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message("Gwen", "Now stop whining. You needed it more than you think. 😜", "gwen_dm", do_pause=False, log_to_history=False, do_restart=False)

        if gwenroute:
            phone_stamp_rel("gwen_dm", back_months=11, do_pause=False)
            send_phone_message("Gwen", "Lunch! Come out! 😠", "gwen_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message(phone_config["phone_player_name"], "Wait, what? Where are you?", "gwen_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message("Gwen", "Where do you think?", "gwen_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message(phone_config["phone_player_name"], "Oh shit! Hold on! Clocking out!", "gwen_dm", do_pause=False, log_to_history=False, do_restart=False)

        ## 10 months ago ##

        ## 9 months ago ##
        if gwenroute:
            phone_stamp_rel("gwen_dm", back_months=9, do_pause=False)
            send_phone_message(phone_config["phone_player_name"], "Is this really it? 😭", "gwen_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message("Gwen", "Hey... don't talk like I'm not coming back.", "gwen_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message("Gwen", "I promised I'll be there for your next birthday.", "gwen_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message(phone_config["phone_player_name"], "images/ch2ep1_1060.jpg", "gwen_dm", 2, do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message(phone_config["phone_player_name"], "😭😭😭", "gwen_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message(phone_config["phone_player_name"], "I hate that this is the last thing I see of you.", "gwen_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message("Gwen", "Hey, stop. Wipe your tears, okay?", "gwen_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message(phone_config["phone_player_name"], "I'm not crying.", "gwen_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message("Gwen", "You are. I can literally see you from the window.", "gwen_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message(phone_config["phone_player_name"], "Where?", "gwen_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message(phone_config["phone_player_name"], "Oh...", "gwen_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message("Gwen", "Wipe them off.", "gwen_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message(phone_config["phone_player_name"], "Okay...", "gwen_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message("Gwen", "Good boy.", "gwen_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message("Gwen", "I told you: do something meaningful while I'm gone. And you promised.", "gwen_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message("Gwen", "So when I get back, something better damn well be waiting for me.", "gwen_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message(phone_config["phone_player_name"], "Yeah. I know what I need to do. I'll get it done before you come back. Promise.", "gwen_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message("Gwen", "Make me proud.", "gwen_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message("Gwen", "Alright, the crew's already yelling at me. I need to turn my phone off.", "gwen_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message("Gwen", "I'll see you later, [mc]. I love you. 😘", "gwen_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message(phone_config["phone_player_name"], "I love you too. See you later... 😔", "gwen_dm", do_pause=False, log_to_history=False, do_restart=False)

            phone_stamp_rel("gwen_dm", back_months=9, do_pause=False)
            send_phone_message("Gwen", "[mc]. Just got settled in, so I figured I'd do a quick check-in.", "gwen_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message("Gwen", "Did you get any sleep?", "gwen_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message("Gwen", "Don't lie to me. I'll know.", "gwen_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message(phone_config["phone_player_name"], "Trying.", "gwen_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message(phone_config["phone_player_name"], "Not exactly winning at it.", "gwen_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message("Gwen", "Try again.", "gwen_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message("Gwen", "Or never mind.", "gwen_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message("Gwen", "I'll just call you.", "gwen_dm", do_pause=False, log_to_history=False, do_restart=False)

            phone_stamp_rel("gwen_dm", back_months=9, do_pause=False)
            send_phone_message("Gwen", "Also, drink some water.", "gwen_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message("Gwen", "I won't be able to text every day.", "gwen_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message("Gwen", "But I'm still here.", "gwen_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message("Gwen", "Okay?", "gwen_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message(phone_config["phone_player_name"], "Okay... 🥲", "gwen_dm", do_pause=False, log_to_history=False, do_restart=False)

        ## 8 months ago ##
        ## 7 months ago ##
        if gwenroute:
            phone_stamp_rel("gwen_dm", back_months=7, do_pause=False)
            send_phone_message("Gwen", "Holy!", "gwen_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message("Gwen", "Saw your charity post!", "gwen_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message("Gwen", "Keep going.", "gwen_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message("Gwen", "Still remember your promise, yeah?", "gwen_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message(phone_config["phone_player_name"], "Yes, boss!", "gwen_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message("Gwen", "Don't wait on me.", "gwen_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message(phone_config["phone_player_name"], "Aye!", "gwen_dm", do_pause=False, log_to_history=False, do_restart=False)

        ## 6 months ago ##
        phone_stamp_rel("gwen_dm", back_months=6, do_pause=False)
        send_phone_message(phone_config["phone_player_name"], "Hey, Gwen. Just checking in.", "gwen_dm", do_pause=False, log_to_history=False, do_restart=False)
        send_phone_message(phone_config["phone_player_name"], "Kinda miss hearing from you.", "gwen_dm", do_pause=False, log_to_history=False, do_restart=False)
        send_phone_message(phone_config["phone_player_name"], "Hope you're eating, sleeping, and... you know. Surviving.", "gwen_dm", do_pause=False, log_to_history=False, do_restart=False)

        phone_stamp_rel("gwen_dm", back_months=6, do_pause=False)
        send_phone_message("Gwen", "Shit! Sorry! I completely missed this.", "gwen_dm", do_pause=False, log_to_history=False, do_restart=False)
        send_phone_message("Gwen", "It's been nonstop. Barely had a second to check my phone.", "gwen_dm", do_pause=False, log_to_history=False, do_restart=False)
        send_phone_message("Gwen", "And don't you dare throw that concern back at me.", "gwen_dm", do_pause=False, log_to_history=False, do_restart=False)
        send_phone_message("Gwen", "YOU eat. YOU sleep.", "gwen_dm", do_pause=False, log_to_history=False, do_restart=False)
        send_phone_message("Gwen", "You hear me?", "gwen_dm", do_pause=False, log_to_history=False, do_restart=False)

        send_phone_message(phone_config["phone_player_name"], "I am.", "gwen_dm", do_pause=False, log_to_history=False, do_restart=False)
        send_phone_message(phone_config["phone_player_name"], "... Mostly.", "gwen_dm", do_pause=False, log_to_history=False, do_restart=False)
        send_phone_message("Gwen", "Call me. I have some time left before the next meeting.", "gwen_dm", do_pause=False, log_to_history=False, do_restart=False)
        send_phone_message(phone_config["phone_player_name"], "😍😍😍", "gwen_dm", do_pause=False, log_to_history=False, do_restart=False)

        ## 5 months ago ##
        phone_stamp_rel("gwen_dm", back_months=5, do_pause=False)
        send_phone_message(phone_config["phone_player_name"], "Saw something today that reminded me of you.", "gwen_dm", do_pause=False, log_to_history=False, do_restart=False)
        send_phone_message(phone_config["phone_player_name"], "Some girl at a café was humming off-key and still looked confident as hell.", "gwen_dm", do_pause=False, log_to_history=False, do_restart=False)
        send_phone_message(phone_config["phone_player_name"], "Made me laugh. You would've rolled your eyes so hard at her. 😂", "gwen_dm", do_pause=False, log_to_history=False, do_restart=False)
        send_phone_message("Gwen", "I absolutely would have.", "gwen_dm", do_pause=False, log_to_history=False, do_restart=False)
        send_phone_message("Gwen", "But I respect the confidence.", "gwen_dm", do_pause=False, log_to_history=False, do_restart=False)
        if gwenroute:
            send_phone_message("Gwen", "Glad I still live rent-free in your head.", "gwen_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message(phone_config["phone_player_name"], "You do.", "gwen_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message(phone_config["phone_player_name"], "You do... 😔", "gwen_dm", do_pause=False, log_to_history=False, do_restart=False)

        ## 4 months ago ##
        if gwenroute:
            phone_stamp_rel("gwen_dm", back_months=4, do_pause=False)
            send_phone_message(phone_config["phone_player_name"], "You holding up okay?", "gwen_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message(phone_config["phone_player_name"], "Not trying to bug you. I've just... been thinking about you a lot lately.", "gwen_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message(phone_config["phone_player_name"], "I don't know what you did to me, but I feel stupidly lonely without you.", "gwen_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message(phone_config["phone_player_name"], "…even with the other girls around.", "gwen_dm", do_pause=False, log_to_history=False, do_restart=False)

            phone_stamp_rel("gwen_dm", back_months=4, do_pause=False)
            send_phone_message("Gwen", "[mc]? Why aren't you answering my calls?", "gwen_dm", do_pause=False, log_to_history=False, do_restart=False)

            phone_stamp_rel("gwen_dm", back_months=4, do_pause=False)
            send_phone_message(phone_config["phone_player_name"], "Fuck me...", "gwen_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message("Gwen", "Hey.", "gwen_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message("Gwen", "I miss you too. Don't spiral on me.", "gwen_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message("Gwen", "And yes, when I get back, I'll absolutely fuck you senseless.", "gwen_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message(phone_config["phone_player_name"], "Calling.", "gwen_dm", do_pause=False, log_to_history=False, do_restart=False)

            phone_stamp_rel("gwen_dm", back_months=4, do_pause=False)
            send_phone_message("Gwen", "Why isn't Aine replying to my text messages?", "gwen_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message(phone_config["phone_player_name"], "We kind of blew up...", "gwen_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message("Gwen", "That \"kind of\" is doing some heavy lifting there. LMAO! 🤣", "gwen_dm", do_pause=False, log_to_history=False, do_restart=False)

        ## 3 months ago ##
        if gwenroute:
            phone_stamp_rel("gwen_dm", back_months=3, do_pause=False)
            send_phone_message("Gwen", "My love still breathing?", "gwen_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message(phone_config["phone_player_name"], "Last I checked, yeah. Unfortunately alive. 😒", "gwen_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message(phone_config["phone_player_name"], "But you barely text, so ask me again in a week.", "gwen_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message("Gwen", "Don't you fucking dare.", "gwen_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message(phone_config["phone_player_name"], "I miss you, Gwen. Come home soon.", "gwen_dm", do_pause=False, log_to_history=False, do_restart=False)

            phone_stamp_rel("gwen_dm", back_months=3, do_pause=False)
            send_phone_message("Gwen", "Sorry for the late reply, [mc].", "gwen_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message("Gwen", "But I'm planning to be back for your birthday.", "gwen_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message("Gwen", "That's a promise. At least to you.", "gwen_dm", do_pause=False, log_to_history=False, do_restart=False)

            send_phone_message(phone_config["phone_player_name"], "... Yeah.", "gwen_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message(phone_config["phone_player_name"], "That's enough to get me through.", "gwen_dm", do_pause=False, log_to_history=False, do_restart=False)

        ## 2 months ago ##
        ## 1 month ago ##







        ##### MOON #####
        ## 13 months ago ##
        phone_stamp_rel("moon_dm", back_months=13, do_pause=False)
        send_phone_message(phone_config["phone_player_name"], "Hey. I've been looking around. Where are you?", "moon_dm", do_pause=False, log_to_history=False, do_restart=False)
        send_phone_message("Moon", "Location update:", "moon_dm", do_pause=False, log_to_history=False, do_restart=False)
        send_phone_message("Moon", "— Near the old rail platform", "moon_dm", do_pause=False, log_to_history=False, do_restart=False)
        send_phone_message("Moon", "— West side", "moon_dm", do_pause=False, log_to_history=False, do_restart=False)
        send_phone_message("Moon", "— Covered", "moon_dm", do_pause=False, log_to_history=False, do_restart=False)
        send_phone_message(phone_config["phone_player_name"], "... Covered?", "moon_dm", do_pause=False, log_to_history=False, do_restart=False)
        send_phone_message("Moon", "Affirmative.", "moon_dm", do_pause=False, log_to_history=False, do_restart=False)
        send_phone_message("Moon", "Windbreak. Partial shade.", "moon_dm", do_pause=False, log_to_history=False, do_restart=False)
        send_phone_message(phone_config["phone_player_name"], "Right. Uh... You waiting for someone?", "moon_dm", do_pause=False, log_to_history=False, do_restart=False)
        send_phone_message("Moon", "Negative.", "moon_dm", do_pause=False, log_to_history=False, do_restart=False)
        send_phone_message("Moon", "Status:", "moon_dm", do_pause=False, log_to_history=False, do_restart=False)
        send_phone_message("Moon", "— Sitting", "moon_dm", do_pause=False, log_to_history=False, do_restart=False)
        send_phone_message("Moon", "— Observing foot traffic", "moon_dm", do_pause=False, log_to_history=False, do_restart=False)
        send_phone_message("Moon", "— Lollipop and hot chocolate acquired", "moon_dm", do_pause=False, log_to_history=False, do_restart=False)
        send_phone_message(phone_config["phone_player_name"], "Huh...", "moon_dm", do_pause=False, log_to_history=False, do_restart=False)
        send_phone_message(phone_config["phone_player_name"], "Didn't know you text this way. It's like you're filing a report.", "moon_dm", do_pause=False, log_to_history=False, do_restart=False)
        send_phone_message(phone_config["phone_player_name"], "LOL. 😅", "moon_dm", do_pause=False, log_to_history=False, do_restart=False)
        send_phone_message("Moon", "Correction.", "moon_dm", do_pause=False, log_to_history=False, do_restart=False)
        send_phone_message("Moon", "This is concise.", "moon_dm", do_pause=False, log_to_history=False, do_restart=False)
        send_phone_message(phone_config["phone_player_name"], "Most people don't list bullet points like this, you know?", "moon_dm", do_pause=False, log_to_history=False, do_restart=False)
        send_phone_message("Moon", "People waste time.", "moon_dm", do_pause=False, log_to_history=False, do_restart=False)
        send_phone_message(phone_config["phone_player_name"], "Fair enough. Can you just... say where exactly you are?", "moon_dm", do_pause=False, log_to_history=False, do_restart=False)
        send_phone_message("Moon", "Stand by.", "moon_dm", do_pause=False, log_to_history=False, do_restart=False)
        send_phone_message("Moon", "Refining.", "moon_dm", do_pause=False, log_to_history=False, do_restart=False)
        send_phone_message("Moon", "Bench. Third from the left.", "moon_dm", do_pause=False, log_to_history=False, do_restart=False)
        send_phone_message("Moon", "Blue paint. Chipped.", "moon_dm", do_pause=False, log_to_history=False, do_restart=False)
        send_phone_message("Moon", "You'll see me before I see you.", "moon_dm", do_pause=False, log_to_history=False, do_restart=False)
        send_phone_message(phone_config["phone_player_name"], "That's... not ominous at all.", "moon_dm", do_pause=False, log_to_history=False, do_restart=False)
        send_phone_message("Moon", "Noted.", "moon_dm", do_pause=False, log_to_history=False, do_restart=False)
        send_phone_message("Moon", "Intent was efficiency.", "moon_dm", do_pause=False, log_to_history=False, do_restart=False)
        send_phone_message(phone_config["phone_player_name"], "I think I'm close.", "moon_dm", do_pause=False, log_to_history=False, do_restart=False)
        send_phone_message("Moon", "Copy.", "moon_dm", do_pause=False, log_to_history=False, do_restart=False)
        send_phone_message("Moon", "I have eyes on you.", "moon_dm", do_pause=False, log_to_history=False, do_restart=False)
        send_phone_message(phone_config["phone_player_name"], "... You didn't have to say it like that.", "moon_dm", do_pause=False, log_to_history=False, do_restart=False)
        send_phone_message(phone_config["phone_player_name"], "Okay. Found you.", "moon_dm", do_pause=False, log_to_history=False, do_restart=False)

        phone_stamp_rel("moon_dm", back_months=13, do_pause=False)
        send_phone_message(phone_config["phone_player_name"], "I made it home, Capt.", "moon_dm", do_pause=False, log_to_history=False, do_restart=False)
        send_phone_message("Moon", "Copy.", "moon_dm", do_pause=False, log_to_history=False, do_restart=False)
        send_phone_message("Moon", "Status check:", "moon_dm", do_pause=False, log_to_history=False, do_restart=False)
        send_phone_message("Moon", "— You: upright", "moon_dm", do_pause=False, log_to_history=False, do_restart=False)
        send_phone_message("Moon", "— Mood: stable", "moon_dm", do_pause=False, log_to_history=False, do_restart=False)
        send_phone_message("Moon", "— Injuries: none observed", "moon_dm", do_pause=False, log_to_history=False, do_restart=False)
        send_phone_message(phone_config["phone_player_name"], "You didn't observe me getting home.", "moon_dm", do_pause=False, log_to_history=False, do_restart=False)
        send_phone_message("Moon", "Inference.", "moon_dm", do_pause=False, log_to_history=False, do_restart=False)
        send_phone_message("Moon", "Your gait was steady when we separated.", "moon_dm", do_pause=False, log_to_history=False, do_restart=False)
        send_phone_message(phone_config["phone_player_name"], "You really don't turn this off, do you? 😕", "moon_dm", do_pause=False, log_to_history=False, do_restart=False)
        send_phone_message("Moon", "Negative.", "moon_dm", do_pause=False, log_to_history=False, do_restart=False)
        send_phone_message("Moon", "But I can... deprioritize.", "moon_dm", do_pause=False, log_to_history=False, do_restart=False)
        send_phone_message(phone_config["phone_player_name"], "That sounds reassuring. I think.", "moon_dm", do_pause=False, log_to_history=False, do_restart=False)
        send_phone_message("Moon", "After-Action Summary:", "moon_dm", do_pause=False, log_to_history=False, do_restart=False)
        send_phone_message("Moon", "— Time spent: productive", "moon_dm", do_pause=False, log_to_history=False, do_restart=False)
        send_phone_message("Moon", "— Environment: acceptable", "moon_dm", do_pause=False, log_to_history=False, do_restart=False)
        send_phone_message("Moon", "— Company:", "moon_dm", do_pause=False, log_to_history=False, do_restart=False)
        send_phone_message("Moon", "   • yours", "moon_dm", do_pause=False, log_to_history=False, do_restart=False)
        send_phone_message("Moon", "   • unexpectedly... good", "moon_dm", do_pause=False, log_to_history=False, do_restart=False)
        send_phone_message(phone_config["phone_player_name"], "\"Unexpectedly?\"", "moon_dm", do_pause=False, log_to_history=False, do_restart=False)
        send_phone_message("Moon", "Clarification.", "moon_dm", do_pause=False, log_to_history=False, do_restart=False)
        send_phone_message("Moon", "Expectation was high.", "moon_dm", do_pause=False, log_to_history=False, do_restart=False)
        send_phone_message("Moon", "Outcome exceeded baseline.", "moon_dm", do_pause=False, log_to_history=False, do_restart=False)
        send_phone_message(phone_config["phone_player_name"], "I'll take that as a compliment.", "moon_dm", do_pause=False, log_to_history=False, do_restart=False)
        send_phone_message("Moon", "You should.", "moon_dm", do_pause=False, log_to_history=False, do_restart=False)
        send_phone_message("Moon", "I don't inflate reports.", "moon_dm", do_pause=False, log_to_history=False, do_restart=False)
        send_phone_message(phone_config["phone_player_name"], "Noted. Anything else in your report?", "moon_dm", do_pause=False, log_to_history=False, do_restart=False)
        send_phone_message("Moon", "One addendum.", "moon_dm", do_pause=False, log_to_history=False, do_restart=False)
        send_phone_message("Moon", "— You laughed more than usual.", "moon_dm", do_pause=False, log_to_history=False, do_restart=False)
        send_phone_message(phone_config["phone_player_name"], "Is that bad?", "moon_dm", do_pause=False, log_to_history=False, do_restart=False)
        send_phone_message("Moon", "Negative.", "moon_dm", do_pause=False, log_to_history=False, do_restart=False)
        send_phone_message("Moon", "Assessment: positive deviation.", "moon_dm", do_pause=False, log_to_history=False, do_restart=False)
        send_phone_message("Moon", "Low risk. Acceptable.", "moon_dm", do_pause=False, log_to_history=False, do_restart=False)
        send_phone_message(phone_config["phone_player_name"], "😅", "moon_dm", do_pause=False, log_to_history=False, do_restart=False)
        send_phone_message(phone_config["phone_player_name"], "Guess it'll take some time to get used to this.", "moon_dm", do_pause=False, log_to_history=False, do_restart=False)
        send_phone_message(phone_config["phone_player_name"], "Anyway, stay safe.", "moon_dm", do_pause=False, log_to_history=False, do_restart=False)
        send_phone_message(phone_config["phone_player_name"], "Say hi to Jess for me.", "moon_dm", do_pause=False, log_to_history=False, do_restart=False)
        send_phone_message("Moon", "Copy.", "moon_dm", do_pause=False, log_to_history=False, do_restart=False)
        send_phone_message("Moon", "I will.", "moon_dm", do_pause=False, log_to_history=False, do_restart=False)

        ## 12 months ago ##
        ## 11 months ago ##
        if (moonroute and moonpoint == 6):
            phone_stamp_rel("moon_dm", back_months=11, do_pause=False)
            send_phone_message(phone_config["phone_player_name"], "So, uh... Capt. I heard you know I'm not celebrating my birthday this year.", "moon_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message("Moon", "Copy.", "moon_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message("Moon", "Intel source was reliable.", "moon_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message(phone_config["phone_player_name"], "What? Reliable?", "moon_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message("Moon", "High confidence.", "moon_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message("Moon", "Motivation assessment: predictable.", "moon_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message(phone_config["phone_player_name"], "Predictable?", "moon_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message("Moon", "You planned the \"I don't want anything\" approach to get me alone.", "moon_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message("Moon", "Birthday bypass strategy.", "moon_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message("Moon", "Objective: intimacy.", "moon_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message(phone_config["phone_player_name"], "How the hell do you always figure this out so fast?", "moon_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message("Moon", "Pattern recognition.", "moon_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message("Moon", "You made the same face every year in the past.", "moon_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message(phone_config["phone_player_name"], "I have a face?", "moon_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message("Moon", "Affirmative.", "moon_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message("Moon", "\"Seduction face.\"", "moon_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message(phone_config["phone_player_name"], "Okay, first of all, rude.", "moon_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message(phone_config["phone_player_name"], "Second of all... you're not wrong.", "moon_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message("Moon", "Already complied.", "moon_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message("Moon", "Mission: successful.", "moon_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message(phone_config["phone_player_name"], "So you're not mad about it?", "moon_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message("Moon", "Negative.", "moon_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message("Moon", "I liked watching you try.", "moon_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message("Moon", "And I liked what followed.", "moon_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message(phone_config["phone_player_name"], "...", "moon_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message(phone_config["phone_player_name"], "I feel extremely seen right now.", "moon_dm", do_pause=False, log_to_history=False, do_restart=False)

            phone_stamp_rel("moon_dm", back_months=11, do_pause=False)
            send_phone_message(phone_config["phone_player_name"], "images/ch2ep1_1064.jpg", "moon_dm", 2, do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message(phone_config["phone_player_name"], "Not gonna lie...", "moon_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message(phone_config["phone_player_name"], "Best birthday I've ever had.", "moon_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message("Moon", "I keep looking at that photo, and I recall our past.", "moon_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message("Moon", "It's strange.", "moon_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message("Moon", "But I don't remember feeling so alive like how it is with us now.", "moon_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message("Moon", "Like you could see all the way through me.", "moon_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message(phone_config["phone_player_name"], "I did.", "moon_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message(phone_config["phone_player_name"], "I always do.", "moon_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message("Moon", "😳", "moon_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message("Moon", "Please keep looking at me like that.", "moon_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message("Moon", "...", "moon_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message("Moon", "Disregard previous transmission.", "moon_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message("Moon", "Emotional clarity temporarily compromised.", "moon_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message("Moon", "Post-operation condition: elevated.", "moon_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message("Moon", "This is normal.", "moon_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message("Moon", "Contained.", "moon_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message("Moon", "Under control.", "moon_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message(phone_config["phone_player_name"], "You okay there, Captain?", "moon_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message("Moon", "Affirmative, Commander.", "moon_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message("Moon", "Status restored.", "moon_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message("Moon", "However...", "moon_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message("Moon", "Recommending same strategy next year.", "moon_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message("Moon", "I'll be ready.", "moon_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message(phone_config["phone_player_name"], "Then I'd like you to at least pretend to have no idea. 😑", "moon_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message("Moon", "Negative.", "moon_dm", do_pause=False, log_to_history=False, do_restart=False)

        ## 10 months ago ##
        ## 9 months ago ##
        if (moonroute and moonpoint == 6):
            phone_stamp_rel("moon_dm", back_months=9, do_pause=False)
            send_phone_message("Moon", "images/ch2ep1_1063.jpg", "moon_dm", 2, do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message(phone_config["phone_player_name"], "... Wow.", "moon_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message(phone_config["phone_player_name"], "Now that ain't fair. Taking that photo without me.", "moon_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message(phone_config["phone_player_name"], "You look incredible, Moon.", "moon_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message(phone_config["phone_player_name"], "If this is how my secretary clocks in, I might need a minute to recover.", "moon_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message("Moon", "Observation:", "moon_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message("Moon", "You're flustered.", "moon_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message(phone_config["phone_player_name"], "A little.", "moon_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message(phone_config["phone_player_name"], "Really damn happy you're working with me now.", "moon_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message("Moon", "Copy.", "moon_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message("Moon", "New objective logged:", "moon_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message("Moon", "— stay by your side", "moon_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message("Moon", "— permanent assignment", "moon_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message("Moon", "No transfer requests.", "moon_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message(phone_config["phone_player_name"], "Permanent, huh?", "moon_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message("Moon", "Affirmative.", "moon_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message("Moon", "Forever is the plan.", "moon_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message(phone_config["phone_player_name"], "I love you, Moon. Past and present.", "moon_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message("Moon", "😳🤯", "moon_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message(phone_config["phone_player_name"], "You froze again? I thought you got past that already?", "moon_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message("Moon", "Negative.", "moon_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message("Moon", "I did not freeze.", "moon_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message("Moon", "I was...", "moon_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message("Moon", "...", "moon_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message("Moon", "Reassessing.", "moon_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message(phone_config["phone_player_name"], "But you froze...", "moon_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message("Moon", "i dnt freeze.", "moon_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message("Moon", "I jus", "moon_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message("Moon", "u knw what i mean.", "moon_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message(phone_config["phone_player_name"], "LMAO! 🤣", "moon_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message(phone_config["phone_player_name"], "Okay, okay. I'll stop pushing. Looks like I broke you already.", "moon_dm", do_pause=False, log_to_history=False, do_restart=False)
        
        ## 8 months ago ##
        ## 7 months ago ##
        if moonroute:
            phone_stamp_rel("moon_dm", back_months=7, do_pause=False)
            send_phone_message(phone_config["phone_player_name"], "Status update:", "moon_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message(phone_config["phone_player_name"], "— You didn't realize you were smiling during the meeting, Cap", "moon_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message(phone_config["phone_player_name"], "— It stuck with me longer than it should have", "moon_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message(phone_config["phone_player_name"], "— I don't think I ever stopped choosing you", "moon_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message("Moon", "That's not how the format works, Commander.", "moon_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message(phone_config["phone_player_name"], "I think it works perfectly, though.", "moon_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message("Moon", "Assessment:", "moon_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message("Moon", "— reckless", "moon_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message("Moon", "— imprecise", "moon_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message("Moon", "— effective", "moon_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message(phone_config["phone_player_name"], "Effective?", "moon_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message("Moon", "Heart rate elevated.", "moon_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message("Moon", "So yes.", "moon_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message(phone_config["phone_player_name"], "Good to know.", "moon_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message("Moon", "One correction.", "moon_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message("Moon", "You forgot the conclusion line.", "moon_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message(phone_config["phone_player_name"], "Conclusion:", "moon_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message(phone_config["phone_player_name"], "— You're mine, Moon.", "moon_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message("Moon", "😍", "moon_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message("Moon", "Conclusion acknowledged.", "moon_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message("Moon", "And reciprocated.", "moon_dm", do_pause=False, log_to_history=False, do_restart=False)

        ## 6 months ago ##
        ## 5 months ago ##
        ## 4 months ago ##
        phone_stamp_rel("moon_dm", back_months=4, do_pause=False)
        send_phone_message(phone_config["phone_player_name"], "Capt. I need you.", "moon_dm", do_pause=False, log_to_history=False, do_restart=False)
        send_phone_message(phone_config["phone_player_name"], "Aine and I blew up.", "moon_dm", do_pause=False, log_to_history=False, do_restart=False)
        send_phone_message(phone_config["phone_player_name"], "Expansion's moving, but she thinks I cut her out. Again.", "moon_dm", do_pause=False, log_to_history=False, do_restart=False)
        send_phone_message("Moon", "Copy.", "moon_dm", do_pause=False, log_to_history=False, do_restart=False)
        send_phone_message("Moon", "Give me your decision. In one line.", "moon_dm", do_pause=False, log_to_history=False, do_restart=False)
        send_phone_message(phone_config["phone_player_name"], "We proceed with Phase One expansion this week.", "moon_dm", do_pause=False, log_to_history=False, do_restart=False)
        send_phone_message(phone_config["phone_player_name"], "I'm not freezing the charity because we can't agree.", "moon_dm", do_pause=False, log_to_history=False, do_restart=False)
        send_phone_message("Moon", "Affirmative.", "moon_dm", do_pause=False, log_to_history=False, do_restart=False)
        send_phone_message("Moon", "That's defensible.", "moon_dm", do_pause=False, log_to_history=False, do_restart=False)
        send_phone_message("Moon", "Gridlock kills momentum. Momentum is food, medicine, beds.", "moon_dm", do_pause=False, log_to_history=False, do_restart=False)
        send_phone_message(phone_config["phone_player_name"], "Thank you.", "moon_dm", do_pause=False, log_to_history=False, do_restart=False)
        send_phone_message(phone_config["phone_player_name"], "I need you to do something.", "moon_dm", do_pause=False, log_to_history=False, do_restart=False)
        send_phone_message(phone_config["phone_player_name"], "Lock the expansion tasks in and push them forward.", "moon_dm", do_pause=False, log_to_history=False, do_restart=False)
        send_phone_message(phone_config["phone_player_name"], "But do it clean. Paper trail, approvals, donors. No mess.", "moon_dm", do_pause=False, log_to_history=False, do_restart=False)
        send_phone_message("Moon", "Copy.", "moon_dm", do_pause=False, log_to_history=False, do_restart=False)
        send_phone_message("Moon", "Action items:", "moon_dm", do_pause=False, log_to_history=False, do_restart=False)
        send_phone_message("Moon", "— Confirm Phase One scope + budget ceiling", "moon_dm", do_pause=False, log_to_history=False, do_restart=False)
        send_phone_message("Moon", "— Freeze Phase Two until joint sign-off", "moon_dm", do_pause=False, log_to_history=False, do_restart=False)
        send_phone_message("Moon", "— Draft comms for staff + donors: \"time-sensitive rollout\"", "moon_dm", do_pause=False, log_to_history=False, do_restart=False)
        send_phone_message("Moon", "— Schedule partner briefing with Aine within 24 hours", "moon_dm", do_pause=False, log_to_history=False, do_restart=False)
        send_phone_message(phone_config["phone_player_name"], "You're really taking my side?", "moon_dm", do_pause=False, log_to_history=False, do_restart=False)
        send_phone_message("Moon", "I'm taking the charity's side.", "moon_dm", do_pause=False, log_to_history=False, do_restart=False)
        send_phone_message("Moon", "Your call keeps the mission alive.", "moon_dm", do_pause=False, log_to_history=False, do_restart=False)
        send_phone_message("Moon", "But your method is bleeding trust.", "moon_dm", do_pause=False, log_to_history=False, do_restart=False)
        send_phone_message(phone_config["phone_player_name"], "... Yeah. I feel bad about it, but I'm thinking about our people.", "moon_dm", do_pause=False, log_to_history=False, do_restart=False)
        send_phone_message(phone_config["phone_player_name"], "What do I say to her?", "moon_dm", do_pause=False, log_to_history=False, do_restart=False)
        send_phone_message("Moon", "Say this:", "moon_dm", do_pause=False, log_to_history=False, do_restart=False)
        send_phone_message("Moon", "— \"I acted because people are waiting.\"", "moon_dm", do_pause=False, log_to_history=False, do_restart=False)
        send_phone_message("Moon", "— \"I should've looped you in before it landed.\"", "moon_dm", do_pause=False, log_to_history=False, do_restart=False)
        send_phone_message("Moon", "— \"Phase Two doesn't move without you.\"", "moon_dm", do_pause=False, log_to_history=False, do_restart=False)
        send_phone_message("Moon", "No sarcasm. No winning the argument.", "moon_dm", do_pause=False, log_to_history=False, do_restart=False)
        send_phone_message(phone_config["phone_player_name"], "She said I don't see her anymore.", "moon_dm", do_pause=False, log_to_history=False, do_restart=False)
        send_phone_message(phone_config["phone_player_name"], "Stuck in me more than it should.", "moon_dm", do_pause=False, log_to_history=False, do_restart=False)
        send_phone_message("Moon", "That's not about the expansion, but about being outpaced by your life.", "moon_dm", do_pause=False, log_to_history=False, do_restart=False)
        send_phone_message("Moon", "Give her a lane. Give her visibility. Give her a \"first call\" rule.", "moon_dm", do_pause=False, log_to_history=False, do_restart=False)
        send_phone_message(phone_config["phone_player_name"], "First call rule?", "moon_dm", do_pause=False, log_to_history=False, do_restart=False)
        send_phone_message("Moon", "If it's urgent, you act.", "moon_dm", do_pause=False, log_to_history=False, do_restart=False)
        send_phone_message("Moon", "If it's not urgent, she hears it from you before the world does.", "moon_dm", do_pause=False, log_to_history=False, do_restart=False)
        send_phone_message("Moon", "Partnership, so to say.", "moon_dm", do_pause=False, log_to_history=False, do_restart=False)
        send_phone_message(phone_config["phone_player_name"], "Alright.", "moon_dm", do_pause=False, log_to_history=False, do_restart=False)
        send_phone_message(phone_config["phone_player_name"], "Do the paperwork. I'll handle Aine.", "moon_dm", do_pause=False, log_to_history=False, do_restart=False)
        send_phone_message("Moon", "Wilco.", "moon_dm", do_pause=False, log_to_history=False, do_restart=False)
        send_phone_message("Moon", "And Commander?", "moon_dm", do_pause=False, log_to_history=False, do_restart=False)
        send_phone_message("Moon", "Next time you feel the storm coming, don't wait for lightning.", "moon_dm", do_pause=False, log_to_history=False, do_restart=False)
        send_phone_message("Moon", "Brief your partner first.", "moon_dm", do_pause=False, log_to_history=False, do_restart=False)
        send_phone_message(phone_config["phone_player_name"], "Affirmative.", "moon_dm", do_pause=False, log_to_history=False, do_restart=False)

        ## 3 months ago ##
        ## 2 months ago ##
        phone_stamp_rel("moon_dm", back_months=2, do_pause=False)
        send_phone_message(phone_config["phone_player_name"], "Hey, Capt. About the sword.", "moon_dm", do_pause=False, log_to_history=False, do_restart=False)
        send_phone_message("Moon", "Copy.", "moon_dm", do_pause=False, log_to_history=False, do_restart=False)
        send_phone_message("Moon", "What about it?", "moon_dm", do_pause=False, log_to_history=False, do_restart=False)
        send_phone_message(phone_config["phone_player_name"], "Sometimes when I hold it, it feels somewhat wrong.", "moon_dm", do_pause=False, log_to_history=False, do_restart=False)
        send_phone_message(phone_config["phone_player_name"], "It's not heavy. But it's as if it's alive.", "moon_dm", do_pause=False, log_to_history=False, do_restart=False)
        send_phone_message("Moon", "Alive?", "moon_dm", do_pause=False, log_to_history=False, do_restart=False)
        send_phone_message(phone_config["phone_player_name"], "I hear things.", "moon_dm", do_pause=False, log_to_history=False, do_restart=False)
        send_phone_message(phone_config["phone_player_name"], "It's not clear. Like voices under water.", "moon_dm", do_pause=False, log_to_history=False, do_restart=False)
        send_phone_message(phone_config["phone_player_name"], "It only happens when I'm alone.", "moon_dm", do_pause=False, log_to_history=False, do_restart=False)
        send_phone_message("Moon", "...", "moon_dm", do_pause=False, log_to_history=False, do_restart=False)
        send_phone_message(phone_config["phone_player_name"], "Is it cursed or something?", "moon_dm", do_pause=False, log_to_history=False, do_restart=False)
        send_phone_message(phone_config["phone_player_name"], "Because if it is, I'd really like a heads up before I even think of unsheathing it.", "moon_dm", do_pause=False, log_to_history=False, do_restart=False)
        send_phone_message("Moon", "Negative.", "moon_dm", do_pause=False, log_to_history=False, do_restart=False)
        send_phone_message("Moon", "Not cursed.", "moon_dm", do_pause=False, log_to_history=False, do_restart=False)
        send_phone_message(phone_config["phone_player_name"], "That pause didn't help.", "moon_dm", do_pause=False, log_to_history=False, do_restart=False)
        send_phone_message("Moon", "It remembers you.", "moon_dm", do_pause=False, log_to_history=False, do_restart=False)
        send_phone_message(phone_config["phone_player_name"], "Remembers how?", "moon_dm", do_pause=False, log_to_history=False, do_restart=False)
        send_phone_message("Moon", "You used it before.", "moon_dm", do_pause=False, log_to_history=False, do_restart=False)
        send_phone_message("Moon", "Not in this life.", "moon_dm", do_pause=False, log_to_history=False, do_restart=False)
        send_phone_message("Moon", "But it was always yours.", "moon_dm", do_pause=False, log_to_history=False, do_restart=False)
        send_phone_message(phone_config["phone_player_name"], "That's not helping either. I know it's mine. But this thing doesn't speak to me centuries ago.", "moon_dm", do_pause=False, log_to_history=False, do_restart=False)
        send_phone_message("Moon", "I eventually passed it on before I took my life, but it simply went back to me.", "moon_dm", do_pause=False, log_to_history=False, do_restart=False)
        send_phone_message("Moon", "But even then, it never listened to me the way it listens to you, now that I have Sora's memories.", "moon_dm", do_pause=False, log_to_history=False, do_restart=False)
        send_phone_message(phone_config["phone_player_name"], "Listens?", "moon_dm", do_pause=False, log_to_history=False, do_restart=False)
        send_phone_message("Moon", "Responds.", "moon_dm", do_pause=False, log_to_history=False, do_restart=False)
        send_phone_message("Moon", "It's waiting.", "moon_dm", do_pause=False, log_to_history=False, do_restart=False)
        send_phone_message(phone_config["phone_player_name"], "Waiting for what?", "moon_dm", do_pause=False, log_to_history=False, do_restart=False)
        send_phone_message("Moon", "For you to reach back to it.", "moon_dm", do_pause=False, log_to_history=False, do_restart=False)
        send_phone_message(phone_config["phone_player_name"], "Moon...", "moon_dm", do_pause=False, log_to_history=False, do_restart=False)
        send_phone_message("Moon", "You're not in danger.", "moon_dm", do_pause=False, log_to_history=False, do_restart=False)
        send_phone_message("Moon", "If the voices get louder, tell me.", "moon_dm", do_pause=False, log_to_history=False, do_restart=False)
        send_phone_message(phone_config["phone_player_name"], "You've dealt with this before?", "moon_dm", do_pause=False, log_to_history=False, do_restart=False)
        send_phone_message("Moon", "I have.", "moon_dm", do_pause=False, log_to_history=False, do_restart=False)
        send_phone_message("Moon", "And you trusted me then.", "moon_dm", do_pause=False, log_to_history=False, do_restart=False)
        send_phone_message("Moon", "You can trust me now.", "moon_dm", do_pause=False, log_to_history=False, do_restart=False)
        send_phone_message(phone_config["phone_player_name"], "Alright.", "moon_dm", do_pause=False, log_to_history=False, do_restart=False)
        send_phone_message(phone_config["phone_player_name"], "I'll keep it close.", "moon_dm", do_pause=False, log_to_history=False, do_restart=False)

        ## 1 months ago ##






        ##### EMMA #####
        ## 13 months ago ##
        phone_stamp_rel("emma_dm", back_months=13, do_pause=False)
        send_phone_message("Emma", "[mc]. [mc]. Emergency.", "emma_dm", do_pause=False, log_to_history=False, do_restart=False)
        send_phone_message(phone_config["phone_player_name"], "Emergency? What happened?", "emma_dm", do_pause=False, log_to_history=False, do_restart=False)
        send_phone_message("Emma", "I need to take a photo of myself for online authentication.", "emma_dm", do_pause=False, log_to_history=False, do_restart=False)
        send_phone_message("Emma", "How do I switch to the front camera?", "emma_dm", do_pause=False, log_to_history=False, do_restart=False)
        send_phone_message(phone_config["phone_player_name"], "... You're serious?", "emma_dm", do_pause=False, log_to_history=False, do_restart=False)
        send_phone_message("Emma", "🫣", "emma_dm", do_pause=False, log_to_history=False, do_restart=False)
        send_phone_message("Emma", "I'm not very tech-savvy, okay?", "emma_dm", do_pause=False, log_to_history=False, do_restart=False)
        send_phone_message("Emma", "I'll learn once you teach me.", "emma_dm", do_pause=False, log_to_history=False, do_restart=False)
        send_phone_message(phone_config["phone_player_name"], "I'm quite impressed you've survived this long.", "emma_dm", do_pause=False, log_to_history=False, do_restart=False)
        send_phone_message(phone_config["phone_player_name"], "Next to the capture button, see the two arrows forming a circle?", "emma_dm", do_pause=False, log_to_history=False, do_restart=False)
        send_phone_message(phone_config["phone_player_name"], "Tap that.", "emma_dm", do_pause=False, log_to_history=False, do_restart=False)
        if emmaroute:
            send_phone_message("Emma", "images/ch2ep1_1061.jpg", "emma_dm", 2, do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message("Emma", "Okay, it worked.", "emma_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message("Emma", "But how do I delete this?", "emma_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message(phone_config["phone_player_name"], "You can't. Once it's sent, it's mine forever.", "emma_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message("Emma", "Then just don't save it.", "emma_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message("Emma", "Problem solved.", "emma_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message(phone_config["phone_player_name"], "Sure.", "emma_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message("Emma", "...", "emma_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message("Emma", "You saved it.", "emma_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message(phone_config["phone_player_name"], "Of course I did.", "emma_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message(phone_config["phone_player_name"], "You telling me not to save it is basically reverse psychology.", "emma_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message(phone_config["phone_player_name"], "I'm keeping this as evidence of your crimes, Detective. 😈", "emma_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message(phone_config["phone_player_name"], "See you in bed.", "emma_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message(phone_config["phone_player_name"], "I mean, in court!", "emma_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message("Emma", "WHY?? 😡", "emma_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message(phone_config["phone_player_name"], "Really like how you've been styling your hair lately. You should keep it.", "emma_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message("Emma", "🥰", "emma_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message("Emma", "You mean that?", "emma_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message(phone_config["phone_player_name"], "Yeah. It kinda reminds me of how you wore it back when we were kids.", "emma_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message("Emma", "🤔", "emma_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message("Emma", "Okay, I will. 😊", "emma_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message("Emma", "I love you!", "emma_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message(phone_config["phone_player_name"], "I love you too, Em.", "emma_dm", do_pause=False, log_to_history=False, do_restart=False)

        ## 12 months ago ##
        if emmaroute:
            phone_stamp_rel("emma_dm", back_months=12, do_pause=False)
            send_phone_message("Emma", "[mc]. [mc]. Quick question.", "emma_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message("Emma", "Possibly urgent. Possibly stupid.", "emma_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message(phone_config["phone_player_name"], "You have my attention.", "emma_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message("Emma", "My laptop says it needs an update.", "emma_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message("Emma", "If I click it, will it explode?", "emma_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message(phone_config["phone_player_name"], "Thank you for contacting [mc]Tech™ Support.", "emma_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message(phone_config["phone_player_name"], "My name is [mc]. I'll be assisting you today.", "emma_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message("Emma", "Huh? What are you talking about?", "emma_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message(phone_config["phone_player_name"], "Before we proceed, I must ask:", "emma_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message(phone_config["phone_player_name"], "Have you tried turning it off and on again?", "emma_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message("Emma", "Hold on.", "emma_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message("Emma", "Okay, I did that. It's still asking to update.", "emma_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message(phone_config["phone_player_name"], "Excellent. Progress has been made.", "emma_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message(phone_config["phone_player_name"], "Now, please click the update button.", "emma_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message(phone_config["phone_player_name"], "Your device will not explode. Probably.", "emma_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message("Emma", "\"Probably\" is not reassuring.", "emma_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message("Emma", "Okay. I clicked it.", "emma_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message(phone_config["phone_player_name"], "Great choice.", "emma_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message(phone_config["phone_player_name"], "While we wait, please refrain from touching anything.", "emma_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message("Emma", "Too late.", "emma_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message(phone_config["phone_player_name"], "Emmaaaaaaaaaa!", "emma_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message("Emma", "Relax! I just adjusted the brightness.", "emma_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message("Emma", "It's done now. It says \"Update Complete.\"", "emma_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message(phone_config["phone_player_name"], "Congratulations.", "emma_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message(phone_config["phone_player_name"], "Your system is up to date and your life remains intact.", "emma_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message("Emma", "Wow.", "emma_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message("Emma", "Thank you, Mr. Tech Support.", "emma_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message(phone_config["phone_player_name"], "Anytime.", "emma_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message(phone_config["phone_player_name"], "[mc]Tech™ Support is available 24/7.", "emma_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message(phone_config["phone_player_name"], "Payment accepted in snacks, compliments, or coffee.", "emma_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message("Emma", "I love you. Keep the change. 😘", "emma_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message(phone_config["phone_player_name"], "Payment received: one (1) heartfelt \"I love you.\"","emma_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message(phone_config["phone_player_name"], "No receipt needed. Transaction complete.","emma_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message(phone_config["phone_player_name"], "Thank you for choosing [mc]Tech™ Support.","emma_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message(phone_config["phone_player_name"], "Please come again if the internet scares you.","emma_dm", do_pause=False, log_to_history=False, do_restart=False)

        ## 11 months ago ##
        phone_stamp_rel("emma_dm", back_months=11, do_pause=False)
        send_phone_message("Emma", "[mc]. [mc]. Happy birthday! 🥰", "emma_dm", do_pause=False, log_to_history=False, do_restart=False)
        send_phone_message("Emma", "I checked the date twice to be sure.", "emma_dm", do_pause=False, log_to_history=False, do_restart=False)
        send_phone_message(phone_config["phone_player_name"], "Thanks, Em.", "emma_dm", do_pause=False, log_to_history=False, do_restart=False)
        send_phone_message(phone_config["phone_player_name"], "But I don't really feel like celebrating my birthdays anymore.", "emma_dm", do_pause=False, log_to_history=False, do_restart=False)
        send_phone_message("Emma", "What?", "emma_dm", do_pause=False, log_to_history=False, do_restart=False)
        if (emmaroute and emmapoint == 5):
            send_phone_message("Emma", "No. I won't accept that.", "emma_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message("Emma", "I'm clocking out early. I'm coming to get you.", "emma_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message("Emma", "We're buying a cake. This is not optional.", "emma_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message("Emma", "Stay there, okay?", "emma_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message(phone_config["phone_player_name"], "Okay...", "emma_dm", do_pause=False, log_to_history=False, do_restart=False)

            phone_stamp_rel("emma_dm", back_months=11, do_pause=False)
            send_phone_message(phone_config["phone_player_name"], "images/ch2ep1_1062.jpg", "emma_dm", 2, do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message("Emma", "Stop slapping my butt!", "emma_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message(phone_config["phone_player_name"], "I don't know. Kinda felt like an invitation.", "emma_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message("Emma", "I hate you for planning this.", "emma_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message("Emma", "I didn't see through it at all. Not even a little.", "emma_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message(phone_config["phone_player_name"], "Guess that makes me your weakness.", "emma_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message(phone_config["phone_player_name"], "That, and technology.", "emma_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message("Emma", "Unfortunately... yes.", "emma_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message(phone_config["phone_player_name"], "Love you, Em.", "emma_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message("Emma", "I love you too, [mc]. I did enjoy tonight.", "emma_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message("Emma", "Just not the slapping.", "emma_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message(phone_config["phone_player_name"], "You're making it very hard to behave. 🤣", "emma_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message("Emma", "😡", "emma_dm", do_pause=False, log_to_history=False, do_restart=False)

        if emmaroute:
            phone_stamp_rel("emma_dm", back_months=11, do_pause=False)
            send_phone_message("Emma", "[mc]. [mc].", "emma_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message("Emma", "I need [mc]Tech™ Support again.", "emma_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message(phone_config["phone_player_name"], "[mc]Tech™ Support online.", "emma_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message(phone_config["phone_player_name"], "Please describe the issue without panicking.", "emma_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message("Emma", "I am already panicking.", "emma_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message("Emma", "I got an email that says my account has been compromised.", "emma_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message(phone_config["phone_player_name"], "Understood.", "emma_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message(phone_config["phone_player_name"], "First question.", "emma_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message(phone_config["phone_player_name"], "Did the email address look even remotely human?", "emma_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message("Emma", "It was something like support-security-alert-official-team@totallylegit.ru", "emma_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message(phone_config["phone_player_name"], "Excellent.", "emma_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message(phone_config["phone_player_name"], "That already tells me everything I need to know.", "emma_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message("Emma", "So, I {b}am{/b} hacked?", "emma_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message(phone_config["phone_player_name"], "No.", "emma_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message(phone_config["phone_player_name"], "You are being courted by a phishing attempt.", "emma_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message("Emma", "Phishing, like fish?", "emma_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message(phone_config["phone_player_name"], "Yes.", "emma_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message(phone_config["phone_player_name"], "Except instead of bait, they use panic.", "emma_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message(phone_config["phone_player_name"], "And instead of a hook, they want your password.", "emma_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message("Emma", "It {b}did{/b} say I had to act immediately or lose access forever.", "emma_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message(phone_config["phone_player_name"], "That's classic lure.", "emma_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message(phone_config["phone_player_name"], "Did you click anything?", "emma_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message("Emma", "...", "emma_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message(phone_config["phone_player_name"], "EMMAAAAAAAAAAAA!", "emma_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message("Emma", "I didn't {b}enter{/b} anything!", "emma_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message("Emma", "I just hovered over the link.", "emma_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message(phone_config["phone_player_name"], "Good.", "emma_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message(phone_config["phone_player_name"], "Hovering is safe.", "emma_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message(phone_config["phone_player_name"], "Clicking is how they get you.", "emma_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message("Emma", "So what do I do now?", "emma_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message(phone_config["phone_player_name"], "Step one: Do not reply.", "emma_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message(phone_config["phone_player_name"], "Step two: Do not click anything.", "emma_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message(phone_config["phone_player_name"], "Step three: Report it as phishing.", "emma_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message("Emma", "That's it?", "emma_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message(phone_config["phone_player_name"], "That's it.", "emma_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message(phone_config["phone_player_name"], "Also delete it. With prejudice.", "emma_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message("Emma", "Okay, done.", "emma_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message("Emma", "😓", "emma_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message("Emma", "I really thought I was about to lose everything.", "emma_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message(phone_config["phone_player_name"], "You did the right thing.", "emma_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message(phone_config["phone_player_name"], "You asked before acting.", "emma_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message("Emma", "Guess I'm learning.", "emma_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message(phone_config["phone_player_name"], "Proud of you.", "emma_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message("Emma", "I love you, Mr. Tech Support. 😁", "emma_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message(phone_config["phone_player_name"], "I love you too!", "emma_dm", do_pause=False, log_to_history=False, do_restart=False)

        ## 10 months ago ##
        if emmaroute:
            phone_stamp_rel("emma_dm", back_months=10, do_pause=False)
            send_phone_message("Emma", "[mc]. [mc]. Confirming a phishing attempt.", "emma_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message(phone_config["phone_player_name"], "Good evening, ma'am. [mc]Tech™ Support online.", "emma_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message(phone_config["phone_player_name"], "What tipped you off?", "emma_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message("Emma", "Email claims my mobile account is \"overdue.\"", "emma_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message("Emma", "Uses urgency. Mentions service interruption.", "emma_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message("Emma", "That's pressure tactic. 😤", "emma_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message(phone_config["phone_player_name"], "Sounds suspicious so far.", "emma_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message("Emma", "Sender domain matches the carrier.", "emma_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message("Emma", "Which is exactly what they'd want you to think.", "emma_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message(phone_config["phone_player_name"], "Naturally.", "emma_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message("Emma", "No spelling errors.", "emma_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message("Emma", "Polite but firm tone.", "emma_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message("Emma", "Includes the last four digits of my account.", "emma_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message(phone_config["phone_player_name"], "Em?", "emma_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message("Emma", "Yes?", "emma_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message(phone_config["phone_player_name"], "Did you forget to top up your prepaid plan again?", "emma_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message("Emma", "Irrelevant.", "emma_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message("Emma", "The email includes a PDF attachment.", "emma_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message(phone_config["phone_player_name"], "A bill?", "emma_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message("Emma", "A {b}weaponized{/b} bill.", "emma_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message(phone_config["phone_player_name"], "😩", "emma_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message(phone_config["phone_player_name"], "Em, what exactly does the subject line say?", "emma_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message("Emma", "\"Monthly Statement — Payment Due.\" Why?", "emma_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message(phone_config["phone_player_name"], "And the sender?", "emma_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message("Emma", "Herizon <billing@herizon.com>", "emma_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message(phone_config["phone_player_name"], "And the amount?", "emma_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message("Emma", "$24.80.", "emma_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message(phone_config["phone_player_name"], "EMMAAAAAAAAAAAAA!", "emma_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message(phone_config["phone_player_name"], "That is your phone bill!", "emma_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message("Emma", "...", "emma_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message("Emma", "Really?", "emma_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message(phone_config["phone_player_name"], "Really!", "emma_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message(phone_config["phone_player_name"], "You told me last week you \"definitely pay it later.\"", "emma_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message("Emma", "I was under duress.", "emma_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message(phone_config["phone_player_name"], "By procrastination.", "emma_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message("Emma", "So, it's not phishing.", "emma_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message(phone_config["phone_player_name"], "No.{#1}", "emma_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message("Emma", "Then why does it feel like a threat?", "emma_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message(phone_config["phone_player_name"], "Because capitalism is scarier than scammers.", "emma_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message("Emma", "I already reported it.", "emma_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message(phone_config["phone_player_name"], "To who?", "emma_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message("Emma", "The carrier.", "emma_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message(phone_config["phone_player_name"], "You reported the carrier... to itself?", "emma_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message("Emma", "In my defense, the form was very convincing.", "emma_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message(phone_config["phone_player_name"], "Please pay your bill.", "emma_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message("Emma", "Fine.", "emma_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message(phone_config["phone_player_name"], "Good. Thank you for choosing [mc]Tech™ Support.", "emma_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message(phone_config["phone_player_name"], "And I love you, Emma Meyer.", "emma_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message("Emma", "I love you too, [mc].", "emma_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message("Emma", "I'll see you later at dinner.", "emma_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message(phone_config["phone_player_name"], "It's your favorite for tonight.", "emma_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message("Emma", "😍", "emma_dm", do_pause=False, log_to_history=False, do_restart=False)

        ## 9 months ago ##
        if emmaroute:
            phone_stamp_rel("emma_dm", back_months=9, do_pause=False)
            send_phone_message("Emma", "[mc]. [mc]. I have a situation.", "emma_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message(phone_config["phone_player_name"], "Why's this a monthly thing now...?", "emma_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message(phone_config["phone_player_name"], "Anyway, [mc]Tech Support™, this is [mc] speaking.", "emma_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message(phone_config["phone_player_name"], "Are you calling about billing, hardware, or a life-ruining pop-up?", "emma_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message("Emma", "I have been charged.", "emma_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message("Emma", "For something I did not consciously agree to.", "emma_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message(phone_config["phone_player_name"], "Ah. Accidental subscription.", "emma_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message(phone_config["phone_player_name"], "Let me guess, free trial, seven days, now billed annually?", "emma_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message("Emma", "How did you know?", "emma_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message(phone_config["phone_player_name"], "Experience.", "emma_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message("Emma", "[mc], I want it canceled.", "emma_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message(phone_config["phone_player_name"], "I can guide you through it.", "emma_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message("Emma", "Can't you cancel it yourself?", "emma_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message(phone_config["phone_player_name"], "I cannot access your account.", "emma_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message(phone_config["phone_player_name"], "That would be illegal, unethical, and deeply unattractive.", "emma_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message("Emma", "Okay, fine.", "emma_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message("Emma", "Guide me, please.", "emma_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message(phone_config["phone_player_name"], "Step one: open the app.", "emma_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message("Emma", "It's open.", "emma_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message(phone_config["phone_player_name"], "Step two: tap your profile icon.", "emma_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message("Emma", "Top right?", "emma_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message(phone_config["phone_player_name"], "Yes.", "emma_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message("Emma", "Why is it smiling at me? 🫤", "emma_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message(phone_config["phone_player_name"], "Ignore the mascot. It feeds on hesitation.", "emma_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message("Emma", "I see \"Account.\"", "emma_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message(phone_config["phone_player_name"], "Tap it.", "emma_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message("Emma", "Now it says \"Manage Subscription.\"", "emma_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message(phone_config["phone_player_name"], "This is exactly where they try to scare you.", "emma_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message("Emma", "It says I'll lose access to premium features.", "emma_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message(phone_config["phone_player_name"], "You never used those.", "emma_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message("Emma", "I {b}might have{/b}.", "emma_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message(phone_config["phone_player_name"], "Em? For what?", "emma_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message("Emma", "I downloaded an e-book called \"Talking Normally: A Guide for Professionals Who Don't\".", "emma_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message("Emma", "It was actually good and informative until five pages later, it said \"Warning: Your current tone may intimidate civilians. Unlock better inflections through Premium Plan now.\"", "emma_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message("Emma", "I wanted to finish it, so I pressed the button.", "emma_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message(phone_config["phone_player_name"], "As your tech support, I don't even know what to say...", "emma_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message("Emma", "It's asking me why I'm leaving.", "emma_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message(phone_config["phone_player_name"], "Select \"Too expensive.\"", "emma_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message("Emma", "There's also \"Not what I expected.\"", "emma_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message(phone_config["phone_player_name"], "That one is emotionally honest but less effective.", "emma_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message("Emma", "Selected.", "emma_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message("Emma", "Now it says, \"Are you sure?\"" , "emma_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message(phone_config["phone_player_name"], "They always ask twice.", "emma_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message(phone_config["phone_player_name"], "This is your moment. Be strong.", "emma_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message("Emma", "I interrogate murder suspects for a living.", "emma_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message("Emma", "Confirmed.", "emma_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message("Emma", "It says \"Subscription canceled.\"", "emma_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message(phone_config["phone_player_name"], "That's it. That's what you want.", "emma_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message("Emma", "😥", "emma_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message("Emma", "They almost made me stay with a discount.", "emma_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message(phone_config["phone_player_name"], "Yeah, they always try one last bribe. Like an ex who learned budgeting.", "emma_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message("Emma", "I'll just buy physical copies next time. Thanks, Mr. Tech Support.", "emma_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message("Emma", "I love you. Keep the change. 😘", "emma_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message(phone_config["phone_player_name"], "Payment received:", "emma_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message(phone_config["phone_player_name"], "One successful cancellation.", "emma_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message(phone_config["phone_player_name"], "Zero data breaches.", "emma_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message(phone_config["phone_player_name"], "One \"I love you\".", "emma_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message(phone_config["phone_player_name"], "Receipt emailed. No refunds.", "emma_dm", do_pause=False, log_to_history=False, do_restart=False)

        ## 8 months ago ##
        if emmaroute:
            phone_stamp_rel("emma_dm", back_months=8, do_pause=False)
            send_phone_message("Emma", "[mc]. [mc]. I require technical assistance.", "emma_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message("Emma", "Again. Sorry. 😖", "emma_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message("Emma", "My phone is altering my messages.", "emma_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message(phone_config["phone_player_name"], "Altering how?", "emma_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message(phone_config["phone_player_name"], "Like typos, or...", "emma_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message("Emma", "Sabotage.", "emma_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message("Emma", "I typed: \"The suspect is cooperative.\"", "emma_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message("Emma", "It sent: \"The suspect is adorable.\"", "emma_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message(phone_config["phone_player_name"], "Oh. My. Goodness!", "emma_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message(phone_config["phone_player_name"], "Please tell me that wasn't to the suspect.", "emma_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message("Emma", "It was to my supervisor.", "emma_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message("Emma", "This compromises my credibility.", "emma_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message(phone_config["phone_player_name"], "Okay. Deep breath.", "emma_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message(phone_config["phone_player_name"], "That's autocorrect.", "emma_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message("Emma", "But I did not authorize correction.", "emma_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message(phone_config["phone_player_name"], "Yeah, it does that anyway.", "emma_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message(phone_config["phone_player_name"], "It guesses what you're trying to say.", "emma_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message("Emma", "It guessed wrong.", "emma_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message("Emma", "And confidently!", "emma_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message(phone_config["phone_player_name"], "You can turn it off.", "emma_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message("Emma", "Really?", "emma_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message("Emma", "Can you guide me through it?", "emma_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message(phone_config["phone_player_name"], "Settings.", "emma_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message(phone_config["phone_player_name"], "Keyboard.", "emma_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message(phone_config["phone_player_name"], "Then toggle off autocorrect.", "emma_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message("Emma", "Done.", "emma_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message("Emma", "If I make a mistake now, it will be my mistake.", "emma_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message("Emma", "I can accept that, at least. 😑", "emma_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message(phone_config["phone_player_name"], "Glad I could help.", "emma_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message(phone_config["phone_player_name"], "Anything else while you've got me?", "emma_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message("Emma", "Yeah.{#1}", "emma_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message("Emma", "Why did it replace \"suspect\" with \"sweetheart\" earlier.", "emma_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message(phone_config["phone_player_name"], "... That one might be on you.", "emma_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message("Emma", "Unacceptable.", "emma_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message("Emma", "Thank you for your assistance.", "emma_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message(phone_config["phone_player_name"], "Anytime!", "emma_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message("Emma", "If this happens again, I will switch to handwritten notes.", "emma_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message("Emma", "Technology has been warned! 😠", "emma_dm", do_pause=False, log_to_history=False, do_restart=False)

            phone_stamp_rel("emma_dm", back_months=8, do_pause=False)
            send_phone_message("Emma", "[mc]. [mc]. The problem has evolved! 😨", "emma_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message(phone_config["phone_player_name"], "Oh no.", "emma_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message(phone_config["phone_player_name"], "What did autocorrect do this time?", "emma_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message("Emma", "It's learning my vocabulary.", "emma_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message("Emma", "It's now attempting to speak like me.", "emma_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message(phone_config["phone_player_name"], "... That's literally what it does.", "emma_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message(phone_config["phone_player_name"], "But I'm scared to ask.", "emma_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message("Emma", "I typed: \"Good morning.\".", "emma_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message("Emma", "It suggested: \"State your purpose.\".", "emma_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message(phone_config["phone_player_name"], "PLEASE tell me you didn't send that.", "emma_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message("Emma", "I didn't send it accidentally.", "emma_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message("Emma", "I was conducting a controlled test.", "emma_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message(phone_config["phone_player_name"], "Of what? Do I dare to ask...?", "emma_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message("Emma", "Autocorrect behavior.", "emma_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message("Emma", "I selected a low-risk civilian.", "emma_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message("Emma", "The barista.", "emma_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message("Emma", "She stared at me for three seconds.", "emma_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message("Emma", "Then she gave me the coffee without speaking.", "emma_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message(phone_config["phone_player_name"], "Em? I'm getting concered now...", "emma_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message(phone_config["phone_player_name"], "You don't test software on people.", "emma_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message("Emma", "I disagree.", "emma_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message("Emma", "People are unpredictable.", "emma_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message("Emma", "Software should not be.", "emma_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message(phone_config["phone_player_name"], "You scared her into compliance.", "emma_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message("Emma", "It also attempted to replace \"thank you\" with \"cooperation noted.\".", "emma_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message(phone_config["phone_player_name"], "Okay, yeah, it's turning into Detective Autocorrect.", "emma_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message(phone_config["phone_player_name"], "We need to turn off the learning feature.", "emma_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message("Emma", "Walk me throught it. I promise this will be the last time. 😭", "emma_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message(phone_config["phone_player_name"], "Open Settings.", "emma_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message(phone_config["phone_player_name"], "Then go to Keyboard.", "emma_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message(phone_config["phone_player_name"], "Look for something like \"Predictive\" or \"Learn from typing.\"", "emma_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message("Emma", "I see \"Predictive Text.\"", "emma_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message(phone_config["phone_player_name"], "Turn it off.", "emma_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message("Emma", "It's resisting.", "emma_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message(phone_config["phone_player_name"], "Emma.", "emma_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message(phone_config["phone_player_name"], "It's a switch.", "emma_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message("Emma", "I turned it off.", "emma_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message("Emma", "It turned itself back on!", "emma_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message(phone_config["phone_player_name"], "... Okay, now I'm scared.", "emma_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message(phone_config["phone_player_name"], "Try again. And don't leave the screen until it stays off.", "emma_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message("Emma", "Off.", "emma_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message("Emma", "It's staying off.", "emma_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message(phone_config["phone_player_name"], "Good.", "emma_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message(phone_config["phone_player_name"], "Now, clear the learned suggestions.", "emma_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message(phone_config["phone_player_name"], "There should be an option like \"Reset Keyboard Dictionary\" or \"Clear personalized data.\"", "emma_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message("Emma", "Found it.", "emma_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message("Emma", "It says it will remove words I've taught it.", "emma_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message(phone_config["phone_player_name"], "Yep. Wipe its brain.", "emma_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message("Emma", "You're recommending memory deletion?", "emma_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message(phone_config["phone_player_name"], "I'm recommending you stop your keyboard from issuing warrants!", "emma_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message("Emma", "Okay, okay. Done!", "emma_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message(phone_config["phone_player_name"], "Test it.", "emma_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message(phone_config["phone_player_name"], "Type: \"Good morning.\"", "emma_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message("Emma", "Good morning.", "emma_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message("Emma", "It didn't accuse anyone.", "emma_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message(phone_config["phone_player_name"], "Huge progress.", "emma_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message("Emma", "Thank you.", "emma_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message("Emma", "Cooperation noted.", "emma_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message(phone_config["phone_player_name"], "EMMAAAAAAAAAAAAAA!", "emma_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message("Emma", "Habit.", "emma_dm", do_pause=False, log_to_history=False, do_restart=False)

        ## 7 months ago ##
        phone_stamp_rel("emma_dm", back_months=7, do_pause=False)
        send_phone_message("Emma", "[mc]. [mc]. I may need your help.", "emma_dm", do_pause=False, log_to_history=False, do_restart=False)
        send_phone_message(phone_config["phone_player_name"], "Tech?", "emma_dm", do_pause=False, log_to_history=False, do_restart=False)
        send_phone_message("Emma", "Not this time, no.", "emma_dm", do_pause=False, log_to_history=False, do_restart=False)
        send_phone_message("Emma", "New case.", "emma_dm", do_pause=False, log_to_history=False, do_restart=False)
        send_phone_message("Emma", "Multiple shell accounts. Clean paperwork with no obvious leaks.", "emma_dm", do_pause=False, log_to_history=False, do_restart=False)
        send_phone_message(phone_config["phone_player_name"], "Hm, nobody's that clean unless they're hiding something.", "emma_dm", do_pause=False, log_to_history=False, do_restart=False)
        send_phone_message("Emma", "Exactly.", "emma_dm", do_pause=False, log_to_history=False, do_restart=False)
        send_phone_message("Emma", "I don't like it.", "emma_dm", do_pause=False, log_to_history=False, do_restart=False)
        send_phone_message(phone_config["phone_player_name"], "Alright. Walk me through what you've tried.", "emma_dm", do_pause=False, log_to_history=False, do_restart=False)
        send_phone_message("Emma", "Cross-referenced vendors.", "emma_dm", do_pause=False, log_to_history=False, do_restart=False)
        send_phone_message("Emma", "Pulled financial trails.", "emma_dm", do_pause=False, log_to_history=False, do_restart=False)
        send_phone_message("Emma", "Interrogated two people.", "emma_dm", do_pause=False, log_to_history=False, do_restart=False)
        send_phone_message("Emma", "They both cried. 😒", "emma_dm", do_pause=False, log_to_history=False, do_restart=False)
        send_phone_message(phone_config["phone_player_name"], "Did it help?", "emma_dm", do_pause=False, log_to_history=False, do_restart=False)
        send_phone_message("Emma", "No.", "emma_dm", do_pause=False, log_to_history=False, do_restart=False)
        send_phone_message("Emma", "But I now know one of them is lactose intolerant.", "emma_dm", do_pause=False, log_to_history=False, do_restart=False)
        send_phone_message(phone_config["phone_player_name"], "Any progress?", "emma_dm", do_pause=False, log_to_history=False, do_restart=False)
        send_phone_message("Emma", "Marginal at best.", "emma_dm", do_pause=False, log_to_history=False, do_restart=False)
        send_phone_message(phone_config["phone_player_name"], "Okay. If it's that airtight, you might be dealing with professional laundering.", "emma_dm", do_pause=False, log_to_history=False, do_restart=False)
        send_phone_message("Emma", "That was my conclusion.", "emma_dm", do_pause=False, log_to_history=False, do_restart=False)
        send_phone_message(phone_config["phone_player_name"], "Look... this might be bigger than what you can legally poke at alone.", "emma_dm", do_pause=False, log_to_history=False, do_restart=False)
        send_phone_message(phone_config["phone_player_name"], "You could bring in outside analysts.", "emma_dm", do_pause=False, log_to_history=False, do_restart=False)
        send_phone_message("Emma", "Are you suggesting your agency?", "emma_dm", do_pause=False, log_to_history=False, do_restart=False)
        send_phone_message(phone_config["phone_player_name"], "As a last resort, of course.", "emma_dm", do_pause=False, log_to_history=False, do_restart=False)
        send_phone_message(phone_config["phone_player_name"], "Sicae can audit quietly. No flags. No noise. No whatsoever.", "emma_dm", do_pause=False, log_to_history=False, do_restart=False)
        send_phone_message("Emma", "I don't like relying on them professionally.", "emma_dm", do_pause=False, log_to_history=False, do_restart=False)
        send_phone_message("Emma", "I know how they operate. Sicae can complicate things more than they should.", "emma_dm", do_pause=False, log_to_history=False, do_restart=False)
        send_phone_message(phone_config["phone_player_name"], "But you called me anyway.", "emma_dm", do_pause=False, log_to_history=False, do_restart=False)
        send_phone_message("Emma", "Yeah.", "emma_dm", do_pause=False, log_to_history=False, do_restart=False)
        send_phone_message("Emma", "Because I trust you.", "emma_dm", do_pause=False, log_to_history=False, do_restart=False)
        send_phone_message(phone_config["phone_player_name"], "So... Sicae?", "emma_dm", do_pause=False, log_to_history=False, do_restart=False)
        send_phone_message("Emma", "I'll think about it.", "emma_dm", do_pause=False, log_to_history=False, do_restart=False)
        send_phone_message("Emma", "Can we talk in person after your shift?", "emma_dm", do_pause=False, log_to_history=False, do_restart=False)
        send_phone_message("Emma", "I don't like having work conversations through a screen.", "emma_dm", do_pause=False, log_to_history=False, do_restart=False)
        send_phone_message(phone_config["phone_player_name"], "Yeah. That works.", "emma_dm", do_pause=False, log_to_history=False, do_restart=False)
        if emmaroute:
            send_phone_message(phone_config["phone_player_name"], "The park?", "emma_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message(phone_config["phone_player_name"], "You still remember it.", "emma_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message("Emma", "😁", "emma_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message("Emma", "You don't have to tug at my heartstrings.", "emma_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message("Emma", "But, fine.", "emma_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message("Emma", "Let's meet there.", "emma_dm", do_pause=False, log_to_history=False, do_restart=False)

        if emmaroute:
            phone_stamp_rel("emma_dm", back_months=7, do_pause=False)
            send_phone_message("Emma", "I need to address something.", "emma_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message(phone_config["phone_player_name"], "That sounds ominous.", "emma_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message(phone_config["phone_player_name"], "Did I commit a crime?", "emma_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message("Emma", "Not a felony.", "emma_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message("Emma", "But don't get comfortable.", "emma_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message(phone_config["phone_player_name"], "😰", "emma_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message("Emma", "You told Aine I'm working a complicated case.", "emma_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message(phone_config["phone_player_name"], "I didn't tell her anything.", "emma_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message(phone_config["phone_player_name"], "That's like... the opposite of details.", "emma_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message("Emma", "It is still information.", "emma_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message("Emma", "Also it made her ask questions.", "emma_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message("Emma", "Which made me tired.", "emma_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message(phone_config["phone_player_name"], "She asked {b}you{/b} questions?", "emma_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message("Emma", "Yes!", "emma_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message("Emma", "She was very polite!", "emma_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message("Emma", "Which somehow makes it harder to escape!", "emma_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message(phone_config["phone_player_name"], "I'm sorry, detective.", "emma_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message(phone_config["phone_player_name"], "I was just explaining why I've been MIA.", "emma_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message("Emma", "I know.", "emma_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message("Emma", "And I appreciate it.", "emma_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message("Emma", "I just prefer when your explanations don't include me.", "emma_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message(phone_config["phone_player_name"], "... Are you jealous of Aine?", "emma_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message("Emma", "No.", "emma_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message("Emma", "I'm just protective of my case.", "emma_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message("Emma", "And protective of you.", "emma_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message("Emma", "And slightly annoyed that you are adorable when you play dumb.", "emma_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message(phone_config["phone_player_name"], "Aww. So you {b}are{/b} jealous.", "emma_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message("Emma", "Wrong!", "emma_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message("Emma", "Don't try to win this with flirting. 😑", "emma_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message(phone_config["phone_player_name"], "It's my personality.", "emma_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message("Emma", "Your personality is a security risk, [mc]!", "emma_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message(phone_config["phone_player_name"], "So what do you want me to say next time?", "emma_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message("Emma", "Say: \"work.\"", "emma_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message("Emma", "Say: \"Emma is busy.\".", "emma_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message("Emma", "Do not say: \"complicated case.\"", "emma_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message(phone_config["phone_player_name"], "Got it. Just \"work.\"", "emma_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message(phone_config["phone_player_name"], "You're really cute when you're bossy, you know that?", "emma_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message("Emma", "I am not cute.", "emma_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message("Emma", "I am exhausted.", "emma_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message("Emma", "And I miss you! 😡", "emma_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message("Emma", "But don't let that distract you.", "emma_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message("Emma", "This is still a reprimand.", "emma_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message(phone_config["phone_player_name"], "Yes, ma'am! I receive the reprimand.", "emma_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message("Emma", "Good. Now bring coffee.", "emma_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message(phone_config["phone_player_name"], "But you don't want anyone coming into your office.", "emma_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message("Emma", "I make exceptions, of course.", "emma_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message("Emma", "For you.", "emma_dm", do_pause=False, log_to_history=False, do_restart=False)

        ## 6 months ago ##
        if emmaroute:
            send_phone_message(phone_config["phone_player_name"], "The month's almost over. No tech emergencies this time?", "emma_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message(phone_config["phone_player_name"], "Did the world finally stop breaking?", "emma_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message("Emma", "I adapted.", "emma_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message("Emma", "And I've been busy.", "emma_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message(phone_config["phone_player_name"], "You're always busy. 😔", "emma_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message("Emma", "So are you.", "emma_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message("Emma", "I've been focusing on Francis.", "emma_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message("Emma", "I'm not taking any other cases right now.", "emma_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message(phone_config["phone_player_name"], "Your boss can't be thrilled about that.", "emma_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message("Emma", "He isn't.", "emma_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message("Emma", "But I made him a deal.", "emma_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message("Emma", "If I close more cases than I did last year, I get the rest of this year to work however I want.", "emma_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message(phone_config["phone_player_name"], "So that's why you leaned on Sicae.", "emma_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message(phone_config["phone_player_name"], "One last push. Leave an impression.", "emma_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message("Emma", "If I have to bend my principles to see this through, then I will.", "emma_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message("Emma", "You want him found too, don't you?", "emma_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message("Emma", "Because I do.", "emma_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message("Emma", "I want justice for what he did to you.", "emma_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message(phone_config["phone_player_name"], "I want him found.", "emma_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message(phone_config["phone_player_name"], "But I don't want you hollowing yourself out to do it.", "emma_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message(phone_config["phone_player_name"], "Use Sicae if it gives you leverage.", "emma_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message(phone_config["phone_player_name"], "Just don't confuse pressure with progress.", "emma_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message(phone_config["phone_player_name"], "I'm not asking you to be reckless for me.", "emma_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message(phone_config["phone_player_name"], "I simply want you to come back intact.", "emma_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message("Emma", "We'll see once I get there.", "emma_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message(phone_config["phone_player_name"], "Come on, Em...", "emma_dm", do_pause=False, log_to_history=False, do_restart=False)

        ## 5 months ago ##
        if emmaroute:
            phone_stamp_rel("emma_dm", back_months=5, do_pause=False)
            send_phone_message(phone_config["phone_player_name"], "Em, we're starting dinner.", "emma_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message(phone_config["phone_player_name"], "Left a plate in the fridge. Top shelf.", "emma_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message("Emma", "You didn't have to.", "emma_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message("Emma", "But thanks.", "emma_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message(phone_config["phone_player_name"], "I wanted to.", "emma_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message("Emma", "I'll eat it when I get home. 🙏", "emma_dm", do_pause=False, log_to_history=False, do_restart=False)

        ## 4 months ago ##
        if emmaroute:
            phone_stamp_rel("emma_dm", back_months=4, do_pause=False)
            send_phone_message("Emma", "[mc]. [mc]. I might be late again.", "emma_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message(phone_config["phone_player_name"], "That's okay.", "emma_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message(phone_config["phone_player_name"], "Do you want me to stay up?", "emma_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message("Emma", "No.{#2}", "emma_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message("Emma", "But leave the porch light on for me. 🙏", "emma_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message(phone_config["phone_player_name"], "Always.", "emma_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message("Emma", "Love you! 😘", "emma_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message(phone_config["phone_player_name"], "Love you too, Em. 💦", "emma_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message("Emma", "Why that emoji??", "emma_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message(phone_config["phone_player_name"], "I miss you. It's been a while, you know?", "emma_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message("Emma", "Mm, [mc]. 🫦", "emma_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message("Emma", "Nevermind, I'm coming home early.", "emma_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message(phone_config["phone_player_name"], "Yes! 😍", "emma_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message("Emma", "No taking photos!", "emma_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message(phone_config["phone_player_name"], "Yes, ma'am!", "emma_dm", do_pause=False, log_to_history=False, do_restart=False)

        ## 3 months ago ##
        if emmaroute:
            phone_stamp_rel("emma_dm", back_months=3, do_pause=False)
            send_phone_message(phone_config["phone_player_name"], "You skipped lunch again, didn't you?", "emma_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message("Emma", "I had coffee.", "emma_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message(phone_config["phone_player_name"], "Yeah... I'm not exactly innocent either.", "emma_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message(phone_config["phone_player_name"], "So I won't lecture you. Just... try not to make it a habit?", "emma_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message("Emma", "I know.", "emma_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message("Emma", "Oh. By the way.", "emma_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message("Emma", "I found a store in the mall that still sells the stuffed toys I used to have.", "emma_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message(phone_config["phone_player_name"], "Seriously? They still make those?", "emma_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message("Emma", "Apparently.", "emma_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message(phone_config["phone_player_name"], "Do you want one?", "emma_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message(phone_config["phone_player_name"], "Say the word. I'll grab it for you.", "emma_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message("Emma", "I'm too old for toys, [mc].", "emma_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message("Emma", "And some memories are better left where they belong.", "emma_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message("Emma", "Still... it was nice seeing them again. 😊", "emma_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message(phone_config["phone_player_name"], "Alright.", "emma_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message(phone_config["phone_player_name"], "But if you change your mind, you know I'm already halfway there.", "emma_dm", do_pause=False, log_to_history=False, do_restart=False)

        ## 2 months ago ##
        ## 1 months ago ##

        ## Present ##
        phone_stamp_rel("emma_dm", back_days=8, do_pause=False)
        send_phone_message("Emma", "[mc]. [mc].", "emma_dm", do_pause=False, log_to_history=False, do_restart=False)
        send_phone_message("Emma", "I've been thinking about getting a car lately.", "emma_dm", do_pause=False, log_to_history=False, do_restart=False)
        send_phone_message(phone_config["phone_player_name"], "That's... a pretty big thought to just drop like that.", "emma_dm", do_pause=False, log_to_history=False, do_restart=False)
        send_phone_message("Emma", "It's not too sudden, is it?", "emma_dm", do_pause=False, log_to_history=False, do_restart=False)
        send_phone_message("Emma", "I'm just tired of either borrowing your truck, or using the company car.", "emma_dm", do_pause=False, log_to_history=False, do_restart=False)
        send_phone_message(phone_config["phone_player_name"], "No need to justify. I'm actually proud of you.", "emma_dm", do_pause=False, log_to_history=False, do_restart=False)
        send_phone_message("Emma", "I just want something reliable.", "emma_dm", do_pause=False, log_to_history=False, do_restart=False)
        send_phone_message("Emma", "Quiet.", "emma_dm", do_pause=False, log_to_history=False, do_restart=False)
        send_phone_message("Emma", "And difficult to break.", "emma_dm", do_pause=False, log_to_history=False, do_restart=False)
        send_phone_message(phone_config["phone_player_name"], "So... basically you.", "emma_dm", do_pause=False, log_to_history=False, do_restart=False)
        send_phone_message("Emma", "😦", "emma_dm", do_pause=False, log_to_history=False, do_restart=False)
        send_phone_message("Emma", "Inaccurate comparison!", "emma_dm", do_pause=False, log_to_history=False, do_restart=False)
        send_phone_message("Emma", "But acceptable.", "emma_dm", do_pause=False, log_to_history=False, do_restart=False)
        send_phone_message(phone_config["phone_player_name"], "Want me to come with you when you look?", "emma_dm", do_pause=False, log_to_history=False, do_restart=False)
        send_phone_message("Emma", "Please.", "emma_dm", do_pause=False, log_to_history=False, do_restart=False)
        send_phone_message(phone_config["phone_player_name"], "I got you. Just say when.", "emma_dm", do_pause=False, log_to_history=False, do_restart=False)






        ##### FREYA #####
        ## 13 months ago ##
        phone_stamp_rel("freya_dm", back_months=13, do_pause=False)
        send_phone_message("Freya", "hey did youeat or were you runningon vibes agian", "freya_dm", do_pause=False, log_to_history=False, do_restart=False)
        send_phone_message(phone_config["phone_player_name"], "Coffee is a food group.", "freya_dm", do_pause=False, log_to_history=False, do_restart=False)
        send_phone_message("Freya", "yuo worry meanyway im stealing your hoodie tomorroww this is not a requets", "freya_dm", do_pause=False, log_to_history=False, do_restart=False)
        send_phone_message(phone_config["phone_player_name"], "WTF?", "freya_dm", do_pause=False, log_to_history=False, do_restart=False)
        send_phone_message(phone_config["phone_player_name"], "I don't know if you stole Gwen's potion called alcohol, because you sound like a drunk sissy.", "freya_dm", do_pause=False, log_to_history=False, do_restart=False)
        send_phone_message(phone_config["phone_player_name"], "I don't even have a hoodie.", "freya_dm", do_pause=False, log_to_history=False, do_restart=False)
        send_phone_message("Freya", "IM NOT drnuk ok??im typignPERFECTLY", "freya_dm", do_pause=False, log_to_history=False, do_restart=False)
        send_phone_message(phone_config["phone_player_name"], "Freya.", "freya_dm", do_pause=False, log_to_history=False, do_restart=False)
        send_phone_message(phone_config["phone_player_name"], "Hit the space bar.", "freya_dm", do_pause=False, log_to_history=False, do_restart=False)
        send_phone_message(phone_config["phone_player_name"], "It's free. You can use it.", "freya_dm", do_pause=False, log_to_history=False, do_restart=False)
        send_phone_message("Freya", "DONTtellMEhowTOlivMYIFE", "freya_dm", do_pause=False, log_to_history=False, do_restart=False)
        send_phone_message(phone_config["phone_player_name"], "THE SPACE BAR, GODDAMNIT!", "freya_dm", do_pause=False, log_to_history=False, do_restart=False)
        if freyaroute:
            send_phone_message("Freya", "im honry", "freya_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message(phone_config["phone_player_name"], "Hi, honry.", "freya_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message(phone_config["phone_player_name"], "Should I call the spelling police?", "freya_dm", do_pause=False, log_to_history=False, do_restart=False)
        
        phone_stamp_rel("freya_dm", back_months=13, do_pause=False)
        send_phone_message("Freya", "😨😱😨", "freya_dm", do_pause=False, log_to_history=False, do_restart=False)
        send_phone_message("Freya", "wtf did i text u last night", "freya_dm", do_pause=False, log_to_history=False, do_restart=False)
        send_phone_message(phone_config["phone_player_name"], "How would {b}I{/b} know?", "freya_dm", do_pause=False, log_to_history=False, do_restart=False)
        send_phone_message(phone_config["phone_player_name"], "You typed like your thumbs were fighting for custody.", "freya_dm", do_pause=False, log_to_history=False, do_restart=False)
        if (freyaroute and freyapoint == 10):
            send_phone_message(phone_config["phone_player_name"], "Wait. Did you...", "freya_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message("Freya", "I DID NOT!!", "freya_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message(phone_config["phone_player_name"], "Hm...", "freya_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message(phone_config["phone_player_name"], "Interesting reaction. I didn't even finish the sentence.", "freya_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message(phone_config["phone_player_name"], "Feels like someone's guilty. Don't worry, Frey. You're secret's safe with me.", "freya_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message("Freya", "SHUT UP SHUT UP SHUT UP!!! DON'T TALK TO ME AGAIN!", "freya_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message("Freya", "😡😡😡😡😡😡😡", "freya_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message(phone_config["phone_player_name"], "You sure put more effort into your punctuations when you're pissed. Nice!", "freya_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message("Freya", "AAAAAAAAAAAAAAAAA!!!", "freya_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message(phone_config["phone_player_name"], "Want me to come over tonight?", "freya_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message("Freya", "...", "freya_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message("Freya", "please? 😍😍😍", "freya_dm", do_pause=False, log_to_history=False, do_restart=False)

        phone_stamp_rel("freya_dm", back_months=13, do_pause=False)
        send_phone_message("Freya", "images/ch2ep1_1037.jpg", "freya_dm", 2, do_pause=False, log_to_history=False, do_restart=False)
        send_phone_message(phone_config["phone_player_name"], "Damn, my queen of blowjobs...", "freya_dm", do_pause=False, log_to_history=False, do_restart=False)
        send_phone_message(phone_config["phone_player_name"], "You looked so good with me in your mouth, Frey.", "freya_dm", do_pause=False, log_to_history=False, do_restart=False)
        send_phone_message(phone_config["phone_player_name"], "But that face paint looks so much better on you. 😉", "freya_dm", do_pause=False, log_to_history=False, do_restart=False)
        send_phone_message("Freya", "dont remind me or im dragging u here rn", "freya_dm", do_pause=False, log_to_history=False, do_restart=False)
        send_phone_message(phone_config["phone_player_name"], "Promise?", "freya_dm", do_pause=False, log_to_history=False, do_restart=False)

        phone_stamp_rel("freya_dm", back_months=13, do_pause=False)
        send_phone_message(phone_config["phone_player_name"], "How long does it take to withdraw a salary, Frey?", "freya_dm", do_pause=False, log_to_history=False, do_restart=False)
        send_phone_message(phone_config["phone_player_name"], "Did the ATM ask you for a full character backstory or what?", "freya_dm", do_pause=False, log_to_history=False, do_restart=False)
        send_phone_message("Freya", "😑😑😑", "freya_dm", do_pause=False, log_to_history=False, do_restart=False)
        send_phone_message("Freya", "shut UP its calculating my financial trauma", "freya_dm", do_pause=False, log_to_history=False, do_restart=False)
        send_phone_message(phone_config["phone_player_name"], "Tell it to hurry. I'm growing roots here.", "freya_dm", do_pause=False, log_to_history=False, do_restart=False)
        send_phone_message("Freya", "daddy chill im on my way", "freya_dm", do_pause=False, log_to_history=False, do_restart=False)

        ## 12 months ago ##
        phone_stamp_rel("freya_dm", back_months=12, do_pause=False)
        send_phone_message("Freya", "ok serious question how many near death experiences does one guy need??", "freya_dm", do_pause=False, log_to_history=False, do_restart=False)
        send_phone_message(phone_config["phone_player_name"], "I'm collecting them. Like stamps.", "freya_dm", do_pause=False, log_to_history=False, do_restart=False)
        send_phone_message("Freya", "maybe trade them in for therapy instead???", "freya_dm", do_pause=False, log_to_history=False, do_restart=False)
        send_phone_message(phone_config["phone_player_name"], "Sounds expensive.", "freya_dm", do_pause=False, log_to_history=False, do_restart=False)
        send_phone_message("Freya", "so is DYING, [mc]", "freya_dm", do_pause=False, log_to_history=False, do_restart=False)
        send_phone_message(phone_config["phone_player_name"], "HEY! that was the road-rager's fault. Not mine.", "freya_dm", do_pause=False, log_to_history=False, do_restart=False)

        ## 11 months ago ##
        phone_stamp_rel("freya_dm", back_months=11, do_pause=False)
        send_phone_message("Freya", "u were quiet", "freya_dm", do_pause=False, log_to_history=False, do_restart=False)
        send_phone_message("Freya", "something wrong", "freya_dm", do_pause=False, log_to_history=False, do_restart=False)
        send_phone_message(phone_config["phone_player_name"], "Is that supposed to be a question or a statement?", "freya_dm", do_pause=False, log_to_history=False, do_restart=False)
        send_phone_message("Freya", "*?", "freya_dm", do_pause=False, log_to_history=False, do_restart=False)
        send_phone_message(phone_config["phone_player_name"], "...", "freya_dm", do_pause=False, log_to_history=False, do_restart=False)
        send_phone_message(phone_config["phone_player_name"], "I'm fine. Just thinking.", "freya_dm", do_pause=False, log_to_history=False, do_restart=False)
        send_phone_message(phone_config["phone_player_name"], "You stremaing?", "freya_dm", do_pause=False, log_to_history=False, do_restart=False)
        send_phone_message(phone_config["phone_player_name"], "*streaming", "freya_dm", do_pause=False, log_to_history=False, do_restart=False)
        send_phone_message("Freya", "pfft 😄", "freya_dm", do_pause=False, log_to_history=False, do_restart=False)
        send_phone_message("Freya", "yeah in a bit", "freya_dm", do_pause=False, log_to_history=False, do_restart=False)
        send_phone_message(phone_config["phone_player_name"], "Tuning in.", "freya_dm", do_pause=False, log_to_history=False, do_restart=False)

        phone_stamp_rel("freya_dm", back_months=11, do_pause=False)
        send_phone_message("Freya", "well shit happy birthday ur officially ancient now", "freya_dm", do_pause=False, log_to_history=False, do_restart=False)
        send_phone_message(phone_config["phone_player_name"], "Thank you. I think?", "freya_dm", do_pause=False, log_to_history=False, do_restart=False)
        send_phone_message("Freya", "dont get sappy im only doing this once a year", "freya_dm", do_pause=False, log_to_history=False, do_restart=False)
        send_phone_message("Freya", "one (1) greeting limited edition cherish it", "freya_dm", do_pause=False, log_to_history=False, do_restart=False)
        send_phone_message(phone_config["phone_player_name"], "You remembered. I'm surprised.", "freya_dm", do_pause=False, log_to_history=False, do_restart=False)
        send_phone_message("Freya", "EXCUSE ME i have a functioning brain", "freya_dm", do_pause=False, log_to_history=False, do_restart=False)
        send_phone_message("Freya", "mostly", "freya_dm", do_pause=False, log_to_history=False, do_restart=False)
        send_phone_message(phone_config["phone_player_name"], "This actually means a lot. Thanks, Frey.", "freya_dm", do_pause=False, log_to_history=False, do_restart=False)
        send_phone_message("Freya", "STOP", "freya_dm", do_pause=False, log_to_history=False, do_restart=False)
        send_phone_message("Freya", "dont make it emotional im allergic", "freya_dm", do_pause=False, log_to_history=False, do_restart=False)
        send_phone_message("Freya", "...", "freya_dm", do_pause=False, log_to_history=False, do_restart=False)
        send_phone_message("Freya", "happy birthday [mc]", "freya_dm", do_pause=False, log_to_history=False, do_restart=False)
        send_phone_message("Freya", "😚", "freya_dm", do_pause=False, log_to_history=False, do_restart=False)

        phone_stamp_rel("freya_dm", back_months=11, do_pause=False)
        send_phone_message("Freya", "i just saw someone who walks exactly like you", "freya_dm", do_pause=False, log_to_history=False, do_restart=False)
        send_phone_message("Freya", "same \"i hate being perceived\" energy", "freya_dm", do_pause=False, log_to_history=False, do_restart=False)
        send_phone_message(phone_config["phone_player_name"], "Maybe it was me?", "freya_dm", do_pause=False, log_to_history=False, do_restart=False)
        send_phone_message("Freya", "no this one looked like they slept", "freya_dm", do_pause=False, log_to_history=False, do_restart=False)
        send_phone_message("Freya", "so definitely not you", "freya_dm", do_pause=False, log_to_history=False, do_restart=False)
        send_phone_message(phone_config["phone_player_name"], "And where exactly are you going with this conversation, Freya?", "freya_dm", do_pause=False, log_to_history=False, do_restart=False)
        if freyaroute:
            send_phone_message("Freya", "to my heart obviously", "freya_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message(phone_config["phone_player_name"], "You've... never actually said you loved me, you know.", "freya_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message("Freya", "EW WHY WOULD YOU SAY IT LIKE THAT", "freya_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message("Freya", "my spine just folded in half", "freya_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message("Freya", "gross emotional man", "freya_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message(phone_config["phone_player_name"], "You brought it up.", "freya_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message("Freya", "im gonna throw up brb", "freya_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message("Freya", "...", "freya_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message("Freya", "fine", "freya_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message("Freya", "i love you ok 😘", "freya_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message("Freya", "if u tell ANYONE i said that i will bite you", "freya_dm", do_pause=False, log_to_history=False, do_restart=False)

        ## 10 months ago ##
        phone_stamp_rel("freya_dm", back_months=10, do_pause=False)
        send_phone_message("Freya", "they moved you to night shift again?", "freya_dm", do_pause=False, log_to_history=False, do_restart=False)
        send_phone_message(phone_config["phone_player_name"], "Yeah.", "freya_dm", do_pause=False, log_to_history=False, do_restart=False)
        send_phone_message("Freya", "AAAAAAAAAAA!!! 🤬", "freya_dm", do_pause=False, log_to_history=False, do_restart=False)
        send_phone_message(phone_config["phone_player_name"], "Relax. It won't last.", "freya_dm", do_pause=False, log_to_history=False, do_restart=False)
        send_phone_message(phone_config["phone_player_name"], "Night shifts burn more electricity and bring in fewer customers. Not exactly cost-efficient.", "freya_dm", do_pause=False, log_to_history=False, do_restart=False)
        send_phone_message("Freya", "sooo basically corporate math is gonna save u?", "freya_dm", do_pause=False, log_to_history=False, do_restart=False)
        send_phone_message(phone_config["phone_player_name"], "Pretty much.", "freya_dm", do_pause=False, log_to_history=False, do_restart=False)
        send_phone_message("Freya", "god bless capitalism i guess", "freya_dm", do_pause=False, log_to_history=False, do_restart=False)

        phone_stamp_rel("freya_dm", back_months=10, do_pause=False)
        send_phone_message("Freya", "i swear u have old man energy sometimes", "freya_dm", do_pause=False, log_to_history=False, do_restart=False)
        send_phone_message(phone_config["phone_player_name"], "Why?", "freya_dm", do_pause=False, log_to_history=False, do_restart=False)
        send_phone_message("Freya", "u make that tiny sigh before sitting down", "freya_dm", do_pause=False, log_to_history=False, do_restart=False)
        send_phone_message("Freya", "thats when the soul leaves the body", "freya_dm", do_pause=False, log_to_history=False, do_restart=False)
        send_phone_message(phone_config["phone_player_name"], "I only sigh around you.", "freya_dm", do_pause=False, log_to_history=False, do_restart=False)
        send_phone_message("Freya", "SEE???? elderly", "freya_dm", do_pause=False, log_to_history=False, do_restart=False)
        send_phone_message("Freya", "😤", "freya_dm", do_pause=False, log_to_history=False, do_restart=False)

        ## 9 months ago ##
        if freyaroute:
            phone_stamp_rel("freya_dm", back_months=9, do_pause=False)
            send_phone_message("Freya", "jeez i hate it when they move your schedules like this", "freya_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message("Freya", "when are u coming back to work", "freya_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message(phone_config["phone_player_name"], "My shift ended an hour ago.", "freya_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message("Freya", "yea but like", "freya_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message("Freya", "come back", "freya_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message("Freya", "the store is too quiet without u", "freya_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message(phone_config["phone_player_name"], "You miss me?", "freya_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message("Freya", "dont get cocky or ill change my answer", "freya_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message("Freya", "😍", "freya_dm", do_pause=False, log_to_history=False, do_restart=False)

        ## 8 months ago ##
        phone_stamp_rel("freya_dm", back_months=8, do_pause=False)
        send_phone_message("Freya", "remember when u said i should \"behave\" on stream", "freya_dm", do_pause=False, log_to_history=False, do_restart=False)
        send_phone_message(phone_config["phone_player_name"], "Because you absolutely should.", "freya_dm", do_pause=False, log_to_history=False, do_restart=False)
        send_phone_message("Freya", "well too late", "freya_dm", do_pause=False, log_to_history=False, do_restart=False)
        send_phone_message("Freya", "chat asked why i kept smiling at my phone", "freya_dm", do_pause=False, log_to_history=False, do_restart=False)
        if freyaroute:
            send_phone_message("Freya", "ur fault btw", "freya_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message("Freya", "images/ch2ep1_1040.jpg", "freya_dm", 2, do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message("Freya", "thats what i was smiling at", "freya_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message(phone_config["phone_player_name"], "Wait, when did you...", "freya_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message("Freya", "queen of blowjobs?", "freya_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message(phone_config["phone_player_name"], "Oh...", "freya_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message(phone_config["phone_player_name"], "You're going to get me doxxed. LOL.", "freya_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message("Freya", "worth it you were sooooo hot btw 😍", "freya_dm", do_pause=False, log_to_history=False, do_restart=False)

        ## 7 months ago ##
        phone_stamp_rel("freya_dm", back_months=7, do_pause=False)
        send_phone_message("Freya", "did u know u have the emotional range of a teaspoon", "freya_dm", do_pause=False, log_to_history=False, do_restart=False)
        send_phone_message(phone_config["phone_player_name"], "I tell you... things.", "freya_dm", do_pause=False, log_to_history=False, do_restart=False)
        send_phone_message("Freya", "u tell me FACTS", "freya_dm", do_pause=False, log_to_history=False, do_restart=False)
        send_phone_message("Freya", "thats not emotions thats customer service voice", "freya_dm", do_pause=False, log_to_history=False, do_restart=False)
        send_phone_message(phone_config["phone_player_name"], "I have emotions.", "freya_dm", do_pause=False, log_to_history=False, do_restart=False)
        send_phone_message("Freya", "name ONE", "freya_dm", do_pause=False, log_to_history=False, do_restart=False)
        if freyaroute:
            send_phone_message(phone_config["phone_player_name"], "I love you.", "freya_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message("Freya", "my entire body made a windows error noise", "freya_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message("Freya", "🤯🤯🤯", "freya_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message(phone_config["phone_player_name"], "You just wanted to get that out of me, didn't you?", "freya_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message("Freya", "😘", "freya_dm", do_pause=False, log_to_history=False, do_restart=False)

        ## 6 months ago ##
        phone_stamp_rel("freya_dm", back_months=6, do_pause=False)
        send_phone_message("Freya", "hey random question", "freya_dm", do_pause=False, log_to_history=False, do_restart=False)
        send_phone_message("Freya", "is miss klara doing okay", "freya_dm", do_pause=False, log_to_history=False, do_restart=False)
        send_phone_message("Freya", "i havent seen her in forever", "freya_dm", do_pause=False, log_to_history=False, do_restart=False)
        send_phone_message(phone_config["phone_player_name"], "She's... not doing great.", "freya_dm", do_pause=False, log_to_history=False, do_restart=False)
        send_phone_message(phone_config["phone_player_name"], "She's been staying in her room most days. Heck, I haven't seen her open the door once.", "freya_dm", do_pause=False, log_to_history=False, do_restart=False)
        send_phone_message("Freya", "shit", "freya_dm", do_pause=False, log_to_history=False, do_restart=False)
        send_phone_message("Freya", "i knew she wasnt like sunshine or anything but thats different", "freya_dm", do_pause=False, log_to_history=False, do_restart=False)
        send_phone_message("Freya", "tell her i said hi i guess", "freya_dm", do_pause=False, log_to_history=False, do_restart=False)
        send_phone_message("Freya", "and that she can punch me if she ever needs to yell at someone", "freya_dm", do_pause=False, log_to_history=False, do_restart=False)
        send_phone_message(phone_config["phone_player_name"], "I'll tell her.", "freya_dm", do_pause=False, log_to_history=False, do_restart=False)
        send_phone_message("Freya", "not the punch me part tho", "freya_dm", do_pause=False, log_to_history=False, do_restart=False)

        ## 5 months ago ##
        phone_stamp_rel("freya_dm", back_months=5, do_pause=False)
        send_phone_message("Freya", "stream overrrrrr", "freya_dm", do_pause=False, log_to_history=False, do_restart=False)
        send_phone_message("Freya", "ty for hanging out chat was actually tolerable today", "freya_dm", do_pause=False, log_to_history=False, do_restart=False)
        if freyaroute:
            send_phone_message("Freya", "ALSO", "freya_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message("Freya", "[mc]", "freya_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message("Freya", "WHAT WAS THAT DONO", "freya_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message("Freya", "i almost choked on my drink live", "freya_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message("Freya", "do u WANT me to die on camera is that it", "freya_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message(phone_config["phone_player_name"], "Consider it hazard pay for letting the internet look at you.", "freya_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message("Freya", "thats not pocket change that was like", "freya_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message("Freya", "\"i feel guilty watching the vods for free\" money", "freya_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message(phone_config["phone_player_name"], "You work hard. Let me spoil you a bit.", "freya_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message("Freya", "stop saying nice things im feral i dont know how to process that", "freya_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message("Freya", "ok fiiiine", "freya_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message("Freya", "special thank u for my favorite whale only: [ftname]", "freya_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message("Freya", "images/ch2ep1_1039.jpg", "freya_dm", 2, do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message(phone_config["phone_player_name"], "...", "freya_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message(phone_config["phone_player_name"], "Worth every cent.", "freya_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message("Freya", "DONT SAY IT LIKE THAT IM GONNA SHORT CIRCUIT", "freya_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message("Freya", "😤😤😤", "freya_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message(phone_config["phone_player_name"], "Cum tribute done.", "freya_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message("Freya", "YOU DID WHAT???", "freya_dm", do_pause=False, log_to_history=False, do_restart=False)

        ## 4 months ago ##
        phone_stamp_rel("freya_dm", back_months=4, do_pause=False)
        send_phone_message("Freya", "im at Corner Potatoes", "freya_dm", do_pause=False, log_to_history=False, do_restart=False)
        send_phone_message("Freya", "these fries are so good im actually mad youre not here", "freya_dm", do_pause=False, log_to_history=False, do_restart=False)
        send_phone_message(phone_config["phone_player_name"], "Hello? You could've invited me?", "freya_dm", do_pause=False, log_to_history=False, do_restart=False)
        send_phone_message("Freya", "i did", "freya_dm", do_pause=False, log_to_history=False, do_restart=False)
        send_phone_message("Freya", "in my head", "freya_dm", do_pause=False, log_to_history=False, do_restart=False)
        send_phone_message("Freya", "you didnt answer", "freya_dm", do_pause=False, log_to_history=False, do_restart=False)
        send_phone_message(phone_config["phone_player_name"], "... 😒", "freya_dm", do_pause=False, log_to_history=False, do_restart=False)

        ## 3 months ago ##
        phone_stamp_rel("freya_dm", back_months=3, do_pause=False)
        send_phone_message("Freya", "movie night on our day off?", "freya_dm", do_pause=False, log_to_history=False, do_restart=False)
        send_phone_message("Freya", "ill even let u pick so u stop crying about my taste", "freya_dm", do_pause=False, log_to_history=False, do_restart=False)
        send_phone_message(phone_config["phone_player_name"], "Your taste is violence and trauma.", "freya_dm", do_pause=False, log_to_history=False, do_restart=False)
        send_phone_message("Freya", "and subtitles", "freya_dm", do_pause=False, log_to_history=False, do_restart=False)
        send_phone_message("Freya", "im cultured", "freya_dm", do_pause=False, log_to_history=False, do_restart=False)
        send_phone_message(phone_config["phone_player_name"], "You made me watch a 3-hour film where everyone died in silence.", "freya_dm", do_pause=False, log_to_history=False, do_restart=False)
        send_phone_message("Freya", "absolute cinema is about suffering [mc]", "freya_dm", do_pause=False, log_to_history=False, do_restart=False)
        send_phone_message("Freya", "also bc u whined like a sissy when i picked the romance one", "freya_dm", do_pause=False, log_to_history=False, do_restart=False)
        send_phone_message(phone_config["phone_player_name"], "It was about two people staring at each other for fifteen DAMN minutes straight.", "freya_dm", do_pause=False, log_to_history=False, do_restart=False)
        send_phone_message(phone_config["phone_player_name"], "Heck, Twilight had better love story than whatever that abomination was.", "freya_dm", do_pause=False, log_to_history=False, do_restart=False)
        send_phone_message("Freya", "THATS CALLED TENSION", "freya_dm", do_pause=False, log_to_history=False, do_restart=False)
        send_phone_message("Freya", "u wouldnt get it", "freya_dm", do_pause=False, log_to_history=False, do_restart=False)
        send_phone_message(phone_config["phone_player_name"], "I get tension. I lived through your commentary.", "freya_dm", do_pause=False, log_to_history=False, do_restart=False)
        send_phone_message("Freya", "my commentary was ICONIC shut up", "freya_dm", do_pause=False, log_to_history=False, do_restart=False)
        send_phone_message("Freya", "anyway pick something good this time", "freya_dm", do_pause=False, log_to_history=False, do_restart=False)
        send_phone_message(phone_config["phone_player_name"], "Lower your expectations.", "freya_dm", do_pause=False, log_to_history=False, do_restart=False)
        send_phone_message("Freya", "never", "freya_dm", do_pause=False, log_to_history=False, do_restart=False)

        if (freyaroute and freyapoint == 10):
            phone_stamp_rel("freya_dm", back_months=3, do_pause=False)
            send_phone_message("Freya", "screw the movie this was a better happy ending", "freya_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message("Freya", "images/ch2ep1_1038.jpg", "freya_dm", 2, do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message(phone_config["phone_player_name"], "... Frey.", "freya_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message(phone_config["phone_player_name"], "You're gonna kill me one of these days.", "freya_dm", do_pause=False, log_to_history=False, do_restart=False)
        
        ## 2 months ago ##
        phone_stamp_rel("freya_dm", back_months=2, do_pause=False)
        send_phone_message("Freya", "soooooo", "freya_dm", do_pause=False, log_to_history=False, do_restart=False)
        send_phone_message("Freya", "u werent gonna tell me", "freya_dm", do_pause=False, log_to_history=False, do_restart=False)
        send_phone_message("Freya", "that youre LEAVING this store to go be mr. fancy REGIONAL MANAGER??", "freya_dm", do_pause=False, log_to_history=False, do_restart=False)
        send_phone_message(phone_config["phone_player_name"], "I was going to tell you today.", "freya_dm", do_pause=False, log_to_history=False, do_restart=False)
        send_phone_message("Freya", "uh huh sure thats what ppl say when they get caught", "freya_dm", do_pause=False, log_to_history=False, do_restart=False)
        send_phone_message("Freya", "cant believe youre abandoning me with THIS gremlin", "freya_dm", do_pause=False, log_to_history=False, do_restart=False)
        send_phone_message(phone_config["phone_player_name"], "I'm not abandoning you.", "freya_dm", do_pause=False, log_to_history=False, do_restart=False)
        send_phone_message("Freya", "you kinda ARE", "freya_dm", do_pause=False, log_to_history=False, do_restart=False)
        send_phone_message("Freya", "whos gonna stop me from fighting customers now???", "freya_dm", do_pause=False, log_to_history=False, do_restart=False)
        send_phone_message(phone_config["phone_player_name"], "You're not supposed to fight customers {b}now{/b}.", "freya_dm", do_pause=False, log_to_history=False, do_restart=False)
        send_phone_message("Freya", "YEAH AND WHO ENFORCES THAT RULE???", "freya_dm", do_pause=False, log_to_history=False, do_restart=False)
        send_phone_message(phone_config["phone_player_name"], "I'll still be around. It's just a different position.", "freya_dm", do_pause=False, log_to_history=False, do_restart=False)
        send_phone_message("Freya", "different position my ass", "freya_dm", do_pause=False, log_to_history=False, do_restart=False)
        if freyaroute:
            send_phone_message(phone_config["phone_player_name"], "Is that a promise next time I visit for a back room \"inspection\"? 😜", "freya_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message("Freya", "stop making me horny im trying to vent!!!", "freya_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message("Freya", "😤😤😤", "freya_dm", do_pause=False, log_to_history=False, do_restart=False)
        send_phone_message("Freya", "youre leaving ME here while you go play boss man somewhere else", "freya_dm", do_pause=False, log_to_history=False, do_restart=False)
        send_phone_message("Freya", "i hate it", "freya_dm", do_pause=False, log_to_history=False, do_restart=False)
        send_phone_message(phone_config["phone_player_name"], "... I didn't think you'd take it this hard.", "freya_dm", do_pause=False, log_to_history=False, do_restart=False)
        send_phone_message("Freya", "like im not crying or anything jeez", "freya_dm", do_pause=False, log_to_history=False, do_restart=False)
        send_phone_message("Freya", "im just MAD bc we were a duo", "freya_dm", do_pause=False, log_to_history=False, do_restart=False)
        send_phone_message("Freya", "and now its just me and an idiot who dont know how to read instructions", "freya_dm", do_pause=False, log_to_history=False, do_restart=False)
        send_phone_message(phone_config["phone_player_name"], "You'll survive. You're Freya.", "freya_dm", do_pause=False, log_to_history=False, do_restart=False)
        send_phone_message("Freya", "stop hyping me up im trying to be mad at you", "freya_dm", do_pause=False, log_to_history=False, do_restart=False)
        send_phone_message(phone_config["phone_player_name"], "You can be mad. I get it.", "freya_dm", do_pause=False, log_to_history=False, do_restart=False)
        send_phone_message(phone_config["phone_player_name"], "But it's a good opportunity. I couldn't turn it down.", "freya_dm", do_pause=False, log_to_history=False, do_restart=False)
        send_phone_message("Freya", "yeah yeah growth character development blah blah whatever", "freya_dm", do_pause=False, log_to_history=False, do_restart=False)
        send_phone_message("Freya", "still hate it", "freya_dm", do_pause=False, log_to_history=False, do_restart=False)
        send_phone_message("Freya", "but im proud of you too or whatever", "freya_dm", do_pause=False, log_to_history=False, do_restart=False)
        send_phone_message(phone_config["phone_player_name"], "Thank you. Really.", "freya_dm", do_pause=False, log_to_history=False, do_restart=False)
        send_phone_message("Freya", "dont make this wholesome im trying to sulk", "freya_dm", do_pause=False, log_to_history=False, do_restart=False)
        send_phone_message("Freya", "😶", "freya_dm", do_pause=False, log_to_history=False, do_restart=False)

        ## 1 month ago ##
        phone_stamp_rel("freya_dm", back_months=1, do_pause=False)
        send_phone_message(phone_config["phone_player_name"], "Frey.", "freya_dm", do_pause=False, log_to_history=False, do_restart=False)
        send_phone_message("Freya", "dont talk to me im sad", "freya_dm", do_pause=False, log_to_history=False, do_restart=False)
        send_phone_message("Freya", "*mad", "freya_dm", do_pause=False, log_to_history=False, do_restart=False)
        send_phone_message(phone_config["phone_player_name"], "Still?", "freya_dm", do_pause=False, log_to_history=False, do_restart=False)
        send_phone_message("Freya", "still so shoo", "freya_dm", do_pause=False, log_to_history=False, do_restart=False)

        phone_stamp_rel("freya_dm", back_months=1, do_pause=False)
        send_phone_message(phone_config["phone_player_name"], "You on shift tomorrow?", "freya_dm", do_pause=False, log_to_history=False, do_restart=False)
        send_phone_message("Freya", "yeah why what did i do", "freya_dm", do_pause=False, log_to_history=False, do_restart=False)
        send_phone_message(phone_config["phone_player_name"], "Nothing... yet.", "freya_dm", do_pause=False, log_to_history=False, do_restart=False)
        send_phone_message(phone_config["phone_player_name"], "Heads up: I've got a performance inspection at your branch tomorrow.", "freya_dm", do_pause=False, log_to_history=False, do_restart=False)
        send_phone_message(phone_config["phone_player_name"], "I'm not really supposed to warn you in advance, so you didn't hear this from me.", "freya_dm", do_pause=False, log_to_history=False, do_restart=False)
        send_phone_message("Freya", "oh so youre cheating for me now", "freya_dm", do_pause=False, log_to_history=False, do_restart=False)
        send_phone_message("Freya", "love that for us", "freya_dm", do_pause=False, log_to_history=False, do_restart=False)
        send_phone_message(phone_config["phone_player_name"], "I just don't want you or the girl you're training getting blindsided.", "freya_dm", do_pause=False, log_to_history=False, do_restart=False)
        send_phone_message("Freya", "oh GREAT her", "freya_dm", do_pause=False, log_to_history=False, do_restart=False)
        send_phone_message("Freya", "she cant even stack buns in the right order", "freya_dm", do_pause=False, log_to_history=False, do_restart=False)
        send_phone_message("Freya", "if she drags my score down im committing a crime", "freya_dm", do_pause=False, log_to_history=False, do_restart=False)
        send_phone_message("Freya", "and why the F does she keeps calling me \"maam\"", "freya_dm", do_pause=False, log_to_history=False, do_restart=False)
        send_phone_message("Freya", "which is RUDE bc im baby", "freya_dm", do_pause=False, log_to_history=False, do_restart=False)
        send_phone_message(phone_config["phone_player_name"], "You're many things. \"Baby\" is not the word I'd use.", "freya_dm", do_pause=False, log_to_history=False, do_restart=False)
        send_phone_message("Freya", "SHUSH! im delicate", "freya_dm", do_pause=False, log_to_history=False, do_restart=False)
        send_phone_message("Freya", "but ok noted inspector sir", "freya_dm", do_pause=False, log_to_history=False, do_restart=False)
        send_phone_message("Freya", "ill make sure no one sets anything on fire", "freya_dm", do_pause=False, log_to_history=False, do_restart=False)
        send_phone_message(phone_config["phone_player_name"], "Walk her through the basics before I get there.", "freya_dm", do_pause=False, log_to_history=False, do_restart=False)
        send_phone_message("Freya", "ugh fiiine \"teamwork\" or whatever", "freya_dm", do_pause=False, log_to_history=False, do_restart=False)
        send_phone_message(phone_config["phone_player_name"], "That would be appreciated.", "freya_dm", do_pause=False, log_to_history=False, do_restart=False)
        send_phone_message("Freya", "if i survive this u owe me fries", "freya_dm", do_pause=False, log_to_history=False, do_restart=False)
        send_phone_message(phone_config["phone_player_name"], "Deal. Just don't bite a customer in front of me.", "freya_dm", do_pause=False, log_to_history=False, do_restart=False)
        send_phone_message("Freya", "no promises", "freya_dm", do_pause=False, log_to_history=False, do_restart=False)
        send_phone_message("Freya", "hey", "freya_dm", do_pause=False, log_to_history=False, do_restart=False)
        send_phone_message("Freya", "can u pick me up after my shift?", "freya_dm", do_pause=False, log_to_history=False, do_restart=False)
        send_phone_message("Freya", "feet will be dead, dignity will be gone, i will require evac", "freya_dm", do_pause=False, log_to_history=False, do_restart=False)
        send_phone_message(phone_config["phone_player_name"], "I'll be there. End of shift, right?", "freya_dm", do_pause=False, log_to_history=False, do_restart=False)
        send_phone_message("Freya", "yeah", "freya_dm", do_pause=False, log_to_history=False, do_restart=False)
        send_phone_message("Freya", "dont be late i wanna complain about management to management", "freya_dm", do_pause=False, log_to_history=False, do_restart=False)

        ## Present ##
        phone_stamp_rel("freya_dm", back_days=2, do_pause=False)
        send_phone_message("Freya", "😎☝️", "freya_dm", do_pause=False, log_to_history=False, do_restart=False)
        send_phone_message(phone_config["phone_player_name"], "Nerd...", "freya_dm", do_pause=False, log_to_history=False, do_restart=False)
        send_phone_message("Freya", "hey 😡", "freya_dm", do_pause=False, log_to_history=False, do_restart=False)
        if freyaroute:
            send_phone_message(phone_config["phone_player_name"], "I love you.", "freya_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message("Freya", "😳😳😳", "freya_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message("Freya", "i love", "freya_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message(phone_config["phone_player_name"], "I love...?", "freya_dm", do_pause=False, log_to_history=False, do_restart=False)
            send_phone_message("Freya", "i love you too goddamnit", "freya_dm", do_pause=False, log_to_history=False, do_restart=False)

        phone_stamp_rel("freya_dm", back_hours=1, back_minutes=36, do_pause=False)
        send_phone_message("Freya", "😒😒😒", "freya_dm", do_pause=False, log_to_history=False, do_restart=False)
        send_phone_message("Freya", "hey, [mc]", "freya_dm", do_pause=False, log_to_history=False, do_restart=False)
        send_phone_message("Freya", "can u pick me up later? 😩", "freya_dm", do_pause=False, log_to_history=False, do_restart=False)
        send_phone_message(phone_config["phone_player_name"], "Yeah, sure. I'll be there.", "freya_dm", do_pause=False, log_to_history=False, do_restart=False)
        send_phone_message(phone_config["phone_player_name"], "Do I need to bring anything? Water? Snacks?", "freya_dm", do_pause=False, log_to_history=False, do_restart=False)
        send_phone_message(phone_config["phone_player_name"], "... a stretcher? Ambulance?", "freya_dm", do_pause=False, log_to_history=False, do_restart=False)
        send_phone_message("Freya", "WOW", "freya_dm", do_pause=False, log_to_history=False, do_restart=False)
        send_phone_message("Freya", "im tired not DYING wtf", "freya_dm", do_pause=False, log_to_history=False, do_restart=False)
        send_phone_message("Freya", "😵‍💫😵‍💫😵‍💫", "freya_dm", do_pause=False, log_to_history=False, do_restart=False)
        send_phone_message("Freya", "but like if u DID show up w an ambulance i wouldnt complain", "freya_dm", do_pause=False, log_to_history=False, do_restart=False)






        ##### CLAIRE #####
        ## 13 months ago ##
        ## 12 months ago ##
        ## 11 months ago ##
        ## 10 months ago ##
        ## 9 months ago ##
        ## 8 months ago ##
        ## 7 months ago ##
        ## 6 months ago ##
        ## 5 months ago ##
        ## 4 months ago ##
        ## 3 months ago ##
        ## 2 months ago ##
        ## 1 months ago ##






        ##### JESS #####
        ## 13 months ago ##
        ## 12 months ago ##
        ## 11 months ago ##
        ## 10 months ago ##
        ## 9 months ago ##
        ## 8 months ago ##
        ## 7 months ago ##
        ## 6 months ago ##
        ## 5 months ago ##
        ## 4 months ago ##
        ## 3 months ago ##
        ## 2 months ago ##
        ## 1 months ago ##

        clear_notifications()
        renpy.restart_interaction()

    def _resolve_typing_name(channel_name, sender_name=None):
        if sender_name:
            return sender_name

        ch = store.phone_channel_data.get(channel_name, None)
        if not ch:
            return "Someone"

        participants = ch.get("participants", [])
        me = store.phone_config["phone_player_name"]
        for p in participants:
            if p != me:
                return p

        return ch.get("display_name", "Someone")

    def phone_pause(length=1.0, channel_name=None, sender_name=None):
        """
        Shows '[name] is typing...' during the pause.
        If channel_name is None, uses current_phone_view (only works if you're inside a chat).
        """
        if channel_name is None:
            channel_name = store.current_phone_view

        if channel_name and channel_name != "channel_list":
            who = _resolve_typing_name(channel_name, sender_name)

            store.channel_typing[channel_name] = who
            renpy.restart_interaction()

            renpy.pause(length)

            if store.channel_typing.get(channel_name) == who:
                store.channel_typing.pop(channel_name, None)
            renpy.restart_interaction()
        else:
            renpy.pause(length)

    def phone_start():
        global phone_mode
        phone_mode = True
        renpy.config.allow_skipping = False
        renpy.restart_interaction()

    def phone_end():
        global phone_mode
        phone_mode = False
        renpy.config.allow_skipping = True
        renpy.restart_interaction()

    def lock_phone_screen():
        global disable_phone_menu_switch
        disable_phone_menu_switch = True

    def unlock_phone_screen():
        global disable_phone_menu_switch
        disable_phone_menu_switch = False

    def present_phone_choices(choices, channel_name):
        global phone_choice_options, phone_choice_channel
        phone_choice_options = choices
        phone_choice_channel = channel_name
        renpy.ui.interact()

    def get_channel_preview(channel_name):
        if channel_name in phone_channels and phone_channels[channel_name]:
            for last_message_tuple in reversed(phone_channels[channel_name]):

                if last_message_tuple[3] == 1:
                    continue

                summary_alt = last_message_tuple[5] if len(last_message_tuple) > 5 else None
                if summary_alt and summary_alt != "none":
                    return summary_alt

                sender = last_message_tuple[1]
                message_text = last_message_tuple[2]
                message_kind = last_message_tuple[3]

                if message_kind == 2:
                    preview_text = "[[image]"
                elif message_kind == 4:
                    preview_text = "[[video]"
                else:
                    preview_text = message_text
                    if message_kind == 3:
                        preview_text = re.sub(r"<[^>]+>", "", preview_text).strip()

                is_group = phone_channel_data.get(channel_name, {}).get("is_group", False)

                if is_group and sender != phone_config["phone_player_name"]:
                    full_preview = "{}: {}".format(sender, preview_text)
                else:
                    full_preview = preview_text

                max_len = phone_config.get("preview_max_length", 35)
                if len(full_preview) > max_len:
                    return full_preview[:max_len - 3] + "..."
                else:
                    return full_preview

        return phone_config["preview_no_message"]

    def switch_channel_view(channel_name):
        global current_phone_view, channel_notifs, channel_seen_latest
        current_phone_view = channel_name
        channel_notifs[channel_name] = False
        channel_seen_latest[channel_name] = True
        renpy.restart_interaction()

    def hide_phone_channel(channel_name):
        global channel_visible
        if channel_name in channel_visible:
            channel_visible[channel_name] = False
            renpy.restart_interaction()

    def show_phone_channel(channel_name):
        global channel_visible
        if channel_name in channel_visible:
            channel_visible[channel_name] = True
            renpy.restart_interaction()

    def hide_all_phone_channels(except_channel=None):
        global channel_visible
        for ch in list(phone_channel_data.keys()):
            if ch != except_channel:
                channel_visible[ch] = False
            else:
                channel_visible[ch] = True
        renpy.restart_interaction()

    def show_all_phone_channels():
        global channel_visible
        for ch in list(phone_channel_data.keys()):
            channel_visible[ch] = True
        renpy.restart_interaction()

    def delete_phone_channel(channel_name):
        global phone_channel_data, phone_channels, channel_last_message_id, channel_seen_latest, channel_notifs, channel_visible, channel_latest_global_id, current_phone_view
        if channel_name in phone_channel_data:
            del phone_channel_data[channel_name]
        if channel_name in phone_channels:
            del phone_channels[channel_name]
        if channel_name in channel_last_message_id:
            del channel_last_message_id[channel_name]
        if channel_name in channel_seen_latest:
            del channel_seen_latest[channel_name]
        if channel_name in channel_notifs:
            del channel_notifs[channel_name]
        if channel_name in channel_visible:
            del channel_visible[channel_name]
        if channel_name in channel_latest_global_id:
            del channel_latest_global_id[channel_name]
        if current_phone_view == channel_name:
            switch_channel_view("channel_list")
        renpy.restart_interaction()

    def add_participant_to_group(channel_name, new_participant_name, added_by_name=None):
        if channel_name in phone_channel_data and phone_channel_data[channel_name]["is_group"]:
            phone_channel_data[channel_name]["participants"].append(new_participant_name)
            if added_by_name:
                template = phone_config.get("group_added", "{adder} added {participant} to the group.")
                message_text = template.format(adder=added_by_name, participant=new_participant_name)
            else:
                template = phone_config.get("group_joined", "{participant} joined the group.")
                message_text = template.format(participant=new_participant_name)
            send_phone_message("", message_text, channel_name, message_kind=1, do_pause=True)

    def remove_participant_from_group(channel_name, participant_to_remove):
        if channel_name in phone_channel_data and phone_channel_data[channel_name]["is_group"]:
            if participant_to_remove in phone_channel_data[channel_name]["participants"]:
                phone_channel_data[channel_name]["participants"].remove(participant_to_remove)
                template = phone_config.get("group_left", "{participant} left the group.")
                message_text = template.format(participant=participant_to_remove)
                send_phone_message("", message_text, channel_name, message_kind=1, do_pause=True)

    def has_any_notification():
        return any(channel_notifs.values())

    def has_any_notification_not_active():
        return any(has_notif for channel, has_notif in channel_notifs.items() if channel != current_phone_view)

    def get_phone_theme_value(key):
        current_theme = phone_config["phone_theme"]
        return phone_config[current_theme].get(key)

    def set_phone_theme(theme_name):
        if theme_name in phone_config:
            phone_config["phone_theme"] = theme_name
            renpy.restart_interaction()
        else:
            renpy.log("Invalid phone theme: " + theme_name)

## -----------------------------------------------------
## Screen: Phone Messages
## -----------------------------------------------------
default phone_zoom = 0.9
default phone_x = 0.5
default phone_y = 0.5
default phone_force_scroll_bottom = False
default phone_scroll_adj = ui.adjustment()

transform phone_position(p_zoom, p_x, p_y):
    anchor (1.5, 0.5)
    xpos p_x
    zoom p_zoom
    on show:
        ypos 1.5
        ease 0.3 ypos p_y
    on hide:
        ease 0.3 ypos 1.5

transform phone_fade_in_dark:
    on show:
        alpha 0.0
        ease 0.3 alpha 1.0
    on hide:
        ease 0.3 alpha 0.0

style phone_scroll_vscrollbar is vscrollbar:
    xsize 12
    xoffset -9
    yoffset 10
    unscrollable "hide"
    base_bar Frame("images/phone/phonethumb.png", 4, 4)
    thumb Frame("images/phone/phonetrack.png", 4, 4)

style phone_history_button is button:
    background None
    hover_background None
    xpadding 0
    ypadding 0

style phone_history_button_text is default:
    size 25
    color "#FFFFFF"
    hover_color "#bbbbbb"
    xalign 0.5
    outlines []

screen phone_ui():
    add Solid("#0008") at phone_fade_in_dark
    zorder 100
    window:
        at phone_position(phone_zoom, phone_x, phone_y)
        xalign 0.5
        yalign 0.5 
        xsize 600
        ysize 1000
        add get_phone_theme_value("screen_background_image")
        add get_phone_theme_value("header_background_image")
        add get_phone_theme_value("base_background_image")
        if current_phone_view != "channel_list" and disable_phone_menu_switch == False:
            $ back_idle = get_phone_theme_value("back_button_notif_image") if has_any_notification_not_active() else get_phone_theme_value("back_button_idle_image")
            $ back_hover = get_phone_theme_value("back_button_hover_image")
            imagebutton:
                at phone_history_close_fancy
                xalign 0.5
                yalign 0.95
                idle back_idle
                hover back_hover
                focus_mask True
                xysize (75, 75)
                action [
                    SetDict(channel_notifs, current_phone_view, False),
                    SetDict(channel_seen_latest, current_phone_view, True),
                    SetVariable("current_phone_view", "channel_list")
                ]
        vbox:
            id "phone_viewport"
            xsize 450
            ysize 825
            yalign 0.230
            xalign 0.475
            vbox:
                spacing 10
                if current_phone_view != "channel_list":
                    null height 5
                    add phone_channel_data[current_phone_view]["icon"]:
                        ypos 40
                        xalign 0.5
                        xysize (50, 50)
                    text phone_channel_data[current_phone_view]["display_name"]:
                        style "phone_header_style"
                        ypos 30
                else:
                    null height 40
                    text phone_config["channels_title"]:
                        style "phone_header_style"
                null height 19
                if current_phone_view == "channel_list":
                    $ yadj = ui.adjustment()
                    viewport:
                        id "message_viewport"
                        xfill True
                        ysize 700
                        ypos 30
                        yadjustment yadj
                        scrollbars "vertical"
                        mousewheel True
                        draggable True
                        style_prefix "phone_scroll"
                        vbox:
                            spacing 10
                            $ visible_channels = [ch for ch in phone_channel_data.keys() if channel_visible.get(ch, True)]
                            python:
                                if phone_config["sort_channels_by_latest"]:
                                    channel_list_to_display = sorted(
                                        visible_channels,
                                        key=lambda ch_name: channel_latest_global_id.get(ch_name, 0),
                                        reverse=True
                                    )
                                else:
                                    channel_list_to_display = visible_channels
                            for channel_name in channel_list_to_display:
                                button:
                                    action [
                                        SetDict(channel_notifs, channel_name, False),
                                        SetDict(channel_seen_latest, channel_name, True),
                                        SetVariable("current_phone_view", channel_name),
                                        SetVariable("phone_force_scroll_bottom", True)
                                    ]
                                    style "phone_channel_button_style"
                                    xfill True
                                    vbox:
                                        hbox:
                                            spacing 10
                                            add phone_channel_data[channel_name]["icon"]:
                                                xysize (50, 50)
                                                yalign 0.5
                                            vbox:
                                                text phone_channel_data[channel_name]["display_name"]:
                                                    style "phone_channel_name_style"
                                                text get_channel_preview(channel_name):
                                                    style "phone_channel_preview_style"

                                            if channel_notifs.get(channel_name, False):
                                                add get_phone_theme_value("notification_dot_image"):
                                                    xalign 1.0
                                                    yalign 0.6
                                                    xoffset -5
                                                    size (25, 25)
                                        null height 10
                                        frame:
                                            background get_phone_theme_value("channel_divider_colour")
                                            xfill True
                                            ysize 2
                else:
                    # inside a specific chat
                    $ yadj = get_phone_yadj(current_phone_view)
                    $ pending_list = channel_pending_anim.get(current_phone_view, [])
                    $ pending_list = pending_list if isinstance(pending_list, list) else ([pending_list] if pending_list else [])
                    if pending_list:
                        timer 0.1 repeat False action SetDict(channel_pending_anim, current_phone_view, [])
                    viewport:
                        id "message_viewport"
                        xfill True
                        ysize 660
                        #
                        yadjustment yadj
                        scrollbars "vertical"
                        mousewheel True
                        draggable True
                        style_prefix "phone_scroll"
                        if phone_config["auto_scroll"] and phone_force_scroll_bottom:
                            $ yadj.value = (yadj.range + 10000000000000000)
                            $ phone_force_scroll_bottom = False
                            timer 0.1 repeat False action SetVariable("phone_force_scroll_bottom", True)
                        vbox:
                            spacing 8
                            xfill True
                            if current_phone_view in phone_channels:
                                $ all_msgs = phone_channels[current_phone_view]
                                $ total = len(all_msgs)
                                $ limit = phone_visible_limit
                                $ start_index = max(0, total - limit)
                                $ visible_msgs = all_msgs[start_index:]
                                $ last_sender_in_chat_view = None
                                if total > limit:
                                    textbutton "View full history...":
                                        at phone_history_close_fancy
                                        style "phone_history_button"
                                        xalign 0.5
                                        action Show("phone_history_ui", channel=current_phone_view)
                                    null height 10
                                for message_data in visible_msgs:
                                    $ msg_id, sender, message_text, message_kind, current_global_id, summary_alt, image_x, image_y = message_data
                                    $ row_id = "msg_%d" % current_global_id
                                    if sender == phone_config["phone_player_name"]:
                                        $ bubble_image = get_phone_theme_value("player_bubble_image")
                                        $ text_colour = get_phone_theme_value("message_player_text_colour")
                                        $ anim_direction = 1
                                    else:
                                        $ bubble_image = get_phone_theme_value("character_bubble_image")
                                        $ text_colour = get_phone_theme_value("message_character_text_colour")
                                        $ anim_direction = -1
                                    $ msg_padding = phone_config["message_padding"]
                                    $ is_group_chat = phone_channel_data[current_phone_view]["is_group"]
                                    if is_group_chat and sender != phone_config["phone_player_name"] and sender != last_sender_in_chat_view:
                                        text sender:
                                            style "phone_sender_name_style"
                                            xalign msg_padding
                                            xoffset 5
                                    if message_kind == 0:
                                        frame:
                                            id row_id
                                            if sender == phone_config["phone_player_name"]:
                                                xpos 1.0 - msg_padding xanchor 1.0
                                            else:
                                                xpos msg_padding xanchor 0.0
                                            background Frame(bubble_image, 23, 23)
                                            padding (15, 10)
                                            xmaximum 360
                                            if msg_id in pending_list:
                                                at message_appear(anim_direction)
                                            text message_text:
                                                color text_colour
                                                size phone_config["message_font_size"]
                                                layout "tex"
                                                outlines []
                                        $ last_sender_in_chat_view = sender
                                    elif message_kind == 1:
                                        null height 15
                                        hbox:
                                            id row_id
                                            xalign 0.5
                                            xmaximum 360
                                            if msg_id in pending_list:
                                                at timestamp_appear()
                                            python:
                                                ts_text = message_text
                                                if isinstance(summary_alt, tuple) and summary_alt:
                                                    mode = summary_alt[0]
                                                    if mode == "abs":
                                                        dt = summary_alt[1]
                                                        fmt = summary_alt[2]
                                                        ts_text = dt.strftime(fmt).lstrip("0")
                                                    elif mode == "rel":
                                                        base = summary_alt[1]
                                                        delta = phone_clock - base
                                                        total_days = delta.days
                                                        hours = (delta.seconds // 3600)
                                                        minutes = (delta.seconds // 60) % 60
                                                        if total_days >= 365:
                                                            years = total_days // 365
                                                            ts_text = "%d year%s ago" % (years, "" if years == 1 else "s")
                                                        elif total_days >= 30:
                                                            months = total_days // 30
                                                            ts_text = "%d month%s ago" % (months, "" if months == 1 else "s")
                                                        elif total_days > 0:
                                                            ts_text = "%d day%s ago" % (total_days, "" if total_days == 1 else "s")
                                                        elif hours:
                                                            ts_text = "%d hour%s ago" % (hours, "" if hours == 1 else "s")
                                                        elif minutes:
                                                            ts_text = "%d min ago" % minutes
                                                        else:
                                                            ts_text = "just now"
                                            text ts_text:
                                                color get_phone_theme_value("timestamp_text_colour")
                                                size phone_config["timestamp_font_size"]
                                                layout "tex"
                                                outlines []
                                        null height 1
                                        $ last_sender_in_chat_view = None
                                    elif message_kind == 2:
                                        frame:
                                            id row_id
                                            if sender == phone_config["phone_player_name"]:
                                                xpos 1.0 - msg_padding xanchor 1.0
                                            else:
                                                xpos msg_padding xanchor 0.0
                                            background Frame(bubble_image, 23, 23)
                                            padding (10, 10)
                                            xmaximum 360
                                            if msg_id in pending_list:
                                                at message_appear(anim_direction)
                                            imagebutton:
                                                idle Image(message_text)
                                                hover Image(message_text)
                                                at scale_to_fit(image_x, image_y)
                                                action Show("phone_image_zoom", pic=message_text)
                                        $ last_sender_in_chat_view = sender
                                    elif message_kind == 4:
                                        frame:
                                            id row_id
                                            if sender == phone_config["phone_player_name"]:
                                                xpos 1.0 - msg_padding xanchor 1.0
                                            else:
                                                xpos msg_padding xanchor 0.0
                                            background Frame(bubble_image, 23, 23)
                                            padding (10, 10)
                                            xmaximum 360
                                            if msg_id in pending_list:
                                                at message_appear(anim_direction)
                                            imagebutton:
                                                idle Movie(size=(image_x, image_y), play=message_text)
                                                hover Movie(size=(image_x, image_y), play=message_text)
                                                action Show("phone_video_player", vid=message_text)
                                        $ last_sender_in_chat_view = sender
                                    elif message_kind == 3:
                                        frame:
                                            id row_id
                                            if sender == phone_config["phone_player_name"]:
                                                xpos 1.0 - msg_padding xanchor 1.0
                                            else:
                                                xpos msg_padding xanchor 0.0
                                            background Frame(bubble_image, 23, 23)
                                            padding (10, 10)
                                            xmaximum 360
                                            if msg_id in pending_list:
                                                at message_appear(anim_direction)
                                            hbox:
                                                spacing 5
                                                xmaximum 340
                                                text replace_emojis(message_text):
                                                    size phone_config["message_font_size"]
                                                    color text_colour
                                                    layout "tex"
                                                    outlines []
                                        $ last_sender_in_chat_view = sender
                            else:
                                text phone_config["empty_channel_message"]:
                                    style "phone_message_style"
                            if phone_choice_options and phone_choice_channel == current_phone_view:
                                null height 20
                                vbox:
                                    xalign 0.5
                                    spacing 8
                                    for i, (preview_text, actual_message, action) in enumerate(phone_choice_options):
                                        $ message_to_send = actual_message if actual_message is not None else preview_text
                                        $ text_colour = get_phone_theme_value("message_player_text_colour")
                                        textbutton preview_text at choice_appear(delay = i * 0.1):
                                            action [
                                                SetVariable("phone_choice_options", []),
                                                SetVariable("phone_choice_channel", None),
                                                SetVariable("disable_phone_menu_switch", False),
                                                Function(send_phone_message, sender=phone_config["phone_player_name"], message_text=message_to_send, channel_name=current_phone_view, do_pause=False),
                                                If(action is not None, action),
                                                Return()
                                            ]
                                            background Frame(get_phone_theme_value("player_bubble_image"), 23, 23)
                                            idle_background Frame(get_phone_theme_value("player_bubble_image"), 23, 23)
                                            hover_background Frame(get_phone_theme_value("player_bubble_hover_image"), 23, 23)
                                            text_color text_colour
                                            text_size phone_config["choice_font_size"]
                                            text_align 0.5
                                            xalign 0.5
                                            padding (15, 10)
                            $ typing_who = channel_typing.get(current_phone_view, None)
                            if typing_who:
                                hbox:
                                    xpos phone_config["message_padding"]
                                    xanchor 0.0
                                    spacing 6

                                    text "[typing_who] is typing":
                                        size int(phone_config["message_font_size"] * 0.85)
                                        color "#AAAAAADD"
                                        italic True
                                        outlines []

                                    add DynamicDisplayable(_typing_dots)
                            null height 30
    key "toggle_afm" action NullAction()

transform phone_history_close_fancy:
    on show:
        alpha 0.0
        zoom 0.7
        yoffset 20
        pause 0.15
        easeout_back 0.35 alpha 1.0 zoom 1.0 yoffset 0
    on hover:
        ease 0.15 zoom 1.08
    on idle:
        ease 0.15 zoom 1.0
    on activate:
        easein 0.08 zoom 0.9

transform phone_history_pop:
    on show:
        alpha 0.0
        zoom 0.92
        yoffset 40
        easeout_back 0.35 alpha 1.0 zoom 1.0 yoffset 0
    on hide:
        easein_back 0.25 alpha 0.0 zoom 0.92 yoffset 40

style phone_history_frame is frame:
    background Solid("#2C2C2FCC")
    xpadding 40
    ypadding 40
    xmargin 0
    ymargin 0

screen phone_history_ui(channel):
    modal True
    zorder 999
    add Solid("#000a") at phone_fade_in_dark
    frame:
        style "phone_history_frame"
        xalign 0.5
        yalign 0.3
        xsize 560
        ysize 900
        at phone_history_pop
        vbox:
            spacing 10
            hbox:
                xalign 0.5
                spacing 10
                if channel in phone_channel_data:
                    add phone_channel_data[channel]["icon"]:
                        xysize (50, 50)
                        yalign 0.5
                text (phone_channel_data[channel]["display_name"] + " — Full History"):
                    style "phone_header_style"
                    yalign 0.5
            null height 15
            $ yadj = ui.adjustment()
            viewport:
                xfill True
                ysize 730
                yadjustment yadj
                scrollbars "vertical"
                mousewheel True
                draggable True
                style_prefix "phone_scroll"
                vbox:
                    spacing 8
                    xfill True
                    if channel in phone_channels:
                        $ all_msgs = phone_channels[channel]
                        $ latest_channel_id = channel_last_message_id.get(channel, 0)
                        $ last_sender_in_chat_view = None
                        for message_data in all_msgs:
                            $ msg_id, sender, message_text, message_kind, current_global_id, summary_alt, image_x, image_y = message_data
                            if sender == phone_config["phone_player_name"]:
                                $ bubble_image = get_phone_theme_value("player_bubble_image")
                                $ text_colour = get_phone_theme_value("message_player_text_colour")
                            else:
                                $ bubble_image = get_phone_theme_value("character_bubble_image")
                                $ text_colour = get_phone_theme_value("message_character_text_colour")
                            $ msg_padding = phone_config["message_padding"]
                            $ is_group_chat = phone_channel_data[channel]["is_group"]
                            if is_group_chat and sender != phone_config["phone_player_name"] and sender != last_sender_in_chat_view:
                                text sender:
                                    style "phone_sender_name_style"
                                    xalign msg_padding 
                                    xoffset 5
                            if message_kind == 0:
                                frame:
                                    if sender == phone_config["phone_player_name"]:
                                        xpos 1.0 - msg_padding xanchor 1.0
                                    else:
                                        xpos msg_padding xanchor 0.0
                                    background Frame(bubble_image, 23, 23)
                                    padding (15, 10)
                                    xmaximum 360
                                    text message_text:
                                        color text_colour
                                        size phone_config["message_font_size"]
                                        layout "tex"
                                        outlines []
                                $ last_sender_in_chat_view = sender
                            elif message_kind == 1:
                                null height 15
                                hbox:
                                    xalign 0.5
                                    xmaximum 360
                                    python:
                                        ts_text = message_text
                                        if isinstance(summary_alt, tuple) and summary_alt:
                                            mode = summary_alt[0]
                                            if mode == "abs":
                                                dt = summary_alt[1]
                                                fmt = summary_alt[2]
                                                ts_text = dt.strftime(fmt).lstrip("0")
                                            elif mode == "rel":
                                                base = summary_alt[1]
                                                delta = phone_clock - base
                                                total_days = delta.days
                                                hours = (delta.seconds // 3600)
                                                minutes = (delta.seconds // 60) % 60
                                                if total_days >= 365:
                                                    years = total_days // 365
                                                    ts_text = "%d year%s ago" % (years, "" if years == 1 else "s")
                                                elif total_days >= 30:
                                                    months = total_days // 30
                                                    ts_text = "%d month%s ago" % (months, "" if months == 1 else "s")
                                                elif total_days > 0:
                                                    ts_text = "%d day%s ago" % (total_days, "" if total_days == 1 else "s")
                                                elif hours:
                                                    ts_text = "%d hour%s ago" % (hours, "" if hours == 1 else "s")
                                                elif minutes:
                                                    ts_text = "%d min ago" % minutes
                                                else:
                                                    ts_text = "just now"
                                    text ts_text:
                                        color get_phone_theme_value("timestamp_text_colour")
                                        size phone_config["timestamp_font_size"]
                                        layout "tex"
                                        outlines []
                                null height 1
                                $ last_sender_in_chat_view = None
                            elif message_kind == 2:
                                frame:
                                    if sender == phone_config["phone_player_name"]:
                                        xpos 1.0 - msg_padding xanchor 1.0
                                    else:
                                        xpos msg_padding xanchor 0.0
                                    background Frame(bubble_image, 23, 23)
                                    padding (10, 10)
                                    xmaximum 360
                                    imagebutton:
                                        idle Image(message_text)
                                        hover Image(message_text)
                                        at scale_to_fit(image_x, image_y)
                                        action Show("phone_image_zoom", pic=message_text)
                                $ last_sender_in_chat_view = sender
                            elif message_kind == 4:
                                frame:
                                    if sender == phone_config["phone_player_name"]:
                                        xpos 1.0 - msg_padding xanchor 1.0
                                    else:
                                        xpos msg_padding xanchor 0.0
                                    background Frame(bubble_image, 23, 23)
                                    padding (10, 10)
                                    xmaximum 360
                                    imagebutton:
                                        idle Movie(size=(image_x, image_y), play=message_text)
                                        hover Movie(size=(image_x, image_y), play=message_text)
                                        action Show("phone_video_player", vid=message_text)
                                $ last_sender_in_chat_view = sender
                            elif message_kind == 3:
                                frame:
                                    if sender == phone_config["phone_player_name"]:
                                        xpos 1.0 - msg_padding xanchor 1.0
                                    else:
                                        xpos msg_padding xanchor 0.0
                                    background Frame(bubble_image, 23, 23)
                                    padding (10, 10)
                                    xmaximum 360
                                    hbox:
                                        spacing 5
                                        xmaximum 340
                                        text replace_emojis(message_text):
                                            size phone_config["message_font_size"]
                                            color text_colour
                                            layout "tex"
                                            outlines []
                                $ last_sender_in_chat_view = sender
                    else:
                        text phone_config["empty_channel_message"]:
                            style "phone_message_style"
                    null height 30
        imagebutton:
            idle "images/phone/back.png"
            hover "images/phone/back_hover.png"
            xalign 0.5
            yalign 1.17
            at phone_history_close_fancy
            focus_mask True
            action Hide("phone_history_ui")

screen phone_image_zoom(pic):
    modal True
    zorder 999
    add Solid("#000a") at zoom_modal
    frame:
        background None
        align (0.5, 0.5)
        at zoom_modal
        add pic at phone_zoom_fit
    key "mouseup_1" action Hide("phone_image_zoom")
    key "game_menu" action Hide("phone_image_zoom")
    key "rollback" action Hide("phone_image_zoom")

init python:
    phone_zoom_w = int(config.screen_width * 0.85)
    phone_zoom_h = int(config.screen_height * 0.85)

transform phone_zoom_fit:
    fit "contain"
    xysize (phone_zoom_w, phone_zoom_h)

style phone_header_style is default:
    size 28
    color get_phone_theme_value("header_text_colour") 
    xalign 0.5
    outlines []

style phone_channel_button_style is button:
    background None
    hover_background get_phone_theme_value("channel_button_hover_background")
    xpadding 10
    ypadding 8

style phone_channel_name_style is default:
    size 22
    color get_phone_theme_value("channel_name_text_colour")
    bold True
    outlines []

style phone_channel_preview_style is default:
    size 18
    color get_phone_theme_value("channel_preview_text_colour")
    outlines []

style phone_message_style is default:
    size 20
    color get_phone_theme_value("empty_channel_text_colour")
    xalign 0.0
    outlines []

style phone_sender_name_style is default:
    size 16
    color get_phone_theme_value("sender_name_text_colour")
    yoffset 2 
    ypadding 0
    yalign 1.0
    outlines []

transform message_appear(pDirection):
    alpha 0.0
    xoffset 50 * pDirection
    parallel:
        ease 0.5 alpha 1.0
    parallel:
        easein_back 0.5 xoffset 0
    alpha 1.0

transform timestamp_appear():
    alpha 0.0
    yoffset 50
    parallel:
        ease 0.5 alpha 1.0
    parallel: 
        easein_back 0.5 yoffset 0

transform choice_appear(delay=0.0):
    alpha 0.0
    yoffset 50
    pause delay
    parallel:
        ease 0.5 alpha 1.0
    parallel: 
        easein_back 0.5 yoffset 0

transform scale_to_fit(maxw, maxh):
    size (maxw, maxh)
    fit "contain"

transform zoom_modal:
    on show:
        alpha 0.0
        zoom 0.9
        easeout_back 0.25 alpha 1.0 zoom 1.0
    on hide:
        easein_back 0.25 alpha 0.0 zoom 0.9

init python:
    for i in range(1, 190):
        num = str(i).zfill(2)
        renpy.image(f"emoji_smiley_{num}", f"phone/emoji/Emoji Smiley-{num}.png")

screen phone_blocker():
    zorder 98
    button:
        xfill True
        yfill True
        background None
        hover_background None
        action NullAction()

screen phone_close_button():
    zorder 101
    imagebutton:
        at phone_history_close_fancy
        hover_sound "audio/switchclick.mp3"
        activate_sound "audio/click.ogg"
        idle "gui/button/close_%s.png"
        hover "gui/button/closeh_%s.png"
        xpos 0.33
        ypos 0.10
        action [
            Hide("phone_ui"),
            Hide("phone_close_button"),
            Hide("phone_blocker"),
            Function(phone_end),
            SetVariable("quick_menu", True)
        ]

transform phone_launcher_slide:
    on show:
        alpha 0.0
        xoffset 80
        easeout_back 0.25 alpha 1.0 xoffset 0
    on hide:
        easein_back 0.20 alpha 0.0 xoffset 80

screen phone_launcher():
    zorder 50
    if not phone_mode:
        imagebutton:
            at phone_launcher_slide
            hover_sound "audio/switchclick.mp3"
            activate_sound "audio/click.ogg"
            idle "images/phone/phone_icon.png"
            hover "images/phone/phone_icon_h.png"
            xalign 0.9855
            yalign 0.15
            action [
                Function(phone_start),
                SetVariable("current_phone_view", "channel_list"),
                Show("phone_ui"),
                Show("phone_close_button"),
                Show("phone_blocker")
            ]

screen phone_video_player(vid):
    modal True
    zorder 999
    add Solid("#000a") at zoom_modal
    frame:
        background None
        align (0.5, 0.5)
        at zoom_modal
        add Movie(play=vid, size=(1500, 1500))
    key "mouseup_1" action Hide("phone_video_player")
    key "rollback" action Hide("phone_video_player")
    key "game_menu" action Hide("phone_video_player")

label after_load:
    if phone_mode:
        $ renpy.config.allow_skipping = False
    else:
        $ renpy.config.allow_skipping = True
    return
