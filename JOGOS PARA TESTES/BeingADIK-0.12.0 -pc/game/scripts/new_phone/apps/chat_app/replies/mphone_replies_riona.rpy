init python:

    def mphone_chat_get_replies_riona(idx):
        global mphone_replies
        global mphone_contact_list
        global mphone_next_state
        global mphone_contact_list
        global mphone_chat_history_list
        global ep10_riona_date
        
        if len(mphone_chat_history_list[idx][4]) == 0:
            return
        
        if mphone_chat_history_list[idx][5] == 1:
            if mphone_chat_history_list[idx][4] == "1":
                if ep10_riona_date:
                    mphone_replies = ["I heard you were sick. I'm starting to miss you. Let me know if I can do something for you. I hope you'll be back soon so we can go to the arcade again!","I hope you get well soon. I assure you that Camila keeps your room clean and not overly decorated. I miss you.",""]
                else:
                    mphone_replies = ["I heard you were sick. I hope you get better soon. Let me know if I can do something for you, ok?","It must be one nasty flu. Get well soon! Drink lots of fluids and rest, ok?",""]
                mphone_next_state = ["h2a","h2b",""]
            else:
                
                mphone_replies = ["","",""]
                mphone_next_state = ["","",""]
                mphone_contact_list[idx][2] = False
        elif mphone_chat_history_list[idx][5] == 2:
            if mphone_chat_history_list[idx][4] == "1":
                mphone_replies = ["Quinn told me what happened to you. Please be safe. You can talk to me. Day or night, I'm here.","",""]
                mphone_next_state = ["h2a","",""]
            else:
                
                mphone_replies = ["","",""]
                mphone_next_state = ["","",""]
                mphone_contact_list[idx][2] = False
        return


    def mphone_chat_them_replies_riona(idx):
        global mphone_replies
        global mphone_contact_list
        global mphone_next_state
        global mphone_chat_history_list
        global mphone_contact_list
        global name
        global ep7_riona_payback
        global ep7_riona_help
        global ep11_rio_text
        global task_list
        global optional_task_list
        if len(mphone_chat_history_list[idx][4]) == 0:
            return
        
        if mphone_chat_history_list[idx][4][0] == "h":
            mphone_chat_history_list[idx][3].append(True)
            mphone_chat_history_list[idx][4] = mphone_chat_history_list[idx][4][1:]
            if mphone_chat_history_list[idx][5] == 1:
                if mphone_chat_history_list[idx][4] == "2a":
                    if ep10_riona_date:
                        ep11_rio_text = 1
                    else:
                        ep11_rio_text = 3
                    optional_task_list[5] = ""
                    updateTaskList()
                    mphone_chat_history_list[idx][3].pop()
                elif mphone_chat_history_list[idx][4] == "2b":
                    if ep10_riona_date:
                        ep11_rio_text = 2
                    else:
                        ep11_rio_text = 4
                    optional_task_list[5] = ""
                    updateTaskList()
                    mphone_chat_history_list[idx][3].pop()
            elif mphone_chat_history_list[idx][5] == 2:
                if mphone_chat_history_list[idx][4] == "2a":
                    ep11_rio_text = 5
                    optional_task_list[4] = ""
                    updateTaskList()
                    mphone_chat_history_list[idx][3].pop()
        elif mphone_chat_history_list[idx][4][0] == " ":
            mphone_replies = ["","",""]
            mphone_next_state = ["","",""]
            mphone_contact_list[idx][2] = False
        return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
