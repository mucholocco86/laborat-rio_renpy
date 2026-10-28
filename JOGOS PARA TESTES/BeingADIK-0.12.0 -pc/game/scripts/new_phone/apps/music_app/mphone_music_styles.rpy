style mphone_music_bar_style:
    font "fonts/candara.ttf"
    size 14 * persistent.scale_factor
    color "#ffffff"
    outlines [ (absolute(2), "#000", absolute(1), absolute(1)) ]

style mphone_music_text_button_style:
    font "fonts/candara.ttf"
    size 15 * persistent.scale_factor
    color "#ffffff"
    hover_color "#fe9416"
    outlines [ (absolute(2), "#000", absolute(1), absolute(1)) ]

style mphone_music_hbar_style:
    xmaximum 45 * persistent.scale_factor
    ymaximum 8 * persistent.scale_factor
    top_bar Frame("mphone_music_bar_white", 5 * persistent.scale_factor, 5 * persistent.scale_factor)
    bottom_bar Frame("mphone_music_bar_grey", 5 * persistent.scale_factor, 5 * persistent.scale_factor)
    thumb Frame("mphone_music_bar_white", 5 * persistent.scale_factor, 5 * persistent.scale_factor)
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
