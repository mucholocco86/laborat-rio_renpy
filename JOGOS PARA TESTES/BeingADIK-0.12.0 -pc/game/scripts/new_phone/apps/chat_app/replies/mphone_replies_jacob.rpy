init python:

    def mphone_chat_get_replies_jacob(idx):
        global mphone_replies
        global mphone_contact_list
        global mphone_next_state
        global mphone_contact_list
        global mphone_chat_history_list
        
        if len(mphone_chat_history_list[idx][4]) == 0:
            return
        
        if mphone_chat_history_list[idx][5] == 6:
            if  mphone_chat_history_list[idx][4] == "1":
                mphone_replies = ["Awesome! mphone_emoji_smile","",""]
                mphone_next_state = [" ","",""]
            else:
                
                mphone_replies = ["","",""]
                mphone_next_state = ["","",""]
                mphone_contact_list[idx][2] = False
        elif mphone_chat_history_list[idx][5] == 7:
            if  mphone_chat_history_list[idx][4] == "1":
                mphone_replies = ["Thanks! I'll check it out later. mphone_emoji_smile","",""]
                mphone_next_state = [" ","",""]
            else:
                
                mphone_replies = ["","",""]
                mphone_next_state = ["","",""]
                mphone_contact_list[idx][2] = False
        elif mphone_chat_history_list[idx][5] == 8:
            if  mphone_chat_history_list[idx][4] == "1":
                mphone_replies = ["Love it! mphone_emoji_smile","",""]
                mphone_next_state = [" ","",""]
            else:
                
                mphone_replies = ["","",""]
                mphone_next_state = ["","",""]
                mphone_contact_list[idx][2] = False
        elif mphone_chat_history_list[idx][5] == 9:
            if  mphone_chat_history_list[idx][4] == "1":
                mphone_replies = ["Amazing, as always! Thanks, you too! mphone_emoji_smile","",""]
                mphone_next_state = [" ","",""]
            else:
                
                mphone_replies = ["","",""]
                mphone_next_state = ["","",""]
                mphone_contact_list[idx][2] = False
        elif mphone_chat_history_list[idx][5] == 10:
            if  mphone_chat_history_list[idx][4] == "1":
                mphone_replies = ["Thanks.","",""]
                mphone_next_state = [" ","",""]
            else:
                
                mphone_replies = ["","",""]
                mphone_next_state = ["","",""]
                mphone_contact_list[idx][2] = False
        elif mphone_chat_history_list[idx][5] == 11:
            if  mphone_chat_history_list[idx][4] == "1":
                mphone_replies = ["Haha! Those are some talented elves. Thank you for the art! mphone_emoji_smile","",""]
                mphone_next_state = [" ","",""]
            else:
                
                mphone_replies = ["","",""]
                mphone_next_state = ["","",""]
                mphone_contact_list[idx][2] = False
        elif mphone_chat_history_list[idx][5] == 12:
            if  mphone_chat_history_list[idx][4] == "1":
                mphone_replies = ["Thanks! I don't know where you found the time to do this, but I appreciate it! mphone_emoji_smile","",""]
                mphone_next_state = [" ","",""]
            else:
                
                mphone_replies = ["","",""]
                mphone_next_state = ["","",""]
                mphone_contact_list[idx][2] = False
        elif mphone_chat_history_list[idx][5] == 13:
            if  mphone_chat_history_list[idx][4] == "1":
                mphone_replies = ["It looks awesome! Thanks, bro! mphone_emoji_smile","",""]
                mphone_next_state = [" ","",""]
            else:
                
                mphone_replies = ["","",""]
                mphone_next_state = ["","",""]
                mphone_contact_list[idx][2] = False
        return


    def mphone_chat_them_replies_jacob(idx):
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
            if mphone_chat_history_list[idx][5] == 6:
                if mphone_chat_history_list[idx][4] == "1":
                    mphone_chat_history_list[idx][2].append("Bro! Your art's ready; I dropped it off in your room. mphone_emoji_cool")
                elif mphone_chat_history_list[idx][4][0] == " ":
                    mphone_replies = ["","",""]
                    mphone_next_state = ["","",""]
                    mphone_contact_list[idx][2] = False
            elif mphone_chat_history_list[idx][5] == 7:
                if mphone_chat_history_list[idx][4] == "1":
                    mphone_chat_history_list[idx][2].append("I just remembered I drew some stuff for you this week. I dropped it off in your room. Tell me what you think.")
                elif mphone_chat_history_list[idx][4][0] == " ":
                    mphone_replies = ["","",""]
                    mphone_next_state = ["","",""]
                    mphone_contact_list[idx][2] = False
            elif mphone_chat_history_list[idx][5] == 8:
                if mphone_chat_history_list[idx][4] == "1":
                    mphone_chat_history_list[idx][2].append("Dropped off some art for you. mphone_emoji_smile")
                elif mphone_chat_history_list[idx][4][0] == " ":
                    mphone_replies = ["","",""]
                    mphone_next_state = ["","",""]
                    mphone_contact_list[idx][2] = False
            elif mphone_chat_history_list[idx][5] == 9:
                if mphone_chat_history_list[idx][4] == "1":
                    mphone_chat_history_list[idx][2].append("Your art is ready. Have a nice Thanksgiving! mphone_emoji_smile")
                elif mphone_chat_history_list[idx][4][0] == " ":
                    mphone_replies = ["","",""]
                    mphone_next_state = ["","",""]
                    mphone_contact_list[idx][2] = False
            elif mphone_chat_history_list[idx][5] == 10:
                if mphone_chat_history_list[idx][4] == "1":
                    mphone_chat_history_list[idx][2].append("The art you wanted is ready. Hope it will cheer you up. mphone_emoji_smile")
                elif mphone_chat_history_list[idx][4][0] == " ":
                    mphone_replies = ["","",""]
                    mphone_next_state = ["","",""]
                    mphone_contact_list[idx][2] = False
            elif mphone_chat_history_list[idx][5] == 11:
                if mphone_chat_history_list[idx][4] == "1":
                    mphone_chat_history_list[idx][2].append("Santa came early with a gift for you. It's funny that his elves draw the same style as me. mphone_emoji_cool")
                elif mphone_chat_history_list[idx][4][0] == " ":
                    mphone_replies = ["","",""]
                    mphone_next_state = ["","",""]
                    mphone_contact_list[idx][2] = False
            elif mphone_chat_history_list[idx][5] == 12:
                if mphone_chat_history_list[idx][4] == "1":
                    mphone_chat_history_list[idx][2].append("Dropped by with some art for you.")
                elif mphone_chat_history_list[idx][4][0] == " ":
                    mphone_replies = ["","",""]
                    mphone_next_state = ["","",""]
                    mphone_contact_list[idx][2] = False
            elif mphone_chat_history_list[idx][5] == 13:
                if mphone_chat_history_list[idx][4] == "1":
                    mphone_chat_history_list[idx][2].append("I forgot to mention that your art was ready. I put it in your room.")
                elif mphone_chat_history_list[idx][4][0] == " ":
                    mphone_replies = ["","",""]
                    mphone_next_state = ["","",""]
                    mphone_contact_list[idx][2] = False
            else:
                mphone_replies = ["","",""]
                mphone_next_state = ["","",""]
                mphone_contact_list[idx][2] = False
        elif mphone_chat_history_list[idx][4][0] == " ":
            mphone_replies = ["","",""]
            mphone_next_state = ["","",""]
            mphone_contact_list[idx][2] = False
        return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
