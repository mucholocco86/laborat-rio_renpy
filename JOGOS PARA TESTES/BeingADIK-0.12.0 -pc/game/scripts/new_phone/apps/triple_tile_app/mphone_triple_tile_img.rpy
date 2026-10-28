screen triple_tile_game_over_screen:
    tag triple_tile_game_over_screen
    modal True
    add "mphone_triple_tile_game_over"
    text "{size=+%d}{color=ffffff}OUT OF MOVES!{/color}{/size}" % (30 * persistent.scale_factor) style "mphone_triple_tile_text_style" xalign 0.50 yalign 0.45
    timer 3 action (Hide("triple_tile_game_over_screen"),SetVariable("triple_tile_game_over", True),SetVariable("triple_tile_hovered_tile",[-1,-1]),Hide("triple_tile_spr_screen"),triple_tile_check_high_score())
    key "mouseup_2" action NullAction()

screen triple_tile_spr_screen:
    tag triple_tile_spr_screen
    modal False

    timer 2 action (Hide("triple_tile_spr_screen"),triple_tile_check_game_over())

    $ tt_combos = 0
    for x in range(0,3):
        for y in range(0,3):
            for k in range(0,3):
                if triple_tile_grid_spr[x][y][k] != 0:
                    $ tt_combos += 1
    if tt_combos > 4:
        $ tt_combos = "_gold"
    elif tt_combos > 3:
        $ tt_combos = "_yellow"
    else:
        $ tt_combos = ""
    for x in range(0,3):
        for y in range(0,3):
            if triple_tile_spr[x][y]:
                add "spr_tt_spr%i%s" % ((3*x + y), tt_combos)

    vbox:
        xalign 0.5
        yalign 0.40
        yoffset 3 * persistent.scale_factor
        spacing 9 * persistent.scale_factor
        for i in range(0,3):
            hbox:
                spacing 6 * persistent.scale_factor
                for j in range(0,3):
                    hbox:
                        for k in range(0,3):
                            if triple_tile_grid_spr[i][j][k] == 0:
                                imagebutton at triple_tile_disappear_combo_transform:
                                    idle "triple_tile_empty"
                                    hover "triple_tile_empty"
                                    if triple_tile_chosen_tile == -1:
                                        action NullAction()
                                    else:
                                        hovered SetVariable("triple_tile_hovered_tile",[i,j])
                                        unhovered SetVariable("triple_tile_hovered_tile",[-1,-1])
                                        action Function(triple_tile_add_tile,i,j)
                            else:
                                imagebutton at triple_tile_disappear_combo_transform:
                                    if triple_tile_show_numbers:
                                        idle "triple_tile_%ib" % triple_tile_grid_spr[i][j][k]
                                        hover "triple_tile_%ib" % triple_tile_grid_spr[i][j][k]
                                    else:
                                        idle "triple_tile_%i" % triple_tile_grid_spr[i][j][k]
                                        hover "triple_tile_%i" % triple_tile_grid_spr[i][j][k]
                                    action NullAction()

image spr_tt_spr0:
    contains:
        "tt_spr0"
        alpha 0.0
        choice:
            easein 0.2 alpha 1.0
        choice:
            easein 0.24 alpha 1.0
        choice:
            easein 0.28 alpha 1.0
        choice:
            easein 0.32 alpha 1.0
        choice:
            easein 0.36 alpha 1.0
        choice:
            easein 0.4 alpha 1.0
        easein 0.2 alpha 0.0

image spr_tt_spr1:
    contains:
        "tt_spr1"
        alpha 0.0
        choice:
            easein 0.2 alpha 1.0
        choice:
            easein 0.24 alpha 1.0
        choice:
            easein 0.28 alpha 1.0
        choice:
            easein 0.32 alpha 1.0
        choice:
            easein 0.36 alpha 1.0
        choice:
            easein 0.4 alpha 1.0
        easein 0.2 alpha 0.0

image spr_tt_spr2:
    contains:
        "tt_spr2"
        alpha 0.0
        choice:
            easein 0.2 alpha 1.0
        choice:
            easein 0.24 alpha 1.0
        choice:
            easein 0.28 alpha 1.0
        choice:
            easein 0.32 alpha 1.0
        choice:
            easein 0.36 alpha 1.0
        choice:
            easein 0.4 alpha 1.0
        easein 0.2 alpha 0.0

image spr_tt_spr3:
    contains:
        "tt_spr3"
        alpha 0.0
        choice:
            easein 0.2 alpha 1.0
        choice:
            easein 0.24 alpha 1.0
        choice:
            easein 0.28 alpha 1.0
        choice:
            easein 0.32 alpha 1.0
        choice:
            easein 0.36 alpha 1.0
        choice:
            easein 0.4 alpha 1.0
        easein 0.2 alpha 0.0

image spr_tt_spr4:
    contains:
        "tt_spr4"
        alpha 0.0
        choice:
            easein 0.2 alpha 1.0
        choice:
            easein 0.24 alpha 1.0
        choice:
            easein 0.28 alpha 1.0
        choice:
            easein 0.32 alpha 1.0
        choice:
            easein 0.36 alpha 1.0
        choice:
            easein 0.4 alpha 1.0
        easein 0.2 alpha 0.0

image spr_tt_spr5:
    contains:
        "tt_spr5"
        alpha 0.0
        choice:
            easein 0.2 alpha 1.0
        choice:
            easein 0.24 alpha 1.0
        choice:
            easein 0.28 alpha 1.0
        choice:
            easein 0.32 alpha 1.0
        choice:
            easein 0.36 alpha 1.0
        choice:
            easein 0.4 alpha 1.0
        easein 0.2 alpha 0.0

image spr_tt_spr6:
    contains:
        "tt_spr6"
        alpha 0.0
        choice:
            easein 0.2 alpha 1.0
        choice:
            easein 0.24 alpha 1.0
        choice:
            easein 0.28 alpha 1.0
        choice:
            easein 0.32 alpha 1.0
        choice:
            easein 0.36 alpha 1.0
        choice:
            easein 0.4 alpha 1.0
        easein 0.2 alpha 0.0

image spr_tt_spr7:
    contains:
        "tt_spr7"
        alpha 0.0
        choice:
            easein 0.2 alpha 1.0
        choice:
            easein 0.24 alpha 1.0
        choice:
            easein 0.28 alpha 1.0
        choice:
            easein 0.32 alpha 1.0
        choice:
            easein 0.36 alpha 1.0
        choice:
            easein 0.4 alpha 1.0
        easein 0.2 alpha 0.0

image spr_tt_spr8:
    contains:
        "tt_spr8"
        alpha 0.0
        choice:
            easein 0.2 alpha 1.0
        choice:
            easein 0.24 alpha 1.0
        choice:
            easein 0.28 alpha 1.0
        choice:
            easein 0.32 alpha 1.0
        choice:
            easein 0.36 alpha 1.0
        choice:
            easein 0.4 alpha 1.0
        easein 0.2 alpha 0.0

image spr_tt_spr0_yellow:
    contains:
        "tt_spr0_yellow"
        alpha 0.0
        choice:
            easein 0.2 alpha 1.0
        choice:
            easein 0.24 alpha 1.0
        choice:
            easein 0.28 alpha 1.0
        choice:
            easein 0.32 alpha 1.0
        choice:
            easein 0.36 alpha 1.0
        choice:
            easein 0.4 alpha 1.0
        easein 0.2 alpha 0.0

image spr_tt_spr1_yellow:
    contains:
        "tt_spr1_yellow"
        alpha 0.0
        choice:
            easein 0.2 alpha 1.0
        choice:
            easein 0.24 alpha 1.0
        choice:
            easein 0.28 alpha 1.0
        choice:
            easein 0.32 alpha 1.0
        choice:
            easein 0.36 alpha 1.0
        choice:
            easein 0.4 alpha 1.0
        easein 0.2 alpha 0.0

image spr_tt_spr2_yellow:
    contains:
        "tt_spr2_yellow"
        alpha 0.0
        choice:
            easein 0.2 alpha 1.0
        choice:
            easein 0.24 alpha 1.0
        choice:
            easein 0.28 alpha 1.0
        choice:
            easein 0.32 alpha 1.0
        choice:
            easein 0.36 alpha 1.0
        choice:
            easein 0.4 alpha 1.0
        easein 0.2 alpha 0.0

image spr_tt_spr3_yellow:
    contains:
        "tt_spr3_yellow"
        alpha 0.0
        choice:
            easein 0.2 alpha 1.0
        choice:
            easein 0.24 alpha 1.0
        choice:
            easein 0.28 alpha 1.0
        choice:
            easein 0.32 alpha 1.0
        choice:
            easein 0.36 alpha 1.0
        choice:
            easein 0.4 alpha 1.0
        easein 0.2 alpha 0.0

image spr_tt_spr4_yellow:
    contains:
        "tt_spr4_yellow"
        alpha 0.0
        choice:
            easein 0.2 alpha 1.0
        choice:
            easein 0.24 alpha 1.0
        choice:
            easein 0.28 alpha 1.0
        choice:
            easein 0.32 alpha 1.0
        choice:
            easein 0.36 alpha 1.0
        choice:
            easein 0.4 alpha 1.0
        easein 0.2 alpha 0.0

image spr_tt_spr5_yellow:
    contains:
        "tt_spr5_yellow"
        alpha 0.0
        choice:
            easein 0.2 alpha 1.0
        choice:
            easein 0.24 alpha 1.0
        choice:
            easein 0.28 alpha 1.0
        choice:
            easein 0.32 alpha 1.0
        choice:
            easein 0.36 alpha 1.0
        choice:
            easein 0.4 alpha 1.0
        easein 0.2 alpha 0.0

image spr_tt_spr6_yellow:
    contains:
        "tt_spr6_yellow"
        alpha 0.0
        choice:
            easein 0.2 alpha 1.0
        choice:
            easein 0.24 alpha 1.0
        choice:
            easein 0.28 alpha 1.0
        choice:
            easein 0.32 alpha 1.0
        choice:
            easein 0.36 alpha 1.0
        choice:
            easein 0.4 alpha 1.0
        easein 0.2 alpha 0.0

image spr_tt_spr7_yellow:
    contains:
        "tt_spr7_yellow"
        alpha 0.0
        choice:
            easein 0.2 alpha 1.0
        choice:
            easein 0.24 alpha 1.0
        choice:
            easein 0.28 alpha 1.0
        choice:
            easein 0.32 alpha 1.0
        choice:
            easein 0.36 alpha 1.0
        choice:
            easein 0.4 alpha 1.0
        easein 0.2 alpha 0.0

image spr_tt_spr8_yellow:
    contains:
        "tt_spr8_yellow"
        alpha 0.0
        choice:
            easein 0.2 alpha 1.0
        choice:
            easein 0.24 alpha 1.0
        choice:
            easein 0.28 alpha 1.0
        choice:
            easein 0.32 alpha 1.0
        choice:
            easein 0.36 alpha 1.0
        choice:
            easein 0.4 alpha 1.0
        easein 0.2 alpha 0.0

image spr_tt_spr0_gold:
    contains:
        "tt_spr0_gold"
        alpha 0.0
        choice:
            easein 0.2 alpha 1.0
        choice:
            easein 0.24 alpha 1.0
        choice:
            easein 0.28 alpha 1.0
        choice:
            easein 0.32 alpha 1.0
        choice:
            easein 0.36 alpha 1.0
        choice:
            easein 0.4 alpha 1.0
        easein 0.2 alpha 0.0

image spr_tt_spr1_gold:
    contains:
        "tt_spr1_gold"
        alpha 0.0
        choice:
            easein 0.2 alpha 1.0
        choice:
            easein 0.24 alpha 1.0
        choice:
            easein 0.28 alpha 1.0
        choice:
            easein 0.32 alpha 1.0
        choice:
            easein 0.36 alpha 1.0
        choice:
            easein 0.4 alpha 1.0
        easein 0.2 alpha 0.0

image spr_tt_spr2_gold:
    contains:
        "tt_spr2_gold"
        alpha 0.0
        choice:
            easein 0.2 alpha 1.0
        choice:
            easein 0.24 alpha 1.0
        choice:
            easein 0.28 alpha 1.0
        choice:
            easein 0.32 alpha 1.0
        choice:
            easein 0.36 alpha 1.0
        choice:
            easein 0.4 alpha 1.0
        easein 0.2 alpha 0.0

image spr_tt_spr3_gold:
    contains:
        "tt_spr3_gold"
        alpha 0.0
        choice:
            easein 0.2 alpha 1.0
        choice:
            easein 0.24 alpha 1.0
        choice:
            easein 0.28 alpha 1.0
        choice:
            easein 0.32 alpha 1.0
        choice:
            easein 0.36 alpha 1.0
        choice:
            easein 0.4 alpha 1.0
        easein 0.2 alpha 0.0

image spr_tt_spr4_gold:
    contains:
        "tt_spr4_gold"
        alpha 0.0
        choice:
            easein 0.2 alpha 1.0
        choice:
            easein 0.24 alpha 1.0
        choice:
            easein 0.28 alpha 1.0
        choice:
            easein 0.32 alpha 1.0
        choice:
            easein 0.36 alpha 1.0
        choice:
            easein 0.4 alpha 1.0
        easein 0.2 alpha 0.0

image spr_tt_spr5_gold:
    contains:
        "tt_spr5_gold"
        alpha 0.0
        choice:
            easein 0.2 alpha 1.0
        choice:
            easein 0.24 alpha 1.0
        choice:
            easein 0.28 alpha 1.0
        choice:
            easein 0.32 alpha 1.0
        choice:
            easein 0.36 alpha 1.0
        choice:
            easein 0.4 alpha 1.0
        easein 0.2 alpha 0.0

image spr_tt_spr6_gold:
    contains:
        "tt_spr6_gold"
        alpha 0.0
        choice:
            easein 0.2 alpha 1.0
        choice:
            easein 0.24 alpha 1.0
        choice:
            easein 0.28 alpha 1.0
        choice:
            easein 0.32 alpha 1.0
        choice:
            easein 0.36 alpha 1.0
        choice:
            easein 0.4 alpha 1.0
        easein 0.2 alpha 0.0

image spr_tt_spr7_gold:
    contains:
        "tt_spr7_gold"
        alpha 0.0
        choice:
            easein 0.2 alpha 1.0
        choice:
            easein 0.24 alpha 1.0
        choice:
            easein 0.28 alpha 1.0
        choice:
            easein 0.32 alpha 1.0
        choice:
            easein 0.36 alpha 1.0
        choice:
            easein 0.4 alpha 1.0
        easein 0.2 alpha 0.0

image spr_tt_spr8_gold:
    contains:
        "tt_spr8_gold"
        alpha 0.0
        choice:
            easein 0.2 alpha 1.0
        choice:
            easein 0.24 alpha 1.0
        choice:
            easein 0.28 alpha 1.0
        choice:
            easein 0.32 alpha 1.0
        choice:
            easein 0.36 alpha 1.0
        choice:
            easein 0.4 alpha 1.0
        easein 0.2 alpha 0.0

transform tt_appear_transform:
    alpha 0.0
    yoffset 200 * persistent.scale_factor
    easein 0.4 alpha 1.0 yoffset 0


transform triple_tile_disappear_combo_transform:
    alpha 1.0
    easein 0.2 alpha 0.0
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
