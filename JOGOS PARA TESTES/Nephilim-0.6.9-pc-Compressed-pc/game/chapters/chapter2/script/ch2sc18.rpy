#Start Chaper
label ch2sc18:

    #play music morning_1

    # start scene 2
        window hide dissolve
        play music outdoors_1 fadein 2.0
        scene black with Dissolve (2.0)
        scene ch2sc18_01 with Dissolve(2.0)
        $ renpy.pause(0.5)
        el "[mc]! There you are!"
        scene ch2sc18_02 with dissolve
        mc "Hey, I was just searching for you."
        scene ch2sc18_03 with dissolve
        $ renpy.pause(0.5)
        scene ch2sc18_04 with dissolve
        el "Well I found you first!"
        scene ch2sc18_03 with dissolve
        $ renpy.pause(0.5)
        mc "*Chuckles* I suppose you did."
        scene ch2sc18_05 with dissolve
        el "So are we ready to leave?"
        scene ch2sc18_09 with dissolve
        $ renpy.pause(0.5)
        scene ch2sc18_22 with dissolve
        mc "Assuming you didn’t sleep in until now and managed to get our supplies, we should be good to leave."
        scene ch2sc18_06 with dissolve
        $ renpy.pause()
        scene ch2sc18_07 with dissolve
        el "Actually, I didn’t get any sleep after you left."
        scene ch2sc18_08 with dissolve
        el "So I got up, had breakfast downstairs with Clark, helped him clean up a bit, and went to the market."
        scene ch2sc18_23 with dissolve
        $ renpy.pause()
        scene ch2sc18_24 with dissolve
        mc "Oh? I thought your butt needed all the extra rest it could get."
        scene ch2sc18_11 with dissolve
        $ renpy.pause()
        scene ch2sc18_12 with dissolve
        el "It does!"
        scene ch2sc18_13 with dissolve
        el "I mean... well..."
        scene ch2sc18_14 with dissolve
        $ renpy.pause()
        scene ch2sc18_15 with dissolve
        el "*Whispers* {size=-10}{b}It wasn’t the same without you.{/b}{/size}"
        scene ch2sc18_16 with dissolve
        $ renpy.pause()
        scene ch2sc18_17 with dissolve
        mc "Hmm? Did you say something?"
        scene ch2sc18_18 with dissolve
        $ renpy.pause()
        scene ch2sc18_19 with dissolve
        el "Who me? N-Nothing! Not a peep! Time to go!"
        scene ch2sc18_20 with dissolve
        $ renpy.pause()
        scene ch2sc18_21 with dissolve
        mc "Sure. Let’s get going."
        scene ch2sc18_25 with dissolve
        mct "..."
        mct "Farewell, Riverside... I’ll see you again one day."
        scene ch2sc18_26 with dissolve
        mct "Take care everyone."
        scene ch2sc18_27 with dissolve
        mct "Gibbs... Sabrina... Flynn... Alice... Maya..."
        scene ch2sc18_28 with dissolve
        mct "..."
        scene ch2sc18_29 with dissolve
        el "You coming?"
        scene ch2sc18_30 with dissolve
        mc "Yeah, I was just... never mind."
        scene ch2sc18_31 with dissolve
        el "So, how did it go with your friend?"
        scene ch2sc18_32 with dissolve
        mc "Oh, it was... it was good to see him again."
        scene ch2sc18_33 with dissolve
        $ renpy.pause()
        scene ch2sc18_34 with dissolve
        el "Who is he?"
        scene ch2sc18_35 with dissolve
        $ renpy.pause(1)
        scene ch2sc18_36 with dissolve
        $ renpy.pause(1)
        scene ch2sc18_37 with dissolve
        $ renpy.pause(1)
        scene ch2sc18_38 with dissolve
        mc "Gibson. He was friends with Mama and Papa for decades, even before I was born."
        mc "He grew up with my dad in Luxenford, that's where they learned their crafts."
        mc "Papa as a carpenter and Gibson as a blacksmith, Gibson has always been... hmm..."
        scene ch2sc18_39 with dissolve
        mc "Kind of like an uncle, in a way? He always had good advice for me while I was growing up."
        scene ch2sc18_40 with dissolve
        $ renpy.pause()
        scene ch2sc18_41 with dissolve
        el "Awwh, that’s so sweet! It must have felt amazing seeing him after so long."
        scene ch2sc18_37 with dissolve
        stop music fadeout 2.0
        $ renpy.pause()
        menu:
            "Appreciative. ({color=#87e1fa}Light Path{/color})":
                scene ch2sc18_42 with dissolve
                $ light += 1
                play music chill_4 fadein 2.0
                mc "It was. I’m glad I took the time to see him before we left."
                scene ch2sc18_43 with dissolve
                mc "We didn’t have time to cover everything, but he told me some interesting things about my parents."

            "Indifferent. ({color=#f00}Dark Path{/color})":
                scene ch2sc18_44 with dissolve
                $ dark += 1
                play music chill_4 fadein 2.0
                mc "He had information I needed. And I managed to get some of it, that’s all."
                scene ch2sc18_45 with dissolve
                mc "There’s no point dwelling on the past, it will only slow me down."

        scene ch2sc18_46 with dissolve
        $ renpy.pause()
        scene ch2sc18_47 with dissolve
        el "Either way, I’m happy you did! I can tell it set your head straight for this journey."
        scene ch2sc18_48 with dissolve
        mc "Yeah... I suppose it did. Also, get this..."
        scene ch2sc18_49 with dissolve
        mc "He told me my mother was a sorceress."
        scene ch2sc18_50 with dissolve
        with vpunch
        el "Woah! Really?!"
        scene ch2sc18_51 with dissolve
        el "I’ve read about them in my mothers books!"
        scene ch2sc18_52 with dissolve
        el "[mc], do you realize how big this is?!"
        scene ch2sc18_53 with dissolve
        el "It’s incredibly rare to be born with magic in your blood!"
        scene ch2sc18_54 with dissolve
        el "Most who are gifted with magic live in the capital as a part of the Mages Guild."
        el "Or in other large cities with established schools for magic."
        scene ch2sc18_55 with dissolve
        $ renpy.pause()
        scene ch2sc18_56 with dissolve
        mc "Huh. I never knew about any of that."
        scene ch2sc18_57 with dissolve
        mc "I wonder what else they didn't tell me about?"
        scene ch2sc18_58 with dissolve
        el "Mhm..."
        scene ch2sc18_59 with dissolve
        el "If you want, we could try to find out more when we reach the capital?"
        scene ch2sc18_60 with dissolve
        mc "I suppose we could... wouldn’t you be bored, though?"
        scene ch2sc18_61 with dissolve
        el "Learning more about you isn’t boring!"
        scene ch2sc18_62 with dissolve
        $ renpy.pause()
        scene ch2sc18_63 with dissolve
        el "I’m actually rather excited to find out more!"
        scene ch2sc18_64 with dissolve
        $ renpy.pause()
        scene ch2sc18_65 with dissolve
        $ renpy.pause()
        scene ch2sc18_65_5 with dissolve
        mc "Thank you, Eliza."
        mc "It... feels good not to be alone in this anymore."
        scene ch2sc18_63 with dissolve
        el "You won’t be, not anymore."
        scene ch2sc18_66 with dissolve
        $ renpy.pause()
        scene ch2sc18_67 with dissolve
        $ renpy.pause()
        ####ANIMATION####
        show eliza_closeup with fade
        $ renpy.pause(6, hard=True)
        $ renpy.pause()
        scene ch2sc18_67 with dissolve
        $ renpy.pause(1)
        scene ch2sc18_68 with dissolve
        $ renpy.pause(1)
        scene ch2sc18_69 with dissolve
        $ renpy.pause(1)
        scene ch2sc18_70 with dissolve
        $ renpy.pause(1)
        scene ch2sc18_71 with dissolve
        $ renpy.pause(1)
        scene ch2sc18_72 with dissolve
        $ renpy.pause(1)
        scene ch2sc18_73 with dissolve
        el "What?"
        menu:
            "You're beautiful.":
                scene ch2sc18_74 with dissolve
                $ renpy.pause()
                scene ch2sc18_75 with dissolve
                mc "Just admiring the beauty the divines have bestowed upon you."
                scene ch2sc18_76 with dissolve
                $ renpy.pause()
                scene ch2sc18_77 with dissolve
                $ renpy.pause()
                scene ch2sc18_78 with dissolve
                $ renpy.pause()
                scene ch2sc18_79 with dissolve
                el "D-Don’t be silly."
                scene ch2sc18_75 with dissolve
                mc "*Chuckles* What? You don't like it when I'm appreciating you?"
                scene ch2sc18_79 with dissolve
                $ eliza_trust += 2
                el "I-I don’t mind when it’s you!"
                "Eliza likes that you complimented her, her trust increased by {size=+3}{b}{color=#2bff8b}2{/color}{/b}{/size}."

            "N-Nothing, let's move out.":
                scene ch2sc18_75 with dissolve
                mc "Nothing, we better get going."

        scene ch2sc18_82 with dissolve
        $ renpy.pause()
        scene ch2sc18_83 with dissolve
        el "You know, [mc]. I’m not just here with you for your revenge, but for everything."
        scene ch2sc18_80 with dissolve
        "You both acknowledge that you’re in this together, for better or worse, with a simple but reassuring smile."
        scene ch2sc18_81 with dissolve
        $ renpy.pause(1)
        "The bond the two of you have formed, it's something... unique."
        scene black with Dissolve(2.5)
        stop music fadeout 2.0
        $ renpy.pause(1)
        "You walk for several hours, leaving Riverside and familiar faces behind."
        scene ch2sc18_84 with Dissolve(2.5)
        play music chill_3 fadein 1.0
        $ renpy.pause(0.5)
        mc "Do you think my mother being a sorceress is related to my abilities?"
        scene ch2sc18_85 with dissolve
        el "There’s definitely a chance of that, magic is usually passed down from parents to their children."
        scene ch2sc18_86 with dissolve
        el "I’ve never seen or encountered magic before."
        el "But from what I’ve read about it in my mothers books, your abilities seem... different."
        scene ch2sc18_87 with dissolve
        mc "How so?"
        scene ch2sc18_88 with dissolve
        el "Well, supposedly with magic you usually have to take time to gather energy or even say incantations, depending on your skill."
        el "And mages typically have one natural born elemental affinity, like fire, or water for example."
        scene ch2sc18_87 with dissolve
        mc "I’ve never had to do any of that... also I have an affinity for wind, but..."
        mc "Gibson claimed my mother was an arcane sorceress."
        scene ch2sc18_89 with dissolve
        el "That’s what I’m saying, [mc]."
        el "From what you've told me, your magic doesn't seem tied to one specific element."
        scene ch2sc18_90 with dissolve
        el "And you don't even need to say incantations, and without being taught anything about magic?"
        scene ch2sc18_91 with dissolve
        el "Even the most skilled sorceresses practice for years, even decades, before they are able to properly control their magic."
        scene ch2sc18_92 with dissolve
        $ renpy.pause()
        scene ch2sc18_93 with dissolve
        el "That’s what makes me think it might be different with you."
        scene ch2sc18_94 with dissolve
        el "I-I don’t think it’s just your mothers magic that has passed down to you."
        scene ch2sc18_95 with dissolve
        $ renpy.pause()
        scene ch2sc18_96 with dissolve
        mc "Your father told me a bit about my abilities when I was younger, but even he didn’t know much."
        scene ch2sc18_97 with dissolve
        $ renpy.pause()
        scene ch2sc18_98 with dissolve
        el "What did he tell you?"
        scene ch2sc18_96 with dissolve
        mc "He said they will grow with time, the more I learn to control them."
        scene ch2sc18_99 with dissolve
        mc "He even told me that when I held... Mama... in my arms after I found her, he saw me absorbing her essence."
        scene ch2sc18_100 with dissolve
        mc "And he thought that my parents were murdered because of my... abilities or powers, or whatever they are."
        scene ch2sc18_101 with dissolve
        $ renpy.pause()
        scene ch2sc18_102 with dissolve
        el "Why would someone go to such extremes just because a ten-year-old child has some kind of power?"
        scene ch2sc18_100 with dissolve
        mc "Well, either to kill me, because I could be a threat to the kingdom..."
        scene ch2sc18_103 with dissolve
        mc "Or to use me in some way that would benefit them."
        scene ch2sc18_104 with dissolve
        mc "Your father seemed to believe that the person who killed my parents is an important figure in the capital."
        scene ch2sc18_105 with dissolve
        $ renpy.pause()
        scene ch2sc18_106 with dissolve
        el "You mean the shady, disgusting, psycho-murderer who ruined both our lives?"
        scene ch2sc18_107 with dissolve
        $ renpy.pause()
        scene ch2sc18_108 with dissolve
        mc "Yes. That’s the one."
        "Your fist tightens as you think about the guy."
        scene ch2sc18_109 with dissolve
        $ renpy.pause()
        scene ch2sc18_110 with dissolve
        $ renpy.pause()
        "."
        ".."
        scene ch2sc18_111 with dissolve
        $ renpy.pause()
        scene ch2sc18_112 with dissolve
        $ renpy.pause()
        scene ch2sc18_113 with dissolve
        $ renpy.pause()
        scene ch2sc18_114 with dissolve
        el "Hey, [mc]."
        scene ch2sc18_115 with dissolve
        el "We’ll find him. I know it!"
        scene ch2sc18_116 with dissolve
        el "And when we do... we’ll have {b}our{/b} revenge."
        scene ch2sc18_117 with dissolve
        $ renpy.pause()
        mct "She's right... whoever killed my parents, they also indirectly caused Eliza's life to crumble."
        scene ch2sc18_118 with dissolve
        $ renpy.pause()
        scene ch2sc18_119 with dissolve
        mc "Thank you."
        mc "Let's keep moving."
        el "*Nods* Mhm-hm!"
        scene black with Dissolve(1.5)
        $ renpy.pause(0.5)
        "You continue onward, walking a few more miles through the meadowy terrain."
        scene ch2sc18_120 with Dissolve(1.5)
        $ renpy.pause()
        scene ch2sc18_121 with dissolve
        $ renpy.pause()
        scene ch2sc18_122 with dissolve
        $ renpy.pause()
        scene ch2sc18_123 with dissolve
        $ renpy.pause()

        scene ch2sc18_124 with dissolve
        el "Hmm? Why’d you stop so suddenly?"

        scene ch2sc18_125 with dissolve
        mc "Look."

        scene ch2sc18_126 with dissolve
        $ renpy.pause()

        scene ch2sc18_127 with dissolve
        $ renpy.pause()

        scene ch2sc18_128 with dissolve
        $ renpy.pause()

        scene ch2sc18_129 with dissolve
        el "Its... beautiful."
        menu:
            "Hold her hand.":
                scene ch2sc18_130 with dissolve
                $ renpy.pause(1.5)
                scene ch2sc18_131 with dissolve
                $ renpy.pause(1.5)
                scene ch2sc18_132 with dissolve
                $ renpy.pause(1.5)
                scene ch2sc18_131 with dissolve
                $ renpy.pause(1.5)
                scene ch2sc18_132 with dissolve
                $ renpy.pause(1.5)
                scene ch2sc18_133 with dissolve
                $ renpy.pause()
                scene ch2sc18_134 with dissolve
                $ renpy.pause()
                scene ch2sc18_135 with dissolve
                "You feel Eliza holding tightly onto your hand."
                scene ch2sc18_133 with dissolve
                $ eliza_trust += 2
                "There’s something oddly comforting having her small, soft hand resting in yours."
                "Eliza likes holding hands with you, her trust has increased by {size=+3}{b}{color=#2bff8b}2{/color}{/b}{/size}."
                scene ch2sc18_135 with dissolve
                $ renpy.pause()
                scene ch2sc18_136 with dissolve
                el "Happy."
                scene ch2sc18_137 with dissolve
                mc "Huh?"
                scene ch2sc18_136 with dissolve
                el "I’m happy."
                menu:
                    "Me too.":
                        scene ch2sc18_139 with dissolve
                        mc "Despite everything... I’m happy too."
                        mc "In moments like this, with you... I catch myself feeling happy."
                        scene ch2sc18_133 with dissolve
                        with vpunch
                        "She squeezes your hand firmly"
                        scene ch2sc18_140 with dissolve
                        $ renpy.pause()
                        scene ch2sc18_141 with dissolve
                        el "Do you intend to carry me until we find a resting spot?"
                        scene ch2sc18_142 with dissolve
                        el "My knees feel like jelly-jam when you say these things, [mc]."
                        scene ch2sc18_143 with dissolve
                        mc "*Chuckles* I’ll try to keep that in mind... Kitten."
                        scene ch2sc18_144 with dissolve
                        "Eliza softly purrs as you stroke her cheek."
                        el "*Purrs softly* Nnnhh..."
                        scene ch2sc18_145 with dissolve
                        mct "She's so cute."
                        scene ch2sc18_146 with dissolve
                        mc "Let’s get going, we’ll want to find shelter before nightfall."
                        scene ch2sc18_147 with dissolve
                        el "..."
                        scene ch2sc18_148 with dissolve
                        el "Mmhmm."
                        scene ch2sc18_149 with dissolve
                        $ renpy.pause()
                        scene ch2sc18_150 with dissolve
                        $ renpy.pause()
                        scene ch2sc18_151 with dissolve
                        el "Huh?!"
                        scene ch2sc18_152 with dissolve
                        el "H-Hey wait up!"
                        mc "*Chuckles* Move those legs of yours missy!"
                        el "Not fair! You were caressing me!"

                    "I can’t allow myself to be happy. Not yet.":
                        scene ch2sc18_139 with dissolve
                        mc "I... never mind. We'd better get going."
                        scene ch2sc18_142 with dissolve
                        el "*Sigh* Sure."

            "Just enjoy the view.":
                scene ch2sc18_128 with dissolve
                mc "With all the doom and gloom the world throws at us, it’s good to know places like this exist."
                scene ch2sc18_129 with dissolve
                el "Agreed. We have to appreciate moments like these."

        scene black with Dissolve(1.5)
        stop music fadeout 2.0
        "Meanwhile... back in Riverside."

        scene ch2sc18_153 with Dissolve(1.5)
        play music darknight_3 fadein 1.0
        $ renpy.pause()

        scene ch2sc18_154 with dissolve
        $ renpy.pause()

        scene ch2sc18_155 with dissolve
        $ renpy.pause()

        scene ch2sc18_156 with dissolve
        $ renpy.pause()

        scene ch2sc18_157 with dissolve
        cl "Sir, I’m afraid we’re closed at the moment. I’m still preparing for tonight’s opening."

        scene ch2sc18_158 with dissolve
        $ renpy.pause()

        scene ch2sc18_159 with dissolve
        $ renpy.pause()

        scene ch2sc18_160 with dissolve
        cl "I must ask that you return later, once we're open."

        scene ch2sc18_161 with dissolve
        cl "This is highly inappropriate!"

        scene ch2sc18_162 with dissolve
        cl "S-Stop right there!"

        scene ch2sc18_163 with dissolve
        cl "Stay back!"

        scene ch2sc18_164 with dissolve
        with vpunch
        $ renpy.pause()

        scene ch2sc18_165 with dissolve
        cl "Hrrrhh! Rrhrrrhhh!"

        scene ch2sc18_165 with dissolve
        with vpunch
        uk "Where. Is. He?"
        cl "Hrrrhh... W-Who? Hraahh!"

        scene ch2sc18_166 with dissolve
        with vpunch
        uk "I asked nicely already. Don't make me ask again."

        scene ch2sc18_167 with dissolve
        cl "W-who are you talking about?!"

        scene ch2sc18_166 with dissolve
        with vpunch
        cl "Arrrghh!"
        uk "Where is he!"
        uk "The boy... when did he leave?"

        scene ch2sc18_167 with dissolve
        cl "H-He left this morning."

        scene ch2sc18_166 with dissolve
        with vpunch
        uk "Which direction?"
        cl "Hrraarrrh!!"

        scene ch2sc18_167 with dissolve
        cl "Towards Luxenford, the capital!"

        scene ch2sc18_168 with dissolve
        uk "See? That wasn’t so hard, was it? You old geezer."
        cl "*Coughs* Bas-"

        scene ch2sc18_166 with dissolve
        with vpunch
        uk "Careful now, you don’t wish to spoil my good mood."

        scene ch2sc18_169 with dissolve
        $ renpy.pause()

        scene ch2sc18_170 with dissolve
        cl_t "[mc]... I-I’m sorry."

        scene ch2sc18_171 with dissolve
        cl_t "May the Divines forgive me."

        scene black with Dissolve(3)
        stop music fadeout 1.0

        scene ch2sc18_172 with Dissolve(1.5)
        play music chill_3 fadein 1.0
        al_t "*Heavy sigh* I can’t believe he's gone again."

        scene ch2sc18_173 with dissolve
        $ renpy.pause()

        scene ch2sc18_174 with dissolve
        $ renpy.pause()

        scene ch2sc18_175 with dissolve
        al_t "I know we talked it through last night, so why do I feel so uncertain that he’ll return?"

        scene ch2sc18_176 with dissolve
        al_t "No, stop it right this second Alice! I will definitely see him again."

        scene ch2sc18_177 with dissolve
        al_t "And when I do, this time I'll be brave enough to tell him how I really feel."

        scene ch2sc18_178 with dissolve
        with vpunch
        al_t "Arrhrh! Why didn’t I just tell him last night?!"
        al_t "Maybe... maybe he would’ve stayed."
        scene ch2sc18_179 with dissolve
        al_t "No, I know him better than that."
        al_t "He’s way too stubborn when he’s set his mind to something."
        scene ch2sc18_180 with dissolve
        al_t "No use crying about it like a baby now. I’ll just have to trust in his promise."
        scene black with Dissolve(2)
        stop music fadeout 2.0
        $ renpy.pause(1)
        scene ch1sc2_c1a33 with Dissolve(2)
        play music chill_4 fadein 1.0
        $ renpy.pause()
        scene ch1sc2_c1a32 with dissolve
        $ renpy.pause()
        scene ch1sc2_c1a31 with dissolve
        $ renpy.pause()
        scene ch2sc18_180 with dissolve
        al_t "[mc]... I-I..."
        al_t "I love you."
        stop music fadeout 2.0
        scene black with Dissolve(2)
        $ renpy.pause(1)
        scene ch2sc10_204 with Dissolve(2)
        play music chill_4 fadein 1.0
        $ renpy.pause(0.5)
        ast "Goodness! It makes a huge difference when using this technique! Thank you Maya!"
        my "*Giggles* You're a quick learner, it feels good being able to teach you these things."
        scene ch2sc10_205 with Dissolve(2)
        $ renpy.pause(0.5)
        ast "By all means, teach me your ways! You're the coolest woman I've ever known..."
        ast "I'd like to become a woman just as confident and capable as you."
        scene ch2sc10_206 with Dissolve(1)
        $ renpy.pause(0.5)
        my "Oh honey... you'll be surpassing me in no time, believe me."
        my "I'm nothing special."
        scene ch2sc10_205 with Dissolve(1)
        $ renpy.pause(0.5)
        ast "You are! And you better stop thinking like that, or... or I'll splash you!"
        scene ch2sc10_206 with Dissolve(1)
        $ renpy.pause(0.5)
        my "Don't you dare! *Giggles*"
        ast "But really, thank you for teaching me Maya..."
        scene ch2sc10_205 with Dissolve(1)
        $ renpy.pause(0.5)
        ast "Getting the soot and ashes out of daddy's clothes has been a nightmare, but this works really well!"
        my "Yeah, rubbing the clothing like this with the water and reeds mixed in, will clean it thoroughly."
        scene ch2sc10_207 with Dissolve(1)
        $ renpy.pause(0.5)
        my "So..."
        ast "Soooo...? *Giggles*"
        my "Are you going to tell me about this boy you fancy?"
        scene ch2sc10_208 with Dissolve(1)
        $ renpy.pause(0.5)
        with vpunch
        ast "*Gasps* B-Boy?! What boy? You're being silly!"
        my "*Snickers* I'm being silly am I? You've been overly eager for me to teach you how to be a woman as of late."
        ast "You're saying outrageous things... I... there's... he's... stop it!"
        scene ch2sc10_209 with Dissolve(1)
        $ renpy.pause(0.5)
        ast "M-Maya! You're embarrasing me!"
        my "Why? It's only the two of us here, I'm done with laundry, I'll be over here... soaking myself in the lovely lake."
        my "Come join me when you're done and ready to talk boys. *Snickers*"
        ast "*Gasps* Maya! Uggghhh!"
        scene ch2sc10_210 with Dissolve(2)
        $ renpy.pause(0.5)
        my "*Moans softly* Mmh... this is the best part of doing laundry... getting a moment to bathe in the lake."
        my "Mmhhh... feeling the setting sun's last warm rays caress my wet skin... mmh..."
        scene ch2sc10_211 with Dissolve(2)
        $ renpy.pause(0.5)
        my "*Moans* Ohh... I should have a few minutes before Asta is done with laundry..."
        my "Just enough time to think about my precious boy... mmh... he finally returned to Riverside... to me."
        scene ch2sc10_210 with Dissolve(2)
        $ renpy.pause(0.5)
        my "Seeing him again... feeling his manly body as we embraced... mmh..."
        my "I need him so badly... I can't stop thinking about him... ohh..."
        scene ch2sc10_211 with Dissolve(2)
        $ renpy.pause(0.5)
        my "That's my good boy... touch me just like that- aahh... feeling my dense breasts... mmhh..."
        my "You're making me feel so good baby... in a way only you can... ohh..."
        scene ch2sc10_212 with Dissolve(2)
        $ renpy.pause(0.5)
        ast "*Calls out* Mayaaaa? I'm done! Where are you?"
        my "*Giggling* Over here sweetie! Come join me, the lake is just heavenly!"
        scene ch2sc10_213 with Dissolve(2)
        $ renpy.pause(0.5)
        ast "You look like you're enjoying yourself while I had to slave away with the last bits of laundry!"
        my "*Snickers* Time for your next lesson, a woman needs to take every opportunity to enjoy herself."
        ast "Oh yeah? *Giggling*"
        scene ch2sc10_214 with Dissolve(2)
        $ renpy.pause(0.5)
        ast "Then I better follow your instructions and enjoy myself!"
        my "That's my girl! *Giggling* Come soak in the lukewarm water, you'll feel like a new woman."
        scene ch2sc10_215 with Dissolve(2)
        $ renpy.pause(0.5)
        ast "Ahh... the height of every day is undressing and just being... free."
        my "You're preaching to the choir... my breasts are desperate for every moment of freedom."
        scene ch2sc10_216 with Dissolve(2)
        $ renpy.pause(0.5)
        ast "I wish I had breasts like yours... I've seen it when you walk through the market, you have the attention of every man."
        my "Trust me honey, that is not something you want... my breasts have more downsides than perks."
        my "Speaking of perks... yours are perfectly perky, that is something a lot of men crave."
        scene ch2sc10_217 with Dissolve(2)
        $ renpy.pause(0.5)
        my "Now, I think it's about time you tell me about this boy you fancy."
        my "I'm going to have to approve of him if he has any hope of dating you."
        ast "*Giggling* Mh-hm!"
        scene ch2sc10_218 with Dissolve(2)
        $ renpy.pause(0.5)
        ast "He looks really cute!"
        ast "Like, the type of guy you'd dream about in a indecent dream! *Giggles*"
        scene ch2sc10_219 with Dissolve(1)
        $ renpy.pause(0.5)
        my "Oooh! Sounds like a snack... I bet you just wanna eat him up! Don't you?"
        ast "Maya! You're being silly... again!"
        scene ch2sc10_218 with Dissolve(1)
        $ renpy.pause(0.5)
        ast "I wonder what he would taste like..."
        my "I knew it!"
        my "More details, darling."
        scene ch2sc10_219 with Dissolve(1)
        $ renpy.pause(0.5)
        ast "Hmm, let's see... he was quite tall, not as tall as daddy but he had a lean frame."
        ast "Dark hair, sky blue eyes... impeccable jawline... *Giggles* And those lips..."
        scene ch2sc10_218 with Dissolve(1)
        $ renpy.pause(0.5)
        my "Mmhh... I love a man with kissable lips!"
        my "So... have you tasted his lips yet? Was he your first kiss?"
        scene ch2sc10_219 with Dissolve(1)
        $ renpy.pause(0.5)
        ast "I-... I haven't kissed him yet! We... I... I haven't spoken to him!"
        my "Oh... honey, you must! You're head over heels crushing on him by the sound of it!"
        scene ch2sc10_217 with Dissolve(1.5)
        $ renpy.pause(0.5)
        ast "You make it sound so easy... he's... intimidating!"
        ast "I think he might be new to Riverside, I haven't seen him around before..."
        scene ch2sc10_218 with Dissolve(1.5)
        $ renpy.pause(0.5)
        my "New to Riverside huh? That's perfect!"
        my "You have a great reason to speak to him now, you could offer to show him around."
        scene ch2sc10_219 with Dissolve(1.5)
        $ renpy.pause(0.5)
        my "Where did you meet him?"
        ast "At... home."
        ast "He was... visiting my dad by the looks of it? Oh and daddy called him 'Little bear'?"
        scene ch2sc10_220 with Dissolve(1.5)
        $ renpy.pause(0.5)
        myt "{b}!!!!{/b}"
        with vpunch
        myt "No way... a young man she hasn't seen in Riverside... dark hair... sky blue eyes... handsome..."
        myt "She's talking about-... [mc]... it has to be! Oh this is bad!"
        myt "I've been unknowingly encouraging her to go after him! No, no, no, no!"
        scene ch2sc10_221 with Dissolve(1.5)
        $ renpy.pause(0.5)
        ast "I think daddy will approve, he seemed quite happy with him."
        ast "If everything goes well, maybe he'll be the man who claims my virtue... *giggles*"
        scene ch2sc10_222 with Dissolve(1.5)
        $ renpy.pause(0.5)
        ast "And if I give him my virtue... we'd have to get married, right Maya?"
        ast "I can just imagine it! Daddy walking me down the aisle and you being my maid of honor!"
        my "Huh?? Oh... this is a little sudden sweetie, don't you think? You haven't even spoken to the guy!"
        scene ch2sc10_223 with Dissolve(1.5)
        $ renpy.pause(0.5)
        ast "I know, but thanks to you, I feel emboldened by your words, I'm going to do it! I'll talk to him!"
        ast "Thanks to you I might finally get a boyfriend! Thank you Maya! I'm so excited!"
        my "Oh honey... please don't act too sudden, you know I say these crazy things..."
        my "What do I know? I'm just an old woman trapped in a loveless marriage."
        ast "You're the best woman I know! You've been like a mother to me since I arrived."
        ast "I can't think of anyone better to listen to!"
        scene ch2sc10_224 with Dissolve(1.5)
        $ renpy.pause(0.5)
        ast "This is most exciting! I'm going to go home and see if I have any nice dresses!"
        my "S-Sure... sounds great sweetie..."
        scene ch2sc10_225 with Dissolve(1.5)
        $ renpy.pause(0.5)
        my "This is bad! Damnit! Me and my big mouth just had to encourage her!"
        my "She's right, I've been like a mother to her and she's been like a daughter to me..."
        my "If she catches feelings for [mc]... I'm... I'm never going to get my chance."
        scene ch2sc10_226 with Dissolve(1.5)
        $ renpy.pause(0.5)
        my "As if my feelings for him weren't complicated enough..."
        my "Now Asta being involved is sure to complicate things even further!"
        my "*Exhales* Just... my... luck..."
        scene ch2sc10_227 with Dissolve(1.5)
        $ renpy.pause(0.5)
        my "*Bubbling* ..."
        my "*Bubbling* {size=+3}{b}.................{/b}{/size}"
        scene black with Dissolve(2.5)
        #play music summon_3 fadein 1.0
        stop music fadeout 1.0
        $ renpy.pause(1)
        scene ch2sc10_228 with Dissolve(2)
        play music forest_1 fadein 1.0
        $ renpy.pause(0.5)
        myt "That dip in the lake was so good..."
        myt "*Sighs* I better hurry home and get started on dinner."
        myt "Shane will throw a fit if dinner isn't on the table when he gets home..."
        scene ch2sc10_229 with Dissolve(1.5)
        $ renpy.pause(0.5)
        myt "Knowing him he'll find a reason to be cross with me tonight, he always does."
        myt "Some days I wish he wouldn't come home at all..."
        scene black with Dissolve(2)
        #play music summon_3 fadein 1.0
        stop music fadeout 1.0
        scene ch2sc10_55 with Dissolve(2)
        play music forest_1 fadein 1.0
        $ renpy.pause(0.5)
        my "*Exhales* Okay... I made it."
        my "I'll just set the table properly and I can get started on dinner."
        scene ch2sc10_230 with Dissolve(1)
        $ renpy.pause(0.5)
        sh "Maya I'm home, I hope dinner is ready for once!"
        my "Shane, you're home so soon? I thought you'd be at least another twenty minutes..."
        sh "What's this? You're just now setting the table? You haven't even started dinner?!"
        scene ch2sc10_231 with Dissolve(1)
        $ renpy.pause(0.5)
        my "I only just got in the door, I'm trying my best you know?"
        sh "Your best? You can't even have dinner ready for your husband after he's busted his ass all day?"
        my "I've been out washing your clothes, do you know how difficult sawdust is to wash out?"
        scene ch2sc10_232 with Dissolve(1)
        $ renpy.pause(0.5)
        sh "You've been slacking off by the sound of it... always making excuses for your poor performance."
        my "Shane, why must you always complain? I don't see you helping out around here-"
        scene ch2sc10_233
        with vpunch
        $ renpy.pause(0.5)
        my "*Gasps* Aah! Owh!"
        sh "*Scoffs* This fat juicy ass of yours must be slowing you down since you can't keep up with chores."
        sh "Maybe you need a spanking more often? To remind you of your duties as a wife?"
        scene ch2sc10_234 with Dissolve(1)
        $ renpy.pause(0.5)
        my "*Angrily* Shane! Go away!"
        sh "Whatever... just get that dinner on the table."
        my "I'm trying my best here!"
        scene ch2sc10_55 with Dissolve(1)
        $ renpy.pause(0.5)
        my "You never pitch in with any of the household chores... you think it's easy?"
        sh "That's your job, my job is to provide for our family, and here you are, taking all day to wash clothes?"
        my "I've been teaching Asta how to do laundry effectively."
        scene ch2sc10_56 with Dissolve(1)
        $ renpy.pause(0.5)
        my "Maybe you could show some compassion? Asta wants to learn how to earn her keep."
        sh "*Scoffs* Why the fuck would I care about some girl who shows up out of nowhere on another man's doorstep?"
        my "You're a heartless man, you know that? Gibson is her father!"
        scene ch2sc10_51 with Dissolve(1)
        $ renpy.pause(0.5)
        sh "Stop wasting time setting the table woman! Who cares what dinnerware we use, just make that damn dinner!"
        my "I care! We have children! We're going to eat dinner as we always do, properly."
        scene ch2sc10_53 with Dissolve(1)
        $ renpy.pause(0.5)
        sh "*Scoffs* Family? What a joke, you're out there wasting your time with another man's child."
        sh "When you should be here, at home, doing your duties as a wife and mother."
        scene ch2sc10_52 with Dissolve(1)
        $ renpy.pause(0.5)
        my "Do you even hear yourself?! So now I can't spend time with other people?"
        my "If Asta wants me to show her a bit of how to manage a household, then I will do just that."
        scene ch2sc10_53 with Dissolve(1)
        $ renpy.pause(0.5)
        sh "Have you no shame woman?"
        sh "You're just using that poor girl as a pretense to see Gibson I bet..."
        sh "You think people won't notice how you're playing mother and wife to them?"
        scene ch2sc10_52 with Dissolve(1)
        $ renpy.pause(0.5)
        my "Shane! That's enough... you're out of line."
        scene ch2sc10_53 with Dissolve(1)
        $ renpy.pause(0.5)
        sh "No, I think not... you're the one who's crossing lines."
        sh "Don't you realise that your actions will have you labeled as the village whore?"
        scene ch2sc10_52 with Dissolve(1)
        $ renpy.pause(0.5)
        my "{b}Shane!{/b}"
        scene ch2sc10_53 with Dissolve(1)
        $ renpy.pause(0.5)
        sh "Not that your reputation matters to me, but we're married, your actions will affect my reputation!"
        scene ch2sc10_52 with Dissolve(1)
        $ renpy.pause(0.5)
        my "Your reputation as what? The village drunk?"
        scene ch2sc10_51 with Dissolve(1)
        $ renpy.pause(0.5)
        sh "What did you just say to me?!"
        sh "Maybe it's time you get a firm backhand? You've been a little too snarky as of late!"
        scene ch2sc10_234 with Dissolve(1)
        $ renpy.pause(0.5)
        my "{b}LEAVE!{/b} The longer you disturb me, the longer it'll be before dinner is finished!"
        sh "*Scoffs* You're lucky I'm starving... otherwise I'd slapped that attitude out of you once and for all."
        scene black with Dissolve(1)
        $ renpy.pause(0.5)
        scene ch2sc10_55 with Dissolve(1)
        $ renpy.pause(0.5)
        my "*Exhales* That was close... he's getting more aggressive..."
        my "Flynn and Sabrina have spoken of wanting to go to Luxenford, the capital."
        my "As much as I want them to remain in Riverside, I need to encourage them to leave."
        my "I refuse to let them be witness to what their father is becoming... or what he might do."
        scene black with Dissolve(2)
        #play music summon_3 fadein 1.0
        stop music fadeout 1.0
        $ renpy.pause(1)

        scene ch2sc18_181 with Dissolve(2.5)
        play music explore_2 fadein 1.0
        $ renpy.pause(0.5)
        el "So... is there anything else my father knew about you? He must have known about you before."
        scene ch2sc18_182 with dissolve
        el "Why else would he have been ready to take you away?"
        scene ch2sc18_183 with dissolve
        mc "Oren... your father, he told me that I’m not human."
        scene ch2sc18_184 with dissolve
        with vpunch
        el "{size=+3}{b}WHAT?!{/b}{/size}"
        scene ch2sc18_185 with dissolve
        mc "I mean-"
        scene ch2sc18_184 with dissolve
        with vpunch
        el "N-Not human?! {size=+3}{b}WHaaaAT?!{/b}{/size}"
        scene ch2sc18_186 with dissolve
        mc "Forget it."
        scene ch2sc18_187 with dissolve
        $ renpy.pause()
        scene ch2sc18_188 with dissolve
        el "No! No, I’m sorry... that was just surprising to hear."
        el "I mean... you look totally human?"
        scene ch2sc18_189 with dissolve
        mc "You can say it."
        scene ch2sc18_190 with dissolve
        el "Huh? Say what?"
        scene ch2sc18_189 with dissolve
        mc "That I’m a freak."
        scene ch2sc18_191 with dissolve
        el "*Sigh*"
        scene ch2sc18_192 with dissolve
        el "Do you want me to beat you up?"
        scene ch2sc18_193 with dissolve
        mc "No?"
        scene ch2sc18_192 with dissolve
        with vpunch
        el "Then stop saying such horseshit!"
        el "I will never see you as anything but you."
        scene ch2sc18_194 with dissolve
        el "It’s your actions that matter to me, [mc]."
        el "Not something that’s out of your control."
        scene ch2sc18_193 with dissolve
        mc "I’m not used to anyone being so... accepting of me."
        scene ch2sc18_194 with dissolve
        el "Well, you should know me well enough by now. I’m not like everyone else."
        scene ch2sc18_196 with dissolve
        mc "I’ve noticed."
        el "..."
        scene ch2sc18_197 with dissolve
        el "Good."
        scene ch2sc18_198 with dissolve
        el "So, tell me. If you’re not human, what are you?"
        scene ch2sc18_199 with dissolve
        el "Some sort of magical elf? No... your ears aren't pointy enough."
        scene ch2sc18_200 with dissolve
        el "Oh! Oh! A merman, perhaps? You know, like a mermaid, but a man?"
        scene ch2sc18_201 with dissolve
        mc "..."

        scene ch2sc18_202 with dissolve
        el "Please don’t be a troll in disguise!"

        scene ch2sc18_203 with dissolve
        el "I don’t think I could handle you being a smelly troll."
        scene ch2sc18_186 with dissolve
        mc "Are you done?"
        scene ch2sc18_204 with dissolve
        el "Hmmm... Mhmm."
        scene ch2sc18_205 with dissolve
        el "Yup! I’m all out of plausible scenarios."
        scene ch2sc18_206 with dissolve
        mc "It’s been truly enlightening listening to your theories. However-"
        scene ch2sc18_207 with dissolve
        mc "According to Oren, I’m something called a {b}'Nephilim'{/b}."
        scene ch2sc18_208 with dissolve
        el "Nephilim?"
        scene ch2sc18_209 with dissolve
        el "What in the blazes is a Nephilim?"
        el "You mentioned this once before... at the apple orchards in Riverside."
        scene ch2sc18_210 with dissolve
        el "I haven't heard of a Nephilim before..."
        el "It certainly wasn't in my mother’s books."
        el "What... is a Nephilim? Will you tell me?"
        scene ch2sc18_207 with dissolve
        mc "There’s a good reason you haven't heard of them."
        mc "Apparently, a Nephilim is the child of a human and an angel."
        scene ch2sc18_211 with dissolve
        el "A-Angel?? Are you for real?!"
        scene ch2sc18_212 with dissolve
        mc "Yes. Your father told me that, other than me, there’s only been one other Nephilim in the history of Midomir."
        scene ch2sc18_213 with dissolve
        mc "Apparently, the other one... Balthazar, he’s the reason the first era ended over five hundred years ago."
        scene ch2sc18_216 with dissolve
        el "Woah, what the actual fuck?"
        el "Did he turn out to be some kind of evil monster?"
        scene ch2sc18_215 with dissolve
        mc "Supposedly, he was able to devour the souls of anything that had recently died."
        scene ch2sc18_214 with dissolve
        mc "Which is something I’m also able to do."

        scene ch2sc18_215 with dissolve
        mc "He got so consumed with feeding on souls and the power it gave him, he wanted to lay waste to all of Midomir."

        scene ch2sc18_216 with dissolve
        el "That’s horrible!"

        scene ch2sc18_215 with dissolve
        mc "He managed to kill thousands upon thousands during the Abyss wars in the 1st Era."
        mc "Humans... Animals... Creatures... Dwarves... Elves... Gnomes... Faes... anything he could devour."

        scene ch2sc18_214 with dissolve
        mc "Eventually he was stopped, though."
        mc "A gathering of the ten strongest wizards and sorceresses sacrificed themselves."
        mc "They created a sacred spell known as {b}'Seal of Solomon'{/b}"

        scene ch2sc18_217 with dissolve
        mc "The mages each had an enchanted ring that they sealed their powers within."

        scene ch2sc18_218 with dissolve
        mc "Then they linked the ten enchanted rings in a ritual."
        mc "And with the combined power, they were finally able to seal Balthazar away in the depths of the Abyss."
        scene ch2sc18_219 with dissolve
        mc "But after sealing him away, all of the wizards and sorceresses died within a week of the ritual."
        mc "It turned out, the rings had also absorbed some of their life essence along with their mana."
        scene ch2sc18_217 with dissolve
        mc "Casting such a complicated spell and having their powers drained, they were too weak to continue."
        scene ch2sc18_214 with dissolve
        mc "All that, just to banish him."
        mc "Now, five hundred years later and we're here in the 2nd Era of Midomir."
        mc "And Stories of Balthazar have been all but forgotten."
        mc "Your father had to do some thorough digging for any scriptures from that time period."
        scene ch2sc18_220 with dissolve
        el "[mc], if all this is true..."
        el "That means..."
        scene ch2sc18_215 with dissolve
        mc "Yeah... I could end up like him, or worse."
        scene ch2sc18_216 with dissolve
        el "There’s no chance of that."
        scene ch2sc18_214 with dissolve
        mc "Yes there is-"
        scene ch2sc18_221 with dissolve
        with vpunch
        el "{b}NO!{/b} I won’t let it happen."
        scene ch2sc18_214 with dissolve
        mc "You won’t be able to stop it."
        scene ch2sc18_222 with dissolve
        with vpunch
        "Eliza grabs you firmly and rests her forehead against your chest."
        el "Oh, yes I will! There’s absolutely no way that I’m letting you-"
        el "-The only person that matters to me, become like that... Balthazar thing."
        scene ch2sc18_223 with dissolve
        el "You won’t become that, I won’t let you."
        scene ch2sc18_224 with dissolve
        el "You got that?"
        scene ch2sc18_225 with dissolve
        mc "Eliza..."
        scene ch2sc18_226 with dissolve
        el "I said-"
        #CHOICE
        menu:
            "Kiss her. ({color=#ff8cdd}Romance{/color})":
                scene ch2sc18_227 with dissolve
                with vpunch
                "Eliza will remember this. Her trust has increased by {size=+3}{b}{color=#2bff8b}3{/color}{/b}{/size}."
                $ eliza_trust += 3
                scene ch2sc18_228 with dissolve
                $ renpy.pause()
                scene ch2sc18_229 with dissolve
                $ renpy.pause()
                scene ch2sc18_230 with dissolve
                el "Mhmm... Mhmh."
                $ eliza_path = True
                elt "His lips are amazing... Mmmh."
                scene ch2sc18_230 with dissolve
                elt "I don’t want him to stop... his taste..."
                scene ch2sc18_232 with dissolve
                $ renpy.pause()
                scene ch2sc18_233 with dissolve
                $ renpy.pause()
                scene ch2sc18_234 with dissolve
                $ renpy.pause()
                scene ch2sc18_230 with dissolve
                elt "{b}OH!{/b}... Mmhm!"
                $ eliza_relationship = True
                scene ch2sc18_235 with dissolve
                elt "He's grabbing my ass! A-And I don’t even mind it... Mmmmhh."
                scene ch2sc18_230 with dissolve
                elt "His touch... it makes me feel safe, wanted, desired."
                scene ch2sc18_230 with dissolve
                elt "I’ve thought about kissing him countless times since we left bed this morning."
                scene ch2sc18_235 with dissolve
                elt "How much I just wanted him to grab me at any moment and just kiss me like I’m his."
                scene ch2sc18_238 with dissolve
                elt "*Soft moans* Mhhmmh. [mc] ... Mmh ... I can’t help the way I feel about him. Not anymore."
                mct "Hearing Eliza’s soft moans as she kisses, would send any man over the edge."
                scene ch2sc18_239 with dissolve
                "Before you are able to gather your thoughts, she continues gently sucking your bottom lip."
                el "Mmhmm... Mmh!"
                scene ch2sc18_240 with dissolve
                $ renpy.pause(1)
                el "*Giggles softly* Yum..."
                scene ch2sc18_241 with dissolve
                el "That was... wild."
                scene ch2sc18_242 with dissolve
                el "W-What was that for?"
                scene ch2sc18_243 with dissolve
                el "N-Not that I’m complaining or anything!!"
                scene ch2sc18_244 with dissolve
                mc "I just felt like kissing you."
                scene ch2sc18_245 with dissolve
                $ renpy.pause()
                scene ch2sc18_246 with dissolve
                el "*Shy* Wa-Was it good for you?"
                scene ch2sc18_244 with dissolve
                mc "Yes, very."
                scene ch2sc18_247 with dissolve
                $ renpy.pause()
                scene ch2sc18_248 with dissolve
                el "G-Good! For me also!"
                el "A-Are you going to do it again?"
                scene ch2sc18_244 with dissolve
                mc "Don’t worry, kitten. You’re safe for now."
                scene ch2sc18_250 with dissolve
                el "G-Good, good, good, good! Safe is Gooood!"
                scene ch2sc18_251 with dissolve
                elt "Dammit! Safe is not good!"
                elt "Not good at all! Why did I say that!"
                scene ch2sc18_252 with dissolve
                elt "Now he's going to think I didn’t like it as much. Dammit. My stupid mouth!"
                elt "I wanted to say, put your tongue back into my mouth! But I couldn't just say that... could I?"
                scene ch2sc18_254 with dissolve
                mc "You know, I heard somewhere that kittens like having their heads patted."
                scene ch2sc18_255 with dissolve
                mc "It seems to be true."
                scene ch2sc18_255_5 with dissolve
                elt "Nnnyaaahh... Mmhmm."
                scene ch2sc18_255 with dissolve
                elt "I’ve never felt so relaxed. He noticed I was upset with myself and calmed me down."
                scene ch2sc18_255_5 with dissolve
                elt "Please, keep petting me like this, [mc]. I... I’ll be your kitten."
                scene ch2sc18_253 with dissolve
                mc "Come, we'd better get going. I want to set up camp before nightfall."
                scene ch2sc18_249 with dissolve
                elt "*Soft purrs* Nnyhhaa... Nnhhh."
                mc "Eliza? C'mon..."
                scene ch2sc18_256 with dissolve
                with vpunch
                el "Y-Yes! Coming!"
                stop music fadeout 2.0
                scene black with Dissolve(1.5)
                jump ch2sc19

            "Thank her. (Friendly)":
                scene ch2sc18_257 with dissolve
                mc "I've got it. I've got it. I’m not going to be consumed with hatred or power."
                mc "You will protect me from all the bad things."
                scene ch2sc18_258 with dissolve
                el "Now, try without the sarcasm, smartass."
                scene ch2sc18_259 with dissolve
                mc "Thank you for always having my back. Even after everything I just told you."
                scene ch2sc18_260 with dissolve
                el "None of that changes how I see you, [mc]. It never will."
                scene ch2sc18_261 with dissolve
                mc "I’m glad. Now, let’s get a move on. We still have a ways to go before we set up camp."
                scene ch2sc18_262 with dissolve
                el "Lead on!"
                stop music fadeout 2.0
                scene black with Dissolve(1.5)
                jump ch2sc19
