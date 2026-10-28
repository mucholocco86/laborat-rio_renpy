label Episode_12_Start:

    #KoGa3 START#
    $ KoGa3GameProgress = "Ep12"
    #KoGa3 END#

    $ achievement.grant("ACHIEVEMENT_EPISODE_11")
    $ achievement.sync()
    $ Emily_Week5_Thursday_WitnessKissErynn = False
    $ Erynn_Week5_Thursday_FridayBeach = False
    $ Erynn_Week5_Thursday_Shower = False
    $ Erynn_Week5_Thursday_Photo = False
    $ Erynn_Week5_Thursday_SniffPanties = False
    $ Erynn_Week5_Thursday_Handjob = False
    $ Erynn_Week5_Thursday_WashBack = False
    $ Valeria_Week5_Thursday_Headscratches = False
    $ Alexis_Week5_Thursday_BreakUpTalk = False
    $ Valeria_Week5_Thursday_2ndChance = False
    $ Alexis_Week5_Thursday_KissWon = False
    $ Brooke_Week5_Thursday_Peek = False
    $ Brooke_Week5_Thursday_CollegeEmily = False
    $ Brooke_Week5_Thursday_MommyBrooke = False
    $ Brooke_Week5_Thursday_Picture = False
    $ Gabi_Week5_Thursday_Picture = False
    $ Iris_Week5_Thursday_BikeRepair = False
    $ Ximena_Week5_Thursday_Watch = False
    $ Brooke_Week5_Thursday_BikeRide = False
    $ John_Week5_Thursday_BikeRide = False
    $ Ethan_Week5_Thursday_Plan = False
    $ Ethan_Week5_Thursday_Punch = False
    $ Ethan_Week5_Thursday_Phone = False
    $ Gianna_Week5_Thursday_CheckOut = False
    $ Gianna_Week5_Thursday_Domino = False

    if Erynn_LikeMC == True:
        jump Week5_Thursday_Erynn
    else:
        jump Week5_Thursday_Morning

label Week5_Thursday_Erynn:
    scene black with Dissolve(2)
    pause 2
    stop music fadeout 1.0
    play music ("Music/LoFi Indie 3.mp3", "Music/LoFi Indie 1.mp3", "Music/LoFi Indie 2.mp3") volume 0.2
    n "Thursday, 08:53."
    scene 12_001 with Dissolve(1)
    mc "{i}(Man... It's morning already?){/i}"
    mc "{i}(*Sigh* Better get up and get ready to go help at the restaurant.){/i}"
    mc "{i}(I hope it won't be too busy today since it's spring break, but it'll be packed, most likely.){/i}"
    scene 12_002 with Dissolve(1)
    mc "..."
    mc "{i}(What the...?){/i}"
    scene 12_003 with Dissolve(1)
    mc "{i}(Why is she here again?){/i}"
    mc "{i}(I'm not still dreaming, am I?){/i}"
    scene 12_004 with Dissolve(1)
    mc "{i}(She looks so cute!){/i}"
    show 12_005
    pause 3
    mc "..."
    mc "{i}(Her opening her eyes all of a sudden actually scared me a little.){/i}"
    scene 12_006 with Dissolve(1)
    mc "{i}(Why isn't she saying anything?){/i}"
    mc "{i}(Is this really a dream?){/i}"
    menu:
        "Say something":
            scene 12_007 with Dissolve(1)
            mc "Hey?"
            er "Good morning!"
            mc "{i}(Not a dream, I guess.){/i}"
            mc "{i}(Why am I bummed out about this? Isn't this better than a dream?){/i}"
            scene 12_008 with Dissolve(1)
            mc "You are real, right?"
            er "Haha. Yes!"
        "Touch her boobs[KoGa3AutoWTChange1]{size=-4}({i}Alexis DatingFalse: Erynn Points-4{/i}) {/size} {/color}":
            scene 12_009 with Dissolve(1)
            mc "{i}(Sorry, Erynn.){/i}"
            mc "{i}(But trust me. This isn't the worst I've done to you in my dreams.){/i}"
            scene 12_010 with Dissolve(1)
            mc "{i}(Since when do dreams feel this real?){/i}"
            er "..."
            if Alexis_Dating == False:
                scene 12_011 with Dissolve(1)
                er "What are you doing?"
                mc "Uh..."
                mc "They're real..."
                er "Of course, they are real! I didn't get a boobjob!"
                scene 12_012 with Dissolve(1)
                mc "Haha, no. That's not what I meant."
                mc "I thought I was dreaming and..."
                er "The first thing you do in your dreams is grab my boob?"
                mc "Haha. Sorry!"
            else:
                $ Erynn_Points -= 4
                scene 12_013 with Dissolve(1)
                er "What are you doing?"
                mc "Uh..."
                er "You can't just..."
                mc "{i}(Shit! Not a dream!){/i}"
                scene 12_014 with Dissolve(1)
                mc "Sorry, Erynn."
                mc "I didn't expect you to be here and thought I was dreaming and..."
                er "And the first thing you do in your dreams is grab my boob?"
                mc "Sorry..."
            scene 12_015 with Dissolve(1)
            er "You're forgiven."
            mc "Thanks."
    scene 12_016 with Dissolve(1)
    if Alexis_Dating == True:
        mc "Sooo... What are you doing here again? Didn't you have another shoot today?"
        er "Yeah. I'll leave in an hour."
        mc "But first you had to come over and wake me again?"
    else:
        mc "Sooo... What are you doing here again?"
        er "I don't know. I like it here. It calms me down."
        mc "You sure you didn't want to try to wake me again?"
    if Erynn_Week5_Tuesday_Wakeup == True:
        er "No..."
    else:
        er "No... Besides. I succeeded last time, already!"
    scene 12_017 with Dissolve(1)
    er "Okay. To be honest, I wanted to at first."
    er "But then I remembered what happened last time and..."
    mc "Oh... That. Haha."
    scene 12_018 with Dissolve(1)
    mc "You can look again!"
    er "Ah... [mc]!"
    mc "Haha."
    scene 12_019 with Dissolve(1)
    mc "Don't worry. I'm wearing underwear this time."
    er "Good..."
    mc "{i}(Hmm... Is she disappointed?){/i}"
    scene 12_020 with Dissolve(1)
    mc "Why didn't you wake me?"
    er "As I said, I wanted to."
    er "But you were sleeping so peacefully, I just couldn't."
    er "I decided to just lie next to you and watch you sleep. I must have dozed off while..."
    scene 12_021 with Dissolve(1)
    mc "That's creepy!"
    er "No, it's not!"
    mc "It's a little creepy."
    scene 12_022 with Dissolve(1)
    mc "You little creepster!"
    er "Don't call me that!"
    mc "Snoopy!"
    er "Not that either!"
    scene 12_023 with Dissolve(1)
    mc "Rinny."
    er "..."
    scene 12_024 with Dissolve(1)
    mc "Good morning, by the way."
    er "Heh. Good morning."
    if Alexis_Dating == False:
        $ Emily_Week5_Thursday_WitnessKissErynn = True
        $ Erynn_Week5_Thursday_FridayBeach = True
        scene 12_025 with vpunch
        n "*Slap*"
        er "Hey!"
        mc "Obligatory slap!"
        scene 12_026 with Dissolve(1)
        er "..."
        mc "..."
        scene 12_027 with Dissolve(1)
        ""
        scene 12_028 with Dissolve(1)
        ""
        scene 12_029 with Dissolve(1)
        m "Did..."
        m "..."
        scene 12_030 with Dissolve(1)
        m "*Shakes head*"
        scene 12_031 with Dissolve(1)
        m "Hey."
        m "You'll never believe what I just witnessed."
        scene 12_032 with Dissolve(1)
        mc "I'm still thinking about what happened two days ago."
        er "..."
        mc "What?"
        scene 12_033 with Dissolve(1)
        er "Don't remind me!"
        mc "Why not? Didn't you enjoy it?"
        mc "{i}(Is she still embarrassed?){/i}"
        er "I did, but..."
        scene 12_034 with Dissolve(1)
        mc "Too bad you got that phone call and had to leave."
        er "Yeah..."
        mc "{i}(I guess she doesn't really want to talk about it.){/i}"
        mc "{i}(I really would've liked to continue.){/i}"
        mc "Anyway. How was the beach yesterday?"
        scene 12_035 with Dissolve(1)
        er "It was fun!"
        mc "Just you, Alexis, and Iris?"
        er "Uh-huh."
        scene 12_036 with Dissolve(1)
        mc "I wish I could've come."
        er "Sorry. We wanted it to be girls only. That was the only day we all had time."
        mc "It's fine. Just me being selfish, I guess."
        if Alexis_Sex == True:
            mc "{i}(And with Alexis there, it might not have been a good idea.){/i}"
        else:
            pass
        scene 12_037 with Dissolve(1)
        er "But we can go tomorrow, if you want?"
        mc "Just us?"
        er "Yeah."
        mc "Okay. Let's do that."
        scene 12_038 with Dissolve(1)
        er "Let's go in the morning though."
        mc "So you can come and wake me up again?"
        er "I didn't today! But yes!"
        mc "Haha. Sounds great."
        scene 12_039 with Dissolve(1)
        mc "{i}(Does she realise where her hand is right now?){/i}"
        mc "{i}(If you're stroking my leg so close to my crotch...){/i}"
        mc "{i}(Fuck... Guess it'll be time for a shower soon. Very soon.){/i}"
        scene 12_040 with Dissolve(1)
        mc "I'm gonna go shower now and get ready for the restaurant."
        er "..."
        er "*Nods*"
        scene 12_041 with Dissolve(1)
        er "Can I come with you?"
        mc "..."
        mc "{i}(What did she just say? Did she...?){/i}"
        mc "What?"
        scene 12_042 with Dissolve(1)
        mc "You mean...?"
        er "Shower."
        er "Together."
        mc "Uh..."
        menu:
            "Shower alone[KoGa3AutoWTChange1]{size=-4}(Erynn Points-4) {/size} {/color}":
                $ Erynn_Points -= 4
                mc "..."
                scene 12_044 with Dissolve(1)
                mc "I'm sorry, Erynn. I don't think we..."
                er "No, no, it's alright."
                er "It was just a stupid idea. Just forget about it."
                er "I have to go home anyway and get ready for the shoot."
                mc "Yeah..."
                scene 12_045 with Dissolve(1)
                er "We'll see each other tomorrow then?"
                mc "Can't wait."
                mc "{i}(Can't wait? Is it even a good idea to go with her?){/i}"
                mc "{i}(I just don't know anymore.){/i}"
                scene 12_046 with Dissolve(1)
                er "Bye, [mc]."
                mc "Bye, Erynn. See you tomorrow."
                scene 12_047 with Dissolve(1)
                mc "{i}(FUUUUUUUCK!!!){/i}"
                mc "{i}(She's finally opening up and getting comfortable around me and I just keep messing things up.){/i}"
                mc "{i}(Why am I the one hesitating all of a sudden?){/i}"
                jump Week5_Thursday_Run
            "Shower with Erynn[KoGa3AutoWTChange1]{size=-4}(Erynn Week5 Thursday Photo) {/size} {/color}":
                $ Erynn_Week5_Thursday_Photo = True
                jump Week5_Thursday_Erynn_Shower
    else:
        if Alexis_Week5_Wednesday_Beach == False:
            pass
        else:
            scene 12_048 with Dissolve(1)
            mc "Yesterday was fun, right? The beach."
            er "Mm-hmm. We should go together again when we all have time."
            mc "Totally."
            scene 12_049 with Dissolve(1)
            mc "Still hate the fact that you kicked my butt at volleyball though."
            mc "Twenty-one to one... Are you kidding me!"
            er "Haha. Sorry."
            er "We'll make new teams next time."
            scene 12_050 with Dissolve(1)
            mc "But since you're here now, you could've joined us at the club."
            er "I needed my sleep. I can't look tired at the shoot."
            er "Speaking of sleep. You look pretty fit this early. Didn't you stay that long? No hangover?"
            mc "We were there for quite some time. I didn't drink though."
            mc "I told Alexis she could drink and I would drive her home after."
            scene 12_051 with Dissolve(1)
            mc "She was so drunk."
            er "Lex? Yeah, she can drink if she lets loose."
            mc "I've never seen her like that."
            if Alexis_Week5_Wednesday_Club_KissIris == False:
                $ Erynn_Week5_Thursday_Photo = True
            else:
                $ Erynn_Points -= 4
                scene 12_052 with Dissolve(1)
                mc "You'll never believe what happened."
                er "What?"
                mc "She kissed Iris."
                er "What? No?"
                mc "Seriously, she did."
                scene 12_053 with Dissolve(1)
                er "Why? How did that happen?"
                mc "It was sort of a bet to see who the better kisser is."
                mc "So we both kissed Iris and..."
                er "You kissed her too?"
                mc "Uh... Yeah."
                scene 12_054 with Dissolve(1)
                er "..."
                mc "{i}(Maybe I shouldn't have told her that?){/i}"
                mc "{i}(But she would find out anyway.){/i}"
                mc "{i}(Let's quickly change topics...){/i}"
        scene 12_055 with Dissolve(1)
        mc "What's today's photo shoot about?"
        mc "Another campaign for a beauty product, or maybe a clothing line?"
        er "Hmm, I don't know the details yet but it's some kind of fantasy setting."
        mc "Oh? That could be interesting. If I didn't have to work today, I'd love to go see that too."
        if Alexis_Week5_Wednesday_Club_KissIris == False:
            scene 12_056 with Dissolve(1)
            er "If I'm able to, I'll send you a picture of how I look."
            mc "Yeah? That'd be great. Thanks."
            mc "A fantasy setting... What could it be?"
            mc "I'm kinda excited."
            er "Haha. I can see that."
        else:
            pass
        scene 12_057 with Dissolve(1)
        mc "Will Ethan be there?"
        er "I don't know. I haven't heard anything from him since last week."
        er "He doesn't come to photo shoots often, anyway."
        mc "Hmm, alright."
        scene 12_058 with Dissolve(1)
        mc "But on the off-chance that he's there and creating trouble. Call me, okay?"
        er "I will, but it will be fine."
        er "You saw for yourself how many people are at a photo shoot. I'll just stay at the set the whole time."
        scene 12_059 with Dissolve(1)
        er "*Nggh...*"
        er "I think it's time to go home and get ready."
        mc "You would have more time if you didn't come over just to wake me!"
        er "Where's the fun in that?"
        mc "*Shakes head*"
        scene 12_060 with Dissolve(1)
        er "Bye, [mc]."
        mc "Bye, Erynn. And don't come over and wake me tomorrow!"
        scene 12_046 with Dissolve(1)
        er "No promises!"
        mc "..."
        jump Week5_Thursday_Run

label Week5_Thursday_Erynn_Shower:
    $ Erynn_Week5_Thursday_Shower = True
    if _in_replay:
        $ Erynn_Points = 60
    scene 12_061 with Dissolve(1)
    mc "Okay?"
    er "Okay."
    mc "{i}(I don't know what else to say.){/i}"
    mc "{i}(Where...? What? Shit... I can't even think anymore either.){/i}"
    scene black with Dissolve(1)
    pause 2
    scene 12_062 with Dissolve(1)
    mc "I'm gonna take my underwear off now. Just so you know."
    er "..."
    er "I've seen it before..."
    mc "Now it's you've 'seen it before'?"
    scene 12_063 with Dissolve(1)
    mc "But earlier when we were in bed and I lifted the blanket, you..."
    er "Because... That was a different situation."
    mc "You and your 'different situations'."
    er "I've prepared myself now."
    mc "{i}(That's at least one of us. I'm never prepared when I see you naked.){/i}"
    scene 12_064 with Dissolve(1)
    er "..."
    scene 12_065 with Dissolve(1)
    mc "Instead of staring, how about you get naked too?"
    er "I was just about to... And I wasn't staring!"
    mc "You still are!"
    scene 12_066 with Dissolve(1)
    mc "..."
    mc "{i}(For once. Please! Please don't get a hard-on! At least not now!){/i}"
    scene 12_067 with Dissolve(1)
    er "..."
    er "Look who's staring now..."
    mc "Can't I?"
    er "*Nods*"
    mc "{i}(I don't know if it's because she models or because of me that she feels this comfortable taking her clothes off in front of me.){/i}"
    scene 12_068 with Dissolve(1)
    mc "{i}(I just wanna grab her and suck on her boobs again.){/i}"
    mc "{i}(But I don't want to scare her away now.){/i}"
    mc "{i}(This was her idea, so let's see where this is going.){/i}"
    scene 12_069 with Dissolve(1)
    mc "..."
    mc "{i}(Hold out a little longer!){/i}"
    scene black with Dissolve(1)
    transform moveup:
        xalign 0.5 yalign 1.0
        linear 5.0 yalign 0.0
    show 12_070 at moveup
    pause 3
    mc "So beautiful!"
    er "Thanks."
    er "Let's get in the shower now."
    scene 12_071 with Dissolve(1)
    mc "What do you mean, now?"
    mc "You still need to take off your panties."
    er "No. They'll stay on!"
    mc "You can't shower with clothes on. Who does that?"
    scene 12_072 with Dissolve(1)
    mc "Besides. This shower has a strict 'no clothes' rule!"
    er "Where does it say that?"
    mc "It's unwritten!"
    er "Heh."
    scene 12_073 with Dissolve(1)
    mc "So you either take everything off or wait outside."
    er "..."
    mc "{i}(No... Did I just shoot myself in the foot?){/i}"
    mc "{i}(I don't care what she's wearing, I just want her to get in here with me.){/i}"
    mc "Uh... Never mi..."
    scene 12_074 with Dissolve(1)
    er "Turn around!"
    mc "What?"
    er "Turn around! And don't you dare look!"
    mc "{i}(She's actually...?){/i}"
    scene 12_075 with Dissolve(1)
    mc "Go ahead."
    mc "{i}(I don't know what's worse.){/i}"
    mc "{i}(Erynn not joining at all or her getting completely nude and I can't look.){/i}"
    mc "{i}(Man...){/i}"
    scene 12_076 with Dissolve(1)
    er "Kay. I'm ready."
    mc "..."
    mc "{i}(I wanna turn around so badly!){/i}"
    scene 12_077 with Dissolve(1)
    mc "Can I...?"
    er "No!"
    mc "Then how do I know you're naked?"
    scene 12_078 with Dissolve(1)
    er "Here!"
    er "Is this enough proof?"
    mc "Uh..."
    menu:
        "Yes":
            mc "Yeah... I believe you."
        "Sniff her panties[KoGa3AutoWTChange1]{size=-4}(Erynn Week5 Thursday SnfPanties) {/size} {/color}":
            $ Erynn_Week5_Thursday_SniffPanties = True
            scene 12_079 with Dissolve(1)
            mc "Mmm..."
            er "Hey! What are you doing?"
            scene 12_080 with vpunch
            n "*Slaps*"
            mc "Aaah..."
            er "I can't believe you're sniffing my panties!"
            mc "Haha. I had to make sure they're yours."
            scene 12_081 with Dissolve(1)
            er "Of course, they are! Who else's would they be?"
            mc "Maybe you grabbed my mom's panties or something?"
            er "Why would I have Emily's underwear? And why would you smell them if you think they're your mom's?"
            er "Why would you smell mine?"
            mc "Haha. I don't know."
            er "And you said I'm the creep?"
    scene 12_082 with Dissolve(1)
    er "..."
    mc "Just to be sure."
    er "*Shakes head*"
    scene 12_083 with Dissolve(1)
    er "Satisfied?"
    mc "Uh-huh! Feels amazing too!"
    er "Get in the shower already!"
    scene black with Dissolve(1)
    pause 2
    play music "Sounds/Shower.mp3" volume 0.4
    scene 12_084 with Dissolve(1)
    mc "Is the water okay for you or do you want it to be warmer?"
    er "This is fine."
    er "I'll wash your back for you."
    mc "Thanks."
    scene 12_085 with Dissolve(1)
    er "You have really broad shoulders."
    mc "Do I?"
    er "Mm-hmm."
    scene 12_086 with Dissolve(1)
    er "Does it feel good?"
    mc "It's amazing!"
    mc "You can come over every day and wash my back from now on!"
    mc "{i}(Not just my back!){/i}"
    er "Haha."
    scene 12_087 with Dissolve(1)
    er "*Humming*"
    mc "..."
    mc "Enjoying yourself?"
    er "Yeah. I kinda like doing this."
    scene 12_088 with Dissolve(1)
    mc "Heh..."
    er "Is this okay?"
    mc "{i}(It's so cute that she even asks me. You can touch me anywhere you like! Anytime!){/i}"
    mc "Sure, continue."
    scene 12_089 with Dissolve(1)
    mc "I can turn around. That will make it easier for you."
    er "No! You keep facing the wall!"
    mc "*Sigh* Fine..."
    mc "{i}(But I want to look at you!){/i}"
    scene 12_090 with Dissolve(1)
    mc "Uh..."
    er "..."
    scene 12_091 with Dissolve(1)
    er "Sorry. I didn't mean to..."
    mc "{i}(She accidentally touched it and it didn't even take a second to get hard.){/i}"
    mc "{i}(Fuck.){/i}"
    mc "It's fine."
    if Erynn_Points >= 49:
        $ Erynn_Week5_Thursday_Handjob = True
        scene 12_099 with Dissolve(1)
        mc "..."
        mc "{i}(Wait what?){/i}"
        mc "{i}(I hoped for many things, but for this to actually happen...?){/i}"
        mc "{i}(This is happening, right?){/i}"
        scene 12_100 with Dissolve(1)
        er "Can I?"
        mc "{i}(It is!){/i}"
        mc "Yeah..."
        scene 12_101 with Dissolve(1)
        er "Am I grabbing it too hard?"
        mc "No..."
        er "If I'm doing something wrong, tell me, okay?"
        mc "{i}(You're doing so much right, right now.){/i}"
        mc "{i}(Holy shit!){/i}"
        show 12_102
        ""
        show 12_103
        mc "You can go a little faster."
        er "Faster? Uhm... Okay."
        show 12_104
        mc "Yeah, like that."
        scene 12_105 with Dissolve(1)
        mc "{i}(Fuck! This feels so good.){/i}"
        mc "I'm about to..."
        scene 12_106 with vpunch
        pause 2
        scene 12_106 with vpunch
        mc "Ahhh..."
        er "..."
        scene black with Dissolve(1)
        pause 2
        scene 12_107 with Dissolve(1)
        mc "That was amazing, Erynn!"
        er "Happy you've enjoyed it. I didn't know if..."
        mc "No, it was perfect!"
        scene 12_108 with Dissolve(1)
        er "That was also the first time that I..."
        er "You know..."
        scene 12_109 with Dissolve(1)
        er "..."
        er "I asked you not to turn around."
        mc "Sorry, I forgot."
        scene 12_110 with Dissolve(1)
        er "Your... Is..."
        mc "Sorry. Can't help it."
        scene black with Dissolve(1)
        transform moveup:
            xalign 0.5 yalign 1.0
            linear 5.0 yalign 0.0
        show 12_111 at moveup
        pause 3
        mc "{i}(This girl is so perfect!){/i}"
        mc "{i}(The more I think about this, the more it feels like a dream.){/i}"
        mc "{i}(Any moment I'll wake up with wet underwear...){/i}"
        mc "Can I kiss you?"
        er "*Nods*"
        scene 12_112 with Dissolve(1)
        ""
        scene 12_113 with Dissolve(1)
        ""
        scene 12_114 with Dissolve(1)
        mc "{i}(Dream or not. I'm gonna enjoy this as much as I can!){/i}"
        scene 12_115 with Dissolve(1)
        er "Mmm..."
        scene 12_116 with Dissolve(1)
        er "Ah-haha..."
        mc "Hey!"
        er "Hey."
        scene 12_117 with Dissolve(1)
        ""
        scene 12_118 with Dissolve(1)
        er "..."
        scene 12_119 with Dissolve(1)
        mc "{i}(I want her hard nipple in my mouth!){/i}"
        scene 12_120 with Dissolve(1)
        er "Ah..."
        mc "{i}(They taste so great!){/i}"
        scene 12_121 with Dissolve(1)
        ""
        scene 12_122 with Dissolve(1)
        mc "..."
        mc "{i}(She's literally sitting on my dick right now.){/i}"
        scene 12_123 with Dissolve(1)
        mc "{i}(I can actually feel her pussy rubbing against it.){/i}"
        mc "{i}(This feels so good.){/i}"
        mc "{i}(I want to put it inside her so badly.){/i}"
        scene 12_124 with Dissolve(1)
        mc "{i}(If I don't stop now, I'm not sure I'll be able to stop at all.){/i}"
        mc "{i}(I don't know if she wants this.){/i}"
        menu:
            "Continue[KoGa3AutoWTChange1]{size=-4}(Erynn Points-4) {/size} {/color}":
                $ Erynn_Points -= 4
                mc "{i}(But I want it!){/i}"
                scene 12_125 with vpunch
                er "Ahh..."
                mc "Sorry."
                scene 12_126 with Dissolve(1)
                er "..."
                scene 12_127 with Dissolve(1)
                mc "{i}(I can't get enough of her.){/i}"
                scene 12_128 with Dissolve(1)
                er "Uhm... [mc]..."
                er "I'm not... With..."
                er "Can we... Stop...?"
                scene 12_129 with Dissolve(1)
                er "[mc]...?"
                er "Please, stop."
                scene 12_130 with Dissolve(1)
                mc "..."
                mc "{i}(Erynn's pussy...){/i}"
                mc "{i}(I want to taste it too!){/i}"
                scene 12_131 with Dissolve(1)
                er "..."
                er "[mc]..."
                scene 12_132 with vpunch
                er "Stop!"
                mc "..."
                scene 12_133 with Dissolve(1)
                mc "{i}(Shit...){/i}"
                mc "{i}(I pushed it way too far without checking if she was comfortable with all of this.){/i}"
                scene 12_134 with Dissolve(1)
                mc "I'm sorry, Erynn."
                mc "I was so in the moment that I..."
                mc "Sorry..."
                er "It's okay."
                scene 12_135 with Dissolve(1)
                mc "No, it's not okay. I promised you we'd go with your pace."
                mc "So, if it's going too fast or I'm overstepping, tell me, okay?"
                er "*Nods*"
                mc "Or push me away as you did just now. I'm not gonna be mad about that."
                scene 12_136 with Dissolve(1)
                ""
                scene 12_137 with Dissolve(1)
                mc "Let's get out of the shower and dry up."
                er "Yeah."
                scene 12_138 with Dissolve(1)
                er "Can I use this towel?"
                mc "Sure. Go ahead."
                stop music fadeout 1.0
                play music ("Music/LoFi Indie 3.mp3", "Music/LoFi Indie 1.mp3", "Music/LoFi Indie 2.mp3") volume 0.2
            "Stop[KoGa3AutoWTChange1]{size=-4}(Erynn Week5 Thursday WashBack) {/size} {/color}":
                $ Erynn_Week5_Thursday_WashBack = True
                scene 12_139 with Dissolve(1)
                mc "I think we need to stop, or I won't be able to."
                mc "I promised we'd take it slow."
                er "*Nods*"
                scene 12_140 with Dissolve(1)
                mc "Alright. Your turn!"
                er "My turn?"
                mc "I'll wash your back now."
                er "Uhm... Okay?"
                scene 12_141 with Dissolve(1)
                er "..."
                scene 12_142 with Dissolve(1)
                mc "How does this feel?"
                er "Really good!"
                er "Just..."
                mc "What?"
                scene 12_143 with Dissolve(1)
                er "You're poking me."
                mc "Oh... Yeah... Sorry about that."
                scene 12_144 with Dissolve(1)
                mc "{i}(I can't get enough of her.){/i}"
                scene 12_145 with Dissolve(1)
                er "..."
                er "Haha. That tickles!"
                scene 12_146 with Dissolve(1)
                er "I thought you wanted to wash my back?"
                mc "I am!"
                er "Really?"
                mc "Just using a different tool."
                scene 12_147 with Dissolve(1)
                mc "This one works better since you're so dirty."
                er "Dirty... I'm not dirty!"
                er "I showered already before I came here."
                mc "Seems like you missed some spots. Good thing I'm helping you."
                scene 12_148 with Dissolve(1)
                mc "Here! Another missed spot!"
                er "Haha."
                scene 12_149 with Dissolve(1)
                mc "And down here."
                er "*Shakes head*"
                scene 12_150 with Dissolve(1)
                mc "{i}(She has such a great ass.){/i}"
                scene 12_151 with vpunch
                n "*Slap*"
                er "Ahh... Hey!"
                mc "Back's all done!"
                mc "Let's do the front as well. You might've missed some spots there, too."
                scene 12_152 with Dissolve(1)
                er "..."
                mc "..."
                scene 12_153 with Dissolve(1)
                mc "Look how dirty they are!"
                mc "You dirty girl!"
                er "*Shakes head* Having fun?"
                mc "Uh-huh."
                show 12_154
                ""
                scene 12_155 with Dissolve(1)
                er "Okay. That's enough. I won't get cleaner than this."
                mc "You sure?"
                mc "I can do a double-check?"
                er "I'm sure."
                stop music fadeout 1.0
                play music ("Music/LoFi Indie 3.mp3", "Music/LoFi Indie 1.mp3", "Music/LoFi Indie 2.mp3") volume 0.2
                scene 12_156 with Dissolve(1)
                mc "Let's get out of the shower and dry up then."
                er "Yeah."
                scene 12_138 with Dissolve(1)
                er "Can I use this towel?"
                mc "Sure. Go ahead."
        scene 12_157 with Dissolve(1)
        er "What?"
        mc "Nothing. Just watching."
        mc "You're so fucking gorgeous!"
        er "*Shakes head* Heh..."
        scene 12_158 with Dissolve(1)
        er "Okay, you can stop now."
        er "Go to your room and wait there."
        mc "I have to dry up too!"
        scene 12_159 with Dissolve(1)
        er "Here. Take this towel then."
        er "I'll be right there."
        mc "*Sigh* Fine..."
        scene 12_160 with Dissolve(1)
        mc "I'll be in my room then."
        er "Give me two minutes."
        mc "Hah. Two minutes..."
        scene 12_161 with Dissolve(1)
        mc "..."
        scene 12_162 with vpunch
        n "*Slap*"
        er "Aaah!"
        mc "Ultimate-double-slap!"
        er "[mc]!"
        mc "Haha."
        $ renpy.end_replay()
        scene 12_163 with Dissolve(1)
        mc "Haha."
        mc "{i}(That was so much fun!){/i}"
        scene 12_164 with Dissolve(1)
        m "..."
        n "Uhm... Honey..."
        scene 12_165 with Dissolve(1)
        mc "MOM!"
        scene 12_166 with Dissolve(1)
        mc "What are you doing in my room?"
        m "I just put your t-shirts that I washed on your bed."
        mc "..."
        scene 12_167 with Dissolve(1)
        m "Don't worry about it."
        m "It's nothing I haven't seen before."
        mc "Yeah. Fifteen years ago!"
        m "It wasn't that long."
        scene 12_168 with Dissolve(1)
        m "I... I meant the time, not your..."
        mc "MOM! Are you fucking kidding me?"
        m "Haha. Sorry."
        scene 12_169 with Dissolve(1)
        m "Hey. You've seen me naked too. We used to bathe together and..."
        mc "You're making it worse now!"
        mc "Can you please just leave?"
        m "Sorry, sorry. I'm going."
        scene 12_170 with Dissolve(1)
        if MC_Bike == False:
            m "Oh, by the way. We'll leave in twenty minutes, okay?"
            mc "Yeah. I'll be ready."
        else:
            m "Oh, by the way. Are you coming with me, or...?"
            mc "I'll take the bike."
            m "Okay. Be careful!"
            mc "I will."
        scene 12_171 with Dissolve(1)
        mc "*Whimpering*"
        mc "{i}(Why does this keep on happening?){/i}"
        scene 12_172 with Dissolve(1)
        er "What are you doing?"
        er "And why are you still naked? Don't you need to get ready?"
        mc "..."
        scene 12_173 with Dissolve(1)
        er "[mc]? Are you sleeping?"
        mc "*Mumbles*"
        er "What?"
        mc "My mom just saw me naked."
        scene 12_174 with Dissolve(1)
        er "Okay? She's your mom. She's seen you naked many times."
        mc "When I was a baby, yeah..."
        er "Later, too."
        mc "She said the same... And how do you even know that?"
        mc "This is even more embarrassing now."
        scene 12_175 with Dissolve(1)
        er "Why is that embarrassing? She's your mom."
        mc "Exactly why! Wouldn't you be if your mom saw you like that?"
        er "She's seen me naked many times."
        er "We even go to the sauna together."
        scene 12_176 with Dissolve(1)
        mc "That was a bad example. It's different..."
        mc "Let's say your dad saw you naked."
        er "..."
        er "I get your point. I wouldn't want that."
        mc "See!"
        scene 12_177 with Dissolve(1)
        er "Go put some clothes on now, before someone else sees you naked."
        mc "Haha, yeah."
        mc "I really need to lock my door so no one can just randomly enter."
        er "What? No! Or you should give me a key."
        mc "Haha."
        jump Week5_Thursday_Erynn_End
    else:
        scene 12_092 with Dissolve(1)
        er "You can do that part yourself!"
        mc "..."
        mc "{i}(How I wish she would just continue.){/i}"
        scene black with Dissolve(1)
        pause 2
        scene 12_093 with Dissolve(1)
        er "There. My part is done."
        mc "Thank you very much, Erynn. It felt amazing!"
        er "You're welcome."
        scene 12_094 with Dissolve(1)
        er "I'll let you finish... Showering..."
        mc "You can stay if you want."
        er "I'll just wait in your room."
        scene 12_095 with Dissolve(1)
        er "..."
        mc "..."
        scene 12_096 with Dissolve(1)
        mc "{i}(I wish she would just stay in here!){/i}"
        scene 12_097 with Dissolve(1)
        er "Hey! I told you not to turn around and look!"
        mc "You looked too!"
        scene 12_098 with Dissolve(1)
        er "I'll use this towel here."
        mc "Sure. Go ahead."
        er "Don't take too long, I have to go in ten minutes."
        mc "I'll be quick."
        mc "{i}(It will be so quick!){/i}"
        stop music fadeout 1.0
        play music ("Music/LoFi Indie 3.mp3", "Music/LoFi Indie 1.mp3", "Music/LoFi Indie 2.mp3") volume 0.2
        $ renpy.end_replay()
        jump Week5_Thursday_Erynn_End

label Week5_Thursday_Erynn_End:
    scene black with Dissolve(1)
    pause 2
    scene 12_178 with Dissolve(1)
    mc "What's today's photo shoot about?"
    mc "Another campaign for a beauty product, or maybe a clothing line?"
    er "Hmm, I don't know the details yet but it's some kind of fantasy setting."
    mc "Oh? That could be interesting. If I didn't have to work today, I'd love to go see that too."
    scene 12_179 with Dissolve(1)
    er "If I'm able to, I'll send you a picture of how I look."
    mc "Yeah? That'd be great. Thanks."
    mc "A fantasy setting... What could it be?"
    mc "I'm kinda excited."
    er "Haha. I can see that."
    scene 12_180 with Dissolve(1)
    mc "Will Ethan be there?"
    er "I don't know. I haven't heard anything from him since last week."
    er "He doesn't come to photo shoots often, anyway."
    mc "Hmm, alright."
    scene 12_181 with Dissolve(1)
    mc "But on the off-chance that he's there and creating trouble. Call me, okay?"
    er "I will, but it will be fine."
    er "You saw for yourself how many people are at a photo shoot. I'll just stay at the set the whole time."
    scene 12_182 with Dissolve(1)
    er "*Nggh...*"
    er "Speaking of the photo shoot. I think I'd better go home now and get ready."
    er "And now I'll have to hurry."
    scene 12_183 with Dissolve(1)
    mc "You would have more time if you didn't come over just to wake me!"
    mc "{i}(Not just wake me!){/i}"
    er "Where's the fun in that?"
    mc "*Shakes head*"
    scene 12_184 with Dissolve(1)
    er "Bye, [mc]."
    mc "Bye, Erynn. And don't forget to come over tomorrow!"
    mc "I shower daily! Some days multiple times!"
    er "Haha."
    scene 12_185 with Dissolve(1)
    er "No promises!"
    mc "..."
    scene 12_186 with Dissolve(1)
    er "Bye-bye."
    er "See you tomorrow!"
    scene 12_187 with Dissolve(1)
    er "Ahh..."
    er "Did you forget something?"
    scene 12_188 with vpunch
    er "Aaah-haha."
    mc "Did you really think I'd let you go just like that?"
    scene 12_189 with Dissolve(1)
    er "You won't?"
    mc "*Shakes head*"
    er "..."
    scene 12_190 with Dissolve(1)
    er "Aaah..."
    scene 12_191 with Dissolve(1)
    ""
    scene 12_192 with Dissolve(1)
    ""
    scene 12_193 with Dissolve(1)
    er "I liked that!"
    mc "There's one more thing."
    er "Yeah?"
    scene 12_194 with vpunch
    n "*Slap*"
    er "Ahhh!"
    er "[mc]!"
    scene 12_195 with Dissolve(1)
    er "I knew it. I so knew it!"
    er "I shouldn't have asked. And don't say obligatory! You used that one already!"
    mc "Haha."
    scene 12_196 with Dissolve(1)
    er "Okay. I'm going now."
    mc "That ass though."
    er "Stop looking at it!"
    mc "Never!"
    scene 12_197 with Dissolve(1)
    mc "Don't look like that or I'll grab you again and I won't let you leave!"
    er "..."
    jump Week5_Thursday_Restaurant

label Week5_Thursday_Morning:
    scene black with Dissolve(2)
    pause 2
    stop music fadeout 1.0
    play music ("Music/LoFi Indie 3.mp3", "Music/LoFi Indie 1.mp3", "Music/LoFi Indie 2.mp3") volume 0.2
    if Layla_Week5_Wednesday_LikeElenaKnow == True:
        scene 12_198 with Dissolve(1)
        n "*Beep-beep-beep*"
        mc "{i}(It's already time? Damn...){/i}"
        mc "{i}(I slept so bad. I just couldn't get Layla out of my mind.){/i}"
        scene 11_2529 with Dissolve(1)
        mc "{i}(Her face...){/i}"
        mc "{i}(That will haunt me for a while.){/i}"
        scene 12_198a with Dissolve(1)
        mc "{i}(It was the correct decision though, right?){/i}"
        mc "{i}(Maybe I should've thought about it a little more. But then we... Fuck!){/i}"
        scene 12_199 with Dissolve(1)
        mc "Ngggh..."
        mc "{i}(I'd better go run for a bit.){/i}"
        mc "{i}(I might be able to forget about this. For a while at least.){/i}"
    else:
        scene 12_198 with Dissolve(1)
        n "*Beep-beep-beep*"
        mc "{i}(Right... I wanted to go for a run before I have to go work at the restaurant.){/i}"
        scene 12_199 with Dissolve(1)
        mc "Ngggh..."
        mc "{i}(Why did I decide to do that? I'll be on my feet the whole day, anyway.){/i}"
        mc "..."
        mc "{i}(I'm awake now...){/i}"
    jump Week5_Thursday_Run

label Week5_Thursday_Run:
    scene black with Dissolve(1)
    pause 2
    stop music fadeout 1.0
    play music "Sounds/Park.mp3" volume 0.5
    scene 12_200 with Dissolve(1)
    mc "{i}(It's so nice and quiet here this early.){/i}"
    mc "{i}(Got the whole park to myself.){/i}"
    mc "..."
    scene 12_201 with Dissolve(1)
    mc "{i}(Except for that one girl over there.){/i}"
    mc "{i}(Wait... Is that...?){/i}"
    scene black with Dissolve(1)
    transform moveup:
        xalign 0.5 yalign 1.0
        linear 5.0 yalign 0.0
    show 12_202 at moveup
    pause 3
    mc "{i}(Valeria!){/i}"
    if Layla_End == True:
        scene 12_203 with Dissolve(1)
        mc "Hey."
        va "Hey..."
        mc "Long time no see."
        scene 12_204 with Dissolve(1)
        va "..."
        mc "..."
        scene 12_205 with Dissolve(1)
        mc "Look. I know why Layla doesn't wanna talk to me."
        mc "But I didn't do anything wrong to you."
        va "I'm Layla's friend."
        mc "Aren't you mine too?"
        va "..."
        scene 12_206 with Dissolve(1)
        mc "The thing I did was... terrible. I didn't know they were sisters though."
        va "Oh, come on!"
        mc "At least at first. And when I found out, it was already too late."
        va "It's never too late. You could... Should have made a decision at training camp or even before."
        scene 12_207 with Dissolve(1)
        mc "I tried! I had feelings for both of them. It wasn't easy."
        va "But it was easy to hook up with both?"
        mc "..."
        va "I don't wanna talk about that right now. I want to finish my training."
        scene 12_208 with Dissolve(1)
        mc "Are we really gonna be like this for the rest of the school year?"
        va "I don't know."
        mc "..."
        scene 12_209 with Dissolve(1)
        va "Bye."
        mc "Yeah... Bye."
        scene 12_210 with Dissolve(1)
        mc "{i}(I really need to find a way to fix my friendships with all of them.){/i}"
        mc "{i}(I don't wanna spend my senior year like this. But how?){/i}"
        jump Week5_Thursday_Restaurant
    else:
        scene 12_211 with Dissolve(1)
        mc "And here I thought I had this whole park to myself."
        mc "But I should have known that little Miss Try-hard would be here too. Stalking me!"
        va "Little Miss Try-hard? Heh... And stalking you?"
        va "I was here first, brave Sir [mc]."
        mc "Haha."
        scene 12_212 with Dissolve(1)
        mc "Hey. Good morning, Val."
        va "Good morning, [mc]."
        if Valeria_LikeMC == False:
            va "How are ya?"
            scene 12_214 with Dissolve(1)
            mc "Still sleepy. Normally I wake up a little later, but because I have to work today, I had to get up a bit earlier."
            mc "How are you?"
            va "I'm good."
        else:
            scene 12_213 with Dissolve(1)
            va "How are ya?"
            scene 12_214 with Dissolve(1)
            mc "Still sleepy. Normally I wake up a little later, but because I have to work today, I had to get up a bit earlier."
            mc "How are you?"
            va "I'm good."
            mc "You look good."
            va "Heh. Thanks."
        scene 12_215 with Dissolve(1)
        mc "Do you always run in those outfits? 'Cause if you do, I'll be here every day."
        va "Haha, I don't. These clothes are from my sponsorship. I'm testing them out."
        mc "Wow. You even have sponsors. That's great."
        va "Yeah."
        if Valeria_LikeMC == False:
            pass
        else:
            scene 12_216 with Dissolve(1)
            mc "They look great, at least."
            va "Thanks. I like them too."
        scene 12_217 with Dissolve(1)
        mc "Wanna sit down for a bit, or do you...?"
        va "No, I could use a little break."
        if Valeria_LikeMC == False:
            pass
        else:
            scene 12_218 with Dissolve(1)
            mc "{i}(They really do look great!){/i}"
            scene 12_219 with Dissolve(1)
            va "Hmm?"
            mc "What?"
            va "I thought you said something."
            mc "{i}(I didn't say that out loud, right? It wouldn't be the first time.){/i}"
        scene 12_220 with Dissolve(1)
        mc "Do you always come to this park to train, or...?"
        va "No, I switch it up."
        va "Sometimes here, sometimes I run at the boardwalk or in the city."
        va "That way I can explore the area a bit as well."
        if Valeria_LikeMC == False:
            pass
        else:
            scene black with Dissolve(1)
            transform moveup:
                xalign 0.5 yalign 1.0
                linear 5.0 yalign 0.0
            show 12_221 at moveup
            pause 3
            mc "{i}(I would explore you, too!){/i}"
            scene 12_222 with Dissolve(1)
            mc "..."
            scene 12_223 with Dissolve(1)
            va "Spacing out again?"
            mc "Sorry. I was just thinking about... yesterday."
            mc "The beach. Your shirt..."
            va "Mmh... Yeah..."
        if Alexis_Week5_Wednesday_Beach == False:
            if Alexis_Week5_Wednesday_Beach_SP == False:
                if Valeria_LikeMC == False:
                    scene 12_224 with Dissolve(1)
                    mc "What have you been doing the last couple of days?"
                    va "Not that much, to be honest. Mostly training."
                    va "Went to the beach yesterday with Tori and co."
                    scene 12_225 with Dissolve(1)
                    mc "That's fun. I mean the beach. Tori and co., not that much. That means Darryl, right?"
                    va "Haha. Yeah, he was there too. Also Jasmine and TJ."
                    mc "How was it?"
                    scene 12_226 with Dissolve(1)
                    va "As you said. Not that much fun. Quite boring actually. No one went into the ocean."
                    va "Tori and Jasmine were just lying on the beach the whole afternoon."
                    va "Darryl and TJ were throwing a football back and forth. I played a little with them, but that's about it."
                    scene 12_227 with Dissolve(1)
                    va "Also. Darryl kept hitting on me. Which was awkward. Especially since Tori was there too."
                    va "At some point, he lay on top of me. I wanted to kick him so badly."
                    va "But since we were at the beach, with all the other people around. I didn't want to make a scene."
                    mc "I would've kicked him!"
                    va "Yeah. Maybe I should've."
                    scene 12_228 with Dissolve(1)
                    mc "So Darryl has a thing for you, huh?"
                    va "I'm not entirely blameless. I flirted too, before."
                    mc "Oh... You're interested in Darryl then?"
                    scene 12_229 with Dissolve(1)
                    va "I think he's attractive, but I wouldn't go there with him."
                    mc "Because of Tori?"
                    va "No, in general. Not my type. Personality wise."
                    va "We're friends and he's a teammate and we do flirt a bit, but that's about it."
                    mc "Is there anyone at school you're interested in?"
                    if Valeria_Points >= 18:
                        scene 12_230 with Dissolve(1)
                        va "There might be someone. We'll see."
                        mc "I'm so curious right now. You're not going to tell me who it is?"
                        va "No."
                        mc "It's not Zach, right?"
                        va "No. Also just a friend."
                        scene 12_231 with Dissolve(1)
                        mc "Is it me?"
                        va "..."
                        va "Yeah. Totally."
                        mc "Haha. Just a friend. I get it."
                    else:
                        scene 12_230 with Dissolve(1)
                        va "Hmm, no. I haven't been looking either. I'm too busy to be in a relationship anyway."
                        mc "How about Zach?"
                        va "How about no!"
                        mc "Haha."
                    if Layla_Week5_Wednesday_LikeElenaKnow == False:
                        scene 12_232 with Dissolve(1)
                        va "We should go to the beach next time."
                        va "Together with Layla and Elena."
                        va "That should be much more fun."
                        if Layla_Dating == True:
                            scene 12_232 with Dissolve(1)
                            mc "We can do that. Layla owes me a beach date, anyway."
                            va "Great!"
                        else:
                            mc "We can do that."
                            va "Great!"
                        scene 12_243 with Dissolve(1)
                        va "Come on. Enough sitting around. Let's do a few more laps."
                        mc "Sure."
                        scene 12_282 with Dissolve(1)
                        ""
                    else:
                        scene 12_233 with Dissolve(1)
                        va "We should go to the beach next time."
                        va "Together with Layla and Elena."
                        va "That should be much more fun."
                        scene 12_234 with Dissolve(1)
                        mc "About that. I don't think it will happen in the near future."
                        va "What? Why?"
                        mc "Uhm... *Sigh* You're going to find out anyway."
                        scene 12_235 with Dissolve(1)
                        mc "Layla and I kinda broke up, I guess."
                        va "You...? What?"
                        mc "Yeah..."
                        va "What happened?"
                        scene 12_236 with Dissolve(1)
                        mc "She... Uhm... Wanted more...?"
                        mc "And I wasn't too sure because..."
                        mc "*Sigh* There's someone else on my mind."
                        scene 12_237 with Dissolve(1)
                        va "Elena?"
                        mc "What...? How...? How do you know?"
                        va "The way you look at her."
                        mc "Is it that obvious?"
                        va "To me, yes."
                        scene 12_238 with Dissolve(1)
                        mc "I'll spare you the details, but I don't think she wants to talk to me."
                        mc "At least for some days, or maybe weeks."
                        va "Does she know you like Elena?"
                        mc "I told her."
                        scene 12_239 with Dissolve(1)
                        va "So there will be talks between the two as well."
                        mc "Oh shit... I hadn't even thought about that."
                        mc "I hope I haven't ruined their friendship as well, now."
                        mc "What a mess."
                        scene 12_240 with Dissolve(1)
                        mc "This is so much worse than I thought."
                        va "It will take some time, but it will be alright."
                        mc "I hope so."
                        scene 12_241 with Dissolve(1)
                        mc "I wanted to go for a run this morning to clear my head."
                        mc "But here I am, still thinking about that situation."
                        va "Sorry."
                        mc "It's not your fault."
                        scene 12_242 with Dissolve(1)
                        va "Come on. Let's go run, then."
                        mc "Sure."
                else:
                    scene 12_244 with Dissolve(1)
                    va "I told you to forget about that!"
                    mc "Like that's gonna happen."
                    mc "Even if I try, it's just... impossible."
                    va "..."
                    scene 12_245 with Dissolve(1)
                    mc "How was your date with Darryl? Did you go?"
                    va "I did go, yes. And it wasn't a date! We went with a few people!"
                    mc "Did you have fun?"
                    va "No..."
                    scene 12_246 with Dissolve(1)
                    mc "Haha. No?"
                    va "..."
                    mc "Sorry. I didn't mean to laugh."
                    mc "{i}(But I'm still happy about that.){/i}"
                    scene 12_247 with Dissolve(1)
                    mc "Did something happen?"
                    va "It was just boring. No one went into the ocean."
                    va "Tori and Jasmine were just lying on the beach the whole afternoon."
                    va "Darryl and TJ were throwing a football back and forth. I played a little with them, but that's about it."
                    scene 12_227 with Dissolve(1)
                    va "Also. Darryl kept hitting on me. Which was awkward. Especially since Tori was there too."
                    va "At some point, he lay on top of me. I wanted to kick him so badly."
                    mc "{i}(What?){/i}"
                    va "But since we were at the beach, with all the other people around. I didn't want to make a scene."
                    mc "I would've kicked him!"
                    va "Yeah. Maybe I should've."
                    scene 12_248 with Dissolve(1)
                    mc "I'll still kick him for you, if you want me to."
                    va "Haha. It's fine. But thanks for offering."
                    mc "Anytime. I still owe you a kick!"
                    va "Haha, you do."
                    scene 12_249 with Dissolve(1)
                    va "You should've just joined us."
                    va "We didn't have to stay with them, but could've done our own thing."
                    mc "{i}(Now I think about it, I should've gone.){/i}"
                    mc "{i}(Spending more time with Val and seeing Darryl's face when I flirt with her. Damn...){/i}"
                    mc "You're right."
                    scene 12_250 with Dissolve(1)
                    mc "Let's go together next time, then."
                    va "Sure."
                    mc "Sure? Not maybe?"
                    va "Not a maybe."
                    scene 12_251 with Dissolve(1)
                    va "How about tomorrow? I have to be somewhere in the afternoon, but we can go in the morning?"
                    mc "Uhm, yeah... Let's do that."
                    va "Cool."
                    scene 12_252 with Dissolve(1)
                    mc "I promise you. It will be much more fun this time!"
                    va "Looking forward to it."
                    scene 12_253 with Dissolve(1)
                    mc "Do we need to go shopping first?"
                    va "I don't think so. Why?"
                    mc "Maybe you need to test some more swimsuits."
                    scene 12_254 with Dissolve(1)
                    va "I actually bought the one..."
                    mc "You did? The one from the pictures?"
                    va "Uh-huh."
                    mc "Can't wait for tomorrow now. It's gonna be amazing!"
                    scene 12_255 with Dissolve(1)
                    mc "..."
                    scene 12_256 with Dissolve(1)
                    va "Come. Let's finish our morning run with a few more laps."
                    mc "Heh..."
                    va "What?"
                    mc "I thought you were going to kiss me for a second."
                    va "Who said I wasn't?"
                    scene 12_257 with Dissolve(1)
                    ""
                    scene 12_258 with Dissolve(1)
                    mc "{i}(It's crazy how much I get turned on by a simple kiss.){/i}"
                    scene 12_259 with Dissolve(1)
                    mc "{i}(Well... I wouldn't call this a simple kiss. She really knows how to work her tongue.){/i}"
                    scene 12_260 with Dissolve(1)
                    mc "..."
                    scene 12_261 with Dissolve(1)
                    mc "You really like your licking, huh?"
                    va "Ever since I licked your face at training camp, I just..."
                    va "I don't know. Yeah... I like it."
                    mc "You can lick me anytime, anywhere you want!"
                    va "..."
                    scene 12_243 with Dissolve(1)
                    va "C'mon. Let's go now."
                    mc "*Sigh* Fine..."
                    scene 12_282 with Dissolve(1)
                    mc "..."
                    va "What's up with that smile?"
                    scene black with Dissolve(1)
                    transform moveup:
                        xalign 0.5 yalign 1.0
                        linear 5.0 yalign 0.0
                    show 12_283 at moveup
                    pause 3
                    mc "{i}(I can't wait for tomorrow.){/i}"
                    scene 12_284 with Dissolve(1)
                    mc "I'm just imagining you wearing that swimsuit right now."
                    va "Heh..."
                    scene 12_285 with vpunch
                    mc "Hey!"
                    mc "Haha."
                    scene 12_286 with Dissolve(1)
                    mc "Okay... Okay... I see. We're doing this again!"
                    mc "If you think it will be like last time in the sand. You're clearly mistaken, girly!"
                    va "Haha. You mean that time I had to slow down or else you'd still be running after me?"
                    mc "It was the sand!"
                    va "Uh-huh."
                    scene 12_287 with Dissolve(1)
                    mc "{i}(I'll get you, and it will be so quick!){/i}"
                    scene 12_288 with Dissolve(1)
                    mc "Oh, come on! That's cheating!"
                    va "Haha."
                    mc "Are you that out of breath that you need to turn to these cheap tactics?"
                    va "I'm not the one breathing so heavily!"
                    mc "..."
                    scene 12_289 with Dissolve(1)
                    mc "VAL!"
                    va "Haha."
                    scene 12_290 with Dissolve(1)
                    va "Uh..."
                    mc "I'm not gonna run around this stupid bench for who knows how long."
                    scene 12_291 with Dissolve(1)
                    va "Aaah..."
                    mc "I'll get you now!"
                    scene 12_292 with vpunch
                    mc "Fuck!"
                    va "Haha. Nice try!"
                    mc "SHIT!"
                    scene 12_293 with Dissolve(1)
                    va "..."
                    va "Are you okay?"
                    mc "I think I twisted my ankle."
                    scene 12_294 with Dissolve(1)
                    va "Which foot is it? Can you stand up?"
                    va "Can you put pressure on it?"
                    mc "I don't know. Let me..."
                    scene 12_295 with Dissolve(1)
                    va "Ahh..."
                    mc "... Catch you first!"
                    scene 12_296 with Dissolve(1)
                    va "Wow... WOW..."
                    va "*Shakes head* And you call me a cheater!"
                    mc "Haha. Sorry, not sorry."
                    scene 12_297 with Dissolve(1)
                    mc "{i}(Haha. What is she doing?){/i}"
                    mc "{i}(She's just lifelessly hanging here.){/i}"
                    scene 12_298 with Dissolve(1)
                    mc "Are you mad at me? Or is it because you got caught?"
                    va "I'm mad at myself for falling for such an obvious trick!"
                    mc "Haha."
                    scene 12_299 with Dissolve(1)
                    va "..."
                    scene 12_300 with Dissolve(1)
                    va "Stop!"
                    mc "Hmm?"
                    va "You don't deserve a kiss, you cheater!"
                    mc "How about this then?"
                    scene 12_301 with Dissolve(1)
                    va "Haha."
                    va "[mc]..."
                    scene 12_302 with Dissolve(1)
                    mc "Seems like that worked."
                    va "..."
                    scene 12_303 with Dissolve(1)
                    mc "What's up with that mischievous smile?"
                    mc "You're making me nervous."
                    mc "You're planning something, right?"
                    va "*Nods*"
                    mc "Haha."
                    scene 12_304 with Dissolve(1)
                    va "But that will be for another time."
                    va "Let's do some actual jogging now."
                    mc "Yeah. I don't have that much time left, anyway."
                    scene black with Dissolve(1)
                    pause 2
                    scene 12_305 with Dissolve(1)
                    mc "*Heavy breathing* What the hell was that? You call this jogging...?"
                    va "With a little interval training."
                    mc "A little, she says..."
                    scene 12_306 with Dissolve(1)
                    va "You don't have to keep up. Just go at your own pace."
                    mc "And have you lap me? No way."
                    va "Haha."
                    mc "{i}(I thought I was doing great with my training the last few days.){/i}"
                    mc "{i}(But every time I run with her, there's still a big difference. I guess I'll have to step up even more.){/i}"
                    scene 12_307 with Dissolve(1)
                    va "You're doing great, though."
                    va "I can see you improving every time we run."
                    mc "Thanks."
                    scene 12_308 with Dissolve(1)
                    va "..."
                    mc "I love head scratches!"
                    scene 12_309 with Dissolve(1)
                    va "Who doesn't?"
                    mc "You too?"
                    va "Mm-hmm."
                    mc "Good to know."
                    scene 12_310 with Dissolve(1)
                    mc "I can stand here the whole day, doing this."
                    va "I won't do this the whole day though!"
                    menu:
                        "Grab her ass[KoGa3AutoWTChange1]{size=-4}(Valeria Points-4) {/size} {/color}":
                            $ Valeria_Points -= 4
                            scene 12_311 with Dissolve(1)
                            va "..."
                            scene 12_312 with Dissolve(1)
                            va "Okay..."
                            va "That's enough for today."
                        "Stay as you are[KoGa3AutoWTChange1]{size=-4}(Valeria Week5 Thursday Headscratches) {/size} {/color}":
                            $ Valeria_Week5_Thursday_Headscratches = True
                            scene 12_313 with Dissolve(1)
                            va "That's enough for today."
                            va "If you're lucky, you'll get some tomorrow!"
                            mc "I'm lucky!"
                            va "Haha."
                    scene 12_314 with Dissolve(1)
                    mc "I'd better leave now or I'll be late for work."
                    mc "What are your plans for the rest of the day?"
                    va "Hmm... I don't know yet."
                    mc "If you're bored, call me!"
                    scene 12_315 with Dissolve(1)
                    va "Maybe I will."
                    mc "See you tomorrow then?"
                    va "Yes."
                    scene 12_316 with Dissolve(1)
                    va "Haha."
                    scene 12_317 with Dissolve(1)
                    ""
                    scene 12_318 with Dissolve(1)
                    va "Bye, [mc]."
                    mc "Later, Val!"
                    scene 12_319 with Dissolve(1)
                    va "..."
                    scene 12_320 with vpunch
                    va "Ahhh... [mc]!"
                    va "I thought you had to leave or you'll be late!"
                    scene 12_321 with Dissolve(1)
                    x "Who's [mc]?"
                    va "..."
            else:
                scene 12_262 with Dissolve(1)
                mc "How was your beach date with Darryl?"
                va "It wasn't a date. You saw I was with a whole group."
                mc "Did you have fun at least?"
                va "Not as much as you did."
                scene 12_263 with Dissolve(1)
                mc "Yeah, I can't deny it. I had a pretty good time."
                va "I can imagine, with three pretty girls surrounding you."
                mc "Haha. I was only invited to carry all their stuff."
                scene 12_266 with Dissolve(1)
                va "Who was the blonde one? Not Erynn. The one with the short hair."
                mc "That's Iris. My ex."
                va "Oh..."
                mc "She's interested in Erynn. It was funny to see her trying to flirt with her."
                scene 12_267 with Dissolve(1)
                mc "I expected some drama. You know, girls in a group setting, there's always something."
                va "..."
                mc "When we played Kill-Fuck-Marry, it was a little awkward. And then the volleyball game. Oh boy..."
                scene 12_268 with Dissolve(1)
                va "I'm happy you had so much fun."
                va "Maybe I should've joined you guys instead."
                mc "You're always welcome to hang out with us."
                mc "So, why didn't you enjoy your beach day? Did something happen?"
                scene 12_247 with Dissolve(1)
                va "It was just boring. No one went into the ocean."
                va "Tori and Jasmine were just lying on the beach the whole afternoon."
                va "Darryl and TJ were throwing a football back and forth. I played a little with them, but that's about it."
                scene 12_227 with Dissolve(1)
                va "Also. Darryl kept hitting on me. Which was awkward. Especially since Tori was there too."
                va "At some point, he lay on top of me. I wanted to kick him so badly."
                va "But since we were at the beach, with all the other people around. I didn't want to make a scene."
                mc "I would've kicked him!"
                va "Yeah. Maybe I should've."
                scene 12_248 with Dissolve(1)
                mc "I'll still kick him for you, if you want me to."
                va "Haha. It's fine. But thanks for offering."
                scene 12_228 with Dissolve(1)
                mc "So Darryl has a thing for you, huh?"
                va "I'm not entirely blameless. I flirted too, before."
                mc "Oh... You're interested in Darryl then?"
                scene 12_229 with Dissolve(1)
                va "I think he's attractive, but I wouldn't go there with him."
                mc "Because of Tori?"
                va "No, in general. Not my type. Personality wise."
                va "We're friends and he's a teammate and we do flirt a bit, but that's about it."
                mc "Is there anyone at school you're interested in?"
                if Valeria_Points >= 18:
                    scene 12_230 with Dissolve(1)
                    va "There might be someone. We'll see."
                    mc "I'm so curious right now. You're not going to tell me who it is?"
                    va "No."
                    mc "It's not Zach, right?"
                    va "No. Also just a friend."
                    scene 12_231 with Dissolve(1)
                    mc "Is it me?"
                    va "..."
                    va "Yeah. Totally."
                    mc "Haha. Just a friend. I get it."
                else:
                    scene 12_230 with Dissolve(1)
                    va "Hmm, no. I haven't been looking either. I'm too busy to be in a relationship anyway."
                    mc "How about Zach?"
                    va "How about no!"
                    mc "Haha."
                if Layla_Week5_Wednesday_LikeElenaKnow == False:
                    scene 12_232 with Dissolve(1)
                    va "We should go to the beach next time."
                    va "Together with Layla and Elena."
                    va "That should be much more fun."
                    if Layla_Dating == True:
                        mc "We can do that. Layla owes me a beach date, anyway."
                        va "Great!"
                    else:
                        mc "We can do that."
                        va "Great!"
                    scene 12_243 with Dissolve(1)
                    va "Come on. Enough sitting around. Let's do a few more laps."
                    mc "Sure."
                    scene 12_282 with Dissolve(1)
                    ""
                else:
                    scene 12_233 with Dissolve(1)
                    va "We should go to the beach next time."
                    va "Together with Layla and Elena."
                    va "That should be much more fun."
                    scene 12_234 with Dissolve(1)
                    mc "About that. I don't think it will happen in the near future."
                    va "What? Why?"
                    mc "Uhm... *Sigh* You're going to find out anyway."
                    scene 12_235 with Dissolve(1)
                    mc "Layla and I kinda broke up, I guess."
                    va "You...? What?"
                    mc "Yeah..."
                    va "What happened?"
                    scene 12_236 with Dissolve(1)
                    mc "She... Uhm... Wanted more...?"
                    mc "And I wasn't too sure because..."
                    mc "*Sigh* There's someone else on my mind."
                    scene 12_237 with Dissolve(1)
                    va "Elena?"
                    mc "What...? How...? How do you know?"
                    va "The way you look at her."
                    mc "Is it that obvious?"
                    va "To me, yes."
                    scene 12_238 with Dissolve(1)
                    mc "I'll spare you the details, but I don't think she wants to talk to me."
                    mc "At least for some days, or maybe weeks."
                    va "Does she know you like Elena?"
                    mc "I told her."
                    scene 12_239 with Dissolve(1)
                    va "So there will be talks between the two as well."
                    mc "Oh shit... I hadn't even thought about that."
                    mc "I hope I haven't ruined their friendship as well, now."
                    mc "What a mess."
                    scene 12_240 with Dissolve(1)
                    mc "This is so much worse than I thought."
                    va "It will take some time, but it will be alright."
                    mc "I hope so."
                    scene 12_241 with Dissolve(1)
                    mc "I wanted to go for a run this morning to clear my head."
                    mc "But here I am, still thinking about that situation."
                    va "Sorry."
                    mc "It's not your fault."
                    scene 12_242 with Dissolve(1)
                    va "Come on. Let's go run, then."
                    mc "Sure."
                    scene 12_282 with Dissolve(1)
                    ""
        else:
            if Valeria_LikeMC == False:
                scene 12_262 with Dissolve(1)
                mc "How was your beach date with Darryl?"
                va "It wasn't a date. You saw I was with a whole group."
                mc "Did you have fun at least?"
                va "Not as much as you did."
                scene 12_263 with Dissolve(1)
                mc "Yeah, I can't deny it. I had a pretty good time."
                va "I can imagine, with three pretty girls surrounding you."
                mc "Haha. I was only invited to carry all their stuff."
                if Alexis_Dating == True:
                    scene 12_264 with Dissolve(1)
                    va "I didn't know you were that serious with Alexis already."
                    va "I knew you were seeing each other, but..."
                    mc "It's going really good."
                    scene 12_265 with Dissolve(1)
                    va "How is she? I mean her face, after she got hit with the ball."
                    mc "She'll be fine. We went to a club afterwards and she drank a lot."
                    mc "If she wakes up today and sees a bruise on her face, she probably won't even know where it's from."
                    va "Still. Please tell her I'm sorry again when you see her."
                    mc "Will do."
                    scene 12_266 with Dissolve(1)
                    va "Who was the blonde one? Not Erynn. The one with the short hair."
                    mc "That's Iris. My ex."
                    va "Oh... You went to the beach with your ex and your new girlfriend?"
                    mc "Yeah, I know. I had some reservations at first, but it was better than expected."
                    mc "It was more like a double date. Iris is interested in Erynn."
                else:
                    scene 12_266 with Dissolve(1)
                    va "Who was the blonde one? Not Erynn. The one with the short hair."
                    mc "That's Iris. My ex."
                    va "Oh..."
                    mc "She's interested in Erynn. It was funny to see her trying to flirt with her."
                scene 12_267 with Dissolve(1)
                mc "I expected some drama. You know, girls in a group setting, there's always something."
                va "..."
                mc "When we played Kill-Fuck-Marry, it was a little awkward. And then the volleyball game. Oh boy..."
                scene 12_268 with Dissolve(1)
                va "I'm happy you had so much fun."
                va "Maybe I should've joined you guys instead."
                mc "You're always welcome to hang out with us."
                mc "So, why didn't you enjoy your beach day? Did something happen?"
                scene 12_247 with Dissolve(1)
                va "It was just boring. No one went into the ocean."
                va "Tori and Jasmine were just lying on the beach the whole afternoon."
                va "Darryl and TJ were throwing a football back and forth. I played a little with them, but that's about it."
                scene 12_227 with Dissolve(1)
                va "Also. Darryl kept hitting on me. Which was awkward. Especially since Tori was there too."
                va "At some point, he lay on top of me. I wanted to kick him so badly."
                va "But since we were at the beach, with all the other people around. I didn't want to make a scene."
                mc "I would've kicked him!"
                va "Yeah. Maybe I should've."
                scene 12_248 with Dissolve(1)
                mc "I'll still kick him for you, if you want me to."
                va "Haha. It's fine. But thanks for offering."
                scene 12_228 with Dissolve(1)
                mc "So Darryl has a thing for you, huh?"
                va "I'm not entirely blameless. I flirted too, before."
                mc "Oh... You're interested in Darryl then?"
                scene 12_229 with Dissolve(1)
                va "I think he's attractive, but I wouldn't go there with him."
                mc "Because of Tori?"
                va "No, in general. Not my type. Personality wise."
                va "We're friends and he's a teammate and we do flirt a bit, but that's about it."
                mc "Is there anyone at school you're interested in?"
                if Valeria_Points >= 18:
                    scene 12_230 with Dissolve(1)
                    va "There might be someone. We'll see."
                    mc "I'm so curious right now. You're not going to tell me who it is?"
                    va "No."
                    mc "It's not Zach, right?"
                    va "No. Also just a friend."
                    scene 12_231 with Dissolve(1)
                    mc "Is it me?"
                    va "..."
                    va "Yeah. Totally."
                    mc "Haha. Just a friend. I get it."
                else:
                    scene 12_230 with Dissolve(1)
                    va "Hmm, no. I haven't been looking either. I'm too busy to be in a relationship anyway."
                    mc "How about Zach?"
                    va "How about no!"
                    mc "Haha."
                if Layla_Week5_Wednesday_LikeElenaKnow == False:
                    scene 12_232 with Dissolve(1)
                    va "We should go to the beach next time."
                    va "Together with Layla and Elena."
                    va "That should be much more fun."
                    if Layla_Dating == True:
                        mc "We can do that. Layla owes me a beach date, anyway."
                        va "Great!"
                    else:
                        mc "We can do that."
                        va "Great!"
                    scene 12_243 with Dissolve(1)
                    va "Come on. Enough sitting around. Let's do a few more laps."
                    mc "Sure."
                    scene 12_282 with Dissolve(1)
                    ""
                else:
                    scene 12_233 with Dissolve(1)
                    va "We should go to the beach next time."
                    va "Together with Layla and Elena."
                    va "That should be much more fun."
                    scene 12_234 with Dissolve(1)
                    mc "About that. I don't think it will happen in the near future."
                    va "What? Why?"
                    mc "Uhm... *Sigh* You're going to find out anyway."
                    scene 12_235 with Dissolve(1)
                    mc "Layla and I kinda broke up, I guess."
                    va "You...? What?"
                    mc "Yeah..."
                    va "What happened?"
                    scene 12_236 with Dissolve(1)
                    mc "She... Uhm... Wanted more...?"
                    mc "And I wasn't too sure because..."
                    mc "*Sigh* There's someone else on my mind."
                    scene 12_237 with Dissolve(1)
                    va "Elena?"
                    mc "What...? How...? How do you know?"
                    va "The way you look at her."
                    mc "Is it that obvious?"
                    va "To me, yes."
                    scene 12_238 with Dissolve(1)
                    mc "I'll spare you the details, but I don't think she wants to talk to me."
                    mc "At least for some days, or maybe weeks."
                    va "Does she know you like Elena?"
                    mc "I told her."
                    scene 12_239 with Dissolve(1)
                    va "So there will be talks between the two as well."
                    mc "Oh shit... I hadn't even thought about that."
                    mc "I hope I haven't ruined their friendship as well, now."
                    mc "What a mess."
                    scene 12_240 with Dissolve(1)
                    mc "This is so much worse than I thought."
                    va "It will take some time, but it will be alright."
                    mc "I hope so."
                    scene 12_241 with Dissolve(1)
                    mc "I wanted to go for a run this morning to clear my head."
                    mc "But here I am, still thinking about that situation."
                    va "Sorry."
                    mc "It's not your fault."
                    scene 12_242 with Dissolve(1)
                    va "Come on. Let's go run then."
                    mc "Sure."
                    scene 12_282 with Dissolve(1)
                    ""
            else:
                $ Valeria_Points -= 2
                scene 12_268 with Dissolve(1)
                mc "And then I saw you again in the afternoon. With Darryl..."
                va "Among others! I told you I was going. I even invited you."
                va "But it seemed like you had plans already. You could've told me."
                mc "I forgot that Erynn invited me."
                va "Erynn? Not Alexis?"
                mc "What?"
                scene 12_269 with Dissolve(1)
                va "..."
                mc "{i}(This is getting awkward now.){/i}"
                scene 12_270 with Dissolve(1)
                va "I didn't know you were that serious with Alexis."
                va "I knew you were seeing each other or even dating, but that looked like a full-on relationship."
                mc "Uhm..."
                va "If I knew earlier, I wouldn't have kissed you or anything."
                va "People date multiple people. I'm okay with that. But once things are getting serious..."
                if Alexis_BeachPoints <= 10:
                    menu:
                        "Break up with Alexis[KoGa3AutoWTChange1]{size=-4}(Alexis Week5 Thursday BreakUpTalk, Valeria Week5 Thursday Headscratches) {/size} {/color}":
                            $ Alexis_Week5_Thursday_BreakUpTalk = True
                            scene 12_322 with Dissolve(1)
                            mc "It might have looked that way."
                            mc "But it hasn't been... How can I say."
                            mc "I don't know. I just don't feel it... With her. And that has been going on for a while."
                            scene 12_323 with Dissolve(1)
                            mc "But I didn't see it until I met someone else."
                            mc "And now I can't stop thinking about her."
                            va "..."
                            scene 12_324 with Dissolve(1)
                            mc "I'm talking about you, by the way."
                            va "I got that."
                            mc "Heh."
                            scene 12_325 with Dissolve(1)
                            mc "..."
                            mc "{i}(Why isn't she saying anything?){/i}"
                            va "You've become very nervous all of a sudden."
                            mc "I am. Do you have any idea how fast my heart is beating right now?"
                            scene 12_326 with Dissolve(1)
                            va "It is!"
                            va "As if you've just sprinted."
                            va "It's actually getting faster, now."
                            scene 12_327 with Dissolve(1)
                            mc "This reminds me of training camp."
                            mc "When you were sitting on my bed and grabbed my hand and put it on your bo..."
                            va "Chest!"
                            mc "Yes. Chest."
                            scene 12_328 with Dissolve(1)
                            va "Training camp was so much fun!"
                            va "The races, the games. The day at the pool."
                            mc "Mm-hmm."
                            va "Let's hope there will be more."
                            scene 12_250 with Dissolve(1)
                            mc "But for now. How about we go to the beach tomorrow?"
                            va "Sure."
                            mc "Sure? I didn't expect that."
                            va "Under one condition. You break it off with Alexis! I don't wanna play these games any longer."
                            mc "I was planning already to end it with her the next time I see her. I don't want to do it over the phone."
                            va "*Nods*"
                            scene 12_251 with Dissolve(1)
                            va "Alright then. Beach, tomorrow. I have to be somewhere in the afternoon though, so can we go in the morning?"
                            mc "Uhm, yeah... Let's do that."
                            va "Cool."
                            scene 12_252 with Dissolve(1)
                            mc "I promise you. It will be much more fun this time!"
                            va "Looking forward to it."
                            scene 12_253 with Dissolve(1)
                            mc "Do we need to go shopping first?"
                            va "I don't think so. Why?"
                            mc "Maybe you need to test some more swimsuits."
                            scene 12_254 with Dissolve(1)
                            va "I actually bought the one..."
                            mc "You did? The one from the pictures?"
                            va "Uh-huh."
                            mc "I can't wait for tomorrow, now. It's gonna be amazing!"
                            scene 12_329 with Dissolve(1)
                            mc "..."
                            scene 12_243 with Dissolve(1)
                            va "Come on. Enough sitting around. Let's do a few more laps."
                            mc "Sure."
                            scene 12_282 with Dissolve(1)
                            mc "..."
                            va "What's up with that smile?"
                            scene black with Dissolve(1)
                            transform moveup:
                                xalign 0.5 yalign 1.0
                                linear 5.0 yalign 0.0
                            show 12_283 at moveup
                            pause 3
                            mc "{i}(I can't wait for tomorrow.){/i}"
                            scene 12_284 with Dissolve(1)
                            mc "I'm just imagining you wearing that swimsuit right now."
                            va "Heh..."
                            scene 12_285 with vpunch
                            mc "Hey!"
                            mc "Haha."
                            scene black with Dissolve(1)
                            pause 2
                            scene 12_305 with Dissolve(1)
                            mc "*Heavy breathing* What the hell was that? You call this jogging...?"
                            va "With a little interval training."
                            mc "A little, she says..."
                            scene 12_306 with Dissolve(1)
                            va "You don't have to keep up. Just go at your own pace."
                            mc "And have you lap me? No way."
                            va "Haha."
                            mc "{i}(I thought I was doing great with my training the last few days.){/i}"
                            mc "{i}(But every time I run with her, there's still a big difference. I guess I'll have to step up even more.){/i}"
                            scene 12_307 with Dissolve(1)
                            va "You're doing great though."
                            va "I can see you improving every time we run."
                            mc "Thanks."
                            scene 12_308 with Dissolve(1)
                            va "..."
                            mc "I love head scratches!"
                            scene 12_309 with Dissolve(1)
                            $ Valeria_Week5_Thursday_Headscratches = True
                            va "Who doesn't?"
                            mc "You too?"
                            va "Mm-hmm."
                            mc "Good to know."
                            scene 12_313 with Dissolve(1)
                            va "That's enough for today."
                            va "If you're lucky, you'll get some tomorrow!"
                            mc "I'm lucky!"
                            va "Haha."
                            scene 12_314 with Dissolve(1)
                            mc "I'd better leave now or I'll be late for work."
                            mc "What are your plans for the rest of the day?"
                            va "Hmm... I don't know yet."
                            mc "If you're bored, call me!"
                            scene 12_315 with Dissolve(1)
                            va "Maybe I will."
                            mc "See you tomorrow then?"
                            va "Yes."
                            scene 12_318 with Dissolve(1)
                            va "Bye, [mc]."
                            mc "Later, Val!"
                            scene 12_319 with Dissolve(1)
                            va "..."
                            scene 12_320 with vpunch
                            va "Ahhh... [mc]!"
                            va "I thought you had to leave or you'll be late!"
                            scene 12_321 with Dissolve(1)
                            x "Who's [mc]?"
                            va "..."
                        "Stay with Alexis[KoGa3AutoWTChange1]{size=-4}(Valeria Friends, Valeria LikeMCFalse, Valeria Week5 Thursday 2ndChance) {/size} {/color}":
                            $ Valeria_Friends = True
                            $ Valeria_LikeMC = False
                            $ Valeria_Week5_Thursday_2ndChance = True
                            scene 12_271 with Dissolve(1)
                            mc "Sorry..."
                            mc "You're right. We shouldn't have..."
                            mc "I wanted it though, and..."
                            scene 12_272 with Dissolve(1)
                            va "I wanted it too but... *Sigh* Let's just stop it now, then."
                            va "I don't wanna end up like... Never mind."
                            mc "{i}(What was she about to say?){/i}"
                            mc "*Nods*"
                            scene 12_273 with Dissolve(1)
                            mc "..."
                            va "..."
                            scene 12_274 with Dissolve(1)
                            ""
                            scene 12_275 with Dissolve(1)
                            ""
                            scene 12_276 with Dissolve(1)
                            ""
                            scene 12_277 with Dissolve(1)
                            n "*Heavy breathing*"
                            scene 12_278 with Dissolve(1)
                            va "That was our last kiss!"
                            mc "Ever?"
                            va "Maybe."
                            mc "Haha. I'll take maybe this time."
                            scene 12_279 with Dissolve(1)
                            mc "Fuck! Why do you have to be so beautiful and be such a good kisser?"
                            va "..."
                            scene 12_280 with Dissolve(1)
                            ""
                            scene 12_243 with Dissolve(1)
                            va "Come on. Enough sitting around. Let's do a few more laps."
                            mc "Sure."
                            scene 12_281 with Dissolve(1)
                            va "..."
                else:
                    $ Valeria_Friends = True
                    $ Valeria_LikeMC = False
                    $ Valeria_Week5_Thursday_2ndChance = True
                    scene 12_271 with Dissolve(1)
                    mc "Sorry..."
                    mc "You're right. We shouldn't have..."
                    mc "I wanted it though, and..."
                    scene 12_272 with Dissolve(1)
                    va "I wanted it too but... *Sigh* Let's just stop it now then."
                    va "I don't wanna end up like... Never mind."
                    mc "{i}(What was she about to say?){/i}"
                    mc "*Nods*"
                    scene 12_273 with Dissolve(1)
                    mc "..."
                    va "..."
                    scene 12_274 with Dissolve(1)
                    ""
                    scene 12_275 with Dissolve(1)
                    ""
                    scene 12_276 with Dissolve(1)
                    ""
                    scene 12_277 with Dissolve(1)
                    n "*Heavy breathing*"
                    scene 12_278 with Dissolve(1)
                    va "That was our last kiss!"
                    mc "Ever?"
                    va "Maybe."
                    mc "Haha. I'll take maybe this time."
                    scene 12_279 with Dissolve(1)
                    mc "Fuck! Why do you have to be so beautiful and be such a good kisser?"
                    va "..."
                    scene 12_280 with Dissolve(1)
                    ""
                    scene 12_243 with Dissolve(1)
                    va "Come on. Enough sitting around. Let's do a few more laps."
                    mc "Sure."
                    scene 12_281 with Dissolve(1)
                    va "..."
    stop music fadeout 1.0
    if Alexis_Dating == True:
        jump Week5_Thursday_Alexis
    else:
        if Layla_Dating == True:
            jump Week5_Thursday_Layla
        else:
            jump Week5_Thursday_Restaurant

label Week5_Thursday_Alexis:
    scene black with Dissolve(1)
    pause 2
    stop music fadeout 1.0
    play music ("Music/LoFi Indie 3.mp3", "Music/LoFi Indie 1.mp3", "Music/LoFi Indie 2.mp3") volume 0.2
    scene 12_330 with Dissolve(1)
    m "Good morning, honey."
    mc "Hey. Morning, Mom."
    m "Did you go for a run already?"
    mc "I did."
    scene 12_331 with Dissolve(1)
    m "I'm leaving in ten minutes."
    m "Are you coming with me, or...?"
    if MC_Bike == False:
        mc "I'll be ready. I just make a quick phone call."
        m "Alright."
    else:
        mc "I'll take the bike today."
        m "Alright. See you at the restaurant then."
        mc "Yeah."
    scene 12_332 with Dissolve(1)
    if Alexis_Week5_Wednesday_Beach == False:
        mc "..."
        mc "She must be awake already, right?"
    else:
        mc "..."
        mc "I hope she's awake already, after yesterday. Maybe I should've called a bit later?"
    if Alexis_Week5_Thursday_BreakUpTalk == True:
        scene 12_333 with Dissolve(1)
        a "Hey!"
        mc "Hi. Morning, Alexis."
        a "..."
        scene 12_335 with Dissolve(1)
        a "How are you?"
        mc "Good..."
        mc "Can we..."
        scene 12_336 with Dissolve(1)
        a "Oh, by the way. You're on speaker."
        a "I'm in the car right now with Layla."
        mc "Oh..."
        la "Hey, [mc]."
        mc "Hey..."
        scene 12_337 with Dissolve(1)
        a "Haha."
        a "Why are you waving? He can't see you."
        la "Shut up! It was... Never mind."
        scene 12_338 with Dissolve(1)
        mc "{i}(I can't really talk to her with Layla there, I guess.){/i}"
        mc "{i}(I didn't wanna do it over the phone anyway.){/i}"
        scene 12_340 with Dissolve(1)
        mc "Where are you headed?"
        a "To the airport."
        mc "Wait... Are you going somewhere?"
        a "No. We're picking someone up."
        mc "Oh..."
        scene 12_341 with Dissolve(1)
        a "I'm not just going on vacation without telling you!"
        mc "Yeah..."
        a "..."
        a "Something wrong?"
        scene 12_342 with Dissolve(1)
        mc "Uhm... No..."
        mc "Just... Can we meet up today?"
        a "Today will be difficult. I'm busy the whole day and I have to work later tonight."
        a "But you can always come by at the bar."
        scene 12_343 with Dissolve(1)
        mc "Yeah. I'll do that."
        mc "See you then. Bye, Alexis."
        a "Uhm..."
        a "Bye?"
        scene 12_344 with Dissolve(1)
        mc "*Sigh*"
        mc "Oh man..."
        scene 12_345 with Dissolve(1)
        a "He sounded weird, right?"
        la "I don't know."
        a "Something's definitely going on."
        jump Week5_Thursday_Restaurant
    else:
        scene 12_334 with Dissolve(1)
        a "Hey!"
        mc "Hi. Morning, Lexi."
        scene 12_335 with Dissolve(1)
        a "How are you?"
        mc "I'm good. How about you?"
        a "Good also."
        scene 12_336 with Dissolve(1)
        a "Oh, by the way. You're on speaker."
        a "I'm in the car right now with Layla."
        mc "Oh..."
        la "Hey, [mc]."
        mc "Hey, Layla."
        scene 12_337 with Dissolve(1)
        a "Haha."
        a "Why are you waving? He can't see you."
        la "Shut up! It was... Never mind."
        scene 12_339 with Dissolve(1)
        mc "Haha. Typical Layla."
        la "What do you mean 'typical Layla'?"
        a "Haha."
        la "Stop laughing or I'll throw the phone out of the window."
        a "Hey! Don't!"
        scene 12_346 with Dissolve(1)
        mc "Where are you headed?"
        a "To the airport."
        mc "Wait... Are you going somewhere?"
        a "No. We're picking someone up."
        mc "Oh..."
        scene 12_341 with Dissolve(1)
        a "I'm not just going on vacation without telling you!"
        if Alexis_Week5_Wednesday_Beach == False:
            mc "Yeah..."
            a "..."
            a "Something wrong?"
            scene 12_347 with Dissolve(1)
            mc "Just that we haven't seen each other for a long time now."
            mc "It feels like you're avoiding me or something."
            a "I'm not..."
            mc "Can we meet today?"
            scene 12_348 with Dissolve(1)
            a "Today is difficult. I've plans the whole day and I have to work at the bar this evening."
            a "You can always come by if you want."
            mc "Hmm... How about tomorrow?"
            scene 12_349 with Dissolve(1)
            a "Sorry. Can't tomorrow either."
            mc "..."
            a "I'm not avoiding you. I mean it."
            scene 12_350 with Dissolve(1)
            mc "Never mind then. I'll see you... whenever..."
            mc "Bye."
            a "Uh... [mc]...?"
            scene 12_344 with Dissolve(1)
            mc "*Sigh*"
            mc "What the fuck is going on?"
            scene 12_351 with Dissolve(1)
            a "That was... weird."
            la "Are you okay?"
            a "Yeah..."
            jump Week5_Thursday_Restaurant
        else:
            scene 12_352 with Dissolve(1)
            mc "You'd better not! At least invite me!"
            a "Haha. Don't worry. I will."
            scene 12_353 with Dissolve(1)
            mc "How are you after yesterday? I wasn't sure if you'd be awake already."
            a "I've been up for some time now. I went for a morning run with my dad, too."
            mc "You did? That's great!"
            a "Yeah. He couldn't believe it either when I agreed to it."
            scene 12_354 with Dissolve(1)
            la "You ran with Dad?"
            a "Uh-huh."
            la "Why didn't he ask me? I wanted to come too!"
            a "Maybe you were still asleep? You can run tomorrow with him. I won't have time then."
            scene 12_355 with Dissolve(1)
            mc "How is your head? Did the ball leave a mark or something?"
            a "I'm good. Forgot that even happened."
            la "What happened?"
            a "Got a ball to my face yesterday at the beach."
            la "Hah..."
            scene 12_356 with Dissolve(1)
            mc "You drank a lot yesterday. No wonder you forgot."
            a "I might have gone a little overboard with the drinking."
            mc "Do you remember the other stuff?"
            a "All except how I got home."
            scene 12_357 with Dissolve(1)
            mc "I drove you."
            a "Yeah. I suspected that. Thank you!"
            mc "Ran into your mom when I dropped off the keys in the kitchen. She drove me home afterwards."
            a "That's sweet of her."
            if Alexis_Week5_Wednesday_Club_KissIris == False:
                pass
            else:
                scene 12_358 with Dissolve(1)
                mc "Since you forgot some things. Do you remember the kiss?"
                a "What kiss exactly? We kissed multiple times."
                mc "The kiss between you and Iris."
                la "You kissed Iris?"
                a "What? No!"
                scene 12_359 with Dissolve(1)
                a "Nice try, [mc]!"
                a "First of all, I'd remember that. Secondly, it would never happen!"
                mc "{i}(She actually forgot? Or is she just pretending?){/i}"
                mc "{i}(I knew I should've taken a picture.){/i}"
                scene 12_360 with Dissolve(1)
                mc "You actually did!"
                a "Uh-huh."
                mc "No. Really! You can ask Iris."
                a "You guys probably..."
                mc "No! I can't believe you don't remember it."
                scene 12_361 with Dissolve(1)
                a "Okay... Let's say I believe you. Why would I have kissed Iris?"
                mc "Well. You were drunk, for starters."
                mc "And you were coming on very strong to me. Kissing me like it was a competition."
                mc "I said I was the better kisser, you said you were."
                a "I am the better kisser!"
                mc "Hah. That's exactly what you said yesterday."
                scene 12_362 with Dissolve(1)
                mc "Then Iris had the idea to kiss us so she could judge us."
                mc "So we did."
                a "Wait! You also kissed Iris?"
                mc "..."
                mc "{i}(I should've just kept my mouth shut about this... Shit...){/i}"
                scene 12_363 with Dissolve(1)
                mc "It was a competition and you agreed to it!"
                mc "I asked you first."
                a "..."
                scene 12_364 with Dissolve(1)
                a "I actually believe you now."
                a "You wouldn't say something this stupid as a joke."
                mc "..."
                a "Who won?"
                mc "Uhm... It doesn't matter."
                a "[mc]! Who won?"
                menu:
                    "I won":
                        scene 12_365 with Dissolve(1)
                        mc "I did."
                        a "Heh."
                    "You won[KoGa3AutoWTChange1]{size=-4}(Alexis Week5 Thursday KissWon) {/size} {/color}":
                        $ Alexis_Week5_Thursday_KissWon = True
                        scene 12_365 with Dissolve(1)
                        mc "{i}(A little white lie... Maybe this won't make her feel as bad...){/i}"
                        mc "You did."
                        a "Hmm..."
                scene 12_366 with Dissolve(1)
                mc "..."
                a "..."
                scene 12_367 with Dissolve(1)
                mc "Are you mad?"
                a "No."
                a "But I hope you enjoyed the kiss with Iris, because it's not gonna happen again!"
                mc "Haha. Don't worry."
                scene 12_368 with Dissolve(1)
                a "Did something else happen?"
                mc "Between us and Iris? No."
                a "No. I meant in general."
                scene 12_362 with Dissolve(1)
                mc "You danced on a pole."
                la "She did what?"
                a "No... Now you're just making stuff up."
                scene 12_353 with Dissolve(1)
                mc "I swear I'm not."
                mc "There were plenty of people taking pictures and videos."
                mc "You'll probably end up on someone's social media."
                scene 12_369 with Dissolve(1)
                la "I'll see if I can find something."
                a "Oh my god..."
                mc "Send it to me if you do."
                la "I will."
                a "I'll never go out drinking again!"
                mc "Haha. You had fun though!"
                scene 12_370 with Dissolve(1)
                mc "Anyway. I'm working at the restaurant today."
                mc "Do you wanna hang out after, maybe?"
                a "Sorry, I can't today. I have plans already, and in the evening, I'll be at the bar."
                mc "Hmm, okay."
                scene 12_371 with Dissolve(1)
                a "But you can always come by if you want."
                mc "Yeah. Marauders are playing today, so I might come and watch the game there."
                a "I'll reserve you a chair."
                mc "Haha, great. Thanks!"
                scene 12_372 with Dissolve(1)
                mc "I'll leave you to it, then."
                mc "Have fun today, and I'll probably see you later tonight."
                a "Mm-hmm. You too."
                scene 12_373 with Dissolve(1)
                a "Bye, [mc]. Love you!"
                mc "Love you too. Bye."
                scene 12_374 with Dissolve(1)
                mc "And bye, Layla!"
                la "Heh. Bye, [mc]. Oh, and let's go running tomorrow or at the weekend!"
                mc "Sure. Text me when and where."
                la "Will do. Bye."
                mc "Bye."
            jump Week5_Thursday_Restaurant

label Week5_Thursday_Layla:
    scene black with Dissolve(1)
    pause 2
    stop music fadeout 1.0
    play music ("Music/LoFi Indie 3.mp3", "Music/LoFi Indie 1.mp3", "Music/LoFi Indie 2.mp3") volume 0.2
    scene 12_330 with Dissolve(1)
    m "Good morning, honey."
    mc "Hey. Morning, Mom."
    m "Did you go for a run already?"
    mc "I did."
    scene 12_331 with Dissolve(1)
    m "I'm leaving in ten minutes."
    m "Are you coming with me, or...?"
    if MC_Bike == False:
        mc "I'll be ready. I just make a quick phone call."
        m "Alright."
    else:
        mc "I'll take the bike today."
        m "Alright. See you at the restaurant, then."
        mc "Yeah."
    scene 12_332 with Dissolve(1)
    mc "{i}(Hmm...){/i}"
    mc "{i}(She's not picking up.){/i}"
    mc "{i}(Is she still sleeping?){/i}"
    scene 12_375 with Dissolve(1)
    la "..."
    play sound "Sounds/Phone_Vibrate.mp3"
    n "*Bzzzt. Bzzzt*"
    a "Who is it?"
    n "*Bzzzt. Bzzzt*"
    a "Pick up already!"
    scene 12_376 with Dissolve(1)
    la "Hey..."
    mc "Hi."
    mc "Did I wake you?"
    la "No..."
    scene 12_377 with Dissolve(1)
    mc "..."
    la "..."
    scene 12_378 with Dissolve(1)
    mc "Say something!"
    la "You say something!"
    mc "Haha."
    scene 12_379 with Dissolve(1)
    mc "How are you?"
    la "I'm good."
    mc "Yeah? And uh... You know... Does it hurt?"
    la "..."
    la "Just a little, but it's fine."
    scene 12_380 with Dissolve(1)
    mc "I can't stop thinking about yesterday."
    la "Me neither."
    mc "..."
    la "..."
    scene 12_381 with Dissolve(1)
    mc "What are you doing right now?"
    la "I'm in the car with Alexis."
    mc "Hey, Alexis."
    la "[mc] says hey."
    a "Hey, [mc]."
    scene 12_382 with Dissolve(1)
    mc "Where are you going?"
    la "The airport."
    mc "The airport? You're going on vacation or something?"
    la "Haha, no. Picking someone up."
    mc "Oh..."
    scene 12_383 with Dissolve(1)
    la "I would've told you yesterday if we were going on vacation."
    mc "Maybe you forgot, because..."
    la "No..."
    scene 12_384 with Dissolve(1)
    la "Are you at the restaurant?"
    mc "Not yet. I'm leaving in ten minutes."
    mc "Just wanted to talk to you first."
    la "Heh."
    scene 12_385 with Dissolve(1)
    mc "What are you doing today?"
    mc "I'll be at the restaurant till five or six, but we can meet up afterwards if you want."
    la "Sorry, I can't today. I have plans already."
    mc "No worries."
    scene 12_386 with Dissolve(1)
    la "How about we go for a run tomorrow and we can make plans then?"
    mc "Perfect."
    mc "Now I can't wait for tomorrow."
    la "Hehe. Me too."
    if Alexis_SP >= 13:
        scene 12_387 with Dissolve(1)
        a "..."
    else:
        pass
    scene 12_388 with Dissolve(1)
    mc "I'll call you later, once I'm done with work."
    la "Okay."
    mc "Bye, Layla. Have fun today!"
    la "You too! Bye, [mc]."
    jump Week5_Thursday_Restaurant

label Week5_Thursday_Restaurant:
    scene black with Dissolve(1)
    pause 2
    stop music fadeout 1.0
    play music ("Sounds/Restaurant_Background.mp3","Sounds/Restaurant_Background2.mp3","Sounds/Restaurant_Background3.mp3") volume 0.2
    scene 12_389 with Dissolve(1)
    n "Rue Madison restaurant, 09:47."
    scene 12_390 with Dissolve(1)
    mc "Hey guys."
    ja "Hey, [mc]."
    mo "Good morning, [mc]."
    mc "How are you?"
    scene 12_391 with Dissolve(1)
    ja "Good, good. You?"
    mc "Enjoying spring break. What can I say?"
    ja "Man... I miss school. All the breaks and holidays you've got."
    mc "Haha, yeah."
    scene 12_392 with Dissolve(1)
    ja "Are you working today?"
    mc "Uh-huh."
    ja "Great! We can use your help."
    mc "That busy?"
    ja "You have no idea. We're still understaffed."
    scene 12_393 with Dissolve(1)
    mc "Yeah. I've heard that Mom's having a difficult time finding people at the moment."
    mo "And she probably triple-checks everything now after... You know."
    mc "Yeah..."
    mc "{i}(Do they know that Rachel is dead? Better not bring it up now. Or at all.){/i}"
    br "Look who decided to show up!"
    scene black with Dissolve(1)
    transform moveup:
        xalign 0.5 yalign 1.0
        linear 5.0 yalign 0.0
    show 12_394 at moveup
    pause 3
    mc "..."
    mc "Hey, Brooke."
    br "Hi."
    scene 12_395 with Dissolve(1)
    br "Long time no see."
    mc "It hasn't been that long."
    br "A week."
    mc "It's already been a week? Damn, time goes fast..."
    menu:
        "Hug Brooke[KoGa3AutoWTChange1]{size=-4}(Brooke Points+2) {/size} {/color}":
            $ Brooke_Points += 2
            # Brooke (8)
            scene 12_398 with vpunch
            br "Aah... [mc]!"
            br "Haha."
            scene 12_399 with Dissolve(1)
            mc "How are you?"
            br "I'm good."
            mc "Miss me?"
            br "A little. Well... Not particularly you, but more the work you do."
            mc "Haha. Good to know."
            scene 12_400 with Dissolve(1)
            mo "And now we know who his favourite is."
            mc "Haha."
            ja "She gets a hug, I only got a fist bump."
            mc "You wanted a hug too? Why didn't you say so?"
            scene 12_401 with Dissolve(1)
            mc "Come here."
            ja "I'm so regretting this now."
            br "Haha."
            scene 12_402 with Dissolve(1)
            m "*Shakes head*"
            scene 12_403 with Dissolve(1)
            br "..."
            scene 12_404 with Dissolve(1)
            br "Alright. Enough playing around."
            br "It's time to work!"
            mc "See that? And you thought she was my favourite?"
            ja "Haha."
            scene 12_405 with Dissolve(1)
            mc "Where should I start?"
            br "The tables."
            br "Flowers, candles, napkins... You know the setup."
            mc "Will do."
            br "Thanks, [mc]."
        "Don't hug her":
            scene 12_396 with Dissolve(1)
            br "Ready for work?"
            mc "I just arrived and you're putting me to work already?"
            br "Of course! That's why you're here, no?"
            mc "Heh. Sure... What do you want me to do?"
            scene 12_397 with Dissolve(1)
            br "You can start with the tables."
            br "Flowers, candles, napkins... You know the setup."
            mc "Will do."
            br "Thanks."
    scene 12_406 with Dissolve(1)
    ""
    scene 12_407 with Dissolve(1)
    ""
    scene black with Dissolve(1)
    pause 2
    scene 12_408 with Dissolve(1)
    mc "{i}(Let's see...){/i}"
    mc "{i}(Yeah. That's all the tables, I think.){/i}"
    scene 12_409 with Dissolve(1)
    mc "{i}(Let's find Brooke and see what I can do next.){/i}"
    mc "Moni... Do you know where Brooke is?"
    mo "In the back somewhere."
    mc "Okay. Thanks."
    scene 12_410 with Dissolve(1)
    mc "Broo..."
    mc "..."
    scene 12_411 with Dissolve(1)
    mc "{i}(What is she doing?){/i}"
    mc "{i}(Is she looking at something?){/i}"
    mc "{i}(Is someone in there?){/i}"
    scene 12_412 with Dissolve(1)
    br "..."
    scene 12_413 with Dissolve(1)
    mc "{i}(She's leaving now.){/i}"
    mc "{i}(I really want to know what she was looking at.){/i}"
    mc "{i}(*Sigh* Why must I be so curious?){/i}"
    mc "{i}(Just a quick peek.){/i}"
    scene 12_414 with Dissolve(1)
    mc "..."
    scene black with Dissolve(1)
    transform moveup:
        xalign 0.5 yalign 1.0
        linear 5.0 yalign 0.0
    show 12_415 at moveup
    pause 3
    mc "{i}(It's... Mom...){/i}"
    scene 12_416 with Dissolve(1)
    mc "{i}(Oh shit!){/i}"
    m "..."
    scene 12_417 with Dissolve(1)
    mc "{i}(Fuck-Shit-Fuck!){/i}"
    mc "{i}(Did she see me?){/i}"
    mc "{i}(Now it looks like I was peeking on my mom instead of just wanting to know what Brooke was looking at!){/i}"
    scene 12_418 with Dissolve(1)
    mc "{i}(Why was Brooke looking?){/i}"
    mc "{i}(And the way she was looking at her...){/i}"
    mc "{i}(Is she...?){/i}"
    menu:
        "Look for Brooke[KoGa3AutoWTChange1]{size=-4}(Brooke Week5 Thursday Peek) {/size} {/color}":
            $ Brooke_Week5_Thursday_Peek = True
            scene 12_420 with Dissolve(1)
            mc "{i}(Let's go find Brooke.){/i}"
            mc "{i}(This will be interesting.){/i}"
            mc "{i}(But where did she go?){/i}"
            jump Week5_Thursday_Restaurant_Brooke
        "Change and go back to work":
            scene 12_419 with Dissolve(1)
            mc "{i}(I'll talk to her later.){/i}"
            mc "{i}(This is going to be fun.){/i}"
            jump Week5_Thursday_Restaurant_Work

label Week5_Thursday_Restaurant_Brooke:
    scene black with Dissolve(1)
    pause 2
    stop music fadeout 1.0
    play music "Sounds/Soft_Moaning.mp3" volume 0.3
    scene 12_421 with Dissolve(1)
    mc "{i}(This is the only place I haven't checked.){/i}"
    mc "{i}(Why did I even come in here? I could've just waited until she came back.){/i}"
    mc "{i}(I'll just head back before someone sees me here.){/i}"
    scene 12_422 with Dissolve(1)
    n "*Silent moan*"
    mc "..."
    mc "{i}(Was that...?){/i}"
    scene 12_423 with Dissolve(1)
    mc "{i}(What the fuck am I doing?){/i}"
    mc "{i}(Why do I have to be so curious all the time?){/i}"
    mc "{i}(If I get caught, Mom will kill me!){/i}"
    scene 12_424 with Dissolve(1)
    mc "..."
    scene black with Dissolve(1)
    transform moveup:
        xalign 0.5 yalign 1.0
        linear 5.0 yalign 0.0
    show 12_425 at moveup
    pause 3
    mc "{i}(Damn!){/i}"
    mc "{i}(That is so freakin' hot!){/i}"
    mc "{i}(Totally worth the risk!){/i}"
    scene 12_426 with Dissolve(1)
    mc "{i}(Who's she thinking about while doing it?){/i}"
    mc "{i}(Mom?){/i}"
    mc "{i}(Yeah... Probably Mom.){/i}"
    scene 12_427 with Dissolve(1)
    mc "{i}(I wish I could see more.){/i}"
    mc "{i}(This isn't the best of angles.){/i}"
    scene 12_428 with Dissolve(1)
    br "*Whispers* Emily..."
    mc "{i}(Yep. Definitely thinking about Mom.){/i}"
    mc "{i}(Would Mom be interested in Brooke?){/i}"
    mc "{i}(Is Mom actually bi?){/i}"
    mc "{i}(She had something with Melissa back in college. And then that time in the pool...){/i}"
    scene 12_429 with Dissolve(1)
    mc "{i}(Imagine Brooke with Mom...){/i}"
    mc "{i}(Fuck!){/i}"
    mc "{i}(Why am I getting turned on by that thought?){/i}"
    mc "{i}(My imagination is going crazy again.){/i}"
    scene 12_430 with Dissolve(1)
    mc "{i}(I wish I could look in her mind and see what's she is imagining.){/i}"
    mc "{i}(Wait... No!){/i}"
    mc "{i}(She's thinking about Mom... I would see... Mom...){/i}"
    mc "{i}(What's wrong with me...?){/i}"
    scene 12_431 with Dissolve(1)
    mc "{i}(What I want to see though is her boobs!){/i}"
    mc "{i}(I wish she had removed her top, too.){/i}"
    scene 10_1304 with Dissolve(1)
    mc "{i}(Last time when we were both undressing, I saw her in her bra.){/i}"
    mc "{i}(She has a nice pair of tits.){/i}"
    scene 12_432 with Dissolve(1)
    mc "{i}(I wanna keep looking and see her finish, but I think I've pushed my luck already.){/i}"
    mc "{i}(I'd better leave now before she notices me being a creep.){/i}"
    $ renpy.end_replay()
    scene 12_433 with Dissolve(1)
    stop music fadeout 1.0
    play music ("Sounds/Restaurant_Background.mp3","Sounds/Restaurant_Background2.mp3","Sounds/Restaurant_Background3.mp3") volume 0.2
    mc "{i}(Shit... Just my luck.){/i}"
    mc "{i}(Of course, someone just enters the bathroom when I'm about to leave...){/i}"
    scene 12_434 with Dissolve(1)
    mc "{i}(*Sigh*){/i}"
    mc "{i}(No other option but to wait now, I guess...){/i}"
    scene 12_435 with Dissolve(1)
    br "Hey, Emily."
    m "Good morning, Brooke. How are you?"
    mc "{i}(Oh... It was Mom who came in here. Don't start imagining things again!){/i}"
    mc "{i}(I hope they'll leave and won't chit-chat so I can get out of here...){/i}"
    scene black with Dissolve(1)
    pause 2
    scene 12_436 with Dissolve(1)
    mc "{i}(Looks like the coast is clear.){/i}"
    mc "{i}(Time to get out of here.){/i}"
    mc "{i}(Hey. That rhymed...){/i}"
    mc "{i}(I'm such an idiot.){/i}"
    jump Week5_Thursday_Restaurant_Work

label Week5_Thursday_Restaurant_Work:
    scene black with Dissolve(1)
    pause 2
    scene 12_437 with Dissolve(1)
    mc "..."
    scene 12_438 with Dissolve(1)
    br "Okay, what's up?"
    br "You've been staring at me for the last minute and a half."
    mc "Minute and a half? Haha. That's oddly specific."
    scene 12_439 with Dissolve(1)
    mc "I found the last pieces of the puzzle."
    br "Hmm?"
    mc "I saw you."
    br "What are you talking about?"
    scene 12_440 with Dissolve(1)
    mc "After I was done setting up the tables, I was looking for you."
    mc "I came around the corner in the hallway and guess who I saw looking at..."
    scene 12_441 with Dissolve(1)
    br "..."
    mc "Mmm..."
    scene 12_442 with Dissolve(1)
    mc "Uh..."
    mc "Where are you taking me?"
    scene 12_443 with Dissolve(1)
    br "Listen!"
    br "I don't know what you think you saw, but you're wrong."
    br "There was nothing and..."
    scene 12_444 with Dissolve(1)
    br "Why are you smiling like that again?"
    mc "It's so cute that you're trying to talk your way out of it."
    br "I'm not. I'm..."
    scene 12_445 with Dissolve(1)
    mc "I was curious what you were looking at."
    mc "So, when you left, I took a quick peek."
    br "..."
    mc "And there was..."
    scene 12_446 with Dissolve(1)
    br "I was just passing by and then..."
    mc "Uh-huh."
    br "No, really..."
    scene 12_447 with Dissolve(1)
    mc "I saw the way you looked at her, Brooke."
    br "..."
    br "Please don't tell your mom. Or anyone, for that matter."
    mc "I won't."
    scene 12_448 with Dissolve(1)
    br "*Sigh* Oh my god..."
    mc "Hey. It's alright. No need to be upset about it."
    scene 12_449 with Dissolve(1)
    mc "So, you like my mom, huh?"
    br "No, it's not like that. It's more of a crush."
    br "She's beautiful, kind, runs a successful business. You know? I look up to her."
    mc "Uh-huh... Who are you trying to fool? Me or yourself?"
    br "..."
    scene 12_450 with Dissolve(1)
    br "Alright. Fine!"
    br "I like your mom!"
    br "And if I had a chance with her, I'd take it!"
    mc "..."
    mc "{i}(I didn't expect her to admit it so quickly.){/i}"
    scene 12_451 with Dissolve(1)
    br "But I don't. She isn't into girls..."
    if Brooke_Points >= 5:
        menu:
            "College Emily[KoGa3AutoWTChange1]{size=-4}(Brooke Week5 Thursday CollegeEmily) {/size} {/color}":
                $ Brooke_Week5_Thursday_CollegeEmily = True
                mc "Hmm... I'm not so sure about that."
                br "What?"
                scene 12_452 with Dissolve(1)
                mc "She had something with a woman before."
                br "..."
                mc "I don't know if it was serious, or just experimental, or..."
                mc "{i}(I can't believe I'm spilling Mom's past.){/i}"
                scene 12_453 with Dissolve(1)
                br "Emily is bi?"
                mc "As I said. I don't know. It's a weird question to ask your mom. Like. Hey, Mom. Are you bi, by chance?"
                br "Heh. Yeah."
            "Don't say anything":
                pass
    else:
        pass
    scene 12_454 with Dissolve(1)
    mc "For how long have you been in love with her?"
    br "I'm not in love with her!"
    mc "Haha. I'm just teasing. But..."
    scene 12_455 with Dissolve(1)
    br "Two years."
    mc "Two years?"
    br "Yeah. First time I met her when I had my interview for this job."
    mc "Wow. Two years... And you haven't made a single move yet?"
    scene 12_456 with Dissolve(1)
    br "She's my boss!"
    mc "And?"
    br "Your mom!"
    mc "You didn't know that before a few weeks ago."
    br "..."
    scene 12_457 with Dissolve(1)
    mc "Are you bi, or like full on..."
    br "Lesbian?"
    mc "Uh, yeah."
    br "Mm-hmm."
    scene 12_458 with Dissolve(1)
    mc "Never had something with a guy before?"
    br "No."
    mc "Not even a kiss?"
    br "No."
    scene 12_459 with Dissolve(1)
    mc "Well, that explains why you shot me down every time I asked you out."
    mc "And also why you didn't mind undressing in front of me."
    br "Sorry."
    mc "My flirting had no effect?"
    if Brooke_Points >= 5:
        scene 12_460 with Dissolve(1)
        br "I actually liked the flirting."
        mc "I knew it! Because you flirted back!"
        br "*Nods* I did."
        mc "So, not a one hundred per cent thing?"
        br "Haha. I don't know."
        scene 12_461 with Dissolve(1)
        mc "If you wanna know for sure, I'm happy to help."
        br "Haha. I'll keep that in mind."
    else:
        br "Not really."
        mc "Heh, okay."
    scene 12_462 with Dissolve(1)
    mc "Uh..."
    br "This conversation made me feel much better about all this."
    br "I was actually scared that someone would find out."
    br "So. Thank you, [mc]. For being so cool with it."
    mc "You're welcome."
    scene 12_463 with Dissolve(1)
    ja "She's definitely the favourite."
    mo "Yeah. I can see them dating in the future."
    scene 12_464 with Dissolve(1)
    mc "..."
    scene 12_465 with Dissolve(1)
    mc "Oh... Look at that."
    mc "Your first semi-kiss with a guy!"
    br "Haha."
    if Brooke_Week5_Thursday_CollegeEmily == True:
        $ Brooke_Week5_Thursday_MommyBrooke = True
        scene 12_466 with Dissolve(1)
        mc "Okay then. What's the plan?"
        br "Hmm?"
        mc "Want me to help you set up a date with Emily?"
        br "What? [mc]! No!"
        scene 12_467 with Dissolve(1)
        mc "Or I can invite you over to our house and once you're there, suddenly something urgent comes up and I have to leave."
        mc "That way you can spend some alone time with her."
        br "[mc]!"
        mc "Don't like the idea?"
        scene 12_468 with Dissolve(1)
        br "..."
        mc "{i}(Is she thinking about it?){/i}"
        mc "{i}(Teasing her is so much fun!){/i}"
        scene 12_469 with Dissolve(1)
        br "*Sigh* Look what you've done. Now I won't be able to stop thinking about it!"
        mc "{i}(Haha. I guess she is.){/i}"
        br "I'll go do... something..."
        mc "If you change your mind..."
        br "..."
        scene 12_470 with Dissolve(1)
        mc "One more thing!"
        mc "If things work out for you. Would you want me to call you Mommy Brooke?"
        br "Haha, [mc]. Oh my god..."
        scene 12_471 with Dissolve(1)
        br "But yes!"
        $ achievement.grant("ACHIEVEMENT_MOMMY_BROOKE")
        $ achievement.sync()
        mc "Haha."
    else:
        pass
    scene black with Dissolve(1)
    pause 2
    scene 12_472 with Dissolve(1)
    mc "Here's your champagne."
    gu "Thank you."
    scene 12_473 with Dissolve(1)
    mc "Can I start you off with something to drink?"
    if Erynn_Week5_Thursday_Photo == True:
        play sound "Sounds/Phone_Message.mp3"
        n "*Bzzzt*"
        gu "A beer for me."
        gu "And I'll take a red wine, please."
        scene 12_474 with Dissolve(1)
        mc "{i}(Let's see who texted me.){/i}"
        mc "{i}(Oh... Erynn.){/i}"
        mc "{i}(Is she done with her shoot?){/i}"
        scene 12_475 with Dissolve(1)
        mc "{i}(It's actually a picture.){/i}"
        mc "..."
        mc "{i}(Hot damn...){/i}"
        scene black with Dissolve(1)
        transform moveup:
            xalign 0.5 yalign 1.0
            linear 5.0 yalign 0.0
        show 12_476 at moveup
        pause 3
        ""
        scene 12_477 with Dissolve(1)
        mc "{i}(Viking warrior or something?){/i}"
        mc "{i}(This is amazing!){/i}"
        scene 12_478 with Dissolve(1)
        mc "{i}(I'd better get the drinks first.){/i}"
        mc "{i}(Then I can have a better look.){/i}"
        scene black with Dissolve(1)
        pause 2
        scene 12_479 with Dissolve(1)
        mc "{i}(Alright. Let's see...){/i}"
        scene 12_480 with Dissolve(1)
        ja "What are you smiling about?"
        ja "Got some good news or something?"
        mc "My friend sent me a picture. Come have a look."
        scene 12_481 with Dissolve(1)
        ja "That's your friend?"
        mc "Yeah."
        ja "Wait. Isn't she the girl from last week?"
        mc "Indeed she is."
        ja "Want me to salute again?"
        mc "Haha."
        scene 12_482 with Dissolve(1)
        br "What are you guys looking at?"
        mc "Hmm? Nothing."
        br "Uh-huh. Can I see?"
        scene 12_483 with Dissolve(1)
        ja "You don't wanna see this. It's guy stuff. Right, [mc]?"
        mc "Yeah. Guy stuff."
        br "Guy stuff...?"
        br "Hey, Moni. I wanted to ask you before."
        br "Which bikini do you like better?"
        scene 12_484 with Dissolve(1)
        ja "Bikini?"
        br "Heh. This is too easy!"
        br "And nothing to worry about. It's girl stuff!"
        ja "..."
        scene 12_485 with Dissolve(1)
        mc "{i}(Let's text her back real quick.){/i}"
        mc "{i}(Thanks for the picture.){/i}"
        mc "{i}(You look amazing, Ryn! Some kind of Viking warrior?){/i}"
        mc "{i}(What's it for? Is the shoot over?){/i}"
        scene 12_486 with Dissolve(1)
        n "*Bzzzt. Bzzzt*"
        mc "{i}(Heh. She's calling now.){/i}"
        scene 12_487 with Dissolve(1)
        mc "Hey."
        er "Hi. Can you talk, or are you busy?"
        mc "Give me a sec."
        scene 12_488 with Dissolve(1)
        mc "Alright."
        mc "How's the shoot going? Or are you done?"
        er "I have a little break. I need to wait until the others are ready and then there will be some more group photos."
        scene 12_489 with Dissolve(1)
        mc "The picture looks amazing!"
        er "Yeah? Thanks."
        mc "Mm-hmm. Really like it. I wouldn't mind putting that up in my room."
        er "Really?"
        mc "Yeah, maybe I'll do that."
        er "..."
        scene 12_490 with Dissolve(1)
        er "I can send you a few more. Then you can choose which one you like best?"
        mc "That'd be great!"
        er "I'll send them after the call."
        mc "Can't wait to see them!"
        scene 12_491 with Dissolve(1)
        mc "You're like a Viking warrior or something?"
        er "It's based in a Viking world. I'm more like a Valkyrie?"
        mc "You've also got wings then?"
        er "In some pictures, I have."
        scene 12_492 with Dissolve(1)
        mc "Now I wish I was at this photo shoot as well."
        mc "Dressed up as a warrior and then taking pictures with you. So cool!"
        mc "Or a slain Viking on the battlefield and you're my Valkyrie who brings me to Valhalla."
        er "Haha. What?"
        mc "Haha. I'm just daydreaming!"
        scene 12_493 with Dissolve(1)
        mc "What's this photo shoot for? I don't think it's perfume, right?"
        er "Haha, no. It's for a mobile game? I think. Could be for PC too."
        er "Uhm... Gach... Gachi something? I can't remember."
        mc "Ah. A gacha game. What's the name? I want to check it out."
        scene 12_494 with Dissolve(1)
        er "Sorry, I forgot. I'll ask again and I'll text you the name."
        mc "Thanks. Are you going to be a character in the game, or...?"
        er "No. The pictures are for several internet ads."
        mc "Using a hot girl as a marketing strategy to lure in more players."
        mc "Can't blame 'em. It works. Even I want to play now, after seeing you."
        scene 12_495 with Dissolve(1)
        er "Did you see? I have tattoos now too."
        mc "Isn't it warpaint?"
        er "Hmm... Yeah. Could be warpaint actually."
        mc "I saw a little. Didn't have time to properly look at the picture. Will do during my break."
        mc "Are those like sticky tattoos, or...?"
        scene 12_496 with Dissolve(1)
        er "It's body paint."
        mc "Must have taken some time to draw them on you."
        er "Yes. A little over an hour."
        er "Got them all over my body. Arms, legs, back. My face."
        if Erynn_Week5_Thursday_Shower == True:
            scene 12_497 with Dissolve(1)
            mc "Let's hope it washes off easily."
            mc "And if not, we can shower together again, and I'll help you."
            er "..."
        else:
            pass
        scene 12_498 with Dissolve(1)
        mc "By the way. Is Ethan there?"
        er "He is."
        mc "Did he...?"
        er "No. There are lots of people here and he's mostly talking to the client."
        scene 12_499 with Dissolve(1)
        er "And now I'm sitting in the makeup trailer and have locked the door."
        mc "Good."
        mc "If anything..."
        er "I will. Thanks."
        scene 12_500 with Dissolve(1)
        n "*Knock-knock*"
        x "Erynn. We're ready."
        er "Yes. I'm coming."
        scene 12_501 with Dissolve(1)
        er "Sorry. Gotta go."
        mc "Don't worry. I have to go back to work, too."
        mc "Thanks for calling and for the picture, Erynn."
        er "You're welcome."
        scene 12_502 with Dissolve(1)
        mc "Bye, Erynn."
        mc "Oh... And send me some more pictures. And don't forget to ask about the name."
        er "I will. Bye, [mc]."
        mc "Bye!"
        scene 12_503 with Dissolve(1)
        play sound "Sounds/Phone_Message.mp3"
        n "*Bzzzt*"
        mc "{i}(That was quick.){/i}"
        scene 12_504 with Dissolve(1)
        mc "{i}(Is she even wearing panties?){/i}"
        mc "{i}(Or is that loincloth everything she has down there?){/i}"
        mc "{i}(I hope it's not too windy there.){/i}"
        scene 12_505 with Dissolve(1)
        mc "{i}(This really is so cool!){/i}"
        scene 12_506 with Dissolve(1)
        mc "{i}(Here's one with the wings.){/i}"
        mc "{i}(How much do those weigh?){/i}"
        scene 12_507 with Dissolve(1)
        mc "Haha."
        mc "{i}(I like this one.){/i}"
        mc "{i}(She pulls off that Viking look perfectly!){/i}"
    else:
        gu "A beer for me."
        gu "And I'll take a red wine, please."
    scene black with Dissolve(1)
    pause 2
    scene 12_508 with Dissolve(1)
    ""
    scene 12_509 with Dissolve(1)
    br "Hey. How are you doing?"
    mc "Hi. It's going good."
    br "I've just sent Jaylen on a fifteen-minute break. Can you keep an eye on his tables?"
    br "I'll take the left side, you the right?"
    mc "Yeah. No problem."
    br "Thanks."
    scene 12_510 with Dissolve(1)
    br "Did you see who I just seated?"
    mc "No. Someone famous?"
    br "Uh-huh. Ximena Vergara."
    if Erynn_Week5_Tuesday_Photoshoot == True:
        scene 12_511 with Dissolve(1)
        mc "I've heard that name before."
        mc "Wait... Isn't she that actress who stars in that famous TV show?"
        br "Entanglement."
        mc "Yeah, that one."
        br "She is."
    else:
        scene 12_511 with Dissolve(1)
        mc "Doesn't really ring a bell."
        br "She's an actress. Stars in Entanglement."
        mc "Right, right. That TV show everybody is so hyped about."
        br "Correct."
    scene 12_512 with Dissolve(1)
    br "Do you watch it?"
    if Layla_Dating == True:
        mc "I saw like one episode. That's about it. You?"
    else:
        mc "I don't. You?"
    br "Every week! You should give it a try. It's really good."
    mc "Next time when I'm bored. I'll watch an episode."
    br "Heh."
    scene 12_513 with Dissolve(1)
    mc "Mom watches it though."
    mc "So how about you come over and watch it together with her?"
    br "..."
    scene 12_514 with Dissolve(1)
    br "Before you get any other stupid ideas..."
    mc "It's a great idea!"
    br "*Sigh* Here. Bring Ms Vergara the menus."
    mc "Oh, you want me to do it?"
    br "Yes! Now go! Table three!"
    scene 12_515 with Dissolve(1)
    mc "..."
    br "Go!"
    mc "Yes, Mommy Brooke!"
    br "*Shakes head*"
    br "I'm regretting telling you."
    mc "No, you aren't. You're secretly enjoying this!"
    if Gabi_End == True:
        scene 12_516 with Dissolve(1)
        mc "{i}(Oh...){/i}"
        mc "{i}(Ms Ramirez is also here. Together with Ms Vergara.){/i}"
        if Alexis_Week5_Wednesday_Beach == True:
            mc "{i}(I keep running into her. Saw her yesterday at the club too.){/i}"
        else:
            if Layla_Dating == True:
                mc "{i}(I keep running into her. Saw her yesterday at the club too.){/i}"
            else:
                pass
        scene 12_517 with Dissolve(1)
        mc "{i}(So this is Ximena Vergara...){/i}"
        mc "{i}(No wonder this TV show is so popular. Maybe I'll check it out after all.){/i}"
        mc "{i}(Are they friends? How did they meet? Maybe they went to school together?){/i}"
        if Valeria_LikeMC == True:
            mc "{i}(Have I seen her before somewhere? Probably on TV or maybe a picture in a magazine...){/i}"
        else:
            pass
        if Week3_Monday_Spanish_Blackmail == False:
            scene 12_518 with Dissolve(1)
            mc "Good afternoon."
            xv "Hi. Good afternoon."
            tr "Hi, [mc]."
            mc "Hello, Ms Ramirez."
            scene 12_520 with Dissolve(1)
            xv "You know each other?"
            tr "He's one of my students."
            xv "Oh..."
            scene 12_521 with Dissolve(1)
            xv "Lucky you. Having such a hot teacher!"
            mc "Uh..."
            tr "Ximena!"
            mc "{i}(I can't really argue with her. I bet half of the boys take her class not just for Spanish.){/i}"
            if Valeria_LikeMC == True:
                scene 12_522 with Dissolve(1)
                xv "Say! Have we met before?"
                mc "{i}(She has the same thought? Maybe we have?){/i}"
                mc "I don't think so."
                xv "Hmm..."
            else:
                pass
        else:
            scene 12_519 with Dissolve(1)
            mc "Good afternoon."
            xv "Hi. Good afternoon."
            tr "Hello..."
        scene 12_523 with Dissolve(1)
        mc "Here are your menus."
        xv "Thank you."
        mc "Can I start you off with something to drink?"
        scene 12_524 with Dissolve(1)
        xv "Two glasses of champagne, please."
        xv "Actually. Make that a whole bottle."
        tr "..."
        mc "Alright."
        if Valeria_LikeMC == True:
            scene 12_525 with Dissolve(1)
            xv "I'm pretty sure I've seen him before..."
            xv "But where?"
        else:
            pass
        scene 12_526 with Dissolve(1)
        xv "Do you know who he reminds me of?"
        tr "Don't say his name!"
        xv "You think so too? He looks a little like him, right?"
        tr "..."
        scene black with Dissolve(1)
        pause 2
        scene 12_527 with Dissolve(1)
        br "That didn't take long."
        mc "Hmm?"
        br "I feel a little bad for her."
        mc "What are you talking about?"
        br "There, look!"
        scene 12_528 with Dissolve(1)
        mc "It was just a matter of time before she got recognised."
        mc "That's one of the drawbacks of being famous."
        br "Still..."
        br "You come to a restaurant to have a nice meal, and then..."
        br "At least let her have her food first, or wait until she leaves."
        scene 12_529 with Dissolve(1)
        mc "I think she's used to it."
        br "I'm a little bit of hypocrite though."
        mc "Why's that?"
        br "I would love a picture with her as well."
        scene 12_530 with Dissolve(1)
        mc "Why don't you go there and ask her?"
        br "Because that would be unprofessional."
        mc "Do you think you're the first server who asked for a picture?"
        br "No, but... *Sigh* Maybe later. Once she leaves."
        scene 12_531 with Dissolve(1)
        mc "Question. She plays the mother in the show, right?"
        br "Yeah."
        mc "How old is she? Late twenties, early thirties? Doesn't she look too young to play that role?"
        br "Well, she's the stepmom. Like a trophy wife."
        scene 12_532 with Dissolve(1)
        br "But she... No never mind. You have to watch it yourself."
        mc "No, tell me."
        br "I don't want to spoil it."
        mc "It's fine. I'm not even sure if I'm ever gonna watch it anyway."
        scene 12_533 with Dissolve(1)
        br "She has an affair with the son."
        mc "Oh wow. You just ruined the whole show for me."
        br "You told me to spoil it!"
        mc "I didn't know it was that big of a spoiler."
        br "..."
        scene 12_534 with Dissolve(1)
        mc "Haha. I'm kidding. I'm kidding, Brooke."
        mc "I really don't care."
        scene 12_535 with Dissolve(1)
        mc "It's such a cliché though. The stepmom and the son."
        br "It is. But there's a big difference in how it's written."
        br "And in this case, it's... Just watch it. You'll see."
        mc "Haha."
        scene 12_536 with Dissolve(1)
        mc "I'd better bring them their champagne now..."
        mc "Before you start spoiling something else."
        br "*Shakes head*"
    else:
        scene 12_537 with Dissolve(1)
        mc "{i}(Oh...){/i}"
        mc "{i}(Gabi is also here. Together with Ms Vergara.){/i}"
        if Alexis_Week5_Wednesday_Beach == True:
            mc "{i}(I keep running into her. Saw her yesterday at the club too.){/i}"
        else:
            if Layla_Dating == True:
                mc "{i}(I keep running into her. Saw her yesterday at the club too.){/i}"
            else:
                pass
        scene black with Dissolve(1)
        transform moveup:
            xalign 0.5 yalign 1.0
            linear 5.0 yalign 0.0
        show 12_538 at moveup
        pause 3
        mc "{i}(Is there any day she doesn't look good?){/i}"
        scene 12_517 with Dissolve(1)
        mc "{i}(So... This is Ximena Vergara...){/i}"
        mc "{i}(Are they friends? How did they meet? Maybe they went to school together?){/i}"
        scene black with Dissolve(1)
        transform moveup:
            xalign 0.5 yalign 1.0
            linear 5.0 yalign 0.0
        show 12_539 at moveup
        pause 3
        mc "{i}(No wonder this TV show is so popular. Maybe I'll check it out after all.){/i}"
        mc "{i}(Have I seen her before somewhere? Probably on TV or maybe a picture in a magazine...){/i}"
        scene 12_540 with Dissolve(1)
        mc "Hi, Ga... Ms Ramirez. Ms Vergara. Good afternoon."
        tr "Uh... Hey..."
        xv "Hi. Good afternoon."
        scene 12_541 with Dissolve(1)
        mc "You look good!"
        tr "Thanks..."
        mc "And so do you, Ms Vergara."
        xv "Thank you."
        scene 12_542 with Dissolve(1)
        xv "Sorry, I didn't catch your name."
        mc "It's [mc]."
        xv "[mc]."
        if Alexis_Week5_Wednesday_Beach == True:
            scene 12_543 with Dissolve(1)
            xv "So this is how you met?"
            xv "You could've told me yesterday!"
            tr "Uhm..."
            mc "{i}(Let's not tell her Gabi is my teacher...){/i}"
        else:
            if Layla_Week5_Wednesday_ClubDate == True:
                scene 12_543 with Dissolve(1)
                xv "So this is how you met?"
                xv "You could've told me yesterday!"
                tr "Uhm..."
                mc "{i}(Let's not tell her Gabi is my teacher...){/i}"
            else:
                scene 12_543 with Dissolve(1)
                xv "You know each other?"
                tr "Uhm... Yeah. We've met before..."
                xv "Hmm..."
                mc "{i}(Let's not tell her Gabi is my teacher...){/i}"
        scene 12_544 with Dissolve(1)
        mc "Here are your menus."
        xv "Thank you."
        mc "Can I start you off with something to drink?"
        scene 12_524 with Dissolve(1)
        xv "Two glasses of champagne, please."
        xv "Actually. Make that a whole bottle. I think we need it."
        tr "..."
        scene 12_545 with Dissolve(1)
        mc "Celebrating?"
        xv "Yes!"
        tr "No!"
        mc "{i}(Heh...?){/i}"
        scene 12_546 with Dissolve(1)
        mc "I'll get you your celebratory and non-celebratory champagne."
        tr "..."
        mc "{i}(Maybe I shouldn't have said anything. Now she's looking mad at me.){/i}"
        xv "Haha. Thank you!"
        scene 12_525 with Dissolve(1)
        xv "I think I've seen him before. Hmm..."
        xv "Or maybe it's just that he reminds me of someone."
        xv "Don't you think he looks a little like..."
        scene 12_547 with Dissolve(1)
        tr "We're not going to talk about him right now!"
        xv "But he does, right?"
        tr "..."
        tr "A little..."
        scene black with Dissolve(1)
        pause 2
        scene 12_527 with Dissolve(1)
        br "That didn't take long."
        mc "Hmm?"
        br "I feel a little bad for her."
        mc "What are you talking about?"
        br "There, look!"
        scene 12_528 with Dissolve(1)
        mc "It was just a matter of time before she got recognised."
        mc "That's one of the drawbacks of being famous."
        br "Still..."
        br "You come to a restaurant to have a nice meal, and then..."
        br "At least let her have her food first or wait until she leaves."
        scene 12_529 with Dissolve(1)
        mc "I think she's used to it."
        br "I'm a little bit of hypocrite though."
        mc "Why's that?"
        br "I would love a picture with her as well."
        scene 12_530 with Dissolve(1)
        mc "Why don't you go there and ask her?"
        br "Because that would be unprofessional."
        mc "Do you think you're the first server who asked for a picture?"
        br "No, but... *Sigh* Maybe later. Once she leaves."
        scene 12_531 with Dissolve(1)
        mc "Question. She plays the mother in the show, right?"
        br "Yeah."
        mc "How old is she? Late twenties, early thirties? Doesn't she look too young to play that role?"
        br "Well, she's the stepmom. Like a trophy wife."
        scene 12_532 with Dissolve(1)
        br "But she... No never mind. You have to watch it yourself."
        mc "No, tell me."
        br "I don't want to spoil it."
        mc "It's fine. I'm not even sure if I'm ever gonna watch it anyway."
        scene 12_533 with Dissolve(1)
        br "She has an affair with the son."
        mc "Oh wow. You just ruined the whole show for me."
        br "You told me to spoil it!"
        mc "I didn't know it was that big of a spoiler."
        br "..."
        scene 12_534 with Dissolve(1)
        mc "Haha. I'm kidding. I'm kidding, Brooke."
        mc "I really don't care."
        scene 12_548 with Dissolve(1)
        tr "..."
        scene 12_535 with Dissolve(1)
        mc "It's such a cliché though. The stepmom and the son."
        br "It is. But there's a big difference in how it's written."
        br "And in this case, it's... Just watch it. You'll see."
        mc "Haha."
        scene 12_536 with Dissolve(1)
        mc "I'd better bring them their champagne now..."
        mc "Before you start spoiling something else."
        br "*Shakes head*"
        scene 12_549 with Dissolve(1)
        mc "Here's your champagne."
        tr "Thank you."
        scene 12_550 with Dissolve(1)
        mc "Did you have a chance to look at the menu yet?"
        tr "We did."
        tr "For the appetizer, I'll take the lobster risotto."
        tr "And for the entree... Let's do the crispy-skin salmon."
        mc "Lobster risotto and the crispy-skin salmon."
        scene 12_551 with Dissolve(1)
        mc "And for you, Ms Vergara?"
        xv "Hmm..."
        xv "You know what? Recommend me something."
        mc "Uhm..."
        scene 12_552 with Dissolve(1)
        mc "{i}(I'm not good at this stuff. What if she doesn't like it?){/i}"
        mc "{i}(She's really put me on the spot now.){/i}"
        mc "{i}(This is so hard. What to pick? Fish or meat?){/i}"
        scene 12_553 with Dissolve(1)
        mc "I'd recommend the pan-seared scallops as an appetizer."
        mc "As for the entree... You can never go wrong with the filet mignon."
        mc "But personally, I would go with the beef Wellington."
        xv "Beef Wellington. That sounds good. Let's do that and the pan-seared scallops."
        mc "Awesome."
        scene 12_554 with Dissolve(1)
        xv "To something new."
        tr "It's a little early for that."
        xv "It's never too early."
    if Layla_Week5_Wednesday_BreakUp == False:
        scene 12_555 with Dissolve(1)
        mc "{i}(Lobster risotto and pan-seared scallops.){/i}"
        mc "{i}(And then the crispy-skin salmon and the beef Wellington.){/i}"
    else:
        scene 12_555 with Dissolve(1)
        mc "{i}(Lobster risotto and pan-seared scallops.){/i}"
        play sound "Sounds/Phone_Vibrate.mp3"
        n "*Bzzzt. Bzzzt*"
        mc "{i}(And then the crispy-skin salmon and the beef Wellington.){/i}"
        n "*Bzzzt. Bzzzt*"
        scene 12_556 with Dissolve(1)
        mc "{i}(Elena... Fuck...){/i}"
        mc "{i}(I should've guessed Layla would tell her.){/i}"
        mc "{i}(Should I even pick up?){/i}"
        mc "{i}(I guess I will... *Sigh*){/i}"
        scene 12_557 with Dissolve(1)
        mc "Hey, Elena."
        el "What did you do?"
        mc "What?"
        scene 12_558 with Dissolve(1)
        el "What did you do, [mc]?"
        mc "{i}(Wait... Didn't Layla tell her?){/i}"
        mc "Why? What's wrong?"
        el "Because Layla doesn't want to talk with me!"
        scene 12_559 with Dissolve(1)
        mc "Why not?"
        mc "{i}(I know why... Why am I being so oblivious?){/i}"
        el "I don't know. That's why I'm calling you since you were with her yesterday!"
        el "Did something happen?"
        scene 12_560 with Dissolve(1)
        mc "Listen. I..."
        el "So something did happen!"
        mc "Elena... Uhm..."
        mc "I think we should talk face-to-face."
        el "..."
        scene 12_561 with Dissolve(1)
        el "Where are you right now?"
        mc "I'm working."
        el "At the restaurant?"
        mc "Yeah. I'll call you when I..."
        scene 12_562 with Dissolve(1)
        el "I'm heading there right now!"
        mc "What?"
        mc "Elena. It's quite busy here at the moment and I..."
        mc "Elena?"
        mc "{i}(She hung up already.){/i}"
        scene 12_563 with Dissolve(1)
        mc "{i}(Man...){/i}"
        mc "{i}(I could fucking scream!){/i}"
        mc "{i}(AAAAH!!!){/i}"
    scene 12_564 with Dissolve(1)
    br "Hey. Jaylen is back from his break."
    br "You can take a quick fifteen-minutes if you want."
    mc "Yeah. Thanks."
    if Valeria_LikeMC == True:
        if Erynn_Week5_Thursday_Shower == True:
            scene 12_566 with Dissolve(1)
            mc "{i}(Let's see if she picks up today.){/i}"
            mc "{i}(With her, it's always a guessing game.){/i}"
            scene 12_567 with Dissolve(1)
            va "Hey."
            mc "Look at that. She picked up."
            va "..."
            va "I can't always immediately pick up when I'm busy!"
            mc "Haha, I know, I know. I'm just joking."
            scene 12_568 with Dissolve(1)
            mc "How are you?"
            va "I'm good. How about you?"
            mc "Same. What are you doing?"
            va "I'll give you a hint. Listen."
            scene 12_569 with Dissolve(1)
            mc "..."
            scene 12_570 with Dissolve(1)
            mc "I can't hear anything with you chewing so loudly."
            va "That's the hint, smartass!"
            mc "Ah... Haha. You're eating! I get it."
            scene 12_571 with Dissolve(1)
            mc "What are you eating?"
            va "Cereal."
            mc "What brand?"
            mc "No wait. Let me guess."
            scene 12_572 with Dissolve(1)
            mc "It's not muesli, right?"
            va "If it was muesli, I would've said muesli instead of cereal."
            mc "Right, right."
            mc "Hmm..."
            scene 12_573 with Dissolve(1)
            mc "Let's think. What type of cereal girl are you...?"
            va "*Shakes head* Cereal girl..."
            mc "It could be anything."
            va "You wanted to guess."
            scene 12_574 with Dissolve(1)
            mc "Something sweet..."
            va "Aren't most of them sweet?"
            mc "Pretty much, yes. Honey pops?"
            va "Good guess. Very close."
            scene 12_575 with Dissolve(1)
            mc "Honey loops?"
            va "Mm-hmm."
            mc "I like those too."
            mc "But cereal for lunch?"
            scene 12_576 with Dissolve(1)
            va "Hey! There were days I've eaten cereal for breakfast, lunch, and dinner!"
            mc "Haha. Me too actually."
            mc "You should've come to the restaurant and eaten here instead."
            scene 12_577 with Dissolve(1)
            va "You're cooking for me?"
            mc "Me? No. I'm not doing that to you."
            va "Haha."
            mc "I'll leave that to the professionals."
            mc "I can make you a bowl of cereal though!"
            va "I'm happy with that."
            scene 12_578 with Dissolve(1)
            mc "..."
            va "..."
            scene 12_579 with Dissolve(1)
            mc "How was your date with Darryl? Did you go?"
            va "I did go, yes. And it wasn't a date! We went with a few people!"
            mc "Did you have fun?"
            va "No..."
            scene 12_580 with Dissolve(1)
            mc "Haha. No?"
            va "..."
            mc "Sorry. I didn't mean to laugh."
            va "Uh-huh..."
            mc "{i}(But I'm still happy about that.){/i}"
            scene 12_581 with Dissolve(1)
            mc "Did something happen?"
            va "It was just boring. No one went into the ocean."
            va "Tori and Jasmine were just lying on the beach the whole afternoon."
            va "Darryl and TJ were throwing a football back and forth. I played a little with them, but that's about it."
            scene 12_582 with Dissolve(1)
            va "Also. Darryl kept hitting on me. Which was awkward. Especially since Tori was there too."
            va "At some point, he lay on top of me. I wanted to kick him so badly."
            mc "{i}(What?){/i}"
            va "But since we were at the beach, with all the other people around. I didn't want to make a scene."
            mc "I would've kicked him!"
            va "Yeah. Maybe I should've."
            scene 12_583 with Dissolve(1)
            mc "I'll still kick him for you, if you want me to."
            va "Haha. It's fine. But thanks for offering."
            mc "Anytime. I still owe you a kick!"
            va "Haha, you do."
            scene 12_584 with Dissolve(1)
            va "You should've just joined us."
            va "We didn't have to stay with them, but could've done our own thing."
            mc "{i}(Now I think about it, I should've gone.){/i}"
            mc "{i}(Spending more time with Val and seeing Darryl's face when I flirt with her. Damn...){/i}"
            mc "You're right."
            scene 12_585 with Dissolve(1)
            mc "Let's go together next time then."
            va "Sure."
            mc "Sure? Not maybe?"
            va "Not a maybe."
            scene 12_586 with Dissolve(1)
            va "How about tomorrow? I have to be somewhere in the afternoon, but we can go in the morning?"
            mc "Uhm, yeah... Let's do that."
            va "Cool."
            scene 12_587 with Dissolve(1)
            mc "I promise you. It will be much more fun this time!"
            va "Looking forward to it."
            scene 12_588 with Dissolve(1)
            mc "Do we need to go shopping first?"
            va "I don't think so. Why?"
            mc "Maybe you need to try on some more swimsuits."
            scene 12_589 with Dissolve(1)
            va "I actually bought the one..."
            mc "You did? The one from the pictures?"
            va "Uh-huh."
            mc "Can't wait for tomorrow now. It's gonna be amazing!"
            scene 12_590 with Dissolve(1)
            mc "Anyway. I think my break is about to be over."
            mc "I'd better head back to work."
            va "Have fun."
            mc "Thanks. I hope your honey loops aren't soggy now. Because no one likes soggy cereal."
            va "Haha, true."
            scene 12_591 with Dissolve(1)
            va "Thanks for calling. And see you tomorrow then."
            mc "Yeah. Bye, Val."
            va "Bye, [mc]."
        else:
            scene 12_565 with Dissolve(1)
            mc "{i}(Can't wait for tonight's game.){/i}"
            mc "{i}(It's gonna be so awesome.){/i}"
    else:
        scene 12_565 with Dissolve(1)
        mc "{i}(Can't wait for tonight's game.){/i}"
        mc "{i}(It's gonna be so awesome.){/i}"
    scene black with Dissolve(1)
    pause 2
    if Gabi_End == True:
        scene 12_592 with Dissolve(1)
        ""
        scene 12_593 with Dissolve(1)
        ""
    else:
        scene 12_594 with Dissolve(1)
        xv "That's our food, I think."
        tr "Mm-hmm."
        scene 12_595 with Dissolve(1)
        mc "The lobster risotto for you, Ms Ramirez."
        tr "Thank you very much."
        scene 12_596 with Dissolve(1)
        mc "And for you, Ms Vergara, the pan-seared scallops."
        xv "Beautiful!"
        scene 12_597 with Dissolve(1)
        mc "Well thank you. What about the food?"
        xv "Heh... Cheeky!"
        scene 12_598 with Dissolve(1)
        mc "May I top off your glass?"
        xv "You may, thanks."
        scene 12_599 with Dissolve(1)
        mc "How about you, Ms Ramirez?"
        tr "Uhm..."
        xv "You can call her Gabriela."
        scene 12_600 with Dissolve(1)
        tr "Ximena!"
        xv "What? It's your name."
        tr "He's... Never mind. You want him to call you Ximena too?"
        xv "No. I like the way he says Ms Vergara."
        tr "*Sigh*"
        scene 12_601 with Dissolve(1)
        tr "Thanks, [mc]. I'm good for now."
        xv "See! You call him by his first name, too!"
        tr "Thanks, Mr Moreno!"
        scene 12_602 with Dissolve(1)
        xv "Moreno? Hmm... An..."
        mc "It's actually Vicari."
        tr "What?"
        mc "Long story."
        scene 12_603 with Dissolve(1)
        mc "Anyway. Enjoy your meals, Ms Ramirez. Ximena!"
        xv "Haha. As I said. Cheeky!"
        xv "Thank you. Mr Vicari!"
        scene 12_604 with Dissolve(1)
        xv "He's charming. I like him."
        xv "And you like him, too!"
        tr "..."
        tr "Can we talk about something else now?"
        xv "Of course, Ms Ramirez."
    if Layla_Week5_Wednesday_BreakUp == True:
        scene black with Dissolve(1)
        pause 2
        scene 12_605 with Dissolve(1)
        br "Hello."
        br "Do you have a reservation?"
        scene 12_606 with Dissolve(1)
        x "Yes! With that guy!"
        mc "..."
        scene 12_607 with Dissolve(1)
        br "Uhm..."
        mc "{i}(Elena...){/i}"
        mc "{i}(She actually came.){/i}"
        scene 12_608 with Dissolve(1)
        mc "It's fine, Brooke. I'll take it from here."
        br "Alright."
        di "Hey, [mc]."
        mc "Hey, guys. Come, you can sit here at the bar."
        scene 12_609 with Dissolve(1)
        mc "How are you? Are you enjoying spring break?"
        ma "Yes! We went to AquaLand yesterday with abuela."
        mc "Wow. That must've been cool. I've never been there. Did you see sharks?"
        scene 12_610 with Dissolve(1)
        di "Yes! They were so big!"
        di "And there were also stingrays. They were feeding them."
        di "And one caught a fish, pressing it against the glass and was eating it."
        mc "That's so cool!"
        di "Yes!"
        scene 12_611 with Dissolve(1)
        mc "Hey, Elena."
        el "..."
        el "Hey..."
        mc "Give me a second, okay? Be right back."
        scene 12_612 with Dissolve(1)
        mc "Brooke. Can you take over for me for a few minutes?"
        br "Sure, no problem."
        mc "Thanks. These drinks are for table eight."
        br "Okay."
        scene 12_613 with Dissolve(1)
        mc "Do you wanna drink or eat something?"
        el "I'm not here to eat!"
        mc "{i}(I know...){/i}"
        ma "Then why are we at a restaurant?"
        scene 12_614 with Dissolve(1)
        di "I'm hungry, Elena."
        ma "I'm hungry too!"
        el "*Sigh* Of course, you are."
        el "We won't be long here. Afterwards, we can..."
        scene 12_615 with Dissolve(1)
        mc "Do you guys like cheese balls?"
        el "[mc], I..."
        ma "Yes!"
        mc "Yes? Alright. Two orders of cheese balls."
        el "[mc]... *Sigh*"
        scene 12_616 with Dissolve(1)
        mc "And to drink?"
        di "Can we have cola, Elena? Please?"
        el "Fine."
        scene 12_617 with Dissolve(1)
        mc "Do you want something?"
        el "No."
        mc "I'll be right back."
        el "[mc]..."
        mc "It'll be just a moment."
        scene black with Dissolve(1)
        pause 2
        scene 12_618 with Dissolve(1)
        mc "Here you go, boys."
        di "There's so many!"
        scene 12_619 with Dissolve(1)
        mc "I know you said you don't want anything, but I got you a coffee."
        el "..."
        el "Thanks..."
        scene 12_620 with Dissolve(1)
        el "Can we talk now?"
        mc "{i}(I guess I've dragged it out long enough.){/i}"
        mc "Yeah... Let's... Let's go outside and talk there."
        el "We can't leave. I have to watch..."
        mc "Right. Uhm..."
        scene 12_621 with Dissolve(1)
        mc "Brooke. Can you do me another favour?"
        mc "I need to talk to my friend. Can you keep an eye on her brothers for a few minutes?"
        br "Sure. No problem."
        mc "Thank you. I owe you."
        scene 12_622 with Dissolve(1)
        br "Are you enjoying the cheese balls?"
        ma "Yes!"
        mc "Don't worry. They'll be fine. Brooke is really nice."
        el "..."
        scene black with Dissolve(1)
        pause 2
        play music ("Music/Slow.mp3", "Music/Slow4.mp3") volume 0.4
        stop music fadeout 1.0
        scene 12_623 with Dissolve(1)
        mc "How about here?"
        el "That's fine..."
        scene 12_624 with Dissolve(1)
        el "Now tell me. What happened?"
        mc "Uhm..."
        scene 12_625 with Dissolve(1)
        mc "Can you please come sit down?"
        el "..."
        mc "Please?"
        scene 12_626 with Dissolve(1)
        mc "..."
        mc "{i}(Where to start?){/i}"
        mc "{i}(And how do I even tell her?){/i}"
        scene 12_627 with Dissolve(1)
        mc "Uhm... Layla and I kinda broke up."
        el "What? You...?"
        mc "{i}(Even though we never really made it official. It still counts as a break up, right?){/i}"
        el "Didn't you go out yesterday? Did something happen?"
        scene 12_628 with Dissolve(1)
        mc "Yeah. We did go out. And no, nothing happened."
        el "Something must have happened!"
        el "She likes you so much. She wouldn't just break up out of nowhere."
        scene 12_629 with Dissolve(1)
        mc "*Sigh*"
        mc "We went to Heaven, stayed a while and I brought her home afterwards."
        mc "She then..."
        el "..."
        scene 12_630 with Dissolve(1)
        mc "She..."
        mc "Man... *Sigh*"
        el "What?"
        scene 12_631 with Dissolve(1)
        mc "She wanted to invite me in and..."
        mc "And have sex."
        el "..."
        scene 12_632 with Dissolve(1)
        mc "But I... I..."
        mc "I couldn't do it because..."
        mc "There's someone else I like."
        mc "And I told her that."
        el "..."
        scene 12_633 with Dissolve(1)
        mc "I told her I..."
        mc "I like you, Elena!"
        scene 12_634 with Dissolve(1)
        el "..."
        mc "..."
        scene 12_635 with Dissolve(1)
        mc "Sorry. I didn't want to make you cry."
        el "I'm not crying because of you!"
        el "I finally understand why Layla doesn't want to talk to me!"
        mc "You..."
        scene 12_636 with Dissolve(1)
        el "Why would you say that?"
        mc "I..."
        el "WHY WOULD YOU SAY THAT TO HER!"
        scene 12_637 with Dissolve(1)
        mc "Because I like you!"
        el "Stop saying that!"
        mc "But it's the truth. You want me to lie to her?"
        el "No!"
        scene 12_638 with Dissolve(1)
        el "But why would you do it then and there?"
        el "Do you have any idea how much courage she must've..."
        mc "Don't you think I know that? What was I supposed to do?"
        mc "I didn't know she planned all that."
        mc "Was I supposed to have sex with her for the first time and tell her afterwards? That's even worse."
        scene 12_639 with Dissolve(1)
        mc "What do you think I should have done? I can't help who I fall for."
        el "How about not having sex and saying you're not ready?"
        mc "Since that would've been believable?"
        mc "She still would've questioned why."
        mc "I was trying to do the right thing."
        scene 12_640 with Dissolve(1)
        el "..."
        mc "..."
        scene 12_641 with Dissolve(1)
        el "You need to fix it!"
        el "Before school starts next week!"
        el "Because I... I can't have..."
        mc "I will."
        scene 12_642 with Dissolve(1)
        mc "{i}(But I have no idea how to do that.){/i}"
        mc "{i}(And the last thing I want is to ruin their friendship.){/i}"
        mc "{i}(I hate seeing her like this.){/i}"
        scene 12_643 with Dissolve(1)
        mc "Come here."
        el "Get off me!"
        menu:
            "Hug her anyway":
                mc "No."
                scene 12_644 with Dissolve(1)
                el "*Crying*"
                mc "{i}(This is the second time I've seen her cry now.){/i}"
                mc "{i}(She seems so tough all the time, but...){/i}"
                mc "I'm so sorry!"
            "Back off":
                mc "Sorry!"
                scene 12_645 with Dissolve(1)
                mc "..."
                el "..."
        scene black with Dissolve(1)
        pause 2
        scene 12_646 with Dissolve(1)
        el "Since when?"
        mc "Since when what?"
        el "Do you have feelings for me."
        scene 12_647 with Dissolve(1)
        mc "The moment I saw you at school. In the reception office when we were both late."
        el "Heh... Yeah right."
        mc "Well, I was attracted to you."
        mc "And then the more time I spent with you and got to know you, the more I liked you."
        scene 12_648 with Dissolve(1)
        el "*Shakes head* Dios mío..."
        mc "{i}(And especially when you roll your eyes!){/i}"
        scene 12_649 with Dissolve(1)
        mc "What? It's the same for you!"
        mc "At first you didn't like me..."
        el "..."
        mc "But the more time you spend with me, you..."
        scene 12_650 with Dissolve(1)
        el "No. I still don't like you."
        mc "Right. I'm just imagining all that."
        el "All what?"
        scene 12_651 with Dissolve(1)
        mc "Training camp? The hot tub?"
        el "We were drinking and having fun. That's it."
        mc "That's it?"
        scene 12_652 with Dissolve(1)
        mc "I can see the way you look at me."
        el "How do I look?"
        mc "..."
        mc "{i}(Cute! Even when you're angry or upset.){/i}"
        scene 12_653 with Dissolve(1)
        mc "Okay... Then what about the beach?"
        el "What about it?"
        mc "Remember when I asked you if you were interested in someone and you said yes?"
        mc "But that he has a girlfriend?"
        el "..."
        scene 12_654 with Dissolve(1)
        mc "I know you were talking about me."
        mc "I just played dumb because I didn't want to make it awkward."
        el "..."
        scene 12_655 with Dissolve(1)
        el "It doesn't matter if I like you or not!"
        el "I will always choose Layla over you!"
        scene 12_656 with Dissolve(1)
        mc "And I will never make you choose."
        mc "But you always think about Layla, your brothers..."
        mc "When will you finally start thinking about yourself first for once?"
        el "..."
        scene 12_657 with Dissolve(1)
        mc "{i}(Yeah...){/i}"
        mc "{i}(What was I expecting to happen?){/i}"
        mc "{i}(That she'll be happy about this and jump into my arms?){/i}"
        mc "{i}(If I want to at least stay friends with Elena, I'll need to fix things with Layla...){/i}"
        scene 12_658 with Dissolve(1)
        mc "{i}(But this talk wasn't as bad as I expected it to be.){/i}"
        mc "{i}(When she came into the restaurant, she was ready to hit me, at least.){/i}"
        scene 12_659 with Dissolve(1)
        mc "Shall we head back inside?"
        mc "They must be close to finishing up their plates."
        el "Yeah."
        scene 12_660 with Dissolve(1)
        ""
        scene 12_661 with Dissolve(1)
        el "..."
        scene 12_662 with Dissolve(1)
        el "[mc]. One more thing."
        mc "Hmm?"
        el "*Sigh*"
        mc "{i}(She seems nervous. Is she...?){/i}"
        scene 12_663 with Dissolve(1)
        el "Uhm..."
        el "I can't afford the cheese balls."
        el "I..."
        scene 12_664 with Dissolve(1)
        mc "Good thing you didn't order any then."
        el "What?"
        mc "I ordered them. So, I'll pay."
        el "You don't..."
        scene 12_665 with Dissolve(1)
        mc "Elena! I'll pay!"
        el "..."
        el "Thanks."
        stop music fadeout 1.0
        play music ("Sounds/Restaurant_Background.mp3","Sounds/Restaurant_Background2.mp3","Sounds/Restaurant_Background3.mp3") volume 0.2
        scene 12_666 with Dissolve(1)
        el "Hey, guys. I'm back."
        di "Elena! I finished the whole plate! All of them!"
        el "Wow! Good job! You must've been hungry."
        di "Yeah! It was really good!"
        scene 12_667 with Dissolve(1)
        el "Thank you for keeping an eye on them."
        br "You're welcome. They're sweet."
        scene 12_668 with Dissolve(1)
        mc "Yeah. Thank you, Brooke."
        br "No problem."
        scene 12_669 with Dissolve(1)
        el "Finish your cola and then we're leaving."
        di "Already?"
        el "I still have stuff to do at home."
        di "Can [mc] come too?"
        mc "..."
        el "No. He has to work."
        scene 12_670 with Dissolve(1)
        el "Thanks for the food and drinks."
        mc "You're welcome."
        mc "And I'll call Layla. And if she doesn't pick up, I'll go to her place."
        el "Thanks."
        scene 12_671 with Dissolve(1)
        mc "Bye, Elena."
        el "Bye."
        ma "Bye, [mc]."
        mc "Bye-bye."
        scene 12_672 with Dissolve(1)
        br "What kinda magic did you use on her?"
        mc "Uh... What?"
        br "Well, when she came in, she was ready to kill you."
        scene 12_673 with Dissolve(1)
        mc "Oh that. No. It was just a misunderstanding."
        mc "I explained it and we're good now."
        mc "{i}(I hope...){/i}"
        br "Hmm..."
    else:
        pass
    if Week3_Monday_Spanish_Blackmail == False:
        scene black with Dissolve(1)
        pause 2
        scene 12_674 with Dissolve(1)
        mc "How was everything?"
        xv "It was perfect. Compliments to the chef."
        mc "Thank you. I'll tell her."
        scene 12_675 with Dissolve(1)
        mc "Can I get you something else?"
        xv "I think we're good. Or do you want another drink, Gabs?"
        tr "No, I'm good."
        xv "Then just the check, please."
        if Gabi_End == False:
            scene 12_676 with Dissolve(1)
            mc "Here you go."
            xv "Oh, so I'm the one who has to pay, huh?"
            mc "Uh... I'm sorry. You're right. I shouldn't assume."
            mc "I should've just put it on the table."
            scene 12_677 with Dissolve(1)
            xv "Haha. I'm joking."
            xv "Of course I'm paying."
            scene 12_678 with Dissolve(1)
            tr "What do you mean by 'of course, I'm paying'?"
            tr "Who paid for drinks yesterday?"
            if Layla_End == True:
                xv "That's why I said that I'm paying."
                tr "Uh-huh."
                mc "{i}(It's funny to see Gabi like this.){/i}"
            else:
                if Layla_Week5_Wednesday_ClubDate == True:
                    scene 12_679 with Dissolve(1)
                    xv "He did."
                    mc "..."
                    tr "He bought me one drink!"
                    mc "{i}(It's funny to see Gabi like this.){/i}"
                else:
                    if Alexis_Week5_Wednesday_Beach == True:
                        scene 12_679 with Dissolve(1)
                        xv "He did."
                        mc "..."
                        tr "He bought me one drink!"
                        mc "{i}(It's funny to see Gabi like this.){/i}"
                    else:
                        xv "That's why I said that I'm paying."
                        tr "Uh-huh."
                        mc "{i}(It's funny to see Gabi like this.){/i}"
            scene 12_680 with Dissolve(1)
            xv "Here you go!"
            mc "Thank you very much."
        else:
            pass
        menu:
            "Ask for a picture[KoGa3AutoWTChange1]{size=-4}(Brooke Week5 Thursday Picture, Brooke Points+2, {i}Gabi End: Gabi Week5 Thursday Picture{/i}) {/size} {/color}":
                $ Brooke_Week5_Thursday_Picture = True
                $ Brooke_Points += 2
                # Brooke (10)
                scene 12_682 with Dissolve(1)
                mc "Uhm... Could I ask for a favour?"
                xv "Depends."
                mc "My colleague is a big fan of the show. Would you mind taking a picture with her?"
                xv "Sure. Of course."
                mc "Thank you. I'll go get her. Be right back."
                scene 12_683 with Dissolve(1)
                mc "Heeey, Brookie."
                br "What did you do?"
                mc "Nothing. Why are you assuming I did something?"
                br "Just a feeling."
                mc "Just come with me for a second."
                scene 12_684 with Dissolve(1)
                br "Why?"
                mc "Ximena Vergara is leaving. Come take a picture with her!"
                br "I'm not gonna ask for a picture, [mc]."
                scene 12_685 with Dissolve(1)
                mc "Well, here's the good news. You don't have to. I already did!"
                br "You did what?"
                mc "I asked her and she said yes!"
                br "[mc]..."
                scene 12_686 with Dissolve(1)
                mc "Come on. Don't let her wait."
                br "This is so embarrassing!"
                mc "It's not!"
                scene 12_687 with Dissolve(1)
                br "You really did ask, right?"
                mc "Haha. I swear I did!"
                mc "Don't be so nervous. It's just a picture."
                scene 12_688 with Dissolve(1)
                br "I'm really sorry."
                br "I..."
                xv "Don't be, it's fine."
                xv "I'm happy to take a picture with you."
                scene 12_689 with Dissolve(1)
                xv "What's your name?"
                br "Brooke."
                xv "Nice to meet you, Brooke."
                br "It's nice to meet you too, Ms Vergara."
                scene 12_690 with Dissolve(1)
                mc "Alright."
                mc "Smile in three... two... one..."
                scene 12_691 with Dissolve(1)
                br "Thank you so very much!"
                xv "My pleasure, Brooke."
                if Gabi_End == True:
                    scene 12_692 with Dissolve(1)
                    xv "Bye, guys. Thank you for the amazing food!"
                    br "Bye."
                    mc "See you next week, Ms Ramirez."
                    tr "Bye..."
                else:
                    $ Gabi_Week5_Thursday_Picture = True
                    scene 12_693 with Dissolve(1)
                    xv "Do you also want a picture?"
                    mc "Uhm... No, it's..."
                    xv "Come on."
                    scene 12_694 with Dissolve(1)
                    br "I'll take the picture for you."
                    mc "Thanks."
                    br "*Whispers* Show me your biggest smile!"
                    mc "*Whispers* Shut up..."
                    scene 12_695 with Dissolve(1)
                    xv "You're actually quite tall."
                    mc "Above average I'd say."
                    xv "A little more than that."
                    scene 12_696 with Dissolve(1)
                    xv "Gabs, you get in here too!"
                    tr "No, no, I'm good."
                    mc "{i}(I wouldn't mind having her in the picture as well.){/i}"
                    xv "Just one picture. Ándale!"
                    scene 12_697 with Dissolve(1)
                    tr "..."
                    mc "..."
                    scene 12_698 with Dissolve(1)
                    tr "Uh..."
                    scene 12_699 with Dissolve(1)
                    tr "*Whispers* Not here!"
                    mc "{i}(She didn't say stop...){/i}"
                    mc "*Whispers* When can we meet again?"
                    tr "..."
                    scene 12_700 with Dissolve(1)
                    br "Ready?"
                    mc "Yeah. Go ahead."
                    br "Three... two... one..."
                    scene 12_701 with Dissolve(1)
                    ""
                    scene 12_702 with Dissolve(1)
                    mc "Thank you very much for the picture."
                    mc "The both of you!"
                    xv "You're very welcome!"
                    scene 12_703 with Dissolve(1)
                    mc "Well, have a nice rest of your day. And we hope to see you again."
                    xv "Thank you. I'm sure you will."
                    br "Bye-bye."
                    mc "Bye, Gabriela, Ms Vergara."
                    xv "Heh. Bye, Mr Vicari!"
                    scene 12_704 with Dissolve(1)
                    tr "Seriously, Ximena. Don't involve me in your schemes."
                    xv "What schemes? You saw the look on his face!"
                    xv "Ask for a copy of the picture next time you see each other."
                    tr "I'll tell him to delete it!"
                scene 12_705 with Dissolve(1)
                pz "Ximena!"
                pz "Ximena! Over here!"
                br "There we go again. Good thing they didn't come inside."
                mc "Heh, yeah."
                scene 12_706 with Dissolve(1)
                br "Can you show me the picture?"
                mc "One second."
                br "Can you also send it to me?"
                mc "Of course."
                scene 12_707 with Dissolve(1)
                br "Why do I look so weird?"
                mc "You don't look weird."
                br "Look at the face I'm making."
                mc "What face? You always look like that."
                scene 12_708 with Dissolve(1)
                br "Hey!"
                mc "That's a compliment!"
                mc "I meant it as you look pretty."
                scene 12_709 with Dissolve(1)
                br "Not as pretty as she is."
                br "Look at her."
                mc "{i}(She's right. I actually might check out that TV show.){/i}"
                mc "Someone's having a new crush!"
                br "No-no-no. That's still Emily!"
                scene 12_710 with Dissolve(1)
                m "What's still me?"
                br "..."
                mc "..."
                scene 12_711 with Dissolve(1)
                mc "Oh hey, Mom."
                mc "We were just talking about... celebrities. In general."
                m "Celebrities? I'm not a celebrity."
                if MC_Bike == True:
                    mc "To me, you are!"
                    scene 12_712 with Dissolve(1)
                    m "Thank you."
                    m "You're so sweet!"
                else:
                    pass
                scene 12_713 with Dissolve(1)
                m "Oh... Were you maybe talking about Ximena Vergara?"
                m "She had a reservation for today if I remember correctly."
                mc "Yeah. She left a few minutes ago."
                m "Bummer. Would've loved to take a picture with her."
                scene 12_714 with Dissolve(1)
                mc "See, Brooke!"
                mc "Nothing wrong with that. Even the owner wants a picture."
                m "Hmm?"
                scene 12_715 with Dissolve(1)
                mc "Nothing. But Brooke has a picture with her."
                m "You do? Can I see it?"
                br "Sure. [mc] has it on his phone."
                scene 12_716 with Dissolve(1)
                m "Such a nice photo."
                m "Two pretty ladies."
                br "Thank you."
                scene 12_717 with Dissolve(1)
                m "I'm a little jealous."
                mc "You don't have to be jealous. You can take a picture with Brooke any day."
                br "She was talking about..."
                scene 12_718 with Dissolve(1)
                m "You know what? You're right."
                m "Let's take a picture, Brooke!"
                br "Uh... Okay..."
                scene 12_719 with Dissolve(1)
                mc "Alright. Ready?"
                m "Mm-hmm."
                mc "Three... two... one... Perfect!"
                scene 12_720 with Dissolve(1)
                mc "Here, check it out. What do you think?"
                m "Beautiful!"
                mc "Two celebrities."
                m "Haha."
                scene 12_721 with Dissolve(1)
                m "Anyway. I have to leave for about an hour."
                m "I need to head to the café."
                m "Brooke, can you take care of things here?"
                br "Of course."
                scene 12_722 with Dissolve(1)
                m "Thank you. See you guys later then."
                mc "Later, Mom."
                br "Bye, Emily."
                scene 12_723 with Dissolve(1)
                br "Let's get back to work, too."
                mc "Yeah."
                mc "By the way. Do you want a copy of that picture?"
                br "Do you even have to ask?"
                scene 12_724 with Dissolve(1)
                mc "Oh, so I can delete it?"
                br "What? No!"
                mc "Haha."
                mc "Don't worry. I'll send it to you."
                scene 12_725 with Dissolve(1)
                br "How about you check on table seven!"
                if Brooke_Week5_Thursday_MommyBrooke == False:
                    mc "Sure."
                else:
                    mc "Anything for you, Mommy Brooke!"
                br "*Sigh* I should've kept my mouth shut."
                mc "Haha."
            "Leave":
                scene 12_681 with Dissolve(1)
                mc "Well, have a nice rest of your day. And we hope to see you again."
                xv "Thank you. I'm sure you will."
                if Gabi_End == False:
                    mc "Bye, Gabi, Ms Vergara."
                    xv "Heh. Bye, Mr Vicari!"
                else:
                    mc "Bye, Ms Ramirez, Ms Vergara."
                    tr "Bye, [mc]."
    else:
        pass
    if Erynn_Week3_Monday_Blackmailhelp == True:
        scene black with Dissolve(1)
        pause 2
        scene 12_767 with Dissolve(1)
        mc "{i}(Only half an hour to go and my shift is over.){/i}"
        mc "{i}(What should I do after?){/i}"
        play sound "Sounds/Phone_Vibrate.mp3"
        n "*Bzzzt. Bzzzt*"
        mc "..."
        if Erynn_Week5_Thursday_Photo == True:
            scene 12_768 with Dissolve(1)
            n "*Bzzzt. Bzzzt*"
            mc "{i}(Oh, it's Erynn again.){/i}"
            mc "{i}(The photo shoot should definitely be finished by now. I hope nothing else happened.){/i}"
            play sound "Sounds/Phone_Vibrate.mp3"
            n "*Bzzzt. Bzzzt*"
            scene 12_769 with Dissolve(1)
            mc "Hey again, Erynn."
            er "Hey."
            mc "Everything alright? The photo shoot must have ended by now, right? Did something happen?"
            scene 12_770 with Dissolve(1)
            er "All's fine. We finished a couple of hours ago. Are you still at work?"
            mc "Only thirty minutes to go."
            if Erynn_Week5_Thursday_Shower == False:
                er "Okay..."
            else:
                scene 12_771 with Dissolve(1)
                mc "Did you get all the paint off? Or else I'll come over and help you."
                er "It's off."
                mc "Little bummed about that!"
                er "Yeah..."
        else:
            scene 12_768 with Dissolve(1)
            n "*Bzzzt. Bzzzt*"
            mc "{i}(Oh, it's Erynn.){/i}"
            scene 12_769 with Dissolve(1)
            mc "Hey, Erynn."
            er "Hey."
            mc "How are ya?"
            scene 12_770 with Dissolve(1)
            er "I'm good. How are you? Are you still at work?"
            mc "Almost finished. Only thirty minutes until the shift change."
            er "Okay..."
        scene 12_772 with Dissolve(1)
        mc "What's wrong?"
        er "Nothing."
        mc "I can hear it in your voice that something's going on, Erynn."
        scene 12_773 with Dissolve(1)
        er "*Sigh*"
        er "Remember when we were at the garage, with John?"
        mc "Well, yeah..."
        er "I said that I would tell you when Ethan will be at his favourite bar."
        scene 12_774 with Dissolve(1)
        mc "He is there right now?"
        er "No, but he will be in like two hours. I heard them talking about it during the shoot."
        mc "Oh... Okay... Uhm..."
        mc "I'll call John and ask if he has time."
        scene 12_775 with Dissolve(1)
        er "What are you going to do?"
        mc "Me, nothing. If Ethan sees me there, he'd probably suspect something's up."
        mc "I don't know if John wants to talk to him or just go look what we're dealing with."
        er "Hmm..."
        scene 12_776 with Dissolve(1)
        er "What should I do?"
        mc "Absolutely nothing!"
        er "But I..."
        mc "No, Erynn. Just stay home!"
        er "..."
        scene 12_777 with Dissolve(1)
        mc "Erynn!"
        er "Yes... Yes! I'll stay home. I promise!"
        mc "Thanks."
        scene 12_778 with Dissolve(1)
        mc "I'll call John now. If it doesn't work out, I'll let you know."
        mc "Or else I'll call you afterwards and tell you what happened."
        er "Alright."
        scene 12_779 with Dissolve(1)
        er "Be careful, okay? The both of you."
        mc "We will. Don't worry."
        mc "Speak to you later. Bye, Erynn."
        er "Bye, [mc]."
        scene 12_780 with Dissolve(1)
        er "*Sigh*"
        scene black with Dissolve(1)
        pause 2
        scene 12_781 with Dissolve(1)
        mc "{i}(Let's see if John has time today.){/i}"
        mc "{i}(I hope he does. Who knows when we'll get another chance.){/i}"
        scene 12_782 with Dissolve(1)
        ir "Hey!"
        mc "Uh... Iris?"
        mc "Is John there?"
        scene 12_783 with Dissolve(1)
        ir "No hey, or how are you?"
        mc "{i}(Where have I heard that before?){/i}"
        mc "Sorry..."
        mc "Hey. How are you, Iris?"
        scene 12_784 with Dissolve(1)
        ir "I'm good. How are you?"
        mc "Also good. You're helping your dad again today?"
        ir "Not just today. It's my job. I'm here every day."
        mc "Ah... Didn't know that. I thought it was more like part-time."
        scene 12_785 with Dissolve(1)
        ir "And that's why we should hang out more, so we can talk!"
        mc "Yeah, we should do that."
        if MC_Bike == True:
            if Iris_Points >= 1:
                $ Iris_Week5_Thursday_BikeRepair = True
                scene 12_786 with Dissolve(1)
                ir "I'm working on my bike at the moment so we can ride together sometime. Since you have one too, now."
                ir "When you have some time one of these days. Why don't you come over and help me?"
                mc "Sure. Sounds fun. Just like old times."
                scene 12_787 with Dissolve(1)
                ir "Old times... It hasn't been that long!"
                mc "You know what I mean."
                ir "..."
            else:
                pass
        else:
            pass
        scene 12_788 with Dissolve(1)
        mc "But I really need to talk to John right now."
        mc "It's kinda important. Is he there?"
        ir "Yeah. I'll go get him."
        mc "Thanks."
        scene 12_789 with Dissolve(1)
        ir "Dad!"
        jo "Hmm?"
        ir "Phone."
        scene 12_790 with Dissolve(1)
        jo "Thanks. Who is it?"
        ir "[mc]."
        scene 12_791 with Dissolve(1)
        jo "Hey, [mc]."
        mc "Hey, John. How are you?"
        if MC_Bike == False:
            jo "Good-good. How are you?"
            mc "I'm good."
        else:
            jo "Good-good. How are you? How's the bike? Did you have a chance already to drive it?"
            mc "I did. It's amazing. Thanks again."
            jo "No need to thank me, thank your mom!"
        scene 12_792 with Dissolve(1)
        jo "What's up?"
        mc "I'm calling because of the uh Erynn situation."
        jo "Right. How is she holding up?"
        mc "She's good. At least I think she is. She's very good at hiding how she really feels."
        jo "Hmm..."
        scene 12_793 with Dissolve(1)
        mc "She called me a few minutes ago, telling me that Ethan will be at his favourite bar today."
        mc "And you said you wanted to meet him or..."
        jo "Check who we're dealing with first."
        mc "Yeah. Do you have time today?"
        scene 12_794 with Dissolve(1)
        jo "Is he there now?"
        mc "No. Erynn said in like two hours."
        jo "I can make that. What kinda bar is it?"
        mc "I've never been myself so I had to look it up."
        scene 12_795 with Dissolve(1)
        mc "It's called Prestige."
        mc "And it's not really a typical bar, but more like a gentlemen's club vibe. But not a strip club."
        jo "Alright. Where is it located?"
        mc "I can come with you and show you. But I won't come into the bar. Can't have Ethan seeing me there."
        scene 12_796 with Dissolve(1)
        jo "Sounds good. I'll come pick you up then once I'm ready."
        jo "It will be at least one and a half hours though."
        mc "That's fine."
        scene 12_797 with Dissolve(1)
        mc "Thanks for doing this, John! I really appreciate it."
        jo "Hey. Don't worry about it."
        jo "Let me get ready and I'll see you later then."
        mc "Okay. Later, John."
        jo "Bye."
        scene 12_798 with Dissolve(1)
        jo "Iris. I'll have to leave for a few hours."
        ir "Everything alright?"
        jo "Hmm? Yeah. I'm going to a bar with [mc]."
        scene 12_799 with Dissolve(1)
        ir "Oh... Can I come?"
        jo "..."
        scene 12_800 with Dissolve(1)
        jo "No. I can't just close down the garage."
        jo "We have some clients coming to pick up their cars later."
        jo "Then there's still the paperwork. And the one from yesterday, since I gave you the day off."
        ir "..."
        jo "You can look as angry as you want. I'm not changing my mind."
        scene 12_801 with Dissolve(1)
        jo "I'm not [mc]. That doesn't work on me either!"
        ir "..."
        scene 12_802 with Dissolve(1)
        ir "*Sigh* Fine... Go have your fun!"
        jo "Thank you!"
        jo "Want me to bring some food after?"
        ir "Pizza! And ice-cream! Chocolate flavour. The good one!"
        jo "Of course."
        scene 12_803 with Dissolve(1)
        jo "See you later."
        ir "Yeah..."
        jo "Love you!"
        if Iris_Points >= 1:
            scene 12_804 with Dissolve(1)
            ir "Your beard pricks!"
            jo "Now you'll have to get used to it, since [mc] has a beard too!"
            ir "He has some stubble!"
            scene 12_805 with Dissolve(1)
            jo "Still a beard!"
            ir "Heh..."
            jo "Later!"
            ir "Bye..."
            scene 12_806 with Dissolve(1)
            ir "*Whispers* We aren't even..."
        else:
            pass
    else:
        pass
    jump Week5_Thursday_Restaurant_End_Brooke

label Week5_Thursday_Restaurant_End_Brooke:
    scene black with Dissolve(1)
    pause 2
    scene 12_726 with Dissolve(1)
    mc "Haaah... This is the best part of having a job."
    br "The time when the shift ends?"
    mc "Exactly!"
    br "Haha."
    if Brooke_Points >= 7:
        scene 12_727 with Dissolve(1)
        mc "Uh..."
        br "Not the money?"
        mc "Oh... The money! Of course, it's the money. How could I forget that?"
        scene 12_728 with Dissolve(1)
        br "But the shift ending is definitely second place."
        mc "Hehe, yeah."
        scene 12_729 with Dissolve(1)
        br "What are you going to do the rest of the day?"
        mc "..."
        br "[mc]...?"
        mc "Sorry, what?"
        scene 12_730 with Dissolve(1)
        br "What are you going to do now?"
        mc "Oh... Uhm... Let's see."
        mc "I have a few hours so I'll probably just go home and maybe watch an episode of that TV show."
        if Brooke_Week5_Thursday_Picture == False:
            br "Haha, okay."
        else:
            $ Ximena_Week5_Thursday_Watch = True
            scene 12_731 with Dissolve(1)
            br "Haha, okay."
            br "Want to check out Ximena?"
            mc "{i}(Yes...){/i}"
            mc "No, just..."
            br "Watch season two episode six. You can thank me later!"
            scene 12_732 with Dissolve(1)
            mc "Is there a sex scene with her or something?"
            br "No."
            mc "Nude scene?"
            br "I'm not telling you, or else you'll say I spoil everything again."
            scene 12_733 with Dissolve(1)
            mc "Fine... Season two episode six?"
            br "Yes."
            br "Or just start from the beginning and watch all the episodes. Trust me, it's worth it."
            mc "You really should come over sometime and watch it with me then. Or with Mom..."
            br "..."
        scene 12_734 with Dissolve(1)
        br "And what are you doing after? Since you said you've got a few hours."
        mc "Going to watch the Marauders."
        br "You've got tickets?"
        scene 12_735 with Dissolve(1)
        mc "No. I'm going to a bar to watch it there."
        mc "I wish I had tickets though."
        mc "Haven't been in the arena in forever."
        br "Same."
        scene 12_736 with Dissolve(1)
        mc "You're a Marauders fan?"
        br "My dad and brother are, and I get to go with them sometimes. But it's been years."
        mc "I didn't know you have a brother. Younger, older?"
        scene 12_737 with Dissolve(1)
        br "Zane. He's a year younger."
        mc "{i}(Zane?){/i}"
        mc "{i}(Must be a common name. I keep hearing it everywhere.){/i}"
        scene 12_738 with Dissolve(1)
        mc "So he is..."
        br "Twenty-one."
        br "He also goes to the beach very often and does some surfing."
        br "I think you would get along."
        mc "Yeah, probably."
        scene 12_739 with Dissolve(1)
        br "Who are the Marauders playing today?"
        mc "Eclipse."
        br "That's a big game!"
        mc "Yeah. Gatling vs Adler. Probably this year's finals also. And MVP-race."
        scene 12_740 with Dissolve(1)
        mc "What are you going to do?"
        br "I have to do some grocery shopping, laundry, and other chores."
        mc "Oh, that kinda day."
        br "Yes. That kinda day."
        scene 12_741 with Dissolve(1)
        mc "Do you still live at home or do you have your own place?"
        br "My own place. Well, I share an apartment with two other girls."
        mc "Oooh..."
        scene 12_742 with Dissolve(1)
        br "They both have boyfriends."
        mc "I wasn't..."
        br "Mm-hmm. I could see it on your face."
        mc "Haha."
        scene 12_743 with Dissolve(1)
        br "Anyway. I'll go change now and get going."
        mc "Yeah, same."
        scene black with Dissolve(1)
        pause 2
        if MC_Bike == True:
            $ Brooke_Week5_Thursday_BikeRide = True
            scene 12_744 with Dissolve(1)
            br "When is the next time you'll be at work?"
            mc "I don't know. Mom hasn't said anything yet."
            mc "Maybe a day at the weekend?"
            scene 12_745 with Dissolve(1)
            mc "Why? You want me here that badly?"
            br "It's always fun when you're here."
            mc "An extra person to boss around, huh?"
            br "That too!"
            scene 12_746 with Dissolve(1)
            mc "The invitation is still there."
            mc "If you ever wanna hang out after work, you can always come over."
            br "Thanks."
            scene 12_749 with Dissolve(1)
            br "What are you doing?"
            mc "Hmm?"
            br "Wait... Is that yours?"
            scene 12_750 with Dissolve(1)
            mc "It is."
            br "I didn't know you had a bike."
            mc "I haven't had it that long yet. Just a few days."
            scene 12_751 with Dissolve(1)
            br "It looks really cool. And fast!"
            mc "Oh, it's fast!"
            mc "Want a ride?"
            scene 12_752 with Dissolve(1)
            br "I'd love to but I don't have time today."
            mc "Yeah, I don't know why I asked. I didn't bring my spare helmet, so it wouldn't have been possible anyway. Sorry."
            br "It's fine."
            mc "How about next time I have to come to work?"
            mc "I'll bring an extra helmet and I can drive you home after?"
            scene 12_753 with Dissolve(1)
            br "Okay."
            mc "Okay?"
            br "Okay!"
            mc "Haha."
            scene 12_754 with Dissolve(1)
            br "Can't wait until next time!"
            mc "Mm-hmm."
            scene 12_755 with Dissolve(1)
            mc "By the way. That was the second kiss already! You're catching up quickly."
            br "Haha. Who knows?"
            br "Bye-bye."
            if Brooke_Week5_Thursday_MommyBrooke == False:
                mc "Bye, Brooke!"
            else:
                mc "Bye, Brooke! I mean Mommy Brooke!"
                br "Haha."
        else:
            scene 12_744a with Dissolve(1)
            br "When is the next time you'll be at work?"
            mc "I don't know. Mom hasn't said anything yet."
            mc "Maybe a day at the weekend?"
            scene 12_745a with Dissolve(1)
            mc "Why? You want me here that badly?"
            br "It's always fun when you're here."
            mc "An extra person to boss around, huh?"
            br "That too!"
            scene 12_746a with Dissolve(1)
            mc "The invitation is still there."
            mc "If you ever wanna hang out after work, you can always come over."
            br "Thanks."
            scene 12_748 with Dissolve(1)
            br "See you next time then!"
            mc "Mm-hmm."
            scene 12_747a with Dissolve(1)
            mc "By the way. That was the second kiss already! You're catching up quickly."
            br "Haha. Who knows?"
            br "Bye-bye."
            if Brooke_Week5_Thursday_MommyBrooke == False:
                mc "Bye, Brooke!"
            else:
                mc "Bye, Brooke! I mean Mommy Brooke!"
                br "Haha."
    else:
        scene 12_756 with Dissolve(1)
        br "Not the money?"
        mc "Oh... The money! Of course, it's the money. How could I forget that?"
        br "But the shift ending is definitely second place."
        mc "Hehe, yeah."
        scene 12_757 with Dissolve(1)
        br "What are you going to do the rest of the day?"
        mc "Oh... Uhm... Let's see."
        mc "I have a few hours so I'll probably just go home and maybe watch an episode of that TV show."
        br "Tell me if you like it or not."
        mc "I will."
        scene 12_758 with Dissolve(1)
        br "And what are you doing after?"
        mc "Going to watch the Marauders."
        br "You've got tickets?"
        scene 12_759 with Dissolve(1)
        mc "No. I'm going to a bar to watch it there."
        mc "I wish I had tickets, though."
        mc "Haven't been in the arena in forever."
        br "Same."
        scene 12_760 with Dissolve(1)
        mc "You're a Marauders fan?"
        br "My dad and brother are, and I get to go with them sometimes. But it's been years."
        mc "I didn't know you have a brother. Younger, older?"
        scene 12_761 with Dissolve(1)
        br "Zane. He's a year younger."
        mc "{i}(Zane?){/i}"
        mc "{i}(Must be a common name. I keep hearing it everywhere.){/i}"
        scene 12_762 with Dissolve(1)
        mc "So he is..."
        br "Twenty-one."
        br "He also goes to the beach very often and does some surfing."
        br "I think you would get along."
        mc "Yeah, probably."
        scene 12_763 with Dissolve(1)
        br "Who are the Marauders playing today?"
        mc "Eclipse."
        br "That's a big game!"
        mc "Yeah. Gatling vs Adler. Probably this year's finals also. And MVP-race."
        scene 12_764 with Dissolve(1)
        mc "What are you going to do?"
        br "I have to do some grocery shopping, laundry and other chores."
        mc "Oh, that kinda day."
        br "Yes. That kinda day."
        scene 12_765 with Dissolve(1)
        mc "Do you still live at home or do you have your own place?"
        br "My own place. Well, I share an apartment with two other girls."
        mc "Oooh..."
        scene 12_742 with Dissolve(1)
        br "They both have boyfriends."
        mc "I wasn't..."
        br "Mm-hmm. I could see it on your face."
        mc "Haha."
        scene 12_766 with Dissolve(1)
        br "Anyway. I'll go change now and get going."
        mc "Yeah, same."
        scene black with Dissolve(1)
        pause 2
        if MC_Bike == True:
            scene 12_744 with Dissolve(1)
            br "When is the next time you'll be at work?"
            mc "I don't know. Mom hasn't said anything yet."
            mc "Maybe a day at the weekend?"
            scene 12_745 with Dissolve(1)
            mc "Why? You want me here that badly?"
            br "It's always fun when you're here."
            mc "An extra person to boss around, huh?"
            br "That too!"
            scene 12_747 with Dissolve(1)
            br "See you next time then!"
            mc "Mm-hmm."
            br "Bye-bye."
            mc "Bye, Brooke!"
        else:
            scene 12_744a with Dissolve(1)
            br "When is the next time you'll be at work?"
            mc "I don't know. Mom hasn't said anything yet."
            mc "Maybe a day at the weekend?"
            scene 12_745a with Dissolve(1)
            mc "Why? You want me here that badly?"
            br "It's always fun when you're here."
            mc "An extra person to boss around, huh?"
            br "That too!"
            scene 12_747a with Dissolve(1)
            br "See you next time then!"
            mc "Mm-hmm."
            br "Bye-bye."
            mc "Bye, Brooke!"
    jump Week5_Thursday_Afternoon

label Week5_Thursday_Afternoon:
    scene black with Dissolve(1)
    pause 2
    stop music fadeout 1.0
    play music ("Music/LoFi Indie 3.mp3", "Music/LoFi Indie 1.mp3", "Music/LoFi Indie 2.mp3") volume 0.2
    if Layla_Week5_Wednesday_BreakUp == True:
        scene 12_807 with Dissolve(1)
        mc "{i}(Let's see if Layla even picks up.){/i}"
        mc "{i}(Should I leave a voicemail if she doesn't?){/i}"
        mc "{i}(No, that would be a cop out.){/i}"
        scene 12_808 with Dissolve(1)
        mc "{i}(It's ringing at least.){/i}"
        mc "{i}(Meaning she hasn't blocked me. Yet...){/i}"
        mc "{i}(She isn't picking up though.){/i}"
        scene 12_809 with Dissolve(1)
        mc "*Sigh*"
        mc "{i}(I wouldn't pick up, either.){/i}"
        mc "{i}(I'll try again tomorrow.){/i}"
    else:
        pass
    if Erynn_Week3_Monday_Blackmailhelp == True:
        scene 12_810 with Dissolve(1)
        mc "{i}(I still have some time before John arrives.){/i}"
        mc "{i}(Why does time always go by so slowly when you're waiting for something?){/i}"
        mc "{i}(What should I do in the meantime?){/i}"
    else:
        scene 12_810 with Dissolve(1)
        mc "{i}(I still have some time before the game.){/i}"
        mc "{i}(But what should I do?){/i}"
    if Week3_Monday_Spanish_Blackmail == False:
        if Ximena_Week5_Thursday_Watch == True:
            mc "{i}(I can watch an episode of Entanglement maybe?){/i}"
            mc "{i}(What did Brooke say? Season two episode six?){/i}"
            mc "{i}(Let's see!){/i}"
            scene black with Dissolve(1)
            pause 2
            scene 12_814 with Dissolve(1)
            mc "{i}(Can't believe I'm actually enjoying this!){/i}"
            mc "{i}(She's so fucking hot!){/i}"
            scene black with Dissolve(1)
            pause 2
            scene 12_815 with Dissolve(1)
            mc "{i}(Is this the scene why Brooke mentioned this particular episode?){/i}"
            mc "{i}(Must be, right?){/i}"
            scene 12_816 with Dissolve(1)
            mc "{i}(I'm getting turned on so much!){/i}"
            mc "{i}(What a fucking lucky bastard!){/i}"
            mc "{i}(Cameraman, you'd better do your job!){/i}"
            show 12_817
            pause 2
            mc "{i}(She even looks good from behind.){/i}"
            scene 12_818 with Dissolve(1)
            mc "{i}(Look at that ass!){/i}"
            scene 12_819 with Dissolve(1)
            mc "Ximena!"
            scene 12_820 with Dissolve(1)
            mc "Ximena!"
            scene 12_821 with Dissolve(1)
            mc "Ahhh..."
            mc "Fuck!"
        else:
            mc "{i}(I can watch an episode of Entanglement maybe?){/i}"
            mc "{i}(Yeah, why not? Let's watch some Ximena!){/i}"
            scene black with Dissolve(1)
            pause 2
            scene 12_811 with Dissolve(1)
            mc "{i}(Can't believe I'm actually enjoying this!){/i}"
            mc "{i}(She's so fucking hot!){/i}"
            scene 12_813 with Dissolve(1)
            mc "{i}(Will there be nude scenes with her as well?){/i}"
    else:
        mc "{i}(I'll just watch some funny videos, I guess.){/i}"
        scene 12_812 with Dissolve(1)
        ""
    if Erynn_Week3_Monday_Blackmailhelp == True:
        jump Week5_Thursday_John
    else:
        jump Week5_Thursday_DylansBar

label Week5_Thursday_John:
    scene black with Dissolve(1)
    pause 2
    scene 12_822 with Dissolve(1)
    n "*Ding-dong*"
    mc "{i}(That must be John.){/i}"
    scene 12_823 with Dissolve(1)
    mc "Hey, John."
    jo "Hey."
    scene black with Dissolve(1)
    transform moveup:
        xalign 0.5 yalign 1.0
        linear 5.0 yalign 0.0
    show 12_824 at moveup
    pause 3
    mc "Look at you. I think I've never seen you in a suit before."
    mc "You look good."
    jo "Thanks."
    scene 12_825 with Dissolve(1)
    jo "Gotta dress the part. Can't just show up in a greasy tank and draw too much attention."
    mc "You're the kinda guy who'll always draw attention when you enter a room. Doesn't matter what you wear or do."
    jo "Haha."
    jo "Ready to go?"
    mc "Yeah."
    scene 12_826 with Dissolve(1)
    mc "What...? I didn't know you drove a Porsche!"
    jo "It's a client's car. I installed a new gear system. I needed to test drive it, so why not now?"
    mc "Heh, I see. Dress the part. Not just with clothes, huh?"
    scene 12_827 with Dissolve(1)
    jo "Do you want to drive? You probably know the way."
    mc "Can I? Fuck yeah!"
    mc "I mean. Every successful businessman needs a driver, right?"
    jo "Exactly."
    scene 12_828 with Dissolve(1)
    jo "Time to get serious now. What does the guy actually look like?"
    jo "Do you have a picture or something?"
    mc "He surely must have social media with some pictures on it. Let me check."
    scene 12_829 with Dissolve(1)
    jo "Hmm, okay... I'll recognise him when he shows up."
    mc "He'll most likely come with a group of goons."
    mc "Are you going to talk to him, or...?"
    jo "Mostly just watch and observe to see what he's all about."
    jo "I'm not going out of my way to talk to him but if there's an opportunity, I will."
    scene black with Dissolve(1)
    pause 2
    scene 12_830 with Dissolve(1)
    mc "Want me to drop you off at the entrance and open the door?"
    jo "Haha, no. I'm not a celebrity!"
    mc "Hehe, okay. Speaking of celebrities. I met one today."
    jo "Yeah? Who?"
    scene 12_831 with Dissolve(1)
    mc "Ximena Vergara."
    jo "I don't know who that is."
    mc "She's an actress. Has a role in Entanglement."
    jo "I don't even know what Entanglement is."
    mc "Haha, fair enough. To be honest, me neither until a few weeks ago. But everyone seems to be talking about it."
    scene 12_832 with Dissolve(1)
    jo "What is it? A movie? TV show?"
    mc "TV show. Lots of intrigue, drama, romance..."
    jo "All the stuff I like."
    mc "Haha."
    if MC_Bike == True:
        $ John_Week5_Thursday_BikeRide = True
        scene 12_833 with Dissolve(1)
        jo "By the way. When are we going for a ride?"
        mc "You mean with the bikes?"
        jo "Mm-hmm."
        mc "Uhm... Whenever you have time. I can go after school, the weekends. Basically every day."
        jo "I'll check my schedule then and plan a nice route."
        mc "Cool."
    else:
        pass
    scene black with Dissolve(1)
    pause 2
    scene 12_834 with Dissolve(1)
    mc "This is it."
    mc "I'll let you out here and go park around the back."
    mc "I'll wait there for you."
    scene 12_835 with Dissolve(1)
    jo "Let's hope he shows up."
    mc "Indeed. Good luck!"
    jo "Thanks. If anything changes or something, call me, alright?"
    mc "Will do."
    scene 12_836 with Dissolve(1)
    ""
    scene 12_837 with Dissolve(1)
    mc "*Sigh...*"
    mc "{i}(I'm the one sitting in the car, doing nothing.){/i}"
    mc "{i}(Why am I so nervous?){/i}"
    mc "{i}(I hope everything goes well...){/i}"
    scene 12_838 with Dissolve(1)
    stop music fadeout 1.0
    play music "Sounds/Bar_Background2.mp3" volume 0.2
    ""
    scene 12_839 with Dissolve(1)
    bt "Good evening, sir."
    jo "Good evening."
    bt "What can I get you?"
    jo "Whiskey, please."
    scene 12_840 with Dissolve(1)
    jo "..."
    scene 12_841 with Dissolve(1)
    jo "..."
    scene 12_842 with Dissolve(1)
    mc "{i}(Man... I hate waiting like this. I don't have the patience for it.){/i}"
    mc "{i}(I really wanna know what's going on.){/i}"
    mc "{i}(Is Ethan there yet?){/i}"
    scene 12_843 with Dissolve(1)
    jo "{i}(No, I haven't se...){/i}"
    x "Haha, Ethan."
    jo "..."
    scene 12_844 with Dissolve(1)
    et "Let's have some fun. Who wants some Crystal?"
    gr "I do!"
    jo "{i}(That's him.){/i}"
    scene 12_845 with Dissolve(1)
    jo "{i}(He's just arrived.){/i}"
    mc "Oh..."
    mc "{i}(I want to know what John's planning on doing, but I'd better leave him to it and not distract him with all my messages.){/i}"
    scene 12_846 with Dissolve(1)
    et "Can you bring us a bottle of Crystal, please?"
    et "Actually. Make that two!"
    jo "..."
    scene black with Dissolve(1)
    pause 2
    scene 12_847 with Dissolve(1)
    et "Be right back."
    gr "Hurry!"
    jo "{i}(I only wanted to observe, but let's see if I can somehow draw his attention.){/i}"
    scene 12_848 with Dissolve(1)
    bt "Good evening, Ethan. Good to see you again."
    et "Hey, Jason. How are you?"
    bt "Can't complain. Give me a minute. I'll be right with you."
    et "Sure. Take your time."
    jo "No, it's too small. It's not worth the investment, nor my time."
    scene 12_849 with Dissolve(1)
    jo "That's why I'm in the talks with the Marauders."
    et "..."
    jo "Yes. Madison Springs. I'll be here for a couple of months."
    scene 12_850 with Dissolve(1)
    jo "You've gotta do me a favour."
    jo "I have multiple meetings and events I'll have to attend the upcoming weeks."
    jo "And as you know. I don't like to turn up on my own."
    jo "Yes. Exactly!"
    scene 12_851 with Dissolve(1)
    jo "I don't want just anyone..."
    jo "She should not only be able to draw attention with her looks, but also keep a conversation going."
    scene 12_852 with Dissolve(1)
    bt "Sorry about that, Ethan."
    et "Hey, no worries."
    bt "What can I do for you?"
    et "We need some snacks. The cheese platter, some crackers, maybe the whole charcuterie board and some fruit."
    scene 12_853 with Dissolve(1)
    jo "No, that's fine."
    jo "Call me once you have the info."
    jo "Yeah. Bye."
    scene 12_854 with Dissolve(1)
    jo "{i}(Didn't take the bait...){/i}"
    jo "{i}(Was it too obvious?){/i}"
    jo "{i}(I should've just stuck with observing for today. What am I doing...?){/i}"
    scene 12_855 with Dissolve(1)
    et "..."
    scene 12_856 with Dissolve(1)
    et "Hi. I'm sorry but I couldn't help overhear your conversation just now."
    et "I might have a solution regarding your... companionship."
    jo "Hmm..."
    et "Let me introduce myself."
    scene 12_857 with Dissolve(1)
    et "I'm Ethan."
    jo "Good to meet you, Ethan."
    jo "I'm John...son. Kyle Johnson."
    jo "{i}(Oh for fuck's sake. Who do I think I am? Some British spy?){/i}"
    et "Good to meet you too, Mr Johnson!"
    scene 12_858 with Dissolve(1)
    jo "Please, have a seat."
    et "Thank you."
    scene 12_859 with Dissolve(1)
    jo "Excuse me."
    bt "Yes?"
    jo "Can I have two more of these, please."
    bt "Of course. Coming right up."
    scene 12_860 with Dissolve(1)
    jo "So... Ethan..."
    jo "Tell me. What can you do for me?"
    scene 12_861 with Dissolve(1)
    mc "*Sigh*"
    mc "{i}(How long has it been now?){/i}"
    mc "{i}(Feels like time is standing still...){/i}"
    mc "{i}(Should I go and have a quick peek? I really want to know what's going on.){/i}"
    scene 12_862 with Dissolve(1)
    mc "{i}(I shouldn't though.){/i}"
    mc "{i}(I know John's got this.){/i}"
    mc "*Deep exhale*"
    scene black with Dissolve(1)
    pause 2
    scene 12_863 with Dissolve(1)
    jo "And how does this work exactly?"
    et "How about we talk over there? I have a table. It's more... private."
    jo "Lead the way."
    scene 12_864 with Dissolve(1)
    et "Sorry, guys. I need our table for a while."
    et "I have some business to discuss."
    et "You can take the champagne with you."
    scene 12_865 with Dissolve(1)
    gr "Don't make it too long, Ethan."
    gr "We're here to have fun today."
    gr "Hey!"
    jo "Good evening."
    scene black with Dissolve(1)
    pause 2
    scene 12_866 with Dissolve(1)
    et "My business thrives on its exclusivity."
    et "All girls are handpicked by me."
    jo "Is there a way to meet the girls beforehand? I'm a picky guy myself."
    et "Of course. You've seen two of them already who are with me today. But let me show you everyone."
    scene 12_867 with Dissolve(1)
    ""
    scene 12_868 with Dissolve(1)
    et "And the last one, Kaley."
    jo "{i}(The last one? Hmm...){/i}"
    jo "{i}(I'm pretty sure Erynn wasn't on this list. Is he keeping her off the list on purpose, or...?){/i}"
    scene 12_869 with Dissolve(1)
    et "What do you think? Anyone caught your fancy?"
    jo "They're all gorgeous, to begin with!"
    et "Aren't they? To be fair, most of them are in the modelling business. Quality over quantity!"
    jo "{i}(He speaks of them as if they're merchandise.){/i}"
    scene 12_870 with Dissolve(1)
    jo "As I said earlier, I'm very picky."
    jo "I have a specific type I'm interested in."
    jo "Blonde. Blue eyes."
    et "..."
    scene 12_871 with Dissolve(1)
    et "Hmm..."
    jo "{i}(Was that too forward? I don't want him to get suspicious now.){/i}"
    jo "{i}(And that's why you should stick with the plan and not change things on the fly...){/i}"
    jo "{i}(But I can't complain. I've already got more info than I wanted.){/i}"
    scene 12_872 with Dissolve(1)
    et "I might have someone else."
    et "Let me check her availability."
    scene 12_873 with Dissolve(1)
    et "Here she is."
    jo "..."
    scene black with Dissolve(1)
    transform moveup:
        xalign 0.5 yalign 1.0
        linear 5.0 yalign 0.0
    show 12_874 at moveup
    pause 3
    jo "{i}(That's her!){/i}"
    scene 12_875 with Dissolve(1)
    et "Do you know her by chance?"
    jo "No, why?"
    et "Your expression changed the moment you saw her."
    jo "She just reminded me of someone I knew a long time ago."
    scene 12_876 with Dissolve(1)
    et "She's gorgeous, isn't she?"
    jo "She most definitely is!"
    et "Blonde... Blue eyes... That what you're looking for?"
    jo "Indeed. But what's the catch?"
    et "What do you mean?"
    scene 12_877 with Dissolve(1)
    jo "She wasn't on your initial list you showed me earlier."
    et "She isn't always available due to the fact that she's my most requested girl."
    et "There's somewhat of a waiting list for her."
    et "Her rate is also dou... triple the amount."
    jo "..."
    scene 12_878 with Dissolve(1)
    jo "What if I take her for two months?"
    et "Two months? Uhm..."
    jo "I'll be in Madison Springs for at least two months."
    jo "I want to hire her for the time I'm here."
    scene 12_879 with Dissolve(1)
    et "Well... That's a first for me... To be honest, I never had that kind of request."
    et "I don't think I can make her available every day. I mean..."
    jo "I won't need her every day. Just on days when I have a meeting or an event."
    jo "I just want to make sure she's available whenever I need her and not on another request."
    jo "{i}(That should also help her by not having to go on other dates for the time being...){/i}"
    scene 12_880 with Dissolve(1)
    et "Let me get that right. So you pay for her, even on the days you won't need her?"
    jo "Exactly."
    jo "Is that a possibility?"
    et "Uhm... Yeah. I think we can come to an arrangement."
    scene 12_881 with Dissolve(1)
    jo "Of course, this is all speculative for now. I'll need to meet her first. See how we flow."
    et "Of course, of course."
    et "Give me a minute. I'll be right back."
    scene 12_882 with Dissolve(1)
    et "I'll need to make some phone calls."
    et "Take care of Mr Johnson for a few minutes for me."
    gr "Sure, no problem."
    scene 12_883 with Dissolve(1)
    jo "Hello, ladies."
    gr "Hi, Mr Johnson."
    gr "We brought some refreshments!"
    scene 12_884 with Dissolve(1)
    jo "Thank you very much!"
    scene 12_885 with Dissolve(1)
    gy "So, how's it going over there?"
    et "This is it. This is what I've been waiting for. He can be my ticket in."
    et "It will open up so many doors if this works out."
    scene 12_886 with Dissolve(1)
    gy "Who is he?"
    et "Some hot-shot business guy."
    et "But more importantly. He has connections! Earlier I overheard him talking about business with the Marauders!"
    et "This can be so huge."
    scene black with Dissolve(1)
    pause 2
    stop music fadeout 1.0
    play music "Music/Battle_Rock2.mp3" volume 0.5
    scene 12_887 with Dissolve(1)
    mc "What was that?"
    mc "I clicked it... I fucking clicked it!"
    scene 12_888 with Dissolve(1)
    mc "*Sigh*"
    mc "What a stupid game!"
    scene 12_889 with Dissolve(1)
    mc "..."
    scene black with Dissolve(1)
    transform moveup:
        xalign 0.5 yalign 1.0
        linear 5.0 yalign 0.0
    show 12_890 at moveup
    pause 3
    mc "{i}(Erynn...){/i}"
    mc "{i}(What's she doing here?){/i}"
    mc "{i}(I told her to stay home! I knew she...){/i}"
    scene 12_891 with Dissolve(1)
    et "Took your sweet little time, huh?"
    mc "{i}(Ethan...){/i}"
    mc "{i}(I should have known.){/i}"
    scene 12_892 with Dissolve(1)
    et "When I say thirty minutes. I mean thirty minutes!"
    er "I had to..."
    et "Stop with your excuses."
    et "And what's with that dress?"
    scene 12_893 with Dissolve(1)
    et "I told you to wear something revealing!"
    et "But what do you do? The opposite. You cover up everything!"
    er "..."
    scene 12_894 with Dissolve(1)
    er "Ahh..."
    et "Now listen the fuck up!"
    scene 12_895 with Dissolve(1)
    mc "{i}(Touch her one more time!){/i}"
    mc "{i}(Ethan, I swear...){/i}"
    scene 12_896 with Dissolve(1)
    er "Stop touching me, Ethan!"
    et "Haha. Again with this attitude?"
    et "I really hate this side of you!"
    er "I hate you!"
    et "..."
    scene 12_897 with vpunch
    er "Aaah..."
    et "I told you to FUCKING LISTEN, ERYNN!"
    menu:
        "Stick with the plan[KoGa3AutoWTChange1]{size=-4}(Ethan Week5 Thursday Plan) {/size} {/color}":
            $ Ethan_Week5_Thursday_Plan = True
            scene 12_898 with Dissolve(1)
            mc "{i}(I really want to go there and beat that fucker up.){/i}"
            mc "{i}(But I also don't want to mess with what John has going on.){/i}"
            mc "{i}(Sorry, Erynn. Just... I'll beat him up next time!){/i}"
            scene 12_899 with Dissolve(1)
            et "I'm talking to an important potential client inside."
            et "And you'd better not mess up this opportunity for me!"
            et "You're going to entertain him! Be flirty! Show interest!"
            et "Anything he wants! You understand?"
            er "..."
            scene 12_900 with Dissolve(1)
            et "DO YOU FUCKING UNDERSTAND, ERYNN?"
            er "*Nods*"
            et "Good! Now get inside!"
            scene 12_901 with Dissolve(1)
            er "When is it finally enough?"
            et "What?"
            er "When is it enough, Ethan?"
            scene 12_902 with Dissolve(1)
            et "We can end this right here, right now, Erynn!"
            et "You know what I want!"
            er "..."
            et "I'll call off everything."
            scene 12_903 with Dissolve(1)
            et "But you know what? I won't be unreasonable!"
            et "We don't have to have sex right now! This place doesn't really scream romance."
            et "We can start by dating. That's what you want, right?"
            et "And then after the second or third date..."
            scene 12_904 with Dissolve(1)
            er "Why would I ever date you after all that you've done to me? To my friends?"
            et "I made a few mistakes, I'll admit that."
            et "But I also forgave the mistake you made with Zane!"
            et "Why can't you forgive mine?"
            er "You're incorrigible, Ethan!"
            scene 12_905 with Dissolve(1)
            et "You'd better be this energetic inside then!"
            et "Let's go!"
            er "..."
            scene 12_906 with Dissolve(1)
            mc "{i}(You can do this, Erynn!){/i}"
            mc "{i}(Stay strong!){/i}"
            scene 12_954 with Dissolve(1)
            play music "Sounds/Bar_Background2.mp3" volume 0.2
            et "Look who had time and decided to show up today!"
            gr "Hey, Erynn."
            er "Hey."
            scene black with Dissolve(1)
            transform moveup:
                xalign 0.5 yalign 1.0
                linear 5.0 yalign 0.0
            show 12_955 at moveup
            pause 3
            et "Erynn. Meet Mr Johnson."
            er "..."
            er "Hello, Mr John...son."
            jo "Good evening."
            scene 12_956 with Dissolve(1)
            jo "Nice to meet you, Erynn."
            er "Nice to meet you too, Mr Johnson."
            jo "I like the dress."
            er "Thank you."
            scene 12_957 with Dissolve(1)
            et "See? I told you the dress suits you."
            er "..."
            et "Isn't she beautiful?"
            jo "Very beautiful!"
            scene 12_958 with Dissolve(1)
            er "..."
            scene 12_959 with Dissolve(1)
            pause 2
            scene 12_960 with Dissolve(1)
            ""
            scene 12_961 with Dissolve(1)
            jo "..."
            scene 12_962 with Dissolve(1)
            jo "Ethan..."
            et "Yes?"
            jo "Do you mind if I talk with Erynn in private? To get to know each other a little?"
            et "Of course, of course. No problem. That's why she's here."
            jo "Thank you."
            scene 12_963 with Dissolve(1)
            jo "Shall we go to the bar?"
            n "*Bzzzt. Bzzzt*"
            er "Okay."
            n "*Bzzzt. Bzzzt*"
            jo "Sorry. Give me a second."
            scene 12_964 with Dissolve(1)
            jo "I've gotta take this."
            et "Go ahead."
            jo "I'll be right back."
            scene 12_965 with Dissolve(1)
            jo "Hey."
            ir "Hey..."
            jo "What's up?"
            ir "When are you coming home? I'm hungry."
            jo "A little bit longer. Maybe an hour or so?"
            scene 12_966 with Dissolve(1)
            ir "Are you still at the bar with [mc]?"
            jo "Uh... Yeah."
            jo "Was everything alright at the garage?"
            ir "Yeah. Mr Harrison came for the documents."
            jo "Ah, okay. Great."
            scene 12_967 with Dissolve(1)
            et "*Whispers* I hope you remember what I said outside!"
            et "*Whispers* Don't screw this up!"
            er "..."
            scene 12_968 with Dissolve(1)
            jo "By the way. What pizza do you want?"
            ir "The usual."
            jo "Which is?"
            ir "Why do you keep forgetting that?"
            scene 12_969 with Dissolve(1)
            jo "Haha, sorry. I don't know."
            jo "Maybe because it's not a common one like pepperoni or margarita."
            ir "You know what? I'll take a calzone this time! Extra cheese but no mushrooms!"
            jo "Calzone, extra cheese, no mushrooms. Got it."
            scene 12_970 with Dissolve(1)
            jo "Anyway. I'll be home in about an hour."
            ir "Fine..."
            jo "See you later."
            ir "Later, Dad. And don't forget the chocolate ice cream!"
            jo "I won't. Bye."
            scene 12_971 with Dissolve(1)
            jo "Sorry about that."
            jo "Shall we head to the bar, Erynn?"
            et "No, no. You can stay here. We'll leave."
            jo "I don't want to take your table."
            et "It's fine."
            scene 12_972 with Dissolve(1)
            et "Let's have some more drinks at the bar, girls."
            jo "Thanks, Ethan."
            et "Don't mention it. Get to know each other."
            scene 12_973 with Dissolve(1)
            jo "How are you feeling?"
            er "Much better now. Thanks for sending him away, John."
            jo "I saw you were uncomfortable around him."
            scene 12_974 with Dissolve(1)
            jo "Is he always this touchy-feely with you?"
            er "*Nods*"
            jo "As long as I'm here, I'll try to keep him away from you as much as I can."
            er "Thank you."
            scene 12_975 with Dissolve(1)
            jo "Do you mind if I ask you some questions about how this normally plays out?"
            jo "If it's too uncomfortable for you..."
            er "No, it's fine. Go ahead."
            jo "So, Ethan calls you when there is a potential new client?"
            scene 12_976 with Dissolve(1)
            er "No. I don't meet them beforehand, usually. Only on the... date itself."
            er "That's why I was surprised when he called me to come here."
            er "But also relieved the moment I saw it was you."
            er "I knew [mc] and you had something planned, but I didn't know what exactly."
            scene 12_977 with Dissolve(1)
            jo "We didn't really have a plan. I'm just winging it, to be honest."
            jo "And it might have been my fault that you had to show up today."
            jo "Sorry about that."
            jo "I came here to check out what kind of person he is, but ended up being a businessman who needs a date for several meetings and outings."
            scene 12_978 with Dissolve(1)
            er "Let's continue with the charade then, I guess."
            er "I'm sure he's keeping an eye on us."
            jo "Exactly my thoughts."
            scene 12_979 with Dissolve(1)
            jo "Thank you very much!"
            er "You're welcome."
            scene black with Dissolve(1)
            pause 2
            scene 12_980 with Dissolve(1)
            er "No, I think you look good in a suit."
            jo "Thank you."
            er "A completely different look from the first time I met you."
            jo "Tank top and full of grease. Couldn't have made a better first impression."
            er "Haha. Grease suits you, too."
            jo "Haha."
            scene 12_981 with Dissolve(1)
            gy "Look at that!"
            gy "She finally listened to you, Ethan."
            gy "Even has her legs on top of his. She's really going for it."
            et "..."
            scene 12_982 with Dissolve(1)
            gy "And she totally mastered that fake smile. Looks so real from here."
            et "That's because she's isn't faking it. That's a genuine laugh."
            et "Is she actually enjoying the conversation with him?"
            scene 12_983 with Dissolve(1)
            gy "Maybe she's into him?"
            et "You think? She can have me! Why would she go for an old guy?"
            gy "He's a handsome dude."
            et "And I'm not?"
            scene 12_984 with Dissolve(1)
            gy "I mean... You're way better looking than him..."
            gy "But maybe it's the tattoos?"
            et "The tattoos?"
            gy "Yeah. She might like dudes with tattoos."
            scene 12_985 with Dissolve(1)
            z "Ethan, I hope you don't mind, but I've brought a friend. You might know each other. This is [mc]."
            et "We do know each other."
            scene 12_986 with Dissolve(1)
            et "{i}(Flowers and butterflies...){/i}"
            et "{i}(Haha. What the fuck?){/i}"
            scene 12_987 with Dissolve(1)
            et "But he didn't have any when he was small and still she liked him!"
            gy "What?"
            scene 12_988 with Dissolve(1)
            et "Never mind. Should I get a tattoo?"
            gy "Uhm... I don't know."
            et "What do you think, Julian?"
            if Valeria_Week4_Friday_Help == True:
                scene 12_989 with Dissolve(1)
                jl "Getting a tattoo?"
                et "Yeah."
                jl "Sure. Why not? I was thinking about getting one myself."
                er "Haha."
            else:
                scene 12_990 with Dissolve(1)
                jl "Sorry. I was thinking about something else. What were you talking about?"
                et "Tattoos. Where has your mind been?"
                jl "Just... I feel like I've seen that Johnson guy before."
                gu "Maybe he was in one of those business magazines you always read."
                jl "Could be, yeah..."
                er "Haha."
            scene 12_991 with Dissolve(1)
            gy "She really seems to be having fun, huh?"
            et "..."
            et "Maybe a little too much. What are they even talking about?"
            et "It's somewhat weird she's so comfortable around him this quickly."
            et "Hmm... Give me a second."
            scene 12_992 with Dissolve(1)
            et "Hey, it's me."
            et "I need a favour."
            et "Give me anything you can find on a Kyle Johnson."
            et "I don't know exactly, but some kind of businessman. I think investments."
            et "As soon as possible."
            scene black with Dissolve(1)
            pause 2
            scene 12_993 with Dissolve(1)
            jo "As much as I'm enjoying talking to you, should we get out of here?"
            er "Uhm, yeah... But I don't think that Ethan..."
            jo "Don't worry about that. I'll take care of it."
            scene 12_994 with Dissolve(1)
            jo "Did you come here by car, or...?"
            er "No, I took an Uber."
            jo "We can drive you home, then."
            jo "[mc] is waiting outside in the car. I'll text him to pick you up."
            er "Oh... Thank you."
            scene 12_995 with Dissolve(1)
            et "..."
            et "Is she leaving already?"
            scene 12_996 with Dissolve(1)
            et "Where do you think you're going?"
            er "..."
            et "You leave whenever I say you can leave!"
            et "Mr Johnson wanted to get to know you and..."
            scene 12_997 with Dissolve(1)
            jo "It's fine. It's actually my fault. I told her she could leave."
            et "Mr Johnson... Did you have a good chat?"
            jo "We did. And we'll have plenty of time to get to know each other."
            et "You've made a decision?"
            scene 12_998 with Dissolve(1)
            et "You can go, then..."
            er "Bye, Mr Johnson."
            jo "Goodbye, Erynn. Hope to see you soon!"
            scene 12_927 with Dissolve(1)
            stop music fadeout 1.0
            play music "Sounds/Street_Traffic.mp3" volume 0.5
            play sound "Sounds/CarHonk.mp3"
            n "*Beep-Beep*"
            er "..."
            scene 12_928 with Dissolve(1)
            mc "Hey."
            er "Oh, it is you. I didn't know which car you'd be in."
            mc "Get in."
            scene 12_929 with Dissolve(1)
            mc "Are you alright?"
            er "*Nods* Yeah."
            scene 12_931 with Dissolve(1)
            er "Thank you, [mc]. Thank you for always being there for me."
            er "I know I can be a handful sometimes..."
            mc "Sometimes?"
            er "Heh..."
            mc "I'll always be there for you!"
            scene 12_932 with Dissolve(1)
            er "I know."
            scene 12_933 with Dissolve(1)
            er "So, this is John's car?"
            mc "Well technically it belongs to a client of his. He's using it to test drive it."
            mc "Before I ask what happened inside, I'll go park somewhere else."
            mc "Can't have Ethan seeing us here."
            scene black with Dissolve(1)
            pause 2
            scene 12_943 with Dissolve(1)
            mc "And did John talk to Ethan, too?"
            er "He's right there. He can tell you."
            er "I'll go move to the back."
            mc "Alright."
            scene 12_944 with Dissolve(1)
            mc "Can you even fit in between there?"
            er "..."
            mc "I mean your..."
            er "Yes! I can fit!"
            mc "Haha."
            if Erynn_LikeMC == True:
                scene 12_945 with vpunch
                n "*Slap*"
                er "Aaah! Hey!"
                mc "Sorry. Just helping. I thought you were stuck there for a second."
                er "By slapping my ass?"
                mc "Haha. I'll push now!"
                er "I've got it!"
            else:
                pass
            scene 12_946 with Dissolve(1)
            jo "Hey."
            mc "Hey."
            er "Thank you again, John. For everything."
            jo "Don't mention it."
            scene 12_947 with Dissolve(1)
            mc "Can you fill me in on what happened?"
            jo "Sure. Let's get out of here first, though."
            jump Week5_Thursday_John_End
        "Help Erynn[KoGa3AutoWTChange1]{size=-4}(Ethan Week5 Thursday Punch, Ethan Week5 Thursday Phone) {/size} {/color}":
            $ Ethan_Week5_Thursday_Punch = True
            $ Ethan_Week5_Thursday_Phone = True
            stop music fadeout 1.0
            play music "Music/Battle_Rock3.mp3" volume 0.5
            scene 12_898 with Dissolve(1)
            mc "{i}(Okay... That's enough.){/i}"
            scene 12_899 with Dissolve(1)
            et "I'm talking to an important potential client inside."
            et "And you'd better not mess this opportunity up for me!"
            et "You're going to entertain him! Be flirty! Show interest!"
            et "Anything he wants! You understand?"
            er "..."
            scene 12_907 with vpunch
            et "Aaah..."
            er "[mc]!"
            scene 12_908 with Dissolve(1)
            mc "I told you to leave her alone!"
            et "Haha. Of course you brought your little friend, too..."
            scene 12_909 with vpunch
            mc "Shut up!"
            et "..."
            scene 12_910 with Dissolve(1)
            et "You'd better let go of me or you're going to regret this!"
            mc "The only one who's going to regret something is you!"
            scene 12_911 with Dissolve(1)
            mc "You can leave, Erynn. You don't have to be here anymore."
            et "No! She can't!"
            mc "Just wait at the front entrance. I'll come pick you up in a few minutes."
            er "Alright..."
            scene 12_912 with Dissolve(1)
            et "ERYNN!"
            mc "I told you to shut up!"
            scene 12_913 with Dissolve(1)
            et "Sending her away because you don't want her to see you're beating someone up..."
            mc "She's seen me beat you up before!"
            mc "I don't want her near you."
            et "..."
            scene 12_914 with Dissolve(1)
            et "You're just pretending to be the good guy! Helping the damsel in distress... Some kind of hero complex."
            et "But in fact, you and I aren't that different, you know?"
            et "We have the same goal. We both just want to fuck her!"
            menu:
                "Smack his head against the door[KoGa3AutoWTChange1]{size=-4}(Ethan WallPunch+1) {/size} {/color}":
                    $ Ethan_WallPunch += 1
                    scene 12_915 with Dissolve(1)
                    mc "We're nothing alike!"
                    mc "For starters, I don't need two other idiots to beat you up!"
                    if Valeria_Week4_Friday_Help == True:
                        et "True. You let a girl do the work!"
                        et "Don't worry, I haven't forgotten about her!"
                        mc "..."
                    else:
                        et "Funny that I got sucker-punched by someone else!"
                    scene 12_909 with vpunch
                    et "Aaah..."
                    menu:
                        "Keep smashing his head[KoGa3AutoWTChange1]{size=-4}(Ethan WallPunch+1) {/size} {/color}":
                            jump Week5_Thursday_Ethan_Hit1
                        "Punch him to the ground":
                            jump Week5_Thursday_Ethan_End
                "(Lie) I've fucked Erynn":
                    mc "{i}(How about I play you at your own game.){/i}"
                    scene 12_918 with Dissolve(1)
                    mc "Here's something you don't know yet."
                    mc "I already did!"
                    mc "More than once!"
                    et "..."
                    scene 12_919 with Dissolve(1)
                    et "You fucking asshole. You always screw everything up!"
                    et "Just like all those years ago!"
                    mc "..."
                    scene 12_920 with Dissolve(1)
                    mc "{i}(I think I didn't even need to dodge.){/i}"
                    mc "If you didn't let your goons do all the work..."
                    mc "You would actually know how to throw a punch!"
                    jump Week5_Thursday_Ethan_End

label Week5_Thursday_Ethan_Hit1:
    $ Ethan_WallPunch += 1
    if Ethan_WallPunch >= 50:
        $ achievement.grant("ACHIEVEMENT_LEARNED_FIRST_TIME")
        $ achievement.sync()
        scene 12_917a with vpunch
        pause 2
        scene 12_917b with Dissolve(1)
        ""
        jump Week5_Thursday_Ethan_End
    else:
        scene 12_916 with vpunch
        ""
        menu:
            "Keep smashing his head[KoGa3AutoWTChange1]{size=-4}(Ethan WallPunch+1) {/size} {/color}":
                jump Week5_Thursday_Ethan_Hit2
            "Punch him to the ground":
                jump Week5_Thursday_Ethan_End

label Week5_Thursday_Ethan_Hit2:
    $ Ethan_WallPunch += 1
    scene 12_917 with vpunch
    ""
    menu:
        "Keep smashing his head[KoGa3AutoWTChange1]{size=-4}(Ethan WallPunch+1) {/size} {/color}":
            jump Week5_Thursday_Ethan_Hit3
        "Punch him to the ground":
            jump Week5_Thursday_Ethan_End

label Week5_Thursday_Ethan_Hit3:
    $ Ethan_WallPunch += 1
    scene 12_909 with vpunch
    ""
    menu:
        "Keep smashing his head":
            jump Week5_Thursday_Ethan_Hit1
        "Punch him to the ground":
            jump Week5_Thursday_Ethan_End

label Week5_Thursday_Ethan_End:
    scene 12_921 with vpunch
    et "Aaah..."
    scene 12_922 with vpunch
    ""
    scene 12_923 with Dissolve(1)
    mc "{i}(You've had this coming for a long time!){/i}"
    mc "{i}(That felt good...){/i}"
    scene 12_924 with Dissolve(1)
    mc "{i}(I'm taking this with me too.){/i}"
    mc "{i}(I don't think it's the only copy he has but who knows...){/i}"
    scene 12_925 with Dissolve(1)
    mc "{i}(Let's quickly get out of here.){/i}"
    mc "{i}(I hope no one saw this.){/i}"
    scene 12_926 with Dissolve(1)
    et "..."
    scene 12_927 with Dissolve(1)
    stop music fadeout 1.0
    play music "Sounds/Street_Traffic.mp3" volume 0.5
    play sound "Sounds/CarHonk.mp3"
    n "*Beep-Beep*"
    er "..."
    scene 12_928 with Dissolve(1)
    mc "Hey."
    er "Oh, it's you."
    mc "Get in."
    scene 12_929 with Dissolve(1)
    mc "Are you alright?"
    er "*Nods* Yeah."
    mc "He didn't hurt you or anything?"
    er "I'm fine."
    scene 12_930 with Dissolve(1)
    er "How are you? What did you do back there?"
    mc "Do you really want to know?"
    er "*Shakes head* No..."
    mc "He got what he deserved. I told him again to leave you alone."
    scene 12_931 with Dissolve(1)
    er "Thank you, [mc]. Thank you for always being there for me."
    er "I know I can be a handful sometimes..."
    mc "Sometimes?"
    er "Heh..."
    mc "I'll always be there for you!"
    scene 12_932 with Dissolve(1)
    er "I know."
    scene 12_933 with Dissolve(1)
    er "Whose car is this?"
    mc "It's John's."
    er "Oh..."
    mc "Well technically it belongs to a client of his. He's using it to test drive it."
    mc "But that reminds me. I should text him and tell him I'm parked somewhere else now."
    scene 12_934 with Dissolve(1)
    er "John is inside?"
    mc "Yeah. He's been there for quite a while now."
    er "Maybe he was talking to Ethan and that's why Ethan told me to come?"
    mc "Shit! You might be right. And now I've screwed everything up."
    scene 12_935 with Dissolve(1)
    stop music fadeout 1.0
    play music "Sounds/Bar_Background2.mp3" volume 0.2
    gy "What the fuck happened to you?"
    et "I got jumped by that little punk."
    gy "Who? The one we beat up the last time?"
    et "Indeed."
    scene 12_936 with Dissolve(1)
    gy "Where is he? Is he still there?"
    et "He left. But go check anyway. Maybe he's still close by."
    jl "Will do."
    et "I'll get the girls. Meet me at my place in an hour."
    scene 12_937 with Dissolve(1)
    gr "Oh my god, Ethan... What happened?"
    et "I got jumped outside."
    jo "..."
    gr "Jumped? Are you alright?"
    et "I will be..."
    scene 12_938 with Dissolve(1)
    jo "Did they take anything?"
    n "*Bzzzt. Bzzzt*"
    et "Motherfucker took my phone..."
    jo "Want me to call the police?"
    et "I'll take care of this myself. I know who he is."
    scene 12_939 with Dissolve(1)
    et "I wanted to discuss some more things but due to this situation..."
    jo "No, understandable."
    et "Here. Take my card. But give me a few days to get everything back in order."
    jo "Of course."
    scene 12_940 with Dissolve(1)
    et "It was good to meet you, Mr Johnson."
    jo "You too, Ethan. You'll hear from me soon."
    et "Great!"
    jo "Take care of yourself. And maybe get a check-up at the hospital. You might have a concussion."
    et "I might do that. Thanks!"
    scene 12_941 with Dissolve(1)
    mc "Stuff happened and I'm parked on Ocean Drive now."
    jo "..."
    jo "{i}(Was it [mc] who beat up Ethan?){/i}"
    scene 12_942 with Dissolve(1)
    jo "I'd like to pay, please."
    bt "It's already been taken care of, sir."
    jo "Oh... Great. Thanks. Have a nice evening."
    bt "Thank you. You have a good evening too, sir."
    scene 12_943 with Dissolve(1)
    stop music fadeout 1.0
    play music "Sounds/Street_Traffic.mp3" volume 0.5
    mc "There he is."
    er "I'll go move to the back."
    scene 12_944 with Dissolve(1)
    mc "Can you even fit in between there?"
    er "..."
    mc "I mean your..."
    er "Yes! I can fit!"
    mc "Haha."
    if Erynn_LikeMC == True:
        scene 12_945 with vpunch
        n "*Slap*"
        er "Aaah! Hey!"
        mc "Sorry. Just helping. I thought you were stuck there for a second."
        er "By slapping my ass?"
        mc "Haha. I'll push now!"
        er "I've got it!"
    else:
        pass
    scene 12_946 with Dissolve(1)
    jo "Hey."
    mc "Hey."
    er "Hi, John."
    jo "Oh, Erynn. Hey."
    scene 12_947 with Dissolve(1)
    jo "Now that explains what happened to Ethan."
    er "What?"
    jo "He came in with a bloody nose and said he was jumped."
    mc "Well deserved!"
    scene 12_948 with Dissolve(1)
    er "[mc]!"
    mc "What? I didn't hit him... that hard..."
    mc "He basically stumbled into my fist."
    er "..."
    scene 12_949 with Dissolve(1)
    mc "But sorry about that, John."
    mc "I wasn't really thinking at that moment and I might have screwed things up for you."
    mc "He was being rough with Erynn and I couldn't just..."
    scene 12_950 with Dissolve(1)
    jo "No, it's fine. I would've done the same thing."
    jo "I got the info I wanted."
    jo "Besides. It's probably a little my fault that he called Erynn."
    mc "Why's that?"
    scene 12_951 with Dissolve(1)
    jo "We were..."
    mc "Or can you tell us everything that happened inside?"
    jo "Sure. But let's get away from here first."
    jump Week5_Thursday_John_End

label Week5_Thursday_John_End:
    scene black with Dissolve(1)
    pause 2
    scene 12_952 with Dissolve(1)
    mc "It sounds like he has a whole business already."
    jo "Indeed."
    mc "Which will make things more difficult, I guess."
    scene 12_953 with Dissolve(1)
    er "Sorry..."
    jo "You don't have to be sorry, Erynn. Nothing of this is your doing."
    jo "We'll figure something out."
    er "*Nods*"
    scene black with Dissolve(1)
    pause 2
    stop music fadeout 1.0
    play music ("Music/LoFi Indie 3.mp3", "Music/LoFi Indie 1.mp3", "Music/LoFi Indie 2.mp3") volume 0.2
    scene 12_999 with Dissolve(1)
    ""
    scene 12_1000 with Dissolve(1)
    er "Again. Thank you so very much for doing this, John."
    er "I know it's..."
    jo "I agreed to it, Erynn."
    if Ethan_Week5_Thursday_Plan == True:
        scene 12_1001 with Dissolve(1)
        er "Still. I'm basically a stranger and..."
        jo "We're not strangers anymore after today, I'd say."
        er "No, you're right."
        er "Thank you!"
    else:
        pass
    scene 12_1002 with Dissolve(1)
    mc "I agree with Erynn."
    mc "You didn't have to do this, but you did. Thank you so much, John."
    jo "I told you before that I'll be there if you need me."
    mc "I know."
    scene 12_1003 with Dissolve(1)
    mc "So, what's the next step?"
    jo "I don't know yet, to be honest."
    jo "I actually got more info today than I'd expected."
    scene 12_1004 with Dissolve(1)
    jo "I'll probably look more into his business for now."
    mc "Yeah. Maybe we'll find a different way to deal with the situation. All of this can't be legit."
    jo "Indeed. I also think I bought us a little more time."
    jo "I don't think you'll be going on another date for the time being, Erynn."
    er "*Nods*"
    scene 12_1005 with Dissolve(1)
    jo "Anyway. I'll call you if anything comes up or changes."
    mc "Great."
    er "Thanks, John."
    scene 12_1006 with Dissolve(1)
    mc "What are you doing now, John?"
    mc "I was planning to go to a bar and watch the Marauders. So if you want to join me..."
    jo "I'd love to, but I promised Iris pizza already. She's been waiting for some time now."
    jo "Love the idea though. Let's go next week sometime?"
    mc "Sure."
    scene 12_1007 with Dissolve(1)
    er "Drive home safely."
    er "And tell Iris hi from me."
    jo "Will do. Bye, Erynn."
    if Ethan_Week5_Thursday_Plan == True:
        er "Bye, Mr Johnson."
        jo "Heh..."
        mc "{i}(Mr Johnson?){/i}"
    else:
        er "Bye, John."
    if Ethan_Week5_Thursday_Plan == False:
        scene 12_1009 with Dissolve(1)
        mc "Thanks again, John."
        jo "Call me if anything changes."
        jo "*Whispers* One more thing. You'll need to be careful now. Ethan won't sit still and will probably be coming for you since you have his phone."
        mc "*Whispers* I know."
    else:
        scene 12_1008 with Dissolve(1)
        mc "Thanks again, John."
        jo "Call me if anything changes."
    scene 12_1010 with Dissolve(1)
    jo "Bye, guys."
    mc "Later."
    er "Bye-bye."
    scene 12_1011 with Dissolve(1)
    mc "Come. I'll take you home."
    er "..."
    mc "What?"
    scene 12_1012 with Dissolve(1)
    er "Just... I live next door and it sounded like this big gesture..."
    mc "..."
    mc "I only wanted to..."
    er "I know."
    mc "You can go on your own if..."
    if Erynn_LikeMC == False:
        scene 12_1013 with Dissolve(1)
        er "No... I didn't mean it in that way."
        er "Sorry... It's really sweet actually!"
        er "Please take me home."
    else:
        scene 12_1014 with Dissolve(1)
        er "Noooo... [mc]..."
        er "Please, take me home! Please...!"
        er "It's really sweet!"
        scene 12_1015 with Dissolve(1)
        er "Please..."
        er "[mc]..."
        mc "*Sigh*"
        scene 12_1016 with Dissolve(1)
        mc "*Mumbles* Every freaking time..."
        er "Hehe..."
        mc "You're just like someone else I know. Always getting what she wants."
        er "Not always!"
    scene 12_1017 with Dissolve(1)
    mc "Ahhh... I needed this."
    er "I'll be right back."
    er "I'm gonna change into something more comfortable."
    mc "Okay."
    if Erynn_LikeMC == False:
        pass
    else:
        scene 12_1018 with Dissolve(1)
        mc "Do you need help? With the dress, I mean."
        er "No, I've got it."
        mc "You sure?"
        er "Mm-hmm..."
    scene black with Dissolve(1)
    pause 1
    scene black with Dissolve(1)
    transform moveup:
        xalign 0.5 yalign 1.0
        linear 5.0 yalign 0.0
    show 12_1019 at moveup
    pause 3
    er "I'm back."
    mc "{i}(I've asked this before, but how does this girl look amazing in everything she wears...?){/i}"
    if Erynn_LikeMC == True:
        scene 12_1020 with Dissolve(1)
        er "Haah... So much more comfortable."
        mc "You don't like wearing dresses?"
        er "No, I do. But I also like taking them off again."
        scene 12_1021 with Dissolve(1)
        mc "Hey, if it gets you more comfortable, you can take everything off."
        mc "Don't mind me."
        er "..."
        mc "Kidding..."
        mc "{i}(Not really.){/i}"
        scene 12_1022 with Dissolve(1)
        mc "You looked really nice today."
        er "Thank you."
        mc "With and without the dress."
        er "Heh..."
        if Alexis_Dating == False:
            menu:
                "Kiss her[KoGa3AutoWTChange1]{size=-4}(Erynn Points+2) {/size} {/color}":
                    $ Erynn_Points += 2
                    # Erynn (62)
                    scene 12_1023 with Dissolve(1)
                    ""
                    scene 12_1024 with Dissolve(1)
                    er "..."
                "Don't kiss":
                    pass
        else:
            pass
        scene 12_1025 with Dissolve(1)
        mc "How are you feeling after all that happened today?"
        mc "Are you really alright?"
        er "I am. Honestly!"
        er "All thanks to you and John."
        scene 12_1026 with Dissolve(1)
        mc "Can you lean forward for a second?"
        er "Okay? What are you doing?"
        mc "Checking if you have any bruises."
        if Ethan_Week5_Thursday_Plan == False:
            scene 12_1027 with Dissolve(1)
            mc "Ethan pushed you pretty hard against that wall."
            mc "I'm just making sure."
            er "Thank you."
        else:
            scene 12_1028 with Dissolve(1)
            er "Why would I have any bruises?"
            mc "I saw what happened outside the club, Erynn."
            mc "Ethan being rough with you and pushing you against that wall."
            er "..."
            scene 12_1029 with Dissolve(1)
            mc "I wanted to come help you so badly."
            mc "But I didn't know what was going on inside with John, so I didn't want to mess anything up."
            mc "But now thinking back, I should've helped you and not let that asshole touch you."
            mc "I'm so sorry!"
            scene 12_1030 with Dissolve(1)
            er "Maybe it was better this way?"
            er "Who knows what Ethan would've done if he saw you there."
            er "So you don't need to apologise."
            er "Let's just forget about today."
            mc "*Nods*"
        scene 12_1031 with Dissolve(1)
        er "And? Any bruises?"
        mc "Nope. Everything looks perfect!"
        er "Oh, thank god. I was scared I would look like you now!"
        scene 12_1032 with Dissolve(1)
        mc "Hey!"
        er "Haha."
        mc "That was such a low blow! I don't have that many bruises!"
        scene 12_1033 with Dissolve(1)
        mc "And just so you know, since you might have some issues with your eyesight..."
        mc "You should be happy to look like me! I'm actually really good-looking!"
        er "Are you?"
        mc "Mm-hmm..."
        er "Who says that?"
        menu:
            "Erynn":
                scene 12_1034 with Dissolve(1)
                mc "You do!"
                er "You must have dreamt that!"
                mc "You know I dream about other stuff."
                er "..."
            "Emily":
                scene 12_1035 with Dissolve(1)
                mc "Mom said that, for starters."
                er "Hmm..."
                mc "No comeback?"
                er "I like Emily. I trust her judgement."
                mc "Well that was easy."
            "Melissa":
                scene 12_1036 with Dissolve(1)
                mc "Melissa does!"
                er "..."
                er "She only says that to be nice to you!"
                mc "Haha."
            "Lots of girls":
                scene 12_1037 with Dissolve(1)
                mc "Lots of girls do."
                er "Hmm... Lots of girls... Of course."
        scene 12_1038 with Dissolve(1)
        er "But I'll admit. You're good-looking!"
        mc "Thanks. So are you!"
        er "Thanks."
        scene 12_1039 with Dissolve(1)
        er "..."
        mc "..."
        scene 12_1040 with Dissolve(1)
        er "Uhm... About John..."
        mc "Hmm? What about John?"
        er "He seems like a dad to you."
        mc "Yeah. In a way he is."
        er "I like him too!"
        if Ethan_Week5_Thursday_Plan == True:
            scene 12_1041 with Dissolve(1)
            mc "You really have a little crush on John, huh?"
            er "No, I don't."
            mc "Look me in the eyes and answer again!"
            er "..."
            er "Maybe a little, okay?"
            scene 12_1042 with Dissolve(1)
            er "Are you jealous?"
            mc "Of John?"
            mc "Fuck yeah!"
            scene 12_1043 with Dissolve(1)
            mc "He's tall, good-looking, tattoos..."
            mc "Cool... Got his own business..."
            er "Great sense of humour."
            mc "That too."
            er "*Whispers* Just like someone else I know..."
            mc "Hmm?"
            scene 12_1044 with Dissolve(1)
            er "Nothing."
            mc "Seems like you had a great time with him in the club."
            er "I did."
            mc "Did you get to know each other, or what did you talk about?"
            er "You!"
            scene 12_1045 with Dissolve(1)
            mc "Me?"
            er "Yeah. I asked him to tell me about you back when you lived in Alvarado."
            mc "Oh shit."
            er "Oh shit is right."
            mc "Haha."
        else:
            pass
        scene 12_1046 with Dissolve(1)
        er "Oh..."
        mc "What now?"
        er "I almost forgot."
        scene 12_1047 with Dissolve(1)
        er "Didn't you wanna go to the bar to watch the game?"
        mc "Oh, that. I thought you forgot something important, seeing your reaction just now."
        er "Isn't it a big game?"
        scene 12_1048 with Dissolve(1)
        mc "It is, but I can stay here with you. I don't mind."
        er "You don't have to. You've done so much for me already."
        er "I feel bad keeping you here. Just go watch the game."
        scene 12_1049 with Dissolve(1)
        mc "Alright. Do you want to come with me?"
        er "Thanks, but I've had enough of bars for today."
        er "And Mom will be home soon. I'm gonna spend some time with her."
        mc "Okay."
        scene 12_1050 with Dissolve(1)
        er "Thanks again, [mc]. For always being there for me!"
        er "You have no idea what this means to me!"
        mc "You're welcome. Besides. You're here for me too."
        er "*Nods*"
        scene 12_1051 with Dissolve(1)
        er "Bye, [mc]."
        mc "See you later, Erynn."
        scene 12_1052 with Dissolve(1)
        ""
        if Alexis_Dating == False:
            scene 12_1053 with Dissolve(1)
            er "Oh... I almost forgot something else."
            er "Are we still on for tomorrow?"
            mc "The beach?"
            er "Yeah!"
            mc "Of course."
            scene 12_1054 with Dissolve(1)
            er "Great."
            er "I'll come pick you up tomorrow, then."
            mc "You mean to wake me up?"
            er "Haha. Probably!"
            scene 12_1055 with Dissolve(1)
            er "..."
        else:
            pass
    else:
        scene 12_1056 with Dissolve(1)
        er "Haah... So much more comfortable."
        mc "You don't like wearing dresses?"
        er "No, I do. But I also like taking them off again."
        scene 12_1057 with Dissolve(1)
        mc "You looked really nice today."
        er "Thank you."
        scene 12_1058 with Dissolve(1)
        mc "How are you feeling after all that happened today?"
        mc "Are you really alright?"
        er "I am. Honestly!"
        er "All thanks to you and John."
        scene 12_1026 with Dissolve(1)
        mc "Can you lean forward for a second?"
        er "Okay? What are you doing?"
        mc "Checking if you have any bruises."
        if Ethan_Week5_Thursday_Plan == False:
            scene 12_1027 with Dissolve(1)
            mc "Ethan pushed you pretty hard against that wall."
            mc "I'm just making sure."
            er "Thank you."
        else:
            scene 12_1028 with Dissolve(1)
            er "Why would I have any bruises?"
            mc "I saw what happened outside the club, Erynn."
            mc "Ethan being rough with you and pushing you against that wall."
            er "..."
            scene 12_1029 with Dissolve(1)
            mc "I wanted to come help you so badly."
            mc "But I didn't know what was going on inside with John, so I didn't want to mess anything up."
            mc "But now thinking back, I should've helped you and not let that asshole touch you."
            mc "I'm so sorry!"
            scene 12_1030 with Dissolve(1)
            er "Maybe it was better this way?"
            er "Who knows what Ethan would've done if he saw you there."
            er "So, you don't need to apologise."
            er "Let's just forget about today."
            mc "*Nods*"
        scene 12_1031 with Dissolve(1)
        er "And? Any bruises?"
        mc "Nope. Everything looks perfect!"
        er "Thanks for making sure."
        scene 12_1059 with Dissolve(1)
        er "Don't get this the wrong way but uhm... John..."
        mc "Hmm? What about John?"
        er "He seems like a dad to you."
        mc "Yeah. In a way he is."
        er "I like him too!"
        if Ethan_Week5_Thursday_Plan == True:
            scene 12_1060 with Dissolve(1)
            mc "You really have a little crush on John, huh?"
            er "No, I don't."
            mc "Look me in the eyes and answer again!"
            er "..."
            er "Maybe a little, okay?"
            scene 12_1061 with Dissolve(1)
            er "..."
            mc "{i}(This is the first time I've seen her like this.){/i}"
            scene 12_1062 with Dissolve(1)
            mc "Can't blame you. He's tall, good-looking, tattoos..."
            mc "Cool... Got his own business..."
            er "Great sense of humour."
            mc "That too."
            scene 12_1063 with Dissolve(1)
            mc "Seems like you had a great time with him in the club."
            er "I did."
            mc "Did you get to know each other, or what did you talk about?"
            er "You!"
            scene 12_1064 with Dissolve(1)
            mc "Me?"
            er "Yeah. I asked him to tell me about you back when you lived in Alvarado."
            mc "Oh shit."
            er "Oh shit is right."
            mc "Haha."
        else:
            pass
        scene 12_1065 with Dissolve(1)
        er "Oh..."
        mc "What now?"
        er "I almost forgot."
        scene 12_1066 with Dissolve(1)
        er "Didn't you wanna go to the bar to watch the game?"
        mc "Oh, that. I thought you forgot something important, seeing your reaction just now."
        er "Isn't it a big game?"
        scene 12_1067 with Dissolve(1)
        mc "It is, but I can stay here with you. I don't mind."
        er "You don't have to. You've done so much for me already."
        er "I feel bad keeping you here. Just go watch the game."
        scene 12_1049 with Dissolve(1)
        mc "Alright. Do you want to come with me?"
        er "Thanks, but I've had enough of bars for today."
        er "And Mom will be home soon. I'm gonna spend some time with her."
        mc "Okay."
        scene 12_1050 with Dissolve(1)
        er "Thanks again, [mc]. For always being there for me!"
        er "You have no idea what this means to me!"
        mc "You're welcome. Besides. You're here for me, too."
        er "*Nods*"
        scene 12_1051 with Dissolve(1)
        er "Bye, [mc]."
        mc "See you later, Erynn."
    jump Week5_Thursday_DylansBar

label Week5_Thursday_DylansBar:
    scene black with Dissolve(1)
    pause 2
    stop music fadeout 1.0
    play music "Sounds/Bar_Background.mp3" volume 0.2
    scene 12_1068 with Dissolve(1)
    mc "{i}(Oh wow... It's packed.){/i}"
    mc "{i}(Lots of people had the same idea.){/i}"
    scene 12_1069 with Dissolve(1)
    if Layla_End == True:
        mc "{i}(Alexis not working today?){/i}"
        mc "{i}(Probably for the best.){/i}"
    else:
        if Alexis_Dating == False:
            mc "{i}(Alexis not working today?){/i}"
        else:
            mc "{i}(Alexis not working today?){/i}"
            mc "{i}(Didn't she say she'd be at the bar this evening?){/i}"
            mc "{i}(Hmm...){/i}"
    scene 12_1070 with Dissolve(1)
    mc "{i}(Haven't seen her before.){/i}"
    mc "{i}(Is she new?){/i}"
    mc "{i}(Probably not. It's not like I come here every day and know all the people who work here.){/i}"
    menu:
        "Check her out[KoGa3AutoWTChange1]{size=-4}(Gianna Week5 Thursday CheckOut) {/size} {/color}":
            $ Gianna_Week5_Thursday_CheckOut = True
            scene black with Dissolve(1)
            transform moveup:
                xalign 0.5 yalign 1.0
                linear 5.0 yalign 0.0
            show 12_1071 at moveup
            pause 3
            mc "{i}(But damn...){/i}"
            mc "{i}(Dylan really knows how to choose them.){/i}"
        "Don't":
            pass
    scene 12_1072 with Dissolve(1)
    bd "Hey, there!"
    mc "Hey, Dylan."
    bd "Came to check out the game?"
    mc "Hell yeah! You can't miss this one."
    bd "Truer words haven't been spoken today."
    scene 12_1073 with Dissolve(1)
    mc "How are ya?"
    bd "Good, good. You?"
    mc "Can't complain. I see you're rockin' the Marauders jersey."
    bd "You gotta represent."
    scene 12_1074 with Dissolve(1)
    mc "Number fifty-seven. Gatling."
    bd "MVP right here."
    x "Heh..."
    scene 12_1075 with Dissolve(1)
    x "MVP my ass."
    bd "Hey-hey-hey!"
    if Gianna_Week5_Thursday_CheckOut == True:
        scene 12_1076 with Dissolve(1)
        mc "{i}(She's right.){/i}"
        mc "{i}(That's definitely an MVP!){/i}"
        x "You know Adler's gonna win MVP!"
        bd "That's heresy, Gianna!"
    else:
        x "You know Adler's gonna win MVP!"
        bd "That's heresy, Gianna!"
    scene 12_1077 with Dissolve(1)
    bd "Don't listen to that heretic!"
    gi "Haha."
    bd "You won't be laughing later!"
    gi "We'll see about that!"
    scene 12_1078 with Dissolve(1)
    bd "*Shakes head* Palm City girls, right? What do they know...?"
    mc "Haha."
    bd "Anyway. What can I get you?"
    mc "A beer, please."
    scene 12_1079 with Dissolve(1)
    play sound "Sounds/Phone_Vibrate.mp3"
    n "*Bzzzt. Bzzzt*"
    mc "{i}(Hmm?){/i}"
    n "*Bzzzt. Bzzzt*"
    scene 12_1080 with Dissolve(1)
    mc "Heh..."
    n "*Bzzzt. Bzzzt*"
    scene 12_1081 with Dissolve(1)
    mc "Yo-yo-yo!"
    na "Hey, [mc]! What's up?"
    mc "Hey, Nate!"
    scene 12_1082 with Dissolve(1)
    mc "How are you? It's been a while."
    na "Sure has been. I'm good. How are you?"
    mc "Yeah, Good too."
    scene 12_1083 with Dissolve(1)
    mc "What are you doing up so late? Isn't it after midnight there?"
    na "It is. But what can I do if the game is broadcast so late."
    mc "You're watching the game too, huh?"
    na "Of course. Adler's gonna kick your ass!"
    mc "Haha. In your dreams!"
    scene 12_1084 with Dissolve(1)
    na "Besides. If I call you in the morning, you'll still be sleeping."
    na "The afternoon, you're in school..."
    mc "Not this week! spring break!"
    scene 12_1085 with Dissolve(1)
    na "Wait... You have spring break this week?"
    mc "Mm-hmm."
    na "We had it last week."
    na "You should've come visited us or something."
    scene 12_1086 with Dissolve(1)
    mc "Yeah, didn't even think about that. So much stuff going on here lately."
    na "Even more reason to come over. Take a break from everything."
    mc "That would be awesome. I could use a break."
    na "You still have a few days left. Check if there's a flight and let's do this!"
    if Nikki_Girlfriend == True:
        mc "You know what? You're right!"
        mc "I wanted to visit Nikki anyway, so I'll make a surprise visit."
        mc "Stay there for a couple of days and drive over to Alvarado on Saturday or something and spend the day with you?"
        na "Sounds perfect! Let's gooo!"
        x "Haha. Let's gooo..."
        scene 12_1088 with Dissolve(1)
        mc "I'll text you the details once I have all the info."
        na "Great! Can't wait."
    else:
        if Cara_Girlfriend == True:
            scene 12_1087 with Dissolve(1)
            mc "You know what? You're right!"
            mc "I wanted to visit Cara anyway, so I'll make a surprise visit."
            mc "Stay there for a couple of days and drive over to Alvarado on Saturday or something and spend the day with you?"
            na "Sounds perfect! Let's gooo!"
            x "Haha. Let's gooo..."
            scene 12_1088 with Dissolve(1)
            mc "I'll text you the details once I have all the info."
            na "Great! Can't wait."
        else:
            scene 12_1087 with Dissolve(1)
            mc "You know what? You're right!"
            mc "I'll book a flight and I'll text you the details later."
            mc "Probably early Saturday. Stay the night and fly back on Sunday."
            na "YES! Let's gooo!"
            x "Haha. Let's gooo..."
    scene 12_1089 with Dissolve(1)
    na "Well... I didn't expect to turn this call into a visit."
    mc "Haha. Things can change quickly."
    na "They sure can."
    na "I guess there's not really a need for us to talk over the phone, now."
    mc "No. We'll have plenty of time to catch up later."
    scene 12_1090 with Dissolve(1)
    na "Cool. We'll see each other on Saturday then."
    na "If anything changes or you can't get a flight, let me know."
    mc "Will do. Bye, Nate!"
    na "Later, [mc]."
    scene 12_1091 with Dissolve(1)
    na "One more thing!"
    mc "Hmm?"
    na "Eclipse gonna win!"
    mc "Haha. Wishful thinking! We'll destroy you!"
    na "Haha. See ya!"
    scene 12_1092 with Dissolve(1)
    x "So, he's coming?"
    na "If he's able to get a flight, yeah."
    if Nikki_Girlfriend == True:
        na "He'll visit his girlfriend in Riverside and drive over to us on Saturday and spend the day."
    else:
        if Cara_Girlfriend == True:
            na "He'll visit his girlfriend in Riverside and drive over to us on Saturday and spend the day."
        else:
            na "He'll be here Saturday and stay the night. Fly black on Sunday."
    scene 12_1093 with Dissolve(1)
    mc "{i}(Can't wait to visit him in Alvarado.){/i}"
    mc "{i}(This will be fun.){/i}"
    if Nikki_Girlfriend == True:
        mc "{i}(And the surprise on Nikki's face when I show up...){/i}"
    else:
        if Cara_Girlfriend == True:
            mc "{i}(And the surprise on Cara's face when I show up...){/i}"
        else:
            pass
    scene 12_1094 with Dissolve(1)
    gi "And here's your beer!"
    mc "Thank you very much."
    mc "Gianna, was it?"
    gi "Mm-hmm."
    scene 12_1095 with Dissolve(1)
    mc "Eclipse fan, huh? In Madison Springs..."
    gi "What can I say?"
    mc "Well... You're brave, that's for sure."
    mc "Or..."
    scene 12_1096 with Dissolve(1)
    gi "Or?"
    mc "..."
    gi "Stupid?"
    mc "I didn't say that! In fact, I didn't say anything."
    scene 12_1097 with Dissolve(1)
    gi "..."
    mc "Haha."
    mc "{i}(She seems fun.){/i}"
    scene 12_1098 with Dissolve(1)
    gi "Who's that guy?"
    bd "You mean [mc]?"
    gi "Yeah. Haven't seen him before."
    if Alexis_Dating == False:
        scene 12_1099 with Dissolve(1)
        bd "He moved back here fairly recently."
        bd "Cool guy."
        gi "So he likes your steaks?"
        bd "That's not the only requirement to be cool..."
        gi "Uh-huh."
    else:
        scene 12_1100 with Dissolve(1)
        bd "That's Alexis's boyfriend."
        gi "Oh, that's him?"
        bd "Mm-hmm. Cool guy."
        gi "Heh... Cool guy... So he likes your steaks?"
        bd "That's not the only requirement to be cool..."
        gi "Uh-huh."
    scene black with Dissolve(1)
    pause 2
    scene 12_1101 with Dissolve(1)
    mc "Five more minutes till tip-off... Getting excited."
    bd "Indeed. So, what are we thinking?"
    mc "Marauders gonna win, of course."
    scene 12_1102 with Dissolve(1)
    bd "How about a little wager?"
    mc "Wait! You don't think they're gonna win?"
    bd "Of course they're gonna win."
    scene 12_1103 with Dissolve(1)
    gi "You're both wrong!"
    mc "Oh yeah? How about you join us in our bet if you're that confident?"
    gi "Sure, I'm in."
    bd "You'd better watch out. She's a brave one."
    scene 12_1104 with Dissolve(1)
    mc "Yeah. I told her that earlier."
    gi "And stupid!"
    mc "No-no-no! I didn't say that!"
    gi "Haha. Kidding..."
    scene 12_1105 with Dissolve(1)
    mc "So, what are we betting?"
    gi "Hmm... Let's see..."
    gi "If the Marauders win. Which is not going to happen, just for the sake of the bet..."
    mc "..."
    gi "I'll pay for everything you order today!"
    scene 12_1106 with Dissolve(1)
    bd "I can turn on the grill if you'd like?"
    mc "Now that you're mentioning it."
    mc "I'm actually getting a bit hungry and can eat one of your steaks, Dylan. Or two..."
    gi "*Shakes head* Heh."
    scene 12_1107 with Dissolve(1)
    mc "What if we lose?"
    gi "You'll work one of my shifts for me."
    mc "Hmm... If that's okay with Dylan."
    bd "I'm fine with it."
    scene 12_1108 with Dissolve(1)
    mc "Alright. You're on!"
    gi "Perfect!"
    gi "I guess I can start thinking about what I'll do on my day off."
    mc "Haha."
    scene black with Dissolve(1)
    pause 2
    scene 12_1109 with Dissolve(1)
    co "And Madison Springs wins the tip-off."
    bd "Let's go Marauders!"
    scene 12_1110 with Dissolve(1)
    co "Gatling for three!"
    gi "..."
    bd "There we go. There we go. Keep repeating this. Let's try to get an early lead."
    bd "I can sense a triple-double coming already!"
    scene 12_1111 with Dissolve(1)
    mc "Yeah?"
    bd "Easy thirty-bomb. Thirty-six points, eleven rebounds and ten assists."
    bd "What do you think?"
    mc "Hmm... Thirty-two, eight and eight."
    x "Twenty-six, six rebounds, four assists..."
    scene 12_1112 with Dissolve(1)
    bd "Sup, Navarro. Only twenty-six points? Not much faith in your client?"
    sn "Hey, Dylan."
    sn "No, I have. But they'll be doubling him the whole game."
    sn "He'll be playing more off-ball, I suppose."
    bd "Hmm..."
    scene 12_1113 with Dissolve(1)
    bd "By the way. What are you doing here?"
    bd "Shouldn't you be at the arena?"
    sn "I have a late meeting after the game which isn't too far from here."
    sn "That way I can watch the whole game and don't have to worry about traffic after."
    scene 12_1114 with Dissolve(1)
    bd "Marauders victory today?"
    sn "Of course. Will be a tough game though. Lots of fouls."
    bd "That's a given. What can I get you? Coffee?"
    sn "No, let's have a beer for now."
    scene 12_1115 with Dissolve(1)
    mc "Good evening, Mr Navarro."
    sn "Hey! Good evening, [mc]. How are you?"
    mc "{i}(Didn't think he'd remember my name...){/i}"
    mc "Good but that can change depending on the outcome of today's game."
    sn "Haha."
    scene 12_1116 with Dissolve(1)
    mc "I haven't thanked you yet for paying for me last time."
    mc "So, thank you."
    sn "You're welcome."
    mc "Today's on me."
    sn "There's no need..."
    scene 12_1117 with Dissolve(1)
    mc "No-no, it's fine."
    mc "It's covered. Right, Gianna?"
    gi "Haha. I can't wait to see your face later."
    scene 12_1118 with Dissolve(1)
    sn "Cheers!"
    mc "Cheers."
    scene 12_1119 with Dissolve(1)
    co "Another two points for Gatling. He's leading the game with seven points."
    sn "Let's go, Marauders!"
    co "Eclipse's coach has seen enough and calls for a timeout."
    co "Eleven to four, Marauders. We'll be right back after a word from our sponsor."
    scene 12_1120 with Dissolve(1)
    sn "Are you training for the relay now?"
    mc "Relay?"
    sn "Yeah. The four-by-100-meter relay tournament."
    mc "Uhm... No?"
    scene 12_1121 with Dissolve(1)
    mc "I haven't heard anything about a relay tournament."
    sn "Coach Mike hasn't said anything yet?"
    mc "No."
    sn "Oh shit..."
    scene 12_1122 with Dissolve(1)
    mc "What's it about?"
    sn "You haven't heard anything from me, alright?"
    sn "Next weekend, there will be a regional competition between eight schools."
    sn "One school had to drop out due to injuries and they asked Madison HS to fill in."
    mc "Interesting. Sounds fun."
    scene 12_1123 with Dissolve(1)
    sn "Other schools have been training for weeks already."
    sn "It's a little different than a standard hundred-meter race, of course. Especially knowing when to start running and how to pass the baton."
    sn "But your school has some good athletes, so you might end up with a good result even though you won't have much time to train."
    sn "Also... It's another opportunity to get scouted for a scholarship."
    scene 12_1124 with Dissolve(1)
    mc "It is. Thanks for the heads up."
    sn "No problem. But as I said..."
    mc "Don't worry. I'll act surprised when Coach announces it next week."
    sn "Good man!"
    scene black with Dissolve(1)
    pause 2
    scene 12_1125 with Dissolve(1)
    co "That's the end of the first quarter."
    co "Marauders lead thirty-two to twenty-six."
    bd "Yeah. That's it. Good start. Three more quarters like this! Let's go! We got this!"
    co "Gatling leading the scoreboard with twelve points and three rebounds. Not much yet from Adler who only shot two of six."
    scene 12_1126 with Dissolve(1)
    bd "Gatling has had an amazing game, right?"
    sn "It was alright. He could've done without those three turnovers."
    bd "What did you say earlier? Twenty-six points? Hah... He's already halfway there."
    bd "Wanna review your prediction?"
    sn "No, I'm good."
    scene 12_1127 with Dissolve(1)
    bd "By the way. Is it possible to get my jersey signed by Gatling?"
    sn "Sure. I can arrange that."
    bd "Awesome. Do you want it now, or...?"
    sn "I don't want your sweaty jersey, Dylan. I'll get you a new one."
    scene 12_1128 with Dissolve(1)
    gi "What are you smiling about?"
    mc "No reason. Just happy..."
    gi "You need to calm down. It was only the first quarter."
    mc "I know, I know."
    scene 12_1129 with Dissolve(1)
    mc "But could you get me some snacks anyway?"
    gi "*Shakes head* Heh..."
    gi "What do you want?"
    mc "Chips, please."
    scene 12_1130 with Dissolve(1)
    bd "You joined the bet!"
    gi "*Sigh* It's not over yet!"
    bd "Haha."
    scene 12_1131 with Dissolve(1)
    sn "For how long have you been a Marauders fan?"
    mc "Always have been."
    mc "Grew up watching Freakin' Zo."
    sn "Haha. Freakin' Zo..."
    scene 12_1132 with Dissolve(1)
    sn "Enzo was an amazing player. Madison Springs legend."
    mc "Won four championships for us!"
    sn "Indeed. Retired way too early."
    sn "He had two more good years in him, if not three!"
    scene 12_1133 with Dissolve(1)
    bd "But if he didn't retire, we wouldn't have had those two bad years."
    bd "Meaning no top spot in the rookie draft, no Gatling."
    bd "Maybe it was planned?"
    scene 12_1134 with Dissolve(1)
    sn "You watch way too many conspiracy theories, Dylan!"
    sn "They did everything to have him sign a new contract. Trust me, I was there."
    sn "But he'd just had enough. Wanted to spend more time with the family."
    scene 12_1135 with Dissolve(1)
    gi "Here's your bag of chips."
    mc "Thanks."
    gi "Want something else?"
    mc "I'm good for now, thank you. Unless you want something, Mr Navarro?"
    sn "I'm good. Thanks."
    scene 12_1136 with Dissolve(1)
    mc "So, Mr Navarro..."
    mc "Did you play any sport in high school or college?"
    sn "How about we drop the mister? It always makes me feel old."
    sn "Just Navarro is fine."
    scene 12_1137 with vpunch
    sn "Or you can call me Santiago!"
    mc "..."
    mc "{i}(What...?){/i}"
    mc "San..ti..."
    sn "Haha. Yeah. Or Santi. That's fine too."
    scene 12_1138 with Dissolve(1)
    mc "{i}(Santiago as in... My real dad Santiago?){/i}"
    sn "Haven't heard anyone call me Santi since college, I think."
    mc "{i}(This is just a coincidence, right? He's just another person who has the same name... Right?){/i}"
    sn "No, I'm lying. There's still one person who calls me that to this day."
    sn "Haven't seen her for quite some time, though."
    scene 12_1139 with Dissolve(1)
    sn "Emily... Little Emi..."
    mc "..."
    mc "{i}(This... This... This is not happening right now...){/i}"
    mc "{i}(My heart is beating like crazy.){/i}"
    scene 12_1140 with Dissolve(1)
    mc "{i}(Santiago... Emily... I have to make sure...){/i}"
    sn "You okay? You just lost all colour in your face."
    mc "Uh... Yeah... I was just thinking that my boss at the restaurant I work at is also called Emily."
    scene 12_1141 with Dissolve(1)
    sn "Emily Vicari from Rue Madison?"
    mc "Yes."
    sn "That's her. We know the same Emily."
    mc "{i}(Now there's no mistaking it.){/i}"
    mc "{i}(This guy must be my dad... HOLY SHIT!){/i}"
    scene 12_1142 with Dissolve(1)
    sn "Anyway. I went off track a bit."
    mc "{i}(Does he know I'm his son?){/i}"
    sn "Sport in high school and college..."
    mc "{i}(I don't think he does. I don't know what Mom told him about me before... She must have at least mentioned my name, no?){/i}"
    sn "I played basketball in high school."
    scene 12_1143 with Dissolve(1)
    mc "{i}(I can actually see it now. We look a bit similar.){/i}"
    sn "And then added football into the mix while at college. American Football that is."
    mc "{i}(Shit... What is he talking about? I zoned out the moment I found out he's my dad.){/i}"
    mc "Basketball and football?"
    sn "Yes."
    scene 12_1144 with Dissolve(1)
    mc "{i}(I don't even know what to say... I feel so awkward now.){/i}"
    mc "Uhm... You didn't want to go professional?"
    sn "I did, I did."
    sn "And I thought I was really good. Until I played together with Zo in college."
    sn "He made me realise I wasn't."
    scene 12_1145 with Dissolve(1)
    mc "You played together with Freakin' Zo?"
    sn "Good friend of mine. Also, my first client once I became an agent."
    mc "Oh wow."
    mc "{i}(I really know nothing about him. Obviously...){/i}"
    mc "{i}(But do I even want to get to know him? I should talk to Mom first anyway. Just to confirm. Stranger things have happened.){/i}"
    scene 12_1146 with Dissolve(1)
    co "Halftime in Madison Springs."
    mc "{i}(Wait... I missed the whole second quarter...){/i}"
    co "Marauders are leading fifty-eight to fifty-one."
    mc "{i}(At least they're still up.){/i}"
    mc "{i}(I'll head outside for a minute to clear my head a bit... This was just too much to take in...){/i}"
    scene black with Dissolve(1)
    pause 2
    n "Half an hour later."
    scene 12_1147 with Dissolve(1)
    co "Gatling for threeee..."
    mc "Yes! Come on!"
    co "Marauders back up eight!"
    scene black with Dissolve(1)
    pause 2
    scene 12_1148 with Dissolve(1)
    co "And he missed the second one."
    mc "How the fuck do you miss both free throws."
    sn "*Shakes head*"
    scene black with Dissolve(1)
    pause 2
    scene 12_1149 with Dissolve(1)
    bd "Did you see that? DID YOU SEE THAT!"
    bd "That's Gatling, baby!"
    bd "Hell yeah!"
    gi "*Sigh*"
    scene black with Dissolve(1)
    pause 2
    scene 12_1150 with Dissolve(1)
    sn "Come on, ref!"
    mc "Why is that a foul? He barely touched the guy!"
    sn "And now he gets a technical. Are you kidding me?"
    mc "Today's league is so fucking soft!"
    mc "Challenge the call!"
    scene black with Dissolve(1)
    pause 2
    scene 12_1151 with Dissolve(1)
    co "Adler for three..."
    co "Swish! Eclipse ahead 121 to 120. Their first lead of the game."
    gi "YES!"
    co "Timeout Marauders. Seven seconds left on the clock."
    scene 12_1152 with Dissolve(1)
    co "Adler with fourteen points in the fourth quarter! He got hot at the right moment!"
    mc "*Shakes head* We were leading the fucking whole game. How can you lose a twelve-point lead in the last eight minutes?"
    mc "Just play some fucking D! How can you leave Adler open like that?"
    mc "And where the fuck is Gatling? Has he scored a single basket this quarter?"
    scene 12_1153 with Dissolve(1)
    gi "What did you get again today?"
    gi "Two beers, three iced teas, a coffee, two packs of chips... Anything else?"
    mc "..."
    mc "And what did you say earlier? It's not over yet!"
    scene 12_1154 with Dissolve(1)
    mc "Seven seconds can be a long time."
    gi "That's something only a guy would say!"
    mc "Ha-ha-ha... Very funny!"
    scene 12_1155 with Dissolve(1)
    co "Here we go! Let's see what the coach drew up."
    sn "Let's go Marauders!"
    mc "Finish it!"
    scene 12_1156 with Dissolve(1)
    co "Inbound to Gatling. Adler is on him."
    bd "You've got this!"
    co "Four seconds... Three..."
    co "Gatling crossover, goes to his right. Fadeaway over Adler. Gatling for the win!"
    gi "Nooo...!"
    scene 12_1157 with Dissolve(1)
    co "Short!"
    gi "YEEES!!!"
    co "Eclipse win. 121 to 120!"
    mc "..."
    scene 12_1158 with Dissolve(1)
    mc "Fuck!"
    mc "Why didn't he pass to Richards? He was completely open."
    mc "Yeah he had an off-shooting night with two out of nine. He was still in a much better position to make the shot!"
    mc "Stupid, stupid decision."
    scene 12_1159 with Dissolve(1)
    bd "That puts a damper on my night."
    bd "Still don't know what happened. How did we lose this?"
    bd "At least you're happy..."
    gi "Eclipse won and I'll have a paid day off."
    mc "..."
    scene 12_1160 with Dissolve(1)
    mc "What do you mean paid day off?"
    gi "Did you think you'd be the one who gets paid when you do my shift for me?"
    gi "That's not how it works. You're the one who failed to specify the conditions."
    gi "But hey. You can keep the tips you make that day. Maybe you'll be able to pay the bill from today that way."
    mc "Yeah-yeah. Just rub it in..."
    scene 12_1161 with Dissolve(1)
    bd "Sneaky one, isn't she?"
    mc "You could've warned me, Dylan!"
    bd "Haha. Sorry..."
    mc "I should've betted with you on Gatling's stats. He wasn't even close to a triple-double."
    bd "You win some, you lose some."
    scene 12_1162 with Dissolve(1)
    bd "How about a free steak meal the day you have to come work here, as compensation?"
    mc "That'd be awesome. Thanks."
    bd "Alright then."
    scene 12_1163 with Dissolve(1)
    bd "Another coffee? Santi...?"
    sn "Hey-hey-hey! It's still Navarro for you!"
    bd "Haha."
    mc "{i}(I completely forgot that I'm sitting next to my... biological father...){/i}"
    mc "{i}(If not for the game and the bet, I probably would have... Man...){/i}"
    mc "{i}(What else is going to happen today? This is crazy.){/i}"
    scene 12_1164 with Dissolve(1)
    a "What's with the atmosphere in here? It's so quiet. Did the Marauders lose or something?"
    if Alexis_Dating == False:
        mc "{i}(That's Alexis's voice...){/i}"
    else:
        mc "{i}(That's Lexi's voice...){/i}"
    gi "Lexi!"
    bd "Good Evening, Lex."
    a "Hey-hey."
    scene 12_1165 with Dissolve(1)
    gi "How are you?"
    a "I'm good. How are you, Gigi? It's been some time since we worked together."
    gi "Yeah. Way too long."
    gi "Blame Dylan! He makes the schedule."
    bd "I can handle one of you. Both of you? Haha, no!"
    scene 12_1166 with Dissolve(1)
    gi "Too much beauty?"
    bd "Beauty? If I wanted beauty in my bar, I'd be the only one working here!"
    a "Haha."
    mc "{i}(Heh. Typical Dylan.){/i}"
    scene 12_1167 with Dissolve(1)
    bt "Thanks for covering for me, Alexis."
    a "I told you before, it's no problem."
    scene 12_1168 with Dissolve(1)
    sn "Hey, Lex!"
    a "Hey."
    if Layla_End == True:
        scene 12_1169 with Dissolve(1)
        a "..."
        mc "{i}(Yeah... She's still mad at me.){/i}"
        mc "{i}(Will this ever change?){/i}"
    else:
        if Alexis_Dating == True:
            if Alexis_Week5_Wednesday_Beach == True:
                if Alexis_Week5_Thursday_BreakUpTalk == False:
                    $ Gianna_Week5_Thursday_Domino = True
                    scene 12_1170 with Dissolve(1)
                    a "Oh, hey... You came."
                    mc "Hey, Lexi. How are you?"
                    scene 12_1191 with Dissolve(1)
                    a "I'm good. How are you, [mc]?"
                    mc "Good. Even though the Marauders lost..."
                    a "Yeah. I figured. Sorry..."
                    mc "You don't have to be sorry about that. They played like shit at the end."
                    scene 12_1192 with Dissolve(1)
                    mc "By the way. I don't like your colleague."
                    a "Who? Gianna? Why don't you like her?"
                    gi "Haha. Because he lost a bet against me."
                    scene 12_1193 with Dissolve(1)
                    a "Yeah, you shouldn't bet against her."
                    a "She's always lucky somehow."
                    gi "It's my superpower."
                    scene 12_1194 with Dissolve(1)
                    mc "Yeah... Now I know who you remind me of..."
                    mc "Domino!"
                    gi "Who's Domino?"
                    mc "The character. Domino."
                    gi "Never heard of her."
                    mc "She's in the Deadpool movie. Look her up."
                    scene 12_1196 with Dissolve(1)
                    a "Hey, I'll be right back."
                    a "Gonna put my jacket away. Don't go anywhere."
                    mc "Don't worry. I'll be here."
                    a "And don't make any more bets with her!"
                    mc "Haha, I won't."
                else:
                    scene 12_1170 with Dissolve(1)
                    a "Oh, hey... Didn't think I'd see you today."
                    mc "Hey. How are you?"
                    scene 12_1191 with Dissolve(1)
                    a "I'm good. How are you, [mc]?"
                    mc "Good. Even though the Marauders lost..."
                    a "Yeah. I figured. Sorry..."
                    mc "You don't have to be sorry about that. They played like shit at the end."
                    scene 12_1195 with Dissolve(1)
                    a "I'll be right back. Can we talk later, or do you have to leave soon?"
                    mc "No, we can talk."
                    a "Okay."
            else:
                scene 12_1171 with Dissolve(1)
                a "Oh, hey..."
                a "Long time no see."
                mc "Yeah. Hey, Alexis. How are you?"
                a "..."
                scene 12_1190 with Dissolve(1)
                a "I'm good. How are you, [mc]..."
                mc "{i}(Why does this feels so awkward now?){/i}"
                mc "{i}(Something changed between us.){/i}"
                mc "So-so. Marauders lost..."
                a "I figured."
                scene 12_1195 with Dissolve(1)
                a "I'll be right back. Can we talk later, or do you have to leave soon?"
                mc "No, we can talk."
                a "Okay."
                mc "{i}(Definitely awkward.){/i}"
        else:
            if Layla_Week5_Wednesday_BreakUp == False:
                scene 12_1171 with Dissolve(1)
                a "Oh, hey..."
                a "You're here as well."
                mc "Hey, Alexis. How are you?"
                scene 12_1190 with Dissolve(1)
                a "I'm good. How are you, [mc]?"
                mc "Good. Even though the Marauders lost..."
                a "Yeah. I figured."
                if Alexis_Sex == True:
                    scene 12_1195 with Dissolve(1)
                    a "Hey, I'll be right back."
                    a "Gonna put my jacket away."
                    mc "Sure."
                else:
                    $ Gianna_Week5_Thursday_Domino = True
                    scene 12_1192 with Dissolve(1)
                    mc "By the way. I don't like your colleague."
                    a "Who? Gianna? Why don't you like her?"
                    gi "Haha. Because he lost a bet against me."
                    scene 12_1193 with Dissolve(1)
                    a "Yeah, you shouldn't bet against her."
                    a "She's always lucky somehow."
                    gi "It's my superpower."
                    scene 12_1194 with Dissolve(1)
                    mc "Yeah... Now I know who you remind me of..."
                    mc "Domino!"
                    gi "Who's Domino?"
                    mc "The character. Domino."
                    gi "Never heard of her."
                    mc "She's in the Deadpool movie. Look her up."
                    scene 12_1196 with Dissolve(1)
                    a "Hey, I'll be right back."
                    a "Gonna put my jacket away."
                    mc "Sure."
            else:
                $ Alexis_SecretPath = False
                scene 12_1172 with Dissolve(1)
                a "..."
                mc "Hey..."
                a "I think we should talk, right?"
                mc "{i}(Layla probably told her...){/i}"
                mc "Sure."
                scene 12_1173 with Dissolve(1)
                a "Let's go sit at a table for a second."
                mc "O-okay..."
                scene 12_1174 with Dissolve(1)
                mc "{i}(This was to be expected.){/i}"
                mc "{i}(Still hoped she wouldn't be here today.){/i}"
                scene 12_1175 with Dissolve(1)
                mc "{i}(She looks like she'll rip me a new one.){/i}"
                mc "{i}(She can be really scary...){/i}"
                scene 12_1176 with Dissolve(1)
                mc "*Sigh...*"
                mc "So, what has Layla told you?"
                a "It doesn't matter what she said."
                a "I want to hear it from you!"
                scene 12_1177 with Dissolve(1)
                mc "Then I'll tell you the same thing I told Elena."
                a "Wait... The other girl is Elena?"
                mc "{i}(Damn... Layla hasn't mentioned that?){/i}"
                mc "{i}(Shooting myself in the foot already.){/i}"
                mc "Yeah..."
                scene 12_1178 with Dissolve(1)
                a "So you were only with Layla to get to Elena?"
                mc "What?"
                mc "No! Of course not!"
                a "Did you even like her?"
                scene 12_1179 with Dissolve(1)
                mc "Yes, I did. I still do!"
                a "..."
                mc "*Sigh* And I know it all sounds... Confusing."
                if Alexis_Sex == True:
                    scene 12_1180 with Dissolve(1)
                    a "As confusing as when you first slept with me and then went for my sister?"
                    mc "..."
                    mc "{i}(She has all rights to be mad at me...){/i}"
                    mc "I'm really sorry about that, Alexis."
                else:
                    pass
                scene 12_1181 with Dissolve(1)
                mc "At first, I didn't even like Elena. Yeah, I found her attractive..."
                mc "{i}(Shut up, [mc]... She doesn't need to know all the details...){/i}"
                mc "But since Layla and Elena are basically joined at the hip, we spent a lot of time together, too."
                mc "And the more I got to know her, the more my feelings grew for her."
                mc "I thought it was just some crush, but..."
                scene 12_1182 with Dissolve(1)
                mc "If I knew what Layla had planned. I wouldn't have gone on that date with her."
                mc "It took me by surprise as well."
                mc "Yeah, the how and when were very questionable. I know that."
                mc "I was panicking too, at that moment."
                scene 12_1183 with Dissolve(1)
                mc "I didn't want her first time to be with a guy who's confused about two girls."
                mc "She deserves so much more than that."
                a "At least you know!"
                mc "I'm sorry, okay? To her, to Elena, to you..."
                mc "The last thing I wanted was to make her cry and break up their friendship."
                scene 12_1184 with Dissolve(1)
                a "..."
                mc "..."
                scene 12_1185 with Dissolve(1)
                a "I'm still angry at you..."
                a "But you did the right thing."
                a "I know many guys who would have taken that... opportunity."
                a "So..."
                scene 12_1186 with Dissolve(1)
                mc "Uhm... Can I ask how Layla's doing?"
                a "I think you have a good idea of how she might feel."
                mc "Yeah..."
                mc "I want to talk to her and explain everything. Especially make everything right again between her and Elena. Hopefully before school starts again."
                mc "I tried calling her, but..."
                scene 12_1187 with Dissolve(1)
                a "Give her a few days."
                a "And don't call her. She'll just ignore it."
                a "Go talk to her personally."
                mc "Can you maybe...?"
                a "No. I'm not helping you. You'll have to figure it out yourself!"
                scene 12_1188 with Dissolve(1)
                mc "Alright. Thanks."
                mc "And thank you for listening and letting me explain."
                a "*Nods*"
                scene 12_1189 with Dissolve(1)
                mc "{i}(Even though both Elena and Alexis said that... *Sigh*){/i}"
                mc "{i}(Why do I still feel like the biggest asshole?){/i}"
    scene black with Dissolve(1)
    pause 2
    scene 12_1197 with Dissolve(1)
    sn "I want to stay longer but..."
    mc "Your meeting?"
    sn "*Sigh* Exactly. Can't be late."
    scene 12_1198 with Dissolve(1)
    sn "Thanks for the company."
    sn "And good luck next week in the relay."
    mc "Thank you. Will you be there, too?"
    sn "I will."
    mc "{i}(Why am I getting nervous again?){/i}"
    scene 12_1199 with Dissolve(1)
    sn "Dylan. It was a pleasure, as always."
    bd "Thanks for stopping by!"
    sn "And I'll get you that signed jersey."
    bd "Thank you very much! Tell him to make that shot next time!"
    sn "Haha. I will!"
    scene 12_1200 with Dissolve(1)
    sn "I wish I could stay a bit longer but I have a meeting to go to."
    if Alexis_Dating == True:
        mc "{i}(Do I tell her who he is or do I wait until I'm a hundred per cent sure?){/i}"
        mc "{i}(I guess I'll wait a few days.){/i}"
        mc "{i}(Good thing I'm planning to visit Nathan. I can use that time to think about all this.){/i}"
        scene 12_1202 with Dissolve(1)
        mc "{i}(Why are they looking over here now?){/i}"
        mc "{i}(Are they talking about me?){/i}"
    else:
        mc "{i}(Should I tell Alexis who he is, or...?){/i}"
        mc "{i}(No... It's none of her business.){/i}"
        mc "{i}(Good thing I'm planning to visit Nathan. I can use that time to think about all this.){/i}"
        scene 12_1201 with Dissolve(1)
        mc "{i}(Why are they looking over here now?){/i}"
        mc "{i}(Are they talking about me?){/i}"
    scene 12_1203 with Dissolve(1)
    sn "Oh, Lex. What do you want for breakfast tomorrow?"
    mc "{i}(Breakfast?){/i}"
    a "You going to the bakery? The usual."
    sn "Alright."
    mc "{i}(Why would... Heh? Now I'm confused.){/i}"
    scene 12_1204 with Dissolve(1)
    mc "{i}(Seriously... What's going on?){/i}"
    if Alexis_Dating == True:
        mc "{i}(Maybe I should talk to her sooner rather than later?){/i}"
    else:
        mc "{i}(Maybe I should talk to her after all?){/i}"
    mc "{i}(I have a weird feeling about all of this.){/i}"
    if Layla_End == True:
        scene 12_1205 with Dissolve(1)
        mc "Hey, uhm... Alexis..."
        a "What?"
        mc "I know we aren't on the best of terms. Or any terms for that matter."
        mc "But can I ask you a question? It's kinda important."
        a "..."
        a "Sure."
        scene 12_1208 with Dissolve(1)
        mc "How to ask this... It's about... Santiago Navarro."
        mc "Who... Who is he to you?"
        a "Santiago?"
        scene 12_1208 with vpunch
        a "He's my dad..."
        x "Make that two please, Alexis."
        scene 12_1211 with Dissolve(1)
        a "Sure, Jamie."
        mc "What... He's your..."
        scene 12_1212 with Dissolve(1)
        mc "{i}(What the fuck is going on...?){/i}"
        mc "{i}(Does that mean she and Layla...){/i}"
    else:
        if Alexis_Dating == False:
            scene 12_1206 with Dissolve(1)
            mc "Hey, Alexis..."
            a "Yes?"
            mc "Can I ask you a question? It's kinda important."
            a "Sure."
            scene 12_1209 with Dissolve(1)
            mc "How to ask this... It's about... Santiago Navarro."
            mc "Who... Who is he to you?"
            a "Santiago?"
            scene 12_1209 with vpunch
            a "He's my dad..."
            x "Make that two please, Alexis."
            scene 12_1211 with Dissolve(1)
            a "Sure, Jamie."
            mc "What... He's your..."
            scene 12_1212 with Dissolve(1)
            mc "{i}(What the fuck is going on...?){/i}"
            mc "{i}(She's my...?){/i}"
            if Layla_Dating == True:
                mc "{i}(And Layla?){/i}"
                mc "{i}(Oh no... What have we done?){/i}"
            else:
                pass
        else:
            if Alexis_Week5_Wednesday_Beach == True:
                if Alexis_Week5_Thursday_BreakUpTalk == False:
                    scene 12_1207 with Dissolve(1)
                    mc "Hey, Lexi..."
                    a "Yeah?"
                    mc "Can I ask you a question? It's kinda important."
                    a "Of course, you can!"
                    scene 12_1210 with Dissolve(1)
                    mc "How to ask this... It's about... Santiago."
                    a "You're calling him Santiago now?"
                    mc "Yeah... Who... Who is he to you?"
                    scene 12_1210 with vpunch
                    a "He's my dad..."
                    x "Make that two please, Alexis."
                else:
                    scene 12_1206 with Dissolve(1)
                    mc "Hey, Alexis..."
                    a "Yes?"
                    mc "Can I ask you a question? It's kinda important."
                    a "Sure."
                    scene 12_1208 with Dissolve(1)
                    mc "How to ask this... It's about... Santiago Navarro."
                    mc "Who... Who is he to you?"
                    a "Santiago?"
                    scene 12_1208 with vpunch
                    a "He's my dad..."
                    x "Make that two please, Alexis."
            else:
                scene 12_1206 with Dissolve(1)
                mc "Hey, Alexis..."
                a "Yes?"
                mc "Can I ask you a question? It's kinda important."
                a "Sure."
                scene 12_1208 with Dissolve(1)
                mc "How to ask this... It's about... Santiago Navarro."
                mc "Who... Who is he to you?"
                a "Santiago?"
                scene 12_1208 with vpunch
                a "He's my dad..."
                x "Make that two please, Alexis."
            scene 12_1211 with Dissolve(1)
            a "Sure, Jamie."
            mc "What... He's your..."
            scene 12_1212 with Dissolve(1)
            mc "{i}(What the fuck is going on...?){/i}"
            mc "{i}(She's my...?){/i}"
            mc "{i}(Oh no... What have we done?){/i}"
    jump Episode_13_Start


# Max Points:

# Alexis (46)
# Melissa (18)
# Layla (100)
# Elena (48)
# Emily (22)
# Erynn (62)
# Tori (18)
# Cara (16)
# Nikki (20)
# Lakeyn (6)
# Brooke (10)
# Adriana (6)
# Naomi (2)
# Valeria (26)
# Zach (10)
# Darryl (4)
# ShaCarri (4)
# Iris (2)
# Sienna (4)

# MC_GoodStudent (14)

# Nikki_Weekend (10)
# Nikki_Visit (40)
# Cara_Weekend (6)
# Cara_Visit (44)
# Alexis_SP (20)
# Alexis_Jealous (16)
# Alexis_Beach (16)

# MC_Sex (35)
# Alexis_Sex (9)
# Tori_Sex (3)
# Lakeyn_Sex (1)
# Nikki_Sex (6)
# Cara_Sex (7)
# Julia_Sex (1)
# Rachel_Sex (1)
# Gabi_Sex (3)
# Iris_Sex (3)
# Layla_Sex (1)

#WTAdded