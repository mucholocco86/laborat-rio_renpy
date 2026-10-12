label ch3sc22:

    window hide dissolve
    play music home_2 fadein 1.0
    scene black with Dissolve (1.0)
    $ renpy.pause(1)
    scene ch3sc22_001 with Dissolve(2.0)
    $ renpy.pause(1.5)
    scene ch3sc22_002 with dissolve
    $ renpy.pause()
    scene ch3sc22_003 with dissolve
    $ renpy.pause(1.5)
    scene ch3sc22_004 with dissolve
    mc "*Whispers* {size=-6}{b}Stop.{/b}{/size}"
    scene ch3sc22_005 with dissolve
    mc "*Whispers* {size=-6}{b}This is it.{/b}{/size}"
    mc "*Whispers* {size=-6}{b}Stay alert, Eliza. Remember, don’t engage until I’ve created an opening for you.{/b}{/size}"
    mc "*Whispers* {size=-6}{b}I’m serious. I know you get impatient when I ask you to stay behind.{/b}{/size}"
    scene ch3sc22_006 with dissolve
    el "*Whispers* {size=-6}{b}I’ll be patient."
    el "*Whispers* {size=-6}{b}But if they hurt you..."
    scene ch3sc22_007 with dissolve
    $ renpy.pause()
    scene ch3sc22_008 with dissolve
    mc "Even if I get hurt, you need to wait."
    mc "It's important. We don’t know how many there are."
    scene ch3sc22_009 with dissolve
    el "Fine, fine!"
    el "I’ll stay back until you give the signal."
    scene ch3sc22_010 with dissolve
    el "For the record, I don’t like it one bit... I should be going with you."
    scene ch3sc22_011 with dissolve
    mc "I know, but I’m counting on you."
    mc "Remember, watch for my signal. Here I go!"
    scene ch3sc22_012 with dissolve
    elt "I won’t fail you, [mc]."
    scene ch3sc22_013 with dissolve
    $ renpy.pause()
    scene ch3sc22_014 with dissolve
    $ renpy.pause()
    scene ch3sc22_015 with dissolve
    $ renpy.pause()
    scene ch3sc22_016 with dissolve
    $ renpy.pause()
    scene ch3sc22_017 with dissolve
    mct "Hmm, there’s not as many as I'd expected. Better stay on guard, though."
    scene ch3sc22_172 with dissolve
    syt "..."
    scene ch3sc22_173 with dissolve
    syt "This should be interesting. Let’s see how he chooses to approach this..."
    stop music fadeout 2.0
    scene ch3sc22_017 with dissolve
    play music darknight_4 fadein 1.0
    mct "I’ll take out the one who’s eating first."
    ###Choice###
    menu:
        "Stealthy approach. ({color=#745099}Stealth{/color})":
            scene ch3sc22_017 with dissolve
            mct "I’ll handle this quietly, just like Rin taught me."
            scene ch3sc22_018 with dissolve
            $ renpy.pause()
            $ stealth += 1
            scene ch3sc22_019 with dissolve
            $ renpy.pause()
            scene ch3sc22_020 with dissolve
            $ renpy.pause(1)
            mct "Perfect, his neck is wide open for a stranglehold."
            scene ch3sc22_021 with dissolve
            with vpunch
            $ renpy.pause(1)
            mct "Their necks are a lot tougher than human necks. But with enough pressure..."
            scene ch3sc22_022 with dissolve
            with vpunch
            "*Bones cracking*"
            $ renpy.pause(1)
            mct "One down."
            scene ch3sc22_023 with dissolve
            mct "One to go."
            scene ch3sc22_024 with dissolve
            $ renpy.pause(1)
            "You land carefully in the tall grass, making sure to stay light on your feet to not alarm the goblin."
            scene ch3sc22_025 with dissolve
            $ renpy.pause()
            scene ch3sc22_026 with dissolve
            $ renpy.pause(0.5)
            "You manage to grab the goblin's head and lock it in, rapidly applying pressure."
            scene ch3sc22_027 with dissolve
            with vpunch
            "*Neck snaps*"
            "You've successfully taken out the goblins without being noticed, {b}{color=#745099}Stealth{/color}{/b} has increased by {size=+3}{b}{color=#2bff8b}1{/color}{/b}{/size}."
            $ renpy.pause()

        "I’ll kill them fast and efficiently. ({color=#ff8400}Strength{/color})":
            scene ch3sc22_017 with dissolve
            mct "I’ll kill them fast and efficiently."
            scene ch3sc22_018 with dissolve
            $ renpy.pause()
            scene ch3sc22_028 with dissolve
            $ renpy.pause()
            scene ch3sc22_029 with dissolve
            $ renpy.pause()
            scene ch3sc22_030 with dissolve
            with vpunch
            gob "Rrrrhhghgh!"
            scene ch3sc22_031 with dissolve
            $ renpy.pause()
            scene ch3sc22_032 with dissolve
            $ strength += 1
            gob "*Screams* Ghrraah! Intrudrrr! Ghrrr! Fresh meat!"
            scene ch3sc22_033 with dissolve
            with vpunch
            "You've successfully taken out the goblins with brute force, {b}{color=#ff8400}Strength{/color}{/b} has increased by {size=+3}{b}{color=#2bff8b}1{/color}{/b}{/size}."
            $ renpy.pause()

    scene ch3sc22_034 with dissolve
    mct "Well that was easy..."
    mct "Does two goblins really qualify as a C-Rank contract?"
    scene ch3sc22_035 with dissolve
    mct "{b}Hmm? OH!{/b}"
    scene ch3sc22_036 with dissolve
    with vpunch
    mct "That was close. I knew it seemed too easy."
    scene ch3sc22_037 with dissolve
    mct "Blazes this guy is huge! I've never seen a goblin like this."
    mct "Let’s see how he handles a punch."
    scene ch3sc22_038 with dissolve
    mct "Time for a nap, buddy."
    scene ch3sc22_039 with dissolve
    with vpunch
    $ renpy.pause()
    scene ch3sc22_040 with dissolve
    $ renpy.pause(1)
    scene ch3sc22_041 with dissolve
    $ renpy.pause(1)
    scene ch3sc22_040 with dissolve
    $ renpy.pause(1)
    scene ch3sc22_042 with dissolve
    with vpunch
    $ renpy.pause(1)
    bz "{b}RrrhoarhhH!{/b}"
    scene ch3sc22_043 with dissolve
    mct "Fuck, he’s faster than I expected! I just barely managed to dodge that swing."
    mct "He didn't even flinch at my punch directly to his abdomen?"
    scene ch3sc22_044 with dissolve
    $ renpy.pause()
    scene ch3sc22_045 with dissolve
    with vpunch
    $ renpy.pause()
    scene ch3sc22_046 with dissolve
    with vpunch
    $ renpy.pause(0.5)
    bz "{b}RrrhhhH!{/b}"
    scene ch3sc22_047 with dissolve
    mct "Huh?! A solid kick to the skull and he didn’t even flinch?"
    ###Choice###
    menu:
        "Taunt him.":
            scene ch3sc22_047 with dissolve
            mct "I've been meaning to get a workout in. This should do the trick..."
            scene ch3sc22_048 with dissolve
            mc "Blazes, you’re one ugly fucker."
            mc "Did you get your looks from your mother or your father? I'm guessing both."
            scene ch3sc22_049 with dissolve
            $ renpy.pause(1)
            bz "Hrrh?"
            scene ch3sc22_050 with dissolve
            with vpunch
            bz "{b}RrrhhhH!{/b}"

        "Try to calm him.":
            scene ch3sc22_047 with dissolve
            mct "*Sigh* I really don't feel like going all out just for a goblin..."
            mct "Perhaps I can convince him to leave the area. Here goes..."
            scene ch3sc22_048 with dissolve
            mc "Hey... Buddy. You setting up camp this close to the capital is causing problems."
            mc "If you leave the area and return to the deep woods, I won't have to kill you."
            mc "Which would save us both a lot of energy. What do you say?"
            scene ch3sc22_049 with dissolve
            $ renpy.pause(1)
            bz "Hrrh?"
            scene ch3sc22_050 with dissolve
            with vpunch
            bz "{b}RrrhhhH!{/b}"

    scene ch3sc22_047 with dissolve
    $ renpy.pause(1)
    "The two of you size each other up and then you both-"
    scene ch3sc22_051 with dissolve
    with vpunch
    "Burst ahead, charging towards one another."
    scene ch3sc22_052 with dissolve
    $ renpy.pause()
    scene ch3sc22_053 with dissolve
    with vpunch
    $ renpy.pause()
    scene ch3sc22_054 with dissolve
    with vpunch
    $ renpy.pause()
    scene ch3sc22_055 with dissolve
    elt "Hrrrhrr... I can’t believe I have to sit back and let him fight on his own."
    elt "He took out those first two goblins with ease. This one is different, though."
    scene ch3sc22_056 with dissolve
    elt "It's way bigger than the other ones, and it doesn’t seem fazed by any of [mc]’s attacks..."
    elt "I know he told me to wait until he gives me a signal, but it feels wrong just sitting here watching..."
    scene ch3sc22_057 with dissolve
    elt "Huh? There’s more of them!"
    scene ch3sc22_058 with dissolve
    $ renpy.pause()
    scene ch3sc22_059 with dissolve
    elt "They're surrounding him! This is my chance. I won’t let them ambush him!"
    elt "He's already fully occupied by the big one!"
    scene ch3sc22_060 with dissolve
    elt "I have to help him!"
    elt "We're a team."
    scene ch3sc22_054 with dissolve
    with vpunch
    $ renpy.pause()
    scene ch3sc22_061 with dissolve
    mct "It seems his head is his most vulnerable spot."
    mct "Let's finish this!"
    scene ch3sc22_062 with dissolve
    mct "I'll infuse my fist with wind energy, like Rin taught me. Even his hardened skin won't resist that."
    scene ch3sc22_063 with dissolve
    $ renpy.pause()
    scene ch3sc22_064 with dissolve
    $ renpy.pause()
    scene ch3sc22_065 with dissolve
    $ renpy.pause(1)
    "You infuse your fist with potent wind energy, enough to send several grown men flying."
    scene ch3sc22_066 with dissolve
    $ renpy.pause()
    scene ch3sc22_067 with dissolve
    with vpunch
    $ renpy.pause()
    scene ch3sc22_068 with dissolve
    mct "{b}FUCK!!{/b} I can’t defend from this angle."
    scene ch3sc22_069 with dissolve
    with vpunch
    $ renpy.pause(0.3)
    mc "*Groans in pain* Hnnrrrh! Fuck!"
    scene ch3sc22_070 with dissolve
    $ renpy.pause(0.3)
    "The berzerkers punch knocks the wind out of you and sends you flying."
    scene ch3sc22_071 with dissolve
    mc "*Groan* Urrhh. That ugly cowfucker has one hell of a punch."
    scene ch3sc22_072 with dissolve
    $ renpy.pause()
    scene ch3sc22_073 with dissolve
    mc "Huh?"
    scene ch3sc22_074 with dissolve
    mc "Great. Even more of them. *Sigh*"
    scene ch3sc22_073 with dissolve
    mc "I was hoping it would’ve just been a few of em, quick and easy."
    scene ch3sc22_075 with dissolve
    mct "Looks like I’ll have to get serious, especially with the big one."
    mct "My hand-to-hand attacks doesn’t seem to faze him at all. He even feigned an injury to get the upper hand."
    scene ch3sc22_076 with dissolve
    mct "I. Fucking. Hate. Goblins."
    scene ch3sc22_077 with dissolve
    $ renpy.pause()
    scene ch3sc22_078 with dissolve
    mct "Huh? Really?"
    scene ch3sc22_079 with dissolve
    gob "Rharrrhgrhh!"
    scene black with dissolve
    $ renpy.pause(0.5)
    scene cut1
    with vpunch
    $ renpy.pause(0.5)
    scene cut2
    with vpunch
    $ renpy.pause(0.5)
    scene black with dissolve
    $ renpy.pause(0.5)
    scene ch3sc22_080 with dissolve
    $ renpy.pause(0.5)
    "Appearing seemingly out of nowhere, Eliza managed to slice & dice the goblin mid-air."
    scene ch3sc22_081 with dissolve
    mc "Thanks."
    scene ch3sc22_082 with dissolve
    el "Don’t thank me just yet."
    el "There’s still plenty more of them left!"
    scene ch3sc22_083 with dissolve
    mct "*Chuckles* I knew she wouldn’t listen..."
    mct "She really can’t stand me being in danger."
    scene ch3sc22_084 with dissolve
    el "How about a little wager?"
    scene ch3sc22_085 with dissolve
    mc "This is hardly the time..."
    scene ch3sc22_084 with dissolve
    el "What are you talking about? It’s the perfect time!"
    scene ch3sc22_085 with dissolve
    mc "*Sigh* What wager do you have in mind?"
    scene ch3sc22_084 with dissolve
    el "It’s simple, really."
    scene ch3sc22_086 with dissolve
    el "Whoever kills the most goblins wins a massage!"
    el "So, you game?"
    scene ch3sc22_087 with dissolve
    mc "Am I game? You won’t stand a chance... I've been slaying goblins since I was fourteen."
    scene ch3sc22_088 with dissolve
    with vpunch
    el "*Shouts* Game on!"
    scene ch3sc22_089 with dissolve
    $ renpy.pause()
    scene ch3sc22_090 with dissolve
    with vpunch
    $ renpy.pause(0.5)
    elt "Take that you ugly beast!"
    scene ch3sc22_091 with dissolve
    with vpunch
    $ renpy.pause(0.5)
    elt "Damn, this feels good!"
    scene ch3sc22_092 with dissolve
    elt "Heh! Easy! I'm so winning that massage!"
    scene ch3sc22_093 with dissolve
    elt "{b}OH SHI-{/b}"
    scene ch3sc22_094 with dissolve
    with vpunch
    el "*Groans* Ahrrh!"
    scene ch3sc22_095 with dissolve
    $ renpy.pause(0.5)
    mc "Damn you're ugly..."
    scene ch3sc22_096 with dissolve
    mc "{b}Eliza!!{/b}"
    scene ch3sc22_094 with dissolve
    el "Hrrnnhgg!"
    scene ch3sc22_097 with dissolve
    with vpunch
    $ renpy.pause(0.5)
    "The gust of wind is too powerful for Eliza, resulting in her losing her footing."
    scene ch3sc22_096 with dissolve
    mc "Fuck, hold on!"
    scene ch3sc22_095 with dissolve
    mc "Play time is over."
    scene ch3sc22_098 with dissolve
    with vpunch
    $ renpy.pause(0.5)
    "You swiftly finish off the goblin by crushing every bone within it's torso by using your wind-infusion."
    scene ch3sc22_099 with dissolve
    $ renpy.pause()
    stop music fadeout 2.0
    scene ch3sc22_100 with dissolve
    with vpunch
    $ renpy.pause()
    play music explore_1 fadein 1.0
    scene ch3sc22_101 with dissolve
    $ renpy.pause()
    scene ch3sc22_102 with dissolve
    el "*Groans* Owwh. It-It hurts, [mc]."
    scene ch3sc22_103 with dissolve
    el "I ... I’m sorry."
    el "I should have paid better attention."
    scene ch3sc22_101 with dissolve
    ###Choice###
    menu:
        "Reassure her.":
            scene ch3sc22_104 with dissolve
            mc "Hey... None of that, okay?"
            mc "You just took a direct hit from a storm spell."
            scene ch3sc22_105 with dissolve
            mc "Not to mention, you just killed two goblins without breaking a sweat."
            mc "I’m proud of you for doing so well."
            scene ch3sc22_106 with dissolve
            $ renpy.pause(1)
            "Eliza's face brightens up upon hearing you praise her."
            scene ch3sc22_108 with dissolve
            el "Y-You really mean that?"
            scene ch3sc22_105 with dissolve
            mc "I wouldn’t have said it otherwise."
            scene ch3sc22_106 with dissolve
            $ renpy.pause()
            scene ch3sc22_108 with dissolve
            el "Thank you... [mc], I-"
            scene ch3sc22_107 with dissolve
            mc "Let me take care of the rest yeah? I’m going to put you on top of these ruins."
            scene ch3sc22_108 with dissolve
            el "O-Okay, but before you do..."
            scene ch3sc22_106 with dissolve
            $ renpy.pause(1)
            scene ch3sc22_109 with dissolve
            $ renpy.pause(1)
            "Eliza leans in for a kiss, just as you feel her warmth breath on your lips-"
            stop music fadeout 2.0
            scene ch3sc22_110 with dissolve
            with vpunch
            gob "Rhrraahrarh!"
            play music battle_3 fadein 1.0
            if eye_beam == True:
                scene ch3sc22_111 with dissolve
                $ renpy.pause(1)
                elt "Fucker! We almost kissed! *Growls in anger* Hrrrghh!"
                scene ch3sc22_112 with dissolve
                $ renpy.pause(1)
                mct "I've had it! They wanted to fuck around... now they're gonna find out!"
                scene ch3sc22_113 with dissolve
                with vpunch
                $ renpy.pause(1)
                "You shoot two high-intensity energy beams from your eyes, instantly killing the goblin who harmed Eliza."
                scene ch3sc22_113_b with dissolve
                syt "{b}Woah!!{/b} By the Earth-mother! I’ve never seen anything like that!"
                syt "He's able to shoot energy beams directly from his eyes?! W-What sort of magic is this?!"
            else:
                scene ch3sc22_114 with dissolve
                $ renpy.pause(1)
                "You've had it with these goblins, you activate your Mana-manipulation and shoot forth an energy projectile of raw mana."
                scene ch3sc22_115 with dissolve
                with vpunch
                $ renpy.pause(1)
                "As the projectile of mana connects with the goblin, it violently begins tearing the creature apart."
                scene ch3sc22_113_b with dissolve
                syt "He’s manipulating energy and using it offensively! But he’s not even a mage!"
                syt "I've never seen mana used in it's raw form before! He's... incredible!"

        "Be cross with her":
            scene ch3sc22_104 with dissolve
            mc "I was reckless to let you fight so soon. You’re not ready."
            scene ch3sc22_103 with dissolve
            stop music fadeout 2.0
            el "S-Sorry..."

    scene ch3sc22_116 with dissolve
    play music battle_3 fadein 1.0
    mc "Sit tight, I’ll be back before you know it."
    scene ch3sc22_117 with dissolve
    el "I suppose it'd be pointless to ask you to be careful?"
    el "So instead, just make sure you kick their butts!"
    scene ch3sc22_116 with dissolve
    mc "Heh. You know I will. See you soon."
    scene ch3sc22_118 with dissolve
    $ renpy.pause(1)
    gob "Rhrraahrarh!"
    scene ch3sc22_119 with dissolve
    $ renpy.pause(1)
    mc "Let's show these guys what happens when they fuck with us... be right back."
    scene ch3sc22_120 with dissolve
    with vpunch
    $ renpy.pause(0.5)
    "You launch yourself off the wall at full speed."
    scene ch3sc22_121 with dissolve
    $ renpy.pause(0.5)
    "As you charge the goblins, you gather wind energy, this time creating a pointed sleeve of violent wind."
    scene ch3sc22_122 with dissolve
    with vpunch
    $ renpy.pause(0.5)
    "The wind easily cuts through the hardened skin of the goblins."
    scene ch3sc22_123 with dissolve
    $ renpy.pause(0.5)
    scene ch3sc22_124 with dissolve
    with vpunch
    $ renpy.pause(0.5)
    with vpunch
    $ renpy.pause()
    scene ch3sc22_125 with dissolve
    mct "Time for the big guy."
    scene ch3sc22_113_b with dissolve
    syt "He’s able to use wind magic too?! Not only that... He’s shaping it, controlling it, even!"
    syt "But that takes years... even decades of practice for most mages to learn!"
    scene ch3sc22_125 with dissolve
    $ renpy.pause()
    scene ch3sc22_126 with dissolve
    $ renpy.pause()
    scene ch3sc22_127 with dissolve
    $ renpy.pause(0.5)
    bz "RrhrrhH!! Hooman!! {b}DIE!!!{/b}"
    scene ch3sc22_128 with dissolve
    $ renpy.pause(0.5)
    "The berzerker charges you head-on, you don't have time to line up a fully-powered attack."
    scene ch3sc22_129 with dissolve
    with vpunch
    $ renpy.pause(0.5)
    "You pertrude an energy barrier made of wind and mana to shield yourself from the berzerkers powerful attack."
    scene ch3sc22_130 with dissolve
    $ renpy.pause(0.5)
    scene ch3sc22_131 with dissolve
    with vpunch
    $ renpy.pause(0.5)
    scene ch3sc22_132 with dissolve
    $ renpy.pause(0.5)
    scene ch3sc22_131 with dissolve
    with vpunch
    $ renpy.pause(0.5)
    scene ch3sc22_132 with dissolve
    $ renpy.pause(0.5)
    scene ch3sc22_133 with dissolve
    mct "Now’s my chance!"
    scene ch3sc22_134 with dissolve
    with vpunch
    $ renpy.pause(0.3)
    "As the berzerker leaned back to land another blow, you swiftly kick yourself upwards, connecting your heel with his jaw."
    scene ch3sc22_135 with dissolve
    el "Yes!! Take that!"
    el "Show that big beefcake who's the boss!"
    scene ch3sc22_134_b with dissolve
    syt "Good work, [mc]! You're incredible! Magical mastery way beyond your young age and..."
    syt "Physical strength to match a goblin berzerker?"
    syt "I think I’ve seen enough... better report back to Dalen."
    scene ch3sc22_136 with dissolve
    mct "Time to join your ugly friends, you fat bastard."
    scene ch3sc22_137 with dissolve
    mct "*Squeezing tighter* Fucking die already!!!"
    with vpunch
    $ renpy.pause(0.5)
    with vpunch
    mc "Hnngh! C'mon!"
    scene ch3sc22_138 with dissolve
    mct "Are you serious?"
    scene ch3sc22_139 with dissolve
    $ renpy.pause()
    scene ch3sc22_140 with dissolve
    $ renpy.pause()
    scene ch3sc22_141 with dissolve
    with vpunch
    $ renpy.pause()
    scene ch3sc22_142 with dissolve
    mct "His resistance to physical attacks is unlike anything I’ve encountered before."
    mct "Looks like I’ll have to use my abilities again."
    mct "I was hoping to avoid doing that so soon. I still feel weak after using them earlier."
    scene ch3sc22_143 with dissolve
    mct "There’s no use crying about it, I have to kill this abomination sooner rather than later."

    if eye_beam == True:
        scene ch3sc22_144 with dissolve
        $ renpy.pause()
        scene ch3sc22_145 with dissolve
        with vpunch
        $ renpy.pause()
        scene ch3sc22_146 with dissolve
        with vpunch
        $ renpy.pause(1)
        "The berzerker just barely managed to escape a direct hit by your eye-beams."
        bz "RhhrhH! Hooman die! Die now!"
        scene ch3sc22_147 with dissolve
        with vpunch
        $ renpy.pause(0.5)
        "You manage to leap out of the way in the last second."
        scene ch3sc22_148 with dissolve
        $ renpy.pause()
        scene ch3sc22_149 with dissolve
        mct "Got you!"
        scene ch3sc22_150 with dissolve
        with vpunch
        bz "*Roars* Ghraahrhr!"
        "Your eye-beams pierce the berzerkers thigh, rendering his leg useless."
        scene ch3sc22_151 with dissolve
        mc "What’s wrong big guy? Leg not feeling well?"
        scene ch3sc22_152 with dissolve
        with vpunch
        bz "Rhooarrhrhg!"
        scene ch3sc22_153 with dissolve
        $ renpy.pause()
        scene ch3sc22_154 with dissolve
        with vpunch
        $ renpy.pause()
        scene ch3sc22_155 with dissolve
        mc "This is the end for you."
        mc "Don’t worry, I’ll put your soul to good use."
        scene ch3sc22_156 with dissolve
        with vpunch
        $ renpy.pause(0.5)
        bz "*Groans in pain* HhrrhH!"
        scene ch3sc22_157 with dissolve
        with vpunch
        $ renpy.pause(0.5)
        bz "Roohhhrh... hhh..."
        scene ch3sc22_158 with dissolve
        with vpunch
        $ renpy.pause(0.5)
        bz "*Death cry* Hhrh! Hhrrhhh! Hhrh! Hh-... h..."
        scene ch3sc22_171 with dissolve
        "You don't waste any time, as soon as the berzerker drew it's last breaths, you begin absorbing his soul."
        mct "His essence is filled with energy. I don't even feel exhausted anymore."
        stop music fadeout 2.0


    else:
        scene ch3sc22_142 with dissolve
        "You feel a large gathering of energy assemble in your fists."
        scene ch3sc22_153 with dissolve
        with vpunch
        $ renpy.pause()
        scene ch3sc22_159 with dissolve
        mct "He’s all beefed up, if I use my mana manipulation to electrify him, all his muscles will be a disadvantage for him."
        scene ch3sc22_160 with dissolve
        mct "Here he comes..."
        scene ch3sc22_161 with dissolve
        $ renpy.pause()
        scene ch3sc22_162 with dissolve
        $ renpy.pause()
        scene ch3sc22_163 with dissolve
        mct "Dodging now, are we?"
        mct "Dodge this!"
        scene ch3sc22_164 with dissolve
        with vpunch
        $ renpy.pause(1.5)
        scene ch3sc22_165 with dissolve
        $ renpy.pause(1.5)
        scene ch3sc22_166 with dissolve
        $ renpy.pause(1.5)
        scene ch3sc22_167 with dissolve
        $ renpy.pause()
        scene ch3sc22_163 with dissolve
        $ renpy.pause(1)
        scene ch3sc22_164 with dissolve
        $ renpy.pause(1)
        scene ch3sc22_165 with dissolve
        $ renpy.pause(1)
        scene ch3sc22_166 with dissolve
        $ renpy.pause(1)
        scene ch3sc22_168 with dissolve
        $ renpy.pause()
        scene ch3sc22_169 with dissolve
        with vpunch
        bz "*Painful groan* Rharhhgrh!"
        scene ch3sc22_170 with dissolve
        "You don't waste any time, as soon as the berzerker drew it's last breaths, you begin absorbing his soul."
        mct "Your essence will be put to good use."
        stop music fadeout 2.0


    scene black with Dissolve(1.5)
    scene abilityunlock_resistance with Dissolve(1.5)
    $ renpy.pause()
    scene black with Dissolve(1.5)
    $ renpy.pause(1)
    scene ch3sc22_135 with Dissolve(1.5)
    play music forest_1 fadein 1.0
    $ renpy.pause(0.5)
    el "{b}Catch!!{/b}"
    scene ch3sc22_100 with dissolve
    with vpunch
    el "I knew you would catch me."
    scene ch3sc22_107 with dissolve
    mc "Always."
    scene ch3sc22_108 with dissolve
    el "We did it. We completed our first C-Rank Quest!"
    scene ch3sc22_109 with dissolve
    "She’s brimming with excitement as she leans closer to you..."
    ###Choice###
    menu:
        "Kiss her. ({color=#ff8cdd}Romance{/color})":
            scene ch3sc22_174 with dissolve
            el "Mmhm..."
            mct "Her lips are as soft as I remember, her scent is conquering my senses with every breath."
            scene ch3sc22_175 with dissolve
            mct "I can feel how much she cares about me with each and every one of her kisses."
            mct "Each one is filled with emotion, tenderness and passion."
            $ eliza_relationship = True
            scene ch3sc22_109 with dissolve
            $ renpy.pause()
            scene ch3sc22_106 with dissolve
            $ renpy.pause()
            scene ch3sc22_108 with dissolve
            $ eliza_path = True
            el "Just like that, the pain is gone."
            scene ch3sc22_107 with dissolve
            mc "I’m happy to be your medic anytime, m'lady."
            scene ch3sc22_174 with dissolve
            $ renpy.pause(1)
            el "*Mwaaah!* Nnhh..."
            scene ch3sc22_106 with dissolve
            $ renpy.pause(0.5)
            el "*Giggling* Mmh!"
            scene ch3sc22_107 with dissolve
            mc "Needed more healing?"
            scene ch3sc22_106 with dissolve
            $ renpy.pause(1)
            scene ch3sc22_108 with dissolve
            el "Something like that..."
            $ eliza_kiss = True
            scene ch3sc22_106 with dissolve
            $ renpy.pause()
            "Eliza feels closer to you than ever before, her trust has increased by {size=+3}{b}{color=#2bff8b}3{/color}{/b}{/size}."
            $ eliza_trust += 3
            scene ch3sc22_108 with dissolve
            el "Should we take a look around these ruins to see if we can find anything worthwhile?"
            scene ch3sc22_107 with dissolve
            mc "Sure. Sylph did mention the Guild could use... well, pretty much anything to decorate the Guild Hall with."

        "Don’t.":
            scene ch3sc22_107 with dissolve
            mc "Let’s take a look around and see if we can find anything of note to bring back to the Guild."
            scene ch3sc22_108 with dissolve
            el "Sure!"


    scene black with Dissolve(1.5)
    "The two of you begin searching the ruins for anything of interest."
    scene ch3sc22_176 with Dissolve(1.5)
    mc "Found something?"
    el "Y-Yeah there’s something lodged here between these rocks"
    el "I think I got it!"
    scene ch3sc22_177 with dissolve
    el "What do you suppose it is?"
    scene ch3sc22_178 with dissolve
    mc "I’m not sure what it’s doing out here, but that’s definitely the sigil of the Kingsguard."
    scene ch3sc22_177 with dissolve
    el "Perhaps the goblins attacked an envoy from the guards at some point?"
    scene ch3sc22_178 with dissolve
    mc "Maybe so. We should definitely take it back to Sylph."
    scene ch3sc22_179 with dissolve
    el "Alright! Kingsguard sigil... neat!"
    el "Let’s see if we can find anything else!"
    scene ch3sc22_180 with dissolve
    elt "Hmm..."
    elt "There’s got to be more interesting stuff laying around these ruins!"
    scene ch3sc22_181 with dissolve
    $ renpy.pause()
    scene ch3sc22_182 with dissolve
    elt "My, my. What do we have here?"
    scene ch3sc22_183 with dissolve
    el "[mc]! Check this out!"
    scene ch3sc22_184 with dissolve
    el "Are you seeing this?"
    scene ch3sc22_185 with dissolve
    mc "Mhm. I’m definitely seeing it."
    scene ch3sc22_186 with dissolve
    el "I think it could be worth a lot!"
    scene ch3sc22_187 with dissolve
    mc "Oh, it’s worth a lot. Trust me."
    scene ch3sc22_186 with dissolve
    el "How do you know? Ever seen anything like it?"
    scene ch3sc22_187 with dissolve
    mc "Nothing that rivals it, no..."
    scene ch3sc22_186 with dissolve
    $ renpy.pause(1)
    scene ch3sc22_187 with dissolve
    $ renpy.pause(1)
    scene ch3sc22_186 with dissolve
    $ renpy.pause(1)
    scene ch3sc22_187 with dissolve
    $ renpy.pause(1)
    scene ch3sc22_188 with dissolve
    el "You’re staring at my ass, aren’t you?"
    scene ch3sc22_187 with dissolve
    mc "Yes... No! I mean-"
    scene ch3sc22_188 with dissolve
    el "*Giggles* It’s alright, you already know I don’t mind when it’s you."
    scene ch3sc22_189 with dissolve
    el "*Whispers* {size=-10}{b}I love having your eyes on me...{/b}{/size}"
    scene ch3sc22_190 with dissolve
    el "Now, check out this thing! I’ve never seen anything like it!"
    scene ch3sc22_191 with dissolve
    mc "It looks old, but there's not a speck of rust on it."
    scene ch3sc22_190 with dissolve
    el "Yeah... I think you’re right. It might even be from the first era?"
    scene ch3sc22_191 with dissolve
    mc "It must be. I don’t imagine a lot of trinkets have survived from that time, though."
    mc "It's still strange that it’s so clean and well-kept. I can't imagine that the goblins maintained it like this."
    scene ch3sc22_190 with dissolve
    el "I say we take it back to Sylph and see if she knows anything about it."
    scene ch3sc22_191 with dissolve
    mc "Good idea. I don’t think we’ll find anything else around here, so let’s head back."
    scene black with Dissolve(1.5)
    $ renpy.pause(1)
    scene ch3sc21_002 with Dissolve(1.5)
    $ renpy.pause(1.5)
    scene ch3sc21_003 with dissolve
    el "I still can’t believe we completely cleared those ruins of so many goblins! There were way more than I expected!"
    el "That was insane! I never imagined such foul creatures existed."
    scene ch3sc21_004 with dissolve
    mc "You did good. I’m proud of you."
    scene ch3sc21_005 with dissolve
    el "I wasn’t about to let you have all the fun."
    scene ch3sc21_006 with dissolve
    el "But thanks. It means a lot coming from you."
    scene ch3sc21_007 with dissolve
    mc "Oren... your father, he'd have been proud of you, Eliza. You fought with zero hesitation."
    scene ch3sc21_008 with dissolve
    el "[mc], thank you for saying that. But I still feel like I let you down, getting caught off-guard by that storm attack..."
    scene ch3sc21_007 with dissolve
    mc "Seriously, don’t beat yourself up over it, Eliza."
    mc "You’ve only been training with me for a couple of weeks. Dodging spells is not something you learn overnight."
    scene ch3sc21_010 with dissolve
    el "Promise I wasn’t a burden?"
    scene ch3sc21_012 with dissolve
    mc "A burden..? You took out two goblins. You know what I did the first time I encountered goblins?"
    scene ch3sc21_010 with dissolve
    el "You probably killed like ten..."
    scene ch3sc21_011 with dissolve
    mc "I froze. I was terrified of them. Their deep snarls, their horrifying yellow eyes, their disgusting sharp teeth..."
    scene ch3sc21_012 with dissolve
    mc "Oren kept tossing me into situations where I'd have to face off against goblins until I stopped being afraid of them."
    scene ch3sc21_007 with dissolve
    mc "You, on the other hand, you just charged into them and started killing them efficiently. Not a shred of fear in you."
    scene ch3sc21_005 with dissolve
    el "You were in danger... I won’t let anyone harm you."
    scene ch3sc21_006 with dissolve
    el "I want to get stronger. I want to be able to fight by your side, as your equal."
    scene ch3sc21_017 with dissolve
    mc "You’re well on your way. It felt great having you fight by me this time."
    scene ch3sc21_018 with dissolve
    elt "He liked having me by his side..."
    elt "I already look forward to our next adventure!"
    scene ch3sc21_040 with dissolve
    el "Let’s get out of here... I feel like I need a long bath!"
    scene ch3sc21_027 with dissolve
    mc "Yeah, you reek..."
    scene ch3sc21_026 with dissolve
    with vpunch
    el "Hey! be nice! *nudges your shoulder* It’s not like you’re smelling of dandelions right now either..."
    scene ch3sc21_017 with dissolve
    mc "*Chuckle* Alright, I guess we’ll both have a bath after we’ve collected our reward."
    scene ch3sc21_026 with dissolve
    el "Deal! Ahh... Just the thought of a warm relaxing bath."
    el "And having my feet massaged."
    scene ch3sc21_007 with dissolve
    mc "Who said anything about that?"
    scene ch3sc21_026 with dissolve
    el "*Giggles* I did, just now! You owe me, I totally saved your ass back there."
    scene ch3sc21_038 with dissolve
    mc "*Sigh* I’m not massaging your smelly feet."
    scene ch3sc21_028 with dissolve
    el "Huh?! How dare you!"
    el "My little feet are cute and you know it!"
    scene ch3sc21_034 with dissolve
    el "Besides, they’ll be nice and fresh after the bath... like the rest of me."
    scene ch3sc21_017 with dissolve
    mc "Alright, alright. You’ll get your massage."
    scene ch3sc21_025 with dissolve
    elt "Yes!! If he treats me like this after killing goblins... I won’t mind hunting down a few more. *Giggles*"
    scene ch3sc21_017 with dissolve
    mc "What are you smiling about?"
    scene ch3sc21_028 with dissolve
    el "Nothing! Let’s gooo! To the Guild we go!"
    stop music fadeout 2.0
    scene black with Dissolve(1.5)
    jump ch3sc23
