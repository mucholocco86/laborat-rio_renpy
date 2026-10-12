screen scr_mm_vault_menu:
    key "game_menu" action [Hide("scr_mm_vault_menu",dissolve),renpy.restart_interaction, SetVariable('quick_menu', False), SetVariable('v_mm_open', False)]

    add "img_vault_main"

    imagebutton:
        idle "img_gradient_[persistent.v_mm_gradient[persistent.v_mm_gradient_order]]" action NullAction()

    add "vault_idle" xalign 0.95 yalign 0.1

    imagebutton:
        xalign 0.01
        yalign 0.98
        auto "btn_mm_back_%s" action [Hide("scr_mm_vault_menu",dissolve),renpy.restart_interaction, SetVariable('quick_menu', False)]

    imagebutton:
        xalign 0.98
        yalign 0.98
        auto "btn_mm_exit_%s" action [Hide("scr_mm_vault_menu",dissolve),Hide("scr_mm_main",dissolve),renpy.restart_interaction, SetVariable('quick_menu', True), SetVariable('v_mm_open', False)]

    use scr_mm_Vault_Combo

init:
    $ v_vault_number = ""
    $ v_vault_number_failed = ""
    $ v_vault_number_success = ""

    default persistent.v_walkthrough_locked = True
    default persistent.v_walkthrough_enabled = False
    default persistent.v_lewd_images_extra_locked = True
    default persistent.v_lewd_images_extra_enabled = False
    default persistent.v_anim_enabled = True
    default persistent.v_sex_anim_enabled_locked = True
    default persistent.v_sex_anim_enabled = not False

    default v_vault_code_1 = "685030"
    default v_vault_code_2 = "338248"
    default v_vault_code_3 = "851375"

style vault_number_style:


    xalign 0.5
    size 80
    color "#25306a"
    outlines [ (3, "#000000", 0, 0) ]

style vault_text_style:
    variant "small"
    size 30

screen scr_mm_Vault_Combo:
    $ tooltip = GetTooltip()
    if len(v_vault_number) == 6:
        if v_vault_number == v_vault_code_1 or v_vault_number == v_vault_code_2 or v_vault_number == v_vault_code_3:
            $ v_vault_number = ""
            $ v_vault_number_success = "{color=#22a074}Unlocked!{/color}"
            timer 0.1 action [Play("sound","sound effects/01/keypad_posative.ogg"),Play("sound2","sound effects/01/door_bolt_unlocking.mp3")]
            timer 1.5 action SetVariable("v_vault_number","")
            timer 1.5 action SetVariable("v_vault_number_success","")
        else:
            $ v_vault_number = ""
            $ v_vault_number_failed = "{color=#9e1010}Wrong Code!{/color}"
            timer 0.1 action [Play("sound","sound effects/01/keypad_negative.ogg")]
            timer 1.5 action SetVariable("v_vault_number","")
            timer 1.5 action SetVariable("v_vault_number_failed","")

    hbox:
        xalign 0.8
        yalign 0.09
        text v_vault_number.center(5) style "vault_number_style"

    hbox:
        xalign 0.855
        yalign 0.09
        text v_vault_number_failed style "vault_number_style"

    hbox:
        xalign 0.83
        yalign 0.09
        text v_vault_number_success style "vault_number_style"

    hbox:
        xalign 0.9
        yalign 0.2
        if len(v_vault_number+"0") >6:
            imagebutton:
                auto "number_0_%s"
            imagebutton:
                auto "number_1_%s"
            imagebutton:
                auto "number_2_%s"
            imagebutton:
                auto "number_3_%s"
            imagebutton:
                auto "number_4_%s"
            imagebutton:
                auto "number_5_%s"
            imagebutton:
                auto "number_6_%s"
            imagebutton:
                auto "number_7_%s"
            imagebutton:
                auto "number_8_%s"
            imagebutton:
                auto "number_9_%s"


        else:
            imagebutton:
                auto "number_0_%s"
                action [
                    Play("sound2","sound effects/01/keypad_beep.ogg"),
                    If(len(v_vault_number+"0") < 6,true=SetVariable("v_vault_number",v_vault_number+"0"),
                    false=If(v_vault_number+"0" == v_vault_code_1,true=[SetField (persistent,"v_secrets_locked", False),SetVariable("v_vault_number",v_vault_number+"0")],
                    false=If(v_vault_number+"0" == v_vault_code_2,true=[SetField (persistent,"v_secrets_locked", False),SetField (persistent,"v_walkthrough_locked", False),SetVariable("v_vault_number","")],
                    false=If(v_vault_number+"0" == v_vault_code_3,true=[SetField (persistent,"v_secrets_locked", False),SetField (persistent,"v_walkthrough_locked", False),SetField (persistent,"v_lewd_images_extra_locked", False),SetField (persistent,"v_sex_anim_enabled_locked", False),SetVariable("v_vault_number","")],
                    false=SetVariable("v_vault_number",v_vault_number+"0")))))]
            imagebutton:
                auto "number_1_%s"
                action [
                    Play("sound2","sound effects/01/keypad_beep.ogg"),
                    If(len(v_vault_number+"1") < 6,true=SetVariable("v_vault_number",v_vault_number+"1"),
                    false=If(v_vault_number+"1" == v_vault_code_1,true=[SetField (persistent,"v_secrets_locked", False),SetVariable("v_vault_number",v_vault_number+"1")],
                    false=If(v_vault_number+"1" == v_vault_code_2,true=[SetField (persistent,"v_secrets_locked", False),SetField (persistent,"v_walkthrough_locked", False),SetVariable("v_vault_number",v_vault_number+"1")],
                    false=If(v_vault_number+"1" == v_vault_code_3,true=[SetField (persistent,"v_secrets_locked", False),SetField (persistent,"v_walkthrough_locked", False),SetField (persistent,"v_lewd_images_extra_locked", False),SetField (persistent,"v_sex_anim_enabled_locked", False),SetVariable("v_vault_number",v_vault_number+"1")],
                    false=SetVariable("v_vault_number",v_vault_number+"1")))))]


            imagebutton:
                auto "number_2_%s"
                action [
                    Play("sound2","sound effects/01/keypad_beep.ogg"),
                    If(len(v_vault_number+"2") < 6,true=SetVariable("v_vault_number",v_vault_number+"2"),
                    false=If(v_vault_number+"2" == v_vault_code_1,true=[SetField (persistent,"v_secrets_locked", False),SetVariable("v_vault_number",v_vault_number+"2")],
                    false=If(v_vault_number+"2" == v_vault_code_2,true=[SetField (persistent,"v_secrets_locked", False),SetField (persistent,"v_walkthrough_locked", False),SetVariable("v_vault_number",v_vault_number+"2")],
                    false=If(v_vault_number+"2" == v_vault_code_3,true=[SetField (persistent,"v_secrets_locked", False),SetField (persistent,"v_walkthrough_locked", False),SetField (persistent,"v_lewd_images_extra_locked", False),SetField (persistent,"v_sex_anim_enabled_locked", False),SetVariable("v_vault_number",v_vault_number+"2")],
                    false=SetVariable("v_vault_number",v_vault_number+"2")))))]


            imagebutton:
                auto "number_3_%s"
                action [
                    Play("sound2","sound effects/01/keypad_beep.ogg"),
                    If(len(v_vault_number+"3") < 6,true=SetVariable("v_vault_number",v_vault_number+"3"),
                    false=If(v_vault_number+"3" == v_vault_code_1,true=[SetField (persistent,"v_secrets_locked", False),SetVariable("v_vault_number",v_vault_number+"3")],
                    false=If(v_vault_number+"3" == v_vault_code_2,true=[SetField (persistent,"v_secrets_locked", False),SetField (persistent,"v_walkthrough_locked", False),SetVariable("v_vault_number",v_vault_number+"3")],
                    false=If(v_vault_number+"3" == v_vault_code_3,true=[SetField (persistent,"v_secrets_locked", False),SetField (persistent,"v_walkthrough_locked", False),SetField (persistent,"v_lewd_images_extra_locked", False),SetField (persistent,"v_sex_anim_enabled_locked", False),SetVariable("v_vault_number",v_vault_number+"3")],
                    false=SetVariable("v_vault_number",v_vault_number+"3")))))]

            imagebutton:
                auto "number_4_%s"
                action [
                    Play("sound2","sound effects/01/keypad_beep.ogg"),
                    If(len(v_vault_number+"4") < 6,true=SetVariable("v_vault_number",v_vault_number+"4"),
                    false=If(v_vault_number+"4" == v_vault_code_1,true=[SetField (persistent,"v_secrets_locked", False),SetVariable("v_vault_number",v_vault_number+"4")],
                    false=If(v_vault_number+"4" == v_vault_code_2,true=[SetField (persistent,"v_secrets_locked", False),SetField (persistent,"v_walkthrough_locked", False),SetVariable("v_vault_number",v_vault_number+"4")],
                    false=If(v_vault_number+"4" == v_vault_code_3,true=[SetField (persistent,"v_secrets_locked", False),SetField (persistent,"v_walkthrough_locked", False),SetField (persistent,"v_lewd_images_extra_locked", False),SetField (persistent,"v_sex_anim_enabled_locked", False),SetVariable("v_vault_number",v_vault_number+"4")],
                    false=SetVariable("v_vault_number",v_vault_number+"4")))))]
            imagebutton:
                auto "number_5_%s"
                action [
                    Play("sound2","sound effects/01/keypad_beep.ogg"),
                    If(len(v_vault_number+"5") < 6,true=SetVariable("v_vault_number",v_vault_number+"5"),
                    false=If(v_vault_number+"5" == v_vault_code_1,true=[SetField (persistent,"v_secrets_locked", False),SetVariable("v_vault_number",v_vault_number+"5")],
                    false=If(v_vault_number+"5" == v_vault_code_2,true=[SetField (persistent,"v_secrets_locked", False),SetField (persistent,"v_walkthrough_locked", False),SetVariable("v_vault_number",v_vault_number+"5")],
                    false=If(v_vault_number+"5" == v_vault_code_3,true=[SetField (persistent,"v_secrets_locked", False),SetField (persistent,"v_walkthrough_locked", False),SetField (persistent,"v_lewd_images_extra_locked", False),SetField (persistent,"v_sex_anim_enabled_locked", False),SetVariable("v_vault_number",v_vault_number+"5")],
                    false=SetVariable("v_vault_number",v_vault_number+"5")))))]
            imagebutton:
                auto "number_6_%s"
                action [
                    Play("sound2","sound effects/01/keypad_beep.ogg"),
                    If(len(v_vault_number+"6") < 6,true=SetVariable("v_vault_number",v_vault_number+"6"),
                    false=If(v_vault_number+"6" == v_vault_code_1,true=[SetField (persistent,"v_secrets_locked", False),SetVariable("v_vault_number",v_vault_number+"6")],
                    false=If(v_vault_number+"6" == v_vault_code_2,true=[SetField (persistent,"v_secrets_locked", False),SetField (persistent,"v_walkthrough_locked", False),SetVariable("v_vault_number",v_vault_number+"6")],
                    false=If(v_vault_number+"6" == v_vault_code_3,true=[SetField (persistent,"v_secrets_locked", False),SetField (persistent,"v_walkthrough_locked", False),SetField (persistent,"v_lewd_images_extra_locked", False),SetField (persistent,"v_sex_anim_enabled_locked", False),SetVariable("v_vault_number",v_vault_number+"6")],
                    false=SetVariable("v_vault_number",v_vault_number+"6")))))]
            imagebutton:
                auto "number_7_%s"
                action [
                    Play("sound2","sound effects/01/keypad_beep.ogg"),
                    If(len(v_vault_number+"7") < 6,true=SetVariable("v_vault_number",v_vault_number+"7"),
                    false=If(v_vault_number+"7" == v_vault_code_1,true=[SetField (persistent,"v_secrets_locked", False),SetVariable("v_vault_number",v_vault_number+"7")],
                    false=If(v_vault_number+"7" == v_vault_code_2,true=[SetField (persistent,"v_secrets_locked", False),SetField (persistent,"v_walkthrough_locked", False),SetVariable("v_vault_number",v_vault_number+"7")],
                    false=If(v_vault_number+"7" == v_vault_code_3,true=[SetField (persistent,"v_secrets_locked", False),SetField (persistent,"v_walkthrough_locked", False),SetField (persistent,"v_lewd_images_extra_locked", False),SetField (persistent,"v_sex_anim_enabled_locked", False),SetVariable("v_vault_number",v_vault_number+"7")],
                    false=SetVariable("v_vault_number",v_vault_number+"7")))))]
            imagebutton:
                auto "number_8_%s"
                action [
                    Play("sound2","sound effects/01/keypad_beep.ogg"),
                    If(len(v_vault_number+"8") < 6,true=SetVariable("v_vault_number",v_vault_number+"8"),
                    false=If(v_vault_number+"8" == v_vault_code_1,true=[SetField (persistent,"v_secrets_locked", False),SetVariable("v_vault_number",v_vault_number+"8")],
                    false=If(v_vault_number+"8" == v_vault_code_2,true=[SetField (persistent,"v_secrets_locked", False),SetField (persistent,"v_walkthrough_locked", False),SetVariable("v_vault_number",v_vault_number+"8")],
                    false=If(v_vault_number+"8" == v_vault_code_3,true=[SetField (persistent,"v_secrets_locked", False),SetField (persistent,"v_walkthrough_locked", False),SetField (persistent,"v_lewd_images_extra_locked", False),SetField (persistent,"v_sex_anim_enabled_locked", False),SetVariable("v_vault_number",v_vault_number+"8")],
                    false=SetVariable("v_vault_number",v_vault_number+"8")))))]
            imagebutton:
                auto "number_9_%s"
                action [
                    Play("sound2","sound effects/01/keypad_beep.ogg"),
                    If(len(v_vault_number+"9") < 6,true=SetVariable("v_vault_number",v_vault_number+"9"),
                    false=If(v_vault_number+"9" == v_vault_code_1,true=[SetField (persistent,"v_secrets_locked", False),SetVariable("v_vault_number",v_vault_number+"9")],
                    false=If(v_vault_number+"9" == v_vault_code_2,true=[SetField (persistent,"v_secrets_locked", False),SetField (persistent,"v_walkthrough_locked", False),SetVariable("v_vault_number",v_vault_number+"9")],
                    false=If(v_vault_number+"9" == v_vault_code_3,true=[SetField (persistent,"v_secrets_locked", False),SetField (persistent,"v_walkthrough_locked", False),SetField (persistent,"v_lewd_images_extra_locked", False),SetField (persistent,"v_sex_anim_enabled_locked", False),SetVariable("v_vault_number",v_vault_number+"9")],
                    false=SetVariable("v_vault_number",v_vault_number+"9")))))]
    if v_vault_number == "":
        textbutton _("RESET") xalign 0.78 yalign 0.27 text_style "vault_text_style"
    else:
        textbutton _("RESET") xalign 0.78 yalign 0.27 action SetVariable("v_vault_number","") text_style "vault_text_style"


    vbox:
        xalign 0.9
        yalign 0.5
        add "separator_short" alpha 0.2 xalign 0.6


        if persistent.v_secrets_locked:
            hbox:
                style_prefix "radio"
                button:
                    text _("Secret Scenes") style "vault_text_style"
                    xsize 450
                textbutton _("{color=#5e5e5e}LOCKED{/color}") action OpenURL(url="https://mrdotsgames.com/become-a-supporter") tooltip "Unlocks the ability to find secret scenes throughout the game.\nPlease subscribe to our $10 tier for the unlock code." text_style "vault_text_style"

        else:

            hbox:
                style_prefix "radio"
                button:
                    text _("Secret Scenes") style "vault_text_style"
                    xsize 450
                textbutton _("ON") action SetField(persistent,"v_secrets_enabled", True) tooltip "Secret scenes can be discovered, and will play when they have been." text_style "vault_text_style"
                textbutton _("/") text_style "vault_text_style"

                textbutton _("OFF") action [SetField(persistent,"v_secrets_enabled", False), Function(Reset_Secret_Values)] tooltip "Secret scenes cannot be discovered and will not play even if they have been previously discovered." text_style "vault_text_style"

            if persistent.v_secrets_enabled:
                add "separator_short" alpha 0.2 xalign 0.6

                hbox:
                    style_prefix "radio"
                    button:
                        text _("Secrets Icon Visible") style "vault_text_style"
                        xsize 450
                    textbutton _("ON") action SetField (persistent,"v_secrets_icon_enabled", True) tooltip "Show the icon in the corner of the game when the current scene has an unfound secret available." text_style "vault_text_style"
                    textbutton _("/") text_style "vault_text_style"
                    textbutton _("OFF") action [SetField(persistent,"v_secrets_icon_enabled", False),Function(Reset_Reappear_Value)] tooltip "Disable the secret icon." text_style "vault_text_style"



            if persistent.v_secrets_icon_enabled:
                add "separator_short" alpha 0.2 xalign 0.6

                hbox:
                    style_prefix "radio"
                    button:
                        text _("Secrets Icon Reappearing") style "vault_text_style"
                        xsize 450
                    textbutton _("ON") action SetField (persistent,"v_secrets_reappear", True) tooltip "Shows the secrets icon a scenes where the secret has already been discovered." text_style "vault_text_style"
                    textbutton _("/") text_style "vault_text_style"
                    textbutton _("OFF") action SetField (persistent,"v_secrets_reappear", False) tooltip "The secrets icon will remain hidden in scenes the secret has already been discovered." text_style "vault_text_style"

        add "separator_short" alpha 0.2 xalign 0.6

        if persistent.v_walkthrough_locked:

            hbox:
                style_prefix "radio"
                button:
                    text _("In-Game Walkthrough") style "vault_text_style"
                    xsize 450
                textbutton _("{color=#5e5e5e}LOCKED{/color}") action OpenURL(url="https://mrdotsgames.com/become-a-supporter") tooltip "Unlock the in game walkthrough. Please subscribe to our $15 tier for the unlock code." text_style "vault_text_style"

        else:
            hbox:
                style_prefix "radio"
                button:
                    text _("In-Game Walkthrough") style "vault_text_style"
                    xsize 450
                textbutton _("ON") action SetField (persistent,"v_walkthrough_enabled", True) tooltip "Enable the in-game walktrough." text_style "vault_text_style"
                textbutton _("/") text_style "vault_text_style"
                textbutton _("OFF") action SetField (persistent,"v_walkthrough_enabled", False) tooltip "Disable the in-game walktrough." text_style "vault_text_style"

        add "separator_short" alpha 0.2 xalign 0.6

        hbox:
            style_prefix "radio"
            button:
                text _("Basic Animations") style "vault_text_style"
                xsize 450
            textbutton _("ON") action SetField (persistent,"v_anim_enabled", True) tooltip "Enable animation animations (Sex based animations are excluded.)." text_style "vault_text_style"
            textbutton _("/") text_style "vault_text_style"
            textbutton _("OFF") action SetField (persistent,"v_anim_enabled", False) tooltip "Disable basic animations (Sex based animations are excluded.).\nNOTE: Not all animations will be disabled. Some are required for a scene to play correctly." text_style "vault_text_style"

        add "separator_short" alpha 0.2 xalign 0.6

        if persistent.v_sex_anim_enabled_locked:
            hbox:
                style_prefix "radio"
                button:
                    text _("Sex/Rolling Animations") style "vault_text_style"
                    xsize 450
                textbutton _("{color=#5e5e5e}LOCKED{/color}") action OpenURL(url="https://mrdotsgames.com/become-a-supporter") tooltip "Unlocks all the sex based animations and rolling images. Please subscribe to our $20 tier for the unlock code." text_style "vault_text_style"
        else:
            hbox:
                style_prefix "radio"
                button:
                    text _("Sex Animations") style "vault_text_style"
                    xsize 450
                textbutton _("ON") action SetField (persistent,"v_sex_anim_enabled", True) tooltip "Enable all sex based animations and rolling images." text_style "vault_text_style"
                textbutton _("/") text_style "vault_text_style"
                textbutton _("OFF") action SetField (persistent,"v_sex_anim_enabled", False) tooltip "Disable all sex based animations and rolling images." text_style "vault_text_style"

        add "separator_short" alpha 0.2 xalign 0.6

        if persistent.v_lewd_images_extra_locked:
            hbox:
                style_prefix "radio"
                button:
                    text _("Extra Lewd Images") style "vault_text_style"
                    xsize 450
                textbutton _("{color=#5e5e5e}LOCKED{/color}") action OpenURL(url="https://mrdotsgames.com/become-a-supporter") tooltip "Unlocks extra lewd images for the gallery. Please subscribe to our $20 tier for the unlock code." text_style "vault_text_style"


        else:
            hbox:
                style_prefix "radio"
                button:
                    text _("Extra Lewd Images") style "vault_text_style"
                    xsize 450
                textbutton _("ON") action SetField (persistent,"v_lewd_images_extra_enabled", True) tooltip "Enables extra lewd images for the gallery." text_style "vault_text_style"
                textbutton _("/") text_style "vault_text_style"
                textbutton _("OFF") action SetField (persistent,"v_lewd_images_extra_enabled", False) tooltip "Disables extra lewd images for the gallery." text_style "vault_text_style"

        add "separator_short" alpha 0.2 xalign 0.6

    if tooltip:
        text "[tooltip]" xalign 0.5 yalign 1.0

init python:
    def Reset_Secret_Values():
        setattr(store.persistent, "v_secrets_icon_enabled", False)
        setattr(store.persistent, "v_secrets_reappear", False)

    def Reset_Reappear_Value():
        setattr(store.persistent, "v_secrets_reappear", False)
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
