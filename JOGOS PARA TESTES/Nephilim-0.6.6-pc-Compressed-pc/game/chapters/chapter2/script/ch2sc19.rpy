#Start Chaper
label ch2sc19:

    #play music morning_1

    # start scene 2
        window hide dissolve
        play music happy_1 fadein 2.0
        scene black with Dissolve (2.0)
        "A few hours of wandering through the woods and pathways, you find a suitable campsite."
        scene ch2sc19_01 with Dissolve(2.0)
        el "This looks like it'll be a nice area to camp. What do you think?"
        scene ch2sc19_02 with dissolve
        mc "Good eyes. This will do nicely for tonight."
        scene ch2sc19_03 with dissolve
        mc "We can make a campfire in front of this log. That way, we won’t have to sit on the ground."
        scene ch2sc19_04 with dissolve
        el "*Giggles* I am known as the master camper in these woods!"
        scene ch2sc19_05 with dissolve
        mc "Sure you are."
        mc "Fire-keeper and master camper... that's so you."
        scene ch2sc19_06 with dissolve
        $ renpy.pause()
        "Eliza shoots you a glance of disbelief."
        scene ch2sc19_07 with dissolve
        el "Hey! I haven’t found us a bad campsite yet."
        scene ch2sc19_08 with dissolve
        mc "What about that time with Irene?"
        scene ch2sc19_09 with dissolve
        $ renpy.pause()
        scene ch2sc19_10 with dissolve
        el "You can’t blame my campsite for some crazy-lunatic and her filthy boyfriend trying to mess with us."
        scene ch2sc19_11 with dissolve
        el "Urrrh! I have goosebumps just thinking about how she was touching you."
        scene ch2sc19_12 with dissolve
        el "I’m pretty sure I even saw her licking your cheek at one point... Uuck!"

        if irene_alive == True:
            el "I'm glad you let her live... hopefully I get to run into her some day!"
            el "I'd love to kick her ass for putting her tongue on you!"

        else:
            el "I-... I'm glad you didn't let her escape... she would only hurt others."

        scene ch2sc19_16 with dissolve
        mc "I was more concerned about him hurting you, though."
        scene ch2sc19_14 with dissolve
        el "Good thing he won’t ever be able to hurt anyone again!"
        scene ch2sc19_15 with dissolve
        el "I know this sounds horrible, but I’m glad you snapped his neck like a twig."
        scene ch2sc19_16 with dissolve
        mc "He was hurting people because he thought it was 'fun'. Who knows how many others he hurt before us?"
        scene ch2sc19_16 with dissolve
        mc "Your father used to tell me, if you’re going to wield a blade, you'd better be prepared to use it."
        scene ch2sc19_17 with dissolve
        el "That sounds like him... he told me the same thing, although he used sticks as an analogy."
        el "Good thing you actually listened."
        scene ch2sc19_16 with dissolve
        mc "More often than not, I didn’t."
        mc "But when it came to combat, he had my full attention."
        scene ch2sc19_18 with dissolve
        mc "I knew it'd be a tool I'd need to achieve my end goal."
        scene ch2sc19_19 with dissolve
        $ renpy.pause()
        scene ch2sc19_20 with dissolve
        el "[mc]?"
        scene ch2sc19_21 with dissolve
        mc "Mh?"
        scene ch2sc19_22 with dissolve
        elt "I really want to ask him if he’s thought about what happens after we get our revenge."
        scene ch2sc19_23 with dissolve
        elt "Will he still want me around after we achieve our goal?"
        elt "Or does he expect us to go our separate ways afterward?"
        scene ch2sc19_20 with dissolve
        el "N-Never mind."
        scene ch2sc19_24 with dissolve
        with vpunch
        el "{b}Camp!{/b} Yes! Let’s setup camp!"
        el "I’ll go scout the area, maybe forage a bit while I’m at it."
        scene ch2sc19_25 with dissolve
        el "You take care of making this place into a halfway decent campsite."
        el "{b}OH!{/b} And get firewood."
        scene ch2sc19_26 with dissolve
        $ renpy.pause()
        scene ch2sc19_27 with dissolve
        mc "Since when are you the boss?"
        scene ch2sc19_28 with dissolve
        with vpunch
        el "{b}Now!{/b}"
        mct "I better not argue..."
        scene ch2sc19_29 with dissolve
        stop music fadeout 2.0
        mct "Geez... that girl. I'd better get started before she comes back."
        scene black with Dissolve(1.5)
        $ renpy.pause(1)
        scene ch2sc19_32 with Dissolve(1.5)
        play music outdoors_2 fadein 1.0
        $ renpy.pause(1.5)
        scene ch2sc19_30 with Dissolve(1.5)
        $ renpy.pause(0.5)
        elt "Gods! Why do I worry so much about the future? About us?"
        scene ch2sc19_31 with Dissolve(1.5)
        $ renpy.pause(0.5)
        elt "Silly question... I know why."
        scene ch2sc19_32 with Dissolve(1.5)
        $ renpy.pause(0.5)
        mct "She sure can be bossy sometimes."
        scene ch2sc19_33 with Dissolve(1.5)
        $ renpy.pause(0.5)
        mct "Pick up this, gather that... Hrrrhh."
        scene ch2sc19_34 with Dissolve(1.5)
        $ renpy.pause(0.5)
        mct "*Chuckles* At least she’s kinda cute even when she's being a pain."
        scene ch2sc19_35 with Dissolve(1.5)
        $ renpy.pause(0.5)
        mct "I guess I feel this way because..."
        #CHOICE
        menu:
            "Caring. (Neutral)":
                scene ch2sc19_36 with dissolve
                mct "I care about her."
                scene ch2sc19_37 with dissolve
                elt "I care about him."

            "Falling. ({color=#ff8cdd}Romance{/color})":
                scene ch2sc19_36 with dissolve
                mct "I’m falling for her."
                $ eliza_relationship = True
                $ eliza_path = True
                scene ch2sc19_37 with dissolve
                elt "I-I’ve fallen for him."

            "Friendship. ({color=#2bff8b}Friendly{/color})":
                scene ch2sc19_36 with dissolve
                mct "She’s become my best friend."
                $ eliza_relationship = False
                $ eliza_path = False
                scene ch2sc19_37 with dissolve
                elt "He's my first and only friend."

        scene ch2sc19_38 with dissolve
        mct "I’ve never had someone be so fiercely loyal before... it’s rather refreshing, actually."
        scene ch2sc19_39 with dissolve
        mct "I know that I can trust her completely."
        mct "Nothing I say or do will scare her away... she’s made that abundantly clear."
        scene ch2sc19_40 with dissolve
        mct "*Sigh* Anyway, I'd better get to work on camp."
        scene ch2sc19_41 with dissolve
        elt "Damn, no signs of any edible mushrooms."
        elt "I really wanted to make something yummy for him."
        scene ch2sc19_42 with dissolve
        elt "I'd better get back. Hopefully he's managed to get a fire going."
        scene ch2sc19_43 with dissolve
        elt "I swear by the Divines, if there’s another Irene situation back at camp, heads will be rolling!"
        scene ch2sc19_44 with dissolve
        $ renpy.pause()
        scene ch2sc19_45 with dissolve
        elt "Heh, heh."
        scene ch2sc19_46 with dissolve
        elt "Well, well, well."
        elt "How could I possibly pass up an opportunity like this?"
        scene ch2sc19_47 with dissolve
        elt "Target in sight... parameters scanned... Objective: Make the target surrender."
        elt "Failure: Not an option."
        scene ch2sc19_48 with dissolve
        elt "Charge!!"
        scene ch2sc19_49 with dissolve
        elt "Oh, you’re so done, 'mister I can sense danger'!"
        scene ch2sc19_50 with dissolve
        el "{b}Hhiiiiyah!{/b}"
        scene ch2sc19_51 with dissolve
        with vpunch
        $ renpy.pause()
        scene ch2sc19_52 with dissolve
        $ renpy.pause()
        scene ch2sc19_53 with dissolve
        el "Do you surrender, tough guy?"
        scene ch2sc19_54 with dissolve
        mc "Eliza? What the hell! You ambushed me!"
        scene ch2sc19_55 with dissolve
        el "Gotcha!"
        el "Do you always expect our enemies to walk up and announce themselves?"
        scene ch2sc19_56 with dissolve
        mc "No."
        scene ch2sc19_55 with dissolve
        el "What happened to your 'I can sense danger' ability?"
        el "I caught you completely off-guard."
        scene ch2sc19_57 with dissolve
        mc "I don’t view you as a threat."
        scene ch2sc19_58 with dissolve
        el "You think I’m too weak to be a threat?"
        scene ch2sc19_57 with dissolve
        mc "No, that’s not what I meant. I don’t see you as a threat because I trust you, Eliza."
        scene ch2sc19_59 with dissolve
        mc "That’s why I didn’t react. Apparently, I trust you so much that my body instinctively knows."
        scene ch2sc19_60 with dissolve
        el "R-Really? You trust me that much?"
        scene ch2sc19_59 with dissolve
        mc "Yes."
        scene ch2sc19_60 with dissolve
        el "I-I trust you too! With my life!"
        "."
        ".."
        if eliza_relationship == True:
            scene ch2sc19_61 with dissolve
            el "I’m going to kiss you now."
            scene ch2sc19_62 with dissolve
            $ renpy.pause()
            scene ch2sc19_63 with dissolve
            "As her soft, warm lips meet yours, a jolt of excitement soars through your body."
            scene ch2sc19_64 with dissolve
            "It doesn’t take long before she opens her mouth, inviting your tongue inside with hers."
            scene ch2sc19_65 with dissolve
            elt "Mmh [mc]! hhmhhmmm."
            scene ch2sc19_66 with dissolve
            ####ANIMATION####
            show mc_el_kiss2 with fade
            $ renpy.pause(3, hard=True)
            $ renpy.pause()
            "She sucks your bottom lip, moaning softly and sending small vibrations into your mouth."
            elt "MmmMmmhhh. Seems like he’s enjoying this as much as I am."
            elt "I love that just kissing me makes him hard."
            elt "[mc]... Mhmhh! Heavens! Having him pinned down between my legs. It’s... making me so wet. [mc] ... Ahhh!"
            "As Eliza gives in to her lust, she begins pushing herself down on top of you, slowly grinding her ass back and forth."
            scene ch2sc19_66 with dissolve
            $ renpy.pause(1)
            scene ch2sc19_64 with dissolve
            el "*Soft moan* Mmhhaahmmhh... W-wait... Aahhh."
            scene ch2sc19_67 with dissolve
            with vpunch
            el "{b}Wait! Time out!{/b}"
            scene ch2sc19_59 with dissolve
            mc "You good?"
            scene ch2sc19_68 with dissolve
            el "Y-Yes I’m good."
            el "*Whispers* {size=-10}{b}Very good.{/b}{/size}"
            scene ch2sc19_57 with dissolve
            mc "Then why did you stop?"
            scene ch2sc19_69 with dissolve
            elt "I can’t let him know that my panties are completely soaked because of him."
            scene ch2sc19_70 with dissolve
            el "Errrh... I-I stopped because..."


        else:
            scene ch2sc19_71 with dissolve

        scene ch2sc19_71 with dissolve
        el "We passed a lake not far back. What do you say? Wanna take a dip with me?"
        scene ch2sc19_72 with dissolve
        mc "You go ahead. I’ll probably scout the area meanwhile."
        scene ch2sc19_73 with dissolve
        el "..."
        el "......"
        scene ch2sc19_74 with dissolve
        el "Don’t be silly, You reek!"
        el "*Giggling* Last one in the lake owes a massage!"
        scene ch2sc19_75 with dissolve
        mct "*Sigh* She’s so damn competitive."
        mct "Winning a massage, though? Definitely won’t miss out on that."
        scene ch2sc19_76 with dissolve
        mc "It’s not like you smell of roses either, you know?"
        scene ch2sc19_77 with dissolve
        el "Which is why we are going swimming!"
        scene ch2sc19_78 with dissolve
        el "And for your information... I do smell like flowers!"
        scene ch2sc19_79 with dissolve
        mc "Sure."
        scene ch2sc19_80 with dissolve
        el "I’ll prove it to you later."
        el "Now, come on! There's a lake with our name on it, just waiting to be used!"
        scene ch2sc19_81 with dissolve
        mc "It'd better not be freezing cold."
        scene ch2sc19_82 with dissolve
        el "*Giggles* only one way to find out! Already looking forward to my massage!"
        scene ch2sc19_83 with dissolve
        stop music fadeout 2.0
        mct "*Sigh* ..."
        mct "She’ll regret that."
        play music battle_1 fadein 1.0
        scene ch2sc19_84 with dissolve
        $ renpy.pause()
        scene ch2sc19_85 with dissolve
        mct "Time to win that massage."
        scene ch2sc19_86 with dissolve
        $ renpy.pause()
        scene ch2sc19_86_blur with dissolve
        with vpunch
        $ renpy.pause()
        scene ch2sc19_87_blur with dissolve
        $ renpy.pause()
        scene ch2sc19_88_blur with dissolve
        mct "Heh. I’ve never gone full speed like this before."
        mct "It’s almost like she isn’t moving..."
        scene ch2sc19_87_blur1 with dissolve
        with vpunch
        stop music fadeout 2.0
        $ renpy.pause()
        scene ch2sc19_89 with dissolve
        el "Heavens!"
        play music chill_1 fadein 2.0
        scene ch2sc19_90 with dissolve
        el "*Panting* Haah... Uff! What the hell was that?"
        scene ch2sc19_91 with dissolve
        el "How were you so fast?!"
        scene ch2sc19_92 with dissolve
        elt "There’s just no way! I had a good lead on him."
        scene ch2sc19_93 with dissolve
        el "Nephilim. Right, that’s cheating!"
        el "You can't win like that!"
        scene ch2sc19_94 with dissolve
        $ renpy.pause()
        scene ch2sc19_94_5 with dissolve
        $ renpy.pause(1)
        scene ch2sc19_95 with dissolve
        mc "How's that cheating? I literally just moved my body."
        scene ch2sc19_96 with dissolve
        el "Well, you happen to have a super powerful body."
        el "Capable of who knows what? Unlike someone else. "
        scene ch2sc19_97 with dissolve
        mc "You can’t blame me for being born like this."
        mc "I just gave it all I've got."
        scene ch2sc19_98 with dissolve
        with vpunch
        el "You owe me a massage!"
        scene ch2sc19_99 with dissolve
        mc "Wha-"
        scene ch2sc19_100 with dissolve
        with vpunch
        el "Don’t argue!"
        scene ch2sc19_101 with dissolve
        mc "Fine, I owe you a massage."
        scene ch2sc19_102 with dissolve
        el "Great! Now get your butt in the water!"
        scene ch2sc19_101 with dissolve
        mc "You just want me to test it out."
        scene ch2sc19_103 with dissolve
        $ renpy.pause()
        scene ch2sc19_104 with dissolve
        el "Smart and handsome, why are you single again?"
        scene ch2sc19_105 with dissolve
        mc "Beautiful..."
        scene ch2sc19_106 with dissolve
        mc "Loyal..."
        scene ch2sc19_107 with dissolve
        mc "Intelligent..."
        scene ch2sc19_108 with dissolve
        mc "Remind me, why are you single?"
        scene ch2sc19_109 with dissolve
        $ renpy.pause()
        scene ch2sc19_110 with dissolve
        el "*Whispers* {size=-10}{b}Because you haven’t claimed me yet.{/b}{/size}"
        scene ch2sc19_111 with dissolve
        mc "Okay, time for a swim."
        scene ch2sc19_112 with dissolve
        $ renpy.pause()
        scene ch2sc19_113 with dissolve
        $ renpy.pause()
        scene ch2sc19_114 with dissolve
        $ renpy.pause()
        scene ch2sc19_115 with dissolve
        elt "He has scars all over his body?!"
        scene ch2sc19_116 with dissolve
        elt "[mc]... what happened to you?"
        elt "I’ll have to ask him about them at some point."
        scene ch2sc19_117 with dissolve
        elt "He’s so fit, though. Even with the scars-"
        elt "-I want to trace my fingertips over them and whisper that I’ll take away his pain."
        scene ch2sc19_118 with dissolve
        $ renpy.pause()
        scene ch2sc19_119 with dissolve
        mc "Coming?"
        scene ch2sc19_117 with dissolve
        $ renpy.pause()
        scene ch2sc19_120 with dissolve
        with vpunch
        el "Huhh?!"
        el "{b}OH{/b}. Y-Yeah, in a moment!"
        scene ch2sc19_121 with dissolve
        mc "Suit yourself!"
        scene ch2sc19_122 with dissolve
        $ renpy.pause(0.5)
        mc "I'm eager to see if this lake lives up to the hype, see in you there!"
        scene ch2sc19_123 with dissolve
        $ renpy.pause()
        scene ch2sc19_124 with dissolve
        $ renpy.pause()
        scene ch2sc19_125 with dissolve
        $ renpy.pause()
        scene ch2sc19_126 with dissolve
        $ renpy.pause()
        scene ch2sc19_127 with dissolve
        $ renpy.pause()
        scene black with dissolve
        $ renpy.pause(1)
        scene ch2sc19_128 with dissolve
        mct "Sweet mother mercy!"
        mct "Stay calm... it's just a tiny bit c-cold."
        scene ch2sc19_129 with dissolve
        $ renpy.pause()
        scene ch2sc19_130 with dissolve
        el "So, how is it?"
        scene ch2sc19_131 with dissolve
        mc "Just wonderful! I really needed this."
        scene ch2sc19_132 with dissolve
        el "Say no more! I’ve been dying to get in!"
        scene ch2sc19_133 with dissolve
        el "..."
        scene ch2sc19_134 with dissolve
        el "Well, could you... give a lady some privacy?"
        scene ch2sc19_135 with dissolve
        $ renpy.pause()
        scene ch2sc19_136 with dissolve
        mc "I’d much rather watch."
        scene ch2sc19_137 with dissolve
        with vpunch
        "If looks could kill... you’d already be dead."
        scene ch2sc19_138 with dissolve
        mc "Okay, okay. I won’t look."
        scene ch2sc19_139 with dissolve
        $ renpy.pause()
        scene ch2sc19_140 with dissolve
        el "D-Don’t look! Okay?"
        scene ch2sc19_141 with Dissolve(2)
        $ renpy.pause()
        scene ch2sc19_142 with Dissolve(2)
        $ renpy.pause(2)
        el "It’s not too cold, is it?"
        scene ch2sc19_143 with dissolve
        mc "No it’s just-"
        scene ch2sc19_144 with dissolve
        el "Hey, [mc]..?"
        scene ch2sc19_143 with dissolve
        mc "Something wrong?"
        scene ch2sc19_144 with dissolve
        el "N-No."
        el "Y-You can look now."
        scene ch2sc19_145 with dissolve
        $ renpy.pause(1)
        elt "I'm so nervous!! P-Please like what you see..."
        #scene black with Dissolve(1)
        ########################ANIMATION#########################
        scene eliza_spin with dissolve
        $ renpy.pause(10.6, hard=True)
        #$ renpy.pause()
        scene ch2sc19_147a
        $ renpy.pause(0.5)
        mc "..."
        scene ch2sc19_148 with dissolve
        el "W-Why are you staring at me like that?"
        el "Avert your eyes! *Giggles*"
        scene ch2sc19_147 with dissolve
        el "You're making me feel self-conscious..."
        mc "You told me I could look?"
        el "I suppose I did... didn't I? W-What do you think?"
        scene ch2sc19_148 with dissolve
        $ renpy.pause()
        ####Choice####
        menu:
            "Wars have been started over lesser asses.":
                scene ch2sc19_149 with dissolve
                $ eliza_trust += 2
                mc "I’d go to war for you."
                scene ch2sc19_150 with dissolve
                el "Y-You would? That’s so romantic!"
                "Eliza enjoys your compliment, her trust has increased by {size=+3}{b}{color=#2bff8b}2{/color}{/b}{/size}."
                scene ch2sc19_150 with dissolve
                el "Well, if you’re done drooling, make some room!"


            "Meh, I've seen better.":
                scene ch2sc19_149 with dissolve
                mc "Nothing, I’ve seen better."
                elt "The first time I reveal my self to a man... was this a mistake?"
                elt "No, I'm not gonna let his bad manners ruin my mood!"
                $ eliza_trust -= 2
                "Eliza did not like your bluntness during a moment of vulnerability. Her trust has decreased by {size=+3}{b}{color=#f00}2{/color}{/b}{/size}."
                scene ch2sc19_147 with dissolve
                el "Okay, first of all... rude!"
                scene ch2sc19_151 with dissolve
                el "And secondly... make some room!"

        scene ch2sc19_152 with Dissolve(1.5)
        $ renpy.pause(1)
        el "*Squeals* Aaiiyhh!! Incoming!"
        scene ch2sc19_153 with dissolve
        stop music fadeout 1.0
        $ renpy.pause()
        scene black with Dissolve(2)
        $ renpy.pause(1)
        scene ch2sc19_154 with Dissolve(2)
        play music dark_1 fadein 1.0
        $ renpy.pause()
        scene ch2sc19_155 with dissolve
        $ renpy.pause()
        scene ch2sc19_156 with dissolve
        uk "Still warm... they're close by."
        scene ch2sc19_157 with dissolve
        uk "See you soon, freak."
        stop music fadeout 1.0
        scene black with Dissolve(2)
        $ renpy.pause(1)
        scene ch2sc19_158 with Dissolve(2)
        play music chill_1 fadein 2.0
        $ renpy.pause()
        scene ch2sc19_159 with dissolve
        $ renpy.pause()
        scene ch2sc19_160 with dissolve
        $ renpy.pause()
        scene ch2sc19_161 with dissolve
        with vpunch
        el "{size=+10}{b}Wuuuaahh!{/b}{/size} It’s freezing!!"
        scene ch2sc19_162 with dissolve
        mc "That’s what you get for making me jump in first!"
        scene ch2sc19_163 with dissolve
        $ renpy.pause()
        scene ch2sc19_164 with dissolve
        with vpunch
        el "It’s on!!"
        el "You're going to regret giving me hard nipples!"
        scene ch2sc19_165 with dissolve
        mc "Eyy!"
        mc "*Chuckling* I didn't want to be the only one with hard nipples in this lake!"
        scene ch2sc19_166 with dissolve
        el "[mc]! You're so gonna get it!"
        el "Come here and accept your punishment!"
        scene ch2sc19_167 with dissolve
        mc "As if I’d willingly admit defeat!"
        scene ch2sc19_168 with dissolve
        el "I see..."
        el "That means..."
        scene ch2sc19_169 with dissolve
        el "You’ve chosen death! *Giggling*"
        scene ch2sc19_170 with dissolve
        el "There’s no escaping judgment!"
        el "Come back here!"
        scene ch2sc19_171 with dissolve
        $ renpy.pause()
        scene ch2sc19_172 with dissolve
        $ renpy.pause(0.5)
        el "Accept your fate! *Snickers*"
        scene ch2sc19_173 with dissolve
        $ renpy.pause(0.5)
        mct "She's a good swimmer."
        scene ch2sc19_174 with dissolve
        mct "I think it’s time to turn this chase around."
        scene ch2sc19_175 with dissolve
        with vpunch
        el "What the?!"
        scene ch2sc19_176 with dissolve
        $ renpy.pause(0.5)
        elt "Damnit! I didn't expect him to deep dive..."
        scene ch2sc19_177 with dissolve
        $ renpy.pause(0.5)
        elt "Hnnhh! This won't save him!"
        scene ch2sc19_178 with dissolve
        $ renpy.pause()
        scene ch2sc19_179 with dissolve
        $ renpy.pause()
        scene ch2sc19_180 with dissolve
        $ renpy.pause()
        scene ch2sc19_181 with dissolve
        mct "*Chuckles* Perfect... she's a sitting duck."
        ###Choice###
        menu:
            "Tease her. ({color=#ff8cdd}Romance{/color})":
                scene ch2sc19_182 with Dissolve(2)
                $ renpy.pause(0.5)
                $ eliza_relationship = True
                "You emerge right behind her, holding her closely."
                el "Huh?!"
                scene ch2sc19_183 with dissolve
                mc "*Whisper* {b}{size=-10}Hi... gorgeous.{/b}{/size}"
                elt "G-Gorgeous?"
                scene ch2sc19_184 with dissolve
                el "H-Hi."
                $ eliza_path = True
                scene ch2sc19_185 with dissolve
                elt "Is he going to-"
                scene ch2sc19_186 with dissolve
                el "Mmmhff!"
                scene ch2sc19_187 with dissolve
                elt "His soft lips tracing my wet skin... I-I... Mmhh, don’t stop."
                scene ch2sc19_188 with dissolve
                el "*Soft moan* Mmmhh... [mc]... Mhhff."
                scene ch2sc19_189 with dissolve
                elt "Would it be bad if I asked him to take me right here? In the lake?"
                elt "I’ve never been with a man before, but when I’m with [mc], I can’t stop imagining how it would feel."
                scene ch2sc19_190 with dissolve
                el "*Giggles* You-Your hands, [mc]."
                el "Mmmhmmhh... What are you-"
                scene ch2sc19_191 with dissolve
                $ renpy.pause()
                scene ch2sc19_192 with dissolve
                $ renpy.pause()
                scene ch2sc19_193 with dissolve
                mc "Just preparing."
                scene ch2sc19_194 with dissolve
                el "For wha-"
                scene ch2sc19_195 with dissolve
                mc "This!"
                el "*Gasps* [mc]!"
                scene ch2sc19_196 with dissolve
                with vpunch
                el "{size=+10}{b}Aaiiihhhh!!{/b}{/size}"


            "Throw her. (Neutral)":
                scene ch2sc19_195 with dissolve
                $ renpy.pause()
                scene ch2sc19_196 with dissolve
                with vpunch
                el "{size=+10}{b}Aaiiihhhh!!{/b}{/size}"


        scene ch2sc19_197 with dissolve
        $ renpy.pause(0.5)
        el "Jerk!"
        scene ch2sc19_198 with dissolve
        el "Okay! I had almost forgiven you..."
        el "Now you’re really dead!"
        scene ch2sc19_199 with dissolve
        mc "As if you can catch me."

        if eliza_relationship == True:
            scene ch2sc19_200 with dissolve
            el "You underestimate me."
            scene ch2sc19_201 with dissolve
            $ renpy.pause()
            scene ch2sc19_202 with dissolve
            $ renpy.pause()
            scene ch2sc19_203 with dissolve
            $ renpy.pause()
            scene ch2sc19_204 with dissolve
            $ renpy.pause()
            scene ch2sc19_205 with dissolve
            $ renpy.pause()
            scene ch2sc19_206 with dissolve
            $ renpy.pause()
            scene ch2sc19_207 with dissolve
            $ renpy.pause()
            scene ch2sc19_208 with dissolve
            mct "Does she really think using my own move against-"
            scene ch2sc19_209 with dissolve
            mct "Huh?"
            scene ch2sc19_210 with dissolve
            $ renpy.pause()
            scene ch2sc19_211 with dissolve
            $ renpy.pause()
            scene ch2sc19_212 with dissolve
            $ renpy.pause()
            scene ch2sc19_213 with dissolve
            $ renpy.pause()
            scene ch2sc19_214 with dissolve
            $ renpy.pause()
            scene ch2sc19_215 with dissolve
            mct "Mmmhh... Eliza."
            mct "*Chuckles* You little predator."
            scene ch2sc19_214 with dissolve
            "She continues to explore you with her wet lips and soft hands for a little longer before she has to surface."
            scene ch2sc19_216 with dissolve
            elt "Mhhh! I hope he enjoyed this as much as I did."
            scene ch2sc19_217 with dissolve
            "As she surfaces for air, she wraps her arms around your neck, pressing her naked body against yours."
            scene ch2sc19_218 with dissolve
            el "Enjoy my little surprise attack?"
            scene ch2sc19_219 with dissolve
            mc "Attack, attack!"
            scene ch2sc19_220 with dissolve
            "She pushes her wet slender body against yours."
            "The sensation of her wet skin rubbing against you sends warmth through your body despite the cool water."
            "Her squishy breasts firmly meld into your chest."
            scene ch2sc19_218 with dissolve
            el "Surrender?"
            scene ch2sc19_219 with dissolve
            mc "I’m at your mercy."
            scene ch2sc19_221 with dissolve
            elt "This should teach him who’s the captain of this lake."
            scene ch2sc19_222 with dissolve
            $ renpy.pause(1)
            el "Mmmh... nnhh... *Mwah*"
            mct "Mmh... fuck... I love her soft lips, she's such an intimate kisser."
            scene ch2sc19_223 with dissolve
            "You hear soft moans from Eliza as she presses her breasts into your face."
            "Her hands pulling on the back of your neck, squeezing you firmly as you kiss her supple breasts."
            elt "*Soft moans* Nnnhh... Mmh... N-No, focus! This is my chance."
            scene ch2sc19_224 with dissolve
            with vpunch
            "With one swift motion she jumps up and pushes you under."
            scene ch2sc19_225 with dissolve
            el "Ha! Got you! I told you not to underestimate me!"
            scene ch2sc19_226 with dissolve
            "..."
            "{b}......{/b}"
            "{size=+20}{b}..........{/b}{/size}"
            elt "Huh... He’s not coming up?"
            scene ch2sc19_226 with dissolve
            elt "Fuck, did I hurt him? Maybe he swallowed water in surprise?!"
            scene ch2sc19_228 with dissolve
            with vpunch
            el "*Worried* {b}[mc]!{/b}"
            scene ch2sc19_229 with dissolve
            with vpunch
            el "W-Where are you?! {b}[mc]!{/b}"
            scene ch2sc19_230 with dissolve
            $ renpy.pause(1)
            el "{b}[mc]!{/b} Are you okay?"
            scene ch2sc19_231 with dissolve
            $ renpy.pause(0.3)
            with vpunch
            mc "Hi, you called?"
            scene ch2sc19_232 with dissolve
            el "Wha- Jerk!"
            el "I thought maybe you were hurt! What if you had drowned!"
            scene ch2sc19_233 with dissolve
            mc "You thought pushing me underwater would harm me?"
            mc "*Chuckles* Cute."
            scene ch2sc19_234 with dissolve
            $ renpy.pause(0.5)
            el "Hnnh..."
            scene ch2sc19_235 with dissolve
            el "Uhh... When you say it like that, it sounds silly."
            scene ch2sc19_233 with dissolve
            mc "'Cause it is silly."
            scene ch2sc19_232 with dissolve
            el "Ass!"
            el "I was worried about you, you know?"
            scene ch2sc19_233 with dissolve
            mc "I’m just teasing you, kitten."
            scene ch2sc19_234 with dissolve
            $ renpy.pause()
            scene ch2sc19_235 with dissolve
            el "Kit-Kitten? W-Why do you keep calling me that? *Blush*"
            scene ch2sc19_236 with dissolve
            mc "I like how your cheeks turn red when I call you that."
            scene ch2sc19_237 with dissolve
            el "T-They don’t! I don't blush!"
            el "Certainly not because of you calling me something so silly!"
            scene ch2sc19_238 with dissolve
            mc "Okay, okay. Noted, I won’t do it again."
            scene ch2sc19_239 with dissolve
            el "I didn’t say that."
            scene ch2sc19_240 with dissolve
            el "I’m okay with it... I like it... I was just frustrated by your teasing..."
            el "Bu-But only when we’re alone! It'd be embarrassing if anyone heard you call me... Kitten."
            scene ch2sc19_238 with dissolve
            mc "We are alone."
            scene ch2sc19_241 with dissolve
            el "Right... Right, right, right!"
            scene ch2sc19_242 with dissolve
            el "Are you wrinkly? I’m wrinkly! Let’s head back to camp!"
            scene ch2sc19_243 with dissolve
            mc "As you wish... kitten."
            scene ch2sc19_244 with dissolve
            $ renpy.pause(1)
            el "!!"
            scene ch2sc19_245 with dissolve
            $ renpy.pause(1)
            elt "I guess I am blushing..."
            elt "*Giggles softly* ..."
            stop music fadeout 1.0

            scene ch2sc19_246 with Dissolve(2)
            play music dark_1 fadein 1.0
            $ renpy.pause()
            scene ch2sc19_247 with dissolve
            $ renpy.pause()
            scene ch2sc19_248 with dissolve
            uk "Aqua briinah dii du’ul activol."
            scene ch2sc19_249 with dissolve
            with vpunch
            $ renpy.pause()
            scene ch2sc19_250 with dissolve
            $ renpy.pause()
            scene ch2sc19_251 with dissolve
            $ renpy.pause()
            scene black with dissolve
            scene ch2sc19_252 with dissolve
            mc "Eliza, get out of the water and hide."
            mc "Do it now, and quickly!"
            scene ch2sc19_253 with dissolve
            "Eliza can tell by the changed tone in your voice and the stiffness of your body that you aren’t messing around anymore."
            scene ch2sc19_254 with dissolve
            elt "Dammit! Every fiber of my body tells me to stay and help with whatever happens."
            scene ch2sc19_255 with dissolve
            with vpunch
            elt "I’ve gotta hide fast. He wouldn’t be this serious about it, otherwise."
            scene ch2sc19_256 with dissolve
            "Eliza rushes to grab her clothes and hides behind a nearby rock, her eyes scanning the rocky terrain for movement."
            scene ch2sc19_257 with dissolve
            $ renpy.pause(1)
            scene ch2sc19_256 with dissolve
            $ renpy.pause(1)
            scene ch2sc19_257 with dissolve
            $ renpy.pause(1)
            scene ch2sc19_256 with dissolve
            $ renpy.pause(1)
            scene black with Dissolve(3)
            stop music fadeout 2.0
            $ renpy.pause(1)


        else:
            scene black with Dissolve(3)
            $ renpy.pause(1)
            stop music fadeout 2.0
            "You and Eliza mess around in the lake for about an hour, before you agree to head back to camp and prepare a meal."
        jump ch2sc19_nz
