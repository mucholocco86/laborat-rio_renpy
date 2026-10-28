init python:

    def mphone_chat_get_replies_zoey(idx):
        global mphone_replies
        global mphone_contact_list
        global mphone_next_state
        global mphone_chat_history_list
        global ep9_mad_at_zoey
        global ep11_zoey_kiss
        
        if len(mphone_chat_history_list[idx][4]) == 0:
            return
        
        if mphone_chat_history_list[idx][5] == 1:
            if  mphone_chat_history_list[idx][4] == "1":
                mphone_replies = ["Ah, that's Jacob.","Awesome! mphone_emoji_cool",""]
                mphone_next_state = ["h2a"," ",""]
            else:
                
                mphone_replies = ["","",""]
                mphone_next_state = ["","",""]
                mphone_contact_list[idx][2] = False
        elif mphone_chat_history_list[idx][5] == 2:
            if  mphone_chat_history_list[idx][4] == "1":
                mphone_replies = ["I'm free all day today. I've got a study day, so not much else planned.","",""]
                mphone_next_state = ["h2a","",""]
            elif  mphone_chat_history_list[idx][4] == "2a":
                mphone_replies = ["Sure. I'm up for it.","I don't feel like it today.",""]
                mphone_next_state = ["h3a","h3b",""]
            elif  mphone_chat_history_list[idx][4] == "3b":
                mphone_replies = ["Is it that boring?","",""]
                mphone_next_state = ["h4a","",""]
            elif  mphone_chat_history_list[idx][4] == "4a":
                if ep9_mad_at_zoey:
                    mphone_replies = ["Ok, I can hang with you for a bit.","Sorry, but I don't want to.",""]
                    mphone_next_state = ["h4b","h4c",""]
                else:
                    mphone_replies = ["Ok, I can hang with you for a bit.","",""]
                    mphone_next_state = ["h4b","",""]
            else:
                
                mphone_replies = ["","",""]
                mphone_next_state = ["","",""]
                mphone_contact_list[idx][2] = False
        elif mphone_chat_history_list[idx][5] == 3:
            if  mphone_chat_history_list[idx][4] == "1":
                mphone_replies = ["Did you get home ok? I must have missed it when you left. Happy Thanksgiving! mphone_emoji_smile","I hope our talk last night didn't bum you out too much. It felt weird saying those things out loud to you, even though I've wanted to say them for quite some time.",""]
                mphone_next_state = ["h2a","h2a",""]
            else:
                
                mphone_replies = ["","",""]
                mphone_next_state = ["","",""]
                mphone_contact_list[idx][2] = False
        elif mphone_chat_history_list[idx][5] == 4:
            if  mphone_chat_history_list[idx][4] == "1":
                mphone_replies = ["Sure does. How's your cold? Feeling better?","",""]
                mphone_next_state = ["h2a","",""]
            elif  mphone_chat_history_list[idx][4] == "2a":
                if persistent.mod_wtenabled:
                    mphone_replies = ["You picked a bad time to return from San Diego. Weather-wise.","[m_c_text]Cute pic.",""]
                else:
                    mphone_replies = ["You picked a bad time to return from San Diego. Weather-wise.","Cute pic.",""]
                mphone_next_state = ["h3a","h3b",""]
            elif  mphone_chat_history_list[idx][4] == "3a" or mphone_chat_history_list[idx][4] == "3b":
                mphone_replies = ["We're putting up Christmas decorations today. We're lugging boxes all over the place. It's a big mess, but many are helping out.","",""]
                mphone_next_state = ["h4a","",""]
            else:
                
                mphone_replies = ["","",""]
                mphone_next_state = ["","",""]
                mphone_contact_list[idx][2] = False
        elif mphone_chat_history_list[idx][5] == 5:
            if ep11_zoey_kiss == 2:
                if  mphone_chat_history_list[idx][4] == "1":
                    mphone_replies = ["Hey. I've been doing some thinking.","",""]
                    mphone_next_state = ["h2a","",""]
                elif  mphone_chat_history_list[idx][4] == "2a":
                    mphone_replies = ["I've been thinking about you and us. Everything we went through and what we said to each other. Like I told you after we kissed, I wanted to make sure that I didn't kiss you for the wrong reasons.","",""]
                    mphone_next_state = ["h3a","",""]
                elif  mphone_chat_history_list[idx][4] == "3a":
                    mphone_replies = ["I think I figured it out. But I don't wanna say it over text.","",""]
                    mphone_next_state = ["h4a","",""]
                elif  mphone_chat_history_list[idx][4] == "4a":
                    mphone_replies = ["It's good. mphone_emoji_smile","",""]
                    mphone_next_state = ["h5a","",""]
                elif  mphone_chat_history_list[idx][4] == "5a":
                    mphone_replies = ["It's not a joke, but I want to tell you in person.","",""]
                    mphone_next_state = ["h6a","",""]
                else:
                    
                    mphone_replies = ["","",""]
                    mphone_next_state = ["","",""]
                    mphone_contact_list[idx][2] = False
            else:
                if  mphone_chat_history_list[idx][4] == "1":
                    mphone_replies = ["Hey, how are you feeling? I feel bad for what happened at the party between us. I think it's because you mean a lot to me, and it hurt to let you down when you opened up like that. I hope we can still be friends.","",""]
                    mphone_next_state = ["h2a","",""]
                elif  mphone_chat_history_list[idx][4] == "2a":
                    mphone_replies = ["I'm here when you feel like you're ready to talk. I'll wait for you.","",""]
                    mphone_next_state = ["h3a","",""]
                else:
                    
                    mphone_replies = ["","",""]
                    mphone_next_state = ["","",""]
                    mphone_contact_list[idx][2] = False
        return


    def mphone_chat_them_replies_zoey(idx):
        global mphone_replies
        global mphone_contact_list
        global mphone_next_state
        global mphone_chat_history_list
        global task_list
        global ep10_zoey_hangout
        global optional_task_list
        global ep11_zoey_kiss
        
        if len(mphone_chat_history_list[idx][4]) == 0:
            return
        
        if mphone_chat_history_list[idx][4][0] == "h":
            mphone_chat_history_list[idx][3].append(True)
            mphone_chat_history_list[idx][4] = mphone_chat_history_list[idx][4][1:]
            if mphone_chat_history_list[idx][5] == 1:
                if mphone_chat_history_list[idx][4] == "1":
                    mphone_chat_history_list[idx][2].append("I'm here. This army guy helped me get in.")
                elif mphone_chat_history_list[idx][4] == "2a":
                    mphone_chat_history_list[idx][2].append("Yeah, that's him. You seem busy, but I'm around when you got time.")
            elif mphone_chat_history_list[idx][5] == 2:
                if mphone_chat_history_list[idx][4] == "1":
                    mphone_chat_history_list[idx][2].append("Are you free this afternoon?")
                elif mphone_chat_history_list[idx][4] == "2a":
                    mphone_chat_history_list[idx][2].append("Sweet! Let's hang out.")
                elif mphone_chat_history_list[idx][4] == "3a":
                    mphone_chat_history_list[idx][2].append("Awesome! My day just got better. I'll drop by later. mphone_emoji_smile")
                    task_list[2] = ""
                    updateTaskList()
                elif mphone_chat_history_list[idx][4] == "3b":
                    mphone_chat_history_list[idx][2].append("It's just for a little while. Please? I'm going crazy over here.")
                elif mphone_chat_history_list[idx][4] == "4a":
                    mphone_chat_history_list[idx][2].append("Yeah, and I wanna see you, dude. Let's do this; I'll drop by, and if you think it sucks, you can send me back home.")
                elif mphone_chat_history_list[idx][4] == "4b":
                    mphone_chat_history_list[idx][2].append("Yes! My day just got better. mphone_emoji_smile")
                    task_list[2] = ""
                    updateTaskList()
                elif mphone_chat_history_list[idx][4] == "4c":
                    mphone_chat_history_list[idx][2].append("Alright. I'm not gonna force you. mphone_emoji_smile")
                    ep10_zoey_hangout = False
                    task_list[2] = ""
                    updateTaskList()
            elif mphone_chat_history_list[idx][5] == 3:
                if mphone_chat_history_list[idx][4] == "2a":
                    mphone_chat_history_list[idx][3].pop()
                    optional_task_list[2] = ""
                    updateTaskList()
            elif mphone_chat_history_list[idx][5] == 4:
                if mphone_chat_history_list[idx][4] == "1":
                    mphone_chat_history_list[idx][2].append("Yeesh. This snow sucks.")
                elif mphone_chat_history_list[idx][4] == "2a":
                    mphone_chat_history_list[idx][2].append("chat_zoey_pic1_ep11_thumb")
                    mgallery_add_photo("chat_zoey_pic1_ep11_zoomed")
                    mphone_chat_history_list[idx][3].append(True)
                    mphone_chat_history_list[idx][2].append("Thanks, I'm good. I'm stuck at work today, but it's alright. At least I'm not freezing in here.")
                elif mphone_chat_history_list[idx][4] == "3a":
                    mphone_chat_history_list[idx][2].append("I miss the warmth of the West Coast, but that's about it... I guess you can't be completely satisfied with everything, no matter where you are. What are you up to?")
                elif mphone_chat_history_list[idx][4] == "3b":
                    mphone_chat_history_list[idx][2].append("chat_zoey_pic2_ep11_thumb")
                    mgallery_add_photo("chat_zoey_pic2_ep11_zoomed")
                    mphone_chat_history_list[idx][3].append(True)
                    mphone_chat_history_list[idx][2].append("Stahp it. What are you up to? mphone_emoji_tongue")
                elif mphone_chat_history_list[idx][4] == "4a":
                    mphone_chat_history_list[idx][2].append("Cool. I bet it will look sweet. Break time is over. Lates.")
            elif mphone_chat_history_list[idx][5] == 5:
                if ep11_zoey_kiss == 2:
                    if mphone_chat_history_list[idx][4] == "2a":
                        mphone_chat_history_list[idx][2].append("Hi. I've been close to calling you like 50 times but forced myself to give you space. What are you thinking?")
                    elif mphone_chat_history_list[idx][4] == "3a":
                        mphone_chat_history_list[idx][2].append("Yeah. And did you?")
                        mphone_chat_history_list[idx][3].append(True)
                        mphone_chat_history_list[idx][2].append("I'm fucking shaking right now, haha.")
                    elif mphone_chat_history_list[idx][4] == "4a":
                        mphone_chat_history_list[idx][2].append("I get it... I mean, I don't get what you want to say, but I get that you don't want to say it in a text. I'm just hoping it's good news. You can't say that either, yeah?")
                    elif mphone_chat_history_list[idx][4] == "5a":
                        mphone_chat_history_list[idx][2].append("No way...")
                        mphone_chat_history_list[idx][3].append(True)
                        mphone_chat_history_list[idx][2].append("This isn't a joke, right?")
                    elif mphone_chat_history_list[idx][4] == "6a":
                        mphone_chat_history_list[idx][2].append("Totally. I'm just gonna go chill out somewhere now, and I'll see you soon, ok?")
                        task_list[1] = ""
                        event_list.append("ep11_zoey_joy_label")
                        updateTaskList()
                else:
                    if mphone_chat_history_list[idx][4] == "2a":
                        mphone_chat_history_list[idx][2].append("I'm not ready for this talk. I don't know what to say to you now.")
                    elif mphone_chat_history_list[idx][4] == "3a":
                        mphone_chat_history_list[idx][2].append("Ok.")
                        task_list[1] = ""
                        updateTaskList()
        
        elif mphone_chat_history_list[idx][4][0] == " ":
            mphone_replies = ["","",""]
            mphone_next_state = ["","",""]
            mphone_contact_list[idx][2] = False
        return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
