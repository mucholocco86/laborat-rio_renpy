init python:

    def mphone_chat_get_replies_jade(idx):
        global mphone_replies
        global mphone_contact_list
        global mphone_next_state
        global mphone_contact_list
        global mphone_chat_history_list
        global jade
        
        if len(mphone_chat_history_list[idx][4]) == 0:
            return
        
        if mphone_chat_history_list[idx][5] == 1:
            if  mphone_chat_history_list[idx][4] == "1":
                mphone_replies = ["Nice... Got any more of those?","I'm studying here.","How's your headache?"]
                mphone_next_state = ["h2a","h2b","h2e"]
            elif mphone_chat_history_list[idx][4] == "2b":
                mphone_replies = ["Yeah, it's too risky. How's your headache?","Ok, do one more...",""]
                mphone_next_state = ["h2e","h2d",""]
            elif mphone_chat_history_list[idx][4] == "2d" or mphone_chat_history_list[idx][4] == "2a":
                mphone_replies = ["Nice. These will come in handy. How's your headache? mphone_emoji_tongue","That's so hot! Why don't you just come up and talk to me?",""]
                mphone_next_state = ["h2e","h3a",""]
            elif mphone_chat_history_list[idx][4] == "2e" or mphone_chat_history_list[idx][4] == "3a":
                mphone_replies = ["I'll miss Cathy, too. I can't imagine how you must be feeling right now, teaching side by side with her for that long.","If it helps, she told me that she was excited about changing jobs, even if the reason why she's doing it isn't the best.",""]
                mphone_next_state = ["h3b","h3c",""]
            elif mphone_chat_history_list[idx][4] == "3b" or mphone_chat_history_list[idx][4] == "3c":
                mphone_replies = ["I'm here if you need to talk more about it. I can try my best to help you process it.","Stay strong, Jade. Changes like these suck, but there isn't much you can do about them. And you'll still be able to see her outside of work.",""]
                mphone_next_state = ["h4a","h4b",""]
            elif mphone_chat_history_list[idx][4] == "4a" or mphone_chat_history_list[idx][4] == "4b":
                mphone_replies = ["Don't feel like you can't talk to me too, though. I enjoy the sexy time we've had together, but I like talking to you too. It doesn't have to be one or the other.","I guess I am your lover. That sounds dirty.",""]
                mphone_next_state = ["h5a","h5b",""]
            elif mphone_chat_history_list[idx][4] == "5a":
                mphone_replies = ["Maybe next time. mphone_emoji_kiss","At least it will be easier to make \"arrangements\" with the phone chats.",""]
                mphone_next_state = ["h6a","h6a",""]
            elif mphone_chat_history_list[idx][4] == "5b":
                mphone_replies = ["Yeah, I remember that from our first time together.","Save that energy for me, [jade]. At least it will be easier to make \"arrangements\" with the phone chats.",""]
                mphone_next_state = ["h6a","h6a",""]
            else:
                
                mphone_replies = ["","",""]
                mphone_next_state = ["","",""]
                mphone_contact_list[idx][2] = False
        elif mphone_chat_history_list[idx][5] == 2:
            mphone_replies = ["","",""]
            mphone_next_state = ["","",""]
            mphone_contact_list[idx][2] = False
        elif mphone_chat_history_list[idx][5] == 3:
            if  mphone_chat_history_list[idx][4] == "1":
                mphone_replies = ["Fuck me! That's so hot. Every time I think about the last time we spent together, I get hard and have to rub one out. These pictures will help me for sure. mphone_emoji_kiss","",""]
                mphone_next_state = ["h2a","",""]
            elif mphone_chat_history_list[idx][4] == "2a":
                mphone_replies = ["When can I see you again?","My hand doesn't feel as good as your tight holes, either.",""]
                mphone_next_state = ["h3a","h3b",""]
            elif mphone_chat_history_list[idx][4] == "3b":
                mphone_replies = ["When can I see you again?","",""]
                mphone_next_state = ["h3a","h",""]
            elif mphone_chat_history_list[idx][4] == "3a":
                mphone_replies = ["Any time, even on short notice, I'm yours. There are a lot of classrooms on campus, just saying. mphone_emoji_evil","",""]
                mphone_next_state = ["h4a","h",""]
            else:
                
                mphone_replies = ["","",""]
                mphone_next_state = ["","",""]
                mphone_contact_list[idx][2] = False
        elif mphone_chat_history_list[idx][5] == 4:
            if  mphone_chat_history_list[idx][4] == "1":
                mphone_replies = ["I don't know how to tell you this, but I have to do it... I've decided that I want to give another relationship a go, so I can't be sneaking around with you anymore. It sucks because I've enjoyed it a lot, but it wouldn't feel good to continue for me. I hope you understand.","",""]
                mphone_next_state = ["h2a","",""]
            elif mphone_chat_history_list[idx][4] == "2a":
                mphone_replies = ["No, I'm dead serious. I can't keep seeing you.","I wish I were. I'd continue in a heartbeat if it felt like I could. But I don't want to start a relationship by having an affair.",""]
                mphone_next_state = ["h3a","h3b",""]
            elif mphone_chat_history_list[idx][4] == "3b" or mphone_chat_history_list[idx][4] == "3a":
                mphone_replies = ["Please, don't make this harder for me. I didn't wish it would come to this. We had fun together in the past; let's leave it at that. I won't tell anyone about what we have done, I swear.","Bye, Jade.",""]
                mphone_next_state = ["h4a","h4b",""]
            else:
                
                mphone_replies = ["","",""]
                mphone_next_state = ["","",""]
                mphone_contact_list[idx][2] = False
        
        return


    def mphone_chat_them_replies_jade(idx):
        global mphone_replies
        global mphone_contact_list
        global mphone_next_state
        global mphone_chat_history_list
        global mphone_contact_list
        global name
        global ep7_done_jade_text
        global jade
        global optional_task_list
        global task_list
        
        if len(mphone_chat_history_list[idx][4]) == 0:
            return
        
        if mphone_chat_history_list[idx][4][0] == "h":
            mphone_chat_history_list[idx][3].append(True)
            mphone_chat_history_list[idx][4] = mphone_chat_history_list[idx][4][1:]
            if mphone_chat_history_list[idx][5] == 1:
                if mphone_chat_history_list[idx][4] == "1":
                    mphone_chat_history_list[idx][2].append("chat_jade_pic1_ep7_thumb")
                    mphone_chat_history_list[idx][3].append(True)
                    mphone_chat_history_list[idx][2].append("I can see you.")
                elif mphone_chat_history_list[idx][4] == "2a":
                    mphone_chat_history_list[idx][2].append("chat_jade_pic2_ep7_thumb")
                    mphone_chat_history_list[idx][3].append(True)
                    mphone_chat_history_list[idx][2].append("I might...")
                elif mphone_chat_history_list[idx][4] == "2b":
                    mphone_chat_history_list[idx][2].append("I can see that. You're such a good student. When half of the class chose to leave, you stayed behind.")
                    mphone_chat_history_list[idx][2].append("Maybe I should stop?")
                    mphone_chat_history_list[idx][3].append(True)
                elif mphone_chat_history_list[idx][4] == "2d":
                    mphone_chat_history_list[idx][2].append("Last one.")
                    mphone_chat_history_list[idx][2].append("chat_jade_pic2_ep7_thumb")
                    mphone_chat_history_list[idx][3].append(True)
                elif mphone_chat_history_list[idx][4] == "2e":
                    mphone_chat_history_list[idx][2].append("It's not really a headache. I don't have the energy to teach today, considering the circumstances.")
                elif mphone_chat_history_list[idx][4] == "3a":
                    mphone_chat_history_list[idx][2].append("This is less obvious, I think. And it doesn't give away that Cathy, not a headache, is the real reason why I'm not teaching today.")
                elif mphone_chat_history_list[idx][4] == "3b":
                    mphone_chat_history_list[idx][2].append("Everything comes to an end, [name]. It's something you learn living life. Especially in a university, you'll see how fast people around you change their trajectories and disappear from your life, only to become acquaintances at best. It's like you only have a year or two to get to know them and care for them before they're gone. With Cathy, it was different. That's why it hurts more. I didn't think she'd end up leaving my side so soon.")
                elif mphone_chat_history_list[idx][4] == "3c":
                    mphone_chat_history_list[idx][2].append("Yes, I'm well aware of her feelings, and I sincerely hope that's the case and that it's not an escape mechanism that she uses to cope with the sad truth that she can't stay here and be mentally healthy.")
                elif mphone_chat_history_list[idx][4] == "4a":
                    mphone_chat_history_list[idx][2].append("I appreciate that. To be honest, it's not why I started this chat with you. I was looking for a distraction and saw my lover sitting in front of me. mphone_emoji_kiss")
                elif mphone_chat_history_list[idx][4] == "4b":
                    mphone_chat_history_list[idx][2].append("That's true. We won't lose contact over this, even though I will miss the daily interactions with her. I didn't intend to burden you with this talk; I was merely looking for a distraction and saw my lover sitting in front of me. mphone_emoji_kiss")
                elif mphone_chat_history_list[idx][4] == "5a":
                    mphone_chat_history_list[idx][2].append("I suppose you're right about that. I am fond of the talks we've had as well. They have been very...real. Thank you, [name]. If we were alone, I'd steal a kiss from you. mphone_emoji_kiss")
                elif mphone_chat_history_list[idx][4] == "5b":
                    if jade == "mommy" or jade == "Mommy":
                        mphone_chat_history_list[idx][2].append("Mommy's hot and young lover. Mmm... Ok, Mommy has to snap out of it before she gets horny. Although being horny and frustrated makes for some hot sex.")
                    else:
                        mphone_chat_history_list[idx][2].append("My hot and young lover. Mmm... Ok, I have to snap out of it before I get horny. Although being horny and frustrated makes for some really good sex.")
                elif mphone_chat_history_list[idx][4] == "6a":
                    ep7_done_jade_text = True
                    mphone_chat_history_list[idx][2].append("Definitely. Now go back to studying, or I will have to scold you for playing with your phone. You know what? I think I might do that either way.")
                elif mphone_chat_history_list[idx][4][0] == " ":
                    mphone_replies = ["","",""]
                    mphone_next_state = ["","",""]
                    mphone_contact_list[idx][2] = False
            elif mphone_chat_history_list[idx][5] == 2:
                if mphone_chat_history_list[idx][4] == "1":
                    mphone_chat_history_list[idx][3].append(True)
                    mphone_chat_history_list[idx][3].append(True)
                    mphone_chat_history_list[idx][2].append("Hey, lover... Are you available? mphone_emoji_kiss")
                    mphone_chat_history_list[idx][2].append("Ugh... I'm so horny right now. I think I tried calling you four times.")
                    mphone_chat_history_list[idx][2].append("Call me when you're free. If I don't answer, I'll call you back.")
                elif mphone_chat_history_list[idx][4][0] == " ":
                    mphone_replies = ["","",""]
                    mphone_next_state = ["","",""]
                    mphone_contact_list[idx][2] = False
            elif mphone_chat_history_list[idx][5] == 3:
                if mphone_chat_history_list[idx][4] == "1":
                    mphone_chat_history_list[idx][2].append("I'm lying in the bathtub, thinking of you.")
                    mphone_chat_history_list[idx][3].append(True)
                    mphone_chat_history_list[idx][3].append(True)
                    mphone_chat_history_list[idx][2].append("chat_jade_pic1_ep8_thumb")
                    mphone_chat_history_list[idx][2].append("chat_jade_pic2_ep8_thumb")
                elif mphone_chat_history_list[idx][4] == "2a":
                    mphone_chat_history_list[idx][2].append("Yes. Rub one out for me. The showerhead doesn't feel nearly as good as your hard cock inside of my pussy.")
                elif mphone_chat_history_list[idx][4] == "3a":
                    mphone_chat_history_list[idx][2].append("Ugh... I don't know. I wish you were living under my bed so I could pick you up and use you whenever there was time for it. I'm hoping that my husband goes away for a trip soon. As soon as that happens, you'll be staying with me until he returns. mphone_emoji_kiss")
                elif mphone_chat_history_list[idx][4] == "3b":
                    mphone_chat_history_list[idx][2].append("Keep talking like that, and I will have to have another round of the showerhead. mphone_emoji_kiss")
                elif mphone_chat_history_list[idx][4] == "4a":
                    mphone_chat_history_list[idx][2].append("You're such a naughty boy. And I love it. I'll keep my eyes open for any unused lecture halls that might suit our needs and urges. mphone_emoji_kiss mphone_emoji_evil")
                    optional_task_list[2] = ""
                elif mphone_chat_history_list[idx][4][0] == " ":
                    mphone_replies = ["","",""]
                    mphone_next_state = ["","",""]
                    mphone_contact_list[idx][2] = False
            elif mphone_chat_history_list[idx][5] == 4:
                if mphone_chat_history_list[idx][4] == "2a":
                    mphone_chat_history_list[idx][2].append("Are you joking?")
                elif mphone_chat_history_list[idx][4] == "3a":
                    mphone_chat_history_list[idx][2].append("Just like that? Do you take back all of the things you've said and done to me? What about the fact that I've risked a lot by having this affair with you? Does that mean nothing to you?")
                elif mphone_chat_history_list[idx][4] == "3b":
                    mphone_chat_history_list[idx][2].append("You don't want to have an affair, but I guess it's ok that you enticed me to initiate an affair with you.")
                elif mphone_chat_history_list[idx][4] == "4a":
                    mphone_chat_history_list[idx][2].append("You better not, or I will take you down with me. Do you hear that? This is fucking ridiculous; there's always another woman for men like you. I'm done with you!")
                    task_list[5] = ""
                    updateTaskList()
                elif mphone_chat_history_list[idx][4] == "4b":
                    mphone_chat_history_list[idx][2].append("This is fucking ridiculous; there's always another woman for men like you. I'm done with you!")
                    task_list[5] = ""
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
