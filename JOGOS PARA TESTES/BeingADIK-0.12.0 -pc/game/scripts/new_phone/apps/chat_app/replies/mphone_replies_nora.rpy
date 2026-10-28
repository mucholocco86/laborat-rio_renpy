init python:

    def mphone_chat_get_replies_nora(idx):
        global mphone_replies
        global mphone_contact_list
        global mphone_next_state
        global mphone_contact_list
        global mphone_chat_history_list
        
        if len(mphone_chat_history_list[idx][4]) == 0:
            return
        
        if mphone_chat_history_list[idx][5] == 1:
            if  mphone_chat_history_list[idx][4] == "1":
                mphone_replies = ["How are your squats coming along?","",""]
                mphone_next_state = ["h2a","",""]
            elif mphone_chat_history_list[idx][4] == "2a":
                mphone_replies = ["Haha! I haven't seen you at the gym lately. Are you avoiding me?","Does that mean it's going well or bad? Because what you just said doesn't mean squat to me. mphone_emoji_laugh",""]
                mphone_next_state = ["h3a","h3b",""]
            elif mphone_chat_history_list[idx][4] == "3a":
                mphone_replies = ["Oh, damn. And I thought my flirting game was on point.","Aw, what a bummer.",""]
                mphone_next_state = ["h4a","h4b",""]
            elif mphone_chat_history_list[idx][4] == "3b":
                mphone_replies = ["Ok, I feel we can keep doing puns for hours. I just wanted to check how you're doing. mphone_emoji_laugh","That pun wasn't as good, though.",""]
                mphone_next_state = ["h4c","h4d",""]
            elif mphone_chat_history_list[idx][4] == "4a" or mphone_chat_history_list[idx][4] == "4b" or mphone_chat_history_list[idx][4] == "4c" or mphone_chat_history_list[idx][4] == "4d":
                mphone_replies = ["I'm fine, thanks. Well, I got rid of Swyper, so I figured I'd do it in case you wrote me something there.","",""]
                mphone_next_state = ["h5a","",""]
            elif mphone_chat_history_list[idx][4] == "5a":
                mphone_replies = ["You're joking, right? Don't make me install Swyper again to check because I'm gonna.","Yes, that's why. You can copy-paste those messages here if you don't mind. mphone_emoji_cool",""]
                mphone_next_state = ["h6a","h6b",""]
            elif mphone_chat_history_list[idx][4] == "6a":
                mphone_replies = ["Very funny, Nora. And no, I'm not going to reinstall that app. I'm happy I met you through it, but I must say I prefer meeting girls in real life.","",""]
                mphone_next_state = ["h7a","",""]
            elif mphone_chat_history_list[idx][4] == "6b":
                mphone_replies = ["I'm not going to reinstall that app. I'm happy I met you through it, but I must say I prefer meeting girls in real life.","",""]
                mphone_next_state = ["h7a","",""]
            elif mphone_chat_history_list[idx][4] == "7a":
                mphone_replies = ["So, what's the private thing you're doing now? mphone_emoji_smile","Yeah, texting and especially sending pictures to each other can be very hot. There's something scary about knowing that whatever I send is stored in your phone.",""]
                mphone_next_state = ["h8a","h8b",""]
            elif mphone_chat_history_list[idx][4] == "8a":
                mphone_replies = ["In my mind, I think you're doing the first one.","Well...which is it?",""]
                mphone_next_state = ["h9a","h9b",""]
            elif mphone_chat_history_list[idx][4] == "8b":
                mphone_replies = ["chat_nora_pic1_ep8_thumb","",""]
                mphone_next_state = ["h9c","",""]
            elif mphone_chat_history_list[idx][4] == "9a" or mphone_chat_history_list[idx][4] == "9b":
                mphone_replies = ["Very nice...","",""]
                mphone_next_state = ["h10a","",""]
            elif mphone_chat_history_list[idx][4] == "9c":
                mphone_replies = ["Likewise. mphone_emoji_smile","",""]
                mphone_next_state = ["h10a","",""]
            elif mphone_chat_history_list[idx][4] == "10a":
                mphone_replies = ["You bet. mphone_emoji_kiss","",""]
                mphone_next_state = [" ","",""]
            else:
                
                mphone_replies = ["","",""]
                mphone_next_state = ["","",""]
                mphone_contact_list[idx][2] = False
        return


    def mphone_chat_them_replies_nora(idx):
        global mphone_replies
        global mphone_contact_list
        global mphone_next_state
        global mphone_chat_history_list
        global mphone_contact_list
        global name
        global task_list
        
        if len(mphone_chat_history_list[idx][4]) == 0:
            return
        
        if mphone_chat_history_list[idx][4][0] == "h":
            mphone_chat_history_list[idx][3].append(True)
            mphone_chat_history_list[idx][4] = mphone_chat_history_list[idx][4][1:]
            if mphone_chat_history_list[idx][5] == 1:
                if mphone_chat_history_list[idx][4] == "2a":
                    mphone_chat_history_list[idx][2].append("They are going through ups and downs.")
                elif mphone_chat_history_list[idx][4] == "3a":
                    mphone_chat_history_list[idx][2].append("Yes, you got me. I even changed gyms because of you.")
                elif mphone_chat_history_list[idx][4] == "3b":
                    mphone_chat_history_list[idx][2].append("Squat do you mean?")
                elif mphone_chat_history_list[idx][4] == "4a":
                    mphone_chat_history_list[idx][2].append("You are persistent; I'll give you that.")
                    mphone_chat_history_list[idx][3].append(True)
                    mphone_chat_history_list[idx][2].append("How are you doing? I appreciate that you showed some initiative and texted me.")
                elif mphone_chat_history_list[idx][4] == "4b":
                    mphone_chat_history_list[idx][2].append("If the new gym doesn't work out, I might return. Maybe in a few days or so.")
                    mphone_chat_history_list[idx][3].append(True)
                    mphone_chat_history_list[idx][2].append("How are you doing? I appreciate that you showed some initiative and texted me.")
                elif mphone_chat_history_list[idx][4] == "4c":
                    mphone_chat_history_list[idx][2].append("I do find puns enjoyable, and they serve as good brain teasers. Aside from a hectic week, I'm doing well.")
                    mphone_chat_history_list[idx][3].append(True)
                    mphone_chat_history_list[idx][2].append("How are you doing? I appreciate that you showed some initiative and texted me.")
                elif mphone_chat_history_list[idx][4] == "4d":
                    mphone_chat_history_list[idx][2].append("I agree. I think we did what we could with that word.")
                    mphone_chat_history_list[idx][3].append(True)
                    mphone_chat_history_list[idx][2].append("How are you doing? I appreciate that you showed some initiative and texted me.")
                elif mphone_chat_history_list[idx][4] == "5a":
                    mphone_chat_history_list[idx][2].append("I see. So that's why you haven't replied to my erotic messages and nude photos.")
                elif mphone_chat_history_list[idx][4] == "6a":
                    mphone_chat_history_list[idx][2].append("Haha. Who knows?")
                elif mphone_chat_history_list[idx][4] == "6b":
                    mphone_chat_history_list[idx][2].append("You called my bluff. Impressive. I was picturing you reinstalling Swyper seconds after I sent my message.")
                elif mphone_chat_history_list[idx][4] == "7a":
                    mphone_chat_history_list[idx][2].append("How old-fashioned. I do find that texting can be titillating once you've made that initial connection with someone. There's something special about being in the confines of your home and texting that I enjoy. For instance, we could both be doing something private right now with neither of us any the wiser.")
                elif mphone_chat_history_list[idx][4] == "8a":
                    mphone_chat_history_list[idx][2].append("If you only knew. I could be nude under my covers or sitting in my casual clothes watching TV.")
                elif mphone_chat_history_list[idx][4] == "8b":
                    mphone_chat_history_list[idx][2].append("You better be careful what you send me, then. I'd hate it if you sent me a picture of yourself right now.")
                elif mphone_chat_history_list[idx][4] == "9a":
                    mphone_chat_history_list[idx][2].append("Sorry to disappoint you.")
                    mphone_chat_history_list[idx][3].append(True)
                    mphone_chat_history_list[idx][2].append("chat_nora_pic2_ep8_thumb")
                elif mphone_chat_history_list[idx][4] == "9b":
                    mphone_chat_history_list[idx][2].append("chat_nora_pic2_ep8_thumb")
                elif mphone_chat_history_list[idx][4] == "9c":
                    mphone_chat_history_list[idx][2].append("Nice haircut; I almost didn't recognize you. Also, now you're trapped in my phone forever.")
                    mphone_chat_history_list[idx][3].append(True)
                    mphone_chat_history_list[idx][2].append("chat_nora_pic2_ep8_thumb")
                elif mphone_chat_history_list[idx][4] == "10a":
                    mphone_chat_history_list[idx][2].append("Thanks for the talk, [name]. I rather enjoyed it. Let's do it again sometime soon.")
                    task_list[6] = ""
                    updateTaskList()
        elif mphone_chat_history_list[idx][4][0] == " ":
            mphone_replies = ["","",""]
            mphone_next_state = ["","",""]
            mphone_contact_list[idx][2] = False
        return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
