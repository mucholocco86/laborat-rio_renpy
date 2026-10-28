label ep11_generate_report_text_label:
$ report_text = ""

if ep11_tommy_admit:
    $ report_text += "• You nudged Nick to come clean when the DIKs fought.\n\n"
else:
    $ report_text += "• You kept Nick's secret when the DIKs fought.\n\n"

if branchJill or ep9_b_kissed_jill:
    $ report_text += "• Jill showed you Lana's grave and told you how she died.\n\n"

if branchIsabella:
    $ report_text += "• Bella told you she lied about the B&R handbook. Your relationship isn't allowed at B&R.\n\n"

if branchSage and jade_state > 0:
    $ report_text += "• You confided in Derek about your fears regarding Sage and Jade.\n\n"

if branchMayaJosy:
    if wt_ep11_maya_josy:
        
            $ report_text += "• You spent time alone with Josy and were introduced to her mom.\n\n"
            if ep11_josy_love == 2:
                $ report_text += "• You told Josy you loved her and she reciprocated.\n\n"
            elif ep11_josy_love == 1:
                $ report_text += "• You told Josy you loved her but she didn't say it back.\n\n"
        
            $ report_text += "• You spent time alone with Maya and learned about her fears.\n\n"
            if ep11_maya_love == 2:
                $ report_text += "• You told Maya you loved her and she reciprocated.\n\n"
            elif ep11_maya_love == 2:
                $ report_text += "• You told Maya you loved her but she didn't say it back.\n\n"
    else:
        if ep11_josy_solo:
            $ report_text += "• You spent time alone with Josy and were introduced to her mom.\n\n"
            if ep11_josy_love == 2:
                $ report_text += "• You told Josy you loved her and she reciprocated.\n\n"
            elif ep11_josy_love == 1:
                $ report_text += "• You told Josy you loved her but she didn't say it back.\n\n"
        else:
            $ report_text += "• You spent time alone with Maya and learned about her fears.\n\n"
            if ep11_maya_love == 2:
                $ report_text += "• You told Maya you loved her and she reciprocated.\n\n"
            elif ep11_maya_love == 2:
                $ report_text += "• You told Maya you loved her but she didn't say it back.\n\n"

if branchAlone and jade_state == 1 and ep11_jade_care:
    $ report_text += "• Despite your concerns about Sage, you found Jade irresistible and continued having sex with her.\n\n"

if ep11_fighter:
    $ report_text += "• You were asked to enter a fighting competition and accepted.\n\n"
elif ep11_music:
    $ report_text += "• You agreed to perform at the faculty's Christmas party.\n\n"
elif not ep8_recital_failed:
    $ report_text += "• You declined to perform at the faculty's Christmas party and to enter a fighting competition.\n\n"
else:
    $ report_text += "• You declined to enter a fighting competition.\n\n"

if ep11_invited_tara:
    if ep11_tara_attitude > 1:
        $ report_text += "• You were mean to Tara but ultimately invited her to the party.\n\n"
    else:
        $ report_text += "• You listened to Tara and invited her to the party.\n\n"
else:
    if ep11_tara_attitude > 1:
        $ report_text += "• You were mean to Tara and didn't invite her to the party.\n\n"
    else:
        $ report_text += "• You listened to Tara but didn't invite her to the party.\n\n"
if ep11_kp_choice == "DIK":
    $ report_text += "• You pulled a mean prank on Kylie and Penny.\n\n"
elif ep11_kp_choice == "NEUTRAL":
    $ report_text += "• You let Leon and Jacob handle Kylie and Penny.\n\n"
else:
    $ report_text += "• You confronted Kylie and Penny at the party.\n\n"

if branchAlone and ep10_rolling:
    
    if ep11_nicole_dating and ep11_rolling:
        
            if ep11_lily_want_more:
                $ report_text += "• You wanted the rolling with Lily to turn into something more.\n\n"
            else:
                $ report_text += "• You liked rolling with Lily without any feelings or strings attached.\n\n"
    
    else:
        if ep11_rolling:
            if ep11_lily_want_more:
                $ report_text += "• You wanted the rolling with Lily to turn into something more.\n\n"
            else:
                $ report_text += "• You liked rolling with Lily without any feelings or strings attached.\n\n"
        if ep10_date_nicole and not ep10_cancel_date_nicole:
            if ep11_nicole_over_lily:
                $ report_text += "• You quit rolling with Lily to keep dating Nicole.\n\n"
            else:
                $ report_text += "• You quit dating Nicole to keep rolling with Lily.\n\n"

if ep10_quinn_help:
    $ report_text += "• Quinn confided in you and opened up about her tragic past and present.\n\n"

if ep11_zoey_kiss == 2:
    $ report_text += "• Your heart gravitated back to Zoey after she declared her love.\n\n"
elif ep11_zoey_kiss == 1:
    $ report_text += "• It was hard, but you rejected Zoey after she declared her love.\n\n"
else:
    $ report_text += "• You rejected Zoey after she declared her love.\n\n"

if not branchAlone or (branchAlone and wt_ep9_branch_numbers != 1):
    if wt_ep11_party_bella:
        $ report_text += "• You left the Christmas Panty Party to party at Bella's.\n\n"
    else:
        if ep11_mg_party and ep11_zoey_kiss != 2:
            $ report_text += "• You left the Christmas Panty Party to party at Bella's.\n\n"
        elif ep11_mg_party and ep11_zoey_kiss == 2:
            $ report_text += "• You planned on leaving the Christmas Panty Party to party at Bella's, but didn't.\n\n"
        else:
            $ report_text += "• You stayed at the Christmas Panty Party instead of going to Bella's.\n\n"
        
if "Sage couch" in tmp_mod_list and "Sage Camila" in tmp_mod_list:

    if ep11_sage_love == 2:
        $ report_text += "• You told Sage you loved her and she reciprocated.\n\n"
    elif ep11_sage_love == 1:
        $ report_text += "• You told Sage you loved her but she didn't say it back.\n\n"
    if ep11_sage_camila_lewd:
        $ report_text += "• You had a threesome with Sage and Camila.\n\n"
else:
    if ep11_sage_love == 2:
        $ report_text += "• You told Sage you loved her and she reciprocated.\n\n"
    elif ep11_sage_love == 1:
        $ report_text += "• You told Sage you loved her but she didn't say it back.\n\n"
    elif ep11_sage_camila_lewd:
        $ report_text += "• You had a threesome with Sage and Camila.\n\n"

if branchJill and (ep11_zoey_kiss < 2 or wt_ep11_zoey_kiss_others):
    $ report_text += "• You pushed Jill's boundaries and had sex in public.\n\n"
if wt_ep9_branch_numbers != 1:
    $ report_text = report_text.replace("\n\n","\n")




show screen ep11_report_screen
$ renpy.pause()
jump ep11EndLabel

image spr_ep11_cabin_sauna_event217:
    "ep11_cabin_sauna_event217" with Dissolve(0.2, alpha=True)
    zoom 1.0
    xalign 0.0 yalign 0.0
    linear 15.0 zoom 1.08
    linear 15.0 zoom 1.00
    repeat

image spr_ep11_home81:
    "ep11_home81" with Dissolve(0.2, alpha=True)
    zoom 1.0
    xalign 0.0 yalign 0.0
    linear 15.0 zoom 1.08
    linear 15.0 zoom 1.00
    repeat

image spr_ep11_trip224:
    "ep11_trip224" with Dissolve(0.2, alpha=True)
    zoom 1.0
    xalign 0.0 yalign 0.0
    linear 15.0 zoom 1.08
    linear 15.0 zoom 1.00
    repeat

image spr_ep11_jsolo86:
    "ep11_jsolo86" with Dissolve(0.2, alpha=True)
    zoom 1.0
    xalign 0.0 yalign 0.0
    linear 15.0 zoom 1.08
    linear 15.0 zoom 1.00
    repeat

image spr_ep11_msolo23:
    "ep11_msolo23" with Dissolve(0.2, alpha=True)
    zoom 1.0
    xalign 0.0 yalign 0.0
    linear 15.0 zoom 1.08
    linear 15.0 zoom 1.00
    repeat

image spr_ep11_pp_nl_event36:
    "ep11_pp_nl_event36" with Dissolve(0.2, alpha=True)
    zoom 1.0
    xalign 0.0 yalign 0.0
    linear 15.0 zoom 1.08
    linear 15.0 zoom 1.00
    repeat
image spr_ep11_pp_zoey_end45:
    "ep11_pp_zoey_end45" with Dissolve(0.2, alpha=True)
    zoom 1.0
    xalign 0.0 yalign 0.0
    linear 15.0 zoom 1.08
    linear 15.0 zoom 1.00
    repeat
image spr_ep11_fr_deco_lily_event45:
    "ep11_fr_deco_lily_event45" with Dissolve(0.2, alpha=True)
    zoom 1.0
    xalign 0.0 yalign 0.0
    linear 15.0 zoom 1.08
    linear 15.0 zoom 1.00
    repeat
image spr_ep11_jade_pre_lewd19:
    "ep11_jade_pre_lewd19" with Dissolve(0.2, alpha=True)
    zoom 1.0
    xalign 0.0 yalign 0.0
    linear 15.0 zoom 1.08
    linear 15.0 zoom 1.00
    repeat
image spr_ep11_lab19:
    "ep11_lab19" with Dissolve(0.2, alpha=True)
    zoom 1.0
    xalign 0.0 yalign 0.0
    linear 15.0 zoom 1.08
    linear 15.0 zoom 1.00
    repeat

screen ep11_report_screen:
    tag ep11_report_screen
    modal True
    if ep11_zoey_kiss == 2:
        add "spr_ep11_pp_zoey_end45"
    elif branchIsabella:
        add "spr_ep11_cabin_sauna_event217"
    elif branchSage:
        add "spr_ep11_home81"
    elif branchJill:
        add "spr_ep11_trip224"
    elif branchMayaJosy:
        if ep11_josy_solo:
            add "spr_ep11_jsolo86"
        else:
            add "spr_ep11_msolo23"
    else:
        if ep10_quinn_help and False not in ep11_quinn_question:
            add "ep11_pp_quinn2_event3"
        elif ep11_lily_want_more and ep11_rolling:
            add "spr_ep11_fr_deco_lily_event45"
        elif ep11_jade_lewd:
            add "spr_ep11_jade_pre_lewd19"
        elif ep10_date_nicole and not ep10_cancel_date_nicole and (ep11_nicole_over_lily or not ep10_rolling):
            add "spr_ep11_pp_nl_event36"
        else:
            add "spr_ep11_lab19"
    add "character_report"

    imagebutton:
        if affinity == "CHICK":
            idle "mphone_bios_big_mc1"
            hover "mphone_bios_big_mc1"
        elif affinity == "DIK":
            idle "mphone_bios_big_mc2"
            hover "mphone_bios_big_mc2"
        else:
            idle "mphone_bios_big_mc3"
            hover "mphone_bios_big_mc3"
        action NullAction()
        xalign 0.0
        yalign 0.5
        yoffset -3 * persistent.scale_factor
        if not branchAlone or ep11_zoey_kiss == 2:
            xoffset -1060 * persistent.scale_factor
        else:
            xoffset -1200 * persistent.scale_factor

    if ep11_zoey_kiss == 2:
        imagebutton at show_slow:
            idle "mphone_bios_big_zoey"
            hover "mphone_bios_big_zoey"
            action NullAction()
            xalign 0.0
            yalign 0.5
            xoffset -1250 * persistent.scale_factor
            yoffset -3 * persistent.scale_factor
        if branchSage:
            imagebutton at hide_slow:
                idle "mphone_bios_big_sage"
                hover "mphone_bios_big_sage"
                action NullAction()
                xalign 0.0
                yalign 0.5
                xoffset -1300 * persistent.scale_factor
                yoffset -3 * persistent.scale_factor
        if branchJill:
            imagebutton at hide_slow:
                idle "mphone_bios_big_jill"
                hover "mphone_bios_big_jill"
                action NullAction()
                xalign 0.0
                yalign 0.5
                xoffset -1300 * persistent.scale_factor
                yoffset -3 * persistent.scale_factor
        if branchIsabella:
            imagebutton at hide_slow:
                idle "mphone_bios_big_isabella"
                hover "mphone_bios_big_isabella"
                action NullAction()
                xalign 0.0
                yalign 0.5
                xoffset -1300 * persistent.scale_factor
                yoffset -3 * persistent.scale_factor
        if branchMayaJosy:
            imagebutton at hide_slow:
                idle "mphone_bios_big_maya"
                hover "mphone_bios_big_maya"
                action NullAction()
                xalign 0.0
                yalign 0.5
                xoffset -1390 * persistent.scale_factor
                yoffset -3 * persistent.scale_factor
            imagebutton at hide_slow2:
                idle "mphone_bios_big_josy"
                hover "mphone_bios_big_josy"
                action NullAction()
                xalign 0.0
                yalign 0.5
                xoffset -1140 * persistent.scale_factor
                yoffset 14 * persistent.scale_factor
    else:
        if branchSage:
            imagebutton:
                idle "mphone_bios_big_sage"
                hover "mphone_bios_big_sage"
                action NullAction()
                xalign 0.0
                yalign 0.5
                xoffset -1300 * persistent.scale_factor
                yoffset -3 * persistent.scale_factor
        if branchJill:
            imagebutton:
                idle "mphone_bios_big_jill"
                hover "mphone_bios_big_jill"
                action NullAction()
                xalign 0.0
                yalign 0.5
                xoffset -1300 * persistent.scale_factor
                yoffset -3 * persistent.scale_factor
        if branchIsabella:
            imagebutton:
                idle "mphone_bios_big_isabella"
                hover "mphone_bios_big_isabella"
                action NullAction()
                xalign 0.0
                yalign 0.5
                xoffset -1300 * persistent.scale_factor
                yoffset -3 * persistent.scale_factor
        if branchMayaJosy:
            imagebutton:
                idle "mphone_bios_big_maya"
                hover "mphone_bios_big_maya"
                action NullAction()
                xalign 0.0
                yalign 0.5
                xoffset -1390 * persistent.scale_factor
                yoffset -3 * persistent.scale_factor
            imagebutton at transform_zoom90:
                idle "mphone_bios_big_josy"
                hover "mphone_bios_big_josy"
                action NullAction()
                xalign 0.0
                yalign 0.5
                xoffset -1140 * persistent.scale_factor
                yoffset 14 * persistent.scale_factor

    imagebutton:
        idle "report_screen_button"
        hover "report_screen_button"
        action (Hide("ep11_report_screen"),Jump("ep11EndLabel"))

    hbox:
        xalign 1.0
        yalign 0.8
        xoffset -60 * persistent.scale_factor
        xminimum 1130 * persistent.scale_factor
        xmaximum 1130 * persistent.scale_factor
        yminimum 720 * persistent.scale_factor
        ymaximum 720 * persistent.scale_factor
        text "[report_text]" style "report_screen_style"
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
