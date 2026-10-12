label lb_ep02_02_01_The_MC_returns_home_Vivian_waits_for_him:
    #SCENE BEGINS

    #the scene begins with Vivian in the bathroom, wearing a long robe, and the red lingerie that she stole from the art theatre - ask Dots about this if you're unsure
    #make sure we can't see what she's wearing underneath her robe

    "Meanwhile, back at the house..."
    #show a blank screen here with this written on it
    #Vivian at the house

    scene sc mcbackhomef 002
    with dissolve
    v"(Sigh...)"
    #Vivian looks worried

    v"([y_name] isn't home yet, and he hasn't returned any of my calls or messages.)"
    #she turns her head slightly, staring at nothing specific

    show sc mcbackhomef 003
    v"(I really hope nothing bad has happened to him.)"
    #she looks concerned

    show sc mcbackhomef 004
    v"(If he's still out looking for that drive, I need to help buy him some more time.)"
    #a slightly different render to the one above
    play music "sound effects/01/Velvet Touch1.mp3" loop fadein 1.0
    show sc mcbackhomef 005
    v"(Perhaps I could do that by calming [vic_name] down...)"
    #she reaches for the binds to her robe: make it look like she's tightening it

    show sc mcbackhomef 001
    with dissolve
    v"(Okay, it's showtime...)"

    #the screen goes blank
    show sc mcbackhomef 006
    with dissolve
    pause 1.0
    #Vivian comes out of the bathroom and enters the bedroom where Victor lays on the bed, looking at his phone
    #Victor is still wearing casual clothing - he needs to be as he will leave the house after this scene ends
    show sc mcbackhomef 007
    with dissolve
    v"Honey?"
    show sc mcbackhomef 006
    vic"Hmm?"
    #he keeps staring at his phone
    show sc mcbackhomef 008
    with dissolve
    vic"Oh... What do you want?"
    #He looks up at her
    show sc mcbackhomef 009
    v"I was just thinking..."
    #Vivian starts to play the seductress
    show sc mcbackhomef 010
    v"It's been a while since you and I... Fooled around."
    #she makes her legs the focus

    show sc mcbackhomef 011
    v"And I thought that tonight would be a good way for us to ease some tension."
    #she turns around so she can show off her ass, with her looking over her shoulder

    show sc mcbackhomef 012
    v"To let off some steam."
    stop music fadeout 1.0

    show sc mcbackhomef 013
    vic"Are you serious?"
    #Victor looks up at her

    show sc mcbackhomef 014
    v"Um, yeah... Why wouldn't I be?"

    show sc mcbackhomef 008
    vic"We're in the middle of a crisis right now, [v_name]."
    #Victor looks back at his phone

    show sc mcbackhomef 013
    vic"And it's all because of that kid."
    #same images as above but he's slightly more angry
    vic"Yet, you don't want to even focus on it."
    #reuse the same render

    show sc mcbackhomef 017
    v"Why do you treat me so badly?"
    show sc mcbackhomef 018
    v"What have I done to deserve any of this?"

    show sc mcbackhomef 019
    vic"Ughh... It's always about you, isn't it?"

    show sc mcbackhomef 020
    vic"You know, if you put more time and energy into the good of this [private_group], rather than your own selfish agenda..."
    vic"Then we wouldn't have any of the problems we currently have."

    show sc mcbackhomef 021
    v"What on earth are you talking about?"

    show sc mcbackhomef 022
    v"What is going on with you?"

    show sc mcbackhomef 023
    vic"I can't listen to this."

    show sc mcbackhomef 024
    vic"I'm leaving."

    show sc mcbackhomef 025
    v"Where are you going?"

    show sc mcbackhomef 026
    vic"OUT!"
    show sc mcbackhomef 027
    vic"To a bar, to a club... Wherever the night takes me."

    show sc mcbackhomef 028
    vic"Because quite frankly, doing just about anything else is more enjoyable than staying here talking to you."

    show sc mcbackhomef 029
    vic"Don't wait up, as I won't be back any time soon..."
    #show an upset Vivian watching Victor leave the room
    #screen goes blank
    scene black
    with dissolve
    scene black
    with Pause (2)

    show sc mcbackhomef 030
    with dissolve
    pause 1.0
    #scene returns with Vivian sitting on the floor of the bathroom, crying
    play music "sound effects/01/Family_Ties1.mp3" loop
    show sc mcbackhomef 031
    with dissolve
    v"(I don't get it... I don't understand him anymore.)"
    show sc mcbackhomef 032
    v"(I do so much for our [private_group], yet he treats me like I don't even exist.)"

    show sc mcbackhomef 033
    v"(And I didn't even get to show off the surprise that I had for him.)"
    #Vivian looks down at her robe

    show sc mcbackhomef 034
    with dissolve
    v"(I don't think I could feel any worse than I do right now.)"
    #Vivian looks at her phone

    show sc mcbackhomef 035
    v"(And I haven't heard back from [y_name], which is starting to worry me even more.)"
    show sc mcbackhomef 036
    with dissolve
    v"(I won't be able to go to sleep until I know he's home safe...)"
    stop music fadeout 1.0
    #screen goes blank
    scene black
    with dissolve
    scene black
    with Pause (2)

    play ambient "sound effects/01/Night_Time_Sound_FX.ogg" loop fadein 1.0
    show sc mcbackhomef 037
    #The scene continues with the MC arriving back at the front door - all the lights are off
    with dissolve
    mc"(Okay, so I'm back a little late, and after curfew.)"
    mc"(But I'm sure everything will be fine, now that I've got the drive back.)"
    #The MC opens the front door with his key and enters
    stop ambient fadeout 1.0
    show sc mcbackhomef 039
    with fast_dissolve
    mc"(Hmm... Everyone must be asleep.)"
    show sc mcbackhomef 040
    v"[y_name]?"
    #Vivian is in the living room and is watching him
    show sc mcbackhomef 041
    mc"[mc_v_address!c]?"
    play music "sound effects/02/Secret Love.mp3" loop fadein 1.0
    if not persistent.v_sex_anim_enabled_locked and persistent.v_sex_anim_enabled:
        scene sc mcbackhomef 042 at tt_top
        pause
    elif True:
        scene sc mcbackhomef 042
    #ROLLING IMAGE OF VIVIAN IN HER ROBE - SHOWING OFF HER LEGS
    mc"(Damn... She never ceases to amaze.)"
    mc"What are you still doing up?"
    scene sc mcbackhomef 045
    v"I was waiting for you. I was worried that something bad may have happened."
    #She puts her arm around him

    show sc mcbackhomef 046
    v"Are you okay my boy? Are you hurt?"

    show sc mcbackhomef 047
    mc"I'm fine, truly."

    show sc mcbackhomef 048
    v"Is that a bruise on the side of your face?"
    #she turns his face to look at his right cheek

    show sc mcbackhomef 049
    mc"No, it's nothing."

    show sc mcbackhomef 050
    v"Well, I'm glad that you're okay."

    show sc mcbackhomef 052
    mc"Where's [mc_vic_address]?"

    show sc mcbackhomef 053
    v"He took off."

    show sc mcbackhomef 054
    v"We had a huge fight."
    v"He was upset with me because he thinks I've been too soft with you."

    show sc mcbackhomef 055
    v"He wanted to shut you out of the next heist he has planned and I told him that it wasn't fair."

    show sc mcbackhomef 056
    mc"Oh, [mc_v_address!c]..."

    show sc mcbackhomef 057
    mc"I'm sorry this happened."

    show sc mcbackhomef 054
    mc"You didn't need to do that."

    show sc mcbackhomef 059
    v"I was just trying to buy you some more time so you could get that flash drive."

    show sc mcbackhomef 060
    mc"Well, I have some good news."
    show sc mcbackhomef 061
    with dissolve
    mc"Look."
    #The MC reaches into his pocket and shows her the drive

    show sc mcbackhomef 062
    v"Oh my God! You got it!"

    show sc mcbackhomef 063
    v"But how?"
    mc"I had a good lead, and followed my instincts, just like you taught me when I was a kid."

    show sc mcbackhomef 065
    v"Aww... Come here."

    show sc mcbackhomef 066
    v"Mmm... I'm so happy that you're safe."
    #they hug

    show sc mcbackhomef 067
    mc"But wasn't I supposed to have the drive back by midnight?"

    show sc mcbackhomef 068
    v"I thought so too, but [vic_name] said that you have until tomorrow morning."

    show sc mcbackhomef 069
    mc"Really?"

    show sc mcbackhomef 068
    v"Yeah, so you got it back with plenty of time to spare."

    show sc mcbackhomef 067
    mc"Awesome."

    show sc mcbackhomef 070
    v"Come, let's talk some more in the living room..."
    #screen goes blank
    scene black
    with dissolve
    scene black
    with Pause (2)

    #the MC and Vivian sit on the sofa, in a slightly dimmed room
    show sc mcbackhomef 071
    with dissolve
    mc"So I have to ask, were you crying before I got home?"

    show sc mcbackhomef 073
    v"It's okay, sweetheart. It's nothing for you to worry about."

    show sc mcbackhomef 074
    mc"Come on, it's not nothing [mc_v_address!c]."

    show sc mcbackhomef 075
    mc"You said that you and [mc_vic_address] had a fight before he left."
    show sc mcbackhomef 076
    mc"It wasn't just about me, was it?"

    show sc mcbackhomef 077
    v"No..."

    show sc mcbackhomef 078
    mc"Well, what then? I want to know."

    show sc mcbackhomef 079
    v"All right, fine... I'll tell you. But don't say I didn't warn you."

    show sc mcbackhomef 080
    v"[vic_name] doesn't find me attractive any more. He doesn't look at me like he used to."

    show sc mcbackhomef 081
    v"I try so hard to please him and to keep some kind of flame burning in our relationship, but every time I do, he puts the fire out."

    show sc mcbackhomef 077
    v"There, are you happy now?"

    show sc mcbackhomef 082
    mc"No, not at all."
    show sc mcbackhomef 078
    with dissolve
    mc"I really wish I could have been here for you, [mc_v_address!c]."

    show sc mcbackhomef 084
    v"Thanks, but maybe he's right."

    show sc mcbackhomef 085
    mc"What do you mean?"

    show sc mcbackhomef 086
    v"Isn't it obvious, sweetheart?"

    show sc mcbackhomef 084
    v"I'm on the wrong side of forty, and my best years are already behind me."

    show sc mcbackhomef 087
    v"Besides, who on earth would want this?"
    #Vivian stands up in front of the MC and undoes her robe

    #ANIMATED SCENE OF VIVIAN UNDOING HER ROBE AND IT FALLS TO THE FLOOR


    if v_ep01_day3_vivian_dress == "black":
        if not persistent.v_sex_anim_enabled_locked and persistent.v_sex_anim_enabled:
            scene sc mcbackhomef 088 at tt_top
            pause
        elif True:
            show sc mcbackhomef 119
            with dissolve

        #ROLLING IMAGE OF VIVIAN IN HER NEGLIGEE
        mc"(Woah...)"
        scene sc mcbackhomef 089
        mc"(After everything I've been through tonight, this a surprise to come home to.)"


        #[Go upstairs / Say something nice]

        menu:
            "Go upstairs":
                #The MC separates from Vivian
                show sc mcbackhomef 093
                mc"(However, I shouldn't be seen talking with her like this, just in case [vic_name] happens to come home.)"
                show sc mcbackhomef 094
                mc"You look great for your age, [mc_v_address!c]."
                show sc mcbackhomef 092
                mc"And don't worry about what anybody else thinks."
                show sc mcbackhomef 095
                mc"That's what you told me when I was younger, remember?"
                show sc mcbackhomef 097
                v"Thanks, sweetheart. You grew up better than I could have hoped for."
                show sc mcbackhomef 096
                mc"And that's mainly because of you."
                show sc mcbackhomef 091
                mc"Anyway, it's been a long day, so I'm probably gonna have a shower and then go to bed."
                show sc mcbackhomef 098
                v"Sure thing, [y_name]."


                stop music fadeout 1.0

                #Go down to SCENE CONTINUES

            "Say something back" (wt="Best option + Bonus image"):

                show sc mcbackhomef 090
                mc"([mc_vic_address] has definitely missed out!)"
                $ rewards_unlock ("vivian",11)
                show sc mcbackhomef 093
                mc"(She really needs to hear this.)"


                menu:
                    "Compliment her"(wt="Bonus Image"):
                        show sc mcbackhomef 094
                        mc"You look amazing, [mc_v_address!c]!"

                        show sc mcbackhomef 095
                        mc"And you shouldn't be so critical of yourself."
                        $ rewards_unlock ("vivian",12)
                        show sc mcbackhomef 094
                        mc"[mc_vic_address!c] is a fool for not being here to see you like this."
                        stop music fadeout 1.0
                        show sc mcbackhomef 097
                        v"Thanks, sweetheart. That's so nice of you to say."
                        play music "sound effects/01/Velvet Touch2.mp3" loop fadein 1.0
                        show sc mcbackhomef 098
                        v"You know, it's a little dim in this room."

                        show sc mcbackhomef 099
                        v"Stand up and take a closer look."

                        mc"Um... Okay."

                        show sc mcbackhomef 100
                        with dissolve
                        mc"Yeah, it really does suit you."
                        #The MC stands before Vivian, looking at her lingerie
                        show sc mcbackhomef 101
                        mc"Where did you get it from?"
                        show sc mcbackhomef 102
                        v"I stole it from the acting theatre the other day while you were performing in front of the teacher."
                        show sc mcbackhomef 102a
                        mc"Oh yeah, don't remind me."
                        #the MC rolls his eyes
                        show sc mcbackhomef 104
                        v"Thank you for the compliment, sweetheart."
                        show sc mcbackhomef 105
                        v"You always know the right things to say to cheer me up."

                        show sc mcbackhomef 106
                        mc"You're welcome."
                        #Vivian hugs the MC

                        show sc mcbackhomef 107
                        v"Mmm..."
                        #show her breasts pressed up against his chest
                        show sc mcbackhomef 108
                        v"I really do miss you when you're not here, you know?"

                        show sc mcbackhomef 107
                        mc"(She's hugging me tighter than normal.)"
                        show sc mcbackhomef 110
                        mc"(And if I didn't know any better, I'd say she's grinding herself against me.)"
                        #show their hips pressed together

                        show sc mcbackhomef 111
                        pause 1.0
                        #She leans back from the hug, but they still hold each other and look into each other's eyes

                        show sc mcbackhomef 112
                        with dissolve
                        #Vivian looks down and sees the tent shape in his pants
                        v"(Oh my...)"
                        show sc mcbackhomef 113
                        v"(It feels like he's a {b}huge{/b} fan of my choice of lingerie.)"
                        show sc mcbackhomef 114
                        v"(Perhaps I could reward him for that. But how?)"
                        #She looks the MC in the eyes
                        show sc mcbackhomef 115
                        mc"[mc_v_address!c]?"
                        show sc mcbackhomef 116
                        v"Yes, [y_name]?"
                        stop music fadeout 1.0
                        #she has a sexy little smirk on her face
                        #Go Down to SCENE CONTINUES

                    "Talk her up"(wt="Bonus image"):
                        show sc mcbackhomef 118
                        mc"You look drop-dead sexy, [mc_v_address!c]!"
                        show sc mcbackhomef 097
                        mc"You know, I think you could be the sole reason for global warming."
                        $ rewards_unlock ("vivian",13)
                        stop music fadeout 1.0
                        show sc mcbackhomef 119
                        mc"And I mean that as a good thing."
                        #Vivian smiles
                        play music "sound effects/01/Velvet Touch2.mp3" loop fadein 1.0
                        show sc mcbackhomef 120
                        v"So, you're saying that you think I'm hot?"
                        #Vivian looks at the MC seductively
                        show sc mcbackhomef 102
                        mc"Uh, yeah... I guess I am."
                        show sc mcbackhomef 095
                        mc"And [mc_vic_address!c] is a fool for not being here to see you like this."

                        show sc mcbackhomef 121
                        v"Thanks, sweetheart. I actually prefer that you're here instead of him right now."

                        show sc mcbackhomef 119
                        mc"Yeah, me too."

                        show sc mcbackhomef 098
                        v"You know, it's a little dim in this room."

                        show sc mcbackhomef 099
                        v"Stand up and take a closer look."

                        mc"Um... Okay."

                        show sc mcbackhomef 100
                        with dissolve
                        mc"Yeah, it really does suit you."
                        #The MC stands before Vivian, looking at her lingerie

                        show sc mcbackhomef 101
                        mc"Where did you get it from?"

                        show sc mcbackhomef 102
                        v"I stole it from the acting theatre the other day while you were performing in front of the teacher."

                        mc"Oh yeah, don't remind me."
                        #the MC rolls his eyes

                        show sc mcbackhomef 104
                        v"Thank you for the compliment, sweetheart."
                        show sc mcbackhomef 105
                        v"You always know the right things to say to cheer me up."

                        show sc mcbackhomef 106
                        mc"You're welcome."
                        #Vivian hugs the MC

                        show sc mcbackhomef 107
                        v"Mmm..."
                        #show her breasts pressed up against his chest
                        show sc mcbackhomef 108
                        v"I really do miss you when you're not here, you know?"

                        show sc mcbackhomef 107
                        mc"(She's hugging me tighter than normal.)"
                        show sc mcbackhomef 110
                        mc"(And if I didn't know any better, I'd say she's grinding herself against me.)"
                        #show their hips pressed together

                        show sc mcbackhomef 111
                        pause 1.5
                        #She leans back from the hug, but they still hold each other and look into each other's eyes

                        show sc mcbackhomef 112
                        with dissolve
                        #Vivian looks down and sees the tent shape in his pants
                        v"(Oh my...)"
                        show sc mcbackhomef 113
                        with dissolve
                        v"(It feels like he's a {b}huge{/b} fan of my choice of lingerie.)"
                        show sc mcbackhomef 114
                        v"(Perhaps I could reward him for that. But how?)"
                        #She looks the MC in the eyes

                        show sc mcbackhomef 115
                        mc"[mc_v_address!c]?"

                        show sc mcbackhomef 116
                        v"Yes, [y_name]?"
                        stop music fadeout 1.0
                        #she has a sexy little smirk on her face
                        #Go Down to SCENE CONTINUES


                    "Criticise [vic_name]"(wt="Best option + Bonus image"):
                        #BEST OPTION - Vivian points or bonus renders
                        show sc mcbackhomef 095
                        mc"I'm sorry, [mc_v_address!c], but [mc_vic_address] is a moron if he can't see how insanely attractive you still are."
                        show sc mcbackhomef 118
                        mc"You look {b}smoking{/b} hot in that!"
                        $ rewards_unlock ("vivian",14)
                        show sc mcbackhomef 120
                        v"Oh, thank you, sweetheart. I don't know what else to say."
                        stop music fadeout 1.0
                        show sc mcbackhomef 119
                        v"(Wow... It was so nice to hear that.)"
                        v"(I suddenly feel a lot sexier wearing this in front of him.)"
                        play music "sound effects/01/Velvet Touch2.mp3" loop fadein 1.0
                        show sc mcbackhomef 098
                        v"You know, it's a little dim in this room."

                        show sc mcbackhomef 099
                        v"Stand up and take a closer look."

                        mc"Um... Okay."

                        show sc mcbackhomef 100
                        with dissolve
                        mc"Yeah, it really does suit you."
                        #The MC stands before Vivian, looking at her lingerie

                        show sc mcbackhomef 101
                        mc"Where did you get it from?"

                        show sc mcbackhomef 102
                        v"I stole it from the acting theatre the other day while you were performing in front of the teacher."

                        mc"Oh yeah, don't remind me."
                        #the MC rolls his eyes

                        show sc mcbackhomef 104
                        v"Thank you for the compliment, sweetheart."
                        show sc mcbackhomef 105
                        v"You always know the right things to say to cheer me up."

                        show sc mcbackhomef 106
                        mc"You're welcome."
                        #Vivian hugs the MC

                        show sc mcbackhomef 107
                        v"Mmm..."
                        #show her breasts pressed up against his chest
                        show sc mcbackhomef 108
                        v"I really do miss you when you're not here, you know?"

                        show sc mcbackhomef 107
                        mc"(She's hugging me tighter than normal.)"
                        show sc mcbackhomef 110
                        mc"(And if I didn't know any better, I'd say she was grinding herself against me.)"
                        #show their hips pressed together

                        show sc mcbackhomef 111
                        pause 1.5
                        #She leans back from the hug, but they still hold each other and look into each other's eyes

                        show sc mcbackhomef 112
                        with dissolve
                        #Vivian looks down and sees the tent shape in his pants
                        v"(Oh my...)"
                        show sc mcbackhomef 113
                        v"(It feels like he's a {b}huge{/b} fan of my choice of lingerie.)"
                        show sc mcbackhomef 114
                        v"(Perhaps I could reward him for that. But how?)"
                        #She looks the MC in the eyes

                        show sc mcbackhomef 115
                        mc"[mc_v_address!c]?"

                        show sc mcbackhomef 116
                        v"[y_name]..."
                        #she has a sexy little smirk on her face

                        show sc mcbackhomef 122
                        v"I have something for you."
                        #Vivian leans forward and kisses the MC, they both close their eyes
                        play sound "sound effects/01/kiss_and_moan_sound_effect01.mp3" loop fadein 1.0
                        show sc mcbackhomef 123
                        with dissolve
                        pause 1.0
                        v"Mmm..."

                        show sc mcbackhomef 124
                        mc"(Oh wow!)"
                        #ANIMATION OF THEM KISSING - ZOOMED OUT SHOT

                        show sc mcbackhomef 125
                        v"(This feels so good, so naughty...)"
                        #her eyes are still closed as they makeout
                        stop sound fadeout 1.0
                        stop music fadeout 1.0
                        play sound "sound effects/01/record_scratch.ogg" noloop
                        show sc mcbackhomef 126
                        with vpunch
                        v"(Wait!)"
                        v"(What the hell am I doing??)"
                        #Her eyes shoot open when she thinks this

                        show sc mcbackhomef 127
                        with dissolve
                        mc"[mc_v_address!c]??"
                        #Vivian looks away

                        show sc mcbackhomef 129
                        mc"Why did you kiss me?"
                        show sc mcbackhomef 130
                        v"I'm sorry, sweetheart... I don't know what came over me."
                        v"I think for a moment there, I thought I was kissing [vic_name]."
                        show sc mcbackhomef 130a
                        mc"(I'm not exactly sure how to feel about that.)"

                        show sc mcbackhomef 132
                        v"Let's just keep this between us, okay?"

                        show sc mcbackhomef 133
                        mc"Uh... Sure thing, [mc_v_address!c]."
                        show sc mcbackhomef 135
                        mc"(I may keep that kiss to myself, but I sure as hell am not going to forget it.)"
                        #Vivian continues to look embarrassed




        #Sound Effect - they hear two sets of doors opening from upstairs
        play sound "sound effects/02/sound_from_upstairs_effect.mp3" noloop
        show sc mcbackhomef 136
        v"Oh, it sounds like the girls are awake."
        #they both look up towards the ceiling while Vivian speaks

        show sc mcbackhomef 137
        v"They've been worried about you, you know."
        #She looks back at the MC
        show sc mcbackhomef 138
        mc"Really?"
        #Vivian has a straight face and a closed mouth
        mc"Even [b_name]??"
        #MC surprised
        show sc mcbackhomef 142
        v"Haha! Well..."
        show sc mcbackhomef 104
        with dissolve
        v"She may have asked about you."
        #Vivian tries to remember
        mc"Right..."
        #The MC gives a sceptical look
        show sc mcbackhomef 102
        with dissolve
        v"Anyway, we'll continue this discussion some other time..."
        #Vivian looks at the MC, gives him an assured look
        #screen goes blank
        scene black
        with dissolve
        scene black
        with Pause (2)
        jump lb_ep02_02_02_Ariel_and_Bella_come_down_to_see_the_MC


    if v_ep01_day3_vivian_dress == "red":
        #ROLLING IMAGE OF VIVIAN IN HER NEGLIGEE
        if not persistent.v_sex_anim_enabled_locked and persistent.v_sex_anim_enabled:
            scene sc mcbackhomef 088a at tt_top
            pause
        elif True:
            show sc mcbackhomef 119a
            with dissolve
            mc"(Woah...)"
        scene sc mcbackhomef 089
        mc"(After everything I've been through tonight, this a surprise to come home to.)"

        #[Go upstairs / Say something nice]

        menu:
            "Go upstairs":
                #The MC separates from Vivian
                show sc mcbackhomef 093
                mc"(However, I shouldn't be seen talking with her like this, just in case [vic_name] happens to come home.)"
                show sc mcbackhomef 094
                mc"You look great for your age, [mc_v_address!c]."
                show sc mcbackhomef 092a
                mc"And don't worry about what anybody else thinks."
                show sc mcbackhomef 095
                mc"That's what you told me when I was younger, remember?"
                show sc mcbackhomef 097a
                v"Thanks, sweetheart. You grew up better than I could have hoped for."
                show sc mcbackhomef 096
                mc"And that's mainly because of you."
                show sc mcbackhomef 091a
                mc"Anyway, it's been a long day, so I'm probably gonna have a shower and then go to bed."
                show sc mcbackhomef 098a
                v"Sure thing, [y_name]."
                stop music fadeout 1.0

                #Go down to SCENE CONTINUES

            "Say something back" (wt="Best option + Bonus image"):

                show sc mcbackhomef 090
                mc"([mc_vic_address] has definitely missed out!)"
                $ rewards_unlock ("vivian",11)
                show sc mcbackhomef 093
                mc"(She really needs to hear this.)"


                menu:
                    "Compliment her"(wt="Bonus image"):
                        show sc mcbackhomef 094
                        mc"You look amazing, [mc_v_address!c]!"
                        $ rewards_unlock ("vivian",12)
                        show sc mcbackhomef 095
                        mc"And you shouldn't be so critical of yourself."

                        show sc mcbackhomef 094
                        mc"[mc_vic_address!c] is a fool for not being here to see you like this."
                        stop music fadeout 1.0
                        show sc mcbackhomef 097a
                        v"Thanks, sweetheart. That's so nice of you to say."
                        play music "sound effects/01/Velvet Touch2.mp3" loop fadein 1.0
                        show sc mcbackhomef 098a
                        v"You know, it's a little dim in this room."

                        show sc mcbackhomef 099a
                        v"Stand up and take a closer look."

                        mc"Um... Okay."

                        show sc mcbackhomef 100a
                        with dissolve
                        mc"Yeah, it really does suit you."
                        #The MC stands before Vivian, looking at her lingerie
                        show sc mcbackhomef 101
                        mc"Where did you get it from?"
                        show sc mcbackhomef 102c
                        v"I stole it from the acting theatre the other day while you were performing in front of the teacher."
                        show sc mcbackhomef 102aa
                        mc"Oh yeah, don't remind me."
                        #the MC rolls his eyes
                        show sc mcbackhomef 104a
                        v"Thank you for the compliment, sweetheart."
                        show sc mcbackhomef 105a
                        v"You always know the right things to say to cheer me up."

                        show sc mcbackhomef 106a
                        mc"You're welcome."
                        #Vivian hugs the MC

                        show sc mcbackhomef 107a
                        v"Mmm..."
                        #show her breasts pressed up against his chest
                        show sc mcbackhomef 108a
                        v"I really do miss you when you're not here, you know?"

                        show sc mcbackhomef 109a
                        mc"(She's hugging me tighter than normal.)"
                        show sc mcbackhomef 110a
                        mc"(And if I didn't know any better, I'd say she was grinding herself against me.)"
                        #show their hips pressed together

                        show sc mcbackhomef 111a
                        pause 1.0
                        #She leans back from the hug, but they still hold each other and look into each other's eyes

                        show sc mcbackhomef 112a
                        with dissolve
                        #Vivian looks down and sees the tent shape in his pants
                        v"(Oh my...)"
                        show sc mcbackhomef 113a
                        v"(It feels like he's a {b}huge{/b} fan of my choice of lingerie.)"
                        show sc mcbackhomef 114a
                        v"(Perhaps I could reward him for that. But how?)"
                        #She looks the MC in the eyes
                        show sc mcbackhomef 115
                        mc"[mc_v_address!c]?"
                        show sc mcbackhomef 116a
                        v"Yes, [y_name]?"
                        stop music fadeout 1.0
                        #she has a sexy little smirk on her face
                        #Go Down to SCENE CONTINUES

                    "Talk her up"(wt="Bonus image"):
                        show sc mcbackhomef 118
                        mc"You look drop-dead sexy, [mc_v_address!c]!"
                        show sc mcbackhomef 097a
                        mc"You know, I think you could be the sole reason for global warming."
                        $ rewards_unlock ("vivian",13)
                        stop music fadeout 1.0
                        show sc mcbackhomef 119a
                        mc"And I mean that as a good thing."
                        #Vivian smiles
                        play music "sound effects/01/Velvet Touch2.mp3" loop fadein 1.0
                        show sc mcbackhomef 120a
                        v"So, you're saying that you think I'm hot?"
                        #Vivian looks at the MC seductively
                        show sc mcbackhomef 102aa
                        mc"Uh, yeah... I guess I am."
                        show sc mcbackhomef 095
                        mc"And [mc_vic_address!c] is a fool for not being here to see you like this."

                        show sc mcbackhomef 121a
                        v"Thanks, sweetheart. I actually prefer that you're here instead of him right now."

                        show sc mcbackhomef 119a
                        mc"Yeah, me too."

                        show sc mcbackhomef 098a
                        v"You know, it's a little dim in this room."

                        show sc mcbackhomef 099a
                        v"Stand up and take a closer look."

                        mc"Um... Okay."

                        show sc mcbackhomef 100a
                        with dissolve
                        mc"Yeah, it really does suit you."
                        #The MC stands before Vivian, looking at her lingerie

                        show sc mcbackhomef 101
                        mc"Where did you get it from?"

                        show sc mcbackhomef 102aa
                        v"I stole it from the acting theatre the other day while you were performing in front of the teacher."

                        mc"Oh yeah, don't remind me."
                        #the MC rolls his eyes

                        show sc mcbackhomef 104a
                        v"Thank you for the compliment, sweetheart."
                        show sc mcbackhomef 105a
                        v"You always know the right things to say to cheer me up."

                        show sc mcbackhomef 106a
                        mc"You're welcome."
                        #Vivian hugs the MC

                        show sc mcbackhomef 107a
                        v"Mmm..."
                        #show her breasts pressed up against his chest
                        show sc mcbackhomef 108
                        v"I really do miss you when you're not here, you know?"

                        show sc mcbackhomef 109a
                        mc"(She's hugging me tighter than normal.)"
                        show sc mcbackhomef 110a
                        mc"(And if I didn't know any better, I'd say she was grinding herself against me.)"
                        #show their hips pressed together

                        show sc mcbackhomef 111a
                        pause 1.5
                        #She leans back from the hug, but they still hold each other and look into each other's eyes

                        show sc mcbackhomef 112a
                        with dissolve
                        #Vivian looks down and sees the tent shape in his pants
                        v"(Oh my...)"
                        show sc mcbackhomef 113a
                        with dissolve
                        v"(It feels like he's a {b}huge{/b} fan of my choice of lingerie.)"
                        show sc mcbackhomef 114a
                        v"(Perhaps I could reward him for that. But how?)"
                        #She looks the MC in the eyes

                        show sc mcbackhomef 115
                        mc"[mc_v_address!c]?"

                        show sc mcbackhomef 116a
                        v"Yes, [y_name]?"
                        stop music fadeout 1.0
                        #she has a sexy little smirk on her face
                        #Go Down to SCENE CONTINUES


                    "Criticise [vic_name]"(wt="Best option + Bonus image"):
                        #BEST OPTION - Vivian points or bonus renders
                        show sc mcbackhomef 095
                        mc"I'm sorry, [mc_v_address!c], but [mc_vic_address] is a moron if he can't see how insanely attractive you still are."
                        show sc mcbackhomef 118
                        mc"You look {b}smoking{/b} hot in that!"
                        $ rewards_unlock ("vivian",14)
                        show sc mcbackhomef 120a
                        v"Oh, thank you, sweetheart. I don't know what else to say."
                        stop music fadeout 1.0
                        show sc mcbackhomef 119a
                        v"(Wow... It was so nice to hear that.)"
                        v"(I suddenly feel a lot sexier wearing this in front of him.)"
                        play music "sound effects/01/Velvet Touch2.mp3" loop fadein 1.0
                        show sc mcbackhomef 098a
                        v"You know, it's a little dim in this room."

                        show sc mcbackhomef 099a
                        v"Stand up and take a closer look."

                        mc"Um... Okay."

                        show sc mcbackhomef 100a
                        with dissolve
                        mc"Yeah, it really does suit you."
                        #The MC stands before Vivian, looking at her lingerie

                        show sc mcbackhomef 101
                        mc"Where did you get it from?"

                        show sc mcbackhomef 102aa
                        v"I stole it from the acting theatre the other day while you were performing in front of the teacher."

                        mc"Oh yeah, don't remind me."
                        #the MC rolls his eyes

                        show sc mcbackhomef 104a
                        v"Thank you for the compliment, sweetheart."
                        show sc mcbackhomef 105a
                        v"You always know the right things to say to cheer me up."

                        show sc mcbackhomef 106a
                        mc"You're welcome."
                        #Vivian hugs the MC

                        show sc mcbackhomef 107a
                        v"Mmm..."
                        #show her breasts pressed up against his chest
                        show sc mcbackhomef 108a
                        v"I really do miss you when you're not here, you know?"

                        show sc mcbackhomef 107a
                        mc"(She's hugging me tighter than normal.)"
                        show sc mcbackhomef 110a
                        mc"(And if I didn't know any better, I'd say she's grinding herself against me.)"
                        #show their hips pressed together

                        show sc mcbackhomef 111a
                        pause 1.5
                        #She leans back from the hug, but they still hold each other and look into each other's eyes

                        show sc mcbackhomef 112a
                        with dissolve
                        #Vivian looks down and sees the tent shape in his pants
                        v"(Oh my...)"
                        show sc mcbackhomef 113a
                        v"(It feels like he's a {b}huge{/b} fan of my choice of lingerie.)"
                        show sc mcbackhomef 114a
                        v"(Perhaps I could reward him for that. But how?)"
                        #She looks the MC in the eyes

                        show sc mcbackhomef 115
                        mc"[mc_v_address!c]?"

                        show sc mcbackhomef 116a
                        v"[y_name]..."
                        #she has a sexy little smirk on her face

                        show sc mcbackhomef 122a
                        v"I have something for you."
                        #Vivian leans forward and kisses the MC, they both close their eyes
                        play sound "sound effects/01/kiss_and_moan_sound_effect01.mp3" loop fadein 1.0
                        show sc mcbackhomef 123a
                        with dissolve
                        pause 1.0
                        v"Mmm..."

                        show sc mcbackhomef 124
                        mc"(Oh wow!)"
                        #ANIMATION OF THEM KISSING - ZOOMED OUT SHOT

                        show sc mcbackhomef 125a
                        v"(This feels so good, so naughty...)"
                        #her eyes are still closed as they makeout
                        stop sound fadeout 1.0
                        stop music fadeout 1.0
                        play sound "sound effects/01/record_scratch.ogg" noloop
                        show sc mcbackhomef 126a
                        with vpunch
                        v"(Wait!)"
                        v"(What the hell am I doing??)"
                        #Her eyes shoot open when she thinks this

                        show sc mcbackhomef 127a
                        with dissolve
                        mc"[mc_v_address!c]??"
                        #Vivian looks away

                        show sc mcbackhomef 129a
                        mc"Why did you kiss me?"
                        show sc mcbackhomef 130aa
                        v"I'm sorry, sweetheart... I don't know what came over me."
                        v"I think for a moment there, I thought I was kissing [vic_name]."
                        show sc mcbackhomef 130c
                        mc"(I'm not exactly sure how to feel about that.)"

                        show sc mcbackhomef 132a
                        v"Let's just keep this between us, okay?"

                        show sc mcbackhomef 133
                        mc"Uh... Sure thing, [mc_v_address!c]."
                        show sc mcbackhomef 135a
                        mc"(I may keep that kiss to myself, but I sure as hell am not going to forget it.)"
                        #Vivian continues to look embarrassed

        #Sound Effect - they hear two sets of doors opening from upstairs
        play sound "sound effects/02/sound_from_upstairs_effect.mp3" noloop
        show sc mcbackhomef 136a
        v"Oh, it sounds like the girls are awake."
        #they both look up towards the ceiling while Vivian speaks

        show sc mcbackhomef 137a
        v"They've been worried about you, you know."
        #She looks back at the MC
        show sc mcbackhomef 138a
        mc"Really?"
        #Vivian has a straight face and a closed mouth
        mc"Even [b_name]??"
        #MC surprised
        show sc mcbackhomef 142a
        v"Haha! Well..."
        show sc mcbackhomef 104a
        with dissolve
        v"She may have asked about you."
        #Vivian tries to remember
        mc"Right..."
        #The MC gives a sceptical look
        show sc mcbackhomef 102c
        with dissolve
        v"Anyway, we'll continue this discussion some other time..."
        #Vivian looks at the MC, gives him an assured look
        #screen goes blank
        scene black
        with dissolve
        scene black
        with Pause (2)
        jump lb_ep02_02_02_Ariel_and_Bella_come_down_to_see_the_MC

    if v_ep01_day3_vivian_dress == "golden":
        if not persistent.v_sex_anim_enabled_locked and persistent.v_sex_anim_enabled:
            scene sc mcbackhomef 088b at tt_top
            pause
        elif True:
            show sc mcbackhomef 119b
            with dissolve
            mc"(Woah...)"
        #ROLLING IMAGE OF VIVIAN IN HER NEGLIGEE

        scene sc mcbackhomef 089
        mc"(After everything I've been through tonight, this a surprise to come home to.)"


        #[Go upstairs / Say something nice]

        menu:
            "Go upstairs":
                #The MC separates from Vivian
                show sc mcbackhomef 093
                mc"(However, I shouldn't be seen talking with her like this, just in case [vic_name] happens to come home.)"
                show sc mcbackhomef 094
                mc"You look great for your age, [mc_v_address!c]."
                show sc mcbackhomef 092b
                mc"And don't worry about what anybody else thinks."
                show sc mcbackhomef 095
                mc"That's what you told me when I was younger, remember?"
                show sc mcbackhomef 097b
                v"Thanks, sweetheart. You grew up better than I could have hoped for."
                show sc mcbackhomef 096
                mc"And that's mainly because of you."
                show sc mcbackhomef 091b
                mc"Anyway, it's been a long day, so I'm probably gonna have a shower and then go to bed."
                show sc mcbackhomef 098b
                v"Sure thing, [y_name]."
                stop music fadeout 1.0

                #Go down to SCENE CONTINUES

            "Say something back" (wt="Best option + Bonus image"):

                show sc mcbackhomef 090
                mc"([mc_vic_address] has definitely missed out!)"
                $ rewards_unlock ("vivian",11)
                show sc mcbackhomef 093
                mc"(She really needs to hear this.)"


                menu:
                    "Compliment her"(wt="Bonus image"):
                        show sc mcbackhomef 094
                        mc"You look amazing, [mc_v_address!c]!"
                        $ rewards_unlock ("vivian",12)
                        show sc mcbackhomef 095
                        mc"And you shouldn't be so critical of yourself."

                        show sc mcbackhomef 094
                        mc"[mc_vic_address!c] is a fool for not being here to see you like this."
                        stop music fadeout 1.0
                        show sc mcbackhomef 097b
                        v"Thanks, sweetheart. That's so nice of you to say."
                        play music "sound effects/01/Velvet Touch2.mp3" loop fadein 1.0
                        show sc mcbackhomef 098b
                        v"You know, it's a little dim in this room."

                        show sc mcbackhomef 099b
                        v"Stand up and take a closer look."

                        mc"Um... Okay."

                        show sc mcbackhomef 100b
                        with dissolve
                        mc"Yeah, it really does suit you."
                        #The MC stands before Vivian, looking at her lingerie
                        show sc mcbackhomef 101
                        mc"Where did you get it from?"
                        show sc mcbackhomef 102ab
                        v"I stole it from the acting theatre the other day while you were performing in front of the teacher."
                        show sc mcbackhomef 102d
                        mc"Oh yeah, don't remind me."
                        #the MC rolls his eyes
                        show sc mcbackhomef 104b
                        v"Thank you for the compliment, sweetheart."
                        show sc mcbackhomef 105b
                        v"You always know the right things to say to cheer me up."

                        show sc mcbackhomef 106b
                        mc"You're welcome."
                        #Vivian hugs the MC

                        show sc mcbackhomef 107b
                        v"Mmm..."
                        #show her breasts pressed up against his chest
                        show sc mcbackhomef 108b
                        v"I really do miss you when you're not here, you know?"

                        show sc mcbackhomef 107b
                        mc"(She's hugging me tighter than normal.)"
                        show sc mcbackhomef 110b
                        mc"(And if I didn't know any better, I'd say she's grinding herself against me.)"
                        #show their hips pressed together

                        show sc mcbackhomef 111b
                        pause 1.0
                        #She leans back from the hug, but they still hold each other and look into each other's eyes

                        show sc mcbackhomef 112b
                        with dissolve
                        #Vivian looks down and sees the tent shape in his pants
                        v"(Oh my...)"
                        show sc mcbackhomef 113b
                        v"(It feels like he's a {b}huge{/b} fan of my choice of lingerie.)"
                        show sc mcbackhomef 114b
                        v"(Perhaps I could reward him for that. But how?)"
                        #She looks the MC in the eyes
                        show sc mcbackhomef 115
                        mc"[mc_v_address!c]?"
                        show sc mcbackhomef 116b
                        v"Yes, [y_name]?"
                        stop music fadeout 1.0
                        #she has a sexy little smirk on her face
                        #Go Down to SCENE CONTINUES

                    "Talk her up"(wt="Bonus image"):
                        show sc mcbackhomef 118
                        mc"You look drop-dead sexy, [mc_v_address!c]!"
                        show sc mcbackhomef 097b
                        mc"You know, I think you could be the sole reason for global warming."
                        $ rewards_unlock ("vivian",13)
                        stop music fadeout 1.0
                        show sc mcbackhomef 119b
                        mc"And I mean that as a good thing."
                        #Vivian smiles
                        play music "sound effects/01/Velvet Touch2.mp3" loop fadein 1.0
                        show sc mcbackhomef 120b
                        v"So, you're saying that you think I'm hot?"
                        #Vivian looks at the MC seductively
                        show sc mcbackhomef 102ab
                        mc"Uh, yeah... I guess I am."
                        show sc mcbackhomef 095
                        mc"And [mc_vic_address!c] is a fool for not being here to see you like this."

                        show sc mcbackhomef 121b
                        v"Thanks, sweetheart. I actually prefer that you're here instead of him right now."

                        show sc mcbackhomef 119b
                        mc"Yeah, me too."

                        show sc mcbackhomef 098b
                        v"You know, it's a little dim in this room."

                        show sc mcbackhomef 099b
                        v"Stand up and take a closer look."

                        mc"Um... Okay."

                        show sc mcbackhomef 100b
                        with dissolve
                        mc"Yeah, it really does suit you."
                        #The MC stands before Vivian, looking at her lingerie

                        show sc mcbackhomef 101
                        mc"Where did you get it from?"

                        show sc mcbackhomef 102ab
                        v"I stole it from the acting theatre the other day while you were performing in front of the teacher."

                        mc"Oh yeah, don't remind me."
                        #the MC rolls his eyes

                        show sc mcbackhomef 104b
                        v"Thank you for the compliment, sweetheart."
                        show sc mcbackhomef 105b
                        v"You always know the right things to say to cheer me up."

                        show sc mcbackhomef 106b
                        mc"You're welcome."
                        #Vivian hugs the MC

                        show sc mcbackhomef 107b
                        v"Mmm..."
                        #show her breasts pressed up against his chest
                        show sc mcbackhomef 108b
                        v"I really do miss you when you're not here, you know?"

                        show sc mcbackhomef 107b
                        mc"(She's hugging me tighter than normal.)"
                        show sc mcbackhomef 110b
                        mc"(And if I didn't know any better, I'd say she's grinding herself against me.)"
                        #show their hips pressed together

                        show sc mcbackhomef 111b
                        pause 1.5
                        #She leans back from the hug, but they still hold each other and look into each other's eyes

                        show sc mcbackhomef 112b
                        with dissolve
                        #Vivian looks down and sees the tent shape in his pants
                        v"(Oh my...)"
                        show sc mcbackhomef 113b
                        with dissolve
                        v"(It feels like he's a {b}huge{/b} fan of my choice of lingerie.)"
                        show sc mcbackhomef 114b
                        v"(Perhaps I could reward him for that. But how?)"
                        #She looks the MC in the eyes

                        show sc mcbackhomef 115
                        mc"[mc_v_address!c]?"

                        show sc mcbackhomef 116b
                        v"Yes, [y_name]?"
                        stop music fadeout 1.0
                        #she has a sexy little smirk on her face
                        #Go Down to SCENE CONTINUES


                    "Criticise [vic_name]"(wt="Best option + Bonus image"):
                        #BEST OPTION - Vivian points or bonus renders
                        show sc mcbackhomef 095
                        mc"I'm sorry, [mc_v_address!c], but [mc_vic_address] is a moron if he can't see how insanely attractive you still are."
                        show sc mcbackhomef 118
                        mc"You look {b}smoking{/b} hot in that!"
                        $ rewards_unlock ("vivian",14)
                        show sc mcbackhomef 120b
                        v"Oh, thank you, sweetheart. I don't know what else to say."
                        stop music fadeout 1.0
                        show sc mcbackhomef 119b
                        v"(Wow... It was so nice to hear that.)"
                        v"(I suddenly feel a lot sexier wearing this in front of him.)"
                        play music "sound effects/01/Velvet Touch2.mp3" loop fadein 1.0
                        show sc mcbackhomef 098b
                        v"You know, it's a little dim in this room."

                        show sc mcbackhomef 099b
                        v"Stand up and take a closer look."

                        mc"Um... Okay."

                        show sc mcbackhomef 100b
                        with dissolve
                        mc"Yeah, it really does suit you."
                        #The MC stands before Vivian, looking at her lingerie

                        show sc mcbackhomef 101
                        mc"Where did you get it from?"

                        show sc mcbackhomef 102d
                        v"I stole it from the acting theatre the other day while you were performing in front of the teacher."
                        show sc mcbackhomef 102ab
                        mc"Oh yeah, don't remind me."
                        #the MC rolls his eyes

                        show sc mcbackhomef 104b
                        v"Thank you for the compliment, sweetheart."
                        show sc mcbackhomef 105b
                        v"You always know the right things to say to cheer me up."

                        show sc mcbackhomef 106b
                        mc"You're welcome."
                        #Vivian hugs the MC

                        show sc mcbackhomef 107b
                        v"Mmm..."
                        #show her breasts pressed up against his chest
                        show sc mcbackhomef 108b
                        v"I really do miss you when you're not here, you know?"

                        show sc mcbackhomef 109b
                        mc"(She's hugging me tighter than normal.)"
                        show sc mcbackhomef 110b
                        mc"(And if I didn't know any better, I'd say she's grinding herself against me.)"
                        #show their hips pressed together

                        show sc mcbackhomef 111b
                        pause 1.5
                        #She leans back from the hug, but they still hold each other and look into each other's eyes

                        show sc mcbackhomef 112b
                        with dissolve
                        #Vivian looks down and sees the tent shape in his pants
                        v"(Oh my...)"
                        show sc mcbackhomef 113b
                        v"(It feels like he's a {b}huge{/b} fan of my choice of lingerie.)"
                        show sc mcbackhomef 114b
                        v"(Perhaps I could reward him for that. But how?)"
                        #She looks the MC in the eyes

                        show sc mcbackhomef 115
                        mc"[mc_v_address!c]?"

                        show sc mcbackhomef 116b
                        v"[y_name]..."
                        #she has a sexy little smirk on her face

                        show sc mcbackhomef 122b
                        v"I have something for you."
                        #Vivian leans forward and kisses the MC, they both close their eyes
                        play sound "sound effects/01/kiss_and_moan_sound_effect01.mp3" loop fadein 1.0
                        show sc mcbackhomef 123b
                        with dissolve
                        pause 1.0
                        v"Mmm..."

                        show sc mcbackhomef 124
                        mc"(Oh wow!)"
                        #ANIMATION OF THEM KISSING - ZOOMED OUT SHOT

                        show sc mcbackhomef 125b
                        v"(This feels so good, so naughty...)"
                        #her eyes are still closed as they makeout
                        stop sound fadeout 1.0
                        stop music fadeout 1.0
                        play sound "sound effects/01/record_scratch.ogg" noloop
                        show sc mcbackhomef 126b
                        with vpunch
                        v"(Wait!)"
                        v"(What the hell am I doing??)"
                        #Her eyes shoot open when she thinks this

                        show sc mcbackhomef 127b
                        with dissolve
                        mc"[mc_v_address!c]??"
                        #Vivian looks away

                        show sc mcbackhomef 129b
                        mc"Why did you kiss me?"
                        show sc mcbackhomef 130ab
                        v"I'm sorry, sweetheart... I don't know what came over me."
                        v"For a moment there, I thought I was kissing [vic_name]."
                        show sc mcbackhomef 130d
                        mc"(I'm not exactly sure how to feel about that.)"
                        mc"(Or if I believe her.)"

                        show sc mcbackhomef 132b
                        v"Let's just keep this between us, okay?"

                        show sc mcbackhomef 133
                        mc"Uh... Sure thing, [mc_v_address!c]."
                        show sc mcbackhomef 135b
                        mc"(I may keep that kiss to myself, but I sure as hell am not going to forget it.)"
                        #Vivian continues to look embarrassed

        #Sound Effect - they hear two sets of doors opening from upstairs
        play sound "sound effects/02/sound_from_upstairs_effect.mp3" noloop
        show sc mcbackhomef 136b
        v"Oh, it sounds like the girls are awake."
        #they both look up towards the ceiling while Vivian speaks

        show sc mcbackhomef 137b
        v"They've been worried about you, you know."
        #She looks back at the MC
        show sc mcbackhomef 138b
        mc"Really?"
        #Vivian has a straight face and a closed mouth
        mc"Even [b_name]??"
        #MC surprised
        show sc mcbackhomef 142b
        v"Haha! Well..."
        show sc mcbackhomef 104b
        with dissolve
        v"She may have asked about you."
        #Vivian tries to remember
        mc"Right..."
        #The MC gives a sceptical look
        show sc mcbackhomef 102ab
        with dissolve
        v"Anyway, we'll continue this discussion some other time..."
        #Vivian looks at the MC, gives him an assured look
        #screen goes blank
        scene black
        with dissolve
        scene black
        with Pause (2)
        jump lb_ep02_02_02_Ariel_and_Bella_come_down_to_see_the_MC