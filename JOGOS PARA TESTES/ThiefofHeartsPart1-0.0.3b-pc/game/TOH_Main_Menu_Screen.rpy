init:
    $ persistent.v_mm_background = 0
    $ persistent.v_mm_custom_background = True
    $ persistent.v_mm_custom_background_imagename = "images/gui/wallpapers/img_background_0.jpg"
    $ persistent.v_mm_gradient = ["black","purple","red","blue","white","disabled"]
    $ persistent.v_mm_gradient_order = 0
    $ v_mm_open = False
    $ v_mm_available = False


    $ persistent.v_mm_background_slot0 = True
    $ persistent.v_mm_background_slot1 = True
    $ persistent.v_mm_background_slot2 = True
    if (persistent.v_mm_background_lucy_1 == True):
        $ persistent.v_mm_background_slot3 = True
    else:
        $ persistent.v_mm_background_slot3 = False

    if (persistent.v_mm_background_bella_1 == True):
        $ persistent.v_mm_background_slot4 = True
    else:
        $ persistent.v_mm_background_slot4 = False

    if (persistent.v_mm_background_bella_2 == True):
        $ persistent.v_mm_background_slot5 = True
    else:
        $ persistent.v_mm_background_slot5 = False



screen toh_main_game_screen:

    imagebutton:
        xalign 0.01 yalign 0.01
        auto "gui/menubuttons/btn_mm_settings_%s.png"
        if v_mm_available:
            action [Show("scr_mm_main",dissolve), SetVariable('v_mm_open', True), renpy.restart_interaction, SetVariable('quick_menu', False)]
        else:
            action NullAction()






screen scr_mm_main:
    modal True
    $ tooltip = GetTooltip()
    key "game_menu" action [Hide("scr_mm_main",dissolve),renpy.restart_interaction, SetVariable('quick_menu', True), SetVariable('v_mm_open', False)]

    if persistent.v_mm_custom_background:
        imagebutton:
            idle "[persistent.v_mm_custom_background_imagename]" action NullAction()
    else:
        imagebutton:
            idle "img_background_[persistent.v_mm_background]" action NullAction()


    imagebutton:
        idle "img_gradient_[persistent.v_mm_gradient[persistent.v_mm_gradient_order]]" action NullAction()

    imagebutton:
        idle "img_mm_horizontal_line" action NullAction()


    imagebutton:
        xalign 0.01
        yalign 0.98
        auto "btn_mm_exit_%s" action [Hide("scr_mm_main",dissolve),renpy.restart_interaction, SetVariable('quick_menu', True), SetVariable('v_mm_open', False)]

    hbox:
        xalign 0.48
        yalign 0.95
        spacing 30

        if not main_menu:
            imagebutton:
                auto "btn_mm_tasks_%s"
                action [Show("scr_mm_tasks_menu",dissolve),renpy.restart_interaction, SetVariable('quick_menu', False)]
                tooltip "Tasks"

            imagebutton:
                auto "btn_mm_contacts_%s"
                action [Show("scr_mm_characters_menu",dissolve),renpy.restart_interaction, SetVariable('quick_menu', False)]
                tooltip "Contacts"

            imagebutton:
                auto "btn_mm_stats_%s"
                action [Show("scr_mm_stats_menu",dissolve),renpy.restart_interaction, SetVariable('quick_menu', False)]
                tooltip "Relationships"

        imagebutton:
            auto "btn_mm_vault_%s"
            action [Show("scr_mm_vault_menu",dissolve),renpy.restart_interaction, SetVariable('quick_menu', False)]
            tooltip "The Vault"

        imagebutton:
            auto "btn_mm_rewards_%s"
            action [Show("scr_mm_rewards_menu",dissolve),renpy.restart_interaction, SetVariable('quick_menu', False)]
            tooltip "Achievements"

        imagebutton:
            auto "btn_mm_sex_%s"
            action [Show("scr_mm_replay_menu",dissolve),renpy.restart_interaction, SetVariable('quick_menu', False)]
            tooltip "Replay and Fantasy Scenes Gallery"

        imagebutton:
            auto "btn_mm_wallpaper_%s"
            action [Show("scr_mm_wallpaper",dissolve),renpy.restart_interaction, SetVariable('quick_menu', False)]
            tooltip "Wallpaper"

    if tooltip:
        text "[tooltip]" outlines [(2, "#000000", 1, 1)] xalign 0.5 yalign 0.85

screen scr_mm_wallpaper:
    $ v_mm_background_max = 2

    key "game_menu" action [Hide("scr_mm_wallpaper",dissolve),renpy.restart_interaction, SetVariable('quick_menu', False)]


    if persistent.v_mm_custom_background:
        imagebutton:
            idle "[persistent.v_mm_custom_background_imagename]" action NullAction()
    else:
        imagebutton:
            idle "img_background_[persistent.v_mm_background]" action NullAction()


    imagebutton:
        idle "img_gradient_[persistent.v_mm_gradient[persistent.v_mm_gradient_order]]" action NullAction()

    imagebutton:
        idle "img_mm_horizontal_line_2" action NullAction()


    hbox:
        xalign 0.475
        yalign 0.85
        if renpy.variant("small"):
            spacing 300
        else:
            spacing 390
        text _("WALLPAPER")
        text _("GRADIENT")






    imagebutton:
        xalign 0.98
        yalign 0.98
        if (getattr(persistent, 'v_mm_custom_background_imagename') == "images/gui/wallpapers/bg_wallpaper_locked.png"):
            auto "btn_mm_exit_%s" action [Hide("scr_mm_wallpaper",dissolve),Hide("scr_mm_main",dissolve),renpy.restart_interaction, SetVariable('quick_menu', True), SetVariable('v_mm_open', False),SetField (persistent, 'v_mm_background', 0),SetField(persistent, 'v_mm_custom_background_imagename',"images/gui/wallpapers/img_background_0.jpg")]
        else:
            auto "btn_mm_exit_%s" action [Hide("scr_mm_wallpaper",dissolve),Hide("scr_mm_main",dissolve),renpy.restart_interaction, SetVariable('quick_menu', True), SetVariable('v_mm_open', False)]



    hbox:
        xalign 0.325
        yalign 0.92


        imagebutton:
            auto "btn_wallpaper_previous_%s"
            if (persistent.v_mm_background > 0 and getattr(persistent, ('v_mm_background_slot' + str(persistent.v_mm_background-1))) == True):
                action [SetField (persistent, 'v_mm_background', persistent.v_mm_background-1),SetField(persistent, 'v_mm_custom_background_imagename',"images/gui/wallpapers/img_background_" + str(persistent.v_mm_background-1) + ".jpg")]
            elif (persistent.v_mm_background > 0):
                action [SetField (persistent, 'v_mm_background', persistent.v_mm_background-1),SetField(persistent, 'v_mm_custom_background_imagename',"images/gui/wallpapers/bg_wallpaper_locked.png")]

        text _("{size=25}WALLPAPER #[persistent.v_mm_background]{/size}")

        imagebutton:
            auto "btn_wallpaper_next_%s"
            if (persistent.v_mm_background < 5 and getattr(persistent, ('v_mm_background_slot' + str(persistent.v_mm_background+1))) == True):
                action [SetField (persistent, 'v_mm_background', persistent.v_mm_background+1),SetField(persistent, 'v_mm_custom_background_imagename',"images/gui/wallpapers/img_background_" + str(persistent.v_mm_background+1) + ".jpg")]
            elif (persistent.v_mm_background < 5):
                action [SetField (persistent, 'v_mm_background', persistent.v_mm_background+1),SetField(persistent, 'v_mm_custom_background_imagename',"images/gui/wallpapers/bg_wallpaper_locked.png")]



    hbox:
        xalign 0.645
        yalign 0.92


        imagebutton:
            auto "btn_wallpaper_previous_%s"
            if persistent.v_mm_gradient_order == 0:
                action SetField (persistent,'v_mm_gradient_order', 0)
            else:
                action SetField (persistent,'v_mm_gradient_order', persistent.v_mm_gradient_order-1)

        text _("{size=25}[persistent.v_mm_gradient[persistent.v_mm_gradient_order]]{/size}")


        imagebutton:
            auto "btn_wallpaper_next_%s"
            if persistent.v_mm_gradient_order == 5:
                action SetField (persistent,'v_mm_gradient_order', 5)
            else:
                action SetField (persistent,'v_mm_gradient_order', persistent.v_mm_gradient_order+1)
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
