init python:

    def mphone_chat_get_replies_rusty(idx):
        global mphone_replies
        global mphone_contact_list
        global mphone_next_state
        global mphone_contact_list
        global mphone_chat_history_list
        
        if len(mphone_chat_history_list[idx][4]) == 0:
            return
        
        if mphone_chat_history_list[idx][5] == 1:
            if  mphone_chat_history_list[idx][4] == "1":
                mphone_replies = ["How is that a middle-ground solution?","Are you kidding me? That's the worst plan I've heard. Why would you agree to that?","Ok. It's not what I had hoped for, but let's make the best out of it."]
                mphone_next_state = ["h2a","h2b","h2c"]
            elif  mphone_chat_history_list[idx][4] == "2a" or mphone_chat_history_list[idx][4] == "2b" or mphone_chat_history_list[idx][4] == "2c":
                mphone_replies = ["What can I help out with?","",""]
                mphone_next_state = ["h3a"," ",""]
            elif  mphone_chat_history_list[idx][4] == "3a":
                mphone_replies = ["Cool. I've got it. What's the venue and budget? Can you tell me any other details now?","",""]
                mphone_next_state = ["h4a","",""]
            elif  mphone_chat_history_list[idx][4] == "4a":
                mphone_replies = ["It sounds like a start. I'll let you know when I have some free time to help plan it.","",""]
                mphone_next_state = ["h5a","",""]
            else:
                
                mphone_replies = ["","",""]
                mphone_next_state = ["","",""]
                mphone_contact_list[idx][2] = False
        return


    def mphone_chat_them_replies_rusty(idx):
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
                    mphone_chat_history_list[idx][2].append("I don't know if you've heard yet, but we had a meeting between frats and the HOTs about the New Year's Eve party. To cut a long story short, we have agreed to throw a big party on campus with the HOTs and the tri-alphas. I wish there were another solution to this, but we had to find a middle ground, and this was it.")
                elif mphone_chat_history_list[idx][4] == "2a" or mphone_chat_history_list[idx][4] == "2b":
                    mphone_chat_history_list[idx][2].append("We couldn't agree on whose turn it was to party with the HOTs, and there were some hurt feelings from the jocks with how we handled the Christmas party. By having a party together, everyone is happy - or miserable, if that's how you want to look at it. Also, since it's winter break and people are busy, we'll need all the help we can get to plan and arrange the party. I hope you understand it's not what I wanted either, but how it had to be.")
                elif mphone_chat_history_list[idx][4] == "2c":
                    mphone_chat_history_list[idx][2].append("Oh? I thought you'd protest the idea. Thanks for making it easier for me. I hope you understand it's not what I wanted either, but that it had to be this way.")
                elif mphone_chat_history_list[idx][4] == "3a":
                    mphone_chat_history_list[idx][2].append("We could use your help with the logistics and planning, as always. Whatever time you can spare is appreciated.")
                elif mphone_chat_history_list[idx][4] == "4a":
                    mphone_chat_history_list[idx][2].append("The HOTs are looking into venues. With a little luck, it will be held somewhere on campus. For the budget, we'll calculate an entry fee based on the invite list and throw in whatever we can spare if needed. There was talk about splitting the dining room into two; one for us and one for the jocks. But nothing is final yet.")
                elif mphone_chat_history_list[idx][4] == "5a":
                    mphone_chat_history_list[idx][2].append("Thanks!")
                    task_list[3] = ""
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
