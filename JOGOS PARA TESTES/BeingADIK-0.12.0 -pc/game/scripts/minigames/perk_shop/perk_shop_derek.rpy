screen shop_derek_screen:
    tag shop_derek_screen
    modal True
    add "shop_bg" xalign 1.0 yalign 0.4

    imagebutton:
        idle "shop_close"
        hover "shop_close_hover"
        action Return()
        xalign 1.0
        yalign 0.08

    vbox:
        xalign 0.923
        yalign 0.23
        text "English Cheat" style "shop_header_style" xalign 0.5
    vbox:
        xalign 0.912
        yalign 0.38
        text "Math Tools" style "shop_header_style" xalign 0.5
    vbox:
        xalign 0.955
        yalign 0.65
        text "Science Perk: Timer" style "shop_header_style" xalign 0.5
    text "Can be bought from within the mini-game" style "shop_desc_style" xalign 0.968 yalign 0.42
    text "Longer test time, 10% per level" style "shop_desc_style" xalign 0.94 yalign 0.70

    vbox:
        xalign 0.77
        yalign 0.58
        spacing 410 * persistent.scale_factor
        add "shop_level%d" % englishCheatBoost
        add "shop_level%d" % sm_perk_time

    if englishCheatBoost < 3:
        text "$%d" % (englishCheatBoost+1) xalign 0.87 yalign 0.292 text_align 0.5 style "shop_money_style"
    else:
        text "Max" xalign 0.895 yalign 0.292 text_align 0.5 style "shop_max_style"

    if sm_perk_time < 3:
        text "$%d" % (sm_perk_time+1) xalign 0.87 yalign 0.785 text_align 0.5 style "shop_money_style"
    else:
        text "Max" xalign 0.895 yalign 0.775 text_align 0.5 style "shop_max_style"

    hbox:
        xalign 0.955
        yalign 0.50
        spacing 50 * persistent.scale_factor
        imagebutton:
            if math_own_q:
                idle "math_tile_q_idle"
                hover "math_tile_q_idle"
            elif not math_own_q and money > 0:
                idle "math_tile_q_idle"
                hover "math_tile_q_hover"
                action Function(ft_play_coin),SetVariable("math_own_q", True), Function(mny,-1)
            else:
                idle "math_tile_q_disabled_idle"
                hover "math_tile_q_disabled_idle"
        imagebutton:
            if math_own_b:
                idle "math_tile_b_idle"
                hover "math_tile_b_idle"
            elif not math_own_b and money > 0:
                idle "math_tile_b_idle"
                hover "math_tile_b_hover"
                action Function(ft_play_coin),SetVariable("math_own_b", True), Function(mny,-1)
            else:
                idle "math_tile_b_disabled_idle"
                hover "math_tile_b_disabled_idle"
        imagebutton:
            if math_own_query:
                idle "math_tile_query_idle"
                hover "math_tile_query_idle"
            elif not math_own_query and money > 0:
                idle "math_tile_query_idle"
                hover "math_tile_query_hover"
                action Function(ft_play_coin),SetVariable("math_own_query", True), Function(mny,-1)
            else:
                idle "math_tile_query_disabled_idle"
                hover "math_tile_query_disabled_idle"

    if not math_own_q:
        text "{size=-%d}$1{/size}" % (30 * persistent.scale_factor) xalign 0.79 yalign 0.58 text_align 0.5 style "shop_money_style"
    else:
        text "{size=-%d}{color=0094d5}SOLD{/color}{/size}" % (50 * persistent.scale_factor) xalign 0.8 yalign 0.58 text_align 0.5 style "shop_money_style"
    if not math_own_b:
        text "{size=-%d}$1{/size}" % (30 * persistent.scale_factor) xalign 0.87 yalign 0.58 text_align 0.5 style "shop_money_style"
    else:
        text "{size=-%d}{color=0094d5}SOLD{/color}{/size}" % (50 * persistent.scale_factor) xalign 0.876 yalign 0.58 text_align 0.5 style "shop_money_style"
    if not math_own_query:
        text "{size=-%d}$1{/size}" % (30 * persistent.scale_factor) xalign 0.947 yalign 0.58 text_align 0.5 style "shop_money_style"
    else:
        text "{size=-%d}{color=0094d5}SOLD{/color}{/size}" % (50 * persistent.scale_factor) xalign 0.957 yalign 0.58 text_align 0.5 style "shop_money_style"


    imagebutton:
        if englishCheatBoost < 3 and money > englishCheatBoost:
            idle "shop_buy"
            hover "shop_buy_hover"
            action (Function(ft_play_coin),SetVariable("englishCheatBoost",englishCheatBoost+1), Function(mny,-(englishCheatBoost+1)))
        else:
            idle "shop_buy_disabled"
            hover "shop_buy_disabled"
        xalign 1.0
        yalign 0.299

    imagebutton:
        if sm_perk_time < 3 and money > sm_perk_time:
            idle "shop_buy"
            hover "shop_buy_hover"
            action (Function(ft_play_coin),SetVariable("sm_perk_time",sm_perk_time+1), Function(mny,-(sm_perk_time+1)))
        else:
            idle "shop_buy_disabled"
            hover "shop_buy_disabled"
        xalign 1.0
        yalign 0.78
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
