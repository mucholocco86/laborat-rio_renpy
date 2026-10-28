init python:

    def mphone_chat_get_replies_heather(idx):
        global mphone_replies
        global mphone_contact_list
        global mphone_next_state
        global mphone_contact_list
        global mphone_chat_history_list
        
        if len(mphone_chat_history_list[idx][4]) == 0:
            return
        
        if mphone_chat_history_list[idx][5] == 1:
            if  mphone_chat_history_list[idx][4] == "1":
                mphone_replies = ["No worries. You don't have to owe me one. Besides, I think most HOTs don't mind me.","I'm happy that I could help. I wasn't sure if telling you about it was a good idea or not.",""]
                mphone_next_state = ["h2a","h2b",""]
            elif  mphone_chat_history_list[idx][4] == "2a":
                mphone_replies = ["Did you bash me? All right, you can undo that damage.","If you say so; I appreciate it! mphone_emoji_smile",""]
                mphone_next_state = ["h3a","h3b",""]
            elif  mphone_chat_history_list[idx][4] == "2b":
                mphone_replies = ["You know him better than me. Thanks for not giving me any more problems with him.","If I were in your shoes, I wouldn't be as happy about being cheated on. I know you have some kind of a deal, but I could never do it.",""]
                mphone_next_state = ["h3c","h3d",""]
            elif  mphone_chat_history_list[idx][4] == "3a" or mphone_chat_history_list[idx][4] == "3b" or mphone_chat_history_list[idx][4] == "3c" or mphone_chat_history_list[idx][4] == "3d":
                mphone_replies = ["Other than that, how's everything with you?","Talk later, Heather. Thanks for the chat.",""]
                mphone_next_state = ["h4a","h4b",""]
            elif  mphone_chat_history_list[idx][4] == "4a":
                mphone_replies = ["No reason. I'd like to get to know you better.","I'm just making sure you're feeling all right.",""]
                mphone_next_state = ["h5a","h5b",""]
            elif  mphone_chat_history_list[idx][4] == "5a":
                mphone_replies = ["Yeah, I'm just trying to be friendly.","Well, I flirt a lot with girls. Flirting is harmless.",""]
                mphone_next_state = ["h5b","h6a",""]
            elif  mphone_chat_history_list[idx][4] == "6a":
                mphone_replies = ["Probably, and I'm pretty sure he'd punch me if you did that.","Hey, if you don't ask, you never know. I'm very bendy. mphone_emoji_cool",""]
                mphone_next_state = ["h7a","h7b",""]
            else:
                
                mphone_replies = ["","",""]
                mphone_next_state = ["","",""]
                mphone_contact_list[idx][2] = False
        return


    def mphone_chat_them_replies_heather(idx):
        global mphone_replies
        global mphone_contact_list
        global mphone_next_state
        global mphone_chat_history_list
        global mphone_contact_list
        global name
        global optional_task_list
        
        if len(mphone_chat_history_list[idx][4]) == 0:
            return
        
        if mphone_chat_history_list[idx][4][0] == "h":
            mphone_chat_history_list[idx][3].append(True)
            mphone_chat_history_list[idx][4] = mphone_chat_history_list[idx][4][1:]
            if mphone_chat_history_list[idx][5] == 1:
                if mphone_chat_history_list[idx][4] == "1":
                    mphone_chat_history_list[idx][2].append("[name], I've been meaning to thank you for telling me about what Tommy did. I have a foggy memory of saying something about owing you one, and I'll put in a good word with the HOTs for you.")
                elif mphone_chat_history_list[idx][4] == "2a":
                    mphone_chat_history_list[idx][2].append("Even so, I think it will mean a lot coming from me. I may have bashed you a bit in the past.")
                elif mphone_chat_history_list[idx][4] == "2b":
                    mphone_chat_history_list[idx][2].append("I didn't tell him that you told me. He was a bit pissed that someone went behind his back, but he'll get over it. He's too horny for his own good sometimes; I know he doesn't mean to hurt me.")
                elif mphone_chat_history_list[idx][4] == "3a":
                    mphone_chat_history_list[idx][2].append("Yeah, a bit. You came off like a creep to me at first, but I can see that you and Tommy are alike in some ways. I like that.")
                elif mphone_chat_history_list[idx][4] == "3b":
                    mphone_chat_history_list[idx][2].append("Sweet.")
                elif mphone_chat_history_list[idx][4] == "3c":
                    mphone_chat_history_list[idx][2].append("Well, it's only fair since you looked out for me.")
                elif mphone_chat_history_list[idx][4] == "3d":
                    mphone_chat_history_list[idx][2].append("It's just sex. It doesn't have to mean anything.")
                elif mphone_chat_history_list[idx][4] == "4b":
                    mphone_chat_history_list[idx][2].append("You too, [name].")
                    if "Answer Heather's text message" in optional_task_list:
                        optional_task_list.remove("Answer Heather's text message")
                elif mphone_chat_history_list[idx][4] == "4a":
                    mphone_chat_history_list[idx][2].append("It's good, I guess. Right now, I'm buried in textbooks, but who isn't? Why are you asking?")
                elif mphone_chat_history_list[idx][4] == "5a":
                    mphone_chat_history_list[idx][2].append("Ok. It feels weird hearing it from you, though. Sometimes I get the feeling you're trying to flirt with me. Maybe I'm paranoid.")
                elif mphone_chat_history_list[idx][4] == "5b":
                    mphone_chat_history_list[idx][2].append("Appreciate it. Talk another time, [name].")
                    if "Answer Heather's text message" in optional_task_list:
                        optional_task_list.remove("Answer Heather's text message")
                elif mphone_chat_history_list[idx][4] == "6a":
                    mphone_chat_history_list[idx][2].append("Aha, so I was right about that. I knew that you and Tommy were alike. But I'm pretty sure he would veto the crap outta you if I put you on my plus one list. mphone_emoji_tongue")
                elif mphone_chat_history_list[idx][4] == "7a":
                    mphone_chat_history_list[idx][2].append("That sounds like Tommy. Talk later, [name].")
                    if "Answer Heather's text message" in optional_task_list:
                        optional_task_list.remove("Answer Heather's text message")
                elif mphone_chat_history_list[idx][4] == "7b":
                    mphone_chat_history_list[idx][2].append("LOL! Whatever that means.")
                    mphone_chat_history_list[idx][3].append(True)
                    mphone_chat_history_list[idx][2].append("Talk later, [name].")
                    if "Answer Heather's text message" in optional_task_list:
                        optional_task_list.remove("Answer Heather's text message")
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
