init python:

    def mphone_chat_get_replies_melanie(idx):
        global mphone_replies
        global mphone_contact_list
        global mphone_next_state
        global mphone_contact_list
        global mphone_chat_history_list
        
        if len(mphone_chat_history_list[idx][4]) == 0:
            return
        
        if mphone_chat_history_list[idx][5] == 1:
            if  mphone_chat_history_list[idx][4] == "1":
                mphone_replies = ["What's up, Mel? Thanks for coming to the party. I hope you had fun.","",""]
                mphone_next_state = ["h2a","",""]
            elif  mphone_chat_history_list[idx][4] == "2a":
                mphone_replies = ["Were you really? You didn't send any vibes my way.","",""]
                mphone_next_state = ["h3a","",""]
            elif  mphone_chat_history_list[idx][4] == "3a":
                if persistent.mod_wtenabled:
                    mphone_replies = ["[m_c_text]You didn't drown in the noise. I saw what you were wearing. You were smoking hot in that.","Sorry, I was too busy with party stuff. I'll do better next time.",""]
                else:
                    mphone_replies = ["You didn't drown in the noise. I saw what you were wearing. You were smoking hot in that.","Sorry, I was too busy with party stuff. I'll do better next time.",""]
                mphone_next_state = ["h4a","h4b",""]
            elif  mphone_chat_history_list[idx][4] == "4a" or mphone_chat_history_list[idx][4] == "4b":
                if persistent.mod_wtenabled:
                    mphone_replies = ["[m_c_text]Fuck... I wish I had. I'm off to a Christmas party soon. And the things I wanna do to you will take longer time than I have on my hands.","Not tonight.",""]
                else:
                    mphone_replies = ["Fuck... I wish I had. I'm off to a Christmas party soon. And the things I wanna do to you will take longer time than I have on my hands.","Not tonight.",""]
                mphone_next_state = ["h5a","h5b",""]
            elif  mphone_chat_history_list[idx][4] == "5a":
                if persistent.mod_wtenabled:
                    mphone_replies = ["[m_c_text]I'd really wanna eat you out... I didn't get the chance to do that last time. mphone_emoji_tongue","It would be easier to list the things I wouldn't wanna do to you. mphone_emoji_evil"]
                else:
                    mphone_replies = ["I'd really wanna eat you out... I didn't get the chance to do that last time. mphone_emoji_tongue","It would be easier to list the things I wouldn't wanna do to you. mphone_emoji_evil"]
                mphone_next_state = ["h6a","h6b",""]
            elif  mphone_chat_history_list[idx][4] == "6a":
                mphone_replies = ["Fuck, yes. Give me a piece of that...","",""]
                mphone_next_state = ["h7a","",""]
            else:
                
                mphone_replies = ["","",""]
                mphone_next_state = ["","",""]
                mphone_contact_list[idx][2] = False
        return


    def mphone_chat_them_replies_melanie(idx):
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
                    mphone_chat_history_list[idx][2].append("I have to admit I was disappointed in you at the party. I dress up sexy like that, and you give me nothing.")
                elif mphone_chat_history_list[idx][4] == "3a":
                    mphone_chat_history_list[idx][2].append("I tried, but I guess I drowned in the noise. There were too many hot girls there.")
                elif mphone_chat_history_list[idx][4] == "4a":
                    mphone_chat_history_list[idx][2].append("I figured you'd like it. I took this picture for you. mphone_emoji_kiss")
                    mphone_chat_history_list[idx][3].append(True)
                    mphone_chat_history_list[idx][3].append(True)
                    mphone_chat_history_list[idx][2].append("chat_melanie_pic1_ep11_thumb")
                    mgallery_add_photo("chat_melanie_pic1_ep11_zoomed")
                    mphone_chat_history_list[idx][2].append("By the way, I got horny again. Do you have time for me?")
                elif mphone_chat_history_list[idx][4] == "4b":
                    mphone_chat_history_list[idx][2].append("It's ok. By the way, I got horny again. Do you have time for me?")
                elif mphone_chat_history_list[idx][4] == "5a":
                    mphone_chat_history_list[idx][2].append("Mmm... And what are those things you would do to me?")
                elif mphone_chat_history_list[idx][4] == "5b":
                    mphone_chat_history_list[idx][2].append("Alright. Another time, then.")
                elif mphone_chat_history_list[idx][4] == "6a":
                    mphone_chat_history_list[idx][2].append("Yeah? Is this what you want to eat?")
                    mphone_chat_history_list[idx][2].append("chat_melanie_pic2_ep11_thumb")
                    mgallery_add_photo("chat_melanie_pic2_ep11_zoomed")
                    mphone_chat_history_list[idx][3].append(True)
                elif mphone_chat_history_list[idx][4] == "6b":
                    mphone_chat_history_list[idx][2].append("I like the sound of that. Have fun tonight. mphone_emoji_kiss")
                elif mphone_chat_history_list[idx][4] == "7a":
                    mphone_chat_history_list[idx][2].append("I'll keep it fresh, shaven, and tasty for you. Have fun tonight. mphone_emoji_kiss")
                elif mphone_chat_history_list[idx][4][0] == " ":
                    mphone_replies = ["","",""]
                    mphone_next_state = ["","",""]
                    mphone_contact_list[idx][2] = False
        elif mphone_chat_history_list[idx][4][0] == " ":
            mphone_replies = ["","",""]
            mphone_next_state = ["","",""]
            mphone_contact_list[idx][2] = False
        return

# Decompiled by unrpyc {v1.3.2}: https://github.com/CensoredUsername/unrpyc dev-branch
