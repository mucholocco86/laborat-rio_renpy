#ch1 scene 7
label ch1sc7:

    #play music

    #start scene 7
    window hide dissolve
    scene black with Dissolve (2.0)
    window show dissolve

    $ renpy.pause(1)
    play music forestnight_1
    scene ch1sc7_01 with Dissolve(2.0)
    $ renpy.pause(1)
    al "[mc]... [mc]! Wake up!"
    scene ch1sc7_02 with dissolve
    mc "Hmmmh..."
    scene ch1sc7_03 with dissolve
    $ renpy.pause(1)
    scene ch1sc7_04 with dissolve
    $ renpy.pause(1)
    scene ch1sc7_05 with dissolve
    mc "Huh? Alice?"
    scene ch1sc7_06 with dissolve
    al "Come on, [mc]! It’s dark... we need to get home!"
    scene ch1sc7_07 with dissolve
    al "I heard some rustling in the bushes..."
    scene ch1sc7_04 with dissolve
    mct "Alice must be scared, but she doesn’t want to admit it."
    scene ch1sc7_08 with dissolve
    $ renpy.pause(1)
    scene ch1sc7_09 with dissolve
    mc "I can’t believe we slept that long."
    mc "Alright, let's go home."
    stop music fadeout 1.0
    scene ch1sc7_10 with dissolve
    play music forestnight_2
    al "Here, I’ll help you up."
    scene ch1sc7_11 with dissolve
    "She grabs your hand firmly and pulls you to your feet."
    scene ch1sc7_12 with dissolve
    mc "Thanks. Lets get home before our parents make us do chores until next moon."
    al "It's so dark out here."
    scene ch1sc7_13 with dissolve
    mc "Come. I'll protect you, remember?"
    scene ch1sc7_14 with dissolve
    al "Y... Yes. Okay, let’s go!"
    scene ch1sc7_15 with dissolve
    mc "Don’t worry, Alice. I won’t let anything bad happen to you... not ever!"
    scene ch1sc7_16 with dissolve
    "Rustling sounds from nearby bushes."
    al "Did you hear that!?"
    scene ch1sc7_17 with dissolve
    mc "Maybe it’s a troll? Or..."
    scene ch1sc7_18 with dissolve
    al "T-Troll?!"
    scene ch1sc7_19 with dissolve
    al "Trolls aren’t real, r-right?"
    scene ch1sc7_20 with dissolve
    mc "They are... but they live up in the mountains, usually in caves."
    mc "The most dangerous thing this close to the village would be wild boars..."
    mc "...maybe a direwolf. But they are very rare."
    scene ch1sc7_21 with dissolve
    al "You promise nothing bad is out here?"
    scene ch1sc7_22 with dissolve
    mc "Yes, Alice. The hunters told me themselves last time I was with Papa at the meat market."
    scene ch1sc7_23 with dissolve
    al_t "Phew. That does make me feel a bit better. The hunters definitely know these woods better than us!"
    al_t "I know it’s late, and it's his birthday... but I'd feel safer if he walked me home."
    scene ch1sc7_24 with dissolve
    al "Mmh... [mc]? Walk me home?"

    #Choice 2a
    menu:
        "Walk Alice home.":
            scene ch1sc7_c2a1 with dissolve
            $ alice_trust += 1
            "Alice's Trust has Increased by {size=+3}{b}{color=#2bff8b}1{/color}{/b}{/size}."
            mc "Sure, Alice. Don't worry, I'll walk you home."
            scene ch1sc7_c2a2 with dissolve
            al "Yay! Thank you, thank you, thank you!"
            al "Ahh! I feel much safer with you... thank you!"
            scene ch1sc7_c2a3 with dissolve
            mct "Ha, she seems excited."
            scene ch1sc7_c2a4 with dissolve
            mc "You don’t have to thank me, we’re best friends."
            scene ch1sc7_c2a5 with dissolve
            al "Still... you’re always so kind to me."
            scene ch1sc7_c2a6 with dissolve
            al "The others... they..."
            scene ch1sc7_c2a7 with dissolve
            mc "I know, Alice. Do they still bother you?"
            scene ch1sc7_c2a8 with dissolve
            al "Not since you scared them off."
            scene ch1sc7_c2a7 with dissolve
            mc "And I’ll do it again."
            scene ch1sc7_c2a9 with dissolve
            al "*Giggles* My knight."
            mc "*Chuckles* I’ve been called worse."
            al "I bet you have!"
            scene black with Dissolve (2.0)
            "You continue chatting for a while as you walk Alice home."
            scene ch1sc7_c2a10 with dissolve
            mc "Here we are Alice, I hope you won’t get in trouble for being out late."
            scene ch1sc7_c2a11 with dissolve
            al "No biggies. Mom knows it's your birthday. But if I do get in trouble, I’ll totally blame you!"
            scene ch1sc7_c2a12 with dissolve
            mc "You might as well, Beth hates me."
            al "No she doesn't, she just thinks you're a bad influence on me."
            mc "Maybe I am, bye bye, Alice. Thanks for making my birthday amazing!"
            al "*Giggles* Anytime [mc]!"
            scene black with Dissolve (2.0)
            jump ch1sc8

            #Choice 2b
        "You're already late, hurry home.":
            "You decide it's best not to keep your worried parents waiting any longer."
            scene ch1sc7_c2b1 with dissolve
            mc "Okay, Alice. You can see your house from here, let's separate."
            mc "We don’t want our parents to worry any longer than they already have..."
            mc "We might get a big, big, big ass-whooping for being out this late!"
            scene ch1sc7_c2b2 with dissolve
            al "Aww... Okay. Bye bye, [mc]. Be safe!"
            scene ch1sc7_c2b3 with dissolve
            mc "Bye! See you tomorrow!"
            mct "Thank you, Alice. I can’t imagine my life without you in it."
            scene ch1sc7_c2b4 with dissolve
            $ renpy.pause(1.5)
            scene ch1sc7_c2b5 with dissolve
            $ renpy.pause(1.5)
            scene ch1sc7_c2b5 with dissolve
            mct "Shitsticks! I’ve gotta get home fast! Mama and Papa will not be happy."
            scene black with Dissolve (2.0)
            jump ch1sc8
