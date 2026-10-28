label chapter_5:
    #Make gallery save-independent:
    if succubus_incountered >= 1:
        $ persistent.g_1to3_unlock = 1
    if g_4_unlock >= 1:
        $ persistent.g_4_unlock = 1
    if g_5_unlock >= 1:
        $ persistent.g_5_unlock = 1
    if g_6_unlock >= 1:
        $ persistent.g_6_unlock = 1
    if g_7_unlock >= 1:
        $ persistent.g_7_unlock = 1
    if g_8_unlock >= 1:
        $ persistent.g_8_unlock = 1
    if g_9_unlock >= 1:
        $ persistent.g_9_unlock = 1
    if g_10_unlock >= 1:
        $ persistent.g_10_unlock = 1
    if g_11_unlock >= 1:
        $ persistent.g_11_unlock = 1
    $ renpy.save_persistent()
    $ chapter = 5
    $ athena_met = 1
    $ artemis_met = 1
    define misty_met = 0
    define toni = Character("Toni", color = "90bf02")
    define erwin = Character("Erwin", color = "f5f2bc")
    define tomas = Character("Tomas", color = "ccaf7a")
    define frankie = Character("Frankie", color = "587d24")
    define frd = Character("Friedrich", color = "bfbfbf")
    define mikel = Character("Mikel", color = "8ba33c")
    define johann = Character("Johann", color = "363636")
    define serena = Character("Serena", color = "0093c4")
    define misty = Character("Misty", color = "a80035")
    define daiana = Character("Daiana", color = "356f82")
    define jamie = Character("Jamie", color = "ffd60a")
    define toni_info = 0
    define erwin_info = 0
    define frankie_info = 0
    define johann_info = 0
    define serena_info = 0
    define misty_info = 0
    define daiana_info = 0
    define jamie_info = 0
    define sus_open = 0
    define suspect_initial = 0
    define jamie_initial = 0
    image v5m1 = Movie(size = (1920,1080), channel="movie", play="0.5/video/v5m1.webm", loop=True)
    image v5m2 = Movie(size = (1920,1080), channel="movie", play="0.5/video/v5m2.webm", loop=True)
    image v5m3 = Movie(size = (1920,1080), channel="movie", play="0.5/video/v5m3.webm", loop=True)
    image v5m4 = Movie(size = (1920,1080), channel="movie", play="0.5/video/v5m4.webm", loop=True)
    image v5m5 = Movie(size = (1920,1080), channel="movie", play="0.5/video/v5m5.webm", loop=True)
    image v5m6 = Movie(size = (1920,1080), channel="movie", play="0.5/video/v5m6.webm", loop=True)
    image v5m7 = Movie(size = (1920,1080), channel="movie", play="0.5/video/v5m7.webm", loop=True)
    image v5m7_2 = Movie(size = (1920,1080), channel="movie", play="0.5/video/v5m7_2.webm", loop=True)
    image v5m8 = Movie(size = (1920,1080), channel="movie", play="0.5/video/v5m8.webm", loop=True)
    image v5m9 = Movie(size = (1920,1080), channel="movie", play="0.5/video/v5m9.webm", loop=True)
    image v5m10 = Movie(size = (1920,1080), channel="movie", play="0.5/video/v5m10.webm", loop=True)
    image v5m11 = Movie(size = (1920,1080), channel="movie", play="0.5/video/v5m11.webm", loop=True)
    image v5m12 = Movie(size = (1920,1080), channel="movie", play="0.5/video/v5m12.webm", loop=True)
    image v5m13 = Movie(size = (1920,1080), channel="movie", play="0.5/video/v5m13.webm", loop=True)
    image v5m14 = Movie(size = (1920,1080), channel="movie", play="0.5/video/v5m14.webm", loop=True)
    image v5m15 = Movie(size = (1920,1080), channel="movie", play="0.5/video/v5m15.webm", loop=True)
    image v5m16 = Movie(size = (1920,1080), channel="movie", play="0.5/video/v5m16.webm", loop=True)
    image v5m17 = Movie(size = (1920,1080), channel="movie", play="0.5/video/v5m17.webm", loop=True)
    image v5m18 = Movie(size = (1920,1080), channel="movie", play="0.5/video/v5m18.webm", loop=True)
    image v5m19 = Movie(size = (1920,1080), channel="movie", play="0.5/video/v5m19.webm", loop=True)
    image v5m20 = Movie(size = (1920,1080), channel="movie", play="0.5/video/v5m20.webm", loop=True)
    image v5m21 = Movie(size = (1920,1080), channel="movie", play="0.5/video/v5m21.webm", loop=True)
    image v5m22 = Movie(size = (1920,1080), channel="movie", play="0.5/video/v5m22.webm", loop=True)
    image v5m23 = Movie(size = (1920,1080), channel="movie", play="0.5/video/v5m23.webm", loop=True)
    image v5m24 = Movie(size = (1920,1080), channel="movie", play="0.5/video/v5m24.webm", loop=False)
    image v5m25 = Movie(size = (1920,1080), channel="movie", play="0.5/video/v5m25.webm", loop=True)
    image v5m26 = Movie(size = (1920,1080), channel="movie", play="0.5/video/v5m26.webm", loop=True)
    define persistent.g_12_unlock = 0
    define persistent.g_13_unlock = 0
    define persistent.g_14_unlock = 0
    define persistent.g_15_unlock = 0
    define persistent.g_16_unlock = 0
    define persistent.g_17_unlock = 0
    #The chapter starts here
    pause(1.5)
    scene black with fade
    scene chapter_5 with dissolve
    $ renpy.pause(3, hard=True)
    play background_s2 "audio/Ambient_ninja_village.mp3" volume 0.4 fadeout 1.0 fadein 1.0 loop
    scene v54 with Dissolve(1.0)
    pause(1.0)
    scene v51 with Dissolve(1.0)
    pause(1.0)
    z "(So, this is Esyl...)"
    play music "audio/Esyl.mp3" volume 0.4 fadeout 1.0 fadein 1.0 loop
    scene v53 with dissolve
    z "(I suppose it looks more cheerful than the town of the faceless god...)"
    scene v55 with dissolve
    z "(And it looks like those two weren't that traumatised by the whole experience... That's good.)"
    scene v58 with dissolve
    z "Something interesting?"
    scene v510 with dissolve
    tr "What kind of fruit do you figure that is?"
    scene v59 with dissolve
    z "The round green one?"
    scene v511 with dissolve
    cndy "Yeah. We didn't have that in Kalytro."
    scene v59 with dissolve
    z "I don't think I've seen it before..."
    scene v56 with dissolve
    Character("Man") "Hello there!"
    scene v57 with dissolve
    z "Hello to you. Would this be your store, sir?"
    scene v56 with dissolve
    Character("Man") "But sir Friedreich, you already know this! It's me, Toni!"
    scene v57 with dissolve
    z "Huh? (Friedreich?)"
    scene v56 with dissolve
    toni "By the way. You look thirty years younger already. You see? Toni's face cream work like magic! You must listen to what Toni say."
    toni "You come to see Toni's wares, lady Karolina and lord Mikel? Toni very happy to see you."
    scene v57 with dissolve
    z "(Oh... He thinks we're-)"
    scene v513 with dissolve
    cndy "Oh. Actually, I'm not really Karolina."
    scene v514 with dissolve
    tr "We're only escorting-"
    scene v515
    play audio "audio/Slap2.mp3"
    with vpunch
    z "!"
    scene v516 with dissolve
    z "I'm sorry mister Toni. It seems the young lady and her brother aren't feeling well this afternoon. Hehehehe..."
    z "They had a heavy breakfast at the mansion and they kept spouting nonsense ever since."
    scene v517 with dissolve
    z "*Whispering. Are you two dumb or something?! The mission isn't over until we deliver Karolina back to her mansion! So stay in character!"
    scene v518 with dissolve
    z "..."
    scene v519 with dissolve
    a "What are you three doing?"
    scene v520 with vpunch
    Character("All three") "Nothing!"
    scene v521 with dissolve
    a "..."
    scene v522 with dissolve
    toni "Oh!"
    toni "You. Lady in the back! Could you be..."
    scene v524 with dissolve
    krlna "!"
    scene v523 with dissolve
    toni "..."
    scene v525 with dissolve
    krlna "Uhm... Yes? Can I help you, sir?"
    scene v526 with dissolve
    toni "..."
    scene v527 with dissolve
    toni "..."
    scene v529 with dissolve
    toni "Oh! Toni knows!"
    scene v528 with dissolve
    krlna "..."
    scene v529 with dissolve
    toni "You are..."
    scene v528 with dissolve
    krlna "..."
    scene v529 with dissolve
    toni "You are..."
    scene v530 with vpunch
    toni "A tourist!"
    scene v531 with dissolve
    krlna "H-Huh?! Uhm... Yeah... E-Exactly..."
    scene v532 with dissolve
    toni "Can Toni interest you in orange candy bar? Expensive, but very fresh and tasty!"
    scene v533 with dissolve
    z "Those things don't look fresh at all..."
    scene v534 with dissolve
    toni "Nonsense! Verrrrry fresh..."
    play music "audio/creepy ambient 3.mp3" fadeout 1.0 fadein 1.0 loop
    play background_s "audio/flies.mp3" volume 0.2 fadeout 1.0 fadein 1.0 loop
    scene v535 with Dissolve(1.0)
    ""
    play music "audio/Esyl.mp3" volume 0.8 fadeout 1.0 fadein 1.0 loop
    stop background_s fadeout 1.0
    scene v536 with dissolve
    toni "Will you take candy bar, sir Friedreich?"
    scene v537 with dissolve
    z "Uhm... I think I'll pass..."
    scene v538 with dissolve
    cndy "I'll take one!"
    scene v539 with dissolve
    tr "Me too."
    scene v540 with dissolve
    z "..."
    scene v541 with Fade(0.5,0.5,0.5)
    pause(1.0)
    scene v542 with Dissolve(1.0)
    pause(1.0)
    scene v543 with Dissolve(1.0)
    pause(1.0)
    scene v544 with dissolve
    tr "Oh, look! That store has some cool stuff!"
    scene v545 with dissolve
    tr "Let's go check it out!"
    scene v546 with dissolve
    tr "..."
    scene v547 with dissolve
    toni "Hello and welcome to Toni's second store. Do you want orange candy ball?"
    scene v548 with dissolve
    pause(1.0)
    scene v549 with dissolve
    a "..."
    scene v5281 with Fade(0.5,0.5,0.5)
    tr "These paintings are really cool..."
    cndy "Yeah..."
    scene v5282 with dissolve
    Character("Man") "You flatter me, tasteful young ladies."
    scene v5283 with dissolve
    Character("Man") "Allow me to welcome you to Esyl."
    scene v5284 with dissolve
    pause(1.0)
    scene v5285 with dissolve
    erwin "The name's Erwin Schmidt. I work as an artist here."
    scene v5286 with dissolve
    cndy "Pleasure to meet you."
    scene v5285 with dissolve
    erwin "Might I ask young lady. Why are you dressed like the young lady Schwartz?"
    scene v5287 with dissolve
    krlna "They're simply escorting me, Erwin. We switched clothes and for my protection."
    scene v5288 with dissolve
    erwin "Lady Schwartz! Pardon my intrusion on your affairs. How was your trip, my lady?"
    scene v5287 with dissolve
    krlna "It was very enjoyable. Thanks for asking."
    scene v5289 with dissolve
    z "So you're the one that drew all these paintings? You're quite good."
    scene v5290 with dissolve
    krlna "Erwin is the city's best artist. Even mother really likes his drawings, and you wouldn't believe how picky she is."
    scene v5291 with dissolve
    erwin "I thank you, young sir. You are most kind."
    erwin "Seeing how you're the party escorting the young lady Schwartz. Would you care for a painting of you together to remember your time here in Esyl?"
    scene v5292 with dissolve
    cndy "You'd paint us?! That'd be-"
    scene v5293 with vpunch
    a "Hold up! Hold up! How much exactly is this going to cost me?"
    scene v5294 with dissolve
    erwin "*Laughs softy. No. This one is on the house."
    scene v5295 with dissolve
    a "..."
    scene v5296 with dissolve
    a "Well... In that case..."
    scene black with fade
    pause(1.0)
    scene v5297 with dissolve
    ""
    pause(1.0)
    stop music fadeout 1.0
    scene v550 with Dissolve(1.0)
    pause(1.0)
    scene v551 with Dissolve(1.0)
    pause(1.0)
    scene v552 with dissolve
    z "(looks like a nice place to sit down and rest a bit before we head to the mansion.)"
    scene v553 with dissolve
    z "(But there's this weird looking guy...)"
    scene v554 with dissolve
    pause(1.0)
    scene v555 with dissolve
    Character("Weird looking guy") "Interesting outfits. Karolina's escorts, I presume?"
    scene v554 with dissolve
    z "(Huh?! How did he-)"
    play music "audio/The butcher of Esyl.mp3" volume 0.8 fadeout 1.0 fadein 1.0 loop
    stop background_s fadeout 1.0
    stop background_s2 fadeout 1.0
    scene v556 with dissolve
    a "May I ask, Who you would be, sir?"
    scene v557 with dissolve
    Character("Weird looking guy") "If you'd sit down. I will answer any questions you have."
    scene v559 with dissolve
    a "..."
    scene v560 with dissolve
    a "Alright."
    scene v561 with dissolve
    z "..."
    scene v562 with Fade(0.5,0.5,0.5)
    pause(1.0)
    scene v563 with dissolve
    a "How did you know who we were?"
    scene v564 with dissolve
    Character("Weird looking guy") "I will answer your questions in a second. But first..."
    Character("Weird looking guy") "How was your trip, Karolina?"
    scene v566 with dissolve
    krlna "It was really fun. Thanks for asking, uncle Tomas."
    scene v567 with dissolve
    pause(1.5)
    scene v568
    play sound "audio/RecordScratch (thanks senpai).ogg"
    stop music
    with vpunch
    Character("All") "UNCLE TOMAS?!"
    scene v569 with dissolve
    krlna "Yeah... That's my uncle. Tomas Schwartz. He's the city's chief detective."
    scene v570 with dissolve
    tomas "Interesting party you have there, Karolina. Who are these people?"
    scene v571 with dissolve
    krlna "They're ninjas from the northern village."
    scene v570 with dissolve
    tomas "Ninjas, huh?"
    scene v574 with dissolve
    a "Chief detective, did you say?"
    scene v573 with dissolve
    tomas "Yes. That'd be me."
    scene v574 with dissolve
    a "Then you'd know about the butcher, I take it?"
    play music "audio/The butcher of Esyl.mp3" volume 0.8 fadeout 1.0 fadein 1.0 loop
    scene v572 with dissolve
    z "The butcher?"
    scene v575 with dissolve
    a "A serial killer in this city who's known by the name 'the butcher'. My sister was sent to deal with him, but she couldn't do it. Said she barely escaped with her life."
    scene v573 with dissolve
    tomas "Your sister? The ninja girl Yumi is your sister?"
    scene v574 with dissolve
    a "Yeah."
    scene v573 with dissolve
    tomas "Well, even though it's true that Yumi didn't kill him. He's been a lot less active of late."
    tomas "Seems your sister did as much damage as she took."
    scene v574 with dissolve
    a "Is that so? That's good to hear..."
    scene v573 with dissolve
    tomas "How is she? She left here before her injuries were healed. The doctor insisted that she stays a few more days, but she didn't listen."
    scene v574 with dissolve
    a "She's fine, doing a lot better now."
    a "When you said the butcher is less active... Does that mean he's still killing people?"
    scene v573 with dissolve
    tomas "Yes... I'm afraid so..."
    scene v574 with dissolve
    a "But why not hire someone to finish the job?"
    scene v573 with dissolve
    tomas "My brother wouldn't have it. Said he already spent enough on this nonsense..."
    a "..."
    tomas "At any rate, whilst you're here, I suggest women don't go out at night. Not alone at least."
    play sound "audio/Cloth_rustle.wav"
    scene v576 with dissolve
    tomas "And if you spot someone that looks like this at night, run!"
    scene v577 with dissolve
    a "Is this what he looks like?"
    scene v576 with dissolve
    tomas "Yes. According to the accounts of some witnesses. Erwin, the city's best artist, helped provide this drawing."
    scene v578 with dissolve
    z "What a creepy costume... What's that on his head?"
    scene v579 with dissolve
    tomas "A hood of some sort. He wears it to hide his identity, of course."
    scene v578 with dissolve
    z "(Makes sense, if he's going to live here amongst the others, I suppose...)"
    z "(Which means he could be anyone.)"
    z "(He seems on the fat side, I suppose. But that doesn't really help...)"
    play sound "audio/Cloth_rustle.wav"
    scene v580 with dissolve
    tomas "Well... I'll get out of your hair."
    play sound "audio/chair.mp3"
    scene v581 with dissolve
    tomas "I wish you a good stay here in town. Just watch yourselves and you'll be fine."
    scene v582 with dissolve
    a "We will. Thank you sir."
    scene v583 with dissolve
    pause(0.3)
    scene v584 with dissolve
    pause(1.0)
    z "So, this guy is really dangerous, right? If even Yumi couldn't deal with him..."
    scene v585 with dissolve
    a "Yes. You three should definitely stay clear of him."
    scene v584 with dissolve
    a "..."
    z "Say... You're not going to try to catch him yourself, are you?"
    scene v586 with dissolve
    a "Hmm... Unlikely that I'll get the chance, I'm afraid. If he's really good, he'll probably be smarter than to go anywhere near me."
    scene v587 with dissolve
    z "Yeah... I see your point..."
    z "..."
    scene test_203 with Dissolve(2.0)
    pause(1.0)
    z "(Could it be... that when I found her back then...)"
    scene v587 with Dissolve(2.0)
    a "..."
    scene v588 with dissolve
    a "Something on your mind?"
    scene v587 with dissolve
    z "Uhm... Well, it's just that... I remembered how injured Yumi was the first time I met her. Was that after she fought this butcher guy?"
    scene v588 with dissolve
    a "Yeah... You found her on her way back from Esyl."
    scene v587 with dissolve
    z "..."
    z "(Damn... Yumi seemed really strong last time when I sparred with her. To think this butcher guy managed to do this much damage to her... And to carry on with his killings after...)"
    z "(I wonder... if I could take him in a fight...)"
    scene v589 with dissolve
    a "Yumi could've taken him. If only that coward didn't only show up at night."
    scene v587 with dissolve
    z "At night?"
    scene v588 with dissolve
    a "Yeah. Yumi and I are stronger under the sun."
    scene v587 with dissolve
    z "You are? How come? You're both humans, right?"
    scene v588 with dissolve
    a "Yeah. But our older brother is the son of Helios, god of the sun."
    scene v589 with dissolve
    a "Mortals who have children with gods like my mother are sometimes blessed after. So their later children might receive small amounts of power from that god."
    scene v587 with dissolve
    z "Is that so... I didn't know that."
    z "..."
    z "(Wait! Does that mean when she fought Athena, she wasn't even at full strength?!)" with vpunch
    stop background_s fadeout 1.0
    stop background_s2 fadeout 1.0
    stop sound fadeout 1.0
    stop music fadeout 1.0
    scene v590 with dissolve
    "Hello and welcome."
    $ misty_met = 1
    scene v591 with dissolve
    misty "My name is Misty and this is my humble shop."
    play music "audio/Misty's theme.mp3" volume 0.8 fadeout 1.0 fadein 1.0 loop
    z "(Uhm... What exactly is she... A demi-human of some sort?)"
    scene v592 with dissolve
    a "Oh... Hello, Misty."
    scene v591 with dissolve
    misty "Sorry to startle you. I know it's rare to see my kind in human settlement."
    scene v592 with dissolve
    a "No, no. Nothing like that. I was just lost in my thoughts."
    scene v591 with dissolve
    misty "Is that so? Can I get you something to drink? Perhaps some tea to ease your nerves, miss..."
    scene v592 with dissolve
    a "Anabelle. And Yeah, I think I'll have one. Thanks."
    scene v591 with dissolve
    misty "Certainly."
    scene v594 with dissolve
    misty "And you? Can I get you anything ladies and gentlemen?"
    scene v593 with dissolve
    cndy "I'll have what Anabelle is having."
    tr "Me too."
    krlna "I'll have one with honey, please."
    scene v594 with dissolve
    misty "And you, sir? Would you like anything?"
    scene v593 with dissolve
    z "Uhm... Let's just go with tea."
    z "(I suppose a tea shop keeper where people come often to chat could be a good source of info.)"
    define choice5_1 = 0
    define choice5_2 = 0
    define choice5_3 = 0
    define misty_q1 = 0
    define misty_q2 = 0
    define misty_q3 = 0
    define misty_q4 = 0
    define misty_q5 = 0
    define misty_q6 = 0
    define misty_q7 = 0
    menu:
        "Ask her a few questions.":
            z "Do you mind if I ask you a few questions?"
            scene v594 with dissolve
            misty "Of course not. Shoot!"
            scene v593 with dissolve
            menu ch5_misty1:
                "Ask about the city." if choice5_1 < 2:
                    z "Being a tea shop keeper, you probably know a lot about the city, right?"
                    scene v594 with dissolve
                    misty "You could say that. Do you have something specific in mind?"
                    scene v593 with dissolve
                    menu ch5_misty2:
                        "Which god does the city worship?" if misty_q1 <> 1:
                            $ choice5_1 += 1
                            $ misty_q1 = 1
                            z "Which god or gods does this city worship?"
                            scene v594 with dissolve
                            misty "There are two temples, one of Dionysus and another of Hermes, I believe."
                            misty "I'm not entirely sure who worships whom, though. And I've never been to any of the temples."
                            scene v593 with dissolve
                            z "I see..."
                            jump ch5_misty2
                        "Any places around here that are worth visiting?" if misty_q2 <> 1:
                            $ choice5_1 += 1
                            $ misty_q2 = 1
                            z "Do you recommend any place we should visit while we're here?"
                            scene v594 with dissolve
                            misty "Well, I might go see the temples if I were you. That aside, the Schwartz mansion, perhaps. Exploring the market might also be worth
                            your time. But stay away from Toni..."
                            scene v593 with dissolve
                            z "Yeah... I got that Idea..."
                            jump ch5_misty2
                        "Change the subject.":
                            $ dummy += 1
                    jump ch5_misty1
                "Ask about the murders." if choice5_2 < 2:
                    z "Can I ask you about the murders that have been going on around here?"
                    scene v594 with dissolve
                    misty "The murders, you say? Yes? What did you want to ask?"
                    scene v593 with dissolve
                    menu ch5_misty3:
                        "Did you know any of the victims?" if misty_q3 <> 1:
                            $ choice5_2 += 1
                            $ misty_q3 = 1
                            z "Did you know any of the victims?"
                            scene v594 with dissolve
                            misty "Yes, I did. One of them was a frequent costumer here. Her name was Riena..."
                            scene v593 with dissolve
                            z "Oh... Sorry to hear that."
                            jump ch5_misty3
                        "Do you feel safe here?" if misty_q4 <> 1:
                            $ choice5_2 += 1
                            $ misty_q4 = 1
                            z "With all the murders going on, do you feel safe around here?"
                            scene v594 with dissolve
                            misty "I only open the shop during the day. The butcher never shows his face before sunset. So, for most part, yes."
                            scene v593 with dissolve
                            z "That's reassuring, I suppose..."
                            jump ch5_misty3
                        "Change the subject.":
                            $ dummy += 1
                    jump ch5_misty1
                "Ask about her." if choice5_3 < 3:
                    z "May I ask a few questions about you?"
                    scene v594 with dissolve
                    misty "*Giggles. About me? That's flattering. Ask away."
                    scene v593 with dissolve
                    menu ch5_misty4:
                        "How long have you been living in Esyl?" if misty_q5 <> 1:
                            $ misty_q5 = 1
                            $ choice5_3 += 1
                            z "How long have you been living in Esyl, if I may ask?"
                            scene v594 with dissolve
                            misty "I was born here. And I've lived here all my life. I've never left Esyl."
                            scene v593 with dissolve
                            jump ch5_misty4
                        "How did you get to have a tea shop?" if misty_q6 <> 1:
                            $ misty_q6 = 1
                            $ choice5_3 += 1
                            z "How did you get to have this place?"
                            scene v594 with dissolve
                            misty "My mother left it to me. She bought the place some thirty years ago, I believe."
                            scene v593 with dissolve
                            jump ch5_misty4
                        "What exactly is your race, if I may ask?" if misty_q7 <> 1:
                            $ misty_q7 = 1
                            $ choice5_3 += 1
                            z "Uhm... I don't mean to be rude, but... What exactly are you?"
                            scene v594 with dissolve
                            misty "I am half beast, half human or what some would call a demi-human. My father was a beast, while my mother was a human."
                            scene v593 with dissolve
                            jump ch5_misty4
                        "Change the subject.":
                            $ dummy += 1
                    jump ch5_misty1
                "Enough questions.":
                    $ dummy += 1
        "Don't.":
            $ dummy += 1
    play sound "audio/pick up 2.mp3"
    scene v595 with dissolve
    misty "Anything else?"
    scene v597 with dissolve
    z "I'm good for now, thanks."
    scene v596 with dissolve
    misty "Very well. I'll be back with your drinks shortly."
    scene v598 with dissolve
    pause(0.3)
    scene v599 with dissolve
    pause(1)
    scene v5101 with dissolve
    z "So, next stop is the mansion, I take it."
    scene v5102 with dissolve
    a "Yeah. It's an hour's walk from here, so let's drink our teas first."
    scene v5101 with dissolve
    pause(1)
    stop background_s fadeout 1.0
    stop background_s2 fadeout 1.0
    stop music fadeout 1.0
    stop sound fadeout 1.0
    scene v5103 with Fade(0.5,0.5,0.5)
    pause(1)
    play music "audio/Esyl.mp3" volume 0.8 fadeout 1.0 fadein 1.0 loop
    scene v5105 with dissolve
    z "And? Once Karolina's back home safe, what then? Do we go home right away?"
    scene v5104 with dissolve
    a "We should probably stay the night here at least. We can begin the journey back fresh in the next morning."
    scene v5107 with dissolve
    a "The mission has been unexpectedly intense as it is, so let's try to take it easy."
    scene v5106 with dissolve
    cndy "Yeah. To be honest with you, that faceless god town was pretty scary... I still feel a bit tense even now."
    play sound "audio/RecordScratch (thanks senpai).ogg"
    stop music
    scene v5108
    Character("Elf") "Perhaps a song to calm the nerves then?"
    scene v5109
    play sound "audio/chair squeak.mp3"
    with vpunch
    cndy "EEEK! Where did you come from?! Who are you?!"
    frankie "Frankie's the name. I am a bard. What song would you like to hear?"
    scene v5110 with dissolve
    tr "Oh? A wood elf?! You're from the west, aren't you?"
    scene v5111 with dissolve
    frankie "Why, yes! Would you like to hear a song from there?"
    scene v5112 with dissolve
    tr "Yeah! I'd love to."
    scene v5113 with dissolve
    frankie "Great! The song of the flying leaves it is then!"
    play music "audio/Frankie's theme.mp3" volume 0.4 fadeout 1.0 fadein 1.0 loop
    show v5m1 with dissolve
    frankie "♫The leaf falls from the tree...♫"
    frankie "♫The wind carries her...♫"
    frankie "♫She lands on another tree...♫"
    frankie "♫But the wind won't let go of her...♫"
    frankie "♫It pushes her again, off the tree and around the cemetery...♫"
    frankie "♫The leaf is flying through the air...♫"
    frankie "♫Faster than a bird and just as free...♫"
    frankie "♫The leaf is flying without a care...♫"
    frankie "♫But she misses her time on the tree...♫"
    scene v5117 with dissolve
    z "(Gods... This is horrible...)"
    scene v5116 with dissolve
    z "(Everyone seems uncomfortable...)"
    scene v5118 with dissolve
    z "(Torr seems to like it though.)"
    hide v5m1
    show v5m1 with dissolve
    frankie "♫The leaf that fell from the tree...♫"
    frankie "♫Is now a hostage of the air...♫"
    frankie "♫That pushed her not one time but three...♫"
    frankie "♫And she wonders now if her fate is fair...♫"
    frankie "♫I hope you enjoyed my song very...♫"
    scene v5121 with dissolve
    frankie "♫...much my ladies and my good sir...♫"
    stop music fadeout 2.0
    scene v5120 with dissolve
    z "(Ugh...)"
    pause(1.0)
    define tipped_frankie = 0
    menu:
        "[ModGreen]Tip him. (Torr Love +1)":
            $ tipped_frankie = 1
            play sound "audio/coin.mp3"
            scene v5122 with dissolve
            z "Well, yes... Thank you, Frankie. Here you go."
            scene v5124 with dissolve
            frankie "Thank you very much, kind sir."
            scene v5127 with dissolve
            tr "Take care, Frankie."
            scene v5128 with dissolve
            pause(0.3)
            scene v5129 with dissolve
            tr "..."
            $ tr_aff += 1
            show screen button_aff with dissolve
            play sound "audio/stats.wav"
            hide screen button_aff with dissolve
            pause(0.5)

        "Don't.":
            scene v5123 with dissolve
            z "Uhm... Well... Thanks, Frankie."
            scene v5125 with dissolve
            frankie "You're welcome."
            scene v5126 with dissolve
            tr "Take care, Frankie."
            scene v5128 with dissolve
            pause(0.3)
            scene v5130 with dissolve
            tr "..."
            pause(1)
    scene black with fade
    pause(1)
    stop background_s fadeout 1.0
    stop background_s2 fadeout 1.0
    stop music fadeout 1.0
    stop sound fadeout 1.0
    pause(2.5)
    play background_s2 "audio/Ambient_ninja_village.mp3" volume 0.7 fadeout 1.0 fadein 1.0 loop
    play music "audio/Mansion.mp3" volume 0.25 fadeout 1.0 fadein 1.0 loop
    scene v5131 with dissolve
    z "(So, this is the mansion... It looks really nice...)"
    scene v5132 with dissolve
    z "(There seems to be quite a few servants... There's this huge guy at the door...)"
    scene v5133 with dissolve
    z "(And there's someone working in the garden...)"
    scene v5134 with dissolve
    z "(Hold on...)"
    scene v5135 with dissolve
    z "(Is that...)"
    scene v5136 with dissolve
    z "(Toni! What's he doing here?! Does he work everywhere...)" with vpunch
    scene v5137 with dissolve
    z "..."
    z "(Carrying on...)"
    scene v5138 with dissolve
    z "... (He looks familiar...)"
    z "(Wait! Is this who I'm supposed to be?! He's huge! And so old!)" with vpunch
    scene v5139 with dissolve
    frd "Welcome home, young mistress."
    frd "You look... a bit different..."
    scene v5140 with dissolve
    krlna "It's me, Friedrich. Karolina. The girl wearing my clothes is one the people escorting me."
    scene v5141 with dissolve
    frd "Ah... Of course. I beg your pardon, young mistress. My eyes don't see very well these days."
    scene v5142 with dissolve
    frd "Welcome to the Schwartz estate. The mistress is expecting you. Please, go on inside."
    stop background_s fadeout 1.0
    stop background_s2 fadeout 1.0
    scene v5145 with Fade(0.5,1.0,0.5)
    z "(Wow... So pretty... And her outfit is so...)"
    z "(...liberal...)"
    z "(Is this Karolina's mother? She looks a bit too young.)"
    scene v5144 with dissolve
    daiana "Welcome to the Schwartz estate. I'm Daiana, the head maid."
    scene v5143 with dissolve
    z "(Oh... She's just the maid...)"
    play sound "audio/creaky door.mp3"
    scene v5146 with dissolve
    Character("Boy") "Daiana! Daiana!"
    scene v5147 with dissolve
    Character("Boy") "Where did you put my toys?! I can't find them anywhere!"
    scene v5148 with dissolve
    daiana "Did you check your closet?"
    scene v5147 with dissolve
    Character("Boy") "I did! They weren't-"
    scene v5149 with dissolve
    krlna "Mikel!"
    scene v5150 with dissolve
    krlna "Come here and give me a hug, you cute little bear!"
    mikel "Karolina! You're back!"
    scene v5151 with dissolve
    krlna "Aww... I missed you..."
    scene v5152 with dissolve
    tr "Hold on... Did she just say..."
    scene v5153 with Dissolve(2.0)
    tr "*Gasps."
    scene v5154 with dissolve
    pause(0.5)
    tr "I'm s-supposed to be that thing?!" with vpunch
    scene v5155 with dissolve
    z "Dude! Keep your voice down!"
    scene v5156 with dissolve
    tr "..."
    scene v5151 with dissolve
    z "(I mean... She does have a point though...)"
    scene v5157 with Dissolve(2.0)
    a "Are you finished, miss Karolina?"
    scene v5158 with dissolve
    krlna "Yeah... I'm not the best artist, but this is more or less how they look like."
    scene v5159 with dissolve
    pause(1.5)
    scene v5162 with Dissolve(2.0)
    z "..."
    scene v5160 with dissolve
    krlna "Everyone, meet my cute and sweet little brother Mikel. Say hi to them, Mikel."
    scene v5161 with dissolve
    mikel "Hi..."
    scene v5162 with dissolve
    z "..."
    scene v5163 with dissolve
    z "(Wait a second...)"
    z "(Now that I look at him... He looks a bit like...)"
    scene v5164 with Dissolve(2.0)
    z "Toni!" with vpunch
    scene v5165 with dissolve
    daiana "Uhh... Did you say something, sir?"
    scene v5166 with dissolve
    z "(Shit! Did I say that out loud?!)"
    z "(Think! Quick!)"
    scene v5167 with dissolve
    z "N-No... It's just that... These paintings! Yes! The paintings are very interesting..."
    scene v5168 with dissolve
    daiana "Yes, they are. The mistress likes them very much."
    scene v5169 with dissolve
    daiana "You have a very good taste, sir."
    scene v5170 with dissolve
    daiana "If you would follow me to the dining hall now. The mistress is waiting for you there."
    scene v5171 with dissolve
    pause(1.0)
    scene v5172 with Fade(0.5,1.0,0.5)
    pause(1.0)
    scene v5173 with dissolve
    z "(So that's Karolina's mother. She has to be.)"
    scene v5174 with dissolve
    serena "Welcome to my house. I'm Serena. The wife of Johann Schwartz, jarl of Esyl. I hope your journey here wasn't too tiring. Please, sit down."
    scene v5175 with dissolve
    z "..."
    scene v5176 with Fade(0.5,0.5,0.5)
    pause(1.0)
    scene v5177 with dissolve
    serena "Karolina, come hug your mother, child."
    play sound "audio/Cloth_rustle.wav"
    scene v5178 with dissolve
    serena "My sweet girl..."
    scene v5179 with dissolve
    serena "Your brother and I missed you a lot, sweet child."
    scene v5180 with dissolve
    krlna "I missed you too, mother. A lot..."
    scene v5179 with dissolve
    serena "Go sit down for dinner for now. We'll talk further tomorrow, alright."
    scene v5180 with dissolve
    krlna "Okay."
    scene v5177 with dissolve
    serena "I thank you for bringing my daughter back to me safely."
    serena "You're very welcome to stay the night, of course."
    scene v5181 with dissolve
    serena "..."
    serena "Hm..."
    scene v5182 with dissolve
    serena "Maybe we'll get to know each other better while you're here."
    scene v5183 with dissolve
    z "(Huh?! Is it just me or is this woman being flirty...)"
    scene v5184 with dissolve
    serena "*Whispering something."
    scene v5185 with dissolve
    z "!"
    scene v5186 with dissolve
    z "(Okay, it's definitely not just me...)"
    scene v5187 with dissolve
    a "I thank you for your hospitality, my lady."
    scene v5177 with dissolve
    serena "Oh, please! No need to 'my lady' me. Just call me Serena."
    play sound "audio/creaky door.mp3"
    scene v5188 with dissolve
    serena "!"
    scene v5189 with dissolve
    z "(Hm... The atmosphere really changed the second this man showed up. Is he the jarl?)"
    scene v5190 with dissolve
    serena "Johann? My darling?"
    scene v5191 with dissolve
    johann "Hm?"
    scene v5192 with dissolve
    serena "We have guests. They brought your daughter home."
    scene v5193 with dissolve
    johann "Hm..."
    scene v5194 with dissolve
    krlna "..."
    scene v5195 with dissolve
    johann "Karolina, my darling."
    play audio "audio/kiss.mp3"
    scene v5196 with dissolve
    johann "*Kisses her."
    scene v5198 with dissolve
    johann "How was your trip?"
    scene v5197 with dissolve
    krlna "It was good, papa. I had a lot of fun."
    scene v5198 with dissolve
    johann "Is that so? That's great, my love."
    johann "I'm sorry, I have a meeting with an important guest and I must go. We'll talk later, alright?"
    scene v5197 with dissolve
    krlna "Yes, papa."
    scene v5199 with dissolve
    pause(0.3)
    scene v5200 with dissolve
    pause(0.3)
    play sound "audio/Door close.mp3"
    scene v5201 with dissolve
    pause(1)
    z "(Great! Another rich asshole. Just what the world needs.)"
    z "(He seems to be a good father, at least...)"
    scene v5202 with Fade(0.5,1.0,0.5)
    "One dinner serving later..."
    scene v5207 with Fade(0.5,1.0,0.5)
    pause(1)
    scene v5206 with dissolve
    serena "I hope the food was to your liking."
    scene v5207 with dissolve
    tr "To our liking?! Are you kidding me?! That was the best food I had in a year!"
    a "Torr!"
    scene v5208 with dissolve
    serena "*Chuckles. Thank you, my darling."
    scene v5206 with dissolve
    serena "I am sorry to be so direct, but I actually have a proposal for your group."
    scene v5303 with dissolve
    a "A proposal?"
    scene v5206 with dissolve
    serena "I know you might have other things that require your attention back at your village. But if you could remain here just for three more days, I think I have a job that might interest you."
    scene v5303 with dissolve
    a "Hm... What do you have in mind?"
    scene v5206 with dissolve
    serena "Am I to understand that you're willing to do it?"
    scene v5303 with dissolve
    a "That depends on the nature of the job. Our party isn't suitable for anything drastic, but it is our duty to help when we can."
    scene v5206 with dissolve
    serena "I see. Well, the job has already been issued to your village before. Alas, it was unsuccessful."
    scene v5303 with dissolve
    a "Are you talking about the butcher? I thought the jarl was not willing to offer a new contract."
    scene v5206 with dissolve
    serena "True. He isn't. But I am."
    scene v5302 with dissolve
    a "Hm..."
    scene v5206 with dissolve
    serena "Honestly, it's for selfish reasons more than anything."
    scene v5204 with dissolve
    z "What do you mean by selfish reasons?"
    scene v5203 with dissolve
    serena "Well, here's the thing, strong ninja boy."
    scene v5204 with dissolve
    z "(I mean... I didn't mind her flirting at first, but now I'm starting to feel I'm not being taken seriously...)"
    scene v5203 with dissolve
    serena "I'm hosting a ball in three days time. It's a party where the participants eat, drink, and dance. Amongst other... 'activities', occasionally..."
    scene v5204 with dissolve
    z "(She's not even being subtle about it at this point...)"
    scene v5303 with dissolve
    a "And what does the ball have to do with the butcher? You think he might attack your guests?"
    scene v5206 with dissolve
    serena "Well, yes. That'd be quite likely."
    serena "The ball will attract a lot of young and pretty women, dressed in pretty clothes. Which would be the primary target for the butcher."
    serena "It will also takes place in the evening, the time where he's most active, from what I understand."
    scene v5300 with dissolve
    a "I see..."
    a "I'm afriad such a mission is beyond the capacity of my team at the moment."
    scene v5206 with dissolve
    serena "But hear me out. The job isn't to kill him."
    scene v5301 with dissolve
    a "Hm?"
    scene v5206 with dissolve
    serena "I only need you to investigate the town, ask the residents some questions, see if you can find any clues to who he might be."
    serena "If you do so during the day, you shouldn't be in any danger."
    serena "My brother in law is the town's chief detective. Any insight you would provide him might be of help."
    serena "And even if you're unable to find anything, if the butcher sees a group of ninjas going around town asking questions, he might decide to remain hidden for a while."
    serena "I'd also ask you attend the ball, of course. There's no way he'll attack anyone with a Keres present."
    serena "If you agree, I'm willing to pay you four times your regular rate. Think of it as compensation for inconveniencing you with this sudden request."
    scene v5302 with dissolve
    a "Hm..."
    scene v5206 with dissolve
    serena "So? What do you say?"
    scene v5214 with dissolve
    a "..."
    z "(I think she wants to do it... The butcher did a number on her sister, after all. And this could get her the chance to get him.)"
    scene v5210 with dissolve
    a "I feel that my judgement is compromised here... So, let's vote on it."
    scene v5212 with dissolve
    a "So? Thoughts?"
    scene v5298 with dissolve
    tr "We get to choose?!"
    tr "I'm in, of course! I'm gonna be a purple belt in no time with the points from both missions."
    scene v5299 with dissolve
    cndy "Me too. I'm in."
    scene v5214 with dissolve
    a "..."
    scene v5210 with dissolve
    a "[mc_name]?"
    scene v5214 with dissolve
    z "(I suppose this is what I signed up for. And I really don't want to stand in Anabelle's way if she thinks she can get back at him for what he did to her sister...)"
    z "Yeah. Let's do it."
    scene v5211 with dissolve
    a "Great!"
    scene v5206 with dissolve
    serena "Splendid! It's settled then?"
    scene v5207 with dissolve
    a "Yeah. We'll do it."
    scene v5205 with dissolve
    serena "Then I'll have Daiana ready your rooms. We'll also provide you with changes of clothes for three days, it's a bit cold around here."
    serena "You'll have the rooms upstairs and to the right. Daian's room is the one to the left."
    scene v5203 with dissolve
    serena "You should go see her in her room if you need... anything..."
    scene v5204 with dissolve
    z "?"
    scene v5205 with dissolve
    serena "Shall we bring some dessert?"
    pause(1.0)
    scene black with fade
    stop background_s fadeout 1.0
    stop background_s2 fadeout 1.0
    stop music fadeout 1.0
    stop sound fadeout 1.0
    pause(2.5)
    scene v5215 with dissolve
    z "(Upstairs and to the right...)"
    if bdsm == 0:
        jump after_bdsm_ch5
    scene v5216 with dissolve
    z "Hm? (The door is slightly open... This is Daiana's room if I recall...)"
    daiana "Hmm..."
    z "*Gulps. (What's going on in there...)"
    dev "Note: This scene has BDSM-ish content."
    menu:
        "[ModGreen]Have a look.":
            pause(0.7)
            label G12:
                $ persistent.g_12_unlock = 1
            scene v5218 with dissolve
            z "(Just a little pe-)"
            scene v5219 with dissolve
            z "..."
            scene v5220 with dissolve
            z "(The fuck!)" with vpunch
            scene v5221 with dissolve
            z "(Is that... a dildo...)"
            z "(What the fuck are they doing?)"
            scene v5222 with dissolve
            serena "Aren't you tired of standing all day? Don't you want to sit?"
            scene v5223_1 with dissolve
            scene v5223_2 with dissolve
            scene v5223_1 with dissolve
            scene v5223_2 with dissolve
            scene v5223_1 with dissolve
            scene v5223_2 with dissolve
            scene v5223_1 with dissolve
            daiana "MHMMM! HHM!"
            scene v5226 with dissolve
            daiana "Hmmm..."
            scene v5224 with dissolve
            pause(0.5)
            scene v5225
            play sound "audio/Slap2.mp3"
            with vpunch
            daiana "HMM!"
            scene v5227 with dissolve
            serena "Come on... Don't be like that."
            serena "The chair is quite comfortable, you know."
            scene v5228 with dissolve
            pause(0.7)
            scene v5229 with dissolve
            daiana "Hmm!"
            scene v5230 with dissolve
            play music "audio/sex music 2.mp3" volume 0.6 fadeout 1.0 fadein 1.0 loop
            serena "Although... It's probably better if you're ready to sit on it."
            scene v5231 with dissolve
            daiana "Mmmm?"
            scene v5232 with dissolve
            daiana "Hm!"
            scene v5233 with dissolve
            serena "Open up, Daiana."
            scene v5234 with dissolve
            daiana "Mhmmm..."
            scene v5235 with dissolve
            serena "Good girl."
            scene v5236 with dissolve
            serena "Let's check if you're ready."
            daiana "Hm..."
            scene v5237 with dissolve
            daiana "HMMM!"
            scene v5238 with dissolve
            daiana "GHMM!"
            show v5m2 with Dissolve(1)
            daiana "Hm..."
            z "(Whoa... She's fingering her! The fuck kind of relationship do these two have?!)"
            show v5m3 with Dissolve(1)
            daiana "Mhhm... Mmm... Hmm..."
            z "(Do they do this kind of thing often?"
            z "(Also, what the fuck is going on with this house?!)"
            daiana "Mhh... Mmmm... Ghm..."
            scene v5240 with dissolve
            daiana "Mhmmm..."
            scene v5241 with dissolve
            serena "Okay, you're ready enough."
            scene v5242 with dissolve
            daiana "Hmmm?"
            scene v5243 with dissolve
            serena "Come on, let's get you seated."
            daiana "HMM!"
            scene v5244
            play sound "audio/chair squeak.mp3"
            with vpunch
            serena "*Throws her on the chair."
            daiana "HM!"
            show v5245 with Dissolve(1)
            pause(0.7)
            serena "What are you doing? This isn't sitting."
            show v5m5 with Dissolve(1)
            pause(0.7)
            serena "This doesn't look comfortable at all. Come on, let go."
            show v5m4 with Dissolve(1)
            pause(0.7)
            serena "Come on, Daiana. I can see you're struggling. Sit down."
            hide v5m5
            show v5m5 with Dissolve(1)
            pause(0.7)
            serena "Come on, give it a rest, will you?"
            serena "Your arms will get tired very soon..."
            show v5m6 with dissolve
            serena "Don't you want to sit down after working all day?"
            z "(Damn... This is so hot...)"
            serena "Just give up. You can't hold on like this forever."
            show v5m7 with Dissolve(1)
            pause(1.2)
            serena "See? You're moving down little by little."
            serena "You're only delaying the inevitable here."
            show v5m8 with Dissolve(1)
            pause(0.7)
            daiana "Hmmmm..."
            serena "Well... If you insist on not sitting down. I won't force you."
            scene v5249 with dissolve
            serena "But let me commend you on your resolve. You deserve a pat on the back."
            daiana "HMMM!"
            scene v5250
            play sound "audio/chair squeak.mp3"
            with vpunch
            daiana "GHMMM!"
            z "(Holy fuck!)"
            show v5m7_2 with Dissolve(1)
            pause(0.7)
            serena "Woops! Sorry about that. Forgot my weight could ruin everything..."
            daiana "Mmmm... Hmmm... Ghm..."
            serena "You were doing so well too..."
            serena "I always spoil everything, don't I? You always have to clean up my messes around the house..."
            serena "I mean..."
            scene v5251 with vpunch
            daiana "MMMMMMMMMM!"
            scene v5251_1 with vpunch
            daiana "Gah... Mah..."
            scene v5251_2 with dissolve
            serena "I just can't help but want you to sit down and relax, you know? After working this hard..."
            scene v5252 with dissolve
            daiana "Khm... Mmmm..."
            scene v5253 with dissolve
            serena "See? Isn't sitting down after a long day the best?"
            scene v5253_1 with dissolve
            scene v5253 with dissolve
            scene v5253_1 with dissolve
            scene v5253 with dissolve
            scene v5253_1 with dissolve
            scene v5253 with dissolve
            daiana "Hmm..."
            pause(0.7)
            stop background_s fadeout 1.0
            stop background_s2 fadeout 1.0
            stop music fadeout 1.0
            stop sound fadeout 1.0
            scene v5254 with dissolve
            z "(Whoa... The fuck did I just witness...)"
            z "(I should take this opportunity to go before they notice me.)"
            scene v5255 with dissolve
            pause(0.7)
            scene v5256 with dissolve
            serena "..."
            pause(0.7)
            $ renpy.end_replay()
            if came_from_gallery == 1:
                $ came_from_gallery = 0
                jump gallery_2
        "Go to your room. [ModRed](Option to turn off BDSM)":
            z "(Nope. I shouldn't invade her privacy... She left the door open unintentionally. I think...)"
            scene v5217 with dissolve
            z "(Let's just go to my room...)"
            if didnt_get_choice_bdsm == 1:
                dev "Would you like to turn BDSM content off for good?"
                menu:
                    "Turn off BDSM for good.":
                        $ bdsm = 0
                    "Don't.":
                        $ dummy += 1
            pause(0.7)
    label after_bdsm_ch5:
    scene v5257 with Fade(0.5,0.5,0.5)
    play background_s2 "audio/Ambient_ninja_village_night.mp3" volume 0.6 fadeout 1.0 fadein 1.0 loop
    z "(Hm... Nice to have my own room again. Not that I minded sharing with Torr...)"
    scene v5258 with dissolve
    z "(The bed is pretty comfy... I think I'll sleep just fine.)"
    pause(1.0)
    scene black with fade
    stop background_s fadeout 1.0
    stop background_s2 fadeout 1.0
    stop music fadeout 1.0
    stop sound fadeout 1.0
    "The ball is in three days..."
    pause(2.5)
    "[mc_name]!"
    pause(1.0)
    play background_s2 "audio/Ambient_ninja_village.mp3" volume 0.5 fadeout 1.0 fadein 1.0 loop
    scene v5259 with Dissolve(2.5)
    "Wake up, [mc_name]."
    scene v5260 with Dissolve(1.5)
    pause(1.0)
    z "Candy..."
    scene v5261 with dissolve
    cndy "Good morning, [mc_name]."
    scene v5260 with dissolve
    z "Good morning..."
    z "..."
    z "Nice to see you looking normal again..."
    scene v5262 with dissolve
    cndy "*Giggles. Really? Thanks. The suit was a bit uncomfortable, to tell you the truth."
    cndy "Then to make things worse, we had to wear those mask at the faceless god's town."
    scene v5263 with dissolve
    z "Heh. Yeah... Trust me, I was worse off than you."
    scene v5262 with dissolve
    cndy "Yeah... Torr told me your masks were suffocating."
    scene v5263 with dissolve
    z "Yeah. You could see well with them on, but they were very uncomfortable."
    scene v5262 with dissolve
    if v4_obeyed_athena <> 1:
        cndy "At least you got to do something cool. You saw Athena! And even disobeyed her and killed a fury! You and Anabelle saved Torr and the town."
    else:
        cndy "At least you got to do something cool. You saw Athena! Then faced a fury and saved Torr along with Anabelle."
    scene v5263 with dissolve
    z "Yeah... Trust me, it wasn't that cool..."
    scene v5261 with dissolve
    cndy "Oh... Sorry. I didn't mean-"
    scene v5260 with dissolve
    z "No. It's fine, Candy. I get what you mean."
    scene v5263 with dissolve
    cndy "..."
    scene v5262 with dissolve
    cndy "Oh, right! I forgot why I was here. Anabelle sent me to wake you. She and Torr are waiting for us downstairs. We're going to discuss our mission."
    scene v5263 with dissolve
    z "Right... I'll be down there in a minute."
    scene v5264 with dissolve
    cndy "Okay. I'll be heading down, then."
    scene v5265 with dissolve
    pause(0.5)
    scene v5266 with dissolve
    pause(1.0)
    scene v5267 with dissolve
    z "(Well... Time to get up...)"
    scene v5268 with Fade(0.5,1.0,0.5)
    pause(1.0)
    z "Good morning."
    play music "audio/kalm (no panik) 2.mp3" volume 0.2 fadeout 1.0 fadein 1.0 loop
    scene v5269 with dissolve
    a "Good morning, [mc_name]. Please, sit down."
    scene v5271 with dissolve
    pause(1.0)
    scene v5270 with dissolve
    a "I hope you slept well?"
    scene v5271 with dissolve
    z "Yeah. I slept fine. Thanks."
    scene v5273 with dissolve
    tr "No weird dreams or anything?"
    scene v5274 with dissolve
    z "Uh... No. Nothing of this sort."
    scene v5279 with dissolve
    z "So? Candy told me we're going to plan the mission."
    scene v5278 with dissolve
    a "That's right. We'll split up and ask questions around town for today and tomorrow."
    scene v5279 with dissolve
    z "Today and tomorrow? What about the day of the ball?"
    scene v5278 with dissolve
    a "If we happen to find any leads, we'll investigate them during the day of the ball. But we'll need to be here before the sun sets."
    scene v5280_1 with dissolve
    a "For Torr and Candy, this is also the case for the first two days."
    scene v5278 with dissolve
    a "I'll allow you to remain in the city during the night if needed, since the butcher doesn't attack men. But that also means I'm trusting your judgement, [mc_name]. So be careful, okay?"
    scene v5279 with dissolve
    z "(It's nice to hear that she trusts me... I don't want to disappoint her...)"
    z "Yeah. Got it."
    scene v5280 with dissolve
    a "One more thing. Since the butcher is known to attack often around the main square, I want you to investigate there. I feel it's safer for Torr and Candy that way."
    scene v5279 with dissolve
    z "Yeah. I agree. I'll do it."
    scene v5280_1 with dissolve
    a "Torr, you'll be in the west side of the city. It's a bit further, so make sure you start heading back here at least two hours before sunset."
    scene v5272 with dissolve
    tr "Got it."
    scene v5280_1 with dissolve
    a "As for you, Candy. You'll be in the south-eastern side. I'll take the northern side. The same goes for you, of course. Make sure to start heading back with an ample time before sunset."
    scene v5277 with dissolve
    cndy "Okay."
    scene v5278 with dissolve
    a "Before you head out, [mc_name]. The detectives office is apparently in your area. So make sure to head there and get as much information from him as you can."
    scene v5279 with dissolve
    z "Understood."
    z "(I sort of expected this. Even though Serena wants us here just for show, Anabelle is quite serious about catching him if she can.)"
    pause(1.0)
    scene black with fade
    pause(1.0)
    stop background_s fadeout 1.0
    stop background_s2 fadeout 1.0
    stop music fadeout 1.0
    stop sound fadeout 1.0
    pause(2.5)
    scene v5304 with dissolve
    pause(0.35)
    scene v5305 with dissolve
    pause(0.35)
    scene v5306 with dissolve
    pause(0.35)
    scene v5307 with dissolve
    pause(0.35)
    scene v5308 with dissolve
    play sound "audio/tension-build.mp3"
    pause(1.0)
    scene v5309 with dissolve
    pause(1.0)
    scene v5311 with dissolve
    z "!{w=0.7}{nw}"
    scene v5310 with dissolve
    irna "!{w=0.7}{nw}"
    scene v5312 with dissolve
    pause(0.7)
    scene v5313 with dissolve
    z "Shit!{w=0.7}{nw}"
    scene v5314
    play sound "audio/Falling2 (loud).mp3"
    with vpunch
    irna "Fuck!"
    scene v5315 with dissolve
    irna "Relax, relax. I'm not here for you, [mc_name]."
    scene v5316 with dissolve
    z "..."
    #Z pushes back
    scene v5314 with dissolve
    pause(1.0)
    play sound "audio/Magic 2.mp3"
    scene v5317 with Dissolve(1)
    pause(1.0)
    scene v5318 with dissolve
    z "You expect me to believe you?"
    play music "audio/Axius's Theme.mp3" volume 0.8 fadeout 1.0 fadein 1.0 loop
    scene v5319 with dissolve
    irna "Trust me! My father has other things to do at the moment!"
    scene v5320 with dissolve
    z "..." #Looks with disbeliefe.
    scene v5321 with dissolve
    if succubus_incountered >= 1:
        if didnt_join_waterfall == 0:
            irna "Okay, okay. Look. I know last time we met I tricked you."
            irna "But come on! Who would fall for something like that?!"
            irna "Two defenseless maidens bathing all alone in the forest and inviting some stranger to bathe with them? Really?"
            scene v5320 with dissolve
            z "..."
            z "(I mean... She does... have a... point...)"
            scene v5321 with dissolve
            irna "I'd expect something like that to work on a human, but you? The son of the great Elnor?"
            scene v5320 with dissolve
            z "..."
        else:
            irna "Okay, okay. Look. I know last time we met I tried to trick you."
            irna "But those were just orders from my father!"
            irna "I know you don't trust me, but I promise you this, if we were to fight here, it isn't gonna go the way you want it to. Son of Elnor or not, you're no match for me, [mc_name]."
            scene v5320 with dissolve
            z "..."
    else:
        irna "Okay, okay. Look. I know you don't trust me."
        irna "But I promise you this, if we were to fight here, it isn't gonna go the way you want it to. Son of Elnor or not, you're no match for me, [mc_name]."
        scene v5320 with dissolve
        z "..."
    scene v5322 with dissolve
    pause(0.4)
    scene v5323
    play sound "audio/slight_hit.mp3"
    with vpunch
    irna "Huh?!"
    scene v5325
    play sound "audio/Punch2.mp3"
    with vpunch
    irna "!"
    scene v5326
    play sound "audio/Falling.mp3"
    with vpunch
    irna "Ugh!"
    scene v5327 with dissolve
    irna "The fuck-"
    scene v5328
    play sound "audio/Falling2 (loud).mp3"
    with vpunch
    irna "!"
    scene v5329 with dissolve
    irna "..."
    scene v5330 with dissolve
    z "..."
    scene v5331 with dissolve
    z "Okay, here's what's going to happen: You're going to tell me everything you know about my father. Every single detail."
    scene v5332 with dissolve
    irna "..." #Looks ginuanly surprised.
    scene v5329 with dissolve
    irna "You really don't remember?"
    scene v5330 with dissolve
    z "..."
    scene v5329 with dissolve
    irna "Hold on! You mean you don't even remember me?!"
    scene v5330 with dissolve
    z "(Huh?! Is she trying to trick me?!)" #Looks surprised
    scene v5331 with dissolve
    z "Should I?"
    scene v5332 with dissolve
    irna "..."
    scene v5329 with dissolve
    irna "You really don't remember..."
    scene v5332 with dissolve
    pause(0.5)
    stop music
    scene white
    pause (0.1)
    play sound "audio/Effect2.mp3"
    scene v5333
    pause (0.4)
    scene white
    pause (0.1)
    scene v5332
    pause(0.5)
    play background_s "audio/heartbeat.mp3" volume 0.6 fadeout 1.0 fadein 1.0 loop
    scene v5334 with dissolve
    z "..." #Looks shocked.
    #z let's go of her and puts his hand on his head.
    scene v5335 with dissolve
    z "(Ugh... My head... What was that...)"
    pause(0.5)
    scene v5336 with dissolve
    pause(0.7)
    scene v5337 with dissolve
    irna "Come. Let's go sit down for a bit."
    #They sit down at a bench.
    stop background_s fadeout 1.0
    scene v5338 with Fade(0.5,2.0,0.5)
    pause(1)
    scene v5338_1 with Dissolve(2.5)
    play music "audio/Irena's theme.mp3" volume 0.2 fadeout 1.0 fadein 1.0 loop
    pause(1)
    scene v5338_2 with Dissolve(2.5)
    pause(1)
    scene v5338 with Dissolve(2.5)
    pause(1)
    #He remembers her a bit, she was there in his childhood, they played together.
    scene v5340 with dissolve
    z "I remember some things... I used to see them in my dreams... You were there. We played together."
    scene v5339 with dissolve
    irna "Yeah. We did. My father and yours were good friends. I came to your house a lot."
    scene v5341 with dissolve
    z "You did?! How come I don't remember very well?"
    scene v5342 with dissolve
    irna "Beats me."
    scene v5343 with dissolve
    z "..."
    scene v5341 with dissolve
    z "The massacre. How did you and your father survive it?"
    scene v5342 with dissolve
    irna "It's even more puzzling how YOU survived it."
    scene v5341 with dissolve
    z "One of the warriors, a Keres called Seira refused to kill me. She took me back with her and raised me as her own."
    scene v5344 with dissolve
    irna "Oh? Seira the daughter of Ares? I wasn't expecting that..."
    irna "When I sensed an incubus with titan blood, I wasn't expecting it to be you..."
    scene v5342 with dissolve
    if succubus_incountered >= 1:
        irna "Even when we met after in the forest. I didn't recognise you."
    irna "It was only later when you and my father talked that I understood who you were."
    scene v5341 with dissolve
    z "I see..."
    scene v5342 with dissolve
    irna "The attack on our underworld city was not a surprise. Not to Elnor. He knew it would happen."
    scene v5341 with dissolve
    z "What?!"
    scene v5342 with dissolve
    irna "He commanded his generals to prepare for the fight. But most of them defected and ran just the day before the attack. That's why the city was defenseless."
    irna "My father was one of those who ran."
    scene v5341 with dissolve
    z "Wait! Does that mean there are many more of us alive?!"
    scene v5342 with dissolve
    irna "There are definitely some, yes. But not that many. It was only the generals and their families that knew about the attack and fled. They were hunted down after, as well."
    if succubus_incountered >= 1:
        irna "You met Nixie, haven't you? Her mother was one of the servants at my fathers house."
    irna "Of course, those who did escape the massacre went into hiding. It's not hard for most of us to hide. Like you for example. You look more or less like an elf. You could probably even pass as a human if you hid your ears."
    irna "And even those who have tails or horns are able to hide them using clothes, magic, or sometimes potions."
    pause(0.5)
    show v5m9 with dissolve
    pause(0.5)
    define ask_irna1 = 0
    define ask_irna2 = 0
    define ask_irna3 = 0
    menu ask_irna: #(Ask her questions)
    #Make animated scene with blinking
        "Ask about your father." if ask_irna1 <> 1:
            $ ask_irna1 = 1
            z "So, my father. What happened to him?"
            scene v5345 with dissolve
            irna "He died, from what I understand. Accounts differ, but most say he was killed by a powerful demi-god called Sirius."
            scene v5345_1 with dissolve
            z "Sirius?! (That's Anabelle and Yumi's brother, isn't it?)"
            scene v5345 with dissolve
            irna "Yeah. Others say he was killed by Theseus, another demi-god."
            irna "Honestly, I don't know."
            hide v5m9
            show v5m9 with dissolve
            z "..."
            jump ask_irna
        "Ask about your mother." if ask_irna2 <> 1:
            $ ask_irna2 = 1
            z "What about my mother, who was she?"
            scene v5345 with dissolve
            irna "I'm not sure. Some claim your titan blood comes from your mother, who was allegedly Demeter."
            irna "While I do know that Elnor kidnapped and fucked her at one point, I don't know if she's really you mother."
            irna "I heard Elnor was messing around with Athena too, before they broke up and had a fight."
            scene v5345_1 with dissolve
            z "Athena?!" with vpunch
            scene v5345 with dissolve
            irna "Yeah. But that was long after you and I were born, I believe."
            scene v5345_1 with dissolve
            z "Oh... So she can't be my mother... (That's reassuring...)"
            scene v5345 with dissolve
            irna "No, I don't think so."
            scene v5345_1 with dissolve
            pause(0.7)
            scene v5345 with dissolve
            irna "Your titan blood could also be from your father, you know."
            scene v5345_1 with dissolve
            z "What do you mean?"
            scene v5346 with dissolve
            irna "Well, according to my father, your father was a demi-god too. He was the son of Nyx, the primordial goddess of night."
            scene v5345_1 with dissolve
            z "What?! He was?!"
            irna "Mhm."
            z "And he had ichor like I do?"
            scene v5345 with dissolve
            irna "I'm not sure... My father never mentioned it."
            hide v5m9
            show v5m9 with dissolve
            z "..."
            jump ask_irna
        "Ask about your how she looks like a human." if ask_irna3 <> 1:
            $ ask_irna3 = 1
            z "So... Which do you use?"
            scene v5349 with dissolve
            irna "Huh?!"
            scene v5350 with dissolve
            z "Magic or potions? How do you look like a human?"
            scene v5347 with dissolve
            irna "Oh... Well, my mother is a nymph. So I don't have a tail or horns or anything."
            hide v5m9
            show v5m9 with dissolve
            z "I see..."
            jump ask_irna
        "No more questions.":
            $ dummy += 1
    stop music fadeout 1.0
    play background_s2 "audio/Ambient_ninja_village.mp3" volume 0.4 fadeout 1.0 fadein 1.0 loop
    z "Alright, Irena. I trust you. At least, I trust you're not going to attack me for now..."
    scene v5348 with dissolve
    irna "Mhm."
    scene v5346 with dissolve
    irna "So, can I ask you a question?"
    scene v5345_1 with dissolve
    z "Yeah?"
    scene v5345 with dissolve
    irna "What are you doing here in Esyl?"
    scene v5345_1 with dissolve
    z "I'm came here on an escort mission, but now I'm investigating something."
    scene v5345 with dissolve
    irna "And what would that be?"
    scene v5345_1 with dissolve
    z "Some killer called the butcher."
    irna "..."
    scene v5359 with dissolve
    irna "Huh?!"
    scene v5358 with dissolve
    z "What?"
    stop background_s fadeout 1.0
    stop background_s2 fadeout 1.0
    play music "audio/The butcher of Esyl.mp3" volume 0.4 fadeout 1.0 fadein 1.0 loop
    scene v5359 with dissolve
    irna "You're trying to catch the butcher too?"
    scene v5358 with dissolve
    z "Trying to catch him too?!"
    scene v5359 with dissolve
    irna "Why do you want to catch him?"
    scene v5358 with dissolve
    z "Why do YOU want to catch him?"
    scene v5359 with dissolve
    irna "Well... He..."
    scene v5358 with dissolve
    pause(0.7)
    scene v5351 with dissolve
    pause(0.7)
    #irna looks sad...
    scene v5352 with vpunch
    irna "I asked you first!" #Looks angry
    scene v5353 with dissolve
    z "..."
    z "I was hired by someone to do so. More or less..."
    scene v5351 with dissolve
    irna "..."
    z "You don't need to answer, if you don't want to."
    scene v5356 with dissolve
    irna "..."
    scene v5354 with dissolve
    irna "No... It's fine..."
    scene v5355 with dissolve
    irna "*Sighs."
    scene v5354 with dissolve
    irna "He killed a friend of mine."
    scene v5356 with dissolve
    z "Oh..."
    scene v5354 with dissolve
    irna "I used to visit her here often. I learned she was killed yesterday when I arrived."
    scene v5356 with dissolve
    z "I'm sorry."
    irna "..."
    scene v5352 with dissolve
    irna "Hufm. I don't want your pity." #Looks away angry
    scene v5357 with dissolve
    z "..."
    #The render is irna looking away:
    z "Listen. How about we go around investigating together?"
    #She looks shocked:
    scene v5358 with dissolve
    z "I'm planning to ask the detective a few questions and then ask the people around the market. Could use some help."
    irna "..."
    #Looks at z with her mouth slightly open:
    scene v5359 with dissolve
    irna "I..."
    pause(0.5)
    scene v5358 with dissolve
    pause(1.5)
    #stands up:
    play sound "audio/chair squeak.mp3"
    scene v5360 with dissolve
    pause(0.5)
    irna "Fine."
    #Render to her standing.
    scene v5361 with dissolve
    irna "We'll probably gather more info that way."
    scene v5362 with dissolve
    z "Yeah."
    pause(1)
    scene black with fade
    pause(2.5)
    scene v5363 with dissolve
    pause(1)
    scene v5365 with dissolve
    pause(1)
    scene v5366 with dissolve
    pause(1)
    scene v5364 with dissolve
    tomas "What brings you here today? No incidents since you arrived here, I hope..."
    scene v5366 with dissolve
    z "No. We just wanted to ask you a few questions."
    scene v5364 with dissolve
    tomas "Questions? About what?"
    scene v5366 with dissolve
    z "The butcher."
    pause(1)
    scene v5363 with dissolve
    pause(1)
    scene v5365 with dissolve
    pause(1)
    scene v5366 with dissolve
    tomas "..."
    scene v5364 with dissolve
    tomas "Serena."
    tomas "She hired you, didn't she?"
    scene v5366 with dissolve
    z "Yeah..."
    tomas "Hm..."
    scene v5364 with dissolve
    tomas "Very well, then. I'll give you whatever information I can. Ask away."
    define asked_abt_ymi = 0
    define ask_tomas1 = 0
    define ask_tomas2 = 0
    define ask_tomas3 = 0
    define ask_tomas4 = 0
    define ask_tomas5 = 0
    define ask_tomas6 = 0
    define ask_tomas7 = 0
    scene v5363 with dissolve
    pause(1)
    menu ask_tomas:
        "Serena mentioned something about his targets being younger women. Mostly in nice clothes." if ask_tomas1 <> 1:
            $ ask_tomas1 = 1
            z "Serena mentioned something about his targets being younger women. Mostly in nice clothes."
            pause(1)
            scene v5365 with dissolve
            pause(1)
            scene v5364 with dissolve
            tomas "Yeah. That's true. He never attacks men. It's always women. No older than thirty. Mostly good looking ones as well."
            scene v5366 with dissolve
            z "Hm..."
            scene v5364 with dissolve
            tomas "He used to attack women walking alone, or in groups of no more than three. However, after his fight with Yumi, he started to only target those that are alone."
            #Irena renders.
            if asked_abt_ymi == 0:
                $ asked_abt_ymi = 1
                scene v5369 with dissolve
                irna "Who's Yumi?"
                scene v5370 with dissolve
                z "One of the ninja girls, she was sent here to kill the butcher some time ago."
                scene v5369 with dissolve
                irna "And?"
                scene v5370 with dissolve
                z "She failed. She was injured, but so was the butcher."
                irna "Hm..."
            scene v5364 with dissolve
            tomas "We also used to see an attack almost on a daily basis. But now it's once every three days or so. And the unsuccessful attempts have become more frequent."
            scene v5366 with dissolve
            irna "Unsuccessful attempts? So some people did managed to get away from him."
            scene v5364 with dissolve
            tomas "Yeah. But he always comes back for them, so I ask them to leave the city as fast as possible."
            scene v5366 with dissolve
            irna "Am I to understand that there are no witnesses that we can talk to in the city?"
            scene v5364 with dissolve
            tomas "I'm afraid not. The last one left two days ago."
            scene v5366 with dissolve
            z "And he never goes out of the city to try and follow them?"
            scene v5364 with dissolve
            tomas "No. He's never done that before."
            scene v5363 with dissolve
            pause(1)
            jump ask_tomas
        "Are the victims usually found?" if ask_tomas2 <> 1:
            $ ask_tomas2 = 1
            z "The victims, what does he do with them after killing them? Do you simply find them where they were attacked."
            pause(1)
            scene v5365 with dissolve
            pause(1)
            scene v5364 with dissolve
            tomas "Yes. They're always left with a knife stab wound sitting or lying in a puddle of blood at the exact spot of the attack."
            tomas "He changes the spots where he attacks often, as well. So it's hard to tell where he might attack."
            scene v5363 with dissolve
            pause(1)
            jump ask_tomas
        "The people here seem to think it's safe during the day. Is this true?" if ask_tomas3 <> 1:
            $ ask_tomas3 = 1
            z "Most people here seem to believe it's safe during the day. Does the butcher never attack before sunset?"
            pause(1)
            scene v5365 with dissolve
            pause(1)
            scene v5364 with dissolve
            tomas "Before it's dark. No. Not once has he attacked someone while there's any light in the sky. It's always in the dark."
            tomas "He probably relies on stealth to kill his victims swiftly and quickly."
            scene v5363 with dissolve
            pause(1)
            jump ask_tomas
        "Is the butcher definitely a man?" if ask_tomas4 <> 1:
            $ ask_tomas4 = 1
            z "So... Everyone is always referring to the butcher as 'he'. Are we certain he's a man?"
            pause(1)
            scene v5365 with dissolve
            pause(1)
            scene v5364 with dissolve
            tomas "I'd love to say that I know at least the answer to this question. But no. We do not know that with certainty."
            tomas "Most accounts from witnesses discribe him as a man, rather tall."
            #Points at painting
            scene v5367 with dissolve
            tomas "And if this illustration is to be believed, he wears some kind of apron and a hood."
            tomas "That said, it was always very dark where he shows up, the victims are panicking, and our butcher could be using an illusion or wearing some kind of clothes to make HER appear as a man, for all we know."
            scene v5368 with dissolve
            z "Hmm... Good point, I suppose..."
            scene v5363 with dissolve
            pause(1)
            jump ask_tomas
        "Whom do you suspect?" if ask_tomas5 <> 1:
            $ ask_tomas5 = 1
            z "Do you have any reason to suspect anyone?"
            pause(1)
            scene v5365 with dissolve
            pause(1)
            scene v5364 with dissolve
            tomas "I couldn't tell. It could be anyone at this point. He leaves very little evidence."
            tomas "What I do know is that he's been living here for a long time... Not only has he been killing for a while now, he also knows the streets of the city like the back of his hand."
            scene v5363 with dissolve
            pause(1)
            jump ask_tomas
        "How did Yumi find him?" if ask_tomas6 <> 1:
            $ ask_tomas6 = 1
            z "One question that comes to mind is how Yumi managed to get to him."
            #Irena renders.
            if asked_abt_ymi == 0:
                $ asked_abt_ymi = 1
                scene v5369 with dissolve
                irna "Who's Yumi?"
                scene v5370 with dissolve
                z "One of the ninja girls, she was sent here to kill the butcher some time ago."
                scene v5369 with dissolve
                irna "And?"
                scene v5370 with dissolve
                z "She failed. She was injured, but so was the butcher."
                irna "Hm..."
            scene v5363 with dissolve
            pause(1)
            scene v5365 with dissolve
            pause(1)
            scene v5364 with dissolve
            tomas "Yes, well... She used an interesting strategy. One which I advised against."
            scene v5366 with dissolve
            z "Hm?"
            scene v5364 with dissolve
            tomas "It was pretty simple really. Bait."
            scene v5366 with dissolve
            z "Bait?"
            scene v5364 with dissolve
            tomas "Yes. She used herself as bait. She drank a potion that made her aura difficult to detect and walked alone at night at the spots where the attacks were known to happen most."
            scene v5366 with dissolve
            z "...I see."
            z "(That was really risky... But I suppose that's the nature of the job...)"
            scene v5363 with dissolve
            pause(1)
            jump ask_tomas
        "When did the killings start?" if ask_tomas7 <> 1:
            $ ask_tomas7 = 1
            z "When exactly did the butcher start killing people?"
            pause(1)
            scene v5365 with dissolve
            pause(1)
            scene v5364 with dissolve
            tomas "About three years ago. Or at least, we started to notice the pattern then."
            tomas "At first it was one attack every month. Sometimes, even less often."
            tomas "But he started to get more vicious with time. And in the last few months, it was almost one attack per day."
            scene v5363 with dissolve
            pause(1)
            jump ask_tomas
        "No more questions.":
            $ dummy += 1
    z "That's all we wanted to ask. Thanks, Tomas."
    pause(1)
    scene v5365 with dissolve
    pause(1)
    scene v5364 with dissolve
    tomas "Watch yourselves out there."
    scene v5363 with dissolve
    pause(1)
    scene v5370 with dissolve
    z "Let's go ask around in the market. Maybe we'll learn something."
    scene v5369 with dissolve
    irna "Alright."
    scene v5370 with dissolve
    pause(1)
    scene black with fade
    pause(1)
    stop background_s fadeout 1.0
    stop background_s2 fadeout 1.0
    stop music fadeout 1.0
    stop sound fadeout 1.0
    pause(2.5)
    play background_s2 "audio/Ambient_ninja_village.mp3" volume 0.4 fadeout 1.0 fadein 1.0 loop
    scene v54 with dissolve
    play music "audio/Esyl.mp3" volume 0.4 fadeout 1.0 fadein 1.0 loop
    pause(0.7)
    $ sus_open = 1
    dev "A suspect menu is now available in the stats screen."
    z "Alright. Let's go ask around."
    scene v5372 with Fade(0.5,1.5,0.5)
    pause(1)
    z "Good day, mister Toni."
    scene v5373 with dissolve
    toni "Hello, blond customer! How can Toni help?"
    scene v5372 with dissolve
    z "We're investigating the butcher's case and would like to ask you a few questions if you don't mind."
    scene v5373 with dissolve
    toni "Of course! Ask Toni anything!"
    scene v5372 with dissolve
    define toni_q1 = 0
    define toni_q2 = 0
    define toni_q3 = 0
    define toni_q4 = 0
    define toni_q5 = 0
    menu ask_toni:
        "How long have you been living in Esyl?" if toni_q1 == 0:
            $ toni_q1 = 1
            z "How long have you been living in the city?"
            scene v5373 with dissolve
            toni "Toni come here few year ago. Business very good here. So Toni come."
            toni "Toni own his store for more than five year. Then Toni expand store because he earn much money."
            scene v5372 with dissolve
            z "I see..."
            jump ask_toni

        "Do you have a family here?" if toni_q3 == 0:
            $ toni_q3 = 1
            z "Do you have a family in the city, mister Toni?"
            scene v5373 with dissolve
            toni "Toni have very big family. Toni have even five wife."
            scene v5372 with dissolve
            z "Huh?! Five wives? You have a harem or something?"
            scene v5376 with dissolve
            toni "Toni very good with women, my friend! I teach you if you want." #Winks at Z
            scene v5377 with dissolve
            z "Hm..."
            scene v5378 with dissolve
            z "(Nah... I think I'll have my own harem very soon. Maybe in two or three more chapters?)" #Looking at camera smiling
            play sound "audio/RecordScratch (thanks senpai).ogg"
            stop music
            dev "Huh?! Don't rush me, dude! I still haven't finished writing chapter 6! Let the story flow and decide on it's own, okay?" with vpunch
            scene v5379 with dissolve
            z "..." #Looks disapointed
            scene v5372 with dissolve
            play music "audio/Esyl.mp3" volume 0.4 fadeout 1.0 fadein 1.0 loop
            jump ask_toni

        "What do you think of the others around the square?" if toni_q4 == 0:
            $ toni_q4 = 1
            z "What are your thoughts on the others around the square? Frankie, Erwin, and Misty."
            scene v5374 with dissolve
            toni "Frankie is bad musician, my friend."
            toni "His music make Toni's ear bleed."
            scene v5373 with dissolve
            toni "Misty is nice little lady. A little... pale. Maybe becuase it cold here. She never buy anything from Toni."
            scene v5374 with dissolve
            toni "Erwin is very good artist. Veeeerrry tasteful. But he is very bad business man."
            scene v5372 with dissolve
            z "How so?"
            scene v5374 with dissolve
            toni "He always paint people for free. How can he make money if he work for free?!"
            scene v5372 with dissolve
            jump ask_toni

        "What do you know about the butcher?" if toni_q2 == 0:
            $ toni_q2 = 1
            z "What do you know about the butcher, mister Toni?"
            scene v5374 with dissolve
            toni "Butcher very bad for business. He kill some of Toni's best customer."
            scene v5371 with dissolve
            z "(How very sensitive...)" #looks annoyed
            scene v5372 with dissolve
            jump ask_toni

        "Do you suspect anyone?" if toni_q5 == 0:
            $ toni_q5 = 1
            z "Do you suspect anyone of being the butcher, mister Toni?"
            scene v5375 with dissolve
            toni "Toni think it someone trying to make him go out off business. Maybe other shop owner."
            scene v5371 with dissolve
            z "(But you seem to own all the shops around here...)" #Looks annoyed.
            scene v5372 with dissolve
            jump ask_toni
    z "Well... Thank you for your time, mister Toni."
    scene v5373 with dissolve
    toni "You welcome, my friend."
    scene v5372 with dissolve
    pause(1.0)
    scene v5380 with Fade(0.5,1.5,0.5)
    pause(1.0)
    z "Hello, mister Erwin."
    scene v5381 with dissolve
    erwin "Hello, young sir. How can I help?"
    scene v5380 with dissolve
    z "I'm investigating the butcher's case and would like to ask a few questions if you have a few minutes."
    scene v5381 with dissolve
    erwin "Of course."
    define erwin_q1 = 0
    define erwin_q2 = 0
    define erwin_q3 = 0
    define erwin_q4 = 0
    define erwin_q5 = 0
    scene v5380 with dissolve
    menu ask_erwin:
        "How long have you been living in Esyl?" if erwin_q1 == 0:
            $ erwin_q1 = 1
            z "How long have you been living in the city?"
            scene v5381 with dissolve
            erwin "I've been living here for almost ten years now."
            scene v5380 with dissolve
            z "I see..."
            jump ask_erwin

        "Do you have a family here?" if erwin_q3 == 0:
            $ erwin_q3 = 1
            z "Do you have a family in the city, mister Erwin?"
            scene v5382 with dissolve
            erwin "I fear I don't have a family here. I left my family when I was a young man. I joined a few traveling artists for a while, then decided to settle here."
            scene v5380 with dissolve
            jump ask_erwin

        "What do you think of the others around the square?" if erwin_q4 == 0:
            $ erwin_q4 = 1
            z "What are your thoughts on the others around the square? Toni, Frankie, and Misty."
            scene v5383 with dissolve
            erwin "Toni, huh? Well... He did sell me some paint once. It started to rot a few days later... So I stopped buying painting supplies from him..."
            scene v5384 with dissolve
            erwin "Frankie has his own style. An artist should always follow their hearts, that is what's most important."
            scene v5381 with dissolve
            erwin "Misty? Ah, yes. The tea shop owner."
            erwin "A lovely lady. We don't speak very often, though."
            scene v5380 with dissolve
            jump ask_erwin

        "What do you know about the butcher?" if erwin_q2 == 0:
            $ erwin_q2 = 1
            z "What do you know about the butcher?"
            scene v5381 with dissolve
            erwin "I'd say I know quite a bit about him..."
            scene v5380 with dissolve
            z "Hm?"
            scene v5385 with dissolve
            erwin "He..." #looks sad
            erwin "He killed the love of my life..."
            scene v5389 with dissolve
            z "..." #looks surprised.
            #Irna in the frame but doesn't show facial expressions.
            scene v5388 with dissolve
            erwin "*Sighs. It was a woman. A very pretty woman called Elien."
            scene v5390 with dissolve
            erwin "She used to buy from me. She liked my paintings a lot. Very much like Lady Schwartz."
            scene v5387 with dissolve
            erwin "..."
            scene v5388 with dissolve
            erwin "I always said to myself. Tomorrow is the day you ask her on a date."
            erwin "But I never could do it. Every time she passed by my shop, the words would refuse to come out of my mouth..."
            scene v5387 with dissolve
            z "The butcher killed her?"
            scene v5388 with dissolve
            erwin "He did."
            scene v5393 with dissolve
            z "..."
            scene v5394 with dissolve
            z "I'm... sorry."
            scene v5387 with dissolve
            pause(0.7)
            scene v5391 with dissolve
            erwin "..." #Looks up at Z
            scene v5390 with dissolve
            erwin "Thank you..."
            scene v5393 with dissolve
            z "(Damn... Erwin looks like a polite and elegant man... It feels bad to see him down like this... The butcher really has to pay for what he's done. The more I talk to the people around here, the more I want to catch this guy.)"
            scene v5380 with dissolve
            jump ask_erwin

        "Do you suspect anyone?" if erwin_q5 == 0:
            $ erwin_q5 = 1
            z "Do you suspect anyone of being the butcher, mister Erwin?"
            scene v5382 with dissolve
            erwin "I'm hardly in a position to suspect any of the people around here. They are all kind and respectful people."
            scene v5380 with dissolve
            jump ask_erwin
    z "Well... That was all I wanted to ask. Thank you for your help, sir."
    scene v5381 with dissolve
    erwin "You're quite welcome. I wish you the best of luck."
    scene v5380 with dissolve
    pause(0.7)
    scene v5395 with Fade(0.5,1.5,0.5)
    pause(1.0)
    z "There's Frankie."
    scene v5396 with dissolve
    z "Hi there, Frankie."
    scene v5397 with dissolve
    frankie "Hm?"
    scene v5398 with dissolve
    if tipped_frankie == 1:
        frankie "Oh! Hello kind sir that tipped me yesterday."
    else:
        frankie "Oh. Hello."
    frankie "Would you like to hear a song?"
    scene v5397 with dissolve
    z "No thanks, Frankie. We're here to ask a few questions regarding the butcher."
    scene v5398 with dissolve
    frankie "Questions? Sure thing!"
    scene v5397 with dissolve
    define frankie_q1 = 0
    define frankie_q2 = 0
    define frankie_q3 = 0
    define frankie_q4 = 0
    define frankie_q5 = 0
    menu ask_frankie:
        "How long have you been living in Esyl?" if frankie_q1 == 0:
            $ frankie_q1 = 1
            z "How long have you been living in the city?"
            scene v5398 with dissolve
            frankie "I came here when I was fourteen. I've lived here ever since."
            scene v5397 with dissolve
            jump ask_frankie

        "Do you have a family here?" if frankie_q3 == 0:
            $ frankie_q3 = 1
            z "Do you have a family in the city, Frankie?"
            scene v5398 with dissolve
            frankie "No family in the city. I left my family and my home to pursue my dream here. It was a sacrifice I was willing to make."
            scene v5397 with dissolve
            z "..."
            z "(Maybe you shouldn't have...)"
            jump ask_frankie

        "What do you think of the others around the square?" if frankie_q4 == 0:
            $ frankie_q4 = 1
            z "What are your thoughts on the others around the square? Toni, Erwin, and Misty."
            scene v5401 with dissolve
            frankie "Toni is a criminal! He sold me a broken guitar! I should've listened to Misty."
            scene v5398 with dissolve
            frankie "Misty, on the other hand, is always nice to me, gives me free tea, and always lets me work at her shop."
            frankie "Erwin is a great artist. And he's always supportive of me, so I like him."
            scene v5397 with dissolve
            jump ask_frankie

        "What do you know about the butcher?" if frankie_q2 == 0:
            $ frankie_q2 = 1
            z "What do you know about the butcher?"
            scene v5399 with dissolve
            frankie "I don't know much. He kills women. Pretty ones. And he only does it at night."
            frankie "You should probably ask Tomas, the detective, if you want to know more about him."
            scene v5397 with dissolve
            jump ask_frankie

        "Do you suspect anyone?" if frankie_q5 == 0:
            $ frankie_q5 = 1
            z "Do you suspect anyone of being the butcher, Frankie?"
            scene v5399 with dissolve
            frankie "Suspect?! No. I don't suspect anyone here." #Looks surprised
            scene v5397 with dissolve
            jump ask_frankie

    z "Alright. That was all, Frankie. Thanks for your help."
    scene v5398 with dissolve
    if tipped_frankie == 1:
        frankie "Sure thing, generous sir!"
    else:
        frankie "Sure thing."
    scene v5397 with dissolve
    pause(1.0)
    scene v5404 with Fade(0.5,1.5,0.5)
    pause(1.0)
    z "(And finally, It's Misty's turn.)"
    z "Good afternoon, miss Misty."
    scene v5405 with dissolve
    misty "Hm?"
    scene v5406 with dissolve
    misty "..."
    scene v5407 with dissolve
    misty "Oh. It's you. Hello there."
    scene v5408 with dissolve
    misty "Good afternoon, sir [mc_name]. Sit down, I'll be with you shortly."
    show v5m10 with dissolve
    z "Maybe later. We were actually hoping to ask you a few questions..."
    scene v5409 with dissolve
    misty "A few questions?"
    show v5m10 with dissolve
    z "Yeah. We're investigating the butcher's case, you see."
    scene v5409 with dissolve
    misty "Oh... Uhm... Sure. What would you like to know?"
    hide v5m10
    show v5m10 with dissolve
    #Misty_q5 living in Esyl
    #Butcher if choice5_2 < 2
    #q7 about her parents
    define misty_q8 = 0
    define misty_q9 = 0
    define misty_q10 = 0
    define misty_q11 = 0
    define misty_q12 = 0
    menu ask_misty:
        "How long have you been living in Esyl?" if misty_q8 == 0:
            $ misty_q8 = 1
            if misty_q5 == 1:
                z "(I already asked her this yesterday.)"
            else:
                z "How long have you been living in the city?"
                scene v5409 with dissolve
                misty "I was born here. And I've lived here all my life. I've never left Esyl."
                hide v5m10
                show v5m10 with dissolve
            jump ask_misty

        "Do you have a family here?" if misty_q9 == 0:
            $ misty_q9 = 1
            z "Do you have a family in the city?"
            scene v5410 with dissolve
            if misty_q7 == 1:
                misty "Oh. As I said yesterday, I've always lived here with my parents here. My mother was a human and my father is a beast. Which is why I'm a demi-human."
            else:
                misty "Oh. well, I've always lived here with my parents here. My mother was a human and my father is a beast. Which is why I'm a demi-human."
            misty "My mother died three years ago, she left me this place."
            hide v5m10
            show v5m10 with dissolve
            z "Sorry to hear that."
            irna "What about your father?"
            scene v5410 with dissolve
            misty "M-My father? He died too... A few months after my mother."
            hide v5m10
            show v5m10 with dissolve
            z "..."
            irna "I see..."
            irna "Husband? Or perhaps lover?"
            scene v5416 with dissolve
            misty "L-Lover?! No! I don't have a-anything like that!"
            hide v5m10
            show v5m10 with dissolve
            jump ask_misty

        "What do you think of the others around the square?" if misty_q10 == 0:
            $ misty_q10 = 1
            z "What are your thoughts on the others around the square? Toni, Erwin, and Frankie."
            scene v5409 with dissolve
            misty "Frankie is a nice guy. His music is a bit of an acquired taste, in my opinion."
            misty "Erwin is a polite person. I think he's a bit shy, but he always says good morning to me."
            scene v5411 with dissolve
            misty "Toni is just... I mean..."
            scene v5412 with dissolve
            misty "Why does everything have to cost so much at his store?!"
            scene v5413 with dissolve
            misty "Well... Stores. And he sells broken stuff! Just ask Frankie!"
            hide v5m10
            show v5m10 with dissolve
            jump ask_misty

        "What do you know about the butcher?" if misty_q11 == 0:
            $ misty_q11 = 1
            if choice5_2 >= 2:
                z "(I already asked her this yesterday.)"
            else:
                z "What do you know about the butcher?"
                scene v5410 with dissolve
                misty "I only know he never shows up during the day. Which is why I never open the shop at night."
                hide v5m10
                show v5m10 with dissolve
            jump ask_misty

        "Do you suspect anyone?" if misty_q12 == 0:
            $ misty_q12 = 1
            z "Do you suspect anyone of being the butcher, Misty?"
            scene v5414 with dissolve
            misty "It could be Toni. I mean, nothing is beyond what this guy is capable of. The painting of the butcher that Erwin drew even looks like him." #Looks angry
            scene v5415 with dissolve
            pause(0.7)
            hide v5m10
            show v5m10 with dissolve
            jump ask_misty

    z "Well, that was all, Misty. Thanks for your help."
    scene v5417 with dissolve
    misty "Sure thing! Come again!"
    pause(1.0)
    scene black with fade
    stop background_s fadeout 1.0
    stop background_s2 fadeout 1.0
    stop music fadeout 1.0
    stop sound fadeout 1.0
    pause(2.5)
    play background_s2 "audio/Ambient_ninja_village.mp3" volume 0.4 fadeout 1.0 fadein 1.0 loop
    scene v5418 with dissolve
    pause(1.0)
    z "*Sighs. Looks like we didn't get much, huh?"
    scene v5420 with dissolve
    irna "I wouldn't say that." #Smiling
    play music "audio/Misty's theme.mp3" volume 0.4 fadeout 1.0 fadein 1.0 loop
    scene v5421 with dissolve
    z "Hm?"
    z "Did I miss something?"
    scene v5422 with dissolve
    irna "Well, aside from the spider girl, they were all telling the truth."
    scene v5421 with dissolve
    z "Huh?! How would you know something like that?"
    scene v5425 with dissolve
    irna "You really don't remember shit, do you?"
    scene v5426 with dissolve
    irna "..."
    scene v5427 with dissolve
    irna "Well, I can tell when people are lying. It's an ability of mine, so to speak."
    scene v5428 with dissolve
    z "Wait! Such an ability exists?!"
    scene v5429 with dissolve
    irna "Yeah. Some people even have it without any magic involved. But it's not as accurate as mine."
    scene v5430 with dissolve
    z "How accurate are we talking?"
    scene v5423 with dissolve
    irna "Depends on the person. But I'm pretty confident about this."
    scene v5421 with dissolve
    z "So out of all the people we questioned, only Misty lied?"
    scene v5420 with dissolve
    irna "Yeah. She lied when talking about her family."
    scene v5421 with dissolve
    z "Was it when she talked about her mother or father?"
    z "Or maybe about not having a lover?"
    scene v5423 with dissolve
    irna "Not entirely sure. But seeing how we're tourists who'll leave the city soon, why would she need to lie?"
    scene v5421 with dissolve
    z "I mean, I can see your point when it comes to her parents being dead. But if it's the lover thing, it's possible she's just shy, or maybe it's a secret affair of some sort."
    scene v5420 with dissolve
    irna "I know, but I'm telling you, she's hiding something bigger than that. Trust me. Succubus instinct."
    scene v5421 with dissolve
    z "(I feel like Irena is right. I sort of had this feeling that Misty is hiding something when we asked her too...)"
    $ misty_info = 1
    scene v5418 with dissolve
    z "So? Think we should look into it?"
    scene v5419 with dissolve
    irna "Yeah. Maybe it's a lead to the butcher somehow."
    scene v5418 with dissolve
    z "Hm... (Well... We don't have any other leads anyway...)"
    z "Alright. Let's try following her home tomorrow."
    irna "Hm..."
    scene v5427 with dissolve
    irna "Yeah... Let's." #Smiling.
    scene v5428 with dissolve
    pause(0.7)
    scene v5431 with Fade(0.5,1.5,0.5)
    pause(1.0)
    z "Well. We'd better head back. Everyone closes in the night around here anyway."
    scene v5432 with dissolve
    irna "Come find me back here tomorrow. We'll start our investigation into the spider girl. And don't be late!"
    scene v5433 with dissolve
    z "Don't be late, you say?"
    z "I hope you'll be able to sleep, being this excited to see me again and all..."
    scene v5434 with dissolve
    irna "Heh. Is this your brain or your dick talking? I just don't like being kept waiting."
    scene v5435 with dissolve
    menu:
        "[ModGreen]Tell her to be careful at night. (Irena Love +1)":
            z "Watch yourself at night, okay Irena?"
            scene v5436 with dissolve
            irna "Huh?!"
            scene v5437 with dissolve
            irna "What are you talking about? It's the butcher that needs to watch himself!"
            scene v5438 with dissolve
            z "*Chuckles. If you say so..."
            $ irna_aff += 1
            show screen button_aff with dissolve
            play sound "audio/stats.wav"
            hide screen button_aff with dissolve
        "Don't.":
            z "Well... Good night, Irena."
    scene v5439 with dissolve
    irna "Good night, [mc_name]."
    scene v5440 with dissolve
    pause(0.7)
    z "(Time to go back to the mansion, I suppose.)"
    stop music fadeout 1.0
    scene v5441 with Fade(0.5,1.5,0.5)
    #Jenny:
    pause(0.7)
    z "(Wow! Great figure!)"
    z "(Should she really be walking around alone? It's almost dark...)"
    z "(I should at least warn her, I guess...)"
    scene v5442 with dissolve
    z "Excuse me, miss?"
    "Hm?"
    z "Jenny?!"
    scene v5443 with dissolve
    jnfr "Huh?! How did you-"
    scene v5444 with dissolve
    jnfr "Wait! [mc_name]?! Is that you?!"
    play music "audio/Alchemy.mp3" volume 0.15 fadeout 1.0 fadein 1.0 loop
    scene v5445 with dissolve
    jnfr "Gods! Look how big you are now! I know I saw at the house last week..."
    scene v5446 with dissolve
    jnfr "...But come on! I still remember you being the size of my leg."
    scene v5447 with dissolve
    z "Pffft... I wasn't that small."
    scene v5448 with dissolve
    jnfr "*Giggles. Maybe you weren't..."
    scene v5447 with dissolve
    z "What are you doing here?"
    scene v5450 with dissolve
    jnfr "Well... I always come to the market during the day, since I don't have anything else to do at the inn. But the market always closes at sunset here for some reason..."
    scene v5451 with dissolve
    z "The inn? No. I mean what are you doing walking all alone at night?! It's dangerous!"
    scene v5452 with dissolve
    jnfr "Huh?! It's not even night yet! And what about you? And you're walking all alone too!" #annoyed
    scene v5453 with dissolve
    z "But I'm a man!"
    scene v5454 with dissolve
    jnfr "Oh? So because you're a big strong man now, you can walk around but I can't?! You know, you used to sleep in my bed when you were scared back in the day! Didn't take you for someone like Ja-" #annoyed rolls her eyes.
    scene v5455 with dissolve
    z "Huh?! No! That's not what I meant! You haven't heard about the serial killer that only attacks women at night in the city?"
    scene v5456 with dissolve
    jnfr "..." #Surprised
    scene v5457 with vpunch
    jnfr "A s-s-serial killer?!"
    scene v5458 with dissolve
    z "Yeah."
    scene v5457 with dissolve
    jnfr "And he only attacks women?" #Surprised
    scene v5458 with dissolve
    z "Yeah... Mostly young and pretty women too. So... You really shouldn't go around walking at night, Jenny."
    jnfr "..."
    scene v5459 with dissolve
    jnfr "Wait. Did you just call me pretty?" #Flirty
    scene v5460 with dissolve
    z "Heh. Maybe..."
    $ jnfr_aff += 1
    show screen button_aff with dissolve
    play sound "audio/stats.wav"
    hide screen button_aff with dissolve
    scene v5461 with dissolve
    jnfr "Well, sorry I snapped at you. And no. I haven't heard about this. Jamie failed to mention it somehow."
    scene v5462 with dissolve
    z "Jamie?"
    scene v5461 with dissolve
    jnfr "Yeah. My betrothed. You met him back at the house, remember?"
    scene v5462 with dissolve
    z "..."
    scene v20128 with Dissolve(2.5)
    #Flashback
    pause(0.7)
    z "(Right... That asshole...)"
    z "(Damn... I recall Gabbie telling me that Jenny was more or less forced into this by her mother, since this guy is super rich...)"
    scene v5462 with Dissolve(2.5)
    pause(1.5)
    #Choice
    define escorting_jenny = 0
    menu:
        "[ModGreen]Tell her you'll escort her back. (Jenny Love +1 Trust +1 Lust +1)":
            $ escorting_jenny = 1
            z "Listen, I'm gonna walk you back, okay?"
            scene v5463 with dissolve
            jnfr "Eh? But-"
            scene v5464 with dissolve
            z "No buts, Jenny. Honestly, it's a good thing I ran into you."
            jnfr "..."
            scene v5463 with dissolve
            jnfr "Fine..."
            scene v5465 with dissolve
            jnfr "Thanks, [mc_name]." #Smiling
            scene v5466 with dissolve
            z "Of course."
            $ jnfr_aff += 1
            $ jnfr_trst += 1
            show screen button_aff with dissolve
            play sound "audio/stats.wav"
            hide screen button_aff with dissolve
            show screen button_trst with dissolve
            play sound "audio/stats.wav"
            hide screen button_trst with dissolve
            #on the way:
            pause(0.7)
            scene black with fade
            pause(1)
            stop background_s fadeout 1.0
            stop background_s2 fadeout 1.0
            stop music fadeout 1.0
            stop sound fadeout 1.0
            pause(2.5)
            play background_s2 "audio/Ambient_ninja_village_night.mp3" volume 0.9 fadeout 1.0 fadein 1.0 loop
            scene v5467 with dissolve
            pause(0.7)
            z "(The streets are better lit than I though they'd be...)"
            scene v5468 with dissolve
            z "(Jenny doesn't seem to be complaining about having me around though...)"
            z "So... How do you like it here?"
            scene v5469 with dissolve
            jnfr "Well... It was nice at first. The markets really have everything here. Mother hardly allowed me to go to the markets with her. So, it's a fresh experience for me. I was having fun."
            scene v5470 with dissolve
            jnfr "Then some dude shows up telling me I could be murdered any second. Which kinda, you know..."
            scene v5471 with dissolve
            z "Heheh. Sorry about that..."
            z "So... Are you gonna settle down here, or..."
            scene v5472 with dissolve
            jnfr "Oh, no. We're only here because Jamie had some business in the city. And I asked to come with him to escape from mother's tyranny, you know?"
            scene v5473 with dissolve
            z "Yeah..."
            scene v5474 with dissolve
            jnfr "Poor Gabbie, though. Mother has nothing to do but boss her around now."
            scene v5475 with dissolve
            z "Actually-"
            scene v5476 with dissolve
            jnfr "Did you know an alchemist in a nearby city wanted to take Gabbie as his apprentice?! The only reason she didn't go was because mother wouldn't to let her! Can you imagine?! It was a great opportunity!"
            scene v5477 with dissolve
            z "Yeah, about that. Gabbie is actually working at the ninja village now."
            scene v5478 with dissolve
            jnfr "Yeah! And who knows when an opportunity like this will-"
            scene v5479 with dissolve
            jnfr "..."
            scene v5480 with vpunch
            jnfr "Wait, W-What?!"
            scene v5481 with dissolve
            jnfr "How did that happen?!"
            scene v5482 with dissolve
            z "I... 'convinced' your mother to let Gabbie go..."
            scene v5483 with dissolve
            jnfr "You convinced..."
            scene v5484 with vpunch
            jnfr "Are you fucking serious?!"
            scene v5485 with dissolve
            z "Yep."
            scene v5484 with dissolve
            jnfr "Whoa, dude! I didn't think it was possible!"
            scene v5485 with dissolve
            z "Let's just say my method was very... persuasive..."
            scene v5486 with dissolve
            jnfr "You must show me this method of yours one day..." #Smiling
            scene v5487 with dissolve
            z "(Heh...)"
            play sound "audio/meow.wav"
            scene v5488 with dissolve
            "Meow."
            scene v5489 with dissolve
            jnfr "EEEK!"
            play sound "audio/Falling.mp3"
            scene v5490 with vpunch
            pause(0.5)
            scene v5491 with dissolve
            z "UGH..."
            scene v5492 with dissolve
            z "It's just a cat, Jenny..."
            scene v5493 with dissolve
            jnfr "..."
            scene v5494 with dissolve
            jnfr "A cat?"
            scene v5495 with dissolve
            pause(1.2)
            scene v5496 with dissolve
            pause(1.2)
            scene v5495 with dissolve
            pause(1.2)
            scene v5496 with dissolve
            pause(1.2)
            scene v5497 with dissolve
            jnfr "Woops!"
            play audio "audio/cloth.mp3"
            scene v5498 with dissolve
            jnfr "Sorry about that..." #after standing
            scene v5499 with dissolve
            z "Don't worry..."
            scene v5505 with dissolve
            jnfr "I guess I'm just a little spooked about that killer stuff... The streets seem to be well lit and safe though..." #after standing
            scene v5506 with dissolve
            z "Still. If you're going to go to the market tomorrow, promise you'll wait for me to walk you back to the inn."
            scene v5507 with dissolve
            jnfr "Okay... It's a date then."
            scene v5508 with dissolve
            jnfr "..."
            scene v5500 with dissolve
            jnfr "Oh no! Your shirt!"
            scene v5502 with dissolve
            z "My shirt?"
            scene v5501 with dissolve
            z "It's fine, I'll wash it later."
            scene v5503 with dissolve
            jnfr "What?! No! It was my fault it got dirty. I'll wash it for you."
            scene v5504 with dissolve
            z "Seriously, don't worry about it. It's not even mine. The jarl's maid gave us clothes when we got here."
            scene v5505 with dissolve
            jnfr "Well, at least let me give you something at the inn. Jamie has plenty of clothes he doesn't use. He won't even notice it's gone."
            scene v5506 with dissolve
            z "Alright, alright. You convinced me."
            scene v5507 with dissolve
            jnfr "Heheh. Just like you did my mother."
            scene v5508 with dissolve
            z "Heh. Yeah... (Just like I 'did' your mother.)"
            pause(0.7)
            stop background_s fadeout 1.0
            stop background_s2 fadeout 1.0
            scene v5509 with Fade(0.5,1.5,0.5)
            pause(0.7)
            z "Cozy."
            scene v5510 with dissolve
            jnfr "Eh... It's fine... It's just a little boring."
            jnfr "Nothing ever happens here. I just keep getting left in the room while Jamie is out meeting those..."
            scene v5511 with dissolve
            jnfr "'Important people.'"
            scene v5512 with dissolve
            z "*Chuckles. Yeah... I can imagine that..."
            scene v5513 with dissolve
            jnfr "Got some clean clothes out for you in the closet, by the way."
            jnfr "I don't think the shirt I got you will go with your pants. So I got you some pants too. Go try them on."
            scene v5514 with dissolve
            z "Alright."
            pause(0.7)
            z "Er... Where's the closet? I don't see any..."
            scene v5515 with dissolve
            jnfr "Dude! It's right there!"
            scene v5516 with dissolve
            z "What are you talking about? There isn't a closet!"
            jnfr "..."
            scene v5517 with dissolve
            jnfr "TA-DA!"
            scene v5518 with dissolve
            z "Huh?!"
            scene v5519 with dissolve
            jnfr "What?"
            scene v5518 with dissolve
            z "You mean this room?"
            scene v5519 with dissolve
            jnfr "Yeah. It's the closet room."
            scene v5518 with dissolve
            z "The closet..."
            z "What?! You have a room that's just a closet?!" with vpunch
            scene v5520 with dissolve
            jnfr "*Giggles. Yeah. I told you Jamie has way too many clothes."
            scene v5521 with dissolve
            z "..."
            scene v5522 with dissolve
            jnfr "You going in or what?"
            scene v5523 with dissolve
            z "Uhm... Yeah."
            pause(0.7)
            #Goes in.
            scene v5524 with Fade(0.5,1.5,0.5)
            play sound "audio/Door close.mp3"
            pause(0.7)
            z "(Gods! Two people could live in here.)"
            label G13:
                $ persistent.g_13_unlock = 1
            play audio "audio/cloth.mp3"
            scene v5525 with dissolve
            z "*Sighs. (Let's just change...)"
            play audio "audio/cloth.mp3"
            play sound "audio/door_lock.mp3"
            scene v5526 with dissolve
            "*Room door unlocking sound."
            scene v5527 with dissolve
            #Render turns to closet's door.
            jamie "Hello, my dear. I'm back!"
            jnfr "Huh?! Jamie?! You're early!"
            z "(What's going on out there? I hear voices...)"
            #Door opens jenny comes in.
            play sound "audio/creaky door.mp3"
            scene v5528 with dissolve
            pause(0.5) #She leans on the door sitting down looking behind her at the door.
            scene v5529
            play sound "audio/Door slam.mp3"
            with vpunch
            pause(0.7)
            scene v5530 with dissolve
            jnfr "J-Just a second, Jamie. I'm changing!"
            scene v5531 with dissolve
            #Still looking behind her at the door.
            jnfr "*Whispering. Listen, Jamie can't know you're here, okay? So don't make a sound."
            scene v5532 with dissolve
            jnfr "I'll distract him while you-"
            #Looks to the front, her face is agains z's dick.
            scene v5533 with dissolve
            jnfr "..."
            play background_s "audio/heartbeat.mp3" volume 0.5 fadeout 1.0 fadein 1.0 loop
            scene v5534 with dissolve
            jnfr "You..."
            scene v5535 with dissolve
            z "..."
            scene v5536 with dissolve
            z "(C'mon! Don't look at me helplessly like that... I can't control it if you do...)"
            scene v5537 with dissolve
            pause(0.25)
            scene v5538 with dissolve
            pause(0.25)
            stop background_s fadeout 1.0
            play music "audio/sex music.mp3" volume 0.1 fadeout 1.0 fadein 1.0 loop
            scene v5539 with dissolve
            pause(0.7)
            z "(Look what you've done...)"
            z "(Gods... I knew Jenny since I was a kid... She's like an older sister to me... This is so awkward...)"
            z "(Why isn't she saying anything...)"
            z "(She's just sitting there looking at it...)"
            scene v5540 with dissolve
            z "(Shit... It's dripping precum...)"
            scene v5541 with dissolve
            pause(0.5)
            scene v5542 with dissolve
            z "(Oh, fuck me!)"
            play audio "audio/magic 7.mp3"
            scene v5543 with dissolve
            pause(0.7)
            scene v5544 with dissolve
            z "(Huh?! What was that? I felt a little magical aura just now...)"
            scene v5545 with dissolve
            pause(0.5)
            scene v5546 with dissolve
            jnfr "*Licks it off."
            z "(Holy fuck!)" with vpunch
            scene v5547 with dissolve
            z "Ah... (Her face... It's so soft against my dick... What in the fuck is she-)"
            scene v5548 with dissolve
            jnfr "Hah..."
            scene v5549 with dissolve
            pause(0.7)
            scene v5m11 with dissolve
            z "(Holy fuck! She's licking it...)"
            z "(That's it. She has lost her mind. Her betrothed is just behind the door...)"
            z "Hah... Jenny..."
            scene v5550 with dissolve
            jnfr "..."
            if came_from_gallery <> 1:
                $ jnfr_lst += 1
                show screen button_lst with dissolve
                play sound "audio/stats.wav"
                hide screen button_lst with dissolve
            pause(0.7)
            jamie "Jenny? What's taking so long?! Hurry up!"
            stop music fadeout 1.0
            scene v5551 with dissolve
            jnfr "..."
            scene v5552
            play sound "audio/Slap2.mp3"
            with vpunch
            jnfr "AH! The fuck am I doing?!"
            z "AWW! (My dick!)"
            play audio "audio/creaky door.mp3"
            scene v5553 with dissolve
            scene v5554
            play sound "audio/Door slam.mp3"
            with vpunch
            "*Slams door on her way out."
            pause(0.7)
            z "(Well... I guess the show is over... But what the hell had gotten into her just now?!)"
            pause(0.5)
            jnfr "C'mon! Jamie! There's something you really need to see!"
            pause(1.5)
            "*Sound of both leaving the room."
            z "(I guess that's my queue to get out of here...)"
            $ renpy.end_replay()
            if came_from_gallery == 1:
                $ came_from_gallery = 0
                jump gallery_2
        "Tell her to wait for Jamie to escort her back.":
            z "Anyway, you shouldn't walk there alone. Maybe wait for your betrothed to escort you."
            jnfr "..."
            scene v5461 with dissolve
            jnfr "Y-Yeah... You're right..."
            scene v5462 with dissolve
    pause(0.7)
    scene black with fade
    stop background_s fadeout 1.0
    stop background_s2 fadeout 1.0
    stop music fadeout 1.0
    stop sound fadeout 1.0
    pause(2.5)
    play background_s2 "audio/Ambient_ninja_village_night.mp3" volume 0.6 fadeout 1.0 fadein 1.0 loop
    scene v5555 with dissolve
    pause(1.5)
    scene v5556 with dissolve
    pause(0.7)
    z "(Home, sweet home...)"
    pause(0.5)
    stop background_s fadeout 1.0
    stop background_s2 fadeout 1.0
    play music "audio/Mansion.mp3" volume 0.25 fadeout 1.0 fadein 1.0 loop
    scene v5557 with Fade(0.5,1.5,0.5)
    pause(0.7)
    scene v5558 with dissolve
    daiana "Good evening, sir [mc_name]."
    scene v5557 with dissolve
    z "Oh. Hi, Daiana. Are the others back?"
    scene v5558 with dissolve
    daiana "Yes. They've retired to their rooms for the night."
    scene v5557 with dissolve
    z "(So they all made it back safely. That's good.)"
    scene v5558 with dissolve
    daiana "The mistress has asked me to prepare the bath for your return."
    scene v5557 with dissolve
    z "Oh? That sounds nice."
    z "(I've been treated to a few quality baths lately. A bath in a mansion like this is not likely to dissapoint either.)"
    scene v5558 with dissolve
    daiana "Please go through the door to your right. You'll find a clean change of clothes prepared for you there. Leave what you're wearing now in the room and enter the bath."
    scene v5557 with dissolve
    z "Got it. Thanks, Daiana."
    scene v5558 with dissolve
    daiana "You're very welcome, sir [mc_name]."
    scene v5557 with dissolve
    pause(0.7)
    play background_s "audio/water.mp3" volume 0.8 fadeout 1.0 fadein 1.0 loop
    scene v5559 with Fade(0.5,1.5,0.5)
    pause(0.7)
    z "..."
    z "Whoa! Is this the bath! It's huge! And luxurious!"
    serena "Why thank you, sweety. I picked its design myself."
    label G14:
    scene v5560 with dissolve
    z "H-Huh?!"
    scene v5561 with dissolve
    pause(0.7)
    scene v5562 with dissolve
    serena "Johan thought it was a waste of money. Can you believe it?"
    play music "audio/sex music.mp3" volume 0.3 fadeout 1.0 fadein 1.0 loop
    scene v5563 with dissolve
    z "*Gulps."
    scene v5564 with dissolve
    serena "Cat got your tongue?"
    scene v5565 with dissolve
    z "Er... I'm sorry for intruding on you, Mrs Schwartz. It's just... Daiana said the bath was ready for me..."
    scene v5566 with dissolve
    serena "Well, Yes. It is."
    serena "Please don't mind me. I'm just enjoying the sound of the water."
    serena "And the company of a handsome young man..." #Flirty.
    scene v5565 with dissolve
    z "..."
    scene v5566 with dissolve
    serena "You're not shy to bathe with me around, are you, honey? I'm old enough to be your mother."
    scene v5565 with dissolve
    z "..."
    scene v5567 with dissolve
    serena "Maybe you are shy, after all. Should I leave?"
    scene v5568 with dissolve
    define affair_w_serena = 0
    menu:
        "Ask her to leave.":
            z "Sorry, yeah... I'm a bit uncomfortable bathing in front of you..."
            scene v5567 with dissolve
            serena "Oh... Well, I'll leave to your bath then."
            scene v5568 with dissolve
        "[ModGreen]Tell her she can stay.":
            $ persistent.g_14_unlock = 1
            $ affair_w_serena = 1
            z "Uhm... N-No. I don't mind the company."
            scene v5570 with dissolve
            serena "Heh. I knew I liked you..."
            scene v5569 with dissolve
            z "..."
            scene v5572 with dissolve
            serena "Well? You're not going to bathe fully clothed, are you?"
            scene v5573 with dissolve
            z "Er... No. Just a second..."
            menu:
                "Undress.":
                    $ dummy += 1
            pause(0.8)
            play sound "audio/cloth.mp3"
            pause(0.8)
            # serena is surprised by z's dick
            scene v5571 with dissolve
            serena "!"
            scene v5572 with dissolve
            serena "Quite gifted in certain... areas, aren't you?"
            scene v5573 with dissolve
            z "You could say that..."
            scene v5574 with dissolve
            serena "Hop into the circular small pool. The water in there is nice and warm."
            scene v5575 with dissolve
            z "Okay..."
            # Goes into pool
            scene v5576 with Fade(0.5,1.5,0.5)
            pause(0.7)
            z "..."
            scene v5577 with dissolve
            z "You're right. It's really nice-"
            play sound "audio/splash.wav"
            scene v5578 with dissolve
            z "!"
            scene v5579 with dissolve
            serena "Got room for one more in here?"
            z "(Gods...)"
            play sound "audio/splash.wav"
            scene v5580 with dissolve
            serena "Like what you see?"
            scene v5581 with dissolve
            z "Yeah... A lot..."
            scene v5582 with dissolve
            serena "*Giggles. Aren't you a sweetheart?"
            serena "Want mommy to help you clean yourself?"
            scene v5583 with dissolve
            z "(Mommy?!)"
            define calling_serena_mommy = 0
            menu:
                "Yes, mommy. [ModGreen](Little more perverted content)":
                    $ calling_serena_mommy = 1
                    z "Yes. Please help me bathe, mommy."
                    scene v5584 with dissolve
                    serena "Okay, dear. Mommy will clean you up."
                    scene v5585 with dissolve
                    serena "Hm?"
                    scene v5586 with dissolve
                    pause(1.2)
                    scene v5587 with dissolve
                    serena "You know... It's not very well mannered to point that thing at your mom..."
                    scene v5588 with dissolve
                    serena "Naughty boy... Maybe mommy should punish you..."
                    scene v5590 with dissolve
                    pause(0.7)
                    z "(Whoa! This is really happening...)"
                    scene v5591 with dissolve
                    serena "Just relax, dear. Mommy will take care of you."
                    show v5m12 with dissolve
                    z "(Fuck! This is amazing. She knows exactly what she's doing...)"
                    scene v5592 with dissolve
                    serena "Does that feel good, dear?"
                    scene v5593 with dissolve
                    z "Hah... Yeah..."
                    scene v5592 with dissolve
                    serena "Want mommy to make you cum?"
                    scene v5593 with dissolve
                    z "Yes, please."
                    scene v5592 with dissolve
                    serena "Ah... But this was supposed to be a punishment..."
                    scene v5594 with dissolve
                    serena "Maybe this will make you reflect on what you did."
                    scene v5595 with dissolve
                    z "Huh?"
                    #Jumps on him.
                    scene v5596 with vpunch
                    z "!"
                    scene v5600 with dissolve
                    serena "Let me ask you something, my boy."
                    #Grabs his dick
                    scene v5601 with dissolve
                    serena "Did you ever fuck a woman?"
                    z "Ah!"
                    scene v5597 with dissolve
                    z "..."
                    scene v5599 with dissolve
                    if nxi_aff >= 2:
                        z "Er... I did, actually. Twice..."
                    else:
                        z "Er... I did, actually. Once..."
                    scene v5598 with dissolve
                    serena "Oh? Mommy is proud of you."
                    serena "Her handsome boy with his handsome cock... What woman wouldn't want him?"
                    scene v5601 with dissolve
                    serena "Now, tell me the truth, boy."
                    serena "Do you desire me, your mom?"
                    serena "Do you want to fuck your mommy?"
                    scene v5602 with dissolve
                    serena "Want to go into mommy's pussy?"
                    z "(Gods... Her teasing is just... I'm almost in...)"
                    serena "Don't lie."
                    serena "Tell the truth and maybe mommy will let you in."
                    z "Yes..."
                    serena "Yes, what?"
                    z "..."
                    z "Yes, mommy. I want to fuck you."
                    scene v5603 with dissolve
                    serena "*Fake Gasp. My boy desires me, after all..."
                    serena "What to do... Oh, what to do..."
                    serena "Oh, but this is so wrong..."
                    serena "Maybe I shouldn't..."
                    scene v5604 with vpunch
                    pause(1)
                    scene v5605 with dissolve
                    serena "AHHH!"
                    z "UH! (So sudden...)"
                    scene v5606 with dissolve
                    serena "Hah... I'm sorry, dear. Mommy just couldn't help herself."
                    show v5m13 with dissolve
                    serena "Ah... Oh... Your cock ah... Is so..."
                    serena "It's reaching... Agh... so... deep..."
                    z "Ah... Yeah..."
                    z "Ready to go faster?"
                    scene v5607 with dissolve
                    serena "Eh? F-Faster? I'm not sure-"
                    scene v5608 with vpunch
                    serena "!"
                    show v5m14 with dissolve
                    serena "Ah! W-Wait! That's too... Ah... Fahhhst..."
                    call screen continue_anim with dissolve
                    serena "Hah... You're breahhking your mommy with your... ahh... cock..."
                    scene v5609 with dissolve
                    serena "Aha!"
                    z "Maybe mommy shouldn't have been such a tease then..."
                    show v5m15 with dissolve
                    serena "Gah... Yeah... Punish me... I'm such... Ah... a bad mom..."
                    serena "Ah... Reshape mommy's insides with your cock..."
                    z "Hah... I'm cumming."
                    call screen continue_anim with dissolve
                    scene v5610 with dissolve
                    z "Should I pull out, or?"
                    scene v5611 with dissolve
                    serena "Uh... Oh... Whatever you want, honey... Oh... Mommy won't complain..."
                    hide v5m15
                    show v5m15 with dissolve
                    menu:
                        "Fill mommy up.":
                            scene v5612 with vpunch
                            serena "Guh..."
                            z "Hah... Hufh... Hahh..."
                            scene v5617 with dissolve
                            serena "Oh, honey..."
                            serena "Look what you've done. You might've gone and knocked mommy up..."
                            z "(Hell! This woman's dirty talk could've made me cum on it's own...)"
                            scene v5618 with dissolve
                            z "Mommy didn't seem to mind when I did it."
                            scene v5617 with dissolve
                            serena "Hehehe. She didn't. Maybe you and I will get to do this again..."
                            scene v5618 with dissolve
                            z "Gods! That'd be awesome..."
                            scene v5617 with dissolve
                            serena "Now go get some sleep, my brave little ninja, you have a lot to do tomorrow."
                        "Paint mommy's back.":
                            scene v5613 with dissolve
                            serena "Go on, honey. Let it out on my back."
                            scene v5614 with dissolve
                            pause(0.7)
                            scene v5615 with dissolve
                            pause(1.2)
                            scene v5617 with dissolve
                            serena "Oh, honey..."
                            serena "Look what you've done. You've soiled mommy's back. Now I have to wash myself again..."
                            z "(Hell! This woman's dirty talk could've made me cum on it's own...)"
                            scene v5618 with dissolve
                            z "Mommy didn't seem to mind when I did it."
                            scene v5617 with dissolve
                            serena "Hehehe. She didn't. Maybe you and I will get to do this again..."
                            scene v5618 with dissolve
                            z "Gods! That'd be awesome..."
                            scene v5617 with dissolve
                            serena "Now go get some sleep, my brave little ninja, you have a lot to do tomorrow."
                    menu:
                        "Okay, mommy.":
                            scene v5618 with dissolve
                            z "Yes, mom."

                        "Okay.":
                            scene v5618 with dissolve
                            z "Yeah..."
                "Yes, ma'am.":
                    z "Yes, please, ma'am."
                    scene v5584 with dissolve
                    serena "Very well then. I'll help clean you up."
                    scene v5585 with dissolve
                    serena "Hm?"
                    scene v5586 with dissolve
                    pause(0.7)
                    scene v5587 with dissolve
                    serena "You know... It's not very well mannered to point that thing at a lady..."
                    scene v5588 with dissolve
                    serena "Naughty boy... Maybe I should punish you..."
                    scene v5590 with dissolve
                    pause(0.7)
                    z "(Whoa! This is really happening...)"
                    scene v5591 with dissolve
                    serena "Just relax, honey. I will take care of you."
                    show v5m12 with dissolve
                    z "(Fuck! This is amazing. She knows exactly what she's doing...)"
                    scene v5592 with dissolve
                    serena "Does that feel good, honey?"
                    scene v5593 with dissolve
                    z "Hah... Yeah..."
                    scene v5592 with dissolve
                    serena "Want to cum?"
                    scene v5593 with dissolve
                    z "Yes, please."
                    scene v5592 with dissolve
                    serena "Ah... But this was supposed to be a punishment..."
                    scene v5594 with dissolve
                    serena "Maybe this will make you reflect on what you did."
                    scene v5595 with dissolve
                    z "Huh?"
                    #Jumps on him.
                    scene v5596 with vpunch
                    z "!"
                    scene v5600 with dissolve
                    serena "Let me ask you something, boy."
                    #Grabs his dick
                    scene v5601 with dissolve
                    serena "Did you ever fuck a woman?"
                    z "Ah!"
                    scene v5597 with dissolve
                    z "..."
                    scene v5599 with dissolve
                    if nxi_aff >= 2:
                        z "Er... I did, actually. Twice..."
                    else:
                        z "Er... I did, actually. Once..."
                    scene v5598 with dissolve
                    serena "Oh? I'm not surprised."
                    serena "A handsome face and a handsome cock like yours. What woman wouldn't want that?"
                    scene v5601 with dissolve
                    serena "Now, tell me the truth, boy."
                    serena "Do you desire older married women, like me?"
                    serena "Do you want to fuck me?"
                    scene v5602 with dissolve
                    serena "Want to go into my pussy?"
                    z "(Gods... Her teasing is just...)"
                    serena "Don't lie."
                    serena "Tell the truth and maybe I'll let you in."
                    z "Yes..."
                    serena "Yes, what?"
                    z "..."
                    z "Yes. I want to fuck you."
                    scene v5603 with dissolve
                    serena "*Fake Gasp. This young handsome boy desires me, after all..."
                    serena "What to do... Oh, what to do..."
                    serena "Oh, but I'm a married woman..."
                    serena "Maybe I shouldn't..."
                    scene v5604 with vpunch
                    pause(1)
                    scene v5605 with dissolve
                    serena "AHHH!"
                    z "UH! (So sudden...)"
                    scene v5606 with dissolve
                    serena "Hah... I'm sorry, honey. I just couldn't help myself."
                    show v5m13 with dissolve
                    serena "Ah... Oh... Your cock ah... Is so..."
                    serena "It's reaching... Agh... so... deep... It's much bigger than my husband's..."
                    z "Ah... Yeah..."
                    z "Ready to go faster?"
                    scene v5607 with dissolve
                    serena "Eh? F-Faster? I'm not sure-"
                    scene v5608 with vpunch
                    serena "!"
                    show v5m14 with dissolve
                    serena "Ah! W-Wait! That's too... Ah... Fahhhst..."
                    call screen continue_anim with dissolve
                    serena "Hah... You're breahhking me with your... ahh... cock... My husband will never be able... Hah... to satisfy me again."
                    scene v5609 with dissolve
                    serena "Aha!"
                    z "Maybe you shouldn't have been such a tease then... Mrs. Schwartz."
                    show v5m15 with dissolve
                    z "Do you often tease your husband like this?"
                    serena "Gah... Yeah... Punish me... I'm such... Ah... a bad wife..."
                    serena "Ah... Reshape my pussy with your cock..."
                    z "Hah... I'm cumming."
                    call screen continue_anim with dissolve
                    scene v5610 with dissolve
                    z "Should I pull out, or?"
                    scene v5611 with dissolve
                    serena "Uh... Oh... Whatever you want, honey... Oh... I'm sure Johan won't complain..."
                    hide v5m15
                    show v5m15 with dissolve
                    menu:
                        "Fill her up.":
                            scene v5612 with vpunch
                            serena "Guh..."
                            z "Hah... Hufh... Hahh..."
                            scene v5617 with dissolve
                            serena "Oh, honey..."
                            serena "Look what you've done. You might've gone and knocked me up... How will I explain to my husband how I got pregnant?"
                            z "(Hell! This woman's dirty talk could've made me cum on it's own...)"
                            scene v5618 with dissolve
                            z "Well, his wife didn't seem to mind when I did it."
                            scene v5617 with dissolve
                            serena "Hehehe. She didn't. Maybe you and I will get to do this again..."
                            scene v5618 with dissolve
                            z "Gods! That'd be awesome..."
                            scene v5617 with dissolve
                            serena "Now go get some sleep, my brave little ninja, you have a lot to do tomorrow."
                        "Paint her back.":
                            scene v5613 with dissolve
                            serena "Go on, honey. Let it out on my back."
                            scene v5614 with dissolve
                            pause(0.7)
                            scene v5615 with dissolve
                            pause(1.2)
                            scene v5617 with dissolve
                            serena "Oh, honey..."
                            serena "Look what you've done. You've soiled my back. Now I have to wash myself again... Can't very well go sleep next to my husband like this, can I?"
                            z "(Hell! This woman's dirty talk could've made me cum on it's own...)"
                            scene v5618 with dissolve
                            z "Well, his wife didn't seem to mind when I did it."
                            scene v5617 with dissolve
                            serena "Hehehe. She didn't. Maybe you and I will get to do this again..."
                            scene v5618 with dissolve
                            z "Gods! That'd be awesome..."
                            scene v5617 with dissolve
                            serena "Now go get some sleep, my brave little ninja, you have a lot to do tomorrow."
    $ renpy.end_replay()
    if came_from_gallery == 1:
        $ came_from_gallery = 0
        jump gallery_2
    pause(0.7)
    stop background_s fadeout 1.0
    stop background_s2 fadeout 1.0
    stop music fadeout 1.0
    stop sound fadeout 1.0
    scene black with fade
    "The ball is in two days..."
    define dont_believe_irna = 0
    pause(2.5)
    play background_s2 "audio/Ambient_ninja_village.mp3" volume 0.4 fadeout 1.0 fadein 1.0 loop
    scene v5620 with dissolve
    pause(0.7)
    z "(Oh? Looks like Anabelle is alone this time.)"
    scene v5621 with dissolve
    z "Good morning."
    scene v5622 with dissolve
    a "Good morning, [mc_name]."
    scene v5621 with dissolve
    z "Uhm... Where are Torr and Candy?"
    scene v5623 with dissolve
    a "They set off to investigate already. They're pretty excited."
    scene v5624 with dissolve
    z "*Chuckles. That's good, I suppose."
    z "Any leads on your end?"
    scene v5625 with dissolve
    a "Nothing decisive, really."
    a "You?"
    scene v5626 with dissolve
    z "Well..."
    z "Remember the girl that showed up with Axius? His daughter Irena?"
    scene v5627 with dissolve
    a "Hm..."
    scene v5625 with dissolve
    a "Not particularly, no."
    if succubus_incountered >= 1:
        scene v5626 with dissolve
        z "She was one of the girls that ambushed me in the forest."
        scene v5625 with dissolve
        a "Oh... Right..."
        scene v5628 with dissolve
        a "Well? What about her?"
    else:
        scene v5628 with dissolve
        a "What about her?"
    scene v5626 with dissolve
    z "I met her yesterday. She was in the square."
    scene v5629 with dissolve
    a "What?! You 'met' her?! Did she not attack you?" #Surprised
    scene v5630 with dissolve
    z "Well it was I that sort of attacked her. She only defended herself. She said she was no longer after me."
    a "..."
    scene v5629 with dissolve
    a "Why is she here then?"
    scene v5630 with dissolve
    z "Came to visit a friend of hers. The butcher apparently killed her. So now, she's after the butcher too."
    scene v5627 with dissolve
    a "Hm..."
    scene v5628 with dissolve
    a "Well, it could be that she's telling the truth..."
    scene v5632 with dissolve
    a "But it might also be a plot to make you let your guard down, so that she can lure you somewhere for example."
    scene v5633 with dissolve
    z "Well... That's not all."
    a "Hm?"
    scene v5626 with dissolve
    z "I remember her, Anabelle. I saw her in my dreams sometimes, back when I was living in that cave."
    z "In my memories, or, well... dreams... We were younger. We played together."
    scene v5625 with dissolve
    a "Go on."
    scene v5626 with dissolve
    z "I asked her about it. She said her father knew mine, they were friends, and that she used to come to my house often and we'd play..."
    a "..."
    z "What do you think about all of this?"
    scene v5625 with dissolve
    a "The more important question is what YOU think, [mc_name]."
    scene v5626 with dissolve
    z "... I think..."
    menu:
        "I believe her. [ModGreen](Recommended, for now)":
            z "I... believe her..."
            z "I've agreed to meet with her today and investigate some lead together. I want to go."
            a "Hm..."
            if a_trst >= 3:
                scene v5634 with dissolve
                a "Okay, [mc_name]. I trust your judgement, and your ability."
                scene v5635 with dissolve
                z "..."
                z "(Whoa... That's actually quite nice to hear...)"
                scene v5632 with dissolve
                a "That said, if you don't make it back here by midnight. I'm going to go looking for you. Deal?"
                scene v5633 with dissolve
                z "*Chuckles. Yeah. Deal."
                scene v5635 with dissolve
                pause(0.7)
            else:
                scene v5625 with dissolve
                a "I suppose this would prove whether she's telling the truth or not."
                scene v5632 with dissolve
                a "I'll keep a loose follow. See where this goes. If she's telling the truth, we might learn something. If not, we'll know never to trust her again."
                scene v5633 with dissolve
                z "Yeah. You're right."
                pause(0.7)
        "I don't believe her.":
            $ dont_believe_irna = 1
            z "I don't think I believe her. I think she's still hiding something."
            z "But I want to see where this could lead, as well. So..."
            z "I've agreed to meet with her today and investigate some lead together. I think I'll go."
            scene v5629 with dissolve
            a "But you said yourself it might be a trap."
            scene v5630 with dissolve
            z "I can handle myself. It won't be the same as last time if she tries something."
            a "Hm..."
            if a_trst >= 3:
                scene v5634 with dissolve
                a "Okay, [mc_name]. I trust your judgement, and your ability."
                scene v5635 with dissolve
                z "..."
                z "(Whoa... That's actually quite nice to hear...)"
                scene v5632 with dissolve
                a "That said, if you don't make it back here by midnight. I'm going to go looking for you. Deal?"
                scene v5633 with dissolve
                z "*Chuckles. Yeah. Deal."
                scene v5635 with dissolve
                pause(0.7)
            else:
                scene v5625 with dissolve
                a "I suppose this would prove whether she's telling the truth or not."
                scene v5632 with dissolve
                a "I'll keep a loose follow. See where this goes. If she's telling the truth, we might learn something. If not, we'll know never to trust her again."
                scene v5633 with dissolve
                z "Yeah. You're right."
                pause(0.7)
    scene v5635 with dissolve
    z "Well... I'm off to the market then."
    scene v5634 with dissolve
    a "Good luck. And be careful."
    scene v5635 with dissolve
    pause(0.7)
    scene black with fade
    pause(2.5)
    scene v5636 with dissolve
    play music "audio/Esyl.mp3" volume 0.4 fadeout 1.0 fadein 1.0 loop
    z "There she is."
    scene v5637 with dissolve
    pause(0.5)
    scene v5638 with dissolve
    irna "[mc_name]."
    scene v5637 with dissolve
    z "Irena."
    scene v5638 with dissolve
    irna "So... Not having second thought, are you?"
    scene v5637 with dissolve
    z "Huh? No. What makes you ask that?"
    scene v5639 with dissolve
    irna "Meh... Not sure."
    scene v5640 with dissolve
    irna "..."
    scene v5641 with dissolve
    irna "It might be quite dangerous, you know. If she's really involved with this..."
    scene v5642 with dissolve
    z "Well... I'm mostly used to it by now."
    scene v5643 with dissolve
    irna "The tough guy act is cool and all, but did you at least consider your options?"
    scene v5644 with dissolve
    z "Heh. What are you acting like a worried mother all of the sudden for, Irena? I did confer with the Keres before agreeing to do this, if you must know."
    scene v5643 with dissolve
    irna "The Keres?"
    scene v5645 with dissolve
    irna "Seira is here with you?!" #Surprised
    scene v5646 with dissolve
    z "Huh? No. Another Keres."
    scene v5647 with dissolve
    irna "Oh, right. That other one... Surrounded by Keres, aren't you? No wonder my father gave up hunting you."
    irna "..."
    scene v5648 with dissolve
    irna "Alright. Let's go kill some time. We'll observe her from afar and follow her home when she's done with her work. Sounds good?"
    scene v5649 with dissolve
    z "Yeah."
    z "(Her attitude changed when she heard about a Keres being here. But for the better, I suppose...)"
    z "(Was she really worried about me after all? Or maybe she thinks we have a better chance to get the butcher with a Keres on our side...)"
    z "(Let's just go through with this for now.)"
    pause(0.7)
    scene black with fade
    stop background_s fadeout 1.0
    stop background_s2 fadeout 1.0
    stop music fadeout 1.0
    pause(2.5)
    play background_s2 "audio/Ambient_ninja_village_night.mp3" volume 0.6 fadeout 1.0 fadein 1.0 loop
    scene v5650 with dissolve
    pause(1.2)
    scene v5651 with dissolve
    pause(1.2)
    scene v5652 with dissolve
    pause(0.7)
    scene v5653 with dissolve
    irna "Alright. Looks like she's leaving."
    scene v5654 with dissolve
    z "Finally. Time to move, then."
    scene v5655 with Fade(0.5,1.0,0.5)
    pause(0.7)
    scene v5656 with dissolve
    pause(0.7)
    play sound "audio/creaky door.mp3"
    scene v5657 with dissolve
    pause(0.7)
    scene v5658 with dissolve
    pause(0.7)
    scene v5659 with dissolve
    pause(0.7)
    scene v5660 with dissolve
    pause(1.2)
    scene v5661 with dissolve
    pause(0.7)
    scene v5662 with dissolve
    pause(0.5)
    scene v5663 with dissolve
    pause(0.7)
    scene v5664 with dissolve
    pause(0.9)
    play sound "audio/door_lock.mp3"
    "*Click."
    pause(0.5)
    play sound "audio/creaky door.mp3"
    scene v5665 with dissolve
    pause(0.7)
    scene v5666 with dissolve
    z "I didn't know you could pick locks!"
    scene v5667 with dissolve
    irna "Plenty of things you don't know about me." #Cocky smile
    scene v5668 with dissolve
    irna "Come on. Let's see where this leads, shall we?"
    stop background_s fadeout 1.0
    stop background_s2 fadeout 1.0
    scene v5669 with Fade(0.5,0.7,0.5)
    pause(1.2)
    play sound "audio/creaky door.mp3"
    scene v5670 with dissolve
    z "Oh. She's coming out."
    scene v5671 with dissolve
    irna "Finally. I thought she might have just gone to sleep for a second."
    z "Whoa... She's almost naked... Hold on! She's carrying something! A bag. A really big one..."
    irna "And her being naked was the first thing you fucking noticed?! I shouldn't have let you be our look-out! How big of a bag are we talking? Can a person fit in there?"
    z "A person? I suppose... A small one... or one chopped to pieces..."
    play sound "audio/creaky door.mp3"
    scene v5672 with dissolve
    z "She's going into the other door..."
    play audio "audio/Door close.mp3"
    scene v5673 with dissolve
    z "She's gone."
    irna "Quick! Let's follow her."
    play background_s "audio/dungeon.mp3" fadeout 1.0 fadein 1.0 loop
    scene v5674 with Fade(0.5,0.7,0.5)
    pause(1.2)
    scene v5675 with dissolve
    pause(1.2)
    scene v5676 with dissolve
    z "Looks like you were right. Something is definitely off about this place."
    scene v5677 with dissolve
    z "She's going into another door... We need to get closer."
    play sound "audio/creaky door.mp3"
    scene v5678 with dissolve
    pause(0.7)
    scene v5679 with dissolve
    z "Let's go."
    scene v5680 with dissolve
    pause(0.7)
    scene v5681 with dissolve
    "*Misty's voice coming back."
    scene v5682 with dissolve
    z "Shit! Hide!"
    scene v5683 with dissolve
    pause(0.7)
    scene v5684 with dissolve
    pause(0.4)
    play audio "audio/Door close.mp3"
    scene v5685 with dissolve
    pause(0.7)
    scene v5686 with dissolve
    pause(0.6)
    scene v5687 with dissolve
    pause(0.6)
    scene v5688 with dissolve
    pause(0.6)
    scene v5689 with dissolve
    pause(0.6)
    scene v5690 with dissolve
    pause(0.7)
    scene v5691 with dissolve
    z "..."
    scene v5692 with dissolve
    z "Alright. The coast is clear."
    scene v5693 with Fade(0.5,0.5,0.5)
    pause(0.4)
    z "What do you figure is behind this door."
    scene v5694 with dissolve
    irna "No idea. But we'd better be prepared for anything. You noticed how she came out of here without the bag she was carrying?"
    scene v5693 with dissolve
    z "Yeah..."
    pause(0.7)
    menu:
        "Open the door.":
            $dummy += 1
    pause(0.4)
    play sound "audio/creaky door.mp3"
    scene v5695 with dissolve
    pause(1.2)
    scene v5696 with dissolve
    play music "audio/creepy ambient.mp3" fadeout 1.0 fadein 1.0 loop
    pause(0.7)
    z "(Fuck! It's blood!)" with vpunch
    "*Vicious devouring sounds."
    z "Huh?! *Whispering: Someone is there, Irena!"
    irna "..."
    z "Irena?"
    pause(0.4)
    menu:
        "Turn to Irena.":
            $dummy += 1
    pause(0.4)
    scene v5697 with dissolve
    irna "..."
    z "..."
    pause(0.4)
    menu:
        "Look up.":
            $dummy += 1
    pause(0.4)
    play sound "audio/Jumpscare (hard).mp3"
    stop music
    scene v5698
    pause(0.4)
    z "(Holy fuck!)" with vpunch
    pause(0.4)
    scene v5699 with dissolve
    z "Fuck! It's coming here!" with vpunch
    scene v5700 with dissolve
    irna "!"
    play sound "audio/slight_hit.mp3"
    scene v5701 with dissolve
    "*Stone hits the wall."
    scene v5702 with dissolve
    pause(0.3)
    scene v5703 with dissolve
    pause(0.7)
    scene v5704 with dissolve
    pause(0.5)
    scene v5705 with dissolve
    pause(1.5)
    scene v5706 with Fade(0.5,1,0.5)
    pause(0.7)
    z "..."
    scene v5707 with dissolve
    pause(1.2)
    scene v5708 with dissolve
    z "What the fuck is that?!"
    scene v5710 with dissolve
    irna "Shit! I had a feeling it was something like this!"
    scene v5711 with dissolve
    z "Huh?! What are you talking about?!"
    scene v5709 with dissolve
    irna "It's obviously her father. He's old enough that he lost most of his intelligence by now."
    scene v5711 with dissolve
    z "The fuck?! How is this obvious?!"
    scene v5709 with dissolve
    irna "Beasts lose their sense of self when they get old. Everyone knows this!"
    scene v5711 with dissolve
    z "I didn't!"
    z "Why didn't you throw the stone further away?!"
    scene v5712 with dissolve
    irna "I was panicking! It's not like you did any better!" #Annoyed
    scene v5713 with dissolve
    z "..."
    scene v5714 with dissolve
    z "(Shit I can feel her breasts pressing on my back)"
    z "(The warmth of her body and breaths...)"
    scene v5715 with dissolve
    z "(I have to think of something else quick!)"
    define irna_hj = 0
    menu:
        "Think about something gross. [ModGreen](Possible Love point)":
            #z closes his eyes
            $ irna_hj = 0
            scene v5739 with dissolve
            z "(Let's think about...)"
            z "(Skeevers! Yeah! How I was eating skeever meat for a few days before I realised what it was...)"
            pause(0.7)
            # Looks down
            scene v5716 with dissolve
            pause(0.7)
            scene v5717 with dissolve
            z "(That seems to have worked...)"
            scene v5715 with dissolve
            z "(Now we just need to wait for the monster to move away from the door...)"
            scene v5742 with Fade(0.5,0.5,0.5)
            pause(0.7)
            scene v5743 with dissolve
            pause(0.3)
            scene v5744 with dissolve
            pause(0.3)
            scene v5745 with dissolve
            pause(0.8)
            z "*Sighs. (Thank the gods... He left...)"
            scene v5736 with Fade(0.5,0.5,0.5)
            pause(0.7)
            scene v5735 with dissolve
            irna "Woosh... That was close..."
            scene v5736 with dissolve
            z "Yeah..."
            scene v5737 with dissolve
            irna "Kinda exciting, though."
            scene v5738 with dissolve
            z "... (I think she and Candy would like each other.)"
            pause(0.7)
            define liked_irnas_hj = 0
            menu:
                "[ModGreen]I guess it was kinda exciting... (Irena Love +1)":
                    z "I suppose it was... In a weird way..."
                    scene v5735 with dissolve
                    irna "Right? I knew you'd get it."
                    scene v5736 with dissolve
                    $ irna_aff += 1
                    show screen button_aff with dissolve
                    play sound "audio/stats.wav"
                    hide screen button_aff with dissolve
                    scene v5735 with dissolve
                    irna "Now let's leave before the spider girl notices something or comes back."
                    scene v5736 with dissolve
                    pause(0.7)

                "Let's not do this again...":
                    z "Nope. That was too crazy for me! Let's not do it again."
                    scene v5737 with dissolve
                    irna "*Sigh. You're no fun..."
                    scene v5735 with dissolve
                    irna "Now let's leave before the spider girl notices something or comes back."
                    scene v5736 with dissolve
                    pause(0.7)
        "[ModGreen]Don't think about something specific. (Irena Lust +1 Possible Love point)":
            label G15:
                $ persistent.g_15_unlock = 1
            scene v5739 with dissolve
            #z closes his eyes
            z "(No need to think about something specific. I just need to calm down. Clear my mind...)"
            scene v5740 with dissolve
            z "(Clear your mind... Just like Hailey used to do...)"
            scene v5740_1 with Dissolve(2)
            pause(1.2)
            scene v5740_2 with Dissolve(2)
            pause(1.7)
            $ irna_hj = 1
            # Looks down
            scene v5739 with Dissolve(2)
            pause(0.7)
            scene v5716 with dissolve
            pause(0.7)
            scene v5718 with dissolve
            z "(Damn it!)"
            scene v5719
            play sound "audio/Cloth_rustle.wav"
            with vpunch
            z "!"
            scene v5720 with dissolve
            irna "Whoa... I didn't think this kind of situation was your thing..." #Cocky smile.
            z "Huh?!"
            irna "Does the thrill of being eaten alive turn you on? I mean, I'm not judging or anything."
            scene v5721 with dissolve
            z "The fuck?! No! Your boobs are pressed against my back, in case you haven't noticed!"
            scene v5720 with dissolve
            irna "Are you sure that's it? I think you find the thrill arousing..."
            scene v5721 with dissolve
            z "No, I don-"
            scene v5722
            play sound "audio/Slap2.mp3"
            with vpunch
            z "Hm!"
            scene v5723 with dissolve
            irna "Shhh... You don't want the spider to hear us, do you?"
            scene v5724 with dissolve
            irna "Let's see how bad the situation is down there."
            play sound "audio/Zip.mp3"
            scene v5725 with dissolve
            "*Unziping sounds."
            scene v5726 with dissolve
            irna "Hm?!"
            scene v5727 with dissolve
            if succubus_incountered >= 1 and didnt_join_waterfall == 0:
                irna "I know I saw it at the waterfall, but now that I'm holding it, it's... Incubi really are different down there, huh?"
            else:
                irna "Incubi really are different down there, huh?"
            play music "audio/sex music 2.mp3" volume 0.2 fadeout 1.0 fadein 1.0 loop
            show v5m16 with Dissolve(1.0)
            pause(0.8)
            z "(Fuck! This girl is crazy!)"
            z "(Why am I letting her do this? It's not like I can't break free...)"
            z "(Although... If I forcefully should break free, I guess the spider might hear us...)"
            z "(Also... I'm not really sure if I want to... I mean... This sort of feels really good...)"
            pause(0.8)
            show v5m17 with dissolve
            if succubus_incountered >= 1:
                irna "Don't worry. I'm not going to suck any energy this time. Just sit back and enjoy it."
            else:
                irna "Don't worry. Even though I'm half succubus, I'm not going to suck any energy from you. Just sit back and enjoy it."
            z "(Gods! For a second, I forgot about that... I don't know if it's the thrill or her technique, but this just feels amazing...)"
            z "(I'm not going to last long...)"
            scene v5730 with dissolve
            irna "The spider is right there, you know. If you make a sound, we're dead."
            scene v5729 with dissolve
            irna "He's not moving at all, though. I think he's enjoying the show."
            scene v5728 with dissolve
            irna "Not as much as your friend down there, though."
            hide v5m17
            show v5m17 with dissolve
            irna "Oh? I can feel you're close. Come on! Let it out!"
            z "Hmm... (I'm cumming...)"
            call screen cum with dissolve
            scene v5731 with vpunch
            pause(0.8)
            scene v5732 with dissolve
            irna "Whoa... That's a lot of cum... What a waste..."
            irna "I guess your friend liked it... Even if you didn't."
            stop music fadeout 1.0
            if came_from_gallery <> 1:
                $ irna_lst += 1
                show screen button_lst with dissolve
                play sound "audio/stats.wav"
                hide screen button_lst with dissolve
            scene v5733 with dissolve
            irna "Oh. Looks like the spider is gone..."
            scene v5734 with dissolve
            irna "Now would be a good time to leave."
            pause(0.7)
            $ renpy.end_replay()
            if came_from_gallery == 1:
                $ came_from_gallery = 0
                jump gallery_2
            scene v5736 with Fade(0.5,0.5,0.5)
            pause(0.7)
            scene v5735 with dissolve
            irna "Woosh... That was close..."
            scene v5736 with dissolve
            pause(0.7)
            z "Are you fucking crazy?!" with vpunch
            scene v5737 with dissolve
            irna "Come on! You have to admit it was extra exciting."
            scene v5738 with dissolve
            pause(0.7)
            define liked_irnas_hj = 0
            menu:
                "[ModGreen]I guess it was kinda exciting... (Irena Love +1)":
                    z "..."
                    scene v5735 with dissolve
                    irna "See?"
                    scene v5736 with dissolve
                    $ irna_aff += 1
                    show screen button_aff with dissolve
                    play sound "audio/stats.wav"
                    hide screen button_aff with dissolve
                    $ liked_irnas_hj = 1
                    scene v5735 with dissolve
                    irna "Now let's leave before the spider girl notices something or comes back."
                    scene v5736 with dissolve
                    pause(0.7)
                "Never pull shit like that again!":
                    z "Nope. That was too crazy for me! Never do that again, okay?"
                    scene v5737 with dissolve
                    irna "*Sigh. Fine... You're no fun..."
                    scene v5735 with dissolve
                    irna "Now let's leave before the spider girl notices something or comes back."
                    scene v5736 with dissolve
                    pause(0.7)
    stop background_s fadeout 1.0
    stop background_s2 fadeout 1.0
    stop music fadeout 1.0
    stop sound fadeout 1.0
    play background_s2 "audio/Ambient_ninja_village_night.mp3" volume 0.4 fadeout 1.0 fadein 1.0 loop
    scene v5747 with Fade(0.5,1,0.5)
    pause(0.7)
    z "So... A dead end after all..."
    scene v5746 with dissolve
    irna "I suppose."
    scene v5747 with dissolve
    z "Seems The bag had simply food in it. What do beasts eat, by the way?"
    scene v5748 with dissolve
    irna "Mostly meat."
    scene v5747 with dissolve
    z "That would explain the blood. What kind of meat are we talking about? Human meat?"
    scene v5749 with dissolve
    irna "Sure. Whatever kind of meat you throw at them. But the butcher leaves the bodies at the scene, remember?"
    scene v5750 with dissolve
    z "Right... So, Misty is probably not our butcher..."
    scene v5749 with dissolve
    irna "Probably not... Or at least, we found no evidence suggesting that she is."
    scene v5750 with dissolve
    z "..."
    scene v5751 with dissolve
    irna "Well, I'm heading back. Had enough excitement for one day."
    irna "If I find anything, I'll be in touch. You know where to find me if you find something yourself."
    scene v5752 with dissolve
    z "Uhm... Not really."
    scene v5753 with dissolve
    irna "Oh, right... I didn't tell you. I have a room at the nearby inn. Not the fancy one, the other one. You can probably find me there."
    scene v5754 with dissolve
    z "Got it. Take care, Irena."
    scene v5755 with dissolve
    irna "Don't try anything too crazy."
    scene v5756 with dissolve
    irna "At least not without me." #Cocky smile
    scene v5757 with dissolve
    z "Heh... Can't promise you that."
    scene v5758 with dissolve
    pause(0.4)
    scene v5759 with dissolve
    pause(1.4)
    # irna leaves.
    $ misty_info = 2
    if escorting_jenny == 1:
        z "(Shit! I'm late! I told Jenny to wait for me!)" with vpunch
        scene v5760 with Fade(0.5,1,0.5)
        pause(0.7)
        z "(I hope she didn't go-"
        scene v5761 with dissolve
        z "-by herself...)"
        scene v5762 with dissolve
        z "(Fuck. She isn't here.)"
        pause(0.7)
        scene v5763 with Fade(0.5,1,0.5)
        pause(1)
        z "(Come on, Jenny! Where are you?)"
        scene v5764 with dissolve
        z "(There!)"
        z "(Thank fuck I found her!)"
        scene v5765 with dissolve
        z "(Huh? Who's that guy?)"
        z "(It's not Jamie, is it?)"
        jnfr "Uhm... N-No please."
        scene v5766 with dissolve
        Character("Some guy") "C'mon, love. It's dangerous alone at night."
        scene v5767 with dissolve
        Character("Some guy") "I'll keep you safe." #Touches her
        scene v5768 with dissolve
        jnfr "S-Stop!"
        scene v5769 with dissolve
        jnfr "EEEK!" with vpunch
        Character("Some guy") "Playing hard to get after wearing such nice clothes and walking around alone at night?"
        z "(Fucker!)"
        menu:
            "Punch him. [ModGreen](Recommended)":
                pause(0.5)
                play audio "audio/Punch.wav"
                pause(0.3)
                scene v5770 with vpunch
                pause(1)
                scene v5771
                play sound "audio/Falling2 (loud).mp3"
                with vpunch
                z "(Woops... Looks like I punched too hard...)"
                scene v5772 with dissolve
                jnfr "Holy fuck, dude! You killed him!"
                scene v5773 with dissolve
                z "Huh? He's not d-dead!"
                z "I think..."
                scene v5774 with dissolve
                Character("Some guy") "*Snores."
                jnfr "..."
                z "See?"
                scene v5775 with dissolve
                jnfr "*laughs."
                scene v5776 with dissolve
                z "Sorry I was late. You should've waited for me, though."
                scene v5777 with dissolve
                jnfr "Yeah... Sorry..."
                scene v5776 with dissolve
                z "Come on. Let's get you back to the inn."
            "Tell him off.":
                pause(0.5)
                scene v5778 with vpunch
                z "Whoa there! What do you think you're doing, buddy?!"
                scene v5779 with dissolve
                Character("Some guy") "Huh? And who are you? I'm just talking to my girl. Got a problem?"
                scene v5780 with dissolve
                jnfr "The fuck?! Your girl?!"
                scene v5781 with dissolve
                jnfr "Actually, this is my betrothed. I was just waiting for him to escort me to the inn. You know? The Gold Fish inn."
                scene v5782 with dissolve
                Character("Some guy") "Wait what?! The Gold Fish?! Y-You guys are that rich?"
                scene v5783 with dissolve
                z "You heard the lady, pal. So, how about you fuck off before I call one of my guards?"
                Character("Some guy") "..."
                scene v5784 with dissolve
                Character("Some guy") "*Leaves."
                scene v5785 with dissolve
                z "Sorry I was late. You should've waited for me, though."
                scene v5786 with dissolve
                jnfr "Yeah... Sorry..."
                scene v5785 with dissolve
                z "Come on. Let's get you back to the inn."
        scene v5787 with Fade(0.5,1,0.5)
        pause(0.7)
        z "Well. Here we are."
        z "I don't need a new shirt this time, I guess."
        scene v5788 with dissolve
        jnfr "..." #Embarrased
        z "(Woops! Looks like I embarrassed her...)"
        scene v5789 with dissolve
        jnfr "Rrrriiiight..."
        scene v5790 with dissolve
        jnfr "On another note..."
        jnfr "My luck has turned to shit ever since you showed up, you know."
        scene v5791 with dissolve
        jnfr "First, I hear there's a guy going around murdering women." #Playful smile
        scene v5792 with dissolve
        jnfr "Then, the next thing I know, some other guy is harrassing me in the middle of the street..."
        scene v5793 with dissolve
        z "You didn't seem to mind when I showed up to rescue you from said other guy."
        z "(Smooth... She knows how to get herself out of an awkward situation.)"
        scene v5794 with dissolve
        jnfr "Eh... I get a lot of this. I could've handled it. You just made it faster, is all."
        scene v5795 with dissolve
        z "I don't know, you looked like a maiden in distress to me."
        scene v5796 with dissolve
        jnfr "Trust me, dude, you're more of maiden in distress than I am."
        scene v5797 with dissolve
        z "Sure, sure. Whatever you say."
        jnfr "..."
        scene v5798 with vpunch
        jnfr "Jamie?!"
        scene v5799 with dissolve
        z "Huh?!"
        scene v5800 with dissolve
        pause(0.7)
        play audio "audio/kiss.mp3"
        scene v5801 with dissolve
        jnfr "*kisses you."
        scene v5802 with dissolve
        jnfr "Jokes aside... Thanks, [mc_name]."
        scene v5803 with dissolve
        $ jnfr_aff += 2
        show screen button_aff with dissolve
        play sound "audio/stats.wav"
        hide screen button_aff with dissolve
        z "Please wait for me tomorrow, okay?"
        scene v5804 with dissolve
        jnfr "Eh... I'm not going to the market tomorrow. We're leaving the day after tomorrow, anyway. Might as well pack my things and get ready."
        scene v5805 with dissolve
        z "Oh? Are you going back home?"
        scene v5806 with dissolve
        jnfr "Yeah. Mother sent me a letter saying she moved to a nearby village. So I'm going there."
        scene v5807 with dissolve
        z "I see... I guess, I'll see you there, then."
        scene v5806 with dissolve
        jnfr "Sure. It's not far from the ninja village. Maybe you and Gabbie can come visit some time."
        scene v5807 with dissolve
        z "Yeah..."
        pause(0.7)
        z "Well. Good night, Jenny."
        scene v5808 with dissolve
        jnfr "Good night."
        scene v5809 with dissolve
        pause(0.5)
        scene v5810 with dissolve
        pause(1.2)
        scene v5811 with dissolve
        z "(Hm? Is that...)"
    else:
        z "(Time to get back, I suppose...)"
        scene black with fade
        pause(1)
        "On the way back to the mansion."
        scene v5811 with dissolve
        z "(Hm? Is that...)"
    scene v5812 with Fade(0.5,0.5,0.5)
    z "(Isn't that Jamie? What's he doing with Johann Schwartz? What are those two up to...)"
    z "(It might be nothing important... But I'm investigating here. I have to be sure.)"
    jamie "And the stupid bridge collapsed. My carriage was barely loaded with the... good stuff, but the shitty bridge collapsed as soon as we passed it. Can you believe it?!"
    z "(Wait, what?! This asshole is responsible for that collapsed bridge on our way here?! Is this fucker the reason why we had to go through the town of the faceless fuck?!)"
    z "..."
    scene v5813 with dissolve
    johann "Well. You'll be pleased to know that the craftsmanship is of the highest quality here in my city."
    z "(Calm down, [mc_name]... I still need to quietly investigate what they're doing. I can't let my anger get the better of me.)"
    johann "Now, I'm particularly interested to see the last few pieces you brought with you."
    scene v5814 with dissolve
    jamie "Yes, of course. After you."
    scene v5815 with dissolve
    z "(Pieces? Good stuff? What's that about?)"
    scene v5816 with dissolve
    z "(Something is off about this. I should at least find out where they're going.)"
    scene v5817 with dissolve
    pause(1)
    stop background_s fadeout 1.0
    stop background_s2 fadeout 1.0
    stop music fadeout 1.0
    stop sound fadeout 1.0
    scene v5818 with Fade(0.5,0.5,0.5)
    pause(0.7)
    z "(This inn is really such a fancy place, huh...)"
    scene v5819 with dissolve
    z "(I shouldn't lose them.)"
    scene v5820 with dissolve
    z "(Shit. Looks like a bouncer or something...)"
    Character("Woman") "Excuse me, sir."
    scene v5821 with dissolve
    z "Hm?"
    scene v5823 with dissolve
    z "Yes?"
    scene v5822 with dissolve
    Character("Woman") "I'm afraid this section is only available for platinum-level guests and above."
    scene v5823 with dissolve
    z "(Platinum level? I don't really know what that is...)"
    z "Oh..."
    define claimed = 0
    menu:
        "Claim to be a platinum-level guest. [ModGreen](More sense)":
            $ claimed = 1
            z "And what makes you think, I'm not a platinum-level guest? (I hope she doesn't ask for some papers or something... But Johann and Jamie didn't show her anything.)"
            scene v5822 with dissolve
            Character("Woman") "Well, then you should know that the dress code doesn't allow such clothes inside, sir."
            scene v5823 with dissolve
            z "Huh?! (What's wrong with my clothes?!)"
            z "(Better keep up the act.)"
            z "Hmph. I'll be back."
            scene v5822 with dissolve
            Character("Woman") "You're very welcome to do so, sir. Just remember to keep to the dress code."
            scene v5823 with dissolve
        "Ask her how you can become a platinum-level guest.":
            z "And how would I become a platinum-level guest?"
            scene v5824 with dissolve
            Character("Woman") "Well, you'll have to see the inn's management about that, sir."
            Character("Woman") "For an exchange of an ample sum of money, you will receive access to many sections in the inn and be familiarised with the dress code required for each."
            scene v5823 with dissolve
            z "I see..."
    z "(Seems the whole access thing has to do with some dress code. I suppose I could solve this issue by borrowing some clothes from the mansion...)"
    z "(Not much I can do now, though. Let's get back to the mansion for tonight.)"
    pause(0.7)
    $ jamie_initial = 1
    scene black with fade
    stop background_s fadeout 1.0
    stop background_s2 fadeout 1.0
    stop music fadeout 1.0
    stop sound fadeout 1.0
    pause(2.5)
    define ended_serena = 0
    #Insert Serena's scene here <-------------------------------------------------------------------------------------------------------------------------------------------------------
    if affair_w_serena == 1:
        scene v51037 with dissolve
        pause(0.5)
        play music "audio/Mansion.mp3" volume 0.25 fadeout 1.0 fadein 1.0 loop
        z "Good evening, Daiana."
        scene v51036 with dissolve
        daiana "Good evening, sir."
        daiana "The mistress would like to see you in her room."
        scene v51037 with dissolve
        z "(Whoa... In her room?!)"
        z "Got it. Thanks, Daiana."
        pause(0.7)
        scene v51038 with Fade(0.5,0.8,0.5)
        pause(0.7)
        scene v51039 with dissolve
        serena "Hm?"
        scene v51040 with dissolve
        serena "Come in, come in."
        scene v51041 with dissolve #Pats the bed next to her.
        serena "Come sit next to me."
        scene v51042 with dissolve
        z "Hm? (What's with this serious look all of the sudden?)"
        pause(0.5)
        play sound "audio/Cloth_rustle.wav"
        scene v51043 with dissolve #sits next to her
        z "..."
        scene v51044 with dissolve
        serena "I know you might be a bit confused..."
        scene v51045 with dissolve
        serena "The truth is, I wanted to apologise for last time..."
        serena "I'm the adult here. So..."
        scene v51046 with dissolve
        pause(0.7)
        scene v51047 with dissolve
        serena "It was a mistake... I'm a married woman... Not mention, old enough to be your mother."
        scene v51048 with dissolve
        z "(Huh?!)"
        scene v51047 with dissolve
        serena "If my husband should find out... My family... My marriage... I can't..."
        scene v51048 with dissolve
        z "(Is she messing with me or is she serious right now? I can't tell...)"
        z "(I mean... What we did... This is obviously not a first for her... Right?)"
        scene v51049 with dissolve #Grabs his hand.
        serena "So... Let's just forget it ever happened. Okay?"
        scene v51050 with dissolve
        z "..."
        menu:
            "[ModGreen]Call her out on her act.":
                label G16:
                    if came_from_gallery == 1:
                        scene black with dissolve
                        "Are you doing a 'mommy' role-play with Serena?"
                        menu:
                            "Yes.":
                                $ calling_serena_mommy = 1
                            "No.":
                                $ calling_serena_mommy = 0
                    $ persistent.g_16_unlock = 1
                scene v51066 with dissolve
                z "Really?"
                play music "audio/sex music.mp3" volume 0.1 fadeout 1.0 fadein 1.0 loop
                scene v51067 with dissolve
                serena "Y-Yes..."
                scene v51068 with dissolve
                z "You didn't seem to care about this last time, though..."
                scene v51069 with dissolve
                serena "W-What?! I told you it was a mistake! I was a little drunk and I-"
                z "(Gods... If this is really an act, she's really good at it...)"
                z "(Let's find out.)"
                scene v51070 with dissolve
                z "You're not drunk now, are you?"
                serena "N-No... You-"
                scene v51071
                play audio "audio/cloth.mp3"
                with vpunch
                serena "!"
                scene v51072 with dissolve
                pause(1)
                scene v51073 with dissolve
                serena "..."
                z "Are you sure?"
                scene v51074 with dissolve
                serena "I-I'm not drunk... So... S-Stop it..."
                play sound "audio/Zip.mp3"
                scene v51075 with dissolve
                z "Oh... But you are drunk."
                scene v51076 with dissolve
                z "Cock-drunk."
                serena "..."
                scene v51077 with dissolve
                serena "... That's n-not... true..."
                scene v51078 with dissolve
                pause(1)
                scene v51079 with dissolve
                pause(1)
                scene v51077 with dissolve
                serena "My husband... I shouldn't... I w-won't..."
                scene v51080 with dissolve
                z "Hm..."
                scene v51077 with dissolve
                pause(0.7)
                scene v51081 with dissolve
                pause(0.7)
                z "Are you sure?"
                serena "!"
                scene v51082 with dissolve
                serena "..."
                scene v51083 with dissolve
                serena "Ah!"
                scene v51084 with dissolve
                serena "..."
                scene v51085 with dissolve
                serena "Hah..."
                scene v51086 with dissolve
                if calling_serena_mommy == 1:
                    z "Your mouth is saying one thing and doing another, mommy."
                else:
                    z "Your mouth is saying one thing and doing another, Mrs.Schwartz."
                serena "I-I..."
                scene v51087 with dissolve
                serena "Ah..."
                scene v51088 with dissolve
                z "Kiss it."
                serena "..."
                play audio "audio/kiss.mp3"
                scene v51089 with dissolve
                serena "Hm..."
                z "See? Wasn't so hard to admit you're a cock-craving slut, was it?"
                serena "Mmm..."
                scene v51090 with dissolve
                z "Here... Take it..."
                scene v51091 with dissolve
                serena "Mmmm..."
                scene v51092 with dissolve
                z "Such a good girl... You almost got the whole tip..."
                serena "Mmmm..."
                if calling_serena_mommy == 1:
                    z "Let me ask you this, mommy."
                    scene v51093 with dissolve #Shoves it in
                    serena "MMMM!"
                    scene v51094 with dissolve
                    serena "Ghk! KHMMM!"
                    scene v51095 with dissolve
                    z "How often do you fantasise about deepthroating your son's dick?"
                    serena "Mmmm..."
                    scene v51096 with dissolve
                    z "Did you use dildos before while thinking about it?"
                    serena "..."
                    scene v51099 with dissolve
                    scene v51100 with dissolve
                    scene v51099 with dissolve
                    scene v51100 with dissolve
                    scene v51099 with dissolve
                    #Shakes her head yes
                    z "Can they reach this deep?"
                    scene v51097 with dissolve
                    scene v51098 with dissolve
                    scene v51097 with dissolve
                    scene v51098 with dissolve
                    scene v51099 with dissolve
                    #Shakes her head no
                else:
                    z "Let me ask you this, Mrs.Schwartz."
                    scene v51093 with dissolve #Shoves it in
                    serena "MMMM!"
                    scene v51094 with dissolve
                    serena "Ghk! KHMMM!"
                    scene v51095 with dissolve
                    z "How often do you deepthroat your husband's dick?"
                    serena "Mmmm..."
                    scene v51096 with dissolve
                    z "Can his dick even reach this deep?"
                    scene v51097 with dissolve
                    scene v51098 with dissolve
                    scene v51097 with dissolve
                    scene v51098 with dissolve
                    scene v51099 with dissolve
                    #Shakes her head no
                z "You know... You haven't even gotten to the base yet."
                serena "Mmm?"
                z "Wanna try?"
                serena "..."
                scene v51099 with dissolve
                scene v51100 with dissolve
                scene v51099 with dissolve
                scene v51100 with dissolve
                scene v51099 with dissolve
                #Shakes her head yes
                z "Well, good luck."
                scene v51101 with dissolve #Deeper
                serena "Ghk! Kahk! Gkhm!"
                scene v51102 with dissolve #Shoves the rest
                serena "Khm! Gkmhkm!"
                scene v51103 with dissolve
                serena "..."
                z "Whoa... You're so good at this..."
                if calling_serena_mommy == 1:
                    z "Okay, mommy. I'm going to start moving now..."
                else:
                    z "Okay, Mrs.Schwartz. I'm going to start moving now..."
                scene v51104 with dissolve
                serena "Mm?!"
                z "What? How else do you expect me to cum?"
                serena "..." #Worried look
                show v5m22 with dissolve #Starts moving
                z "Ahh... This is amazing..."
                serena "Hm..."
                if calling_serena_mommy == 1:
                    z "You look like you like it as much as I do, mommy."
                else:
                    z "You look like you like it as much as I do, Mrs.Schwartz."
                serena "*Gagging. Mhm..."
                if calling_serena_mommy == 1:
                    z "Who knew my mommy was such a slut with a well-practiced throat..."
                else:
                    z "Who knew the jarl's wife was such a slut with a well-practiced throat..."
                if calling_serena_mommy == 1:
                    z "Your throat was made for this, mommy."
                else:
                    z "Your throat was made for this, Mrs.Schwartz."
                    z "Too bad your husband won't reach deep enough to enjoy these parts of you..."
                serena "Hmm..."
                z "Damn... I'm going to cum..."
                menu:
                    "Pour it down her throat.":
                        pause(0.7)
                        scene v51105 with vpunch
                        serena "Khg! Kahgkhak!"
                        z "Yeah... Take it..."
                        scene v51109 with dissolve
                        serena "Ahhh... <3"
                    "Paint her with cum.":
                        pause(0.7)
                        scene v51107 with dissolve
                        serena "Gaaah..."
                        z "Yeah... Take it..."
                        scene v51108 with dissolve
                        serena "Ahhh... <3"
                pause(0.7)
                scene v51110 with Fade(0.5,0.8,0.5)
                serena "Kaaah... You almost... hah... killed me... I need... hah... air, you know..."
                scene v51111 with dissolve
                serena "Gods... hah... That was so..."
                scene v51112 with dissolve
                serena "...intense..."
                scene v51113 with dissolve
                serena "Seems I underestimated you..."
                z "Was? You mean you're not up to the real thing?"
                scene v51114 with dissolve
                serena "W-What?!"
                scene v51115
                play sound "audio/cloth.mp3"
                with vpunch
                serena "..."
                serena "(This kid... He still has the energy...)"
                scene v51116 with dissolve
                if calling_serena_mommy == 1:
                    z "Do you want it, mommy?"
                else:
                    z "Do you want it, Mrs.Schwartz?"
                scene v51117 with dissolve
                serena "Oh gods... I don't know if I can take it..."
                show v5m23 with dissolve
                if calling_serena_mommy == 1:
                    z "Sure you can. Your slutty body was made for this, mommy."
                else:
                    z "Sure you can. Your slutty body was made for this, Mrs.Schwartz."
                z "Now, let me ask again."
                z "Do you want it?"
                if calling_serena_mommy == 1:
                    z "Your son's big cock?"
                    z "Want your son to fuck you again?"
                else:
                    z "The big cock of a man who isn't your husband?"
                    z "Want to make your husband a cuckold again?"
                scene v51117 with dissolve
                serena "Oh, gods... I want it..."
                hide v5m23
                show v5m23 with dissolve
                z "What do you want? You have to be a bit more specific."
                serena "..."
                if calling_serena_mommy == 1:
                    z "What do you want, mom? You're not getting it unless you speak clearly."
                else:
                    z "What do you want, Mrs.Schwartz? You're not getting it unless you speak clearly."
                serena "..."
                scene v51117 with dissolve
                if calling_serena_mommy == 1:
                    serena "I want my son's big cock inside me!"
                else:
                    serena "I want this big cock to fuck me like my husband could never do!"
                scene v51115 with dissolve
                z "Good girl."
                menu:
                    "Ram it in.":
                        $ dummy += 1
                scene v51118 with vpunch
                serena "OHHH!"
                show v5m25 with dissolve
                serena "GAHH! AHH! OHH! You're- AHH! breaking me!"
                z "I'm sure you're not that easy to break."
                z "So? Do you still think it was a mistake? Do you need a bit more pumping to convince you?"
                serena "Ahh... Yeah... Pump me more... I need... Ah... convincing..."
                show v5m26 with dissolve
                serena "Ahh... Ohh..."
                serena "My pussy... Ahh... You're reshaping it... with your cock!"
                if calling_serena_mommy == 1:
                    serena "Oh... What kind of... ah... mother has her pussy... shaped to her son's... ahhh... cock..."
                    serena "Ahh... Such a naughty... boy... doing this... Ahh... to your mother..."
                    z "(Gods... She's really into the role, huh...)"
                else:
                    serena "Oh... What kind of... ah... wife has her pussy... shaped to a man's... ahhh... cock... who isn't... her husband..."
                    serena "Ahh... Such a naughty... boy... Stealing another man's... ahhh... wife..."
                    serena "Making her... ahhhh... fall in love... with your... ohhh... cock..."
                    z "(Gods...)"
                z "I'm about to..."
                serena "Uhh... Do it, boy... Fill my pussy up..."
                serena "Ohhh... Ahhh... Ohh..."
                menu:
                    "Fill her up.":
                        scene v51119 with vpunch
                        serena "OHHH!"
                        scene v51122 with dissolve
                        pause(1.2)
                    "Pull out.":
                        scene v51120 with dissolve
                        serena "Aww..."
                        scene v51121 with dissolve
                        pause(1.2)
                stop background_s fadeout 1.0
                stop background_s2 fadeout 1.0
                stop music fadeout 1.0
                stop sound fadeout 1.0
                play background_s2 "audio/Ambient_ninja_village_night.mp3" volume 0.4 fadeout 1.0 fadein 1.0 loop
                scene v51123 with Fade(0.5,1.5,0.5)
                serena "..."
                scene v51124 with dissolve
                serena "You should go back to your room, honey. You can't sleep here... Johann will come back soon."
                scene v51125 with dissolve
                z "Yeah..."
                play sound "audio/Cloth_rustle.wav"
                scene v51126 with dissolve
                pause(0.8)
                scene v51127 with dissolve
                pause(0.5)
                z "Good night..."
                scene v51128 with dissolve
                serena "Good night, darling."
                scene v51129 with dissolve
                pause(1.2)
                $ renpy.end_replay()
                if came_from_gallery == 1:
                    $ came_from_gallery = 0
                    jump gallery_2
            "Tell her you understand.":
                if came_from_gallery == 0:
                    $ ended_serena = 1
                scene v51051 with dissolve
                z "Yeah... No. I understand."
                scene v51052 with dissolve
                serena "Oh... Okay. It's behind us, then?"
                scene v51053 with dissolve
                z "Yeah."
                play audio "audio/kiss.mp3"
                scene v51054 with dissolve
                serena "Aww... I knew you were a good boy. *Kisses you on the cheek.*"
                scene v51055 with dissolve
                serena "..."
                scene v51056 with dissolve
                pause(0.6)
                scene v51057
                play audio "audio/kiss.mp3"
                with vpunch
                z "Mmm!"
                scene v51058 with dissolve
                serena "Hahh..."
                scene v51059 with dissolve
                serena "This is our goodbye-kiss. Okay?"
                scene v51060 with dissolve
                serena "Now back to your room, honey. Get some sleep."
                scene v51061 with dissolve
                z "Y-Yeah..."
                play sound "audio/Cloth_rustle.wav"
                scene v51062 with dissolve # Gets up
                pause(0.7)
                scene v51063 with dissolve
                z "Good night..."
                scene v51064 with dissolve
                serena "Good night."
                scene v51065 with dissolve
                pause(0.7)
    scene black with fade
    stop background_s fadeout 1.0
    stop background_s2 fadeout 1.0
    stop music fadeout 1.0
    stop sound fadeout 1.0
    pause(2.5)
    #In front of his room
    play background_s2 "audio/Ambient_ninja_village_night.mp3" volume 0.4 fadeout 1.0 fadein 1.0 loop
    scene v5926 with dissolve
    pause(0.7)
    scene v5927 with dissolve
    a "..."
    scene v5928 with dissolve
    pause(0.7)
    play sound "audio/creaky door.mp3"
    scene v5930 with dissolve
    a "..."
    scene v5929 with dissolve
    a "(There he is... Looks like he's fine.)"
    scene v5932 with dissolve
    a "(Cute...)" #Smiling
    scene v5933 with dissolve
    pause(1.5)
    play audio "audio/creak.mp3"
    scene v5934 with dissolve
    pause(2.5)
    scene v5935 with dissolve
    a "You'll be a great fighter one day, [mc_name]. And with the right guidance, a great man. Like my brother."
    scene v5936 with dissolve
    pause(1.5)
    scene v5935 with dissolve
    a "I'll see to it that you do. I promise."
    scene v5936 with dissolve
    pause(2.5)
    play audio "audio/creak.mp3"
    scene v5937 with dissolve
    pause(1.5)
    scene v5938 with dissolve
    pause(1.5)
    stop background_s fadeout 1.0
    stop background_s2 fadeout 1.0
    stop music fadeout 1.0
    stop sound fadeout 1.0
    scene black with fade
    "The ball is tomorrow..."
    pause(2.5)
    play background_s2 "audio/Ambient_ninja_village.mp3" volume 0.5 fadeout 1.0 fadein 1.0 loop
    scene v5825 with dissolve
    pause(1.2)
    scene v5827 with dissolve
    z "(Anabelle is on her own again...)"
    z "(She's meditating... Wow... Her Aura is really impressive.)"
    scene v5828 with dissolve
    z "(I almost don't want to interrupt.)"
    scene v5829 with dissolve
    a "Come closer, [mc_name]. Stand in front of me, so I can see you."
    scene v5830 with dissolve
    z "(Oh. She noticed me.)"
    show v5m18 with dissolve
    z "(I can feel the warmth of her aura from here... It sort of feels like sunlight. I can see why she's not wearing her jacket.)"
    z "(If I recall, some claimed that Venus's magical ability is only second to Anabelle's. But I can tell there's quite the gap...)"
    z "(I wonder who is actually stronger, Anabelle or Seira...)"
    z "Hi, Anabelle."
    scene v5831 with dissolve
    a "Hi."
    scene v5832 with dissolve
    z "Have the others already left like yesterday?"
    scene v5831 with dissolve
    a "No. I told them to get some more rest today. There's only one day left to the ball."
    scene v5832 with dissolve
    z "Oh... Should I not go investigate today, then?"
    scene v5833 with dissolve
    a "Hm? You sound disappointed. Did you find something out with Irena?"
    scene v5832 with dissolve
    z "Not really. I did see the jarl doing some suspicious business with someone at a nearby inn, though."
    scene v5834 with dissolve
    a "The jarl? In what way was the business suspicious?"
    scene v5835 with dissolve
    z "Well, he was talking with another guy about some merchandise they brought here... The guy, Jamie, is betrothed to Gabbie's sister. He said the bridge on the way here collapsed after one of his carriages passed over it."
    #Stops meditating
    play audio "audio/Cloth_rustle.wav"
    scene v5836 with dissolve
    a "Hold up, hold up. Let me sit down first."
    scene v5837 with dissolve
    a "That's a lot of info. Gabbie meaning our new alchemist girl?"
    scene v5838 with dissolve
    z "Yep."
    scene v5837 with dissolve
    a "And this Jamie said something about bringing suspicious stuff into town and causing the bridge to collapse on his way here?"
    scene v5838 with dissolve
    z "Exactly."
    scene v5839 with dissolve
    a "But why is the stuff he brought suspicious?"
    scene v5840 with dissolve
    z "He referred to it as 'the good stuff'. And the jarl called it something similar. They didn't seem to want to reveal what it was."
    scene v5841 with dissolve
    a "Hm..."
    scene v5840 with dissolve
    z "I followed them a bit. They went into a room in the expensive inn. Or rather, a section, which I wasn't allowed to go into."
    z "But I think I could borrow some nice clothes from here and try again. The lady at the counter there mentioned that I needed to stick to a dress code to get in."
    a "..."
    scene v5842 with dissolve
    a "Well... We're probably getting off the trail to the butcher here..."
    scene v5843 with dissolve
    a "That said. If there's suspicious business in the city that's harming others, it's very much our job to look into it. Besides, it's not like we have any better leads at this point."
    scene v5844 with dissolve
    a "And you say it might have had something to do with the collapse of the bridge."
    scene v5845 with dissolve
    a "..."
    scene v5846 with dissolve
    a "Okay, [mc_name]. But I want you to take Candy with you."
    scene v5847 with dissolve
    z "(Damn... Her body is so... perfect... I should try not to stare like a pervert here...)"
    z "Candy?"
    scene v5848 with dissolve
    a "Yeah. I promised Torr I'd investigate something with her today, since we didn't get to do anything together last time. And I want Candy to see some action."
    scene v5849 with dissolve
    a "I don't want her to see too much action, though. So if you happen to find something dangerous, you should come back here and regroup. We'll discuss next steps together."
    scene v5850 with dissolve
    z "Got it."
    scene v5851 with dissolve
    a "Good. Go wake her up. It's about time for her to wake up, anyway."
    scene v5852 with dissolve
    pause(0.7)

    scene v5853 with Fade(0.5,0.5,0.5)
    pause(0.5)
    z "(I think that's their room at the end of the hall.)"
    scene v5854 with dissolve
    pause(0.5)
    play sound "audio/creaky door.mp3"
    scene v5855 with dissolve
    pause(0.5)
    play audio "audio/Door close.mp3"
    scene v5856 with dissolve
    tr "..."
    scene v5857 with dissolve
    tr "Oh. Morning, [mc_name]."
    scene v5858 with dissolve
    z "Hi, Torr."
    z "Heard you're with Anabelle today."
    scene v5859 with dissolve
    tr "Yep. Gotta learn from the best if I want to make it to black belt quickly, you know?" #cocky looking away
    scene v5860 with dissolve
    z "..."
    scene v5861 with dissolve
    tr "..." #looks at z
    scene v5862 with dissolve
    tr "What?"
    scene v5863 with dissolve
    z "Nothing."
    tr "..." #Looks at z with half-closed eyes
    scene v5864 with dissolve
    tr "Anyway, why are you up here?"
    scene v5865 with dissolve
    z "Came to wake Candy. She's going with me today, apparently. Is she awake already?"
    tr "..."
    scene v5866 with dissolve
    tr "Pffft..."
    scene v5867 with dissolve
    tr "Pffffffffttttttttttttttt..." #Holding her Laughter
    z "What?"
    scene v5868 with dissolve
    tr "You want to wake up Candy? Sure, sure. Good luck with that."
    scene v5869 with dissolve
    z "?"
    scene v5870 with dissolve
    tr "Well... I'm off to see Anabelle. Bye."
    scene v5871 with dissolve
    z "Yeah..."
    scene v5872 with dissolve
    "*Torr laughs going down the stairs."
    z "(What was that about?)"
    play sound "audio/creaky door.mp3"
    scene v5873 with dissolve
    pause(0.5)
    z "(There she is.)"
    scene v5874 with dissolve
    z "(Cute. Even though her sleeping posture is such a mess...)"
    z "(Aaaand, it was probably not the best idea that I of all people should wake her up. She's barely wearing anything...)"
    scene v5875 with dissolve
    z "Hey, Candy. It's time to wake up."
    cndy "..."
    z "(Huh? No reaction? Maybe I should raise my voice a bit?)"
    z "CAAAANDYYYY!"
    scene v5876 with dissolve
    cndy "Mm..."
    scene v5877 with dissolve
    cndy "Zzz..."
    z "('Mm?' That's it?! I was basically shouting just now!)"
    scene v5878 with dissolve
    z "Come on, Candy!"
    scene v5879
    play sound "audio/Slap2.mp3"
    with vpunch
    cndy "Hmm!"
    scene v5880 with dissolve
    z "Whoa! Aggressive, aren't you?"
    cndy "..."
    scene v5881 with dissolve
    cndy "Gah... Zzzzzz..."
    z "..."
    z "(Seems the conventional method won't work... I have to do something more... creative.)"
    define cndy_wake1 = 0
    define lvpunch = Move((0, 10), (0, -10), .10, bounce=True, repeat=True, delay=1.5)
    menu:
        "Cover her mouth.":
            scene v5884 with dissolve
            z "Come on, sleepyhead!"
            pause(1)
            scene v5885
            play sound "audio/creak.mp3"
            with vpunch
            cndy "MHHHHH!"
        "Close her nose.":
            scene v5882 with dissolve
            z "Come on, sleepyhead!"
            pause(1)
            scene v5883
            play sound "audio/creak.mp3"
            with vpunch
            cndy "GAHHH!"
        "Shout REALLY loud.":
            $ cndy_wake1 = 1
            scene v5886 with dissolve
            z "Psst... Hey Candy..."
            scene v5887
            play sound "audio/creak.mp3"
            with vpunch
            z "WAKE UP!!!!!!!"
            cndy "AHHHHH!" with vpunch
    scene v5888 with dissolve
    cndy "..."
    z "Morning, Candy."
    cndy "..."
    scene v5889 with dissolve
    if cndy_wake1 == 0:
        cndy "Ahh! What's going on?! S-Someone tried to strangle me while I was sleeping!"
    else:
        cndy "Ahh! What's going on?! I heard shouting."
    scene v5890 with dissolve
    z "Yeah... That was me."
    cndy "..."
    scene v5891 with dissolve
    cndy "H-HUH?!"
    scene v5892 with dissolve
    if cndy_wake1 == 0:
        z "I d-didn't strangle you or anything! I was just trying to wake you up!"
    else:
        z "I had to shout! You wouldn't wake up no matter what I did!"
    cndy "..."
    scene v5893 with dissolve
    cndy "W-Well... I suppose I can be a bit of a heavy sleeper... Torr does similar stuff sometimes to wake me..."
    scene v5894 with dissolve
    z "(A bit of a heavy sleeper...)"
    scene v5895 with dissolve
    cndy "But I'm not late or anything! Anabelle said I can sleep in today."
    scene v5896 with dissolve
    z "Yeah, I know. But something came up and Anabelle told me to take you with me."
    scene v5897 with dissolve
    cndy "Really? You mean you found something?"
    scene v5898 with dissolve
    z "Well, it's just a random lead at this point."
    scene v5897 with dissolve
    cndy "Cool. Finally some real work."
    cndy "Tell me more!"
    scene v5898 with dissolve
    z "Okay. First, you'll have to borrow some clothes from Karolina again, we're..."
    stop background_s2 fadeout 3.0
    play background_s "audio/Ambient_ninja_village_night.mp3" volume 0.4 fadeout 1.0 fadein 5.0 loop
    scene black with Fade(2.5,2.5,0.7)
    scene v5899 with dissolve
    pause(0.7)
    scene v5900 with dissolve
    pause(0.7)
    scene v5901 with dissolve
    z "..."
    z "...."
    z "....."
    scene v5902 with dissolve
    z "(She's late...)" #annoyed
    scene v5903 with dissolve
    z "..."
    scene v5904
    play sound "audio/Door slam.mp3"
    with vpunch
    krlna "Yeah, yeah. Hold on, I'm going to tell him!" #Opens the door while looking inside
    scene v5905 with dissolve
    krlna "She just needs a few more seconds okay?" #Turns to z
    scene v5906 with dissolve
    z "..."
    scene v5907 with dissolve
    z "Fine..."
    scene v5908 with dissolve
    cndy "*Shouting. WHAT DID HE SAY?!"
    scene v5909 with dissolve
    krlna "He said it's fine!" #shouting while looking inside
    scene v5910 with dissolve
    pause(0.7)
    scene v5911
    play sound "audio/Door slam.mp3"
    with vpunch
    krlna "*Slams door."
    scene v5912 with dissolve
    z "(Maybe I shouldn't have said that...)"
    pause(0.7)
    scene black with fade
    pause(0.7)
    "Twenty minutes later..."
    pause(0.7)
    scene v5913 with dissolve
    pause(0.7)
    play audio "audio/creaky door.mp3"
    scene v5914 with dissolve
    "*Door opens."
    scene v5915 with dissolve
    cndy "..."
    scene v5916 with dissolve
    cndy "S-Sorry for making you w-wait..."
    scene v5917 with dissolve
    z "(Whoa... She looks really nice...)"
    menu:
        "[ModGreen]Tell her she looks pretty. (Candy Love +4)":
            z "(Candy is a really pretty girl, isn't she...)"
            z "Wow, Candy! You look really pretty."
            scene v5924 with dissolve
            cndy "..." #Blushes
            scene v5925 with dissolve
            cndy "Th-Thanks..."
            scene v5923 with dissolve
            $ cndy_aff += 4
            show screen button_aff with dissolve
            play sound "audio/stats.wav"
            hide screen button_aff with dissolve
            scene v5922 with dissolve
            cndy "You look n-nice too..."
            scene v5923 with dissolve
            z "Thanks..."
            z "We should go. We're already a bit late."
            scene v5922 with dissolve
            cndy "Y-Yeah... Sorry about that. Didn't know rich people took this long getting ready."
            scene v5923 with dissolve
        "Tell her the rich girl look suits her. [ModGreen](Candy Love +2)":
            z "Wow, Candy! Being rich agrees with you. I bet these clothes suit you more than Karolina."
            scene v5921 with dissolve
            cndy "Heheh. You think so?" #Smiles
            cndy "Th-Thanks..."
            scene v5923 with dissolve
            $ cndy_aff += 2
            show screen button_aff with dissolve
            play sound "audio/stats.wav"
            hide screen button_aff with dissolve
            scene v5922 with dissolve
            cndy "You look n-nice too..."
            scene v5923 with dissolve
            z "Thanks..."
            z "We should go. We're already a bit late."
            scene v5922 with dissolve
            cndy "Y-Yeah... Sorry about that. Didn't know rich people took this long getting ready."
            scene v5923 with dissolve
        "Focus on the mission.":
            z "Great! Your clothes are perfect. They'll let us pass no problem."
            scene v5918 with dissolve
            cndy "Y-Yeah..." #Disappointed
            scene v5920 with dissolve
            z "We should go. We're already a bit late."
            scene v5919 with dissolve
            cndy "Y-Yeah... Sorry about that. Didn't know rich people took this long getting ready."
            scene v5920 with dissolve
    pause(0.7)
    scene black with fade
    stop background_s fadeout 1.0
    stop background_s2 fadeout 1.0
    stop music fadeout 1.0
    stop sound fadeout 1.0
    pause(2.5)
    play music "audio/Mansion.mp3" volume 0.25 fadeout 1.0 fadein 1.0 loop
    scene v5939 with dissolve
    z "Good evening, miss."
    if claimed == 1:
        scene v5941 with dissolve
        z "I apologise for yesterday. Apparently, management forgot to mention the bit about the dress code."
        scene v5940 with dissolve
        Character("Woman") "Oh! No, please. Nothing to apologise for... I'd offer you some company on the house as compensation for the misunderstanding yesterday, but you seem to have that already covered."
    else:
        scene v5941 with dissolve
        z "Management told me about the dress code, but they weren't very specific... I trust this is fine?"
        scene v5940 with dissolve
        Character("Woman") "Yes. No problem, sir. You already seem to have company..."
    scene v5944 with dissolve
    Character("Woman") "Just a room then, I assume?"
    scene v5942 with dissolve
    z "(Huh? Just a room? Company? What does that mean? Let's play along...)"
    scene v5943 with dissolve
    z "Yeah. Just a room, please."
    scene v5946 with dissolve
    Character("Woman") "Name, please?"
    scene v5949 with dissolve
    z "(Shit... Let's make up a name, quick.)"
    define viktor = 0
    if vns_trst >= 2:
        $ viktor = 1
        scene v5943 with dissolve
        z "Viktor. With a K."
    else:
        z "R-Ronald. The name's Ronald..."
        scene v5947 with dissolve
        Character("Woman") "Hm..." #looks at z in disbeliefe
    scene v5948 with dissolve
    if viktor == 1:
        Character("Woman") "Very good. Room four is now booked in your name, mister Viktor."
    else:
        Character("Woman") "Very good. Room four is now booked in your name, mister Ronald."
    scene v5950 with dissolve
    z "Thanks."
    scene v5951 with dissolve
    z "..."
    scene v5952 with dissolve
    z "Hm? (Erwin? What's he doing here?)"
    scene v5953 with dissolve
    z "Hey, Candy."
    cndy "Mmm?"
    z "Don't look directly at him, but Erwin is sitting on the couch over there."
    scene v5954 with dissolve
    cndy "Erwin?"
    scene v5955 with dissolve
    z "The artist from the square. Remember him?"
    scene v5956 with dissolve
    cndy "Oh, right..."
    cndy "Is this something we should be worried about?"
    scene v5957 with dissolve
    z "No. I don't think he spotted us. Let's just keep it that way, and we'll be fine."
    scene v5956 with dissolve
    cndy "Okay..."
    scene v5957 with dissolve
    pause(0.7)
    scene black with fade
    pause(1.5)
    scene v5958 with Dissolve(2.5)
    pause(1)
    scene v5959 with Dissolve(2.5)
    pause(1)
    scene v5960 with Dissolve(2.5)
    pause(1)
    scene v5961 with Dissolve(2.5)
    pause(1)
    scene v5962 with Dissolve(2.5)
    z "..."
    cndy "..."
    z "(What?! Is this...)"
    scene v5963 with vpunch
    z "A brothel?! Is this what they were hiding?!"
    scene v5964 with dissolve
    cndy "Uhm... W-Where's our room?"
    play sound "audio/Cloth_rustle.wav"
    scene v5965 with dissolve
    z "Huh? Oh. It's supposed to be number four down the hall, but-"
    scene v5966
    play audio "audio/whoosh.mp3"
    play sound "audio/chains.mp3"
    with vpunch
    stop sound
    cndy "I'll head over there first, then!" #Snaches the key and runs
    z "Huh?"
    scene v5967 with dissolve
    z "Wait!"
    scene v5968 with dissolve
    z "(We only needed to get in to see what this place was. We don't need the room...)"
    scene v5969 with Fade(0.5,1,0.5)
    pause(1)
    scene v5970 with dissolve
    pause(0.7)
    scene v5971 with dissolve
    pause(0.7)
    play sound "audio/pick up 2.mp3"
    scene v5972 with dissolve
    cndy "(Gods! Why did I act all embarrassed like that?! I was supposed to be helping [mc_name] investigate, not run away like a scared little girl!)"
    play sound "audio/sip.mp3"
    scene v5973 with dissolve
    pause(0.7)
    scene v5974 with dissolve
    cndy "Ugh... (That tastes weird...)"
    scene v5975 with dissolve
    cndy "(Damn... I'm so unreliable, aren't I?)"
    scene v5976 with dissolve
    pause(0.7)
    play sound "audio/sip.mp3"
    scene v5973 with dissolve
    pause(0.7)
    scene v5977 with dissolve
    cndy "(Eww... What the hell is even this? It's not water or wine...)"
    scene v5978 with dissolve
    cndy "(Why can't I be like [mc_name]? Anabelle really seems to respect him...)"
    play sound "audio/sip.mp3"
    scene v5979 with dissolve
    pause(0.7)
    scene v5980 with dissolve
    cndy "Hmm..."
    scene v5981 with dissolve
    cndy "(I mean... who doesn't? He already has more points than I do. Even though he joined up like a week ago.)"
    play sound "audio/sip.mp3"
    scene v5979 with dissolve
    pause(0.7)
    scene v5980 with dissolve
    cndy "(Of course he's going to advance faster than me! He's a strong and capable man... He even tied with Yumi and beat Tamara already.)"
    play sound "audio/sip.mp3"
    scene v5982 with dissolve
    pause(0.7)
    scene v5983 with dissolve
    cndy "Bah... (Damn... This stuff is strong... Why did I drink the whole thing like an idiot?!)"
    play sound "audio/creaky door.mp3"
    scene v5984 with dissolve
    "*Door opens."
    z "Candy?"
    scene v5985 with dissolve
    cndy "Yeah... I'm in here."
    scene v5986 with dissolve
    z "..."
    z "Are you alright? Your face looks a bit... reddish..."
    scene v5987 with dissolve
    cndy "Yeah... I might have drunk something wrong..."
    scene v5988 with dissolve
    z "Oh? Well, we got what we wanted. It was just a brothel. Nothing to do with the butcher. Want to wash your face? Refreshen up a little before we leave?"
    cndy "..."
    scene v5987 with dissolve
    cndy "Nah... I'm good."
    scene v5988 with dissolve
    z "Well. I'm going to the bathroom, then."
    scene v5989 with dissolve
    cndy "Oh..."
    play sound "audio/Door close.mp3"
    scene v5990 with dissolve
    z "*Goes to the bathroom."
    scene v5991 with dissolve
    cndy "{size=-10}No... Don't leave...{/size}"
    scene v5992 with dissolve
    pause(0.7)
    scene v5993 with dissolve
    cndy "(Gods... I'm so horny... What the hell did I drink?!)"
    pause(0.7)
    scene v5994 with Fade(0.5,1,0.5)
    pause(0.7)
    z "Hm... (Is this the bathroom? Very tasteful... This place really is for rich people, huh?)"
    scene v5995 with dissolve
    z "Hm?"
    z "(Is that... what I think it is?)"
    scene v5996 with dissolve
    z "..."
    z "(Probably... I'm in a brothel, after all...)"
    z "(I guess Candy is on the other side...)"
    z "...."
    z "....."
    pause(1.5)
    define slideright = CropMove(0.35, "slideright")
    define slideleft = CropMove(0.35, "slideleft")
    show screen button_v5_put_ur_pp with Dissolve(1.3)
    call screen button_v5_dont_put_ur_pp with Dissolve(1.3)
    label bad_idea:
        hide screen button_v5_dont_put_ur_pp
        hide screen button_v5_put_ur_pp
        z "(Nah... That's too crazy. She knows I'm right behind the wall...)"
        z "(Let's just head back... This was obviously not what we're looking for...)"
        jump after_gloryhole
    label put_ur:
        hide screen button_v5_dont_put_ur_pp
        hide screen button_v5_put_ur_pp
        pause(0.7)
        z "..."
        pause(0.7)
        scene v5997 with Fade(0.5,1,0.5)
        pause(0.7)
        cndy "(I want to masturbate... But [mc_name] could come back any second...)"
        label G17:
            $ persistent.g_17_unlock = 1
        scene v5998 with dissolve
        cndy "..."
        scene v5999 with dissolve
        cndy "!"
        scene v51000 with dissolve
        pause(1)
        scene v51001 with dissolve
        pause(1)
        scene v51002 with dissolve
        pause(1)
        scene v51003
        stop background_s fadeout 1.0
        stop background_s2 fadeout 1.0
        play sound "audio/Falling2 (loud).mp3"
        stop music fadeout 1.0
        with vpunch
        pause(0.7)
        cndy "(Whoa... It's exactly like that time in his room... So... menacing...)"
        cndy "(What does he think he's doing shoving it in the hole?)"
        cndy "(Eh... I'm too horny to think straight right now...)"
        play audio "audio/whoosh.mp3"
        scene v51025 with slideright
        z "(This was a dumb idea. I should probably pull it out before she notices it...)"
        play audio "audio/whoosh.mp3"
        scene v51003 with slideleft
        pause(0.7)
        scene v51004 with dissolve
        cndy "Ahh... (Have fun with this dick now, think later...)"
        play audio "audio/whoosh.mp3"
        scene v51026 with slideright
        z "(Holy shit! She's actually touching it!)"
    play audio "audio/whoosh.mp3"
    scene v51004 with slideleft
    play music "audio/sex music.mp3" volume 0.3 fadeout 1.0 fadein 1.0 loop
    pause(0.7)
    cndy "(It's drawing me towards it... I feel helpless against it, I can't refuse... Gods, why do I like this feeling so much?! Is this normal?)"
    scene v51005 with dissolve
    pause(0.25)
    scene v51006 with dissolve
    pause(0.25)
    play audio "audio/kiss.mp3"
    scene v51007 with dissolve
    pause(0.25)
    cndy "(The smell... It's making my head spin...)"
    scene v51006 with dissolve
    pause(0.25)
    scene v51005 with dissolve
    pause(0.25)
    cndy "(I can't describe it... But it's sooooo good... I think...)"
    scene v51006 with dissolve
    pause(0.25)
    play audio "audio/kiss.mp3"
    scene v51007 with dissolve
    pause(0.25)
    cndy "(It weirdly tastes good too...)"
    scene v51006 with dissolve
    pause(0.25)
    scene v51005 with dissolve
    pause(0.25)
    cndy "(Right?)"
    scene v51006 with dissolve
    pause(0.25)
    play audio "audio/kiss.mp3"
    scene v51007 with dissolve
    pause(0.25)
    cndy "(Or is it my horniness talking?)"
    play audio "audio/whoosh.mp3"
    scene v51027 with slideright
    z "(Fuck me! She's licking and kissing it... This girl is wild...)"
    play audio "audio/whoosh.mp3"
    scene v51004 with slideleft
    cndy "(I've lost track of how many times I kissed it already...)"
    scene v51005 with dissolve
    pause(0.25)
    scene v51006 with dissolve
    pause(0.25)
    play audio "audio/kiss.mp3"
    scene v51007 with dissolve
    pause(0.25)
    cndy "(I want more, I...)"
    scene v51008 with dissolve
    cndy "(I need more...)"
    play audio "audio/whoosh.mp3"
    scene v51026 with slideright
    z "Ahh... (She's...)"
    play audio "audio/whoosh.mp3"
    scene v51008 with slideleft
    cndy "(I want it deeper in my mouth... Is this normal? Wanting such a thing in my mouth?)"
    scene v51009 with dissolve
    cndy "(Eh... Who cares?)"
    cndy "Hmm... (It's too big... It won't fit...)"
    scene v51010 with dissolve
    cndy "*Gagging. Khk... Ghak..."
    cndy "(Shit! I can't stop... I can't control myself...)"
    scene v51011 with dissolve
    cndy "Kh... Gah... (I can't... breathe...)"
    cndy "Ghk! (I can't go... deeper... It's hitting the back of my throat...)"
    scene v51012 with dissolve
    cndy "(Need air... But my body... won't... let... me...)"
    cndy "Ghk! Khk! (... I'm...)"
    play audio "audio/whoosh.mp3"
    scene v51026 with slideright
    z "Hahh... (Holy fuck! She's deepthroating me!)"
    play audio "audio/whoosh.mp3"
    scene v51012 with slideleft
    pause(0.8)
    scene v51011 with dissolve
    pause(0.25)
    scene v51010 with dissolve
    pause(0.5)
    scene v51013 with dissolve
    cndy "Gah..."
    cndy "Hahh... (Fuck... I almost passed out while sucking [mc_name]'s cock... That was so scary...)"
    scene v51014 with dissolve
    cndy "..."
    pause(0.5)
    play audio "audio/kiss.mp3"
    scene v51015 with dissolve
    cndy "(That's it. I lost it.)"
    cndy "(My body is moving on it's own...)"
    scene v51016 with dissolve
    cndy "(And my mind is giving up too...)"
    scene v51017 with dissolve
    cndy "Ghk! (I have to suck this cock...)"
    scene v51018 with dissolve
    cndy "Mmmm... (So good...)"
    show v5m19 with dissolve
    cndy "Mmmm... (Cock... tastes... so... good...)"
    cndy "Hmmm... (Can't... stop...)"
    z "Fuck yeah... Keep going, Candy..."
    cndy "Ghk! Kh... (My brain... needs... air...)"
    cndy "Khm... (But it... also... wants... cock...)"
    show v5m20 with dissolve
    cndy "Hmm... (It's... hopeless... I can't... stop...)"
    cndy "Khm... (My throat... must've been... reshaped... specifically for... this cock... by now...)"
    cndy "Ghk! Kh... (It's so.... addictive... I hope I can get back... to normal... after this...)"
    z "Hah... (I can't believe she's doing this... She's pretty good at this...)"
    cndy "(I can't... take it anymore... I have to... touch... myself...)"
    show v5m21 with dissolve
    cndy "Hmmmm... (I feel like... I'm drunk...)"
    cndy "Khm... (Choking... on his dick... feels... so... good...)"
    cndy "Mmmmm... (Do all dicks... taste so... delicious... Or is it... because he's... an incubus...)"
    z "Hah... Fuck... (I'm going to cum...)"
    cndy "Mmm... (I've never... felt so... good... in my life...)"
    cndy "(I'm... cumming...)"
    cndy "(I'm-)"
    call screen cum with dissolve
    scene v51019 with vpunch
    cndy "MMM!!!"
    play audio "audio/magic 7.mp3"
    stop music fadeout 3.0
    scene v51020 with dissolve
    cndy "Khkgkhk! (Cumming...)"
    scene v51021 with dissolve
    cndy "Gah... Hah... Ah... Hah..."
    scene v51022 with dissolve
    cndy "Hehehehe. (Goodbye, mister cock...)"
    if came_from_gallery <> 1:
        $ cndy_lst += 4
        show screen button_lst with dissolve
        play sound "audio/stats.wav"
        hide screen button_lst with dissolve
    pause(0.7)
    $ renpy.end_replay()
    if came_from_gallery == 1:
        $ came_from_gallery = 0
        jump gallery_3
    play audio "audio/whoosh.mp3"
    scene v51023 with slideright
    pause(0.7)
    z "..."
    z "Holy fuck!" with vpunch
    z "(What the fuck did we just do?! What was I thinking?!)"
    z "(Am I supposed to go back and say: Oh, hi, Candy. I'm done with the bathroom. Let's go back...)"
    z "..."
    z "(Actually this is basically the only thing I can say...)"
    z "..."
    z "(I mean... Sure I shoved it in the hole, but she's the one who started sucking it...)"
    z "..."
    z "(Fuck. Let's get this over with.)"
    scene v51029 with Fade(0.5,1,0.5)
    pause(0.7)
    scene v51030 with dissolve
    pause(0.7)
    scene v51031 with dissolve
    z "..."
    z "Errr... I'm d-done with the bathroom..."
    z "A-Are you ready to go? (Fuck... Please play along...)"
    scene v51032 with dissolve
    cndy "Y-Yeah... I just..."
    scene v51033 with dissolve
    cndy "S-Spilled some water! On my face and chest! Yeah! I'm just gonna go to the bathroom real quick to dry myself, okay?"
    scene v51034 with dissolve
    z "S-Sure..."
    play sound "audio/RunningBeats.ogg"
    scene v51035 with dissolve
    cndy "*Runs to the bathroom."
    play sound "audio/Door close.mp3"
    z "..."
    z "(That went well...)"
    z "(Considering.)"
    label after_gloryhole:
    define johann_initial = 0
    $ johann_initial = 1
    pause(0.7)
    scene black with fade
    stop background_s fadeout 1.0
    stop background_s2 fadeout 1.0
    stop music fadeout 1.0
    stop sound fadeout 1.0
    pause(2.5)
    play background_s2 "audio/Ambient_ninja_village_night.mp3" volume 0.4 fadeout 1.0 fadein 1.0 loop
    scene v5257 with dissolve
    z "*Sighs."
    play audio "audio/creak.mp3"
    scene v5258 with dissolve
    z "(The ball is tomorrow... We still haven't figured out anything...)"
    z "(But there have been no killing ever since we arrived. I suppose that's a good thing.)"
    z "(It probably also means that the butcher has noticed us being here... So at least one of us has already run into him at one point.)"
    z "(If things go smoothly tomorrow we might go home without having to deal with him at all.)"
    z "(I should be pleased about this... But it really bugs me for some reason...)"
    z "(I feel like I missed something... I feel like I already met the butcher at one point...)"
    z "(I feel like tomorrow, things will go south...)"
    z "(Is this... the succubus instinct Irena was talking about, or am I imagining things?)"
    z "(Am I...)"
    pause(1.0)
    scene black with fade
    stop background_s fadeout 1.0
    stop background_s2 fadeout 1.0
    stop music fadeout 1.0
    stop sound fadeout 1.0
    pause(1.0)
    jump chapter_6
