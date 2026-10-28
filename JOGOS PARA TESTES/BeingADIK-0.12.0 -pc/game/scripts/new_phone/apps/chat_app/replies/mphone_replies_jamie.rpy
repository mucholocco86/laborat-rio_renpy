init python:

    def mphone_chat_get_replies_jamie(idx):
        global mphone_replies
        global mphone_contact_list
        global mphone_next_state
        global mphone_contact_list
        global mphone_chat_history_list
        
        if len(mphone_chat_history_list[idx][4]) == 0:
            return
        
        if mphone_chat_history_list[idx][5] == 1:
            if  mphone_chat_history_list[idx][4] == "1":
                mphone_replies = ["Are you ok?","",""]
                mphone_next_state = ["h2a","",""]
            elif  mphone_chat_history_list[idx][4] == "2a":
                mphone_replies = ["Did you consider doing that?","But did it work? Are you drunk?",""]
                mphone_next_state = ["h3a","h3b",""]
            elif  mphone_chat_history_list[idx][4] == "3a":
                mphone_replies = ["Why did she ask you that?","Did the fanny bullets work? Are you drunk?",""]
                mphone_next_state = ["h4a","h3b",""]
            elif  mphone_chat_history_list[idx][4] == "3b":
                mphone_replies = ["Jacob and I went to the HOTs. Come here if you feel like it.","Cool. Have fun! mphone_emoji_smile",""]
                mphone_next_state = ["h4b","h4c",""]
            elif  mphone_chat_history_list[idx][4] == "4a":
                mphone_replies = ["That's one hell of a story.","You made the right call, bro.",""]
                mphone_next_state = ["h5a","h5b",""]
            elif  mphone_chat_history_list[idx][4] == "4b" or mphone_chat_history_list[idx][4] == "5a" or mphone_chat_history_list[idx][4] == "5b":
                mphone_replies = ["Cool. Have fun! mphone_emoji_smile","",""]
                mphone_next_state = ["h4c","",""]
            else:
                
                mphone_replies = ["","",""]
                mphone_next_state = ["","",""]
                mphone_contact_list[idx][2] = False
        elif mphone_chat_history_list[idx][5] == 2:
            if  mphone_chat_history_list[idx][4] == "1":
                mphone_replies = ["Thanks for the reminder! mphone_emoji_smile","",""]
                mphone_next_state = [" ","",""]
            else:
                
                mphone_replies = ["","",""]
                mphone_next_state = ["","",""]
                mphone_contact_list[idx][2] = False
        return


    def mphone_chat_them_replies_jamie(idx):
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
                if mphone_chat_history_list[idx][4] == "2a":
                    mphone_chat_history_list[idx][2].append("My asshole is a burn victim! This is just what I imagine bleaching your anus feels like.")
                elif mphone_chat_history_list[idx][4] == "3a":
                    mphone_chat_history_list[idx][2].append("Not really, but one time Dany asked me to do it.")
                elif mphone_chat_history_list[idx][4] == "3b":
                    mphone_chat_history_list[idx][2].append("No, I'm not drunk. Derek took the bottle and continued by himself. I'm hanging out with Leon; we're heading downtown hoping to get lucky.")
                elif mphone_chat_history_list[idx][4] == "4a":
                    mphone_chat_history_list[idx][2].append("It's a long story... The short version is that I asked her to bleach her asshole. It was kind of a turn-off... You know, hairy and brown. I didn't wanna do anal when it looked like that, so I asked her to bleach and wax it. She got mad and, after a rant on double standards, told me she'd do it if I did it too. I was almost on board, but then I asked if anal was in on the deal, and there's just no way I will take a dildo to my asshole to make things even.")
                elif mphone_chat_history_list[idx][4] == "4b":
                    mphone_chat_history_list[idx][2].append("That's where you went? I'm not so sure about it... I think we're gonna try to get into some bars or call it a night.")
                elif mphone_chat_history_list[idx][4] == "4c":
                    mphone_chat_history_list[idx][2].append("You too! mphone_emoji_cool")
                elif mphone_chat_history_list[idx][4] == "5a":
                    mphone_chat_history_list[idx][2].append("Sadly, it's just one of many like it. I'll tell you some more another time. I need to go; we're about to try our luck getting into a bar.")
                elif mphone_chat_history_list[idx][4] == "5b":
                    mphone_chat_history_list[idx][2].append("Yeah, sometimes I wonder, though... I need to go; we're about to try our luck getting into a bar.")
                elif mphone_chat_history_list[idx][4][0] == " ":
                    mphone_replies = ["","",""]
                    mphone_next_state = ["","",""]
                    mphone_contact_list[idx][2] = False
            elif mphone_chat_history_list[idx][5] == 2:
                if mphone_chat_history_list[idx][4] == "1":
                    mphone_chat_history_list[idx][2].append("Your flowers could use a splash of water. I didn't do it for you this time.")
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
