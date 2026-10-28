init python:

    def rooster_append_reply_jamie_ep9(idx):
        global mroosterChoices
        global mroosterHistory_text
        global mroosterHistory_avatars
        global mroosterHistory_liked
        global mroosterHistory_likes
        global totalDikChoices
        global tmpdik
        global totalChickChoices
        
        mroosterHistory_text[idx].append(mroosterChoices[idx][mroosterChoices[idx][0]])
        mroosterHistory_avatars[idx].append(mc_avatar)
        mroosterHistory_nicknames[idx].append(roosterNickMC)
        mroosterHistory_liked[idx].append(False)
        
        if mroosterChoices[idx][0] == 1:
            mroosterHistory_likes[idx].append(6)
            add_rooster_comment_response(idx,"jamie","{color=#00a0e6}@%s{/color} Yeah, we did! Thanks for the reminder." % roosterNickMC.split("@")[1], 3)
            add_rooster_comment_response(idx,"tommy","{color=#00a0e6}@%s{/color} NO! You can't come! FUCK OFF!" % roosterNickMinny.split("@")[1], 10)
        elif mroosterChoices[idx][0] == 2:
            mroosterHistory_likes[idx].append(3)
            add_rooster_comment_response(idx,"jamie","{color=#00a0e6}@%s{/color} Don't worry. I've got this." % roosterNickMC.split("@")[1], 3)
            add_rooster_comment_response(idx,"tommy","{color=#00a0e6}@%s{/color} NO! None of you fat bitches can come! FUCK OFF!" % roosterNickMinny.split("@")[1], 10)
        elif mroosterChoices[idx][0] == 3:
            mroosterHistory_likes[idx].append(8)
            totalDikChoices += 1
            tmpdik += 1
            add_rooster_comment_response(idx,"tommy","{color=#00a0e6}@%s{/color} Damn, you beat me to it! LMAO!" % roosterNickMC.split("@")[1], 4)
            add_rooster_comment_response(idx,"jacob","{color=#00a0e6}@%s{/color} SAVAGE! LOL!" % roosterNickMC.split("@")[1], 5)
            add_rooster_comment_response(idx,"dany","{color=#00a0e6}@%s{/color} Are you gonna let them talk to my friends like that!?" % roosterNickJamie.split("@")[1], 2)
            add_rooster_comment_response(idx,"jamie","{color=#00a0e6}@%s{/color} Please, just relax!" % roosterNickDany.split("@")[1], 1)
        return

    def rooster_append_reply_elena_ep9(idx):
        global mroosterChoices
        global mroosterHistory_text
        global mroosterHistory_avatars
        global mroosterHistory_liked
        global mroosterHistory_likes
        global totalDikChoices
        global tmpdik
        global totalChickChoices
        global name
        
        mroosterHistory_text[idx].append(mroosterChoices[idx][mroosterChoices[idx][0]])
        mroosterHistory_avatars[idx].append(mc_avatar)
        mroosterHistory_nicknames[idx].append(roosterNickMC)
        mroosterHistory_liked[idx].append(False)
        
        if mroosterChoices[idx][0] == 1:
            mroosterHistory_likes[idx].append(16)
            add_rooster_comment_response(idx,"elena","{color=#00a0e6}@%s{/color} Yes! Listen to [name]! Get it done, party people!" % roosterNickMC.split("@")[1], 13)
            add_rooster_comment_response(idx,"johnboy","{color=#00a0e6}@%s{/color} I'm gonna rally some people right now." % roosterNickMC.split("@")[1], 10)
            add_rooster_comment_response(idx,"jacob","{color=#00a0e6}@%s{/color} Do it! I'll be there to help out with taking pictures." % roosterNickJohnBoy.split("@")[1], 6)
        elif mroosterChoices[idx][0] == 2:
            totalChickChoices += 1
            tmpdik -= 1
            mroosterHistory_likes[idx].append(6)
            add_rooster_comment_response(idx,"elena","{color=#00a0e6}@%s{/color} This was our idea; it wouldn't be fair to let you take care of it. Sounds to me like you've already got too much riding on your shoulders tonight." % roosterNickMC.split("@")[1], 13)
            add_rooster_comment_response(idx,"sage","{color=#00a0e6}@%s{/color} Don't forget to have fun! Let's dance!!!" % roosterNickMC.split("@")[1], 8)
        elif mroosterChoices[idx][0] == 3:
            mroosterHistory_likes[idx].append(11)
            add_rooster_comment_response(idx,"lily","{color=#00a0e6}@%s{/color} I'll work extra for you if you want it, babe!" % roosterNickMC.split("@")[1], 9)
            add_rooster_comment_response(idx,"rose","{color=#00a0e6}@%s{/color} YAY! [name] is there! Keep your pants on until we're there!" % roosterNickMC.split("@")[1], 5)
            add_rooster_comment_response(idx,"sandy","{color=#00a0e6}@%s{/color} GRRR!!!" % roosterNickMC.split("@")[1], 3)
        
        return

    def rooster_append_reply_camila_ep9(idx):
        global mroosterChoices
        global mroosterHistory_text
        global mroosterHistory_avatars
        global mroosterHistory_liked
        global mroosterHistory_likes
        
        mroosterHistory_text[idx].append(mroosterChoices[idx][mroosterChoices[idx][0]])
        mroosterHistory_avatars[idx].append(mc_avatar)
        mroosterHistory_nicknames[idx].append(roosterNickMC)
        mroosterHistory_liked[idx].append(False)
        
        if mroosterChoices[idx][0] == 1:
            mroosterHistory_likes[idx].append(1)
            add_rooster_comment_response(idx,"camila","{color=#00a0e6}@%s{/color} Yes! Let's dance all night! But don't forget to hydrate." % roosterNickMC.split("@")[1], 1)
        elif mroosterChoices[idx][0] == 2:
            mroosterHistory_likes[idx].append(1)
            add_rooster_comment_response(idx,"camila","{color=#00a0e6}@%s{/color} Haha! You could tell, huh?" % roosterNickMC.split("@")[1], 1)

    def rooster_append_reply_karen_ep9(idx):
        global mroosterChoices
        global mroosterHistory_text
        global mroosterHistory_avatars
        global mroosterHistory_liked
        global mroosterHistory_likes
        
        mroosterHistory_text[idx].append(mroosterChoices[idx][mroosterChoices[idx][0]])
        mroosterHistory_avatars[idx].append(mc_avatar)
        mroosterHistory_nicknames[idx].append(roosterNickMC)
        mroosterHistory_liked[idx].append(False)
        
        if mroosterChoices[idx][0] == 1:
            mroosterHistory_likes[idx].append(16)
            add_rooster_comment_response(idx,"karen","{color=#00a0e6}@%s{/color} Thanks!!!" % roosterNickMC.split("@")[1], 5)
        elif mroosterChoices[idx][0] == 2:
            mroosterHistory_likes[idx].append(1)
            add_rooster_comment_response(idx,"maya","{color=#00a0e6}@%s{/color} Haha! And you dodged a bullet question, I believe. Hm?" % roosterNickMC.split("@")[1], 2)
            add_rooster_comment_response(idx,"karen","{color=#00a0e6}@%s{/color} Thanks for fixing it!" % roosterNickMC.split("@")[1], 5)
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
