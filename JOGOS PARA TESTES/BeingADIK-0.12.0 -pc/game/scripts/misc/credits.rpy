screen cred_thanks:
    tag cred_thanks
    if steamConfig:
        text "This game is only a reality thanks to the generous donations and support from thousands of Patrons.\n\nA huge thanks to all my Patrons, past, present, and future ones.\nThank you for trusting me.\n\nThank you for playing!\nSee you in the final season!\nJoin my Discord server for more information.":
            text_align 0.5
            font "fonts/candara.ttf"
            size 40 * persistent.scale_factor
            yalign 0.5
            xalign 0.5
    else:
        text "This game is only a reality thanks to the generous donations and support from thousands of Patrons.\n\nA huge thanks to all my Patrons, past, present, and future ones.\nThank you for trusting me.\n\nThank you for playing!\nSee you in the final season!\nJoin my Discord server for more information.\n Support the game development at {color=#e51475}patreon.com/DrPinkCake{/color}":
            text_align 0.5
            font "fonts/candara.ttf"
            size 40 * persistent.scale_factor
            yalign 0.5
            xalign 0.5
    imagebutton:
        idle "pinkcake_logo_btn"
        xalign 0.98
        yalign 0.95
        action NullAction()

screen skipCreditsScreen:
    tag skipCreditsScreen
    add "2d_jacob_screen_main_scroll" at jacob_screen_main_scroller
    imagebutton:
        idle "credits_invis_button"
        hover "credits_invis_button"
        action Jump("skipped_credits_label")
        xpos 0
        ypos 0
label game_credits:
    play music "<from 2.5>music/ep10/isolation.mp3"
    $ qM = quick_menu
    $ quick_menu = 0
    $ credits_speed = 60
    $ credits_speed2 = 127
    $ credits_speed_bg = (credits_speed2)/17
    $ credits_isPlaying = True
    scene 2d_jacob_screen_main
    show screen skipCreditsScreen
    show credits_fg with dissolve
    $ renpy.pause(1.5)
    hide credits_fg with dissolve
    show cred at Move((0.5, 8.4), (0.5, 0.0), credits_speed, repeat=False, bounce=False, xanchor="center", yanchor="bottom")
    show cred_sage_bg with dissolve
    $ renpy.pause(credits_speed_bg+22)
    hide cred_sage_bg with dissolve
    show cred_jade_bg with dissolve
    $ renpy.pause(credits_speed_bg+22)
    hide cred_jade_bg with dissolve

    show cred_jill_bg
    hide cred
    show credits_ph at Move((0.64, 0.06), (0.64, 0.06), credits_speed2, repeat=False, bounce=False, xanchor="center", yanchor="bottom")
    show cred_patrons1a at Move((0.37, 1.02), (0.37, 1.02), credits_speed2, repeat=False, bounce=False, xanchor="center", yanchor="bottom")
    show cred_patrons1b at Move((0.54, 1.02), (0.54, 1.02), credits_speed2, repeat=False, bounce=False, xanchor="center", yanchor="bottom")
    show cred_patrons1c at Move((0.71, 1.02), (0.71, 1.02), credits_speed2, repeat=False, bounce=False, xanchor="center", yanchor="bottom")
    show cred_patrons1d at Move((0.88, 1.02), (0.88, 1.02), credits_speed2, repeat=False, bounce=False, xanchor="center", yanchor="bottom")
    with dissolve
    $ renpy.pause(credits_speed_bg+4)
    hide cred_jill_bg with dissolve
    hide credits_ph
    hide cred_patrons1a
    hide cred_patrons1b
    hide cred_patrons1c
    hide cred_patrons1d
    with dissolve

    show cred_envy_bg at Move((-0.2,1.0),(-0.2,1.0),credits_speed, repeat=False, xanchor="center",yanchor="bottom")
    show cred_patrons2a at Move((0.37, 1.02), (0.37, 1.02), credits_speed2, repeat=False, bounce=False, xanchor="center", yanchor="bottom")
    show cred_patrons2b at Move((0.54, 1.02), (0.54, 1.02), credits_speed2, repeat=False, bounce=False, xanchor="center", yanchor="bottom")
    show cred_patrons2c at Move((0.71, 1.02), (0.71, 1.02), credits_speed2, repeat=False, bounce=False, xanchor="center", yanchor="bottom")
    show cred_patrons2d at Move((0.88, 1.02), (0.88, 1.02), credits_speed2, repeat=False, bounce=False, xanchor="center", yanchor="bottom")
    with dissolve

    $ renpy.pause(credits_speed_bg+4)

    hide cred_envy_bg with dissolve
    hide cred_patrons2a
    hide cred_patrons2b
    hide cred_patrons2c
    hide cred_patrons2d
    with dissolve

    show cred_camila_bg
    show cred_patrons3a at Move((0.37, 1.02), (0.37, 1.02), credits_speed2, repeat=False, bounce=False, xanchor="center", yanchor="bottom")
    show cred_patrons3b at Move((0.54, 1.02), (0.54, 1.02), credits_speed2, repeat=False, bounce=False, xanchor="center", yanchor="bottom")
    show cred_patrons3c at Move((0.71, 1.02), (0.71, 1.02), credits_speed2, repeat=False, bounce=False, xanchor="center", yanchor="bottom")
    show cred_patrons3d at Move((0.88, 1.02), (0.88, 1.02), credits_speed2, repeat=False, bounce=False, xanchor="center", yanchor="bottom")
    with dissolve

    $ renpy.pause(credits_speed_bg+4)
    hide cred_camila_bg with dissolve

    hide cred_patrons3a
    hide cred_patrons3b
    hide cred_patrons3c
    hide cred_patrons3d
    with dissolve

    show cred_cathy_bg at Move((0.55,1.0),(0.55,1.0),credits_speed, repeat=False, xanchor="center",yanchor="bottom")
    show cred_patrons4a at Move((0.37, 1.02), (0.37, 1.02), credits_speed2, repeat=False, bounce=False, xanchor="center", yanchor="bottom")
    show cred_patrons4b at Move((0.54, 1.02), (0.54, 1.02), credits_speed2, repeat=False, bounce=False, xanchor="center", yanchor="bottom")
    show cred_patrons4c at Move((0.71, 1.02), (0.71, 1.02), credits_speed2, repeat=False, bounce=False, xanchor="center", yanchor="bottom")
    show cred_patrons4d at Move((0.88, 1.02), (0.88, 1.02), credits_speed2, repeat=False, bounce=False, xanchor="center", yanchor="bottom")
    with dissolve
    $ renpy.pause(credits_speed_bg+4)

    hide cred_cathy_bg
    hide cred_patrons4a
    hide cred_patrons4b
    hide cred_patrons4c
    hide cred_patrons4d
    with dissolve


    show cred_riona_bg at Move((-0.2,1.0),(-0.2,1.0),credits_speed, repeat=False, xanchor="center",yanchor="bottom")
    show cred_patrons5a at Move((0.37, 1.02), (0.37, 1.02), credits_speed2, repeat=False, bounce=False, xanchor="center", yanchor="bottom")
    show cred_patrons5b at Move((0.54, 1.02), (0.54, 1.02), credits_speed2, repeat=False, bounce=False, xanchor="center", yanchor="bottom")
    show cred_patrons5c at Move((0.71, 1.02), (0.71, 1.02), credits_speed2, repeat=False, bounce=False, xanchor="center", yanchor="bottom")
    show cred_patrons5d at Move((0.88, 1.02), (0.88, 1.02), credits_speed2, repeat=False, bounce=False, xanchor="center", yanchor="bottom")
    with dissolve
    $ renpy.pause(credits_speed_bg+4)

    hide cred_riona_bg
    hide cred_patrons5a
    hide cred_patrons5b
    hide cred_patrons5c
    hide cred_patrons5d
    with dissolve

    show cred_zoey_bg at Move((-0.2,1.0),(-0.2,1.0),credits_speed, repeat=False, xanchor="center",yanchor="bottom")
    show cred_patrons6a at Move((0.37, 1.02), (0.37, 1.02), credits_speed2, repeat=False, bounce=False, xanchor="center", yanchor="bottom")
    show cred_patrons6b at Move((0.54, 1.02), (0.54, 1.02), credits_speed2, repeat=False, bounce=False, xanchor="center", yanchor="bottom")
    show cred_patrons6c at Move((0.71, 1.02), (0.71, 1.02), credits_speed2, repeat=False, bounce=False, xanchor="center", yanchor="bottom")
    show cred_patrons6d at Move((0.88, 1.02), (0.88, 1.02), credits_speed2, repeat=False, bounce=False, xanchor="center", yanchor="bottom")
    with dissolve
    $ renpy.pause(credits_speed_bg+4)

    hide cred_zoey_bg
    hide cred_patrons6a
    hide cred_patrons6b
    hide cred_patrons6c
    hide cred_patrons6d
    with dissolve

    show cred_maya_bg
    show cred_patrons7a at Move((0.37, 1.02), (0.37, 1.02), credits_speed2, repeat=False, bounce=False, xanchor="center", yanchor="bottom")
    show cred_patrons7b at Move((0.54, 1.02), (0.54, 1.02), credits_speed2, repeat=False, bounce=False, xanchor="center", yanchor="bottom")
    show cred_patrons7c at Move((0.71, 1.02), (0.71, 1.02), credits_speed2, repeat=False, bounce=False, xanchor="center", yanchor="bottom")
    show cred_patrons7d at Move((0.88, 1.02), (0.88, 1.02), credits_speed2, repeat=False, bounce=False, xanchor="center", yanchor="bottom")
    with dissolve

    $ renpy.pause(credits_speed_bg+4)


    hide cred_maya_bg
    hide cred_patrons7a
    hide cred_patrons7b
    hide cred_patrons7c
    hide cred_patrons7d
    with dissolve

    show cred_josy_bg
    show cred_patrons8a at Move((0.37, 1.02), (0.37, 1.02), credits_speed2, repeat=False, bounce=False, xanchor="center", yanchor="bottom")
    show cred_patrons8b at Move((0.54, 1.02), (0.54, 1.02), credits_speed2, repeat=False, bounce=False, xanchor="center", yanchor="bottom")
    show cred_patrons8c at Move((0.71, 1.02), (0.71, 1.02), credits_speed2, repeat=False, bounce=False, xanchor="center", yanchor="bottom")
    show cred_patrons8d at Move((0.88, 1.02), (0.88, 1.02), credits_speed2, repeat=False, bounce=False, xanchor="center", yanchor="bottom")
    with dissolve

    $ renpy.pause(credits_speed_bg+4)

    hide cred_josy_bg
    hide cred_patrons8a
    hide cred_patrons8b
    hide cred_patrons8c
    hide cred_patrons8d
    with dissolve

    show cred_quinn_bg at Move((-0.2,1.0),(-0.2,1.0),credits_speed, repeat=False, xanchor="center",yanchor="bottom") with dissolve
    show cred_patrons9a at Move((0.37, 1.02), (0.37, 1.02), credits_speed2, repeat=False, bounce=False, xanchor="center", yanchor="bottom")
    show cred_patrons9b at Move((0.54, 1.02), (0.54, 1.02), credits_speed2, repeat=False, bounce=False, xanchor="center", yanchor="bottom")
    show cred_patrons9c at Move((0.71, 1.02), (0.71, 1.02), credits_speed2, repeat=False, bounce=False, xanchor="center", yanchor="bottom")
    show cred_patrons9d at Move((0.88, 1.02), (0.88, 1.02), credits_speed2, repeat=False, bounce=False, xanchor="center", yanchor="bottom")
    with dissolve

    $ renpy.pause(credits_speed_bg+4)

    hide cred_quinn_bg
    hide cred_patrons9a
    hide cred_patrons9b
    hide cred_patrons9c
    hide cred_patrons9d
    with dissolve

    show cred_isabella_bg with dissolve
    show cred_patrons10a at Move((0.37, 1.02), (0.37, 1.02), credits_speed2, repeat=False, bounce=False, xanchor="center", yanchor="bottom")
    show cred_patrons10b at Move((0.54, 1.02), (0.54, 1.02), credits_speed2, repeat=False, bounce=False, xanchor="center", yanchor="bottom")
    show cred_patrons10c at Move((0.71, 1.02), (0.71, 1.02), credits_speed2, repeat=False, bounce=False, xanchor="center", yanchor="bottom")
    show cred_patrons10d at Move((0.88, 1.02), (0.88, 1.02), credits_speed2, repeat=False, bounce=False, xanchor="center", yanchor="bottom")
    with dissolve

    $ renpy.pause(credits_speed_bg+4)

    hide cred_isabella_bg
    hide cred_patrons10a
    hide cred_patrons10b
    hide cred_patrons10c
    hide cred_patrons10d
    with dissolve

    show cred_mc_bg with dissolve
    show cred_patrons11a at Move((0.37, 1.02), (0.37, 1.02), credits_speed2, repeat=False, bounce=False, xanchor="center", yanchor="bottom")
    show cred_patrons11b at Move((0.54, 1.02), (0.54, 1.02), credits_speed2, repeat=False, bounce=False, xanchor="center", yanchor="bottom")
    show cred_patrons11c at Move((0.71, 1.02), (0.71, 1.02), credits_speed2, repeat=False, bounce=False, xanchor="center", yanchor="bottom")
    show cred_patrons11d at Move((0.88, 1.02), (0.88, 1.02), credits_speed2, repeat=False, bounce=False, xanchor="center", yanchor="bottom")
    with dissolve

    $ renpy.pause(credits_speed_bg+4)

    hide cred_mc_bg
    hide cred_patrons11a
    hide cred_patrons11b
    hide cred_patrons11c
    hide cred_patrons11d
    with dissolve

    show cred_lily_bg at Move((-0.2,1.0),(-0.2,1.0),credits_speed, repeat=False, xanchor="center",yanchor="bottom") with dissolve
    show cred_patrons12a at Move((0.37, 1.02), (0.37, 1.02), credits_speed2, repeat=False, bounce=False, xanchor="center", yanchor="bottom")
    show cred_patrons12b at Move((0.54, 1.02), (0.54, 1.02), credits_speed2, repeat=False, bounce=False, xanchor="center", yanchor="bottom")
    show cred_patrons12c at Move((0.71, 1.02), (0.71, 1.02), credits_speed2, repeat=False, bounce=False, xanchor="center", yanchor="bottom")
    show cred_patrons12d at Move((0.88, 1.02), (0.88, 1.02), credits_speed2, repeat=False, bounce=False, xanchor="center", yanchor="bottom")
    with dissolve

    $ renpy.pause(credits_speed_bg+4)

    hide cred_lily_bg
    hide cred_patrons12a
    hide cred_patrons12b
    hide cred_patrons12c
    hide cred_patrons12d
    with dissolve

    show cred_derek_bg at Move((-0.2,1.0),(-0.2,1.0),credits_speed, repeat=False, xanchor="center",yanchor="bottom") with dissolve
    show cred_patrons13a at Move((0.37, 0.24), (0.37, 0.24), credits_speed2, repeat=False, bounce=False, xanchor="center", yanchor="bottom")
    show cred_patrons13b at Move((0.54, 0.24), (0.54, 0.24), credits_speed2, repeat=False, bounce=False, xanchor="center", yanchor="bottom")
    show cred_patrons13c at Move((0.71, 0.24), (0.71, 0.24), credits_speed2, repeat=False, bounce=False, xanchor="center", yanchor="bottom")
    show cred_patrons13d at Move((0.88, 0.24), (0.88, 0.24), credits_speed2, repeat=False, bounce=False, xanchor="center", yanchor="bottom")
    with dissolve

    $ renpy.pause(credits_speed_bg+4)

    hide cred_derek_bg
    hide cred_patrons13a
    hide cred_patrons13b
    hide cred_patrons13c
    hide cred_patrons13d
    with dissolve

    label skipped_credits_label:
    stop music fadeout 15
    $ credits_isPlaying = False
    hide credits_fg
    hide screen skipCreditsScreen
    hide cred
    hide credits_ph
    hide cred_patrons1a
    hide cred_patrons1b
    hide cred_patrons1c
    hide cred_patrons1d
    hide cred_patrons2a
    hide cred_patrons2b
    hide cred_patrons2c
    hide cred_patrons2d
    hide cred_patrons3a
    hide cred_patrons3b
    hide cred_patrons3c
    hide cred_patrons3d
    hide cred_patrons4a
    hide cred_patrons4b
    hide cred_patrons4c
    hide cred_patrons4d
    hide cred_patrons5a
    hide cred_patrons5b
    hide cred_patrons5c
    hide cred_patrons5d
    hide cred_patrons6a
    hide cred_patrons6b
    hide cred_patrons6c
    hide cred_patrons6d
    hide cred_patrons7a
    hide cred_patrons7b
    hide cred_patrons7c
    hide cred_patrons7d
    hide cred_patrons8a
    hide cred_patrons8b
    hide cred_patrons8c
    hide cred_patrons8d
    hide cred_patrons9a
    hide cred_patrons9b
    hide cred_patrons9c
    hide cred_patrons9d
    hide cred_patrons10a
    hide cred_patrons10b
    hide cred_patrons10c
    hide cred_patrons10d
    hide cred_patrons11a
    hide cred_patrons11b
    hide cred_patrons11c
    hide cred_patrons11d
    hide cred_patrons12a
    hide cred_patrons12b
    hide cred_patrons12c
    hide cred_patrons12d
    hide cred_patrons13a
    hide cred_patrons13b
    hide cred_patrons13c
    hide cred_patrons13d

    hide cred_envy_bg
    hide cred_mc_bg
    hide cred_cathy_bg
    hide cred_zoey_bg
    hide cred_isabella_bg
    hide cred_riona_bg
    hide cred_josy_bg
    hide cred_jade_bg
    hide cred_lily_bg
    hide cred_derek_bg
    hide cred_maya_bg
    hide cred_camila_bg
    hide cred_sage_bg
    hide cred_quinn_bg
    hide cred_jill_bg
    show screen cred_thanks with dissolve
    $ renpy.pause()
    hide screen cred_thanks with dissolve
    if not steamConfig:
        if not nonPatreonConfig:
            scene 2d_jacob_screen_main
            show version_end
            $ renpy.pause()
            hide version_end
    scene bsky
    if not steamConfig:
        $ renpy.pause()
        scene 2d_jacob_screen_main
        if not nonPatreonConfig:
            show patreon_promo
            $ renpy.pause()
    else:
        $ game_is_ending = True
        show screen dlc
        pause
        $ game_is_ending = False
    $ quick_menu = qM
    return

init python:
    credits = ("Created by", "Dr PinkCake"), ("Proofreading by", "Ignatz"), ("Beta testers", "ParX\nN7\nDasati\nDorian Rast\nChiss"), ("Discord staff", "N7\nDasati\nDorian Rast\nBender\nheOy\nChiss\nClau"), ("Special thanks to former staff", "dAAAMN313\nDawe\nDodgyNomad\nEnyo\nTommybuns\nZangs"), ("Jacob's 2D art commissioned by","FlowerXL"),("Arieth model by courtesy of","Dawe3DArts"),("Ermine drawings commissioned by","Monniponi"),("Special thanks","renpytom\nmill29"),\
("","{size=%d}{color=#fe9416}Music {/color}{color=#ffffff}(Creative commons license for commercial use){/color}{/size}" % (40 * persistent.scale_factor)),\
("","Slow day blues - A to Z guitars"),\
("","03 Three's a crowd- Absentrealities"),\
("","04 Surf punk rock - Absentrealities"),\
("","Adventure - Alexander Nakarada"),\
("","Blood And Steel - Alexander Nakarada"),\
("","[[Classical] Freedom - Alexander Nakarada"),\
("","[[Rock n Roll] Jack the Lumberer - Alexander Nakarada"),\
("","[[Acoustic] Journey Of Hope - Alexander Nakarada"),\
("","Medieval Loop One - Alexander Nakarada"),\
("","Medieval Loop Two - Alexander Nakarada"),\
("","Medieval Loop Three - Alexander Nakarada"),\
("","[[Melodic Piano] Reaching the sky - Alexander Nakarada"),\
("","[[Acoustic] Relaxing Ballad - Alexander Nakarada"),\
("","[[Acoustic Ballad] Rustic Ballad - Alexander Nakarada"),\
("","[[Acoustic & Ballad] Simple Ballad - Alexander Nakarada"),\
("","Uplifting Ballad - Alexander Nakarada"),\
("","Skeleton Keys - Alexander Nakarada"),\
("","[[Piano] Spring in Russia- Alexander Nakarada"),\
("","The crown - Alexander Nakarada"),\
("","[[Piano Improvisation] Winter - Alexander Nakarada"),\
("","STRYV Surge (Ivory Remix) - Arlindo Detomi"),\
("","Driving Rock - AShamaluevMusic"),\
("","Energetic - AShamaluevMusic"),\
("","Inspirational Piano Ambient - AShamaluevMusic"),\
("","Inspiring Acoustic - AShamaluevMusic"),\
("","Inspiring Acoustic Guitar and Choir - AShamaluevMusic"),\
("","Optimistic - AShamaluevMusic"),\
("","Piano Cinematic - AShamaluevMusic"),\
("","Romantic Piano- AShamaluevMusic"),\
("","Cosmos - Bare Weed"),\
("","Just Peachy (original) - Bellsmarie"),\
("","Art Nouveau - Chriszornstudios"),\
("","Metal - Chrys Guth"),\
("","Lonely - Chukura"),\
("","Wise old river (Acoustic version) - Daniel Couper"),\
("","Adventure - DarkMoloko"),\
("","Feel bad - Desert sharks"),\
("","Jingle - Ds'Air"),\
("","All of the pieces - Emily Ventre"),\
("","Metal - Free Royalty Free Music"),\
("","Merry Bay - Ghostrifter Official"),\
("","Midnight Stroll - Ghostrifter Official"),\
("","Morning Routine - Ghostrifter Official"),\
("","Subtle Break - Ghostrifter Official"),\
("","Unknown power [[Deep Bass track] - HodgeY"),\
("","Halloween - HoliznaCC0"),\
("","Apra - Hyde"),\
("","60s & 70s Rock Fleetwood Mac Inspired Instrumental - Hyde"),\
("","Drum&Bass Rock Pendulum Inspired Instrumental - Hyde"),\
("","Mumford & Sons Inspired - Hyde"),\
("","Good old days - Jantrax"),\
("","Rio - Jantrax"),\
("","Second Chance - Jantrax"),\
("","Roads (Original Mix) - Jet Voon"),\
("","Anachronist - Kevin MacLeod"),\
("","First call - Kevin MacLeod"),\
("","Fluffing a Duck - Kevin MacLeod"),\
("","Marty Gots A Plan - Kevin MacLeod"),\
("","Octoblues - Kevin MacLeod"),\
("","Radio Martini - Kevin MacLeod"),\
("","Sing Along with Jim - Kevin MacLeod"),\
("","Windswept - Kevin MacLeod"),\
("","Chill - Loudtech"),\
("","Acoustic - Mason Carter Music"),\
("","Fallen Colors (Original mix) - Meizong"),\
("","Night Lights (Original mix) - Meizong"),\
("","No Comments (Original mix) - Meizong"),\
("","Phate (Original mix) - Meizong"),\
("","Raveyard (Original Mix) - Meizong"),\
("","Reaching Halo - Meizong & Yeeflex"),\
("","Skyline (Original mix) - Meizong [[Argofox]"),\
("","Starfire (Original Mix) - Meizong"),\
("","The Heat (Original Mix) - Meizong"),\
("","Don't Count On Me - Melodic In Fusion"),\
("","Faked Reality - Melodic In Fusion"),\
("","Isolation - Melodic In Fusion"),\
("","EmptyV - Melodic In fusion"),\
("","See You Smile - Melodic In Fusion"),\
("","This silence - Melodic In Fusion"),\
("","Time goes by - Melodic In Fusion"),\
("","Funk rock instrumental - Mironov Sound"),\
("","The Unbound Inn - Nerdy Metalhead"),\
("","By your side - Nicolai Heidlas"),\
("","Golden alley - Nicolai Heidlas"),\
("","Let's begin - Nicolai Heidlas"),\
("","Lost souls - Nicolai Heidlas"),\
("","Never give up - Nicolai Heidlas"),\
("","Roadtrip - Nicolai Heidlas"),\
("","Rockin' Riff - Nicolai Heidlas"),\
("","Someways - Nicolai Heidlas"),\
("","Sunny acoustic rock - Nicolai Heidlas"),\
("","Wings - Nicolai Heidlas"),\
("","Winter sunshine - Nicolai Heidlas"),\
("","The Sound Of Summer - Oskar Hill & Meizong"),\
("","Guitar Gentle - PeriTune"),\
("","Guitar Melancholy - PeriTune"),\
("","Guitar Melancholy2 - PeriTune"),\
("","Gentle Theme2 Guitar - PeriTune"),\
("","Gentle Theme2 MusicBox - PeriTune"),\
("","Gentle Theme2 Piano - PeriTune"),\
("","Suspense5 - PeriTune"),\
("","Classicals breakbeat - Punk rock mashed up"),\
("","Heavy - Ryan Pollard TK-473"),\
("","Credits - Ryansyah R. Poetra"),\
("","Food chain - Sean Danielsen"),\
("","Black box - Silent Partner"),\
("","DC Love Go-Go - Silent Partner"),\
("","Get back - Silent Partner"),\
("","Let her in - Silent Partner"),\
("","Scrapbook - Silent Partner"),\
("","Some obsession - Silent Partner"),\
("","Hot Mustard - S Strong"),\
("","Slavic Battle Theme - Steven O'Brien"),\
("","My heart - Summertime"),\
("","Down - The Night"),\
("","Medicate me - The Night"),\
("","Relax - The Sisonpyh"),\
("","Halloween Again - The Zombie Dandies"),\
("","The Friendly Monster Shop - The Zombie Dandies"),\
("","Acoustic guitar arrangement for song - TRow"),\
("","Your smile - Valtteri Kujala"),\
("","Fresh Air Original Instrumental Indie rock/pop - Wayne John Bradley"),\
("","They Say - Wowa"),\
("","\n{size=%d}{color=#fe9416}Music {/color}{color=#ffffff}by courtesy of {color=#fe9416}Dirty Toy Company{/color}{/color}{/size}" % (40 * persistent.scale_factor)),\
("","Burn You Down - Dirty Toy Company"),\
("","Over the Horizon - Dirty Toy Company"),\
("","Stand and Fight - Dirty Toy Company")

    credits2 = ("","GooseQuack"),\
("","Knightwalker"),\
("","MrAug360"),\
("","Demented Reaper"),\
("","TheDuck"),\
("","Andresen"),\
("","Mistress Elemental"),\
("","Peerless Girl"),\
("","TheDctr007"),\
("","Du"),\
("","Jamiro"),\
("","IMxCrusada"),\
("","Tre_ZEN"),\
("","The Exception"),\
("","Hootenanee"),\
("","Markus K."),\
("","XIII Ghost"),\
("","BlackyTGC"),\
("","Raidin"),\
("","Jrderhuntr"),\
("","Agni"),\
("","CheMat"),\
("","Geralt Of Ashkelon"),\
("","Space Cat"),\
("","Blind Cat"),\
("","TheNavigator"),\
("","Touhara Kiminonawa"),\
("","Lehua"),\
("","Cyrano"),\
("","Henry \"Mushu\" Chen"),\
("","thuganomics85"),\
("","Dark Wanderer"),\
("","BunnyRabbit"),\
("","Courun Yauntyrr"),\
("","Kevin from Queensland"),\
("","Fiy"),\
("","Legend Teigen"),\
("","Anekei"),\
("","Judgement Kazzy"),\
("","NicOdin"),\
("","Dravald"),\
("","Sageoson"),\
("","Bruce Zhiyu"),\
("","Kristof_E"),\
("","Unckie V"),\
("","Errol"),\
("","Achtag"),\
("","GnotGnap"),\
("","Chamber691"),\
("","DoerflerN256"),\
("","BoxerBlake"),\
("","The Quiet Wolf"),\
("","Valkyr"),\
("","KobeMags"),\
("","MonSe75"),\
("","Volttx"),\
("","Odofondas"),\
("","Gus Chiggins"),\
("","Chus El Grande"),\
("","DahBobaPanda"),\
("","DaveT"),\
("","GallivantingGlobetrotter"),\
("","Kujo Nakayama"),\
("","Ville \"Turso\" Topi"),\
("","Martin Grozdanov"),\
("","Milasecond"),\
("","Megatron"),\
("","Monki"),\
("","Superchat"),\
("","Raptures Demise"),\
("","R4MPZY"),\
("","Jamison"),\
("","Andy Pops"),\
("","Lectiuss"),\
("","Dacks"),\
("","KrazyCooter52"),\
("","DevilishlySinful"),\
("","Thomas Kain"),\
("","Magician14"),\
("","devarius2005"),\
("","The Other Corey"),\
("","JimboSolo"),\
("","Milkman"),\
("","Andres Reyes \"Blue\""),\
("","Fede_Nico90"),\
("","Anton."),\
("","Kaine Scott Francis"),\
("","turbinho07"),\
("","Bamallama626"),\
("","Gig17"),\
("","Fyrtue"),\
("","Austin Atwood"),\
("","Mike Pearce"),\
("","Hazel"),\
("","VeKyJa"),\
("","AcerProHp"),\
("","J H Trickey"),\
("","DLGG"),\
("","Hedden"),\
("","Littlejohn"),\
("","Diver"),\
("","Chaotic"),\
("","Scotty D"),\
("","John D Rockefeller"),\
("","Albert R"),\
("","JeremySolo"),\
("","Boy Cook"),\
("","Jakesimmii"),\
("","Michael Maimone"),\
("","BulbasaurRave"),\
("","Lollipappy"),\
("","Goofy Wolverine"),\
("","Dr.Pancakes"),\
("","Chillhelm"),\
("","snip_cz"),\
("","Dish aka Goofy Gamer"),\
("","RainyNoir"),\
("","Bender"),\
("","Hargmenrar"),\
("","Lesleythekid"),\
("","Encaitar"),\
("","Nobuddy"),\
("","Beast of Bray"),\
("","Ahlex"),\
("","Rob The Panty Sniffer"),\
("","GingerAvenger51"),\
("","InsanePyrDragon"),\
("","ProfessorWhiskers"),\
("","Kreedom"),\
("","Nightpopcorn456"),\
("","DevlynD"),\
("","PainTrainPanda"),\
("","Scoog"),\
("","Dolphintales"),\
("","Midget Smalls"),\
("","Xavier Xiong"),\
("","Misakhi"),\
("","IstvanT"),\
("","Eyox76"),\
("","Cinder"),\
("","Derick Garcia"),\
("","Cico"),\
("","Richard Lyle (The Fat Explorer)"),\
("","Nightingale172"),\
("","Chris65687"),\
("","GrimPao"),\
("","Boris Xanovavych"),\
("","smokey grey"),\
("","Sava"),\
("","Coco"),\
("","KessY"),\
("","Exorikk"),\
("","Laureline"),\
("","UnequalSym"),\
("","Andrew Stevens"),\
("","Draven"),\
("","Gapesy"),\
("","FlyDaBro"),\
("","Wolfegrimm"),\
("","Brando Meatstick"),\
("","Chance C"),\
("","Micheal Ortiz"),\
("","RTKMason"),\
("","Mahani"),\
("","Templar366"),\
("","Castor833"),\
("","Sebastian Larsen"),\
("","Garithian"),\
("","its El Gio"),\
("","Liborex"),\
("","ForceLord"),\
("","Alkaline"),\
("","lduke1990"),\
("","Swarley1337"),\
("","James B."),\
("","Sg22"),\
("","Dorian Rast"),\
("","Tallbuilding72"),\
("","YaBoiiKrunch"),\
("","Sintei"),\
("","DaveyD"),\
("","Jonas Jalapeños"),\
("","Eduardo Vazquez"),\
("","Shia Fall"),\
("","Luca Gambit"),\
("","Reedy97"),\
("","Iconas"),\
("","Mark Brundish"),\
("","Ricky Giovagnoli"),\
("","Travis W"),\
("","Venrist"),\
("","AggieSlimer"),\
("","Ryo69"),\
("","Elke"),\
("","Alexey Malynov"),\
("","T.Burgos"),\
("","Ybq29"),\
("","KeithSchlumbrecht"),\
("","GentlemanCorpse"),\
("","KelseyDrew"),\
("","Mr.E"),\
("","Billyboy"),\
("","Linuxathlon"),\
("","Nick B"),\
("","GV"),\
("","MrRage67"),\
("","Gillian Ferber"),\
("","oC Hydra"),\
("","Mordechai Blumstein"),\
("","Smiley Yo"),\
("","ThatOneBlackSuperHero"),\
("","Todd Goober"),\
("","CasrerXD"),\
("","JC Oakley"),\
("","Vespiex"),\
("","FerVlucht"),\
("","OmniOmega"),\
("","Ksteelwall21"),\
("","Jia69"),\
("","TheRastaPhoenix"),\
("","RyanD"),\
("","John Vayas"),\
("","Graffis"),\
("","Obeze Ducc"),\
("","RagingPekka"),\
("","A Braidford"),\
("","Donavan"),\
("","J Jonah"),\
("","Keith Schlumbrecht"),\
("","TakeruShu"),\
("","Merlin"),\
("","Schalimo"),\
("","Sorbid"),\
("","Immentale"),\
("","Serpsss"),\
("","Marco Kuiter"),\
("","MysticusMX"),\
("","Terrial"),\
("","Kyler Wilson"),\
("","MuchoRusso :3"),\
("","Mike Nevares"),\
("","Sotos Jos"),\
("","Ninjadude"),\
("","Spencer Kjorstad"),\
("","JebtheReb"),\
("","Buckeyerard"),\
("","Spooky Ghoul"),\
("","Niccolado"),\
("","ETCL"),\
("","AstrexXx"),\
("","Crowbar"),\
("","Palomenian Briass"),\
("","Kanyegula"),\
("","h3ung"),\
("","Raltar"),\
("","ZADRO"),\
("","Seabass"),\
("","Siwash"),\
("","Joenichh"),\
("","Lhua&Bi"),\
("","Chugworth"),\
("","Nickatron"),\
("","old_norseman"),\
("","Andr0id"),\
("","Wolfsen"),\
("","Joetechno85"),\
("","KamCA"),\
("","Rabler"),\
("","DonkeyPuncher"),\
("","Yama_No_Andre"),\
("","Raynn"),\
("","Nexus"),\
("","Tony Bell"),\
("","TKuniyou"),\
("","Dark Gnark"),\
("","The_Prof"),\
("","QuickKobold"),\
("","akaLiv"),\
("","Nordwolf"),\
("","Teejay Andhouses"),\
("","Daniil Gavrilov"),\
("","Black-X"),\
("","Myron “NEJi” Jones Jr."),\
("","Matija \"MAT\" Sikic"),\
("","Audon"),\
("","MaRaider"),\
("","Matt G"),\
("","John \"Tony Much\" White"),\
("","MusicalPenguino"),\
("","Bryan Chevalier"),\
("","Kodyy"),\
("","papa_bearly"),\
("","Nachito×Fajitas Peña"),\
("","Deep Star (TerRapTus)"),\
("","FateInDarkness"),\
("","Cheeteezy08"),\
("","Teufelhunde DJI"),\
("","CØLD"),\
("","Celestia [[Cordelia/Vexy]"),\
("","ZackNero03"),\
("","Anomaly"),\
("","Barracade 167"),\
("","Killdead1119"),\
("","Felldoys"),\
("","IamMarty132"),\
("","Spidykhan"),\
("","Furbal"),\
("","Jdog"),\
("","JurassicTwizzler"),\
("","The A/V Club"),\
("","Pseudolurker"),\
("","Texas2243"),\
("","Codie"),\
("","Phearsen"),\
("","xjacobadobo"),\
("","Steven Hagen"),\
("","Malus"),\
("","PC5517"),\
("","Fotivator"),\
("","Mad God"),\
("","Cryosy"),\
("","Philip R Rogers"),\
("","Michael Matta"),\
("","Kozmicsin"),\
("","Altair P"),\
("","Johnny"),\
("","Catu"),\
("","BryGuy"),\
("","Jon Jester"),\
("","Drew A"),\
("","Andrew V"),\
("","Sanapa"),\
("","Daniel Caton"),\
("","Chad Denmead"),\
("","AJ Casino"),\
("","Trunks Parker"),\
("","Apex"),\
("","Andr4d3F4bi0"),\
("","Chris \"SkyFox\" J"),\
("","Richard Bruce"),\
("","Band"),\
("","IskSMF"),\
("","Eddie Catich"),\
("","tonymack21 gaming"),\
("","Jango Fett"),\
("","JoeyTai"),\
("","Skammer22"),\
("","ShaYu"),\
("","X32"),\
("","EchoFoxtrot"),\
("","Chris Hughes"),\
("","SevenSorrows"),\
("","Brash"),\
("","Legione"),\
("","M4R4Z"),\
("","Adr1jus"),\
("","Darma"),\
("","Kyokann"),\
("","Matouš Pánek"),\
("","Valdis300"),\
("","DamoTheHuman"),\
("","Bishop"),\
("","rcclark92"),\
("","Blacksky003"),\
("","The Trickster's DIK"),\
("","DarylAnon"),\
("","Tanish"),\
("","Deadfall39"),\
("","StarRanger"),\
("","RJayFame2014"),\
("","Alexx992"),\
("","Cjixeres"),\
("","Robbie"),\
("","Lee x Project"),\
("","White Rhino"),\
("","The 6uys"),\
("","MDK Rhino"),\
("","PHIISON"),\
("","Moratyr"),\
("","ShadowAE"),\
("","Wutskrakin"),\
("","FatWolf"),\
("","Inky"),\
("","PhelanPKell"),\
("","Redwolf900"),\
("","TigerDIK"),\
("","Relo"),\
("","Souledge"),\
("","Fallen1o9"),\
("","Laguna_25"),\
("","Kcell"),\
("","SLOBRUH"),\
("","Lucifer"),\
("","hperk209"),\
("","NeverForever13"),\
("","Kranckiss"),\
("","TomaxTK"),\
("","AzeroFTW"),\
("","Insomniac Charms"),\
("","Boomski"),\
("","IzztheGreat"),\
("","Array"),\
("","NewtFaced"),\
("","Rhaya Vae"),\
("","Adde91"),\
("","LegendarySnail"),\
("","theamazingpickle"),\
("","si22"),\
("","Axosiel"),\
("","poncorke"),\
("","ChaseHammer"),\
("","dunners8312"),\
("","_FY_"),\
("","Mith"),\
("","Karasu"),\
("","ComeWashMyBack"),\
("","yuan47"),\
("","VainfulOcelot"),\
("","Dias"),\
("","Bamfzilla"),\
("","Bald Bandicoot"),\
("","Juiceboxx"),\
("","Pyromander"),\
("","Innocent Bystander"),\
("","B Townsend"),\
("","Flamingo0213"),\
("","EpIsaace"),\
("","Dick Thundernutz"),\
("","Scootrk"),\
("","Dillon W"),\
("","Kuzo"),\
("","Cahuela"),\
("","Rellik6801"),\
("","Potato Prophet"),\
("","RoseOpium"),\
("","XoF"),\
("","Talinova"),\
("","Traeix"),\
("","F1gure8"),\
("","Homesixks"),\
("","JEH"),\
("","DistantHoliday"),\
("","Prof_Amezy"),\
("","Jakonus303"),\
("","RedPandaMan"),\
("","TenthWolf"),\
("","CreepyInsane"),\
("","Teresjulo"),\
("","GentleGiant"),\
("","Infidel"),\
("","EvilJackal"),\
("","BusinessBill"),\
("","DirtyGuy1"),\
("","FishCakee"),\
("","JP3Games"),\
("","Smunch"),\
("","Djandsam"),\
("","Mr. Worldwide"),\
("","Ladenbigdog1"),\
("","Yanis Panagaris"),\
("","Colt J.T."),\
("","Lonely Fermata"),\
("","Tolga Yayan"),\
("","xBuddx"),\
("","Sad Little Squonk"),\
("","Matze905"),\
("","Harrison H."),\
("","Void1995"),\
("","nobrainer"),\
("","Iska"),\
("","rannhuehue"),\
("","TurinAtmos"),\
("","Tonyv1324"),\
("","BigPappE"),\
("","TripodGG"),\
("","El Bicho"),\
("","Armyman0187"),\
("","Magnumzero"),\
("","Sir Waxy"),\
("","Hyral"),\
("","xQc"),\
("","Paltse"),\
("","Dr Nurse MJB"),\
("","Thorgon"),\
("","Stitchy"),\
("","Taryn Jane"),\
("","PetBuddha"),\
("","MoonPiece"),\
("","Baalzie"),\
("","Chopper323"),\
("","OzzWooT"),\
("","Bobby Halpin"),\
("","Nathan Enkay"),\
("","obtain"),\
("","Mo0rk"),\
("","Thearticgamer43"),\
("","Scornful"),\
("","Oniya"),\
("","Denster1991"),\
("","Bimble"),\
("","Tyler Robbins"),\
("","Zaioed"),\
("","Jing Cheng Lin"),\
("","dayandmorrow"),\
("","Tann13"),\
("","Grenader"),\
("","The Wlyde One"),\
("","BlazingBlue"),\
("","Blacknyellow962"),\
("","NME"),\
("","Englen"),\
("","Jimbo"),\
("","BombenLP"),\
("","sunlockfire"),\
("","Guihras"),\
("","Chris Lampe"),\
("","Dany^^"),\
("","Zabios"),\
("","Paappoio"),\
("","Milo.Dracon"),\
("","SlipperyJim"),\
("","Miniweener"),\
("","Brädwurst"),\
("","BTFCoFounder"),\
("","TonytheTiger"),\
("","Bow"),\
("","TwisterVult"),\
("","Goobie"),\
("","TheAlphaNomad"),\
("","C3NTUR10N"),\
("","Incog"),\
("","Style"),\
("","Kinka"),\
("","Flux"),\
("","KrombompolousSycheal"),\
("","PimpMonkey33"),\
("","Rakzorr"),\
("","JayTokyo"),\
("","Bubbless"),\
("","Clau"),\
("","Shab Gaung"),\
("","Adde"),\
("","Izeiza"),\
("","MGotzex"),\
("","TheDCTR"),\
("","SURVIVOR2281"),\
("","Iridium Brian"),\
("","Igor.M"),\
("","Galaaz"),\
("","Prophet #1"),\
("","Leftdead85"),\
("","THE TEACHER"),\
("","Saphfire"),\
("","Commander Paco"),\
("","Zexial"),\
("","Manuel"),\
("","Rh0D3s"),\
("","BarkingBlade"),\
("","Rainmaker Nova"),\
("","Kurmblog"),\
("","EddieBear"),\
("","0077y"),\
("","TheMetalDoctor"),\
("","Atratus Draco"),\
("","Andrew"),\
("","Devarius Chaos"),\
("","Charles Stephens"),\
("","KBC"),\
("","DerSouper"),\
("","Ya Boii Krunch"),\
("","DRAKO"),\
("","jerseybish"),\
("","iFobz"),\
("","Max Lawerence"),\
("","WarDaddy417"),\
("","See-thru"),\
("","ven"),\
("","Nacho×Fajitas"),\
("","Captain Cookman"),\
("","kellySHOUT"),\
("","TheMiSmith"),\
("","BheadR"),\
("","Marrokev"),\
("","KingTheFlash"),\
("","Wave>U"),\
("","Highway Hitman"),\
("","K0TT0N3Y3J03"),\
("","Daggers"),\
("","ChuckasaurusRex"),\
("","RELLIK6801"),\
("","Raziel"),\
("","Sebbern McLien"),\
("","Yight Lagami"),\
("","TripleNiple333"),\
("","Connor"),\
("","Joe T"),\
("","Elliot Holm"),\
("","Kristian Rasmussen"),\
("","AutisticByDefault"),\
("","Eden"),\
("","Stevo Starkis"),\
("","Travis Moloney"),\
("","Cap'n Jojo"),\
("","David M"),\
("","CullenxBohannon"),\
("","Jimsave"),\
("","Prometheus"),\
("","Myrmex09"),\
("","SomeWhiteGuy"),\
("","Grimhyw"),\
("","Opetox"),\
("","Acidsphere"),\
("","EpicQuentin"),\
("","Bryan the Ronin"),\
("","YarbleDarb"),\
("","MatthewAMEL"),\
("","Famas"),\
("","Outcalled"),\
("","Deooirian"),\
("","Mararonz"),\
("","Jonathan Hang"),\
("","TheFeedingNoob"),\
("","Meloo"),\
("","Sir Rocket"),\
("","TubbyNumNums"),\
("","Ctexman"),\
("","Kingslayer"),\
("","Sokemboppers"),\
("","SkrrtKobain"),\
("","Koipao"),\
("","Adrian Ferreira Jr"),\
("","Amuxic"),\
("","Jalo Maila"),\
("","Nensha"),\
("","Stryker67"),\
("","Dango Knight"),\
("","WorkGalaxy"),\
("","Ty Whaley"),\
("","FelixJFry"),\
("","Linwe"),\
("","BeachDog2600 & YerGurlMerle"),\
("","GiovanniE"),\
("","EuphoricOverflux"),\
("","DiabloKaiser"),\
("","Kallibur"),\
("","Alexir"),\
("","Sir8L4CK"),\
("","DaChonk"),\
("","RJay2014"),\
("","RunicDog"),\
("","Dudedafool"),\
("","tommyjellybeans"),\
("","Necronomenah"),\
("","Freddy Garcia"),\
("","LunaMoth171"),\
("","clityeastwood"),\
("","GarboDan"),\
("","KingJulien"),\
("","EmeraldArcher94"),\
("","ScubaJ"),\
("","Squirrel Chief"),\
("","Asklepios89"),\
("","Treydas"),\
("","LG144"),\
("","Mooner"),\
("","3rdson"),\
("","NoFear2243"),\
("","Siri.Mana"),\
("","rellik6801"),\
("","lawngnomes13"),\
("","Ateo"),\
("","DMaple"),\
("","Cozy Mitts"),\
("","Medic2954 | MeDIK"),\
("","Grancruise"),\
("","Marcus East"),\
("","El_Zebinho"),\
("","Colt Lane"),\
("","Nyx"),\
("","Kanne Bankai"),\
("","Just Dale"),\
("","NeverEnoughHats"),\
("","Darkby"),\
("","ChickWitaDik"),\
("","Tig10101"),\
("","Dr Stefen Lowbert"),\
("","E-Gag"),\
("","Joker's Respite"),\
("","Mortie 10"),\
("","Soursteezel"),\
("","John Munson"),\
("","CR-LMAO"),\
("","NukeQC"),\
("","Just Jared"),\
("","Kane Russell"),\
("","DrRick"),\
("","Kodan"),\
("","Lifeboatboy"),\
("","heOy"),\
("","Anthony_Bayless"),\
("","Yurinim"),\
("","DimitrisAssassin"),\
("","Future_Tactic"),\
("","Rkoon"),\
("","AnimalBop"),\
("","Hondo"),\
("","J ICE"),\
("","Noah Vane"),\
("","Archaeus"),\
("","Canada_Dry"),\
("","Erikachan"),\
("","KaylonGrace"),\
("","Vanilla Legend"),\
("","Zolomak"),\
("","ShoOty"),\
("","Wide Weinered Westerner"),\
("","Ace_Decius"),\
("","Perth Next"),\
("","Joseph Zakutny"),\
("","FERKILL"),\
("","James Attwood"),\
("","Dylbo"),\
("","Myllypuron Mestari"),\
("","Tom Cruise Missile"),\
("","Dragonlord Tevin"),\
("","Lord_K"),\
("","Terralion"),\
("","Daniel Matten"),\
("","HUIT21POCHTLI"),\
("","ViciousDragon7"),\
("","IamHere19"),\
("","Alex6545111"),\
("","Usia"),\
("","Killdead"),\
("","Araxis"),\
("","Emperor of Catkind"),\
("","Gatzou The Beast"),\
("","Razpy the Baddy"),\
("","Micha B"),\
("","Jason M"),\
("","BrandonB123"),\
("","Lentro"),\
("","Rishku"),\
("","YoItsGiooo"),\
("","cerealkiiller"),\
("","WhirlwindKanyo"),\
("","Kaleb Erik Potvin"),\
("","godofmoose"),\
("","Str. Vlar."),\
("","ChilcotinBlaise"),\
("","Richard Daniels"),\
("","Pricefielt"),\
("","Gabriel Abas"),\
("","JacksonianMcKee"),\
("","CATALYS7"),\
("","hallow.iv"),\
("","Quimbly"),\
("","BaneBlackGuard"),\
("","RagnarLT"),\
("","Eliteange1"),\
("","Tavor"),\
("","RAW2408"),\
("","TheRiblin"),\
("","A10forthewin"),\
("","ReelLaguna25"),\
("","ROBERT WATKINS"),\
("","Joseph West"),\
("","JoJ2k / Cam P"),\
("","AmazingLife"),\
("","TheSkyLife"),\
("","Zclif"),\
("","Jaymeen"),\
("","Confuzoled"),\
("","JIBAR"),\
("","Trevor Loots"),\
("","Thistlewick"),\
("","Kenaxion"),\
("","DickMaas"),\
("","Kiddnyght"),\
("","King Tez"),\
("","Yankee19#"),\
("","boonanasplit"),\
("","Pancakes"),\
("","Vvamp"),\
("","Matt Meeker"),\
("","Jaydentaj1"),\
("","Papimomo"),\
("","MadLamb"),\
("","GhastlyMagician"),\
("","Shay1337"),\
("","Malathus"),\
("","Smokespy"),\
("","SebJeff"),\
("","tonyv1324"),\
("","ShogunD"),\
("","Giomar S."),\
("","Joseph Mancheli"),\
("","ODINSON"),\
("","ViTYAN"),\
("","TRGEO"),\
("","VENI"),\
("","Sebastian Lien"),\
("","grouchy"),\
("","Yolonero"),\
("","Snake Plissken"),\
("","Ji Woo Lee"),\
("","Blitzkrieging"),\
("","Senpaireaperz"),\
("","scbigmac07"),\
("","Brasko"),\
("","Ijiero"),\
("","Kashini"),\
("","ahri_xo"),\
("","KingHawk"),\
("","Yvan Dupot"),\
("","Slived Cupwinner"),\
("","DrH"),\
("","Buggarebob74"),\
("","WR. Romano"),\
("","Gẙrø zēppelî"),\
("","Alan J"),\
("","IcePickLobotomy"),\
("","Arsheron"),\
("","Donte Calhoun"),\
("","DIK Jizones"),\
("","marka__"),\
("","Chad6o"),\
("","Tetrimus"),\
("","Matthew Just"),\
("","Raul Mihai Musat"),\
("","Dillion Washington"),\
("","JJlar99"),\
("","Opily"),\
("","Robby G"),\
("","Barbandor!"),\
("","Ogreslayer"),\
("","Revan"),\
("","CheggtheBox12"),\
("","Master Chief"),\
("","Baron Bart"),\
("","Tain"),\
("","Praledon"),\
("","jack_hole21"),\
("","Delta_Ollie"),\
("","BigEd11766"),\
("","tylercool45"),\
("","jacksonianmckee"),\
("","XxJarheadxX"),\
("","Snubba&Menace"),\
("","Jayskiii"),\
("","Snips51"),\
("","Jediassassin115"),\
("","Discord_The_Movie"),\
("","tripx32"),\
("","RightKnee"),\
("","Fuzbo Nuggins"),\
("","TutungZO"),\
("","OzzGoblinn"),\
("","Jmaldopr12"),\
("","Dpsmith67"),\
("","Maverick"),\
("","Cesium Salami"),\
("","sledgetek"),\
("","SaiyanPhantom"),\
("","Rareapollo3808"),\
("","Proud Heretic"),\
("","Corbin"),\
("","DocHolliday"),\
("","heaveriy"),\
("","Skah Waya"),\
("","Bruupo"),\
("","ProjectMelon"),\
("","NaparcaPlouata"),\
("","thelingletingle"),\
("","Filip Cehlárik"),\
("","Demis Bandini"),\
("","AntHun"),\
("","VibingFoxSpirit"),\
("","Foster"),\
("","OlorinShadow"),\
("","Jonas Trummer"),\
("","Stoic"),\
("","Travis Klopfenstine"),\
("","BiznisWalrus"),\
("","SHASAANG"),\
("","Dre as"),\
("","Sheffer"),\
("","OtakuWolf Matt"),\
("","Langelito"),\
("","Hotwheelsofdoom"),\
("","Dustin Owen"),\
("","Erik Rex"),\
("","Benji"),\
("","ImN0tDon"),\
("","Jack Mehoff"),\
("","Grouchy"),\
("","Legi"),\
("","JohnnyDash"),\
("","Maango"),\
("","Tayoxrbl"),\
("","Legion2A93"),\
("","Kokonek"),\
("","ShoeyJaw"),\
("","DocProfMahogany"),\
("","Agent Perry"),\
("","WayneWhen"),\
("","Dr Ty"),\
("","AliRoses"),\
("","Puko"),\
("","Fall4Cake<3"),\
("","X-m11"),\
("","David Somerville"),\
("","Alpha_Alenko"),\
("","batyoxide"),\
("","BombJackSmoe"),\
("","Horny Thorny"),\
("","Flavio Paganini"),\
("","HeavyHungHorse"),\
("","Yangxiaolong"),\
("","BobyOfficial"),\
("","Popaulinho"),\
("","SilentSam"),\
("","Cgibbonsbk1976"),\
("","Nate Black"),\
("","Shtemby"),\
("","Phionex"),\
("","Terryisbarry"),\
("","Kannis"),\
("","Ryan-Patrick Lavarias"),\
("","Lindsey V"),\
("","Chris Rainger"),\
("","Brett Carter"),\
("","Mr. Dimgray"),\
("","Medoroa"),\
("","Duff Matterhorn"),\
("","ZaR"),\
("","Cortarsos"),\
("","commanderlex27"),\
("","Piruliento"),\
("","T. Hes"),\
("","Evowatch"),\
("","Riona's Lover Motisba"),\
("","\\Dorian Gray\\"),\
("","Silverone"),\
("","Dpassion"),\
("","Reyla Ray"),\
("","Black58a"),\
("","Axel"),\
("","DamonBekmos"),\
("","Th3Crak"),\
("","Ryuga"),\
("","Thor von Fiddle"),\
("","Sady"),\
("","Raddenleggaz"),\
("","Mijo"),\
("","Craggin"),\
("","McKenzie"),\
("","Achilles8210"),\
("","L E W Y"),\
("","Thatnewcarsmell"),\
("","SemiTerminaal"),\
("","WindPlays"),\
("","Franklin Harris"),\
("","Marr"),\
("","Louis-Gabriel (EdgeOfMemory)"),\
("","Timmy"),\
("","Kolby Jack Cheese"),\
("","Sage's Boyfriend Jake"),\
("","Senjka"),\
("","Rust"),\
("","Colton82"),\
("","Calebthewanderer"),\
("","Basstie"),\
("","Deeznuts"),\
("","Pretzeal"),\
("","Zombino"),\
("","CinderHearted"),\
("","M3ch87"),\
("","gdakar"),\
("","Jozondi"),\
("","CaptainKurtJac"),\
("","Snowman"),\
("","Ano Veloz"),\
("","BlueBadger141"),\
("","Dashthebash"),\
("","ThatOtherGuyAdam"),\
("","manichewan"),\
("","Buller"),\
("","Segs"),\
("","James Hart"),\
("","MLott512"),\
("","Siri.mana"),\
("","ron77"),\
("","4nubis"),\
("","Willhema"),\
("","Nacho Fajitas"),\
("","Th0mm0"),\
("","M00NERO5"),\
("","Superslyngel"),\
("","Aleksis Kivi"),\
("","IAMSOMOODY"),\
("","Mingorian"),\
("","StarRipper007"),\
("","LilyLove"),\
("","ChillBaron"),\
("","Eric m"),\
("","Da Chonk"),\
("","Reaper"),\
("","Captain Hardkock"),\
("","Nomad"),\
("","MCmowbz"),\
("","TheDeckerdude"),\
("","Notsud"),\
("","Gakoknight"),\
("","Merkury"),\
("","ChaoticCause"),\
("","CjV"),\
("","Subby"),\
("","Felixp2777"),\
("","DrFive70"),\
("","XerotheWolf"),\
("","tokenbg1009"),\
("","McRick"),\
("","Yepod"),\
("","Exile"),\
("","Gioji"),\
("","Jeffox"),\
("","Grob Az"),\
("","KAIROPRACTOR"),\
("","Faco3107"),\
("","Ramrod"),\
("","Chezmoi & Cursor"),\
("","MikeRolo1"),\
("","Adiuro"),\
("","Wicuria"),\
("","ASexyPancake"),\
("","Eyeballs47"),\
("","Gambit Zone"),\
("","Joseph Micheli"),\
("","Denzel Ballestar"),\
("","Marco Yu"),\
("","P4P-K"),\
("","DG"),\
("","Neopherus"),\
("","Ghengiz"),\
("","Hades XD"),\
("","TheLostRito"),\
("","Jimminator70"),\
("","CitricRug"),\
("","Sym | Tek Knight"),\
("","Juls1981"),\
("","CallMeSpikey"),\
("","SamSam"),\
("","R & H"),\
("","iCrusade"),\
("","Chiabobblehead"),\
("","Paul Conte"),\
("","vaxice"),\
("","TA5KMA5T3R"),\
("","Crawlmeister"),\
("","SquirrelChief"),\
("","Gendrix"),\
("","Tobito Sephiroth"),\
("","Yuugon"),\
("","Feelharmony"),\
("","Turkey Bacon Sausage"),\
("","SilentHornet"),\
("","Wylie"),\
("","flex"),\
("","BergarN"),\
("","Tim Organo"),\
("","Microwavable"),\
("","Carlas Kravelin"),\
("","Satavious"),\
("","Lintumfudgey"),\
("","Zaraskill"),\
("","Voidseeker"),\
("","Panzerdk"),\
("","OneEyedBenson"),\
("","Outlawz"),\
("","moy56"),\
("","Antonio Tallo"),\
("","N1gHtB3aSt"),\
("","MackTheKnife"),\
("","FrenchToa$t"),\
("","Marka"),\
("","JBS"),\
("","DIK Gulp&Racoon"),\
("","BadOmen"),\
("","RussTheBus"),\
("","Wildfirewulf"),\
("","DirtyDawg3D"),\
("","Reverend Big Nips"),\
("","KingBWIII"),\
("","Adriano Siqueira"),\
("","EmpathicLotus"),\
("","MINSOO JEON"),\
("","Rafael Casarín"),\
("","DPassion"),\
("","Rok Jeselnik (RJ)"),\
("","oftheunusual"),\
("","Eyesach M!"),\
("","JackLoveJilly"),\
("","JohnLOL"),\
("","Azotemi"),\
("","TeddyBob"),\
("","ZnGAlex"),\
("","Azuz"),\
("","Saska"),\
("","Turkey Bacon"),\
("","Slimjiim"),\
("","The Gaspless"),\
("","fandref"),\
("","Niwkou"),\
("","BlackStormGhost"),\
("","Androshark"),\
("","Alex Ferrie"),\
("","Galer"),\
("","injineer"),\
("","Kaunatar"),\
("","Young_Wolf_99"),\
("","AMH"),\
("","Unholyzelos"),\
("","SuperCraig"),\
("","Superocco"),\
("","SwayEvenly"),\
("","InstaCoffee"),\
("","hewpe"),\
("","Pearce"),\
("","JustSavySnipes"),\
("","KFZ"),\
("","Neppyfish"),\
("","shortaru"),\
("","RawrHatesYou"),\
("","Mike Oxlong"),\
("","Corvin"),\
("","Firefreezer34"),\
("","Killa161"),\
("","TheMaster5025"),\
("","SLADE"),\
("","Jericho"),\
("","4h Productions"),\
("","CamShaft"),\
("","VampWhispers"),\
("","Zephyrus87"),\
("","CheeseGuy"),\
("","Shambo3693"),\
("","RicardoS"),\
("","Bougester"),\
("","will.i.am.not"),\
("","Range11a"),\
("","SludgeMan"),\
("","ANDJAMYOGI"),\
("","Alven"),\
("","Sebastian F. Lien"),\
("","Craigbk1976"),\
("","Collapse replies"),\
("","Cable"),\
("","Sethman409"),\
("","fallenguru"),\
("","Stift80"),\
("","NatsuSixx"),\
("","SgtSagara21"),\
("","Graivin"),\
("","HornyThorny"),\
("","Muumin-H"),\
("","Boxy"),\
("","DGTSM"),\
("","Aubrey Burmaster"),\
("","Kelimdar"),\
("","Bob -Dips Student"),\
("","Tristan 'Timothy' Taylor"),\
("","Lyria Astralius"),\
("","Jae | eptru"),\
("","Rowan"),\
("","SanoSora"),\
("","Noishpa"),\
("","Thadonut"),\
("","Dbright79"),\
("","Gantzbiker"),\
("","GodOfStengthX~(MrDracoX)"),\
("","PatrickXD"),\
("","Ava Thunderheart"),\
("","Bullit"),\
("","Xaphion"),\
("","Rusty - The Throuple Doomsayer"),\
("","BY"),\
("","Scaphandrier5793"),\
("","Foster1nz"),\
("","BuckWilicker"),\
("","Soraiiro"),\
("","Brask9"),\
("","4iGamer"),\
("","Valhalla"),\
("","mAdCapper"),\
("","DevilDawg"),\
("","Tevio"),\
("","Paul \"Walker\" Leong"),\
("","Ferny"),\
("","Ant Lonlieano"),\
("","Susubi"),\
("","Dr_Snowcone9620"),\
("","DarkDemonZERO"),\
("","Kevin \"PK\" Krämer"),\
("","Adam Curtis"),\
("","Chasteigner"),\
("","Slaymore"),\
("","LHBH"),\
("","JoeDIK"),\
("","BazelWarv"),\
("","HIGHZL"),\
("","Vertganti"),\
("","Nidhi Srivastava"),\
("","Erdaneq"),\
("","Adler"),\
("","L3aNo"),\
("","Le Mile"),\
("","Ray Sanchize"),\
("","Liam|N7 Lover"),\
("","Fatty Walsh"),\
("","i0Thug"),\
("","Max | NonTruce"),\
("","Manberry1981"),\
("","DrunkenWizardAu"),\
("","The Big Squid"),\
("","Blake Norwood"),\
("","NoxEternis"),\
("","IrishOrion"),\
("","LaggerHrvat"),\
("","MrDracoX"),\
("","SilkFox"),\
("","Nykiwi"),\
("","Mitch Essam"),\
("","ChamporadoPapi"),\
("","MourningStar"),\
("","George Lieman III"),\
("","domoronnoc1"),\
("","AngelousDraven"),\
("","NightGuardian47"),\
("","LuckyLyonHRT"),\
("","CharlesMagnus"),\
("","Joshua Didier"),\
("","HomieSimpson"),\
("","Trip_X32"),\
("","Haruspex1412"),\
("","Jk Yarlim"),\
("","ThéoHoarau"),\
("","RemixedMind"),\
("","Replica EDT"),\
("","nicnizzy"),\
("","Will Folklore D"),\
("","Asher"),\
("","AutumnGold2368"),\
("","Flerrox"),\
("","Switch92"),\
("","Arkafazin"),\
("","Cem Baran Anşin"),\
("","Deidave"),\
("","Maldurch"),\
("","GanoesParan"),\
("","SpectreSprkR"),\
("","Shaquille_oatmeal56"),\
("","Gagerz"),\
("","JP_and_Dolly"),\
("","Artemys Knight"),\
("","Bareclaw"),\
("","Matthew Black"),\
("","Hepha3stus"),\
("","Imperaattori"),\
("","xRingyx"),\
("","Murphy"),\
("","Giodude"),\
("","Rodney"),\
("","Eiríkr Inn Úlfr Óðinnsson"),\
("","Ulf Delta-Kappa-Alpha"),\
("","ThrasherHT"),\
("","Aaman Perrypop"),\
("","TheChaoticCause"),\
("","CrLmao"),\
("","Cartho"),\
("","OD TRILOGY"),\
("","Marvipego"),\
("","Fealumch"),\
("","Vityan"),\
("","Bread"),\
("","Failtasmagoria - Quinn's Broccoli Farmer"),\
("","Sour"),\
("","Kevin Leake"),\
("","Shiro"),\
("","OrpheusTheMF & FORTUNAdelVENTO"),\
("","Nap"),\
("","Kguy117"),\
("","Andolt"),\
("","Broseph K"),\
("","Verdendall"),\
("","Cage Sabian"),\
("","Blake Norwood."),\
("","danielvan29"),\
("","Cheesedbean"),\
("","Yingjie Li"),\
("","MatteoNEV"),\
("","Blackman1000000"),\
("","DudeNamedNico"),\
("","DIK McRick (Sage Lover)"),\
("","Anonymous donors")
    credits_s = "{font=fonts/candara.ttf}"
    c1 = ""
    for c in credits:
        if not c1==c[0]:
            credits_s += "\n{size=%d}{color=#fe9416}" % (40 * persistent.scale_factor) + c[0] + "{/color}{/size}\n"
            credits_s += "{size=%d}" % (40 * persistent.scale_factor) + c[1] + "{/size}\n"
        else:
            credits_s += "{size=%d}" % (40 * persistent.scale_factor) + c[1] + "{/size}\n"
        c1=c[0]
    credits_s += "{/font}"


    credits_ph = "\n{size=%d}{color=#fe9416}{font=fonts/candara.ttf}A special thanks to the Season 3 Massive {/font}{font=fonts/symbolfont.ttf}DIK{/font}{font=fonts/candara.ttf} patrons{/font}{/color}{/size}" % (40 * persistent.scale_factor)
    credits_p1 = ["{font=fonts/candara.ttf}{size=%d}" % (30 * persistent.scale_factor),"{font=fonts/candara.ttf}{size=%d}" % (30 * persistent.scale_factor),"{font=fonts/candara.ttf}{size=%d}" % (30 * persistent.scale_factor),"{font=fonts/candara.ttf}{size=%d}" % (30 * persistent.scale_factor)]
    credits_p2 = ["{font=fonts/candara.ttf}{size=%d}" % (30 * persistent.scale_factor),"{font=fonts/candara.ttf}{size=%d}" % (30 * persistent.scale_factor),"{font=fonts/candara.ttf}{size=%d}" % (30 * persistent.scale_factor),"{font=fonts/candara.ttf}{size=%d}" % (30 * persistent.scale_factor)]
    credits_p3 = ["{font=fonts/candara.ttf}{size=%d}" % (30 * persistent.scale_factor),"{font=fonts/candara.ttf}{size=%d}" % (30 * persistent.scale_factor),"{font=fonts/candara.ttf}{size=%d}" % (30 * persistent.scale_factor),"{font=fonts/candara.ttf}{size=%d}" % (30 * persistent.scale_factor)]
    credits_p4 = ["{font=fonts/candara.ttf}{size=%d}" % (30 * persistent.scale_factor),"{font=fonts/candara.ttf}{size=%d}" % (30 * persistent.scale_factor),"{font=fonts/candara.ttf}{size=%d}" % (30 * persistent.scale_factor),"{font=fonts/candara.ttf}{size=%d}" % (30 * persistent.scale_factor)]
    credits_p5 = ["{font=fonts/candara.ttf}{size=%d}" % (30 * persistent.scale_factor),"{font=fonts/candara.ttf}{size=%d}" % (30 * persistent.scale_factor),"{font=fonts/candara.ttf}{size=%d}" % (30 * persistent.scale_factor),"{font=fonts/candara.ttf}{size=%d}" % (30 * persistent.scale_factor)]
    credits_p6 = ["{font=fonts/candara.ttf}{size=%d}" % (30 * persistent.scale_factor),"{font=fonts/candara.ttf}{size=%d}" % (30 * persistent.scale_factor),"{font=fonts/candara.ttf}{size=%d}" % (30 * persistent.scale_factor),"{font=fonts/candara.ttf}{size=%d}" % (30 * persistent.scale_factor)]
    credits_p7 = ["{font=fonts/candara.ttf}{size=%d}" % (30 * persistent.scale_factor),"{font=fonts/candara.ttf}{size=%d}" % (30 * persistent.scale_factor),"{font=fonts/candara.ttf}{size=%d}" % (30 * persistent.scale_factor),"{font=fonts/candara.ttf}{size=%d}" % (30 * persistent.scale_factor)]
    credits_p8 = ["{font=fonts/candara.ttf}{size=%d}" % (30 * persistent.scale_factor),"{font=fonts/candara.ttf}{size=%d}" % (30 * persistent.scale_factor),"{font=fonts/candara.ttf}{size=%d}" % (30 * persistent.scale_factor),"{font=fonts/candara.ttf}{size=%d}" % (30 * persistent.scale_factor)]
    credits_p9 = ["{font=fonts/candara.ttf}{size=%d}" % (30 * persistent.scale_factor),"{font=fonts/candara.ttf}{size=%d}" % (30 * persistent.scale_factor),"{font=fonts/candara.ttf}{size=%d}" % (30 * persistent.scale_factor),"{font=fonts/candara.ttf}{size=%d}" % (30 * persistent.scale_factor)]
    credits_p10 = ["{font=fonts/candara.ttf}{size=%d}" % (30 * persistent.scale_factor),"{font=fonts/candara.ttf}{size=%d}" % (30 * persistent.scale_factor),"{font=fonts/candara.ttf}{size=%d}" % (30 * persistent.scale_factor),"{font=fonts/candara.ttf}{size=%d}" % (30 * persistent.scale_factor)]
    credits_p11 = ["{font=fonts/candara.ttf}{size=%d}" % (30 * persistent.scale_factor),"{font=fonts/candara.ttf}{size=%d}" % (30 * persistent.scale_factor),"{font=fonts/candara.ttf}{size=%d}" % (30 * persistent.scale_factor),"{font=fonts/candara.ttf}{size=%d}" % (30 * persistent.scale_factor)]
    credits_p12 = ["{font=fonts/candara.ttf}{size=%d}" % (30 * persistent.scale_factor),"{font=fonts/candara.ttf}{size=%d}" % (30 * persistent.scale_factor),"{font=fonts/candara.ttf}{size=%d}" % (30 * persistent.scale_factor),"{font=fonts/candara.ttf}{size=%d}" % (30 * persistent.scale_factor)]
    credits_p13 = ["{font=fonts/candara.ttf}{size=%d}" % (30 * persistent.scale_factor),"{font=fonts/candara.ttf}{size=%d}" % (30 * persistent.scale_factor),"{font=fonts/candara.ttf}{size=%d}" % (30 * persistent.scale_factor),"{font=fonts/candara.ttf}{size=%d}" % (30 * persistent.scale_factor)]
    c1 = ""
    tmpCount = 0
    tmpCount2 = 0
    for c in credits2:
        if tmpCount2 < 26:
            if tmpCount == 0:
                credits_p1[0] += c[1] + "\n"
                tmpCount += 1
            elif tmpCount == 1:
                credits_p1[1] += c[1] + "\n"
                tmpCount += 1
            elif tmpCount == 2:
                credits_p1[2] += c[1] + "\n"
                tmpCount += 1
            else:
                credits_p1[3] += c[1] + "\n"
                tmpCount = 0
                tmpCount2 += 1
        elif tmpCount2 < 53:
            if tmpCount == 0:
                credits_p2[0] += c[1] + "\n"
                tmpCount += 1
            elif tmpCount == 1:
                credits_p2[1] += c[1] + "\n"
                tmpCount += 1
            elif tmpCount == 2:
                credits_p2[2] += c[1] + "\n"
                tmpCount += 1
            else:
                credits_p2[3] += c[1] + "\n"
                tmpCount = 0
                tmpCount2 += 1
        elif tmpCount2 < 80:
            if tmpCount == 0:
                credits_p3[0] += c[1] + "\n"
                tmpCount += 1
            elif tmpCount == 1:
                credits_p3[1] += c[1] + "\n"
                tmpCount += 1
            elif tmpCount == 2:
                credits_p3[2] += c[1] + "\n"
                tmpCount += 1
            else:
                credits_p3[3] += c[1] + "\n"
                tmpCount = 0
                tmpCount2 += 1
        elif tmpCount2 < 107:
            if tmpCount == 0:
                credits_p4[0] += c[1] + "\n"
                tmpCount += 1
            elif tmpCount == 1:
                credits_p4[1] += c[1] + "\n"
                tmpCount += 1
            elif tmpCount == 2:
                credits_p4[2] += c[1] + "\n"
                tmpCount += 1
            else:
                credits_p4[3] += c[1] + "\n"
                tmpCount = 0
                tmpCount2 += 1
        elif tmpCount2 < 134:
            if tmpCount == 0:
                credits_p5[0] += c[1] + "\n"
                tmpCount += 1
            elif tmpCount == 1:
                credits_p5[1] += c[1] + "\n"
                tmpCount += 1
            elif tmpCount == 2:
                credits_p5[2] += c[1] + "\n"
                tmpCount += 1
            else:
                credits_p5[3] += c[1] + "\n"
                tmpCount = 0
                tmpCount2 += 1
        elif tmpCount2 < 161:
            if tmpCount == 0:
                credits_p6[0] += c[1] + "\n"
                tmpCount += 1
            elif tmpCount == 1:
                credits_p6[1] += c[1] + "\n"
                tmpCount += 1
            elif tmpCount == 2:
                credits_p6[2] += c[1] + "\n"
                tmpCount += 1
            else:
                credits_p6[3] += c[1] + "\n"
                tmpCount = 0
                tmpCount2 += 1
        elif tmpCount2 < 188:
            if tmpCount == 0:
                credits_p7[0] += c[1] + "\n"
                tmpCount += 1
            elif tmpCount == 1:
                credits_p7[1] += c[1] + "\n"
                tmpCount += 1
            elif tmpCount == 2:
                credits_p7[2] += c[1] + "\n"
                tmpCount += 1
            else:
                credits_p7[3] += c[1] + "\n"
                tmpCount = 0
                tmpCount2 += 1
        elif tmpCount2 < 215:
            if tmpCount == 0:
                credits_p8[0] += c[1] + "\n"
                tmpCount += 1
            elif tmpCount == 1:
                credits_p8[1] += c[1] + "\n"
                tmpCount += 1
            elif tmpCount == 2:
                credits_p8[2] += c[1] + "\n"
                tmpCount += 1
            else:
                credits_p8[3] += c[1] + "\n"
                tmpCount = 0
                tmpCount2 += 1
        elif tmpCount2 < 242:
            if tmpCount == 0:
                credits_p9[0] += c[1] + "\n"
                tmpCount += 1
            elif tmpCount == 1:
                credits_p9[1] += c[1] + "\n"
                tmpCount += 1
            elif tmpCount == 2:
                credits_p9[2] += c[1] + "\n"
                tmpCount += 1
            else:
                credits_p9[3] += c[1] + "\n"
                tmpCount = 0
                tmpCount2 += 1
        elif tmpCount2 < 269:
            if tmpCount == 0:
                credits_p10[0] += c[1] + "\n"
                tmpCount += 1
            elif tmpCount == 1:
                credits_p10[1] += c[1] + "\n"
                tmpCount += 1
            elif tmpCount == 2:
                credits_p10[2] += c[1] + "\n"
                tmpCount += 1
            else:
                credits_p10[3] += c[1] + "\n"
                tmpCount = 0
                tmpCount2 += 1
        elif tmpCount2 < 296:
            if tmpCount == 0:
                credits_p11[0] += c[1] + "\n"
                tmpCount += 1
            elif tmpCount == 1:
                credits_p11[1] += c[1] + "\n"
                tmpCount += 1
            elif tmpCount == 2:
                credits_p11[2] += c[1] + "\n"
                tmpCount += 1
            else:
                credits_p11[3] += c[1] + "\n"
                tmpCount = 0
                tmpCount2 += 1
        elif tmpCount2 < 323:
            if tmpCount == 0:
                credits_p12[0] += c[1] + "\n"
                tmpCount += 1
            elif tmpCount == 1:
                credits_p12[1] += c[1] + "\n"
                tmpCount += 1
            elif tmpCount == 2:
                credits_p12[2] += c[1] + "\n"
                tmpCount += 1
            else:
                credits_p12[3] += c[1] + "\n"
                tmpCount = 0
                tmpCount2 += 1
        elif tmpCount2 < 350:
            if tmpCount == 0:
                credits_p13[0] += c[1] + "\n"
                tmpCount += 1
            elif tmpCount == 1:
                credits_p13[1] += c[1] + "\n"
                tmpCount += 1
            elif tmpCount == 2:
                credits_p13[2] += c[1] + "\n"
                tmpCount += 1
            else:
                credits_p13[3] += c[1] + "\n"
                tmpCount = 0
                tmpCount2 += 1

    if tmpCount > 2:
        credits_p13[3] += " \n"
    elif tmpCount > 1:
        credits_p13[3] += " \n"
        credits_p13[2] += " \n"
    elif tmpCount > 0:
        credits_p13[3] += " \n"
        credits_p13[2] += " \n"
        credits_p13[1] += " \n"


    credits_p1[0] += "{/size}{/font}"
    credits_p1[1] += "{/size}{/font}"
    credits_p1[2] += "{/size}{/font}"
    credits_p1[3] += "{/size}{/font}"
    credits_p2[0] += "{/size}{/font}"
    credits_p2[1] += "{/size}{/font}"
    credits_p2[2] += "{/size}{/font}"
    credits_p2[3] += "{/size}{/font}"
    credits_p3[0] += "{/size}{/font}"
    credits_p3[1] += "{/size}{/font}"
    credits_p3[2] += "{/size}{/font}"
    credits_p3[3] += "{/size}{/font}"
    credits_p4[0] += "{/size}{/font}"
    credits_p4[1] += "{/size}{/font}"
    credits_p4[2] += "{/size}{/font}"
    credits_p4[3] += "{/size}{/font}"
    credits_p5[0] += "{/size}{/font}"
    credits_p5[1] += "{/size}{/font}"
    credits_p5[2] += "{/size}{/font}"
    credits_p5[3] += "{/size}{/font}"
    credits_p6[0] += "{/size}{/font}"
    credits_p6[1] += "{/size}{/font}"
    credits_p6[2] += "{/size}{/font}"
    credits_p6[3] += "{/size}{/font}"
    credits_p7[0] += "{/size}{/font}"
    credits_p7[1] += "{/size}{/font}"
    credits_p7[2] += "{/size}{/font}"
    credits_p7[3] += "{/size}{/font}"
    credits_p8[0] += "{/size}{/font}"
    credits_p8[1] += "{/size}{/font}"
    credits_p8[2] += "{/size}{/font}"
    credits_p8[3] += "{/size}{/font}"
    credits_p9[0] += "{/size}{/font}"
    credits_p9[1] += "{/size}{/font}"
    credits_p9[2] += "{/size}{/font}"
    credits_p9[3] += "{/size}{/font}"
    credits_p10[0] += "{/size}{/font}"
    credits_p10[1] += "{/size}{/font}"
    credits_p10[2] += "{/size}{/font}"
    credits_p10[3] += "{/size}{/font}"
    credits_p11[0] += "{/size}{/font}"
    credits_p11[1] += "{/size}{/font}"
    credits_p11[2] += "{/size}{/font}"
    credits_p11[3] += "{/size}{/font}"
    credits_p12[0] += "{/size}{/font}"
    credits_p12[1] += "{/size}{/font}"
    credits_p12[2] += "{/size}{/font}"
    credits_p12[3] += "{/size}{/font}"
    credits_p13[0] += "{/size}{/font}"
    credits_p13[1] += "{/size}{/font}"
    credits_p13[2] += "{/size}{/font}"
    credits_p13[3] += "{/size}{/font}"

init:
    image cred = Text(credits_s, text_align=0.5)
    image credits_ph = Text(credits_ph, text_align=0.5)
    image cred_patrons1a = Text(credits_p1[0], text_align=0.5)
    image cred_patrons1b = Text(credits_p1[1], text_align=0.5)
    image cred_patrons1c = Text(credits_p1[2], text_align=0.5)
    image cred_patrons1d = Text(credits_p1[3], text_align=0.5)
    image cred_patrons2a = Text(credits_p2[0], text_align=0.5)
    image cred_patrons2b = Text(credits_p2[1], text_align=0.5)
    image cred_patrons2c = Text(credits_p2[2], text_align=0.5)
    image cred_patrons2d = Text(credits_p2[3], text_align=0.5)
    image cred_patrons3a = Text(credits_p3[0], text_align=0.5)
    image cred_patrons3b = Text(credits_p3[1], text_align=0.5)
    image cred_patrons3c = Text(credits_p3[2], text_align=0.5)
    image cred_patrons3d = Text(credits_p3[3], text_align=0.5)
    image cred_patrons4a = Text(credits_p4[0], text_align=0.5)
    image cred_patrons4b = Text(credits_p4[1], text_align=0.5)
    image cred_patrons4c = Text(credits_p4[2], text_align=0.5)
    image cred_patrons4d = Text(credits_p4[3], text_align=0.5)
    image cred_patrons5a = Text(credits_p5[0], text_align=0.5)
    image cred_patrons5b = Text(credits_p5[1], text_align=0.5)
    image cred_patrons5c = Text(credits_p5[2], text_align=0.5)
    image cred_patrons5d = Text(credits_p5[3], text_align=0.5)
    image cred_patrons6a = Text(credits_p6[0], text_align=0.5)
    image cred_patrons6b = Text(credits_p6[1], text_align=0.5)
    image cred_patrons6c = Text(credits_p6[2], text_align=0.5)
    image cred_patrons6d = Text(credits_p6[3], text_align=0.5)
    image cred_patrons7a = Text(credits_p7[0], text_align=0.5)
    image cred_patrons7b = Text(credits_p7[1], text_align=0.5)
    image cred_patrons7c = Text(credits_p7[2], text_align=0.5)
    image cred_patrons7d = Text(credits_p7[3], text_align=0.5)
    image cred_patrons8a = Text(credits_p8[0], text_align=0.5)
    image cred_patrons8b = Text(credits_p8[1], text_align=0.5)
    image cred_patrons8c = Text(credits_p8[2], text_align=0.5)
    image cred_patrons8d = Text(credits_p8[3], text_align=0.5)
    image cred_patrons9a = Text(credits_p9[0], text_align=0.5)
    image cred_patrons9b = Text(credits_p9[1], text_align=0.5)
    image cred_patrons9c = Text(credits_p9[2], text_align=0.5)
    image cred_patrons9d = Text(credits_p9[3], text_align=0.5)
    image cred_patrons10a = Text(credits_p10[0], text_align=0.5)
    image cred_patrons10b = Text(credits_p10[1], text_align=0.5)
    image cred_patrons10c = Text(credits_p10[2], text_align=0.5)
    image cred_patrons10d = Text(credits_p10[3], text_align=0.5)
    image cred_patrons11a = Text(credits_p11[0], text_align=0.5)
    image cred_patrons11b = Text(credits_p11[1], text_align=0.5)
    image cred_patrons11c = Text(credits_p11[2], text_align=0.5)
    image cred_patrons11d = Text(credits_p11[3], text_align=0.5)
    image cred_patrons12a = Text(credits_p12[0], text_align=0.5)
    image cred_patrons12b = Text(credits_p12[1], text_align=0.5)
    image cred_patrons12c = Text(credits_p12[2], text_align=0.5)
    image cred_patrons12d = Text(credits_p12[3], text_align=0.5)
    image cred_patrons13a = Text(credits_p13[0], text_align=0.5)
    image cred_patrons13b = Text(credits_p13[1], text_align=0.5)
    image cred_patrons13c = Text(credits_p13[2], text_align=0.5)
    image cred_patrons13d = Text(credits_p13[3], text_align=0.5)

    image cred_camila_bg = "credits_camila_bg"
    image cred_cathy_bg = "credits_cathy_bg"
    image cred_derek_bg = "credits_derek_bg"
    image cred_envy_bg = "credits_envy_bg"
    image cred_isabella_bg = "credits_isabella_bg"
    image cred_jade_bg = "credits_jade_bg"
    image cred_jill_bg = "credits_jill_bg"
    image cred_josy_bg = "credits_josy_bg"
    image cred_lily_bg = "credits_lily_bg"
    image cred_maya_bg = "credits_maya_bg"
    image cred_mc_bg = "credits_mc_bg"
    image cred_quinn_bg = "credits_quinn_bg"
    image cred_riona_bg = "credits_riona_bg"
    image cred_sage_bg = "credits_sage_bg"
    image cred_zoey_bg = "credits_zoey_bg"

    image credits_fg:
        "credits_fg1" with Dissolve(0.5, alpha=True)
        pause 1
        "credits_fg2" with Dissolve(0.5, alpha=True)
        pause 1
        repeat
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
