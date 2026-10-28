init offset = 90





default -90 persistent.godson_gallery_unlocked = []




default -90 gallery_media_controls_visible = False
default -90 gallery_media_transport_visible = False
default -90 gallery_media_paused = False
default -90 gallery_media_scrubbing = False
default -90 gallery_media_preview_focused = False
default -90 gallery_media_resume_after_scrub = True
default -90 gallery_media_file = None
default -90 gallery_media_duration = 0.0
default -90 gallery_media_position = 0.0
default -90 gallery_media_seek_origin = 0.0
default -90 gallery_media_position_text = "0:00"
default -90 gallery_media_duration_text = "0:00"
default -90 gallery_media_preview_hold_ticks = 0

init -10 python:
    GODSON_GALLERY_SCENES = (
    {
        "id": "marnie",
        "title": "MARNIE",
        "subtitle": "Crossing the Line",
        "thumbnail": "images/mommysnaps/marnienot1.jpg",
        "movie": "gui/marnienotfuckingyou.webm",
        "legacy_flag": "seen_notsex1",
    },
    {
        "id": "mommy",
        "title": "MOMMY",
        "subtitle": "Sex Scene Bedroom",
        "thumbnail": "images/jennifer_sex_scene_starts/upright/jenloop.png",
        "replay_label": "jennifer_sex_gallery_replay",
        "legacy_flag": None,
    },
    {
        "id": "princess",
        "title": "YUNI & MC",
        "subtitle": "Nighttime Fun",
        "thumbnail": "images/gallery snaps/yunichristmas.jpg",
        "movie": "gui/yunisuperevil.webm",
        "legacy_flag": "seen_yunisuperevil",
    },
    {
        "id": "nina",
        "title": "NINA",
        "subtitle": "The Appointment",
        "thumbnail": "images/newgame/snap26.jpg",
        "movie": "gui/ninaloveyou.webm",
        "legacy_flag": "seen_ninaloveyou",
    },
    {
        "id": "lorraine",
        "title": "LORRAINE",
        "subtitle": "A Very Short Reunion",
        "thumbnail": "images/newgame/snap35.jpg",
        "movie": "gui/lorrainesex1.webm",
        "legacy_flag": "seen_lorrainesex1",
    },
    {
        "id": "bianca_robert",
        "title": "BIANCA & ROBERT",
        "subtitle": "After Hours",
        "thumbnail": "images/gallery snaps/biancaandhenry.jpg",
        "movie": "gui/bianca1.webm",
        "legacy_flag": "seen_bianca1",
    },
    {
        "id": "gianna_paid",
        "title": "GIANNA & MC",
        "subtitle": "Paid in Full",
        "thumbnail": "images/gallery snaps/giannapaybad.jpg",
        "movie": "gui/payingiannabad.webm",
        "legacy_flag": "seen_payingianna1",
    },
    {
        "id": "lorraine_strip",
        "title": "LORRAINE",
        "subtitle": "A Private Demonstration",
        "thumbnail": "images/gallery snaps/lorrainestrip.jpg",
        "movie": "gui/lorrainestrip.webm",
        "legacy_flag": "seen_lorrainestrip",
    },
    {
        "id": "marnie_party_dance",
        "title": "MARNIE",
        "subtitle": "The Party Begins",
        "thumbnail": "images/gallery snaps/marnieintromovie.jpg",
        "movie": "gui/marniepartydance.webm",
        "legacy_flag": "seen_marniepartydance",
    },
    {
        "id": "martha_hard",
        "title": "MARTHA & MC",
        "subtitle": "Cutting Loose",
        "thumbnail": "images/gallery snaps/marthahardgallery.jpg",
        "movie": "gui/marthahard.webm",
        "legacy_flag": "seen_marthahard",
    },
    {
        "id": "marnie_morning",
        "title": "MARNIE",
        "subtitle": "Morning Tension",
        "thumbnail": "images/gallery snaps/mcblahblahgallery.jpg",
        "movie": "gui/mcblahblah.webm",
        "legacy_flag": "seen_marn",
    },
    {
        "id": "marnie_sexaddict_two",
        "title": "MARNIE & MC",
        "subtitle": "Temptation, Part II",
        "thumbnail": "images/gallery snaps/mcsexaddict2.jpg",
        "movie": "gui/marniesexaddict2.webm",
        "legacy_flag": "seen_marniesexaddict2",
    },
    {
        "id": "martha_twerk",
        "title": "MARTHA",
        "subtitle": "Dancefloor Tease",
        "thumbnail": "images/gallery snaps/mctwerkgallery.jpg",
        "movie": "gui/mctwerk.webm",
        "legacy_flag": "seen_mctwerk1",
    },
    {
        "id": "yuni_dark_joke",
        "title": "YUNI",
        "subtitle": "A Dangerous Joke",
        "thumbnail": "images/gallery snaps/mcyuni16.jpg",
        "movie": "gui/mcyuni16.webm",
        "legacy_flag": "seen_yuni16",
    },
    {
        "id": "marnie_sexaddict_one",
        "title": "MARNIE & MC",
        "subtitle": "Temptation, Part I",
        "thumbnail": "images/gallery snaps/sexaddict1.jpg",
        "movie": "gui/marniesexaddict1.webm",
        "legacy_flag": "seen_marniesexaddict2",
    },
    {
        "id": "marnie_grab_her",
        "title": "MARNIE & MC",
        "subtitle": "A Stolen Kiss",
        "thumbnail": "images/gallery snaps/Snapshot_20260728212330.jpg",
        "movie": "gui/mcgrabher.webm",
        "legacy_flag": "seen_mcgrabher",
    },
    {
        "id": "marnie_grab_kiss",
        "title": "MARNIE & MC",
        "subtitle": "Upstairs Together",
        "thumbnail": "images/gallery snaps/Snapshot_20260728212343.jpg",
        "movie": "gui/mcgrabkiss.webm",
        "legacy_flag": "seen_mcgrabkiss",
    },
    {
        "id": "yuni_pushes_joke",
        "title": "YUNI",
        "subtitle": "Pushing the Joke",
        "thumbnail": "images/gallery snaps/Snapshot_20260728212431.jpg",
        "movie": "gui/mcyuni7.webm",
        "legacy_flag": "seen_yuni7",
    },
    {
        "id": "yuni_stream",
        "title": "YUNI",
        "subtitle": "Live and Unfiltered",
        "thumbnail": "images/gallery snaps/yunistreamgallery.jpg",
        "movie": "gui/yunistream.webm",
        "legacy_flag": "seen_yunistream",
    },
)

    def unlock_gallery_scene(scene_id):
        unlocked = getattr(persistent, "godson_gallery_unlocked", None)
        
        if not isinstance(unlocked, list):
            unlocked = list(unlocked or [])
            persistent.godson_gallery_unlocked = unlocked
        
        if scene_id not in unlocked:
            unlocked.append(scene_id)
            renpy.save_persistent()

    def gallery_scene_unlocked(scene_id, legacy_flag=None):
        unlocked = getattr(persistent, "godson_gallery_unlocked", None) or []
        
        if scene_id in unlocked:
            return True
        
        
        
        if legacy_flag and getattr(persistent, legacy_flag, False):
            return True
        
        return False

    def gallery_unlocked_count():
        return sum(
        1
        for entry in GODSON_GALLERY_SCENES
        if gallery_scene_unlocked(entry["id"], entry["legacy_flag"])
    )


init -5 python:
    GALLERY_MEDIA_CHANNEL = "gallery_media"

    renpy.music.register_channel(
    GALLERY_MEDIA_CHANNEL,
    mixer=config.movie_mixer,
    loop=False,
    stop_on_mute=False,
    movie=True,
    force=True,
)

    def gallery_media_format_time(value):
        seconds = max(0, int(value or 0))
        minutes, seconds = divmod(seconds, 60)
        
        if minutes >= 60:
            hours, minutes = divmod(minutes, 60)
            return "{}:{:02d}:{:02d}".format(hours, minutes, seconds)
        
        return "{}:{:02d}".format(minutes, seconds)

    def gallery_media_prepare(movie_path):
        global gallery_media_controls_visible
        global gallery_media_transport_visible
        global gallery_media_paused
        global gallery_media_scrubbing
        global gallery_media_preview_focused
        global gallery_media_resume_after_scrub
        global gallery_media_file
        global gallery_media_duration
        global gallery_media_position
        global gallery_media_seek_origin
        global gallery_media_position_text
        global gallery_media_duration_text
        global gallery_media_preview_hold_ticks
        
        gallery_media_controls_visible = False
        gallery_media_transport_visible = False
        gallery_media_paused = False
        gallery_media_scrubbing = False
        gallery_media_preview_focused = False
        gallery_media_resume_after_scrub = True
        gallery_media_file = movie_path
        gallery_media_duration = 0.0
        gallery_media_position = 0.0
        gallery_media_seek_origin = 0.0
        gallery_media_position_text = "0:00"
        gallery_media_duration_text = "0:00"
        gallery_media_preview_hold_ticks = 0
        
        
        
        renpy.music.stop(channel=GALLERY_MEDIA_CHANNEL, fadeout=0)
        renpy.music.play(
        movie_path,
        channel=GALLERY_MEDIA_CHANNEL,
        loop=False,
        fadeout=0,
        
        
        synchro_start=True,
    )

    def gallery_media_cleanup():
        global gallery_media_controls_visible
        global gallery_media_transport_visible
        global gallery_media_paused
        global gallery_media_scrubbing
        global gallery_media_preview_focused
        global gallery_media_file
        global gallery_media_preview_hold_ticks
        
        gallery_media_controls_visible = False
        gallery_media_transport_visible = False
        gallery_media_paused = False
        gallery_media_scrubbing = False
        gallery_media_preview_focused = False
        gallery_media_file = None
        gallery_media_preview_hold_ticks = 0
        renpy.music.stop(channel=GALLERY_MEDIA_CHANNEL, fadeout=0)

    def gallery_media_toggle_controls():
        global gallery_media_controls_visible
        global gallery_media_transport_visible
        
        gallery_media_controls_visible = not gallery_media_controls_visible
        
        if not gallery_media_controls_visible:
            gallery_media_transport_visible = False

    def gallery_media_toggle_transport():
        global gallery_media_transport_visible
        gallery_media_transport_visible = not gallery_media_transport_visible

    def gallery_media_toggle_pause():
        global gallery_media_paused
        global gallery_media_position
        global gallery_media_seek_origin
        
        
        if (
        gallery_media_duration > 0.0
        and gallery_media_position >= gallery_media_duration - 0.25
        and gallery_media_file
    ):
            gallery_media_position = 0.0
            gallery_media_seek_origin = 0.0
            renpy.music.play(
            gallery_media_file,
            channel=GALLERY_MEDIA_CHANNEL,
            loop=False,
            fadeout=0,
            synchro_start=True,
        )
            gallery_media_paused = False
            return
        
        gallery_media_paused = not gallery_media_paused
        renpy.music.set_pause(
        gallery_media_paused,
        channel=GALLERY_MEDIA_CHANNEL,
    )

    def gallery_media_preview_focus(focused):
        global gallery_media_preview_focused
        gallery_media_preview_focused = bool(focused)

    def gallery_media_scrub_changed(value):
        global gallery_media_scrubbing
        global gallery_media_resume_after_scrub
        global gallery_media_position
        global gallery_media_position_text
        
        if not gallery_media_scrubbing:
            gallery_media_scrubbing = True
            gallery_media_resume_after_scrub = not gallery_media_paused
            renpy.music.set_pause(True, channel=GALLERY_MEDIA_CHANNEL)
        
        gallery_media_position = max(
        0.0,
        min(float(value), max(gallery_media_duration, 0.0)),
    )
        gallery_media_position_text = gallery_media_format_time(
        gallery_media_position
    )

    def gallery_media_commit_seek(adjustment):
        global gallery_media_scrubbing
        global gallery_media_paused
        global gallery_media_position
        global gallery_media_seek_origin
        global gallery_media_position_text
        global gallery_media_preview_hold_ticks
        
        if not gallery_media_file:
            gallery_media_scrubbing = False
            return
        
        requested_target = max(
        0.0,
        min(float(adjustment.value), max(gallery_media_duration, 0.0)),
    )
        
        
        
        
        target = float(int(requested_target + 0.5))
        if gallery_media_duration > 0.0:
            last_keyframe = float(int(max(gallery_media_duration - 0.001, 0.0)))
            target = min(target, last_keyframe)
        
        
        
        
        play_spec = "<from {:.3f}>{}".format(target, gallery_media_file)
        gallery_media_position = target
        gallery_media_seek_origin = target
        gallery_media_position_text = gallery_media_format_time(target)
        gallery_media_paused = not gallery_media_resume_after_scrub
        gallery_media_scrubbing = False
        
        
        
        gallery_media_preview_hold_ticks = 2
        
        renpy.music.play(
        play_spec,
        channel=GALLERY_MEDIA_CHANNEL,
        loop=False,
        fadeout=0,
        synchro_start=True,
    )
        renpy.music.set_pause(
        gallery_media_paused,
        channel=GALLERY_MEDIA_CHANNEL,
    )

    def gallery_media_tick(adjustment):
        global gallery_media_duration
        global gallery_media_position
        global gallery_media_position_text
        global gallery_media_duration_text
        global gallery_media_preview_hold_ticks
        
        if gallery_media_preview_hold_ticks > 0:
            gallery_media_preview_hold_ticks -= 1
        
        raw_duration = renpy.music.get_duration(GALLERY_MEDIA_CHANNEL) or 0.0
        raw_position = renpy.music.get_pos(GALLERY_MEDIA_CHANNEL)
        
        
        
        gallery_media_duration = max(
        gallery_media_duration,
        float(raw_duration),
        0.0,
    )
        
        if raw_position is not None and not gallery_media_scrubbing:
            position = float(raw_position)
            
            
            
            
            if (
            gallery_media_seek_origin > 0.0
            and position + 0.25 < gallery_media_seek_origin
        ):
                position += gallery_media_seek_origin
            
            if gallery_media_duration > 0.0:
                position = min(position, gallery_media_duration)
            
            gallery_media_position = max(0.0, position)
            
            adjustment.set_range(max(gallery_media_duration, 1.0))
            adjustment.value = gallery_media_position
            adjustment.update()
        
        gallery_media_position_text = gallery_media_format_time(
        gallery_media_position
    )
        gallery_media_duration_text = gallery_media_format_time(
        gallery_media_duration
    )

    def gallery_media_clock_displayable(st, at, which):
        """Redraws a clock without rebuilding the movie-player screen."""
        
        if which == "position":
            value = gallery_media_position_text
            alignment = 1.0
        else:
            value = gallery_media_duration_text
            alignment = 0.0
        
        return Text(
        value,
        style="ui_gallery_media_time_text",
        xsize=155,
        text_align=alignment,
    ), 0.10


init screen gallery():
    tag menu

    use game_menu(_("Gallery"), scroll="viewport"):
        $ gallery_count = gallery_unlocked_count()
        $ gallery_total = len(GODSON_GALLERY_SCENES)
        $ gallery_columns = 3
        $ gallery_rows = (gallery_total + gallery_columns - 1) // gallery_columns
        $ gallery_empty_cells = gallery_columns * gallery_rows - gallery_total

        vbox:
            spacing 34
            xfill True

            hbox:
                xfill True

                vbox:
                    spacing 6

                    text _("MEMORIES") style "ui_section_eyebrow"
                    text _("Unlocked scenes can be replayed at any time.") style "ui_gallery_intro"

                null width 80

                frame:
                    style "ui_gallery_count_frame"
                    xalign 1.0

                    text _("[gallery_count]/[gallery_total] UNLOCKED") style "ui_gallery_count_text"

            grid gallery_columns gallery_rows:
                spacing 34

                for entry in GODSON_GALLERY_SCENES:
                    use gallery_card(entry)

                for i in range(gallery_empty_cells):
                    null width 784 height 505


init screen gallery_card(entry):
    $ is_unlocked = gallery_scene_unlocked(entry["id"], entry["legacy_flag"])
    $ replay_label = entry.get("replay_label", None)
    $ replay_action = [PauseAudio("music", True), Function(renpy.call_in_new_context, replay_label), PauseAudio("music", False)] if replay_label else Show("gallery_player", entry=entry)

    button:
        style "ui_gallery_card"
        sensitive is_unlocked
        action replay_action
        at ui_button_motion

        has fixed
        xfill True
        yfill True

        add entry["thumbnail"]:
            xpos 22
            ypos 22
            xysize (740, 340)
            fit "cover"

        if not is_unlocked:
            add Solid("#05080ADC"):
                xpos 22
                ypos 22
                xysize (740, 340)

            add "gui/ui_refresh/lock.png":
                xalign 0.5
                ypos 102
                xysize (150, 150)

            text _("LOCKED"):
                style "ui_gallery_locked_text"
                xalign 0.5
                ypos 270

        else:
            add Solid("#0010164C"):
                xpos 22
                ypos 22
                xysize (740, 340)

            add "gui/ui_refresh/play.png":
                xalign 0.5
                ypos 104
                xysize (146, 146)

        text entry["title"]:
            style "ui_gallery_title"
            xpos 28
            ypos 384

        text entry["subtitle"]:
            style "ui_gallery_subtitle"
            xpos 28
            ypos 445

        if is_unlocked:
            text _("REPLAY"):
                style "ui_gallery_replay_text"
                xalign 1.0
                xpos 750
                ypos 398


init screen gallery_player(entry):
    default gallery_media_seek_adjustment = ui.adjustment(
        range=1.0,
        value=0.0,
        changed=gallery_media_scrub_changed,
        adjustable=True,
    )

    modal True
    zorder 500

    on "show" action [
        Function(gallery_media_prepare, entry["movie"]),
        PauseAudio("music", True),
    ]
    on "hide" action [
        Function(gallery_media_cleanup),
        PauseAudio("music", False),
    ]

    add Solid("#000000")



    add Movie(channel=GALLERY_MEDIA_CHANNEL):
        xysize (3840, 2160)



    button:
        style "ui_gallery_media_reveal_surface"
        xfill True
        yfill True
        action Function(gallery_media_toggle_controls)

        add Solid("#00000000")



    timer 0.10 repeat True action Function(
        gallery_media_tick,
        gallery_media_seek_adjustment,
        _update_screens=False,
    )

    if gallery_media_controls_visible:
        if gallery_media_transport_visible:
            $ gallery_media_play_label = _("PLAY") if gallery_media_paused else _("PAUSE")




            button:
                style "ui_gallery_media_transport_guard"
                xalign 0.5
                yalign 0.965
                action NullAction()

                add Solid("#00000000")

            frame:
                style "ui_gallery_media_transport_frame"
                xalign 0.5
                yalign 0.965

                has hbox
                spacing 30
                xalign 0.5
                yalign 0.5

                textbutton gallery_media_play_label:
                    style "ui_gallery_media_play_button"
                    action Function(gallery_media_toggle_pause)
                    at ui_button_motion

                add DynamicDisplayable(
                        gallery_media_clock_displayable,
                        "position",
                    ):
                    xsize 155
                    yalign 0.5

                bar:
                    style "ui_gallery_media_seek_bar"
                    adjustment gallery_media_seek_adjustment
                    hovered Function(gallery_media_preview_focus, True)
                    unhovered Function(gallery_media_preview_focus, False)
                    released Function(
                            gallery_media_commit_seek,
                            gallery_media_seek_adjustment,
                        )
                    yalign 0.5

                add DynamicDisplayable(
                        gallery_media_clock_displayable,
                        "duration",
                    ):
                    xsize 155
                    yalign 0.5



            add GodsonScrubPreviewOverlay(
                "gallery",
                entry["movie"],
                820.0,
                2450.0,
                gallery_media_seek_adjustment,
            ):
                xysize (3840, 2160)

        vbox:
            spacing 18
            xalign 0.975
            yalign 0.805

            textbutton _("MEDIA PLAYER"):
                style "ui_gallery_media_side_button"
                selected gallery_media_transport_visible
                action Function(gallery_media_toggle_transport)
                at ui_button_motion

            textbutton _("CLOSE"):
                style "ui_gallery_media_side_button"
                action Hide("gallery_player")
                at ui_button_motion

    key "game_menu" action Hide("gallery_player")


style ui_gallery_intro:
    font gui.interface_text_font2
    size 46
    color "#C7D1D6"

style ui_gallery_count_frame:
    background Frame("gui/ui_refresh/button_selected.png", 34, 34)
    padding (34, 18)
    yalign 0.5

style ui_gallery_count_text:
    font gui.interface_text_font
    size 38
    color "#FFFFFF"

style ui_gallery_card is button:
    xsize 784
    ysize 505
    background Frame("gui/ui_refresh/gallery_idle.png", 38, 38)
    hover_background Frame("gui/ui_refresh/gallery_hover.png", 38, 38)
    insensitive_background Frame("gui/ui_refresh/gallery_locked.png", 38, 38)
    padding (0, 0)

style ui_gallery_title:
    font gui.interface_text_font
    size 48
    color "#FFFFFF"
    outlines [(2, "#00000099", 0, 2)]

style ui_gallery_subtitle:
    font gui.interface_text_font2
    size 34
    color "#A9B7BE"

style ui_gallery_locked_text:
    font gui.interface_text_font
    size 38
    color "#D6E0E4"
    outlines [(3, "#000000CC", 0, 2)]

style ui_gallery_replay_text:
    font gui.interface_text_font
    size 31
    color "#3CDFFF"

style ui_gallery_close_button is button:
    xsize 210
    ysize 66
    background Frame("gui/ui_refresh/quick_idle.png", 28, 28)
    hover_background Frame("gui/ui_refresh/quick_hover.png", 28, 28)
    padding (18, 8)

style ui_gallery_close_button_text is button_text:
    font gui.interface_text_font
    size 27
    color "#FFFFFF"
    hover_color "#FFFFFF"
    xalign 0.5
    yalign 0.5





style ui_gallery_media_reveal_surface is button:
    background None
    hover_background None
    insensitive_background None
    padding (0, 0)
    hover_sound None
    activate_sound None

style ui_gallery_media_transport_guard is button:
    xsize 3260
    ysize 176
    background None
    hover_background None
    insensitive_background None
    padding (0, 0)
    hover_sound None
    activate_sound None

style ui_gallery_media_side_button is button:
    xsize 330
    ysize 78
    background Frame("gui/ui_refresh/quick_idle.png", 28, 28)
    hover_background Frame("gui/ui_refresh/quick_hover.png", 28, 28)
    selected_background Frame("gui/ui_refresh/quick_selected.png", 28, 28)
    padding (22, 10)

style ui_gallery_media_side_button_text is button_text:
    font gui.interface_text_font
    size 29
    color "#E7DED0"
    hover_color "#FFE6A8"
    selected_color "#FFE6A8"
    outlines [(2, "#000000CC", 0, 1)]
    xalign 0.5
    yalign 0.5

style ui_gallery_media_transport_frame is frame:
    xsize 3260
    ysize 176
    background Transform(Frame("gui/ui_refresh/panel_strong.png", 48, 48), alpha=0.20)
    padding (48, 28)

style ui_gallery_media_play_button is button:
    xsize 220
    ysize 82
    background Frame("gui/ui_refresh/quick_idle.png", 28, 28)
    hover_background Frame("gui/ui_refresh/quick_hover.png", 28, 28)
    padding (22, 10)

style ui_gallery_media_play_button_text is button_text:
    font gui.interface_text_font
    size 30
    color "#E7DED0"
    hover_color "#FFE6A8"
    outlines [(2, "#000000CC", 0, 1)]
    xalign 0.5
    yalign 0.5

style ui_gallery_media_seek_bar is bar:
    xsize 2450
    ysize 82
    left_bar Frame("gui/christmas_noir/slider_track_fill.png", 30, 30)
    right_bar Frame("gui/christmas_noir/slider_track_empty.png", 30, 30)
    thumb "gui/christmas_noir/slider_thumb_idle.png"
    hover_thumb "gui/christmas_noir/slider_thumb_hover.png"
    thumb_offset 41

style ui_gallery_media_time_text is text:
    font gui.interface_text_font
    size 31
    color "#F4E9D2"
    outlines [(2, "#000000CC", 0, 1)]
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
