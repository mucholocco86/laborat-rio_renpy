label ga_nova3:
    $ renpy.music.set_volume(0.8, channel='music3')
    play music3 novascene fadein 2
    scene fc 20
    bla "You swiftly grab Nova's waist and draw her in, your touch sparking a rapid blush across her cheeks almost immediately." with dis
    scene fc 21
    no "W-What's going on with you now...?" 
    show fc 22
    no "We really have no time to waste..."
    show fc 20 
    mc "No, we don't."
    mc "And that's precisely why I want to dedicate the next few hours entirely to you, Nova."
    show fc 22
    no "We need to get that treasure for El Coyote."
    show fc 20
    mc "We have time."
    mc "Actually... even if we didn't, I don't give a fuck."
    mc "Right now, you're the only thing on my mind, Nova. The only one deserving of attention."
    mc "I'm sorry I haven't shown you enough how much you really mean to me."
    show fc 21
    no "W-What's gotten into you all of a sudden?"
    show fc 20
    mc "Today was our date. Everything else can wait."
    no "Mmh...?"
    mc "I just want to prove to you that you're much more than my clumsy, quirky, ginger friend."
    show fc 22
    no "Ohh... y-you heard that."
    no "Um..."
    no "T-This is a bit embarrassing."
    no "What I meant is that I–"
    play sound bodycollide
    scene fc 23
    bla "You gently tug Nova closer, making your lips meet in a tender kiss." with dis06
    no ". . ."
    no "Mmh?"
    play sound2 clothes3
    scene fc 24
    bla "After a brief moment of hesitation, Nova leans into you and reciprocates the kiss with an energetic passion that lingers for several seconds." with dis12
    no "{bt=3}*Moaning* MMMmmmmmmmh...{/bt}"
    mct "Damn, her soft, fleshy lips feel like pure magic... I could kiss her for hours without getting tired."
    no "MMMMmmmm..."
    play sound3 chair1
    play sound4 couch
    scene fc 25
    no "*Breaking away from the kiss and easing onto the bed* W-Wow."with dis12
    no "W-Where did that come from...?"
    show fc 27
    mc "Just something we should've done a long time ago."
    mc "I mean, can you believe this was actually our first kiss?"
    mc "After {i}everything{/i} we've done together?"
    show fc 26
    no "Was it...? Are you sure?"
    no "N-Never really thought about it, but... now that you mention it..."
    show fc 27
    mc "*Chuckles* Come on, stop! We've moved past that already!"
    mc "You {i}definitely{/i} know that was our first kiss."
    show fc 25
    no "*Giggles* Okay, okay..."
    no "I know it was."
    no "And... it felt... as perfect as I had hoped."
    show fc 27
    mc "I felt the same way."
    show fc 25
    no "I-I'm glad."
    show fc 27
    mc "Tell me then, is there anything else you've been hoping for...?"
    show fc 25
    no "Well... if we actually do have some time to spare before going back to The New World..."
    no "W-We could... cuddle for a bit."
    no "Maybe kiss a little bit more..."
    show fc 27
    mc "Ah, I couldn't have thought of a better idea myself."
    mc "Do you mind if I take off the E-suit?"
    show fc 25
    no "Not at all."
    play sound rubclotheslong
    play sound2 clothes4
    play sound7 clothes3
    scene fc 28
    bla "You take off the top part of the E-suit as Nova gives you a surreptitious onceover, a playful smirk gracing her lips." with Dissolve(1.9)
    mct "Man, I'm already hard as a rock and she’s barely touched me."
    mct "And her sexy look isn't making it any easier..."
    play sound3 clothes3
    scene fc 29 with dis15
    mc "*Lifting her head* Fuck... I want you so bad, Nova." with dis
    mc "I want us to be way more than friends."
    mc "And I think we've danced around it long enough... don't you think?"
    no "Mm-hm..."
    if novadildo and crimesuccess:
        mc "There’s no pretense this time. No external interferences. No crazy chicks with guns, aphrodisiacs, or bizarre duplicating artifacts. No more excuses."
    elif crimesuccess: 
        mc "There’s no pretense this time. No external interferences. No crazy chicks with guns or bizarre duplicating artifacts. No more excuses."
    elif novadildo:
        mc "There’s no pretense this time. No external interferences. No crazy chicks with guns or aphrodisiacs. No more excuses."
    else:
        mc "There’s no pretense this time. No external interferences. No more excuses."
    mc "Now, it's just me... longing for you."
    no "Mmmhh..."
    mc "Don’t you want me too?"
    show fc 30
    no "I do..."
    no "And I don't think I can hold out much longer before going completely insane..."
    show fc 31
    mc "Oh, my poor Nova..."
    mc "I'm gonna give you everything you're craving... and more..."
    show fc 30
    no "Please..."
    no "I want it so bad..."
    no "I want to... take things to the next level with you. I want..."
    no "I want you to be the one."
    show fc 31
    mct "FINALLY she's shedding all that nervousness and speaking her mind clearly..."
    mc "Oh Nova..."
    mc "There's literally nothing else I want more in this world right now."
    no "*Purring* Mmmmmmh..."
    mc "*Teasingly* Wait... we're still talking about cuddling, right?"
    no "*Giggles* Mhhmm."
    show fc 30
    no "Of course..."
    no "I need you to {i}cuddle{/i} me hard..."
    show fc 31
    mc "Oh boy..."
    play sound3 chair1
    play sound4 couch
    show fc 32
    mc "*Sitting next to her* Why don't you take those shorts off too?"with dis12
    mc "Consider it my only request for the night."
    mc "I'm just itching to see that perfect round butt of yours again."
    show fc 33
    no "Uh..."
    no "*Giggles* Well, if you insist..."
    play sound chair2
    play sound2 clothes5
    show fc 34
    no "*Standing up* I haven't been hitting the gym in a while, so... my butt might not be at its peak." with dis12
    mc "I'm sure it's still just as–"
    play sound clothes4
    play sound6 clothes4
    show fc 35 with dis12
    mc "...good." with dis08
    play sound2 clothes3
    play sound7 clothes3
    show fc 36 with dis15
    mc "Jesus Christ, Nova..."with dis
    mc "You only brought up the training bit because you wanted me to swoon over how flawlessly perfect your butt was, didn't you?"
    no "*Giggles* Perhaps."
    mc "Not to mention those panties look sexy as fuck on you..."
    show fc 37
    no "*Giggles* Do you like them?" with dis
    mc "Hell yeah..."
    no "Anything else you like...?"
    mc "Well, we can start talking about that sexy, toned tummy of yo–"
    $ renpy.music.set_volume(0.7, delay=9.0, channel='music3')
    play sound chair1
    play sound2 clotheswhoosh
    play sound3 whoosh6
    play sound4 squeak
    scene fc38 
    bla "Stirred by the shower of compliments, Nova enthusiastically leaps onto you, initiating another passionate kiss." with hpunch 
    play sound5 clothes3
    show fc 39
    mc "*Kissing her back* (God... her fragrance is intoxicating...)" with dis15
    no "MMMMmmmmm..."
    show fc 40
    mc "*Groping her butt* (I can't get enough of her body...)" with dis14
    mct "She's like pure energy, a mischievous little devil tempting me..."
    no "Mmmmmm..."
    mct "But I need to take it slow... Nova's first time has to be special."
    mct "Given her moans and reactions, she's probably fantasized about this even more eagerly than I have... I can't ruin it now."
    show fc 41
    no "MMMmmmmmmm..." with dis14
    show fc 42 with dis12
    no "*Interrupting the kiss* C-Can I..." with dis12
    no "*Whispering* Can I touch it...?"
    mc "*Whispering* Touch it...?"
    mct "Or maybe there's no need to be that gentle with her after all..."
    mc "*Whispering* Fuck yes, you can..."
    play sound clothes4
    play sound2 clothes5
    play soundlow zip volume 0.6
    scene fc 43 with dis17
    no "*Whispering* Oh my god..."with dis12
    no "*Whispering* You're so... hard..."
    no "*Whispering* I-Is that all for me?"
    mc "You know it is..."
    $ renpy.music.set_volume(0.45, delay=8.0, channel='music3')
    play sound clothes5 fadein 2
    $ renpy.music.set_volume(1.0, channel='soundloop')
    $ renpy.music.set_volume(1.0, channel='soundloop2')
    play soundloop wetting4 fadein 2
    play soundloop2 wetting4 fadein 2 volume 0.4
    scene novasex1 with dis2
    bla "Nova pulls your pants down and proceeds to jerk you off, as her lips close around yours once more." with dis12
    no "MMmmmmmmMMmm..."
    mct "Oh my god, her fingers are curled so tightly around my dick..."
    mct "She’s so soft..."
    mct "And the best part is that I didn't even have to prompt her or guide her into it."
    no "*Moaning in between breaths* AAaahhh..."
    mct "There’s a hint of nervousness behind each of her movements, but her fierce passion shines through."
    mct "This feels too damn good..."
    no "Mmmmmhh..."
    mct "I wanna make her mine..."
    pause
    stop soundloop fadeout 2
    stop soundloop2 fadeout 2
    play sound2 clothes3
    play sound rubclotheslong
    play soundlow squeak
    scene fc 44 with dis2
    no "*Leaning over your lap* MMmmmmmhh..." with dis12
    mc "Oh fuck yes..."
    show fc 45
    mc "I've missed your touch so much, Nova..." with dis12
    no "Me too..."
    no "I wanna... taste you again..."
    play sound4 clothes3
    show fc 46
    mc "*Pulling her panties down* Were you left yearning for more after the last time you sucked my cock, you naughty girl?" with dis14
    no "*Giggles* Maybe..."
    mc "It's all yours then..."
    $ renpy.music.set_volume(0.35, delay=7.0, channel='music3')
    play soundloop blowjob2 fadein 2
    scene novasex2 with dis2
    bla "Without thinking twice, Nova wraps her fleshy lips around your member and starts sucking your dick with fervor. Her slurpy sounds fill the air, ceasing only for her brief gasps for air."with dis 
    mc "Oooooohhhhh f-fuck yeaaaahhh..." 
    mc "That's it babe..."
    mct "Oh my god, she’s just pouring out drool from her mouth..."
    mct "I feel like I'm in heaven..."
    no "*Gagging* MMmmmhhh... mmmhmhhh..."
    scene novasex2b with dis2
    mc "Nice job..." with dis 
    no "*Gagging* MmmMmMMmmmhh..."
    bla "Nova’s every move makes it clear how much she’s savoring the moment. Her tongue glides enthusiastically around your cockhead, her desire to please overpowering her."
    mc "Oh Nova..."
    mc "You're so fucking good at this..."
    no "MMmmmmmh..."
    mct "Dear Lord, she barely needs to pause for breath..."
    mc "Please don't stop..."
    no "*Gagging* MMmmmm..."
    mc "Don't stop now..."
    pause
    play sound chair1
    play sound2 squeak
    stop soundloop fadeout 1
    scene fc 47
    bla "You suddenly stand up and push Nova onto the bed beside you."with dis12
    mc "F-Fuck, Nova, I'm about to lose it."
    mc "No more foreplay... I don’t want any more wasted time."
    mc "Let's do it NOW..."
    play sound4 squeak
    play sound3 clothes3
    play sound8 ["<silence 0.4>", bodycollide]
    scene fc 48
    bla "You spread Nova's legs and get on top of her, slapping your fully erect cock on her tummy with an enticing “plap.”"with dis12
    mc "I {i}need{/i} to be inside of you..."
    mc "I NEED to feel your pussy..."
    no "Aahh..."
    play sound5 clothes3
    show fc 49
    no "Mmmh... I c-can't. S-Sorry. I want to, b-but I can’t." with dis12
    mc "E-Eh? What? What happened?"
    no "I..."
    no "I promised my mom we wouldn't do it without a condom."
    mc "W-What?"
    mc "But... I d-didn't bring any. Do you have any here?"
    no "N-No."
    mc "Then..."
    mc "Shit, p-please don't bail on me now."
    no ". . ."
    mc "D-Do you really want to stop?"
    scene fc 50
    no ". . ." with dis15
    show fc 51
    mc "What if... I just make sure to finish outside?"
    mc "Would you want to continue then...?"
    show fc 50
    no ". . ."
    show fc 51
    no ". . ."
    play sound2 clothes3
    show fc 52
    no "*Playfully* Would you tell my mom?" with Dissolve(1.3)
    show fc 53
    mc "Not even a word..."
    no "Hmm."
    show fc 52
    no "Okay then..."
    show fc 53
    mc "*Teasingly* Okay, what?"
    show fc 52
    no "Okay... let's do it."
    show fc 53
    mc "Do what?"
    show fc 52
    no "*Giggles* You know what."
    show fc 53
    mc "Mmmm... not really, no. You'll have to be more explicit."
    mc "What exactly do you want me to do?"
    no ". . ."
    show fc 52
    no "*Whispering* I want you to fuck me."
    no "*Whispering* Now."
    show fc 53
    mc "Oh, Nova... hearing those words is literally a dream come true."
    play sound clothes3
    play soundlow squeak
    play sound7 ["<silence 0.6>", penetration2] volume 0.6
    play sound6 rubbody volume 0.6
    scene fc 54
    bla "You gently place the tip of your dick on Nova's pussy. A soft moan escapes her lips, but her eyes betray no sense of nervousness. She is ready for you." with dis12
    no "Aaah..."
    mc "You sure about this...?"
    no "*Whispering* Yes..."
    no "*Whispering* Put it in..."
    mc "Here we go..."
    play sound penetration3
    show fc 55
    mc "AAAAaaaaahh..." with dis15
    no "AAAAAAaaaAAAGhh..."
    mc "F-Fuck, you're so tight..."
    play sound2 clothes3
    play sound4 squeak 
    show fc 56
    no "*Panting* OH MY GOD."with dis12
    no "*Panting* OH MY G-GOD, IT'S IN."
    show fc 57
    mc "It is, at last..."
    show fc 56
    no "It feels so huge..."
    show fc 57
    mc "I'm gonna start to move, okay?"
    show fc 56
    no "Yes..."
    no "O-Okay..."
    no "I'm ready..."
    play soundloop novasex3 fadein 2 volume 1.1
    scene novasex3 with dis2
    no "*Moans* Aaahh..." with dis12
    no "Oh my g-god..."
    no "OH MY FUCKING GOD."
    mc "Ohhhhh Nova, FINALLY..."
    mc "You have no idea for how long I've been longing for this... how long I’ve been thinking about this..."
    no "M-Me too..."
    no "*Panting* I've b-been dreaming about this... f-for ages..."
    mc "Dear Lord, you're too tight..."
    no "*Panting* You're too big..."
    mct "If she wasn't absolutely soaked right now, I wouldn't even be able to fit the tip in..."
    mct "But fuck me, this feels like heaven..."
    no "*Moans* AAAAaaaAAaahh..."
    mc "D-Does it hurt...? L-Let me know if it’s too much..."
    no "N-No! It feels..."
    no "A-A-AaAAagghhh..."
    no "{bt=3}*Moans* Good...{/bt}"
    mc "Good girl..."
    no "*Moans* AAAAAaahhh..."
    no "Oh, [mc]..."
    mc "Do you like feeling me inside of you? Is it what you hoped for?"
    no "*Moaning* I f-fucking love it....."
    stop soundloop fadeout 2
    play sound clothes3
    play soundlow squeak
    scene fc 58
    mc "I don’t believe you... let me check that myself..." with dis2
    no "*Giggles* Mmmmmmh..."
    play sound2 rubbody
    show fc 59
    bla "You lift Nova's shirt up, revealing her erect nipples." with dis15
    mc "Ah, you weren’t kidding..."
    no "*Giggles* Mmmh..."
    mc "God, you're so fucking hot."
    mc "Ready to speed up a bit...?"
    no "*Giggles* Mm-hm..."
    play sound5 clothes3
    play sound6 clothes3
    play sound7 squeak fadein 1 volume 0.6
    play soundloop novasex3b fadein 2
    scene novasex3b with dis2
    no "AAAAaahhhhh... aaaaahhh..." with dis12
    mc "*Panting* Oh baby..."
    no "MMmhh.... mmmmm.... mmmggghh..."
    pause
    no "*Panting* J-Jesus..."with dis12
    mc "Ohh y-yeah..."
    no "*Panting* Oh [mc]..."
    no "*Panting* From down here you look so..."
    no "*Panting* So p-powerful... so strong..."
    no "*Panting* I can see... all your muscles..."
    no "*Panting* The veins on your a-arms... you’re so... unghhh..."
    no "*Panting* AAAaaAAAaaAaahhhh..."
    no "*Panting* P-Please, take me..."
    no "*Panting* Make me yours..."
    bla "Nova's words, coupled with the sight of your manhood penetrating the petite ginger girl's pale physique, kindle a fire within you. You renew your thrusts with exuberance."
    mc "AAahhh... FUCK YES..."
    no "D-Do you like my body too?"
    mc "I fucking love your body... your skin... your cute face... your tight ass..."
    no "*Moaning* MMMMmmmmmhh... yeah..."
    mc "Your pussy feels like it’s... sucking me in..."
    no "*Moaning* Oh [mc]..."
    no "*Moaning* This feels... i-incredible..."
    no "AAAAAAGGHH....."with hpunch 
    no "YES... give it all to me..."
    no "Go deeper..."
    no "G-Go faster..."
    mc "Deeper?"
    mct "I can actually sense her tension easing and her body getting more relaxed... maybe she's ready for some harder thrusts?"
    mc "A-Are you sure?"
    no "*Panting* I've never been m-more certain of anything..."
    no "*Panting* Give me every inch..."
    stop soundloop fadeout 1
    play sound chair1
    play sound3 clothes3
    play sound4 rubclotheslong
    play sound2 squeak
    scene fc 60
    bla "You finally peel off Nova's shirt and pin her body against the bed." with dis
    mc "Now you'll see the real deal..."
    no "*Breathing heavily in anticipation* Yeah..."
    no "*Breathing heavily in anticipation* Fuck me HARD, [mc]..."
    play sound4 squeak
    scene novasex3c with dis2
    no "Oh my GOD....." with dis12
    no "{sc=2}Oh my fucking GODDDDD........{/sc}"
    bla "You begin thrusting your hips relentlessly against Nova's, your dick hitting the deepest parts of her with each thrust. Goosebumps appear all over her skin as she adjusts to your new speed."
    mc "OOOOOOooohhh fuuuuuck..."
    mct "I knew she could take it all... she might be petite, but she's resilient as a nail."
    mc "AAAahh..."
    mc "N-Now we're talking, babe..."
    no "*Panting* AAAAAAhhh... AAAHHHHH... AAAAGGGGHHHGHH..."
    mc "O-Oh sweet heavens, t-this is amazing..."
    no "*Panting* Oh Lord... y-you're gonna break me..."
    mc "Isn't this what you wanted...? Didn’t you hope I’d f-fuck you like this?"
    no "*Panting* AAAAAAGgghhh... yeah..."
    pause
    no "Oh my god..."with dis
    no "{sc=2}Oh my god......{/sc}"
    no "{sc}OH MY GODDDDDD......{/sc}"
    play soundlow chair1
    play sound squeak
    scene novasex3c2 with hpunch
    mc "*Panting* FUUUUUUCKKK...." with dis12
    no "*Panting* OH GOOD GRACIOUS..."
    no "*Panting* Aaahhhh..."
    no "*Panting* I d-d-don't think I can keep up this pace, [mc]..."
    if novadildo:
        mc "*Panting* I saw your pussy devouring that dildo, Nova..."
    mc "*Panting* I know you can do this..."
    if novadildo:
        no "*Panting* B-But you're WAY thicker than t-that..."
        no "*Panting* And w-way more..."
    else:
        no "*Panting* T-This is just too..."
    no "{sc=2}*Panting* Intense....{/sc}"
    mc "*Panting* Aaaahhh..."
    mc "*Panting* I love how wet you are, even at this speed..."
    no "*Panting* I'm gonna cum, [mc]..."
    no "*Panting* I can't..."
    no "*Panting* H-Hold it..."
    no "*Panting* Any..."
    no "*Panting* MORE!!!!"with hpunch
    no "{sc=2}*Panting* [mc!u]....{/sc}"with hpunch
    play sound cumall
    play sound2 chair1
    play sound3 squeak
    scene fc 59b
    no "{sc=2}*Orgasming* AAAAAAAaaghhhhhhhhhgh...{/sc}" with hpunchlong4 
    play sound4 cum4
    play sound5 squeak
    bla "You stop as Nova’s thighs wrap tightly around your waist, her shudders and shakes surprising you as she orgasms." with hpunch
    play sound6 cum4
    play sound7 squeak
    scene fc 59b
    no "{sc=2}*Orgasming* AAAAAAAaaghhhhhhhhhgh...{/sc}" with hpunchlong4 
    mc "*Panting* Damn..."
    no "*Panting* OH, [mc!u]..."
    no "*Giggles* T-This sensation was... indescribable..."
    mc "Y-Your hips spasmed so hard that I thought you were gonna snap my cock..."
    no "*Giggles* S-Sorry..."
    play sound ["<silence 0.6>", chair1] volume 0.7
    play sound2 ["<silence 0.6>", squeak]
    play sound3 clothes3
    play sound4 rubbody
    scene fc 61
    bla "As though she were a squirrel clinging to a branch, Nova deftly spins on top of you, prompting you to sit on the bed." with dis17
    mc "Huh...?"
    no "*Recovering her breath* We're not done here yet..."
    no "*Panting* I need..."
    scene novasex4 with dis2
    no "*Panting* Moreeeee..." with dis12
    no "*Panting* Oh my goddd..."
    bla "Nova starts to bounce on your cock, seemingly immune to fatigue."
    mc "Oooohhh Lord..."
    no "*Moans* AAAaaahh..."
    no "*Moans* Aaaaaahhhh... it's sp-preading me apart..."
    mc "You're doing just fine... keep going..."
    mc "Ride that cock for all it’s worth..."
    bla "The tantalizing view of Nova's petite breasts bouncing right in front of your face propels you into a new realm of heightened sensations and pleasure."
    bla "Her ceaseless energy awakens something deep within you, enhancing your own drive."
    mc "M-My god, Nova, yessss..."
    mc "So good..."
    no "*Moans* Yeaahhh..."
    mc "Go faster..."
    no "*Moaning* Can I...?"
    mc "How is that even a question...?"
    no "*Giggles* Okay..."
    scene novasex4bswitch with dis2
    no "*Panting* AAAaaaagghhhh... aaaaaahhh... aaaAaaaAAAhh..."with dis12
    mc "O-O-Ohh f-fuck..."
    show screen novaangle1 with dis
    pause
    no "*Moans* Oh my g-god, [mc]..." with dis
    no "AAAAaahhhh..."
    mc "D-Does this feel as good as you expected?"
    no "*Moans* It f-feels M-MUCH BETTER..."
    no "AAAaahhh... aaaghhhh..."
    mc "Good..."
    no "*Panting* I can feel you... deep within... exploring every part of me..."
    no "*Panting* This feels... like m-magic..."
    no "{sc=2}AAAAAHHhhhhhh...{/sc}"
    mc "Ohhh fuck, you're a total addict..."
    no "*Panting* Holy fuck, all that wait was so worth it..."
    no "{sc=2}*Biting her lip* MMMHhhMMMMmmmhhhh.....{/sc}"with hpunch 
    mc "AAaghh..."
    no "*Panting* All those awkward talks about sex at school and college where I couldn't join in..."
    no "*Panting* It was all worth it... just for this moment..."
    no "*Panting* Oh, [mc]..."
    mc "F-Fuck yes..."
    mc "We have to make up for the lost time now..."
    no "*Panting* Y-Yes, we have to..."
    no "*Panting* I want you to f-fuck me... every day..."
    if novadildo:
        mc "And we'll have to hit up another party soon and play the polygraph game with Dolores and Haskel again, eh?"
        mc "You’ll probably have spicier things to tell this time..."
        no "*Giggles* YEEESsssss PLEASE!!!"
    play sound chair1
    play sound2 squeak
    scene novasex4cswitch 
    show screen novaangle2
    hide screen novaangle1
    with dis14
    no "{sc=2}AAAAAHHhhhhh... aahaahhh... aaaAAAGGHHhh....{/sc}" with dis12
    bla "Nova pushes you down onto the bed, molding her body against yours and taking your dick as deeply inside her as she can."
    no "{sc=2}AAAHHhh... aahhh... aaaghahhhh....{/sc}"
    mc "*Panting* Good grief..."
    pause
    no "{sc=2}*Faint voice* Oh my g-god, [mc], I-I'm gonna cum again...{/sc}"with dis 
    mc "*Panting* F-Fuck, me too, Nova..."
    mc "*Panting* I'm at my a-absolute limit..."
    no "{sc=2}*Panting* P-Please, just give me 20 seconds...{/sc}"
    no "{sc=2}*Panting* I'm almost there...{/sc}"
    no "{sc=2}*Panting* Please d-don't move...{/sc}"
    mc "*Panting* Oh god..."
    bla "You avert your gaze from the sight of the ginger girl's perfect body, and instead silently implore the spirits for the strength to endure another 20 seconds."
    no "{sc=2}AAAAAHHhhhhh...{/sc}"
    mc "*Panting* N-Nova..."
    no "{sc=2}*Panting* I'm cumming...{/sc}"
    no "{sc=2}*Panting* I'M CUMMING!{/sc}"
    play sound cum4
    no "{sc=2}*Panting* OH MY GOD, [mc!u]!!!{/sc}" with hpunch 
    play sound2 cum4
    no "{sc=2}AAAAAAAAAAAGGHHHHHHHH...{/sc}" with hpunch 
    play sound cum4
    no "{sc=2}YEEEESSSS...{/sc}" with hpunch 
    mc "{sc=2}F-FUCK, I CAN'T...{/sc}"
    play sound penetration3
    play sound2 penetration2
    play sound3 squeak
    play soundlow chair1 volume 0.33
    play sound4 penetration3
    scene fc 62 
    hide screen novaangle2
    with dis
    bla "At the very last second, Nova lets your cock slip out of her pussy, right as you climax." with dis
    play sound5 slap1
    play sound6 cumall
    show fc 63
    mc "*Cumming* AAAAAAAAAAHHHHHH..." with hpunchlong3
    play sound7 cumall
    show fc 63
    mc "*Cumming* FUUUUUUUUCCKKKK..." with hpunchlong3
    play sound6 cumall
    show fc 63
    mc "*Cumming* OOOoooooohhh..." with hpunchlong3
    no "Whoa..."
    play sound chair1
    play soundloop rain3 fadein 20
    stop music3 fadeout 18
    scene fc 64
    mc "*Collapsing onto your back* OH MY GOD....." with dis12 
    mc "*Breathless* Man..."
    mc "*Breathless* What in the world just happened..."
    mc "*Breathless* I don't even know if I'm still in the same dimension..."
    play sound2 squeak
    play sound3 clothes3 
    play sound4 clothes3
    scene fc 66
    bla "You watch Nova as she hops off you and rolls over the bed, purring like a playful cat." with dis15
    show fc 65
    no "Oh, [mc]..."
    no "Just... WOW."
    show fc 66
    mc "I take it you enjoyed it..."
    show fc 65
    no "Enjoy...?"
    no "I enjoy drawing and watching anime, this was..."
    no "I don't even know what this was."
    show fc 66
    mc "*Chuckles* I'm–"
    play sound chair1
    play sound2 squeak
    show novasexzoom
    no "C-Can we do it again?!" with vpunch 
    scene fc 68
    mc "*Chuckles* Of course, we..."
    mc "Wait... you mean... now?"
    show novasexnod
    no "*Nods*"
    mc "Now... like... immediately?"
    scene novasexnod
    no "*Nods*"
    mc "Um..."
    mc "I m-mean... I-I'd love to, but I need a little rest. R-Refractory period and all."
    mc "The spirit is willing, but the flesh is spongy and... bruised."
    scene fc 67
    no "Rest like... for a minute?"
    scene fc 68
    mc "M-More like..."
    no ". . ."
    mc "...10?"
    play sound squeak
    play sound2 clothes3
    show fc 69
    no "*Sitting up* PERFECT!" with dis
    no "Right on schedule! Enough time to eat and head back to The New World later, but also just enough for me to do something I've been itching to try!"
    show fc 70
    mc "W-What are you going to do...?"
    show fc 69
    no "It's a surprise!"
    no "Give me 10 minutes!"
    no "Actually... I already straightened my hair, so... just 5!"
    no "You stay here and recover!"
    play sound squeak
    play sound2 dooropen1
    play sound3 run
    scene fc 71
    bla "Nova bolts out of the room at lightning speed." with dis2
    play sound4 chair1
    scene fc 64
    mc "*Lounging back on bed* Holy cow..." with dis
    mct "This girl is going to be the death of me."
    mct "She really has unlimited energy... and what's better, she knows how to use it."
    no "I'm almost finished!"
    mc "Not even a minute has passed!" with hpunch
    no "There's water and eggs in the fridge if you need them!"
    mc "O-Okay, thanks!"
    mct "Oh Jesus, she wants to wring me out like an orange..."
    mct "I mean... not that I'm complaining."
    mct "I never thought I'd find someone who'd match my energy levels, but damn..."
    mct "And how tight and wet she is... sheesh. Wars have been fought over less."
    play sound doorclose
    no "*Closing the door* Done!"
    mc "Oh my gosh, Nova, it hasn't even been 3 minutes..."
    $ renpy.music.set_volume(0.5, channel='music3')
    play music3 ["<silence 1.3>"]
    queue music3 silverware fadein 4
    stop soundloop fadeout 16
    play sound wood2
    show fc 72
    mc "*Turning your head towards her* You can't expect me to..."with dis14
    mc "Oh my god."
    play sound2 chair2
    play sound3 squeak
    scene fc 73
    mc "*Standing up* Oh my fucking god..." with dis12
    bla "You can feel your body deciding to defiantly ignore any notion of a refractory period, as blood rushes to your cock."
    mc "How..."
    mc "Is that a wig?"
    show fc 75
    no "*Giggles* Of course not!" with dis 
    no "But it's not a real dye, just a spray can I bought."
    no "The blue color will wash away the next time I shower."
    show fc 74
    if novadildo:
        mc "Oh fuck, babe, you don’t know how much I’ve wanted this..."
        show fc 75
        no "I've been wanting to do this since the party when I first wore this cosplay."
        no "It's been lingering in my mind since that day..."
        show fc 74
        mc "You and me both..."
        show fc 75
        no "Except this time... no alarms will go off if we get too close."
        no "*Whispering* This time... we can touch each other as much as we want..."
    else:
        mc "Oh fuck, babe, this is REALLY turning me on, and I don't even play that game..."
        show fc 75
        no "*Giggles* It's not Jinx from the game, but the show! It's different!"
        show fc 74
        mc "Wherever it's from, I like it..."
    play sound wood2 volume 0.5 fadein 2
    play sound2 rubbody
    play soundlow clothes3
    scene fc 76
    bla "You effortlessly scoop up Nova by the thighs, lifting her against the wall as if she weighed nothing." with dis12
    if novadildo:
        mc "Fuck yes, we can..."
    show fc 77
    no "*Giggles* You're so strong..."
    show fc 76
    if novadildo:
        mc "You can't even imagine how many times I pictured myself fucking you in your Jinx costume."
    else:
        mc "Fucking you while you're in cosplay is a fantasy I didn't even know I had."
    show fc 77
    no "Well... you can make it a reality now."
    no "Fuck me right here and right now."
    show fc 76
    mc "Is that what you want, you dirty girl?"
    show fc 77
    no "Yeah..."
    no "I want you to fuck me against this wall just like you fucked Maat that day in front of me..."
    no "Make me scream like she did..."
    no "Actually... scratch that. Make me scream louder..."
    show fc 76
    mc "Oh yeah..."
    play sound penetration2
    scene novasex5 with dis2
    bla "You penetrate Nova's warm pussy once more, pressing her against the wall with strong, passionate thrusts." with dis12
    no "AAAAaaahhh..."
    mc "L-Like this?"
    no "*Moans* Yessss..."
    no "*Moans* Oh, fuckkk..."
    no "*Moans* Y-You're so deep..."
    mc "Aaaaahhh... I know..."
    no "*Whines* AAAAaghhh... f-fuck..."
    mc "I thought Jinx was a tough one..."
    no "AAAahh... I-I am a tough girl...."
    mc "Are you...?"
    no "Yeah... and I can... pr-prove it..."
    no "F-Fuck my pussy, [mc]..."
    no "Make it yours..."
    no "Do whatever you want to me..."
    no "{bt=3}*Whispering* I can take it all...{/bt}"
    play sound slam
    scene novasex5b
    pause 0.001
    no "{sc=2}*Panting* AAAAHHH.... AAAAGHHhhhh...{/sc}" with hpunch
    mc "*Panting* Ooooohhhhh..."
    no "*Panting* AAAAagGGGHHHH..."
    no "*Panting* J-Just like thisss..."
    no "*Panting* OOOoooggghhhhh... aaaAAAAaaHHh...."
    no "*Panting* T-This is c-completely surreal..."
    no "{sc=2}*Panting* OH MY GODDDDD...{/sc}"with hpunch 
    mc "F-Fuck yeah..."
    no "{sc=2}*Panting* AAAAAAGHHH... YESSSS...{/sc}"
    mc "I r-really hope these walls are thick enough, or the next encounter with your neighbors might get a tad awkward..."
    no "*Panting* AAAAHHHH... "
    no "*Panting* P-PLEASE DON'T STOP..."
    bla "Yielding to the moment, Nova just lets herself go and completely surrenders her body to you, her sole focus to maintain a tight grip on your neck."
    mc "*Panting* Oh shit..."
    mc "*Panting* I'm g-gonna cum again..."
    no "*Panting* AAAAAHHHHH..."
    no "*Panting* NOT YET, PLEASE..."
    mc "*Panting* I-I can't stop it..."
    no "*Panting* I'm gonna cum too..."
    no "*Panting* I'm almost there..."
    mc "*Panting* I-I have to set you down..."
    no "*Holding onto your neck* NOT YET PLEASE..."
    no "{sc=2}*Panting* AAAAGH!!!{/sc}" with hpunch 
    mc "*Panting* Oh, Nova..."
    mc "*Panting* O-Okay, I really have to set you down now..."
    mc "*Panting* I have to s-stop or I'm gonna finish insi–"
    play sound bodycollide2
    play sound2 fall3
    play sound4 fall2
    play sound3 clotheswhoosh
    play sound5 penetration2
    scene novaspinner
    bla "Nova twirls around you like a fidget spinner, clasping onto you incredibly tightly and forcing you to lean against the wall." with hpunch
    $ ns5c = True
    scene novasex5cswitch 
    show screen novaangle3
    with dis2
    mc "{sc=2}O-O-OHHH FUCKKKKK.....{/sc}" with dis12
    no "{sc=2}*Squeals* AAAAHHHH.... AAHHH.... AAAAAGGGGHH...{/sc}"
    mc "{bt=3}W-W-What the fuck are you doing, Nova...{/bt}"
    no "{sc=2}*Squeals* F-Fuck yes...{/sc}"
    no "{sc=2}*Panting* Oh my god, this is AMAZING....{/sc}"
    mc "{bt=3}O-Oh s-sweet Jesus....{/bt}"
    no "{sc=2}*Squeals* AAaaaahhh...{/sc}"
    mc "{bt=3}Y-You're fucking crazy...{/bt}"
    no "{sc=2}AAAAAAAAGGHHHhhh...{/sc}"
    no "{sc=2}P-Please don't let me go, [mc]...{/sc}"
    mc "{bt=3}I'm not even holding you...{/bt}"
    no "{sc=2}*Squeals* AAAAAAAHHHH!!!!{/sc}" with hpunch 
    bla "Nova continues to milk you furiously, letting out a piercing shriek with each forceful collision of your cock against her petite form." 
    no "{sc=2}AAaaghhh... aaaghhh... aaAAAhhh... AaaggGGhh...{/sc}"
    mc "{bt=3}Nova, s-stop...{/bt}"
    mc "{bt=3}You're gonna make me cum inside...{/bt}"
    no "{sc=2}*Panting* I don't c-c-care anymore...{/sc}"
    no "{sc=2}*Panting* I-I want you to f-fill me up...{/sc}"
    mc "{bt=3}B-But you said...{/bt}"
    no "{sc=2}*Panting* E-Empty yourself INSIDE of me...{/sc}" with hpunch
    mc "{bt=3}Oh f-fuck...{/bt}"
    mc "{bt=3}I-I'm cumming so much...{/bt}"
    no "{sc=2}*Panting* Yeah... cum inside me... please. Please. Pleaseeeee.{/sc}" with hpunch
    play soundlow thunder fadein 1
    scene novasex6 
    hide screen novaangle3
    with dis12
    play sound4 ["<silence 6.72>", cum3]
    play sound3 ["<silence 7.22>", cum3]
    play sound2 ["<silence 8.05>", cum3]
    play sound ["<silence 9.2>", cumall]
    play sound6 ["<silence 9.2>", slap1]
    no "{sc=2}I'm cumming...{/sc}{w=1.3}{nw}" with dis08
    no "{sc=2}OH [mc!u]...{/sc}{w=1.1}{nw}" 
    no "{sc=2}YES.{/sc}{w=0.38}{nw}"
    no "{sc=2}YES. YES.{/sc}{w=0.37}{nw}"
    no "{sc=2}YES. YES. YES. {/sc}{w=0.37}{nw}"
    no "{sc=2}YES. YES. YES. YES. {/sc}{w=0.37}{nw}"
    no "{sc=2}YES. YES. YES. YES. YES. {/sc}{w=0.37}{nw}"
    no "{sc=2}YES. YES. YES. YES. YES. YES.{/sc}{w=0.37}{nw}"
    no "{sc=2}AHH!{/sc}{w=0.28}{nw}"
    no "{sc=2}AHH! AHH!{/sc}{w=0.28}{nw}"
    no "{sc=2}AHH! AHH! AHH! {/sc}{w=0.28}{nw}"
    no "{sc=2}AHH! AHH! AHH! AGHH! {/sc}{w=0.28}{nw}"
    no "{sc=2}AHH! AHH! AHH! AGHH! AAAGGHHH!!!!{/sc}{w=0.29}{nw}" 
    no "{sc=2}AAAAAGH!!{/sc}{w=0.5}{nw}"with hpunch 
    no "{sc=2}{size=33}AAAAAAAAAAAHHH!!!{/sc}{w=0.83}{nw}"with hpunch 
    no "{sc=3}{size=36}AAAAAAAAAAAAAGGGGGHHHHH!!!!{/sc}{w=1.15}{nw}"with hpunch 
    no "{sc}{size=39}AAAAAAAAAAHAAAGGGGGHHHHHHHHHH......{/sc}{w=2.9}{nw}"with hpunch 
    stop music3 fadeout 16
    play soundloop rain3 fadein 11
    play sound4 penetration3
    scene fc 79 with Dissolve(1.3)
    no "{bt=3}*Finally releasing her tight grip* AAAaaAaaaaggghhh...{/bt}"with dis2
    mc "*Panting* Oooooh jeeeezzzz..."
    mct "God, I feel like I just unloaded 3 gallons of cum inside her..."
    mct "Even though I came twice in less than 10 minutes..."
    no "*Panting* W-W-Waaawaaa...."
    mc "*Panting* Oh, Nova..."
    play sound penetration3
    play sound2 rubbody
    play sound4 ["<silence 0.9>", fallfull]
    scene fc 80 with Dissolve(1.1)
    no "*Collapsing to the floor* G-Gggaaaaahhh..." with vpunchslow
    mc "Oh boy..."
    $ renpy.end_replay()


label ga_penny3:
    $ renpy.music.set_volume(0.4, channel='music3b')
    play music3b pennysex fadein 2
    show fg 80 
    mc "*Turning around* Hmm?" with Dissolve(1.3)
    mc "Oh Lord..." 
    show fg 81
    p "Probably even a bit too much lately, but... *giggles* that's beside the point now."
    p "You know, all this... fooling around between us?"
    show fg 80
    mc "Aha..."
    show fg 81
    p "I've come to the conclusion that... there's nothing wrong with it."
    show fg 80
    mc "Nothing wrong, no..."
    show fg 81
    p "I mean, we're just having fun."
    p "And isn't that what matters most?"
    show fg 80
    mc "Those are my thoughts exactly..."
    show fg 81
    p "Good! I just wanted to make sure we were on the same page."
    p "As long as we don't cross the line... it's all good."
    p "It'd just bring waaay too many headaches... I don’t think either of us want more drama in our lives."
    show fg 80
    mc "And... where exactly are we drawing that line...?"
    show fg 81
    p "*Giggles* You know exactly where."
    p "So, before we continue with this little photo session... do you think we can control ourselves?"
    p "Or should we hit the brakes right here?"
    show fg 80
    mc "I'm known for my self-control. But I have a better question: do we want to?"
    mc "Like you said, there's nothing wrong with a bit of... fooling around."
    mc "Just a spicy photo session."
    show fg 81
    p "Exactly."
    p "Again, good to see we're on the same page."
    show fg 80
    mc "The very same."
    p "Mm-hm..."
    play sound clothes3
    play sound2 clothes3
    show fg 82 with dis2
    bla "Penelope gracefully glides along the studio's light stand, leaning against it, and unveiling her naked form before you." with dis
    mc "Oh my fucking god..."
    show fg 83
    p "I'm glad I have a friend who I trust and with whom I can do these kinds of things, [mc]."
    p "I would have never dared to do a naked session if it wasn't for you."
    p "Even if the photos were supposed to be private."
    show fg 82
    mc "It should be a crime to cover your body with clothes..."
    show fg 83
    p "*Giggles* Alright, so... come on, take a pic. Bring out the artist in you."
    p "Do you think this pose enhances my... features?"
    play sound zoomout
    show fg 82
    show camera2
    mc "I think it does, yes..." with dis08
    play sound camera
    show black
    pause 0.08
    hide black
    pause
    show fg 83
    p "I also want a picture with you."with dissolve
    show fg 82
    mc "Just you and me?"
    p "Mm-hm."
    mc "With me... naked?"
    p "Mm-hmmm..."
    mc "*Chuckles* Very well."
    mc "What kind of manager would I be if I refused such a simple request from my client?"
    play sound clothes
    play sound2 belt
    scene fg 84 with dis17
    bla "You race to shed your clothes, Penny’s gaze on you all the while. You notice her gaze growing more and more lustful with every passing second."with dis12
    show fg 86
    mc "Do you like what you see? Do I look... artistic?"with dis12
    show fg 85
    p "*Giggles* Very much."
    p "I'll admit it's quite alluring to see you in this lighting."
    p "Regina's room was... too dark to appreciate it all."
    show fg 86
    mc "I could say the very same thing..."
    play sound clothes3
    show fg 88
    p "*Approaching you* Alright, big boy..." with dis15
    p "Let's take a pic together."
    p "Do you remember last time?"
    p "You sitting, and me perched on top of you."
    show fg 87
    mc "I do..."
    show fg 88
    p "Only this time... *giggles* I won't jump up all startled when I notice your junk, don't worry."
    show fg 87
    mc "That sounds good..."
    show fg 88
    p "You can leave your phone on that tripod with timed shots enabled, or... even recording."
    p "Then we can select the perfect shot and keep it for ourselves... sound good?"
    show fg 87
    mc "That's a fantastic idea..."
    show fg 95b with dis17
    bla "You grab your phone and set it up on a tripod, aiming the camera at the Lamborghini, and start recording." with dis12
    p "Good."
    mc "Good..."
    play sound ["<silence 0.1>", carsuspension2]
    play sound2 clothes3
    show fg 90
    p "*Sitting on the car* Are you okay? Your mind seems to be elsewhere, [mc]." with dis12
    show fg 89
    mc "I can assure you, my mind is only in one place in the world right now..."
    show fg 90
    p "You're not secretly plotting to sell these pics online, right?"
    show fg 89
    mc "I'd never let another man see you in your most glorious form."
    show fg 90
    p "Oh my, so selfish..."
    play sound ["<silence 0.1>", carsuspension2]
    show fg 91
    bla "You sit on the car's hood next to Penelope." with dis12
    play sound3 rubbody
    play sound2 carsuspension2
    show fg 92
    p "*Climbing on top of you* Does it bother you if I sit like this? Or... is it too much...?" with dis12
    mct "Oh sweet Lord Jesus, she's not wasting any second..."
    p "...[mc]?"
    play sound4 rubbody
    show fg 93
    mc "Does it bother you if I touch you like this...?" with dis12
    scene pennygrop1 with dis2
    p "*Soft moan* Aahh..." with dis
    p "N-No, it doesn't..."
    mct "Boy, I could never get enough of her massive, perfect tits..."
    mct "They're almost too much to hold in just my hands."
    p "*Soft moan* Mmmmh..."
    mct "And those perky nipples tell me she's as excited as I am..."
    p "*Soft moan* Aahh..."
    mc "Penny..."
    p "Yeah...?"
    mc "I might have overestimated my self-control..."
    mc "I-I'm having a hard time right now trying to control myself..."
    play sound2 bodycollide2
    play sound rubbody fadein 1
    play sound2 rubbody fadein 1
    scene fg 94b
    bla "Penelope seizes your hands and redirects them downward." with dis15
    show fg 95
    p "I'll admit that... I'm a bit horny right now too." with dis12
    p "But... that's normal."
    p "We're just humans after all. We have a history together, and this is quite an... explicit session."
    p "But as long as we... don't cross..."
    play sound3 clothes3
    scene pennysex0 with dis2
    p "The line..." with dis
    mc "O-O-Oh my god..."
    p "As long as we keep it..."
    p "*Whispering* Professional..."
    bla "Penny starts sensually gliding her hands up and down your shaft, pressing it against her pussy and moistening it with her touch. You can practically feel her needy warmth."
    mc "Oh, fuck..."
    p "*Whispering* God..."
    p "*Whispering* I-It feels... so... massive..."
    mc "Oh, Penny..."
    p "*Whispering* So warm..."
    bla "Penelope continues to touch your fully erect member as a prolonged silence surrounds you."
    pause 
    p "*Deep exhale* Fuuu..." with dis06
    mc "I-Is everything okay?"
    p "Can I..." 
    p "C-Can I be frank with you, [mc]?"
    mc "Of course..."
    p "*Deep exhale* Okay..."
    p "All this teasing between us... it started off as a game because I just loved watching how jittery you'd get every single time."
    p "But... then... it went too far. That day at Regina's room. It went way too far."
    p "I tried to stop... but I couldn't."
    p "I... I thought that if I acted casually about it, if I didn't make a big deal out of it... it would stay like that. As a game."
    p "That I would stop thinking about you 24/7."
    mc "And...?"
    p "And..."
    p "*Biting her lip* F-FUCK, this isn't working, [mc]." 
    p "I'm..."
    p "I-I think I'm a little more than just a bit horny right now..."
    p "It's... almost..."
    p "{sc=1}Painful...{/sc}"
    mc "You're not the only one feeling that way..."
    play sound rubbody
    play sound2 clothes3
    scene fg 97b
    p "*Biting her lip* W-We probably should stop here for today..." with dis15
    p "Before that other wild idea of mine pops back into my head, and we end up regretting this forever."
    mc "What other idea...?"
    scene fg 97c
    p "Ah... nothing. It was just... a c-crazy thought I had."
    show fg 97
    mc "I'd really like to hear it..."
    show fg 97c
    p "It's not worth it. It was {i}really{/i} crazy."
    show fg 97
    mc "I {i}really{/i} like crazy ideas, Penny..."
    p ". . ."
    mc "Come on, please..."
    show fg 96
    p "Well... I thought..."
    show fg 97c
    p "Um... imagine for a second... hypothetically... if there were absolutely no consequences for your actions. Stay with me, alright?"
    show fg 97
    mc "Alright..."
    show fg 96
    p "I thought that..."
    p "Maybe..."
    p "The solution to get rid of all this sexual tension between us..."
    p "Would be to..."
    show fg 98
    p "*Removing her gloves* To..." with dis15
    p "Actually... {w=0.5}have... {w=0.5}sex...{w=0.5} once." 
    p "Just... once."
    show fg 99
    mc ". . ."
    mc "W-What did you just say...?"
    show fg 98
    p "I think it's my imagination that’s been driving me insane lately."
    p "So maybe if I just..."
    p "F-Feel it once."
    p "Instead of {i}thinking{/i} about how you’d f-fuck... or about how your cock would feel in my t-tight pussy..."
    p "If I could just actually feel it once..."
    p "Without feelings attached..."
    show fg 100
    p "*Caressing your dick* Maybe then... the sexual tension would ease up..." with dis15
    p "And we could go back to being our regular selves."
    p "Hah... crazy idea, right...?"
    mct "Oh my fucking god, YES PLEASE..."
    p "Am I crazy?"
    mc "No, you're not..."
    p ". . ."
    show fg 99
    p ". . ." with dis14
    show fg 98
    p "O-Okay..."
    p "Let's keep it casual."
    show fg 100
    p "I-I'm gonna try to... put it inside. Once." with dis12
    mct "Oh sweet heavens."
    p "Let's cross this line... just once."
    p "And after this... the game will be over. It will be... our secret."
    p "Forever."
    show fg 98
    p "Deal...?"with dis12
    show fg 99
    mc "Deal..."
    show fg 100
    p "Alright..." with dis12
    p "Here goes nothing..."
    play sound ["<silence 0.1>", carsuspension2]
    play sound2 clothes3
    show fg 101b with dis15
    bla "Penelope sits up and lets out a moan as the head of your cock rubs against her pussy lips." with dis12
    p "*Moans* Aaahh..."
    mct "She's wet as fuck even without any kind of foreplay..."
    p "S-Shit... this is crazy, [mc]."
    p "We're crazy."
    mc "This is the best idea you've ever had in your life."
    p "*Giggles* Of course you'd say that..."
    p "Okay..."
    p "Okay."
    p "Are you ready...?"
    mc "I'm not sure if I'm ready, but I certainly want it..."
    p "*Deep exhale* . . ."
    play sound5 penetration2 fadein 1
    play sound6 clothes3
    show fg 102 with dis2
    bla "After a brief moment of hesitation, she slowly lets the tip of your cock slide inside of her dripping pussy." with dis12
    p "*Moans* O-O-Oooohhh..."
    mc "Oh god, FINALLY..."
    p "F-F-fuck, IT'S IN."
    mc "It is..."
    play sound6 penetration2 fadein 1
    show fg 103
    p "MMMmmmmmMmmhhh..." with dis17
    show fg 104
    p "O-Ohhh wooOOOow, that feels..." with dis12
    p "Holy fuck, [mc], that feels..."
    p "G-Good..."
    $ renpy.music.set_volume(0.2, delay=9.0, channel='music3b')
    play soundloop pennysex1 fadein 5
    scene pennysex1 with dis2
    p "{sc=2}M-MY GODDDDD....{/sc}" with dis12
    mc "Ooh PENNY...."
    mct "Oh my god, it's happening at last."
    mct "No more teasing."
    mct "No more games."
    mct "I'm inside Penelope."
    mct "I'm having sex with her. I’m fucking Penelope Carter."
    mct "I'm living out the fantasy of what her 180,000 followers can only dream of."
    mct "And sweet Jesus, it feels good..."
    p "*Moaning* Aaaghhh, [mc]..."
    mc "F-Fuuuck yes, this is better than I imagined..."
    p "*Giggles* Oh y-yeah? You thought about this...? Thought about fucking little old me?"
    mc "All the fucking time..."
    p "*Moaning* AAaaahhh..."
    p "Just... a little bit faster..."
    mc "Oh boy..."
    mc "Please, d-don't let me stop you..."
    p "Just... a little bit... okay...?"
    $ renpy.music.set_volume(0.15, delay=6.0, channel='music3b')
    stop soundloop fadeout 3
    scene pennysex2b with dis2
    p "AAAAAaaahhhhh... yeaaahh..." with dis12
    mc "Jesus Christ, that feels good, Penny..."
    p "Mmmmmhh... *giggles* y-yeah..."
    mc "W-Where the fuck did you learn to move like that?"
    p "L-Like what...?"
    p "I just imagine I'm... d-dancing..."
    p "J-Just that it feels... so fucking better..."
    p "*Panting* AAaahhh...."
    mc "Y-Yeaah, keep going..."
    p "*Groaning* F-Fuck, you're so fucking big, [mc]..."
    bla "You can feel Penelope's tight cavity slowly adjust to your size. Each of her movements feels extra sensitive on your dick."
    mc "Take it all..."
    p "AAaahh..."
    mc "Take it balls deep..."
    p "I c-can't... it’s t-too much..."
    mc "Try it for me, baby girl..."
    p "I..."
    p "A-Are you sure?"
    mc "Don’t you wanna ditch this tension once and for all? And feel good and r-relaxed?"
    mc "We've crossed the line already... might as well roll with it, right?"
    p "*Giggles* That's a good point..."
    mc "You'll see how good it feels..."
    p "*Moaning* Okay..."
    p "*Moaning* I'm g-gonna drop myself on you, yes...?"
    mc "Fuck yes..."
    p "O-Okay, here we go..."
    $ renpy.music.set_volume(0.1, delay=6.0, channel='music3b')
    scene pennysex3b with dis2
    p "*Moaning* OH GOD.{sc=2} OH MY FUCKING GOD.{/sc}" with dis12
    bla "Penelope lets herself drop, the weight of her body slamming you against the car with each powerful thrust."
    p "*Screaming* AAAaaahhhh, fuck THAT'S {b}HUGE{/b}..."
    mc "O-Oh Penny..."
    p "T-T-This is o-otherworldly..."
    mc "*Panting* Fuck, it really is..."
    mc "Ohhh f-fuck..."
    mc "FUUUUUCK..."with hpunch 
    p "*Panting* P-Please, please don't cummm..."
    p "Please let me cum first..."
    mc "You're asking for a lot there, Penny..."
    p "I-I need to cum so I can get rid of the... tension..."
    p "I need it..."
    p "I need to... I n-need to do this..."
    p "Please..."
    p "*Moans* AAAaaaAahh..."
    p "M-My god, this feels better with each passing second... aaaahhhh... how the fuck is this possible..."
    pause
    scene pennysex3_2b with dis15
    p "*Panting* AAAaahhh... aAAAAAahh... aaaaahhhhhh..." with dis12
    mc "Holy shit..."
    p "{sc=2}*Squeals* AAAAAAAAGHHH!{/sc}"
    mc "Oh y-yeah, good girl..."
    p "O-Oh my god, [mc], you're stretching me out so much..."
    mc "Y-You're taking it like a pro, Penny..."
    p "Ohhhhh god...."
    mc "That's it, babe, ride that dick..."
    mc "Keep riding it like that..."
    p "Oh, [mc]..."
    mc "Penny..."
    pause 
    bla "Penny’s jiggling, voluptuous body fills your every sense, as each individual bounce and thrust causes your body to radiate with a divine pleasure."with dis08
    p "*Panting* AAAah... aaaaaahhh... aaaaahhhh..."
    p "*Panting* F-Fuck, I'm getting tired, [mc]..."
    p "*Panting* B-But I don't want it to stop..."
    p "*Panting* Not when I'm this close..."
    p "*Panting* Not when it feels... t-this good..."
    mct "Maybe now that she's gotten used to it, I can let her “rest” and simply relish the pleasure..."
    mc "Now it’s my turn to ask..."
    mc "Are you ready?"
    p "*Panting* Ready... f-for what...?"
    play soundlow slam
    scene pennysex4b with vpunch
    p "{sc=2}OH MY F-FUCKING GOD...........!!!{/sc}" with dis12
    mc "OH FUCK YESSS...."with hpunch 
    p "AAAAAAHHHhh!!!"with hpunch 
    mc "This is what you wanted, didn't you...?"
    mc "You wanted me to fuck you this hard from the beginning... always teasing, always flirting..."
    p "O-Oh Lord, t-this is unbelievable..."
    mc "You wanted this, didn’t you, you naughty girl?"
    p "F-Fuck YESSSS, I did..."
    p "Fuck me hard, [mc]..."
    mc "Oh I will..."
    pause
    bla "You keep hammering Penelope's pussy, your ears drowning in her small, constant whimpers of pleasure."with dis 
    p "*Panting* I-I'm gonna cum so hard, [mc]..."
    p "*Panting* I'm almost there..."
    p "*Panting* P-Please don't s-slow down..."
    mc "I'm gonna give you the orgasm of your life..."
    mc "You’ll never forget this..."
    scene pennysex4_2b with dis15
    p "{sc=2}AAAAAAAHAHHH YEAAAAHHHH...!!!{/sc}" with dis12
    p "{sc=2}*Biting her tongue* MMMMmmMMMmhhhh!!!!{/sc}"
    mc "*Panting* O-Oh god... I knew you'd love it hard..."
    p "{sc=2}*Noises of pleasure* MmmMmmggggGGggghhh!{/sc}"
    mct "I don't think anyone could take it as roughly as she does..."
    mct "She’s a total sex freak..."
    mct "I can literally feel the tip of my cock poking the innermost parts of her."
    p "{sc=2}MmmMmmgggmmmmmh....{/sc}"
    mct "I feel so fucking powerful destroying her slender body like this..."
    p "{sc=2}AAAAaahhhh...{/sc}"
    mct "And she seems to like all of it..."
    mct "This is gonna leave a mark."
    p "{sc=2}MmmMMmmmmmh!!{/sc}"
    mc "*Panting* A-Are you gonna cum?"
    p "*Biting her tongue* Y-Y-Y-Yahh..."
    p "I'm gonna..."
    p "I'M THERE!"
    p "{sc=2}DON'T STOP!!!{/sc}"
    p "I'm..."
    p "I'M–"
    play sound2 carsuspension 
    play sound7 slap1
    play sound3 cum4
    scene fg 105
    p "{sc=2}*Orgasming* AAAAAAAAaaaAAAAAGHHHH.....!!!{/sc}" with hpunch
    bla "Penelope orgasms, soaking your cock in vaginal fluids and contracting all of her muscles at once."
    play sound4 carsuspension
    play sound5 slam volume 0.4
    play sound6 penetration2
    stop music3b fadeout 8
    play soundloop vent fadein 9 volume 0.8
    scene fg106
    bla "She faints on top of you, utterly dazed, her legs still trembling uncontrollably." with vpunch
    p "*Breathing heavily* AAaAAAaaahghh . . . . . ."
    mc "*Catching your breath* Oh, Penny..."
    mc "Fuck, that was intense."
    p "*Breathing heavily* . . ."
    mc "Got rid of all that sexual tension, eh?"
    p "*Breathing heavily* Mm-hmmm...."
    mc "Glad I could be of service..."
    mct "Man, I can't believe I just fucked Penny."
    mct "I was literally just a few seconds away from cumming too."
    mct "But I can't really ask much more of her, to be honest."
    mct "That was insane."
    p "{bt=3}{i}*Unintelligible murmurs*{/bt}"
    mc "What...?"
    p "{bt=3}{i}*Unintelligible murmurs*{/bt}"
    mc "You're gonna have to say it louder."
    p "{bt=3}{size=10}*Whispering* Break me.......{/bt}"
    mc "Eh?"
    p "{bt=3}{size=25}*Whispering* Break me please...{/bt}"
    $ renpy.music.set_volume(0.35, channel='music3')
    play music3 pennysex fadein 3
    stop soundloop fadeout 12
    show fg 107
    mc "What...?" with dis12
    scene fg 109
    mc "What did you say...?"with dis12
    show fg109
    p "I want you..."
    p "I want you to break me."
    p "I want you to fuck me again until you ruin me..."
    p "And again... and again."
    p "Grab me and use me as rough as you can... don’t give me a second or a moment to breathe..."
    p "{bt=3}*Whispering* I want you to destroy me...{/bt}"
    scene fg108
    mc "A-Are you fucking serious?"
    scene fg109
    p "C’mon... you were talking such a big game earlier, [mc]..."
    p "Split me in half..."
    scene fg108
    mc "Oh, baby..."
    menu pennysexcarr:
        with dis12
        "Fuck her in missionary" if pennylambomis:
            $ renpy.music.set_volume(0.2, delay=7.0, channel='music3')
            play sound4 carsuspension
            play sound5 slam volume 0.35
            play sound6 whoosh6 
            if pennylambo1:
                scene carmisagain with hpunch 
                p "*Panting* AAAAaaaaaaahhh..." with dis
                p "*Panting* A-A-Again...?"
                mc "*Panting* I just can't stop, Penny..."
                p "*Panting* O-O-Oh my goddd..."
                pause 
                scene pennysex6b with dis15
                p "{sc=2}AAAAAAAAHHH....{/sc}" with dis  
                p "{sc=2}SWEET LORD, [mc!u]...{/sc}"  
                mc "*Panting* FUCK YES...." 
                pause
                $ pennylambomis = False
                $ pennylambodog = True
                jump pennysexcarr
            scene fg110
            mc "*Pulling her to the front of the car* Bring that tiny waist of yours here..." with hpunch
            if not pennylambodog:
                p "*Still catching her breath from the last position* J-Jeez..."
                p "A-Aren't you even gonna let me–"
            else:
                p "Yeah..."
                p "Fill me up with your huge cock..."
                p "My body’s all yours... this pussy, this mouth, everything..."
                p "Yours..."
                mc "Now you'll see what's good..."
            scene pennysex5b with dis15
            if not pennylambodog:
                bla "You suddenly penetrate her, cutting her off."with dis12
                p "AAaaaaaaahhhh... MY G-GOD, I GUESS NOT..."
            else:
                p "AAaaaaaaahhhh... MY G-GOD, YEAHHH..." with dis12
            mc "OH FUCK..."
            p "Mmmmmmmhhh YESSSSS..."
            mc "O-Oh my god, Penny..."
            p "*Moaning* Yeah..."
            p "F-Fuck me..."
            p "Fuck me with that monster fucking cock of yours... give me what I need..."
            p "Shove every inch of it inside of me..."
            pause 
            bla "You continue to hammer her relentlessly, feeling how your dick breaks the resistance that her tight insides offer with each stroke." with dis
            p "*Moans* AAAaaaAAhh..."
            p "Oh my god, you're tearing me apart..."
            p "*Giggles* A-And I fucking love it..."
            p "Mmmmmhhh..."
            scene pennysex5_2b 
            pause 0.01
            mc "Ahhhh..."
            mc "Dear Lord, about time I get a good look at these tits of yours..."
            mc "You have no right to be this hot..."
            p "*Moaning* AAAaaahhh..."
            mc "I fucking love how your boobs bounce..."
            p "T-They're all yours... I told you, e-everything is yours..."
            p "*Moans* AAAaaaaAAaahh..."
            p "D-Do with me as you please..." 
            p "*Moaning* Just don't stop fucking me ever..."
            mc "Y-You're a fucking nympho..."
            p "*Moaning* Faster..."
            p "*Panting* Fuck me harder..."
            mc "Very well..."
            if pennyrough:
                scene pennysex6_2b with dis15
                p "AAAAAAAAHHH.... y-yeah... HIT ME!{w=3.6}{nw}" with dis12               
            else:
                scene pennysex6b with dis15
                p "AAAAAAAAHHH!!!" with dis12
            p "MmmmMMMmMmmmhhh..." with hpunch
            p "F-Fuck yeah..."
            p "Punish me..."
            p "Punish me for all the teasing..."
            p "I've been a bad girl... mmmMmmhh... all those naughty dresses... all those comments..."
            p "F-Fucking punish me..." 
            mc "AAAAAAARGHHH, fuck, PENNY..."
            mc "*Panting* AAAahhhh..."
            mc "O-Oh god, my dick's gonna be sore after this..."
            p "*Squeals* AAAAAaghhh..."
            $ pennylambo1 = True
            $ pennylambomis = False
            $ pennylambodog = True
            jump pennysexcarr
        "Fuck her from behind" if pennylambodog:
            $ renpy.music.set_volume(0.2, delay=7.0, channel='music3')
            play sound4 carsuspension
            play sound5 slam volume 0.35
            play sound6 whoosh6 
            if pennylambo2:
                scene cardogagain with hpunch 
                p "*Panting* AAAAaaaaaaahhh..." with dis
                p "*Panting* Fuck, [mc]... don't you ever run out of stamina?"
                mc "*Panting* Not with you..."
                p "*Panting* O-O-Oh my goddd..."
                p "*Panting* I need... t-to rest..."
                play sound fallfull
                play sound2 carsuspension
                play sound3 carsuspension
                scene pennycartransfall2 with vpunch 
                p "{sc=2}AAAAAAAAHHH....{/sc}" with dis 
                p "{sc=2}[mc!u]...{/sc}"     
                mc "*Panting* GGGgghhh...." 
                pause
                $ pennylambomis = True
                $ pennylambodog = False
                jump pennysexcarr
            scene fg111
            mc "*Pulling her to the side of the car* Come here..." with hpunch
            if not pennylambomis:
                p "*Still catching her breath from the last position* J-Jeez..."
                p "A-Aren't you even gonna let me–"
            else:
                mc "Your tits are the fucking best I've ever seen in my life, Penny, but goddamn, this butt of yours deserves some attention too..."
                p "*Giggles* Please, put it back inside..."
                mc "Your wish is my command..."
            scene pennysex7b with dis15
            if not pennylambomis:
                bla "You suddenly penetrate her, cutting her off."with dis12
                p "AAaaaaaaahhhh... MY G-GOD, I GUESS NOT..."
            else:
                p "MMmmmmMmmmmm... Y-YEAAAHHHHHH..." with dis12
            mc "*Panting* Oh dear Lord, y-your pussy is so fucking tight, Penny..."
            p "AAAaaaahhh..."
            p "*Panting* Hell y-yeah, that's the stuff..."
            p "*Panting* Slam it in me..."
            mc "Aaaahhh...."
            p "*Panting* Yes..."
            p "*Panting* D-Deeper..."
            p "*Panting* H-Harderrrr..."with hpunch 
            mc "*Panting* God..."
            p "*Panting* I d-don't give a shit anymore..."
            p "*Panting* I don't give a shit about consequences..."
            p "*Panting* I just want you to fuck me every day..."
            p "*Panting* J-Just take your cock and fucking give it to me..."
            p "*Panting* I want Mom and Dalia to hear me scream..."
            mc "Oh f-fuck me, don't say that or you're gonna make me cum instantly..."
            p "*Giggles* AAAAAaahaaahaaahhh..."
            scene pennysex7_2b with dis15
            p "AAAAaahhh...." with dis12
            p "*Squeals* Oh my god, you're so deep..."
            mc "D-Do you even realize we're fucking on a $400,000 car?"
            p "*Panting* F-Fuck yeah we are...."
            p "*Giggles* And that makes it so much hotter..."
            p "AaAAaaahhhhhhh..." with hpunch 
            p "Crush me against this car, [mc]..."
            p "*Giggles* L-Let's see if it breaks before I do..."
            mc "Oh yeah, Penny..."
            scene pennysex7_3b with dis15
            p "*Panting* AAAaahhh..." with dis12
            p "*Panting* I never imagined I could ever feel so filled..."
            p "*Panting* D-Don't slow down, please..."
            mct "I knew Penny had hinted she was into rough sex, but... holy fuck." 
            mct "We're rutting like fucking animals in the middle of mating season."
            mct "And she's enjoying it as much as I am."
            p "*Moans* MMMMmmmMMmmhh..."
            mct "No, she’s definitely enjoying it more..."
            scene pennysex7_2b with dis15
            p "*Moans* AAAaaaahhh..."with dis12
            p "Oh d-d-dear LORD... I can't even feel my legs anymore..."
            p "{sc=2}AAAAAAAAGHHHHH... YEAHHH...{/sc}"with hpunch 
            p "Fuck, I c-can't..." with hpunch
            play sound fallfull
            play sound2 carsuspension
            play sound3 carsuspension
            if pennyrough:
                scene pennycartransfall1 with vpunch 
            else:
                scene pennycartransfall2 with vpunch 
            bla "Penelope's legs give out, and you both tumble onto the floor."with dis
            p "{sc=2}AAAAAAAAHHH.... my GODDDDD.....!!!!{/sc}" with hpunch
            mc "F-Fuck yes..."
            mc "Y-You told me yourself that you wanted me to fuck you without giving you time to even breathe, didn't you...?"  
            p "*Squeals* AAAAAAaaaaaHHHH..."   
            if pennyrough:
                p "Y-Y-Yeaahh.... I deserve it..." 
                p "Be rough with me..."   
                p "Use me..."  
            else:
                p "Y-Y-Yeaahh...." 
                p "Keep fucking me like that..."
                p "I-It feels so good..."
            p "AAAAAAAAahhh..."with hpunch 
            p "*Panting* Fuck me..." 
            $ pennylambo2 = True
            $ pennylambomis = True
            $ pennylambodog = False
            jump pennysexcarr
        "Finish" if pennylambo1 or pennylambo2:    
            mc "I-I'm at my limit, Penny..." with dis
            p "{sc=2}*Panting* AAaaa.... aaaahhh... aaaaaahhh...{/sc}"
            mc "*Panting* I'm gonna cum..."with hpunch 
            mc "*Panting* I'M GONNA..."with hpunch
            jump valentinoendr
label valentinoendr:
    play sound doorclose2
    play sound2 slam
    play sound3 doorslam
    bla "You hear a sudden noise.{w=0.8}{nw}" with hpunch 
    play sound5 penetration2
    play sound5 carsuspension
    scene fg 112 with dis12
    mc "*Suddenly stopping* W-What was that?" with dis
    p "{bt=3}MMMmmmmmmhmmm...{/bt}"
    mc "H-Hold on... THE DOOR!"
    mc "Someone just kicked the door open!"with hpunch 
    mc "Shit, I totally forgot about where we are! We have to get out of here!"
    p "{bt=3}*Giggles* Oh nooo...{/bt}"
    mc "*Whispering* S-Shit, Penny, keep it down! We need to leave!"
    p "{bt=3}Keep fucking me...{/bt}"
    mc "*Whispering* Don't you realize that if they catch us they're gonna hit us with a massive fee for property damage?!"with hpunch
    p "{bt=3}*Giggles* I'm the damaged property here...{/bt}"
    play sound4 carsuspension
    show fg 113
    p "{bt=3}*Blowing you* Please, make me cum again...{/bt}" with dis14
    scene fg113
    p "{bt=3}*Blowing you* Pretty pretty please...?{/bt}"
    mc "G-G-Ggggghhhh... P-Pennyyy s-stay quieeeeet..."
    play sound clotheswhoosh
    play sound3 clotheswhoosh
    play sound2 curtain2
    scene fg115
    val "*Pushing aside the curtains* This is the last time I work with this shitty studio, you hear me?!" with hpunch 
    val "I couldn't even get inside! UNBELIEVABLE!"
    show fg 115b
    asp "I-I don't know what happened, Mr. Valentino, I'm so sorry!"
    asp "Someone from the cleaning staff must have forgotten to–"
    scene fg 115
    val "Don't sell me that bullshit, bitch!"
    val "Now go find my girl and tell her to start getting changed!"
    show fg 115b
    asp "Y-Yes, right away, Mr. Valentino!"
    show fg 115
    val "Then why are you still here?! Move, you fucking incompetent dog!" with hpunch
    asp "Y-Yes!"
    play sound run
    show fg 116
    val "Hmm..." with dis12
    show fg 16
    val "*Sighs* (This is what happens when you give women any kind of important job.)"
    val "(Anyway... at least the car's good to go.)"
    show fg 117 with dis14
    val "(I'm gonna get that emo bitch fired as soon as Ulysses gives us the contract.)" with dis
    play sound type1
    val "*Typing* (She'll regret having disrespected me like that...)"
    show fg 118 with dis15
    pause
    scene pennysex9b 
    show fg 119
    with dis12
    pause
    $ renpy.music.set_volume(0.1, delay=7.0, channel='music3')
    hide fg 119 with dis17
    mc "*Whispering* J-Jesus..." with dis12
    p "MMmMmMmmmmhh..."
    mct "Oh Lord..."
    mct "What the fuck is happening to me...?"
    mct "If we get caught, we're gonna get in BIG trouble."
    mct "But I just..."
    mct "Fuck, I just {b}can't{/b} seem to stop..."
    p "*Biting down on her panties with force* MMMMMGH!" with hpunch
    mct "Please, just a little bit more..."
    p "MMMMmmmmmh..."
    mct "The sounds she makes..."
    mct "The way her body feels..."
    mct "Or the way she absolutely LOVES being dominated..."
    mct "Every single thing about Penny just makes me want to turn into an animal and unleash my primal instincts."
    p "MMMMMmmmmmHHHHH..."
    mct "She not only managed to keep up with my rhythm, but she relished every single second of it..."
    mct "If I hadn't put her panties in her mouth, her moans would have revealed us already."
    p "MMMmmmmMmMmmmhh..."
    mct "We need to leave..."
    p "{sc=2}MMMMMMMHHHHHHhhh...{/sc}"
    mc "But I NEED to cum first..."
    p "{sc=2}MMMMMMMMMmmmMMHHHHmHHhhh...{/sc}" 
    mc "I'm finally almost there..."
    mc "My balls are about to explode..."
    p "{sc=2}MMMMMmmmmMMMMmmmMMHHHHmmHHhhh...{/sc}" with hpunch
    mc "I'm..."
    menu:
        with dis
        "Cum inside":
            $ renpy.music.set_volume(0.16, delay=10.0, channel='music3')
            $ pennycreampie = True
            play sound3 penetration2
            scene fg 120 with dis
            pause .2
            play sound5 cumall
            play sound4 slap1
            scene fg 121
            mc "*Trying to repress your groans* AAAAAAaaaaahhh..." with hpunch 
            play sound3 penetration2
            scene fg 120 with dis
            play sound5 cumall
            play sound4 slap1
            scene fg 121
            mc "AAaaaaahhh..." with hpunch
            play sound3 penetration2
            scene fg 120 with dis
            play sound5 cumall
            play sound4 slap1
            scene fg 121
            mc "AAaaaaaaAAAAaaaaaaaahhhhh..." with hpunch
            mc "F-Fuuuuuuck..."
            scene fg 122
            bla "You can feel how Penelope orgasms again at the same time as you finish unloading an insane amount of jizz deep inside her warm vagina." with dis15
            mc "*Whispering* Take it all..."
            play sound penetration2
            play sound2 penetration3
            scene fg 123 with dis17
            mc "*Whispering* Oh, Penny..." with dis
            scene fg 124
            mc "That was..." with dis14
            mc "Glorious..."
        "Cum outside":
            $ renpy.music.set_volume(0.16, delay=10.0, channel='music3')
            play sound rubbody
            play sound2 fall2
            scene fg 125 with dis12
            mc "FUCK, COME HERE..." with dis
            mc "I wanna turn your beautiful body into a fucking mess..."
            play sound5 cumall
            play sound6 bodycollide
            scene fg 126
            mc "*Trying to repress your groans* AAAAAAaaaaahhh..." with hpunch 
            play sound3 penetration2
            scene fg 127 with dis
            play sound5 cumall
            play sound4 bodycollide
            scene fg 128
            mc "AAaaaaahhh..." with hpunch
            play sound3 penetration2
            scene fg 129 with dis
            play sound5 cumall
            play sound4 bodycollide
            scene fg 130
            mc "AAaaaaaaAAAAaaaaaaaahhhhh..." with hpunch
            mc "F-Fuuuuuuck..."
    play sound ["<silence 0.3>", fallfull] volume 0.6
    stop music3 fadeout 12
    play soundloop vent fadein 12
    if pennycreampie:
        scene pennysex10 with dis12
    else:
        scene pennysex10_2 with dis12
    bla "As you take a step back, Penelope's legs finally surrender and she crumples onto the floor, completely spent." with dis
    mc "*Panting* Oh god, Penny..."
    p "{bt=3}*Panting* Gggg-gG-gg-gggghhh...{/bt}"
    mc "W-What?"
    p "{bt=3}*Panting* AAAAaaaagahhhgh...{/bt}"
    mct "I-I’d better give her a minute."
    scene fg 131
    val "Hmm?" with dis12
    show fg 132
    val "(What the hell was that noise?)"with dis12
    val "Hello??"
    val "Is there anyone there?"
    if pennycreampie:
        show pennysex10
    else:
        show pennysex10_2
    mc "*Whispering* F-Fuck! He heard us!"
    mc "*Whispering* Shit, shit shit... Penny, we've gotta get out of here!"
    p "{bt=3}*Panting* AAAAaahhhgghgh....{/bt}"
    p "{bt=3}*Panting* I f-feel like I juust got r-rammed by arr bull...{/bt}"
    p "{bt=3}*Giggles* A bull...{/bt}"
    mc "*Whispering* Penny, focus!" with hpunch 
    mc "*Whispering* Snap out of it!"
    val "ASPEN?? Is that you?"
    mc "*Whispering* PENNY! HE'S COMING THIS WAY!" with hpunch 
    mc "*Whispering* I NEED YOU TO STAND UP!"
    mc "*Whispering* I CAN'T CARRY YOU AWAY LIKE A POTATO SACK!"
    p "{bt=3}*Giggles* Hahahahhgaa...{/bt}"
    p "{bt=3}*Panting* Potato...{/bt}"
    mc "*Whispering* Goddammit!" with hpunch 
    scene fg 133 with dis2
    pause 
    play sound risingshortb fadein 1
    pause .6
    play sound2 debris3
    show fg 134 with dissolve
    pause
    play music quirky7 fadein 8
    show fg 135
    val "Hmph." with dis12
    val "(There's no one here.)"
    val "(Maybe something toppled from the scaffolding.)"
    show fg 134
    val "(This place is filthy as fuck, though.)"
    val "(I swear, this is the last gig with this studio.)"
    play sound lightstage
    show fg 136
    pause
    show fg 137
    val "*Sniffs* (And seriously, what the fuck is this stench?)" with dis12
    val "(Smells like the Lamborghini...)"
    val "(It seems... kinda familiar, but I can't quite put my finger on it.)"
    val "(Perhaps our cleaning crews are using the same cleaning supplies?)"
    scene fg 138 with dis22
    pause
    show fg 139 with dis2
    pause
    play soundlow wood2
    show fg 140 with dis2
    pause 
    play sound2 whoosh6
    play sound run
    scene fg 141
    show mcpotato with hpunch
    pause 
    $ renpy.end_replay()


label ga_luna2:
    $ renpy.music.set_volume(0.8, channel='music3')
    play music3 ["<silence 0.8>"]
    queue music3 lunasex1 fadein 2
    play sound debris3
    stop soundloop fadeout 11
    scene fl 100
    bla "Luna leans in quickly and catches your lips with a sudden kiss." with dis12
    mct "W-What?"
    mct "How..."
    mct "Why..."
    mct "I don't..."
    play sound hay
    play sound2 debris3
    scene fl 101
    bla "Your thoughts and concerns fade as you eagerly return the kiss, drawing closer to Luna." with dis14
    mct "Fuck it..."
    l "Mmmm..."
    play sound2 footsteps
    scene fl 102 with dis17
    bla "Without breaking the kiss, you effortlessly lift Luna from the floor, carrying her towards the nearby barrels." with dis
    l "Mmmmhh..."
    play soundlow woodhit
    scene fl 103
    mc "*Dropping her on top of the barrels* Wow..." with dis12
    mc "That sure was unexpected."
    show fl 105
    l "I'm sorry, I just had a–"
    show fl 103
    mc "Oh, don't you dare apologize!"
    mc "That was amazing."
    mc "I just didn't expect you to take the lead, it caught me off guard."
    show fl 104
    l "I just felt like I wanted to do it."
    l "So... I did it."
    l "You told me I had to open myself to you and be the real me from now on, so..."
    show fl 103
    mc "Ahh, I dig that."
    mc "Anything else you want to share with me, miss?"
    mc "What made you want to kiss me so bad?"
    show fl 104
    l "*Giggles playfully* Well..."
    l "I guess your words got me."
    l "You're always caring, funny, confident, intelligent, and you share my quirky hobbies."
    l "Being with you is simply... fun."
    show fl 105
    l "And, uh, you're also... handsome. And... like..."
    l "S-Super hot."
    l "You're s-so... fit."
    show fl 103
    mc "Oh, yeah?"
    l "Mm-hm."
    mc "Well, since we're sharing feelings here..."
    mc "Gotta say, every word I said before stands true. You're kind, genuine, clever, and I love your humor."
    mc "But, let me also add... you're also incredibly hot, Luna."
    mc "Your body, your face, and your eyes – they're simply irresistible."
    show fl 104
    l "T-Thank you..."
    show fl 105
    l "And oh, I forgot!"
    l "I also like that I can touch you with my hands without getting visions."
    l "It makes me feel more... connected to you."
    show fl 103
    mc "You should take off those gloves, then."
    mc "You can touch all you want."
    show fl 104
    l "*Giggles* Okay..."
    play sound untie
    show fl 106
    bla "Luna begins untying the laces of her gloves." with dis15
    play sound2 clothes3
    scene fl 107
    l "*Breathing nervously* . . ." with dis15
    mc "*Chuckles* So?"
    mc "You're scared to touch now?"
    show fl 108
    l "I'm not!"
    l "I mean..."
    l "With anyone else, I might be. But... not with you."
    show fl 107
    mc "Hmm, I don't know, you look pretty scared to me."
    mc "You might have to convince me otherwise."
    show fl 109 with dis12
    mc "Ah, I see..." with dis
    mc "Is that all, though?"
    play sound2 clothes3
    scene fl 110
    bla "Luna's fingers trace a path up your chest, reaching toward the back of your head, where she cups your neck with a gentle embrace." with Dissolve(1.9)
    play sound rubbody
    play sound3 wood volume 0.4 fadein 1
    scene fl 111
    l "{sc=2}*Twitching* MMmm-m-m-mmmmhh......{/sc}" with dis12
    mc "L-Luna? You okay?"
    l "*Purring like a cat* Mmmmrr-mhhh-hmm."
    l "Y-Your skin is so warm."
    mc "Oh."
    l "It feels... good."
    l "T-Touching someone else, I mean."
    scene fl 112
    l "Will I ever get used to this feeling?" with dis08
    mc "Through enough practice? I'm sure of it."
    mc "But it'll never stop feeling good, don't worry."
    play sound chair3
    scene fl 113
    bla "Luna leaps back into your arms, initiating another passionate kiss. Her fingers eagerly weave through your hair, tracing the lines of your neck with tender caresses." with dis12
    mct "Oh, man..."
    mct "I never thought I'd see Luna acting so passionately."
    mct "And I fucking love it."
    play sound rubbody
    play soundlow chair2
    scene fl 114
    l "*Putting her feet back onto the ground* MMmmmmmmhh..." with dis15
    mct "I love how she can't keep her hands on a single place."
    mct "As if she wanted to map every inch of me."
    scene fl 115
    mct "And the way she molds her body to mine, refusing to release her grip..." with dis15
    mct "God, she turns me on so much."
    play sound2 wood volume 0.4
    scene fl 116
    l "*Leaning forward* Mmmmmh..."with dis14
    mct "Oh shit, please don't–"
    play sound rubbody
    scene fl 117
    l "*Leaning back* Mmmmh?" with dis
    mc "Um... s-sorry, I..."
    mc "I got too excited."
    show fl 118
    l "Is that..."
    show fl 119
    mc "...Yes."
    mc "Sorry."
    show fl 118
    l "No, no, it's okay."
    l "I just... wasn't expecting it."
    show fl 119
    mc "Yeah..."
    mct "This is awkward."
    mc "Um..."
    mc "If you give me one minute..."
    l ". . ."
    l "Hmm."
    mc "You okay?"
    play sound clothes
    scene fl 120
    bla "Luna lowers herself to her knees, moving with such deliberate slowness that it feels as if time itself is moving in slow motion." with dis25
    mct "W-What is going on...?"
    mc "L-Luna?"
    l "Do you want me to..."
    l "Help you...?"
    mc "Wha..."
    scene fl 122
    mc "W-What did you just say?" with dis15
    scene fl 121
    l "If you want to."
    scene fl 122
    mc "I..."
    mc "I mean..."
    mc "I-I would like to, yeah."
    mct "Jesus Christ, just seeing Luna in this position, speaking like that... I can feel the blood rushing to my cock."
    mc "Are you sure, though?"
    show fl 121
    l "Yeah."
    l "I want to do it."
    show fl 123
    l "*Giggles playfully* I mean, I was about to do it anyway at my uncle's place, right after your... massage."
    l "I would probably have done it already if my dad hadn't interrupted."
    l "I guess I owe it to you."
    show fl 122
    mc "So you really wanted to do that right before you left the terrace! I thought it was all in my head."
    show fl 123
    l "*Giggles* I suppose that now that I promised you to be completely transparent, I can't keep secrets from you anymore."
    show fl 122
    mc "Well, if I can be sincere too, I will admit that right now you're driving me wild down there..."
    show fl 121
    l "Let me lend a hand, then."
    l "Let me... help you feel good."
    l "Like you helped me."
    play sound clothes3
    play sound2 ["<silence 1>", zip] volume 0.4
    scene fl 124
    mc "*Reaching for your zipper* Oh man..." with dis15
    mc "Very well, then..."
    play sound3 clothes3
    play sound4 clothes4
    scene fl 125 with dis2
    l ". . ." with dis
    mc "Ahh, much better..."
    l "Wh..."
    l "W-Wow."
    show fl 126
    mc "All good?"
    show fl 125
    l "I mean... y-yeah."
    l "I guess."
    l "I..."
    l "I wasn't sure of what to expect, but... wow."
    l "H-How can you keep all that inside your pants...?"
    l "Aren’t you in swimming class?! How do you hide it in your trunks?!"
    show fl 126
    mc "Well... I'm usually not this... excited."
    show fl 125
    l "Ah."
    l "Yeah."
    l "That... makes sense."
    l ". . ."
    l "Can I... touch it?"
    mc "Of course... I thought that was the whole point."
    scene fl 127
    l "Ah... y-yeah... of course."with dis15
    l "Sorry, I'm a bit jittery."
    mc "No need to be, Luna."
    mc "There's literally nothing you could do that would be wrong."
    scene fl 128
    l "That's... reassuring." with dis15
    scene uefuefneubf
    bla "Luna playfully trails her fingers along, mimicking tiny legs as they saunter up to your manhood."with dis2
    l "Hmm..."
    mc "Now grab it..."
    play sound rubbody
    play sound2 ["<silence 0.3>", bodycollide]
    play sound3 ["<silence 0.3>", bodycollide]
    scene nvruiwoqww
    l "{sc=2}*Twitching* M-M-Mmm-m-m-mmmhh . . . . . .{/sc}" with dis
    mc "O-Ohhh god..."
    mct "I fucking love the way she twitches each time she touches me with her bare hands..."
    scene fl 131
    l "*Pulling herself together* Mmmh..."with dis
    mc "Y-You okay?"
    l "Mm-hm..."
    play soundlow wood2 fadein 1
    play sound2 clothes3
    $ renpy.music.set_volume(0.6, delay=7.0, channel='music3')
    scene lunah1 with dis22
    bla "Luna draws near, so close that your dick nearly reaches her face, her touch moving in a teasingly slow, deliberate motion." with dis12
    mc "O-Ohh my fucking god, yes..."
    l "It's so... warm..."
    l "So hard..."
    l "I can feel it... on my hand!"
    l "*Giggles playfully* It's pulsing!"
    mc "Y-Yeah..."
    mct "Oh dear, she's so close..."
    mct "My cock is literally skimming her lips."
    l "I didn't know giving “massages” could be as fun as receiving them."
    mc "R-Right?"
    l "Yeah..."
    mc "Aahh..."
    mc "Y-You know, maybe..."
    mc "You should take those clothes off, Luna...?"
    l "My... clothes?"
    l "What for?"
    mc "Well..."
    mc "Now I could probably come up with some silly excuse, but I value this newfound honesty policy between us."
    mc "The truth is, I just want to see you naked again so fucking badly."
    l "*Giggles* Ah, I see..."
    play soundlow wood2
    play sound2 clothes3
    play sound3 belt
    scene fl 133 with dis12
    bla "Luna sidles away, her playful smirk lingering as she begins to unfasten her hunter corset." with dis
    mct "Fuck yes..."
    play sound5 clothes
    stop sound3 fadeout 1
    scene fl 134 with dis17
    bla "She slips out of the leather corset, unveiling a tight black shirt that perfectly contours her slender figure." with dis12
    mc "That shirt looks good on you... although it doesn't seem very breathable."
    show fl 135
    l "Yeah... it really isn't."
    l "It almost feels like a thermal t-shirt."
    l "Good for hunting demons, but perhaps not so much for... alternative activities."
    l "It was actually making me sweat a bit."
    show fl 134
    mc "So I could actually have come up with an excuse after all."
    mc "What a wasted opportunity."
    l "*Snorts* Mm-hm."
    play sound clothes3
    scene fl 136 with dis17
    pause
    play sound5 buttons volume 0.4
    play sound2 clothes3
    play sound3 clothes
    scene fl 137 with dis2
    bla "Luna slips off her shirt, revealing, indeed, faint traces of sweat on her porcelain skin." with dis
    mc "Jesus fucking Christ..."
    show fl 138
    mc "Simply... wow." with dis12
    mc "I had forgotten how perfectly shaped your tits were."
    play soundlow wood
    scene fl 140
    l "*Standing up* Oh, please." with dis12
    scene fl 139
    mc "I'm serious."
    mc "I mean... just look at you!"
    mc "So... oof."
    scene fl 140
    l "*Giggles* Stop giving me that smirk!"
    l "*Giggles* It makes me jittery!"
    show fl 139
    mc "I can't help it."
    mc "Topless Luna Hernandez and the silly smirk on my face go together."
    mc "It's a reflex."
    play soundlow wood
    play sound clothes3
    scene fl 141
    bla "Luna strides towards you with surprising confidence, pressing your dick against her belly." with dis14
    play sound2 clothes2
    show fl 142
    l "*Lifting your face mask up* Hmm." with dis
    mc "*Chuckles* Ahh, fair enough."
    play sound3 wood fadein 1
    $ renpy.music.set_volume(0.45, delay=7.0, channel='music3')
    play soundloop handjobslow fadein 4 volume 0.2
    scene lunah2 with dis22
    bla "Luna gracefully kneels down before you and starts jacking you off again." with dis
    mc "Ohhh yeah, babe..."
    mct "Oh my god, her face is so close again..."
    mct "I wanna put my cock inside her little cute mouth so bad..."
    mct "I {i}need{/i} to."
    mct "Should I try it? Or at least... ask?"
    mct "I mean, it's Luna we're talking about, I already can't believe she's doing what she's doing."
    mct "Although... I bet she's yearning for physical contact. She's been missing it all her life because of her condition."
    l "Am I doing it right...?"
    mc "Fucking perfect."
    mct "Maybe..."
    mc "Are you sure you don't wanna take off your pants too, though?"
    l "My pants?"
    l "Is it because you're concerned about me sweating or because you want to see more of me...?"
    mc "Why not both?"
    l "Hah."
    l "Okay..."
    l "I guess I can do that..."
    mc "Fuck yes..."
    stop soundloop fadeout 1
    play sound footsteps
    scene fl 144 with dis15
    play sound chair2
    mc "*Sitting on a nearby box* Please, don't mind me." with dis
    mc "I'm just getting a better seat for the show."
    show fl 145
    l "*Playfully giggles* You're so silly, you know that?" with dis12
    mc "A silly, but happy man."
    show fl 146
    l "*Unfastening her belts* Ah, that usually goes together, you're right..."with dis12
    play sound beltdrop
    show fl 147 with dis12
    pause
    play sound2 clothes5 volume 0.4
    show fl 148 with dis17
    mct "Oh wow, she's wearing a thong!" with dis
    mct "And oh god, that body..."
    mc "Please, come back here, Luna."
    mc "I need it."
    mc "NOW."
    scene fl 149
    l "I haven't even fully taken off my pants yet!" with dis 
    show fl 150
    mc "There's no need."
    mc "It's sexier this way."
    show fl 151
    mc "You're not gonna leave me hanging now, are you?" with dis
    l "*Giggles* You're lucky I'm so nice. The kindest soul some people have ever met, I hear..."
    mc "*Chuckles* Lucky me indeed..."
    mct "I adore seeing Luna at ease, playing along."
    play sound clothes
    scene fl 152 with dis2
    bla "Luna elegantly walks towards you and crouches between your legs." with dis
    mc "That's right..."
    play soundloop handjobslow fadein 4 volume 0.16
    scene lunah3 with dis22
    mc "Aaahh, yeah, that's it..." with dis
    mc "*Meticulously examining every inch of Luna's naked body* (Jesus, she's fucking breathtaking.)"
    mct "And she's entirely for me and me alone..."
    mc "Aaahh, yes..."
    mc "Are you still having fun being on the giving side?"
    l "Mm-hm."
    l "I feel so..."
    mc "Horny?"
    l "*Giggles* Y-Yes."
    mc "Are you enjoying the feeling of running your hands along my cock?"
    l "I am..."
    l "It... t-turns me on."
    l "Caressing your... big... t-thing."
    mc "*Chuckles* (She's just as cute and innocent as she looks.)"
    l "I-I'm sorry, I never talked about sex with my family, s-so... saying gross stuff out loud still feels a bit... embarrassing."
    mc "Don't worry, you can ask me whatever you want."
    mc "We can explore whatever you want... together."
    l "I'd like that..."
    menu:
        with dis
        "Let her continue":
            mct "As much as I'd like to push her a little further, I can't ask her for much more."with dissolve
            mct "She's already way out of her comfort zone."
            l "*Slight moan* Mmmm..."
            mct "She's obviously so turned on, though."
            mct "Maybe it's my turn to give something in return..."
        "Ask her for a blowjob":
            $ lunablowjob = True
            mc "Agh... I can't bear the teasing anymore, Luna..." with dissolve
            mc "Do you think you could... maybe... use your mouth?"
            scene lunah4 with dis22
            bla "Luna moves her face even closer and starts giving you small kisses on the tip of your shaft." with dis
            mc "O-o-oohhh, Jesus, now that level of teasing is just pure evil..."
            l "There's no way I can fit your huge... {i}c-cock{/i} inside my mouth, [mc]."
            l "It’s too big for me, I think..."
            mct "She said “cock”!"
            mc "Not even the tip?"
            mc "I'm sure you can do it..."
            l ". . ."
            l "It's too big..."
            mct "Maybe she needs a little more time..."
            l "*Slight moan* Mmmm..."
            mc "Well, in that case..."
    play sound chair2
    play sound2 clothes3
    stop soundloop fadeout 1
    scene fl 153
    bla "You suddenly stand up and lift Luna off the floor." with dis12     
    l "U-uh?"
    mc "You're horny as fuck, aren't you?"   
    l ". . ."
    l "*Whispering* Yes..."
    mc "Do you want me to take care of you too?"
    mc "We can have fun together."
    l ". . ."
    mc "You don’t have to be shy here... it’s just you and me."
    mc "Just open up and say what's on your mind, like we talked about before!"
    mc "There are no taboo topics with me, no bad questions."
    l "I know..."
    mc "You want me to play with your pussy, don't you, naughty girl?"
    l ". . ."
    mc "You want me to make you cum, like I did last time? Making you all breathless and dazed...?"
    l ". . ."
    scene fl153
    l "*Nods*"
    play sound clothes3
    play sound2 clothes3 fadein 1
    play sound7 wood2 fadein 1
    scene fl 155
    mc "Good girl..." with dis14
    l "*Moans* AAAaaaahh..."
    bla "You start caressing Luna's lips through her underwear's thin fabric, as she instinctively closes her legs."
    mc "You're so wet..."
    l "AAahh..."
    mc "Do you want me to stop...?"
    l "N-NO..."
    play sound whoosh6
    play soundlow clotheswhoosh
    scene fl155
    pause .15
    play sound2 ["<silence 0.5>", beltdrop]
    play sound3 bootsdrop
    scene fl 157
    mc "*Lifting Luna so fast her boots slip off* How about we make ourselves a bit more comfortable then?"with dis08
    show fl 158
    l "W-Wow, you're so strong."
    l "Um... more comfortable, y-yeah, sure."
    l "That sounds... good."
    play sound clothes2
    play sound2 clotheswhoosh
    scene fl 158b
    bla "You remove Luna's trousers entirely and toss them across the room." with hpunch
    play sound3 chair3
    play soundlow whoosh6
    scene fl 159
    mc "*Sitting down* Better, isn't it?" with vpunch 
    show fl 160
    l "Y-Your..."
    l "I mean..."
    l "Your..."
    l "Y-Your {i}thing{/i} is so close to my..."
    show fl 159
    mc "We've done this before."
    show fl 160
    l "Y-Yeah, but last time you weren't naked."
    show fl 159
    mc "Just relax."
    show fl 160
    l "O-Okay."
    l "Relax."
    l "I can do that."
    play sound rubbody 
    scene fl 161 with dis17
    play sound2 penetration2 volume 0.4
    bla "You gently move your hand towards Luna's already soaking wet pussy and slowly insert two fingers inside of her." with dis12
    scene fl 163
    l "*Moaning* Ooooooohhh my god, [mc]..." with dis15
    l "T-That... felt... good..."
    show fl 164
    bla "As you continue softly massaging Luna's insides, she gradually guides her right hand towards your dick, brushing it with her fingertips." with dis17
    play sound2 rubbody
    play sound3 bodycollide
    scene fl 165
    l "{sc=2}*Twitching* MMmm-m-m-m-mmmmhh......{/sc}" with dis12
    mct "Wow, even her vagina contracts when she twitches like that!"
    l "W-Whoa..."
    l "K-Keep going, please..."
    mc "With pleasure..."
    $ renpy.music.set_volume(0.3, delay=7.0, channel='music3')
    play soundloop wetting3 fadein 3
    scene lunah5 with dis22
    l "AAAAaaaaahhhhh..." with dis
    l "O-Oh my GOD!"
    l "*Moaning* I had f-forgotten... h-how amazing this feels..."
    mct "God, I love her so much."
    l "*Moans* AAaahh..."
    mct "There's something about Luna..."
    mct "I don't know if it's her always sweet, neutral tone of voice, or her always gentle, reserved attitude."
    mct "But seeing her letting out these loud moans... it drives me absolutely wild."
    l "*Moans* Oh f-fuck, [mc]..."
    if lunablowjob:
        mc "Fuck?! That’s the second bad word out of your mouth tonight, Luna."
    else:
        mc "Fuck?! An elegant lady like you shouldn't use such foul language, Luna."
    mc "Bad girl..."
    l "*Giggles* Aaa-ahaahh... y-yeah..."
    l "*Moans* S-Sorry..."
    mct "I wonder if using her hands to touch me while being fingered also increases her pleasure."
    mct "Literally all she's experiencing now must feel like a new world to her."
    l "AAaahhh..."
    l "F-Faster..."
    mc "Huh...?"
    l "G-Go... faster..."
    mc "Hah..."
    mc "You'll see now..."
    $ renpy.music.set_volume(0.2, delay=7.0, channel='music3')
    play soundloop2 wetting4 fadein 3
    stop soundloop fadeout 3
    scene lunah6 with dis22
    l "*Squeals* AAAAAAAaaahhh y-yeah! YEAH!"with dis
    l "*Moans* MMMmmmmMmmmhh..."
    l "*Panting* Oh Dios mio, [mc]..."
    mct "OH FUCK YES, her voice can't be sexier when she speaks in Spanish..."
    l "*Moans* K-K-Keep this p-pace, p-please..."
    mc "I won't slow down one bit..."
    mct "Jesus, she's so fucking tight."
    mct "I can't help but imagine the sensation of penetrating Luna."
    mct "I imagine it has to be an experience bordering on the mystical..."
    l "*Squeals* AAAAaaaaahhh..."
    l "*Moans* D-Diosss..."
    mct "Just seeing the way she squirms at the slightest touch..."
    mct "She's simply craving serious physical closeness."
    mct "And oh boy, I will be there to give her all the affection she needs..."
    l "*Moans* Ooooooohhh my goddd...."
    l "*Moans* I t-think..."
    l "*Moans* I-I think I'm g-gonna come..."
    l "*Moans* I can feel it coming..."
    l "*Squeals* AAAAAaaaaahhHH!"
    mct "Man, she's so fucking hot..."
    l "*Moans intensely* AAAAaaaaaAAAaahhh..."
    mct "I wanna make her scream."
    mct "I wanna make her writhe in pleasure."
    mct "I wanna make her cum over and over again..."
    l "[mc], I'm c-coming...!"
    mc "Me too, Luna, I'm almost there..."
    l "AAaahh..."
    l "AAAAAAaAaaghh..."with hpunch
    l "AAAAAAAAAAAAAAAHHHHHH..."with hpunch
    $ renpy.music.set_volume(0.4, delay=8.0, channel='music3')
    stop soundloop2
    play sound2 punch volume 0.3
    play sound3 cum4
    scene fl 166
    l "{sc=2}*Orgasming* MMMMMMmmMMMmmMmMmmmm.......!!!{/sc}" with hpunch
    play sound4 cum4
    l "{sc=2}*Orgasming* MmmmmhhmmmmMMMmMmmm......{/sc}" with hpunch
    play sound5 cum4
    l "{sc=2}*Orgasming* MmmMMMMHHHhhmmMMMmMmmm......{/sc}" with hpunch
    mct "W-Wow, that felt intense."
    play sound wood2
    scene fl 167 with dis2
    play sound2 woodhit
    bla "Luna struggles to rise, managing to crawl for a few feet before succumbing to the floor in exhaustion." with vpunch
    l "*Panting* Wow..."
    l "T-This was even more... vigorous than the first massage."
    mc "And it will only get more intense from this point."
    l "I'm not sure if I'd be able to stand it..."
    mc "Oh, I'm sure you would..."
    play sound ["<silence 0.6>", hay]
    play sound2 chair2
    show fl 168
    mc "*Sitting on the haystack* (Awh man, I was so close to finishing.)" with dis12
    mc "(Just a few more seconds and I would–)"
    play soundlow wood2 fadein 1
    scene fl 169
    mc "H-Huh...?" with dis15
    mc "Luna...?"
    show fl 170
    l "You didn't... finish."
    show fl 169
    mc "Eh... no."
    mc "I was about to, but–"
    play sound2 rubbody
    play sound wood2 fadein 1 volume 0.6
    play sound3 ["<silence 0.4>", bodycollide]
    scene fl 171
    bla "Luna suddenly straightens up and firmly grasps your member with both of her delicate hands. A fierce look of determination flashes across her face." with dis12
    mc "O-Oh Lord..."
    $ renpy.music.set_volume(0.2, delay=9.0, channel='music3')
    play soundloop wetting6 fadein 3
    scene lunah7 with dis22
    mc "O-O-Ohhh god, Luna..." with dis
    mc "Oh, f-fuck yes..."
    l "I want you to finish too..."
    l "I want you to feel... as good as I did."
    l "I want you to teach me... how to give you pleasure."
    mc "Oh babe..."
    mc "You've got the perfect touch..."
    l "I-It feels so... enormous between my hands."
    mc "You're handling it just right..."
    l "*Giggles* Thank you."
    mc "Aahhh..."
    mct "I swear, I can't resist when she looks at me with this angelic expression of hers."
    l "Like this...?"
    mc "Y-Yeah, keep doing what you're doing..."
    if lunablowjob:
        mc "*Looking at Luna's lips* (Man, this is becoming unbearable...)"
        mct "I-I know she said no, but–"
        play sound2 rubbody
        play sound wood2 fadein 1 volume 0.6
        stop soundloop fadeout 1
        scene fl 172 with dis15
        bla "Almost as if sensing your thoughts, Luna slouches down again and starts licking your shaft." with dis
        mc "G-Goodness gracious..."
        l "*Whispering* This is what you wanted, right...?"
        mc "FUCK YES..."
        mc "Please..."
        mc "Do it..."
        play sound2 ["<silence 0.25>", blow5]
        scene fl 173
        bla "Luna slides her lips over the tip of your dick. You can feel her throat gradually accommodating, overcoming a few reflexes along the way." with dis17
        mc "OOOOOOOhhhhh YES, f-finally..."
        play sound3 blowpop volume 0.5
        scene fl 174 with dis17
        l "*Giggles* Hah..." with dis08
        l "Turns out it could fit in after all..."
        mc "Told you..."
        mc "Now put it back in..."
        play sound2 ["<silence 0.25>", blow5]
        scene fl 173
        l "Mmmmm..." with dis17
        mc "YES..."
        mc "Use your hands too..."
        play sound debris
        play soundloop blowjob2 fadein 3
        scene lunah9 with dis22
        mc "O-O-OOOoooohhh Luna..." with dis
        mc "Exactly like this, yeah..."
        l "*Moans* Mmmmm..."
        mct "At last..."
        mct "My cock is inside Luna's mouth..."
        mct "I can feel her warmth..."
        mct "Her tongue sliding under my cock..."
        mct "And fuck me, it feels as good as I imagined..."
        l "*Gagging* Mmmmm..."
        mc "T-This feels unbelievable..."
        l "Mm-hmmm..."
        pause 
        bla "As Luna finds her own rhythm, she grows increasingly confident with each passing moment, embracing and savoring every second of the new experience." with dis 
        mc "AAAAAahh..."
        mc "Good girl..."
        play sound debris
        play sound2 fallhay
        play soundloop2 blowjob2 fadein 3
        play soundloop3 blowjob2 fadein 3
        stop soundloop fadeout 3
        scene lunah10 with dis2
        bla "You sit back onto the haystack as Luna, undeterred, continues sucking you off, taking your dick even deeper into her tight throat." with dis 
        mc "{sc=2}F-FUUUUUCK...{/sc}"
        mc "LUNA..."
        mc "Oh sweet Lord, y-you're a natural..."
        l "Mmmmm..."
        mct "In the end it will be true what they say about innocent-looking girls..."
        mct "They end up being the freakiest in bed..."
        mc "AAAAaaah, fuck yes..."
        l "*Pressing her hands tight against your body* MMMMmmmmmhh..."
        mct "I can sense it in the way she moans."
        mct "I can see it written all over her face."
        mct "Those innocent features, now twisted by desire... and corrupted by lust."
        mc "J-Jesus fucking Christ, Luna..."
        mc "You're something else..."
        mc "I told you that you could do it, didn't I...?"
        l "MMmmmMm–"
        stop soundloop2 fadeout 1
        stop soundloop3 fadeout 1
        play soundloop wetting6 fadein 2
        play soundloop4 wetting6 fadein 2
        play sound blow4
        play sound2 blow5
        scene lunah8b
        l "*Stopping to recover her breath* AAAaAAAAHHh..." with dis12
        l "*Panting* Y-Yes, yyyyou..."
        mc "T-Take your time, get your breath back..."
        l "*Recovering her breath* W-Wow..."
        l "*Recovering her breath* Y-Yes..."
        l "*Recovering her breath* Yes, y-you did say I could do it."
        l "*Recovering her breath* And I could! I got all of your... d-dick inside my mouth."
        mc "I-I'm sure you're capable of much more than you think..."
        l "*Recovering her breath* Hah... maybe you're right..."
        mct "Even as she struggled for breath, her gaze remained locked on my face. Her hands shuffled back and forth between my cock and her own body."
        mct "This is it, she can't get more uninhibited than she is right now."
        mct "Every barrier she had was completely replaced by the rush of hormones and raw desire."
        mct "Is it wrong that I feel proud about being the one who brought her to this state...?"
        l "I'm ready... to continue..."
        mc "Don't let me stop you..."
        play sound blow5
        stop soundloop fadeout 3
        stop soundloop4 fadeout 3
        play soundloop2 blowjob2 fadein 3
        play soundloop3 blowjob2 fadein 3
        scene lunah10 with dis22
        bla "Luna hungrily takes your dick inside her mouth again, enthusiastically continuing to suck it." with dis
        mc "Fuck yes, that's it..."
        l "Mmmmm..."
        mc "AAaaaaah..."
        mc "Fuck, Luna, I'm gonna cum..."
        play sound2 ["<silence 0.2>", debris]
        stop soundloop2 fadeout 3
        stop soundloop3 fadeout 3
        play soundloop blowjob2faster fadein 3
        play soundloop4 blowjob2faster fadein 3
        scene lunah11 with dis22
        bla "Determined to give you as much pleasure as possible, Luna hastens her pace, surpassing your expectations with a deliciously unanticipated speed." with dis 
        mc "O-O-Ooohhh my fucking god..."
        mc "F-Fuck, Luna, I'm g-gonna cum so much..."
        l "*Gagging* MMMmmmM..."
        mc "I'm almost there... don't stop now..."
        mc "K-Keep that pace..."
        l "*Gagging* MMMmmmmh..."
        mc "Milk that cock, babe..."
        mc "Milk it till it's fucking dry..."
        l "*Gagging* MMMmmmMmmmmhhh......"
        mc "Look at me..."
        mc "That's it..."
        mc "Look at me while you choke on my cock..."
        l "*Gagging* MMMmmmmh..."
        menu cumminglunaatticr:
            with dis
            "Cum on her":
                mc "Shit, I'm almost..." with dis06
                mc "I'm cumming!" with hpunch 
                if lunablowjob:
                    play sound blow4
                    play sound2 blow5
                    stop soundloop fadeout 2
                    stop soundloop4 fadeout 2
                else:
                    play sound rubbody
                    stop soundloop2 fadeout 2
                    stop soundloop3 fadeout 2
                scene fl 175b with dis17
                pause .1
                show fl 175
                play sound cumall
                play sound2 cumall
                mc "{sc=2}FFFFFFUUUUCKKK.....{/sc}{w=0.65}{nw}" with vpunch 
                play sound cumall
                play sound2 cumall
                mc "{sc=2}FFFFFFFFFUUUUUUUUUUUCKKKKKKK.....{/sc}" with vpunch 
                scene fl 176
                l "Wow." with dis15
                mc "OOOooooooh, godddd..." 
                mc "That was... glorious..."
                l "Geez, what a mess."
                mc "I'm sorry..."
                l "I-It's okay."
                l "Nothing that can't be cleaned."
                l "I-I've got a cloth right there."
            "Finish in her mouth" if lunablowjob:
                play sound rubbody
                stop soundloop fadeout 2
                stop soundloop4 fadeout 2
                scene fl 177
                mc "Oh f-f-fuck..." with dis
                mc "I'm cumming!" with hpunch 
                play sound cumall
                play sound2 cum3
                play sound3 fallhay 
                play sound4 impactwood
                scene fl 178
                mc "{sc=2}*Kicking the floor* FFFFFFFFFUCKKKKKKK.....{/sc}" with vpunch 
                l "Mmmmgh..."
                play sound cumall
                play sound2 cum3
                play sound3 fallhay
                play sound4 impactwood
                scene fl 179
                mc "{sc=2}AAAAaaaaaaaaghhh....{/sc}" with hpunchlong4  
                l "MMmmmmmmhmhmhh......" 
                play sound blow4
                play sound2 blow5
                show fl 180
                bla "Luna steps back with her mouth brimming with cum, not knowing exactly what to do next." with dis17
                mc "Ooooh, godddd..." 
                mc "That was... glorious..."
                l ". . ."
                play sound swallow
                play sound2 swallow
                scene fl 181
                l "*Swallowing* Mmph." with dis
                scene fl 182
                l "W-Wow." with dis
                l "That was... m-more than expected."
                mc "Yeah... sorry."
                l "I-It's okay."
                l "Easier to... clean, I-I guess."
                mct "She didn't even flinch when swallowing..."
                mct "My little deviant... Who would have thought..."
    else:
        mct "Man, now that she's using both of her hands, this feels like heaven..."
        mct "Only if she went fa–"
        stop soundloop fadeout 1
        play soundloop2 wetting6 fadein 2
        play soundloop3 wetting6 fadein 2
        scene lunah8 with dis22
        bla "Almost as if sensing your thoughts, Luna hastens her pace, determined to give you as much satisfaction as possible." with dis 
        mc "Ooooohhh, L-Luna..."
        l "Does it feel good...?"
        mc "Fucking incredible..."
        mc "P-Please, don't stop."
        l "Okay..."
        mc "Looks like your magic touch is finally doing the trick on me..."
        l "*Giggles* But this specific power is just for you..."
        mc "F-Fuck yeah..."
        play sound ["<silence 0.4>", spit]
        play sound2 ["<silence 0.4>", spit]
        stop soundloop2 fadeout 1
        stop soundloop3 fadeout 1
        scene fl 120b
        bla "Luna spits on the tip of your cock and uses it to lube your member." with dis12
        mc "My little deviant..."
        play soundloop2 wetting6 fadein 2
        play soundloop3 wetting6 fadein 2
        scene lunah8b with dis22
        mc "{sc=2}F-FUUUUUCK...{/sc}" with dis 
        l "Better?"
        mc "Much better..."
        l "*Whispering* Good..."
        mct "She's enjoying this."
        mct "She WANTS this."
        mct "I can sense it in the way she speaks."
        mct "I can see it written all over her face."
        mct "Those innocent features, now twisted by desire... and corrupted by lust."
        mct "Is it wrong that I feel proud about being the one who brought her to this state...?"
        mc "AAAAaaaahhh..."
        mc "J-Jesus fucking Christ, Luna..."
        mc "You're something else..."
        l "Mm-hm..."
        mc "AAAaahhh..."
        mc "F-Fuck, I'm g-gonna cum so much..."
        mc "I'm almost there... don't stop now..."
        l "I won't..."
        mc "Milk that cock, babe..."
        mc "Milk it till it's fucking dry..."
        jump cumminglunaatticr
    stop music3 fadeout 10
    play soundloop birds fadein 6
    play soundloop2 birds fadein 6
    play sound clothes
    play sound2 wood2 fadein 1 volume 0.4
    play sound3 debris
    scene fl 183 with dis22
    play sound4 chair2
    mc "*Sitting on the floor* My god, Luna..." with dis 
    mc "You left me empty."
    l "*Giggles* Did I...?"
    mc "For real..."
    $ renpy.end_replay()

label ga_alex2:
    show black 
    x "Mission failed, I can't open the window."with dis
    mc "Really?"
    play sound2 clothes3
    play sound3 clothes3
    scene eee 66
    mc "*Taking the shirt off your face* How..." with dis14
    stop soundloop2 fadeout 15
    $ renpy.music.set_volume(0.8, channel='music3')
    play music3 sexyalex2 fadein 7
    mc "...come?" with dis12
    x "The handle is stuck on something."
    x "Another thing to add to the never-ending list of repairs needed in this apartment..."
    play sound chair1
    show eee 67
    x "*Jumping on the couch* So I guess we'll have to go with plan B." with dis12
    x "You said... you don't mind, right?"
    show eee 68
    mc "Not..."
    mc "Not at all."
    show eee 67
    x "You okay?"
    show eee 68
    mc "Y-Yeah."
    show eee 67
    x "What's with that stammering? Did you really get shy all of a sudden?"
    x "After how much we've already seen of each other?"
    show eee 68
    mc "C-Certainly not!"
    mc "It's just that... I was expecting you to wear a bra under that shirt."
    show eee 67
    x "A bra? Why would I?"
    x "I'm in my own home. Wearing just an oversized T-shirt is the best thing in the world."
    x "And being able to take it off at night? Even better!"
    show eee 68
    mc "So you've been sleeping naked, huh?"
    mc "Aren't you afraid of some nosy neighbor catching a glimpse?"
    show eee 69
    x "Nah... the closest building is still too far away."
    x "And even then, the only apartment from where they could see us is where an old couple lives."
    show eee 68
    mc "I see..."
    show eee 69
    x "Anyway... goodnight, [mc]."
    x "I'm off to sleep on my “king-sized mattress”... you have fun out here."
    x "Sorry I don't have anything better to offer."
    show eee 68
    mc "It's okay... don't worry."
    show eee 67
    x "Before going to sleep, though, I just wanted to say..."
    show eee 69
    x "Look, I know I'm not the most expressive girl in the world."
    x "But... I still have emotions deep down. I’m not a cold-hearted tin-man like most would think!"
    show eee 67
    x "And today, you made me feel... um..."
    show eee 69
    x "I guess I just want you to know that... I really appreciate everything you did."
    x "Even if sometimes I make it seem like I couldn’t be bothered."
    show eee 67
    x "I mean... coming here to take care of me, and bringing me all the medicine."
    x "It... it really meant a lot."
    x "So thank you, [mc]."
    x "You've become... very special to me."
    show eee 68
    mc "You're... welcome..."
    show eee 70
    x "Did you even listen to a word I just said?" with dis
    x "Because it looked like you were staring at my tits the whole time."
    show eee 71
    mc "Uh..."
    mc "Something about... special medicine?"
    show eee 70
    x "So I open up my soul to you and you don't even pay attention?"
    show eee 71
    mc "Come on!"
    mc "You can't expect me to focus after showing up like that!"
    mc "I'm still in shock."
    show eee 70
    x "*Snorts* I see..."
    show eee 67
    x "Well, I'll let you be, then."with dis
    x "Rest well!"
    show eee 68
    mc "Aren’t you going to kiss me goodnight before you go?"
    show eee 70
    x "A goodnight kiss?"with dis
    show eee 71
    if alexkisswest:
        mc "The one we had in Blackridge really left me hungry for another."
    else:
        mc "I'm not sure I'll be able to fall asleep without one."
    show eee 67
    x "I'm sorry, I might have no symptoms at the moment thanks to your meds, but I'm still sick." with dis 
    x "I'd just pass on the cold to you."
    x "And with how whiney you could be, I wouldn’t want to hear about it."
    x "Plus, you’re our main offensive weapon in Eternum, and the one who's carrying the Gems. We need you at full capacity."
    show eee 68
    mc "Well... as long as I stay away from your airways, I should be good."
    show eee 70
    x "*Chuckles* Ah, yeah, a flawless plan." with dis
    x "You know my “airways” are required in a kiss, right?"
    show eee 71
    mc "Well then, we can always find... {i}other{/i} goodnight rituals that don't involve them..."
    mc "Something that keeps our mouths away from each other."
    show eee 70
    x "Oh, really?"
    x "Such as?"
    show eee 71
    menu:
        with dis
        "Caress her":
            mc "Well... I could kiss you... but maybe a little further south..." with dis06 
            show eee 70
            x "Ah, yes, “further south”."
            x "There’s so many places that are further down. Where did you have in mind, exactly...?"
            show eee 71
            mc "Hmm, let me think..."
            play sound squeak
            play sound3 clothes3
            show eee 83 with dis15
            bla "Feeling emboldened by Alex's playful demeanor, you stand up while pulling her closer and nestling her between the cushions." with dis
            mc "Well..."
            mc "I certainly have a couple spots in mind."
            show eee 84
            x "Do you now?"
            x "Now the suspense is killing me. I’m very curious where this mystery leads..."
            show eee 83
            mc "*Chuckles* You can probably imagine."
            show eee 84
            x "Who, me?"
            x "I'm just a sweet and innocent princess, I can't possibly imagine what you have in that dirty mind of yours."
            x "Maybe I need someone bad like you to enlighten me..."
            show eee 83
            mc "Well... I thought I could kiss your toes..."
            show eee 84
            x "Mm-hm... warm..."
            show eee 83
            mc "Then your thighs..."
            show eee 84
            x "Ah, getting warmer..."
            show eee 83
            mc "And then..."
            show eee 84
            x "Yes...?"
            play sound4 fall2
            play sound5 fall2
            play sound6 clothes3
            show eee 85 with dis12
            mc "*Kneeling between her legs* Better yet, why don’t I just demonstrate for you..." with dis
            x "Burning hot..."
            show eee 86 
            bla "You caress Alex's intimate parts through her underwear. She doesn't recoil or shy away, although you can hear her breaths quickening at the feel of your touch." with dis 
            show eee 87
            bla "You gently move the delicate fabric of her panties to the side, revealing the smooth contours of her perfectly shaved pussy." with dis
            mct "Oh sweet Lord..."
            play sound bodycollide
            show eee 88
            bla "Without waiting a second longer, you shove your head in between Alex's firm thighs and spread her velvety lips with your tongue." with dis
            show eee 89
            x "*Letting out a suppressed moaning* MMMmmmh..." with dis12
            mc "Can I continue, then...?"
            x "Mm-hm..."
            scene alexsex0_1 with dis17
            bla "Upon noticing Alex's inviting response, you tightly grab her legs and start eating her out." with dis 
            x "O-Ooh.... FUCK, [mc]..."
            mct "God, I love her taste..."
            mct "Her scent..."
            mct "I love everything about her..."
            x "*Gasping* AAAaaahh..."
            mct "Now that I think about it, I have never heard Alex moaning before."
            mct "It sounds so unlike her, but incredibly hot at the same time..."
            x "AAAahhh s-shit..."
            x "*Moaning* F-Fuck, this feels so good..."
            mct "This is definitely a side of her that I’ve never seen before."
            x "P-Please keep doing what you're doing..."
            bla "Your eyes wander from Alex's pussy to her athletic body, taking joy in each one of her involuntary squirms and reactions."with dis
            x "Aaahh..."
            x "T-This is definitely..."
            x "T-The best “goodnight kiss” I've ever gotten..."
            x "AAaahhhh..."
            x "F-Fuck, [mc]..."
            mc "Mmmm..."
            pause
            play soundlow chair2
            play sound2 clothes3
            play sound3 ["<silence 0.1>", chair1]
            scene eee 90 
            bla "Alex abruptly pushes you to the side and stands up." with dis14
            mc "W-What happened?"
            mc "Was something wrong...?"
            play sound4 fall2
            show eee 94
            bla "She kneels down between your legs without saying a word." with dis12
            mc "Okay, I like where this is going..."
            play sound clothes3
            play sound7 clothes3
            show eee 95 with dis15
            mc "Oh fuck yes..." with dis
            bla "Alex stares mesmerized at your junk for a few seconds before pulling your pants down completely."
            play sound clothes3
            play sound7 clothes3
            show eee 96 with dis15
            pause
            show eee 96c
            x "I bet you feel better now."with dis12
            show eee 96b
            mc "Definitely..."
            show eee 96c
            x "I almost could feel your pants about to burst while you were going down on me."
            x "And looks like I wasn't wrong."
            show eee 92
            x "*Standing up again* You were ready for battle down there, huh?" with dis12
            show eee 93
            mc "I can't help it... that's the effect you have on me."
            show eee 92
            x "Now... before you continue what you were doing..."
            x "I thought I could give you a hand too."
            show eee 93
            mc "That sounds damn good to me..."
            show eee 92
            x "I mean, you're my guest after all."
            x "I wouldn't want you to feel uncomfortable, or to make you do all the work."
            x "What would people say of me, right?"
            show eee 93
            mc "I surely wouldn't want you to be known as a bad hostess..."
        "Ask her to caress you":
            mc "Well... you could kiss me on... some other part." with dis06 
            play sound squeak
            play sound3 clothes3
            show eee 72
            x "*Getting comfortable between the cushions* Another part, huh...?" with dis12
            x "Such as...?"
            show eee 73
            mc "Surprise me."
            show eee 72
            x "No, no, it was your idea!"
            x "Did you have something in mind?"
            show eee 73
            mc "*Chuckles* You can probably guess."
            show eee 72
            x "Who, me?"
            x "I'm just a sweet and innocent princess, I couldn’t possibly imagine what you have in that dirty mind of yours."
            x "Please, enlighten me..."
            show eee 73
            mc "*Chuckles* Well..."
            mc "You could kiss me on my chest, for example."
            x "Mm-hm."
            mc "Then my stomach..."
            x "Hmmmph..."
            mc "Then you could take off my pants, and..."
            play sound2 bodycollide
            play sound bodycollide
            show eee 74
            x "*Gasps* Hold on there!" with dis08
            x "You nasty pervert!"
            show eee 75
            mc "It's you who asked me what was on my mind."
            show eee 74
            x "Yes, but I thought you were a gentleman, not a perv."
            x "I invite you to my own home, I let you stay under my roof, eat my chips, and this is how you behave yourself?"
            x "No kiss for you."
            x "Sick or not, you don't deserve my lips, [mc]..."
            show eee 75
            mc "Awh, really?"
            mc "And what about your hands?"
            show eee 74
            x "*Gasps* Gross! Definitely not that either."
            x "You should be grateful for just getting my foot."
            show eee 75
            mc "Well, depending on where I am getting it... I'd definitely accept that."
            mc "Although... I'd need to get a little more comfortable for that."
            show eee 74
            x "Oh, is that so?"
            show eee 72
            x "Don't let me stop you, then..."with dis
            x "Feel free to get more comfortable, if you want."
            show eee 73
            mc "Can I take my pants off?"
            show eee 72
            x "Of course, do what you wish."
            x "Make yourself at home."
            show eee 77
            mc "Ah, thank goodness. You have no idea how much I appreciate that." with dis14
            mc "The warmth was starting to become unbearable."
            play sound clothes5
            show eee 78 with dis17
            bla "You pull your pants down, exposing your already-fully-erect member." with dis
            x "*Mumbling* Jesus..."
            play sound2 clothes3
            scene eee 79
            x "*Touching your dick with her toes* What the hell is that, [mc]...?" with dis15
            show eee 80b
            mct "Oh, fuck yes..." with dis08
            mc "W-What do you mean?"
            show eee 79
            x "I mean the fact that a third of your blood is currently concentrated in your dong." with dis08
            x "You sure were ready for battle down there." 
            show eee 80b
            mc "I can't help it, it's the effect you have on me." with dis08
            show eee 79 
            x "Really? Just because of seeing my boobs?"with dis08
            show eee 80b
            mc "Your naked body, your constant teasing..."with dis08
            mc "It’s all of you, Alex."
            show eee 79
            x "Ah, I see..."with dis08
            play sound clothes3
            play soundlow squeak
            show eee 82
            bla "Alex spreads her legs and puts her feet around your hard cock."with dis15
            mc "*Clenching your fist* Oh yes..."
            show eee 81
            x "Perv..."
            scene alexsex0_2 with dis17
            mc "Oh, f-fuck..." with dis
            bla "Alex quickly sets a pace, gently jacking you off with her warm and surprisingly skilled feet."
            mc "Oh YES..."
            mc "God..."
            mc "You're good at this..."
            x "Thank you."
            mc "Aaahh..."
            mc "I-I've gotta say..."
            mc "This is definitely the best “goodnight kiss” I've ever gotten..."
            x "*Giggles* I bet."
            x "You're hard as fuck."
            mc "F-Fuck, how could I not..."
            bla "Your eyes wander from Alex's feet to her athletic body, captivated by the subtle transformation of her expression, which seems to grow more lustful with each passing moment."with dis
            mc "Aaaah..."
            x "*Giggles* Mmh."
            mc "You're enjoying this, aren't you?"
            x "*Giggles* Probably not as much as you..."
            mc "*Chuckles* P-Probably not..."
            pause
            play soundlow chair2
            play sound2 clothes3
            play sound3 clothes3
            scene eee 93 with dis17
            bla "Alex abruptly stops the footjob and stands up, positioning herself in front of you." with dis
            mc "W-What happened...?"
            show eee 92
            x "Before we continue..."
            x "Let me get rid of this for you..."
            play sound4 fall2
            play sound5 fall2
            show eee 95
            bla "She kneels down between your legs and stares mesmerized at your junk for a few seconds before pulling your pants down." with dis12
            play sound clothes3
            play sound7 clothes3
            show eee 96 with dis14
            pause
            show eee 96c
            x "You know... I might have been too harsh before..."with dis12
            x "So..."
            x "Okay."
            x "I'll let you... have my hands."
            x "I guess you've earned it after all you've done today."
            show eee 96b
            mc "Oh man..."
            show eee 96c
            x "So..."
            x "Can I... grab it...?"
            show eee 96b
            mc "O-Of course..."
    play sound2 clothes3
    play soundlow squeak fadein 1
    show eee 97 with dis14
    play sound3 bodycollide
    bla "Alex straddles you and firmly wraps her small hands around your dick." with dis12
    mc "O-O-Oh, fuck yes..."
    mc "*Caressing her thigh* I guess you do have some five-star amenities after all..."
    show eee 98
    x "*Giggles* Well..." with dis12
    x "As long as our... airways... stay away from each other..."
    x "We should be good... right?"
    x "I wouldn't want the girls to get mad at me because I got you sick."
    mc "Definitely..."
    scene alexsex0_3 with dis2
    bla "Alex starts to jack you off in a teasingly slow manner, as your cock gets unbelievably hard." with dis12
    mc "Oh Jesus, t-that feels good..."
    x "Mm-hm..."
    mc "Aaahh..."
    x "*Soft moan* Why do I feel like you’re even stiffer than that day in Eternum, [mc]..."
    x "This thing is pulsating so much, as if it were about to explode."
    mc "F-Fuck, Alex, you're driving me insane..."
    if alexfootjob:
        mc "Don't you wanna switch now? I need to edge off a bit..."
        mc "And... I could give you a hand too..."
    else:
        mc "Don't you wanna switch again? I need to edge off a bit..."
    x "Nah-ah. You aren’t going anywhere."
    x "*Giggles* Teasing you is even more enjoyable..."
    mc "Aaahh..."
    mc "F-Fuck... seeing it right in front of you like this..."
    mc "I can't stop imagining how it would feel to stuff my cock inside your petite body... you see how deep inside you it’d go...?"
    x "*Scoffs* What do you mean, petite? I'm not petite."
    x "Any woman would look small next to your ginormous junk."
    mc "Nah... you are. It's just that your attitude gives you a strong presence, making you seem... larger."
    x "*Chuckles* Bullshit."
    mc "How tall are you?"
    x "5'4''."
    mc "So, same as Nova..."
    x "*Giggles* I'm taller than Nova."
    mc "You're my little petite princess..."
    x "*Giggles* Shut the fuck up."
    pause
    bla "As the teasing continues, the anticipation starts to intensify to unbearable levels, blurring the border between pleasure and pain." with dis 
    mc "*Panting* F-Fuck, Alex..."
    mc "I..."
    mc "I can't bear this anymore."
    x "*Soft voice* Do you want me to go faster...?"
    mc "I want to fuck you..."
    mc "I {i}need{/i} to..."
    mc "Aren't you horny too?"
    x ". . ."
    x "Would it go to your head if I said yes...?"
    mc "Then..."
    mc "If we both want it, why don’t..."
    x ". . ."
    pause
    play sound2 clothes3
    play sound squeak fadein 1
    show eee 99 with dis17
    bla "Alex stands up and grabs the side seams of her panties." with dis
    play sound3 clothes3
    play sound4 clothes3
    show eee 100
    bla "She pulls them down to her thighs and lets them drop to the floor." with dis17
    mct "No."
    mct "It's impossible."
    mct "I’m dreaming, right?"
    show eee 103
    bla "You slowly raise your gaze to Alex's face, afraid that uttering a single word could change the course of what you think is about to happen." with dis17
    x "*Breathing very quickly* . . . ."
    show eee 102
    x "Okay, I'm about to say something that I'll probably regret deeply tomorrow morning."
    x "Or... probably regret before the night is over."
    show eee 103
    mc "Oh god."
    show eee 102
    x "Q-Quiet."
    x "D-Don't utter a single word or you'll make me change my mind. Do you understand?"
    show eee 103
    bla "You nod intensely, feeling your heartbeat skyrocket to worrying levels."
    x "*Breathing very quickly* . . . ."
    show eee 102
    x "Yes, I'm horny as fuck."
    x "So..."
    show eee 103
    x "*Breathing very quickly* . . . ."
    show eee 102
    x "I'm going to let you put it in."
    show eee 103
    mct "OH GOD."
    show eee 102
    x "But JUST the tip."
    x "And only for... like... two minutes. Three minutes, tops. If you can last that long."
    x "Those are the two simple rules you have to follow, or else this thing is over."
    x "A-Are we clear?"
    show eee 103
    mc "Just the tip, and three minutes tops..."
    show eee 102
    x "Good."
    show eee 103
    x "*Breathing very quickly* . . . ."
    play sound2 clothes3
    play sound3 clothes3
    play sound squeak fadein 1
    show eee 104 with dis17
    bla "Alex gets on the couch and straddles you, getting into position." with dis12
    mc "Oh my fucking god, Alex..."
    x "*Bitting her lip* Are you ready?"
    mc "No man can be ready for this..."
    play sound5 penetration2 fadein 1
    show eee 105
    bla "Alex lets out a loud moan as she mounts the tip of your cock and it slides slowly into her warm embrace." with dis17
    x "*Moaning* F-Fuck..."
    mc "OH MY GOD..."
    play sound6 penetration2 fadein 1
    show eee 106
    x "*Letting her body sink into you* F-FUUUCK..."with dis17
    $ renpy.music.set_volume(0.3, delay=10.0, channel='music3')
    $ renpy.music.set_volume(1.0, channel='soundloop')
    $ renpy.music.set_volume(1.0, channel='soundloop2')
    play soundloop alexsex1_2 fadein 3
    scene alexsex1_1 with dis22
    x "*Panting* Aargh.... aaaahh... aaaahhh..."with dis12
    x "Oh m-my g-gooood..."
    mc "Jesus Christ, Alex..."
    x "*Moaning* Yeah..."
    x "T-This is..."
    x "J-Just what I needed..."
    mc "Oh babe..."
    mct "It happened."
    mct "I'M FINALLY INSIDE OF ALEX."
    mct "I'M FUCKING HER."
    mct "And she's even tighter than I imagined, good lord..."
    x "F-Fuck, [mc], h-how can this just be the tip..."
    x "It's... too big..."
    mc "Does it hurt?"
    x "H-Hurt?"
    x "F-Fuck no... it feels AMAZING..."
    pause
    stop soundloop fadeout 2
    play soundloop2 alexsex1_2 fadein 3
    scene alexsex1_2 with dis22
    bla "Alex continues to ride you in ecstasy. You feel her tight pussy gradually accommodate your size more and more with each thrust, as if her young, athletic body was begging for more."with dis
    x "*Moaning* Mmmmm..."
    x "F-Fuck yes..."
    mc "Oh good lord..."
    x "*Giggles* MMmmmmMmm..."
    mc "Oh my, Alex..."
    x "You know..."
    x "W-We've already exceeded the three-minute mark, [mc]..."
    mc "P-Please, don't get off me..."
    mc "Let me stay inside you forever..."
    x "I..."
    x "AAAaahh..."
    x "I certainly don't want to stop..."
    x "*Moaning* Mmmmmhh..."
    x "I... {i}c-can't{/i} stop..."
    pause
    x "I wonder if... for that matter..."with dis
    x "Since we already broke one of the two rules... maybe we should break the other one as well..."
    mc "W-What?"
    x "*Panting* I-I think I can take it deeper."
    x "I want to see if I can take... ALL OF YOU... inside of me..."
    x "I wanna know how it feels..."
    mct "Oh Jesus..."
    bla "You grab on tight to the blanket under you and look at the ceiling, trying not to cum too fast and end this ethereal dream."
    x "*Whispering* So tell me..."
    x "*Whispering* Are you ready now..."
    x "*Whispering* For the ride of your life, cowboy...?"
    mc "Lord give me strength..."
    stop soundloop2 fadeout 1
    play sound penetration3
    show eee 106c with dis17
    x "AAAAAaAaaAaaaAAAAHH..." with dis
    mc "SHIIIIT..."
    x "*Giggles* W-Wow...."
    play soundloop alexsex1_3 fadein 2
    scene alexsex1_3 with dis22
    x "OH M-MY GOOOOODDDDD..." with dis
    x "*Squealing* AAAAAAHh..."
    mc "OH GOOD LORD..."
    x "Oh F-FUCK, [mc!u]!"with hpunch
    x "YES!" with hpunch
    x "{sc=2}Y-YES!{/sc}" with hpunch 
    bla "Alex rides your cock hungrily, taking all of your length, balls deep inside her hot pussy as if she had been possessed."
    x "*Panting* YES! YES..."
    x "Y-YES!" with hpunch
    mc "Oh Alex..."
    x "*Panting* OH MY F-F-FFUCKING GOD..."
    mc "I-It's so fucking tight..."
    mc "So warm..."
    mc "So wet..."
    x "*Panting* AAahh..."
    x "*Panting* I a-almost... c-can't breathe..."
    x "*Panting* But I can't stop either..."
    mct "Dear Lord, I can feel how my cock fills her completely, stretching her to her physical limit..." 
    mct "The head of my dick hitting her cervix with each thrust..."
    x "AAARGH FUCK, [mc]..." with hpunch 
    x "P-P-Please don't cum..."
    x "Not yet..."
    x "I d-don't want this to s-stop..."
    x "*Groaning* AAAAaaRgh..."
    x "Give me more of you..."
    pause
    stop soundloop fadeout 2
    play soundloop2 alexsex1_4 fadein 3
    scene alexsex1_4 with dis22
    bla "Just when you thought it was impossible, Alex still manages to increase her intensity and continues to ride you relentlessly." with dis 
    x "*Squealing* F-FFFUCK YES!"
    x "*Squaling* Fuck me, [mc]!"with hpunch
    x "HARDER!" with hpunch 
    x "DEEPER!" with hpunch 
    x "Fill me up just like that..."
    x "I want every inch of you inside of me..."
    bla "You finally take a moment to lift your head and focus on the woman who seems to be draining the very essence of your being."
    mc "*Panting* Holy fuck..."
    mc "Oh my god, Alex, I'm gonna c-cum so hard..."
    mc "I c-can feel it coming..."
    x "*Panting* I'm a-almost there..."
    x "AAAaaHHhhh..."
    x "*Panting* J-Just hang in there a bit more, please..."
    pause
    stop soundloop2 fadeout 2
    play soundloop alexsex1_5 fadein 3
    scene alexsex1_5 with dis22
    x "*Panting* Aaahhh... aaaAAaahh... AAAAHH!" with dis 
    x "{sc=2}OH MY GOD!{/sc}" with hpunch 
    x "{sc=2}[mc!u]!!!{/sc}" with hpunch 
    mc "OH ALEX..."
    mct "How the fuck this couch is still standing is something I'll never know..."
    x "AAAHH..."
    mct "J-Just the tip, she said..."
    x "AAAAAHHHH..."
    x "I... I'M–"
    mc "A-Alex, I'm gonna..."
    x "*Panting* F-Fuck, I'm cumming too!"
    mc "Y-You need to... get off me..."
    x "F-Fuck no..."
    mc "B-But–"
    x "*Panting* F-Finish inside me..."
    mc "W-What...?"
    x "*Panting* I want you... to cum... inside me!"
    x "*Squeals* AAAAAAAGH!" with hpunch 
    x "*Panting* G-Give me everything you got..."
    mc "B-But what if..."
    x "{sc=2}SHUT THE FUCK UP AND FILL ME UP!!!{/sc}" with hpunch
    mc "Oh babe..."
    pause
    play sound clothes4
    play sound3 chair1
    play sound4 squeak
    play sound5 cumall
    stop soundloop fadeout 1
    scene eee 107 with dis17
    $ renpy.music.set_volume(0.6, delay=20.0, channel='music3')
    play sound2 cumall
    mc "*Creampieing Alex* AAAAARGH!!!" with vpunch
    play sound6 cumall
    x "*Orgasming at the same time as you* AAAAAHHHH..." with vpunch 
    play sound7 cumall
    mc "AAAArrrghhh..."with vpunch 
    play sound3 cumall
    mc "*Still cumming inside Alex* AAaaaahhhh..." with vpunch 
    x "*Breathing heavily* Aaahh... aaaahh... aaahhh..."with dis14
    x "*Breathing heavily* Haha..."
    play sound penetration3
    scene eee 108
    x "I-I feel like you just unloaded a whole gallon inside of me..." with dis15
    mc "M-Maybe you’re not far off..."
    play sound2 penetration3
    play sound7 penetration3
    show eee 109 with dis2
    bla "Alex stands up with difficulty, while the hot load you just shot deep inside of her starts to ooze out."with dis12
    play sound3 chair1
    play sound2 squeak
    show eee 110
    x "*Rolling to the side* Unbelievable..." with dis12
    show eee 111
    mc "My god..."
    show eee 110
    x "That got... a b-bit out of hand... haha..."
    show eee 111
    mc "You're... too much..."
    show eee 110
    x "This can't happen again, you know that, right?"
    show eee 111
    mc "W-What?"
    mc "Are you serious?"
    show eee 110
    x "Absolutely."
    x "This will... never happen again."
    x "N-Never again..."
    show eee 111
    mc "Huh."
    show eee 110
    x "Do you... understand?"
    show eee 111
    mc "Yeah... it won't happen again."
    show eee 110
    x "It was... good... but it was a one time thing."
    show eee 111
    mc "O-Okay."
    show eee 110
    x "No more."
    show eee 111
    mc "Not in a million years."
    show eee 110
    x "Never again."
    show eee 111
    mc "Never..."
    show eee 110
    x "...again."
    scene eee 111
    x ". . ."
    mc ". . ."
    x ". . ."
    $ renpy.music.set_volume(0.4, delay=15.0, channel='music3')
    $ renpy.music.set_volume(1.0, channel='soundloop3')
    play sound w1
    play sound2 w1
    play soundloop3 shower2 fadein 1
    scene eee111b
    pause .13
    play soundloop alexsex2_4
    scene alexsex2_4
    pause .1
    x "MMmmmMMMmMHH!" with dis
    bla "Alex briefly breaks the kiss, allowing herself a moment to catch her breath and find the words she wants to share."
    x "*Whispering* F-Fuck, [mc]..."
    x "*Whispering* G-Go easy..."
    mc "You know I can't, Alex..."
    x "*Moaning* Mmmmmm..."
    x "T-That was supposed to be the last time..."
    mc "You were the one who followed me to the shower, remember...?"
    x "B-Because you were taking too long... and I'm the one paying the water bill."
    mc "Suuure, you didn't come with {i}any{/i} other intentions..."
    x "I'm not the one who got hard as soon as I stepped into the shower."
    mc "Ah... well, I'm guilty there."
    mc "I just love fucking you too much."
    x "*Giggles* Ah."
    x "*Whispering* Then do it..."
    x "*Whispering* Fuck me hard, [mc]..."
    stop soundloop
    play soundloop2 alexsex2_4
    scene alexsex2_3 with dis2
    bla "You shut her up by kissing her again, while continuing to pound her pussy without break." with dis
    x "*Moaning* MMmmmmMmmhh..."
    mct "Oh my fucking god, this feels like heaven..."
    mct "How easily she lets me slide all the way into the deepest depths of her... while still being outrageously tight..."
    mct "It's insane..."
    x "*Moaning* MMmMh!"
    mct "She has a body made to sin."
    mct "I mean, god, she's almost dripping more than the shower."
    mct "I wonder if I could ever make her squirt... make her banter that day at the park with Axel a reality..."
    x "*Moaning* Mmmmm.... MMmmmmMhh... MMMMmmhHHHHh!"
    pause
    stop soundloop2
    play soundloop alexsex2_4
    scene alexsex2_5 with dis2
    x "*Moaning* MMMmmmmMmmm..."with dis
    bla "You continue to penetrate Alex incessantly, pounding your body against the tattooed girl's slim figure."
    mct "Fuck, I love how synchronized we are..."
    mct "The way she pushes her hips against mine with each stroke..."
    mct "The fierce passion in her kisses, even despite the challenge of maintaining a constant connection due to the relentless hammering..."
    mct "And how she pulls me back closer to her with her leg..."
    mct "We’re as close as two humans could be, but it’s like she still hungers for more..."
    x "*Moaning loudly* MMMmMMH!"with hpunch
    mct "She wants me."
    x "*Moaning* MMmmmmmh!"with hpunch
    mct "And I want her..."
    x "*Moaning* MMMmmmmmMMmmhhhh..."with hpunch
    mct "I want to break her..."
    pause
    stop soundloop 
    play soundloop2 alexsex2_1 
    scene alexsex2_1 with dis2
    x "AAAAAAHH!" with dis 
    bla "You drastically increase your pace, with Alex responding in kind, adapting to the new rhythm almost instantly."
    x "Oh F-F-FUCK, [mc]!"
    x "AAAAaaaaaHHhhh..."
    mc "F-Fuck yes..."
    x "*Panting* W-We shouldn't have kissed... now y-you'll get sick..."
    mc "Fuck that..."
    mc "I'd get sick for a year if that meant I got to fuck you one more time..."
    x "AAAAaaahhh... yes... right there..."
    mc "O-Oh, Alex..."
    mc "I want to fuck you SO hard..."
    x "*Panting* Y-Yeah, do it then..."
    x "*Panting* Fuck me harder..."
    mc "I want to break you..."
    mc "I want to find out where your limits are..."
    x "*Panting* AAAahhh... YES..."
    x "*Whispering* B-Break me..."
    stop soundloop2 
    play soundloop alexsex2_1 
    scene alexsex2_2 with dis2
    x "*Moaning* Oh m-my GODDDD..."with dis
    x "AAAHHHH!"
    x "*Panting* Shit, [mc], I'm gonna cum again..."
    mc "M-Me too, Alex..."
    x "*Squealing* AAAAARGH!"
    bla "You continue to incessantly pound Alex's pussy as she groans loudly with pleasure. With the walls as thin as they are in these apartments, no doubt the neighbors could hear the two of you going at it continuously."
    x "AAAAAaaaAAAhhhhh..."
    x "*Panting* F-Fuck..."
    mc "Shit, I'm almost there..."
    x "*Panting* Y-You can finish inside again, but..."
    mc "Oh boy..."
    x "*Panting* This is the last time, you hear me?"
    mc "O-Okay..."
    x "*Panting* This was a mistake, we should’ve just stopped earlier..."
    mc "A-Agreed..."
    x "*Panting* So t-this is it! F-For real this time..."
    x "*Panting* Never again..."
    mc "Never..."
    x "*Panting* Again..."
    $ renpy.music.set_volume(0.5, delay=1.0, channel='music3')
    play sound w1
    play sound2 w1
    stop soundloop3
    play soundloop alexsex3_1 volume 0.9
    play soundloop3 rain3
    scene eee111c
    pause .13
    scene alexsex3_1
    pause .1
    x "AAAaaaahhh... MY GOD..." with dis
    x "{sc=2}[mc!u]!!!{/sc}" with hpunch 
    x "{sc=2}AAAAAAHHHHH!!!{/sc}" with hpunch 
    x "{sc=2}Y-YEAH!{/sc}" with hpunch 
    x "{sc=2}F-FUCK M-ME!!{/sc}" with hpunch 
    x "{sc=2}F-FUCK M-ME H-HARDER...{/sc}" with hpunch 
    mc "*Panting* Oh babe..."
    x "AAAahh..."
    x "*Panting* T-T-This i-is i-it..."
    x "*Panting* I-I'm a-at... m-my l-lim-mit..."
    x "*Panting* I-I c-can't..."
    bla "Alex's voice cracks every time you shove your cock into her, which makes her words almost unintelligible as the pleasure completely overtakes her."
    x "AAAA-A-ARh-HhhHA..." 
    mct "I'm almost at my limit as well..."
    mct "But fuck... dominating Alex like this is so damn hot..."
    x "*Moaning* AAAAa-AGAHH..." with hpunch 
    mc "Oooohhh, I'm almost there again..."
    x "AAAaaaahh..."
    mc "*Pulling Alex's head* You're gonna take it all like the good princess you are, aren't you, babe...?"
    x "Ggggghh..."
    x "*Panting* Y-Yeah...."
    x "*Panting* G-Give i-it a-a-all t-to m-me..."
    x "*Panting* I w-want it..."
    stop soundloop 
    play soundloop2 alexsex3_2 volume 0.9
    scene alexsex3_2 with dis2
    bla "You continue pumping Alex's pussy until you both reach the bounds of raw, carnal ecstasy."with dis
    x "Oh m-my god."
    x "I'm c-cumming."
    x "I'm c-coming a-again..."
    x "Aaaaaahh..."
    x "AAAAAAAAaaaAAaahhh...." with hpunch
    play sound cumall
    x "{sc=2}AAAAAAAAAAAAAaaaaaGGHHHHhhhh!!!{/sc}"with hpunch
    bla "You can feel Alex orgasming even more intensely than before."
    bla "Her whole body tenses up and her vaginal walls contract, giving you a wave of unimaginable pleasure."
    mc "Fuuuuuck..."
    x "*Panting* J-Jesusss C-Christ..."
    stop soundloop2
    play soundloop alexsex3_1 volume 0.9
    scene alexsex3_1 with dis2
    x "*Panting* [mc]... p-please..."with dis
    mc "*Panting* I-I know, babe, just hold on a bit more, I'm almost... there... too..."
    x "*Panting* AAaaaahhh... I c-can't..."
    mc "*Panting* I am almost..."
    stop soundloop fadeout 1
    play sound clothes3
    play sound2 clothes4
    play sound3 penetration3
    scene eee 112 with dis14
    pause
    play sound5 cumall
    play soundlow penetration3
    play sound4 slap1
    show eee 113
    mc "{sc=2}AAAAAAAAGHHH...{/sc}" with hpunch
    play sound6 cumall
    bla "As if compelled by a primal instinct, you unleash every ounce of jizz left in you deep inside Alex for the third time tonight." with hpunch
    play sound7 cumall
    mc "Fuuuuuckk...." with hpunch
    x "G-G-Gggghhh..."
    stop music3 fadeout 14
    play sound clothes3
    play sound2 fall2
    play sound3 penetration3
    play sound4 woodhit
    scene eee 114 with dis22
    bla "You slowly step away as you watch, almost with a sort of pride, a completely exhausted Alex collapsing onto the ground." with dis
    x "*Panting heavily* Oh my fucking bloody fuck shitty fucked damnit fucker..."
    x "*Panting heavily* FUUUUUCK... I can barely even speak..."
    mc "*Leaning on the wall and recovering your breath* T-That was... p-pretty intense, huh?"
    x "I c-can't... stand up."
    x "I can’t feel my legs."
    mc "You're an absolute wild beast, Alex."
    mc "Tonight was..."
    mc "I don't even know how to describe it with words."
    x "I have never felt anything that comes even close to this..."
    x "Just... holy fuck..."
    mc "Well... I hereby declare your apartment officially christened."
    x "*Cracked chuckle* Yeah... I'd say it's been christened alright."
    mc "*Trying to stand up* Jesus... I’m having trouble walking too."
    mc "I'm going to take a shower. A real one, this time."
    x "Yeah... you go ahead. I'll go after."
    x "Probably better if I just stay out here this time..."
    mc "You sure you're okay?"
    x "Yeah..."
    x "I just need a minute to compose myself."
    play sound thunder
    show eee 115 with dis03
    pause .4
    show eee 114 with dis22
    x "Or maybe... a couple of minutes..." with dis
    stop sound fadeout 1
    $ renpy.end_replay()

label ga_dalia3:
    $ renpy.music.set_volume(0.65, channel='music3')
    play music3 eyg fadein 6
    show ed 54
    d ". . ." with dis
    mc "I like that smirk."
    show ed 51
    d "Might be this homemade whiskey talking, but... fuck it, alright."
    d "Let's do this."
    show ed 54
    mc "Wait... really?"
    play sound chair3
    show ed 54b
    d "*Leaning forward* Yeah... why not." with dis
    d "I'm not one to shy away from a competition, no matter the circumstances."
    d "Let's make it interesting."
    d "The game... is on."
    mc "You know, I've always loved your competitive side..."
    play sound2 chair2
    show ed 58 
    bla "Dalia stands up with determination and grabs one of the darts."with dis12
    mc "Do you wanna make a few test throws?"
    show ed 56
    d "I need no tests."with dis
    d "You can start taking off your shoes, though."
    d "It'll save us time."
    mc "*Chuckles* You'll pay for that overconfidence."
    d "Just watch. Straight to the center."
    play sound dart
    scene ed59 with hpunch
    pause .4
    mc "HAH!"with dis08
    show ed 60
    d "Dammit."with dis
    d "I drank too much."
    show ed 61
    mc "*Grabbing a blue dart* This will be the easiest competition in the history of competitions." with dis12
    mc "Don't try to find excuses."
    show ed 62
    d "*Chuckles* Shut up and throw it already."
    d "Just make sure not to hit me."
    play sound dart
    scene ed62b with hpunch
    pause .4
    mc "Yes!" with dis08 
    show ed 63
    d "Huh, nice one."with dis 
    show ed 64
    mc "Thank you."
    show ed 63
    d "Beginner's luck."
    show ed 64
    mc "More like pure skill."
    show ed 63
    d "*Laughs* Sure..."
    play sound clothes3
    play sound7 clothes3
    show ed 65
    bla "Dalia slowly removes her boots and leaves them under the table."with dis15
    mc "Wow..."
    mc "Your legs really look as if they were sculpted in marble."
    d "*Giggles playfully* Shut up and play, Michelangelo."
    play sound dart
    scene ed66
    pause 
    play sound w1
    scene ed67 
    pause 
    play sound belt
    scene ed 68
    bla "Dalia unbuttons her corset and takes it off." with dis17
    mc "Nice..."
    play sound dart
    scene ed69
    pause 
    play sound5 w1
    show ed70
    pause 
    play sound clothes4
    scene ed 71 with dis17
    mc "I really like this game..."with dissolve
    show ed 72
    d "I-I think there's something wrong with my dart."with dis
    d "Let me use yours."
    show ed 73
    mc "No way! I got used to this one already."with dis
    show ed 74
    d "So you're admitting that they're not the same?"
    show ed 73
    mc "Mmm..."
    mc "Okay, fine, I'll use the red one."
    mc "But if I win... I get to suck your tits."
    show ed 74
    d "What?! You're dreaming."
    show ed 73
    mc "No deal then."
    d ". . ."
    show ed 74
    d "You can lick my ankles."
    show ed 73
    mc "Your tits."
    show ed 74
    d "My legs."
    show ed 73
    mc "Your abs."
    d ". . ."
    show ed 74
    d "Okay, my abs."
    show ed 73
    mc "Oh boy... one of my fantasies is about to come true."
    show ed 75 with dis17
    d "*Giggles* And now you throw the darts like a professional??"with dissolve 
    mc "Mm-hm..."
    play sound dart
    scene ed76 with hpunch 
    pause .4
    mc "Because I AM a professional!" with dis08 
    mc "I almost hit the center!"
    d "*Grumbling* Make room!"
    scene ed 77 with dis15
    pause 
    d "*Takes a deep breath*"with dis08
    play sound dart
    scene ed78 with hpunch 
    pause .4
    d "AAGH!" with dis08
    show ed 79
    d "NO FUCKING WAY!!!" with hpunch
    d "You {i}had{/i} to have your lucky throw just when I finally got the hang of it!"
    mc "*Chuckles* It is what it is..."
    show ed 80
    d "*Sighs* Okay, okay, fine..." with dis15
    d "Let's get it over with."
    show ed 81
    mc "Oh yes, finally..."
    mc "Are you wearing a bra?"
    show ed 80
    d "You know I'm not."
    show ed 81
    mc "Oh dear..."
    show ed 80
    d "Why are you so excited? You've seen me naked already."
    show ed 81
    mc "Seeing a girl like you naked will always be as exciting as the first time."
    mc "You wouldn't understand."
    d "Hmm."
    play sound clothes3
    show ed 82 with dis15
    bla "Dalia slowly opens her shirt, revealing her nicely shaped breasts and her well-toned abdomen to you."with dis
    mc "WHOA..."
    show ed 84
    mc "You always leave me speechless..."with dis12
    d "Mm-hm."
    mct "God, her tummy is so fucking sexy..."
    d ". . ."
    d "(Why is him looking at my body with such lewdness turning me on?)"
    d "(Why am I enjoying this?)"
    d "(I'm enjoying losing a game!)"
    d "(Am I giving up my principles...?)"
    play sound clothes3
    play soundlow wood fadein 2
    show ed 84b with dis14
    d "W-What are you doing?!" with dis06
    show ed 85
    mc "You said I'd get to lick your abs if I won."
    show ed 84b
    d "W-What? For real? I thought you were kidding."
    show ed 85
    mc "Kidding? I've been fantasizing about it since I saw you in all your glory that day in your beach."
    show ed 84b
    d "Um..."
    d "Well, o-okay, I guess."
    d "If it's part of the game..."
    d "B-But be quick."
    show ed 86 
    mc "Of course..." with dis12
    bla "You can feel Dalia's whole body shuddering and her sparse, blonde body hair standing on end the moment you touch her stomach."
    d "Hmph!"
    mc "You okay?"
    d "Y-Yeah, you just... tickled me."
    scene daliawest1 with dis2
    bla "You start licking Dalia's stomach, taking pleasure in each one of her body's involuntary reactions."with dis
    mct "Man... I'd eat her whole if I could."
    mct "Her smell is incredible."
    mct "We've been riding a horse for hours, drinking some weird homemade booze, but her own scent covers it all somehow."
    d "(God, this is awkward.)"
    d "(Very awkward.)"
    d "(Incredibly awkward.)"
    d ". . ."
    d "(Why...)"
    d "(Why is it turning me on, then...?)"
    d "(Goddammit, Dalia...)"
    d "(I better stop it before... I...)" 
    play sound clothes2
    show ed 88
    d "O-Okay, this is enough."with dis08
    d "You had your fun embarrassing me already."
    play sound2 clothes3
    play sound6 wood fadein 2
    show ed 90
    mc "*Standing up* Certainly. But I've gotta say, you taste really good."with dis15
    show ed 89
    d "*Snorts* If you say so."
    show ed 90
    mc "Did you enjoy it too?"
    mc "I don't remember seeing your nipples so hard when we started."
    show ed 91
    d "*Giggles* Oh, shut up and let's continue playing."
    show ed 89
    d "Although... I only have my panties left to lose, so I don't think the game is gonna last."
    show ed 90
    mc "Oh, do you accept your defeat?"
    show ed 91
    d "Yeah, yeah, you win. You're way better than me at darts."
    d "Happy?"
    show ed 90
    mc "Well... since it's the last round... we can raise the stakes a little."
    mc "What about..."
    show ed 91
    d "*Imitating your voice* {i}If I win, I get another blowjob..."
    show ed 89
    d "Something like that?"
    show ed 90
    mc "Um..."
    play sound clothes3
    show ed 92
    d "*Taking her shirt off* We know each other pretty well already, [mc]." with dis15
    show ed 93
    mct "Jesus Christ, look at that body..."
    show ed 92
    d "You're... predictable. Especially when you're horny."
    show ed 93
    mc "So..."
    show ed 92
    d "Yeah, no."
    d "As I said, it's obvious that you're better than me."
    show ed 93
    mc "Then I'll throw the dart with the gloves on, to even the odds. That makes it way more difficult."
    d "Hmm."
    show ed 92
    d "And... you have to throw it with your eyes closed."
    show ed 93
    mc "What?!"
    show ed 92
    d "And... if I win... it's YOU who has to give ME head."
    show ed 93
    mc "Wha–"
    mct "Oh my god."
    mct "OH GOD. Calm down, [mc]." 
    mct "Don't let her see that it's a win-win for you no matter what."
    mc "Um... a-alright. Seems fair."
    show ed 92
    d "Good, then."
    d "I go first."
    show ed 93
    mc "Now THE GAME is on."
    show ed 94 with dis15
    d "Hmm..." with dis06
    d "(I can't believe I really asked him to go down on me. Alex is such a bad influence, I shouldn't listen to her.)"
    d "(And I can't believe I actually got horny enough to ask him to do that either. Alcohol is also a bad influence.)"
    d "(I should stick to the irons. They'd never betray me.)"
    mc "In another situation I'd probably rush you, but I'm enjoying the view too much for that."
    show ed 58
    d "O-Oh, yeah, sorry!"
    d "*Taking a deep breath* Here I go."
    play sound dart
    show ed 95 with hpunch
    pause .2
    d "Oh!"with dis06
    d "OHH!" 
    show ed 96
    d "YAY! I told you I had gotten the hang of it!"with hpunch 
    d "BULLSEYE!"with hpunch
    mc "Don't celebrate ahead of time..."
    show ed 95
    d "Come on! Have you seen that?! It's literally at the center!"
    mc "Just watch and see..."
    show ed 97
    bla "Dalia snorts playfully, handing you a dart and carefully watching you to ensure you don't open your eyes." with dis12
    scene ed 95
    mc "*Taking a deep breath* Let me calculate the effect of the wind..."with dis
    play sound3 glitch4
    scene dartglitch
    pause
    play sound dart
    show ed 98 with hpunch
    pause .2
    d "W-WHAT?!" with dis06
    d "What the hell?!" with hpunch
    mc "Can I open my eyes now?"
    d "How the fuck did you do that?!"
    mc "Oh, bullseye!"
    show ed 99
    d "*Giggles* Don't bullshit me, you cheated!" with dis12
    show ed 98c
    mc "No, I didn't!"
    show ed 99
    d "You used your powers!"
    show ed 98c
    mc "I used all my {i}skills{/i} available."
    mc "That's not cheating in my books."
    show ed 99
    d "Hah! I should have established the rules earlier."
    show ed 98c
    mc "Well... I guess it's a tie."
    mc "Should we throw again?"
    d "Hmm..."
    show ed 98d
    d "Either that, or..."
    show ed 99
    d "*Giggles* Nah, forget it. I'm getting carried away."
    show ed 98c
    mc "I want you to get carried away so bad, Dalia..."
    mc "Let's just say what crosses our minds."
    mc "Full transparency."
    mc "We're in a cabin in the middle of nowhere, who cares?"
    show ed 98d
    d "Erm..."
    d "I guess... you got a point."
    show ed 98c
    mc "What did you think about?"
    show ed 98d
    d "Well... it's just that..."
    d "Since we both “won”..."
    d "What about... breaking the tie with one last challenge?"
    show ed 99
    d "*Giggles playfully* I can't believe I'm the one suggesting this and not you."
    d "I'll admit that I'm a bit turned on right now."
    show ed 98c
    mc "Please, tell me you're suggesting a 69..."
    show ed 98d
    d "I mean... with what we already did at The Cove server..."
    d "It's not... weird, right?"
    show ed 99
    d "Is it weird?"
    show ed 98c
    mc "Absolutely not."
    show ed 99
    d "So I thought..."
    d "The first one to make the other cum... wins?"
    play sound clothes2
    play sound2 buttons
    show ed 100
    bla "You rip your shirt off and roughly pull Dalia towards you. She doesn't resist at all." with dis 
    mc "Fuck, you have no fucking idea of how much you're turning me on right now, Dalia."
    show ed 100b
    d "Easy win for me, then."
    show ed 100
    mc "Hell no, I'm gonna eat your pussy so raw that you're gonna cum in 10 seconds."
    show ed 100b
    d "Now it's you who's being overly confident, [mc]..."
    show ed 100
    mc "Have I told you how fucking much I love your competitive side?"
    show ed 100b
    d "*Giggles* I bet you'll like it even more now..."
    play sound fall2
    play soundlow ["<silence 0.3>", woodhit]
    show ed 101
    bla "Dalia pushes you to the ground, positioning herself above you, with her legs on either side."with dis12
    show ed 102
    mc "Oh my goodness gracious..." with dis12
    mc "Take off your panties..."
    play sound clothes2
    show ed 103 with dis
    mc "Oh Jesus..."with dis06
    play soundlow clotheswhoosh volume 0.6
    play sound2 woodhit volume 0.5
    scene ed 103b
    bla "You grab Dalia by her huge buttocks and pull her to the ground. You open her ass cheeks, exposing her swollen, already wet pussy."with dis 
    mct "Oh man, this is happening..."
    scene ed 104
    d "(Oh shit. It is happening.)"
    d "(I'm doing a 69.)"
    d "(With [mc].)"
    show ed 103b
    mc "Fuck, I can't wait any longer..."
    play sound bodycollide
    play sound2 bodycollide
    play sound3 blow4
    scene ed 105
    bla "Without giving her a second to breathe, you start attacking Dalia's swollen lips." with dis 
    d "Hmph!"with hpunch
    show ed 106
    d "Hmmmmhhh...." with dis14
    show ed 107
    d "(Holy fuck, he's not wasting a second...)"with dis12
    d "*Moaning* Mmmm..."
    d "(And that feels good...)"
    play sound belt
    show ed 108 with dis15
    d "*Pulling your trousers down* (You've gotta keep up your game, Dalia...)"with dis06
    stop sound fadeout 1
    $ renpy.music.set_volume(0.3, delay=10.0, channel='music3')
    play soundloop blowjob2 fadein 3
    scene daliawest2 with dis22
    d "Mmmm..."with dis08
    mct "Oh my goooooddd..."
    d "*Moaning* Mmmm..."
    bla "You feel your dick head disappear inside of Dalia's mouth, even though you can't actually see it."
    mct "My god..."
    bla "You get fully erect in a matter of seconds, as she quickly covers your cock in saliva."
    mct "I can't even concentrate properly on her..."
    mct "She's not only sucking my cock... the things she does with her tongue... she moves it in circles like a swirling vortex while she moves up and down."
    mct "This is not gonna last long..."
    d "Mmmmmm..."
    d "(Fuck... this is absolutely amazing...)"
    d "(This is so fucking hot.)"
    d "(I want this to last forever...)"
    d "(But you've gotta win, Dalia.)"
    d "(I have to squeeze him to the fullest...)"
    pause
    play soundloop2 blowjob2faster fadein 2
    stop soundloop fadeout 1
    scene daliawest3 with dis2
    bla "Almost as if you could read each other's thoughts, you two up your pace at the same time, decided to make the other cum first." with dis
    mct "OH GOD."
    d "(OH JESUS...)"
    mct "Shit, I'm gonna cum too fast..."
    d "(Fuck, I'm gonna cum...)"
    d "(I'm not used to this sensation, it's not fair...)"
    if calypsohandjob:
        mct "You just lost your battle of power against Calypso, [mc]."
        mct "You can't lose here too..."
        mct "But..."
        mct "Fuck, Dalia's technique is just too fucking goooood...."
    else:
        d "Mmmmmh..."
    d "(I am enjoying sucking his cock as much as him eating my pussy...)"
    d "(What the hell is wrong with me...)"
    scene daliawest4 with dis2
    bla "After spending a few minutes in complete silence, only interrupted by Dalia's moans and whimpers, you start to feel the climax really close." with dis 
    mct "Shit, this is amazing..."
    bla "You lick up and down her perfectly shaved pussy and press your tongue in as far as you can get it."
    d "Mmmmh..."
    d "*Moaning more intensely* MMMmmm!!"
    mc "She's also close..."
    pause 
    play sound blow4
    stop soundloop2 fadeout 1
    show ed 109
    d "*Catching her breath* AAAaaaagh!"with dis
    d "F-FUCK, [mc!u]..."
    mc "Oh, Dalia..."
    d "You're not gonna win..."
    mc "It's you who won't be able to–"
    play soundloop deepthroat fadein 2
    scene daliawest5 with dis2
    mct "OH MY GOD."with dis
    bla "You suddenly feel your cock completely penetrating Dalia's throat, forcing you to stop your task for a second."
    mct "OH FUCK."
    mct "There's no way on earth she's doing that with her mouth..."
    mct "My god....."
    mct "How the hell can she take it so deep??"
    mct "Her throat offers no resistance at all..."
    mct "As if it lets me stretch it at will..."
    mct "O-O-Ohh shit I'm gonna cum."
    mct "Come on, [mc], make her cum first!"
    mct "Suck her clit."
    mct "You can do it..."
    menu:
        with dis
        "Cum":
            mct "OH SHIT."with dissolve
            mct "I CAN'T–"
            stop soundloop
            play sound cum2
            play sound2 cum3
            play sound3 cum4
            scene ed 110
            mc "*Cumming inside Dalia's throat* AAAAAAAAARGHHHHH...."with vpunch  
            play sound cum2
            play sound2 cum3
            play sound3 cum4
            scene ed 110b
            mc "AAAAAHH YEAaahhh..." with vpunch 
            play sound cum2
            play sound2 cum3
            play sound3 cum4
            $ renpy.music.set_volume(0.5, delay=20.0, channel='music3')
            scene ed 111
            mc "*Still cumming* Oo-Ohhhh..." with vpunch
            mc "F-Fuck yes..."
            mc "Take it all, babe..."
            play sound blow2
            d "*Swallowing* MMMMmmmmhh..."
            mc "Good girl..."
            mc "You like that, don't you?"
            d "*Assertively* Mm-hmm..."
            play sound2 blowpop
            show ed 109 with dis17
            bla "Dalia laps every last bit of cum, skillfully licking your cock until it gleams, leaving not a trace behind."with dis06
            d "F-Fuck... you're gonna make me develop a fetish for this..."
            mc "Yes, please..."
            play sound clothes5
            play sound4 chair2
            show ed 112 with dis2
            d "*Rolling onto her side and clumsily standing up* A-Anyways... I think t-this is a v-victory!"with dis
            mc "I've never been happier to lose a game."
            mc "That was simply too much for me to handle..."
            show ed 114
            d "It really was... my jaw hurts." with dis
            mc "When it comes to this, you're a goddess..."
            show ed 112
            d "*Giggles* T-Thanks." with dis
            $ renpy.end_replay()
        "Make her cum first":
            mct "Oh fuck..."with dissolve
            menu:
                with dis
                "{size=35}Cum":
                    mct "OH SHIT."with dissolve
                    mct "I CAN'T–"
                    stop soundloop
                    play sound cum2
                    play sound2 cum3
                    play sound3 cum4
                    scene ed 110
                    mc "*Cumming inside Dalia's throat* AAAAAAAAARGHHHHH...."with vpunch  
                    play sound cum2
                    play sound2 cum3
                    play sound3 cum4
                    scene ed 110b
                    mc "AAAAAHH YEAaahhh..." with vpunch 
                    play sound cum2
                    play sound2 cum3
                    play sound3 cum4
                    $ renpy.music.set_volume(0.5, delay=20.0, channel='music3')
                    scene ed 111
                    mc "*Still cumming* Oo-Ohhhh..." with vpunch
                    mc "F-Fuck yes..."
                    mc "Take it all, babe..."
                    play sound blow2
                    d "*Swallowing* MMMMmmmmhh..."
                    mc "Good girl..."
                    mc "You like that, don't you?"
                    d "*Assertively* Mm-hmm..."
                    play sound2 blowpop
                    show ed 109 with dis17
                    bla "Dalia laps every last bit of cum, skillfully licking your cock until it gleams, leaving not a trace behind."with dis06
                    d "F-Fuck... you're gonna make me develop a fetish for this..."
                    mc "Yes, please..."
                    play sound clothes5
                    play sound4 chair2
                    show ed 112 with dis2
                    d "*Rolling onto her side and clumsily standing up* A-Anyways... I think t-this is a v-victory!"with dis
                    mc "I've never been happier to lose a game."
                    mc "That was simply too much for me to handle..."
                    show ed 114
                    d "It really was... my jaw hurts." with dis
                    mc "When it comes to this, you're a goddess..."
                    show ed 112
                    d "*Giggles* T-Thanks." with dis
                    $ renpy.end_replay()
                "Make her cum first":
                    play sound7 beat
                    mct "Oh my my fucking god..."with dissolve  
                    menu:
                        with dis
                        "{size=40}Cum":
                            mct "OH SHIT."with dissolve
                            mct "I CAN'T–"
                            stop soundloop
                            play sound cum2
                            play sound2 cum3
                            play sound3 cum4
                            scene ed 110
                            mc "*Cumming inside Dalia's throat* AAAAAAAAARGHHHHH...."with vpunch  
                            play sound cum2
                            play sound2 cum3
                            play sound3 cum4
                            scene ed 110b
                            mc "AAAAAHH YEAaahhh..." with vpunch 
                            play sound cum2
                            play sound2 cum3
                            play sound3 cum4
                            $ renpy.music.set_volume(0.5, delay=20.0, channel='music3')
                            scene ed 111
                            mc "*Still cumming* Oo-Ohhhh..." with vpunch
                            mc "F-Fuck yes..."
                            mc "Take it all, babe..."
                            play sound blow2
                            d "*Swallowing* MMMMmmmmhh..."
                            mc "Good girl..."
                            mc "You like that, don't you?"
                            d "*Assertively* Mm-hmm..."
                            play sound2 blowpop
                            show ed 109 with dis17
                            bla "Dalia laps every last bit of cum, skillfully licking your cock until it gleams, leaving not a trace behind."with dis06
                            d "F-Fuck... you're gonna make me develop a fetish for this..."
                            mc "Yes, please..."
                            play sound clothes5
                            play sound4 chair2
                            show ed 112 with dis2
                            d "*Rolling onto her side and clumsily standing up* A-Anyways... I think t-this is a v-victory!"with dis
                            mc "I've never been happier to lose a game."
                            mc "That was simply too much for me to handle..."
                            show ed 114
                            d "It really was... my jaw hurts." with dis
                            mc "When it comes to this, you're a goddess..."
                            show ed 112
                            d "*Giggles* T-Thanks." with dis
                            $ renpy.end_replay()
                        "Make her cum first":
                            play sound7 beat
                            bla "{w=0.3}{nw}"with hpunch
                            menu:
                                with dis
                                "{size=65}Cum":
                                    mct "OH SHIT."with dissolve
                                    mct "I CAN'T–"
                                    stop soundloop
                                    play sound cum2
                                    play sound2 cum3
                                    play sound3 cum4
                                    scene ed 110
                                    mc "*Cumming inside Dalia's throat* AAAAAAAAARGHHHHH...."with vpunch  
                                    play sound cum2
                                    play sound2 cum3
                                    play sound3 cum4
                                    scene ed 110b
                                    mc "AAAAAHH YEAaahhh..." with vpunch 
                                    play sound cum2
                                    play sound2 cum3
                                    play sound3 cum4
                                    $ renpy.music.set_volume(0.5, delay=20.0, channel='music3')
                                    scene ed 111
                                    mc "*Still cumming* Oo-Ohhhh..." with vpunch
                                    mc "F-Fuck yes..."
                                    mc "Take it all, babe..."
                                    play sound blow2
                                    d "*Swallowing* MMMMmmmmhh..."
                                    mc "Good girl..."
                                    mc "You like that, don't you?"
                                    d "*Assertively* Mm-hmm..."
                                    play sound2 blowpop
                                    show ed 109 with dis17
                                    bla "Dalia laps every last bit of cum, skillfully licking your cock until it gleams, leaving not a trace behind."with dis06
                                    d "F-Fuck... you're gonna make me develop a fetish for this..."
                                    mc "Yes, please..."
                                    play sound clothes5
                                    play sound4 chair2
                                    show ed 112 with dis2
                                    d "*Rolling onto her side and clumsily standing up* A-Anyways... I think t-this is a v-victory!"with dis
                                    mc "I've never been happier to lose a game."
                                    mc "That was simply too much for me to handle..."
                                    show ed 114
                                    d "It really was... my jaw hurts." with dis
                                    mc "When it comes to this, you're a goddess..."
                                    show ed 112
                                    d "*Giggles* T-Thanks." with dis
                                    $ renpy.end_replay()
                                "Make her cum first":
                                    play sound7 beat
                                    bla "{w=0.3}{nw}"with hpunch
                                    menu:
                                        with dis
                                        "{sc=2}{size=85}Cum{/sc}":
                                            mct "OH SHIT."with dissolve
                                            mct "I CAN'T–"
                                            stop soundloop
                                            play sound cum2
                                            play sound2 cum3
                                            play sound3 cum4
                                            scene ed 110
                                            mc "*Cumming inside Dalia's throat* AAAAAAAAARGHHHHH...."with vpunch  
                                            play sound cum2
                                            play sound2 cum3
                                            play sound3 cum4
                                            scene ed 110b
                                            mc "AAAAAHH YEAaahhh..." with vpunch 
                                            play sound cum2
                                            play sound2 cum3
                                            play sound3 cum4
                                            $ renpy.music.set_volume(0.5, delay=20.0, channel='music3')
                                            scene ed 111
                                            mc "*Still cumming* Oo-Ohhhh..." with vpunch
                                            mc "F-Fuck yes..."
                                            mc "Take it all, babe..."
                                            play sound blow2
                                            d "*Swallowing* MMMMmmmmhh..."
                                            mc "Good girl..."
                                            mc "You like that, don't you?"
                                            d "*Assertively* Mm-hmm..."
                                            play sound2 blowpop
                                            show ed 109 with dis17
                                            bla "Dalia laps every last bit of cum, skillfully licking your cock until it gleams, leaving not a trace behind."with dis06
                                            d "F-Fuck... you're gonna make me develop a fetish for this..."
                                            mc "Yes, please..."
                                            play sound clothes5
                                            play sound4 chair2
                                            show ed 112 with dis2
                                            d "*Rolling onto her side and clumsily standing up* A-Anyways... I think t-this is a v-victory!"with dis
                                            mc "I've never been happier to lose a game."
                                            mc "That was simply too much for me to handle..."
                                            show ed 114
                                            d "It really was... my jaw hurts." with dis
                                            mc "When it comes to this, you're a goddess..."
                                            show ed 112
                                            d "*Giggles* T-Thanks." with dis
                                            $ renpy.end_replay()
                                        "Make her cum first":
                                            play sound7 beat
                                            bla "{w=0.3}{nw}"with hpunch
                                            menu:
                                                with dis
                                                "{sc=4}{size=115}Cum{/sc}":
                                                    mct "OH SHIT."with dissolve
                                                    mct "I CAN'T–"
                                                    stop soundloop
                                                    play sound cum2
                                                    play sound2 cum3
                                                    play sound3 cum4
                                                    scene ed 110
                                                    mc "*Cumming inside Dalia's throat* AAAAAAAAARGHHHHH...."with vpunch  
                                                    play sound cum2
                                                    play sound2 cum3
                                                    play sound3 cum4
                                                    scene ed 110b
                                                    mc "AAAAAHH YEAaahhh..." with vpunch 
                                                    play sound cum2
                                                    play sound2 cum3
                                                    play sound3 cum4
                                                    $ renpy.music.set_volume(0.5, delay=20.0, channel='music3')
                                                    scene ed 111
                                                    mc "*Still cumming* Oo-Ohhhh..." with vpunch
                                                    mc "F-Fuck yes..."
                                                    mc "Take it all, babe..."
                                                    play sound blow2
                                                    d "*Swallowing* MMMMmmmmhh..."
                                                    mc "Good girl..."
                                                    mc "You like that, don't you?"
                                                    d "*Assertively* Mm-hmm..."
                                                    play sound2 blowpop
                                                    show ed 109 with dis17
                                                    bla "Dalia laps every last bit of cum, skillfully licking your cock until it gleams, leaving not a trace behind."with dis06
                                                    d "F-Fuck... you're gonna make me develop a fetish for this..."
                                                    mc "Yes, please..."
                                                    play sound clothes5
                                                    play sound4 chair2
                                                    show ed 112 with dis2
                                                    d "*Rolling onto her side and clumsily standing up* A-Anyways... I think t-this is a v-victory!"with dis
                                                    mc "I've never been happier to lose a game."
                                                    mc "That was simply too much for me to handle..."
                                                    show ed 114
                                                    d "It really was... my jaw hurts." with dis
                                                    mc "When it comes to this, you're a goddess..."
                                                    show ed 112
                                                    d "*Giggles* T-Thanks." with dis
                                                    $ renpy.end_replay()
                                                "Make her cum first":
                                                    play sound7 beat
                                                    d "MMMMmmH!" with hpunch 
    $ renpy.music.set_volume(0.5, delay=12.0, channel='music3')
    stop soundloop
    play sound cum4
    play sound2 slap1
    scene ed 113
    d "AAaaaagggghhghghhhh..." with hpunch 
    mct "Yes!"
    play sound3 cum4
    bla "Dalia orgasms, squeezing her legs together with astonishing force, and covering you in her juices." with hpunch  
    d "H-H-Holy fuck, [mc]..."
    d "Y-You son of a b-biiitch..."
    mc "I-I can't breathe..."
    play sound clothes5
    play sound4 chair2
    show ed 114 with dis2
    d "*Rolling onto her side and clumsily standing up* Lord have mercy..."with dis
    d "That was... WOW."
    d "I have trouble standing upright."
    d "I've never been happier to lose in a game in my life."
    play sound2 tablehit
    show ed 115
    bla "You grab Dalia's butt and you turn her around, slamming her against the table." with dis
    mc "I swear this booty of yours should be worshiped, Dal."
    show ed 116
    d "I don't know what you're trying to do, but I can still smack your face, you know?"with dis12
    d "Get off me."
    show ed 117
    mc "I just want to cum with you... take it as my prize for winning."
    show ed 116
    d "We're not gonna f-fuck."
    d "A-And I'm not giving you more head. My jaw hurts."
    d "Just t-take your victory home."
    show ed 117
    mc "I just wanna finish using these glorious ass cheeks of yours..."
    show ed 116
    d "My... ass cheeks?"
    show ed 117
    mc "Yeah, just..."
    $ renpy.music.set_volume(0.35, delay=12.0, channel='music3')
    $ renpy.music.set_volume(0.45, channel='soundloop2')
    play soundloop2 daliawest6 fadein 2 
    scene daliawest6 with dis2
    mc "Like this..." with dis 
    d "AAahh..."
    bla "You use Dalia's dripping juices to lubricate her own buttocks and use them as your personal toy, sliding your cock between them with ease."
    mc "Oh fuck yes..."
    mct "Dalia's ass is so huge... it almost envelops my entire cock."
    mct "And I love how soft it feels when she's not flexing it..."
    mct "If I close my eyes it almost feels as if I was fucking her..."
    bla "Dalia lets out a soft moan each time your cock rubs against her swollen, still sensitive pussy."
    d "Aaahhh..."
    mc "Oh babe..."
    stop soundloop2 fadeout 2
    play soundloop daliawest7 fadein 2
    scene daliawest7 with dis2
    bla "Almost unconsciously, you increase your pace, slamming your hips against Dalia's." with dissolve 
    mc "OH FUCK YES..."
    d "AAahh..."
    mc "God, Dalia..."
    mc "Everything about your body is so perfect..."
    mc "Firm and tight in all the right places... and irresistibly soft where it's meant to be..."
    mc "You drive me insane..."
    d "AAaahh..."
    mc "I wanna fuck you so bad..."
    mc "I want to bone you until neither of us can walk straight..."
    d "AAahh..."
    d "Not..."
    d "N-Not now. Not here..."
    mc "Does that mean... that you want me to fuck you another day...?"
    d "I..."
    d "M-Maybe in... another s-situation."
    d "Now s-shut up and hit me harder..."
    mc "Oh babe..."
    $ menudjdbdf = True
    $ daliaslapwestern = False
    menu:
        with dis
        "Slap her ass":
            $ daliaslapwestern = True
            stop soundloop fadeout 2
            play sound6 rubbody
            scene daliawest8 with dis12
            pause 0.4
            play sound slap3
            play sound2 slap1
            play sound3 slap3
            pause .2
            d "AAAAahhggg....{w=1.1}{nw}" with dissolve
            scene ed 126
            d "Mmmmmhm..."with dis12
            mc "Was it too much? Did I hit you too hard?"
            d "N-No... it's okay..."
            mc "Tough girl..."
            play soundloop daliawest7 fadein 2
            scene daliawest10 with dis15
            d "AAaaahh..." with dissolve
            mc "Fuck, you have such a sensitive skin, it's already all red..."
            d "*Playfully moaning* Mm-hm..."
            mc "You {i}did{/i} love that, right, you naughty girl?"
            d "F-Fuck yes..."
            mc "Oh boy..."
            mc "So you like it rough, eh...?"
            if penelopepath:
                d "*Giggles* I d-don't know... m-maybe."
                mc "Just like her sis... interesting."
                mc "I guess it's in the genes..."
                d "Eh...? Penny?"
                mc "Yeah... she drank Veritaserum when we went to the Warthogs server and she admitted to... liking it rough."
                d "Hah..."
                d "I knew it."
                mc "Fuck, this feels so good, Dalia..."
                d "I..."
                d "I c-can take it harder than her."
                mc "Huh...?"
                d "I-I'm sure I can take it WAY harder than Penny..."
                mc "Oh god..."
                d "Spank me harder..."
                mc "Oh baby..."
            else:
                d "Fuck, I guess I do..."
            menu spankdaliareplay:
                with dis
                "Spank her again":
                    stop soundloop fadeout 2
                    play sound6 rubbody
                    scene daliawest9 with dis12
                    pause 0.4
                    play sound slap3
                    play sound2 slap1
                    play sound3 slap3
                    pause .2
                    d "AAAAahhggg....{w=1}{nw}" with dissolve
                    play soundloop daliawest7 fadein 2
                    if menudjdbdf:
                        scene daliawest11 with dis15
                    else:
                        scene daliawest10 with dis15
                    d "Mmmmmmm..."with dissolve
                    if menudjdbdf:
                        $ menudjdbdf = False
                        d "(Shit... I really like this...)"
                        d "(What is wrong with me...)"
                        d "(I love how he's slamming his hips against mine...)"
                        d "(How his balls pound my pussy with each thrust...)"
                        d "*Moaning* Mmmm..."
                        d "(God, he's so strong.)"
                        d "(I almost would like to...)" 
                        d "(Do I really want [mc] to... fuck me?)"
                        d "(Fuck, who am I kidding, OF COURSE I DO...)"
                        d "(He's... the one...)"
                        d "MMMmmmmmmmhhmmm..."
                    jump spankdaliareplay
                "Continue the butt job":
                    mc "Aaagh fuck yes..." with dissolve
        "Continue the butt job":
            mc "Aaagh fuck yes..." with dissolve
    mc "*Panting* Shit, I'm almost there..."
    mc "I'm g-gonna cum, Dalia..."
    stop soundloop fadeout 1
    play sound rubbody
    play sound2 wood
    scene ed 129
    bla "Dalia gracefully lifts her legs and rolls over, settling on her back with poise."with dis15
    mc "Fuck, Dalia, you're not gonna leave me hanging now, right...?"
    mc "I don't even know how I've managed to last for so long..."
    show ed 128
    d "I want you to finish on... my face. Not on my back."
    show ed 129
    mc "Do you want... a facial?"
    play sound rubbody
    play soundlow wood volume 0.4
    if daliaslapwestern:
        scene ed 130
    else:
        scene ed 130b
    d "Is that okay...?"with dis12
    if daliaslapwestern:
        scene ed 131
    else:
        scene ed 131b
    mc "What kind of question is that?"
    mc "Come here..."
    show ed 132
    bla "You get closer to Dalia and after so long, it only takes you a couple of strokes to unload everything you've been holding in." with dis12
    play sound cum2
    play sound2 cumall
    play sound3 cum4
    scene ed 133
    mc "AAAAAAAAARGHHHHH...."with hpunch 
    play sound cum2
    play sound2 cumall
    play sound3 cum4
    mc "FUCK YESSS..."with hpunch
    show ed 134
    mc "Oh my fucking god..." with dis12
    mc "I left my balls empty..."
    d "I can see that..."
    show ed 135
    d "AAaahh..." with dis14
    mc "Oh Lord, Dalia..."
    play sound blow6
    show ed 136
    bla "Dalia leans forward and starts skillfully polishing your cock head, swallowing it all and not leaving a trace of cum behind." with dis14
    play sound6 blow2
    d "*Swallowing* MMMMmmmmhh..."
    play sound2 blowpop
    show ed 137 with dis17
    mc "O-O-Oh my god..."with dis06
    mc "You're gonna end up developing a fetish for swallowing my cum..."
    d "*Giggles* If I don't have it already..."
    mc "Good grief..."
    mc "Each thing you say makes me obsess more about you."
    d "I hope you enjoyed the... competition."
    d "I certainly did... even if I lost."
    mc "I'd say it's been more of a tie."
    d "*Giggles* Yeah. I like that better..."
    play sound chair2
    play sound5 clothes3
    if daliaslapwestern:
        show ed 138b
    else:
        show ed 138
    bla "Dalia comes down from the table and grabs a rag from the kitchen to clean her face." with dis15
    if daliaslapwestern:
        d "Damn, my butt is burning like hell."
        d "I bet you left a mark."
        mc "A mark...?"
        mc "Maybe a bit. You can hardly see it."
        d "*Giggles* You're a terrible liar, [mc]."
    else:
        d "*Sniffing the rag* This is an... intense smell."
        mct "She's a devious freak... I love it."
    $ renpy.end_replay()

label ga_side3:
    play music2b calypsolewd fadein 6
    scene calywest1 with dis17
    pause 8.5
    scene eec 55 
    mc "Oh sweet lord..."with dis
    mct "Look at that body..."
    mct "My god, her breasts are absolutely perfect, just as I imagined."
    mc "I can't believe I'm seeing this."
    play sound water
    show eec 58 with dis12
    ca "*Sitting on the corner of the tub* Yes... I cannot believe I am letting you see it either."with dis06
    ca "Maybe all this time spent among commoners is muddying my temperament."
    show eec 56
    mc "Ah... you ended up becoming fond of me, didn't you?"
    show eec 57
    ca "I ended up taking pity on you, more like."
    ca "This is what you were yearning for, so... I suppose I can grant you that wish."
    show eec 56
    mc "And it's even better than I imagined... I officially release you from your debts."
    show eec 58
    ca "Remember, you must keep your mouth shut."
    ca "If word gets out that I revealed myself to my human squire, it would ruin my reputation... for a few decades at least."
    show eec 56
    mc "My lips are sealed, my Princess."
    show eec 57
    ca "They better be."
    ca "I am committing quite a sacrilege here."
    ca "My old Tutor of Elegance and Virtue would be horrified if she discovered I'm doing this."
    show eec 56
    mc "God, everything you say excites me more..."
    mc "Don't you feel the same?"
    show eec 57
    ca "Hmph. What I feel is... contradiction."
    ca "Many Lords in Hyril'ar would surrender all their possessions just to see what you are seeing right now, you know?"
    ca "And here I am... showing myself in my purest form to a mere mortal."
    show eec 56
    mct "She keeps insisting on that, but her subtle smirk tells a different story. I can tell she's taking pleasure in breaking her royal protocols..."
    mc "Don't worry, it'll be our secret."
    mc "And besides, I didn't even touch you, so... no purity or virtue was lost."
    mc "Unless..."
    show eec 57
    ca "Hah, you better not continue that sentence."
    play sound water
    play sound2 wood fadein 1
    show eec 59 with dis14
    ca "*Standing up* No human has ever touched me, and none ever will."with dis
    ca "That is a line I will never cross."
    mc "What if it's you who touches me instead...?"
    show eec 61
    ca "Same thing applies."with dis12
    show eec 60
    mc "I see... that's too bad."
    mc "I'll use the few seconds I have left to admire your beauty a bit more, then."
    ca "Hmm."
    mct "Jesus, she really has a spectacular body."
    mct "Is it bad that I want to grab the Princess and completely {i}destroy{/i} her against that rotten cabinet? Might as well make even more of a mess in here..."
    mct "My god, my pants are about to explode."
    show eec 61
    ca "Well, now it is your turn to get undressed."
    show eec 60
    mc "I'm sorry?"
    show eec 62
    ca "What do you mistake me for, some kind of common harlot who gets naked without reciprocation? Nonsense!"with dis08
    ca "You need to undress for me as well."
    show eec 60
    mc "I thought you were granting my wish."with dis08
    show eec 62
    ca "And I still am."with dis08
    ca "You are forgetting who you are dealing with, [mc]. I am an heir to the Hyril’ar Realm and there are different protocols with me."
    show eec 60
    mc "That's a fair point, I guess."with dis08
    mct "She really wants to keep a high profile all the time, eh? To keep her superior social status in check."
    mct "Alright, I can play her game."
    mct "I've never been one to feel ashamed of my physique, and now that I look even more muscular, it only strengthens my confidence."
    mc "Very well."
    mc "Your wish is my command, my Princess."
    play sound belt
    show eec 63
    bla "You slowly begin to undress while Calypso gazes at you."with dis15
    play sound2 clothes4
    play sound3 clothes3
    show eec 64 with dis15
    pause .3
    mct "Dammit... I thought that if I took my time undressing, my erection would go away." with dis12
    mct "This might be awkward..."
    show eec 66
    ca ". . ." with dis12
    play sound5 clothes
    mc "*Finishing undressing* Well... it's done. Equal conditions."
    show eec 67
    ca "Holy Mother of Turska... what is that??"with dis12
    show eec 68
    mc "Um..."with dissolve
    mc "Yeah... s-sorry about that. I know erections are probably... out of protocol."
    mc "I couldn't help it."
    show eec 67
    ca "I mean..."with dissolve
    ca "You are ... better-endowed than what I imagined."
    ca "Are you... half-orc, perhaps?"
    show eec 68
    mc "Um... nope, only human."with dissolve
    show eec 67
    ca "Are you sure?"with dissolve
    show eec 68
    mc "Yeah, pretty sure. No orcs in my family that I know of."with dissolve
    show eec 67
    ca "I see..."with dissolve
    mct "God, her short glances to my cock are turning me on so much..."
    show eec 68
    mc "You seem quite enthralled by my naked body, Princess."with dissolve
    mc "Isn't your gaze upon my intimate areas also a breach of protocol?"
    show eec 69
    ca "P-Please, I am not e-enthralled by anything."
    ca "Although... I will admit that the whole situation is {i}certainly{/i} out of protocol, yes."
    show eec 68
    mc "You can look at it. I don't mind, really."
    show eec 69
    ca "I have looked at it enough."
    ca "I was just surprised because... it doesn't match your skinny physique, that is all."
    show eec 68
    mc "Hey, I'm not skinny!"
    show eec 69
    ca "Please... Hyril'ar elite guards probably weigh twice as much as you."
    ca "{i}That{/i} is a strong male."
    show eec 68
    mc "But muscles don't always equal strength. I'm likely stronger than them."
    show eec 69
    ca "I highly doubt it."
    ca "General Arannis once carried me all the way back to the castle from the Eldermoor Huntlands when my horse ran away."
    show eec 68
    mc "I don't know how far that is to the castle, but I'm sure I could do that too."
    show eec 69
    ca "*Huffing* If you say so..."
    ca "I will keep it in mind if we ever find ourselves in a similar situation."
    show eec 68
    mc "I'd be happy to show you how strong and vigorous I can be..."
    show eec 70
    ca "You know, I decided to tolerate your indecent innuendos given the situation we are in since they're almost... endearing."with dis12
    ca "But I must warn you, they are about as futile as a dwarf's attempt to outrun an elven archer."
    ca "No human will ever touch me."
    ca "Not now, not ever."
    show eec 71
    mc "But I touched you already. Several times."
    show eec 70
    ca "Hmph. Fair, I guess. No human will ever touch me {i}below my shoulders{/i}, since you prefer to nitpick."
    show eec 71
    mc "I gotta say, today has made me regret being human like never before."
    show eec 70
    ca "I will not blame you for the shortcomings of your race."
    ca "And neither should you."
    ca "Even if we set aside the stark contrast in our social classes, a human would never be able to endure an elven woman."
    ca "It is just how it is."
    show eec 71
    mc "*Chuckles* Okay, now you're clearly underestimating me."
    show eec 72
    ca "Please..."
    show eec 71
    mc "Oh, is that a challenge...?"
    show eec 72
    ca "*Soft chuckle* If we were in Hyril'ar, I might even consider allowing you to test yourself with one of my maids."
    ca "Some of them would surely agree purely out of a morbid fascination with the idea."
    show eec 71
    mc "That sounds incredibly hot, but... I could definitely “endure” even an elven princess."
    show eec 72
    ca "Please, spare yourself the embarrassment."
    ca "You would be finished before even starting."
    show eec 71
    mc "Hah! Who do you take me for? That's not true!"
    show eec 72
    ca "If I wanted to, I could make you finish without touching you."
    show eec 71
    mc "Not true."
    show eec 72
    ca "In less than a minute."
    show eec 71
    mc "Not true."
    ca ". . ."
    show eec 73 
    ca ". . ." with dis12
    play sound beat
    play sound2 whoosh7
    scene eec74 with Dissolve(.3)
    scene eec 74
    bla "An intense tingling runs through your body." with dis12
    show eec 75
    mc "O-O-Ohh... shit, w-what was that?"with dis
    show eec 76 with Dissolve(.1)
    play sound whoosh7
    play sound2 woodhit
    play sound3 fall3
    play sound4 fall
    scene eec77b
    bla "A strong force pulls you down into the floor." with vpunch 
    show eec 78
    mc "W-What's going on?!" with dis14
    play sound5 spell2
    show eec 79 with flashfast
    mc "What the fuck..." with dis06
    ca "You do not seem to fully understand here, [mc], and now I am starting to take it as a personal affront."
    show eec 80
    mc "O-Oh boy..." with dis14
    show eec 79
    ca "So let me stoop to your level here."with dis
    show eec 80
    ca "I could make you {i}ejaculate{/i} without touching your dirty, inferior human body."with dis
    ca "That is how superior the elven race is."
    ca "Was I clear enough now?"
    show eec 79
    mc "I'm sorry, but you're wrong, my Princess..."with dis
    ca "*Playful chuckle* We will see about that..."
    play soundlow penetration2
    play sound grab2
    play sound2 woodhit volume 0.4
    show eec 81
    bla "The surprisingly warm ghostly hand grabs your shaft firmly." with hpunch 
    mc "O-Oh shit...!"
    $ renpy.music.set_volume(1.0, channel='soundloop')
    $ renpy.music.set_volume(0.3, delay=10.0, channel='music2b')
    play soundloop wetting2 fadein 3
    scene calywest2 with dis22
    mc "O-O-Ohhh my god..."with dissolve 
    mc "W-What the hell is this...?!"
    ca "*Giggles* Elven magic."
    mc "Ahhh... fuck, your mages sure know the best spells..."
    mct "What in the world?!"
    mct "This doesn't feel like a normal handjob..."
    mct "It doesn't even feel like a hand. It feels as if my whole cock was embraced by something... warm... and incredibly tight..."
    mct "Fuck, she's squeezing it so hard that she'll make it explode..."
    ca "All well down there, [mc]? You seem to be struggling."
    mc "P-Pretty well, yes."
    mc "I've never been... aaahhh... b-better."
    mct "Fuck, I'm gonna cum..."
    mct "FUCK, am I gonna cum already?!"
    mct "No, no, no, I can't give her that satisfaction..."
    scene calywest3 with dis22
    mc "Aaaahhh... holy fuck..." with dis
    mct "Okay... yeah..."
    mct "That's it... you can hold it, [mc]..."
    mct "You can do it."
    mct "Think of ugly things..."
    mct "Nooo... don't look at her, that makes it worse..."
    mct "Don't look at Calypso's perfectly shaped body... her hourglass curves... don't look at her mesmerizing tits..."  
    mct "Fuck..."
    mct "Hold on there, [mc]..."
    mct "Focus on what she’s gonna do next after she gets frustrated that she can’t make you cum without touching you..."
    mct "Y-Yeah, that's it..."
    mct "Her superior status will crumble..."
    mct "Maybe then she’ll want to try harder..."
    mct "And she’ll probably get closer..."
    mct "Oh boy, imagine burying my cock deep inside the Princess' pure depths..."
    mct "Just imagine..."
    mct "Seeing her eyes rolled up with pleasure..."
    mct "BEGGING me for more..."
    mct "And me cumming all over her pretty face..."
    mc "*Muttering* Yeah... you like having fluids of a plebeian on your face now, don't you, Princess...? What a filthy girl..."
    ca "What?"
    mc "E-Eh...? N-Nothing! Nothing!"
    mc "I just... ahhh..."
    mc "Nothing..."
    scene calywest4 with dis2
    ca "Your tenacity is admirable, I must acknowledge that."with dis08
    bla "Calypso boosts her speed, increasing the pressure and warmth of her magic hand even more."
    mc "AAAaahh..."
    mct "Goodness gracious, I can't even move."
    mct "It feels as if my whole body was paralyzed."
    ca "I am surprised by your... endurance."
    mc "T-Thanks."
    mct "If she can really make me feel this way without touching me..."
    mct "How would her actual hand feel? Or her mouth..."
    mct "Her pussy..."
    mc "AAaahh..."
    mct "I wanna sully the Princess so much..."
    mct "I wanna corrupt her..."
    mc "Aaahh..."
    mc "L-Looks like you won't be able to make me “finish” after all, Princess..."
    stop soundloop fadeout 1
    play sound3 penetration2
    play sound5 penetration2
    scene eec 83
    ca "*Clenching her fist even harder* You are restraining yourself." with dis
    mc "*Gritting your teeth* W-W-Well, that's the p-point."
    ca "Do you think you can overpower me?"
    ca "You will see now..."
    play sound spell2
    play sound2 penetration2
    show eec 84 
    bla "Another magic hand appears."with flashfast
    mc "Oh boy..."
    play soundloop wetting1 fadein 2
    scene calywest5 with dis2
    mc "AAAaaaaaugghh..."with dis06
    bla "As Calypso launches her final assault, a torrent of sensations unlike anything you have ever known engulfs you."
    play sound3 penetration2
    play sound5 penetration2
    ca "*Clenching her fists* This has gone on for long enough!"with hpunch 
    mc "Oh FUCK."
    mc "T-This is too much..."
    play sound3 penetration2
    play sound5 penetration2
    ca "Hmmmhhgg..."with hpunch
    play sound3 penetration2
    play sound5 penetration2
    ca "*Grumbling* Release yourself for your Princess!"with hpunch
    play sound3 penetration2
    play sound5 penetration2
    ca "That is an order!"with hpunch
    mct "Oh shit, she sounded so angry, but it was so hot at the same time..."
    bla "With every stroke of the hand, the sensation intensifies, firmly anchoring you to the earth beneath, immobilizing you with overwhelming force."
    play sound3 penetration2
    play sound5 penetration2
    ca "*Grumbling* Why is he not finishing?!"with hpunch
    mc "O-O-Ohh my god..."
    mc "Hhnnnggg..."
    pause
    play sound wood
    scene eec 85
    mc "Oh god..."with dis
    mct "At this rate my balls are gonna explode."
    stop soundloop fadeout 7
    mct "But I did it!"
    mct "I'm not cumming!"
    mct "I won."
    mct "I..."
    mct "Huh...?"
    show eec 86
    mc "She stopped...?" with dis
    scene eec 87
    $ renpy.music.set_volume(0.5, channel='music2')
    $ renpy.music.set_volume(0.5, channel='music2b')
    stop music2b
    play music2 saloon2 
    pause 
    mc "Eh...?"with dis08
    mc "C-Calypso?"
    ca ". . ."
    play sound clothes3
    show eec 88 
    bla "Calypso touches your cock with the tip of her finger." with dis14
    scene calywest6 with dis2
    play sound2 rubclotheslong
    pause 4.9
    stop sound2
    pause .7
    play sound squirt
    play sound2 cum3
    play sound3 cum4
    play sound5 slap1
    scene eec89
    mc "FFFFFFFFFFFUUUCKKKKK...." with vpunch 
    play sound squirt
    play sound2 cum3
    play sound3 cum4
    mc "AAAAAaaaAARgggGGHhh..." with vpunch
    play sound squirt
    play sound2 cum3
    play sound3 cum4
    mc "AAAaaaahhHhh..." with vpunch
    play sound6 woodhit volume 1.1
    play sound7 fall3
    play sound5 fall2
    show eec90
    mc "*Collapsing to the ground* H-Holy Jeebus Harry and Broseph..."with vpunch
    mc "*Catching your breath* God..."
    mc "*Catching your breath* Okay... y-you win..."
    mc "*Catching your breath* Unbelievable..."
    $ renpy.end_replay()


label ga_annie3:
    $ renpy.music.set_volume(0.35, channel='music3')
    play music3 sexyannie fadein 10
    show eaa37 
    a "WAIT!" with dis 
    a "Umm... d-don't go!"
    scene eaa 38
    mc "Huh?"
    mc "What's the matter?"
    show eaa 39
    a "*Clears throat* I mean, you can go... but before you do... I just thought that..."with dis 
    a "Well, I’ve had a lot of time to myself this past week and..."
    a "I’ve been thinking a lot... and feeling a lot of... umm, {i}feelings{/i}... eheh..."
    a "And I was wondering if we possibly, by chance, maybe... c-continue our little {i}practice{/i} sessions?"
    show eaa 40
    mc "Practice... like with the guitar?"
    show eaa 39
    a "N-No. Not the guitar."
    a "I mean... remember last time in Andromeda? When you taught me... certain things? And made me feel... certain ways?"
    show eaa 40
    mc "How could I forget..."
    show eaa 39
    a "Well... I thought that... maybe... we’re a little overdue for some more... p-practice."
    a "Like... kissing, or... you know, k-kissing with some tongue too."
    show eaa 40
    mc "Ah... that kind of “practicing”..."
    show eaa 39
    a "Yeah, I mean..."
    a "What if Dalia suddenly kisses me one day? With my severe lack of practice, I'd only embarrass myself."
    show eaa 40
    mc "You want to kiss Dalia?"
    show eaa 41
    a "Y-You know what I mean!"with dis08
    show eaa 42
    mc "*Chuckles* I'm honestly not sure."
    show eaa 41
    a "D-Don't make fun of me!"
    show eaa 42
    mc "It's you who keeps going in circles, dancing around what you’re really getting at!"
    mc "Why don't you just tell me what you really want?"
    mc "Be direct."
    show eaa 43
    a "*Taking a deep breath* Hnnn..."with dis
    show eaa 44
    a "I..."with dissolve
    a "I want you to kiss me."
    show eaa 45
    mc "See? It wasn't so hard."
    mc "*Chuckles* Now come here, silly girl."
    show eaa 48
    bla "Annie gets closer to you. Her alluring blue eyes gaze deeply into yours, as she playfully begins swinging her petite hips." with dis15
    mct "Sometimes I forget how small Annie is."
    mct "She was wearing heels in that server the whole time, so I guess that also created the illusion of her being taller."
    show eaa 46
    mc "You need to be more direct, Annie." with dis
    show eaa 47
    a "I’m trying!"
    a "I-It's just that... I don't want to make things awkward or anything."
    show eaa 46
    mc "I've told you about a hundred times the way I feel about you."
    mc "There's no way you can make things uncomfortable between us."
    show eaa 47
    a "I-I know..."
    show eaa 46
    mct "I shouldn't be so afraid to make the first move either when it comes to Annie."
    mct "She's told me how she feels as well, after all."
    play sound clothes2
    play sound2 fall2
    show eaa 49 with dis 
    mc "*Picking her up* Alright, so... you told me you want to practice kissing again, is that correct?" with dis06
    show eaa 50
    a "Yes sir..."
    show eaa 49
    mc "And do you have any preference on who you practice with?"
    mc "I've heard Professor Keating is such a good kisser."
    show eaa 50
    a "*Giggles* I’ll have to take your word on that one. As for me, I only want it to be you."
    show eaa 49
    mc "Oh..."
    mc "Well, that makes things easier..."
    show eaa 51 with dis
    bla "You lean in, and your lips meet in a soft, tender kiss." with dis06
    a "Mmmm..."
    play sound chair1
    play sound4 clothes3
    play sound2 ["<silence 0.1>", plate]
    show eaa 52
    bla "Without your lips ever parting, you carry Annie towards her bed and both of you fall back onto the soft mattress."with dis
    play sound clothes3
    show eaa 53
    a "*Sitting up* I missed you so much. Being back in your embrace... it’s just what I needed."with dis12
    show eaa 54
    mc "Me too..."
    show eaa 53
    a "Do you mind if I... get a little more comfortable?"
    a "You should know... for some reason this outfit always feels a bit itchy against my skin."
    show eaa 54
    mc "Ah, yes, I remember..."
    mc "Maybe you should just stop wearing these pajamas altogether."
    show eaa 53
    a "*Giggles* Yeah, maybe I will start going to sleep naked."
    show eaa 54
    mc "That sounds like a really good idea..."
    show eaa 53
    a "But you know, if I do that, I get cold really easily... I’d need someone to keep me warm..."
    show eaa 54
    mct "I like seeing Annie growing in confidence, teasing and joking around."
    show eaa 55 with dis12
    pause
    play sound clothes4
    show eaa 56 with dis12
    mc "Oh boy..."with dis06
    play sound2 clothes2
    show eaa 57 with dis12
    mc "I’ll never get tired of seeing your gorgeous body, Annie." with dis08
    show eaa 58
    a "T-Thank you..."
    show eaa 57
    mc "Now, where were we...?"
    play soundlow chair1
    $ renpy.music.set_volume(0.6, channel='soundloop2')
    $ renpy.music.set_volume(0.27, delay=15.0, channel='music3')
    play soundloop2 kissing fadein 2
    scene annieb1 with dis2
    bla "Without answering your question, Annie eagerly pounces on you and resumes the kiss."with dis08
    a "Mmmmmhm..."
    mct "Her soft skin feels so warm... I can’t keep my hands from tracing her every outline."
    mct "She's so light, but at the same time I can feel all of her beautiful curves tightly hugging my body."
    mct "I can tell she wants this as much as me."
    bla "As time goes by, Annie summons more and more confidence and lustfully deepens the kiss."
    a "*Slight moan* Mmmm..."
    mct "Feeling her heart pounding is so intoxicating."
    mct "I just want to hold her tighter..."
    mct "I want her to feel how much I desire her..."
    a "Mmm..."
    stop soundloop2 fadeout 1
    play sound clothes3
    scene eaa 58
    a "*Breaking the kiss* I... "with dis12
    show eaa 57
    mc "All good?"
    show eaa 58
    a "I want..."
    a "I want to do that thing again."
    show eaa 57
    mc "That “thing”?"
    show eaa 58
    a "In Andromeda."
    a "I w-want you to... I need to feel your finger i-inside of me again."
    show eaa 57
    mc "Naughty girl..."
    play sound chair1
    show eaa 59
    bla "You grab Annie and throw her onto the bed." with dis12
    mc "We're gonna have to make ourselves even more comfortable for that."
    play sound clothes3
    play sound2 clothes4
    show eaa 60
    mc "*Taking your shirt off* You don't mind if I take this thing off, right?"with dis12
    a "Nuh-uh..."
    mc "Now... as much as I like those cute pajamas, I'm afraid we'll have to get rid of them."
    show eaa 62 
    bla "Annie looks at her pants and, after a moment's hesitation, slowly starts slipping them off."with dis12
    play sound clothes
    show eaa 63 with dis12
    pause .3
    show eaa 64 with dis14
    mc "Oh my..." with dis
    mc "No panties, eh?"
    mc "Were you expecting this to happen?"
    show eaa 65
    a "Perhaps..."
    show eaa 64
    mc "Fuck, I just want to explore every inch of you..."
    show eaa 66
    a "I... I'm n-not sure I'm ready, [mc]."
    show eaa 64
    mc "Ready for what?"
    show eaa 66
    a "You know what I mean..."
    a "Ready for... {i}sex."
    show eaa 64
    mc "Like I’ve told you before, we can take it as slow as you want. I’m only going to accept however much you’re willing to give."
    mc "I want you to feel safe. I just want to take you to a place where you can let go of your shyness, your inhibitions, and truly embrace your desires without reservation."
    mc "And until then... you set the pace."
    a ". . ."
    play sound clothes3
    show eaa 67 with dis14
    bla "As if you had pronounced some magic words, Annie's legs slowly open for you and you’re again blessed with a sight that no other man has seen before."with dis
    show eaa 68
    mc "Oh Annie..."with dis12
    mct "God... I just want to devour all of her."
    play sound clotheswhoosh
    play soundlow chair1
    scene eaa69
    mc "*Pulling Annie towards you* Come here..." with hpunch
    a "W-WHAT? Wait!"
    a "I said I'm not ready!"
    a "I just wanted the same thing we did in Andromeda!"
    mc "I know. We can do that... but maybe instead of a finger, we can try it with something else you were playing with earlier."
    mc "You'll see..."
    a "What?! Are you gonna use your mouth... your tongue... on my...?"
    mc "I’m dying to taste you, Annie."
    a "[mc], I... I-I'm not sure if I'm ready for that either!"
    a "W-What if you don’t like the way I taste? O-Or what if I feel strange or..."
    play soundlow clothes4
    show eaa 70 with dis14
    bla "You start sliding your tongue between Annie's outer lips." with dis
    a "[mc!u]!" with hpunch
    mc "There’s no way such a beautiful girl like you..."
    bla "Your tongue slowly starts grazing around her wet pussy."
    mc "Could taste anything other than amazing..."
    a "I'm..."
    show eaa 71
    a "Not..."with dis 
    a "Reaaaaddyyy..."
    a "Oh [mc]... that feels..."
    play soundlow chair1 volume 0.7
    show eaa 72
    a "Oh my GOD!" with dis08
    $ renpy.music.set_volume(0.19, delay=10.0, channel='music3')
    $ renpy.music.set_volume(0.8, channel='soundloop')
    play soundloop wetting5 fadein 2
    scene annieb2 with dis2
    a "MMmmmm..." with dis
    a "Oh god..."
    bla "You begin to taste every inch of Annie, spreading her tight lips as you gracefully move your tongue back and forth."
    mct "Maybe I should have started slower."
    a "*Moaning* Mmmm-aahh-mmm..."
    mct "Although she doesn't seem to mind..."
    a "Oh my god, [mc]..."
    mct "I fucking love her taste..."
    a "AAaahh... how are you doing that..."
    a "Y-Your tongue feels so... aaAaahhh..."
    mct "Maybe now I could try focusing on her clit."
    mct "Her thighs seem to keep pushing my mouth toward it..."
    mct "Here we go..."
    stop soundloop fadeout 1
    play sound clothes4
    play soundlow punch volume 0.4
    scene eaa 73
    a "AAAAGH! What's that!"with hpunch 
    a "*Grabbing your head* STOP!"
    mc "You don't like it?"
    a "NO! I mean... d-don’t stop..."
    play soundloop wetting4 fadein 2
    scene annieb3 with dis2
    a "[mc]. . . . . . . . . . .  . !"with dis
    bla "Annie's body language screams of ecstasy as you continue attacking her swollen clit."
    a "Oh godddddd..."
    a "Mmmmmm..."
    a "Oh yes. OH... FUCK YES!"
    a "Please don't stop!"
    a "Keep doing what you're doing... WHATEVER IT IS!"
    a "Eat me whole..."
    mct "Oh boy..."
    mct "It's so tempting to let go of the reins and allow my desires to consume me, permitting nothing but passion to drive us both wild...."
    mct "But I have to resist the urge, for now. I know Annie better than herself, and I know she’s really close but not quite ready to go all the way."
    mct "This moment is about more than just my pleasure."
    mct "Although... I'm not sure how long I'll be able to hold out..."
    a "*Loudly moaning* AAAAaaaaGH... aaahhh..."
    mct "Thank god it's storming outside, otherwise it’d be nearly impossible to not hear her moans throughout the house..."
    a "AAaahh... oh god [mc]... I think I'm gonna... C-CUM..."
    a "Again..."
    a "[mc]! You’re gonna make me..."
    a "I can feel it coming..."
    a "Aaah..."
    a "AAAaahhh..."
    stop soundloop fadeout 1
    play sound clothes4
    play soundlow punch volume 0.4
    play sound cum3
    scene eaa 73
    a "AAAAARRRHHHGGHH..." with hpunch
    a "MY GOD!" with hpunch
    a "HEAVENS!"with hpunch 
    a "WHAT... WHAT WAS THAT?!"
    a "That was... soooo... amazing..."
    mc "*Muffled* Y-You're kind of crushing my skull with your thighs..."
    mct "How the hell are her legs so strong?!"
    play soundlow chair1
    play sound2 clothes4
    scene eaa 74 with dis15
    bla "You move aside and let Annie collapse on the bed after her orgasm."with dis
    a "Wow..."
    a "M-My legs are still shaking."
    a "I almost forgot where we were..."
    show eaa 75
    mc "*Sitting on the edge of the bed* See? You just have to trust me."
    show eaa 74
    a "I guess you're right..."
    play soundlow chair3 volume 0.4
    play sound clothes3
    show eaa 76 with dis15
    a "*Sitting up and crawling towards you* I guess from now on I should..."with dis06
    show eaa 77
    a ". . ." with dis08
    show eaa 78
    a "W-W-When did you lose your pants?!" with dis12
    show eaa 79
    mc "Slowly after I started going down on you..."
    mc "You didn't notice?"
    show eaa 78
    a "N-Not at all."
    show eaa 79
    mc "I guess you were too absent-minded..."
    show eaa 78
    a "I-It looks..."
    a "It looks as big as it was in Eternum."
    show eaa 79
    mc "I'd be surprised if something didn't look the same as in Eternum. We're literally an identical replica of ourselves in there."
    show eaa 78
    a "I know, I meant that..."
    a "It's {i}still{/i} big."
    show eaa 79
    mc "Do you want to... give me another handjob?"
    a ". . ."
    show eaa 78
    a "I mean... it’s only fair that..."
    a "Since you got to use your tongue, I should be able to use mine too..."
    show eaa 79
    mc "Fuck, I was hoping you'd say that so much..."
    show eaa 80
    bla "Annie slowly positions herself on your side and lightly touches your dick with the tip of her tongue." with dis15
    a "*Sniffs* Your scent is just so... alluring..."
    show eaa 81
    a "Aaahh..."with dis12
    mc "Yes..."
    scene annieb4 with dis2
    bla "Annie eagerly starts lapping up your shaft."with dis
    mc "Oh, fuck yes..."
    a "*Slight moan* Mmmm..."
    mc "Oh Annie..."
    a "It's so slippery..."
    a "And..."
    a "I can feel you pulsing, [mc]..."
    mc "Because I'm so fucking horny for you right now..."
    a "There's no way I can fit all of you inside of my mouth..."
    mc "You'd be surprised how much you can take..."
    a "Mmmmh..."
    a "Y-You’re just too thick."
    mc "Don't you wanna try it...?"
    mc "Please, just the tip..."
    mc "I’m dying to feel your lips wrapped around me..."
    a "Aaaahhh... that does sound... good..."
    a "I guess..."
    a "I guess I could try..."
    mc "Attagirl..."
    scene eaa 82
    a "*Breathing noticeably faster* Alright..."with dis14
    a "I’ll give it a shot... only for you..."
    mc "Please..."
    play sound6 blow6 volume 0.3
    show eaa 83 with dis14
    bla "Annie slowly envelopes the tip of your cock between her soft lips before taking more of it inside her small, warm mouth. She struggles a bit at first, but then quickly becomes accustomed to it."with dis08
    mc "Yeah, just like t-that..."
    mc "Now take it deeper..."
    play sound blow6 volume 0.5
    show eaa 84 with dis15
    mc "AAAAAHHH..." with dis08
    play soundloop blowjob2 fadein 2
    $ renpy.music.set_volume(0.1, delay=8.0, channel='music3')
    scene annieb5 with dis2
    mc "HOT DAMN..."with dis
    mc "Oh my fucking god, this can't be real..."
    mc "I can’t believe you’re actually..."
    mc "Oh, baby, yes..."
    a "*Moaning* MMmmmmMMMmm..."
    play sound blow5
    stop soundloop fadeout 1
    scene eaa 86
    a "*Taking a deep breath* AAaahh..."with dis
    mc "No, don't stop, please..."
    a "I... I n-need to catch my breath!"
    mc "Oh... I t–"
    play sound2 blow4
    play soundloop blowjob2 fadein 1
    $ renpy.music.set_volume(1.0, channel='soundloop2')
    scene annieb5 
    bla "Annie shuts you up quickly by eagerly fitting as much of your dick as she can into her mouth again."with dis12
    mc "F-FUCK..."
    mc "Yeah... keep going... suck it as hard as you can, babe..."
    a "*Sucking harder* Mmmmh...!"
    mct "This sensation is unreal..."
    mct "I can feel Annie's lips stretched to the max... her small mouth completely filled by my cock..."
    a "*Choking* Mmmm... mmmm... mmmmhh..."
    mct "She's getting it so wet... she really seems to be savoring it..."
    mc "Good girl..."
    mc "That's it..."
    mc "Breathe through your nose..."
    mc "Just don't stop..."
    mct "My god..."
    mct "She's gonna drive me crazy..."
    a "*Moaning* Mmmhm..."
    mct "I can feel her getting more comfortable and confident with herself as time goes by..."
    mct "She's enjoying this as much as me."
    a "MMmmMmMmmhm...."
    mct "Should I push her limits? Or let her find her own rhythm?"
    menu:
        with dis
        "Let her find her own rhythm":
            $ anniefuckface = False
            mct "I should let her take the reins on this... but maybe a little feedback wouldn’t hurt." with dissolve
            mc "*Panting* Annie...?"
            a "Hmm?"
            mc "D-Do you think you can go a little bit faster?"
            mc "I'm almost there..."
            stop soundloop fadeout 2
            play soundloop2 blowjob3annie fadein 2
            scene annieb6 with dis2
            bla "Annie obediently shifts gears and sloppily sucks your cock much faster, taking it as deep down her throat as she can." with dis
        "Push her limits":
            $ anniefuckface = True
            mct "Fuck it, I can't restrain myself anymore..."with dissolve
            play sound5 clothes4
            stop soundloop fadeout 2
            play soundloop2 blowjob4annie fadein 2
            scene annieb7 with dis2
            mc "AHHHHHHGG...." with dis
            mc "NOW WE'RE TALKING..."
            bla "You grab Annie's head and start fucking her mouth. You can hear her choking with each thrust, but Annie's throat willingly takes all of you."
    mc "HOLY FUCK..."
    mc "O-Oh my god..."
    mc "That's it..."
    if not anniefuckface:
        a "*Choking* Hnng... mmmh... hhnng?"
        mc "N-Not sure what you asked, b-but... FUCK YES!"
    else:
        a "*Choking* Hnng... hnnggg... hhhnnnggg!"
        mc "F-Fuck YES!"
    mc "Take it all..."
    mc "GOOD GIRL..."
    mct "My god... this is really happening..."
    mct "The sweet, innocent, little girl I've known for years..."
    mct "The same one that used to blush and hide every time anything even remotely sexual was mentioned..."
    if not anniefuckface:
        mct "Is here milking my cock like a mad woman..."
    else:
        mct "Is here letting me use her mouth to milk my cock..."
    stop soundloop2 fadeout 1
    play sound woosh1
    scene eaa 84c
    mc "Come on Annie, you're gonna miss the entire movie!" with flashfast
    a "B-But that guy is... n-naked!"
    a "T-They showed his..."
    mc "The scene is over, don't worry!"
    a "Y-you sure?"
    mc "Yes!"
    stop soundloop
    $ renpy.music.set_volume(0.15, delay=1.0, channel='music3')
    if not anniefuckface:
        play soundloop2 blowjob3annie fadein 1
        scene annieb6 
    else:
        play soundloop2 blowjob4annie fadein 1
        scene annieb7
    play sound woosh1
    mc "AAAAargh... fuck, Annie..." with flashfast
    mc "That's it... suck it until it's dry..."
    a "*Choking* MMmmmmmmmhhh..."
    stop soundloop2 fadeout 1
    play sound woosh1
    scene eaa 84b
    adad "You better take care of my little girl while you're in the USA, [mc]." with flashfast
    mc "Rest assured Mr. Winters, I won’t let anything happen to her!"
    mc "I'll take care of Annie as if she was my sister!"
    stop soundloop
    $ renpy.music.set_volume(0.15, delay=1.0, channel='music3')
    if not anniefuckface:
        play soundloop2 blowjob3annie fadein 1
        scene annieb6 
    else:
        play soundloop2 blowjob4annie fadein 1
        scene annieb7
    play sound woosh1
    a "*Choking* MMMmmMhhhHh!" with flashfast
    mc "Oh GOD, Annie, I'm gonna fucking cum!"
    a "Mmmmmhh..."
    stop soundloop2 fadeout 1
    play sound blow4
    play sound2 blow5
    scene eaa 85
    a "*Catching her breath* AAAAaaaAAAArgHhhh..."with dis 
    a "*Catching her breath* I c-can't... take it... anymore..."
    play sound3 clothes4
    play sound4 chair3
    play sound5 fall2
    play sound6 fall3
    show eaa 87
    bla "You pull Annie to the floor as she collapses, completely exhausted, right in front of you." with dis12
    a "*Panting* A-Are you... gonna... finish on m-me...?"
    mc "I want to..."
    mc "Can I...?"
    a "*Panting* Yeah..."
    a "*Panting* Do it... empty y-yourself all over me, [mc]..."
    mc "Oh god Annie, I'm..."
    mc "I'M ALMOST..."
    play sound cum2
    play sound2 cumall
    play sound3 cum4
    show eaa 88
    mc "AAAAAAHHHH..." with hpunchlong4
    scene eaa 89 with dis17
    mc "Jeez..." with dis
    a "H-Holy cow..."
    a "You... released... a lot..."
    mct "Man, I love seeing her slim body covered in my cum."
    mc "You okay? Sorry, I couldn't really hold back there..."
    show eaa 90
    a "Yeah..."with dissolve 
    a "I-It's okay."
    a "It tastes... weird. I mean, not bad, just umm... different. I can't really liken it to anything I've had before."
    play soundlow chair2
    stop music3 fadeout 8
    play soundloop rain3 fadein 7
    scene eaa 91
    a "*Standing up* Oh god, my jaw hurts..."with dis15
    mc "Yeah... that ended up being pretty intense... I hope I didn't overdo it there."
    mc "But my god, I have to say... that felt unbelievably good."
    show eaa 92
    a "R-Really? It c-couldn't have been that big of a deal, right...?"with dis
    show eaa 93
    mc "Are you kidding me?"
    mc "Goddammit Annie... that was mind-blowing."
    show eaa 92
    a "Oh... well t-thanks."
    a "I mean... I'm glad. I didn't know I could make someone feel like that."
    a "I actually had a lot of fun too."
    a "Maybe even too much... I forgot to lock the door."
    show eaa 93
    mc "Well, I'm sure Dalia and Penelope would knock before entering your room."
    mc "Not so sure about Nancy though..."
    mc "Let's just say she has a bad history with closed doors."
    show eaa 92
    a "Still, w-we should be more careful."
    a "Imagine if Nancy had caught us... she'd kick us out of the house!"
    show eaa 93
    mc "*Snorts* I highly doubt that."
    if nancypath:
        mc "Why would she? We weren't doing anything wrong."
        mc "And besides, knowing Nancy, I think it's more probable that she'd be asking us to join rather than giving us the boot!"
        show eaa 94
        a "[mc]!" with dis08
        a "Don't be nasty!"
        show eaa 94b
        mc "*Chuckles* Okay, okay."
        show eaa 95
        a "Do you think she'd really ask that, though...?" with dis
        a "It's true that she can be quite passionate, but..."
        mc "Huh...?"
        mc "Do I sense some... interest?"
        show eaa 94
        a "O-Of course not!" with dis08
        a "I was just... digressing."
        show eaa 94b
        mc "Ah yeah, of course..."
    show eaa 96
    a "*Clears throat* Anyway, I'm gonna take a shower!"with dis12
    a "I can't really go to bed like this... you've made quite the mess of me."
    mc "Of course."
    mc "Good night, Annie."
    mc "Thank you for an amazing night."
    show eaa 97
    a "Oh, before I leave..."with dis 
    a "I wanted to say something."
    mc "What is it?"
    show eaa 98
    bla "She slowly approaches you, raises herself onto her tiptoes, and leans into your shoulder."with dis14
    mc "Are you okay?"
    a "Next time..."
    mc "Huh?"
    show eaa 99 
    a "*Whispering* Next time... I'll be {i}ready{/i} for you."with dis14
    play sound doorclose
    play sound2 run
    show eaa 36 with dis15
    bla "Annie rushes out and heads towards the bathroom."with dis 
    mct "Oh my god..." 
    stop soundloop
    $ renpy.end_replay()


label ga_nancy2:
    scene black
    mc "W-What are you doing?!" with dis08
    mc "Nancy?"
    play sound7 generator
    $ renpy.music.set_volume(0.45, channel='music3')
    play music3 nancysexy fadein 9
    show ds 7
    bla "The elevator's emergency lights flash on." with dis
    mc "Oh..."
    show ds 8
    n "But then I thought..." with dissolve
    n "...fuck that."
    n "If destiny doesn't want to give me an opportunity... I'll create my own."
    n "I'll take what I want."
    n "And what I want... is you, [mc]."
    show ds 7
    mc "I like that way of thinking..."with dissolve
    show ds 8
    n "What about you? Do you know what you want...?"with dissolve
    play sound3 clothes3
    show ds 9
    mc "*Caressing her cheek* Fuck, Nancy..." with dis12
    mc "You know exactly what I want."
    mc "We still have a yoga session pending, don't we?"
    show ds 10
    n "Ah, you're very right, mister. What an eager boy..."
    show ds 9
    mc "Should we continue it now?"
    show ds 10
    n "Hmmm... now seems like as good a time as any..."
    show ds 11
    mc "Maybe we should get a bit more comfortable, then." with dis12
    mc "These clothes look a little restrictive... Do you mind if I help you get rid of them...?"
    n "Mm-hm..."
    show ds 12 with dis12
    pause
    play sound buttons
    play sound2 clothes4
    show ds 13
    bla "You rip off the buttons of Nancy's blouse, revealing her bra and increasing your temptation to unfathomable levels."with dis
    mc "Fuck, yes..."
    mc "I'm gonna eat you up, Nancy..."
    play sound3 woodhit
    play soundlow elevatorstop
    show ds 14
    n "*Pushing you against the wall* Oh no, no chance!" with dis12
    n "That already happened last time, remember?"
    show ds 16
    n "Now... it's my turn." with dis
    if nancymommy:
        n "Let your mommy take care of you. You’ve been such a good boy, after all..."
    else:
        n "Let me take care of you..."
    show ds 15
    mc "With pleasure..."
    show ds 16
    n "Any special requests...?"
    show ds 15
    mc "Hmm..."
    mc "Take off your bra. I wanna see those perfectly shaped tits of yours again..."
    show ds 16
    if nancymommy:
        n "Oh my, are you not excited enough? Wanna play with my titties in front of your face again, baby boy?"
    else:
        n "Oh my, are you not excited enough? Wanna play with my titties in front of your face again?"
    show ds 15
    mc "You could say that... I’ve always been more of a... tactile learner."
    mc "Just the idea of your tits isn’t enough for a hedonist like me..."
    show ds 16
    n "*Giggles* I don't know, you look plenty excited to me, [mc]."
    n "That bulge in your pants gives you away."
    show ds 15
    mc "You're denying my request, then? Such a tease..."
    show ds 16
    n "Oh, not at all."
    n "I’m just trying to take back some control of the situation... can’t have you getting too antsy, sweetheart..."
    n "But... it'd be very rude if I refused."
    play sound clothes4
    show ds 17 with dis15
    pause
    play soundlow ["<silence 0.2>", clothes2]
    show ds 18
    if nancymommy:
        mc "That's it, Mommy..." with dis12
    else:
        mc "That's it, Nancy..." with dis12
    play sound2 clothes3
    show ds 19
    bla "Nancy removes her bra, exposing her hefty tits to the cold elevator air." with dis15
    mc "Oh god..."
    mc "Can you... can you give me a little spin?"
    show ds 21
    n "*Giggles* You're wasting your time, [mc]." with dis12
    n "This emergency stop is only temporary. If someone calls for the elevator, it’ll start up again..."
    n "Tick, tock, [mc]..."
    show ds 20
    mc "I don't give a fuck. I've been craving this moment for so long... nothing’s gonna stop me from enjoying this to the fullest."
    show ds 21
    n "*Chuckles* Living in the present, eh?"
    show ds 20
    mc "Life is too short to never take risks..."
    show ds 21
    n "I couldn't agree more. As long as what you do doesn't hurt anyone... sometimes you’ve gotta just take a chance."
    show ds 20
    mc "Taking a chance, eh? Maybe I should start taking more chances with you, too."
    show ds 21
    n "I’d like to see you try, [mc]..."
    show ds 22 with dis14
    n "*Kneeling down* You know, my mother used to say that risk-takers defy destiny with every decision. I’ve always kept that thought in my head."with dis06
    mc "Very wise woman, indeed..."
    play sound belt
    play sound2 clothes5
    show ds 23 with dis17
    n "Jesus..."with dis06
    n "What do they feed you boys nowadays?"
    mc "Do you like what you see?"
    play sound3 ["<silence 0.8>", slapsoft] volume 1.2
    show ds 25
    bla "Nancy reaches out and gently wraps her hands around your cock, before slapping your meat across her cheek."with dis12
    mc "O-Oh, god..."
    show ds 24
    n "Y-yeah, I guess you could say I like it..."with dissolve
    show ds 25
    mc "Fuck, Nancy..."with dissolve
    mc "You have me throbbing..."
    show ds 24
    n "You sure have a lot of love to give, [mc]."with dissolve
    show ds 25
    mc "What can I say, hot red-headed MILFs are my weakness..."with dissolve
    show ds 24
    n "MILFs, eh? I thought you’d have been playing around with all those younger girls..."with dissolve
    if nancymommy:
        n "Were you actually saving your loads for mommy...?"
    else:
        n "Were you actually saving your loads for me...?"
    show ds 25
    mc "You can have as many loads as you want..."with dissolve
    show ds 26
    bla "Nancy moves her tongue southward and begins giving small licks to your balls. "with dis15
    mc "O-O-Ohh..."
    show ds 24
    n "*Giggles* Mmmm... guess I’ve gotta check what you’ve been saving for me..." with dis15
    show ds 26
    mc "Take it into your mouth, please..."with dis15
    mc "I need it..."
    show ds 27
    n "Mmmm..." with dis15
    mc "Oh my god..."
    show ds 28
    n "Mmmm..." with dis14
    show ds 27 with dis14
    mc "Oh... Nancy..."with dis06
    mc "That's it... suck it fast..."
    $ renpy.music.set_volume(0.15, delay=10.0, channel='music3')
    play soundloop blowjob2 fadein 2
    scene nancyele1 with dis2
    mc "AAaaaahhh..." with dis
    mc "That's it..."
    mc "J-Jesus Christ, this feels too good..."
    bla "Nancy’s pillowy lips wrap around your girth, and you can’t help but let out a noise."
    n "*Moaning* MMmMmm..."
    mc "Keep looking in my eyes, Nancy..."
    n "Mmmm..."
    mct "I’ve known Nancy all my life... yet I’m still not used to the size of her enormous bust..."
    mct "All those years, and still no sag..."
    mct "No back problems, either."
    n "*Gagging* MmmMmmm..."
    mct "Hmm... between Nancy and Penelope... I wonder who's got the bigger pair..."
    mct "Penny did say that Nancy has a habit of stealing her bras..."
    mct "Man, I wish I could compare the two pairs."
    mct "Mother and daughter..."
    n "*Gagging* Mmmggghh..."
    mc "Aghhh... yeah..."
    mc "Keep pumping it, Nancy..."
    pause
    bla "Nancy continues to milk your cock with a steady rhythm, as her expressions grow more and more lecherous." with dis
    mc "AAaahh..."
    mc "G-God, how long can you keep that pace?"
    mc "D-Don't you need to breathe?"
    n "Mmmm...?"
    stop soundloop fadeout 1
    play sound blow4
    show ds 24
    n "*Catching her breath* I'm just breathing through my nose."with dis12
    n "You can reduce stress and anxiety just by controlling your breathing. You can learn a lot from yoga."
    mc "Ah, I guess that–"
    play soundloop blowjob2 fadein 2
    scene nancyele2 with dis2
    bla "Nancy envelops your cock inside her mouth before you can even finish your sentence."with dis
    mc "A-a-a-a-aaaahhh..."
    mc "Jesus..."
    mct "I was hoping she’d be good at this, but she's blown me away..."
    mc "Aaaahhh, yeah, that’s it..."
    mct "Nancy doesn’t seem to be interested in stopping before sucking the life out of me..."
    mc "Please, Nancy, don't stop..."
    pause
    stop soundloop fadeout 1
    play sound blow4
    show ds 29
    n "*Recovering her breath* AAAghh... FUCK!"with dis
    mc "Ah, your nose-breathing technique failed you?"
    show ds 24
    n "I guess I'll have to keep training..." with dis
    show ds 25
    mc "I think I have some free time for practice between our yoga sessions..."with dissolve
    show ds 24
    n "Good idea! But for today... I have something else in mind."with dissolve
    show ds 25
    mc "Oh... and what might that be...?"with dissolve
    play sound3 woodhit volume 0.4
    play soundlow elevatorstop
    show ds 30
    bla "Nancy pulls you to the ground and swings her leg over you." with dis12
    mc "Oh boy..."
    mc "Wait..."
    mc "You're not wearing panties?"
    play sound clothes4
    show ds 31
    n "*Straddling you and lifting her skirt* I guess I woke up a little naughty today." with dis12
    show ds 32
    if nancymommy:
        mc "What a naughty mommy..."
    else:
        mc "How naughty..."
    show ds 31
    n "You had no right to turn my life upside down like this, [mc]."
    n "I can't get you out of my head."
    n "Every single minute."
    n "Every single day."
    n "I... {w}NEED you... {w}inside me..."
    show ds 32
    mc "Oh my god..."
    mc "Are we..."
    mc "Are we really gonna do this?"
    mc "Are we..."
    show ds 31
    n "Yes, we are. We're gonna continue right where we left off last time, [mc]."
    n "I promised you, remember?"
    show ds 32
    mc "Oh fuck, yes..."
    mct "Oh my god, I'm about to fuck Nancy."
    mct "S-She's about to fuck me!"
    mct "Is this really gonna happen?"
    show ds 31
    n "Yes, it IS going to happen."
    show ds 32
    mc "W-What? Can you read my mind?"
    show ds 31
    n "Your face is like an open book, [mc]."
    show ds 32
    mc "Oh... I can imagine..."
    mc "I can't help but get the feeling we're about to get interrupted once again."
    mc "Right before the best moment."
    mc "Something's gonna happen..."
    n "*Giggles* Hmm."
    show ds 31
    n "Not this time, baby boy."
    n "This time, I won't let anything or anyone stop me."
    n "This time..."
    show ds 33
    n "You're all mine..." with dis17
    mc "O-Oh my god..."
    scene nancyele3 with Dissolve(3)
    pause 4.5
    play soundlow penetration2
    mc "AAaaaaahh...{w=5.6}{nw}" with dis2
    scene ds 34
    n "*Squeals* AAAAAAaaaaagggghh..." with Dissolve(1.7)
    n "Y-YEAH!"
    n "A-Are you ready...?"
    mc "O-O-Oh, god..."
    $ renpy.music.set_volume(0.1, delay=5.0, channel='music3')
    scene nancyele4 with dis2
    pause .5
    mc "OH M-MY FUCKING GOD..." with dis14
    bla "She starts moving up and down. Your cock spreads her wet lips apart, and quickly adjusts to Nancy’s wetness."
    n "O-Oh m-my g-goddd, [mc]...."
    n "*Moaning* This is..."
    n "AAaahhh..."
    n "T-This is it..."
    n "You're finally inside me, baby..."
    mc "F-FUUUUCK..."
    n "*Moaning* Y-You have no idea how long I've been..."
    n "AAhhh..."
    n "...how long I've been fantasizing about this moment..."
    mc "F-Fuck, me too, Nancy..."
    mc "Your pussy feels so good..."
    mct "I'm inside Nancy... I'm fucking her..."
    mct "This is not a dream, it's happening..."
    n "*Moaning* Aaaahh..."
    pause
    scene black with dis
    scene nancyele5 with dis2
    n "AAAaaahhh..." with dis
    mc "G-God..."
    n "D-Does it feel good, [mc]?"
    mc "*Panting* I've never felt anything so incredible..."
    mc "You f-feel... absurdly good."
    n "I can feel your cock f-filling me... aahh... every inch of your cock pumping in and out of me..."
    n "S-So much...."
    n "*Squeals* AAaaghh..."
    n "I bet you must drive the girls at your school crazy..."
    mc "W-Well..."
    if eva1 or maatsex:
        mc "T-Truth is, I've never done something like this in the real world."
    else:
        mc "T-Truth is, I've never done something like this."
    n "Oh... well..."
    n "Let me show you what you've been missing, then..."
    mc "Oh fuck yes..."
    n "MmmmMm..."
    n "I-I want more..."
    n "I {i}need{/i} more, baby..."
    mc "More?"
    if nancymommy:
        n "Can you handle me going faster, sweetie? I’ll start slowly... and it’ll make your mommy feel so much better..."
    else:
        n "Can you handle me going faster, sweetie? I’ll start slowly... and it’ll make your old babysitter feel so much better..."
    mc "F-Faster?"
    mc "Y-Yeah, I can take it..."
    n "That's my boy..."
    pause
    play sound blow5
    play sound2 clothes3
    scene ds 35 with dis15
    bla "Nancy gets off of you and removes her skirt." with dis15
    mc "*Panting* O-Okay, I just need a second."
    mct "Come on, [mc], you can do it."
    mct "Don't cum yet, don't cum yet, don't cum yet, don't cum yet."
    show ds 36
    n "You good?"
    show ds 35
    mc "Y-Yeah! I'm fine!"
    play sound clothes4
    play soundlow clothes2
    show ds 37b with dis15
    pause .1
    bla "Nancy hops back onto you and guides your cock into herself once more." with dis
    n "Good..."
    play sound3 blow4
    show ds 37
    mc "O-Oh god..."with dis15
    n "Because..."
    play sound2 blow4
    play sound4 penetration2
    play soundlow woodhit
    show ds 38 with vpunch
    mc "S-Shiiiit..." with dis
    n "Because I don't plan to stop riding you until one of us faints..."
    mc "Oh boy..."
    scene nancyele6 with dis2
    n "*Panting* AHHH..." with dis
    n "F-FUCKKK!"
    mc "OH GOD..."
    n "R-RIGHT THERE!"
    mc "Oh, fuck yeah, Nancy..."
    n "AAAAHGH..."
    bla "Nancy's pussy stretches around you, her wet folds surrounding the entire length of your dick."
    bla "The relentless onslaught of her hips is somehow balanced by the dance that her perfect breasts perform in front of you."
    mc "Jesus Christ..."
    n "YEAH... YEAH!"
    n "G-God, I needed this {i}so{/i} much, [mc]..."
    n "Y-You have no idea..."
    n "All this time..."
    n "Everything is paying off for this one moment..."
    mc "AAahhh..."
    mc "Y-Yes..."
    mc "FUCK YES!"
    mc "Are you enjoying riding my cock, Nancy?"
    n "Fuck yes, I am..."
    mc "Have you ever taken a cock like mine?"
    n "N-Not even close..."
    pause
    scene black with dis
    scene nancyele7 with dis2
    n "AAAAAHHH..." with dis
    bla "Nancy's screams fill the small enclosed space, echoing against the high ceiling."
    mct "I wonder how thick the walls of the elevator are... could anyone hear us?"
    n "Y-YEAH!"
    mc "G-God..."
    mc "I-I hope there are no security cameras in the elevator."
    n "H-HAH!"
    n "T-That would be quite the spectacle, eh...?"
    n "The poor security guard having to watch the two of us – AGH... FUCK! – h-having sweaty, animal sex in an elevator in the middle of the day..."
    n "O-One for the spank bank, for s-sure..."
    mc "I b-bet..."
    n "AAahh..."
    n "Luckily there are no cameras in this one, since it doesn't go to the labs..."
    mc "Too bad... I'd have liked to take a souvenir home..."
    pause
    n "AAAhh..." with dis
    n "*Panting* Jesus, my legs are going numb..."
    n "I'm not sure I can..."
    scene black with dis
    scene nancyele9 with dis2
    bla "Without letting her finish her sentence, you grab her tightly and begin to slam her." with dis
    n "AAAAAaaaGHH, BABYYYYY!"
    n "*Gritting her teeth* M-MY GOD!"with hpunch
    mc "AAAaghh, fuck, Nancy..."
    n "*Squealing* J-Jesus Christ, y-you're like a fucking bull..."
    mc "All I wish to do is to serve my queen..."
    n "AAAGH..."
    n "Y-Yeah..."
    n "That's it..."
    n "Harder..."
    n "H-HARDER!"with hpunch
    n "Fuck your queen, [mc]..."
    n "F-Fuck your queen with that m-monster fucking cock of yours..."
    n "AAAAghh!"
    mc "*Panting* I can feel you soaking my cock with your juices..."
    n "AAAhhh F-FUCK, t-this is insaaaanee..."
    n "AAAAH!"with hpunch
    mc "Let me hear you scream like that... I fucking love making you feel that way..."
    pause
    scene black with dis
    scene nancyele8 with dis2
    bla "Nancy's voice rises in pitch as you hammer away inside her, fucking her for all you're worth." with dis
    n "*Screaming* AAAAAAAGHHH!" with hpunch
    mc "Oh f-fuck yeah!"
    n "*Squealing* AAAAaaaaaahh...."
    if nancymommy:
        mc "What a naughty mommy... what if your daughters could see you being fucked like this?"
    else:
        mc "What a naughty empress... what if your subjects could see you being fucked like this?"
    n "*Screaming* AAAAAaahh..."
    mc "Do you like being fucked roughly by me?"
    n "I-I LOVE IT..."
    n "AAAaahh..."
    mc "I knew it..."
    n "*Panting* M-Make me yours, [mc]..."
    bla "Each wild slam of your hips hits the deepest parts of Nancy’s inner cavity."
    n "Oh m-my god, I'm gonna cum, [mc]..."
    n "You're gonna make me cum..."
    n "Keep fucking me like this, please..."
    n "I-I'm almost there..."
    n "AAAAAAHHH..."
    n "J-Just a bit more, baby..."
    if nancymommy:
        n "M-Make your mommy cum!"
    else:
        n "M-Make your queen cum!"
    pause
    play sound cum1
    play sound2 cum2
    play sound3 slap1
    scene ds 39
    n "AAAAAAARGH!!!!" with hpunchlong3
    bla "Nancy's body trembles as wave after wave of pleasure runs through her entire body. Her thighs squeeze against you, and you wince from the stress of not cumming right then."
    n "*Recovering her breath* My god..."
    n "GGGGggghh... This one was even better than the orgasms you gave me in Semper Invicta..."
    play sound6 clothes3
    show ds 40b with dis15
    n "*Struggling to her feet* Dear Lord..."with dis08
    n "How the hell do you do it..."
    play sound3 woodhit volume 0.5
    play soundlow elevatorstop
    show ds 40
    mc "*Pushing her against the wall* Come here..."with dis
    n "*Panting* W-What are you doing..."
    mc "We're not done yet, Nancy..."
    n "W-What?"
    n "I-I can't continue! I'm exhausted, [mc]..."
    mc "Don't worry, my queen, just lean against the wall and let me do the work here..."
    show ds 41
    n "*Giggles* Y-you're fucking nuts."with dis14
    n "Are you never satiated?"
    mc "I could never get my fill of you..."
    scene nancyele10 with dis2
    n "AAAAAARGGGHH... g-good Lord have mercy..." with dis08
    n "*Screaming* AHHHH!"
    n "[mc!u]!!!" with vpunch
    mc "M-My god..."
    mc "Your pussy is so fucking addictive..."
    mc "I can't stop myself..."
    n "AAAahh..."
    n "D-Don't stop then..."
    n "F-Fuck me again, [mc]..."
    n "P-Pin me against the wall and fucking lay into me!!"
    n "GGGGaghh!" with vpunch
    n "M-Make a mess of me, baby..."
    mc "I'm gonna fuck the shit out of you..."
    n "Oh my gggawd..."
    mct "It’s taken me everything I have not to cum already."
    mct "I want this sensation to last as long as possible, but... I can’t help but want to pound Nancy’s cunt until I collapse..."
    mc "Oh, Nancy..."
    n "Ohgaaawf..."
    mct "She's completely gone... the things she's saying don't even make sense anymore."
    bla "You pump your cock in and out of Nancy's lascivious body for several minutes until her ass cheeks start reddening."
    pause
    mct "Think I can shift up one more gear..."with dis
    scene black with dis
    scene nancyele11 with dis2
    n "*Screaming* AAAAAAAGH..." with dis
    n "AAAAH!" with vpunch
    mc "Oh god, Nancy, I'm getting close..."
    n "I'm c-c-cummingg already... a-again....."
    mc "I'm g-gonna cum too..."
    n "*Panting* I-If you’re gonna cum, then cum, baby..."
    n "*Panting* Don’t worry about this being the only time we do this... I p-promise we’ll do it again..."
    n "Now cum for me, let me take care of you..."
    if nancymommy:
        n "Cum for mommy, baby..."
    else:
        n "Cum for your queen, baby..."
    n "G-GOD!" with vpunch
    mc "FUUUUCK, I'M..."
    n "W-WAIT! D-D-DON'T CUM INSIDE!!"
    mc "I'm almost there..."
    n "N-Not inside!" with vpunch
    n "AAAHhh!"
    n "I c-can't have another child!"
    mc "*Panting* W-Would that be that bad...? Look at these hips, Nancy... I’m p-pretty sure you’re meant to have some more kids..."
    n "[mc] s-s-stop joking!"with vpunch
    mc "Oh fuck..."
    mct "Oh god, this is gonna be harder than she thinks..."
    mct "I wanna fill her up so badly..."
    mct "I can’t upset her, though... not if I want to do this again..."
    n "[mc!u]!!!" with vpunch
    mct "Oh fuck, I'm gonna–"
    play sound ["<silence 0.4>", blow4]
    play sound2 ["<silence 0.4>", blow5]
    scene ds 43 with dis
    bla "You pull out at the last second." with dis08
    play soundlow slap1 volume 0.5
    play sound4 cum1
    play sound5 cum2
    play sound6 cum3
    show ds 44
    mc "AAAAAAAAAAAAAAHHHH..." with hpunch
    play sound cum1
    play sound2 cum2
    play sound3 cum3
    mc "AAAaaaaaahh..." with vpunch
    n "*Orgasming again* AAaaaahh..."with vpunch
    stop music3 fadeout 14
    play soundloop2 vent volume 0.4 fadein 6
    show ds 45 with dis17
    mc "*Hyperventilating* Jesus fucking Christ..." with dis
    mc "Oh Nancy..."
    mc "I don’t think I've ever cummed so hard in my life..."
    n "*Exhausted chuckle* Hah..."
    n "Is it that bad?"
    mc "Well, you're definitely gonna need a shower when you get home..."
    mc "God..."
    mc "Nancy, this was..."
    n "*Still breathing heavily* D-Don't even try it. I can’t describe it either..."
    n "Where did you learn to–"
    play sound ding
    play soundloop fan volume 1.3
    stop soundloop2 fadeout 3
    show ds 45 with vpunch
    pause .3
    play sound2 woodhit
    play sound3 elevatorstop volume 0.3
    show ds 46
    n "*Leaning against the wall* Oh no."with dis12
    show ds 47
    mc "What's this?"
    show ds 46
    n "T-The elevator! Someone called it!"
    stop soundloop
    $ renpy.end_replay()





label ga_penny2:
    show dpp 30 with dis
    p "Finally! I think she left, [mc]!"with dis
    p "Phew, that was close!"
    show dpp 31
    mc "C-Cool, just be careful when going out, there's a..."with dissolve
    stop music fadeout 6
    play musicb night fadein 6
    play sound2 dooropen2
    play sound doorsqueakk
    show dpp 33
    p "*Opens the wardrobe door* O-Oh SHIT!" with dis08
    mc "B-Be careful with–"
    play sound fall2 volume 1.4
    play sound2 fall
    play sound3 fall3
    scene dpp 34 with vpunch
    pause 0.9
    mc "Ouch..." with dis
    mc "A-Are you okay?"
    p "*Laughs* Hahaha!"
    mc "*Chuckles* What are you laughing at?"
    p "*Chuckles* Nothing, I'm just laughing at the absurdity of this situation."
    p "Oh god..."
    p "At this point I don't care about Regina anymore. I don't even care about that damn yearbook."
    play sound clothes4
    show dpp 35
    p "Honestly? I just want to spend time with you doing cra..."with dis12
    show dpp 36
    p "C-Crazy..." with dissolve
    play sound2 clothes2
    play sound3 clothes4
    show dpp 37
    p "*Jumping up* [mc]!!"with dis06
    show dpp 38
    mc "What?" with dis
    p "Y-Your toga! Y-You're..."
    show dpp 39
    mc "Huh?" with dissolve
    show dpp 40
    mc "*Awkward laugh* Oh... erm... shit." with dissolve
    play sound clothes4
    show dpp 42
    mc "*Standing up* It's just that... that wardrobe was way too small, and..."with dis
    show dpp 41
    p "W-Where are your underpants? Have you been going commando all night?"
    show dpp 42
    mc "Um... yeah, I didn't want them to ruin my costume."
    p ". . ."
    show dpp 41
    p "My fucking god, [mc], you're hung like a fucking horse. That cock is a weapon!"
    if not dare1:
        p "I thought you were messing with Regina when she asked you how big you were."
        p "Now I think you were underselling it."
    show dpp 42
    mc "Uh?"
    mc "But you stared at me before the party. In the shower."
    mc "Didn't you?"
    show dpp 41
    p "Well, y-yeah, but you weren't hard. And you were in the shower."
    p "There must have been... shrinkage or something, I don't know. Now it's like... three times the size."
    show dpp 42
    mc "I-I've just been trying to keep it in check all night."
    mc "But it doesn’t help that you’ve been teasing me, Penny..."
    mc "And the fact that you can't take your eyes off it isn't helping either..."
    mc "Actually, it's turning me on even more."
    show dpp 43
    p "*Laughs* EXCUSE ME? Now your donkey dick is my fault?" with dis
    show dpp 44
    mc "Oh, absolutely."
    if novadildo or holdondildo:
        if pennyshower:
            mc "Our conversation in the bathroom, the locker room when I asked you for a bra, the truth or dare game..."
        else:
            mc "First the locker room when I asked you for a bra, then the truth or dare game..."
    else:
        mc "First our conversation in the bathroom, then the truth or dare game..."
    if dare3:
        mc "I even dared you to flash me, and you snaked your way around that! You ruined the sanctity of Truth or Dare, in my opinion."
    mc "It’s like you’re trying to set a world record for bluest balls!"
    mc "Pretty rude to your manager, if you ask me. I might have to shelve you for my other clients..."
    show dpp 43
    p "*Giggles* What other clients?"
    p "And it's not my fault that you're a horny dog."
    p "Are you telling me that I'm to blame for you getting an erection at awkward moments? I don’t think it’s my fault that you can’t control yourself around me..."
    show dpp 44
    mc "It’s your fault, a hundred percent."
    mc "It's been like torture."
    show dpp 43
    p "*Giggles* Oh my, I had no idea you were suffering this much, baby!"
    p "I'm so sorry."
    show dpp 44
    mc "Nuh-uh, I don't forgive you."
    show dpp 43
    p "*Chuckles* Pretty please... [mc]?"
    show dpp 44
    mc "Nope."
    show dpp 43
    p "Come on..."
    p "Isn’t there anything I can do for you to forgive me?"
    p "I’m {i}so{/i} very sorry for flaunting my lewd body in front of you, [mc]. I had no idea it would cause you so much stress..."
    play music2 pennysong fadein 20
    show dpp 44
    mct "I like where this is going..."
    stop musicb fadeout 10
    mc "Well, as compensation for all the teasing that you've made me go through..."
    mc "What if you let me see what you’re hiding under that dress...?"
    show dpp 43
    p "You want to see me naked? The photoshoot wasn’t enough for you, perv?"
    show dpp 44
    mc "Oh, but now it's different. That day was strictly professional."
    mc "I was just performing my due diligence as a prospective manager."
    show dpp 43
    p "And today?"
    show dpp 44
    mc "Today it's... a personal request."
    show dpp 43
    p "A personal request, huh?"
    show dpp 44
    mc "Just a quick boobie flash! That's all I’m asking for."
    show dpp 43
    p "And what's in it for me?"
    show dpp 44
    mc "Hmm... my forgiveness?"
    p "*Snorts* Hmm."
    mc "And the possibility to keep working with the most respected manager in Kredon."
    mc "It's a pretty sweet deal, if you ask me."
    show dpp 45
    p "Hmm."with dissolve
    show dpp 43
    p "Here?"with dissolve
    show dpp 44
    mc "Here..."
    show dpp 47
    p "Okay, superstud... you’ve convinced me."with dis12
    p "I guess you have a point. I really wouldn’t want to risk upsetting my manager..."
    p "*Giggles* And honestly? The truth is that I've definitely been teasing you for quite a bit... and it’s been very, VERY fun."
    show dpp 46
    mct "Oh yes... FINALLY!"
    show dpp 47
    p "Okay, take a good look, [mc]."
    p "It won't last..."
    play sound clothes4 volume 1.3
    show dpp 48 with dis15
    bla "Penelope slips off the top of her dress, her bare breasts heaving before your eyes." with dis
    mc "Oh, fuck yes..."
    show dpp 49
    mc "I'd forgotten how perfect they were, Penny." with dis12
    mc "I suspected you weren't wearing a bra when I saw you in that dress. With tits like yours, you wouldn’t even need one."
    show dpp 50
    p "Happy now, Mr. [lastname]?" with dis
    p "Do you forgive me for acting naughty? For being such a tease? For flaunting myself all around you?"
    mc "Not quite yet, Miss Carter..."
    mc "You'll have to try much harder."
    play sound clothes4 volume 1.3
    show dpp 51 with dis15
    p "*Giggles* Okay, okay..."with dis08
    p "Hmm, I wonder what else I could do...?"
    p "How about..."
    play sound2 clothes4 volume 1.3
    show dpp 52 with dis15
    mc "Much better..."with dis
    mc "My god, this was worth the wait... I’ve been wanting to see you like this ever since I saw that first pic on Instagram..."
    show dpp 53
    bla "Penelope continues stripping for you. She leans softly against the bedpost, and curves her rear into an inviting pose." with dis15
    show dpp 54
    p "Okay... I don't have a single piece of clothing left on me."
    p "This should more than compensate you for all the teasing. I hope you enjoyed the spectacle."
    show dpp 53
    mc "Penny... you're a fucking goddess."
    mc "Your face, your ass, those gumdrop nipples... you’re making a man drool..."
    show dpp 54
    p "Yeah, I can tell that you're liking the show."
    p "Your cock has been growing redder and redder throughout this little exhibition... not to mention bigger."
    show dpp 53
    mc "I’m not the only one enjoying this. You like showing off for me, don’t you?"
    mc "You like when I gaze at your bare tits..."
    mc "Admit it. You like being my personal little model, Penny."
    show dpp 54
    p "I could say the same thing about you. [mc] Junior seems to be really enjoying himself."
    p "*Giggles* You should see your face."
    p "I'd love to know what's running through your mind right now."
    show dpp 53
    mc "Well, since you asked... I was thinking about how those huge, heavy tits of yours would feel in my hands."
    show dpp 54
    p "Oh, really...?"
    p "Well..."
    p "In the interest of science... do you wanna feel for yourself?"
    show dpp 53
    mc "Wait... are you serious?"
    p "Mm-hm..."
    show dpp 54
    p "Yeah, why not? You’ve caught me in a pretty good mood."
    p "Treat yourself..."
    show dpp 55
    bla "You move closer to Penelope, frantically trying to memorize every square inch of the model’s ethereal body." with dis2
    mc "God..."
    play sound clothes3
    show dpp 56
    bla "Your hands enclose both of her breasts, indulging in their warmth and tenderness. Penny releases a little squeak of surprise." with dis14
    p "Aaah..."
    show dpp 57
    mc "Dear Lord, they feel so incredibly soft..." with dis12
    show dpp 56
    mc "They're firm enough not to sag... yet, they’re so supple."with dis12
    show dpp 57
    mc "And I can barely fit them in my hands..."with dis12
    show dpp 58
    mc "*Grabbing her by the waist* Can I try one last thing before we end this, Penny?"with dis
    p "W-What? What are you gonna do?"
    mc "Something I've been dreaming about since I first spotted you and your “assets” in Kredon."
    show dpp 59
    bla "You wrap your mouth around Penelope’s erect nipple, and begin licking the “best tits on Instagram.”" with dis14
    p "W-What are you doing...?"
    show dpp 60
    p "Oh fuck..." with dis14
    show dpp 61
    p "*Giggles* You're crazy, [mc]..." with dis
    p "Although... I've gotta say that I kinda love your cockiness."
    scene pennyparty1
    bla "You wrap your arms around Penelope's waist, holding her in place with a firm grip before beginning to suck on the blonde's voluptuous breasts." with dis2
    p "Damn, [mc]..."
    p "Mmmm..."
    p "F-Fuck, keep sucking..."
    p "I d-didn't know I was so sensitive there..."
    mct "Jesus Christ..."
    mct "Her skin, her scent, the heat she radiates..."
    mct "This feels like a goddamn dream come true."
    p "MMmmmmmm..."
    scene pennyparty2
    bla "Unable to resist, you suck on Penelope's breast as hard as you can, alternating between little nipple flicks and small bites, determined to leave some sort of mark." with dis2
    p "Aaahh... y-yeah... you're doing such a good job..."
    mct "There are thousands of men in Penelope’s DMs who would pay exorbitant amounts of money just to see her naked."
    mct "Yet here I am, seeing them up close and personal."
    mct "No... not only that... I'm feeling her... I'm tasting her..."
    mct "She's mine... For at least tonight, Penelope Carter is all mine..."
    p "Aaaah!"
    mct "I feel like I could do this all night."
    mct "I just want to devour her..."
    scene dpp 63
    p "*Shoving your face away* Okay, okay, that's enough!" with dis12
    show dpp 62
    mc "Aw, really? I was just starting to enjoy myself!"
    show dpp 63
    p "*Giggles* You've been enjoying it since the beginning."
    p "Besides, [mc] Junior over there was constantly poking me down here, in case you didn't notice."
    show dpp 62
    mc "Not my fault. Your tits are literally making me lose my mind, Penny."
    show dpp 63
    p "You {i}really{/i} like my tits, huh?"
    show dpp 62
    mc "“Like” is an understatement."
    mc "I want to worship them on an altar."
    show dpp 63
    p "*Giggles* You're a filthy little degenerate."
    show dpp 62
    mc "Can't deny it. What can I say, your tits bring it out of me."
    p "Hmm..."
    show dpp 64
    p "You know what..." with dis12
    p "Since you seem to like them so much..."
    play sound chair1
    show dpp 65 with dis12
    p "*Shoving you down to the couch* How about I give you a little memory that’ll truly be unforgettable..."with dis08
    show dpp 66
    mc "Oh god..."
    show dpp 65
    p "*Giggles* Jesus, [mc], how long can you keep up an erection like that?"
    show dpp 66
    mc "With your naked body in front of me? Probably hours."
    mc "I mean... holy fuck, Penny."
    mc "Your body is almost indescribably perfect. It’s like someone pushed all your body’s features to their max settings."
    show dpp 65
    p "Well, I'm not the only one with their “features” pushed at the max here..."
    play sound2 chair4
    show dpp 67
    bla "Penelope kneels between your legs and ties up her hair." with dis12
    show dpp 68
    p "Well..." with dis12
    mc "O-Ooh god..."
    p "We're gonna have to do something about this, don't you think?"
    p "We can't go back to the party with you in this state."
    p "What if it slips out of your costume again? We can’t have Nova or another girl accidentally catching sight of this monster dick, can we?"
    show dpp 69
    mc "Definitely... there have already been too many wardrobe malfunctions tonight..."with dis
    mc "Did you have a plan in mind?"
    show dpp 70
    bla "Penny grabs both of her boobs and quickly buries your cock between them." with dis14
    mc "OH GOD..."
    scene pennyparty3 with dis2
    mc "Oh my fucking GOD."with dis
    mc "They're so damn warm..."
    p "*Giggles* I can imagine. Do you like feeling my big titties wrapped around your cock like this?"
    mc "Fuck me, keep going..."
    mc "I love it when you stare into my eyes, Penny..."
    mc "Keep looking at me with that face... It’s like you’re drenched in lust..."
    p "*Giggles* I confess that doing this in Regina's dorm is kind of... arousing. We could get caught at any... single... moment."
    scene dpp 71
    mc "AAAahh yeah..." with dis12
    mc "My god, Penny, please don't stop..."
    scene pennyparty4 with dis2
    bla "Your dick begins to lubricate itself with precum, and, as if motivated by the liquid, Penny increases her pace with a quiet determination." with dis
    bla "Her eyes flit back and forth between your face and the meat buried in her chest."
    mc "O-O-Ohhh fuck yes, that's it..."
    mc "T-This is amazing..."
    mc "The “{i}Best tits on Instagram{/i}”, eh...?"
    mc "How many DMs have you gotten about this exact situation?"
    p "*Giggles* I've lost count."
    p "They offer me money, gifts, and even trips sometimes!"
    mc "Aaaahh... this feels so good..."
    p "I rejected all their requests, but here I am doing it for free, for some high school kid with a fat dick."
    p "Not a very good business move, I guess..."
    mc "*Chuckles* Y-You won't catch me complaining..."
    mc "But I’m not just some high school kid, y’know..."
    pause
    play sound chair3
    scene dpp 72
    bla "You stand up and seize Penelope's breasts with your hands, your dick still trapped between them." with dis
    mc "I think it’s time for me to take the lead, Penny..."
    mc "You're okay with it, right?"
    p "Yeah, I guess you can take a shot..."
    $ renpy.music.set_volume(0.35, delay=7.0, channel='music2')
    scene pennyparty5 with dis2
    mc "Aaaahh... yeah!" with dis
    mc "YEAH!"
    mc "That's it, Penny..."
    mc "Keep staring into my eyes like that..."
    mct "My fucking god, Penny's cleavage feels like fucking a pussy..."
    mct "I'm FUCKING the best tits on Instagram!"
    pause
    mc "AAaaahh..."with dis08
    bla "You thrust into Penelope’s cleavage frantically, your balls slapping against her tummy with each stroke."
    mc "This sensation is amazing..."
    mc "AAaahhh..."
    mc "A-Am I squeezing them too hard?"
    p "I like it that way..."
    p "*Giggles* It feels good when you’re a little rough with them..."
    p "Being used for your pleasure like this is... pretty fucking hot, not gonna lie."
    mc "Oooh god... you’re a naughty girl, aren’t you..."
    mc "You're gonna make me cum way too quickly..."
    play sound clothes4
    scene dpp 73 with dis
    bla "You abruptly grab Penelope and lift her to her feet." with dis
    p "W-Why did you stop?"
    mc "I don't wanna finish yet..."
    p "You don't?"
    mc "Not yet, babe..."
    show dpp 74
    p "F-fuck... y-you're..."with dis
    show dpp 75
    p "Y-You're touching my pussy with your dick..."
    mc "Your lips are literally dripping over my cock, Penelope..."
    mc "I don’t think it would be fair if I was the only one to cum tonight... Besides, you’ve been so generous tonight..."
    mc "And you’re so... tempting..."
    show dpp 73
    p "Don’t even think about it, [mc]."with dis
    p "W-We're not gonna f-fuck. I’m not a first date kinda girl, y’know..."
    p "Besides, we don't even have a condom..."
    mc "Oh... so a condom is what’s stopping us? If I had one, we would be fucking right now?"
    show dpp 75
    p "*Giggles* I didn't say that."with dis
    p "We’ve already done so much tonight. You’re not satisfied yet?"
    play sound clothes4
    play soundlow clothes1
    scene dpp 76
    bla "You turn Penelope around and slide your penis between her thick thighs again." with dis12
    p "Aahh..."
    scene pennyparty6 with dis2
    p "AAaaaah... What are you d-doing to me?" with dis
    bla "You carefully begin to slide your dick between Penelope's legs, each thrust slightly spreading apart her pussy lips."
    mc "Oh god, Penny..."
    p "Fuck, [mc]..."
    mc "You're actually dripping..."
    mc "Did you get that turned on from having my cock between your tits?"
    p "AAaahhh..."
    pause
    mct "I know she'd get mad just for trying, but..."with dis08
    mct "I’m literally going insane trying to not bury my cock balls-deep inside of her."
    p "*Slight moan* AAaahh..."
    mc "Do you like this? Gliding your pussy along my cock?"
    p "I-I do... I like it a lot..."
    p "Move faster... please move faster..."
    mc "You want it faster? Tell me, Penny..."
    p "Y-Yesss!"
    menu:
        with dis
        "Romantic approach":
            play sound2 clothes4
            scene pennyparty7 with dis2
            bla "You hasten your pace, slamming your hips against Penelope's generous buttocks while exhaling small breaths on her neck." with dis
            p "AAAAhhh..."
            mc "Ohhh Penny..."
            mc "This feels so fucking good..."
            p "AAaaahh..."
            p "I-It d-does... s-so fucking good..."
            p "K-Keep up that pace, [mc]..."
            bla "Penelope squeezes her legs together, and more juices drip down her thighs. Your dick begins to slide even more smoothly against her lips."
            mc "Oh g-god, yes..."
            pause
            p "MmmMmmm..." with dis08
            mc "I know you were craving for this..."
            mc "I know you fingered yourself thinking about me..."
            mc "Don't think I forgot what you said that day in Warthogs, miss..."
            mc "Or are you gonna tell me that was all a lie?"
            p "*Giggles* A-A-AAhhh..."
            p "I-It was just because you were the only guy in the house..."
            p "*Moaning* AAaaahh..."
            p "Y-You’re telling me you haven’t jacked off to me since arriving in Kredon?"
            p "The walls aren’t that thick y’know, it’s amazing what you can hear in the hallway during a midnight b-bathroom trip..."
            mc "Aaah..."
            mc "You’re right, I haven't been able to stop dreaming of spending a night with you in weeks..."
            p "Aaaahh..."
            mc "My only wish is seeing your divine body writhe in pleasure..."
            p "AAAaaHhhh..."
            mc "After I pump it... all... night... long..."
            p "AAAAAAAAAAAGHH..."
            p "F-Fuck, [mc]... I'm gonna cum..."
            mc "M-Me too..."
            mc "God, Penny..."
            mc "F-Fuck, I'm about to..."
            p "Y-YEAH!"
            p "Cum for me, baby..."
            mc "F-Fuck, I can't stop it..."
            p "AAAAH..."
            play sound cum2 volume 1.5
            play sound2 cum1
            play sound3 cum3
            play sound4 slap1
            scene dpp 77
            mc "AAAAAAAGGHHH!" with hpunch
        "Rough approach":
            play sound2 clothes4
            scene pennyparty7b with dis2
            bla "Your hands wrap around Penelope’s soft neck as you hasten your pace, your hips slamming relentlessly against the blonde's buttocks." with dis
            p "Mmmghhh... y-yess..."
            mc "Ohhh Penny..."
            mc "This feels so fucking good..."
            p "AAaaahh..."
            p "I-It d-does... s-so fucking good..."
            p "K-Keep up that pace, [mc]..."
            bla "Penelope squeezes her legs together, and more juices drip down her thighs. Your dick begins to slide even more smoothly against her lips."
            mc "Oh g-god, yes..."
            pause
            p "MmmMmmm..." with dis08
            mc "You love this, don't you? My hands wrapped around your neck, thrusting into you from behind..."
            mc "I know you want to be fucked roughly... I know you like ropes..."
            mc "You want everyone to treat you like a princess, but really you’re a kinky little girl, aren’t you, Penny...?"
            mc "Don't think I forgot what you said that day in Warthogs, miss..."
            mc "Or are you gonna tell me that was all a lie?"
            p "*Choking* A-A-AAhhh..."
            p "*Giggles* I-It w-wasn't a lieeee..."
            p "I-I want to be fucked so hard that my pussy is sore the n-next day..."
            mc "Ohh... f-fuck me, Penny..."
            mc "You like me using your body as a toy, don't you?"
            p "*Choking* Y-Yeagh... u-use me as your fucking toy, [mc]..."
            mc "I wanna make your body writhe in pleasure, Penny..."
            p "AAAaaHhhh..."
            mc "After I pump it... all... night... long..."
            p "AAAAAAAAAAAGHH..."
            p "*Choking* F-Fuck... I'm gonna cum, [mc]..."
            mc "M-Me too..."
            mc "God, Penny..."
            mc "F-Fuck, I'm about to..."
            p "Y-YEAH!"
            p "Cum for me, baby..."
            mc "F-Fuck, I can't stop it..."
            p "AAAAH..."
            play sound cum2 volume 1.5
            play sound2 cum1
            play sound3 cum3
            play sound4 slap1
            scene dpp 78
            mc "AAAAAAAGGHHH!" with hpunch
    p "Aaah!"
    play sound cum2 volume 1.5
    play sound2 cum1
    play sound3 cum3
    mc "AAAAAARRGGHHH..." with hpunch
    show dpp 79 with dis2
    mc "Goddamn..."with dis08
    mct "I needed this so badly... my blue balls were about to fucking explode..."
    stop music2 fadeout 10
    play music night fadein 7
    play sound ["<silence 0.4>", fall2]
    show dpp 80
    mc "*Sitting down on the floor* Holy shit..." with dis15
    mc "You're something else, Penny..."
    show dpp 83
    p "Me? You're fucking crazy..."
    p "How’d you convince me to get you off in my archenemy’s room?"
    show dpp 80
    mc "*Chuckles* Hah!"
    mc "Like you're one to talk!"
    show dpp 83
    p "I'm gonna have to ask you to come to all the parties I'm invited to from now on, [mc]."
    p "Tonight's was... definitely the craziest one I've ever had."
    show dpp 80
    mc "Agree with you there, that's for sure..."
    mc "But hey, going crazy sometimes is worthwhile, don't you think? Imagine if we’d never decided to sneak in here tonight..."
    show dpp 83
    p "Oh, for sure."
    p "What's life without going a little crazy from time to time?"
    show dpp 80
    mc "I like the way you think, miss."
    show dpp 82
    p "So... what should we do about that?" with dissolve
    p "You sure emptied yourself. It was like a fire hose!"
    show dpp 79
    mc "Oh, the jizz?"
    mc "Um... should I clean it? Guess I can look around for some sprays..."
    show dpp 82
    p "Uh..."
    show dpp 83
    p "Nah, fuck it." with dissolve
    p "It's my payback for the yearbook."
    show dpp 80
    mc "*Laughs* I wish I could see Regina's disgusted face when she sees that puddle."
    show dpp 83
    p "I guess I'll settle for seeing it in class."
    show dpp 80
    mc "*Chuckles* Make sure to tell me about it after!"
    show dpp 83
    p "Will do."
    p "But anyway... we should get dressed and get the fuck out of here before someone finds us."
    show dpp 80
    mc "Just let me say goodbye to my beloved twins before you cover them."
    mc "I'll miss you, girls."
    mc "I’ll always cherish the time we’ve spent together."
    show dpp 83
    p "*Snorts* You're such a dork. You’re lucky I think you’re cute."
    stop music
    $ renpy.end_replay()






label ga_nova2:
    play soundloop clock fadein 1
    scene dr57 with dis
    no "Now we wait."with dis
    mc "Cool..."
    stop music3
    play sound ding
    scene dr 58
    pause
    mc "*Taking a deep breath* (Okay...)" with dis08
    mct "This..."
    play sound4 chair3
    play soundloop2 beat2
    stop soundloop
    scene clockwhoosh05
    mc "*Hyperventilating* (THIS IS NOT COOL.)"with hpunch
    mct "What the fuck was in that wine..."
    mct "I'm hornier than an off-duty marine in Thailand."
    mc "*Taking another deep breath* . . ."
    mct "Jesus, I'd even fuck a watermelon if there was one in front of me."
    mct "And what's with this huge erection? It's starting to hurt, even."
    mct "Was there Viagra in that damn drink?!"
    mc ". . ."
    scene dr 60
    mct "Am I the only one having a meltdown right now?" with dis
    show dr 61
    bla "You can see Nova curled up on her chair nervously jiggling her legs."with dis12
    no "(Oh god.)"
    no "(OH MY FUCKING GOD.)"
    no "(I NEED TO TOUCH MYSELF.)"
    no "(What is happening to me?!)"
    no "(At this rate I'll end up seeping through my pants.)"
    no "(I haven't felt this horny since that day in the Egyptian server.)"
    no "(Oh no, Nova, don't think about that again...)"
    no "(Not again...)"
    no "(Stop thinking about that day...)"
    no "(God, that day...)"
    if maatsex:
        if maatsexvariant:
            no "(I wish that [mc] fucked ME against the wall, not Maat...)"
        else:
            no "(I wish that [mc] fucked ME against the ground, not Maat...)"
        no "(The way she was moaning with pleasure...)"
        no "(There was... so much force in those thrusts...)"
        no "(The noise of [mc]'s hips slamming against hers...)"
        no "(I’ve never played with anything that big. C-Could I even take it...?)"
    else:
        no "(I wish [mc] would have fucked me that day...)"
        no "(Oh Jesus...)"
    mc "*Clears throat* So..."
    mc "Still good, Nova? Are you feeling anything?"
    stop soundloop2 fadeout 25
    $ renpy.music.set_volume(0.38, channel='music3b')
    play music3b silverware fadein 25
    show dr 65
    no "Um..." with dis12
    no "P-Perhaps just a tiny, liiittle, small something, y-yeah."
    no "Y-you?"
    show dr 62
    mc "I don’t think I've ever felt hornier in my life."with dissolve
    no ". . ."
    show dr 65
    no "O-Okay, I lied. ME TOO. I-I don’t think I’ve ever felt so... slick." with dis08
    no "I-I guess we’re both in this boat together, eh? Haha..."
    no "Who would have thought that drink would really work, huh?"
    mc "*Nervous laugh* Y-Yeah, right? Crazy."
    show dr 62
    no "I have like... t-this weird sensation inside..."with dissolve
    no "Like a..."
    show dr 65
    no "Burning."with dissolve
    no "It’s like something is making me just want to... tear off my clothes and go to town on myself..."
    mc "Right?!"
    show dr 64
    no "Must be the wine."with dissolve
    show dr 62
    mc "I guess so."with dissolve
    no ". . ."
    no "Are you..."
    show dr 65
    no "A-Are you hard?" with dis08
    show dr 62
    mc "Um... yep. I've been stiff for quite some time already."with dissolve
    no ". . ."
    show dr 64
    no "Makes sense. Can't blame you."with dissolve
    show dr 62
    mc "So... wetter than you’ve ever been, huh?"with dissolve
    show dr 65
    no "Well..."with dissolve
    no "Yeah. My panties are just so... damp."
    no "Y-You know, the wine."
    mc "Yeah, the wine..."
    show dr 62
    mc "Isn't it funny how we always end up stuck in the most bizarre situations?"with dissolve
    mc "First, we're taken as hostages by a crazy Egyptian nympho... and now this."
    show dr 64
    no "Oh, that day... y-yeah, I'd forgotten about it."with dissolve
    no "But... well, this is different."
    no "That time we were forced to... get intimate. This time it's just the opposite."
    no "Easier."
    show dr 65
    no "Much easier."with dis06
    show dr 62
    mc "That blowjob, though?"with dis06
    mc "My god, I'd go broke just to repeat that right now."
    show dr 65
    no ". . ."with dis06
    no "You're saying that because of the wine."
    mc "Ehh... I'm not so sure, to be honest."
    mc "I've been thinking about it since that day."
    mc "It was... fucking amazing."
    mc "Those faces you made, Nova... The way you started choking..."
    show dr 64
    no "I mean... it was... entertaining, I guess. I was trying to make it look a-accurate, for Maat."with dis08
    no "I-I mean it’s not like I... wanted to..."
    show dr 65
    no "*Clears throat* B-But anyway, let's change the subject. This is not helping."with dis06
    mc "Yeah..."
    mc "How much time is left?"
    no "I don't even wanna know."
    mc "You know..."
    mc "I had an idea that would make this much easier for both of us."
    no "I'm all ears..."
    mc "There's a way we could reduce this craving we're feeling."
    mc "We could... touch ourselves."
    show dr 63
    no "WHAT?!" with dissolve
    mc "Think about it. A quick wank and all this urge goes away."
    mc "We win the challenge, and everyone's happy."
    show dr 62
    no "You're crazy."with dissolve
    mc "Is that a no?"
    no "It's a... “do what you want”."
    no "I'm n-not touching myself in front of you."
    no "But suit yourself."
    mc "Oh thank god... I don't think I would have held much longer."
    play sound clothes3
    play sound2 clothes3
    play sound3 clothes2
    show dr 66
    bla "You take off the robes that were covering your hips and thighs, releasing your cock in all its splendor." with dis15
    mc "*Sigh of relief* Oh god..."
    mc "Much better..."
    show dr 63
    no "Goddammit, [mc], I thought you'd go to a corner or something!"
    mc "What's the fun in that?"
    mc "And besides, don't act like we haven't seen each other naked before..."
    show dr 65
    no "*Mumbling* Hmm."with dis06
    show mchandjob05 with dis14
    bla "You begin to slowly stroke your dick." with dis12
    mc "AAAaaagh..."
    mc "Man, I needed this so much..."
    mc "No more craving."
    mc "Now the wine only makes the sensation feel... stronger."
    scene dr 65
    no ". . ." with dis12
    mc "I thought you wanted me to go to the corner, Nova? But you can’t even take your eyes off me..."
    no "*Shaking her legs nervously* Hmm."
    show mchandjob052
    mc "Ahhh, yes..."with dis12
    mc "This feels so good..."
    mc "When I close my eyes, I can see you kneeling in front of me that day, Nova..."
    scene dr 65
    mc "Do you remember?"with dis12
    no "*Shaking her legs nervously* Hmm... vaguely."
    mc "Oh fuck, you were so good..."
    mc "And when you hit my cock against your cheek..."
    mc "So fucking sloppy..."
    no "*Hyperventilating* . . ."
    mc "So warm..."
    play sound chairmove volume 1.5
    play sound2 chair2
    show dr 68
    no "OKAY, FINE." with dis
    no "Do you want me to touch myself? FINE, I'll do it."
    show dr 69
    mct "OH YEAH!"
    mc "I only proposed that because it'll help us."
    mc "All I want is for you to win that CPU."
    show dr 68
    no "Yeah... s-so do I."
    show dr 70 with dis14
    pause
    play sound belt
    play sound2 clothes4
    show dr 71 with dis15
    mc "Oh boy..."with dis08
    mc "You have a damn great butt, Nova. Dolores never stood a chance."
    no "*Little giggle* Right?"
    play sound3 chair2
    show dr 72 with dis12
    bla "Nova sits back on her chair, refusing to turn away from your erect member." with dis06
    show dr 73 with dis14
    mct "She's super petite and slim, but she has these thighs... I wish I could shove my face between them." with dis08
    mct "And the way she looks at me... goddamn."
    mc "The sooner you start, the sooner you'll feel better, Nova..."
    show dr 75 with dis14
    no "Yeah... I guess..." with dis08
    show dr 74
    mc "*Fapping faster* Oh, fuck yes..."
    show dr 75
    no "This wine is making my head spin..."
    show dr 74
    mc "If you don't feel comfortable, you can go to the corner, like you said."
    mc "I won't-"
    show dr 75
    no "Nah. I..."
    no "I don't mind."
    no "It's not as if we hadn't done anything before."
    no "This is nothing compared to that day."
    show dr 74
    mc "No arguments from me..."
    play sound clothes3
    show dr 76 with dis15
    bla "Nova moves her panties to the side, exposing her perfectly waxed pussy right in front of you." with dis12
    show dr 77 with dis15
    no "Fuck, my insides are burning..." with dis
    mc "I bet..."
    mc "Now... do it..."
    play soundlow penetration2
    show dr 78 with dis15
    no "AAaaaargh..." with dis08
    show dr 79
    no "Oh... F-FUCK!" with dis12
    mc "Better, right?"
    no "Yeah..."
    scene novadild1 with dis17
    no "*Moaning* M-Much, much better..." with dis
    mc "Told you..."
    no "Mmmm..."
    no "F-Fuck, it feels more intense than usual... for some reason..."
    no "Ahhh..."
    no "This wine..."
    mc "I'm not sure everything is the wine's fault, Nova."
    mc "Admit you enjoy seeing me stroking my cock..."
    mc "You can’t take your eyes off me jacking off, can you?"
    no "*Giggles* Perhaps a bit..."
    no "Perhaps I..."
    no "AAaaah..."
    play sound chair2
    play sound2 belt
    scene dr 80
    no "*Hyperventilating* Ahhhgh..."with dis15
    no "F-Fuck, why doesn’t this burning go away?"
    mc "I don't know, but I feel the same way..."
    play sound3 buttons
    play sound4 clothes5
    show dr 81 with dis15
    no "Aaahh... better..."with dis
    mc "Oh lord, I missed this sight..."
    scene novadild2
    bla "Nova starts fingering herself faster and deeper, turning her attention from her own labor to your dick, and vice versa."with Dissolve(1.85)
    no "AAAahhh, fuck yes..."
    mc "Better...?"
    no "M-Much better, yeah..."
    no "B-But... at the same time..."
    no "I feel hornier and hornier every second."
    no "I-It's not a bad sensation, but..."
    no "It’s as if my body wants... more."
    no "I-Is it not happening to you?"
    mc "It started happening since you started fingering yourself in front of me..."
    no "*Giggles* You're crazy."
    mc "I guess we're just two of a kind, then."
    no "*Moaning* Aaahh..."
    no "I-I guess so..."
    mc "You seem to be enjoying yourself..."
    no "I c-could say the..."
    no "*Moaning* Ahhh..."
    no "I could say the same..."
    no "I..."
    play sound2 chair2
    show dr 82
    no "*Hyperventilating* F-Fuck..." with dis12
    mc "Are you okay?"
    no "Why is this not enough?!"
    mc "You know, I have an idea..."
    play sound3 chair3
    show dr 82b
    no "D-don't move from your chair!"with dis
    mc "I won't!"
    mc "My idea is right behind you, actually..."
    show dr 83
    no "Hmm?"with dis08
    show dr 84
    no "W-Wait, what? The dildo?"
    no "I-I'm not using that."
    mc "Come on... you know you want to..."
    mc "If not for you, do it for me..."
    show dr 83
    mc "I NEED to see you using it."with dis12
    mc "Just this once..."
    no ". . ."
    mc "Imagine how good it would make you feel..."
    no ". . ."
    show dr 85
    no "Fuck."with dis12
    no "D-don't tell my mom what I'm about to do."
    mc "Good girl..."
    play sound chair2
    play sound2 jump1
    show dr 86
    bla "Replacing her embarrassment with curiosity, Nova gets on top of the table with a quick jump and grabs the toy."with dis14
    no "God, this thing is way bigger than I thought."
    mct "I can’t tear my eyes away from her pussy..."
    mct "It looks so fucking tight. She doesn't even mind showing it to me anymore."
    no "...and softer."
    mc "Is it stiff?"
    play soundlow wood
    show dr 87
    no "Um... well... not really."with dis12
    no "I mean, it's rigid, but also flexible."
    no "I guess this way it's easier to..."
    show dr 88
    mc "To put it inside your pussy."with dis
    show dr 87
    no "Y-Yeah, that."with dis
    show dr 88
    mc "You think you can take it all?"with dis
    show dr 87
    no "I can't."with dis
    show dr 88
    mc "Have you ever tried something so big?"with dis
    show dr 87
    no "I-I have toys, but... nothing even half the size of this."with dis
    show dr 88
    mc "Well, there's only one way to test yourself..."with dis
    no ". . ."
    show dr 89
    no "F-Fuck it. I can't hold it." with dis14
    mc "Attagirl..."
    show dr 90
    bla "She lets out a high-pitched whine as soon as she feels the cold surface of the dildo against her pussy lips." with dis12
    no "*Moans* F-Fuck, it's cold."
    mc "It'll get warm soon enough..."
    play sound ["<silence 0.2>", penetration2]
    show dr 91
    no "*Moans* Aaaahhhhhh..." with dis14
    mc "That's it..."
    play sound2 penetration2
    show dr 92
    bla "Nova's vagina offers no resistance as she softly sticks the dildo inside of her." with dis14
    $ renpy.music.set_volume(0.2, delay=6.0, channel='music3b')
    play soundloop wettingdildo1 fadein 3
    scene novadild3 with dis2
    no "AAAaahhh..." with dis
    no "Gggggh..."
    no "T-That's more like it..."
    mc "Is this soothing that sensation you were feeling?"
    no "D-Definitely..."
    mc "*Fapping faster* God..."
    mc "Does it feel better than your fingers?"
    no "Much f-fucking better..."
    no "I feel... f-f-filled."
    mc "I wish I could be the one filling you up..."
    no "*Giggles* AAagh..."
    scene mchandjob053
    bla "Nova stares directly at your dick."with Dissolve(1.5)
    no "Y-You'd be too big for me..."
    mc "Nonsense..."
    mc "You're handling that dildo like such a pro, Nova."
    mc "Think of it like... practice."
    scene novadild3
    no "*Giggles* T-Thank you..." with dis14
    mc "I could slide right in..."
    no "Aaaah..."
    mc "Does my cock turn you on?"
    no "*Moans* F-Fuck, it does..."
    no "Ahhh..."
    mc "Do you like thinking about me sliding all the way into you, Nova?"
    no "*Moans* I-I do..."
    pause
    play sound chair2
    scene novadild4 with dis2
    no "AAAH, FUCK..." with dis
    bla "Nova accelerates the pace of her movements and pushes the dildo as far as her untrained vagina allows her to."
    no "*Moaning* A-A-A-A-AAHH..."
    mc "You liked sucking my cock, didn't you?"
    no "I..."
    no "I did..."
    mc "You say that Maat pressured you into it... but you were already curious, right?"
    no "*Moaning* Fuck..."
    mc "Would you do it again?"
    no "A-Again?"
    no "I mean..."
    no "It was so... juicy..."
    no "So huge..."
    no "So... heavy in my hands..."
    no "*Moans* AAAH!"
    no "W-We've gotta ask Akira where he bought this wine."
    mc "I agree..."
    no "*Pinching her own nipple* It made my whole body so s-sensitive..."
    no "I need... more..."
    no "I..."
    stop soundloop fadeout 3
    play soundlow wood
    scene dr 93
    bla "Nova suddenly comes down from the table."with dis2
    play sound slam
    show dr 94 with vpunch
    pause
    show dr 95
    mc "What's going on?" with dis12
    show dr 96
    no "That pose... doesn't let me..."
    no "...go deep enough."
    show dr 95
    mc "Oh my... are you going to do what I think you're going to do?"
    play sound2 chair2
    play soundlow wood
    show dr 97
    no "*Getting on top of the table* Perhaps... are we going too far?" with dis15
    show dr 98
    mc "Why?"
    mc "We're just playing a game at a party. Nothing else."
    show dr 97
    no "A p-pretty intense game."
    show dr 98
    mc "I like to win. Don't you?"
    show dr 97
    no "I do."
    show dr 98
    mc "And do you still have that burning sensation from the wine?"
    show dr 97
    no "Fuck, I do..."
    show dr 98
    mc "Then we're doing nothing wrong."
    mc "We're gonna win this shit... but we don't have to suffer more than necessary."
    no ". . ."
    show dr 97
    no "I guess you're right..."
    play soundlow wood
    show dr 99 with dis15
    no "I hope you enjoy the show, then."with dissolve
    mc "You know I will..."
    play sound penetration2
    show dr 100
    no "AAAAAHHHH..." with dis14
    play soundloop wettingdildo2 fadein 2
    scene novadild5 with dis2
    no "Aaaaahhhh..." with dis
    no "Oh my god..."
    mc "Oh baby..."
    no "*Panting* F-Fuck..."
    mc "Are you finally feeling better now?"
    no "Better... yeah...."
    no "{bt=4}MmMMm... much better...{/bt}"
    mc "Did you ever get yourself off like this before?"
    no "*Panting* N-No..."
    no "*Panting* T-The toy I have at home can't even stand upright..."
    mc "I already know what to get you for Christmas this year, then."
    no "*Giggles* D-Don't you dare..."
    scene novadild6 with dis2
    no "AAAaaaahhh... y-yeah..." with dis08
    no "*Panting* Fuck, this feels so good..."
    bla "Nova continues to ride the dildo tirelessly while her own juices drip and soak the toy."
    mc "God, I love seeing your ass bouncing like that, Nova..."
    no "*Panting* Do you?"
    mc "But I know you can take it deeper..."
    mc "I know my personal hacker girl can do better than that..."
    no "*Panting* Aaahh... can I...?"
    no "I-Is that what you want?"
    mc "Fuck yes..."
    play soundloop2 wettingdildo3 fadein 3
    stop soundloop fadeout 2
    scene novadild7 with dis2
    bla "Following your command, Nova shoves the dildo deeper and deeper inside her with each bounce until she's able to take it almost entirely." with dis08
    no "AAAAAaaaahh..."
    mc "Good girl..."
    no "Ggggghh..."
    no "*Panting* L-Like this?"
    mc "Oh my fucking god, yes..."
    no "*Panting* AAaahh... aaahhh... ahhhh..."
    mct "She looks so gone... her mind must be going a mile a minute."
    mc "The fact that I'm watching you while you masturbate turns you on, doesn't it?"
    no "*Panting* It does..."
    no "I want you to watch me..."
    no "I w-want you to keep your eyes on me, without l-looking away..."
    mc "How many times have you fantasized about the Egyptian server?"
    no "*Moaning* Aahhh..."
    no "S-So many times..."
    no "God, that was s-so f-fucking hot......"
    no "I couldn’t get the sight of your... c-cock out of my head, [mc]..."
    no "And your groans when I took you into my mouth..."
    no "I think I masturbated for 2 weeks straight t-thinking about it."
    mc "Oh yes..."
    no "But it shouldn't have been so... hot... that was supposed to be... s-scary."
    no "W-Why was it so hot?"
    no "*Panting* Is it bad that I thought about it so much, [mc]? The smells, the sounds..."
    no "The way my heart was racing..."
    no "Am I... broken, [mc]?"
    mc "No, you're not, Nova..."
    mc "You’re just... curious."
    no "AAAaaaahh..."
    no "*Panting* F-Fuck..."
    no "*Panting* I g-got to the bottom..."
    mc "That's my girl..."
    mc "You're such a fast learner, Nova."
    no "*Panting* F-Fuck yess..."
    pause
    play soundloop wettingdildo3 fadein 2
    stop soundloop2 fadeout 3
    scene novadild8 with dis2
    no "*Groaning* AAAaaaAAAAaahh..." with dis
    mc "Oh sweet Lord..."
    no "HHHHhhggg... t-this is so good..."
    mct "I can't stop imagining Nova riding my cock instead of that dildo..."
    mct "She always seems to have infinite energy. I bet she'd be able to bounce up and down for hours until I passed out..."
    mct "Boy, I've gotta live to experience something like that one day..."
    pause
    no "*Groaning* Aaaaahh... f-fuck..." with dis08
    no "F-FUCK! I'm gonna cum, [mc]..."
    mc "The things you said at the cafeteria... they were all lies, right?"
    no "*Groaning with pleasure* Ehh...?"
    no "Ah... y-yes..."
    mc "You ARE looking for someone to fulfill all your kinky desires."
    no "*Groaning* YES..."
    mc "And you want ME to fuck you..."
    no "I'm gonna c-come..."
    mc "I asked you a question..."
    no "AAAAHHhh..."
    mc "Nova..."
    no "YES!" with hpunch
    no "I want YOU to fuck me!"with hpunch
    no "*Panting* Only you..."
    mc "Oh babe..."
    menu:
        with dis
        "Grab Nova and fuck her":
            stop soundloop fadeout 1
            play sound chair2
            play soundlow slam3
            play sound3 penetration2
            play sound7 penetration2
            scene dr 117
            no "W-What...?!"with dis08
            no "No!"
            no "I-I was almost there!"
            play sound5 chair3
            play sound6 wood
            play sound7 clothes1
            play soundlow slam3
            show dr 118
            no "[mc]! W-What the fuck are you doing?!" with dis
            show dr 119
            mc "Nova, I need to feel that tight pussy of yours..."with dissolve
            show dr 118
            no "WHAT?!" with hpunch
            no "We're gonna lose the challenge!"
            show dr 119
            mc "Fuck that challenge..."with dissolve
            show dr 118
            no "I don't... I..."with dissolve
            no "My god, y-your cock is even bigger than the dildo!"
            no "AND WAY THICKER!" with hpunch
            show dr 119
            mc "Imagine how it'd feel inside of you..."with dissolve
            show dr 118
            no "I... eh..."with dissolve
            no "I-I'm not gonna lose my virginity in a lib-"
            no "I-I mean... I don't... I can't!"
            show dr 119
            mc "You said that you wanted me to-"with dissolve
            show dr 118
            no "It was the wine talking!"with hpunch
            no "J-Just dirty talk!"
            no "And the burning is gone already!"
            no "I-It was a great idea, so now we can sto..."
            play sound knock3
            show dr 119
            sir "*Knocking on the door* Hey there, guys!" with dissolve
            show dr 120
            sir "The challenge is over!"with dissolve
            sir "Nova? [mc]?"
            no "F-Fuck! Told you!"with hpunch
            no "G-Get off me!"
            mct "Goddammit..."
            stop music3b fadeout 9
            play music2b partypenny
            play music3 partyfar fadein 6
            show dr 104
            bla "You quickly get dressed again and hide your boner as best as you can."with dis15
            mct "Fuck."
            mct "What the hell happened to me? I knew the challenge was about to end and he could be back any second."
            mct "I got carried away... I need to learn some self-control."
            play soundlow knock1
            sir "Hello?"
        "Let her come":
            no "Oh god..." with dis08
            no "Yeah..."
            no "OH GOD!"with hpunch
            no "I'm coming!"with hpunch
            play sound5 woodhit volume 0.6
            stop soundloop fadeout 1.5
            play sound7 penetration2
            play sound6 penetration2
            scene dr 101 with dis15
            play sound cum1 volume 1.3
            play sound2 cum2 volume 1.3
            play soundlow cum3
            show dr 101
            no "*Groans* AAAAAaaargh..." with hpunch
            bla "Nova lets the full length of the dildo get inside her and orgasms, contracting all the muscles of her slim body."
            play sound cum1 volume 1.3
            play sound2 cum2 volume 1.3
            play soundlow cum3
            no "*Groans* AAaaah..." with hpunch
            play sound4 slam3
            show dr 102 with dis
            no "*Collapsing* Jesus..." with dis08
            show dr 103
            mc "My god..."with dis12
            mc "That was hot as fuck, Nova..."
            no "*Panting* Yeah..."
            mc "Why can't I cum too?! This cursed wine is fucking with me..."
            mc "I'm horny as fuck, but I can't cum!"
            no "*Recovering her breath* That got a bit out of hand."
            mc "You did great. I knew you could take it all..."
            no "*Recovering her breath* It sure was... intense..."
            play sound knock3
            show dr 102
            sir "*Knocking on the door* Hey there, guys!" with dis
            sir "The challenge is over!"
            play sound penetration2
            show dr 101
            no "F-Fuck!"with dis
            no "The challenge! I almost forgot about it!"
            no "D-Distract him, p-please!"
            mc "W-What? Me?"
            no "Y-Yeah!" with hpunch
            no "I s-still have a dildo inside my p-pussy, in case you didn't notice!"
            stop music3b fadeout 9
            play music2b partypenny
            play music3 partyfar fadein 6
            show dr 104
            bla "You quickly get dressed again and hide your boner as best as you can."with dis15
            mct "Fuck."
            mct "Why the hell couldn't I cum?"
            mct "This fucking blue-balling wine..."
            sir "Nova? [mc]?"
    mc "*Clears throat* Y-Yeah, yeah, we're here."
    stop music3b
    stop music3
    stop music2b
    $ renpy.end_replay()





label ga_luna1:
    play music2 lunadodd fadein 1
    show dm 33 with dis12
    l "*Lying down* O-Okay." with dis
    l "If you really don't mind... I won't say no. You’ve convinced me!"
    show dm 34
    mc "Sweet! No one can refuse one of my rubdowns!"
    show dm 33
    l "Well, I don't know many people who would refuse a free massage."
    l "Unless the person offering it had some sort of ulterior motive."
    show dm 34
    mc "*Chuckles* There's no hidden agenda, I promise."
    mc "I can use some sunscreen oil too, if you want."
    show dm 33
    l "Yeah, sure. I could use some of it on my lower back."
    l "There's a bottle under the table."
    show dm 34
    mc "Excellent then!"
    mc "Thank you for signing up for our premier massage package here at [lastname] Massage Parlor."
    mc "Are you ready, ma'am?"
    play sound clothes4
    show dm 35
    l "*Giggles* Sure." with dis14
    mct "Sweet Lord have mercy..."
    mct "This view is almost too much..."
    mc "*Taking a deep breath* (But luckily, you're not an animal, [mc]. Inhale and exhale, now...)"
    mct "Though, if Luna wanted me to be an animal..."
    l "[mc]?"
    show dm 36
    mc "*Clears throat* Y-Yeah!" with dis14
    mc "I was saying..."
    mc "Ah, yeah! Please, relax and prepare to enjoy the experience, ma'am."
    l "*Giggles* Mm-hm."
    show dm 37 with dis2
    pause .1
    bla "You gently put your hands on Luna's lower back." with dis12
    bla "Her skin immediately tenses, and her breathing begins to pick up."
    show dm 38
    mc "Is everything okay?" with dis
    show dm 39
    l "Y-Yes."
    l "It's just that... your hands are cold."
    show dm 38
    mc "Oops, my bad."
    mc "On the other hand, your skin feels really warm after being exposed to the sun for such a long time."
    mc "Sorry about that!"
    show dm 39
    l "No problem..."
    scene lunaf1 with dis2
    bla "You start massaging Luna's lower back at a steady pace, squeezing your fingers in a firm but tender manner." with dis12
    mc "Your lower back muscles are really tense, Luna."
    mc "You're full of knots."
    l "Am I?"
    mc "Yeah, totally."
    l "And what's the solution?"
    mc "Well, my years of massaging experience have prepared me for this. It'll have to be a lengthy treatment."
    mc "You'll need lots of relaxing, periodic caresses from a trustworthy masseur."
    l "*Giggles* That would be you?"
    mc "You happen to be in luck, ma'am."
    l "*Giggles* I think that’s a treatment plan I can follow..."
    bla "Little by little, Luna's muscles begin to relax, as the temperatures of your hands and her body even out."
    mc "Starting to feel better?"
    scene dm 39
    l "Yeah..." with dis12
    l "It feels... {w}great."
    mc "I'm glad."
    scene lunaf1 with dis14
    mc "Do you like to sunbathe when you have the opportunity?"with dis06
    l "I do..."
    l "But my skin is so pale that, even if I manage not to get sunburned, I end up with ridiculous tan lines."
    l "So I usually avoid it."
    mc "I see."
    mc "You can remove the top of your bikini, if you want."
    scene dm 39
    l "Hmm? What...?"with dis12
    mc "Uh, I mean..."
    mct "Did that sound too forward?"
    mc "You know, if you don't want tan lines. I-I’ve heard that’s what Penny does to avoid tan lines for modeling shoots!"
    mc "I know that most women try to avoid them."
    l "Oh..."
    l "Sure... good idea. I’ll have to thank Penny next time I see her."
    play sound clothes4
    play sound2 clothes3
    show dm 40
    bla "Luna takes off her bikini top and drops it next to the table." with dis15
    l ". . ."
    mct "Damn, I didn’t think that’d work. But I'm glad it did..."
    play sound clothes2
    scene lunaf2 with dis2
    mc "Oof, your legs are super tense too." with dis
    mc "You’re lucky that I got here in time!"
    l "*Giggles* I'll have to recommend your services to everyone I know."
    l "You're very caring."
    mc "Well, it’s the duty of a good masseuse to leave every one of their customers satisfied!"
    mc "Here at the [lastname] Massage Parlor, customer satisfaction is priority numero uno!"
    l "*Giggles* That's a good policy."
    mct "She's totally relaxed now."
    mct "It feels like she trusts me completely."
    mct "And for some reason that makes me feel special."
    mct "I just want to make her feel... safe."
    mct "Is that normal?"
    mct "I mean, fuck, I'm massaging a half naked girl with a 10/10 body and I can only think of how nice it is that she's feeling comfortable around me."
    mct "Although..."
    mct "Well, now that I’m thinking about it..."
    mct "Jesus, Luna's body is breathtaking."
    mct "The way she's arching her back makes her curvy butt stand out even more."
    mct "I wonder if she's doing that on purpose..."
    pause
    mc "All good, Luna?"with dissolve
    mc "You're so quiet all of a sudden."
    mc "Please tell me you didn't fall asleep. That would be devastating for my customer reviews."
    scene dm 41
    l "No... I didn't." with dis12
    l "I'm feeling better than I thought I’d be."
    l "It's just that... I love the feeling of your hands. You weren’t exaggerating about your expertise."
    l "It's like a... p-pampering sensation."
    mc "Happy to hear that..."
    scene lunaf2 with dis17
    mc "If you want to change your position or you want me to change anything, just let me know." with dis08
    mc "The most important thing is that you are comfortable."
    scene dm 41
    l "I'm doing terrific..."with dis
    l "Just..."
    l "Do you mind if I turn around?"
    mc "*Gulps* Not at all."
    mct "Oh boy..."
    mct "Is she going to put her top back on, or...?"
    play sound clothes3
    play sound2 clothes4
    show dm 45 with dis14
    l "*Turning around* Thank you." with dissolve
    show dm 46
    mct "Doesn't seem to be the case..."with dissolve
    show dm 45
    l "T-This is a little embarrassing, though."with dissolve
    show dm 46
    mc "Nonsense!"with dissolve
    mc "You have nothing to worry about, our employees are strictly professional."
    mc "Their gaze never drifts to where it doesn't belong."
    mc "Just relax and continue enjoying your massage, ma'am."
    l "*Giggles* Mm-hm..."
    scene lunaf3 with dis22
    mct "My god, Luna's skin feels softer than silk." with dis
    mct "She barely has any body hair, and it almost looks like porcelain."
    l ". . ."
    mct "She’s completely changed since the beginning of the massage."
    mct "It almost feels like she’s asking me to touch it... to caress it..."
    mct "I know she's not used to touching other people with her bare hands, but she's probably not used to any other kind of physical contact either."
    mct "Maybe that's what makes it so special."
    pause
    bla "The birdsong above is only interrupted by the noise of your hands rubbing up against Luna's body and the soothing sound of her soft sighs and small moans." with dis08
    mct "Man, this is getting hotter and hotter every second, and we're not even saying anything."
    mct "I wonder what she's thinking right now."
    mct "She looks so... receptive."
    mct "Would it be crazy to try to make things a little more intimate...?"
    l ". . ."
    mc "Does it feel good, Luna?"
    l "Mm-hm..."
    mc "If you want me to change the position of my hands, you just have to say so."
    show dm 47
    l "Your hands...?"with dis15
    mc "Yeah, I mean..."
    mc "I wouldn't want to cross any line that could make you uncomfortable."
    l "Oh..."
    l "Don't worry..."
    l "I feel safe in your hands. I feel... good."
    mc "Alright..."
    show dm 48
    bla "You move your hand along Luna's thigh." with dis14
    mct "Alright... she didn't flinch."
    mct "So far so good..."
    show dm 49
    bla "Luna lets out a slight moan." with dis15
    mc "Are you okay? I can sto–"
    show dm 51
    l "N-No. Don't. Don’t stop."
    l "It feels good."
    l "I-I want you to touch me."
    show dm 50
    mc "Touch you?"
    show dm 51
    l "Yes. I want to... feel your hands all over my... body."
    show dm 50
    mct "Oh god."with dis06
    mct "Did she really say that?!"
    mc "Alright, ma'am..."
    mc "Here at [lastname] Parlor... the customer's always right."
    mc "Your wish... is my command..."
    scene lunaf4 with dis22
    bla "You start rubbing the palm of your hand against Luna's pussy as delicately as possible." with dis08
    l "*Slightly moaning* Aahh..."
    mct "Jesus..."
    mct "I can feel Luna's fleshy pussy through the fabric."
    mct "She's wetter now than when she was in the pool."
    l "Aaaahh..."
    pause
    mc "*Looking at Luna's chest* (Damn, Luna's tits sure are bigger than they seem at first glance)."with dis06
    mct "She can barely cover them with her arm."
    mct "Come on... let me see those pink nipples..."
    mct "Please..."
    bla "Luna's fidgeting accelerates, and her breath hastens."
    scene dm 52
    l "Ahh... ahh... ahhh..."with dis15
    play sound clothes4
    play sound2 chair4
    show dm 53
    l "*Moaning* Oh my god..." with dis15
    mct "OH YES!"
    scene lunaf5 with dis2
    l "*Moaning* O-Oh g-god..." with dissolve
    bla "Carried away by the situation, Luna’s arm drops to her side, completely freeing her breasts. Her legs twitch nervously."
    mct "That's what I'm talking about..."
    bla "Her shyness almost completely forgotten, Luna’s body begins to roll on the massage table."
    l "*Moaning* Ahh... aah... ah...."
    mct "My god, look at those perfectly round boobs... I need to stop myself from bending down and just going to town on her... I’m still not sure how she’d react."
    mct "I have to imagine we’re close to her limits, considering her lack of physical contact."
    mct "I just want to take her and make her mine..."
    mct "But... you've gotta wait, [mc]... Now’s not the proper time for it."
    pause
    l "*Moaning* Agh... aah..." with dis08
    mct "Luna's whimpers of pleasure are intoxicating."
    mct "I never thought I’d live to hear them..."
    scene lunaf6 with dis2
    l "*Panting* AAahh... ahh... aah..." with dis
    mc "You're perfect, Luna..."
    mct "Fuck, my pants are about to explode. Getting into some jeans was a bad fucking idea."
    l "*Moaning* Ahh...!"
    mct "Her back is tense and stiff, but instead of moving away, she's bringing her hips towards me."
    mct "I like that..."
    mct "Judging by her reactions to my caresses, I bet that any kind of physical touch feels way more intense to Luna."
    mct "As if her whole body had sensitivity cranked to max."
    mct "How I'd like to drive her crazy with pleasure..."
    l "Ahh... {w}ahhhh...."
    play sound clothes4
    play sound2 chair4
    show dm 54
    l "*Sitting up* Aaagh...!" with dis12
    l "Oh g-god..."
    show dm 55
    mc "Is everything okay?" with dis12
    l "*Blowing out air* No..."
    l "I mean... y-yes."
    show dm 56
    mc "We can stop here, if you want." with dissolve
    show dm 57
    l "No..." with dis
    l "I..."
    show dm 58
    bla "Luna puts her hand on your chest one more time. You can see a shiver running through her body as she sighs deliriously." with dis12
    l "I-I can feel your heart beating."
    l "It's pounding..."
    show dm 59
    l "I..." with dis14
    l "I want you to keep massaging me."
    l "B-But... I want to feel you {i}somewhere else..."
    show dm 60
    mc "Somewhere else?"with dissolve
    mc "Do you mean... that you want me to touch you directly?"
    show dm 59
    l "Y-Yes."with dissolve
    show dm 60
    mct "Oh my god... Did Luna Hernandez really just ask me what I think she asked me?"with dissolve
    show dm 61
    mc "My Luna..." with dis12
    show dm 62
    bla "You move the thin piece of clothing to the side, revealing Luna's smooth, pink pussy." with dis15
    show dm 63
    bla "You cautiously insert one finger inside her." with dis15
    l "AAaahhh..."
    show dm 64
    l "OH M-MY GOD."with dis
    l "Y-You're inside."
    mc "I am..."
    l "*Hyperventilating* Ahh..."
    scene lunaf7 with dis22
    bla "You insert both fingers inside Luna's vagina and start massaging her insides with a steady rhythm." with dis08
    l "*Panting* Oh g-god..."
    l "Aaaahh... ahhhh... aaah..."
    mct "Jesus... like I expected, Luna feels incredibly tight."
    mct "However, her pussy’s so soaked... my fingers are sliding in, like her whole body was begging me for them."
    l "*Panting* Ahhh..."
    l "*Panting* T-This is... {w}incredible..."
    bla "As you begin to increase your pace further, Luna's whole body twists and twitches. A high-pitched moan escapes her mouth."
    mct "Thank god the sounds of the mountain cover up her sounds."
    l "*Panting* AAahh... aahh..."
    pause
    mct "God, it drives me insane when she looks me in the eyes."with dis
    mct "I wonder how Luna’s sensitivity to physical touch would affect her during sex..."
    mct "Would it be counterproductive?"
    mct "Or on the contrary... would she become insatiable?"
    l "*Moaning* AHHH... "
    l "*Moaning* [mc]..."
    l "*Panting* AHHH!"
    l "*Panting* W-What is going on... "
    mct "Is she gonna come?"
    l "*Panting* AAAahhh... I can't..."
    l "*Panting* I h-h-have to..."
    play sound cum2
    play sound2 cum2
    play sound3 chair3
    play sound4 clothes4
    scene dm 66
    l "AAAAAaaaaaAaahhh...." with hpunchlong3
    if anniepath:
        mct "You did it again, [mc]..."
    play sound5 clothes3 volume 1.5
    show dm 67 with dis15
    l "*Recovering her breath* Ahhh... ahghh... ahh... ahhh..."with dis
    mc "My god, your body is unbelievably perfect, Luna..."
    l "*Recovering her breath* Ahhh... ahh... ahhh..."
    l "*Recovering her breath* {b}F-FUCK..."
    mc "Um... excuse me?!"
    mc "Did you just say the “F” word?!"
    l "*Recovering her breath* W-What...?"
    mc "*Chuckles* Nothing..."
    mct "It's the first time I heard her swear in the time I’ve known her."
    mct "That was hot..."
    l "*Recovering her breath* My god... t-that was... the most intense thing I've ever felt..."
    mc "That's good to hear..."
    show dm 68 with dis15
    pause
    show dm 69
    bla "Luna's hand starts to move along your torso towards your jeans." with dis14
    mct "Hmm...?"
    show dm 70
    mct "Is she trying to sense my body as before? Or is she..."with dis15
    show dm 67
    mct "Oh my god, is this really happening?!" with dis12
    mct "Is she going to..."
    play soundlow carhorn
    stop music2
    play music birds volume 1.5
    show dm 71
    her "[mc]! Where are you?" with hpunch
    stop musicb
    $ renpy.end_replay()


label ga_alex1:
    stop music fadeout 1
    stop musicb fadeout 1
    stop music2 fadeout 1
    stop music2b fadeout 1
    play music3 sexyalex fadein 1
    show ccc 29 with dis
    mc "Now... where's my prize?"with dis
    show ccc 28
    x "Oh, I know what you want, and... you wouldn't be able to handle it, pretty boy."
    show ccc 29
    mc "I'm pretty sure I would..."
    mc "I know you better than you think. I definitely could handle you."
    mc "I know that under that tough girl facade of yours, you're as sweet as a cupcake. You can't deceive me."
    show ccc 28
    x "*Chuckles* I'm too much woman for you, [mc]."
    show ccc 29
    mc "I could totally prove you wrong, Alex..."
    play sound clothes3
    show ccc 30 with dis15
    x "*Removing her gloves* Oh, could you? And how would you do that, exactly?" with dis08
    show ccc 30b
    mc "Give me 20 minutes and I'll show you."with Dissolve(.4)
    show ccc 30
    x "How about 20 seconds?"with Dissolve(.4)
    show ccc 30b
    mc "Oh, are we negotiating now?"with Dissolve(.4)
    show ccc 31
    x "We're not. That's my..." with dis17
    play sound zippo
    stop music3 fadeout 5
    play music night fadein 4
    pause .2
    show ccc 32 with dis15
    play sound2 zippo
    mc "What's that noise? Is someone coming?" with dis08
    show ccc 33 with dis15
    mct "Goddammit, nice timing..."with dis08
    mct "They're gonna kill the mood, whoever they are."
    show ccc 34
    mc "Hmm?" with dis08
    show ccc 35
    play sound zippo
    will "*Lights a cigarette*"
    play sound2 smoke
    show ccc 36
    will "*Exhales*" with dis17
    show ccc 38
    mc "Oh man, you have to be kidding me..." with dis15
    show ccc 37
    x "Who is it?"
    show ccc 38
    mc "It's... y-your father."
    show ccc 37
    x "My father? What’s he doing?"
    show ccc 38
    mc "He's smoking. He's... just standing there, menacingly. If looks could kill, I’d be super worried."
    show ccc 37
    x "Hmm, yeah, sounds like him."
    show ccc 38
    mc "Wait, someone else is coming..."
    play soundlow leaves2 volume 0.3
    show ccc 39 with dis15
    mc "Oh shit, it's your brother..." with dis08
    x "It's so nice to see the Bardot family reunited."
    ax "Dad, I swear to god, it was him!" with hpunch
    will "Go back to the party, Axel."
    ax "Maybe he's in witness protection! Or maybe..."
    will "I told you to drop that line of thinking. I will not repeat myself."
    ax "B-But you have to listen to me!"
    ax "It makes no sense that–"
    play sound leaves
    play sound2 leaves
    play sound3 leaves
    play sound4 punch
    show ccc 40
    will "ENOUGH!" with hpunch
    will "I'M GETTING SICK OF YOUR IDIOCY!" with hpunch
    will "You have to start taking things seriously! I will not have you sullying the Bardot name, like your sister!"with hpunch
    ax "I-I'm sorry, Dad..."
    will "Now get back to the fucking mansion and do what you were told!"
    will "ARE WE CLEAR?" with hpunch
    ax "Y-Yes! I'm s-sorry..."
    play sound smoke
    show ccc 36
    will "I’m surrounded by idiots fucking everywhere." with dis17
    show ccc 38 with dis15
    mc "Seems like they had a fight and Axel ran away." with dis08
    show ccc 37
    x "What were they talking about?"
    show ccc 38
    mc "I'm not sure, I didn't quite catch it. They're too far."
    play soundlow leaves2
    show ccc 41
    mc "O-Okay, I think Axel went back to the mansion, but William is still there." with dis12
    mc "But... f-fuck, I left my mask at the entrance of the maze. We can't let them see us."
    mc "W-We'll wait here until he goes back to the mansion."
    show ccc 42
    x "*Giggles* You sound a little shaky, [mc]." with dis08
    x "Are you afraid of my daddy?"
    show ccc 43
    mc "W-What? I'm not!"with dissolve
    show ccc 42
    x "Are you shaking because of Axel, then? Is he the one making you so nervous?"with dissolve
    x "You can admit it, don't worry. I won't laugh."
    show ccc 43
    mc "Of course not! Not now, not ever..."with dissolve
    show ccc 44
    x "Then... Why are you so nervous, [mc]?" with dis15
    mc "What are you doing?!"
    stop music fadeout 18
    play music3 sexyalex fadein 6
    x "Maybe it's... because of me?"
    mc "W-What? No!"
    show ccc 45
    x "No? I don't make you nervous? Not one tiny... little... bit...?" with dis12
    mc "Not one bit..."
    play sound clothes3
    show ccc 46
    x "And what if I do this?" with Dissolve(1.4)
    x "Still nothing...?"
    mc "Nothing..."
    play sound2 clothes3
    show ccc 47
    x "And now...?"with Dissolve(1.4)
    mct "Oh god..."
    mct "This feels so dangerous, yet so exciting..."
    mc "I've never been less nervous..."
    play sound3 clothes3
    show ccc 48
    x "I guess I've lost my touch. I'm used to getting people on edge..."with Dissolve(1.4)
    mc "You'll have to try harder with me..."
    show ccc 49
    x "Well, I do like challenges... and like I told you, I never lose..." with dis12
    mc "We’ll see about that..."
    play sound belt volume 2
    x "*Removing your belt* Now tell me...."
    x "What if I..."
    show ccc 50
    x "(Hmm?)" with dis
    show ccc 51
    x "(Holy shit, his cock is huge as fuck!)" with dis12
    x "(This is... certainly not what I was expecting.)"
    x "(I was joking about salami the other day, and this whole time he was packing this...)"
    mc "You okay, Alex? You're so quiet all of a sudden..."
    mc "Are {i}you{/i} nervous about something...?"
    show ccc 52
    x "O-Of course not... It's just that..."with dissolve
    x "I-I'm surprised you got hard so fast. That's all. Couldn’t help yourself, eh?"
    show ccc 53
    x "But I guess it's a natural reaction when you're nervous..." with dissolve
    mc "You’re not letting up on that, huh?"
    mc "I'm sorry to burst your bubble, but I feel very relaxed next to you. No nervousness whatsoever."
    show ccc 54
    blank "{i}Alex grabs your penis softly, but firmly." with dis15
    x "This doesn't look relaxed to me."
    mc "{size=28}O-Oh, god..."
    show ccc 55
    x "I'm sorry? Did you say anything?" with dis12
    mc "N-Nothing."
    show ccc 54
    mc "Y-your hands are just... cold." with dis12
    x "*Chuckles* Yeah, I bet..."
    show boyle1 with dis2
    mc "Oh, f-fuck..." with dissolve
    mc "O-O-Oh god..."
    x "Shhhh..."
    x "Keep your voice down..."
    x "You wouldn’t want my daddy to hear us, would you...?"
    mc "O-Okay, I'll admit it... you're making me a bit nervous now, A-Alex..."
    mc "T-This was fun, b-but we’ve gotta hide..."
    mc "What if your father finishes his cigar and comes this way...?!"
    x "You’re scared of him seeing us do this?"
    x "If he saw you, with your pants down, getting your huge, thick cock rubbed by his little girl... After what you said to him the other day in my house?"
    x "He'd definitely kill you..."
    x "Seriously, he would. No joke. He'd send someone to kill you in the real world."
    x "Not because he cares about me, but because this is the ultimate way of “sullying the Bardot name”, you know?"
    x "The daughter of one of the richest, most powerful men on the planet, is currently giving you a handjob, less than 20 feet away from her dad."
    mc "AAahh..."
    mc "I d-don't want him to kill me..."
    x "*Giggles* Isn't it thrilling? The risk of getting caught? My boobs pressed against your back... my hands holding onto your manhood, giving you these long... slow... strokes..."
    mc "I-It's... a c-confusing mixture of emotions..."
    x "Well... I’ll tell you what... if you finish before he puts out his cigar, I'll let you hide..."
    mc "What? I-I can't finish before he does..."
    x "Oh, is that another challenge...?"
    mc "Aahh... w-what?"
    play soundlow leaves2
    scene ccc 56
    blank "{i}Alex stops and walks in front of you." with dis15
    show ccc 57
    x "I see what you're trying to do..."
    x "This has now become personal."
    show ccc 56
    mc "What? I'm not trying to do any–"
    play sound clothes3
    show ccc 59 with dis15
    mc "Holy shit..." with dissolve
    mc "Those perky nipples... I’ve thought about them ever since we visited Ogygia..."
    play soundlow leaves2
    show ccc 60
    blank "{i}She kneels down before you and grabs your dick once again." with dis12
    mc "Oh god..."
    show ccc 61
    x "Do my hands still feel cold?"
    show ccc 60
    mc "Not anymore..."
    show ccc 61
    x "Good..."
    $ renpy.music.set_volume(0.2, delay=10.0, channel='music3')
    play music wetting3 fadein 6
    show boyle2 with dis22
    mc "O-Oh Jesus!" with dissolve
    mc "F-Fuck..."
    mct "God, I can't believe Alexandra Bardot is giving me a handjob..."
    mc "Ahhh..."
    mc "This is a t-terrible idea, Alex..."
    mc "But... fuck, I love seeing your tits bouncing like that..."
    mc "You’re driving me insane..."
    mc "I'm not gonna last much longer at this rate..."
    x "That's the idea."
    mc "You're enjoying this too, right, you pervert?"
    mc "Your hard nipples give you away..."
    x "I'm enjoying the thrill of the risk. We could be caught at any moment."
    x "Check your ego..."
    pause
    show boyle3 with dis22
    blank "{i}Alex starts massaging your balls and increases the speed of her shakes even further." with dissolve
    mc "G-God..."
    x "Do you like this...? Calling ME a pervert, when you’re such a dirty boy, [mc]..."
    mc "Y-Yeah..."
    mc "Ahhh..."
    mc "This is definitely not how an upper-class lady should behave, Alex..."
    x "Yeah..."
    x "It definitely isn't..."
    x "But who gives a fuck? I've never been part of this world anyway... right?"
    x "Fuck them all..."
    mc "Y-Yeah, fuck them all..."
    mc "AAahh, yeah..."
    x "Are you gonna cum...?"
    mc "Not yet..."
    x "Are you close?"
    mc "I'm not sure..."
    stop music fadeout 1
    scene ccc 61
    x "You're gonna make me sweat, aren't you? You’re gonna make me work that load out?" with dis
    show ccc 60
    mc "I know you can try harder..."
    show ccc 61
    x "*Chuckles* Fuck you."
    x "Very well, then..."
    show ccc 62 with dis15
    x "Let's try a bit harder..." with dis08
    mc "Oh fuck yes, that's it..."
    x "Will my tight, little mouth be enough?"
    mc "We'll see..."
    mc "Let me feel it..."
    show ccc 63
    blank "{i}She puts your dick inside her mouth and starts caressing your glans with her tongue." with dis12
    mc "Oh... F-FUCK!"
    show ccc 62
    x "Keep your voice down, you idiot..."with dis15
    mc "S-Sorry..."
    show ccc 63
    mc "I... aahhh... I forgot..."with dis12
    play music blowjob2 fadein 3
    show boyle4 with dis22
    mc "Oh my f-fucking god..."with dis08
    mc "Ahhh... yeah... that's the spot, Alex..."
    mc "Don't stop..."
    stop music fadeout 2
    scene ccc 64 with Dissolve(1.75)
    play soundlow putoutcigar
    will "*Putting out his cigarette*"with dis
    mc "Aaahh...!"
    will ". . ."
    show ccc 65
    will ". . ." with dis15
    blank ". . . . . ."
    will ". . ."
    show ccc 66
    will "*Leaving* This company needs a fucking purge." with dis15
    play music blowjob2 fadein 3
    show boyle4 with dis22
    x "Mmmmm...."with dissolve
    mc "Oh g-god..."
    mc "Your mouth feels amazing..."
    mc "Do you like the taste of my cock, Alex?"
    x "Mmmffhhh..."
    mc "I'll take that as a yes..."
    x "Mmm-hmmmm..."
    mc "You look so good taking that cock in your mouth..."
    mct "I’d love to feel how my dick stretches her lips..."
    x "*Gagging* Mmmmh..."
    mct "Fuck yes, she's drooling all over me..."
    mc "Oh yeah..."
    mct "I wish I could push it further..."
    show boyle5 with dis22
    blank "{i}As if she had heard your thoughts, Alex suddenly increases her pace, taking your cock deeper into her throat." with dissolve
    mc "Ohhh... F-FUCK!!"
    x "*Gagging* Mmmmm... mmmmhhh... mmmmmfffhhh..."
    mc "Oh baby..."
    mc "Oh my god..."
    mc "J-Just like that...!"
    x "*Gagging* MMmmhh..."
    mc "Aaahhh..."
    mc "Your mouth feels so tight..."
    x "Mmmm..."
    mct "She's completely obsessed..."
    mc "I'm gonna cum so much, Alex..."
    mc "You’re doing such a good job, I can feel it coming..."
    menu:
        with dis
        "Cum in her mouth":
            $ boylemouth = True
        "Cum on her face":
            $ boylemouth = False
    mc "Aaahhh... I'm almost..."with dissolve
    mc "I'm..."
    stop music fadeout 1
    if boylemouth:
        scene ccc 67b with dis
    else:
        scene ccc 69b with dis
    play sound cum2 volume 1.5
    play sound2 cum1
    play sound3 cum3
    if boylemouth:
        show ccc 67
        blank "{i}You grab Alex's head and unload your seed deep inside her throat." with hpunch
    else:
        show ccc 69
        blank "{i}You push Alex away at the last second and you unload your seed all over her." with hpunch
    play sound cum2 volume 1.5
    play sound2 cum1
    play sound3 cum3
    mc "AAaaaaaarghh..." with hpunch
    if boylemouth:
        show ccc 68 with dis15
    else:
        show ccc 70 with dis15
    mc "Oh my god..." with dis08
    mc "Holy shit, that was a lot..."
    x "Hmph."
    stop music3 fadeout 8
    play musicb night fadein 10
    play soundlow leaves2
    if boylemouth:
        show ccc 73
        x "*Standing up* You could have warned me or something, you fucking idiot." with dis17
    else:
        show ccc 71
        x "*Standing up* God, what a fucking mess."with dis17
        mc "Y-Yeah, sorry about that."
        show ccc 72
        x "*Wiping her face* You could have warned me or something, you fucking idiot."with dis12
    mc "I did! But you were too engrossed in your task..."
    show ccc 73b
    x "That's not true! You didn't say shit!" with dis12
    x "And I w-wasn't engrossed in anything."
    show ccc 74
    x "But anyway, what matters is that I won! You came before my father finished his cigar!" with dis12
    mc "I... think he left a while ago."
    show ccc 75
    x "WHAT?!" with dissolve
    show ccc 75b
    x "Goddammit!"
    stop musicb
    $ renpy.end_replay()




label ga_annie2:
    stop music fadeout 1
    stop musicb fadeout 1
    stop music2 fadeout 1
    play music2b sexy4 fadein 1
    stop music3 fadeout 1
    show cx 9 with dis
    pause
    play sound3 clothes
    show cx 10
    blank "{i}She removes her bodysuit and lets it slide down her body to the floor." with dis2
    show cx 11 with dis15
    mct "Wow..." with dissolve
    mct "I know I already saw her naked that night in my room, but... well, there was barely any source of light then. Man, she's... stunning."
    mc "You're so pretty, Annie..."
    a "Mm-hm..."
    mct "God, she's shaking like a leaf. She’s so precious."
    mct "She's not even looking me in the eye... I don't think I've seen her so nervous before. And considering it’s Annie, that's saying something."
    mct "What could I do to calm her down...?"
    mc "Annie?"
    a "Hmm?"
    play sound clothes2
    play sound2 fall2
    play soundlow dodge
    show cx 12
    mc "*You pick her up like she weighs nothing* Hop!" with hpunch
    a "AAAAH!" with hpunch
    a "[mc]! What are you doing?!" with hpunch
    a "I'M NAKED!!"with hpunch
    mc "Oh, believe me, I know..."
    mc "I thought that was the idea!"
    show cx 14
    a "W-Well y-yeah, I know!" with dis
    a "B-B-But..."
    a "I mean..."
    a "G-God, this is so embarrassing...!"
    show cx 13
    mc "Seeing you undressing just for me was hot as fuck, Annie."
    show cx 14
    a "W-Was it?"
    show cx 13
    mc "But you looked way too nervous, so I wanted to calm you down a little."
    show cx 14
    a "Calm me down?! Y-You grabbed me while I was naked!"
    a "Like... totally naked! You're touching my... b-butt!"
    a "How is that supposed to calm me down?!"
    show cx 13
    mc "Would it help if I got naked too?"
    show cx 14
    a "N-No! That'd make things worse!"with hpunch
    show cx 13
    mc "*Chuckles* Can I tell you something?"
    show cx 14
    a "I... Y-Yes..."
    show cx 13
    mc "But I need you to relax first."
    show cx 14
    a "I'm relaxed! I'm super relaxed!"
    show cx 13
    mc "No, you're not!"
    mc "Let's do something. I want you to look me in the eyes."
    show cx 14
    a "Y-Your eyes?"
    show cx 13
    mc "Mm-hm..."
    show cx 15
    blank "{i}Her eyes make contact with yours. You start to feel her limbs loosening their grip around you." with dis12
    mc "I know you're nervous. It's totally normal to be. And you tend to be a jittery girl anyway, so a little nervousness makes sense here."
    mc "But... Do you think I'm NOT nervous? I'm super scared too! I mean, in my arms, I'm holding an adorably precious, absolutely gorgeous girl whom I’ve liked for years."
    mc "We just went on a date on a spaceship hurtling between constellations in the sky! I'm surprised I'm not weak in the knees yet."
    mc "I know it's scary to get out of your comfort zone, but... I think we can overcome it together."
    mc "So let's stop fooling around and cut to the chase: I like you, and you like me."
    mc "I want to be with you... in {i}that{/i} way."
    a ". . ."
    mc "That’s how I feel. If you don't feel the same way... we can always go back to where we were a month ago and stay friends!"
    mc "It’ll be a little awkward at first, but our friendship is strong, and I know we’d be back to normal in no time."
    mc "Is that what you want?"
    show anniesmh2
    a "*Shakes her head*"
    mc "I know it's scary to cross this bridge when you're not sure what your partner might want, so let me be clear..."
    mc "I love how open your heart is to others, how sweet and kind you are to people you’ve just met. I love your adorable blushes, your kind laughs, and... your petite body and curvy ass."
    mc "You are so ridiculously pretty, Annie, that I can’t help but want to take our relationship to the next level."
    mc "I want to be with you."
    a ". . ."
    mc "Is... is that what you want too?"
    show annienod2
    a "*Nods her head*"
    mc "*Sighs with relief* I feel so much better now that we're finally speaking clearly, don't you?"
    scene annienod2
    a "*Nods her head*"
    mc "Alright so... can I ask you another question?"
    scene annienod2
    a "*Nods her head*"
    mc "Can I kiss you?"
    scene cx 18
    a "*Smiles*" with dis08
    scene annienod3
    a "*Nods her head*"
    show cx 20
    blank "{i}She kisses you with a sincere, unrestrained passion. Her legs wrap around you."with dis
    mct "Her lips are trembling... but her body isn’t shaking anymore."
    show cx 21
    mc "Well, after getting all that off my chest, I feel so much better." with dis
    mc "*Caressing her cheek* I feel like I could never get enough of you, Annie..."
    play soundlow clothes3
    show cx 22b
    a "I feel the same way..." with dis12
    show cx 22
    mc "Must be this place... We have to leave a generous tip when we leave."
    show cx 22b
    a "*Giggles* Definitely!"
    a "I guess we should leave the room before they need it for someone else..."
    show cx 22
    mc "Hmm... I'm pretty sure they wouldn’t mind if we stayed for an extra 20 minutes..."
    show cx 22b
    a "20 minutes? How much time do you need to change your clothes?"
    play sound clothes3
    show cx 24
    mc "Well... I was actually thinking of doing something else while we're here..." with dis12
    show cx 25
    a "Oh, really...? What do you have in mind?"
    show cx 24
    mc "Do you remember our night together in my room?"
    show cx 25
    a "Remember? You'll probably laugh at me, but... I've been thinking about it all the time."
    show cx 24
    mc "Is that so? What have you been thinking about, exactly, Ms. Winters?"
    show cx 25
    a "Well..."
    a "You know..."
    a "The sound of the rain against the window..."
    a "The feeling of your skin against mine..."
    a "The heat that you were giving off..."
    a "Your ragged breaths on the back of my neck..."
    show cx 24
    mc "Nothing else?"
    show cx 25
    a "*Giggles* Well..."
    a "And..."
    a "The feeling of your... {i}cock{/i}... between my thighs..."
    show cx 26
    mct "She pronounced \"cock\" as if she was saying a forbidden word. I love how innocent she is..."with dis
    play soundlow clothes3
    show cx 27
    blank "{i}You gently spread her legs to expose her pussy."with dis15
    mct "What a sight..."
    mct "I wonder how many people have seen Annie's most intimate part. She seems like she’d get changed in a corner of the locker room, covered in a towel."
    mct "The fact that she's allowing ME to see and do this with her... it turns me on so much..."
    show cx 28
    mc "Did I hear that right? You've been thinking about my cock?" with dis
    mc "Have I been fooled all these years? Innocent, shy Annie is actually a horny, perverted little girl?"
    show cx 29
    a "*Giggles* Maybe just a bit..."with dis08
    show cx 30
    blank "{i}You start massaging her perky breasts and kissing down her neck."with dis12
    a "Ahh..."
    a "*Moans* Oh god..."
    mct "She's not shaking anymore, but her breaths have quickened."
    mct "God, there are so many things I want to do to Annie right now... but it's still Annie. I don't wanna cross any line too fast."
    show cx 27
    mc "You're making me so horny, Annie..." with dis12
    a "You too..."
    show cx 30b
    mc "Let me take care of you tonight..." with dis12
    play soundlow chair3
    show cx 31
    a "*Gasps*" with dis08
    mc "Is everything okay?"
    a "Y-Yeah. It's just that... I wasn't expecting..."
    mc "Oh... I'm sorry, I should have warned you."
    a "N-No! It's okay!"
    a "It's what I want..."
    a "Please, c-continue..."
    show astro1 with dis2
    a "Aaahhh..." with dis08
    mc "If you want me to stop, just let me know..."
    a "*Soft moan* N-No..."
    a "It feels good..."
    mct "Her skin’s so warm and soft... She’s so delicate..."
    mct "And I can feel her starting to get wet..."
    a "Mmm..."
    show astro2 with dis17
    blank "{i}You start increasing the speed of your caresses."with dis08
    a "*Moans* Aaahhh..."
    a "Oh god..."
    mc "Better?"
    a "*Moans* Y-Yeah..."
    mct "Now we're talking..."
    mct "She's starting to let herself go... moving her hips to the rhythm of my fingers..."
    mct "And her lips are now soaked in her own juice..."
    mc "Can you feel yourself getting wetter?"
    a "Y-Yeah..."
    a "It feels g-great..."
    mc "It'll only get better from here, baby..."
    mc "I just want to make you feel good..."
    a "Aahhhh... [mc]..."
    pause
    a "*Moaning* Aaahh..."with dissolve
    mc "All good?"
    scene cx 34
    a "Y-Yes..." with Dissolve(1.3)
    show cx 33
    mc "I'm gonna put my fingers inside you now... alright?"
    show cx 34
    a "A-Alright..."
    show cx 35
    a "Do it..."with dis12
    play soundlow blow1
    show cx 36
    blank "{i}You slide two fingers inside her."with dis15
    show cx 37
    a "O-O-Ohhh m-my g-god...!"with dis08
    show cx 36
    a "*Her hips spasm* Y-You put t-them inside me..."with dis08
    mc "Yes I did..."
    show cx 37
    a "Ahhh..." with dis08
    show cx 36
    mc "Do they feel good?"with dis08
    show cx 38
    a "Yes, they do..." with dis12
    mc "Do you want me to move them?"
    a "Y-Yes... p-please!"
    $ renpy.music.set_volume(0.2, delay=6.0, channel='music2b')
    $ renpy.music.set_volume(0.6, channel='music3')
    play music3 wetting1 fadein 5
    show astro3 with dis2
    a "O-Ohhh..." with dissolve
    a "My... GOD!!"
    a "This is... aaaAAah...!"
    mct "Annie's pussy feels so tight, even more than I imagined..."
    mct "But she's so wet that her vagina lets me plug my fingers in and out with ease..."
    a "*Panting* Aaaaah... aaahhh!"
    a "Yeah!"
    a "P-Please, keep g-going!"
    a "*Panting* K-Keep going, [mc]! Y-You’re hitting such a... g-good spot!"
    show astro4 with Dissolve(2.2)
    blank "{i}You start kissing Annie, while your fingers stroke her at the same steady pace." with dis08
    a "Mmmm.... mmmm.... mmmmmhh!"
    mct "Her lips always feel so soft... I can feel the soft tickle of her breath, it’s almost synced with her accelerated heartbeat."
    a "*High-pitched moaning* Mmmmmhh...!"
    mct "And her little moans are driving me insane..."
    $ renpy.music.set_volume(0.9, delay=2.5, channel='music3')
    show astro5 with Dissolve(2.3)
    a "*Squeals* AAAAAHHhh!" with dis08
    blank "{i}You curve your fingers inside her, changing their positions, and hasten your pace."
    a "OH M-MY G-GOD..."
    a "W-What is going on...?!"
    a "W-What are you *moans* doooooing to m-me...?"
    a "*Squeals* AAAAHHH!"
    a "Y-You have to stop! S-STOP! [mc]!"
    a "Ahhh... S-Stop! Or I'm g-gonna... {i}p-piss{/i} myself!"
    a "OH JESUS!"
    mc "Don't worry, baby..."
    mc "You're not gonna. That sensation is normal – you're about to orgasm."
    mc "Have you ever had one before? Touching yourself to your naughty thoughts...? Have you ever made yourself cum while jilling off in your room by yourself?"
    a "W-What? Aaahhhh...."
    a "An o-orgasm? I d-don't know..."
    mc "I guess that answers my question..."
    a "*Panting* Oh g-god..."
    a "Oh... {i}F-FUCK!"
    a "Aaaaahhh...."
    a "[mc]... S-Seriously... p-please... I d-don't know w-what..."
    a "AAAaaHHHhh!"with vpunch
    a "[mc]!!!"with vpunch
    play sound cum2
    stop music3 fadeout 1
    scene cx 39 with dis08
    play sound2 cum2
    a "AAAAAAAARGHGHHHH!!" with hpunch
    play sound3 cum2
    a "AAAAAAAAHHHHhhh..." with hpunch
    blank "{i}You can feel Annie's thighs squeeze around your hand, as her whole body tightens. Her hips gyrate back and forth as she orgasms from your ministrations." with dissolve
    play soundlow chair4
    show cx 40
    a "*Collapses* Oh my god..." with dis08
    mc "How was that, little lady?"
    a "T-That..."
    a "That was... indescribable..."
    a "My god... is this how you feel every time you... do this?"
    mc "*Chuckles* More or less..."
    show cx 41 with dis12
    pause
    play soundlow blow1
    show cx 42
    blank "{i}You gently pull your fingers out from Annie's insides, completely covered in her own juices." with dis12
    play sound2 chair4
    show cx 42b with dis12
    a "*Leaning back* WOW!" with dissolve
    a "That was incredible!"
    mc "Glad you liked it..."
    a "\"Like\" it? It was the best experience of my life!"
    mc "Nice..."
    a "(Oh my god! I can't believe it!)"
    a "([mc] made me... {i} cum{/i}!)"
    show cx 42c
    a "*Giggles*" with dis08
    a "Hmm?"
    play sound chair4
    show cx 43
    a "*Gets up* W-What's that?!" with dis12
    mc "What?"
    a "That... BULGE!"
    mc "Oh... well..."
    mc "You turn me on so much, Annie... I'd be lying if I said I wasn’t rock-hard the whole time..."
    a "Wow..."
    play sound2 clothes3
    show cx 44 with dis15
    a "Can I..." with dissolve
    a "Can I see it?"
    mct "Oh fuck yes..."
    mc "Of course you can see it... After all, you’re responsible for it..."
    play sound clothes3
    play soundlow clothes
    show cx 45
    a "*Takes off your tights*"with dis17
    mc "Much better..."
    a ". . ."
    play sound2 chair4
    play soundlow whoosh6
    show cx 46 with hpunch
    pause .4
    a "My... {w}GOD!" with dis08
    a "That thing is huge! You have such a big dick...!"
    mc "Y-You had already seen it!"
    a "B-But... I didn't look much at it! That day I was... too nervous!"
    a "And I only saw it from between my legs! I didn't know it went that far down..."
    mc "Well, you have pretty generous hips, so... even if you could only see the tip poking out..."
    show cx 47
    mc "I mean..."with dis
    a "...I g-guess that makes sense."
    a ". . ."
    a "Can I... {w}can I touch it? {w}Please?"
    mc "I want you to kill me if I ever say no to that question..."
    play sound clothes3
    show cx 48 with dis2
    pause
    show cx 49
    blank "{i}Annie grabs your shaft with tenderness." with dis17
    mc "Oh, yeah..."
    play music3 wetting2 fadein 2
    show astro6 with dis2
    blank "{i}She starts to slowly move her hand along your penis."with dis08
    mc "Ohhh... god..."
    mct "Wow, I wasn't expecting her to take the lead so quickly..."
    mct "I guess she's finally starting to be comfortable with her own sexuality... Or my cock just made her really horny..."
    mc "Oh, Annie..."
    mc "This feels so good..."
    a "You made me feel so good with your fingers... You made me cum and it felt SO good... I just want to make you feel good too..."
    mc "You're definitely succeeding at making me feel good..."
    mc "That's it, baby..."
    mc "Keep stroking it..."
    mc "AAaahhh..."
    mc "You’re such a good girl, Annie..."
    a "Do you want me to go faster?"
    mc "Oh fuck yes, please..."
    $ renpy.music.set_volume(0.9, channel='music3b')
    stop music3 fadeout 2
    play music3b wetting3 fadein 2
    show astro7 with dis2
    mc "Ahhhh..." with dissolve
    a "L-Like this?"
    mc "Y-Yeah, just like that..."
    a "(My god, it REALLY is huge...)"
    a "(I could put like 3 hands here and it still wouldn’t cover it all...)"
    a "It's t-throbbing so hard!"
    mc "Ahh... I know..."
    mct "Annie's hands feel so small and soft... but she's squeezing my cock so fucking hard! It feels amazing..."
    mc "Aaaahhh... keep going, Annie..."
    mc "Aaahh... FASTER!"
    $ renpy.music.set_volume(1.0, delay=2.0, channel='music3')
    stop music3b fadeout 2
    play music3 wetting4 fadein 2
    show astro8 with dis2
    mc "AAAAAHHhhhh..." with dissolve
    mc "Oh, fuck..."
    mct "Man, I can't believe her thin arm isn't tired yet..."
    mc "Oh god, that's it..."
    mc "This is incredible..."
    mc "Aaahh..."
    mc "D-Do you like beating off my cock, Annie?"
    a "I-I do..."
    mc "W-What do you like?"
    mc "Say it... I wanna hear you describe what you’re doing..."
    a "I..."
    a "I love beating off your... massive... pulsing... d-dirty cock..."
    mc "AAAaahh, fuck yes..."
    a "It’s just so big... I don’t want to stop playing with it..."
    a "C-Can we do this more often?"
    a "I-I wanna...{w} practice..."
    mc "Yeah, we can, baby..."
    mct "God... hearing her talk dirty is driving me crazy..."
    mc "*Panting* F-Fuck, I won't last much longer, Annie..."
    mc "You're too g-good at this..."
    a "I want to make you cum, [mc]... You were so good to me..."
    mc "I'm almost there..."
    menu:
        with dis
        "Cum":
            stop music3 fadeout 1
            play sound cum1
            play sound2 cum2
            play sound3 cum3
            scene cx 50
            mc "AAAAAAAARGHH!" with hpunch
            play sound4 cum1
            play sound5 cum2
            play sound6 cum3
            mc "AAAAAaaahhhhhhhh..." with hpunch
            a "W-Wow!"
            a "(Look at all that cum shooting out...)"
            a "(I made that happen?)"
        "Grab Annie and put her on top of you":
            stop music3 fadeout 1
            play sound chair4
            play soundlow chair1
            scene cx 52
            mc "Bring that tight little pussy of yours over here..." with dis08
            show cx 51
            a "Wait..."
            a "W-WHAT?!"with hpunch
            a "I'M NOT READY!"with hpunch
            a "Not yet!"
            a "I'm not ready yet!"
            a "I c-can't take all that! I'm not ready yet! I'm not..."
            a "F-First I have to get myself a-appropriately psyched up f-for..."
            show cx 52
            mc "It's okay, Annie..."
            mc "I won't force you to do anything you don't want to..."
            mc "I just want to feel your pussy lips again..."
            show cx 51
            a "M-My... lips?"
            show cx 53
            mc "Yeah... Like the thighjob in my room, but..."with dis
            show cx 54
            mc "*You softly pull Annie's hips towards you* This time..."with dis15
            show cx 55
            mc "Aahh... you’re in control..." with dis15
            a "Aaahh..."
            show cx 56
            a "Oh god, it's so warm... and sticky..." with dis
            mc "Oh yeah..."
            play music3 wetting5 fadein 2
            show astro9 with dis2
            blank "{i}Annie immediately starts moving her hips back and forth along your cock, her juices spreading all over you." with dissolve
            a "*Moaning* AAAahh..."
            mc "Oh Annie..."
            mc "F-Fuck, I love your body..."
            mc "How petite you are, how easy it is to move you along my cock..."
            mct "God, I'd love to stretch out her tiny pussy..."
            mc "I want you so bad, Annie... I can’t wait ‘til the day you can finally take this dick... But not yet..."
            a "*Moaning* Aaaahh... aaahhh..."
            a "W-We’ve g-gotta do some practicing b-beforehand, [mc]..."
            a "Aaahhh... I-I have t-to get ready for you..."
            mc "*Panting* Oh g-god, I'm gonna cum..."
            mc "Ahh... I w-was at the edge already... But you’re pushing me over..."
            a "T-That sensation... it's coming again... I c-can feel it..."
            mc "Oh baby... just a little bit more..."
            a "AAAAaahh... Y-YEAH!"
            mc "I'm almost..."
            stop music3 fadeout 1
            play sound cum1
            play sound2 cum2
            play sound3 cum3
            scene cx 57
            mc "AAAAAAAARGHH!" with hpunch
            play sound4 cum1
            play sound5 cum2
            play sound6 cum3
            mc "AAAAAaaahhhhhhhh..." with hpunch
            a "W-Wow!"
            a "(Look at all that cum shooting out...)"
            a "(I made that happen?)"
    play sound chair1
    play sound2 chair4
    scene cx 58
    mc "MY GOD!" with dis12
    mc "Jesus fucking Christ... that felt...{w} good..."
    play soundlow chair1
    show cx 59
    a "*Lying down next to you* OH MY GOD!" with dis
    a "This has been... {w}the BEST night of my life!"
    show cx 60
    mc "Better than our first night together, you think?"
    show cx 59
    a "Definitely better..."
    mct "I love feeling her warm body curled up next to me. It feels comfortable... I almost feel... safe."
    a "This is exactly how I imagined everything would be... no, even better!"
    a "Everything's been simply..."
    a "*Sighs* Perfect..."
    show cx 60
    mc "Yeah, I can hardly imagine a better date..."
    mc "And hey, it's not even over yet!"
    show cx 59
    a "I wish we could stay like this forever..."
    stop music2b
    $ renpy.end_replay()


label ga_dalia2:
    $ renpy.music.set_volume(0.4, channel='music3')
    stop music fadeout 1
    stop musicb fadeout 1
    stop music2 fadeout 1
    stop music2b fadeout 1
    play music3 covesexy fadein 2
    scene cd 34 with dis
    d "I'm talking about the bet. Let's do it."with dis
    show cd 33
    mc "The..."
    mc "W-Wait, what?"
    show cd 34
    d "Isn't that what you wanted?"
    show cd 33
    mc "Um... y-yeah..."
    play sound sand
    show cd 35
    d "*Undoing her bikini* Never let it be said that Dalia doesn't honor her bets." with dis12
    if not rotundafail:
        d "The other day I bet and won 100 eternals in the rotunda from Jasticus' trainer."
    d "Sometimes you win, sometimes you lose..."
    play sound2 sand
    show cd 36
    mc "*Standing up* Did this really work? Or am I dreaming?"with dis12
    show cd 37
    d "Everything you did for me today really meant a lot. Coming to the competition, giving me that pep-talk before the trials, cheering me on and cheering me up..."with dis04
    d "You came looking for me when I was at one of my lowest points, and you helped me regain my self-esteem."
    d "And... well, that kiss honestly wasn’t half bad."
    d "So... as a thank you for everything... I'm choosing not to overthink your definition of \"beating me in a fight.\""
    show cd 38 with dis17
    mc "My god..." with dis08
    mc "You're fucking perfect..."
    show cd 39
    d "You’re saying so many nice things today... but well, I can't say I don't like being praised..."with dis04
    play sound sand
    show cd 40
    if dalianaked:
        d "I know you already saw me naked, but I hope this can still get you in the mood." with dis12
    else:
        d "Well... I hope this is enough to get you in the mood."with dis12
    d "It's gonna be difficult to do my part otherwise."
    show cd 41
    mc "I doubt that'll be a problem..."
    if dalianaked:
        show cd 40
        d "At least this time I'm getting naked for you voluntarily, not accidentally. You creep."
        show cd 41
        mc "I thought it was clear that that was just a huge misunderstanding..."
        show cd 40
        d "*Giggles* I still have my doubts..."
    show cd 42 with dis15
    d "*Starts to slowly open your fly*"with dis08
    mc "(Oh... fuck yeah!)"
    play sound zip
    pause .2
    play sound2 clothes3
    show cd 43 with dis17
    d "What the..." with dissolve
    d "Jesus Christ..."
    d "I wasn't expecting..."
    d "T-That..."
    show cd 44
    mc "*Taking off your shorts* I mean..."with dis15
    play sound clothes3
    show cd 45
    mc "You made me so fucking horny, Dalia. Do you see how hard you made me?"with dis12
    mc "I’m like a rock. Couldn't help it. Your tits, your ass, your abs... the entire package."
    show cd 46
    d "Still, that was way too fast. Did you get hard during our sincere and emotional exchange?"with dis04
    show cd 45
    mc "Of course not... only once you took off your pants. Your tummy is way too sexy."with dis04
    show cd 46
    d "I'll choose to believe you..."with dis04
    d "I don't want to dirty our best memory together."
    show cd 45
    mc "Dirty the memory? We're only making it better..."with dis04
    show cd 46
    d "Yeah, I’m sure we’re making it better for you."with dis04
    d "Anyways..."
    d "I should probably start before this... monster starts going down."
    show cd 45
    mc "I don't think that's gonna happen..."with dis04
    mc "Take your time... I’m not in a rush."
    show cd 47
    d "*Gets close to you*" with dis15
    mc "(Oh fuck yeah...)"
    d "(Jesus, this thing looks huge up close... and the smell...)"
    show cd 48
    mc "You sure you can take it?" with dis
    show cd 49
    d "Of course."
    show cd 48
    mc "Is it making you horny?"
    show cd 49
    d "N-no!"
    show cd 48
    mc "You're in denial today, Dalia..."
    show cd 50
    d "I'm already starting to regret agreeing to this."with dissolve
    mc "Your mouth says that, but your eyes say otherwise..."
    d "Shut up, idiot."
    show cd 51
    blank "{i}She starts licking the head of your penis."with dis12
    mc "Oh, yeah..."
    show cd 52
    blank "{i}Gently kisses and licks you along the length of your cock."with dis12
    show cd 51
    mc "(I can feel how her breathing keeps speeding up...)"with dis12
    show cd 52
    mc "You're driving me insane, Dalia..." with dis12
    mc "Stop teasing me... Put it inside your mouth, please..."
    d "I thought you said you weren’t in a rush..."
    show cd 51
    mc "I might have spoken too soon..."with dis12
    show cd 53 with dis12
    mc "Oh, y-yes..." with dissolve
    show cd 51
    d "Does it feel good?" with dis12
    show cd 53
    mc "It feels amazing..." with dis12
    show cd 54
    d "*Slight moan*"with dis12
    mc "Oh fuck yeah, baby..."
    show cd 55
    mc "(Oh my god, Dalia's sucking my cock...)"with dis12
    mc "(This is like a dream come true...)"
    show cd 56
    mc "Oh... fuck, your mouth is so warm..." with dis12
    mc "That’s a good girl..."
    show cd 57
    mc "(God, I'm stretching her little mouth so much...)"with dis
    show cd 56
    mc "That's it, Dalia..."with dis
    mc "Deeper..."
    show cd 57
    mc "Make it wet..."with dis
    show cd 58
    mc "Now, let's try that little thing we talked about all those weeks ago, shall we?" with dis12
    d "Mmmm...?"
    play sound blow4
    play sound2 blow4
    show cd 59
    blank "*You gently push Dalia's head further onto your cock*"with dis12
    d "Mmmph!"
    mc "Oh f-fuck, yes!"
    play sound3 blow5
    show cd 60
    d "*Recovering her breath* AAahh..." with dis12
    mc "Holy shit, so it was true, huh? No gag reflex..."
    d "*Panting* I m-might have underestimated the size..."
    mc "Is it too much for you?"
    d "*Panting* Of course not, but..."
    d "W-Well, I s-still have to breathe, you know?"
    d "Are you trying to kill me?"
    mc "Not at all..."
    mc "I'll let you set the pace... Be as greedy as you want."
    show cd 56
    d "Hmmmph..." with dis12
    mc "Oh yeah... that's a good girl..."
    $ renpy.music.set_volume(0.1, delay=5.0, channel='music3')
    play music blowjob2 fadein 5
    scene daliablow1 with Dissolve(2.5)
    mc "Ohhhh Jesus..."with dis08
    mc "(She's taking it so fucking deep...)"
    mc "(God, I can feel the tip of my cock slipping down her throat...)"
    mc "(And yet, she keeps taking it in and out without a single gag...)"
    d "*Moans*"
    mc "H-Holy shit, Dalia, you're a fucking natural..."
    mc "It’s so tight... almost feels like a pussy..."
    mc "Ahhh..."
    mc "Your throat’s squeezing me so much..."
    mc "Y-You're enjoying this too, aren't you?"
    d "Mmmmhmm..."
    mc "That’s what I thought... You dirty girl..."
    pause
    mc "Come here, I wanna fuck your little mouth..."with dissolve
    d "*Moans*"
    mc "That’s it..."
    play music2 blowjob4 fadein 5
    stop music fadeout 5
    scene daliablow2 with dis2
    mc "A-A-Aaaahh f-fuck yes...!" with dissolve
    mc "Oh my god, Dalia...!"
    mc "(It slides in so easily... her throat feels tight, but there’s no resistance...)"
    d "Mmmm...!"
    scene daliablow3 with dis17
    mc "Ahhh...." with dissolve
    mc "You're basically drooling, Dalia... You like my cock that much?"
    d "Mmmph..."
    mc "You're doing an amazing job..."
    mc "Oh god..."
    mc "If you wanna stop, just give me a sign, babe..."
    d "Mmm...!"
    mc "(At first I thought she was trying to prove something, but looking at her face I can tell she's enjoying it...)"
    mc "Aaaahhh..."
    mc "Fuck, I don't think anyone could take it so deep and so fast..."
    scene daliablow4 with dis17
    mc "Oh f-fuck yeah..." with dissolve
    mc "Do you like getting your mouth fucked, Dalia?"
    d "Hmph... mmph... mmph..."
    mc "That’s it, work all that cum out..."
    mc "(And her tongue gliding on the underside of my dick feels too good, even if it barely has space to move...)"
    pause
    mc "Oh g-god... I think I'm gonna cum..."with dissolve
    mc "I can't hold it...!"
    stop music2
    play sound4 blow1
    play sound6 blow4
    scene cd 60b
    d "*Pulls away and takes several breaths* F-FUCK!" with dissolve
    play sound snow2
    play sound3 sand
    scene cd 61
    d "*Lies back on the sand* J-Jesus...!" with dis08
    d "*Panting* T-Too much... d-dick... N-Need... oxygen!"
    mc "Are you okay?"
    d "*Panting* Fuck yeah, I am..."
    d "It's just that... t-that thing is... too big..."
    d "I couldn't fucking breathe... How do they do that shit in porn!?"
    play sound sand
    show cd 62
    mc "*Getting on top of her* Oh shit, Dalia..."with dis08
    mc "You have no idea how close I am..."
    show cd 63
    d "Oh, that's too bad... poor baby [mc]..."
    show cd 62
    mc "My balls are about to explode..."
    show cd 63
    d "Stop groping me!"
    show cd 62
    mc "Your boobs are fantastic, did I ever tell you that?"
    show cd 63
    d "Never, not even once."
    show cd 65b
    mc "*Pinching her nipples* And your hard nipples give you away – you're horny as fuck..." with dis
    show cd 64
    d "*Giggles* Shut up!"with dis
    show cd 65
    mc "But it's true... isn't it?"
    show cd 64
    d "Perhaps."
    show cd 65
    mc "I want to cum on your pretty little face, Dalia..."
    d ". . ."
    show cd 64
    d "{size= 22} Cum in my mouth..."with dissolve
    show cd 65
    mc "I'm sorry, what did you just say?"with dis04
    show cd 64
    d "Cum{w} in{w} my{w} mouth."
    show cd 65
    mc "Would you like that, you slutty pervert? Are you hungry for some cum?"
    show cd 66
    d "Please..." with dis15
    show cd 67
    d "I want you to release your seed in my little mouth..."with dis12
    show cd 66 with dis12
    d "*Whispering* All of it..."with dis
    d "Pretty please..."
    d "Haven't I done such a good job?"
    show cd 67
    mc "(Oh my god...)"with dis
    mc "Open up for me, babe..."
    play music2 blowjob2 fadein 2
    scene daliablow5 with dis17
    blank "{i}Slightly opens her mouth to let your dick in." with dissolve
    mc "Oh, yeah, that's it..."
    d "Mmm..."
    mc "Ahh..."
    mc "(Her lips wrap around me like a second skin...)"
    mc "Oh god, go faster, Dalia..."
    mc "Take it all in..."
    stop music2 fadeout 2
    play music blowjob2 fadein 3
    scene daliablow6 with dis15
    mc "AAagh... yeah...!"with dissolve
    d "Mmmph... mmmph... mmph..."
    mc "You little cum addict... You want it so bad, don’t you?"
    mc "You drive me crazy when you look me in the eyes like that..."
    d "Mmmm..."
    mc "F-Fuck, I'm gonna cum so much..."
    mc "Are you sure you can take it?"
    d "Mm-hmmm...."
    stop music fadeout 2
    play music2 blowjob4 fadein 3
    scene daliablow7
    mc "*Grabbing her head with both hands and taking control of her movement* AAaahhh... fuck!" with dis15
    mc "Oh... D-Dalia..."
    mc "(Holy shit, I can feel the back of her throat with each thrust...)"
    mc "Oh god, I'm cumming..."
    mc "I'm cumming!!!"
    stop music2
    play sound cum1
    play sound2 cum2
    play sound3 cum3
    scene cd 68
    mc "*Burying your cock balls deep into Dalia's mouth* AAAAAArgh...!" with hpunch
    play sound4 cum3
    d "Gggh...!"with hpunch
    play sound5 cum3
    d "Ghhhh...."with hpunch
    play sound6 cum3
    mc "*Still cumming* Aaahhh..."with hpunch
    play sound blow4
    show cd 69
    mc "Jesus fucking Christ..." with dis15
    mc "I came like a horse... Are you okay?"
    d ". . ."
    play sound swallow
    show cd 70
    d "*Swallows*" with dis
    d "Mm-hm..."
    mc "Good girl..."
    stop music3 fadeout 7
    play music waves2 fadein 7
    show cd 71 with dis2
    d "*Wipes off her mouth* God..." with dissolve
    d "Strangely, it tastes exactly like I thought it would..."
    show cd 72
    mc "Well, well, well... so you openly admit having fantasized about how my cum tastes, huh...?" with dis12
    show cd 74
    d "Oh, shut up!"with dis15
    show cd 73
    mc "But seriously though, that was... unbelievable!"
    show cd 74
    d "By the amount of... jizz you just dropped in my tummy, I could tell you enjoyed it, yeah..."
    stop music
    $ renpy.end_replay()





label ga_nancy1:
    stop music fadeout 1
    stop musicb fadeout 1
    play music2 sexy3 fadein 1
    stop music2b fadeout 1
    stop music3 fadeout 1
    scene bt 27 with dis
    n "Oh, before I forget..." with dis
    mc "(I’d hate myself if I didn’t at least try...)"
    n "I think this goes without saying, but let’s not mention this to anyone. My daughters especially... heavens knows what they’d think if they learned we bathed together."
    n "They'd probably end up–"
    play sound water2
    show bt 28 with hpunch
    pause
    show bt 29 with dis08
    pause
    show bt 28
    n "[mc]?" with dis08
    mc "I couldn't find the wine, my Empress, but I believe I’ve come up with a better way to serve you... if you so desire..."
    show bt 30
    n "Oh, really...?" with dis08
    n "Please enlighten me, my Champion..."
    show bt 31
    mc "Well, I thought we could make your first day on Eternum much more... memorable."with dis04
    show bt 30
    n "Memorable, you say? Well I’m already having a difficult time not thinking about just how hard you feel pressed against me..."with dis04
    show bt 31
    mc "My only wish is to serve my Empress."with dis04
    play soundlow water3
    show bt 35
    mc "*You start kissing her neck*" with dis
    n "Oh, [mc]..."
    n "W-What are you doing..."
    mc "If you want me to stop, please—"
    n "Don’t you dare."
    play soundlow water2
    show bt 36
    mc "*Giving her a hickey*" with dis
    n "*Whispers* Mmmm..."
    mc "(Finally I get to feel Nancy’s breasts filling my hands... they’re so much bigger than I thought...)"
    mc "(I can even feel her heart beating so quickly... she seems nervous, yet so excited at the same time...)"
    mc "(I can tell she was looking forward to this.)"
    play soundlow water
    show bt 32
    mc "God..." with dis
    show bt 34
    mc "I can’t keep my hands off of you. Every inch of you is just so... unreal!"with dis08
    mc "Have you always had such amazing breasts?"
    show bt 33
    n "*Giggles* Since I was 17." with Dissolve(.7)
    show bt 32
    mc "I guess I never paid attention back then, since I was only five and had no interest in them..." with dis04
    show bt 33
    n "*Giggles* Well I’m so glad you’re paying attention to them now..." with dis04
    n "Oh [mc]... how you’ve grown into such a strong, handsome man..."
    n "After having taken care of you for so long back then... I never thought we’d be in this position now..."
    show bt 32
    mc "Does that mean you won’t take care of me anymore then?"with dissolve
    show bt 33
    n "Oh, I will. Just... in another way."with dissolve
    play soundlow water3
    show bt 35
    n "Ohh..." with dis
    play soundlow water2
    show bt 36 with dis
    pause
    play soundlow water3
    show bt 37
    n "Oh, my boy..." with dis
    mc "*Sucking and licking her nipples* (I can feel her breath spike with every dash of my tongue against her nipples...)"
    mc "(I love how hard they are...)"
    play soundlow water
    show bt 38
    n "Ahh..." with dis
    n "You have no idea how much I’ve fantasized about this moment, [mc]..."
    mc "(She feels so warm... her skin is so soft and smooth...)"
    n "Ahhhhh..."
    play soundlow water2
    show bt 39 with dis15
    n "*Coming out of the water* Alright..." with dissolve
    n "I can’t hold back anymore."
    play sound fall2
    show bt 40 with dis12
    n "Does the Champion truly want to serve his Empress?" with dissolve
    show bt 41
    mc "More than anything in this world."
    show bt 40
    n "You know... I remember from my history classes that it was always taboo for royalty to intermingle with common folk..."
    n "But I think we’ve broken enough rules today..."
    show bt 40
    n "I need to feel my Champion... taste the forbidden fruit..."
    show bt 42 with dis12
    pause
    mc "You're..."with dis08
    mc "Perfect..."
    show bt 43
    mc "I can’t hold back any longer..." with dis12
    mc "I want you so bad, Nancy..."
    show bt 44 with dis15
    n "AAaaaahh..." with dis
    n "Just like that..."
    scene nancycun1 with dis15
    n "Ahhh..." with dissolve
    n "Yeah..."
    mc "(I’ve barely even started and Nancy’s juices are already covering my face...)"
    mc "(She really has been waiting for me...)"
    n "Y-You... you really do know..."
    n "Ah!"
    n "What you’re doing..."
    mc "(Her little whimpers are turning me on so much...)"
    mc "(I can’t get enough of her taste...)"
    n "Oh, my C-Champion feels..."
    n "Oh, s-screw the Champion shit..."
    n "Yes [mc]! YES!"
    scene nancycun2 with dis15
    n "*Moaning louder* Ahhh... d-don’t... don’t stop..." with dissolve
    n "Jesus Christ..."
    n "I g-guess you... really could be a... good candidate after all..."
    pause
    n "MMmmmh..." with dissolve
    n "I c-can’t remember... t-the last time... I’ve f-felt like th–"
    n "AH! AH!"
    n "Oh my god [mc], I think I'm actually g-going to c-come..."
    mc "(Already?)"
    n "I haven’t b-been able to... in s-so long..."
    n "P-Please!"
    n "Don’t stop!"
    n "Right..."
    n "There..."
    n "You..."
    n "You're..."
    play sound cum2
    scene bt 45
    n "AAAAAhhh...!!!" with hpunch
    play sound2 cum2
    n "AAAhhhhhhhhh...." with hpunch
    mc "(Damn, she came HARD!)"
    n "OH MY GOD!!!" with hpunch
    n "I c-can’t..."
    n "F-Feel my legs..."
    n "Ahhh... Christ!! I’m looking like some inexperienced teenager here... this is so embarrassing..."
    n "What have you done to me?!"
    n "AAaahh..."
    n "P-Please, give me a minute..."
    n "I need to..."
    mc "You took care of me countless times..."
    play sound water2
    show bt 46
    mc "*Dragging her to the edge of the pool* Now I want to keep taking full care of you..." with dis12
    n "*Giggles* [mc]! You’re insatiable!"
    mc "I wanna make you squirm again..."
    mc "Just relax..."
    mc "And let me do all the work..."
    n "Mmhm..."
    play soundlow water3
    show bt 47
    mc "*Lifting her hips* Now come here..." with dis
    n "Oh [mc], how are you so strong?!"
    scene nancycun3 with dis15
    n "OH MY GOD...!" with dissolve
    mc "(I'll focus on her clit now... keep my licks gentle and steady...)"
    n "AAaaaaahh..."
    n "*Moaning* Oh my g-gawd...."
    mc "(Man, Nancy is dripping wet right now...)"
    n "*Moaning* Ahhh.... ahhh... aghh..."
    n "Yeah..."
    mc "(I love how flexible she is.)"
    mc "(The yoga classes are definitely paying off...)"
    n "Aaaaaah... y-yeahh...!"
    mc "(Who would’ve thought we’d end up in this kind of pose together...)"
    n "Keep that rhythm [mc]..."
    n "Aaaahh..."
    scene bt 48 with dis15
    play sound bombdistant1
    show bt 48 with hpunch
    pause 1
    play sound2 drain
    show bt 49 with dis2
    mc "W-What was that...?"with dissolve
    n "Ahh, w-what? I d-didn't hear anything..."
    mc "All the water is gone too..."
    n "M-Maybe a p-pipe e-exploded... I d-don’t care... just PLEASE D-DON’T STOP NOW!"
    mc "Now you'll see what else I can do..."
    scene nancycun4 with dis2
    n "A-A-AAAHHH..." with dissolve
    n "H-Holyyy fuuuck!! [mc]!!"
    mc "(This pose is so damn sexy. And I can suck on her clit at the perfect angle...)"
    mc "(The way she’s gyrating her hips... it’s like she’s begging for more...)"
    n "AAAaahhh... AAAAhhh... J-Jesus Christ..."
    mc "(She's getting there...)"
    hide nancycun4
    scene nancycun5
    n "AAAAaaghhh..." with dis15
    n "Oh g-god, [mc]...!!!"
    n "Please keep going..."
    n "Take all of me..."
    n "I’m yours my b-boy..."
    n "...aaaAHHHHhh...."
    mc "(Time to shift into the final gear...)"
    hide nancycun5
    scene nancycun6
    n "AAAAaaghhh..." with dis15
    n "HHHgggg... T-This is... insane..."
    mc "(Her legs are trembling.)"
    play sound bombdistant1
    pause
    n "I'M G-GONNAA C-CUM A-AGAAAIN...!"with dissolve
    n "AHHH.... AAAHHHHH!"
    n "R-Right there, right there, right t-thereeeeee..."
    n "AAHH Y-YEAAH!"
    play sound cum2
    scene bt 50
    n "THAT’S ITTTTT...!!!" with hpunch
    show bt 52 with dis
    n "GGgggghhh...." with dissolve
    mc "(Holy shit, that was a huge orgasm! Her entire lower body is quivering...)"
    n "*Panting* J-Jesus... C-Christ..."
    n "I d-didn't even know... I c-could feel like this..."
    show bt 50
    n "Oh [mc]..." with dis
    play sound blow1
    show bt 51
    mc "Your taste and smell are so intoxicating, Nancy..." with dis12
    n "*Giggles* I c-can't believe I've come two times in a row... in such a short amount of time..."
    n "You made a mess of me..."
    play sound fall2
    show bt 53
    mc "Phew, that position was exhausting, but well worth it. I just need to catch my breath for a sec..." with dis08
    show bt 54
    n "I thought you wanted to take full care of me...?" with dis
    mc "Well look who’s insatiable now..."
    show bt 55
    n "*Getting on top of you* It’s time I get what I’ve been really hungry for..." with dis12
    show bt 56
    mc "Oh my god..." with dissolve
    mc "A-Are you sure you wan–"
    play sound bombdistant1
    show bt 55
    n "I want you to fuck me, [mc]." with dissolve
    n "I've wanted you to fuck me ever since I first saw you in that park. I thought maybe it was just a fleeting urge and it’d pass quickly... but no..."
    n "I can’t stop thinking about you filling me up."
    n "I want to fulfill all the fantasies I haven't even dared to tell anyone about."
    show bt 56
    mc "I'll fulfill them all..."with dissolve
    play sound bombdistant1
    show bt 57
    n "And now..." with dis
    n "Your huge cock is gonna be deep inside of me..."
    n "So I can feel every inch of you..."
    n "This time though... I want you to lie back and let your babysitter do all the work..."
    n "Because I’m gonna ride you until you burst..."
    mc "Oh my god, Nancy..."
    show bt 58 with dis12
    n "AAahh..." with dissolve
    mc "I can’t believe this is really happening..."
    n "*Giggles* Believe it, baby... Now fuck me already..."
    show bt 59
    n "AAAaahh..." with dis12
    mc "Ohhh fuuuu..."
    play soundlow bombdistant1
    n "God [mc], you’re so damn big..."
    mc "Yeah... and that’s only the tip..."
    n "Please... push it deeper... fill me up!!"
    stop music2 fadeout 2
    play music2b fireplace
    play sound doorwoodclose
    play sound2 rocks
    show bt 60 with dis
    play soundlow bombdistant1
    leg "MY EMPRESS!" with hpunch
    play sound splash2
    n "*Whispering* W-What the...!"
    stop music2
    $ renpy.end_replay()






label ga_side2:
    stop music fadeout 1
    stop musicb fadeout 1
    stop music2 fadeout 1
    stop music2b fadeout 1
    $ renpy.music.set_volume(0.2, channel='music3')
    play music3 sexy2 fadein 1
    scene bbb 101 with dis
    mc "W-What now...?" with dis
    mc "Holy shit Maat, what a body..."
    show bbb 103
    ma "You're done now. You're free to go." with dis08
    ma "There's an Exit Portal just behind the temple, between two granite rocks."
    ma "And you can take the girl's gun, I don't want it anymore."
    ma "Thank you for playing with me. I hope you enjoyed the game."
    show bbb 101
    mc "What? But..." with dis08
    mc "I gotta finish now! You can't leave me hanging like this!"
    show bbb 102
    ma "Yes, I can, and I will." with dissolve
    ma "I dictate the rules in my own game."
    ma "You're not allowed to cum, unless..."
    show bbb 101
    mc "Unless?" with dissolve
    show bbb 102
    ma "Unless you finish with me." with dissolve
    ma "Never in my life have I ever been so turned on. And my clumsy fingers just aren’t satisfying me enough right now..."
    ma "You’ve filled up her mouth, but now I need your big, fat cock to fill me up this time..."
    ma "I need you to fuck me... use every inch of you to finally satisfy the hunger I have deep inside of me..."
    ma "I want you to destroy me..."
    show bbb 104
    mc "You're completely nuts." with dis12
    ma "*Giggles* Tell me something I don't know..."
    mc "So you want me to fuck you?"
    ma "Yes I do..."
    ma "I want you to fuck me so hard..."
    ma "None of that gentle, lovey-dovey shit... I want you to be rough..."
    ma "I want you to use me like a little–"
    play soundlow clothes1
    play sound clothes2
    show bbb 105
    mc "*Pulling her arm* Come here, you psycho bitch..." with hpunch
    ma "YES! LIKE THAT!"
    menu:
        with dis
        "Push her against the wall":
            $ maatsexvariant = True
            mc "I'm gonna teach you a fucking lesson." with dis08
            ma "Yes..."
            play sound fall
            show bbb 109 with dis
        "Pull her to the ground":
            $ maatsexvariant = False
            mc "Get down. Now." with dis08
            play sound jewelry fadein 1.5
            play sound2 clothes3
            show bbb 112b with Dissolve(1.6)
            ma "*Removing her ornaments* ...Or what?" with dis08
            ma "What if I don’t...?"
            play sound6 jewelry2 fadein 1.5
            show bbb 112b2
            mc "Trying to see for yourself?" with dis12
            ma "*Giggles* Mm-hm..."
            mc "I'm gonna teach you a fucking lesson..."
            play sound fall
            show bbb 112 with dis
    ma "YES!" with dissolve
    ma "That’s it! Give it to me!"
    mc "Shut the fuck up already!"
    mc "I'm gonna fucking tear you apart."
    ma "Yeah... Do it... Ravage me..."
    show bbb 106
    no "Oh my god, this sure escalated quickly..."
    no "Um... You... You two go on and do your thing... I'll... I'll be waiting outside."
    if maatsexvariant:
        show bbb 109
    else:
        show bbb 112
    ma "I've been such a naughty girl..."
    ma "Teach me a lesson..."
    ma "Use every part of me for nothing but your pleasure..."
    ma "Abuse me... I deserve it..."
    mc "I hope you're wet enough, cunt."
    ma "I’m dripping for you... now pin me down and shove your rock hard cock inside of me already!"
    ma "Give me every inch..."
    if maatsexvariant:
        show bbb 110
    else:
        show bbb 113
    mc "Now you'll see what happens when you don't listen..." with dis
    ma "Yeah... All of it..."
    ma "Don’t keep me waiting..."
    play sound piston
    if maatsexvariant:
        show bbb 111
    else:
        show bbb 114
    ma "Fuuuuuuuu–!" with hpunch
    ma "*Giggles* Y-Yeah...! That’s it! FUCK!"
    if maatsexvariant:
        show maat8 with Dissolve(2)
    else:
        show maat10 with Dissolve(2)
    ma "Aaahh... Arghhh... Ahhhhh..." with dissolve
    ma "*Panting* Oh my god...!"
    ma "AHHH....!"
    mc "Ahh..."
    mc "I thought a bitch like you would be more loose..."
    mc "(Fuck, it feels amazing to be in control... to be so dominant over her...)"
    mc "(I can feel how my dick is stretching her with every thrust...)"
    ma "A-A-Aaahh... I... I..."
    ma "O-oh my ggga-ad...!"
    mc "What?"
    ma "Aaaahhh...."
    ma "S-Sloo-aaw...!"
    mc "I don't understand what you’re trying to say..."
    ma "Aaahh... Y-You're gonna break me..."
    mc "Good..."
    show novamaat with dis12
    pause
    no "(Oh my god...)" with dissolve
    no "(Why am I still here?)"
    no "(Why can't I stop looking?)"
    no "(That looks so... intense... I can't imagine being in her position.)"
    no "(But it also looks so... arousing...)"
    no "(I m-mean... [mc] seems so powerful...)"
    hide novamaat with dis15
    ma "*Panting* Ahhh... ahhh... ahgh..." with dissolve
    ma "You... you like that...??"
    ma "How you shoved your hard c-cock down her th-throat..."
    ma "And now you’re shoving that cock... deep inside my p-pussy..."
    mc "I do..."
    pause
    scene black with dis12
    if maatsexvariant:
        show maat9 with Dissolve(2)
    else:
        show maat11 with Dissolve(2)
    ma "Ahhh... [mc]..." with dissolve
    mc "(F-Fuck, this is incredible...)"
    mc "(I'm hitting the deepest part of her...)"
    if maatsexvariant:
        mc "(The feeling of her thick thighs slapping against my body with each thrust... it feels so fucking carnal and empowering...)"
        mc "(Watching her huge tits bounce as I slam inside of her...)"
    else:
        mc "(The way her ass feels as it slaps against my hips with every thrust... it feels so fucking carnal and empowering...)"
        mc "(Seeing her tiny waist from above... her body buckling as it gives way to all of me...) "
    mc "(I can't believe I haven't cummed yet...)"
    mc "(But I can feel it building... I’m almost there...)"
    ma "Hhhhgg..."
    ma "You're f-fucking me so h-h-hard..."
    mc "Ahh... This is what you were hungry for, right??"
    ma "Y-Yeah..."
    ma "I'm.... Hggg..."
    ma "I... I c-can’t hold it in... I’m almost there..."
    ma "Keep f-fucking me... just like that..."
    ma "Oh d-don't s-stoppp... pleeeease..."
    ma "AAaaaahh...."
    ma "I'm..."
    ma "Gonna..."
    ma "Fucking..."
    ma "Cummmm–!!"
    play sound squirt
    if maatsexvariant:
        scene bbb 111
    else:
        scene bbb 114
    ma "A-A-Aaa-a-agggghhh....{w=0.25}{nw}" with hpunch
    ma "A-A-Aaa-a-agggghhh....{w=0.25}{nw}" with hpunch
    ma "A-A-Aaa-a-agggghhh...." with hpunch
    ma "F-F-Fuuuuuuuck!!" with hpunch
    if maatsexvariant:
        play sound4 jewelry fadein 1.5
        play sound5 clothes3
        show bbb 115b with dis17
        ma "*Removing her ornaments* Oh m-my g-god...!" with dis08
        ma "I c-can't even..."
        play soundlow fall
        play sound3 fall2
        show bbb 115 with dis08
    else:
        play sound blow3
        show bbb 115 with Dissolve(2)
        play sound2 fall
        play sound3 fall2
    ma "*Collapsing to the ground* Jesus fucking Christ..." with dis08
    ma "M-My whole body is... numb..."
    ma "I've never had an orgasm so strong in my life..."
    ma "F-Fuck, it's still going... Aghhhhh..."
    ma "If this wasn't Eternum, I'd be sore for a week..."
    show bbb 107
    no "(Oh my god...)"
    no "(That must have felt... so intense...)"
    no "(I don’t look anything like that after I do my thing... hm...)"
    show bbb 116
    mc "Fuuuuck, after all that buildup, I can’t keep it in any longer..." with dis12
    mc "My balls are about to explode..."
    ma "*Giggles* Give it to me, baby... cover me..."
    ma "I want to feel your hot seed all over my body..."
    play sound cum2
    show bbb 117
    mc "AAAAaaahhhh!!!" with hpunch
    play sound2 cum2
    mc "Aaaaahh..." with hpunch
    show bbb 118
    ma "MMmmmm..." with dis15
    ma "You're a fucking beast..."
    ma "Just the way I like it..."
    show bbb 119
    ma "Mmmm...." with dis12
    mc "Thank you for this, Maat. It's been... amazing."
    mc "I wasn't expecting to meet someone so depraved today, but you won’t hear me complaining."
    ma "Mm-hm..."
    mc "Maybe we should do it again some time..."
    ma "Mmmm..."
    mc "In the meantime, can you hold this for me, please?"
    mc "It's a present, so you remember us."
    ma "Mm-hmmm..."
    mc "Come on, take a look!"
    show bbb 120
    ma "Hmm...?" with dis12
    show bbb 121
    ma "Huh...?!" with dis
    ma "W-Wha..."
    show bbb 122
    ma "WHAT?!" with hpunch
    ma "F-Fuck!" with hpunch
    ma "Where's my jewel?!"
    ma "Shit, where's Sekhmet's Ornament?!" with hpunch
    stop music3
    $ renpy.music.set_volume(0.2, channel='music3')
    $ renpy.end_replay()



label ga_nova1:
    stop music fadeout 1
    stop musicb fadeout 1
    stop music2b fadeout 1
    stop music2 fadeout 1
    $ renpy.music.set_volume(0.2, channel='music3')
    play music3 sexy2 fadein 1
    scene bbb 70 with dis
    mc "Show her the dagger, Nova." with dis
    mc ". . ."
    show bbb 71
    mc "Nova...?" with dis08
    show bbb 73
    pause
    show bbb 74
    mc "N-Nova?!" with dis
    show bbb 73 with dis
    pause
    no "You’re... massive..." with dis
    show bbb 74
    mc "W-What the fuck?! What's wrong with you??"
    mc "This is not the time for your jokes!"
    show bbb 73
    no "Jesus Christ..."
    no "It's throbbing too..."
    no "Have you ever had sex with a girl? Is she still alive?"
    show bbb 74
    mc "W-What?! Oh come on, d-don't exaggerate!"
    show bbb 73
    no "That would break me in two..."
    no "That's like..."
    show bbb 74
    mc "Nova, focus here!!"
    mc "Do you know where my dagger is?!"
    show bbb 73
    no "Did you get that hard... because of me?"
    show bbb 74
    mc "W-Well, what the hell was I supposed to do?"
    mc "I can't help it, and I'm not a monk alright?!"
    show bbb 73
    no "Whoa..."
    show bbb 36
    ma "*Giggles* You two are way more fun than I was expecting..." with dis12
    ma "Now, if you want your little gun back, you have to do one last thing for me..."
    show bbb 70
    mc "What?! You said you'd let us go! You gave us your word!"
    mc "Fucking liar!"
    show bbb 36
    ma "That’s right, I said I'd let you go. But I didn't say anything about the girl's gun..."
    ma "I always keep my promises, so you're free to go."
    ma "But... if you want the gun, there’s only one more thing left to do..."
    show bbb 70
    mc "Bah! You're a cheat!"
    mc "What the hell else do you want?!"
    show bbb 36
    ma "*Giggles*"
    ma "I want her to wrap those rosy lips around that hard cock... and give you a nice, wet blowjob..."
    show bbb 70
    mc "What? You're..."
    stop music2 fadeout 6
    show bbb 73
    no "O-Ok."
    show bbb 70
    mc ". . ."
    show bbb 74
    mc "D-Did you just say... \"Ok\"?" with dis15
    show bbb 75
    no "I um... can't lose Dione, [mc]."
    no "So I'll... I'll do whatever it takes."
    show bbb 74
    mc "But... Um..."
    mc "Are you sure about this?"
    show bbb 75
    no "We’ve come this far. At this point... one step, more or less, won’t make a difference..."
    no "And w-we have no alternative. Do we?"
    show bbb 74
    mc "Uhh..."
    mc "I guess not..."
    play sound fall2
    show bbb 76
    ma "I already know the answer, but just because I want us to hear it straight from your mouth..." with dis
    ma "You've never done this before, have you?"
    show bbb 77
    no ". . ." with dissolve
    no "Um..."
    no "N-No."
    show bbb 76
    ma "Do you need any tips?" with dissolve
    show bbb 77
    no "No!" with dissolve
    show bbb 76
    ma "You have really juicy-looking lips. You're gonna do just fine." with dissolve
    ma "And I know you're dying to try it... hide it as much as you want, but I know you’re hungry for him. That’s the important part here."
    ma "Oral sex is exponentially more enjoyable when the giving side savors it as much as the receiving side..."
    show bbb 77
    no "W-What are you talking about?" with dissolve
    no "I'm just doing this because you're making me!"
    show bbb 76
    ma "Heh, sure... of course..." with dissolve
    show bbb 77
    no "You better give me my gun back after this." with dissolve
    show bbb 76
    ma "You can ask around. Maat always keeps her promises." with dissolve
    show bbb 78
    ma "*Chuckles* Well..." with dis08
    ma "You better start soon, baby. Don’t want him getting soft on you."
    mc "It's unlikely..."
    ma "*Chuckles* This might be the best show I've ever seen..."
    ma "I'll give you two some space..."
    play sound clothes3
    show bbb 79 with dis15
    pause
    show bbb 80
    no "*Slowly approaches*" with dis15
    mc "(Oh god...)"
    mc "(I can feel her warm breath on me...)"
    show bbb 81
    mc "Are you sure you’re okay with this, Nova?" with dis
    mc "We can..."
    mc "We can come back to get your gun another day. I wouldn't want you to..."
    no "It's okay."
    show bbb 80
    no "It's alright..." with dis
    no "Why go through all that extra trouble? I would feel much better leaving this place with Dione back in my possession."
    no "Satisfying the wishes of a nympho freak seems like a small price to pay."
    show bbb 82
    no "*Gently pushes your dick with her cheek*" with dis15
    mc "(Fuck, I'm rock-hard right now...)"
    no "Hm, you don’t smell bad at all..."
    show bbb 83
    no "*Starts licking your glans*" with dis12
    mc "Oh g-god, that feels good...."
    mc "Your tongue feels so soft... and warm..."
    show bbb 84
    no "And you taste... just like your smell. Like you, but stronger." with dis15
    mc "(I need to feel the inside of her mouth so bad...)"
    show bbb 83
    no "*Keeps licking*" with dis15
    show bbb 83b
    no "*Gently kisses your glans*" with dis12
    mc "(She drives me insane every time she looks me in the eyes...)"
    show bbb 83
    mc "Oh god, I can't bear the teasing anymore..." with dis12
    show bbb 90
    ma "Fuck, you two are so hot..." with dis12
    show bbb 83
    no "I don’t know if I can fit it all in my mouth..." with dis12
    show bbb 83b
    mc "I'm sure you can... At least the tip..." with dis
    show bbb 83
    mc "Try it..." with dis
    show bbb 85
    no "Mmm...." with dis15
    mc "Oh, yeah..."
    show bbb 83
    no "Like this?" with dis15
    mc "Yes..."
    show bbb 85
    mc "Oh..." with dis15
    mc "Just like that..."
    show bbb 90
    ma "Oh, fuck yes!" with dis12
    ma "This is so hot!"
    ma "Come on, baby..."
    show bbb 86
    ma "Take him a bit deeper now..." with dis12
    show bbb 87 with dis15
    pause
    show bbb 86
    ma "There you go..." with dis12
    show bbb 87 with dis15
    pause
    show bbb 86
    ma "Oh god..." with dis12
    $ renpy.music.set_volume(0.17, channel='music3')
    show bbb 87 with dis15
    pause
    $ renpy.music.set_volume(0.15, channel='music3')
    show bbb 88
    no "Mmmm..." with dis15
    $ renpy.music.set_volume(0.13, channel='music3')
    show bbb 86
    mc "Oh my god, Nova..." with dis15
    show bbb 88
    no "Mmmmhh..." with dis15
    $ renpy.music.set_volume(0.1, channel='music3')
    play music blowjob2 fadein 2
    show maat2 with Dissolve(2)
    pause 1
    mc "You feel... so amazing..." with dis
    mc "(She doesn't look like she's being forced to do anything...)"
    mc "(She’s giving it her all... making my cock so wet and sloppy... I'm fucking loving it...)"
    scene bbb 90
    ma "That's how you do it! Atta girl!" with dis
    ma "This spectacle is pleasing the Pharaohs, Nova!"
    show maat2
    no "Mmm..." with dis15
    ma "Suck it deep, baby..."
    mc "Oh, fuck yes..."
    pause
    show maat3
    ma "I thought a cock of that size would be too much for your first time..." with dis15
    ma "But you seem to be handling it so well..."
    no "*Gagging* M-Mmm..."
    ma "I can see from here how her pussy is dripping wet, [mc]."
    ma "I think she's enjoying this moment more than us..."
    stop music fadeout 1
    play sound blow3
    scene bbb 89
    no "*Recovering her breath* Aghhh..." with dis15
    no "That's... not true..."
    no "I'm just... doing this... because... you... are making me..."
    show bbb 90
    ma "*Giggles* Of course!"
    ma "Just a little bit more, alright?"
    show bbb 89
    no "*Recovering her breath* A bit... more?"
    mc "Yes, please..."
    no "Ok..."
    show bbb 87
    no "Mmm..." with dis12
    play music blowjob2 fadein 3
    show maat4 with Dissolve(2)
    pause 1
    mc "Oh, Nova..." with dis
    mc "(The way she glides her tongue along my shaft, while she continues to suck every bit of my cock... it feels amazing...)"
    mc "(And I love the gagging sounds she's making... They're driving me crazy...)"
    mc "You're incredible..."
    no "*Moaning* Mmmm..."
    pause
    show maat5 with Dissolve(2)
    mc "Ahhh... Just keep it up..." with dis08
    ma "You might deny it now, but I know this is not the last time you'll be doing this to him, baby..."
    ma "You’re only going to crave it more and more... needing to feel him fill up your mouth every day... and you’re going to love each second of it..."
    mc "(Oh god, I fucking hope so...)"
    mc "(I don't even remember where I am... Or why I came here...)"
    mc "(All I can focus on now... is her...)"
    pause
    stop music fadeout 1.5
    play sound blow3
    scene bbb 100
    mc "*Standing up* Ahhh, fuck yeah..." with dis12
    no "*Recovering her breath* Ahhh.... ahh... ahh..."
    no "I need... a minute..."
    show bbb 91
    ma "You two are something else..." with dis08
    show bbb 100
    no "Ahhh... Ahh... Is this... enough?"
    show bbb 91
    ma "Almost... Just a little bit more..."
    show bbb 100
    no "Why do you... enjoy this so much...?"
    show bbb 92
    ma "I get off on the feeling of power..." with dis08
    ma "And I love watching..."
    ma "Usually, I just settle for forcing my male visitors to jerk off, only to kick them out right before they finish."
    ma "I never had the chance to do this... And it's a million times better..."
    play sound clothes3
    show bbb 94 with dis15
    pause
    show bbb 95
    ma "Fuck... Look at what you're doing to me..." with dis15
    ma "I'm so horny..."
    show bbb 96
    ma "*Fingering herself* Come on, keep going..." with dis12
    ma "Don't you wanna fuck her mouth, [mc]?"
    show bbb 100
    mc "I do..." with dis
    no "Fuck... my... mouth...?"
    mc "You’ve got me dying for more. I want you to swallow every inch, Nova, so I can feel the back of your throat..."
    no "*Giggles*"
    no "You're so raunchy, [mc]..."
    no "But..."
    no "Well... I guess we’ve already passed the point of no return..."
    mc "(Fuck yes...)"
    show bbb 98
    mc "*Gently placing Nova's head right in front of your dick*" with dis15
    no "W-Wait! I can't take it all!"
    no "M-My mouth is too small!"
    mc "It’s alright, just take it as far down as you can comfortably go..."
    no "B-But..."
    no "Well, okay, I'll try..."
    mc "That's my favorite little hacker girl... just tap me on the thigh if it’s too much..."
    mc "Mmm, come here..."
    play sound blow1
    show bbb 99
    no "*Gagging* Hhhhmf!!" with dissolve
    mc "Aaaahh... yeah...."
    show bbb 96
    ma "Oh my god... You're gonna be a pro, ginger girl..." with dis
    play music blowjob2 fadein 3
    show maat6 with Dissolve(2.1)
    pause 2
    mc "Oh my fucking god, yes..." with dis08
    mc "(Her lips are wrapped around my dick so tightly...)"
    mc "(For someone with such a tiny mouth, she’s handling me like a champ...)"
    mc "You feel unbelievably good, Nova..."
    no "MMmmmmm..."
    mc "Aaaahhh... yes..."
    ma "It’s like you two are perfectly synchronized..."
    mc "Yes..."
    mc "(It really feels that way...)"
    mc "(The way she’s stuffing her mouth with as much of my cock as she can handle... I thought for sure she’d be choking by now...)"
    mc "(But she hasn’t asked me to stop at all...)"
    pause
    show maat7 with Dissolve(2)
    no "*Gagging* Ahmmmmm..." with dissolve
    mc "Ahhh..."
    mc "Looks like computers aren’t your only talent..."
    no "Mm-hmmm...."
    mc "Fuck, I'm gonna cum..."
    mc "I'm at my limit..."
    ma "Stop!" with hpunch
    stop music fadeout 1
    play sound blow3
    scene bbb 100
    mc "W-What?" with dis
    no "*Gasping for air* AAAAaaaaahhh...!"
    no "Oh my god..."
    stop music3
    $ renpy.music.set_volume(0.2, channel='music3')
    $ renpy.end_replay()



label ga_annie1:
    stop music fadeout 1
    stop musicb fadeout 1
    play music2 anniesexy fadein 1
    stop music2b fadeout 1
    stop music3 fadeout 1
    scene an 61 with dis
    mc "Um... Annie...?" with dis
    show an 59
    a "Y-Yeah...?" with dis
    show an 58
    mc "I’m just going to come right out and say it. I can’t help it, you’re really turning me on right now..."with dissolve
    show an 59
    a "R-Really? W-Well... I guess that’s normal, given the circumstances."with dissolve
    a "...But, for what it’s worth, you’re really turning me on too..."
    show an 58
    mc "I’m sorry, I know I must be really poking you right now..."with dissolve
    show an 59
    a "*Nervious laughter* D-Don't worry! It's okay..."with dissolve
    a "It um... doesn't bother me."
    show an 61
    mc "(Well, here goes nothing...)" with dis
    a "(\"Doesn't bother me\"?? Really, Annie?!)"
    a "(Couldn't you think of anything better to sa—)"
    show an 62
    a ". . . !" with dis
    show an 64 with dis12
    pause
    show an 65
    a "(Is that his...?)" with dis
    mc "I’m sorry, Annie... I can’t help it... you’re driving me insane..."
    mc "Are you okay with this...?"
    show an 64
    a "Yes... " with dis
    a "You feel... good there..."
    show an 65 with dis
    a "But now I wanna know how you feel back here..." with dis
    $ renpy.music.set_volume(0.43, channel='music2')
    show an 66 with dis
    pause
    $ renpy.music.set_volume(0.37, channel='music2')
    show an 65 with dis
    $ renpy.music.set_volume(0.3, channel='music2')
    mc "Oh god, Annie..." with dissolve
    a "Does that feel okay...?"
    mc "It does... C-Come here..."
    show annierub0 with dis15
    pause
    a "Ahh..." with dis
    mc "You still... good...?"
    a "Yes... But... Now I’m the one feeling a little uncomfortable..."
    a "It’s just, my pants..."
    a "They're rubbing against my..."
    mc "Maybe I can help you this time..."
    mc "Move aside for a second..."
    play soundlow chair1
    scene an 67 with dis
    a "Alright..." with dissolve
    mc "Can I... take off your pants...?"
    a "[mc]... Um, I don’t know if I’m ready to go all the way toni-"
    mc "No, no. Of course. I just want to cuddle a little closer with you..."
    a "Mmm, that does sound nice..."
    mc "I just wanna feel your soft skin..."
    a "*Giggles*"
    a "I’m sorry. I’m just a little nervous because no one has ever touched me there before, or even seen it, for that matter."
    a "Just you."
    mc "I know. If it’s too much all at once, we can just..."
    a "[mc]. I said I’m nervous, but that doesn’t mean I... don’t want to..."
    mc "Uhh—"
    play soundlow chair1
    show an 69
    a "Pants off, right?" with dis12
    a "To... feel more comfortable."
    mc "Y-Yeah. To feel more comfortable."
    a "Alright..."
    play sound chair2
    show an 70 with dis15
    mc "(If this is a dream, please god don’t wake me up now...)" with dissolve
    a "*Giggles* I can't believe I'm doing this. This is a side that I’ve never shown to anyone before..."
    play sound clothes
    show an 71 with dis15
    pause .6
    show an 72 with Dissolve(2)
    mc "Holy..." with dissolve
    show an 73
    a "Oh god... now I feel even more embarrassed..." with dis
    mc "Don’t be. Let me get a better look at you."
    a "B-Better... look...?"
    a "Are you s-sure you..."
    show an 74 with dis12
    mc "I’ve never been more sure, Annie." with dis
    mc "I've wanted you for so long."
    a "R-Really? But..."
    a "I thought you weren’t interested in me..."
    show an 75
    mc "Where did you get that idea from?" with dis
    mc "You're perfect."
    mc "And I’m not just saying that because I’m finally seeing your gorgeous body. You’ve always been perfect to me... inside and out. I just didn’t want to risk ruining our friendship."
    a "W-What? M-Me either!"
    show an 76 with dis
    pause
    show an 77
    a "W-Wait." with hpunch
    show an 78
    a "This is all happening so fast..." with dis
    a "I'm still not ready for anything... in there..."
    a "But I do believe I was promised cuddles...?"
    mc "*Chuckles* You know I’m not one to break my promises."
    play soundlow chair1
    show an 79 with dis12
    mc "*Kissing her neck* And don’t you worry. I’m perfectly fine with going as slow as you want." with dissolve
    mc "Better now? Without those pesky pants?"
    a "Y-Yeah... m-much better. You’re so warm..."
    mc "Do you mind if I move a bit? I want to feel all of you against me..."
    a "Y-Yes..."
    $ renpy.music.set_volume(0.23, channel='music2')
    show annierub5 with dis15
    a "Oh m-my god." with dissolve
    mc "Does that feel good for you too?"
    a "Y-Yes..."
    a "Oh [mc]..."
    mc "You’re... so wet..."
    mc "You like my dick gliding against you like that...?"
    a "Mm-hm..."
    mc "Agh... I need to go faster..."
    a "Please..."
    mc "You sure?"
    a "Yes..."
    show annierub3 with dis15
    a "AHH..." with dissolve
    a "OH MY..."
    a "Just like that... not too fast, I’m so sensitive right now..."
    mc "Oh Annie..."
    a "Mmmm..."
    mc "(Holy shit, this is really happening! I'm fucking Annie's thighs!)"
    mc "(She feels so amazing...)"
    a "(Ahh... the way he’s grinding against my... mmmm...)"
    a "(I never would’ve thought I’d have a chance with him...)"
    a "Aaaaahh..."
    mc "Jesus, Annie..."
    mc "The way you’re dripping all over my dick..."
    a "[mc]..." with dissolve
    a "You’re making me feel so... so good down there..."
    scene black with dis
    show annierub4 with dis
    mc "AAaaahhh..." with dis
    mc "Yeah..."
    mc "Just like that..."
    a "(Oh my god...)"
    a "(His...)"
    a "(...It's bigger than my arm!)"
    a "(How...)"
    a "(Is that what they’re supposed to look like?!)"
    a "(That thing is supposed to fit inside of me...?)"
    a "(All of it?!)"
    a "(There's no way on Earth I could take all of him.)"
    a "(...Right?)"
    scene black with dis
    play sound chair1
    show annierub2 with dis
    a "Aaaahhh..." with dis
    a "My god..."
    mc "Ahhh... I'm almost there..."
    a "(How can he feel so good? I’m just rubbing against it...)"
    a "(I wonder how he’d feel inside of me...)"
    a "(But no... fitting all that... that’d be impossible...)"
    a "(I'm too small, and he's just... too big...)"
    a "Mmmmhh..."
    mc "Oh Annie..."
    mc "I'm... I’m about to..."
    a "(Well, maybe with a bit of practice...)"
    mc "I’m cumming!!!"
    a "(Together we could...)"
    $ renpy.music.set_volume(0.26, channel='music2')
    play sound cum2
    play sound3 cum1
    scene an 80
    mc "AAaahhh!!" with hpunch
    a "W-What?"
    $ renpy.music.set_volume(0.30, channel='music2')
    play sound2 cum2
    play sound3 cum1
    scene an 80
    mc "Ohhhhhh!!" with hpunch
    show an 81
    a "Oh my god..." with dis15
    mc "Ahhhh...."
    mc "Oh shit, I'm sorry, Annie..."
    a "I..."
    a "Oh god, I gotta go!"
    mc "What?"
    $ renpy.music.set_volume(0.35, channel='music2')
    play sound chair2
    show an 82 with dis15
    mc "Did I do something wrong, Annie? I’m sorry! I didn’t know it was going to be that much!" with dissolve
    show an 83
    a "N-No! It wasn’t that!" with dis
    a "It was amazing!"
    a "B-But then..."
    $ renpy.music.set_volume(0.4, channel='music2')
    show annienervous with Dissolve(1.7)
    a "T-Then you start thinking, Y-Y-YOU KNOW?!" with dissolve
    a "*Nervous giggle*"
    a "L-Like... What j-just happened?!"
    a "AGH! I got carried away, like I ALWAYS DO!"
    a "I only came here t-to sleep and then... next thing I know I’m doing that..."
    a "I mean, I just stuck your... thing... in between my thighs... before I’ve even gotten my first k-kiss!!"
    a "*Nervous giggle*"
    mc "No, no! It's okay! You’re good! I like you, Annie! We can..."
    a "I started m-moving and then I c-couldn't stop and... now I’m not going to have my fairy tale ending... because what kind of Disney princess romance begins with a THIGH JOB?! AHAHAH!!"
    mc "Annie..."
    a "I was looking forward t-to this, b-but didn’t think it’d be like {i}this{/i}!"
    a "*Nervous laughter*"
    a "I mean..."
    mc "(She's not listening to me anymore...)"
    a "We skipped like 14 steps! In one night!"
    a "We didn't even kiss!"
    a "And w-why did it feel so good?"
    a "Why am I naked?"
    a "WHY DOES THIS THING TASTE SO SALTY?!" with hpunch
    a "What will [mc] think of me after all of this?!"
    mc "What? I'm right here! I’ll tell you right now what I think..."
    a "How am I supposed to look at everyone tomorrow?!"
    a "I..."
    a "THINK! I need to think!"
    a "Um..."
    scene an 90 with dissolve
    a "I'm gonna... go... think! Good night [mc]!"
    mc "Good—"
    play music2b rain3
    stop music2
    play soundlow doorslam
    show an 91 with hpunch
    pause .6
    mc "...night." with dis12
    stop music2
    $ renpy.music.set_volume(0.5, channel='music2')
    $ renpy.end_replay()

label ga_penny1:
    stop music fadeout 1
    stop musicb fadeout 1
    play music2 photoshot fadein 1
    stop music2b fadeout 1
    stop music3 fadeout 1
    show aaw 137 with dis
    p "You know... this whole thing got me thinking..." with dis
    p "And I realized, I've never had nude photos taken of me."
    p "Mainly because I haven’t had anyone that I was truly comfortable with."
    show aaw 138
    mc "*Gulps* Uh-huh..." with dissolve
    show aaw 137
    p "Maybe we could use our remaining 10 minutes to take a few topless photos." with dissolve
    p "I mean, they aren’t gonna be published anyways. I really just want to have some for my own private collection."
    show aaw 138
    mc "Makes sense..." with dissolve
    show aaw 137
    p "That Valentino guy made me realize that I'll never feel comfortable doing something like this with a stranger. But you’re no stranger, [mc], and since I have you here..."with dissolve
    show aaw 138
    mc "Umm..." with dissolve
    mc "Just to recap..."
    mc "Y-You want me to take some pictures of you while you’re... topless?"
    show aaw 139
    p "Well, I mean... If you're not comfortable with it, that's okay." with Dissolve(.8)
    p "Just thought that..."
    mc "N-NO! I mean, yes, sure, no problem!"
    mc "Let’s get those puppies out! Er, I mean—let me get that camera back out!"
    mc "Whatever you need!"
    show aaw 140
    p "Awesome!" with dis
    p "Thank you, [mc]."
    play sound clothes
    show aaw 141
    p "It's nice to have someone I can truly trust. I feel like I don’t have to be ashamed around you." with Dissolve(1.5)
    p "Aside from Philippe and Paul, everyone I've ever met in the fashion world has been a pervert or a freeloader."
    mc "I can imagine..."
    mc "(Oh my god, am I about to see Penelope naked?)"
    mc "(Thank you, Jesus.)"
    show aaw 142
    p "That sleazy guy is gone, right?" with dis
    mc "Y-Yeah, I made sure of it."
    mc "Don't worry, I'll warn you if I hear him coming."
    show aaw 143
    p "Alright then." with dis
    mc "(OH SWEET BABY JESUS. LOOK AT THOSE MAGNIFICENT BEAUTIES.)"
    p "Let's get to it!"
    mc "Y-Y-Yeah!"
    show aaw 144
    p "How should we do it?" with dis
    show aaw 145
    mc "D-Do it?"
    show aaw 144
    p "What pose?"
    show aaw 145
    mc "P-P-Pose?"
    show aaw 144
    p "Yeah, for the first set of pictures. How should I pose? You’re the expert here, aren’t you?"
    show aaw 145
    mc "Ah! Yeah, of course!"
    mc "(Come on, [mc], stay focused.)"
    mc "(I think all my blood is being directed to the wrong head...)"
    mc "I like how you posed before. We can try that one again..."
    show aaw 144
    p "Sure! Sounds good."
    play sound chain
    play sound2 chair4
    show aaw 146 with dis
    mc "Y-Yeah, this is a good angle." with dissolve
    mc "(You're seeing something that many men would pay a lot of money for, [mc].)"
    mc "(How the hell did I get so lucky?)"
    play sound camera
    show black
    pause 0.08
    hide black
    pause 0.3
    play sound camera
    show black
    pause 0.08
    hide black
    pause 0.08
    play sound2 camera
    show black
    pause 0.08
    hide black
    pause .5
    mc "(Man, her breasts are shaped so perfectly.)" with dissolve
    mc "(And that tiny waist of hers makes them seem even bigger.)"
    show aaw 147
    p "What about this one?" with dis
    show aaw 148
    mc "A-Also really nice."
    play sound camera
    show black
    pause 0.08
    hide black
    pause 0.08
    play sound3 camera
    show black
    pause 0.08
    hide black
    pause 0.08
    play sound2 camera
    show black
    pause 0.08
    hide black
    pause 0.2
    play sound2 camera
    show black
    pause 0.08
    hide black
    pause 0.5
    mc "Sexy as hell..." with dissolve
    show aaw 149
    p "Come on, you’ve been behind the camera for too long!" with dis
    mc "What??"
    p "Let's take a picture together!"
    mc "Not a chance."
    play sound chain
    play sound2 chair4
    show aaw 150
    p "Oh don’t be like that! It'll be fun!" with dis
    mc "No, it won't!"
    p "*Pulling your jersey off* Let’s get rid of this! We both need to be topless!"
    mc "No! I'm gonna look like a deformed potato next to you!"
    p "*Laughs* That's not true! You're very handsome!"
    mc "Oh please, Penny! I'm really not photogenic, don't make me do it!"
    p "Shhh, stop complaining and come sit down!"
    play sound chain
    play sound2 chair4
    show aaw 151
    mc ". . ." with Dissolve(.8)
    p "*Looking through the camera* You look great!"
    show aaw 152
    mc "Yeah, sure."
    show aaw 151
    p "Ok, let me set the timer..."
    p "Done! On my way!"
    play sound chain
    play sound2 chair4
    show aaw 153
    p "Alright, I set the timer for 15 seconds." with dis
    show aaw 154
    p "*Giggles* Isn't this fun?!" with dis
    mc "Y-Yeah, so much fun..."
    mc "(Oh no. Please no. Not now.)"
    mc "(Bad dick! No time for boner!)"
    show aaw 155
    mc "(Alright, just calm down [mc]. Stop overthinking things. We’re just making art!)" with dis
    mc "(Don’t think about Penelope's huge, perfect tits.)"
    mc "(Try not to notice how the cold breeze is stiffening her pink, perky nipples...)"
    mc "(Not gonna think about the cute, little freckles all over her curvy body...)"
    mc "(Or how her breasts are slightly paler than the rest of body... because she probably never sunbathes topless... meaning you’re likely the first man who’s gotten to see her breasts in who knows how long... and...)"
    play sound camera
    show black
    pause 0.08
    hide black
    pause
    p "Huh??" with dis
    show aaw 156
    p "Oh, come on, [mc]!"
    p "You're not even looking at the camera!"
    p "We have to do another one!"
    show aaw 157
    mc "I think that’s good enough, Penny. Valentino is gonna come back at any moment."
    p "I know, I know! That's why we gotta hurry!"
    p "Last one and we're done."
    p "15 seconds!"
    play sound chain
    play sound2 chair4
    show aaw 158
    mc ". . . !!!" with dis
    mc "(Oh shit.)"
    show aaw 159
    p "Am I centered? I can't tell." with dis
    play sound clothes
    show aaw 160 with Dissolve(1.5)
    mc "(Oh my fucking god...)" with dis
    mc "(My dick is rubbing up against her ass...)"
    show aaw 161
    p "Huh?" with dis
    show aaw 162
    p "(Oh my god.)" with dis
    p "(Is this...)"
    show aawp 1
    p "(Is this huge thing I’m feeling... his...)" with dis
    p "(His...)"
    show aawpv
    play sound5 whoosh3
    pause 1
    play sound musicstop
    play sound2 chain
    stop music2
    play music tictoc
    pause 2.1
    scene aawp 2 with Dissolve(.3)
    p ". . ." with dissolve
    mc ". . ."
    show aaw 164
    p "Uhm..." with dis12
    show aaw 163
    mc "(Oh god...)"
    mc "(Now I feel like that Valentino pervert...)"
    mc "Um..."
    show aaw 164
    p "I'm so sorry, I didn't..."
    show aaw 163
    mc "No! I'm the one who's sorry! I didn't mean to..."
    show aaw 164
    p "It's o-okay!"
    p "I mean, I should have known that was gonna happen."
    p "I got carried away."
    p "It's just, I'm not used to..."
    show aaw 163
    mc "No no... It's my fault. I..."
    show aaw 164
    p "I'm gonna go get dressed before Valentino comes back. I'll meet you by the entrance."
    show aaw 163
    mc "S-Sure!"
    stop music2
    $ renpy.end_replay()


label ga_dalia1:
    stop music fadeout 1
    stop musicb fadeout 1
    play music2 sneaky fadein 1
    stop music2b fadeout 1
    stop music3 fadeout 1
    scene db 21 with dis
    d "(That was a nice running session.)" with dis
    d "(There's still a few days left until Mr. Keating's test, so I can spend the rest of the today playing Eternum without feeling guilty!)"
    d "(But I'll take a shower first. Gotta get all this sweat off of me...)"
    show db 22
    d "(Dammit, why is there still no lock on this door?! I've asked Mom dozens of times.)" with Dissolve(.8)
    d "(I don't mind if she or Penny comes in while I'm indecent, or even Annie.)"
    d "(But [mc] lives here too now, so...)"
    d "(I better make sure he's not home. Don’t want him getting any free looks...)"
    show db 23
    d "[mc]!!" with dis
    show db 24
    d ". . ." with dissolve
    show db 23
    d "HELLO?! Is anybody home?" with dissolve
    show db 24
    d ". . ." with dissolve
    show db 25
    d "(Alright, seems like the coast is clear.)" with dis
    show db 26
    d "(My clothes are all drenched. I’m just gonna throw everything straight into the washer.)" with Dissolve(1.3)
    play sound clothes
    show db 27 with Dissolve(2.3)
    pause
    show db 28
    mc "(Oh shit, she took her top off...)"
    mc "(She must be getting changed...)"
    show db 29
    pause
    show db 30 with dis
    pause
    show db 31 with dis
    pause
    show db 33 with dis
    pause
    show db 34 with dis
    pause
    play sound clothes
    show db 35 with Dissolve(2.3)
    mc "(Damn...)" with dis
    play sound2 clothes
    show db 36 with Dissolve(2.3)
    mc "(Holy shit, look at that ass...)" with dis
    mc "(You can definitely tell she's been going to the gym.)"
    show db 37 with Dissolve(2)
    mc "(Wow, Dalia is smokin’...)" with dis
    show db 28
    mc "(Oh lord... is she going to take her underwear off too?)"
    show db 37
    mc "(Please God of Tits & Ass, if you exist and you're listening to me, hear my prayers and let me see those goods...)"
    show db 38 with dis
    mc "(Yes! YES!)" with dissolve
    d "*Unhooking her sports bra*"
    mc "(This is happening!)"
    play sound clip
    show daliav1 with dissolve
    pause .3
    hide daliav1
    show db 39
    with dissolve
    mc "(THERE IS A GOD.)" with dis
    play sound2 clothes
    show db 40 with Dissolve(2)
    mc "(Oh fuuuuck...)" with dissolve
    show db 41
    mc "(Sweet, sweet baby Jesus...)" with Dissolve(1.2)
    mc "(Look at those perfectly shaped breasts...)"
    mc "(Those little pink nipples...)"
    mc "(Those toned abs...)"
    mc "(Oh shit, full-on chub incoming...)"
    show db 42
    d "(Hmm... Looks like those deep squats are working. My booty is definitely getting bigger! Ass to grass, baby!)" with dis
    show db 43
    d "(And my abs are finally getting more visible too.)" with dis
    d "(Even though I eat like a horse.)"
    d "(Guess I can thank my fast metabolism for that.)"
    show db 44
    d "(Mmm, this is a nice feeling... getting a little more self-confidence and being comfortable with my body.)" with dis
    d "(That's why everyone should start exercising: to love who you see in the mirror and not worry whether other people like you.)"
    show db 45
    d "(Not that it's wrong to want people to like you.)" with Dissolve(1.3)
    play sound clothes
    show db 46
    d "(I’m not looking to attract the eyes of anyone special, anyways...)" with Dissolve(2)
    d "(I mean...)"
    show db 47
    d "(Y-Yeah, nobody. N-Not in that way.)" with Dissolve(1.2)
    d "(It’s not like I have the time for that, in any case.)"
    show db 48
    mc "(Oh my god.)" with Dissolve(1.5)
    mc "(Is this real life?)"
    show db 49 with Dissolve(1.4)
    mc "(Oh god, the things I'd do to her right now...)" with dis
    mc "(And that's... wrong! Bad [mc]! Get a hold of yourself.)"
    mc "(Man, being under the same roof as 4 other women is not going to be healthy for me.)"
    mc "(I need to get laid soon, or else I'm going to lose my mind...)"
    show daliav2 with dis
    pause 6
    hide daliav2
    show db 28
    with dis
    mc "(Oh my fucking god, her beautiful ass cheeks shake in such a mesmerizing rhythm... I’m getting hypnotized...)" with dissolve
    show db 48
    mc "(I feel like my dick is gonna explode...)" with dis
    mc "(This is too much...)"
    show db 49
    mc "(Can you leave already, Dalia?!)"with dis
    mc "(I need to get out of here! Or maybe... I could have a lil’ wank to relieve the tension.)"
    show db 50
    d "(I feel stronger than ever.)" with dis
    d "(No wonder I'm level 27 in Eternum.)"
    show db 51
    d "(Anyway, I think I’ve wasted enough time in here.)" with Dissolve(1.5)
    d "(Time to take that shower and get clean.)"
    mc "(Huh?)"
    mc "(She's... she's coming this way!)"
    show db 52
    mc "(OH SHIT!)" with hpunch
    mc "(She's gonna use the shower!)"
    show db 53
    mc "(Of course she's gonna use the shower, [mc]. She's getting naked in the bathroom, what else did you expect her to do, dumbass?!)" with dissolve
    show db 52
    mc "(Oh fuck, she's gonna think I was spying on her!)" with dissolve
    show db 53
    mc "(Because that's exactly what you were doing, idiot!)"with dissolve
    show db 52
    mc "(Oh no, now I'm completely fucked!)"with dissolve
    mc "(I have to do something!)"
    mc "(I need to get out of here...)"
    show db 54
    mc "(I have to disappear, to escape...)"with dissolve
    mc "(Must... teleport...)"
    mc "(Channel my inner powers...)"
    mc "(Summon the magic flowing around me...)"
    mc "(...focus... and...)"
    mc "(VANISH!!)" with hpunch
    stop music2 fadeout 1.5
    play sound risingshort
    show white with Dissolve(1.5)
    pause
    play music bathfan fadein 4
    hide white
    show db 55
    with Dissolve(3)
    pause
    show db 56 with dis
    pause
    show db 57
    pause 1
    mc "Aw shit..." with dis
    mc "I guess I can't teleport. Hmph."
    mc "Um..."
    show db 58
    mc "H-Hi Dalia!" with dis
    play sound punch
    show db 59
    d "WHAT THE FUCK ARE YOU DOING HERE?!" with hpunch
    mc "AAAargh..."
    stop music fadeout 1
    $ renpy.end_replay()

label ga_side1:
    stop music fadeout 1
    stop musicb fadeout 1
    play music2 sexy1 fadein 1
    stop music2b fadeout 1
    stop music3 fadeout 1
    show eva 9 with dis
    eva "I like you, [mc]. You have a very inquisitive mind and you aren’t afraid to ask questions." with dis
    eva "I like you a lot."
    eva "You know, I think you’re deserving of my most special massage..."
    eva "I'll convince you that this world can be real for you, too."
    eva "How does that sound?"
    play soundlow chair1
    show eva 10
    mc "Mm, good... you’ve got me curious."with dis
    eva "Have you ever done anything like this before?"
    show eva 11
    mc "N-Not really." with dis
    mc "And... I like you too, Eva. I appreciate that my conversation doesn’t fall on deaf ears. But I’ll be honest... I'm kinda nervous."
    show eva 10
    eva "There’s no need for that feeling here, baby." with dis
    eva "Let me help you relax and ease your mind..."
    play soundlow chair1
    show eva 12
    eva "But first... Do you mind if I get a little more... comfortable?" with dis
    eva "The neon lights on this dress make me a little too warm..."
    mc "Of course, go ahead..."
    eva "Thank you..."
    show eva 13 with dis
    pause
    play sound snap
    show eva 14
    eva "*Snaps fingers*"
    show eva 15 with Dissolve(1.6)
    mc "(Oh my god, she's driving me insane.)" with dissolve
    mc "(I'm so fucking hard...)"
    show eva 16 with dis
    pause
    play sound snap
    show eva 17
    eva "*Snaps fingers*"
    show eva 18 with Dissolve(1.6)
    mc "(Oh Jesus...)" with dissolve
    show eva 19 with Dissolve(1.3)
    eva "I might not know any spells for cleaning, but at least I know this bit of magic..." with dissolve
    eva "Much better now..."
    eva "Don't you think, [mc]?"
    mc "Y-Yeah... whatever makes you more... c-comfortable..."
    show eva 20
    eva "Miss Ambrose requires us to wear that dress. It’s really lovely and I like it a lot, but it does make us girls sweat after awhile..."
    mc "Yeah, I guess it can be a little..."
    show eva 21
    mc "A l-little..." with dis
    mc "Wow..."
    show eva 22
    mc "Damn, Eva..." with dis
    mc "Your body is... perfect..."
    eva "*Giggles*"
    show eva 23
    eva "Thank you..." with dis
    eva "I was hoping I’d be to your liking..."
    mc "You definitely are..."
    show eva 24
    eva "Then I guess you must be ready for some... further relaxation..." with dis
    mc "You bet I am..."
    show eva 26
    eva "Then let's not waste any more time." with dis
    eva "I'm sure there are a lot of things you’d like to do on your first day in Eternum."
    mc "Everything else can wait... right now you’ve got my full attention..."
    play soundlow chair1
    show eva 27
    eva "*Unzipping your zip* Now, that's the spirit, baby..." with dis
    eva "I always say that in Eternum, only the now is what matt–"
    play sound zip
    show eva 28 with Dissolve(1.5)
    eva "Wow..." with dis
    eva "My god, [mc]..."
    mc "What's the matter?"
    eva "It's... It's huge..."
    eva "I've never seen one so big..."
    mc "Oh..."
    mc "Is that a problem?"
    show eva 29
    eva "*Giggles* Maybe..." with Dissolve(1.3)
    eva "I don’t know what to do with all of you..."
    eva "But I think it’s a problem I’d love to solve..."
    show eva 30
    eva "Mmmm..." with dis
    mc "Oh god..."
    $ renpy.music.set_volume(0.42, channel='music2')
    eva "Your scent is captivating... [mc]."
    $ renpy.music.set_volume(0.35, channel='music2')
    show eva 31
    eva "Mmmmh..." with dis
    $ renpy.music.set_volume(0.28, channel='music2')
    mc "Oh yeah..."
    $ renpy.music.set_volume(0.21, channel='music2')
    show eva 32
    eva "MMMmmmmmhh..." with Dissolve(1.5)
    $ renpy.music.set_volume(0.15, channel='music2')
    play musicb blowjob1 fadein 1
    show eva0 with Dissolve(1.5)
    $ renpy.music.set_volume(0.08, channel='music2')
    pause
    mc "Ohhhh... FUCK..." with dis
    eva "MMmmmmMMmm..."
    mc "Oh my fucking god..."
    mc "Y-You feel amazing!"
    mc "Please, don't stop..."
    eva "Mmmm..."
    mc "Oh yeah..."
    mc "(I can feel her tongue...)"
    mc "(Gliding all over me...)"
    mc "(I love it...)"
    pause
    hide eva0
    show eva2
    with Dissolve(1.5)
    mc "Ohhhh... fuck..." with dissolve
    mc "Oh, fuck, Eva..."
    mc "I don't know about \"the other world\", but this feels incredible..."
    mc "Right here, right now..."
    eva "Mmmm..."
    mc "Oh yes..."
    pause
    mc "Oh shit, I'm about to cum..." with dissolve
    mc "I can't hold it..."
    stop musicb fadeout 1
    play soundlow chair1
    hide eva2
    show eva 33
    eva "*Gasping for air* Aaaahh..." with dis
    mc "Ohh..."
    eva "N-No..."
    eva "Don't cum just yet..."
    mc "What?"
    eva "I’m not done with you..."
    eva "I want to feel you... inside me..."
    play soundlow chair1
    show eva 34
    mc "WHAT?!" with dis
    mc "(OH SHIT, THIS IS REALLY HAPPENING!)"
    eva "I want..."
    eva "I need you to fuck me... please..."
    eva "I have to know how it feels to ride such a big cock..."
    mc "Yes..."
    show eva 35
    eva "I’m not supposed to be doing this..." with dis
    mc "Doing what?"
    show eva 36
    eva "*Removing her veil* Having sex. A blowjob is supposed to be our most intimate interaction with clients, and only on the most special occasions." with dis
    eva "This is... something personal."
    eva "And also strictly forbidden..."
    show eva 37
    eva "So please, don't tell Miss Ambrose..." with dis
    mc "My lips are sealed..."
    eva "Thank you, [mc]..."
    show eva 38 with Dissolve(1.5)
    pause
    play soundlow penetration
    show eva3 with dissolve
    pause 1.6
    hide eva3
    show eva 39
    with Dissolve(1.5)
    eva "Ahhhh..." with dissolve
    mc "Oh my god..."
    show eva4 with Dissolve(1.5)
    eva "AAAa-a-argh..." with dissolve
    eva "F-Fuck..."
    mc "Oh my god..."
    eva "It's so big..."
    mc "You're so fucking tight, Eva..."
    eva "Stretch it..."
    eva "Let me take all of you in, [mc]..."
    eva "Aaahh..."
    pause
    hide eva4
    show b
    with dissolve
    show eva5
    with Dissolve(1)
    eva "Aaahh..." with dissolve
    eva "F-Fuck..."
    eva "It feels so much better than I thought..."
    eva "I've never f-felt so full in all my life..."
    mc "Oh my god, Eva..."
    mc "This is amazing..."
    pause
    eva "Go faster..." with dis
    eva "I want to feel you deeper..."
    eva "Give it to me hard..."
    eva "D-DEEPER..."
    hide eva5
    show b
    with dissolve
    show eva6
    with Dissolve(1)
    eva "AAAARRGHH..." with dissolve
    eva "T-That's it!"
    eva "AaAaaahh..."
    eva "Yeah! J-Just like that!"
    eva "Oh my fucking god, keep going!"
    eva "Please... please... don't stop!"
    eva "Aaaahh... ahh... ahhhh..."
    eva "Keep going, baby..."
    pause
    hide eva6
    show b
    with dissolve
    show eva7
    with Dissolve(1)
    eva "AAAAAHHHH..." with dissolve
    mc "Oh my g-god..."
    mc "Your pussy feels incredible..."
    eva "I can’t get enough of you, baby..."
    eva "Aaahhh... "
    pause
    eva "Fuck, I'm about to finish... Give me every inch, [mc]!" with dissolve
    mc "Don't stop riding it..."
    hide eva7
    show b
    with dissolve
    show eva9
    with Dissolve(1)
    eva "Aaahhh... AAahhh... Ahhh..." with dis
    eva "Yeah... YEAH!"
    mc "AAAAH... Fuck..."
    mc "I... I can’t hold it..."
    eva "I think I’m gonna cum..."
    mc "Ahhh... Y-Your pussy is squeezing..."
    eva "Your cock is driving me insane..."
    eva "Aaaahhhhhh..."
    eva "I c-can't..."
    play sound cum1
    hide eva9
    show eva 39
    hide b
    eva "A-A-AAAARGHHH..." with hpunch
    play sound2 cum1
    eva "AAaahhh..." with hpunch
    eva "Oh my god..."
    mc "I'm about to cum too..."
    play sound fall2
    show eva 40
    eva "Come here, baby..." with dis
    eva "Cum on my face..."
    eva "Cover me with your seed..."
    mc "Ohh, fuck..."
    play sound cum2
    show eva 41
    mc "AAAARGH..." with hpunch
    play sound2 cum2
    mc "Ahhh... yeahhhh..." with hpunch
    show eva8 with Dissolve(1.5)
    eva "*Recovering her breath* Oh my fucking god..." with dis
    eva "That was... insane..."
    eva "How are you so good?"
    mc "Am I? I don't know, I didn't do anything special..."
    mc "I just let myself go."
    mc "I was trying to avoid cumming too early more than anything else."
    mc "Which was... not an easy thing to do, considering that you're unbelievably hot."
    mc "I'm sorry I made a mess of you."
    eva "No, no... I wanted it... it’s exactly what I needed..."
    stop music2
    $ renpy.music.set_volume(0.5, channel='music2')

    $ renpy.end_replay()
