init python:

    def mphone_chat_get_replies_tommy(idx):
        global mphone_replies
        global mphone_contact_list
        global mphone_next_state
        global mphone_contact_list
        global mphone_chat_history_list
        global ep7_pinkrose
        
        if len(mphone_chat_history_list[idx][4]) == 0:
            return
        
        if mphone_chat_history_list[idx][5] == 1:
            if  mphone_chat_history_list[idx][4] == "1":
                if ep7_pinkrose:
                    mphone_replies = ["Why? I thought we agreed on the work schedule.","Sure, if you take my shift next week.",""]
                else:
                    mphone_replies = ["Why? I thought we agreed on the work schedule.","Sure, but only if you take my shift at the elderly home next week.",""]
                mphone_next_state = ["h2a","h2b",""]
            elif  mphone_chat_history_list[idx][4] == "2a":
                mphone_replies = ["Sure, but only if you take my shift at the elderly home next week.","Sure, I'll cover for you.","No, I don't think so."]
                mphone_next_state = ["h2b","h3a","h3b"]
            elif  mphone_chat_history_list[idx][4] == "2b":
                if ep7_pinkrose:
                    mphone_replies = ["That's what you're asking me to do right now. I think that's fair.","It's a give and take, Tommy.",""]
                else:
                    mphone_replies = ["I think it's a fair trade.","It's a give and take, Tommy.",""]
                mphone_next_state = ["h4a","h4b",""]
            elif  mphone_chat_history_list[idx][4] == "3b":
                mphone_replies = ["Aha, trying to guilt-trip me now, are you? It didn't work. But I'll cover for you; you did say \"please\".","All right. I'm doing this for them. And you'll cover for me next week.",""]
                mphone_next_state = ["h4c","h4d",""]
            else:
                
                mphone_replies = ["","",""]
                mphone_next_state = ["","",""]
                mphone_contact_list[idx][2] = False
        return


    def mphone_chat_them_replies_tommy(idx):
        global mphone_replies
        global mphone_contact_list
        global mphone_next_state
        global mphone_chat_history_list
        global mphone_contact_list
        global task_list
        
        if len(mphone_chat_history_list[idx][4]) == 0:
            return
        
        if mphone_chat_history_list[idx][4][0] == "h":
            mphone_chat_history_list[idx][3].append(True)
            mphone_chat_history_list[idx][4] = mphone_chat_history_list[idx][4][1:]
            if mphone_chat_history_list[idx][5] == 1:
                if mphone_chat_history_list[idx][4] == "1":
                    mphone_chat_history_list[idx][2].append("I'm too lazy to check if you're in your room or not. Pink Rose. Tomorrow. Can you cover for me?")
                elif mphone_chat_history_list[idx][4] == "2a":
                    mphone_chat_history_list[idx][2].append("Something came up, and I can't cancel. Are you covering for me or what?")
                elif mphone_chat_history_list[idx][4] == "2b":
                    if ep7_pinkrose:
                        mphone_chat_history_list[idx][2].append("What? I'm gonna have to work two times next week?")
                    else:
                        mphone_chat_history_list[idx][2].append("Come on, that's retarded. I'm not working there again.")
                elif mphone_chat_history_list[idx][4] == "3a":
                    mphone_chat_history_list[idx][2].append("Awesome! Thanks, brother. mphone_emoji_smile")
                    task_list[2] = ""
                    updateTaskList()
                elif mphone_chat_history_list[idx][4] == "3b":
                    mphone_chat_history_list[idx][2].append("Are you gonna make me beg? Please! Dude, I can't cancel. Do you want the others to have to pull my weight?")
                elif mphone_chat_history_list[idx][4] == "4a":
                    mphone_chat_history_list[idx][2].append("Fuck it. Ok, deal. Thanks.")
                    task_list[2] = ""
                    updateTaskList()
                elif mphone_chat_history_list[idx][4] == "4b":
                    mphone_chat_history_list[idx][2].append("Fuck it, I don't have time to argue. It's a deal, this time. Thanks.")
                    task_list[2] = ""
                    updateTaskList()
                elif mphone_chat_history_list[idx][4] == "4c":
                    mphone_chat_history_list[idx][2].append("Fuck you. And thanks.")
                    task_list[2] = ""
                    updateTaskList()
                elif mphone_chat_history_list[idx][4] == "4d":
                    mphone_chat_history_list[idx][2].append("Deal. Thanks.")
                    task_list[2] = ""
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
