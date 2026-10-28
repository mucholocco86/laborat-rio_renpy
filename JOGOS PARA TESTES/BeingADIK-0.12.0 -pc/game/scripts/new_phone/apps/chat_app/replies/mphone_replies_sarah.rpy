init python:

    def mphone_chat_get_replies_sarah(idx):
        global mphone_replies
        global mphone_contact_list
        global mphone_next_state
        global mphone_contact_list
        global mphone_chat_history_list
        
        if len(mphone_chat_history_list[idx][4]) == 0:
            return
        
        if mphone_chat_history_list[idx][5] == 1:
            if  mphone_chat_history_list[idx][4] == "1":
                mphone_replies = ["Hey. Thanks for the party; I'm still tired from it.","",""]
                mphone_next_state = ["h2a","",""]
            elif  mphone_chat_history_list[idx][4] == "2a":
                mphone_replies = ["I would too if I went to their party.","What are you up to?",""]
                mphone_next_state = ["h3a","h3b",""]
            elif  mphone_chat_history_list[idx][4] == "3a" or mphone_chat_history_list[idx][4] == "3b":
                mphone_replies = ["You sprung out of the shower when you saw me text you, huh? Desperate much?","Now, that I'd like to see. mphone_emoji_tongue",""]
                mphone_next_state = ["h4a","h4b",""]
            elif  mphone_chat_history_list[idx][4] == "4a" or mphone_chat_history_list[idx][4] == "4b":
                mphone_replies = ["Stop with that \"papi\" shit.","",""]
                mphone_next_state = ["h5a","",""]
            elif  mphone_chat_history_list[idx][4] == "5a":
                mphone_replies = ["If you were here, I would. Damn...","I'm outta here.",""]
                mphone_next_state = ["h6a","h6b",""]
            elif  mphone_chat_history_list[idx][4] == "6a":
                mphone_replies = ["Fuck, I can't. Papi is busy tonight. Crap, now you made me say it.","",""]
                mphone_next_state = ["h7a","",""]
            else:
                
                mphone_replies = ["","",""]
                mphone_next_state = ["","",""]
                mphone_contact_list[idx][2] = False
        return


    def mphone_chat_them_replies_sarah(idx):
        global mphone_replies
        global mphone_contact_list
        global mphone_next_state
        global mphone_chat_history_list
        global mphone_contact_list
        if len(mphone_chat_history_list[idx][4]) == 0:
            return
        
        if mphone_chat_history_list[idx][4][0] == "h":
            mphone_chat_history_list[idx][3].append(True)
            mphone_chat_history_list[idx][4] = mphone_chat_history_list[idx][4][1:]
            if mphone_chat_history_list[idx][5] == 1:
                if mphone_chat_history_list[idx][4] == "2a":
                    mphone_chat_history_list[idx][2].append("If you're tired from one party, try pulling a two-nighter. I dozed off on the alphas' couch halfway through their party.")
                elif mphone_chat_history_list[idx][4] == "3a":
                    mphone_chat_history_list[idx][2].append("Lol. Did you want something? I'm halfway out of the shower.")
                elif mphone_chat_history_list[idx][4] == "3b":
                    mphone_chat_history_list[idx][2].append("I'm halfway out of the shower.")
                elif mphone_chat_history_list[idx][4] == "4a":
                    mphone_chat_history_list[idx][2].append("Yeah, I've been sitting by my phone waiting for you to notice me, papi.")
                elif mphone_chat_history_list[idx][4] == "4b":
                    mphone_chat_history_list[idx][2].append("I'm sure you would, papi.")
                elif mphone_chat_history_list[idx][4] == "5a":
                    mphone_chat_history_list[idx][2].append("Oh, no. I've upset papi. Punish me, papi.")
                    mphone_chat_history_list[idx][3].append(True)
                    mphone_chat_history_list[idx][2].append("chat_sarah_pic1_ep11_thumb")
                    mgallery_add_photo("chat_sarah_pic1_ep11_zoomed")
                elif mphone_chat_history_list[idx][4] == "6a":
                    mphone_chat_history_list[idx][2].append("There's room in the shower for both of us. But you better hurry.")
                elif mphone_chat_history_list[idx][4] == "6b":
                    mphone_chat_history_list[idx][2].append("Hahaha!")
                elif mphone_chat_history_list[idx][4] == "7a":
                    mphone_chat_history_list[idx][2].append("Hahaha!")
                elif mphone_chat_history_list[idx][4][0] == " ":
                    mphone_replies = ["","",""]
                    mphone_next_state = ["","",""]
                    mphone_contact_list[idx][2] = False
        elif mphone_chat_history_list[idx][4][0] == " ":
            mphone_replies = ["","",""]
            mphone_next_state = ["","",""]
            mphone_contact_list[idx][2] = False
        return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
