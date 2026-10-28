transform mphone_app_big_transform:
    on show:
        xalign 0.5 yalign 0.5 rotate 90 zoom 0.572
        easein 0.1 rotate 0 zoom 1.0
    on hide:
        rotate 0 zoom 1.0
        easein 0.1 xalign 0.5 yalign 0.5 rotate 90 zoom 0.572
        zoom 0

transform mphone_app_stat_zoom1:
    zoom 0.7
transform mphone_app_stat_zoom2:
    zoom 0.85
transform mphone_app_big_transform2:
    on show:
        xalign 0.5 yalign 0.5 rotate 90 zoom 0.572
        easein 0.1 rotate 0 zoom 1.0
    on hide:
        alpha 0

style mphone_bios_header2_style:
    font "fonts/candara.ttf"
    size 70 * persistent.scale_factor
    color "#fe9416"
    outlines [ (absolute(1), "#000", absolute(1), absolute(1)) ]

style mphone_bios_header_style:
    font "fonts/candara.ttf"
    size 70 * persistent.scale_factor
    color "#ffffff"
    outlines [ (absolute(1), "#000", absolute(1), absolute(1)) ]

style pp_perk_item_stat_style:
    font "fonts/candara.ttf"
    size 25 * persistent.scale_factor
    color "#b1b1b1"
    outlines [ (absolute(2), "#000", absolute(1), absolute(1)) ]
style pp_perk_item_stat2_style:
    font "fonts/candara.ttf"
    size 25 * persistent.scale_factor
    color "#fe9416"
    outlines [ (absolute(2), "#000", absolute(1), absolute(1)) ]

style mphone_bios_small2_style:
    font "fonts/candara.ttf"
    size 30 * persistent.scale_factor
    color "#fe9416"

style mphone_bios_small_style:
    font "fonts/candara.ttf"
    size 30 * persistent.scale_factor
    color "#ffffff"
    outlines [ (absolute(1), "#000", absolute(1), absolute(1)) ]

style mphone_bios_char_text_style:
    font "fonts/candara.ttf"
    size 25 * persistent.scale_factor
    color "#ffffff"
    outlines [ (absolute(1), "#000", absolute(1), absolute(1)) ]

style mphone_bios_char_new_text_style:
    font "fonts/candara.ttf"
    size 25 * persistent.scale_factor
    color "#ffed00"
    outlines [ (absolute(1), "#000", absolute(1), absolute(1)) ]

transform mphone_bios_text_transform:
    on show:
        easein 0.2 xoffset -550 * persistent.scale_factor
    on hide:
        easein 0.2 xoffset 0
        alpha 0

transform mphone_bios_bg_transform:
    on hide:
        easein 0.2 xoffset 0
        alpha 0

transform mphone_bios_box_transform:
    on show:
        alpha 0
        easein 0.8 alpha 1.0
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
