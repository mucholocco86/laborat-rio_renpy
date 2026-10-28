init python:

    def mphone_chat_get_replies_nicole(idx):
        global mphone_replies
        global mphone_contact_list
        global mphone_next_state
        global mphone_contact_list
        global mphone_chat_history_list
        
        if len(mphone_chat_history_list[idx][4]) == 0:
            return
        
        if mphone_chat_history_list[idx][5] == 1:
            if  mphone_chat_history_list[idx][4] == "1":
                mphone_replies = ["Perfect! Now I don't have to ask Lily for yours. mphone_emoji_tongue","You just saved me the trouble of reinstalling Swyper to contact you. mphone_emoji_kiss",""]
                mphone_next_state = ["h2a","h2b",""]
            elif mphone_chat_history_list[idx][4] == "2a" or mphone_chat_history_list[idx][4] == "2b":
                mphone_replies = ["Likewise. I do feel guilty pulling you away from work like that. Did you get into any trouble?","It was. I have to swing by more often.",""]
                mphone_next_state = ["h3a","h3b",""]
            elif mphone_chat_history_list[idx][4] == "3a" or mphone_chat_history_list[idx][4] == "3b":
                mphone_replies = ["Come on... No, you don't... Do you?","Unfair! I was drunk, and I don't even remember doing that.",""]
                mphone_next_state = ["h4a","h4b",""]
            elif mphone_chat_history_list[idx][4] == "4a" or mphone_chat_history_list[idx][4] == "4b":
                mphone_replies = ["Well... I'm happy I bring you girls some laughter.","I guess I deserve that for drinking too much.",""]
                mphone_next_state = ["h5a","h5b",""]
            else:
                
                mphone_replies = ["","",""]
                mphone_next_state = ["","",""]
                mphone_contact_list[idx][2] = False
        elif mphone_chat_history_list[idx][5] == 2:
            if  mphone_chat_history_list[idx][4] == "1":
                mphone_replies = ["Hi, Nicole!","The federal government?",""]
                mphone_next_state = ["h2a","h2b",""]
            elif  mphone_chat_history_list[idx][4] == "2a" or mphone_chat_history_list[idx][4] == "2b":
                mphone_replies = ["Not at all! You just saved me the trouble of reinstalling Swyper to contact you. mphone_emoji_kiss","Perfect! Now I don't have to ask Lily for yours. mphone_emoji_tongue",""]
                mphone_next_state = ["h3b","h3a",""]
            elif  mphone_chat_history_list[idx][4] == "3a" or mphone_chat_history_list[idx][4] == "3b":
                mphone_replies = ["Likewise. It's a shame I had to leave.","It was. I have to swing by more often.",""]
                mphone_next_state = ["h4a","h4b",""]
            elif mphone_chat_history_list[idx][4] == "4a" or mphone_chat_history_list[idx][4] == "4b":
                mphone_replies = ["Come on... No, you don't... Do you?","Unfair! I was drunk, and I don't even remember doing that.",""]
                mphone_next_state = ["h5a","h5b",""]
            elif mphone_chat_history_list[idx][4] == "5a" or mphone_chat_history_list[idx][4] == "5b":
                mphone_replies = ["Well... I'm happy I bring you girls some laughter.","I guess I deserve that for drinking too much.",""]
                mphone_next_state = ["h6a","h6b",""]
            else:
                
                mphone_replies = ["","",""]
                mphone_next_state = ["","",""]
                mphone_contact_list[idx][2] = False
        elif mphone_chat_history_list[idx][5] == 3:
            if  mphone_chat_history_list[idx][4] == "1":
                mphone_replies = ["Hey, what are you up to? mphone_emoji_smile","",""]
                mphone_next_state = ["h2a","",""]
            elif  mphone_chat_history_list[idx][4] == "2a":
                mphone_replies = ["Oof. A double shift? That sounds rough. Don't work too hard. I'm doing fine. I'm off to a Christmas party with friends soon. And this week is finals week, so my schedule is swamped with studying.","",""]
                mphone_next_state = ["h3a","",""]
            elif  mphone_chat_history_list[idx][4] == "3a":
                if persistent.mod_wtenabled:
                    mphone_replies = ["It won't be that kind of party. But there will be good food, good friends, talks and laughs.","I bet you look sexy as always tonight.",""]
                else:
                    mphone_replies = ["It won't be that kind of party. But there will be good food, good friends, talks and laughs.","[m_c_text]I bet you look sexy as always tonight.",""]
                mphone_next_state = ["h4a","h4b",""]
            elif  mphone_chat_history_list[idx][4] == "4a":
                mphone_replies = ["Thanks! Talk soon, yeah?","",""]
                mphone_next_state = ["h5a","",""]
            elif  mphone_chat_history_list[idx][4] == "4b":
                mphone_replies = ["Called it. Talk soon, yeah?","",""]
                mphone_next_state = ["h5a","",""]
            else:
                
                mphone_replies = ["","",""]
                mphone_next_state = ["","",""]
                mphone_contact_list[idx][2] = False
        return


    def mphone_chat_them_replies_nicole(idx):
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
                    mphone_chat_history_list[idx][2].append("Since I got your number, I thought it was fair that you get mine, too. XOXO Nicole mphone_emoji_kiss")
                elif mphone_chat_history_list[idx][4] == "2a":
                    mphone_chat_history_list[idx][2].append("Yes, I've pestered her enough about you already. I'm sure she doesn't want you to do the same about me. mphone_emoji_laugh")
                    mphone_chat_history_list[idx][3].append(True)
                    mphone_chat_history_list[idx][2].append("It was nice seeing you tonight.")
                elif mphone_chat_history_list[idx][4] == "2b":
                    mphone_chat_history_list[idx][2].append("Aw, shoot! But I guess we can do whatever we would do on Swyper in texts anyway.")
                    mphone_chat_history_list[idx][3].append(True)
                    mphone_chat_history_list[idx][2].append("It was nice seeing you tonight.")
                elif mphone_chat_history_list[idx][4] == "3a":
                    mphone_chat_history_list[idx][2].append("No, we girls look out for each other, and Stanley doesn't need another reason to kick you out. Haha! I wish you could behave, but I do enjoy the fun you bring to work. We call it \"pulling a [name]\" when someone gets nude and dances in the cage. mphone_emoji_laugh")
                elif mphone_chat_history_list[idx][4] == "3b":
                    mphone_chat_history_list[idx][2].append("You should! But if you did, I fear I'd be broke from the free private dances you'd get. mphone_emoji_smile")
                    mphone_chat_history_list[idx][3].append(True)
                    mphone_chat_history_list[idx][2].append("I do enjoy the fun you bring to work. We call it \"pulling a [name]\" when someone gets nude and dances in the cage. mphone_emoji_laugh")
                elif mphone_chat_history_list[idx][4] == "4a":
                    mphone_chat_history_list[idx][2].append("Haha! We totally do! The other day, Rose was all like, \"Aaahhh, my shift just started. Time to pull a [name].\". mphone_emoji_laugh")
                elif mphone_chat_history_list[idx][4] == "4b":
                    mphone_chat_history_list[idx][2].append("It's one of those stories that will live on forever here. mphone_emoji_laugh")
                elif mphone_chat_history_list[idx][4] == "5a":
                    mphone_chat_history_list[idx][2].append("The girls love you! mphone_emoji_kiss")
                    mphone_chat_history_list[idx][3].append(True)
                    mphone_chat_history_list[idx][2].append("Time for dinner. Thanks for the chat! mphone_emoji_heart")
                    if "Answer Nicole's text message" in optional_task_list:
                        optional_task_list.remove("Answer Nicole's text message")
                elif mphone_chat_history_list[idx][4] == "5b":
                    mphone_chat_history_list[idx][2].append("Kinda. mphone_emoji_smile")
                    mphone_chat_history_list[idx][3].append(True)
                    mphone_chat_history_list[idx][2].append("Time for dinner. Thanks for the chat! mphone_emoji_heart")
                    if "Answer Nicole's text message" in optional_task_list:
                        optional_task_list.remove("Answer Nicole's text message")
                elif mphone_chat_history_list[idx][4][0] == " ":
                    mphone_replies = ["","",""]
                    mphone_next_state = ["","",""]
                    mphone_contact_list[idx][2] = False
            elif mphone_chat_history_list[idx][5] == 2:
                if mphone_chat_history_list[idx][4] == "1":
                    mphone_chat_history_list[idx][2].append("Guess who?")
                elif mphone_chat_history_list[idx][4] == "2a":
                    mphone_chat_history_list[idx][2].append("Hey! I got your digits from Lily. I hope you don't mind. mphone_emoji_smile")
                elif mphone_chat_history_list[idx][4] == "2b":
                    mphone_chat_history_list[idx][2].append("Almost! It's Nicole. mphone_emoji_laugh I got your number from Lily. I hope you don't mind.")
                elif mphone_chat_history_list[idx][4] == "3a":
                    mphone_chat_history_list[idx][2].append("Yes, I've pestered her enough about you already. I'm sure she doesn't want you to do the same about me. mphone_emoji_laugh")
                    mphone_chat_history_list[idx][3].append(True)
                    mphone_chat_history_list[idx][2].append("It was nice seeing you tonight.")
                elif mphone_chat_history_list[idx][4] == "3b":
                    mphone_chat_history_list[idx][2].append("Aw, shoot! But I guess we can do whatever we would do on Swyper in texts anyway.")
                    mphone_chat_history_list[idx][3].append(True)
                    mphone_chat_history_list[idx][2].append("It was nice seeing you tonight.")
                elif mphone_chat_history_list[idx][4] == "4a":
                    mphone_chat_history_list[idx][2].append("Yeah, I was gonna grind on you! LOL! JK! I do enjoy the fun you bring to work. We call it \"pulling a [name]\" when someone gets nude and dances in the cage. mphone_emoji_laugh")
                elif mphone_chat_history_list[idx][4] == "4b":
                    mphone_chat_history_list[idx][2].append("You should! But if you did, I fear I'd be broke from the free private dances you'd get. mphone_emoji_smile")
                    mphone_chat_history_list[idx][3].append(True)
                    mphone_chat_history_list[idx][2].append("I do enjoy the fun you bring to work. We call it \"pulling a [name]\" when someone gets nude and dances in the cage. mphone_emoji_laugh")
                elif mphone_chat_history_list[idx][4] == "5a":
                    mphone_chat_history_list[idx][2].append("Haha! We totally do! The other day, Rose was all like, \"Aaahhh, my shift just started. Time to pull a [name].\". mphone_emoji_laugh")
                elif mphone_chat_history_list[idx][4] == "5b":
                    mphone_chat_history_list[idx][2].append("It's one of those stories that will live on forever here. mphone_emoji_laugh")
                elif mphone_chat_history_list[idx][4] == "6a":
                    mphone_chat_history_list[idx][2].append("The girls love you! mphone_emoji_kiss")
                    mphone_chat_history_list[idx][3].append(True)
                    mphone_chat_history_list[idx][2].append("Time for dinner. Thanks for the chat! mphone_emoji_heart")
                    if "Answer Nicole's text message" in optional_task_list:
                        optional_task_list.remove("Answer Nicole's text message")
                elif mphone_chat_history_list[idx][4] == "6b":
                    mphone_chat_history_list[idx][2].append("Kinda. mphone_emoji_smile")
                    mphone_chat_history_list[idx][3].append(True)
                    mphone_chat_history_list[idx][2].append("Time for dinner. Thanks for the chat! mphone_emoji_heart")
                    if "Answer Nicole's text message" in optional_task_list:
                        optional_task_list.remove("Answer Nicole's text message")
                elif mphone_chat_history_list[idx][4][0] == " ":
                    mphone_replies = ["","",""]
                    mphone_next_state = ["","",""]
                    mphone_contact_list[idx][2] = False
            elif mphone_chat_history_list[idx][5] == 3:
                if mphone_chat_history_list[idx][4] == "2a":
                    mphone_chat_history_list[idx][2].append("Hiii! I'm working a double shift tonight. It's a busy evening, but you caught me on a break. How are you? mphone_emoji_kiss")
                elif mphone_chat_history_list[idx][4] == "3a":
                    mphone_chat_history_list[idx][2].append("Then it's good that you're going to a party tonight to blow off steam. The double shifts aren't fun, but they happen and are hard to escape.")
                elif mphone_chat_history_list[idx][4] == "4a":
                    mphone_chat_history_list[idx][2].append("I'd much rather do that tonight, too. Enjoy!")
                    mphone_chat_history_list[idx][2].append("chat_nicole_pic1_ep11_thumb")
                    mgallery_add_photo("chat_nicole_pic1_ep11_zoomed")
                    mphone_chat_history_list[idx][2].append("By the way, this is what I'm wearing tonight. For your eyes only...")
                    mphone_chat_history_list[idx][3].append(True)
                    mphone_chat_history_list[idx][3].append(True)
                elif mphone_chat_history_list[idx][4] == "4b":
                    mphone_chat_history_list[idx][2].append("I do. For your eyes only... mphone_emoji_kiss")
                    mphone_chat_history_list[idx][2].append("chat_nicole_pic1_ep11_thumb")
                    mgallery_add_photo("chat_nicole_pic1_ep11_zoomed")
                    mphone_chat_history_list[idx][3].append(True)
                elif mphone_chat_history_list[idx][4] == "5a":
                    mphone_chat_history_list[idx][2].append("I'll have some free time during the holidays when Luke has Marvin. Let's get together and do something. mphone_emoji_kiss")
        elif mphone_chat_history_list[idx][4][0] == " ":
            mphone_replies = ["","",""]
            mphone_next_state = ["","",""]
            mphone_contact_list[idx][2] = False
        return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
