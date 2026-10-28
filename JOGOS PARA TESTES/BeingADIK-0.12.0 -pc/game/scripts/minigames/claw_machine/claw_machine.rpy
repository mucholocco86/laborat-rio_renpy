screen claw_machine_screen:
    tag claw_machine_screen
    modal True

    if grab_hovered == "up":
        timer 0.01 repeat True action SetDict(claw_offset,1,max(claw_offset[1]-2,-800))
        add "grab_lever_up"
    elif grab_hovered == "right":
        timer 0.01 repeat True action SetDict(claw_offset,0,min(claw_offset[0]+2,550))
        add "grab_lever_right"
    else:
        add "grab_lever_idle"

    add "grab_claw" xoffset claw_offset[0] * persistent.scale_factor yoffset claw_offset[1] * persistent.scale_factor

    imagebutton:
        focus_mask True
        idle "grab_zone_right"
        hover "grab_zone_right"
        hovered Play("sfx1","sound_effects/season3/claw_machine.mp3", loop=True),SetVariable("grab_hovered", "right")
        unhovered Stop("sfx1"),SetVariable("grab_hovered", "idle")
        action NullAction()

    imagebutton:
        focus_mask True
        idle "grab_zone_up"
        hover "grab_zone_up"
        hovered Play("sfx1","sound_effects/season3/claw_machine.mp3", loop=True),SetVariable("grab_hovered", "up")
        unhovered Stop("sfx1"),SetVariable("grab_hovered", "idle")
        action NullAction()

    imagebutton:
        focus_mask True
        idle "grab_button_idle"
        hover "grab_button_hover"
        action Play("sfx2","sound_effects/season2/beep.mp3",loop=False),Return()
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
