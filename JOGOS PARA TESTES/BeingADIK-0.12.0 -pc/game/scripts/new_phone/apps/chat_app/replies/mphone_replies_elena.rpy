init python:

    def mphone_chat_get_replies_elena(idx):
        global mphone_replies
        global mphone_contact_list
        global mphone_next_state
        global mphone_contact_list
        global mphone_chat_history_list
        global ep10_shroom_choice
        global branchAlone
        global ep10_jb_elena_hot
        
        if len(mphone_chat_history_list[idx][4]) == 0:
            return
        
        if mphone_chat_history_list[idx][5] == 1:
            if  mphone_chat_history_list[idx][4] == "1":
                mphone_replies = ["We're definitely missing you girls here. Without you, it feels like the party hasn't started yet.","Maybe I'll do that. But don't blame me if the photos come out looking like shit.",""]
                mphone_next_state = ["h2a","h2b",""]
            elif  mphone_chat_history_list[idx][4] == "2a":
                mphone_replies = ["An hour for makeup? That's crazy.","See you soonish, then! mphone_emoji_smile",""]
                mphone_next_state = ["h3a","h3b",""]
            elif  mphone_chat_history_list[idx][4] == "2b":
                mphone_replies = ["Thanks! I got it. See you soon!","",""]
                mphone_next_state = ["h3c","",""]
            else:
                
                mphone_replies = ["","",""]
                mphone_next_state = ["","",""]
                mphone_contact_list[idx][2] = False
        elif mphone_chat_history_list[idx][5] == 2:
            if  mphone_chat_history_list[idx][4] == "1":
                mphone_replies = ["Thanks! Downloading them and praying that I look good. mphone_emoji_cool","Awesome! Great job. I can't wait to see how they came out looking. Downloading them now. mphone_emoji_smile",""]
                mphone_next_state = ["h2a","h2b",""]
            else:
                
                mphone_replies = ["","",""]
                mphone_next_state = ["","",""]
                mphone_contact_list[idx][2] = False
        elif mphone_chat_history_list[idx][5] == 3:
            if mphone_chat_history_list[idx][4] == "1":
                mphone_replies = ["Happy Thanksgiving to you too! I meant to talk to you last night, but the night was over too fast. I hope you girls had fun. mphone_emoji_smile","Right back at you! I hope you didn't spend all night taking care of JB.",""]
                mphone_next_state = ["h2a","h2b",""]
            elif mphone_chat_history_list[idx][4] == "2a":
                mphone_replies = ["Oh? Did something happen? You can trust me if you want to talk about it.","That's a shame. I hope it turned out well, whatever it was.",""]
                mphone_next_state = ["h3a","h3b",""]
            elif mphone_chat_history_list[idx][4] == "2b":
                if ep10_shroom_choice == "DIK":
                    mphone_replies = ["Did I do something to you? I don't have the faintest idea what you mean by that. mphone_emoji_surprised","Fuck... What did I do now? I bet it was something stupid. mphone_emoji_laugh",""]
                    mphone_next_state = ["h3c","h3d",""]
                else:
                    mphone_replies = ["Heather? Why? She didn't even seem drunk to me.","That's nice of you. mphone_emoji_smile",""]
                    mphone_next_state = ["h3e","h3f",""]
            elif mphone_chat_history_list[idx][4] == "3a" or mphone_chat_history_list[idx][4] == "3b" or mphone_chat_history_list[idx][4] == "3e" or mphone_chat_history_list[idx][4] == "3f" or mphone_chat_history_list[idx][4] == "4c" or mphone_chat_history_list[idx][4] == "4d" or mphone_chat_history_list[idx][4] == "4e":
                mphone_replies = ["Yeah, that... I'm not gonna lie. That made me feel uncomfortable.","You don't have to apologize for him. He wasn't himself when he said it.",""]
                mphone_next_state = ["h4a","h4b",""]
            elif mphone_chat_history_list[idx][4] == "3c" or mphone_chat_history_list[idx][4] == "3d":
                mphone_replies = ["Well, were you a lollipop?","Sorry, but I don't remember that.","I like to lick things."]
                mphone_next_state = ["h4c","h4d","h4e"]
            elif mphone_chat_history_list[idx][4] == "4a" or mphone_chat_history_list[idx][4] == "4b":
                if branchAlone and ep10_jb_elena_hot:
                    if persistent.mod_wt_enabled:
                        mphone_replies = ["There's nothing to apologize for, trust me. mphone_emoji_smile","Thanks, Elena. Don't worry about it. We're cool. mphone_emoji_cool","[m_c_text]Honestly, I was weirdly flattered and a bit interested in doing that. But maybe you're right about it getting awkward if we did that together. Hot as you are, I value our friendship even more than having sex with you. Besides, I'd probably ruin him for you.  mphone_emoji_cool"]
                    else:
                        mphone_replies = ["There's nothing to apologize for, trust me. mphone_emoji_smile","Thanks, Elena. Don't worry about it. We're cool. mphone_emoji_cool","Honestly, I was weirdly flattered and a bit interested in doing that. But maybe you're right about it getting awkward if we did that together. Hot as you are, I value our friendship even more than having sex with you. Besides, I'd probably ruin him for you.  mphone_emoji_cool"]
                    
                    mphone_next_state = ["h6a","h6b","h6c"]
                else:
                    mphone_replies = ["There's nothing to apologize for, trust me. mphone_emoji_smile","Thanks, Elena. Don't worry about it. We're cool. mphone_emoji_cool",""]
                    mphone_next_state = ["h6a","h6b",""]
            elif mphone_chat_history_list[idx][4] == "6c":
                if persistent.mod_wt_enabled:
                    mphone_replies = ["Huh? Who's talking about me like that?","[m_c_text]Like I told JB, I think you're hot, but I wouldn't fuck you since you're his girl. Then he said there's a way around it...but I don't know.",""]
                else:
                    mphone_replies = ["Huh? Who's talking about me like that?","Like I told JB, I think you're hot, but I wouldn't fuck you since you're his girl. Then he said there's a way around it...but I don't know.",""]
                mphone_next_state = ["h7a","h7b",""]
            elif mphone_chat_history_list[idx][4] == "7a" or mphone_chat_history_list[idx][4] == "7b":
                mphone_replies = ["You too. mphone_emoji_kiss","",""]
                mphone_next_state = [" ","",""]
            else:
                
                mphone_replies = ["","",""]
                mphone_next_state = ["","",""]
                mphone_contact_list[idx][2] = False
        elif mphone_chat_history_list[idx][5] == 4:
            if  mphone_chat_history_list[idx][4] == "1":
                mphone_replies = ["I woke up the day after, and it felt like some bizarre dream. Like, did that actually happen? I had to think about it for a long time before I realized it was real. It's a weird feeling, but I'm more concerned about how you and John Boy are doing.","",""]
                mphone_next_state = ["h2a","",""]
            elif  mphone_chat_history_list[idx][4] == "2a":
                mphone_replies = ["You don't have to worry about me as long as you're ok. We did something fun together; that's how I look at it.","I don't feel different about it, but I'd appreciate it if this could stay between us three.",""]
                mphone_next_state = ["h3a","h3b",""]
            else:
                
                mphone_replies = ["","",""]
                mphone_next_state = ["","",""]
                mphone_contact_list[idx][2] = False
        return


    def mphone_chat_them_replies_elena(idx):
        global mphone_replies
        global mphone_contact_list
        global mphone_next_state
        global mphone_chat_history_list
        global mphone_contact_list
        global ep10_shroom_choice
        global branchIsabella
        global branchMayaJosy
        global branchSage
        global branchAlone
        global branchJill
        global task_list
        global ep10_elena_offer
        if len(mphone_chat_history_list[idx][4]) == 0:
            return
        
        if mphone_chat_history_list[idx][4][0] == "h":
            mphone_chat_history_list[idx][3].append(True)
            mphone_chat_history_list[idx][4] = mphone_chat_history_list[idx][4][1:]
            if mphone_chat_history_list[idx][5] == 1:
                if mphone_chat_history_list[idx][4] == "1":
                    mphone_chat_history_list[idx][2].append("[name]! We're running a bit late. Girls and makeup, you know the deal. If you want to start snapping pictures of the guests, go ahead.")
                elif mphone_chat_history_list[idx][4] == "2a":
                    mphone_chat_history_list[idx][2].append("Haha! I bet! I'm already done with my costume, but the others aren't. Riona's been in front of the mirror for at least an hour now. mphone_emoji_laugh")
                elif mphone_chat_history_list[idx][4] == "2b":
                    mphone_chat_history_list[idx][2].append("The photos will come out great if you don't move the camera. Just turn the camera on, press that button I showed you, and you'll be fine. The timer should be set already too.")
                elif mphone_chat_history_list[idx][4] == "3a":
                    mphone_chat_history_list[idx][2].append("Yeah, I never understood it either. See you guys in a bit! Party hard for us until then.")
                elif mphone_chat_history_list[idx][4] == "3b":
                    mphone_chat_history_list[idx][2].append("You know it!")
                elif mphone_chat_history_list[idx][4] == "3c":
                    mphone_chat_history_list[idx][2].append("Party hard!")
                elif mphone_chat_history_list[idx][4][0] == " ":
                    mphone_replies = ["","",""]
                    mphone_next_state = ["","",""]
                    mphone_contact_list[idx][2] = False
            elif mphone_chat_history_list[idx][5] == 2:
                if mphone_chat_history_list[idx][4] == "1":
                    mphone_chat_history_list[idx][2].append("Sup, everyone! I'm sending everyone the same text to let you all know that the Halloween pictures are done! Jacob's been doing some magic to them with a little bit of my assistance. You can download the pictures {color=00b0ff}here{/color}.")
                elif mphone_chat_history_list[idx][4] == "2a":
                    task_list[3] = ""
                    updateTaskList()
                    mgallery_init_album()
                    mphone_chat_history_list[idx][2].append("You always do, love.")
                elif mphone_chat_history_list[idx][4] == "2b":
                    task_list[3] = ""
                    updateTaskList()
                    mgallery_init_album()
                    mphone_chat_history_list[idx][2].append("Some of them are hilarious! mphone_emoji_laugh")
            elif mphone_chat_history_list[idx][5] == 3:
                if mphone_chat_history_list[idx][4] == "1":
                    mphone_chat_history_list[idx][2].append("Happy Thanksgiving, [name]! Thanks for last night. You worked your butt off as usual, huh? mphone_emoji_kiss")
                elif mphone_chat_history_list[idx][4] == "2a":
                    if ep10_shroom_choice == "DIK":
                        mphone_chat_history_list[idx][2].append("I bet it was over fast for you. Haha, you were fucked up. For me, it was so-so. I can't really talk about it, but I didn't get into party mode because of it.")
                    else:
                        mphone_chat_history_list[idx][2].append("Right? Actually, it was so-so. I can't really talk about it, but I didn't get into party mode because of it.")
                elif mphone_chat_history_list[idx][4] == "2b":
                    if ep10_shroom_choice == "DIK":
                        mphone_chat_history_list[idx][2].append("He was easy compared to you. Do you even remember what you did to me? mphone_emoji_laugh")
                    else:
                        mphone_chat_history_list[idx][2].append("No, but I did spend the night taking care of Heather.")
                elif mphone_chat_history_list[idx][4] == "3a":
                    mphone_chat_history_list[idx][2].append("I know I can, but I don't want to betray her trust. mphone_emoji_heart")
                    mphone_chat_history_list[idx][3].append(True)
                    mphone_chat_history_list[idx][2].append("By the way, I feel like I have to apologize to you. John Boy told me he talked to you about something last night. Involving you and us, I believe...")
                elif mphone_chat_history_list[idx][4] == "3b":
                    mphone_chat_history_list[idx][2].append("It will. mphone_emoji_smile")
                    mphone_chat_history_list[idx][3].append(True)
                    mphone_chat_history_list[idx][2].append("By the way, I feel like I have to apologize to you. John Boy told me he talked to you about something last night. Involving you and us, I believe...")
                elif mphone_chat_history_list[idx][4] == "3c":
                    mphone_chat_history_list[idx][2].append("You tongued my cheek hard, thinking I was a lollipop. mphone_emoji_tongue mphone_emoji_laugh")
                elif mphone_chat_history_list[idx][4] == "3d":
                    mphone_chat_history_list[idx][2].append("You bet your cute butt it was stupid. You tongued my cheek hard, thinking I was a lollipop. mphone_emoji_tongue mphone_emoji_laugh")
                elif mphone_chat_history_list[idx][4] == "3e":
                    mphone_chat_history_list[idx][2].append("She wasn't drunk. She's dealing with some stuff right now. But don't worry about it.")
                    mphone_chat_history_list[idx][3].append(True)
                    mphone_chat_history_list[idx][2].append("By the way, I feel like I have to apologize to you. John Boy told me he talked to you about something last night. Involving you and us, I believe...")
                elif mphone_chat_history_list[idx][4] == "3f":
                    mphone_chat_history_list[idx][2].append("By the way, I feel like I have to apologize to you. John Boy told me he talked to you about something last night. Involving you and us, I believe...")
                elif mphone_chat_history_list[idx][4] == "4c":
                    mphone_chat_history_list[idx][2].append("No, [name]. I'm not a lollipop. But I can't deny that I taste great! mphone_emoji_laugh")
                    mphone_chat_history_list[idx][3].append(True)
                    mphone_chat_history_list[idx][2].append("By the way, I feel like I have to apologize to you. John Boy told me he talked to you about something last night. Involving you and us, I believe...")
                elif mphone_chat_history_list[idx][4] == "4d":
                    mphone_chat_history_list[idx][2].append("It's ok, [name]. I thought it was funny. mphone_emoji_laugh")
                    mphone_chat_history_list[idx][3].append(True)
                    mphone_chat_history_list[idx][2].append("By the way, I feel like I have to apologize to you. John Boy told me he talked to you about something last night. Involving you and us, I believe...")
                elif mphone_chat_history_list[idx][4] == "4e":
                    mphone_chat_history_list[idx][2].append("Haha! Well, that's honest. mphone_emoji_laugh")
                    mphone_chat_history_list[idx][3].append(True)
                    mphone_chat_history_list[idx][2].append("By the way, I feel like I have to apologize to you. John Boy told me he talked to you about something last night. Involving you and us, I believe...")
                elif mphone_chat_history_list[idx][4] == "4a" or mphone_chat_history_list[idx][4] == "4b":
                    if branchAlone:
                        mphone_chat_history_list[idx][2].append("He mentioned it to me before, and once again after he saw how you and I got closer as friends. But I always told him no because you're my friend, and I don't want things to get awkward between us. Anyway, I wanted to apologize if he embarrassed you somehow.")
                    elif branchIsabella or branchMayaJosy:
                        mphone_chat_history_list[idx][2].append("He mentioned it to me before, and once again after he saw how you and I got closer as friends. But I always told him no because you're my friend, and I don't want things to get awkward between us. And I'm not quite sure if you're available or not. Anyway, I wanted to apologize if he embarrassed you somehow.")
                    else:
                        mphone_chat_history_list[idx][2].append("He mentioned it to me before, and once again after he saw how you and I got closer as friends. But I always told him no because you're my friend, and I don't want things to get awkward between us. And I know you're not available, too. Anyway, I wanted to apologize if he embarrassed you somehow.")
                elif mphone_chat_history_list[idx][4] == "6a" or mphone_chat_history_list[idx][4] == "6b":
                    mphone_chat_history_list[idx][2].append("Awesome! Have a great day, [name]. See you sometime after the weekend. mphone_emoji_kiss")
                    task_list[0] = ""
                    updateTaskList()
                elif mphone_chat_history_list[idx][4] == "6c":
                    mphone_chat_history_list[idx][2].append("HAHA! I don't think you would ruin him for me. A big dick isn't all a girl wants in a man, you know? And I value our friendship highly, too, and honestly, I didn't think you'd even want to have sex with me. Especially after hearing how some pretty hot girls started to talk about you, I figured that competition sealed the deal.")
                elif mphone_chat_history_list[idx][4] == "7a":
                    mphone_chat_history_list[idx][2].append("Let's just say they are girls who figured out it was you on that poster. Anyway, let's continue this conversation another time. Have a great day, [name]. See you sometime after the weekend. mphone_emoji_kiss")
                    ep10_elena_offer = True
                    task_list[0] = ""
                    updateTaskList()
                elif mphone_chat_history_list[idx][4] == "7b":
                    mphone_chat_history_list[idx][2].append("I don't know, either. This isn't what I thought this conversation would lead to. Let's continue it another time, ok? Have a great day, [name]. See you sometime after the weekend. mphone_emoji_kiss")
                    ep10_elena_offer = True
                    task_list[0] = ""
                    updateTaskList()
            elif mphone_chat_history_list[idx][5] == 4:
                if mphone_chat_history_list[idx][4] == "1":
                    mphone_chat_history_list[idx][2].append("I wanted to check in on you to make sure things aren't weird after the party. mphone_emoji_smile")
                elif mphone_chat_history_list[idx][4] == "2a":
                    mphone_chat_history_list[idx][2].append("It was the same for us. John Boy couldn't stop talking about it. You should have seen him; he was so excited that it had happened. And I was like you - \"Did that really happen!?\" I felt good that I made him happy, but it was weird not knowing how you felt after. It's one thing to do something when you're drunk at a party, but the day after, you could feel different.")
                elif mphone_chat_history_list[idx][4] == "3a":
                    task_list[2] = ""
                    updateTaskList()
                    mphone_chat_history_list[idx][2].append("Then I'm relieved. mphone_emoji_laugh")
                elif mphone_chat_history_list[idx][4] == "3b":
                    task_list[2] = ""
                    updateTaskList()
                    mphone_chat_history_list[idx][2].append("Naturally. That's what I told John Boy. I'm relieved you feel good. mphone_emoji_smile")
        
        elif mphone_chat_history_list[idx][4][0] == " ":
            mphone_replies = ["","",""]
            mphone_next_state = ["","",""]
            mphone_contact_list[idx][2] = False
        return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
