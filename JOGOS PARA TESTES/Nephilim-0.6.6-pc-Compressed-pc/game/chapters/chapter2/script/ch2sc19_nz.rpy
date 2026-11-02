#Start Chaper
label ch2sc19_nz:

    #play music morning_1

    # start scene 2
        window hide dissolve
        play music darknight_3 fadein 2.0
        scene black with Dissolve (2.0)

        scene nz_fight_01 with Dissolve(2.0)
        mct "There’s no mistaking it. I definitely felt an incantation being cast nearby."
        mct "Birds have stopped chirping."
        scene nz_fight_02 with dissolve
        mct "I’m being watched. I’ve felt a gaze upon me ever since I left the water."
        scene nz_fight_03 with dissolve
        with vpunch
        mct "Huh??!"
        #ANIMATION
        show kunai_ani with fade
        $ renpy.pause(3, hard=True)
        $ renpy.pause()
        scene nz_fight_05 with dissolve
        with vpunch
        $ renpy.pause(0.5)
        scene nz_fight_05_5 with dissolve
        $ renpy.pause(0.3)
        scene nz_fight_06 with dissolve
        $ renpy.pause(0.3)
        scene nz_fight_07 with dissolve
        $ renpy.pause(1)
        scene nz_fight_08 with dissolve
        mct "Three Kunai masked as one?"
        mct "Has to be a Shadow-trace incantation."
        mct "Which means-"
        stop music fadeout 1.0
        scene nz_fight_09 with dissolve
        play music battle_1 fadein 1.0
        with vpunch
        mct "Huh!!"
        scene nz_fight_10 with dissolve
        with vpunch
        $ renpy.pause(0.3)
        mc "*Groans* Hrrgh!"
        scene nz_fight_11 with dissolve
        mct "He's fast!"
        scene nz_fight_12 with dissolve
        $ renpy.pause()
        scene nz_fight_13 with dissolve
        $ renpy.pause()
        scene nz_fight_14 with dissolve
        $ renpy.pause()
        scene nz_fight_15 with dissolve
        with vpunch
        $ renpy.pause(0.5)
        "His punch has enough force to knock the wind out of you."
        scene nz_fight_16 with dissolve
        with vpunch
        $ renpy.pause(1)
        with vpunch
        "Without hesitation, he grabs the back of your neck and forces you under."
        scene nz_fight_17 with dissolve
        $ renpy.pause()
        scene nz_fight_18 with dissolve
        $ renpy.pause()
        stop music fadeout 1.0
        scene nz_fight_19 with Dissolve(1.5)
        play music feels_2 fadein 1.0
        $ renpy.pause(0.5)
        "As water fills your lungs, you feel pulses of energy surge through your veins."
        scene nz_fight_20 with dissolve
        mct "He’s stronger than I anticipated. I won’t be able to hold back against this guy."
        "Anger... pain... regret... revenge... You feel the emotions stir within you."
        "Suddenly you feel a burst of power surge through your body."
        stop music fadeout 1.0
        scene nz_fight_21 with dissolve
        play music battle_2 fadein 1.0
        with vpunch
        $ renpy.pause()
        scene nz_fight_22 with dissolve
        with vpunch
        $ renpy.pause(1)
        "Your body repels the attacker with a forceful blast of pure energy."
        scene nz_fight_23 with dissolve
        mc "Enough."
        scene nz_fight_24 with dissolve
        mc "Tell me..."
        scene nz_fight_25 with dissolve
        mc "Are you brave?"
        scene nz_fight_26 with dissolve
        mc "Or just incredibly dumb?"
        scene nz_fight_27 with dissolve
        mc "I’m guessing it’s the latter."
        scene nz_fight_27_b with dissolve
        mc "Let's see what you've got then!"
        scene nz_fight_28 with dissolve
        with vpunch
        $ renpy.pause()
        scene nz_fight_29 with dissolve
        $ renpy.pause()
        scene nz_fight_30 with dissolve
        $ renpy.pause()
        scene nz_fight_31 with dissolve
        elt "T-They're running on water?!"
        elt "His eyes are red again... [mc] must be tapping into his Nephilim powers."
        scene nz_fight_32 with dissolve
        elt "I-I just hope he doesn’t lose control again."
        elt "If he does... I'll need to be ready to approach him."
        scene nz_fight_33 with dissolve
        with vpunch
        $ renpy.pause()
        scene nz_fight_34 with dissolve
        with vpunch
        $ renpy.pause()
        scene nz_fight_35 with dissolve
        $ renpy.pause()
        scene nz_fight_36 with dissolve
        mc "Hah! Gotcha!"
        scene nz_fight_37 with dissolve
        uk "You’ve still got a lot to learn. Too bad you’ll be dead soon."
        scene nz_fight_38 with dissolve
        $ renpy.pause()
        scene nz_fight_39 with dissolve
        with vpunch
        $ renpy.pause()
        scene nz_fight_40 with dissolve
        $ renpy.pause()
        scene nz_fight_41 with dissolve
        with vpunch
        $ renpy.pause()
        scene nz_fight_42 with dissolve
        $ renpy.pause()
        scene nz_fight_43 with dissolve
        $ renpy.pause()
        scene nz_fight_44 with dissolve
        $ renpy.pause()
        scene nz_fight_45 with dissolve
        $ renpy.pause()
        scene nz_fight_46 with dissolve
        mct "Fuck! Another Shadow-trace!"
        scene nz_fight_47 with dissolve
        $ renpy.pause()
        scene nz_fight_48 with dissolve
        mc "{b}Shado-Jin.{/b}"
        scene nz_fight_49 with dissolve
        uk "Ahh, took you long enough to figure out, whelpling."
        scene nz_fight_50 with dissolve
        mc "I’ve encountered one of you before. You’re an elusive bunch."
        scene nz_fight_49 with dissolve
        uk "Most people don’t know we exist, for good reason."
        scene nz_fight_50 with dissolve
        mc "Is the bounty on me really that big?"
        mc "Shado-Jin’s usually don’t get hired unless it’s major."
        scene nz_fight_51 with dissolve
        uk "Your bounty is large enough, indeed."
        uk "But my reason for being here is more... of the personal sort."
        scene nz_fight_52 with dissolve
        uk "You see... the other Shado-Jin you said you encountered..."
        uk "Happened to be my brother."
        uk "So killing you is a matter of settling the score."
        uk "Now, killing the girl hiding up in the rocks will be a kill I'll savor."
        scene nz_fight_53 with dissolve
        with vpunch
        uk "I do enjoy how women squeal when you begin cutting them open!"
        scene nz_fight_54 with dissolve
        mct "He's aware of Eliza."
        mct "Threatening her? Bad choice, pal."
        menu:
            "Show no mercy.":
                scene nz_fight_55 with dissolve
                mc "Threatening someone I care about? That’s your last mistake."
                scene nz_fight_56 with dissolve
                $ renpy.pause()
                scene nz_fight_57 with dissolve
                $ renpy.pause()
                scene nz_fight_58 with dissolve
                with vpunch
                $ renpy.pause()

            "Taunt him.":
                scene nz_fight_55 with dissolve
                mc "Your brother was weak. Time to find out if you’re just as pathetic."
                scene nz_fight_56 with dissolve
                $ renpy.pause()
                scene nz_fight_57 with dissolve
                $ renpy.pause()
                scene nz_fight_58 with dissolve
                with vpunch
                $ renpy.pause()

        scene nz_fight_59 with dissolve
        $ renpy.pause()
        scene nz_fight_60 with dissolve
        $ renpy.pause()
        scene nz_fight_61 with dissolve
        $ renpy.pause()
        scene nz_fight_62 with dissolve
        with vpunch
        $ renpy.pause()
        scene nz_fight_63 with dissolve
        $ renpy.pause()
        scene nz_fight_64 with dissolve
        $ renpy.pause()
        scene nz_fight_65 with dissolve
        $ renpy.pause()
        scene nz_fight_66 with dissolve
        $ renpy.pause(0.5)
        scene nz_fight_67 with dissolve
        with vpunch
        $ renpy.pause(0.5)
        scene nz_fight_68 with dissolve
        with vpunch
        $ renpy.pause(1)
        scene nz_fight_69 with dissolve
        $ renpy.pause()
        menu:
            "Kill him. ({color=#f00}Dark Path{/color}) Ability unlock {color=#f00}Eye beam{/color}.":
                $ dark += 5
                "{color=#f00}Dark morality{/color} has increased by {size=+3}{b}{color=#2bff8b}5{/color}{/b}{/size}."
                scene nz_fight_70 with dissolve
                mct "Pathetic... just like his brother."
                $ dark_path = True
                "You feel a burning sensation in your eyes, yet it doesn’t hurt."
                scene nz_fight_71 with dissolve
                $ renpy.pause()
                $ eye_beam = True
                scene nz_fight_72 with dissolve
                $ renpy.pause()
                scene nz_fight_74 with dissolve
                $ renpy.pause()
                $ nz_alive = False
                scene nz_fight_75 with dissolve
                stop music fadeout 1.0
                with vpunch
                $ renpy.pause()
                scene nz_fight_75_b with dissolve
                play music darknight_1 fadein 1.0
                elt "Yes! That’s right! Don’t mess with [mc]!"
                scene nz_fight_76 with dissolve
                $ renpy.pause(1)
                scene nz_fight_77 with dissolve
                $ renpy.pause(1)
                scene nz_fight_78 with dissolve
                $ renpy.pause(1)
                scene nz_fight_79 with dissolve
                $ renpy.pause(1)
                scene nz_fight_80 with dissolve
                with vpunch
                $ renpy.pause()
                scene nz_fight_81 with dissolve
                $ renpy.pause()
                scene nz_fight_82 with dissolve
                $ renpy.pause()
                scene nz_fight_83 with dissolve
                $ renpy.pause()
                scene nz_fight_84 with dissolve
                $ renpy.pause()
                scene black with Dissolve(1.5)
                $ renpy.pause(1)
                scene abilityunlock_beam1 with Dissolve(1.5)
                $ renpy.pause()
                scene black with Dissolve(1.5)
                $ renpy.pause(1)
                scene nz_fight_84 with Dissolve(1.5)
                $ renpy.pause(1)


            "Let him live. ({color=#87e1fa}Light Path{/color}) Ability unlock {color=#87e1fa}Mana Manipulation{/color}.":
                $ light += 5
                "{color=#87e1fa}Light morality{/color} has increased by {size=+3}{b}{color=#2bff8b}5{/color}{/b}{/size}."
                scene nz_fight_70 with dissolve
                mct "Pathetic... just like his brother."
                $ light_path = True
                "You feel a burning sensation in your eyes, yet it doesn’t hurt."
                scene nz_fight_71 with dissolve
                $ renpy.pause()
                scene nz_fight_72 with dissolve
                $ renpy.pause()
                mct "No, I don't need to kill him. I'll just siphon his mana essence."
                stop music fadeout 1.0
                $ renpy.pause()
                $ mana_manipulation = True
                scene nz_fight_75_b with dissolve
                play music darknight_1 fadein 1.0
                elt "Yes! That’s right! Don’t mess with [mc]!"
                scene nz_fight_76 with dissolve
                $ renpy.pause()
                scene nz_fight_77 with dissolve
                $ renpy.pause()
                scene nz_fight_78 with dissolve
                $ renpy.pause()
                scene nz_fight_79 with dissolve
                $ renpy.pause()
                scene nz_fight_80 with dissolve
                with vpunch
                $ renpy.pause()
                scene nz_fight_81 with dissolve
                $ renpy.pause()
                scene nz_fight_82_b with dissolve
                $ renpy.pause()
                scene nz_fight_83_b with dissolve
                $ renpy.pause()
                scene nz_fight_84_b with dissolve
                $ renpy.pause()
                scene black with Dissolve(1.5)
                $ renpy.pause(1)
                scene abilityunlock_mana1 with Dissolve(1.5)
                $ renpy.pause()
                scene black with Dissolve(1.5)
                $ renpy.pause(1)
                scene nz_fight_84_b with Dissolve(1.5)
                $ renpy.pause(1)

        scene nz_fight_87 with dissolve
        stop music fadeout 1.0
        with vpunch
        "Suddenly, you feel a sharp pain inside your head, unlike anything you’ve ever felt before."
        "The excruciating pain lingers for a few moments and then your body loses its strength..."
        scene nz_fight_88 with dissolve
        el "[mc]!!"
        play music sad_1 fadein 1.0
        scene nz_fight_89 with dissolve
        "Your body feels totally weak as you collapse to the ground."
        scene nz_fight_90 with dissolve
        mc "*Heavy coughs* Hrrh... fuck- hggrhh..."
        scene nz_fight_90_b with dissolve
        el "{b}[mc]!{/b}"
        scene nz_fight_90_b2 with dissolve
        with vpunch
        el "I'm coming!"
        el "Just hold on!"
        scene nz_fight_91 with dissolve
        $ renpy.pause()
        scene nz_fight_92 with dissolve
        $ renpy.pause()
        scene nz_fight_93 with dissolve
        el "No! No! No! Don’t you dare!"
        scene black with Dissolve(3)
        stop music fadeout 1.0
        $ renpy.pause(1)
        scene nz_fight_94 with Dissolve(2)
        play music feels_2 fadein 1.0
        $ renpy.pause(0.5)
        elt "P-Please be okay! Please be okay!"
        scene nz_fight_95 with dissolve
        "Eliza grabs you and clings onto you."
        elt "Thank the heavens, he's still breathing!"
        scene nz_fight_96 with dissolve
        elt "His breathing is so weak, though. What in the five hells happened?"
        elt "I need to do something... I can't leave his fate up to chance!"
        scene nz_fight_97 with dissolve
        elt "Think, Eliza! Think!"
        scene nz_fight_98 with Dissolve(4)
        $ renpy.pause(4, hard=True)
        scene nz_fight_97 with Dissolve(2)
        $ renpy.pause()
        scene nz_fight_99 with dissolve
        with vpunch
        elt "That’s right! I saw some Purple Liferoot on the way here!"
        scene nz_fight_100 with dissolve
        "Eliza gently puts you down and then sprints toward the nearby woods."
        el "Be right back! Don’t go anywhere!"
        scene nz_fight_93 with dissolve
        $ renpy.pause()
        scene nz_fight_101 with dissolve
        el "It was around here, somewhere. I’m sure of it!"
        scene nz_fight_102 with dissolve
        with vpunch
        el "There!!"
        scene nz_fight_103 with dissolve
        $ renpy.pause()
        scene nz_fight_104 with dissolve
        elt "Yes! This is it!"
        scene nz_fight_105 with dissolve
        elt "One should be enough. They’re very potent."
        scene nz_fight_106 with dissolve
        $ renpy.pause()
        scene nz_fight_107 with dissolve
        elt "Just hold on, [mc]. It’s my turn to save you!"
        scene black with Dissolve(2)
        $ renpy.pause(2)
        scene nz_fight_108 with dissolve
        el "Please, [mc]. You need to chew on these, please!"
        scene nz_fight_109 with dissolve
        el "When the Liferoot petals are in your system, they'll heal you slowly but effectively."
        scene nz_fight_110 with dissolve
        el "Don’t worry, I’m not going anywhere. I’m staying right here with you til you wake up."
        scene nz_fight_111 with dissolve
        el "*Whispers* {size=-10}{b}Please be okay.{/b}{/size}"
        el "*Whispers* {size=-10}{b}Rest... I'll be right here when you wake up.{/b}{/size}"
        scene black with Dissolve(2)
        $ renpy.pause(1)
        scene nz_fight_112 with Dissolve(2)
        $ renpy.pause(1)
        "Several hours later..."
        scene black with Dissolve(2)
        $ renpy.pause(1)
        scene nz_fight_113 with Dissolve(2)
        $ renpy.pause(1.5)
        scene black with Dissolve(1)
        $ renpy.pause(1)
        scene nz_fight_113 with Dissolve(2)
        $ renpy.pause(1.5)
        scene nz_fight_114 with dissolve
        stop music fadeout 1.0
        $ renpy.pause(1.5)
        scene nz_fight_115 with dissolve
        play music explore_2 fadein 1.0
        el "You’re awake!"
        scene nz_fight_116 with dissolve
        mc "What happened?"
        scene nz_fight_117 with dissolve
        el "You collapsed! Almost stopped breathing."
        el "I thought-... but you're awake now!"
        scene nz_fight_118 with dissolve
        el "I-I... I’m sorry! I-I couldn’t do more..."
        el "I was just hiding like you told me... I'm sorry!"
        mct "I can tell she's been worried... I feel completely fine now, stronger than before."
        mct "I better get up and distract her."
        scene nz_fight_119 with dissolve
        mc "None of that self pity, you hear me? Now c’mon."
        scene nz_fight_120 with dissolve
        el "What are-"
        scene nz_fight_121 with dissolve
        mc "Take my hand and let’s go."
        mc "All that swimming made me famished."
        scene nz_fight_122 with dissolve
        el "O-Okay."
        scene nz_fight_123 with dissolve
        elt "His hands are so strong and warm."
        elt "He makes me feel so reassured with just a single touch..."
        scene nz_fight_124 with dissolve
        el "You know..."
        el "You didn’t have to put back on your shirt for my sake."
        scene nz_fight_125 with dissolve
        mc "Yeah, sure."
        mc "*Chuckles* Let me just freeze to death after nearly dying."
        scene nz_fight_126 with dissolve
        el "I’d keep you warm."
        scene nz_fight_127 with dissolve
        mc "Careful, I might take you up on that."
        scene nz_fight_128 with dissolve
        elt "Please do."
        elt "I have several ideas to keep us warm. *Giggling*"
        scene black with Dissolve(2.5)
        #play music summon_3 fadein 1.0
        stop music fadeout 1.0
        $ renpy.pause(1)
        scene ss18 with Dissolve(1.5)
        $ renpy.pause()
        scene black with Dissolve(2.5)
        scene ch2sc10_235 with Dissolve(2.5)
        play music forest_1 fadein 1.0
        #stop music fadeout 1.0
        $ renpy.pause(1)
        my "*Giggling* Beth!"
        my "That's outrageous... even for me!"
        scene ch2sc10_236 with Dissolve(1.5)
        $ renpy.pause(0.5)
        bet "*Snickers* You've really never tried it? You must!"
        bet "I'm telling you, you'll be elevated to a whole new level of pleasure."
        my "*Whispers excitedly* {size=-10}{b}How does it feel? Being filled in both... holes.{/b}{/size}"
        scene ch2sc10_237 with Dissolve(1.5)
        $ renpy.pause(0.5)
        my "C'mon Beth! You can't tease me like that and not give me the answer!"
        bet "*Snickers* All I'm going to say is... next time you buy your... eggplants, buy two."
        bet "One for each... you know!"
        bet "Oh and you're going to want to be alone... you won't be able to contain your moans when you get started."
        scene ch2sc10_238 with Dissolve(1.5)
        $ renpy.pause(0.5)
        my "That shouldn't be an issue, Shane spends most nights at the tavern."
        my "*Snickers* Which means I can be as loud as the pleasure demands."
        bet "*Giggles* That's where I'm lucky to not have a man... nobody to disturb my... needs."
        my "Oh I'd love to have my eggplants replaced with a man... a proper man."
        scene ch2sc10_239 with Dissolve(1.5)
        $ renpy.pause(0.5)
        bet "*Giggling* If you ever find such a man... {b}let's share him!{/b}"
        my "*Gasps* {b}Beth!{/b} You're so bad!"
        bet "I'm sure we can agree a man like that is exceptionally rare, and we're besties! *Giggles*"
        bet "We're both in need of a proper man, desperately so, so if either of us finds one... we'll share?"
        scene ch2sc10_238 with Dissolve(1.5)
        $ renpy.pause(0.5)
        my "*Snickers* Gosh... alright, we'll share!"
        bet "Could you imagine? *Giggling* The two of us giving in to our desires with one man?"
        my "Stop it... before I start leaking! The thought alone is... tantalizing."
        scene ch2sc10_239 with Dissolve(1.5)
        $ renpy.pause(0.5)
        bet "Come, let's go buy those eggplants! I don't see any proper men nearby."
        my "*Snickers* Yeah, I'm not interested in any of the men in Riverside..."
        scene ch2sc10_240 with Dissolve(1.5)
        $ renpy.pause(0.5)
        myt "[mc]... maybe when he returns? But... would I really be okay with sharing him?"
        myt "He's my precious boy... hmh, something to think about... I could..."
        myt "Offer him the choice? Yes, I'll present him the idea some day, and then he can choose."
        myt "If he is satisfied with me alone, that'd be perfect! But... if Beth and I together would make him even happier..."
        myt "I would be okay with that outcome as well, at least I'd still get to be with him."
        myt "Beth moved here with Alice alone, she's never had a man in Riverside, and my situation isn't much better..."
        myt "[mc] would be exactly what we're both craving in our lives, he's a real man."
        myt "*Giggling* Whatever he chooses... he's going to be spoiled rotten!"
        scene black with Dissolve(2.5)
        #play music summon_3 fadein 1.0
        stop music fadeout 1.0
        $ renpy.pause(1)
        scene ss92 with Dissolve(2)
        $ renpy.pause()
        scene nz_fight_129 with Dissolve(2.5)
        play music relax_2 fadein 1.0
        #stop music fadeout 1.0
        $ renpy.pause()
        scene nz_fight_130 with dissolve
        $ renpy.pause()
        scene nz_fight_131 with dissolve
        $ renpy.pause()
        scene nz_fight_132 with dissolve
        el "That was fun! The swimming part, I mean!"
        el "Not the 'assassin-man attacking us for no reason' part, or the 'you almost dying' part."
        scene nz_fight_133 with dissolve
        el "It’s been at least two moons since I last swam in a lake."
        scene nz_fight_134 with dissolve
        el "There’s just something soothing about swimming in nature."
        el "*Giggling* Wouldn't you agree?"
        scene nz_fight_135 with dissolve
        mc "Yeah... I do feel refreshed."
        mc "Not sure if it’s the swimming or the Liferoot you gave me, though."
        scene nz_fight_136 with dissolve
        el "Aaand you had fun."
        scene nz_fight_137 with dissolve
        mc "..."
        scene nz_fight_138 with dissolve
        $ renpy.pause()
        scene nz_fight_139 with dissolve
        with vpunch
        el "Admit it!"
        scene nz_fight_140 with dissolve
        mc "And... I had fun, yes."
        scene nz_fight_141 with dissolve
        el "I knew it!"
        el "I have to say, you’re a pretty good swimmer."
        scene nz_fight_142 with dissolve
        mc "I used to swim a lot when I was younger."
        scene nz_fight_141 with dissolve
        el "Not anymore?"
        el "How come?"
        scene nz_fight_142 with dissolve
        mc "Well, after your father took me under his wing, there wasn’t really time or need for swimming."
        scene nz_fight_143 with dissolve
        $ renpy.pause(0.2)
        with vpunch
        el "If father was here, I’d tell him off!"
        el "There should always be time for swimming, or other fun activities!"
        scene nz_fight_143_b with dissolve
        mct "She’s cute when she gets all worked up over these things."
        mct "She really doesn’t like the idea of me having a hard time."
        scene nz_fight_144 with dissolve
        mc "I would have loved to see you try."
        mc "He was absurdly strict about the activities I had to do."
        scene nz_fight_142 with dissolve
        mc "He wanted me focused, disciplined, and prepared."
        scene nz_fight_141 with dissolve
        el "So that’s why you’re so rough around the edges."
        scene nz_fight_145 with dissolve
        mc "Hm?"
        scene nz_fight_146 with dissolve
        el "You know, socially."
        el "I mean, it makes sense. You were with my father for ten years."
        el "Half your life focused solely on training and revenge."
        scene nz_fight_147 with dissolve
        el "I don’t imagine that leaves a lot of time for having friends, or just being a kid."
        scene nz_fight_142 with dissolve
        mc "Yeah. It probably wasn’t ideal, but I’m trying to be more open."
        scene nz_fight_141 with dissolve
        el "I’ve noticed. I’m proud of you, [mc]."
        scene nz_fight_145 with dissolve
        mc "..."
        scene nz_fight_146 with dissolve
        el "No, I mean it. I've seen you trying."
        el "Especially when we were at Riverside, but also when it's just us."
        scene nz_fight_148 with dissolve
        $ renpy.pause()
        scene nz_fight_148_b with dissolve
        el "You’ve become more relaxed around me, able to let your guard down and enjoy the things we do."
        scene nz_fight_149 with dissolve
        mc "Perhaps you’re right."
        mc "I didn’t even realize..."
        scene nz_fight_150 with dissolve
        el "I like it! There's plenty of doom, gloom, and rainy days in the world."
        scene nz_fight_151 with dissolve
        el "We should enjoy the moments we get along the way, where we can just be free and live!"
        scene nz_fight_152 with dissolve
        mc "How much water did you swallow?"
        scene nz_fight_153 with dissolve
        with vpunch
        el "Hush, you! *Giggle*"
        el "You don't want to end up as a victim of my tickle-attack, do you?"
        scene nz_fight_154 with dissolve
        mc "*Chuckles* Show me some mercy..."
        mc "You seem to be happy... it’s a good look on you."
        scene nz_fight_155 with dissolve
        $ renpy.pause()
        scene nz_fight_156 with dissolve
        elt "Because of you!"
        elt "How could I not be happy when we're... together."
        scene black with Dissolve(2)
        $ renpy.pause(0.5)
        "You manage to forage a few edibles on your way back to camp."
        #play music explore_1 fadein 1.0
        stop music fadeout 1.0
        scene ss18 with Dissolve(2)
        $ renpy.pause()
        scene ch2sc10_241 with Dissolve(2)
        play music relax_2 fadein 1.0
        #stop music fadeout 1.0
        $ renpy.pause(1)
        bet "Judging by the amount of eggplants you bought... you're aiming to have quite the experience!"
        my "*Giggling* Oh stop it! I'm not going to use them all today! I just wanted to have some extras..."
        bet "In case your desire overwhelm you before the next market day?"
        my "*Nods* Mhh-hm! Running out of such... lovely vegetables, is not an option!"
        scene ch2sc10_242 with Dissolve(2)
        $ renpy.pause(1)
        bet "*Giggling* And here I was thinking I was down bad! You're just as lustful!"
        my "Oh please! You're much worse Beth, you're going to drain some poor man completely dry one day."
        bet "*Snickers* No doubt... but I'd need to find a worthy man first, I have no interest in any common oaf."
        scene ch2sc10_243 with Dissolve(2)
        $ renpy.pause(1)
        my "What about the village elder? I've seen him eyeing you for years."
        bet "Eeuw! He's like sixty! No."
        bet "The man who'll earn the right to my fruit will be... younger, mmhh... much younger."
        my "*Giggles* See what I'm saying? You're down bad! How young are we talking?"
        scene ch2sc10_244 with Dissolve(2)
        $ renpy.pause(1)
        bet "Around half my age should suffice, not younger than twenty, but not older than twenty-three."
        bet "I want him young, hung and ready to satisfy my every desire!"
        my "*Scoffs* He's going to be a busy man if he has any hope of keeping up with your... needs."
        bet "Oh he's going to be busy alright! He'll be tasting my fruit first thing in the morning, every morning!"
        scene ch2sc10_245 with Dissolve(2)
        $ renpy.pause(1)
        my "Beth! You'll suffocate the poor man!"
        bet "If he wants to breathe, he'll earn it by eating me out until I come all over his young face."
        my "*Giggling* I don't know where you get these lewd ideas from..."
        bet "My romance novels, they're quite... spicy."
        my "Sounds like I'll need to borrow a few of them... you know, for research."
        bet "Oh absolutely! Next time you're over for a visit, I'll have a few for you."
        scene black with Dissolve(2)
        $ renpy.pause(1)
        scene ch2sc10_246 with Dissolve(2)
        $ renpy.pause(1)
        my "How's Alice doing? With everything... you know?"
        bet "I can only assume your lack of directness is because you're referring to your nephew."
        my "That obvious huh? I assume she knows of his return?"
        scene ch2sc10_247 with Dissolve(1.5)
        $ renpy.pause(0.5)
        my "Hey... hey, I know it's been tough on you guys... talk to me?"
        scene ch2sc10_248 with Dissolve(1.5)
        $ renpy.pause(0.5)
        bet "I know he's your nephew... but-... I hate him, I really hate him Maya!"
        my "Hey... come on now, no you don't..."
        bet "I do! You remember how deeply it affected Alice when he disappeared that night!"
        bet "How I've continuously had to comfort her for a decade now as she wakes up sobbing and screaming in her sleep!"
        scene ch2sc10_249 with Dissolve(1.5)
        $ renpy.pause(0.5)
        my "I'm well aware, you know full well I've been through the same with Sabrina and Flynn."
        bet "Mhm, I know... we've all suffered because of that boy!"
        my "That's where you're wrong, he didn't do anything. None of this is his fault."
        scene ch2sc10_248 with Dissolve(1.5)
        $ renpy.pause(0.5)
        bet "He's made my little girl go through hell! And now he just shows up out of nowhere?!"
        bet "And guess what? Here's the kicker, he spends a day or two warming Alice up again and then what does he do?!"
        with vpunch
        bet "He fucking leaves her! {b}AGAIN!{/b}"
        scene ch2sc10_249 with Dissolve(1.5)
        $ renpy.pause(0.5)
        my "He has no bad intent, he had to leave... he needs closure for what happened to his parents."
        my "He can never be what Alice wants him to be until that matter has been resolved, I felt it when I saw him."
        my "Neither you nor I can imagine what that night did to him, losing his parents like that."
        my "So stop judging him... yes, I agree that it sucks he had to leave, I wanted him to stay as well."
        scene ch2sc10_248 with Dissolve(1.5)
        $ renpy.pause(0.5)
        bet "Why even bother coming to Riverside?! If he just wanted to leave again, why not just skip past it?"
        bet "Now I'm back to square one, Maya! Just as Alice's nightmares were beginning to subside!"
        scene ch2sc10_249 with Dissolve(1.5)
        $ renpy.pause(0.5)
        my "She'll be fine, she's a big girl now Beth... if anything, seeing him alive, will give her peace of mind."
        bet "You... you think so?"
        scene ch2sc10_250 with Dissolve(1.5)
        $ renpy.pause(0.5)
        my "Look at me."
        bet "Hmm?"
        my "I know so."
        my "[mc] stopping by to see Riverside, will have the opposite effect on Alice than what you believe."
        my "I'm speaking from experience, as someone who has felt the horror of losing him... seeing him has calmed my nerves."
        bet "I-... I really want you to be right on this one Maya... I just can't believe he would leave her again."
        scene ch2sc10_251 with Dissolve(1.5)
        $ renpy.pause(0.5)
        my "Come sweetie... let's have a drink at your place, then we can talk more about it."
        bet "Okay... yeah, I'd like that."
        bet "Alice should be at home..."
        my "Lovely, maybe we should include her in the matter? She's a grown woman now."
        bet "I don't know Maya... she's my little girl."
        scene ch2sc10_252 with Dissolve(1.5)
        $ renpy.pause(0.5)
        my "She'll always be, but including her, you'll get the answers straight from the source."
        my "Only Alice can really tell you how this affects her."
        bet "Okay... you're right, I shouldn't keep shielding her... clearly it ain't possible..."
        my "*Giggling* It was a first, but I had to give up on that years ago..."
        my "Our kids have reached the age of being able to fend for themselves, so we have to let them."
        bet "Even if it's scary?"
        my "Even if it's scary, yes."
        scene black with Dissolve(2)
        #play music explore_1 fadein 1.0
        stop music fadeout 1.0
        $ renpy.pause(1)
        scene ss93 with Dissolve(2)
        $ renpy.pause()
        scene ch2sc10_180 with Dissolve(2)
        play music forest_1 fadein 1.0
        #stop music fadeout 1.0
        $ renpy.pause(0.5)
        ast "*Giggling* I wonder if he'll be at the tavern tonight?"
        ast "He has to be! Where else would an outsider be staying?"
        gib "Who are you talking about sweetie?"
        ast "Nobody! *Giggles*"
        scene ch2sc10_253 with Dissolve(1.5)
        $ renpy.pause(0.5)
        gib "C'mon, I'm not going to stop you from going if that's what you're thinking..."
        gib "You're a grown woman and you've been to the tavern plenty of times without issue."
        scene ch2sc10_180 with Dissolve(1.5)
        $ renpy.pause(0.5)
        ast "*Giggling* Alright, alright! I know better than to think you'll let this go..."
        ast "That guy who was visiting you recently... I-... I fancy him!"
        scene ch2sc10_253 with Dissolve(1.5)
        $ renpy.pause(0.5)
        gb "Who? [mc]?"
        gb "*Chuckles* Heh! Now that I didn't see coming..."
        gb "My long lost daughter fancies the son I never had... that'll be one for the books!"
        scene ch2sc10_180 with dissolve
        $ renpy.pause(0.5)
        ast "*Giggling* The son you've never had? Then you must know him well!"
        ast "That's all I need to know, I want to find out the rest on my own! That's why I'm going to the tavern!"
        gb "Is this the first boy you've liked?"
        scene ch2sc10_254 with dissolve
        $ renpy.pause(0.5)
        ast "Uh-huh! It's exciting!"
        ast "I'm a little nervous but... I've talked to Maya about it, and she's given me courage!"
        ast "I'm going to grab the situation by the balls and handle it like a woman!"
        scene ch2sc10_180 with dissolve
        $ renpy.pause(0.5)
        gb "Hey... language young lady!"
        ast "*Giggles* Sorry daddy!"
        gb "*Sighs* Listen Asta, I'm really glad to see you like this, but there's something I must tell you."
        scene ch2sc10_254 with dissolve
        $ renpy.pause(0.5)
        ast "Hmm? What is it? Is this dress not suitable to meet [mc]?"
        scene ch2sc10_255 with dissolve
        $ renpy.pause(0.5)
        gb "How do I best put this... you won't be meeting [mc] tonight sweetie."
        ast "Huh??"
        scene ch2sc10_256 with dissolve
        $ renpy.pause(0.5)
        ast "But daddy! You just said I could go-"
        scene ch2sc10_255 with Dissolve(1.5)
        $ renpy.pause(0.5)
        gib "You still can, you can still go and have fun with your friends."
        gib "Just, [mc] won't be there."
        scene ch2sc10_256 with dissolve
        $ renpy.pause(0.5)
        ast "I don't understand..."
        ast "Why won't he be? Travelers always stay at the tavern."
        scene ch2sc10_255 with dissolve
        $ renpy.pause(0.5)
        gb "He's already left town sweetie, he won't be back for quite some time I think."
        ast "..."
        astt "No way... just as I found the courage to put myself out there..."
        scene ch2sc10_256 with dissolve
        $ renpy.pause(0.5)
        ast "Daddy, will he be back some day?"
        scene ch2sc10_253 with dissolve
        $ renpy.pause(0.5)
        gib "I'm sure of it honey, he will return to Riverside one day."
        gib "But you needn't wait for that, go, have some fun. Who knows, maybe there's another great guy?"
        scene ch2sc10_254 with dissolve
        $ renpy.pause(0.5)
        ast "Hmm, no. I'll wait for his return."
        ast "I haven't spoken to [mc], but I feel it daddy... he's the one I want."
        scene ch2sc10_253 with dissolve
        $ renpy.pause(0.5)
        gb "*Chuckles* Hah... I would love to tell you that you're being silly..."
        gb "But this is exactly how I fell in love with your mother..."
        gb "I saw her just once, browsing the market stalls in Luxenford."
        gb "After that I spent a full week looking around the market, hoping for a chance to run into her."
        scene ch2sc10_180 with dissolve
        $ renpy.pause(0.5)
        ast "*Giggles* And it totally worked! Otherwise I wouldn't be here!"
        gb "Yeah... that's why I'm in no position to tell you about what you're feeling."
        gb "When you know, you just... know."
        scene ch2sc10_254 with dissolve
        $ renpy.pause(0.5)
        ast "Mhm! I fully believe that as well!"
        ast "I'll still go to the tavern, I already told Alice and Sabrina I'd meet them there."
        ast "But any guy attempts to approach me... they're getting the cold shoulder! Mh-hm!"
        scene ch2sc10_180 with Dissolve(1.5)
        $ renpy.pause(0.5)
        ast "I already have a man... even if he isn't aware! *Snickers*"
        gb "*Chuckles* He's definitely lucky to have your affections sweetie, now go on... get out of here."

        scene black with Dissolve(2)
        #play music explore_1 fadein 1.0
        stop music fadeout 1.0
        $ renpy.pause(1)
        scene ss92 with Dissolve(2)
        $ renpy.pause()
        scene nz_fight_157 with Dissolve(2)
        play music explore_1 fadein 1.0
        #stop music fadeout 1.0
        $ renpy.pause(0.5)
        el "I can't believe you're actually cooking..."
        el "What are you making for us?"
        scene nz_fight_158 with dissolve
        mc "You’ll have to wait and see."
        scene nz_fight_159 with dissolve
        el "Nuh uh! Taste test!"
        scene nz_fight_160 with dissolve
        $ renpy.pause()
        scene nz_fight_161 with dissolve
        $ renpy.pause(1)
        mc "*Chuckles* What are you doing?"
        el "Aaaaaah!"
        el "AaaaaaaaaHhHhh......"
        menu:
            "Let her taste":
                scene nz_fight_162 with dissolve
                $ eliza_trust += 2
                $ renpy.pause(1)
                el "Mfffh!"
                mc "Fine... here you go."
                scene nz_fight_163 with dissolve
                el "Mhmmmh, Nom, nom, nom."
                scene nz_fight_164 with dissolve
                el "Yummy!"
                scene nz_fight_165 with dissolve
                mc "It’s just a roasted bun..."
                mc "Let's not pretend I’m a chef."
                scene nz_fight_166 with dissolve
                el "No, it’s really good, [mc]! Savory and decently salted as well."
                el "Have you tried it yet?"
                scene nz_fight_167 with dissolve
                mc "No, not yet."
                scene nz_fight_164 with dissolve
                el "Here, let me. Open up!"
                el "You'll love it!"
                scene nz_fight_167 with dissolve
                mc "Are you serious?"
                scene nz_fight_168 with dissolve
                $ renpy.pause(0.5)
                with vpunch
                el "*Growls* Hrrrh!"
                scene nz_fight_169 with dissolve
                mc "Fine!"
                scene nz_fight_170 with dissolve
                $ renpy.pause()
                scene nz_fight_171 with dissolve
                mc "..."
                scene nz_fight_172 with dissolve
                $ renpy.pause()
                scene nz_fight_173 with dissolve
                $ renpy.pause()
                scene nz_fight_174 with dissolve
                mc "Oh, that is really good!"
                scene nz_fight_175 with dissolve
                el "See! I told you so!"
                scene nz_fight_176 with dissolve
                mc "I guess your stubbornness is useful at times."
                scene nz_fight_175 with dissolve
                el "It sure is! Now back to work, Chef [mc]!"
                el "Our dinner won't cook itself!"
                scene nz_fight_177 with dissolve
                mc "You’re ridiculous."
                scene nz_fight_175 with dissolve
                el "Ridiculously cute, you mean!"
                scene nz_fight_176 with dissolve
                mc "Sometimes."
                scene nz_fight_178 with dissolve
                el "All the time! *Giggle*"
                "Eliza enjoys fooling around with you. Her trust has increased by {size=+3}{b}{color=#2bff8b}2{/color}{/b}{/size}."
                scene black with Dissolve(1.5)

            "Tell her to wait":
                scene nz_fight_167 with dissolve
                mc "No, you sit and wait."
                mc "You’re lucky I’m even making dinner. I did beat you to the lake ..."
                scene nz_fight_164 with dissolve
                el "I’m very pleased you’re making dinner for us!"
                scene nz_fight_169 with dissolve
                mc "Good. I don’t cook often, so lower your expectations."
                scene nz_fight_166 with dissolve
                el "I’m sure it’ll be fine! Besides, I’m starving."
                el "So even if you end up burning it, I’d probably still eat it all up!"
                scene nz_fight_165 with dissolve
                mc "I don’t think I’m that terrible."
                scene nz_fight_164 with dissolve
                el "I’ll be the judge of that, mister."
                scene black with Dissolve(1.5)
        $ renpy.pause(1)
        scene nz_fight_179 with Dissolve(1.5)
        $ renpy.pause(0.5)
        "A short while later"
        scene nz_fight_180 with dissolve
        $ renpy.pause()
        scene nz_fight_181 with dissolve
        $ renpy.pause()
        scene nz_fight_182 with dissolve
        "Once dinner is fully cooked, you trace your fingers across Eliza's shoulder as she rests."
        mc "Hey, sleepyhead... dinner's ready."
        el "Nnnh... no more nap?"
        mc "*Chuckles* No more nap."
        scene black with Dissolve(1.5)
        $ renpy.pause(1)
        scene nz_fight_183 with Dissolve(1.5)
        $ renpy.pause(1)
        el "Yum yum yum! This is really good!"
        scene nz_fight_184 with dissolve
        mct "Heh, it’s kinda infectious to see her enjoying the small things."
        scene nz_fight_185 with dissolve
        mc "Everything to your liking?"
        scene nz_fight_186 with dissolve
        el "This was just what I needed! You have to cook more often!"
        scene nz_fight_187 with dissolve
        mc "Yeah, that’s a full barrel of 'no'."
        scene nz_fight_188 with dissolve
        el "Oh, come on! It’s so yummy... please?"
        el "{size=+3}{b}Biiiiig{/b}{/size} please with a cherry on top? Oh! And added cream as well!"
        scene nz_fight_187 with dissolve
        mc "*Sighs* ..."
        mc "We’ll take turns."
        scene nz_fight_189 with dissolve
        el "Deal! No take backs allowed!"
        el "*Excitedly* I'm going to be living like a Queen! Thank you!"
        scene nz_fight_190 with dissolve
        mct "*Sigh* She’s so happy."
        mct "With everything she's had to endure because of me... the least I can do is try to make her happy."
        scene nz_fight_191 with dissolve
        el "*Yawns* Hnnnhhh!"
        scene nz_fight_191_b with dissolve
        el "Are you ready for bed? I’m starting to feel a bit sleepy."
        scene nz_fight_192 with dissolve
        mc "I was just thinking about that, actually."
        scene nz_fight_193 with dissolve
        el "I’m not looking forward to the ground..."
        el "But at least it’s one of the nicer campsites we’ve had."
        scene nz_fight_192 with dissolve
        mc "Let me know if you get cold, I’ll get up and stoke the fire."
        scene nz_fight_194 with dissolve
        el "That’s sweet of you. I have a better idea, though."
        scene nz_fight_192 with dissolve
        mc "I’m all ears."
        scene nz_fight_195 with dissolve
        el "You... you could just keep me warm. You know, like last night?"
        scene nz_fight_196 with dissolve
        mc "You want me to hold you?"
        scene nz_fight_197 with dissolve
        el "Yes! I- no..."
        scene nz_fight_198 with dissolve
        $ renpy.pause()
        scene nz_fight_199 with dissolve
        el "I mean- I do, if you do?"
        menu:
            "Keep her warm. ({color=#ff8cdd}Romance{/color})":
                scene nz_fight_200 with dissolve
                with vpunch
                mc "Come here!"
                mc "It's about time we get you tucked in."
                scene nz_fight_201 with dissolve
                el "H-Hey! You big brute!"
                $ eliza_relationship = True
                scene nz_fight_202 with dissolve
                el "That eager, huh?"
                scene nz_fight_203 with dissolve
                mc "Something like that."
                scene black with Dissolve(1.5)
                $ renpy.pause(1)
                scene nz_fight_204 with Dissolve(1.5)
                $ renpy.pause()
                $ eliza_path = True
                scene nz_fight_205 with dissolve
                el "Really? You don’t mind?"
                scene nz_fight_206 with dissolve
                mc "Eliza, I’ve been thinking about having you in my arms again since this morning."
                mc "I obviously don't mind."
                scene nz_fight_207 with dissolve
                el "Uh! Okay! Then you should probably cuddle me all night!"
                el "And you should keep me close!"
                scene nz_fight_208 with dissolve
                el "Else you risk me getting cold."
                scene nz_fight_209 with dissolve
                mc "I’m not taking my hands off you until we wake up."
                scene nz_fight_208 with dissolve
                el "Promise?"
                scene nz_fight_209 with dissolve
                mc "Promise."
                scene nz_fight_210 with dissolve
                el "*Giggling happily* Good! I’ll hold you to that."
                scene nz_fight_211 with dissolve
                elt "I feel so protected in his arms."
                elt "Like nothing in the world can get me. It’s just me and [mc]."
                elt "I-I just want to be near him and protect him."
                elt "I want to make him happy, the way he makes me happy."
                scene nz_fight_212 with dissolve
                elt "I won’t let anyone hurt him."
                elt "When we reach the capital, there will be no shortage of people wanting to take advantage of him."
                elt "I’ll have to stay alert."
                scene nz_fight_213 with dissolve
                el "So..."
                scene nz_fight_214 with dissolve
                mc "Hmm?"
                scene nz_fight_205 with dissolve
                el "What’s the verdict?"
                scene nz_fight_206 with dissolve
                mc "On what?"
                scene nz_fight_205 with dissolve
                el "You know... I said earlier you'd find out if I really smell like flowers or not. Why don’t you find out?"
                scene nz_fight_215 with dissolve
                mc "*Inhales deeply* . .. ..."
                scene nz_fight_216 with dissolve
                el "*Giggles* H-Hey, that tickles!"
                scene nz_fight_215 with dissolve
                mc "*Inhales deeply* Mmmh..."
                scene nz_fight_216 with dissolve
                el "*Giggling* Oh that feels-... mmh-hm..."
                scene nz_fight_207 with dissolve
                el "So... what do you think?"
                scene nz_fight_206 with dissolve
                mc "You smell like morning."
                scene nz_fight_205 with dissolve
                el "Huh? Are you sure you didn’t smell the grass instead."
                scene nz_fight_206 with dissolve
                mc "Let me explain. Imagine waking up at dawn, just before sunrise."
                mc "You step into a field of early spring flowers, in your case it would be Dreamveil & Sunroot."
                scene nz_fight_209 with dissolve
                mc "The morning dew is trickling down the leaves, and a chilly breeze brings your senses alive with the smell of a new day... Morning."
                mc "That’s how you smell."
                scene nz_fight_211 with dissolve
                $ renpy.pause()
                elt "Heavens! I'm going to melt!!!"
                scene nz_fight_210 with dissolve
                el "I-I... Thank you, [mc]."
                scene nz_fight_207 with dissolve
                el "You really have a way with words, don’t you?"
                scene nz_fight_211 with dissolve
                elt "I feel all giddy after that description. Didn't expect that from him."
                scene nz_fight_205 with dissolve
                el "Did you-"
                scene nz_fight_206 with dissolve
                mc "Yes, I liked it."
                scene nz_fight_205 with dissolve
                el "I-I won’t mind if you want to... sniff me again..."
                scene nz_fight_215 with dissolve
                "You gently strafe her smooth neck with the tip of your nose while inhaling."
                mct "Divines grant me strength. Her scent is the single most intoxicating thing I’ve ever come across."
                mc "*Whispers* {size=-10}{b}Goodnight, kitten.{/b}{/size}"
                scene nz_fight_216 with dissolve
                el "*Purrs* {size=-10}{b}Goodnight, [mc]. Nnh-Nyahh...{/b}{/size}"
                stop music fadeout 2.0
                scene black with Dissolve(2)
                $ renpy.pause(1, hard=True)


            "Keep it friendly. (Friendship)":
                scene nz_fight_196 with dissolve
                mc "Tell you what: IF we wake up freezing, I’ll consider it."
                scene nz_fight_195 with dissolve
                $ eliza_relationship = False
                el "O-Okay."
                scene nz_fight_191 with dissolve
                el "Night, night!"
                $ eliza_path = False
                scene nz_fight_196 with dissolve
                mc "Goodnight."
                stop music fadeout 2.0
                scene black with Dissolve(2)
                $ renpy.pause(1, hard=True)

        play music explore_1 fadein 2.0
        scene nz_fight_217 with Dissolve(3)
        $ renpy.pause(1)
        mct "As far as sleeping on the ground goes... this wasn't half-bad."
        scene nz_fight_218 with Dissolve(2)
        $ renpy.pause(1)
        mct "Seems like I'm the last one to arise today."
        scene nz_fight_219 with dissolve
        $ renpy.pause(1)
        mct "Usually she's the one sleeping in."
        scene nz_fight_220 with dissolve
        mct "I wonder why she’s up early today?"
        scene nz_fight_221 with dissolve
        mc "*Yawn* Hnnngh!"
        scene nz_fight_220 with dissolve
        mct "I better go look for her."
        scene nz_fight_222 with dissolve
        mct "I have a feeling about where she might have gone."
        mct "Sleeping on the ground, even after we made the campsite, she'd be a little dirty again."
        scene black with Dissolve(2)
        stop music fadeout 1.0
        $ renpy.pause(1)
        scene nz_fight_223 with Dissolve(2)
        play music chill_1 fadein 2.0
        $ renpy.pause()
        scene nz_fight_224 with dissolve
        $ renpy.pause()
        scene nz_fight_225 with dissolve
        $ renpy.pause()
        scene nz_fight_226 with dissolve
        with vpunch
        el "{b}[mc]!!{/b}"
        scene nz_fight_227 with dissolve
        mc "."
        mc ".."
        scene nz_fight_227_b with dissolve
        mc "Why’d you stop?"
        scene nz_fight_228 with dissolve
        el "'Cause you’re drooling."
        el "If I didn't know better I'd say you've seen the love of your life! *Snickering*"
        scene nz_fight_227_b with dissolve
        mc "*Chuckles* You wish."
        mc "I’m just... enjoying the scenery."
        scene nz_fight_228 with dissolve
        el "I think you’ve seen plenty for now!"
        el "At least try to act like a gentleman, and turn around."
        scene nz_fight_227_b with dissolve
        mc "Sure, just hurry up."
        scene nz_fight_230 with dissolve
        el "So bossy."
        el "Didn’t you sleep well last night?"
        scene nz_fight_231 with dissolve
        el "It sure felt like you did, based on what was pressing against me this morning."
        mc "*Chuckles* Sorry."
        scene nz_fight_233 with dissolve
        el "Don’t be sorry. I took it as a compliment."
        scene nz_fight_234 with dissolve
        mc "Good. It’s not like I have any control over something like that."
        scene nz_fight_235 with dissolve
        mc "Especially... sleeping next to you."
        scene nz_fight_236 with dissolve
        elt "Awwh, He's so cute when he gets shy!"
        scene nz_fight_237 with dissolve
        el "Good to know I have that effect on you."
        el "In fact it made me want to remain in your arms longer, but I had to take the chance to wash off the dirt."
        el "Since we don't know when we'll next pass a river or lake again."
        scene nz_fight_238 with dissolve
        with vpunch
        el "{b}Hyuuuah!{/b}"
        el "Kitten-attack! *Giggling*"
        scene nz_fight_239 with dissolve
        mc "You ready? The sooner we get moving, the faster we reach the capital."
        scene nz_fight_240 with dissolve
        el "Hey, you shouldn’t rush a lady!"
        el "Heavens, did my father really not teach you any manners?"
        scene black with Dissolve(1.5)
        $ renpy.pause(1)

        scene nz_fight_149 with Dissolve(1.5)
        $ renpy.pause(0.5)
        mc "It wasn’t exactly on his list, no."
        mc "Your father taught me a lot of things, but how to socialize? That wasn't his strength."
        scene nz_fight_146 with dissolve
        el "*Sigh* Well, then..."
        el "I suppose I’ll have to teach you, better late than never!"
        scene nz_fight_144 with dissolve
        mc "Thanks, I’m good."
        mc "Now let’s go."
        scene nz_fight_147 with dissolve
        el "Don’t be so stubborn!"
        el "Don't underestimate how much manners and public perception can help you in social situations."
        scene nz_fight_150 with dissolve
        el "We’re going to the capital, Luxenford, right?"
        el "That means a lot of high profile nobles, merchants, and guilds..."
        el "Not to mention the royal family! {b}House Valois.{/b}"
        scene nz_fight_151 with dissolve
        el "Social skills will be very important when it comes to dealing with these types of people."
        scene nz_fight_149 with dissolve
        mc "Hmmh, you actually have a point. *Sighs*"
        scene nz_fight_148_b with dissolve
        el "I don’t know whether to be happy that you agree with me, or insulted that you seem so surprised."
        scene nz_fight_152 with dissolve
        mc "No, really."
        mc "You came up with a great idea, Eliza."
        scene nz_fight_148 with dissolve
        $ renpy.pause()
        scene nz_fight_148_b with dissolve
        el "Thank you, [mc]."
        el "So, I’ll start teaching you proper social etiquette on the way."
        scene nz_fight_151 with dissolve
        el "You’ll be ready for lavish parties with high ranking officials in no time! *Giggling*"
        scene nz_fight_149 with dissolve
        mc "How do you even know all this?"
        scene nz_fight_147 with dissolve
        el "I know it’s not exactly common for commoners... like me."
        el "My mother taught me, though."
        el "She said if I were to get anywhere in life, I'd need to know, in order to marry a proper man."
        scene nz_fight_144 with dissolve
        mc "Makes sense, I suppose."
        scene nz_fight_143 with dissolve
        el "Hmhf. I-I don’t want that, though."
        el "I don’t need some fancy-pants nobleman with a stick up his ass to take care of me."
        scene nz_fight_144 with dissolve
        mc "I know, Eliza."
        scene nz_fight_143_b with dissolve
        mct "*Chuckles* Does she realize she's squeezing my arm tighter with every word?"
        scene nz_fight_143 with dissolve
        el "Some-some two-faced, rich, wine sipping... {b}Urgh!{/b}"
        scene nz_fight_145 with dissolve
        $ renpy.pause()
        scene nz_fight_144 with dissolve
        mc "I know."
        scene nz_fight_146 with dissolve
        el "Y-You do?"
        scene nz_fight_142 with dissolve
        mc "Yes... None of that appeals to you."
        mc "That would be a safe life."
        mc "A tedious, boring, vanilla life, it'd fit most people."
        mc "You aren’t like most people, though... That would never be enough for you."
        scene nz_fight_146 with dissolve
        el "I-"
        scene nz_fight_148 with dissolve
        elt "He really knows me well."
        scene nz_fight_142 with dissolve
        mc "You crave adventure, you enjoy the thrill of what each day might bring."
        mc "But above all, you want what you’ve never had."
        scene nz_fight_146 with dissolve
        el "Mmmh... what I’ve never had?"
        scene nz_fight_145 with dissolve
        $ renpy.pause()
        scene nz_fight_144 with dissolve
        mc "Passion."
        scene nz_fight_148 with dissolve
        elt "He's right! I've never had passion in my life... until I met you, [mc]."
        elt "He really... sees me."
        scene nz_fight_141 with dissolve
        el "You really know me that well?"
        scene nz_fight_144 with dissolve
        mc "Mmh. I see you, Eliza."
        scene nz_fight_148 with dissolve
        $ renpy.pause()
        scene nz_fight_148_b with dissolve
        el "*Blush* I-I... I see you too, [mc]."
        el "You know... my life has been pretty exciting since we met."
        scene nz_fight_149 with dissolve
        mc "Hmm. I suppose it has."
        scene nz_fight_150 with dissolve
        el "There’s no telling what'll happen when we reach the capital."
        scene nz_fight_151 with dissolve
        el "I mean, there could even be bandits lurking around that tree over there!"
        scene nz_fight_152 with dissolve
        mc "Okay, calm down, little miss thrill seeker. Our lives aren’t that exciting."
        scene nz_fight_141 with dissolve
        el "*Giggle* I suppose not! A girl can dream though, right?"
        scene nz_fight_149 with dissolve
        mc "You want bandits to pop out and try to rob us?"
        scene nz_fight_150 with dissolve
        el "Well, not exactly... But I’m dying to test out my combat skills after our recent training sessions."
        scene nz_fight_135 with dissolve
        mc "You’ve been doing well... You improve fast."
        mc "You're quick to adapt to the things I teach you, with consistent training you'll be a force to be reckoned with."
        scene nz_fight_136 with dissolve
        el "You’re just saying that. I feel like I could be way better."
        scene nz_fight_142 with dissolve
        mc "Nobody became {b}Thrynn{/b}, The Giant, or {b}Crixus{/b}, God of the arena, overnight, you know?"
        scene nz_fight_144 with dissolve
        mc "Trust me, you’ve improved a lot in a short amount of time... More than most."
        scene nz_fight_141 with dissolve
        el "You really think so?"
        scene nz_fight_144 with dissolve
        mc "I know so. I’m proud of you."
        scene nz_fight_241 with dissolve
        $ renpy.pause()
        el "Mwaaahh!"
        scene nz_fight_242 with dissolve
        el "That means a lot coming from you!"
        el "I can’t take all the credit though. You’re a great teacher."
        scene nz_fight_243 with dissolve
        mc "Hmm, you think so?"
        mc "I’ve never taught anyone before... I’m just kind of winging it."
        scene nz_fight_242 with dissolve
        el "Yes, I definitely think so! How else would I be doing so great?"
        el "A student can only excel under great tutelage."
        scene nz_fight_244 with dissolve
        mc "I suppose we’re a great team."
        scene nz_fight_245 with dissolve
        el "The best team!"
        scene nz_fight_246 with dissolve
        el "The dream team!"
        el "Nobody can defeat us!"
        ####Choice####
        menu:
            "Kiss her. ({color=#ff8cdd}Romance{/color})":
                $ eliza_relationship = True
                $ eliza_trust +=1
                scene nz_fight_247 with dissolve
                $ renpy.pause()
                elt "Mmmhhaahh... He’s such a good kisser!"
                scene nz_fight_248 with dissolve
                el "My life definitely isn’t lacking in the passion department around you."
                scene nz_fight_249 with dissolve
                mc "It’s getting harder and harder to keep my hands off you."
                scene nz_fight_248 with dissolve
                el "Then don’t."
                $ eliza_path = True
                scene nz_fight_247 with dissolve
                $ renpy.pause()
                el "*Mhwwaahh!*"
                mct "She always tastes incredible... mmh."
                scene nz_fight_249 with dissolve
                mc "I'm becoming addicted to these lips of yours."
                el "*Giggling* ..."
                scene nz_fight_248 with dissolve
                el "Why don't you taste them again? You know... for good measure!"
                scene nz_fight_247 with dissolve
                el "Mmmh-nnhh..."
                "Just as you get a firm hold on her perky ass, you hear a sound off in the distance"
                with vpunch
                scene nz_fight_250 with Dissolve(1.5)
                with vpunch
                uk "{b}*Loudly* Arrgh!! Bloody arse!{/b}"
                elt "*Sighs heavily* Typical... he had just grabbed my ass!"
                mct "*Exhales* Fuck me... I guess we'll need to investigate."
                scene black with Dissolve(2)
                stop music fadeout 2.0
                $ renpy.pause(1)
                jump ch2sc23

            "Move on. (Neutral)":
                scene nz_fight_244 with dissolve
                mc "Let's get going. Would be nice to find an inn before night."
                scene nz_fight_242 with dissolve
                el "I couldn't agree more!"
                scene nz_fight_251 with dissolve
                with vpunch
                uk "*Loud* Arrgh!! Bloody arse!"
                scene black with Dissolve(2)
                stop music fadeout 2.0
                $ renpy.pause(1)
                jump ch2sc23
