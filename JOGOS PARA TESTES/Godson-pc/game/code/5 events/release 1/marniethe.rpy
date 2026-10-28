label marniem2:

    scene black
    with slowfade

    pause 3.0

    scene a105
    with slowfade

    mar "(Okay... this is mad. This is completely, absolutely mad.)"
    mar "(I'm standing outside my own bedroom with nothing on, thinking about sneaking upstairs to a younger man's room, who I just met....)"
    mar "(Henry is right there, inside the room, asleep, and I should be getting back into bed before I do something stupid.)"

    scene a106
    with medium_dissolve

    mar "(But God.....)"
    mar "(The way he looked at me downstairs, like he wanted to eat me alive... Henry hasn't looked at me like that in years.)"
    mar "(I know I'm not supposed to want that, but my whole body is acting like it's been waiting for it.)"

    scene a107
    with medium_dissolve

    mar "(No sex. That's the rule. I can keep that rule.)"
    mar "(Kissing is bad, touching is worse, and letting him put his hands all over me is probably a terrible idea...)"
    mar "(But it's not sex. It's not the same as what happened with George. It can't be the same.)"

    scene a108
    with medium_dissolve

    mar "(I just want to feel wanted for one night. That's all.)"
    mar "(I want his mouth on mine. I want his hands on my tits. I want to stop feeling invisible.)"
    mar "(Right... bathroom excuse if Henry wakes up. Quiet steps. No panicking. And absolutely, definitely, no sex.)"
    mar "(Well, here we go...)"

    scene black
    with fade

    pause 2.0

    scene marnieup
    with ffast_dissolve

    call godson_locked_cutscene ("gui/marnieup.webm", 31.0, "seen_marnieup") from _call_godson_locked_cutscene_12

    scene a128
    with ffade

    mar "......"
    mar "........."
    mar "............"

    scene a130
    with medium_dissolve

    mar "(Well...here we are...)"
    mar ".........."
    mar "(Should I even do this....?)"

    scene a131
    with medium_dissolve

    mar "(I'm just doing exactly what Henry tells me not to.)"
    mar "(........)"
    mar "(You know what, it's fine, I'm still a woman who has needs. If Henry can't take care of those needs, then I have to look elsewhere. No reason to tell him about it though.)"
    mar "............"

    scene a129
    with medium_dissolve

    mar "(That's it, I'm doing this.)"
    mar "(No turning back now.)"

    stop music2 fadeout 2.0
    stop music fadeout 2.0

    scene black
    with slowfade

    pause 3.0

    scene black
    with slowfade


    if marnie_first_night_invite_route == "evil" or sexwithmarnie:
        jump evilsex
    elif marnie_first_night_invite_route == "sexaddict" or fooledaroundwithmarnie:
        jump sexaddictsex1
    else:
        jump marnie2nd


label evilsex:

    $ sexwithmarnie = True
    $ fooledaroundwithmarnie = False

    voice my_audio["108"]
    nar "As soon as Marnie walks through the door, you tell her your plans to fuck her brains out."
    voice my_audio["109"]
    nar "It's not long before she goes into a fit of rage. She turns, points a finger at you, and says-"

    scene marnienotfuckingyou
    with ffast_dissolve
    call godson_locked_cutscene ("gui/marnienotfuckingyou.webm", 296.01, "seen_notsex1") from _call_godson_locked_cutscene_13

    $ unlock_gallery_scene("marnie")
    jump dad1

label sexaddictsex1:

    $ sexwithmarnie = False
    $ fooledaroundwithmarnie = True

    scene black
    with slowfade

    pause 2.0

    voice my_audio["680"]
    nar "Marnie enters your room without saying a word and stops just inside the doorway, fixing you with a long, unmistakably inviting stare."
    voice my_audio["681"]
    nar "You stare back as she slowly approaches, every step deliberate, that alluring look in her eyes making her intentions increasingly difficult to misunderstand."
    voice my_audio["682"]
    nar "But just before she reaches you, Marnie stops, lifts one bare foot, and extends it towards you... offering a silent command before anything else can begin."

    jump sexwatch

label sexwatch:

    scene marniesexaddict1
    with ffast_dissolve
    call godson_locked_cutscene ("gui/marniesexaddict1.webm", 83.0, "seen_marniesexaddict1") from _call_godson_locked_cutscene_14

    jump chi166


label chi166:

    menu:
        "*Continue.*":


            jump sexwatch2
        "*Keep watching.*":


            window hide
            jump sexwatch


label sexwatch2:

    scene black
    with ffade

    scene marniesexaddict2
    with ffast_dissolve
    call godson_locked_cutscene ("gui/marniesexaddict2.webm", 90.0, "seen_marniesexaddict2") from _call_godson_locked_cutscene_15

    jump chi1667


label chi1667:

    menu:
        "*Continue.*":


            jump marniegone
        "*Keep watching.*":


            window hide
            jump sexwatch2

label marniegone:



    $ fooledaroundwithmarnie = True

    scene black
    with slowfade

    pause 2.0

    play music my_audio["think2"] fadein 2.0

    mar "Oh God... what have I done?"
    mar "That wasn't supposed to happen. I told myself we wouldn't take it that far, and then I lost control all over again."
    mar "I can't believe I've done this to Henry again. After everything we've already put each other through..."

    scene x97
    with medium_dissolve

    mar "The kissing was bad enough, but then I put my mouth on you... and somehow, we ended up having sex."
    mar "It may have only lasted a few moments, but that doesn't make it any less real. You were inside me, and I allowed it to happen."
    mar "Henry trusted me to come upstairs and check on you. Instead, I betrayed him beneath his own roof."

    scene x98
    with medium_dissolve

    mar "Stupid, stupid Marnie! Why do you keep doing things like this!?"
    mar "All you had to do was walk away! But no. You just had to make the same bloody mistake all over again!"

    menu:
        "Marnie, calm down. We both wanted it, and I'm not going to pretend I regret it.":


            scene x99
            with medium_dissolve

            mar "That's precisely the problem! I wanted it, and some foolish part of me still wants more!"
            mar "But wanting you doesn't make what we did acceptable. It only means I failed to stop myself."
            mar "Henry trusted me, and I repaid that trust by sneaking into another man's room and allowing things to go much too far."

            scene x100
            with medium_dissolve

            mar "I need to leave before Henry realizes how long I've been up here."
            mar "Please don't follow me, and don't come downstairs looking at me as though nothing happened. I need time to think."
            mar "We'll speak later... if I can even bring myself to face you again. Goodnight."
        "Well... I enjoyed every second of it. I'm not going to lie about that.":


            scene x99
            with medium_dissolve

            mar "Of course you enjoyed it! You're standing there looking entirely too pleased with yourself!"
            mar "Meanwhile, I have to walk downstairs, look my husband in the eyes, and pretend I wasn't just wrapped around you."
            mar "This may be exciting for you, but I have a marriage downstairs that I've just betrayed all over again."

            scene x100
            with medium_dissolve

            mar "I'm getting out of here before Henry comes looking for me and finds us standing together like this."
            mar "Don't say a word about what happened, not to Henry, not to Martha, and certainly not to anyone attending that party."
            mar "Stay here and give me enough time to compose myself. I'm leaving. Goodnight."
        "It lasted about fifteen seconds. You're acting like we spent the whole night together.":


            scene x99
            with medium_dissolve

            mar "Do not reduce what happened to a bloody stopwatch!"
            mar "You were inside me! Whether it lasted fifteen seconds or fifteen hours, I still had sex with someone who isn't my husband!"
            mar "Honestly, the fact that it happened so quickly only makes me feel more ridiculous. I threw away my judgment without even stopping to think!"

            scene x100
            with medium_dissolve

            mar "I have to get out of this room before you say something else that makes me want to scream."
            mar "If Henry asks, I'll decide what to tell him. You are going to remain here and keep your mouth firmly shut."
            mar "I need to leave now. Please... just stay away from me until I've had time to think."

    jump marnie2nd
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
