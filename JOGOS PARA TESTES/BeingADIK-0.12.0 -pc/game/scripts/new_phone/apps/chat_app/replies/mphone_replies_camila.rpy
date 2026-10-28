init python:

    def mphone_chat_get_replies_camila(idx):
        global mphone_replies
        global mphone_contact_list
        global mphone_next_state
        global mphone_contact_list
        global ep11_zoey_kiss
        global mphone_chat_history_list
        
        if len(mphone_chat_history_list[idx][4]) == 0:
            return
        
        if mphone_chat_history_list[idx][5] == 1:
            if  mphone_chat_history_list[idx][4] == "1":
                mphone_replies = ["I'm glad to hear it's not just me who gets tired post-orgasm. mphone_emoji_laugh","You're welcome. mphone_emoji_evil",""]
                mphone_next_state = ["h2a","h2b",""]
            else:
                
                mphone_replies = ["","",""]
                mphone_next_state = ["","",""]
                mphone_contact_list[idx][2] = False
        elif mphone_chat_history_list[idx][5] == 2:
            if  mphone_chat_history_list[idx][4] == "1":
                mphone_replies = ["I think you repaid me in full with this one. mphone_emoji_evil","",""]
                mphone_next_state = ["h2a","",""]
            elif  mphone_chat_history_list[idx][4] == "2a":
                mphone_replies = ["Yep, you blew it.","",""]
                mphone_next_state = ["h3a","",""]
            elif  mphone_chat_history_list[idx][4] == "3a":
                if ep11_zoey_kiss == 2:
                    mphone_replies = ["We'll see... The thing is, I'm not sure if I can owe you one. We'll talk.","",""]
                    mphone_next_state = ["h4c","",""]
                else:
                    mphone_replies = ["Aha, I see how it is. You pulled the switcheroo on me.","It's finals week, Cammy. Can I owe you after?",""]
                    mphone_next_state = ["h4a","h4b",""]
            else:
                
                mphone_replies = ["","",""]
                mphone_next_state = ["","",""]
                mphone_contact_list[idx][2] = False
        return


    def mphone_chat_them_replies_camila(idx):
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
                if mphone_chat_history_list[idx][4] == "1":
                    mphone_chat_history_list[idx][2].append("I'm sitting in class trying to focus, but you fucked me too good. Whatever the teacher is saying is going in one ear and out the other. Thanks for that (read that as genuine and sarcastic at the same time). mphone_emoji_heart")
                    mphone_chat_history_list[idx][3].append(True)
                    mphone_chat_history_list[idx][2].append("chat_camila_pic1_ep11_thumb")
                    mgallery_add_photo("chat_camila_pic1_ep11_zoomed")
                elif mphone_chat_history_list[idx][4] == "2a":
                    mphone_chat_history_list[idx][2].append("I'm not tired; I'm satisfied. So satisfied. mphone_emoji_kiss")
                elif mphone_chat_history_list[idx][4] == "2b":
                    mphone_chat_history_list[idx][2].append("mphone_emoji_kiss")
                elif mphone_chat_history_list[idx][4][0] == " ":
                    mphone_replies = ["","",""]
                    mphone_next_state = ["","",""]
                    mphone_contact_list[idx][2] = False
            elif mphone_chat_history_list[idx][5] == 2:
                if mphone_chat_history_list[idx][4] == "1":
                    mphone_chat_history_list[idx][2].append("Don't forget that I owe you one. mphone_emoji_cool mphone_emoji_tongue")
                    mphone_chat_history_list[idx][3].append(True)
                    mphone_chat_history_list[idx][2].append("chat_camila_pic2_ep11_thumb")
                    mgallery_add_photo("chat_camila_pic2_ep11_zoomed")
                elif mphone_chat_history_list[idx][4] == "2a":
                    mphone_chat_history_list[idx][2].append("Oh, shoot. I wanted to owe you one...")
                elif mphone_chat_history_list[idx][4] == "3a":
                    mphone_chat_history_list[idx][3].append(True)
                    mphone_chat_history_list[idx][2].append("chat_camila_pic3_ep11_thumb")
                    mgallery_add_photo("chat_camila_pic3_ep11_zoomed")
                    mphone_chat_history_list[idx][2].append("Not so fast. Now you owe ME one. mphone_emoji_evil mphone_emoji_laugh")
                elif mphone_chat_history_list[idx][4] == "4a" or mphone_chat_history_list[idx][4] == "4b":
                    mphone_chat_history_list[idx][2].append("You owe me. I owe you. Who cares? Let's get together soon. mphone_emoji_eggplant")
                elif mphone_chat_history_list[idx][4] == "4c":
                    mphone_chat_history_list[idx][2].append("You can't weasel your way out of it. You owe me. mphone_emoji_tongue")
                elif mphone_chat_history_list[idx][4] == " ":
                    mphone_replies = ["","",""]
                    mphone_next_state = ["","",""]
                    mphone_contact_list[idx][2] = False
        elif mphone_chat_history_list[idx][4][0] == " ":
            mphone_replies = ["","",""]
            mphone_next_state = ["","",""]
            mphone_contact_list[idx][2] = False
        return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
