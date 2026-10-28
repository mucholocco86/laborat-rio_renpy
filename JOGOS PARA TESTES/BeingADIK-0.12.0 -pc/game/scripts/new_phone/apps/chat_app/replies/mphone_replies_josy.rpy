init python:

    def mphone_chat_get_replies_josy(idx):
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
                    mphone_replies = ["So, the party started. When are you girls coming?","[m_c_text]You're missing out on so much fun already!",""]
                else:
                    mphone_replies = ["So, the party started. When are you girls coming?","You're missing out on so much fun already!",""]
                mphone_next_state = ["h2a","h2b",""]
            elif  mphone_chat_history_list[idx][4] == "2a":
                mphone_replies = ["I haven't seen any HOTs here.","Take your time. New people drop in by the minute, so no one is bored.",""]
                mphone_next_state = ["h3a","h3b",""]
            elif  mphone_chat_history_list[idx][4] == "2b":
                if persistent.mod_wtenabled:
                    mphone_replies = ["Did I say fun? I meant chores. Tommy's lack of work ethic is keeping me busy. mphone_emoji_sad","[m_c_text]It's fun watching guests arrive. People are very inventive with their costumes. Well, not everyone, but many.",""]
                else:
                    mphone_replies = ["Did I say fun? I meant chores. Tommy's lack of work ethic is keeping me busy. mphone_emoji_sad","It's fun watching guests arrive. People are very inventive with their costumes. Well, not everyone, but many.",""]
                mphone_next_state = ["h3c","h3d",""]
            elif  mphone_chat_history_list[idx][4] == "3a" or mphone_chat_history_list[idx][4] == "3b" or mphone_chat_history_list[idx][4] == "4a" or mphone_chat_history_list[idx][4] == "4b" or mphone_chat_history_list[idx][4] == "4c":
                if persistent.mod_wtenabled:
                    mphone_replies = ["I'll let you get back to putting on your costume. We'll talk soon.","[m_c_text]Can't wait to see you tonight. Good luck with the costume! mphone_emoji_kiss",""]
                else:
                    mphone_replies = ["I'll let you get back to putting on your costume. We'll talk soon.","Can't wait to see you tonight. Good luck with the costume! mphone_emoji_kiss",""]
                mphone_next_state = ["h5a","h5b",""]
            elif  mphone_chat_history_list[idx][4] == "3c":
                mphone_replies = ["I know. But the things he's making me do need to be done. I'm kind of hoping he'll wake up and feel guilty for not helping out at some point.","You once told me it was hell living with him, I don't want it to be like that while I'm living here. I think it's better to play along.",""]
                mphone_next_state = ["h4a","h4b",""]
            elif  mphone_chat_history_list[idx][4] == "3d":
                mphone_replies = ["Some people came dressed alike, but you two are unique so far.","",""]
                mphone_next_state = ["h4c","",""]
            else:
                
                mphone_replies = ["","",""]
                mphone_next_state = ["","",""]
                mphone_contact_list[idx][2] = False
        return


    def mphone_chat_them_replies_josy(idx):
        global mphone_replies
        global mphone_contact_list
        global mphone_next_state
        global mphone_chat_history_list
        global mphone_contact_list
        global optional_task_list
        global task_list
        global RPjosy
        if len(mphone_chat_history_list[idx][4]) == 0:
            return
        
        if mphone_chat_history_list[idx][4][0] == "h":
            mphone_chat_history_list[idx][3].append(True)
            mphone_chat_history_list[idx][4] = mphone_chat_history_list[idx][4][1:]
            if mphone_chat_history_list[idx][5] == 1:
                if mphone_chat_history_list[idx][4] == "2a":
                    mphone_chat_history_list[idx][2].append("I'm almost ready, but some aren't, and I think a few have already left. We won't take too long.")
                elif mphone_chat_history_list[idx][4] == "2b":
                    mphone_chat_history_list[idx][2].append("We are? Like what?")
                elif mphone_chat_history_list[idx][4] == "3a":
                    mphone_chat_history_list[idx][2].append("I'm sure I saw Arieth and Ashley leave somewhere. Oh well.")
                elif mphone_chat_history_list[idx][4] == "3b":
                    mphone_chat_history_list[idx][2].append("It sounds like there won't be a shortage of guests. mphone_emoji_smile")
                elif mphone_chat_history_list[idx][4] == "3c":
                    mphone_chat_history_list[idx][2].append("You do know how to fight that, don't you? If you go along with everything he says, he's gonna end up using you. Tell him no or ignore him. Trust me, that works.")
                elif mphone_chat_history_list[idx][4] == "3d":
                    mphone_chat_history_list[idx][2].append("No one came dressed as Maya and me, right?")
                elif mphone_chat_history_list[idx][4] == "4a":
                    mphone_chat_history_list[idx][2].append("To me, that sounds like a fool's errand. Don't forget to put yourself first sometimes. mphone_emoji_kiss")
                elif mphone_chat_history_list[idx][4] == "4b":
                    mphone_chat_history_list[idx][2].append("I get your point. Good luck with that!")
                    mphone_chat_history_list[idx][3].append(True)
                    mphone_chat_history_list[idx][2].append("Maybe that came off as sarcastic? I didn't mean it that way. mphone_emoji_kiss")
                elif mphone_chat_history_list[idx][4] == "4c":
                    mphone_chat_history_list[idx][2].append("That's good!")
                elif mphone_chat_history_list[idx][4] == "5a":
                    mphone_chat_history_list[idx][2].append("mphone_emoji_smile")
                    optional_task_list[1] = ""
                elif mphone_chat_history_list[idx][4] == "5b":
                    mphone_chat_history_list[idx][2].append("Can't wait to see you as well. mphone_emoji_kiss")
                    RPjosy += 1
                    optional_task_list[1] = ""
                elif mphone_chat_history_list[idx][4] == " ":
                    mphone_replies = ["","",""]
                    mphone_next_state = ["","",""]
                    mphone_contact_list[idx][2] = False
        
        
        elif mphone_chat_history_list[idx][4] == " ":
            mphone_replies = ["","",""]
            mphone_next_state = ["","",""]
            mphone_contact_list[idx][2] = False
        return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
