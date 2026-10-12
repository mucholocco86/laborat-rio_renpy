init:
    $ v_ep01_09_01_Mikayla_Sex_path = False
    $ v_ep01_09_01_Tasha_Sex_path = False
    $ v_ep01_09_01_Tasha_and_Mikayla_Sex_path = False
    $ v_ep01_09_01_Mik_points = 0
    $ v_ep01_09_01_Tasha_points = 0



label lb_ep01_The_MC_and_Harry_at_the_club:
    pause 1.0
    centered "Several hours later...{w=2.0}{nw}" with dissolve
    show text "Several hours later..." #THESE LINES ARE NOT DUPLICATES. Needed to fade the text in and out!
    scene bg black with Dissolve(1)
    pause 1.0
    #this appears on the screen
    #scene starts with the MC and Harry arriving at the nightclub
    play music "sound effects/01/party_music#1.ogg" loop fadein 1.0
    play ambient "sound effects/01/people_talking_at_party1.ogg" loop fadein 1.0
    scene sc harrybar b001
    with dissolve
    ha"I don’t know how you convinced me to come here but I am sooo glad that you did!"
    show sc harrybar b005
    ha"This place is awesome!"
    show sc harrybar b003
    ha"Look at these women, dude!!"
    show sc harrybar b004
    ha"Who’d have thought a club with a name like 'Eager Beaver' would draw in plentiful pussy?"
    show sc harrybar b007
    mc"(Hehe... He’s like a kid in a candy store!)"
    mc"(Hopefully, he’ll be distracted long enough for me to find the owner of the tattoo parlour.)"
    show sc harrybar b008
    mc"How about you go and find us a table, order the first of the three rounds you owe me, while I go and use the restroom?"
    #Harry doesn’t even look at the MC when he replies
    show sc harrybar b009
    mc"Sure thing, dude..."
    #the MC leaves Harry’s side while he continues ogling the women in the club
    show sc harrybar b011
    mc"(That Travis guy said his boss would be here. But he gave me no clue what he looks like.)"
    #The MC looks around and sees a guy sitting at a booth with tattoos all over his face and head
    #- https://www.thesun.co.uk/wp-content/uploads/2022/10/pix-sun-features-xd-pictured-769497366.jpg
    mc"(Hmm... I’m guessing it’s probably that guy.)"
    # or mc"(Hmm... I’m guessing that's him over there.)" 
    #show a close-up of his face and arms
    show sc harrybar b012
    mc"(Geez... Have enough tattoos there, buddy?)"
    #The MC approaches the tattoo guy
    show sc harrybar b014
    mc"Excuse me? I was just admiring the uh... work you’ve had done."
    show sc harrybar b015
    guy"Oh really?"
    show sc harrybar b016
    guy"And what exactly is it that you admire so much?"
    #He says nonchalantly. Expressionless
    show sc harrybar b017
    mc"The fact that you have pretty much covered everywhere..."
    show sc harrybar b016
    mc"That is, I presume you have."
    mc"What do they all mean?"
    show sc harrybar b019
    guy"You’re not here to talk about tattoos. Certainly not mine."
    show sc harrybar b020
    guy"So why don’t you cut to the chase and tell me what you want, kid?"
    show sc harrybar b016
    mc"Word on the street is that you're the guy to see about specific tattoo designs."
    show sc harrybar b022
    mc"Is there any chance you can tell me about this one in particular?"
    #The MC shows him the image he drew
    show sc harrybar b023
    guy"All right, who sent you??"
    #The guy stands up and confronts the MC
    show sc harrybar b024
    mc"Nobody sent me. No one specifically."
    menu:
        "Be cocky"(wt="Funnier option"):
            show sc harrybar b025
            mc"I saw this tattoo and thought it would look good on one of my butt cheeks."
            show sc harrybar b026
            guy"Are you trying to be a smart ass?"
        "Be honest":
            show sc harrybar b025
            mc"I'd just like some more information about it is all."
            show sc harrybar b026
            guy"Don't play dumb with me. I can smell bullshit a mile away."
    #The guy grabs the MC by the throat
    show sc harrybar b027
    with vpunch
    guy"You walked into the wrong club tonight."
    mc"(Uh-oh... Maybe I overstepped the line this time.)"
    show sc harrybar b028
    with dissolve
    pause 1.5
    show sc harrybar b278
    with dissolve
    pause 2.0

    #The guy looks over the MC’s shoulder and sees a cop at the bar. He gives him this look
    #- https://static.wikia.nocookie.net/bttf/images/6/6c/Back-to-the-Future-back-to-the-future-8228558-640-480.jpg/revision/latest?cb=20110619071611

    #The Guy looks over the MC’s shoulder and notices a heavy set nightclub security guy watching what’s going on and he backs off
    #- https://miro.medium.com/v2/resize:fit:1200/1*up3UgWzG0BPflDodSnYx1A.png

    #Other Patrons in the club also watch on as this is happening
    show sc harrybar b029
    with dissolve
    guy"However, I’m going to cut you a break."
    show sc harrybar b030
    guy"Otherwise, I’d be sticking one of my needles in a very uncomfortable place."
    #The guy lets the MC go
    show sc harrybar b031
    guy"Now get the hell out of here."
    #The MC turns and walks away from the table
    show sc harrybar b032
    mc"(Shit... That was stupid of me.)"
    show sc harrybar b034
    mc"(What am I going to do now?)"
    mc"(I’ll go and find Harry and then see if I can come up with another plan.)"
    mc"(Or I could just get completely shit-faced drunk? Whatever happens first...)"
    scene black
    with dissolve
    scene black
    with Pause (2)
    #He finds Harry sitting in a booth. He’s Harry is chatting up a hot girl"
    show sc harrybar b038
    with dissolve
    mc"(What the hell?)"
    #Girl #1 is a tall blonde, with big breasts with an award-winning smile.
    #Harry sees the MC
    show sc harrybar b039
    ha"[y_name]!"
    show sc harrybar b036
    ha"This is the guy I was telling you about."
    #the MC greets the blonde who looks like her - https://www.instagram.com/mikaylademaiter/
    show sc harrybar b040
    ha"[y_name], this is Mikayla."
    mc"Hi there."
    show sc harrybar b042
    mik"Hello, tall and handsome."
    show sc harrybar b043
    ha"Isn’t she the greatest?"
    show sc harrybar b045
    mc"Uh, yeah..."
    #show a close-up of her cleavage
    show sc harrybar b046
    ha"Mikayla lived in my apartment building for a little while before she moved away from town."
    mc"So you two kind of know each other already then?"
    show sc harrybar b048
    mik"I suppose so."
    show sc harrybar b049
    mik"Harry was always shy whenever I tried to talk to him."
    show sc harrybar b050
    mik"Not so much tonight though. He came straight up to me!"
    mc"(Sounds like Harry is making up for some lost time.)"
    #Mikayla looks beyond the MC
    show sc harrybar b046
    ha"Mikayla was just telling me that she and her girlfriend are flight attendants, and they’re here for the night."
    mc"Sorry, did you say girlfriend?"
    show sc harrybar b040
    ha"Yeah."
    show sc harrybar b039
    ha"You’re going to love her too, buddy."
    #Harry looks beyond the MC
    show sc harrybar b046
    ha"Speak of the devil. Here she is now."
    #the MC turns around and sees Girl #2 and she is also a stunner. She’s a brunette, with a slender figure, great legs and ass
    show sc harrybar b054
    with fast_dissolve
    mc"(Holy shit...)"
    if not persistent.v_sex_anim_enabled_locked and persistent.v_sex_anim_enabled:
        scene sc harrybar b057 at tt_top
        pause
    elif True:
        scene sc harrybar b054
    mc"(Her friend is stunning as well!)"
    #Rolling Screen of Girl #2
    scene sc harrybar b058
    tash"Hi there."
    show sc harrybar b059
    tash"Mikayla! Why didn’t you come back to our table?"
    show sc harrybar b060
    tash"I was worried that you’d gone home with a guy already!"
    show sc harrybar b061
    mik"Sorry, I ran into an old acquaintance of mine, Harry."
    show sc harrybar b062
    mik"That’s his friend, [y_name]."
    show sc harrybar b064
    mc"It’s a pleasure to meet you."
    tash"You too."
    #Tasha kisses him on the cheek
    play sound "sound effects/01/mwah_short_kissing_sound_effect3.mp3"
    show sc harrybar b065
    tash"Mwah!"
    #And then the other
    stop sound fadeout 1.0
    play sound2 "sound effects/01/mwah_short_kissing_sound_effect5.mp3"
    show sc harrybar b066
    tash"Mwah!"
    stop sound2 fadeout 1.0
    mc"Um... Thanks?"
    show sc harrybar b068
    mik"Don’t mind her. She’s part-European."
    mik"And fluent in several languages. French, German and Italian to name a few."
    show sc harrybar b054
    mc"European, eh?"
    mc"(I've picked up the odd phrase.)"
    mc"(I should say something clever.)"
    menu:
        "Speak French":
            show sc harrybar b054
            mc"Revenons à nos moutons. Ils ont besoin de nous!\n{i}Translation: Let's go back to our sheep. They need us!{/i}"
            show sc harrybar b060
            tash"Haha!"
            show sc harrybar b059
            tash"I like this guy."
            mc"(What's so funny?)"
            mc"(Did I say it right?)"

        "Speak German":
            show sc harrybar b054
            mc"Alles hat ein Ende, nur die Wurst hat zwei.\n{i}Translation: Everything has an end, only the sausage has two.{/i}"
            show sc harrybar b064
            tash"..."
            show sc harrybar b059
            mc"(Hmm... Maybe she's not that fluent in German.)"
            mc"(That or my German really needs work.)"

        "Speak Italian":
            show sc harrybar b054
            mc"Il porcospino ha molti cazzi.\n{i}Translation: The porcupine has a lot of pricks.{/i}"
            show sc harrybar b064
            tash"Fascinating..."
            show sc harrybar b059
            mc"(I knew she'd be impressed.)"

    show sc harrybar b070
    mik"Come, have a seat."
    show sc harrybar b071
    ha"I’ll get the waiter’s attention and order us all some drinks..."
    #They all sit down, order some drinks and introduce themselves.
    #screen goes blank
    stop music fadeout 1.0
    stop ambient fadeout 1.0
    scene black
    with dissolve
    scene black
    with Pause (2)



    #NOTE: Position the MC between Mikayla and Tasha
    #https://previews.123rf.com/images/pressmaster/pressmaster1201/pressmaster120100702/12324222-image-of-two-happy-couples-interacting-in-night-club.jpg
    #Dance music plays - Tasha and the MC talk up close due to the sound in the club
    play music "sound effects/01/party_music#2.ogg" loop fadein 1.0
    play ambient "sound effects/01/people_talking_at_party2.ogg" loop fadein 1.0
    show sc harrybar b072
    with dissolve
    mc"So Harry said that you and Mikayla are both flight attendants, yes?"
    show sc harrybar b077b
    tash"That's correct."
    #Tasha takes a sip of her cocktail
    show sc harrybar b076
    mc"Wow, that’s pretty cool."
    show sc harrybar b088
    mc"What kind of flights do you usually travel on?"
    show sc harrybar b089
    tash"We both mainly do domestic flights across the country but we’re hoping to move into international flights real soon."
    show sc harrybar b077
    mc"That’s awesome!"
    show sc harrybar b079
    mc"And you get cheaper travel to anywhere you want to go, right?"
    show sc harrybar b093
    tash"Yeah, it’s one of many amazing perks of doing this job."
    show sc harrybar b080
    mik"So Harry tells me that you both work at a local gym?"
    mc"That’s right."
    show sc harrybar b082
    mik"I could tell. You must work out a lot, huh?"
    #Mikayla runs a hand across the MC’s bicep’
    mc"When I’m not having to clean up after Harry, sure!"
    show sc harrybar b084
    mik"I really need to get to the gym. It’s been so long that I struggle to take off my heels and undress after I come home after a long day."
    show sc harrybar b085
    ha"Well, if you happen to have that problem later tonight, I’d be more than happy to assist you."
    show sc harrybar b086
    mik"Haha! Normally if I’m struggling that badly, then I ask for Tasha’s help."
    show sc harrybar b087
    mc"You two live together?"
    show sc harrybar b088
    tash"Oh, yeah..."
    show sc harrybar b089
    tash"We do {i}everything{/i} together..."
    mc"(Harry, you wonderful bastard for knowing Mikayla!)"
    #The Dance music changes
    show sc harrybar b091
    mik"So you both seem like you’re great at smooth-talking..."
    mik"But how are you two with your feet?"
    show sc harrybar b088
    mc"Our feet?"
    show sc harrybar b093
    tash"Yeah... How are you on the dance floor?"
    menu:
        "Saturday Night Fever":
            show sc harrybar b088
            mc"Well, when it comes to dancing, I've been called a modern day {i}Anthony Manero{/i}."
            show sc harrybar b079
            tash"Is that so?"
            show sc harrybar b076
            tash"Well... I can't wait to see that!"
        "Napoleon Dynamite":
            show sc harrybar b088
            mc"Gosh...!"
            mc"I don't mind pairing up with another, however, when I dance solo is where I really shine!"
            show sc harrybar b079
            tash"Is that right?"
            show sc harrybar b076
            tash"Well... We might have to clear the dance floor for you later."
        "Dirty Dancing":
            show sc harrybar b088
            mc"Well, when it comes to dancing, I have this saying..."
            mc"{i}Nobody puts [y_name] in the corner.{/i}"
            play sound "sound effects/01/sexy_female_laugh4.mp3"
            show sc harrybar b089
            tash"Hahaha!"
            stop sound fadeout 1.0
    show sc harrybar b093
    tash"And what about, Harry?"
    show sc harrybar b094
    ha"Yeah, you can count me out!"
    show sc harrybar b095
    ha"Sorry ladies, but the closest I ever came to learning how to dance was waiting outside the toilet and I was busting to take a piss!!"
    show sc harrybar b096
    mc"(Dammit Harry...)"
    show sc harrybar b097
    mik"That’s a shame."
    #Mikayla and Tasha move out of the booth
    show sc harrybar b098
    with dissolve
    tash"If you change your minds, boys, then you know where to find us."
    #Mikayla whispers in the MC’s ear
    show sc harrybar b099
    mik"{i}(*Whispering*){/i}\nYou should tell Harry that nothing gets a girl more wet than a guy who knows how to dance."
    mik"Or at least tries to."
    show sc harrybar b101
    mc"(Oh geez...)"
    #The girls head to the dance floor - we see a behind shot of them holding hands
    show sc harrybar b102
    mc"What the fuck is wrong with you, dude??"
    #The MC smacks Harry on the shoulder
    show sc harrybar b095
    ha"What?"
    show sc harrybar b103
    mc"What was with that busting to take a piss, line?"
    show sc harrybar b106
    ha"It’s true. I can’t dance for shit!"
    show sc harrybar b105
    mc"Neither can I, but that’s not going to stop me from going out there with those two and try"
    show sc harrybar b107
    mc"So you either locate your cock and balls and get your shit together, or this guy is gonna go home with \"two\" flight attendants tonight."
    show sc harrybar b104
    ha"Ughh.... Fine."
    show sc harrybar b109
    ha"But I call dibs on Mikayla!"
    show sc harrybar b111
    mc"Huh?"
    show sc harrybar b112
    mc"Why?"
    show sc harrybar b115
    ha"Dude... I’ve had the biggest hard-on for her ever since the day she moved into my apartment block."
    show sc harrybar b109
    ha"When she left, I was kicking myself for not approaching her."
    show sc harrybar b114
    ha"But now I get a second chance!"
    show sc harrybar b116
    mc"You do realise that she doesn’t live here anymore, right?"
    show sc harrybar b117
    ha"I know... But I don’t care about that. I just want to bed her. That’s all."
    show sc harrybar b114
    mc"Oh, well, then I say go for it, Casanova!"
    show sc harrybar b120
    mc"Let’s do this..."
    #The guys leave the booth and head to the dance floor
    stop music fadeout 1.0
    stop ambient fadeout 1.0
    #screen goes blank
    scene black
    with dissolve
    scene black
    with Pause (2)

    #the scene returns with Harry and the MC approaching the dance floor
    # We see them in the background and the girls dance together in the foreground within the same renders
    play music "sound effects/01/party_music#3.ogg" loop fadein 1.0
    play ambient "sound effects/01/people_talking_at_party3.ogg" loop fadein 1.0
    show sc harrybar b121
    with dissolve
    pause 2.0
    show sc harrybar b122
    with dissolve
    mik"Well look who finally decided to show up."
    show sc harrybar b123
    tash"We were starting to wonder if you two had gone home to your mommies."
    show sc harrybar b124a
    ha"Never!!"
    show sc harrybar b125
    mc"Ready, Harry?"
    show sc harrybar b128
    ha"Uh, sure."
    #The MC moves ahead while Harry looks to the ceiling and puts his hands together as if he’s praying
    show sc harrybar b127
    ha"(Please get me through this, lords of the dance!)"
    #The MC moves towards Mikayla while Harry dances with Tasha
    show sc harrybar b135
    mc"May I have this dance?"
    show sc harrybar b128
    ha"(Oh... That’s a bad start.)"
    show sc harrybar b137
    ha"(I was hoping to dance with Mikayla.)"
    show sc harrybar b129
    ha"(But maybe [y_name] is putting in a good word for me.)"
    show sc harrybar b130
    ha"(Yeah, I’m sure that’s what he’s going to do.)"
    show sc harrybar b135
    mik"Sure..."
    show sc harrybar b136
    mik"Just a word of warning though. I was the under-18 state champion for dancing."
    #She has a serious face
    show sc harrybar b135
    mik"So no pressure."
    show sc harrybar b137
    mc"Are you going to say that with a straight face... to a guy who was voted in high school as the most likely to set the place on fire with his dancing shoes?"
    #The MC has this face when he says this line above - https://pixhost.to/show/821/445207376_screenshot-2024-02-11-at-11-06-19-am.jpg
    play sound "sound effects/01/sexy_female_laugh3.mp3"
    show sc harrybar b138
    mik"Hahaha!"
    stop sound fadeout 1.0
    show sc harrybar b139
    mik"Well then... Let’s set this place alight, shall we?"
    show sc harrybar b131
    tash"Are you sure you want to dance with me, Harry?"
    show sc harrybar b133
    ha"Yeah, I’m all in!"
    #Harry takes her in his arms
    show sc harrybar b134
    tash"Woah!"
    #Show the MC with Mikayla before they start dancing

    #MC takes Mikayla in his arms
    #(Montage scene)

    #One render moves into another in this order
    show sc harrybar b140
    with dissolve
    pause 2.0
    show sc harrybar b141
    with dissolve
    pause 2.0
    show sc harrybar b142
    with dissolve
    pause 2.0
    #Show both couples dancing with their partners in different poses
    #- https://as1.ftcdn.net/v2/jpg/01/58/53/18/1000_F_158531850_6mPd332ZzikoN4g4BbTWDa0Srl4Vkkgg.jpg

    #Show both couples in a different pose - https://cdn2.vectorstock.com/i/1000x1000/29/36/dancing-couples-vector-1392936.jpg

    #Show the MC and Mikayla in a sexy pose - https://i.pinimg.com/564x/16/97/65/16976538a3634e78a58803be084b60ca.jpg
    show sc harrybar b143
    with dissolve
    mik"Not bad..."
    show sc harrybar b144
    mik"If only your high school chums could see you now, huh?"
    show sc harrybar b145
    mik"I’m sure they’d be jealous."
    show sc harrybar b146
    mc"And not just because of my dancing ability."
    #show the MC considering kissing her - https://www.shutterstock.com/image-photo/fashion-photo-sexy-elegant-couple-600nw-246673573.jpg
    show sc harrybar b147
    pause 1.0
    #Mikayla smiles and then turns away, playing hard to get
    show sc harrybar b145
    with dissolve
    mik"Let's stick to dancing, Romeo."
    show sc harrybar b146
    mc"As you wish."
    show sc harrybar b149
    with dissolve
    pause 2.0
    show sc harrybar b150
    with dissolve
    pause 2.0
    show sc harrybar b151
    with dissolve
    pause 2.0
    #Show the MC and Mikayla in another sexy pose - https://i.etsystatic.com/10331312/c/998/792/0/282/il/fc0b33/3102759387/il_340x270.3102759387_tw70.jpg
    #Show Harry and Tasha - https://i.pinimg.com/236x/ce/e0/46/cee046948a970d19e37dd6c9787c19a9.jpg
    #Show Harry and Tasha in another position - https://thumbs.dreamstime.com/z/couple-dancing-tango-10973413.jpg
    show sc harrybar b152
    with dissolve
    mc"(Goddamn, Harry! Where did you pull that move from?)"
    show sc harrybar b151
    mc"(Sure you can't dance for shit! Liar...)"
    stop music fadeout 1.0
    stop ambient fadeout 1.0
    scene black
    with dissolve
    scene black
    with Pause (2)


    play music "sound effects/01/party_music#7.ogg" loop fadein 1.0
    play ambient "sound effects/01/people_talking_at_party5.ogg" loop fadein 1.0
    #The music changes
    show sc harrybar b139
    with dissolve
    mik"Thanks so much for the dance."
    mik"I’m going to partner up with Harry now."
    mik"Would you mind looking after my friend?"
    show sc harrybar b154
    mc"I'd be more than happy to."
    #MIkayla walks over to Harry while Tasha comes over to the MC and takes his hands preparing to dance
    show sc harrybar b155
    tash"So, do you want to lead?"
    show sc harrybar b156
    mc"You read my mind..."
    #MC takes Tasha in his arms
    #(Montage scene)
    show sc harrybar b157
    with dissolve
    pause 2.0
    show sc harrybar b165
    with dissolve
    pause 2.0
    show sc harrybar b158
    with dissolve
    pause 2.0
    #Show the MC and Tasha - https://www.shutterstock.com/image-photo/young-sexy-couple-dances-caribbean-260nw-1188125251.jpg
    #Show this next pose for them - https://as1.ftcdn.net/v2/jpg/02/24/31/30/1000_F_224313023_wYEjPR3lOTJ7caOAvpLHdCLJ22ZV6iFs.jpg
    show sc harrybar b159
    with dissolve
    mc"(Holy crap!!)"
    show sc harrybar b161
    mc"(Both of these girls sure know how to move.)"
    show sc harrybar b162
    mc"(If we get to go home with them, then I’ll have a tough decision to make.)"
    show sc harrybar b163
    mc"(And Harry will no doubt have his say on this as well.)"
    show sc harrybar b164
    with dissolve
    mc"(He has his sights set on Mikayla, but I’d be lying if I said I wasn't attracted to her too...)"
    #Show Harry and Mikayla - https://as1.ftcdn.net/v2/jpg/02/08/75/78/1000_F_208757889_oR9wxpkYfWVILd9n8ogf5Bo0bOKf1Npf.jpg
    #Show the MC and Tasha - https://as1.ftcdn.net/v2/jpg/01/08/71/72/1000_F_108717207_h4ZvqNR5Vi1PtxUpQGJnSu5j0K6lBZKi.jpg
    #Show both couples dancing with their partners in different poses - https://static1.bigstockphoto.com/0/1/2/large1500/210340126.jpg
    show sc harrybar b165
    with dissolve
    pause 2.0
    show sc harrybar b166
    with dissolve
    pause 2.0
    stop music fadeout 1.0
    stop ambient fadeout 1.0
    #screen goes blank"
    scene black
    with dissolve
    scene black
    with Pause (2)

    #The girls, Harry and the MC are back at the booth
    #Harry chats with Mikayla while the MC talks with Tasha
    play music "sound effects/01/party_music#4.ogg" loop fadein 1.0
    play ambient "sound effects/01/people_talking_at_party4.ogg" loop fadein 1.0
    show sc harrybar b167
    with dissolve
    tash"Not bad, [y_name]."
    show sc harrybar b168
    tash"Mikayla and I didn’t see this coming from you. And certainly not Harry!"
    show sc harrybar b169
    mc"What can I say..."
    show sc harrybar b170
    mc"When we see objects of great beauty... We must have them."
    show sc harrybar b172
    mc"Even if it means taking great risk."
    #Tasha smiles
    show sc harrybar b173
    tash"You certainly seem the type to take great risks."
    show sc harrybar b174
    mc"I’ve been known to do so when the occasion calls for it."
    show sc harrybar b173
    tash"So what about your dreams and desires?"
    tash"What do you want out of life?"
    show sc harrybar b189
    mc"Wow, what a question..."
    show sc harrybar b176
    mc"I guess at this stage of my life, I’m more focused on the present rather than the future."
    show sc harrybar b171
    mc"But if you really want to know, I’d love to run my own gym one day."
    show sc harrybar b177
    tash"So what’s stopping you?"
    show sc harrybar b178
    mc"A lot of things... Money for one."
    show sc harrybar b179
    mc"And then I don’t know the first thing about running my own business."
    show sc harrybar b177
    tash"You never went to college?"
    show sc harrybar b181
    mc"I’m afraid not."
    show sc harrybar b182
    tash"How come?"
    menu:
        "Make something up":
            mc"(Even though we only just met, I don't want to tell her anything about what we really do when I'm not at the gym.)"
            show sc harrybar b184
            mc"Tried it, wasn't for me. I had shall we say, other priorities."
            show sc harrybar b185
            tash"Fair enough."
        "Tell her the real reason":
            show sc harrybar b184
            mc"Let’s just say that putting my [public_group] first has always been the main priority for me."
            show sc harrybar b185
            tash"That’s understandable."
    show sc harrybar b195
    with dissolve
    tash"So, do you live with anyone?"
    show sc harrybar b174
    mc"Yeah, I have an older [b_mc_rel] and a younger [a_mc_rel] as well."
    show sc harrybar b178
    mc"And we all live with a couple of other people."
    show sc harrybar b184
    tash"It sounds like you’re all pretty close."
    show sc harrybar b181
    mc"Yes and no."
    show sc harrybar b178
    mc"We're just as dysfunctional as anybody else."
    show sc harrybar b182
    tash"I know that feeling."
    show sc harrybar b177
    tash"But at some point, you may have to leave them behind to go after what you really want in life."
    show sc harrybar b174
    mc"Is that what you and Mikayla have done?"
    show sc harrybar b188
    tash"In a matter of speaking, yes."
    show sc harrybar b190
    tash"We meet new people every day and we’re not restricted by anything or anyone."
    mc"Hmm..."
    show sc harrybar b191
    mc"(She sure is interested in my personal life.)"
    show sc harrybar b200
    mc"(Which is kind of nice as I don’t normally open up to anyone, especially people who I've only just met.)"
    show sc harrybar b202
    mc"Another drink?"
    show sc harrybar b194
    tash"That’d be great, thanks..."
    stop music fadeout 1.0
    stop ambient fadeout 1.0
    #screen goes blank
    scene black
    with dissolve
    scene black
    with Pause (2)


    #The girls, Harry and the MC are back still in the booth
    #The MC now chats with Mikayla while Harry talks with Tasha
    #IMPORTANT - make sure Mikayla and Tasha are sitting next to each other in the booth
    #The MC - Mikayla - Tasha - Harry
    play music "sound effects/01/party_music#5.ogg" loop fadein 1.0
    play ambient "sound effects/01/people_talking_at_party5.ogg" loop fadein 1.0
    show sc harrybar b204
    with dissolve
    mc"So Harry was saying that you’re only here for the night, yes?"
    show sc harrybar b205
    mik"That’s right. We fly back out tomorrow morning."
    show sc harrybar b206
    mik"But we’re here every now and then."
    show sc harrybar b207
    mik"How do you find living here?"
    show sc harrybar b211
    mc"It has its moments. Not always good."
    show sc harrybar b209
    mik"Yeah, I heard about the recent crime spree."
    show sc harrybar b210
    mc"Uh, yeah..."
    show sc harrybar b211
    mc"Ever since the global financial crisis, people have been finding all kinds of ways to survive, you know?"
    show sc harrybar b213
    mik"True... The same thing is happening in my hometown."
    mik"And the scary thing about that is, just about anybody could be a thief."
    show sc harrybar b214
    mc"Yeah, you’re right."
    show sc harrybar b215
    mik"So... You and Tasha looked like you were getting on pretty famously?"
    show sc harrybar b216
    mc"You think?"
    show sc harrybar b217
    mik"It sure seemed that way."
    show sc harrybar b218
    mc"Do you think I should get her number?"
    show sc harrybar b219
    mik"Yeah, about that..."
    show sc harrybar b220
    mik"She and I don’t {b}do{/b} serious relationships."
    show sc harrybar b221
    mik"We move around a lot so we both know that we wouldn’t be able to fully commit to any guy or girl."
    mc"(Did she say guy or girl??)"
    show sc harrybar b222
    mik"But that doesn’t stop us from having nights out like this and having something more casual, you know?"
    show sc harrybar b223
    mc"Yeah, I read ya."
    show sc harrybar b224
    mc"But what if I’m not interested in Tasha?"
    show sc harrybar b225
    mik"Is that you signalling your intentions, [y_name]?"
    show sc harrybar b226
    mik"That’s very forward of you."
    show sc harrybar b227
    mik"But a word of warning. I’m pretty sure that Harry has already made his decision."
    show sc harrybar b228
    mc"Really?"
    show sc harrybar b229
    mik"Yeah, but nothing is ever set in stone with me."
    show sc harrybar b230
    mik"So how come you and your friend are both single?"
    menu:
        "I'm not sure":
            show sc harrybar b231
            mc"I don’t know..."
            show sc harrybar b232
            mc"I guess that Harry and I don’t want to be tied down. That’s the furthest thing from our minds."
            show sc harrybar b233
            mc"But personally speaking, I haven’t met the right girl."
            show sc harrybar b226
            mc"And I’m okay with that."
            show sc harrybar b235
            mc"When the time comes, I hope that I end up with someone who I’m compatible with."
        "I'm a player":
            show sc harrybar b231
            mc"Well, if I'm being honest..."
            show sc harrybar b232
            mc"I like to play the field. To explore my options."
            show sc harrybar b222
            mik"So what if you meet the right girl, someone that completely blows your mind?"
            show sc harrybar b221
            mik"What would you do then?"
            show sc harrybar b219
            mik"Would you continue to play the field?"
            show sc harrybar b234
            mc"Trust me. I haven't met anyone like that, yet."
    show sc harrybar b236
    mik"And how do you know I’m not that person? Or even Tasha?"
    show sc harrybar b237
    mc"It’s a little early to tell don’t you think?"
    show sc harrybar b238
    mc"I mean, we don’t know each other that well."
    show sc harrybar b239
    mik"I suppose you're right."
    show sc harrybar b240
    mik"But why don’t we put that to the test?"
    #Mikayla takes out her phone
    show sc harrybar b241
    mc"What are you doing?"
    #She looks at her phone, typing on it
    show sc harrybar b242
    mik"One second..."
    mik"Ah, here it is."
    show sc harrybar b244
    mik"It’s an app where you can take a compatibility test."
    show sc harrybar b245
    mik"It tells you what kind of girlfriend or even lover you’re going to end up with."
    show sc harrybar b250
    mc"Seriously?"
    show sc harrybar b251
    mc"All that stuff seems like a load of nonsense."
    show sc harrybar b246
    mik"Possibly... But it could be a lot of fun too."
    show sc harrybar b248
    mik"You and Harry came here to enjoy yourselves, right?"
    show sc harrybar b250
    mc"Yeah, we did."
    show sc harrybar b251
    mc"All right, fine. I’ll take your test. What do I need to do?"
    #Mikayla leans over and puts her arm around him
    show sc harrybar b252
    mik"You only have to answer a few questions and then it will give you a short answer at the end depending on your responses."
    #She hands him her phone."
    show sc harrybar b253
    mc"Hmm..."
    show sc harrybar b254
    mc"(This is silly, but as she said, it’s just some harmless fun.)"

    #NOTE- Place the phone screen in the middle of the render, and the options for each question will come up
    #- https://pixhost.to/show/821/445209128_phone-screen-render.png
    #The player has to simply select the option that they prefer which will determine which girl the MC goes home with.

    #Screen Notification for the player here

    #This is a game of skill and maybe even some luck. Choose the answers to each question that suit you best and shortly after the test is finished, you will get some options to choose from."

    #QUESTION 1
    mc"What kind of movies do you like to watch?"

    #Answer options:
    show sc harrybar b254a
    #[Drama / Comedy]
    menu (screen="scr_ep01_09_01_quiz_choice"):
        "Drama"(wt="+1 Tasha Point"): #1+ TASHA
            $ v_ep01_09_01_Tasha_points += 1
            show sc harrybar b254
            mc"(I do like a good drama. Especially the one about the guy who liked running.)"
            mc"(This answer is more me.)"

        "Comedy"(wt="+1 Mikayla Point"): #1+ MIKAYLA
            $ v_ep01_09_01_Mik_points += 1
            show sc harrybar b254
            mc"(Comedy for sure!)"
            mc"(I mean, who doesn't like seeing someone cop a snowball to the face from close range?)"

    #QUESTION 2
    show sc harrybar b254
    mc"Which of these two would you prefer your perfect girl to have?"
    show sc harrybar b254b
    #Answer options:

    #[Great intelligence / A great sense of humour]
    menu (screen="scr_ep01_09_01_quiz_choice_small"):
        "Great intelligence"(wt="+1 Tasha Point"): #1+ TASHA
            $ v_ep01_09_01_Tasha_points += 1
            show sc harrybar b254
            mc"(A girl with a brain every day of the week.)"
            mc"(Smart, but not too smart.)"

        "A great sense of humour"(wt="+1 Mikayla Point"): #1+ MIKAYLA
            $ v_ep01_09_01_Mik_points += 1
            show sc harrybar b254
            mc"(A girl with a a great sense of humour every day of the week.)"
            mc"(And one who can dish it out as well as taking it.)"

    #QUESTION 3
    show sc harrybar b254
    mc"Where are you likely to take your girl on a first date?"
    #Answer options:
    show sc harrybar b254c
    #[Nightclub / Restaurant]
    menu (screen="scr_ep01_09_01_quiz_choice"):
        "Nightclub"(wt="+1 Mikayla Point"): #1+ MIKAYLA
            $ v_ep01_09_01_Mik_points += 1
            show sc harrybar b254
            mc"(Deep down I'm a party animal!)"
            mc"(So a nightclub it is.)"

        "Restaurant"(wt="+1 Tasha Point"): #1+ TASHA
            $ v_ep01_09_01_Tasha_points += 1
            show sc harrybar b254
            mc"(Dinner for two at a restaurant for sure.)"
            mc"(Fine dining all the way!)"


    #QUESTION 4
    show sc harrybar b254
    mc"You take your girl to a live event. Which of these are you taking her to?"
    show sc harrybar b254d
    #Answer options:

    #[A rock concert / The ballet]
    menu (screen="scr_ep01_09_01_quiz_choice"):
        "A rock concert"(wt="+1 Mikayla Point"): #1+ MIKAYLA
            $ v_ep01_09_01_Mik_points += 1
            show sc harrybar b254
            mc"(Nothing beats being in the middle of a moshpit, jumping up and down and headbanging along to my favourite bands!)"

        "The ballet"(wt="+1 Tasha Point"): #1+ TASHA
            $ v_ep01_09_01_Tasha_points += 1
            show sc harrybar b254
            mc"(Hmm... The ballet is the one with bear in the little car, isn't it?)"


    #QUESTION 5
    show sc harrybar b254
    mc"What do you see when you look at your lover’s smile?"

    #Answer options:
    show sc harrybar b254e
    #[Kinkiness / Desire]
    menu (screen="scr_ep01_09_01_quiz_choice"):
        "Kinkiness"(wt="+1 Mikayla Point"): #1+ MIKAYLA
            $ v_ep01_09_01_Mik_points += 1
            show sc harrybar b254
            mc"(I love girls who are a little more on the kinky side.)"
            mc"(I wonder if I'll get to see that later tonight from either of these two.)"

        "Desire"(wt="+1 Tasha Point"): #1+ TASHA
            $ v_ep01_09_01_Tasha_points += 1
            show sc harrybar b254
            mc"(A girl with desire in their eyes and in their smile are always a good time.)"
            mc"(I wonder if I'll get to see that later tonight from either of these two.)"


    #QUESTION 6
    show sc harrybar b254
    mc"What is your idea of the perfect wedding?"
    show sc harrybar b254
    mc"A big wedding with all of your friends and family present, or would you elope so it’s just the two of you?"
    show sc harrybar b254f
    #Answer options:

    #[Big wedding / Elope]
    menu (screen="scr_ep01_09_01_quiz_choice"):
        "Big wedding"(wt="+1 Tasha Point"): #1+ TASHA
            $ v_ep01_09_01_Tasha_points += 1
            show sc harrybar b254
            mc"(Big wedding. All my friends, some family and plenty of booze!)"

        "Elope"(wt="+1 Mikayla Point"): #1+ MIKAYLA
            $ v_ep01_09_01_Mik_points += 1
            show sc harrybar b254
            mc"(There's something about disappearing with that one special person to get married which intrigues me.)"
            mc"(Not that getting married is high on my agenda right now.)"

    #- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    stop music fadeout 1.0
    stop ambient fadeout 1.0
    scene black
    with dissolve
    scene black
    with Pause (2)
    if v_ep01_09_01_Tasha_points > v_ep01_09_01_Mik_points:
        #"This response by the player if they got three or more TASHA POINTS"
        #The MC reads out what is on the screen
        play music "sound effects/01/party_music#6.ogg" loop fadein 1.0
        play ambient "sound effects/01/people_talking_at_party6.ogg" loop fadein 1.0
        show sc harrybar b263
        with dissolve
        mc"All done."
        show sc harrybar b264
        mik"So... How did you do?"
        show sc harrybar b265
        mc"It said something like... even though one girl may seem like the obvious choice, the other girl will be more suited to you."
        #the MC looks at Mikayla
        show sc harrybar b266
        mc"What does that mean?"
        #Mikayla gives a slight smile.
        show sc harrybar b267
        mik"Put simply..."
        show sc harrybar b268
        mik"You’re more suited to being with someone like Tasha."
        show sc harrybar b269
        mc"Really? You can tell that from a simple personality test?"
        show sc harrybar b270
        mik"Pretty much."
        show sc harrybar b271
        mc"But what if I’m not interested in Tasha?"
        show sc harrybar b272
        mc"What if I’m looking for something or someone a little different."
        mc"Even for just one night."
        show sc harrybar b273
        mik"Then I'm sorry to tell you, but it looks like you've already made up your mind."
        show sc harrybar b276
        mik"So what do you want to do?"
        show sc harrybar b268
        mik"Make a move on my best friend and potentially have a memorable night, or go home and make love to your hand?"

        #NOTE: The Mikayla and Tasha options will automatically come up no matter what.
        #The idea here is the player can still go against the results of the compatibility test if they want to.
        #It will make it easier for them to get these two outcomes.

        #However, if they want the threesome ending, then they have to get exactly THREE of the SIX questions right.
        #If they do that, then the "Choose Both" option will become available to select
        #Even with this third option, the player can still choose Mikayla or Tasha


        #Choose Tasha]
        menu:
            "Choose Tasha"(wt="Sex with Tasha"):
                show sc harrybar b268
                pause 0.1
                $ v_ep01_09_01_Tasha_Sex_path = True
                stop music fadeout 1.0
                stop ambient fadeout 1.0
                scene black
                with dissolve
                scene black
                with Pause (2)
                jump lb_ep01_The_MC_and_Tasha_or_Mikayla_sex_path

    if v_ep01_09_01_Tasha_points < v_ep01_09_01_Mik_points:
        #IMPORTANT - create a variable for the option the player chooses here and keep it open for Scene 11-01

        #If the player chooses "Mikayla", the sex scene with Mikayla will begin in the next document

        #If the player chooses "Tasha", the sex scene with Tasha will begin in the next document

        #screen goes blank"
        #"This response by the player if they got more than three MIKAYLA POINTS"

        play music "sound effects/01/party_music#6.ogg" loop fadein 1.0
        play ambient "sound effects/01/people_talking_at_party6.ogg" loop fadein 1.0
        #The MC reads out what is on the screen"
        show sc harrybar b263
        with dissolve
        mc"All done."
        show sc harrybar b264
        mik"So... How did you do?"
        show sc harrybar b265
        mc"It said something like... even though you may not believe in love at first sight, when you first see her,
        she’s definitely the best option for you on that specific day."
        #the MC looks at Mikayla
        show sc harrybar b266
        mc"What does that mean?"
        #Mikayla happily smiles
        show sc harrybar b267
        mik"Put simply..."
        show sc harrybar b268
        mik"It means that you want to be with someone different to the kind of girl you normally go for."
        mik"Even if it seems wrong."
        show sc harrybar b267
        mik"Maybe someone like me."
        show sc harrybar b269
        mc"Oh..."
        show sc harrybar b265
        mc"What about Harry? You know he has a bit of a crush on you, right?"
        show sc harrybar b273
        mik"I’m well aware."
        show sc harrybar b276
        mik"So what do you want to do?"
        show sc harrybar b277
        mik"Betray your best friend so you can spend the night with me..."
        show sc harrybar b151
        mik"Or resist the temptation so your buddy can have what he’s waited almost a year for?"

        #[Choose Mikayla]
        menu:
            "Choose Mikayla"(wt="Sex with Mikayla"):
                show sc harrybar b151
                pause 0.1
                $ v_ep01_09_01_Mikayla_Sex_path = True
                stop music fadeout 1.0
                stop ambient fadeout 1.0
                scene black
                with dissolve
                scene black
                with Pause (2)
                jump lb_ep01_The_MC_and_Tasha_or_Mikayla_sex_path

    if v_ep01_09_01_Tasha_points == v_ep01_09_01_Mik_points:
        # IMPORTANT - create a variable for the option the player chooses here and keep it open for Scene 11-01

        # If the player chooses "Mikayla", the sex scene with Mikayla will begin in the next document

        # If the player chooses "Tasha", the sex scene with Tasha will begin in the next document

        # NOTE: The Mikayla and Tasha options will automatically come up no matter what.
        # The idea here is the player can still go against the results of the compatibility test if they want to.
        # It will make it easier for them to get these two outcomes.

        # However, if they want the threesome ending, then they have to get exactly THREE of the SIX questions right.
        # If they do that, then the "Choose Both" option will become available to select
        # Even with this third option, the player can still choose Mikayla or Tasha
        # screen goes blank"


        # "This response by the player if they got exactly three TASHA POINTS and three MIKAYLA POINTS"

        play music "sound effects/01/party_music#6.ogg" loop fadein 1.0
        play ambient "sound effects/01/people_talking_at_party6.ogg" loop fadein 1.0
        #The MC reads out what is on the screen
        show sc harrybar b263
        with dissolve
        mc"All done."
        show sc harrybar b264
        mik"So... How did you do?"
        show sc harrybar b265
        mc"It says that I’m open to anything, and if I go with the flow, then the experiences I undergo could be unforgettable."
        #the MC looks at Mikayla
        show sc harrybar b266
        mc"What does that mean?"
        show sc harrybar b267
        mik"It means that you’re at a crossroads. You're still undecided."
        show sc harrybar b268
        mik"On one hand, you’re more suited to being with someone like Tasha."
        show sc harrybar b273
        mik"On the other, it might also mean that you want to be with someone different to the kind of girl you normally go for."
        mik"Even if it seems wrong."
        show sc harrybar b270
        mik"Maybe even someone like me."
        show sc harrybar b271
        mc"So what you’re saying is that I’m at a stalemate?"
        show sc harrybar b270
        mik"Kind of..."
        show sc harrybar b273
        mik"You still have the power to choose, [y_name]."
        show sc harrybar b274
        mik"It’s entirely up to you."
        show sc harrybar b275
        mik"The test is not the final decision maker."
        mik"You are."
        show sc harrybar b277
        mik"So what do you want to do?"
        mik"Go with what some test is suggesting, or simply say, screw the damn test!"
        show sc harrybar b275
        mik"And maybe you’d like to try something that you probably never have before."
        #Mikayla gives a cheeky smile

        #[Choose Mikayla / Choose Tasha]
        menu:
            "Choose Mikayla"(wt="Sex with Mikayla"):
                show sc harrybar b275
                pause 0.1
                $ v_ep01_09_01_Mikayla_Sex_path = True
                stop music fadeout 1.0
                stop ambient fadeout 1.0
                scene black
                with dissolve
                scene black
                with Pause (2)
                jump lb_ep01_The_MC_and_Tasha_or_Mikayla_sex_path

            "Choose both"(wt="Sex with Mikayla and Tasha"):
                show sc harrybar b275
                pause 0.1
                $ v_ep01_09_01_Tasha_and_Mikayla_Sex_path = True
                stop music fadeout 1.0
                stop ambient fadeout 1.0
                scene black
                with dissolve
                scene black
                with Pause (2)
                jump lb_ep01_The_MC_and_Tasha_or_Mikayla_sex_path

            "Choose Tasha"(wt="Sex with Tasha"):
                show sc harrybar b275
                pause 0.1
                $ v_ep01_09_01_Tasha_Sex_path = True
                stop music fadeout 1.0
                stop ambient fadeout 1.0
                scene black
                with dissolve
                scene black
                with Pause (2)
                jump lb_ep01_The_MC_and_Tasha_or_Mikayla_sex_path
        stop music fadeout 1.0
        stop ambient fadeout 1.0
        scene black
        with dissolve
        scene black
        with Pause (2)
        jump lb_ep01_The_MC_and_Tasha_or_Mikayla_sex_path

    # IMPORTANT - create a variable for the option the player chooses here and keep it open for Scene 11-01

    # If the player chooses "Mikayla", the sex scene with Mikayla will begin in the next document

    # If the player chooses "Choose both", the "Threesome" sex scene with both girls will begin in the next document

    # If the player chooses "Tasha", the sex scene with Tasha will begin in the next document

    # NOTE: If the players want the threesome ending, then they have to get exactly THREE of the SIX questions right.
    # If they do that, then the "Choose Both" option will become available to select
    # Even with this third option, the player can still choose Mikayla or Tasha

    # screen goes blank"

