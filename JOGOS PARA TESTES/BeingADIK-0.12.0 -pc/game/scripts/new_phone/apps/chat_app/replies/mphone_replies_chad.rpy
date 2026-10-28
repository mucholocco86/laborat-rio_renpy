init python:

    def mphone_chat_get_replies_chad(idx):
        global mphone_replies
        global mphone_contact_list
        global mphone_next_state
        global mphone_contact_list
        global mphone_chat_history_list
        global ep3_intervenedChad
        
        if len(mphone_chat_history_list[idx][4]) == 0:
            return
        
        if mphone_chat_history_list[idx][5] == 1:
            if  mphone_chat_history_list[idx][4] == "1":
                mphone_replies = ["Hey, Chad. It's [name]. I need to ask you something private, but I don't want to do it over the phone. Can we meet up?","",""]
                mphone_next_state = ["h2a","",""]
            elif  mphone_chat_history_list[idx][4] == "2a":
                mphone_replies = ["It's about our frats. Someone is framing me and the DIKs for something we didn't do. I talked to Anthony about it earlier, and he said you accused me of doing something I never did. It has got something to do with some pictures someone sent you.","",""]
                mphone_next_state = ["h3a","",""]
            elif  mphone_chat_history_list[idx][4] == "3a":
                mphone_replies = ["Is that why you attacked me? Because if it is, we need to talk. I had nothing to do with those pictures, whatever they were.","",""]
                mphone_next_state = ["h4a","",""]
            elif  mphone_chat_history_list[idx][4] == "4a":
                mphone_replies = ["I'm not bullshitting you. I have no beef with you. I wanna find out why I'm getting blamed for something I didn't do. Let's talk about it. Please? 5 minutes is all I ask for.","",""]
                mphone_next_state = ["h5a","",""]
            elif  mphone_chat_history_list[idx][4] == "5a":
                mphone_replies = ["Then meet me at a place where none of your friends will show.","",""]
                mphone_next_state = ["h6a","",""]
            elif  mphone_chat_history_list[idx][4] == "6a":
                mphone_replies = ["Thank you. I'll be there.","",""]
                mphone_next_state = ["h7a","",""]
            else:
                
                mphone_replies = ["","",""]
                mphone_next_state = ["","",""]
                mphone_contact_list[idx][2] = False
        elif mphone_chat_history_list[idx][5] == 2:
            if  mphone_chat_history_list[idx][4] == "1":
                mphone_replies = ["We knew Caleb did it, but not Darius.","",""]
                mphone_next_state = ["h2a","",""]
            elif  mphone_chat_history_list[idx][4] == "2a":
                mphone_replies = ["Ok. Did they spare Nick's room for a reason?","",""]
                mphone_next_state = ["h3a","",""]
            elif  mphone_chat_history_list[idx][4] == "3a":
                mphone_replies = ["Ok. That's interesting...","",""]
                mphone_next_state = ["h4a","",""]
            elif  mphone_chat_history_list[idx][4] == "4a":
                mphone_replies = ["I think it proved that there wasn't a reason why Nick's room wasn't as trashed as the rest. And probably that it had nothing to do with the letters...","",""]
                mphone_next_state = ["h5a","",""]
            else:
                
                mphone_replies = ["","",""]
                mphone_next_state = ["","",""]
                mphone_contact_list[idx][2] = False
        return


    def mphone_chat_them_replies_chad(idx):
        global mphone_replies
        global mphone_contact_list
        global mphone_next_state
        global mphone_chat_history_list
        global mphone_contact_list
        global task_list
        global ep3_intervenedChad
        
        if len(mphone_chat_history_list[idx][4]) == 0:
            return
        if mphone_chat_history_list[idx][4][0] == "h":
            mphone_chat_history_list[idx][3].append(True)
            mphone_chat_history_list[idx][4] = mphone_chat_history_list[idx][4][1:]
            if mphone_chat_history_list[idx][5] == 1:
                if mphone_chat_history_list[idx][4] == "2a":
                    if ep3_intervenedChad:
                        mphone_chat_history_list[idx][2].append("What is it about?")
                    else:
                        mphone_chat_history_list[idx][2].append("?")
                elif mphone_chat_history_list[idx][4] == "3a":
                    mphone_chat_history_list[idx][2].append("I don't know what you're talking about.")
                elif mphone_chat_history_list[idx][4] == "4a":
                    mphone_chat_history_list[idx][2].append("Stop bullshitting me. I told you what I'd do if you threatened me again.")
                elif mphone_chat_history_list[idx][4] == "5a":
                    mphone_chat_history_list[idx][2].append("I don't want to be seen talking to you.")
                elif mphone_chat_history_list[idx][4] == "6a":
                    mphone_chat_history_list[idx][2].append("I've got gym, then class. Meet me in the library at 6 p.m.")
                elif mphone_chat_history_list[idx][4] == "7a":
                    task_list[0] = ""
                    updateTaskList()
                    mphone_chat_history_list[idx][2].append("Come alone and be on time. I'm not going to stick around and wait.")
            elif mphone_chat_history_list[idx][5] == 2:
                if mphone_chat_history_list[idx][4] == "1":
                    mphone_chat_history_list[idx][2].append("I asked Ant and Alex about what you wanted to know. They said it was Caleb and Darius who trashed the mansion.")
                elif mphone_chat_history_list[idx][4] == "2a":
                    mphone_chat_history_list[idx][2].append("It was Dawe's idea. Caleb and Darius weren't tri-alphas at the time. Dawe planned to use that to get out of trouble for trashing your place. Dawe was scared of the consequences after I got kicked out of the frat. They even kept Caleb as a pledge for a while in case they needed to do it again.")
                elif mphone_chat_history_list[idx][4] == "3a":
                    mphone_chat_history_list[idx][2].append("They didn't seem to know or care about which room was whose. Dawe and the rest told them what to do. Alex and Jimmy kept a lookout for you guys, and when you returned, they got out of there. They were almost finished by then, anyway.")
                elif mphone_chat_history_list[idx][4] == "4a":
                    mphone_chat_history_list[idx][2].append("I dunno if that helped you, but that's all I know.")
                elif mphone_chat_history_list[idx][4] == "5a":
                    mphone_chat_history_list[idx][2].append("You didn't hear this from me.")
                    task_list[3] = ""
                    updateTaskList()
        elif mphone_chat_history_list[idx][4][0] == " ":
            mphone_replies = ["","",""]
            mphone_next_state = ["","",""]
            mphone_contact_list[idx][2] = False
        return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
