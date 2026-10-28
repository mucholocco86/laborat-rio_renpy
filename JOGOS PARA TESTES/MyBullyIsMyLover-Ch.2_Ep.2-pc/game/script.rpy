style default:
    outlines [ (absolute(2), "#000", absolute(1), absolute(1)) ]

default lilyhelp = False
#default skyroute = False
default ainecomfort = False
default lilytutor = False
default aineheadpat = False
default skycelebrate = False


label start:
    jump tutorial
label ep1:
    stop music fadeout 2
    $ name = renpy.input("What is your name?(Default: Kei)")
    $ name = name.strip()
    if name == "":
        $ name = "Kei"
    $ persistent.name = name
    pause
    play music 'audio/riftstable.mp3' fadein 2 volume 0.5
    scene pro_1
    with Dissolve(3.0)
    mc "The story is kind of ridiculous, to be honest. Are you sure about it?"
    un "Yes~!"
    mc "It will take time, you know?"
    un "Time is a trivial thing. I shall hark e'en if it takes years~"
    mc "Jesus, what's with the way you talk?"
    mc "Well, alright. Let's start with how I met them."
    mc "But, let me tell you about myself and this photo first."
    stop music fadeout 3
    scene pro
    with Dissolve(3.0)
    pause
    scene ep1p1s
    with dissolve
    $ renpy.pause()
    scene i1
    with dissolve
    show screen showpoints
    play music 'audio/Typhoon.mp3'
    mc "My name is [mc], 23 years old."
    scene i2
    with dissolve
    mc "I can proudly say that I'm quite a decent guy."
    mc "Good brain with a nice body build... I mean, what more could I ask for?"
    mc "Maybe money?"
    mc "Well, I'd be lying to myself if I told you that I don't need it. We all need it to survive in this world."
    mc "Money makes the world go round. But, we need to work for it."
    mc "However, it was not that easy with the state of society back then."
    mc "To tell you the truth, I even graduated college with honors, but I haven't had any luck finding a decent job."
    mc "Even someone who graduated with honors like me is getting rejected in the corporate world."
    mc "So... I decided to temporarily find something I could do to get by, until I could find a job within my field of study."
    mc "I mean... what else could I have done? At least the pay covered my daily expenses and needs."
    mc "And what's more, the more work experience you have, the easier it is for you to be accepted in much bigger jobs."
    scene i3
    with dissolve
    mc "Also, I'm extremely thankful to this girl.."
    mc "Her name is Sky."
    mc "She is my close childhood friend."
    mc "She's a very lovely girl who always took care of me and the entire house."
    mc "She is working as an online English tutor for foreign kids."
    mc "But despite it being stressful, I could still see that she loves her job."
    mc "We are close to each other, probably too close, hehee..."
    mc "We've helped and supported each other however we could with our struggles in life."
    mc "Don't let her height fool you — believe me when I say that she's just a year younger than me. Hahaha..."
    mc "She's really cute, isn't she?"
    scene i4
    with dissolve
    mc "And this is Klara."
    mc "She is my guardian."
    mc "She was working abroad for two years at that time, and left the house to me and Sky."
    mc "When did she come back?"
    mc "I can't precisely tell you, but it took her some time."
    scene i2
    with dissolve
    mc "Everything was going fine at that moment..."
    mc "...or so I thought..."
    stop music fadeout 2
    scene i49
    with dissolve
    mc "Because the girl who bullied me in high school..."
    mc "...showed up at the most unexpected time."
    scene title2
    with dissolve
    $ renpy.pause()
    play music 'audio/Ocean.mp3'
    scene black
    with dissolve
    s "Pssst! Wake uuuup!"
    s "Wake up~!"
    scene i5
    with dissolve
    mc "Hmmmm?"
    s "Hey, wake up or you're going to be late!"
    scene i6
    with dissolve
    mc "Hmmm... Sky? What time is it?"
    s "It's already 6 am!"
    mc "Ohh... don't worry, I still have a lot of time..."
    mc "......"
    scene i7
    with dissolve
    mc "Hmm?"
    mc "Wait, w-what the heck are you doing, Sky?"
    s "Huh? What do you mean?"
    scene i8
    with dissolve
    mc "I can literally see your panties right now!"
    s "Oh? What does it matter? You see them all the time, don't you?"
    mc "Well, yes! But you're in my bed right now and..."
    scene i9
    with dissolve
    mc "I can see your..."
    s "See my what?"
    yt "This girl..."
    yt "Ever since we both reached adulthood, we've noticed changes in our bodies, and we also noticed one more thing..."
    yt "I know it is totally wrong, so I've been holding back and telling myself that it is wrong... "
    yt "But... I'm sexually attracted to my childhood friend. And I know that she's attracted to me too."
    yt "Damn it! I should find an excuse to get out of this situation!"
    mc "N-nothing! I'll go ahead and get ready now or I will be late for work!"
    s "Didn't you say that you still have a lot of time?"
    mc "Ahhh! Nevermind!"

    scene black
    with dissolve
    with fade

    scene i10
    with dissolve
    play sound 'audio/doorknock.mp3'
    "*knocks*"
    mc "Hey, Sky! I'm going now!"
    s "Alright! Take care! And don't forget to bring me home some burgers!"
    mc "Sure!"
    yt "She sure likes burgers a lot. I'm wondering why she doesn't get fat, the way she eats."
    yt "Anyway, let's just get going..."
    stop music fadeout 2

    scene black
    with dissolve
    with fade

    play music 'audio/BlackCat.mp3' fadein 2
    scene i11
    with dissolve
    $ renpy.pause()
    scene i12
    with dissolve
    l "Good morning, [mc]! You're always on time, as I expect from you."
    mc "Good morning, Lily!"
    yt "This is Lily. She's my co-worker here at the burger shack."
    yt "But unlike me, she's still finishing her college degree."
    yt "She works full time during the day and is taking just a couple of courses at night, so she doesn't exhaust herself."
    yt "Pretty smart thinking I'd say."
    yt "I really admire her diligence. But at the same time, I feel sorry for her."
    yt "She told me that she lost both her parents in a car accident a few years ago and now lives on her own."
    l "Come on, [mc]. Customers will start swarming this place soon."
    mc "Yeah, sorry. I'll just change into my uniform."

    scene black
    with dissolve
    with fadeq

    "A few hours later..."

    scene black
    with dissolve
    with fadeq

    play sound 'audio/busyrestaurant.mp3' loop fadein 2
    scene i13
    with dissolve
    mc "Here's your double cheeseburger and medium soda for take out. Please enjoy!"
    cu "Thanks!"
    scene i14
    with dissolve
    ass "I told you that I literally found a cockroach inside my burger, you bitch! What are you gonna do about it?!"
    scene i16
    with dissolve
    l "Uhm. ahh... I'm really sorry sir. I..."
    l "It's very unlikely for that to happen sir... I mean..."
    ass "What kind of customer service does this place have?! The employees and the food here are like shit!"
    ass "What is the owner even thinking of hiring people like you?! You useless piece of shit!"
    scene i15
    with dissolve
    yt "Then just don't eat here, you asshole!"
    yt "This kind of customer isn't actually new here. This sort of thing happens pretty often."
    yt "But I'm already used to it after all the time I've spent working here."
    yt "Lily though... has only been working here for two weeks."
    yt "Now, what do I do?"
    menu:
        "Help her":
            $ lilyhelp = True
            scene i18
            with dissolve
            mc "Good morning, sir. My name is [mc]. Can I ask what seems to be the problem?"
            ass "Well, I just told this bitch that I found a cockroach in my burger!"
            ass "Do you know how disgusting that shit is, huh?!"
            yt "Let me guess...  This asshole probably just wants to trick us into giving him food without paying a single penny."
            yt "Well, let's see."
            mc "I apologize that you had to experience such a horrible thing, sir."
            mc "However, can I please request that you show us the burger with the cockroach in it as you have said?"
            ass "I... threw it in the trash can of course!"
            yt "*chuckles* I knew it."
            mc "It is not my duty and we are forbidden to open the garbage bins during work hours to maintain the hygiene of the place."
            mc "However, I am willing to risk my job and check the garbage bin you threw it in."
            mc "If we can prove your experience, then we will be happy to compensate you however we can."
            mc "However... If such a thing never happened, we have the right to ban you from entering this place again for rudeness and interrupting business."
            mc "As you can see, a lot of people are waiting to get their food."
            mc "So you're not just inconveniencing us but the people who are waiting in line as well."
            mc "Furthermore, we have the highest food hygiene rating out of all the burger shacks in the entire town."
            mc "We're doing quality and hygiene checks every opening and closing of the place."
            mc "So I can confidently say that it is extremely unlikely for your experience to happen."
            mc "But, I am not saying that you are wrong, thus I'll go ahead and check that bin."
            mc "Can you please tell me which bin you threw your food in?"
            ass "Uh... Eh... Uhm... Nevermind! I'll never come to this shitty place! I'm going to make sure to leave a bad review of this place!"
            scene i19
            with dissolve
            yt "Well... That took care of it."
            $ lilypoint += 1
            $ renpy.notify(lilynotif)
            mc "Next please!"
            scene i20
            with dissolve
            l "Uhm... Thanks for helping me, [mc]. I really appreciate it."
            mc "Don't worry, I'm here to help you, but we have to develop your customer service skills next time, alright?"
            scene i21
            with dissolve
            l "Haha! Alright, you're the boss."
        "Let her deal with it":
            $ lilyhelp = False
            yt "I should just let her deal with it. She needs to learn how to handle customers like this on her own if she's going to work here."

    scene black
    with dissolve
    with fade

    scene i22
    with dissolve
    mc "Go ahead and take your lunch now, Lily. I'll take care of the customers."
    l "Got it. Thanks, [mc]!"
    scene i23
    with dissolve
    c "Hey there!"
    yt "Oh... This is miss Charlotte. She's our regular customer here."
    mc "Good morning, ma'am. How may I serve you today?"
    c "Can I have three double cheeseburgers and two extra large sodas please?"
    yt "A lot of food as usual, huh?"
    mc "Sure, coming right up!"

    scene black
    with dissolve
    with fadeq

    scene i24
    with dissolve
    mc "Here's your order, ma'am."
    c "Thank you!"
    scene i25
    with dissolve
    mc "Uhm... I apologize if it's rude of me, but do you usually eat these all by yourself?"
    c "I used to, but now, I share it with someone else."
    mc "Oh, I see."
    mc "Please enjoy it, then."
    c "We will! Thanks again."
    scene i26
    with dissolve
    yt "Is it just me? Or did her personality somehow change? She used to be kind of rude if I remember it correctly."
    yt "Strange..."
    stop sound fadeout 2
    stop music fadeout 2

    scene black
    with dissolve
    with fadeq

    "After your shift..."

    scene black
    with dissolve
    with fadeq

    play music 'audio/Boogie.mp3' fadein 2
    if lilyhelp:
        scene i27
        with dissolve
        yt "Alright, got the burgers for Sky. I should probably go home now."
        l "Hold on, [mc]!"
        scene i28
        with dissolve
        mc "Hm? Lily? Do you need something?"
        scene i29
        "*kisses*"
        scene i30
        with dissolve
        mc "Uh... w-what was that for?"
        l "For helping me earlier, of course!"
        scene i31
        with dissolve
        mc "Oh... uuhh... It's nothing. Hahaa..."
        scene i32
        with dissolve
        mc "But like I said, we need to do something about your skills so you can handle that kind of customer next time."
        mc "Maybe we can talk about it when we both have free time."
        mc "Before we start our shift, maybe?"
        l "Sure! I'm up for it."
        l "Are you going home now?"
        mc "Yeah... And you?"
        l "I still have two courses to sit through in a couple hours, so I'll be going home late tonight."
        mc "Then, you should hurry now, or you'll be late."
        l "Don't worry, the academy is just a short walk from here."
        mc "Alright then, I'll see you tomorrow?"
        l "It's Saturday tomorrow, [mc]. It's our day off~!"
        mc "Oh, right. I forgot!"
        mc "See you on Sunday, then."
        l "Of course! See you, [mc]!"
    else:
        scene i27
        with dissolve
        yt "Alright, got the burgers for Sky. I should probably go home now."

    scene black
    with dissolve
    with fade

    scene i33
    with dissolve
    l "Shina~! Wait for meee~!"
    scene i34
    with dissolve
    sh "Hi, Lily!"
    l "Are we heading to class now?"
    sh "Of course, you silly. Where else would we go?"
    l "Well, you might want to watch something on Netflix before we head to class. We still have an hour and a half."
    sh "Oh, right! Now that you mention it, there's this series I discovered just yesterday, and it's pretty amazing! I'm sure you'll like it."
    l "If it's coming from you, I'm sure I will. Let's try it!"

    scene black
    with dissolve
    with fade

    scene i35
    with dissolve
    yt "*sigh*..."
    yt "Why the hell did it have to rain all of a sudden? Now I'm drenched."
    yt "I better take a bath right away or I'll catch a cold for sure."

    scene black
    with dissolve
    with fadeq

    scene i36
    with dissolve
    yt "Alright, let's give these burgers to Sky."

    scene black
    with dissolve
    with fadeq

    scene i37
    with dissolve
    play sound 'audio/doorknock.mp3'
    "*knocks*"
    mc "Sky? Are you in there?"
    s "Yeah! Just come in!"
    mc "Oh, alright..."

    scene black
    with dissolve
    with fadeq

    play sound 'audio/opendoor.mp3'
    scene i38
    with dissolve
    $ renpy.pause()
    play sound 'audio/closedoor.mp3'
    scene i39
    with dissolve
    mc "W-what the hell, Sky?! Why did you let me in when you're naked?!"
    scene i40
    with dissolve
    s "Why are you reacting like that? You've seen me naked several times before! I'm just changing my clothes!"
    s "In fact, we already-"
    scene i41
    with dissolve
    mc "Shhhh! Don't remind me of that! That was just an accident, right?! An accident!"
    s "Alright, if you say so~"
    scene i42
    with dissolve
    s "Hm?"
    s "Wha... My burgers~!!"
    scene i43
    with dissolve
    s "Hehe~"
    s "Thank you, [mc]. You're the best!"
    scene i44
    "*kisses*"
    image srb:
        "i45.jpg"
        pause 3.0
        "i46.jpg"
        pause .2
        repeat
    show srb
    with dissolve
    mc "Y-you're welcome..."
    yt "Damn it! How can I forget about what happened that time if she keeps doing this?!"
    yt "We both said it was just an accident but..."
    scene i101
    with flash
    $ renpy.pause()
    yt "...I don't really feel like it was."
    show srb
    with dissolve
    s "By the way, [mc]. I got a call from Mom earlier."
    mc "Hm? What did she say? Did something bad happen?"
    s "No, you dummy. It's nothing like that."
    s "She told me that she put the other rooms up for rent and the tenants will move in tomorrow morning."
    mc "Hm? What made her decide to put the rooms up for rent? She didn't have any desire to do that before."
    s "It was a good decision, to be honest. It's such a waste for the rooms to just stand empty accumulating dust."
    s "What's more, she told me that the rent money will go to the two of us, and it will really help us with upkeep and maintenance of the house."
    mc "Do you have any idea who's moving in?"
    s "Hmm... All she told me is that three girls are moving in tomorrow."
    yt "Three girls? Why do I feel uneasy about this?"
    mc "Do you know their names?"
    s "Nope. She didn't give me any further information."
    mc "Oh...  I see. So we should fix up the other rooms, right?"
    s "Yep! You got it! We can do it now, if it's alright with you."
    mc "Yeah, sure. I'm not really very tired yet. It's also Saturday tomorrow so..."
    s "Great! Then, let's get it done."
    stop music fadeout 2

    scene black
    with Dissolve(2.0)
label skypause:
    if _in_replay:
        $ name = persistent.gallery_name
    scene skypause
    with dissolve
    $ renpy.pause()
    $ renpy.end_replay()
    play sound 'audio/gamepause.mp3'
    show title at move_slide
    with flash
    $ renpy.notify(imageunlock)
    $ renpy.pause()

    scene black
    with dissolve
    with fadeq

    "After you finished fixing up the rooms, you and Sky ate dinner and went to bed..."

    scene black
    with dissolve
    with fadeq

    "Saturday morning..."

    scene black
    with dissolve
    with fadeq

    play music 'audio/Damage.mp3'
    scene i47
    with dissolve
    play sound 'audio/doorbell.mp3'
    "*doorbell rings*"
    scene i48
    with dissolve
    yt "That's probably them..."
    yt "Well? Time to meet our housemates, I guess."

    scene black
    with dissolve
    with fadeq

    image bob:
        "i49.jpg"
        pause 3.0
        "i50.jpg"
        pause .2
        repeat
    play sound 'audio/opendoor.mp3'
    show bob
    with dissolve
    a "Good morning!"
    mc "Good morning! Are you guys-"
    yt "Wait... WHAT THE HELL??!!!"
    yt "Pink eyes with long black hair... And this face..."
    yt "Aine??!!!"
    yt "And these two are her friends -- Emma... and Gwen..."
    yt "No wonder I felt uneasy when Sky told me that it's three girls who're moving in!"
    yt "I had the terrible experience of being bullied by this girl back when I was in high school because of my physical appearance."
    yt "I admit that I really looked pretty terrible back then. I was so fat and heavy that with a single step I could make the earth tremble."
    yt "After I graduated high school, I got motivated and hit the gym. I also took a fighting class while I was at it."
    yt "Still, it was not easy..."
    yt "There were several times that I thought I was going to die because of how hard it was for me to workout with that hideous body of mine..."
    yt "...until the thought of quitting that shit entered my mind."
    yt "However, I didn't let it faze me..."
    yt "I pushed through heaven and hell just to change myself."
    yt "After I finally achieved my desired result, I swore to myself that I would one day take revenge for everything Aine did to me."
    yt "I had the greatest revenge plan ever in the entire universe! HAHAHAHAHA!!"
    yt "However, I heard that she has become successful in life while I remain a nobody."
    yt "Considering that, it was hard for me to take my revenge."
    yt "Thus, I realized it would just be a waste of time, so I decided to just abandon my plan and finally move on from it."
    yt "So... Why now?! What the heck she doing here with these two?!"
    a "Hello?"
    yt "Could it be..."
    yt "But... they don't seem to recognize me..."
    yt "Well, I've changed a lot physically — that must be why."
    yt "And Aine... As far as I can remember she wasn't like this back then."
    yt "She used to kick my ass and order me around. But why do I feel like she's a totally different person now?"
    yt "It's not like her to be so nice and even greet somebody, especially a guy like me. What the hell happened to her?"
    a "Hello, mister?"
    yt "Then, l'll just pretend like I don't know them and go with the flow for now."
    mc "Oh, I'm sorry, I spaced out. Are you guys the tenants?"
    a "Yes sir! Miss Klara said that we can move in today."
    mc "Sorry, I forgot to introduce myself. I'm [mc], by the way."
    yt "Oh shit! I already messed up! I'm not supposed to tell them my real name! Fuuuuck~!"
    a "That's alright. Nice to meet you [mc]."
    yt "They don't really remember me at all! What in the world is happening here?!"
    yt "Or they might be pretending that they don't know me. I still need to be careful."
    image bob2:
        "i51.jpg"
        pause 3.0
        "i52.jpg"
        pause .2
        repeat
    show bob2
    with dissolve
    a "By the way, this is Emma."
    e "Hi..."
    yt "Emma... Aine's lackey."
    yt "Never mind Aine, she's the one I really need to be careful with."
    yt "She's the most cunning of the three of them. She might be a girl of a few words, but she's extremely smart."
    yt "She follows whatever Aine tells her to do."
    yt "That includes doing errands, which she's doing without question or any second thoughts."
    yt "She's almost like her servant to be honest."
    image bob3:
        "i53.jpg"
        pause 3.0
        "i54.jpg"
        pause .2
        repeat
    show bob3
    with dissolve
    a "And this is Gwen."
    yt "Gwen... The tag-along."
    yt "I don't really have a problem with her since she didn't really do anything bad to me before, except for that one time..."
    yt "Well... it wasn't really that bad, was it?"
    g "Nice to meet you [mc]."
    g "{i}Hmm... he looks quite familiar. Someone I've met before?{/i}"
    image bob4:
        "i55.jpg"
        pause 3.0
        "i56.jpg"
        pause .2
        repeat
    show bob4
    with dissolve
    a "And my name is Aine."
    yt "And lastly, Aine..."
    yt "*sighs*"
    yt "The most beautiful girl in the whole high school."
    yt "There were a lot of guys trying to date her back then. However, they all failed miserably."
    yt "She turned them all down without any mercy."
    yt "And... yes. I admit that I used to have a crush on her too."
    yt "Of course, as a man of culture, I also confessed to her and got rejected. But the worst thing was that..."
    yt "...I became her errand boy."
    yt "I will never forget that horrible experience!"
    yt "The immature me swore to definitely get a revenge one day. But..."
    yt "It's also my fault why all that happened. Futhermore, I've already abandoned that plan for a while now."
    yt "Plus, I'm an extremely soft-hearted guy..."
    yt "...and seeing the way she is right now..."
    yt "......"
    yt "Arrrggh! Don't be a fucking simp, [mc]! Think with your head, not with the one down under!"
    a "Uhm... You're spacing out again, [mc]. Is something wrong?"
    yt "Should I even let them enter?"
    menu:
        "Let them in":
            jump iwanttofuckingplaythegameandnotbeabitch
        "Close the fucking door":
            jump idontwantthembitchesinfrontofme
label iwanttofuckingplaythegameandnotbeabitch:
    mc "Oops..."
    mc "Well, nice to meet you guys. Please come inside. I'll give you a little tour of the house."

    scene black
    with dissolve
    with fade

    scene i57
    with dissolve
    mc "It isn't that big to be honest, but here's the living room."
    scene i58
    with dissolve
    a "These interiors are really nice! It's small but simple. I like it!"

    scene black
    with dissolve
    with fadeq

    scene i59
    with dissolve
    mc "Here's the kitchen."
    scene i60
    with dissolve
    mc "Sky is the one who's usually in charge here so I don't really touch anything in here."
    scene i61
    with dissolve
    a "Sky?"
    mc "Yes, she's my childhood friend. When Klara went abroad, she left the house in our care."
    mc "Let's go upstairs, so I can introduce her to you."
    g "Sure!"

    scene black
    with dissolve
    with fadeq

    scene i62
    with dissolve
    mc "There are a total of four rooms up here. My room is in the right corner and Sky's room is in the middle."
    mc "The available rooms are the one in front of mine and the one near the stairs."
    mc "You guys can choose wherever you want to stay. But the biggest room is the one near the stairs."
    a "Then that will be our room, right, Emma?"
    e "Hm?... Ah... yes..."
    g "Then, I guess mine will be the one right in front of [mc]'s room."

    scene black
    with dissolve
    with fadeq

    scene i63
    with dissolve
    play sound 'audio/doorknock.mp3'
    "*knocks*"
    mc "Sky, the tenants are here! Come and meet them!"
    s "Oh, really?! Hold on... I'm coming!"
    scene i65
    with dissolve
    play sound 'audio/opendoor.mp3'
    "*door opens*"
    s "Hi~!"
    mc "Everyone this is Sky."
    mc "Sky this is Emma, Aine and Gwen."
    scene i64
    with dissolve
    s "Nice to meet you guys! I hope you enjoy your stay here!"
    a "Nice to meet you too Sky. You look so cute~"
    s "Oh... Hehehe~ Thanks!"
    yt "This is so unlike her... I'm curious what happened to change her so much."
    yt "She used to be a bitch back in high school."
    scene i65
    with dissolve
    s "Okay, I have to get back to work right now, I'm really busy at the moment. I'll just see you guys later!"
    a "Oh, alright~!"
    play sound 'audio/closedoor.mp3'
    image bib:
        "i66.jpg"
        pause 3.0
        "i67.jpg"
        pause .2
        repeat
    show bib
    with dissolve
    mc "Do you guys need any help with your things?"
    a "Thanks, but we can take care of it. There's not much anyway."
    g "Yeah! We're all good. Thanks for the house tour."
    mc "Fair enough. I'll leave you guys for now so you can settle in to your rooms."

    scene black
    with dissolve
    with fade

    scene i68
    with dissolve
    yt "Shit! What do I do now?"
    yt "They don't seem to recognize who I am. But I'm afraid that they're just pretending, especially Aine!"
    yt "I don't want to go through those horrible experiences again!"
    yt "However, I can stand up for myself now. I'm not the same as before..."
    scene i69
    yt "...That's right! She can never oppress me ever again!"
    yt "She will never mistreat this handsome face of mine! HAHAHAHAHAHAHAHA!!!"
    scene i70
    with dissolve
    yt "Oops... I got carried away."
    yt "But... Aine..."
    yt "She's become even more beautiful than when we were in high school."
    yt "Besides that, I'm really curious about what made her personality change."
    yt "Is it life experience?"
    yt "Maybe heartbreak?"
    yt "No, no, no, no! Aine? Heartbroken?"
    yt "*chuckles* I will only believe that if lightning strikes right now."
    play sound 'audio/thunder.mp3'
    "*thunder!!*" with flash
    scene i71
    with dissolve
    yt "OH SHIT!!"
    yt "Do you have a problem with me, huh?!!"
    stop sound
    play sound 'audio/thunder.mp3'
    "*thunder!!*" with flash
    scene i72
    with dissolve
    yt "Alright! I'm sorry! I'm sorry!"
    stop sound
    scene i70
    with dissolve
    yt "But is it really true? Aine being heartbroken?"
    yt "......"
    yt "Well, I guess I can find out more since she's here now."
    yt "Maybe I'll try to get closer to her. We'll see how it goes."
    yt "But I still need to be careful..."
    yt "Especially with Emma. She's a smart girl. She'll probably catch me if I make a single misstep."
    yt "And what's up with Gwen? I heard that she inherited her father's company."
    yt "Why would an owner of a big company live in a place like this?"
    yt "Just because she wants to?"
    yt "Nah... That's ridiculous! That would be so totally unlike her!"
    yt "She's a fancy girl who likes fancy things and places."
    yt "I just don't get it..."
    yt "I really find it all so strange..."
    yt "They were also pretty nice to Sky."
    yt "Sky is the kind of girl that has a strong reaction against bitches."
    yt "I don't know where she picked it up but..."
    yt "...if Sky couldn't detect any malicious aura from them, then..."
    scene i101
    with flash
    $ renpy.pause()
    scene i73
    with hpunch
    yt "Aahhhh! Why do I always remember that every time I think of her?!"
    yt "*sighs* Why did we even do that?"
    stop music fadeout 2

    scene black
    with dissolve

    yt "It happened three months ago during the hottest heat wave of the year."
    yt "Even worse, the AC was broken at the time."

    scene black
    with dissolve
    with fadeq

    play music 'audio/SunsetEyes.mp3'
label skyfirsttime:
    if _in_replay:
        $ name = persistent.gallery_name
    scene i74
    with dissolve
    mc "Ahh... it's so friggin hot!"
    mc "Damn that repairman! Why does he have to be on a vacation at a time like this?!"
    mc "What's even worse is it's night time and the electricity has been out for 3 hours now!"
    mc "This house feels like hell right now!"
    scene i75
    with dissolve
    s "Ohh... Don't be such a baby."
    s "Mr. Scott has been working really hard these past few years, you know?"
    s "It's just heat! Just take your clothes off and you'll be fine!"
    scene i76
    with dissolve
    mc "Sky! Help me! I'm about to die..."
    play sound 'audio/chair.mp3'
    show i77
    s "Stop overreacting, will you?" with hpunch
    mc "Hey, you're just making it worse, you know?"
    scene i78
    with dissolve
    s "Oh, come on! We haven't cuddled like this in forever! Stop whining and just deal with it!"
    mc "Because it's hot!"
    yt "I... I can feel her boobs pressing against my chest!"
    yt "God... they're so soft."
    yt "Her height hasn't really changed much, but her body sure has."
    yt "She's not that scrawny girl I used to chase around the yard anymore..."
    yt "She's grown into this ridiculously cute, seriously attractive woman. And..."
    yt "... she's just in her underwear. One thin layer away from skin-to-skin."
    yt "I... want to..."
    yt "Shit, wait!" with hpunch
    yt "I can't be thinking like this! She's been there for me through everything!"
    yt "No, no, no, no... Snap out of it, [mc]! Don't be a damn perv!"
    scene i79
    with dissolve
    s "{i}Oh no...{/i}"
    s "{i}I can feel him getting hard. He's definitely reacting to me right now.{/i}"
    s "{i}His length is pressing up against me...{/i}"
    s "{i}I know I shouldn't let my thoughts wander, but part of me enjoys moments like this...{/i}"
    s "{i}I always have. It just feels... familiar, and warm.{/i}"
    s "{i}But yeah... it definitely feels different now than it used to.{/i}"
    yt "Shit... I'm getting hard. I should probably move her off me. Now."
    yt "I mean, I could do it, no problem. But I don't wanna upset her."
    yt "We've done this before—a lot, actually. But this is different."
    yt "We're adults now. Our bodies aren't playing innocent anymore."
    yt "It's one thing when you're kids, it's another when your childhood friend looks like this."
    yt "And if Sky... if she shifts again, I don't know if I'll be able to stop myself."
    s "{i}I know I should pull away... but I don't want to. Not yet.{/i}"
    scene i80
    with dissolve
    s "{i}And... [mc]'s scent... it's driving me wild.{/i}"
    s "*sniffs*"
    scene i81
    with dissolve
    s "Oooh~"
    s "{i}I just... can't get enough of it.{/i}"
    yt "Yeah... there it goes..."
    scene i82
    with dissolve
    s "Mnnhh~"
    mc "Sky?!"
    yt "She's grinding against me now! Damn it... I need to stop this before it goes too far!"
    s "{i}Mnnhhh~"
    s "{i}I'm soaking... I can't help it~{/i}"
    mc "Sky, wait—we shouldn't be doing this!"
    show black
    play sound 'audio/zipper.mp3'
    with hpunch
    "*zips*"
    scene i83
    with dissolve
    s "......"
    mc "Sky, hold on! Please, just listen—"
    scene i84
    yt "Shit... why does she have to look at me like that?"
    mc "Sky, this isn't a good idea. We live together, this could really mess things up!"
    scene i85
    with dissolve
    s "Do you really believe that?"
    mc "Of course I do!"
    s "Then why are you looking at me like that?"
    s "You want this. I can feel it—your eyes say it all."
    s "We're both adults. We know what this is. It's not the first time for either of us, is it?"
    mc "I mean, no... it's not. But still—"
    yt "She's not wrong. I've been here before..."
    yt "... but doing this with someone I see every day? Someone who's always been close? That's a different kind of risk."
    yt "And yet... the way she looks at me—it's like my body's already decided."
    s "So what's it gonna be, [mc]?"
    s "Are you going to keep pretending? Or are you going to show me how you really feel?"
    mc "......"
    mc ".........."
    show i86
    with hpunch
    mc "*kisses*"
    scene i87
    with dissolve
    s "Mnnhh~"
    s "{i}[mc]'s scent is overwhelming... I can feel myself dripping~{/i}"
    yt "Am I really going through with this?"
    yt "If I take this any further, there's no turning back."
    yt "But screw it—this moment's ours."
    scene black
    play sound 'audio/chair.mp3'
    with hpunch
    s "Ahh!"
    scene i88
    with dissolve
    "*licks*"
    s "Haaah~ [mc]... That feels incredible~"
    yt "God... she tastes sweet. Like strawberries, almost."
    yt "Every second just pulls me deeper—I don't want it to stop."
    scene i89
    with dissolve
    s "Take me, [mc]. Right here. Right now. I don't care what happens."
    mc "A-are you sure about this?"
    s "Yes. I want all of you."
    yt "Then... I won't hold back anymore."

    scene black
    with dissolve
    with fadeq

    scene i90
    with dissolve
    mc "We're about to cross the line, Sky. There will be no turning back if we go further."
    s "It doesn't matter. We both want this."
    s "Just... do it slowly... It's been so long since my first time."
    yt "Damn! Seeing Sky's face like that makes my mind go blank!"
    mc "Okay, I'm putting it in."
    scene i91
    with dissolve
    s "MMMMHH~!!"
    yt "She's... so tight! I can't believe that this isn't her first time at all!"
    scene i92
    with dissolve
    s "AAHHHH~!!"
    yt "Shit! Even her moan is so erotic!"
    s "Y-you can move now, [mc]."
    mc "Alright."
    show sky1
    with dissolve
    $ renpy.pause()
    s "*moans* Aahh~ hhnng~ mmnnnh~"
    $ renpy.pause()
    s "*moans* Haaahh~! You're so big inside me, [mc]~"
    s "Your dick is reaching up to my womb!"
    pause
    show sky2
    with dissolve
    $ renpy.pause()
    mc "You're too tight! I... I won't last much longer!"
    $ renpy.pause()
    s "T-then let's change positions now. Let me do it."
    pause

    scene black
    with dissolve
    with fadeq

    play sound 'audio/chair.mp3'
    scene i93
    with dissolve
    s "Let's do it this way."
    mc "Alright..."
    scene i94
    with dissolve
    s "M-MMNNHH~!! haaaah~"
    s "You're reaching even deeper inside me!"
    mc "Yeah... it feels so good!"
    s "I'm going to move now."
    show sky3
    with dissolve
    $ renpy.pause()
    s "*moans* Ahhh~ Ahhh~ Ahhh~"
    $ renpy.pause()
    show sky4
    with dissolve
    $ renpy.pause()
    mc "Shit! Don't squeeze me like that!"
    s "I can't help it~ It feels so good~"
    $ renpy.pause()
    show sky5
    with dissolve
    $ renpy.pause()
    s "[mc]~! [mc]~!"
    s "I'm..."
    $ renpy.pause()
    show i95
    with hpunch
    s "CUMMING~!!!!"
    mc "Sky, I'm also about to-"
    s "Do it outside! I'm not... safe today!"
    mc "Let's get off the bed!"
    scene i96
    with dissolve
    mc "Here I come, Sky!"
    scene i97
    with hpunch
    mc "Argh!"
    scene i98
    with dissolve
    $ renpy.pause()
    scene i99
    with dissolve
    $ renpy.pause()
    scene i100
    with dissolve
    $ renpy.pause()
    scene i101
    with dissolve
    s "{i}Haaah~ [mc]'s cum... It's so full of his scent!{/i}"
    $ renpy.end_replay()

    scene black
    with dissolve
    with fade

    scene i102
    with dissolve
    s "[mc]... There's something I need to tell you."
    mc "Hm? What's up?"
    s "Please don't be mad, but..."
    s "This was actually... my first time."
    mc "Wait—what?"
    mc "Then... you lied to me?"
    s "I didn't lie. I just... didn't tell the whole truth. I was scared you'd stop again if you knew."
    s "I know we live together, and this probably makes everything more complicated..."
    s "But I couldn't keep holding back anymore."
    mc "But... I didn't notice anything when I... you know."
    mc "So nothing ever happened with your ex?"
    s "No. Nothing. We never went that far."
    mc "Then... how—"
    s "You remember I did gymnastics all through high school, right?"
    s "Let's just say the stretching took care of that part a long time ago."
    mc "So... I was your first?"
    scene i103
    with dissolve
    s "*blushes* You were. And honestly? I'm glad it was you."
    s "Because I like you, [mc]. Maybe I shouldn't..."
    s "... but I do. I care about you more than I probably should."
    s "And it's not just lust or some spur-of-the-moment thing. It's real. It's... honest."
    s "I know things might never be romantic between us. But still—"
    s "Please..."
    s "Just acknowledge how I feel."
    menu:
        "Accept her feelings":
            $ skyroute = True
            mc "You know what, Sky? I've been trying to fight these feelings too."
            mc "I kept telling myself it was a bad idea... that crossing that line would ruin everything."
            s "R-really?"
            mc "Yeah. I mean, we've been through a lot together."
            mc "I feel the same way."
            s "Thank you, [mc]..."
            s "I'm... really happy to hear that."
            mc "I wonder what Klara would say if she found out about this."
            s "Ehh, probably give us the 'responsible adult' speech. *giggles*"
            s "Let's just keep this our little secret for now."
            mc "Like we have a choice."
            s "Exactly."
            mc "Still, one thing I'm curious about..."
            mc "If this was your first time, how'd you get so good at all that?"
            s "*giggles* Easy. I watch porn every day!"
            mc "Damn... That would explain our monthly internet cap too."
            s "Hey~! We split the bill, remember?"
            mc "Alright, alright... no more complaints from me."
        "Reject her":
            $ skyroute = False
            scene i104
            with dissolve
            mc "I'm sorry, Sky. I do care about you... probably more than I should."
            mc "But we're living under the same roof, and if we let these feelings take over, it could ruin everything."
            mc "And you know Klara would murder me if she found out."
            s "......"
            s "It's okay. I get it."

    mc "Let's just get some sleep."

    scene black
    with dissolve
    with fade

    scene i105
    with dissolve
    yt "After that night, we talked things through and agreed to call it a mistake."
    yt "But we both knew it wasn't."
    yt "One thing led to another... too fast to stop."
    yt "I took Sky's virginity, and we just kept pretending it didn't mean anything."
    yt "*sighs*"
    stop music fadeout 2


    scene black
    with dissolve
    with fadeq

    "Later at lunch time..."

    scene black
    with dissolve
    with fadeq

    play music 'audio/DontShoot.mp3'
    show i106
    with wipeleft
    yt "Hm? Aine? What is she thinking?"
    yt "Am I actually right about her being heartbroken?"
    yt "Did she actually have a boyfriend or what?"
    yt "Should I talk to her?"
    menu:
        "Talk to her":
            $ ainecomfort = True
            $ ainepoint += 1
            $ renpy.notify(ainenotif)
            yt "Thick skin {b}activate{/b}!"
            scene i107
            play sound 'audio/woosh.mp3'
            mc "Hey, Aine. What's up? Why do you look unhappy? Are there issues with the room?"
            scene i108
            with dissolve
            a "[mc]?"
            a "Oh, no! Emma and I actually like the room. It really has enough space for both of us."
            mc "Then why do you look troubled? Is anything wrong?"
            scene i109
            with dissolve
            a "No, it's..."
            a "...Yes there is... but..."
            a "...it's a bit personal, and I don't think we're close enough for me to tell you."
            mc "That's okay. But whatever it is, never let it affect you very much."
            mc "I may not be in a position to tell you this, since I also have my own struggles..."
            mc "...but problems are just obstacles to be overcome. They can be quite challenging sometimes."
            scene i110
            with dissolve
            mc "Still, don't ever lose your happiness just from focusing too much on your problems, alright?"
            a "Mmnh..."
            yt "Wait... did I just give advice to Aine?"
            yt "It was such random advice and it just came out of nowhere!"
            yt "Plus, my hand moved on its own!"
            yt "What the heck did I just do?!"
            scene i108
            with dissolve
            mc "Oh, I'm sorry. I didn't mean to..."
            a "*giggles* It's fine. Don't worry."
            scene i111
            with dissolve
            mc "Then, why don't we go down and eat lunch. I'm sure you'll like Sky's food."
            a "Is it lunch time already?"
            mc "Yeah! It's already 11 am."
            a "Really?! I totally lost track of time!"
            a "Let me just get Emma and Gwen then."
        "Ignore her":
            $ ainecomfort = False
            yt "Nah... But I will tell her that it's lunch time already."
            scene i111
            with dissolve
            mc "Hey, Aine let's go down and eat lunch."
            a "Is it that time already?"
            mc "Yeah! It's already 11am."
            a "Really?! I totally lost track of time!"
            a "Let me just get Emma and Gwen then."
    stop music fadeout 2

    scene black
    with dissolve
    with fade

    play music 'audio/GoodAndBad.mp3'
    scene i112
    with dissolve
    yt "Oh, man... This smells so delicious."
    mc "Hey, Sky!"
    scene i113
    with dissolve
    s "Oh! You're all here! Please come and sit right down. The food's almost done."
    g "I got to say though. You don't really look the part, Sky."
    g "I mean, you look too cute to cook. Haha."
    scene i114
    with dissolve
    s "Hehehe~ You're not the only one who's said that."

    scene black
    with dissolve
    with fade

    scene i115
    with dissolve
    s "So... why did you guys decide to live here?"
    s "Was it because of [mc]?"
    mc "Mmp! *cough* *cough* *cough*"
    yt "Oh, damn! I forgot that Sky knew about my experiences!"
    yt "She probably knows that it's her!"
    scene i116
    with dissolve
    e "*munch* *munch* *munch*"
    a "Huh? What do you mean?"
    s "Well, first of all, he's handsome. Second, he's got a good personality."
    s "You guys might be looking for a boyfriend."
    mc "*cough* *cough*"
    g "Do you need some water?"
    mc "N-no I'm fine. Very fine. All good."
    a "Uhh.. no! We didn't come here for that. And we didn't even know him until just today."
    s "{i}Oh really? How come?{/i}"
    s "*giggles* Relax I'm just kidding!"
    s "What do you guys do for a living though?"
    scene i117
    with dissolve
    a "*sighs* That's actually the reason why we're here."
    a "Gwen and I lost our jobs, and we cannot afford our old apartment anymore."
    yt "Oh...  I see they were living in the same place as usual."
    yt "......"
    yt "Wait... what the fuck?!" with hpunch
    yt "Lost their jobs... did Gwen lose her company too?!"
    scene i118
    with dissolve
    g "Well, we could actually still afford it. But it's better to save what's left of our money until we can find new jobs."
    yt "Are you kidding me right now?"
    yt "No, no, no. That's not you at all, Gwen!"
    yt "......"
    yt "Well... to be honest, it was a long time ago. And people do change."
    yt "However, I just can't imagine them changing at all. Possibly Gwen would."
    yt "Aine really is the main question here."
    s "Then, how about Emma?"
    scene i116
    with dissolve
    e "*munch* *munch* *munch*"
    a "Emma still has her job. You may not believe it, but she's a private investigator."
    yt "......"
    yt "Uh-oh..."
    yt "I feel like my life is on a countdown right now."
    s "Oh, wow! That's amazing! How about you and Gwen?"
    a "I actually worked at Gwen's company. Which, unfortunately, had to close down due to certain circumstances."
    a "It's a long story and Gwen probably doesn't want to talk about it right now."
    g "Yeah, it's not that I don't trust you guys, but events are pretty confidential at the moment. So I'd like to keep it that way for now."
    yt "So, is that the reason why Aine looked so down?"
    s "Don't worry, I understand that kind of thing."
    scene i119
    with dissolve
    a "How about you two? What are you doing for a living?"
    mc "Hm?"
    mc "My job is nothing compared to yours. I'm just working in a burger shack in midtown."
    mc "It's temporary, until I can find a decent job within my own field of study."
    a "Hmm... It's still a job to be proud of. So chin up, [mc]."
    yt "Are you really saying that to me right now?! I'm afraid that this is all just a weird dream, Aine."
    mc "I'm fine with it. I think it's actually better to have some work experience before applying for another job."
    g "That's true! That's a good mindset, [mc]!"
    mc "Thanks!"
    scene i115
    with dissolve
    s "And I'm just working here at home."
    s "I'm an online teacher to foreign kids. It's pretty stressful to be honest. But I'm still enjoying it since I really like this job."
    s "You can say that it is my passion. Hehehe~"
    scene i116
    with dissolve
    a "Really? I also worked as an online teacher for a couple of months before I started working for Gwen!"
    a "I really liked it, but I still had to pursue something within my own field of study like what [mc] said."
    s "I totally agree with you."
    s "Oh, I'm sorry to duck out of our conversation here. I need to go back upstairs to teach some classes at 1pm."
    scene i115
    with dissolve
    mc "I'll wash the dishes, Sky."
    s "Thanks, [mc]. I'll be going right now. I'll see you later!"

    scene black
    with dissolve
    with fade

    scene i120
    with dissolve
    a "Let me help you, [mc]."
    mc "It's alright, I can handle it."
    a "No, I insist. Since we're living here now, we should be helping you guys with at least some of the chores."
    mc "Hm... Alright."
    mc "I'll wash the dishes, why don't you dry them and put them away."
    a "Sure!"

    scene black
    with dissolve
    with fadeq

    scene i121
    with dissolve
    mc "Aine?"
    a "Hm? Yes?"
    mc "Can I ask you something?"
    scene i122
    with dissolve
    a "That will depend on the question."
    yt "What's with that smile?"
    mc "Was losing your job the reason why you look sad earlier?"
    scene i123
    with dissolve
    a "......"
    mc "Uhm... You don't have to answer it if that makes you uncomfortable."
    image akb:
        "i124.jpg"
        pause 3.0
        "i125.jpg"
        pause .2
        repeat
    show akb
    with dissolve
    a "*sighs* Alright, I'll tell you. However, you need to promise me that you won't tell anyone about it, okay? Even Sky."
    mc "Sure, I promise. I'm a man of my word."
    a "......"
    a "My parents..."
    mc "Hm? What about your parents?"
    a "*sighs*...They set me up in an arranged marriage."
    mc "WHAT?!!" with hpunch
    image akb2:
        "i126.jpg"
        pause 3.0
        "i127.jpg"
        pause .2
        repeat
    show akb2
    with dissolve
    a "*whispers* Be quiet!"
    a "*whispers* I trusted you with my secret!"
    show akb
    with dissolve
    a "{i}But... I don't know why I trusted him with it. I actually don't feel that this is the first time that we've met.{/i}"
    a "{i}I felt it when we arrived earlier.{/i}"
    a "{i}Strange...{/i}"
    mc "Oh, I'm sorry, I didn't mean to suddenly shout."
    show akb
    with dissolve
    a "Jeez..."
    mc "But, how come? I mean... Why did they set you up in an arranged marriage?"
    a "That's all I can tell you for now. Sorry."
    mc "That's alright. Thank you for trusting me with your secret though."
    scene i128
    with dissolve
    a "Remember, not a word to anyone, okay?"
    mc "I promised and I'll keep my word."
    stop music fadeout 2

    scene black
    with dissolve
    with fadeq

    "Late that night..."

    scene black
    with dissolve
    with fadeq

    play music 'audio/SlowEvening.mp3'
    scene i129
    with dissolve
    yt "Aine stuck in an arranged marriage, huh?"
    yt "Now I see why she looked so depressed earlier."
    yt "She must be against it for her to look that way."
    yt "But I still wonder about her personality though..."
    yt "An arranged marriage couldn't be the reason she changed, right?"
    scene i130
    with dissolve
    e "Hey there, fatso..."
    show i131
    with hpunch
    yt "God damn! That monotonous voice really sends shivers down my spine!"
    yt "Wait, what did she call me?!"
    scene i132
    with dissolve
    mc "What did you just call me?!"
    e "Stop it, I know it's you."
    mc "So, you knew all along?!"
    e "Yes."
    mc "Then, why are you here?! Are you going to-"
    e "No."
    mc "I haven't even finished my sentence, yet!"
    mc "Then why come and move in here?"
    e "Help."
    mc "......."
    mc "Are you a robot or what?"
    mc "Could you please answer me in a complete sentence? Aine has changed, but you're still the same as before, you psycho woman!"
    image ebb:
        "i133.jpg"
        pause 3.0
        "i134.jpg"
        pause .2
        repeat
    show ebb
    with dissolve
    e "Change? I don't see any problem with the way I am right now."
    mc "There is definitely a problem!"
    e "Aine, changed? You just misunderstood her, fatso."
    mc "Huh?! What do you mean I misunderstood her? With all the things she did to me back then?"
    mc "How could I misunderstand her?"
    e "The Aine that you're seeing right now is the real her."
    e "She didn't change, fatso."
    mc "Could you please stop calling me that already?!"
    e "......"
    mc "Uhh... Could you please show me some emotion?"
    e "Unnecessary."
    mc "Pff... Bummer."
    mc "But... What do you mean, her real personality?"
    e "Just what the words say."
    e "She did all those things to hide her real self away."
    mc "Hide her real self? You're not making any sense, Emma."
    mc "How are bullying me and hurting every guy's feelings relevant to that?"
    e "I'll leave that to you to discover."
    e "But the real Aine is really gentle and kind."
    mc "I wish I could believe that, but..."
    e "You saw it yourself, right?"
    e "At the stairs... and in the kitchen."
    mc "You were spying on me?!"
    e "Kind of..."
    mc "*sighs*"
    yt "I don't want to believe her, but now that I've interacted with Aine without her knowing who I am..."
    yt "...she may actually be right."
    mc "Alright, let's say that I believe you."
    mc "But why does she not even recognize me?"
    e "That's simple."
    e "She already forgot about you."
    e "Not just her, Gwen forgot about you, too."
    e "And you've changed a lot physically."
    mc "After everything that happened?!"
    e "Gwen didn't hurt you back then, did she?"
    mc "Well, no. But something..."
    e "Hm?"
    mc "...Nevermind."
    e "Time flies. As the days and years go by, people forget about things and people change."
    e "You know that, right?"
    e "I know you are not that stupid."
    mc "Did you just sort of praise me?"
    e "I don't have a problem with you. I was just doing what Aine told me to do. I'm her servant after all."
    mc "*chuckles* So I was actually right about you being her servant."
    e "You may not know this, but Aine is from a rich family with a well-known name."
    e "I was appointed by her mother to serve her, as members of my family have done for generations."
    e "My family are loyal servants to Aine's family."
    mc "Jeez, what a bigshot! I never thought of Aine having a family like that!"
    mc "If she has that kind of family, why does she still have to work?"
    e "Aine never liked how her family did things."
    e "She might have lived in a mansion with the power to get anything she wanted, but she was like a prisoner."
    e "She's had no right to decide what she wanted to do with her own life."
    e "Even though she's a daughter of a rich family, she has no say in her own future."
    e "So, when she finished her college degree, she decided to force herself out of that place."
    e "It was painful for her to do so, because she has a sister who is very close to her."
    e "But at that time, she thought she must do it to gain a little freedom."
    e "As her servant, I must be always by her side."
    mc "So she's basically a run-away child, huh?"
    e "Not really."
    e "Her mother agreed to it."
    e "...Somehow."
    e "But even now that she's left that house, and thought she was finally free of her family's shackles, things are still the same."
    mc "And now she is being set up for an arranged marriage..."
    e "That's right. And that's also where you come in."
    mc "What?!"
    mc "What part can I possibly have in her and her family's problems?"
    e "You were part of it since the start."
    e "Furthermore, it wasn't a coincidence that we chose to live here."
    e "I set it all up."
    e "I tracked you down and found where you lived."
    e "I was the one who convinced Klara to put the other rooms in the house up for rent."
    mc "Wait a minute. How did you even know Klara?"
    e "It doesn't matter."
    e "I was also lucky that Gwen's company closed down."
    e "That made it easier for us to move here."
    mc "Your friend just lost her company and you call that lucky?!"
    e "Gwen is my friend, but I only care about Aine's welfare. I only have one purpose in life, and that's to serve her until I die."
    e "And even if Gwen's company hadn't closed down I would still have found a way to come here and ask for your help."
    mc "You're telling me all of this, but I still can't see what 'help' you want from me, Emma."
    e "I know that you liked Aine and I know that you're a good guy..."
    mc "There you go praising me again. It really creeps me out!"
    mc "Yeah... I liked Aine before, but what does that matter?"
    e "I want to save y-"
    e "I want to save Aine and you're going to help me. Even if you turn me down, I will still bug you until you say yes."
    mc "Yeah, yeah... I know you. Just tell me already."
    e "I know this is unfair to you, so I'm going to ask you with all my heart."
    scene i135
    with dissolve
    e "......"
    scene i136
    with dissolve
    e ".........."
    scene i137
    with dissolve
    e "Please, [mc]~"
    yt "Did her voice just..."
    e "Please marry Aine~"
    stop music fadeout 2

    scene black
    with Dissolve(2.0)
label emmapause:
    if _in_replay:
        $ name = persistent.gallery_name
    scene emmapause
    with dissolve
    $ renpy.pause()
    $ renpy.end_replay()
    play sound 'audio/gamepause.mp3'
    show title at move_slide
    with flash
    $ renpy.notify(imageunlock)
    $ renpy.pause()

    scene black
    with dissolve
    with fadeq

    play music 'audio/Meander.mp3'
    image ebb2:
        "i138.jpg"
        pause 3.0
        "i139.jpg"
        pause .2
        repeat
    show ebb2
    with dissolve
    mc "Oh, yeah! Su-"
    mc "Wait..."
    mc "WHAT THE HECK DID YOU JUST SAY?!" with hpunch
    e "I want you to marry Aine."
    mc "Hold on... Do you even know what you're talking about, Emma?"
    mc "Marry Aine?!"
    mc "Me? Marrying the girl who bullied me in high school?! That's the most ridiculous idea I've heard in my entire life, you know that?!"
    mc "Please tell me you're just kidding. Hahahahahaha~!"
    e "No, I'm serious."
    mc "Ha..."
    mc "You're really serious about it?!"
    mc "Why me?! There are a lot of people out there who have a lot more potential to be her husband! I'm just a nobody, Emma!"
    mc "I'm just a plain dude working in a burger shack, trying to get by in his daily life!"
    mc "If I ever agree to that ridiculous idea and disregard everything she did before, what can I even offer her?!"
    mc "My abs? My triceps? My handsome face?"
    e "......"
    mc "If her family is like you've said, what can I even do for her?"
    mc "I don't have the power to do things!"
    e "The fact that you're a nobody right now is the reason it has to be you."
    e "I plan to hide Aine after you get married."
    e "You don't have a name in industry or commerce, so it will be hard for her family to find her."
    mc "Is that the whole reason?"
    mc "I find that plan stupid! You're an investigator, aren't you?"
    e "No, that's not all."
    e "I know that you liked Aine before. She used to order you around, but you're a guy and you could have chosen to refuse her."
    e "She made you suffer, but you didn't try to refuse and fight back."
    e "Because deep down, your feelings for her were, and still are stronger than your anger."
    e "So, I'm sure that you won't hurt her in any way. That's another reason."
    mc "*sighs*"
    mc "You told me that you're not going to order me around. But, isn't this like what you guys did to me back then?"
    mc "Yeah, I admit it. It's not just that I liked her. I really loved her before. And I'm such an idiot for doing that!"
    mc "However, I'm not that guy anymore, Emma. The {b}me{/b} of the past is long gone, and that includes my feelings for Aine."
    mc "To be honest, I even swore to myself back then that I would get revenge on you guys. But I already moved on from that."
    mc "Heck, I didn't even want to see your faces here. I could've closed the door on you guys when you arrived earlier."
    mc "I know I should've done that because of what you guys did to me."
    mc "But I'm not a douchebag who'd do that."
    mc "However, I can't just let you enter here and suddenly tell me that I need to marry the girl who once made me suffer, Emma!"
    mc "You're just thinking about your own benefit! But what about me? Did you even try to consider me in that plan of yours, huh?"
    e "I..."
    mc "You didn't right? You just want what's best for Aine and that's it! Gwen lost her company, and you didn't even feel sorry for her at all?"
    mc "Jesus, Emma! For a moment there, you showed me real emotion, but now, you're just back to that monotonous voice of yours!"
    mc "You're really making me think that you're a robot or something, do you know that?"
    image ebb3:
        "i140.jpg"
        pause 3.0
        "i141.jpg"
        pause .2
        repeat
    show ebb3
    with dissolve
    e "{i}N-no... you're wrong... I'm...{/i}"
    mc "*sighs*"
    yt "What should I even do here?! I can't just agree to marry Aine just like that!"
    yt "Well, I mean... Aine is really beautiful. And I totally wouldn't mind her becoming my wife. Ehe he heee~"
    yt "That is, if she hadn't done anything to me back then."
    yt "I can't just marry a girl that I have a bad history with! That's just... weird!"
    yt "What's more..."
    yt "Everything is just too sudden. And I bet she doesn't even know about this plan at all..."
    yt "It should be the other way around, but I need to know if she's really worthy of my handsome face..."
    yt "Wait, what am I saying?"
    yt "Well... that's kind of true..."
    yt "All I have are looks and brains. I don't have the power to make things happen. Heck, I'm not even well known here in town."
    yt "But still... I need to know my self-worth here."
    yt "I'm not going to just go along with this and let them do it, but I do need to let them redeem themselves to me."
    scene i142
    with flash
    $ renpy.pause()
    show ebb3
    with flash
    yt "!!!!"
    yt "Holy shit!"
    yt "Why the hell did that pop inside my head all of a sudden?!"
    yt "Am I going crazy now?!"
    yt "But..."
    yt "...that's right... everybody deserves a chance."
    yt "Furthermore, about Aine's problem..."
    show ebb2
    with dissolve
    mc "You know that an Arranged Marriage won't happen unless both parties agree to it, right?"
    mc "You're a private investigator, you should know that."
    e "I know that. But I told you, she doesn't have any control over her life decisions."
    e "Her family will eventually force her to agree with it."
    e "No one could stop them from doing so, they always have a way through the law. That's how powerful her family is."
    mc "What a messed-up family she has!"
    mc "Then, how about you? You were appointed by her family right? Are you okay with betraying their trust?"
    e "I'm not betraying them. I'm just doing what they told me to do, and that's to serve and protect Aine."
    mc "Jeez... You're messed up too, you know that?"
    e "......"
    mc "After thinking about it for a while and considering what you said about her family, getting us married will solve nothing."
    mc "At the end of the day, even if we get married that doesn't free her from her family's control. It will take more than just that."
    mc "I'm not saying that I agree to go along with this plan of yours. But I'm going to see how it goes from here."
    mc "And I'm going to do it in my own way."
    mc "I may be soft hearted..."
    mc "But, that doesn't deny the fact that you two gave me a hard time before. So I can't trust you in any way."
    e "Fair enough."
    mc "Also, I have a few conditions if you want me in this stupid plan of yours."
    e "What are they?"
    mc "Stop spying on me. It makes me uncomfortable thinking that you might be just around a corner listening and watching what I do."
    e "Alright."
    mc "Promise me."
    e "I promise."
    mc "Lastly, stop calling me 'fatso' and call me by my name."
    scene i143
    with dissolve
    e "H-huh? B-but... I..."
    yt "Why is she acting like this all of a sudden?"
    mc "Then, you won't see me do anything."
    e "A-alright... I will..."
    e "[mc]..."
    e "......"
    e "{i}Saying his name once was okay, but twice is just..."
    e "{i}I-I can't let him see me like this, but I don't have a choice..."
    yt "Hmm?"
    mc "Good! Then, we're done here. I'm going to bed now. I still have work tomorrow."
    e "Okay."
    stop music fadeout 2
    scene black
    with dissolve
    scene i144
    with dissolve
    $ renpy.pause()
    show i145
    play sound 'audio/thud.mp3'
    with hpunch
    e "{i}......{/i}"
    e "{i}I knew this would happen...{/i}"
    e "......"
    e "{i}That was... the first time I ever talked to him without Aine beside me. That took all the courage I have...{/i}"
    e "{i}I feel so spent..."
    e "{i}Thank god~ It's over... *sighs*{/i}"
    play music 'audio/Inspiring.mp3'
    scene i146
    with flash
    k "Emma! How are you doing, honey? I read the email you sent me!"
    k "I'm still in shock over what I read, honey."
    k "I didn't expect you to ask my permission for something like that."
    k "You're a strange one, aren't you?"
    k "Holding back your own feelings for the sake of your friend's well being."
    e "Uhm... I don't understand what you're talking about, Miss Klara."
    scene i147
    with dissolve
    k "I am a grown up woman, Emma."
    k "Did you think I wouldn't notice as you kept checking on [mc] before?"
    k "I agreed on keeping your secret as I thought you would do something about it yourself, but you failed..."
    k "You are intelligent, yet too innocent."
    scene i148
    with dissolve
    e "What... are you..."
    k "I wasn't able to personally confront you girls about [mc] before, since I was always away due to the nature of my work."
    k "And that... is something I deeply and will forever regret as his guardian."
    k "Even after everything stopped when I escalated it to the school's deciplinary committee, you still contacted me and kept on apologizing."
    k "You were always concerned about him despite what you were doing to him."
    k "That is enough for me to know that you have something for [mc]."
    scene i149
    with dissolve
    e "......"
    k "You can't even deny it."
    k "I was extremely confused by you. You were giving him a hard time, so why did you show concern for him."
    k "However, I understood as soon as I did some research and learned about you and your family's history."
    k "I'm not good with giving advice to people, but..."
    k "If ever [mc] and your friend get married, then what about you?"
    k "You can't just hide it away forever, Emma."
    k "That will only make you suffer."
    scene i150
    with dissolve
    e "I did this to myself, Miss Klara. I am nothing but a servant now..."
    k "What do you mean?"
    e "......"
    k "You really don't talk much, do you?"
    k "*sighs* Well then, about the marriage..."
    k "I can't control [mc]'s decision about that, honey."
    k "Even if I agree, it's still up to him if he wants it or not."
    k "What's more... how can they even get married if their relationship is in such a mess?"
    e "I... don't know..."
    e "Maybe I could just tie them together with a rope until they forgive each other."
    k "......"
    k "..........."
    e "Miss Klara?"
    k "*sighs* Look. I have an idea."
    k "You guys are looking for a place to stay, right?"
    e "Yes..."
    k "I will open my doors to you."
    k "It may be selfish of me to do this to him, but this is all for the better."
    e "O-okay..."
    k "You guys go and live there together with him."
    k "Right now, he's a bit blinded with what you did to him, but there is something he did wrong himself and he needs to realize that."
    k "So this is a chance to fix your mistakes and redeem yourselves to each other."
    k "You are all grown up now, be mature."
    k "And I just want to let you know that I do not agree with your idea."
    k "I still want what's best for [mc]."
    k "But, whatever happens from here on out will be up to you guys to decide. I won't interfere with your decisions."
    k "[mc] is old enough to know what he wants and needs."
    k "And lastly, Emma?"
    e "Yes, Miss Klara?"
    k "Thank you for caring for [mc]."
    k "I know you didn't have any choice, so you must have endured a lot seeing him get hurt."
    k "If it was up to me... It would be you that I want [mc] to marry. Despite everything, I know that you're a good soul."
    scene i151
    with dissolve
    e "......"
    e "......*sobs*"
    k "I'm sorry, honey... I trust you on this. I'll leave everything to you for now. Don't let me down."
    scene i145
    with flash
    e "{i}Miss Klara... What do I do now?{/i}"
    stop music fadeout 2

    scene black
    with dissolve
    with fade

    play music 'audio/SAX.mp3'
    scene i152
    with dissolve
    $ renpy.pause()
    show i153
    with hpunch
    yt "AAAHHHH~!!!"
    play sound 'audio/chair.mp3'
    scene i154
    with dissolve
    yt "I can't sleep at all~! I still have a job to do tomorrow for Christ's sake!"
    yt "I can't help but think about what Emma and I discussed down stairs!"
    yt "'I'm gOiNg tO sEe hOw iT gOeS fRoM hErE.'"
    yt "You don't even know what to do, you idiot!"
    yt "If I ever do make a move with Aine. I will come up against her family for sure!"
    yt "And... what's with Emma's reaction earlier? She's really confusing the hell out of me!"
    yt "For a moment she shows a bit of her emotion, and then she goes back to being a robot all of a sudden. What's wrong with her?!"
    scene i155
    with dissolve
    yt "Urrgghh! Stop thinking about it already!"
    scene i156
    with dissolve
    yt "*sighs*"
    yt "What should I do now? I can't really sleep."
    yt "Should I play some computer games?"
    yt "Nah... That will just make things worse."
    yt "I remember playing that famous game called Genshin Impact once, and before I even realized it, it was already 5 in the morning!"
    yt "Good thing it was my day off!"
    yt "So, not a good idea!"
    yt "......"
    yt "Well then, I guess I'll just head downstairs and see if there's something I can eat. Maybe a full stomach will help me sleep later."

    scene black
    with dissolve
    with fade

    scene i157
    with dissolve
    $ renpy.pause()
    scene i158
    with dissolve
    yt "Gwen?"
    yt "Drinking wine in the middle of the night, huh?"
    yt "Well, what do I even expect from her? She was a drunkard back in high school."
    yt "Only difference now is that she's using a wine glass. *chuckles*"
    scene i159
    with dissolve
    g "Hey... Can't sleep?"
    mc "Yeah, how did you know?"
    g "Just a guess, since I couldn't sleep either."
    mc "Is that why you're drinking?"
    g "Mmm..."
    yt "She must be really devastated from losing her company."
    yt "Well, of course she would be. It's a company we're talking about here."
    g "By the way, do you want some?"
    menu:
        "Sure":
            $ gwenpoint += 1
            $ renpy.notify(gwennotif)
            mc "Hm... Sure, just a little bit."
        "No, thanks{#ep1}":
            mc "Uh... No, thanks. I'm good. I just came here to eat."
            g "No worries."

    scene black
    with dissolve
    with fadeq

    scene i160
    with dissolve
    mc "Ahh... That was good!"
    g "Hmm... noodles, huh? They're not good for you, you know?"
    yt "Are you my mother or something?"
    scene i161
    with dissolve
    mc "Well, this is the quickest food I can fix. I need to go back to bed as soon as I can, I have a shift tomorrow."
    g "Oh, that's right. You work in a burger shack in midtown."
    mc "Yeah."
    g "Before you head back to your room, can I ask you something?"
    mc "Uhh... yeah? What is it?"
    g "Do you..."
    g "...still remember me, [mc]?"
    yt "Uh-oh..."
    mc "W-what do you mean?"
    scene i162
    with dissolve
    g "Sheesh... No need to pretend anymore, [mc]. We're alone here, I know it's you!"
    g "I didn't remember you until we met earlier, though..."
    g "Things were so busy during and after college that I didn't have any time to even think about the past."
    g "Dude, seriously, what happened to you? You look like a different person now!"
    g "Way more handsome than before, that's for sure!"
    g "You still remember me, right? right~? Hahaha!"
    scene i163
    with dissolve
    yt "Well damn..."
    yt "I guess Gwen will be Gwen, after all. She talks non-stop sometimes."
    menu:
        "Yes{#ep1}":
            mc "Yes, I remember you. Not just you, I remember Aine and Emma too!"
        "No{#ep1}":
            mc "No, I... don't."
            g "Oh, come on... I know you remember me! Stop pretending already!"
            mc "*sighs*"
            mc "...Alright, I remember you. Not just you, I remember Aine and Emma too!"
    scene i162
    with dissolve
    g "Who knew this is how we would meet again? Hahaa!"
    yt "You should ask Emma."
    g "So you do still remember me, huh? Well I knew you would..."
    mc "Of course. How could I forget about you after what happened in the past?"
    scene i164
    with dissolve
    g "Dude, I didn't do anything to you before!"
    mc "Uhh... No, I didn't mean that."
    mc "{b}We{/b} technically did it..."
    scene i165
    with dissolve
    g "Oh..."
    g "...That."
    g "I didn't! But still, I think it was only fair!"
    g "Yeah, I was drunk, but I already apologized for giving you that... that... big..."
    g "Ahh, nevermind! I just took responsibility! You also agreed to do it with me anyway!"
    scene i166
    with dissolve
    yt "Well, that's true..."
    yt "Gwen was my soft spot since she didn't really do anything to me. In fact, she even tried to defend me one time."
    yt "Although I was not very willing, I still found myself helping her every time she needed it."
    yt "To be honest, I was also following Emma and Aine's orders, but it was different with her..."

    scene black
    with dissolve
    yt "It was during the afternoon class..."
    yt "I was on my way back from the restroom to our classroom when I found her in the corridor drunk."

    scene i167
    with dissolve
    mc "Gwen?"
    scene i168
    with dissolve
    mc "H-hey, Gwen. Why are you-"
    scene i169
    with dissolve
    mc "Eek! You reek of alcohol!"
    scene i170
    with dissolve
    g "Oh, [mc]? H-help-"
    g "Mmp! Help me... Mmp! Go to the restroom."
    mc "A-alright!"

    scene black
    with dissolve
    with fadeq

    scene i171
    with dissolve
    mc "Are you sure you want me in here? This is the girls' restroom! What if someone comes in and sees me?"
    g "Then, just tell them that-"
    g "Mmp!"
    g "You're helping me!"
    mc "Jeez!"
    mc "You skipped our afternoon classes just to drink?!"
    mc "Have you been on the rooftop with those girls in the other class again? You could put yourself in danger, you know?"
    mc "You shouldn't just wander around the school drunk! What if some random retard took advantage of you?"
    scene i172
    with dissolve
    g "You know, [mc]... We're really not that close... and yet... you still choose to... help me."
    mc "Well... you're different from Aine and Emma. You don't force me to do anything I don't want to. That's why..."
    scene i173
    with dissolve
    g "Hmm... You're... a good guy... you know that?"
    g "*giggles* I already envy... the lucky girl that you... will marry in the future."
    scene i174
    with dissolve
    mc "That will never happen..."
    mc "No one likes me because of how I look..."
    show i175
    play sound 'audio/woosh.mp3'
    g "Hey! Love isn't... all about how you... look! It's about how... you feel and what... your heart dictates!"
    g "Aine... may have rejected you... but there will be... a girl who will eventually... like you for who... you are!"
    g "Don't body shame yourself, stupid!"
    g "I mean, dude... I don't even see you that way!"
    scene i176
    with dissolve
    mc "...You talk like you have experience with it. But, you've never had a boyfriend, right?"
    mc "You just watch too many romantic movies..."
    g "H-hey! How did you... know about that?!"
    mc "I saw you watching on your mobile phone once before."
    mc "No, too many times, I think..."
    scene i177
    with dissolve
    g "Y-you!"
    show i171
    g "Mmp!"
    g "Uwaaa..."
    mc "Yikes!"

    scene black
    with dissolve
    with fadeq

    scene i178
    with dissolve
    g "Ugh! The world is... spinning like crazy..."
    mc "Huh? Should I take you to the nurse's office instead?"
    g "N-no... if the nurse... sees that I'm drunk... I will be sent... for guidance... counseling for sure..."
    mc "Well, I think you really need it."
    scene i179
    with dissolve
    g "I don't, you idiot!"
    g "Let me... just stay here..."
    scene i180
    with dissolve
    g "...for a moment......."
    mc "H-hey, Gwen. Hold on!"
    show black
    play sound 'audio/doorslam.mp3'
    "*baam*!" with hpunch
    play sound 'audio/thud.mp3'
    "*thud*!" with hpunch
    scene i181
    with dissolve
    yt "God friggin..."
    yt "Good thing I got a hold of her and she landed on the toilet! That could've been dangerous!"
    mc "Hey, Gwen... I still have to go back to class!"
    mc "Gwen? Hey, Gwen!"
    yt "She's out cold..."
    scene i182
    with dissolve
    yt "I don't want this... and yet, I still end up helping her anyway..."
    yt "If not for her personality. We could've been real friends for sure."
    yt "*sighs*"
    yt "What do I do now?"
    yt "Should I just lift her up and carry her to the nurse's office?"
    yt "But, she's so heavy... I don't have the strength to lift her!"
    yt "Damn it! If only my body was fit!"
    scene i183
    with dissolve
    yt "Wait..."
    yt "What the...! Have I been holding Gwen's thigh this whole time?!"
    scene i184
    with dissolve
    yt "W-wow... It feels... so smooth..."
    yt "I never felt anything so smooth before..."
    yt "Oh no! I'm getting a boner! And it's hitting her down there!"
    scene i185
    g "Mmnhh~"
    yt "Did she just moan?"
    yt "No no no no! Not now! I can't... lift Gwen up!"
    mc "Uhm... Gwen? Please wake up!"
    mc "Come on Gwen, wake up! Hey~!"

    scene black
    with dissolve
    with fadeq

    "An hour later..."

    scene black
    with dissolve
    with fadeq

    scene i186
    with dissolve
    yt "Urrh! It's getting really painful now and my legs are numb!"
    yt "My meat keeps on hitting her thing down there, and it just won't calm down!"
    yt "I really need to wake her up now!"
    mc "*wiggles* Hey, Gwen! Wake up, now!" with hpunch
    scene i187
    g "*moans* H-haaah~ Ahhh~!"
    yt "Ahh! I shouldn't have done that! It just made things worse!"
    yt "How can she just moan like that and still be unconscious?!"
    yt "But, she responds every time my thing grinds her down there..."
    mc "*sighs* I don't want to do this but you leave me no choice, Gwen!"
    yt "Let me just get it out, and..."
    mc "*wiggles*" with hpunch
    scene i188
    with dissolve
    g "*moans* Mnnhh~ Haah~"
    scene i189
    with dissolve
    yt "W-what is this?! T-this feels so good~!"
    scene i190
    with dissolve
    g "Mnnh~"
    scene i191
    with dissolve
    g "Wha..."
    show i192
    play sound 'audio/woosh.mp3'
    with hpunch
    g "Ahhhh~! What are you doing to me, you pervert!"
    scene i193
    with dissolve
    mc "Finally! Do you know how long I've been trying to wake you up?!"
    mc "You were sleeping on top of me for more than an hour!"
    mc "I couldn't help but think of perverted things! And this thing started reacting!"
    scene i192
    g "You could've just lifted me up, you know?!"
    mc "I would've already done that if I had the strength to lift you up! But, I don't!"
    mc "You kept responding every time I tried to move my... thing..."
    mc "That's the only way I found to wake you up!"
    scene i194
    with dissolve
    g "So... you're like that... because of me?"
    scene i193
    with dissolve
    mc "Of course! We're the only ones in here! Who else could've caused it?"
    mc "You're just so attractive and your... your thighs felt so soft!"
    mc "I couldn't help it! Plus, your moans made it even worse!"
    g "Then... that big... I mean... It's been like that for an hour now?"
    mc "Yes! That's why I had no choice but to do that, since it's getting really painful!"
    mc "It could be bad if it stayed like that for too long, you know?"
    scene i194
    with dissolve
    g "Oh... I'm sorry, I didn't know..."
    g "{i}Despite his big body, his thing is... so fucking huge!"
    g "{i}So, does every man's thing look like this?"
    scene i195
    with dissolve
    mc "*sighs* Let's just forget about it, I still need to go back to class. You can stay here if you want."
    g "Wait... are you... going back with that thing?"
    mc "Well, what can I do? It's still reacting to your body. I'll just have to force it into my pants!"
    scene i196
    with dissolve
    g "T-then... do you want to... go further?"
    g "I should... take responsibility for making it like that. You also said that it's dangerous for it to stay like that, right?"
    g "{i}I... I don't know what I'm thinking anymore... my body is just asking for more because of what he did...{/i}"
    g "{i}I wonder how would it feel if I...{/i}"
    scene i197
    with dissolve
    mc "W-what are you..."
    yt "Does she mean that I can do more than that to her?"
    yt "*gulps* I... wonder how would it feel if we... if we..."
    scene i196
    with dissolve
    g "Come on, give me an answer."
    mc "*nods* Mmh! Mmh!"
    g "Then..."
    stop music fadeout 2

    scene black
    with dissolve
    with fade

    play music 'audio/WhereEverYouGo.mp3'
label gwenmcpast:
    if _in_replay:
        $ name = persistent.gallery_name
    scene i198
    with dissolve
    mc "D-do you know how to do this?"
    g "No, I don't... This is... the first time."
    yt "I... pretty much guessed that."
    scene i199
    with dissolve
    g "I should just put your thing in here, right?"
    mc "Yeah, I think so..."
    g "{i}Slowly... and...{/i}"
    scene i200
    with dissolve
    g "MMNNHH~!!"
    yt "I-it's not even halfway in, but it already feels so good! It feels so hot inside her!"
    mc "If it's too painful, we can just stop, Gwen."
    g "Be quiet, you mongrel! I'm trying to..."
    scene i201
    with dissolve
    g "AAAHHHHHH~!!!"
    mc "Gwen, I felt... something break inside you..."
    scene i202
    with dissolve
    g "I... can't believe that I would be giving this to you at all, big boy."
    g "Who could've thought that-"
    play sound 'audio/opendoor.mp3'
    g1 "Did you hear something in there?"
    scene i203
    play sound 'audio/gasp.mp3'
    g "*gasps*!"
    scene i204
    with dissolve
    yt "Uh-oh!"
    g2 "Hmm... no. I don't think so."
    g1 "I thought I heard someone moan."
    g2 "It's probably your imagination. You just play too many porn games these days."
    g1 "Yeah, yeah! Whatever! Let's just go."
    scene i205
    with dissolve
    mc "Phew!"
    scene i206
    with dissolve
    g "MMMNNNNHHHHHHH~!!"
    mc "Wait... did you just..."
    scene i207
    with dissolve
    g "*huff* I... I don't know..."
    g "The thought of being... seen made me really nervous, but then... *huff*"
    yt "Well, that's weird..."
    scene i208
    with dissolve
    mc "T-then... are we... done already? Since you-"
    scene i209
    g "Shhhhh... *giggles*"
    g "Why do you look sad? Don't worry..."
    g "...We're not done yet."
    g "We already went this far."
    g "We can't let our first times go to waste, right?"
    mc "How did you know that this is my first time?"
    g "Well... isn't it obvious?"
    mc "Ouch..."
    g "Sheesh~! Don't be like that... I'm not insulting you or anything."
    g "I told you, don't think of you that way."
    g "Look, come here."
    scene i210
    with dissolve
    "*kisses*"
    mc "!!!!"
    yt "This is... just purely because of lust, right?"
    scene i209
    with dissolve
    g "Now there goes our first kiss too. *giggles*"
    yt "The longer I look at her, the more beautiful she becomes... I didn't know Gwen could be this pretty."
    scene i211
    with dissolve
    g "I don't really know how, but I'm going to try and move my hips, okay?"
    mc "Uh... Okay..."
    show gwen1
    with dissolve
    $ renpy.pause()
    g "Mnnhhh~! Oh my god~!!"
    g "Ahh~ Hahh~ Ahh~!!"
    mc "Shhhh... Keep your voice down! What if someone hears us again?!"
    g "Let them hear us, then! I... don't care anymore, [mc]. It's starting to feel so good~!"
    $ renpy.pause()
    show gwen2
    with dissolve
    $renpy.pause()
    mc "G-Gwen... S-slow down a bit!"
    mc "If you keep doing that, I'm..."
    g "Inside me, [mc]! Just do it inside me!"
    mc "Are you sure?! You might..."
    g "Don't worry about that! I just want to enjoy this!"
    mc "Alright then, if you say so!"
    $ renpy.pause()
    show gwen3
    with dissolve
    $ renpy.pause()
    g "Something's about to come out again, [mc]!"
    g "I'm... almost..."
    mc "Me too, Gwen!"
    mc "I'm..."
    $ renpy.pause()
    scene i212
    with hpunch
    g "AAAAAHHHHH~!!!"
    mc "Arrggh~!"
    with hpunch
    $ renpy.pause()
    with hpunch
    $ renpy.pause()
    with hpunch
    $ renpy.pause
    scene i213
    with dissolve
    g "*huff* *huff*"
    g "I can feel your... hot stuff inside me... *huff*"
    scene i214
    with dissolve
    yt "Is it... over already?"
    yt "*sighs* I guess it is... I don't want it to be over so-"
    scene i213
    with dissolve
    g "Do you... want to keep going? *giggles*"
    scene i215
    with dissolve
    mc "Whaaa..."
    mc "*nods* Mmh!"
    scene black
    with dissolve
    scene i216
    with dissolve
    mc "(We kept on doing...)"
    scene black
    with dissolve
    scene i217
    with dissolve
    mc "(And doing...)"
    scene black
    with dissolve
    scene i218
    with dissolve
    mc "(And doing it... like we didn't have a care in the world.)"
    mc "(We didn't stop until our bodies couldn't take it any longer.)"
    mc "(We fell asleep in there from exhaustion. And that was the moment I realized that my body has endurance for things like that after all. Hahaha!)"
    mc "(For the love of God, no one entered the restroom while we were doing it. Except the janitor who caught us sleeping in there naked. *chuckles*)"
    mc "(Thinking back now... that was really embarrassing. But...)"
    mc "(...That moment filled with lust together with Gwen, is one of the things I will never forget.)"
    image gkb:
        "i219.jpg"
        pause 3.0
        "i220.jpg"
        pause .2
        repeat
    show gkb
    with dissolve
    yt "After that day, things became different..."
    yt "I thought it would make us closer to each other, but it doesn't always work that way..."
    yt "Even talking to each other made it really awkward..."
    yt "I was blaming her for what happened. But, to be honest... I really shouldn't have — I consented to everything we did, too."
    yt "And now... she is right in front of me, and it's getting awkward... again..."
    yt "Although, I'm just glad that she didn't discriminate against me like Emma and Aine did."
    image gkb2:
        "i221.jpg"
        pause 3.0
        "i222.jpg"
        pause .2
        repeat
    show gkb2
    with dissolve
    mc "Yeah, yeah... Let's just forget about the past already."
    g "Do you... regret what happened that time?"
    mc "Uh... not really. Did you?"
    g "A bit, yeah..."
    mc "Really?! Why?"
    g "Hmm... I can't tell you that, yet."
    g "We may have done something in the past, but things are... a little bit different now..."
    mc "Well... yeah, I get it."
    mc "Then, I'm going to go upstairs now."
    g "Sure!"
    g "Good night, and nice to meet you again, [mc]."
    g "And don't worry, I won't tell Emma and Aine."
    yt "Well, Emma was the one who set this up, you know?"
    mc "Thanks... and good night."
    $ renpy.end_replay()
    stop music fadeout 2

    scene black
    with Dissolve(2.0)
label gwenpause:
    if _in_replay:
        $ name = persistent.gallery_name
    scene gwenpause
    with dissolve
    $ renpy.pause()
    $ renpy.end_replay()
    play sound 'audio/gamepause.mp3'
    show title at move_slide
    with flash
    $ renpy.notify(imageunlock)
    $ renpy.pause()

    scene black
    with dissolve
    with fade

    scene i152
    with dissolve
    yt "Hmm... Talking about the past and discovering my identity doesn't seem to be a big deal to her at all."
    yt "Her mind must be full of thoughts about her company."
    yt "......"
    yt "Ahh... don't think of helping her again, you idiot! Your plate's already full with Emma and Aine's problem!"
    yt "*sighs* Whatever... Let's just go to sleep..."
    yt "......"
    yt "........."
    play sound 'audio/thunder.mp3'
    "*thunder*!!" with flash
    scene i153
    with hpunch
    yt "OH COME.. OOOOOONNNNN~!!"

    scene black
    with dissolve
    with fade

    play music 'audio/Elevate.mp3'
    scene i223
    with dissolve
    s "[mc], wake up~!"
    mc "Mmmnnn... 5 more minutes..."
    scene i224
    with dissolve
    s "Hey~! It's already 7:30am! Your shift is at 8am, right?!"
    scene i225
    mc "WHA? 7:30am?!"
    s "What happened? You never woke up this late before!"
    scene i226
    mc "Oh fuck, fuck, fuck, fuck!"
    s "You need to really hurry now or you'll be late!"
    menu:
        "Thank her":
            $ skypoint += 1
            $ renpy.notify(skynotif)
            scene i227
            with dissolve
            mc "Thanks for waking me up, Sky!"
            s "No problem. Just hurry up!"
            mc "I will!"
        "Just rush!":
            s "Go, go, go, go~!"

    scene black
    with dissolve
    with fade

    scene i228
    with dissolve
    yt "Damn it! I've got to hurry now!"
    yt "Emma and that damned thunder wouldn't let me go to sleep last night!"
    yt "And I just missed the opportunity to coach Lily!"
    yt "They've only been here for a day, and things are already getting stressful! *sighs*"
    scene i229
    with dissolve
    stop music fadeout 1
    mc "Oh..."
    scene i230
    with dissolve
    a "Mm! *sniffs*"
    scene i231
    with dissolve
    a "Mm!! *sobs*"
    mc "No, no, no, no, don't you dare-"
    show i232
    with hpunch
    a "*crying* WAAAAAAHHH~!!"
    s "Oh... I forgot to tell him that Aine is using the bathroom."

    scene black
    with dissolve
    with fade

    play music 'audio/Elevate.mp3'
    scene i233
    with dissolve
    yt "I must say, coming here every morning and seeing Lily is like a breath of fresh air. Haha."
    yt "Let's just forget about what happened and enjoy this day with Lily."

    scene black
    with dissolve
    with fade

    scene i234
    with dissolve
    l "Good morning, [mc]. You're a bit late today. That's quite unusual. Hehe."
    image lwb:
        "i235.jpg"
        pause 3.0
        "i236.jpg"
        pause .2
        repeat
    show lwb
    with dissolve
    mc "Yeah, I had trouble sleeping last night."
    yt "That friggin thunder!"
    mc "I woke up at 7:30 and had to rush to get here. Aha haa..."
    mc "We missed our chance for me to coach you too. *sighs*"
    menu:
        "Apologize":
            mc "Sorry, Lily. Can we do it some other time?"
            l "That's alright! No need to apologize!"
            $ lilypoint += 1
            $ renpy.notify(lilynotif)
        "Don't say anything":
            l "That's alright!"

    l "Hmmm....."
    l "Maybe we can do it later after our shift, instead?"
    mc "Are you sure? Won't that make you late for your courses?"
    l "No! I still have 2 hours of free time after every shift. I can spend an hour with you."
    yt "I might go home a little bit late because of this, but that's no reason to refuse."
    yt "First of all, I missed our chance earlier that I promised Lily."
    yt "Second, it's not just to be friendly, it's part of my responsibility as her senior co-worker to teach and guide her."
    mc "Alright, then. Let's do it after our shift today."
    l "Great! I can teach you some techniques to help you sleep better, too! *giggles*"
    mc "Good! I can't wait to learn about them!"
    scene i237
    with dissolve
    un "Good morning, guys!"
    mc "Good morning, boss!"
    l "Good morning, Miss Jess!"
    scene i238
    with dissolve
    yt "This is Miss Jess, our boss and the owner of this place. She is very kind, but she can be quite strict when she needs to."
    yt "She often comes here to check the place and observe her employees' performance. You could call it an evaluation."
    yt "I wonder if she'll do that today. If she does, it will be Lily's first time. I hope she does okay."
    j "I kept telling you not to call me boss, didn't I?"
    mc "Haha. Alright then, Miss Jess."
    j "Good!"
    j "Now then, we'll do the usual today."
    j "Oh, I forgot. This will be Lily's first time, right?"
    scene i239
    with dissolve
    l "Uhm... First time with what, Miss Jess?"
    j "I come here at least once a month to check the place and observe you guys' performance for a whole shift."
    j "I will give you comments and suggestions about your performance after the observation."
    j "Don't be nervous, Lily. I won't fire anyone if you guys somehow mess up."
    l "Oh... A-alright..."
    l "{i}I'm still really nervous~! This is my first time to be evaluated!{/i}"
    j "And I'm sure [mc] won't let that happen, right?"
    mc "Of course, Miss Jess!"
    j "Then, let's start with the first customer to come in."

    scene black
    with dissolve
    with fadeq

    "After your shift..."

    scene black
    with dissolve
    with fadeq

    scene i240
    with dissolve
    mc "Phew!"
    yt "What a busy day! Why does it seem like a lot of people come here to eat during evaluations?"
    yt "Are they attracted to Miss Jess or something?"
    l "Ahh... That was really nerve wracking!"
    l "Thank god, I managed to survive."
    scene i241
    with dissolve
    j "Good job, both of you!"
    j "Impeccable performance from [mc] as expected."
    j "However, you need to work on your approach to customers, Lily. I can see that you're having trouble with things you don't know yet."
    j "I'm pretty sure [mc] can give you advice about that."
    j "But still, you did an excellent job!"
    l "Thanks, Miss Jess."
    scene i242
    with dissolve
    j "Alright, that will be all for today. I need to see my husband now."
    mc "You already have a husband?!"
    j "Why do you seem so shocked, [mc]? I was just kidding."
    j "We're far from that. I do have a lot of competition, after all."
    yt "Competition?!"
    scene i243
    with dissolve
    "*door opens*"
    j "Speak of the devils."
    scene i244
    with dissolve
    j "Hey, you two. My place is already closed."
    z "Bruh... I can still see the cashiers right there!"
    j "Well, their shift is already over."
    i "It's okay, Zoey. We can just find another place to grab some food."
    j "*sighs* Alright, I'll let you buy what you want just this once. But come here during business hours next time."
    scene i245
    with dissolve
    i "For real? Thanks, Jess! You know we really like your burgers!"
    j "You already told me that like a million times."

    scene black
    with dissolve
    with fadeq

    "A few moments later..."

    scene black
    with dissolve
    with fadeq

    scene i246
    with dissolve
    mc "Are those two twins? They look almost identical."
    scene i247
    with dissolve
    j "Yes, they are twins. Their story however, {size=-10}is... quite tragic...{/size}"
    mc "Hm?"
    scene i248
    with dissolve
    j "I'll leave you guys now. Take care on your way home."
    l "You too, Miss Jess. Please take care."
    scene i249
    with dissolve
    mc "Alright, should we start?"
    l "Sure!"
    mc "Let's change out of our uniforms."

    scene black
    with dissolve
    with fade

    scene i250
    with dissolve
    mc "Okay... First thing's first. I want to ask you about your work history since I haven't really asked you about your previous jobs before."
    image lwtb:
        "i251.jpg"
        pause 3.0
        "i252.jpg"
        pause .2
        repeat
    show lwtb
    with dissolve
    l "I only had one job before. I was a contact center agent, but it wasn't really much since I didn't last long there."
    mc "Why is that? That's a great job to be honest."
    l "It's not that I'm shy or anything. But I tend to get nervous when talking to people that I don't know. Especially if they're angry."
    l "Unfortunately, I was fired by my boss due to a lot of 'Agent Error' as I kept giving wrong information to the customers."
    l "To them, it was enough of a reason to fire me."
    l "I think I only lasted for a month there."
    yt "Hmm... getting nervous when talking to other people, huh? She said she's not a shy type, and I can vouch for that too."
    yt "Hmmmm... I think I have an idea what's going on."
    mc "I think I know what your problem is, Lily."
    image lwtb2:
        "i253.jpg"
        pause 3.0
        "i254.jpg"
        pause .2
        repeat
    show lwtb2
    with dissolve
    l "Really?"
    mc "Yeah! And I think you're losing focus when talking to your customers. Especially the irate ones."
    mc "I believe that you have the skill to handle it. But things get muddled in your head and you tend to get panicky in those situations."
    mc "As a result, you can't perform your best."
    mc "To tell you the truth, I kept getting nervous for the first couple of weeks after I started here too!"
    mc "But I learned how to overcome it, and that's what I'll tell you about now."
    l "Okay. So what should I do?"
    mc "First thing you need to do is to 'Plan and Visualize'. Or 'Imagery Training' is what most people call it."
    l "Imagery Training?"
    mc "Yep! It's really simple!"
    mc "Just try to imagine a scenario where you're facing a challenge in your daily life."
    mc "Here, for example."
    mc "And then, imagine yourself using the proper or ideal way to handle it."
    mc "I think it is a very effective technique!"
    mc "Because our thoughts shape our reality. Our thoughts generate feelings, feelings lead to action, and action leads to results."
    l "Jeez... That's deep, [mc]."
    mc "Oh... is it? Hahaha!"
    l "Haha. Don't mind me. Please, continue."
    mc "Right. I think the best time for you to do it is in the morning when your mind is still clear. Anytime before we start our shift should be perfect."
    mc "And don't just think about it. Try to visualize the scene and simulate your feelings in it."
    mc "Try doing it as much as you can and your subconscious will do everything it can to help turn the images into reality."
    mc "It won't be easy and you won't be able to do it overnight, but you'll get there eventually."
    l "Alright. I'll remember what you taught me and try it as soon as I get home."
    mc "Shouldn't you be taking some notes instead?"
    l "Don't worry, I can remember things fairly well. Especially if it is something that was discussed."
    mc "Good!"
    mc "Oh, and one more thing! This is also very important."
    mc "Always take a deep breath when you're about to answer your customer. Not just during your Imagery Training, but also in real situations."
    mc "It will help you clear your mind and relax you a little bit."
    l "Hmm... Okay~! I'll try that too!"
    yt "I think we should try doing a scenario, right now. We still have time."
    yt "I still remember what happened last time. That should be a perfect scenario!"
    yt "What should I do?"
    menu:
        "Do it now":
            $ lilytutor = True
            mc "I think we should try a sample scenario right now. We still have time."
            mc "And I want to help you as much as I can."
            mc "Who knows when we'll be able do this again, you know?"
            l "Oh, yes! Sure, [mc]! I'm up for the challenge!"
            mc "Great! Then, do you still remember that guy from last time?"
            l "Uhh... Yes, I do."
            mc "Good. Now try to imagine that scenario happening again."
            scene i255
            with dissolve
            l "Okay..."
            scene i16
            with flash
            ass "I told you that I literally found a cockroach inside my burger, you bitch! What are you gonna do about it?!"
            scene i255
            with dissolve
            l "Uhm..."
            yt "She seems to be panicking again."
            mc "Remember what I told you when you're about to answer your customer?"
            menu:
                "Take a deep breath":
                    mc "Take a deep breath and think of what the ideal answer to the situation is."
                    l "....."
                "Take a short breath":
                    mc "Take a short breath and think of what the ideal answer to the situation is."
                    l "....."
                    show lwtb
                    with dissolve
                    l "Wait... isn't it supposed to be a deep breath?"
                    mc "Oh, yeah! You're right! Sorry, I was thinking of something else for a moment there."
            scene i255
            with dissolve
            l "*inhales*..."
            l "*exhales*..."
            scene i256
            with dissolve
            l "I'm sorry for your terrible experience, sir. We will be happy to compensate you however we can."
            l "But, we need proof of your experience in order for us to do so."
            scene i257
            with dissolve
            l "{i}Whoa... How did I...{/i}"
            mc "Excellent! I knew you had it in you, Lily! Hahaha!"
            l "I... I didn't expect that at all!"
            mc "Now that we confirmed you definitely have the skill, it's just a matter of how you can do that in a real situation next time."
            scene i258
            with dissolve
            l "Thank you, [mc]. I promise I will do my best to improve."
            mc "That's good to hear! Just take your time. You'll eventually get there."
            l "I will! Haha!"
        "Not right now":
            $ lilytutor = False
            yt "Nah... I should just let her do it herself first."

    scene i259
    with dissolve
    "*phone vibrates*"
    l "Oh! That's mine!"
    scene i260
    with dissolve
    l "Hello, Shina?"
    "......"
    l "Right now?"
    ".........."
    l "Oh... I see. Alright, I'm coming then!"
    show lwtb2
    with dissolve
    l "I'm sorry, [mc]. I need to go now."
    l "My classmate, Shina, needs me right now."
    mc "That's alright. Don't worry about me."
    l "About the sleeping technique I mentioned earlier. I'll just message it to you so you can try it later when you sleep."
    l "It's just a simple step-by-step process."
    mc "Yeah, sure! I can't wait to learn about it!"
    yt "And I hope that it will put me to sleep even with everything going through my mind. Haha."
    if lilytutor:
        scene i261
        with dissolve
        l "Oh, hold on..."
        l "Before I go..."
        scene i262
        with dissolve
        l "*kisses*"
        mc "!!!!"
        yt "What the...!"
        scene i263
        with dissolve
        l "Thanks, I really appreciate small gestures like this. You earned it."
        yt "I guess this is a step-up from the last time, huh?"
    l "I'll go now. See you tomorrow, [mc]."
    mc "See you tomorrow, Lily."
    stop music fadeout 2

    scene black
    with Dissolve(2.0)
label lilypause:
    if _in_replay:
        $ name = persistent.gallery_name
    scene lilypause
    with dissolve
    $ renpy.pause()
    $ renpy.end_replay()
    play sound 'audio/gamepause.mp3'
    show title at move_slide
    with flash
    $ renpy.notify(imageunlock)
    $ renpy.pause()

    scene black
    with dissolve
    with fade

    play music 'audio/Ocean.mp3'
    play sound 'audio/closedoor.mp3'
    scene i265
    with dissolve
    $ renpy.pause()
    scene i266
    with dissolve
    a "Hm? Good afternoon, [mc]."
    yt "Damn! I can't get used to her greeting me every time she sees me."
    yt "It seems she's not upset about what happened earlier."
    yt "Well... it was just an accident, so..."
    image amcghb:
        "i267.jpg"
        pause 3.0
        "i268.jpg"
        pause .2
        repeat
    show amcghb
    with dissolve
    mc "Oh... Good afternoon."
    a "How was your day at work?"
    mc "Well... Ordinary. But it's pretty tiring since I work nonstop."
    mc "My only break is for lunch."
    a "I see..."
    image amcghb2:
        "i269.jpg"
        pause 3.0
        "i270.jpg"
        pause .2
        repeat
    show amcghb2
    with dissolve
    mc "How's your job hunt working for you?"
    a "Still nothing so far, to be honest."
    mc "Did you try searching online?"
    a "Yeah, that's actually where I tried looking."
    a "I submitted my resume to a lot of companies yesterday, but I've had no response from any of them so far."
    yt "She seems to be really brooding about it."
    yt "Should I try and comfort her?"
    menu:
        "Comfort her":#headpats
            $ ainepoint += 1
            $ renpy.notify(ainenotif)
            $ aineheadpat = True
            mc "After only one day... Don't worry about it for now. I'm sure you'll get a response sooner or later."
            if ainecomfort:
                scene i271
                with dissolve
                mc "What did I tell you yesterday?"
                mc "Never let your problems take away your happiness, right?"
                mc "So cheer up already."
                a "Mnnh..."
                scene i272
                with dissolve
                a "{i}W-why does his hand feel so familiar? I feel so comfortable when he does this to me... Just like last time at the stairs.{/i}"
                a "{i}It's like I was used to it, but somehow forgot the feeling and having it again makes me miss it.{/i}"
                a "{i}I... don't get it...{/i}"
                a "A-alright..."
            else:
                scene i272
                with dissolve
                a "Mnnh..."
                a "{i}W-why does his hand feel so familiar? I feel so comfortable when he does this to me... Just like last time at the stairs.{/i}"
                a "{i}It's like I was used to it, but somehow forgot the feeling and having it again makes me miss it.{/i}"
                a "{i}I... don't get it...{/i}"
                a "A-alright..."
            mc "Good~!"
        "Don't do it{#ep1}":
            $ aineheadpat = False
            mc "Nope! I should just let her be."
    mc "I'll head to my room now, alright?"
    a "Sure, I have to go to the laundry room as well."
    mc "Okay."

    if aineheadpat:
        scene i273
        with dissolve
        mc "*sighs*"
        scene i274
        with flash
        a "{size=-10}*mumbles* N-nooo... d-don't hurt me... mom...{/size}"
        yt "Is she dreaming again? I can't hear what she's saying..."
        scene i275
        with flash
        yt "I shouldn't have done that back then..."
        yt "Now, it has become a muscle memory..."

    scene black
    with dissolve
    with fade

    scene i276
    with dissolve
    play sound 'audio/doorknock.mp3'
    mc "*knocks*"
    mc "Sky? Are you in there? I have your burgers!"
    s "Oh, hold on!"
    scene i277
    with dissolve
    play sound 'audio/opendoor.mp3'
    "*door opens*"
    mc "Here. We ran out of double cheeseburgers, so it's a double patty with lettuce and tomato this time."
    mc "You're good with it, right?"
    image smcbb:
        "i278.jpg"
        pause 3.0
        "i279.jpg"
        pause .2
        repeat
    show smcbb
    with dissolve
    s "Yeah! I still love them. Hehe."
    s "By the way have you seen Aine?"
    mc "She's downstairs I think. She told me earlier she was going to the laundry room. Not really sure about now."
    mc "Why?"
    s "I want to talk to her because there is an opening on my team."
    s "She told us she had experience with online teaching, right?"
    s "So I think she's the best one I could hire right now."
    mc "Wait a minute..."
    mc "You're already a team leader?!"
    s "Yup! *giggles*"
    mc "Since when?!"
    s "I didn't tell you, but I was just promoted last week."
    s "I was so busy that I didn't even have time to celebrate. Hehehe~"
    yt "She's working really hard... She definitely deserves at least a small celebration."
    yt "I think I should take her somewhere."
    yt "What should I tell her?"
    menu:
        "Tell her to celebrate":
            $ skycelebrate = True
            mc "Well then, would you like to go somewhere with me on my next day off?"
            image smcbb2:
                "i280.jpg"
                pause 3.0
                "i281.jpg"
                pause .2
                repeat
            show smcbb2
            with dissolve
            s "Really~?! Did you just ask me on a date?"
            mc "I did not! I'm just asking you to celebrate your promotion, that's all!"
            s "*giggles* There's nothing wrong with a date between childhood friends, you know?"
            s "And of course, I would love to!"
            mc "Do you have time, though? Saturday isn't your day off, right?"
            s "I don't have any days off, to be honest."
            s "But now that I'm a team leader, I have more flexibility and I can just take a one-day leave."
            mc "Isn't it supposed to be the other way around? Like the higher position, the busier it gets?"
            s "In some other jobs, that's usually the case. But we're different here."
            s "I'm still teaching classes, but most of the time I just have to supervise the team, submit a report of the day to our boss and that's all!"
            mc "That sounds nice, but is your boss okay with you taking a leave day?"
            s "Of course! And I won't turn you down if you're asking me on a date. *giggles*"
            mc "I told you, it's not a date!"
            s "Ehhh.... But I want it to be a date~!"
            mc "*sighs* Alright, alright... I won't argue."
            s "Great! Hehehe~"
        "Don't tell her":
            $ skycelebrate = False
            yt "Let's just leave her be for now. She might be too busy to accept it anyway."
            mc "I see."
            s "{i}Ehh... I was expecting him to ask me out... What a bummer!{/i}"

    image smcbb3:
        "i282.jpg"
        pause 3.0
        "i283.jpg"
        pause .2
        repeat
    show smcbb3
    with dissolve
    s "I'll go look for Aine, then. I need someone to fill the vacant spot as soon as possible."
    s "But... do you think she'll accept?"
    mc "To be honest, I'm not really sure. She came from a corporation. She might want something bigger."
    mc "But you won't know until you ask."
    s "I guess so... I'll talk to her now."
    mc "Sure!"
    yt "I need a quick nap, then. I'm pretty exhausted today."

    scene black
    with dissolve
    with fade

    scene i284
    with dissolve
    yt "If she's really looking for a job, she won't be too picky, right?"
    yt "I'm still mixed up about the past and present her, so I'm not really sure what to think of her yet."
    yt "I have so many questions in my head that I want to ask her."
    yt "......"
    yt "Should I risk it and just ask her directly? Or should I take it slow?"
    yt "......"
    yt "Risking it wouldn't be wise. And I still need her to prove herself to me, that's the plan."
    yt "I should just go with the flow however I can for now."
    yt "And, I'm sure I won't have any problem with Emma and Gwen."
    yt "I somehow got Emma in control now..."
    yt "I wonder where she is, though. I didn't see her when I came home."
    yt "......"
    scene i285
    with dissolve
    yt "!!!!"
    yt "Could she be spying on me again?!"
    scene i286
    play sound 'audio/woosh.mp3'
    mc "Emma?"
    scene i287
    play sound 'audio/woosh.mp3'
    mc "Emma?"
    scene i284
    play sound 'audio/chair.mp3'
    yt "No she's not... She's probably still working."
    yt "I also wonder why Gwen regrets what we did back then..."
    yt "....."
    yt "Aahhh~! So many questions! Forget about it and just take a nap!"
    yt "Wait, did Lily already send me the sleeping technique she was talking about?"
    yt "Let's check my phone."
    scene i288
    with dissolve
    yt "......"
    yt "Oh, great! Here it is! I need to try this out, now!"
    l "(Hello, [mc]~! Lily here, your Sleeping Guru!)"
    yt "Guru?"
    l "(Now, I shall teach you a special method to sleep within just ten seconds!)"
    yt "Just ten seconds?! That sounds too good to be true, Lily!"
    l "(I call it the 'Military Method'!)"
    yt "That... sounds very comforting..."
    l "(Step 1: Relax your entire face, including the muscles inside your mouth.)"
    l "(Step 2: Drop your shoulders to release the tension and let your hands drop to the side of your body.)"
    l "(Step 3: Exhale, relaxing your chest.)"
    l "(Step 4: Relax your legs, thighs, and calves.)"
    l "(Step 5: Say the words “don't think” over and over for 10 seconds.)"
    l "(And finally, you'll find yourself waking up from a very good sleep!)"
    play sound 'audio/chair.mp3'
    scene i289
    with dissolve
    yt "Alright, let's do the steps one to four at the same time."
    yt "And then..."
    scene i290
    with dissolve
    yt "Don't think, don't think, don't think, don't think, don't think, don't think, don't think...."
    yt "Don't..."
    yt "...think......"
    yt "......"

    scene black
    with dissolve
    with fadeq

    "Meanwhile..."

    scene black
    with dissolve
    with fadeq

    scene i291
    with dissolve
    s "There she is, watching TV."
    scene i292
    with dissolve
    s "Hey, Aine!"
    a "Hey, Sky! Do you need something?"
    s "I just want to ask you if you're still looking for a job."
    scene i293
    with dissolve
    a "Yeah... I am. I tried submitting my resume to a lot of companies, but there's still no response from them."
    s "Then, I have a possibility for you."
    a "A possibility? What is it?"
    scene i292
    with dissolve
    s "There's a vacant spot on my teaching team, and I'm looking for someone well suited for it. And I think you're that person!"
    s "You mentioned that you have experience with it before, right?"
    s "We can also save time training you since you already know what to do."
    s "But it's alright if you don't want it. It's not much compared to your previous job, after all."
    scene i294
    with dissolve
    a "Really?! No~! I'll gladly accept it, Sky!"
    s "Excellent!"
    a "I don't really mind if it's not that much. It's still a great job!"
    a "I told you that I loved doing it, right? So it's really not a problem for me. I'd be more than happy to be back doing online teaching."
    a "Thanks for the offer, Sky. That makes me feel a little bit better."
    scene i295
    with dissolve
    s "{i}A little bit? Does she still have problems aside from finding a job?{/i}"
    s "{i}I wonder... Is it about [mc]?{/i}"
    s "{i}I know that she gave [mc] a hard time during high school, but I wasn't there to help him since I was in an 'Girls-Only High School' before.{/i}"
    s "{i}I used to really hate her."
    s "{i}But now, I don't really have a problem with her and the idea of her and her friends staying here, since it was really a long time ago.{/i}"
    s "{i}[mc] and I are too mature now to even think about getting back at them or anything.{/i}"
    s "{i}And I'm pretty sure that they are okay with it too.{/i}"
    s "{i}As long as they don't do anything to [mc], then we're good.{/i}"
    s "{i}I sure hope you know what you're doing, Mom.{/i}"
    s "{i}Because if I happen to see any dirty tricks from them, there will be fire in this house.{/i}"
    scene i294
    with dissolve
    a "But wait... You said 'my team', right? Then, that means you're a team leader already?"
    s "Yeah! I didn't tell you yet, but I just got promoted recently. Hehe!"
    a "Wow~! Congrats! That's really impressive, Sky! It will be my pleasure to work under you."
    s "Thanks~!"
    a "So when can I start working?"
    s "Well... you need to have your own PC first. After that, you can start right away if you're ready."
    a "Oh, no problem, then. I'll just order a PC later so I can start tomorrow or the day after."
    s "Good idea! I'll leave that to you. Now I need to go back up and continue with my work."
    scene i296
    with dissolve
    a "Wait a minute, Sky..."
    a "Uhhmm... Can I have your hand for a moment?"
    s "Huh? My hand? Alright..."
    scene i297
    with dissolve
    a "Uhm..."
    s "{i}Ehh... What is she doing?{/i}"
    scene i298
    with dissolve
    a "{i}No, it's not the same at all. *sighs*{/i}"
    a "{i}The feeling is different when it's him...{/i}"
    a "T-thanks..."
    s "No problem. I'll go now."
    a "Sure!"
    scene i299
    with dissolve
    s "That was weird..."
    stop music fadeout 2

    scene black
    with Dissolve(2.0)
label ainepause:
    if _in_replay:
        $ name = persistent.gallery_name
    scene ainepause
    with dissolve
    $ renpy.pause()
    $ renpy.end_replay()
    play sound 'audio/gamepause.mp3'
    show title at move_slide
    with flash
    $ renpy.notify(imageunlock)
    $ renpy.pause()

    scene black
    with dissolve
    with fadeq

    "Later at dinner time..."

    scene black
    with dissolve
    with fadeq

    play music 'audio/YouAndMe.mp3'
    scene i300
    with dissolve
    s "Okay, dinner is almost ready. Can you get [mc] for me please, Aine?"
    s "Why is he still asleep at this time? Jeez!"
    a "Alright, I'll bring him down."

    scene black
    with dissolve
    with fade

    play sound 'audio/doorknock.mp3'
    scene i301
    with dissolve
    a "*knocks*"
    a "[mc]? Dinner is ready!"
    "......"
    a "{i}He's not answering. Maybe he's still asleep?{/i}"
    scene i302
    with dissolve
    a "{i}His door is open...{/i}"
    a "{i}I shouldn't enter someone's room like this, but he can't just sleep all night on an empty stomach.{/i}"
    play sound 'audio/opendoor.mp3'
    scene i303
    with dissolve
    "*door opens*"
    a "[mc]?"
    scene i304
    with dissolve
    a "Yeah, he's still asleep. He must've been really tired."
    a "I need to wake him up."
    scene i306
    with dissolve
    a "*shake* [mc]..."
    a "Wake up, [mc]. The dinner is ready!"
    mc "Mmmnnn? Sky?"
    scene i305
    with dissolve
    a "No, this is Aine. You need to wake up! You can't go all night with an empty stomach!"
    scene i307
    with dissolve
    scene i308
    with hpunch
    a "*moans* M-mmnnhh~!"
    mc "Mmm... 5 more minutes, Sky..."
    mc "......"
    mc "Why is your head... so smooth and squishy?"
    mc "*squish* *squish*"
    scene i309
    with dissolve
    a "*moans* Aahhh~! Hnngg~!"
    yt "!!!!"
    yt "Wait... this isn't Sky!"
    scene i310
    play sound 'audio/woosh.mp3'
    yt "Who is..."
    scene i311
    with dissolve
    a "Mm! *sniffs* *sobs*"
    mc "What the... Aine?!"
    a "Mm!! *sobs*"
    mc "What are you-"
    scene black
    a "*crying* WHAAAAAAA~!!"
    play sound 'audio/slap.mp3'
    a "*slap*!!" with hpunch
    mc "Aww!"

    jump ep2
