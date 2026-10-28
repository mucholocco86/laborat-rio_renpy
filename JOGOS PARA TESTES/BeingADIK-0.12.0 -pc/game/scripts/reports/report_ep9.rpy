label ep9_generate_report_text_label:
$ report_text = ""
if ep9_mad_at_zoey:
    $ report_text += "• You told Zoey you were mad at her.\n\n"
else:
    $ report_text += "• You told Zoey your feelings were all over the place.\n\n"

if ep9_derek_better_friend:
    $ report_text += "• You told Derek he is a better friend than Zoey.\n\n"
else:
    $ report_text += "• You told Derek that Zoey is a better friend than him.\n\n"

if branchIsabella and not branchJill:
    if ep8_jill_state == 1:
        if ep9_b_kissed_jill:
            $ report_text += "• When breaking up with Jill, she kissed you, and you kissed her back.\n\n"
        else:
            $ report_text += "• You broke up with Jill and tried to make her understand your choice.\n\n"
    else:
        $ report_text += "• You got closure with Jill and talked to her about you and Bella.\n\n"

if ep9_josy_choice == "DIK":
    $ report_text += "• You punched Oscar after he insulted Josy.\n\n"
elif ep9_josy_choice == "CHICK":
    $ report_text += "• You comforted Josy after Oscar insulted her.\n\n"
else:
    $ report_text += "• You threw Oscar out of the party after he insulted Josy.\n\n"

if ep9_heather_lewd == 2:
    $ report_text += "• You got a blowjob and a boobjob from Heather.\n\n"

if ep9_prep_truce:
    $ report_text += "• You let the preps inside at the party.\n\n"
else:
    $ report_text += "• You didn't let the preps inside at the party.\n\n"

if ep9_riona_choice == "CHICK":
    $ report_text += "• You rejected Riona's advances at the Halloween party.\n\n"
elif ep9_riona_choice == "NEUTRAL":
    $ report_text += "• You told Riona that you were in a relationship at the Halloween party.\n\n"
elif ep9_riona_choice == "DIK":
    $ report_text += "• You made out with Riona at the Halloween party.\n\n"

if ep9_vinny_choice == "DIK":
    $ report_text += "• You punched Vinny and wanted to fight him.\n\n"
elif ep9_vinny_choice == "CHICK":
    $ report_text += "• You tried to defuse the situation with Vinny.\n\n"
else:
    $ report_text += "• You confronted Vinny and threatened him.\n\n"

if branchAlone and not wt_ep9_branch_numbers < 2:
    if ep9_sarah_melanie_lewd:
        $ report_text += "• You ended the night with Sarah and Melanie.\n\n"
    elif ep9_lily_nicole_lewd:
        $ report_text += "• You ended the night with Lily and Nicole.\n\n"
    elif ep9_quinn_lewd:
        $ report_text += "• You ended the night with Quinn.\n\n"
    elif ep9_tiffani_gina_tara:
        $ report_text += "• You ended the night in bed with Tiffani, Tara & Gina.\n\n"
    elif wt_ep9_branch_numbers < 2:
        $ report_text += "• You ended the night on your couch.\n\n"
if branchSage and wt_ep9_end_pick=="Sage":
    $ report_text += "• You had anal sex with Sage and ended the night with her in your bed.\n\n"
if branchIsabella and wt_ep9_end_pick=="Bella":
    $ report_text += "• You had sex with Bella and ended the night with her in your bed.\n\n"
if branchMayaJosy  and wt_ep9_end_pick=="Maya":
    $ report_text += "• You had a threesome with Maya and Josy and ended the night with them.\n\n"
if branchJill  and wt_ep9_end_pick=="Jill":
    if ep9_told_jill:
        $ report_text += "• You told Jill that you saw Matthew cheating on Bianca with Olivia.\n\n"
    else:
        $ report_text += "• You didn't tell Jill that you saw Matthew cheating on Bianca with Olivia.\n\n"
    $ report_text += "• You had sex with Jill and ended the night with her in your bed.\n\n"

if ep9_jm_sad:
    $ report_text += "• You broke up with Josy and Maya and made them sad.\n\n"





show screen ep9_report_screen
$ renpy.pause()
jump ep9EndLabel

image spr_ep9_jm_committing17:
    "ep9_jm_committing17" with Dissolve(0.2, alpha=True)
    zoom 1.0
    xalign 0.0 yalign 0.0
    linear 15.0 zoom 1.08
    linear 15.0 zoom 1.00
    repeat

image spr_ep9_ending_sage10:
    "ep9_ending_sage10" with Dissolve(0.2, alpha=True)
    zoom 1.0
    xalign 0.0 yalign 0.0
    linear 15.0 zoom 1.08
    linear 15.0 zoom 1.00
    repeat

screen ep9_report_screen:

    modal True tag ep9_report_screen
    if branchIsabella and wt_ep9_end_pick=="Bella":
        add "anim_bella_kiss3_ep9"
    elif branchSage and wt_ep9_end_pick=="Sage":
        add "spr_ep9_ending_sage10"
    elif branchJill  and wt_ep9_end_pick=="Jill":
        add "anim_jill_branch_ep9"
    elif branchMayaJosy and wt_ep9_end_pick=="Maya":
        add "spr_ep9_jm_committing17"
    
    elif ep9_quinn_lewd and wt_ep9_end_pick=="Quinn":
            add "ep9_quinn_lewd77"
    elif ep9_spoon_lily  and wt_ep9_end_pick=="Lily":
            add "ep9_lily_nicole_lewd70"
    elif ep9_spoon_nicole  and wt_ep9_end_pick=="Lily":
            add "ep9_ending_nicole_lily12"
    elif ep9_kissed_rio and wt_ep9_end_pick =="Other":
            add "anim_riona_kiss_ep9"
    else:
            add "anim_rain_ep9"
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
        action (Hide("ep9_report_screen"),Jump("ep9EndLabel"))

    hbox:
        xalign 1.0
        yalign 0.8
        xoffset -60 * persistent.scale_factor
        xminimum 1130 * persistent.scale_factor
        xmaximum 1130 * persistent.scale_factor
        yminimum 720 * persistent.scale_factor
        ymaximum 720 * persistent.scale_factor
        text "[report_text]" style "report_screen_style"

style report_screen_style:
    font "fonts/candara.ttf"
    size 32 * persistent.scale_factor
    color "ffed00"
    outlines [(2, "#000000", 0, 0)]

transform transform_zoom90:
    zoom 0.96
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
