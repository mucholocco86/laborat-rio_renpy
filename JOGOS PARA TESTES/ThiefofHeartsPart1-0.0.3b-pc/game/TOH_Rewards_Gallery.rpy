init:
    default persistent.megan_gallery_unlocked = False
    default persistent.juliet_gallery_unlocked = False
    default persistent.zora_gallery_unlocked = False

init python:
    v_rewards_who = "ariel"
    v_rewards_min_digits = {
        
        

        'ariel': 1,
        'bella': 1,
        'vivian': 1,
        'megan': 1,
        'juliet': 1,
        'zora': 1
    }


    v_rewards_counts = {}
    for who, digits in v_rewards_min_digits.items():
        i = 0
        while renpy.loadable("images/rewards/lewd gallery/" + who + "/lewd_" + who + "_" + str(i + 1) + ".jpg"):
            i += 1
            varname = 'v_rewards_' + who + '_' + str(i).zfill(digits)
            if getattr(persistent, varname) == None:
                setattr(persistent, varname, False)
        v_rewards_counts[who] = i

    def count_unlocked_rewards(who):
        rv = 0
        for i in range(1, v_rewards_counts[who] + 1):
            if getattr(persistent, 'v_rewards_' + who + '_' + str(i).zfill(v_rewards_min_digits[who])):
                rv += 1
        if rv == v_rewards_counts[who]:
            return '{color=#33ff33}%d/%d{/color}' % (rv, v_rewards_counts[who])
        else:
            return '%d/%d' % (rv, v_rewards_counts[who])




screen scr_rewards(v_image_donut, pers_var):
    zorder -10
    $ already_found = getattr(persistent, pers_var)
    if persistent.v_extra_settings_donuts_enabled == False and already_found:
        textbutton "" action NullAction()
    else:
        imagebutton:
            idle v_image_donut
            focus_mask True
            action [Hide ("scr_rewards"),SetVariable("persistent." + pers_var, True),Notify("This secret image was already unlocked!" if already_found else "New Secret Image Unlocked!")]



init python:

    def rewards_unlock(name,number):
        var_name = "v_rewards_"+name+"_"+str(number)
        already_found = getattr(persistent, var_name)
        if already_found:
            pass
        else:
            renpy.notify("A new secret image was unlocked!")
            setattr(store.persistent, var_name, True)

    def wallpaper_unlock(number):
        var_slot = ('v_mm_background_slot' + str(number))
        already_found = getattr(persistent, var_slot)
        if already_found:
            pass
        else:
            renpy.notify("A new wallpaper was unlocked!")
            setattr(store.persistent, var_slot, True)

    def rewards_count_range(who,start,end):
        
        rv = 0
        v_counter = start
        for i in range(start, end + 1):
            already_found = getattr(persistent, 'v_rewards_' + who + '_' + str(v_counter))
            if already_found:
                rv += 1
            v_counter +=1
        
        return str(rv)+"/"+str(end-start+1)













screen scr_mm_rewards_menu:
    key "game_menu" action [Hide("scr_mm_rewards_menu",dissolve),renpy.restart_interaction, SetVariable('quick_menu', False)]

    add "rewards_background"

    imagebutton:
        idle "img_gradient_[persistent.v_mm_gradient[persistent.v_mm_gradient_order]]" action NullAction()


    imagebutton:
        xalign 0.01
        yalign 0.98
        auto "btn_mm_back_%s" action [Hide("scr_mm_rewards_menu",dissolve),renpy.restart_interaction, SetVariable('quick_menu', False)]

    imagebutton:
        xalign 0.98
        yalign 0.98
        auto "btn_mm_exit_%s" action [Hide("scr_mm_rewards_menu",dissolve),Hide("scr_mm_main",dissolve),renpy.restart_interaction, SetVariable('quick_menu', True), SetVariable('v_mm_open', False)]


    frame:
        xalign 0.3
        yalign 0.05
        has hbox
        imagebutton:
            auto "btn_ariel_rewards_%s" action [Show("scr_mm_rewards_images",dissolve),SetVariable ("v_rewards_who","ariel")]
            foreground Text(_(count_unlocked_rewards('ariel')),style="generic_button_style_outline")
        imagebutton:
            auto "btn_bella_rewards_%s" action [Show("scr_mm_rewards_images",dissolve),SetVariable ("v_rewards_who","bella")]
            foreground Text(_(count_unlocked_rewards('bella')),style="generic_button_style_outline")
        imagebutton:
            auto "btn_vivian_rewards_%s" action [Show("scr_mm_rewards_images",dissolve),SetVariable ("v_rewards_who","vivian")]
            foreground Text(_(count_unlocked_rewards('vivian')),style="generic_button_style_outline")
        if persistent.megan_gallery_unlocked:
            imagebutton:
                auto "btn_megan_rewards_%s" action [Show("scr_mm_rewards_images",dissolve),SetVariable ("v_rewards_who","megan")]
                foreground Text(_(count_unlocked_rewards('megan')),style="generic_button_style_outline")
        else:
            imagebutton:
                auto "btn_question_%s" action NullAction()

        if persistent.juliet_gallery_unlocked:
            imagebutton:
                auto "btn_juliet_rewards_%s" action [Show("scr_mm_rewards_images",dissolve),SetVariable ("v_rewards_who","juliet")]
                foreground Text(_(count_unlocked_rewards('juliet')),style="generic_button_style_outline")
        else:
            imagebutton:
                auto "btn_question_%s" action NullAction()


        if persistent.zora_gallery_unlocked:
            imagebutton:
                auto "btn_zora_rewards_%s" action [Show("scr_mm_rewards_images",dissolve),SetVariable ("v_rewards_who","zora")]
                foreground Text(_(count_unlocked_rewards('zora')),style="generic_button_style_outline")
        else:
            imagebutton:
                auto "btn_question_%s" action NullAction()


        imagebutton:
            auto "btn_question_%s" action NullAction()



screen scr_mm_rewards_images:
    key "game_menu" action [Hide("scr_mm_rewards_images",dissolve),renpy.restart_interaction, SetVariable('quick_menu', False)]

    add "rewards_background"

    imagebutton:
        idle "img_gradient_[persistent.v_mm_gradient[persistent.v_mm_gradient_order]]" action NullAction()

    frame:
        xalign 0.02
        yalign 0.05
        imagebutton idle "btn_[v_rewards_who]_rewards_hover" action NullAction()



    vpgrid:
        xalign 0.55
        yalign 0.01
        ysize 0.60
        cols 4
        spacing 10
        draggable True
        mousewheel True

        scrollbars "vertical"
        side_xalign 0.5

        for i in range(1, v_rewards_counts[v_rewards_who] + 1):
            vbox xalign 0.5 yalign 0.5:
                if getattr(persistent, 'v_rewards_' + v_rewards_who + '_' + str(i).zfill(v_rewards_min_digits[v_rewards_who])):
                    imagebutton:
                        focus_mask True
                        idle "images/rewards/lewd gallery/[v_rewards_who]/thumbs/lewd_[v_rewards_who]_{0}_thumb_idle.jpg".format(i)
                        hover "images/rewards/lewd gallery/[v_rewards_who]/thumbs/lewd_[v_rewards_who]_{0}_thumb_hover.jpg".format(i)
                        action Show("scr_lewd",dissolve, i=i)
                else:
                    add "screens/locked.png"
                text "[i]" xalign 0.5 yalign 0.5 outlines [ (3, "#000000", 0, 0) ]




    imagebutton:
        xalign 0.01
        yalign 0.98
        auto "btn_mm_back_%s" action [Hide("scr_mm_rewards_images",dissolve),renpy.restart_interaction, SetVariable('quick_menu', False)]

    imagebutton:
        xalign 0.98
        yalign 0.98
        auto "btn_mm_exit_%s" action [Hide("scr_mm_rewards_menu",dissolve),Hide("scr_mm_rewards_images",dissolve),Hide("scr_mm_main",dissolve),renpy.restart_interaction, SetVariable('quick_menu', True), SetVariable('v_mm_open', False)]





init:
    $ var_ext2 = ""

screen scr_lewd(i):
    $ tooltip = GetTooltip()
    on "hide" action SetVariable("var_ext2","")
    $ var_img = "images/rewards/lewd gallery/[v_rewards_who]/lewd_[v_rewards_who]_{0}".format(i)
    $ var_ext = var_ext2 + ".jpg"

    imagebutton:
        idle var_img + var_ext
        action NullAction()

    vbox:
        xalign 0.02
        yalign 0.02
        style_prefix "radio"
        textbutton _("#1") action SetVariable("var_ext2","") text_outlines [ (3, "#000000", 0, 0) ]
        textbutton _("#2") action SetVariable("var_ext2","A") text_outlines [ (3, "#000000", 0, 0) ]
        if persistent.v_lewd_images_extra_enabled:
            textbutton _("#3") action SetVariable("var_ext2","B") text_outlines [ (3, "#000000", 0, 0) ]
            textbutton _("#4") action SetVariable("var_ext2","C") text_outlines [ (3, "#000000", 0, 0) ]
        else:
            textbutton _("{color=#5e5e5e}#3{/color}") action OpenURL(url="https://mrdotsgames.com/become-a-supporter") tooltip "Unlocks with a secret code obtained at our $20 tier." text_style "vault_text_style"
            textbutton _("{color=#5e5e5e}#4{/color}") action OpenURL(url="https://mrdotsgames.com/become-a-supporter") tooltip "Unlocks with a secret code obtained at our $20 tier." text_style "vault_text_style"

    vbox:
        xalign 0.5
        yalign 1.0
        if tooltip:
            text "[tooltip]"

    imagebutton:
        xalign 0.01
        yalign 0.98
        auto "btn_mm_back_%s" action [Hide("scr_lewd",dissolve),renpy.restart_interaction, SetVariable('quick_menu', False)]


    imagebutton:
        xalign 0.98
        yalign 0.98
        auto "btn_mm_exit_%s" action [Hide("scr_lewd",dissolve),Hide("scr_mm_rewards_menu",dissolve),Hide("scr_mm_rewards_images",dissolve),Hide("scr_mm_main",dissolve),renpy.restart_interaction, SetVariable('quick_menu', True), SetVariable('v_mm_open', False)]
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
