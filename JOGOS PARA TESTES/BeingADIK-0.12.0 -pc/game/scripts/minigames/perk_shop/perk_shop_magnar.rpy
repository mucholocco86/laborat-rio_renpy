screen shop_magnar_screen:
    tag shop_magnar_screen
    modal True
    add "shop_bg" xalign 1.0 yalign 0.4

    imagebutton:
        idle "shop_close"
        hover "shop_close_hover"
        action Return()
        xalign 1.0
        yalign 0.08

    vbox:
        xalign 0.955
        yalign 0.43
        spacing 130 * persistent.scale_factor
        text "English booster" style "shop_header_style" xalign 0.5
        text "Math booster" style "shop_header_style" xalign 0.5
        text "Science booster" style "shop_header_style" xalign 0.5
        text "Science Perk: Pencil" style "shop_header_style" xalign 0.5
    text "Use on notepad to check off tasks" style "shop_desc_style" xalign 0.945 yalign 0.74

    vbox:
        xalign 0.77
        yalign 0.43
        spacing 87 * persistent.scale_factor
        add "shop_level%d" % englishBoost
        add "shop_level%d" % mathBoost
        add "shop_level%d" % sm_perk_purity

    if englishBoost < 3:
        text "$%d" % (englishBoost+1) xalign 0.87 yalign 0.28 text_align 0.5 style "shop_money_style"
    else:
        text "Max" xalign 0.89 yalign 0.28 text_align 0.5 style "shop_max_style"
    if mathBoost < 3:
        text "$%d" % (mathBoost+1) xalign 0.87 yalign 0.45 text_align 0.5 style "shop_money_style"
    else:
        text "Max" xalign 0.89 yalign 0.45 text_align 0.5 style "shop_max_style"
    if sm_perk_purity < 3:
        text "$%d" % (sm_perk_purity+1) xalign 0.87 yalign 0.62 text_align 0.5 style "shop_money_style"
    else:
        text "Max" xalign 0.89 yalign 0.62 text_align 0.5 style "shop_max_style"

    if not sm_perk_pencil:
        text "$1" xalign 0.87 yalign 0.82 text_align 0.5 style "shop_money_style"
    else:
        text "{size=-%d}Sold Out{/size}" % (15 * persistent.scale_factor) xalign 0.905 yalign 0.80 text_align 0.5 style "shop_max_style"

    imagebutton:
        if englishBoost < 3 and money > englishBoost:
            idle "shop_buy"
            hover "shop_buy_hover"
            action (Function(ft_play_coin),SetVariable("englishBoost",englishBoost+1), Function(mny,-(englishBoost+1)))
        else:
            idle "shop_buy_disabled"
            hover "shop_buy_disabled"
        xalign 1.0
        yalign 0.285
    imagebutton:
        if mathBoost < 3 and money > mathBoost:
            idle "shop_buy"
            hover "shop_buy_hover"
            action (Function(ft_play_coin),SetVariable("mathBoost",mathBoost+1), Function(mny,-(mathBoost+1)))
        else:
            idle "shop_buy_disabled"
            hover "shop_buy_disabled"
        xalign 1.0
        yalign 0.454
    imagebutton:
        if sm_perk_purity < 3 and money > sm_perk_purity:
            idle "shop_buy"
            hover "shop_buy_hover"
            action (Function(ft_play_coin),SetVariable("sm_perk_purity",sm_perk_purity+1), Function(mny,-(sm_perk_purity+1)))
        else:
            idle "shop_buy_disabled"
            hover "shop_buy_disabled"
        xalign 1.0
        yalign 0.618
    imagebutton:
        if not sm_perk_pencil and money > 0:
            idle "shop_buy"
            hover "shop_buy_hover"
            action (Function(ft_play_coin),SetVariable("sm_perk_pencil",True), Function(mny,-1))
        else:
            idle "shop_buy_disabled"
            hover "shop_buy_disabled"
        xalign 1.0
        yalign 0.811

style shop_header_style:
    font "fonts/collegiate.ttf"
    size 42 * persistent.scale_factor
    color "#2d2d2d"

style shop_max_style:
    font "fonts/collegiate.ttf"
    size 70 * persistent.scale_factor
    color "#055f88"

style shop_money_style:
    font "fonts/cabin-regular.ttf"
    size 80 * persistent.scale_factor
    color "#56e57b"
    outlines [(2, "#2d2d2d", 0, 0)]

style shop_desc_style:
    font "fonts/candara.ttf"
    size 25 * persistent.scale_factor
    color "#2d2d2d"
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
