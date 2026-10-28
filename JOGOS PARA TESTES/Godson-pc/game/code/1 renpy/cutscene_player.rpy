





default godson_cutscene_controls_visible = False
default godson_cutscene_transport_visible = False
default godson_cutscene_paused = False
default godson_cutscene_scrubbing = False
default godson_cutscene_preview_focused = False
default godson_cutscene_resume_after_scrub = True
default godson_cutscene_file = None
default godson_cutscene_duration = 0.0
default godson_cutscene_position = 0.0
default godson_cutscene_seek_origin = 0.0
default godson_cutscene_position_text = "0:00"
default godson_cutscene_duration_text = "0:00"
default godson_cutscene_ever_positioned = False
default godson_cutscene_seek_grace_ticks = 0
default godson_cutscene_preview_hold_ticks = 0
default godson_cutscene_paused_before_menu = False


init 85 python:
    GODSON_CUTSCENE_CHANNEL = "godson_cutscene"

    renpy.music.register_channel(
    GODSON_CUTSCENE_CHANNEL,
    mixer=config.movie_mixer,
    loop=False,
    stop_on_mute=False,
    movie=True,
    force=True,
)

    def godson_cutscene_format_time(value):
        seconds = max(0, int(value or 0))
        minutes, seconds = divmod(seconds, 60)
        
        if minutes >= 60:
            hours, minutes = divmod(minutes, 60)
            return "{}:{:02d}:{:02d}".format(hours, minutes, seconds)
        
        return "{}:{:02d}".format(minutes, seconds)

    def godson_cutscene_prepare(movie_path, expected_duration):
        global godson_cutscene_controls_visible
        global godson_cutscene_transport_visible
        global godson_cutscene_paused
        global godson_cutscene_scrubbing
        global godson_cutscene_preview_focused
        global godson_cutscene_resume_after_scrub
        global godson_cutscene_file
        global godson_cutscene_duration
        global godson_cutscene_position
        global godson_cutscene_seek_origin
        global godson_cutscene_position_text
        global godson_cutscene_duration_text
        global godson_cutscene_ever_positioned
        global godson_cutscene_seek_grace_ticks
        global godson_cutscene_preview_hold_ticks
        global godson_cutscene_paused_before_menu
        
        godson_cutscene_controls_visible = False
        godson_cutscene_transport_visible = False
        godson_cutscene_paused = False
        godson_cutscene_scrubbing = False
        godson_cutscene_preview_focused = False
        godson_cutscene_resume_after_scrub = True
        godson_cutscene_file = movie_path
        godson_cutscene_duration = max(0.0, float(expected_duration or 0.0))
        godson_cutscene_position = 0.0
        godson_cutscene_seek_origin = 0.0
        godson_cutscene_position_text = "0:00"
        godson_cutscene_duration_text = godson_cutscene_format_time(
        godson_cutscene_duration
    )
        godson_cutscene_ever_positioned = False
        godson_cutscene_seek_grace_ticks = 0
        godson_cutscene_preview_hold_ticks = 0
        godson_cutscene_paused_before_menu = False
        
        renpy.stop_skipping()
        
        
        renpy.music.stop(channel=GODSON_CUTSCENE_CHANNEL, fadeout=0)
        renpy.music.play(
        movie_path,
        channel=GODSON_CUTSCENE_CHANNEL,
        loop=False,
        fadeout=0,
        
        
        synchro_start=True,
    )
        renpy.music.set_pause(False, channel=GODSON_CUTSCENE_CHANNEL)

    def godson_cutscene_cleanup():
        global godson_cutscene_controls_visible
        global godson_cutscene_transport_visible
        global godson_cutscene_paused
        global godson_cutscene_scrubbing
        global godson_cutscene_preview_focused
        global godson_cutscene_file
        global godson_cutscene_preview_hold_ticks
        global godson_cutscene_paused_before_menu
        
        godson_cutscene_controls_visible = False
        godson_cutscene_transport_visible = False
        godson_cutscene_paused = False
        godson_cutscene_scrubbing = False
        godson_cutscene_preview_focused = False
        godson_cutscene_file = None
        godson_cutscene_preview_hold_ticks = 0
        godson_cutscene_paused_before_menu = False
        renpy.music.stop(channel=GODSON_CUTSCENE_CHANNEL, fadeout=0)

    def godson_cutscene_toggle_controls():
        global godson_cutscene_controls_visible
        global godson_cutscene_transport_visible
        
        godson_cutscene_controls_visible = not godson_cutscene_controls_visible
        
        if not godson_cutscene_controls_visible:
            godson_cutscene_transport_visible = False

    def godson_cutscene_toggle_transport():
        global godson_cutscene_transport_visible
        godson_cutscene_transport_visible = not godson_cutscene_transport_visible

    def godson_cutscene_toggle_pause():
        global godson_cutscene_paused
        godson_cutscene_paused = not godson_cutscene_paused
        renpy.music.set_pause(
        godson_cutscene_paused,
        channel=GODSON_CUTSCENE_CHANNEL,
    )

    def godson_cutscene_pause_for_menu():
        global godson_cutscene_paused_before_menu
        
        
        
        
        godson_cutscene_paused_before_menu = bool(godson_cutscene_paused)
        renpy.music.set_pause(True, channel=GODSON_CUTSCENE_CHANNEL)

    def godson_cutscene_restore_after_menu():
        global godson_cutscene_paused_before_menu
        
        if godson_cutscene_file:
            renpy.music.set_pause(
            godson_cutscene_paused_before_menu,
            channel=GODSON_CUTSCENE_CHANNEL,
        )
        
        godson_cutscene_paused_before_menu = False

    def godson_cutscene_preview_focus(focused):
        global godson_cutscene_preview_focused
        godson_cutscene_preview_focused = bool(focused)

    def godson_cutscene_scrub_changed(value):
        global godson_cutscene_scrubbing
        global godson_cutscene_resume_after_scrub
        global godson_cutscene_position
        global godson_cutscene_position_text
        
        if not godson_cutscene_scrubbing:
            godson_cutscene_scrubbing = True
            godson_cutscene_resume_after_scrub = not godson_cutscene_paused
            renpy.music.set_pause(True, channel=GODSON_CUTSCENE_CHANNEL)
        
        godson_cutscene_position = max(
        0.0,
        min(float(value), max(godson_cutscene_duration, 0.0)),
    )
        godson_cutscene_position_text = godson_cutscene_format_time(
        godson_cutscene_position
    )

    def godson_cutscene_commit_seek(adjustment):
        global godson_cutscene_scrubbing
        global godson_cutscene_paused
        global godson_cutscene_position
        global godson_cutscene_seek_origin
        global godson_cutscene_position_text
        global godson_cutscene_seek_grace_ticks
        global godson_cutscene_preview_hold_ticks
        
        if not godson_cutscene_file:
            godson_cutscene_scrubbing = False
            return
        
        requested_target = max(
        0.0,
        min(float(adjustment.value), max(godson_cutscene_duration, 0.0)),
    )
        
        
        
        
        
        target = float(int(requested_target + 0.5))
        if godson_cutscene_duration > 0.0:
            last_keyframe = float(int(max(godson_cutscene_duration - 0.001, 0.0)))
            target = min(target, last_keyframe)
        play_spec = "<from {:.3f}>{}".format(target, godson_cutscene_file)
        
        godson_cutscene_position = target
        godson_cutscene_seek_origin = target
        godson_cutscene_position_text = godson_cutscene_format_time(target)
        godson_cutscene_paused = not godson_cutscene_resume_after_scrub
        godson_cutscene_scrubbing = False
        godson_cutscene_preview_hold_ticks = 2
        
        
        
        
        godson_cutscene_seek_grace_ticks = 30
        
        renpy.music.play(
        play_spec,
        channel=GODSON_CUTSCENE_CHANNEL,
        loop=False,
        fadeout=0,
        synchro_start=True,
    )
        renpy.music.set_pause(
        godson_cutscene_paused,
        channel=GODSON_CUTSCENE_CHANNEL,
    )

    def godson_cutscene_tick(adjustment):
        global godson_cutscene_duration
        global godson_cutscene_position
        global godson_cutscene_position_text
        global godson_cutscene_duration_text
        global godson_cutscene_ever_positioned
        global godson_cutscene_seek_grace_ticks
        global godson_cutscene_preview_hold_ticks
        
        if godson_cutscene_preview_hold_ticks > 0:
            godson_cutscene_preview_hold_ticks -= 1
        
        raw_duration = renpy.music.get_duration(GODSON_CUTSCENE_CHANNEL) or 0.0
        raw_position = renpy.music.get_pos(GODSON_CUTSCENE_CHANNEL)
        playing = renpy.music.get_playing(GODSON_CUTSCENE_CHANNEL)
        
        godson_cutscene_duration = max(
        godson_cutscene_duration,
        float(raw_duration),
        0.0,
    )
        
        if raw_position is not None:
            godson_cutscene_ever_positioned = True
            
            if not godson_cutscene_scrubbing:
                position = float(raw_position)
                
                if (
                godson_cutscene_seek_origin > 0.0
                and position + 0.25 < godson_cutscene_seek_origin
            ):
                    position += godson_cutscene_seek_origin
                
                if godson_cutscene_duration > 0.0:
                    position = min(position, godson_cutscene_duration)
                
                godson_cutscene_position = max(0.0, position)
                adjustment.set_range(max(godson_cutscene_duration, 1.0))
                adjustment.value = godson_cutscene_position
                adjustment.update()
            
            godson_cutscene_seek_grace_ticks = 0
        
        elif godson_cutscene_seek_grace_ticks > 0:
            godson_cutscene_seek_grace_ticks -= 1
        
        godson_cutscene_position_text = godson_cutscene_format_time(
        godson_cutscene_position
    )
        godson_cutscene_duration_text = godson_cutscene_format_time(
        godson_cutscene_duration
    )
        
        if (
        godson_cutscene_ever_positioned
        and not playing
        and not godson_cutscene_paused
        and not godson_cutscene_scrubbing
        and godson_cutscene_seek_grace_ticks <= 0
    ):
            return "finished"
        
        return None

    def godson_cutscene_clock_displayable(st, at, which):
        if which == "position":
            value = godson_cutscene_position_text
            alignment = 1.0
        else:
            value = godson_cutscene_duration_text
            alignment = 0.0
        
        return Text(
        value,
        style="godson_cutscene_time_text",
        xsize=155,
        text_align=alignment,
    ), 0.10


label godson_locked_cutscene(movie_file, duration, seen_flag=None):
    $ _godson_previous_allow_skipping = config.allow_skipping
    $ config.allow_skipping = False
    $ renpy.stop_skipping()

    call screen godson_cutscene_player(movie_file, duration)

    $ config.allow_skipping = _godson_previous_allow_skipping

    if seen_flag is not None:
        $ setattr(persistent, seen_flag, True)
        $ renpy.save_persistent()

    return


init 90 screen godson_cutscene_player(movie_file, expected_duration):
    default godson_cutscene_seek_adjustment = ui.adjustment(
        range=max(float(expected_duration), 1.0),
        value=0.0,
        changed=godson_cutscene_scrub_changed,
        adjustable=True,
    )

    modal True
    zorder 600

    on "show" action Function(
        godson_cutscene_prepare,
        movie_file,
        expected_duration,
    )
    on "hide" action Function(godson_cutscene_cleanup)



    button:
        style "godson_cutscene_reveal_surface"
        xfill True
        yfill True
        action Function(godson_cutscene_toggle_controls)

        add Solid("#00000000")

    timer 0.10 repeat True action Function(
        godson_cutscene_tick,
        godson_cutscene_seek_adjustment,
        _update_screens=False,
    )

    if godson_cutscene_controls_visible:
        if godson_cutscene_transport_visible:
            $ godson_cutscene_play_label = _("PLAY") if godson_cutscene_paused else _("PAUSE")





            button:
                style "godson_cutscene_transport_guard"
                xalign 0.5
                yalign 0.965
                action NullAction()

                add Solid("#00000000")

            frame:
                style "godson_cutscene_transport_frame"
                xalign 0.5
                yalign 0.965

                has hbox
                spacing 30
                xalign 0.5
                yalign 0.5

                textbutton godson_cutscene_play_label:
                    style "godson_cutscene_play_button"
                    action Function(godson_cutscene_toggle_pause)
                    at ui_button_motion

                add DynamicDisplayable(
                        godson_cutscene_clock_displayable,
                        "position",
                    ):
                    xsize 155
                    yalign 0.5

                bar:
                    style "godson_cutscene_seek_bar"
                    adjustment godson_cutscene_seek_adjustment
                    hovered Function(godson_cutscene_preview_focus, True)
                    unhovered Function(godson_cutscene_preview_focus, False)
                    released Function(
                            godson_cutscene_commit_seek,
                            godson_cutscene_seek_adjustment,
                        )
                    yalign 0.5

                add DynamicDisplayable(
                        godson_cutscene_clock_displayable,
                        "duration",
                    ):
                    xsize 155
                    yalign 0.5



            add GodsonScrubPreviewOverlay(
                "cutscene",
                movie_file,
                865.0,
                2360.0,
                godson_cutscene_seek_adjustment,
            ):
                xysize (3840, 2160)

        vbox:
            spacing 18


            xalign 0.992
            yalign 0.735

            textbutton _("MEDIA PLAYER"):
                style "godson_cutscene_side_button"
                selected godson_cutscene_transport_visible
                action Function(godson_cutscene_toggle_transport)
                at ui_button_motion

            textbutton _("SKIP"):
                style "godson_cutscene_side_button"
                action Return("skip")
                at ui_button_motion

    key "rollback" action NullAction()
    key "rollforward" action NullAction()


    key "game_menu" action [
        Function(godson_cutscene_pause_for_menu),
        ShowMenu("preferences"),
        Function(godson_cutscene_restore_after_menu),
    ]
    key "hide_windows" action NullAction()
    key "skip" action NullAction()
    key "toggle_skip" action NullAction()


init 90 style godson_cutscene_reveal_surface is button:
    background None
    hover_background None
    insensitive_background None
    padding (0, 0)
    hover_sound None
    activate_sound None

init 90 style godson_cutscene_transport_guard is button:
    xsize 3260
    ysize 176
    background None
    hover_background None
    insensitive_background None
    padding (0, 0)
    hover_sound None
    activate_sound None

init 90 style godson_cutscene_side_button is button:
    xsize 330
    ysize 78
    background Frame("gui/ui_refresh/quick_idle.png", 28, 28)
    hover_background Frame("gui/ui_refresh/quick_hover.png", 28, 28)
    selected_background Frame("gui/ui_refresh/quick_selected.png", 28, 28)
    padding (22, 10)

init 90 style godson_cutscene_side_button_text is button_text:
    font gui.interface_text_font
    size 29
    color "#E7DED0"
    hover_color "#FFE6A8"
    selected_color "#FFE6A8"
    outlines [(2, "#000000CC", 0, 1)]
    xalign 0.5
    yalign 0.5

init 90 style godson_cutscene_transport_frame is frame:
    xsize 3260
    ysize 176
    background Transform(Frame("gui/ui_refresh/panel_strong.png", 48, 48), alpha=0.20)
    padding (48, 28)

init 90 style godson_cutscene_play_button is button:
    xsize 220
    ysize 82
    background Frame("gui/ui_refresh/quick_idle.png", 28, 28)
    hover_background Frame("gui/ui_refresh/quick_hover.png", 28, 28)
    padding (22, 10)

init 90 style godson_cutscene_play_button_text is button_text:
    font gui.interface_text_font
    size 30
    color "#FFE6A8"
    hover_color "#FFFFFF"
    outlines [(2, "#000000CC", 0, 1)]
    xalign 0.5
    yalign 0.5

init 90 style godson_cutscene_seek_bar is bar:
    xsize 2360
    ysize 82
    left_bar Frame("gui/christmas_noir/slider_track_fill.png", 30, 30)
    right_bar Frame("gui/christmas_noir/slider_track_empty.png", 30, 30)
    thumb "gui/christmas_noir/slider_thumb_idle.png"
    hover_thumb "gui/christmas_noir/slider_thumb_hover.png"
    thumb_offset 41

init 90 style godson_cutscene_time_text:
    font gui.interface_text_font
    size 30
    color "#F6E7BF"
    outlines [(2, "#000000DD", 0, 1)]
    yalign 0.5
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
