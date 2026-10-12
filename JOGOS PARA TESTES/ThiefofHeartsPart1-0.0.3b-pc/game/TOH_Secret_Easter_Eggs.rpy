
default persistent.v_secrets_locked = True
default persistent.v_secrets_enabled = not persistent.v_secrets_locked
default persistent.v_secrets_icon_enabled = not persistent.v_secrets_locked
default persistent.v_secrets_reappear = False
default persistent.v_secrets_ep01_03_02_1 = False
default persistent.v_secrets_ep01_03_04_1 = False
default persistent.v_secrets_ep01_06_01_1 = False
default persistent.v_secrets_ep01_07_01_1 = False
default persistent.v_secrets_ep01_13_03_1 = False

default persistent.v_secrets_ep02_01_04_1 = False
default persistent.v_secrets_ep02_02_03_1 = False
default persistent.v_secrets_ep02_03_09_1 = False

default persistent.v_secrets_ep02_03_07_1 = False
default persistent.v_secrets_ep02_03_08_1 = False
default persistent.v_secrets_ep02_03_11_1 = False


default persistent.v_secrets_ep03_01_03_1 = False
default persistent.v_secrets_ep03_01_06_1 = False
default persistent.v_secrets_ep03_03_04_1 = False
default persistent.v_secrets_ep03_04_03_1 = False




default v_ep01_ariel_fantasy_counter = 0
default v_ep01_bella_fantasy_counter = 0
default v_ep01_vivian_fantasy_counter = 0
default v_ep01_megan_fantasy_counter = 0
default v_ep01_mystery_girl_fantasy_counter = 0

init python:

    from ast import literal_eval

init:
    image img_secret_scene_overlay:
        "gui/overlay/secret_scene_overlay.png"

    screen scr_hover_img(img):
        add img yalign 0.98 xalign 0.98

    screen scr_secret_icon(pers_var):
        zorder -10
        $ already_found = getattr(persistent, pers_var)
        if not renpy.get_screen("menu") and not v_mm_open and persistent.v_secrets_enabled and persistent.v_secrets_icon_enabled and (already_found == False or (persistent.v_secrets_reappear and already_found)):
            add "gui/overlay/secret_scene_icon.png" yalign 0.98 xalign 0.98

    screen scr_secret_hotspot(base_image, hotspot_loc, pers_var):
        zorder -10

        $ already_found = getattr(persistent, pers_var)
        if not renpy.get_screen("menu") and not v_mm_open and persistent.v_secrets_icon_enabled and (already_found == False or (persistent.v_secrets_reappear and already_found)):
            imagemap:
                ground base_image
                hotspot (literal_eval(hotspot_loc)) action [Notify("Secret Easter Egg was already unlocked!" if already_found else "Secret Easter Egg Unlocked!"),SetVariable("persistent." + pers_var,True),Hide(),Hide(screen="scr_secret_icon",_layer="ontop"),Hide("scr_hover_img")] hovered If((persistent.v_secrets_icon_enabled) or (already_found and persistent.v_secrets_reappear),ShowTransient("scr_hover_img", img="gui/overlay/secret_scene_icon_hover.png")) unhovered Hide("scr_hover_img")
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
