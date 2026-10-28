screen mphone_vault_app_screen:
    tag mphone_vault_app_screen
    modal True
    fixed:
        at mphone_app_transform
        add "mphone_vault_app_bg"
    key "mousedown_4" action NullAction()
    key "mousedown_5" action NullAction()
    key "mouseup_2" action Hide("mphone_vault_app_screen")
    if persistent.golden_phone and persistent.golden_phone_skin_enabled:
        add "mphone_shell_gold"
    else:
        add "mphone_shell"
    fixed:
        at mphone_app_transform
        add "mphone_fg"

        imagebutton at mphone_off_transform:
            idle "mphone_off_circle_idle"
            hover "mphone_off_circle_hover"
            action Hide("mphone_vault_app_screen")
            xalign 0.5
            yalign mphone_off_yalign

        if vault_unlocked:
            text "REWARD\nUNLOCKED" text_align 0.5 style "mphone_vault_text_style" xalign 0.5 yalign 0.46
        else:
            text "ENTER CODE" style "mphone_vault_text_style" xalign 0.5 yalign 0.28
            hbox:
                at mphone_app_transform
                yalign 0.46
                xalign 0.5
                spacing 30 * persistent.scale_factor
                for x in range(0,4):
                    vbox:
                        xalign 0.5
                        imagebutton at mphone_vault_arrow_zoom:
                            xalign 0.5
                            idle "mphone_arrow_up_idle"
                            hover "mphone_arrow_up_hover"
                            if safe_digits[x] < 9:
                                action SetDict(safe_digits,x, safe_digits[x]+1)
                            else:
                                action SetDict(safe_digits,x, 0)
                        textbutton "%s" % safe_digits[x] text_style "mphone_vault_digit_style" xalign 0.5
                        imagebutton at mphone_vault_arrow_zoom:
                            xalign 0.5
                            idle "mphone_arrow_down_idle"
                            hover "mphone_arrow_down_hover"
                            if safe_digits[x] > 0:
                                action SetDict(safe_digits,x, safe_digits[x]-1)
                            else:
                                action SetDict(safe_digits,x, 9)

    fixed:
        at mphone_app_transform
        imagebutton:
            if vault_unlocked:
                idle "mphone_vault_unlock"
                hover "mphone_vault_unlock"
            else:
                idle "mphone_vault_lock_idle"
                hover "mphone_vault_lock_hover"
            xalign 0.5
            yalign 0.67
            if currentEpisode == 9 and safe_digits[0] == 4 and safe_digits[1] == 2 and safe_digits[2] == 3 and safe_digits[3] == 2 and not vault_unlocked:
                action (SetVariable("vault_unlocked", True), safe_rewards_unlock_ep9(), calcRenders(), Function(vault_ach_func))
            elif currentEpisode == 10 and safe_digits[0] == 8 and safe_digits[1] == 3 and safe_digits[2] == 1 and safe_digits[3] == 3 and not vault_unlocked:
                action (SetVariable("vault_unlocked", True), safe_rewards_unlock_ep10(), calcRenders(), Function(vault_ach_func))
            elif currentEpisode == 11 and safe_digits[0] == 3 and safe_digits[1] == 2 and safe_digits[2] == 5 and safe_digits[3] == 8 and not vault_unlocked:
                action (SetVariable("vault_unlocked", True), safe_rewards_unlock_ep11(), calcRenders(), Function(vault_ach_func))
            elif currentEpisode == 12 and safe_digits[0] == 0 and safe_digits[1] == 1 and safe_digits[2] == 2 and safe_digits[3] == 5 and not vault_unlocked:
                action (SetVariable("vault_unlocked", True), safe_rewards_unlock_ep12(), calcRenders(), Function(vault_ach_func))
            else:
                action NullAction()
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
