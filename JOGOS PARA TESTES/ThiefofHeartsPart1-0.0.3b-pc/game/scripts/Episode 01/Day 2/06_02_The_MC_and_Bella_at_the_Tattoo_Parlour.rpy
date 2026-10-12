init:
    $ v_ep01_06_02_Tattoo_Parlour_Secret = False
    $ v_ep01_06_02_Tattoo_Parlour_Date = False
    $ v_ep01_06_02_Tattoo_Parlour_Tattoo_Response = ""
    $ v_ep01_06_02_Tattoo_Parlour_Tattoo_Choice = ""
    $ v_ep01_06_02_Tattoo_Parlour_Tip = False
    $ v_ep01_06_02_Tattoo_Relationship_Choice = ""
    $ v_ep01_task04_help_bella_tattoo_parlour_counter = 0

    image sc tattoo parlour tatto girl blowing kiss:
        "sc tattoo parlour b032" with Dissolve(0.2, alpha=True)
        pause 0.5
        "sc tattoo parlour b032a" with Dissolve(0.2, alpha=True)
        pause 0.8
        "sc tattoo parlour b032" with Dissolve(0.2, alpha=True)

    layeredimage sc tattoo parlour tatto girl teasing:
        always:
            "sc tattoo parlour b033 base"

        always:
            "sc tattoo parlour tatto girl teasing head"

        always:
            "sc tattoo parlour tatto girl teasing body"

    image sc tattoo parlour tatto girl teasing head:
        "sc tattoo parlour b033 head 1" with Dissolve(0.2, alpha=True)
        pause 1.0
        "sc tattoo parlour b033 head 2" with Dissolve(0.2, alpha=True)
        pause 0.8
        "sc tattoo parlour b033 head 3" with Dissolve(0.2, alpha=True)
        pause 0.8
        "sc tattoo parlour b033 head 1" with Dissolve(0.2, alpha=True)

    image sc tattoo parlour tatto girl teasing body:
        "sc tattoo parlour b033 body 1" with Dissolve(0.2, alpha=True)
        pause 0.4
        "sc tattoo parlour b033 body 2" with Dissolve(0.2, alpha=True)
        pause 0.4
        "sc tattoo parlour b033 body 3" with Dissolve(0.2, alpha=True)
        pause 0.4
        "sc tattoo parlour b033 body 2" with Dissolve(0.2, alpha=True)
        pause 0.4
        repeat

    image sc tattoo parlour tattoist sit1:
        "sc tattoo parlour b086a" with Dissolve(0.2, alpha=True)
        pause 1.0
        "sc tattoo parlour b086" with Dissolve(0.2, alpha=True)

    image sc tattoo parlour tattoist sit2:
        "sc tattoo parlour b094" with Dissolve(0.2, alpha=True)
        pause 1.0
        "sc tattoo parlour b095" with Dissolve(0.2, alpha=True)

    image sc tattoo parlour bella walk:
        "sc tattoo parlour b116" with Dissolve(0.2, alpha=True)
        pause 0.6
        "sc tattoo parlour b116a" with Dissolve(0.2, alpha=True)
        pause 0.6
        "sc tattoo parlour b116b" with Dissolve(0.2, alpha=True)
        pause 0.6
        "sc tattoo parlour b116c" with Dissolve(0.2, alpha=True)
        pause 0.6
        "sc tattoo parlour b116d" with Dissolve(0.2, alpha=True)


    image sc tattoo parlour tatto girl teasing breast:
        "sc tattoo parlour b132" with Dissolve(0.2, alpha=True)
        pause 0.6
        "sc tattoo parlour b132a" with Dissolve(0.2, alpha=True)
        pause 0.6
        "sc tattoo parlour b132b" with Dissolve(0.2, alpha=True)
        pause 0.6
        repeat

    image sc tattoo parlour tatto girl teasing pussy1:
        "sc tattoo parlour b134" with Dissolve(0.2, alpha=True)
        pause 1.0
        "sc tattoo parlour b134a" with Dissolve(0.2, alpha=True)
        pause 1.0
        "sc tattoo parlour tatto girl teasing pussy2" with Dissolve(0.2, alpha=True)

    image sc tattoo parlour tatto girl teasing pussy2:
        "sc tattoo parlour b134b" with Dissolve(0.2, alpha=True)
        pause 1.0
        "sc tattoo parlour b134c" with Dissolve(0.2, alpha=True)
        pause 1.0
        repeat

    image sc tattoo parlour tatto girl fingering pussy1:
        "sc tattoo parlour b137" with Dissolve(0.2, alpha=True)
        pause 1.0
        "sc tattoo parlour b137a" with Dissolve(0.2, alpha=True)
        pause 1.0
        repeat

    image sc tattoo parlour tatto girl fingering pussy2:
        "sc tattoo parlour b138" with Dissolve(0.2, alpha=True)
        pause 0.6
        "sc tattoo parlour b138a" with Dissolve(0.2, alpha=True)
        pause 0.6
        repeat

    image sc tattoo parlour tatto girl fingering pussy3:
        "sc tattoo parlour b137" with Dissolve(0.2, alpha=True)
        pause 0.3
        "sc tattoo parlour b137a" with Dissolve(0.2, alpha=True)
        pause 0.3
        repeat

    image sc tattoo parlour tatto girl fingering pussy4:
        "sc tattoo parlour b139" with Dissolve(0.2, alpha=True)
        pause 0.3
        "sc tattoo parlour b139a" with Dissolve(0.2, alpha=True)
        pause 0.3
        repeat

    image sc tattoo parlour tatto girl going down tease1:
        "sc tattoo parlour b145" with Dissolve(0.2, alpha=True)
        pause 0.3
        "sc tattoo parlour b145a" with Dissolve(0.2, alpha=True)
        pause 0.3
        repeat

    image sc tattoo parlour tatto girl eating out:
        "sc tattoo parlour b163" with Dissolve(0.2, alpha=True)
        pause 0.6
        "sc tattoo parlour b163a" with Dissolve(0.2, alpha=True)
        pause 0.6
        repeat

init -1:
    transform tt_02_06_02_Tattoo_top_down_1:
        xpos 0    ## or anything else slightly outside your screen
        ypos 0
        easein 6 xpos 0 ypos -2541  ## or wherever you want it to end up

    transform tt_02_06_02_Tattoo_top_down_2:
        xpos 0    ## or anything else slightly outside your screen
        ypos 0
        easein 1 xpos 0 ypos -752  ## or wherever you want it to end up

label lb_ep01_06_02_Tattoo_Parlour_1:
    #Thief Of Hearts - Ep 1 Scene 06-02 - Tattoo Parlour
    #The MC and Bella check out the local tattoo parlour
    #SCENE BEGINS
    #scene starts with the MC waiting in the carpark behind the clothing store
    play ambient "sound effects/01/suburb_neighborhood_ambience.ogg" loop fadein 1.0
    scene sc tattoo parlour b001
    with dissolve
    mc"(Where the hell is she?)"
    mc"(I thought she said to meet her at three.)"
    #Bella arrives
    show sc tattoo parlour b002
    mc"(Finally...)"
    #[Be a dick / Hear her out]x
    menu:
        "Be a dick":
            show sc tattoo parlour b006
            mc"What time do you call this?"
            show sc tattoo parlour b005
            b"What do you mean?"
            show sc tattoo parlour b006
            mc"You’re twenty minutes late! And for a normal person, that would be the same as stealing!"
            show sc tattoo parlour b007
            b"Oh shut up. I had shit to deal with."
            b"Besides, if it were up to me then I’d prefer not to be here."
            show sc tattoo parlour b008
            mc"Yeah, well, that’s not the case."
            show sc tattoo parlour b009
            b"Let’s get this over with."
            show sc tattoo parlour b010
            mc"Fine."
        "Hear her out"(wt="Task Point"):
            show sc tattoo parlour b003
            b"Sorry I’m late. I had a lot of shit to deal after my shift ended."
            show sc tattoo parlour b004
            mc"It’s fine. I was wondering if you were going to back out."
            $ rewards_unlock ("bella",2)
            show sc tattoo parlour b005
            b"Never... I have a job to do, even if I’d rather be somewhere else."
            $ v_ep01_task04_help_bella_tattoo_parlour_counter += 1
    #(scene continues)
    show sc tattoo parlour b011
    mc"So where is this tattoo parlour?"
    show sc tattoo parlour b012
    b"It’s only a few blocks from here. Leave your bike where it is and we can walk."
    b"I’ll tell you all about it on the way..."
    #Player has to click on the MAP icon at the top of the screen and then choose the TATTOO PARLOUR which will highlight when the cursor hovers over it
    #when they click on it, the screen will go blank and they will be taken to the PARLOUR
    #screen goes blank
    stop ambient fadeout 1.0
    scene black
    with dissolve
    scene black
    with Pause (2)
    #the MC and Bella stand outside the tattoo parlour named "Artistic Prick"
    play ambient "sound effects/01/street_sound_day_ambience.ogg" loop fadein 1.0
    scene sc tattoo parlour b013
    with dissolve
    mc"Is this the place?"
    #show the outside of the store - https://c8.alamy.com/comp/T2EJH4/green-and-white-vespa-scooter-with-red-leather-seat-parked-outside-tattoo-studio-front-door-T2EJH4.jpg
    b"Yeah, it is."
    mc"Artistic Prick?"
    show sc tattoo parlour b014
    mc"Is that the name of the store or the guy running it?"
    show sc tattoo parlour b015
    b"Haha! I’m not sure but it’s a clever name."
    show sc tattoo parlour b013
    mc"Hopefully his sense of humour matches it."
    show sc tattoo parlour b016
    b"Come on, let’s go and check it out."
    #screen crossfade so the MC and Bella are inside the store in the next render
    #inside of the store looks like this and he’s working on - https://www.daz3d.com/trendy-tattoo-shop or https://www.daz3d.com/the-tattoo-studio-with-poses-for-genesis-8-female-and-male
    #Have them look around the room, seeing a few different people in various places.
    stop ambient fadeout 2.0
    $ renpy.music.set_volume(0.3, 2.0, channel="sound")
    $ renpy.music.set_volume(0.6, 1.0, channel="music")
    play sound "sound effects/01/tattoo_machine_close.ogg" loop
    play music "sound effects/01/Inked_Souls.ogg" loop fadein 1.0
    show sc tattoo parlour b017
    with dissolve
    b"Hmm, I wonder who the owner is."
    #From the camera angle, they won't be able to see too much yet of the person getting the tattoo
    show sc tattoo parlour b018
    mc"That guy's working on someone right now, so it could be him."
    $ renpy.music.set_volume(0.8, 0.5, channel="sound")
    show sc tattoo parlour b019
    b"Excuse me, we..."
    show sc tattoo parlour b020
    b"OH!"
    if not persistent.v_sex_anim_enabled_locked and persistent.v_sex_anim_enabled:
        scene sc tattoo parlour b021_wip at tt_02_06_02_Tattoo_top_down_1
        pause
    elif True:
        show sc tattoo parlour b021
    mc"(Woah! I never expected to see this in here.)"
    scene sc tattoo parlour b022
    b"Oh my, I'm sorry if we are intruding. Maybe we should come back later."
    show sc tattoo parlour b023
    tattooist"Haha! You're not intruding."
    tattooist"And there's a sign out front to warn customers what can happen in here."
    show sc tattoo parlour b024
    tattooist"But don't worry about her. She assures me that she doesn't mind if other people see her like this."
    #tattooist leans over
    stop sound fadeout 1.0
    show sc tattoo parlour b025
    tattooist"{i}(*Whispering*){/i}\nIn fact, she's sort of into other people watching her, if you know what I mean."
    show sc tattoo parlour b026
    b"Oh...!"
    #Bella Glances at the MC thinking this:
    show sc tattoo parlour b027
    b"(It feels weird to be in the same room as [y_name] and near this naked young woman.)"
    show sc tattoo parlour b028
    b"Well as long as she's okay with it, then I guess I'm okay with it too. How about you, [y_name]?"
    show sc tattoo parlour b027
    menu:
        "Be charming":
            show sc tattoo parlour b029
            mc"How can I object to staring at this near-naked beauty before me?"
            #Naked Girl in chair winks and blows a kiss at the MC
            play sound "sound effects/01/sex/blow_kiss.ogg" loop
            if not persistent.v_sex_anim_enabled_locked and persistent.v_sex_anim_enabled:
                show sc tattoo parlour tatto girl blowing kiss
                $ renpy.pause(0.5, hard=True)
                woman"Mwah!{w=0.8}{nw}"
                pause
            else:
                show sc tattoo parlour b032a
                woman"Mwah!{w=0.8}{nw}"
            #Bella gets a little jealous from his response
            stop sound fadeout 1.0
            scene sc tattoo parlour b034
            b"(Hmm, I knew it wouldn't bother him, but why is his response bothering me so much.)"
            $ v_ep01_06_02_Tattoo_Parlour_Tattoo_Response = "charming"
        "Be composed"(wt="Task Point + Extra scene with tattoo girl in Episode 2 if you get the Bella Heart"):
            show sc tattoo parlour b030
            mc"If you're okay with it, then I don't see any problem."
            $ rewards_unlock ("bella",3)
            #Bella gives him a soft, almost loving look.
            show sc tattoo parlour b035
            b"(Hmm, I didn't expect that from [y_name]. Interesting...)"
            $ v_ep01_task04_help_bella_tattoo_parlour_counter += 1
            $ v_ep01_06_02_Tattoo_Parlour_Tattoo_Response = "composed"
        "Be crude"(wt="Choose this option for an Extra Scene with tattoo girl in Episode 2"):
            show sc tattoo parlour b031
            mc"Are you kidding! I think it's downright sexy to watch this hottie's crotch getting tattooed!"
            #Naked Girl in chair licks her lips at the MC while also pinching her nipples and lightly spreading and rubbing her clit. We here a slight moan from her
            show sc tattoo parlour b033
            pause 0.5
            if not persistent.v_sex_anim_enabled_locked and persistent.v_sex_anim_enabled:
                show sc tattoo parlour tatto girl teasing
                with faster_dissolve
            else:
                show sc tattoo parlour b033 base
                with faster_dissolve
            woman"Mmm..."
            mc"HOT DAMN!"
            #Bella shoots the MC a dirty look
            show sc tattoo parlour b036
            b"(Yep, it's no surprise that he's acting like a gross pig.)"
            $ v_ep01_06_02_Tattoo_Parlour_Tattoo_Response = "crude"
    play sound "sound effects/01/tattoo_machine_close.ogg" loop
    show sc tattoo parlour b038
    b"Anyway, we’re looking for the owner. Are you him?"
    show sc tattoo parlour b019
    #he doesn’t look at the MC as he is working on a girl tattoo and is nearly finished
    show sc tattoo parlour b037
    tattooist"No, I would be his assistant. The boss is off today."
    tattooist"You’ll have to come back tomorrow."
    show sc tattoo parlour b038
    b"Well maybe you can help us?"
    show sc tattoo parlour b039
    tattooist"Looking for a tattoo? Then please, take a seat as I’m almost done here."
    b"Actually, no, I’m not-"
    show sc tattoo parlour b040
    mc"{i}(*Whispering*){/i}\nShh... Just go with it, [b_name]."
    show sc tattoo parlour b041
    b"{i}(*Whispering*){/i}\nBut I don’t want a tattoo, if {i}this{/i} is anything to go by."
    show sc tattoo parlour b042
    mc"{i}(*Whispering*){/i}\nYeah, but he doesn't know that."
    if v_ep01_06_02_Tattoo_Parlour_Tattoo_Response == "charming":
        mc"{i}(*Whispering*){/i}\nAnd I think you'd look great with a tattoo."
        show sc tattoo parlour b043
        b"{i}(*Whispering*){/i}\nYeah, well it's not happening. And there's no way I'm getting naked."
        show sc tattoo parlour b044
        mc"{i}(*Whispering*){/i}\nWe at least need him to {b}think{/b} that you want one."
        show sc tattoo parlour b045
        mc"Sir, she’d be happy to get inked."
        mc"Preferably something from your catalogue."
        show sc tattoo parlour b046
        b"{i}(*Whispering*){/i}\nDamnit [y_name]..."
    elif v_ep01_06_02_Tattoo_Parlour_Tattoo_Response == "composed":
        mc"{i}(*Whispering*){/i}\nAnd I think you'd look good with a tattoo."
        show sc tattoo parlour b051
        b"{i}(*Whispering*){/i}\nReally? Well it's not happening, and even if I did get one, I couldn't be naked like that around you."
        show sc tattoo parlour b052
        mc"{i}(*Whispering*){/i}\nOf course not, but we need him to {b}think{/b} you want to."
        show sc tattoo parlour b053
        mc"Sure, she’ll be happy to get inked."
        mc"Preferably something from your catalogue."
    elif v_ep01_06_02_Tattoo_Parlour_Tattoo_Response == "crude":
        mc"{i}(*Whispering*){/i}\nAnd I think you'd look hot with a tattoo."
        show sc tattoo parlour b047
        b"{i}(*Whispering*){/i}\nWell it's not happening, and I'm not getting naked so you can ogle me. So forget it."
        show sc tattoo parlour b048
        mc"{i}(*Whispering*){/i}\nAwe, you're no fun...."
        #the MC addresses the tattooist"
        show sc tattoo parlour b049
        mc"Ahem, she’d be happy to get inked."
        mc"Preferably something from your catalogue."
        show sc tattoo parlour b050
        b"{i}(*Whispering*){/i}\nYou jackass."
    show sc tattoo parlour b054
    tattooist"We can go through those before we begin, but for now, take a look around."
    tattooist"Maybe one of our personal designs on the wall will be something you’d be interested in."
    #The MC and Bella look at designs on the wall and examples of other tattoos that people have done
    #the tattoo artist continues to work in the background
    show sc tattoo parlour b055
    mc"Can you see that design anywhere in here?"
    b"No, it’s a pretty specific tattoo. So it should stick out like a sore thumb."
    show sc tattoo parlour b056
    mc"Do you have that image with you?"
    show sc tattoo parlour b057
    b"Of course."
    #Bella hands the MC a sheet with the image she drew herself"
    show sc tattoo parlour b058
    b"Here."
    #we see the image for the first time"
    show sc tattoo parlour b059
    mc"Hmm..."
    #the MC looks back up at the wall
    show sc tattoo parlour b060
    mc"Yeah, I’m not seeing it here."
    show sc tattoo parlour b061
    mc"I guess we’ll have to wait until he’s finished so we can grill him with our questions..."
    #screen goes blank
    stop sound fadeout 1.0
    stop music fadeout 1.0
    $ renpy.music.set_volume(1.0, 1.0, channel="sound")
    $ renpy.music.set_volume(1.0, 1.0, channel="music")
    scene black
    with dissolve
    pause 1.0
    centered "20 minutes later...{w=2.0}{nw}" with dissolve
    show text "20 minutes later..." #THESE LINES ARE NOT DUPLICATES. Needed to fade the text in and out!
    scene bg black with Dissolve(1)
    pause 1.0
    $ renpy.music.set_volume(0.6, 0.0, channel="music")
    play music "sound effects/01/Ink and Iron.mp3" loop fadein 1.0
    #We see the women who was getting the tattoo getting ready to leave
    if v_ep01_06_02_Tattoo_Parlour_Tattoo_Response == "crude":
        # if the player chose crude earlier
        scene sc tattoo parlour b062
        with dissolve
        tattooist"All right, looks like you’re up. Just give me a minute to go drain the lizard."
        show sc tattoo parlour b130
        mc"Sure, no problems."
        #The woman will come up to him, whisper in his ear as she puts his hand on her breast and says
        show sc tattoo parlour b131a
        woman"Hey stud..."
        show sc tattoo parlour b131
        with dissolve
        woman"So you liked looking at my new tattoo huh?"
        mc"Uh huh..."
        if not persistent.v_sex_anim_enabled_locked and persistent.v_sex_anim_enabled:
            show sc tattoo parlour tatto girl teasing breast
        else:
            show sc tattoo parlour b132
        woman"Well if we meet again, I'll let you get a {b}really{/b} close look at it."
        show sc tattoo parlour b133
        mc"Oh, really now?"
        b"(Seriously [y_name]!)"
        # She moves his hand down to her crotch and rubs his finer on her clit
        if not persistent.v_sex_anim_enabled_locked and persistent.v_sex_anim_enabled:
            show sc tattoo parlour tatto girl teasing pussy1
        else:
            show sc tattoo parlour b137
        woman"In the meantime, I want to be sure I remember you..."
        mc"(Oh shit!)"
        woman"And so you don't forget about me, mmm..."
        show sc tattoo parlour b135
        woman"I want those big fingers of yours to get really familiar with the area."
        show sc tattoo parlour b136
        pause 1.0
        show sc tattoo parlour b137
        with hpunch
        mc"(Oh my god!)"
        mc"(She's got an iron-like grip on my hand!)"
        #She pushes his fingers into her pussy as she continues to rub his hand up and down her clit.
        if not persistent.v_sex_anim_enabled_locked and persistent.v_sex_anim_enabled:
            show sc tattoo parlour tatto girl fingering pussy1
        else:
            show sc tattoo parlour b137
        woman"Feel how warm and wet my pussy is..."
        woman"Let your fingers remember just how badly it's begging for your big hard cock."
        woman"Mmm, fuck..."
        if not persistent.v_sex_anim_enabled_locked and persistent.v_sex_anim_enabled:
            show sc tattoo parlour tatto girl fingering pussy2
        else:
            show sc tattoo parlour b138a
        woman"If I do see you again..."
        if not persistent.v_sex_anim_enabled_locked and persistent.v_sex_anim_enabled:
            show sc tattoo parlour tatto girl fingering pussy3
        else:
            show sc tattoo parlour b137
        woman"I want to feel- NGHH..."
        woman"Your {b}big{/b} cock cum deep inside my tight...{w} wet...{w}..."
        # We see her legs clinch around the MC's hand as she climaxes
        if not persistent.v_sex_anim_enabled_locked and persistent.v_sex_anim_enabled:
            show sc tattoo parlour tatto girl fingering pussy4
        else:
            show sc tattoo parlour b139
        woman"OH FUCK ME!" with vpunch
        show sc tattoo parlour b140
        woman"Fuck yes!" with vpunch
        woman"Mmmm..." with vpunch
        woman"Your fingers are so wonderful..."
        show sc tattoo parlour b141
        woman"I hope I get to taste my cum on your cock next time."
        #She pulls his fingers out and then sucks on them to taste the juices
        show sc tattoo parlour b142
        woman"Mmm..."
        mc"(This chick is something else!)"
        # She winks at Bella as she rubs the MC's finger against her clit
        show sc tattoo parlour b143
        woman"And feel free to bring your gorgeous friend over there too."
        # She sticks out her tongue and holds up two fingers against her mouth as she says this
        show sc tattoo parlour b144
        woman"I can think of a few things I'd like to do to her too."
        if not persistent.v_sex_anim_enabled_locked and persistent.v_sex_anim_enabled:
            show sc tattoo parlour tatto girl going down tease1
        else:
            show sc tattoo parlour b145a
        pause 1.0
        b"(Yeah, like that'll happen. This bitch is crazy!)"
        show sc tattoo parlour b146
        b"(I can't believe [y_name] just has let her do all of that.)"
        show sc tattoo parlour b147
        woman"Thanks for the ride, handsome. Until next time..."
        # We see the woman walking out of the place from behind
        show sc tattoo parlour b148
        mc"Oh man, I hope I run into her again."
        show sc tattoo parlour b149
        mc"Then again, and again, and again after that!"
        #Bella gives a disgusted look
        show sc tattoo parlour b150
        b"Ughh..."
        # The tattooist returns
        show sc tattoo parlour b151
        tattooist"Okay, sorry for the wait."
        # MC has a big grin on his face
        show sc tattoo parlour b152a
        mc"No problem at all!"
        show sc tattoo parlour b152
        mc"We were just seeing your last client out. You have a wonderful place here, Sir!"
        show sc tattoo parlour b153
        tattooist"Huh?"
        show sc tattoo parlour b154
        b"You really are a pig."
        show sc tattoo parlour b155
        tattooist"Uh, sure."
        show sc tattoo parlour b156
        tattooist"Let me get the catalogue for you both to look through."
        tattooist"Was there a specific design that you were looking for?"
    elif v_ep01_06_02_Tattoo_Parlour_Tattoo_Response == "charming":
        scene sc tattoo parlour b062
        with dissolve
        tattooist"All right, looks like you’re up."
        tattooist"Let me get the catalogue for you both to look through."
        #Bella remains standing and shoots the MC a glaring look while the tattooist’ back is turned
        show sc tattoo parlour b063
        b"{i}(*Whispering*){/i}\nDo something."
        show sc tattoo parlour b064
        mc"{i}(*Whispering*){/i}\nRelax. I got this."
        show sc tattoo parlour b065
        tattooist"Was there a specific design that you were looking for?"
    else:
        scene sc tattoo parlour b062
        with dissolve
        tattooist"All right, looks like you’re up."
        tattooist"Let me get the catalogue for you both to look through."
        #Bella remains standing and shoots the MC a glaring look while the tattooist’ back is turned
        show sc tattoo parlour b063
        b"{i}(*Whispering*){/i}\nDo something."
        show sc tattoo parlour b066
        mc"{i}(*Whispering*){/i}\nRelax. I got this."
        show sc tattoo parlour b065
        tattooist"Was there a specific design that you were looking for?"
    scene sc tattoo parlour b067
    b"I um... I’m not sure. This is my first time."
    show sc tattoo parlour b068
    tattooist"No problem at all."
    show sc tattoo parlour b069
    tattooist"Here, have a good look through our portfolio. You might see something that stands out."
    #the tattooist hands Bella the design book
    show sc tattoo parlour b070
    mc"Hmm..."
    show sc tattoo parlour b071
    mc"I don’t suppose you have a design that looks like this by any chance?"
    #the MC points at the design to the artist on the sheet that he drew for Bella
    #the tattooist hesitates and doesn’t make eye contact with the MC. He has his head down as he replies
    show sc tattoo parlour b072
    tattooist"Um, no... No, we don’t."
    #Bella flicks the page over and sees the design the punk chick girl had
    show sc tattoo parlour b073
    b"What about this one?"
    #Bella shows him the identical image in the book and he has a guilty look on his face
    show sc tattoo parlour b074
    tattooist"Oh, right..."
    tattooist"Sorry, I only started here recently."
    #the MC shoots him a suspicious look
    show sc tattoo parlour b075
    tattooist"And I wouldn’t recommend that tattoo design for your, um..."
    #[Girlfriend / Friend / Sister]
    menu:
        "Girlfriend":
            show sc tattoo parlour b078
            mc"Girlfriend..."
            b"(Huh?)"
            show sc tattoo parlour b079
            mc"I just want the best for her, you know?"
            #the MC pulls Bella in close and kisses her on the cheek
            #she’s not impressed
            play sound "sound effects/01/Male_kissing_girl_on_the_cheek.mp3"
            show sc tattoo parlour b080
            mc"Mwah!"
            b"(I am so going to kill him for this later.)"
            stop sound fadeout 1.0
            $ v_ep01_06_02_Tattoo_Relationship_Choice = "Girlfriend"
            #mc"(He needs to believe that we’re together. That way. he might take us more seriously.)"
            #Bella shoots the MC a raised eyebrow look
        "Friend"(wt="Bonus Image"):
            show sc tattoo parlour b076
            mc"She’s my, um... friend."
            $ v_ep01_06_02_Tattoo_Relationship_Choice = "Friend"
            $ rewards_unlock ("bella",4)
            #Bella shoots the MC a raised eyebrow look
            show sc tattoo parlour b077
            tattooist"Oh."
        "[b_mc_rel!c]"(wt="Task Point"):
            show sc tattoo parlour b076
            mc"She’s my [b_mc_rel]."
            $ v_ep01_06_02_Tattoo_Relationship_Choice = "[b_mc_rel!c]"
            $ v_ep01_task04_help_bella_tattoo_parlour_counter += 1
            #Bella shoots the MC a raised eyebrow look
            show sc tattoo parlour b077
            tattooist"Oh."
    #scene continues
    tattooist"Anyway..."
    stop music fadeout 2.0
    play music2 "sound effects/01/Ink in Flesh.mp3" loop fadein 2.0
    show sc tattoo parlour b075
    tattooist"Some other design, perhaps?"
    #[Insist / Let [b_name] handle it]
    menu:
        "Insist"(wt="Task Point"):
            #Bella and the MC play good cop - bad cop. She looks nice and he looks threatening
            show sc tattoo parlour b081
            mc"No, this is the one she’s going to get."
            show sc tattoo parlour b082
            mc"And if not, then we’re going to go somewhere else."
            show sc tattoo parlour b083
            tattooist"Good luck with that. I’m the only one that inks that specific design."
            show sc tattoo parlour b084
            mc"Oh, so you know all about this one then, huh?"
            show sc tattoo parlour b085
            tattooist"(Shit! I wasn’t meant to say that.)"
            $ v_ep01_task04_help_bella_tattoo_parlour_counter += 1
            #the MC stands over the tattooist in a mildly threatening way"
            show sc tattoo parlour tattoist sit1
            mc"And you were lying about only starting here last week as well, weren't you?"
            #Bella looks up at the artist with adoring eyes, baiting him in
            show sc tattoo parlour b087
            b"It’s all right, um..."
            show sc tattoo parlour b088
            tattooist"Travis."
            show sc tattoo parlour b089
            b"Travis..."
            b"You can tell us."
            show sc tattoo parlour b090
            b"We won’t tell anyone. I promise."
            $ v_ep01_06_02_Tattoo_Parlour_Tattoo_Choice = "Force"
            show sc tattoo parlour b090a
        "Let [b_name] handle it"(wt="Extra images of [b_name]"):
            #BONUS IMAGES OF BELLA IF THE PLAYER CHOOSES THIS OPTION
            show sc tattoo parlour b091
            b"I’ve got this."
            #Bella addresses the MC and then sits up in the chair
            show sc tattoo parlour b092
            b"Why don't you please have a seat and relax, um..."
            show sc tattoo parlour b093
            tattooist"Travis."
            show sc tattoo parlour tattoist sit2
            b"Okay, Travis."
            b"Listen very carefully."
            show sc tattoo parlour b096
            b"We just want to know more about the design, where it came from or someone we can talk to who might be of some help."
            b"Right now, preferably."
            #Bella looks into his eyes, gives a slight smile and caresses his arm
            show sc tattoo parlour b097
            travis"I’d really like to, miss, but, I could get into a lot of trouble if I do that."
            show sc tattoo parlour b095
            b"Come on..."
            show sc tattoo parlour b098
            b"We won’t tell anyone. I promise."
            #Bella purposely bends forward to show him her huge cleavage
            if not persistent.v_sex_anim_enabled_locked and persistent.v_sex_anim_enabled:
                show sc tattoo parlour b099 at top
                travis"I-i’m sorry, but I-"
                scene sc tattoo parlour b099 at tt_02_06_02_Tattoo_top_down_2
                pause 1.5
                #the tattooist notices her cleavage
                travis"(Woah...)"
            else:
                show sc tattoo parlour b099 at top
                travis"I-I’m sorry, but I-"
                #the tattooist notices her cleavage
                show sc tattoo parlour b099 at center
                pause 1.5
                travis"(Woah...)"
            #mc"(Seems like she’s winning him over.)"
            #show a close-up of her chest
            mc"(Poor guy... No way could any man resist those.)"
            $ rewards_unlock ("bella",5)
            #THREE BONUS RENDERS OF BELLA (THREE NEW IMAGES OF HER IN THE TATTOO PARLOUR) ADDED TO THE PHOTO GALLERY FOR HER
            $ v_ep01_06_02_Tattoo_Parlour_Tattoo_Choice = "[b_name]"
            travis"I uh- I..."
            scene sc tattoo parlour b100
    #scene continues
    travis"Okay, fine..."
    show sc tattoo parlour b101
    travis"Maybe I know {i}something{/i} about it."
    show sc tattoo parlour b102
    travis"(Sigh...)"
    show sc tattoo parlour b103
    travis"It was meant to be taken out of our catalogue but the owner hasn't updated it yet."
    travis"I inked that design for someone just last week."
    show sc tattoo parlour b104
    mc"I need you to give me a name!"
    show sc tattoo parlour b105
    travis"Weren't your parents meant to do that?"
    #the tattooist misunderstands the question due to nervousness (humour)
    show sc tattoo parlour b106
    mc"A name of the person you did that tattoo for, dumbass!"
    show sc tattoo parlour b107
    travis"Oh, right."
    travis"Unfortunately, they paid in cash."
    travis"So we don’t have a record or even a booking name."
    show sc tattoo parlour b108
    mc"Damn..."
    show sc tattoo parlour b109
    b"Maybe we should come back tomorrow and talk to his boss about it."
    show sc tattoo parlour b110
    mc"Yeah, but that will be even more time wasted."
    show sc tattoo parlour b109
    b"Well what other choice do we have?"
    b"He doesn't actually know anything useful."
    #Bella and the MC arguing
    show sc tattoo parlour b111
    travis"Allow me to intervene if I may."
    show sc tattoo parlour b105
    travis"If time is an issue and you need to know more..."
    travis"Then there’s this club that our boss frequents in the evenings."
    travis"He'll be there tonight, actually."
    show sc tattoo parlour b106
    mc"What club?"
    show sc tattoo parlour b105
    travis"It’s called the \"Eager Beaver\"."
    show sc tattoo parlour b112
    b"Is it a men’s club?"
    show sc tattoo parlour b113
    travis"The name would suggest that, but no. It’s a pretty popular underground club."
    travis"And a decent pickup joint from what I’m told."
    show sc tattoo parlour b109
    b"You should check it out."
    show sc tattoo parlour b110
    mc"Yeah, tonight if possible."
    show sc tattoo parlour b113
    travis"If you do decide to go, and my boss asks who told you he'd be there, please leave my name out of it."
    travis"He'd beat me to a bloody pulp if he knew I put you onto him."
    show sc tattoo parlour b106
    mc"Why would he do that? Does he not want the extra business?"
    show sc tattoo parlour b107
    travis"It's kind of a long story."
    show sc tattoo parlour b105
    travis"But also, the owner is my brother."
    show sc tattoo parlour b104
    mc"Oh."
    show sc tattoo parlour b113
    travis"He gave me this job when I was desperate for work."
    show sc tattoo parlour b107
    travis"I'm on probation and I don't want to go back to a life of crime, ya know?"
    show sc tattoo parlour b108
    mc"Uh, yeah... Of course."
    show sc tattoo parlour b112
    b"Don't worry. He'll have no idea that we spoke to you."
    show sc tattoo parlour b106
    mc"Anything else?"
    show sc tattoo parlour b107
    travis"Nope, that’s it. I’ve told you everything I know."
    show sc tattoo parlour b114
    b"Thanks for your help, Travis."
    if v_ep01_06_02_Tattoo_Parlour_Tattoo_Choice == "[b_name]":
        show sc tattoo parlour b115
        b"Love the store by the way."
        if not persistent.v_sex_anim_enabled_locked and persistent.v_sex_anim_enabled:
            scene sc tattoo parlour bella walk
        else:
            show sc tattoo parlour b116
        travis"T-thanks!"
        #Travis watches Bella leave the store so her ass and legs are the focus

    #"Add these options if the player stole the old man’s wallet during the Vivian scene
    if v_ep01_06_01_Vivian_Work_Revenge == True:
        #[Tip him / Leave]
        menu:
            "Tip him"(wt="Best option + Task Point"):
                show sc tattoo parlour b118
                mc"Here..."
                mc"(Stealing that old man's wallet means I can afford to do this.)"
                #the MC hands him a $20 bill."
                show sc tattoo parlour b119
                mc"For your time."
                $ v_ep01_task02_girls_tattoo_counter += 1
                show sc tattoo parlour b120
                travis"Sweet!"
                $ v_ep01_06_02_Tattoo_Parlour_Tip = True
                show sc tattoo parlour b121
                pause 1.0
                stop music2 fadeout 1.0
                $ renpy.music.set_volume(1.0, 1.0, channel="music")
                scene black
                with dissolve
                scene black
                with Pause (2)
            "Leave":
                show sc tattoo parlour b121a
                mc"Thanks for your time..."
                stop music2 fadeout 1.0
                $ renpy.music.set_volume(1.0, 1.0, channel="music")
                scene black
                with dissolve
                scene black
                with Pause (2)
    else:
        #The MC follows Bella out of the store and Travis breathes a sigh of relief
        #screen goes blank
        show sc tattoo parlour b121a
        mc"Thanks for your time..."
        stop music2 fadeout 1.0
        $ renpy.music.set_volume(1.0, 1.0, channel="music")
        scene black
        with dissolve
        scene black
        with Pause (2)
    #scene returns with the MC and Bella outside the store again
    play ambient "sound effects/01/street_sound_day_ambience.ogg" loop fadein 1.0
    scene sc tattoo parlour b122
    with dissolve
    b"So, you now have a new lead on the tattoo. But what about the club?"
    $ v_ep01_task04_help_bella_tattoo_parlour_counter += 1
    show sc tattoo parlour b123
    mc"Well, we should go there tonight, shouldn’t we?"
    show sc tattoo parlour b124
    b"We? Yeah, nah..."
    b"You’re on your own with that one."
    b"I can’t be out after curfew, otherwise, [mc_vic_address] will have a fit!"
    show sc tattoo parlour b125
    mc"Shit..."
    mc"Okay, don’t worry about it. I’ll figure something out."
    if v_ep01_06_02_Tattoo_Parlour_Tattoo_Response == "crude":
        # Bella has a disgusted look on her face again.
        show sc tattoo parlour b157
        b"Oh and I hope you know that little show you put on in there with that insane woman was just gross."
        b"I can't believe you let her do something like that."
        show sc tattoo parlour b158
        mc"Sorry, at first I was taken by total surprise."
        mc"But in all honesty, what man in their right mind would ever protest to what happened in there?"
        show sc tattoo parlour b159
        b"Ugh, well I don't care what happens if you do see her again..."
        b"But if you know what's good for you, you will pretend her little offer to me never happened."
        show sc tattoo parlour b160
        b"GOT IT?!"
        show sc tattoo parlour b161
        mc"Okay, okay, I got it."
        show sc tattoo parlour b162
        mc"(Although, I'd be lying if I said that the thought hadn't crossed my mind.)"
        # A image flashes in the MC's head of the tattoo girl going down on bella, we only see a POV from bella's perspective.
        if not persistent.v_sex_anim_enabled_locked and persistent.v_sex_anim_enabled:
            show sc tattoo parlour tatto girl eating out
        else:
            show sc tattoo parlour b163
        with flash(0.2, 0, 0.2, "#fff")
        woman"Mmm..."
        b"Yes! Suck that clit you bitch!"
        scene sc tattoo parlour b162
        with flash(0.1, 0, 0.1, "#fff")
        with hpunch
        mc"(Shit!)"
        mc"(I better stop that imagery right there before I find [b_name]'s foot lodged in my ass.)"
    show sc tattoo parlour b122
    b"You better get to work. You wouldn’t want to be late."
    show sc tattoo parlour b126
    mc"You’re right..."
    show sc tattoo parlour b126
    mc"I guess I’ll speak with you tomorrow or whenever."
    show sc tattoo parlour b122
    b"Sure."
    show sc tattoo parlour b123
    mc"Thanks for helping me out with this."
    if v_ep01_task04_help_bella_tattoo_parlour_counter == 5:
        $ task_completed(4,"aa")
        $ v_ep01_bella_aa_tasks_counter += 1
    if v_ep01_task04_help_bella_tattoo_parlour_counter == 4:
        $ task_completed(4,"a")
    if v_ep01_task04_help_bella_tattoo_parlour_counter == 3:
        $ task_completed(4,"b")
    if v_ep01_task04_help_bella_tattoo_parlour_counter == 2:
        $ task_completed(4,"c")
    if v_ep01_task04_help_bella_tattoo_parlour_counter <= 1:
        $ task_completed(4,"d")
    show sc tattoo parlour b127
    b"It’s not like I had much choice."
    show sc tattoo parlour b128
    b"But you’re welcome, I suppose."
    show sc tattoo parlour b129
    b"See ya."
    #Bella turns and walks in the opposite direction - the MC watches her leave
    #screen goes blank "
    stop ambient fadeout 1.0
    scene black
    with dissolve
    scene black
    with Pause (2)
    jump lb_ep01_MC_rides_to_work
    #NEXT SCENE: ToH’s ep01 Scene 07-01
