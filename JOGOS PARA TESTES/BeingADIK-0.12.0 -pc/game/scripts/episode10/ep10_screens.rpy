screen ep10_render_screen(x):
    tag ep10_render_screen
    modal False
    imagebutton:
        focus_mask True
        idle "ep10_card_"+ x +"_idle"
        hover "ep10_card_"+ x +"_hover"
        action (Function(unlock_ep10_render,x),Hide("ep10_render_screen"))

init python:
    def unlock_ep10_render(x):
        if x == "zo1" and not persistent.ep10_cardzo1:
            persistent.ep10_cardzo1 = True
            persistent.rew_zoey_unlocked += 1
        elif x == "zo2" and not persistent.ep10_cardzo2:
            persistent.ep10_cardzo2 = True
            persistent.rew_zoey_unlocked += 1
        elif x == "zo3" and not persistent.ep10_cardzo3:
            persistent.ep10_cardzo3 = True
            persistent.rew_zoey_unlocked += 1
        elif x == "zo4" and not persistent.ep10_cardzo4:
            persistent.ep10_cardzo4 = True
            persistent.rew_zoey_unlocked += 1
        elif x == "zo5" and not persistent.ep10_cardzo5:
            persistent.ep10_cardzo5 = True
            persistent.rew_zoey_unlocked += 1
        elif x == "zo6" and not persistent.ep10_cardzo6:
            persistent.ep10_cardzo6 = True
            persistent.rew_zoey_unlocked += 1
        elif x == "zo7" and not persistent.ep10_cardzo7:
            persistent.ep10_cardzo7 = True
            persistent.rew_zoey_unlocked += 1
        elif x == "zo8" and not persistent.ep10_cardzo8:
            persistent.ep10_cardzo8 = True
            persistent.rew_zoey_unlocked += 1
        elif x == "zo17" and not persistent.ep10_cardzo17:
            persistent.ep10_cardzo17 = True
            persistent.rew_zoey_unlocked += 1
        elif x == "zo13" and not persistent.ep10_cardzo13:
            persistent.ep10_cardzo13 = True
            persistent.rew_zoey_unlocked += 1
        elif (x == "zo18" or x == "zo18b") and not persistent.ep10_cardzo18:
            persistent.ep10_cardzo18 = True
            persistent.rew_zoey_unlocked += 1
        persistent.chat_new_rewards = True
        calcRenders()
        renpy.show_screen("srmsg")
        return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
