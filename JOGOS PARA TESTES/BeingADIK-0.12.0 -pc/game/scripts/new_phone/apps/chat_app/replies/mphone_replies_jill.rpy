init python:

    def mphone_chat_get_replies_jill(idx):
        global mphone_replies
        global mphone_contact_list
        global mphone_next_state
        global mphone_contact_list
        global mphone_chat_history_list
        
        if len(mphone_chat_history_list[idx][4]) == 0:
            return
        
        if mphone_chat_history_list[idx][5] == 1:
            if  mphone_chat_history_list[idx][4] == "1":
                if persistent.mod_wtenabled:
                    mphone_replies = ["Let me know if you want me to meet you outside.","[m_c_text]When are you showing up for the party? mphone_emoji_smile",""]
                else:
                    mphone_replies = ["Let me know if you want me to meet you outside.","When are you showing up for the party? mphone_emoji_smile",""]
                mphone_next_state = ["h2a","h2b",""]
            elif mphone_chat_history_list[idx][4] == "2a" or mphone_chat_history_list[idx][4] == "2b":
                if persistent.mod_wtenabled:
                    mphone_replies = ["I'm surprised they wanted to come.","[m_c_text]Take your time. I'm excited to see your costume!",""]
                else:
                    mphone_replies = ["I'm surprised they wanted to come.","Take your time. I'm excited to see your costume!",""]
                mphone_next_state = ["h3a","h3b",""]
            elif mphone_chat_history_list[idx][4] == "3a":
                mphone_replies = ["I like Bianca. She's fun!","So, there are more stories about her rebelling, or what you would call it?",""]
                mphone_next_state = ["h4b","h4a",""]
            elif mphone_chat_history_list[idx][4] == "3b":
                if persistent.mod_wtenabled:
                    mphone_replies = ["[m_c_text]I'm so curious about what you're dressed as! Can you tell me what that hint was again?","That sounds like an impractical costume.",""]
                else:
                    mphone_replies = ["I'm so curious about what you're dressed as! Can you tell me what that hint was again?","That sounds like an impractical costume.",""]
                mphone_next_state = ["h4c","h4d",""]
            elif mphone_chat_history_list[idx][4] == "4a":
                mphone_replies = ["Noted. I guess I'll see you in a bit. I'm gonna get back to the party now.","",""]
                mphone_next_state = ["h5a","",""]
            elif mphone_chat_history_list[idx][4] == "4b":
                mphone_replies = ["That makes me happy to hear! I'm gonna get back to the party. See you soon! mphone_emoji_kiss","",""]
                mphone_next_state = ["h5a","",""]
            elif mphone_chat_history_list[idx][4] == "4c":
                if persistent.mod_wtenabled:
                    mphone_replies = ["I can eat you? Hm... Sounds like you're dressed as food. ","[m_c_text]Who knows? I might do that. mphone_emoji_tongue",""]
                else:
                    mphone_replies = ["I can eat you? Hm... Sounds like you're dressed as food.","[m_c_text]Who knows? I might do that. mphone_emoji_tongue",""]
                mphone_next_state = ["h5b","h5c",""]
            elif mphone_chat_history_list[idx][4] == "4d":
                mphone_replies = ["I can't wait to see it! See you soon. mphone_emoji_kiss","",""]
                mphone_next_state = ["h5a","",""]
            else:
                
                mphone_replies = ["","",""]
                mphone_next_state = ["","",""]
                mphone_contact_list[idx][2] = False
        elif mphone_chat_history_list[idx][5] == 2:
            if  mphone_chat_history_list[idx][4] == "1":
                mphone_replies = ["Of course, I'll be there.","Are you sure you want to tell her about it?",""]
                mphone_next_state = ["h2a","h2b",""]
            elif mphone_chat_history_list[idx][4] == "2b":
                mphone_replies = ["Ok. As long as you're sure.","",""]
                mphone_next_state = ["h2a","",""]
            else:
                
                mphone_replies = ["","",""]
                mphone_next_state = ["","",""]
                mphone_contact_list[idx][2] = False
        elif mphone_chat_history_list[idx][5] == 3:
            if  mphone_chat_history_list[idx][4] == "1":
                mphone_replies = ["Are you ready for the party? mphone_emoji_smile","",""]
                mphone_next_state = ["h2a","",""]
            elif mphone_chat_history_list[idx][4] == "2a":
                mphone_replies = ["Beautiful! mphone_emoji_heart","Damn it... I was gonna wear that tonight.",""]
                mphone_next_state = ["h3a","h3b",""]
            elif mphone_chat_history_list[idx][4] == "2a":
                mphone_replies = ["It was going to be a surprise, but it's fine... I'll change into a shirt instead. You look way more beautiful than me wearing that. mphone_emoji_heart","",""]
                mphone_next_state = ["h3a","",""]
            else:
                
                mphone_replies = ["","",""]
                mphone_next_state = ["","",""]
                mphone_contact_list[idx][2] = False
        elif mphone_chat_history_list[idx][5] == 4:
            if  mphone_chat_history_list[idx][4] == "1":
                mphone_replies = ["Long! It felt like it would never end. I had chemistry class and lab afterward. Then I tried to study for the finals with the little time left in the day. How was yours?","",""]
                mphone_next_state = ["h2a","",""]
            elif mphone_chat_history_list[idx][4] == "2a":
                mphone_replies = ["You'll have to tell me all about that.","So, you didn't study any today?",""]
                mphone_next_state = ["h3a","h3b",""]
            elif mphone_chat_history_list[idx][4] == "3a" or mphone_chat_history_list[idx][4] == "3b":
                mphone_replies = ["As long as we take it easy. I won't have much energy left after the finals, I feel.","",""]
                mphone_next_state = ["h4a","",""]
            elif mphone_chat_history_list[idx][4] == "4a":
                mphone_replies = ["Haha! I'm sure they will suck. Let's do that.","Sounds like the perfect Friday night.",""]
                mphone_next_state = ["h5a","h5a",""]
            else:
                
                mphone_replies = ["","",""]
                mphone_next_state = ["","",""]
                mphone_contact_list[idx][2] = False
        return


    def mphone_chat_them_replies_jill(idx):
        global mphone_replies
        global mphone_contact_list
        global mphone_next_state
        global mphone_chat_history_list
        global mphone_contact_list
        global name
        global ep8_recital_failed
        global RPjill
        global task_list
        global optional_task_list
        
        if len(mphone_chat_history_list[idx][4]) == 0:
            return
        
        if mphone_chat_history_list[idx][4][0] == "h":
            mphone_chat_history_list[idx][3].append(True)
            mphone_chat_history_list[idx][4] = mphone_chat_history_list[idx][4][1:]
            if mphone_chat_history_list[idx][5] == 1:
                if mphone_chat_history_list[idx][4] == "2a":
                    mphone_chat_history_list[idx][2].append("Thank you, but you don't have to do that for me. I'm meeting up with Bianca and Liv soon.")
                elif mphone_chat_history_list[idx][4] == "2b":
                    mphone_chat_history_list[idx][2].append("Soon, I think. It depends on when Bianca and Liv show up.")
                elif mphone_chat_history_list[idx][4] == "3a":
                    mphone_chat_history_list[idx][2].append("You hear all kinds of stories from your parties, and it piqued their interest. It was Bianca, mostly, who wanted to come. I guess you can say that she's always gone against the grain.")
                elif mphone_chat_history_list[idx][4] == "3b":
                    mphone_chat_history_list[idx][2].append("I'm starting to regret my choice of costume. I'm having a hard time moving around in it.")
                elif mphone_chat_history_list[idx][4] == "4a":
                    mphone_chat_history_list[idx][2].append("Go ahead and ask her. I'm sure she'll be happy to tell you about them.")
                elif mphone_chat_history_list[idx][4] == "4b":
                    mphone_chat_history_list[idx][2].append("She likes you too. She described you as a breath of fresh air that the \"gang\" needed. She does love our dinner parties and gatherings, but she's also the one who insists we should go out more and have fun together.")
                    if not ep8_recital_failed:
                        mphone_chat_history_list[idx][3].append(True)
                        mphone_chat_history_list[idx][2].append("Also, my friends haven't stopped raving about what you did for me at the recital. You truly amazed them.")
                elif mphone_chat_history_list[idx][4] == "4c":
                    mphone_chat_history_list[idx][2].append("Something you can eat and go! mphone_emoji_laugh")
                elif mphone_chat_history_list[idx][4] == "4d":
                    mphone_chat_history_list[idx][2].append("It's not something you'd wear on any other day. mphone_emoji_laugh")
                elif mphone_chat_history_list[idx][4] == "5a":
                    mphone_chat_history_list[idx][2].append("mphone_emoji_smile mphone_emoji_kiss")
                    RPjill += 1
                    optional_task_list[2] = ""
                elif mphone_chat_history_list[idx][4] == "5b":
                    mphone_chat_history_list[idx][2].append("Interesting guess. You'll find out soon enough. mphone_emoji_kiss")
                    RPjill += 1
                    optional_task_list[2] = ""
                elif mphone_chat_history_list[idx][4] == "5c":
                    mphone_chat_history_list[idx][2].append("Well, the costume isn't edible. So, I don't think you will.")
                    mphone_chat_history_list[idx][3].append(True)
                    mphone_chat_history_list[idx][2].append("See you soon! mphone_emoji_kiss")
                    RPjill += 1
                    optional_task_list[2] = ""
                elif mphone_chat_history_list[idx][4][0] == " ":
                    mphone_replies = ["","",""]
                    mphone_next_state = ["","",""]
                    mphone_contact_list[idx][2] = False
            elif mphone_chat_history_list[idx][5] == 2:
                if mphone_chat_history_list[idx][4] == "1":
                    mphone_chat_history_list[idx][2].append("Good morning. I've been thinking about what you told me about Matthew and Liv, and I have decided to tell Bianca about it. It doesn't sit right with me to keep this from her. Could you be here with me when I tell her today? I would appreciate it so much. mphone_emoji_heart")
                elif mphone_chat_history_list[idx][4] == "2a":
                    mphone_chat_history_list[idx][2].append("Thank you! mphone_emoji_kiss")
                    task_list[7] = ""
                    updateTaskList()
                elif mphone_chat_history_list[idx][4] == "2b":
                    mphone_chat_history_list[idx][2].append("Yes. It will hurt to see her get hurt, but if I don't tell her, I will regret it forever.")
                    task_list[7] = ""
                    updateTaskList()
            elif mphone_chat_history_list[idx][5] == 3:
                if mphone_chat_history_list[idx][4] == "2a":
                    mphone_chat_history_list[idx][2].append("I am! What do you think?")
                    mphone_chat_history_list[idx][2].append("chat_jill_pic1_ep11_thumb")
                    mgallery_add_photo("chat_jill_pic1_ep11_zoomed")
                    mphone_chat_history_list[idx][3].append(True)
                elif mphone_chat_history_list[idx][4] == "3a":
                    mphone_chat_history_list[idx][2].append("Thank you! I'll call you when I'm about to leave. mphone_emoji_kiss")
                elif mphone_chat_history_list[idx][4] == "3b":
                    mphone_chat_history_list[idx][2].append("Haha! You should have told me earlier. mphone_emoji_tongue")
            elif mphone_chat_history_list[idx][5] == 4:
                if mphone_chat_history_list[idx][4] == "1":
                    mphone_chat_history_list[idx][2].append("How was your day?")
                elif mphone_chat_history_list[idx][4] == "2a":
                    mphone_chat_history_list[idx][2].append("You poor thing. But that's finals week for you. I've had a great day! I just came back home from a meeting with Jonathan. And it was productive! I have so many new ideas.")
                elif mphone_chat_history_list[idx][4] == "3a":
                    mphone_chat_history_list[idx][2].append("I will! But now I have to study some more before it gets too late. Can we see each other on Friday?")
                elif mphone_chat_history_list[idx][4] == "3b":
                    mphone_chat_history_list[idx][2].append("I studied from this morning to early afternoon. But now I have to study some more before it gets too late. Can we see each other on Friday?")
                elif mphone_chat_history_list[idx][4] == "4a":
                    mphone_chat_history_list[idx][2].append("Of course! I have a test too. How about if you come to my place and we unwind together? You can tell me all about how much your tests sucked.")
                elif mphone_chat_history_list[idx][4] == "5a":
                    mphone_chat_history_list[idx][2].append("It's a date! mphone_emoji_kiss")
                    task_list[4] = ""
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
