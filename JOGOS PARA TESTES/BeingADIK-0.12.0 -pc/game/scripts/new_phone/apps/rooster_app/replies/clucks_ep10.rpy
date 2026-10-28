init python:

    def rooster_append_reply_lily_ep10(idx):
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
            add_rooster_comment_response(idx,"alex","{color=#00a0e6}@%s{/color} Pff! Like you'd know what to do with her." % roosterNickMC.split("@")[1], 5)
            add_rooster_comment_response(idx,"lily","{color=#00a0e6}@%s{/color} Sure do, King." % roosterNickMC.split("@")[1], 4)
        elif mroosterChoices[idx][0] == 2:
            mroosterHistory_likes[idx].append(8)
            add_rooster_comment_response(idx,"lily","{color=#00a0e6}@%s{/color} You know it, King." % roosterNickMC.split("@")[1], 5)
        elif mroosterChoices[idx][0] == 3:
            mroosterHistory_likes[idx].append(10)
            add_rooster_comment_response(idx,"sarah","{color=#00a0e6}@%s{/color} Oh, lucky me. But I'd rather borrow the whole toy to play with." % roosterNickMC.split("@")[1], 5)
            add_rooster_comment_response(idx,"lily","{color=#00a0e6}@%s{/color} I'm not stingy. I like to share." % roosterNickSarah.split("@")[1], 15)
        return

    def rooster_append_reply_leon_ep10(idx):
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
            mroosterHistory_likes[idx].append(26)
            add_rooster_comment_response(idx,"lily","{color=#00a0e6}@%s{/color} Yeah, a fun house mirror. No, strike that. Even that would be a prettier sight." % roosterNickMC.split("@")[1], 13)
            add_rooster_comment_response(idx,"envy","{color=#00a0e6}@%s{/color} I'm seriously considering getting a haircut and never wearing green again." % roosterNickMC.split("@")[1], 10)
        elif mroosterChoices[idx][0] == 2:
            mroosterHistory_likes[idx].append(23)
            add_rooster_comment_response(idx,"jamie","{color=#00a0e6}@%s{/color} If I knew, you wouldn't have to ask... Didn't anyone check in with Leon about it yet?" % roosterNickMC.split("@")[1], 13)
            add_rooster_comment_response(idx,"sarah","{color=#00a0e6}@%s{/color} Oh, girl! You can delete this picture all you want. There is no way you can delete all those re-clucks, though." % roosterNickJamie.split("@")[1], 17)
            add_rooster_comment_response(idx,"jacob","{color=#00a0e6}@%s{/color} Don't worry, bro. We all make mistakes." % roosterNickJamie.split("@")[1], 7)
            add_rooster_comment_response(idx,"dany","{color=#00a0e6}@%s{/color} Dressing in lingerie is a mistake to you!? That sounds misogynistic." % roosterNickJacob.split("@")[1], 1)
            add_rooster_comment_response(idx,"jacob","And I'm muting this comment section. It was fun while it lasted. Cya!",1)
        elif mroosterChoices[idx][0] == 3:
            mroosterHistory_likes[idx].append(10)
            add_rooster_comment_response(idx,"jacob","{color=#00a0e6}@%s{/color} It would be humiliating as fuck! LOL! I like it!" % roosterNickMC.split("@")[1], 5)
            if not branchMayaJosy:
                add_rooster_comment_response(idx,"tommy","{color=#00a0e6}@%s{/color} Fuck no! No one wants to look at this shit for an entire week." % roosterNickMC.split("@")[1], 4)
            add_rooster_comment_response(idx,"rusty","{color=#00a0e6}@%s{/color} HAHA! Nice idea!" % roosterNickMC.split("@")[1], 2)
            add_rooster_comment_response(idx,"johnboy","{color=#00a0e6}@%s{/color} Hell Week is supposed to punish the maggots. When our brothers do this voluntarily, we oughta question if it's a punishment or not." % roosterNickMC.split("@")[1], 3)
            add_rooster_comment_response(idx,"jamie","{color=#00a0e6}@%s{/color} Trust me, it's a punishment. This isn't the first time I've made a bad choice while drinking." % roosterNickJohnBoy.split("@")[1], 9)
        return

    def rooster_append_reply_derek_ep10(idx):
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
            mroosterHistory_likes[idx].append(5)
            totalChickChoices += 1
            tmpdik -= 1
            add_rooster_comment_response(idx,"derek","Hey, it's my cluck. I didn't click on their fat faces to post a comment. Even after Gender Studies, I can't shake these bitches.",6)
        elif mroosterChoices[idx][0] == 2:
            mroosterHistory_likes[idx].append(3)
            add_rooster_comment_response(idx,"derek","{color=#00a0e6}@%s{/color} These girls need to learn how to tolerate people who are different. Am I right?" % roosterNickMC.split("@")[1], 4)

    def rooster_append_reply_elena_ep10(idx):
        global mroosterChoices
        global mroosterHistory_text
        global mroosterHistory_avatars
        global mroosterHistory_liked
        global mroosterHistory_likes
        global totalDikChoices
        global tmpdik
        global affinity
        global branchSage
        global branchAlone
        global ep9_photos
        global ep10_quinn_photo
        global totalChickChoices
        
        mroosterHistory_text[idx].append(mroosterChoices[idx][mroosterChoices[idx][0]])
        mroosterHistory_avatars[idx].append(mc_avatar)
        mroosterHistory_nicknames[idx].append(roosterNickMC)
        mroosterHistory_liked[idx].append(False)
        
        if mroosterChoices[idx][0] == 1:
            mroosterHistory_likes[idx].append(15)
            totalChickChoices += 1
            tmpdik -= 1
            add_rooster_comment_response(idx,"elena","{color=#00a0e6}@%s{/color} Thanks, cutie. It's fun to have these as memories of a great party." % roosterNickMC.split("@")[1], 6)
            add_rooster_comment_response(idx,"jacob","{color=#00a0e6}@%s{/color} Thanks, bro." % roosterNickMC.split("@")[1], 2)
        elif mroosterChoices[idx][0] == 2:
            if affinity == "DIK":
                mroosterHistory_likes[idx].append(7)
                if branchSage:
                    add_rooster_comment_response(idx,"sage","{color=#00a0e6}@%s{/color} You know it." % roosterNickMC.split("@")[1], 7)
                    add_rooster_comment_response(idx,"sarah","{color=#00a0e6}@%s{/color} FYI, this is public." % roosterNickMC.split("@")[1], 5)
                elif branchAlone:
                    add_rooster_comment_response(idx,"sage","{color=#00a0e6}@%s{/color} If you only knew. GRR!" % roosterNickMC.split("@")[1], 6)
                else:
                    add_rooster_comment_response(idx,"sage","{color=#00a0e6}@%s{/color} LOL. Easy there." % roosterNickMC.split("@")[1], 5)
            else:
                mroosterHistory_likes[idx].append(5)
                add_rooster_comment_response(idx,"sage","{color=#00a0e6}@%s{/color} Do you really think I'm that innocent? Hm?" % roosterNickMC.split("@")[1], 6)
        elif mroosterChoices[idx][0] == 3:
            if ep9_photos[4]:
                mroosterHistory_likes[idx].append(6)
                add_rooster_comment_response(idx,"jill","{color=#00a0e6}@%s{/color} It's such a funny picture!" % roosterNickMC.split("@")[1], 3)
            elif ep9_photos[5]:
                mroosterHistory_likes[idx].append(5)
                add_rooster_comment_response(idx,"maya","{color=#00a0e6}@%s{/color} Way better!" % roosterNickMC.split("@")[1], 3)
            elif ep9_photos[6]:
                mroosterHistory_likes[idx].append(5)
                add_rooster_comment_response(idx,"josy","{color=#00a0e6}@%s{/color} All that time spent in the gym is starting to pay off." % roosterNickMC.split("@")[1], 4)
            elif ep9_photos[7] or ep9_photos[8]:
                mroosterHistory_likes[idx].append(4)
                if ep9_photos[7]:
                    ep10_quinn_photo = 1
                else:
                    ep10_quinn_photo = 2
                add_rooster_comment_response(idx,"quinn","{color=#00a0e6}@%s{/color} What are you, a teenage girl?" % roosterNickMC.split("@")[1], 4)

    def rooster_append_reply_jill_ep10(idx):
        global mroosterChoices
        global mroosterHistory_text
        global mroosterHistory_avatars
        global mroosterHistory_liked
        global mroosterHistory_likes
        global totalDikChoices
        global tmpdik
        global affinity
        global name
        global totalChickChoices
        
        mroosterHistory_text[idx].append(mroosterChoices[idx][mroosterChoices[idx][0]])
        mroosterHistory_avatars[idx].append(mc_avatar)
        mroosterHistory_nicknames[idx].append(roosterNickMC)
        mroosterHistory_liked[idx].append(False)
        
        if mroosterChoices[idx][0] == 1:
            mroosterHistory_likes[idx].append(10)
            add_rooster_comment_response(idx,"jill","{color=#00a0e6}@%s{/color} Haha, it was! A little bit." % roosterNickMC.split("@")[1], 12)
        elif mroosterChoices[idx][0] == 2:
            mroosterHistory_likes[idx].append(8)
            totalDikChoices += 1
            tmpdik += 1
            add_rooster_comment_response(idx,"mc","{color=#00a0e6}@%s{/color} Whoops! I tagged the wrong person." % roosterNickTybalt.split("@")[1], 10)
            add_rooster_comment_response(idx,"mc","{color=#00a0e6}@%s{/color} Did you see this?" % roosterNickTybalt.split("@")[1], 10)
            add_rooster_comment_response(idx,"mc","{color=#00a0e6}@%s{/color} Dammit, it happened again." % roosterNickTybalt.split("@")[1], 15)
            add_rooster_comment_response(idx,"jill","{color=#00a0e6}@%s{/color} [name]..." % roosterNickMC.split("@")[1], 12)
            add_rooster_comment_response(idx,"mc","{color=#00a0e6}@%s{/color} Total accident, I swear!" % roosterNickTybalt.split("@")[1], 11)
            add_rooster_comment_response(idx,"mc","{color=#00a0e6}@%s{/color} Ok, that last one wasn't meant for you; it was meant for my girlfriend Jill. Sorry!" % roosterNickTybalt.split("@")[1], 20)
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
