screen party_planner_item_perk_screen:
    tag party_planner_item_perk_screen
    modal True

    add "party_planner_perks_overlay"

    text "{u}Select two Items{/u}" style "pp_perk_style_big" yalign 0.3
    text "Start every Party Planning round with 1 more..." style "pp_perk_style" yalign 0.4

    hbox:
        xalign 0.5
        yalign 0.55
        spacing 30 * persistent.scale_factor
        for x in range(0,len(pp_icons_limited_list)):
            vbox:
                if x in tmp_list:
                    text pp_icons_limited_list[x] style "pp_perk_item_selected_style" yalign 0.5 xalign 0.5
                else:
                    text pp_icons_limited_list[x] style "pp_perk_item_style" yalign 0.5 xalign 0.5
                imagebutton:
                    if x in tmp_list:
                        idle "pp_"+pp_icons_limited_list[x].lower()+"_active"
                    else:
                        idle "pp_"+pp_icons_limited_list[x].lower()+"_idle"
                    hover "pp_"+pp_icons_limited_list[x].lower()+"_hover"

                    if x in tmp_list:
                        action (Play("sfx1", "sound_effects/interlude/select_choice.mp3", loop = False),SetDict(tmp_list, tmp_list.index(x), -1))
                    else:
                        if tmp_list[0] == -1:
                            action (Play("sfx1", "sound_effects/interlude/select_choice.mp3", loop = False),SetDict(tmp_list, 0, x))
                        else:
                            action (Play("sfx1", "sound_effects/interlude/select_choice.mp3", loop = False),SetDict(tmp_list, 1, x))
                    yalign 0.5
                    xalign 0.5
                if x in tmp_list:
                    text "{size=+%d}%d{/size}" % ((10 * persistent.scale_factor),pp_inventory_limited_start_list[x]+1) style "pp_perk_item_selected_style" yalign 0.5 xalign 0.5
                else:
                    if pp_inventory_limited_start_list[x] > 0:
                        text "{size=+%d}%d{/size}" % ((10 * persistent.scale_factor),pp_inventory_limited_start_list[x]) style "pp_perk_item_style" yalign 0.5 xalign 0.5
                    else:
                        text "{color=ff0000}{size=+%d}%d{/size}{/color}" % ((10 * persistent.scale_factor),pp_inventory_limited_start_list[x]) style "pp_perk_item_style" yalign 0.5 xalign 0.5

    textbutton "Continue" text_style "pp_perk_continue_style":
        xalign 0.5
        yalign 0.70
        if not -1 in tmp_list:
            action (Play("sfx1", "sound_effects/menu.mp3", loop = False),Jump("party_planner_end_perk1_menu_label"))

    if persistent.pp_tutorial != 2 and currentEpisode == 9:
        if pp_tut_state == 0:
            imagebutton:
                idle "pp_invis_tutorial_button"
                hover "pp_invis_tutorial_button"
                action SetVariable("pp_tut_state",pp_tut_state+1)
            imagebutton:
                idle "party_planner_tutorial_text_box"
                hover "party_planner_tutorial_text_box"
            text "Between parties, you upgrade your {color=ffc27b}Items{/color} inventory by selecting two different items. You will always start party planning rounds with these items." xalign 0.15 yalign 0.91 style "pp_tut_text_style"
        elif pp_tut_state == 1:
            imagebutton:
                idle "pp_invis_tutorial_button"
                hover "pp_invis_tutorial_button"
                action SetVariable("pp_tut_state",pp_tut_state+1)
            imagebutton:
                idle "party_planner_tutorial_text_box"
                hover "party_planner_tutorial_text_box"
            text "This upgrade is permanent, and it's up to you how best to plan for your future needs. At the start, having at least one of each {color=ffc27b}item{/color} is a good strategy." xalign 0.15 yalign 0.91 style "pp_tut_text_style"
        elif pp_tut_state == 2:
            imagebutton:
                idle "pp_invis_tutorial_button"
                hover "pp_invis_tutorial_button"
                action SetVariable("pp_tut_state",pp_tut_state+1)
            imagebutton:
                idle "party_planner_tutorial_text_box"
                hover "party_planner_tutorial_text_box"
            text "For your first party, select two extra starting {color=ffc27b}items{/color}. {color=ffed00}Hint!{/color} {color=ffc27b}Food{/color}, {color=ffc27b}Liquor{/color}, and {color=ffc27b}Speakers{/color} can be useful in the first mini-game round." xalign 0.15 yalign 0.91 style "pp_tut_text_style"


label party_planner_end_perk1_menu_label:
$ renpy.block_rollback()
hide screen party_planner_item_perk_screen
$ pp_dik_info = -1
$ pp_inventory_limited_start_list[tmp_list[0]] = pp_inventory_limited_start_list[tmp_list[0]] + 1
$ pp_inventory_limited_start_list[tmp_list[1]] = pp_inventory_limited_start_list[tmp_list[1]] + 1
$ tmpInt = -1
show screen party_planner_perk_screen
pause
label party_planner_end_perk2_menu_label:
$ renpy.block_rollback()
hide screen party_planner_perk_screen
$ persistent.pp_tutorial = 2
$ renpy.jump(pp_continue_label)
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
