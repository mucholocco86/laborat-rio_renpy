init python:
    def rooster_append_reply_diks_ep12(idx):
        global mroosterChoices
        global mroosterHistory_text
        global mroosterHistory_avatars
        global mroosterHistory_liked
        global mroosterHistory_likes
        global ep11_mg_party
        global ep11_zoey_kiss
        
        mroosterHistory_text[idx].append(mroosterChoices[idx][mroosterChoices[idx][0]])
        mroosterHistory_avatars[idx].append(mc_avatar)
        mroosterHistory_nicknames[idx].append(roosterNickMC)
        mroosterHistory_liked[idx].append(False)
        
        if mroosterChoices[idx][0] == 1:
            mroosterHistory_likes[idx].append(3)
            add_rooster_comment_response(idx,"tommy","{color=#00a0e6}@%s{/color} You can take a backseat if you've got shit to do." % roosterNickMC.split("@")[1], 2)
            add_rooster_comment_response(idx,"mc","{color=#00a0e6}@%s{/color} I'm a bit limited because it's Christmas, but I'm sure that goes for all of us. Let me know what I can do." % roosterNickTommy.split("@")[1], 1)
            add_rooster_comment_response(idx,"tommy","{color=#00a0e6}@%s{/color} Aight." % roosterNickMC.split("@")[1], 1)
        elif mroosterChoices[idx][0] == 2:
            mroosterHistory_likes[idx].append(3)
            if ep11_mg_party and ep11_zoey_kiss < 2:
                add_rooster_comment_response(idx,"derek","{color=#00a0e6}@%s{/color} Are you going to leave this party before midnight, too?" % roosterNickMC.split("@")[1], 2)
                add_rooster_comment_response(idx,"mc","{color=#00a0e6}@%s{/color} Shush." % roosterNickDerek.split("@")[1], 1)
                add_rooster_comment_response(idx,"melanie","{color=#00a0e6}@%s{/color} Yeah! Where the hell did you go?" % roosterNickMC.split("@")[1], 3)
            else:
                add_rooster_comment_response(idx,"derek","{color=#00a0e6}@%s{/color} This guy is celebrating early." % roosterNickMC.split("@")[1], 2)
                add_rooster_comment_response(idx,"camila","{color=#00a0e6}@%s{/color} I'd better catch you on the dance floor for this one! Did you even dance once at the Christmas party?" % roosterNickMC.split("@")[1], 2)
                add_rooster_comment_response(idx,"mc","{color=#00a0e6}@%s{/color} I don't dance well in underwear. Or with other clothes, for that matter." % roosterNickCamila.split("@")[1], 1)
        elif mroosterChoices[idx][0] == 3:
            mroosterHistory_likes[idx].append(2)
            add_rooster_comment_response(idx,"tara","{color=#00a0e6}@%s{/color} XOXO" % roosterNickMC.split("@")[1], 5)
        return
    def rooster_append_reply_tiffani_ep12(idx):
        global mroosterChoices
        global mroosterHistory_text
        global mroosterHistory_avatars
        global mroosterHistory_liked
        global mroosterHistory_likes
        global name
        
        mroosterHistory_text[idx].append(mroosterChoices[idx][mroosterChoices[idx][0]])
        mroosterHistory_avatars[idx].append(mc_avatar)
        mroosterHistory_nicknames[idx].append(roosterNickMC)
        mroosterHistory_liked[idx].append(False)
        
        if mroosterChoices[idx][0] == 1:
            mroosterHistory_likes[idx].append(3)
            add_rooster_comment_response(idx,"tiffani","{color=#00a0e6}@%s{/color} Thanks, [name]. You too!!! I have to turn my phone off now." % roosterNickMC.split("@")[1], 2)
        elif mroosterChoices[idx][0] == 2:
            mroosterHistory_likes[idx].append(3)
            add_rooster_comment_response(idx,"leon","{color=#00a0e6}@%s{/color} I actually had a shot to correct the hangover. It made wonders for my hangover, but not so much for my test results." % roosterNickMC.split("@")[1], 3)
        elif mroosterChoices[idx][0] == 3:
            mroosterHistory_likes[idx].append(3)
            add_rooster_comment_response(idx,"tiffani","{color=#00a0e6}@%s{/color} Thanks, [name]. You too!!! I have to turn my phone off now." % roosterNickMC.split("@")[1], 1)
            add_rooster_comment_response(idx,"tara","{color=#00a0e6}@%s{/color} Aw, thank you!" % roosterNickMC.split("@")[1], 1)
        return
    def rooster_append_reply_dawe_ep12(idx):
        global mroosterChoices
        global mroosterHistory_text
        global mroosterHistory_avatars
        global mroosterHistory_liked
        global mroosterHistory_likes
        global totalDikChoices
        global tmpdik
        
        mroosterHistory_text[idx].append(mroosterChoices[idx][mroosterChoices[idx][0]])
        mroosterHistory_avatars[idx].append(mc_avatar)
        mroosterHistory_nicknames[idx].append(roosterNickMC)
        mroosterHistory_liked[idx].append(False)
        
        if mroosterChoices[idx][0] == 1:
            mroosterHistory_likes[idx].append(8)
            add_rooster_comment_response(idx,"alex","{color=#00a0e6}@%s{/color} For once, I agree with this guy." % roosterNickMC.split("@")[1], 1)
            add_rooster_comment_response(idx,"elena","{color=#00a0e6}@%s{/color} Don't pout. We'll make it work." % roosterNickMC.split("@")[1], 5)
        elif mroosterChoices[idx][0] == 2:
            totalDikChoices += 1
            tmpdik += 1
            mroosterHistory_likes[idx].append(7)
            add_rooster_comment_response(idx,"slop","{color=#00a0e6}@%s{/color} Sure can do! One bikini image is coming right up. {color=#00a0e6}Here{/color} is your requested image. Thank you for using SLOP!" % roosterNickMC.split("@")[1], 1)
            add_rooster_comment_response(idx,"dawe","{color=#00a0e6}@%s{/color} WHAT THE FUCK!?" % roosterNickMC.split("@")[1], 5)
            add_rooster_comment_response(idx,"alex","{color=#00a0e6}@%s{/color} I'm gonna kill this guy!" % roosterNickMC.split("@")[1], 2)
        return
    def rooster_append_reply_nikita_ep12(idx):
        global mroosterChoices
        global mroosterHistory_text
        global mroosterHistory_avatars
        global mroosterHistory_liked
        global mroosterHistory_likes
        global totalDikChoices
        global tmpdik
        
        mroosterHistory_text[idx].append(mroosterChoices[idx][mroosterChoices[idx][0]])
        mroosterHistory_avatars[idx].append(mc_avatar)
        mroosterHistory_nicknames[idx].append(roosterNickMC)
        mroosterHistory_liked[idx].append(False)
        
        if mroosterChoices[idx][0] == 1:
            mroosterHistory_likes[idx].append(4)
            add_rooster_comment_response(idx,"sally","{color=#00a0e6}@%s{/color} It had to die. Salloony was a time thief!" % roosterNickMC.split("@")[1], 2)
            add_rooster_comment_response(idx,"mc","{color=#00a0e6}@%s{/color} I get it. You wanted me for yourself." % roosterNickSally.split("@")[1], 3)
            add_rooster_comment_response(idx,"sally","{color=#00a0e6}@%s{/color} Haha! No! I wanted you to work. GRRR!" % roosterNickMC.split("@")[1], 2)
        elif mroosterChoices[idx][0] == 2:
            mroosterHistory_likes[idx].append(2)
            add_rooster_comment_response(idx,"nikita","{color=#00a0e6}@%s{/color} Stalker alert." % roosterNickMC.split("@")[1], 1)
            add_rooster_comment_response(idx,"mc","{color=#00a0e6}@%s{/color} Said the one who had already been following me. I see you." % roosterNickNikita.split("@")[1], 2)
            add_rooster_comment_response(idx,"nikita","{color=#00a0e6}@%s{/color} Uh-oh! Busted! O_O" % roosterNickMC.split("@")[1], 1)
        
        return

    def rooster_append_reply_mc_ep12(idx):
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
            mroosterHistory_likes[idx].append(50)
        elif mroosterChoices[idx][0] == 2:
            mroosterHistory_likes[idx].append(45)
            add_rooster_comment_response(idx,"mia","{color=#00a0e6}@%s{/color} I'll give you a follow then. I would love to see it." % roosterNickMC.split("@")[1], 11)
            add_rooster_comment_response(idx,"erin","{color=#00a0e6}@%s{/color} I thought you already followed him." % roosterNickMia.split("@")[1], 4)
            add_rooster_comment_response(idx,"mia","{color=#00a0e6}@%s{/color} Shush!" % roosterNickErin.split("@")[1], 5)
        return
    def rooster_append_reply_diks2_ep12(idx):
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
            mroosterHistory_likes[idx].append(3)
            add_rooster_comment_response(idx,"derek","{color=#00a0e6}@%s{/color} Dammit... Ok. The glasses sucked. They were fun for like a minute, and after that, the joke became you. I had to ditch them." % roosterNickMC.split("@")[1], 2)
            add_rooster_comment_response(idx,"mc","{color=#00a0e6}@%s{/color} I'll gladly collect the $1000 at your convenience." % roosterNickDerek.split("@")[1], 3)
            add_rooster_comment_response(idx,"derek","{color=#00a0e6}@%s{/color} We said $10." % roosterNickMC.split("@")[1], 2)
            add_rooster_comment_response(idx,"mc","{color=#00a0e6}@%s{/color} Sure. Now you remember..." % roosterNickDerek.split("@")[1], 4)
        elif mroosterChoices[idx][0] == 2:
            mroosterHistory_likes[idx].append(3)
            add_rooster_comment_response(idx,"chen","{color=#00a0e6}@%s{/color} Sorry! My mistake!" % roosterNickMC.split("@")[1], 2)
            add_rooster_comment_response(idx,"marc","{color=#00a0e6}@%s{/color} So, I'm in?" % roosterNickMC.split("@")[1], 2)
            add_rooster_comment_response(idx,"mc","{color=#00a0e6}@%s{/color} Sigh..." % roosterNickMarc.split("@")[1], 3)
            add_rooster_comment_response(idx,"marc","{color=#00a0e6}@%s{/color} ???" % roosterNickMC.split("@")[1], 1)
        return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
