init python:

    def mphone_chat_get_replies_sage(idx):
        global mphone_replies
        global mphone_contact_list
        global mphone_next_state
        global mphone_contact_list
        global mphone_chat_history_list
        global pathMayaJosy
        global affinity
        
        if len(mphone_chat_history_list[idx][4]) == 0:
            return
        
        if mphone_chat_history_list[idx][5] == 4:
            if  mphone_chat_history_list[idx][4] == "1":
                mphone_replies = ["Hilarious... Can you delete that one, or will I face another embarrassment on campus soon?","Would.",""]
                mphone_next_state = ["h2a","h2b",""]
            elif  mphone_chat_history_list[idx][4] == "2a":
                mphone_replies = ["Then don't send it to me. Let me forget about it, please.","Do you get off to it or what?",""]
                mphone_next_state = ["h3a","h3b",""]
            elif  mphone_chat_history_list[idx][4] == "2b" or mphone_chat_history_list[idx][4] == "3a" or mphone_chat_history_list[idx][4] == "3b":
                mphone_replies = ["See you soon. I'm almost ready here.","",""]
                mphone_next_state = ["h3c","",""]
            elif  mphone_chat_history_list[idx][4] == "3c":
                mphone_replies = ["I already put on a shirt.","Put on a nice bra. Got it.",""]
                mphone_next_state = ["h4a","h4b",""]
            elif  mphone_chat_history_list[idx][4] == "4a" or mphone_chat_history_list[idx][4] == "4b":
                mphone_replies = ["You're so hot in that... Are you wearing it tonight?","",""]
                mphone_next_state = ["h5a","",""]
            elif  mphone_chat_history_list[idx][4] == "5a":
                if ep11_sage_love == 2:
                    mphone_replies = ["Love you too. mphone_emoji_heart","",""]
                else:
                    mphone_replies = ["See you soon. Thanks for the pictures. mphone_emoji_smile","",""]
                mphone_next_state = [" ","",""]
            else:
                
                mphone_replies = ["","",""]
                mphone_next_state = ["","",""]
                mphone_contact_list[idx][2] = False
        return


    def mphone_chat_them_replies_sage(idx):
        global mphone_replies
        global mphone_contact_list
        global mphone_next_state
        global mphone_chat_history_list
        global mphone_contact_list
        global name
        global task_list
        global optional_task_list
        global ep11_sage_love
        
        if len(mphone_chat_history_list[idx][4]) == 0:
            return
        
        if mphone_chat_history_list[idx][4][0] == "h":
            mphone_chat_history_list[idx][3].append(True)
            mphone_chat_history_list[idx][4] = mphone_chat_history_list[idx][4][1:]
            if mphone_chat_history_list[idx][5] == 4:
                if mphone_chat_history_list[idx][4] == "1":
                    mphone_chat_history_list[idx][2].append("chat_sage_pic1_ep11_thumb")
                    mgallery_add_photo("chat_sage_pic1_ep11_zoomed")
                    mphone_chat_history_list[idx][3].append(True)
                    mphone_chat_history_list[idx][2].append("Look at this hot girl I found on my phone. mphone_emoji_laugh mphone_emoji_tongue")
                elif mphone_chat_history_list[idx][4] == "2a":
                    mphone_chat_history_list[idx][2].append("I would never leak this to someone. It's for my eyes only.")
                elif mphone_chat_history_list[idx][4] == "2b":
                    mphone_chat_history_list[idx][2].append("LOL mphone_emoji_laugh mphone_emoji_eggplant")
                elif mphone_chat_history_list[idx][4] == "3a":
                    mphone_chat_history_list[idx][2].append("Never. I'm gonna make it my screensaver. Can't wait for tonight. mphone_emoji_smile")
                elif mphone_chat_history_list[idx][4] == "3b":
                    mphone_chat_history_list[idx][2].append("Oh, yeah. Men in bras are totally my kink. mphone_emoji_evil")
                elif mphone_chat_history_list[idx][4] == "3c":
                    mphone_chat_history_list[idx][2].append("You better put on a shirt or something nice.")
                elif mphone_chat_history_list[idx][4] == "4a":
                    if ep11_sage_love == 2:
                        mphone_chat_history_list[idx][2].append("Good boy. And here you go; now we're even. It's only fair that we both have pictures of each other from the party. mphone_emoji_heart")
                    else:
                        mphone_chat_history_list[idx][2].append("Good boy. And here you go; now we're even. It's only fair that we both have pictures of each other from the party. mphone_emoji_laugh")
                    mphone_chat_history_list[idx][2].append("chat_sage_pic2_ep11_thumb")
                    mgallery_add_photo("chat_sage_pic2_ep11_zoomed")
                    mphone_chat_history_list[idx][3].append(True)
                elif mphone_chat_history_list[idx][4] == "4b":
                    if ep11_sage_love == 2:
                        mphone_chat_history_list[idx][2].append("LOL. Keep it underneath a nice shirt, though. And here you go; now we're even. It's only fair that we both have pictures of each other from the party. mphone_emoji_heart")
                    else:
                        mphone_chat_history_list[idx][2].append("LOL. Keep it underneath a nice shirt, though. And here you go; now we're even. It's only fair that we both have pictures of each other from the party. mphone_emoji_laugh")
                    mphone_chat_history_list[idx][2].append("chat_sage_pic2_ep11_thumb")
                    mgallery_add_photo("chat_sage_pic2_ep11_zoomed")
                    mphone_chat_history_list[idx][3].append(True)
                elif mphone_chat_history_list[idx][4] == "5a":
                    mphone_chat_history_list[idx][2].append("Haha! No. Tonight, I'm wearing this.")
                    mphone_chat_history_list[idx][2].append("chat_sage_pic3_ep11_thumb")
                    mgallery_add_photo("chat_sage_pic3_ep11_zoomed")
                    mphone_chat_history_list[idx][3].append(True)
                    mphone_chat_history_list[idx][3].append(True)
                    if ep11_sage_love == 2:
                        mphone_chat_history_list[idx][2].append("See you tonight! Love you. mphone_emoji_heart")
                    else:
                        mphone_chat_history_list[idx][2].append("See you tonight!")
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
