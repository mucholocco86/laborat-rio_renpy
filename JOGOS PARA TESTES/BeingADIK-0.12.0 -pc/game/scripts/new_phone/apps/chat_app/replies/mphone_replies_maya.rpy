init python:

    def mphone_chat_get_replies_maya(idx):
        global mphone_replies
        global mphone_contact_list
        global mphone_next_state
        global mphone_contact_list
        global mphone_chat_history_list
        global ep7_solo_maya
        global ep7_hot_sage_phase
        global ep11_gift_list
        global branchMayaJosy
        global branchZoey
        
        if len(mphone_chat_history_list[idx][4]) == 0:
            return
        
        if mphone_chat_history_list[idx][5] == 1:
            if  mphone_chat_history_list[idx][4] == "1":
                mphone_replies = ["How's it going?","",""]
                mphone_next_state = ["h2a","",""]
            elif  mphone_chat_history_list[idx][4] == "2a":
                mphone_replies = ["I'm so excited!","Are you happy with your costume?",""]
                mphone_next_state = ["h3a","h3b",""]
            elif  mphone_chat_history_list[idx][4] == "3a":
                mphone_replies = ["I don't know how scary it will be, but we have scary movies playing in the home theater at least.","Well, I've seen some creepy costumes so far.",""]
                mphone_next_state = ["h4a","h4b",""]
            elif  mphone_chat_history_list[idx][4] == "3b":
                mphone_replies = ["I didn't realize you'd do something with your hair for this. I thought the costume was enough.","That's nice of her. I spent 10 seconds doing mine. But it doesn't matter since I'm wearing a helmet.",""]
                mphone_next_state = ["h4c","h4d",""]
            elif  mphone_chat_history_list[idx][4] == "4a":
                mphone_replies = ["We put them on to get the mood right. I doubt many will be watching.","I'm not sure people will be watching, though. It does feel like a waste of time.",""]
                mphone_next_state = ["h5a","h5b",""]
            elif  mphone_chat_history_list[idx][4] == "4b":
                mphone_replies = ["Yeah, I think most are.","",""]
                mphone_next_state = ["h5c","",""]
            elif  mphone_chat_history_list[idx][4] == "4c":
                mphone_replies = ["I can't wait to see how you look. mphone_emoji_kiss","I bet you both look amazing. mphone_emoji_smile",""]
                mphone_next_state = ["h5d","h5d",""]
            elif  mphone_chat_history_list[idx][4] == "4d":
                mphone_replies = ["I do spend a short time on makeup, yes.","You could spend less on it too. What's stopping you?",""]
                mphone_next_state = ["h5e","h5f",""]
            else:
                
                mphone_replies = ["","",""]
                mphone_next_state = ["","",""]
                mphone_contact_list[idx][2] = False
        elif mphone_chat_history_list[idx][5] == 2:
            if  mphone_chat_history_list[idx][4] == "1":
                mphone_replies = ["Oh? What kind of problem?","",""]
                mphone_next_state = ["h2a","",""]
            elif  mphone_chat_history_list[idx][4] == "2a":
                mphone_replies = ["That sounds like a wonderful problem to have! It would have sucked if there wasn't anything you wanted to watch. mphone_emoji_smile","You're on your own with that one. You know how bad I'm at movies.",""]
                mphone_next_state = ["h3a","h3b",""]
            elif  mphone_chat_history_list[idx][4] == "3a":
                mphone_replies = ["Comedy. You can't go wrong with laughter.","Action.","What the hell is a romcom?",""]
                mphone_next_state = ["h4a","h4b","h4c"]
            elif  mphone_chat_history_list[idx][4] == "4a" or mphone_chat_history_list[idx][4] == "4b":
                if branchZoey and branchMayaJosy:
                    mphone_replies = ["I'm glad I could help.","",""]
                    mphone_next_state = ["h5a","",""]
                else:
                    mphone_replies = ["I'm glad I could help.","So, when do you want to watch it with me?",""]
                    mphone_next_state = ["h5a","h5b",""]
            elif  mphone_chat_history_list[idx][4] == "4c":
                if branchZoey and branchMayaJosy:
                    mphone_replies = ["Sounds good! Go for it.","",""]
                    mphone_next_state = ["h5a","",""]
                else:
                    mphone_replies = ["Sounds good! Go for it.","Yeah, why not? I can sit through one of those. When do you wanna watch it?",""]
                    mphone_next_state = ["h5a","h5b",""]
            else:
                
                mphone_replies = ["","",""]
                mphone_next_state = ["","",""]
                mphone_contact_list[idx][2] = False
        return


    def mphone_chat_them_replies_maya(idx):
        global mphone_replies
        global mphone_contact_list
        global mphone_next_state
        global mphone_chat_history_list
        global mphone_contact_list
        global optional_task_list
        global task_list
        global RPmaya
        if len(mphone_chat_history_list[idx][4]) == 0:
            return
        
        if mphone_chat_history_list[idx][4][0] == "h":
            mphone_chat_history_list[idx][3].append(True)
            mphone_chat_history_list[idx][4] = mphone_chat_history_list[idx][4][1:]
            if mphone_chat_history_list[idx][5] == 1:
                if mphone_chat_history_list[idx][4] == "2a":
                    mphone_chat_history_list[idx][2].append("I just left my dorm. I'm heading to the HOTs now to meet up with everyone.")
                
                elif mphone_chat_history_list[idx][4] == "3a":
                    mphone_chat_history_list[idx][2].append("Same! I hope it will be a scary night! mphone_emoji_evil")
                elif mphone_chat_history_list[idx][4] == "3b":
                    mphone_chat_history_list[idx][2].append("Yes, it was worth the money. Josy spent a long time doing my hair earlier.")
                elif mphone_chat_history_list[idx][4] == "4a":
                    mphone_chat_history_list[idx][2].append("OMG! Really?")
                elif mphone_chat_history_list[idx][4] == "4b":
                    mphone_chat_history_list[idx][2].append("That sounds awesome! Everyone is taking Halloween seriously, then?")
                elif mphone_chat_history_list[idx][4] == "4c":
                    mphone_chat_history_list[idx][2].append("We both did our hair! It's a special night, after all. mphone_emoji_smile")
                elif mphone_chat_history_list[idx][4] == "4d":
                    mphone_chat_history_list[idx][2].append("I envy guys. You have it easy when it comes to so much. Like makeup and hair.")
                elif mphone_chat_history_list[idx][4] == "5a":
                    mphone_chat_history_list[idx][2].append("I'm gonna have a look, at least.")
                    mphone_chat_history_list[idx][3].append(True)
                    mphone_chat_history_list[idx][2].append("I'm almost at the HOTs now; I'll see you soon! mphone_emoji_kiss")
                    optional_task_list[0] = ""
                    RPmaya += 1
                elif mphone_chat_history_list[idx][4] == "5b":
                    mphone_chat_history_list[idx][2].append("I guess it depends on how fun the party is. mphone_emoji_tongue")
                    mphone_chat_history_list[idx][3].append(True)
                    mphone_chat_history_list[idx][2].append("I'm almost at the HOTs now; I'll see you soon! mphone_emoji_kiss")
                    optional_task_list[0] = ""
                    RPmaya += 1
                elif mphone_chat_history_list[idx][4] == "5c":
                    mphone_chat_history_list[idx][2].append("Awesome!")
                    mphone_chat_history_list[idx][3].append(True)
                    mphone_chat_history_list[idx][2].append("I'm almost at the HOTs now; I'll see you soon! mphone_emoji_kiss")
                    optional_task_list[0] = ""
                    RPmaya += 1
                elif mphone_chat_history_list[idx][4] == "5d":
                    mphone_chat_history_list[idx][2].append("mphone_emoji_smile")
                    mphone_chat_history_list[idx][3].append(True)
                    mphone_chat_history_list[idx][2].append("I'm almost at the HOTs now; I'll see you soon! mphone_emoji_kiss")
                    optional_task_list[0] = ""
                    RPmaya += 1
                elif mphone_chat_history_list[idx][4] == "5e":
                    mphone_chat_history_list[idx][2].append("Haha! Idiot. mphone_emoji_laugh")
                    mphone_chat_history_list[idx][3].append(True)
                    mphone_chat_history_list[idx][2].append("I'm almost at the HOTs now; I'll see you soon! mphone_emoji_kiss")
                    optional_task_list[0] = ""
                    RPmaya += 1
                elif mphone_chat_history_list[idx][4] == "5f":
                    mphone_chat_history_list[idx][2].append("I wish. I have to maintain some kind of standard, or I'd scare you away. mphone_emoji_tongue")
                    mphone_chat_history_list[idx][3].append(True)
                    mphone_chat_history_list[idx][2].append("I'm almost at the HOTs now; I'll see you soon! mphone_emoji_kiss")
                    optional_task_list[0] = ""
                    RPmaya += 1
                elif mphone_chat_history_list[idx][4] == " ":
                    mphone_replies = ["","",""]
                    mphone_next_state = ["","",""]
                    mphone_contact_list[idx][2] = False
            elif mphone_chat_history_list[idx][5] == 2:
                if mphone_chat_history_list[idx][4] == "1":
                    mphone_chat_history_list[idx][2].append("Thank you again for the gift. Although with the gift you've given me, I have a problem.")
                elif mphone_chat_history_list[idx][4] == "2a":
                    mphone_chat_history_list[idx][2].append("I can't decide what movie I want to watch! mphone_emoji_cry mphone_emoji_laugh")
                elif mphone_chat_history_list[idx][4] == "3a":
                    mphone_chat_history_list[idx][2].append("Yeah, you're right. Can you help me out? Romcom or a comedy?")
                elif mphone_chat_history_list[idx][4] == "3b":
                    mphone_chat_history_list[idx][2].append("Doh! I'll figure something out. Anyway, thanks again! mphone_emoji_kiss")
                elif mphone_chat_history_list[idx][4] == "4a":
                    mphone_chat_history_list[idx][2].append("So true. Although there aren't many comedies that make me laugh out loud. But comedy it is!")
                elif mphone_chat_history_list[idx][4] == "4b":
                    mphone_chat_history_list[idx][2].append("Haha! Action? Hm... I don't know... Well, there is one action-comedy I want to watch.")
                    mphone_chat_history_list[idx][3].append(True)
                    mphone_chat_history_list[idx][2].append("Ok! I have decided. Action-comedy it is!")
                elif mphone_chat_history_list[idx][4] == "4c":
                    mphone_chat_history_list[idx][2].append("An abbreviation of romantic comedy. Picture a love story that makes you laugh.")
                elif mphone_chat_history_list[idx][4] == "5a":
                    mphone_chat_history_list[idx][2].append("mphone_emoji_heart")
                elif mphone_chat_history_list[idx][4] == "5b":
                    mphone_chat_history_list[idx][2].append("If you're around during winter break, we should make time for it. Thanks for the help! mphone_emoji_heart")
        
        elif mphone_chat_history_list[idx][4] == " ":
            mphone_replies = ["","",""]
            mphone_next_state = ["","",""]
            mphone_contact_list[idx][2] = False
        return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
