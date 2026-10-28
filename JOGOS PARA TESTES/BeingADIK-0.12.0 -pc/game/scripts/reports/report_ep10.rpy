label ep10_generate_report_text_label:
$ report_text = ""

if ep10_rolling:
    $ report_text += "• You decided to roll with Lily.\n\n"
elif (not ep10_rolling and ep9_lily_nicole_lewd and ep7_lily_lewd) or (not ep10_rolling and not ep9_lily_nicole_lewd and ep7_lily_lewd and branchAlone):
    $ report_text += "• You decided against rolling with Lily.\n\n"
elif branchAlone and ep8_quinn_lewd:
    if ep10_quinn_help:
        $ report_text += "• You told Quinn you'd still help her when she told you that she peddled drugs.\n\n"
    else:
        $ report_text += "• You told Quinn you didn't want to help her with her drug business.\n\n"

if ep8_midterms_cheated == "DIK":
    if ep10_bella_overreacting:
        $ report_text += "• Bella discovered that you cheated on your midterms ,and you told her that she was overreacting.\n\n"
    else:
        $ report_text += "• Bella discovered that you cheated on your midterms, and you promised you wouldn't do it again.\n\n"
elif ep8_midterms_cheated == "NEUTRAL":
    $ report_text += "• Bella discovered who cheated on the midterms.\n\n"
else:
    $ report_text += "• Bella didn't discover who cheated on the midterms.\n\n"

if ep10_jm_solo == "Maya":
    if ep10_feelingsForMaya:
        $ report_text += "• You spent some quality time with Maya and told her about your feelings for her.\n\n"
    else:
        $ report_text += "• You spent some quality time with Maya.\n\n"
else:
    if branchMayaJosy:
        $ report_text += "• You spent some quality time with Josy.\n\n"
    else:
        if ep10_feelingsForJosy:
            $ report_text += "• You spent some quality time with Josy, and you told each other about your feelings for one another.\n\n"
        elif branchAlone and not ep10_feelingsForJosy:
            $ report_text += "• You spent some quality time with Josy and told her you're over her.\n\n"
        else:
            $ report_text += "• You spent some quality time with Josy, and she told you she still has feelings for you.\n\n"

if branchJill:
    $ report_text += "• You met Jill's parents and saw Jill's childhood home.\n\n"
elif branchSage:
    if not ep9_sage_vanilla and ep10_sage_lewd:
        $ report_text += "• You went out on a date with Sage, and she blew you in the movie theater.\n\n"
    else:
        $ report_text += "• You went out on a classic date with Sage.\n\n"
elif branchIsabella:
    $ report_text += "• You spent time with Bella and deepened your relationship with her.\n\n"
elif branchMayaJosy:
    $ report_text += "• Josy and Maya seem interested in playing The Dare Game with you.\n\n"
elif branchAlone:
    if ep10_rejected_nicole:
        $ report_text += "• You told Nicole that you weren't ready to date her because she's got a kid.\n\n"
    elif ep10_date_nicole and ep10_cancel_date_nicole:
        $ report_text += "• You told Nicole that you wanted to date her but canceled on her to date Nora.\n\n"
    elif ep10_date_nicole:
        $ report_text += "• You dated Nicole and got to know more about her past.\n\n"
    elif ep10_dating_nora:
        $ report_text += "• You dated Nora, but after she found out you were a student in her class, she broke up with you.\n\n"
    elif ep10_cathy_lewd:
        $ report_text += "• You went back to Cathy's place for coffee and finally fucked her.\n\n"

if ep10_shroom_choice == "DIK":
    $ report_text += "• At the BBQ party, you ate a mushroom and encouraged others to have one too.\n\n"
elif ep10_shroom_choice == "NEUTRAL":
    $ report_text += "• At the BBQ party, you didn't eat a mushroom.\n\n"
else:
    $ report_text += "• At the BBQ party, you tried to discourage your brothers from eating mushrooms.\n\n"

if ep10_zoey_jacob:
    $ report_text += "• You told Jacob it was cool for him to hook up with Zoey.\n\n"
else:
    $ report_text += "• You told Jacob you didn't want him to hook up with Zoey.\n\n"

if ep10_patrick_choice == "DIK":
    $ report_text += "• You punched Patrick when he was being rough with Maya.\n\n"
elif ep10_patrick_choice == "NEUTRAL":
    $ report_text += "• You confronted Patrick when he was being rough with Maya.\n\n"
else:
    $ report_text += "• You defused the situation when Patrick was being rough with Maya.\n\n"

if ep10_got_contracts:
    $ report_text += "• You stole the contract from Patrick at Thanksgiving.\n\n"
else:
    $ report_text += "• You didn't steal the contract from Patrick at Thanksgiving.\n\n"






show screen ep10_report_screen
$ renpy.pause()
jump ep10EndLabel

image spr_ep10_bella_solo6:
    "ep10_bella_solo6" with Dissolve(0.2, alpha=True)
    zoom 1.0
    xalign 0.0 yalign 0.0
    linear 15.0 zoom 1.08
    linear 15.0 zoom 1.00
    repeat

image spr_ep10_sage_date49:
    "ep10_sage_date49" with Dissolve(0.2, alpha=True)
    zoom 1.0
    xalign 0.0 yalign 0.0
    linear 15.0 zoom 1.08
    linear 15.0 zoom 1.00
    repeat

image spr_ep10_jill_solo41:
    "ep10_jill_solo41" with Dissolve(0.2, alpha=True)
    zoom 1.0
    xalign 0.0 yalign 0.0
    linear 15.0 zoom 1.08
    linear 15.0 zoom 1.00
    repeat

image spr_ep10_josy_solo_pic2:
    "ep10_josy_solo_pic2" with Dissolve(0.2, alpha=True)
    zoom 1.0
    xalign 0.0 yalign 0.0
    linear 15.0 zoom 1.08
    linear 15.0 zoom 1.00
    repeat

image spr_ep10_maya_solo_pic1:
    "ep10_maya_solo_pic1" with Dissolve(0.2, alpha=True)
    zoom 1.0
    xalign 0.0 yalign 0.0
    linear 15.0 zoom 1.08
    linear 15.0 zoom 1.00
    repeat

image spr_ep10_quinn_dt46:
    "ep10_quinn_dt46" with Dissolve(0.2, alpha=True)
    zoom 1.0
    xalign 0.0 yalign 0.0
    linear 15.0 zoom 1.08
    linear 15.0 zoom 1.00
    repeat

screen ep10_report_screen:
    tag ep10_report_screen
    modal True
    if branchIsabella:
        add "spr_ep10_bella_solo6"
    elif branchSage:
        add "spr_ep10_sage_date49"
    elif branchJill:
        add "spr_ep10_jill_solo41"
    elif branchMayaJosy:
        if ep10_jm_solo == "Josy":
            add "spr_ep10_josy_solo_pic2"
        else:
            add "spr_ep10_maya_solo_pic1"
    else:
        if ep10_quinn_help:
            add "spr_ep10_quinn_dt46"
        elif ep10_date_nicole and not ep10_cancel_date_nicole:
            add "anim_envy_kiss_ep10"
        elif ep10_riona_date:
            add "anim_riona_kiss_ep10"
        elif ep10_rolling:
            add "anim_lily_kiss_ep10"
        else:
            add "anim_bbq_intro_ep10"
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
        if not branchAlone:
            xoffset -1060 * persistent.scale_factor
        else:
            xoffset -1200 * persistent.scale_factor

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
        action (Hide("ep10_report_screen"),Jump("ep10EndLabel"))

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
