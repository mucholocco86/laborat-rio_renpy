init python:

    def mphone_chat_get_replies_quinn(idx):
        global mphone_replies
        global mphone_contact_list
        global mphone_next_state
        global mphone_contact_list
        global mphone_chat_history_list
        
        if len(mphone_chat_history_list[idx][4]) == 0:
            return
        
        if mphone_chat_history_list[idx][5] == 1:
            if  mphone_chat_history_list[idx][4] == "1":
                mphone_replies = ["Did you just return? Did it take all night?","",""]
                mphone_next_state = ["h2a","",""]
            elif  mphone_chat_history_list[idx][4] == "2a":
                mphone_replies = ["Are you safe?","I'm happy whatever you did went well. mphone_emoji_smile",""]
                mphone_next_state = ["h3a","h3b",""]
            elif  mphone_chat_history_list[idx][4] == "3a" or mphone_chat_history_list[idx][4] == "3b":
                mphone_replies = ["Rest up. mphone_emoji_kiss","",""]
                mphone_next_state = [" ","",""]
            else:
                
                mphone_replies = ["","",""]
                mphone_next_state = ["","",""]
                mphone_contact_list[idx][2] = False
        elif mphone_chat_history_list[idx][5] == 2:
            if  mphone_chat_history_list[idx][4] == "1":
                mphone_replies = ["Wellness check. How are you?","",""]
                mphone_next_state = ["h2a","",""]
            elif  mphone_chat_history_list[idx][4] == "2a":
                mphone_replies = ["Humor is intact. The patient seems stable.","I know. But I needed to open with something that didn't sound so clingy.",""]
                mphone_next_state = ["h3a","h3b",""]
            elif  mphone_chat_history_list[idx][4] == "3a" or mphone_chat_history_list[idx][4] == "3b":
                mphone_replies = ["Lay low? For how long will you have to do that? When can I see you again?","",""]
                mphone_next_state = ["h4a","",""]
            elif  mphone_chat_history_list[idx][4] == "4a":
                mphone_replies = ["I have my finals on Friday and will head home sometime during the weekend. I hope you can squeeze me in.","",""]
                mphone_next_state = ["h5a","",""]
            elif  mphone_chat_history_list[idx][4] == "5a":
                mphone_replies = ["Can't wait. mphone_emoji_eggplant","",""]
                mphone_next_state = [" ","",""]
            else:
                
                mphone_replies = ["","",""]
                mphone_next_state = ["","",""]
                mphone_contact_list[idx][2] = False
        return


    def mphone_chat_them_replies_quinn(idx):
        global mphone_replies
        global mphone_contact_list
        global mphone_next_state
        global mphone_chat_history_list
        global mphone_contact_list
        global ep7_solo_quinn
        global optional_task_list
        global task_list
        if len(mphone_chat_history_list[idx][4]) == 0:
            return
        
        if mphone_chat_history_list[idx][4][0] == "h":
            mphone_chat_history_list[idx][3].append(True)
            mphone_chat_history_list[idx][4] = mphone_chat_history_list[idx][4][1:]
            if mphone_chat_history_list[idx][5] == 1:
                if mphone_chat_history_list[idx][4] == "1":
                    mphone_chat_history_list[idx][2].append("I'm back home. It went well.")
                elif mphone_chat_history_list[idx][4] == "2a":
                    mphone_chat_history_list[idx][2].append("Pretty much. I had to make a couple of trips back and forth, but now I can rest. I'm gonna crash for a while.")
                elif mphone_chat_history_list[idx][4] == "3a":
                    mphone_chat_history_list[idx][2].append("It's too early to tell. But for the moment, I'm as safe as I can be. Don't worry about me, ok? mphone_emoji_kiss")
                    task_list[5] = ""
                    updateTaskList()
                elif mphone_chat_history_list[idx][4] == "3b":
                    mphone_chat_history_list[idx][2].append("You don't have to worry about me. If you need me, I'll be in bed. mphone_emoji_kiss")
                    task_list[5] = ""
                    updateTaskList()
                elif mphone_chat_history_list[idx][4][0] == " ":
                    mphone_replies = ["","",""]
                    mphone_next_state = ["","",""]
                    mphone_contact_list[idx][2] = False
            elif mphone_chat_history_list[idx][5] == 2:
                if mphone_chat_history_list[idx][4] == "2a":
                    mphone_chat_history_list[idx][2].append("LOL. Wellness check? I'm not 80 years old.")
                elif mphone_chat_history_list[idx][4] == "3a" or mphone_chat_history_list[idx][4] == "3b":
                    mphone_chat_history_list[idx][2].append("I'm fine. I'm still monitoring the situation on my end and trying to lay low.")
                elif mphone_chat_history_list[idx][4] == "4a":
                    mphone_chat_history_list[idx][2].append("For a while longer. I'll tell you more in person. I'm busy right now, but I'll see you soon enough.")
                elif mphone_chat_history_list[idx][4] == "5a":
                    mphone_chat_history_list[idx][2].append("Trust me. I'll find some time to squeeze you in. All of you will be squeezed in. mphone_emoji_tongue")
                    task_list[4] = ""
                    updateTaskList()
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
