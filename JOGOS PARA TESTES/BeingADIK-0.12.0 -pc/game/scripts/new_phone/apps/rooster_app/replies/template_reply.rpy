init python:
    def template_reply(idx):
        global mroosterChoices
        global mroosterHistory_text
        global mroosterHistory_avatars
        global mroosterHistory_liked
        global mroosterHistory_likes
        
        mroosterHistory_text[idx].append(mroosterChoices[idx][mroosterChoices[idx][0]])
        mroosterHistory_avatars[idx].append("rooster_mini_mc1")
        mroosterHistory_nicknames[idx].append(roosterNickMC)
        mroosterHistory_liked[idx].append(False)
        mroosterHistory_likes[idx].append(5)
        
        if mroosterChoices[idx][0] == 1:
            mroosterHistory_text[idx].append("OPTION 1 chosen")
            mroosterHistory_avatars[idx].append("rooster_mini_mc1")
            mroosterHistory_nicknames[idx].append(roosterNickMC)
            mroosterHistory_liked[idx].append(False)
            mroosterHistory_likes[idx].append(5)
        elif mroosterChoices[idx][0] == 2:
            mroosterHistory_text[idx].append("I chose option 2")
            mroosterHistory_avatars[idx].append("rooster_mini_mc1")
            mroosterHistory_nicknames[idx].append(roosterNickMC)
            mroosterHistory_liked[idx].append(False)
            mroosterHistory_likes[idx].append(5)
        
        return

    def template_reply2(idx):
        global mroosterChoices
        global mroosterHistory_text
        global mroosterHistory_avatars
        global mroosterHistory_liked
        global mroosterHistory_likes
        
        mroosterHistory_text[idx].append(mroosterChoices[idx][mroosterChoices[idx][0]])
        mroosterHistory_avatars[idx].append("rooster_mini_mc1")
        mroosterHistory_nicknames[idx].append(roosterNickMC)
        mroosterHistory_liked[idx].append(False)
        mroosterHistory_likes[idx].append(5)
        
        if mroosterChoices[idx][0] == 1:
            mroosterHistory_text[idx].append("OPTION 1b chosen")
            mroosterHistory_avatars[idx].append("rooster_mini_mc1")
            mroosterHistory_nicknames[idx].append(roosterNickMC)
            mroosterHistory_liked[idx].append(False)
            mroosterHistory_likes[idx].append(5)
        elif mroosterChoices[idx][0] == 2:
            mroosterHistory_text[idx].append("I chose option 2b")
            mroosterHistory_avatars[idx].append("rooster_mini_mc1")
            mroosterHistory_nicknames[idx].append(roosterNickMC)
            mroosterHistory_liked[idx].append(False)
            mroosterHistory_likes[idx].append(5)
        
        return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
