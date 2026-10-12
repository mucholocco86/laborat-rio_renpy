init:
    $ v_ep01_06_01_Vivian_Work_Date = False
    $ v_ep01_06_01_Vivian_Work_Revenge = False

    image sc vivian work butt slap1:
        "sc vivianwork v008a" with Dissolve(0.2, alpha=True)
        pause 0.2
        "sc vivianwork v008" with Dissolve(0.2, alpha=True)

    image sc vivian table walk:
        "sc vivianwork v023" with Dissolve(0.2, alpha=True)
        pause 2.0
        "sc vivianwork v023a" with Dissolve(0.2, alpha=True)
        pause 2.0
        "sc vivianwork v023b" with Dissolve(0.2, alpha=True)

    image sc vivian work old man search:
        "sc vivianwork v091" with Dissolve(0.2, alpha=True)
        pause 0.6
        "sc vivianwork v092" with Dissolve(0.2, alpha=True)
        pause 0.6
        repeat

    image sc vivian work secret masturbate1:
        "sc vivianwork v121a" with Dissolve(0.2, alpha=True)
        pause 0.6
        "sc vivianwork v121b" with Dissolve(0.2, alpha=True)
        pause 0.6
        repeat

    image sc vivian work secret masturbate2:
        "sc vivianwork v122" with Dissolve(0.2, alpha=True)
        pause 0.6
        "sc vivianwork v122a" with Dissolve(0.2, alpha=True)
        pause 0.6
        repeat

    image sc vivian work secret masturbate3:
        "sc vivianwork v123" with Dissolve(0.2, alpha=True)
        pause 0.6
        "sc vivianwork v123a" with Dissolve(0.2, alpha=True)
        pause 0.6
        repeat

    image sc vivian work secret co-worker masturbate1:
        "sc vivianwork v126" with Dissolve(0.2, alpha=True)
        pause 1.0
        "sc vivianwork v126a" with Dissolve(0.2, alpha=True)

    image sc vivian work secret masturbate4:
        "sc vivianwork v127" with Dissolve(0.2, alpha=True)
        pause 0.6
        "sc vivianwork v127a" with Dissolve(0.2, alpha=True)
        pause 0.6
        repeat

    image sc vivian work secret co-worker masturbate2:
        "sc vivianwork v129" with Dissolve(0.2, alpha=True)
        pause 0.6
        "sc vivianwork v129a" with Dissolve(0.2, alpha=True)
        pause 0.6
        "sc vivianwork v129b" with Dissolve(0.2, alpha=True)
        pause 0.6
        repeat

    image sc vivian work secret masturbate5:
        "sc vivianwork v130" with Dissolve(0.2, alpha=True)
        pause 0.4
        "sc vivianwork v130a" with Dissolve(0.2, alpha=True)
        pause 0.4
        "sc vivianwork v130b" with Dissolve(0.2, alpha=True)
        pause 0.4
        repeat

label lb_ep01_06_01_Vivian_Work_1:
    #Thief Of Hearts - Ep 1 Scene 06-01 - Vivian

    #Note: This scene belongs to the Vivian path. The scene starts with the MC going to Vivian’s workplace. She works at a local diner as a waitress.
    #The MC learns that Vivian’s job is to do a performance by imitating a relative of a German artist. And that his side job is to help her steal a costume for the job.

    #NOTE: The Extra scene option is only available in this scene if the player chooses to visit Vivian/Mom as either their first or second option.
    #They will have the chance to get bonus renders of her if they make the right choice(s).

    #SCENE BEGINS

    #the scene continues with the MC arriving at Vivian’s workplace"
    #It’s a local diner in a middle-class area - there are a few patrons in there as it’s just before lunch"
    play ambient "sound effects/01/quiet_restaurant_ambient_noise.ogg" loop fadein 1.0
    scene sc vivianwork v001
    with dissolve
    mc"(I think this is the first time I’ve come to see [mc_v_address] at her job.)"
    show sc vivianwork v002
    mc"(This is a nice restaurant. Certainly one for the middle to upper class.)"
    show sc vivianwork v003
    mc"(Hmm... I don’t see her?)"
    #the MC sees her in her waitress uniform, attending to some patrons"
    show sc vivianwork v004
    mc"(Ah... There she is.)"
    #closer image of Vivian in her uniforv"
    if not persistent.v_sex_anim_enabled_locked and persistent.v_sex_anim_enabled:
        scene wip_ep01_vivian_work_01 at tt_top
        pause
    elif True:
        show sc vivianwork v005
    mc"(Damn... I know it’s only a waitresses uniform, but [mc_v_address] looks stunning in it.)"
    mc"(To be fair, she’d look attractive even if she was wearing a potato sack!)"
    #Vivian serves a gentleman who is clearly a rich person with the way he is dressed"
    scene sc vivianwork v006
    v"Okay gentlemen, I’ll have your drinks for you shortly."
    show sc vivianwork v008
    old_man"Thanks, sweet cheeks."
    #one of the men slaps her ass and laughs"
    $ ui.timer(0.1, Play("sound", "sound effects/01/slap1.ogg"))
    show sc vivian work butt slap1
    play sound2 "sound effects/01/Old_Man_Laugh1.mp3"
    old_man"Hahaha!"
    #Vivian has a defeated look on her face. She returns to the counter"
    show sc vivianwork v009
    mc"(Da fuck??)"
    # or mc"(Da fuq??)
    stop sound fadeout 1.0
    stop sound2 fadeout 1.0
    show sc vivianwork v010
    mc"(Why is [mc_v_address] letting that fat fucker do that to her?)"
    mc"(I should teach that old geezer some manners, but I need to check on her first.)"
    show sc vivianwork v011
    mc"(I'll deal with this asshole later.)"
    #the MC approaches Vivian, who has her back turned to him"
    show sc vivianwork v012a
    mc"[mc_v_address]?"

    #she turns around"
    show sc vivianwork v012b
    v"[y_name]?"
    show sc vivianwork v012
    v"What are you doing here?"
    show sc vivianwork v013
    mc"I thought I’d surprise you!"
    show sc vivianwork v014
    v"That’s sweet of you."
    show sc vivianwork v015
    mc"Um, I know you’re working at the moment, but, do you think we could go somewhere to talk?"
    mc"It’s about... You know..."
    show sc vivianwork v016
    v"Oh..."
    show sc vivianwork v017
    v"One second."
    #Vivian addresses her boss, who is a huge guy with a menacing look - important for later - e.g. https://i.dailymail.co.uk/i/pix/2011/08/04/article-0-0D496EDF00000578-812_468x337.jpg"
    show sc vivianwork v018
    v"Boss, I’m just going to take my break if that’s okay?"
    show sc vivianwork v019
    boss"Sure thing, [v_name]."
    boss"But ten minutes, and that’s it. The lunch rush will be starting shortly."
    show sc vivianwork v020
    v"Thanks, boss."
    #Vivian turns back to the MC"
    show sc vivianwork v021
    v"Let’s go find somewhere to chat."
    show sc vivianwork v022
    mc"Lead the way."
    #Vivian walks in front of the MC so the player can see her from behind"
    if not persistent.v_sex_anim_enabled_locked and persistent.v_sex_anim_enabled:
        show sc vivian table walk
        mc"(Damn [mc_v_address]... When you’re showing that much of your legs and wearing such a tight dress...)"
        mc"(I can almost understand why that old guy spanked you.)"
        mc"(Not that he should have.)"
    elif True:
        show sc vivianwork v023
        mc"(Damn [mc_v_address]... When you’re showing that much of your legs and wearing such a tight dress...)"
        show sc vivianwork v023a
        mc"(I can almost understand why that old guy spanked you.)"
        show sc vivianwork v023b
        mc"(Not that he should have.)"
    show sc vivianwork v024
    v"Have a seat."
    #the MC and Vivian sit at a table away from everyone"
    show sc vivianwork v025
    v"So what brings you here?"
    show sc vivianwork v026
    mc"I’ll get to that in a moment..."
    show sc vivianwork v027
    mc"I saw what happened before with that old guy, [mc_v_address]."
    mc"Why the hell did you let him do that? Why don’t you slap him or tell your boss?"
    show sc vivianwork v026
    mc"He needs to be punished for his actions."
    show sc vivianwork v028
    v"I’m sorry you had to see that. Please promise me that you won’t do or say anything to him."
    show sc vivianwork v029
    mc"Uhh... Fine. I won’t."
    show sc vivianwork v030
    mc"Why did you let it happen? Did you enjoy it?"
    show sc vivianwork v031
    v"No, not at all."
    v"I’m just as angry as you are about it, sweetheart."
    show sc vivianwork v028
    v"But if I reacted and caused a scene, then it could cost me my job."
    show sc vivianwork v032
    v"We're tight for money right now [y_name]. I can't afford to lose this job."
    show sc vivianwork v033
    v"And if I get sacked, then [vic_name] will be furious with me."
    show sc vivianwork v025
    v"I hope you can understand."
    #mc"(It’s not right, but I get where she’s coming from.)"
    show sc vivianwork v026
    mc"Fine, I’ll let it go."
    show sc vivianwork v034
    v"So what did you want to see me about?"
    show sc vivianwork v035
    mc"Well, I want to start doing some work on the side as soon as possible, so I can help by bringing in some extra money for us all."
    mc"And to also get back into [mc_vic_address]’s good books."
    show sc vivianwork v036
    v"That’s great that you’re showing some initiative, [y_name]."
    v"And I’m sorry for what happened yesterday with the job."
    show screen scr_secret_icon("v_secrets_ep01_06_01_1") onlayer ontop
    with { "ontop": dissolve}
    show sc vivianwork v037
    v"[vic_name] is very set in his ways. He’s a perfectionist. Sure he overreacts sometimes, but he does provide for all of us."
    show sc vivianwork v038
    mc"I can’t believe you’re still defending him, [mc_v_address]."
    mc"The way he talks to you is so... condescending."
    show sc vivianwork v037
    v"I know, and his drinking is becoming a bigger problem."
    v"Between you and me, I’m starting to feel uncomfortable being around him and I hate not feeling appreciated."
    show sc vivianwork v039
    v"I feel bad for you [a_name] and [b_name] that he doesn’t show you the appreciation you deserve either."
    show sc vivianwork v040
    v"I’m not an idiot... I know he treats me like I’m just his errand-girl."
    v"And to be frank, after last night, I feel disgusted whenever I think about being intimate with him."
    show sc vivianwork v041
    v"Lately, he's been out very late at night."
    v"It makes me wonder..."
    mc"(What is she referring to?)"
    #Vivian is lost in thought, thinking if Victor is having an affair"
    show sc vivianwork v042
    v"Hmm..."
    show sc vivianwork v043
    show screen scr_secret_hotspot ("sc vivianwork v043","893, 747, 100, 140","v_secrets_ep01_06_01_1")
    with faster_dissolve
    v"You know we haven’t done it in several months."
    v"A woman has {b}{i}needs{/i}{/b} you know..."
    hide screen scr_secret_hotspot
    show sc vivianwork v044
    mc"Okay too much information, [mc_v_address]."
    show sc vivianwork v045
    v"Sorry sweetheart. I don’t mean to dump this all on you."
    show sc vivianwork v046
    v"I do appreciate you listening to me though. It’s nice to have somebody to talk to about this."
    show sc vivianwork v047
    mc"Any time, [mc_v_address]."
    mc"So as I was saying before, I need some extra work to keep [vic_name] off my back. At least for a while."
    mc"Any ideas?"
    hide screen scr_secret_icon onlayer ontop
    with { "ontop": dissolve}
    show sc vivianwork v036
    v"I’m not too sure. However, perhaps you could help me with something."
    show sc vivianwork v035
    mc"Sure... Name it."
    show sc vivianwork v048
    v"[vic_name] has asked me to find a blonde wig and a classy nineteenth-century European-styled dress."
    show sc vivianwork v049
    v"He also asked me to start learning German, and try to perfect the accent."
    show sc vivianwork v050
    mc"How come?"
    show sc vivianwork v051
    v"I presume he wants me to impersonate a German woman around my age."
    v"There’s also this acting theatre in town where he wants me to watch a local play to get an idea of the character he wants me to become."
    show sc vivianwork v052
    mc"Hmm... Perhaps this place could have a few items that you might need."
    mc"Like that wig and dress for instance."
    show sc vivianwork v053
    mc"Hmm... I think I know where you’re going with this."
    show sc vivianwork v054
    v"I don’t suppose you would like to go with me to this theatre, would you?"
    show sc vivianwork v045
    v"If [vic_name] finds out you were able to help me succeed, then it will better your chances of being on this big mission he’s been so secretive about."
    show sc vivianwork v046
    v"Will you help me, sweetheart?"
    show sc vivianwork v047
    #[Agree / Think about it]
    menu choice2:
        "Agree"(wt="You will have a 'Special Date' scene with [v_name] at home + Task Point"):
            #IMPORTANT: Choosing this option will unlock a special date with Vivian after the task has been completed.
            #Make sure to set up a variable for this choice
            mc"Sure, I’d be more than happy to help."
            mc"(Spending more time with her would be great. And I can use that time to help boost her self esteem.)"
            mc"(Plus she stood up for me last night, and has bought me some time to get the drive back.)"
            $ v_ep01_task02_girls_tattoo_counter += 1
            $ rewards_unlock ("vivian",2)
            $ v_ep01_06_01_Vivian_Work_Date = True
        "Think about it":
            #IMPORTANT: Choosing this option will lock any chance of having a special date with Vivian after the task has been completed.
            #Make sure to set up a variable for this choice
            mc"Hmm... Can I have some time to think about this?"
            show sc vivianwork v045
            v"Of course."
    #scene continues
    show sc vivianwork v055
    coworker"Excuse me, [v_name]?"
    coworker"The Boss told me your break time is up."
    show sc vivianwork v056
    coworker"He needs you to attend to Table 4."
    show sc vivianwork v057
    v"Oh, sure thing Cathy. Thanks."
    v"I’ll be there in a moment."
    show sc vivianwork v058
    v"(Great... What does the old man want now?)"
    #the co-worker leaves"
    show sc vivianwork v059
    v"I better get back to work. You should get going. I’ll see you at home."
    show sc vivianwork v060
    mc"Sure thing."
    #Vivian goes to leave, and then stops to ask the MC something"
    if v_ep01_03_04_Vivians_Room_Entered:
        show sc vivianwork v061
        v"Oh, one more thing I need to ask you."
        show sc vivianwork v062
        v"Did you go to bed straight after your private discussion with [vic_name] last night?"
        show sc vivianwork v063
        #mc"Um... I think so."
        mc"Yeah, why?"
        show sc vivianwork v062
        v"You didn’t come to my room to try and speak with me, did you?"
        show sc vivianwork v063a
        mc"(Oh shit... Does she know that I was in her room last night?)"
        show sc vivianwork v063
        mc"I’m not sure what you mean, [mc_v_address]."
        mc"I was pretty much in my room all night."
        show sc vivianwork v061
        v"Oh..."
        v"Well, never mind. Forget I said anything."
        show sc vivianwork v064
        v"I’ll see you at home, sweetheart. Thanks for coming to see me."
        v"Run along now."
        #Vivian leaves the table and goes to attend to the old man"
        show sc vivianwork v065
        mc"(I wonder if she knows I was lying to her.)"
        show sc vivianwork v066
        if v_ep01_06_01_Vivian_Work_Date:
            mc"(Anyway, it will be nice to work with [mc_v_address] and help her out while spending time with her away from the rest of the [private_group].)"
        else:
            mc"(I should consider helping [mc_v_address] with her job. If anything, it would be nice spending time with her away from the rest of the [private_group].)"
    else:
        show sc vivianwork v064
        v"I’ll see you at home, sweetheart. Thanks for coming to see me."
        v"Run along now."
        #Vivian leaves the table and goes to attend to the old man"
        show sc vivianwork v065
        if v_ep01_06_01_Vivian_Work_Date:
            mc"(It sure will be nice to work with [mc_v_address] and help her out...)"
            show sc vivianwork v066
            mc"(And it would mean I get to spend time with her away from the rest of the [private_group].)"
        else:
            mc"(I should consider helping [mc_v_address] with her job.)"
            show sc vivianwork v066
            mc"(If anything, it could be nice spending time with her away from the rest of the [private_group].)"
    show sc vivianwork v067
    old_man"Thanks, toots."
    show sc vivianwork v068
    $ ui.timer(0.1, Play("sound", "sound effects/01/slap2.ogg"))
    play sound2 "sound effects/01/Old_Man_Laugh1.mp3"
    old_man"Hahaha!"
    show sc vivianwork v071
    #He slaps her ass again and Vivian walks away, feeling disappointed and demeaned"
    #mc"Goddamit..."
    mc"That mother fu..."
    stop sound fadeout 1.0
    stop sound2 fadeout 1.0
    show sc vivianwork v069
    if v_ep01_work_visit_options_1 == "[v_name]" or v_ep01_work_visit_options_2 == "[v_name]":
        #*EXTRA SCENE OPTION: Only available if the player chooses to visit Vivian either first or second.
        #If the player chooses to visit her last, the automatic choice will be the "Leave" option below.
        menu:
            "Leave":
                jump lb_ep01_06_01_Vivian_Work_2
            "Revenge"(wt=If(persistent.v_secrets_enabled and persistent.v_secrets_ep01_06_01_1,"Best option and Special Secret Scene after you leave the restaurant","Best Option")):
                show sc vivianwork v070
                mc"(I know I promised her that I wouldn’t, but I can’t let this shit slide a second time.)"
                #mc"(I don’t want her to lose her job, so I’m going to have to be very clever with how I go about this.)"
                #the MC sees the old man get up and head to the bathroom
                show sc vivianwork v073
                mc"(It looks like he’s going to the bathroom.)"
                mc"(I know exactly what I’m going to do...)"
                stop ambient fadeout 1.0
                scene black
                with dissolve
                scene black
                with Pause (2)
                #screen goes blank
                #show the old man in the restroom washing his hands
                play music "sound effects/01/Smooth Move.mp3" loop fadein 1.0
                play sound "sound effects/01/water_faucet_loop.ogg" loop fadein 1.0
                show sc vivianwork v074
                with dissolve
                old_man"Money, money, money... Must be funny, in a rich man’s world..."
                old_man"(I love being rich.)"
                show sc vivianwork v075
                old_man"(I might have to come back just to further mess with that hot ass bitch waitress.)"
                stop sound fadeout 1.0
                show sc vivianwork v076
                old_man"(Time to use my special hands, one final time.)"
                #the old man heads out of the men’s room and the MC enters at the same time. He runs into him"
                play sound "sound effects/01/Falling Over Sound Effect.mp3"
                show sc vivianwork v077 with faster_dissolve
                with hpunch
                old_man"Uhhh!{w=0.5}{nw}"
                show sc vivianwork v078
                with faster_dissolve
                old_man"What the hell??"
                old_man"Watch where you’re going you pipsqueak!"
                stop sound fadeout 1.0
                show sc vivianwork v079
                mc"Oh, I’m sorry Sir."
                #mc"I thought you were the door to the restroom."
                #old_man"Get out of my way!"
                mc"You looked like another door."
                show sc vivianwork v080
                old_man"Whatever, out of my way!"
                #the mc steps aside"
                show sc vivianwork v081
                old_man"Goddamn young’un’s these days. No respect for their elders, or the rich."
                #the old man grumbles and leaves the restroom
                #mc"(Well, he might be pissed off right now, but not as much as he’s going to be once he realises that I swiped this from inside his jacket.)"
                show sc vivianwork v082
                mc"(Well, he might be pissed off right now...)"
                show sc vivianwork v083
                mc"(But not as much as he’s going to be later on.)"
                #the MC holds up his wallet and opens it - he sees a few $50 bills in there"
                #mc"(Jackpot!)"
                #the MC holds onto the cash and the wallet
                #mc"(I’ll ditch the evidence once I’m outside...)"
                show sc vivianwork v084
                mc"(So generous of him to leave such a big tip for [mc_v_address].)"
                play sound "sound effects/01/toilet_flushing_sound_effect.mp3" fadein 0.5
                show sc vivianwork v085
                mc"Enjoy fishing your wallet out of the river you old prick!"
                $ v_ep01_06_01_Vivian_Work_Revenge = True
                stop sound fadeout 1.0
                stop music fadeout 1.0
                #screen goes blank
                scene black
                with dissolve
                scene black
                with Pause (2)
                #scene returns - the old man is at the counter
                play ambient "sound effects/01/quiet_restaurant_ambient_noise.ogg" loop fadein 1.0
                show sc vivianwork v086
                with dissolve
                old_man"I’m here to pay for the wonderful meal and the little extra helping."
                show sc vivianwork v087
                v"Sure..."
                show sc vivianwork v088
                v"(The sooner I get him out of here the better.)"
                show sc vivianwork v089
                v"Here’s your bill, Sir."
                show sc vivianwork v090
                old_man"Sure thing. Let me just get my wall-"
                #the old man reaches inside his pocket and realises his wallet is gone"
                old_man"Huh?"
                if persistent.v_anim_enabled:
                    show sc vivian work old man search
                else:
                    show sc vivianwork v091
                old_man"My wallet’s gone!!"
                old_man"(Where the fuck did I leave it?)"
                v"Well, you have to pay for your lunch, Sir."
                v"Do you have a major credit card that you can use?"
                show sc vivianwork v093
                old_man"Did you not hear me??"
                old_man"I just said my wallet is gone!"
                show sc vivianwork v094
                old_man"Wait!"
                old_man"The little pipsqueak! I ran into him in the bathroom."
                old_man"Where is he?"
                show sc vivianwork v095
                v"(Dammit, [y_name].)"
                v"(Please don’t tell me that you were behind this.)"
                show sc vivianwork v096
                v"Who are you talking about, Sir?"
                v"I don’t see any young men in the restaurant."
                show sc vivianwork v097
                old_man"(Fuck!! He’s long gone by now with my money!)"
                #the boss comes over - https://i.dailymail.co.uk/i/pix/2011/08/04/article-0-0D496EDF00000578-812_468x337.jpg"
                show sc vivianwork v097a
                boss"Is there a problem here, [v_name]?"
                show sc vivianwork v098
                with dissolve
                pause 1.0
                if not persistent.v_sex_anim_enabled_locked and persistent.v_sex_anim_enabled:
                    scene sc vivianwork v099 at tt_top
                    pause
                    old_man"(Gulp!)"
                    v"The gentleman can’t pay for his meal."
                    show sc vivianwork v100
                    boss"You’re going to have to come with me, Sir. We can figure out another way that you can pay for this."
                elif True:
                    show sc vivianwork v099
                    old_man"(Gulp!)"
                    v"The gentleman can’t pay for his meal."
                    show sc vivianwork v100a
                    boss"You’re going to have to come with me, Sir. We can figure out another way that you can pay for this."
                #old_man"(Shit... I don’t think I can talk my way out of this one.)"
                scene sc vivianwork v101
                old_man"Ughh... Fine."
                #the old man goes with the boss of the restaurant out the back"
                #screen goes blank"
                scene black
                with dissolve
                scene black
                with Pause (2)
                #scene returns - Vivian is at the front counter with her head down and she doesn’t notice the MC walking towards her"
                show sc vivianwork v102
                with dissolve
                show sc vivianwork v103
                mc"So... Did I miss anything important?"
                #Vivian looks up and sees the MC"
                show sc vivianwork v104
                v"You’re still here. I knew it!"
                #Vivian comes out from behind the counter and has a disappointed expression on her face"
                v"Why did you do that, [y_name]?"
                show sc vivianwork v016
                v"What if he finds out what you did?"
                show sc vivianwork v105
                mc"I’m not worried."
                mc"Besides, what’s he going to do?"
                show sc vivianwork v106
                mc"He’s an old fart and I’m nearly in the prime of my youth."
                #mc confident and a little cocky
                show sc vivianwork v107
                v"Hmm..."
                v"(He’s not wrong.)"
                show sc vivianwork v108
                mc"Look, I’m sorry, [mc_v_address]. I know you didn’t want me to do that."
                mc"But after what you told me about your problems with [mc_vic_address], I just didn’t like seeing that old guy treating you that way."
                mc"You don’t deserve that."
                show sc vivianwork v109
                mc"Continue scolding me now if you want to."
                #mc puts his head down, expecting the worst"
                show sc vivianwork v110
                v"That’s honestly the nicest thing anyone has done for me in a long, long time."
                show sc vivianwork v111
                v"Thank you, [y_name]."
                #Vivian kisses him on the cheek"
                play sound "sound effects/01/mwah_short_kissing_sound_effect3.mp3"
                show sc vivianwork v112
                v"Mwah!"
                show sc vivianwork v113
                mc"(Oh!)"
                $ rewards_unlock ("vivian",3)
                #THREE BONUS RENDERS OF VIVIAN (IN HER WAITRESS OUTFIT OR IN THE RESTAURANT) ADDED TO THE PHOTO GALLERY FOR HER PROFILE
                stop sound fadeout 1.0
                show sc vivianwork v114
                v"You better get out of here before he sees you."
                v"Bye, [y_name]."
                stop ambient fadeout 1.0
                #final shot is of Vivian smiling at the MC as he exits the restaurant"
                #screen goes blank
                scene black
                with dissolve
                scene black
                with Pause (2)
                #END SCENE
                if persistent.v_secrets_enabled and persistent.v_secrets_ep01_06_01_1:
                    label lb_ep01_06_01_Vivian_Work_1_fantasy_scene:
                        if not _in_replay:
                            scene img_secret_scene_overlay onlayer anim_layer
                            with { "anim_layer": dissolve}
                        else:
                            show screen scr_end_replay
                        show sc vivianwork v115
                        with dissolve
                        v"I can't believe [y_name]."
                        show sc vivianwork v116
                        v"I'm just glad he didn't get me fired."
                        show sc vivianwork v117
                        v"Although, it was pretty great of him to do that for me."
                        show sc vivianwork v118
                        v"I'd forgotten what it's like to have someone care about me so much. Lord knows [vic_name] never does anything like that for me."
                        v"[y_name]'s a really great guy. Any girl he ends up with would be lucky to have him."
                        show sc vivianwork v119
                        v"I just wish [vic_name] would act more like him."
                        show sc vivianwork v120
                        # Vivian starts acting like she is going to urinate
                        v"Someone with a good sense of morals, and who is not afraid to take business into their own hands when they need to."
                        play music "sound effects/01/Family_Feud.mp3" loop fadein 1.0
                        show sc vivianwork v121
                        #Instead we see her hand go down to inbetween her theighs
                        v"Someone young and strong, willing to do anything for me..."
                        #her hand starts to move up and down, the player not able to see, but its clear what she's doing.

                        if not persistent.v_sex_anim_enabled_locked and persistent.v_sex_anim_enabled:
                            show sc vivian work secret masturbate1
                        else:
                            show sc vivianwork v121a
                        v"Mmm... A man who takes care of me and tends to- mmm, my needs..."
                        v"Someone who would drop everything for me..."
                        if not persistent.v_sex_anim_enabled_locked and persistent.v_sex_anim_enabled:
                            show sc vivian work secret masturbate2
                        else:
                            show sc vivianwork v122
                        play sex2 "sound effects/01/sex/teasing_friends_pussy.ogg" loop
                        v"Oh fuck yes... Right there."
                        #He legs separate a bit more and we can see a bit more, but still not much
                        v"(I really wish I had someone like that right now to make my pussy theirs.)"
                        show sc vivianwork v124
                        v"Oh god, I need someone to fuck me good and hard... Right here, right now."
                        # Cuts to stall next to her where the other waitress has already been the whole time going to the bathroom
                        show sc vivianwork v125
                        cathy"(I can't believe what I'm hearing. It sounds like someone is masturbating in the next stall, and I think it's [v_name]!)"
                        v"Oh!"
                        if not persistent.v_sex_anim_enabled_locked and persistent.v_sex_anim_enabled:
                            show sc vivian work secret masturbate2
                        else:
                            show sc vivianwork v122
                        v"(How I've missed having someone go down on me and fucking me raw all night long!)"
                        # We see her hand start to reach down to her vagina
                        if not persistent.v_sex_anim_enabled_locked and persistent.v_sex_anim_enabled:
                            show sc vivian work secret co-worker masturbate1
                        else:
                            show sc vivianwork v126
                        cathy"(Wow! This is so hot!)"
                        if not persistent.v_sex_anim_enabled_locked and persistent.v_sex_anim_enabled:
                            show sc vivian work secret masturbate3
                        else:
                            show sc vivianwork v123
                        stop sex1 fadeout 1.0
                        play sex2 "sound effects/01/sex/woman_moaning_sound_effect.ogg" loop fadein 1.0
                        v"That's it, fuck me with that big cock..."
                        v"Fuck yes, give me that sweet release..."
                        if v_ep01_03_04_Vivians_Room_Remained:
                            v"I know you shot your cum all over my shower as you watched me last night, and I don't care!"
                            v"But now I want you to shoot that delicious seed deep inside of me!"
                        else:
                            v"I want your hot seed inside of me!"
                        show sc vivianwork v128
                        cathy"(She must be thinking about her husband. That is so hot!)"
                        show sc vivianwork v128a
                        cathy"(I need to lose this top.)"
                        if not persistent.v_sex_anim_enabled_locked and persistent.v_sex_anim_enabled:
                            show sc vivian work secret masturbate4
                        else:
                            show sc vivianwork v127
                        v"Yes, pound my pussy with that big cock of yours, I'm so close..."
                        v"Let me cum all over your cock!"
                        if not persistent.v_sex_anim_enabled_locked and persistent.v_sex_anim_enabled:
                            show sc vivian work secret co-worker masturbate2
                        else:
                            show sc vivianwork v129
                        cathy"(Shit, I'm going to cum with her...)"
                        cathy"(God I want to cum so badly, but I need to keep silent.)"
                        if not persistent.v_sex_anim_enabled_locked and persistent.v_sex_anim_enabled:
                            show sc vivian work secret masturbate5
                        else:
                            show sc vivianwork v130
                        stop sex1 fadeout 1.0
                        play sex2 "sound effects/01/sex/orgasm_sound.mp3"
                        v"NGHH!!" with hpunch
                        v"Yes, fuck me [y_name]!!" with hpunch
                        # Cuts to single outside shot of the manager looking in the direction of the bathrooms
                        show sc vivianwork v131
                        v"OH MY GOD!!"
                        show sc vivianwork v132
                        cathy"(Oh sweet jesus!)" with hpunch
                        cathy"(NGHH!)" with hpunch
                        stop sex2 fadeout 1.0
                        show sc vivianwork v133
                        v"Oh wow..."
                        v"I really needed that."
                        show sc vivianwork v134
                        cathy"(Oh wow, you and me both sister!)"
                        show sc vivianwork v135
                        cathy"(I've never squirted like that before. Mmm, I taste amazing.)"
                        show sc vivianwork v136
                        v"Shit, I hope nobody heard that."
                        show sc vivianwork v137
                        v"I should be ashamed of myself for doing that at work."
                        v"And worse yet, I'm pretty sure I called out [y_name]'s name."
                        v"What the hell is wrong with me??"
                        show sc vivianwork v140
                        v"(And why the hell am I talking to myself??)"
                        v"(It's just as well nobody else is in here.)"
                        show sc vivianwork v138
                        cathy"(I would have never expected that it wasn't her husband she was thinking about.)"
                        cathy"(But instead it was her [mc_v_rel]... That's even hotter!)"
                        show sc vivianwork v139
                        cathy"(I can't believe how hard I came when I heard her call out his name.)"
                        show sc vivianwork v140
                        v"(I know I should be more ashamed, but that was the most powerful orgasm I've had in a very long time.)"
                        v"(It felt better than I could've ever imagined. Damn, I really needed that.)"
                        show sc vivianwork v137
                        v"(I guess what he doesn't know won't hurt [y_name]. But I can't ever do that again.)"
                        v"(That was wrong in oh so many ways)."
                        show sc vivianwork v139
                        cathy"(It's probably best that I remain quiet until she leaves. I can't let her know that I was here the whole time.)"
                        cathy"(I have to admit though, it felt great to climax with her, even if she has no idea that I was even in here.)"
                        show sc vivianwork v141
                        cathy"(I wonder what would've happened if [v_name] found out that I was in the next stall.)"
                        show sc vivianwork v136
                        v"(Dammit, I better get cleaned up and back to work before they wonder where I've been...)"
                        stop music fadeout 1.0
                        scene onlayer anim_layer
                        with { "anim_layer": dissolve}
                        scene black
                        with dissolve
                        scene black
                        with Pause (2)
                        $ v_ep01_vivian_fantasy_counter += 1
                        $ persistent.replay_vivian_fantasy = False
                        $ renpy.end_replay()
                jump lb_ep01_06_01_Vivian_Work_3

label lb_ep01_06_01_Vivian_Work_2:
    show sc vivianwork v070
    mc"(No, I promised her that I wouldn’t do or say anything to this guy. And I don’t want her to lose her job because of me.)"
    show sc vivianwork v072
    mc"(I better get out of here...)"
    stop ambient fadeout 1.0
    scene black
    with dissolve
    scene black
    with Pause (2)
    #screen goes blank
    #END SCENE

label lb_ep01_06_01_Vivian_Work_3:
    #TEMP MENU UNTIL INTERACTABLE MENU MADE
    if(v_ep01_work_visit_options_3 == ""):
        show sc mctown m02
        with dissolve
        mc"(Okay, where to next?)"
        menu:
            "Clothing Store ([b_name])" if (v_ep01_work_visit_options_1 != "[b_name]" and v_ep01_work_visit_options_2 != "[b_name]"):
                #"If the player clicks on the CLOTHING STORE (scene with BELLA)"
                if v_ep01_work_visit_options_2 == "":
                    $ v_ep01_work_visit_options_2 = "[b_name]"
                else:
                    $ v_ep01_work_visit_options_3 = "[b_name]"
                scene black
                with dissolve
                pause 2.0
                jump lb_ep01_04_01_Bella_Work_1

            "Computer Shop ([a_name])" if (v_ep01_work_visit_options_1 != "[a_name]" and v_ep01_work_visit_options_2 != "[a_name]"):
                #"If the player clicks on the COMPUTER SHOP (scene with ARIEL)"
                if v_ep01_work_visit_options_2 == "":
                    $ v_ep01_work_visit_options_2 = "[a_name]"
                else:
                    $ v_ep01_work_visit_options_3 = "[a_name]"
                #the screen will go blank and take the player to the computer shop
                scene black
                with dissolve
                pause 2.0
                jump lb_ep01_05_01_Ariel_Work_1

            "Restaurant ([v_name])" if (v_ep01_work_visit_options_1 != "[v_name]" and v_ep01_work_visit_options_2 != "[v_name]"):
                #"If the player clicks on the RESTAURANT (scene with Vivian)"
                if v_ep01_work_visit_options_2 == "":
                    $ v_ep01_work_visit_options_2 = "[v_name]"
                else:
                    $ v_ep01_work_visit_options_3 = "[v_name]"
                #the screen will go blank and take the player to the restaurant"
                scene black
                with dissolve
                pause 2.0
                jump lb_ep01_06_01_Vivian_Work_1
    else:
        jump lb_ep01_06_02_Tattoo_Parlour_1
