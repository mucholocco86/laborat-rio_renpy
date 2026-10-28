init python:

    def mphone_chat_get_replies_nick(idx):
        global mphone_replies
        global mphone_contact_list
        global mphone_next_state
        global mphone_contact_list
        global mphone_chat_history_list
        
        if len(mphone_chat_history_list[idx][4]) == 0:
            return
        
        if mphone_chat_history_list[idx][5] == 1:
            if  mphone_chat_history_list[idx][4] == "1":
                mphone_replies = ["I appreciate the offer, brother. I might take you up on that. mphone_emoji_smile","I appreciate the offer, brother. You don't have to feel guilty about it, though. I enjoy working there.",""]
                mphone_next_state = ["h2a","h2b",""]
            elif  mphone_chat_history_list[idx][4] == "2a":
                mphone_replies = ["I'm not sure either, but I don't think we should think too far ahead. Let's just focus on work for now and see where it takes us.","It could be how we need to run it from now on, yeah. It's too early to tell, but I wouldn't be surprised if we need to keep doing this even after the mansion is restored.",""]
                mphone_next_state = ["h3a","h3b",""]
            elif  mphone_chat_history_list[idx][4] == "2b":
                mphone_replies = ["If that makes you feel better, go ahead.","You don't have to feel guilty. I know that Derek likes the work, and Rusty's fine with it too.",""]
                mphone_next_state = ["h3c","h3d",""]
            elif  mphone_chat_history_list[idx][4] == "3b":
                mphone_replies = ["No, it should calm down, but we'll have to wait and see.","I hope and I think not. As long as we keep busting our asses now, we should be fine.",""]
                mphone_next_state = ["h3d","h3d",""]
            else:
                
                mphone_replies = ["","",""]
                mphone_next_state = ["","",""]
                mphone_contact_list[idx][2] = False
        return


    def mphone_chat_them_replies_nick(idx):
        global mphone_replies
        global mphone_contact_list
        global mphone_next_state
        global mphone_chat_history_list
        global mphone_contact_list
        global name
        if len(mphone_chat_history_list[idx][4]) == 0:
            return
        
        if mphone_chat_history_list[idx][4][0] == "h":
            mphone_chat_history_list[idx][3].append(True)
            mphone_chat_history_list[idx][4] = mphone_chat_history_list[idx][4][1:]
            if mphone_chat_history_list[idx][5] == 1:
                if mphone_chat_history_list[idx][4] == "1":
                    mphone_chat_history_list[idx][2].append("Hey, I saw that Cluck that Derek posted. If you want to switch work with me, let me know, ok? I feel kinda guilty letting you guys work over there while we're getting a chance to stay at The Pink Rose after we're done.")
                elif mphone_chat_history_list[idx][4] == "2a":
                    mphone_chat_history_list[idx][2].append("Please do. Let me know if you want it next week or whenever. On that topic, I'm not sure for how long we're gonna be working like this. Is this our new way to stay a frat from now on?")
                elif mphone_chat_history_list[idx][4] == "2b":
                    mphone_chat_history_list[idx][2].append("Thanks, [name]. That feels good to know. That removes some of the guilt, but I'll still have to check with Derek and Rusty if they want to switch.")
                elif mphone_chat_history_list[idx][4] == "3a":
                    mphone_chat_history_list[idx][2].append("Right. I hear what you're saying.")
                elif mphone_chat_history_list[idx][4] == "3b":
                    mphone_chat_history_list[idx][2].append("Ok, that's good to know. At least it won't be this intense...right?")
                elif mphone_chat_history_list[idx][4] == "3c":
                    mphone_chat_history_list[idx][2].append("Will do!")
                elif mphone_chat_history_list[idx][4] == "3d":
                    mphone_chat_history_list[idx][2].append("Thank you, [name]. I needed to hear that. mphone_emoji_smile")
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
