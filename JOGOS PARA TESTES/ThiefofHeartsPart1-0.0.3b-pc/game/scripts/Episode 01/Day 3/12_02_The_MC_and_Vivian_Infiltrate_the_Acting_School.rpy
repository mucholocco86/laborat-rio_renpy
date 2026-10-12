init:
    $ v_ep01_day3_left_door = False
    $ v_ep01_day3_middle_door = False
    $ v_ep01_day3_right_door = False
    $ v_ep01_12_02_truthful_vivian = False
    $ v_ep01_task05_help_vivian_counter = 0
    $ v_ep01_day3_vivian_dress = "black"

label lb_ep01_The_MC_and_Vivian_acting_school1:
    #The MC and Vivian arrive at the acting school and they sit inside her car, surveying the back entrance
    #The MC looks through binoculars
    centered "A short time later...{w=2.0}{nw}" with dissolve
    show text "A short time later..." #THESE LINES ARE NOT DUPLICATES. Needed to fade the text in and out!
    scene bg black with Dissolve(1)
    pause 1.0
    scene sc vivianac v001
    with dissolve
    mc"Okay, let me see if I have this right."
    show sc vivianac v003
    mc"We’ll enter the theatre through the back entrance."
    show sc vivianac v004
    mc"You said that the door will be key-locked but we should have no issues getting in."
    show sc vivianac v005
    mc"There will be an acting class taking place around the time we’re stealing the items you need."
    show sc vivianac v006
    mc"Once we have the items, we carefully make our way back out the way we came in."
    show sc vivianac v007
    mc"Is that about right?"
    show sc vivianac v008
    v"Yeah, that’s correct."
    show sc vivianac v009
    v"Also, try not to make eye contact with anyone."
    show sc vivianac v010
    v"And we’ll also have to make sure not to make too much noise, as to not give ourselves away."
    show sc vivianac v011
    mc"Don’t worry. I'll be as quiet as a ninja in a pillow factory."
    show sc vivianac v012
    mc"Besides, I’m sure with your background in this field, if someone happens to see us, then you’re the perfect person to divert attention away."
    show sc vivianac v013
    v"Um... Yeah."
    #Vivian has a look of doubt
    #The MC looks through binoculars
    show sc vivianac v004
    mc"All right, it looks like the back entrance is clear now."
    show sc vivianac v014
    v"We should make our move..."
    $ renpy.music.set_volume(1.0, 0.0, channel="sound3")
    $ renpy.music.set_volume(1.0, 0.0, channel="sound4")
    $ ui.timer(0.1, Play("sound", "sound effects/01/car_door_opening.mp3"))
    $ ui.timer(0.3, Play("sound2", "sound effects/01/car_door_opening.mp3"))
    scene black
    with dissolve
    pause 1.0
    $ ui.timer(0.1, Play("sound3", "sound effects/01/car_door_closing.mp3"))
    $ ui.timer(0.5, Play("sound4", "sound effects/01/car_door_closing.mp3"))
    pause 2.0
    #cross screen fade
    #show the MC and Vivian outside the back of the acting theatre - the MC is in the middle of picking the lock
    play ambient "sound effects/01/street_sound_day_ambience.ogg" loop fadein 1.0
    show sc vivianac v015
    with dissolve
    pause 1.0
    stop sound fadeout 1.0
    stop sound2 fadeout 1.0
    stop sound3 fadeout 1.0
    stop sound4 fadeout 1.0
    mc"And I turn it like this, and..."
    play sound "sound effects/01/Door_Opening.mp3"
    show sc vivianac v016
    mc"Yahtzee!"
    stop ambient fadeout 1.0
    stop sound fadeout 1.0
    scene black
    with dissolve
    scene black
    with Pause (2)
    #Vivian enters through the back entrance, the MC looks around to make sure no one sees them, then enters and closes the door behind him
    play music "sound effects/01/Spy Glass.mp3" loop fadein 1.0
    show sc vivianac v018
    with dissolve
    v"Hmm..."
    show sc vivianac v017c
    with dissolve
    v"{i}(*Whispering*){/i}\nOkay... It’s a short walk to the dressing room which should be right over..."
    #Vivian looks around and sees the door to the dressing room.
    show sc vivianac v019
    v"{i}(*Whispering*){/i}\nThere."
    show sc vivianac v017d
    mc"{i}(*Whispering*){/i}\nOkay, I've set a timer."
    show sc vivianac v017a
    mc"{i}(*Whispering*){/i}\nTen minutes, and we're in and out."
    #They enter through to the dressing room door until they see all the costumes, dresses and wigs - https://media.istockphoto.com/id/154945972/photo/dressing-room.jpg?s=612x612&w=0&k=20&c=l6Kna67dCcK3cWCWXmWS7aXXM5jEYA3POud6GXYRYbA=
    show sc vivianac v017b
    v"Let's get to work then..."
    scene black
    with dissolve
    scene black
    with Pause (2)
    show sc vivianac v021
    with dissolve
    mc"Oh wow."
    show sc vivianac v023
    v"No time for dawdling, [y_name]."
    #The MC does so then looks around and is amazed by all the clothes and wigs
    show sc vivianac v024
    mc"Yes, of course."
    show sc vivianac v025
    mc"By the way, I can see why you wanted to come here."
    show sc vivianac v026b
    mc"This place has more than what we need."
    show sc vivianac v026
    v"I know. It’s the best theatre in the city."
    #Vivian looks through the wigs and finds a blonde one
    show sc vivianac v027
    v"I think this wig will do just nicely."
    show sc vivianac v028
    v"(I should be able to pull off the look [vic_name] wants with this.)"
    #She looks at the MC
    show sc vivianac v029
    v"Remember now, you keep watch just in case someone is coming this way."
    #The MC peers through the main door of the dressing room - https://media.gettyimages.com/id/200118382-001/photo/man-peering-around-slightly-open-door.jpg?s=1024x1024&w=gi&k=20&c=ztz-t23kejDwUmSNV72zqe3rVawBXCsluQnhTazwCEA=
    show sc vivianac v030
    mc"Sure thing, [mc_v_address]."
    show sc vivianac v031
    v"(I know I’ve seen a few of those dresses here before, that I’m going to need for this job.)"
    #Vivian pulls out a green/blue dress which is a classy nineteenth-century European-styled dress
    show sc vivianac v032
    v"(This one looks like it might be appropriate.)"
    show sc vivianac v033
    v"(But before we leave, I have to make sure that it’s going to fit.)"
    show sc vivianac v036
    v"[y_name]..."
    show sc vivianac v037
    mc"What’s up?"
    show sc vivianac v038
    v"I have to try this dress on, just to make sure the one I take is the right size."
    show sc vivianac v039
    v"Is there anyone out there?"
    #The MC checks outside the door to the hallway again
    show sc vivianac v040
    mc"No, the coast is still clear."
    show sc vivianac v041
    v"Okay, keep your eyes out there while I get changed."
    stop music fadeout 2.0
    #Show Vivian looking at the MC who is looking out the door
    show sc vivianac v042
    v"(I'm sure I can trust my [mc_v_rel] not to look.)"
    #Vivian puts a hand on one of the shoulder straps of her dress
    #show the MC’s face
    play music "sound effects/01/Midday_Mischief_with_Vivian.mp3" loop fadein 2.0
    show sc vivianac v043
    mc"(Ah, geez...)"
    show sc vivianac v044
    mc"(Okay, this is no big deal...)"
    show sc vivianac v045
    mc"(Except that [mc_v_address] is getting changed behind me.)"
    #[Peek /Keep watch]
    menu:
        "Peek"(wt="Task Point"):
            show sc vivianac v046
            mc"(One little peek won’t hurt, right?)"
            show sc vivianac v047
            pause 1.0
            #The MC looks back over his shoulder just as Vivian starts to remove her dress
            show sc vivianac v048
            mc"(Holy shit.)"
            #Vivian strips down to just her lingerie - she wears an alluring bra and underwear/panties, while still wearing heels - front/side view
            show sc vivianac v049
            mc"(Incredible...)"
            #She has her head down so she doesn’t know the MC is looking at her
            #show sc vivianac v052
            #ROLLING SCREEN HERE
            show sc vivianac v049b
            mc"(Damn... her ass is something else.)"
            mc"(She's certainly defying her age.)"
            show sc vivianac v050
            mc"(Aww... She's covering her chest.)"
            show sc vivianac v050a
            mc"(No, don't turn around!!)"
            mc"(Then again, it's still a pretty good view.)"
            show sc vivianac v050b
            v"(Let’s hope this one fits.)"
            show sc vivianac v053
            v"(Hmm... It feels pretty good.)"
            #Vivian bends down to step into the dress, giving the MC an incredible view of her cleavage
            show sc vivianac v054
            mc"(God damn...)"
            #A close-up of her hanging cleavage
            show sc vivianac v055
            mc"(Those things could have saved the Titanic...{w} Probably.)"
            #Vivian pulls her dress up so it covers her body
            show sc vivianac v057
            v"(There we go. It’s perfect!)"
            #The MC turns away and looks out the door
            show sc vivianac v058
            v"Ahem! You can turn around now, [y_name]."
            show sc vivianac v059
            v"So what do you think?"
            #The MC turns back and looks at Vivian in the dress
            #ROLLING SCREEN OF VIVIAN
            #show sc vivianac v059b
            show sc vivianac v058b
            mc"(Wow...)"
            show sc vivianac v060
            mc"Damn... You look perfect."
            show sc vivianac v061
            v"Are you sure it doesn’t make me look fat?"
            show sc vivianac v062
            mc"Don’t be ridiculous."
            mc"You’re like Mary Antoinette re-incarnated!"
            show sc vivianac v063
            mc"Just ignore the fact she was guillotined, of course."
            play sound "sound effects/01/sexy_female_laugh1.mp3" fadein 1.0
            show sc vivianac v065
            v"Haha!"
            stop sound fadeout 1.0
            show sc vivianac v066
            v"My [mc_v_rel] knows his history. Very good."
            $ v_ep01_task05_help_vivian_counter += 1
            show sc vivianac v067
            v"All right, I’ll just change back into my clothes so continue to keep watch, and then I’ll let you know when we can get out of here."
            #The MC turns away again and looks out the door
            show sc vivianac v068
            mc"(Okay, I had a good look already.)"

    #[Keep watch / Peek again]
            menu:
                "Keep watch":
                    show sc vivianac v069
                    mc"(As tempting as it is to check her out again, I better do as I’m told this time.)"
                    show sc vivianac v070
                    mc"(Knowing my luck, someone will show up when I let my guard down.)"
                    stop music fadeout 1.0
                    scene black
                    with dissolve
                    scene black
                    with Pause (2)

                    #GO DOWN TO > #scene continues

                "Peek again"(wt="Task Point"):
                    show sc vivianac v071
                    mc"(But who knows when I’ll get this chance again?)"
                    #The MC turns and this time Vivian has her back turned so the MC can see her ass in a g-string
                    show sc vivianescape v01
                    with dissolve
                    pause 1.0
                    show sc vivianescape v02
                    with dissolve
                    pause 1.0
                    show sc vivianac v050a
                    with dissolve
                    pause 1.0
                    #ROLLING SCREEN HERE
                    #show sc vivianac v054
                    show sc vivianescape v03
                    with dissolve
                    mc"(Blimey...)"

                    #ROLLING SCREEN HERE
                    show sc vivianac v056
                    mc"(I'm so happy I agreed to join her on this heist.)"
                    show sc vivianescape v05
                    mc"(To think, I could have missed out on seeing this.)"
                    $ v_ep01_task05_help_vivian_counter += 1
                    show sc vivianac v054
                    mc"(Fuck me...)"
                    show sc vivianescape v04
                    mc"(If only she would show me just a little bit more.)"
                    $ rewards_unlock ("vivian",5)
                    show sc vivianac v273
                    with dissolve
                    pause 1.0
                    show sc vivianac v274
                    with dissolve
                    pause 1.0
                    #Vivian pulls up her original dress from behind
                    show sc vivianac v046
                    with dissolve
                    mc"(Okay, that’s enough.)"
                    mc"(I better not push my luck.)"
                    #The MC turns away and looks out the door
                    stop music fadeout 1.0
                    scene black
                    with dissolve
                    scene black
                    with Pause (2)
                    #GO DOWN TO > #scene continues

        "Keep watch":
            show sc vivianac v069
            mc"(As tempting as it is to look, I better do as I’m told.)"
            show sc vivianac v070
            mc"(Knowing my luck, the second I take my eyes away from this hallway, someone will show up!)"
            scene black
            with dissolve
            scene black
            with Pause (2)

            show sc vivianac v058
            with dissolve
            v"Ahem! You can turn around now, [y_name]."
            show sc vivianac v059
            v"So what do you think?"
            #The MC turns back and looks at Vivian in the dress
            #ROLLING SCREEN OF VIVIAN
            #show sc vivianac v059b
            show sc vivianac v058b
            mc"(Wow...)"
            show sc vivianac v060
            mc"Damn... You look perfect."
            show sc vivianac v061
            v"Are you sure it doesn’t make me look fat?"
            show sc vivianac v062
            mc"Don’t be ridiculous."
            show sc vivianac v063
            mc"You’re like Mary Antoinette re-incarnated!"
            show sc vivianac v064
            mc"Just ignore the fact she was guillotined, of course."
            play sound "sound effects/01/sexy_female_laugh1.mp3" fadein 1.0
            show sc vivianac v065
            v"Haha!"
            stop sound fadeout 1.0
            show sc vivianac v066
            v"My [mc_v_rel] knows his history. Very good."
            show sc vivianac v067
            v"All right, I’ll just change back into my clothes so continue to keep watch, and then I’ll let you know when we can get out of here."
            #The MC turns away again and looks out the door
            stop music fadeout 1.0
            scene black
            with dissolve
            scene black
            with Pause (2)

            #scene continues

    #The MC sees someone in the hallway
    scene sc vivianac v069
    with dissolve
    mc"(I hope she's just about-)"
    show sc vivianac v072
    with vpunch
    mc"{i}(*Whispering*){/i}\nOh shit!"
    show sc vivianac v041
    v"{i}(*Whispering*){/i}\nWhat’s wrong?"
    show sc vivianac v074
    mc"{i}(*Whispering*){/i}\nThere’s a guy out there!"
    mc"{i}(*Whispering*){/i}\nIf he sees us, then we're screwed!"
    show sc vivianac v276
    v"{i}(*Whispering*){/i}\nWhat are we going to do?"
    #The MC exits the changing room
    show sc vivianac v076
    mc"{i}(*Whispering*){/i}\nLeave it to me. I’ll see if I can talk my way out of this."
    #Vivian looks concerned
    show sc vivianac v275
    v"{i}(*Whispering*){/i}\n[y_name]..."
    play sound "sound effects/01/door_close_soft.mp3" fadein 1.0
    show sc vivianac v277
    v"(Dammit... He's gone.)"
    show black
    with dissolve
    #show the MC outside in the hallway
    stop sound fadeout 1.0
    scene sc vivianac v079
    with dissolve
    mc"Excuse me."
    show sc vivianac v081
    un"Who are you? And what were you doing in the costumes and props room?"
    show sc vivianac v084
    mc"Sorry, I’m just a little lost. This is my first time at this theatre."
    show sc vivianac v083
    un"Wait! I know exactly who you are."
    show sc vivianac v082
    mc"You... You do??"
    #The MC looks concerned
    show sc vivianac v083
    un"Yeah, the teacher said that you might be wandering around."
    show sc vivianac v085
    un"You’re here for the acting class, right?"
    show sc vivianac v088
    mc"Uh, yeah, that’s me!"
    show sc vivianac v087
    mc"Sorry, I must have taken a wrong turn somewhere."
    show sc vivianac v086
    un"Completely understandable."
    show sc vivianac v089
    un"The first time I came here I managed to get stuck in a broom closet!"
    show sc vivianac v087
    mc"I see.."
    show sc vivianac v090
    un"Anyway, you better come with me as they’ve already started."
    show sc vivianac v082
    mc"(Uh-oh... What the hell have I got myself into this time?)"
    mc"(So much for that good luck going my way,)"
    show sc vivianac v082b
    mc"(Hmm... Why does this corridor look so familiar?)"
    mc"(It kind of reminds me of the inside of a hotel...)"
    #screen goes blank
    scene black
    with dissolve
    scene black
    with Pause (2)


    #Show Vivian in the changing room after the MC has left with the theatre actor
    show sc vivianac v042
    with dissolve
    v"(I’m going to have to do this alone then.)"
    show sc vivianac v041
    v"(I’ll put everything in a bag, just in case someone sees me on my way out.)"
    show sc vivianac v031
    v"(It will be less suspicious that way.)"
    #show Vivian placing the wig and dress in the carry bag she finds)
    show sc vivianescape v06
    with dissolve
    v"(Okay, I have the dress, and also a wig, that should be about it.)"
    #Vivian holds the carry bag and prepares to leave the room
    show sc vivianescape v07
    v"(I better go and find [y_name].)"
    v"(Who knows what kind of mess he’s gotten himself into this time...)"
    #screen goes blank
    scene black
    with dissolve
    scene black
    with Pause (2)


    #The MC enters the small theatre where there is a stage and a few other members of the acting class
    #There are a couple of people on the stage acting out a scene
    #One is a skinny guy and the other is an old man sitting in a chair
    show sc vivianac v095
    with dissolve
    man"You know, you can’t just push people around Mister Topper."
    #The MC takes a seat and waits for them to finish
    show sc vivianac v096
    man"You know what you are?"
    show sc vivianac v097
    man"You're a bitch."
    show sc vivianac v098
    man"You’re a salty little bitch and I bet you like it from both ends!"
    show sc vivianac v099
    older_man"Oh yeah? Well, you're nothing more than a wilted lettuce leaf."
    older_man"Limp, lifeless, and nobody's first choice. "
    #The drama coach stands in front of the stage with the other actors seated behind her
    show sc vivianac v101
    drama_coach"Stop, stop, stop...!"
    show sc vivianac v102
    drama_coach"Ughh... What is it with this class today?"
    #The coach puts his head to his forehead and closes his eyes
    show sc vivianac v103
    drama_coach"Get off my stage."
    #The two actors leave the stage and take a seat in the audience
    #The drama teacher addresses her actors
    show sc vivianac v104
    drama_coach"People... Acting isn't just about memorizing lines and putting on a show."
    show sc vivianac v105
    drama_coach" It's about diving deep into the human experience, exploring emotions, and telling stories that resonate with audiences."
    #The drama teacher has her arms/hand outstretched like this - https://img.freepik.com/free-photo/how-could-you-portrait-frustrated-upset-shocked-young-african-american-man-reaching-hands-forward-shake-arms-frowning-grimacing-angry-camera-white-background_176420-52685.jpg
    show sc vivianac v106
    drama_coach"It's about stepping into someone else's shoes and seeing the world through their eyes."
    show sc vivianac v107
    drama_coach"Am I getting through to any of you or am I just wasting my time?"
    #The drama coach notices the MC sitting in the audience and points to him
    show sc vivianac v109
    drama_coach"You!"
    show sc vivianac v108
    drama_coach"Who are you?"
    show sc vivianac v111
    un"Yo, Miss Fonzarelli!"
    show sc vivianac v112
    un"I found your guy wandering around out back."
    show sc vivianac v110
    drama_coach"You’re new here?"
    show sc vivianac v114
    mc"Um, yes, I am."
    show sc vivianac v115
    drama_coach"Ah, so you’re the gentleman who emailed me."
    drama_coach"You're the young actor from Darkham City, right?"
    show sc vivianac v116
    mc"That’s me. And yes, I am."
    show sc vivianac v124
    mc"(Where the fuck is Darkham City??)"
    #The drama coach
    show sc vivianac v118
    drama_coach"All right then. Up you go."
    show sc vivianac v119
    mc"Excuse me?"
    show sc vivianac v120
    un"Onto the stage, kid."
    show sc vivianac v121
    mc"Oh, um... I feel like it would be better if I let everyone else do their thing and tomorrow I’ll be ready to-"
    show sc vivianac v122
    drama_coach"You’re holding up my class!"
    show sc vivianac v123
    drama_coach"Now get up there!"
    show sc vivianac v124
    mc"(Shit...)"
    mc"(I won't be able to talk my way out of this one.)"
    #The MC takes the side stairs to get to the stage as the drama coach heads back down to the floor
    show sc vivianac v117
    mc"(And how will I know when [mc_v_address] has the things that we came here for?)"
    show sc vivianac v125
    mc"(I better get up there before I further piss off Mary Poppins...)"
    scene black
    with dissolve
    scene black
    with Pause (2)

    #show Vivian walking through a corridor trying to find the right theatre that the MC is in
    play music "sound effects/01/Midnight Heist.mp3" loop fadein 1.0
    show sc vivianescape v08
    with dissolve
    v"(I have no idea where [y_name] was taken to by that theatre actor.)"
    #Vivian looks around and looks lost, confused
    show sc vivianescape v09
    v"(This place has changed a lot.)"
    v"(No surprises I guess, considering that it’s been almost twenty years since I was last here.)"
    #show three doors at the end of a corridor
    show sc vivianescape v10
    v"(Maybe he’s in one of these rooms.)"

    #[Door to the left / Middle door / Door to the right]

    #MINI-GAME - The trick to this is if the player picks the correct door the first time asking, then they will get three options in the second set of options further below

    #If they get it right the second time of guessing, they will only get two options

    #If they take three goes to get the right door, only one option will be available

    #"Door to the right" is the correct answer
label lb_ep01_day3_door_options:

    menu:
        "Door to the left":
            if v_ep01_day3_left_door == False:
                $ v_ep01_day3_left_door = True
                show sc vivianescape v10
                v"(Maybe he’s in this door.)"
                #Vivian opens the door and it’s just a broom closet
                show sc vivianescape v12
                with dissolve
                v"(Hmm... Not even close. It’s just a cleaners closet.)"
                scene black
                with dissolve
                scene black
                with Pause (2)
                scene sc vivianescape v10
                with dissolve
                #The menu options are now - Middle Door / Door to the Right
                jump lb_ep01_day3_door_options
            v"(I've already tried that door.)"
            jump lb_ep01_day3_door_options


        "Middle door":
            if v_ep01_day3_middle_door == False:
                $ v_ep01_day3_middle_door = True
                show sc vivianescape v10
                v"(Maybe he's in there.)"
                #Vivian opens the door and it’s just a storage room
                show sc vivianescape v11
                with dissolve
                v"(Hmm... It looks like a room for file storage.)"
                scene black
                with dissolve
                scene black
                with Pause (2)
                scene sc vivianescape v10
                with dissolve
                #The menu options are now - Door to the left / Door to the Right
                jump lb_ep01_day3_door_options
            v"(I've already tried that door.)"
            jump lb_ep01_day3_door_options

        "Door to the right"(wt="Task Point"):
            if v_ep01_day3_right_door == False:
                $ v_ep01_day3_right_door = True
                show sc vivianescape v10
                v"(That could be it.)"
                #Vivian opens the door and finds another clothing/changing room
                #the room contains numerous gowns and costumes compared to the other changing room
                #https://res.cloudinary.com/mtc-2018/image/upload/c_fit,f_auto,q_auto:eco,w_1000/MTC-BTC-Tim-Grey-59.jpg
                show sc vivianescape v14
                with dissolve
                v"(Oh... What’s this room?)"
                $ v_ep01_task05_help_vivian_counter += 1
                #Go Down to Vivian inside the Costumes Room


    #Costumes Room
    #Show Vivian looks at a closed wardrobe

    #Vivian goes over to an open wardrobe and opens it
    show sc vivianescape v15
    v"(These look like more costumes and outfits.)"
    #Vivian shuffles through the dresses - https://c8.alamy.com/comp/2K2BB8C/woman-going-through-her-clothes-rear-view-of-a-woman-going-through-the-clothes-in-her-closet-2K2BB8C.jpg
    show sc vivianescape v16
    with dissolve
    v"(Oh wow! There’s a lot more in here than the other room.)"
    show sc vivianescape v18
    with dissolve
    v"(Well, I’ve already taken a couple of things, so stealing another dress isn’t going to make much difference.)"
    show sc vivianescape v17
    with dissolve
    v"(I should look for something that I could wear for [vic_name].)"
    v"(I might be able to surprise him.)"
    show sc vivianescape v15
    v"(But what drawer should I choose?)"

    #[Left / Middle / Right]

    #Second set of options
    #IF the player found the correct door in one guess, then they will get ALL THREE options below

    #IF the player found the correct door with their second guess, then they will get the "Left" and "Right" options only

    #IF the player found the correct door with their third guess, then they will get the "Left" option only

    #The dress for the Middle" option will be what Vivian takes with her and will wear during Episode 2

    menu:
        "Top Drawer":
            #Vivian checks the left side of the inside of the wardrobe
            show sc vivianescape v19
            v"(Oh, this one looks interesting.)"
            #Vivian puts this dress up against her body - https://www.daz3d.com/seductive-queen or https://www.daz3d.com/dforce-headline-outfit-for-genesis-8-females (the red one)
            show sc vivianescape v26
            v"(I wonder how it would look on me?)"
            #BONUS VIVIAN IMAGE ADDED TO HER GALLERY OF HER IN THIS OUTFIT
            show sc vivianescape v23
            v"(It's pretty sexy, very eye-catching.)"
            #Vivian puts the dress up against her body
            show sc vivianescape v19
            v"(Yeah, I’m going to take this black one.)"
            #Vivian checks the middle of the wardrobe and finds this dress - https://www.daz3d.com/z-fatal-attraction-poses-and-partials-for-genesis-3-and-8-female
            show sc vivianescape v25
            v"(I might wear this for [vic_name] later in the week, when he least suspects it.)"
            show sc vivianescape v22b
            v"(I just hope I’m not going to all this effort for nothing.)"
            show sc vivianescape v26
            v"(But I have to do something to spice up our marriage.)"
            #Vivian looks hopeful
            show sc vivianescape v24
            v"(Anything for my husband to look at me like he use to.)"
            #screen goes blank
            show sc vivianescape v22b
            v"(I better get back to the task at hand.)"
            v"(I have to find [y_name]!!)"
            $ v_ep01_day3_vivian_dress = "black"


        "Middle Drawer"(wt="Task Point"):
            #Vivian checks the middle of the inside of the wardrobe
            show sc vivianescape v23b
            v"(Oh, this one looks interesting.)"
            #Vivian puts this dress up against her body - https://www.daz3d.com/z-fatal-attraction-poses-and-partials-for-genesis-3-and-8-female
            show sc vivianescape v25b
            v"(I wonder how it would look on me? Or if it’s sexy enough?)"
            #BONUS VIVIAN IMAGE ADDED TO HER GALLERY OF HER IN THIS OUTFIT
            show sc vivianescape v20
            v"(Yeah, I’m going to take this red one.)"
            $ v_ep01_task05_help_vivian_counter += 1
            show sc vivianescape v26b
            v"(I might wear this for [vic_name] later in the week, when he least suspects it.)"
            show sc vivianescape v22
            v"(I just hope I’m not going to all this effort for nothing.)"
            show sc vivianescape v26b
            v"(But I have to do something to spice up our marriage.)"
            #Vivian looks hopeful
            show sc vivianescape v24b
            v"(Anything for my husband to look at me like he use to.)"
            show sc vivianescape v22
            v"(I better get back to the task at hand.)"
            v"(I have to find [y_name]!!)"
            $ v_ep01_day3_vivian_dress = "red"

        "Bottom drawer":
            #Vivian checks the right side of the inside of the wardrobe
            show sc vivianescape v21
            v"(Oh, this one looks interesting.)"
            #Vivian puts this dress up against her body - https://www.daz3d.com/dforce-greek-princess-outfit-set-for-genesis-8-and-81-females
            show sc vivianescape v26c
            v"(I wonder how it would look on me?)"
            #BONUS VIVIAN IMAGE ADDED TO HER GALLERY OF HER IN THIS OUTFIT
            show sc vivianescape v23c
            v"(It's pretty sexy, very eye-catching.)"
            #Vivian puts the dress up against her body
            show sc vivianescape v25c
            v"(Hmm... Should I do it?)"
            show sc vivianescape v21
            v"(Yeah, I’m going to take this golden one.)"
            #Vivian checks the middle of the wardrobe and finds this dress - https://www.daz3d.com/z-fatal-attraction-poses-and-partials-for-genesis-3-and-8-female
            show sc vivianescape v25c
            v"(I might wear this for [vic_name] later in the week, when he least suspects it.)"
            show sc vivianescape v22c
            v"(I just hope I’m not going to all this effort for nothing.)"
            show sc vivianescape v26c
            v"(But I have to do something to spice up our marriage.)"
            #Vivian looks hopeful
            show sc vivianescape v24c
            v"(Anything for my husband to look at me like he use to.)"
            show sc vivianescape v22c
            v"(I better get back to the task at hand.)"
            v"(I have to find [y_name]!!)"
            $ v_ep01_day3_vivian_dress = "golden"


    stop music fadeout 1.0
    #screen goes blank
    scene black
    with dissolve
    scene black
    with Pause (2)



    show sc vivianac v126
    with dissolve
    mc"All right, so what do I do?"
    show sc vivianac v127
    drama_coach"The topic was family disagreements, but now the theme is \"Karma\"."
    show sc vivianac v128
    drama_coach"Give me a sixty-second monologue about this topic."
    show sc vivianac v129
    mc"By myself?"
    show sc vivianac v130
    drama_coach"Do you see anyone else on that stage with you?"
    show sc vivianac v131
    mc"Okay, well..."
    mc"Karma..."
    #Vivian watches from the side of the stage, hiding behind a curtain
    show sc vivianac v132
    v"(What is he doing??)"
    #The MC looks down at the floor and is nervous
    show sc vivianac v133
    mc"Well, you see, karma is like this mystical thing, right?"
    show sc vivianac v134
    mc"It's supposed to be all about cause and effect, like what goes around comes around and stuff."
    show sc vivianac v135
    mc"But honestly, who really believes in that? I mean, come on, bad things happen to good people all the time, and vice versa."
    show sc vivianac v136
    mc"It's just a coincidence, right? Plus, if karma were real, wouldn't we all be living in some kind of cosmic utopia by now?"
    show sc vivianac v137
    mc"So yeah, karma's a nice idea, but let's face it, life's just a random mess and we're all just trying to make sense of it."
    #Vivian still watches from the side of the stage, hiding behind a curtain
    show sc vivianac v138
    v"(Oh, [y_name]...)"
    #Vivian watches from the side of the stage, hiding behind a curtain
    #Everyone including the audience looks unconvinced by the MC’s speech with their arms folded
    show sc vivianac v139
    drama_coach"What’s your name again?"
    show sc vivianac v140
    mc"It’s um... It’s [y_name]."
    show sc vivianac v141
    mc"[y_name] Galvan."
    show sc vivianac v142
    drama_coach"Well, Mister Galvan, you need to hear this."
    show sc vivianac v144
    drama_coach"Let me be the first and probably only person to tell you that..."
    show sc vivianac v145
    drama_coach"...that monologue was the worst piece of acting, probably in the history of theatre."
    show sc vivianac v146
    drama_coach"That performance was like my ex-husband’s old coffee table."
    show sc vivianac v143
    drama_coach"Wooden and boring."
    show sc vivianac v147
    drama_coach"Do you know why?"
    show sc vivianac v148
    drama_coach"I saw no truth in your monologue, no actual examples of how karma has affected you personally."
    show sc vivianac v139
    drama_coach"It was like a performance from a high-school dropout reading from a dictionary."
    show sc vivianac v149
    drama_coach"I’ve seen more life from patients in a coma."
    show sc vivianac v150
    mc"Wow... Harsh."
    show sc vivianac v145
    drama_coach"This is a professional acting class, Mister Galvan."
    show sc vivianac v144
    drama_coach"And my theatre is no place for phonies."
    show sc vivianac v142
    drama_coach"I recommend that once this class is over, you return to that pigeonhole town you call Darkham City."
    show sc vivianac v145
    drama_coach"Because to be perfectly frank, acting is not for you."

    #[Stand down / Be truthful]
    menu:
        "Stand down":
            show sc vivianac v143
            mc"(I better get off this stage before I make things worse.)"
            #The MC walks off the stage and heads back to his seat
            show sc vivianac v140
            mc"(I sure hope [mc_v_address] never performed in front of this woman, because she sounds like a psycho hose beast!)"
            #screen goes blank
            scene black
            with dissolve
            scene black
            with Pause (2)

            #The MC heads outside and meets up with Vivian in the parking lot
            play ambient "sound effects/01/street_sound_day_ambience.ogg" loop fadein 1.0
            show sc vivianac v157
            with dissolve
            v"[y_name]! Where were you?"
            show sc vivianac v158
            mc"I was stuck in that stupid acting class!"
            show sc vivianac v159
            mc"That teacher running it wouldn’t let anyone leave until it was finished."
            show sc vivianac v160
            mc"It was horrible."
            show sc vivianac v161
            v"I know. I saw it."
            show sc vivianac v162
            mc"You did?"
            show sc vivianac v163
            v"Yeah... I’m afraid so."
            show sc vivianac v164
            mc"I honestly have no idea what I was trying to say."
            show sc vivianac v165
            mc"I bumbled through it like a clown in a circus, tripping over my own oversized shoes and making a fool out of myself."
            show sc vivianac v166
            v"I’m sorry that you had to go through that sweetheart."
            if v_ep01_task05_help_vivian_counter == 5:
                $ task_completed(5,"aa")
                $ v_ep01_vivian_aa_tasks_counter += 1
            if v_ep01_task05_help_vivian_counter == 4:
                $ task_completed(5,"a")
            if v_ep01_task05_help_vivian_counter == 3:
                $ task_completed(5,"b")
            if v_ep01_task05_help_vivian_counter == 2:
                $ task_completed(5,"c")
            if v_ep01_task05_help_vivian_counter <= 1:
                $ task_completed(5,"d")
            v"Come on. Get in the car before someone from the theatre sees us together..."
            stop ambient fadeout 1.0
            #GO DOWN TO > #scene continues

            #- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

        "Be truthful"(wt="Task Point"):
            #This option will give the player a couple of bonus images of Vivian
            #The MC takes a breath and looks down, trying to compose himself
            show sc vivianac v167
            mc"(No, I'm not letting this snobby bitch make a fool out of me.)"
            mc"(Hmm... Karma.)"
            show sc vivianac v168
            mc"You want some truth?"
            show sc vivianac v169
            mc"All right, well here it is..."
            show sc vivianac v170
            mc"Karma affects people in many ways. Some may call it just plain bad luck."
            show sc vivianac v151
            mc"You know the recent crime spree and the heist last weekend that everybody has been talking about?"
            show sc vivianac v172
            mc"Whose to say that those people didn’t deserve it?"
            show sc vivianac v173
            mc"Maybe it’s karma for them?"
            #Vivian watches from the side of the stage, hiding behind a curtain
            show sc vivianac v138
            v"(He’s talking about us and the job we almost pulled off.)"
            show sc vivianac v188
            mc"Perhaps they did wrong to innocent people and being stolen from is just fair retribution."
            show sc vivianac v176
            mc"And I know what you’re thinking."
            show sc vivianac v177
            mc"What the hell would I know about karma at my age?"
            show sc vivianac v178
            mc"Well, karma has affected me too."
            show sc vivianac v189
            mc"I’m guilty of doing some bad things in the past for what I believe was for the right reasons."
            show sc vivianac v179
            mc"And I’ve done good things for people, too."
            play music "sound effects/01/karma_speech.mp3" loop fadein 1.0
            show sc vivianac v180
            mc"There’s one person in particular who doesn’t always get recognised for how amazing she really is."
            $ rewards_unlock ("vivian",6)
            #Vivian watches from the side of the stage and smiles
            show sc vivianac v181
            mc"But I’ve been the victim of karma more times in the past forty-eight hours than most people are in a year."
            if v_ep01_09_01_Tasha_and_Mikayla_Sex_path == True:
                show sc vivianac v183
                mc"Whether it’s losing important files..."
                mc"Or having my bike stolen or having a one-night stand with two beautiful women..."
                mc"And then waking up to find out that they’ve taken my wallet, phone and also my goddamn clothes!!"
            else:
                show sc vivianac v182
                mc"Whether it’s losing important files..."
                mc"Or having my bike stolen or having a one-night stand with a beautiful woman..."
                mc"And then waking up to find out that she’s taken my wallet, phone and also my goddamn clothes!!"
            #show the small audience of actors laughing, but the teacher keeps a straight face
            play sound "sound effects/01/small_class_laughing_effect.mp3"
            show sc vivianac v184
            if persistent.v_sounds_text_on == True:
                "(Audience laughs)"
            else:
                pause 2.0
            #The MC looks up, angry and upset
            show sc vivianac v185
            mc"Yeah, you all laugh, but where’s the justice?"
            stop sound fadeout 1.0
            show sc vivianac v186
            mc"Did I really deserve to be the victim of karma?"
            #The MC has his head down while he continues to talk
            show sc vivianac v187
            mc"I don’t know, maybe I did deserve it."
            show sc vivianac v138
            mc"And I’m sure that karma will come back for me again and again until I change my ways..."
            #The teacher and a small audience of actors are stunned into silence
            stop music fadeout 3.0
            show sc vivianac v188
            $ renpy.pause(2.0, hard=True)
            #The MC looks down, feeling relieved to get things off of his chest
            #The drama coach stands and thinks, he has a hand upon his chin - https://elements-video-cover-images-0.imgix.net/files/111a2667-2599-4e1a-9976-2316c5c63eef/inline_image_preview.jpg?auto=compress%2Cformat&h=394&w=700&fit=min&s=e510bbc4d7711821c5525e57492857ca
            show sc vivianac v189
            with dissolve
            $ renpy.pause(1.0, hard=True)
            drama_coach"Hmm..."
            show sc vivianac v190
            drama_coach"Interesting piece, young man."
            show sc vivianac v153
            drama_coach"Was that from a TV show?"
            show sc vivianac v194
            mc"Huh?"
            show sc vivianac v191
            drama_coach"That was so much better."
            #She starts clapping
            play sound "sound effects/01/golf_clap_sound_effect.mp3"
            show sc vivianac v192
            pause 1.0
            show sc vivianac v193
            pause 2.0
            #And then everyone else in the theatre stands up and starts clapping
            show sc vivianac v140
            mc"(What the hell just happened?)"
            #Vivian watches from the side of the stage, hiding behind a curtain
            show sc vivianac v195
            v"(He was incredible! Where did that come from?)"
            #The drama coach turns to her class and points at the MC
            show sc vivianac v196
            drama_coach"Now people, {b}THAT{/b} was a monologue!"
            stop sound fadeout 1.0
            #He turns back to face the MC
            show sc vivianac v197
            drama_coach"Mister Galvan... Parts of your story may have been a huge fabrication, but you nailed the topic regardless."
            show sc vivianac v198
            mc"(If only she knew.)"
            show sc vivianac v199
            drama_coach"There might be an actor in you yet."
            #Vivian still watches from a hidden part of the theatre
            #Vivian has a huge smile on her face
            show sc vivianac v200
            v"(I’m so impressed with my [mc_v_rel].)"
            v"(He was superb.)"
            #TWO BONUS RENDERS OF VIVIAN (IN HER CURRENT OUTFIT AT THE THEATRE) ADDED TO THE PHOTO GALLERY FOR HER PROFILE
            show sc vivianac v199
            drama_coach"Take a seat, and we’ll see what you can come up with tomorrow."
            #The MC walks off the stage
            show sc vivianac v201
            mc"(Whatever I said, they all seemed to buy it as an impromptu monologue, even though I was being completely honest.)"
            show sc vivianac v202
            mc"(I sure hope that [mc_v_address] never tried out for this acting class, because this woman is a complete and utter moron!!)"
            show sc vivianac v203
            mc"(However, a career in acting is kind of intriguing.)"
            mc"(With a bit of work, maybe I could be the next \"Barry\"...?)"
            #screen goes blank
            scene black
            with dissolve
            scene black
            with Pause (2)
            #The MC heads outside and meets up with Vivian in the parking lot
            play ambient "sound effects/01/street_sound_day_ambience.ogg" loop fadein 1.0
            show sc vivianac v287
            with dissolve
            v"[y_name]!"
            show sc vivianac v279
            mc"Hey, sorry I didn’t get out of there sooner."
            show sc vivianac v159
            mc"The teacher running it wouldn’t let anyone leave until her class was finished."
            show sc vivianac v281
            mc"She made me do some one-man monologue about a random topic."
            show sc vivianac v272
            v"I know. I saw it."
            show sc vivianac v283
            mc"You did?"
            show sc vivianac v284
            v"Yeah, and you were terrific, [y_name]."
            $ v_ep01_task05_help_vivian_counter += 1
            show sc vivianac v281
            mc"So that was you watching from the side of the stage."
            show sc vivianac v285
            v"Yeah, it was."
            v"I loved how you completely stuck it to the teacher and everyone else in there."
            v"And you gave me enought time to get the things we need for the next job!"
            show sc vivianac v286
            mc"So... You’re not mad?"
            show sc vivianac v287
            v"Of course not!"
            show sc vivianac v285
            v"I couldn’t be any more proud of you right now."
            if v_ep01_task05_help_vivian_counter == 5:
                $ task_completed(5,"aa")
                $ v_ep01_vivian_aa_tasks_counter += 1
            if v_ep01_task05_help_vivian_counter == 4:
                $ task_completed(5,"a")
            if v_ep01_task05_help_vivian_counter == 3:
                $ task_completed(5,"b")
            if v_ep01_task05_help_vivian_counter == 2:
                $ task_completed(5,"c")
            if v_ep01_task05_help_vivian_counter <= 1:
                $ task_completed(5,"d")
            show sc vivianac v289
            v"Come on. Get in the car before someone from the theatre sees us together..."
            $ v_ep01_12_02_truthful_vivian = True
            stop ambient fadeout 1.0

    #scene continues
    scene black
    with dissolve
    scene black
    with Pause (2)
    #cross-fade screen

    #show Vivian driving while the MC looks out the window from the passenger seat
    play music "sound effects/01/On the Way Home1.mp3" loop fadein 1.0
    play ambient "sound effects/01/car_interior_ambience.ogg" loop fadein 1.0
    if persistent.v_anim_enabled:
        scene anim_ep01_road_right105_slow:
            size (config.screen_width, config.screen_height)
    else:
        scene bg driving right105
    show sc vivianac v205b
    with dissolve
    pause 2.0
    if persistent.v_anim_enabled:
        scene anim_ep01_road_left_slow:
            size (config.screen_width, config.screen_height)
    else:
        scene bg driving left
    show sc vivianac v232b
    v"So overall, a job well done, right?"
    #The MC is deep in thought
    if persistent.v_anim_enabled:
        scene anim_ep01_road_right105_slow:
            size (config.screen_width, config.screen_height)
    else:
        scene bg driving right105
    show sc vivianac v208b
    mc"Yeah..."
    if persistent.v_anim_enabled:
        scene anim_ep01_road_left_slow:
            size (config.screen_width, config.screen_height)
    else:
        scene bg driving left
    show sc vivianac v206b
    v"What’s wrong, sweetheart?"
    show sc vivianac v207b
    v"You know you can tell me anything, right?"
    if persistent.v_anim_enabled:
        scene anim_ep01_road_right105_slow:
            size (config.screen_width, config.screen_height)
    else:
        scene bg driving right105
    show sc vivianac v209b
    mc"Okay..."
    show sc vivianac v210b
    mc"There’s something bothering me about all of this."
    show sc vivianac v209b
    mc"You seemed to know a lot about that theatre"
    if persistent.v_anim_enabled:
        scene anim_ep01_road_left_slow:
            size (config.screen_width, config.screen_height)
    else:
        scene bg driving left
    show sc vivianac v211b
    v"What are you implying?"
    if persistent.v_anim_enabled:
        scene anim_ep01_road_right105_slow:
            size (config.screen_width, config.screen_height)
    else:
        scene bg driving right105
    show sc vivianac v212b
    mc"I can’t shake this feeling that you had been there before."
    mc"Maybe even more than a few times. Or you know people that work there."
    show sc vivianac v213b
    mc"Do you?"
    #Vivian looks away
    if persistent.v_anim_enabled:
        scene anim_ep01_road_left_slow:
            size (config.screen_width, config.screen_height)
    else:
        scene bg driving left
    show sc vivianac v214b
    v"I’m sorry, [y_name]. I should’ve told you sooner."
    if persistent.v_anim_enabled:
        scene anim_ep01_road_right105_slow:
            size (config.screen_width, config.screen_height)
    else:
        scene bg driving right105
    show sc vivianac v215b
    mc"Told me what?"
    if persistent.v_anim_enabled:
        scene anim_ep01_road_left_slow:
            size (config.screen_width, config.screen_height)
    else:
        scene bg driving left
    show sc vivianac v216b
    v"You know the acting teacher?"
    if persistent.v_anim_enabled:
        scene anim_ep01_road_right105_slow:
            size (config.screen_width, config.screen_height)
    else:
        scene bg driving right105
    show sc vivianac v212b
    mc"Who? Miss Fonzarelli?"
    if persistent.v_anim_enabled:
        scene anim_ep01_road_left_slow:
            size (config.screen_width, config.screen_height)
    else:
        scene bg driving left
    show sc vivianac v211b
    v"Yeah..."
    show sc vivianac v214b
    v"She was my acting teacher when I was a little younger than you are now..."
    stop music fadeout 0.5
    play music "sound effects/01/Stronger Than Steel.mp3" loop fadein 0.5
    stop ambient fadeout 1.0
    with dissolve
    #cross-screen fade
    #flashback scene while Vivian narrates
    #show a young Vivian auditioning - performing a monologue on the stage in front of a younger Mr. Fonzarelli
    show sc vivianac v218
    with flash(0.25, 0, 0.75, "#fff")
    v"{i}Many years ago, I auditioned to be in one of Miss Fonzarelli’s theatre plays.{/i}"
    show sc vivianac v219
    with dissolve
    v"{i}It was a pretty big deal and all the actors who auditioned saw it as a chance to go on to bigger and better things.{/i}"
    #show a young Vivian smiling after her audition
    show sc vivianac v220
    with dissolve
    v"{i}It looked like I was a shoo-in for the role.{/i}"
    v"{i}But when it came to deciding who would get it, she crushed my dreams.{/i}"
    #show a young Vivian upset and trying to hold back tears while Fonzarelli is criticising her
    show sc vivianac v221
    with dissolve
    v"{i}Not only did she give the role to someone else, but she called me to her office and told me that I didn’t have what it takes to be an actress.{/i}"
    #show a young Vivian running off in tears
    show sc vivianac v222
    with dissolve
    v"{i}And so I never went back there again. Or to any acting theatre.{/i}"
    scene black
    with Dissolve(1.0)
    #the flashback ends and we see them talking in the car again
    play music "sound effects/01/On the Way Home2.mp3" loop fadein 1.0
    play ambient "sound effects/01/car_interior_ambience.ogg" loop fadein 1.0
    if persistent.v_anim_enabled:
        scene anim_ep01_road_right105_slow:
            size (config.screen_width, config.screen_height)
    else:
        scene bg driving right105
    show sc vivianac v223b
    with flash(0.25, 0, 0.75, "#fff")
    mc"But you’re a wonderful actor."
    show sc vivianac v224b
    mc"I’ve seen you first-hand, watching from inside the van whenever you’ve had to perform as different characters."
    show sc vivianac v225b
    mc"You’re arguably the biggest reason why so many jobs that you and [mc_vic_address] have succeeded with have been a success."
    show sc vivianac v226b
    mc"It just doesn’t make sense. There has to be another reason."
    if persistent.v_anim_enabled:
        scene anim_ep01_road_left_slow:
            size (config.screen_width, config.screen_height)
    else:
        scene bg driving left
    show sc vivianac v227b
    v"You know, I’ve always felt that I didn’t get that role because of who I am, and where we’re from."
    show sc vivianac v228b
    mc"Do you mean because we’re considered to be lower-class?"
    if persistent.v_anim_enabled:
        scene anim_ep01_road_left_slow:
            size (config.screen_width, config.screen_height)
    else:
        scene bg driving left
    show sc vivianac v229b
    v"I’ve never wanted to believe it, but yeah."
    show sc vivianac v230b
    v"I was always late with my monthly payments for classes and I think that ultimately cost me in the end."
    show sc vivianac v231b
    v"It felt like a case of not what you know, but who you know."
    show sc vivianac v216b
    v"And who has the most money."
    if persistent.v_anim_enabled:
        scene anim_ep01_road_right105_slow:
            size (config.screen_width, config.screen_height)
    else:
        scene bg driving right105
    show sc vivianac v233b
    mc"So that’s why you were hesitant to go in there."
    if persistent.v_anim_enabled:
        scene anim_ep01_road_left_slow:
            size (config.screen_width, config.screen_height)
    else:
        scene bg driving left
    show sc vivianac v227b
    v"Yeah... I didn’t want to give her the chance to humiliate me again."
    show sc vivianac v229b
    v"But I also didn’t want [vic_name] to be angry for not getting the job done."
    if persistent.v_anim_enabled:
        scene anim_ep01_road_left_slow:
            size (config.screen_width, config.screen_height)
    else:
        scene bg driving left
    show sc vivianac v230b
    v"Which was the most important thing."
    if persistent.v_anim_enabled:
        scene anim_ep01_road_right105_slow:
            size (config.screen_width, config.screen_height)
    else:
        scene bg driving right105
    show sc vivianac v234b
    mc"I’m so sorry to hear that."
    show sc vivianac v235b
    mc"I had no idea."
    if persistent.v_anim_enabled:
        scene anim_ep01_road_left_slow:
            size (config.screen_width, config.screen_height)
    else:
        scene bg driving left
    show sc vivianac v236b
    mc"Why didn’t you tell me about any of this before?"
    show sc vivianac v237b
    v"I was embarrassed."
    show sc vivianac v238b
    v"I didn’t want you to know that I made a fool out of myself in front of everyone in that same theatre."
    show sc vivianac v229b
    v"It still brings up some bad memories."
    if persistent.v_anim_enabled:
        scene anim_ep01_road_right105_slow:
            size (config.screen_width, config.screen_height)
    else:
        scene bg driving right105
    show sc vivianac v239b
    mc"Trust me, it’s not as bad as it seems. I know from recent experience."
    #Vivian laughs
    if persistent.v_anim_enabled:
        scene anim_ep01_road_left_slow:
            size (config.screen_width, config.screen_height)
    else:
        scene bg driving left
    show sc vivianac v240b
    v"Haha, touche."
    show sc vivianac v232b
    v"But you don’t have any expectations on you, [y_name]."
    v"I’m proud of you for going up there though."
    if persistent.v_anim_enabled:
        scene anim_ep01_road_right105_slow:
            size (config.screen_width, config.screen_height)
    else:
        scene bg driving right105
    show sc vivianac v225b
    mc"Sure, but we both know that you’ll always be the true actor in our [private_group]."
    if persistent.v_anim_enabled:
        scene anim_ep01_road_left_slow:
            size (config.screen_width, config.screen_height)
    else:
        scene bg driving left
    show sc vivianac v241b
    v"Thanks for coming with me today, [y_name]."
    show sc vivianac v242b
    v"I couldn’t have done it without you."
    #Vivian places her hand on top of his
    if persistent.v_anim_enabled:
        scene anim_ep01_road_right105_slow:
            size (config.screen_width, config.screen_height)
    else:
        scene bg driving right105
    show sc vivianac v243b
    mc"You’re welcome."
    show sc vivianac v246b
    mc"You know that I’m always here for you."
    #Vivian smiles and looks into his eyes


    #"Add this scene and lines if the player selected BE TRUTHFUL earlier in this scene"
    if v_ep01_12_02_truthful_vivian == True:
        if persistent.v_anim_enabled:
            scene anim_ep01_road_left_slow:
                size (config.screen_width, config.screen_height)
        else:
            scene bg driving left
        show sc vivianac v231b
        v"(Darnit, a red light...)"
        stop ambient fadeout 4.0
        pause 2.0
        play ambient2 "sound effects/01/Car_Motor_Running_Sound_FX.mp3"
        show sc vivianac v246
        with dissolve
        v"I know you are, sweetheart..."
        #Without thinking, Vivian kisses the MC on the lips
        show sc vivianac v248
        pause 1.0
        play sound "sound effects/01/kissed_by_Vivian_short.mp3" loop fadein 1.0
        show sc vivianac v249
        v"Mmm..."
        show sc vivianac v249
        pause 0.5
        stop music fadeout 1.0
        play sound2 "sound effects/01/record_scratch.ogg"
        show sc vivianac v250
        with vpunch
        mc"(Oh!)"
        stop sound fadeout 1.0
        stop sound2 fadeout 1.0
        #Vivian’s eyes shoot open when she realises she’s kissing the MC.
        #She retracts her lips
        play music "sound effects/01/On the Way Home2.mp3" loop fadein 1.0
        show sc vivianac v251
        pause 1.5
        show sc vivianac v252
        v"Oh, I’m so sorry, [y_name]!"
        show sc vivianac v253
        v"I meant to kiss you on the cheek."
        show sc vivianac v254
        v"(I think...)"
        #The MC and Vivian look away from each other
        show sc vivianac v255
        mc"It’s fine, [mc_v_address]."
        show sc vivianac v256
        mc"It’s no big deal."
        stop ambient2 fadeout 1.0
        play ambient "sound effects/01/car_interior_ambience.ogg" loop fadein 1.0
        show sc vivianac v291
        with dissolve
        pause 1.0
        if persistent.v_anim_enabled:
            scene anim_ep01_road_rear_slow:
                size (config.screen_width, config.screen_height)
        else:
            scene bg driving rear
        show sc vivianac v257b
        with dissolve
        mc"(Was it really a mistake or did she genuinely mean to do that?)"

    #scene continues
    if v_ep01_mc_task_visit_options_3 == "":
        show sc vivianac v258b
        mc"Um... Do you think you could drop me off up here?"
        show sc vivianac v259b
        mc"I just need to use the library so I can do some more research that might help me locate the flash drive."
        if persistent.v_anim_enabled:
            scene anim_ep01_road_right105_slow:
                size (config.screen_width, config.screen_height)
        else:
            scene bg driving right105
        show sc vivianac v260b
        mc"You don’t mind, do you?"
        if persistent.v_anim_enabled:
            scene anim_ep01_road_left_slow:
                size (config.screen_width, config.screen_height)
        else:
            scene bg driving left
        show sc vivianac v261b
        v"Uh, no, Not at all."
        if persistent.v_anim_enabled:
            scene anim_ep01_road_right105_slow:
                size (config.screen_width, config.screen_height)
        else:
            scene bg driving right105
        show sc vivianac v263b
        mc"Thanks, [mc_v_address]."
        if persistent.v_anim_enabled:
            scene anim_ep01_road_left_slow:
                size (config.screen_width, config.screen_height)
        else:
            scene bg driving left
        show sc vivianac v262b
        v"I can drop you off at the front entrance."
        if persistent.v_anim_enabled:
            scene anim_ep01_road_right105_slow:
                size (config.screen_width, config.screen_height)
        else:
            scene bg driving right105
        show sc vivianac v264b
        mc"No, no... it’s cool."
        show sc vivianac v269b
        mc"It’s kind of out of your way and I know of a shortcut to get there pretty quickly."
        if persistent.v_anim_enabled:
            scene anim_ep01_road_left_slow:
                size (config.screen_width, config.screen_height)
        else:
            scene bg driving left
        show sc vivianac v265b
        v"Sure, I’ll pull the car up just after the next set of lights..."
        #Vivian looks concerned
        if v_ep01_12_02_truthful_vivian == True:
            if persistent.v_anim_enabled:
                scene anim_ep01_road_rear_slow:
                    size (config.screen_width, config.screen_height)
            show sc vivianac v266b
            v"(I really hope I didn’t weird him out because of that kiss...)"
        stop ambient fadeout 1.0
        stop music fadeout 1.0
        #screen goes blank
        scene black
        with dissolve
        scene black
        with Pause (2)
        if v_ep01_mc_task_visit_options_2 == "":
            jump lb_ep01_The_MC_meets_Zora
        else:
            jump lb_ep01_MC_gets_a_call_from_Megan1
    else:
        #Add these lines if the player has already helped Ariel and/or Bella do their tasks"
        if persistent.v_anim_enabled:
            scene anim_ep01_road_left_slow:
                size (config.screen_width, config.screen_height)
        else:
            scene bg driving left
        show sc vivianac v267b
        v"We’re almost home."
        show sc vivianac v268b
        v"Do you have any plans tonight?"
        if persistent.v_anim_enabled:
            scene anim_ep01_road_right105_slow:
                size (config.screen_width, config.screen_height)
        else:
            scene bg driving right105
        show sc vivianac v269b
        mc"Uh, no. I think I’ve done as much as I can today."
        show sc vivianac v263b
        mc"I’ll ask [a_name] if she has any more info on the flash drive but other than that, it should be a quiet night in."
        show sc vivianac v255b
        mc"(I haven’t decided if I’ll tell [mc_v_address] about Megan yet.)"
        #Vivian looks concerned
        if v_ep01_12_02_truthful_vivian == True:
            if persistent.v_anim_enabled:
                scene anim_ep01_road_rear_slow:
                    size (config.screen_width, config.screen_height)
            show sc vivianac v271b
            v"(I really hope I didn’t weird him out because of that kiss...)"
        stop ambient fadeout 1.0
        stop music fadeout 1.0
        #Vivian continues to drive as the screen fades out
        #screen goes blank
        scene black
        with dissolve
        scene black
        with Pause (2)
        jump lb_ep01_The_MC_sees_Vivian_in_the_bathroom
    stop ambient fadeout 1.0
    stop music fadeout 1.0
    #Vivian continues to drive as the screen fades out
    #screen goes blank
    scene black
    with dissolve
    scene black
    with Pause (2)
