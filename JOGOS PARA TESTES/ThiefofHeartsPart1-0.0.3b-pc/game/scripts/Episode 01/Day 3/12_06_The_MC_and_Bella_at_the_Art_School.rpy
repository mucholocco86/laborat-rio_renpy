init:
    $ v_ep01_task06_help_bella_counter = 0
    $ v_ep01_task06_help_bella_artclass = False



label lb_ep01_The_MC_and_Bella_at_the_art_school:
    centered "Twenty minutes later...{w=2.0}{nw}" with dissolve
    show text "Twenty minutes later..." #THESE LINES ARE NOT DUPLICATES. Needed to fade the text in and out!
    scene bg black with Dissolve(1)
    pause 1.0
    #The MC waits patiently outside the college for Bella to arrive which is quiet at this time - https://www.daz3d.com/morayta-university-entrance
    play ambient "sound effects/01/outside_college_campus_ambience.ogg" loop fadein 1.0
    scene sc artschool a001
    with dissolve
    b"Hey, I’m here."
    #The MC turns and sees Bella dressed in a school-like uniform - https://cdn.discordapp.com/attachments/396072929563246602/1210225215041306665/s-l1600.png?ex=65e9c910&is=65d75410&hm=300c576ba8ecbbbca84ec9f6d02175aad8c2317a5a1ac365193d3e9429bd0b6f&
    #Or - https://www.daz3d.com/flirty-school-uniform-for-genesis-8-female-s - https://www.daz3d.com/hot-uniforms-college-girl
    show sc artschool a002
    mc"Um... What is that you’re wearing?"
    show sc artschool a003
    b"It’s a college uniform that we acquired from one of the parents at that party we were at the other day."
    show sc artschool a004
    b"What do you think?"
    #she poses for him
    menu:
        "Cheeky response":
            mc"Hmm..."
            #The MC notices that Bella has changed clothes
            if not persistent.v_sex_anim_enabled_locked and persistent.v_sex_anim_enabled:
                scene sc artschool a006b at tt_top
                pause
            elif True:
                scene sc artschool a364
            #ROLLING SCREEN FOR BELLA IN THIS OUTFIT
            scene sc artschool a007
            mc"Are you meant to be a college student or are you performing at a mens bachelor party later tonight?"
            $ v_ep01_bella_arrogant_counter += 1
            show sc artschool a003
            b"Oh, piss off, [y_name]."
            show sc artschool a015
            mc"I'm just joking, [b_name]."
            show sc artschool a007
            mc"Don't worry, I'm sure you won't attract any attention once we're inside."
            show sc artschool a005
            mc"(I am lying my ass off.)"
        "Question her choice"(wt="Task Point"):
            show sc artschool a007
            mc"Don’t you think it’s a bit much?"
            show sc artschool a008
            b"What do you mean?"
            show sc artschool a009
            mc"What I’m saying is, you’ll stand out like a disco ball in a library."
            $ v_ep01_bella_cocky_counter += 1
            show sc artschool a010
            b"Nah, it’ll be fine."
            mc"Yeah, you're probably right."
            $ v_ep01_task06_help_bella_counter += 1
        "It should work":
            show sc artschool a009
            mc"Yeah, you look great."
            show sc artschool a004
            b"Oh, thanks..."
            show sc artschool a005
            b"(This is a surprise. I was fully expecting him to mock me.)"
            $ v_ep01_bella_respect_counter += 1
    show sc artschool a011
    b"So are we doing this or not?"
    show sc artschool a364
    mc"(I have to admit, she looks pretty damn good in that outfit.)"
    show sc artschool a365
    mc"(Hopefully, I can keep my focus on the job as soon as we get in there.)"
    show sc artschool a006
    mc"So once we’re in there, what do you want me to do?"
    show sc artschool a014
    b"Just help me find the art class and then I’ll locate the tools that [mc_vic_address] has asked me to steal."
    show sc artschool a015
    mc"Piece of cake!"
    show sc artschool a016
    b"Lets get going then..."
    #The MC walks towards the college with Bella - show them from behind
    stop ambient fadeout 1.0
    #screen goes blank
    scene black
    with dissolve
    scene black
    with Pause (2)

    #The MC walks towards the college with Bella - show them from behind
    #scene continues
    #College setting - https://www.daz3d.com/fg-university
    #This setting design has been used by a couple of well-known devs. So if you can find something else, something more unique, then choose that instead
    #https://www.daz3d.com/highschool-hallway
    #https://www.daz3d.com/school-hallway
    #https://www.daz3d.com/tesla3dcorp-high
    #Art Class - https://www.daz3d.com/the-artist-s-nook
    #Art Studio - https://www.daz3d.com/art-studio
    #https://media.istockphoto.com/id/1136806202/photo/large-group-of-students-having-an-art-class-with-their-teacher-in-a-studio.jpg?s=612x612&w=0&k=20&c=5hcQe62R_WOdAWgtYDGKP0zwxJ-nmEcjCOSmEnIG5hA=

    #the MC and Bella hide behind a wall and look down the corridor to see if the coast is clear - https://pixhost.to/show/1094/447975518_screenshot-2024-02-22-at-8-33-01-pm.jpg
    play music "sound effects/01/School Hallways1.mp3" loop fadein 1.0
    show sc artschool a017
    with dissolve
    b"Okay, it’s quiet enough for us to move around."
    #The MC walks with Bella down the hallway
    show sc artschool a018
    mc"Did you see anyone on the way in?"
    show sc artschool a019
    b"No, we should be fine."
    show sc artschool a020
    mc"What about the art class?"
    show sc artschool a021
    mc"Won’t there be students in there?"
    show sc artschool a022
    b"I checked this out. The art classes are usually in the mornings and straight after lunch."
    show sc artschool a023
    b"There is a class a little later on but we should be gone by then."
    show sc artschool a024
    b"So the room should be unoccupied right now."
    show sc artschool a025
    mc"How do you even know that this art class will have the things that you need?"
    show sc artschool a026
    b"It’s the best art school in the city. This class has pretty much everything."
    #A guy who looks like Mr. Strickland - https://static.wikia.nocookie.net/bttf/images/6/6c/Back-to-the-Future-back-to-the-future-8228558-640-480.jpg/revision/latest?cb=20110619071611 - comes around the corridor and sees the MC and Bella
    show sc artschool a027
    with vpunch
    the_dean"Hey! You two..."
    show sc artschool a028
    the_dean"Shouldn’t you be in class?"
    #[Handle the situation / Let [b_name] handle it]
    menu:
        the_dean"Shouldn’t you be in class?"
        "Handle the situation"(wt="Task Point"):
            show sc artschool a029
            mc"We were asked to bring some items to the art class, Sir."
            show sc artschool a030
            the_dean"Firstly, you will address me as Dean Pritchard."
            show sc artschool a031
            mc"Yes, of course."
            show sc artschool a032
            the_dean"These items are for Miss Cleary’s art class I presume?"
            show sc artschool a033
            mc"That’s right!"
            show sc artschool a034
            the_dean"I see."
            show sc artschool a035
            the_dean"Well, no doubt she’ll appreciate you helping her out."
            show sc artschool a036
            the_dean"Are you two staying back to take her class?"
            show sc artschool a037
            mc"Uh, yeah... Sure we are."
            $ v_ep01_task06_help_bella_counter += 1
            show sc artschool a038
            the_dean"I’m sure it will be a real eye-opener for you both."
            show sc artschool a039
            the_dean"Anyway, off you go."
            show sc artschool a040
            b"Yes, Dean Pritchard."
            #the dean leaves
            show sc artschool a041
            b"Damn... That was close."
            show sc artschool a049
            b"What do you think he meant about this art class being an eye-opener?"
            show sc artschool a052
            mc"Beats the hell out of me."
            show sc artschool a054
            b"Come on, let’s get what we came here for before we run into anyone else..."
            stop music fadeout 1.0
            #screen goes blank
            scene black
            with dissolve
            scene black
            with Pause (2)

            #GO DOWN TO > #scene continues

        "Let [b_name] handle it"(wt="Funnier option"):
            show sc artschool a326
            b"Sorry, Sir."
            b"We were just on our way back."
            show sc artschool a328
            the_dean"You will address me as Dean Pritchard."
            show sc artschool a329
            b"Yes, of course."
            #the dean looks the MC up and down
            show sc artschool a330
            the_dean"I’ve never seen you around here before, son."
            show sc artschool a331
            b"This is um, Larry."
            show sc artschool a332
            b"He’s a special needs kid who is new to the college."
            show sc artschool a333
            mc"(What the fuck??)"
            #The MC gives Bella a strange look
            show sc artschool a334
            b"I was showing him around and he’s also going to help me to take some items to the art class."
            #the dean eyes up the MC
            show sc artschool a335
            the_dean"He doesn’t say much."
            #The MC acts like a special needs kid
            show sc artschool a333
            mc"(God damn you, [mc_b_address]...)"
            show sc artschool a336
            mc"My name is Larry..."
            show sc artschool a337
            mc"LARRY!"
            show sc artschool a338
            the_dean"Hmm... It makes complete sense why you’re assisting him."
            show sc artschool a339
            the_dean"However, I think we could do with a kid like him on the special needs football team."
            show sc artschool a338
            the_dean"They mainly use a balloon, but I'm sure young Larry will enjoy it a lot."
            show sc artschool a366
            b"I’ll recommend him to the coach."
            show sc artschool a341
            the_dean"Good idea."
            #the dean looks at Bella
            show sc artschool a342
            the_dean"And I see that you’re parading the new college uniform."
            show sc artschool a343
            b"Oh... Yeah, that’s right!"
            show sc artschool a344
            the_dean"Very nice."
            show sc artschool a345
            the_dean"So you said that you’re getting some things for Miss Cleary’s art class."
            show sc artschool a346
            b"We were just about to go and collect them."
            show sc artschool a347
            the_dean"Well, no doubt she’ll appreciate you helping her out."
            show sc artschool a348
            the_dean"Are you two also staying back to take her class?"
            show sc artschool a349
            b"Yes, we are."
            show sc artschool a330
            the_dean"I’m sure it will be a real eye-opener for you both."
            show sc artschool a328
            the_dean"Anyway, off you go."
            show sc artschool a352
            b"Yes, Dean Pritchard."
            #The Dean leaves
            show sc artschool a353
            b"Damn... That was close."
            #The MC looks at Bella unimpressed
            show sc artschool a354
            mc"Special needs kid... Really?"
            show sc artschool a355
            b"Haha! It was all I could think of on the spot."
            show sc artschool a358
            b"And besides, he bought it."
            show sc artschool a356
            mc"I can’t believe he didn't say much about your highly-revealing uniform."
            #Bella poses in her uniform
            show sc artschool a357
            b"You seem genuinely surprised."
            b"I guess he just presumed that this is the new one."
            show sc artschool a358
            b"Wearing this uniform doesn’t seem so ridiculous now, does it?"
            show sc artschool a359
            b"Plus it was the perfect distraction for old geezers like the dean."
            mc"(Damn, she’s got me there.)"
            show sc artschool a362
            b"What do you think he meant about this art class being an eye-opener?"
            show sc artschool a363
            mc"Beats the hell out of me."
            show sc artschool a054
            b"Come on, let’s get what we came here for before we run into anyone else..."
            #screen goes blank
            stop music fadeout 1.0
            scene black
            with dissolve
            scene black
            with Pause (2)

    #scene continues

    #The MC enter the art studio/class - https://i.etsystatic.com/8102476/r/il/93b6c6/3639162290/il_fullxfull.3639162290_eqwa.jpg
    #IMPORTANT: Have a shelf in the room that has a stock of paints, supplies and chemicals - https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhcQAFWjgHkSWBhEg4kXJQSb-PE1HejvlPbHvOAUEplqH2ZkQ99busxvC83EN81qez92-RyVmLgyVznae8EyPq8adZIEQLNUHU717kYMCvi8lkIy3dnXEOlRJg6DjFT0k_B6jjaH4mlgbU/d/Paint+organized.jpg
    play music "sound effects/01/School Hallways2.mp3"
    show sc artschool a055
    with dissolve
    b"Deserted, just as predicted."
    show sc artschool a056
    mc"What exactly are we looking for again?"
    show sc artschool a057
    b"Okay... So I’m going to need a specific set of paints, brushes and canvases, preferably rolled up so it will be easier to transport out of here."
    show sc artschool a058
    b"As I said before, they all should be somewhere in this room."
    #Bella pulls out her phone and the MC looks at it to
    show sc artschool a059
    b"This is kind of what they should look like."
    #she flicks through each item on her phone but we don’t see what they are looking at
    show sc artschool a061
    mc"But why these items? Why can’t we get them from a local paint or stationery store?"
    show sc artschool a062
    b"These aren’t ordinary supplies, [y_name]."
    show sc artschool a063
    b"I did some research on the main art professor at this college."
    show sc artschool a064
    b"A lot of these items that we need are exclusive to this college."
    show sc artschool a065
    b"The professor has a lot of contacts in Europe and orders the paints and oils specifically for these classes."
    show sc artschool a066
    b"You can’t find them anywhere else in the city and if I’m going to forge this painting, then they will enable me to do the job correctly."
    show sc artschool a067
    mc"Even the brushes?"
    show sc artschool a068
    b"Well, while we’re here we may as well take them as they will be of high quality."
    show sc artschool a069
    b"But to make the painting look old and authentic, we need to find a small tub of potassium sulphite."
    show sc artschool a070
    b"I’ll get you to focus on finding the first three items first."
    show sc artschool a062
    mc"All right, well let’s split up and we’ll find them together."
    #The MC and Bella are on opposite sides of the room
    #the MC looks at the various items/equipment in the room
    show sc artschool a072
    with dissolve
    mc"(Okay, so she said that we’re looking for a set of paints, brushes, and some rolled-up canvases.)"
    #The MC looks over at Bella who has her back turned to him
    show sc artschool a076
    mc"(Damn... Could her skirt be any shorter?)"

    #[Look for the items / Hold your gaze]
    menu:
        mc"(Damn... Could her skirt be any shorter?)"
        "Look for the items"(wt="Task Point"):
            show sc artschool a075
            mc"(Hmm... I need to focus on the task at hand.)"
            $ v_ep01_task06_help_bella_counter += 1
            scene black
            with dissolve
            scene black
            with Pause (2)

    #GO TO > scene continues

        "Hold your gaze"(wt="Bonus Image"):
            show sc artschool a078a
            mc"(Yet, I can’t look away.)"
            #Bella bends over slightly and the MC can see up the back of her skirt and the curves of her ass
            mc"(Damn...)"
            if not persistent.v_sex_anim_enabled_locked and persistent.v_sex_anim_enabled:
                scene sc artschool a078 at tt_top
                pause
            elif True:
                scene sc artschool a078a
            #ROLLING SCREEN of Bella bent over
            mc"(Does she know I’m staring at her, and she’s teasing me on purpose?)"
            $ rewards_unlock ("bella",7)
            #Bella calls out without turning around
            scene sc artschool a078a
            b"Have you found anything yet?"
            show sc artschool a081
            mc"Oh, err, I guess you could say I did, but not what you need."
            #TWO BONUS RENDERS OF BELLA (IN HER UNIFORM) ADDED TO THE PHOTO GALLERY FOR HER PROFILE
            show sc artschool a076
            mc"(I need to focus on the task at hand.)"
            scene black
            with dissolve
            scene black
            with Pause (2)

    #scene continues

    #NOTE: This will be a "Point & Click" game - the player will be shown the entire art class.
    #All they have to do is click on the three items that Bella has described

    #show sc artschool a083

    #ITEMS to be placed around the class
    #- A rolled up canvas - https://artsuppliesaustralia.com.au/cdn/shop/articles/d7bcd302f05687a5b400beced5569322.jpg?v=1660782723
    # - A set of paints -
    # - A set of specific brushes

    #https://www.daz3d.com/hobby-props-art-supplies

    #HYPER - I kind of like that idea - just I wouldn't make it that easy to find the stuff. Make it hard to find (For those puzzle fans), but ALSO LEAVE a skip button somewhere for those who don't want to puzzle at all

    #An example of what the room could look like and where these three items could be placed - https://pixhost.to/show/1108/448186920_screenshot-2024-02-23-at-9-45-41-am.png

    #Once the player has found them all, the scene will continue

    show sc artschool a084
    with dissolve
    mc"[b_name]? I’ve found all three of those items you asked for."
    show sc artschool a084
    b"Awesome!"
    #Bella looks around the classroom
    show sc artschool a086
    b"Hmm..."
    mc"Are you all right?"
    show sc artschool a085
    mc"You look like you have something on your mind."
    show sc artschool a089
    b"Oh, it’s nothing."
    show sc artschool a087
    mc"Come on, [mc_b_address]."
    show sc artschool a090
    mc"Tell me."
    show sc artschool a092
    b"It’s just... This art class is even more incredible than the photos I’ve seen online."
    show sc artschool a093
    b"It doesn’t do it justice in any way, shape or form."
    show sc artschool a100
    mc"Why don’t you apply?"
    show sc artschool a101
    b"I wanted something like this several years ago."
    show sc artschool a096
    b"My art teacher in high school said I had the most potential of any student that he’d ever taught before."
    show sc artschool a100
    mc"So what happened?"
    show sc artschool a098
    b"The same thing that always happens to us. We needed the money."
    b"That was the most important thing."
    show sc artschool a100
    b"So I worked various jobs while learning everything that [mc_vic_address] taught me."
    show sc artschool a101
    b"But the more I worked, the less that art became a focus for me."
    show sc artschool a098
    b"And I eventually had to give up on it."
    show sc artschool a102
    mc"I’m sorry, [b_name]. I had no idea."
    show sc artschool a103
    b"It’s fine. I guess some things aren’t meant to be."
    #Bella looks up at the stand of paints and oils that goes up to the ceiling - https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhcQAFWjgHkSWBhEg4kXJQSb-PE1HejvlPbHvOAUEplqH2ZkQ99busxvC83EN81qez92-RyVmLgyVznae8EyPq8adZIEQLNUHU717kYMCvi8lkIy3dnXEOlRJg6DjFT0k_B6jjaH4mlgbU/d/Paint+organized.jpg
    show sc artschool a104
    b"Hey... I think I can see the paint thinner up on that shelf."
    show sc artschool a105
    b"Can you hold the ladder steady while I go up there to get it?"
    show sc artschool a107
    mc"Oh, sure thing."
    #Bella climbs a ladder of paint supplies and chemicals
    show sc artschool a108
    with dissolve
    mc"(This would be the worst time for someone to walk in right now.)"
    #The MC holds the ladder while Bella is above him on the ladder
    show sc artschool a109
    mc"(As soon as we get this last item, we’re out of here.)"
    #Bella looks through the tubs of paints and chemicals
    show sc artschool a110
    b"Hmm... I'm pretty sure this is it."
    b"I just need to find out for sure."
    #The MC looks up so he can see directly up the back of Bella’s skirt
    show sc artschool a111
    mc"(Oh shit...)"
    mc"(It’s only when I see her skirt from this angle that I realise just how damn short it is!)"
    #[Look away / Take a closer look]

    menu:
        mc"(It’s only when I see her skirt from this angle that I realise just how damn short it is!)"
        "Look away"(wt="You will take an Art Class + 2 Task Points"):
            $ v_ep01_task06_help_bella_artclass = True
            #The MC and Bella stay for the art class
            show sc artschool a113
            mc"(No, I can’t get distracted.)"
            show sc artschool a114
            mc"(If I stared any longer, she may have noticed.)"
            show sc artschool a115
            mc"(Or worse, she could fall.)"
            show sc artschool a116
            b"Okay, I got it!"
            #She looks down at the MC who is looking away
            show sc artschool a117
            b"Hmm..."
            show sc artschool a118
            b"Did you see anything?"
            show sc artschool a119
            mc"Huh?"
            show sc artschool a120
            b"Outside the class."
            show sc artschool a121
            b"Did you see anyone looking in or passing by?"
            mc"Uh, no. Not at all."
            #Bella gets down from the ladder and places the items in their carry bag
            show sc artschool a123
            with dissolve
            b"All right..."
            show sc artschool a124
            b"Let’s get the hell out of here before we-"
            #The art-class teacher enters the room - https://www.daz3d.com/z-professions-teacher-pose-mega-set-for-genesis-9-and-8-female
            show sc artschool a125
            teacher"Ah, excuse me. Can I help you two?"
            show sc artschool a126
            b"Oh, um... We were just..."
            show sc artschool a127
            mc"Here for the art class."
            show sc artschool a128
            mc"Sorry if we’re a little early."
            show sc artschool a129
            teacher"Oh, that’s perfectly fine."
            show sc artschool a130
            teacher"Feel free to take a seat."
            teacher"We'll begin once the rest of the class and our special guests have arrived."
            mc"(Special guests?)"
            show sc artschool a132
            mc"Sure, we’ll do that."
            #The MC and Bella sit down on stools in front of a blank canvas
            show sc artschool a133
            b"What are you doing?"
            show sc artschool a134
            mc"Blending in."
            show sc artschool a135
            mc"Besides, if we try and leave now, then it will look too suspicious."
            show sc artschool a136
            mc"Especially because we have..."
            #The MC points down to the items that they stole which are in their bag
            show sc artschool a137
            mc"...these in our possession."
            show sc artschool a138
            b"Shit..."
            show sc artschool a139
            b"So what now?"
            show sc artschool a140
            mc"We sit through this class, and once it’s finished, we leave, calmly and casually."
            show sc artschool a141
            b"(I have a bad feeling about this...)"
            stop music fadeout 1.0
            #screen goes blank
            scene black
            with dissolve
            scene black
            with Pause (2)



            #scene returns with more people in the class - a few males and a few females
            show sc artschool a142
            teacher"Thank you everyone for attending this afternoon’s very special class."
            show sc artschool a143
            teacher"And today you’re in for a real treat, especially for those who are interested in modern and abstract art."
            show sc artschool a144
            teacher"Which brings me to our special guest."
            #A young woman wearing a robe - https://naked.titis.org/uploads/posts/2023-03/1678644435_naked-titis-org-p-sophia-myles-naked-erotika-vkontakte-3.jpg-  https://www.aznude.com/view/movie/a/artschoolconfidential.html?jwsource=cl
            show sc artschool a145
            with dissolve
            teacher"This is Sophie."
            show sc artschool a146
            teacher"She’ll be our figure model for today’s session."
            show sc artschool a147
            mc"(Model?)"
            #The young woman sheds her robe and is nude underneath - https://cdn1.aznude.com/sophiamyles/artschoolconfidential/myles-art-n-04.jpg
            show sc artschool a148
            with vpunch
            mc"(Oh my God!)"
            show sc artschool a150
            b"Oh my..."
            show sc artschool a151
            b"[y_name]! This is..."
            show sc artschool a152
            mc"Yeah, it is."
            show sc artschool a153
            b"Well, we have to get out of here!"
            show sc artschool a154
            mc"Why?"
            show sc artschool a156
            b"Because!"
            show sc artschool a159
            b"Don’t you think this is a little uncomfortable?"
            show sc artschool a160
            mc"Not at all."
            #The MC looks the nude model up and down
            show sc artschool a148
            mc"I’ve always had a keen interest in... abstract art."
            #Bella shoots the MC a snarky look while he continues to gaze at the nude model who gives him an obvious smile
            show sc artschool a162
            mc"Don’t just sit there, [b_name]..."
            show sc artschool a148
            mc"Pick up a brush and get to painting or whatever it is you’re meant to do."
            #Show the MC with a silly grin on his face as he tries to paint the model
            show sc artschool a159
            b"(How is that I’m the one who loves art yet he is enjoying this more than I am?)"
            scene black
            with dissolve
            scene black
            with Pause (2)

            #show the nude model in a different pose
            #The teacher walks around looking at each class member’s drawings of Sophie - https://pixhost.to/show/1144/448532967_img_7447.jpg
            play music "sound effects/01/Painting Dreams1.mp3"
            show sc artschool a163
            mc"(This is awesome!)"
            $ v_ep01_task06_help_bella_counter += 1
            show sc artschool a164
            b"(This is so embarassing.)"
            show sc artschool a165
            b"(He must be loving this right now.)"
            show sc artschool a166
            teacher"Good..."
            #She checks the MC’s drawing of Sophia - https://pixhost.to/show/1144/448532980_img_7450.jpg
            show sc artschool a167
            teacher"Hmm..."
            show sc artschool a168
            teacher"I have to say..."
            show sc artschool a168b
            teacher"I’m seeing a bit of a Picasso influence here."
            #Bella looks jealous
            show sc artschool a169
            b"(Is she fucking kidding me??)"
            show sc artschool a170
            mc"Well what can I say? I’m influenced by the absolute greats."
            show sc artschool a171
            teacher"Indeed..."
            #The teaches wanders back to the front of the class
            show sc artschool a163
            teacher"Marvellous!"
            show sc artschool a164
            teacher"Another triumph!"
            #the art teacher stands before Bella's painting
            show sc artschool a369
            teacher"Hmm..."
            #the teacher studies Bella's painting
            b"Is there something wrong?"
            #Bella looks confused
            show sc artschool a370
            teacher"The color palette you've chosen is...interesting, though I'm not sure if that's the right word for it."
            #The teacher looks bemused
            show sc artschool a371
            teacher"I can see that you're attempting to create some sort of balance, but it looks like you just threw things on the canvas without a second thought."
            show sc artschool a372
            teacher"Were you in a rush? Because it certainly has this 'last-minute homework' vibe to it."
            #Teacher is being condescending
            show sc artschool a164
            b"(Sigh... This day just keeps getting worse.)"
            #Bella looks down
            b"(I want to bite back and tell this bitch what I think of her...)"
            #Bella looks like she wants to retaliate
            show sc artschool a169
            b"(But I don't want to make a scene.)"
            #She then changes her mind and tries not to show she's upset
            show sc artschool a168
            teacher"You should spend some more time learning from this young man."
            show sc artschool a171
            #The teacher puts her hand on the MC's shoulder while she speaks to Bella
            teacher"I'm sure he could teach you a few handy tips and tricks."
            #The teacher looks at the MC, impressed
            show sc artschool a159
            b"(Seeing as you got us into this situation [y_name], I'm going to make you pay for this.)"
            #Bella shoots the MC a pissed-off look, mouth closed
            #She gets the MC back shortly by volunteering him to be a nude model
            show sc artschool a172
            teacher"Thank you, Sophie. You can put your robe back on."
            #Teacher addresses the class
            show sc artschool a173
            with dissolve
            teacher"Very good, all of you. Some interesting portrayals of how you see abstract art."
            show sc artschool a174
            teacher"I forgot to mention that we were also meant to have a male model joining us today, but he called in sick and was unable to make it."
            show sc artschool a175
            teacher"So it looks like we’re going to end our class a little earlier than usual."
            show sc artschool a176
            teacher"Unless of course one of you fine gentlemen doesn’t mind standing in as our male model."
            play sound "sound effects/01/small_class_laughing_effect.mp3"
            show sc artschool a175
            class"Hahaha!"
            show sc artschool a178
            teacher"I’m kidding, of course."
            if v_ep01_06_02_Tattoo_Relationship_Choice == "Girlfriend":
                show sc artschool a186
                b"(Time to get a little revenge for that \"Girlfriend\" thing [y_name] did at the Tattoo parlour yesterday.)"
            stop sound fadeout 1.0
            #Bella grabs the MC’s hand and raises it
            show sc artschool a179
            b"He’ll do it!!"
            #Everybody turns to look at the MC, including the teacher
            stop music fadeout 1.0
            show sc artschool a181
            with vpunch
            mc"(What the hell??)"
            stop sound fadeout 1.0
            show sc artschool a182
            teacher"Oh..."
            #The MC looks shocked
            show sc artschool a184
            teacher"That’s wonderful!"
            show sc artschool a185
            teacher"I admire your confidence, young man. Come on up here!"
            #Bella looks at the MC with a funny smirk
            mc"(Fuck!)"
            show sc artschool a186
            b"(Serves you right for being so cocky, [b_mc_address].)"
            show sc artschool a188
            mc"(Hmm...)"
            show sc artschool a189
            mc"(All right, [mc_b_address]... I’ll play your game.)"
            #The MC approaches the teacher
            show sc artschool a190
            teacher"Thank you for filling in."
            teacher"I'm looking forward to this."
            show sc artschool a191
            teacher"You’ll find a robe when you can get changed in the back room."
            show sc artschool a190
            teacher"We'll see you shortly..."
            #screen goes blank
            scene black
            with dissolve
            scene black
            with Pause (2)

            #the scene returns with the class waiting for the MC to return
            show sc artschool a193
            teacher"Are you okay back there?"
            show sc artschool a194
            mc"Yeah, I'll be out in a sec."
            #Bella has a cocky smile on her face
            show sc artschool a195
            b"(He’ll back out for sure. There’s no way [y_name] will-)"
            #The MC comes out to the floor wearing just a robe
            show sc artschool a196
            mc"Sorry about that."
            show sc artschool a206
            b"(Oh my God! He might actually go through with it!)"
            show sc artschool a197
            mc"I’m ready to be your... muse."
            #He says confidently
            show sc artschool a198
            teacher"Marvellous!"
            #The teacher addresses everyone in the class while the MC moves towards the stool at the front
            show sc artschool a199
            teacher"Remember what I said earlier on, class. Today’s assignment is about shadow."
            show sc artschool a200
            teacher"So don’t get too hung up on details."
            #The MC takes his robe off- https://pixhost.to/show/1144/448537369_screenshot-2024-02-24-at-10-58-46-pm.jpg -
            show sc artschool a202
            teacher"All right, everybody..."
            show sc artschool a204a
            teacher"Looks like our model is ready to go."
            menu:
                "Take the robe off":
                    show sc artschool a204b
                    with vpunch
            play sound "sound effects/01/classroom_gasp.mp3"
            teacher"You may begin."
            show sc artschool a203
            student1"Oh wow..."
            #The MC makes this pose - https://pixhost.to/show/1144/448537361_screenshot-2024-02-24-at-10-58-10-pm.jpg
            stop sound fadeout 1.0
            show sc artschool a205
            student2"So much sinew."
            play music "sound effects/01/In The Pocket.mp3" loop fadein 1.0
            show sc artschool a204
            student2"I’m going to need a bigger pencil."
            #Bella’s looks surprised
            show sc artschool a206
            b"(Oh my God...)"
            show sc artschool a213
            b"([y_name] just went the Full Monty!)"
            #Bella’s eyes widen when she looks down at the MC crotch - https://pixhost.to/show/1144/448537364_screenshot-2024-02-24-at-10-58-22-pm.jpg
            show sc artschool a207
            b"(I hate to admit this, but I’m pretty impressed.)"
            #Bella realises what she just thought, and her expression changes
            show sc artschool a208
            b"(I mean... ew!)"
            show sc artschool a209
            teacher"I hope you’re all inspired, class."
            #The teacher has a big closed smile on her face as she admires the MC’s figure
            show sc artschool a210
            teacher"I certainly am."
            #Bella starts drawing the MC on her canvas and has a little smile - https://pixhost.to/show/1144/448537367_screenshot-2024-02-24-at-10-58-33-pm.jpg
            show sc artschool a211
            b"(Well played, [b_mc_address].)"
            b"(I didn't think you had it in you.)"
            #The MC smiles at Bella
            show sc artschool a212
            b"(You’ve won this round.)"
            $ v_ep01_task06_help_bella_counter += 1
            show sc artschool a204
            b"(And a lot of new admirers from what I can tell...)"
            stop music fadeout 1.0
            #screen goes blank
            scene black
            with dissolve
            scene black
            with Pause (2)

            #The scene returns with Bella waiting in class for the MC to get changed
            #Everyone else has left
            show sc artschool a216
            b"So... I guess some congratulations are in order?"
            show sc artschool a217
            mc"Nah, there’s no need for that."
            show sc artschool a218
            b"I don’t know how you could be so calm about all this."
            mc"I’ve been in worse situations."
            show sc artschool a220
            b"For some strange reason, I believe you."
            show sc artschool a221
            mc"So... Did you enjoy the show?"
            show sc artschool a222
            b"I am not answering that."
            show sc artschool a223
            mc"I’ll take that as a yes then."
            show sc artschool a224
            mc"Come on, grab the bag with the stuff and let’s get out of here."
            #show them leaving the classroom - the MC before Bella
            show sc artschool a225
            b"That wasn’t a yes, [y_name]!"
            show sc artschool a226
            mc"Keep telling yourself that, [mc_b_address]."
            #The MC exits the classroom, taunting Bella while she is still arguing and chasing him out of the class
            show sc artschool a227
            with dissolve
            b"[y_name]!"
            show sc artschool a228
            with dissolve
            b"[y_name]!!"
            #screen goes blank
            scene black
            with dissolve
            scene black
            with Pause (2)

            #GO DOWN TO > #scene continues

    #- - - - - - - - - - - - - - - - - - - - - - - - - - -  - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

        "Take a closer look"(wt="You will go to the Girls Locker Room +2 Task Points"):

            show sc artschool a240
            mc"(I may never get a chance like this again.)"
            #Show Bella looking at a tub of paint thinner
            show sc artschool a230
            b"(Hmm... This one isn’t labelled, but I have a feeling that it could be paint thinner.)"
            #Show a close-up between Bella’s legs so the MC can see her thong panties
            show sc artschool a231
            mc"(Holy shit! Is she wearing a thong??)"
            #Bella opens the tub of paint thinner
            show sc artschool a233
            b"(Yep, just as I suspected.)"
            show sc artschool a234
            b"(On second thought, I probably don’t need this. I should have enough at home.)"
            #Bella looks down and panics while she’s still holding the open tub of paint thinner
            show sc artschool a231
            mc"Mmm..."
            show sc artschool a237a
            with hpunch
            b"[y_name]! Hold the ladder still... Oh!!"
            show sc artschool a237b
            with vpunch
            mc"Oh fuck!!"
            #Bella grabs the ladder tightly and spills the pain thinner on herself
            #screen shakes
            show sc artschool a237c
            with vpunch
            b"Shit! Shit! Shit!"
            show sc artschool a239
            mc"[b_name]??"
            show sc artschool a240
            mc"Are you okay?"
            show sc artschool a241
            b"No, I’m not okay!! Look at my outfit!!"
            #Show Bella’s uniform with a paint thinner stain on it - https://cdn.apartmenttherapy.info/image/upload/v1582640660/at/art/photo/2020-02/clean-paint-out-of-clothes/oil-based-paint-fresh-thinner.jpg
            show sc artschool a242
            mc"What happened?"
            show sc artschool a241
            b"I'm coming down..."
            show sc artschool a243
            with dissolve
            b"I slipped and spilt some paint thinner on myself. The lid wasn’t screwed on."
            #Bella looks at her top covered in paint thinner
            show sc artschool a244
            mc"(Oh, shit... I can’t tell her that it’s probably my fault that this happened.)"
            show sc artschool a245
            b"God dammit. What am I going to do?"
            show sc artschool a246
            b"I can't walk around the campus grounds looking like this!"
            show sc artschool a245
            mc"I have an idea. We can find you some other clothes."
            show sc artschool a248
            b"Where the hell am I going to get them from?"
            b"If you haven’t noticed already, this is an art class."
            show sc artschool a249
            mc"Well, when we went past the gymnasium on the way in, the girls were playing basketball in there."
            show sc artschool a250
            b"Of course you noticed that."
            show sc artschool a248
            b"What’s your point?"
            mc"Some of those girls would surely have a change of clothes in the locker room, as they’re all wearing what looked like matching basketball tops."
            show sc artschool a253
            b"That’s your grand plan? To steal another girl’s clothes?"
            show sc artschool a254
            mc"Do you have a better idea?"
            show sc artschool a255
            b"Hmm..."
            show sc artschool a256
            b"Fine. It looks like we don’t have any other options."
            show sc artschool a257
            mc"We better get a move on then. Just in case anyone sees you in here like this."
            show sc artschool a258
            b"This better work otherwise you are dead meat when we get home..."
            mc"(Gulp! I think she knows that it was me who caused this...)"
            stop music fadeout 1.0
            #screen goes blank
            scene black
            with dissolve
            scene black
            with Pause (2)



            #scene returns with the MC and Bella in the girls’ locker room - https://image1.masterfile.com/getImage/614-02984823em-cheerleaders-in-locker-room-stock-photo.jpg
            show sc artschool a260
            with dissolve
            mc"Look, there's plenty of the girls' clothes on the bench."
            show sc artschool a261
            mc"Find a top and skirt in your size and then we can get going."
            show sc artschool a262
            b"Okay, okay. Don’t rush me."
            b"You stay right here and keep an eye out in case someone comes in."
            #The MC stays put while Bella looks through the girl’s clothing which is on a bench in the locker room
            scene black
            with dissolve
            pause 0.5
            show sc artschool a264
            with dissolve
            mc"(Damn... This is nerve-racking but also really exciting!!)"
            show sc artschool a266
            mc"(It would be a hell of a way for me to get caught.)"
            show sc artschool a265
            mc"(I can already see the weekly college newsletter front page now...)"
            mc"{i}(Local pervert gets caught in the girls locker room!){/i}"
            b"Hey...?"
            #Bella finds some girls’ clothes
            show sc artschool a268
            b"I think I found some clothes that will fit."
            show sc artschool a269
            b"Go around the corner so I can get changed."
            show sc artschool a270
            b"And don’t even think about taking a peek. I know what you can be like, [b_mc_address]."
            mc"I don’t know what you’re talking about..."
            #The MC walks around the corner so he can’t see Bella changing
            scene black
            with dissolve
            pause 0.5
            play music "sound effects/01/Midnight Heist.mp3" loop fadein 1.0
            show sc artschool a272
            with dissolve
            mc"(Hmm...)"
            show sc artschool a273
            mc"(It’s tempting to look, but she’ll put my balls in a blender if I even think about popping my head around the corner.)"
            #cross-screen fade
            show sc artschool a274
            mc"[b_name]!"
            show sc artschool a275
            mc"Are you decent?"
            show sc artschool a276
            b"[y_name]! I need your help!!"
            show sc artschool a277
            mc"(Huh?)"
            #The MC goes around the corner and sees Bella in her replacement uniform
            #Her skirt fits but her top is too small, leaving her noticeable in a bra and the school shirt can barely cover it
            show sc artschool a281a
            with dissolve
            mc"What’s wrong?"
            show sc artschool a280
            with dissolve
            b"Isn’t it obvious?"
            b"This damn shirt is way too small!!"
            show sc artschool a281
            b"My uh... My chest feels like it's going to fall out of it!"
            b"And I can't put my bra back on as it's still stained and wet."
            mc"(If it were up to me, I'd make her walk out dressed like this!)"
            show sc artschool a281a
            menu:
                "Ask about her skirt"(wt="Task Point"):
                    show sc artschool a281a
                    mc"What happened to your skirt?"
                    $ v_ep01_task06_help_bella_counter += 1
                    show sc artschool a281
                    b"It's also stained and a little wet."

                    menu:
                        b"It's also stained and a little wet."
                        "Move on":
                            show sc artschool a280
                            b"What am I going to do?"
                        "Suggest something"(wt="Task Point"):
                            mc"Let me see it from the back."
                            show sc artschool a280
                            b"What for?"
                            show sc artschool a281a
                            mc"Turn around for me. I wanna check something."
                            mc"Quickly now."
                            show sc artschool a281
                            b"Um, okay."
                            show sc artschool a281b
                            with dissolve
                            pause 2.0
                            show sc artschool a281c
                            with dissolve
                            mc"(Damn...)"
                            show sc artschool a281e
                            mc"(Now I don't feel guilty about her spilling that stuff on her dress.)"
                            show sc artschool a281d
                            b"[y_name]?"
                            show sc artschool a281f
                            b"What are you looking at?"
                            show sc artschool a281e
                            mc"Just as I suspected. You also have a stain on the back of your underwear."
                            mc"(There's no stain, but she doesn't know that.)"
                            $ rewards_unlock ("bella",8)
                            show sc artschool a281c
                            mc"And you're right. Your top does look a little tight too."
                            $ v_ep01_task06_help_bella_counter += 1
                            show sc artschool a281d
                            b"What am I going to do?"
                            show sc artschool a281c
                            mc"(I don't suppose I can trick her into taking her underwear off, haha!)"

                "Move on":
                    show sc artschool a280
                    b"What am I going to do?"
            play ambient "sound effects/01/girls_locker_room_talk.ogg" fadein 1.0
            show sc artschool a282
            mc"Well..."
            #The basketball girls enter the changing room making plenty of noise
            #Bella and the MC looks towards the door - sound effect as a door opens
            show sc artschool a283
            b"{i}(*Whispering*){/i}\nOh shit!"
            b"{i}(*Whispering*){/i}\nWhat's that?"
            show sc artschool a284
            mc"{i}(*Whispering*){/i}\nDamn!!"
            mc"{i}(*Whispering*){/i}\nThe girls are done with their practice!"
            #Bella’s face fills with dread
            show sc artschool a286
            mc"{i}(*Whispering*){/i}\nCome with me!"
            #The MC grabs her hand and they hide behind a set of lockers - the MC has a carry bag slung over her shoulder that carries all the items they’ve stolen
            #Bella still has the small top over her and her breasts/cleavage showing
            #The basketball girls stand in between a set of lockers where their school uniforms are laid out on a bench. Meanwhile, the MC and Bella hide behind a set of lockers - https://media.gettyimages.com/id/200482551-001/photo/teenage-girls-in-gym-locker-room.jpg?s=612x612&w=gi&k=20&c=s7bQUPLkAiDWJaA7LA-BQq1Og6qE2bsDl9sx7wcq_CY=
            show sc artschool a287
            girl1"What the hell???"
            stop ambient fadeout 1.0
            show sc artschool a290
            girl1"Who the fuck took my clothes!?"
            #Girl1 eyeballs one of the other girls
            girl1"And why do you look so guilty, Yumi?"
            show sc artschool a291
            girl2"Oh screw you, Davina. Why would I want your clothes?"
            show sc artschool a292
            girl2"Besides, they only fit your fat ass!"
            #Show Bella standing in front of the MC as they hide behind another set of lockers
            show sc artschool a293
            b"(Did she just call that girl fat?)"
            #Bella looks insulted
            show sc artschool a294
            girl1"All right, that’s it. Bring it on bitch!!"
            #The girls get into a catfight and the other girls on the team surround them and taunt/cheer them on - sound effect
            #It allows the MC and Bella to escape
            show sc artschool a295
            mc"{i}(*Whispering*){/i}\nCome on [mc_b_address], this is our chance to escape while all the girls are distracted."
            show sc artschool a296
            b"{i}(*Whispering*){/i}\nBut what about this top that I’m wearing?"
            b"{i}(*Whispering*){/i}\nIf we have to run, there's no way it will hold them in!"
            #Show Bella’s obscene cleavage up close
            show sc artschool a297
            mc"Hmm..."
            mc"(I'll have to take her word for it.)"
            #The basketball coach leaves his office to see who is fighting
            #The MC sees inside the coach’s room door - https://media.compliancesigns.com/media/catalog/product/a/u/authorized-personnel-only-sign-nhe-25053_1000.gif
            #He sees a jacket hanging over his seat inside the office
            show sc artschool a296
            mc"{i}(*Whispering*){/i}\nI have an idea."
            mc"{i}(*Whispering*){/i}\nCome with me."
            show sc artschool a298
            with dissolve
            b"{i}(*Whispering*){/i}\nSo what's the plan?"
            show sc artschool a298c
            b"{i}(*Whispering*){/i}\nWhat are you going to do?"
            show sc artschool a298a
            mc"{i}(*Whispering*){/i}\nThe plan?"
            mc"{i}(*Whispering*){/i}\nOh, right! The plan."
            show sc artschool a298b
            mc"{i}(*Whispering*){/i}\nJust wait."
            show sc artschool a298d
            mc"{i}(*Whispering*){/i}\nAll right, he's walking away. Stay right here."
            mc"{i}(*Whispering*){/i}\nI'll be right back."
            show sc artschool a299a
            with dissolve
            mc"(Let me see here.)"
            show sc artschool a299b
            mc"(Ah...)"
            show sc artschool a299c
            mc"(Jackpot!)"
            stop music fadeout 1.0
            scene black
            with dissolve
            scene black
            with Pause (2)

            #the scene returns and we see the same two girls fighting in the locker room
            play ambient "sound effects/01/girls_locker_room_fight.ogg" fadein 1.0
            show sc artschool a300
            with dissolve
            girl1"I’m gonna kill you!"
            #The MC and Bella sneak behind the girls and exit the locker room - Bella is wearing the coach’s oversized jacket around her
            show sc artschool a301
            girl2"Not if I kill you first!"
            #The basketball coach enters the room and gets between the girls
            show sc artschool a302
            coach"(Ah shit...)"
            stop ambient fadeout 1.0
            #the coach grabs both girls by their earlobes
            show sc artschool a303
            with hpunch
            coach"Off to Dean Pritchard’s office with you both!"
            coach"And the rest of you get changed and go home!"
            #The coach rolls his eyes
            show sc artschool a304
            coach"(Goddamit... I can’t believe that this has happened again!)"
            scene black
            with dissolve
            scene black
            with Pause (2)

            #show cross-fade
            #show the MC and Bella walking out the front of the college. MC has a carry bag over his shoulder with the things they stole
            play ambient "sound effects/01/street_sound_day_ambience.ogg" loop fadein 1.0
            play music "sound effects/01/Walking on Sunshine1.mp3" loop fadein 1.0
            show sc artschool a305
            mc"Don’t draw any attention to yourself. Just keep walking."
            #We see Bella still wearing the coach’s jacket
            show sc artschool a306
            b"I’m not complaining, but, this jacket is way too big."
            show sc artschool a307
            mc"That sounds like complaining."
            show sc artschool a308
            mc"Hey, it was the best I could find on short notice."
            #They’re away from the college now
            show sc artschool a368b
            with dissolve
            pause 1.5
            show sc artschool a309
            with dissolve
            mc"So I guess that makes up for the paint thinner issue, right?"
            show sc artschool a310
            b"Not on your life."
            show sc artschool a311
            with dissolve
            b"I know what you were doing."
            show sc artschool a312
            b"However, I do appreciate the quick thinking and getting us out of there unscathed."
            #Bella and the MC continue to walk away from the college
            show sc artschool a313
            mc"You’re welcome..."
            stop ambient fadeout 1.0
            #screen goes blank
            scene black
            with dissolve
            scene black
            with Pause (2)

    #- - - - stop sound fadeout 1.0- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

    #scene continues

    if v_ep01_mc_task_visit_options_3 == "":
        #"Add these lines if the player hasn’t helped Vivian and/or Ariel do their tasks yet"
        #Bella smiles as they reach a street corner near home
        play music "sound effects/01/Walking on Sunshine1.mp3" loop fadein 1.0
        play ambient "sound effects/01/street_sound_day_ambience.ogg" loop fadein 1.0
        if v_ep01_task06_help_bella_artclass:
            show sc artschool a314b
            with dissolve
            mc"So, I’m going to head into town as I have some things I gotta do."
            show sc artschool a365c
            b"That’s cool, I can walk home from here."
            show sc artschool a324a
            mc"All right, I'm heading in the opposite direction when we get to the end of this street."
            mc"I’ll be back a little later on."
            show sc artschool a323a
            with dissolve
            mc"How long do you think it will take you to make a forgery of that painting?"
            show sc artschool a321a
            b"I’m not sure. Hopefully, no more than a week."
            show sc artschool a322a
            b"Thanks again for helping me today."
            show sc artschool a325a
            b"It wasn’t perfect, but I guess things can’t always go to plan, right?"
            show sc artschool a323a
            mc"They certainly don’t if you’re me."
            if v_ep01_task06_help_bella_counter == 5:
                $ task_completed(6,"aa")
                $ v_ep01_bella_aa_tasks_counter += 1
            if v_ep01_task06_help_bella_counter == 4:
                $ task_completed(6,"a")
            if v_ep01_task06_help_bella_counter == 3:
                $ task_completed(6,"b")
            if v_ep01_task06_help_bella_counter == 2:
                $ task_completed(6,"c")
            if v_ep01_task06_help_bella_counter <= 1:
                $ task_completed(6,"d")
            #Bella smirks
            show sc artschool a324a
            mc"You know, [mc_vic_address] will be pretty impressed with you."
            show sc artschool a325a
            b"And you too."
            b"Anyway, I'm this way. See you later, [y_name]."
            #Bella walks away from him and the MC watches her
            show sc artschool a324a
            mc"(Hmm... She doesn’t seem too pissed at me.)"
            #The MC smiles
            mc"(As long as she’s going home happy, then I’ve done my job...)"
            stop music fadeout 1.0
            stop ambient fadeout 1.0
            #screen goes blank
            scene black
            with dissolve
            scene black
            with Pause (2)
        else:
            show sc artschool a314
            with dissolve
            mc"So, I’m going to head into town as I have some things I gotta do."
            show sc artschool a368a
            b"That’s cool, I can walk home from here."
            show sc artschool a316
            mc"You might want this bag."
            #The MC hands Bella the carry bag
            show sc artschool a317a
            with dissolve
            b"Thanks."
            show sc artschool a324
            mc"All right, I'm heading in the opposite direction when we get to the end of this street."
            mc"I’ll be back a little later on."
            show sc artschool a323
            with dissolve
            mc"How long do you think it will take you to make a forgery of that painting?"
            show sc artschool a321
            b"I’m not sure. Hopefully, no more than a week."
            show sc artschool a322
            b"Thanks again for helping me today."
            show sc artschool a325
            b"It wasn’t perfect, but I guess things can’t always go to plan, right?"
            show sc artschool a323
            mc"They certainly don’t if you’re me."
            if v_ep01_task06_help_bella_counter == 5:
                $ task_completed(6,"aa")
                $ v_ep01_bella_aa_tasks_counter += 1
            if v_ep01_task06_help_bella_counter == 4:
                $ task_completed(6,"a")
            if v_ep01_task06_help_bella_counter == 3:
                $ task_completed(6,"b")
            if v_ep01_task06_help_bella_counter == 2:
                $ task_completed(6,"c")
            if v_ep01_task06_help_bella_counter <= 1:
                $ task_completed(6,"d")
            #Bella smirks
            show sc artschool a324
            mc"You know, [mc_vic_address] will be pretty impressed with you."
            show sc artschool a325
            b"And you too."
            b"Anyway, I'm this way. See you later, [y_name]."
            #Bella walks away from him and the MC watches her
            show sc artschool a324
            mc"(Hmm... She doesn’t seem too pissed at me.)"
            #The MC smiles
            mc"(As long as she’s going home happy, then I’ve done my job...)"
            stop music fadeout 1.0
            stop ambient fadeout 1.0
            #screen goes blank
            scene black
            with dissolve
            scene black
            with Pause (2)

        if v_ep01_mc_task_visit_options_2 == "":
            jump lb_ep01_The_MC_meets_Zora
        else:
            jump lb_ep01_MC_gets_a_call_from_Megan1
        #END SCENE


    else:
        #"Add these lines if the player has already helped Vivian and/or Ariel do their tasks"
        #show the MC and Bella walking side by side on the
        if v_ep01_task06_help_bella_artclass:
            play music "sound effects/01/Walking on Sunshine1.mp3" loop fadein 1.0
            play ambient "sound effects/01/street_sound_day_ambience.ogg" loop fadein 1.0
            show sc artschool a365c
            with dissolve
            b"So I guess I should thank you for helping me today, [y_name]."
            b"It wasn’t perfect, but I guess things can’t always go to plan, right?"
            show sc artschool a314b
            mc"They certainly don’t if you’re me."
            if v_ep01_task06_help_bella_counter == 5:
                $ task_completed(6,"aa")
                $ v_ep01_bella_aa_tasks_counter += 1
            if v_ep01_task06_help_bella_counter == 4:
                $ task_completed(6,"a")
            if v_ep01_task06_help_bella_counter == 3:
                $ task_completed(6,"b")
            if v_ep01_task06_help_bella_counter == 2:
                $ task_completed(6,"c")
            if v_ep01_task06_help_bella_counter <= 1:
                $ task_completed(6,"d")
            #Bella smirks
            show sc artschool a324a
            with dissolve
            mc"So how long do you think it will take you to make a forgery of that painting?"
            show sc artschool a321a
            b"I’m not sure. Hopefully, no more than a week."
            show sc artschool a323a
            mc"You know, [mc_vic_address] will be pretty impressed with you."
            show sc artschool a322a
            b"And you too."
            show sc artschool a324a
            mc"(Hmm... She doesn’t seem too pissed at me.)"
            #The MC smiles
            mc"(As long as she’s going home happy, then I’ve done my job...)"
            #screen goes blank
            #final shot here of the MC and Bella walking side by side on the sidewalk in the suburbs heading home
            #screen goes blank
            stop ambient fadeout 1.0
            stop music fadeout 1.0
            scene black
            with dissolve
            scene black
            with Pause (2)
        else:
            play ambient "sound effects/01/street_sound_day_ambience.ogg" loop fadein 1.0
            show sc artschool a315
            with dissolve
            b"So I guess I should thank you for helping me today, [y_name]."
            b"It wasn’t perfect, but I guess things can’t always go to plan, right?"
            show sc artschool a318
            mc"They certainly don’t if you’re me."
            if v_ep01_task06_help_bella_counter == 5:
                $ task_completed(6,"aa")
                $ v_ep01_bella_aa_tasks_counter += 1
            if v_ep01_task06_help_bella_counter == 4:
                $ task_completed(6,"a")
            if v_ep01_task06_help_bella_counter == 3:
                $ task_completed(6,"b")
            if v_ep01_task06_help_bella_counter == 2:
                $ task_completed(6,"c")
            if v_ep01_task06_help_bella_counter <= 1:
                $ task_completed(6,"d")
            #Bella smirks
            show sc artschool a368a
            with dissolve
            mc"So how long do you think it will take you to make a forgery of that painting?"
            show sc artschool a320
            b"I’m not sure. Hopefully, no more than a week."
            show sc artschool a318
            mc"You know, [mc_vic_address] will be pretty impressed with you."
            show sc artschool a321
            b"And you too."
            show sc artschool a324
            mc"(Hmm... She doesn’t seem too pissed at me.)"
            #The MC smiles
            mc"(As long as she’s going home happy, then I’ve done my job...)"
            #screen goes blank
            #final shot here of the MC and Bella walking side by side on the sidewalk in the suburbs heading home
            #screen goes blank
            stop ambient fadeout 1.0
            stop music fadeout 1.0
            scene black
            with dissolve
            scene black
            with Pause (2)

        jump lb_ep01_The_MC_sees_Vivian_in_the_bathroom

    #END SCENE

    #If the player has already done the tasks with Vivian and Ariel, then the story will continue on with:
    #Scene 13-01 - The MC sees Vivian in the shower"