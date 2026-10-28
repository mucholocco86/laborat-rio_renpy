init python:

    def mphone_chat_get_replies_sally(idx):
        global mphone_replies
        global mphone_contact_list
        global mphone_next_state
        global mphone_contact_list
        global mphone_chat_history_list
        
        if len(mphone_chat_history_list[idx][4]) == 0:
            return
        
        if mphone_chat_history_list[idx][5] == 1:
            if  mphone_chat_history_list[idx][4] == "1":
                mphone_replies = ["For what?","Yeah, that works for me.",""]
                mphone_next_state = ["h2a","h2b",""]
            elif  mphone_chat_history_list[idx][4] == "2a":
                mphone_replies = ["Oh, yeah! That works for me.","Was that today? I thought it was tomorrow.",""]
                mphone_next_state = ["h2b","h2c",""]
            elif  mphone_chat_history_list[idx][4] == "2b":
                mphone_replies = ["That's fine. I can't think of anything else we'd need.","Bring a snack if you need it. I don't know how long it will take to write the report.",""]
                mphone_next_state = [" ","h3b",""]
            elif  mphone_chat_history_list[idx][4] == "2c":
                mphone_replies = ["Whatever. Tonight works for me. Drop by when you're free.","Maybe your note is wrong.",""]
                mphone_next_state = ["h4a","h4b",""]
            elif  mphone_chat_history_list[idx][4] == "4b":
                mphone_replies = ["Whatever. Tonight works for me. Drop by when you're free.","Are you sure? I found your handwriting at the lab to be unintelligible.",""]
                mphone_next_state = ["h4a","h5a",""]
            else:
                
                mphone_replies = ["","",""]
                mphone_next_state = ["","",""]
                mphone_contact_list[idx][2] = False
        elif mphone_chat_history_list[idx][5] == 2:
            if  mphone_chat_history_list[idx][4] == "1":
                mphone_replies = ["Science class isn't at the top of my priorities this week. I have Math and English for my finals.",""]
                mphone_next_state = ["h2a","",""]
            elif  mphone_chat_history_list[idx][4] == "2a":
                mphone_replies = ["You can? Then I'll drop by.","Did you pass those classes?",""]
                mphone_next_state = ["h3a","h3b",""]
            else:
                
                mphone_replies = ["","",""]
                mphone_next_state = ["","",""]
                mphone_contact_list[idx][2] = False
        return


    def mphone_chat_them_replies_sally(idx):
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
                    mphone_chat_history_list[idx][2].append("I'm showing up in a couple of hours. Is that ok?")
                elif mphone_chat_history_list[idx][4] == "2a":
                    mphone_chat_history_list[idx][2].append("What do you mean \"for what\"? Have you already forgotten that we're writing the lab report today?")
                elif mphone_chat_history_list[idx][4] == "2b":
                    mphone_chat_history_list[idx][2].append("I'll bring my laptop and notes. Do we need anything else?")
                elif mphone_chat_history_list[idx][4] == "2c":
                    mphone_chat_history_list[idx][2].append("No, we said today. I made a note of it. I can't be responsible if you forgot, you scatterbrain.")
                elif mphone_chat_history_list[idx][4] == "3b":
                    mphone_chat_history_list[idx][2].append("Noted.")
                elif mphone_chat_history_list[idx][4] == "4a":
                    mphone_chat_history_list[idx][2].append("Ok.")
                elif mphone_chat_history_list[idx][4] == "4b":
                    mphone_chat_history_list[idx][2].append("It's not. Maybe your brain is wrong!")
                elif mphone_chat_history_list[idx][4] == "5a":
                    mphone_chat_history_list[idx][2].append("I'm showing up tonight, and that's final!")
            elif mphone_chat_history_list[idx][5] == 2:
                if mphone_chat_history_list[idx][4] == "1":
                    mphone_chat_history_list[idx][2].append("Can we study together tomorrow? I'll be at the library all day.")
                elif mphone_chat_history_list[idx][4] == "2a":
                    mphone_chat_history_list[idx][2].append("I can help you with those.")
                elif mphone_chat_history_list[idx][4] == "3a":
                    mphone_chat_history_list[idx][2].append("mphone_emoji_smile")
                    task_list[2] = ""
                    updateTaskList()
                elif mphone_chat_history_list[idx][4] == "3b":
                    mphone_chat_history_list[idx][2].append("Of course, I passed those classes! mphone_emoji_angry")
                    mphone_chat_history_list[idx][3].append(True)
                    mphone_chat_history_list[idx][2].append("Let me know if you're not going to show up tomorrow.")
                    task_list[2] = ""
                    updateTaskList()
        
        elif mphone_chat_history_list[idx][4][0] == " ":
            mphone_replies = ["","",""]
            mphone_next_state = ["","",""]
            mphone_contact_list[idx][2] = False
        return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
