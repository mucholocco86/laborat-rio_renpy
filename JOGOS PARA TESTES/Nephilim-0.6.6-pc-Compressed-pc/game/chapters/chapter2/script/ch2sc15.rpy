#Start Chaper
label ch2sc15:

    #play music morning_1

    # start scene 2
        window hide dissolve
        #play music explore_2 fadein 2.0
        scene black with Dissolve (2.0)
        scene ch2sc15_01 with Dissolve(2.0)
        $ renpy.pause()
        play music summon_2 fadein 2.0
        window show dissolve
        scene ch2sc15_01
        el "Look at that."
        el "Doesn’t that just look... heavenly!"
        scene ch2sc15_02 with dissolve
        $ renpy.pause()
        scene ch2sc15_03 with dissolve
        mc "It’s a tavern bed..."
        scene ch2sc15_04 with dissolve
        el "Still, just thinking about the nights ahead of us, this bed will feel like heaven!"
        scene ch2sc15_05 with dissolve
        mc "You sure get excited about the weirdest things."
        scene ch2sc15_06 with dissolve
        el "Huuh? Is it so weird that I want my butt to feel comfy in a warm bed, instead of freezing my cheeks off on the cold ground?"
        scene ch2sc15_05 with dissolve
        mc "When you put it like that..."
        scene ch2sc15_07 with dissolve
        el "That’s right, even you can’t disagree on this!"
        scene ch2sc15_08 with dissolve
        el "Now hurry up! Let’s get comfy!"
        scene ch2sc15_09 with dissolve
        mc "Sure."
        scene ch2sc15_10 with dissolve
        $ renpy.pause()
        scene ch2sc15_11 with dissolve
        $ renpy.pause()
        scene ch2sc15_12 with dissolve
        $ renpy.pause()
        scene ch2sc15_13 with dissolve
        $ renpy.pause()
        scene ch2sc15_12 with dissolve
        $ renpy.pause()
        scene ch2sc15_14 with dissolve
        $ renpy.pause()
        scene ch2sc15_15 with dissolve
        el "Ahh... so much better! All set!"

        if eliza_relationship == True:
            scene ch2sc15_16 with dissolve
            el "It wasn't that long ago I'd never shared a bed with a boy before."
            el "Or hugged one, even. Let alone kissed one, now look at me."
            el "Sharing a bed with you... the first person I've done those things with."
            scene ch2sc15_17 with dissolve
            el "Longing to be embraced by you... to feel your rough hands on my delicate skin."
            scene ch2sc15_18 with dissolve
            el "Why do you have this effect on me, [mc]?"
            el "Why can't I stop thinking about you?"
            scene ch2sc15_19 with dissolve
            mc "Eliza..."
            mc "I... I feel the same."
            scene ch2sc15_20 with dissolve
            el "Y-You do?"
            scene ch2sc15_19 with dissolve
            mc "I do. Being close to you, it calms me."
            mc "And I’m not just talking about my temper..."
            scene ch2sc15_21 with dissolve
            mc "You calm every nerve in my body when you're near... but at the same time, you also excite me."
            scene ch2sc15_22 with dissolve
            mc "I’m not certain how to best describe these feelings between us, but I look forward to discovering them with you."
            scene ch2sc15_23 with dissolve
            elt "He’s so cute! No one has ever been this honest with me before."
            $ eliza_trust += 2
            "Eliza appreciates your honesty, her trust has increased by {size=+3}{b}{color=#2bff8b}2{/color}{/b}{/size}."
            scene ch2sc15_24 with dissolve
            el "[mc]?"
            scene ch2sc15_25 with dissolve
            mc "Mh?"
            stop music fadeout 2.0
            scene ch2sc15_26 with dissolve
            el "Hold me?"
            ###Choice###
            menu:
                "Hold Eliza.":
                    scene ch2sc15_27 with dissolve
                    play music feels_1 fadein 2.0
                    mc "Sure, come here."
                    scene ch2sc15_28 with dissolve
                    "As Eliza turns her back to you, you grab her small waist, pulling her closely against you in a warm embrace."
                    scene ch2sc15_29 with dissolve
                    el "Mmhm."
                    scene ch2sc15_30 with dissolve
                    el "I needed this."
                    scene ch2sc15_31 with dissolve
                    mc "Honestly, I did too."
                    scene ch2sc15_32 with dissolve
                    el "You know, you can be really sweet when you want to be."
                    scene ch2sc15_33 with dissolve
                    mc "Dont ge-"
                    scene ch2sc15_34 with dissolve
                    el "'Don’t get used to it.' Yada yada... Too late. I’m used to it, and I like it."
                    scene ch2sc15_35 with dissolve
                    mc "*Sigh* ..."
                    scene ch2sc15_36 with dissolve
                    $ renpy.pause(1)
                    el "*Giggling*"
                    scene ch2sc15_35 with dissolve
                    "Eliza snuggles closely against you, feeling safe in your arms"
                    scene ch2sc15_37 with dissolve
                    el "Hey, [mc]?"
                    scene ch2sc15_38 with dissolve
                    mc "Hmm?"
                    scene ch2sc15_39 with dissolve
                    el "Would you mind telling me about your mentor? I feel like there's more to him than you’ve told me."
                    scene ch2sc15_40 with dissolve
                    mc "Sure. I think it’s time I told you more about him."
                    scene ch2sc15_41 with dissolve
                    el "So, there is more to it?"
                    scene ch2sc15_42 with dissolve
                    mc "Yes. But I’m not sure you'll like it."
                    scene ch2sc15_43 with dissolve
                    el "I can handle it. Besides, I want to know more about you and what you had to go through."
                    scene ch2sc15_44 with dissolve
                    mc "*You exhale deeply* Alright..."
                    scene ch2sc15_45 with dissolve
                    mc "I’ll start with his name... Oren."
                    scene ch2sc15_46 with dissolve
                    with vpunch
                    "{b}!!{/b}"
                    scene ch2sc15_47 with dissolve
                    el "Huh? Strange... that was my fathers name."
                    scene ch2sc15_48 with dissolve
                    mc "Not strange."
                    scene ch2sc15_47 with dissolve
                    el "Wait... you’re saying, m-my father was your mentor?"
                    scene ch2sc15_49 with dissolve
                    el "That he was the one who took you away after your parents were ... murdered?"
                    scene ch2sc15_48 with dissolve
                    mc "Yes."
                    scene ch2sc15_50 with dissolve
                    el "It can’t be."
                    scene ch2sc15_51 with dissolve
                    el "Why would he have even been there? Why would he have gone to Riverside late at night?"
                    scene ch2sc15_52 with dissolve
                    "Eliza remains silent for a moment before she sits up, turning to face you."
                    scene ch2sc15_53 with dissolve
                    $ renpy.pause()
                    scene ch2sc15_54 with dissolve
                    $ renpy.pause()
                    scene ch2sc15_55 with dissolve
                    el "He-He left because of you?"
                    scene ch2sc15_56 with dissolve
                    mc "Yes."
                    scene ch2sc15_57 with dissolve
                    mc "I know you probably hate me now..."
                    scene ch2sc15_56 with dissolve
                    mc "'Why didn't I tell you sooner?' I'm sure you're thinking that."
                    scene ch2sc15_57 with dissolve
                    mc "'What are the chances I ran into you in the woods?' Slim to none, if I didn't know where to look."
                    scene ch2sc15_56 with dissolve
                    mc "I didn’t want your father to take me away that night, Eliza. I didn’t ask him to protect me..."
                    mc "I completely understand if you want to remain here tomorrow, when I set out."
                    scene ch2sc15_58 with dissolve
                    with vpunch
                    el "{b}Shut up!{/b}"
                    scene ch2sc15_59 with dissolve
                    el "[mc], do you still not know me at all?"
                    scene ch2sc15_60 with dissolve
                    mc "What do you-"
                    scene ch2sc15_58 with dissolve
                    el "Let me finish."
                    scene ch2sc15_59 with dissolve
                    el "I don’t blame you. You were only ten years old. Your parents just got murdered."
                    scene ch2sc15_55 with dissolve
                    el "Yes, you could have told me when we met. But would I even have believed you back then?"
                    scene ch2sc15_59 with dissolve
                    el "It wouldn't change anything, either way."
                    scene ch2sc15_61 with dissolve
                    el "I’m not even mad at my father, either."
                    scene ch2sc15_62 with dissolve
                    el "Yes, it led to me having a shit upbringing. And to my mother abandoning me to be on my own."
                    scene ch2sc15_63 with dissolve
                    el "And yes, I wish that I could have had a normal life with my family intact."
                    scene ch2sc15_64 with dissolve
                    el "But then, I wouldn’t have met you."
                    scene ch2sc15_59 with dissolve
                    el "Meeting you has been the best experience of my life."
                    scene ch2sc15_65 with dissolve
                    el "We’ve grown a lot closer lately, and I’ve caught myself feeling happy when you’re around."
                    scene ch2sc15_64 with dissolve
                    el "Because of you, I’m alive and I get to travel and see the world of Midomir..."
                    scene ch2sc15_66 with dissolve
                    el "With a person I care about, respect, and look up to."
                    scene ch2sc15_67 with dissolve
                    mc "Eliza..."
                    scene ch2sc15_68 with dissolve
                    $ renpy.pause()
                    scene ch2sc15_69 with dissolve
                    el "You didn’t take anything away from me, okay?"
                    scene ch2sc15_70 with dissolve
                    el "Quite the opposite, actually. You’ve given me so much."
                    scene ch2sc15_71 with dissolve
                    el "So, if I ever hear you feel guilty about this again, you’ll upset me, okay? You’ll hurt me."
                    scene ch2sc15_72 with dissolve
                    mc "I-I don't deserve this. You’re being too kind towards me after all the turmoil I’ve caused your family."
                    scene ch2sc15_73 with dissolve
                    el "Yes you do, [mc]. I'm the only one who can tell you what you need to hear."
                    scene ch2sc15_74 with dissolve
                    el "So I’ll say it just once."
                    scene ch2sc15_75 with dissolve
                    el "I forgive you."
                    scene ch2sc15_76 with dissolve
                    mc "Eliza, I-"
                    scene ch2sc15_77 with dissolve
                    with vpunch
                    "Before you manage to finish your sentence, Eliza has already wrapped her arms tightly around your neck."
                    "You just barely manage to support the sudden embrace without falling over the edge of the bed."
                    scene ch2sc15_78 with dissolve
                    "She’s pressing every part of herself against you. You feel your heart racing as you catch the scent of her hair."
                    "With her soft breasts squishing against your chest, you’re able to feel her heart pounding too."
                    scene ch2sc15_79 with dissolve
                    el "I forgive you, okay?"
                    el "I’m here, [mc]. I’m not leaving you."
                    scene ch2sc15_78 with dissolve
                    $ renpy.pause()

                    ####Choice####
                    menu:
                        "I’m not leaving you, either. Not now, not ever.":
                            scene ch2sc15_80 with dissolve
                            mc "I'm not going anywhere either Eliza, I will protect you with everything I've got."
                            "Eliza remains silent, but she's squeezing you even tighter than before."
                            "Eliza feels at peace hearing your words, her trust increased by {size=+3}{b}{color=#2bff8b}3{/color}{/b}{/size}."
                            $ eliza_trust += 3

                        "It’s too early to make such promises.":
                            scene ch2sc15_80 with dissolve
                            mc "It's too soon to make such promises."
                            mc "We don't know what awaits us... but I'm glad you feel this way."
                            el "Take your time. I want you to be sure before making such a promise."
                            "Eliza understands your hesitation, her trust increased by {size=+3}{b}{color=#2bff8b}1{/color}{/b}{/size}."
                            $ eliza_trust += 1

                    scene ch2sc15_81 with dissolve
                    el "I’m happy."
                    scene ch2sc15_80 with dissolve
                    mc "I’m happy too."
                    scene ch2sc15_82 with dissolve
                    el "Let’s get some rest... I do want to hear more about my father, but not now."
                    el "We need to be well rested for tomorrow."
                    scene ch2sc15_83 with dissolve
                    mc "I’ll tell you more soon, I promise."
                    scene ch2sc15_82 with dissolve
                    el "I’m counting on it!"
                    scene ch2sc15_78 with dissolve
                    mc "."
                    mc ".."
                    scene ch2sc15_84 with dissolve
                    mc "Eliza?"
                    scene ch2sc15_85 with dissolve
                    el "Mmh?"
                    scene ch2sc15_84 with dissolve
                    mc "You’ll have to let go if we’re going to sleep."
                    scene ch2sc15_86 with dissolve
                    with vpunch
                    el "{b}OH!{/b} Right. Silly me! Let’s catch some shuteye."
                    scene ch2sc15_87 with dissolve
                    mc "Silly you, indeed."
                    scene ch2sc15_88 with dissolve
                    mc "Your hand is still on my chest."
                    scene ch2sc15_89 with dissolve
                    el "Your heart is beating really fast."
                    scene ch2sc15_89 with dissolve
                    $ renpy.pause()
                    #Kiss choice
                    menu:
                        "Kiss her.":
                            scene ch2sc15_88 with dissolve
                            mc "By the gods, you're beautiful."
                            scene ch2sc15_90 with dissolve
                            $ renpy.pause()
                            scene ch2sc15_90_5 with dissolve
                            $ renpy.pause()
                            scene ch2sc15_90 with dissolve
                            $ renpy.pause(1.5)
                            scene ch2sc15_90_5 with dissolve
                            $ renpy.pause(1.5)
                            scene ch2sc15_90 with dissolve
                            $ renpy.pause(1.5)
                            el "Mmh... one more."
                            scene ch2sc15_90_5 with dissolve
                            $ renpy.pause(1.5)
                            scene ch2sc15_90 with dissolve
                            $ renpy.pause(1.5)
                        "You seem to have that effect on me.":
                            scene ch2sc15_91 with dissolve
                            mc "You're the reason it's beating this fast."

                    scene ch2sc15_92 with dissolve
                    el "Okaaay! Sleepy time!"
                    scene ch2sc15_91 with dissolve
                    mc "Sleep is good."
                    scene ch2sc15_90_5 with dissolve
                    $ renpy.pause(2.5)
                    scene ch2sc15_90 with dissolve
                    $ renpy.pause(2.5)
                    scene ch2sc15_92 with dissolve
                    el "Seriously! Sleep! Yes, sleep."
                    scene ch2sc15_88 with dissolve
                    mc "You little vixen."
                    scene ch2sc15_90 with dissolve
                    $ renpy.pause(1)
                    el "Uh-uh! No more tonight..."
                    mc "*Chuckles* But you're so tasty..."
                    scene ch2sc15_93 with dissolve
                    "The two of you get comfortable."
                    el "Night, night! Sweet dreams!"
                    scene ch2sc15_94 with dissolve
                    mc "*Yawns* Goodnight... kitten."
                    scene ch2sc15_95 with dissolve
                    "It doesn’t take long till sleep claims the two of you."
                    stop music fadeout 2.0
                    scene black with Dissolve(3)
                    $ renpy.pause(1)
                    jump ch2sc15fb15



                "Go to sleep.":

                    scene ch2sc15_96 with dissolve
                    play music feels_1 fadein 2.0
                    mc "Not tonight. I’m exhausted, and tomorrow will be a long day for us."
                    mc "Some other time, okay?"
                    scene ch2sc15_97 with dissolve
                    el "You’re right. I shouldn’t have asked."
                    scene ch2sc15_98 with dissolve
                    mc "Don’t say that. I’m just drained today. And we have a bunch to do tomorrow before leaving."
                    scene ch2sc15_96 with dissolve
                    mc "Don’t forget about morning practice, either."
                    scene ch2sc15_99 with dissolve
                    el "Like I would forget about kicking your ass!"
                    scene ch2sc15_100 with dissolve
                    mc "I'd love to see you try."
                    scene ch2sc15_101 with dissolve
                    el "Some day it will happen."
                    scene ch2sc15_99 with dissolve
                    el "And tomorrow is that day!"
                    scene ch2sc15_100 with dissolve
                    mc "Try not to stumble around like a drunken sailor this time."
                    scene ch2sc15_102 with dissolve
                    el "Hey! I managed to get a good handle on the footwork in the end."
                    scene ch2sc15_103 with dissolve
                    el "[mc]?"
                    scene ch2sc15_96 with dissolve
                    mc "Mhh?"
                    scene ch2sc15_103 with dissolve
                    el "Mind telling me some more about your mentor? I can’t help but feel there’s more to him than what you’ve told me so far."
                    scene ch2sc15_96 with dissolve
                    mc "Sure, I suppose you deserve to know."
                    scene ch2sc15_102 with dissolve
                    el "Sounds intriguing!"
                    scene ch2sc15_98 with dissolve
                    mc "Don’t get too excited, I doubt you'll like what I have to say."
                    scene ch2sc15_103 with dissolve
                    el "I can handle it. Besides, I want to know more about you and what you had to go through."
                    scene ch2sc15_104 with dissolve
                    mc "I’ll start with his name... Oren."
                    scene ch2sc15_105 with dissolve
                    el "Weird... my father also went by Oren."
                    scene ch2sc15_105_5 with dissolve
                    with vpunch
                    el "Wait, are you saying... ?"
                    scene ch2sc15_106 with dissolve
                    mc "Yes."
                    scene ch2sc15_105 with dissolve
                    el "He was the one who took you away after your parents were... murdered?"
                    scene ch2sc15_107 with dissolve
                    mc "Yes."
                    scene ch2sc15_105 with dissolve
                    el "It... It can’t be."
                    scene ch2sc15_108 with dissolve
                    el "Why would he even have been there? Your village isn’t close to my home."
                    scene ch2sc15_109 with dissolve
                    el "Tell me everything!"
                    scene ch2sc15_104 with dissolve
                    mc "Eliza... I will tell you more soon. But that’s enough for now. We have a big day ahead of us tomorrow."
                    scene ch2sc15_109 with dissolve
                    el "You can’t just drop a bomb like that on me and then not follow through!"
                    scene ch2sc15_108 with dissolve
                    el "I have so much to ask."
                    scene ch2sc15_106 with dissolve
                    mc "Soon, I promise."
                    scene ch2sc15_96 with dissolve
                    mc "Goodnight."
                    scene ch2sc15_110 with dissolve
                    el "Hmph... Goodnight."
                    scene ch2sc15_95 with dissolve
                    "Despite Eliza not being too happy with the amount of information you shared, she quickly falls asleep."
                    stop music fadeout 2.0
                    scene black with Dissolve(3)
                    $ renpy.pause(1)
                    jump ch2sc15fb15




        else:
            scene ch2sc15_16 with dissolve
            el "You good?"
            scene ch2sc15_19 with dissolve
            mc "I'm good."
            scene ch2sc15_17 with dissolve
            el "I'm going to have such amazing dreams about all the adventures ahead of us!"
            scene ch2sc15_19 with dissolve
            mc "I wouldn't get too excited. Have you ever seen Goblins or Trolls?"
            scene ch2sc15_20 with dissolve
            el "No. But I'll kick their ass!"
            scene black with Dissolve(2)
            scene ch2sc15_93 with dissolve
            el "Goodnight!"
            scene ch2sc15_94 with dissolve
            mc "Niiight..."
            scene ch2sc15_95 with dissolve
            "It doesn't take long before both of you doze off."
            scene black with Dissolve(3)
            stop music fadeout 2.0
            $ renpy.pause(1)
            jump ch2sc15fb15
