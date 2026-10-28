init python:


    def rooster_append_reply_josy_ep8(idx):
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
            totalChickChoices += 1
            tmpdik -= 1
            mroosterHistory_likes[idx].append(5)
            if pathMayaJosy:
                add_rooster_comment_response(idx,"josy","{color=#00a0e6}@%s{/color} I loved working out with you!" % roosterNickMC.split("@")[1], 4)
            else:
                add_rooster_comment_response(idx,"josy","{color=#00a0e6}@%s{/color} It was so fun working out with you!" % roosterNickMC.split("@")[1], 4)
        elif mroosterChoices[idx][0] == 2:
            mroosterHistory_likes[idx].append(8)
            totalDikChoices += 1
            tmpdik += 1
            add_rooster_comment_response(idx,"dawe","{color=#00a0e6}@%s{/color} I don't see your muscles beating mine, you scrawny bitch!"  % roosterNickMC.split("@")[1], 8)
            add_rooster_comment_response(idx,"anthony","{color=#00a0e6}@%s{/color} I don't think he's that far off. If he just focused on lifting heavier and eating right, he'd be bigger than you."  % roosterNickDawe.split("@")[1], 5)
            add_rooster_comment_response(idx,"dawe","{color=#00a0e6}@%s{/color} Shut up!"  % roosterNickAnthony.split("@")[1], 4)
        return

    def rooster_append_reply_derek_ep8(idx):
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
            mroosterHistory_likes[idx].append(4)
            add_rooster_comment_response(idx,"derek","{color=#00a0e6}@%s{/color} Yet I feel violated!" % roosterNickMC.split("@")[1], 2)
            add_rooster_comment_response(idx,"maya","{color=#00a0e6}@%s{/color} Stop being such a Karen." % roosterNickDerek.split("@")[1], 4)
            add_rooster_comment_response(idx,"derek","{color=#00a0e6}@%s{/color} Politically incorrect, much? Typical feminists!" % roosterNickMaya.split("@")[1], 1)
        elif mroosterChoices[idx][0] == 2:
            mroosterHistory_likes[idx].append(2)
            add_rooster_comment_response(idx,"derek","{color=#00a0e6}@%s{/color} Wow! You're taking the side of the man? I'm disappointed, [mc_de]."  % roosterNickMC.split("@")[1], 2)
            add_rooster_comment_response(idx,"maya","{color=#00a0e6}@%s{/color} Stop it. Wilbert's is great. For such a small store, they sure have everything."  % roosterNickDerek.split("@")[1], 3)
            add_rooster_comment_response(idx,"derek","{color=#00a0e6}@%s{/color} Yeah, they're pretty damn heavy on security! I'll give you that." % roosterNickMaya.split("@")[1], 0)
        return

    def rooster_append_reply_lily_ep8(idx):
        global mroosterChoices
        global mroosterHistory_text
        global mroosterHistory_avatars
        global mroosterHistory_liked
        global mroosterHistory_likes
        global ep6_envy_lewd
        
        mroosterHistory_text[idx].append(mroosterChoices[idx][mroosterChoices[idx][0]])
        mroosterHistory_avatars[idx].append(mc_avatar)
        mroosterHistory_nicknames[idx].append(roosterNickMC)
        mroosterHistory_liked[idx].append(False)
        
        if mroosterChoices[idx][0] == 1:
            mroosterHistory_likes[idx].append(10)
            add_rooster_comment_response(idx,"leon","{color=#00a0e6}@%s{/color} Why would you give him your shift?" % roosterNickTommy.split("@")[1], 6)
            add_rooster_comment_response(idx,"tommy","{color=#00a0e6}@%s{/color} I fucking had to. I'll never do it again, though." % roosterNickLeon.split("@")[1], 4)
            if ep6_envy_lewd:
                add_rooster_comment_response(idx,"envy","{color=#00a0e6}@%s{/color} LAMB CHOP! Haha!" % roosterNickMC.split("@")[1], 6)
        elif mroosterChoices[idx][0] == 2:
            mroosterHistory_likes[idx].append(15)
            add_rooster_comment_response(idx,"lily","{color=#00a0e6}@%s{/color} MWAH!" % roosterNickMC.split("@")[1], 4)
            add_rooster_comment_response(idx,"tommy","{color=#00a0e6}@%s{/color} Very funny! Tania just told me nothing happened!" % roosterNickMC.split("@")[1], 2)
            add_rooster_comment_response(idx,"heather","{color=#00a0e6}@%s{/color} Still working hard on not caring, huh?" % roosterNickTommy.split("@")[1], 8)
            if ep6_envy_lewd:
                add_rooster_comment_response(idx,"envy","{color=#00a0e6}@%s{/color} LAMB CHOP! Haha!" % roosterNickMC.split("@")[1], 6)
        return

    def rooster_append_reply_jill_ep8(idx):
        global mroosterChoices
        global mroosterHistory_text
        global mroosterHistory_avatars
        global mroosterHistory_liked
        global mroosterHistory_likes
        global RPjill
        
        mroosterHistory_text[idx].append(mroosterChoices[idx][mroosterChoices[idx][0]])
        mroosterHistory_avatars[idx].append(mc_avatar)
        mroosterHistory_nicknames[idx].append(roosterNickMC)
        mroosterHistory_liked[idx].append(False)
        
        if mroosterChoices[idx][0] == 1:
            RPjill += 1
            mroosterHistory_likes[idx].append(1)
            add_rooster_comment_response(idx,"jill","{color=#00a0e6}@%s #SmartyPants{/color}" % roosterNickMC.split("@")[1], 0)
        elif mroosterChoices[idx][0] == 2:
            RPjill += 1
            mroosterHistory_likes[idx].append(1)
            add_rooster_comment_response(idx,"jill","{color=#00a0e6}@%s{/color} Haha!" % roosterNickMC.split("@")[1], 0)
        return

    def rooster_append_reply_quinn_ep8(idx):
        global mroosterChoices
        global mroosterHistory_text
        global mroosterHistory_avatars
        global mroosterHistory_liked
        global mroosterHistory_likes
        global ep6_quinn_lewd
        global affinity
        global ep8_quinn_rejected_you
        
        mroosterHistory_text[idx].append(mroosterChoices[idx][mroosterChoices[idx][0]])
        mroosterHistory_avatars[idx].append(mc_avatar)
        mroosterHistory_nicknames[idx].append(roosterNickMC)
        mroosterHistory_liked[idx].append(False)
        
        if mroosterChoices[idx][0] == 1:
            mroosterHistory_likes[idx].append(13)
            if ep6_quinn_lewd and affinity != "CHICK" and not ep8_quinn_rejected_you:
                add_rooster_comment_response(idx,"quinn","{color=#00a0e6}@%s{/color} I'm just getting warmed up, broccoli." % roosterNickMC.split("@")[1], 6)
            else:
                add_rooster_comment_response(idx,"quinn","{color=#00a0e6}@%s{/color} I'm just getting warmed up, bitch." % roosterNickMC.split("@")[1], 6)
            add_rooster_comment_response(idx,"heather","{color=#00a0e6}@%s{/color} Yeah, what the hell was that pic? It was kinda weird." % roosterNickQuinn.split("@")[1], 9)
        elif mroosterChoices[idx][0] == 2:
            mroosterHistory_likes[idx].append(9)
            add_rooster_comment_response(idx,"quinn","{color=#00a0e6}@%s{/color} See!? No shame!" % roosterNickMC.split("@")[1], 5)
            add_rooster_comment_response(idx,"leon","{color=#00a0e6}@%s{/color} HAHA! The titty airplane! That's fucking funny!" % roosterNickMC.split("@")[1], 9)
            add_rooster_comment_response(idx,"jacob","{color=#00a0e6}@%s{/color} Way to own it! LOL!" % roosterNickMC.split("@")[1], 5)
        return

    def rooster_append_reply_mc_ep8(idx):
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
            add_rooster_comment_response(idx,"sage","{color=#00a0e6}@%s{/color} Haha... Who are you?" % roosterNickMC.split("@")[1], 0)
        elif mroosterChoices[idx][0] == 2:
            mroosterHistory_likes[idx].append(1)
            add_rooster_comment_response(idx,"sage","{color=#00a0e6}@%s{/color} I don't know. I've never gotten one. But yeah, probably. It is a nice leaf." % roosterNickMC.split("@")[1], 0)
        return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
