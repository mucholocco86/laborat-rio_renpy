label ch1ep2:
    scene ch1ep1e
    with dissolve
    pause
    scene ch1ep1s
    with dissolve
    pause
    show screen day_monday
    play sound closedoor
    play music 'audio/RunForTheMan.mp3'
    scene ch1ep2_1
    with dissolve
    pause
    show ch1ep2_2 
    yt "So after that raid on Hera's safe house, they are making their move just as I thought they would. It didn't even take that long."
    yt "Although, I wonder..."
    yt "Isn't this guy supposed to be an old hag? What changed?"
    yt "I have a good guess in mind, but I will need concrete answers from Aine."
    yt "First, I need to get rid of this maggot quickly."
    scene ch1ep2_3
    with dissolve
    yt "Klara seems to have detected an unruly presence and is on standby." #hiding somewhere 
    yt "I'm glad we had that discussion at Beach Island."
    scene ch1ep2_4
    with flash
    mc "If my intuition is right, I'm sure what we did at Hera's safe house alerted whoever is pulling the strings behind her back."
    mc "If so, they'll move sooner than we think. We must be prepared if that happens."
    scene ch1ep2_5
    with dissolve
    mc "I still don't know what they want or their true goal, but I won't let that affect our lives."
    mc "We have people with the right skillsets to do this. I need you to trust me and let me be your brains."
    scene ch1ep2_6
    with flash
    yt "This confirms my hypothesis. Someone's indeed pulling some strings."
    yt "But who?"
    yt "... This tacky son of a bitch?"
    yt "Nah, that person wouldn't be so stupid to show up here blatantly."
    yt "If I were pulling the strings, I would try and exhaust my own resources first; and that's what they are doing."
    yt "I can't carelessly question this guy either since that would only raise his suspicions of me."
    show ch1ep2_7
    with dissolve
    yt "However, considering that he got this from his \"sources\" and not on his own, I can exploit that and turn this into a game of denial."
    yt "That will open an opportunity to make my move."
    transform zoom_image:
        xalign 0.5
        yalign 0.5
        zoom 0.8
    transform zoomouttop_image:
        zoom 0.05
    # Set the x and y coordinates for the first image
    transform first_image:
        xalign 0.2
        yalign 0.05
        zoom 0.2
    play sound papermovement
    show ch1ep2_8 at first_image with Dissolve(0.2)
    # Pause for the desired duration
    pause 0.1
    # Set the x and y coordinates for the second image
    transform second_image:
        xalign 0.5
        yalign 0.05
        zoom 0.2
    play sound papermovement
    show ch1ep2_9 at second_image with Dissolve(0.2)
    # Pause for the desired duration
    pause 0.1
    # Set the x and y coordinates for the third image
    transform third_image:
        xalign 0.8
        yalign 0.05
        zoom 0.2
    play sound papermovement
    show ch1ep2_10 at third_image with Dissolve(0.2)
    # Pause for the desired duration
    pause 0.1
    yt "I can see three scenarios of how I could handle this... Mentz... whatever his name is..." #three small images on top of the current screen
    play sound papermovement
    show ch1ep2_10 at zoomouttop_image with Dissolve(0.2)
    play sound papermovement
    show ch1ep2_9 at zoomouttop_image with Dissolve(0.2)
    yt "First scenario: The good old \"Act of Confusion\"." #shows the first screen
    play sound pop
    show ch1ep2_8 at zoom_image
    mc "What...?"
    fr "Man, fuck you!"
    play sound papermovement
    show ch1ep2_8 at first_image with Dissolve(0.2)
    play sound papermovement
    show ch1ep2_8 at zoomouttop_image with Dissolve(0.2)
    play sound papermovement
    show ch1ep2_9 at second_image with Dissolve(0.2)
    yt "Second scenario: Outsmart him." #shows the second screen
    play sound pop
    show ch1ep2_9 at zoom_image
    mc "Hm-hmm!"
    fr "For real, for real. No cap, on God!"
    play sound papermovement
    show ch1ep2_9 at second_image with Dissolve(0.2)
    play sound papermovement
    show ch1ep2_9 at zoomouttop_image with Dissolve(0.2)
    play sound papermovement
    show ch1ep2_10 at third_image with Dissolve(0.2)
    yt "Third scenario: Be aggressive." #shows the third screen
    play sound pop
    show ch1ep2_10 at zoom_image
    mc "Fuck off, you son of a bitch!"
    fr "Say what now?!"
    play sound papermovement
    show ch1ep2_10 at third_image with Dissolve(0.2)
    play sound papermovement
    show ch1ep2_9 at second_image with Dissolve(0.2)
    play sound papermovement
    show ch1ep2_8 at first_image with Dissolve(0.2)
    yt "I don't want to sound overly suspicious, but whatever scenario I choose, I need to entice him enough to keep coming back here for the plan I have in mind." 
    yt "Then, finish him with Klara's grand finale."
    yt "If he were at least decent with his approach, I would've probably overlooked the fact that he's a complete twat."
    yt "But instead, my pride tells me I must put this guy in his place."
    play sound papermovement
    hide ch1ep2_8 with Dissolve(0.2)
    play sound papermovement
    hide ch1ep2_9 with Dissolve(0.2)
    play sound papermovement
    hide ch1ep2_10 with Dissolve(0.2)
    menu:
        with dissolve
        "Act of confusion":
            scene ch1ep2_11
            with dissolve
            mc "Um... the... what...?"
            fr "Oh, fuckin' hell... Of course, it would be the deaf servant who welcomes me."
            scene ch1ep2_12
            with dissolve
            fr "Read my lips, you thick donkey!"
            fr "Bring! Me! Aine! Agnor!"
            fr "Do you understand me now?"
            scene ch1ep2_13
            with dissolve
            mc "I... hold on, I'm still trying to process..."
            mc "You're Francis... Pretzeloctopus?"
            mc "And you're looking for... someone named Aine?"
            fr "Hmph, so you {i}can{/i} hear: you're just denser than lead!"
            fr "Mentzelopoutous, and my relationship with Aine is none of your business!"
            fr "Fetch her this instant! Do not dare to make me ask again!"
            mc "But... uhm... who is she? I've never met this Aine you're looking for."
            play sound woodhit
            fr "Do not waste my time! I was informed she would be here!" with hpunch
            fr "Sincerity dictates that I do not enjoy this state of idleness!"
        "Outsmart him":
            scene ch1ep2_14
            with dissolve
            mc "So, Sir Pretzeloctopus..."
            fr "That's Mentzelopoutous, you uncultured swine!"
            mc "Right, Metaloffofus."
            show ch1ep2_15
            fr "Hrrr... Why you little...!"
            mc "Anyways, you said you were looking for an Aine Agnor, correct?"
            fr "If your ears functioned properly, you would know the answer is {b}\"yes\"{/b}!"
            mc "I have never met her, but the fact that you're supposed to marry her means that she must come from wealth, no?"
            fr "Yes, I suppose."
            fr "Now hurry and bring her to me! I've already played enough of your games!"
            fr "Sincerity dictates that I do not enjoy this state of idleness!"
            scene ch1ep2_16
            with dissolve
            mc "That's the thing: there is nobody by that name here."
            play sound woodhit
            show ch1ep2_17
            with hpunch
            fr "Don't lie to me, boy! I do not take kindly to those that insult my intelligence!"
            mc "Just think about it: does this neighborhood seem like one she would pass through, let alone reside in?"
            scene ch1ep2_18
            with dissolve
            mc "A lovely young lady like her surely would be able to find a living arrangement far more appealing to someone of her status."
            mc "Hell, we even had to wait days for someone to fix our bathtub recently."
            mc "Would this Aine lady live somewhere where she has to go two full days without a functioning bath?"
            scene ch1ep2_19
            with dissolve
            mc "With all that said, I can assure you that nobody named either Aine or Agnor lives here."
            mc "I know you said you're in a rush, but you're more than welcome to look around this humble house for yourself if it would make you feel better."
            fr "There's no need. I suppose it would be well beneath her to live in this slum."
            mc "Hey, now-{w=0.5}{nw}"
            fr "I shall take my leave for now."
            fr "However, if I discover that you lied to my face, then I promise it will be the last lie you’ll ever tell!"
        "Be aggressive":
            scene ch1ep2_20
            with dissolve
            mc "Hm, so that dick-eating trap of yours does shut sometimes."
            fr "I beg your pardon?!"
            mc "I said what I said, pretty boy."
            play sound woosh
            show ch1ep2_21
            n "*whispers* Pffft! Haha!"
            a "Hm?"
            scene ch1ep2_22
            with dissolve
            mc "You had your turn to speak; now, it's my turn."
            mc "I don't care who the hell you are."
            mc "You don't come to {i}my{/i} house and threaten anyone."
            fr "Threaten?! Who said anything about malicious intent?!"
            mc "The fact that you pointed out you're her betrothed yet still can't find her tells me all I need to know about your personality and intentions."
            mc "First off, I don't know who this Aine person is."
            mc "Second, even if she were here, there is no fucking way I'd let you anywhere near her."
            mc "Now use that private school education to figure out what's good for you and get the fuck out of here."
            fr "How... dare you speak to me in this manner! You've just made the biggest mistake of your worthless life!" 
            play sound woodhit
            show ch1ep2_23
            mc "Then do something about it, Bitchie Billions. I'm right here." with hpunch
            fr "Sincerity dictates that I do not enjoy this state of idleness!"
            fr "I'll...! I'll-{w=0.5}{nw}"
    
    play music 'audio/DarkAngel.mp3'
    play sound horrorimpact
    transform image_klara_zoom:
        xalign 0.4 yalign 0.1
        zoom 1.0
        linear 60.0 zoom 1.5
    pause 0.2
    show ch1ep2_24 at image_klara_zoom
    pause
    fr "I-is someone there?"
    show ch1ep2_25 at image_klara_zoom
    with Dissolve(3.0)
    k "FUCK..."
    k "OFF..."
    play sound bodyfall
    show ch1ep2_26
    with hpunch
    fr "AIEEEEEEEEEEEE!!!!!!"
    fr "S-stay back! D-don't you know who I am?"
    play sound waterphone
    show ch1ep2_27
    pause
    k "{cps=30}Mentzelopoutous... a name unheard of, but thanks to me, it will haunt you forever..."
    k "{cps=30}It seems you've been asking the wrong questions, young man."
    k "{cps=30}You should be trembling as you inquire who the hell {i}{b}I{/b}{/i} am."
    scene ch1ep2_28
    with dissolve
    k "{cps=30}I am the one whose cursed property you dared to trespass onto with your cheap, imitation Nieman Marcus shoes."
    k "{cps=30}I am the one who takes pleasure in crushing the skulls of unwelcome guests on my land, regardless of their status or family name."
    k "{cps=30}I am the one who will become the ghastly apparition that haunts your every waking moment..."
    scene ch1ep2_29
    with dissolve
    k "{cps=30}... And the final vision that consumes your soul if you do not remove your filthy, sycophantic face from my presence in five seconds."
    fr "You-you're bluffing, surely?!"
    k "{cps=30}Oh? You care to try me, hm?"
    fr "..."
    k "{cps=30}Five."
    k "{cps=30}Four."
    k "{cps=30}Three."
    play sound running
    show ch1ep2_30
    fr "Okay! Okay! Just stay the hell away from me!"
    stop sound fadeout 2
    play sound2 cardriveaway 
    scene ch1ep2_31
    with dissolve
    k "... The rich ones always flee quickly."
    play music 'audio/RunForTheMan.mp3'
    play sound woosh
    show ch1ep2_32
    k "Good job handling that first interaction, but are you sure we should let him go like that?"
    k "We could've given him a quick and painless death. Well, maybe not so painless."
    scene ch1ep2_33
    with dissolve
    mc "... You're joking, right?"
    scene ch1ep2_34
    with dissolve
    k "..."
    scene ch1ep2_35
    with dissolve
    mc "Right?"
    scene ch1ep2_36
    with dissolve
    k "..."
    play sound woosh
    show ch1ep2_37
    mc "A-anyway..."
    mc "Let's gather everyone who's here at the moment. We have some important matters to discuss."

    scene black
    with dissolve
    with fade

    scene ch1ep2_38
    with dissolve
    mc "Now that everyone here knows what just happened..."
    mc "Let's hear what you have to say, Aine."
    a "Why me~? I don't even know what is going on~!"
    a "It was supposed to be his father, not him~!"
    a "When? How? Why? I don't know! I didn't approve of anything!"
    mc "Alright, alright. Calm down and breathe. We won't get anywhere if you're like this."
    scene ch1ep2_39
    with dissolve
    n "Francis is my ex-boyfriend."
    mc "Excuse me?"
    n "I know him fairly well, and I may be able to answer yer questions 'bout him."
    n "But, who are ya people for him to come to this place? What's yer connection with him?"
    n "I haven't seen him for Lord knows how long. And him being here doesn't exactly tickle my fancy."
    n "His condescendin' tone alone is enough to piss me off. And I'm a very patient person."
    scene ch1ep2_40
    with dissolve
    mc "..."
    k "I'll leave that decision to you."
    scene ch1ep2_41
    with dissolve
    mc "Alright then, listen up."

    scene black
    with dissolve
    with fadeq

    "An hour later..."

    scene black
    with dissolve
    with fadeq

    scene ch1ep2_42
    with dissolve
    mc "We are still trying to locate Jovian's whereabouts, but that's all we've been through."
    n "Okay, so count me in."
    mc "I'm sorry, what?"
    n "I told ya, he's my ex, and I can help ya make him rack off."
    mc "Yeah, you are exes, but you don't have to get involved with us."
    n "What happened between us is already behind me. I have my reason for wantin' to do this."
    mc "And... that is?"
    scene ch1ep2_43
    with dissolve
    n "I'm sure yer assumin' it by now, but Francis is a playboy."
    n "Sure, he's an idiot, but he's a dangerous bloke once he means things."
    e "Aine and I can vouch for that."
    mc "Huh..."
    scene ch1ep2_44
    with dissolve
    n "I discovered that after several weeks of being in a relationship with him, and so... I broke up with him shortly after."
    n "Frustrated with my decision, he fired my old man who was doin' work for him as retaliation."
    n "Our lives went downhill as he continued to spite my family and me whenever he had the chance."
    n "However, we were fortunate enough to recover from all that on our own when we moved to the countryside, away from his wrath."
    n "Now, I have a chance to return the favour, and I simply can't live knowin' that he could be lurkin' around these parts."
    mc "That's quite a concise explanation for something very horrible..."
    scene ch1ep2_45
    with dissolve
    n "I told ya I'm a straightforward person, mate."
    n "I hate creatin' drama, so if I have something to tell or ask from ya, I'll lay it out in one sentence if I can."
    scene ch1ep2_46
    with dissolve
    mc "Uhh... Gwen?"
    g "..."
    scene ch1ep2_47
    with dissolve
    n "..."
    scene ch1ep2_48
    with dissolve
    n "I won't look away just because yer older, ya know?"
    scene ch1ep2_49
    with dissolve
    g "I like her."
    scene ch1ep2_50
    with dissolve
    mc "Then how about you two? How do you know him?"
    scene ch1ep2_51
    with dissolve
    a "Well..."
    a "Emma and I have known him since middle school."
    scene ch1ep2_52
    with dissolve
    e "He was one of those boys who sought Aine's attention. The first one, in fact."
    e "There were too many, so we gave them nicknames. Hence him being \"Schoolboy A\"."
    play sound woosh3
    show ch1ep2_53
    n "Bloody hell, lass! I know yer quite the beauty and all, but I didn't know ya had heaps of suitors!"
    a "*sighs* They never became my suitors. I just turned them all down."
    a "And having my family name over my head acted like an insect repellent no matter how little..."
    a "But I have no idea when this all came to be. Mother didn't even mention anything about it when we were there."
    a "I'm so confused right now..."
    play sound woosh3
    show ch1ep2_54
    mc "You were forced into marriage, to begin with. There's nothing new about it."
    a "That's not the point!"
    yt "What's on your mind this time, Hera? Is this what you really want?"
    mc "Ugh... Why can't old people simply say what they want?"
    stop music
    play sound woodhit
    show ch1ep2_55
    with hpunch
    g "Whoa!" (multiple=2)
    mc "Eek!" (multiple=2)
    transform image_klaramc_zoom:
        xalign 0.45 yalign 0.1
        zoom 1.0
        linear 60.0 zoom 1.5
    play music 'audio/DarkAngel.mp3'
    scene ch1ep2_56 at image_klaramc_zoom
    with dissolve
    k "I told you, we could've just ended his miserable life..."
    k "Bury his decaying remains six feet deep in the backyard, where the worms will feast on his flesh. Or even better, entomb him in the basement, left to molder in darkness..."
    k "Then we can savor the sight of his body being devoured by maggots, cannibalized by his own kind, as we indulge in wine, the putrid stench only serving to enhance the experience..."
    k "No prying eyes nor cameras shall pierce this shadowy realm; I'll guarantee that no one ever discovers our secret..."
    k "Absolutely no one..."
    k "Our twisted secret will be forever locked away, hidden in the depths of our wicked souls..."
    scene ch1ep2_57
    with dissolve
    s "Uhm... Mom, are you okay...?"
    play music 'audio/RunForTheMan.mp3'
    play sound woosh
    show ch1ep2_58
    k "Yep! Perfectly fine, my dear!"
    mc "Phew!"
    image mcnatabfr:
        "ch1ep2_59.jpg"
        pause 3.0
        "ch1ep2_60.jpg"
        pause .2
        repeat
    show mcnatabfr
    with dissolve
    mc "So... I assume you have a plan, then?"
    n "I know his most vulnerable Achilles heel."
    n "Women, especially me."
    mc "You?"
    n "He was extremely frustrated when I broke up with him, and I know he still hasn't moved on from it."
    n "Or maybe he did, but I'll put money on it."
    n "I've been wantin' to do this for a long time, but I couldn't for personal reasons."
    n "Now, however... maybe I can."
    n "But for this to work, we need a build-up, and he needs to come back here."
    mc "*chuckles* It seems we have the same thing in mind."
    stop music fadeout 2

    if moonroute:
        scene black
        with dissolve
        with fade

        play sound2 dawnambient loop
        scene ch1ep2_61
        with dissolve
        pause 0.5
        scene ch1ep2_62
        with Dissolve(0.2)
        play sound thunder
        scene ch1ep2_61
        with Dissolve(1.0)
        pause
        scene ch1ep2_63
        with dissolve
        mc "..."
        yt "Looks like we are going to have a downpour tonight. I better move fast."
        play sound closedoor
        scene ch1ep2_64
        with dissolve
        k "[mc], did you bring an umbrella?"
        mc "Yeah!"
        k "Alright, be careful!"
        stop sound2
        play sound cardoorclose
        scene ch1ep2_65
        with Dissolve(0.1)
        pause
        scene ch1ep2_66
        with dissolve
        $ renpy.sound.set_volume(1.5, 1.0)
        play sound2 carstart
        pause 0.5
        scene ch1ep2_67
        with Dissolve(0.1)
        pause 0.8
        scene ch1ep2_67a
        with dissolve
        pause
        show ch1ep2_67b
        with Dissolve(2.0)
        pause
        $ renpy.sound.set_volume(1.0, 1.0)
        play sound3 thunder
        pause 0.5
        show black
        with Dissolve(0.2)
        pause 0.9
        stop sound2 fadeout 3
        play sound forestambience loop fadein 3
        scene ch1ep2_67c
        with Dissolve(2.0)
        pause
        scene ch1ep2_67d
        with Dissolve(2.0)
        pause
        play music 'audio/Circularity.mp3'
        scene ch1ep2_68
        with Dissolve(0.3)
        un "Four!"
        scene ch1ep2_69
        with Dissolve(0.2)
        m "Six!"
        scene ch1ep2_70
        with Dissolve(0.2)
        m "Eight!"
        scene ch1ep2_71
        with Dissolve(0.2)
        m "You made it!"
        scene ch1ep2_72
        with dissolve
        eg "Of course we made it! How many times do you think we've tried to escape before?"
        scene ch1ep2_73
        with dissolve
        si "Although, this is all we could secure. I'm unsure if this is enough, but at least they are all fully clipped." #guns
        m "It's fine. You two carry them. You're better than me when it comes to firearms, anyway."
        scene ch1ep2_74
        with dissolve
        eg "Let's get going. We should reach the border before sunrise, yeah?"

        scene black
        with dissolve
        with fadeq

        scene ch1ep2_75
        with dissolve
        si "Man~! I wonder what it's like outside now."
        m "Someone told me that many people are doing fine now that the war is over."
        scene ch1ep2_76
        with dissolve
        si "Hmm..."
        scene ch1ep2_77
        with dissolve
        si "When we're finally free, what do you guys plan on doing?"
        m "Haven't we talked about this already?"
        eg "I can worry about that once we leave this place. But maybe..."
        scene ch1ep2_78
        with dissolve
        eg "... Find a boyfriend? Gotta give your V-card to somebody someday, right?"
        si "Eugh~!"
        scene ch1ep2_79
        with dissolve
        eg "What about you?"
        si "Well, I'd like to get a job, you know?"
        si "But I must go to college first and get a degree. I heard it's hard to find a job without one."
        eg "That's rather a practical plan coming from someone as dumb as you."
        show ch1ep2_80
        si "Hey, don't judge me! You are not any better!"
        scene ch1ep2_81
        with dissolve
        eg "How about you, Four? Got something in mind?"
        m "..."
        scene ch1ep2_82
        with dissolve
        m "I'm... going to find my true purpose."
        si "True purpose? That's deep..."
        scene ch1ep2_83
        with dissolve
        si "You know, I’ve heard there's a world outside, with vast oceans and sandy shores."
        si "If we could escape this place, what if we open a cozy little beach café together?"
        scene ch1ep2_84
        with dissolve
        m "A beach café? I wonder where you heard about it. Nonetheless, that sounds like a wonderful dream, Six."
        m "But we've never seen much of the outside world. Are you sure it exists?"
        scene ch1ep2_83
        with dissolve
        si "I'm not entirely certain, but I believe it does."
        si "We can create a warm and inviting place where people from all walks of life could come and enjoy the sea, the sun, and our company."
        scene ch1ep2_84
        with dissolve
        m "Imagine waking up to the sunrise over the ocean, preparing the café for the day, and feeling the sand beneath our feet."
        m "It would be a life so different from what we've known."
        scene ch1ep2_83
        with dissolve
        si "And in the evenings, we could sit on the beach, watching the sunset while sharing stories and laughter, feeling the gentle sea breeze on our faces."
        si "It would be a taste of freedom we've never experienced."
        scene ch1ep2_84
        with dissolve
        m "It's a beautiful dream, Six."
        m "Even if we don't know for sure what the outside world holds for us, let's keep that dream alive, and maybe someday, we can make it a reality."
        eg "As I said, we can worry about that once we're out."
        scene ch1ep2_85
        with dissolve
        m "By the way, do you know someone named Maya from your squad?"
        si "Maya?"
        eg "Nope, never heard of that name before."
        scene ch1ep2_86
        with dissolve
        m "...{w=0.8}{nw}"
        play music 'audio/Ballad.mp3'
        play sound2 sniperfire_distant
        show sixshotslowmo
        pause 4.0
        play sound2 bodyhit
        show ch1ep2_87
        pause 0.3
        play sound2 bodyfall
        scene ch1ep2_88
        with hpunch
        pause 0.5
        play sound2 thud2
        show ch1ep2_89
        m "Six!"
        eg "No! Don’t fucking move! They're using her as bait!"
        m "But!"
        show black
        pause 0.1
        hide black
        show ch1ep2_89a
        with Dissolve(1.0)
        si "{cps=20}H-huh...?{w} Why can't I...{w} feel my leg?"
        hide ch1ep2_89a
        show black
        pause 0.1
        hide black
        show ch1ep2_89b
        with Dissolve(1.0)
        si "{cps=20}What... What happened...?"
        hide ch1ep2_89b
        show black
        pause 0.1
        hide black
        show ch1ep2_89c
        with Dissolve(1.0)
        si "{cps=20}Four...?{w} Eight...?"
        si "{cps=20}H-help...{w} my leg...{w} I can't..."
        eg "Throw a smoke, Four! I'll drag her out of there!"
        m "I... I don't have any!"
        eg "Urh, damn it!"
        hide ch1ep2_89c
        show ch1ep2_90
        m "C-crawl towards us, Six! Hurry!"
        si "{cps=20}Crawl...?{w} I..."
        m "Hurry, Six! Hurry!"
        eg "Keep your fucking head down, Four!"
        scene ch1ep2_91
        with dissolve
        si "{cps=20}Am I...{w} going to..."
        show ch1ep2_92
        m "You are not!"
        show ch1ep2_93
        m "Come on, reach my hand!"
        play sound2 sniperrechamber
        show ch1ep2_94
        with Dissolve(0.2)
        pause
        #images alternating/becomes faster and faster
        hide ch1ep2_94
        show ch1ep2_95
        with Dissolve(2.0)
        pause
        stop music fadeout 5
        pause 0.3
        hide ch1ep2_95
        show ch1ep2_94
        with Dissolve(0.1)
        pause 0.3
        hide ch1ep2_94
        show ch1ep2_95
        with Dissolve(0.1)
        pause 0.3
        hide ch1ep2_95
        show ch1ep2_94
        with Dissolve(0.1)
        play sound3 sixdeathtransition
        pause 0.3
        hide ch1ep2_94
        show ch1ep2_95
        pause 0.3
        hide ch1ep2_95
        show ch1ep2_94
        pause 0.3
        hide ch1ep2_94
        show ch1ep2_95
        pause 0.3
        hide ch1ep2_95
        show ch1ep2_94
        pause 0.2
        hide ch1ep2_94
        show ch1ep2_95
        pause 0.2
        hide ch1ep2_95
        show ch1ep2_94
        pause 0.1
        hide ch1ep2_94
        show ch1ep2_95
        pause 0.1
        hide ch1ep2_95
        show ch1ep2_94
        pause 0.1
        hide ch1ep2_94
        show ch1ep2_95
        pause 0.1
        hide ch1ep2_95
        show ch1ep2_94
        pause 0.05
        hide ch1ep2_94
        show ch1ep2_95
        pause 0.05
        hide ch1ep2_95
        show ch1ep2_94
        pause 0.05
        hide ch1ep2_94
        show ch1ep2_95
        pause 0.05
        hide ch1ep2_95
        show ch1ep2_94
        pause 0.05
        hide ch1ep2_94
        show ch1ep2_95
        pause 0.05
        hide ch1ep2_95
        show ch1ep2_94
        pause 0.05
        hide ch1ep2_94
        show ch1ep2_95
        pause 0.05
        hide ch1ep2_95
        show ch1ep2_94
        pause 0.05
        hide ch1ep2_94
        show ch1ep2_95
        pause 0.05
        hide ch1ep2_95
        show ch1ep2_94
        pause 0.05
        hide ch1ep2_94
        show ch1ep2_95
        pause 0.05
        show ch1ep2_96
        pause 0.5
        si "{cps=15}I... I don't want to die...{w=0.8}{nw}" with Dissolve(1.0)
        show ch1ep2_97
        m "Si-{w=0.4}{nw}"
        show black
        play sound sniperfire_distant
        pause 0.5
        play sound2 moonscream
        m "*screaming in anguish*"
        play sound exhale_female
        show moonblink
        with dissolve
        pause 8.8
        scene ch1ep2_98
        with dissolve
        pause 0.5
        scene ch1ep2_99
        with Dissolve(0.2)
        scene ch1ep2_98
        play sound thunder
        with Dissolve(1.0)
        pause
        scene ch1ep2_100
        with dissolve
        pause
        play sound2 cloth
        scene ch1ep2_101
        with dissolve
        pause
        play sound rain_heavy fadein 3 loop
        scene ch1ep2_102
        with dissolve
        pause
        scene ch1ep2_103
        with Dissolve(0.2)
        m "Ah..."
        scene ch1ep2_104
        with dissolve
        m "..."
        m "... Where are you?"
        $ renpy.sound.set_volume(0.5, 1.0)
        play sound2 rain_umbrella loop
        scene ch1ep2_105
        with dissolve
        pause 0.5
        play music 'audio/Forever.mp3'
        pause
        scene ch1ep2_106
        with dissolve
        mc "What are you doing? You'll get sick."
        m "... 'Sup."
        scene ch1ep2_107
        with Dissolve(0.2)
        gu "[mc], the rain's pouring harder! You should take shelter inside for now!"
        scene ch1ep2_108
        with dissolve
        mc "Come on."
        scene ch1ep2_109
        with dissolve
        m "Did you walk all the way here?"
        mc "Well, I could have, but it would not be that convenient, especially at this hour."
        mc "The truck is in the parking lot. I went through the other side. I thought you would be there since most students use that entrance."
        m "Sorry, I didn't mention where I'd be waiting."
        mc "You're lucky I know the academy well."
        $ renpy.sound.set_volume(1.0, 1.0)
        stop sound2 fadeout 2
        scene ch1ep2_110
        with dissolve
        mc "Man... it's not going to stop soon, is it?"
        m "I don't think so..."
        m "Night students can stay until eleven, don't worry."
        scene ch1ep2_111
        with dissolve
        mc "Yeah. Luckily, the guards still know me."
        m "Oh?"
        mc "I attend the alumni gathering every year, so..."
        scene ch1ep2_112
        with dissolve
        m "I see."
        mc "..."
        scene ch1ep2_113
        with dissolve
        mc "Were you just waiting for me to come, or did you remember something?"
        m "*chuckles* And yet, you came within seconds." 
        yt "... I'm not sure if she intended that to sound sexual, or if I'm just that curious about what she might do again."
        menu:
            "Really?":
                scene ch1ep2_114
                with dissolve
                mc "Really? Did that happen last time too?"
                m "Yeah, I was caught off guard and told you I was sleeping instead."
                mc "I'm quite curious about you, you know?"
            "I'm not that weak":
                scene ch1ep2_114
                with dissolve
                mc "I don't usually come within seconds. So, I'm not that weak, you know?"
                $ moonpoint += 1
                $ renpy.notify(moonnotif)
                m "You're quick on the uptake, Commander..." #smirking
                m "I honestly didn't expect you'd get that one. You're curious, aren't you?"
                mc "In more ways than one."
                m "Hmmmm..."
                mc "On a serious note, I'm {i}really{/i} curious about you."
        
        scene ch1ep2_115
        with dissolve        
        mc "Ever since that clash between you and Emma, and with what Klara said after that, it never left my mind."
        mc "Furthermore, you're the type of person who could appear strange to some."
        mc "You appear in the most unexpected ways. You do and say things out of the blue."
        mc "Who are you? Where did you come from, Moon Chi?"
        scene ch1ep2_116
        with dissolve 
        m "Would you listen if I told you?"
        mc "You bet I would. You've given me more than enough clues to be interested in the mystery that is you."
        mc "Of course, only if it's alright for you to talk about it."
        play sound2 cloth
        scene ch1ep2_117
        with dissolve 
        m "..."
        m "Let's take a walk."
        yt "Where on the moon's surface was she hiding her hair?"
        yt "*chuckles* \"Apply some 69 on me\", nice!"
        stop music fadeout 2

        scene black
        with dissolve
        with fade

        play music 'audio/DesolateSpace.mp3'
        $ renpy.sound.set_volume(0.3, 1.0)
        scene ch1ep2_118
        with dissolve 
        m "My name wasn't Moon, and my last name was never Chi."
        mc "Huh?"
        scene ch1ep2_119
        with dissolve 
        m "My name used to be Lee Ha-Jeong."
        stop sound fadeout 2
        scene ch1ep2_120
        with dissolve 
        mf "There she is, just like we discussed in our deal."
        scene ch1ep2_121
        with dissolve 
        mil "Can you walk?"
        m "..."
        mil "I'll take that as a no."
        play sound2 cloth
        scene ch1ep2_122
        with dissolve 
        mf "And my money?"
        scene ch1ep2_123
        with dissolve
        pause
        scene ch1ep2_124
        with dissolve 
        mf "Make sure I never see her again!"
        mil "..."
        mil "Trust me."
        mil "You won't."
        scene ch1ep2_125
        with dissolve 
        mf "This never happened, Sergeant!"
        play sound rain_heavy fadein 2 loop
        scene ch1ep2_126
        with dissolve 
        m "Amidst their war against Sha Crea, I was sold by my father to Glabia's military when I was twelve years old."
        m "But I couldn't care less about what would happen to me."
        m "I thought it might be a chance. I thought it was fine as long as I didn't end up in a slave market."
        mc "That's... fucked up..."
        mc "W-why? How can he just..."
        scene ch1ep2_127
        with dissolve 
        m "He wasn't my biological father."
        m "He said he picked me up somewhere but never told me where or who my real parents were."
        m "Glabia was in such desperate need of manpower to the point where they'd go as far as how they enlisted me."
        mc "If they needed military force, why someone as young as you? I don't get it."
        scene ch1ep2_128
        with dissolve 
        m "Well, the {i}me{/i} as you see now..."
        m "... Isn't really me, or who I was back then."
        mc "What?! I'm so confused!"
        m "I have no idea what they did to me. All I know is that it involved science or experiments with the human body."
        m "They said the younger you are, the higher your body's chance to endure the procedure."
        mc "What the hell..."
        stop sound fadeout 2
        scene ch1ep2_129
        with dissolve
        m "When I woke up, I felt different... stronger..."
        m "A lot stronger than my tiny body could handle... It felt like I could do anything."
        m "Then, I realized that it wasn't me anymore. My consciousness was somehow just entombed inside this new body."
        m "Honestly, I was glad..."
        m "That body filled with diseases was gone..."
        m "However..."
        scene ch1ep2_130
        with dissolve
        mil "What is your name?"
        m "Lee Ha-Jeong..."
        mil "Do you remember everything before you came here?"
        m "Yes."
        mil "Good. This proves you are one of the successful subjects."
        scene ch1ep2_131
        with dissolve
        m "Successful... subjects...?"
        mil "From now on, Lee Ha-Jeong is no longer of this world."
        mil "That person didn't exist, nor was she ever born."
        mil "You shall be called... {b}\"Subject Number Four\"{/b}."
        mil "You are nothing but a weapon. A tool to help us win this war."
        mil "Glabia's military now owns you. You don't have any freedom until you've served your purpose."
        mil "And that is to die fighting for his territory."
        m "..."
        scene ch1ep2_132
        with dissolve
        mil "I'm under your squad. Let's enjoy our time here while we are still alive, yeah?"
        scene ch1ep2_133
        with dissolve
        mil "Unlike you, I'm nothing but a normal human being, so don't mind me trying to act all high and mighty once in a while."
        mil "I'll be in your care, {i}Captain Number Four{/i}."
        play sound rain_heavy fadein 2 loop
        scene ch1ep2_134
        with dissolve
        m "The existence I entered into... was even worse."
        m "I killed hundreds against my own will. I was in a war I shouldn't have been fighting."
        m "I was nothing but a child without any other purpose but to offer my life for something I barely understood."
        m "I wasn't fighting for Glabia's glory. I was fighting to survive."
        m "Many of my friends tried to escape from the military. Yet no one ever did succeed."
        m "They all either died or were captured and detained for months with barely any water or food."
        scene ch1ep2_135
        with dissolve
        m "When the war finally came to an end, someone came to me and offered help to gain my freedom."
        m "She told me to take my friends with me, but they all had lost hope..."
        m "Except for my two closest friends..."
        m "Subjects Number Six and Eight..."
        stop music fadeout 2
        scene ch1ep2_136
        with dissolve
        mc "Did they..."
        m "Mhm."
        m "We were about to cross the border, but they were followed."
        m "... Six was shot in front of me, and Eight..."
        stop sound fadeout 2
        play music 'audio/ShallowWater.mp3'
        $ renpy.sound.set_volume(1.0, 1.0)
        show black
        with Dissolve(0.5)
        pause 0.5
        hide black
        play sound forestambience loop
        play sound2 moonscream
        show ch1ep2_137
        with hpunch
        pause
        play sound2 thud2
        show ch1ep2_138
        with hpunch
        eg "Four!"
        eg "No, Moon! Listen to me!"
        eg "You need to run!"
        m "What?!"
        show ch1ep2_139
        eg "That's Number Two with her goddamn sniper rifle, Four! She's the only one with that kind of  aim in this environment!"
        eg "I'm sure she followed me and Six, and if the rest of the Loyalists are with her, they will be here soon!"
        eg "No matter how much of a special subject you are, we will still be outnumbered!"
        eg "I'll distract Two and give you enough time to run!"
        m "I will not leave you behind, Eight! Six is already-"
        scene ch1ep2_140
        with Dissolve(0.4)
        eg "Unlike me, you and Six had real dreams! So it's alright if I die here in exchange for your freedom, Four!"
        eg "Go!"
        eg "Run, and don't look back!"
        eg "Find that purpose you were talking about! And promise me you'll use the name Six gave to you! That's all I ask!"
        scene ch1ep2_141
        with dissolve
        m "*hics*"
        play sound2 thud2
        show ch1ep2_142
        with hpunch
        eg "STOP CRYING AND RUN! THAT'S A FUCKING ORDER!"
        play sound2 woosh2
        show ch1ep2_143
        with hpunch
        pause 0.5
        play sound2 umpfire
        show ch1ep2_144
        eg "RAAAAAAHHHHHH!{w=2.0}{nw}"
        play sound2 sniperfire_distant
        show ch1ep2_145
        play sound3 gasp
        m "*gasps*"
        scene ch1ep2_146
        with Dissolve(1.0)
        eg "R-run..."
        eg "Don't... stop..."
        eg "For all of us... who have... and will die in this hell..."
        scene ch1ep2_147
        with dissolve
        eg "Survive... and live..."
        $ renpy.sound.set_volume(0.3, 1.0)
        play sound rain_heavy fadein 3 loop
        scene ch1ep2_148
        with dissolve
        m "She sacrificed herself for me."
        m "I could still hear her last words fade away as I ran for my life."
        mc "..."
        scene ch1ep2_149
        with dissolve
        m "If not for their support, I would've killed myself long ago. It was thanks to them that I'm here."
        m "I wanted to go back for their bodies and at least give them a proper burial, but..."
        m "..."
        m "Now, I can't even cry to mourn their deaths every year on the day when I lost them."
        mc "Why is that?"
        scene ch1ep2_150
        with dissolve
        m "Whatever the military did to me has had a slow side effect on my body."
        m "It eventually killed my tear glands, and my eyes started malfunctioning."
        mc "That's why you're always wearing glasses..."
        m "Mhm."
        m "If I get too emotional, blood comes out instead of tears. Then a sharp, excruciating pain in my eyes follows soon after."
        m "So I avoid crying even if I want to..."
        yt "Being unable to cry is something I've never heard of before. But I can't imagine the pain she has to endure by constantly holding herself back."
        mc "How were you... able to escape from that place?"
        scene ch1ep2_151
        with dissolve
        m "I don't know."
        mc "Wait, you... you don't know?"
        stop sound fadeout 2
        play sound2 forestambience fadein 2 loop
        scene ch1ep2_152
        with dissolve
        m "I was filled with adrenaline and had no idea how long I was at it, but I kept on running again and again."
        m "Last thing I recall, I fell and lost consciousness."
        stop sound2 fadeout 2
        $ renpy.sound.set_volume(1.0, 1.0)
        play sound seawaves fadein 2 loop
        scene ch1ep2_153
        with Dissolve(1.0)
        pause
        scene ch1ep2_154
        with dissolve
        pause
        stop music fadeout 2
        play sound2 watermovement
        scene ch1ep2_155
        with dissolve
        m "When I opened my eyes..."
        scene black
        with dissolve
        pause 0.3
        play music2 'audio/DearMoon.mp3' loop
        scene ch1ep2_156
        with Dissolve(5.0)
        m "... What I saw was freedom spread out before me."
        scene ch1ep2_157
        with Dissolve(2.0)
        pause
        play sound2 moonlaugh
        scene ch1ep2_158
        with dissolve
        m "I thought that if there was such thing as fate, I could only laugh at how cruel it was."
        play sound2 thud2
        show ch1ep2_159
        with hpunch
        m "And at that moment, I promised myself that I would keep living for both Six and Eight's sake."
        $ renpy.sound.set_volume(0.3, 1.0)
        play sound rain_heavy fadein 2 loop
        scene ch1ep2_160
        with dissolve
        m "Later, uncle found me lying on that beach and happily took me in. However, what boggles my mind is that..."
        mc "Glabia territory is in another country."
        m "That's right."
        m "How I got out and got here is still a mystery today."
        mc "If you think about it, it's just... impossible."
        image bfcttmlmomct:
            "ch1ep2_161.jpg"
            pause 3.0
            "ch1ep2_162.jpg"
            pause .2
            repeat
        show bfcttmlmomct
        with dissolve
        m "*chuckles* Maybe I was meant to find you."
        m "Because before you came into my life, I had nothing."
        m "However, lately..."
        scene ch1ep2_163
        with dissolve
        m "It's so much fun whenever you are around~!"
        yt "She's a simple girl with nothing but a simple wish."
        yt "To find where she belongs. Her purpose."
        yt "She wasn't kidding when she said she's like Emma. The only difference is that, unlike Emma, she has nowhere to go."
        m "I'm not sure if you are the purpose I'm looking for."
        m "Even if it's just a coincidence, I don't care."
        m "But the fact that you always come whenever I wish for it is enough for me to hope it is you."
        m "Maybe Six and Eight gave their lives for this. For me to meet you and fill what I'm missing."
        scene ch1ep2_164
        with dissolve
        mc "A life..."
        m "Mhm. That's all I want as I carry their dreams and the name Six gave me."
        m "I am not Lee Ha-Jeong."
        m "I am not Subject Number Four either."
        m "Now that I have you, I can finally start accepting myself as Moon Chi!"
        yt "This might just be the first {i}real{/i} smile I got from her so far."
        scene ch1ep2_165
        with dissolve
        mc "You know, I don't care what your real name is. It doesn't matter to me whether it's Lee Ha-Jeong or Moon Chi."
        mc "Aside from your name and physical body, you are still {i}you{/i}, and that's all that matters."
        mc "Now, whether or not I am the purpose you're looking for..."
        mc "I'll say, fuck that! It doesn't matter."
        scene ch1ep2_166
        with dissolve
        m "Huh?"
        mc "Because I will welcome you with arms open wide either way. Not because you need it, but because I want to."
        mc "Life is always full of uncertainties. So, how about we find out whether I am that person or not?"
        scene ch1ep2_167
        with dissolve
        m "..."
        scene ch1ep2_168
        with dissolve
        m "Yeah, I'd love that!"
        scene ch1ep2_169
        with dissolve
        m "{i}{cps=20}Six...{w} Eight..."
        m "{i}Is this it...?"
        m "{i}I found it, right...?"
        scene ch1ep2_170
        with dissolve
        pause 0.3
        scene ch1ep2_171
        with Dissolve(0.2)
        m "!!!"
        scene ch1ep2_172
        with dissolve
        m "*hics*"
        play sound2 woosh
        play sound3 bodyhit
        show ch1ep2_173
        with hpunch
        pause
        scene ch1ep2_174
        with dissolve
        mc "Hey, hey, hey! You said it hurts, didn't you? Did I say anything to make you cry?"
        scene ch1ep2_175
        with dissolve
        m "I just felt..."
        m "..."
        scene ch1ep2_176
        with dissolve
        m "No, never mind."
        if moonpoint == 4:
            label moonlollipopplay:
            if _in_replay:
                $ name = persistent.gallery_name
            stop music2 fadeout 3
            scene ch1ep2_177
            with dissolve
            mc "Well, will this cheer you up?"
            m "Mint?"
            mc "Mint."
            scene ch1ep2_178
            with dissolve
            m "Mind sharing?"
            scene ch1ep2_179
            with dissolve
            mc "Come and take it."
            play music 'audio/Adjunto.mp3'
            scene ch1ep2_180
            with dissolve
            pause
            scene ch1ep2_181
            with dissolve
            m "Mm, this tastes better than last time."
            m "Is it a different brand?"
            m "... Or is it because it just came out of your mouth?"
            mc "Probably because I want you to take it from me this time."
            scene ch1ep2_182
            with dissolve
            mc "Or perhaps you want something and are not afraid to get it?"
            mc "I'm still not quite used to this {i}Commander{/i} and {i}subordinate{/i} play, but I'll play along if we approach it our own way."
            m "*chuckles* God, I like you a lot. You're good at causing some {i}activity{/i} inside me."
            mc "Mind telling me what that activity is, hm? My dear subordinate..."
            m "..."
            scene ch1ep2_183
            with dissolve
            m "Wanna cross the line with me?"
            mc "Do you?"
            m "Order me, Commander..."
            mc "You ever kissed a man before?"
            m "No?"
            mc "Then close your eyes."
            scene ch1ep2_184
            with dissolve
            m "..."
            play sound2 woosh
            show ch1ep2_185
            m "Stop, not here."
            scene ch1ep2_186
            with dissolve
            pause
            play sound2 opendoor
            scene ch1ep2_187
            with dissolve
            m "Coast is clear."
            play sound2 closedoor
            play sound3 chairdrag
            show ch1ep2_188
            with hpunch
            pause
            mc "Hold on, are you su-"
            scene ch1ep2_189
            with dissolve
            pause
            scene ch1ep2_190
            with dissolve
            m "Yes, I am sure... Make me all dirty, Commander..."
            mc "In that case, are you prepared for your first order, Moon Chi?"
            scene ch1ep2_191
            with dissolve
            m "Your wish..."
            play sound2 cloth
            scene ch1ep2_192
            with dissolve
            m "... Is my command."
            play sound2 thud2
            show ch1ep2_193
            with hpunch
            mc "Ah, ah, ah. While I appreciate your ambition, obedient subordinates never move without direct orders."
            mc "Next time you make a mistake, there will be {i}consequences{/i}."
            m "Mmm... and what do these {i}consequences{/i} look like?"
            mc "Would you like a taste?"
            m "I think I would..."
            scene ch1ep2_194
            with dissolve
            mc "Just to see why you should obey, right?"
            m "Of course..."
            scene ch1ep2_195
            with dissolve
            "As soon as the words leave her mouth, you immediately close the distance, silencing her with your lips."
            "Surprised at first, she quickly regains her composure, deepening the kiss."
            "Pressing your body against hers, you hold the kiss for a few seconds before slowly breaking away."
            scene ch1ep2_196
            with dissolve
            mc "That punishment is called {b}the silent treatment{/b}."
            mc "Next time, you won't get off so easily with just a little silence."
            m "Then do you intend to make me scream, Commander?"
            m "I'm not afraid to take a {i}beating{/i}, you know."
            mc "Oh, really? That's a handy piece of intel..."
            m "But you've forgotten one critical rule regarding engagement, Commander."
            play sound2 woosh
            show ch1ep2_197
            mc "What wo- Hey!"
            "Before you can blink, Moon ducks and vanishes right before you."
            scene ch1ep2_198
            with dissolve
            "Intrigued, you look around until you feel a soft hand on your back."
            "From behind, you hear Moon whisper into your ear, sending chills down your entire body."
            scene ch1ep2_199
            with dissolve
            m "*whispers* Looking for something, [mc]?"
            scene ch1ep2_200
            with dissolve
            "You turn around to see her standing before you, her alluring dark eyes looking deviously into yours."
            scene ch1ep2_201
            with dissolve
            m "Never lose sight of your target."
            mc "Well played, Moon."
            mc "It seems like I could use a reminder of the rules. Why don't we make this fun for both of us?"
            m "I'm listening, Commander."
            mc "How about you use that little toy you're holding to show me what I should do?"
            scene ch1ep2_202
            with dissolve
            "As if reading your mind, she slowly licks the lollipop, circling the tip while never breaking your gaze."
            m "You mean this thing right here?"
            mc "... That's {i}exactly{/i} what I mean..."
            m "I like the way you think, Commander. I accept."
            mc "Perfect..."
            mc "But first, strip."
            m "As my Commander orders."
            play sound2 cloth
            scene ch1ep2_203
            with Dissolve(1.0)
            "With one swift movement, Moon removes her pants, then her top."
            "You cannot help but pause and stare at the sight before you."
            mc "Damn... what a beautiful full Moon tonight..."
            m "Do you intend to observe like last time, Commander?"
            m "Or do you plan to explore for yourself the mysteries of this Moon?"
            scene ch1ep2_204
            with dissolve
            mc "\"Houston\", \"Voyager I\" is at full liftoff, ready to explore that celestial body."
            m "Nerd... but \"Voyager I\" won't be exploring any depths today."
            m "Let's just start with exploring the surface for now. I don't think I'm ready for anything more yet."
            mc "Not a problem. Let's do what you're comfortable with."
            scene ch1ep2_205
            with dissolve
            mc "After all, I am a commander, not a tyrant."
            m "You're {i}my{/i} Commander, [mc]."
            m "Now..."
            scene ch1ep2_206
            with dissolve
            m "Let's start with this lesson: always attack the most vulnerable, {i}sensitive{/i} areas."
            mc "Yes, ma'am."
            mc "But let me borrow that for a second."
            scene ch1ep2_207
            with dissolve
            "Smiling inquisitively, Moon hands you the lollipop."
            scene ch1ep2_208
            with dissolve
            "You take the stick from her, licking the sweet, minty candy until it glistens in the light."
            scene ch1ep2_209
            with dissolve
            "Using the moistened tip, you slowly trace a circle around her nipple, leaving a trail of sweetness on her sensitive bud."
            scene ch1ep2_210
            with dissolve
            m "Aahhh..."
            "A quiet moan escapes from her lips."
            show ch1ep2_211
            "Sensing an opportunity to take further control of the situation, you place the lollipop back into her mouth."
            mc "No matter what happens, do not let it fall out of your mouth."
            mc "That's an order. Do you understand?"
            scene ch1ep2_212
            with dissolve
            "Moon gives you a small nod."
            m "Mhm..."
            mc "Good girl. Now it's time to study the lesson you've prepared for me."
            scene ch1ep2_213
            with dissolve
            "You lower your mouth towards her breast, sticking your tongue out towards her waiting nipple."
            scene ch1ep2_214
            with dissolve
            "But just before you make contact, you pause and look up at her, who looks down at you in return."
            "While there is excitement and anticipation in her eyes, you can also sense some apprehension."
            "Since this is her first time exposing herself so vulnerably to anyone, let alone a man, you can understand why she is still hesitant."
            mc "Hey, Moon."
            m "Mm?"
            mc "If you want me to stop, just say \"Stop\" or give me a sign like tapping my shoulder three times."
            mc "Don't feel like you have to force yourself to do anything just to please me. I promise I won't get mad if you want to stop."
            mc "We all have boundaries, and this first time will be about what makes you feel good."
            mc "Does that sound alright?"
            m "Mhm."
            "You can sense the tension leave her body as your assurance eases her worries."
            mc "Good. I better start the lesson, or we'll both get impatient."
            show moon1
            with Dissolve(1.0)
            pause
            "Unable to wait any longer, you flick your tongue down onto her nipple."
            "You follow the path you traced with the lollipop just moments ago, the sweet, minty flavor guiding the way."
            m "Hm! Mmhhh..."
            "Your first move elicits a surprised gasp from your subordinate, followed by a gentle moan of pleasure."
            "Motivated by the positive feedback, you continue to use your tongue to draw around her hardening teat, alternating speeds and directions so Moon can never anticipate your next move."
            m "Mm...nnhhhh...!"
            "Her nipple hardens to a point, the firm bumps on her cool skin contrasting with the smoothness of your warm tongue."
            yt "Moon... I can't imagine what you've been through to make it here."
            yt "Those Glabia fuckers... how dare they treat someone amazing like you as just a means to their end goal."
            yt "I know I'm far from perfect, but I will always promise you one thing."
            yt "You will always have a home and a purpose with me."
            yt "I would be a fool to let you go."
            m "Hmmm!!"
            mc "Faster? Of course!"
            pause
            show moon2
            with dissolve
            "Sensing she is close to the edge, you change tactics."
            "Your lips envelop her firm nub. You suck firmly but gently, your tongue continuing to circle her hidden nipple."
            m "Gmmm! Hmmm!!"
            yt "That's it, Moon. Let the feeling flow throughout your body."
            yt "Let's make this a moment you'll always remember."
            yt "Hope you don't mind disobeying because I don't plan to stop until you can't hold back anymore."
            m "Mmh!! Urhhh!!"
            "The corners of Moon's mouth open ever so slightly, revealing a crack in her resilient attempt to diligently obey your order."
            "The small window of opportunity is all you need to channel your focus into one goal:{w} make Moon {b}scream{/b}."
            yt "I've got you right where I want you, Moon."
            yt "You said you don't mind a little roughness, so let's see how you react to {i}this{/i}."
            hide moon1
            hide moon2
            show ch1ep2_215
            "You take Moon's nipple between your teeth, nibbling gently."
            play sound2 woodhit
            show ch1ep2_216
            with hpunch
            m "Naaaaahhh!!!"
            "This change in sensation snaps her last threads of resistance."
            "Moon's mouth opens wide, letting out the cry of pleasure that she had been holding back with all her willpower."
            "The lollipop falls, bouncing off her plump breast before finally resting in her lap."
            scene ch1ep2_217
            with dissolve
            "Satisfied with your actions, you finally break away from her nipple, the skin still wet from your hard work."
            "As she struggles to regain her breath, you speak up. "
            mc "How do you feel, dear subordinate?"
            m "Hh... like I'm... I can't... wow..."
            m "I've never... felt anything... like that... ever..."
            mc "I'm glad you found my learning techniques acceptable."
            mc "But unfortunately, I must point out that you disobeyed a direct order from your Commander."
            mc "I told you not to let that fall out of your mouth regardless of what happens, did I not?" #pointing at lollipop
            m "You did..."
            mc "And as you know, failure to obey an order leads to punishment."
            scene ch1ep2_218
            with dissolve
            m "Oh?"
            mc "Mhm- can't have my subordinate think I'm getting {i}soft{/i} on her."
            m "Then tell me, Commander:{w} what do you intend to do with me?"
            mc "On your knees, Chi. You need to learn the proper way to satisfy your Commander with obedience."
            m "Yes, sir."
            mc "But before that, let me clean up the small mess you made when you disobeyed."
            m "No: a subordinate should clean up her own mess, Commander."
            scene ch1ep2_219
            with dissolve
            "Keeping her eyes on you the whole time, she slowly drags her finger along her breast."
            scene ch1ep2_220
            with dissolve
            "She then licks her finger clean, making sure to travel its whole length as she smirks at you."
            m "See? All clean and at your service, Commander."
            mc "... Hot DAMN..."
            play sound2 thud2
            scene ch1ep2_221
            with dissolve
            "She lets out a small chuckle at your response, then kneels before you."
            m "Well, Commander [mc], will you punish me by making me clean your rifle?"
            mc "Very perceptive of you. But I expect you to polish the whole thing, not just the barrel."
            m "Of course, Commander. I always make sure to take care of {i}every{/i} objective."
            scene ch1ep2_222
            with dissolve
            m "But if I may, what would you say to making things more interesting?"
            mc "You had my curiosity, but now you have my attention."
            m "I think it's only fair that a Commander demonstrates the proper way to execute the task his subordinate failed."
            m "Your subordinate has to learn somehow, doesn't she?"
            m "But that's not all."
            mc "Go on..."
            m "If you can succeed where I failed, I'll let you put your dick inside me..."
            m "... And I don't just mean inside my mouth..."
            mc "Ohhh yes... I have no choice but to accept."
            m "I knew you would, Commander. Now, please open wide."
            scene ch1ep2_223
            with dissolve
            "You do as she says, and she puts the lollipop inside your mouth."
            show ch1ep2_224
            with hpunch
            m "Ghhk!"
            "As soon as you close your lips, she surprises you by trying to take your whole length into her mouth."
            show ch1ep2_225
            with hpunch
            m "*coughs* Kuh! Urk!"
            mc "S-start slowleh; dun try tuh take it all ah once."
            "You speak out of the corner of your mouth, careful not to drop the lollipop."
            scene ch1ep2_226
            with dissolve
            m "Looks like I need some more practice first. Maybe I'll start with just the tip?"
            "You nod in agreement, signaling for her to try again."
            m "Actually, I think I know a better way to take care of your artillery gun."
            show moon3
            with Dissolve(1.0)
            pause
            "This time, she wraps her lips around your balls, sucking gently before sucking more intensely."
            "An unexpected change in sensation, but a very {i}pleasant{i} surprise for you."
            mc "That's... ah... better..."
            "Her small lips form a tight seal around your sack, sending waves of pleasure through your lower body as she moves her tongue back and forth."
            "Simultaneously, she begins to stroke your cock with her hand, squeezing softly like she's afraid to hurt you."
            mc "You can stroke-hmm! A bit harder."
            "Encouraged by your advice, she holds your dick firmly, stroking slowly as she continues to suck on your scrotum."
            mc "... Good!"
            yt "Fuck, not just good-{i}damn{/i} good..."
            yt "Is this really her first time doing this?"
            yt "I know it is, but how her hands and mouth are moving... it's like she naturally knows exactly what to do."
            yt "If she keeps going like this, I won't last long..."
            yt "Dammit [mc], whose first time is it now? Ahah..."
            m "Hm? Let's see if you can keep your mouth closed after this."
            show moon4
            with dissolve
            "As if she read your mind, Moon speeds up, licking and sucking your balls with a renewed vigor to exact revenge for what you did to her."
            "She simultaneously strokes the full length of your cock, squeezing firmly at the base and gradually releasing her hold as she reaches your tip."
            mc "Hrhhh!"
            yt "Shit! She's {i}good{/i}..."
            yt "... And yet so {i}bad{/i}!"
            yt "Fuck! Nobody's made me cum this quickly before."
            yt "I have to resist the urge... but... getting harder... to hold back!"
            "Sensing you're approaching the edge, Moon speeds up even more."
            yt "Dammit! I'm gonna cum!"
            mc "Moon! I'm cumming!"
            m "Hm?"
            hide moon3
            hide moon4
            show ch1ep2_227
            with hpunch
            mc "I'm-hruuhhhh!!"
            "You expel your load, narrowly missing Moon's face."
            "Her eyes open wide in surprise."
            "But her expression quickly changes to amusement once she sees your face."
            scene ch1ep2_228
            with dissolve
            m "Well, Commander, it seems like you were unable to practice what you preach."
            "Sure enough, your mouth hangs open as you gasp for air, lollipop on the ground."
            mc "Well...{w} that was...{w} quite the {i}job{/i} well done."
            mc "You clearly possess...{w} a unique set...{w} of skills..."
            m "Well, I've already found you, so should I kill you, Commander?"
            mc "Damn near just did with your bare hands... and mouth..."
            m "As much as I like you, your failure does mean that you won't get to explore the full Moon after all, Commander."
            "You hate to admit it, but she's right. A deal is a deal."
            mc "Ah, that's a shame, but I'll survive. You were already amazing today!"
            mc "You want to go-{w=0.5}{nw}"
            show ch1ep2_229
            m "But that doesn't mean we have to be done."
            mc "Interesting..."
            scene ch1ep2_230
            with dissolve
            m "You've been nothing but a kind and considerate Commander to me, so you deserve a reward."
            m "Maybe you won't get to unlock all of my secrets, but I can still give you a {i}teaser{/i}, if you're up for that?"
            menu:
                "End things here":
                    mc "As tempting as that sounds, we should probably head back now. It's getting late, and I don't want you to be too tired to wake up for school."
                    scene ch1ep2_231
                    with dissolve
                    m "... Yeah, you're right. But thank you so much for today."
                    mc "No, thank {i}you{/i}. I don't know what I did to deserve someone as amazing as you."
                    mc "But I cannot thank the universe, fate, or whatever caused our paths to cross enough."
                    mc "You'll always have a purpose with me, Moon. Until I die, I promise you'll never have to wander this world alone again."
                    m "Thank you, [mc]. Thank you for everything."
                    mc "Now let's get going before they find us and kick us out of here like this!"
                    m "Mhm!"
                "One more round":
                    mc "How can I say no to such a generous offer?"
                    mc "Since it's your treat, tell me what happens next."
                    m "Sit."
                    "You do as she says, sitting on the closest desk."
                    play sound2 chairdrag
                    scene ch1ep2_232
                    with dissolve
                    mc "As you command, dear subordinate."
                    m "Smartass. Now you just stay where you are. I want to try something."
                    scene ch1ep2_233
                    with dissolve
                    "Moon climbs onto the desk, positioning her feet behind you and grabbing your knees for support."
                    "She then slowly lowers herself until the tip of her clit rests against the base of your dick."
                    m "I've heard of the cowgirl position before, but since we can't do that today, I will try my unique take on it."
                    mc "Go ahead, Moon. I think you have the right idea already."
                    show moon5
                    with Dissolve(1.0)
                    "She begins moving up and down your member, using her clit to stimulate you both."
                    "You can feel the moisture of her labia sliding against your erect cock, gliding her clit smoothly against you."
                    "Still sensitive from Moon's last assault, waves of pleasure immediately begin coursing through your body again."
                    mc "Fffuck! You sure are a natural at this!"
                    m "Hnhh! Are you calling me a whore?"
                    mc "I wouldn't dare."
                    m "Maybe I'd like it if you called me a dirty name..."
                    mc "Oh, really? I'll-hm! Keep that in mind for next time."
                    m "C-confident there will be a next time, are we?"
                    mc "Why not? I think we make a nice pair."
                    m "Maybe, just maybe if... nnh... you play your cards right, Commander..."
                    mc "I can live with... that for now!"
                    pause
                    hide moon5
                    show moon6
                    with dissolve
                    "Moon quickens the pace, surprising you again with how much energy she can derive from such a small body."
                    m "Hnngg! Hmmmm!!"
                    "Her juices coat the bottom of your dick, allowing her to grind even faster."
                    m "Aahhh! Aaaahhhh!"
                    mc "Hmmg! Grmmm!!"
                    "As she continues to grind, your moans become guttural and more frequent, signaling that you both are approaching your limits."
                    "Pleasure floods from your dick to throughout your entire body, almost overwhelming you to the point of collapse."
                    "Somehow, you manage to keep your balance, allowing Moon's clit to continue attacking your manhood with no mercy."
                    mc "Arggh! Fuck! Moon, I'm gonna cum again!"
                    m "Mmmh! Me too!"
                    m "Cum on me! I don't care where! Just do it!"
                    menu:
                        "Cum on her face":
                            hide moon6
                            play sound2 woodhit
                            show ch1ep2_234
                            with hpunch
                            m "Nghiiaaaaa!! [mc]!!!!"
                            "As soon as she finishes giving this final command, she screams in ecstasy, her body contracting in wave after wave of unabated bliss."
                            mc "Moon-let me mark you as mine!"
                            mc "Kneel! Now!"
                            play sound2 thud2
                            show ch1ep2_235
                            with hpunch
                            "Whether consciously or subconsciously, Moon falls to her knees, unable to stand."
                            show ch1ep2_236
                            with hpunch
                            "You caress her face with one hand, using the other to hold your cock as you shoot stream after stream of hot liquid onto her face."
                            play sound2 thud3
                            show ch1ep2_237
                            with hpunch
                            "You then collapse next to her, giving you a close look at your handiwork."
                            mc "Hah... so sorry... got carried away..."
                            "Moon glares at you for one second, then raises her open hand above her head."
                            show black
                            pause
                            "You brace for a slap which... never comes."
                            scene ch1ep2_238
                            with dissolve
                            "You open your eyes and see Moon using her finger to wipe some of your cum off of her."
                            scene ch1ep2_239
                            with dissolve
                            pause
                            scene ch1ep2_240
                            with dissolve
                            "She looks at it, then shrugs and sticks her finger into her mouth."
                            "You can only stare at her, speechless at her actions."
                            m "Mmm... I love salty flavors..."
                            m "Thanks for the snack, Commander."
                            m "Or should I say, {i}Cum{/i}mander?"
                            mc "... you really are something else, Moon Chi."
                        "Cum on her stomach":
                            hide moon6
                            play sound2 woodhit
                            show ch1ep2_234
                            with hpunch
                            m "Nghiiaaaaa!! [mc]!!!!"
                            "As soon as she finishes giving this final command, she screams in ecstasy, her body contracting in wave after wave of unabated bliss."
                            mc "Moon-don't fall!"
                            mc "I'm cumming right now!"
                            show ch1ep2_241
                            with hpunch
                            "Unable to hold back, you shoot stream after stream of hot liquid all over her stomach."
                            scene ch1ep2_242
                            with dissolve
                            "The liquid flows down her ribs, forming several small rivers that rise and fall with each breath."
                            mc "Hah... so sorry... got carried away..."
                            scene ch1ep2_243
                            with dissolve
                            "Moon glares at you for one second, then raises her open hand above her head."
                            show black
                            pause
                            "You brace for a slap which... never comes."
                            scene ch1ep2_244
                            with dissolve
                            "You open your eyes and see Moon using her finger to wipe some of your cum off her."
                            scene ch1ep2_245
                            with dissolve
                            pause
                            scene ch1ep2_246
                            with dissolve
                            "She looks at it, then shrugs and sticks her finger into her mouth."
                            "You can only stare at her, speechless at her actions."
                            m "Mmm... I love salty flavors..."
                            m "Thanks for the snack, Commander."
                            m "Or should I say, {i}Cum{/i}mander?"
                            mc "... you really are something else, Moon Chi."
                    stop music fadeout 2
                    
                    scene black
                    with dissolve
                    with fade

                    play music 'audio/Forever.mp3'
                    scene ch1ep2_247
                    with dissolve
                    mc "Well, we should probably head back now. It's getting late, and I don't want you to be too tired to wake up for school tomorrow."
                    scene ch1ep2_248
                    with dissolve
                    m "Yeah, you're right. Thank you so much for listening to me."
                    mc "No, thank {i}you{/i}."
                    mc "I don't know what I did to deserve someone as amazing as you, but I cannot thank enough the universe, fate, or whatever caused our paths to cross."
                    mc "You'll always have a purpose with me, Moon."
                    mc "Until I die, I promise you'll never have to wander this world alone ever again."
                    scene ch1ep2_249
                    with dissolve
                    "You can see the effect that your words have on Moon."
                    "Though she cannot cry, her grateful smile is all you need to ensure that you will always keep that promise, come hell or high water."
                    m "Thank you for saying that, [mc]. Thank you for everything."
                    mc "There's no need to thank me, Moon. You deserve to feel like you belong."
                    mc "Now, as much as I want to keep heaping praises on you, let's get going before they find us and kick us out!"
                    scene ch1ep2_250
                    with dissolve
                    m "What are we going to do, though?"
                    m "... I think the rain isn't going to stop anytime soon."
                    mc "Should we run to the parking lot? We got an umbrella anyway."
                    m "Unless we want to make everyone wait."
                    mc "Yeah, let's just run."
                    $ renpy.sound.set_volume(1.0, 1.0)
                    scene ch1ep2_251a
                    with Dissolve(2.0)
                    pause
            $ renpy.end_replay()
        else:
            scene ch1ep2_251
            with dissolve
            m "... I think the rain isn't going to stop anytime soon."
            mc "Should we run to the parking lot? We got an umbrella anyway."
            m "Unless we want to make everyone wait."
            mc "Yeah, let's just run."
    stop sound fadeout 2
    stop music fadeout 2
    stop music2 fadeout 2
    $ renpy.music.set_volume(1.0, 1.0)
    $ renpy.sound.set_volume(1.0, 1.0)

    call hide_days from _call_hide_days
    with dissolve
    scene black
    with dissolve
    with fadeq

    show screen day_thursday with dissolve
    "Three days later..."
    "Thursday afternoon..."

    scene black
    with dissolve
    with fadeq

    play music 'audio/TheDetective.mp3'
    play sound cityalley loop
    scene ch1ep2_252
    with dissolve
    pause
    scene ch1ep2_253
    with flash
    un "You demanded this, Francis, so failure is not an option."
    un "Return to your post and execute your task flawlessly."
    un "I expect not to lay eyes on you until you've achieved tangible outcomes."
    un "Remember, only results hold any significance. That has always been my lesson to you."
    scene ch1ep2_252
    with flash
    pause
    scene ch1ep2_254
    with dissolve
    fr "Ugh... those two! They undoubtedly orchestrated that!"
    fr "My self-esteem and pride took a hit that night, but I shall reclaim them!"
    fr "This isn't just about locating Aine anymore!"
    scene ch1ep2_255
    with dissolve
    fr "First, I must move clo-{w=0.5}{nw}"
    stop music
    play sound2 twinkle
    show ch1ep2_256
    fr "Wooooow...!"
    fr "Wait, something isn't right!"
    play music 'audio/InsideTheTent.mp3'
    play sound2 woosh
    show ch1ep2_257
    shu "*hics* *whimpers*"
    shu "Ooww~!"
    play sound2 woosh3
    show ch1ep2_258
    fr "*chuckles* Hm..."
    fr "Greetings, Miss. You seem to require assistance. Allow me, a {i}distinguished{/i} gentleman, to offer my expertise and cunning."
    scene ch1ep2_259
    with dissolve
    shu "*hics* Please! I accidentally stepped on a rock and twisted my ankle!"
    shu "Oowie~!"
    fr "Well, don't worry. Sir Francis has come just in time to save your day."
    stop sound fadeout 2
    scene ch1ep2_260
    with flash
    n "And that's all there is to it. Simple, yet effective."
    n "I'll install hidden cameras around the area as soon as possible and let one of ya keep eyes on it."
    mc "Good idea. Freya might be able to take that responsibility."
    mc "As for the first phase, you can leave it to me."
    scene ch1ep2_261
    with dissolve
    mc "I have just the right person in mind."
    shu "... Me? Why me?"
    scene black
    with Dissolve(0.2)
    pause 0.8
    play sound smallbell
    show ch1ep2_262
    g "Damn... Look at you!"
    g "I still can't comprehend how making you cross-dress is so freaking easy!"
    scene ch1ep2_263
    with dissolve
    shu "You happy now, woman?"
    play sound closedoor
    scene ch1ep2_264
    with dissolve
    f "I have them, Gwenny!"
    g "Bring them here before that guy gets near the house. Good that you spotted him early."
    shu "W-w-wait, what are those?!"
    play sound woosh
    show ch1ep2_265
    f "Hm-hmmm~!"
    shu "No... anything but that!"
    scene ch1ep2_266
    with dissolve
    f "Mmmm?"
    shu "No. NO. NO! NOOO!"
    f "Yes, yes, yes, yes~!"
    play sound cityalley loop
    scene ch1ep2_267
    with flash
    fr "Here, let me help you."
    shu "Ow! It hurts so bad!"
    play sound2 twinkle
    scene ch1ep2_268
    with dissolve
    fr "Fret not, my lady. I'll carry you all the way home."
    fr "{i}Our{/i} home."
    shu "Really~?"
    fr "Of course! Don't you know who I am?"
    fr "I am Sir Francis Mentzelopoutous, son of Bonheur Mentzelopoutous and heir to the Mentzelopoutous Industries fortune."
    fr "I shall protect you with my life and ensure you never suffer harm again."
    scene ch1ep2_269
    with dissolve
    pause
    scene ch1ep2_270
    with dissolve
    shu "Thank you, my hero."
    fr "Although I lament the situation in which we met, I am thankful that I happened upon this neighborhood today."
    fr "I'm certain the Gods and Deities intended for our paths to cross in he-{w=2.0}{nw}"
    play sound2 thud3
    show ch1ep2_271
    pause
    play sound2 woosh
    show ch1ep2_272
    shu "Oh, whoops!"
    scene ch1ep2_273
    with dissolve
    fr "..."
    shu "..."
    scene ch1ep2_274
    with dissolve
    fr "Y-y-y-y-your..."
    shu "*imitating a deep voice* Yeah, I'm a dude."
    fr "I-I've been kissed..."
    fr "By a male...?"
    shu "*imitating a deep voice* Yep!"
    play sound2 wilhelmscream
    show ch1ep2_275
    with hpunch
    fr "AAAAHHHH~! DADDY~!" #Wilhelm Scream sfx
    shu "Hey, mister~! Come back again, okay~? We have so much more to share with each other~!"
    scene ch1ep2_276
    with Dissolve(1.0)
    pause
    play sound2 introslam
    show ch1ep2_277
    shu "Fare thee well, my dignity..."
    stop sound fadeout 2
    stop music fadeout 2

    scene black
    with Dissolve(2.0)
label shupause:
    if _in_replay:
        $ name = persistent.gallery_name
    scene shupause
    with dissolve
    $ renpy.pause()
    $ renpy.end_replay()
    play sound 'audio/gamepause.mp3'
    show title at move_slide
    with flash
    $ renpy.notify(imageunlock)
    $ renpy.pause()

    scene black
    with Dissolve(1.0)
    pause 1.0
    play music 'audio/InsideTheTent.mp3'
    play sound smallbell
    show ch1ep2_278
    pause
    scene ch1ep2_279
    with dissolve
    mc "Hey, buddy! How did it go?"
    shu "It worked, but I want my dignity back..."
    scene ch1ep2_280
    with dissolve
    mc "See? I told you it would work."
    n "I'm deeply impressed."
    mc "I knew it would take a narcissist to fight another one effectively."
    mc "Plus, with Shu's looks and build, he can easily be mistaken for a girl."
    scene ch1ep2_281
    with dissolve
    s "You guys are evil..."
    scene ch1ep2_282
    with dissolve
    n "Which makes me wonder..."
    n "Are you {i}actually{/i} a boy?"
    shu "A man! I'm a man!"
    play sound closedoor
    scene ch1ep2_283
    with Dissolve(0.3)
    f "[mc]! I got perfect footage!"
    mc "Oh? Well, it-{w=0.5}{nw}"
    play sound woodhit
    show ch1ep2_284
    with hpunch
    shu "DELETE IT~!"
    shu "SAVE WHAT LITTLE DIGNITY I HAVE LEFT~!"
    shu "HAVE YOU NO MERCY~?!"
    scene ch1ep2_285
    with dissolve
    n "Nevertheless, you did a bang-up job, Shu. I'm proud of you."
    play sound woosh
    show ch1ep2_286
    shu "Hmm...! Hmhmhmmm...!"
    n "Wha-what am I looking at?"
    scene ch1ep2_287
    with dissolve
    mc "Oh, sometimes he loves getting praised."
    g "Sometimes?"
    scene ch1ep2_288
    with dissolve
    shu "I'm still worthy!"
    g "Oh boy..."
    scene ch1ep2_289
    with dissolve
    mc "Just delete that video, Frey. The plan worked: that's what's important."
    f "Are you sure? I mean..."
    scene ch1ep2_290
    with dissolve
    mc "..."
    mc "When did you start growing?"
    f "I'm on heels."
    mc "That's not what I meant..."
    scene ch1ep2_291
    with dissolve
    shu "No, no! Please don't delete it! It's proof I can still reach greater heights!" #still blushing and hugging himself
    f "What do you mean, {i}greater heights{/i}?"
    shu "Furthermore, we may still use it against him. Who knows?" 
    mc "Are you sure?"
    shu "Yeah!"
    mc "... Then could you snap out of it? Your fifteen minutes of fame are over, dude."
    mc "Come and help us over here."
    shu "Send the video to me later, okay?"
    f "Why the sudden change of heart?"
    if gwenroute:
        scene ch1ep2_292
        with dissolve
        g "Can I go outside for now?"
        mc "You good?"
        g "Yeah, I just need to collect my thoughts."
        mc "Alright, then."
        play sound closedoor
        scene ch1ep2_293
        with dissolve
        shu "What happened to her? She seems troubled."
        f "I dunno. She was fine this morning."
        scene ch1ep2_294
        with dissolve
        a "*whispers* Her mom's birthday is coming up."
        mc "... How come she never told me about it?"
        a "*whispers* I heard that they aren't on good terms. Perhaps that is the reason?" 
        mc "I know that, but still..."
        mc "Hmm..."
    scene ch1ep2_295
    with dissolve
    n "It looks like we're done with everythin' down here. All that's left are yer rooms."
    mc "Yeah, movers carried the new beds to each room yesterday. You should be good."
    n "Ya helping?"
    mc "I'll double-check things down here, then try to catch up to you if I can."
    n "Gotcha."
    scene ch1ep2_296
    with dissolve
    a "Wait, we'll help!"
    scene ch1ep2_297
    with dissolve
    f "Sorry, I can't help! I need to start my stream ASAP! Byeeee~!"
    mc "All good. Good luck with your stream."
    play sound closedoor
    scene ch1ep2_298
    with dissolve
    mc "How about you?"
    shu "..."
    play sound closedoor
    show ch1ep2_299
    mc "*sighs*"
    stop music fadeout 4
    scene ch1ep2_300
    with dissolve
    mc "..."
    yt "Why is she staring at that empty cabinet?"
    play sound horrorimpact
    show ch1ep2_28
    with hpunch
    pause 0.1
    scene ch1ep2_300
    mc "Ugh..."
    menu:
        "Talk to her":
            $ klararoute = True
            play music 'audio/TheSpy.mp3'
            scene ch1ep2_301
            with dissolve
            k "Hm? Yes, dear?"
            mc "You've been staring at that cabinet for a while now. What did it do to you?"
            k "I'm estimating how many cans of tomato sauce I can fit in here."
            mc "For bolognese?"
            k "Sure."
            scene ch1ep2_302
            with dissolve
            mc "..."
            scene ch1ep2_303
            with dissolve
            k "..."
            scene ch1ep2_304
            with dissolve
            mc "... For bolognese, right?"
            scene ch1ep2_305
            with dissolve
            k "..."
            scene ch1ep2_306
            with dissolve
            mc "..."
            show ch1ep2_307
            k "Haha! Of course, for bolognese! What else were you thinking, [mc]?"
            mc "Well, I thought it involved a human victim."
            play sound punch
            show ch1ep2_308
            with hpunch
            k "Are you implying I'm letting you eat humans, hm?"
            mc "No, no! It's just... you've been very in touch with your dark side lately. And I'm honestly worried if you're okay or not."
            image blklsttwmc:
                "ch1ep2_309.jpg"
                pause 3.0
                "ch1ep2_310.jpg"
                pause .2
                repeat
            show blklsttwmc
            with dissolve
            k "It must be the constant stress and pressure finally getting to me. I've had a lot to think about these past few days."
            k "Our company, you and Sky, the problem about Jovian, that Francis guy, refurnishing the house..."
            k "*sighs*"
            mc "Wait, wait! Refurnishing the house and your company is your responsibility, but the rest falls upon me."
            mc "You don't have to carry everything on your shoulders. I'm at the age where I should be repaying you for taking care of me."
            mc "So at least let me take on my responsibilities, you know?"
            k "We've talked about that, I know. But I also have another thing in mind..."
            mc "Uh-huh? Which is?"
            k "I didn't think I would be exposed, especially to you."
            mc "Expo-{w=0.5}{nw}"
            mc "Ooohh...!"
            mc "Yeah, now that I remember it, I'm gonna go tell Sky!"
            show ch1ep2_311
            mc "Sky-{w=0.5}{nw}"
            play sound bodyhit
            show ch1ep2_312
            with hpunch
            mc "Mmmmp!"
            k "No, stop, stop, stop!"
            image blklsttwmc2:
                "ch1ep2_313.jpg"
                pause 3.0
                "ch1ep2_314.jpg"
                pause .2
                repeat
            show blklsttwmc2
            with dissolve
            mc "Come on, she should at least know that part about you. We know so little of your past."
            mc "Are you afraid of what she might think of you after she finds out?"
            k "... Thinking back and comparing myself to the old me is embarrassing."
            mc "So you're embarrassed, I get it. But Sky is your daughter. I'm sure she'll be happy to discover that part of you."
            k "Ugh..."
            mc "Well then, how about this?"
            mc "I'll keep it between us, but you need to tell me more. Deal?"
            stop music fadeout 2
            scene ch1ep2_315
            with dissolve
            k "*sighs* Where do I even start?"
            k "... Well, during high school, I was a well-known {i}entity{/i}..."
            k "They used to call me..."
            stop music
            play sound2 ghostlybreath
            show black
            k "The \"Poltergeist of Drealerra\"..."
            play music 'audio/DarkAngel.mp3'
            play sound bodyfall
            show ch1ep2_316
            with hpunch
            ml "Huugh! The... The..."
            ml "You're the Poltergeist of Drealerra! S-stay away from me!"
            scene ch1ep2_317
            with dissolve
            mc "Poltergeist of Drealerra? What exactly did you do in your prime?"
            k "That hurts..."
            mc "I mean, during your younger days...?"
            scene ch1ep2_318
            with dissolve
            ml "I heard you were exorcised from the academy that day! H-have you come back to haunt the students again?!"
            k "I simply graduated like the other students did, Mister Lenon..."
            k "I am not a Poltergeist, a ghost, or a phantom. I'm alive and was nothing but a regular student."
            scene ch1ep2_319
            with dissolve
            k "Mmm... Maybe a student with a bit of a personality disorder..."
            mc "Personality disorder? You seem fine to me."
            scene ch1ep2_320
            with dissolve
            k "[mc], be a good boy and go home for now."
            mc "Nah-uhh! I'm listening to this!"
            k "Please?"
            mc "Hm-mm! No way!"
            k "*sighs*"
            scene ch1ep2_321
            with dissolve
            k "I'm sorry for startling you; it wasn't my intention."
            k "Please, let me help you up."
            play sound chairdrag
            scene ch1ep2_322
            with dissolve
            ml "So... all those rumors surrounding the academy were all a huge misunderstanding?"
            k "Yes, Mister Lenon. However, I can't blame the students as I used to have a creepy presence, if not intimidating."
            k "I even had a lot of enemies and was sent to guidance counseling many times."
            scene ch1ep2_323
            with dissolve
            mc "So you're telling me you used to be a delinquent?!"
            k "*sighs* More or less..."
            mc "But why did they call you the Poltergeist?! What the hell did you do?!"
            scene ch1ep2_324
            with dissolve
            k "You see, I used to stay in an abandoned classroom during breaks. I even slept there when I didn't feel like going home."
            k "There were some cases where students would pass by that classroom, and..."
            play sound woodbreak_reverb
            show ch1ep2_325
            pause
            scene ch1ep2_326
            with dissolve
            st "... I-is s-somebody in there?"
            "..."
            play sound doorknock
            st "H-hello...?"
            play sound doorcreak
            scene ch1ep2_327
            with Dissolve(3.0)
            pause
            play sound scream_female
            st "WAAAAAAAAAAAAH~!!!{w=2.0}{nw}" with hpunch
            play sound bodyfall
            show ch1ep2_328
            with hpunch
            pause
            play sound closedoor
            scene ch1ep2_329
            with dissolve
            pause
            scene ch1ep2_324
            with dissolve
            k "Sometimes, other students did challenges at night, and..."
            play sound radiostatic_long loop
            scene ch1ep2_331
            with dissolve
            st1 "Poltergeist, if you are here, please give us a sign."
            scene ch1ep2_332
            with dissolve
            st2 "P-poltergeist, i-if you are here, please stay away from us..."
            play sound2 cloth2
            show ch1ep2_333
            st1 "*whispers* What are you doing?! We're supposed to be communicating with whoever it is!"
            st2 "I-I think this is a bad idea... Let's go home, please! I'm about to pee my pants...!"
            st1 "Hah! Don't be a wimp! A spirit like this is nothing to me!"
            st1 "Trust me, I've done this a lot befo-{w=0.7}{nw}"
            play sound2 opendoorcreak
            show ch1ep2_334
            pause
            play sound2 woodhit
            show ch1ep2_335
            with hpunch
            st1 "Eeek~!" (multiple=2)
            st2 "Eeek~!" (multiple=2)
            st1 "P-poltergeist, if you have a name..."
            scene ch1ep2_336
            with dissolve
            st1 "Please talk to us using this spirit bo-{w=0.6}{nw}"
            play sound2 doorslam2
            play sound zombiebreathe loop
            show ch1ep2_337
            pause
            scene ch1ep2_338
            with dissolve
            st1 "P-polterge-{w=0.5}{nw}"
            play sound waterphone
            show ch1ep2_339
            pause
            scene ch1ep2_340
            with dissolve
            st2 "Wh-where did it go...?!"
            play sound3 horrorimpact
            show klaracreepwalk
            pause 0.4
            show ch1ep2_341
            with hpunch
            play sound scream_female2
            play sound2 scream_female
            sts "AAAAAAAAAAAAAAAAAAAAHHHHHHHHHHHHH~!!!!!!{w=1.5}{nw}"
            scene ch1ep2_342
            with dissolve
            mc "Creepy..."
            mc "No, you were downright scary..."
            k "It was my personal space, so I had to scare them away."
            mc "How did you survive high school with all that going on?"
            k "It wasn't easy."
            k "I didn't talk. By that, I mean I really didn't. Not even to my teachers."
            mc "What about when they made you read aloud? How on earth..."
            k "Ah, that part was simple..."
            play sound chairdrag
            scene ch1ep2_343
            with dissolve
            tea "Klara Hahn, please read page 146."
            k "..."
            k "...."
            k "....."
            k "......"
            k "......."
            scene ch1ep2_344
            with dissolve
            play sound applause_crowd
            tea "A truly captivating recital that has enraptured everyone present! Kindly take your seat, Miss Hahn, and bask in the admiration."
            stop music
            play sound scratch
            show ch1ep2_345
            pause 1.0
            play music 'audio/InsideTheTent.mp3'
            mc "Someone call an ambulance... I think I'm losing it..."
            k "Huh?"
            mc "So you were a goth girl with a healthy dose of insanity. Okay, I need to take note of that."
            k "[mc], we have business to discuss with Mister Lenon, don't we? This is no time to chit-chat about my past."
            ml "Business?"
            play sound woosh
            show ch1ep2_346
            mc "That's right! We'd like to talk to you about your house, Mister Lenon."
            mc "We have an offer you cannot refuse."
            image klmctaffbklhd:
                "ch1ep2_347.jpg"
                pause 3.0
                "ch1ep2_348.jpg"
                pause .2
                repeat
            show klmctaffbklhd
            with dissolve
            mc "You did great changing the topic."
            mc "So how did Mister Lenon recognize you? I thought the rumors were limited to just the academy?"
            k "Those who had seen me eventually sketched my face."
            k "The rumors were debunked within the academy's immediate vicinity once they confirmed that it was me instead of some kind of spirit haunting the students."
            k "That said, there were still those who strongly believed in supernatural beings."
            k "Among those people was Mister Lenon, a former janitor at the academy."
            k "Despite the debunking, they are still convinced that something is within that classroom."
            k "I know... it's crazy."
            k "But then again, my whole life was crazy up to that point. So, it didn't even bother me."
            mc "Then how did you change? I mean... thinking back and looking at you now..."
            mc "Don't tell me you have a split personality?!"
            k "The one who did everything you just heard about and the person you're talking to now are one and the same."
            k "I haven't changed as we never lose our demons, [mc]. We only learn to live with and resist them."
            mc "Yeah, I kinda knew that. But how did you get from that..."
            mc "... To this?"
            k "As I mentioned, I had a lot of enemies. That was after the debunking happened."
            k "But that's a story for another time. We still have a lot to do, [mc]."
            menu:
                "Yeah, you're right...":
                    $ klararoute = False
                    scene ch1ep2_349
                    with dissolve
                    mc "Yeah, you're right."
                    mc "Why don't you rest? Leave everything else to me."
                    k "Can you manage?"
                    mc "We're almost done, anyway. There isn't much to do aside from the rooms upstairs."
                    k "Great. I can now rest my back before cooking dinner."
                "How about...":
                    $ klararoute = True
                    scene ch1ep2_349
                    with dissolve
                    mc "That sounds fair, but how about this?"
                    k "Hm?"
                    mc "Why don't I take you out tonight?"
                    k "Take me... out? To where exactly?"
                    mc "A dinner date. Just you and me."
                    scene ch1ep2_350
                    with dissolve
                    k "..."
        "Leave her be":
            $ klararoute = False
            yt "Yeah, no way..."
            yt "It's best to leave her alone. She might not be in the mood..."
    stop music fadeout 2

    scene black
    with dissolve
    with fade

    play music 'audio/ThePlan.mp3'
    play sound closedoor
    scene ch1ep2_351
    with dissolve
    e "I'm home..."
    mc "Oh, hey Em. How was it today?"
    scene ch1ep2_352
    with dissolve
    e "*sighs* The same. We still have no lead on Jovian."
    mc "Well, we figured this would be hard since we started from nothing."
    image emmctajobu:
        "ch1ep2_353.jpg"
        pause 3.0
        "ch1ep2_354.jpg"
        pause .2
        repeat
    show emmctajobu
    with dissolve
    e "However, I went with my last resort and shared this case with my colleagues, who happily agreed to investigate."
    e "Aside from that, I also shared it with the First Division's special department."
    e "That gives us more eyes and ears looking for any clues on his whereabouts."
    mc "That's nice and all, but... I didn't know you had that many connections..."
    e "Why the doubting look?"
    mc "Well, knowing you... it would be implausible..."
    e "..."
    e "If there is anything you should never doubt about me, it's my work. I take it seriously, [mc]..."
    e "By the way, where's the rest of the gang?"
    mc "I like that you call it the \"gang\" now."
    mc "Most of them are upstairs refurnishing their rooms. Klara's in the kitchen counting how much tomato sauce she can put in the cabinets."
    e "Tomato... sauce? For?"
    mc "Dunno."
    scene ch1ep2_355
    with dissolve
    e "*whispers* Are you sure we are not eating humans?"
    mc "I mean..."
    play sound step
    scene ch1ep2_356
    with dissolve
    mc "Hey, all done? I was about to go upstairs."
    n "They're makin' the finishing touches on their own, but all rooms are mostly done, includin' yours."
    n "Of course, I kept it simple as ya requested."
    mc "Nice!"
    e "I'm going to check mine."
    n "Why don't I give ya guys a tour of the results?"

    scene black
    with dissolve
    with fadeq

    play sound closedoor
    scene ch1ep2_357
    with dissolve
    n "Here's Aine and Emma's room."
    scene ch1ep2_358
    with dissolve
    a "Hey, guys!"
    a "What do you think? It's not much, but I supervised the changes myself!"
    if aineroute:
        scene ch1ep2_359
        with dissolve
        e "Aren't you staying in [mc]'s room?"
        a "Well, yes. But I decided to keep my PC setup here. So, I'll still be staying here most of the time."
        a "I can't leave my best friend alone, can I?"
        e "Actually, you can..."
    scene ch1ep2_360
    with dissolve
    mc "This part here looks pretty cozy. I like it."
    play sound chair
    scene ch1ep2_361
    with dissolve
    n "Two bean bags for the two lovely ladies."
    n "Extremely comfortable, specially designed for movie marathons. Netflix and chill, maybe? If ya know what I mean..."
    yt "This looks and sounds lewdly familiar..."
    yt "Don't they do this in porn videos? What do they call it again?"
    scene ch1ep2_362
    with dissolve
    mc "Damn, you got your TV, too. Now I'm kinda jealous I can't have one."
    e "Why not?"
    mc "My room is smaller compared to yours. I can't fit a lot of stuff in there."
    scene ch1ep2_363
    with dissolve
    n "Klara tasked me to change every bed to a spring memory foam one, and I think it was a wise choice."
    play sound woosh
    play music 'audio/StepIntoSuccess.mp3'
    show ch1ep2_364
    n "Introducing the ultimate sleep revolution: the Spring Memory Foam Bed!"
    n "Experience unparalleled comfort as ya drift off into dreamland on this marvel of modern bedding technology."
    scene ch1ep2_365
    with dissolve
    n "This Spring Memory Foam Bed combines the best of both worlds: the classic support of a traditional innerspring mattress with the plush contourin' comfort of cutting-edge memory foam technology."
    n "The hybrid design ensures a perfect night's sleep, no matter yer sleeping style."
    scene ch1ep2_366
    with dissolve
    n "Say hooroo to restless nights as the individually-pocketed springs respond to yer body's unique shape and movement, providing targeted support and minimizin' motion transfer."
    n "Meanwhile, the luxurious memory foam layer cradles yer body, relievin' pressure points and ensurin' ya wake up refreshed and pain-free!"
    mc "Okay, oka-{w=0.5}{nw}"
    scene ch1ep2_367
    with dissolve
    n "The Spring Memory Foam Bed also features a breathable, moisture-wicking cover that keeps ya cool and comfortable throughout the night."
    scene ch1ep2_368
    with dissolve
    n "As a bonus, the cover uses copper-infused threads, minimizing odors and unpleasant smells!"
    mc "Wai-{w=0.5}{nw}"
    play sound chair
    show ch1ep2_369
    with hpunch
    n "Plus, these eco-friendly materials and \"CertiGC\"-certified foam ensure that yer sleep space remains healthy and free from harmful chemicals."
    n "Upgrade yer sleep experience with the Spring Memory Foam Bed and wake up each mornin' feelin' revitalized and ready to conquer the day."
    play sound woosh2
    play sound2 applause_crowd
    show ch1ep2_370
    n "Trust, and you'll never look back!"
    e "*clapping*"
    a "Whoa...!"
    mc "I mean... is that it?"
    scene ch1ep2_371
    with dissolve
    n "There's more!"
    mc "No, no, that's-{w=0.5}{nw}"
    play sound woosh2
    show ch1ep2_372
    n "Presentin' the sleek and stylish Wall-Mounted Flat Screen TV, designed to revolutionize yer home entertainment experience and elevate yer interior decor game!"
    n "This Wall-Mounted Flat Screen TV boasts an ultra-thin design and a frameless display, makin' it the perfect centerpiece for any modern livin' space."
    n "With an expansive, high-resolution screen, you'll enjoy crystal-clear images, vibrant colors, and sharp contrasts that bring your favorite movies, shows, and games to life!"
    mc "Phew, that's a lot shorter than-{w=0.5}{nw}"
    show ch1ep2_373
    n "Thanks to the innovative wall-mountin' system, ya can say goodbye to bulky TV stands and tangled cables."
    n "Its easy-to-install mount ensures yer TV will sit flush against the wall, creatin' a seamless, minimalist look that saves space and enhances your home's aesthetic."
    n "Transform yer living room into the ultimate viewin' haven and indulge in the immersive visual adventure ya deserve!"
    play sound2 applause_crowd
    scene ch1ep2_374
    with dissolve
    mc "Now you sound like a TV ad."
    mc "Are you sure you're not running a home improvement business?"
    n "Nay! I'm simply a know-it-all kinda woman."
    n "Should we check Sky's room?"
    scene ch1ep2_375
    with dissolve
    a "You guys go ahead. I'm staying here for now."
    e "Same. I need to change my clothes."
    a "Enjoy the tour, [mc]!"
    
    scene black
    with dissolve
    with fade

    play sound closedoor
    scene ch1ep2_376
    with dissolve
    s "Tadaaa~!"
    mc "Nothing much changed in here. You really aren't nitpicky even with your room."
    s "That's right! I asked Naomi not to change anything except for a few improvements!"
    mc "I see."
    scene ch1ep2_377
    with dissolve
    n "Here, we got the same bed as in the main bedroom."
    scene ch1ep2_378
    with dissolve
    n "I thought Sky's table was a tad too high for her, so I changed it to a proper work table that could accommodate her height."
    scene ch1ep2_379
    with dissolve
    n "Then, we added a few paintings and posters to liven up the room's atmosphere."
    n "I wanted to add more accessories and small furniture, but she refused."
    scene ch1ep2_380
    with dissolve
    s "I'm already fine with just these. Thanks, Naomi!"
    n "No worries!"
    stop music fadeout 4
    play sound opendoor
    scene ch1ep2_381
    with dissolve
    n "On to Gwen's room, then."
    mc "Ladies first."
    n "Cheers, mate."
    s "Wait, I want to see her room too!"
    $ renpy.music.set_volume(0.3, 1.0)
    play music 'audio/InYourArmsAgainInst.mp3'
    scene ch1ep2_382
    with dissolve
    n "*chuckles* She's already testing it out."
    scene ch1ep2_383
    with dissolve
    mc "One of your additions, I assume?"
    n "I'd say it was her personal request."
    $ renpy.music.set_volume(1.0, 1.0)
    play sound opendoor
    scene ch1ep2_384
    with dissolve
    pause
    stop music fadeout 3
    scene ch1ep2_385
    with dissolve
    mc "Gwe-{w=0.4}{nw}"
    play sound cloth2
    show ch1ep2_386
    n "Hold on, I know this song. Let her finish. I want to hear her voice."
    play sound inhale_female
    scene ch1ep2_387
    with dissolve
    pause 1.0
    play music ["<from 14.4 to 192>audio/InYourArmsAgain.mp3"] fadein 0.5
    scene ch1ep2_388
    with Dissolve(1.0)
    g "When the sunlight hits my face, it won't be long...{w=6.5}{nw}" with dissolve
    g "'Til the time I can forget when I felt strong...{w=7.5}{nw}" with dissolve
    g "But until the night I'm in your arms again...{w=7.5}{nw}" with dissolve
    g "I don't wanna get my hopes up in the end...{w=5.5}{nw}" with dissolve
    scene ch1ep2_389
    with dissolve
    g "...{w=4.3}{nw}"
    scene ch1ep2_391
    with dissolve
    mc "All the way I thought that you'd be here with me..." (multiple=2) with dissolve
    g "All the way I thought that you'd be here with me...{w=7.0}{nw}" (multiple=2) with dissolve
    mc "Though I messed up everything I aimed to be..." (multiple=2) with dissolve
    g "Though I messed up everything I aimed to be...{w=6.0}{nw}" (multiple=2) with dissolve
    scene ch1ep2_392
    with dissolve
    mc "On the borderline of something to call sane..." (multiple=2) with dissolve
    g "On the borderline of something to call sane...{w=7.5}{nw}" (multiple=2) with dissolve
    mc "Keep my balance, stand up, forget everything..." (multiple=2) with dissolve
    g "Keep my balance, stand up, forget everything...{w=5.5}{nw}" (multiple=2) with dissolve
    stop music fadeout 1.0
    scene ch1ep2_393
    with dissolve
    pause 0.5
    play sound exhale_female
    g "..."
    yt "Gwen, how did you..."
    play sound applause_crowd
    scene ch1ep2_394
    with dissolve
    g "Hm?"
    play music 'audio/InYourArmsAgainInst.mp3' fadein 4
    scene ch1ep2_395
    with dissolve
    n "She's got an amazing voice. Have ya heard her sing before?"
    mc "Once or twice during high school, but this is the first time I experienced it in its... full majesty."
    mc "And... I know this song..."
    scene ch1ep2_396
    with dissolve
    s "I didn't know you had such a great voice, Gwen...! I wanna cry...!"
    g "There is no reason for you to cry, Sky..."
    scene ch1ep2_397
    with dissolve
    n "Yer voice is very close, if not perfect, compared to the original's. How..."
    g "... Maybe because you guys are looking at the actual artist herself?"
    mc "Yeah..."
    play sound woodhit
    show ch1ep2_398
    s "Whaaaaaaaaaaaat?!"
    scene ch1ep2_399
    with flash
    mc "It's the song... we wrote together for fun back then..."
    mc "Or at least, that's what she told me."
    scene ch1ep2_400
    with flash
    mc "Gwen, when did you..."
    g "For now, that's a topic for only you and me."
    mc "*chuckles* Alright, copy that."
    scene ch1ep2_401
    with dissolve
    s "Y-you're a singer?! How come you didn't tell us that!"
    scene ch1ep2_402
    with dissolve
    n "It's a local acoustic song published years ago. However, the artist remained anonymous 'til today."
    n "So it was ya all along."
    n "Thank you for such a wonderful song. I love it and listen to it all the time."
    n "Now that I met ya, I can say I'm a huge fan."
    s "So am I~! Sing another song, Gwen!"
    scene ch1ep2_403
    with dissolve
    g "Thanks, but it's the only original song I've got."
    g "Since I've published \"In Your Arms Again\", I never got to pursue my artistic side."
    s "But why? You have a singer's voice in you! It's such a waste, really!"
    g "Well... Let's say I have responsibilities."
    scene ch1ep2_404
    with dissolve
    mc "..."
    scene ch1ep2_405
    with dissolve
    mc "*whispers* Change the topic, Naomi."
    play sound woosh
    show ch1ep2_406
    play music 'audio/StepIntoSuccess.mp3'
    n "Do you know what made her voice sound even better?"
    n "Introducing the S.S.S.S.S., aka the SuRhapsody Surround Sound Speaker System!"
    g "That's a whole mouthful..."
    scene ch1ep2_407
    with dissolve
    n "A true masterpiece of audio engineering designed to elevate yer music listening experience to new heights and make every note come alive!"
    n "The SuRhapsody Surround Sound Speaker System has been meticulously crafted to deliver studio-quality sound, capturing the full range of your favourite melodies, from the deepest bass to the highest treble."
    n "Immerse yerself in a concert-like atmosphere as the rich, multi-dimensional audio fills yer space, enveloping ya in a sonic embrace."
    scene ch1ep2_408
    with dissolve
    n "Experience music like never before with the SuRhapsody Surround Sound Speaker System!"
    n "A symphony of sound that will awaken yer senses and redefine yer listening experience."
    n "Yer personal concert hall awaits!"
    scene ch1ep2_409
    with dissolve
    g "Dang... As someone who used to run a company, I'd buy it."
    play sound woosh
    show ch1ep2_410
    n "That's not all!"
    mc "... Okay, maybe that was a bad idea. It'll never end at this point."
    play sound woosh2
    show ch1ep2_411
    n "Let me show ya the DreamSaver™ Ultimate Storable Bed with Spring Memory Foam!"
    scene ch1ep2_412
    with dissolve
    n "Crikey! This is a game-changer for small spaces and fair dinkum sleepin' solutions."
    n "Combining the best of both worlds, this hybrid ripper mattress marries the support of spring mattresses with the comfort of memory foam for a bonza sleep experience."
    n "But wait, there's more! Check out these key features like..."
    play sound doorslam
    show ch1ep2_413
    with hpunch
    pause 0.4
    show ch1ep2_414
    n "The Ingenious Space-Saving Solution and the Advanced Hybrid Design!"
    n "Plus, with our No-Risk Trial and Warranty... give the DreamSaver™ Ultimate Storable Bed a go in yer home with our 100-night, risk-free trial."
    n "Not fully satisfied, mate? No worries! Just send it back for a complete refund, no questions asked."
    play sound chair
    scene ch1ep2_415
    with dissolve
    n "Elevate yer sleep experience and make the most of yer living space with the DreamSaver™ Ultimate Storable Bed with Spring Memory Foam!"
    scene ch1ep2_416
    with dissolve
    g "I was impressed initially, but now, you sound like a Cesa City TV advertisement..."
    mc "Those early morning TV ads?"
    g "Yeah..."
    mc "But hey, at least she knows where she came from..."
    s "Get me this one too~! I want the DreamSaver™ Ultimate Storable Bed too~!"
    n "We should ask Klara first."
    mc "Should we just go and check my room?"
    g "Yeah..."
    play sound opendoor
    scene ch1ep2_417
    with dissolve
    g "Okay, why does your room feel so different now?"
    play sound woodhit
    show ch1ep2_418
    with hpunch
    n "That's because it was made with passion!"
    n "Introducing the Ultimate Whiteboard - yer perfect partner for brainstorming, collaboration, and organization!"
    mc "No, no, no, not that!"
    scene ch1ep2_419
    with dissolve
    n "Then let me introduce the Transformer Workstation!"
    mc "Stop."
    play sound chair2
    scene ch1ep2_420
    with dissolve
    n "Introducing the LuxeComfort ErgoChair!"
    g "No, seriously, stop..."
    play sound woosh
    show ch1ep2_421
    n "Anyway, I made it as simple as I could."
    n "Plus, with the repainting job, it looks much better than before."
    menu:
        "It could use more work":
            mc "Hm, I think it could use a bit more work."
            n "Really?"
            n "I wonder what I missed."
        "It's perfect":
            mc "Yeah, it's perfect, Naomi. You've done a wonderful job these past few days."
            $ naomipoint += 1
            $ renpy.notify(naominotif)
            n "No worries, mate. Ya can entrust these things to me!"

    mc "Although I wonder how much these changes cost Klara..."
    mc "You've done a significant refurbishing and repainting job downstairs too."
    scene ch1ep2_422
    with dissolve
    n "New furniture, new appliances, the repainting, and the overhaul of yer water system."
    n "All in all, it was about..."
    n "Five thousand dollars."
    mc "Oof... Can I refund my entire room, please?"
    g "Yeah, mine too... Five thousand dollars is waaaay too steep even for me!"
    n "Don't worry. She said she should have done this long ago, and it's her responsibility."
    scene ch1ep2_423
    with dissolve
    s "[mc], where's your setup?"
    mc "Oh, I traded it."
    s "Huh? For a laptop?"
    mc "It's still a high-end laptop. I figured I don't need that much hardware and followed our creator's wishes."
    s "Our creator's wishes...?"
    scene ch1ep2_424
    with dissolve
    n "That will be all for this tour."
    scene ch1ep2_425
    with dissolve
    n "If ya guys want any future changes, don't hesitate to call me. Y'all got my digits now."
    g "Sure, will do!"
    menu:
        "Let me walk you out":
            $ naomiroute = True
            mc "Let me walk you out."
            n "Aye! Cheers, mate."
            scene ch1ep2_428
            with dissolve
            g "..."
            scene ch1ep2_429
            with dissolve
            g "Am I the only one feeling the chemistry between those two?"
            s "Hm?"
            stop music fadeout 2

            scene black
            with dissolve
            with fade

            play sound cityalley loop
            play music 'audio/DifLoveInst.mp3'
            scene ch1ep2_430
            with dissolve
            mc "I can't believe how amazing the house looks after the refurbishment. You have such a talent for this."
            n "I wouldn't say it was talent, mate."
            n "But thanks; it was a labour of love, and I'm happy with how it turned out. I'm glad ya like it too."
            image namctahreno:
                "ch1ep2_431.jpg"
                pause 3.0
                "ch1ep2_432.jpg"
                pause .2
                repeat
            show namctahreno
            with dissolve
            n "If I may ask, what's yer favourite part of the new design?"
            mc "That's a tough one..."
            mc "I love what you've done with the bedrooms, but I like the living room the most. It feels warm and inviting now."
            mc "Why ask, though?"
            n "Nothing. I just love hearing that my work is appreciated."
            mc "Well, I'm sure everyone appreciates it. You've outdone yourself, that's for sure."
            n "That's kind of ya to say."
            mc "You should join us for dinner next time."
            n "*chuckles* I'll think about it."
            n "Anyways, I better get goin'."
            n "If my old man is around, I'm sure I'll be gettin' a call from him by now."
            mc "Alright, take care!"
            scene ch1ep2_433
            with dissolve
            n "..."
            scene ch1ep2_434
            with dissolve
            n "About that dinner..."
            mc "Yeah?"
            n "How 'bout ya come and visit me later next week instead?"
            mc "And what does that mean...?"
            n "I know what you're thinkin', but..."
            n "Commitment and adult stuff is the last thing on my list right now, mate. However, come and find out for yerself."
            yt "I'm sure she has the proper intentions..."
            yt "But she's also the type to leave you questioning, huh?"
            mc "Sure, then. Let me know when."
            n "{cps=15}I will..."
            play sound2 cardriveaway
            scene ch1ep2_435
            with dissolve
            yt "God, why do I like the sound of her voice so much? Especially when she's speaking almost under her breath, like just now."
            yt "It tickles me somewhere it shouldn't."
            stop sound fadeout 2
            stop music fadeout 2

            scene black
            with Dissolve(2.0)
            label naomipause3:
            if _in_replay:
                $ name = persistent.gallery_name
            scene naomipause3
            with dissolve
            $ renpy.pause()
            $ renpy.end_replay()
            play sound 'audio/gamepause.mp3'
            show propertysexlogo at move_slide
            with flash
            $ renpy.notify(imageunlock)
            $ renpy.pause()
        "See you later":
            $ naomiroute = False
            mc "See you later, Naomi!"
            n "Catch'ya, mate."
            scene ch1ep2_426
            with dissolve
            g "..."
            scene ch1ep2_427
            with dissolve
            g "If you wanted to get her..."
            g "That was the opportune moment."
            mc "... What?!"
    stop music fadeout 2
    stop sound fadeout 2

    if klararoute:
        scene black
        with dissolve
        with fadeq

        "7 pm..."

        scene black
        with dissolve
        with fadeq

        play sound cityalley loop
        scene ch1ep2_436
        with dissolve
        mc "Ready?"
        k "I'm ready."
        play music 'audio/TuVoz.mp3'
        show klaradatenightshowcase
        with Dissolve(1.0)
        pause 12.5
        show ch1ep2_437
        with dissolve
        mc "Here, for you."
        k "My goodness, you shouldn't have!"
        mc "This is a special occasion, my lady. Even if it was not, a woman like you deserves such treatment."
        k "Are you putting on your gentleman act?"
        mc "There is no such thing as a gentleman act."
        scene ch1ep2_438
        with dissolve
        k "..."
        mc "What's wrong?"
        k "It's been a while since I've been given a gift like this. Do you know that?"
        mc "... You're blushing."
        scene ch1ep2_439
        with dissolve
        k "Am I not allowed to? You're being cheeky again."
        mc "*sniffs*"
        k "What?"
        mc "You're wearing the perfume I bought you a week ago."
        scene ch1ep2_440
        with dissolve
        k "So...?"
        mc "So I think you smell good: dare I say, pleasant, m'lady."
        mc "And you used the word \"So\", which means you're either trying to deny the truth..."
        mc "... Or buy time to make up a lie."
        k "It's the flowers, [mc]."
        mc "No, it's not~!"
        k "*sighs*"
        mc "*chuckles* Shall we?"
        scene ch1ep2_441
        with dissolve
        k "Mm, show me what you've prepared in such a short amount of time."
        stop sound fadeout 2

        scene black
        with dissolve
        with fade

        scene ch1ep2_442
        with dissolve
        k "A gallery?"
        mc "Well, you've always had an affinity for art, so I thought you might like this."
        k "Being thoughtful, are we?"
        mc "Just trying to make you happy."
        mc "Regardless, it's been so long since we spent time together like this."
        mc "Use this opportunity to relax, as a brief escape from all your problems and responsibilities."
        scene ch1ep2_443
        with dissolve
        k "My... I honestly thought I'd never have the chance. Thank you so much, [mc]."
        mc "Anything for my lady."
        scene ch1ep2_444
        with dissolve
        k "One question..."
        mc "Yeah?"
        k "What did you do?"
        mc "What do you mean?"
        k "It's 7 pm. They should be closed at this time."
        mc "Ah... I made some{w} {i}arrangements{/i}."
        scene ch1ep2_445
        with flash
        shu "You want to take Miss Klara to an art gallery? Isn't it a bit late right now?"
        mc "That's what will make it special, don't you think? A private showing for just the two of us."
        scene ch1ep2_446
        with dissolve
        shu "Hm, you got a point there..."
        shu "So you want to make arrangements, I assume?"
        mc "Yeah. Is that something within your sphere of influence?"
        mc "If it's not, don't worry about it. I don't want to abuse your power. I'll think of something else."
        shu "Well, no, it's not... Making an establishment like the International Art Gallery open exclusively for you isn't really about money."
        scene ch1ep2_447
        with dissolve
        shu "Although, worry not! The Omnipotent Shu has just the right person for you!"
        mc "Your dad?"
        shu "Ding, ding~! Bingo~!"
        play sound dialtone loop
        scene ch1ep2_448
        with dissolve
        "..."
        "...."
        "....."
        play sound phoneclick
        scene ch1ep2_449
        with dissolve
        shu "Hey, dad!"
        un "Shu! You called. Is everything good?"
        shu "Yeah, been having fun lately, you know me!"
        un "That's good, that's good!"
        scene ch1ep2_450
        with dissolve
        shu "Say, are you close to Golden City?"
        un "Not just close: I'm actually at Golden City's Meridian branch. Do you want me to meet you?"
        shu "No, but I want you to meet someone you know."
        shu "So come here as soon as you can. You know my current address, yeah?"
        un "Of course! Give me five to ten minutes."
        play sound phoneclick
        scene ch1ep2_451
        with dissolve
        mc "I'm still astounded by how nice your dad is to you."

        scene black
        with dissolve
        with fade

        play sound cardoorclose
        scene ch1ep2_452
        with dissolve
        mc "Hey, Mister Diego! It's been a hot minute!"
        di "Come on, Shu! Are you serious?"
        di "Well if it isn't my boy, [mc]!"
        scene ch1ep2_453
        with dissolve
        di "Damn, look at you!"
        mc "Still keeping the beard, huh?"
        di "Hah! It's flourished into part of my face's natural landscape, [mc]. I would hate to destroy it now."
        scene ch1ep2_454
        with dissolve
        di "So, you two are neighbors. It's reassuring to know my child is in good hands."
        mc "Not really." (multiple=2)
        shu "Not really." (multiple=2)
        di "Haha! Alright, I get it."
        scene ch1ep2_455
        with dissolve
        di "So, what can I do for my favorite young gentlemen?"
        mc "I'd like to know if you could help me make arrangements with the International Art Gallery for tonight."
        di "Ah, yes... that place. It'll take more than some sweet talk to make it work."
        di "But you know me. It's no challenge."
        di "Why do you need it tonight, if I may ask?"
        scene ch1ep2_456
        with flash
        k "My god... The owner of the Meridian hotel chain is Shu's father?"
        k "How did you gain so many connections?"
        mc "*chuckles* The only connection I have is Jess and Shu, really. But being overall a nice guy helped."
        scene ch1ep2_457
        with dissolve
        un "Welcome to the International Art Gallery - Golden City branch."
        scene ch1ep2_458
        with dissolve
        mak "My name is Maki."
        mak "Under Sir Diego's request, I'm in charge of your reservation tonight."
        scene ch1ep2_459
        with dissolve
        yt "God damn, she's tall!"
        scene ch1ep2_460
        with dissolve
        mak "You may feel free to give yourselves a tour."
        mak "However, please refrain from touching anything as some of the works posted here are artifacts dating back to ancient civilizations."
        scene ch1ep2_461
        with dissolve
        mc "Thank you, Maki. We'll make sure to remember that. Sorry for making you work an extra shift tonight, though."
        mak "No worries!"
        mak "If I may be candid, this shift was offered with a good amount of compensation, so it was my pleasure to accept it."
        yt "So money does talk after all. Haha!"
        mak "I'm going to leave you two for now. Please enjoy your night together."
        play sound bodyhit
        show ch1ep2_462
        pause 0.5
        show ch1ep2_463
        mak "Ah!{w=0.9}{nw}"
        play sound cloth2
        show ch1ep2_464
        with hpunch
        mc "Whoa, there! Are you alright?"
        yt "Wait, what the hell? She's... extremely light! I almost can't feel her weight!"
        play sound cloth
        scene ch1ep2_465
        with dissolve
        mak "Aha haa... Yes, thank you."
        mak "I'm so clumsy sometimes that I even trip over my own feet."
        mc "O-okay; be careful, then."
        mak "If you need anything, I'll be at my station."
        scene ch1ep2_466
        with dissolve
        yt "Well, that was eerie..."
        yt "I'm not that ripped to catch someone her size easily..."
        k "..."
        play sound woosh
        show ch1ep2_467
        with hpunch
        mc "Eek!"
        mc "What's with that glare?"
        scene ch1ep2_468
        with dissolve
        k "I'm your date, am I not? Focus on me."
        mc "I couldn't just let her fall."
        k "Yes, you could have..."
        scene ch1ep2_469
        with dissolve
        mc "..."
        play sound waterphone
        play music 'audio/DarkAngel.mp3'
        show klaraknifeglare
        pause
        k "Yes... you could have, right?"
        mc "... Where did you get the knife?"
        k "At home. Brought it for {i}insurance{/i}, just in case..."
        mc "*gulps*"
        mc "N-not for me, right...?"
        k "No, but in case someone takes {b}{i}my{/i}{/b} date away from me, then..."
        k "You know what happens next..."
        mc "G-got it.."
        k "For tonight, you are {b}{i}mine{/i}{/b}, and {b}{i}mine{/i}{/b} alone.{w} Understand?"
        mc "U-understood..."
        play sound woosh
        play music 'audio/TuVoz.mp3'
        hide klaraknifeglare
        show ch1ep2_470
        k "Anyway~! Let's take a look at these first!"
        mc "Phew!"
        scene ch1ep2_471
        with dissolve
        k "Wait..."
        mc "Hm? Found something interesting?"
        scene ch1ep2_472
        with dissolve
        k "[mc], take a look at these!"
        mc "Hmmm..."
        play sound pop
        show ch1ep2_475
        mc "Dead people."
        play sound pop
        show ch1ep2_474
        mc "A dagger."
        play sound pop
        show ch1ep2_473
        mc "Lots of dead people."
        play sound woosh
        show ch1ep2_476
        mc "They resonating with you?"
        k "Yes, but these are more than just people."
        mc "You didn't even hesitate to agree..."
        k "This is your Clan's history, [mc]."
        scene ch1ep2_477
        with dissolve
        mc "You mean those assassins we met at the hideout?"
        k "Mhm, they call themselves \"The Sicae\"."
        k "Considering you don't know what these are, I'm guessing they never mentioned it in your history classes?"
        mc "No, not at all..."
        k "I thought as much. This part of history slowly but surely disappeared from textbooks until it became forgotten by almost everyone."
        scene ch1ep2_475
        with dissolve
        k "This here was Sicae's first rebellion against the government."
        mc "Did they win?"
        k "Yes, initially. However..."
        scene ch1ep2_473
        with dissolve
        k "They underestimated the government's power and..."
        mc "They eventually suffered horrible losses."
        k "That's right."
        scene ch1ep2_478
        with dissolve
        mc "... I'm curious: Are there still others who are... part of Sicae besides those we met back then?"
        k "I'm not sure. I don't know what has happened to them for the past two years."
        k "Only they may know."
        mc "Huh... I'll have to ask if ever I meet one of them again."
        scene ch1ep2_474
        with dissolve
        mc "What about this dagger, though? It looks strange compared to what people are using now."
        k "It's the first dagger ever forged specifically to stab and kill people."
        k "You notice how it's curved out?"
        mc "Yeah?"
        k "The design was intentional: a convex curve causes more damage internally."
        k "Whenever they stabbed a person, they twisted the knife to lacerate any organs near the stabbed area."
        mc "What the f..."
        mc "You sure know a lot about this..."
        scene ch1ep2_479
        with dissolve
        k "Not only that, but the curve also makes it easier to cut a person's neck deeper than what normal knives could."
        mc "Damn... How could they take people's lives so easily like that?"
        play music 'audio/Hallucinations.mp3'
        transform image_klaramuseum_zoom:
            xalign 0.4 yalign 0.1
            zoom 1.0
            linear 60.0 zoom 1.5
        play sound horrorimpact
        show ch1ep2_480 at image_klaramuseum_zoom
        k "There's more to this world than meets the eye, [mc]."
        k "As we speak, there are people suffering a hundred times more than what we've been through."
        k "There are people crying for help, screaming in agony."
        k "There are those who have lost their minds to pain, falling into the abyss of torture each... and every... second."
        k "Yet, no one is around to help those people. They are forever trapped in torment, distress, and misery..."
        play sound lightsoff
        show ch1ep2_481
        pause 1.0
        show ch1ep2_482
        mc "Whoa! What..."
        mak "{size=+10}Attention everyone: we're currently experiencing an unexpected power outage."
        mak "{size=+10}Our reliable backup system will kick in shortly to restore power."
        mak "{size=+10}We appreciate your patience and understanding during this time."
        mc "Damn, now of all times?"
        scene ch1ep2_483
        with dissolve
        mc "Klara, should we-{w=0.5}{nw}"
        play sound2 heartbeatslow loop
        play sound waterphone
        show ch1ep2_484
        pause
        mc "Uhh... Klara?"
        scene ch1ep2_485
        with dissolve
        mc "Klara?"
        scene ch1ep2_486
        with dissolve
        mc "Where the hell did you go?!"
        play sound waterphone2
        show klarapass
        with dissolve
        pause 0.8
        show ch1ep2_487
        mc "Huh!"
        mc "Come on... you don't have to do me like this..."
        play sound cloth2
        show ch1ep2_488
        with hpunch
        mc "Eek!{w=0.8}{nw}"
        stop sound2
        play music 'audio/TuVoz.mp3'
        play sound woosh
        show ch1ep2_489
        k "Got you~!"
        show ch1ep2_490
        mc "Oof!"
        k "Sicae's job is to save those people, [mc]. There's your answer."
        mc "... Was it necessary to make me shit my pants before telling me that?!"
        play sound lightsoff
        scene ch1ep2_491
        with dissolve
        k "Oh, the lights are back!"
        mak "{size=+10}Great news! The power has been successfully restored, and there's no longer a need for the backup system."
        mak "{size=+10}Thank you all for your patience, and we apologize for any inconvenience this may have caused."
        yt "*chuckles* She sure is enjoying this. I can't see any signs of stress on her face now."
        yt "Good job, me!"
        scene ch1ep2_492
        with dissolve
        mc "So if Sicae does as you said, why did you leave your family?"
        k "Simple: I did not want to be part of it."
        k "I left them, they didn't look for me, and now here I am. Sometimes, the greatest decisions don't have to be complicated or dramatic."
        scene black
        with dissolve
        pause 0.3
        scene ch1ep2_493
        with Dissolve(1.0)
        pause
        scene black
        with dissolve
        pause 0.3
        scene ch1ep2_494
        with dissolve
        pause
        scene black
        with dissolve
        pause 0.3
        scene ch1ep2_495
        with dissolve
        pause

        scene black
        with dissolve
        with fade

        scene ch1ep2_496
        with dissolve
        k "Oh, god... My stomach hurts from all that laughing."
        mc "You feeling hungry now?"
        k "Definitely, I'm starving."
        scene ch1ep2_497
        with dissolve
        mc "How about we keep chatting over some food and wine?"
        k "Sounds great! Lead the way!"
        scene ch1ep2_498
        with dissolve
        pause
        stop music fadeout 4
        play music2 'audio/AMiMadre.mp3' loop fadein 4
        scene black
        with dissolve
        pause 0.5
        scene ch1ep2_499
        with Dissolve(2.0)
        pause
        scene ch1ep2_500
        with dissolve
        k "Oh, wow... Did you make some {i}arrangements{/i} for this place, too?"
        mc "Yes, but I actually chipped in a little on the reservation."
        scene ch1ep2_501
        with dissolve
        k "You didn't have to spend that much money just for my sake, [mc]. You know I'm content with even the simplest things."
        mc "Yeah, it wasn't easy on a burger flipper's salary. But who knows when we'll ever get an opportunity like this again?"
        mc "I think that alone is enough justification. So just this once, please accept it."
        scene ch1ep2_502
        with dissolve
        k "You are aiming to impress, aren't you? Surely you are not trying to court me?"
        menu:
            "Raise her curiosity":
                yt "Let me borrow your technique, Naomi."
                mc "Hm? Maybe, I am. What's so wrong with trying to win my lady's heart?"
            "Reassure her":
                yt "Let me borrow your technique, Naomi."
                mc "I can reassure you that my intention is genuine, Klara."
                mc "In any case, what's so wrong with trying to win my lady's heart?"
                $ klarapoint += 1
                $ renpy.notify(klaranotif)

        scene ch1ep2_503
        with dissolve
        k "*chuckles*"
        scene ch1ep2_504
        with dissolve
        pause
        play sound cloth
        scene ch1ep2_505
        with dissolve
        mc "So, did you live a normal life after you left?"
        mc "Based on everything you've told me, I believe your life was anything but."
        k "*giggles* I did, eventually."
        scene ch1ep2_506
        with dissolve
        k "Oh, they have our usuals here."
        mc "Wanna go with them?"
        scene ch1ep2_507
        with dissolve
        mich "Good evening, and welcome to Mana Miller's! My name is Michelle, and I will be your server tonight."
        mich "Are you ready to order, or would you like some recommendations?"
        mc "The usual?"
        k "The usual."
        scene ch1ep2_508
        with dissolve
        mc "Yes, we've made our choices."
        mich "Wonderful! What can I get for you?"
        scene ch1ep2_509
        with dissolve
        k "We'd both like the ribeye steak, please."
        mich "Great choice! How would you like your steaks cooked?"
        k "Medium-rare for both of us."
        mich "Excellent. And would you like any sides with your steaks?"
        scene ch1ep2_508
        with dissolve
        mc "Yes, we'll have the garlic mashed potatoes and the salad, if you have it."
        mich "Of course!"
        mich "Now, how about something to drink? We have a lovely selection of wines to pair with your steaks."
        scene ch1ep2_509
        with dissolve
        k "We've been looking at the wine list, and we'd like to share a bottle of Cabernet Sauvignon."
        mich "A fantastic choice! That wine pairs beautifully with our ribeyes."
        mich "I'll get your order in right away. Is there anything else I can get for you?"
        k "No, that should be everything. Thank you, Michelle."
        mich "You're very welcome. Enjoy your evening, and if you need anything else, please don't hesitate to ask."
        scene ch1ep2_510
        with dissolve
        k "Now, where were we?"
        k "Ah, yes. Things eventually got better."
        scene ch1ep2_511
        with dissolve
        k "However, I had a lot of enemies just because they found my presence unpleasant."
        k "Especially those two girls..."
        stop music2 fadeout 3
        play music 'audio/EmptyStreets.mp3' fadein 3
        scene ch1ep2_512
        with dissolve
        pause
        play sound2 bodyhit
        play sound woodcrash
        show ch1ep2_513
        with hpunch
        pause
        play sound woodcrash
        show ch1ep2_514
        with hpunch
        pause
        play sound fleshstab
        show ch1ep2_515
        with hpunch
        k "Hrnn!"
        mc "Hey, hey, relax!"
        scene ch1ep2_516
        with dissolve
        k "Hmmm?"
        yt "Is it just me? Or does she look tantalizingly gorgeous with a knife in hand?"
        scene ch1ep2_517
        with dissolve
        mc "Did they just let you get away with beating both those girls?"
        mc "Hell, are they even still alive...?"
        k "I was sent to guidance counseling, but they didn't get anything from me."
        k "After that, they sent me to meet with the principal along with our guidance counselor, Miss Parker."
        stop music fadeout 3
        play music2 'audio/AMiMadre.mp3' fadein 3 loop
        scene ch1ep2_518
        with dissolve
        pk "My name is Kai. I believe we've already met during the opening ceremony."
        pk "How are you holding up, Klara?"
        scene ch1ep2_519
        with dissolve
        k "..."
        pk "P-please don't stare at me like that. I mean no harm."
        pk "I'm here to help you, so please talk to me."
        k "..."
        pk "Just one word to explain your behavior will be enough."
        scene ch1ep2_520
        with dissolve
        k "{size=-20}... myself."
        pk "Hm? What was that?"
        k "... I was protecting myself."
        show ch1ep2_521
        pk "Hohohohooo!"
        k "..."
        scene ch1ep2_522
        with dissolve
        pk "Ahem, I mean... Alright, that's the first step."
        pk "We should clap to that, yeah? Good job, Klara!"
        play sound applause_crowd
        scene ch1ep2_523
        with dissolve
        k "*clapping*"
        scene ch1ep2_524
        with dissolve
        pk "Klara, I understand you're going through a difficult time, and we genuinely want to help you."
        pk "Miss Parker informed me about the incident with the two girls. Can you tell me what exactly happened?"
        k "..."
        scene ch1ep2_525
        with dissolve
        mp "Klara, we're not here to judge or blame you. We want to understand the situation better and find ways to support you."
        scene ch1ep2_526
        with dissolve
        pk "We need to know your side of the story. We believe everyone should feel safe and comfortable at school, and that includes you."
        scene ch1ep2_527
        with dissolve
        k "..."
        scene ch1ep2_528
        with dissolve
        k "They... One was saying mean things to me, and one was trying to stab me with a knife. It pissed me off, so I tried to stop them."
        mp "My god..."
        scene ch1ep2_529
        with dissolve
        pk "Thank you for sharing that with us, Klara. I know it takes courage for you to speak up."
        pk "We'll address the situation and make sure those girls understand the consequences of their actions."
        mp "Aside from that, we also want to help you develop healthy ways to cope with your emotions and communicate with others."
        mp "I'd like to invite you to join a support group here at school for students who struggle with social interaction."
        mp "It's a safe space for everyone to share their experiences, learn from one another, and make friends."
        k "... Friends? What does that mean?"
        mp "They are the people who will stay with you. The ones who will love you despite who you are."
        k "... I don't want that. I don't need them."
        scene ch1ep2_530
        with dissolve
        pk "We understand that it might feel overwhelming, but remember that we're here to support you every step of the way."
        pk "You can start by attending just one session and see how you feel afterward."
        mp "And I'll be there with you, Klara. You can even tell me if you don't feel like continuing, and I'll stop the session."
        mp "What do you think?"
        k "..."
        scene ch1ep2_531
        with dissolve
        k "... I'll try."
        scene ch1ep2_532
        with dissolve
        pk "That's all we ask: just give it a try. We believe in you."
        pk "You have the intelligence to catch up with your lessons despite your numerous absences."
        pk "Your advisor also informed me that you have an incredible talent in sketch art."
        pk "All that said, we're confident that you can make positive changes in your life with time and support."
        scene ch1ep2_533
        with dissolve
        mc "Did you attend?"
        k "Not only did I attend, but I found it entertaining, so I stayed."
        k "Eventually, I opened up, and people started to understand me."
        k "There were still those who clearly didn't like me, but it didn't matter at that point. I knew I wasn't alone."
        k "I'm not trying to be ironic here, but it felt like a curse had been lifted from me."
        k "I was still me, but a better version. I got so used to talking with others that I almost forgot who I was before."
        scene ch1ep2_534
        with dissolve
        mc "Haha! Well, it's nice to know this version of you."
        mc "I knew you had a dark side within you, but I never knew your full origin story."
        image klresmctabklpast:
            "ch1ep2_535.jpg"
            pause 3.0
            "ch1ep2_536.jpg"
            pause .2
            repeat
        show klresmctabklpast
        with dissolve
        k "That's all there is to my past. It's nothing to write home about, really."
        mc "What do you mean, \"nothing to write home about\"?"
        mc "You went from that, to this. That makes you unique, and I love every part of it."
        mc "Now, it might sound a bit cringe, but I'll say it anyway."
        mc "Knowing this, I can proudly brag about you."
        mc "\"Hey, this is Klara. I know her, and she's freaking cool!\", stuff like that."
        k "*giggles* It seems you know the exact words to get a woman my age all giddy and happy, [mc]."
        mc "Come on, it wasn't that impressive!"
        k "I've always known this about you: you have the innate ability to positively affect the people around you without realizing it."
        k "And I told you, small things like a simple show of appreciation are enough to make me happy."
        k "No need to go all fancy next time, okay?"
        yt "So she's looking forward to a next time. That's good."
        yt "I wonder how I can pull off something that would impress an experienced lady like her without being too fancy.."
        yt "That'll be a unique challenge, but it does make things interesting."
        yt "Maybe I should approach things the old-fashioned way."
        yt "My job is to support her and ease the weight on her shoulders, and that's exactly what I'm doing."
        mc "*chuckles* Alright, noted."
        stop music2 fadeout 2

        scene black
        with dissolve
        with fade
        
        if klarapoint == 4:
            label klaradrunkshow:
            if _in_replay:
                $ name = persistent.gallery_name
            play music 'audio/TuVozVoice.mp3' fadein 2
            scene ch1ep2_537
            with dissolve
            k "Weeeeeeeeeeeeee~! AHAHAHAHAAA~!"
            mc "You're almost there, you're almost there."
            play sound chair
            scene ch1ep2_538
            with dissolve
            k "*softly chuckles* Thank you, [mc]... I had fun..."
            mc "Indeed. You had fun drinking all that wine and scaring the shit out of me."
            k "Haah! I got you, didn't I?"
            mc "Alright, alright, you did."
            mc "Now, rest. We both still have work tomorrow."
            k "Wait..."
            mc "Hm?"
            k "Can you... remove my stockings, please, [mc]...? I don't think I'll be able to right now."
            mc "Are you sure?"
            k "Just... don't touch anything down there."
            mc "Okay."
            mc "Lift your hips a little bit for me?"
            play sound chair
            scene ch1ep2_539
            with dissolve
            k "Mmhh..."
            play sound cloth
            scene ch1ep2_540
            with Dissolve(1.0)
            yt "Oh... my... god..."
            yt "I mean... where the hell are you looking, [mc]?! Come on, focus on your task!"
            play sound cloth
            scene ch1ep2_541
            with dissolve
            pause
            play sound cloth
            scene ch1ep2_542
            with dissolve
            k "Mhh..."
            yt "Well, shieeeeeeet..."
            k "Remove my top, too..."
            mc "A-alright..."
            play sound chair
            scene ch1ep2_543
            with dissolve
            mc "There. Are you sure you want to sleep like that?"
            k "Yes... All that wine made my body feel so hot..."
            k "Ahah... Sorry you have to see me like this. I can't drink like I used to..."
            scene ch1ep2_544
            with dissolve
            yt "I'm pretty sure she won't remember this tomorrow. But, Jesus..."
            yt "The alcohol seems to be making her forget her limits."
            k "Anyway, that's enough excitement for one night... Off to bed with you..."
            menu:
                "Kiss her goodnight":
                    play sound chair
                    scene ch1ep2_545
                    with dissolve
                    mc "Alright. Goodnight, Klara."
                    scene ch1ep2_546
                    with dissolve
                    k "¡Mmmnn! ¡No... me beses! Huelo como una... vieja apestosa que se baña en alcohol..."
                    mc "... Tu forma de hablar ciertamente se vuelve colorida cuando estás borracha."
                    $ klarapoint += 1
                    $ renpy.notify(klaranotif)
                    mc "*chuckles* {i}That{/i} country sure did stick with us, huh?"
                "Try to cop a feel":
                    yt "Dude, are you crazy?! You must have a death wish!"
                    yt "She might be drunk, but drunk or not, she still has that dark Klara living inside of her."
                    yt "Unless I want my blood to end up in those tomato sauce cans, I better keep my hands to myself!"
            
            scene ch1ep2_547
            with dissolve
            mc "Oh, that's right, the knife."
            mc "Give me the knife. You look like a drunk college girl who passed out on the street and can't remember where her clothes went..."
            scene ch1ep2_548
            with dissolve
            k "Mnnh!"
            mc "You can't even undress yourself right now. How do you expect to sleep safely next to a deadly weapon?"
            scene ch1ep2_549
            with dissolve
            k "Mhh..."
            mc "Where were you even hiding that?"
            scene ch1ep2_550
            with dissolve
            yt "Better take this back to the kitchen, then get some sleep myself."
            $ renpy.end_replay()
        else:
            play music 'audio/TuVozVoice.mp3' fadein 2
            scene ch1ep2_537
            with dissolve
            k "Weeeeeeeeeeeeee~! AHAHAHAHAAA~!"
            mc "You're almost there, you're almost there."
            play sound chair
            scene ch1ep2_538
            with dissolve
            k "*softly chuckles* Thank you, [mc]... I had fun..."
            mc "Indeed. You had fun drinking all that wine and scaring the shit out of me."
            k "Haah! I got you, didn't I?"
            mc "Alright, alright, you did."
            mc "Now, rest. We both still have work tomorrow."
    stop music fadeout 2

    if aineroute:
        scene black
        with dissolve
        with fade

        play sound opendoor
        play music 'audio/Forever.mp3'
        scene ch1ep2_551
        with dissolve
        pause
        scene ch1ep2_552
        with dissolve
        pause
        play sound chair
        scene ch1ep2_553
        with dissolve
        pause
        scene black
        with dissolve
        play sound cloth
        scene ch1ep2_554
        with dissolve
        pause
        scene black
        with dissolve
        play sound cloth
        scene ch1ep2_555
        with dissolve
        pause
    stop music fadeout 2

    call hide_days from _call_hide_days_1
    with dissolve
    scene black
    with dissolve
    with fadeq

    show screen day_friday with dissolve
    "Friday afternoon..."

    scene black
    with dissolve
    with fadeq

    play music 'audio/FuNck.mp3'
    scene ch1ep2_556
    with dissolve
    mc "You guys going somewhere?"
    l "I'm on my way to the academy, as usual. But I think Freya is going somewhere else."
    scene ch1ep2_557
    with dissolve
    f "Yeah, I'm going to the bookstore to grab some school supplies."
    mc "Need some help? Want me to tag along?"
    f "Nah, I got this. There's not much to carry, so you can head home first."
    mc "Alright, then. You two take care."
    scene ch1ep2_557a
    with dissolve
    f "..."
    l "What's wrong, Frey?"
    f "... Have you ever had your heart broken, Lil?"
    l "Huh?"

    scene black
    with dissolve
    with fadeq

    play sound traffic loop
    scene ch1ep2_558
    with dissolve
    yt "Things are surprisingly going smoothly for everyone, considering there were some threats or disturbances a few days ago."
    if moonroute:
        yt "Not only that..."
        yt "I got to know Moon. She only told me parts of her story, but I think hearing it in full detail will be definitely interesting."
        yt "Aside from that, she's amusing to be with, and I can't wait to... {i}explore{/i} more of the Moon's surface... and depths."
    if klararoute:
        yt "I also got to bond with Klara and learn more about her."
        yt "It's weird that she doesn't want Sky to know about her past."
        yt "I will find my chance to tell Sky."
        yt "... But I want to do so in a way that riles Klara a bit without pissing her off."
        yt "... I'm already getting some ideas! This is going to be a challenging but fun tease! Haha!"
    if naomiroute:
        scene ch1ep2_559
        with dissolve
        yt "Naomi is starting to captivate me more as well. She will be of use to us, that's for sure."
        yt "Not only she's good at fixing ye {i}pipes{/i}, but she's {i}handy{/i} in other ways, I'm sure!"
        yt "I wonder what other things she can handle well..."
        yt "... God, do I sound like a creep."
    if aineroute:
        yt "Meanwhile, Aine is starting to get clingier."
        yt "But I'd be a liar if I said that I hate cuddling with her at night."
        yt "I'm getting so used to her presence that I can no longer live without it. She's just so precious, man."
        yt "Wait... Am I the one getting clingy?"
        yt "..."
        yt "Nah, nah, nah! It can't be!"
        yt "... Oh well, I guess that isn't so bad."
    if emmaroute:
        scene ch1ep2_560
        with dissolve
        yt "Emma is starting to get used to her freedom, too."
        yt "I don't know how to describe it exactly, but it's like she now has room to breathe..."
        yt "Fuck, that sounds stupid... What do you mean by room to breathe, idiot?"
        yt "She's always been able to breathe!"
        yt "I guess I mean that she's starting to open up and have more casual conversations with the gang."
        yt "*chuckles* Damn you, Em. Now I'm calling it the gang too."
    if gwenroute:
        yt "Well, everyone except for one."
        yt "Gwen..."
        yt "I never would have guessed it. She is troubled, and I don't feel comfortable not seeing the usual her."
        yt "Hm, I wonder if I can do something about it?"
    stop music
    stop sound
    show ch1ep2_561
    un "Excuse me, young man?"
    show ch1ep2_562
    with hpunch
    mc "Whoa! Where did you come from?!"
    play music 'audio/TimeZones.mp3' fadein 2
    scene ch1ep2_563
    with dissolve
    yt "Hold on... Have I met her before? When did..."
    yt "She seems familiar..."
    scene ch1ep2_562
    with dissolve
    yt "No, no, familiar is an understatement. I feel... like I'm actually close to her?"
    yt "What the hell is this intense feeling in my chest? My heart feels like it's being squeezed..."
    scene ch1ep2_564
    with dissolve
    mc "I mean, sorry. Do you need something?"
    un "May I ask what time it is?"
    scene ch1ep2_565
    with dissolve
    yt "Shades, and, although not exactly built for walking, a cane...{w} Is she blind?"
    scene ch1ep2_566
    with dissolve
    mc "Oh, uhm... I think it's almost quarter to five right now."
    un "Oh no... It's getting late."
    mc "Uhh, are you..."
    un "A person with an eye disability, yes."
    mc "I {i}was{/i} wondering that, but I was going to ask if you were lost."
    scene ch1ep2_567
    with dissolve
    un "Kind of..."
    un "Did you, perhaps, see a woman with brown hair, purple ends? Ponytail?"
    mc "I... don't think I've seen anyone with that hair color here."
    mc "That said, I've been in this area for only a few minutes."
    un "She also has a piercing on her nose..."
    mc "I think I'm starting to picture what she looks like.{w} What's her name?"
    un "Judith."
    mc "Judith..."
    mc "Why don't we wait for her here? She might be looking for you and come back here, just in case."
    un "Mhm, okay."

    scene black
    with dissolve
    with fadeq

    scene ch1ep2_568
    with dissolve
    un "..."
    mc "..."
    yt "Well, this is awkward... I should at least start a conversation."
    scene ch1ep2_569
    with dissolve
    mc "Uhh... You got a name?"
    ee "My name is E."
    scene ch1ep2_570
    with dissolve
    mc "Just E?"
    mc "Like... Adelle?"
    ee "..."
    mc "... Drake?"
    ee "..."
    mc "Eminem..."
    scene ch1ep2_571
    with dissolve
    ee "You have a good sense of humor. Don't mind what others tell you."
    mc "They don't tell me anything, actually..."
    scene ch1ep2_572
    with dissolve
    mc "... Hey, listen. I've got this strange feeling in my chest."
    mc "Have we... met somewhere?"
    ee "Hmm? I don't believe so. However, I do know what you are."
    mc "Huh? {i}What{/i} am I?"
    scene ch1ep2_573
    with dissolve
    ee "Your existence seems entwined with a mysterious phenomenon in this universe."
    ee "You're one of the rare individuals with an uncertain future."
    ee "You're not bound by the same enigmatic cycle that governs others, a cycle whispered to involve four cryptic principles."
    ee "Instead, you have the power to forge your own destiny."
    mc "I... I don't understand."
    play sound cloth
    scene ch1ep2_574
    with dissolve
    ee "I'm a fortune teller. Would you like to know what I see in your future?"
    mc "Based on what you just said, I'm not sure I want to know."
    scene ch1ep2_575
    with dissolve
    ee "All I can see is an immense expanse of white..."
    ee "Does greatness and purity await you?"
    ee "Or perhaps emptiness?"
    scene ch1ep2_576
    with dissolve
    ee "... Or it could be that my eyes are playing tricks on me."
    yt "She's quite peculiar..."
    mc "Enigmatic cycle? Four cryptic principles?"
    mc "What are those even?"
    ee "You'll discover the answers..."
    ee "In due time..."
    scene ch1ep2_577
    with dissolve
    jud "*huff* E!"
    mc "Oh, is that her?"
    ee "Based on the sound of her voice, yes, it is."
    scene ch1ep2_578
    with dissolve
    jud "*huff* Where the hell have you been wandering off to? I've been looking for you for the past five hours!"
    play sound woodhit
    show ch1ep2_579
    with hpunch
    mc "Five hours?!"
    mc "So you were lost for five hours?!"
    ee "I think so..."
    mc "Why didn't you tell me?! We could've..."
    ee "I don't have any means to tell time."
    scene ch1ep2_580
    with dissolve
    mc "*sighs* Right..."
    scene ch1ep2_581
    with dissolve
    jud "She's my patient, and a little exploring is sometimes problematic."
    jud "Thank you for watching her. I hope she didn't give you much trouble."
    mc "No, not at all. I'm on my way home, so it's fine."
    scene ch1ep2_582
    with dissolve
    jud "Shall I return?"
    ee "Yes."
    stop music fadeout 3
    play music2 'audio/RewindTimeINST.mp3' loop fadein 3
    play sound cloth
    scene ch1ep2_583
    with dissolve
    mc "Well then, I'll get going too. Take care, E, Judith."
    scene ch1ep2_584
    with dissolve
    ee "Take care, young man. We are looking forward to seeing you again."
    show ecanereturn
    with Dissolve(0.7)
    pause 4.3
    play sound swordimpact
    show ch1ep2_585
    with hpunch
    pause 1.0
    play sound2 cloth
    play sound swordscrape
    show ch1ep2_586
    ee "Once you've discovered your heading, prepare yourself, and return to the place where it all began for you."
    ee "Find someone named \"7th\"."
    ee "You must remember.{w} We'll be waiting, [mc]."
    play sound ehum
    scene ch1ep2_587
    with Dissolve(2.0)
    mc "!!!" #mc suddenly tearing up/Eternity hum
    play sound traffic loop
    show ch1ep2_588
    with hpunch
    mc "W-wait, no! D-don't go! Please, don't leave us!"
    scene ch1ep2_589
    with Dissolve(1.0)
    mc "Huh? Whose..."
    scene ch1ep2_590
    with dissolve
    mc "Whose memories were those just now...?"
    stop music2 fadeout 2
    stop sound fadeout 2

    if (gwenroute and gwenpoint == 9):
        scene black
        with dissolve
        with fade

        play sound cityalley loop
        scene ch1ep2_591
        with dissolve
        yt "Ugh... I feel dizzy. What the hell just happened?"
        scene ch1ep2_592
        with dissolve
        mc "..."
        yt "Damn, I can't get it over my head! I felt like an idiot in the middle of the road!"
        g "Yeah, I know, I know!" with hpunch
        scene ch1ep2_593
        with dissolve
        mc "Hm?"
        g "But... come on, dad! We haven't seen each other for years. Do I really have to do it now?!"
        scene ch1ep2_594
        with dissolve
        "..."
        g "What do you mean I {i}have{/i} to go?!"
        yt "... This is it! This is the opportunity I was looking for!"
        play sound2 woosh
        show ch1ep2_595
        mc "Hey."
        play sound2 woodhit
        show ch1ep2_596
        with hpunch
        g "What?!"
        scene ch1ep2_597
        with dissolve
        g "Oh, [mc]... I'm sorry, I was talking to Dad."
        play sound2 woosh3
        show ch1ep2_598
        mc "Gimme."
        mc "NOW."
        scene ch1ep2_599
        with dissolve
        pause 0.5
        play sound2 bodyhit
        show ch1ep2_600
        pause 0.1
        show ch1ep2_601
        pause 1.0
        scene ch1ep2_602
        with dissolve
        mc "Glenn, this is [mc]. What's up?"
        gl "Right on time! Here comes my savior."
        gl "It's Emilda's birthday tomorrow. I don't think she'll celebrate it anyway, but I'm telling Gwen to go and visit her at least this once."
        gl "I want Gwen to take this chance to reconcile with her mom, but..."
        scene ch1ep2_603
        with dissolve
        mc "Yeah, I know. She's been troubled by it these past few days."
        mc "You want Gwen to go, okay. Then how about you?"
        gl "Me? Haha! No cha-{w=0.7}{nw}"
        mc "If you want Gwen to go, then you should too."
        mc "I don't want to meddle with your family's issues, but you should give yourselves a chance to talk together."
        gl "*sighs* So much for my savior..."
        mc "It will only be fair for Gwen if you go. And she needs your support, Glenn."
        mc "This issue started with me, so I will come too. I want to talk to her personally."
        scene ch1ep2_604
        with dissolve
        g "Are you serious, [mc]? She might kill you, you know?"
        mc "*chuckles* We'll see if she's religious enough, then."
        scene ch1ep2_605
        with dissolve
        g "Well, if my boys are with me, I'll go."
        mc "Good."
        scene ch1ep2_606
        with dissolve
        mc "So, how about it, Glenn? Only two choices: do or die."
        mc "Do we let the situation stay as it is? Or do we do something about it?"
        mc "It's my day off tomorrow, so I have no problem if we go now. I will even take care of the preparations for her birthday."
        mc "Well, if we survive the first day, that is..."
        gl "[mc], let me just say this now..."
        mc "Yeah?"
        gl "You're already twice the guy I am! You're going to make this old man cry!"
        scene ch1ep2_607
        with dissolve
        mc "What..."
        g "Ignore him when he's like that. You'll get nowhere."
        mc "I-I see..."
        scene ch1ep2_608
        with dissolve
        gl "Alright then, prepare yourselves! I'll pick you up in thirty minutes."
        play sound2 phoneclick
        "*click*"
        scene ch1ep2_609
        with dissolve
        mc "I know you've been taking the lead in our relationship. Now, it's my time to show what I have to offer."
        play sound2 cloth2
        show ch1ep2_610
        mc "Go, go, go! You got this!"
        mc "Or should I say, your mom does?" 
        g "Okay-I'm going, I'm going! Stop pushing me!"
        stop sound fadeout 2

        scene black
        with dissolve
        with fade

        play music 'audio/Forever.mp3'
        play sound2 cityalley loop
        scene ch1ep2_611
        with dissolve
        pause
        scene ch1ep2_612
        with dissolve
        mc "You nervous?"
        g "No; I'm just not sure about the three of us going there, [mc]. I don't like all the \"what if's\" popping up in my brain."
        mc "... Yeah, you're nervous."
        scene ch1ep2_613
        with dissolve
        g "..."
        mc "..."
        play sound cloth2
        show ch1ep2_614
        mc "Come on! It bothers me not seeing you as your usual self, you know?"
        mc "Are you afraid she might judge who you've become?"
        g "*sighs* More or less, yeah..."
        scene ch1ep2_615
        with dissolve
        yt "She's fidgeting: she's {i}really{/i} nervous."
        scene ch1ep2_616
        with dissolve
        mc "Hey, give me your hand."
        g "Hm? Why?"
        mc "Just do it."
        scene ch1ep2_617
        with dissolve
        pause
        play sound slap
        show ch1ep2_618
        with hpunch
        pause 0.5
        play sound woodhit
        show ch1ep2_619
        with hpunch
        g "God, fuuuck! What was that for?!"
        scene ch1ep2_620
        with dissolve
        g "Wait... my hands."
        mc "A quick way to get you back on track. Klara taught me that long ago. Although, you can't perform this technique alone."
        mc "Pretty damn effective, right?"
        g "Yeah... that woke me up, for sure!"
        scene ch1ep2_621
        with dissolve
        mc "Also, I'm pissed at you."
        g "Wait, what did I do?!"
        mc "You didn't tell me what was happening until Aine told me about your mom's birthday."
        mc "Didn't you say we should talk to each other when we have problems? Especially if it concerns one or both of us?"
        mc "I know I'm not your boyfriend yet, and your mom may be a special case, but still, we should share this with each other."
        play sound woosh
        show ch1ep2_622
        mc "Hmp!"
        play sound woosh
        show ch1ep2_623
        mc "Hmp!"
        play sound woodhit
        show ch1ep2_624
        with hpunch
        g "Argh! Playing the damsel doesn't suit your character!"
        mc "Ow, ow, ow! Okay, alright, I give up!"
        play sound cloth2
        show ch1ep2_625
        with hpunch
        pause
        scene ch1ep2_626
        with dissolve
        g "I'm sorry, okay?"
        mc "Shit... I've missed that. Should we tell Glenn we need an extra thirty minutes?"
        g "Haha! No, we can't travel to mom's once it gets dark."
        play sound cloth
        scene ch1ep2_627
        with dissolve
        mc "Huh? Why is that?"
        g "First, it takes more than an hour to get from here to her place."
        g "Second, we'll be passing through a dangerous area before we can access the main road to reach our destination."
        mc "Dangerous area?"
        g "Dad knows more about that place than I do, but you'll see."
        scene ch1ep2_628
        with dissolve
        mc "In any case, I know you're not the most emotionally expressive person."
        mc "You have never shown much emotion towards me, for instance."
        mc "You've always been the type to shrug things off and carry on."
        mc "But, Gwen... Promise me that you'll open up to me from now on."
        mc "Tell me whatever it is that's bothering you. It pains me to see you suffering, no matter how little it seems to you."
        mc "It's just... not like you."
        play sound cloth
        scene ch1ep2_629
        with dissolve
        g "Alright, I promise. I'm sorry for making you worry."
        g "And thank you. You're simply the best man a girl could ask for."
        play sound cloth2
        show ch1ep2_630
        mc "*chuckles* That's my girl."
        scene ch1ep2_631
        with dissolve
        g "Aw, shit...!"
        scene ch1ep2_632
        with dissolve
        g "Maybe I should tell dad we need extra thirty minutes after a-{w=2.0}{nw}"
        stop music
        play sound jesscarroar
        show ch1ep2_633
        pause
        play sound3 cardoorclose
        show ch1ep2_634
        gl "Ey, lovebirds!"
        play music 'audio/SorryMyBad.mp3'
        scene ch1ep2_635
        with dissolve
        gl "Oh... did I interrupt something?"
        g "Yes, you did."
        scene ch1ep2_636
        with dissolve
        mc "*shaking his head*"
        scene ch1ep2_637
        with dissolve
        gl "Wait, kids, what did I do?!"
        stop sound2
        play sound cardoorclose
        scene ch1ep2_638
        with dissolve
        gl "Come on, tell me. What did I do?"
        g "Just get us there, dad."
        show ch1ep2_639
        gl "But you're pissed!"
        show ch1ep2_640
        mc "She does sound pissed."
        show ch1ep2_641
        g "Let me drive, then. Scoot over."
        gl "No can do. This is my ride. Why don't you ask Johnny to get yours?"
        play sound chair
        show ch1ep2_642
        with hpunch
        g "Because why would you arrive when we were just getting to the juicy part?!"
        gl "Oh... my bad..."
        scene ch1ep2_639
        with dissolve
        gl "Anywho, are you ready?"
        scene ch1ep2_643
        with dissolve
        g "Well, whatever happens, I have you boys anyway. I've got nothing to lose."
        mc "Now {i}that's{/i} the Gwen I know."
        scene ch1ep2_644
        with dissolve
        gl "..."
        scene ch1ep2_645
        with dissolve
        gl "Don't squirt on my floor, both of you. Just had the car washed."
        scene ch1ep2_646
        with dissolve
        g "Ahahahahaaa!"
        mc "What do you mean?"
        stop music fadeout 2

        scene black
        with dissolve
        with fade

        play sound carmoving loop
        scene ch1ep2_647
        with dissolve
        pause
        scene ch1ep2_648
        with dissolve
        mc "Is this the place?"
        g "Yep!"
        gl "Did Gwen mention this area to you?"
        mc "Yeah, she said we can't go through here when it gets dark."
        stop sound fadeout 2
        play sound2 cardriveinterior loop fadein 2
        scene ch1ep2_649
        with dissolve
        gl "It's not that we can't, but more like we shouldn't. People try to avoid this place at night."
        mc "May I ask why? What kind of danger happens here?"
        stop sound2 fadeout 2
        play sound carmoving loop
        scene ch1ep2_650
        with dissolve
        gl "Kidnappers, carjackers, holdups, and even occasional rape cases."
        gl "Seems like a lush and peaceful place at first sight, right?"
        mc "Yeah... I feel like I could picnic here and would have no problems at all."
        gl "Exactly, and that's the deceiving part."
        gl "We could take the main road all the way to the freeway, but that would take us five hours to get to Emilda's place."
        gl "And we don't want that as Emilda hates nighttime visitors."
        mc "Even family?"
        g "Yeah, it doesn't matter."
        g "She's a woman who has strict rules, and you need to follow them no matter who you are."
        g "As dad and I are both extremely laid-back people, we are among her most despised enemies."
        g "Especially me, given who I am now."
        stop sound fadeout 2
        play sound2 cardriveinterior loop fadein 2
        scene ch1ep2_651
        with dissolve
        mc "That clears some things up for me but raises more questions. How did you two even end up together?"
        gl "Shit happens ahahaha!"
        gl "Well, I can't remember the last time we saw each other. Maybe she doesn't even remember me."
        scene ch1ep2_652
        with dissolve
        g "Oh, I don't think she'd forget so easily..."
        gl "Is there... something I should know?"
        g "Wait, I know something about mom that you don't?"
        gl "I'd be happy to hear what it is, Gwen. Unexpected things like that make me nervous when it comes to your mom."
        g "You'll see, or maybe you won't. She never told anyone about it anyway."
        g "I only discovered it by accident, and I don't think she'll like it if I tell you."
        gl "Not even one hint?"
        g "You're her husband. Why don't you ask her when we get there?"
        scene ch1ep2_653
        with dissolve
        gl "Ex. Ex-husband."
        gl "I'd be surprised if she even looks twice in my direction."
        g "*chuckles* I figured you'd say that."
        stop sound2 fadeout 2

        scene black
        with dissolve
        with fade

        scene ch1ep2_654
        with dissolve
        pause
        play music 'audio/InYourArmsAgainInst.mp3' fadein 2
        scene ch1ep2_655
        with flash
        mc "Whoa, whoa, whoa..."
        mc "You're doing your assignments now? Is it because the final exam is coming, or did you get a concussion that changed your personality?"
        mc "Are you sick? What did you eat?"
        g "No, I'm writing a song."
        scene ch1ep2_656
        with dissolve
        mc "A... song? The heck?"
        scene ch1ep2_657
        with flash
        gl "Did he finally hear it?"
        g "..."
        scene ch1ep2_658
        with dissolve
        g "It took me some time to sing again, but I did. He did hear me sing it, much to my surprise."
        gl "What did he say?"
        scene ch1ep2_659
        with dissolve
        pause
        g "He was speechless, at the time... just enjoyed every part of it..."
        scene ch1ep2_660
        with dissolve
        gl "I'd expect nothing less from him."
        gl "[mc] is a rare man, Gwen. Not everyone can muster the courage to do something like this."
        gl "Even I must admit: if I were in his place, I wouldn't have had the mental and emotional strength to even think about Emilda, let alone suggest to talk with her."
        scene ch1ep2_661
        with dissolve
        g "I know..."
        g "I may not have been the first to know him considering his past interactions with Aine and Emma..."
        g "But I know that I'm the only one who knows who he truly is in his heart of hearts."
        scene ch1ep2_662
        with dissolve
        g "I love him, dad. I love him so much."
        gl "That's why you left."
        g "It may have been stupid of me, but I will never regret that decision..."
        g "It was worth it... so that I could meet him again..."
        g "Although, I don't have to tell him right now."
        g "I'm afraid, dad..."
        gl "Of what?"
        g "I'm afraid I might get my heart torn apart again." with Dissolve(1.0)
        scene ch1ep2_663
        with dissolve
        gl "..."
        scene ch1ep2_664
        with dissolve
        gl "My daughter, who I know better than anybody..."
        gl "The one who's always unapologetically bold and level-headed... I've never seen you act this way."
        scene ch1ep2_662
        with dissolve
        g "*chuckles* He's the only one who ever did, and he's the only one who ever could."
        g "It may have started with lust, but I fell for him hard, dad..."
        g "Harder than I ever expected myself to."
        scene ch1ep2_665
        with dissolve
        g "I mean, look at him."
        g "He's clearly tired from all the weight on his shoulders, and yet... he's still trying to be the bridge for our family."
        g "I don't care about what others think anymore. As long as I have him, I will never ask for more..."
        gl "Ah, youth..."
        stop music fadeout 2
        scene ch1ep2_666
        with dissolve
        gl "Wake him up, though. We're here."
        g "Wait, how long have we been here?"
        gl "About five minutes now."
        g "Shit, shit, shit!"
        scene ch1ep2_667
        with dissolve
        g "[mc]?"
        mc "Hmm?"
        g "[mc], wake up! We're here!"
        scene ch1ep2_668
        with dissolve
        mc "Oh, damn. Sorry, I dozed off."
        mc "... But I could get used to waking up to sights like this one."
        g "Don't tempt me, [mc]... we have to go meet the witch."
        gl "And I'm sure you'll need that rest for what will happen next."
        scene black
        with dissolve
        play sound parkwind loop
        scene ch1ep2_669
        with dissolve
        mc "This place is pretty... how should I say this..."
        scene ch1ep2_670
        with dissolve
        mc "Grandiose?"
        g "It fits dad's tastes more, to be honest."
        gl "I built it myself after our marriage. I see she hasn't changed much."
        play sound2 woodhit
        show ch1ep2_671
        with hpunch
        un "I HATE HER!"
        play sound2 woosh
        show ch1ep2_672
        gl "Yep, we're definitely at the right place..."
        scene ch1ep2_673
        with dissolve
        mc "Who was that?"
        g "Knowing her? Probably one of her reading buddies."
        play sound2 glasshit
        show ch1ep2_674
        emi "Hey, you can't just turn your back on me like that, dear!"
        scene ch1ep2_675
        with dissolve
        gl "..."
        play music 'audio/BringInTheClowns.mp3'
        play sound2 woosh
        show ch1ep2_676
        emi "Oh."
        show ch1ep2_677
        gl "You see? One word from her becomes a knife in your heart, stopping you dead!"
        mc "Oh, no, no... she can't..."
        play sound2 woosh
        show ch1ep2_678
        gl "She can absolutely do that!"
        play sound2 woosh2
        show ch1ep2_679
        emi "And I can also track the whereabouts of my bible!"
        gl "I wasn't the one who misplaced your damn bible! It was you!"
        show ch1ep2_680
        emi "I told you to put it in the travel case!"
        gl "What do you think I did?!"
        emi "You left it somewhere else! Why do you think I couldn't find it?"
        gl "I placed it exactly as instructed!"
        emi "No, you didn't!"
        play sound2 woosh
        show ch1ep2_681
        emi "You also...!"
        gl "What?!"
        emi "You also insisted on..."
        emi "... On buying that stupid book with the supposed secrets of architecture!"
        show ch1ep2_682
        gl "I didn't insist! I asked if you wanted to buy it!"
        emi "I wasn't interested!"
        g "Mom?"
        gl "That's why I asked you!"
        emi "I said no, yet you still bought it!"
        g "Dad?"
        gl "Because I wanted to read it!"
        emi "Then why bother asking me?!"
        show ch1ep2_683
        with hpunch
        g "MOM, DAD!!"
        scene ch1ep2_684
        with dissolve
        gl "..." (multiple=2)
        emi "..." (multiple=2)
        g "Can we... not start with this?"
        g "Please?"
        scene ch1ep2_685
        with dissolve
        gl "Whatever, Emilda."
        gl "Is my room clean?!"
        emi "Use your eyes, not your mouth!"
        scene ch1ep2_686
        with dissolve
        emi "..."
        emi "...."
        show ch1ep2_687
        emi "Ooohh..."
        play sound2 cloth2
        show ch1ep2_688
        with hpunch
        mc "Woah!"
        g "And... there you go..."
        emi "W-water... Get me some water..."
        scene ch1ep2_689
        with dissolve
        mc "Gwen, help me drag her to the lounge."
        g "Sure..."
        stop sound fadeout 2
        stop music fadeout 2

        scene black
        with dissolve
        with fade
         
        play sound parkwind loop
        play music 'audio/Foxear.mp3'
        scene ch1ep2_690
        with dissolve
        yt "Now that I got a good look at them both, Gwen is certainly the spitting image of Emilda."
        mc "Is it what I think it is?"
        g "It's exactly what you think it is."
        mc "So Glenn doesn't know about this?"
        g "No. Her pride is more important to her, after all."
        g "Isn't that right, mom?"
        scene ch1ep2_691
        with dissolve
        emi "You shouldn't have come here."
        g "I didn't want to."
        scene ch1ep2_692
        with dissolve
        g "You cast me away like a stray animal instead of your daughter. I don't have one damn reason to see you."
        g "But dad and [mc] here insisted that I should come, so we could have a chance to talk as a family."
        g "And then the first thing you did was pick a fight?"
        g "How long has it been since dad and I left? I can't even remember anymore."
        g "Get a fucking grip and move on."
        scene ch1ep2_693
        with dissolve
        emi "I was hoping you'd be more mature and respectful the next time I saw you, but clearly, that was wishful thinking."
        emi "You run your mouth even more now."
        scene ch1ep2_694
        with dissolve
        emi "It is because of this insolent, uncultured... boy, I assume?"
        menu:
            with dissolve
            "Try to answer Emilda":
                $ reconcilestep1 = False
                $ gwenroute = False
                scene ch1ep2_697
                with dissolve
                mc "Emilda, if I may-{w=0.5}{nw}"
                play sound2 chair
                show ch1ep2_698
                with hpunch
                emi "{b}You{/b} shut your mouth!"
                emi "You are the sole reason why this family was destroyed, and now you have the guts to show up here?!"
                emi "Who do you think you are?!"
                mc "Uhm... I thought if only we could talk somehow..."
                play sound2 cloth2
                show ch1ep2_699
                g "No, fuck this, [mc]! This will never work!"
                g "We're leaving. Now!"
                scene ch1ep2_700
                with dissolve
                yt "Ugh, shit! I should have waited for a better chance to jump in."
                yt "Now I just made everything worse!"
                stop music fadeout 2
                jump gwenfamilyreconcileend
            "Don't meddle with them":
                $ reconcilestep1 = True
                play sound2 woodhit
                show ch1ep2_695
                with hpunch
                pause
                scene ch1ep2_696
                with dissolve
                g "Call [mc] that again and I will fucking {b}kill{/b} you... Just try it, I hope the fuck you do..."
                yt "I wanna marry her right now..."
                g "Don't even think about telling us to leave, since dad still owns this house..."
                g "Be glad that he still has some compassion left for you because if anything, you're the one who should have left..."

        scene ch1ep2_701
        with dissolve
        emi "Right, {i}I{/i} should have been the one who left after trying my best for what we once called {i}our family{/i}."
        emi "{i}I{/i} should have been the one who left for trying to make you a proper woman."
        show ch1ep2_702
        g "*scoffs* Proper woman."
        g "Shut up and maybe kill that attitude until at least tomorrow."
        g "Despite all your bullshit, we're sincerely trying to give you a proper birthday here."
        scene ch1ep2_703
        with dissolve
        emi "!!!"
        scene ch1ep2_704
        with dissolve
        yt "That's a genuine reaction! Could it be that she didn't know it was her birthday tomorrow?!"
        scene ch1ep2_705
        with dissolve
        g "Let's get out of here, [mc]."
        yt "This feels like I'm choosing the right wires to cut in a ticking time bomb."
        yt "I should approach this delicate situation carefully."
        yt "For now, let's observe and ask for clues on what I can do."
        yt "I need to get a chance to talk to Emilda somehow, but now is not the right time. I'll let them cool off first."
        stop sound fadeout 2

        scene black
        with dissolve
        with fadeq

        play sound chair
        show ch1ep2_706
        with hpunch
        g "Ugh... I'm exhausted."
        play sound closedoor
        scene ch1ep2_707
        with dissolve
        mc "It took that much to face her, huh?"
        play sound cloth
        scene ch1ep2_708
        with dissolve
        g "I doubt this will work, [mc]. You saw what always happens when we see each other."
        g "For a moment, everything starts with the expected big fight."
        g "But as the conversation continues, things return to how they used to be: just sparring with words."
        g "Or at least that's how things have been after our family went into disarray."
        mc "..."
        scene ch1ep2_709
        with dissolve
        mc "I'm wondering..."
        scene ch1ep2_710
        with dissolve
        mc "Does she have anything she likes?"
        g "Like material things, or...?"
        mc "Anything."
        scene ch1ep2_711
        with dissolve
        g "Hm, well... I can name a few."
        stop music fadeout 2

        scene black
        with dissolve
        with fadeq

        "7 pm..."

        scene black
        with dissolve
        with fadeq

        scene ch1ep2_712
        with dissolve
        yt "It's seven, and yet no one's in the kitchen or even downstairs."
        yt "This family is in complete shambles."
        scene ch1ep2_713
        with dissolve
        yt "Still, I'll proceed as planned and wait till she gets here."
        scene ch1ep2_714
        with flash
        play music 'audio/TheSpy.mp3'
        g "She used to be the main cook for the family, but she liked it when dad served her food, especially when it was specifically cooked for her."
        mc "Uh-huh..."
        g "Be careful, though. She has quite a taste for gourmet food."
        g "She used to critique dad's food all the time, and that's how he eventually got good at cooking."
        scene ch1ep2_715
        with dissolve
        g "Just take note..."
        g "Whatever you're gonna do, be yourself, and don't let her intimidate you."
        g "She can sense fear and uses that to her advantage, be it a normal conversation or argument."
        g "That said, you're neither my dad nor me, so still show her respect as much as you can."
        g "Lastly, don't mention our relationship: she'll hate that."
        g "If she wants to talk about it, let her initiate the conversation."
        play sound2 cookingpotboil fadein 2 loop
        scene ch1ep2_716
        with flash
        yt "I may flip burgers daily, but I know my fine dining."
        scene ch1ep2_717
        with dissolve
        pause 0.5
        play sound sizzling
        scene ch1ep2_718
        with dissolve
        yt "So get your ass down here, Emilda!"
        stop sound2 fadeout 2
        stop sound fadeout 4
        scene ch1ep2_719
        with dissolve
        emi "*sniffs*"
        scene ch1ep2_720
        with dissolve
        emi "Who's..."
        emi "Oh my god, is that Glenn?"
        play sound3 woosh
        show ch1ep2_721
        emi "Hmm..."
        show ch1ep2_722
        emi "Oh."
        scene ch1ep2_723
        with dissolve
        yt "That \"Oh\" does hurt. I feel you now, Glenn. I feel you."
        scene ch1ep2_722
        with dissolve
        yt "But the smell brought her down here. That's a good start."
        yt "Now, to finish plating this."
        scene ch1ep2_724
        with dissolve
        emi "So it's just Gwen's boyfriend."
        menu:
            with dissolve
            "Good evening...":
                $ reconcilestep2 = True
                scene ch1ep2_725
                with dissolve
                mc "Good evening, Emilda."
                mc "Are we perhaps expecting anyone to be down here at this time?"
                emi "..."
                emi "No. And that's \"ma'am\" to you."
                emi "I don't recall giving you permission to use my kitchen, young man."
            "We are not a couple yet...":
                $ reconcilestep2 = False
                scene ch1ep2_725
                with dissolve
                mc "*chuckles* Gwen and I aren't a couple yet, Emilda. But we are getting there."
                emi "Hmp, that's \"ma'am\" to you, fornicator."
                emi "And I don't recall giving you permission to use my kitchen."
        
        scene ch1ep2_726
        with dissolve
        emi "I can't believe you would just go ahead and use my belongings without asking. We're nowhere near close, and your parents should have taught you better."
        emi "If not for Gwen, you would have been long gone by now."
        yt "I know Gwen told me she'd kill me, but I don't think she's that intimidating."
        yt "Perhaps she's holding back because of what Gwen told her earlier? Or is it something else?"
        yt "Now that is interesting."
        yt "Sorry, Gwen. But if I have to be myself, I'll do this my way."
        scene ch1ep2_725
        with dissolve
        mc "You're right, ma'am. I shouldn't be here, so I have a proposal."
        scene ch1ep2_726
        with dissolve
        emi "Whatever; I'm not interested in talking to you."
        emi "You are the one who-{w=0.5}{nw}"
        play sound platedown
        show ch1ep2_727
        mc "Are you sure about that?"
        scene ch1ep2_728
        with dissolve
        emi "*gulps*"
        yt "Come on, sit down. You can't resist the delectable, mouthwatering aroma, can you?"
        scene ch1ep2_729
        with dissolve
        gl "*whispers* Shit, that smells so damn good! Did you know he can cook like that?"
        gl "*whispers* Even the plating looks elegant and inviting!"
        scene ch1ep2_730
        with dissolve
        g "*whispers* I knew he could cook, and he does taste good, but not like that!"
        gl "*whispers* \"He tastes good\"...?"
        scene ch1ep2_731
        with Dissolve(0.2)
        g "*whispers* Fuck~! I'm getting wet!"
        gl "*whispers* Oh, stop..."
        scene ch1ep2_732
        with Dissolve(0.2)
        emi "... What is it that you propose?"
        mc "It's simple."
        mc "I know you despise me as I'm the one who destroyed your family."
        mc "So if you don't like my food, I'll stay away from you and your family for good: even Gwen."
        g "*whispers* He's confident."
        gl "*whispers* Recklessly so."
        show ch1ep2_732
        emi "Hmp. And if I do?"
        mc "First, we'll talk."
        mc "And second, you'll let me call you by your name."
        emi "You're underestimating me, are you not?"
        mc "*chuckles* I'm not the type to underestimate anybody, ma'am."
        scene ch1ep2_734
        with dissolve
        emi "..."
        scene ch1ep2_735
        with dissolve
        emi "Alright, you've got yourself a deal, young man."
        menu:
            with dissolve
            "Let her sit down on her own":
                $ reconcilestep3 = False
                play sound platedown
                scene ch1ep2_739
                with dissolve
                mc "I hope you enjoy our offering tonight."
            "Offer her a seat":
                $ reconcilestep3 = True
                play sound woosh
                show ch1ep2_736
                mc "Excellent!"
                mc "Welcome to [mc]'s popup restaurant, exclusively open for our one and lovely guest."
                mc "We have a charming table ready for you, Madam."
                mc "Please, allow me to guide you to your seat."
                play sound cloth
                scene ch1ep2_737
                with dissolve
                emi "..."
                emi "At least you know how to act like a gentleman. I'll assume this is how you enchanted my daughter."
                scene ch1ep2_738
                with dissolve
                gl "*whispers* He's killing it!"
                g "*whispers* Absolutely. But did mom just call me her daughter?"
                play sound platedown
                scene ch1ep2_739
                with dissolve
                mc "I hope you enjoy our offering tonight."

        emi "... What do we have here?"
        yt "Alright, let's go Naomi mode."
        scene ch1ep2_740
        with dissolve
        mc "I'm delighted to present our signature dish:{w} the Confit Potato and Gourmet Burger Patty with our exquisite yellow sauce."
        mc "We begin by slow-cooking the potatoes in a luxurious duck fat confit, allowing them to absorb the rich flavors and achieve an unparalleled tenderness."
        scene ch1ep2_741
        with dissolve
        mc "Atop the confit potato, you'll find our gourmet burger patty, crafted from prime cuts of beef and seasoned to perfection with our secret blend of herbs and spices."
        mc "This succulent patty is then seared to a beautiful medium-rare, ensuring a tender and juicy bite."
        scene ch1ep2_742
        with dissolve
        mc "The crowning glory of this dish is our unique yellow sauce."
        mc "It combines the tangy notes of Dijon mustard with the velvety smoothness of hollandaise, infused with a hint of saffron for a subtle, earthy undertone."
        mc "This delectable sauce brings the dish together, creating a harmonious blend of flavors that will delight your palate."
        mc "We recommend savoring each bite, taking in the symphony of flavors and textures."
        scene ch1ep2_743
        with dissolve
        mc "To complement the rich flavors and textures of our Confit Potato and Gourmet Burger Patty with yellow sauce..."
        mc "I would highly recommend our elegant and full-bodied Red Wine."
        mc "This wine boasts notes of dark fruits, such as blackcurrant and black cherry, along with subtle hints of cedar and vanilla from oak barrel aging."
        mc "The wine's firm tannins and balanced acidity will beautifully cut through the dish's richness, creating a harmonious and delightful pairing."
        mc "{cps=20}Bon appétit!"
        scene ch1ep2_744
        with dissolve
        emi "Hm, you know your ingredients. But how about the taste?"
        scene ch1ep2_745
        with dissolve
        emi "..."
        play sound utensilsonplate
        scene ch1ep2_746
        with dissolve
        pause
        scene ch1ep2_747
        with dissolve
        emi "*exhales deeply*"
        yt "Just an exhale?! Give me more, damn it!"
        scene ch1ep2_748
        with dissolve
        emi "After taking a bite, I can appreciate the creativity and effort put into this."
        emi "The potatoes are tender, and the burger patty is well-seasoned."
        yt "Nice!"
        emi "However, the yellow sauce, while interesting, could use a bit more balance."
        emi "The tanginess slightly overpowers the other flavors in the dish."
        emi "Perhaps more creaminess or a hint of sweetness would round out the sauce and harmonize the dish entire."
        yt "Shit! I should've spent more time with the sauce!"
        scene ch1ep2_749
        with dissolve
        emi "You were surely underestimating me. I am not someone who is impressed by anybody so easily."
        mc "..."
        if (reconcilestep2 and reconcilestep3):
            emi "Don't get too disheartened about it. You are not a chef."
            emi "I was only criticizing your food..."
            scene ch1ep2_750
            with dissolve
            emi "I didn't say I didn't like it... [mc]."
            scene ch1ep2_751
            with dissolve
            yt "Whoa, did I just get a smile from her? She even called me by my name!"
            scene ch1ep2_752
            with dissolve
            gl "That's our cue. Let's leave them alone for now."
            g "You don't want to hear what they're going to talk about?"
            gl "I want to know, but this is their time, not ours."
            g "If you say so."
            scene ch1ep2_753
            with dissolve
            emi "Now, a deal is a deal. I will at least listen to what you have to say."
            scene ch1ep2_754
            with dissolve
            mc "Thanks, Emilda. And I'm glad you liked what I prepared for you."
            emi "You're lucky I'm in a generous mood right now, young man. I just finished my daily Bible reading before coming down here."
            yt "Hey, she's not unreasonable at all. She may have a proper rationale for everything she's done."
            stop music fadeout 2
            jump gwenfamilyreconcilecontinue
        else:
            $ gwenroute = False
            emi "I will let you sleep here tonight. I'm not so evil as to let you go through the dangerous roads in this area in the dark."
            emi "However, I want you to leave first thing tomorrow."
            emi "Lastly, as part of our deal, leave Gwen and my family alone."
            scene ch1ep2_755
            with dissolve
            gl "*sighs*"
            g "We tried, dad. I knew this wouldn't work in the first place."
            gl "What about you and [mc] now?"
            g "..."
            scene ch1ep2_756
            with dissolve
            g "I guess we'll see..."
            stop music fadeout 2
            jump gwenfamilyreconcileend

        label gwenfamilyreconcilecontinue:
        
        scene black
        with dissolve
        with fade

        play music 'audio/Foxear.mp3'
        scene ch1ep2_757
        with dissolve
        emi "Sit, and sit properly."
        play sound cloth
        scene ch1ep2_758
        with dissolve
        emi "Your cooking was impressive given that you are not a chef."
        emi "You know your ingredients and your flavors. Where did you learn?"
        play sound chair
        scene ch1ep2_759
        with dissolve
        mc "Ah, Klara used to work abroad, so Sky and I were forced to cook on our own."
        mc "We'd look into her secret recipes or through cookbooks. Sometimes, we'd search online."
        mc "All those years of trial and error provided me with the knowledge I have for food."
        scene ch1ep2_760
        with dissolve
        emi "I see, that's interesting."
        emi "If given a chance, I would like to meet her."
        mc "I can arrange something."
        emi "Don't bother for now."
        emi "So, I assume you want to know what happened?"
        mc "Glenn already told me what happened to you guys back then and that it was because of me."
        scene ch1ep2_765
        with dissolve
        mc "Sorry if I sound condescending, but I want to know your reason for casting Gwen out and going as far as to divorce Glenn."
        mc "What was on your mind? What did you think when you made those decisions?"
        mc "I got the gist of it, but I want to hear it from you directly without any pride in the way."
        scene ch1ep2_762
        with dissolve
        emi "Are you planning to reconcile my family? If so, I'd suggest you give it up."
        emi "You saw our current state. I can't see a bright side to any of this."
        emi "So there is no point in telling you."
        scene ch1ep2_765
        with dissolve
        mc "Perhaps.{w} But what's important to me is to know you better."
        mc "I've come to understand both Gwen and Glenn. The only person left is you."
        scene ch1ep2_762
        with dissolve
        emi "And what are you going to do after this?"
        mc "*chuckles* Nothing but celebrate your birthday. All three of us came here for that reason."
        scene ch1ep2_763
        with dissolve
        emi "..."
        scene ch1ep2_764
        with dissolve
        emi "Why bother?"
        emi "I stopped celebrating my birthday so long ago that I forgot it was tomorrow."
        yt "I was right."
        scene ch1ep2_765
        with dissolve
        mc "... You've got no one to celebrate it with, do you?"
        scene ch1ep2_762
        with Dissolve(0.3)
        emi "There is still a thick wall between you and me, [mc]. Don't forget."
        scene ch1ep2_766
        with dissolve
        yt "That's the tone I want. Let's say something to bait her in..."
        scene ch1ep2_765
        with dissolve
        mc "I apologize. I stepped out of line."
        mc "However, you said you don't see a bright side. But if you ask me, {i}you{/i} are the bright side of your family."
        emi "What are you trying to say?"
        scene ch1ep2_766
        with dissolve
        yt "I need something that will contradict her beliefs to crack her open..."
        yt "Let's go Klara mode."
        scene ch1ep2_767
        with dissolve
        mc "If you spoon-feed your student, they will never learn, Emilda."
        emi "Hm, alright, keep your secrets. Regardless, I'm afraid I have to disagree."
        scene ch1ep2_768
        with dissolve
        emi "Making someone learn should always be systematic. A course that everyone can follow."
        emi "I grew up in a family where systems, rules, and discipline were the keys to one's future and well-being."
        emi "In my family, we believe that by adhering to these systems, one can achieve success and happiness."
        scene ch1ep2_769
        with dissolve
        emi "Perhaps my methods were too rigid, but I truly believed that by enforcing discipline, I was doing what was best for my family."
        emi "I never thought my strictness would push them away, leaving me all alone."
        emi "Maybe it's hard for you to understand, but that is how I was raised."
        emi "I thought it was the only way to secure a bright future for Gwen."
        scene ch1ep2_770
        with dissolve
        emi "If you don't follow our ways, you'll never have friends, support, or the connections needed to thrive in this world."
        emi "People like you who refuse to conform may find temporary happiness."
        emi "But in the long run, you'll be left behind, struggling to catch up with those who played by the rules."
        scene ch1ep2_771
        with dissolve
        emi "Now look what Gwen has become."
        emi "A vulgar woman with a major lack of respect."
        emi "I wanted to protect her from the harsh realities of the world, from being taken advantage of or making mistakes that would affect her future."
        emi "But instead, my attempts to control her only pushed her further away."
        scene ch1ep2_772
        with dissolve
        emi "When I heard about Gwen losing her maidenhood to a no-name high schooler without any reputation, I was devastated."
        emi "I had done everything in my power up to that point to guide her on the right path, yet she still made choices I couldn't accept."
        emi "I felt like a failure as a mother, and I couldn't fathom why my system didn't work with her."
        emi "Maybe I was too harsh, but I only wanted the best for her, for our family."
        emi "I didn't want them to suffer the consequences of poor decisions, and I didn't want them to be left behind in a competitive world."
        emi "But now I realize that in my quest to protect them, I might have done more harm than good."
        scene ch1ep2_773
        with dissolve
        emi "That being said, I never considered my ways as wrong, and I never will."
        emi "That is my {i}pride{/i} as-{w=0.7}{nw}"
        show ch1ep2_774
        with Dissolve(0.2)
        emi "..."
        scene ch1ep2_775
        with dissolve
        emi "How did you..."
        mc "I baited you in and triggered you with a point of contention."
        mc "Getting someone riled up gives them a reason to respond, especially when they have a strong sense of pride."
        mc "I just nudged you into sharing what I wanted to hear since our conversation started, and you did."
        scene ch1ep2_776
        with flash
        e "Yes, you'll need it, but once you learn the methods behind it, please use this technique wisely and responsibly."
        e "It can backfire if the other person feels they've been tricked or forced into revealing more than they were comfortable with."
        mc "Understood."
        scene ch1ep2_777
        with flash
        emi "Hahahahaa~! How amusing!"
        scene ch1ep2_778
        with dissolve
        emi "*sighs* \"Eliciting information\". Very bold, but I must admit, it's impressive."
        emi "Alright, you've triumphed over me again and, yet again, obtained what you wanted."
        emi "You're starting to earn my respect, so I'll allow you to converse with me more casually. But watch your words, dear."
        yt "Thanks, Em. All your advice and training paid off... Somehow."
        scene ch1ep2_779
        with dissolve
        mc "So it's \"dear\" now? I'm not sure I've earned that yet."
        emi "Believe me, nobody -and I mean nobody- has ever made my mouth open up like that. You've earned it."
        mc "Thanks, Emilda. But... aren't you upset by what I did?"
        scene ch1ep2_780
        with dissolve
        emi "That's the reaction you were expecting?"
        mc "Well, yeah..."
        emi "Under different circumstances, I might have been."
        emi "However, candidly speaking, your food offering softened me up to your wiles."
        emi "Whether that was intentional or not, it deserves recognition."
        emi "So, what can this old lady do for you now?"
        play sound cloth
        scene ch1ep2_781
        with dissolve
        mc "Like you said, I got what I wanted. So how about I do something for you instead?"
        mc "I heard from Gwen you enjoy massages, apart from food."
        mc "I'm not an expert, but my technique can still help you relax."
        emi "Is that so? You've certainly done your homework."

        scene black
        with dissolve
        with fade

        scene ch1ep2_782
        with dissolve
        mc "She fell asleep while I gave her a shoulder massage."
        gl "Well, she likes that. Didn't Gwen tell you?"
        mc "She did."
        scene ch1ep2_783
        with dissolve
        gl "I'm quite impressed you lasted that long talking to her. Not everybody can."
        mc "Must be because I didn't find her that intimidating to begin with, so I wasn't afraid."
        mc "Gwen also told me that she can sense fear and use that to her advantage during arguments."
        gl "Hah, all the time. Don't I know it."
        gl "Anyway, let's take her to her room."

        scene black
        with dissolve
        with fadeq

        scene ch1ep2_784
        with dissolve
        pause
        scene ch1ep2_785
        with dissolve
        gl "*sighs* Still as beautiful as the day I lost you..."
        scene ch1ep2_786
        with dissolve
        yt "So their feelings are mutual..."
        yt "... I can see a silver lining."
        yt "Now, if I can do something, tomorrow will be an interesting day."
        scene ch1ep2_787
        with dissolve
        gl "[mc], come to the pool in a few minutes. I want to know what you both talked about."
        mc "Copy. I'll go talk to Gwen for a bit."
        stop music fadeout 2

        scene black
        with dissolve
        with fadeq

        play music 'audio/TheSpy.mp3'
        play sound closedoor
        scene ch1ep2_788
        with dissolve
        mc "Gwen, we-{w=0.5}{nw}"
        play sound2 woosh2
        show ch1ep2_789
        mc "Woah!{w=0.8}{nw}"
        play sound2 cloth2
        show ch1ep2_790
        mc "Wait!"
        play sound2 woodhit
        show ch1ep2_791
        with hpunch
        g "Oh, come on! I've been pussyblocked twice already, and I hate not getting what I want!"
        mc "*chuckles* I don't remember spoiling you this much."
        mc "But let's save it for a better time. First, we need to talk."
        mc "It's important."
        scene ch1ep2_792
        with dissolve
        g "Oh? What is it?"
        mc "About you and Emilda..."
        stop music fadeout 2

        scene black
        with dissolve
        with fade

        play sound nightambience loop fadein 2
        scene ch1ep2_793
        with dissolve
        yt "... Uhm, why is the pool steaming?"
        yt "Where is he, anyway?"
        scene ch1ep2_794
        with dissolve
        mc "Uh, Glenn?"
        scene ch1ep2_795
        with dissolve
        gl "Right here, my boy!"
        play music 'audio/BlackMarch.mp3'
        play sound2 slamimpact
        show ch1ep2_796
        pause 2.0
        play sound2 slamimpact
        show ch1ep2_797
        pause 2.0
        play sound2 slamimpact
        show ch1ep2_798
        pause 2.0
        scene ch1ep2_799
        with dissolve
        mc "*gulps*"
        yt "Yeah, better not cause any issues to warrant those arms around my neck..."
        scene ch1ep2_800
        with dissolve
        mc "So you've turned your pool into a hot spring? Pretty damn cool!"
        gl " You think so? This was one of my first masterpieces back in the day."
        scene ch1ep2_801
        with dissolve
        gl "It seamlessly transforms from a refreshing pool to a soothing hot spring at a touch of a button."
        gl "And it features a dynamic temperature control system. An architectural marvel, so I would call it."
        gl "You wanna take a dip? It's good for your butt!"
        yt "Why my butt?"
        scene ch1ep2_802
        with dissolve
        mc "No, I'm good, thanks."
        mc "I'll probably just dip my legs in."
        stop music fadeout 5
        play sound2 watermovement
        scene ch1ep2_803
        with dissolve
        gl "Ahh, that feels very good!"
        play sound2 watermovement
        show ch1ep2_804
        with hpunch
        mc "Ack! That's hot!"
        scene ch1ep2_805
        with dissolve
        gl "So... What did you get from her?"
        mc "Everything I wanted to know."
        gl "Damn, how did you even manage to do that with Emilda?"
        mc "I've never experienced her full wrath, unlike you and Gwen, so I can't say for sure."
        mc "I managed, I guess?"
        gl "Okay, tell me about it."
        stop sound fadeout 2

        scene black
        with dissolve
        with fade

        play music 'audio/Foxear.mp3'
        play sound nightambience loop fadein 2
        scene ch1ep2_806
        with dissolve
        mc "That's all she said."
        gl "Just as I thought..."
        gl "I mean, I knew her ways and methods of discipline, but... I didn't realize she was looking out for Gwen that much."
        scene ch1ep2_807
        with dissolve
        mc "She was confident that it would work, but obviously, that didn't turn out to be the case."
        gl "Do you think she was right imposing her beliefs on Gwen?"
        mc "Honestly?"
        mc "I don't think she was wrong, at least."
        mc "Emilda was merely trying her best for Gwen."
        mc "She only knew the method that she grew up with: an absolute method in her perspective."
        mc "Putting myself into her shoes, I can't say I wouldn't have done the same thing for my daughter."
        mc "Not in a bad way, but Gwen is simply different. And knowing both of them now, I can see why they didn't understand each other."
        mc "However, Gwen's resilience, or perhaps stubbornness, makes her strong. She doesn't have to change."
        gl "What are you going to do now, then?"
        scene ch1ep2_808
        with dissolve
        mc "Prove Emilda wrong."
        gl "How are you going to do that? She said it herself: she will never consider her ways wrong."
        mc "No, not her ways."
        gl "Hm?"
        mc "Gwen came up with the idea earlier, and I think... it might work."
        scene ch1ep2_809
        with dissolve
        mc "I hope it's not too much to ask, but we need your help, Glenn."
        gl "Of course, anything for my kids! I've tried and never got this far, so I won't be the roadblock now!"
        gl "Tell me what it is, and I'll do my best."
        stop music fadeout 2
        stop sound fadeout 2

        call hide_days from _call_hide_days_2
        with dissolve
        scene black
        with dissolve
        with fadeq

        show screen day_saturday with dissolve
        "Saturday, 7 am..."

        scene black
        with dissolve
        with fadeq

        play sound parkwind loop
        scene ch1ep2_810
        with dissolve
        emi "Good morning, dear. All set?"
        mc "Good morning, Emilda. Yeah, all set here."
        play music 'audio/GreedyPersonality.mp3'
        scene ch1ep2_811
        with dissolve
        g "..."
        mc "*chuckles* Good morning, Gwen."
        scene ch1ep2_812
        with dissolve
        g "Good morning."
        g "... Am I sick? Or did she just call you \"dear\"?"
        mc "No, you're not sick, that's for sure."
        scene ch1ep2_813
        with dissolve
        emi "Let me help you. I'm not letting you cook alone for my sake."
        mc "Sure, why not?"
        emi "Please tell me we're having a carrot cake."
        mc "If it's something you like, I know Glenn won't forget it. In fact, he's the one who bought all the ingredients."
        show ch1ep2_814
        emi "Hmp. Of course, he won't."
        scene ch1ep2_815
        with dissolve
        mc "Hmmm?"
        emi "W-what? I did not say anything."
        scene ch1ep2_816
        with dissolve
        g "Okay, you're calling him \"dear\", and now he's teasing you. The hell happened last night?"
        emi "He proved to me that he's credible, and I like him. Thus, I took back what I said about him."
        emi "He has everything I could ask from a man. For that part, I must say you chose the right person."
        play sound2 cloth2
        show ch1ep2_817
        g "*whispers* Hey, good job!"
        mc "*whispers* Well, it's not over yet."
        show ch1ep2_818
        emi "I don't like it when someone talks about me behind my back!"
        play sound2 woosh
        show ch1ep2_819
        mc "I assure you, we are not."
        g "*whispers* We kinda are, though..."
        scene ch1ep2_820
        with dissolve
        emi "Where is your father? I didn't see him upstairs."
        g "Hmnn? Dunno! Probably got tired of you and left."
        play sound2 woosh
        show ch1ep2_821
        mc "*whispers* Don't sound too suspicious!"
        g "*whispers* I'm trying!"
        show ch1ep2_822
        emi "Okay, what is it? Spit it out, you two!"
        g "Not over our dead body!"
        play sound2 woosh
        show ch1ep2_823
        mc "Relax, Emilda. Today is your special day! I mean, you only turn..."
        play sound2 woosh
        show ch1ep2_824
        mc "*whispers* How old is she now?"
        g "*whispers* Fifty."
        play sound2 woosh
        show ch1ep2_825
        mc "I mean, you only turn fifty once, right?"
        emi "I guess so..."
        mc "You know, they say life begins at fifty! And look at you: you're practically aging in reverse!"
        scene ch1ep2_826
        with dissolve
        emi "*giggles* Oh, stop it! But do go on..."
        play sound2 woodhit
        show ch1ep2_827
        with hpunch
        g "What the hell was that giggle supposed to mean?!"
        show ch1ep2_828
        mc "You're like a fine wine - you just get better with age!"
        emi "You're deliberately flattering this old woman, aren't you?"
        mc "Uh, no...?"
        scene ch1ep2_829
        with dissolve
        pause
        scene ch1ep2_830
        with dissolve
        emi "Well? I did not tell you to stop, did I?"
        play sound2 woosh
        show ch1ep2_831
        mc "I must say, your beauty is simply timeless."
        mc "I mean, look at your radiant skin and those sparkling eyes - they could easily pass for someone in their thirties!"
        emi "*giggles* Oh, you're really laying it on thick, aren't you?"
        mc "Well, it's only fitting for a woman as stunning as you."
        mc "And have you noticed how your hair seems to have its natural highlights?"
        mc "It's like you've discovered the secret to eternal youth!"
        emi "Oh, stop! You're making me blush."
        g "Seriously?"
        scene ch1ep2_832
        with dissolve
        mc "And Emilda, have you seen how toned and fit you are?"
        mc "You could easily give those fitness influencers a run for their money! It's truly inspiring!"
        emi "Well, I try to eat healthily and stay active as much as possible between my bible studies."
        g "Oh boy..."
        mc "And one last thing. Your sense of style is absolutely on point."
        mc "You always look effortlessly chic, no matter the occasion. You're a true fashion icon in our eyes."
        g "You mean {i}your{/i} eyes."
        emi "Oh, thank you, dear. You've made me feel extraordinary today."
        g "Jesus Christ. So this is how you won her over...?"
        stop music fadeout 5
        play sound2 jesscarroar
        mc "Special? We're not there yet."
        scene ch1ep2_833
        with dissolve
        mc "..."
        g "Mhm."
        stop sound fadeout 2
        scene ch1ep2_781
        with flash
        mc "I heard from Gwen you enjoy massages, apart from food."
        mc "I'm not an expert, but my technique can still help you relax."
        emi "Is that so? You've certainly done your homework."
        play music 'audio/InYourArmsAgainINST.mp3' fadein 2
        scene ch1ep2_837
        with dissolve
        mc "Let me just ask one more thing..."
        emi "Hm?"
        mc "Do you know how Gwen is currently living right now?"
        scene ch1ep2_838
        with dissolve
        emi "No, I don't. Although, I'm certain she must be a mess and a headache to you."
        scene ch1ep2_839
        with dissolve
        mc "No, Emilda. Gwen has played a huge role in who I am now."
        mc "Wherever my life leads me, she will always be a part of me."
        emi "What are you trying to say?"
        mc "If given the opportunity, would you be willing to make up with Gwen?"
        scene ch1ep2_840
        with dissolve
        emi "..."
        scene ch1ep2_841
        with dissolve
        emi "Yes."
        emi "I never consider my ways wrong, but..."
        emi "There are times when my conscience makes me question what I did to her."
        emi "Was I justified, or was I too much? Was it worth losing her for the sake of my pride?"
        emi "She's my only child and my most prized treasure."
        emi "Even if it's been so long that the odds are near zero, I would like to take the chance to have her in my arms again."
        scene ch1ep2_842
        with dissolve
        g "Is that so...?"
        mc "Yeah, she said it herself."
        g "..."
        scene ch1ep2_843
        with dissolve
        g "[mc]... can you bring them here?"
        mc "Who?"
        g "Everyone."
        mc "Well, it's not out of the question. But what are you planning to do?"
        scene ch1ep2_844
        with dissolve
        g "I will make her understand..."
        g "It has to be me..."
        stop music fadeout 2
        scene black
        with Dissolve(1.0)
        pause
        play sound parkwind loop
        play sound2 slamimpact
        show ch1ep2_834a
        pause 0.3
        play sound3 slamimpact
        show ch1ep2_834b
        pause 0.3
        play sound2 slamimpact
        show ch1ep2_834
        play music 'audio/ExtraFries.mp3'
        shu "Ahoy, lads and lasses! The almighty gang has arrived!"
        show ch1ep2_835
        emi "A-aah, why so many people at once? What's happening?"
        play sound2 cloth2
        show ch1ep2_836
        g "This is my birthday present to you... mom."
        scene ch1ep2_845
        with dissolve
        g "These are my friends, the people who have been there with me through thick and thin and have accepted me for who I am with open arms."
        g "They've helped me grow and become the woman I am today, even after I rejected your \"path to success\" or whatever you might call it."
        scene ch1ep2_846
        with dissolve
        a "I would say instead that you've been there for {i}us{/i}. I cannot even count the times you've set us straight."
        e "Mhm, I agree. Gwen is like the gang's pillar. A critical foundation that never asks for recognition."
        scene ch1ep2_847
        with dissolve
        a "By the way, good morning and happy birthday, Mrs. Wilson. My name is Aine."
        a "Emma and I have only met you once before, but you're still as pretty as since the last time we saw you."
        emi "T-thank you, dear."
        scene ch1ep2_848
        with dissolve
        e "Happy birthday, Mrs. Wilson. I'm Emma."
        e "I apologize. We don't have gifts for you since Mr. Wilson told us to hurry when he woke us all up."
        e "It's such a pleasure to see you again."
        emi "Oh, uh... Don't worry about it, dear. It's okay."
        play sound2 introslam
        play music ["<from 10 to 185>audio/ChoirOfAngels.mp3"] loop
        show ch1ep2_849
        shu "Ahhh...! Happy birthday to you, Mrs. Wilson. My name is Shu. I'm [mc]'s best friend."
        emi "Where is this light coming from?"
        shu "This is the first time we've met, but still, I must say your beauty is truly breathtaking."
        play sound2 heavenlyharp
        scene ch1ep2_850
        with Dissolve(1.0)
        shu "It's as if the heavens have graced us with the presence of a divine goddess, sending you here to live among us, mere mortals."
        shu "Your radiance shines brighter than the sun, casting a warm glow that fills the hearts of everyone in this sacred landscape."
        shu "Your eyes, deep and enchanting like the night sky, draw us in and hold us captive with their magnetic allure."
        scene ch1ep2_851
        with dissolve
        shu "Your smile could tame the wildest of beasts and bring peace to even the stormiest of seas."
        play sound2 seagulls
        shu "In all my years sailing the vast oceans, I've never encountered a beauty so captivating and mesmerizing as yours."
        shu "On this special day, we are all truly-{w=0.8}{nw}"
        stop music
        play sound3 scratch
        play sound2 woosh2
        show ch1ep2_852
        with hpunch
        play music 'audio/ExtraFries.mp3'
        g "Too long and unrealistic! NEXT!"
        scene ch1ep2_853
        with dissolve
        n "G'day, Emilda! I'm Naomi, a mate of Gwen's. Just wanted to say happy birthday and introduce meself."
        scene ch1ep2_854
        with dissolve
        emi "Oh, hello there, Naomi."
        emi "Your accent, are you from Cesa Cityside?"
        n "Yeah! Although I work home maintenance in Golden City, so I currently live there."
        emi "That sounds interesting. It's rare for a woman to take that kind of job nowadays."
        scene ch1ep2_853
        with dissolve
        n "Yeah, but it's a beaut of a job and I love it. Plus, livin' in Golden City is an absolute corker."
        emi "Let's talk later. I have friends from Cesa: perhaps you may know them."
        n "Absolutely!"
        scene ch1ep2_855
        with dissolve
        mc "Your accent is pretty strong today, Naomi. What gives?"
        n "My inner bogan comes out when I'm excited. It's my first time at a party."
        mc "Are you serious?!"
        scene ch1ep2_856
        with dissolve
        g "Hey, short stacks! Introduce yourselves!"
        play sound2 woosh
        show ch1ep2_857
        m "Hi, my name is Moon. I'm [mc]'s bodyguard."
        emi "Bodyguard?"
        show ch1ep2_858
        emi "You have a bodyguard?"
        mc "I don't know, I just got here."
        scene ch1ep2_859
        with dissolve
        s "Hello, Mrs. Wilson~! My name is Sky. I live with [mc]."
        scene ch1ep2_860
        with dissolve
        s "I don't have any significant things to say, but I wish you a happy birthday~!"
        play sound2 cloth2
        show ch1ep2_861
        s "Mmf?"
        emi "Oh, my heavens! You are such a cutie!"
        scene ch1ep2_862
        with dissolve
        emi "You didn't tell me you live with someone this adorable, dear!"
        mc "*chuckles* Well... you didn't ask."
        play sound2 woosh
        show ch1ep2_863
        f "Heya, Mrs. Wilson! Can I take a selfie with you real quick?"
        emi "Uhm, sure..."
        scene ch1ep2_864
        with dissolve
        f "Smile~!"
        play sound2 digitalcamera
        hide ch1ep2_864
        show black
        pause 0.1
        show ch1ep2_864
        pause 0.5
        play sound2 woosh
        show ch1ep2_865
        f "Thankie!"
        f "By the way, the name's Freya! I'm Aine's little sister!"
        f "I'm a locally-based streamer, but quite famous internationally!"
        f "Shu and I are starting a Cryptocurrency business. If you're interested in getting rich, don't hesitate to get in touch."
        emi "O-okay...? I don't even know what that is..."
        stop music fadeout 2
        play music2 'audio/OfSoberMind.mp3' fadein 2 loop
        scene ch1ep2_866
        with Dissolve(2.0)
        k "Oh...! You have such beautiful hands...!"
        scene ch1ep2_867
        with dissolve
        k "And you're quite gorgeous, especially for your age...!"
        scene ch1ep2_868
        with dissolve
        k "Aww...! I'm sure you'd be very good to eat...!"
        emi "W-wait, wha-what? W-who's this?"
        stop music2
        play sound2 woodhit
        show ch1ep2_869
        with hpunch
        mc "Klara, back to your cage."
        play music 'audio/ExtraFries.mp3'
        show ch1ep2_870
        k "Ahem!"
        k "I'm sorry, dear. It seems I got too excited meeting Gwen's mother."
        scene ch1ep2_871
        with dissolve
        k "My name is Klara Hahn, [mc]'s guardian."
        emi "Hahn..."
        emi "Wait a minute, I remember you!"
        emi "You were that first-year who was mistaken for some kind of ghost back in high school at the academy, weren't you?"
        scene ch1ep2_872
        with dissolve
        k "*chuckles* Yes, that would be me."
        emi "I was in my second year. Although I never saw you, the rumors about you traveled academy-wide, even to the college area!"
        k "I was that famous?"
        emi "Yes! Yes, you were!"
        emi "Oh my... It's so surreal that we get to meet this way. It takes me back to those days."
        scene ch1ep2_873
        with dissolve
        emi "So, this lovely gentleman is..."
        k "Yes, I hope he didn't give you much trouble."
        emi "No, I'm pleased to have him here."
        stop music fadeout 5
        play music2 'audio/InYourArmsAgainINST.mp3' fadein 5 loop
        scene ch1ep2_874
        with dissolve
        emi "And... all of you as well."
        emi "I never thought Gwen would..."
        scene ch1ep2_875
        with dissolve
        mc "You may already know, but I didn't look like this in high school."
        mc "In fact, you could say that I was literally twice the guy back then that I am now."
        mc "But Gwen liked me and never judged me despite my appearance."
        mc "She was already decisive even before I met her, Emilda. "
        mc "Everyone here loves her for who she is."
        scene ch1ep2_876
        with dissolve
        k "[mc] filled me in on the situation on our way here."
        k "And Gwen has been living in my house, so it's my job to tell you."
        k "If you're worried about her current state, there is no need."
        k "I personally hired Gwen to be the CEO of my company. She's too overqualified for any positions below that level."
        scene ch1ep2_877
        with Dissolve(2.0)
        emi "..."
        scene ch1ep2_878
        with dissolve
        emi "Gwen, I'm so-{w=0.5}{nw}"
        g "No, don't say sorry. It's long past time for you to use that word."
        emi "Right... because I'm a failure as a mother."
        play sound2 cloth2
        show ch1ep2_879
        with hpunch
        g "..."
        scene ch1ep2_880
        with dissolve
        g "I've called you many things, but a failure was never one of them."
        g "Yes, I rejected your teachings and discipline."
        g "Not because I didn't like it, but rather because I didn't need it."
        g "I knew what I was doing. All I needed was freedom to become who I wanted to be."
        scene ch1ep2_881
        with dissolve
        g "I may be selfish, vulgar, and stubborn, but I never strayed away from my vision."
        g "I know you were only trying your best for our family. And for that, I sincerely thank you."
        g "None of us are failures here, Mom."
        scene ch1ep2_882
        with dissolve
        g "But... if I had one failure in my life, then that would be..."
        mc "Hm?"
        scene ch1ep2_883
        with dissolve
        emi "So... were you a part of this?"
        gl "Perhaps?"
        gl "I asked Gwen to visit you, but the ones who pulled all the strings were those two."
        emi "... Can we talk later?"
        gl "As long as you don't start things with \"Oh\"."
        emi "*chuckles* You hate it that much?"
        stop music2 fadeout 4
        play music 'audio/ExtraFries.mp3' fadein 4 loop
        scene ch1ep2_884
        with dissolve
        emi "Now then..."
        emi "I don't want my birthday to become a melancholic family reconciliation meeting."
        scene ch1ep2_885
        with dissolve
        emi "Dear, may I ask you to take care of things down here?"
        mc "Of course! Klara and Sky are here. Leave it to us."
        mc "We might just be the best cooks you can ask for on your birthday."
        emi "I love your confidence. Don't forget the carrot cake: it won't be my birthday without one."
        mc "Sure!"
        scene ch1ep2_886
        with dissolve
        emi "Now, come with me to my room."
        g "Wait, what are we doing?"
        emi "Please, just this once, I ask you to honor my wishes."
        g "Okay...?"
        scene ch1ep2_887
        with dissolve
        emi "Do any of you know their fashion?"
        play sound2 woosh
        show ch1ep2_888
        pause
        shu "She's a streamer and does cosplay. Aside from Gwen, nobody else here has such impeccable fashion sense."
        scene ch1ep2_889
        with dissolve
        emi "Your name is Freya, right? Come give me a hand, dear."
        f "Alrighty~!"
        scene ch1ep2_890
        with dissolve
        shu "I don't know what's happening, but..."
        scene ch1ep2_891
        with dissolve
        shu "The high seas are waiting, folks!"
        show ch1ep2_892
        shu "Let's goooo~!!!"
        gl "Hey, hey, wait!"
        play sound2 watersplash
        show ch1ep2_893
        pause
        shu "HOOOOOOOOOOOOOOOOOOOOOOOOOOT!!!" with hpunch
        shu "MY EYES!!! THEY'RE BURNING!!!" with hpunch
        shu "OH, THE HUMANITY!!!" with hpunch
        scene ch1ep2_894
        with dissolve
        mc "You forgot to turn off the heater last night..."
        gl "My bad... sorry, miss..."
        shu "I'M!" with hpunch
        shu "A!" with hpunch
        shu "GUY!!!" with hpunch
        mc "His idiocy makes for good entertainment sometimes, though. Not gonna lie..."
        stop music fadeout 2
        stop sound fadeout 2

        scene black
        with dissolve
        with fadeq

        "Two hours later..."

        scene black
        with dissolve
        with fadeq

        play sound parkwind loop
        scene ch1ep2_895
        with dissolve
        shu "Just on the table?"
        k "Yes please, honey. Thank you."
        shu "I got you, I got you."
        play sound2 chairdrag
        scene ch1ep2_896
        with dissolve
        gl "Jesus, it's been two hours. What the hell are they doing to her?"
        gl "Emilda, are you guys ready yet?! It's been two hours, and the kids are hungry!"
        scene ch1ep2_897
        with dissolve
        emi "Coming, we're coming!"
        f "Come on, Gwenny! Hurry!"
        g "I'm in goddamn heels, Frey! Don't rush me!"
        f "They're not even that high!"
        scene ch1ep2_898
        with dissolve
        shu "Juice, juice, juice~!"
        scene ch1ep2_899
        with dissolve
        shu "Hey, here's some juice for every-{w=0.9}{nw}"
        play sound2 glassbreak
        show ch1ep2_900
        shu "... one."
        play music 'audio/LoveALittleHarder.mp3'
        show gwennewhairshowcase
        with Dissolve(1.0)
        pause 10.0
        show ch1ep2_901
        with dissolve
        g "I look stupid, don't I?"
        scene ch1ep2_902
        with dissolve
        mc "N-no, n-not at all..."
        k "Oh... my... goodness..."
        play sound2 cloth2
        show ch1ep2_903
        with hpunch
        shu "Y-y-y-y-y-y-y-"
        shu "Y-y-you're!"
        shu "You're!"
        shu "A girl!" with hpunch
        e "What else would she be?"
        scene ch1ep2_904
        with dissolve
        g "*sighs* Do I have to stay like this until tonight?"
        emi "Just until this afternoon, if you can."
        emi "I admit I was wrong, so just this once, let me see you as how I wanted you to be."
        emi "After this, you are free. I will no longer try to tell you what to do."
        scene ch1ep2_905
        with dissolve
        g "To be fair, I like the hair. Thanks, Frey."
        f "Hm-hmmm! I got you!"
        scene ch1ep2_906
        with dissolve
        mc "Well, the food's ready, everyone! Let's eat!"

        scene black
        with dissolve
        with fadeq

        scene ch1ep2_907
        with dissolve
        shu "Say this morning, I woke up and looked in the mirror."
        shu "And every part of my body was in place."
        shu "Many people died and never saw this day."
        shu "So another day I live, I appreciate."
        scene ch1ep2_909
        with dissolve
        shu "Don't ever wanna act too high and mighty, 'cause tomorrow I can fall down on my face."
        shu "So in everything, Lord, I give you praise, and that puts a smile on my face."
        shu "Lord, I thank you for sunshine."
        shu "Thank you for rain."
        shu "Thank you for joy."
        shu "Thank you for pain."
        shu "It's a beautiful day."
        shu "It's a beautiful day, ayy ayyay..."
        scene ch1ep2_910
        with dissolve
        shu "Amen."
        show ch1ep2_911
        g "*holding back her laughter* Mpfff!"
        scene ch1ep2_912
        with dissolve
        emi "..."
        emi "That was a lovely prayer, young lady."
        scene ch1ep2_913
        with dissolve
        shu "I'm a guy..."
        emi "Such moving words and sincere gratitude towards our Lord... so moving that this stoic old woman almost wept..."
        emi "Please tell me, miss, is your family involved in the church?"
        show ch1ep2_914
        with hpunch
        shu "I'M A G-{w=0.5}{nw}"
        scene ch1ep2_915
        with dissolve
        shu "Ugh, never mind..."
        scene ch1ep2_916
        with dissolve
        shu "Hmm... my dad shares his name with a saint?" 
        scene ch1ep2_917
        with dissolve
        emi "Oh?"
        scene ch1ep2_918
        with dissolve
        emi "... Anyway!"
        emi "You guys have fun to your heart's content."
        scene ch1ep2_919
        with dissolve
        mc "There, there."
        stop music fadeout 2
        stop sound fadeout 2

        scene black
        with dissolve
        with fadeq

        "Late at night..."

        scene black
        with dissolve
        with fadeq

        play music 'audio/InYourArmsAgainInst.mp3'
        scene ch1ep2_920
        with dissolve
        yt "Phew! What a day!"
        yt "I hope the gang returned home safely."
        scene ch1ep2_921
        with dissolve
        yt "Now, then, where are those three?"
        scene ch1ep2_922
        with dissolve
        emi "Glenn, I..."
        gl "There's no need to explain, Emilda. I already know."
        scene ch1ep2_923
        with dissolve
        emi "At least let me finish what I'm going to say, will you?"
        gl "... Go ahead."
        scene ch1ep2_924
        with dissolve
        emi "I know I was wrong, and I'm truly sorry. You and Gwen deserved better. I know that now."
        emi "[mc] and Gwen made me realize that things don't always have to be how I want them to be."
        emi "There are more ways to this world than what I know."
        emi "So from now on, I want to erase who I've been and become someone better."
        emi "I hope it's not too late and too selfish, but..."
        emi "Glenn, come back to me, you and Gwen."
        scene ch1ep2_925
        with dissolve
        gl "Are you... serious?"
        emi "Yes."
        scene ch1ep2_926
        with dissolve
        emi "I spent years thinking only of my pride instead of thinking of you both as my family."
        emi "I want to make things right. I want to make up the years I missed as Gwen's mother and... as your wife."
        play sound cloth
        scene ch1ep2_927
        with Dissolve(1.0)
        emi "So please, I beg of you..."
        emi "Give me one more chance to prove I can be better. Let me prove there is more to me than just constantly arguing with you and Gwen."
        scene ch1ep2_928
        with dissolve
        gl "I'm sure you can. I never once doubted your capabilities as a woman, Emilda. Why do you think I married you?"
        gl "I left because your extreme adherence to your beliefs put us all in this situation; the only way to salvage anything was to leave."
        scene ch1ep2_929
        with dissolve
        gl "But none of that matters now. So, I want to ask you something personal."
        emi "Yes?"
        gl "Do you miss me?"
        show ch1ep2_930
        emi "Yes! Yes, I do! I still love you, Glenn!"
        scene ch1ep2_931
        with dissolve
        gl "Then that's more than enough for me."
        emi "I'm sorry, I'm really sorry... I didn't mean to lose both of you..."
        play music 'audio/SorryMyBad.mp3'
        play sound woosh
        show ch1ep2_932
        mc "This is awesome."
        scene ch1ep2_933
        with dissolve
        mc "It's awesome, you know?"
        mc "You guys are breaking down the walls. You're healing."
        scene ch1ep2_934
        with dissolve
        mc "... It's important."
        gl "..."
        emi "..."
        mc "*deeply exhales*"
        mc "... I ruined the moment, didn't I?"
        scene ch1ep2_935
        with dissolve
        emi "Yes. Yes, you did."
        play sound woosh
        show ch1ep2_936
        mc "Anyway, I'm gonna...{w} go talk to Gwen."
        scene ch1ep2_937
        with dissolve
        emi "*sighs* That young man..."
        stop music fadeout 4
        scene black
        with dissolve
        pause 1.0
        play sound nightambience loop
        scene ch1ep2_938
        with Dissolve(1.0)
        mc "Ah, there's my angel. Still keeping the hair?"
        play sound2 chair
        scene ch1ep2_939
        with dissolve
        g "Haha! I've never been a fan of letting my hair down all day, but I like it this time. Freya did a good job."
        mc "She sure did! You look breathtaking!"
        g "It's good to change up styles once in a while."
        play sound2 cloth
        scene ch1ep2_940
        with dissolve
        mc "You know what I'm thinking?"
        scene ch1ep2_941
        with dissolve
        mc "You should let it down more often from now on. I'd love to see how it sways every time I thrust."
        scene ch1ep2_942
        with dissolve
        g "Hmmm..."
        scene ch1ep2_943
        with dissolve
        g "Thrust, huh? Now, I'm curious."
        mc "Would you like to test it now?"
        g "... No, not right now."
        scene ch1ep2_944
        with dissolve
        mc "Huh... It's rare for you to refuse me after talking dirty and riling me up like that."
        g "... I have something to tell you, [mc]."
        scene ch1ep2_945
        with dissolve
        mc "..."
        yt "Well, I did tell her to open up to me."
        scene ch1ep2_946
        with dissolve
        mc "Okay, I'm listening."
        scene ch1ep2_947
        with dissolve
        g "You were wondering about what happened to my company, right?"
        mc "Oh, yeah... I'm still curious about what happened."
        mc "I heard you were quite successful, and it wouldn't be like you to fail at something so quickly."
        scene ch1ep2_948
        with dissolve
        g "*chuckles* I was a failure even before I took that company from my father."
        g "I didn't lose it, nor did it close down, [mc]."
        g "I left it."
        mc "Huh?! Why?!"
        stop sound fadeout 2
        play music 'audio/InYourArmsAgainInst.mp3' fadein 2
        scene ch1ep2_655
        with Dissolve(1.0)
        mc "Whoa, whoa, whoa..."
        mc "You're doing your assignments now? Is it because the final exam is coming up, or did you get a concussion that changed your personality?"
        mc "Are you sick? What did you eat?"
        g "No, I'm writing a song."
        scene ch1ep2_656
        with dissolve
        mc "A... song? The heck?"
        scene ch1ep2_949
        with dissolve
        mc "So you sing?"
        g "Not really. It's just for fun, you know?"
        g "But I can't properly express what I want to write in words."
        scene ch1ep2_950
        with dissolve
        mc "Let me see."
        mc "..."
        scene ch1ep2_951
        with dissolve
        mc "It's good! Who are you dedicating this to?"
        scene ch1ep2_952
        with dissolve
        g "..."
        show ch1ep2_949
        g "Tch, the hell do you mean who am I dedicating it to? I told you, it's only for fun."
        mc "Well, artists always have certain inspirations for their songs."
        mc "Plus, the amount of \"you\" and \"your\" in the lyrics suggests that you're writing it for someone."
        mc "Are you brokenhearted or what?"
        scene ch1ep2_953
        with dissolve
        g "... I am."
        mc "So you've had a boyfriend? Why didn't you tell me?" #looking away
        g "Why would I?"
        mc "Right..."
        scene ch1ep2_954
        with dissolve
        g "..."
        scene ch1ep2_955
        with dissolve
        g "Do you... want to help me write that?"
        mc "Are you sure?"
        scene ch1ep2_956
        with Dissolve(1.0)
        g "Yeah, since we're graduating in a couple of weeks, this..."
        g "... Is going to be my last memory of you."

        scene black
        with dissolve
        with fadeq

        scene ch1ep2_957
        with dissolve
        pause
        scene ch1ep2_958
        with dissolve
        g "*whispers* I wish we could spend more time like this. But I don't know what you're so afraid of..."
        g "*whispers* If you feel the same way, then fucking tell me, idiot..."
        scene ch1ep2_959
        with dissolve
        g "..."
        scene ch1ep2_960
        with dissolve
        g "*whispers* Or... am I the one who's afraid?"
        g "*whispers* Come on, dude... why am I like this when it comes to him?"
        g "*sighs*"
        scene ch1ep2_961
        with dissolve
        g "Hey, [mc]. Wake up."
        mc "Hmmm?"
        scene ch1ep2_962
        with dissolve
        g "Check this out."
        mc "..."
        g "What do you think?"
        scene ch1ep2_963
        with dissolve
        mc "That looks great if it's a finished product, but... isn't it too short?"
        g "It's more than enough for a slow rhythm acoustic song."
        mc "Can you sing it?"
        g "You mean now?"
        mc "Yep! I want to hear what it sounds like."
        scene ch1ep2_964
        with dissolve
        g "Well..."
        g "Here goes nothing."
        scene ch1ep2_965
        with dissolve
        g "When the sunlight hits my face, it won't be long..."
        g "'Til the time I can forget when I felt strong..."
        scene ch1ep2_966
        with dissolve
        g "But until the night I'm in your arms again..."
        g "I don't wanna get my hopes up in the end..."
        scene ch1ep2_967
        with dissolve
        g "..."
        mc "You're... so goddamn beautiful..."
        scene ch1ep2_968
        with dissolve
        g "What?"
        scene ch1ep2_969
        with dissolve
        mc "No, no, the song! I meant that song was beautiful!"
        scene ch1ep2_970
        with dissolve
        g "..."
        scene ch1ep2_971
        with dissolve
        g "I'll be here the day after graduation."
        g "Come meet me if you want to. If not, I'll still be waiting for you."
        scene ch1ep2_972
        with dissolve
        mc "You know, you sound so different these past few days. What's happening with you?"
        scene ch1ep2_973
        with dissolve
        g "Nothing, just come if you have time, okay? I'll sing you the entire song."
        mc "For real?! Alright, I'll have to come then!"
        
        scene black
        with dissolve
        with fade

        scene ch1ep2_974
        with dissolve
        mc "*sighs* I wish I had asked for her phone number."
        scene ch1ep2_975
        with dissolve
        jo "Young man."
        mc "Johnny."
        scene ch1ep2_976
        with dissolve
        jo "The young lady said you would be here."
        mc "Where's Gwen? I've been waiting for her since morning."
        jo "Young Miss won't able to come. She's not feeling very well and couldn't get up from bed."
        mc "Oh, that's... too bad."
        mc "Then, can you give me her number instead? I want to ask how she's doing."
        jo "I'm afraid I don't have the authority to give her contact information away."
        scene ch1ep2_977
        with dissolve
        jo "However, she gave me this."
        scene ch1ep2_978
        with dissolve
        mc "It's the song's lyrics..."
        jo "She asked me to give it to you and told me that I must tell you that she's..."
        play sound shower loop fadein 2
        scene ch1ep2_979
        with Dissolve(2.0)
        g "*hics* Sorry... I'm sorry..."
        g "*hics* Why am I... a fucking coward when it comes to you?!"
        stop sound fadeout 2.0
        play sound2 nightambience fadein 2 loop
        scene ch1ep2_980
        with dissolve
        mc "That's why you didn't come... you were afraid to tell me how you felt."
        mc "But why? Why were you so afraid?"
        image blink:
            "ch1ep2_981.jpg"
            pause 3.0
            "ch1ep2_982.jpg"
            pause .2
            repeat
        show blink
        with dissolve
        g "It was certainly fear..."
        g "I was afraid that opening up and confessing my feelings for you would make me feel vulnerable."
        g "I feared that expressing my feelings might expose me to emotional risks and weaken me."
        g "Honestly, I still feel the same way. But now that we've passed that barrier, I feel more comfortable telling you all this."
        mc "Hold on. So the reason why you left your company was..."
        g "You."
        g "To overcome my {i}only{/i} failure in life."
        g "To gain what I failed to get before, even if it meant risking my whole heart."
        g "And most importantly, to pursue what I truly want."
        g "Without you, a huge part of me was missing."
        g "It wasn't the company or the money that completed me, but {i}you{/i}."
        g "I fell hard for you, [mc]. And I never, {i}ever{/i} forgot about you."
        mc "Shit, Gwen..."
        mc "You're making me fall in love with you again."
        mc "... Although, I don't feel like I deserve what you did for me."
        mc "I'm just me. Nothing but an average Joe who flips burgers every day."
        mc "Compared to what you could've had with your company, dropping everything to pursue this unremarkable guy is a major downgrade."
        g "That was one of my worries if I told you I left my company for you: I didn't want you to judge yourself."
        g "However, think of what you did for me."
        g "To me, you're not unremarkable nor just an average guy, [mc]."
        g "I knew I would find my happiness with you."
        g "Even if you were just a dime-a-dozen guy, I'm not looking for somebody with superhuman gifts."
        g "Or a superhero in some fairytale shit."
        g "Just someone I can turn to, somebody I can kiss."
        g "Ever since what happened in that bathroom, it's always been only you for me."
        g "And I'm willing to give everything away just to have you in my arms again."
        g "That's how much I love you, [mc]."
        play sound cloth
        scene ch1ep2_983
        with dissolve
        mc "Well, I think I'll have to apologize for being so naive. I'm sorry."
        g "It doesn't matter now. We're far and beyond that in our relationship, aren’t we?"
        mc "Hm, you got a point."
        mc "So... the song. You dedicated it to me."
        g "No, it's a song dedicated to {i}me{/i}."
        g "It could be heard as a love song at first, but..."
        g "It's a song about longing, vulnerability, and the struggle to find strength and hope amidst personal challenges."
        g "The lyrics suggest that somebody is going through a difficult time and is seeking solace and support from a significant person in their life."
        g "The sunlight hitting the person's face symbolizes hope and the possibility of healing."
        g "While the night spent in that person's arms represents the comfort and security that this somebody longs for."
        scene ch1ep2_984
        with dissolve
        mc "The repeated lines in the chorus suggest a constant cycle of hope and fear."
        mc "As the person doesn't want to get their hopes up in case things don't work out in the end."
        mc "... Right?"
        g "Well, you wrote that part."
        mc "The next parts convey a sense of self-awareness."
        mc "The person acknowledges their mistakes and challenges to maintain their balance and sanity."
        mc "The plea for help in picking up the pieces of their pride shows vulnerability and a desire for support from someone who understands them."
        g "That's right."
        g "Overall, \"In Your Arms Again\" tells a story of emotional struggle, the search for support and solace, and the hope for healing and strength."
        mc "I see now..."
        mc "It's not just for you, but everything you faced."
        mc "It's a masterpiece, Gwen."
        g "{i}Our{/i} masterpiece."
        g "You should give yourself more credit, you know?"
        scene ch1ep2_985
        with dissolve
        g "But never mind the song."
        g "[mc], what have you done?"
        mc "Huh?"
        g "First, you got my dad on your side, which I did not expect."
        g "Now, you've fixed my biggest problem."
        g "My family."
        scene ch1ep2_986
        with dissolve
        g "Sure, I thought of the solution, but you became the bridge that united us again."
        g "Without you, this would have been an impossible dream at best."
        g "Just how much do you want to make this woman's heart race for you?"
        scene ch1ep2_987
        with dissolve
        g "Fuck the dating phase, [mc]. You deserve my \"yes\" without even asking for it."
        mc "You mean..."
        g "*giggles* Yeah! I'm all yours!"
        mc "Well... shit!"
        mc "I'm... I'm at a loss for words, Gwen. This is unexpected, but it feels so right."
        mc "I didn't think we'd find ourselves here so soon, but I'm truly grateful we have."
        g "It's rare to meet someone who can make such a significant impact in your life."
        scene ch1ep2_988
        with dissolve
        g "You know, I used to think I didn't need it..."
        scene ch1ep2_989
        with dissolve
        g "But now, I'm excited about the idea of competing for that ring to be on my finger, [mc]~!"
        label gwenanal:
        if _in_replay:
            $ name = persistent.gallery_name
        stop sound2 fadeout 4
        stop music fadeout 4
        play music2 'audio/QuieroSer.mp3' fadein 4 loop
        mc "Well, then..."
        mc "Come and get it, my fallen angel."
        "Still blushing, Gwen gives you a knowing smirk."
        g "Oh, it'll be my absolute {i}pleasure{/i}!"
        play sound chair
        show ch1ep2_990
        with hpunch
        "She throws herself into your arms, driving her lips passionately into yours."
        "The sheer force catches you by surprise and knocks you back, but you recover and return her kiss with an equal intensity."
        scene ch1ep2_991
        with dissolve
        "Your tongues dance passionately in each other's mouths, two synchronized beings moving as one."
        "You continue kissing for a few more moments before you reluctantly break away."
        scene ch1ep2_992
        with dissolve
        mc "Holy... what was that?"
        g "The best kiss of your whole damn life? I know it was for me."
        mc "I mean, where did that come from?"
        mc "We've kissed before, but that felt so much more..."
        g "Passionate? Awesome? Exciting?"
        mc "Real."
        mc "Like everything you had, you put in that kiss."
        mc "Your lips were the messenger that told me how you really feel about me."
        g "You gonna put that on a Hallmark card or something, Mr. Corny?"
        mc "Hey, I'm trying to put into words the thing that made me speechless. Cut me some slack, will you?"
        g "Actually, corny comment aside..."
        g "You pretty much described it exactly."
        g "Now that I know you're the man who will always have my heart, I don't have to hold anything else back."
        g "All that relief, joy, love, longing, ecstasy... everything I'm feeling in this moment, I poured into that kiss."
        g "Words can't describe how much today-"
        g "No-how much {i}you{/i} mean to me, but I hope my actions say what my words cannot."
        mc "Sounds like you have another song on your mind. Are you releasing another single after this?"
        g "Heh, maybe... but..."
        play sound cloth
        scene ch1ep2_993
        with dissolve
        g "Would you rather have me sing right now..."
        g "... Or would you rather make me {i}squirm{/i}?"
        mc "Hmm... that's a choice that keeps getting {i}harder{/i} each second..."
        mc "Might need to get up and walk around to think..."
        g "Oh, cut the bullshit, [mc]."
        g "I've been waiting all day for this, and you're really making me wait even more?"
        g "I don't think so."
        scene ch1ep2_994
        with dissolve
        g "I'm only gonna say this once, but I'll say it in a way that makes it impossible to not understand."
        g "Fuck. Me. {b}Hard{/b}."
        "The desire to do exactly that is almost literally bursting out of you, but somehow you keep your composure."
        "Instead, you choose to tease her just a little bit further."
        mc "No. Wait."
        scene ch1ep2_995
        with dissolve
        g "... Did you not hear what I said, dumbass?"
        mc "I did, but-"
        show ch1ep2_996
        g "No! No more-"
        show ch1ep2_997
        g "W-mmph!"
        "You silence her with a surprise kiss, pushing your tongue deep into her mouth."
        scene ch1ep2_998
        with dissolve
        "Gwen's eyes open wide in shock, but flutter closed as she gives into her desire."
        "You feel a tug on your shirt."
        play sound cloth
        scene ch1ep2_999
        with Dissolve(1.0)
        g "That was a slick move, Casanova. But now, it's my turn."
        "With no wasted motion, she undoes the buttons on your shirt and removes it from your body."
        g "Mmm..."
        g "But that's not enough!"
        mc "*chuckles* I think I get the idea... but what about my view?"
        play sound cloth
        scene ch1ep2_1000
        with Dissolve(1.0)
        "Just as efficiently as she removed your shirt, Gwen strips off her clothes in one fluid motion."
        "Her pale skin glistens in the moonlight as the cool air begins to form goosebumps across her body."
        mc "That's more like it."
        g "I'm not done yet."
        scene ch1ep2_1001
        with dissolve
        "She turns around, giving you a lovely rear view."
        "Gwen's seductive look then turns devious."
        g "Now you'll only fully get to see my ass for this next part since you were such an ass for making me wait."
        scene ch1ep2_1002
        with dissolve
        "She slides her panties down her legs, keeping her thighs together to prevent you from sneaking any peeks."
        scene ch1ep2_1003
        with dissolve
        pause 0.5
        play sound slap
        show ch1ep2_1004
        with hpunch
        "She gives her butt a smack."
        "The skin jiggles tauntingly in front of you, practically begging you to run up and grab it."
        scene ch1ep2_1005
        with dissolve
        "As if she can read your mind, Gwen holds two fingers to where you're staring, then brings them to her eyes."
        scene ch1ep2_1006
        with dissolve
        g "My eyes are up here, mister."
        mc "But the show is down there."
        g "*giggles* Do you want to keep watching? Or do you want me to move on to the next act?"
        mc "Please, do go on."
        g "I thought so."
        scene ch1ep2_1007
        with dissolve
        "Gwen unhooks her bra, letting the fabric glide slowly down her shoulders..."
        "Then her arms..."
        "Then her hands..."
        scene ch1ep2_1008
        with dissolve
        "Until it finally falls off and lands at her feet."
        "Your mouth hangs wide open, mesmerized at the vision before you."
        scene ch1ep2_1009
        with dissolve
        "Gwen then uses her arms to cover her most intimate parts, smiling coyly as she turns around to face you."
        g "I hope you enjoyed the opening act, [mc]."
        mc "Guh..."
        g "Hm-hm... but that's all you'll see for now..."
        mc "No... you can't!"
        g "Relax, dumbo! You didn't let me finish."
        g "All you'll see... until you show me what I want to see."
        g "Catch my drift?"
        mc "Absolutely."
        play sound cloth
        scene ch1ep2_1010
        with Dissolve(1.0)
        "You hastily remove your remaining clothes, baring yourself nude in front of Gwen."
        mc "There. Happy now?"
        g "*giggles* It's hard to tell who's happier: you, me, or little [mc] down there."
        mc "Hey! He's not little."
        g "Sorry: {i}big, powerful{/i}, little [mc]."
        mc "... You drive me crazy sometimes, you know that?"
        scene ch1ep2_1011
        with dissolve
        g "Just sometimes? Then it looks like I need to try harder."
        mc "Maybe in some ways... like showing me what you're hiding right now."
        scene ch1ep2_1012
        with Dissolve(1.0)
        g "Oh, you mean {i}these{/i}?"
        "Gwen moves her hands away, revealing her hidden gems."
        g "They've been dying to make an appearance all day."
        g "But now that they're out, it would be a shame if they had to settle for being a solo act."
        g "Don't you think they'd enjoy having someone else to play along with?"
        mc "I couldn't agree more."
        play sound cloth2
        show ch1ep2_1013
        "You grab her and pull her towards you, unable to wait any longer."
        "Your lips find hers, sharing another deep kiss as your hand travels along her body, coming to rest on her perky breast."
        "Her nipple hardens beneath your touch, the firmness pushing against your palm."
        scene ch1ep2_1014
        with dissolve
        "Before you can continue, Gwen grabs your hand, pushing it down to her pussy."
        "Almost immediately, you sense a warm moisture coating your fingertips."
        scene ch1ep2_1015
        with dissolve
        g "Do you feel that, [mc]?"
        mc "Mhm."
        g "I'm literally dripping right now. You know what that means?"
        mc "Tell me."
        g "It means, fuck the foreplay. I'm ready to go now."
        mc "That's music to my ears."
        mc "Now lay down. It's go time."
        play sound chair
        scene ch1ep2_1016
        with Dissolve(1.0)
        "Gwen reclines back into the chair, propping herself up with her elbows."
        g "I like where this is going... what do you want me to do?"
        mc "Lift your legs up. You wanted me to fuck you hard, right?"
        g "I did..."
        mc "Cool, because I intend to fuck you hard and deep!"
        g "Talk is cheap. Just do it!"
        scene ch1ep2_1017
        with dissolve
        "Using your hands to hold Gwen's legs up, you push yourself into her."
        g "Hnghh! F-finally!"
        "With how wet Gwen is, you're not surprised that you feel basically zero resistance."
        show gwen21
        with dissolve
        "Despite her request to go hard, you start off at a moderate pace, letting her pussy get used to your size."
        "You adopt a smooth rhythm, sliding your cock the entire length into her before moving back so just the tip remains in between her lips."
        g "Mnnhhh... oohhh...!"
        "It doesn't take long for Gwen to let you know you're doing the right thing."
        yt "Gwen..."
        yt "I can't believe I forgot about you after all those moments we shared."
        yt "I'm sorry I wasn't ready to make you mine in high school, but I'm forever grateful that you found your way back to me."
        yt "To think about all the things you gave up for my sake... your friends... your family... your job... and now your heart..."
        yt "I won't make the same mistake again."
        yt "You deserve the world and so much more than I can give you."
        yt "But all I can do is cherish your heart that you've given to me, and live every day to be worthy of such an honor."
        "You continue your steady movements, the pleasure building for both of you."
        g "Ohhh! Ahhh!"
        g "[mc]! Faster!"
        hide gwen21
        show gwen22
        with dissolve
        mc "Got it!"
        "You increase the speed, thrusting your hips as fast as you can."
        mc "How's... that?!"
        g "Ghh! Great!!"
        "The silence of the night is broken by the sounds of your bodies colliding over and over."
        hide gwen22
        show ch1ep2_1018
        "*thud* *thud* *thud* *thud*"
        emi "Hm? What was that?"
        gl "Uh..."
        emi "Is someone knocking on the door?"
        gl "I think it's just the wind knocking some branches against each other."
        emi "Are you sure? Because I could swear it-"
        scene ch1ep2_1019
        with dissolve
        gl "Yep, trust me. Let's move to a different room that's much quieter."
        scene ch1ep2_1020
        with dissolve
        gl "{i}Really, kids? On your mom's birthday?{/i}"
        gl "{i}The vigor of youth, I guess...{/i}"
        show gwen22
        with dissolve
        g "Oohhh! Hahh!!"
        mc "Hmm! Gwen, I'm almost there!"
        g "Nhhh... no! W-wait!"
        hide gwen22
        show ch1ep2_1021
        "You pause, slightly annoyed but concerned."
        mc "What happened? Is something wrong?"
        g "N-not at all... I j-ahh-just want to try something else first."
        scene ch1ep2_1022
        with dissolve
        g "You know, before we both cum."
        g "Let's make it one intense finish today."
        mc "As the lady requests."
        g "Always the gentleman. Now it's time for you to take a seat."
        g "Let me do the work."
        play sound chair
        scene ch1ep2_1023
        with dissolve
        "You do as she says. Gwen turns around, lowering herself onto your throbbing dick."
        g "Ahhh..."
        g "F-fuck... is it bigger than before?"
        mc "I don't think so, but you did stop me when I was getting close."
        scene ch1ep2_1024
        with dissolve
        g "Heh, sorry, but not really."
        g "I think this next bit will have you thanking me soon."
        show gwen23
        with dissolve
        "As soon as she finishes her sentence, Gwen begins moving her legs, grinding her pussy up and down your cock."
        "She moves with expert precision, shaking her butt slightly from side to side once she gets to your base."
        "Every time she does that, sensations of pleasure pulse through your entire lower body."
        mc "D-damn, Gwen! Where did you learn to ride like that?"
        g "Ngahh!! Maybe I'm a natural?"
        g "Or-mmghh!-maybe I've been practicing like every good artist does?"
        mc "Hmm! Naughty girl!"
        "She turns, exposing her supple breast to you."
        "Your mouth wraps around the firm nipple, sucking gently and giving it a quick bite before releasing."
        g "Aghh!! You jerk!"
        mc "That's for-hrrh!-for being a bad girl."
        mc "But admit it: you liked it, didn't you?"
        g "Mnhh! I n-never said I didn't."
        g "Just give a girl a warning n-next time!"
        mc "Maybe I will, maybe I won't."
        g "So it's like that, hm? Two c-can play at that game!"
        hide gwen23
        show gwen24
        with dissolve
        "She increases the pace, moving up and down so forcefully that her ass shakes violently every time it slams down onto your thighs."
        "The marvelous sight combined with her grinding on your member has you approaching the edge once again."
        "Desperate to hold on, you try and think of anything to delay the inevitable."
        "But all you can think of are her ass slamming down onto your thighs... her pussy walls hugging and massaging your cock..."
        yt "Oh well, mission failed. We'll get 'em next time."
        mc "Gwen! I'm gonna cum!"
        g "Haaahh!!! Me too!"
        "Looks like you're not the only one who's losing control due to her."
        g "Cum anywhere y-you want!"
        mc "Rrgh! You sure?"
        g "P-pill! It's ok!"
        menu:
            "Cum inside":
                "Unable to hold on any longer, you release your load deep inside Gwen."
                hide gwen24
                show ch1ep2_1025
                with hpunch
                mc "Hmm!!"
                play sound chair
                show ch1ep2_1026
                with hpunch
                g "[mc]!!!"
                "As Gwen reaches climax, the walls of her vagina contract rhythmically up and down your cock, seemingly milking every last drop out of you."
                mc "Hahh... hahh..."
                "You catch your breath, taking this time to look down at the mess in between your legs."
                "Your cum drips out of Gwen's pussy, coating your cock down to the base."
            "Cum outside":
                "Unable to hold on any longer, you pull out just in time before spraying your load all over the ground."
                hide gwen24
                show ch1ep2_1027
                with hpunch
                mc "Hmm!!"
                play sound chair
                show ch1ep2_1026
                with hpunch
                g "[mc]!!!"
                "As Gwen reaches climax, she arches her back and screams your name."
                mc "Hahh... hahh..."
                "You catch your breath, taking this time to look down at the mess before you."
                "Despite cumming outside, the tip of your dick is still covered in cum. This girl really has a special effect on you."
        
        scene ch1ep2_1028
        with dissolve
        g "Shiiittt... give me... a minute, [mc]..."
        "Somehow, Gwen was able to hold herself up, using your knees as support."
        scene ch1ep2_1029
        with dissolve
        "Once she catches her breath, she stands up to survey her handiwork."
        scene ch1ep2_1030
        with dissolve
        "She kneels down so her face is right next to your manhood, smiling at the sight."
        g "You really didn't hold back at all, did you?"
        mc "I couldn't help it. You bring all that out of me, literally."
        g "Such a shame... all of that waste..."
        mc "It's fine, I can clean it up."
        g "Hell no. I got this."
        scene ch1ep2_1031
        with dissolve
        "She wraps her lips around your dick, taking the full length into her mouth."
        scene ch1ep2_1032
        with dissolve
        "Still keeping her lips sealed around your cock, she uses her tongue to lick around the whole thing until all of the liquid is gone, replaced by her saliva."
        scene ch1ep2_1033
        with dissolve
        "Then, she gradually pulls away from your dick."
        scene ch1ep2_1034
        with dissolve
        "She looks up at you, smirks, then swallows."
        scene ch1ep2_1035
        with dissolve
        "Gwen opens her mouth for you to see."
        g "Told you, I got it."
        "By some miracle, you're able to prevent yourself from cumming all over her face."
        mc "My god, Gwen. What did I ever do to deserve you?"
        scene ch1ep2_1036
        with dissolve
        g "Fucking me in the bathroom was a good start."
        mc "If only that worked on every girl."
        g "Too bad I'm not every girl, [mc]."
        mc "Yeah... but I like having just one of you. It makes you that much more special."
        g "Enough of the sappy talk, [mc]. I'm still not done yet."
        mc "Oh yeah?"
        g "Not even close... and it's all because of you."
        g "You already took my virginity, and after today you've officially taken my heart."
        g "The only thing you haven't taken yet is my rear entrance, if you know what I mean."
        mc "You mean... backdoor exploration?"
        g "Backdoor exploration, oopsie poopsie, playing in the mud, anal, whatever you want to call it."
        g "What do you say, [mc]: are you up for it?"
        menu:
            "Not today":
                mc "As generous of an offer that is, I'm kind of spent after what we just did."
                mc "So I'll have to apologize and decline any backstage performances."
                g "No problem, [mc]. As long as I have you, I'm happy."
                g "Whether or not you decide to explore every opening doesn't matter."
            "Let's explore":
                mc "What a generous offer. Of course I'm up for it!"
                mc "If you don't believe me, just look down."
                scene ch1ep2_1037
                with dissolve
                "You gesture towards your staff, which sure enough is standing tall and ready to go."
                g "*giggles* Okay, but unlike what we just did, please go slowly."
                g "I've never done this before, so I don't know what it feels like."
                mc "Don't worry, Gwen. Just say the word \"chocolate\" if you want to stop."
                scene ch1ep2_1038
                with dissolve
                g "... Chocolate? Really?"
                mc "Yeah... well, it is what it is."
                play sound chair
                scene ch1ep2_1039
                with dissolve
                "Like before, Gwen positions herself so her butt rests above your dick."
                "But this time, your tip rests against the opening of her anus."
                "Gwen pauses, seemingly unsure of whether or not to continue."
                "You decide to use this time to reassure her."
                scene ch1ep2_1040
                with dissolve
                mc "Just go as far as you can go, Gwen. Don't worry about fitting everything in there or about what's happening with me."
                "Whether or not your words worked, Gwen begins to lower herself onto you."
                scene ch1ep2_1041
                with dissolve
                g "Hngh...!"
                "She pushes the very tip of your cock inside her ass, pausing there."
                g "Ugh... so far so good, I think."
                g "I'll try to go down a little bit more."
                mc "No worries, no hurry. Take your time."
                scene ch1ep2_1042
                with dissolve
                "She lowers herself further so that entire head of your cock is now inside."
                g "Ngh... okay, now it's starting to feel a little... weird."
                mc "Do you want to stop?"
                scene ch1ep2_1043
                with dissolve
                g "No, no, I think I just need to get used to it. Give me a second."
                "Gwen stays there for a little while, taking the time to adapt to the new sensation."
                g "Okay, I think I'm good to keep going."
                scene ch1ep2_1044
                with dissolve
                "She lowers herself again, this time taking about half of your dick into her ass."
                g "Ghh... that's as far as I can go, I think..."
                g "[mc], try moving a little, but go slowly. I'll move too, so don't move too much."
                mc "Okay."
                show gwen25
                with dissolve
                "You move your hips up and down gently, making sure to slide your dick no more than halfway into her."
                g "Ahhh... mmhhh..."
                mc "How do you feel?"
                g "It hurt a little at first, but now the pain is fading away."
                "You continue at the same pace for a little while."
                g "Mmhhh... oohhh...."
                mc "How about now?"
                g "It's... starting to feel... better."
                g "Not like when we have regular sex, but it feels pleasing in its own way."
                g "How does this feel, though?"
                "You feel her anus contract, which sends a sudden jolt of pleasure down your cock."
                mc "Mgh! That felt good!"
                g "Good to know... let's move a little faster."
                hide gwen25
                show gwen26
                with dissolve
                "You quicken your movements, still making sure not to push too far inside of her."
                g "Hmm... hmm!"
                mc "Feeling better?"
                g "M-mhm! Oohhh!"
                "Having already adapted to the new sensation, Gwen's body is now beginning to enjoy it increasingly with each movement."
                "As she moves, she contracts her sphincter muscles around your cock, eliciting pleasure with every squeeze."
                g "Ghh!! F-faster!"
                g "B-but don't go too deep!"
                mc "Got it!"
                hide gwen26
                show gwen27
                with dissolve
                "Your bodies move faster, almost to the same speed when you were inside her pussy."
                "While Gwen's movements are still controlled, her voice becomes shakier as she fully surrenders herself to the ecstasy of the moment."
                g "Ngaahh! Hmmhh!!!"
                mc "Ah!! SHIT!"
                g "W-word choice!"
                mc "S-sorry!"
                "You feel yourself nearing your limit once again, Gwen's movements and squeezing becoming too much for you to handle."
                mc "Gwen! I'm gonna cum again!"
                g "O-outside! Please!"
                g "Don't need-hm!-to explain!"
                "You pull out of her ass, cumming all over her back as you reach climax again."
                hide gwen27
                show ch1ep2_1045
                with hpunch
                mc "Gwen!!!"
                show ch1ep2_1046
                with hpunch
                g "[mc]! [mc]!!!"
                play sound thud3
                show ch1ep2_1047
                with hpunch
                "Gwen reaches her apex shortly after, collapsing to the ground as her legs give out."
                mc "{i}Huff... huff...{/i}"
                "As your breathing returns to normal, you look down at Gwen."
                scene ch1ep2_1048
                with dissolve
                g "Hahhh... aaahhh..."
                "Despite the exhausted look on her face, her chest heaving, and her back covered in cum, you can't help but say:"
                mc "You are beautiful, Gwen."
                scene ch1ep2_1049
                with dissolve
                g "Huh... sh... shut up..."
                mc "I mean it, really."
                mc "Not just because of what we did tonight, but because of who you are to me."
                mc "You were the first one at the academy to show me that I mattered."
                mc "You were the one who gave up an almost guaranteed opportunity for a successful life, just so you'd have a non-guaranteed chance to rekindle our relationship."
                mc "You were the one who gave me your entire being, both your body and your heart, even when I can't fully give my heart to you."
                mc "You may be my fallen angel, but that still means I will always know you as my angel."
                scene ch1ep2_1050
                with dissolve
                "Gwen sits up and looks at you, tears in her eyes."
                scene ch1ep2_1051
                with dissolve
                g "You already have my heart, [mc]. You don't need to say things like that anymore, you know?"
                mc "I know, but you deserve to know how I truly feel about you."
                g "God, I want to hug you right now..."
                mc "Ah, ah. Let's get cleaned up first. Please."
                g "Haahaa, I knew you'd say something like that."
                g "Come on, there's a bathroom down the hall."
        stop music2 fadeout 2
        
        scene black
        with dissolve
        with fade
        
        play music 'audio/Forever.mp3'
        play sound nightambience loop
        scene ch1ep2_1052
        with dissolve
        "The two of you lay together on the deck, enjoying the cool breeze as you stare up at the clear night sky."
        "Gwen rests her head on your shoulder, her arm wrapped across your chest."
        "You rest for a few minutes, enjoying a pleasant silence and the comfort of each other's company."
        "However, you feel the need to break the silence to ask an important question."
        scene ch1ep2_1053
        with dissolve
        mc "Hey, Gwen."
        g "Hey, [mc]."
        mc "Do you recall when you mentioned being on the pill just now?"
        g "Hm?"
        g "Oh, yeah. Why?"
        mc "I don't remember you ever taking any birth control before. When did you start?"
        scene ch1ep2_1054
        with dissolve
        g "Do you remember that time when we did it in my room?"
        mc "Of course. It's one of my favorite memories."
        g "Perv."
        mc "At your service."
        g "Anyways, I missed my period by a few days right after that, so I decided to buy a pregnancy test."
        g "Thankfully, the test ended up negative. However, ever since, I decided to be extra careful."
        mc "Really?"
        g "Mhm. I'm not opposed to you putting a baby in me, but not right now."
        yt "Interesting..."
        scene ch1ep2_1055
        with dissolve
        g "I have to crush my competition and win first place in your heart before that happens. And then, we'll talk. Or fuck."
        mc "You don't literally mean you'll crush them, right?"
        g "Like I said, I don't want any real fights, so I'll keep it chill. I promise."
        mc "That's good to know."
        scene ch1ep2_1056
        with dissolve
        mc "Anyways, let's get dressed and head inside! This is nice, but I'm sure we'll get sick if we sleep out here."
        g "Carry me to bed?"
        mc "You have legs, don't you?"
        g "After the things we did tonight, I'll be lucky if I can even stand up tomorrow without being sore."
        g "Besides, this fallen angel needs time to rest her wings and legs."
        mc "Fine, I can't argue with you there."
        play sound2 woodhit
        show ch1ep2_1057
        with hpunch
        mc "Up you go! Your bed awaits, my angel!"
        g "Ahh! This is not what I meant!"
        $ renpy.end_replay()
label gwenfamilyreconcileend:
    stop music fadeout 2
    stop sound fadeout 2
    call hide_days from _call_hide_days_3
    with dissolve
    scene black
    with Dissolve(2.0)
    show ch1ep2end
    with Dissolve(1.0)
    pause 191.0

    scene black
    with dissolve
    with fadeq

    show screen day_monday with dissolve
    "Monday..."

    scene black
    with dissolve
    with fadeq

    play sound shower loop fadein 2
    play music 'audio/EveryoneRainfalls.mp3'
    scene ch1ep2_1058
    with Dissolve(2.0)
    pause
    f "{i}You know... my fans often ask what it's like to be me."
    f "{i}On the surface, it seems simple enough: I just stream the games I love."
    f "{i}You know, sit down, crush some scrubs, and watch money roll in.{w} \nIt must be nice, then?"
    f "{i}I cosplay and wear dresses I like for my viewers to see.{w} \nIt must be nice, then?"
    stop sound fadeout 2
    scene ch1ep2_1059
    with dissolve
    f "{i}But I ask myself, \"Is it\"?"
    f "{i}I must be living my best life, then?"
    f "{i}... \"Am I\"?"
    scene ch1ep2_1060
    with dissolve
    f "{i}I can't give them a proper answer, because I don't know."
    f "{i}I don't know what I want, and I don't know if I really want this kind of job."
    f "{i}I'm only doing this for the sake of self-reliance and not having to depend on others."
    scene ch1ep2_1061
    with dissolve
    f "{i}That's how it has always been for me."
    scene ch1ep2_1062
    with dissolve
    f "{i}I don't want anything else, as long as I can live comfortably enough and provide for myself."
    f "{i}That's all that matters, right?"
    play sound cityalley loop
    scene ch1ep2_1063
    with Dissolve(1.0)
    f "{i}... That's what I thought...{w} until one day when it all changed."
    f "{i}A fan asked me what it is that I like the most."
    f "{i}... What it is... that I like the most...{w} yeah..."
    scene ch1ep2_1064
    with dissolve
    pause
    show ch1ep2_1065
    f "{i}Ah, that guy!"
    play sound2 closedoor
    scene ch1ep2_1066
    with dissolve
    f "..."
    if aineroute:
        scene ch1ep2_1068
        with dissolve
        f "{i}But then... reality always slaps me in the face."
        f "{i}Because the one thing that I like the most has already been taken by someone else."
    else:
        scene ch1ep2_1067
        with dissolve
        f "{i}But then... reality always slaps in the face."
        f "{i}Because the one thing that I like the most has already been taken by someone else."
    stop music fadeout 2
    play music2 ["<from 51.5 to 251>audio/JustOneKiss.mp3"] loop fadein 2
    scene ch1ep2_1069
    with Dissolve(2.0)
    f "..."
    f "{i}The guy that I like..."
    f "{i}... Is my sister's fiancé..."
    scene ch1ep2_1070
    with dissolve
    f "{i}And honestly...?"
    f "{i}I hate seeing them like this..."
    scene ch1ep2_1071
    with Dissolve(2.0)
    f "{i}It hurts... a lot..."
    call hide_days from _call_hide_days_4
    with dissolve
    stop music2 fadeout 3
    stop sound fadeout 3
    scene black
    with Dissolve(3.0)
    pause


    

    jump ch1ep3
