define bia = Character("Bianca")
define childs = Character("Bianca's Children")
define rob = Character("Robert")
define chi1 = Character("First Child")
define chi2 = Character("Second Child")

label nina1alt:

    scene black
    with slowfade

    pause 2.0

    play music my_audio["night ambience"] loop
    scene night
    with slowfade
    pause 2.0
    stop music fadeout 1.0

    scene black
    with slowfade

    play music my_audio["apartment4"] loop fadein 2.0

    pause 2.0

    scene r1
    with slowfade

    bia "Alright, you two. Bedtime."
    childs "Goodnight, Mummy."
    bia "Goodnight, loves. Did you say goodnight to Daddy?"
    chi1 "We tried."
    chi2 "He said he was busy again."

    scene r2
    with medium_dissolve

    chi1 "He's always busy."
    chi2 "Even when he stops working, he says he's tired."
    chi1 "We miss playing with him."
    bia "Oh..."
    bia "..........."

    scene r3
    with medium_dissolve
    pause

    scene r4
    with medium_dissolve
    pause

    scene r5
    with medium_dissolve

    bia "......"
    bia "........."
    bia "............."
    childs "......"
    childs "........."
    chi1 "M-Mummy...?"
    bia "!!!"

    scene r6
    with medium_dissolve

    bia "Yes, sweetheart?"

    scene r7
    with medium_dissolve

    chi1 "Are you and Daddy getting divorced?"
    bia "What? No. No, sweetheart."
    chi1 "You don't talk much anymore."
    chi2 "And Daddy never comes out of that room."
    chi1 "We don't want one of you to leave."
    bia "Hey, look at me. Nobody is going anywhere."
    bia "Your dad is stressed, and he's working far too much. That's a grown-up problem. It isn't because of you, and it isn't something you two have to fix."
    bia "He loves you. I love you. I'll talk to him, alright?"
    bia "Now try to get some sleep. We'll talk again in the morning if you're still worried."
    bia "Goodnight, loves. And no television after I close this door."

    scene black
    with slowfade

    play sound my_audio["doorclose"] noloop

    pause 1.5

    play sound my_audio["barefeet3"] noloop

    pause 2.0

    play sound2 my_audio["typing"] loop fadein 1.0

    scene r8
    with medium_dissolve

    rob "........"
    rob ".........."
    rob "............."
    bia "......."
    bia "........."
    bia "Ah-ahem!"

    stop sound
    stop sound2

    scene r9
    with medium_dissolve

    rob "Hm?"
    rob "What is it, honey?"
    bia "The children are finally in bed."
    bia "They tried to say goodnight to you."

    scene r10
    with medium_dissolve

    bia "They said you wouldn't even look up from the computer."
    bia "Robert, they weren't asking for the whole evening. They wanted five minutes with their father."
    bia "They miss you."

    scene r11
    with medium_dissolve

    bia "And tonight, one of them asked if we were getting divorced."
    bia "They see you in this room all day. They see us barely speaking."
    bia "I told them nobody was leaving, but I need you to help me make that feel true."
    bia "This cannot keep being my job alone."

    scene r12
    with medium_dissolve

    rob "........"
    rob "............."
    rob "................."
    rob "...................."

    scene r13
    with medium_dissolve

    rob "That's fine, honey. Thanks."

    play sound my_audio["typing"] loop fadein 1.0
    scene r15
    with medium_dissolve
    pause

    scene r16
    with medium_dissolve

    bia "........"
    bia "............"
    bia "..............."

    scene r17
    with medium_dissolve
    pause

    scene r18
    with medium_dissolve
    pause

    scene r19
    with medium_dissolve
    pause
    stop sound
    stop sound2

    scene bianca1
    with medium_dissolve
    call godson_locked_cutscene ("gui/bianca1.webm", 41.0, "seen_bianca1") from _call_godson_locked_cutscene_16

    play sound my_audio["typing"] loop fadein 1.0
    scene r35
    with medium_dissolve
    pause

    scene r36
    with medium_dissolve

    bia "......."
    bia ".........."
    bia "............."

    scene r37
    with medium_dissolve
    pause

    scene r38
    with medium_dissolve
    pause

    scene r39
    with medium_dissolve
    pause

    scene r40
    with medium_dissolve
    pause

    scene black
    with slowfade

    pause 2.0

    scene r41
    with slowfade

    bia "(I'm tired of having the same argument with the back of his head.)"
    bia "(Every deadline becomes an emergency. Every emergency becomes another reason for our family to wait.)"
    bia "(I've tried being patient. I've tried being understanding. All it's done is teach him that I'll keep carrying everything while he works.)"
    bia "(The children are starting to notice. I can't keep telling them this is normal.)"
    bia "(If he won't make time for this family, I'm done waiting for permission to live my own life.)"

    play sound2 my_audio["slamhand"] noloop
    scene r42
    with hpunch

    bia "(Enough.)"
    bia "(I am not spending another night sitting quietly while he complains about work.)"
    bia "(Maybe he needs to be pulled away from that computer before he remembers there is a life outside it.)"
    bia "(I'm not giving up on us. But I'm done doing all the work by myself.)"
    bia "(Right. Let's see if he can ignore this.)"
    bia "........"
    bia "............"

    scene r43
    with medium_dissolve

    rob "This project is a disaster. They changed the requirements again and still expect it finished tonight."
    rob "How am I supposed to fix all of this in a few hours?"
    bia "......."

    scene r44
    with medium_dissolve

    rob "Every time I fix one problem, they send me three more."
    rob "They can find somebody else to clean up this mess."
    rob "A 'great opportunity.' That's what they called it."
    rob "What a damn joke."
    bia "........"

    scene r45
    with medium_dissolve

    rob "......."
    rob ".........."
    bia "Close the laptop, Robert. We're going out."

    stop sound fadeout 1.0
    scene r46
    with medium_dissolve

    rob "What? Where are we going?"
    bia "Jennifer's birthday party."
    bia "You just said they can find somebody else. Good. Let them."
    rob "Bianca, I was frustrated. I can't just walk away from..."
    bia "You can, and tonight you will. I need to get out of this house, and you're coming with me."

    scene r47
    with medium_dissolve

    bia "And don't tell me you only need ten more minutes. Your ten minutes have lasted three years."
    bia "The children are in bed. We have somewhere to be. For once, work can wait for us."
    bia "I miss having fun with my husband. I want one evening where you're actually there."
    rob "Honey, this deadline is important. Can't you go without me?"
    rob "I swear I'll make it up to you and the kids after I get through this week."

    scene r48
    with medium_dissolve

    bia "No. I'm done accepting 'later.'"
    bia "One night away from that computer will not destroy your career."
    bia "But if nothing changes between us, this marriage might not be so lucky."

    scene r49
    with medium_dissolve

    bia "Close it. Get dressed. We leave in ten minutes."
    bia "The children will be fine for a few hours."
    bia "I'm asking you to show up for me tonight, Robert."
    bia "Please don't make me drag you away from that desk."

    scene r50
    with medium_dissolve

    rob "Bianca. Dammit, wait!"

    scene black
    with slowfade
    stop music fadeout 2.0

    pause 2.0
    stop music fadeout 2.0
    stop sound fadeout 2.0

    jump party1
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
