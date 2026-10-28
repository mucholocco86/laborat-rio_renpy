init python:
    MC_Name = "D"  
    mc_nvl = Character(MC_Name, kind=nvl, image="nighten", callback=Phone_SendSound)
    global show_last_dialogue
    show_last_dialogue = False  



default persistent.seen_marniepartydance = False



label intro_1:

    stop music fadeout 2.0

    scene black
    with slowfade

    $ renpy.pause(3, hard=True)

    scene marniepartydance
    with ffast_dissolve

    call godson_locked_cutscene ("gui/marniepartydance.webm", 69.0, "seen_marniepartydance") from _call_godson_locked_cutscene



    scene black
    pause 2.0
    play music my_audio["partymusic"] loop
    $ renpy.pause(9.0, hard=True)
    scene a1
    with slowfade
    $ evil = True

    hen "So... it's true. You really have been cheating on me."
    mar "H-Henry...! Wait! I can explain.... I-I didn't know you were standing there."
    hen "Save it, Marnie! I saw everything. I saw enough."
    hen "After everything we've been through... after all these years together, this is how I find out?"

    scene a2
    with medium_dissolve

    hen "You know what hurts the most, Marnie? We opened our home to him. We trusted him."
    hen "I let him stay under our roof because I thought we were helping someone who needed us... and the whole time this was happening behind my back?"
    hen "How long has this been going on? How many times did you look me in the eyes and pretend everything was fine?"
    mar "Henry... please. I know how this looks, but just... please let me explain."

    scene a3
    with medium_dissolve

    mar "I know you're angry, and you have every right to be, but just listen to me for a moment."
    mar "I never wanted to hurt you. I wasn't trying to throw everything we have away... I just....made a mistake."
    hen "A mistake? Marnie, a mistake is forgetting something at the store. You don't accidentally end up with your tongue down another man's throat behind your husband's back!"
    hen "Look, we're not doing this out here in front of everyone. Let's go to the bedroom and talk about this privately."

    scene a4
    with medium_dissolve

    menu:
        mc ""
        "Why don't you let the lady dance with whoever she wants to dance with?":



            hen "This has nothing to do with you! Stay out of my marriage!"
            scene a5
            with medium_dissolve

            mar "Stop! Please, don't make this any worse than it already is!"
            mar "Just let me handle Henry. I don't need you fighting with him."

            menu:
                mc ""
                "Why should I? He's the one embarrassing you in front of everyone. Screw him!":



                    mar "Because he's my husband, and this is between us. You need to back off."
                    mar "Please... just give me a moment to speak with him."
                    pass
                "He doesn't get to tell you who you can dance with.":


                    mar "That isn't helping right now. You've already done more than enough."
                    mar "Just stop talking and let me deal with this before someone gets hurt."
                    pass
                "Forget him, Marnie. Come back and dance with me.":


                    mar "Are you serious? Henry just caught us, and you're asking me to keep dancing?"
                    mar "Stop pushing this. You're only making everything worse."
                    pass
        "Why are you even listening to this guy? Just let him go. Fuck him!":


            hen "You have a lot of nerve speaking to me like that while standing in MY home!"
            scene a5
            with medium_dissolve

            mar "Stop it! Don't speak to Henry like that!"
            mar "You've made your point, but this has gone far enough!"

            menu:
                mc ""
                "Why are you defending him after the way he's talking to you? Screw this guy!":



                    mar "Because whatever has happened between us, he is still my husband!"
                    mar "You don't get to stand there and tell me how I should speak to him!"
                    pass
                "I'm only saying what you're too afraid to say yourself!":


                    mar "You have no idea what I'm afraid to say!"
                    mar "Stay out of this and let me speak for myself!"
                    pass
                "You'd be better off without him, and you know it!":


                    mar "You don't know anything about our marriage!"
                    mar "Don't use what happened between us as an excuse to tear my life apart!"
                    pass
        "Hey, fuckface! Get the fuck out of here and let the woman have some fun!":



            hen "What the fuck did you just say to me!?"
            scene a5
            with medium_dissolve

            mar "Stop! Both of you, stop this right now!"
            mar "I am NOT letting this turn into a fight in the middle of the party!"

            menu:
                mc ""
                "What are you going to do, Henry? Hit me in front of your wife?":



                    mar "STOP! Don't provoke him. This isn't some game!"
                    mar "Back off and keep your mouth shut before this gets completely out of control."
                    pass
                "Come on. Show everyone what kind of man you really are, bitch!":


                    mar "Enough! I won't stand here while you deliberately try to humiliate him!"
                    mar "Whatever you think this is, you need to stop now!"
                    pass
                "Marnie clearly doesn't want you anymore. Take the hint and leave.":


                    mar "[playerName], don't you dare speak for me!"
                    mar "You don't get to decide what I want, and you certainly don't get to dismiss my husband for me!"
                    pass



    scene a6
    with medium_dissolve

    mar "Okay, Henry. Let's go talk."
    mar "This is all just a complete misunderstanding, I promise you."
    mar "Let's just talk in the bedroom, like you asked."
    hen "...."
    hen "Fine."

    scene a7
    with medium_dissolve

    mc "........."
    mc "............."

    scene a8_1
    with medium_dissolve

    voice my_audio["1"]
    nar "Look at him, walking away like he actually won something. Like dragging her into another room somehow changes what just happened. (volume for Narration is in the game settings.)"
    voice my_audio["2"]
    nar "The way she looked at you, the way she kissed you... do you really think Henry can erase that with a few angry words?"
    voice my_audio["3"]
    nar "That poor bastard still thinks this is his perfect little marriage. He has no idea the cracks were already there long before tonight."

    scene a8
    with medium_dissolve

    voice my_audio["4"]
    nar "You close your eyes, letting the frustration sink deeper. Not because you accept defeat... but because you understand patience."
    voice my_audio["5"]
    nar "Let Henry have his moment. Let him pretend he's still the man in control. Everyone deserves one final comforting lie."
    voice my_audio["6"]
    nar "You'll deal with this later. For now, find your friends, Myles and Sun. Something tells you this night still has a few surprises left."

    jump mylesz


label mylesz:

    scene black
    with slowfade

    pause 2.0

    scene a10
    with slowfade

    voice my_audio["198"]
    tan "DID YOU GO TO THE FUCKIN' PARTY!? Yo' BITCH ass was supposed to call the electric company before they closed!"
    voice my_audio["199"]
    tan "Mama just opened the mail, and now she's running through the house talking about they're gonna cut the damn lights off!"
    my "What? I could've sworn I handled that shit yesterday...."
    voice my_audio["200"]
    tan "Well, clearly, you didn't, because I'm standing here looking at a bright red shutoff notice with your name written all over this bullshit!"
    voice my_audio["201"]
    tan "And don't start acting confused now! Daddy told you about it three days ago, Mama reminded you this morning, and I texted you twice!"
    voice my_audio["202"]
    tan "But somehow, yo' STUPID ass had enough time to run off to a damn party!"
    scene a11
    with medium_dissolve
    my "First of all, lower your fuckin' voice. I said I handled it, so I must've paid the wrong balance or something."
    my "Second, don't come at me like I'm the only grown person living in that damn house!"

    scene a12
    with medium_dissolve

    voice my_audio["203"]
    tan "Oh, here you go with that shit. Ain't nobody saying you're the only grown person in the house."
    voice my_audio["204"]
    tan "I'm saying everybody trusted you to do one fucking thing, and now Mama's panicking, Daddy's pretending he can't hear her, and the refrigerator is full of groceries."
    voice my_audio["205"]
    tan "So, when the lights go out and all that food spoils, are you gonna magically fix that shit too!?"

    scene a13
    with medium_dissolve

    voice my_audio["206"]
    tan "Because I'm sick of this whole family waiting until something catches fire, then calling you like you're the goddamn emergency hotline!"
    voice my_audio["207"]
    tan "And I'm even more sick of yo ass acting like we're bothering you whenever the mess finally lands in your lap!"
    voice my_audio["208"]
    tan "You wanted to be Mister Fix-Everything, so congratulations, nigga. Something needs fixing."

    scene a14
    with medium_dissolve

    my "Man, listen, I'm at a fuckin' party! I'm not about to stand in the middle of somebody's house arguing with yo' ugly ass over a light bill!"
    my "I'll call them in the morning, figure out what happened, and handle it like I handle every other got' damn thing around there!"
    voice my_audio["209"]
    tan "Tomorrow morning? They're talking about shutting it off tonight, DUMBASS!"
    voice my_audio["210"]
    tan "But, sure, keep partying. Maybe the DJ can come over and power the house when everything goes dark!"

    scene a15
    with medium_dissolve

    my "You know what? Since everybody in that house suddenly knows so damn much, one of y'all can pick up the phone and deal with it!"
    my "I'm tired of being the mechanic, the plumber, the bill collector, the therapist, and the only motherfucka' anybody calls when something goes wrong!"
    my "I'll handle it when I get home! Until then, stop blowing up my phone with this bullshit!"
    voice my_audio["211"]
    tan "WHAT THE FUCK YOU MEAN DON..."

    scene a16
    with medium_dissolve

    menu:
        mc ""
        "Family trouble?":



            my "Man, you heard all that shit?"
            my "Yeah, bro. Same bullshit, different day."
            my "Every time something goes wrong in that house, I'm the first motherfucker they call."

            scene a17
            with medium_dissolve

            my "I swear, sometimes I feel like I got three grown-ass children waiting for me at home."
            my "My pops ignores every problem until it gets too big to ignore, my moms panics over everything, and Tania starts screaming before anybody even knows what happened."
            my "Then they all turn around and expect me to drop whatever I'm doing and save the fucking day."

            menu:
                mc ""
                "How did you end up being responsible for everything?":



                    scene a18
                    with medium_dissolve

                    my "It started with little shit. Paying a bill online, fixing a leaking pipe, filling out some paperwork for my pops."
                    my "Then everybody figured out I was the one who could actually get shit done."
                    my "Next thing I knew, every problem in that house had my fucking name written on it."

                    menu:
                        mc ""
                        "So they basically punished you for being dependable.":



                            scene a19
                            with medium_dissolve

                            my "That's exactly what happened."
                            my "At first, everybody appreciates you. Then they get comfortable, and appreciation turns into expectation."
                            my "Now, if I don't immediately fix something, they act like I'm the one who caused the damn problem."

                            menu:
                                mc ""
                                "You need to stop helping them for a while.":



                                    scene a20
                                    with medium_dissolve

                                    my "I've tried, bro. I really have."
                                    my "But the second I step back, my moms starts stressing herself sick, Tania starts fighting with everybody, and my pops disappears into another room."
                                    my "Then I feel like an asshole because I know I could've handled the whole thing in ten minutes."

                                    scene a21
                                    with medium_dissolve

                                    my "That's how they keep pulling me back in."
                                    my "They don't even have to ask anymore. All they gotta do is let the house start falling apart and wait for my conscience to kick in."
                                    my "Sometimes I wonder whether they need me, or whether I've just made them believe they can't survive without me."
                                "Let them blame you. That doesn't make it your responsibility.":


                                    scene a20
                                    with medium_dissolve

                                    my "I know that, but knowing something and actually living by it are two different things."
                                    my "I've spent years being the person everybody leans on. The minute I move, the whole family starts wobbling."
                                    my "It's hard to walk away when you already know exactly who's gonna hit the ground first."

                                    scene a21
                                    with medium_dissolve

                                    my "Maybe I need to let them fall once."
                                    my "Not because I want anybody to suffer, but because they need to learn how to stand without grabbing onto me."
                                    my "Otherwise, I'm gonna wake up one day and realize I spent my whole life carrying people who never learned how to walk."
                                "Fuck it. Change your number and let them figure it out.":


                                    scene a20
                                    with medium_dissolve

                                    my "Man, don't tempt me."
                                    my "Sometimes I picture throwing this phone in a lake, packing a bag, and disappearing before anybody notices."
                                    my "Just one whole week where nobody knows how to reach me or ask me for shit."

                                    scene a21
                                    with medium_dissolve

                                    my "But I'd probably spend the whole trip wondering whether the house burned down without me."
                                    my "That's the fucked-up part. Even when they're not around, they're still in my head."
                                    my "I need to figure out how to leave without feeling like I'm abandoning everybody."
                        "Do they ever thank you for any of that shit?":


                            scene a19
                            with medium_dissolve

                            my "Sometimes, but it's always after the fact."
                            my "They'll thank me when the bill gets paid or the sink stops leaking, then call me five minutes later with something else."
                            my "It's like every thank-you comes with another assignment attached to it."

                            menu:
                                mc ""
                                "Then their thanks doesn't mean much.":



                                    scene a20
                                    with medium_dissolve

                                    my "That's how it feels."
                                    my "I don't need anybody kissing my ass, but damn, at least let me enjoy solving one problem before you throw another one at me."
                                    my "Sometimes I don't even think they see me as a person. I'm just the solution standing in the room."

                                    scene a21
                                    with medium_dissolve

                                    my "Maybe that's why I came out tonight."
                                    my "I needed to be somewhere nobody was asking me to repair, pay for, or explain some shit."
                                    my "For a couple hours, I just wanted to be Myles instead of everybody's emergency contact."
                                "You should start charging their asses.":


                                    scene a20
                                    with medium_dissolve

                                    my "Shit, I'd be rich by now."
                                    my "Plumbing fees, mechanic fees, counseling fees, late-night emergency fees. I could retire before thirty."
                                    my "Tania would still complain about the bill, though."

                                    scene a21
                                    with medium_dissolve

                                    my "Jokes aside, maybe I do make things too easy for them."
                                    my "They never have to think about what my time is worth because I've always given it away for free."
                                    my "That might be the first thing I need to change."
                                "Maybe they appreciate you more than they know how to say.":


                                    scene a20
                                    with medium_dissolve

                                    my "Maybe. My family ain't exactly good at sitting down and talking about feelings."
                                    my "My moms worries, my pops gets quiet, and Tania insults you when she's trying to say she cares."
                                    my "I know they love me. They just have a fucked-up way of showing it."

                                    scene a21
                                    with medium_dissolve

                                    my "But love can't be the excuse for everything."
                                    my "At some point, they gotta understand that I get tired too."
                                    my "I can love them without letting every one of their problems become mine."
                        "Why didn't your parents teach everybody to handle their own shit?":


                            scene a19
                            with medium_dissolve

                            my "Because my parents barely know how to handle their own shit."
                            my "My pops grew up believing the answer to every problem was to stay quiet until it disappeared."
                            my "My moms grew up in a family where everybody got involved in everything, so she expects the whole house to move whenever one person has a problem."

                            menu:
                                mc ""
                                "Sounds like you became the parent in that house.":



                                    scene a20
                                    with medium_dissolve

                                    my "Some days, that's exactly what it feels like."
                                    my "I'm the one reminding people about appointments, making sure bills get paid, and stopping arguments before somebody says something they can't take back."
                                    my "Meanwhile, I'm supposed to somehow build my own life on whatever time is left over."

                                    scene a21
                                    with medium_dissolve

                                    my "I love my family, but I don't wanna raise the people who raised me."
                                    my "That shouldn't be my job."
                                    my "I need to start setting some boundaries before I forget I'm allowed to have a life of my own."
                                "Your father needs to step the fuck up.":


                                    scene a20
                                    with medium_dissolve

                                    my "I've told him that before."
                                    my "He always says he's tired, he's worked his whole life, and he doesn't wanna deal with everybody's drama."
                                    my "Like I don't get tired. Like I don't have my own shit I'm trying to do."

                                    scene a21
                                    with medium_dissolve

                                    my "That's probably what pisses me off the most."
                                    my "He gets to decide he's finished, and somehow that means everything becomes my responsibility."
                                    my "I respect my pops, but I'm not gonna spend the rest of my life finishing everything he walks away from."
                                "And your mother needs to stop panicking and start thinking.":


                                    scene a20
                                    with medium_dissolve

                                    my "My moms can't help that shit. The second something goes wrong, her mind jumps straight to the worst possible outcome."
                                    my "A late bill turns into homelessness. A strange noise in the car turns into the engine exploding."
                                    my "Then she calls me already halfway into a breakdown."

                                    scene a21
                                    with medium_dissolve

                                    my "I don't blame her for being scared."
                                    my "I just wish she understood that every time she puts that fear on me, I gotta carry it too."
                                    my "After a while, a man starts getting tired of holding everybody else's anxiety."
                "Why don't you just move out?":


                    scene a18
                    with medium_dissolve

                    my "You think I haven't tried?"
                    my "I've saved money, looked at apartments, and even filled out applications."
                    my "But every time I get close, some new emergency comes along and eats everything I've saved."

                    menu:
                        mc ""
                        "What kind of emergencies?":



                            scene a19
                            with medium_dissolve

                            my "The car breaks down, the water heater dies, my moms needs something, or Tania gets behind on one of her bills."
                            my "It's never one huge disaster. It's a hundred smaller problems that keep reaching into my pockets."
                            my "By the time everybody's okay again, I'm back at the starting line."

                            menu:
                                mc ""
                                "Stop giving them your moving money.":



                                    scene a20
                                    with medium_dissolve

                                    my "I know that's what I should do."
                                    my "But it's hard to sit on money while somebody you love is standing in front of you saying they need help."
                                    my "Especially when you know nobody else in the house can cover it."

                                    scene a21
                                    with medium_dissolve

                                    my "Still, you're right."
                                    my "If I keep treating every family emergency like it's more important than my future, I'm never gonna have one."
                                    my "Next time I save enough, that money needs to stay mine."
                                "They'll keep having emergencies as long as you keep paying for them.":


                                    scene a20
                                    with medium_dissolve

                                    my "That's what I'm starting to realize."
                                    my "Nobody prepares for shit because they already know I'll find a way to cover it."
                                    my "They don't need a backup plan. Apparently, I'm the backup plan."

                                    scene a21
                                    with medium_dissolve

                                    my "Maybe the only way they'll learn is if I stop catching them."
                                    my "Not forever, but long enough for them to feel the consequences of never planning ahead."
                                    my "I can't keep sacrificing every opportunity I get just to make sure they're comfortable."
                                "Sounds like they don't want you to leave.":


                                    scene a20
                                    with medium_dissolve

                                    my "Sometimes I wonder about that."
                                    my "Nobody directly tells me not to go, but whenever I talk about moving, everybody suddenly remembers ten things they need me for."
                                    my "My moms gets quiet, my pops changes the subject, and Tania starts joking about taking my room."

                                    scene a21
                                    with medium_dissolve

                                    my "Maybe they're scared of what happens when I'm gone."
                                    my "But that's their fear to deal with. It can't become my prison."
                                    my "Sooner or later, they're gonna have to learn how that house works without me standing in the middle of it."
                        "How much money have they cost you?":


                            scene a19
                            with medium_dissolve

                            my "I stopped counting because it was starting to piss me off."
                            my "A few hundred here, another thousand there, then something else breaks before I recover."
                            my "I've probably paid enough into that house to own part of the motherfucker."

                            menu:
                                mc ""
                                "Then make them pay you back.":



                                    scene a20
                                    with medium_dissolve

                                    my "I've asked before."
                                    my "Everybody agrees, tells me they'll handle it, then another month passes and somehow nobody remembers the conversation."
                                    my "I could write that shit down and put it on the refrigerator, and they'd still act surprised."

                                    scene a21
                                    with medium_dissolve

                                    my "Maybe I need to stop lending money and start saying no."
                                    my "A debt nobody intends to repay isn't a loan. It's just me giving away another piece of my future."
                                    my "I'm done doing that shit without thinking."
                                "You've been financing their lives while delaying your own.":


                                    scene a20
                                    with medium_dissolve

                                    my "Damn."
                                    my "I never really thought about it like that, but yeah."
                                    my "Every time I help them move forward, I push myself another step back."

                                    scene a21
                                    with medium_dissolve

                                    my "That's gotta stop."
                                    my "I don't want to resent my family, but that's exactly where this road is headed."
                                    my "I need to start investing in myself before there's nothing left of me to invest."
                                "You should've bought yourself something instead.":


                                    scene a20
                                    with medium_dissolve

                                    my "Man, I don't even remember the last big thing I bought just because I wanted it."
                                    my "Everything I make already has somewhere else to go before it even reaches my account."
                                    my "Bills, repairs, groceries, somebody needing help, then whatever's left disappears."

                                    scene a21
                                    with medium_dissolve

                                    my "Maybe that's why tonight matters more than it should."
                                    my "This party is probably the first thing I've done for myself in weeks."
                                    my "And even here, they still found a way to drag me back into that house."
                        "So what's actually stopping you from leaving now?":


                            scene a19
                            with medium_dissolve

                            my "Guilt, mostly."
                            my "I keep imagining my moms struggling, my pops pretending everything's fine, and Tania trying to do everything by herself."
                            my "I know leaving doesn't mean I don't love them, but it still feels that way."

                            menu:
                                mc ""
                                "That's not guilt. That's conditioning.":



                                    scene a20
                                    with medium_dissolve

                                    my "Maybe it is."
                                    my "They've needed me for so long that being needed started feeling like proof that I mattered."
                                    my "Now, the idea of not being there makes me feel useless."

                                    scene a21
                                    with medium_dissolve

                                    my "That's probably something I need to unlearn."
                                    my "My value can't just come from how many problems I solve for other people."
                                    my "I need to believe I'm worth something even when nobody's asking me for help."
                                "Leave anyway. They'll adjust.":


                                    scene a20
                                    with medium_dissolve

                                    my "They'd have to."
                                    my "Maybe it'd be ugly for a while, but people usually learn when they don't have another choice."
                                    my "As long as I'm there, they'll never have a reason to change."

                                    scene a21
                                    with medium_dissolve

                                    my "Yeah, bro. I think I already know what I need to do."
                                    my "I just keep waiting for leaving to stop feeling wrong."
                                    my "Maybe it never will. Maybe I need to do it while it still feels wrong."
                                "You can move out without disappearing from their lives.":


                                    scene a20
                                    with medium_dissolve

                                    my "That's true."
                                    my "I could still help sometimes without living in the middle of every crisis."
                                    my "Maybe having my own space would make it easier to decide what actually needs me and what doesn't."

                                    scene a21
                                    with medium_dissolve

                                    my "That's probably the balance I've been missing."
                                    my "I don't have to abandon my family, but I also don't have to sacrifice myself for them."
                                    my "I can love them from an apartment with a locked door and my phone on silent."
                "What does your sister actually do around the house?":


                    scene a18
                    with medium_dissolve

                    my "Tania does more than it sounds like, honestly."
                    my "She cooks, helps my moms, keeps track of groceries, and handles a lot of the little shit nobody notices."
                    my "Her problem is that she doesn't know how to ask for help without sounding like she's threatening somebody."

                    menu:
                        mc ""
                        "She always talks to you like that?":



                            scene a19
                            with medium_dissolve

                            my "Since we were kids."
                            my "Tania could ask you to pass the salt and make it sound like she's about to slap the shit out of you."
                            my "That's just her voice when she's irritated, which is most of the fucking time."

                            menu:
                                mc ""
                                "I would've hung up sooner.":



                                    scene a20
                                    with medium_dissolve

                                    my "Usually, I let her finish because underneath all that yelling, there might actually be something important."
                                    my "But tonight, I wasn't standing here listening to a whole speech about a bill I already thought I paid."
                                    my "She's lucky I answered at all."

                                    scene a21
                                    with medium_dissolve

                                    my "I'll call her back when I cool off."
                                    my "She'll still be mad, I'll still be irritated, and somehow we'll figure the shit out."
                                    my "That's basically how our relationship works."
                                "You let her get away with too much.":


                                    scene a20
                                    with medium_dissolve

                                    my "Probably."
                                    my "But if I come at her too hard, the argument turns into World War Three, and my moms starts crying because we're fighting."
                                    my "Sometimes letting Tania run her mouth is easier than dealing with the aftermath."

                                    scene a21
                                    with medium_dissolve

                                    my "Still, she needs to learn where the line is."
                                    my "Being my sister doesn't mean she gets to talk to me any kind of way."
                                    my "Next time, I'm ending the conversation before she gets halfway through her first insult."
                                "Sounds like that's how she shows she cares.":


                                    scene a20
                                    with medium_dissolve

                                    my "That's exactly what it is."
                                    my "She gets scared, then the fear comes out sounding like anger."
                                    my "She ain't calling because she hates me. She's calling because she trusts me more than anybody else."

                                    scene a21
                                    with medium_dissolve

                                    my "I just wish trust didn't always sound like somebody cussing me out."
                                    my "But that's Tania."
                                    my "Loud, disrespectful, and probably the first person who'd show up if I ever really needed her."
                        "Does she help you, or just yell while you fix everything?":


                            scene a19
                            with medium_dissolve

                            my "She helps."
                            my "She might complain the entire time, but she'll be right beside me holding the flashlight or making phone calls."
                            my "Out of everybody in that house, she's probably the closest thing I have to backup."

                            menu:
                                mc ""
                                "Then maybe you two should work together more.":



                                    scene a20
                                    with medium_dissolve

                                    my "We've talked about it."
                                    my "The problem is, both of us think we're the one who knows what needs to happen."
                                    my "So, instead of working together, we spend half the time arguing about whose plan makes more sense."

                                    scene a21
                                    with medium_dissolve

                                    my "Still, you're right."
                                    my "If I could get her to stop yelling long enough to listen, we could probably take half the weight off each other."
                                    my "Maybe I need to treat her more like a partner and less like another problem to manage."
                                "So she isn't the real problem.":


                                    scene a20
                                    with medium_dissolve

                                    my "Nah, not really."
                                    my "She's just the loudest part of a much bigger problem."
                                    my "Tania's the one who calls because everybody else already dumped the situation on her."

                                    scene a21
                                    with medium_dissolve

                                    my "I probably shouldn't have gone off on her like that."
                                    my "She's frustrated for the same reason I am."
                                    my "We're both tired of being the only two people in that house who notice when shit needs to get done."
                                "Backup shouldn't call you a bitch-ass motherfucker.":


                                    scene a20
                                    with medium_dissolve

                                    my "Man, that's just how we talk."
                                    my "I call her worse than that when she pisses me off."
                                    my "Five minutes later, one of us is asking the other what they want from the store."

                                    scene a21
                                    with medium_dissolve

                                    my "We're good, bro."
                                    my "That argument sounded worse than it was."
                                    my "By tomorrow, she'll be stealing food off my plate and acting like none of this ever happened."
                        "You two sound exactly alike.":


                            scene a19
                            with medium_dissolve

                            my "Don't ever tell her that."
                            my "She'll spend the next three hours explaining why she's smarter, better-looking, and somehow more mature than me."
                            my "But yeah... we probably get that shit from our moms."

                            menu:
                                mc ""
                                "No wonder you two argue so much.":



                                    scene a20
                                    with medium_dissolve

                                    my "Exactly."
                                    my "We're both stubborn, loud when we're mad, and convinced we're the only person in the room making sense."
                                    my "It's like arguing with a shorter, meaner version of myself."

                                    scene a21
                                    with medium_dissolve

                                    my "But that's probably why we understand each other too."
                                    my "Tania knows exactly what gets under my skin because the same shit gets under hers."
                                    my "We fight hard, but we look out for each other even harder."
                                "She sounds fun. You should introduce us.":


                                    scene a20
                                    with medium_dissolve

                                    my "Hell no."
                                    my "The last thing I need is you and Tania in the same room encouraging each other's bullshit."
                                    my "She'd either hate you immediately or decide you're her new favorite person. There ain't no middle."

                                    scene a21
                                    with medium_dissolve

                                    my "Maybe one day, but not tonight."
                                    my "I already got enough family drama without bringing one of my boys into it."
                                    my "Trust me, you're safer enjoying Tania from a distance."
                                "At least you aren't dealing with all of it alone.":


                                    scene a20
                                    with medium_dissolve

                                    my "That's true."
                                    my "As much as she gets on my nerves, I don't know what I'd do if she wasn't there."
                                    my "She catches a lot of shit before it ever reaches me."

                                    scene a21
                                    with medium_dissolve

                                    my "Maybe I need to remember that before I start treating her like she's part of the problem."
                                    my "She's tired too."
                                    my "We might both be carrying the same family from opposite ends."
        "Sounds like somebody's having a rough night.":



            my "Man, you don't know the half of it."
            my "I leave the house for a few hours, and suddenly everybody forgets how to function."
            my "I swear they wait until I'm gone before they start discovering problems."

            scene a17
            with medium_dissolve

            my "That house can go three straight days without anybody saying shit to me."
            my "But the minute I put on decent clothes, step outside, and try to enjoy myself, the phone starts ringing."
            my "It's like they can smell me having a good time."

            menu:
                mc ""
                "What was that argument even about?":



                    scene a18
                    with medium_dissolve

                    my "The electric bill."
                    my "I thought I paid it yesterday, but apparently there's still some balance sitting there."
                    my "Now everybody's acting like the whole damn power grid is about to collapse because of me."

                    menu:
                        mc ""
                        "Did you actually forget to pay it?":



                            scene a19
                            with medium_dissolve

                            my "I don't think so."
                            my "I remember logging in, seeing the balance, and entering the payment information."
                            my "Maybe the payment didn't go through, or I paid the old balance instead of the new one."

                            menu:
                                mc ""
                                "Then Tania might have a reason to be pissed.":



                                    scene a20
                                    with medium_dissolve

                                    my "She has a reason to be worried. That doesn't mean she gets to call me screaming like I did the shit on purpose."
                                    my "I'm allowed to make one mistake without everybody acting like the family is doomed."
                                    my "Especially after all the mistakes I've fixed for them."

                                    scene a21
                                    with medium_dissolve

                                    my "I'll handle it when I get home."
                                    my "But they're gonna start learning how to speak to me before I solve anything else."
                                    my "Being useful doesn't mean I have to accept being disrespected."
                                "Maybe the company fucked something up.":


                                    scene a20
                                    with medium_dissolve

                                    my "That's what I'm thinking."
                                    my "Those companies will take your money, lose the record, then charge you a fee for asking where it went."
                                    my "But nobody at home wants to hear that. They already decided I'm guilty."

                                    scene a21
                                    with medium_dissolve

                                    my "I'll pull up the confirmation when I get back."
                                    my "And when I prove I paid that shit, Tania better apologize with the same energy she used to cuss me out."
                                    my "I might even make her put it in writing."
                                "Either way, it can wait until tomorrow.":


                                    scene a20
                                    with medium_dissolve

                                    my "That's what I said."
                                    my "The lights are still on, the company is closed, and nobody's solving shit tonight."
                                    my "All that yelling is just everybody stressing themselves out for no reason."

                                    scene a21
                                    with medium_dissolve

                                    my "I'm done letting their panic become my emergency."
                                    my "If something can't be handled until morning, then it waits until morning."
                                    my "Tonight, I'm at a party, and I'm trying to remember what having a life feels like."
                        "Why is the bill your responsibility in the first place?":


                            scene a19
                            with medium_dissolve

                            my "Because I'm the one who set up the online account."
                            my "My pops hates doing anything on a computer, my moms gets confused by all the passwords, and Tania refuses to keep track of due dates."
                            my "So, naturally, the whole thing became my job."

                            menu:
                                mc ""
                                "Give Tania the password and make it her problem.":



                                    scene a20
                                    with medium_dissolve

                                    my "I tried that once."
                                    my "She changed the password, forgot what she changed it to, and somehow locked everybody out of the account."
                                    my "Guess who had to call customer service and fix that shit."

                                    scene a21
                                    with medium_dissolve

                                    my "Still, I might give her another chance."
                                    my "She's older now, and I'm more tired."
                                    my "One of those things has to make her responsible eventually."
                                "Your father should be paying his own damn bill.":


                                    scene a20
                                    with medium_dissolve

                                    my "He does pay it. I just handle the actual payment."
                                    my "He'll hand me the money or transfer it, then act like the rest is some mysterious technical process only I understand."
                                    my "The man can rebuild half a car, but a website scares the shit out of him."

                                    scene a21
                                    with medium_dissolve

                                    my "Maybe I need to stop making excuses for him."
                                    my "He learned how to use every other thing he wanted to use."
                                    my "He can learn how to click 'pay now' without me holding his hand."
                                "You made yourself too useful.":


                                    scene a20
                                    with medium_dissolve

                                    my "That's the story of my fucking life."
                                    my "I help somebody once, and suddenly I've volunteered for a permanent position."
                                    my "Nobody even remembers how the job became mine."

                                    scene a21
                                    with medium_dissolve

                                    my "I need to start being selectively incompetent."
                                    my "Maybe if I fuck up a few easy things, everybody will stop acting like I'm the household superhero."
                                    my "Either that, or they'll finally learn how to save themselves."
                        "They called you at a party over a light bill?":


                            scene a19
                            with medium_dissolve

                            my "Exactly."
                            my "The lights are still on. Nobody is sitting in darkness. Nothing is on fire."
                            my "But Tania called me like the police were outside with a battering ram."

                            menu:
                                mc ""
                                "Your family sounds dramatic as hell.":



                                    scene a20
                                    with medium_dissolve

                                    my "Bro, dramatic doesn't even cover it."
                                    my "My moms can turn a late payment into a family meeting, and Tania treats every inconvenience like somebody declared war."
                                    my "My pops just disappears until everybody gets tired."

                                    scene a21
                                    with medium_dissolve

                                    my "And I'm always the idiot standing in the middle trying to calm everybody down."
                                    my "Maybe tonight, they can be dramatic without an audience."
                                    my "I'm keeping my phone in my pocket for the rest of this party."
                                "You should've told them the lights look fine from here.":


                                    scene a20
                                    with medium_dissolve

                                    my "Man, I should've."
                                    my "Then Tania would've called me an asshole, my moms would've called asking why I upset my sister, and my pops would've texted one word: 'Problem?'"
                                    my "That man sends texts like every letter costs money."

                                    scene a21
                                    with medium_dissolve

                                    my "See, now I'm getting mad all over again."
                                    my "I'm done talking about those motherfuckers for a minute."
                                    my "I came here to drink, have fun, and mind somebody else's business for once."
                                "Maybe they just wanted an excuse to ruin your night.":


                                    scene a20
                                    with medium_dissolve

                                    my "Sometimes it feels like that."
                                    my "Not because they're malicious, but because they can't stand the idea of handling something while I'm enjoying myself."
                                    my "If they're stressed, everybody has to be stressed."

                                    scene a21
                                    with medium_dissolve

                                    my "I gotta stop letting that shit work."
                                    my "Their bad night doesn't automatically have to become mine."
                                    my "Whatever's happening at home will still be there when I decide to deal with it."
                "Why does your family rely on you so much?":


                    scene a18
                    with medium_dissolve

                    my "Because I usually come through."
                    my "That's really all it takes. You solve enough problems, and people stop developing their own solutions."
                    my "Eventually, they don't even try. They just call you."

                    menu:
                        mc ""
                        "Doesn't it feel good knowing they need you?":



                            scene a19
                            with medium_dissolve

                            my "Sometimes."
                            my "I'm not gonna lie. There's a part of me that likes knowing I'm the person everybody trusts."
                            my "But being needed stops feeling good when nobody cares whether you're exhausted."

                            menu:
                                mc ""
                                "Maybe that's why you never really say no.":



                                    scene a20
                                    with medium_dissolve

                                    my "Probably."
                                    my "Saying yes makes me feel useful. Saying no makes me feel like I'm letting everybody down."
                                    my "Even when I know they're asking too much, I still want to be the person who can handle it."

                                    scene a21
                                    with medium_dissolve

                                    my "That's not healthy, is it?"
                                    my "I need to stop confusing being loved with being useful."
                                    my "If they only value me when I'm fixing something, then we've got a much bigger problem than a light bill."
                                "They need you, but do they know you need them too?":


                                    scene a20
                                    with medium_dissolve

                                    my "I don't know."
                                    my "I don't really ask anybody for much. By the time I need help, I'm already halfway through solving the problem myself."
                                    my "Maybe they assume I don't need anything because I never let them see me struggle."

                                    scene a21
                                    with medium_dissolve

                                    my "That's partly on me."
                                    my "I can't expect people to support me if I keep pretending I don't need support."
                                    my "Maybe I need to start giving them a chance to show up for me."
                                "Being needed isn't the same thing as being respected.":


                                    scene a20
                                    with medium_dissolve

                                    my "Yeah, that's the part that stings."
                                    my "They trust me to solve everything, but they don't always respect my time, plans, or boundaries."
                                    my "It's like my ability matters more than I do."

                                    scene a21
                                    with medium_dissolve

                                    my "I need both."
                                    my "I want to help my family, but I also want them to see the person doing the helping."
                                    my "Otherwise, I'm just another appliance in that house, useful until I finally break."
                        "What happens when you need help?":


                            scene a19
                            with medium_dissolve

                            my "I usually figure it out myself."
                            my "My family would help if I asked, but asking them means explaining everything three times and listening to ten different opinions."
                            my "Most of the time, doing it alone is easier."

                            menu:
                                mc ""
                                "So you don't trust them the way they trust you.":



                                    scene a20
                                    with medium_dissolve

                                    my "Damn. I guess I don't."
                                    my "Not because they're bad people, but because I know helping me would turn into another situation I'd have to manage."
                                    my "Even when I'm the one who needs support, I'd still end up directing everybody."

                                    scene a21
                                    with medium_dissolve

                                    my "That's probably why I'm so tired."
                                    my "There is no version of my life where I get to stop being in charge."
                                    my "I need people around me who can carry something without asking me how to hold it."
                                "Maybe you should ask anyway.":


                                    scene a20
                                    with medium_dissolve

                                    my "Maybe."
                                    my "They can't learn how to support me if I never give them anything to do."
                                    my "I might be keeping the whole cycle alive by refusing to let anybody help."

                                    scene a21
                                    with medium_dissolve

                                    my "Next time something comes up, maybe I'll make Tania handle it."
                                    my "She'll complain, insult me, and probably do it wrong the first time."
                                    my "But at least I won't automatically take everything on myself."
                                "Fuck that. Keep handling your own business.":


                                    scene a20
                                    with medium_dissolve

                                    my "That's been working so far."
                                    my "Well... working might be a strong word."
                                    my "I'm surviving, but I don't know if constantly being exhausted counts as having your shit together."

                                    scene a21
                                    with medium_dissolve

                                    my "Maybe independence ain't supposed to mean doing everything alone."
                                    my "I can handle my own business without refusing every hand somebody offers."
                                    my "I just need better hands around me."
                        "They rely on you because you allow it.":


                            scene a19
                            with medium_dissolve

                            my "I know."
                            my "That's the answer nobody likes hearing, but it's true."
                            my "They couldn't keep putting everything on me if I stopped accepting it."

                            menu:
                                mc ""
                                "Then stop complaining and change it.":



                                    scene a20
                                    with medium_dissolve

                                    my "Damn, bro. Straight for the throat."
                                    my "But you're right. Complaining at a party isn't gonna change what happens when I walk back into that house."
                                    my "I need to actually start saying no."

                                    scene a21
                                    with medium_dissolve

                                    my "Not threatening to say it. Not thinking about saying it."
                                    my "I need to look somebody in the face, say no, and survive whatever guilt trip comes afterward."
                                    my "That's probably the only way any of this changes."
                                "Set boundaries before they take everything you have.":


                                    scene a20
                                    with medium_dissolve

                                    my "That's what I'm afraid of."
                                    my "I keep giving them time, money, and energy like I have an unlimited supply."
                                    my "One day, I'm gonna reach for something for myself and realize there's nothing left."

                                    scene a21
                                    with medium_dissolve

                                    my "I can't let it get that far."
                                    my "Helping them should be a choice, not the default setting of my entire life."
                                    my "I'm gonna start making them ask instead of assuming."
                                "Or accept that this is just your role in the family.":


                                    scene a20
                                    with medium_dissolve

                                    my "Hell no."
                                    my "I might be the dependable one, but that doesn't mean I agreed to become everybody's permanent caretaker."
                                    my "A role can change when the person playing it gets tired."

                                    scene a21
                                    with medium_dissolve

                                    my "Maybe that's what I needed to hear."
                                    my "This shit isn't written in stone."
                                    my "I became this person over time, which means I can become somebody else."
                "Do you ever get a break from any of them?":


                    scene a18
                    with medium_dissolve

                    my "Not a real one."
                    my "Even when nobody calls, I'm still waiting for the phone to ring."
                    my "That's the worst part. The problems don't even have to be happening for me to feel responsible for them."

                    menu:
                        mc ""
                        "Turn the phone off.":



                            scene a19
                            with medium_dissolve

                            my "I've thought about it."
                            my "But then I start imagining some real emergency happening while I'm unreachable."
                            my "My brain starts creating disasters before I even touch the power button."

                            menu:
                                mc ""
                                "You're letting fear control your life.":



                                    scene a20
                                    with medium_dissolve

                                    my "Yeah."
                                    my "I keep telling myself I'm staying available because I'm responsible."
                                    my "But maybe I'm really just scared of what could happen if I'm not there."

                                    scene a21
                                    with medium_dissolve

                                    my "I can't prevent every bad thing."
                                    my "And being reachable every second doesn't mean I'll always be able to fix it."
                                    my "Maybe the first real break I take starts with accepting that."
                                "Give them another number for emergencies.":


                                    scene a20
                                    with medium_dissolve

                                    my "Whose number? Yours?"
                                    my "Nah, I'm playing, but that might actually work."
                                    my "I could tell them to call Tania first and only call me if something is genuinely serious."

                                    scene a21
                                    with medium_dissolve

                                    my "They'd abuse it for the first week."
                                    my "But eventually, they'd learn that a missing remote isn't an emergency."
                                    my "I need to stop being available for every level of bullshit."
                                "A real emergency will still exist when you turn it back on.":


                                    scene a20
                                    with medium_dissolve

                                    my "That's true."
                                    my "Most emergencies aren't actually emergencies. They're just problems everybody wants solved immediately."
                                    my "The house probably won't explode because I ignored my phone for two hours."

                                    scene a21
                                    with medium_dissolve

                                    my "You know what? I'm putting this shit on silent."
                                    my "If somebody calls again, they're waiting until I'm ready."
                                    my "Tonight, they can save themselves."
                        "Take a trip without them.":


                            scene a19
                            with medium_dissolve

                            my "I've always wanted to do that."
                            my "Just get in the car, pick a direction, and not tell anybody where I'm going until I'm already there."
                            my "Somewhere quiet, with no family group chat and no damn bills."

                            menu:
                                mc ""
                                "Then do it. Stop waiting for permission.":



                                    scene a20
                                    with medium_dissolve

                                    my "You're right."
                                    my "Nobody's gonna walk into my room and hand me a permission slip to live my own life."
                                    my "If I keep waiting until the family doesn't need me, I'll never leave the driveway."

                                    scene a21
                                    with medium_dissolve

                                    my "I'm gonna plan something."
                                    my "Even if it's only a weekend, I'm going somewhere and turning this phone off."
                                    my "They'll either survive or learn something."
                                "Bring me. I'll make sure you ignore their calls.":


                                    scene a20
                                    with medium_dissolve

                                    my "Man, you'd probably answer just to talk shit to them."
                                    my "Actually, that might be exactly what I need."
                                    my "Somebody standing there reminding me that every ringing phone doesn't require a response."

                                    scene a21
                                    with medium_dissolve

                                    my "All right, then."
                                    my "One of these weekends, we're getting the fuck out of town."
                                    my "And if my family calls, your disrespectful ass is handling customer service."
                                "You'll spend the whole trip worrying about them.":


                                    scene a20
                                    with medium_dissolve

                                    my "Probably, at first."
                                    my "I'd check my phone every five minutes and imagine the house falling apart."
                                    my "But maybe after a day or two, I'd finally understand that the world keeps moving without me."

                                    scene a21
                                    with medium_dissolve

                                    my "That's something I need to see with my own eyes."
                                    my "Not just for them. For me."
                                    my "I need proof that taking care of myself doesn't automatically destroy everybody else."
                        "Maybe this party is your break.":


                            scene a19
                            with medium_dissolve

                            my "It was supposed to be."
                            my "Good music, free drinks, and a few hours where nobody asks me to crawl under a sink."
                            my "Then Tania's loud ass found me."

                            menu:
                                mc ""
                                "Then forget the call and enjoy yourself.":



                                    scene a20
                                    with medium_dissolve

                                    my "That's exactly what I'm about to do."
                                    my "The bill will still exist tomorrow, and everybody at home will still be dramatic."
                                    my "But this party only happens tonight."

                                    scene a21
                                    with medium_dissolve

                                    my "Fuck it."
                                    my "I'm done talking about my family."
                                    my "Let's find Sun, get a drink, and see what other kind of trouble is happening around here."
                                "You aren't very good at relaxing.":


                                    scene a20
                                    with medium_dissolve

                                    my "No shit."
                                    my "Even when I'm sitting down, my brain is standing up making a list."
                                    my "I don't think I know how to relax without feeling like I'm forgetting something."

                                    scene a21
                                    with medium_dissolve

                                    my "Maybe I need practice."
                                    my "So, for the rest of tonight, I'm not fixing anything."
                                    my "If somebody has a problem, they better find a different motherfucker."
                                "You came here to escape, not to have fun.":


                                    scene a20
                                    with medium_dissolve

                                    my "Damn."
                                    my "Maybe you're right. I wasn't looking forward to the party as much as I was looking forward to not being home."
                                    my "That's probably not a good sign."

                                    scene a21
                                    with medium_dissolve

                                    my "I need more in my life than places to hide from my family."
                                    my "I need something that's actually mine."
                                    my "Maybe tonight is when I start figuring out what that looks like."
        "She sounds Black and Hispanic, a dangerous combination. Your sister always talks to you like that?":



            my "That's Tania."
            my "She doesn't know how to start a conversation unless the first word is an insult."
            my "But if somebody outside the family talked to me like that, she'd be the first one ready to fight."

            scene a17
            with medium_dissolve

            my "She's loud, disrespectful, stubborn, and probably the only person in that house who understands why I'm so damn tired."
            my "We argue because both of us are stuck cleaning up after everybody else."
            my "The difference is, she screams about it while I keep pretending I can handle everything."

            menu:
                mc ""
                "Sounds like you and Tania are carrying the whole family.":



                    scene a18
                    with medium_dissolve

                    my "Pretty much."
                    my "She handles my moms, the food, and most of the day-to-day stuff."
                    my "I handle the bills, repairs, paperwork, and anything that requires talking to somebody without cussing them out."

                    menu:
                        mc ""
                        "Then why were you two fighting each other?":



                            scene a19
                            with medium_dissolve

                            my "Because we're both tired."
                            my "When people are carrying too much, they don't always yell at the person who caused the problem."
                            my "Sometimes they yell at the only other person still standing there."

                            menu:
                                mc ""
                                "You should apologize to her.":



                                    scene a20
                                    with medium_dissolve

                                    my "Yeah, I probably should."
                                    my "She came at me wrong, but I know she was stressed."
                                    my "And hanging up on her isn't gonna make the bill disappear."

                                    scene a21
                                    with medium_dissolve

                                    my "I'll call her later."
                                    my "Not right now, though. I need at least one drink before I willingly step back into that argument."
                                    my "Then we'll figure it out like we always do."
                                "She should apologize first.":


                                    scene a20
                                    with medium_dissolve

                                    my "She won't."
                                    my "Tania could be standing over your body holding the murder weapon and still ask why you made her do it."
                                    my "Apologies aren't exactly her strongest skill."

                                    scene a21
                                    with medium_dissolve

                                    my "But I know her."
                                    my "She'll call later, act like nothing happened, and ask whether I want food."
                                    my "That's basically her version of saying sorry."
                                "Both of you need to stop doing everything for everybody else.":


                                    scene a20
                                    with medium_dissolve

                                    my "That's the real answer."
                                    my "As long as Tania and I keep catching every problem, nobody else has a reason to change."
                                    my "We're tired because we keep protecting everybody from the consequences of being irresponsible."

                                    scene a21
                                    with medium_dissolve

                                    my "Maybe we need to make a deal."
                                    my "Split what actually needs doing, refuse everything else, and let the grown people in that house grow the fuck up."
                                    my "It won't be peaceful, but at least it might finally be fair."
                        "Which one of you does more?":


                            scene a19
                            with medium_dissolve

                            my "Depends on the day."
                            my "Tania probably does more inside the house. I handle more of the stuff that costs money or requires leaving."
                            my "Neither of us wins, because we're both doing too damn much."

                            menu:
                                mc ""
                                "Sounds like she deserves more credit.":



                                    scene a20
                                    with medium_dissolve

                                    my "She does."
                                    my "I get so irritated by how she talks that sometimes I forget how much shit she's actually handling."
                                    my "My moms would probably lose her mind without Tania there every day."

                                    scene a21
                                    with medium_dissolve

                                    my "I should tell her that."
                                    my "Not tonight, because she'd never let me live it down."
                                    my "But eventually, I should let her know I see what she does."
                                "You both deserve a break.":


                                    scene a20
                                    with medium_dissolve

                                    my "No argument there."
                                    my "Tania needs to go somewhere she can't hear my moms calling her name, and I need somewhere without cell service."
                                    my "Maybe we should send our parents on a vacation and stay home in peace."

                                    scene a21
                                    with medium_dissolve

                                    my "Actually, knowing them, they'd call us from the vacation."
                                    my "Still, something has to change."
                                    my "Neither of us can keep living like we're on duty every hour of the day."
                                "You should leave and let Tania deal with it.":


                                    scene a20
                                    with medium_dissolve

                                    my "I couldn't do that to her."
                                    my "As much as I want out, leaving every problem on Tania would make me just as selfish as everybody else."
                                    my "She'd tell me to go, but I know what it would cost her."

                                    scene a21
                                    with medium_dissolve

                                    my "If I leave, I need to help her build a way out too."
                                    my "Maybe not at the same time, but she deserves a life beyond that house just as much as I do."
                                    my "We both need an exit plan."
                        "Why don't you two split the responsibilities properly?":


                            scene a19
                            with medium_dissolve

                            my "We try."
                            my "Then something comes up that doesn't fit neatly into anybody's category, and we both end up dealing with it."
                            my "Our family has a talent for creating problems that require every department."

                            menu:
                                mc ""
                                "Make a list and force everybody to choose a job.":



                                    scene a20
                                    with medium_dissolve

                                    my "You know what? That isn't a bad idea."
                                    my "Put every bill, chore, and responsibility on paper, then make everybody claim something."
                                    my "No more pretending they didn't know."

                                    scene a21
                                    with medium_dissolve

                                    my "They'll complain like hell."
                                    my "But maybe seeing everything written down will finally show them how much Tania and I are doing."
                                    my "At the very least, it'll make the next argument more organized."
                                "Your parents aren't children. Stop assigning them chores.":


                                    scene a20
                                    with medium_dissolve

                                    my "Exactly."
                                    my "The fact that we even need a system is ridiculous."
                                    my "These are grown people who somehow became less responsible because Tania and I became more responsible."

                                    scene a21
                                    with medium_dissolve

                                    my "Maybe a list isn't the answer."
                                    my "Maybe the answer is simply refusing to do things that never belonged to us."
                                    my "They'll remember how to be adults once nobody else volunteers."
                                "Move out together and leave your parents there.":


                                    scene a20
                                    with medium_dissolve

                                    my "Me and Tania sharing an apartment?"
                                    my "We'd either become the most organized household in the city or kill each other before the first rent payment."
                                    my "There would be no peaceful middle ground."

                                    scene a21
                                    with medium_dissolve

                                    my "Still, it might be easier than living at home."
                                    my "At least our problems would be ours."
                                    my "No parents, no surprise bills, and nobody pretending they can't hear the smoke detector."
                "Your sister sounds like the only one willing to challenge you.":


                    scene a18
                    with medium_dissolve

                    my "She is."
                    my "Everybody else lets me take over because it makes their lives easier."
                    my "Tania's the only one who'll tell me when she thinks I'm wrong, even if she says it in the most disrespectful way possible."

                    menu:
                        mc ""
                        "Do you think she was right tonight?":



                            scene a19
                            with medium_dissolve

                            my "About the bill needing to be handled? Yeah."
                            my "About calling me and immediately acting like I intentionally fucked everybody over? Hell no."
                            my "She was right about the problem and wrong about how she came at me."

                            menu:
                                mc ""
                                "Then tell her that when you call back.":



                                    scene a20
                                    with medium_dissolve

                                    my "I will."
                                    my "I'm not apologizing for being at a party, but I can admit I should've double-checked the payment."
                                    my "And she can admit that screaming doesn't make a problem easier to solve."

                                    scene a21
                                    with medium_dissolve

                                    my "That's probably the most mature way to handle it."
                                    my "Which means Tania will hate every second of the conversation."
                                    my "But she'll listen eventually."
                                "Who cares how she said it if she was right?":


                                    scene a20
                                    with medium_dissolve

                                    my "I care."
                                    my "Being right doesn't give somebody permission to disrespect you."
                                    my "Especially when you've spent years cleaning up their mistakes without making them feel like shit."

                                    scene a21
                                    with medium_dissolve

                                    my "I'll fix the bill."
                                    my "But I'm also gonna make it clear that I'm not the family's punching bag."
                                    my "They can need me without treating me like I owe them everything."
                                "You probably needed somebody to call you out.":


                                    scene a20
                                    with medium_dissolve

                                    my "Maybe."
                                    my "I get so used to being the competent one that I don't always take it well when somebody points out I dropped something."
                                    my "Tania knows exactly how to hit that nerve."

                                    scene a21
                                    with medium_dissolve

                                    my "I can own the mistake without accepting all the extra bullshit."
                                    my "That's probably the balance."
                                    my "Fix what I did wrong, then make everybody else own their part too."
                        "Does she ever stop you from taking on too much?":


                            scene a19
                            with medium_dissolve

                            my "Sometimes."
                            my "She'll tell me to let something go, then turn around and call me the next day because she took it on instead."
                            my "We're both terrible at following our own advice."

                            menu:
                                mc ""
                                "You two are enabling each other.":



                                    scene a20
                                    with medium_dissolve

                                    my "Damn, you're probably right."
                                    my "Every time one of us tries to step back, the other steps forward and catches the problem."
                                    my "So, nothing ever actually changes."

                                    scene a21
                                    with medium_dissolve

                                    my "We need to stop rescuing each other from setting boundaries."
                                    my "If Tania says no, I can't quietly do it for her, and she can't do that shit to me."
                                    my "Otherwise, we're just keeping the same broken system alive."
                                "At least somebody notices you're doing too much.":


                                    scene a20
                                    with medium_dissolve

                                    my "Yeah."
                                    my "Tania sees it because she's right there doing too much beside me."
                                    my "Everybody else just sees the results and assumes we aren't struggling."

                                    scene a21
                                    with medium_dissolve

                                    my "That's probably why we fight so hard."
                                    my "We know exactly what the other person is carrying."
                                    my "Sometimes anger is easier than admitting we're both scared the family will collapse if we stop."
                                "Maybe you should listen to her more often.":


                                    scene a20
                                    with medium_dissolve

                                    my "Don't let her hear you say that."
                                    my "She already thinks she's the smartest person in every room."
                                    my "One outside vote of confidence and she'll become unbearable."

                                    scene a21
                                    with medium_dissolve

                                    my "But yeah, I should probably listen sometimes."
                                    my "Under all the yelling, Tania usually has a point."
                                    my "I just wish she delivered those points without trying to verbally stab me."
                        "You respect her, don't you?":


                            scene a19
                            with medium_dissolve

                            my "Of course I do."
                            my "She drives me fucking crazy, but she's strong as hell."
                            my "She takes care of everybody and still finds enough energy to argue with me for an hour."

                            menu:
                                mc ""
                                "You should tell her that.":



                                    scene a20
                                    with medium_dissolve

                                    my "She'd laugh in my face."
                                    my "Then she'd ask what I broke or how much money I needed."
                                    my "We don't really do serious emotional speeches."

                                    scene a21
                                    with medium_dissolve

                                    my "Still, maybe I should say it once."
                                    my "Not some dramatic bullshit. Just let her know I see her."
                                    my "Everybody deserves to hear that sometimes."
                                "Sounds like you're proud of her.":


                                    scene a20
                                    with medium_dissolve

                                    my "I am."
                                    my "She could've left all this shit on me, but she didn't."
                                    my "No matter how much she complains, she's always there."

                                    scene a21
                                    with medium_dissolve

                                    my "That's my little sister."
                                    my "I can call her every name in the book, but nobody else better try it."
                                    my "She earned my respect a long time ago."
                                "Then stop acting like she's another burden.":


                                    scene a20
                                    with medium_dissolve

                                    my "That's fair."
                                    my "Sometimes I lump her in with everybody else because she's the one calling me."
                                    my "But most of the time, she's calling because she's already been dealing with the problem alone."

                                    scene a21
                                    with medium_dissolve

                                    my "I need to remember who's actually standing beside me."
                                    my "Tania isn't the burden."
                                    my "She's the other person carrying it."
                "So what do you actually want for yourself?":


                    scene a18
                    with medium_dissolve

                    my "Peace."
                    my "A place where nothing breaks unless I broke it, and nobody needs money unless it's me."
                    my "A whole day where the only decisions I make are about what I want."

                    menu:
                        mc ""
                        "What would your own place look like?":



                            scene a19
                            with medium_dissolve

                            my "Clean, quiet, and far enough away that nobody can walk over unannounced."
                            my "A decent television, a couch nobody else has ruined, and a refrigerator that doesn't mysteriously empty overnight."
                            my "Nothing fancy. Just mine."

                            menu:
                                mc ""
                                "That sounds easy enough to get.":



                                    scene a20
                                    with medium_dissolve

                                    my "It should be."
                                    my "But somehow, the simplest things feel impossible when everybody else's needs keep getting placed ahead of yours."
                                    my "I keep telling myself I'll do it after the next problem is solved."

                                    scene a21
                                    with medium_dissolve

                                    my "There will always be another problem."
                                    my "Maybe that's what I needed to accept."
                                    my "If I want my own life, I'm gonna have to build it while the family is still calling."
                                "You'd get lonely.":


                                    scene a20
                                    with medium_dissolve

                                    my "Maybe."
                                    my "But I'd rather be lonely in a quiet apartment than surrounded by people who only call my name when something goes wrong."
                                    my "Besides, lonely doesn't have to mean alone forever."

                                    scene a21
                                    with medium_dissolve

                                    my "I could invite people over because I wanted them there."
                                    my "Then, when I was tired, I could close the door."
                                    my "That kind of control sounds pretty damn good right now."
                                "Tania would be at your place every day.":


                                    scene a20
                                    with medium_dissolve

                                    my "She'd have a key before I finished unpacking."
                                    my "I'd come home and find her eating my food, wearing my clothes, and complaining about how I decorated."
                                    my "So much for peace."

                                    scene a21
                                    with medium_dissolve

                                    my "But honestly, I probably wouldn't mind."
                                    my "I don't need to escape Tania completely."
                                    my "I just need a door I can lock when she starts getting on my nerves."
                        "What would you do if nobody needed you for a month?":


                            scene a19
                            with medium_dissolve

                            my "I don't even know."
                            my "That's how long it's been since I thought about what I wanted without checking how it affected everybody else."
                            my "I'd probably sleep for the first week."

                            menu:
                                mc ""
                                "Then spend the second week doing something reckless.":



                                    scene a20
                                    with medium_dissolve

                                    my "Now you're speaking my language."
                                    my "Get out of town, spend some money on myself, and ignore every responsible thought in my head."
                                    my "Nothing too stupid, but definitely something Tania would yell about."

                                    scene a21
                                    with medium_dissolve

                                    my "Maybe I don't need a whole month."
                                    my "Maybe I just need to start taking pieces of my life back whenever I can."
                                    my "Tonight can be the first piece."
                                "That's sad, bro. You don't even know what you want.":


                                    scene a20
                                    with medium_dissolve

                                    my "Yeah."
                                    my "I've gotten so good at being useful to everybody else that I never built anything for myself."
                                    my "Take away the family problems, and I'm not sure what's left."

                                    scene a21
                                    with medium_dissolve

                                    my "But maybe that's not sad. Maybe it's an open space."
                                    my "I can decide what goes there."
                                    my "For once, I can build something that isn't meant to save anybody."
                                "You'd probably start missing the chaos.":


                                    scene a20
                                    with medium_dissolve

                                    my "I hate to admit it, but maybe."
                                    my "When you've lived in chaos long enough, quiet starts feeling suspicious."
                                    my "I'd probably wake up wondering what I forgot."

                                    scene a21
                                    with medium_dissolve

                                    my "That's something else I'd have to learn."
                                    my "Peace isn't the warning before another problem."
                                    my "Sometimes peace is just peace."
                        "Why haven't you gone after any of that yet?":


                            scene a19
                            with medium_dissolve

                            my "Because wanting something for myself always feels selfish."
                            my "The minute I think about spending money, moving out, or taking a trip, I remember somebody at home needs something."
                            my "Then I put myself back at the bottom of the list."

                            menu:
                                mc ""
                                "Being selfish might be exactly what you need.":



                                    scene a20
                                    with medium_dissolve

                                    my "Maybe in small doses."
                                    my "Not the kind where I stop caring about everybody."
                                    my "Just enough selfishness to remember that I'm one of the people I'm supposed to care about."

                                    scene a21
                                    with medium_dissolve

                                    my "Yeah."
                                    my "I can help my family without disappearing inside their problems."
                                    my "From now on, Myles gets a place on the list too."
                                "Nobody is ever going to put you first except you.":


                                    scene a20
                                    with medium_dissolve

                                    my "That's hard to hear, but it's true."
                                    my "Everybody else is focused on surviving their own life."
                                    my "I can't sit around waiting for them to notice I've been neglecting mine."

                                    scene a21
                                    with medium_dissolve

                                    my "I have to choose myself."
                                    my "Not every time, but enough that I actually start moving forward."
                                    my "Otherwise, I'll be having this same conversation ten years from now."
                                "Maybe you enjoy having an excuse not to chase what you want.":


                                    scene a20
                                    with medium_dissolve

                                    my "Damn, bro."
                                    my "You think I'm hiding behind my family?"
                                    my "Maybe part of me is. If I'm always busy fixing their lives, I never have to risk failing at my own."

                                    scene a21
                                    with medium_dissolve

                                    my "That's a fucked-up thought."
                                    my "But maybe I needed it."
                                    my "I can't keep blaming them for every step I'm afraid to take."

    jump after1

label after1:

    scene a22
    with medium_dissolve

    sun "Guys! There you are! I've been looking all over for you two!"
    sun "Come outside with me for a second! I have an idea that's about to take MILF Hunters to the next level!"

    scene a23
    with medium_dissolve

    sun "I'm serious! I think I found our next perfect candidate!"
    sun "I'm talking EXACTLY what we've been looking for! This might be the best one yet!"
    my "Bro, what the fuck are you talking about?"
    my "You disappear for half the party and come back acting like you discovered gold or something."

    scene a24
    with medium_dissolve

    sun "That's because maybe I did. You guys just need to trust the vision."
    my "Okay, but who is it? You can't just walk over here hyping this up and not tell us anything."
    sun "Relax, relax. All great things require patience."
    sun "When you guys hear what I found out, you're gonna understand why I wanted to tell you in private."

    scene a25
    with medium_dissolve

    sun "A true mastermind never reveals everything too early."
    sun "You gotta let the suspense build. That's what separates regular ideas from legendary ones."
    sun "Now come on, let's go outside before somebody ruins the moment."

    play sound my_audio["bang sound 4"] noloop
    scene a26
    with hpunch

    hen "You son of a bitch! Tell me the truth! Did you sleep with my wife?!"
    rob "Henry! Stop! Let him go! This isn't how you handle this!"
    hen "Answer me! You knew she was married and you still went after her!"

    play sound my_audio["bang sound 4"] noloop
    scene a27
    with hpunch

    voice my_audio["7"]
    nar "W-What the FUCK!?"
    voice my_audio["8"]
    nar "Tell him to get his FUCKING hands off of you. RIGHT. NOW!"

    menu:
        "THE FUCK!? Get your fucking hands off me! I don't know what you're talking about!":




            hen "Don't play stupid with me!"
            hen "She practically admitted it! I saw the look on her face!"
            rob "Henry, calm down! Screaming at him isn't going to fix anything!"
            hen "No, Robert! I want to hear him say it!"

            menu:
                mc ""
                "FUCK YOU! GET THE FUCK OFF ME!":



                    hen "You arrogant little bastard!"
                    hen "You really think this is some kind of joke, don't you!?"
                    rob "Henry, enough! You're letting your anger control you!"
                    rob "Look at me! Are you going to calm down now!?"
                    pass
                "You better back up before I MAKE you back up!":


                    hen "You think threatening me is smart right now!?"
                    hen "You come into my home, disrespect me, and now you want to act tough!?"
                    rob "Both of you stop! This isn't helping anything!"
                    rob "Henry, breathe! Are you calm now!?"
                    pass
                "Maybe you should worry about why she wanted someone else around!":


                    hen "You really have no shame, do you!?"
                    hen "After everything you've done, you're still standing here running your mouth!"
                    rob "Henry, don't let him bait you! Walk away from this!"
                    rob "Are you going to be calm!?"
                    pass
        "Maybe you should ask your wife instead of grabbing me like a psycho!":


            hen "I already talked to her!"
            hen "I know something happened! I can see it all over both of your faces!"
            rob "Henry, listen to yourself! You're losing control!"
            hen "I trusted you around my family you son of a bitch!"

            menu:
                mc ""
                "Sounds like you and Marnie have problems that started before me! GET THE FUCK OFF ME!":



                    hen "Don't you dare try to turn this around!"
                    hen "You knew exactly what you were doing!"
                    rob "Henry, enough! Let him go!"
                    rob "Are you finished!? Are you calm!?"
                    pass
                "You're embarrassing yourself right now! FUCK ARE YOU DOING!?":


                    hen "No. What's embarrassing is finding out everyone else knew before I did!"
                    hen "Standing there wondering how long I've been lied to!"
                    rob "I get it, but this isn't the answer!"
                    rob "Calm down! Are you good!?"
                    pass
                "GET...THE...FUCK...OF ME, NOW! BEFORE I BREAK YOUR ARM!":


                    hen "After everything that happened, you're threatening ME!?"
                    rob "Enough! Both of you!"
                    rob "Henry.....HENRY!"
                    pass
        "Back the fuck up before I slap the shit out of you!":


            hen "There it is! That's who you really are!"
            hen "Walking around pretending to be innocent when you know EXACTLY what happened!"
            rob "Henry, come on! Step away from him!"
            hen "He needs to admit it!"

            menu:
                mc ""
                "I don't need to admit anything to you!":



                    hen "Because you don't care who you hurt!"
                    hen "That's the difference between you and me!"
                    rob "Henry, that's enough!"
                    rob "Are you going to calm down!?"
                    pass
                "Believe whatever helps you sleep at night, pussy!":


                    hen "You smug little...!"
                    rob "HENRY! Don't let him get to you! STOP THIS!"
                    rob "HENRY! CALM DOWN!"
                    pass
                "Maybe if you paid attention, you wouldn't be standing here asking me STUPID ASS QUESTIONS!":


                    hen "You have no idea what you're talking about!"
                    hen "You don't know anything about our marriage!"
                    rob "Okay, that's enough! Conversation is over!"
                    rob "HENRY! CALM DOWN!"
                    pass




    scene henrypunch
    with medium_dissolve
    if not persistent.seen_marniepartydanc:


        $ config.allow_skipping = False
        $ renpy.pause(6.0, hard=True)
        $ config.allow_skipping = True


        $ persistent.seen_marniepartydanc = True
        $ renpy.save_persistent()
    else:



        pause 6.0

    stop music

    scene black
    pause 2.0
    jump intro_3






label intro_3:

    $ resetallflags()
    scene black
    with slowfade
    play music my_audio["godsontheme"] loop
    $ renpy.pause(3, hard=True)
    scene mcquote
    with slowfade
    $ renpy.pause(7, hard=True)

    scene mcbegin
    with slowfade
    $ renpy.pause(1, hard=True)


label name1:
    python:
        while True:
            playerName = renpy.input("What is your character's first name? (8 Letter Max)", allow="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ", length=8)
            
            if playerName:
                playerName = playerName.strip()
                playerNameReal = playerName
                MC_Name = playerName
                break

    python:
        while True:
            playerLastName = renpy.input("What is your character's last name?", allow="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ", length=15)
            
            if playerLastName:
                playerLastName = playerLastName.strip()
                break

    scene mcbegin2
    with slowfade

    python:
        initials = playerName[0] + '.' + playerLastName[0] + '.'
        MC_Nickname = initials

    menu:
        "(Use initials as nickname. For example, James Johnson, you will be called, J.J.)":

            $ MC_Name = MC_Nickname
            $ playerName = MC_Nickname
            $ mc_nvl = Character(MC_Name, kind=nvl, image="nighten", callback=Phone_SendSound)
        "(Stick with full name.)":

            $ mc_nvl = Character(MC_Name, kind=nvl, image="nighten", callback=Phone_SendSound)

    python:
        while True:
            fatherName = renpy.input("What is [playerName]'s father's first name? (8 Letter Max)", allow="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ", length=8)
            
            if fatherName:
                fatherName = fatherName.strip()
                break

    jump thestart

label thestart:

    scene mcbegin
    with slowfade

    python:
        while True:
            playerNumberInput = renpy.input("Enter fictional game phone number (just type 7 numbers):", allow="0123456789", length=7)
            
            if len(playerNumberInput) == 7 and playerNumberInput.isdigit():
                formattedNumber = playerNumberInput[:3] + "-" + playerNumberInput[3:]
                playerNumber = "999-" + formattedNumber
                break

    python:
        while True:
            player_languages_raw = renpy.input(
        "Every language you can read, separated by commas (example: english, spanish) For game purposes only:",
        length=500
    )
            player_languages = normalize_player_languages(player_languages_raw)
            
            if player_languages:
                break

    stop music
    scene mcsanta
    if not persistent.seen_marniepartydan:


        $ config.allow_skipping = False
        $ renpy.pause(2.0, hard=True)
        $ config.allow_skipping = True


        $ persistent.seen_marniepartydan = True
        $ renpy.save_persistent()
    else:



        pause 2.0

    stop music fadeout 3.0
    scene black
    with slowfade

    play music my_audio["night ambience"] loop
    scene a28
    with slowfade
    pause

    scene mcphone
    with medium_dissolve
    if not persistent.seen_marniepartyda:


        $ config.allow_skipping = False
        $ renpy.pause(12.0, hard=True)
        $ config.allow_skipping = True


        $ persistent.seen_marniepartyda = True
        $ renpy.save_persistent()
    else:



        pause 12

    scene a30
    with medium_dissolve

    myles_nvl "Yo dude! You make it to the place yet or what?"

    menu(nvl=True):
        "Yep, just got here.":


            mc_nvl "Yeah, I just got here."
            mc_nvl "Still sitting outside trying to figure out what the hell I'm supposed to say."
            myles_nvl "Damn. So that's really the place?"
            myles_nvl "Go knock, bro. You already came all that way."
            myles_nvl "Just keep your eyes open. You don't know these people yet."
        "Yeah, I'm here. But worried...":


            mc_nvl "Yeah, I'm here."
            mc_nvl "I don't know, man. Something about this feels weird."
            myles_nvl "Of course it feels weird."
            myles_nvl "Your dad's in a coma, then you find a note telling you to show up at some random address and ask for a woman you've never met."
            myles_nvl "Still don't know why you didn't tell me her name, but it's all good."
        "Where you at?":


            mc_nvl "Where you at?"
            myles_nvl "At home. Where the hell else would I be?"
            myles_nvl "You ain't tell me you needed backup."
            myles_nvl "You want me to come over there or something?"
        "Remind me again what I'm doing right now?":


            mc_nvl "Remind me what the hell I'm doing here again."
            myles_nvl "Bro, are you serious?"
            myles_nvl "You told me they found that note at the hospital."
            myles_nvl "It had this address on it and said you needed to come here and speak to some woman."
            myles_nvl "That's all you told me. You don't remember telling me that?"

            menu(nvl=True):
                "Oh yeah, that's right.":


                    mc_nvl "Yeah, yeah. I remember."
                    mc_nvl "My head's just all over the place right now."
                    myles_nvl "I figured."
                    myles_nvl "Just making sure you didn't hit your head on the way over there."
                "Sorry, I'm still processing everything.":


                    mc_nvl "I'm still trying to process all this."
                    mc_nvl "It doesn't even feel real yet."
                    myles_nvl "You don't gotta apologize to me."
                    myles_nvl "Your dad's lying in a hospital and now you're chasing some note he left behind."
                    myles_nvl "That's a lot of shit to get dropped on you at once."
                "I'm just overwhelmed.":


                    mc_nvl "I'm overwhelmed, man."
                    mc_nvl "Every time I think I understand what's happening, something else gets added."
                    myles_nvl "Yeah, I get it."
                    myles_nvl "Just take it one thing at a time."
                    myles_nvl "Right now, all you gotta do is knock on the door and find out who this woman is."

    myles_nvl "But for real, how are you holding up?"
    myles_nvl "And don't just hit me with some 'I'm good' bullshit."

    menu(nvl=True):
        "Honestly, I don't know.":


            mc_nvl "Honestly, I don't know."
            mc_nvl "One minute I feel fine, then the next minute I start thinking about everything again."
            myles_nvl "Yeah. That makes sense."
            myles_nvl "You don't gotta have some perfect answer right now."
            myles_nvl "The whole situation is fucked."

            menu(nvl=True):
                "I keep thinking he might not wake up.":


                    mc_nvl "I keep thinking he might not wake up."
                    myles_nvl "I know."
                    myles_nvl "I'm not gonna lie and tell you that thought isn't scary."
                    myles_nvl "But he's still here, bro. Until somebody says otherwise, don't write him off."
                "I just want to know why he sent me here.":


                    mc_nvl "I just want to know why he sent me here."
                    mc_nvl "Why this woman? Why this house?"
                    myles_nvl "That's what you're there to find out."
                    myles_nvl "Maybe she knows something about him you don't."
                    myles_nvl "Or maybe he trusted her enough to help you with something."
                "I don't really want to talk about it.":


                    mc_nvl "I don't really want to talk about it right now."
                    myles_nvl "All right."
                    myles_nvl "I'm not gonna keep pushing."
                    myles_nvl "Just don't disappear on everybody and sit there dealing with all this alone."
        "I'm numb, I guess.":


            mc_nvl "I don't know. I mostly just feel numb."
            mc_nvl "Like all this is happening to somebody else."
            myles_nvl "Yeah, shock will do that."
            myles_nvl "You probably haven't even had time to really sit down and process anything."
            myles_nvl "Hospital, the note, driving out there... you've just been moving."

            menu(nvl=True):
                "Maybe moving is better than thinking.":


                    mc_nvl "Maybe moving is better than sitting around thinking."
                    myles_nvl "For now, maybe."
                    myles_nvl "Just don't keep running forever."
                    myles_nvl "Eventually, all that shit catches up with you."
                "I don't even know what I'm supposed to feel.":


                    mc_nvl "I don't even know what I'm supposed to feel."
                    myles_nvl "There isn't a right answer."
                    myles_nvl "Mad, scared, confused...whatever comes up, it comes up."
                    myles_nvl "You don't gotta force yourself to react a certain way."
                "I'm fine. I just need answers.":


                    mc_nvl "I'm fine."
                    mc_nvl "I just need some answers."
                    myles_nvl "Then get the answers."
                    myles_nvl "Knock on the door, talk to this unknown chick, and see what she knows."
                    myles_nvl "At least then you won't be sitting there guessing."
        "I'm trying not to think about it too much.":


            mc_nvl "I'm trying not to think about it too much."
            mc_nvl "Every time I do, my head starts going somewhere bad."
            myles_nvl "I get it."
            myles_nvl "Just don't act like you're okay if you're not."
            myles_nvl "You don't have to give me some big speech. Just say something."

            menu(nvl=True):
                "What do you want me to say?":


                    mc_nvl "What do you want me to say?"
                    mc_nvl "My dad's in a coma, and I have no idea why he sent me here."
                    myles_nvl "You can say exactly that."
                    myles_nvl "I'm not asking you to solve the whole situation through text."
                    myles_nvl "I'm just checking on my boy."
                "I really don't know what to say.":


                    mc_nvl "I really don't know what to say."
                    myles_nvl "Then don't say much."
                    myles_nvl "Just know you can call me if your head starts getting too loud."
                    myles_nvl "Even if we sit on the phone and don't talk about shit."
                "I'll deal with it later.":


                    mc_nvl "I'll deal with it later."
                    mc_nvl "Right now, I just need to get through this."
                    myles_nvl "Fair enough."
                    myles_nvl "Handle what's in front of you first."
                    myles_nvl "Just don't keep saying 'later' until six months go by."

    myles_nvl "Anyway, go see what this chick has to say."
    myles_nvl "Maybe your dad left that note because he knew she'd be able to explain something."
    myles_nvl "And if the whole thing feels wrong, leave. You don't owe anybody in that house shit."

    menu(nvl=True):
        "I'll let you know what happens.":


            mc_nvl "I'll let you know what happens."
            myles_nvl "You better."
            myles_nvl "Don't have me sitting here wondering whether you got kidnapped by some suburban cult."
            myles_nvl "Text me when you get inside."
        "You really think I should go in?":


            mc_nvl "You really think I should go in?"
            myles_nvl "You took the bus all the way there."
            myles_nvl "Might as well find out why your dad wanted you to come."
            myles_nvl "Just don't ignore your gut if something feels off."
        "I might just leave.":


            mc_nvl "Part of me wants to just leave."
            myles_nvl "You can."
            myles_nvl "But you'll probably spend the whole bus ride home wondering what was behind that door."
            myles_nvl "At least talk to her first. Then decide."

    myles_nvl "Anyway bro, I'm gonna let you handle that."
    myles_nvl "But seriously, call me if you need anything."
    myles_nvl "I don't care if it's about your dad, this random chick, or you just need somebody to talk shit with."
    myles_nvl "I'm here. You already know that."

    scene a31_1
    with medium_dissolve
    pause

    scene a31
    with medium_dissolve
    pause
    jump knoc1

label knoc1:

    menu:
        "*Knock on the door.*":




            scene mcknock
            with medium_dissolve

            if not persistent.seen_marniepartyd:


                $ config.allow_skipping = False
                $ renpy.pause(13.2, hard=True)
                $ config.allow_skipping = True


                $ persistent.seen_marniepartyd = True
                $ renpy.save_persistent()
            else:



                pause 13.2
                pass
        "*Wait for someone to walk by.*":


            mc "......."
            mc ".........."
            mc "............."
            jump knoc1
        "*Do nothing.*":


            mc "......."
            mc ".........."
            mc "............."
            jump knoc1
        "*Stand here looking stupid.*":


            mc "......."
            mc ".........."
            mc "............."
            jump knoc1

    $ pe2 = "{image=sexaddict} What's up! I'm here to see a hott woman named, Marnie!"
    $ pe1 = "{image=good} Good evening, sir. I need to speak with someone named, Marnie?"
    $ pe3 = "{image=evil} Out of my way. Now."

    scene a32
    with medium_dissolve

    menu:
        "[pe1]":




            $ resetallflags()
            $ good = True
            $ memory_chose_good_path = True
            $ show_tooltip(n=1)
            play sound2 my_audio["goodturn"] noloop
            $ default_mouse = "good"

            scene a33
            with medium_dissolve

            hen "Marnie? That's my wife."
            hen "What do you want with her?"

            menu:
                mc ""
                "My father told me I needed to find her. He said she'd help me.":



                    hen "Your father?"

                    scene a34
                    with medium_dissolve

                    hen "Alright... slow down."
                    hen "How exactly does your father know my wife? Because I don't recall Marnie mentioning him."
                "I'm sorry for showing up unannounced. My father left me one name and one address... Marnie's.":


                    hen "Your father gave you my address?"

                    scene a34
                    with medium_dissolve

                    hen "That's... oddly specific."
                    hen "So how exactly does he know my wife?"
                "I know this sounds strange, but my father told me if anything ever happened to him, I needed to come here and speak with Marnie.":


                    hen "..."

                    scene a34
                    with medium_dissolve

                    hen "Well, that's definitely not something I hear every day."
                    hen "How does your father know my wife?"

            menu:
                mc ""
                "I'm afraid I don't know. He only left me her name and this address.":



                    hen "That's pretty convenient."
                "I wish I had a better answer for you. I'm just doing what he left in a note. He's in a coma.":


                    hen "A coma..."
                    hen "Right..."
                "If I knew more, I'd tell you. I'm just as confused as you are.":


                    hen "You definitely look confused."

            scene a35
            with medium_dissolve

            hen "Listen, kid... from where I'm standing, a complete stranger has shown up at my front door asking for my wife by name."
            hen "You've got to admit, that's not exactly an everyday occurrence."
            hen "So forgive me if I'm a little cautious."

            scene a36
            with medium_dissolve

            hen "Marnie's a kind woman. Sometimes a little too kind."
            hen "I have to be the one who asks the difficult questions around here."
            hen "Now help me understand why I shouldn't close this door and call it a night."

            scene a37
            with medium_dissolve

            menu:
                mc ""
                "Because if our situations were reversed, I'd hope someone would at least hear my story.":



                    scene a38
                    with medium_dissolve

                    hen "..."
                    hen "......."
                    hen ".........."

                    scene a39
                    with medium_dissolve

                    hen "That's a fair answer."
                    hen "Doesn't mean I trust you... but it's fair."
                "I'm not asking you to trust me. Just give me five minutes.":


                    scene a38
                    with medium_dissolve

                    hen "..."
                    hen "......."
                    hen ".........."

                    scene a39
                    with medium_dissolve

                    hen "Five minutes."
                    hen "Five minutes is all you get, and then I'm kicking you out. From where I'm standing, you could just be here to rob me."
                "If, after you've heard me out, you still want me to leave, I'll leave without causing any trouble.":


                    scene a38
                    with medium_dissolve

                    hen "..."
                    hen "......."
                    hen ".........."

                    scene a39
                    with medium_dissolve

                    hen "Well, I GUESS you've been respectful enough since I opened the door. That counts for something."

            scene a39_1
            with medium_dissolve

            hen "Alright."
            hen "You can come in. But understand something... I still don't know who you are, and until I do, I'm keeping a close eye on you."
            hen "Come on. Let's see if Marnie recognizes you, or your 'father'."
            hen "One wrong move, and you're done. Got it?"
            stop music fadeout 2.0
            jump insidehouse
        "[pe2]":




            $ resetallflags()
            $ sexaddict = True
            $ memory_chose_sexaddict_path = True
            $ show_tooltip(n=3)


            scene a33
            with medium_dissolve

            hen "Marnie? That's my wife."
            hen "...And what exactly do you mean by 'hot woman'?"

            menu:
                mc ""
                "Come on, man. It was a compliment.":



                    hen "A compliment?"
                    hen "To another man's wife?"

                    scene a34
                    with medium_dissolve

                    hen "Either you've got a hell of a lot of confidence..."
                    hen "...or absolutely no common sense."
                    hen "Which one is it?"
                "Hey, I'm just saying she's beautiful. Can't blame a guy for having eyes.":


                    hen "..."

                    scene a34
                    with medium_dissolve

                    hen "Oh, I can blame you."
                    hen "Especially when you're standing on my porch saying it."
                "Relax. I haven't even met her yet. I'm just going off what I heard.":


                    hen "What you've heard?"

                    scene a34
                    with medium_dissolve

                    hen "Now I'm even more interested in who's been talking about my wife."

            menu:
                mc ""
                "I just call it like I see it.":



                    hen "Mm-hmm. Well you haven't seen anything, so far."
                "Didn't mean any disrespect.":


                    hen "Sure you didn't."
                "I just figured honesty was the best policy. Do you want me to lie about it?":


                    hen "Not at somebody else's front door."

            scene a35
            with medium_dissolve

            hen "Listen, kid..."
            hen "You don't knock on a stranger's door, ask for his wife, then start rating her appearance."
            hen "Most people would already have the door slammed in their face."

            scene a36
            with medium_dissolve

            hen "Lucky for you, I'm trying very hard to be patient."
            hen "So if you've actually got a reason for being here besides making smart remarks..."
            hen "I'd suggest you tell me now."

            scene a37
            with medium_dissolve

            menu:
                mc ""
                "My father told me Marnie could help me. That's why I'm here.":



                    scene a38
                    with medium_dissolve

                    hen "..."
                    hen "......."
                    hen ".........."

                    scene a39
                    with medium_dissolve

                    hen "You really should've led with that."
                "Look, I joke around when I'm nervous. Bad habit.":


                    scene a38
                    with medium_dissolve

                    hen "..."
                    hen "......."
                    hen ".........."

                    scene a39
                    with medium_dissolve

                    hen "Clearly."
                    hen "It's not a habit I'd recommend keeping."
                "I know that sounded bad, but I'm genuinely here because my father sent me.":


                    scene a38
                    with medium_dissolve

                    hen "..."
                    hen "......."
                    hen ".........."

                    scene a39
                    with medium_dissolve

                    hen "Well..."
                    hen "I'm still not convinced, but at least you're making more sense now."

            scene a39_1
            with medium_dissolve

            hen "Fine."
            hen "You can come in."
            hen "But if I hear one more comment about my wife looking 'hot,' you'll be explaining yourself from the other side of my front door."
            hen "Now come on. Let's see why Marnie's apparently so important to your father."

            jump insidehouse
        "[pe3]":



            stop music fadeout 2.0
            play music2 my_audio["apartment4"] loop fadein 15.0
            scene mcangry
            with medium_dissolve

            if not persistent.seen_marnieparty:


                $ config.allow_skipping = False
                $ renpy.pause(30, hard=True)
                $ config.allow_skipping = True


                $ persistent.seen_marnieparty = True
                $ renpy.save_persistent()
            else:



                pause 30

            jump introevil

label introevil:

    $ resetallflags()
    $ evil = True
    $ memory_chose_evil_path = True
    $ show_tooltip(n=2)
    play sound2 my_audio["evilturn"] noloop
    $ default_mouse = "evil"

    scene a40
    with medium_dissolve

    voice my_audio["9"]
    nar "Heh.....I guess he didn't enjoy your little, surprise entrance."
    voice my_audio["10"]
    nar "There was no need for words. You're here for a woman, not whoever the FUCK this guy is."
    voice my_audio["11"]
    nar "Besides, you explained yourself after you came in. That has to count for something."

    menu:
        "You done?":




            scene mcangry2
            with ffast_dissolve


            if not persistent.seen_marniepart:


                $ config.allow_skipping = False
                $ renpy.pause(14.0, hard=True)
                $ config.allow_skipping = True


                $ persistent.seen_marniepart = True
                $ renpy.save_persistent()
            else:



                pause 14.0

            pass
        "Relax, buddy. I explained myself after I came in, at least. Doesn't that count?":


            scene mcangry3
            with ffast_dissolve

            if not persistent.seen_marniepar:


                $ config.allow_skipping = False
                $ renpy.pause(14, hard=True)
                $ config.allow_skipping = True


                $ persistent.seen_marniepar = True
                $ renpy.save_persistent()
            else:



                pause 14.0

            pass
        "It was just a fucking joke man, chill the fuck out.":




            scene mcangry4
            with ffast_dissolve

            if not persistent.seen_marniepa:


                $ config.allow_skipping = False
                $ renpy.pause(14, hard=True)
                $ config.allow_skipping = True


                $ persistent.seen_marniepa = True
                $ renpy.save_persistent()
            else:



                pause 14.0
            pass

    scene black
    with fade

    scene a42
    with medium_dissolve

    mar "Jesus, Henry! What's with all the yelling?!"
    hen "This FUCKING piece of work barged into our house! Then he shoved me out of the way and said he needed to talk to you!"
    hen "I don't know who the FUCK he is!"
    hen "Just get in here and talk to him so he can get the FUCK outta here!"
    jump continue1


label continue1:

    scene a43
    with medium_dissolve

    mar "Someone wanted to see... me?"
    mar "Oh... I've got a visitor!"
    hen "Ugh....yes, that's what I said!"
    hen "Just get over here!"

    scene marniewalk1
    with medium_dissolve

    if not persistent.seen_marniep:


        $ config.allow_skipping = False
        $ renpy.pause(13.4, hard=True)
        $ config.allow_skipping = True


        $ persistent.seen_marniep = True
        $ renpy.save_persistent()
    else:



        pause 13.4

    scene a44
    with medium_dissolve

    hen "......."
    hen "..........."
    hen "So? Do you know this guy?"

    mar "......."
    mar "Oh my........"

    scene mcsexstuff
    with medium_dissolve
    if not persistent.seen_marnie:


        $ config.allow_skipping = False
        $ renpy.pause(13.8, hard=True)
        $ config.allow_skipping = True


        $ persistent.seen_marnie = True
        $ renpy.save_persistent()
    else:



        pause 13.8

    scene a47
    with medium_dissolve

    mar "No. I've never met him before."
    hen "Good. Then he can leave. I'll send him on his way right now."
    mar "W-What!? Henry, honestly... why would you do that? He hasn't done anything."
    hen "What do you mean he, 'hasn't done anything'??"

    scene a48
    with medium_dissolve

    mar "Look, it's nearly midnight. We can't just throw the poor boy outside because he knocked on our door."
    mar "He's obviously come all this way for a reason. Let him stay the night, let him settle in, let him feel comfortable, and tomorrow we can hear him out properly."
    hen "Marnie, that's exactly the kind of thinking that gets you into trouble."
    mar "I don't see what's so terrible about making someone feel welcome."

    scene a49
    with medium_dissolve

    mar "We've got a lovely guest room, clean sheets, a hot shower... honestly, I'd hate for him to spend the night all tense when we could just help him unwind a little."
    hen "Marnie..."
    hen "Do you ever stop and think about how half the things you say sound?"
    mar "What? I only meant we should make him comfortable. I don't know why you always make it sound like something else."

    scene a50
    with medium_dissolve

    hen "Alright, alright. Fine. He can stay."
    hen "But he stays one night. One. Tomorrow we find out exactly why he's here, and if I don't like the answer, he's gone."

    scene a51
    with medium_dissolve

    mar "Thank you. I knew you wouldn't leave someone stranded."
    mar "Once he's had something warm to eat, a proper bed, and a chance to relax a bit, I'm sure everything will make much more sense in the morning."
    hen "You're lucky your heart's bigger than your common sense."

    scene a53
    with medium_dissolve

    hen "Well, if he's staying, then we're going over the house rules."
    hen "I don't care why he came here. While he's under my roof, he'll respect my home, my wife, and everybody in this house."
    hen "And he's gonna hear that from me personally."

    menu:
        mc ""
        "You know I'm standing right here, don't you? I can literally hear everything you're saying.":



            scene a54
            with medium_dissolve

            hen "Good. Then I won't have to waste my breath repeating myself."
            hen "Since you're already listening, pay close attention. This is my house, not a hotel."
            hen "While you're under this roof, you show respect to everyone living here. You don't wander around wherever you feel like it, you don't make yourself at home, and you don't forget whose name is on this front door."
            hen "If you have a problem with any of that, you're welcome to leave before the night's over."
            pass
        "Sounds fair enough. So... what exactly are these rules?":


            scene a54
            with medium_dissolve

            hen "Rule number one: respect this house."
            hen "Rule number two: respect me and my wife. I don't tolerate smart remarks, attitude, or anyone trying to push boundaries."
            hen "Rule number three: if you need something, you ask. You don't go snooping around, opening doors that aren't yours, or making yourself too comfortable."
            hen "You follow those rules, we'll get along just fine. You don't... and tomorrow morning will come a lot sooner than you're expecting."
            pass
        "You always give every guest a speech like this, or am I just special?":


            scene a54
            with medium_dissolve

            hen "Don't flatter yourself."
            hen "Most guests don't show up at my front door unannounced asking for my wife by name."
            hen "Most guests introduce themselves before expecting me to let them spend the night in my home."
            hen "So yes... you're getting special treatment. Just not the kind you were probably hoping for."
            pass

    scene a55
    with medium_dissolve

    hen "One more thing. My mother-in-law, Martha, lives here too. She's usually the first one awake every morning, so don't go wandering around the house thinking everyone's asleep."
    hen "Lorraine is Marnie's younger sister. She's staying with us for the time being, so if you see another woman around the house who looks a bit like Marnie, that's her."
    hen "Jennifer and Yuni are our daughters. Jennifer's room is down the hall, Yuni's is at the far end. Stay out of both unless one of them specifically asks you to come in. Especially Jennifer...."
    hen "We are also holding a birthday party for Jennifer, tomorrow night. But you should be gone by then."

    scene a56
    with medium_dissolve

    hen "Most everybody's asleep by eleven, so keep the noise down if you're still awake. This isn't some college dorm where people are shouting all night."
    hen "The kitchen's yours if you're hungry, but clean up after yourself. If you make a mess, you clean it. Marnie shouldn't have to pick up after a grown man."
    hen "You respect this house, and we'll respect you. Break that trust, and your stay here will be a very short one."
    nar "......."
    voice my_audio["12"]
    nar "Hmmm......."

    scene a57
    with medium_dissolve

    voice my_audio["13"]
    nar "Your eyes drift toward Marnie almost on instinct."
    voice my_audio["14"]
    nar "You can't help but notice how her long shirt hugs her curves, especially the way it stretches across her full huge breasts. The fabric's thin enough to hint at what's underneath, and you feel a stirring as your eyes linger there a second too long."
    voice my_audio["15"]
    nar "She carries herself with this casual confidence that's somehow even sexier than if she were trying. Her mature, voluptuous body has this magnetic pull that makes it hard to look away, and you can feel the heat building as you give in to the urge to keep watching..."

    $ upe2 = "{image=good} *Resist The Urge. Give the woman a polite warm smile.*"

    $ upe1 = "{image=evil} {image=sexaddict} *Give in and lust over the older woman. Stare at her.*"

    menu:



        "[upe1]" if evil or sexaddict:
            jump evilcho1

        "[upe2]" if good:
            jump goodchoice

label goodchoice:
    stop music fadeout 1.0
    play music my_audio["goodtheme"] loop fadein 1.0

    voice my_audio["49"]
    nar "The urge is there, but an urge is not an order. You let it pass without giving it anything more."
    voice my_audio["50"]
    nar "Instead, you offer her a warm, harmless smile. The sort that asks for nothing in return."
    scene marniesmile
    with medium_dissolve
    voice my_audio["51"]
    nar "Her answer is immediate. She smiles back, and whatever tension had begun to form quietly disappears."
    voice my_audio["52"]
    nar "A troubling thought does not make you a bad man. What matters is the choice you make after it, and you, choose to be kind."

    scene mcsmile
    with medium_dissolve

    voice my_audio["53"]
    nar "You turn your attention back to Henry, who is still explaining the rules of the house."
    voice my_audio["54"]
    nar "You give him a small, friendly smile. Not enough to interrupt him, but enough to show that you are listening."
    voice my_audio["55"]
    nar "You did not come here to cause trouble. Whatever this strange house has waiting for you, you intend to meet it as a decent man."
    jump henrywait


label evilcho1:

    play music my_audio["think2evil"] loop fadein 1.0

    scene a66
    with medium_dissolve

    $ marniestare = True
    $ memory_marnie_noticed_stare = True
    $ show_tooltip(n=5)


    voice my_audio["16"]
    nar "You give in to the urge, letting your eyes linger on Marnie without restraint."
    voice my_audio["17"]
    nar "You squint slightly, taking in every detail of her form as your gaze travels down her body appreciatively."

    scene a59
    with medium_dissolve

    voice my_audio["18"]
    nar "Yes! Perfect! She knows you're staring at her."
    voice my_audio["19"]
    nar "A knowing sense of shock plays on her face as she seems to understand exactly where your mind has gone."

    scene a60
    with medium_dissolve

    voice my_audio["20"]
    nar "Your eyes continue downward, drinking in the sight of her thick thighs and perfectly shaped feet."
    voice my_audio["21"]
    nar "You feel a primal urge as you imagine tracing your tongue along those arches and sucking on those perfectly pedicured toes."
    voice my_audio["22"]
    nar "Your cock grows harder as your eyes fixate on those feet, legs, and everything between them that you're desperate to explore."
    voice my_audio["23"]
    nar "Henry is still talking to you, but it all sounds like meaningless gibberish now. Your entire being is focused on Marnie's body."

    scene a63
    with medium_dissolve

    mar "........"
    mar "............."
    mar ".................."



    scene mcblahblah
    with medium_dissolve
    if not persistent.seen_marn:


        $ config.allow_skipping = False
        $ renpy.pause(14.5, hard=True)
        $ config.allow_skipping = True


        $ persistent.seen_marn = True
        $ renpy.save_persistent()
    else:



        pause 14.5

    scene a67
    play sound my_audio["fahh"] noloop
    with hpunch
    pause 2.0

    voice my_audio["24"]
    nar "Well, that was quite a show."
    voice my_audio["25"]
    nar "You can't decide if this woman wants you to fuck her brains out, or is just teasing you for the fun of it."
    voice my_audio["26"]
    nar "However, the-"
    hen "Hey! Are you listening!?"
    jump henrywait

label henrywait:

    mar "Henry, wait honey."

    scene a64
    with medium_dissolve

    mar "Henry, darling, I think that's enough for one evening. The poor boy is probably exhausted after travelling all this way."
    mar "Why don't we show him where he'll be sleeping, let him get settled in, and the rest can wait until tomorrow? There'll be plenty of time for more of this in the morning."
    hen "...Alright, alright. Fair enough."

    scene black
    with slowfade

    scene a69
    with slowfade

    hen "Your room's upstairs. Go up the stairs and look to your left when you get to the top. It's the door right there."
    hen "You'll be staying there for tonight, just one night. Tomorrow morning we'll sit down, have a real conversation, and you can tell us exactly why you came looking for Marnie."
    hen "Until then, just remember everything we talked about here tonight, and we'll get along just fine."

    scene a70
    with medium_dissolve

    hen "One last thing. I'll be reading for a while before I head to bed, so I'd appreciate it if you kept the noise to a minimum."
    hen "If you need the bathroom or the kitchen, that's fine. Just try not to slam doors or wake anybody up. Most of the house is already asleep."
    hen "Other than that... welcome, I guess. Get some rest. Tomorrow's probably going to be a long day for all of us."
    hen "That's about all I can think of right now."

    scene a71
    with medium_dissolve

    hen "Anything else you can think of, Marnie?"
    mar "Well, I was just thinking... if he get's too hot up there, I could help him take off whatever clothes he needs. I always sleep better when I'm naked."

    scene a72
    play sound my_audio["bang sound 1"] noloop
    stop music
    with hpunch

    hen "God damn it, Marnie! We talked about this! Wake up!!"
    hen "You keep saying things without thinking about how they sound! We even went to therapy because of it, remember!? You can't keep doing this!"
    hen "You're a beautiful woman, and people hear those comments differently than you mean them. Think before you speak!"

    scene mchenryangry
    with medium_dissolve

    if not persistent.seen_marni:


        $ config.allow_skipping = False
        $ renpy.pause(14, hard=True)
        $ config.allow_skipping = True


        $ persistent.seen_marni = True
        $ renpy.save_persistent()
    else:



        pause 14

    scene black
    with slowfade

    pause 2.0

    scene a76
    with medium_dissolve

    $ upe5 = "{image=evil} {image=sexaddict} Hang on, before you go, I want to see that thing you did with your tongue, mouth, and fingers earlier. It was hott."

    $ upe4 = "{image=evil} Who gives a shit? So you slept with some guy and got knocked up. So what? Tell him to get over it."

    $ upe3 = "{image=good} That was almost twenty years ago though. I'm not trying to excuse what you did. But, shouldn't time heal things?"

    mar "I'm.....sorry you had to see that... Henry doesn't normally lose his temper. Well... not without good reason, anyway."
    mar "And before you start thinking he's some horrible man... he isn't. Truth is... I earned that reaction a long time ago."
    mar "About eighteen years ago, I made a dreadful mistake. I... slept with another man. His name was George."
    mar "It was only once, and I'm not saying that makes it any better, but it only happened once. Then I found out I was pregnant with Yuni... and, well... everything just sort of... fell apart after that."
    $ foundoutmarniecheated = True


    menu:
        mc ""
        "I got it, but, does he always talk to you like that?":



            scene a77
            with medium_dissolve

            mar "Oh, goodness, no. If he did, I'd have probably smacked him over the head with one of his books by now."
            mar "He's actually a wonderful husband. That's the awful part of all this. Henry didn't deserve what I did to him... not even a little bit."
            mar "Every now and then something reminds him of it, and all those feelings come rushing back. I suppose that's the price we both pay for trying to put something like that behind us."

        "[upe3]" if good:

            scene a77
            with medium_dissolve

            mar "People always say that... 'It was years ago; time heals all,' as though time actually magically fixes everything."
            mar "It doesn't, really. It makes it easier to live with, but it doesn't make it disappear."
            mar "Henry forgave me. I truly believe he did. But forgiving someone and forgetting what happened... those are two very different things."

        "[upe4]" if evil:

            scene a77
            with medium_dissolve

            mar "Please don't say that. It wasn't just some little mistake. I betrayed the man who loved me more than anyone else ever has."
            mar "Every time Henry looked at Yuni... he was reminded of what I'd done. Imagine carrying something like that around every single day, then trying to smile through it anyway."
            mar "He had every reason to leave me, but he didn't. So no... I'm not going to tell him to 'get over it.' The least I can do is spend the rest of my life trying to be the wife he deserved from the very beginning."


    scene a78
    with medium_dissolve

    $ upe6 = "{color=#228B22}[CONVERT]{/color}{image=good} You know what, this has already gone too far. I'm sorry for asking this. Just forget about it."

    $ upe5 = "{image=evil} {image=sexaddict} Hang on, before you go, I want to see that tongue thing you did with your mouth and fingers earlier. It was hot."

    $ upe7 = "{image=evil} Just fucking do it!"

    $ upe8 = "{image=good} I appreciate you telling me. That couldn't have been easy to talk about."

    $ upe38 = "{image=good} It sounds like you've been blaming yourself for awhile."

    mar "George used to come by the house every now and then. Henry trusted him, I trusted him... we all did."
    mar "One evening Henry was away, George stopped by, we had a few drinks, started talking, and... well... I've always been a bit daft with the way I speak. I say things without thinking how they sound, and I suppose I gave him the wrong idea."
    mar "One poor decision led to another, and before I knew it I'd destroyed the best thing that had ever happened to me."
    mar "But anyway... that's all in the past now. I just thought you deserved to know why Henry reacted the way he did."
    mar "We really should be getting to bed now, anyway."

    menu:
        mc ""


        "[upe8]" if good:

            $ memory_marnie_compassion = True
            $ show_tooltip(n=6)

            scene a83
            with medium_dissolve

            mar "No... it never is. I don't enjoy talking about it, but pretending it never happened would be even worse."
            mar "Henry and I have spent years trying to put our lives back together. Some days are easier than others."
            mar "Anyway... it's getting rather late. Why don't you head upstairs and get yourself some proper rest? We'll talk more in the morning."
            mar "You have a good night! Sleep well!"
            jump upstairs1

        "[upe38]" if good:

            $ memory_marnie_compassion = True
            $ show_tooltip(n=6)

            scene a83
            with medium_dissolve

            mar "I have."
            mar "When you hurt someone you love that deeply, I don't think that feeling ever completely goes away. You simply learn to live with it."
            mar "Anyway... it's getting rather late. Why don't you head upstairs and get yourself some proper rest? We'll talk more in the morning."
            mar "You have a good night! Sleep well!"
            jump upstairs1

        "[upe5]" if evil or sexaddict:

            scene a79
            play sound my_audio["bang sound 1"] noloop
            with hpunch

            mar "Y-You do?"
            scene a80
            with medium_dissolve
            mar "......"
            mar "........."

            scene a81
            with medium_dissolve

            mar "N-No....I can't. That would be wrong."
            mar "Like Henry said, I don't want to give you the wrong idea."
            mar "Honestly, I'm surprised you're even asking that...."

            scene a82
            with medium_dissolve

            menu:
                "But I like it when you act like a slutty whore. It's hott as fuck!":




                    $ memory_marnie_cruelty = True
                    $ show_tooltip(n=7)

                    mar "....."
                    mar "........do you?"
                    mar "........."
                    mar ".............."
                    mar ".....alright then, I guess."
                    jump tongueout
                "[upe6]":


                    scene a83
                    with medium_dissolve
                    $ resetallflags()
                    $ good = True
                    $ memory_marnie_backed_away = True
                    $ show_tooltip(n=8)

                    play sound2 my_audio["goodturn"] noloop
                    $ default_mouse = "good"
                    mar "W-Well... that's a relief. You honestly had me worried for a moment there."
                    mar "I'm not going to pretend I didn't notice the way you were looking at me earlier, however. Those eyes of yours... they weren't exactly difficult to read, and I don't think I'll be forgetting that anytime soon."
                    mar "Still... I appreciate you letting the matter go. I think that's for the best."
                    mar "Now, why don't you head upstairs and get yourself some proper rest? We'll have a fresh start in the morning, love."
                    mar "Have a good night! Sleep well!"
                    jump upstairs1

                "[upe7]" if evil:

                    $ memory_marnie_cruelty = True
                    $ show_tooltip(n=7)

                    mar "......."
                    mar "..........."
                    mar "Yes sir."
                    jump tongueout


label tongueout:


    $ marniefingersinmouth = True

    $ upe9 = "{image=evil} *Say nothing. Breathe deeply and stare at the woman. Start giving in to The Urge.*"

    scene mcblowkiss
    with medium_dissolve

    if not persistent.seen_blowkiss:


        $ config.allow_skipping = False
        $ renpy.pause(13.2, hard=True)
        $ config.allow_skipping = True


        $ persistent.seen_blowkiss = True
        $ renpy.save_persistent()
    else:



        pause 13.2

    scene a83
    with medium_dissolve
    mar "Well, how was that?"

    menu:
        "Fucking hott! You're such a sexy slutty whore!":




            mar "Oh-....well, thank you, I guess?"
            mar "I was always told that, as a woman, you should make sure men are happy when they are around you, so I'm glad I did just that! You are happy now, aren't you?"
            mar "Anyway... it's getting rather late. Why don't you head upstairs and get yourself some proper rest? We'll talk more in the morning."
            mar "You have a good night! Sleep well!"
            if sexaddict or evil:
                jump upstairsexaddict
            else:
                jump upstairs1
        "Pretty good I suppose. Would have liked to see a bit more.":


            mar "I understand! But I think that's where we should leave it, for now."
            mar "Like Henry said, I really should stop acting like this, but at least I'm glad I was able to entertain you."
            mar "Anyway... it's getting rather late. Why don't you head upstairs and get yourself some proper rest? We'll talk more in the morning."
            mar "You have a good night! Sleep well!"
            if sexaddict or evil:
                jump upstairsexaddict
            else:
                jump upstairs1

        "[upe9]" if evil:

            voice my_audio["27"]
            nar "For a moment, you simply stare at this stupid cum dumpster standing in front of you."
            voice my_audio["28"]
            nar "Your breathing grows deeper, your pulse heavier, as the last of your restraint begins to slip."
            voice my_audio["29"]
            nar "What takes its place is something simpler. Something raw, wordless, and entirely focused on the woman in front of you. This dumb whore of a wife knows the hunger in you, and judging by her smile, it's exactly the reaction she wanted."
            voice my_audio["30"]
            nar "You'd bet money that she wants you to stick your tongue down her throat right now. All you need to do, is hear her say it."
            mar "......"
            mar "........."
            mar "Hellooooo? Are you there?"
            mar "Ah, I see, you must be in shock. Well, I guess I credit that to my skills, after all!"
            mar "It's times like this we would usually make-out! I mean, I want to kiss you, but-"
            mar "S-Sorry! I'm being silly! It's like Henry said, I really should stop talking like this!"
            mar "Anyway... it's getting rather late. Why don't you head upstairs and get yourself some proper rest? We'll talk more in the morning."
            mar "You have a good night! Sleep well!"

            $ marniemakeout = True
            $ memory_marnie_kiss = True
            $ show_tooltip(n=9)


            scene mcgrabkiss
            with fade
            call godson_locked_cutscene ("gui/mcgrabkiss.webm", 60.1, "seen_mcgrabkiss") from _call_godson_locked_cutscene_1

            scene black
            with slowfade

            pause 3.0
            jump wellgreat


label wellgreat:

    $ memory_marnie_contact_added = True
    $ show_tooltip(n=4)


    scene a84
    with slowfade

    voice my_audio["31"]
    nar "Well, that 'kind of' went as expected."
    voice my_audio["32"]
    nar "Let's just hope no issues come from that. However, something tells you that's not the end of it."
    voice my_audio["33"]
    nar "Not to mention.....for some reason.....you felt someone.....watching you just now while your tongue was down Marnie's throat. And, you don't sense that they were happy about it either."
    voice my_audio["34"]
    nar "Whatever, who cares, at any rate, you stand at the foot of the staircase for a quiet moment, your eyes slowly following each step until they disappear into the darkness above."
    voice my_audio["35"]
    nar "It's been one hell of a day. A stranger's home. A marriage hanging together by old scars. A woman named Marnie your father somehow trusted enough to send you here."
    voice my_audio["36"]
    nar "Nothing about tonight makes sense... but if your father believed this was where your journey had to begin, then for now, all you can do is keep moving."

    scene a85
    with medium_dissolve

    voice my_audio["37"]
    nar "Your thoughts drift back to the hospital. The steady beeping of machines. The smell of disinfectant. Your father lying unconscious, unable to explain any of this himself."
    voice my_audio["38"]
    nar "All he left behind was a name... an address... and the hope that coming here would answer questions he no longer could."
    voice my_audio["39"]
    nar "You don't know whether this house holds the answers you're looking for or simply more questions. Either way, turning back now isn't an option."

    scene black
    with slowfade
    play sound my_audio["stairs2"] noloop

    pause 2.0

    scene a86
    with slowfade

    voice my_audio["40"]
    nar "You make your way upstairs, each step creaking softly beneath your feet."
    voice my_audio["41"]
    nar "At the top of the landing, just as Henry described, a door waits on your left. This must be the room."
    stop sound fadeout 1.0

    scene a87
    with medium_dissolve

    voice my_audio["42"]
    nar "You pause outside the door and press an ear against it, listening carefully."
    voice my_audio["43"]
    nar "Silence."
    voice my_audio["44"]
    nar "Not a television. Not footsteps. Not even the sound of someone breathing. Whoever stayed here before you, if anyone ever did, certainly isn't inside now."
    voice my_audio["45"]
    nar "Satisfied, you wrap your hand around the doorknob, quietly push the door open, and step inside."
    jump goinside

label goinside:

    scene black
    with slowfade

    play sound my_audio["dco"] noloop
    pause 2.0

    scene a88
    with slowfade

    voice my_audio["46"]
    nar "The room is far nicer than you expected. Spacious, clean, and surprisingly modern, with polished hardwood floors stretching from wall to wall."
    voice my_audio["47"]
    nar "A neatly made bed sits against one side of the room, opposite a comfortable sofa. A well-built gaming computer rests on a sturdy desk nearby, while six large windows allow the moonlight to spill gently across the floor."
    voice my_audio["48"]
    nar "For someone expecting nothing more than a place to sleep, this feels less like a guest room... and more like a place someone actually cared enough to make feel like home."
    jump pare

label upstairsexaddict:

    scene black
    with slowfade

    pause 2.0

    $ memory_marnie_contact_added = True
    $ show_tooltip(n=4)


    scene a84
    with slowfade

    voice my_audio["56"]
    nar "Before you can head upstairs, a familiar feeling stops you, the quiet certainty that someone has been watching."
    voice my_audio["57"]
    nar "You've always noticed things other people miss: a faint movement, a shifted shadow, the smallest change in the air when someone tries too hard to remain still."
    voice my_audio["58"]
    nar "Whoever it was, had been watching your interaction with Marnie from the beginning."
    voice my_audio["60"]
    nar "Well, never the matter. Anyway, you stand at the foot of the staircase for a quiet moment, your eyes slowly following each step until they disappear into the darkness above."
    voice my_audio["35"]
    nar "It's been one hell of a day. A stranger's home. A marriage hanging together by old scars. A woman named Marnie your father somehow trusted enough to send you here."
    voice my_audio["36"]
    nar "Nothing about tonight makes sense... but if your father believed this was where your journey had to begin, then for now, all you can do is keep moving."

    scene a85
    with medium_dissolve

    voice my_audio["37"]
    nar "Your thoughts drift back to the hospital. The steady beeping of machines. The smell of disinfectant. Your father lying unconscious, unable to explain any of this himself."
    voice my_audio["38"]
    nar "All he left behind was a name... an address... and the hope that coming here would answer questions he no longer could."
    voice my_audio["39"]
    nar "You don't know whether this house holds the answers you're looking for or simply more questions. Either way, turning back now isn't an option."

    scene black
    with slowfade
    play sound my_audio["stairs2"] noloop

    pause 2.0

    scene a86
    with slowfade

    voice my_audio["40"]
    nar "You make your way upstairs, each step creaking softly beneath your feet."
    voice my_audio["41"]
    nar "At the top of the landing, just as Henry described, a door waits on your left. This must be the room."
    stop sound fadeout 1.0

    scene a87
    with medium_dissolve

    voice my_audio["42"]
    nar "You pause outside the door and press an ear against it, listening carefully."
    voice my_audio["43"]
    nar "Silence."
    voice my_audio["44"]
    nar "Not a television. Not footsteps. Not even the sound of someone breathing. Whoever stayed here before you, if anyone ever did, certainly isn't inside now."
    voice my_audio["45"]
    nar "Satisfied, you wrap your hand around the doorknob, quietly push the door open, and step inside."
    jump goinside


label upstairs1:

    scene black
    with slowfade

    pause 2.0

    $ memory_marnie_contact_added = True
    $ show_tooltip(n=4)


    scene a84
    with slowfade

    voice my_audio["56"]
    nar "Before you can head upstairs, a familiar feeling stops you, the quiet certainty that someone has been watching."
    voice my_audio["57"]
    nar "You've always noticed things other people miss: a faint movement, a shifted shadow, the smallest change in the air when someone tries too hard to remain still."
    voice my_audio["58"]
    nar "Whoever it was, had been watching your interaction with Marnie from the beginning."
    voice my_audio["59"]
    nar "Strangely, you sensed no hostility from them. If anything, they seem pleased by the kindness you showed her."
    voice my_audio["60"]
    nar "Well, never the matter. Anyway, you stand at the foot of the staircase for a quiet moment, your eyes slowly following each step until they disappear into the darkness above."
    voice my_audio["35"]
    nar "It's been one hell of a day. A stranger's home. A marriage hanging together by old scars. A woman named Marnie your father somehow trusted enough to send you here."
    voice my_audio["36"]
    nar "Nothing about tonight makes sense... but if your father believed this was where your journey had to begin, then for now, all you can do is keep moving."

    scene a85
    with medium_dissolve

    voice my_audio["37"]
    nar "Your thoughts drift back to the hospital. The steady beeping of machines. The smell of disinfectant. Your father lying unconscious, unable to explain any of this himself."
    voice my_audio["38"]
    nar "All he left behind was a name... an address... and the hope that coming here would answer questions he no longer could."
    voice my_audio["39"]
    nar "You don't know whether this house holds the answers you're looking for or simply more questions. Either way, turning back now isn't an option."

    scene black
    with slowfade
    play sound my_audio["stairs2"] noloop

    pause 2.0

    scene a86
    with slowfade

    voice my_audio["40"]
    nar "You make your way upstairs, each step creaking softly beneath your feet."
    voice my_audio["41"]
    nar "At the top of the landing, just as Henry described, a door waits on your left. This must be the room."
    stop sound fadeout 1.0

    scene a87
    with medium_dissolve

    voice my_audio["42"]
    nar "You pause outside the door and press an ear against it, listening carefully."
    voice my_audio["43"]
    nar "Silence."
    voice my_audio["44"]
    nar "Not a television. Not footsteps. Not even the sound of someone breathing. Whoever stayed here before you, if anyone ever did, certainly isn't inside now."

    scene x43
    with medium_dissolve

    voice my_audio["61"]
    nar "You nearly start to reach for the door when that familiar feeling returns. A quiet pressure at the back of your neck."
    voice my_audio["62"]
    nar "Someone is watching you."
    voice my_audio["63"]
    nar "Not merely passing by, either. Whoever it is has been studying you long enough to see how you treated Marnie."

    scene x44
    with medium_dissolve
    play music my_audio["sneaky4"] loop fadein 2.0

    voice my_audio["64"]
    nar "You turn and find a woman watching from another doorway."
    voice my_audio["65"]
    nar "Her glasses catch what little light reaches the hallway, but they do nothing to hide the interest in her eyes."
    voice my_audio["66"]
    nar "She doesn't look embarrassed at being caught. If anything, she looks pleased that you finally noticed her."

    scene x45
    with medium_dissolve

    voice my_audio["67"]
    nar "She steps further into view, and for a moment, your thoughts become considerably less organised."
    voice my_audio["68"]
    nar "She is beautiful, confident, and very aware of the effect she has on you. And my God.....those fucking tits."
    voice my_audio["69"]
    nar "Then she smiles and motions towards the room behind her. No words are needed. The invitation is perfectly clear."

    scene x46
    with medium_dissolve

    voice my_audio["70"]
    nar "Careful."
    voice my_audio["71"]
    nar "You don't know this woman. You don't know why she was watching you, and you certainly don't know what she wants."
    voice my_audio["72"]
    nar "Your own room is right there. You could open the door, step inside, and put this entire situation behind you."

    scene x47
    with medium_dissolve

    voice my_audio["73"]
    nar "That's right, don't look at her."
    voice my_audio["74"]
    nar "Open your door. Go inside. Close it behind you. A simple three-step plan with very little chance of ruining your life."
    voice my_audio["75"]
    nar "Every useful instinct you possess is telling you to stay away from that woman. Unfortunately, curiosity has never been known for listening."

    menu:
        "*Accept her silent invitation and follow her into the room.*":




            voice my_audio["76"]
            nar "Exactly! Go into your room and-........wait, what? No! No, no, no, don't do THAT!"
            voice my_audio["77"]
            nar "Of course. You ignore every warning and choose the mysterious woman instead."
            voice my_audio["78"]
            nar "Should I be surprised? All they need is a pair of giant milkers and you're ready to follow anyone into the abyss! And here I thought you were ready to remain a decent guy, instead of fucking yourself."
            voice my_audio["79"]
            nar "Without saying a word, you accept the mysterious, definately not going to kill you, sexy big-titted woman into her room. Against your greater concince I might add."
            stop narration
            jump jennifer1
        "*Take the hint, ignore her, and go into your own room.*":


            voice my_audio["104"]
            nar "Oh, thank God. A sensible decision."
            voice my_audio["105"]
            nar "You break eye contact, enter your room, and close the door before curiosity can change your mind."

            $ memory_jennifer_resisted = True
            jump goinside
        "*Absolutely not. If she wants to meet you, she can do it as normal person. Walk up to you, shake your hand, and say hello.*":


            voice my_audio["106"]
            nar "Excellent. Distance is a fine defence against beautiful women with huge tits and suspicious smiles."
            voice my_audio["107"]
            nar "You turn away from her invitation and remove yourself from the situation entirely."

            $ memory_jennifer_resisted = True
            jump goinside



    scene black
    with slowfade

    pause 2.0

    scene a88
    with slowfade

    nar "The room is far nicer than you expected. Spacious, clean, and surprisingly modern, with polished hardwood floors stretching from wall to wall."
    nar "A neatly made bed sits against one side of the room, opposite a comfortable sofa. A well-built gaming computer rests on a sturdy desk nearby, while six large windows allow the moonlight to spill gently across the floor."
    nar "For someone expecting nothing more than a place to sleep, this feels less like a guest room... and more like a place someone actually cared enough to make feel like home."
    jump pare

label pare:

    menu:
        "*Prepare for bed*.":



            if good or supergood:
                jump marnie2nd
            else:
                jump henrymarniebed
        "*Do nothing.*":

            mc "......."
            mc ".........."
            mc ".............."
            jump pare
        "*Just stand here.*":

            mc "......."
            mc ".........."
            mc ".............."
            jump pare

label henrymarniebed:



    if good or supergood:
        jump marnie2nd

    scene black
    with slowfade
    if evil:
        play music my_audio["think2evil"] loop
    else:
        play music my_audio["think2"] loop

    pause 3.0

    scene a90
    with slowfade

    sec "Oooh yeah Marnie, that's hott!"
    sec "Fuck! I would come over there right now and grab you by the neck!"
    sec "Choke you and fuck your brains out all over that bed!"

    scene a91
    with medium_dissolve

    mar "Oh gosh...stop. You wouldn't do that!"
    sec "I would, in fact, I'd fuck you all over that house!"
    sec "I'd fuck you in front of your daughters too! How's that sound!?"
    mar "Well, I don't know if they would want to watch us fuck. Well, maybe Jennifer would, but."
    sec "Oh yeah, that fucking hott slut Jennifer would gladly watch us fuck!"
    sec "Erm....anyway, let's do some more exercises. Are you ready?"
    mar "Yes! I'm ready! Let's start!"
    sec "Good."

    scene mctongue
    with medium_dissolve

    call godson_locked_cutscene ("gui/mctongue.webm", 14.0, "seen_mctongue") from _call_godson_locked_cutscene_2

    play sound my_audio["bang sound 1"] noloop
    scene a96
    with hpunch

    hen "Marnie... what the hell am I listening to right now?"
    hen "Every time you're on one of these calls, it sounds less like therapy and more like the two of you are having sex."
    hen "I'm trying to read my book over here, and all I can hear is you two. It's fucking distracting."

    scene a97
    with medium_dissolve

    mar "Oh, Henry, would you relax? It's perfectly normal. He's my sex therapist, you know this. He's having me role-play different situations so we can work through things."
    mar "It's not nearly as scandalous as you're making it out to be. Honestly, if you listened to the whole conversation instead of the odd sentence here and there, you'd know that."
    hen "Maybe... but from where I'm sitting it sounds fucking ridiculous. Anybody walking past this room would think something completely different was going on."
    hen "I swear, every session sounds stranger than the last. I still don't understand how pretending to fuck each other is supposed to fix anything."
    mar "Because it's helping me understand why I think and behave the way I do. You don't have to understand every part of it, darling... you just have to trust that I'm trying to become a better wife."

    scene a98
    with medium_dissolve

    sec "Who the fuck was that? Was that your stupid fucking husband again?"
    mar "Yes, I'm sorry. You can just ingore him. He doesn't understand this kind of therapy."
    sec "Yeah? Well tell that fucking loser to shut his mouth while I phone-fuck his wife!"
    mar "Oh gosh, don't be so mean! This is just roleplay, after all."

    scene a99
    with medium_dissolve

    sec "Right, roleplay. Well let's continue our phone-fuck roleplay then."
    sec "What do you think about me fucking Jennifer and you at the same time? I wanna fuck that hot slut."
    mar "Um, well.... Jennifer is....she, does her own thing."
    mar "Also, is this part of the roleplay, or?"

    scene a100
    with medium_dissolve

    sec "What about if I fuck you and your mother at the same time?"
    sec "That bitch has got the biggest ass out of all of you. I dream about putting my face in it."
    sec "I'd fuck her, cum in her, then fuck you until I came again."
    sec "Then I'd go to Jennifer's room and fuck her too, then that bitch Lorraine is next."
    mar "Wow, really? You'd fuck my entire family? What about Yuni?"
    sec "I'd fuck her later. That's saving the best for last, heh."

    scene a101
    play sound my_audio["bang sound 1"] noloop
    with hpunch

    hen "Alright! I've had enough! I'm outta here!"

    scene a102
    with medium_dissolve

    mar "......"
    mar ".........."

    scene a103
    with medium_dissolve

    mar "Huh?"
    mar "Henry, where are you going?"
    hen "I can't fucking read while hearing that shit! I'm gonna sleep in the basement, fuck this."

    scene a104
    with medium_dissolve

    mar "Henry, come back to bed. This is silly."
    hen "Fuck that. I'm out. I'm not listening to this."
    hen "I swear, sometimes it feels like I'm not even your husband anymore."
    mar "What? Why would you say that? What's wrong with you?"
    hen "Nothing!"
    hen "Ugh, I'm gone! I'll be in the basement!"
    hen "Bye!"
    jump room223

label insidehouse:

    stop music fadeout 2.0

    scene black
    with slowfade
    play music2 my_audio["apartment4"] loop fadein 2.0

    pause 3.0

    scene a40
    with slowfade

    hen "Alright, let's just see if your little story matches up."
    hen "Keep quiet and don't say anything. I'm still tempted to throw your ass out right now."

    scene a41
    with medium_dissolve

    hen "Marnie!"
    mar "What!?"
    hen "Get in here! You have a visitor!"
    mar "A what!?"
    hen "A visitor! You have a visitor!"

    scene black
    with fade

    pause 2.0

    scene a42
    with fade

    mar "What? What's going on?"
    mar "What are you talking about?"
    jump continue1

label room223:

    stop music fadeout 2.0
    scene black
    with slowfade
    jump room224

label room224:


    if good or supergood:
        jump marnie2nd

    play music my_audio["apartment4"] loop fadein 2.0
    scene a89
    with slowfade



    menu:
        "*Text Marnie.*":



            jump marnie_message_label
        "*Watch Porn*":

            scene black
            with fade
            jump video1
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
