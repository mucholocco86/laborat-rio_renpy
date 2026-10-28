screen party_planner_perk_screen:
    tag party_planner_perk_screen
    modal True

    add "party_planner_perks2_overlay"

    text "{size=-%d}{u}Select one Perk{/u}{/size}" % (20 * persistent.scale_factor) style "pp_perk_style_big" yalign 0.0

    vpgrid:
        xalign 0.5
        yalign 0.5
        rows 4
        cols 3
        spacing 0
        draggable False
        mousewheel False
        for x in range(0,12):
            imagebutton:
                if pp_dik_info == x or pp_perk_list[x]:
                    idle "pp_perk_bg_selected_idle"
                    if pp_dik_info == x:
                        hover "pp_perk_bg_selected_hover"
                    else:
                        hover "pp_perk_bg_selected_idle"
                    if pp_perk_list[x]:
                        action NullAction()
                    else:
                        action (Play("sfx1", "sound_effects/interlude/select_choice.mp3", loop = False),SetVariable("pp_dik_info",-1))
                else:
                    idle "pp_perk_bg_idle"
                    hover "pp_perk_bg_hover"
                    action (Play("sfx1", "sound_effects/interlude/select_choice.mp3", loop = False),SetVariable("pp_dik_info",x))

    textbutton "{size=-%d}Continue{/size}" % (20 * persistent.scale_factor) text_style "pp_perk_continue_style":
        xalign 0.5
        yalign 1.0
        yoffset 5 * persistent.scale_factor
        if pp_dik_info != -1:
            action (Play("sfx1", "sound_effects/menu.mp3", loop = False),SetDict(pp_perk_list,pp_dik_info,True), Jump("party_planner_enable_perks_label"))


    text "Pink Weiß" style "pp_perks_header_style" xalign 0.21 yalign 0.1
    imagebutton:
        idle "pp_beers_active"
        hover "pp_beers_active"
        xalign 0.11
        yalign 0.19
    imagebutton:
        idle "pp_cups_active"
        hover "pp_cups_active"
        xalign 0.237
        yalign 0.19
    text "don't need              to activate." style "pp_perks_header_style" xalign 0.188 yalign 0.2


    text "Finger Food" style "pp_perks_header_style" xalign 0.5 yalign 0.1
    imagebutton:
        idle "pp_food_active"
        hover "pp_food_active"
        xalign 0.395
        yalign 0.19
    imagebutton:
        idle "pp_trashcans_active"
        hover "pp_trashcans_active"
        xalign 0.522
        yalign 0.19
    text "don't need              to activate." style "pp_perks_header_style" xalign 0.53 yalign 0.2


    text "Jello Shots" style "pp_perks_header_style" xalign 0.80 yalign 0.1
    imagebutton:
        idle "pp_liquor_active"
        hover "pp_liquor_active"
        xalign 0.685
        yalign 0.19
    imagebutton:
        idle "pp_cups_active"
        hover "pp_cups_active"
        xalign 0.81
        yalign 0.19
    text "don't need              to activate." style "pp_perks_header_style" xalign 0.875 yalign 0.2


    text "Connections" style "pp_perks_header_style" xalign 0.208 yalign 0.317
    imagebutton:
        idle "pp_drugs_active"
        hover "pp_drugs_active"
        xalign 0.261
        yalign 0.412
    text "Reduces the cost of              by {color=fe9416}$3{/color}." style "pp_perks_header_style" xalign 0.145 yalign 0.415


    text "Wholesale" style "pp_perks_header_style" xalign 0.5 yalign 0.317
    imagebutton:
        idle "pp_kegs_active"
        hover "pp_kegs_active"
        xalign 0.55
        yalign 0.412
    text "Reduces the cost of               by {color=fe9416}$3{/color}." style "pp_perks_header_style" xalign 0.50 yalign 0.415


    text "Black Friday" style "pp_perks_header_style" xalign 0.80 yalign 0.317
    imagebutton:
        idle "pp_speakers_active"
        hover "pp_speakers_active"
        xalign 0.837
        yalign 0.412
    text "Reduces the cost of               by {color=fe9416}$2{/color}." style "pp_perks_header_style" xalign 0.858 yalign 0.415


    text "Crowdfunding" style "pp_perks_header_style" xalign 0.208 yalign 0.534
    text "Increase the party budget by {color=fe9416}$4{/color}." style "pp_perks_header_style" xalign 0.145 yalign 0.630


    text "DIK Party" style "pp_perks_header_style" xalign 0.5 yalign 0.534
    text "50% extra {color=ffed00}bonus score{/color}\nfrom activities." style "pp_perks_header_style" xalign 0.50 yalign 0.630 text_align 0.5


    text "Easy to Please" style "pp_perks_header_style" xalign 0.805 yalign 0.534
    text "Receive {color=#fe9416}20%{/color} extra {color=fe9416}Happiness{/color} points\nfor each fulfilled {color=00ff00}need{/color} for every DIK." style "pp_perks_header_style" xalign 0.865 yalign 0.630 text_align 0.5


    text "Hard to Let Down" style "pp_perks_header_style" xalign 0.195 yalign 0.753
    text "Unfulfilled {color=00ff00}needs{/color} lose {color=#fe9416}20%{/color} fewer\n{color=fe9416}Happiness{/color} points for every DIK." style "pp_perks_header_style" xalign 0.145 yalign 0.862 text_align 0.5


    text "Multiplier Madness" style "pp_perks_header_style" xalign 0.505 yalign 0.753
    text "DIKs with at least {color=fe9416}50% Happiness{/color}\nadd an extra {color=#e51475}0.1x multiplier{/color}." style "pp_perks_header_style" xalign 0.50 yalign 0.862 text_align 0.5


    text "Below Budget" style "pp_perks_header_style" xalign 0.805 yalign 0.753
    text "Save up to {color=#fe9416}$5{/color} for\nthe next party budget.\nExcess money is lost between parties." style "pp_perks_header_style" xalign 0.870 yalign 0.878 text_align 0.5

    if persistent.pp_tutorial != 2 and currentEpisode == 9:
        if pp_tut_state == 3:
            imagebutton:
                idle "party_planner_tutorial_focus_score7"
                hover "party_planner_tutorial_focus_score7"
                action SetVariable("pp_tut_state",pp_tut_state+1)
            imagebutton:
                idle "party_planner_tutorial_text_box"
                hover "party_planner_tutorial_text_box"
            text "{color=ffed00}Perks{/color} offer powerful advantages. Between parties, you may select one new {color=ffed00}perk{/color}." xalign 0.15 yalign 0.89 style "pp_tut_text_style"
        elif pp_tut_state == 4:
            imagebutton:
                idle "party_planner_tutorial_focus_score7"
                hover "party_planner_tutorial_focus_score7"
                action SetVariable("pp_tut_state",pp_tut_state+1)
            imagebutton:
                idle "party_planner_tutorial_text_box"
                hover "party_planner_tutorial_text_box"
            text "This upgrade is permanent, and it's up to you how best to plan for your future needs." xalign 0.15 yalign 0.89 style "pp_tut_text_style"
        elif pp_tut_state == 5:
            imagebutton:
                idle "party_planner_tutorial_focus_score7"
                hover "party_planner_tutorial_focus_score7"
                action SetVariable("pp_tut_state",pp_tut_state+1)
            imagebutton:
                idle "party_planner_tutorial_text_box"
                hover "party_planner_tutorial_text_box"
            text "A recommended starting {color=ffed00}perk{/color} is either {color=ffc27b}Pink Weiß{/color} or {color=ffc27b}Crowdfunding{/color}, but you may choose differently too. Don't be scared to experiment!" xalign 0.15 yalign 0.91 style "pp_tut_text_style"

label party_planner_enable_perks_label:
$ renpy.block_rollback()
if pp_perk_list[0]:
    $ pp_icons_limited_dependency_list[0] = ""
if pp_perk_list[1]:
    $ pp_icons_limited_dependency_list[3] = ""
if pp_perk_list[2]:
    $ pp_icons_limited_dependency_list[5] = ""
if pp_perk_list[3]:
    $ pp_price_limited_list[2] = 1
if pp_perk_list[4]:
    $ pp_price_limited_list[4] = 2
if pp_perk_list[5]:
    $ pp_price_limited_list[7] = 1
if pp_perk_list[6]:
    $ pp_extra_budget = 4
if pp_perk_list[7]:
    $ pp_bonus_multiplier = 1.50
if pp_perk_list[8]:
    $ pp_extra_happiness = 1.2
if pp_perk_list[9]:
    $ pp_happiness_penalty = 0.8
if pp_perk_list[10]:
    $ pp_multiplier_madness = 0.10
if pp_perk_list[11]:
    if pp_perk_list.count(True) > 1:
        $ pp_below_budget = min(pp_money,5)
        if pp_below_budget > 0:
            $ mphone_pp_history_list.append("• The {color=ffed00}Below Budget{/color} perk saved {color=00ff00}$[pp_below_budget]{/color} for the next party.")

jump party_planner_end_perk2_menu_label
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
