label ep12_generate_report_text_label:
$ report_text = ""

if branchAlone and ep11_rolling and not branchZoey and not ep11_nicole_over_lily:
    if ep12_rolling:
        $ report_text += "• You told Lily you felt something more for her, and she felt conflicted about it.\n\n"
    else:
        $ report_text += "• You stopped rolling with Lily.\n\n"

if breakup:
    if "Isabella" in breakup:
        if branchZoey:
            $ report_text += "• You and Bella broke up, and you reunited with Zoey.\n\n"
        elif ep4_toldDerekAboutJade:
            $ report_text += "• Bella broke up with you because of what you did with Jade.\n\n"
    elif "Jill" in breakup:
        if branchZoey:
            $ report_text += "• You and Jill broke up, and you reunited with Zoey.\n\n"
        elif ep4_toldDerekAboutJade:
            $ report_text += "• Jill broke up with you because of what you did with Jade.\n\n"
        elif ep12_mc_slut:
            $ report_text += "• Jill broke up with you after learning about your extensive sexual history.\n\n"
        elif tc > 4:
            $ report_text += "• You broke up with Jill because you failed to stay faithful to her.\n\n"
    elif "Sage" in breakup:
        if ep4_toldDerekAboutJade:
            $ report_text += "• Sage broke up with you after learning what you did with Jade.\n\n"
        elif branchZoey:
            $ report_text += "• You and Sage broke up, and you reunited with Zoey.\n\n"
        elif branchSage and ep12_break_or_tell == "break":
            $ report_text += "• You broke up with Sage without giving her a real reason.\n\n"
        elif branchSage and ep12_break_or_tell == "tell":
            $ report_text += "• Sage broke up with you after you told her what you did with Jade.\n\n"
        elif tc > 4:
            $ report_text += "• You broke up with Sage because you didn't feel enough to truly commit to her.\n\n"
        elif ep11_sage_love == 1 or RPsage < 22:
            $ report_text += "• Sage broke up with you because she didn't feel enough for you.\n\n"
        elif ep12_zoey_friend:
            $ report_text += "• Sage broke up with you because you chose to stay friends with Zoey.\n\n"
    elif "Josy" in breakup or "Maya" in breakup:
        if branchZoey:
            $ report_text += "• You parted ways with Josy and Maya, then reunited with Zoey.\n\n"
        elif tc > 4:
            $ report_text += "• You broke up with Josy and Maya because you failed to stay faithful.\n\n"
        else:
            $ report_text += "• You broke up with Josy and Maya because they didn't feel enough for you.\n\n"
elif roadZoey:
    $ report_text += "• You reunited with Zoey.\n\n"

if roadZoey and ep12_nicole_breakup:
    $ report_text += "• You stopped dating Nicole to be with Zoey.\n\n"
elif ep12_nicole_path and ep12_nicole_dating > 0 and ep12_nicole_breakup:
    if ep12_nicole_dating == 2:
        $ report_text += "• Nicole rejected you after learning that you had a threesome with Sandy and Tania.\n\n"
    else:
        $ report_text += "• Nicole rejected you after talking to Sandy about your intentions to have sex with her.\n\n"

if ep12_riona_side == "Quinn":
    $ report_text += "• When Riona confided in you, you tried to get her to patch things up with Quinn.\n\n"
else:
    $ report_text += "• When Riona confided in you, you told her to stay away from Quinn.\n\n"

if not branchZoey and branchIsabella and not ep4_toldDerekAboutJade:
    if roadIsabella:
        $ report_text += "• You had a long and serious talk with Bella about her past and your relationship. It reaffirmed your love for one another.\n\n"
    elif "Isabella" in breakup:
        $ report_text += "• You decided to break up with Bella because you failed to stay faithful to her.\n\n"

if ep12_offered_room == "DIK":
    $ report_text += "• You refused to give up a part of your room so that more DIKs can join the fraternity.\n\n"
elif ep12_offered_room == "NEUTRAL":
    $ report_text += "• You didn't speak your mind on giving up a part of your room so that more DIKs can join the fraternity.\n\n"
else:
    $ report_text += "• You offered to give up a part of your room so that more DIKs can join the fraternity.\n\n"

if ep12_brawler_comp_won:
    $ report_text += "• You fought in the fighting competition and won.\n\n"
elif ep11_fighter:
    $ report_text += "• You fought in the fighting competition but lost.\n\n"
elif ep11_music:
    $ report_text += "• You performed at the faculty's Christmas party and got an opportunity for a summer job.\n\n"

if not branchZoey:
    if ep12_zoey_friend:
        $ report_text += "• You decided to remain friends with Zoey.\n\n"
    else:
        $ report_text += "• You ended your friendship with Zoey.\n\n"

if ep12_forgave_nick:
    $ report_text += "• Nick tried to patch it up with the DIKs, and you forgave him.\n\n"
else:
    $ report_text += "• Nick tried to patch it up with the DIKs, but you didn't forgive him.\n\n"

if ep12_mc_slut:
    $ report_text += "• You were outed as a slut during Quinn's drinking game.\n\n"
else:
    $ report_text += "• Quinn tried to embarrass you during her drinking game.\n\n"

if not (ep12_nicole_path and ep12_nicole_dating > 0 and ep12_nicole_breakup):
    if ep12_nicole_ditch and ep12_nicole_breakup:
        $ report_text += "• Nicole distanced herself from you after you ditched her dinner invitation.\n\n"
    elif ep12_nicole_breakup:
        $ report_text += "• You told Nicole you didn't want to kiss her at midnight, and it seemed to have ended your relationship.\n\n"
if roadMayaJosy:
    $ report_text += "• You couldn't decide between Josy and Maya, so you chose to break your own heart instead of theirs.\n\n"
if roadMaya:
    if branchMayaJosy:
        $ report_text += "• You decided to continue your relationship with Maya when Josy and Maya wanted a break.\n\n"
    else:
        $ report_text += "• You decided to be with Maya when Josy and Maya broke up.\n\n"
if roadJosy:
    if branchMayaJosy:
        $ report_text += "• You decided to continue your relationship with Josy when Josy and Maya wanted a break.\n\n"
    else:
        $ report_text += "• You decided to be with Josy when Josy and Maya broke up.\n\n"

if roadJill:
    if ep12_jill_love:
        $ report_text += "• You told Jill that you love her at the New Year's Eve party, and she reciprocated.\n\n"
    else:
        $ report_text += "• You told Jill that you love her at the New Year's Eve party, but she didn't reciprocate.\n\n"
if roadQuinn:
    $ report_text += "• You decided to be with Quinn at the New Year's Eve party.\n\n"
if roadSage:
    $ report_text += "• You cemented your love for Sage.\n\n"
if ep12_midnight_kiss == "Nicole":
    $ report_text += "• You gave Nicole a midnight kiss at the New Year's Eve party.\n\n"
if ep12_midnight_kiss == "Camila":
    $ report_text += "• You gave Camila a midnight kiss at the New Year's Eve party.\n\n"
if ep12_midnight_kiss == "Sarah":
    $ report_text += "• You gave Sarah a midnight kiss at the New Year's Eve party.\n\n"
if ep12_midnight_kiss == "Melanie":
    $ report_text += "• You gave Melanie a midnight kiss at the New Year's Eve party.\n\n"
if ep12_midnight_kiss == "Nikita":
    $ report_text += "• You gave Nikita a midnight kiss at the New Year's Eve party.\n\n"
if ep12_midnight_kiss == "Jade":
    $ report_text += "• You decided you weren't ready to give up on Jade and had sex with her at the New Year's Eve party.\n\n"
if ep12_midnight_kiss == "Lily":
    $ report_text += "• You stood next to Lily at midnight on New Year's Eve at the party.\n\n"
if ep12_midnight_kiss == "Sally":
    $ report_text += "• You ended the night with Sally at the New Year's Eve party.\n\n"
if ep12_midnight_kiss == "Elena":
    $ report_text += "• You ended the night with Elena and John Boy at the New Year's Eve party.\n\n"
if ep12_midnight_kiss == "Alone":
    if ep12_hotties_club:
        $ report_text += "• You spent midnight alone but ended up making out with Tiffani, Mia, and Erin at the New Year's Eve party.\n\n"
    else:
        $ report_text += "• You spent midnight alone at the New Year's Eve party.\n\n"






show screen ep12_report_screen
$ renpy.pause()
jump ep12EndLabel

image spr_ep12_jill:
    "ep12_jill_lewd28" with Dissolve(0.2, alpha=True)
    zoom 1.0
    xalign 0.0 yalign 0.0
    linear 15.0 zoom 1.08
    linear 15.0 zoom 1.00
    repeat
image spr_ep12_bella:
    "ep12_np2_fw104" with Dissolve(0.2, alpha=True)
    zoom 1.0
    xalign 0.0 yalign 0.0
    linear 15.0 zoom 1.08
    linear 15.0 zoom 1.00
    repeat
image spr_ep12_sage:
    "ep12_sage_lewd46" with Dissolve(0.2, alpha=True)
    zoom 1.0
    xalign 0.0 yalign 0.0
    linear 15.0 zoom 1.08
    linear 15.0 zoom 1.00
    repeat
image spr_ep12_zoey:
    "ep12_zoey17" with Dissolve(0.2, alpha=True)
    zoom 1.0
    xalign 0.0 yalign 0.0
    linear 15.0 zoom 1.08
    linear 15.0 zoom 1.00
    repeat
image spr_ep12_josy:
    "ep12_np2_fw223" with Dissolve(0.2, alpha=True)
    zoom 1.0
    xalign 0.0 yalign 0.0
    linear 15.0 zoom 1.08
    linear 15.0 zoom 1.00
    repeat
image spr_ep12_josy2:
    "ep12_np2_fw226" with Dissolve(0.2, alpha=True)
    zoom 1.0
    xalign 0.0 yalign 0.0
    linear 15.0 zoom 1.08
    linear 15.0 zoom 1.00
    repeat
image spr_ep12_mayaa:
    "ep12_np2_fw231" with Dissolve(0.2, alpha=True)
    zoom 1.0
    xalign 0.0 yalign 0.0
    linear 15.0 zoom 1.08
    linear 15.0 zoom 1.00
    repeat
image spr_ep12_mayab:
    "ep12_np2_fw231b" with Dissolve(0.2, alpha=True)
    zoom 1.0
    xalign 0.0 yalign 0.0
    linear 15.0 zoom 1.08
    linear 15.0 zoom 1.00
    repeat
image spr_ep12_maya2:
    "ep12_np2_fw237" with Dissolve(0.2, alpha=True)
    zoom 1.0
    xalign 0.0 yalign 0.0
    linear 15.0 zoom 1.08
    linear 15.0 zoom 1.00
    repeat
image spr_ep12_maya_josya:
    "ep12_np2_fw239" with Dissolve(0.2, alpha=True)
    zoom 1.0
    xalign 0.0 yalign 0.0
    linear 15.0 zoom 1.08
    linear 15.0 zoom 1.00
    repeat
image spr_ep12_maya_josyb:
    "ep12_np2_fw239b" with Dissolve(0.2, alpha=True)
    zoom 1.0
    xalign 0.0 yalign 0.0
    linear 15.0 zoom 1.08
    linear 15.0 zoom 1.00
    repeat
image spr_ep12_quinn:
    "ep12_np2_qend4" with Dissolve(0.2, alpha=True)
    zoom 1.0
    xalign 0.0 yalign 0.0
    linear 15.0 zoom 1.08
    linear 15.0 zoom 1.00
    repeat

image spr_ep12_riona:
    "ep12_mc_rio_room44" with Dissolve(0.2, alpha=True)
    zoom 1.0
    xalign 0.0 yalign 0.0
    linear 15.0 zoom 1.08
    linear 15.0 zoom 1.00
    repeat
image spr_ep12_lily:
    "ep12_np2_fw170" with Dissolve(0.2, alpha=True)
    zoom 1.0
    xalign 0.0 yalign 0.0
    linear 15.0 zoom 1.08
    linear 15.0 zoom 1.00
    repeat
image spr_ep12_sally:
    "ep12_sally23" with Dissolve(0.2, alpha=True)
    zoom 1.0
    xalign 0.0 yalign 0.0
    linear 15.0 zoom 1.08
    linear 15.0 zoom 1.00
    repeat
image spr_ep12_jade:
    "ep12_np2_jade10" with Dissolve(0.2, alpha=True)
    zoom 1.0
    xalign 0.0 yalign 0.0
    linear 15.0 zoom 1.08
    linear 15.0 zoom 1.00
    repeat
image spr_ep12_camila:
    "ep12_np2_fw90" with Dissolve(0.2, alpha=True)
    zoom 1.0
    xalign 0.0 yalign 0.0
    linear 15.0 zoom 1.08
    linear 15.0 zoom 1.00
    repeat
image spr_ep12_nikita:
    "ep12_np2_fw50" with Dissolve(0.2, alpha=True)
    zoom 1.0
    xalign 0.0 yalign 0.0
    linear 15.0 zoom 1.08
    linear 15.0 zoom 1.00
    repeat
image spr_ep12_bianca:
    "ep12_bianca_lewd29" with Dissolve(0.2, alpha=True)
    zoom 1.0
    xalign 0.0 yalign 0.0
    linear 15.0 zoom 1.08
    linear 15.0 zoom 1.00
    repeat
image spr_ep12_elena:
    "ep12_elena_lewd16" with Dissolve(0.2, alpha=True)
    zoom 1.0
    xalign 0.0 yalign 0.0
    linear 15.0 zoom 1.08
    linear 15.0 zoom 1.00
    repeat
image spr_ep12_sarah:
    "ep12_np2_fw76" with Dissolve(0.2, alpha=True)
    zoom 1.0
    xalign 0.0 yalign 0.0
    linear 15.0 zoom 1.08
    linear 15.0 zoom 1.00
    repeat
image spr_ep12_melanie:
    "ep12_np_josy12" with Dissolve(0.2, alpha=True)
    zoom 1.0
    xalign 0.0 yalign 0.0
    linear 15.0 zoom 1.08
    linear 15.0 zoom 1.00
    repeat
image spr_ep12_nicole:
    "ep12_nic_lewd5" with Dissolve(0.2, alpha=True)
    zoom 1.0
    xalign 0.0 yalign 0.0
    linear 15.0 zoom 1.08
    linear 15.0 zoom 1.00
    repeat
image spr_ep12_nora:
    "ep12_nora_lewd23" with Dissolve(0.2, alpha=True)
    zoom 1.0
    xalign 0.0 yalign 0.0
    linear 15.0 zoom 1.08
    linear 15.0 zoom 1.00
    repeat
image spr_ep12_alone:
    "ep12_np_dj1_fr2" with Dissolve(0.2, alpha=True)
    zoom 1.0
    xalign 0.0 yalign 0.0
    linear 15.0 zoom 1.08
    linear 15.0 zoom 1.00
    repeat


screen ep12_report_screen:
    tag ep12_report_screen
    modal True
    if roadJill:
        add "spr_ep12_jill"
    elif roadIsabella:
        add "spr_ep12_bella"
    elif roadSage:
        add "spr_ep12_sage"
    elif roadZoey:
        add "spr_ep12_zoey"
    elif roadJosy:
        if branchMayaJosy:
            add "spr_ep12_josy"
        else:
            add "spr_ep12_josy2"
    elif roadMaya:
        if branchMayaJosy:
            if maya_shiny_dress:
                add "spr_ep12_mayaa"
            else:
                add "spr_ep12_mayab"
        else:
            add "spr_ep12_maya2"
    elif roadMayaJosy:
        if maya_shiny_dress:
            add "spr_ep12_maya_josya"
        else:
            add "spr_ep12_maya_josyb"
    elif roadQuinn:
        add "spr_ep12_quinn"
    else:
        if ep12_midnight_kiss == "Riona":
            add "spr_ep12_riona"
        elif ep12_midnight_kiss == "Lily":
            add "spr_ep12_lily"
        elif ep12_midnight_kiss == "Sally":
            add "spr_ep12_sally"
        elif ep12_midnight_kiss == "Jade":
            add "spr_ep12_jade"
        elif ep12_midnight_kiss == "Camila":
            add "spr_ep12_camila"
        elif ep12_midnight_kiss == "Nikita":
            add "spr_ep12_nikita"
        elif ep12_midnight_kiss == "Bianca":
            add "spr_ep12_bianca"
        elif ep12_midnight_kiss == "Elena":
            add "spr_ep12_elena"
        elif ep12_midnight_kiss == "Sarah":
            add "spr_ep12_sarah"
        elif ep12_midnight_kiss == "Melanie":
            add "spr_ep12_melanie"
        elif ep12_midnight_kiss == "Nicole":
            add "spr_ep12_nicole"
        elif ep12_nora_state == 2:
            add "spr_ep12_nora"
        else:
            add "spr_ep12_alone"
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
        if not roadAlone or breakup or roadQuinn:
            xoffset -1060 * persistent.scale_factor
        else:
            xoffset -1200 * persistent.scale_factor

    if roadZoey:
        imagebutton:
            idle "mphone_bios_big_zoey"
            hover "mphone_bios_big_zoey"
            action NullAction()
            xalign 0.0
            yalign 0.5
            xoffset -1250 * persistent.scale_factor
            yoffset -3 * persistent.scale_factor
    else:
        if branchSage:
            if roadSage:
                imagebutton:
                    idle "mphone_bios_big_sage"
                    hover "mphone_bios_big_sage"
                    action NullAction()
                    xalign 0.0
                    yalign 0.5
                    xoffset -1300 * persistent.scale_factor
                    yoffset -3 * persistent.scale_factor
            else:
                imagebutton at hide_slow:
                    idle "mphone_bios_big_sage"
                    hover "mphone_bios_big_sage"
                    action NullAction()
                    xalign 0.0
                    yalign 0.5
                    xoffset -1300 * persistent.scale_factor
                    yoffset -3 * persistent.scale_factor
        if branchJill:
            if roadJill:
                imagebutton:
                    idle "mphone_bios_big_jill"
                    hover "mphone_bios_big_jill"
                    action NullAction()
                    xalign 0.0
                    yalign 0.5
                    xoffset -1300 * persistent.scale_factor
                    yoffset -3 * persistent.scale_factor
            else:
                imagebutton at hide_slow:
                    idle "mphone_bios_big_jill"
                    hover "mphone_bios_big_jill"
                    action NullAction()
                    xalign 0.0
                    yalign 0.5
                    xoffset -1300 * persistent.scale_factor
                    yoffset -3 * persistent.scale_factor
        if branchIsabella:
            if roadIsabella:
                imagebutton:
                    idle "mphone_bios_big_isabella"
                    hover "mphone_bios_big_isabella"
                    action NullAction()
                    xalign 0.0
                    yalign 0.5
                    xoffset -1300 * persistent.scale_factor
                    yoffset -3 * persistent.scale_factor
            else:
                imagebutton at hide_slow:
                    idle "mphone_bios_big_isabella"
                    hover "mphone_bios_big_isabella"
                    action NullAction()
                    xalign 0.0
                    yalign 0.5
                    xoffset -1300 * persistent.scale_factor
                    yoffset -3 * persistent.scale_factor
        if branchMayaJosy:
            if roadMayaJosy:
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
            elif roadJosy:
                imagebutton at hide_slow:
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
            elif roadMaya:
                imagebutton:
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
            if roadMaya:
                imagebutton:
                    idle "mphone_bios_big_maya"
                    hover "mphone_bios_big_maya"
                    action NullAction()
                    xalign 0.0
                    yalign 0.5
                    xoffset -1330 * persistent.scale_factor
                    yoffset -3 * persistent.scale_factor
            if roadJosy:
                imagebutton at transform_zoom90:
                    idle "mphone_bios_big_josy"
                    hover "mphone_bios_big_josy"
                    action NullAction()
                    xalign 0.0
                    yalign 0.5
                    xoffset -1240 * persistent.scale_factor
                    yoffset 14 * persistent.scale_factor
        if roadQuinn:
            imagebutton:
                idle "mphone_bios_big_quinn"
                hover "mphone_bios_big_quinn"
                action NullAction()
                xalign 0.0
                yalign 0.5
                xoffset -1300 * persistent.scale_factor
                yoffset -3 * persistent.scale_factor

    imagebutton:
        idle "report_screen_button"
        hover "report_screen_button"
        action (Hide("ep12_report_screen"),Jump("ep12EndLabel"))

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
