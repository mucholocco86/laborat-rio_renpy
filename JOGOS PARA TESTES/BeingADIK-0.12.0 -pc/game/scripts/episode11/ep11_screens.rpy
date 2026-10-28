screen ep11_render_screen(x):
    tag ep11_render_screen
    modal False
    imagebutton:
        focus_mask True
        idle "ep11_card_"+ x +"_idle"
        hover "ep11_card_"+ x +"_hover"
        action (Function(unlock_ep11_render,x),Hide("ep11_render_screen"))

init python:
    def unlock_ep11_render(x):
        if x == "ly1" and not persistent.ep11_cardly1:
            persistent.ep11_cardly1 = True
            persistent.rew_lily_unlocked += 1
        elif x == "ly2" and not persistent.ep11_cardly2:
            persistent.ep11_cardly2 = True
            persistent.rew_lily_unlocked += 1
        elif x == "my2" and not persistent.ep11_cardmy2:
            persistent.ep11_cardmy2 = True
            persistent.rew_maya_unlocked += 1
        elif x == "my3" and not persistent.ep11_cardmy3:
            persistent.ep11_cardmy3 = True
            persistent.rew_maya_unlocked += 1
        elif x == "my4" and not persistent.ep11_cardmy4:
            persistent.ep11_cardmy4 = True
            persistent.rew_maya_unlocked += 1
        elif x == "my5" and not persistent.ep11_cardmy5:
            persistent.ep11_cardmy5 = True
            persistent.rew_maya_unlocked += 1
        elif x == "ly3" and not persistent.ep11_cardly3:
            persistent.ep11_cardly3 = True
            persistent.rew_lily_unlocked += 1
        elif x == "ly4" and not persistent.ep11_cardly4:
            persistent.ep11_cardly4 = True
            persistent.rew_lily_unlocked += 1
        elif x == "ly5" and not persistent.ep11_cardly5:
            persistent.ep11_cardly5 = True
            persistent.rew_lily_unlocked += 1
        elif x == "ly6" and not persistent.ep11_cardly6:
            persistent.ep11_cardly6 = True
            persistent.rew_lily_unlocked += 1
        elif x == "ly7" and not persistent.ep11_cardly7:
            persistent.ep11_cardly7 = True
            persistent.rew_lily_unlocked += 1
        elif x == "ly8" and not persistent.ep11_cardly8:
            persistent.ep11_cardly8 = True
            persistent.rew_lily_unlocked += 1
        elif x == "ly9" and not persistent.ep11_cardly9:
            persistent.ep11_cardly9 = True
            persistent.rew_lily_unlocked += 1
        elif x == "ly10" and not persistent.ep11_cardly10:
            persistent.ep11_cardly10 = True
            persistent.rew_lily_unlocked += 1
        elif x == "ly11" and not persistent.ep11_cardly11:
            persistent.ep11_cardly11 = True
            persistent.rew_lily_unlocked += 1
        elif x == "ly12" and not persistent.ep11_cardly12:
            persistent.ep11_cardly12 = True
            persistent.rew_lily_unlocked += 1
        elif x == "ly13" and not persistent.ep11_cardly13:
            persistent.ep11_cardly13 = True
            persistent.rew_lily_unlocked += 1
        elif x == "ly14" and not persistent.ep11_cardly14:
            persistent.ep11_cardly14 = True
            persistent.rew_lily_unlocked += 1
        
        persistent.chat_new_rewards = True
        calcRenders()
        renpy.show_screen("srmsg")
        return

screen ep11_cookie_timer:
    tag ep11_cookie_timer
    modal False
    timer 240 repeat False action Jump("ep11_bella_lewd_cookie_label")

transform show_slow:
    alpha .0
    linear 2.0 alpha .0
    linear 4.0 alpha 1.0
transform hide_slow:
    alpha 1.0
    linear 2.0 alpha 1.0
    linear 4.0 alpha .0
transform hide_slow2:
    zoom 0.96
    alpha 1.0
    linear 2.0 alpha 1.0
    linear 4.0 alpha .0
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
