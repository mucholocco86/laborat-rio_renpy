init python:

    def mphone_chat_get_replies_dad(idx):
        global mphone_replies
        global mphone_contact_list
        global mphone_next_state
        global mphone_contact_list
        global mphone_chat_history_list
        
        if len(mphone_chat_history_list[idx][4]) == 0:
            return
        
        if mphone_chat_history_list[idx][5] == 2:
            if  mphone_chat_history_list[idx][4] == "1":
                mphone_replies = ["Sorry. I'm fine, Dad. mphone_emoji_smile I should have called you earlier this week, but I've been busy planning our Halloween party. It's happening tonight.","Yeah, everything's fine, Dad. We have a big party tonight, so I've been busy. Can I call you tomorrow or something?",""]
                mphone_next_state = ["h2a","h2b",""]
            elif  mphone_chat_history_list[idx][4] == "2a":
                mphone_replies = ["I can tell you what it isn't - a girl ghost. Thanks for that, by the way. The guys have been very nice by reminding me of it.","I'm dressed as a Spartan, I think. The costume was named Greek Warrior.",""]
                mphone_next_state = ["h3a","h3b",""]
            elif  mphone_chat_history_list[idx][4] == "2b" or mphone_chat_history_list[idx][4] == "3a" or mphone_chat_history_list[idx][4] == "3b":
                mphone_replies = ["I love you too, Dad.","Dad... That kiss emoji makes your text look weird as hell.",""]
                mphone_next_state = ["h3c","h3d",""]
            else:
                
                mphone_replies = ["","",""]
                mphone_next_state = ["","",""]
                mphone_contact_list[idx][2] = False
        elif mphone_chat_history_list[idx][5] == 3:
            if  mphone_chat_history_list[idx][4] == "1":
                mphone_replies = ["Thanks! I'll do my best.","Thanks, but who's to say that I will pass the tests?",""]
                mphone_next_state = ["h2a","h2b",""]
            elif  mphone_chat_history_list[idx][4] == "2a" or mphone_chat_history_list[idx][4] == "2b":
                mphone_replies = ["Winter break starts after my tests on Friday. I think I'll stay here until Sunday, then I'll come home. So, either Sunday or Monday. I'll let you know.","",""]
                mphone_next_state = ["h3a","",""]
            elif  mphone_chat_history_list[idx][4] == "3a":
                mphone_replies = ["You too!","",""]
                mphone_next_state = [" ","",""]
            else:
                
                mphone_replies = ["","",""]
                mphone_next_state = ["","",""]
                mphone_contact_list[idx][2] = False
        elif mphone_chat_history_list[idx][5] == 4:
            if  mphone_chat_history_list[idx][4] == "1":
                mphone_replies = ["Happy New Year! I survived the night. How was your night?","",""]
                mphone_next_state = ["h2a","",""]
            elif  mphone_chat_history_list[idx][4] == "2a":
                mphone_replies = ["That's nice. I'm happy you didn't end up spending it at home by yourself.","",""]
                mphone_next_state = ["h3a","",""]
            else:
                
                mphone_replies = ["","",""]
                mphone_next_state = ["","",""]
                mphone_contact_list[idx][2] = False
        return


    def mphone_chat_them_replies_dad(idx):
        global mphone_replies
        global mphone_contact_list
        global mphone_next_state
        global mphone_chat_history_list
        global mphone_contact_list
        global totalDikChoices
        global tmpdik
        global totalChickChoices
        if len(mphone_chat_history_list[idx][4]) == 0:
            return
        
        if mphone_chat_history_list[idx][4][0] == "h":
            mphone_chat_history_list[idx][3].append(True)
            mphone_chat_history_list[idx][4] = mphone_chat_history_list[idx][4][1:]
            if mphone_chat_history_list[idx][5] == 2:
                if mphone_chat_history_list[idx][4] == "1":
                    mphone_chat_history_list[idx][2].append("I wanted to check in on you. Is everything all right?")
                elif mphone_chat_history_list[idx][4] == "2a":
                    mphone_chat_history_list[idx][2].append("Halloween, you say. What's your costume?")
                elif mphone_chat_history_list[idx][4] == "2b":
                    mphone_chat_history_list[idx][2].append("Of course. I just wanted to make sure everything was all right. Have a fun party, son. I love you. mphone_emoji_kiss")
                elif mphone_chat_history_list[idx][4] == "3a":
                    mphone_chat_history_list[idx][2].append("I'm sorry about that. It was a fond memory resurfacing, and I should maybe have thought a bit more before mentioning it in front of your friends. Have a fun night! I love you. mphone_emoji_kiss")
                elif mphone_chat_history_list[idx][4] == "3b":
                    mphone_chat_history_list[idx][2].append("Off to battle with you, then. Have a fun night, son. I love you. mphone_emoji_kiss")
                elif mphone_chat_history_list[idx][4] == "3c":
                    totalChickChoices += 1
                    tmpdik -= 1
                    mphone_chat_history_list[idx][3].pop()
                elif mphone_chat_history_list[idx][4] == "3d":
                    totalDikChoices += 1
                    tmpdik += 1
                    mphone_chat_history_list[idx][3].pop()
                elif mphone_chat_history_list[idx][4][0] == " ":
                    mphone_replies = ["","",""]
                    mphone_next_state = ["","",""]
                    mphone_contact_list[idx][2] = False
            elif mphone_chat_history_list[idx][5] == 3:
                if mphone_chat_history_list[idx][4] == "1":
                    mphone_chat_history_list[idx][2].append("Good luck with your tests this week. I don't know how you do it; I would fail every single test. I'm proud of you.")
                elif mphone_chat_history_list[idx][4] == "2a":
                    mphone_chat_history_list[idx][2].append("Did you decide which date you're coming home for Christmas yet?")
                elif mphone_chat_history_list[idx][4] == "2b":
                    mphone_chat_history_list[idx][2].append("With all that studying you do, I'm sure you will pass them. If not, then I would blame the teachers.")
                    mphone_chat_history_list[idx][3].append(True)
                    mphone_chat_history_list[idx][2].append("Did you decide which date you're coming home for Christmas yet?")
                elif mphone_chat_history_list[idx][4] == "3a":
                    mphone_chat_history_list[idx][2].append("I can't wait to have you. Have a good week!")
                elif mphone_chat_history_list[idx][4][0] == " ":
                    mphone_replies = ["","",""]
                    mphone_next_state = ["","",""]
                    mphone_contact_list[idx][2] = False
            elif mphone_chat_history_list[idx][5] == 4:
                if mphone_chat_history_list[idx][4] == "1":
                    mphone_chat_history_list[idx][2].append("Happy New Year! I hope your big party went well. Love you.")
                elif mphone_chat_history_list[idx][4] == "2a":
                    mphone_chat_history_list[idx][2].append("Happy to hear that. We had a nice dinner together. Almost everyone from work showed up for it. I stayed after dinner for drinks and celebrated midnight with Paul and Clark.")
                elif mphone_chat_history_list[idx][4] == "3a":
                    mphone_chat_history_list[idx][2].append("Your old man still has a couple of parties worth per year in him. Haha!")
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
