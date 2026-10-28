init python:

    def mphone_chat_get_replies_lily(idx):
        global mphone_replies
        global mphone_contact_list
        global mphone_next_state
        global mphone_contact_list
        global mphone_chat_history_list
        
        if len(mphone_chat_history_list[idx][4]) == 0:
            return
        
        if mphone_chat_history_list[idx][5] == 2:
            if  mphone_chat_history_list[idx][4] == "1":
                mphone_replies = ["Got one from the back?","You sure know what I need. I'll put this one to good use later. mphone_emoji_tongue","You didn't have to do that."]
                mphone_next_state = ["h2a","h2b","h2c"]
            elif  mphone_chat_history_list[idx][4] == "2a" or mphone_chat_history_list[idx][4] == "2b" or mphone_chat_history_list[idx][4] == "2c":
                mphone_replies = ["Thanks! I'll still get a dance later, yeah?","You're the best. Those pictures are so hot... I feel much better already. mphone_emoji_laugh",""]
                mphone_next_state = ["h3a","h3b",""]
            else:
                
                mphone_replies = ["","",""]
                mphone_next_state = ["","",""]
                mphone_contact_list[idx][2] = False
        return


    def mphone_chat_them_replies_lily(idx):
        global mphone_replies
        global mphone_contact_list
        global mphone_next_state
        global mphone_chat_history_list
        global mphone_contact_list
        global optional_task_list
        if len(mphone_chat_history_list[idx][4]) == 0:
            return
        
        if mphone_chat_history_list[idx][4][0] == "h":
            mphone_chat_history_list[idx][3].append(True)
            mphone_chat_history_list[idx][4] = mphone_chat_history_list[idx][4][1:]
            if mphone_chat_history_list[idx][5] == 2:
                if mphone_chat_history_list[idx][4] == "1":
                    mphone_chat_history_list[idx][2].append("Since you didn't want a private dance tonight, I figured this could serve as a little pick-me-up for whenever you get a private moment. mphone_emoji_kiss")
                    mphone_chat_history_list[idx][3].append(True)
                    mphone_chat_history_list[idx][2].append("chat_lily_pic1_ep11_thumb")
                    mgallery_add_photo("chat_lily_pic1_ep11_zoomed")
                elif mphone_chat_history_list[idx][4] == "2a":
                    mphone_chat_history_list[idx][2].append("It was going to be a surprise, but yeah, here you go.")
                    mphone_chat_history_list[idx][3].append(True)
                    mphone_chat_history_list[idx][2].append("chat_lily_pic2_ep11_thumb")
                    mgallery_add_photo("chat_lily_pic2_ep11_zoomed")
                elif mphone_chat_history_list[idx][4] == "2b":
                    mphone_chat_history_list[idx][2].append("Put this one to good use too. mphone_emoji_eggplant")
                    mphone_chat_history_list[idx][3].append(True)
                    mphone_chat_history_list[idx][2].append("chat_lily_pic2_ep11_thumb")
                    mgallery_add_photo("chat_lily_pic2_ep11_zoomed")
                elif mphone_chat_history_list[idx][4] == "2c":
                    mphone_chat_history_list[idx][2].append("I know, but I wanted to do it for you. Here's another one you might enjoy. mphone_emoji_smile")
                    mphone_chat_history_list[idx][3].append(True)
                    mphone_chat_history_list[idx][2].append("chat_lily_pic2_ep11_thumb")
                    mgallery_add_photo("chat_lily_pic2_ep11_zoomed")
                elif mphone_chat_history_list[idx][4] == "3a":
                    mphone_chat_history_list[idx][2].append("Consider this as something extra. mphone_emoji_evil")
                elif mphone_chat_history_list[idx][4] == "3b":
                    mphone_chat_history_list[idx][2].append("mphone_emoji_kiss")
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
