init python:
    def new_chat_msg(who,isThem,whichChat):
        global mphone_chat_history_list
        global mphone_contact_list
        
        for x in range(0,len(mphone_chat_history_list)):
            if mphone_chat_history_list[x][0] == who:
                mphone_chat_history_list[x][1] = len(mphone_chat_history_list[x][2])
                if isThem:
                    mphone_chat_history_list[x][4] = "h1"
                else:
                    mphone_chat_history_list[x][4] = "1"
                mphone_chat_history_list[x][5] = whichChat
                mphone_contact_list[x][2] = True
        return

    def mphone_get_chat_str(s):
        global mphones_emotes
        global mphone_chat_history_list
        str = s
        for i in mphones_emotes:
            if i[0] in str:
                i[1] = True
                str = str.replace(i[0],"")
            else:
                i[1] = False
        return str

    def mphone_mc_replies(idx,i):
        global mphone_chat_history_list
        global mphone_replies
        global mphone_next_state
        if len(mphone_replies[i])==0 or len(mphone_next_state[i])==0:
            return
        mphone_chat_history_list[idx][2].append(mphone_replies[i])
        mphone_chat_history_list[idx][3].append(False)
        mphone_chat_history_list[idx][4] = mphone_next_state[i]
        renpy.restart_interaction()
        return

    def mphone_chat_handle_replies(idx):
        global mphone_chat_history_list
        if mphone_chat_history_list[idx][0] == "Dad":
            mphone_chat_them_replies_dad(idx)
            mphone_chat_get_replies_dad(idx)
        elif mphone_chat_history_list[idx][0] == "Camila":
            mphone_chat_them_replies_camila(idx)
            mphone_chat_get_replies_camila(idx)
        elif mphone_chat_history_list[idx][0] == "Chad":
            mphone_chat_them_replies_chad(idx)
            mphone_chat_get_replies_chad(idx)
        elif mphone_chat_history_list[idx][0] == "Derek":
            mphone_chat_them_replies_derek(idx)
            mphone_chat_get_replies_derek(idx)
        elif mphone_chat_history_list[idx][0] == "Elena":
            mphone_chat_them_replies_elena(idx)
            mphone_chat_get_replies_elena(idx)
        elif mphone_chat_history_list[idx][0] == "Heather":
            mphone_chat_them_replies_heather(idx)
            mphone_chat_get_replies_heather(idx)
        elif mphone_chat_history_list[idx][0] == "Isabella":
            mphone_chat_them_replies_isabella(idx)
            mphone_chat_get_replies_isabella(idx)
        elif mphone_chat_history_list[idx][0] == "Jacob":
            mphone_chat_them_replies_jacob(idx)
            mphone_chat_get_replies_jacob(idx)
        elif mphone_chat_history_list[idx][0] == "Jade":
            mphone_chat_them_replies_jade(idx)
            mphone_chat_get_replies_jade(idx)
        elif mphone_chat_history_list[idx][0] == "Jamie":
            mphone_chat_them_replies_jamie(idx)
            mphone_chat_get_replies_jamie(idx)
        elif mphone_chat_history_list[idx][0] == "Jill":
            mphone_chat_them_replies_jill(idx)
            mphone_chat_get_replies_jill(idx)
        elif mphone_chat_history_list[idx][0] == "John Boy":
            mphone_chat_them_replies_johnboy(idx)
            mphone_chat_get_replies_johnboy(idx)
        elif mphone_chat_history_list[idx][0] == "Josy":
            mphone_chat_them_replies_josy(idx)
            mphone_chat_get_replies_josy(idx)
        elif mphone_chat_history_list[idx][0] == "Leon":
            mphone_chat_them_replies_leon(idx)
            mphone_chat_get_replies_leon(idx)
        elif mphone_chat_history_list[idx][0] == "Lily":
            mphone_chat_them_replies_lily(idx)
            mphone_chat_get_replies_lily(idx)
        elif mphone_chat_history_list[idx][0] == "Madame Rose":
            mphone_chat_them_replies_madame_rose(idx)
            mphone_chat_get_replies_madame_rose(idx)
        elif mphone_chat_history_list[idx][0] == "Magnar":
            mphone_chat_them_replies_magnar(idx)
            mphone_chat_get_replies_magnar(idx)
        elif mphone_chat_history_list[idx][0] == "Maya":
            mphone_chat_them_replies_maya(idx)
            mphone_chat_get_replies_maya(idx)
        elif mphone_chat_history_list[idx][0] == "Melanie":
            mphone_chat_them_replies_melanie(idx)
            mphone_chat_get_replies_melanie(idx)
        elif mphone_chat_history_list[idx][0] == "Nick":
            mphone_chat_them_replies_nick(idx)
            mphone_chat_get_replies_nick(idx)
        elif mphone_chat_history_list[idx][0] == "Nicole":
            mphone_chat_them_replies_nicole(idx)
            mphone_chat_get_replies_nicole(idx)
        elif mphone_chat_history_list[idx][0] == "Nora":
            mphone_chat_them_replies_nora(idx)
            mphone_chat_get_replies_nora(idx)
        elif mphone_chat_history_list[idx][0] == "Quinn":
            mphone_chat_them_replies_quinn(idx)
            mphone_chat_get_replies_quinn(idx)
        elif mphone_chat_history_list[idx][0] == "Riona":
            mphone_chat_them_replies_riona(idx)
            mphone_chat_get_replies_riona(idx)
        elif mphone_chat_history_list[idx][0] == "Rusty":
            mphone_chat_them_replies_rusty(idx)
            mphone_chat_get_replies_rusty(idx)
        elif mphone_chat_history_list[idx][0] == "Sage":
            mphone_chat_them_replies_sage(idx)
            mphone_chat_get_replies_sage(idx)
        elif mphone_chat_history_list[idx][0] == "Sally":
            mphone_chat_them_replies_sally(idx)
            mphone_chat_get_replies_sally(idx)
        elif mphone_chat_history_list[idx][0] == "Sarah":
            mphone_chat_them_replies_sarah(idx)
            mphone_chat_get_replies_sarah(idx)
        elif mphone_chat_history_list[idx][0] == "Tommy":
            mphone_chat_them_replies_tommy(idx)
            mphone_chat_get_replies_tommy(idx)
        elif mphone_chat_history_list[idx][0] == "Zoey":
            mphone_chat_them_replies_zoey(idx)
            mphone_chat_get_replies_zoey(idx)
        return

    def mphone_scene_to_chat(who, list):
        global mphone_chat_history_list
        
        for x in range(0,len(mphone_chat_history_list)):
            if mphone_chat_history_list[x][0] == who:
                for i in list:
                    mphone_chat_history_list[x][2].append(i[1])
                    mphone_chat_history_list[x][3].append(i[2])
                return
        return

    def fixChatLists():
        global mphone_chat_history_list
        tmpBool = False
        for i in mphone_chat_history_list:
            if len(i[2])<len(i[3]):
                tmpBool = True
                i[3].pop()
        if tmpBool:
            fixChatLists()
        return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
