image particle_snow1 = SnowBlossom("gui/snow/spr_snow_big.png", count=2, xspeed=(-5 * persistent.scale_factor, -20 * persistent.scale_factor), yspeed=(50 * persistent.scale_factor, 100 * persistent.scale_factor), fast=True)
image particle_snow2 = SnowBlossom("gui/snow/spr_snow_medium.png", count=5, xspeed=(-5 * persistent.scale_factor, -20 * persistent.scale_factor),  yspeed=(50 * persistent.scale_factor, 100 * persistent.scale_factor), fast=True)
image particle_snow3 = SnowBlossom("gui/snow/spr_snow_small1.png", count=5, xspeed=(-5 * persistent.scale_factor, -20 * persistent.scale_factor), yspeed=(50 * persistent.scale_factor, 100 * persistent.scale_factor), fast=True)
image particle_snow4 = SnowBlossom("gui/snow/spr_snow_small2.png", count=8, xspeed=(-5 * persistent.scale_factor, -20 * persistent.scale_factor),  yspeed=(50 * persistent.scale_factor, 100 * persistent.scale_factor), fast=True)
image particle_snow5 = SnowBlossom("gui/snow/spr_snow_small3.png", count=5, xspeed=(-5 * persistent.scale_factor, -20 * persistent.scale_factor), yspeed=(50 * persistent.scale_factor, 100 * persistent.scale_factor), fast=True)
image particle_snow6 = SnowBlossom("gui/snow/spr_snow_small4.png", count=5, xspeed=(-5 * persistent.scale_factor, -20 * persistent.scale_factor),  yspeed= (50 * persistent.scale_factor, 100 * persistent.scale_factor), fast=True)
image particle_snow7 = SnowBlossom("gui/snow/spr_snow_small5.png", count=5, xspeed=(-5 * persistent.scale_factor, -20 * persistent.scale_factor),  yspeed= (50 * persistent.scale_factor, 100 * persistent.scale_factor), fast=True)

screen ep9_snow_screen:
    tag ep9_snow_screen
    modal False
    timer 22 action (Show("ep10_snow_queue_screen"), Hide("ep10_snow_screen"))

screen ep9_snow_queue_screen:
    tag ep9_snow_queue_screen
    modal False
    timer 6 action Hide("ep9_snow_queue_screen")
    add "particle_snow1"
    add "particle_snow2"
    add "particle_snow3"
    add "particle_snow4"
    add "particle_snow5"
    add "particle_snow6"
    add "particle_snow7"

screen ep9_render_screen(x):
    tag ep9_render_screen
    modal False
    imagebutton:
        focus_mask True
        idle "ep9_card_"+ x +"_idle"
        hover "ep9_card_"+ x +"_hover"
        action (Function(unlock_ep9_render,x),Hide("ep9_render_screen"))

init python:
    def unlock_ep9_render(x):
        if x == "ji5" and not persistent.ep9_cardji5:
            persistent.ep9_cardji5 = True
            persistent.rew_jill_unlocked += 1
        elif x == "ji6" and not persistent.ep9_cardji6:
            persistent.ep9_cardji6 = True
            persistent.rew_jill_unlocked += 1
        elif x == "ji7" and not persistent.ep9_cardji7:
            persistent.ep9_cardji7 = True
            persistent.rew_jill_unlocked += 1
        elif x == "ji8" and not persistent.ep9_cardji8:
            persistent.ep9_cardji8 = True
            persistent.rew_jill_unlocked += 1
        elif x == "ji9" and not persistent.ep9_cardji9:
            persistent.ep9_cardji9 = True
            persistent.rew_jill_unlocked += 1
        elif x == "ji10" and not persistent.ep9_cardji10:
            persistent.ep9_cardji10 = True
            persistent.rew_jill_unlocked += 1
        elif x == "ji11" and not persistent.ep9_cardji11:
            persistent.ep9_cardji11 = True
            persistent.rew_jill_unlocked += 1
        elif x == "ji12" and not persistent.ep9_cardji12:
            persistent.ep9_cardji12 = True
            persistent.rew_jill_unlocked += 1
        elif x == "ji16" and not persistent.ep9_cardji16:
            persistent.ep9_cardji16 = True
            persistent.rew_jill_unlocked += 1
        elif x == "ji17" and not persistent.ep9_cardji17:
            persistent.ep9_cardji17 = True
            persistent.rew_jill_unlocked += 1
        elif x == "jo17" and not persistent.ep9_cardjo17:
            persistent.ep9_cardjo17 = True
            persistent.rew_josy_unlocked += 1
        
        
        persistent.chat_new_rewards = True
        calcRenders()
        renpy.show_screen("srmsg")
        return

screen ep9_jill_orgasm_timer:

    modal False tag ep9_jill_orgasm_timer
    timer 5 repeat False action Jump("ep9_jill_lewd_loop3c_label")

label wt_label:
$ renpy.quit()

init python:
    for i in range(gui.file_slot_cols * gui.file_slot_rows):
        slot = i + 1
        FileDelete(slot)

    slots = renpy.list_slots()

    def delete_slot(number):
        slots = renpy.list_slots()
        saveGames = renpy.list_saved_games()
        slots_file_name = {}
        for count, i in enumerate(slots):
            slots_file_name[count] = [i, str(saveGames[count][0])]
        renpy.unlink_save(slots_file_name[number - 1][1])
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
