label Episode_6_Start:

    #KoGa3 START#
    $ KoGa3GameProgress = "Ep6"
    #KoGa3 END#

    $ achievement.grant("ACHIEVEMENT_EPISODE_5")
    $ achievement.sync()
    $ Erynn_Week2_Tuesday_Fly = False
    $ Melissa_Week2_Tuesday_Dream = False
    $ Melissa_Week2_Wednesday_Stories = False
    $ Naomi_Week2_Wednesday_Math_Answer = False
    $ Layla_Week2_Wednesday_Rude = False
    $ Layla_Week2_Wednesday_HelpUp = False
    $ Layla_Week2_Wednesday_Knows = False
    $ Alexis_Week2_Wednesday_Tell = False
    $ Alexis_Week2_Wednesday_Breakup = False
    $ Layla_Friends = False
    $ Layla_Week2_Wednesday_SpanishHelp = False
    $ Layla_Week2_Wednesday_CheckOut = False
    $ Layla_Week2_Wednesday_Chichis = False
    $ Erynn_Week2_Thursday_Confront = False
    $ Erynn_Friends = False
    $ Riverside_End = False
    $ Nikki_Week2_Weekend_Movie = False
    $ Nikki_Week2_Weekend_Handle = False
    $ Nikki_Week2_Weekend_SexInside = False
    $ Cara_Week2_Weekend_SexInside = False

    jump Week2_Tuesday_Erynn_Apartment2

label Week2_Tuesday_Erynn_Apartment2:
    scene black with Dissolve(2)
    pause 2
    stop music fadeout 1.0
    play music "Music/Slow4.mp3" volume 0.3
    n "2 hours later."
    scene 06_001 with Dissolve(1)
    mc "Hey! Welcome back."
    mc "Where did you storm off to?"
    mc "I've found your phone, by the way."
    scene 06_002 with Dissolve(1)
    er "..."
    mc "What's wrong?"
    mc "Why are you crying?"
    mc "Erynn?"
    scene 06_003 with Dissolve(1)
    er "Sorry... Can you please leave?"
    mc "Uh? Something wrong? What happened?"
    er "..."
    scene 06_004 with Dissolve(1)
    mc "Hey, are you okay?"
    er "Please [mc]... I need to be alone."
    menu:
        "Leave":
            mc "Okay... Sorry."
        "What's wrong?[KoGa3AutoWTChange1]{size=-4}(Erynn Points-2) {/size} {/color}":
            $ Erynn_Points -= 2
            mc "Can you tell me what happened?"
            scene 06_005 with Dissolve(1)
            er "[mc]... Please, leave!"
            mc "Okay... Sorry."
    scene 06_006 with Dissolve(1)
    mc "{i}(*Sigh* Where should I go now?){/i}"
    mc "{i}(And what actually happened? That was so weird...){/i}"
    x "[mc]!"
    scene 06_007 with Dissolve(1)
    mc "..."
    mc "Melissa?"
    scene 06_008 with Dissolve(1)
    me "Hi. I know you are mad at me, but..."
    mc "*Shakes head* I'm not mad at you."
    me "Thanks. Can we please talk?"
    mc "Uhm... Sure..."
    scene 06_009 with Dissolve(1)
    me "Were you going somewhere?"
    mc "Not really, no. Just looking for a place to stay."
    me "What? Aren't you staying with Erynn?"
    mc "Guess not."
    scene 06_010 with Dissolve(1)
    me "No? She told me you were. That's why I was coming over."
    mc "Well... I was. But she asked me to leave."
    me "Did something happen?"
    scene 06_011 with Dissolve(1)
    mc "I have no idea. She was on the phone and she left. After a couple of hours, she came back crying and wanted to be alone."
    me "Okay... Uhm... Can you wait here for a moment? I'm going to check up on her and then I'll come back."
    scene 06_012 with Dissolve(1)
    me "I really think we need to talk."
    mc "Hmm... Okay."
    scene 06_013 with Dissolve(1)
    me "I'll be quick."
    mc "It's fine. Take the time you need. Or rather, however much time Erynn needs..."
    me "Thank you."
    mc "And Melissa... Can you bring me my t-shirt? I forgot it when I left. It's in a red bag."
    me "Sure."
    scene black with Dissolve(1)
    pause 2
    scene 06_014 with Dissolve(1)
    n "*Knock-knock*"
    me "..."
    scene 06_015 with Dissolve(1)
    n "*Knock-knock*"
    er "Nooo..."
    me "Erynn, it's me. Please, open up."
    me "..."
    me "Erynn!"
    scene 06_016 with Dissolve(1)
    er "Mom..."
    me "Hey. How are..."
    scene 06_017 with vpunch
    me "Oh..."
    er "..."
    me "Are you alright?"
    er "No."
    scene 06_018 with Dissolve(1)
    me "What happened? Does it have anything to do with [mc]?"
    if Alexis_Friends == True:
        er "No, it's about... work."
        me "Want to talk about it?"
        er "I can't."
    else:
        er "No, not really. Maybe... In a way..."
        me "Want to talk about it?"
        er "*Shakes head*"
    scene 06_019 with Dissolve(1)
    me "I met [mc] downstairs on the street. I actually came by to see how you guys are doing."
    er "I asked him to leave because I need to be alone for a while."
    me "Hmm..."
    scene 06_020 with Dissolve(1)
    er "What did he say?"
    me "Nothing. He has no idea what's going on."
    er "..."
    scene 06_021 with Dissolve(1)
    me "I'll let him stay at my place for today. I need to talk to him anyway."
    er "Right... I think we need to talk about something too. But not today."
    scene 06_022 with Dissolve(1)
    me "Just come by when you are ready, okay?"
    er "*Nods* Yeah..."
    me "Well... I'm going to pick [mc] up. I hope he didn't leave."
    er "Thanks, Mom."
    scene 06_023 with Dissolve(1)
    me "Oh... He said he left his t-shirt here?"
    er "Yes, let me get it."
    me "Thank you."
    scene black with Dissolve(1)
    pause 2
    scene 06_024 with Dissolve(1)
    me "Hey! Thanks for waiting."
    mc "Sure."
    me "Come on. Let's go then. I parked this way."
    scene 06_025 with Dissolve(1)
    mc "Did you talk to Erynn?"
    me "I did. But I'm none the wiser. She'll come around when she's ready to talk."
    mc "..."
    me "I'll let you stay at my place, but there's one condition."
    mc "Okay... What's the condition?"
    me "You talk to your mom tomorrow and let her explain."
    menu:
        "Okay":
            mc "I will."
        "How is she?":
            scene 06_026 with Dissolve(1)
            mc "I will."
            mc "How is she doing?"
            me "Not good. She hasn't come out of the house since..."
    scene 06_027 with Dissolve(1)
    mc "Uhm about..."
    me "Let's go home first. I'll tell you there."
    mc "*Nods*"
    jump Week2_Tuesday_Melissa_Home

label Week2_Tuesday_Melissa_Home:
    scene black with Dissolve(1)
    pause 2
    stop music fadeout 1.0
    play music ("Music/LoFi Indie 3.mp3", "Music/LoFi Indie 1.mp3", "Music/LoFi Indie 2.mp3") volume 0.2
    scene 06_028 with Dissolve(1)
    me "Are you hungry? Do you want to eat or drink something?"
    mc "No, I'm good."
    me "Okay. If you're thirsty, you know where the kitchen is. Help yourself. But no alcohol!"
    mc "Gotcha. Thanks, Mel."
    me "I'll get myself something. *Sigh* I think I'll need it."
    scene 06_029 with Dissolve(1)
    mc "..."
    mc "*Sigh*"
    me "Ready to talk?"
    scene black with Dissolve(1)
    transform moveup:
        xalign 0.5 yalign 1.0
        linear 5.0 yalign 0.0
    show 06_030 at moveup
    pause 3
    mc "..."
    mc "Yeah..."
    scene 06_031 with Dissolve(1)
    me "Let me start by apologising."
    mc "..."
    me "Nothing is going on between your mother and me. We were drinking and having fun, one thing led to another and... You saw what happened."
    scene 06_032 with Dissolve(1)
    mc "You aren't..."
    mc "..."
    me "What? Dating? In a relationship?"
    mc "Yes..."
    scene 06_033 with Dissolve(1)
    me "We aren't. We are friends."
    mc "..."
    me "No... Not friends with benefits either. Just friends."
    mc "Hmm..."
    mc "{i}(Just friends? Friends don't kiss each other.){/i}"
    mc "{i}(I wouldn't kiss Nathan...){/i}"
    mc "{i}(Well... I would kiss a friend who's a girl... Maybe it's different between girls?){/i}"
    scene 06_034 with Dissolve(1)
    mc "So, you kiss each other when you are drinking and having fun?"
    me "Normally, we don't..."
    mc "But it happened before?"
    me "If I'm being honest... Yes. Long time ago... When we were in college."
    scene 06_035 with Dissolve(1)
    mc "Truth or dare game, or something like that?"
    me "No, not really. We were just... experimenting, I guess."
    mc "{i}(Experimenting...){/i}"
    me "{i}(I hope Emily won't be mad that I'm telling him all this. But, he's old enough.){/i}"
    me "{i}(It's in the past anyway. Nothing will change that.){/i}"
    mc "Did you know about Dad... I mean Andres?"
    scene 06_036 with Dissolve(1)
    me "I did. But I think you should talk to your mother about that."
    mc "*Sigh*"
    me "Hey! Everything will be fine. Just let her explain. She's not a bad person."
    mc "Yeah, I know."
    scene 06_037 with Dissolve(1)
    mc "How did you actually meet? You and Mom."
    me "Hmm... Long time ago. At college actually."
    jump FB_Emily_Melissa

label FB_Emily_Melissa:
    scene black with Dissolve(2)
    pause 2
    n "Many years ago."
    scene 06_038 with Dissolve(1)
    me "{i}(I missed this. Since Rinny goes to kindergarten, I can do some running again.){/i}"
    scene black with Dissolve(1)
    transform moveup:
        xalign 0.5 yalign 1.0
        linear 5.0 yalign 0.0
    show 06_039 at moveup
    pause 3
    me "{i}(But I actually miss her already. Heh...){/i}"
    me "{i}(Let's take a short break.){/i}"
    scene 06_040 with Dissolve(1)
    d "And what do you expect from me now?"
    me "{i}(What's happening between them?){/i}"
    me "{i}(Shouldn't they talk... privately, maybe?){/i}"
    scene black with Dissolve(1)
    transform moveup:
        xalign 0.5 yalign 1.0
        linear 5.0 yalign 0.0
    show 06_041 at moveup
    pause 3
    m "Nothing!"
    scene 06_042 with Dissolve(1)
    d "Nothing?"
    m "Yeah, nothing! I don't expect anything from you, Andres."
    m "I just wanted to be honest with you."
    d "Honest? Why didn't you start with the fact that you cheated on me!"
    m "I didn't cheat."
    scene 06_043 with Dissolve(1)
    d "Oh? So you just happened to get pregnant by yourself, Emily? Funny. Is that how it works?"
    m "..."
    d "Speechless now?"
    scene 06_044 with Dissolve(1)
    m "It happened before we started our relationship."
    d "Then why didn't you tell me this before we started dating? Don't you think this was important?"
    m "Because I found out a week ago."
    d "You know about this for a week and you didn't tell me?"
    m "..."
    d "What?"
    scene 06_045 with Dissolve(1)
    m "Do you think this was easy for me? I don't know how you would react."
    d "Like this! Exactly like this!"
    m "See. And that's what I was afraid of. Can't you put yourself in my shoes?"
    scene 06_046 with Dissolve(1)
    d "No Emily, I can't. I don't fuck around as you do."
    me "{i}(What is that guy's problem?){/i}"
    scene 06_047 with Dissolve(1)
    d "Who's the father?"
    m "..."
    d "Emily! Who's the freaking father?"
    m "Santiago."
    scene 06_048 with Dissolve(1)
    d "What the fuck! Are you fucking kidding me? You... With that asshole? I can't believe this."
    d "Were you drunk, on drugs or just completely out of your mind?"
    scene 06_049 with Dissolve(1)
    me "HEY!"
    me "Don't talk to her like that! Especially in that tone."
    d "What?"
    scene 06_050 with Dissolve(1)
    me "She's pregnant! Don't you think she's stressed enough already? She doesn't need to hear your bullshit."
    d "Who are you?"
    me "None of your business."
    d "Well... This isn't any of your business either! So stop butting in..."
    me "You made it my business by talking to her that way."
    scene 06_051 with Dissolve(1)
    d "Oh, really?"
    me "Yeah, really!"
    d "..."
    me "Whatcha gonna do? Trying to intimidate me too? Have a go at it!"
    d "Heh... You know what? I've heard enough. I don't have to deal with this."
    scene 06_052 with Dissolve(1)
    m "Andres?"
    d "Leave me alone, slut!"
    me "..."
    m "*Sigh*"
    scene 06_053 with Dissolve(1)
    me "Hey... Are you alright?"
    m "I don't know..."
    m "Sorry."
    scene 06_054 with Dissolve(1)
    me "You don't have to be sorry for anything. You didn't do anything wrong."
    me "I'm the one who needs to apologise for butting in."
    m "No... You were right. He shouldn't talk to me like that."
    scene 06_055 with Dissolve(1)
    me "Come..."
    me "Let's sit down for a moment."
    m "*Nods*"
    scene 06_056 with Dissolve(1)
    me "I'm Melissa."
    m "Hi, Melissa. Emily."
    me "Nice to meet you, Emily."
    m "You too."
    scene 06_057 with Dissolve(1)
    me "I didn't want to eavesdrop, but it was hard to ignore you guys when you were practically standing next to me."
    m "It's fine. And you actually helped me. Besides, it's not a secret... In a few months everyone will know anyway."
    me "Yeah... You're telling me..."
    scene 06_058 with Dissolve(1)
    m "Wait... Are you... pregnant?"
    me "Haha, no. I was though. Two years ago. I have a little girl."
    scene 06_059 with Dissolve(1)
    m "Really? What's her name?"
    me "Erynn!"
    m "Aw... That's so cute!"
    scene 06_060 with Dissolve(1)
    m "Can I ask you how old you are?"
    me "Sure. I'm twenty."
    m "Oh? So you were eighteen when you were pregnant? Heh, just like me."
    scene 06_061 with Dissolve(1)
    me "Yeah... Right out of high school. My parents couldn't be more proud."
    m "..."
    m "{i}(I actually wish I could tell my parents...){/i}"
    scene 06_062 with Dissolve(1)
    m "Was it... Sorry. I don't even know if you want to talk about all this with a stranger."
    m "It's just... *Sigh* You were in the same situation as me, and I don't know who to turn to."
    m "I'm actually so scared. I have tons of questions and..."
    scene 06_063 with Dissolve(1)
    me "Emily! Just ask away. I don't mind at all."
    m "Really?"
    me "Yeah... Back then, I wish I had someone I could ask, probably the same question you have right now."
    scene 06_064 with Dissolve(1)
    m "Thank you. You are the greatest Mel!"
    me "Uh..."
    scene 06_065 with Dissolve(1)
    me "{i}(Seems like she was stressed out even more than I thought.){/i}"
    scene 06_066 with Dissolve(1)
    m "Oh sorry... Can I call you Mel?"
    me "Sure."
    m "Heh. I like you already."
    m "So, Mel..."
    scene black with Dissolve(1)
    pause 2
    scene 06_067 with Dissolve(1)
    m "Haha... That's the cutest thing ever. You need to try to record it next time and show me."
    me "I will."
    n "*Bzzzt. Bzzzt.*"
    scene 06_068 with Dissolve(1)
    m "Hmm... One second."
    m "..."
    m "Oh shit! It's this late already?"
    scene 06_069 with Dissolve(1)
    m "I'd better head back to my dorm. Get at least a bit of studying in before tomorrow's philosophy test."
    me "Ms Wright?"
    m "Yeah... How did... You go to MSU as well?"
    me "Uh-huh."
    scene 06_070 with Dissolve(1)
    m "Oh? You must be... a junior?"
    me "I'm a freshman, actually."
    m "Really? Hmm... I can't remember seeing you before."
    me "Haha. It's probably the hair. It was blonde and much longer until a few days ago."
    m "I can't even imagine. You need to show me a picture of that."
    scene black with Dissolve(2)
    pause 2
    n "Some time later."
    scene 06_071 with Dissolve(1)
    n "*Bzzzt. Bzzzt.*"
    me "Hmm..."
    scene 06_072 with Dissolve(1)
    me "{i}(Heh... It's Emily.){/i}"
    scene 06_073 with Dissolve(1)
    me "Hey, Emily. How are..."
    m "Mel!"
    me "Uh... Yeah?"
    m "This is an emergency. I need you. Now!"
    scene 06_074 with Dissolve(1)
    me "Did something happen?"
    m "Please come to my dorm. Quick!"
    me "What's wrong?"
    me "Em?"
    scene 06_075 with Dissolve(1)
    me "{i}(She hung up.){/i}"
    me "{i}(Oh no! Maybe something's wrong with the baby?){/i}"
    scene 06_076 with Dissolve(1)
    me "Mom... I need to go to my friend's place. It's important."
    me "I don't know how long I'll be gone, so could you please take care of Erynn until I get back?"
    pa "Of course."
    me "Thank you."
    scene black with Dissolve(1)
    pause 2
    scene 06_077 with Dissolve(1)
    me "*Heavy breathing*"
    me "{i}(I'm so out of breath...){/i}"
    n "*Knock-knock*"
    me "Emily?"
    scene 06_078 with Dissolve(1)
    me "Hey. Are you..."
    m "Finally!"
    scene black with Dissolve(1)
    transform moveup:
        xalign 0.5 yalign 1.0
        linear 5.0 yalign 0.0
    show 06_079 at moveup
    pause 3
    me "Uhm..."
    m "Come on in."
    me "Are you alright? Is everything okay with the baby?"
    scene 06_080 with Dissolve(1)
    m "What? Yeah, everything's fine."
    me "Okay? Then what's the big emergency?"
    scene 06_081 with Dissolve(1)
    m "It's right here."
    m "I don't know which dress I should pick."
    scene 06_082 with Dissolve(1)
    me "You're kidding, right?"
    m "No. Look for yourself. I can't decide. You need to help me."
    me "*Sigh* That's why you called me over?"
    m "Of course. I need your opinion."
    me "And here I thought that... *Shakes head* Never mind."
    me "Why would you need to wear a dress anyway?"
    scene 06_083 with Dissolve(1)
    m "Well, it's Friday. I need to party as much as I can before I can't fit into those dresses anymore."
    me "Partying? You know you shouldn't be drinking!"
    m "Of course, Mel. I'm not drinking. Just having fun. Dancing, chatting, maybe a little bit of flirting, you know..."
    me "*Sigh*"
    scene 06_084 with Dissolve(1)
    m "So, which one do you think?"
    me "Hmm... I don't know. I think they both look great."
    me "Can you try them on?"
    scene 06_085 with Dissolve(1)
    m "Sure."
    scene 06_086 with Dissolve(1)
    m "Purple or fuchsia first?"
    me "Uhm... Purple?"
    m "Hehe... Okay!"
    scene black with Dissolve(1)
    pause 2
    scene 06_087 with Dissolve(1)
    m "Option one. What are we thinking?"
    me "You look hot!"
    scene 06_088 with Dissolve(1)
    m "Thanks. I like the colour of this one, but it shows no cleavage."
    me "Is that important?"
    m "Of course it is, Mel. I need to show off my assets."
    me "Heh... I think you show plenty of assets with how skintight that dress is."
    m "Let me show you the other one."
    scene black with Dissolve(1)
    pause 2
    scene 06_089 with Dissolve(1)
    m "Option number two."
    me "I see what you meant about cleavage being important."
    me "Your boobs look amazing in this one."
    scene 06_090 with Dissolve(1)
    m "Right?"
    me "Haha."
    m "Option number two it is. Thanks!"
    scene 06_091 with Dissolve(1)
    am "Hey, girls."
    m "Oh... Hey, Adriana."
    me "Hi."
    scene 06_092 with Dissolve(1)
    m "Meet my friend. Adriana, Melissa. Melissa, this is Adriana, my roommate. And friend!"
    am "Haha. And friend..."
    am "Hey, Melissa. I like your hair colour."
    me "Hi. Thank you. Right back at you."
    am "Thanks."
    scene 06_093 with Dissolve(1)
    am "Are you going out tonight?"
    m "Yeah. I'll try not to wake you when I get back."
    am "Don't worry about it."
    m "Or do you want to come with us?"
    am "Thanks, but I'm not staying. Just picking something up."
    scene black with Dissolve(1)
    pause 2
    scene 06_094 with Dissolve(1)
    am "I'm heading out. Have fun girls. Bye."
    me "Bye, Adriana. Nice to meet you."
    am "You too!"
    m "Bye-bye."
    scene 06_095 with Dissolve(1)
    m "Well... That was Adriana. And now you know as much about her as I do."
    me "What? Didn't you say she's your roommate?"
    m "Yeah... She is... But she's never here. Except for studying when she has a test."
    m "I have no idea where she goes every day."
    me "Maybe she has a boyfriend and stays with him?"
    m "Hmm... Could be."
    scene 06_096 with Dissolve(1)
    me "Does she know you're pregnant?"
    m "No, not yet. Since she's never here, I didn't bring it up yet."
    me "Since she's almost never here, you basically have this room all to yourself then?"
    m "Hehe, yup. And I'm not complaining."
    scene 06_097 with Dissolve(1)
    m "Alright... Your turn now."
    me "My turn?"
    m "Uh-huh. You're coming with me."
    me "Emily... I can't. I have to..."
    m "No. I've already decided."
    me "But I need to..."
    scene 06_098 with Dissolve(1)
    m "Can't you ask your parents to babysit?"
    m "Please Mel? Just this once? For me?"
    m "Mel..."
    me "*Sigh* Fine... I'll call them and ask."
    scene 06_099 with Dissolve(1)
    m "Haha. You are the greatest!"
    me "Uh..."
    scene 06_100 with Dissolve(1)
    m "You make the call and I'll check my closet. I'll find something for you."
    me "What do you mean?"
    m "You can't go like that. Well... You can. You look hot in everything you wear."
    me "Uh? Thanks."
    scene 06_101 with Dissolve(1)
    m "But I really want to see you in a dress."
    me "There's a reason I don't wear dresses. I just don't look good in them."
    m "I don't believe that for a second."
    m "Mel... Please?"
    me "*Sigh...*"
    scene 06_102 with Dissolve(1)
    m "Yay! You are the greatest, Mel!"
    me "You said that already."
    m "I mean it."
    scene black with Dissolve(1)
    pause 2
    scene 06_103 with Dissolve(1)
    m "I think I've found the perfect one for you."
    m "Take a look. What do you think? You like black, right?"
    me "Hmm, I do. But maybe too short and not enough fabric?"
    m "As I said. Perfect! You'll look so good in this, Mel. Try it on at least?"
    me "Sure."
    scene 06_104 with Dissolve(1)
    m "How long has it been since last you wore a dress?"
    me "Years. I think I was 16 then."
    scene black with Dissolve(1)
    transform moveup:
        xalign 0.5 yalign 1.0
        linear 5.0 yalign 0.0
    show 06_105 at moveup
    pause 3
    m "Wow!"
    m "You have an amazing body!"
    me "Eh... Thanks."
    scene 06_106 with Dissolve(1)
    m "You need to show it off more."
    m "You're so pretty! You could be a model, you know that?"
    me "..."
    me "Can I have the dress, please?"
    m "Yeah... Sorry. I'll look for some shoes for you."
    scene black with Dissolve(1)
    pause 2
    scene 06_107 with Dissolve(1)
    me "So... What do you think? Please, be honest."
    m "Oh... my... Melissa!"
    scene 06_108 with Dissolve(1)
    me "It's bad, right?"
    m "What? Are you kidding me?"
    scene black with Dissolve(1)
    transform moveup:
        xalign 0.5 yalign 1.0
        linear 5.0 yalign 0.0
    show 06_109 at moveup
    pause 3
    m "Mel. You look gorgeous!"
    m "You should wear dresses more often. I mean it."
    me "I don't know. This isn't me."
    m "This dress is so you!"
    scene 06_110 with Dissolve(1)
    m "I'm a little jealous now. You're going to take all the attention away from me!"
    me "I can wear something else."
    m "I'm kidding, Mel! You're wearing that dress! End of discussion!"
    me "Heh..."
    scene 06_111 with Dissolve(1)
    m "Come on. Let's leave before you change your mind."
    me "..."
    scene black with Dissolve(2)
    pause 2
    scene 06_112 with Dissolve(1)
    m "*Sigh* I hate this. I really want to drink a cocktail. Can I order one? Just one?"
    me "No! You can't!"
    m "Can I have a sip of yours then? A really small one, just for the taste?"
    scene 06_113 with Dissolve(1)
    me "Emily, no!"
    m "But I hate soda."
    me "Then why did you order it? Just leave it and take something else."
    me "If you just want to taste, why don't you take a mocktail?"
    m "Oh yeah! Why haven't I thought about that? See, Mel. That's why you had to come with."
    scene 06_114 with Dissolve(1)
    x "Hey, ladies. Can I get you anything?"
    m "Heh... What?"
    scene 06_115 with Dissolve(1)
    bt "Dylan! What are you still doing here? I've told you many times to go home."
    bd "But dad... I need to practice for when I'm going to run this place."
    bt "You can practice once you're done with school."
    bd "*Inaudible grumbling*"
    bt "Home! Now!"
    scene 06_116 with Dissolve(1)
    bt "Sorry about that."
    m "Don't worry. He was nice."
    scene 06_117 with Dissolve(1)
    m "Haha... That was cute."
    me "Mm-hmm..."
    m "The bartender is such a hunk."
    me "Emily!"
    scene 06_118 with Dissolve(1)
    m "What? Don't you think?"
    me "Well... He's good-looking... Not my type, though."
    m "Hmm... Okay."
    scene 06_119 with Dissolve(1)
    m "What did the guy look like who... uhm..."
    me "Got me pregnant?"
    m "Yeah..."
    me "Tall, athletic, blonde, covered in tattoos..."
    scene 06_120 with Dissolve(1)
    m "So, you are into tattoos?"
    me "Yeah, I like them."
    m "He sounds like a sexy Viking, huh?"
    me "Haha. Actually... Yeah! That's a good description."
    scene 06_121 with Dissolve(1)
    m "You don't have any picture of him?"
    me "No, I don't. I didn't have my camera with me at that time."
    me "*Sigh* I wish you could take photos with your mobile phone. Wouldn't that be something?"
    m "Great idea. I have it with me all the time. We could've taken pictures right now."
    scene 06_122 with Dissolve(1)
    me "..."
    me "What are you doing?"
    m "Shush..."
    me "Em!"
    m "I'm picturing your sexy Viking in my mind."
    me "Seems like you're doing more than just picturing him..."
    scene 06_123 with Dissolve(1)
    m "Oh, you know it. He's just so hot..."
    me "Seriously, Emily..."
    m "Mmm... Yes... Mr Viking... Pillage me!"
    me "Emily! Quit thirsting over him!"
    m "Haha."
    scene 06_124 with vpunch
    m "Aah!"
    x "Hey there, hot stuff. What's so funny?"
    scene 06_125 with Dissolve(1)
    m "Hey, Santi. You scared me."
    sa "Hi! Sorry."
    sa "Where have you been? I haven't seen you around in weeks."
    sa "Don't tell me you are still seeing that guy. What was his name... Andrew?"
    scene 06_126 with Dissolve(1)
    m "Andres..."
    sa "You can do better, Emily!"
    sa "He's..."
    m "*Sigh* Let's not talk about him..."
    scene 06_127 with Dissolve(1)
    sa "I'm so sorry... Who's your beautiful friend?"
    m "Oh. This is Melissa."
    sa "Hi, Melissa. I'm Santiago or just Santi."
    me "Hey."
    scene 06_128 with Dissolve(1)
    m "And hands off. She's my friend."
    sa "I would never."
    m "Uh-huh..."
    scene 06_129 with Dissolve(1)
    sa "Sorry, Mel. Someone stole my heart already."
    m "..."
    me "Don't worry about it."
    sa "I haven't seen you around before. Are you new?"
    me "Hmm... Sort of."
    scene black with Dissolve(1)
    pause 2
    scene 06_130 with Dissolve(1)
    sa "How about we get out of here? I think we have some catching up to do."
    m "I'm here with Melissa. I'm not going to leave her alone."
    sa "I'll introduce her to my friends. She won't be alone."
    m "No Santi. I know your friends."
    sa "*Sigh* Okay... I get the hint."
    sa "I'll leave you to it. For today!"
    scene 06_131 with Dissolve(1)
    sa "Well... Nice to meet you, Melissa. I'll see you around, Emily."
    m "Uhm... Santiago? Can we meet at the weekend? I really need to talk to you."
    sa "Sure. Call or text me."
    scene 06_132 with Dissolve(1)
    sa "Bye, girls."
    me "Bye."
    scene 06_133 with Dissolve(1)
    sa "And Emily... You look really hot in that dress."
    m "Thank you."
    sa "You too, Melissa. That dress is fire."
    me "Thanks."
    m "See! I told you!"
    scene 06_134 with Dissolve(1)
    x "Oooh! She turned him down!"
    sa "Shut up, Zo!"
    me "So... He's the..."
    m "Mm-hmm. That's him."
    me "He's more my type."
    scene 06_135 with Dissolve(1)
    m "Hey!"
    me "If he had tattoos..."
    m "Haha..."
    scene black with Dissolve(1)
    pause 2
    scene 06_136 with Dissolve(1)
    ""
    scene 06_137 with Dissolve(1)
    sa "Seriously, Emi?"
    sa "You can't do this to me."
    sa "Don't tell me to leave and then dance like this in front of me!"
    scene 06_138 with Dissolve(1)
    m "What do you mean? I'm just dancing with Melissa."
    sa "..."
    sa "You call that dancing?"
    scene 06_139 with Dissolve(1)
    me "Uhm... Emily?"
    m "Uh-huh. What do you call it?"
    sa "I know what you're doing, Emily!"
    m "You do? Jealous?"
    sa "Totally."
    m "Yeah?"
    scene 06_140 with Dissolve(1)
    m "*Whispers* Grab my boobs."
    me "*Whispers* What?"
    m "*Whispers* Grab my boobs!"
    scene 06_141 with Dissolve(1)
    m "..."
    m "How about now?"
    sa "*Shakes head* Em..."
    scene 06_142 with Dissolve(1)
    sa "Can you please come with me?"
    m "No... I told you before. I'm here with my friend."
    scene 06_143 with Dissolve(1)
    me "..."
    scene 06_144 with Dissolve(1)
    sa "Heh..."
    sa "You're something else, Emily."
    sa "I'll let you win this one. You better call me tomorrow, though!"
    scene 06_145 with Dissolve(1)
    m "Haha."
    m "Did you see his face? Totally worth it."
    me "Haha."
    jump FB_Emily_Melissa_Sex

label FB_Emily_Melissa_Sex:
    scene black with Dissolve(1)
    pause 2
    scene 06_146 with Dissolve(1)
    m "Haha..."
    m "That was so much fun. I really needed that."
    m "Come, Mel... Lay down next to me."
    scene 06_147 with Dissolve(1)
    me "Uhm... Did you lose your panties?"
    m "Hmm? I took them off before we went to the club. Don't worry. No one saw."
    me "Are you sure about that?"
    m "No... Haha."
    me "*Shakes head*"
    scene 06_148 with Dissolve(1)
    me "If I didn't know any better, I'd say you are drunk."
    m "Not a sip of alcohol. Just happy. Come on, join me."
    me "Santiago was right. You're something else."
    m "Haha."
    scene 06_149 with Dissolve(1)
    m "Thank you for coming with me. I really needed that."
    me "Sure."
    me "And honestly... I needed that too."
    me "I had fun."
    m "Good."
    scene 06_150 with Dissolve(1)
    m "You can stay the night if you'd like. As you know, there's a free bed."
    me "Might be better to sober up a bit before going home."
    m "Great. So we can talk a bit more."
    scene 06_151 with Dissolve(1)
    m "You're a good kisser."
    me "Heh... Thank you."
    me "First time I've kissed a girl."
    m "Yeah? How was it?"
    me "It was good..."
    scene 06_152 with Dissolve(1)
    me "You've kissed another girl before?"
    m "Mm-hmm."
    m "Wasn't as good as yours, though."
    me "Haha. Thanks?"
    scene 06_153 with Dissolve(1)
    ""
    scene 06_154 with Dissolve(1)
    ""
    scene 06_155 with Dissolve(1)
    m "..."
    scene 06_156 with Dissolve(1)
    m "Mel?"
    me "Hmm?"
    m "Can I kiss you?"
    me "..."
    me "*Nods*"
    scene 06_157 with Dissolve(1)
    me "..."
    scene 06_158 with Dissolve(1)
    ""
    scene 06_159 with Dissolve(1)
    ""
    scene 06_160 with Dissolve(1)
    me "Em..."
    scene 06_161 with Dissolve(1)
    m "Want to stop?"
    me "..."
    me "*Shakes head*"
    scene 06_162 with Dissolve(1)
    m "..."
    scene 06_163 with Dissolve(1)
    ""
    scene black with Dissolve(1)
    transform moveup:
        xalign 0.5 yalign 1.0
        linear 5.0 yalign 0.0
    show 06_164 at moveup
    pause 3
    me "..."
    scene 06_165 with Dissolve(1)
    m "You are so beautiful, Mel."
    me "Thank you. So are you."
    scene 06_166 with Dissolve(1)
    ""
    scene 06_167 with Dissolve(1)
    ""
    scene 06_168 with Dissolve(1)
    ""
    scene 06_169 with Dissolve(1)
    ""
    scene 06_170 with Dissolve(1)
    ""
    scene 06_171 with Dissolve(1)
    ""
    scene 06_172 with Dissolve(1)
    me "Mmm..."
    scene 06_173 with Dissolve(1)
    ""
    scene 06_174 with Dissolve(1)
    ""
    scene 06_175 with Dissolve(1)
    m "Sucking boobs is fun!"
    me "Heh..."
    scene 06_176 with Dissolve(1)
    m "Wanna give mine a go?"
    me "I was waiting for my turn."
    m "Hmm."
    scene 06_177 with Dissolve(1)
    ""
    scene 06_178 with Dissolve(1)
    ""
    scene 06_179 with Dissolve(1)
    ""
    scene 06_180 with Dissolve(1)
    ""
    scene 06_181 with Dissolve(1)
    ""
    scene 06_182 with Dissolve(1)
    ""
    scene 06_183 with Dissolve(1)
    ""
    scene 06_184 with Dissolve(1)
    ""
    scene 06_185 with Dissolve(1)
    ""
    scene 06_186 with Dissolve(1)
    ""
    scene 06_187 with Dissolve(1)
    ""
    scene 06_188 with Dissolve(1)
    ""
    scene black with Dissolve(1)
    transform moveup:
        xalign 0.5 yalign 1.0
        linear 5.0 yalign 0.0
    show 06_189 at moveup
    pause 3
    me "..."
    scene 06_190 with Dissolve(1)
    me "Don't smile like that while looking at my..."
    m "..."
    scene 06_191 with Dissolve(1)
    ""
    scene 06_192 with Dissolve(1)
    ""
    scene 06_193 with Dissolve(1)
    ""
    scene 06_194 with Dissolve(1)
    ""
    scene 06_195 with Dissolve(1)
    me "*Moaning*"
    scene 06_196 with Dissolve(1)
    me "Ah... Emily!"
    scene 06_197 with Dissolve(1)
    me "Mmm..."
    scene 06_198 with Dissolve(1)
    ""
    scene 06_199 with Dissolve(1)
    ""
    scene 06_200 with Dissolve(1)
    m "You're tasty!"
    m "I enjoyed this more than I thought."
    me "You and me both!"
    scene 06_201 with Dissolve(1)
    ""
    scene 06_202 with vpunch
    m "Hahaha..."
    m "Not just pretty, but strong too."
    me "I got excited to taste you now."
    m "..."
    scene 06_203 with Dissolve(1)
    ""
    scene 06_204 with Dissolve(1)
    ""
    scene 06_205 with Dissolve(1)
    ""
    scene 06_206 with Dissolve(1)
    ""
    scene 06_207 with Dissolve(1)
    m "{i}(Why does it feel so different with a girl...){/i}"
    m "{i}(Much softer... More... sensual, maybe?){/i}"
    scene 06_208 with Dissolve(1)
    ""
    scene 06_209 with Dissolve(1)
    ""
    show 06_210
    m "*Moaning*"
    scene 06_211 with Dissolve(1)
    m "Mmm... Melissa..."
    scene 06_212 with Dissolve(1)
    ""
    scene 06_213 with Dissolve(1)
    ""
    scene 06_214 with Dissolve(1)
    m "Ah..."
    m "Fuck... Mel..."
    scene 06_215 with Dissolve(1)
    ""
    scene 06_216 with Dissolve(1)
    ""
    scene 06_217 with Dissolve(1)
    ""
    scene 06_218 with Dissolve(1)
    ""
    scene 06_219 with Dissolve(1)
    ""
    scene 06_220 with Dissolve(1)
    ""
    scene 06_221 with Dissolve(1)
    m "I'm... I'm..."
    scene 06_222 with Dissolve(1)
    me "Ahh..."
    scene 06_223 with Dissolve(1)
    ""
    $ renpy.end_replay()
    scene black with Dissolve(2)
    pause 2
    scene 06_224 with Dissolve(1)
    me "{i}(I actually had a good night of sleep...){/i}"
    me "{i}(But I'd better head home to check on Erynn.){/i}"
    me "{i}(I hope I get there before she wakes up. But knowing her, she's probably already eating pancakes.){/i}"
    scene 06_225 with Dissolve(1)
    me "{i}(I guess I'll let her sleep some more.){/i}"
    n "*Knock-knock*"
    me "{i}(Really? This early on a Saturday?){/i}"
    scene 06_226 with Dissolve(1)
    n "*Knock-knock*"
    me "{i}(*Sigh* Stop knocking already or you wake her up.){/i}"
    n "*Knock-knock*"
    me "..."
    me "{i}(What is so important?){/i}"
    scene 06_227 with Dissolve(1)
    d "Hey... Uhm?"
    me "Melissa."
    d "Hi, Melissa. I'm Andres."
    me "Hey."
    d "Is Emily here?"
    scene 06_228 with Dissolve(1)
    me "She's sleeping."
    d "Oh... Uhm, can I come in?"
    me "I just told you... She's still sleeping."
    d "But it's really important."
    me "*Sigh* Wait here a second."
    d "Okay, thanks."
    scene 06_229 with Dissolve(1)
    d "And Melissa... I'm sorry about last time. It's just..."
    me "It's fine. But you better be apologising to Emily."
    d "That's why I'm here."
    scene 06_230 with Dissolve(1)
    me "Hey, Emily. Wake up."
    m "Ngggh... It's still early..."
    me "I know. Sorry... Andres is here."
    scene 06_231 with Dissolve(1)
    m "What? *Sigh*"
    me "He wants to talk."
    m "Now?"
    me "Seems like it. I need to go anyway, so I'll leave you two alone."
    scene 06_232 with Dissolve(1)
    m "Can't you stay?"
    me "I need to check up on Erynn."
    m "Oh, yeah. Sorry."
    scene 06_233 with Dissolve(1)
    m "Can I call you later?"
    me "Of course!"
    me "Good luck with... You know."
    m "*Nods* Thanks. Bye, Mel."
    me "Bye, Emily."
    jump Week2_Tuesday_Melissa_Home2

label Week2_Tuesday_Melissa_Home2:
    scene black with Dissolve(2)
    pause 2
    scene 06_234 with Dissolve(1)
    mc "So you basically became best friends in college?"
    me "Yeah, we did. A random encounter turned into an amazing friendship."
    me "I can't even imagine a life without her anymore."
    scene 06_235 with Dissolve(1)
    mc "I guess I'm not adopted then?"
    me "Oh, definitely not. I was at the hospital when you arrived."
    me "And by the way. You took your sweet little time and gave your mom a very hard time."
    mc "..."
    scene 06_236 with Dissolve(1)
    me "Want me to show you those pictures at the hospital?"
    mc "No, I believe you. Actually, I never doubted it, to begin with. I was just mad when I said that and not thinking straight."
    me "Everything will be fine if you talk to her."
    mc "Yeah..."
    scene 06_237 with Dissolve(1)
    mc "Oh... Speaking about pictures. Erynn told me there's a picture of you when you still had your natural hair colour."
    me "Haha. She told you that?"
    mc "Can I see? I'm really curious about what it looks like. I just can't picture you as a blonde."
    me "Sure. Let me look for it."
    scene 06_238 with Dissolve(1)
    me "If I still have it, it must be here in this box between all the other older pictures."
    menu:
        "Look closer":
            if Melissa_Points >= 9:
                scene 06_239 with Dissolve(1)
                mc "..."
                mc "Just take them all out. I like looking at... pictures."
                scene 06_240 with Dissolve(1)
                mc "{i}(Why doesn't everyone do squats...){/i}"
            else:
                scene 06_239 with Dissolve(1)
                mc "..."
                mc "Just grab them all."
            scene black with Dissolve(1)
            me "Here you go, [mc]."
            me "[mc]?"
            scene 06_241 with Dissolve(1)
            mc "Oh, sorry. Thanks"
            me "Daydreaming?"
            mc "Uh... Something like that..."
        "Don't":
            mc "Just grab them all."
            scene 06_241 with Dissolve(1)
            me "Here you go."
            mc "Thanks."
    scene 06_242 with Dissolve(1)
    mc "Haha... What is this?"
    me "Which one?"
    scene 06_243 with Dissolve(1)
    me "Haha."
    mc "Looks like you really wanted to be there, haha..."
    me "I can't believe I kept that one."
    mc "Some kind of furry party?"
    me "Haha. Something like that."
    scene 06_244 with Dissolve(1)
    mc "This is great. I saw those ears in Mom's closet once. Now I know where they came from."
    me "Emily still has them?"
    mc "Yeah."
    me "Hmm..."
    mc "Heh. Are you planning something?"
    me "I just might..."
    scene 06_245 with Dissolve(1)
    mc "I saw this one at Erynn's."
    me "That was a fun day."
    mc "Yeah seems like it."
    scene 06_246 with Dissolve(1)
    mc "Is that Andres carrying mom?"
    me "No..."
    mc "Then who?"
    mc "Oh? Is that?"
    me "Yes..."
    mc "{i}(Too bad I can't see his face...){/i}"
    scene 06_247 with Dissolve(1)
    mc "What is his name?"
    me "Santi. Santiago."
    mc "Looks like Mom really liked him?"
    me "She did."
    scene 06_248 with Dissolve(1)
    me "Heh... Little Erynn. She loved to fly like that."
    mc "Maybe she still does. Have you tried?"
    me "Haha. I think I'm not able to get her up there anymore."
    me "Maybe you can?"
    menu:
        "I can try[KoGa3AutoWTChange1]{size=-4}(Erynn Week2 Tuesday Fly) {/size} {/color}":
            $ Erynn_Week2_Tuesday_Fly = True
            scene 06_249 with Dissolve(1)
            mc "I can try next time we use your pool."
            mc "Reenact the Dirty Dancing scene or something..."
            me "Haha. She'd love that actually."
        "Don't think so":
            mc "..."
            mc "Don't think I can do that either..."
    scene 06_250 with Dissolve(1)
    mc "Your first tattoo?"
    me "Yeah. I had it for about a week. But that's when I first showed it to Emily."
    me "It would've been hard to cover that up at the beach..."
    mc "She looks so surprised. What did she say about it?"
    me "She actually liked it."
    mc "Really?"
    me "Yeah. She knows I love tattoos."
    scene 06_251 with Dissolve(1)
    mc "What the... *Shakes head*"
    me "Haha."
    me "Let's just skip to the next one."
    scene 06_252 with Dissolve(1)
    mc "Here is Erynn again on the beach."
    me "..."
    mc "No wait... That's you!"
    scene 06_253 with Dissolve(1)
    mc "Uh..."
    me "Haha, yes. That's the one."
    scene 06_254 with Dissolve(1)
    mc "You looked so different."
    mc "The blonde hair... No tattoos..."
    mc "Erynn really looks like you."
    scene 06_255 with Dissolve(1)
    mc "How old were you when this picture was taken?"
    me "Eighteen."
    menu:
        "Nice picture":
            scene 06_253 with Dissolve(1)
            mc "It's a really nice picture."
            mc "Still can't believe this is you."
        "Beautiful[KoGa3AutoWTChange1]{size=-4}(Melissa Points+2) {/size} {/color}":
            $ Melissa_Points += 2
            # Melissa (14)
            mc "You were really beautiful."
            scene 06_256 with Dissolve(1)
            me "Were?"
            mc "Uh... I mean... You still are."
            me "That's better."
            mc "..."
            scene 06_257 with Dissolve(1)
            me "Haha... I'm just messing around."
            mc "..."
            mc "{i}(You are beautiful, though.){/i}"
    scene 06_258 with Dissolve(1)
    me "I'm going to get myself another beer. Do you want one?"
    mc "Didn't you say earlier, no alcohol?"
    me "One beer is fine."
    mc "I won't say no to that."
    me "Okay."
    scene 06_259 with Dissolve(1)
    mc "Wait... You're not tricking me, are you?"
    me "Me? Never!"
    mc "Ha... Ha..."
    mc "{i}(She's awesome!){/i}"
    scene 06_260 with Dissolve(1)
    me "Cheers."
    mc "Cheers!"
    scene black with Dissolve(1)
    pause 2
    scene 06_261 with Dissolve(1)
    mc "Haha... I just can't picture Mom like that."
    mc "Was she really that crazy?"
    me "I have plenty more stories of her."
    if Melissa_Points >= 11:
        $ Melissa_Week2_Tuesday_Dream = True
        jump Week2_Tuesday_Melissa_Dream
    else:
        jump Week2_Wednesday

label Week2_Tuesday_Melissa_Dream:
    scene 06_262 with Dissolve(1)
    me "You know... You actually really look like your father."
    mc "Yeah? So he was handsome too?"
    me "Haha."
    me "He was."
    scene 06_263 with Dissolve(1)
    mc "..."
    me "..."
    scene 06_264 with Dissolve(1)
    ""
    scene 06_265 with Dissolve(1)
    me "Mmm..."
    scene 06_266 with Dissolve(1)
    me "{i}(How did we get to here?){/i}"
    me "{i}(We were just talking and looking at pictures.){/i}"
    me "{i}(I can't believe I'm doing this... With him...){/i}"
    scene 06_267 with Dissolve(1)
    me "{i}(Why does this excite me this much?){/i}"
    me "{i}(Why am I not stopping him?){/i}"
    scene 06_268 with Dissolve(1)
    me "{i}(Sorry, Emily...){/i}"
    me "{i}(I want this.){/i}"
    scene 06_269 with Dissolve(1)
    ""
    scene 06_270 with Dissolve(1)
    ""
    scene 06_271 with Dissolve(1)
    ""
    scene 06_272 with Dissolve(1)
    me "{i}(I should tell him to stop.){/i}"
    me "{i}(But why can't I?){/i}"
    scene 06_273 with Dissolve(1)
    me "Ah... [mc], keep going..."
    me "[mc]!"
    scene 06_274 with vpunch
    me "*Heavy Breathing*"
    me "{i}(What was that?){/i}"
    me "{i}(That felt so real...){/i}"
    scene 06_275 with Dissolve(1)
    me "{i}(I can't believe I dreamt about him...){/i}"
    me "{i}(It was a dream... Right?){/i}"
    me "..."
    scene 06_276 with Dissolve(1)
    me "*Sigh*"
    me "{i}(Why am I so horny now?){/i}"
    me "{i}(Did it really turn me on this much?){/i}"
    me "..."
    me "{i}(What time is it? Is he still asleep?){/i}"
    scene 06_277 with Dissolve(1)
    me "Mmm..."
    scene 06_278 with vpunch
    me "{i}(Oh my god! What am I doing?){/i}"
    me "{i}(Really, Melissa...){/i}"
    scene 06_279 with Dissolve(1)
    me "*Sigh*"
    me "{i}(I better go do some yoga to calm down...){/i}"
    $ renpy.end_replay()
    jump Week2_Wednesday

label Week2_Wednesday:
    scene black with Dissolve(2)
    pause 2
    n "Wednesday, 07:12."
    scene 06_280 with Dissolve(1)
    mc "*Yawn*"
    mc "{i}(It's still early but it's so hot already...){/i}"
    mc "{i}(What a difference compared to Riverside.){/i}"
    scene 06_281 with Dissolve(1)
    mc "..."
    mc "{i}(This is the first time I've slept in Erynn's room.){/i}"
    mc "{i}(It has changed a lot over the years.){/i}"
    mc "{i}(No more plushies. All the posters are gone...){/i}"
    if Alexis_Friends == True:
        scene 06_282 with Dissolve(1)
        mc "{i}(Even has a picture of her next to her bed.){/i}"
        scene 06_283 with Dissolve(1)
        mc "{i}(They are really good friends, huh?){/i}"
        if Alexis_Sex == True:
            mc "{i}(I guess I'll keep it to myself that I hooked up with Alexis.){/i}"
        else:
            pass
    else:
        scene 06_282 with Dissolve(1)
        mc "{i}(They are really good friends, huh?){/i}"
        scene 06_283 with Dissolve(1)
        mc "{i}(Does Erynn know about Alexis and me?){/i}"
        mc "{i}(She surely would've said something.){/i}"
        mc "{i}(Probably for the best anyway.){/i}"
    scene black with Dissolve(1)
    pause 2
    scene 06_284 with Dissolve(1)
    mc "{i}(Is Melissa already awake?){/i}"
    scene 06_285 with Dissolve(1)
    mc "{i}(Oh...){/i}"
    mc "{i}(Morning yoga.){/i}"
    menu:
        "Keep watching[KoGa3AutoWTChange1]{size=-4}(Melissa Points-2) {/size} {/color}":
            $ Melissa_Points -= 2
            scene 06_286 with Dissolve(1)
            ""
            scene 06_287 with Dissolve(1)
            ""
            scene 06_288 with Dissolve(1)
            me "..."
            me "Morning, [mc]!"
            mc "Uh... Good morning, Melissa..."
            mc "{i}(I'm such an idiot.){/i}"
        "Say something":
            mc "Hey! Morning, Melissa."
            scene 06_289 with Dissolve(1)
            me "Good morning, [mc]."
            me "Could you sleep in Erynn's bed?"
            mc "Yeah, I slept really well."
    scene 06_290 with Dissolve(1)
    mc "Yoga, first thing in the morning. You must have a lot of energy already."
    if Melissa_Week2_Tuesday_Dream == True:
        me "Heh... You could say that."
        me "..."
    else:
        me "I always do a little yoga after I wake up."
        me "Helps my body to wake up."
    scene 06_291 with Dissolve(1)
    me "Are you hungry? I don't know what you eat in the morning. I have bread... Some muesli..."
    mc "No-no... It's fine, thanks. I was planning to go home and talk to Mom."
    me "That's a good idea."
    scene 06_292 with Dissolve(1)
    mc "Melissa... Question though."
    mc "Do you have time later today to cut my hair?"
    me "Hmm... I'm fully booked today. But we can do it now?"
    mc "Yeah, if you don't mind. That'd be perfect."
    scene 06_293 with Dissolve(1)
    mc "It's so hot here, so I just want the sides to be shaved. Maybe that helps a bit."
    me "Yeah and it's not even summer yet. This year especially will be a very hot one."
    me "I'll get my stuff."
    mc "Thanks. But finish your yoga first."
    me "Wanna join me?"
    mc "Haha. Maybe next time."
    scene black with Dissolve(1)
    pause 2
    scene 06_294 with Dissolve(1)
    me "So, shaving the sides. What about the top? Keep it longer?"
    mc "Yes, like a comb-over"
    me "Alright."
    scene black with Dissolve(1)
    pause 2
    scene 06_295 with Dissolve(1)
    me "Want me to get a mirror or..?"
    mc "No, I can see my reflection in the window here. I look like you now!"
    me "Wasn't that what you're going for?"
    mc "Haha. Who knows?"
    mc "Looks good. Exactly what I had in mind. Thank you, Melissa."
    me "You're welcome."
    scene 06_296 with Dissolve(1)
    me "Are you heading next door now?"
    mc "Mm-hmm."
    scene 06_297 with Dissolve(1)
    me "Do me a favour and let her explain yes?"
    mc "I will."
    if Melissa_Points >= 11:
        $ Melissa_Week2_Wednesday_Stories = True
        me "Thank you. And let's do this again sometime. Drinking beers, telling stories. I had fun."
        mc "Definitely."
    else:
        me "Thank you."
    mc "Bye, Melissa."
    me "See you."
    jump Week2_Wednesday_Emily_Talk

label Week2_Wednesday_Emily_Talk:
    scene black with Dissolve(1)
    pause 2
    scene 06_298 with Dissolve(1)
    mc "{i}(Why am I so nervous?){/i}"
    mc "Mom?"
    scene 06_299 with Dissolve(1)
    m "[mc]!"
    scene 06_300 with Dissolve(1)
    m "How..."
    scene 06_301 with Dissolve(1)
    m "Sorry..."
    menu:
        "Hug[KoGa3AutoWTChange1]{size=-4}(Emily Points+2) {/size} {/color}":
            $ Emily_Points += 2
            # Emily (6)
            scene 06_302 with Dissolve(1)
            m "..."
            scene 06_303 with Dissolve(1)
            m "*Crying* I'm sorry. I'm so sorry..."
            mc "I'm sorry too."
        "Don't hug":
            pass
    scene 06_304 with Dissolve(1)
    m "How are you? Is your eye okay?"
    mc "I'm good. It healed up pretty quickly."
    mc "..."
    mc "I'm sorry about the restaurant. I promised I'd help, and..."
    m "I understand, after what I said..."
    mc "No... I totally overreacted."
    scene 06_305 with Dissolve(1)
    mc "And I'm really sorry about that. I know it's no excuse, but I had a shitty day... It was just the first thing that came to mind, and..."
    m "It's okay. I shouldn't have told you like that. I'm sorry too."
    m "Do you want to talk? If you have any questions, I'm happy to tell you everything."
    mc "*Nods* Yeah..."
    mc "So... about Andres. He isn't my real dad?"
    m "No. Let's sit down. It's a long story."
    scene 06_306 with Dissolve(1)
    m "Your real dad's name is Santiago."
    mc "Santi."
    m "Oh... You know?"
    mc "Melissa told me his name."
    m "Okay... Did she say anything else?"
    mc "No. She told me to ask you."
    scene 06_307 with Dissolve(1)
    m "Well... We dated on and off in high school and college."
    m "I was already pregnant with you before I met Andres."
    mc "Does he know that he has a son?"
    m "Santiago? He does."
    mc "..."
    jump FB_Emily_Santiago

label FB_Emily_Santiago:
    scene black with Dissolve(2)
    pause 2
    n "Many years ago."
    scene 06_308 with Dissolve(1)
    sa "Hey, gorgeous."
    scene black with Dissolve(1)
    transform moveup:
        xalign 0.5 yalign 1.0
        linear 5.0 yalign 0.0
    show 06_309 at moveup
    pause 3
    m "Hey."
    sa "Missed me?"
    scene 06_310 with Dissolve(1)
    m "No..."
    sa "Haha. Liar."
    scene 06_311 with Dissolve(1)
    sa "You look beautiful, by the way."
    m "Thanks."
    scene 06_312 with Dissolve(1)
    sa "So... You wanted to talk?"
    m "*Nods* Yes..."
    m "Be careful up there."
    sa "I am."
    scene 06_313 with Dissolve(1)
    m "..."
    m "Can you come down, please?"
    sa "What? Scared I'd fall off?"
    scene 06_314 with Dissolve(1)
    sa "Aaah..."
    m "SANTIAGO!"
    scene 06_315 with Dissolve(1)
    sa "Haha..."
    m "Are you fucking kidding me?"
    m "Don't do this to me! This is not funny!"
    sa "Sorry-sorry."
    scene 06_316 with Dissolve(1)
    m "Can you please come down?"
    m "It makes me uncomfortable."
    sa "I love it when you worry about me."
    m "..."
    m "Please, Santi?"
    scene 06_317 with Dissolve(1)
    sa "I'm sorry."
    sa "Forgive me?"
    m "No..."
    scene black with Dissolve(1)
    transform moveup:
        xalign 0.5 yalign 1.0
        linear 5.0 yalign 0.0
    show 06_318 at moveup
    pause 3
    m "Hahaha..."
    sa "Please, forgive me! I can't have you be angry at me. Even though I like when you look at me like that!"
    m "..."
    m "Fine. Can you put me down now?"
    m "We need to talk."
    scene 06_319 with Dissolve(1)
    sa "I like you in my arms."
    m "Santi..."
    scene 06_320 with Dissolve(1)
    sa "You're so gorgeous!"
    sa "Most beautiful girl in the world!"
    m "..."
    scene 06_321 with Dissolve(1)
    m "Santi..."
    m "We really need to talk."
    scene 06_322 with Dissolve(1)
    sa "I heard the good news already."
    m "You know?"
    sa "Of course."
    m "Who told you? Melissa?"
    sa "No. Diego. One of my friends."
    m "How does he..? Wait... What are we talking about?"
    scene 06_323 with Dissolve(1)
    sa "Your break-up with Andres. About time if you ask me. You are way out of his league."
    m "Oh..."
    sa "Aren't you broken up?"
    m "We are."
    scene 06_324 with Dissolve(1)
    sa "Good."
    m "..."
    sa "What did you want to talk about then?"
    scene 06_325 with Dissolve(1)
    m "*Sigh*"
    m "..."
    m "I'm pregnant."
    scene 06_326 with Dissolve(1)
    sa "..."
    sa "What?"
    m "I'm pregnant."
    sa "..."
    scene 06_327 with Dissolve(1)
    sa "Is it?"
    m "It's yours."
    sa "..."
    scene 06_328 with Dissolve(1)
    sa "Wow..."
    sa "Uhm... That's..."
    m "..."
    m "Sorry..."
    scene 06_329 with Dissolve(1)
    sa "No. It's not your fault, Emily..."
    sa "It's just..."
    sa "*Sigh*"
    sa "I don't know what to say."
    scene 06_330 with Dissolve(1)
    sa "..."
    sa "Can I have a few days?"
    sa "Just to have it sink in, and..."
    sa "Man... I don't know. To think?"
    m "*Nods*"
    scene 06_331 with Dissolve(1)
    sa "I'm sorry..."
    sa "This is probably not what you want to hear right now..."
    m "No, I understand."
    sa "We will talk about it, but I need a clear mind for it. And right now..."
    sa "*Sigh*"
    scene 06_332 with Dissolve(1)
    sa "Want me to bring you home?"
    m "No, I'll stay here a bit longer. I need to think too."
    sa "Alright."
    sa "We'll figure it out, okay?"
    m "*Nods*"
    scene 06_333 with Dissolve(1)
    ""
    scene 06_334 with Dissolve(1)
    sa "I'll call you tomorrow."
    m "Alright."
    sa "Bye, Emily."
    m "Bye..."
    scene 06_335 with Dissolve(1)
    m "..."
    scene 06_336 with Dissolve(1)
    m "*Sigh*"
    m "What should I do?"
    m "I wish you were still here, Mom! I really need you right now."
    scene black with Dissolve(2)
    pause 2
    scene 06_337 with Dissolve(1)
    m "Hello..."
    pa "Hi. Are you, Emily?"
    m "Uhm..."
    pa "Don't worry. We are Santiago's parents. Do you have a minute to talk to us?"
    m "..."
    m "Sure."
    scene black with Dissolve(1)
    pause 2
    scene 06_338 with Dissolve(1)
    pa "What we mean is..."
    pa "You guys are so young and you are still in college. You have your whole lives ahead of you."
    pa "We just think it would be better."
    m "..."
    scene 06_339 with Dissolve(1)
    pa "Here, this is for you. For your trouble."
    m "Heh... Trouble?"
    m "I can't believe this."
    scene 06_340 with Dissolve(1)
    pa "Honey, listen..."
    m "Don't honey me!"
    m "Keep your money. I don't want it."
    scene 06_341 with Dissolve(1)
    m "This is my decision. I won't let anyone decide for me!"
    m "Don't contact me again. Goodbye!"
    scene black with Dissolve(2)
    pause 2
    scene 06_342 with Dissolve(1)
    sa "Hey... Where have you been? Are you alright?"
    sa "Had to call around to find out where you are. Why aren't you answering my calls? Are you ignoring me?"
    scene 06_343 with Dissolve(1)
    m "..."
    sa "Can we talk?"
    m "No!"
    sa "Please?"
    scene 06_344 with Dissolve(1)
    m "*Sigh...*"
    sa "What?"
    sa "Did I do something?"
    scene 06_345 with Dissolve(1)
    sa "Where are you going?"
    m "Away from you!"
    sa "What's wrong?"
    m "I don't want to see you anymore."
    sa "What happened? I don't understand."
    sa "Emily..."
    scene 06_346 with Dissolve(1)
    sa "Is she mad at me?"
    me "No shit!"
    sa "Why?"
    me "..."
    scene 06_347 with Dissolve(1)
    sa "Emily! Wait!"
    m "..."
    jump Week2_Wednesday_Emily_Talk2

label Week2_Wednesday_Emily_Talk2:
    scene black with Dissolve(2)
    pause 2
    scene 06_348 with Dissolve(1)
    mc "What happened then?"
    m "I left school for a while because of the pregnancy and when I went back, he had already graduated."
    m "We didn't have any contact until six years ago when we ran into each other in the city."
    m "We've met a few times since."
    scene 06_349 with Dissolve(1)
    mc "He didn't want to meet me?"
    m "He did, but I told him about the promise I made to Andres."
    m "And he said that it might be better just to keep it that way."
    m "Do you want to meet him?"
    mc "..."
    scene 06_350 with Dissolve(1)
    mc "I don't know yet. I have to get used to it first and think about it."
    m "Take all the time you need. I'll support your decision."
    mc "Thanks."
    mc "What was the promise?"
    scene 06_351 with Dissolve(1)
    m "Andres was always there for me, for us, when you were born."
    m "He helped us with everything."
    scene 06_352 with Dissolve(1)
    m "When you were around a year old, you started to call him dad."
    m "Heh... Every time you said it, he started crying."
    m "He asked me to marry him but he had one condition."
    scene 06_353 with Dissolve(1)
    mc "Not to tell me he isn't my real dad."
    m "Exactly."
    m "He said he would do it himself when he was ready."
    m "And I agreed to it."
    scene 06_354 with Dissolve(1)
    m "I hoped that he would tell you when you were living with him..."
    mc "Yeah... He didn't..."
    mc "..."
    scene 06_355 with Dissolve(1)
    mc "Why did you actually break up?"
    m "We always had our problems and small fights, like every couple I suppose."
    mc "Really? I never saw or heard you fight."
    m "We tried our best to keep you out of it."
    m "But once I started meeting up with Santiago, things became worse."
    scene 06_356 with Dissolve(1)
    m "I know I shouldn't have, but we only talked, mostly about you."
    m "But Andres thought I was cheating on him and broke the promise I made."
    m "Which wasn't true."
    m "But every time we fought, the smallest of things, he brought up Santiago again."
    m "Said that I never truly loved him, that my heart is still with Santiago."
    scene 06_357 with Dissolve(1)
    mc "Seems to me that you still love him."
    m "I'll always love him. He gave me you."
    mc "..."
    m "Our last fight ended when he said that this was his biggest mistake."
    scene 06_358 with Dissolve(1)
    mc "But if he thinks I'm a mistake, why did you send me to him?"
    scene 06_359 with Dissolve(1)
    m "I'm the mistake! Not you. Don't you ever think that! He loved... loves you."
    m "The one thing I'm still grateful for is how he took you in as his own son and cares about you."
    if Andres_FB_Punch == True:
        scene 06_360 with Dissolve(1)
        mc "Well... Not anymore. He actually hit me and that's why I moved back here."
        m "He did what? No, he didn't?"
        mc "..."
        scene 06_361 with Dissolve(1)
        m "Are you alright?"
        mc "It's fine..."
        m "No! This is not fine! I can't believe it. I'm calling him right now."
        mc "No, Mom... It was my fault."
        mc "I accused him of cheating, just like I did with you and..."
        scene 06_362 with Dissolve(1)
        m "No! That's still no reason to hit you. He should never lay a hand on you!"
        mc "Are you really going to call him?"
        m "Of course."
        scene 06_363 with Dissolve(1)
        m "..."
        m "ANDRES! You hit [mc]?"
        m "..."
        m "DO YOU THINK..."
        m "Hello?"
        m "ANDRES?"
        scene 06_364 with Dissolve(1)
        m "OH THAT MOTHERFUCKER HUNG UP."
        mc "{i}(Wow... I've never heard Mom swear like that.){/i}"
        mc "{i}(That's actually funny.){/i}"
        scene 06_365 with Dissolve(1)
        m "Sorry."
        mc "No, it's alright."
    else:
        pass
    scene 06_366 with Dissolve(1)
    m "*Sigh*"
    m "I sent you there because you always listened to him. He always knew what to do and say."
    m "I guess that's where I failed as a mother... I'm sorry, [mc]."
    menu:
        "Disagree[KoGa3AutoWTChange1]{size=-4}(Emily Points+2) {/size} {/color}":
            $ Emily_Points += 2
            # Emily (8)
            scene 06_367 with Dissolve(1)
            mc "No... Don't say that! You're an amazing mother. You did the thing that was best for me at that time."
            mc "If you didn't send me there, who knows what would've happened."
            mc "And it was me who stayed longer than just spring break. Much longer..."
            mc "I'm not mad at you at all."
            m "Thank you."
        "Don't say anything":
            mc "..."
    scene 06_368 with Dissolve(1)
    m "Oh, shit! It's this late already..."
    m "I'm sorry, [mc]. I need to head to the restaurant."
    scene 06_369 with Dissolve(1)
    mc "It's okay. I need to leave for school anyway."
    m "I'll tell you more later when I'm back, okay?"
    mc "Sure. Do you still need me to help at the restaurant?"
    scene 06_370 with Dissolve(1)
    m "Oh... If you could help out for two, three hours in the evening?"
    mc "Of course."
    m "Thank you so much."
    m "See you later, yes?"
    mc "Yeah."
    scene 06_371 with Dissolve(1)
    mc "By the way... Do you know how much money it was?"
    m "No, I didn't take the envelope."
    mc "You should've taken it and ran with it."
    m "I'd rather have you than any money in the world."
    scene 06_372 with Dissolve(1)
    mc "..."
    mc "I mean both."
    m "Oh... Haha..."
    menu:
        "Love you[KoGa3AutoWTChange1]{size=-4}(Emily Points+2) {/size} {/color}":
            $ Emily_Points += 2
            # Emily (10)
            scene 06_373 with Dissolve(1)
            mc "And Mom..."
            mc "I love you!"
            scene 06_374 with Dissolve(1)
            m "I love you!"
            if Emily_Points == 10:
                scene 06_375 with Dissolve(1)
                m "..."
            else:
                pass
            jump Week2_Wednesday_School
        "Leave":
            jump Week2_Wednesday_School

label Week2_Wednesday_School:
    scene black with Dissolve(1)
    pause 2
    stop music fadeout 1.0
    play music ("Music/LoFi Upbeat 1.mp3", "Music/LoFi Upbeat 2.mp3", "Music/LoFi Upbeat 3.mp3", "Music/LoFi Upbeat 4.mp3") volume 0.2
    n "Wednesday, 08:26. School."
    scene 06_376 with Dissolve(1)
    ""
    scene 06_377 with Dissolve(1)
    mc "Yo. Sup, Zachy!"
    z "Hey! Why are you so happy today?"
    mc "Nothing in particular. Just a good day I guess."
    z "Gotcha. Wait... What are you doing here? Track has no training today, no?"
    mc "How do you even know that?"
    scene 06_378 with Dissolve(1)
    z "Valeria!"
    mc "Right... The new girl."
    mc "{i}(He probably knows her whole schedule.){/i}"
    mc "Well... I forgot to check my schedule for today and it seems I don't have classes until 10."
    mc "But since I'm here anyway, I thought that I might get some running in. Better than leaving and having to come back an hour later."
    scene 06_379 with Dissolve(1)
    z "Aren't you the model student."
    mc "You know me."
    z "Yeah, exactly... This is so unlike you. At Madison High, you did everything possible to not go to classes and here you are."
    z "Even coming to school when you don't have lessons. Really must be a good day."
    mc "Haha..."
    scene 06_380 with Dissolve(1)
    z "Seems like your schedule isn't the only thing you forget to check."
    mc "What?"
    z "Or maybe you are going commando?"
    mc "Why are you even looking at my butt?"
    scene 06_381 with Dissolve(1)
    x "Haha. That explains why you lost at gay chicken, Zach."
    z "Hey! No, that was... I mean... I have a sensitive dick... Nothing to do with..."
    z "Just shut up or I'll beat your ass later on the field."
    x "Beat my ass? Dude..."
    z "FUCK!"
    mc "{i}(What are they even talking about?){/i}"
    scene 06_382 with Dissolve(1)
    mc "What the fuck is gay chicken?"
    z "It's when two guys are holding each other's dick and the guy who gets hard first loses."
    mc "*Shakes head* I so regret asking..."
    scene 06_383 with Dissolve(1)
    mc "I stayed the night at... someone else's place. Didn't have a change."
    z "Right... The good day. Now I get it. My man!"
    z "But why not wear the one you wore yesterday? Nothing wrong with that."
    z "When they're not dirty, why change? I sometimes wear mine the whole week."
    mc "..."
    if Rachel_End == False:
        if Rachel_Week1_Saturday_Picture == True:
            scene 06_384 with Dissolve(1)
            mc "Speaking about dirty. Remember the picture you sent me?"
            z "Which one? I've sent so many."
            mc "The blonde girl... Who's supposedly your dream girl."
            z "Hmm... Still many. Can't remember a specific one."
            mc "I'm sure I've deleted it, but let me check."
            scene 06_385 with Dissolve(1)
            mc "Hmm... Maybe I didn't... This one here."
            z "Oh... Lovely RayRay."
            mc "{i}(Lovely RayRay?){/i}"
            z "She's hot right?"
            mc "I'm going to delete it now!"
            scene 06_386 with Dissolve(1)
            mc "Where did you get it from?"
            z "That was taken from one of her live shows."
            z "She's a camgirl on MyPlace. Also did some porn a while back."
            scene 06_387 with Dissolve(1)
            z "I can send you a video of her where she puts a huge..."
            mc "I'm good, thanks. *Shakes head*"
            z "Haha..."
            scene 06_388 with Dissolve(1)
            z "Anyway... I gotta go. See you later."
            mc "Later, Zach. Kick some ass!"
            z "Hey!"
            scene 06_389 with Dissolve(1)
            mc "{i}(Well, fuck me...){/i}"
            mc "{i}(Making sure I've actually deleted it now!){/i}"
        else:
            scene 06_388 with Dissolve(1)
            z "Anyway... I gotta go. See you later."
            mc "Later, Zach. Kick some ass!"
            z "Hey!"
    else:
        scene 06_388 with Dissolve(1)
        z "Anyway... I gotta go. See you later."
        mc "Later, Zach. Kick some ass!"
        z "Hey!"
    jump Week2_Wednesday_School_Math

label Week2_Wednesday_School_Math:
    scene black with Dissolve(1)
    pause 2
    scene 06_390 with Dissolve(1)
    n "Wednesday, 10:37. Math class."
    scene 06_391 with Dissolve(1)
    td "Let's continue now with 7.3 Trigonometric Substitution."
    ro "Do you get any of this?"
    scene 06_392 with Dissolve(1)
    mc "Yeah. It isn't that difficult."
    ro "Really? Am I that stupid? I don't understand a thing..."
    scene 06_393 with Dissolve(1)
    td "Let's motivate by trying to solve the following problem..."
    td "We have a circle of radius A..."
    td "And I want to evaluate the marked area, this quarter of the circle."
    td "So... What's the answer?"
    scene 06_394 with Dissolve(1)
    td "..."
    td "No one?"
    menu:
        "Answer[KoGa3AutoWTChange1]{size=-4}(Naomi Week2 Wednesday Math Answer, Naomi Points+2, MC GoodStudent+2) {/size} {/color}":
            $ Naomi_Week2_Wednesday_Math_Answer = True
            $ Naomi_Points += 2
            # Naomi (2)
            $ MC_GoodStudent += 2
            # MC_GoodStudent (14)
            scene 06_395 with Dissolve(1)
            td "Yes, [mc]."
            mc "Area is 1 over 4 pi A squared."
            ro "*Whispers* What the fuck..."
            scene 06_396 with Dissolve(1)
            td "Correct."
            td "Okay. Now we'll keep this in mind and we do it systematically by calculating the area of the following object."
        "Don't answer":
            td "Come on, guys? Really?"
            td "*Sigh*"
            td "Area is 1 over 4 pi A squared."
            td "Now we keep this in mind and we do it systematically by calculating the area of the following object."
    scene black with Dissolve(1)
    pause 2
    scene 06_397 with Dissolve(1)
    if Naomi_Week2_Wednesday_Math_Answer == True:
        ro "Hey, [mc]. How do you even know all that stuff? This is a sports academy."
        mc "Heh... I had a good teacher back in the day."
    else:
        ro "Hey, [mc]. You said earlier that this wasn't so hard, right?"
        mc "Mm-hmm. Her explanation was a little rough, but..."
    ro "*Sigh* I should've never taken advanced math."
    mc "It isn't that bad or..?"
    scene 06_398 with Dissolve(1)
    ro "Man... If only you knew..."
    ro "I hate to ask you this but you really need to help me out."
    ro "Do you have time to tutor me after school? I can pay you."
    mc "Uhm..."
    scene 06_399 with Dissolve(1)
    la "Too late..."
    mc "..."
    scene black with Dissolve(1)
    transform moveup:
        xalign 0.5 yalign 1.0
        linear 5.0 yalign 0.0
    show 06_400 at moveup
    pause 3
    la "He's my tutor already!"
    scene 06_401 with Dissolve(1)
    ro "Yeah, but..."
    la "Let's go!"
    mc "Layla?"
    scene black with Dissolve(1)
    pause 2
    scene 06_402 with Dissolve(1)
    if Layla_Points >= 23:
        mc "Where are you taking me?"
        la "Haha..."
        la "Away from him. You're my private tutor! I won't let him steal you away from me."
        scene 06_403 with Dissolve(1)
        mc "He was going to pay me though..."
        if Layla_Week1_Saturday_Beach_Boobs == True:
            la "Was he?"
            scene 06_404 with Dissolve(1)
            mc "..."
            scene 06_405 with Dissolve(1)
            la "That's your payment!"
            menu:
                "Joke":
                    mc "I'd still rather take the money though..."
                    scene 06_406 with Dissolve(1)
                    la "Hey!"
                    mc "Haha."
                    la "Good to know..."
                    scene 06_407 with Dissolve(1)
                    mc "So you better start saving up. I'm expensive."
                    la "Pfff..."
                    scene 06_408 with Dissolve(1)
                    ""
                "Thanks":
                    mc "Thanks. Payment accepted."
                    mc "Cool."
        else:
            mc "He was going to pay me though..."
            la "I'm much more fun to tutor."
    else:
        mc "Why did you drag me out here?"
        la "You're my private tutor, I won't let him steal you away from me."
        scene 06_403 with Dissolve(1)
        mc "He was going to pay me though..."
        la "I can pay you too. Come..."
    scene 06_409 with Dissolve(1)
    la "I didn't know you were taking advanced math. Are you crazy?"
    mc "Haha... I quite like math."
    la "You do?"
    mc "Uh-huh."
    la "As I said. Crazy!"
    if Erynn_Week1_Stay == False:
        scene 06_410 with Dissolve(1)
        la "So, you were at Melissa's, huh?"
        mc "{i}(How does she?){/i}"
        mc "Uhm... How do you know?"
        scene 06_411 with Dissolve(1)
        la "You've cut your hair. You told me she's your neighbour."
        mc "Right."
        la "I like it."
        mc "Thanks."
    else:
        scene 06_410 with Dissolve(1)
        la "I like the new hair."
        mc "Thanks. Had it cut this morning, actually. My neighbour is a hairstylist."
        la "Oh? That's very practical."
        mc "Sure is."
    scene 06_412 with Dissolve(1)
    mc "What class did you have just now?"
    la "Biology."
    mc "Fun. I like biology."
    scene 06_413 with Dissolve(1)
    la "Not that kind of biology."
    mc "That's not what I meant."
    la "Yeah, right."
    mc "Haha..."
    x "*Clears throat* Ahem..."
    scene 06_414 with Dissolve(1)
    mc "Oh... Good morning, Principal Moore."
    la "..."
    scene black with Dissolve(1)
    transform moveup:
        xalign 0.5 yalign 1.0
        linear 5.0 yalign 0.0
    show 06_415 at moveup
    pause 3
    am "Good morning."
    scene 06_416 with Dissolve(1)
    am "What are you doing here? Shouldn't you be heading towards class?"
    la "I have a free hour."
    am "Do you?"
    la "Yeah, I do!"
    scene 06_417 with Dissolve(1)
    am "You know I'm going to check that."
    la "Go ahead. Check it if you don't believe me."
    scene 06_418 with Dissolve(1)
    am "*Sigh* ..."
    am "Seriously, Layla."
    scene 06_419 with Dissolve(1)
    mc "Damn... Do you always talk to the principal like that?"
    la "Like what?"
    menu:
        "Never mind":
            mc "*Shakes head*"
            mc "Never mind..."
        "Rude[KoGa3AutoWTChange1]{size=-4}(Layla Week2 Wednesday Rude, Layla Points+2) {/size} {/color}":
            $ Layla_Week2_Wednesday_Rude = True
            $ Layla_Points += 2
            # Layla (38)
            scene 06_420 with Dissolve(1)
            mc "You were kinda rude."
            la "..."
            la "Was I?"
            mc "Yeah..."
            scene 06_421 with Dissolve(1)
            la "Sorry..."
            mc "You don't have to apologise to me. Rather to her."
            la "Yeah... You're right. I'll do that next time I see her."
            scene 06_422 with Dissolve(1)
            mc "Don't look so sad now."
            la "Hey! My hair! Haha."
            mc "Haha."
            scene 06_423 with Dissolve(1)
            la "..."
            la "Look what you did! It's a mess..."
            scene 06_424 with Dissolve(1)
            mc "Haha. I think you look cute with your messy hair."
            la "Haha. Yeah?"
            scene 06_425 with Dissolve(1)
            la "Payback!"
            mc "Hey!"
            scene 06_426 with Dissolve(1)
            mc "Haha..."
            la "This is so much fun!"
    scene black with Dissolve(1)
    pause 2
    scene 06_427 with Dissolve(1)
    la "*Yawn*"
    mc "Hehe tired already? It's not even noon..."
    la "It's noon somewhere."
    mc "That's true."
    scene 06_428 with Dissolve(1)
    la "I stayed up too late."
    mc "Doing what?"
    scene 06_429 with Dissolve(1)
    la "Watching a tv show."
    menu:
        "Check her out[KoGa3AutoWTChange1]{size=-4}({i}Layla Points > 27: Layla Points+2{/i}, {i}else: Layla Points-2{/i}) {/size} {/color}":
            if Layla_Points >= 27:
                $ Layla_Points += 2
                # Layla (40)
            else:
                $ Layla_Points -= 2
            show 06_430
            pause 5
            la "What?"
            mc "Nothing."
            la "..."
            scene 06_431 with Dissolve(1)
            la "Oh, before I forget."
        "Don't":
            scene 06_431 with Dissolve(1)
            la "Oh, before I forget."
    la "Do you have time today to help me with Spanish?"
    mc "Sure."
    la "Right after classes?"
    scene 06_432 with Dissolve(1)
    mc "I have detention first."
    la "Yeah, that's right. Stupid Mr Coleman..."
    mc "Hehe. Stupid me, actually, but okay."
    if Layla_Week1_Saturday_Beach_Boobs == True:
        scene 06_433 with Dissolve(1)
        la "Hmm... How about this? I know a good pizza place. Once you're done with detention, we can eat there and then do some Biology."
        mc "Biology? I'm in for that?"
        la "Uh... I meant Spanish... Spanish!"
        mc "Haha."
        la "{i}(How embarrassing!){/i}"
        scene 06_434 with Dissolve(1)
        mc "Yeah. Sounds good. Can't remember last time I had pizza."
        la "I'll text you the address later."
    else:
        scene 06_433 with Dissolve(1)
        la "Hmm... How about this? I know a good pizza place. Once you're done with detention, we can eat there and then do some Spanish."
        mc "Yeah. Sounds good. Can't remember last time I had pizza."
        la "I'll text you the address later."
    scene black with Dissolve(1)
    pause 2
    scene 06_411 with Dissolve(1)
    mc "Shall we head inside before the principal checks up on us again?"
    la "Good idea."
    scene 06_435 with Dissolve(1)
    mc "What?"
    la "Can you help me up?"
    menu:
        "Don't help[KoGa3AutoWTChange1]{size=-4}(Layla Points-4) {/size} {/color}":
            $ Layla_Points -= 4
            scene 06_436 with Dissolve(1)
            mc "Pfff... No!"
            la "..."
            scene 06_437 with Dissolve(1)
            la "How mean."
            la "See you later, then?"
            mc "Yeah. bye, Layla."
            la "Bye..."
        "Help her up[KoGa3AutoWTChange1]{size=-4}(Layla Week2 Wednesday HelpUp, Layla Points+2) {/size} {/color}":
            $ Layla_Week2_Wednesday_HelpUp = True
            $ Layla_Points += 2
            # Layla (42)
            scene 06_438 with Dissolve(1)
            la "Please?"
            mc "{i}(How can you say no to that?){/i}"
            scene 06_439 with Dissolve(1)
            mc "Come on."
            la "Yay!"
            mc "One... two... three!"
            scene 06_440 with Dissolve(1)
            la "Thank you."
            mc "You're welcome."
            scene 06_441 with Dissolve(1)
            la "See you later, then?"
            mc "Yeah. Bye, Layla."
            la "Bye-bye, [mc]."
    jump Week2_Wednesday_Pizzeria

label Week2_Wednesday_Pizzeria:
    scene black with Dissolve(1)
    pause 2
    stop music fadeout 1.0
    play music ("Music/LoFi Italian 1.mp3", "Music/LoFi Italian 2.mp3", "Music/LoFi Italian 3.mp3") volume 0.2
    n "Wednesday, 13:47."
    scene 06_338a with Dissolve(1)
    mc "{i}(This must be it. I can smell the pizza already. So good...){/i}"
    scene 06_339a with Dissolve(1)
    la "Ah, there he is."
    la "Hey, [mc]."
    mc "Hi."
    la "Look who I stumbled into."
    if Alexis_Intro_Ignore == True:
        scene 06_340b with Dissolve(1)
        la "Let me introduce you to my sister. This is..."
        mc "Alexis."
        a "Hi. Uh..."
        scene 06_341a with Dissolve(1)
        la "You know each other?"
        mc "Not really. We saw each other at Dylan's and she's best friends with Erynn. So, we met a few times."
        scene 06_343a with Dissolve(1)
        a "Oh? You are the [mc], Erynn's neighbour from back in the day."
        mc "Exactly."
        a "Yeah, she told me you're back."
        scene 06_354a with Dissolve(1)
        a "Okay. I have to go now. Just stayed out of curiosity."
        la "Can't you stay to eat?"
        a "I have to bring this stuff home."
        scene 06_355a with Dissolve(1)
        a "Thank you very much for helping her, [mc]."
        mc "Sure thing."
        a "Later, Lays."
        la "Bye, Lexi."
        a "And I'll see you around, I guess?"
        mc "Probably, yeah."
        la "Bye-bye."
        mc "Bye."
        jump Week2_Wednesday_Pizzeria_Spanish
    else:
        if Alexis_Sex == True:
            scene 06_342a with Dissolve(1)
            mc "{i}(Oh no. Why is this happening... I don't believe in karma, but this...){/i}"
            scene 06_340a with Dissolve(1)
            la "Let me introduce you to my sister. This is..."
            mc "Alexis."
            a "Hi, [mc]."
            la "You know each other?"
            mc "{i}(Oh shit... Maybe I shouldn't have said anything.){/i}"
            menu:
                "Tell everything[KoGa3AutoWTChange1]{size=-4}(Alexis Week2 Wednesday Tell, Layla Week2 Wednesday Knows, Alexis Week2 Wednesday Breakup, Layla Friends, Alexis Friends, Layla Points-8, Elena Points-8, Alexis Points-8, {i}Alexis Week1 ConcertFalse: Alexis Week2 Wednesday Breakup{/i}) {/size} {/color}":
                    $ Alexis_Week2_Wednesday_Tell = True
                    $ Layla_Week2_Wednesday_Knows = True
                    $ Alexis_Week2_Wednesday_Breakup = True
                    $ Layla_Friends = True
                    $ Alexis_Friends = True
                    $ Layla_Points -= 8
                    $ Elena_Points -= 8
                    $ Alexis_Points -= 8
                    scene 06_341_01a with Dissolve(1)
                    mc "Yeah, we used to hook up."
                    scene 06_344a with Dissolve(1)
                    la "Haha. You're funny."
                    a "..."
                    scene 06_345a with Dissolve(1)
                    mc "What?"
                    mc "I'm not lying to her as you did."
                    a "I never lied to her. I didn't know it was you!"
                    la "Uh, guys?"
                    scene 06_346a with Dissolve(1)
                    la "Lexi, what's going on?"
                    a "I'm so sorry, Lays."
                    la "Wait? You're not joking?"
                    a "..."
                    scene 06_347a with Dissolve(1)
                    if Layla_Points >= 29:
                        la "Oh my god..."
                        la "The one time I like a guy?"
                    else:
                        la "Oh my god..."
                    a "I didn't know it was him... You never told me his name."
                    la "You never told me you were seeing someone either."
                    a "Lays, please..."
                    scene 06_348a with Dissolve(1)
                    la "And why didn't you tell me you're dating my sister?"
                    mc "Uh... We weren't dating and I didn't know she was your sister."
                    mc "That's why I'm telling you right now..."
                    scene 06_349a with Dissolve(1)
                    a "Layla?"
                    mc "Where are you going, Layla? What about Spanish."
                    la "I don't care about stupid Spanish."
                    if Alexis_Week1_Concert == False:
                        scene 06_350a with Dissolve(1)
                        a "Couldn't you let her stay out of it? Or not tell her this way, at least?"
                        a "Yes, we hooked up in the past. But that's... In the past."
                        if Layla_Points >= 29:
                            a "She likes you, don't you like her?"
                            mc "..."
                        else:
                            mc "..."
                        scene 06_351a with Dissolve(1)
                        a "*Sigh*"
                        a "I hope you're happy!"
                    else:
                        $ Alexis_Week2_Wednesday_Breakup = True
                        scene 06_350a with Dissolve(1)
                        a "I know you're mad at me. And I deserve that, it's all my fault. But this..."
                        a "This wasn't necessary. At least not in this way..."
                        if Layla_Points >= 29:
                            a "She likes you, don't you like her?"
                            mc "..."
                        else:
                            mc "..."
                        scene 06_351a with Dissolve(1)
                        a "*Sigh*"
                        a "I hope you're happy! We're done!"
                    scene 06_352a with Dissolve(1)
                    mc "{i}(Fuck...){/i}"
                    mc "{i}(She's actually right. This wasn't the place and time.){/i}"
                    mc "{i}(And surely not the way I did it.){/i}"
                    mc "*Sigh*"
                    mc "{i}(I should apologise. I guess I'll stop by Dylan's bar once I'm done helping Mom at the restaurant.){/i}"
                    mc "{i}(I'd better try calling Layla too...){/i}"
                    jump Week2_Wednesday_Dylansbar
                "Leave out details":
                    scene 06_341_02a with Dissolve(1)
                    mc "We met a few times. On the plane, at Dylan's, and she's best friends with Erynn."
                    a "That's right. We run into each other quite often."
                    mc "We do, huh?"
                    a "Yeah, funny..."
                    if Alexis_Friends == True:
                        scene 06_354a with Dissolve(1)
                        a "Okay. I have to go now. Just stayed out of curiosity."
                        la "Can't you stay to eat?"
                        a "I have to bring this stuff home."
                        scene 06_355a with Dissolve(1)
                        a "Thank you very much for helping her, [mc]."
                        mc "Sure thing."
                        a "Later, Lays."
                        la "Bye, Lexi."
                        a "And I'll see you around, I guess?"
                        mc "Probably, yeah."
                        a "*Whisper* You'll need to tell her at some point..."
                        mc "{i}(I know...){/i}"
                        la "Bye-bye."
                        mc "Bye."
                        jump Week2_Wednesday_Pizzeria_Spanish
                    else:
                        scene 06_343b with Dissolve(1)
                        la "Come sit down."
                        a "..."
                        mc "..."
                        scene black with Dissolve(1)
                        pause 2
                        scene 06_353a with Dissolve(1)
                        mc "{i}(Why did I sit down next to her?){/i}"
                        mc "{i}(This is so awkward...){/i}"
                        scene 06_356a with Dissolve(1)
                        la "Did you have fun in detention?"
                        mc "It was so much fun. Especially since Darryl was there too."
                        la "Really? Haha. Unlucky."
                        mc "Tell me about it."
                        scene 06_357a with Dissolve(1)
                        a "Who's Darryl?"
                        la "He's a member of the track team. He thinks he's the second coming of Usain Bolt."
                        mc "Haha, so true."
                        a "Oh..."
                        a "{i}(My heart is beating so fast.){/i}"
                        a "{i}(Does he like Layla?){/i}"
                        a "{i}(*Sigh* Why am I even staying. I should just go. But...){/i}"
                        scene 06_358a with Dissolve(1)
                        mc "I see you did some shopping before, huh?"
                        la "No-no, not me. That was Lexi."
                        mc "Okay."
                        la "Yeah, she has to do all kinds of housework as punishment."
                        scene 06_359a with Dissolve(1)
                        a "Layla!"
                        mc "Punishment?"
                        la "She took Dad's car without permission and went somewhere. She didn't come home until the next day."
                        a "Layla, please stop. It's none of his business..."
                        mc "{i}(Was that the day of the concert?){/i}"
                        mc "{i}(She told me she couldn't stay multiple times. I guess it's my fault.){/i}"
                        scene 06_360a with Dissolve(1)
                        mc "*Whisper* Sorry."
                        a "Uh..."
                        a "{i}(It's not your fault.){/i}"
                        scene 06_361a with Dissolve(1)
                        la "Shall we order something?"
                        mc "Yeah. I'm pretty hungry. Haven't had anything yet today."
                        la "Let me use the ladies' room real quick. I'll bring the menu back with me."
                        mc "Okay."
                        la "Be right back."
                        if Layla_Week1_Saturday_Beach_Boobs == True:
                            scene 06_362a with Dissolve(1)
                            la "Don't be mean, and please don't interview him."
                            a "Just go..."
                            la "Haha."
                        else:
                            pass
                        scene black with Dissolve(1)
                        pause 2
                        scene 06_363a with Dissolve(1)
                        a "..."
                        a "Hey, how are you?"
                        mc "No. No, Alexis. We are not doing this today."
                        scene 06_364a with Dissolve(1)
                        a "Can we please talk? I want to explain."
                        mc "*Sigh*"
                        a "Please, [mc]."
                        menu:
                            "I've heard enough[KoGa3AutoWTChange1]{size=-4}(Alexis Friends, Alexis Week2 Wednesday Breakup, Alexis Points-8) {/size} {/color}":
                                $ Alexis_Friends = True
                                $ Alexis_Week2_Wednesday_Breakup = True
                                $ Alexis_Points -= 8
                                scene 06_366a with Dissolve(1)
                                mc "I've heard enough already."
                                mc "We are done, Alexis!"
                                a "..."
                            "Talk":
                                mc "Okay. Talk..."
                                a "Not here. Can we meet up later? I'll text you."
                        scene black with Dissolve(1)
                        pause 2
                        scene 06_367a with Dissolve(1)
                        la "I'm back with the menus."
                        la "I hope you guys behaved..."
                        scene 06_368a with Dissolve(1)
                        la "Do you have any idea what you're going to order?"
                        a "Well, I'll be going actually."
                        la "What? Can't you stay to eat, Lex?"
                        a "I have to bring the groceries home and then I have to do some other stuff."
                        la "Hmm alright..."
                        if Alexis_Friends == True:
                            scene 06_369a with Dissolve(1)
                            a "Thank you very much for helping her, [mc]."
                            mc "Yeah. No problem."
                            scene 06_370a with Dissolve(1)
                            a "Bye guys."
                            la "See you later."
                            a "*Whisper* You'll need to tell her at some point..."
                            mc "{i}(I know...){/i}"
                            mc "Bye..."
                            jump Week2_Wednesday_Pizzeria_Spanish
                        else:
                            scene 06_369a with Dissolve(1)
                            a "Thank you very much for helping her, [mc]."
                            mc "Yeah. No problem."
                            menu:
                                "Don't help[KoGa3AutoWTChange1]{size=-4}(Alexis Friends, Alexis Week2 Wednesday Breakup, Alexis Points-4) {/size} {/color}":
                                    $ Alexis_Friends = True
                                    $ Alexis_Week2_Wednesday_Breakup = True
                                    $ Alexis_Points -= 4
                                    scene 06_370a with Dissolve(1)
                                    a "Bye guys."
                                    la "See you later."
                                    a "*Whisper* You'll need to tell her at some point..."
                                    mc "{i}(I know...){/i}"
                                    mc "Bye..."
                                    jump Week2_Wednesday_Pizzeria_Spanish
                                "Help her[KoGa3AutoWTChange1]{size=-4}(Alexis Points+2) {/size} {/color}":
                                    $ Alexis_Points += 2
                                    # Alexis (28)
                                    scene 06_371a with Dissolve(1)
                                    mc "Wait... I'll help you out."
                                    a "Uh? You don't have to..."
                                    mc "They look heavy."
                                    a "Thank you."
                                    scene 06_372a with Dissolve(1)
                                    a "See you later, Lays."
                                    la "Bye, Lexi."
                                    mc "I'll be right back, Layla."
                                    la "Okay. Should I order for you, already? Do you know what you want?"
                                    mc "Uhm, yeah sure. I'll have a pepperoni pizza."
                                    la "Okay."
                                    jump Week2_Wednesday_Alexis_Help
        else:
            scene 06_340b with Dissolve(1)
            la "Let me introduce you to my sister. This is..."
            mc "Alexis."
            a "Hi, [mc]."
            scene 06_341a with Dissolve(1)
            la "You know each other?"
            mc "We met a few times. On the plane, at Dylan's, and she's best friends with Erynn."
            scene 06_343a with Dissolve(1)
            a "That's right. We run into each other quite often."
            mc "We do, huh?"
            a "Yeah, funny..."
            scene 06_354a with Dissolve(1)
            a "Okay. I have to go now. Just stayed out of curiosity."
            la "Can't you stay to eat?"
            a "I have to bring this stuff home."
            scene 06_355a with Dissolve(1)
            a "Thank you very much for helping her, [mc]."
            mc "Sure thing."
            a "Later, Lays."
            la "Bye, Lexi."
            a "And I'll see you around, I guess?"
            mc "Probably, yeah."
            la "Bye-bye."
            mc "Bye."
            jump Week2_Wednesday_Pizzeria_Spanish

label Week2_Wednesday_Alexis_Help:
    scene black with Dissolve(1)
    pause 2
    stop music fadeout 1.0
    play music "Music/Valeria - Emptiness.mp3" volume 0.6
    scene 06_373a with Dissolve(1)
    ""
    scene 06_374a with Dissolve(1)
    a "{i}(Should I talk to him now?){/i}"
    a "..."
    a "Uhm..."
    mc "..."
    scene 06_375a with Dissolve(1)
    a "{i}(Why am I so scared?){/i}"
    a "..."
    scene black with Dissolve(1)
    pause 2
    scene 06_376a with Dissolve(1)
    a "Thank you, [mc]."
    mc "Sure."
    scene 06_377a with Dissolve(1)
    mc "..."
    a "Sorry."
    a "..."
    a "I never expected this to happen..."
    a "From the first moment I saw you on the plane, I was attracted to you."
    scene 06_378a with Dissolve(1)
    a "The cute guy who was asleep on the plane next to my seat."
    mc "..."
    scene black with Dissolve(2)
    pause 2
    n "Two weeks ago."
    scene 01_003 with Dissolve(1)
    a "{i}(Is he sleeping?){/i}"
    a "{i}(I'm sorry I have to wake you up.){/i}"
    scene 01_004 with Dissolve(1)
    a "Uhm... Excuse me?"
    scene 01_005 with Dissolve(1)
    a "{i}(Oh. He's cute.){/i}"
    a "Hi."
    scene black with Dissolve(2)
    pause 2
    scene 06_380a with Dissolve(1)
    a "I didn't know who you were at first."
    a "And when we started talking, I felt an immediate connection. I had so much fun. You even made me forget I was on a plane."
    scene 06_381a with Dissolve(1)
    a "But once you told me the story about Erynn, my heart dropped. I remembered you immediately."
    a "I couldn't believe that it was you. You could've been anyone, just a random encounter. But you were Erynn's childhood friend..."
    scene 06_381b with Dissolve(1)
    mc "Why didn't you just tell me who you were back then?"
    a "I don't know... I liked the way you looked at me and how comfortable you made me feel."
    a "And I was scared you'd change your opinion of me or treat me differently when you knew."
    mc "..."
    mc "To be fair. I probably would have."
    a "..."
    scene 06_382a with Dissolve(1)
    a "I knew I was betraying Erynn's friendship, that's why I left the plane without saying anything."
    a "But I regretted it almost immediately. I wanted to see you again, to get to know you."
    scene black with Dissolve(2)
    pause 2
    n "Two weeks ago. MS Airport."
    scene 06_379_01a with Dissolve(1)
    a "{i}(Is he coming out?){/i}"
    a "{i}(Why didn't I just talk to him?){/i}"
    a "..."
    scene 06_379_02a with Dissolve(1)
    a "{i}(What am I doing here? He's Erynn's friend.){/i}"
    a "{i}(I shouldn't...){/i}"
    a "{i}(I should leave, right? This is...){/i}"
    a "..."
    a "{i}(Two more minutes... Three...){/i}"
    scene black with Dissolve(2)
    pause 2
    scene 06_382a with Dissolve(1)
    a "You can't believe how happy I was when we met again in the bar. I just couldn't say no anymore to the feelings I had..."
    a "Have... for you."
    a "The times we spent together since then were just amazing."
    a "This will sound stupid but, I missed you the days we didn't see each other."
    scene 06_383a with Dissolve(1)
    a "I wanted to tell you many times. I was just so afraid it would end badly. I didn't want it to end. So it was always one more day, just one more day."
    a "And because of my hesitation, I made it even worse."
    a "I even lied to Erynn. I've never lied to her. She'll probably never forgive me for this."
    a "She was actually the one who was supposed to go to the concert with me. But I lied to her, telling her I couldn't go. Because I wanted to spend one more day with you."
    scene 06_384a with Dissolve(1)
    a "The day you found out, was actually the day I wanted to talk to Erynn about us."
    a "I needed to tell her first before I told you."
    a "She'd been my best friend for a long time, so she deserved to know."
    a "But as you know, it didn't work out like that."
    scene 06_385a with Dissolve(1)
    a "We met too, before. A few times actually."
    mc "Yeah... I remember."
    a "Erynn always talked about you, you know. I was always jealous of her. Even though she doesn't have any siblings, she had this amazing friendship and bond with you. That's something I always wanted."
    mc "You have a sister."
    a "I know. I love Layla. But back then, we didn't have the relationship we have now."
    a "We weren't close. We went to separate schools, had different friends, different hobbies. We never hung out together except at the dinner table."
    a "Now we talk about everything."
    scene 06_386a with Dissolve(1)
    mc "Almost everything. Seems like you didn't tell her about me or us. She still doesn't know."
    a "..."
    scene 06_387a with Dissolve(1)
    a "I wanted to tell her, many times. But then she told me about a boy she met at school."
    a "It was the first time she actually talked with me about boys. She always sounded happy when talking about him."
    a "I didn't want to usurp her happiness with mine."
    a "She always started with, 'The boy from the track team' and then continued on. I never asked his name. I thought she would tell me when she was ready."
    a "Maybe I should've asked her. Then I would've known we were talking about you."
    scene 06_388a with Dissolve(1)
    mc "And then what?"
    mc "Stop how you are feeling? You couldn't do it for Erynn. Which I still don't get, actually. What has Erynn got to do with... us?"
    a "You'll understand once you talk to her. I can't even count the hours she talked about you. The moment she found out you were back, she... You just had to see it."
    mc "..."
    scene 06_389a with Dissolve(1)
    a "I have to tell Layla though. Or the same thing will happen, what happened with Erynn."
    a "I lost her, I lost you... I can't lose Layla."
    a "I don't want to make the same mistakes again..."
    scene 06_390a with Dissolve(1)
    mc "What do you mean you lost Erynn? Aren't you friends?"
    a "She ended our friendship."
    mc "..."
    scene 06_391a with Dissolve(1)
    mc "{i}(Why would she do that?){/i}"
    mc "{i}(Does Erynn know about Alexis and me?){/i}"
    mc "{i}(Is that why she behaved so strangely yesterday?){/i}"
    mc "{i}(I really should talk to her.){/i}"
    scene 06_392a with Dissolve(1)
    a "And that's why I really need to talk with Layla, [mc]."
    mc "I'll talk to her..."
    a "But..."
    mc "No. Please let me, Lexi... Alexis."
    a "..."
    mc "Now is not the right time though. We have an important Spanish test coming up and she can't fail that one or she'll fail the whole semester."
    scene 06_393a with Dissolve(1)
    a "What? I thought she was doing good at her studies. What happened?"
    mc "{i}(Maybe that Lucas guy has something to do with it? Does Alexis know about him?){/i}"
    mc "I don't know, but I agreed to help and tutor her."
    scene 06_394a with Dissolve(1)
    a "Please do. Thank you so much, [mc]."
    a "Well uhm... I'm going to leave then, so you can help her study."
    mc "Yeah."
    a "Thank you for listening and letting me explain."
    scene 06_395a with Dissolve(1)
    a "After all this, I really hope we can be friends one day."
    a "I never wanted to hurt anyone. I'm so sorry, I was just..."
    menu:
        "Let her go[KoGa3AutoWTChange1]{size=-4}(Alexis Points-2) {/size} {/color}":
            $ Alexis_Points -= 2
            mc "Yeah, I understand."
            scene 06_396a with Dissolve(1)
            a "Bye, [mc]."
            mc "Bye, Alexis."
        "Stop her[KoGa3AutoWTChange1]{size=-4}(Alexis Points+2) {/size} {/color}":
            $ Alexis_Points += 2
            # Alexis (30)
            scene 06_397a with Dissolve(1)
            mc "Apology accepted. Besides, I'm sorry too. The way I reacted towards you wasn't my greatest moment."
            mc "This isn't your fault. I should've let you explain back then."
            a "..."
            scene 06_398a with Dissolve(1)
            a "Stop! Don't be nice to me. I don't deserve that."
            mc "You deserve more than that, Lexi..."
            a "Please, let me go."
            scene 06_399a with Dissolve(1)
            mc "Lexi!"
            a "No, [mc]. We... This..."
            a "This is goodbye."
            mc "But..."
            a "No. We can't..."
            scene 06_400a with Dissolve(1)
            a "Goodbye, [mc]."
            mc "..."
            mc "Bye..."
            scene 06_401a with Dissolve(1)
            a "*Crying*"
    scene black with Dissolve(1)
    pause 2
    scene 06_402a with Dissolve(1)
    mc "{i}(Fuck!){/i}"
    mc "{i}(But... Maybe it's for the better? I don't know. Fuck...){/i}"
    mc "..."
    mc "*Sigh*"
    mc "{i}(Come on. Get your head straight, [mc]. Let's help out Layla. That's the priority for today.){/i}"
    scene black with Dissolve(1)
    pause 2
    stop music fadeout 1.0
    play music ("Music/LoFi Italian 1.mp3", "Music/LoFi Italian 2.mp3", "Music/LoFi Italian 3.mp3") volume 0.2
    scene 06_403a with Dissolve(1)
    la "Hey, you're back! I scooted over so you can sit next to me."
    mc "Hehe, thanks."
    scene 06_404a with Dissolve(1)
    la "Thank you, [mc]. For helping her."
    mc "No problem."
    la "She's gorgeous, isn't she?"
    menu:
        "Yes":
            mc "Yes, she's very pretty."
        "So are you[KoGa3AutoWTChange1]{size=-4}(Layla Points+2) {/size} {/color}":
            $ Layla_Points += 2
            # Layla (44)
            scene 06_405a with Dissolve(1)
            mc "Yeah, very pretty, just like her sister."
            la "Hehe... Thanks."
        "Don't answer":
            mc "..."
    scene 06_406a with Dissolve(1)
    la "She's been behaving weirdly though the last few days."
    mc "Yeah? How so?"
    scene 06_407a with Dissolve(1)
    la "First, she was so happy. I've never seen her that way."
    la "I actually caught her skipping around the house."
    la "Oh... And singing. She has a really good voice, but she never sings when people are around."
    la "For some reason, she didn't care who heard her. She sang the same song over and over again. 'Cause nothing compares...' You know it?"
    mc "Uh... Yeah. I've heard it a few times."
    mc "..."
    scene 06_408a with Dissolve(1)
    la "But then it changed. Now she behaves the complete opposite and looks sad most of the time."
    la "I think she met someone and something must have happened."
    mc "Hmm..."
    la "I asked her, but she didn't want to talk about it."
    mc "..."
    mc "{i}(Dammit, Alexis...){/i}"
    jump Week2_Wednesday_Pizzeria_Spanish

label Week2_Wednesday_Pizzeria_Spanish:
    $ Layla_Week2_Wednesday_SpanishHelp = True
    scene black with Dissolve(1)
    pause 2
    scene 06_409a with Dissolve(1)
    mc "This smells so good."
    la "Doesn't it?"
    scene 06_410a with Dissolve(1)
    mc "Well, buen provecho!"
    la "Hey! We didn't start with Spanish yet."
    mc "Of course we did."
    scene black with Dissolve(1)
    pause 2
    scene 06_411a with Dissolve(1)
    la "Haah... I'm full. That was so good."
    mc "It was great!"
    la "Best place to have pizza."
    mc "You have a piece left though."
    scene 06_412a with Dissolve(1)
    la "Yeah, I can't finish it."
    la "Do you want it?"
    mc "If you aren't going to eat it, I'll have it, thanks."
    la "Hehe."
    if Layla_Points >= 34:
        scene 06_414a with Dissolve(1)
        la "Here you go. Say aaah..."
        mc "..."
        scene 06_415a with Dissolve(1)
        la "Come on. You want it or not?"
        la "Aaah..."
        scene 06_416a with Dissolve(1)
        la "Hahaha."
        mc "You are ridiculous."
        scene 06_417a with Dissolve(1)
        la "I know..."
    else:
        scene 06_413a with Dissolve(1)
        la "Here you go."
        mc "Thank you."
    scene black with Dissolve(1)
    pause 2
    scene 06_418a with Dissolve(1)
    mc "Ready to do some Spanish?"
    la "No. Do we really have to?"
    mc "Isn't that the reason we're here?"
    la "..."
    mc "Come on. It won't be that bad. I'll make it fun."
    la "*Sigh* Okay..."
    scene black with Dissolve(1)
    pause 2
    scene 06_419a with Dissolve(1)
    ""
    scene 06_420a with Dissolve(1)
    ""
    scene black with Dissolve(1)
    pause 2
    scene 06_421a with Dissolve(1)
    la "But the one thing I don't get is this here."
    la "Why do they use tranquilo here and in this example, they use tranquila."
    la "Shouldn't it be the same?"
    scene 06_422a with Dissolve(1)
    mc "No. When you talk to a girl it's tranquila, when talking to a boy, it's tranquilo."
    la "Oh? That isn't that difficult then."
    la "So it changes depending on who you talk to."
    mc "Exactly."
    menu:
        "Check her out[KoGa3AutoWTChange1]{size=-4}({i}Layla Points > 34: Layla Week2 Wednesday CheckOut{/i}) {/size} {/color}":
            if Layla_Points >= 34:
                $ Layla_Week2_Wednesday_CheckOut = True
                if Alexis_Sex == False:
                    scene 06_423a with Dissolve(1)
                    ""
                else:
                    scene 06_423a with Dissolve(1)
                    mc "{i}(They are bigger than Alexis's I think.){/i}"
                    mc "..."
                    mc "{i}(Why am I even comparing them?){/i}"
                scene 06_424a with Dissolve(1)
                mc "..."
                scene 06_425a with Dissolve(1)
                la "Hey!"
                mc "Uh?"
                la "Spanish remember? Not Biology..."
                if Layla_Week1_Saturday_Beach_Boobs == True:
                    scene 06_426a with Dissolve(1)
                    mc "Who's fault is that, you think? You showed them to me. Now I can't get them out of my mind..."
                    la "..."
                    mc "Sorry."
                    la "I don't mind."
                else:
                    scene 06_426a with Dissolve(1)
                    la "..."
                    mc "Sorry."
                    la "I don't mind."
                scene 06_427a with Dissolve(1)
                $ Layla_Week2_Wednesday_Chichis = True
                la "How do you say boobs in Spanish?"
                mc "Uh... Tetas."
                la "Tetas? That doesn't sound cute at all."
                mc "Well, you could say chichis..."
                scene 06_428a with Dissolve(1)
                la "Hehe chichis, that's funny. And sounds much better than tetas."
                la "How do you say can I kiss you in Spanish?"
                scene 06_429a with Dissolve(1)
                mc "Puedo besarte?"
                la "Sí..."
                mc "..."
                menu:
                    "Kiss her[KoGa3AutoWTChange1]{size=-4}(Layla Points+2) {/size} {/color}":
                        $ Layla_Points += 2
                        # Layla (46)
                        scene 06_431a with Dissolve(1)
                        ""
                        scene 06_432a with Dissolve(1)
                        ""
                        scene 06_433a with Dissolve(1)
                        mc "You taste like pizza."
                        la "..."
                    "Don't kiss":
                        if Alexis_Friends == True:
                            scene 06_430a with Dissolve(1)
                            mc "Nice try, I'll give you that."
                            la "..."
                        else:
                            scene 06_430a with Dissolve(1)
                            mc "Nice try, I'll give you that."
                            la "..."
                            mc "{i}(I shouldn't... Especially after what happened with Alexis...){/i}"
                scene 06_434a with Dissolve(1)
                mc "Quieres seguir con esto o aprender más español?\n(Do you want to continue with this, or learn more Spanish?)"
                la "Uh... What now?"
                scene 06_435a with Dissolve(1)
                mc "Spanish it is. Let's continue our lesson."
                la "What did you just say?"
                mc "Okay, where were we?"
                la "..."
            else:
                $ Layla_Points -= 2
                scene 06_423a with Dissolve(1)
                ""
                scene 06_425a with Dissolve(1)
                la "What are you doing?"
                mc "Nothing... Sorry."
                la "Uh-huh..."
        "Don't":
            pass
    scene black with Dissolve(1)
    pause 2
    scene 06_436a with Dissolve(1)
    la "I can't anymore. This is enough for one day."
    mc "Yeah, I agree. You did well though."
    la "You think? I'm not so sure."
    la "I understand it now, but it's still some days until the test on Monday."
    mc "You'll be fine."
    scene 06_437a with Dissolve(1)
    la "Can we do this again? I might need a refresher. Like some time this weekend?"
    mc "Uhm..."
    if Nikki_FB_Choose == True:
        if Nikki_Week2_Tuesday_Phonecall == True:
            mc "{i}(The weekend... The wedding!){/i}"
            mc "{i}(That reminds me, I still need to give Nikki a call){/i}"
            la "How about Sunday, in the evening?"
        else:
            la "How about Sunday, in the evening?"
    else:
        if Cara_FB_Choose == True:
            if Cara_Week2_Tuesday_Phonecall == True:
                mc "{i}(The weekend... The wedding!){/i}"
                mc "{i}(That reminds me, I still need to give Cara a call){/i}"
                la "How about Sunday, in the evening?"
            else:
                la "How about Sunday, in the evening?"
        else:
            la "How about Sunday, in the evening?"
    mc "Okay. I think I can make that."
    la "Cool. I'll let you know later where we can meet."
    mc "Sounds good. Let's get going then, yeah?"
    scene 06_438a with Dissolve(1)
    la "Thank you so much, [mc]. I really appreciate this."
    mc "Anytime, Layla."
    mc "See you."
    la "Bye-bye."
    jump Week2_Wednesday_Dylansbar

label Week2_Wednesday_Dylansbar:
    scene black with Dissolve(1)
    pause 2
    stop music fadeout 1.0
    play music "Sounds/Bar_Background.mp3" volume 0.3
    n "Wednesday, 20:02."
    scene 06_439a with Dissolve(1)
    mc "Hey there, Dylan."
    bd "Hi, [mc]. How are you?"
    mc "Exhausted. Long day..."
    bd "Haha. I see."
    scene 06_440a with Dissolve(1)
    if Alexis_Week2_Wednesday_Tell == True:
        mc "Alexis not here?"
        bd "No. She took the day off."
        mc "Hmm okay..."
        mc "{i}(Guess I have to apologise another day.){/i}"
    else:
        pass
    bd "What can I get you?"
    mc "A beer, please."
    bd "Coming right up."
    scene black with Dissolve(1)
    pause 2
    scene 06_441a with Dissolve(1)
    bd "Here you go."
    mc "Thanks, man."
    scene 06_442 with Dissolve(1)
    mc "Slow night?"
    bd "No, no, this is just the calm before the storm."
    bd "The game is on tonight, it will be packed soon."
    mc "Right. I almost forgot."
    bd "..."
    bd "I could use your help with something though."
    scene 06_443 with Dissolve(1)
    mc "Uhm... Okay?"
    bd "I invented this new grilling technique. Makes the meat juicier and more flavourful. It's amazing."
    mc "Sounds amazing."
    bd "Yeah, let me tell you. You'll be blown away."
    mc "How about I try it next time? I don't have much cash on me today."
    scene 06_444 with Dissolve(1)
    bd "Don't worry about it. It's on the house."
    bd "I'll use you as some sort of test subject, you know."
    mc "You're not poisoning me, are you?"
    bd "You're a good customer. I would never..."
    scene 06_445 with Dissolve(1)
    mc "What happens to bad customers?"
    bd "Haha..."
    mc "..."
    mc "Anyway. I won't say no to free food."
    bd "Great."
    scene black with Dissolve(1)
    pause 2
    scene 06_446 with Dissolve(1)
    mc "{i}(Hmm... Tastes the same as last time. But still great.){/i}"
    bd "So? What do you think?"
    mc "{i}(What should I tell him?){/i}"
    menu:
        "Be honest":
            scene 06_447a with Dissolve(1)
            mc "It's good. But it tastes the same as last time."
            bd "Really? Hmm... Might have done something wrong then."
            mc "It's probably me... What do they always say on those cooking shows? Sophisticated palate or something."
            mc "Yeah, I don't have that."
            bd "Hehe... Thanks for the feedback."
            mc "Anytime."
        "Say it's great":
            scene 06_447 with Dissolve(1)
            if Alexis_Friends == True:
                mc "Damn Dylan. This is amazing."
                bd "Haha... Told you!"
            else:
                mc "Damn Dylan. This is amazing."
                bd "Haha... Told you!"
                mc "You'll make a great husband one day with those cooking skills."
                scene 06_448 with Dissolve(1)
                bd "{i}(Husband? Did he just propose to me?){/i}"
                bd "{i}(See Alexis, I told you he likes me...){/i}"
                bd "You're a funny guy."
    scene 06_449 with Dissolve(1)
    x "Hey, Dylan."
    bd "Oh... Good evening, Mr Navarro."
    bd "The usual?"
    scene 06_450 with Dissolve(1)
    sn "No, not this time. I'll have a coffee. Black."
    bd "Still on the clock?"
    sn "When ain't I?"
    bd "Haha, true."
    scene 06_451 with Dissolve(1)
    sn "Don't tell me the TV is broken..."
    bd "No, it works. The game hasn't started yet. But I'll put it on for you."
    bd "I know you like those sports debates."
    sn "Thanks."
    scene 06_452 with Dissolve(1)
    bd "How is Silva doing?"
    sn "Still a pain in the ass."
    bd "He's making shots though, especially from three."
    sn "He'd better be, after the contract I negotiated for him."
    bd "True. I'll get you your coffee."
    sn "Thanks."
    scene black with Dissolve(1)
    pause 2
    scene 06_453 with Dissolve(1)
    sn "Hey."
    mc "{i}(Is he talking to me?){/i}"
    mc "Hi."
    sn "The steaks here are great, huh?"
    mc "They are. Dylan invented this new grilling technique."
    scene 06_454 with Dissolve(1)
    sn "Haha, new technique... He's been saying that for the last ten years."
    sn "Really now, how many ways can you cook a steak? Put some salt and pepper on it and throw it on the grill, et voila..."
    bd "Hey, hey! No spilling secrets!"
    scene 06_455 with Dissolve(1)
    bd "Here, your coffee. No salt, no pepper!"
    sn "Just how I like it."
    mc "Haha..."
    scene black with Dissolve(1)
    pause 2
    scene 06_456 with Dissolve(1)
    sn "Do you watch basketball?"
    mc "Yes, I do."
    sn "Who's your team?"
    mc "Marauders, of course."
    sn "Good man."
    scene 06_457 with Dissolve(1)
    sn "Do you play?"
    mc "Recreationally. I'm too short to play professionally."
    scene 06_458 with Dissolve(1)
    sn "Hmm... What are you? Six-one, six-two?"
    mc "Six-one, yes."
    sn "Okay. If you're a good ball handler and can shoot the three-ball, you should be fine with all the small ball they're playing nowadays."
    mc "Maybe yeah, but I'd rather stick to track."
    sn "Track and field? Interesting."
    scene black with Dissolve(1)
    pause 2
    scene 06_459 with Dissolve(1)
    sn "Oh... Come on!"
    mc "Come on."
    sn "..."
    sn "If you can't score an easy lay-up, just get off the court, right?"
    mc "True."
    sn "*Sigh* What's the coach doing?"
    sn "I think I need to make some calls again..."
    if Andres_FB_Punch == True:
        play sound "Sounds/Phone_Vibrate.mp3"
        n "*Bzzzt. Bzzzt*"
        scene 06_460 with Dissolve(1)
        mc "{i}(Oh? It's Erynn...){/i}"
        mc "{i}(I'd better take this outside.){/i}"
        jump Week2_Wednesday_Erynn_Call
    else:
        if Nikki_FB_Choose == True:
            jump Week2_Wednesday_Nikki_Call
        else:
            jump Week2_Wednesday_Cara_Call

label Week2_Wednesday_Nikki_Call:
    if Nikki_Week2_Tuesday_Phonecall == True:
        scene black with Dissolve(1)
        pause 2
        scene 06_460 with Dissolve(1)
        mc "{i}(Oh shit! It's that late already. I'd better call Nikki now.){/i}"
        scene 06_461 with Dissolve(1)
        mc "Hey, Nikki."
        mc "How are you?"
        ni "Sorry, I can't hear you."
        scene 06_462 with Dissolve(1)
        mc "Wait. I'm in a bar, I'll go outside."
        ni "Okay."
        scene black with Dissolve(1)
        pause 2
        stop music fadeout 1.0
        play music "Sounds/Street_Traffic.mp3" volume 0.3
        scene 06_463 with Dissolve(1)
        mc "Better?"
        ni "Yes! Hi."
        mc "Hey, how are you?"
        scene 06_464 with Dissolve(1)
        ni "I'm good. How are you?"
        mc "Better than the last few days."
        mc "Sorry I'm calling so late. I was watching the game and it totally slipped my mind."
        scene 06_465 with Dissolve(1)
        ni "No worries. I would've called if I didn't hear from you in the next hour."
        mc "Sorry again."
        ni "So, you're out drinking on a Wednesday?"
        scene 06_471 with Dissolve(1)
        mc "Yeah. Wasn't planned though. Just wanted a beer tonight."
        ni "Long day?"
        mc "You could say that. Very busy. What are you doing?"
        scene 06_466 with Dissolve(1)
        ni "Just came home from work. Going to watch some TV and then off to bed."
        ni "Anyway. Have you decided? You're coming right?"
        mc "Yeah. There's something I need to talk about with... Dad."
        mc "{i}(And I need to talk to you.){/i}"
        ni "Great. You didn't really have a choice anyway. We booked the ticket already."
        scene 06_472 with Dissolve(1)
        mc "Haha. Okay. Thanks."
        mc "Can't wait to see you again."
        ni "Me too."
        ni "Aaah..."
        mc "What?"
        scene 06_467 with Dissolve(1)
        ni "I don't know why I'm getting nervous all of a sudden."
        mc "Haha."
        mc "So, when's the flight?"
        ni "Friday. I'll send you the details. You'll be arriving here late afternoon. The wedding is Saturday."
        mc "Will be a busy weekend, huh?"
        ni "Yeah. Preparations are in full swing already."
        scene 06_468 with Dissolve(1)
        ni "Well. I'll leave you be, so you can continue watching... the game. Whatever game it is."
        mc "Haha. Thanks."
        ni "I'm really happy you're coming."
        mc "Me too."
        ni "See you Friday then. I'll come to pick you up at the airport."
        mc "Thanks. See you then. Bye, Nikki."
        ni "Bye, [mc]."
        scene 06_469 with Dissolve(1)
        ni "..."
    else:
        play sound "Sounds/Phone_Vibrate.mp3"
        n "*Bzzzt. Bzzzt*"
        scene 06_460 with Dissolve(1)
        mc "{i}(Oh? It's Nikki...){/i}"
        mc "{i}(I totally forgot she called a few days ago...){/i}"
        scene 06_462 with Dissolve(1)
        mc "Hey, Nikki."
        mc "How are you?"
        ni "Sorry, I can't hear you."
        mc "Wait. I'll go outside."
        ni "Okay."
        scene black with Dissolve(2)
        pause 2
        stop music fadeout 1.0
        play music "Sounds/Street_Traffic.mp3" volume 0.3
        scene 06_463 with Dissolve(1)
        mc "Better?"
        ni "Yes! Hi, [mc]."
        mc "Hey, how are you?"
        scene 06_464 with Dissolve(1)
        ni "I'm good, thanks. I tried to call you a few days ago."
        mc "Yeah sorry. I was busy and totally forgot afterwards."
        ni "No worries."
        ni "The reason I tried to reach you was that our parents are getting married this weekend..."
        scene 06_470 with Dissolve(1)
        mc "Oh shit! It's this weekend?"
        ni "Uh-huh."
        scene 06_465 with Dissolve(1)
        ni "You're coming right?"
        mc "Yeah. There's something I need to talk about with... Dad."
        mc "{i}(And I need to talk to you.){/i}"
        ni "Great. You didn't really have a choice anyway. We booked the ticket already."
        scene 06_472 with Dissolve(1)
        mc "Haha. Okay. Thanks."
        mc "Can't wait to see you again."
        ni "Me too."
        mc "So, when's the flight?"
        scene 06_467 with Dissolve(1)
        ni "Friday. I'll send you the details. You'll be arriving here late afternoon. The wedding is Saturday."
        mc "Will be a busy weekend, huh?"
        ni "Yeah. Preparations are in full swing already."
        scene 06_468 with Dissolve(1)
        ni "I'm really happy you're coming."
        mc "Me too."
        ni "See you Friday then. I'll come to pick you up at the airport."
        mc "Thanks. See you then. Bye, Nikki."
        ni "Bye, [mc]."
        scene 06_469 with Dissolve(1)
        ni "..."
    scene black with Dissolve(1)
    pause 2
    scene 06_473 with Dissolve(1)
    mc "{i}(*Sigh* I feel so conflicted right now...){/i}"
    mc "{i}(I really wanna see her, but how do I explain... this mess...){/i}"
    play sound "Sounds/Phone_Vibrate.mp3"
    n "*Bzzzt. Bzzzt*"
    scene 06_474 with Dissolve(1)
    mc "Hey. Did you forget something?"
    er "[mc]?"
    mc "Erynn?"
    er "Yes."
    jump Week2_Wednesday_Erynn_Call

label Week2_Wednesday_Cara_Call:
    if Cara_Week2_Tuesday_Phonecall == True:
        scene black with Dissolve(1)
        pause 2
        scene 06_460 with Dissolve(1)
        mc "{i}(Oh shit! It's that late already. I'd better call Cara now.){/i}"
        scene 06_461 with Dissolve(1)
        mc "Hey Cara."
        mc "How are you?"
        c "Sorry, I can't hear you."
        scene 06_462 with Dissolve(1)
        mc "Wait. I'm in a bar, I'll go outside."
        c "Okay."
        scene black with Dissolve(1)
        pause 2
        stop music fadeout 1.0
        play music "Sounds/Street_Traffic.mp3" volume 0.3
        scene 06_463 with Dissolve(1)
        mc "Better?"
        c "Yes! Hi, [mc]."
        mc "Hey, how are you?"
        scene 06_464_02 with Dissolve(1)
        c "I'm good. How are you?"
        mc "Better than the last few days."
        mc "Sorry I'm calling so late. I was watching the game and it totally slipped my mind."
        scene 06_465_02 with Dissolve(1)
        c "No worries. I would've called if I didn't hear from you in the next hour."
        mc "Sorry again."
        c "So, you're out drinking on a Wednesday?"
        scene 06_471 with Dissolve(1)
        mc "Yeah. Wasn't planned though. Just wanted a beer tonight."
        c "Long day?"
        mc "You could say that. Very busy. What are you doing?"
        scene 06_466_02 with Dissolve(1)
        c "Right now? Uhm... Brushing my teeth? And then I'm going to watch some TV before going to bed."
        c "..."
        c "Anyway. Have you decided? You're coming right?"
        mc "Yeah. There's something I need to talk about with... Dad."
        mc "{i}(And I need to talk to you.){/i}"
        c "Great. You didn't really have a choice anyway. We booked the ticket already."
        scene 06_472 with Dissolve(1)
        mc "Haha. Okay. Thanks."
        mc "Can't wait to see you again."
        c "Me too."
        c "Aaah..."
        mc "What?"
        scene 06_467_02 with Dissolve(1)
        c "I don't know why I'm getting nervous all of a sudden."
        mc "Haha."
        mc "So, when's the flight?"
        c "Friday. I'll send you the details. You'll be arriving here late afternoon. The wedding is Saturday."
        mc "Will be a busy weekend, huh?"
        c "Yeah. Preparations are in full swing already."
        scene 06_468_02 with Dissolve(1)
        c "Well. I'll leave you be, so you can continue watching... the game. Whatever game it is."
        mc "Haha. Thanks."
        c "I'm really happy you're coming."
        mc "Me too."
        c "See you Friday then. I'll come to pick you up at the airport."
        mc "Thanks. See you then. Bye, Cara."
        c "Bye, [mc]."
        scene 06_469_02 with Dissolve(1)
        c "..."
    else:
        play sound "Sounds/Phone_Vibrate.mp3"
        n "*Bzzzt. Bzzzt*"
        scene 06_460 with Dissolve(1)
        mc "{i}(Oh? It's Cara...){/i}"
        mc "{i}(I totally forgot she called a few days ago...){/i}"
        scene 06_462 with Dissolve(1)
        mc "Hey Cara."
        mc "How are you?"
        c "Sorry, I can't hear you."
        mc "Wait. I'll go outside."
        c "Okay."
        scene black with Dissolve(2)
        pause 2
        stop music fadeout 1.0
        play music "Sounds/Street_Traffic.mp3" volume 0.3
        scene 06_463 with Dissolve(1)
        mc "Better?"
        c "Yes! Hi."
        mc "Hey, how are you?"
        scene 06_464_02 with Dissolve(1)
        c "I'm good, thanks. I tried to call you a few days ago."
        mc "Yeah sorry. I was busy and totally forgot afterwards."
        c "No worries."
        c "The reason I tried to reach you was that our parents are getting married this weekend..."
        scene 06_470 with Dissolve(1)
        mc "Oh shit! It's this weekend?"
        c "Uh-huh."
        scene 06_465_02 with Dissolve(1)
        c "You're coming right?"
        mc "Yeah. There's something I need to talk about with... Dad."
        mc "{i}(And I need to talk to you.){/i}"
        c "Great. You didn't really have a choice anyway. We booked the ticket already."
        scene 06_472 with Dissolve(1)
        mc "Haha. Okay. Thanks."
        mc "Can't wait to see you again."
        c "Me too."
        mc "So, when's the flight?"
        scene 06_467_02 with Dissolve(1)
        c "Friday. I'll send you the details. You'll be arriving here late afternoon. The wedding is Saturday."
        mc "Will be a busy weekend, huh?"
        c "Yeah. Preparations are in full swing already."
        scene 06_468_02 with Dissolve(1)
        c "I'm really happy you're coming."
        mc "Me too."
        c "See you Friday then. I'll come to pick you up at the airport."
        mc "Thanks. See you then. Bye, Cara."
        c "Bye, [mc]."
        scene 06_469_02 with Dissolve(1)
        c "..."
    scene black with Dissolve(1)
    pause 2
    scene 06_473 with Dissolve(1)
    mc "{i}(*Sigh* I feel so conflicted right now...){/i}"
    mc "{i}(I really wanna see her, but how do I explain... this mess...){/i}"
    play sound "Sounds/Phone_Vibrate.mp3"
    n "*Bzzzt. Bzzzt*"
    scene 06_474 with Dissolve(1)
    mc "Hey. Did you forget something?"
    er "[mc]?"
    mc "Erynn?"
    er "Yes."
    jump Week2_Wednesday_Erynn_Call

label Week2_Wednesday_Erynn_Call:
    stop music fadeout 1.0
    play music "Sounds/Street_Traffic.mp3" volume 0.3
    scene 06_475 with Dissolve(1)
    mc "Hi. How are you?"
    er "Uhm..."
    mc "It's really loud there. Are you clubbing?"
    er "Something like that."
    scene 06_476 with Dissolve(1)
    er "*Sigh*"
    mc "What's wrong?"
    er "I think we need to talk."
    mc "I agree. I need to talk to you as well... I have time now. What's up?"
    er "I..."
    scene 06_477 with Dissolve(1)
    x "Hey. What are you doing on your phone again?"
    x "Can you come over here already?"
    mc "Erynn?"
    scene 06_478 with Dissolve(1)
    er "Can you give me a minute?"
    x "..."
    er "Please?"
    x "One minute. Then you better move your ass next to mine."
    scene 06_471 with Dissolve(1)
    mc "Erynn?"
    er "Sorry."
    mc "Who was that?"
    er "No one..."
    mc "Are you okay?"
    scene 06_479 with Dissolve(1)
    er "{i}(No...){/i}"
    er "..."
    er "{i}(I don't want to do this...){/i}"
    mc "Erynn?"
    scene 06_480 with Dissolve(1)
    er "Yeah. I'm okay."
    mc "So you want to talk?"
    er "I can't now. Can we meet up tomorrow?"
    mc "Sure."
    er "Okay. Uhm, six o'clock, in the park?"
    mc "That's fine for me."
    scene 06_481 with Dissolve(1)
    x "Do I really have to come to get you?"
    er "..."
    x "And clean yourself up. Always the same..."
    scene 06_482 with Dissolve(1)
    er "I'm sorry. I have to go."
    mc "Okay. See you tomorrow."
    scene 06_483 with Dissolve(1)
    er "..."
    scene 06_484 with Dissolve(1)
    mc "Erynn?"
    mc "..."
    mc "That was weird."
    scene black with Dissolve(1)
    pause 2
    stop music fadeout 1.0
    play music "Sounds/Bar_Background.mp3" volume 0.3
    scene 06_485 with Dissolve(1)
    mc "Shit, the game's over already?"
    bd "Yup, you missed an intense ten minutes."
    mc "Damn... Did we at least win?"
    bd "At the buzzer."
    mc "Fuck yeah!"
    scene 06_486 with Dissolve(1)
    mc "Your friend left?"
    bd "Yeah. Work called."
    bd "He's a busy person. one of the best, if not the best, sports agents."
    mc "Oh wow. So I need to stay in contact with him if I want to be an athlete..."
    bd "Haha. You won't find a better person with all the connections he has."
    mc "Good to know."
    scene black with Dissolve(1)
    pause 2
    scene 06_487 with Dissolve(1)
    bd "Well... We're about to close. You don't have to go home, but you can't stay here."
    bd "Haha. I always wanted to say that. Finally found the perfect moment."
    mc "Hehe. Time to go home then. School day tomorrow."
    mc "What do I owe you?"
    bd "It's paid already."
    mc "What?"
    scene 06_488 with Dissolve(1)
    bd "Mr Navarro paid it."
    mc "Really? That was nice of him."
    mc "I'll have to thank him next time I see him."
    bd "He mostly comes here when the Marauders play on the road."
    mc "Okay. Thanks, Dylan, and have a good night."
    bd "Good night."
    jump Week2_Thursday

label Week2_Thursday:
    scene black with Dissolve(2)
    pause 2
    stop music fadeout 1.0
    play music "Music/Battle_Rock3.mp3" volume 0.4
    n "Thursday, 17:51."
    scene 06_489 with Dissolve(1)
    mc "{i}(Hmm... I might be a bit early.){/i}"
    mc "{i}(What does she want to talk about? She sounded weird yesterday.){/i}"
    scene 06_490 with Dissolve(1)
    mc "{i}(Maybe about us?){/i}"
    if Alexis_Friends == True:
        mc "{i}(*Sigh* I don't know.){/i}"
    else:
        mc "{i}(Maybe what happened with Alexis?){/i}"
        mc "{i}(*Sigh* I don't know.){/i}"
    scene black with Dissolve(1)
    pause 2
    scene 06_491 with Dissolve (1)
    mc "{i}(18:20... Still not here...){/i}"
    mc "{i}(Did she forget? Let's call her.){/i}"
    scene 06_492 with Dissolve(1)
    play sound "Sounds/Phone_Message.mp3"
    n "*Bzzzt*"
    mc "{i}(Oh? That might be from her.){/i}"
    scene 06_493 with Dissolve(1)
    er "Hey. I'm so sorry. Something came up and I can't make it. I'll call you later. Erynn."
    mc "..."
    menu:
        "Angry reply[KoGa3AutoWTChange1]{size=-4}(Erynn Points-4) {/size} {/color}":
            $ Erynn_Points -= 4
            scene 06_494 with Dissolve(1)
            mc "You couldn't tell me earlier? I've been waiting half an hour already..."
            mc "..."
            mc "Heh. No reply, huh?"
            mc "Okay. Whatever Erynn..."
        "Nice reply":
            scene 06_494a with Dissolve(1)
            mc "Okay. No worries. We'll postpone it, I guess."
            mc "..."
            mc "Hmm, no reply. Must be busy."
            mc "Better get going then."
    scene black with Dissolve(1)
    pause 2
    scene 06_495 with Dissolve(1)
    mc "*Sigh*"
    mc "{i}(Seriously, I don't get her sometimes.){/i}"
    mc "{i}(First she wants to talk, then asks me to leave, now she doesn't show up...){/i}"
    scene black with Dissolve(1)
    pause 2
    scene 06_496 with Dissolve(1)
    mc "{i}(I really need to talk to her though. Ask her what's going on.){/i}"
    mc "{i}(It's getting ridiculous...){/i}"
    scene 06_497 with Dissolve(1)
    mc "{i}(Eh? What the fuck!){/i}"
    mc "..."
    scene 06_498 with Dissolve(1)
    mc "{i}(So, this is why you stood me up?){/i}"
    mc "{i}(I can't believe this...){/i}"
    scene 06_499 with Dissolve(1)
    mc "{i}(She's on a freakin' date with Ethan.){/i}"
    mc "{i}('It was work-related' my ass...){/i}"
    mc "{i}(She was probably partying with him yesterday too...){/i}"
    scene 06_500 with vpunch
    er "{i}([mc]!){/i}"
    er "{i}(Oh no!){/i}"
    scene 06_501 with Dissolve(1)
    er "{i}(No... This isn't...){/i}"
    scene 06_502 with Dissolve(1)
    mc "{i}(Yeah, I just caught you red-handed!){/i}"
    mc "{i}(What do you have to say now?){/i}"
    mc "{i}(Fucking 'work-related' again?){/i}"
    scene 06_503 with Dissolve(1)
    mc "{i}(I'm out of here.){/i}"
    er "[mc]! Wait!"
    scene 06_504 with Dissolve(1)
    et "Where are you going?"
    er "Let go!"
    et "You are not going after him. We're not done here!"
    er "Let me fucking go, Ethan!"
    scene black with Dissolve(1)
    pause 2
    scene 06_505 with Dissolve(1)
    er "[mc], please wait!"
    er "Wait!"
    scene 06_506 with Dissolve(1)
    er "I'm sorry."
    er "There's a reason I had to be there."
    menu:
        "Don't talk[KoGa3AutoWTChange1]{size=-4}(Erynn Points-8, Erynn Friends) {/size} {/color}":
            $ Erynn_Points -= 8
            $ Erynn_Friends = True
            scene 06_507 with Dissolve(1)
            mc "Honestly Erynn, I don't want to talk with you right now."
            er "I had to..."
            mc "No Erynn."
            scene 06_508 with Dissolve(1)
            er "Please, [mc]. It was..."
            mc "Work-related?"
            scene 06_509 with Dissolve(1)
            er "..."
            er "Ethan, he..."
            mc "Ethan this, Ethan that..."
            er "Why don't you let me explain?"
            mc "Because I don't want to hear it."
            er "It's just like years ago... You didn't talk to me then, either."
            mc "I guess I haven't changed that much, then. Compared to someone..."
            er "[mc]!"
            if Alexis_Friends == True:
                scene 06_511 with Dissolve(1)
                mc "I'm leaving. I don't want to do this now..."
                er "[mc]... Please just..."
                mc "No, Erynn."
                mc "Bye!"
            else:
                scene 06_510 with Dissolve(1)
                er "Does this have to do with Alexis?"
                er "Did she ask you to do this?"
                mc "What? This has nothing to do with Alexis. This is between you and me."
                er "Are you together?"
                mc "No, we aren't."
                scene 06_511 with Dissolve(1)
                mc "I'm leaving. I don't want to do this now..."
                er "[mc]... I'm sorry. Please just..."
                mc "No, Erynn."
                mc "Bye!"
            scene 06_512 with Dissolve(1)
            er "[mc]!"
            er "I need you."
            er "Please, [mc]..."
            scene black with Dissolve(2)
            pause 2
            scene 06_513 with Dissolve(1)
            er "*Crying*"
            er "{i}(What should I do now?){/i}"
            er "{i}(I just can't do this anymore...){/i}"
            jump Week2_Thursday_Emily_Home
        "Confront her[KoGa3AutoWTChange1]{size=-4}(Erynn Points+2, Erynn Week2 Thursday Confront) {/size} {/color}":
            $ Erynn_Points += 2
            # Erynn (30)
            $ Erynn_Week2_Thursday_Confront = True
            scene 06_514 with Dissolve(1)
            mc "The reason you being that asshole's girlfriend? Is that why you've been so shady lately? Trying to hide all this?"
            er "What? NO! I would never..."
            scene 06_507 with Dissolve(1)
            mc "Then why would you even hang out with that guy, huh? You especially should know what he's like."
            er "I..."
            mc "Or is it just like back then? So you can make fun of me again?"
            er "I have never made fun of you. What are you talking about?"
            scene 06_515 with Dissolve(1)
            mc "Of course, you don't remember. It was just a normal day in the life of Erynn..."
            er "What?"
            mc "My confession. I told you I liked you. But you just made a joke out of it and laughed with your friends."
            er "..."
            mc "Does that ring a bell?"
            er "..."
            scene 06_516 with Dissolve(1)
            er "That didn't happen."
            mc "That didn't happen? Was it so insignificant to you? Must have happened to you a lot then, huh? Do you know how..."
            er "We didn't laugh about you."
            mc "What?"
            er "We didn't laugh about you."
            mc "Oh really?"
            jump FB_Erynn_MC

label FB_Erynn_MC:
    scene black with Dissolve(2)
    pause 2
    stop music fadeout 1.0
    play music "Music/Slow.mp3" volume 0.5
    n "A few years ago."
    scene 06_517 with Dissolve(1)
    m "Hey, honey. Are you going somewhere?"
    mc "Yeah. I'm going to Erynn's."
    m "Okay, have fun."
    scene 06_518 with Dissolve(1)
    m "..."
    m "Are you looking for something?"
    mc "No..."
    scene 06_519 with Dissolve(1)
    m "What are you doing with my flower?"
    mc "Nothing..."
    m "..."
    scene 06_520 with Dissolve(1)
    m "[mc]. Come here for a second."
    mc "Why?"
    m "Come here."
    scene 06_521 with Dissolve(1)
    mc "What now?"
    m "Nothing..."
    mc "MOM!"
    m "Haha."
    scene 06_522 with Dissolve(1)
    m "Go have fun."
    mc "..."
    scene 06_523 with Dissolve(1)
    mc "Mom... Don't do that."
    m "Sorry, haha."
    scene black with Dissolve(1)
    pause 2
    scene 06_524 with Dissolve(1)
    mc "{i}(Why is Ethan here again? Does he have to come every day?){/i}"
    mc "Hey, Erynn."
    scene 06_525 with Dissolve(1)
    er "Oh hey, [mc]."
    mc "I want to ask you something."
    er "Okay."
    scene 06_526 with Dissolve(1)
    er "Hey. What's up?"
    mc "Uhm..."
    mc "Erynn... I... I like... you."
    scene 06_527 with Dissolve(1)
    er "Hehe... You're so cute. I like you too."
    mc "..."
    mc "No. That's not what I mean."
    er "No? You don't like me?"
    mc "..."
    scene 06_528 with Dissolve(1)
    er "Is that flower for me?"
    mc "Yes..."
    scene 06_529 with Dissolve(1)
    mc "Do you want to be my... my girlfriend?"
    er "Oh... I... Uhm..."
    er "{i}(Why would he ask me that here? Now? What should I say?){/i}"
    er "I..."
    et "Hey, Erynn. Come here for a sec."
    scene 06_530 with Dissolve(1)
    er "Sorry, [mc]... I'll be right back."
    er "{i}(What should I do?){/i}"
    scene 06_531 with Dissolve(1)
    et "Here check his reply. He actually got detention, that idiot."
    er "Haha... I knew it."
    scene 06_532 with Dissolve(1)
    a "Haha. We even told him it would be a bad idea."
    er "Haha, right?"
    et "Haha..."
    scene 06_533 with Dissolve(1)
    mc "{i}(Why are they laughing?){/i}"
    scene 06_534 with Dissolve(1)
    et "So what did little dweeb want?"
    er "Don't call him that!"
    scene 06_535 with Dissolve(1)
    et "Look at him standing there with his flower."
    et "Wait... Don't tell me he confessed to you?"
    er "..."
    et "Haha... He did? Oh my god. That's too funny."
    scene 06_536 with Dissolve(1)
    et "Hey, buddy. Nice try. How about you grow a few inches first?"
    a "Ethan!"
    scene 06_537 with Dissolve(1)
    er "[mc]... Wait! Don't go!"
    er "Damn Ethan!"
    scene 06_538 with Dissolve(1)
    er "Why do you always bully him?"
    et "What? Why not? It's funny."
    er "It's not!"
    er "Can't you leave him alone?"
    a "I'm going home! You guys solve this."
    scene 06_539 with Dissolve(1)
    et "I just don't understand how you can be friends with this little kid."
    er "Who are you to call him a little kid? Ever looked at yourself in a mirror?"
    et "All the time. Look at me. Compared to him I'm..."
    scene 06_540 with Dissolve(1)
    er "Ethan! Just stop! For once!"
    et "Come on, Erynn. Don't tell me you actually like him."
    er "Of course I like him. I've known him my whole life. We're friends."
    et "Heh, friends... He clearly wants to be more."
    scene 06_541 with Dissolve(1)
    er "And what he wants is none of your business."
    et "Haha. Don't tell me you're going to be his girlfriend."
    er "Still none of your business."
    scene 06_542 with Dissolve(1)
    et "I don't know if you're joking or being serious here. Do you really like him like that?"
    er "I told you, he and I are friends. And if you continue like this, you and I won't be anymore."
    scene 06_543 with Dissolve(1)
    et "Erynn... Just think about it. He's what? Like eight?"
    er "*Rolls eyes*"
    et "Well... it makes no difference. He's still a pathetic little boy."
    scene 06_544 with Dissolve(1)
    er "I told you to stop, Ethan!"
    et "I can do whatever I want. It has nothing to do with you."
    er "It has everything to do with me. Just leave him alone!"
    if Alexis_Friends == False:
        scene black with Dissolve(2)
        pause 2
        scene 05_456a with Dissolve(1)
        a "Hey, are you okay?"
        mc "Go away. Just leave me alone!"
        a "Ethan is an idiot. I don't like him either."
        mc "..."
        scene 05_457a with Dissolve(1)
        a "I think what you did was really cute."
        a "Nobody ever gave me flowers."
        mc "It's just one flower."
        a "That doesn't matter. I'd love to get flowers from a boy one day."
        scene 05_458a with Dissolve(1)
        mc "{i}(Uh?){/i}"
        mc "Hey! What are you doing?"
        scene 05_459a with Dissolve(1)
        a "Happy Birthday, [mc]!"
        mc "..."
        scene 06_545 with Dissolve(1)
        a "..."
        scene 06_546 with Dissolve(1)
        a "{i}(No... I can't believe he just stole my first kiss...){/i}"
    else:
        pass
    scene black with Dissolve(1)
    pause 2
    scene 06_547 with Dissolve(1)
    m "{i}(Is he back already?){/i}"
    m "[mc]?"
    mc "Yes..."
    scene 06_548 with Dissolve(1)
    m "You're back early."
    m "Isn't Erynn home?"
    mc "..."
    m "Hey... What's wrong, honey?"
    mc "Nothing."
    scene 06_549 with Dissolve(1)
    m "Hey come here. What happened? And don't say nothing again."
    mc "..."
    m "Weren't you going to celebrate your birthday with Erynn?"
    scene 06_550 with Dissolve(1)
    mc "She was there with her friends."
    m "And?"
    scene 06_551 with Dissolve(1)
    mc "They were laughing at me."
    m "Why were they laughing at you?"
    mc "..."
    scene 06_552 with Dissolve(1)
    m "Erynn would never laugh at you. Are you sure you didn't misunderstand?"
    mc "I saw them laughing and looking at me."
    m "Just go back and talk to Erynn. She can probably explain that it was nothing."
    scene 06_553 with Dissolve(1)
    mc "..."
    m "What? Since when are you shy?"
    mc "I'm not!"
    m "Well then go and talk to her."
    scene 06_554 with Dissolve(1)
    er "One more thing. This conversation stays between us. You won't tell anyone about this."
    et "Or what?"
    er "Try me, Ethan! I swear I'll make your life a living hell."
    et "Heh..."
    er "And leave [mc] alone. I mean it!"
    et "Whatever..."
    scene 06_555 with Dissolve(1)
    et "*Mumbles* Just wait Erynn... We aren't done here."
    er "What did you say?"
    et "I said see you tomorrow at school."
    er "{i}(He's so annoying.){/i}"
    scene black with Dissolve(1)
    pause 2
    scene 06_556 with Dissolve(1)
    et "What are you doing here again?"
    mc "I'm..."
    et "Just go away!"
    scene 06_557 with Dissolve(1)
    mc "But today is my..."
    et "But, but, but... Are you stupid?"
    scene 06_558 with Dissolve(1)
    et "Erynn hates you! Don't you get it?"
    et "She doesn't want to play with little idiots like you."
    et "You are just annoying and ruin everything..."
    mc "..."
    mc "I..."
    scene 06_559 with vpunch
    et "LEAVE!"
    scene black with Dissolve(1)
    pause 2
    scene 06_560 with Dissolve(1)
    n "*Door slams*"
    m "Back again?"
    m "[mc]?"
    n "*Door slams*"
    m "*Sigh*"
    scene black with Dissolve(1)
    pause 2
    n "*Knock-knock*"
    scene 06_561 with Dissolve(1)
    er "Hey, Emily."
    m "Hey, sweetheart. How are you?"
    er "I'm good. Is [mc] here?"
    m "I think he's in his room."
    scene 06_562 with Dissolve(1)
    m "Did something happen, Erynn?"
    er "Uhm... Ethan was mean to him."
    m "Hmm..."
    scene 06_563 with Dissolve(1)
    m "Well you can try to talk to him, but I think it's best to let him cool off a bit."
    m "He can be stubborn."
    er "Okay. I'll come back later, then."
    m "Thank you, Erynn. I'll try to calm him down in the meantime."
    er "Bye-bye."
    m "Bye, sweetheart."
    jump Week2_Thursday_Erynn

label Week2_Thursday_Erynn:
    scene black with Dissolve(2)
    pause 2
    scene 06_564 with Dissolve(1)
    mc "..."
    mc "Fuck!"
    mc "So you weren't laughing about the flower and the confession?"
    scene 06_565 with Dissolve(1)
    er "What? No! Of course not. To be honest, I was a bit embarrassed but I really liked it, actually."
    er "Did you think this whole time I was laughing at you?"
    mc "Well yeah... How should I have known?"
    scene 06_566 with Dissolve(1)
    er "Why didn't you just ask me? I tried to talk to you afterwards, but you just ignored me all the time."
    er "And then a few weeks later, you were gone. I tried to call you, but you never answered. I even asked your mom, and she told me that you wouldn't even take her calls."
    er "I wrote you letters, but never got one back."
    er "What else could I have done?"
    scene 06_567 with Dissolve(1)
    mc "I never read the letters."
    er "What? Why not?"
    mc "Because I was a stupid little boy... Well, I still am, actually... Stupid that is."
    scene 06_568 with Dissolve(1)
    er "You weren't and you aren't."
    er "{i}(If someone is stupid, it's definitely me.){/i}"
    mc "You sure about that? Because I'm not."
    scene 06_569 with Dissolve(1)
    mc "Fuck! Why did I even believe that guy? This... This has all been my fault. Everything..."
    mc "Nothing would have happened if I'd just... Fuck!"
    er "[mc]..."
    scene 06_570 with Dissolve(1)
    mc "Sorry, Erynn. Let's talk later, please."
    er "But... I just..."
    mc "Sorry. I need to actually think this time, before I do something stupid again..."
    er "I understand..."
    mc "I'll call you."
    scene black with Dissolve(1)
    pause 2
    scene 06_571 with Dissolve(1)
    er "*Sigh*"
    er "{i}(That's not all though. I need to tell you so much more. And it's worse than this...){/i}"
    jump Week2_Thursday_Emily_Home

label Week2_Thursday_Emily_Home:
    scene black with Dissolve(1)
    pause 2
    if Erynn_Week2_Thursday_Confront == True:
        scene 06_572 with Dissolve(1)
        mc "{i}(I even lost all those years with my mom because of this...){/i}"
        menu:
            "Hug":
                scene 06_574 with Dissolve(1)
                mc "Mom..."
                m "[mc]? You scared me."
                mc "I'm so sorry."
                m "Honey, what's wrong?"
                scene 06_575 with Dissolve(1)
                mc "I'm so sorry about everything. This has all been my fault."
                m "Now you're scaring me even more. I've never seen you like this. What happened?"
            "Talk":
                scene 06_573 with Dissolve(1)
                mc "Hey, Mom. I need to talk to you."
                m "Hey, honey. What's wrong?"
                scene 06_575 with Dissolve(1)
                mc "I'm so sorry about everything. This has all been my fault."
                m "I've never seen you like this. What happened?"
        scene black with Dissolve(1)
        pause 2
        scene 06_576 with Dissolve(1)
        m "*Sigh*"
        m "That explains a lot of things."
        mc "Yeah. I'm so sorry."
        m "It's fine, it's all in the past now."
        mc "Yeah. Feels like I can finally move on, start a new chapter or something."
    else:
        scene 06_572 with Dissolve(1)
        mc "Hey, Mom. I need to talk to you."
        scene 06_573 with Dissolve(1)
        m "Hey, honey. What do you want to talk about?"
        m "You want to continue our conversation from yesterday?"
        mc "No... It's... Erynn."
        scene black with Dissolve(1)
        pause 2
        scene 06_576 with Dissolve(1)
        m "But why didn't you let her explain?"
        mc "I don't know... She's behaving somewhat strangely... And when I saw her with Ethan, I just saw red..."
        m "You and that Ethan guy never got along, huh?"
        mc "He's an idiot."
        m "..."
        m "I still think it's best to talk to her. You let me explain, and we're okay now."
        m "Put everything on the table, and afterwards, you can both start a new chapter or something."
    if Andres_FB_Punch == False:
        mc "Well, not just yet though. There's one more thing I need to do."
        m "Okay?"
        jump Week2_Thursday_Emily_Wedding
    else:
        scene black with Dissolve(1)
        pause 2
        scene 06_577 with Dissolve(1)
        mc "How is the restaurant doing, actually? Any news?"
        m "It's coming along."
        mc "Did you find some people already?"
        m "I hired a server. Still looking for a cook and another server."
        scene 06_578 with Dissolve(1)
        mc "I have nothing planned this weekend. I can help out."
        m "Yeah? That'd be great."
        scene black with Dissolve(1)
        pause 2
        scene 06_581 with Dissolve(1)
        m "Are you hungry? Cause I'm craving some fast food."
        mc "Wait? You eat that?"
        m "Once in a while, yes."
        mc "Burgers, fries, chicken wings?"
        scene 06_582 with Dissolve(1)
        m "If you knew what I ate during my pregnancy with you, you'd call me crazy."
        mc "Haha..."
        jump Episode_7_Start

label Week2_Thursday_Emily_Wedding:
    scene black with Dissolve(1)
    pause 2
    scene 06_579 with Dissolve(1)
    mc "Uhm... Andres is getting married this weekend."
    m "Oh? That's this weekend?"
    mc "Yeah. Forgot about it myself."
    if Cara_FB_Choose == True:
        mc "Cara called me and reminded me."
    else:
        mc "Nikki called me and reminded me."
    m "And you want to go?"
    mc "Yeah. I promised them. Besides, there are some things I need to talk to him about."
    scene 06_580 with Dissolve(1)
    m "I understand. When is the wedding, exactly?"
    mc "Saturday. So I have to fly tomorrow."
    m "What about school?"
    mc "Yeah, about that..."
    scene 06_581 with Dissolve(1)
    m "It's fine. I'll call them and say you have a family matter."
    mc "Thanks, Mom."
    mc "Do you want to come with?"
    scene 06_582 with Dissolve(1)
    m "No-no-no... Not a good idea."
    mc "Haha. Would be funny if you suddenly showed up, huh?"
    m "He'd be jumping for joy."
    mc "Haha..."
    mc "When was the last time you saw Andres?"
    scene 06_583 with Dissolve(1)
    m "When I tried to visit you back in Alvarado."
    mc "{i}(Damn. What a stupid question.){/i}"
    mc "Sorry."
    m "It's fine."
    scene 06_584 with Dissolve(1)
    mc "Is it weird for you that he's getting married?"
    m "No. We've been divorced for seven years already. I actually don't care. He's free to do whatever he wants."
    scene 06_585 with Dissolve(1)
    mc "{i}(Hmm... Maybe Andres was right that she never really loved him?){/i}"
    mc "..."
    scene black with Dissolve(1)
    pause 2
    scene 06_581 with Dissolve(1)
    m "Are you hungry? Cause I'm craving some fast food."
    mc "Wait? You eat that?"
    m "Once in a while, yes."
    mc "Burgers, fries, chicken wings?"
    scene 06_582 with Dissolve(1)
    m "If you knew what I ate during my pregnancy with you, you'd call me crazy."
    mc "Haha..."
    scene black with Dissolve(2)
    pause 2
    n "Friday, 09:32."
    scene 06_586 with Dissolve(1)
    m "Are you ready? We need to leave!"
    mc "One second."
    scene 06_587 with Dissolve(1)
    mc "Good to go."
    m "You've got everything?"
    mc "I think so."
    scene 06_588 with Dissolve(1)
    m "Here. Can you give this to Andres and Haley?"
    mc "I will."
    scene 06_589 with Dissolve(1)
    m "When is your flight back?"
    mc "It's the same flight as last time, so Sunday morning."
    m "Okay. I'll come to pick you up then. This time at the airport."
    mc "Hehe. Thank you."
    if Nikki_FB_Choose == True:
        jump Week2_Weekend_Nikki
    else:
        jump Week2_Weekend_Cara

label Week2_Weekend_Nikki:
    scene black with Dissolve(2)
    pause 2
    stop music fadeout 1.0
    play music ("Music/LoFi Indie 3.mp3", "Music/LoFi Indie 1.mp3", "Music/LoFi Indie 2.mp3") volume 0.2
    n "Friday, 16:36. Riverside Airport."
    scene 06_590 with Dissolve(1)
    mc "Hey, Nikki. I hope you didn't have to wait too long."
    ni "Hi!"
    mc "Thanks for picking..."
    scene 06_591 with vpunch
    mc "Umpf..."
    ni "I missed you."
    scene 06_592 with Dissolve(1)
    ni "Sorry. Maybe I was a little too excited."
    mc "Hehe. Maybe just a little."
    menu:
        "Kiss":
            scene 06_594 with Dissolve(1)
            mc "I missed you too."
            mc "{i}(Wow... I almost kissed her on the lips.){/i}"
            ni "{i}(For a second I thought he'd kiss me on the lips...){/i}"
        "Hug":
            scene 06_593 with Dissolve(1)
            mc "I missed you too."
    scene 06_595 with Dissolve(1)
    ni "What is this on your face?"
    mc "What? Do I have something on my face?"
    scene 06_596 with Dissolve(1)
    ni "Yeah... This..."
    ni "What is this? Hair? Is this supposed to be a beard?"
    scene 06_597 with Dissolve(1)
    mc "..."
    ni "Haha..."
    scene 06_598 with Dissolve(1)
    ni "I'm kidding... Where are you going?"
    mc "Back to Madison Springs. The girls are nicer there."
    scene 06_599 with Dissolve(1)
    ni "Haha, you wish. You aren't going anywhere!"
    mc "Hehe..."
    scene 06_600 with Dissolve(1)
    ni "It's... Interesting?"
    mc "Haha. You hate it? Should I shave?"
    ni "No... I don't mind it."
    mc "Good. Because I didn't bring a shaver."
    ni "You can use mine!"
    scene 06_601 with Dissolve(1)
    mc "Must be a really good one. Your face is so smooth."
    ni "Ha-ha... Very funny..."
    mc "Haha."
    scene 06_602 with Dissolve(1)
    ni "I've missed our banter."
    mc "Me too."
    ni "Let's get outta here."
    scene black with Dissolve(1)
    pause 2
    scene 06_603 with Dissolve(1)
    mc "Must have been busy around the house the last couple of days or weeks."
    ni "It was alright, actually. Yeah, there was more stress and tension the closer we got to the wedding date, but all in all, I think we managed."
    mc "Is everyone home?"
    scene 06_604 with Dissolve(1)
    ni "Only Cara as far as I know. Mom and Andres are at the venue. Setting stuff up and double-checking everything for tomorrow."
    mc "Do we need to help out?"
    ni "No, Cara and I offered, but they want it to be a surprise."
    scene 06_605 with Dissolve(1)
    mc "Early weekend then..."
    ni "Haha, yes."
    mc "Do you still have to work today?"
    ni "No, I have the whole weekend off, which is rare."
    scene black with Dissolve(2)
    pause 2
    scene 06_606 with Dissolve(1)
    mc "{i}(Hmm... Isn't that Andres?){/i}"
    mc "..."
    scene 06_607 with Dissolve(1)
    mc "{i}(It's definitely him!){/i}"
    mc "Hey. Didn't you say Andres is helping at the venue?"
    ni "Yeah, he is. Why?"
    mc "No reason..."
    scene 06_608 with Dissolve(1)
    mc "{i}(What the fuck is he doing here then? With... whoever that is.){/i}"
    mc "{i}(I guess I have to have more than just one talk with him...){/i}"
    mc "{i}(Fuck me.){/i}"
    scene 06_609 with Dissolve(1)
    mc "Why are we still sitting still?"
    ni "Red light. Something the matter?"
    mc "No... Let's just drive home."
    ni "Okay?"
    mc "{i}(Calm down. This could all be a big misunderstanding again. Let's not jump to conclusions...){/i}"
    scene black with Dissolve(1)
    pause 2
    scene 06_629 with Dissolve(1)
    ni "Hey, Cara. Look who I picked up off the street."
    mc "{i}(Heh?){/i}"
    c "Hey, [mc]."
    mc "Hey, Cara."
    scene 06_630 with Dissolve(1)
    c "We missed you."
    mc "Missed you too."
    scene 06_631 with Dissolve(1)
    c "How are you?"
    c "How is life in Madison Springs?"
    mc "Eh... It has its ups and downs, I guess."
    c "Like everywhere..."
    mc "Yeah."
    c "You can always move back in with us... Right, Nikki?"
    scene 06_632 with Dissolve(1)
    ni "Uhm..."
    mc "..."
    play sound "Sounds/Phone_Vibrate.mp3"
    n "*Bzzzt. Bzzzt*"
    scene 06_633 with Dissolve(1)
    c "Oh, sorry. I need to take this."
    mc "Take your time. I need to unpack anyway. We'll talk later, yes?"
    c "Of course. I want to hear all about your new school."
    mc "Haha, alright."
    scene black with Dissolve(1)
    pause 2
    scene 06_634 with Dissolve(1)
    ni "You can have your old room for the next few days."
    mc "Thanks. It's so empty..."
    mc "Do you already know what will happen to this room?"
    ni "Probably stay as a guestroom."
    ni "Maybe someone will come and visit once in a while."
    mc "..."
    scene 06_635 with Dissolve(1)
    mc "Haah..."
    ni "Tired?"
    mc "Exhausted!"
    ni "Really?"
    mc "No, I'm okay. Just wanted to lie down for a second."
    scene 06_636 with Dissolve(1)
    ni "Good idea."
    mc "..."
    scene 06_637 with Dissolve(1)
    mc "By the way. What was that just now? Picked up off the street, huh?"
    ni "Haha, sorry... I wanted to say something funny or clever but that's the best I could come up with."
    mc "If that was your best, I'm sorry..."
    ni "It was too much pressure."
    scene 06_638 with Dissolve(1)
    ni "What are your plans for today?"
    mc "I thought we'd have to help with the preparations, but since we don't, I have no idea..."
    mc "Just relax a bit?"
    mc "You?"
    scene 06_639 with Dissolve(1)
    ni "Hmm... I was thinking of going to the movies. I haven't been in a long time and there's actually a movie playing I want to see."
    ni "Do you want to join me?"
    mc "Which movie?"
    ni "Uh... It's a romance flick. But we can watch something else if you want?"
    menu:
        "It's fine[KoGa3AutoWTChange1]{size=-4}(Nikki Week2 Weekend Movie, Nikki Weekend Points+2) {/size} {/color}":
            $ Nikki_Week2_Weekend_Movie = True
            $ Nikki_Weekend_Points += 2
            # Nikki_Weekend (2)
            scene 06_641 with Dissolve(1)
            mc "It's fine. I don't watch many movies anyway. So, let's go watch the one you want to see."
            ni "Thanks."
            ni "That reminds me. I rarely saw you watch TV when you were living here."
            mc "True. I only watch sports actually."
            mc "Is there a sport you watch or do you have a favourite team or something?"
            scene 06_642 with Dissolve(1)
            ni "No. I like to play sports. But watching others... Not my thing. I have to watch clients at the gym the all day already."
            mc "True. I liked to watch when you were doing your exercises though..."
            scene 06_643 with Dissolve(1)
            ni "..."
            ni "{i}(And I liked you watching me...){/i}"
        "Watch something else":
            scene 06_640 with Dissolve(1)
            mc "I'd rather watch something else if you don't mind."
            ni "Yeah, of course."
    scene black with Dissolve(1)
    pause 2
    scene 06_644 with Dissolve(1)
    ni "Okay. I'm gonna get ready then."
    mc "When's the movie?"
    ni "In two hours."
    scene 06_645 with Dissolve(1)
    mc "Uhm... Why would you need two hours to get ready?"
    ni "I need to shower, do my hair, makeup, and pick out some clothes."
    scene 06_646 with Dissolve(1)
    mc "We're going to the movies. You look fine to me."
    ni "*Sigh*"
    mc "You're right. I'll zip it."
    menu:
        "Need help?":
            scene 06_647 with Dissolve(1)
            mc "Can I help you with anything?"
            ni "Want to wash my back in the shower?"
            mc "Sure!"
            ni "Haha..."
            scene 06_648 with Dissolve(1)
            mc "*Sigh*"
            mc "{i}(Why do girls always need so long to get ready?){/i}"
            mc "{i}(I actually wanted to talk to you about Andres.){/i}"
            mc "{i}(I guess we'll talk after the movie. Don't want to ruin the fun now...){/i}"
            scene 06_649 with Dissolve(1)
            mc "{i}(Was she serious about the shower? I never know with her...){/i}"
            mc "{i}(Does she still... Do I still?){/i}"
            mc "{i}(This is so confusing...){/i}"
            mc "{i}(But should I even go?){/i}"
            menu:
                "Join Nikki[KoGa3AutoWTChange1]{size=-4}(Nikki Weekend Points+2) {/size} {/color}":
                    $ Nikki_Weekend_Points += 2
                    # Nikki_Weekend (4)
                    scene black with Dissolve(2)
                    pause 2
                    scene 06_650 with Dissolve(1)
                    mc "Hey Nikki, were you..."
                    scene 06_651 with Dissolve(1)
                    c "AAAH! [mc]!"
                    mc "Oh? Sorry, Cara."
                    scene 06_652 with Dissolve(1)
                    c "Why didn't you knock?"
                    mc "Sorry, I thought Nikki was in there."
                    c "That doesn't change the fact that you should still knock..."
                    mc "You're right, sorry."
                    c "..."
                    c "Never mind... I guess we're even now!"
                    mc "{i}(Oh yeah, she caught me masturbating once. Totally forgot that...){/i}"
                    scene 06_653 with Dissolve(1)
                    ni "What's going on?"
                    mc "Uh? I thought you were in the shower, and Cara..."
                    ni "I was joking..."
                    ni "{i}(He really wanted to join me?){/i}"
                "Just wait":
                    mc "{i}(I think she was just joking.){/i}"
        "Just wait":
            mc "I'll get myself ready as well then."
            scene 06_648 with Dissolve(1)
            mc "*Sigh*"
            mc "{i}(Why do girls always need so long to get ready?){/i}"
            mc "{i}(I actually wanted to talk to you about Andres.){/i}"
            mc "{i}(I guess we talk after the movie. Don't want to ruin the fun now...){/i}"
    scene black with Dissolve(1)
    pause 2
    scene 06_675 with Dissolve(1)
    ni "Okay, I'm ready. Didn't take too long, right?"
    mc "{i}(Wow...){/i}"
    scene black with Dissolve(1)
    transform moveup:
        xalign 0.5 yalign 1.0
        linear 5.0 yalign 0.0
    show 06_676 at moveup
    pause 3
    mc "You know we're just going to the movies?"
    ni "Yeah, that's why I dressed casually."
    mc "{i}(I like your casual.){/i}"
    mc "..."
    mc "Yeah... Casual..."
    scene 06_677 with Dissolve(1)
    ni "I still need to put on my cardigan. It's downstairs."
    mc "{i}(At least that will cover something. That way I might be able to actually concentrate on the movie.){/i}"
    ni "Shall we?"
    mc "Yes."
    scene black with Dissolve(1)
    pause 2
    scene 06_682 with Dissolve(1)
    mc "{i}(Cardigan? There are more holes in it than a fishnet. So much for covering up...){/i}"
    ni "What is it?"
    menu:
        "Nothing":
            mc "Nothing..."
        "Gorgeous[KoGa3AutoWTChange1]{size=-4}(Nikki Weekend Points+2) {/size} {/color}":
            $ Nikki_Weekend_Points += 2
            # Nikki_Weekend (6)
            scene 06_683 with Dissolve(1)
            mc "You look gorgeous."
            ni "Thank you. But why are you laughing?"
            mc "Nothing in particular, just happy I guess..."
            ni "..."
    if Nikki_Weekend_Points == 6:
        scene 06_684 with Dissolve(1)
        ni "Here, you drive."
        mc "Eh, sure."
        scene 06_685 with Dissolve(1)
        ni "..."
        ni "{i}(I'm happy, too.){/i}"
    else:
        scene 06_684 with Dissolve(1)
        ni "Here, you drive."
        mc "Eh, sure."
    scene black with Dissolve(1)
    pause 2
    scene 06_690 with Dissolve(1)
    ni "This is the first time I've let someone else drive my car."
    mc "It is? I'm honoured."
    ni "Haha..."
    mc "Where is it exactly?"
    ni "Not so far from your old school. I'll direct you."
    mc "My very own GPS with a sexy voice. Awesome."
    ni "..."
    scene black with Dissolve(1)
    pause 2
    scene 06_691 with Dissolve(1)
    ni "So, how is the new school?"
    mc "It's good actually. I joined the track and field team."
    ni "Oh? You must miss our morning runs then?"
    menu:
        "Yes":
            scene 06_692a with Dissolve(1)
            mc "I do. Was a great way to start the day. Enjoyable company as well."
            ni "Haha, enjoyable company... That's what I was?"
            mc "Uh-huh..."
            if Nikki_Weekend_Points == 6:
                scene 06_693 with Dissolve(1)
                ni "{i}(I miss them too...){/i}"
                scene 06_694 with Dissolve(1)
                ni "Want to go for a run tomorrow morning?"
                mc "Sure, why not."
                ni "Great."
            else:
                scene 06_694 with Dissolve(1)
                ni "Want to go for a run tomorrow morning?"
                mc "Sure, why not."
                ni "Great."
        "Not really":
            scene 06_692 with Dissolve(1)
            mc "No, not really. Maybe the running but I didn't like to wake up that early."
            ni "Haha, it wasn't that early..."
    scene black with Dissolve(1)
    pause 2
    if Nikki_Week2_Weekend_Movie == True:
        scene 06_696 with Dissolve(1)
        ni "Did you find anything you want to watch?"
        mc "Didn't you want to see that romance movie?"
        ni "We can watch something else, I can come another time."
        mc "No-no-no. Let's go watch it. I don't mind. Really!"
        scene 06_697 with Dissolve(1)
        ni "Thank you!"
        scene 06_698 with Dissolve(1)
        ni "Ahh... So prickly."
        mc "The beard, I get it..."
        ni "Beard? Haha."
        mc "Funny. Obviously overreacting."
        ni "Obviously..."
    else:
        scene 06_695 with Dissolve(1)
        ni "Did you find anything?"
        mc "Yeah, how about this one? Looks interesting, no?"
        ni "Your decision, I don't mind."
    scene black with Dissolve(2)
    pause 2
    scene 06_699 with Dissolve(1)
    mc "Oh, forgot to get something to drink and some snacks."
    mc "What do you want?"
    ni "Nothing, thanks!"
    mc "You sure? Popcorn or something?"
    ni "I'm not hungry."
    menu:
        "Annoy her":
            scene 06_699a with Dissolve(1)
            mc "Right, carbs and stuff, I remember..."
            ni "..."
            mc "Haha. Be right back. Save me a seat."
            ni "Maybe. I just might give it to someone else..."
            mc "Then we'll have to share a seat."
            ni "Just go get your snacks."
            mc "Haha..."
            if Nikki_Weekend_Points == 6:
                scene 06_699b with Dissolve(1)
                ni "{i}(Idiot...){/i}"
            else:
                pass
        "Be right back":
            mc "Be right back."
    scene black with Dissolve(1)
    pause 2
    scene 06_700 with Dissolve(1)
    ni "Found something?"
    mc "Just some sweetened popcorn and a soda."
    scene 06_701 with Dissolve(1)
    mc "..."
    mc "{i}(I knew it.){/i}"
    scene 06_702 with Dissolve(1)
    ni "Just testing if they're tasty."
    mc "..."
    scene black with Dissolve(1)
    pause 2
    scene 06_703 with Dissolve(1)
    mc "I thought you didn't want anything."
    ni "Yeah, I'm not hungry."
    mc "I can see that."
    ni "I'll only take a few."
    mc "Uh-huh..."
    scene 06_704 with Dissolve(1)
    mc "Do you want popcorn? I'll get you some."
    ni "I'm good. Thanks, though."
    mc "{i}(Because you're eating mine!){/i}"
    if Nikki_Week2_Weekend_Movie == True:
        scene black with Dissolve(1)
        pause 2
        scene 06_705 with Dissolve(1)
        ""
        scene 06_706 with Dissolve(1)
        mc "{i}(Looks like she's enjoying the movie.){/i}"
    else:
        scene black with Dissolve(2)
        pause 2
        scene 06_705a with Dissolve(1)
        ""
        scene 06_706a with Dissolve(1)
        mc "{i}(She's looking kinda uncomfortable. Maybe I should've let her pick and watch the romance movie...){/i}"
    scene black with Dissolve(1)
    pause 2
    scene 06_707 with Dissolve(1)
    ""
    scene 06_708 with Dissolve(1)
    ""
    scene 06_709 with Dissolve(1)
    mc "..."
    mc "{i}(Now you're thirsty...){/i}"
    menu:
        "Give her the soda[KoGa3AutoWTChange1]{size=-4}(Nikki Weekend Points+2) {/size} {/color}":
            $ Nikki_Weekend_Points += 2
            # Nikki_Weekend (8)
            mc "{i}(That's what you get for eating my popcorn.){/i}"
            if Nikki_Weekend_Points == 8:
                scene 06_710 with Dissolve(1)
                mc "Here."
                ni "Thank you!"
                scene 06_711 with Dissolve(1)
                ni "{i}(Do you have any idea what you're doing to me?){/i}"
                scene black with Dissolve(1)
                pause 2
                scene 06_712 with Dissolve(1)
                ni "They're cute, right? The movie couple."
                mc "..."
                ni "The way they look at each other. The way they're holding hands..."
                scene 06_713 with Dissolve(1)
                ni "..."
                ni "{i}(Heh? They actually fit perfectly.){/i}"
            else:
                scene 06_710 with Dissolve(1)
                mc "Here."
                ni "Thank you!"
        "Let her be thirsty":
            mc "{i}(That's what you get for eating my popcorn.){/i}"
    scene black with Dissolve(1)
    pause 2
    if Nikki_Week2_Weekend_Movie == True:
        scene 06_716 with Dissolve(1)
        mc "{i}(Still holding hands, huh?){/i}"
        mc "{i}(I guess it's okay for today.){/i}"
        scene 06_717 with Dissolve(1)
        ni "What did you think about the movie? Did you enjoy it?"
        mc "Yeah, it was good, very cute."
        scene 06_718 with Dissolve(1)
        ni "..."
        ni "And now an honest answer!"
        scene 06_719 with Dissolve(1)
        mc "Why? Why do girls watch that type of movie?"
        ni "Haha..."
        mc "Next time, when you visit me in Madison Springs, I'll pick the movie..."
        scene 06_720 with Dissolve(1)
        ni "{i}(Next time?){/i}"
        ni "No..."
        mc "No?"
        ni "No! When I come to visit you, we won't go to the movies, we'll go to the beach!"
        mc "Haha, fair enough."
    else:
        scene 06_714 with Dissolve(1)
        mc "Sorry."
        ni "Hmm?"
        mc "I know this wasn't the movie you wanted to see."
        ni "It was alright..."
        mc "I was being selfish. We should've watched yours."
        scene 06_715 with Dissolve(1)
        mc "Well, next time, when you visit me in Madison Springs, we'll watch something you want to see."
        ni "No..."
        mc "No?"
        ni "If I come to visit you, we won't go to the movies, we'll go to the beach!"
        mc "Haha, fair enough."
    if Nikki_Weekend_Points >= 5:
        ni "Do you want to grab a drink? I know a nice bar."
        menu:
            "No":
                mc "I think we'd better call it for today. Important day tomorrow."
                ni "Right..."
                jump Week2_Weekend_Nikki_End
            "Yes[KoGa3AutoWTChange1]{size=-4}(Nikki Weekend Points+2) {/size} {/color}":
                $ Nikki_Weekend_Points += 2
                # Nikki_Weekend (10)
                mc "Yeah, why not."
                scene black with Dissolve(1)
                pause 2
                scene 06_721 with Dissolve(1)
                mc "Why are there no free parking spaces? This is ridiculous."
                ni "It's Friday. Everyone's out tonight."
                mc "Yeah, seems like it."
                scene 06_722 with Dissolve(1)
                mc "How about I let you out here and you can look for a table?"
                mc "In the meantime, I'll search for a place to park the car."
                ni "Sure."
                scene 06_723 with Dissolve(1)
                mc "Okay, see you soon, I hope."
                ni "Haha. Don't leave me for too long."
                scene black with Dissolve(1)
                pause 2
                scene 06_724 with Dissolve(1)
                x "Hey there."
                ni "Hi..."
                scene 06_725 with Dissolve(1)
                x "What's a cutie like you doing here, all alone?"
                ni "Come on... You can do better. Try again."
                x "What?"
                ni "Your pickup line. You surely have something better, no?"
                x "Uhm... You... I lost my phone, can I..."
                scene 06_726 with Dissolve(1)
                mc "{i}(Really... Can't leave her alone for a second without another dude trying to swoop in.){/i}"
                scene black with Dissolve(1)
                transform moveup:
                    xalign 0.5 yalign 1.0
                    linear 5.0 yalign 0.0
                show 06_727 at moveup
                pause 3
                mc "{i}(*Sigh* She looks stunning though...){/i}"
                menu:
                    "Join them":
                        scene 06_728 with Dissolve(1)
                        mc "Hey. Are you a parking ticket? Because you've got FINE written all over you."
                        ni "Haha..."
                        x "Dude. What are you doing?"
                        scene 06_729 with Dissolve(1)
                        mc "Isn't this the bad pickup line meeting?"
                        x "What? No!"
                        mc "Oh? My bad."
                        ni "Haha."
                    "Let Nikki handle it[KoGa3AutoWTChange1]{size=-4}(Nikki Week2 Weekend Handle) {/size} {/color}":
                        $ Nikki_Week2_Weekend_Handle = True
                        scene 06_730 with Dissolve(1)
                        x "Did it hurt?"
                        ni "{i}(*Sigh* I'll play along I guess...){/i}"
                        ni "Did what hurt?"
                        x "When you fell from heaven."
                        scene 06_731 with Dissolve(1)
                        ni "I dug my way up from hell actually."
                        x "What?"
                        ni "Yeah, I'm evil, pure evil..."
                        scene 06_728 with Dissolve(1)
                        mc "Hey, you can't use my line..."
                        ni "Haha... Sorry. It fitted perfectly though, right?"
                        scene 06_732 with Dissolve(1)
                        mc "It's true though. She's pure evil, and lots of other things."
                        ni "Don't tell him my secrets."
                scene 06_733 with Dissolve(1)
                mc "Want to grab something to drink?"
                ni "Yeah."
                x "Hey! What the fuck man..."
                scene black with Dissolve(1)
                pause 2
                scene 06_734 with Dissolve(1)
                if Nikki_Week2_Weekend_Handle == False:
                    ni "Speaking about parking tickets. You found a spot?"
                else:
                    ni "Did you find a parking spot? Not too far I hope."
                mc "Uh, yeah well... About that. We shouldn't stay too long, just to be sure."
                ni "Haha... Two drinks max, then."
                scene black with Dissolve(1)
                pause 2
                scene 06_735 with Dissolve(1)
                ni "In a few hours, we will officially be brother and sister."
                mc "..."
                mc "{i}(Damn... Why haven't I said anything yet... Don't I want to tell her?){/i}"
                mc "{i}(I think I should talk to Andres first, to hear both sides.){/i}"
                mc "..."
                mc "{i}(And I need to talk to him about the picture... To know for sure what's going on with that woman before it becomes a misunderstanding and I ruin something else.){/i}"
                mc "{i}(Why is everything so complicated?){/i}"
                scene 06_736 with Dissolve(1)
                mc "{i}(And why can't I tell her that I still like her?){/i}"
                ni "Hmm?"
                ni "{i}(Something on his mind?){/i}"
                scene 06_737 with Dissolve(1)
                mc "You look very pretty today."
                ni "..."
                mc "I li... I missed you, Nikki..."
                ni "..."
                scene 06_738 with Dissolve(1)
                ni "Why are you flirting with me?"
                mc "..."
                mc "How is this even flirting? I just..."
                ni "How isn't this flirting?"
                ni "You've been doing this the whole day. And you know it."
                mc "{i}(And you haven't?){/i}"
                scene 06_739 with Dissolve(1)
                ni "..."
                ni "Keep this up and I might end up making a mistake."
                mc "A mistake?"
                scene 06_740 with Dissolve(1)
                ""
                scene 06_741 with Dissolve(1)
                mc "..."
                ni "Something like this."
                scene 06_742 with Dissolve(1)
                mc "I wish we met earlier. Before... you know."
                ni "{i}(Stop... This is hard enough already.){/i}"
                ni "{i}(I wish we could just... But...){/i}"
                ni "{i}(No, Nikki...){/i}"
                scene 06_743 with Dissolve(1)
                ni "Seeing how you're spewing nonsense, you must be a bit tipsy..."
                mc "{i}(She's right. We shouldn't do this...){/i}"
                mc "{i}(Why do I feel so bad about it though. My heart's pounding like crazy.){/i}"
                mc "Yeah... You might be right."
                ni "..."
                ni "Let's go home."
                jump Week2_Weekend_Nikki_Continue
    else:
        ni "Let's go home."
        jump Week2_Weekend_Nikki_End

label Week2_Weekend_Nikki_End:
    $ Nikki_Girlfriend = False
    $ Riverside_Friends = True
    scene black with Dissolve(2)
    pause 2
    scene 06_791 with Dissolve(1)
    mc "{i}(Two o'clock already...){/i}"
    n "*Knock-knock*"
    scene 06_792 with Dissolve(1)
    mc "Yeah?"
    scene 06_794 with Dissolve(1)
    ni "Hey!"
    mc "Hey, come on in."
    ni "Thanks. I saw that the lights were still on."
    scene 06_795 with Dissolve(1)
    ni "You can't sleep either?"
    mc "No, I tried, but... nothing."
    ni "Too excited for the wedding?"
    mc "No, it's something else. I need..."
    scene 06_796 with Dissolve(1)
    ni "I have an idea."
    mc "Yeah?"
    ni "Let's play a game or something."
    mc "Sure, what kind of game?"
    ni "A card game, maybe?"
    mc "You have a deck?"
    scene 06_797 with Dissolve(1)
    ni "Yeah, let me get it real quick."
    mc "Want to ask Cara if she wants to join?"
    scene 06_798 with Dissolve(1)
    ni "I was in her room before I came here. She's sleeping already."
    mc "Oh, okay."
    mc "{i}(Let's play a few games, but then I really need to tell her.){/i}"
    scene black with Dissolve(1)
    pause 2
    scene 06_799 with Dissolve(1)
    ni "Let's make it interesting."
    mc "What do you have in mind?"
    ni "The loser has to do something embarrassing at the wedding party."
    mc "I'm totally game for that."
    scene 06_800 with Dissolve(1)
    mc "Can't wait to see what you're about to do."
    ni "Hey! Who says I'm going to lose?"
    mc "Haha..."
    scene black with Dissolve(2)
    pause 2
    stop music fadeout 1.0
    play music "Music/Battle_Rock2.mp3" volume 0.5
    n "Saturday, 08:23."
    scene 06_807 with Dissolve(1)
    d "[mc], are you awake already?"
    scene 06_808 with Dissolve(1)
    d "..."
    d "What is going on here?"
    scene 06_809 with Dissolve(1)
    ni "Aaah... Andres!"
    mc "Get out!"
    scene 06_810 with Dissolve(1)
    d "Not before you tell me what's going on here."
    mc "Just get out already..."
    d "That's why you wanted to live with your mom again, right? You've been sleeping with each other behind our backs?"
    ni "..."
    d "This is wrong. What are you trying to accomplish? Are you rebelling against this marriage?"
    scene 06_811 with Dissolve(1)
    mc "Rebelling... Obviously..."
    ni "..."
    mc "Can you stop jumping to conclusions? We just played cards late last night and fell asleep."
    d "Playing cards... Half naked..."
    mc "We're wearing clothes, aren't we?"
    d "..."
    scene 06_812 with Dissolve(1)
    mc "And why would this even matter? This doesn't have anything to do with you."
    d "Nothing to do with me? How can you be so stupid! I can't believe you were hiding this from us all this time."
    mc "We didn't sleep with each other..."
    d "Don't bullshit me. I know when you're lying."
    mc "Oh yeah... I'm the one lying? Like you've been telling me everything, right?"
    d "I've always been truthful."
    scene 06_813 with Dissolve(1)
    mc "Okay. Let's see. Hmm... How about the fact that you aren't my real dad?"
    d "..."
    scene 06_814 with Dissolve(1)
    ni "What?"
    ni "[mc]?"
    scene 06_815 with Dissolve(1)
    d "Heh. You've been living with her for two weeks and she's already broken her promise..."
    d "Should've known."
    mc "No. You should have told me way before. Actually, you should've never asked for such a promise to begin with. It wasn't your decision to make..."
    d "Yeah. I'm not your real dad. Now you've heard it from me. Happy?"
    mc "..."
    scene 06_816 with Dissolve(1)
    d "So what are you doing here then, huh? There's no reason for you to be here. Go live your life with your mom."
    mc "Wow... You were my dad for so many years. And in a way you still are. I came to support you and talk to you about all this. Seems like it was a mistake."
    d "..."
    scene 06_817 with Dissolve(1)
    ni "Uhm..."
    ni "Guys?"
    scene 06_818 with Dissolve(1)
    d "Support me? You call this supporting me? Sleeping with my soon-to-be step-daughter."
    mc "We..."
    d "You're just like your mom. Sleeping around and not caring about the consequences."
    mc "Leave her out of it."
    d "Afraid of what I'm going to say?"
    mc "No... This has nothing to do with her."
    d "Do you know how our relationship ended? I'll tell you. She was sleeping around with your real dad."
    mc "She met up with him to talk. Nothing more."
    scene 06_819 with Dissolve(1)
    d "That's what she told you? That cheating bitch!"
    mc "HEY! Don't talk about her like that."
    d "She ruined everything."
    mc "Haha. Totally. It's all her fault. You like to blame others. A bad habit I got from you by the way."
    mc "If you want to know who the real cheater is, look in a mirror. You'll be surprised."
    d "What are you talking about?"
    scene 06_820 with Dissolve(1)
    mc "I saw you. Yesterday."
    d "Where?"
    mc "In the city."
    d "I wasn't in the city."
    mc "{i}(One lie after another.){/i}"
    mc "Then tell me, where were you?"
    d "I was with Haley the whole day. Preparing for the wedding."
    scene 06_821 with Dissolve(1)
    mc "Always been truthful, huh?"
    mc "How do you explain this then?"
    d "..."
    d "Where did you get that?"
    mc "As I said, I saw you."
    d "Heh. She's just a colleague..."
    scene 06_822 with Dissolve(1)
    mc "So first of all, you weren't with Haley."
    mc "Second. Do you always put your arm around your female colleagues?"
    d "What?"
    mc "How about we ask Haley if she knows her?"
    mc "You work at the same company. She should know her, right?"
    scene 06_823 with Dissolve(1)
    ni "Andres?"
    ni "Are you cheating on Mom?"
    mc "{i}(I'm so sorry you had to find out this way, Nikki.){/i}"
    scene 06_824 with Dissolve(1)
    d "Give me that!"
    mc "No..."
    ni "Andres! Stop!"
    scene 06_825 with vpunch
    mc "..."
    scene 06_826 with Dissolve(1)
    mc "Smashing my phone... Do you think that will change the facts?"
    mc "Now I finally understand why you didn't tell me about Haley for about a year."
    mc "Scared to mix up their names?"
    scene 06_827 with vpunch
    d "You son of a bitch."
    ni "[mc]!"
    menu:
        "Hit him back":
            scene 06_828 with vpunch
            mc "You never deserved Mom. And you don't deserve Haley and this family!"
            ni "[mc]! Please stop!"
            scene 06_830 with Dissolve(1)
            ni "And you get out of my house."
            d "Nikki, let me..."
            ni "LEAVE! GET OUT!"
        "Don't hit him":
            scene 06_829 with Dissolve(1)
            mc "You never deserved Mom. And you don't deserve Haley and this family!"
            ni "[mc], don't!"
            scene 06_830 with Dissolve(1)
            ni "What are you doing? How can you even hit him..."
            d "Nikki, let me..."
            ni "LEAVE! GET OUT!"
    scene black with Dissolve(1)
    pause 2
    scene 06_831 with Dissolve(1)
    ni "Are you alright?"
    mc "Yeah... How about you?"
    scene 06_832 with Dissolve(1)
    ni "Why didn't you tell me he isn't your father? And more importantly that he's cheating on my mom!"
    mc "I wanted to. I wasn't sure if... I just..."
    ni "When?"
    ni "When they were married?"
    scene 06_833 with Dissolve(1)
    mc "No... I needed to hear it from him first before I said something that maybe would've been a misunderstanding."
    mc "I've made so many mistakes lately because I didn't listen and let people explain. I needed to be sure."
    scene 06_834 with Dissolve(1)
    ni "..."
    ni "You know what was a mistake? This here!"
    scene 06_835 with Dissolve(1)
    mc "Nikki..."
    ni "I need to go find Mom."
    mc "I'm sorry."
    ni "I'm sorry, too..."
    scene black with Dissolve(1)
    pause 2
    scene 06_836 with Dissolve(1)
    mc "{i}(Fuck... Wherever I go, I ruin something.){/i}"
    mc "..."
    scene black with Dissolve(1)
    pause 2
    scene 06_837 with Dissolve(1)
    n "Nikki, I'm sorry. I never..."
    jump Week2_Weekend_NikkiCara_End

label Week2_Weekend_Nikki_Continue:
    if _in_replay:
        $ MC_SexCounter = 2
        $ SexCounter_Nikki = 2
    $ MC_SexCounter += 1
    $ SexCounter_Nikki += 1
    # Nikki_Sex (3)
    scene black with Dissolve(2)
    pause 2
    scene 06_791 with Dissolve(1)
    mc "{i}(Two o'clock already...){/i}"
    n "*Knock-knock*"
    scene 06_793 with Dissolve(1)
    mc "Nikki?"
    scene black with Dissolve(1)
    transform moveup:
        xalign 0.5 yalign 1.0
        linear 5.0 yalign 0.0
    show 06_838 at moveup
    pause 3
    ni "I can't sleep."
    mc "..."
    mc "Me neither."
    scene 06_839 with Dissolve(1)
    mc "What are..."
    ni "I also wish we met earlier, before..."
    scene 06_840 with Dissolve(1)
    ni "I miss you. So much."
    mc "..."
    scene 06_841 with Dissolve(1)
    ni "Every day I wanted to call you... Just to hear your voice..."
    ni "Asking if you can come back..."
    scene 06_842 with Dissolve(1)
    mc "I need to talk to you."
    ni "Not now..."
    ni "Why can't we just..."
    mc "..."
    scene 06_843 with Dissolve(1)
    mc "Nikki... We shouldn't..."
    ni "I know..."
    ni "I told you I'll make a mistake..."
    mc "{i}(Why do I want this so bad?){/i}"
    scene 06_844 with Dissolve(1)
    mc "{i}(She can make me forget about everything...){/i}"
    scene black with Dissolve(2)
    pause 2
    scene 06_845a with Dissolve(1)
    ni "Do you like the outfit?"
    mc "You look gorgeous. But it doesn't really matter. It's coming off anyway."
    ni "Haha. You're right..."
    scene black with Dissolve(1)
    pause 2
    scene 06_845 with Dissolve(1)
    mc "{i}(Who can say no to this?){/i}"
    scene 06_846 with Dissolve(1)
    ni "Touch me!"
    mc "..."
    scene 06_847 with Dissolve(1)
    ni "{i}(I missed this...){/i}"
    scene 06_848 with Dissolve(1)
    ni "Ah... [mc]."
    scene black with Dissolve(1)
    pause 2
    scene 06_849 with vpunch
    ni "Haha..."
    ni "Your mood changed quickly."
    scene 06_850 with Dissolve(1)
    ni "Mmm... I remember that body!"
    ni "{i}(How did he become more handsome in just a few weeks...){/i}"
    scene 06_851 with Dissolve(1)
    ""
    scene 06_852 with Dissolve(1)
    ni "{i}(Do you have any idea the way you make me feel?){/i}"
    scene 06_853 with Dissolve(1)
    mc "{i}(Even her panties are wet already.){/i}"
    scene 06_854 with Dissolve(1)
    ""
    scene black with Dissolve(1)
    pause 2
    scene 06_855 with Dissolve(1)
    ni "*Heavy breathing*"
    scene 06_856 with Dissolve(1)
    ni "..."
    scene 06_857 with Dissolve(1)
    ni "Aaah..."
    scene 06_858 with Dissolve(1)
    ni "I wanted this the moment I saw you at the airport..."
    mc "Me too..."
    scene 06_860 with Dissolve(1)
    ""
    scene 06_859 with Dissolve(1)
    ""
    scene black with Dissolve(1)
    pause 2
    scene 06_861 with Dissolve(1)
    ni "[mc]... Keep going..."
    scene 06_864 with Dissolve(1)
    ni "Aaah..."
    scene 06_865 with Dissolve(1)
    ""
    scene 06_863 with Dissolve(1)
    ""
    scene 06_862 with Dissolve(1)
    ni "Hey. Let me lie down for a second. This isn't the most comfortable of positions..."
    mc "Haha, sorry."
    scene black with Dissolve(1)
    pause 2
    scene 06_866 with Dissolve(1)
    ""
    scene 06_867 with Dissolve(1)
    mc "Better?"
    ni "Yeah, keep going..."
    scene 06_868 with Dissolve(1)
    ni "{i}(This is so good.){/i}"
    ni "I quite like this one..."
    mc "I do too..."
    ni "{i}(Yeah, I can feel you're close...){/i}"
    menu:
        "Pull out":
             scene 06_869 with vpunch
             ""
             scene 06_869 with vpunch
             ""
             scene black with Dissolve(1)
             pause 2
             scene 06_870 with Dissolve(1)
             mc "*Heavy breathing*"
             ni "Want to go again?"
             mc "Heh... Sure!"
        "Cum inside[KoGa3AutoWTChange1]{size=-4}(Nikki Week2 Weekend SexInside) {/size} {/color}":
            $ Nikki_Week2_Weekend_SexInside = True
            scene 06_871 with vpunch
            ""
            scene 06_871 with vpunch
            ""
            scene black with Dissolve(1)
            pause 2
            scene 06_872 with Dissolve(1)
            mc "*Heavy breathing*"
            ni "Want to go again?"
            mc "Heh... Sure!"
    scene black with Dissolve(1)
    pause 2
    scene 06_873 with Dissolve(1)
    mc "Wow. We're pretty good at this."
    ni "Haha. We are!"
    scene 06_874 with Dissolve(1)
    mc "..."
    $ renpy.end_replay()
    scene black with Dissolve(2)
    pause 2
    stop music fadeout 1.0
    play music "Music/Battle_Rock2.mp3" volume 0.5
    n "Saturday, 08:23."
    scene 06_807 with Dissolve(1)
    d "[mc], are you awake already?"
    scene 06_808_01 with Dissolve(1)
    d "..."
    d "What is going on here?"
    scene 06_809_01 with Dissolve(1)
    ni "Aaah... Andres."
    mc "Get out!"
    scene 06_810 with Dissolve(1)
    d "Not before you tell me what's going on here."
    mc "Just get out already..."
    d "That's why you wanted to live with your mom again, right? You've been sleeping with each other behind our backs?"
    ni "..."
    scene 06_811b with Dissolve(1)
    mc "Sorry."
    mc "Here, wear this in the meantime."
    ni "Thank you."
    scene 06_811_01 with Dissolve(1)
    d "This is wrong. What are you trying to accomplish? Are you rebelling against this marriage?"
    mc "Rebelling... Obviously..."
    ni "..."
    mc "{i}(Obviously? I sound just like Nikki...){/i}"
    scene 06_812 with Dissolve(1)
    mc "No... We like each other. And why would this even matter? This doesn't have anything to do with you."
    d "Nothing to do with me? Like each other? How can you be so stupid! With her?"
    ni "Excuse me?"
    d "I can't believe you were hiding this from us all this time."
    mc "Oh yeah... Like you've been telling me everything, right?"
    d "I've always been truthful."
    scene 06_813 with Dissolve(1)
    mc "Okay. Let's see. Hmm... How about the fact that you aren't my real dad?"
    d "..."
    scene 06_814_01 with Dissolve(1)
    ni "What?"
    ni "[mc]?"
    scene 06_815 with Dissolve(1)
    d "Heh. You've been living with her for two weeks and she's already broken her promise..."
    d "Should've known."
    mc "No. You should have told me way before. Actually, you should've never asked for such a promise to begin with. It wasn't your decision to make..."
    d "Yeah. I'm not your real dad. Now you've heard it from me. Happy?"
    mc "..."
    scene 06_816 with Dissolve(1)
    d "So what are you doing here then, huh? There's no reason for you to be here. Go live your life with your mom."
    mc "Wow... You were my dad for so many years. And in a way you still are. I came to support you and talk to you about all this. Seems like it was a mistake."
    d "..."
    scene 06_817_01 with Dissolve(1)
    ni "Uhm..."
    ni "Guys?"
    scene 06_818 with Dissolve(1)
    d "Support me? You call this supporting me? Sleeping with my soon-to-be step-daughter."
    mc "We..."
    d "You're just like your mom. Sleeping around and not caring about the consequences."
    mc "Leave her out of it."
    d "Afraid of what I'm going to say?"
    mc "No... This has nothing to do with her."
    d "Do you know how our relationship ended? I'll tell you. She was sleeping around with your real dad."
    mc "She met up with him to talk. Nothing more."
    scene 06_819 with Dissolve(1)
    d "That's what she told you? That cheating bitch!"
    mc "HEY! Don't talk about her like that."
    d "She ruined everything."
    mc "Haha. Totally. It's all her fault. You like to blame others. A bad habit I got from you by the way."
    mc "If you want to know who is the real cheat and ruins relationships, look in a mirror. You'll be surprised."
    d "What are you talking about?"
    scene 06_820 with Dissolve(1)
    mc "I saw you. Yesterday."
    d "Where?"
    mc "In the city."
    d "I wasn't in the city."
    mc "{i}(One lie after another.){/i}"
    mc "Then tell me, where were you?"
    d "I was with Haley the whole day. Preparing for the wedding."
    scene 06_821 with Dissolve(1)
    mc "Always been truthful, huh?"
    mc "How do you explain this then?"
    d "..."
    d "Where did you get that?"
    mc "As I said, I saw you."
    d "Heh. She's just a colleague..."
    scene 06_822 with Dissolve(1)
    mc "So first of all, you weren't with Haley."
    mc "Second. Do you always put your arm around your female colleagues?"
    d "What?"
    mc "How about we ask Haley if she knows her?"
    mc "You work at the same company. She should know her, right?"
    scene 06_823_01 with Dissolve(1)
    ni "Andres?"
    ni "Are you cheating on Mom?"
    mc "{i}(I'm so sorry you had to find out this way, Nikki.){/i}"
    scene 06_824_01 with Dissolve(1)
    d "Give me that!"
    mc "No..."
    ni "Andres! Stop!"
    scene 06_825 with vpunch
    mc "..."
    scene 06_826 with Dissolve(1)
    mc "Smashing my phone... Do you think that will change the facts?"
    mc "Now I finally understand why you didn't tell me about Haley for about a year."
    mc "Scared to mix up their names?"
    scene 06_827_01 with vpunch
    d "You son of a bitch."
    ni "[mc]!"
    menu:
        "Hit him back[KoGa3AutoWTChange1]{size=-4}(Nikki Weekend Points-2) {/size} {/color}":
            $ Nikki_Weekend_Points -= 2
            scene 06_828_01 with vpunch
            mc "You never deserved Mom. And you don't deserve Haley and this family!"
            ni "[mc]! Please stop!"
            scene 06_830_01 with Dissolve(1)
            ni "And you get out of my house."
            d "Nikki, let me..."
            ni "LEAVE! GET OUT!"
        "Don't hit him[KoGa3AutoWTChange1]{size=-4}(Riverside End) {/size} {/color}":
            scene 06_829_01 with Dissolve(1)
            mc "You never deserved Mom. And you don't deserve Haley and this family!"
            ni "[mc], don't!"
            scene 06_830_01 with Dissolve(1)
            ni "What are you doing? How can you even hit him..."
            d "Nikki, let me..."
            ni "LEAVE! GET OUT!"
    scene black with Dissolve(1)
    pause 2
    scene 06_831_01 with Dissolve(1)
    ni "Are you alright?"
    mc "Yeah... How about you?"
    scene 06_832_01 with Dissolve(1)
    ni "Why didn't you tell me he isn't your father? And more importantly that he's cheating on my mom!"
    mc "I wanted to. I wasn't sure if... I just..."
    ni "When?"
    ni "When they were married?"
    scene 06_833_01 with Dissolve(1)
    mc "No... I needed to hear it from him first, before I said something that maybe would've been a misunderstanding."
    mc "I've made so many mistakes lately because I didn't listen and let people explain. I needed to be sure."
    scene 06_834_01 with Dissolve(1)
    ni "..."
    ni "You know what was a mistake? This here!"
    scene 06_835_01 with Dissolve(1)
    mc "Nikki..."
    ni "I need to go find Mom."
    mc "I'm sorry."
    ni "I'm sorry too..."
    scene black with Dissolve(1)
    pause 2
    scene 06_836 with Dissolve(1)
    mc "{i}(Fuck... Wherever I go, I ruin something.){/i}"
    mc "..."
    scene black with Dissolve(1)
    pause 2
    scene 06_837 with Dissolve(1)
    n "Nikki, I'm sorry. I never..."
    if Nikki_Weekend_Points >= 7:
        scene black with Dissolve(2)
        pause 2
        scene 06_904 with Dissolve(1)
        mc "{i}(It was the right decision to leave, right?){/i}"
        mc "{i}(They probably don't want to see me anyway.){/i}"
        ni "[mc]!"
        scene 06_905 with Dissolve(1)
        mc "Nikki?"
        ni "Please wait."
        ni "Where are you going?"
        mc "Home..."
        scene 06_906 with Dissolve(1)
        mc "I shouldn't have come. I ruined everything... Again."
        ni "No. You didn't."
        mc "I'm sorry, Nikki."
        ni "[mc], you didn't! You saved her from making a horrible mistake."
        mc "..."
        scene 06_907 with Dissolve(1)
        ni "Don't leave. I don't want you to go, [mc]."
        ni "I'm sorry that I called us a mistake. I was mad. I didn't mean it. You're the best thing that could've happened to me."
        mc "..."
        ni "Stay and move back in with us."
        mc "Nikki, be realistic. That won't work. I'll always remind Haley of Andres and..."
        ni "No, you're nothing like him. She likes you."
        mc "..."
        mc "*Sigh* I can't leave my mom. I won't do that to her again. I've hurt her so much already."
        ju "Hey, [mc]."
        scene 06_908 with Dissolve(1)
        ju "Long time no see. Where've you been these last few weeks?"
        ju "Skipping school is bad!"
        mc "Not now, Julia..."
        ju "Wow... Someone's in a mood."
        ju "Hey, Nikki."
        ni "Hey."
        if Julia_FB_Sex == True:
            $ Nikki_Girlfriend = False
            $ Riverside_End = True
            scene 06_909 with Dissolve(1)
            ju "{i}(What are they doing here together?){/i}"
            ju "{i}(Are they dating?){/i}"
            ju "Remember, if you want to have fun again. call me [mc]. Last time was great!"
            mc "..."
            mc "{i}(What is she doing?){/i}"
            scene 06_910 with Dissolve(1)
            ni "What are you talking about?"
            ju "Nothing! Don't worry. We just had a little... something at the club, right, [mc]? Haha."
            ni "Something?"
            ni "When was that?"
            ju "A few weeks ago..."
            mc "..."
            scene 06_911 with Dissolve(1)
            mc "Sorry, Nikki. I..."
            ni "It's true?"
            ni "I guess I was wrong. Nothing like him? Heh... Are you sure you and Andres aren't related?"
            ni "I can't believe I cared..."
            scene 06_912 with Dissolve(1)
            mc "Nikki..."
            ni "No. Go home or wherever... Ruin someone else's life."
            mc "Nikki!"
            scene 06_913 with Dissolve(1)
            mc "Fuck!"
            mc "Thanks, Julia."
            ju "What did I do?"
            jump Week2_Weekend_NikkiCara_End
        else:
            ju "I guess I'm interrupting. I'll leave you two. Bye-bye."
            ju "{i}(Are they dating?){/i}"
            scene black with Dissolve(1)
            pause 2
            scene 06_914 with Dissolve(1)
            mc "My bus is here."
            ni "You're really leaving?"
            mc "I have to."
            ni "Then I'll drive you."
            mc "Thanks, but no... This is hard enough already..."
            scene 06_915 with Dissolve(1)
            ni "[mc]..."
            mc "Bye, Nikki."
            ni "..."
            scene 06_916 with Dissolve(1)
            ni "[mc]!"
            ni "Wait!"
            scene 06_917 with Dissolve(1)
            mc "..."
            scene black with Dissolve(1)
            pause 2
            scene 06_918 with Dissolve(1)
            ni "I love you!"
            jump Week2_Weekend_NikkiCara_End
    else:
        $ Nikki_Girlfriend = False
        $ Riverside_Friends = True
        jump Week2_Weekend_NikkiCara_End

label Week2_Weekend_Cara:
    scene black with Dissolve(2)
    pause 2
    stop music fadeout 1.0
    play music ("Music/LoFi Indie 3.mp3", "Music/LoFi Indie 1.mp3", "Music/LoFi Indie 2.mp3") volume 0.2
    n "Friday, 16:35. Riverside Airport."
    scene 06_610 with Dissolve(1)
    mc "{i}(Hmm... She isn't here yet?){/i}"
    mc "{i}(Or maybe she's waiting outside?){/i}"
    mc "..."
    mc "{i}(Oh...){/i}"
    scene 06_611 with Dissolve(1)
    c "Booo..."
    mc "Hey, there you are!"
    scene 06_612 with Dissolve(1)
    c "You didn't even flinch..."
    mc "I saw you in the reflection."
    c "..."
    c "No fun."
    menu:
        "Kiss":
            scene 06_614 with Dissolve(1)
            c "Hi."
            mc "Hey Cara. How are you?"
            c "Really good. I'm really happy you came."
        "Hug":
            scene 06_613 with Dissolve(1)
            c "Hi."
            mc "Hey Cara. How are you?"
            c "Really good. I'm really happy you came."
    scene 06_615 with Dissolve(1)
    c "Hmm..."
    mc "What?"
    c "Something's different about you."
    mc "I changed my hair."
    c "Yeah, I saw that, looks good. But that's not it."
    mc "Nothing else changed. Nothing I can think of at least."
    c "I'll figure it out later."
    scene 06_616 with Dissolve(1)
    mc "Anyway. Thanks for picking me up."
    c "Of course."
    mc "How did you get here? Did you get your license?"
    scene 06_617 with Dissolve(1)
    c "No... Not yet."
    c "With all the wedding preparations going on. Mom didn't have time to teach me."
    mc "What about Nikki?"
    c "She comes home late from work, and I don't want to drive in the dark."
    scene 06_618 with Dissolve(1)
    mc "If you haven't planned anything for today. I can teach you. So you can practice a bit."
    c "Really? I'd like that."
    mc "Now we only need to find a car."
    c "I'll ask Mom if we can use hers."
    mc "Cool."
    scene 06_619 with Dissolve(1)
    mc "So, do we call an Uber now?"
    c "Or we can take the bus?"
    mc "Fine by me."
    scene 06_620 with Dissolve(1)
    mc "Why are you smiling? Something good happen today?"
    c "I'm just really happy..."
    scene black with Dissolve(1)
    pause 2
    scene 06_621 with Dissolve(1)
    mc "Must have been busy around the house the last couple of days or weeks."
    c "It was alright actually. Yeah, there was more stress and tension the closer we got to the wedding date. But all in all, I think we managed."
    mc "Is everyone home?"
    scene 06_623 with Dissolve(1)
    c "Only Nikki as far as I know, but she had to go to work today, so I'm not sure. Mom and Andres are at the venue. Setting stuff up and double-checking everything for tomorrow."
    mc "Do we need to help out?"
    c "No, Nikki and I offered, but they want it to be a surprise."
    scene 06_623 with Dissolve(1)
    mc "Early weekend then..."
    c "Yes!"
    mc "So, no school for you either, today?"
    c "No, I called in sick, so I could pick you up."
    mc "Haha. Thanks."
    scene black with Dissolve(1)
    pause 2
    scene 06_625 with Dissolve(1)
    mc "{i}(Hmm... isn't that Andres?){/i}"
    mc "..."
    scene 06_626 with Dissolve(1)
    mc "{i}(It's definitely him!){/i}"
    mc "Hey. Didn't you say Andres is helping at the venue?"
    c "Yeah, he is. Why?"
    mc "No reason..."
    scene 06_627 with Dissolve(1)
    mc "{i}(What the fuck is he doing here then? With... whoever that is.){/i}"
    mc "{i}(I guess I have to have more than just one talk with him...){/i}"
    mc "{i}(Fuck me.){/i}"
    scene 06_628 with Dissolve(1)
    mc "Why are we still standing still?"
    c "Red light. Something the matter?"
    mc "No... I just want to get home."
    c "Okay?"
    mc "{i}(Calm down. This could all be a big misunderstanding again. Let's not jump to conclusions...){/i}"
    scene black with Dissolve(1)
    pause 2
    scene 06_654 with Dissolve(1)
    c "Hey Nikki. Look what I've found."
    ni "One second Cara."
    mc "{i}(Heh? Deja vu?){/i}"
    scene 06_655 with Dissolve(1)
    ni "Kay, what is..."
    ni "Oh? Hey!"
    mc "Hey, Nikki. How are you?"
    scene 06_656 with Dissolve(1)
    ni "I'm good, thanks. How about you? I'm so happy you decided to come."
    mc "Good too. I didn't really have a choice..."
    ni "Haha, true."
    scene 06_657 with Dissolve(1)
    ni "How's life in Madison Springs?"
    mc "Eh... It has its ups and downs I guess."
    ni "You have a beach though..."
    mc "Yeah. That's definitely a big up. Went there already last weekend."
    ni "Oh? I'm so jealous..."
    scene 06_658 with Dissolve(1)
    ni "Next time we come to visit you then, right Cara?"
    c "Uhm... Yes..."
    scene 06_659 with Dissolve(1)
    ni "Well, I'd really like to stay and chat, but I have a few more clients today."
    mc "I'm here for a couple of days. We'll find some time to talk."
    ni "Great. If I don't see you again today, save me a dance at the wedding tomorrow."
    mc "Haha, okay..."
    scene black with Dissolve(1)
    pause 2
    scene 06_660 with Dissolve(1)
    c "You can have your old room for the next few days."
    mc "Thanks. It's so empty..."
    mc "Do you already know what will happen to this room?"
    c "Probably stay as a guestroom."
    c "Maybe someone will come and visit once in a while."
    mc "..."
    scene 06_661 with Dissolve(1)
    mc "Haah..."
    c "Hey! You can't be tired now. You still need to teach me how to drive..."
    mc "Hehe, don't worry. I'm good to go."
    scene 06_662 with Dissolve(1)
    mc "Did you ask Haley already for the car?"
    c "No, let me call her."
    scene 06_663 with Dissolve(1)
    c "Uhm... What should I say?"
    mc "Ask her if you can take the car to practice driving."
    c "Okay. But what if she says no?"
    mc "Then we'll do something else."
    scene 06_664 with Dissolve(1)
    c "..."
    c "Hey, Mom."
    c "Yes, he's here."
    c "..."
    c "Mom... I have a question. Can I borrow your car?"
    c "I know. That's why [mc] will teach me."
    c "Yes."
    scene 06_665 with Dissolve(1)
    c "Where? Uh..."
    mc "Empty parking lot."
    c "On an empty parking lot."
    c "..."
    c "Where is that?"
    c "Ah, okay, yeah I know where it is."
    scene 06_666 with Dissolve(1)
    c "..."
    c "Why does she have your keys? She has her own car..."
    c "..."
    c "Yes, we'll be careful."
    scene 06_667 with Dissolve(1)
    c "Thank you."
    c "Bye-bye."
    scene 06_668 with Dissolve(1)
    c "Good to go. She said yes."
    mc "Cool."
    scene 06_669 with Dissolve(1)
    c "Okay, I'm going to change then. Can you go ask Nikki for the keys?"
    mc "Yeah, will do."
    scene 06_648 with Dissolve(1)
    mc "*Sigh*"
    mc "{i}(I actually wanted to talk to you about Andres.){/i}"
    mc "{i}(I guess we'll talk after. Better to keep her mind on the driving...){/i}"
    mc "{i}(Let's ask Nikki for the keys.){/i}"
    scene black with Dissolve(2)
    pause 2
    scene 06_670 with Dissolve(1)
    mc "Hey, Nikki. Do you..."
    scene 06_671 with Dissolve(1)
    ni "[mc]!"
    mc "{i}(Shit.){/i}"
    scene 06_672 with Dissolve(1)
    mc "I'm so sorry... I should've knocked."
    ni "..."
    ni "It's fine. Did you need something?"
    mc "Yeah, Haley's car keys."
    ni "One second."
    mc "..."
    ni "Come on in."
    scene 06_673 with Dissolve(1)
    mc "Sorry, Nikki."
    ni "Here you go."
    mc "Thanks."
    ni "Going somewhere?"
    scene 06_674 with Dissolve(1)
    mc "Teaching Cara how to drive. A little practice lesson."
    ni "That's sweet of you."
    ni "Have fun and be careful, yeah?"
    mc "We will be."
    scene black with Dissolve(1)
    pause 2
    scene 06_675 with Dissolve(1)
    c "Okay, I'm ready."
    mc "{i}(Wow...){/i}"
    scene black with Dissolve(1)
    transform moveup:
        xalign 0.5 yalign 1.0
        linear 5.0 yalign 0.0
    show 06_678 at moveup
    pause 3
    menu:
        "Joke[KoGa3AutoWTChange1]{size=-4}(Cara Weekend Points+2) {/size} {/color}":
            $ Cara_Weekend_Points += 2
            # Cara_Weekend (2)
            mc "What's with that outfit?"
            c "What?"
            mc "Are you trying to seduce your driving instructor?"
            scene 06_679 with Dissolve(1)
            c "..."
            c "You're my instructor."
            mc "Exactly... It's just practice, you know."
            scene 06_680 with Dissolve(1)
            c "*Sigh* I'll go change."
            mc "I'm kidding. It's fine. You look really cute."
            c "..."
            c "Thanks."
            scene 06_681 with Dissolve(1)
            mc "I would change your shoes though. Put some sneakers on or something."
            mc "That will make it easier."
            c "I'll change them quick."
        "Let's go":
            mc "Okay. Let's go."
            scene 06_681 with Dissolve(1)
            mc "I would change your shoes though. Put some sneakers on or something."
            mc "That will make it easier."
            c "I'll change them quick."
    scene black with Dissolve(1)
    pause 2
    scene 06_686 with Dissolve(1)
    mc "Excited?"
    c "Yes, and nervous. Thank you for doing this."
    mc "My pleasure. Well, maybe. I'll know once I see how you drive."
    c "Haha."
    menu:
        "Mention hair[KoGa3AutoWTChange1]{size=-4}(Cara Weekend Points+2) {/size} {/color}":
            scene 06_687 with Dissolve(1)
            $ Cara_Weekend_Points += 2
            # Cara_Weekend (4)
            mc "I like what you did with your hair."
            c "{i}(Oh? He actually noticed...){/i}"
            c "Thank you..."
            scene 06_688 with Dissolve(1)
            mc "Here you go miss, please have a seat."
            c "Full service, huh?"
            mc "Everything for my one and only student."
            c "Haha. Thank you."
            scene 06_689 with Dissolve(1)
            c "..."
            c "{i}(My one and only...){/i}"
        "Say nothing":
            scene 06_688 with Dissolve(1)
            mc "Here you go miss, please have a seat."
            c "Full service, huh?"
            mc "Of course."
            c "Thank you."
    scene black with Dissolve(1)
    pause 2
    scene 06_744 with Dissolve(1)
    mc "Oh? This is an automatic. This will make things much easier."
    c "Yeah?"
    mc "Only two pedals instead of three and no manual gearchanges."
    c "Okay?"
    scene 06_745 with Dissolve(1)
    mc "I'll explain once we're there."
    mc "You know the way?"
    c "Yes, just follow Main Street for now."
    scene black with Dissolve(1)
    pause 2
    scene 06_746 with Dissolve(1)
    c "Next intersection, you need to go left."
    mc "Never been here before."
    c "Yeah, mostly industry and bigger supermarkets are located here."
    scene black with Dissolve(1)
    pause 2
    scene 06_747 with Dissolve(1)
    mc "This place is perfect for practice. Completely empty."
    c "Yeah, and no one watching me fail miserably."
    mc "Don't worry, you'll do fine."
    mc "Let's start this."
    scene 06_748 with Dissolve(1)
    mc "This is your transmission."
    mc "You see the letters here?"
    c "Uh-huh."
    scene 06_749 with Dissolve(1)
    mc "P is for parking, R for reverse, N neutral, and D is drive."
    mc "The others aren't important for now."
    scene 06_750 with Dissolve(1)
    mc "Hey! Are you paying attention?"
    c "Yes I am, Mr Instructor!"
    mc "..."
    scene black with Dissolve(1)
    pause 2
    scene 06_751 with Dissolve(1)
    mc "Then we have two pedals down here."
    c "I see them."
    mc "{i}(What is she doing...){/i}"
    scene 06_752 with Dissolve(1)
    mc "Haha..."
    c "Why are you laughing?"
    menu:
        "Tell her":
            mc "Good thing this is an empty parking lot. If people had seen you, they'd think you were giving me a blowjob."
            c "Ew... Why would you even say that? You told me to pay attention..."
            c "I need to concentrate, okay?"
            mc "You're right, I'm sorry... Let's continue."
        "Don't":
            mc "It's nothing. Just a stupid thought."
            c "..."
            mc "Let's continue."
    scene black with Dissolve(1)
    pause 2
    scene 06_754 with Dissolve(1)
    mc "That's about it. Ready to give it a go?"
    c "I don't know... What if I hit something?"
    mc "It's an empty parking lot, there's nothing to hit... It would be impressive actually if you were able to hit something."
    c "..."
    mc "Besides. What happened to your confidence?"
    c "It's scary, you know?"
    mc "Come on... Let's change seats."
    scene 06_755 with Dissolve(1)
    c "Can't we do it together for the first time?"
    menu:
        "Joke[KoGa3AutoWTChange1]{size=-4}(Cara Weekend Points-2) {/size} {/color}":
            $ Cara_Weekend_Points -= 2
            scene 06_753 with Dissolve(1)
            mc "I'm sorry to inform you, but your first time..."
            c "Can you be serious for once? This might be a joke to you, but I really want to learn."
            mc "Sorry, sorry..."
            scene 06_755 with Dissolve(1)
            mc "Okay, what do you have in mind?"
        "Leave it be":
            mc "What? How are we supposed to do that?"
    c "I'll sit on your lap and steer while you do the pedals?"
    mc "..."
    c "Please?"
    scene black with Dissolve(1)
    pause 2
    scene 06_756 with Dissolve(1)
    c "Okay, you can let go of the brake."
    c "Accelerate a little."
    c "This is easy."
    mc "..."
    mc "{i}(She's so cute.){/i}"
    mc "You're doing good."
    scene 06_757 with Dissolve(1)
    mc "{i}(If this happened back then, I would...){/i}"
    mc "{i}(Oh fuck...){/i}"
    mc "{i}(Why did I agree to this? I should've known this would happen.){/i}"
    c "{i}(Is that his...){/i}"
    scene 06_758 with Dissolve(1)
    mc "How about you try on your own now, yes?"
    c "..."
    if Cara_Weekend_Points == 4:
        c "{i}(But I like it this way...){/i}"
        c "Yeah."
    else:
        c "Yeah."
    scene black with Dissolve(1)
    pause 2
    scene 06_759 with Dissolve(1)
    mc "Put your foot on the brake, change it to drive and then slowly let go of the brake."
    mc "The car will start moving on its own."
    scene 06_760 with Dissolve(1)
    c "Oh my god, [mc], I'm doing it."
    c "Look..."
    scene 06_761 with Dissolve(1)
    c "Look!"
    mc "Eyes up front."
    scene 06_760 with Dissolve(1)
    c "Sorry, sorry. Haha. I'm driving!"
    scene black with Dissolve(1)
    pause 2
    scene 06_762 with Dissolve(1)
    c "I did it."
    mc "You did great. With a few more practices with Nikki or your mom, you'll be good to go."
    c "Thank you so much for this."
    if Cara_Weekend_Points == 4:
        scene 06_763 with Dissolve(1)
        mc "..."
        c "{i}(I miss this... Spending time with you. I miss you...){/i}"
        mc "So, shall we head home?"
    else:
        mc "So, shall we head home?"
    scene 06_764 with Dissolve(1)
    c "Or we could maybe grab something to drink?"
    menu:
        "Okay[KoGa3AutoWTChange1]{size=-4}(Cara Weekend Points+2) {/size} {/color}":
            $ Cara_Weekend_Points += 2
            # Cara_Weekend (6)
            mc "Yeah, I'm up for that. Maybe something to eat, too?"
            c "We can do that."
            scene 06_765 with Dissolve(1)
            c "Okay, let's go, I'll drive..."
            mc "Haha Cara, you wish."
            scene black with Dissolve(1)
            pause 2
            scene 06_766 with Dissolve(1)
            mc "Why are there no free parking spaces? This is ridiculous."
            c "It's Friday. Everyone's out tonight."
            mc "Yeah, seems like it."
            scene 06_767 with Dissolve(1)
            mc "How about I let you out here and you can look for a table?"
            mc "In the meantime, I'll search for a place to park the car."
            c "Sure."
            scene 06_768 with Dissolve(1)
            mc "Okay, see you soon, I hope."
            c "Haha. Don't leave me for too long."
            scene black with Dissolve(1)
            pause 2
            scene 06_769 with Dissolve(1)
            x "Hey there, babe. What are you doing here all alone?"
            c "Waiting..."
            scene 06_770 with Dissolve(1)
            x "Guess what. I'm here, you no longer need to wait."
            c "..."
            scene 06_771 with Dissolve(1)
            x "You don't have to be shy, cutie."
            mc "{i}(What is he trying to accomplish?){/i}"
            scene black with Dissolve(1)
            transform moveup:
                xalign 0.5 yalign 1.0
                linear 5.0 yalign 0.0
            show 06_772 at moveup
            pause 3
            mc "{i}(He's right though. She looks really cute.){/i}"
            scene 06_773 with Dissolve(1)
            x "What's your name?"
            c "Don't touch me."
            x "Oh come on baby, don't be like that. I know you like it..."
            menu:
                "Let her handle it":
                    scene 06_774 with vpunch
                    n "*Slap*"
                    c "I said don't touch me!"
                    x "Aaah..."
                    x "What the fuck."
                    scene 06_775 with Dissolve(1)
                    mc "You heard what she said. You'd better leave or you'll be slapped again, this time by me. And it won't be a slap!"
                    x "Chill man... I'm leaving, okay? You'd better watch out. You know what they say. Redheads are crazy..."
                    c "..."
                    scene 06_776 with Dissolve(1)
                    mc "Are you alright?"
                    c "Yeah... Thank you."
                    mc "No. That was all you. Sorry for making you wait."
                "Intervene":
                    scene 06_777 with Dissolve(1)
                    mc "Hey gorgeous. Thanks for waiting."
                    c "Hey. Finally!"
                    scene 06_778 with Dissolve(1)
                    x "Why didn't you say you have a boyfriend?"
                    c "{i}(Boyfriend...){/i}"
            scene black with Dissolve(1)
            pause 2
            scene 06_779 with Dissolve(1)
            c "Water? You don't want to drink?"
            mc "I still need to drive later, so..."
            c "I could..."
            mc "No!"
            c "You don't even know what I was about to say."
            mc "Uh-huh..."
            c "Haha."
            if Cara_Weekend_Points >= 3:
                scene black with Dissolve(1)
                pause 2
                scene 06_780 with Dissolve(1)
                c "Where have you parked?"
                mc "Pretty far..."
                mc "It's on the other side of the park. There were no free spaces anywhere."
                c "Okay."
                scene 06_781 with Dissolve(1)
                c "Oh?"
                c "Come, let's sit here for a moment."
                scene 06_782 with Dissolve(1)
                c "Do you remember this bench?"
                mc "I do."
                mc "But the thing you said back then, isn't true anymore..."
                c "Haha, stop."
                scene 06_783 with Dissolve(1)
                mc "..."
                mc "Stealing my moves, huh?"
                c "Uh-huh..."
                c "I like this."
                scene 06_784 with Dissolve(1)
                mc "I hope you're wearing panties, or people..."
                c "Of course I am. Don't ruin my moment."
                mc "Haha..."
                scene black with Dissolve(2)
                pause 2
                scene 06_785 with Dissolve(1)
                c "In a few hours, we will officially be brother and sister."
                mc "..."
                mc "{i}(Damn... Why haven't I said anything yet... Don't I want to tell her?){/i}"
                mc "{i}(I think I should talk to Andres first, to hear both sides.){/i}"
                mc "..."
                mc "{i}(And I need to talk to him about the picture... To know for sure what's going on with that woman before it becomes a misunderstanding and I ruin something else.){/i}"
                mc "{i}(Why is everything so complicated?){/i}"
                scene 06_786 with Dissolve(1)
                mc "{i}(And why can't I tell her that I still like her?){/i}"
                c "Hmm?"
                c "{i}(Something on his mind?){/i}"
                scene 06_787 with Dissolve(1)
                mc "Today was fun. You look very pretty by the way."
                c "..."
                mc "I li... I missed spending time with you..."
                c "..."
                scene 06_788 with Dissolve(1)
                mc "I wish we met earlier. Before... you know."
                c "{i}(Stop... This is hard enough already.){/i}"
                mc "..."
                c "*Sigh*"
                scene 06_789 with Dissolve(1)
                c "Here, feel better?"
                scene 06_790 with Dissolve(1)
                c "Seeing how you're spewing nonsense, you must be exhausted."
                mc "{i}(She's right. We shouldn't do this...){/i}"
                mc "{i}(Why do I feel so bad about it though. My heart's pounding like crazy.){/i}"
                mc "Yeah... You might be right."
                c "..."
                c "Let's go home."
                jump Week2_Weekend_Cara_Continue
            else:
                jump Week2_Weekend_Cara_End
        "No":
            mc "I'd rather go home and relax a little."
            c "I must have been a handful, huh?"
            mc "Hehe. No. Just the long flight."
            scene 06_765 with Dissolve(1)
            c "Okay, let's go home then, I'll drive..."
            mc "Haha, Cara, you wish."
            if Cara_Weekend_Points >= 3:
                jump Week2_Weekend_Cara_Continue
            else:
                jump Week2_Weekend_Cara_End

label Week2_Weekend_Cara_End:
    $ Cara_Girlfriend = False
    $ Riverside_Friends = True
    $ Nikki_SP = False
    scene black with Dissolve(4)
    pause 2
    scene 06_791 with Dissolve(1)
    mc "{i}(Two o'clock already...){/i}"
    n "*Knock-knock*"
    scene 06_792 with Dissolve(1)
    mc "Yeah?"
    scene 06_801 with Dissolve(1)
    c "Hey!"
    mc "Hey, come on in."
    c "Thanks. I saw that the lights were still on."
    scene 06_802 with Dissolve(1)
    c "You can't sleep either?"
    mc "No, I tried, but... nothing."
    c "Too excited for the wedding?"
    mc "No, it's something else. I need..."
    scene 06_803 with Dissolve(1)
    c "I have an idea."
    mc "Yeah?"
    c "Let's play a game or something."
    mc "Sure, what kind of game?"
    c "A card game, maybe?"
    mc "You have a deck?"
    scene 06_804 with Dissolve(1)
    c "Yeah, let me get it real quick."
    mc "Want to ask Nikki if she wants to join?"
    c "I was in her room before I came here. She's sleeping already."
    mc "Oh, okay."
    mc "{i}(Let's play a few games, but then I really need to tell her.){/i}"
    scene black with Dissolve(1)
    pause 2
    scene 06_805 with Dissolve(1)
    c "Let's make it interesting."
    mc "What do you have in mind?"
    c "The loser has to do something embarrassing at the wedding party."
    mc "I'm totally game for that."
    scene 06_806 with Dissolve(1)
    mc "Can't wait to see what you're about to do."
    c "Hey! Who says I'm going to lose?"
    mc "Haha..."
    scene black with Dissolve(2)
    pause 2
    stop music fadeout 1.0
    play music "Music/Battle_Rock2.mp3" volume 0.5
    n "Saturday, 08:23."
    scene 06_807 with Dissolve(1)
    d "[mc], are you awake already?"
    scene 06_808a with Dissolve(1)
    d "..."
    d "What's going on here?"
    scene 06_809a with Dissolve(1)
    c "Aaah... Andres!"
    mc "Get out!"
    scene 06_810 with Dissolve(1)
    d "Not before you tell me what's going on here."
    mc "Just get out already..."
    d "That's why you wanted to live with your mom again, right? You've been sleeping with each other behind our backs?"
    c "..."
    d "This is wrong. What are you trying to accomplish? Are you rebelling against this marriage?"
    scene 06_811a with Dissolve(1)
    mc "Rebelling... Obviously..."
    c "..."
    mc "Can you stop jumping to conclusions? We just played cards late last night and fell asleep."
    d "Playing cards... Half naked..."
    mc "We're wearing clothes, aren't we?"
    d "..."
    scene 06_812 with Dissolve(1)
    mc "And why would this even matter? This doesn't have anything to do with you."
    d "Nothing to do with me? How can you be so stupid! I can't believe you were hiding this from us all this time."
    mc "We didn't sleep with each other..."
    d "Don't bullshit me. I know when you are lying."
    mc "Oh yeah... I'm the one lying. Like you've been telling me everything, right?"
    d "I've always been truthful."
    scene 06_813 with Dissolve(1)
    mc "Okay. Let's see. Hmm... How about the fact that you aren't my real dad?"
    d "..."
    scene 06_814a with Dissolve(1)
    c "What?"
    c "[mc]?"
    scene 06_815 with Dissolve(1)
    d "Heh. You've been living with her for two weeks and she's already broken her promise..."
    d "Should've known."
    mc "No. You should have told me way before. Actually, you should've never asked for such a promise to begin with. It wasn't your decision to make..."
    d "Yeah. I'm not your real dad. Now you've heard it from me. Happy?"
    mc "..."
    scene 06_816 with Dissolve(1)
    d "So what are you doing here then, huh? There's no reason for you to be here. Go live your life with your mom."
    mc "Wow... You were my dad for so many years. And in a way you still are. I came to support you and talk to you about all this. Seems like it was a mistake."
    d "..."
    scene 06_817a with Dissolve(1)
    c "Uhm..."
    c "Guys?"
    scene 06_818 with Dissolve(1)
    d "Support me? You call this supporting me? Sleeping with my soon-to-be step-daughter."
    mc "We..."
    d "You're just like your mom. Sleeping around and not caring about the consequences."
    mc "Leave her out of it."
    d "Afraid of what I'm going to say?"
    mc "No... This has nothing to do with her."
    d "Do you know how our relationship ended? I'll tell you. She was sleeping around with your real dad."
    mc "She met up with him to talk. Nothing more."
    scene 06_819 with Dissolve(1)
    d "That's what she told you? That cheating bitch!"
    mc "HEY! Don't talk about her like that."
    d "She ruined everything."
    mc "Haha. Totally. It's all her fault. You like to blame others. A bad habit I got from you by the way."
    mc "If you want to know who is the real cheat and ruins relationships, look in a mirror. You'll be surprised."
    d "What are you talking about?"
    scene 06_820 with Dissolve(1)
    mc "I saw you. Yesterday."
    d "Where?"
    mc "In the city."
    d "I wasn't in the city."
    mc "{i}(One lie after another.){/i}"
    mc "Then tell me, where were you?"
    d "I was with Haley the whole day. Preparing for the wedding."
    scene 06_821 with Dissolve(1)
    mc "Always been truthful, huh?"
    mc "How do you explain this then?"
    d "..."
    d "Where did you get that?"
    mc "As I said, I saw you."
    d "Heh. She's just a colleague..."
    scene 06_822 with Dissolve(1)
    mc "So first of all, you weren't with Haley."
    mc "Second. Do you always put your arm around your female colleagues?"
    d "What?"
    mc "How about we ask Haley if she knows her?"
    mc "You work at the same company. She should know her, right?"
    scene 06_823a with Dissolve(1)
    c "Andres?"
    c "Are you cheating on Mom?"
    mc "{i}(I'm so sorry you had to find out this way, Cara.){/i}"
    scene 06_824a with Dissolve(1)
    d "Give me that!"
    mc "No..."
    c "Andres! Stop!"
    scene 06_825 with vpunch
    mc "..."
    scene 06_826 with Dissolve(1)
    mc "Smashing my phone... Do you think that will change the facts?"
    mc "Now I finally understand why you didn't tell me about Haley for about a year."
    mc "Scared to mix up their names?"
    scene 06_827a with vpunch
    d "You son of a bitch."
    c "[mc]!"
    menu:
        "Hit him back":
            scene 06_828a with vpunch
            mc "You never deserved Mom. And you don't deserve Haley and this family!"
            c "[mc]! Please stop!"
            scene 06_830a with Dissolve(1)
            c "And you get out of my house."
            d "Cara, let me..."
            c "LEAVE! GET OUT!"
        "Don't hit him":
            scene 06_829a with Dissolve(1)
            mc "You never deserved Mom. And you don't deserve Haley and this family!"
            c "[mc], don't!"
            scene 06_830a with Dissolve(1)
            c "What are you doing? How can you even hit him..."
            d "Cara, let me..."
            c "LEAVE! GET OUT!"
    scene black with Dissolve(1)
    pause 2
    scene 06_831a with Dissolve(1)
    c "Are you alright?"
    mc "Yeah... How about you?"
    scene 06_832a with Dissolve(1)
    c "Why didn't you tell me he isn't your father? And more importantly that he's cheating on my mom!"
    mc "I wanted to. I wasn't sure if... I just..."
    c "When?"
    c "When they were married?"
    scene 06_833a with Dissolve(1)
    mc "No... I needed to hear it from him first before I said something that maybe would've been a misunderstanding."
    mc "I've made so many mistakes lately because I didn't listen and let people explain. I needed to be sure."
    scene 06_834a with Dissolve(1)
    c "..."
    c "You know what was a mistake? This here!"
    scene 06_835a with Dissolve(1)
    mc "Cara..."
    c "I need to go find Mom."
    mc "I'm sorry."
    c "I'm sorry too..."
    scene black with Dissolve(1)
    pause 2
    scene 06_836 with Dissolve(1)
    mc "{i}(Fuck... Wherever I go, I ruin something.){/i}"
    mc "..."
    scene black with Dissolve(1)
    pause 2
    scene 06_837a with Dissolve(1)
    n "Cara, I'm sorry. I never..."
    jump Week2_Weekend_NikkiCara_End

label Week2_Weekend_Cara_Continue:
    if _in_replay:
        $ MC_SexCounter = 2
        $ SexCounter_Cara = 2
    $ MC_SexCounter += 1
    $ SexCounter_Cara += 1
    # Cara_Sex (3)
    scene black with Dissolve(2)
    pause 2
    scene 06_791 with Dissolve(1)
    mc "{i}(Two o'clock already...){/i}"
    n "*Knock-knock*"
    scene 06_793 with Dissolve(1)
    mc "Cara?"
    scene black with Dissolve(1)
    transform moveup:
        xalign 0.5 yalign 1.0
        linear 5.0 yalign 0.0
    show 06_875 at moveup
    pause 3
    mc "Can't you sleep?"
    c "..."
    scene 06_876 with Dissolve(1)
    mc "What's wrong?"
    c "..."
    scene 06_877 with Dissolve(1)
    mc "Hey. Did something happen?"
    c "..."
    scene 06_878 with Dissolve(1)
    mc "..."
    scene 06_879 with Dissolve(1)
    mc "Uh Cara... We shouldn't."
    c "I know... But..."
    c "*Sigh*"
    mc "{i}(Why do I want this so bad?){/i}"
    mc "..."
    scene 06_880 with Dissolve(1)
    ""
    scene 06_881 with vpunch
    c "Aaah..."
    scene 06_882 with Dissolve(1)
    c "The moment I saw you at the airport. I wanted this..."
    mc "I feel the same way."
    scene black with Dissolve(2)
    pause 2
    scene 06_883 with Dissolve(1)
    ""
    scene 06_884 with Dissolve(1)
    c "Mmm [mc]..."
    scene black with Dissolve(1)
    pause 2
    scene 06_885 with Dissolve(1)
    c "I can feel you're hard already..."
    mc "Can you blame me?"
    scene 06_886 with Dissolve(1)
    c "Earlier in the car, and in the park too..."
    mc "I know..."
    scene 06_887 with Dissolve(1)
    mc "{i}(Since when is she so forward...?){/i}"
    mc "{i}(This feels so good.){/i}"
    scene 06_888 with Dissolve(1)
    mc "..."
    scene black with Dissolve(1)
    pause 2
    scene 06_889 with Dissolve(1)
    mc "{i}(I love it when she takes control.){/i}"
    scene 06_889a with Dissolve(1)
    ""
    scene 06_890 with Dissolve(1)
    mc "{i}(She's so much more confident.){/i}"
    show 06_891
    ""
    scene 06_892 with Dissolve(1)
    ""
    scene 06_893 with Dissolve(1)
    c "{i}(He makes me feel so good...){/i}"
    scene black with Dissolve(1)
    pause 2
    scene 06_894 with Dissolve(1)
    ""
    scene 06_895 with Dissolve(1)
    c "Want to try something new?"
    mc "Who are you?"
    c "Haha..."
    scene black with Dissolve(1)
    pause 2
    scene 06_896 with Dissolve(1)
    mc "{i}(That's definitely new...){/i}"
    mc "..."
    scene 06_897 with vpunch
    c "Aaah..."
    scene 06_898 with Dissolve(1)
    c "{i}(Not what I had in mind but...){/i}"
    scene black with Dissolve(1)
    pause 2
    scene 06_899 with Dissolve(1)
    ""
    scene 06_900 with Dissolve(1)
    mc "Cara... I'm..."
    menu:
        "Pull out":
             scene 06_901 with vpunch
             ""
             scene 06_901 with vpunch
             ""
        "Cum inside[KoGa3AutoWTChange1]{size=-4}(Cara Week2 Weekend SexInside) {/size} {/color}":
            $ Cara_Week2_Weekend_SexInside = True
            scene 06_902 with vpunch
            ""
            scene 06_902 with vpunch
            ""
    scene black with Dissolve(1)
    pause 2
    scene 06_903 with Dissolve(1)
    mc "Wow. You were amazing. Where did that all come from?"
    c "Haha. I watched some videos."
    mc "Videos? Haha..."
    c "Don't laugh! You watch them too."
    mc "I don't have to when I'm with you..."
    c "..."
    $ renpy.end_replay()
    scene black with Dissolve(2)
    pause 2
    stop music fadeout 1.0
    play music "Music/Battle_Rock2.mp3" volume 0.5
    n "Saturday, 08:23."
    scene 06_807 with Dissolve(1)
    d "[mc], are you awake already?"
    scene 06_808a_01 with Dissolve(1)
    d "..."
    d "What's going on here?"
    scene 06_809a_01 with Dissolve(1)
    c "Aaah... Andres."
    mc "Get out!"
    scene 06_810 with Dissolve(1)
    d "Not before you tell me what's going on here."
    mc "Just get out already..."
    d "That's why you wanted to live with your mom again, right? You've been sleeping with each other behind our backs?"
    c "..."
    scene 06_811b_01 with Dissolve(1)
    mc "Sorry."
    mc "Here, wear this in the meantime."
    c "Thank you."
    scene 06_811a_01 with Dissolve(1)
    d "This is wrong. What are you trying to accomplish? Are you rebelling against this marriage?"
    mc "Rebelling..."
    c "..."
    scene 06_812 with Dissolve(1)
    mc "No... We like each other. And why would this even matter? This doesn't have anything to do with you."
    d "Nothing to do with me? Like each other? How can you be so stupid! With her?"
    c "Excuse me?"
    d "I can't believe you were hiding this from us all this time."
    mc "Oh yeah... Like you've been telling me everything, right?"
    d "I've always been truthful."
    scene 06_813 with Dissolve(1)
    mc "Okay. Let's see. Hmm... How about the fact that you aren't my real dad?"
    d "..."
    scene 06_814a_01 with Dissolve(1)
    c "What?"
    c "[mc]?"
    scene 06_815 with Dissolve(1)
    d "Heh. You've been living with her for two weeks and she's already broken her promise..."
    d "Should've known."
    mc "No. You should have told me way before. Actually, you should've never asked for such a promise to begin with. It wasn't your decision to make..."
    d "Yeah. I'm not your real dad. Now you've heard it from me. Happy?"
    mc "..."
    scene 06_816 with Dissolve(1)
    d "So what are you doing here then, huh? There's no reason for you to be here. Go live your life with your mom."
    mc "Wow... You were my dad for so many years. And in a way you still are. I came to support you and talk to you about all this. Seems like it was a mistake."
    d "..."
    scene 06_817a_01 with Dissolve(1)
    c "Uhm..."
    c "Guys?"
    scene 06_818 with Dissolve(1)
    d "Support me? You call this supporting me? Sleeping with my soon-to-be step-daughter."
    mc "We..."
    d "You're just like your mom. Sleeping around and not caring about the consequences."
    mc "Leave her out of it."
    d "Afraid of what I'm going to say?"
    mc "No... This has nothing to do with her."
    d "Do you know how our relationship ended? I'll tell you. She was sleeping around with your real dad."
    mc "She met up with him to talk. Nothing more."
    scene 06_819 with Dissolve(1)
    d "That's what she told you? That cheating bitch!"
    mc "HEY! Don't talk about her like that."
    d "She ruined everything."
    mc "Haha. Totally. It's all her fault. You like to blame others. A bad habit I got from you by the way."
    mc "If you want to know who is the real cheat and ruins relationships, look in a mirror. You'll be surprised."
    d "What are you talking about?"
    scene 06_820 with Dissolve(1)
    mc "I saw you. Yesterday."
    d "Where?"
    mc "In the city."
    d "I wasn't in the city."
    mc "{i}(One lie after another.){/i}"
    mc "Then tell me, where were you?"
    d "I was with Haley the whole day. Preparing for the wedding."
    scene 06_821 with Dissolve(1)
    mc "Always been truthful, huh?"
    mc "How do you explain this then?"
    d "..."
    d "Where did you get that?"
    mc "As I said, I saw you."
    d "Heh. She's just a colleague..."
    scene 06_822 with Dissolve(1)
    mc "So first of all, you weren't with Haley."
    mc "Second. Do you always put your arm around your female colleagues?"
    d "What?"
    mc "How about we ask Haley if she knows her?"
    mc "You work at the same company. She should know her, right?"
    scene 06_823a_01 with Dissolve(1)
    c "Andres?"
    c "Are you cheating on Mom?"
    mc "{i}(I'm so sorry you had to find out this way, Cara.){/i}"
    scene 06_824a_01 with Dissolve(1)
    d "Give me that!"
    mc "No..."
    c "Andres! Stop!"
    scene 06_825 with vpunch
    mc "..."
    scene 06_826 with Dissolve(1)
    mc "Smashing my phone... Do you think that will change the facts?"
    mc "Now I finally understand why you didn't tell me about Haley for about a year."
    mc "Scared to mix up their names?"
    scene 06_827a_01 with vpunch
    d "You son of a bitch."
    c "[mc]!"
    menu:
        "Hit him back[KoGa3AutoWTChange1]{size=-4}(Cara Weekend Points-2) {/size} {/color}":
            $ Cara_Weekend_Points -= 2
            scene 06_828a_01 with vpunch
            mc "You never deserved Mom. And you don't deserve Haley and this family!"
            c "[mc]! Please stop!"
            scene 06_830a_01 with Dissolve(1)
            c "And you get out of my house."
            d "Cara, let me..."
            c "LEAVE! GET OUT!"
        "Don't hit him[KoGa3AutoWTChange1]{size=-4}(Riverside End, Nikki SPFalse) {/size} {/color}":
            scene 06_829a_01 with Dissolve(1)
            mc "You never deserved Mom. And you don't deserve Haley and this family!"
            c "[mc], don't!"
            scene 06_830a_01 with Dissolve(1)
            c "What are you doing? How can you even hit him..."
            d "Cara, let me..."
            c "LEAVE! GET OUT!"
    scene black with Dissolve(1)
    pause 2
    scene 06_831a_01 with Dissolve(1)
    c "Are you alright?"
    mc "Yeah... How about you?"
    scene 06_832a_01 with Dissolve(1)
    c "Why didn't you tell me he isn't your father? And more importantly that he's cheating on my mom!"
    mc "I wanted to. I wasn't sure if... I just..."
    c "When?"
    c "When they were married?"
    scene 06_833a_01 with Dissolve(1)
    mc "No... I needed to hear it from him first before I said something that maybe would've been a misunderstanding."
    mc "I've made so many mistakes lately because I didn't listen and let people explain. I needed to be sure."
    scene 06_834a_01 with Dissolve(1)
    c "..."
    c "You know what was a mistake? This here!"
    scene 06_835a_01 with Dissolve(1)
    mc "Cara..."
    c "I need to go find Mom."
    mc "I'm sorry."
    c "I'm sorry, too..."
    scene black with Dissolve(1)
    pause 2
    scene 06_836 with Dissolve(1)
    mc "{i}(Fuck... Wherever I go, I ruin something.){/i}"
    mc "..."
    scene black with Dissolve(1)
    pause 2
    scene 06_837a with Dissolve(1)
    n "Cara, I'm sorry. I never..."
    if Cara_Weekend_Points >= 3:
        scene black with Dissolve(2)
        pause 2
        scene 06_904 with Dissolve(1)
        mc "{i}(It was the right decision to leave, right?){/i}"
        mc "{i}(They probably don't want to see me, anyway.){/i}"
        c "[mc]!"
        scene 06_905 with Dissolve(1)
        mc "Cara?"
        c "Please wait."
        c "Where are you going?"
        mc "Home..."
        scene 06_906_01 with Dissolve(1)
        mc "I shouldn't have come. I ruined everything... Again."
        c "No. You didn't."
        mc "I'm sorry Cara."
        c "[mc], you didn't! You saved her from making a horrible mistake."
        mc "..."
        scene 06_907_01 with Dissolve(1)
        c "Don't leave. I don't want you to go [mc]."
        c "I'm sorry that I called us a mistake. I was mad. I didn't mean it. You're the best thing that could've happened to me."
        mc "..."
        c "Stay and move back in with us."
        mc "Cara, be realistic. That won't work. I'll always remind Haley of Andres and..."
        c "No, you're nothing like him. She likes you."
        mc "..."
        mc "*Sigh* I can't leave my mom. I won't do that to her again. I've hurt her so much already."
        ju "Hey, [mc]."
        scene 06_908_01 with Dissolve(1)
        ju "Long time no see. Where've you been these last few weeks?"
        ju "Skipping school is bad!"
        mc "Not now, Julia..."
        ju "Wow... Someone's in a mood."
        ju "Hey, Cara."
        c "Hey."
        if Julia_FB_Sex == True:
            $ Cara_Girlfriend = False
            $ Riverside_End = True
            $ Nikki_SP = False
            scene 06_909_01 with Dissolve(1)
            ju "{i}(What are they doing here together?){/i}"
            ju "{i}(Are they dating? She hasn't told me... I thought she didn't like him like that...){/i}"
            ju "Remember, if you want to have fun again. call me [mc]. Last time was great!"
            mc "..."
            mc "{i}(What is she doing?){/i}"
            scene 06_910_01 with Dissolve(1)
            c "What are you talking about?"
            ju "Nothing Cara! Don't worry. We just had a little... something at the club, right, [mc]? Haha."
            c "Something?"
            c "When was that?"
            ju "A few weeks ago..."
            mc "..."
            scene 06_911_01 with Dissolve(1)
            mc "Sorry, Cara. I..."
            c "It's true?"
            c "I guess I was wrong. Nothing like him? Heh... Are you sure you and Andres aren't related?"
            c "I can't believe I cared..."
            scene 06_912_01 with Dissolve(1)
            mc "Cara..."
            c "No. Go home or wherever... Ruin someone else's life."
            mc "Cara!"
            scene 06_913 with Dissolve(1)
            mc "Fuck!"
            mc "Thanks, Julia."
            ju "What did I do?"
            jump Week2_Weekend_NikkiCara_End
        else:
            ju "I guess I'm interrupting. I'll leave you two. Bye-bye."
            ju "{i}(Are they dating? She hasn't told me anything...){/i}"
            scene black with Dissolve(1)
            pause 2
            scene 06_914_01 with Dissolve(1)
            mc "My bus is here."
            c "You're really leaving?"
            mc "I have to."
            c "Then I'll come with you."
            mc "Thanks, but no... This is hard enough already..."
            scene 06_915_01 with Dissolve(1)
            c "[mc]..."
            mc "Bye, Cara."
            c "..."
            scene 06_916_01 with Dissolve(1)
            c "[mc]!"
            c "Wait!"
            scene 06_917_01 with Dissolve(1)
            mc "..."
            scene black with Dissolve(1)
            pause 2
            scene 06_918_01 with Dissolve(1)
            c "I love you!"
            jump Week2_Weekend_NikkiCara_End
    else:
        $ Cara_Girlfriend = False
        $ Riverside_Friends = True
        $ Nikki_SP = False
        jump Week2_Weekend_NikkiCara_End

label Week2_Weekend_NikkiCara_End:
    scene black with Dissolve(2)
    pause 2
    stop music fadeout 1.0
    play music "Sounds/Aeroplane_Onboard.mp3" volume 0.3
    scene 06_919 with Dissolve(1)
    if Nikki_FB_Choose == True:
        mc "{i}(I'm so sorry, Nikki...){/i}"
    else:
        mc "{i}(I'm so sorry, Cara...){/i}"
    mc "{i}(I should never have come...){/i}"
    mc "{i}(Now I've hurt her too.){/i}"
    mc "{i}(Whatever I do, wherever I go... it's just...){/i}"
    x "Hey!"
    scene 06_920 with Dissolve(1)
    mc "..."
    mc "Hey. What are you doing here?"
    jump Episode_7_Start

# Max Points:

# Alexis (30)
# Melissa (14)
# Layla (46)
# Elena (14)
# Emily (10)
# Erynn (28)
# Tori (2)
# Cara (16)
# Nikki (20)
# Lakeyn (6)
# Brooke (2)
# Adriana (4)
# Naomi (2)

# MC_GoodStudent (14)

# Nikki_Weekend (10)
# Cara_Weekend (6)

# MC_Sex (15)
# Alexis_Sex (5)
# Tori_Sex (1)
# Lakeyn_Sex (1)
# Nikki_Sex (3)
# Cara_Sex (3)
# Julia_Sex (1)
# Rachel_Sex (1)

#WTAdded