init python:
    def rooster_append_reply_josy_ep11(idx):
        global mroosterChoices
        global mroosterHistory_text
        global mroosterHistory_avatars
        global mroosterHistory_liked
        global mroosterHistory_likes
        global branchMayaJosy
        
        mroosterHistory_text[idx].append(mroosterChoices[idx][mroosterChoices[idx][0]])
        mroosterHistory_avatars[idx].append(mc_avatar)
        mroosterHistory_nicknames[idx].append(roosterNickMC)
        mroosterHistory_liked[idx].append(False)
        
        if mroosterChoices[idx][0] == 1:
            mroosterHistory_likes[idx].append(6)
            add_rooster_comment_response(idx,"blogguy1","{color=#00a0e6}@%s{/color} Another troll account. Clean this comment up, too." % roosterNickMC.split("@")[1], 18)
            add_rooster_comment_response(idx,"sage","{color=#00a0e6}@%s{/color} Yeah! Stop it, you troll. LMAO" % roosterNickMC.split("@")[1], 4)
            add_rooster_comment_response(idx,"maya","{color=#00a0e6}@%s{/color} I am so confused right now." % roosterNickMC.split("@")[1], 5)
            add_rooster_comment_response(idx,"bloguser1","FREE RAM for your computer! {color=#00a0e6}Download here{/color} Offer expires in 24 hours!",2)
        elif mroosterChoices[idx][0] == 2:
            if branchMayaJosy:
                mroosterHistory_likes[idx].append(4)
                add_rooster_comment_response(idx,"blogguy1","{color=#00a0e6}@%s{/color} Don't insert yourself into someone else's conversation. Show some respect." % roosterNickMC.split("@")[1], 12)
            else:
                mroosterHistory_likes[idx].append(8)
                add_rooster_comment_response(idx,"blogguy1","{color=#00a0e6}@%s{/color} I already reported the posts as spam. Thanks for looking out!" % roosterNickMC.split("@")[1], 10)
            add_rooster_comment_response(idx,"maya","{color=#00a0e6}@%s{/color} I am so confused right now." % roosterNickMC.split("@")[1], 5)
            add_rooster_comment_response(idx,"bloguser1","FREE RAM for your computer or phone! {color=#00a0e6}Download here{/color} Offer expires in 24 hours!",2)
        return

    def rooster_append_reply_lily_ep11(idx):
        global mroosterChoices
        global mroosterHistory_text
        global mroosterHistory_avatars
        global mroosterHistory_liked
        global mroosterHistory_likes
        global branchAlone
        global totalDikChoices
        global tmpdik
        
        mroosterHistory_text[idx].append(mroosterChoices[idx][mroosterChoices[idx][0]])
        mroosterHistory_avatars[idx].append(mc_avatar)
        mroosterHistory_nicknames[idx].append(roosterNickMC)
        mroosterHistory_liked[idx].append(False)
        
        if mroosterChoices[idx][0] == 1:
            mroosterHistory_likes[idx].append(7)
            add_rooster_comment_response(idx,"sage","{color=#00a0e6}@%s{/color} No cigar." % roosterNickMC.split("@")[1], 3)
            add_rooster_comment_response(idx,"sarah","{color=#00a0e6}@%s{/color} Baby Doo-doo Dawe?" % roosterNickSage.split("@")[1], 4)
            add_rooster_comment_response(idx,"sage","{color=#00a0e6}@%s{/color} BUZZ!!! Wrong!" % roosterNickSarah.split("@")[1], 4)
            add_rooster_comment_response(idx,"dawe","{color=#00a0e6}@%s{/color} STOP IT! I'm sorry, ok?" % roosterNickSage.split("@")[1], 2)
            add_rooster_comment_response(idx,"sage","{color=#00a0e6}@%s{/color} Mama HOT accepts your apology." % roosterNickDawe.split("@")[1], 3)
            add_rooster_comment_response(idx,"dawe","For the record, I'm hung like a gorilla!", 2)
            add_rooster_comment_response(idx,"sarah","{color=#00a0e6}@%s{/color} You should probably search online before saying that." % roosterNickDawe.split("@")[1], 4)
        elif mroosterChoices[idx][0] == 2:
            mroosterHistory_likes[idx].append(6)
            if branchAlone:
                totalDikChoices += 1
                tmpdik += 1
                add_rooster_comment_response(idx,"sarah","{color=#00a0e6}@%s{/color} Aw, you're just like the rest of the boys?" % roosterNickMC.split("@")[1], 2)
            else:
                add_rooster_comment_response(idx,"lily","{color=#00a0e6}@%s{/color} What!? He isn't? You just ruined my childhood. So, it was just a fat guy in a red suit that came to my house in the middle of the night?" % roosterNickMC.split("@")[1], 3)
                add_rooster_comment_response(idx,"sarah","{color=#00a0e6}@%s{/color} That sounds scary! Did the dude steal anything? It might have been a robbery." % roosterNickLily.split("@")[1], 2)
                add_rooster_comment_response(idx,"lily","{color=#00a0e6}@%s{/color} He did steal something! He took Santa's milk and cookies." % roosterNickSarah.split("@")[1], 2)
                add_rooster_comment_response(idx,"sarah","{color=#00a0e6}@%s{/color} You know what you have to do. Call the cops already." % roosterNickLily.split("@")[1], 4)
                add_rooster_comment_response(idx,"sage","{color=#00a0e6}@%s @%s{/color} Or here's an idea... Get back to work!" % (roosterNickSarah.split("@")[1],roosterNickLily.split("@")[1]), 3)
                add_rooster_comment_response(idx,"sarah","{color=#00a0e6}@%s{/color} You heard Mama HOT." % roosterNickLily.split("@")[1], 5)
        return

    def rooster_append_reply_dany_ep11(idx):
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
            mroosterHistory_likes[idx].append(5)
            add_rooster_comment_response(idx,"jamie","{color=#00a0e6}@%s{/color} You're right. I'm so done with her; you have no idea!" % roosterNickMC.split("@")[1], 4)
            add_rooster_comment_response(idx,"leon","{color=#00a0e6}@%s{/color} YEEEES! Let's find you someone new to bang tonight." % roosterNickJamie.split("@")[1], 2)
            add_rooster_comment_response(idx,"dany","{color=#00a0e6}@%s{/color} BURN IN HELL!" % roosterNickJamie.split("@")[1], 3)
            add_rooster_comment_response(idx,"suzy","{color=#00a0e6}@%s{/color} You're single now, right?" % roosterNickJamie.split("@")[1], 1)
        elif mroosterChoices[idx][0] == 2:
            mroosterHistory_likes[idx].append(4)
            add_rooster_comment_response(idx,"dany","{color=#00a0e6}@%s{/color} STAY OUT OF THIS! You didn't even know Franz! How dare you!?" % roosterNickMC.split("@")[1], 3)
            add_rooster_comment_response(idx,"wendy","{color=#00a0e6}@%s{/color} He's not wrong, though. Franz wouldn't have wanted this." % roosterNickDany.split("@")[1], 4)
            add_rooster_comment_response(idx,"jamie","RIP Franz.", 4)
            add_rooster_comment_response(idx,"suzy","{color=#00a0e6}@%s{/color} You're single now, right?" % roosterNickJamie.split("@")[1], 1)
        return

    def rooster_append_reply_bianca_ep11(idx):
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
            mroosterHistory_likes[idx].append(2)
            add_rooster_comment_response(idx,"jill","{color=#00a0e6}@%s{/color} There's no rush, but I definitely want those photos as memories." % roosterNickMC.split("@")[1], 1)
            add_rooster_comment_response(idx,"mc","{color=#00a0e6}@%s{/color} Did you know that Bianca and Carla are here tonight? You should have come!" % roosterNickJill.split("@")[1], 1)
            add_rooster_comment_response(idx,"jill","{color=#00a0e6}@%s{/color} I'm aware, and my answer remains unchanged. Say hi to them from me!" % roosterNickMC.split("@")[1], 1)
        return

    def rooster_append_reply_diks_ep11(idx):
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
            mroosterHistory_likes[idx].append(42)
            add_rooster_comment_response(idx,"tiffani","{color=#00a0e6}@%s{/color} OMG YES!!!" % roosterNickMC.split("@")[1], 9)
            add_rooster_comment_response(idx,"sarah","{color=#00a0e6}@%s{/color} HAHA! Kind of a stretch, but I like it!" % roosterNickMC.split("@")[1], 12)
            add_rooster_comment_response(idx,"jamie","{color=#00a0e6}@%s{/color} JINGLE BALLS JINGLE BALLS JIGGLING ALL THE WAY!" % roosterNickMC.split("@")[1], 14)
        elif mroosterChoices[idx][0] == 2:
            mroosterHistory_likes[idx].append(34)
            add_rooster_comment_response(idx,"tiffani","{color=#00a0e6}@%s{/color} LOL! You're too funny!" % roosterNickMC.split("@")[1], 9)
            add_rooster_comment_response(idx,"elena","{color=#00a0e6}@%s{/color} BONERRIFIC! Am I right?" % roosterNickMC.split("@")[1], 10)
            add_rooster_comment_response(idx,"rusty","{color=#00a0e6}@%s{/color} Remind me to block these girls on our DIK account later." % roosterNickMC.split("@")[1], 19)
        else:
            mroosterHistory_likes[idx].append(55)
            add_rooster_comment_response(idx,"tiffani","{color=#00a0e6}@%s{/color} LMAO! What the hell was that!?" % roosterNickMC.split("@")[1], 15)
            add_rooster_comment_response(idx,"jacob","Floss on a walrus fucking floored me! AHAHAHA!",22)
            add_rooster_comment_response(idx,"derek","{color=#00a0e6}@%s{/color} You set the fucking fire alarm off with that burn!" % roosterNickMC.split("@")[1], 25)
            add_rooster_comment_response(idx,"rusty","{color=#00a0e6}@%s{/color} Remind me to block these girls on our DIK account later." % roosterNickMC.split("@")[1], 19)
            add_rooster_comment_response(idx,"mc","Thank you! Thank you! I'll be here all night. And luckily, those girls won't be.", 18)
        return

    def rooster_append_reply_mc_ep11(idx):
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
            mroosterHistory_likes[idx].append(2)
            add_rooster_comment_response(idx,"derek","Change your password or something. Someone else is using your account.", 1)
            add_rooster_comment_response(idx,"mc","FREE RAM for your computer! {color=#00a0e6}Download here{/color} Offer expires in 24 hours!",2)
            add_rooster_comment_response(idx,"mc","{color=#00a0e6}@%s{/color} Right! I'm on it!" % roosterNickDerek.split("@")[1], 1)
            add_rooster_comment_response(idx,"jamie","FREE RAM for your computer! {color=#00a0e6}Download here{/color} Offer expires in 24 hours!",2)
            add_rooster_comment_response(idx,"arieth","FREE RAM for your computer! {color=#00a0e6}Download here{/color} Offer expires in 24 hours!",2)
            add_rooster_comment_response(idx,"dawe","FREE RAM for your computer! {color=#00a0e6}Download here{/color} Offer expires in 24 hours!",2)
        return

    def rooster_append_reply_maya_ep11(idx):
        global mroosterChoices
        global mroosterHistory_text
        global mroosterHistory_avatars
        global mroosterHistory_liked
        global mroosterHistory_likes
        global ep11_virus
        
        mroosterHistory_text[idx].append(mroosterChoices[idx][mroosterChoices[idx][0]])
        mroosterHistory_avatars[idx].append(mc_avatar)
        mroosterHistory_nicknames[idx].append(roosterNickMC)
        mroosterHistory_liked[idx].append(False)
        
        if mroosterChoices[idx][0] == 1:
            mroosterHistory_likes[idx].append(2)
            add_rooster_comment_response(idx,"maya","{color=#00a0e6}@%s{/color} I feel the same way! Let's compare notes before Friday; maybe we can learn something from each other." % roosterNickMC.split("@")[1], 2)
            add_rooster_comment_response(idx,"derek","{color=#00a0e6}@%s @%s{/color} You nerds better stay away from the finals talk tonight." % (roosterNickMC.split("@")[1],roosterNickMaya.split("@")[1]), 1)
            if ep11_virus:
                add_rooster_comment_response(idx,"mc","FREE RAM for your computer! {color=#00a0e6}Download here{/color} Offer expires in 24 hours!",2)
            add_rooster_comment_response(idx,"maya","{color=#00a0e6}@%s{/color} That's your conscience speaking. You should study more." % roosterNickDerek.split("@")[1], 2)
        elif mroosterChoices[idx][0] == 2:
            mroosterHistory_likes[idx].append(5)
            add_rooster_comment_response(idx,"maya","{color=#00a0e6}@%s{/color} I can't wait!" % roosterNickMC.split("@")[1], 3)
            if ep11_virus:
                add_rooster_comment_response(idx,"mc","FREE RAM for your computer! {color=#00a0e6}Download here{/color} Offer expires in 24 hours!",2)
            add_rooster_comment_response(idx,"derek","{color=#00a0e6}@%s{/color} Why wait a week when you can start already? Let's get wasted tonight!" % roosterNickMC.split("@")[1], 1)
            add_rooster_comment_response(idx,"maya","{color=#00a0e6}@%s{/color} Don't overdo it." % roosterNickDerek.split("@")[1], 1)
        
        
        return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
