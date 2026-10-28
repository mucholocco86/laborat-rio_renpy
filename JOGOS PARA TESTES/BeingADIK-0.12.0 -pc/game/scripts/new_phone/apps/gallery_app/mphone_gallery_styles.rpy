style mphone_custom_wallpaper_style:
    font "fonts/candara.ttf"
    size 30 * persistent.scale_factor
    color "#ffffff"
    hover_color "#fe9416"
    outlines [ (absolute(2), "#000", absolute(1), absolute(1)) ]

style mphone_gallery_header_style:
    font "fonts/candara.ttf"
    size 40 * persistent.scale_factor
    color "#ffffff"

transform mphone_gallery_button_hide_transform:
    on hover:
        alpha 1.0
    on idle:
        alpha 1.0
        ease 3 alpha 0.0

    alpha 1.0
    ease 3 alpha 0.0
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
