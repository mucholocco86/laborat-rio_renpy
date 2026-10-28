
#DIANA SCENES
default is_diana_anim_tj1 = False
default is_diana_anim_tj2 = False
default is_diana_anim_tj3 = False

default bj_pos_toggle = True
default bj_pov_toggle = True
default is_diana_anim_bj1 = False
default is_diana_anim_bj2 = False
default is_diana_anim_bj3 = False
default is_diana_anim_bj3_first = True
default is_diana_bj_notfirst = False
default is_diana_bj_refusedpay = False

default vsex_pos_toggle = True
default vsex_pov_toggle = True
default is_diana_anim_vsex1 = False
default is_diana_anim_vsex2 = False
default is_diana_anim_vsex3 = False

default asex_pos_toggle = True
default asex_pov_toggle = True
default asex_pos_toggle2 = True
default asex_pov_toggle2 = True
default is_diana_anim_asex1 = False
default is_diana_anim_asex2 = False
default is_diana_anim_asex3 = False
default is_diana_anim_asex4 = False

image is_diana_anim_tj2 = Movie(play="images/is_scenes/diana/is_diana_tj/anims/is_diana_anim_tj2.webm", loop=True)

image is_diana_anim_bj1 = Movie(play="images/is_scenes/diana/is_diana_bj/anims/is_diana_anim_bj1.webm", loop=True)
image is_diana_anim_bj2 = Movie(play="images/is_scenes/diana/is_diana_bj/anims/is_diana_anim_bj2.webm", loop=True)
image is_diana_anim_bj3 = Movie(play="images/is_scenes/diana/is_diana_bj/anims/is_diana_anim_bj3.webm", loop=True)
image is_diana_anim_bj4 = Movie(play="images/is_scenes/diana/is_diana_bj/anims/is_diana_anim_bj4.webm", loop=True)



screen h_is_diana_tj1_hover_areas():
    add "h_is_diana_nipple_hover"
    add "h_is_diana_breast_hover"

screen h_is_diana_tj1():
    imagebutton:
        idle "interact_indicator_idle"
        hover "interact_indicator_hover"
        focus_mask True
        action NullAction()
        hovered [
            Show("h_is_diana_tj1_hover_areas")
        ]
        unhovered [
            Hide("h_is_diana_tj1_hover_areas")
        ]

    imagebutton auto "h_is_diana_nipple_%s":
        focus_mask True
        action Jump("h_is_diana_tj1_nipple")
    
    imagebutton auto "h_is_diana_breast_%s":
        focus_mask True
        action Jump("h_is_diana_tj1_breast")
    
    imagebutton auto "main_choices_op1_%s":
        focus_mask True
        action Jump("is_diana_tj2")
    text "Continue":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 832 xanchor 0.5 yanchor 0.5 italic True

screen is_diana_tj_choice03():
    imagebutton auto "main_choices_op1_%s":
        focus_mask True
        action Jump("is_diana_tj_cumface")
    text "Cum on face":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 832 xanchor 0.5 yanchor 0.5 italic True
    
    imagebutton auto "main_choices_op2_%s":
        focus_mask True
        action Jump("is_diana_tj_cumbreasts")
    text "Cum on breasts":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 959 xanchor 0.5 yanchor 0.5 italic True

default h_is_diana_tj1_nipple_first = True
default h_is_diana_tj1_nipple_second = False
label is_diana_tj1:
    if mc_coin >= 1:
        $ mc_visit_diana += 1
        $ mc_coin -= 1

        $ brothel_coin_new -= 1

        $ mcname = persistent.name
        if persistent.name == "None" or mcname == "None":
            while mcname == "None" or mcname == "":
                $ mcname = renpy.input("There was an issue with your name. Please rewrite your name:", length=32)
            $ persistent.name = mcname
        if not persistent.scene5_p3_replay:
            $ persistent.scene5_p3_replay = True
        $ diana_tj = True
        scene 7_s24 with dissolve
        if cycle == 0:
            di "Come here, baby~"
        elif cycle == 1:
            di "I have seen staring at them for a while, I guess you couldn't handle it anymore~"
        elif cycle == 2:
            di "You want to cover my tits?"
        elif cycle == 3:
            di "I want you to see you fuck my tits like a pussy~"
        stop music fadeout 2.0
        $ h_is_diana_tj1_nipple_first = True
        $ h_is_diana_tj1_nipple_second = False
        $ is_diana_tj_sitting_first = True
        $ is_diana_tj_lying_first = True
        scene 7_s25 with dissolve
        scene is_diana_tj_1 with Fade(1.0,0.5,0.5)
        ""
        scene is_diana_tj_2 with fade
        di "Want to feel me up first~?"
        scene is_diana_tj_5 with dissolve
        if not interact_indicator:
            $ interact_indicator = True
            call screen interact_tutorial with Dissolve(0.3)
        call screen h_is_diana_tj1 with dissolve
    else:
        if mc_harem_diana:
            $ mcname = persistent.name
            if persistent.name == "None" or mcname == "None":
                while mcname == "None" or mcname == "":
                    $ mcname = renpy.input("There was an issue with your name. Please rewrite your name:", length=32)
                $ persistent.name = mcname
            if not persistent.scene5_p3_replay:
                $ persistent.scene5_p3_replay = True
            mc "I don't have enough coin..."
            scene 7_s24 with dissolve
            di "Coin? You don't need coin, baby. We're lovers afterall."
            di "Come over here~"
            scene 7_s25 with dissolve
            $ diana_tj = True
            stop music fadeout 2.0
            $ h_is_diana_tj1_nipple_first = True
            $ h_is_diana_tj1_nipple_second = False
            $ is_diana_tj_sitting_first = True
            $ is_diana_tj_lying_first = True
            scene 7_s25 with dissolve
            scene is_diana_tj_1 with Fade(1.0,0.5,0.5)
            ""
            scene is_diana_tj_2 with fade
            di "Want to feel me up first~?"
            scene is_diana_tj_5 with dissolve
            call screen h_is_diana_tj1 with dissolve
        else:
            mc "(I don't have enough coin...)"
            call screen is_diana with dissolve

label h_is_diana_tj1_nipple:
    if h_is_diana_tj1_nipple_first:
        scene is_diana_tj_6 with fade
        perception "Her nipples are already hard and sensitive, standing at attention as if begging for your touch."
        di "Ahh... yes, just like that... don't stop, please..."
        scene is_diana_tj_5 with dissolve
        $ h_is_diana_tj1_nipple_first = False
        $ h_is_diana_tj1_nipple_second = True
        call screen h_is_diana_tj1 with dissolve
    elif h_is_diana_tj1_nipple_second:
        scene is_diana_tj_6 with fade
        perception "You take one nipple in your mouth, sucking more eagerly, Her body trembles before you."
        di "Hey, you know there's no milk in there, right? No matter how hard you suck, it won't happen~"
        scene is_diana_tj_5 with dissolve
        call screen h_is_diana_tj1 with dissolve

label h_is_diana_tj1_breast:
    scene is_diana_tj_8 with fade
    di "Ahh~"
    scene is_diana_tj_9 with dissolve
    sensation "They're impossibly soft, yet firm, the skin smooth and warm to the touch. 
    You knead them gently, your thumbs brushing over her hardened nipples, drawing a soft gasp from her lips."
    di "Hnnn~"
    scene is_diana_tj_5 with dissolve
    call screen h_is_diana_tj1 with dissolve

default is_diana_tj_sitting_first = True
default is_diana_tj_lying_first = True

label is_diana_tj2:
    $ mcname = persistent.name
    $ is_diana_tj_sitting_first = True
    $ is_diana_tj_lying_first = True
    scene is_diana_tj_4 with dissolve
    di "Show me that cock, I'll keep it nice and warm between my tits~"
    scene is_diana_tj_5 with dissolve

label is_diana_tj_sitting:
    $ is_diana_anim_tj1 = True
    $ is_diana_anim_tj2 = False
    $ is_diana_anim_tj3 = False
    if is_diana_tj_sitting_first:
        scene black with Fade(0.5,0.5,0.5)
        show diana_tj01 with dissolve
        perception "She shifts her body, her hands eagerly grabbing her breasts and pressing them together, creating a tight, warm tunnel for your cock."
        $ is_diana_tj_sitting_first = False
        call screen scene05_choice04 with dissolve
    else:
        scene black with Dissolve(0.3)
        show diana_tj01 with dissolve
        d "Mmmm~ See how your pre-cum is already flowing?"
    call screen scene05_choice04 with dissolve

label is_diana_tj_lying:
    $ is_diana_anim_tj1 = False
    $ is_diana_anim_tj2 = True
    $ is_diana_anim_tj3 = False
    if is_diana_tj_lying_first:
        scene black with Fade(0.5,0.5,0.5)
        show is_diana_anim_tj2 with dissolve
        perception "You position yourself above her, your cock throbbing as you slide it between the soft, warm valley of her tits."
        $ is_diana_tj_lying_first = False
        call screen scene05_choice04 with dissolve
    else:
        scene black with Dissolve(0.3)
        show is_diana_anim_tj2 with dissolve
        di "I'm getting wet just by looking at you fucking my tits~"
        call screen scene05_choice04 with dissolve

label is_diana_tj_reverse:
    $ is_diana_anim_tj1 = False
    $ is_diana_anim_tj2 = False
    $ is_diana_anim_tj3 = True
    scene black with Dissolve(0.3)
    show diana_rtj01 with dissolve
    di "Mmmm~"
    di "{i}*lick* *lick*...{/i}"
    scene black with Dissolve(0.3)
    show diana_rtj02 with dissolve
    di "{i}Humph!{/i} You like that?"
    call screen scene05_choice04 with dissolve

label is_diana_tj_faster:
    $ renpy.music.stop(channel='diana_channel')
    if is_diana_anim_tj1:
        show diana_tj01_faster with dissolve
        hide diana_tj01
        di "{i}Humph!{/i} You like that?"
        call screen scene05_choice04 with dissolve
    elif is_diana_anim_tj2:
        show is_diana_anim_tj2_faster with dissolve
        hide is_diana_anim_tj2
        di "{i}Mmm...{/i}"
        call screen scene05_choice04 with dissolve
    else:
        show diana_rtj02_faster with dissolve
        hide diana_rtj02
        di "{i}*lick* *lick*...{/i}"
        call screen scene05_choice04 with dissolve

label is_diana_tj_cumface:
    $ diana_cum_on_face = True
    sensation "The friction of her soft, enveloping tits is too much to bear, the warmth and pressure driving you closer and closer to the edge."
    d "Spilling your seed? Hold on, let me take off my dress first~"
    play sound "se_sfx/blowjob/facial5.mp3" 
    scene is_diana_tj_12 with vpunch
    perception "Your cock throbs as the first spurt of cum shoots out, hot and thick. Her lips part instinctively, her tongue darting out to catch the first pulse as you aim directly at her face."
    play sound "se_sfx/blowjob/facial4.mp3" 
    scene is_diana_tj_13 with vpunch
    perception "Another patch of cum shoot out, one spurt lands on her tongue again. The rest splashes across her cheeks and nose, some even streaking through her hair as your release paints her face."
    scene is_diana_tj_14 with dissolve
    di "Yumm~ You got some in my mouth..."
    scene is_diana_tj_15 with dissolve
    mc "Hahh... you opened your mouth intentionally."  
    scene is_diana_tj_14 with dissolve
    di "Of course. How else would I get a taste?"
    di "How about you use my mouth hole next time? I want a full load of that potent seed in my throat~ Let me gargle it before I swallow it down."
    scene is_diana_tj_15 with dissolve
    scene black with Fade(1.0,0.5,0.5)
    $ renpy.end_replay()
    if not mc_diana_scene:
        jump scene05_diana_scene
    jump diana_sex_end

label is_diana_tj_cumbreasts:
    $ diana_cum_on_breasts = True
    perception "Just as you're about to tip over the edge, you pull out from between her soft, warm breasts, your cock throbbing urgently in your hand."
    d "Spilling your seed? Hold on, let me take off my dress first~"
    play sound "se_sfx/blowjob/facial1.mp3" 
    scene is_diana_tj_16 with vpunch
    perception "You aim directly at her chest. The first spurt of semen shoots out, the thick, hot liquid splashing against her skin. Diana gasps softly, her body shudders as she feels the warmth spread across her."
    play sound "se_sfx/blowjob/facial4.mp3" 
    scene is_diana_tj_17 with vpunch
    mc "{i}Nghhh!{/i}"
    scene is_diana_tj_18 with dissolve
    di "My tits are all covered up with your seed, [mc]... I can't believe you would dirty me like this~"
    scene is_diana_tj_19 with dissolve
    mc "God... I can't get enough of your breasts."
    mc "It's like they were made for this."
    scene is_diana_tj_18 with dissolve
    di "Maybe they were~ Maybe their purpose was for [mc] to jerk his big fat cock between them all along. And once he's done, he'll spill his warm seed and mark them as his~"
    scene is_diana_tj_19 with dissolve
    mc "Stop! You're making me hard again..."
    scene is_diana_tj_18 with dissolve
    di "*giggles* Why should I? You being hard equals more coin for me~"
    scene is_diana_tj_19 with dissolve
    $ renpy.end_replay()
    if not mc_diana_scene:
        jump scene05_diana_scene
    scene black with Fade(1.0,0.5,0.5)
    jump diana_sex_end

screen is_diana_bj_choice01():
    imagebutton auto "main_choices_op2_%s":
        focus_mask True
        action [
            ToggleVariable("bj_pos_toggle"), 
            If(bj_pos_toggle, Jump("is_diana_bj_choice04_pay"), Jump("is_diana_bj_pov1"))
        ]
    text "Change position":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 959 xanchor 0.5 yanchor 0.5 italic True

    if not is_diana_anim_bj_part2:
        imagebutton auto "main_choices_op3_%s":
            focus_mask True
            action Jump("is_diana_bj_pov1")
        text "Change POV":
            size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 1086 xanchor 0.5 yanchor 0.5 italic True
    else:
        imagebutton auto "main_choices_op3_%s":
            focus_mask True
            action Jump("is_diana_bj_pov2")
        text "Change POV":
            size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 1086 xanchor 0.5 yanchor 0.5 italic True

    imagebutton auto "main_choices_op4_%s":
        focus_mask True
        action Jump("is_diana_bj_cum")
    text "Cum":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 1214 xanchor 0.5 yanchor 0.5 italic True

screen is_diana_bj_choice02():
    imagebutton auto "main_choices_op1_%s":
        focus_mask True
        action Jump("is_diana_bj_cum_inside")
    text "Cum inside":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 832 xanchor 0.5 yanchor 0.5 italic True
    
    imagebutton auto "main_choices_op2_%s":
        focus_mask True
        action Jump("is_diana_bj_cum_outside")
    text "Cum outside":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 959 xanchor 0.5 yanchor 0.5 italic True

label is_diana_bj1:
    if mc_coin >= 2:
        $ mc_visit_diana += 1
        $ brothel_coin_new -= 2
        $ mcname = persistent.name
        if persistent.name == "None" or mcname == "None":
            while mcname == "None" or mcname == "":
                $ mcname = renpy.input("There was an issue with your name. Please rewrite your name:", length=32)
            $ persistent.name = mcname
        if not persistent.scene6_p3_replay:
            $ persistent.scene6_p3_replay = True
        scene 7_s24 with dissolve
        if cycle == 0:
            di "Better hold on to you semen, or I might steal it~"
        elif cycle == 1:
            di "Follow me~"
        elif cycle == 2:
            di "I'll swallow every drop~"
        elif cycle == 3:
            di "Make me choke on it."
        scene 7_s25 with dissolve
        stop music fadeout 2.0
        $ is_diana_anim_bj1 = True
        $ is_diana_anim_bj2 = False
        $ is_diana_anim_bj3 = False
        $ is_diana_anim_bj4 = False
        $ bj_pov_toggle = True
        $ is_diana_bj_refusedpay = False
        $ mc_coin -= 2
        $ diana_bj = True
        jump scene05_choice03_bj
    else:
        if mc_harem_diana:
            $ mcname = persistent.name
            if persistent.name == "None" or mcname == "None":
                while mcname == "None" or mcname == "":
                    $ mcname = renpy.input("There was an issue with your name. Please rewrite your name:", length=32)
                $ persistent.name = mcname
            if not persistent.scene6_p3_replay:
                $ persistent.scene6_p3_replay = True
            mc "I don't have enough coin..."
            scene 7_s24 with dissolve
            di "Coin? You don't need coin, baby. We're lovers afterall."
            di "Come over here~"
            scene 7_s25 with dissolve
            stop music fadeout 2.0
            $ is_diana_anim_bj1 = True
            $ is_diana_anim_bj2 = False
            $ is_diana_anim_bj3 = False
            $ bj_pov_toggle = True
            $ is_diana_bj_refusedpay = False
            $ diana_bj = True
            jump scene05_choice03_bj
        else:
            mc "(I don't have enough...)"
            call screen is_diana with dissolve

label is_diana_bj_before:
    scene 5_s17 with dissolve
    di "{i}Mmmm~{/i} Your wish is my command."
    scene 5_s35 with dissolve
    jump scene05_choice03_bj

default is_diana_anim_bj4 = False
label scene05_choice03_bj:
        $ mcname = persistent.name
        $ is_diana_anim_bj1 = True
        $ is_diana_anim_bj2 = False
        $ is_diana_anim_bj3 = False
        $ is_diana_anim_bj4 = False
        $ bj_pov_toggle = True
        scene black with Fade(1.0,0.5,1.0)
        perception "Before you can even get another word out, Diana strips off her clothes and drops to her knees. Her fingers sliding up your thighs, teasingly close to your throbbing cock."
        scene is_diana_bj_3 with fade
        sensation "Her hot breath caresses your skin as her wet tongue works it's way between your testicles."
        scene is_diana_bj_4 with dissolve
        sensation "Her tongue flicks over your frenulum, teasing it as if she's trying to make you climax right then and there."
        show is_diana_anim_bj1 with Dissolve(1.0)
        sensation "She finally takes your cock into her mouth, her lips clamp down tight and her throat swallows you greedily. Her tongue swirls around the head."
        $ bj_pos_toggle = True
        call screen is_diana_bj_choice01 with dissolve

default is_diana_anim_bj_part2 = False
label is_diana_bj_choice04_pay:
    $ bj_pov_toggle = False
    $ is_diana_anim_bj_part2 = True
    if is_diana_anim_bj3_first:
        scene black with fade
        perception "Diana slowly lies back on the nearby table, positioning herself just right. Her body arches invitingly."
        scene is_diana_bj_18 with fade
        di "Go ahead, baby. Fuck my mouth like it owes you coin."
        scene is_diana_bj_19 with dissolve
        di "Ahhhhhhh~"
        scene is_diana_bj_33 with dissolve
        show is_diana_anim_bj3 with dissolve
        sensation "As you slide your cock into her waiting mouth, she opens wider, her lips stretching around your tip greedily."
        sensation "Her tongue swirls around you, and her throat tightens, as if her only purpose is to milk every last drop of your seed."
        $ is_diana_anim_bj1 = False
        $ is_diana_anim_bj2 = False
        $ is_diana_anim_bj3 = True
        $ is_diana_anim_bj4 = False
        $ is_diana_anim_bj3_first = False
        call screen is_diana_bj_choice01 with dissolve
    else:
        scene black with Dissolve(0.3)
        show is_diana_anim_bj3 with dissolve
        $ is_diana_anim_bj1 = False
        $ is_diana_anim_bj2 = False
        $ is_diana_anim_bj3 = True
        $ is_diana_anim_bj4 = False
        call screen is_diana_bj_choice01 with dissolve

label is_diana_bj_pov1:
    $ is_diana_anim_bj_part2 = False
    $ is_diana_anim_bj3 = False
    $ is_diana_anim_bj4 = False
    if bj_pov_toggle:
        $ is_diana_anim_bj2 = True
        $ is_diana_anim_bj1 = False
        $ bj_pov_toggle = False
        scene black with Dissolve(0.3)
        show is_diana_anim_bj2 with dissolve
        di "Aghhh~ *slurp*"
    else:
        $ is_diana_anim_bj1 = True
        $ is_diana_anim_bj2 = False
        $ bj_pov_toggle = True
        scene black with Dissolve(0.3)
        show is_diana_anim_bj1 with dissolve
        di "*cough* Sho tashty~"
    call screen is_diana_bj_choice01 with dissolve


label is_diana_bj_pov2:
    $ is_diana_anim_bj_part2 = True
    $ is_diana_anim_bj1 = False
    $ is_diana_anim_bj2 = False
    $ is_diana_anim_bj3 = True
    if bj_pov_toggle:
        $ bj_pov_toggle = False
        scene black with Dissolve(0.3)
        show is_diana_anim_bj3 with dissolve
        di "*slurp* Yesh~ Use my mouth like a toy~!"
    else:
        $ bj_pov_toggle = True
        scene black with Dissolve(0.3)
        show is_diana_anim_bj4 with dissolve
        di "Mfhmmm! *cough* *gag*"
    call screen is_diana_bj_choice01 with dissolve

label is_diana_bj_cum:
    mc "I can't hold it anymore!"
    call screen is_diana_bj_choice02 with dissolve

label is_diana_bj_cum_inside:
    if is_diana_anim_bj1 or is_diana_anim_bj2:
        sensation "She senses you're about to explode and doubles down, her tongue flicking and swirling around the tip of your cock, teasing you mercilessly."
        scene is_diana_bj_32 with dissolve
        mc "Ahhnn!"
        sensation "The subtle squeeze of her throat is all the encouragement you need—she's practically begging for you to ejaculate in her greedy mouth."
        play sound "se_sfx/blowjob/blowjob_cum3.mp3" 
        scene is_diana_bj_1 with vpunch
        mc "Fuck! Diana!"
        di "Mmmmnn~"
        sensation "You erupt. Diana doesn't gag or pull away, instead, she holds you deep, swallowing every thick, hot rope of cum you pump into her throat."
        play sound "se_sfx/blowjob/blowjob_cum2.mp3" 
        scene is_diana_bj_2 with vpunch
        mc "{i}NGHHNNN!!{/i}"
        scene is_diana_bj_5 with fade
        mc "Haah... hah.."
        scene is_diana_bj_6 with dissolve
        ""
        scene is_diana_bj_5 with dissolve
        mc "...Diana?"
        scene is_diana_bj_7 with dissolve
        di "{i}Ahhhnn~{/i}"
        scene is_diana_bj_6 with dissolve
        ""
        scene is_diana_bj_5 with dissolve
        mc "Fuck... You're gonna make me hard again."
        scene is_diana_bj_8 with dissolve
        jump is_diana_bj_cum_swallow

    elif is_diana_anim_bj3 or is_diana_anim_bj4:
        play sound "se_sfx/blowjob/gag1.mp3" 
        scene is_diana_bj_20 with vpunch
        perception "You push your shaft deep inside her throat and release everything. You can hear Diana gulping down some of your seed, her throat flexing with each swallow."
        play sound "se_sfx/blowjob/blowjob_cum3.mp3" 
        scene is_diana_bj_21 with vpunch
        perception "Diana moans as she struggles to swallow everything. Only when her stomach is full of your seed do you finally let her come up for air."
        scene is_diana_bj_23 with dissolve
        di "{i}*cough* *cough* Ahhhhhh~{/i}"
        scene is_diana_bj_28 with dissolve
        di "{i}Mmmm~{/i} So thick and warm..."
        di "Thank you for feeding me~"
        scene is_diana_bj_29 with dissolve
        $ renpy.end_replay()
        if not mc_diana_scene:
            jump scene05_diana_scene
        jump diana_sex_end

label is_diana_bj_cum_swallow:
    mc "Swallow it all."
    di "Mmmm~"
    scene is_diana_bj_9 with dissolve
    play sound "se_sfx/blowjob/swallow4.mp3" 
    di "{i}*gulp* *gulp*{/i}"
    scene is_diana_bj_10 with dissolve
    di "{i}Ahhhhhh~{/i}"
    scene is_diana_bj_11 with dissolve
    di "God, that was a huge load. I might just skip dinner—your seed's all I need to feel full~"
    di "I can feel your seed sloshing in my belly~ How does that make you feel?"
    scene is_diana_bj_12 with dissolve
    $ renpy.end_replay()
    if not mc_diana_scene:
        jump scene05_diana_scene
    jump diana_sex_end
        

label is_diana_bj_cum_outside:
    $ diana_cum_on_face = True
    if is_diana_anim_bj1 or is_diana_anim_bj2:
        sensation "Diana senses you're close and picks up the pace, her lips sliding faster and messier over your cock."
        play sound "se_sfx/blowjob/facial6.mp3" 
        scene is_diana_bj_13 with vpunch
        perception "At the last moment, you pull your cock out of her warm, wet mouth. She closes her eyes and tilts her head forward, ready to be painted with your seed."
        play sound "se_sfx/blowjob/facial3.mp3" 
        scene is_diana_bj_14 with vpunch
        perception "You blow your load all over her face, each hot spurt splashing across her cheeks, lips, and hair, marking her as yours."
        scene is_diana_bj_15 with dissolve
        mc "Hah... hah..."
        scene is_diana_bj_16 with dissolve
        di "You've really claimed me now, haven't you? I'm covered in your seed..."
        scene is_diana_bj_15 with dissolve
        $ renpy.end_replay()
        if not mc_diana_scene:
            jump scene05_diana_scene
        jump diana_sex_end

    elif is_diana_anim_bj3 or is_diana_anim_bj4:
            sensation "Diana feels you're about to burst and speeds up, her lips sliding faster and sloppier over your cock."
            play sound "se_sfx/blowjob/facial7.mp3" 
            scene is_diana_bj_24 with vpunch
            perception "At the last moment, you pull your cock free from her warm, sloppy mouth. She instinctively closes her eyes and tilts her head slightly downward, awaiting your release."
            play sound "se_sfx/blowjob/facial4.mp3" 
            scene is_diana_bj_25 with vpunch
            perception "You explode all over her face, each thick, hot rope splattering across her cheeks, lips, and hair, marking her as yours."
            scene is_diana_bj_27 with dissolve
            mc "Hah... hah..."
            scene is_diana_bj_26 with dissolve
            di "Did you enjoy covering my face in your seed? I'm your little canvas now, aren't I?"
            scene is_diana_bj_27 with dissolve
            $ renpy.end_replay()
            if not mc_diana_scene:
                jump scene05_diana_scene
            jump diana_sex_end

image is_diana_anim_vsex1 = Movie(play="images/is_scenes/diana/is_diana_sex/anims/is_diana_anim_vsex1.webm", loop=True)
image is_diana_anim_vsex2 = Movie(play="images/is_scenes/diana/is_diana_sex/anims/is_diana_anim_vsex2.webm", loop=True)
image is_diana_anim_vsex3 = Movie(play="images/is_scenes/diana/is_diana_sex/anims/is_diana_anim_vsex3.webm", loop=True)

screen is_diana_sex_h_is1_hover_areas():
    add "is_diana_sex1_ass_hover"
    add "is_diana_sex1_feet_hover"

screen is_diana_sex_h_is1():
    imagebutton:
        idle "interact_indicator_idle"
        hover "interact_indicator_hover"
        focus_mask True
        action NullAction()
        hovered [
            Show("is_diana_sex_h_is1_hover_areas")
        ]
        unhovered [
            Hide("is_diana_sex_h_is1_hover_areas")
        ]

    
    imagebutton auto "is_diana_sex1_ass_%s":
        focus_mask True
        action Jump("is_diana_sex_ass1")
    
    imagebutton auto "is_diana_sex1_feet_%s":
        focus_mask True
        action Jump("is_diana_sex_feet1")
    
    imagebutton auto "main_choices_op1_%s":
        focus_mask True
        action Jump("is_diana_vsex2")
    text "Continue":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 832 xanchor 0.5 yanchor 0.5 italic True


screen is_diana_sex_choice01():
    imagebutton auto "main_choices_op1_%s":
        focus_mask True
        action Jump("is_diana_vsex_choice01_ass")
    text "Eat her ass":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 832 xanchor 0.5 yanchor 0.5 italic True
    
    imagebutton auto "main_choices_op2_%s":
        focus_mask True
        action Jump("is_diana_vsex_choice01_puss")
    text "Eat her pussy":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 959 xanchor 0.5 yanchor 0.5 italic True

screen is_diana_vsex_choice01():
    if bonus_scene3:
        imagebutton auto "main_choices_op0_%s":
            focus_mask True
            action Jump("is_diana_vsex_cowgirl")
        text "Reverse cowgirl":
            size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 702 xanchor 0.5 yanchor 0.5 italic True

    imagebutton auto "main_choices_op2_%s":
        focus_mask True
        action [
            ToggleVariable("vsex_pos_toggle"), 
            If(vsex_pos_toggle, Jump("is_diana_vsex3"), Jump("is_diana_vsex_pov1"))
        ]
    text "Change position":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 959 xanchor 0.5 yanchor 0.5 italic True
        
    if not is_diana_anim_vsex3 and not bonus_scene3_vsex:
        imagebutton auto "main_choices_op3_%s":
            focus_mask True
            action [
                ToggleVariable("vsex_pov_toggle"), 
                If(vsex_pov_toggle, Jump("is_diana_vsex_pov2"), Jump("is_diana_vsex_pov1"))
            ]
        text "Change POV":
            size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 1086 xanchor 0.5 yanchor 0.5 italic True
    
    else:
        add "main_choices_op3_idle"
        text "Change POV":
            size persistent.choices_text_size color "#818181" font "candara.ttf" xpos 2260 ypos 1086 xanchor 0.5 yanchor 0.5 italic True

    imagebutton auto "main_choices_op4_%s":
        focus_mask True
        action Jump("is_diana_vsex_cum")
    text "Cum":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 1214 xanchor 0.5 yanchor 0.5 italic True

screen is_diana_vsex_choice02():
    if mc_harem_diana and mc_convince_diana_pregnancy:
        imagebutton auto "main_choices_op1_%s":
            focus_mask True
            action Jump("is_diana_vsex_cum_inside")
        text "Cum inside":
            size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 832 xanchor 0.5 yanchor 0.5 italic True
    
    imagebutton auto "main_choices_op2_%s":
        focus_mask True
        action Jump("is_diana_vsex_cum_outside")
    text "Cum outside":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 959 xanchor 0.5 yanchor 0.5 italic True

    if is_diana_anim_vsex1 == True or is_diana_anim_vsex2 == True:
        imagebutton auto "main_choices_op3_%s":
            focus_mask True
            action Jump("is_diana_sex_cum_feet1")
        text "Cum on feet":
            size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 1086 xanchor 0.5 yanchor 0.5 italic True
            
default is_diana_first_time_vsex_harem = False


label is_diana_vsex1:
    $ diana_tj = False
    $ diana_asex = False
    $ diana_bj = False
    $ brothel_diana_vsex_notfirst = True
    if mc_coin >= 4:
        $ mc_visit_diana += 1
        $ brothel_coin_new -= 4
        $ mcname = persistent.name
        if persistent.name == "None" or mcname == "None":
            while mcname == "None" or mcname == "":
                $ mcname = renpy.input("There was an issue with your name. Please rewrite your name:", length=32)
            $ persistent.name = mcname
        if not persistent.scene7_p3_replay:
            $ persistent.scene7_p3_replay = True
        scene 7_s24 with dissolve
        if cycle == 0:
            if mc_harem_diana:
                if diana_pregnant:
                    di "What's the point of that? I'm already pregnant with yours, darling."
                    di "Just kidding~ I never miss the chance of feeling your seed gushing out of my womb~"
                else:
                    if mc_convince_diana_pregnancy:
                        di "I'm ready, [mc]. If that's truly what you want... I won't object to you inseminating me today."
                    else:
                        di "Careful you don't accidentally leave a baby in my womb, [mc]."
            else:
                di "Careful you don't accidentally leave a baby in my womb, [mc]."
        elif cycle == 1:
            di "I like it rough. I want to be left trembling, legs too weak to carry me by the end of it. Think you can manage that?"
        elif cycle == 2:
            di "You won't find a tighter hole in all of Irda~"
        elif cycle == 3:
            if diana_pregnant:
                di "You'll never tire of breeding me, huh? Oh well~ I won't complain."
            else:
                di "Careful... I might be ovulating."
        scene 7_s25 with dissolve
        stop music fadeout 2.0
        $ mc_coin -= 4
        $ is_diana_anim_vsex1 = True
        $ is_diana_anim_vsex2 = False
        $ is_diana_anim_vsex3 = False
        $ vsex_pov_toggle = True
        $ is_diana_vsex3_first = True
        $ diana_vsex = True
        jump brothel_diana_vsex
    else:
        if mc_harem_diana:
            $ mcname = persistent.name
            if persistent.name == "None" or mcname == "None":
                while mcname == "None" or mcname == "":
                    $ mcname = renpy.input("There was an issue with your name. Please rewrite your name:", length=32)
                $ persistent.name = mcname
            if not persistent.scene7_p3_replay:
                $ persistent.scene7_p3_replay = True
            mc "I don't have enough coin..."
            scene 7_s24 with dissolve
            di "Coin? You don't need coin, baby. We're lovers afterall."
            di "Come over here~"
            scene 7_s25 with dissolve
            stop music fadeout 2.0
            $ is_diana_anim_vsex1 = True
            $ is_diana_anim_vsex2 = False
            $ is_diana_anim_vsex3 = False
            $ vsex_pov_toggle = True
            $ is_diana_vsex3_first = True
            $ diana_vsex = True
            jump brothel_diana_vsex
        else:
            mc "(I don't have enough coin...)"
            call screen is_diana with dissolve

default brothel_diana_vsex_notfirst = False
label brothel_diana_vsex:
    $ mcname = persistent.name
    $ is_diana_anim_vsex1 = True
    $ is_diana_anim_vsex2 = False
    $ is_diana_anim_vsex3 = False
    $ vsex_pov_toggle = True
    $ is_diana_vsex3_first = True
    if brothel_diana_vsex_notfirst:
        scene black with Fade(1.0,0.5,0.5)
        scene is_diana_sex_1 with fade
        ""
        scene is_diana_sex_2 with dissolve
        ""
        scene is_diana_sex_3 with dissolve
        di "Care to moisturize me first?"
        if not interact_indicator:
            $ interact_indicator = True
            call screen interact_tutorial with Dissolve(0.3)
        call screen is_diana_sex_h_is1 with dissolve
    else:
        jump is_diana_vsex2

label is_diana_sex_ass1:
    call screen is_diana_sex_choice01 with dissolve

label is_diana_sex_feet1:
    scene is_diana_sex_4 with dissolve
    sensation "Your tongue traces slowly along the curve of her sole. Her skin tastes sweet, and you can't resist taking your time, teasing her with every flick of your tongue."
    scene is_diana_sex_5 with dissolve
    di "Mmm, do I taste good?"
    perception "Your lips close around her toes, sucking on each one slowly, your tongue flicking between them."
    scene is_diana_sex_3 with dissolve
    call screen is_diana_sex_h_is1 with dissolve

label is_diana_vsex_choice01_puss:
    scene is_diana_sex_6 with dissolve
    sensation "You bury your face between her soft cheeks, your tongue diving into her dripping pussy. She's already wet, her folds glistening as you savor her sweet, musky taste."
    scene is_diana_sex_10 with dissolve
    di "Ahh~ uh~ Fuck, don't stop..."
    sensation "Her moans deepen, her hips grinding against your face as a flood of her warm juices spills over, coating your chin and dripping sensuously onto the bed beneath."
    scene is_diana_sex_3 with dissolve
    call screen is_diana_sex_h_is1 with dissolve

label is_diana_vsex_choice01_ass:
    di "Ah, ah, ah. That hole isn't available right now~"
    call screen is_diana_sex_h_is1 with dissolve

label is_diana_vsex_before:
    scene 5_s17 with dissolve
    di "My pussy is yours, baby~"
    scene 5_s35 with dissolve
    jump is_diana_vsex2
    
label is_diana_vsex2:
    $ is_diana_vsex_cowgirl_first = True
    $ is_diana_vsex_cowgirl_sec = False

    $ is_diana_anim_vsex1 = True
    $ is_diana_anim_vsex2 = False
    $ is_diana_anim_vsex3 = False
    $ vsex_pov_toggle = True
    $ vsex_pos_toggle = True
    $ is_diana_vsex3_first = True
    $ bonus_scene3_vsex = False
    scene is_diana_sex_28 with fade
    sensation "You guide yourself to her entrance, feeling the heat and wetness of her pussy as you push inside. 
    She's so tight, her walls clenching around you as you sink deeper."
    show is_diana_anim_vsex1 with dissolve
    perception "Her back arches as you begin to move, the angle allowing you to go deeper with each thrust. 
    Her moans grow louder, filling the room with the sound of her pleasure."
    di "Ahh~ Deeper! Fuck me harder, baby~"
    call screen is_diana_vsex_choice01 with dissolve

label is_diana_vsex_pov1:
    $ is_diana_anim_vsex1 = True
    $ is_diana_anim_vsex2 = False
    $ is_diana_anim_vsex3 = False
    $ vsex_pov_toggle = True
    $ vsex_pos_toggle = True
    $ bonus_scene3_vsex = False
    scene black with Dissolve(0.3)
    show is_diana_anim_vsex1 with dissolve
    di "Nghh~ Uh~ Ah~ Fuck, keep fucking my tight hole~"
    call screen is_diana_vsex_choice01 with dissolve

label is_diana_vsex_pov2:
    $ is_diana_anim_vsex1 = False
    $ is_diana_anim_vsex2 = True
    $ bonus_scene3_vsex = False
    $ is_diana_anim_vsex3 = False
    scene black with Dissolve(0.3)
    show is_diana_anim_asex2 with dissolve
    di "Nghh~ Uh~ Ah~"
    di "Ahhh~ You're hitting my cervix! Fuck, it's so deep~"
    call screen is_diana_vsex_choice01 with dissolve

label is_diana_vsex_faster:
    $ bonus_scene3_vsex = False
    $ renpy.music.stop(channel='diana_channel')
    if is_diana_anim_vsex1:
        show is_diana_anim_vsex1_faster with dissolve
        hide is_diana_anim_vsex1
        di "Ahhh~ You're hitting my cervix! Fuck, it's so deep~"
        call screen is_diana_vsex_choice01 with dissolve
    elif is_diana_anim_vsex2:
        show is_diana_anim_asex2_faster with dissolve
        hide is_diana_anim_asex2
        di "Mfhmmm~"
        call screen is_diana_vsex_choice01 with dissolve
    else:
        show is_diana_anim_vsex3_faster with dissolve
        hide is_diana_anim_vsex3
        di "Yes! F-faster~ Fuck me!"
        #di "Fuck me... Impregnate me!"
        call screen is_diana_vsex_choice01 with dissolve


default is_diana_vsex3_first = True    
label is_diana_vsex3:
    $ bonus_scene3_vsex = False
    $ is_diana_anim_vsex1 = False
    $ is_diana_anim_vsex2 = False
    $ is_diana_anim_vsex3 = True
    if is_diana_vsex3_first:
        scene black with fade
        perception "You guide Diana onto the table. 
        She obeys without hesitation, lying back on a table. Slowly, she lifts her legs, 
        spreading them wide, her pussy glistening and ready for you."
        scene is_diana_sex_29 with dissolve
        show is_diana_anim_vsex3 with dissolve
        perception "You step forward, aligning your cock with her dripping entrance. With a single, powerful thrust, you push inside her, her tight, wet walls parting to welcome you again."
        $ is_diana_vsex3_first = False
        call screen is_diana_vsex_choice01 with dissolve
    else:
        scene black with Dissolve(0.3)
        show is_diana_anim_vsex3 with dissolve
        di "Ahh~ Mghmm~"
        call screen is_diana_vsex_choice01 with dissolve

label is_diana_vsex_cum:
    mc "I'm cumming!"
    if mc_harem_diana and mc_convince_diana_pregnancy:
        di "Do it inside! Uhh~ Fill me with your baby batter!"
    elif mc_harem_diana:
        di "I'm still not ready for a baby, darling! Please pull out!"
    else:
        di "Don't forget to pull out!"
    call screen is_diana_vsex_choice02 with dissolve

label is_diana_vsex_cum_inside:
    if is_diana_anim_vsex1 or is_diana_anim_vsex2:
        sensation "Diana's body reacts instinctively, her inner walls tightening like a vice, urging you to release everything deep inside her."
        play sound "se_sfx/sex/sex_cum6.mp3" 
        if persistent.xray_mode:
            scene is_diana_sex_30_xray1 with vpunch
            sensation "As you bury yourself to the hilt, your release comes in powerful waves, each spurt met with her body convulsing in response."
            mc "{i}Nghhnnnn!{/i}"
            play sound "se_sfx/sex/sex_cum7.mp3" 
            scene is_diana_sex_30_xray2 with vpunch
            sensation "You stay buried inside her, savoring the aftershocks of pleasure coursing through both of you. Her walls continue to milk every last drop of your seed."
            di "You've filled me so completely... It's so warm~ I can feel your seed deep inside me..."
            mc "Hahh... hah..."
            scene is_diana_sex_11_xray3 with dissolve
        else:
            scene is_diana_sex_30 with vpunch
            sensation "As you bury yourself to the hilt, your release comes in powerful waves, each spurt met with her body convulsing in response."
            mc "{i}Nghhnnnn!{/i}"
            play sound "se_sfx/sex/sex_cum7.mp3" 
            scene is_diana_sex_30 with vpunch
            sensation "You stay buried inside her, savoring the aftershocks of pleasure coursing through both of you. Her walls continue to milk every last drop of your seed."
            di "You've filled me so completely... It's so warm~ I can feel your seed deep inside me..."
            mc "Hahh... hah..."
            scene is_diana_sex_11 with dissolve
        if diana_pregnant:
            di "Were you trying to give me twins? Or maybe triplets this time?"
            mc "...What?"
            di "You came inside me again, you know. I'll be... even more pregnant now."
            mc "That's not how that works..."
            di "Come on, baby, I was just joking~"
        else:
            call pregnancy_check_diana from ___pregnancy_check_diana
            if diana_pregnant:
                di "Fhmmnn~ You did it... you came inside me!"
                mc "Hahh... right. How does it feel? Ready to be a mother?"
                di "Gods... It's a lot scarier now that it's real."
                mc "Calm down. I'll be with you throughout it all, remember?"
                di "Y-Yes. I know~ I'm glad it was you, [mc]."
            else:
                di "Mhnnmm~ I don't feel it..."
                mc "Feel what? That you're pregnant?"
                di "Mhm. Usually your little seeds would travel to my eggs, right? Maybe they got stuck somewhere... *chuckles* or they were too stupid to find it."
                mc "Come on. There's no way you can tell this early."
                di "Hmm... whatever. We can just try again, hmm~?"
                mc "*chuckles* Right."

        di "Thank you for using my pussy~"
        scene black with Fade(1.0,0.5,0.5)
        perception "Diana tries her best to keep your seed from spilling out, her thighs trembling as she dresses up."
        $ renpy.end_replay()
        jump diana_sex_end

    elif is_diana_anim_vsex3:
        sensation "Diana's body responds instinctively, her pussy tightening around your cock, urging you to unleash everything deep inside her."
        play sound "se_sfx/sex/sex_cum5.mp3" 
        if persistent.xray_mode:
            scene is_diana_sex_31_xray1 with vpunch
            sensation "As you slam into her one last time, your release explodes in thick, hot ropes. Her pussy grips you tightly, milking every drop of your seed."
            mc "{i}Agnhhhh!{/i}"
            play sound "se_sfx/sex/sex_cum2.mp3" 
            scene is_diana_sex_31_xray2 with vpunch
            sensation "You stay buried inside her, savoring the way her walls flutter and pulse around you, greedily holding onto every last drop of your seed."
            scene is_diana_sex_16_xray3 with dissolve
        else:
            scene is_diana_sex_31 with vpunch
            sensation "As you slam into her one last time, your release explodes in thick, hot ropes. Her pussy grips you tightly, milking every drop of your seed."
            mc "{i}Agnhhhh!{/i}"
            play sound "se_sfx/sex/sex_cum2.mp3" 
            scene is_diana_sex_31 with vpunch
            sensation "You stay buried inside her, savoring the way her walls flutter and pulse around you, greedily holding onto every last drop of your seed."
            scene is_diana_sex_16 with dissolve
        if diana_pregnant:
            di "Were you trying to give me twins? Or maybe triplets this time?"
            mc "...What?"
            di "You came inside me again, you know. I'll be... even more pregnant now."
            mc "That's not how that works..."
            di "Come on, baby, I was just joking~"
        else:
            call pregnancy_check_diana from _pregnancy_check_diana
            if diana_pregnant:
                di "Fhmmnn~ You did it... you came inside me!"
                mc "Hahh... right. How does it feel? Ready to be a mother?"
                di "Gods... It's a lot scarier now that it's real."
                mc "Calm down. I'll be with you throughout it all, remember?"
                di "Y-Yes. I know~ I'm glad it was you, [mc]."
            else:
                di "Mhnnmm~ I don't feel it..."
                mc "Feel what? That you're pregnant?"
                di "Yes. It doesn't feel like I am."
                mc "Come on... There's no way you can tell this early."
                di "Hmm... whatever. We can try again, right~?"
                mc "*chuckles* Right."
    
        di "Thank you for using my pussy~"
        scene black with Fade(1.0,0.5,0.5)
        perception "Diana tries her best to keep your seed from spilling out, her thighs trembling as she dresses up."
        $ renpy.end_replay()
        jump diana_sex_end

    else:
        mc "Diana, I'm—!"
        if mc_harem_diana and mc_convince_diana_pregnancy:
            di "Yes, yes, yes~! Fuck! Fill me! Pump your hot load deep inside my slutty pussy! Breed me!"
            mc "I'm gonna fill your pussy!"
            di "Yes~! Give me everything!"
            play sound "se_sfx/sex/sex_cum9.mp3" 
            scene diana_bonus1 with vpunch
            sensation "You thrust up hard to meet her final slam and explode deep inside her. Thick, heavy ropes of cum flood her pussy, filling her womb as her walls continue to spasm around you."
            play sound "se_sfx/sex/sex_cum3.mp3" 
            scene diana_bonus2 with vpunch
            di "Mmmhhh~! Keep cumming... Give me every drop~ I can feel it shooting so deep inside me!"
            perception "Your cum mixes with her juices and starts leaking out around your cock with every twitch of her overstimulated pussy."
            play sound "se_sfx/sex/touch2.mp3" 
            scene diana_bonus3 with Dissolve(1.0)
            if diana_pregnant:
                di "*chuckles* You really put your back into this load, hmm?"
                mc "It feels even better when I think about impregnating you..."
                di "Oooh~ Well, I can't deny that I feel the same when I think about you putting a kid in me."
                di "Regardless, the one growing in my belly is enough for now~"
            else:
                call pregnancy_check_diana from __pregnancy_check_diana
                if diana_pregnant:
                    di "Fhmmnn~ You did it... you came inside me!"
                    mc "Hahh... right. How does it feel? Ready to be a mother?"
                    di "Gods... It's a lot scarier now that it's real."
                    mc "Calm down. I'll be with you throughout it all, remember?"
                    di "Y-Yes. I know~ I'm glad it was you, [mc]."
                else:
                    di "Mhnnmm~ I don't feel it..."
                    mc "Feel what? That you're pregnant?"
                    di "Yes. It doesn't feel like I am."
                    mc "Come on... There's no way you can tell this early."
                    di "Hmm... whatever. We can try again, right~?"
                    mc "*chuckles* Right."
        else:
            di "I'm still not ready for a baby, darling! Please pull out!"
            play sound "se_sfx/blowjob/facial2.mp3" 
            scene diana_bonus4 with vpunch
            perception "You pull out quickly, just before filling up her womb."
            play sound "se_sfx/blowjob/facial4.mp3" 
            scene diana_bonus5 with vpunch
            perception "Your cock throbs as hot streams of cum shoot across her ass and back, painting her skin in thick, glistening lines."
            mc "Nghhhh!"
            di "Ahnn~ Hahh..."
            di "You really couldn't resist making a mess of me, could you?"

        di "Thank you for using my pussy~"
        scene black with Fade(1.0,0.5,0.5)
        perception "Diana tries her best to keep your seed from spilling out, her thighs trembling as she dresses up."
        $ renpy.end_replay()
        jump diana_sex_end

label is_diana_vsex_cum_outside:
    if is_diana_anim_vsex1 or is_diana_anim_vsex2:
        mc "{i}Nhnnggg!{/i}"
        play sound "se_sfx/blowjob/facial1.mp3" 
        scene is_diana_sex_13 with vpunch
        perception "You pull out quickly, just before filling up her womb."
        perception "Your cock throbs as hot streams of cum shoot across her ass, painting her skin in thick, glistening lines."
        play sound "se_sfx/blowjob/facial4.mp3" 
        scene is_diana_sex_14 with vpunch
        mc "Nghhhh!"
        scene is_diana_sex_15 with dissolve
        di "Ahnn~ Hahh..."
        di "You really couldn't resist making a mess of me, could you?"
        scene black with Fade(1.0,0.5,0.5)
        $ renpy.end_replay()
        if not mc_diana_scene:
            jump scene05_diana_scene
        perception "Diana finally stands, carefully collecting her clothes."
        jump diana_sex_end

    elif is_diana_anim_vsex3:
        play sound "se_sfx/sex/touch2.mp3" 
        scene is_diana_sex_19 with vpunch
        perception "You pull out quickly, just before filling up her womb."
        perception "Hot streams of your semen erupt, splattering across Diana's stomach, painting her skin."
        play sound "se_sfx/blowjob/facial7.mp3" 
        scene is_diana_sex_20 with vpunch
        mc "Nghhhh!"
        scene is_diana_sex_17 with dissolve
        di "Ahh~ It's so... warm."
        di "You really couldn't resist making a mess of me, could you?"
        scene is_diana_sex_18 with dissolve
        scene black with Fade(1.0,0.5,0.5)
        $ renpy.end_replay()
        if not mc_diana_scene:
            jump scene05_diana_scene
        perception "Diana finally stands, carefully collecting her clothes while making no effort to clean herself off, your cum still glistening on her skin."
        jump diana_sex_end

    else:
        play sound "se_sfx/sex/touch2.mp3" 
        scene diana_bonus4 with vpunch
        perception "You pull out quickly, just before filling up her womb."
        perception "Your cock throbs as hot streams of cum shoot across her ass, painting her skin in thick, glistening lines."
        play sound "se_sfx/blowjob/facial7.mp3" 
        scene diana_bonus5 with vpunch
        mc "Nghhhh!"
        di "Ahh~ It's so... warm."
        di "You really couldn't resist making a mess of me, could you?"
        scene black with Fade(1.0,0.5,0.5)
        $ renpy.end_replay()
        if not mc_diana_scene:
            jump scene05_diana_scene
        perception "Diana finally stands, carefully collecting her clothes while making no effort to clean herself off, your cum still glistening on her skin."
        jump diana_sex_end

label is_diana_sex_cum_feet1:
    play sound "se_sfx/blowjob/facial6.mp3" 
    scene is_diana_sex_21 with vpunch
    perception "You pull out from her slick pussy and guide your throbbing shaft toward her delicate feet, your cum already bubbling at the tip."
    play sound "se_sfx/blowjob/facial7.mp3" 
    scene is_diana_sex_22 with vpunch
    perception "Thick, hot streams of cum spurt across her soles, coating them in a glistening, sticky layer."
    di "Ahh~!"
    perception "Diana jolts slightly as she feels the warmth of your seed spreading over her soles. Her toes curl instinctively, catching some of your seed as it drips down."
    scene is_diana_sex_23 with dissolve
    di "My oh my... I didn't know you were into feet {i}that{/i} much. You really couldn't resist, could you?"
    di "I'll let you cover my soles and toes whenever you like... I'll make sure they're ready for you~"
    scene black with Fade(1.0,0.5,0.5)
    $ renpy.end_replay()
    if not mc_diana_scene:
        jump scene05_diana_scene
    perception "Diana wipes off your semen from her feet then dresses up."
    jump diana_sex_end


image is_diana_anim_asex1 = Movie(play="images/is_scenes/diana/is_diana_sex/anims/is_diana_anim_asex1.webm", loop=True)
image is_diana_anim_asex2 = Movie(play="images/is_scenes/diana/is_diana_sex/anims/is_diana_anim_asex2.webm", loop=True)
image is_diana_anim_asex3 = Movie(play="images/is_scenes/diana/is_diana_sex/anims/is_diana_anim_asex3.webm", loop=True)
image is_diana_anim_asex4 = Movie(play="images/is_scenes/diana/is_diana_sex/anims/is_diana_anim_asex4.webm", loop=True)

screen is_diana_asex_h_is1_hover_areas():
    add "is_diana_sex1_ass_hover"
    add "is_diana_sex1_feet_hover"
    
screen is_diana_asex_h_is1():
    imagebutton:
        idle "interact_indicator_idle"
        hover "interact_indicator_hover"
        focus_mask True
        action NullAction()
        hovered [
            Show("is_diana_asex_h_is1_hover_areas")
        ]
        unhovered [
            Hide("is_diana_asex_h_is1_hover_areas")
        ]

    imagebutton auto "is_diana_sex1_ass_%s":
        focus_mask True
        action Jump("is_diana_asex_ass1")
    
    imagebutton auto "is_diana_sex1_feet_%s":
        focus_mask True
        action Jump("is_diana_asex_feet1")
    
    imagebutton auto "main_choices_op1_%s":
        focus_mask True
        action Jump("is_diana_asex2")
    text "Continue":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 832 xanchor 0.5 yanchor 0.5 italic True

screen is_diana_asex_choice01():
    imagebutton auto "main_choices_op1_%s":
        focus_mask True
        action Jump("is_diana_asex_choice01_ass")
    text "Eat her ass":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 832 xanchor 0.5 yanchor 0.5 italic True
    
    imagebutton auto "main_choices_op2_%s":
        focus_mask True
        action Jump("is_diana_asex_choice01_puss")
    text "Eat her pussy":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 959 xanchor 0.5 yanchor 0.5 italic True

screen is_diana_asex_controls():
    if bonus_scene3:
        imagebutton auto "main_choices_op0_%s":
            focus_mask True
            action Jump("is_diana_asex_pile")
        text "Piledriver":
            size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 702 xanchor 0.5 yanchor 0.5 italic True

    if is_diana_anim_asex1 or is_diana_anim_asex2 or bonus_scene3_asex:
        imagebutton auto "main_choices_op2_%s":
            focus_mask True
            action Jump("is_diana_asex3")
        text "Change position":
            size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 959 xanchor 0.5 yanchor 0.5 italic True

        if not bonus_scene3_asex:
            imagebutton auto "main_choices_op3_%s":
                focus_mask True
                action [
                    ToggleVariable("asex_pov_toggle"), 
                    If(asex_pov_toggle, Jump("is_diana_asex_pov2"), Jump("is_diana_asex_pov1"))
                ]
            text "Change POV":
                size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 1086 xanchor 0.5 yanchor 0.5 italic True

        else:
            imagebutton auto "main_choices_op3_%s":
                focus_mask True
            text "Change POV":
                size persistent.choices_text_size color "#818181" font "candara.ttf" xpos 2260 ypos 1086 xanchor 0.5 yanchor 0.5 italic True

    elif is_diana_anim_asex3 or is_diana_anim_asex4 or bonus_scene3_asex:
        imagebutton auto "main_choices_op2_%s":
            focus_mask True
            action Jump("is_diana_asex2")
        text "Change position":
            size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 959 xanchor 0.5 yanchor 0.5 italic True

        if not bonus_scene3_asex:
            imagebutton auto "main_choices_op3_%s":
                focus_mask True
                action [
                    ToggleVariable("asex_pov_toggle"), 
                    If(asex_pov_toggle, Jump("is_diana_asex_pov4"), Jump("is_diana_asex_pov3"))
                ]
            text "Change POV":
                size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 1086 xanchor 0.5 yanchor 0.5 italic True
        else:
            imagebutton auto "main_choices_op3_%s":
                focus_mask True
            text "Change POV":
                size persistent.choices_text_size color "#818181" font "candara.ttf" xpos 2260 ypos 1086 xanchor 0.5 yanchor 0.5 italic True

    imagebutton auto "main_choices_op4_%s":
        focus_mask True
        action Jump("is_diana_asex_cum")
    text "Cum":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 1214 xanchor 0.5 yanchor 0.5 italic True

screen is_diana_asex_choice02():
    imagebutton auto "main_choices_op1_%s":
        focus_mask True
        action Jump("is_diana_asex_cum_inside")
    text "Cum inside":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 832 xanchor 0.5 yanchor 0.5 italic True
    
    imagebutton auto "main_choices_op2_%s":
        focus_mask True
        action Jump("is_diana_asex_cum_outside")
    text "Cum outside":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 959 xanchor 0.5 yanchor 0.5 italic True

    if is_diana_anim_asex1 or is_diana_anim_asex2:
        imagebutton auto "main_choices_op3_%s":
            focus_mask True
            action Jump("is_diana_sex_cum_feet1")
        text "Cum on feet":
            size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 1086 xanchor 0.5 yanchor 0.5 italic True

label is_diana_asex1:
    if mc_coin >= 6:
        $ mc_visit_diana += 1
        $ brothel_coin_new -= 6
        $ mcname = persistent.name
        if persistent.name == "None" or mcname == "None":
            while mcname == "None" or mcname == "":
                $ mcname = renpy.input("There was an issue with your name. Please rewrite your name:", length=32)
            $ persistent.name = mcname
        if not persistent.scene8_p3_replay:
            $ persistent.scene8_p3_replay = True
        scene 7_s24 with dissolve
        if cycle == 0:
            di "Follow me, sweetheart~"
        if cycle == 1:
            di "Better stretch me first... unless you love it when I scream."
        elif cycle == 2:
            di "You wanna fuck my tight little hole?"
        elif cycle == 3:
            di "Then fuck me raw and leave your cum inside all day."
        scene 7_s25 with dissolve
        stop music fadeout 2.0
        $ mc_coin -= 6
        $ diana_asex = True
        $ is_diana_anim_asex1 = True
        $ is_diana_anim_asex2 = False
        $ is_diana_anim_asex3 = False
        $ is_diana_anim_asex4 = False
        $ asex_pov_toggle = True
        $ is_diana_asex2_first = True
        $ bonus_scene3_asex = False
        scene black with Fade(1.0,0.5,0.5)
        scene is_diana_sex_1 with fade
        ""
        scene is_diana_sex_2 with dissolve
        ""
        scene is_diana_sex_3 with dissolve
        di "Won't you stretch my ass first?"
        call screen is_diana_asex_h_is1 with dissolve
    else:
        if mc_harem_diana:
            $ mcname = persistent.name
            if persistent.name == "None" or mcname == "None":
                while mcname == "None" or mcname == "":
                    $ mcname = renpy.input("There was an issue with your name. Please rewrite your name:", length=32)
                $ persistent.name = mcname
            if not persistent.scene8_p3_replay:
                $ persistent.scene8_p3_replay = True
            mc "I don't have enough coin..."
            scene 7_s24 with dissolve
            di "Coin? You don't need coin, baby. We're lovers afterall."
            di "Come over here~"
            $ bonus_scene3_asex = False
            scene 7_s25 with dissolve
            stop music fadeout 2.0
            $ diana_asex = True
            $ is_diana_anim_asex1 = True
            $ is_diana_anim_asex2 = False
            $ is_diana_anim_asex3 = False
            $ is_diana_anim_asex4 = False
            $ asex_pov_toggle = True
            $ is_diana_asex2_first = True
            scene black with Fade(1.0,0.5,0.5)
            scene is_diana_sex_1 with fade
            ""
            scene is_diana_sex_2 with dissolve
            ""
            scene is_diana_sex_3 with dissolve
            di "Won't you stretch my ass first?"
            call screen is_diana_asex_h_is1 with dissolve
        else:
            mc "(I don't have enough money...)"
            call screen is_diana with Dissolve(0.5)

label is_diana_asex_ass1:
    #$ mcname = persistent.name
    $ is_diana_anim_asex1 = True
    $ is_diana_anim_asex2 = False
    $ is_diana_anim_asex3 = False
    $ is_diana_anim_asex4 = False
    $ asex_pov_toggle = True
    $ is_diana_asex2_first = True
    call screen is_diana_asex_choice01 with dissolve

label is_diana_asex_choice01_puss:
    scene is_diana_sex_6 with dissolve
    sensation "You bury your face between her soft cheeks, your tongue diving into her dripping pussy. She's already wet, her folds glistening as you savor her sweet, musky taste."
    scene is_diana_sex_10 with dissolve
    di "Ahh~ uh~ Fuck, don't stop..."
    sensation "Her moans deepen, her hips grinding against your face as a flood of her warm juices spills over, coating your chin and dripping sensuously onto the bed beneath."
    scene is_diana_sex_3 with dissolve
    call screen is_diana_asex_h_is1 with dissolve

label is_diana_asex_feet1:
    scene is_diana_sex_4 with dissolve
    sensation "Your tongue traces slowly along the curve of her sole. Her skin tastes sweet, and you can't resist taking your time, teasing her with every flick of your tongue."
    scene is_diana_sex_5 with dissolve
    di "Mmm, do I taste good?"
    perception "Your lips close around her toes, sucking on each one slowly, your tongue flicking between them."
    scene is_diana_sex_3 with dissolve
    call screen is_diana_asex_h_is1 with dissolve

label is_diana_asex_choice01_ass:
    scene is_diana_sex_6 with dissolve
    perception "You tighten your grip on her hips, holding her steady as your tongue explores her anus, teasing her tight rim."
    scene is_diana_sex_9 with dissolve
    di "Ahh~ You're... relentless... I can't take it~"
    perception "You circle her rim with the tip of your tongue, teasing her sensitive nerves before plunging in again, eliciting a sharp gasp from her lips."
    di "Y-you're making me feel... things I never thought I'd enjoy..."
    scene is_diana_sex_7 with dissolve
    di "I'm ready for you now~"
    scene is_diana_sex_3 with dissolve
    call screen is_diana_asex_h_is1 with dissolve

default is_diana_asex2_first = True
label is_diana_asex2_before:
    scene 5_s17 with dissolve
    di "Oh! Well, aren't you bold..."
    di "Of course, let me prepare myself for you."
    di "Just promise you'll go easy on me~"
    scene 5_s35 with dissolve
    jump is_diana_asex2

label is_diana_asex2:
    $ is_diana_asex_pile_first = True
    $ is_diana_asex_pile_sec = False

    $ bonus_scene3_asex = False
    $ mcname = persistent.name
    $ is_diana_anim_asex1 = True
    $ is_diana_anim_asex2 = False
    $ is_diana_anim_asex3 = False
    $ is_diana_anim_asex4 = False
    $ asex_pov_toggle = True
    $ asex_pos_toggle = True
    if is_diana_asex2_first:
        scene is_diana_sex_32 with dissolve
        perception "The head of your cock presses against her tight, quivering hole, the sensitive skin there fluttering at the touch."
        perception "Diana lets out a soft gasp, her body instinctively tightening for a moment before she forces herself to relax, her breath hitching as she surrenders to the sensation."
        di "Ah~ I usally don't say this, but... be gentle..."
        show is_diana_anim_asex1 with dissolve
        di "It's... so big! Uhh~ I can feel it stretching me open... fuck, it's so deep!"
        $ is_diana_asex2_first = False
        call screen is_diana_asex_controls with dissolve
    else:
        scene black with Dissolve(0.3)
        show is_diana_anim_asex1 with dissolve
        di "God! Ahhh~ Hah~"
        call screen is_diana_asex_controls with dissolve

default is_diana_asex3_first = True
label is_diana_asex3:
    $ bonus_scene3_asex = False
    $ is_diana_anim_asex1 = False
    $ is_diana_anim_asex2 = False
    $ is_diana_anim_asex3 = True
    $ is_diana_anim_asex4 = False
    $ asex_pov_toggle = True
    $ asex_pos_toggle = True
    if is_diana_asex3_first:
        scene black with Fade(1.0,0.5,0.5)
        perception "You grip Diana's hair, pushing her head down against the bed. You immediately start pounding her ass."
        show is_diana_anim_asex3 with dissolve
        perception "With each thrust, your cock slides deeper into her tight rectum, her body now more accustomed to your girth, allowing you to bury yourself even further."
        di "Mfghmmm!! Yes! Destroy my ass! Make it yours! Fuck me harder!"
        sensation "Her rectum clenches and releases around you, as if drawing you in. The wet, slapping sounds of your hips meeting her ass fill the room."
        $ is_diana_asex3_first = False
        call screen is_diana_asex_controls with dissolve
    else:
        scene black with Dissolve(0.3)
        show is_diana_anim_asex3 with dissolve
        di "Don't stop... ahh! I want it! Fill me up, claim me! Fuck my ass like the fucking slut I am!"
        call screen is_diana_asex_controls with dissolve
    
label is_diana_asex_pov1:
    $ bonus_scene3_asex = False
    $ is_diana_anim_asex1 = True
    $ is_diana_anim_asex2 = False
    $ is_diana_anim_asex3 = False
    $ is_diana_anim_asex4 = False
    $ asex_pov_toggle = True
    $ asex_pos_toggle = True
    scene black with Dissolve(0.3)
    show is_diana_anim_asex1 with dissolve
    di "Nhnnn~ Fuck!"
    call screen is_diana_asex_controls with dissolve

label is_diana_asex_pov2:
    $ bonus_scene3_asex = False
    $ is_diana_anim_asex1 = False
    $ is_diana_anim_asex2 = True
    $ is_diana_anim_asex3 = False
    $ is_diana_anim_asex4 = False
    scene black with Dissolve(0.3)
    show is_diana_anim_asex2 with dissolve
    di "Deeper! ...Ngh! Ahhh~"
    di "Ahh! God! You're ravaging my asshole!"
    call screen is_diana_asex_controls with dissolve

label is_diana_asex_pov3:
    $ bonus_scene3_asex = False
    $ is_diana_anim_asex1 = False
    $ is_diana_anim_asex2 = False
    $ is_diana_anim_asex3 = True
    $ is_diana_anim_asex4 = False
    scene black with Dissolve(0.3)
    show is_diana_anim_asex3 with dissolve
    di "Keep... pounding... ah! My little tight hole!"
    call screen is_diana_asex_controls with dissolve

label is_diana_asex_pov4:
    $ bonus_scene3_asex = False
    $ is_diana_anim_asex1 = False
    $ is_diana_anim_asex2 = False
    $ is_diana_anim_asex3 = False
    $ is_diana_anim_asex4 = True
    scene black with Dissolve(0.3)
    show is_diana_anim_asex4 with dissolve
    di "Nghaaahh! It's so fucking big!"
    di "My ass! Uhhh! You're stretching me so wide!"
    call screen is_diana_asex_controls with dissolve

label is_diana_asex_faster:
    $ bonus_scene3_asex = False
    scene black with Dissolve(0.3)
    if is_diana_anim_asex1:
        show is_diana_anim_asex1_faster with dissolve
        hide is_diana_anim_asex1
        di "Ahh! God!"
        di "You're ravaging my ass!"
        call screen is_diana_asex_controls with dissolve
    elif is_diana_anim_asex2:
        show is_diana_anim_asex2_faster with dissolve
        hide is_diana_anim_asex2
        di "Uh! Ah!"
        call screen is_diana_asex_controls with dissolve
    elif is_diana_anim_asex3:
        show is_diana_anim_asex3_faster with dissolve
        hide is_diana_anim_asex3
        di "My ass! Uhhh! You're stretching me so wide!"
        call screen is_diana_asex_controls with dissolve
    elif is_diana_anim_asex4:
        show is_diana_anim_asex4_faster with dissolve
        hide is_diana_anim_asex4
        di "Fuck! Don't stop! I'm so close!"
        call screen is_diana_asex_controls with dissolve

label is_diana_asex_cum:
    mc "I'm gonna...!"
    di "Go ahead! Fill my little hole! Pump your seed deep inside me!"
    call screen is_diana_asex_choice02 with dissolve

label is_diana_asex_cum_inside:
    if is_diana_anim_asex3 or is_diana_anim_asex4:
        sensation "You sink deeper her tight, gripping ass. The thought of spilling deep inside her consumes you, the primal urge to breed her ass, overwhelming every other sensation."
        di "You're getting bigger!"
        perception "Her body trembles beneath you, her moans growing louder, more desperate, as you pound her ass with relentless force."
        play sound "se_sfx/sex/sex_cum6.mp3"
        scene is_diana_sex_35 with vpunch
        sensation "The warmth and tightness of her rectum finally push you over the edge, and you empty yourself into her ass."
        mc "NGHHHHH! Take it all!"
        play sound "se_sfx/sex/sex_cum8.mp3"
        scene is_diana_sex_35 with vpunch
        di "Nghhh! Fuck, it's so much..."
        scene is_diana_sex_24 with dissolve
        perception "As you slowly pull out, your cum begins to spill from her stretched hole, thick and warm, dripping down on the bed."
        di "My poor ass was {i}not{/i} ready for your size... or your load..."
        di "I'll be feeling this... in my stomach all day long... and I'll love every second of it~"
        scene black with Fade(1.0,0.5,0.5)
        if not mc_diana_scene:
            jump scene05_diana_scene
        perception "Diana stands up, her legs wobbling as if they might give out. Just as she begins to stumble, you step forward and catch her in time."
        $ renpy.end_replay()
        jump diana_sex_end

    elif is_diana_anim_asex1 or is_diana_anim_asex2:
        perception "You thrust deep into Diana's tight hole, preparing to release your seed."
        desire "It doesn't matter where it ends up; the thought of filling her ass is the only thing on your mind."
        play sound "se_sfx/sex/sex_cum4.mp3" 
        scene is_diana_sex_36 with vpunch
        sensation "The relentless heat and tightness of her ass clenching around you is too much to bear. With a groan, you lose control, your hips jerking and unleash your seed deep inside her."
        mc "NGHHHHH!"
        play sound "se_sfx/sex/sex_cum3.mp3" 
        scene is_diana_sex_36 with vpunch
        di "Haaanghh! Fuck, it's so much... I can feel it filling me up!"
        scene is_diana_sex_12 with dissolve
        perception "Hot streams of your semen spill from her as you pull out, leaving a sticky trail that drips down her thighs and pools beneath her."
        di "Ahh... uhh... I can feel it all the way in... so much... you've ruined my ass..."
        di "I'm going to be walking funny for the rest of the day thanks to your huge cock..."
        scene black with Fade(1.0,0.5,0.5)
        $ renpy.end_replay()
        if not mc_diana_scene:
            jump scene05_diana_scene
        perception "Diana stands up, her legs wobbling as if they might give out. Just as she begins to stumble, you step forward and catch her in time."
        jump diana_sex_end

    else:
        mc "I'm gonna fill your greedy tight hole!"
        di "Yes~! Fill me~! Pump your hot load deep inside my slutty ass! Let it leak for days~"
        mc "Here it comes!"
        play sound "se_sfx/sex/sex_cum6.mp3" 
        scene diana_bonus6 with vpunch
        sensation "You slam down to the hilt one last time and explode inside her. Thick, heavy ropes of cum flood deep into her bowels."
        di "Mmmhhh~! Keep cumming... Give me every drop~"
        play sound "se_sfx/sex/sex_cum3.mp3" 
        scene diana_bonus7 with vpunch
        sensation "The sheer volume quickly fills her, and you can feel your own seed being forced back around your cock with every twitch of her overstimulated walls."
        di "Haaah... Fuck... You really flooded me. I can feel it sloshing around inside..."
        play sound "se_sfx/sex/touch3.mp3" 
        scene diana_bonus8 with Dissolve(1.0)
        mc "Hahh... fahhh..."
        di "You really did ruin this hole. I'm going to be feeling you for days... just like I wanted~"
        scene black with Fade(1.0,0.5,0.5)
        $ renpy.end_replay()
        if not mc_diana_scene:
            jump scene05_diana_scene
        perception "Diana stands up, her legs wobbling as if they might give out. Just as she begins to stumble, you step forward and catch her in time."
        jump diana_sex_end

label is_diana_asex_cum_outside:
    if is_diana_anim_asex1 or is_diana_anim_asex2:
        play sound "se_sfx/blowjob/facial7.mp3" 
        scene is_diana_sex_13 with vpunch
        sensation "You withdraw from her ass, the tight ring of her anus clinging to you until the very last moment."
        di "Ahhnn~!"
        perception "Hot ropes of cum erupt from your throbbing cock, splattering across her ass in thick, glistening streaks. Her body arches slightly under the sensation."
        play sound "se_sfx/blowjob/facial2.mp3" 
        scene is_diana_sex_14 with vpunch
        mc "Nghhhh!"
        scene is_diana_sex_15 with dissolve
        di "Hah... Hah... I don't think I'll ever get used to your size..."
        perception "Her anus twitches, struggling to close fully after being stretched so thoroughly, but eventually, she gives up, letting herself remain open and exposed."
        scene black with Fade(1.0,0.5,0.5)
        $ renpy.end_replay()
        if not mc_diana_scene:
            jump scene05_diana_scene
        perception "Diana rises to her feet, her legs shaky, threatening to buckle beneath her. Just as she begins to fall, you step forward, 
        catching her in your arms."
        jump diana_sex_end

    elif is_diana_anim_asex3 or is_diana_anim_asex4:
        play sound "se_sfx/blowjob/facial2.mp3" 
        scene is_diana_sex_25 with vpunch
        sensation "You withdraw from her ass, the tight ring of her anus clinging to you until the very last moment."
        di "Fuck~!"
        perception "Hot ropes of cum erupt from your throbbing cock, splattering across her bare back and cheeks in thick, glistening streaks."
        play sound "se_sfx/blowjob/facial7.mp3" 
        scene is_diana_sex_26 with vpunch
        mc "Nghhhh!"
        scene is_diana_sex_27 with dissolve
        di "Hah... Hah... I don't think I'll ever get used to your size..."
        perception "Her anus twitches, struggling to close fully after being stretched so thoroughly, but eventually, she gives up, letting herself remain open and exposed."
        scene black with Fade(1.0,0.5,0.5)
        if not mc_diana_scene:
            jump scene05_diana_scene
        perception "Diana rises to her feet, her legs shaky, threatening to buckle beneath her. Just as she begins to fall, you step forward, 
        catching her in your arms."
        $ renpy.end_replay()
        jump diana_sex_end

    else:
        play sound "se_sfx/blowjob/facial2.mp3" 
        scene diana_bonus9 with vpunch
        sensation "You withdraw from her ass, the tight ring of her anus clinging to you until the very last moment."
        di "Fuck~!"
        perception "Hot ropes of cum erupt from your throbbing cock, splattering across her bare back and cheeks in thick, glistening streaks."
        play sound "se_sfx/blowjob/facial7.mp3" 
        scene diana_bonus10 with vpunch
        mc "Nghhhh!"
        di "Hah... Hah... I don't think I'll ever get used to your size..."
        perception "Her anus twitches, struggling to close fully after being stretched so thoroughly, but eventually, she gives up, letting herself remain open and exposed."
        scene black with Fade(1.0,0.5,0.5)
        if not mc_diana_scene:
            jump scene05_diana_scene
        perception "Diana rises to her feet, her legs shaky, threatening to buckle beneath her. Just as she begins to fall, you step forward, 
        catching her in your arms."
        $ renpy.end_replay()
        jump diana_sex_end

#MAIA IS SCENES #####################################################################################################################################
#####################################################################################################################################################
#####################################################################################################################################################
#####################################################################################################################################################
#####################################################################################################################################################
image is_maia_anim_hj1 = Movie(play="images/is_scenes/maia/is_maia_hj/anims/is_maia_anims_hj1.webm", loop=True)
image is_maia_anim_hj2 = Movie(play="images/is_scenes/maia/is_maia_hj/anims/is_maia_anims_hj2.webm", loop=True)

image is_maia_anim_hj1_faster = Movie(play="images/is_scenes/maia/is_maia_hj/anims/is_maia_anims_hj1_faster.webm", loop=True)
image is_maia_anim_hj2_faster = Movie(play="images/is_scenes/maia/is_maia_hj/anims/is_maia_anims_hj2_faster.webm", loop=True)

image is_maia_anim_hj1_preg = Movie(play="images/is_scenes/maia/is_maia_hj/anims/is_maia_anims_hj1_preg.webm", loop=True)
image is_maia_anim_hj1_preg_faster = Movie(play="images/is_scenes/maia/is_maia_hj/anims/is_maia_anims_hj1_preg_faster.webm", loop=True)

default maia_hj_pos_toggle = True
default maia_hj_pov_toggle = True
default is_maia_anim_hj1 = True
default is_maia_anim_hj2 = False
default is_maia_anim_hj3 = False

default maia_hj = False
default maia_tj = False
default maia_bj = False
default maia_sj = False
default maia_fj = False

screen is_maia_hj_controls():
    imagebutton auto "main_choices_op1_%s":
        focus_mask True
        action Jump("is_maia_hj_faster")
    text "Faster":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 832 xanchor 0.5 yanchor 0.5 italic True
    
    imagebutton auto "main_choices_op2_%s":
        focus_mask True
        action [
            ToggleVariable("maia_hj_pos_toggle"), 
            If(maia_hj_pos_toggle, Jump("is_maia_hj_pos2_pre"), Jump("is_maia_hj_pov1"))
        ]
    text "Change position":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 959 xanchor 0.5 yanchor 0.5 italic True

    imagebutton auto "main_choices_op3_%s":
        focus_mask True
        action Jump("is_maia_hj_cum")
    text "Cum":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 1086 xanchor 0.5 yanchor 0.5 italic True

screen is_maia_hj_choice3():
    imagebutton auto "main_choices_op1_%s":
        focus_mask True
        action Jump("is_maia_hj_cumface")
    text "Cum on face":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 832 xanchor 0.5 yanchor 0.5 italic True
    
    imagebutton auto "main_choices_op2_%s":
        focus_mask True
        action Jump("is_maia_hj_cumbreast")
    text "Cum on breasts":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 959 xanchor 0.5 yanchor 0.5 italic True

screen is_maia_hj2_choice():
    imagebutton auto "main_choices_op1_%s":
        focus_mask True
        action Return()
    text "\"(Yes!)\"":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 832 xanchor 0.5 yanchor 0.5
    
    imagebutton auto "main_choices_op2_%s":
        focus_mask True
        action Jump("is_maia_hj_pov1")
    text "\"(Hell no!)\"":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 959 xanchor 0.5 yanchor 0.5

label is_maia_hj1:
    $ maia_virgin = False
    $ mcname = persistent.name
    if persistent.name == "None" or mcname == "None":
        while mcname == "None" or mcname == "":
            $ mcname = renpy.input("There was an issue with your name. Please rewrite your name:", length=32)
        $ persistent.name = mcname
    if not persistent.scene3_p2_replay:
        $ persistent.scene3_p2_replay = True
    stop music fadeout 3.0
    $ maia_hj = True
    $ is_maia_anim_hj1 = True
    $ is_maia_anim_hj2 = False
    $ is_maia_anim_hj3 = False
    $ maia_hj_pov_toggle = True
    $ maia_hj_pos_toggle = True

    scene 18_s8 with dissolve
    if cycle == 0:
        m "You don't need to ask, [mx]~"
    elif cycle == 1:
        m "A h-handjob? A-as you wish, [mx]! I'll make sure it feels amazing~"
    elif cycle == 2:
        m "Y-yes~"
    elif cycle == 3:
        m "Of course, [mx]!"
    #"[cycle]"
    scene 18_s7 with dissolve
    scene black with Fade(1.0,0.5,0.5)
    jump is_maia_hj2

label is_maia_hj2:
    stop music fadeout 2.0
    sensation "Maia's soft fingers wrap around your shaft, her grip teasingly loose at first before tightening with a sultry rhythm."
    if maia_pregnant and maia_pregnancy_timer >= pregnancy_time // 2:
        show is_maia_anim_hj1_preg with dissolve
    else:
        show is_maia_anim_hj1 with dissolve
    if cycle == 0:
        m "When you're close... Just let it out, don't worry about telling me~"
    elif cycle == 1:
        m "Should I go faster? Or do you like it slow?"
    elif cycle == 2:
        m "Don't worry, [mx]... I'll take care of you. Just relax and let me handle everything~"
    elif cycle == 3:
        m "I love making you feel good, [mx]~"
    call screen is_maia_hj_controls with dissolve

label is_maia_hj_pov1:
    $ is_maia_anim_hj1 = True
    $ is_maia_anim_hj2 = False
    $ maia_hj_pov_toggle = True
    $ maia_hj_pos_toggle = True
    if maia_pregnant and maia_pregnancy_timer >= pregnancy_time // 2:
        scene black with Dissolve(0.1)
        show is_maia_anim_hj1_preg
    else:
        scene black with Dissolve(0.3)
        show is_maia_anim_hj1 with dissolve
    call screen is_maia_hj_controls with dissolve

default is_maia_pos2_first = True
label is_maia_hj_pos2_pre:
    if is_maia_pos2_first:
        mc "(Should I tell her to put her feet on my face?)"
        call screen is_maia_hj2_choice with dissolve
        mc "I want to lick your feet while you jerk me off."
        if maia_pregnant and maia_pregnancy_timer >= pregnancy_time // 2:
            scene is_maia_hj3_preg with dissolve
            m "M-my feet? A-are you sure, [mx]?"
            scene is_maia_hj4_preg with dissolve
            mc "Yes. I want to feel those soft soles against my face while I cum."
            scene is_maia_hj1_preg with dissolve
            m "I-If that's what you want, [mx]... then I'll gladly do it."
            scene is_maia_hj2_preg with dissolve
        else:
            scene is_maia_hj3 with dissolve
            m "M-my feet? A-are you sure, [mx]?"
            scene is_maia_hj4 with dissolve
            mc "Yes. I want to feel those soft soles against my face while I cum."
            scene is_maia_hj1 with dissolve
            m "I-If that's what you want, [mx]... then I'll gladly do it."
            scene is_maia_hj2 with dissolve
        $ is_maia_pos2_first = False
        jump is_maia_hj_pos2
    else:
        mc "Your feet, my face. Now."
        m "Hehe~"
        jump is_maia_hj_pos2

label is_maia_hj_pos2:
    scene black with Fade(0.5,0.5,0.5)
    $ is_maia_anim_hj1 = False
    $ is_maia_anim_hj2 = True
    scene black with Dissolve(0.3)
    show is_maia_anim_hj2 with dissolve
    if cycle == 0:
        m "D-Do you really enjoy licking my feet, [mx]?"
        mc "Mhmm..."
    elif cycle == 1:
        m "Hehe~ I never knew you liked my feet this much, [mx]..."
        m "I'll be sure to keep them extra soft and clean just for you~"
    elif cycle == 2:
        m "A-Are you comfortable like this?"
        mc "Don't worry about me... Just smother my face with them."
    elif cycle == 3:
        m "Ah~ Your tongue... it tickles! Hehe~"
    call screen is_maia_hj_controls with dissolve

label is_maia_hj_faster:
    scene black with Dissolve(0.3)
    if is_maia_anim_hj1:
        if maia_pregnant and maia_pregnancy_timer >= pregnancy_time // 2:
            show is_maia_anim_hj1_preg_faster with dissolve
            hide is_maia_anim_hj1_preg with dissolve
            m "Please don't hold back, [mx]~"
        else:
            show is_maia_anim_hj1_faster with dissolve
            hide is_maia_anim_hj1 with dissolve
            m "Please don't hold back, [mx]~"
        call screen is_maia_hj_controls with dissolve
    elif is_maia_anim_hj2:
        show is_maia_anim_hj2_faster with dissolve
        hide is_maia_anim_hj2 with dissolve
        m "D-do my feet taste good, [mx]?"
        call screen is_maia_hj_controls with dissolve

label is_maia_hj_cum:
    if is_maia_anim_hj1:
        call screen is_maia_hj_choice3 with dissolve
    else:
        mc "Your feet are gonna make me cum!"
        m "Go ahead, [mx]~ Let it all out~"
        play sound "se_sfx/blowjob/facial3.mp3" 
        scene is_maia_hj13 with vpunch
        mc "{i}Hnnggggg!!{/i}"
        play sound "se_sfx/blowjob/facial4.mp3" 
        scene is_maia_hj14 with vpunch
        m "{i}Uh~{/i}"
        scene is_maia_hj15 with dissolve
        m "My hand is so wet from your seed... D-Did you enjoy it, [mx]?"
        scene is_maia_hj16 with dissolve
        mc "Mhmm. Keep those feet in top shape. Next time, I might want to cover them instead."
        scene is_maia_hj15 with dissolve
        m "O-Of course, [mx]! I'll take good care of them~"
        scene is_maia_hj16 with dissolve
        scene black with Fade(1.0,0.5,0.5)
        perception "Maia wipes off your cum and tidies herself up."
    $ renpy.end_replay()
    if in_scene18:
        jump scene19
    else:
        jump maia_sex_end

label is_maia_hj_cumface:
    mc "Come closer. I want to mark your pretty face."
    if maia_pregnant and maia_pregnancy_timer >= pregnancy_time // 2:
        scene is_maia_hj3_preg with dissolve
        m "Huh? Oh! O-Of course... please, [mx]~"
        #play sound "se_sfx/blowjob/facial3.mp3" 
        scene is_maia_hj7_preg with vpunch
        mc "{i}Ahhhh!{/i}"
        #play sound "se_sfx/blowjob/facial4.mp3" 
        scene is_maia_hj8_preg with vpunch
        m "{i}Hah!{/i}"
        scene is_maia_hj9_preg with dissolve
        m "{i}*Sniff*{/i} Some of it... went up my nose..."
        scene is_maia_hj10_preg with dissolve
        mc "What do you say, Maia?"
        scene is_maia_hj9_preg with dissolve
        m "What do I—Oh! T-Thank you for cumming on my face, [mx]!"
        scene is_maia_hj10_preg with dissolve
        mc "Good girl."
    else:
        scene is_maia_hj3 with dissolve
        m "Huh? Oh! O-Of course... please, [mx]~"
        play sound "se_sfx/blowjob/facial4.mp3" 
        scene is_maia_hj7 with vpunch
        mc "{i}Ahhhh!{/i}"
        play sound "se_sfx/blowjob/facial3.mp3" 
        scene is_maia_hj8 with vpunch
        m "{i}Hah!{/i}"
        scene is_maia_hj9 with dissolve
        m "{i}*Sniff*{/i} Some of it... went up my nose..."
        scene is_maia_hj10 with dissolve
        mc "What do you say, Maia?"
        scene is_maia_hj9 with dissolve
        m "What do I—Oh! T-Thank you for cumming on my face, [mx]!"
        scene is_maia_hj10 with dissolve
        mc "Good girl."
    scene black with Fade(1.0,0.5,0.5)
    perception "Maia wipes off your cum and fixes her appearance before getting dressed."
    $ renpy.end_replay()
    if in_scene18:
        jump scene19
    else:
        jump maia_sex_end

label is_maia_hj_cumbreast:
    mc "I wanna mark those milk jugs of yours."
    if maia_pregnant and maia_pregnancy_timer >= pregnancy_time // 2:
        scene is_maia_hj3_preg with dissolve
        m "M-Milk jugs...?"
        scene is_maia_hj5_preg with vpunch
        mc "{i}Ahhhh!{/i}"
        scene is_maia_hj6_preg with vpunch
        m "{i}Aah~{/i} It's so hot..."
        scene is_maia_hj17_preg with dissolve
        m "My breasts are completely covered with your seed, [mx]..."
        scene is_maia_hj18_preg with dissolve
        mc "Don't they look even more beautiful like that?"
        scene is_maia_hj17_preg with dissolve
        m "I... I think? I-I mean yes! They do, [mx]!"
        scene is_maia_hj18_preg with dissolve
    else:
        scene is_maia_hj3 with dissolve
        m "M-Milk jugs...?"
        play sound "se_sfx/blowjob/facial4.mp3" 
        scene is_maia_hj5 with vpunch
        mc "{i}Ahhhh!{/i}"
        play sound "se_sfx/blowjob/facial3.mp3" 
        scene is_maia_hj6 with vpunch
        m "{i}Aah~{/i} It's so hot..."
        scene is_maia_hj17 with dissolve
        m "My breasts are completely covered with your seed, [mx]..."
        scene is_maia_hj18 with dissolve
        mc "Don't they look even more beautiful like that?"
        scene is_maia_hj17 with dissolve
        m "I... I think? I-I mean yes! They do, [mx]!"
        scene is_maia_hj18 with dissolve
    mc "Good girl."
    scene black with Fade(1.0,0.5,0.5)
    perception "Maia wipes off your cum, looking a little flustered as she does."
    $ renpy.end_replay()
    if in_scene18:
        jump scene19
    else:
        jump maia_sex_end

###########################################################TITJOB####################################################################################
#####################################################################################################################################################
image is_maia_anim_tj1 = Movie(play="images/is_scenes/maia/is_maia_tj/anims/is_maia_anims_tj1.webm", loop=True)
image is_maia_anim_tj2 = Movie(play="images/is_scenes/maia/is_maia_tj/anims/is_maia_anims_tj2.webm", loop=True)

image is_maia_anim_tj1_faster = Movie(play="images/is_scenes/maia/is_maia_tj/anims/is_maia_anims_tj1_faster.webm", loop=True)
image is_maia_anim_tj2_faster = Movie(play="images/is_scenes/maia/is_maia_tj/anims/is_maia_anims_tj2_faster.webm", loop=True)

image is_maia_anim_tj2_preg = Movie(play="images/is_scenes/maia/is_maia_tj/anims/is_maia_anims_tj2_preg.webm", loop=True)
image is_maia_anim_tj2_preg_faster = Movie(play="images/is_scenes/maia/is_maia_tj/anims/is_maia_anims_tj2_preg_faster.webm", loop=True)

default is_maia_anim_tj1 = True
default is_maia_anim_tj2 = False
default is_maia_anim_tj3 = False
default maia_tj_pov_toggle = True
default maia_tj_pos_toggle = True

screen is_maia_tj_controls():
    imagebutton auto "main_choices_op1_%s":
        focus_mask True
        action Jump("is_maia_tj_faster")
    text "Faster":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 832 xanchor 0.5 yanchor 0.5 italic True

    imagebutton auto "main_choices_op2_%s":
        focus_mask True
        action [
            ToggleVariable("maia_tj_pos_toggle"), 
            If(maia_tj_pos_toggle, Jump("is_maia_tj_pos2"), Jump("is_maia_tj_pov1"))
        ]
    text "Change position":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 959 xanchor 0.5 yanchor 0.5 italic True

    imagebutton auto "main_choices_op3_%s":
        focus_mask True
        action Jump("is_maia_tj_cum")
    text "Cum":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 1086 xanchor 0.5 yanchor 0.5 italic True

label is_maia_tj1:
    $ maia_virgin = False
    $ mcname = persistent.name
    if persistent.name == "None" or mcname == "None":
        while mcname == "None" or mcname == "":
            $ mcname = renpy.input("There was an issue with your name. Please rewrite your name:", length=32)
        $ persistent.name = mcname
    if not persistent.scene4_p2_replay:
        $ persistent.scene4_p2_replay = True
    stop music fadeout 3.0
    $ maia_tj = True
    $ is_maia_anim_tj1 = True
    $ is_maia_anim_tj2 = False
    $ maia_tj_pov_toggle = True
    $ maia_tj_pos_toggle = True

    scene 18_s8 with dissolve
    if cycle == 0:
        m "Y-You want to use my breasts like that...?"
    elif cycle == 1:
        m "As you wish, [mx]~"
    elif cycle == 2:
        m "O-Of course, [mx]! Let me warm you up between them~"
    elif cycle == 3:
        m "I'll make sure to squeeze nice and tight~"
    scene 18_s7 with dissolve
    scene black with Fade(1.0,0.5,0.5)
    jump is_maia_tj2

label is_maia_tj2:
    sensation "Maia kneels before you, pressing her soft, warm mounds together, enveloping your cock in their pillowy embrace."
    show is_maia_anim_tj1 with dissolve
    if cycle == 0:
        m "S-so thick and hard~ I'll be sure to make it feel better, [mx]~"
    elif cycle == 1:
        m "I love feeling you throb between my breasts, [mx]~"
    elif cycle == 2:
        m "Just relax, [mx]~ I'll service you properly with my breasts."
    elif cycle == 3:
        m "{i}Mmm~{/i} Your warmth is spreading all over me... should I go faster?"
    call screen is_maia_tj_controls with dissolve

label is_maia_tj_pov1:
    $ is_maia_anim_tj1 = True
    $ is_maia_anim_tj2 = False
    $ maia_tj_pov_toggle = True
    $ maia_tj_pos_toggle = True
    scene black with Dissolve(0.3)
    show is_maia_anim_tj1 with dissolve
    call screen is_maia_tj_controls with dissolve

label is_maia_tj_pos2:
    $ is_maia_anim_tj1 = False
    $ is_maia_anim_tj2 = True
    scene black with Dissolve(0.3)
    if maia_pregnant and maia_pregnancy_timer >= pregnancy_time // 2:
        show is_maia_anim_tj2_preg with dissolve
    else:
        show is_maia_anim_tj2 with dissolve
    call screen is_maia_tj_controls with dissolve

label is_maia_tj_faster:
    scene black with Dissolve(0.3)
    if is_maia_anim_tj1:
        show is_maia_anim_tj1_faster with dissolve
        hide is_maia_anim_tj1 with dissolve
        m "I-I can feel it throbbing more... Are you ready, [mx]?"
    elif is_maia_anim_tj2:
        if maia_pregnant and maia_pregnancy_timer >= pregnancy_time // 2:
            show is_maia_anim_tj2_preg_faster with dissolve
            hide is_maia_anim_tj2_preg with dissolve
            m "T-This position makes it look like you're having sex with my breasts~"
        else:
            show is_maia_anim_tj2_faster with dissolve
            hide is_maia_anim_tj2 with dissolve
            m "T-This position makes it look like you're having s-sex with my breasts~"
    call screen is_maia_tj_controls with dissolve

label is_maia_tj_cum:
    if is_maia_anim_tj1:
        mc "I'm close... Maia, squeeze them tighter!"
        play sound "se_sfx/blowjob/facial3.mp3" 
        scene is_maia_tj3 with vpunch
        mc "{i}Aaaahhh!!{/i}"
        play sound "se_sfx/blowjob/facial5.mp3" 
        scene is_maia_tj4 with vpunch
        m "{i}Mmm~{/i} So much, [mx]..."
        scene is_maia_tj5 with dissolve
        m "Your warm seed is all over my breasts... It's dripping down..."
        scene is_maia_tj6 with dissolve
        mc "God... Your breasts were made for this."
        scene is_maia_tj5 with dissolve
        m "A-am I really that good?"
        scene is_maia_tj6 with dissolve
        mc "Mhm."
        scene is_maia_tj5 with dissolve
        m "T-then I'll keep making you feel good, [mx]~"
        scene is_maia_tj6 with dissolve
    else:
        if maia_pregnant and maia_pregnancy_timer >= pregnancy_time // 2:
            mc "I'm cumming!"
            m "D-don't hold back, [mx]. Fill my breasts~"
            play sound "se_sfx/blowjob/facial2.mp3" 
            scene is_maia_tj7_preg with vpunch
            mc "{i}Hnnggggg!!{/i}"
            play sound "se_sfx/blowjob/facial3.mp3" 
            scene is_maia_tj7_preg with vpunch
            m "{i}Uh~{/i}"
            scene is_maia_tj9_preg with dissolve
            m "{i}Ahh~{/i} It's so hot..."
            m  "And y-your scent... [mx]... Do you like seeing me like this?"
            scene is_maia_tj10_preg with dissolve
            mc "Seeing you like what? Covered with my cum? Yeah, absolutely."
            m "Mhmm~"
        else:
            mc "I'm cumming!"
            m "D-don't hold back, [mx]. Fill my breasts~"
            play sound "se_sfx/blowjob/facial2.mp3" 
            scene is_maia_tj7 with vpunch
            mc "{i}Hnnggggg!!{/i}"
            play sound "se_sfx/blowjob/facial4.mp3" 
            scene is_maia_tj7 with vpunch
            m "{i}Uh~{/i}"
            scene is_maia_tj9 with dissolve
            m "{i}Ahh~{/i} It's so hot..."
            m  "And y-your scent... [mx]... Do you like seeing me like this?"
            scene is_maia_tj10 with dissolve
            mc "Seeing you like what? Covered with my cum? Yeah, absolutely."
            m "Mhmm~"
    scene black with Fade(1.0,0.5,0.5)
    perception "Maia scoops up the dripping cum from her chest, glancing at you with a flushed face before wiping herself clean."
    $ renpy.end_replay()
    if in_scene18:
        jump scene19
    else:
        jump maia_sex_end

#############################################BJ#######################################################
#############################################BJ#######################################################
#############################################BJ#######################################################
image is_maia_anim_bj1 = Movie(play="images/is_scenes/maia/is_maia_bj/anims/is_maia_anim_bj1.webm", loop=True)
image is_maia_anim_bj2 = Movie(play="images/is_scenes/maia/is_maia_bj/anims/is_maia_anim_bj2.webm", loop=True)
image is_maia_anim_bj3 = Movie(play="images/is_scenes/maia/is_maia_bj/anims/is_maia_anim_bj3.webm", loop=True)
image is_maia_anim_bj4 = Movie(play="images/is_scenes/maia/is_maia_bj/anims/is_maia_anim_bj4.webm", loop=True)

image is_maia_anim_bj1_faster = Movie(play="images/is_scenes/maia/is_maia_bj/anims/is_maia_anim_bj1_faster.webm", loop=True)
image is_maia_anim_bj2_faster = Movie(play="images/is_scenes/maia/is_maia_bj/anims/is_maia_anim_bj2_faster.webm", loop=True)
image is_maia_anim_bj3_faster = Movie(play="images/is_scenes/maia/is_maia_bj/anims/is_maia_anim_bj3_faster.webm", loop=True)
image is_maia_anim_bj4_faster = Movie(play="images/is_scenes/maia/is_maia_bj/anims/is_maia_anim_bj4_faster.webm", loop=True)

default is_maia_anim_bj1 = True
default is_maia_anim_bj2 = False
default is_maia_anim_bj3 = False
default maia_bj_pov_toggle = True
default maia_bj_pos_toggle = True

default is_maia_bj2_first = True
default is_maia_bj3_first = True

default is_maia_bj3_second = False

screen is_maia_bj_choice01():
    imagebutton auto "main_choices_op1_%s":
        focus_mask True
        action Jump("is_maia_bj_faster")
    text "Faster":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 832 xanchor 0.5 yanchor 0.5 italic True
    
    if not is_maia_anim_bj1:
        imagebutton auto "main_choices_op2_%s":
            focus_mask True
            action Jump("is_maia_bj1")
        text "Regular blowjob":
            size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 959 xanchor 0.5 yanchor 0.5 italic True
    else:
        add "main_choices_op2_idle"
        text "Regular blowjob":
            size persistent.choices_text_size color "#818181" font "candara.ttf" xpos 2260 ypos 959 xanchor 0.5 yanchor 0.5 italic True
    
    if not is_maia_anim_bj2:
        imagebutton auto "main_choices_op3_%s":
            focus_mask True
            action Jump("is_maia_bj2")
        text "Deepthroat":
            size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 1086 xanchor 0.5 yanchor 0.5 italic True
    else:
        add "main_choices_op3_idle"
        text "Deepthroat":
            size persistent.choices_text_size color "#818181" font "candara.ttf" xpos 2260 ypos 1086 xanchor 0.5 yanchor 0.5 italic True

    if not is_maia_anim_bj3:
        imagebutton auto "main_choices_op4_%s":
            focus_mask True
            action Jump("is_maia_bj3")
        text "69":
            size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 1214 xanchor 0.5 yanchor 0.5 italic True
    else:
        add "main_choices_op4_idle"
        text "69":
            size persistent.choices_text_size color "#818181" font "candara.ttf" xpos 2260 ypos 1214 xanchor 0.5 yanchor 0.5 italic True

    imagebutton auto "main_choices_op5_%s":
        focus_mask True
        action Jump("is_maia_bj_cum")
    text "Cum":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 1340 xanchor 0.5 yanchor 0.5 italic True

screen is_maia_bj_choice02():
    imagebutton auto "main_choices_op1_%s":
        focus_mask True
        action Jump("is_maia_bj_cum_inside")
    text "Cum inside":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 832 xanchor 0.5 yanchor 0.5 italic True
    
    imagebutton auto "main_choices_op2_%s":
        focus_mask True
        action Jump("is_maia_bj_cum_outside")
    text "Cum inside":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 959 xanchor 0.5 yanchor 0.5 italic True

label is_maia_bj:
    $ maia_mouth_virgin = False
    $ maia_virgin = False
    $ mcname = persistent.name
    if persistent.name == "None" or mcname == "None":
        while mcname == "None" or mcname == "":
            $ mcname = renpy.input("There was an issue with your name. Please rewrite your name:", length=32)
        $ persistent.name = mcname
    if not persistent.scene5_p2_replay:
        $ persistent.scene5_p2_replay = True
    stop music fadeout 3.0
    $ maia_bj = True
    scene 18_s8 with dissolve
    if cycle == 0:
        m "I'll be happy to give you one, [mx]! Just lay back and relax."
    elif cycle == 1:
        m "Of course, [mx]."
    elif cycle == 2:
        m "Do you like it when I lick it, [mx]?"
    elif cycle == 3:
        m "I would be happy to service you with my mouth, [mx]."
    scene 18_s7 with dissolve
    $ is_maia_anim_bj1 = True
    $ is_maia_anim_bj2 = False
    $ is_maia_anim_bj3 = False
    $ is_maia_bj2_first = True
    #bj1
    if not is_maia_bj3_first:
        $ is_maia_bj3_second = True
    scene is_maia_bj3 with Fade(0.5,0.5,0.5)
    perception "Maia sinks to her knees before you, fingers trembling slightly as she undoes your pants revealing your cock. She leans in, wrapping her lips around you with eager devotion."
    scene is_maia_bj4 with dissolve
    sensation "Her warm, wet mouth envelopes you, tongue swirling tentatively at first before she grows more confident."
    show is_maia_anim_bj1 with dissolve
    m "Mfhmmm."
    mc "Good girl... You're getting better at this."
    m "Mhmmm~"
    call screen is_maia_bj_choice01 with dissolve

label is_maia_bj1:
    $ is_maia_anim_bj1 = True
    $ is_maia_anim_bj2 = False
    $ is_maia_anim_bj3 = False
    scene black with Dissolve(0.3)
    show is_maia_anim_bj1 with dissolve
    call screen is_maia_bj_choice01 with dissolve

label is_maia_bj2:
    $ is_maia_anim_bj1 = False
    $ is_maia_anim_bj2 = True
    $ is_maia_anim_bj3 = False
    if is_maia_bj2_first:
        mc "Try to go all the way down."
        scene black with Dissolve(0.3)
        show is_maia_anim_bj2 with dissolve
        sensation "She hesitates for just a moment before obediently complying, sinking deeper until you feel the tight embrace of her wet and slimy throat constrict around your cock."
        mc "Yeah, just like that."
        m "*gag* Mfhmmm..."
        $ is_maia_bj2_first = False
        call screen is_maia_bj_choice01 with dissolve
    else:
        scene black with Dissolve(0.3)
        show is_maia_anim_bj2 with dissolve
        m "*gag* Mfhmmm..."
        call screen is_maia_bj_choice01 with dissolve

label is_maia_bj3:
    $ is_maia_anim_bj1 = False
    $ is_maia_anim_bj2 = False
    $ is_maia_anim_bj3 = True
    if is_maia_bj3_first:
        mc "Get on top of me. I want to make you feel good too."
        scene is_maia_bj1 with dissolve
        m "Y-You don't have to, [mx]... I feel good w-whenever you feel good..."
        scene is_maia_bj0 with dissolve
        mc "Come on. I insist."
        scene is_maia_bj1 with dissolve
        m "Yes~"
        scene is_maia_bj0 with dissolve
        scene black with Fade(0.5,0.5,0.5)
        perception "She climbs on top of you, her soft thighs straddling your body. Her glistening folds are on full display, her breath hitching as you grip her hips and pull her closer."
        scene is_maia_bj17 with dissolve
        perception "Wasting no time, you lean in, your tongue running along her sensitive clit. A sharp gasp leaves her lips, her whole body trembling at the sensation."
        m "[mx]..."
        mc "Yeah?"
        m "C-Can you... keep doing it?"
        mc "Doing what?"
        m "Licking me... D-Down there~"
        mc "Oh? Don't mind if I do."
        scene black with Dissolve(0.3)
        show is_maia_anim_bj4 with dissolve
        m "Nhnn~"
        $ is_maia_bj3_first = False
        scene black with Dissolve(0.3)
        show is_maia_anim_bj3 with dissolve
        call screen is_maia_bj_choice01 with dissolve

    elif is_maia_bj3_second:
        mc "Get on top of me. I want to make you feel good too."
        scene is_maia_bj1 with dissolve
        m "W-Will you... lick me down there like last time, [mx]?"
        scene is_maia_bj0 with dissolve
        scene black with Dissolve(0.3)
        show is_maia_anim_bj4 with dissolve
        ""
        scene black with Dissolve(0.3)
        show is_maia_anim_bj3 with dissolve
        call screen is_maia_bj_choice01 with dissolve

    else:
        scene black with Dissolve(0.3)
        show is_maia_anim_bj4 with dissolve
        ""
        scene black with Dissolve(0.3)
        show is_maia_anim_bj3 with dissolve
        call screen is_maia_bj_choice01 with dissolve

label is_maia_bj_faster:
    scene black with Dissolve(0.3)
    if is_maia_anim_bj1:
        show is_maia_anim_bj1_faster with dissolve
        hide is_maia_anim_bj1 with dissolve
        m "Nhnnn..."
        call screen is_maia_bj_choice01 with dissolve
    elif is_maia_anim_bj2:
        show is_maia_anim_bj2_faster with dissolve
        hide is_maia_anim_bj2 with dissolve
        m "*gulk* *gag* Nhnnn!"
        perception "Saliva dribbles down her chin as she takes you deeper, her throat tightening as she struggles to take more of you. A desperate gag escapes her, but she doesn't pull away."
        call screen is_maia_bj_choice01 with dissolve
    elif is_maia_anim_bj3:
        show is_maia_anim_bj4_faster with dissolve
        hide is_maia_anim_bj4 with dissolve
        m "Ah~ Mghmmm~"
        scene black with Dissolve(0.3)
        show is_maia_anim_bj3_faster with dissolve
        call screen is_maia_bj_choice01 with dissolve

label is_maia_bj_cum:
    mc "I'm cumming!"
    if is_maia_anim_bj1 or is_maia_anim_bj2:
        call screen is_maia_bj_choice02 with dissolve
    elif is_maia_anim_bj3:
        m "Mghmmm~"
        sensation "Her throat tightens even further, eagerly awaiting your release."
        play sound "se_sfx/blowjob/blowjob_cum1.mp3" 
        scene is_maia_bj14 with vpunch
        mc "Hnnngg!"
        play sound "se_sfx/blowjob/facial4.mp3" 
        scene is_maia_bj14 with vpunch
        perception "Maia's body shudders with every spurt, her hands gripping the bed as she takes it all."
        scene is_maia_bj15 with dissolve
        m "Sho mush..."
        scene is_maia_bj16 with dissolve
        play sound "se_sfx/blowjob/swallow1.mp3" 
        m "*gulp* *gulp*"
        scene is_maia_bj17 with dissolve
        mc "Good girl."
        m "Thank you for making me feel good too, [mx]!"
        scene black with Fade(0.5,0.5,0.5)
        perception "Maia stands up, her expression warm as she helps you dress, a satisfied glow on her flushed face."
    $ renpy.end_replay()
    if in_scene18:
        jump scene19
    else:
        jump maia_sex_end

label is_maia_bj_cum_inside:
    if is_maia_anim_bj1:
        m "Mghmmm~"
        sensation "Her throat tightens even further, eagerly awaiting your release."
        play sound "se_sfx/blowjob/blowjob_cum1.mp3" 
        scene is_maia_bj5 with vpunch
        mc "Hnnngg!"
        play sound "se_sfx/blowjob/facial4.mp3" 
        scene is_maia_bj5 with vpunch
        perception "Maia jolts with each pulse of your release, swallowing hungrily as a muffled moan vibrates around you."
        mc "Show me your hard work."
        scene is_maia_bj6 with dissolve
        m "Ahhhhnn~"
        scene is_maia_bj7 with dissolve
        play sound "se_sfx/blowjob/swallow1.mp3" 
        m "*gulp* *gulp*"
        scene is_maia_bj8 with dissolve
        mc "Good girl."
        m "Mmm~ Thank you for the delicious semen, [mx]!"
        scene black with Fade(0.5,0.5,0.5)
        perception "Maia wipes the corner of her lips before standing up, gently helping you dress as a soft blush lingers on her cheeks."

    elif is_maia_anim_bj2:
        m "Nghmmmm!"
        play sound "se_sfx/blowjob/blowjob_cum1.mp3" 
        scene is_maia_bj13 with vpunch
        perception "You grip the back of her head, pushing her down. The moment you explode deep in her throat, Maia gags around you, her fingers clenching against your legs."
        play sound "se_sfx/blowjob/gag1.mp3" 
        scene is_maia_bj13 with vpunch
        mc "*gulk* *gag*!"
        scene is_maia_bj7 with dissolve
        mc "Hah... hah..."
        scene is_maia_bj6 with dissolve
        m "I caught et shis time, [mx]! Shee?"
        mc "Good job."
        scene is_maia_bj7 with dissolve
        play sound "se_sfx/blowjob/swallow1.mp3" 
        m "*gulp* *gulp*"
        scene is_maia_bj8 with dissolve
        m "Ahhhhh~ I'm getting used to your taste, [mx]... I-I kinda love it..."
        scene black with Fade(0.5,0.5,0.5)
        perception "She stands up, helping you dress, her fingers lingering just a little longer than necessary as she bites her lip."
    $ renpy.end_replay()
    if in_scene18:
        jump scene19
    else:
        jump maia_sex_end

label is_maia_bj_cum_outside:
    mc "I wanna cover your face!"
    play sound "se_sfx/blowjob/facial3.mp3" 
    scene is_maia_bj9 with vpunch
    perception "Maia pulls away, her lips wet and slightly swollen, before positioning your throbbing cock right in front of her flushed face."
    mc "Ahgnnn!"
    play sound "se_sfx/blowjob/facial4.mp3" 
    scene is_maia_bj10 with vpunch
    m "Mmmmm~"
    scene is_maia_bj11 with dissolve
    m "I love having your seed on my face, [mx]~"
    scene is_maia_bj12 with dissolve
    scene black with Fade(0.5,0.5,0.5)
    perception "She lingers for a moment, savoring the sensation before finally wiping herself off, a dazed, satisfied look still present as she helps you dress."
    $ renpy.end_replay()
    if in_scene18:
        jump scene19
    else:
        jump maia_sex_end

#############################################SEX#######################################################
#############################################SEX#######################################################
#############################################SEX#######################################################
image is_maia_anim_vsex1 = Movie(play="images/is_scenes/maia/is_maia_sex/anims/is_maia_anim_vsex1.webm", loop=True)
image is_maia_anim_vsex2 = Movie(play="images/is_scenes/maia/is_maia_sex/anims/is_maia_anim_vsex2.webm", loop=True)

image is_maia_anim_asex1 = Movie(play="images/is_scenes/maia/is_maia_sex/anims/is_maia_anim_asex1.webm", loop=True)
image is_maia_anim_asex2 = Movie(play="images/is_scenes/maia/is_maia_sex/anims/is_maia_anim_asex2.webm", loop=True)

image is_maia_anim_vsex1_faster = Movie(play="images/is_scenes/maia/is_maia_sex/anims/is_maia_anim_vsex1_faster.webm", loop=True)
image is_maia_anim_vsex2_faster = Movie(play="images/is_scenes/maia/is_maia_sex/anims/is_maia_anim_vsex2_faster.webm", loop=True)

image is_maia_anim_asex1_faster = Movie(play="images/is_scenes/maia/is_maia_sex/anims/is_maia_anim_asex1_faster.webm", loop=True)
image is_maia_anim_asex2_faster = Movie(play="images/is_scenes/maia/is_maia_sex/anims/is_maia_anim_asex2_faster.webm", loop=True)

default is_maia_anim_vsex1 = True
default is_maia_anim_vsex2 = False
#default is_maia_anim_vsex3 = False

default maia_sex_pov_toggle = True
default maia_sex_pos_toggle = True
####
default is_maia_anim_asex1 = False
default is_maia_anim_asex2 = False
#default is_maia_anim_asex3 = False

#default maia_asex_pov_toggle = True
#default maia_asex_pos_toggle = True

default is_maia_anim_sex2_first = True
default is_maia_asex_first = True
screen is_maia_sex_sex1():
    imagebutton auto "main_choices_op1_%s":
        focus_mask True
        action Jump("is_maia_sex_faster")
    text "Faster":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 832 xanchor 0.5 yanchor 0.5 italic True
    
    imagebutton auto "main_choices_op2_%s":
        focus_mask True
        action [
            ToggleVariable("maia_sex_pos_toggle"), 
            If(maia_sex_pos_toggle, Jump("is_maia_sex2"), Jump("is_maia_sex1"))
        ]
    text "Change position":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 959 xanchor 0.5 yanchor 0.5 italic True

    if is_maia_anim_asex1 or is_maia_anim_asex2:
        imagebutton auto "main_choices_op3_%s":
            focus_mask True
            action [SetVariable("is_maia_anim_vsex1", True), SetVariable("is_maia_anim_asex1", False), SetVariable("is_maia_anim_asex2", False), Jump("is_maia_sex1")]
        text "Vaginal":
            size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 1086 xanchor 0.5 yanchor 0.5 italic True
    else:
        add "main_choices_op3_idle"
        text "Vaginal":
            size persistent.choices_text_size color "#818181" font "candara.ttf" xpos 2260 ypos 1086 xanchor 0.5 yanchor 0.5 italic True

    if is_maia_anim_vsex1 or is_maia_anim_vsex2:
        imagebutton auto "main_choices_op4_%s":
            focus_mask True
            action [SetVariable("is_maia_anim_asex1", True), SetVariable("is_maia_anim_vsex1", False), SetVariable("is_maia_anim_vsex2", False), Jump("is_maia_sex1")]
        text "Anal":
            size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 1214 xanchor 0.5 yanchor 0.5 italic True
    else:
        add "main_choices_op4_idle"
        text "Anal":
            size persistent.choices_text_size color "#818181" font "candara.ttf" xpos 2260 ypos 1214 xanchor 0.5 yanchor 0.5 italic True

    imagebutton auto "main_choices_op5_%s":
        focus_mask True
        action Jump("is_maia_sex_cum")
    text "Cum":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 1340 xanchor 0.5 yanchor 0.5 italic True

screen is_maia_sex_sex2():
    imagebutton auto "main_choices_op1_%s":
        focus_mask True
        action Jump("is_maia_sex_faster")
    text "Faster":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 832 xanchor 0.5 yanchor 0.5 italic True
    
    imagebutton auto "main_choices_op2_%s":
        focus_mask True
        action [
            ToggleVariable("maia_sex_pos_toggle"), 
            If(maia_sex_pos_toggle, Jump("is_maia_sex2"), Jump("is_maia_sex1"))
        ]
    text "Change position":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 959 xanchor 0.5 yanchor 0.5 italic True

    if is_maia_anim_asex1 or is_maia_anim_asex2:
        imagebutton auto "main_choices_op3_%s":
            focus_mask True
            action [SetVariable("is_maia_anim_vsex1", True), SetVariable("is_maia_anim_asex1", False), SetVariable("is_maia_anim_asex2", False), Jump("is_maia_sex2")]
        text "Vaginal":
            size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 1086 xanchor 0.5 yanchor 0.5 italic True
    else:
        add "main_choices_op3_idle"
        text "Vaginal":
            size persistent.choices_text_size color "#818181" font "candara.ttf" xpos 2260 ypos 1086 xanchor 0.5 yanchor 0.5 italic True

    if is_maia_anim_vsex1 or is_maia_anim_vsex2:
        imagebutton auto "main_choices_op4_%s":
            focus_mask True
            action [SetVariable("is_maia_anim_asex1", True), SetVariable("is_maia_anim_vsex1", False), SetVariable("is_maia_anim_vsex2", False), Jump("is_maia_sex2")]
        text "Anal":
            size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 1214 xanchor 0.5 yanchor 0.5 italic True
    else:
        add "main_choices_op4_idle"
        text "Anal":
            size persistent.choices_text_size color "#818181" font "candara.ttf" xpos 2260 ypos 1214 xanchor 0.5 yanchor 0.5 italic True

    imagebutton auto "main_choices_op5_%s":
        focus_mask True
        action Jump("is_maia_sex_cum")
    text "Cum":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 1340 xanchor 0.5 yanchor 0.5 italic True


label is_maia_sex:
    $ maia_virgin = False
    $ mcname = persistent.name
    if persistent.name == "None" or mcname == "None":
        while mcname == "None" or mcname == "":
            $ mcname = renpy.input("There was an issue with your name. Please rewrite your name:", length=32)
        $ persistent.name = mcname
    if not persistent.scene6_p2_replay:
        $ persistent.scene6_p2_replay = True
    stop music fadeout 3.0
    $ maia_sex = True
    mc "I'm in the mood for some sex."
    scene 18_s8 with dissolve
    if cycle == 0:
        if maia_sex > maia_anal_sex:
            m "You want to do it the same way again, [mx]? I... I liked it a lot last time."
        elif maia_anal_sex > maia_sex:
            m "Do you want to use my butt again, [mx]?"
        else:
            m "M-Me too!"

    elif cycle == 1:
        if maia_sex > maia_anal_sex:
            m "I still remember how good it felt, [mx]... I want you again."
        elif maia_anal_sex > maia_sex:
            m "M-My butthole is still a little sore from last time but of course, [mx]!"
        else:
            m "I'll be sure to make you feel extra good, [mx]!"

    elif cycle == 2:
        if maia_sex > maia_anal_sex:
            m "You can have me however you want, [mx]... I'm all yours."
        elif maia_anal_sex > maia_sex:
            m "You really like it there, don't you, [mx]? It's okay... I do too now."
        else: 
            m "Please use my holes to your hearts content, [mx]."
    elif cycle == 3:
        if maia_sex > maia_anal_sex:
            m "I was hoping you'd come back for me again, [mx]..."
        elif maia_anal_sex > maia_sex:
            m "You want to use my butt again, don't you? I could tell by that look, [mx]~"
        else:
            m "I was thinking the same thing, [mx]!"

    scene 18_s7 with dissolve
    scene black with Fade(0.5,0.5,0.5)
    if maia_sex > maia_anal_sex:
        $ is_maia_anim_vsex1 = True
        $ is_maia_anim_vsex2 = False
        $ maia_sex_pos_toggle = True
        $ is_maia_asex_first = True
        $ is_maia_anim_sex2_first = True
        $ is_maia_vsex_faster_first = True
        perception "Maia barely has time to react before you pull her onto the bed, her body pressing into the sheets as you move behind her. You lift her leg, exposing her dripping pussy."
        show is_maia_anim_vsex1 with dissolve
        sensation "The tip of your cock presses against her slick entrance, teasing her folds before you push inside. A sharp gasp rips from Maia's throat as you fill her inch by inch, her walls squeezing around you like a vice."
        m "Ah! Hah~ Yes!"
        mc "My... you're a lot more vocal now."
        m "I-I love it, [mx]!"
        m "I want to be... ngh! Like... this! forever~"
        sensation "Her lewd confession sends a jolt straight to your cock, making you throb inside her tight, welcoming pussy."
        call screen is_maia_sex_sex1 with dissolve
        
    elif maia_anal_sex > maia_sex:
        $ is_maia_anim_vsex1 = False
        $ is_maia_anim_vsex2 = False
        $ is_maia_anim_asex1 = True
        $ is_maia_anim_asex2 = False
        $ is_maia_asex_first = False
        show is_maia_anim_asex1 with dissolve
        sensation "Her ass stretches around you, inch by inch, her body struggling to take you. She's so tight, so hot, and every little twitch makes you throb even harder."
        m "Hnnn~ [mx]!"
        m "Ahh! It's so—so big... ngh!"
        mc "You love it, don't you?"
        call screen is_maia_sex_sex1 with dissolve

    else:
        $ is_maia_anim_vsex1 = True
        $ is_maia_anim_vsex2 = False
        $ maia_sex_pos_toggle = True
        $ is_maia_asex_first = True
        $ is_maia_anim_sex2_first = True
        $ is_maia_vsex_faster_first = True
        if maia_pussy_virgin:
            $ maia_pussy_virgin = False
            perception "Maia barely has time to react before you pull her onto the bed, her body pressing into the sheets as you move behind her. You lift her leg, exposing her dripping pussy."
            show is_maia_anim_vsex1 with dissolve
            sensation "The tip of your cock presses against her slick entrance, teasing her folds before you push inside. A sharp gasp rips from Maia's throat as you fill her inch by inch, her walls squeezing around you like a vice."
            m "Ah! Hah~ Yes! I'm so glad you're my first, [mx]~!"
            mc "You're not a virgin anymore. How does it feel?"
            m "I-I love it, [mx]!"
            m "I want to be... ngh! Like... this! forever~"
            sensation "Her lewd confession sends a jolt straight to your cock, making you throb inside her tight, welcoming pussy."
        else:
            perception "Maia barely has time to react before you pull her onto the bed, her body pressing into the sheets as you move behind her. You lift her leg, exposing her dripping pussy."
            show is_maia_anim_vsex1 with dissolve
            sensation "The tip of your cock presses against her slick entrance, teasing her folds before you push inside. A sharp gasp rips from Maia's throat as you fill her inch by inch, her walls squeezing around you like a vice."
            m "Ah! Hah~ Yes!"
            mc "My... you're a lot more vocal now."
            m "I-I love it, [mx]!"
            m "I want to be... ngh! Like... this! forever~"
            sensation "Her lewd confession sends a jolt straight to your cock, making you throb inside her tight, welcoming pussy."
        call screen is_maia_sex_sex1 with dissolve

label is_maia_sex1:
    if is_maia_anim_vsex1 or is_maia_anim_vsex2:
        $ is_maia_anim_vsex1 = True
        $ is_maia_anim_vsex2 = False
        scene black with Dissolve(0.3)
        show is_maia_anim_vsex1 with dissolve
        m "Hah~ Ahhhnn~"
        call screen is_maia_sex_sex1 with dissolve
    elif is_maia_anim_asex1 or is_maia_anim_asex2:
        $ is_maia_anim_asex1 = True
        $ is_maia_anim_asex2 = False
        if is_maia_asex_first:
            mc "I wanna fuck your ass."
            if maia_anus_virgin:
                $ maia_anus_virgin = False
                m "This will be my first time in the butt, [mx]..."
                mc "I'll be gentle."
                scene black with Dissolve(0.3)
                show is_maia_anim_asex1 with dissolve
                sensation "Her ass stretches around you, inch by inch, her body struggling to take you. She's so tight, so hot, and every little twitch makes you throb even harder."
                m "Hnnn~ [mx]!"
                m "Ahh! It's so—so big... ngh!"
                mc "*chuckles* Congratulations on losing your anal virginity."
                m "T-Thank you... Uhnnmm~!"
                $ is_maia_asex_first = False
            else:
                m "P-Please be gentle, [mx]..."
                scene black with Dissolve(0.3)
                show is_maia_anim_asex1 with dissolve
                sensation "Her ass stretches around you, inch by inch, her body struggling to take you. She's so tight, so hot, and every little twitch makes you throb even harder."
                m "Hnnn~ [mx]!"
                m "Ahh! It's so—so big... ngh!"
                mc "You love it, don't you?"
                $ is_maia_asex_first = False
            call screen is_maia_sex_sex1 with dissolve
        else:
            scene black with Dissolve(0.3)
            show is_maia_anim_asex1 with dissolve
            m "Agh! Nhnn..."
            call screen is_maia_sex_sex1 with dissolve
            
label is_maia_sex2:
    if is_maia_anim_sex2_first:
        mc "I want to see your ass bouncing on my cock."
        $ is_maia_anim_sex2_first = False
        scene black with Fade(0.5,0.5,0.5)
        perception "Leaning back onto the bed, you watch Maia crawl over you, her body trembling with anticipation. She straddles you, positioning herself above your cock, her glistening folds hovering over the tip."
        if is_maia_anim_vsex1 or is_maia_anim_vsex2:
            show is_maia_anim_vsex2 with dissolve
            $ is_maia_anim_vsex1 = False
            $ is_maia_anim_vsex2 = True
            m "Ahhhh~"
            sensation "Slowly, she lowers herself down, taking you inch by inch until she's fully impaled on your cock. Her walls flutter around you, squeezing you deliciously as she gasps."
            mc "Your ass is really fat, Maia."
            m "F-Fat?! Is... Is that a good thing?"
            mc "Of course it is!"
            m "Mhmmm~"
            call screen is_maia_sex_sex2 with dissolve
        elif is_maia_anim_asex1 or is_maia_anim_asex2:
            $ is_maia_anim_asex1 = False
            $ is_maia_anim_asex2 = True
            show is_maia_anim_asex2 with dissolve
            m "Ahhhh~"
            sensation "She slowly lowers herself, letting her tight anus stretch around your cock. Soft whimpers escape her lips as she struggles to take you in."
            mc "Your ass is taking me so well, Maia."
            m "A-Ahh~! R-Really?"
            mc "Yeah... feels amazing wrapped around me."
            m "Mhmm~ I-I want to make you feel even better, [mx]~"
            call screen is_maia_sex_sex2 with dissolve
    else:
        if is_maia_anim_vsex1 or is_maia_anim_vsex2:
            $ is_maia_anim_vsex1 = False
            $ is_maia_anim_vsex2 = True
            scene black with Dissolve(0.3)
            show is_maia_anim_vsex2 with dissolve
            m "Ahn~ Hah~"
            call screen is_maia_sex_sex2 with dissolve
        elif is_maia_anim_asex1 or is_maia_anim_asex2:
            $ is_maia_anim_asex1 = False
            $ is_maia_anim_asex2 = True
            if is_maia_asex_first:
                mc "I wanna fuck your ass."
                m "P-Please be gentle, [mx]..."
                scene black with Dissolve(0.3)
                show is_maia_anim_asex2 with dissolve
                "Her ass stretches around you, inch by inch, her body struggling to take you. She's so tight, so hot, and every little twitch makes you throb even harder."
                m "Hnnn~ [mx]!"
                m "Ahh! It's so—so big... ngh!"
                mc "You love it, don't you?"
                $ is_maia_asex_first = False
                call screen is_maia_sex_sex2 with dissolve
            else:
                scene black with Dissolve(0.3)
                show is_maia_anim_asex2 with dissolve
                m "Ah! Nghnn..."
                call screen is_maia_sex_sex2 with dissolve

default is_maia_vsex_faster_first = True
label is_maia_sex_faster:
    scene black with Dissolve(0.3)
    if is_maia_anim_vsex1:
        show is_maia_anim_vsex1_faster with dissolve
        hide is_maia_anim_vsex1 with dissolve
        if is_maia_vsex_faster_first:
            perception "With a firm grip on her leg, you start thrusting faster, each movement sending ripples of pleasure through both of you. Maia's moans grow louder, more shameless, as her body completely surrenders to you."
            m "Haahhh! Hah! Nghnnnn~"
            mc "Out of words now?"
            m "[mx]! [mx]! ...[mx]!"
            play sound "se_sfx/masturbate_female/6_masturbate_cum1.mp3"
            scene is_maia_sex1 with vpunch
            m "Nhgnnnnnnnn!!"
            mc "I'm still not done."
            scene is_maia_sex0 with dissolve
            m "[mx]... wait... I'm still—"
            show is_maia_anim_vsex1_faster with dissolve
            perception "A broken whimper spills from her lips as you slam into her again, the overstimulation making her tremble beneath you."
            m "Nghnnn!"
            $ is_maia_vsex_faster_first = False
            call screen is_maia_sex_sex1 with dissolve
        else:
            show is_maia_anim_vsex1_faster with dissolve
            hide is_maia_anim_vsex1
            m "Y-Yes! [mx]... Do it... Harder!"
            call screen is_maia_sex_sex1 with dissolve
    elif is_maia_anim_vsex2:
        show is_maia_anim_vsex2_faster with dissolve
        hide is_maia_anim_vsex2
        m "Hah! Ahhh! Mhmmnnn~"
        sensation "Her walls clench around you, her body completely at your mercy as she loses herself in pleasure."
        call screen is_maia_sex_sex2 with dissolve
    elif is_maia_anim_asex1:
        show is_maia_anim_asex1_faster with dissolve
        hide is_maia_anim_asex1
        m "Ahh! Nhn! Not... not so fast, [mx]..."
        perception "You pick up the pace, fucking her tight little hole without restraint. Each thrust forces a lewd moan from her lips, her body quivering under the intensity."
        call screen is_maia_sex_sex1 with dissolve
    elif is_maia_anim_asex2:
        show is_maia_anim_asex2_faster with dissolve
        hide is_maia_anim_asex2
        m "[mx]! I-It's so deep! Nghh! I—I feel so full~"
        call screen is_maia_sex_sex2 with dissolve

label is_maia_sex_cum:
    mc "I'm cumming!"
    if is_maia_anim_vsex1:
        $ maia_sex += 1
        sensation "The walls of her pussy tighten instinctively around you, as if urging you to release everything deep inside her."
        play sound "se_sfx/sex/sex_cum1.mp3" 

        if persistent.xray_mode:
            scene is_maia_sex2_xray1 with vpunch
            mc "Hngg!"
            play sound "se_sfx/sex/sex_cum2.mp3" 
            scene is_maia_sex2_xray2 with vpunch
            m "Mfghmmmmmm!"
            play sound "se_sfx/sex/touch2.mp3" 
            scene is_maia_sex3_xray3 with dissolve
            mc "Hahh... hah..."
        else:
            scene is_maia_sex2 with vpunch
            mc "Hngg!"
            play sound "se_sfx/sex/sex_cum2.mp3" 
            scene is_maia_sex2 with vpunch
            m "Mfghmmmmmm!"
            play sound "se_sfx/sex/touch2.mp3" 
            scene is_maia_sex3 with dissolve
            mc "Hahh... hah..."

        if not maia_pregnant:
            call pregnancy_check_maia from call_pregnancy_check_maia
        if maia_pregnant:
            scene is_maia_sex4 with dissolve
            m "I'm already pregnant, but I will always accept your seed, [mx]~"
            scene is_maia_sex3 with dissolve
            mc "You're so fucking hot when you say stuff like that."
            scene is_maia_sex4 with dissolve
            m "*giggles* I-It feels good when [mx] spills his seed inside me~"
            m "I want to birth your next child, [mx]... and your next, and the next!"
            scene is_maia_sex3 with dissolve
        else:
            scene is_maia_sex4 with dissolve
            m "You came inside, [mx]... T-That means I might get pregnant..."
            scene is_maia_sex3 with dissolve
            mc "We'll see."
            scene is_maia_sex4 with dissolve
            m "W-We can... try again then~ I-If [mx] wants..."
            scene is_maia_sex3 with dissolve
        scene black with Fade(0.5,0.5,0.5)
        perception "Her legs wobble as she tries to stand, her body still tingling from the pleasure."
        
    elif is_maia_anim_vsex2:
        $ maia_sex += 1
        sensation "The tight heat around you pulses desperately, coaxing out your release."
        play sound "se_sfx/sex/sex_cum2.mp3" 
        if persistent.xray_mode:
            scene is_maia_sex8_xray1 with vpunch
            mc "Hngg!"
            play sound "se_sfx/sex/sex_cum1.mp3" 
            scene is_maia_sex8_xray2 with vpunch
            m "Mfghmmmmmm!"
            play sound "se_sfx/sex/touch2.mp3" 
            scene is_maia_sex9_xray3 with dissolve
        else:
            scene is_maia_sex8 with vpunch
            mc "Hngg!"
            play sound "se_sfx/sex/sex_cum1.mp3" 
            scene is_maia_sex8 with vpunch
            m "Mfghmmmmmm!"
            play sound "se_sfx/sex/touch2.mp3" 
            scene is_maia_sex9 with dissolve

        if not maia_pregnant:
            call pregnancy_check_maia from __call_pregnancy_check_maia
        if maia_pregnant:
            m "Did you enjoy my pussy, [mx]?"
            mc "Your pussy is a gift from the heavens, Maia."
            m "I'm so glad that you like it~ Always know this it is yours, [mx]. Weather I'm sleeping or awake—use it whenever you wish~"
            mc "*chuckles* Did your pregnancy make you hornier or something?"
            m "Maybe~"
        else:
            mc "Hahh... hah..."
            m "Mmm~ Thank you for ejaculating inside me, [mx]! Now... we can finally have children~"
            mc "It's not guarented."
            m "W-We can... try again then~ I-If [mx] wants."
        scene black with Fade(0.5,0.5,0.5)
        perception "She tries to get up, but her legs tremble beneath her, betraying just how much she enjoyed it."

    elif is_maia_anim_asex1:
        $ maia_anal_sex += 1
        sensation "Her tight little hole clenches around you, as if instinctively trying to keep you buried deep inside. Even through the slight discomfort, she still wants to give you a proper orgasm."
        m "D-Do it... inside, [mx]!"
        play sound "se_sfx/sex/sex_cum2.mp3" 
        scene is_maia_sex5 with vpunch
        mc "Fuck, you're so tight!"
        play sound "se_sfx/sex/sex_cum1.mp3" 
        scene is_maia_sex5 with vpunch
        m "Nhnn!"
        play sound "se_sfx/sex/touch3.mp3" 
        scene is_maia_sex7 with dissolve
        m "My... hah... my butt... It's so full..."
        scene is_maia_sex6 with dissolve
        mc "You took it so well, Maia."
        scene is_maia_sex7 with dissolve
        m "T-Thank you, [mx]... A-Anything for you..."
        scene is_maia_sex6 with dissolve
        scene black with Fade(0.5,0.5,0.5)
        perception "She shifts slightly, trying to regain her composure, but her shaky legs betray just how much she was pushed to her limits."

    elif is_maia_anim_asex2:
        $ maia_anal_sex += 1
        sensation "Her tight ring squeezes you desperately, milking every last drop from you. Even through the overwhelming stretch, she moans, lost in the pleasure."
        m "Don't... Don't hold back, [mx]!"
        play sound "se_sfx/sex/sex_cum1.mp3" 
        scene is_maia_sex10 with vpunch
        mc "Fuck, you're so tight!"
        play sound "se_sfx/sex/sex_cum2.mp3" 
        scene is_maia_sex10 with vpunch
        m "Nhnn!"
        play sound "se_sfx/sex/touch3.mp3" 
        scene is_maia_sex11 with dissolve
        m "Nhnn! M-My butt... nghh... It's too much~"
        mc "You took it so well, Maia."
        m "T-Thank you, [mx]... Anything for you..."
        scene black with Fade(0.5,0.5,0.5)
        perception "She slowly rises, her legs weak and trembling, her body still trying to recover from the intensity."
    $ renpy.end_replay()
    jump maia_sex_end
#############################################FOOTJOB#######################################################
#############################################FOOTJOB#######################################################
#############################################FOOTJOB#######################################################
image is_maia_anim_fj1 = Movie(play="images/is_scenes/maia/is_maia_fj/anims/is_maia_anim_fj1.webm", loop=True)
image is_maia_anim_fj2 = Movie(play="images/is_scenes/maia/is_maia_fj/anims/is_maia_anim_fj2.webm", loop=True)

image is_maia_anim_fj1_faster = Movie(play="images/is_scenes/maia/is_maia_fj/anims/is_maia_anim_fj1_faster.webm", loop=True)
image is_maia_anim_fj2_faster = Movie(play="images/is_scenes/maia/is_maia_fj/anims/is_maia_anim_fj2_faster.webm", loop=True)

default is_maia_anim_fj1 = True
default is_maia_anim_fj2 = False

default maia_fj_pos_toggle = True
default is_maia_footjob2_first = True
screen is_maia_fj():
    imagebutton auto "main_choices_op1_%s":
        focus_mask True
        action Jump("is_maia_footjob_faster")
    text "Faster":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 832 xanchor 0.5 yanchor 0.5 italic True
    
    imagebutton auto "main_choices_op2_%s":
        focus_mask True
        action [
            ToggleVariable("maia_fj_pos_toggle"), 
            If(maia_fj_pos_toggle, Jump("is_maia_footjob2"), Jump("is_maia_footjob1"))
        ]
    text "Change position":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 959 xanchor 0.5 yanchor 0.5 italic True

    imagebutton auto "main_choices_op3_%s":
        focus_mask True
        action Jump("is_maia_footjob_cum")
    text "Cum":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 1086 xanchor 0.5 yanchor 0.5 italic True

label is_maia_footjob:
    $ maia_virgin = False
    $ mcname = persistent.name
    if persistent.name == "None" or mcname == "None":
        while mcname == "None" or mcname == "":
            $ mcname = renpy.input("There was an issue with your name. Please rewrite your name:", length=32)
        $ persistent.name = mcname
    if not persistent.scene7_p2_replay:
        $ persistent.scene7_p2_replay = True
    stop music fadeout 3.0
    $ maia_fj = True
    $ is_maia_anim_fj1 = True
    $ is_maia_anim_fj2 = False
    $ maia_fj_pos_toggle = True
    $ is_maia_footjob2_first = True

    scene 18_s10 with dissolve
    if cycle == 0:
        m "Oh! Of course, [mx]..."
    elif cycle == 1:
        m "You... really like my feet, [mx]."
    elif cycle == 2:
        m "As you wish, [mx]."
    elif cycle == 3:
        m "I... Anything you want, [mx]."

    scene 18_s9 with dissolve
    scene black with Fade(1.0,1.0,1.0)
    show is_maia_anim_fj1 with dissolve
    sensation "Even though she's always walking barefoot, Her feet are incredibly soft, their velvety texture sending shivers of pleasure up your spine as she presses them against you. "
    m "Do you like it, [mx]?"
    mc "Yes."
    m "I'm glad~"
    call screen is_maia_fj with dissolve

label is_maia_footjob1:
    $ is_maia_anim_fj1 = True
    $ is_maia_anim_fj2 = False
    scene black with Dissolve(0.3)
    show is_maia_anim_fj1 with dissolve
    m "Mmmm~"
    call screen is_maia_fj with dissolve

label is_maia_footjob2:
    $ is_maia_anim_fj1 = False
    $ is_maia_anim_fj2 = True
    if is_maia_footjob2_first:
        scene black with Fade(0.5,0.5,0.5)
        perception "You guide Maia onto the table, positioning her feet snugly so your cock can slide effortlessly between them."
        show is_maia_anim_fj2 with dissolve
        sensation "The warmth of her soles envelops you, their smoothness arousing you even further."
        mc "Fuck... your feet were made for this, Maia."
        m "T-Thank you, [mx]~"
        $ is_maia_footjob2_first = False
        call screen is_maia_fj with dissolve
    else:
        scene black with Dissolve(0.3)
        show is_maia_anim_fj2 with dissolve
        m "Mnnnh~"
        call screen is_maia_fj with dissolve

label is_maia_footjob_faster:
    scene black with Dissolve(0.3)
    if is_maia_anim_fj1:
        show is_maia_anim_fj1_faster with dissolve
        hide is_maia_anim_fj1
        m "Hahh! Hah! I can't wait for you to cover my feet, [mx]~"
        call screen is_maia_fj with dissolve
    elif is_maia_anim_fj2:
        show is_maia_anim_fj2_faster with dissolve
        hide is_maia_anim_fj2
        m "I-It feels like you're having sex with my feet, [mx]~"
        call screen is_maia_fj with dissolve
        
label is_maia_footjob_cum:
    mc "I'm cumming!"
    if is_maia_anim_fj1:
        sensation "You reach your limit, your cock twitching between her feet as thick spurts of hot seed spill onto her soft skin."
        play sound "se_sfx/blowjob/facial2.mp3" 
        scene is_maia_fj1 with vpunch
        m "Ah! So hot!"
        play sound "se_sfx/blowjob/facial1.mp3" 
        scene is_maia_fj2 with vpunch
        mc "Ahhh!"
        scene is_maia_fj4 with dissolve
        mc "Hah... Good job, Maia."
        scene is_maia_fj3 with dissolve
        m "I'm glad you enjoyed using my feet, [mx]."
        scene is_maia_fj4 with dissolve
        scene black with Fade(0.5,0.5,0.5)
        perception "She carefully wipes off her feet before standing up, her expression still tinged with excitement."
    elif is_maia_anim_fj2:
        sensation "The warmth and slick friction of her soles push you over the edge, making you climax intensely. Maia doesn't pull away—she simply watches, fascinated, as you 'inseminate' her feet."
        play sound "se_sfx/blowjob/facial1.mp3" 
        scene is_maia_fj5 with vpunch
        mc "Ahhhng!"
        play sound "se_sfx/blowjob/facial2.mp3" 
        scene is_maia_fj5 with vpunch
        m "[mx]..."
        mc "Show me your feet."
        scene is_maia_fj7 with dissolve
        m "Hehe... Do you like them, [mx]?"
        scene is_maia_fj6 with dissolve
        mc "I do. One day, I want you to smother them on my face."
        scene is_maia_fj7 with dissolve
        m "R-Really?! I mean... Of course! Anything for you, [mx]!"
        scene is_maia_fj6 with dissolve
        scene black with Fade(0.5,0.5,0.5)
        perception "She carefully wipes off her feet before standing up, her expression still tinged with excitement."
    $ renpy.end_replay()
    if in_scene18:
        jump scene19
    else:
        jump maia_sex_end

##############################################################NIGHT##################################################################################
#####################################################################################################################################################
default is_maia_night_lbreasts = False
default is_maia_night_lass = False
default is_maia_night_lfeet = False
default is_maia_night_top = False
default is_maia_night_panties = False
default is_maia_night_lbreasts_cum = False
default is_maia_night_choices = True
screen is_maia_night_controls():
    if is_maia_night_choices:
        imagebutton auto "main_choices_op1_%s":
            focus_mask True
            action Jump("is_maia_night_lbreasts")
        text "Look at breasts":
            size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 832 xanchor 0.5 yanchor 0.5 italic True
        
        imagebutton auto "main_choices_op2_%s":
            focus_mask True
            action Jump("is_maia_night_lass")
        text "Look at ass":
            size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 959 xanchor 0.5 yanchor 0.5 italic True

        imagebutton auto "main_choices_op3_%s":
            focus_mask True
            action Jump("is_maia_night_lfeet")
        text "Look at feet":
            size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 1086 xanchor 0.5 yanchor 0.5 italic True
    
    if is_maia_night_lbreasts:
        if not is_maia_night_top:
            imagebutton auto "main_choices_op1_%s":
                focus_mask True
                action [SetVariable("is_maia_night_top", True), Jump("is_maia_night_lbreasts_tits")]
            text "Take off top":
                size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 832 xanchor 0.5 yanchor 0.5 italic True
        if not is_maia_night_panties:
            imagebutton auto "main_choices_op2_%s":
                focus_mask True
                action [SetVariable("is_maia_night_panties", True), Jump("is_maia_night_lbreasts_pussy")]
            text "Take off panties":
                size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 959 xanchor 0.5 yanchor 0.5 italic True
            
        if is_maia_night_top and is_maia_night_panties:
            imagebutton auto "main_choices_op1_%s":
                focus_mask True
                action Jump("is_maia_night_breast_op1")
            text "Inspect breasts":
                size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 832 xanchor 0.5 yanchor 0.5 italic True
            
            imagebutton auto "main_choices_op2_%s":
                focus_mask True
                action Jump("is_maia_night_breast_op2")
            text "Inspect nipples":
                size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 959 xanchor 0.5 yanchor 0.5 italic True

            imagebutton auto "main_choices_op3_%s":
                focus_mask True
                action Jump("is_maia_night_breast_op3")
            text "Inspect belly":
                size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 1086 xanchor 0.5 yanchor 0.5 italic True
            
            imagebutton auto "main_choices_op4_%s":
                focus_mask True
                action Jump("is_maia_night_breast_op4")
            text "Inspect pussy":
                size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 1214 xanchor 0.5 yanchor 0.5 italic True

            imagebutton auto "main_choices_op5_%s":
                focus_mask True
                action Jump("is_maia_night_lbreasts_cum")
            text "Cum":
                size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 1340 xanchor 0.5 yanchor 0.5 italic True

    if is_maia_night_lass:
        imagebutton auto "main_choices_op1_%s":
            focus_mask True
            action Jump("is_maia_night_ass_fass")
        text "Finger ass":
            size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 832 xanchor 0.5 yanchor 0.5 italic True
        
        imagebutton auto "main_choices_op2_%s":
            focus_mask True
            action Jump("is_maia_night_ass_fpussy")
        text "Finger pussy":
            size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 959 xanchor 0.5 yanchor 0.5 italic True

        imagebutton auto "main_choices_op3_%s":
            focus_mask True
            action Jump("is_maia_night_lass_cum")
        text "Cum":
            size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 1086 xanchor 0.5 yanchor 0.5 italic True
    
    if is_maia_night_lfeet:
        imagebutton auto "main_choices_op1_%s":
            focus_mask True
            action Jump("is_maia_night_feet_lick")
        text "Lick feet":
            size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 832 xanchor 0.5 yanchor 0.5 italic True
        
        imagebutton auto "main_choices_op2_%s":
            focus_mask True
            action Jump("is_maia_night_lfeet_cum")
        text "Cum":
            size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 959 xanchor 0.5 yanchor 0.5 italic True

screen is_maia_night_panties():
    imagebutton auto "main_choices_op1_%s":
        focus_mask True
        action Jump("is_maia_night_panties_op1")
    text "Sniff panties":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 832 xanchor 0.5 yanchor 0.5 italic True
    
    imagebutton auto "main_choices_op2_%s":
        focus_mask True
        action Return()
    text "Put panties away":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 959 xanchor 0.5 yanchor 0.5 italic True

default mc_masturbated = False
label is_maia_night:
    $ mcname = persistent.name
    if persistent.name == "None" or mcname == "None":
        while mcname == "None" or mcname == "":
            $ mcname = renpy.input("There was an issue with your name. Please rewrite your name:", length=32)
        $ persistent.name = mcname
    if not persistent.scene8_p2_replay:
        $ persistent.scene8_p2_replay = True
    stop music fadeout 3.0
    $ is_maia_night_lbreasts = False
    $ is_maia_night_lass = False
    $ is_maia_night_lfeet = False
    $ is_maia_night_top = False
    $ is_maia_night_panties = False
    $ is_maia_night_lbreasts_cum = False
    $ is_maia_night_choices = True
    $ mc_masturbated = True
    scene m_sleep1_1 with dissolve
    call screen is_maia_night_controls with dissolve

label is_maia_night_lbreasts:
    $ is_maia_night_choices = False
    $ is_maia_night_lbreasts = True
    $ is_maia_night_lass = False
    $ is_maia_night_lfeet = False
    scene black with Fade(1.0,0.5,0.5)
    scene is_maia_night_breast_1 with dissolve
    call screen is_maia_night_controls with dissolve

label is_maia_night_lbreasts_tits:
    if is_maia_night_panties:
        scene is_maia_night_breast_4 with dissolve
    else:
        scene is_maia_night_breast_2 with dissolve
    perception "You take off her shirt revealing a pair of breasts. She breathes softly, her chest rising and falling in a gentle rhythm."
    mc "(Those heavy breasts look even softer tonight...)"
    call screen is_maia_night_controls with dissolve

label is_maia_night_breast_op1:
    perception "Her breasts are gently rounded, the soft curves catching the light as she breathes deeply. They sway ever so slightly."
    call screen is_maia_night_controls with dissolve
label is_maia_night_breast_op2:
    perception "Her nipples, soft and delicate, stand faintly against her skin, a subtle invitation to touch, responding to the cool air around them."
    sensation "You lightly touch the tip of her right nipple, teasing it in a slow, circling pattern."
    m "Mmmmm..."
    call screen is_maia_night_controls with dissolve
label is_maia_night_breast_op3:
    perception "Her belly looks smooth and soft, with just enough firmness to show she takes care of herself."
    call screen is_maia_night_controls with dissolve
label is_maia_night_breast_op4:
    perception "Her pussy is clean-shaven, the labia folds keeping what's inside hidden, teasing you to keep staring."
    call screen is_maia_night_controls with dissolve

label is_maia_night_lbreasts_pussy:
    if is_maia_night_top:
        scene is_maia_night_breast_4 with dissolve
    else:
        scene is_maia_night_breast_3 with dissolve
    perception "You slide her panties down her legs, the smoothness of her skin teasing your fingers as the fabric glides effortlessly over her slender thighs."
    mc "(Your pussy is too erotic, Maia.)"
    call screen is_maia_night_panties with dissolve
    call screen is_maia_night_controls with dissolve

label is_maia_night_panties_op1:
    sensation "You take a whiff of her freshly removed panties. They smell fresh and floral, a clear indication she has washed them recently. The lingering scent of her pussy, however, only serves to heighten your arousal."
    call screen is_maia_night_controls with dissolve

label is_maia_night_lbreasts_cum:
    mc "(Fuck, I can't hold it—!)"
    if maia_pregnant and maia_pregnancy_timer >= pregnancy_time // 2: 
        scene is_maia_night_breast_5_preg with vpunch
        mc "Ah!"
        scene is_maia_night_breast_6_preg with vpunch
    else:
        scene is_maia_night_breast_5 with vpunch
        mc "Ah!"
        scene is_maia_night_breast_6 with vpunch
    mc "{i}Ngh!{/i}"
    m "{i}Mhmmmm...{/i}"
    mc "(Better head to bed...)"
    scene black with Fade(1.0,0.5,0.5)
    $ renpy.end_replay()
    jump free_roam_sleep

default is_maia_night_ass_fpussy_first = True
default is_maia_night_ass_fpussy_second = False
default is_maia_night_ass_fass_first = True
label is_maia_night_lass:
    $ is_maia_night_choices = False
    $ is_maia_night_lbreasts = False
    $ is_maia_night_lass = True
    $ is_maia_night_lfeet = False
    $ is_maia_night_ass_fpussy_first = True
    $ is_maia_night_ass_fpussy_second = False
    $ is_maia_night_ass_fass_first = True
    scene is_maia_night_ass1 with fade
    perception "You take a look at the curve of her ass, round and full, catching the soft glow of the candlelight. The flickering flames cast a warm, golden sheen across her skin."
    mc "(This round, perfect ass is mine tonight.)"
    scene is_maia_night_ass2 with dissolve
    mc "(Let's get rid of this...)"
    scene is_maia_night_ass3 with dissolve
    perception "You slide her panties down, letting them fall to the floor revealing the folds of her pussy, aswell as her anus."
    scene is_maia_night_ass4 with dissolve
    call screen is_maia_night_controls with dissolve

label is_maia_night_ass_fass:
    if is_maia_night_ass_fass_first:
        scene is_maia_night_ass5 with dissolve
        mc "(Damn... So tight.)"
        play sound "se_sfx/sex/touch1.mp3" 
        scene is_maia_night_ass6 with dissolve
        mc "(My finger's barely getting through...)"
        sensation "You wriggle two fingers into her, slowly, feeling the tight heat of her ass envelop you. Her walls are slick and warm, clenching around your fingers as you move."
        m "{i}Mhhmmmm!{/i}"
        mc "(Oops... Did I forget to lube my finger first?)"
        $ is_maia_night_ass_fass_first = False
    else:
        scene is_maia_night_ass5 with dissolve
        m "{i}Mhnnn!{/i}"
        play sound "se_sfx/sex/touch1.mp3" 
        scene is_maia_night_ass6 with dissolve
        mc "(It's so warm inside... Clenching already?)"
    scene is_maia_night_ass3 with dissolve
    call screen is_maia_night_controls with dissolve

label is_maia_night_ass_fpussy:
    if is_maia_night_ass_fpussy_first:
        scene is_maia_night_ass7 with dissolve
        mc "(A little dry...)"
        scene is_maia_night_ass8 with dissolve
        play sound "se_sfx/sex/touch2.mp3" 
        ""
        play sound "se_sfx/sex/touch3.mp3" 
        scene is_maia_night_ass7 with dissolve
        sensation "At first, your fingers meet resistance, dry and tentative, but soon they're slicked with the warm, honeyed nectar of her arousal, dripping from her walls."
        play sound "se_sfx/sex/touch2.mp3" 
        scene is_maia_night_ass8 with dissolve
        m "{i}Mhmmm...{/i}"
        mc "(That changed fast. She's already soaking... Good girl, Maia.)"
        $ is_maia_night_ass_fpussy_first = False
        $ is_maia_night_ass_fpussy_second = True
    elif is_maia_night_ass_fpussy_second:
        scene is_maia_night_ass7 with dissolve
        mc "(Damn... She's dripping now.)"
        play sound "se_sfx/sex/touch2.mp3" 
        scene is_maia_night_ass8 with dissolve
        sensation "You push deeper, your fingers curling inward, and there it is—a soft, hidden lump that pulses under your touch."
        play sound "se_sfx/sex/touch3.mp3" 
        scene is_maia_night_ass7 with dissolve
        sensation "Her body reacts instantly, a sharp twitch, a gasp caught in her throat, as you brush against it. The sensation sends a shiver through her, her hips arching slightly, begging for more."
        play sound "se_sfx/sex/touch2.mp3" 
        scene is_maia_night_ass8 with dissolve
        m "{i}Mhmmm...{/i}"
        mc "(She's squeezing down hard... Is she already about to—?)"
        sensation "You press harder, teasing that sweet spot with a firmer touch. Her back arches, her breath hitches, and a low moan escapes her lips as her body trembles."
        play sound "se_sfx/masturbate_female/6_masturbate_cum1.mp3" loop
        scene is_maia_night_ass8 with vpunch
        m "{i}Mhnnnn!!{/i}"
        play sound "se_sfx/sex/touch4.mp3" 
        scene is_maia_night_ass8 with vpunch
        mc "(Whoa... She really came.)"
        mc "(No need to thank me, Maia.)"
        $ is_maia_night_ass_fpussy_second = False
    else:
        mc "(She just came... Better not over do it.)"
    scene is_maia_night_ass3 with dissolve
    call screen is_maia_night_controls with dissolve

label is_maia_night_lass_cum:
    mc "(I'm cumming!)"
    scene is_maia_night_ass9 with vpunch
    mc "{i}Ah!{/i}"
    scene is_maia_night_ass10 with vpunch
    mc "{i}Hah... hah...{/i}" 
    mc "(I better get back to bed.)"
    scene black with Fade(1.0,0.5,0.5)
    $ renpy.end_replay()
    jump free_roam_sleep

label is_maia_night_lfeet:
    $ is_maia_night_choices = False
    $ is_maia_night_lbreasts = False
    $ is_maia_night_lass = False
    $ is_maia_night_lfeet = True
    scene is_maia_night_feet1 with Fade(0.5,0.5,0.5)
    perception "Your eyes drift downward, taking in the sight of her feet. The soles are delicate, with a softness that seems to invite touch."
    mc "(I can't fight this urge... I need to cover those sexy feet, Maia.)"
    call screen is_maia_night_controls with dissolve
label is_maia_night_feet_lick:
    scene is_maia_night_feet2 with dissolve
    mc "{i}Mmm...{/i} So soft..."
    sensation "Your tongue drags slowly along the sole of her foot, the texture warm and velvety against your taste buds. The faint salt of her skin mingles with the smoothness, sending a shiver through you as her toes curl slightly in response."
    scene is_maia_night_feet3 with dissolve
    sensation "You take her toes into your mouth, one by one, your lips closing around them as you suck gently. Each toe is soft and yielding, and the faint pressure of your tongue against them draws a quiet, breathy sigh from her."
    mc "({i}Mmm...{/i} Smells like strawberry shampoo...)"
    m "{i}Mnmmm...{/i}"
    scene is_maia_night_feet1 with dissolve
    call screen is_maia_night_controls with dissolve

label is_maia_night_lfeet_cum:
    mc "(Fuck... I'm gonna coat those soles!)"
    scene is_maia_night_feet5 with vpunch
    mc "{i}Ahh!{/i}"
    scene is_maia_night_feet6 with vpunch
    mc "Hah... haah..."
    scene black with Fade(1.0,0.5,0.5)
    $ renpy.end_replay()
    jump free_roam_sleep

#YUUHI IS SCENES #####################################################################################################################################
#####################################################################################################################################################
#####################################################################################################################################################
#####################################################################################################################################################
#####################################################################################################################################################
image is_yuuhi_anim_hj1 = Movie(play="images/is_scenes/yuuhi/is_yuuhi_hj/anims/is_yuuhi_anims_hj1.webm", loop=True)
image is_yuuhi_anim_hj2 = Movie(play="images/is_scenes/yuuhi/is_yuuhi_hj/anims/is_yuuhi_anims_hj2.webm", loop=True)
image is_yuuhi_anim_hj3 = Movie(play="images/is_scenes/yuuhi/is_yuuhi_hj/anims/is_yuuhi_anims_hj3.webm", loop=True)
image is_yuuhi_anim_hj1_faster = Movie(play="images/is_scenes/yuuhi/is_yuuhi_hj/anims/is_yuuhi_anims_hj1_faster.webm", loop=True)
image is_yuuhi_anim_hj2_faster = Movie(play="images/is_scenes/yuuhi/is_yuuhi_hj/anims/is_yuuhi_anims_hj2_faster.webm", loop=True)
image is_yuuhi_anim_hj3_faster = Movie(play="images/is_scenes/yuuhi/is_yuuhi_hj/anims/is_yuuhi_anims_hj3_faster.webm", loop=True)

image is_yuuhi_anim_bj1 = Movie(play="images/is_scenes/yuuhi/is_yuuhi_bj/anims/is_yuuhi_anims_bj1.webm", loop=True)
image is_yuuhi_anim_bj2 = Movie(play="images/is_scenes/yuuhi/is_yuuhi_bj/anims/is_yuuhi_anims_bj2.webm", loop=True)
image is_yuuhi_anim_bj3 = Movie(play="images/is_scenes/yuuhi/is_yuuhi_bj/anims/is_yuuhi_anims_bj3.webm", loop=True)
image is_yuuhi_anim_bj1_faster = Movie(play="images/is_scenes/yuuhi/is_yuuhi_bj/anims/is_yuuhi_anims_bj1_faster.webm", loop=True)
image is_yuuhi_anim_bj2_faster = Movie(play="images/is_scenes/yuuhi/is_yuuhi_bj/anims/is_yuuhi_anims_bj2_faster.webm", loop=True)
image is_yuuhi_anim_bj3_faster = Movie(play="images/is_scenes/yuuhi/is_yuuhi_bj/anims/is_yuuhi_anims_bj3_faster.webm", loop=True)

image is_yuuhi_anim_asex1 = Movie(play="images/is_scenes/yuuhi/is_yuuhi_sex/anims/is_yuuhi_anims_asex1.webm", loop=True)
image is_yuuhi_anim_asex2 = Movie(play="images/is_scenes/yuuhi/is_yuuhi_sex/anims/is_yuuhi_anims_asex2.webm", loop=True)
image is_yuuhi_anim_asex3 = Movie(play="images/is_scenes/yuuhi/is_yuuhi_sex/anims/is_yuuhi_anims_asex3.webm", loop=True)
image is_yuuhi_anim_asex1_faster = Movie(play="images/is_scenes/yuuhi/is_yuuhi_sex/anims/is_yuuhi_anims_asex1_faster.webm", loop=True)
image is_yuuhi_anim_asex2_faster = Movie(play="images/is_scenes/yuuhi/is_yuuhi_sex/anims/is_yuuhi_anims_asex2_faster.webm", loop=True)
image is_yuuhi_anim_asex3_faster = Movie(play="images/is_scenes/yuuhi/is_yuuhi_sex/anims/is_yuuhi_anims_asex3_faster.webm", loop=True)

default yuuhi_hj_pos_toggle = True
default yuuhi_hj_pov_toggle = True
default is_yuuhi_anim_hj1 = True
default is_yuuhi_anim_hj2 = False
default is_yuuhi_anim_hj3 = False

default yuuhi_hj = False
default yuuhi_bj = False
default yuuhi_asex = False
default yuuhi_fj = False

screen is_yuuhi_hj_controls():
    imagebutton auto "main_choices_op1_%s":
        focus_mask True
        action Jump("is_yuuhi_hj_faster")
    text "Faster":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 832 xanchor 0.5 yanchor 0.5 italic True
    
    imagebutton auto "main_choices_op2_%s":
        focus_mask True
        action [
            ToggleVariable("yuuhi_hj_pos_toggle"), 
            If(yuuhi_hj_pos_toggle, Jump("is_yuuhi_hj_pos2"), Jump("is_yuuhi_hj_pov1"))
        ]
    text "Switch position":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 959 xanchor 0.5 yanchor 0.5 italic True

    if is_yuuhi_anim_hj3 == False:
        imagebutton auto "main_choices_op3_%s":
            focus_mask True
            action [
                ToggleVariable("yuuhi_hj_pov_toggle"), 
                If(yuuhi_hj_pov_toggle, Jump("is_yuuhi_hj_pov2"), Jump("is_yuuhi_hj_pov1"))
            ]
        text "Switch POV":
            size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 1086 xanchor 0.5 yanchor 0.5 italic True
    else:
        add "main_choices_op3_idle"
        text "Switch POV":
            size persistent.choices_text_size color "#818181" font "candara.ttf" xpos 2260 ypos 1086 xanchor 0.5 yanchor 0.5 italic True

    imagebutton auto "main_choices_op4_%s":
        focus_mask True
        action Jump("is_yuuhi_hj_cum2")
    text "Cum":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 1214 xanchor 0.5 yanchor 0.5 italic True

screen is_yuuhi_hj_choice3():
    imagebutton auto "main_choices_op1_%s":
        focus_mask True
        action Jump("is_yuuhi_hj_cumface")
    text "Cum on face":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 832 xanchor 0.5 yanchor 0.5 italic True
    
    imagebutton auto "main_choices_op2_%s":
        focus_mask True
        action Jump("is_yuuhi_hj_cumbreasts")
    text "Cum on breasts":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 959 xanchor 0.5 yanchor 0.5 italic True

label is_yuuhi_hj1:
    $ mcname = persistent.name
    if persistent.name == "None" or mcname == "None":
        while mcname == "None" or mcname == "":
            $ mcname = renpy.input("There was an issue with your name. Please rewrite your name:", length=32)
        $ persistent.name = mcname
    if not persistent.scene1_p3_replay:
        $ persistent.scene1_p3_replay = True
    $ yuuhi_hj = True
    $ is_yuuhi_anim_hj1 = True
    $ is_yuuhi_anim_hj2 = False
    $ is_yuuhi_anim_hj3 = False
    $ yuuhi_hj_pov_toggle = True
    $ yuuhi_hj_pos_toggle = True
    scene 31_s13 with dissolve
    if cycle == 0:
        yuuhi "A handy? Come here~"
    elif cycle == 1:
        yuuhi "Does my hand feel {i}that{/i} good?"
    elif cycle == 2:
        yuuhi "I'll serve it thoroughly~"
    elif cycle == 3:
        yuuhi "Follow me~"
    scene 31_s14 with dissolve
    scene black with Fade(1.0,0.5,0.5)
    jump is_yuuhi_hj2

label is_yuuhi_hj2:
    stop music fadeout 2.0 
    perception "Yuuhi's trembling fingers tear at her top buttons. Her breasts spill free, soft and flushed, rising and falling with each desperate gasp. Her nipples harden under your gaze—begging to be marked."
    show is_yuuhi_anim_hj1 with dissolve
    perception "Her palm slaps wetly against your cock. She whimpers, hips grinding nothing as her panties darken."
    if cycle == 0:
        yuuhi "S-so warm... and hard..."
        yuuhi "Don't worry, [mc]... I'll take care of you."
    elif cycle == 1:
        yuuhi "Mmm... You're throbbing so much. Is it because of me?"
        yuuhi "I can feel you twitching in my hand~ You're so sensitive, [mc]... Do you like it when I stroke you like this?"
    elif cycle == 2:
        yuuhi "[mc], you're making such a mess... dripping everywhere. Should I go faster?"
        yuuhi "You're stretching my fingers apart... I-I wanna feel you burst in my hands... make me all sticky with it."
    elif cycle == 3:
        yuuhi "[mc]...! You're shaking so much... Does it feel that good?"
        yuuhi "If you want to ejacualte, then please do. Don't hold back."
    call screen is_yuuhi_hj_controls with dissolve

label is_yuuhi_hj_pov1:
    $ is_yuuhi_anim_hj1 = True
    $ is_yuuhi_anim_hj2 = False
    $ is_yuuhi_anim_hj3 = False
    $ yuuhi_hj_pov_toggle = True
    $ yuuhi_hj_pos_toggle = True
    scene black with Dissolve(0.3)
    show is_yuuhi_anim_hj1 with dissolve
    call screen is_yuuhi_hj_controls with dissolve

label is_yuuhi_hj_pov2:
    $ is_yuuhi_anim_hj1 = False
    $ is_yuuhi_anim_hj2 = True
    $ is_yuuhi_anim_hj3 = False
    scene black with Dissolve(0.3)
    show is_yuuhi_anim_hj2 with dissolve
    call screen is_yuuhi_hj_controls with dissolve

label is_yuuhi_hj_pos2:
    scene black with Fade(0.5,0.5,0.5)
    perception "You guide her to the table. She obeys, her body stretching beneath you, anticipation flickering in her eyes. You climb over her."
    $ is_yuuhi_anim_hj1 = False
    $ is_yuuhi_anim_hj2 = False
    $ is_yuuhi_anim_hj3 = True
    scene black with Dissolve(0.3)
    show is_yuuhi_anim_hj3 with dissolve
    if cycle == 0:
        yuuhi "D-does... [mc] like his wifes hand-pussy grip?"
    elif cycle == 1:
        yuuhi "Hehe~ It's so big in my little hand..."
    elif cycle == 2:
        yuuhi "Hahh... it's getting even harder. I-Is it because you're close? You wanna let it all out?"
    elif cycle == 3:
        yuuhi "Nnnh! C'mon, [mc]... I want you to make to cover me with it..."
    sensation "Her fingers tighten around your cock, her strokes slow and deliberate as she watches your reaction."
    call screen is_yuuhi_hj_controls with dissolve

label is_yuuhi_hj_faster:
    scene black with Dissolve(0.3)
    if is_yuuhi_anim_hj1:
        show is_yuuhi_anim_hj1_faster with dissolve
        hide is_yuuhi_anim_hj1 with dissolve
        yuuhi "Hmph! Hmph! Please don't hold back, cover my face!"
        call screen is_yuuhi_hj_controls with dissolve
    elif is_yuuhi_anim_hj2:
        show is_yuuhi_anim_hj2_faster with dissolve
        hide is_yuuhi_anim_hj2 with dissolve
        yuuhi "Mhmmm~ Does this feel good, [mc]?"
        call screen is_yuuhi_hj_controls with dissolve
    else:
        show is_yuuhi_anim_hj3_faster with dissolve
        hide is_yuuhi_anim_hj3 with dissolve
        yuuhi "Does it feel better in this position, [mc]?"
        call screen is_yuuhi_hj_controls with dissolve

label is_yuuhi_hj_cum2:
    if is_yuuhi_anim_hj1 or is_yuuhi_anim_hj2:
        mc "I'm painting your cute face!"
        yuuhi "Go ahead and mark it, [mc]!"
        play sound "se_sfx/blowjob/facial1.mp3" 
        scene is_yuuhi_hj9 with vpunch
        perception "Your balls tighten as thick ropes blast across her face. Yuuhi's eyelid flutters wildly when a pearly strand splatters across her cornea."
        play sound "se_sfx/blowjob/facial2.mp3" 
        scene is_yuuhi_hj8 with vpunch
        mc "{i}Hngghhhh!{/i}"
        scene is_yuuhi_hj12 with dissolve
        mc "Hah... hah..."
        scene is_yuuhi_hj10 with dissolve
        yuuhi "D-did I milk you good? My throat's... still empty though..."
        yuuhi "O-or my... butt... if you want a tighter fit~"
        scene is_yuuhi_hj12 with dissolve
        scene black with Fade(1.0,0.5,0.5)
        perception "Yuuhi rises on shaky legs, her soaked panties clinging to her swollen pussy lips."
        $ renpy.end_replay()
        jump yuuhi_sex_end
    else:
        call screen is_yuuhi_hj_choice3 with dissolve

label is_yuuhi_hj_cumface:
    mc "I'll mark your pretty face!"
    yuuhi "Make me yours, [mc]!"
    play sound "se_sfx/blowjob/facial1.mp3" 
    scene is_yuuhi_hj17 with vpunch
    perception "Your eruption paints her face in sticky streaks, one particularly viscous globule dangling from her gasping lips"
    play sound "se_sfx/blowjob/facial4.mp3" 
    scene is_yuuhi_hj18 with vpunch
    mc "{i}Hngghhhh!{/i}"
    scene is_yuuhi_hj20 with dissolve
    mc "Hah... hah... Perfect... canvas..."
    scene is_yuuhi_hj19 with dissolve
    yuuhi "I-I'll... never wash this scent off..." 
    scene is_yuuhi_hj20 with dissolve
    scene black with Fade(1.0,0.5,0.5)
    perception "Yuuhi sways upright, her drenched thighs leaving slick prints on the floor."
    $ renpy.end_replay()
    jump yuuhi_sex_end

label is_yuuhi_hj_cumbreasts:
    mc "I'll mark your breasts!"
    yuuhi "Please! cover them with your seed~"
    play sound "se_sfx/blowjob/facial2.mp3" 
    scene is_yuuhi_hj21 with vpunch
    perception "Thick spurts arch through the air, each rope sizzling as it lands on her nipples. Her chest heaves, making the cum pool in her cleavage."
    play sound "se_sfx/blowjob/facial5.mp3" 
    scene is_yuuhi_hj22 with vpunch
    mc "{i}Hngghhhh!{/i}"
    scene is_yuuhi_hj24 with dissolve
    mc "Hah... hah..."
    scene is_yuuhi_hj23 with dissolve
    yuuhi "I'm yours forever, [mc]~"
    scene is_yuuhi_hj24 with dissolve
    scene black with Fade(1.0,0.5,0.5)
    perception "Yuuhi stumbles up, her soaked pussy audibly squelching with each step."
    $ renpy.end_replay()
    jump yuuhi_sex_end

########################################################################################################################
###############################################YUUJI BJ#################################################################
########################################################################################################################
default yuuhi_bj_pos_toggle = True
default yuuhi_bj_pov_toggle = True
default is_yuuhi_anim_bj1 = True
default is_yuuhi_anim_bj2 = False
default is_yuuhi_anim_bj3 = False

screen is_yuuhi_bj_controls():
    imagebutton auto "main_choices_op1_%s":
        focus_mask True
        action Jump("is_yuuhi_bj_faster")
    text "Faster":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 832 xanchor 0.5 yanchor 0.5 italic True
    
    imagebutton auto "main_choices_op2_%s":
        focus_mask True
        action [
            ToggleVariable("yuuhi_bj_pos_toggle"), 
            If(yuuhi_bj_pos_toggle, Jump("is_yuuhi_bj_pos2"), Jump("is_yuuhi_bj_pov1"))
        ]
    text "Change position":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 959 xanchor 0.5 yanchor 0.5 italic True

    if is_yuuhi_anim_bj1 == False:
        imagebutton auto "main_choices_op3_%s":
            focus_mask True
            action [
                ToggleVariable("yuuhi_bj_pov_toggle"), 
                If(yuuhi_bj_pov_toggle, Jump("is_yuuhi_bj_pov2"), Jump("is_yuuhi_bj_pos2"))
            ]
        text "Change POV":
            size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 1086 xanchor 0.5 yanchor 0.5 italic True
    else:
        add "main_choices_op3_idle"
        text "Change POV":
            size persistent.choices_text_size color "#818181" font "candara.ttf" xpos 2260 ypos 1086 xanchor 0.5 yanchor 0.5 italic True
    
    imagebutton auto "main_choices_op4_%s":
        focus_mask True
        action Jump("is_yuuhi_bj_cum")
    text "Cum":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 1214 xanchor 0.5 yanchor 0.5 italic True

screen is_yuuhi_bj_cum():
    imagebutton auto "main_choices_op1_%s":
        focus_mask True
        action Jump("is_yuuhi_bj_cum_inside")
    text "Cum inside":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 832 xanchor 0.5 yanchor 0.5 italic True
    
    imagebutton auto "main_choices_op2_%s":
        focus_mask True
        action Jump("is_yuuhi_bj_cum_outside")
    text "Cum outside":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 959 xanchor 0.5 yanchor 0.5 italic True

label is_yuuhi_bj1:
    $ mcname = persistent.name
    if persistent.name == "None" or mcname == "None":
        while mcname == "None" or mcname == "":
            $ mcname = renpy.input("There was an issue with your name. Please rewrite your name:", length=32)
        $ persistent.name = mcname
    if not persistent.scene2_p3_replay:
        $ persistent.scene2_p3_replay = True
    $ yuuhi_bj = True
    $ is_yuuhi_anim_bj1 = True
    $ is_yuuhi_anim_bj2 = False
    $ is_yuuhi_anim_bj3 = False
    $ yuuhi_bj_pov_toggle = True
    $ yuuhi_bj_pos_toggle = True
    scene 31_s13 with dissolve
    if cycle == 0:
        yuuhi "Mmm~ [mc] wants to use my mouth?" 
    elif cycle == 1:
        yuuhi "O-on it! I'll make it nice and wet for you~"
    elif cycle == 2:
        yuuhi "Hehe~ I'll be happy to give it some attention~"  
    elif cycle == 3:
        yuuhi "I'll drool a lot on it, [mc]~"
    scene 31_s14 with dissolve
    scene black with Fade(1.0,0.5,0.5)
    jump is_yuuhi_bj2

label is_yuuhi_bj2:
    stop music fadeout 2.0 
    perception "Yuuhi's lips part, a string of saliva stretching between them as she kneels before you."
    show is_yuuhi_anim_bj1 with dissolve
    sensation "Her warm mouth envelops your tip, the slick heat of her tongue swirling around you. She sucks in a slow rhythm, cheeks hollowing as she fights her gag reflex."
    if cycle == 0:
        yuuhi "*Glck* Sho shalty..."  
    elif cycle == 1:
        yuuhi "*Gag* *cough*..."  
    elif cycle == 2:
        yuuhi "*Choke* Nghhh! Sho deep!" 
    elif cycle == 3:
        yuuhi "C-can't... *gasp*... breathe..."
    call screen is_yuuhi_bj_controls with dissolve

label is_yuuhi_bj_cum:
    call screen is_yuuhi_bj_cum with dissolve

label is_yuuhi_bj_cum_inside:
    if is_yuuhi_anim_bj1:
        mc "I'm cumming! Swallow it all!"
        play sound "se_sfx/blowjob/gag2.mp3" 
        scene is_yuuhi_bj9 with vpunch
        sensation "Your throbbing cock twitches against the tight walls of her throat before spilling thick ropes of seed directly down her convulsing esophagus."
        play sound "se_sfx/sex/sex_cum1.mp3" 
        scene is_yuuhi_bj10 with vpunch
        mc "Aghhh!"
        perception "Yuuhi chokes, her nose scrunching as her body instinctively rebels against the overwhelming flood."
        scene is_yuuhi_bj22 with Fade(0.5,0.5,0.5)
        mc "Hah... hah..."
        yuuhi "*cough* I-It's... *hic*... in ma moush..."
        mc "You know what to do."
        yuuhi "Yesh~"
        scene is_yuuhi_bj24 with dissolve
        yuuhi "*gulp* *gulp*"
        scene is_yuuhi_bj23 with dissolve
        yuuhi "Ahhhhhhh~"
        scene is_yuuhi_bj29 with dissolve
        yuuhi "Do you like watching me swallow?"
        scene is_yuuhi_bj30 with dissolve
        mc "It's the hottest thing ever."
        scene is_yuuhi_bj29 with dissolve
        yuuhi "I wonder why... Is it a dominance thing?"
        scene is_yuuhi_bj30 with dissolve
        mc "You know what? I don't think I ever thought about it."
        scene is_yuuhi_bj29 with dissolve
        yuuhi "Regardless, if it makes you happy then I'll try to do it... even though your semen stinks and is so viscous it gets stuck to the back of my throat."
        yuuhi "Not to mention how depraved it is to make a cute girl swallow something that comes out of a penis."
        scene is_yuuhi_bj30 with dissolve
        mc "..."
    elif is_yuuhi_anim_bj2 or is_yuuhi_anim_bj3:
        mc "I'm gonna fill your throat!"
        play sound "se_sfx/sex/sex_cum1.mp3" 
        scene is_yuuhi_bj53 with vpunch
        perception "You hold her in place, groaning as she swallows around you, each gulp sending tremors through her body."
        mc "Nghhh!"
        play sound "se_sfx/sex/sex_cum3.mp3" 
        scene is_yuuhi_bj53 with vpunch
        yuuhi "Glllck~! Mmm! Mmm!"
        perception "Milky bubbles form at the corners of her lips, erupting from her flaring nostrils as she struggles to breathe through the onslaught."
        scene is_yuuhi_bj54 with Fade(0.5,0.5,0.5)
        yuuhi "*cough* S-Shank you... for the... {i}*hick*{/i} tashty shemen..."
        scene is_yuuhi_bj55 with dissolve
        play sound "se_sfx/blowjob/swallow3.mp3" 
        yuuhi "*gulp* *gag*"
        scene is_yuuhi_bj56 with dissolve
        yuuhi "Ahhhhh~"
        scene is_yuuhi_bj60 with dissolve
        mc "Good girl."
        scene is_yuuhi_bj59 with dissolve
        yuuhi "Mhmmm~ It tastes... salty."
        yuuhi "You ever licked a blade before, [mc]?"
        scene is_yuuhi_bj60 with dissolve
        mc "I have not..."
        scene is_yuuhi_bj59 with dissolve
        yuuhi "Well, it kinda tastes like it."
        scene is_yuuhi_bj60 with dissolve
        mc "Wait, how do you know that?"
        scene is_yuuhi_bj59 with dissolve
        yuuhi "Umm... S-So how was your day today?"
        scene is_yuuhi_bj60 with dissolve
        mc "..."
    scene black with Fade(1.0,0.5,0.5)
    perception "Yuuhi dresses up and leaves the room. A sudden burp escapes her lips. She freezes, eyes widening in shock, her cheeks turning a deep crimson. Her gaze flicks to you, flustered and mortified, before she squeaks out a hasty excuse."
    $ yuuhi_total_cum_in_mouth += 4.67
    $ renpy.end_replay()
    jump yuuhi_sex_end

label is_yuuhi_bj_cum_outside:
    if is_yuuhi_anim_bj1:
        mc "i'm gonna cover your face!"
        play sound "se_sfx/blowjob/facial4.mp3" 
        scene is_yuuhi_bj25 with vpunch
        perception "Your seed paints her features in thick, white streaks, dripping down her flushed cheeks."
        play sound "se_sfx/blowjob/facial2.mp3" 
        scene is_yuuhi_bj26 with vpunch
        yuuhi "Eep!"
        perception "Her lashes flutter as she blinks through the mess, strands of seed clinging to her lips."
        scene is_yuuhi_bj28 with dissolve
        yuuhi "*sniff* I-I look... disgusting..."
        yuuhi "But... if you like it..."
        scene is_yuuhi_bj27 with dissolve
        mc "I do like it."
        scene is_yuuhi_bj28 with dissolve
        yuuhi "Mhmm~"
        yuuhi "*giggles* My Pops would lose his mind if he saw me like this."
        scene is_yuuhi_bj27 with dissolve
        mc "You look perfect. If only I had a phone to cement this moment forever."
        scene is_yuuhi_bj28 with dissolve
        yuuhi "Phone? You mean painting me like this?"
        scene is_yuuhi_bj27 with dissolve
        mc "R-Right..."
        scene is_yuuhi_bj28 with dissolve
        yuuhi "That's a step too far... Where would you even hang such a painting?"
        yuuhi "*laughs* Imagine if we had visitors, and they saw it just hanging there in the living room. 'E-Execue me, what's that?!' 'Oh! That's just from the time when [mc] ejaculated all over my face.'"
        scene is_yuuhi_bj27 with dissolve
        mc "*chuckles* You're funny."
    elif is_yuuhi_anim_bj2 or is_yuuhi_anim_bj3:
        mc "i'm cumming!"
        yuuhi "Ahhn!"
        play sound "se_sfx/blowjob/facial4.mp3"
        scene is_yuuhi_bj61 with vpunch
        perception "You unload onto her, coating her skin until she's drenched in your semen."
        play sound "se_sfx/blowjob/facial2.mp3" 
        scene is_yuuhi_bj62 with vpunch
        mc "Aghhhh!"
        perception "Yuuhi shuts her eyes, dazed and breathless, before giving you a hazy, satisfied smile."
        scene is_yuuhi_bj57 with Fade(0.5,0.5,0.5)
        yuuhi "*pant* You love painting my cute little face, don't you?"
        scene is_yuuhi_bj58 with dissolve
        mc "Of course, you're my woman after all."
        scene is_yuuhi_bj57 with dissolve
        yuuhi "I'm [mc]'s woman~"
        scene is_yuuhi_bj58 with dissolve
    scene black with Fade(1.0,0.5,0.5)
    perception "Yuuhi wipes her face with the back of her hand before hastily pulling on her clothes. She kisses you then leaves the room."
    $ renpy.end_replay()
    jump yuuhi_sex_end

label is_yuuhi_bj_pov1:
    $ is_yuuhi_anim_bj1 = True
    $ is_yuuhi_anim_bj2 = False
    $ is_yuuhi_anim_bj3 = False
    $ yuuhi_bj_pov_toggle = True
    $ yuuhi_bj_pos_toggle = True
    scene black with Dissolve(0.3)
    show is_yuuhi_anim_bj1 with dissolve
    yuuhi "*slurp* So big~! I can hardly breath!"
    call screen is_yuuhi_bj_controls with dissolve

label is_yuuhi_bj_pov2:
    $ is_yuuhi_anim_bj1 = False
    $ is_yuuhi_anim_bj2 = True
    $ is_yuuhi_anim_bj3 = False
    scene black with Dissolve(0.3)
    show is_yuuhi_anim_bj2 with dissolve
    yuuhi "Mnnmm~ My pussy starts to get so wet when you take control of my mouth like this~"
    call screen is_yuuhi_bj_controls with dissolve

label is_yuuhi_bj_pos2:
    $ is_yuuhi_anim_bj1 = False
    $ is_yuuhi_anim_bj2 = False
    $ is_yuuhi_anim_bj3 = True
    scene black with Dissolve(0.3)
    show is_yuuhi_anim_bj3 with dissolve
    yuuhi "*gag* *cough* Fhnnmmm~! I feel it all the way down my throat~!"
    call screen is_yuuhi_bj_controls with dissolve


label is_yuuhi_bj_faster:
    if is_yuuhi_anim_bj1:
        show is_yuuhi_anim_bj1_faster with dissolve
        hide is_yuuhi_anim_bj1 with dissolve
        yuuhi "{i}Mghmmm!{/i} You're being so rough with me~"
        yuuhi "I feel like I'm about to spill my pussy liquid from being used like this~!"
        call screen is_yuuhi_bj_controls with dissolve
    elif is_yuuhi_anim_bj2:
        show is_yuuhi_anim_bj2_faster with dissolve
        hide is_yuuhi_anim_bj2 with dissolve
        mc "Ahhn! Your tongue feels so good..."
        yuuhi "{i}*gag* *choke*{/i}"
        call screen is_yuuhi_bj_controls with dissolve
    else:
        show is_yuuhi_anim_bj3_faster with dissolve
        hide is_yuuhi_anim_bj3 with dissolve
        yuuhi "{i}Aghhhh! *gag*{/i}"
        mc "Fuck, Yuuhi! You're trying to swallow down my whole cock!"
        yuuhi "It's an instinctive reaction to having something shoved down your throat!"
        call screen is_yuuhi_bj_controls with dissolve

########################################################################################################################
###############################################YUUJI ASEX#################################################################
########################################################################################################################
default yuuhi_asex_pos_toggle = True
default yuuhi_asex_pov_toggle = True
default is_yuuhi_anim_asex1 = False
default is_yuuhi_anim_asex2 = False
default is_yuuhi_anim_asex3 = False

screen is_yuuhi_asex_controls():
    imagebutton auto "main_choices_op1_%s":
        focus_mask True
        action Jump("is_yuuhi_asex_faster")
    text "Faster":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 832 xanchor 0.5 yanchor 0.5 italic True
    
    imagebutton auto "main_choices_op2_%s":
        focus_mask True
        action [
            ToggleVariable("yuuhi_asex_pos_toggle"), 
            If(yuuhi_asex_pos_toggle, Jump("is_yuuhi_asex_pos2"), Jump("is_yuuhi_asex_pov1"))
        ]
    text "Change position":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 959 xanchor 0.5 yanchor 0.5 italic True

    if is_yuuhi_anim_asex1 == False:
        imagebutton auto "main_choices_op3_%s":
            focus_mask True
            action [
                ToggleVariable("yuuhi_asex_pov_toggle"), 
                If(yuuhi_asex_pov_toggle, Jump("is_yuuhi_asex_pov2"), Jump("is_yuuhi_asex_pos2"))
            ]
        text "Change POV":
            size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 1086 xanchor 0.5 yanchor 0.5 italic True
    else:
        add "main_choices_op3_idle"
        text "Change POV":
            size persistent.choices_text_size color "#818181" font "candara.ttf" xpos 2260 ypos 1086 xanchor 0.5 yanchor 0.5 italic True

    imagebutton auto "main_choices_op4_%s":
        focus_mask True
        action Jump("is_yuuhi_asex_cum")
    text "Cum":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 1214 xanchor 0.5 yanchor 0.5 italic True

screen is_yuuhi_asex_cum():
    imagebutton auto "main_choices_op1_%s":
        focus_mask True
        action Jump("is_yuuhi_asex_cum_inside")
    text "Cum inside":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 832 xanchor 0.5 yanchor 0.5 italic True
    
    imagebutton auto "main_choices_op2_%s":
        focus_mask True
        action Jump("is_yuuhi_asex_cum_outside")
    text "Cum outside":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 959 xanchor 0.5 yanchor 0.5 italic True

label is_yuuhi_asex1:
    $ mcname = persistent.name
    if persistent.name == "None" or mcname == "None":
        while mcname == "None" or mcname == "":
            $ mcname = renpy.input("There was an issue with your name. Please rewrite your name:", length=32)
        $ persistent.name = mcname
    if not persistent.scene3_p3_replay:
        $ persistent.scene3_p3_replay = True
    $ yuuhi_asex = True
    $ is_yuuhi_anim_asex1 = True
    $ is_yuuhi_anim_asex2 = False
    $ is_yuuhi_anim_asex3 = False
    $ yuuhi_asex_pov_toggle = True
    $ yuuhi_asex_pos_toggle = True
    scene 31_s13 with dissolve
    if cycle == 0:
        yuuhi "It's embarrassing but... I'm starting to really like it in the butt." 
    elif cycle == 1:
        yuuhi "I noticed that your... penis gets bigger when you hear me whimper, [mc]~"
    elif cycle == 2:
        yuuhi "My favorite activity as of recently~"  
    elif cycle == 3:
        yuuhi "Go easy on me, [mc]~"
        yuuhi "You know how tight it is..."
    scene 31_s14 with dissolve
    scene black with Fade(1.0,0.5,0.5)
    jump is_yuuhi_asex2

label is_yuuhi_asex2:
    stop music fadeout 2.0 
    perception "Yuuhi shivers as you press against her entrance, her body instinctively tensing before she forces herself to relax. 
    Her breath hitching as your tip teases her tight ass, stretching her inch by inch." 
    show is_yuuhi_anim_asex1 with dissolve
    sensation "Her walls cling greedily around you. A strangled moan escapes her lips, a mix of pleasure and the delicious burn of being filled."
    if cycle == 0:
        yuuhi "I-It's so big...! Ungh... Ahh~" 
    elif cycle == 1:
        yuuhi "Nghhh! Yes! Keep going, [mc]~" 
    elif cycle == 2:
        yuuhi "[mc]'s cock is... r-rearranging... my g-guts...!" 
    elif cycle == 3:
        yuuhi "*whimper*"
    perception "Sweat-slick skin slaps against yours as she rocks between pain and pleasure, her plug abandoned on the floor."
    yuuhi "This feels so much better than my tiny fingers~ Ahnnmm~! It's like trying to compare an ogre with a goblin~!"
    call screen is_yuuhi_asex_controls with dissolve

label is_yuuhi_asex_cum:
    call screen is_yuuhi_asex_cum with dissolve

label is_yuuhi_asex_cum_inside:
    if is_yuuhi_anim_asex1:
        mc "I'm gonna fill your hole!"
        sensation "Your pace turns erratic as the pressure builds, her snug walls milking you for everything you have. 
        Yuuhi's body jolts with each deep thrust, her moans dissolving into breathy gasps."
        play sound "se_sfx/sex/sex_cum4.mp3" 
        scene is_yuuhi_asex22 with vpunch
        sensation "With one final push, you bury yourself to the hilt, releasing thick, molten ropes deep inside her. Yuuhi's eyes roll back as the warmth floods her."
        play sound "se_sfx/sex/sex_cum2.mp3" 
        scene is_yuuhi_asex22 with vpunch
        mc "Aghhh!"
        yuuhi "Amghhhh! My butthole!"
        scene is_yuuhi_asex23 with dissolve
        mc "Hah... hah..."
        scene is_yuuhi_asex24 with dissolve
        yuuhi "Haaaa! I-It's so... hot..."
        scene is_yuuhi_asex23 with dissolve
        mc "You did good. Try to hold it in a little longer."
        scene is_yuuhi_asex24 with dissolve
        yuuhi "Mmmm~ It's already leaking~"
        yuuhi "Why do you want me to keep it in there anyway?"
        scene is_yuuhi_asex23 with dissolve
        mc "Seeing you squirm while trying not to let a drop out will make me go crazy."
        scene is_yuuhi_asex24 with dissolve
        yuuhi "*chuckles* You're {i}such{/i} a pervert~"
        scene is_yuuhi_asex23 with dissolve
    elif is_yuuhi_anim_asex2 or is_yuuhi_anim_asex3:
        mc "I'm gonna breed your ass!"
        sensation "Your pace turns erratic as the pressure builds, her snug walls milking you for everything you have. 
        Yuuhi's body jolts with each deep thrust, her moans dissolving into breathy gasps."
        play sound "se_sfx/sex/sex_cum5.mp3" 
        scene is_yuuhi_asex14 with vpunch
        sensation "A broken sob leaves her lips as she feels you release inside her, her walls clamping down in reflex, milking every last drop."
        mc "Nghhh!"
        play sound "se_sfx/sex/sex_cum1.mp3" 
        scene is_yuuhi_asex14 with vpunch
        yuuhi "Mmm! Mmm!"
        scene is_yuuhi_asex15 with dissolve
        mc "Hah... hah..."
        yuuhi "T-Thank you... *pant*... for... stuffing me..."
        mc "You'll be a good wife, Yuuhi."
        yuuhi "O-Oh... I... T-Thank you, [mc]!"
        yuuhi "I knew that letting my husband have full access to my butthole would be a good idea."
        mc "Explain to me how that's the case."
        yuuhi "Firstly, the more open the wife is to pleasing her husband, the better their relationship is! Also, I have monthly periods, did you know that?"
        mc "Yes, I did know that, Yuuhi..."
        yuuhi "Right. So when that happens, there's no choice but to use my butthole if you want to relive yourself."
        mc "..."
    scene black with Fade(1.0,0.5,0.5)
    perception "Yuuhi dresses up. Her gaping anus trickles down drops of cum all the while."
    $ yuuhi_total_cum_in_ass += 4.24
    $ renpy.end_replay()
    jump yuuhi_sex_end

label is_yuuhi_asex_cum_outside:
    if is_yuuhi_anim_asex1:
        mc "I'm cumming!"
        play sound "se_sfx/sex/touch3.mp3" 
        scene is_yuuhi_sex27 with vpunch
        perception "The moment you pull out, thick, pearly streaks erupt from your tip, splattering across her twitching, gaping hole."
        play sound "se_sfx/blowjob/facial1.mp3" 
        scene is_yuuhi_sex28 with vpunch
        yuuhi "Ahh~! Mmmn... s-so warm! "
        scene is_yuuhi_sex29 with dissolve
        yuuhi "*sniff* Did you... not want to finish inside, [mc]?"
        scene is_yuuhi_sex30 with dissolve
        mc "Inside, outside... does it really matter? You won't get pregnant either way."
        scene is_yuuhi_sex29 with dissolve
        yuuhi "I-I know that pregnancy is futile this way, but I can roleplay as you breeding me when you finish inside~"
        scene is_yuuhi_sex30 with dissolve
        mc "You want to roleplay as me breeding you?"
        scene is_yuuhi_sex29 with dissolve
        yuuhi "Mhm. It's so hot, [mc]. You should try it!"
        scene is_yuuhi_sex30 with dissolve
    elif is_yuuhi_anim_asex2 or is_yuuhi_anim_asex3:
        mc "i'm cumming!"
        sensation "A shudder racks through your body as you yank yourself free at the last second."
        play sound "se_sfx/sex/touch3.mp3" 
        scene is_yuuhi_sex16 with vpunch
        yuuhi "Ahhn!"
        perception "Yuuhi whimpers as she glances back, biting her lip as she feels the sticky heat trickling down her ass."
        play sound "se_sfx/blowjob/facial1.mp3" 
        scene is_yuuhi_sex17 with vpunch
        yuuhi "Ahhn~! S-So much... This amount would definitely make me pregnant on the first try~"
        scene is_yuuhi_sex18 with dissolve
        yuuhi "Do you think there's a chance I will get pregnant if your seed drips down and touches my pussy hole?"
        mc "Umm... it's highly unlikely. It needs to be much deeper."
        yuuhi "Ah, looks like there's still much I need to learn."
        mc "Just don't go learning things from that friend of yours. She seems to be doing more harm than good."
    scene black with Fade(1.0,0.5,0.5)
    perception "Yuuhi wipes off your cum from her ass then dresses up and leaves the room."
    $ renpy.end_replay()
    jump yuuhi_sex_end

label is_yuuhi_asex_pov1:
    $ is_yuuhi_anim_asex1 = True
    $ is_yuuhi_anim_asex2 = False
    $ is_yuuhi_anim_asex3 = False
    $ yuuhi_asex_pov_toggle = True
    $ yuuhi_asex_pos_toggle = True
    scene black with Dissolve(0.3)
    show is_yuuhi_anim_asex1 with dissolve
    yuuhi "Mhngnmm~ Like how flexiable I am, [mc]?"
    mc "I do. I can see your ass and pussy clearly this way."
    yuuhi "It—Mghmm~! It even feels better this way because you can reach deeper~!"
    call screen is_yuuhi_asex_controls with dissolve

label is_yuuhi_asex_pov2:
    $ is_yuuhi_anim_asex1 = False
    $ is_yuuhi_anim_asex2 = True
    $ is_yuuhi_anim_asex3 = False
    scene black with Dissolve(0.3)
    show is_yuuhi_anim_asex2 with dissolve
    yuuhi "Fhmmmnn~! You like it when I squeeze it like this?"
    mc "Yeah, keep it like this."
    yuuhi "I-I can't... every time you—Ahhn~! ...Every time you hit that spot I instinctively let loose~!"
    call screen is_yuuhi_asex_controls with dissolve

label is_yuuhi_asex_pos2:
    $ is_yuuhi_anim_asex1 = False
    $ is_yuuhi_anim_asex2 = False
    $ is_yuuhi_anim_asex3 = True
    scene black with Dissolve(0.3)
    show is_yuuhi_anim_asex3 with dissolve
    yuuhi "You're taking my anal virginity!"
    mc "It's already been taken, girl."
    yuuhi "Pretend you're taking it for the first time again~! My anus was soo tight then that I almost passed out~!"
    call screen is_yuuhi_asex_controls with dissolve

label is_yuuhi_asex_faster:
    if is_yuuhi_anim_asex1:
        show is_yuuhi_anim_asex1_faster with dissolve
        hide is_yuuhi_anim_asex1 with dissolve
        yuuhi "N-Not so rough~ Please, [mc]~"
        mc "I thought you liked it rough?"
        yuuhi "I do! I'm just pretending that I wasn't a complete harlot for anal!"
        call screen is_yuuhi_asex_controls with dissolve
    elif is_yuuhi_anim_asex2:
        show is_yuuhi_anim_asex2_faster with dissolve
        hide is_yuuhi_anim_asex2 with dissolve
        yuuhi "Ahhhh~ My... butt is being wrecked!"
        yuuhi "Faster! Fasstteerrr~!"
        call screen is_yuuhi_asex_controls with dissolve
    else:
        show is_yuuhi_anim_asex3_faster with dissolve
        hide is_yuuhi_anim_asex3 with dissolve
        yuuhi "{i}Ngh! Ngh! AHH~{/i}"
        mc "Oh? You like it when I hit this wall here?"
        yuuhi "Yes~! It's like you're touching my pussy!"
        call screen is_yuuhi_asex_controls with dissolve


########################################################################################################################
###############################################YUUJI FJ#################################################################
########################################################################################################################
screen is_yuuhi_fj_controls():
    imagebutton auto "main_choices_left_op1_%s":
        focus_mask True
        action Jump("is_yuuhi_fj1_faster")
    text "Faster":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 292 ypos 832 xanchor 0.5 yanchor 0.5 italic True
    
    imagebutton auto "main_choices_left_op2_%s":
        focus_mask True
        action Jump("is_yuuhi_fj1_slower")
    text "Slower":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 292 ypos 959 xanchor 0.5 yanchor 0.5 italic True

    imagebutton auto "main_choices_left_op3_%s":
        focus_mask True
        action Jump("is_yuuhi_fj_cum")
    text "Cum":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 292 ypos 1086 xanchor 0.5 yanchor 0.5 italic True

image is_yuuhi_anim_fj1 = Movie(play="images/is_scenes/yuuhi/is_yuuhi_fj/anims/is_yuuhi_anims_fj1.webm", loop=True)
image is_yuuhi_anim_fj1_faster = Movie(play="images/is_scenes/yuuhi/is_yuuhi_fj/anims/is_yuuhi_anims_fj1_faster.webm", loop=True)
label is_yuuhi_fj1:
    $ mcname = persistent.name
    if persistent.name == "None" or mcname == "None":
        while mcname == "None" or mcname == "":
            $ mcname = renpy.input("There was an issue with your name. Please rewrite your name:", length=32)
        $ persistent.name = mcname
    if not persistent.scene4_p3_replay:
        $ persistent.scene4_p3_replay = True
    $ yuuhi_fj = True
    scene 31_s7 with dissolve  
    if cycle == 0:
        yuuhi "My feet? Ohh~ You like them, don't you?"  
    elif cycle == 1:
        yuuhi "Hehe~ You're so dirty, [mc]... You want to see them all messy, don't you?"  
    elif cycle == 2:
        yuuhi "Ehe~ Anything for you, [mc]~ Just sit back and let me take care of it."
    elif cycle == 3:
        yuuhi "{i}Mmn...{/i} Of course~"
    scene 31_s8 with dissolve  
    scene black with Fade(1.0,0.5,0.5)
    jump is_yuuhi_fj2

label is_yuuhi_fj2:
    stop music fadeout 2.0 
    perception "Before she can react, you grab her leg, stripping away her socks in one swift motion. Her toes twitch at the sudden exposure."
    scene is_yuuhi_fj3 with dissolve  
    sensation "Your tongue glides across her delicate soles, tracing every curve and arch with slow, indulgent licks."
    yuuhi "Aah~! Your tongue feels... mmh, so ticklish..."
    scene is_yuuhi_fj1 with dissolve
    yuuhi "Mmmm~"
    scene is_yuuhi_fj2 with dissolve
    perception "You take her toes into your mouth, sucking them one by one, savoring their warmth."
    yuuhi "{i}Nnngh...{/i} Y-You're really... sucking on them..."
    scene is_yuuhi_fj4 with fade
    yuuhi "Like this?"
    show is_yuuhi_anim_fj1 with dissolve
    call screen is_yuuhi_fj_controls with dissolve

label is_yuuhi_fj_cum:
    sensation "The soft friction of her feet, combined with their warm, velvety texture, pushes you over the edge."
    play sound "se_sfx/sex/touch4.mp3" 
    scene is_yuuhi_fj5 with vpunch
    perception "Without a word, Yuuhi presses her feet together, presenting them eagerly, ready for you to mark them with your cum."
    mc "{i}Hnggg!{/i}"
    play sound "se_sfx/blowjob/facial5.mp3" 
    scene is_yuuhi_fj6 with vpunch
    ""
    scene is_yuuhi_fj7 with dissolve
    yuuhi "S-So much~ Just from my feet? Hehe~ You must really love them."
    scene is_yuuhi_fj8 with dissolve
    mc "Your feet are heavenly... Keep taking care of them."
    scene is_yuuhi_fj7 with dissolve
    yuuhi "Of course, [mc]~"
    scene is_yuuhi_fj8 with dissolve
    scene black with Fade(1.0,0.5,0.5)
    perception "She wipes away the mess with a teasing hum before slipping her socks back on."
    $ renpy.end_replay()
    jump yuuhi_sex_end

label is_yuuhi_fj1_faster:
    show is_yuuhi_anim_fj1_faster with dissolve
    hide is_yuuhi_anim_fj1 with dissolve
    yuuhi "Hah~ ah~"
    call screen is_yuuhi_fj_controls with dissolve
label is_yuuhi_fj1_slower:
    show is_yuuhi_anim_fj1 with dissolve
    hide is_yuuhi_anim_fj1_faster with dissolve
    yuuhi "It's okay, we can take our time~"
    call screen is_yuuhi_fj_controls with dissolve

label is_yuuhi_sex_limit:
    if not yuuhi_harem_training_finished:
        scene 31_s15 with dissolve
        yuuhi "Umm... I'm really tired right now... Is it okay if we can continue tomorrow instead?"
        scene 31_s16 with dissolve
    else:
        scene 31_s15 with dissolve
        yuuhi "[mc]... We've done it three times now... I'm honestly really impressed you could keep up with me... but, to be honest, my body feels a little numb right now. Can we take a break and continue tomorrow, please?"
        scene 31_s16 with dissolve
    call screen is_yuuhi with dissolve

########################################################################################################################
###############################################REBECCA HJ#################################################################
########################################################################################################################
image is_reb_anim_hj1 = Movie(play="images/is_scenes/reb/is_reb_hj/is_reb_hj1.webm", loop=True)
image is_reb_anim_hj2 = Movie(play="images/is_scenes/reb/is_reb_hj/is_reb_hj2.webm", loop=True)
image is_reb_anim_hj3 = Movie(play="images/is_scenes/reb/is_reb_hj/is_reb_hj3.webm", loop=True)

image is_reb_anim_hj1_faster = Movie(play="images/is_scenes/reb/is_reb_hj/is_reb_hj1_faster.webm", loop=True)
image is_reb_anim_hj2_faster = Movie(play="images/is_scenes/reb/is_reb_hj/is_reb_hj2_faster.webm", loop=True)
image is_reb_anim_hj3_faster = Movie(play="images/is_scenes/reb/is_reb_hj/is_reb_hj3_faster.webm", loop=True)

default reb_hj_pos_toggle = True
default reb_hj_pov_toggle = True
default is_reb_anim_hj1 = True
default is_reb_anim_hj2 = False
default is_reb_anim_hj3 = False

default reb_hj = False
default reb_bj = False
default reb_asex = False
default reb_fj = False

screen is_reb_hj_controls():
    if not is_reb_anim_hj_speed:
        imagebutton auto "main_choices_op1_%s":
            focus_mask True
            action Jump("is_reb_hj_faster")
        text "Faster":
            size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 832 xanchor 0.5 yanchor 0.5 italic True
    else:
        imagebutton auto "main_choices_op1_%s":
            focus_mask True
            action Jump("is_reb_hj_slower")
        text "Slower":
            size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 832 xanchor 0.5 yanchor 0.5 italic True

    imagebutton auto "main_choices_op2_%s":
        focus_mask True
        action [
            ToggleVariable("reb_hj_pos_toggle"), 
            If(reb_hj_pos_toggle, Jump("is_reb_hj_pos2"), Jump("is_reb_hj_pov1"))
        ]
    text "Change position":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 959 xanchor 0.5 yanchor 0.5 italic True

    if is_reb_anim_hj1 == False:
        imagebutton auto "main_choices_op3_%s":
            focus_mask True
            action [
                ToggleVariable("reb_hj_pov_toggle"), 
                If(reb_hj_pov_toggle, Jump("is_reb_hj_pov2"), Jump("is_reb_hj_pos2"))
            ]
        text "Change POV":
            size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 1086 xanchor 0.5 yanchor 0.5 italic True
    else:
        add "main_choices_op3_idle"
        text "Change POV":
            size persistent.choices_text_size color "#818181" font "candara.ttf" xpos 2260 ypos 1086 xanchor 0.5 yanchor 0.5 italic True

    imagebutton auto "main_choices_op4_%s":
        focus_mask True
        action Jump("is_reb_hj_cum2")
    text "Cum":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 1214 xanchor 0.5 yanchor 0.5 italic True

default is_reb_hj_first = True

label is_reb_hj_first:
    $ mcname = persistent.name
    if persistent.name == "None" or mcname == "None":
        while mcname == "None" or mcname == "":
            $ mcname = renpy.input("There was an issue with your name. Please rewrite your name:", length=32)
        $ persistent.name = mcname
    if not persistent.scene5_p5_replay:
        $ persistent.scene5_p5_replay = True
    if is_reb_hj_first:
        $ is_reb_hj_first = False
        scene 63_s1 with dissolve
        r "So a 'handjob' is the same as jerking, right?"
        scene 63_s2 with dissolve
        mc "Yes. And again... please stop saying it like that."
        scene 63_s1 with dissolve
        r "Alright, alright... Come here."
        scene 63_s2 with dissolve
        $ reb_hj = True
        $ is_reb_anim_hj1 = True
        $ is_reb_anim_hj2 = False
        $ is_reb_anim_hj3 = False
        $ reb_hj_pov_toggle = True
        $ reb_hj_pos_toggle = True
        jump is_reb_hj2
    else:
        jump is_reb_hj1

label is_reb_hj1:
    $ mcname = persistent.name
    if persistent.name == "None" or mcname == "None":
        while mcname == "None" or mcname == "":
            $ mcname = renpy.input("There was an issue with your name. Please rewrite your name:", length=32)
        $ persistent.name = mcname
    if not persistent.scene5_p5_replay:
        $ persistent.scene5_p5_replay = True
    $ reb_hj = True
    $ is_reb_anim_hj1 = True
    $ is_reb_anim_hj2 = False
    $ is_reb_anim_hj3 = False
    $ reb_hj_pov_toggle = True
    $ reb_hj_pos_toggle = True
    $ is_reb_hj_pos2_second = True
    scene 63_s1 with dissolve
    if cycle == 0:
        r "*sigh* Here we go again..."
    elif cycle == 1:
        r "You're addicted, aren't you?"
    elif cycle == 2:
        r "It can't feel {i}that{/i} good...?"
    elif cycle == 3:
        r "Do you want to ejaculate on my breasts?"
    scene 63_s2 with dissolve
    scene black with Fade(1.0,0.5,0.5)
    jump is_reb_hj2

default is_reb_hj2_first = True
label is_reb_hj2:
    stop music fadeout 2.0 
    $ is_reb_anim_hj_speed = False
    show is_reb_anim_hj1 with Fade(1.0,1.0,1.0)
    if is_reb_hj2_first:
        $ is_reb_hj2_first = False
        r "H-Heh... It's already hard. I barely even touched it..."
        mc "That's what you do to me."
        perception "She hesitates for just a moment, biting her lip. Then her hand wraps around your shaft—her grip a little too tight at first, but warm and eager."
        r "I-Is this okay? Too rough?"
        mc "No... it's good. Really good."
        sensation "She starts to move her hand more fluidly, experimenting with rhythm and pressure. Each pump gets smoother, more confident."
        r "It's kind of... fun, seeing you twitch like this..."
        sensation "Her thumb brushes your tip now and then, sending little jolts through your core. Her breath grows a little heavier as the moment drags on."
        r "You're breathing really hard... A-Am I doing it right?"
        mc "You're doing amazing."
        r "*giggle* You really like this, huh..."
        sensation "She quickens her pace now, hand gliding up and down in short, steady strokes. Her fingers squeeze just a little harder, finding a natural rhythm."
        r "I can feel it throbbing... It's so hot..."
    else:
        sensation "Her thumb brushes your tip now and then, sending little jolts through your core. Her breath grows a little heavier as the moment drags on."
        r "You're breathing really hard... A-Am I doing it right?"
        mc "You're doing amazing."
        r "*giggle* You really like this, huh..."
        sensation "She quickens her pace now, hand gliding up and down in short, steady strokes. Her fingers squeeze just a little harder, finding a natural rhythm."
        r "I can feel it throbbing... It's so hot..."
    call screen is_reb_hj_controls with dissolve

label is_reb_hj_pov1:
    $ is_reb_anim_hj_speed = False
    $ is_reb_anim_hj1 = True
    $ is_reb_anim_hj2 = False
    $ is_reb_anim_hj3 = False
    $ reb_hj_pov_toggle = True
    $ reb_hj_pos_toggle = True
    scene black with Dissolve(0.3)
    show is_reb_anim_hj1 with dissolve
    r "Hmph~ Don't worry, I'll make it feel better..."
    call screen is_reb_hj_controls with dissolve

label is_reb_hj_pov2:
    $ is_reb_anim_hj_speed = False
    $ is_reb_anim_hj1 = False
    $ is_reb_anim_hj2 = True
    $ is_reb_anim_hj3 = False
    scene black with Dissolve(0.3)
    show is_reb_anim_hj3 with dissolve
    r "Your tongue... Ahnn~ Gods..."
    mc "I can't wait till your breasts are full of milk."
    r "W-What?! D-Don't say that..."
    sensation "Your lips seal tighter around her nipple as your tongue flicks across its sensitive tip. The soft flesh stiffens even more beneath the pressure."
    r "H-Hey! Don't bite—ngh! Gods, you're like a baby..."
    perception "Her thighs clench instinctively, a faint shiver running through her body as one hand grips your shoulder to steady herself."
    call screen is_reb_hj_controls with dissolve

default is_reb_hj_pos2_first = True
default is_reb_hj_pos2_second = False
label is_reb_hj_pos2:
    $ is_reb_anim_hj_speed = False
    $ is_reb_anim_hj1 = False
    $ is_reb_anim_hj2 = False
    $ is_reb_anim_hj3 = True
    if is_reb_hj_pos2_first:
        $ is_reb_hj_pos2_second = True
        $ is_reb_hj_pos2_first = False
        scene is_reb_hj9 with Fade(1.0,1.0,1.0)
        perception "You rest your head across her lap, your face turned toward her body. Her soft thighs are warm beneath you, steady and comforting."
        scene is_reb_hj10 with dissolve
        r "...Are you really comfortable like this?"
        scene is_reb_hj9 with dissolve
        mc "Very."
        scene is_reb_hj10 with dissolve
        r "Tch... Men."
        scene is_reb_hj11 with dissolve
        sensation "Your fingers trail up her side as your lips reach her chest. The fabric of her top is thin—easy to slip down, exposing one perfect breast."
        r "W-What are you doing? Wait—"
        sensation "You gently kiss around the curve, drawing a surprised gasp from her. Your lips find her nipple, warm and soft, and you suck lightly."
        r "Haaah~ T-That's... not fair..."
        scene is_reb_hj13 with dissolve
        sensation "Her hand hesitates, then wraps around your shaft—slowly, delicately, as if still trying to understand what she's doing."
        show is_reb_anim_hj2 with dissolve
        r "I was supposed to be helping you, n-not the other way around..."
        mc "This helps me relax."
        r "Y-You're impossible..."
        sensation "Her hand moves with growing confidence. Meanwhile, your tongue flicks across her nipple in slow circles. You feel her thigh muscles twitch beneath your cheek."
        perception "Her breath quickens. Her other hand grabs the edge of the mattress behind her for balance."
        r "It's twitching again... You really like this, huh?"
        mc "Love it."
        r "Y-You're lucky I like how warm your mouth feels..."
        sensation "Her hand glides faster, now coated in your arousal. She adjusts her position a little, giving you more access to her breast—even pushing your head gently forward."
        r "Suck harder..."
        sensation "You obey, sealing your lips tighter as her nipple stiffens between your teeth. Her stroking grows more intense, her palm gliding, squeezing, twisting just slightly at the top."
        r "It's going to happen soon, isn't it...?"
        mc "Yeah..."
    elif is_reb_hj_pos2_second:
        $ is_reb_hj_pos2_second = False
        scene black with Dissolve(0.3)
        show is_reb_anim_hj2 with dissolve
        r "Nghnn~ Keep sucking it!"
        perception "Her breast is warm against your mouth, the skin soft and faintly flushed. You feel her nipple throb slightly with each suck, her fingers tangling in your hair."
        r "Ahh~... You're making me feel weird down there..."
        perception "Her legs shift restlessly, her thighs pressing together as her breath quickens. You feel her other hand stroking you a little faster in rhythm with each whimper."
    else:
        scene black with Dissolve(0.3)
        show is_reb_anim_hj2 with dissolve
        r "Mmmmm~ I can't believe I let you do this... But it feels too good~!"
    call screen is_reb_hj_controls with dissolve

default is_reb_anim_hj_speed = False
label is_reb_hj_faster:
    scene black with Dissolve(0.3)
    $ is_reb_anim_hj_speed = True
    if is_reb_anim_hj1:
        show is_reb_anim_hj1_faster with dissolve
        hide is_reb_anim_hj1 with dissolve
        sensation "She tightens her grip and speeds up, each stroke sending a jolt of pleasure through you. The wet sounds of her hand working you echo faintly in the room."
        r "I can feel it pulsing so much... Does my hand feel {i}that{/i} good?"
        call screen is_reb_hj_controls with dissolve
    elif is_reb_anim_hj2:
        show is_reb_anim_hj3_faster with dissolve
        hide is_reb_anim_hj3 with dissolve
        sensation "Her nipple brushes your tongue as her hand pumps you faster, your moans muffled against her breast."
        r "Gods—yes! Between your mouth and this... You're gonna make me lose it..."
        call screen is_reb_hj_controls with dissolve
    else:
        show is_reb_anim_hj2_faster with dissolve
        hide is_reb_anim_hj2 with dissolve
        sensation "You're buried against her chest as her hand moves urgently. Her breath trembles in your ear with every slick motion."
        r "Come on~ Ejaculate. My hand is getting tired!"
        call screen is_reb_hj_controls with dissolve

label is_reb_hj_slower:
    scene black with Dissolve(0.3)
    $ is_reb_anim_hj_speed = False
    if is_reb_anim_hj1:
        show is_reb_anim_hj1 with dissolve
        hide is_reb_anim_hj1_faster with dissolve
        sensation "Her pace is slow and teasing, fingers gliding along your cock. Each stroke leaves a warm trail, keeping you on edge."
        r "Mmm~ You want to enjoy it a little longer?"
        call screen is_reb_hj_controls with dissolve
    elif is_reb_anim_hj2:
        show is_reb_anim_hj3 with dissolve
        hide is_reb_anim_hj3_faster with dissolve
        perception "Your mouth stays latched around her nipple as her hand moves slowly, gently."
        r "Nnnh~ You're sucking so sweetly... I can barely focus..."
        call screen is_reb_hj_controls with dissolve
    else:
        show is_reb_anim_hj2 with dissolve
        hide is_reb_anim_hj2_faster with dissolve
        sensation "Her nipple fills your mouth while her strokes remain slow, deliberate. Her scent, her warmth, her voice—everything surrounds you."
        r "It feels unreal... Don't stop, not yet..."
        call screen is_reb_hj_controls with dissolve

label is_reb_hj_cum2:
    $ reb_tj = False
    $ reb_fj = False
    $ reb_bj = False
    $ reb_sex = False
    if is_reb_anim_hj1:
        mc "Rebecca—I'm gonna cum..."
        r "O-Oh! Wait—!"
        show screen cum
        scene is_reb_hj1 with vpunch
        sensation "You groan as your release hits. Thick ropes shoot across her sweaty breasts, splattering up to her arm. She gasps softly, lips parting in awe."
        scene is_reb_hj2 with vpunch
        r "Ahhn! Hey! where are you aiming!?"
        hide screen cum
        scene is_reb_hj4 with Dissolve(1.0)
        r "Insane... You even covered my breasts with it."
        scene is_reb_hj3 with dissolve
        mc "Sorry. You were too good."
        scene is_reb_hj4 with dissolve
        r "It's fine. Just give me a towel next time, okay?"
        scene is_reb_hj3 with dissolve
        scene black with Fade(1.0,1.0,1.0)
        sensation "She wipes her hand on a cloth nearby, cheeks slightly flushed."
    else:
        mc "I'm close!"
        r "Go ahead! Just don't stop sucking~!"
        show screen cum
        play sound "se_sfx/blowjob/facial5.mp3" 
        scene is_reb_hj5 with vpunch
        sensation "With a heavy gasp, you erupt. Your body arches slightly against her hand, and thick spurts shoot up, some landing on your stomach, others on her wrist and forearm."
        play sound "se_sfx/blowjob/facial3.mp3" 
        scene is_reb_hj6 with vpunch
        perception "She flinches slightly but doesn't stop, milking out the last few pulses with slow, firm strokes."
        hide screen cum
        scene is_reb_hj7 with Dissolve(1.0)
        r "...That's a lot..."
        scene is_reb_hj8 with Dissolve(1.0)
        sensation "You pull away from her breast, lips glistening, her nipple now wet and sensitive."
        mc "Your breasts are heavenly, Rebecca."
        scene is_reb_hj7 with dissolve
        r "Don't say it like that!"
        scene is_reb_hj8 with dissolve
        mc "Sorry..."
        scene is_reb_hj7 with dissolve
        r "*sigh* Hand me something to wipe with..."
        scene is_reb_hj8 with dissolve
    $ renpy.end_replay()
    jump reb_sex_end


########################################################################################################################
###############################################REBECCA FJ#################################################################
########################################################################################################################
image is_reb_anim_fj = Movie(play="images/is_scenes/reb/is_reb_fj/is_reb_fj.webm", loop=True)
image is_reb_anim_fj_faster = Movie(play="images/is_scenes/reb/is_reb_fj/is_reb_fj_faster.webm", loop=True)

screen is_reb_fj_choice01():
    imagebutton auto "main_choices_op1_%s":
        focus_mask True
        action Jump("is_reb_fj_choice01_touch")
    text "Touch":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 832 xanchor 0.5 yanchor 0.5 italic True
    
    imagebutton auto "main_choices_op2_%s":
        focus_mask True
        action Jump("is_reb_fj_choice01_lick")
    text "Lick":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 959 xanchor 0.5 yanchor 0.5 italic True

    imagebutton auto "main_choices_op3_%s":
        focus_mask True
        action Jump("is_reb_fj_choice01_sniff")
    text "Sniff":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 1086 xanchor 0.5 yanchor 0.5 italic True
    
    imagebutton auto "main_choices_op4_%s":
        focus_mask True
        action Jump("is_reb_fj")
    text "Continue":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 1214 xanchor 0.5 yanchor 0.5 italic True

screen is_reb_fj_controls():
    imagebutton auto "main_choices_op1_%s":
        focus_mask True
        action Jump("is_reb_fj_faster")
    text "Faster":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 832 xanchor 0.5 yanchor 0.5 italic True
    
    imagebutton auto "main_choices_op2_%s":
        focus_mask True
        action Jump("is_reb_fj_slower")
    text "Slower":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 959 xanchor 0.5 yanchor 0.5 italic True

    imagebutton auto "main_choices_op3_%s":
        focus_mask True
        action Jump("is_reb_fj_cum")
    text "Cum":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 1086 xanchor 0.5 yanchor 0.5 italic True

label is_reb_fj1:
    $ is_reb_fj_choice01_sniff_first = False
    $ is_reb_fj_choice01_lick_first = False
    $ reb_fj = True
    scene 63_s1 with dissolve
    if cycle == 0:
        r "*sigh* Alright, feet boy~ What a dirty guy my husband turned out to be..."
    elif cycle == 1:
        r "You're addicted, aren't you?"
    elif cycle == 2:
        r "It can't feel {i}that{/i} good...?"
    elif cycle == 3:
        r "Do you want to ejaculate on my breasts?"
    scene 63_s2 with dissolve
    scene black with Fade(1.0,0.5,1.2)
    scene is_reb_fj2 with dissolve
    r "Would you be a good boy and lick them clean?"
    scene is_reb_fj1 with dissolve
    call screen is_reb_fj_choice01 with dissolve
    

default is_reb_fj_first = True
label is_reb_fj_first:
    $ mcname = persistent.name
    if persistent.name == "None" or mcname == "None":
        while mcname == "None" or mcname == "":
            $ mcname = renpy.input("There was an issue with your name. Please rewrite your name:", length=32)
        $ persistent.name = mcname
    if not persistent.scene6_p5_replay:
        $ persistent.scene6_p5_replay = True
    if is_reb_fj_first:
        $ is_reb_fj_first = False
        mc "I was thinking... maybe we could try something different."
        if mc_can_sex_reb:
            mc "I want you to use your feet."
        else:
            scene 63_s1 with dissolve 
            r "If it involves you putting something inside me, the answer's still no, [mc]."
            scene 63_s2 with dissolve
            mc "It's not that. I want you to use your feet."
        scene 63_s3 with dissolve
        r "...What?"
        scene 63_s4 with dissolve
        mc "I'm serious."
        scene 63_s3 with dissolve
        r "You're joking."
        scene 63_s4 with dissolve
        mc "Why would I joke about something like this?"
        scene 63_s3 with dissolve
        r "I mean, I did ask you kiss them before... D-Did that awaken something in you?"
        scene 63_s4 with dissolve
        mc "Maybe it did."
        scene 63_s3 with dissolve
        r "Gods... I don't know how to feel about that."
        r "And how exactly is that supposed to work?"
        scene 63_s4 with dissolve
        mc "I'll show you. Just trust me."
        scene 63_s3 with dissolve
        r "Wait, are you really... attracted to my feet?"
        scene 63_s4 with dissolve
        mc "I am."
        scene 63_s3 with dissolve
        r "Huh... I guess all those years of taking care of my soles weren't for nothing."
        scene 63_s1 with dissolve
        r "*sigh* Fine, feet boy. Show me how this works."
        scene 63_s2 with dissolve
        stop music fadeout 2.0 
        scene is_reb_fj1 with Fade(1.0,1.0,1.0)
        perception "Rebecca lays back on the bed, stretching her legs toward you with an amused smirk. She wiggles her toes at your face."
        scene is_reb_fj2 with dissolve
        r "Well? Don't just stare—show me what all the fuss is about, feet boy."
        scene is_reb_fj1 with dissolve
        call screen is_reb_fj_choice01 with dissolve
    else:
        stop music fadeout 2.0 
        jump is_reb_fj1


label is_reb_fj_choice01_touch:
    scene is_reb_fj3 with Dissolve(1.0)
    sensation "Your fingers trail across the soft curve of her arch. You feel the subtle warmth of her skin, the way her toes twitch under your touch."
    perception "She flexes her foot playfully, letting you rub each toe in turn. Her heel fits perfectly in your palm."
    r "...That actually feels kinda good..."
    scene is_reb_fj1 with Dissolve(1.0)
    call screen is_reb_fj_choice01 with dissolve

default is_reb_fj_choice01_lick_first = True
label is_reb_fj_choice01_lick:
    if is_reb_fj_choice01_lick_first:
        scene is_reb_fj4 with Dissolve(1.0)
        perception "You lean in and press your tongue along her arch, slow and deliberate."
        r "H-Hey—!"
        perception "Her legs tense for a moment in surprise, then relax again."
        sensation "Your tongue laps at the soft skin between her toes. Salty. Clean. Warm."
        scene is_reb_fj2 with Dissolve(1.0)
        r "I-Is that really enjoyable for you? You're such a weirdo..."
        scene is_reb_fj1 with dissolve
    else:
        scene is_reb_fj4 with Dissolve(1.0)
        perception "You lean in and press your tongue along her arch, slow and deliberate."
        r "Good boy~"
        sensation "Your tongue laps at the soft skin between her toes. Salty. Clean. Warm."
        scene is_reb_fj2 with Dissolve(1.0)
        r "Do they look clean to you? Maybe you should try again~"
        scene is_reb_fj1 with dissolve
    call screen is_reb_fj_choice01 with dissolve

default is_reb_fj_choice01_sniff_first = True
label is_reb_fj_choice01_sniff:
    if is_reb_fj_choice01_sniff_first:
        sensation "You inhale slowly. A faint hint of lavender lotion... and something purely her."
        scene is_reb_fj2 with dissolve
        r "Excuse me? What are you doing?"
        scene is_reb_fj1 with dissolve
        mc "Just taking in your sweet smell."
        scene is_reb_fj2 with dissolve
        r "Heh... Pervert."
        scene is_reb_fj1 with dissolve
        perception "Her cheeks flush, but she doesn't pull away."
    else:
        sensation "You inhale slowly. A faint hint of lavender lotion... and something purely her."
        scene is_reb_fj2 with dissolve
        r "How do I smell?"
        scene is_reb_fj1 with dissolve
        mc "Lovely. Almsot euphoric."
        scene is_reb_fj2 with dissolve
        r "Gods, you're weird."
        scene is_reb_fj1 with dissolve
        perception "Her cheeks flush, but she doesn't pull away."
    call screen is_reb_fj_choice01 with dissolve

label is_reb_fj:
    scene is_reb_fj8 with Fade(1.0,1.0,1.0)
    r "Ahh~ That tickles..."
    mc "They're so soft."
    show is_reb_anim_fj with Dissolve(1.0)
    r "Glad you're enjoying yourself, pervert."
    mc "Something wrong?"
    r "Not at all, feet boy."
    mc "Stop calling me that..."
    r "*laughs* Says the man who's humping my soles like a desperate mutt."
    mc "..."
    sensation "Her soles press against your length—warm, velvety, and slightly slick with sweat. She flexes her toes curiously as you slide your shaft between her feet."
    r "Mnn... you're really going through with it, huh?"
    mc "Of course I am..."
    sensation "You thrust slowly between the arches of her feet. Her skin feels incredible—soft from years of careful care, with just the faintest textured ridges that send jolts of pleasure with each stroke."
    perception "Rebecca watches you with flushed cheeks, clearly trying to maintain her confident facade. But her curiosity betrays her—eyes wide, lips parted."
    r "You're breathing heavier already... Does it feel that good?"
    mc "More than good..."
    r "Tch... You're such a pervert."
    sensation "She slides her feet up and down in an alternating rhythm. Her toes curl occasionally, brushing your tip and making your hips twitch."
    mc "Fuck... Rebecca..."
    r "You better not get any on my thighs. Or face. Or stomach."
    mc "Can't promise that..."
    r "Ugh. Men."
    sensation "She squeezes slightly tighter, and her rhythm becomes more confident—smirking as she notices you twitch more violently with every motion."
    r "Say it."
    mc "Say what...?"
    r "Say you love my feet."
    mc "I love your feet, Rebecca..."
    r "Heh~ That's more like it."
    call screen is_reb_fj_controls with dissolve

label is_reb_fj_faster:
    r "Faster? Sure~"
    scene black with Dissolve(0.3)
    show is_reb_anim_fj_faster with dissolve
    hide is_reb_anim_fj
    r "How's this? Huh? You're making such a weird face right now~"
    call screen is_reb_fj_controls with dissolve

label is_reb_fj_slower:
    scene black with Dissolve(0.3)
    show is_reb_anim_fj with dissolve
    hide is_reb_anim_fj_faster
    r "Do you like it when I brush my toes on the tip?"
    r "Maybe I'll let you use them some other time~"
    r "Or maybe you'll wake up one day with them in your mouth, gagging all over them."
    call screen is_reb_fj_controls with dissolve

label is_reb_fj_cum:
    $ reb_tj = False
    $ reb_hj = False
    $ reb_bj = False
    $ reb_sex = False
    $ reb_fj = True
    mc "I'm cumming!"
    r "A-Already?"
    show screen cum
    play sound "se_sfx/blowjob/facial3.mp3" 
    scene is_reb_fj5 with vpunch
    sensation "With a final upward stroke from her arches, the pleasure crests and breaks—you groan as thick strands spill across her soles and ankles, warm and messy."
    play sound "se_sfx/blowjob/facial2.mp3" 
    scene is_reb_fj6 with vpunch
    perception "Rebecca's expression tightens as the first jet hits her skin, followed by another... and another. She stares at the trail glistening between her toes, a mix of disgust and fascination on her face."
    scene is_reb_fj7 with Dissolve(1.5)
    r "...It's everywhere."
    hide screen cum
    mc "Worth it."
    r "Tch... I'm going to need at least two towels for this."
    mc "Or your tongue—"
    r "Say one more word and you're sleeping in the doghouse."
    mc "Noted."
    r "Ugh... Come on, feet boy. Help me clean this mess."
    $ renpy.end_replay()
    jump reb_sex_end