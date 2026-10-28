style eng_style_word:
    size 80 * persistent.scale_factor
    font "fonts/bradhitc.ttf"
    color "#2b2b2b"

style eng_style_word2:
    size 100 * persistent.scale_factor
    font "fonts/bradhitc.ttf"
    color "#2b2b2b"

style eng_style_words:
    size 40 * persistent.scale_factor
    font "fonts/bradhitc.ttf"
    color "#2b2b2b"

style eng_style_titles:
    size 20 * persistent.scale_factor
    font "fonts/cabin-regular.ttf"
    color "#2b2b2b"

init -5 python:
    style.english_bar_style = Style(style.default)
    style.english_bar_style.left_bar = Frame("left_var", 0, 0)
    style.english_bar_style.right_bar = Frame("right_var", 0, 0)
    style.english_bar_style.ymaximum = 20 * persistent.scale_factor 

transform alpha_dissolve:
    alpha 0.0
    linear 0.5 alpha 1.0
    on hide:
        linear 0.5 alpha 0
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
