init:
    $ ep03_01_07_vivian_robe_off = False
    $ v_ep03_vivian_hearts_counter = 0

    image sc evescenemcviv vivian fall:
        "sc evescenemcviv f032" with Dissolve(0.2, alpha=True)
        pause 1.0
        "sc evescenemcviv f033" with Dissolve(0.2, alpha=True)

label lb_ep03_01_07_Evening_scene_in_Vivians_bedroom:
    #SCENE BEGINS
    #the MC sits on the bed and Vivian stands before him
    scene sc evescenemcviv f001
    with dissolve
    mc"So what did you want to show me?"
    show sc evescenemcviv f002
    v"Stay right here, I need to change."
    show sc evescenemcviv f003
    v"I’ll be back shortly."
    show sc evescenemcviv f006
    with dissolve
    pause 1.0

    #Vivian goes into the bathroom
    play music "sound effects/01/Touch_and_Tension1.mp3" loop fadein 1.0
    show sc evescenemcviv f004
    with dissolve
    pause 2.0

    #show the MC waiting as he sits on the bed

    #show the MC looking around
    show sc evescenemcviv f007
    with dissolve
    mc"Do you need a hand at all?"

    #Vivian calls out from the bathroom
    show sc evescenemcviv f005
    v"No, I’m good."
    show sc evescenemcviv f005a
    with dissolve
    pause 1.0
    show sc evescenemcviv f005b
    with dissolve
    pause 2.0
    show sc evescenemcviv f005c
    with dissolve
    pause 2.0
    if not persistent.v_sex_anim_enabled_locked and persistent.v_sex_anim_enabled:
        scene sc evescenemcviv f005e at tt_top
        with dissolve
        pause 4.0
    elif True:
        show sc evescenemcviv f005d
        with dissolve
        pause 2.0
    scene black
    with dissolve
    scene black
    with Pause (2)
    scene black
    with dissolve
    centered "Several minutes later...{w=2.0}{nw}" with dissolve
    show text "Several minutes later..."
    scene bg black with Dissolve(1)
    pause 1.0
    scene black
    with dissolve

    show sc evescenemcviv f005
    with dissolve
    v"Okay, I’m coming out now..."

    #the door opens and we see Vivian dressed in the same green dress she showed the MC at the acting theatre in Episode 1
    #she also has a blonde wig on
    #https://pixhost.to/show/110/520242837_001.png
    show sc evescenemcviv f010
    with dissolve
    pause 1.5
    show sc evescenemcviv f011
    v"So, what do you think?"
    show sc evescenemcviv f012
    mc"Oh wow!"
    #The MC’s eyes widen
    show sc evescenemcviv f013
    mc"Is this for the..."
    show sc evescenemcviv f014
    v"The heist? Yeah, it is."
    show sc evescenemcviv f015
    v"I wanted you to be the first to see how I looked with my wig on."
    show sc evescenemcviv f016
    with dissolve
    pause 1.0
    show sc evescenemcviv f017
    with dissolve
    v"How do I look? Could I pass for a natural blonde?"
    #she does a quarter-turn
    #then a half turn so the MC can see her from behind
    #then another quarter-turn
    #then faces him again

    menu:
        "Wonderful":
            show sc evescenemcviv f021
            mc"You look wonderful, [mc_v_address!c]."
            show sc evescenemcviv f013
            mc"Like a natural blonde."
            show sc evescenemcviv f022
            v"Aww... Thanks, sweetheart."

        "Incredible"(wt="Bonus Image"):
            show sc evescenemcviv f021
            mc"You look incredible, [mc_v_address!c]."
            show sc evescenemcviv f013
            mc"You do the natural blonde look perfectly."
            $ rewards_unlock ("vivian",15)
            show sc evescenemcviv f022
            v"Aww... Thanks, sweetheart."

        "Sensational":
            show sc evescenemcviv f021
            mc"You look sensational, [mc_v_address!c]."
            show sc evescenemcviv f013
            mc"And yeah, all natural."
            show sc evescenemcviv f020
            mc"When we pull off this job, you'll be a huge reason why."
            show sc evescenemcviv f022
            v"Aww... Thanks, sweetheart."
    show sc evescenemcviv f020
    v"Oh, I have a couple more things to show you."
    show sc evescenemcviv f015
    v"Let me just get them out of my bag."

    #She bends down to pick a couple of things out of her bag - a hat and glasses
    show sc evescenemcviv f023
    with dissolve
    v"Here they are."

    #she stands back up and puts on her hat,
    #https://pixhost.to/show/110/520242841_002.png

    # And next she puts on her glasses and has a blank stare

    #https://pixhost.to/show/110/520242855_003.png
    show sc evescenemcviv f025
    with dissolve
    v"Actually, let me put the glasses on first."
    show sc evescenemcviv f023
    with dissolve
    pause 2.0
    show sc evescenemcviv f025b
    with dissolve
    pause 1.0
    show sc evescenemcviv f026a
    with dissolve
    pause 1.0
    v"Now how do I look?"
    show sc evescenemcviv f026
    menu:
        "Normal":
            show sc evescenemcviv f026
            mc"You look kind of normal, actually."
            show sc evescenemcviv f029
            v"Oh, that’s not really what I was aiming for."
            $ v_ep01_vivian_cocky_counter += 1
            show sc evescenemcviv f043
            v"I’ve heard that this woman has a real attitude problem, so I've been trying to get into character by pretending to be like her."
            show sc evescenemcviv f030
            v"I guess I can make some adjustments."

        "Snobby"(wt="Bonus Image"):
            show sc evescenemcviv f026
            mc"No offense, but you kind of look like an art snob, actually."
            show sc evescenemcviv f028
            $ rewards_unlock ("vivian",16)
            v"Awesome! That’s exactly what I was aiming for!"
            show sc evescenemcviv f043
            v"And I’ve heard that this woman has a real attitude problem, so I've been trying to get into character by pretending to be like her."
            show sc evescenemcviv f044
            v"So thanks."

        "Great":
            show sc evescenemcviv f026
            mc"Great, actually."
            show sc evescenemcviv f043
            v"That's a relief. I heard that this woman has a real attitude problem."
            show sc evescenemcviv f045
            v"I've been trying to get into character by pretending to be like her."
            show sc evescenemcviv f030a
            mc"Oh, right."
            show sc evescenemcviv f054
            mc"Well, I’m sure you’ll nail it on the day!"
            show sc evescenemcviv f050
            v"Thanks."

    #Vivian stumbles slightly in her heels. She’s off-balance
    show sc evescenemcviv vivian fall
    v"Woah!{w=2.0}{nw}"
    #the MC catches her before she falls to the floor
    play sound "sound effects/02/falling_over.mp3" noloop
    show sc evescenemcviv f034
    with faster_dissolve
    with vpunch
    mc"[mc_v_address!c]!"
    show sc evescenemcviv f035
    mc"Are you all right?"
    show sc evescenemcviv f036
    v"Yeah, I’m fine."
    show sc evescenemcviv f037
    v"Just felt a little woozy for a moment there."

    #show the empty bottle of wine  on the counter and her wine glass next to it
    show sc evescenemcviv f038
    mc"How much did you have to drink?"
    show sc evescenemcviv f040
    mc"Did you have the whole bottle?"
    show sc evescenemcviv f041
    v"Haha, maybe."
    show sc evescenemcviv f042
    v"Once I started, I just couldn’t stop."
    show sc evescenemcviv f043
    v"I figured that if [vic_name] drinks on weeknights, then why can't I?"
    #she looks disappointed
    show sc evescenemcviv f039
    mc"Yeah, you’re right, I suppose."
    mc"Just be careful not to overdo it, [mc_v_address!c]."
    show sc evescenemcviv f041
    v"I love how you care so much about me."
    show sc evescenemcviv f045
    mc"It’s nothing."
    #The MC brushes it off
    v"The girls do too you know?"
    show sc evescenemcviv f042
    mc"I’m aware."
    #she gives him bedroom eyes
    show sc evescenemcviv f046
    v"(I don’t know why, but lately, whenever it’s just the two of us, I feel even sexier than normal.)"

    #[Leave / Stick around]
    menu:
        "Leave"(wt="Bonus Image"):
            show sc evescenemcviv f047
            mc"Anyway... It seems like you’re doing better."
            show sc evescenemcviv f048
            mc"I’m heading off to bed as I have to be up in time to go with [a_name] to find some clothes at [b_name]’s store."
            show sc evescenemcviv f049
            v"Of course."
            show sc evescenemcviv f051
            v"Thanks for checking up on me."
            $ rewards_unlock ("vivian",17)
            show sc evescenemcviv f048
            mc"Are you sure you’re okay?"
            show sc evescenemcviv f044
            v"Honestly, you don’t have to keep asking me, [y_name]."
            show sc evescenemcviv f040
            mc"Yeah, but what about [mc_vic_address]?"
            show sc evescenemcviv f050
            v"I can handle him. Don’t worry so much about it."
            show sc evescenemcviv f051
            mc"Okay..."
            show sc evescenemcviv f048
            mc"You should probably change out of that dress."
            show sc evescenemcviv f052
            mc"You wouldn’t want to damage or stain it."
            show sc evescenemcviv f053
            v"Yeah, good point."
            show sc evescenemcviv f054
            mc"Night, [mc_v_address!c]."
            show sc evescenemcviv f048
            mc"And thanks again for dinner."
            mc"It was wonderful."
            show sc evescenemcviv f049
            v"You’re welcome, sweetheart."
            show sc evescenemcviv f050
            v"Goodnight..."
            show sc evescenemcviv f055
            with dissolve
            pause 1.5
            stop music fadeout 1.0
            #Final shot of Vivian smiling as the MC exits her room
            #SCENE ENDS
            scene black
            with dissolve
            scene black
            with Pause (2)
            jump lb_ep03_02_01_Training_in_The_Park_with_Zora

        "Stick around"(wt="Best option"):
            show sc evescenemcviv f056
            v"Anyway, I should get out of this dress."
            show sc evescenemcviv f057
            v"I wouldn’t want to ruin it, or stain it."
            stop music fadeout 1.0
            #without thinking Vivian starts stripping down to her underwear
            play music "sound effects/01/Temptation1.mp3" loop fadein 1.0
            show sc evescenemcviv f058
            with dissolve
            pause 1.0
            #start with her pulling at each of her shoulder straps
            show sc evescenemcviv f059
            with dissolve
            pause 1.0
            #then show it sliding down from the top
            show sc evescenemcviv f060
            with dissolve
            pause 1.0
            #show her bra-covered cleavage and her dress under it covering her stomach
            show sc evescenemcviv f061
            with dissolve
            pause 1.0
            #show the dress sliding off the rest of her body, a close-up of Vivian’s underwear
            show sc evescenemcviv f062
            with dissolve
            pause 1.0
            #show a full shot of Vivian in her bra and panties and still has her shoes on
            show sc evescenemcviv f012
            with dissolve
            mc"Uh... Would you like me to leave the room?"
            #The MC is sitting on her bed again now
            show sc evescenemcviv f064
            v"Why? I have nothing that you haven’t seen before, right?"
            show sc evescenemcviv f065
            mc"Excuse me?"
            show sc evescenemcviv f066
            v"A woman walking around in her underwear."
            show sc evescenemcviv f067
            v"Besides, I don’t see why it’s such a big deal."
            v"I’m not exactly amazing to look at, especially in my underwear."
            $ v_ep03_01_05_checking_on_Vivian_counter += 1
            #[Keep looking / Don’t look]
            menu:
                "Keep looking"(wt="Bonus Image"):
                    #the MC takes a look over at Vivian in her underwear. She looks depressed
                    #ROLLING SCREEN OF VIVIAN IN HER UNDERWEAR
                    if not persistent.v_sex_anim_enabled_locked and persistent.v_sex_anim_enabled:
                        scene sc evescenemcviv f069 at tt_top
                        with dissolve
                        pause 6.0
                    elif True:
                        show sc evescenemcviv f067a
                        with dissolve
                        pause 2.0
                    show sc evescenemcviv f062
                    with dissolve
                    pause 2.0
                    $ rewards_unlock ("vivian",18)
                    #show the dress sliding off the rest of her body, a close-up of Vivian’s underwear
                    scene sc evescenemcviv f061
                    with dissolve
                    pause 2.0
                    show sc evescenemcviv f068
                    with dissolve
                    mc"(...)"
                    $ v_ep01_vivian_cocky_counter += 1
                    pause 1.0
                    v"[y_name]?"
                    stop music fadeout 2.0

                "Don’t look":
                    #The MC looks away from her
                    show sc evescenemcviv f068
                    pause 2.0
                    v"[y_name]?"
                    $ v_ep01_vivian_respect_counter += 1
                    stop music fadeout 2.0
                    #scene continues BELOW

    #Vivian puts on a loose-fitting robe so we can still see the underwear she’s still wearing underneath
    #https://5.imimg.com/data5/WD/KU/OF/ANDROID-74592873/product-jpeg-500x500.jpg (example)
    #she stands before the MC who sits on the bed and she seems downhearted
    #She looks down at him when she says this
    show sc evescenemcviv f082
    with dissolve
    mc"Yeah, [mc_v_address!c]?"
    play music "sound effects/01/Family_Ties1.mp3" loop fadein 1.0
    show sc evescenemcviv f070
    with dissolve
    v"Why doesn’t [vic_name] love me anymore?"
    show sc evescenemcviv f065
    v"Why doesn’t he want..."
    show sc evescenemcviv f071
    with dissolve
    v"This?"
    #Vivian points at her own figure - https://pixhost.to/show/146/520741106_screenshot-2024-10-09-at-12-14-36-pm.jpg
    #THIS pose, but Vivian is in her underwear when she points to herself
    show sc evescenemcviv f072
    with dissolve
    pause 2.0


    #She’s not showing her body off to impress the MC, she genuinely thinks she’s unattractive to anyone
    #show a close-up of her body here
    show sc evescenemcviv f073
    with dissolve
    mc"It’s not your fault."
    show sc evescenemcviv f072
    v"Sorry honey. Let me just tie this back up."
    pause 1.5
    show sc evescenemcviv f074
    with dissolve
    v"You shouldn't really be seeing me like this."
    show sc evescenemcviv f079
    v"It's not fair on you."
    show sc evescenemcviv f063
    mc"It's fine, [mc_v_address!c]."
    show sc evescenemcviv f082
    mc"(She was quick to open then close her robe, which is a shame.)"
    #Compliment her / Tell her it’s [vic_name]’s fault]
    menu:
        "Compliment her"(wt="Best option"):
            #The MC looks concerned and genuine here
            mc"[mc_vic_address] has a wonderful, loving and beautiful person who has made it clear she will do anything for him, and he’s too blind to see any of it."
            show sc evescenemcviv f079
            v"You think I’m beautiful?"
            #She looks optimistic
            show sc evescenemcviv f075
            mc"Yes, of course. Even a blind man knows that you’re attractive!"
            show sc evescenemcviv f076
            v"Thank you, sweetheart."
            $ v_ep01_vivian_respect_counter += 1
            show sc evescenemcviv f079
            v"You have no idea how badly I needed to hear that."
            show sc evescenemcviv f078
            mc"I wouldn’t say that if I didn’t mean it."
            $ v_ep03_01_05_checking_on_Vivian_counter += 1

        "Tell her it’s [vic_name]’s fault":
            mc"[mc_vic_address] should be doing more for you. For all of us."
            #The MC looks agitated here
            show sc evescenemcviv f077
            mc"I’m honestly getting sick and tired of his shit."
            show sc evescenemcviv f078
            mc"The way he talks to you, to me, to the girls."
            show sc evescenemcviv f077a
            mc"Sometimes I wish something bad would happen to him."
            show sc evescenemcviv f074
            v"Don’t say that, honey."
            $ v_ep01_vivian_arrogant_counter += 1
            show sc evescenemcviv f079
            v"I know he can be difficult and he has a hard time showing his real emotions, but I’m sure he means well."
            show sc evescenemcviv f081
            mc"All I’m saying is, you deserve a hell of a lot better."

    show sc evescenemcviv f083
    v"I appreciate that, honey."


    show sc evescenemcviv f082
    mc"Anyway, it’s getting kind of late. So I should probably go to bed."
    show sc evescenemcviv f081
    mc"I don’t think I should be here if [mc_vic_address] suddenly bursts in."
    show sc evescenemcviv f083
    v"Yeah, that would be difficult to explain."
    show sc evescenemcviv f084
    v"Maybe even a little funny, depending on how you look at it."
    show sc evescenemcviv f082
    mc"I hope you’re okay now."
    show sc evescenemcviv f079
    v"Thank you for your concern and for checking up on me."
    show sc evescenemcviv f081
    mc"It’s my pleasure."
    if v_ep03_01_05_checking_on_Vivian_counter >= 4:
        $ vivian_love_level +=1
        $ v_ep03_vivian_hearts_counter +=1
    #The MC stands up and heads to the door to leave the room
    show sc evescenemcviv f085
    v"Hey..."
    show sc evescenemcviv f086
    with dissolve
    pause 2.0
    #he turns around and we see a full shot of Vivian in her underwear and robe standing up and looking at him
    show sc evescenemcviv f087
    v"Aren’t you gonna give me a kiss goodnight?"

    #"If the player has less than 2 Vivian Hearts
    if vivian_love_level <= 1:
        show sc evescenemcviv f088
        mc"Oh, sure. I can do that."
        play sound "sound effects/01/Male_kissing_girl_on_the_cheek.mp3" noloop
        show sc evescenemcviv f090
        mc"Mwah!"
        #The MC kisses her on the cheek
        show sc evescenemcviv f091
        v"Night, [y_name]."
        #she smiles as he kisses her on the cheek
        #Go down to scene continues
        stop music fadeout 1.0
        scene black
        with dissolve
        scene black
        with Pause (2)
        jump lb_ep03_02_01_Training_in_The_Park_with_Zora
    else:
        show sc evescenemcviv f088
        mc"Oh, sure. I can do that."
        stop music fadeout 1.0
        show sc evescenemcviv f146
        with dissolve
        pause 1.5
        show sc evescenemcviv f151
        with dissolve
        pause 1.5
        show sc evescenemcviv f142
        with dissolve
        pause 1.5
        show sc evescenemcviv f112
        with dissolve
        pause 1.5
        play music2 "sound effects/01/Touch_and_Tension.mp3" loop fadein 1.0
        play sound "sound effects/01/kiss_and_moan_sound_effect03.mp3" loop fadein 1.0
        show sc evescenemcviv f092
        with dissolve
        pause 2.0
        v"Mmm..."
        #The MC kisses Vivian on the lips, and they close their eyes as they embrace
        show sc evescenemcviv f093
        with dissolve
        pause 2.0
        #Then they tongue kiss
        stop sound fadeout 1.0
        #scene continues
        #Vivian stops and looks a little surprised
        show sc evescenemcviv f099
        with dissolve
        v"Sorry, I think we got a bit carried away there."
        show sc evescenemcviv f100
        with dissolve
        show sc evescenemcviv f101
        with dissolve
        v"(Though a part of me wishes he didn’t stop.)"
        show sc evescenemcviv f102
        with dissolve
        v"(It could be because of all the wine I drank.)"
        #she places a hand on the side of her head like she has a headache
        show sc evescenemcviv f103
        with faster_dissolve
        mc"Yeah, maybe we did."
        mc"Even so, it was nice, right?"
        show sc evescenemcviv f104
        v"Yeah, it was."
        with faster_dissolve
        #She softly smiles
        show sc evescenemcviv f105
        v"But let’s not overdo things, [y_name]."
        show sc evescenemcviv f106
        v"I’m still your-"
        show sc evescenemcviv f107
        mc"I know, I know."
        show sc evescenemcviv f105
        v"However... Kissing is okay."
        show sc evescenemcviv f099
        v"But no more than that."
        show sc evescenemcviv f153
        v"Before we continue, let me um... Tie my robe back up."
        show sc evescenemcviv f154
        v"Again..."
        pause 1.5
        show sc evescenemcviv f107
        with dissolve
        mc"Now that that's sorted, where were we?"

        #The MC and Vivian kiss again - full shot so we see them both
        play sound "sound effects/01/kiss_and_moan_sound_effect04.mp3" loop fadein 1.0
        show sc evescenemcviv f092
        with dissolve
        v"Mmm..."
        #then the two of them kiss and hold each other tightly
        show sc evescenemcviv f109
        v"(This feels so nice. Even more so after the evening I’ve had.)"
        show sc evescenemcviv f110
        with dissolve
        pause 2.0
        stop sound fadeout 1.0

        #the MC tries to undo the bind to Vivian's robe while they make out

        #Vivian steps back and looks at the MC
        show sc evescenemcviv f107
        with dissolve
        mc"On second thought..."
        show sc evescenemcviv f155
        with dissolve
        v"Honey, please don't do that."
        show sc evescenemcviv f151
        mc"But I wanna see all of you, [mc_v_address!c]."
        show sc evescenemcviv f153
        v"Sweetheart, what we're doing is enough already."
        show sc evescenemcviv f154
        with dissolve
        v"We shouldn't push our luck."
        v"And I've already shown you a lot more than I should have."
        show sc evescenemcviv f101
        with dissolve
        v"(It was wrong of me to flaunt my body in front of him.)"
        v"(Now I'm starting to regret it a little.)"
        show sc evescenemcviv f100
        with dissolve
        v"(I don't want him to get the wrong idea about me.)"
        #[Do it anyway / Listen to her]
        menu:
            "Do it anyway"(wt="Best option"):
                $ ep03_01_07_vivian_robe_off = True
                show sc evescenemcviv f152
                mc"I know, but this is my way of showing you how much I love the way you look no matter what."
                #the MC unbinds her robe - Vivian hesitantly looks down and watches him do it - we see her underwear underneath her robe
                show sc evescenemcviv f150
                with dissolve
                pause 1.0
                #then the MC pulls the robe off her shoulders with his hands
                show sc evescenemcviv f155
                with dissolve
                pause 1.0
                show sc evescenemcviv f156
                with dissolve
                pause 1.0
                #the robe falls off Vivians body, leaving her in her underwear before the MC
                show sc evescenemcviv f157
                with dissolve
                pause 1.0
                mc"Perfect..."
                $ v_ep01_vivian_cocky_counter += 1
                #show a tall behind shot of Vivian in just her underwear
                #ROLLING SCREEEN
                if not persistent.v_sex_anim_enabled_locked and persistent.v_sex_anim_enabled:
                    scene sc evescenemcviv f158 at tt_top
                    with dissolve
                    pause 6.0
                elif True:
                    show sc evescenemcviv f158a
                    with dissolve
                    pause 2.0
                play sound "sound effects/02/new_kissing_sound_FX1.mp3" loop fadein 1.0
                show sc evescenemcviv f161
                with dissolve
                v"Mmm..."
                #the MC and Vivian makeout while she's in her underwear
                show sc evescenemcviv f162
                with dissolve
                v"(Oh geez... I'm making out with [y_name] while I'm hardly wearing anything.)"
                #show a close-up of her body pressed up against the MC's while they makeout

                #[Squeeze her breast/ Fondle her ass]
                menu:
                    "Squeeze her breast"(wt="Bonus Image"):
                        show sc evescenemcviv f163
                        with dissolve
                        pause 2.0
                        $ rewards_unlock ("vivian",19)
                        show sc evescenemcviv f164
                        with dissolve
                        pause 2.0
                        #the MC cups her breast while they make out
                        #show a close-up
                        #and then one of the shots expanded out so we see both of them in the shot with the MC’s hand on her breast

                    "Fondle her asscheeks"(wt="Bonus Image"):
                        show sc evescenemcviv f165
                        with dissolve
                        pause 2.0
                        $ rewards_unlock ("vivian",20)
                        show sc evescenemcviv f166
                        with dissolve
                        pause 2.0
                        #the MC puts his hand on her ass while they make out
                        #show a close-up

                show sc evescenemcviv f167
                with dissolve
                pause 1.5
                show sc evescenemcviv f168
                with dissolve
                v"Oh, [y_name]!"
                #The MC kisses the side of Vivian's neck as she moans
                #then they hear someone coming up the stairs
                stop music2 fadeout 0.5
                stop sound fadeout 0.5
                play sound2 "sound effects/02/sound_from_upstairs_effect.mp3" noloop
                #Vivian tells him to hide in the bathroom
                show sc evescenemcviv f169
                with dissolve
                v"{i}(*Whispering*){/i}\nOh!"
                v"{i}(*Whispering*){/i}\nThat’s probably [vic_name]."
                show sc evescenemcviv f157
                with dissolve
                mc"(Shit!!)"
                show sc evescenemcviv f153a
                with dissolve
                v"{i}(*Whispering*){/i}\nI need to get my robe back on!"
                #Vivian picks up her robe from the floor and puts it back on
                pause 1.0
                stop sound2 fadeout 1.0
            "Listen to her":
                show sc evescenemcviv f150
                mc"Fine. I'll stop."
                $ v_ep01_vivian_respect_counter += 1
                show sc evescenemcviv f151
                mc"But can we continue what we were doing?"
                show sc evescenemcviv f105
                v"Yes, of course we can."
                play sound "sound effects/02/new_kissing_sound_FX.mp3" loop fadein 1.0
                show sc evescenemcviv f110
                with dissolve
                v"Mmm..."
                #they continue kissing
                #they hear someone coming up the stairs

                #[Stop / Cup her breast/ Grab her ass]
                menu:
                    "Stop":
                        pause 1.0

                    "Cup her breast":
                        show sc evescenemcviv f094
                        with dissolve
                        pause 2.0
                        show sc evescenemcviv f095
                        with dissolve
                        pause 2.0
                        #the MC cups her breast while they make out
                        #show a close-up
                        #and then one of the shots expanded out so we see both of them in the shot with the MC’s hand on her breast

                    "Grab her asscheeks":
                        show sc evescenemcviv f096
                        with dissolve
                        pause 2.0
                        show sc evescenemcviv f097
                        with dissolve
                        pause 2.0
                        #the MC puts his hand on her ass while they make out
                        #show a close-up
                        #and then one of the shots expanded out so we see both of them in the shot with the MC’s hand on her ass, under her robe
                stop sound fadeout 1.0
                show sc evescenemcviv f098
                with dissolve
                pause 1.0
                stop music fadeout 0.5
                play sound2 "sound effects/02/sound_from_upstairs_effect.mp3" noloop
                show sc evescenemcviv f111
                with dissolve
                pause 1.0
                #Vivian tells him to hide in the bathroom
                show sc evescenemcviv f113
                v"{i}(*Whispering*){/i}\nOh!"
                show sc evescenemcviv f112
                v"{i}(*Whispering*){/i}\nThat’s probably [vic_name]."
                show sc evescenemcviv f111
                mc"(Shit!!)"
                stop sound2 fadeout 1.0

    show sc evescenemcviv f114
    with dissolve
    v"{i}(*Whispering*){/i}\nQuick! Hide in the bathroom!"
    #the MC rushes off and hides in the bathroom
    show sc evescenemcviv f114a
    with dissolve
    pause 1.0
    play sound "sound effects/01/door_close_soft.mp3" noloop
    show sc evescenemcviv f114b
    with dissolve
    pause 1.0
    #Victor enters the bedroom
    play music "sound effects/01/Cool Vibes.mp3" loop fadein 1.0
    show sc evescenemcviv f115
    with dissolve
    vic"Oh, you’re still awake."
    show sc evescenemcviv f116
    #He says calmly
    v"Hey honey."
    show sc evescenemcviv f117
    v"How did things go with the client you drove around?"
    show sc evescenemcviv f118
    vic"Awful!"
    show sc evescenemcviv f119
    vic"Damn idiot couldn’t speak a word of English!"
    show sc evescenemcviv f120
    vic"I think he was Brazilian, or Chinese, or... something weird."
    show sc evescenemcviv f125
    vic"I wish they’d stop giving me these jobs where I have to drive around these moronic clients!"
    show sc evescenemcviv f126
    vic"Anyway, I’m busting to take a piss and then I’m gonna go to bed."
    show sc evescenemcviv f120
    vic"Don’t mind me, I’m gonna be a while so you can go to sleep."
    show sc evescenemcviv f122
    v"NO!"
    #Vivian blocks the bathroom door to stop him from entering
    show sc evescenemcviv f121
    v"I mean... You can’t go in there."
    show sc evescenemcviv f126
    vic"Why the fuck not??"
    show sc evescenemcviv f124
    v"It’s um... The toilet. It’s not flushing properly."
    show sc evescenemcviv f120
    vic"Really!? Are you fucking kidding me??"
    #He throws his arms up
    show sc evescenemcviv f125
    vic"What the hell, [v_name]?"
    show sc evescenemcviv f127
    vic"Have you been stuffing your tampons down there or something?"
    #Show a shot of Vivian’s ass from the MC’s point of view
    show sc evescenemcviv f128
    v"Um, no... I haven’t."
    show sc evescenemcviv f129
    v"Please, you don’t want to go in there, trust me."
    #She touches his arm to persuade him
    show sc evescenemcviv f132
    v"Just use the one downstairs."
    show sc evescenemcviv f130
    vic"Fine, whatever."
    show sc evescenemcviv f131
    vic"But I expect you to get that shitter fixed for me to use by tomorrow."
    show sc evescenemcviv f132
    v"I’ll look into it as soon as I get up in the morning."
    show sc evescenemcviv f133
    vic"Grr..."
    #Victor angry
    show sc evescenemcviv f134
    vic"By the way, you should tie your robe up."
    show sc evescenemcviv f135
    vic"The last thing [y_name] needs is to see you walking around with barely anything on."
    show sc evescenemcviv f123
    vic"You know how impressionable that kid is."
    show sc evescenemcviv f136
    v"(He sure is.)"
    #Vivian has a naughty look on her face
    show sc evescenemcviv f130
    vic"And I don't want to know why you're wearing that damn wig."
    vic"I don't want to see it again until the day of the heist, you hear me?"
    show sc evescenemcviv f137
    v"Oh, sure thing, [vic_name]."
    show sc evescenemcviv f138
    v"(My husband may not like seeing me like this, but at least one man in this house does.)"
    show sc evescenemcviv f139
    v"(The only one who matters to me right now.)"
    #Vivian has a daydream smile on her face

    #Victor leaves the bedroom and goes back downstairs

    #screen fades and then the MC exits the bathroom
    play sound "sound effects/01/door_close_soft.mp3" noloop
    stop music fadeout 1.0
    show sc evescenemcviv f139a
    with dissolve
    pause 3.0

    show sc evescenemcviv f140
    v"You better get out of here [y_name] before he comes back."
    show sc evescenemcviv f141
    mc"Okay."
    play music "sound effects/02/Late Night Whispers.mp3" loop fadein 1.0
    show sc evescenemcviv f103
    with dissolve
    mc"I’ll see you in the morning."
    show sc evescenemcviv f104
    v"Of course."
    if vivian_love_level >= 2:
        #the MC will kiss her here if the player has 2 VIVIAN HEARTS
        play sound "sound effects/01/kiss_and_moan_sound_effect06.mp3" loop fadein 1.0
        show sc evescenemcviv f108
        with dissolve
        pause 2.0
        v"Mmm..."
        show sc evescenemcviv f092
        with dissolve
        pause 2.0
        stop sound fadeout 1.0
        show sc evescenemcviv f091
        v"Okay, that's enough."
        #they embrace for a deep kiss
        show sc evescenemcviv f142
        mc"Night, [mc_v_address!c]."
        show sc evescenemcviv f144
        mc"And thank you for dinner."
        show sc evescenemcviv f145
        mc"It was wonderful."
        show sc evescenemcviv f143
        v"You’re welcome, sweetheart."
        show sc evescenemcviv f146
        v"Goodnight, [y_name]."
        show sc evescenemcviv f150
        mc"By the way."
        show sc evescenemcviv f149
        mc"Your robe has come undone again."
        v"(Damn! Haha!)"
        show sc evescenemcviv f152
        mc"Night..."
        show sc evescenemcviv f147
        with dissolve
        v"(Cheeky boy...)"
        pause 2.0
        #A final shot of Vivian in her underwear watching the MC leave the bedroom
    stop music fadeout 2.0
    #(screen goes blank)"
    scene black
    with dissolve
    scene black
    with Pause (2)
    jump lb_ep03_02_01_Training_in_The_Park_with_Zora
