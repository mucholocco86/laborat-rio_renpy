screen pp_dik_budget_screen:
    tag pp_dik_budget_screen
    modal False
    imagebutton at show_hide_dissolve:
        idle "bg_toprightmsg"
        xalign 0.9825
        yalign -0.01
        action NullAction()
    text "{size=%d}{color=#ffffff}Party budget:{/color} $%d{/size}" % (34 * persistent.scale_factor,pp_money) style "pp_style_nm_header" xalign 0.97 yalign 0.012 at show_hide_dissolve

screen pp_dik_preferences_screen:
    tag pp_dik_preferences_screen
    modal False

    text "What the DIKs want" style "pp_style_nm_header" xalign 0.88 yalign 0.04
    vbox:
        xalign 0.98 yalign 0.15
        spacing 20 * persistent.scale_factor
        hbox:
            spacing 20 * persistent.scale_factor
            for i in range(0,4):
                vbox:
                    imagebutton:
                        idle "pp_%s_%d_idle" % (pp_dik_list[i],pp_nm_dik_happiness[i])
                        hover "pp_%s_%d_idle" % (pp_dik_list[i],pp_nm_dik_happiness[i])
                        action NullAction()
                    text "%s" % pp_nm_activity_description[currentActivity][pp_nm_party_preference[i][currentActivity]] style "pp_style_nm_text" xalign 0.5
        hbox:
            spacing 20 * persistent.scale_factor
            for i in range(4,8):
                vbox:
                    imagebutton:
                        idle "pp_%s_%d_idle" % (pp_dik_list[i],pp_nm_dik_happiness[i])
                        hover "pp_%s_%d_idle" % (pp_dik_list[i],pp_nm_dik_happiness[i])
                        action NullAction()
                    text "%s" % pp_nm_activity_description[currentActivity][pp_nm_party_preference[i][currentActivity]] style "pp_style_nm_text" xalign 0.5

    text "{size=-%d}Party budget: $%d{/size}" % ((10 * persistent.scale_factor),pp_money) style "pp_style_nm_header" xalign 0.98 yalign 0.5


style pp_style_nm_header:
    font "fonts/cabin-regular.ttf"
    color "#fe9416"
    size 35 * persistent.scale_factor
    outlines [(2, "#000000", 0, 0)]

style pp_style_nm_text:
    font "fonts/cabin-regular.ttf"
    color "#ffffff"
    size 20 * persistent.scale_factor
    outlines [(2, "#000000", 0, 0)]
    xmaximum 140 * persistent.scale_factor
    xminimum 140 * persistent.scale_factor
    yminimum 80 * persistent.scale_factor
    text_align 0.5

screen pp_nm_happiness_screen:
    tag pp_nm_happiness_screen
    modal False

    text "DIKs' Happiness" style "pp_style_nm_header" xalign 0.88 yalign 0.04
    vbox:
        xalign 0.98 yalign 0.2
        spacing 10 * persistent.scale_factor
        hbox:
            spacing 20 * persistent.scale_factor
            for i in range(0,4):
                vbox:
                    imagebutton:
                        idle "pp_%s_%d_idle" % (pp_dik_list[i],pp_nm_tmp_happiness[i])
                        hover "pp_%s_%d_idle" % (pp_dik_list[i],pp_nm_tmp_happiness[i])
                        action NullAction()
                    imagebutton:
                        idle "pp_happiness%d" % pp_nm_tmp_happiness[i]
                        hover "pp_happiness%d" % pp_nm_tmp_happiness[i]
                        action NullAction()

        hbox:
            spacing 20 * persistent.scale_factor
            for i in range(4,8):
                vbox:
                    imagebutton:
                        idle "pp_%s_%d_idle" % (pp_dik_list[i],pp_nm_tmp_happiness[i])
                        hover "pp_%s_%d_idle" % (pp_dik_list[i],pp_nm_tmp_happiness[i])
                        action NullAction()
                    imagebutton:
                        idle "pp_happiness%d" % pp_nm_tmp_happiness[i]
                        hover "pp_happiness%d" % pp_nm_tmp_happiness[i]
                        action NullAction()
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
