init python:


    def rooster_append_reply_ashley_ep7(idx):
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
            mroosterHistory_likes[idx].append(11)
            add_rooster_comment_response(idx,"ashley","{color=#00a0e6}@%s{/color} Thanks!" % roosterNickMC.split("@")[1], 1)
        elif mroosterChoices[idx][0] == 2:
            mroosterHistory_likes[idx].append(3)
            add_rooster_comment_response(idx,"melanie","{color=#00a0e6}@%s{/color} What an overused pun!"  % roosterNickMC.split("@")[1], 8)
            add_rooster_comment_response(idx,"ashley","{color=#00a0e6}@%s{/color} Haha! Even I've heard it too many times by now."  % roosterNickMelanie.split("@")[1], 5)
            add_rooster_comment_response(idx,"lily","Yeah, too much cheese on that comment for me.", 7)
            add_rooster_comment_response(idx,"jimmy","{color=#00a0e6}@alphas{/color} Lol, what a loser.", 8)
        return

    def rooster_append_reply_jimmy_ep7(idx):
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
            mroosterHistory_likes[idx].append(9)
            add_rooster_comment_response(idx,"dawe","{color=#00a0e6}@%s{/color} Fuck you! I'm not jacking off. I needed to scratch it and Jimmy's got shit timing with the pic!" % roosterNickMC.split("@")[1], 4)
            add_rooster_comment_response(idx,"jimmy","{color=#00a0e6}@%s{/color} Don't blame me. When's your hand not on your dick, brah?" % roosterNickDawe.split("@")[1], 3)
            add_rooster_comment_response(idx,"alex","{color=#00a0e6}@%s{/color} Jimmy's got a point. It's either on your dick or in your face with the fingers in your nose." % roosterNickDawe.split("@")[1], 3)
            add_rooster_comment_response(idx,"dawe","{color=#00a0e6}@%s{/color} Shut up!" % roosterNickAlex.split("@")[1], 1)
            add_rooster_comment_response(idx,"caleb","{color=#00a0e6}@%s{/color} I'm watching you. Keep talking shit and find out what happens." % roosterNickMC.split("@")[1], 8)
        elif mroosterChoices[idx][0] == 2:
            mroosterHistory_likes[idx].append(8)
            add_rooster_comment_response(idx,"dawe","{color=#00a0e6}@%s{/color} Hahaha! If that's what you think, then you're the gay one! Why are you even looking at this pic?"  % roosterNickMC.split("@")[1], 7)
            add_rooster_comment_response(idx,"jimmy","{color=#00a0e6}@%s{/color} LOL! Fucking got him!"  % roosterNickDawe.split("@")[1], 4)
            add_rooster_comment_response(idx,"anthony","No one got their ass fucked last night. Right, guys? And pegging doesn't count.", 4)
            add_rooster_comment_response(idx,"alex","{color=#00a0e6}@%s{/color} I fucking hate this guy."  % roosterNickMC.split("@")[1], 5)
            add_rooster_comment_response(idx,"caleb","{color=#00a0e6}@%s{/color} I'm watching you. Keep talking shit and find out what happens." % roosterNickMC.split("@")[1], 8)
        return

    def rooster_append_reply_leon_ep7(idx):
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
            mroosterHistory_likes[idx].append(15)
            add_rooster_comment_response(idx,"tommy","Ah, yeah! Cleaning the pole. That and \"pole cheeks\" are his trademark moves.",18)
            add_rooster_comment_response(idx,"envy","Hahah!",3)
            add_rooster_comment_response(idx,"rose","{color=#00a0e6}@%s{/color} Ok, now I'm intrigued! What's pole cheeks?"  % roosterNickTommy.split("@")[1], 8)
            add_rooster_comment_response(idx,"tommy","{color=#00a0e6}@%s{/color} It's just like it sounds. He inserts the pole between his cheeks and clenches hard. [name] puts a twist on it by lifting his legs to demonstrate the power of his buttocks."  % roosterNickRose.split("@")[1], 13)
            add_rooster_comment_response(idx,"lily","{color=#00a0e6}@%s{/color} Nice try, Tommy. But that's actually not far off from a real move."  % roosterNickTommy.split("@")[1], 5)
            add_rooster_comment_response(idx,"rose","{color=#00a0e6}@%s{/color} Very nice! Lol!"  % roosterNickTommy.split("@")[1], 8)
        elif mroosterChoices[idx][0] == 2:
            mroosterHistory_likes[idx].append(7)
            add_rooster_comment_response(idx,"leon","{color=#00a0e6}@%s{/color} Sorry, brother. It had to be done. It's so funny!"  % roosterNickMC.split("@")[1], 10)
            add_rooster_comment_response(idx,"tommy","{color=#00a0e6}@%s{/color} Luckily for you, most seem to approve of your pastime activity. You can catch [name] on stage Mondays and Thursdays. Bring a raincoat. You will get wet in one way or another."  % roosterNickMC.split("@")[1], 12)
            add_rooster_comment_response(idx,"camila","{color=#00a0e6}@%s{/color} Is that why there's a spray bottle in the photo?"  % roosterNickTommy.split("@")[1], 6)
            add_rooster_comment_response(idx,"quinn","This guy is kinkier than I thought.",8)
            add_rooster_comment_response(idx,"riona","{color=#00a0e6}@%s{/color} Ikr?"  % roosterNickQuinn.split("@")[1], 6)
            add_rooster_comment_response(idx,"elena","You guys are a bunch of bullies.",4)
            add_rooster_comment_response(idx,"ashley","This is too funny!",5)
        elif mroosterChoices[idx][0] == 3:
            mroosterHistory_likes[idx].append(13)
            add_rooster_comment_response(idx,"riona","{color=#00a0e6}@%s{/color} Sounds expensive and exotic at the same time."  % roosterNickMC.split("@")[1], 3)
            add_rooster_comment_response(idx,"lily","If Stanley saw this, he'd be so mad. Haha!",6)
            add_rooster_comment_response(idx,"envy","{color=#00a0e6}@%s{/color} Definitely! He still groans about the last time."  % roosterNickLily.split("@")[1], 5)
            add_rooster_comment_response(idx,"rose","{color=#00a0e6}@%s{/color} Good luck getting into an empty private room."  % roosterNickMC.split("@")[1], 5)
            add_rooster_comment_response(idx,"quinn","This guy is kinkier than I thought.",8)
            add_rooster_comment_response(idx,"riona","{color=#00a0e6}@%s{/color} Ikr?"  % roosterNickQuinn.split("@")[1], 6)
        return

    def rooster_append_reply_derek_ep7(idx):
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
            mroosterHistory_likes[idx].append(12)
            add_rooster_comment_response(idx,"derek","{color=#00a0e6}@%s{/color} Maggot brothers for life."  % roosterNickMC.split("@")[1], 8)
        elif mroosterChoices[idx][0] == 2:
            mroosterHistory_likes[idx].append(21)
            add_rooster_comment_response(idx,"elena","{color=#00a0e6}@%s{/color} Yes! You should be proud."  % roosterNickMC.split("@")[1], 7)
            add_rooster_comment_response(idx,"lily","{color=#00a0e6}@%s{/color} It's such a great thing you're doing. You can always visit the club another time."  % roosterNickMC.split("@")[1], 10)
        if mroosterChoices[idx][0] == 1 or mroosterChoices[idx][0] == 2:
            add_rooster_comment("riona","{color=#00a0e6}@%s{/color} I have no clue what's going on in this pic, but I think it looks sweet." % roosterNickDerek.split("@")[1],17)
            add_rooster_comment("arieth","{color=#00a0e6}@%s{/color} I'm tired of doing your dirty laundry! It's not fair that I have to check if I can wash your white undies with my white clothes because of this problem." % roosterNickDawe.split("@")[1],8)
            add_rooster_comment("sarah","{color=#00a0e6}@%s{/color} This is absolutely disgusting. Tell us more." % roosterNickArieth.split("@")[1],4)
            add_rooster_comment("melanie","{color=#00a0e6}@%s{/color} Eww! We share that washing machine!" % roosterNickArieth.split("@")[1],2)
            add_rooster_comment("arieth","{color=#00a0e6}@%s{/color} This one time, Dawe was on a keto diet and only ate like fatty food to burn more fat. I don't know how it works, and I think he doesn't know either because he like literally ended up gaining weight." % roosterNickSarah.split("@")[1],8)
            add_rooster_comment("arieth","{color=#00a0e6}@%s{/color} And his farts smelled really bad! Normally, I don't mind them, but this time it was horrible!" % roosterNickSarah.split("@")[1],7)
            add_rooster_comment("dawe","{color=#00a0e6}@%s{/color} Answer when I'm calling you!" % roosterNickArieth.split("@")[1],4)
            add_rooster_comment("arieth","{color=#00a0e6}@%s{/color} And I just knew that I would have to wash his underwear with the colored clothes without even looking." % roosterNickSarah.split("@")[1],5)
        return

    def rooster_append_reply_sage_ep7(idx):
        global mroosterChoices
        global mroosterHistory_text
        global mroosterHistory_avatars
        global mroosterHistory_liked
        global mroosterHistory_likes
        global ep7_becky_lewd
        global ep7_rica_lewd
        global assman
        global ep7_lily_lewd
        global ep6_quinn_lewd
        
        mroosterHistory_text[idx].append(mroosterChoices[idx][mroosterChoices[idx][0]])
        mroosterHistory_avatars[idx].append(mc_avatar)
        mroosterHistory_nicknames[idx].append(roosterNickMC)
        mroosterHistory_liked[idx].append(False)
        
        if mroosterChoices[idx][0] == 1:
            mroosterHistory_likes[idx].append(12)
            add_rooster_comment_response(idx,"sage","{color=#00a0e6}@%s{/color} Thanks!"  % roosterNickMC.split("@")[1], 5)
        elif mroosterChoices[idx][0] == 2:
            mroosterHistory_likes[idx].append(7)
            add_rooster_comment_response(idx,"sage","{color=#00a0e6}@%s{/color} Haha, I'm open to suggestions."  % roosterNickMC.split("@")[1], 7)
            add_rooster_comment_response(idx,"jacob","{color=#00a0e6}@%s{/color} We miss you, girls."  % roosterNickSage.split("@")[1], 10)
        elif mroosterChoices[idx][0] == 3:
            mroosterHistory_likes[idx].append(4)
            if ep6_quinn_lewd:
                add_rooster_comment_response(idx,"quinn","{color=#00a0e6}@%s{/color} It's cool. Ask next time, though."  % roosterNickMC.split("@")[1], 1)
            else:
                add_rooster_comment_response(idx,"quinn","{color=#00a0e6}@%s{/color} So, you're both a pervert and a fucking thief?"  % roosterNickMC.split("@")[1], 3)
            if ep7_lily_lewd:
                add_rooster_comment_response(idx,"lily","{color=#00a0e6}@%s{/color} Do you drink absinthe? Interesting... Also, I hope you're still thinking about what we talked about."  % roosterNickMC.split("@")[1], 2)
            else:
                add_rooster_comment_response(idx,"lily","{color=#00a0e6}@%s{/color} Now it makes sense."  % roosterNickMC.split("@")[1], 3)
        if mroosterChoices[idx][0] > 0:
            if ep7_becky_lewd:
                add_rooster_comment_response(idx,"becky","{color=#00a0e6}@%s{/color} Hey, you..."  % roosterNickMC.split("@")[1], 2)
            if ep7_rica_lewd:
                add_rooster_comment_response(idx,"riona","{color=#00a0e6}@%s{/color} *Pokes you*"  % roosterNickMC.split("@")[1], 1)
                if assman:
                    add_rooster_comment_response(idx,"camila","{color=#00a0e6}@%s{/color} Ass man! Haha!"  % roosterNickMC.split("@")[1], 5)
                    add_rooster_comment_response(idx,"riona","{color=#00a0e6}@%s{/color} HAHAH!"  % roosterNickCamila.split("@")[1], 2)
            if ep7_lily_lewd and mroosterChoices[idx][0] != 3:
                add_rooster_comment_response(idx,"lily","{color=#00a0e6}@%s{/color} Still thinking about it, I hope."  % roosterNickMC.split("@")[1], 1)
        return

    def rooster_append_reply_mc_ep7(idx):
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
            add_rooster_comment_response(idx,"quinn","{color=#00a0e6}@%s{/color} Not yet."  % roosterNickMC.split("@")[1], 3)
        elif mroosterChoices[idx][0] == 2:
            mroosterHistory_likes[idx].append(7)
            add_rooster_comment_response(idx,"quinn","{color=#00a0e6}@%s{/color} Aha... I'll remember that."  % roosterNickMC.split("@")[1], 3)
        return

    def rooster_append_reply_isabella_ep7(idx):
        global mroosterChoices
        global mroosterHistory_text
        global mroosterHistory_avatars
        global mroosterHistory_liked
        global mroosterHistory_likes
        global ep7_pinkrose
        
        mroosterHistory_text[idx].append(mroosterChoices[idx][mroosterChoices[idx][0]])
        mroosterHistory_avatars[idx].append(mc_avatar)
        mroosterHistory_nicknames[idx].append(roosterNickMC)
        mroosterHistory_liked[idx].append(False)
        
        if mroosterChoices[idx][0] == 1:
            mroosterHistory_likes[idx].append(1)
            add_rooster_comment_response(idx,"isabella","{color=#00a0e6}@%s{/color} Go fish."  % roosterNickMC.split("@")[1], 0)
            add_rooster_comment_response(idx,"mc","{color=#00a0e6}@%s{/color} Haha!"  % roosterNickIsabella.split("@")[1], 1)
        elif mroosterChoices[idx][0] == 2:
            mroosterHistory_likes[idx].append(1)
            add_rooster_comment_response(idx,"isabella","{color=#00a0e6}@%s{/color} Smart-ass."  % roosterNickMC.split("@")[1], 1)
        elif mroosterChoices[idx][0] == 3:
            mroosterHistory_likes[idx].append(1)
            if ep7_pinkrose:
                add_rooster_comment_response(idx,"isabella","{color=#00a0e6}@%s{/color} Yeah, I have to work on that. Maybe the cage dancer could give me some advice?"  % roosterNickMC.split("@")[1], 1)
            else:
                add_rooster_comment_response(idx,"isabella","{color=#00a0e6}@%s{/color} Yeah, I have to work on that."  % roosterNickMC.split("@")[1], 0)
        return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
