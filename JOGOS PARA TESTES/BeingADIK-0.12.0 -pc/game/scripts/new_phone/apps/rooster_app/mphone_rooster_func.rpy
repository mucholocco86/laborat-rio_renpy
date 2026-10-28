init python:
    def mphone_rooster_clear():
        global mroosterChoices
        for x in mroosterChoices:
            if x[0] == 0:
                x[0] = -1
        return

    def get_rooster_nick(who):
        global roosterNickMC
        global rooster_nick_list
        for x in rooster_nick_list:
            if x[0].lower().replace(" ","") == who.lower().replace(" ",""):
                return x[1]
        return roosterNickMC

    def add_new_rooster_post(who, what, likes, picture, reply_function):
        global mroosterLikesArray
        global mroosterLikedArray
        global mroosterAvatarArray
        global mroosterNickArray
        global mroosterTextArray
        global mroosterPhotoArray
        global mroosterCommentSectionArray
        global mroosterPostsArray
        global mroosterHistory_avatars
        global mroosterHistory_nicknames
        global mroosterHistory_likes
        global mroosterHistory_liked
        global mroosterHistory_text
        global mroosterChoices
        
        mroosterLikesArray.insert(0,likes)
        mroosterLikedArray.insert(0,False)
        if who == "mc":
            mroosterAvatarArray.insert(0,mc_avatar)
        else:
            mroosterAvatarArray.insert(0,"rooster_mini_" + who)
        mroosterTextArray.insert(0,what)
        mroosterPhotoArray.insert(0,picture)
        mroosterCommentSectionArray.insert(0,reply_function)
        mroosterNickArray.insert(0,get_rooster_nick(who))
        mroosterPostsArray.insert(0,0)
        mroosterHistory_avatars.insert(0,[])
        mroosterHistory_nicknames.insert(0,[])
        mroosterHistory_likes.insert(0,[])
        mroosterHistory_liked.insert(0,[])
        mroosterHistory_text.insert(0,[])
        mroosterChoices.insert(0,[0])
        return

    def add_rooster_comment(who, what, likes):
        global mroosterPostsArray
        global mroosterHistory_avatars
        global mroosterHistory_nicknames
        global mroosterHistory_likes
        global mroosterHistory_liked
        global mroosterHistory_text
        
        mroosterPostsArray[0] += 1
        if who == "mc":
            mroosterHistory_avatars[0].append(mc_avatar)
        elif who == "tyballs":
            mroosterHistory_avatars[0].append("rooster_mini_alt")
        else:
            mroosterHistory_avatars[0].append("rooster_mini_" + who)
        mroosterHistory_nicknames[0].append(get_rooster_nick(who))
        mroosterHistory_likes[0].append(likes)
        mroosterHistory_liked[0].append(False)
        mroosterHistory_text[0].append(what)
        return

    def add_rooster_comment_response(idx, who, what, likes):
        global mroosterPostsArray
        global mroosterHistory_avatars
        global mroosterHistory_nicknames
        global mroosterHistory_likes
        global mroosterHistory_liked
        global mroosterHistory_text
        
        mroosterPostsArray[idx] += 1
        if who == "mc":
            mroosterHistory_avatars[idx].append(mc_avatar)
        elif who == "tyballs":
            mroosterHistory_avatars[idx].append("rooster_mini_alt")
        else:
            mroosterHistory_avatars[idx].append("rooster_mini_" + who)
        mroosterHistory_nicknames[idx].append(get_rooster_nick(who))
        mroosterHistory_likes[idx].append(likes)
        mroosterHistory_liked[idx].append(False)
        mroosterHistory_text[idx].append(what)
        return

    def add_rooster_choice(what):
        global mroosterChoices
        mroosterChoices[0].append(what)
        return

    def rooster_reply_func(idx):
        global mroosterCommentSectionArray
        if mroosterCommentSectionArray[idx] == "rooster_section_leon_ep7":
            rooster_append_reply_leon_ep7(idx)
            return
        elif mroosterCommentSectionArray[idx] == "rooster_section_derek_ep7":
            rooster_append_reply_derek_ep7(idx)
            return
        elif mroosterCommentSectionArray[idx] == "rooster_section_jimmy_ep7":
            rooster_append_reply_jimmy_ep7(idx)
            return
        elif mroosterCommentSectionArray[idx] == "rooster_section_ashley_ep7":
            rooster_append_reply_ashley_ep7(idx)
            return
        elif mroosterCommentSectionArray[idx] == "rooster_section_sage_ep7":
            rooster_append_reply_sage_ep7(idx)
            return
        elif mroosterCommentSectionArray[idx] == "rooster_section_isabella_ep7":
            rooster_append_reply_isabella_ep7(idx)
            return
        elif mroosterCommentSectionArray[idx] == "rooster_section_jill_ep7":
            rooster_append_reply_jill_ep7(idx)
            return
        elif mroosterCommentSectionArray[idx] == "rooster_section_mc_ep7":
            rooster_append_reply_mc_ep7(idx)
            return
        elif mroosterCommentSectionArray[idx] == "rooster_section_riona_ep7":
            rooster_append_reply_riona_ep7(idx)
            return
        elif mroosterCommentSectionArray[idx] == "rooster_section_josy_ep8":
            rooster_append_reply_josy_ep8(idx)
            return
        elif mroosterCommentSectionArray[idx] == "rooster_section_derek_ep8":
            rooster_append_reply_derek_ep8(idx)
            return
        elif mroosterCommentSectionArray[idx] == "rooster_section_lily_ep8":
            rooster_append_reply_lily_ep8(idx)
            return
        elif mroosterCommentSectionArray[idx] == "rooster_section_quinn_ep8":
            rooster_append_reply_quinn_ep8(idx)
            return
        elif mroosterCommentSectionArray[idx] == "rooster_section_jill_ep8":
            rooster_append_reply_jill_ep8(idx)
            return
        elif mroosterCommentSectionArray[idx] == "rooster_section_jamie2_ep8":
            rooster_append_reply_jamie2_ep8(idx)
            return
        elif mroosterCommentSectionArray[idx] == "rooster_section_mc_ep8":
            rooster_append_reply_mc_ep8(idx)
            return
        elif mroosterCommentSectionArray[idx] == "rooster_section_elena_ep9":
            rooster_append_reply_elena_ep9(idx)
            return
        elif mroosterCommentSectionArray[idx] == "rooster_section_jamie_ep9":
            rooster_append_reply_jamie_ep9(idx)
            return
        elif mroosterCommentSectionArray[idx] == "rooster_section_camila_ep9":
            rooster_append_reply_camila_ep9(idx)
            return
        elif mroosterCommentSectionArray[idx] == "rooster_section_karen_ep9":
            rooster_append_reply_karen_ep9(idx)
            return
        elif mroosterCommentSectionArray[idx] == "rooster_section_derek_ep10":
            rooster_append_reply_derek_ep10(idx)
            return
        elif mroosterCommentSectionArray[idx] == "rooster_section_leon_ep10":
            rooster_append_reply_leon_ep10(idx)
            return
        elif mroosterCommentSectionArray[idx] == "rooster_section_elena_ep10":
            rooster_append_reply_elena_ep10(idx)
            return
        elif mroosterCommentSectionArray[idx] == "rooster_section_mc_ep10":
            rooster_append_reply_mc_ep10(idx)
            return
        elif mroosterCommentSectionArray[idx] == "rooster_section_lily_ep10":
            rooster_append_reply_lily_ep10(idx)
            return
        elif mroosterCommentSectionArray[idx] == "rooster_section_jill_ep10":
            rooster_append_reply_jill_ep10(idx)
            return
        elif mroosterCommentSectionArray[idx] == "rooster_section_josy_ep11":
            rooster_append_reply_josy_ep11(idx)
            return
        elif mroosterCommentSectionArray[idx] == "rooster_section_lily_ep11":
            rooster_append_reply_lily_ep11(idx)
            return
        elif mroosterCommentSectionArray[idx] == "rooster_section_dany_ep11":
            rooster_append_reply_dany_ep11(idx)
            return
        elif mroosterCommentSectionArray[idx] == "rooster_section_bianca_ep11":
            rooster_append_reply_bianca_ep11(idx)
            return
        elif mroosterCommentSectionArray[idx] == "rooster_section_diks_ep11":
            rooster_append_reply_diks_ep11(idx)
            return
        elif mroosterCommentSectionArray[idx] == "rooster_section_mc_ep11":
            rooster_append_reply_mc_ep11(idx)
            return
        elif mroosterCommentSectionArray[idx] == "rooster_section_maya_ep11":
            rooster_append_reply_maya_ep11(idx)
            return
        elif mroosterCommentSectionArray[idx] == "rooster_section_diks_ep12":
            rooster_append_reply_diks_ep12(idx)
            return
        elif mroosterCommentSectionArray[idx] == "rooster_section_dany_ep12":
            rooster_append_reply_dany_ep12(idx)
            return
        elif mroosterCommentSectionArray[idx] == "rooster_section_tiffani_ep12":
            rooster_append_reply_tiffani_ep12(idx)
            return
        elif mroosterCommentSectionArray[idx] == "rooster_section_josy_ep12":
            rooster_append_reply_josy_ep12(idx)
            return
        elif mroosterCommentSectionArray[idx] == "rooster_section_nikita_ep12":
            rooster_append_reply_nikita_ep12(idx)
            return
        elif mroosterCommentSectionArray[idx] == "rooster_section_dawe_ep12":
            rooster_append_reply_dawe_ep12(idx)
            return
        elif mroosterCommentSectionArray[idx] == "rooster_section_tybalt_ep12":
            rooster_append_reply_tybalt_ep12(idx)
            return
        elif mroosterCommentSectionArray[idx] == "rooster_section_mc_ep12":
            rooster_append_reply_mc_ep12(idx)
            return
        elif mroosterCommentSectionArray[idx] == "rooster_section_sarah_ep12":
            rooster_append_reply_sarah_ep12(idx)
            return
        elif mroosterCommentSectionArray[idx] == "rooster_section_diks2_ep12":
            rooster_append_reply_diks2_ep12(idx)
            return
        return

    def getListIdx(what, list):
        for i in range(0,len(list)):
            if what == list[i]:
                return i
        return -1

    def checkedCluck():
        global roosterCurrentIdx
        global mroosterCommentSectionArray
        global freeRoamID
        global task_list
        global event_list
        
        if mroosterCommentSectionArray[roosterCurrentIdx] == "rooster_section_josy_ep12":
            if freeRoamID == "ep12_2":
                if task_list[2] == "Check Josy's cluck":
                    event_list.append("ep12_fr2_td_label")
                    task_list[2] = "Check out TheDiane"
        return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
