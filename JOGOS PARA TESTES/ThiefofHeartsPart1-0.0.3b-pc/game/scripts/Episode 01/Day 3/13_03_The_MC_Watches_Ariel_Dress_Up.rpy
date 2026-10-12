init:
    $ v_ep01_13_03_Ariels_Room = False
    $ v_ep01_13_03_Bellas_Room = False
    $ v_ep01_13_03_Ariels_Panties = False
    $ v_ep01_13_03_Ariels_Look = ""
    $ v_ep01_13_03_Ariels_Name = ""




    image sc ariel dress up finger:
        "sc arielcosplay a023" with Dissolve(0.2, alpha=True)
        pause 0.4
        "sc arielcosplay a023a" with Dissolve(0.2, alpha=True)
        pause 0.4
        "sc arielcosplay a023b" with Dissolve(0.2, alpha=True)
        pause 0.4
        repeat

    image sc ariel dress up spin:
        "sc arielcosplay a026" with Dissolve(0.2, alpha=True)
        pause 0.8
        "sc arielcosplay a026a" with Dissolve(0.2, alpha=True)
        pause 0.8
        "sc arielcosplay a026b" with Dissolve(0.2, alpha=True)
        pause 0.8
        "sc arielcosplay a026c" with Dissolve(0.2, alpha=True)
        pause 0.8
        "sc arielcosplay a026d" with Dissolve(0.2, alpha=True)
        pause 0.8
        "sc arielcosplay a026" with Dissolve(0.2, alpha=True)

    image sc ariel dress fall:
        "sc arielcosplay a057a" with Dissolve(0.2, alpha=True)
        pause 0.8
        "sc arielcosplay a058" with Dissolve(0.2, alpha=True)
        pause 0.2
        "sc arielcosplay a058" with hpunch

    image sc ariel dress rub1:
        "sc arielcosplay a062" with Dissolve(0.2, alpha=True)
        pause 0.8
        "sc arielcosplay a062a" with Dissolve(0.2, alpha=True)
        pause 0.8
        "sc arielcosplay a062" with Dissolve(0.2, alpha=True)
        pause 0.8
        "sc arielcosplay a062b" with Dissolve(0.2, alpha=True)
        pause 0.8
        repeat

    image sc ariel dress rub2:
        "sc arielcosplay a062" with Dissolve(0.2, alpha=True)
        pause 0.4
        "sc arielcosplay a062a" with Dissolve(0.2, alpha=True)
        pause 0.4
        "sc arielcosplay a062" with Dissolve(0.2, alpha=True)
        pause 0.4
        "sc arielcosplay a062b" with Dissolve(0.2, alpha=True)
        pause 0.4
        repeat

    image sc ariel dress rub3:
        "sc arielcosplay a063" with Dissolve(0.2, alpha=True)
        pause 0.8
        "sc arielcosplay a063a" with Dissolve(0.2, alpha=True)
        pause 0.8
        repeat

    image sc ariel dress rub3a:
        "sc arielcosplay a063" with Dissolve(0.2, alpha=True)
        pause 0.4
        "sc arielcosplay a063a" with Dissolve(0.2, alpha=True)
        pause 0.4
        repeat

    image sc ariel dress rub4:
        "sc arielcosplay a064" with Dissolve(0.2, alpha=True)
        pause 0.8
        "sc arielcosplay a064a" with Dissolve(0.2, alpha=True)
        pause 0.8
        repeat

    image sc ariel dress rub5:
        "sc arielcosplay a064" with Dissolve(0.2, alpha=True)
        pause 0.4
        "sc arielcosplay a064a" with Dissolve(0.2, alpha=True)
        pause 0.4
        repeat

    image sc ariel dress breast fondle1:
        "sc arielcosplay a065" with Dissolve(0.2, alpha=True)
        pause 0.4
        "sc arielcosplay a065a" with Dissolve(0.2, alpha=True)
        pause 0.4
        repeat

    image sc ariel dress rub6:
        "sc arielcosplay a066" with Dissolve(0.2, alpha=True)
        pause 0.4
        "sc arielcosplay a066a" with Dissolve(0.2, alpha=True)
        pause 0.4
        repeat

    image sc ariel dress rub7:
        "sc arielcosplay a067" with Dissolve(0.2, alpha=True)
        pause 0.4
        "sc arielcosplay a067a" with Dissolve(0.2, alpha=True)
        pause 0.4
        repeat

    image sc ariel dress rub8:
        "sc arielcosplay a068" with Dissolve(0.2, alpha=True)
        pause 0.4
        "sc arielcosplay a068a" with Dissolve(0.2, alpha=True)
        pause 0.4
        repeat

    image sc ariel dress rub9:
        "sc arielcosplay a067" with Dissolve(0.2, alpha=True)
        pause 0.4
        "sc arielcosplay a067a" with Dissolve(0.2, alpha=True)
        pause 0.4
        repeat

    image sc ariel dress rub10:
        "sc arielcosplay a069" with Dissolve(0.2, alpha=True)
        pause 0.4
        "sc arielcosplay a069a" with Dissolve(0.2, alpha=True)
        pause 0.4
        repeat

label lb_ep01_13_03_MC_Evening_Visit1:
    #the MC returns home after dark and enters the house
    #It's quiet - the player gets given three options.
    #the doors are closed but there's a light coming from inside Bella and Ariel's bedrooms (under their doors), whereas it's dark under Vivian's room
    scene sc girlsrooms g22
    with dissolve
    mc"(It's good to be home, and with fifteen minutes to spare.)"
    mc"(Hmm... The lights are on in [b_name] and [a_name]'s rooms.)"
    #On the screen, show the bedroom doors - Ariel, Bella, the MC and the main bedroom
    #The main bedroom (Vivian and Victor's can't be chosen)

    #The other three room doors can be clicked on
    show sc bellayoga y092
    mc"(I wonder if they would be up for a chat?)"

label lb_ep01_13_03_MC_Evening_Visit2:
    if v_ep01_13_03_Ariels_Room == False and v_ep01_13_03_Bellas_Room == False:
        show sc girlsrooms g22
    else:
        show sc girlsrooms g22
        with dissolve
    #[ [a_name]'s door / [b_name]'s door / Go to bed]
    menu:
        "[a_name]'s door" if v_ep01_13_03_Ariels_Room == False:
            $ v_ep01_13_03_Ariels_Room = True
            jump lb_ep01_13_03_Ariel_dress_up

        "[b_name]'s door" if v_ep01_13_03_Bellas_Room == False:
            $ v_ep01_13_03_Bellas_Room = True
            jump lb_ep01_13_03_Bella_evening_yoga

        "Go to bed"(wt="Choose this last"):
            #The MC stands in the hallway
            show sc bellayoga y092
            mc"(There's no point staying up an longer.)"
            mc"(Besides, I'm completely exhausted after today.)"
            mc"(Time to call it a night...)"
            #screen goes blank
            scene black
            with dissolve
            scene black
            with Pause (2)
            jump lb_ep01_The_MC_goes_to_the_art_gallery

label lb_ep01_13_03_Ariel_dress_up:
    #The MC knocks on Ariel's door
    play sound "sound effects/01/Door_Knock_Sound_Effect_Free.mp3"
    show sc arielcosplay a001
    with dissolve
    if persistent.v_sounds_text_on == True:
        "(Knock, knock, knock)"
    else:
        pause 1.0
    a"{i}(*Muffled*){/i}\nCome on in."
    #The MC enters her room. Ariel is in her bathroom
    stop sound fadeout 1.0
    play sound2 "sound effects/01/door_close_soft.mp3"
    show sc arielcosplay a002
    mc"Where are you, [a_name]?"
    show sc arielcosplay a003
    a"{i}(*Muffled*){/i}\nI'll be with you in a second!"
    stop sound2 fadeout 1.0
    show sc arielcosplay a004
    mc"(She let me in here tonight this time.)"
    show sc arielcosplay a005
    mc"(I wonder why.)"
    show sc arielcosplay a006
    a"So, what do you think?"
    #Ariel comes out wearing a superhero costume with glasses on - https://www.daz3d.com/marvelous-bodysuit-female-super-hero-textures
    play music "sound effects/01/Cosplay Dreams.mp3" loop fadein 1.0
    mc"..."
    #ROLLING SCREEN OF ARIEL IN THE OUTFIT
    #She looks shy
    if not persistent.v_sex_anim_enabled_locked and persistent.v_sex_anim_enabled:
        scene wip_ep01_ariel_cosplay_01 at tt_top
        pause
    elif True:
        show sc arielcosplay a007
    mc"Wow!"
    mc"What's all this for?"
    scene sc arielcosplay a008
    a"I um... It's for Nerdapalooza!"
    show sc arielcosplay a009
    mc"What on earth is Nerdapalooza!"
    show sc arielcosplay a010
    a"It's like a convention for superhero, villain, anime and comic characters."
    a"It's going to be in town next week."
    a"They're inviting people to come as their own character."
    show sc arielcosplay a013
    mc"Wait, you made this outfit?"
    show sc arielcosplay a012
    a"Yeah, just a bit at a time for the past three months."
    a"I loosely based it off of one of my favourite anime characters."
    a"Do you like it?"
    show sc arielcosplay a014
    menu:
        #[It's great / It suits you / You look hot ]
        "It's great":
            mc"I have to say, you look pretty great in it."
            mc"You'll definitely turn heads if you walked down the street in that."
            mc"I'd certainly take a second look."
            $ v_ep01_ariel_cocky_counter += 1
            show sc arielcosplay a015
            a"Thanks."
            $ v_ep01_13_03_Ariels_Look = "great"
        "It suits you"(wt="Best option"):
            mc"I have to say, it really suits you."
            mc"You've definitely pulled off the super nerd look!"
            $ v_ep01_ariel_respect_counter += 1
            show sc arielcosplay a016
            with dissolve
            a"Thanks, that's exactly what I was aiming for."
            $ v_ep01_13_03_Ariels_Look = "suits"
            #ONE BONUS RENDER OF ARIEL (IN HER OUTFIT) ADDED TO THE PHOTO GALLERY FOR HER PROFILE
        "You look hot":
            mc"I have to say, you look incredibly hot."
            show sc arielcosplay a017
            b"Oh, thanks... But I was kind of going for the more nerdy look."
            $ v_ep01_ariel_arrogant_counter += 1
            show sc arielcosplay a018
            mc"Oh, okay."
            $ v_ep01_13_03_Ariels_Look = "hot"
    #scene continues
    show screen scr_secret_icon("v_secrets_ep01_13_03_1") onlayer ontop
    with { "ontop": dissolve}
    show sc arielcosplay a013
    mc"So, have you come up with a name?"
    show sc arielcosplay a019
    a"A name?"
    show sc arielcosplay a020
    mc"Yeah, a name for your character?"
    show sc arielcosplay a021
    a"Oh... No, I haven't."
    show sc arielcosplay a022
    mc"Well, you gotta have a name."
    mc"Why don't we come up with one together?"
    show sc arielcosplay a019
    a"Um, okay."
    show sc arielcosplay a020
    mc"Let's see here..."
    #The MC looks Ariel up and down
    if persistent.v_anim_enabled:
        show sc ariel dress up finger
    else:
        show sc arielcosplay a023
    mc"Turn around for me."
    show sc arielcosplay a024
    a"Huh? Why?"
    show sc arielcosplay a025
    mc"I need a little more inspiration."
    #Ariel turns around so we see her from the back
    if persistent.v_anim_enabled:
        show sc ariel dress up spin
        mc"Hmm..."
        mc"(Wait, is she not...)"
    else:
        show sc arielcosplay a026a
        mc"Hmm..."
        show sc arielcosplay a026c
        mc"(Wait, is she not...)"
        show sc arielcosplay a026
    #Ariel turns on her side
    #Discussions before that could be the MC asking her "why" this outfit, and then you can put your description above for Ariel's reply (her love of anime, maybe it's influenced by a fave character of hers etc).
    #This has potential to be the sexiest scene featuring Ariel which I think is needed.
    #[Are you not wearing panties? / Don't ask her]
    menu:
        "Are you not wearing panties?"(wt="Best option"):
            show sc arielcosplay a013
            mc"Before I help give you a name, there is something I was wondering."
            show sc arielcosplay a027
            a"Hmm..."
            show sc arielcosplay a011
            mc"It's not like I was trying to look, but, are you not wearing any panties underneath that outfit?"
            show sc arielcosplay a029
            a"Really now? That's what you wanted to ask me?"
            a"Get your mind out of the gutter."
            a"Of course I'm wearing... \"something\" under there."
            a"It's just designed in such a way as to not look like I am."
            show sc arielcosplay a030
            a"There's no way I could go out in public like that, let alone wear it that way around you."
            show sc arielcosplay a031
            mc"I'm sorry to have asked. I couldn't help but be curious."
            mc"I'm a guy, after all."
            show sc arielcosplay a029
            a"Well, stop thinking about that and focus on my character name already."
            $ v_ep01_13_03_Ariels_Panties = True
        "Don't ask her":
            show sc arielcosplay a028
            mc"All right..."
            #She faces him again
            mc"I think I have it."
            show sc arielcosplay a029
            a"Really?"
    show sc arielcosplay a032
    mc"Yeah. How about..."
    menu:
        "Princess":
            mc"Foxy Princess?"
            a"Hmm..."
            mc"Because of the ears, and I also think that it's a decent play on words."
            show sc arielcosplay a033
            a"Yeah, I got that. But I'm in no way \"Foxy\", let alone a princess."
            a"Plus this is based on a wolf character."
            show sc arielcosplay a033a
            mc"I think you're selling yourself short, but okay..."
            show sc arielcosplay a030
            a"What about..."
            a"The Scarlet Wolf?"
            show sc arielcosplay a031
            mc"Hmm..."
            mc"That's pretty damn good."
            show sc arielcosplay a028
            mc"I like it!"
            show sc arielcosplay a029
            a"Yeah, me too."
            $ v_ep01_13_03_Ariels_Name = "princess"
        "Wise":
            mc"The Wise Wolf?"
            a"Hmm..."
            mc"You know, because you're smart and at times you see things before anyone else does."
            show sc arielcosplay a033
            a"True, and that name does fit very well with the series I based this from, but I was hoping for something more unique."
            show sc arielcosplay a033a
            mc"Oh..."
            show sc arielcosplay a030
            a"What about this..."
            a"The Scarlet Wolf?"
            show sc arielcosplay a031
            mc"Hmm..."
            mc"That's pretty damn good."
            show sc arielcosplay a028
            mc"I like it!"
            show sc arielcosplay a029
            a"Yeah, me too."
            $ v_ep01_13_03_Ariels_Name = "wise"
        "Scarlet"(wt="Best option"):
            mc"The Scarlet Wolf?"
            a"Hmm..."
            show sc arielcosplay a029
            a"That's pretty darn good."
            $ rewards_unlock ("ariel",5)
            a"Did you just come up with that on the spot?"
            show sc arielcosplay a028
            mc"Sure did."
            show sc arielcosplay a029
            a"I like it. It's a very strong name and fits well with the theme I wanted."
            $ v_ep01_13_03_Ariels_Name = "scarlet"
            #ONE BONUS RENDER OF ARIEL (IN HER OUTFIT) ADDED TO THE PHOTO GALLERY FOR HER PROFILE
    #scene continues
    stop music fadeout 2.0
    play music "sound effects/01/Dressed in Dreams.mp3" loop fadein 1.0
    show sc arielcosplay a028
    mc"I have to ask, why did you want me to see you like this?"
    show sc arielcosplay a030
    a"I needed a second opinion."
    a"And because I feel like you're the only person I can trust."
    show sc arielcosplay a034
    a"If I showed my costume to [b_name], she would probably laugh at me."
    a"[mc_v_address!c] never seems to have the time, and [mc_vic_address], well, do I really need to explain?"
    show sc arielcosplay a035
    mc"Yeah, fair point."
    show sc arielcosplay a036
    mc"Well, I'm honoured to be asked."
    show sc arielcosplay a037
    show screen scr_secret_hotspot ("sc arielcosplay a037","1630, 585, 150, 110","v_secrets_ep01_13_03_1")
    a"I need another favour from you."
    hide screen scr_secret_hotspot
    show sc arielcosplay a037a
    mc"Name it."
    show sc arielcosplay a038
    a"As I said, I want to go to this event next week, but I don't want to go alone."
    show sc arielcosplay a039
    a"Would you maybe want to come with me?"
    show sc arielcosplay a041
    mc"To Nerdpalooza?"
    show sc arielcosplay a040
    mc"Hmm..."
    #Ariel looks hopeful
    mc"It's not really my thing, but..."
    mc"Sure, why the hell not?"
    show sc arielcosplay a042
    a"Really?"
    show sc arielcosplay a043
    mc"Yeah, you only live once, right?"
    show sc arielcosplay a044
    a"Awesome!"
    show sc arielcosplay a042
    a"But we'll have to get you a costume!"
    show sc arielcosplay a043
    mc"Excuse me?"
    show sc arielcosplay a045
    a"In order to be admitted, you have to wear an original costume like this."
    show sc arielcosplay a046
    mc"Oh..."
    show sc arielcosplay a047
    mc"(I never thought about that.)"
    mc"(I just hope she's not expecting me to wear my underpants on the outside of my outfit or anything like that.)"
    show sc arielcosplay a048
    a"I also have an online friend who said that they are going."
    show sc arielcosplay a042
    a"This is going to be so much fun!"
    show sc arielcosplay a041
    mc"Yeah, but let's keep the excitement down for the next few days so no one else has any idea that we're going to this."
    show sc arielcosplay a049
    a"Sure thing. I can do that."
    hide screen scr_secret_icon onlayer ontop
    with { "ontop": dissolve}
    show sc arielcosplay a050
    mc"Anyway, I'll leave you to it as I'll be going to bed shortly."
    #Ariel hugs the MC
    show sc arielcosplay a051
    with hpunch
    a"Thank you so much for agreeing to go."
    show sc arielcosplay a052
    a"I knew I could count on you."
    #Show their bodies pressed together."
    show sc arielcosplay a053
    mc"You're welcome."
    #Ariel smiles
    show sc arielcosplay a054
    mc"Goodnight, {i}Mini Marvel{/i}."
    #Ariel smiles
    show sc arielcosplay a055
    a"Right back atcha, {i}Comedy Crusader...{/i}"
    #screen goes blank
    if persistent.v_secrets_enabled and persistent.v_secrets_ep01_13_03_1:
        label lb_ep01_13_03_Ariel_Room_1_fantasy_scene:
            stop music fadeout 1.0
            scene black
            with dissolve
            scene black
            with Pause (2)
            # Scene opens up with ariel sitting on her bed after the MC has left.
            if not _in_replay:
                scene img_secret_scene_overlay onlayer anim_layer
                with { "anim_layer": dissolve}
            else:
                show screen scr_end_replay
            centered "Ten minutes later...{w=2.0}{nw}" with dissolve
            show text "Ten minutes later..." #THESE LINES ARE NOT DUPLICATES. Needed to fade the text in and out!
            scene bg black with Dissolve(1)
            pause 1.0
            play music "sound effects/01/Whispering Heart.mp3" loop fadein 1.0
            scene sc arielcosplay a056
            with dissolve
            a"(Whew, so glad to be out of that robe. It gets real heavy after a while.)"
            show sc arielcosplay a057
            a"(But I'm so excited! I can actually go to Nerdapalooza!)"
            show sc ariel dress fall
            a"(It's going to be so much fun!)"
            # She falls back onto the bed
            a"(I'm so glad that [y_name] agreed to go with me.)"
            show sc arielcosplay a059
            a"(I don't think I would of had the courage to go by myself, especially in this outfit.)"
            a"([y_name] is the only person I'd want with me if I were to go out in public. And he did say I look really good in my costume.)"
            if v_ep01_13_03_Ariels_Panties:
                # We see her reach down to her crotch
                show sc arielcosplay a060
                a"(I just hope that he believed my answer about my underwear.)"
                # Cuts to a shot of her hand covering her pussy
                show sc arielcosplay a061
                a"(It would have been so embarrassing if he'd realized that I wasn't wearing any.)"
            else:
                # We see her reach down to her crotch
                show sc arielcosplay a060
                a"(I'm just glad he didn't notice that I wasn't wearing any panties.)"
                # Cuts to a shot of her hand covering her pussy
                show sc arielcosplay a061
                a"(It would have been so embarrassing had he realized it.)"
            # Cuts back to her upper body, the outfit slipping off so only the bra is showing
            show sc arielcosplay a060
            a"(I have to admit though, it was pretty exciting being so close to another guy with nothing but my birthday suit on down here.)"
            # Her hand starts to move around on her pussy
            play sex1 "sound effects/01/sex/ariel_moan_loop1.ogg" loop fadein 1.0
            if not persistent.v_sex_anim_enabled_locked and persistent.v_sex_anim_enabled:
                show sc ariel dress rub1
            else:
                show sc arielcosplay a062
            a"(In fact, it was a big turn on.)"
            if not persistent.v_sex_anim_enabled_locked and persistent.v_sex_anim_enabled:
                show sc ariel dress rub3
            else:
                show sc arielcosplay a063
            a"(Just one slip of the cloth and he could have seen my soft, pink, teen vagina. Mmm... )"
            if not persistent.v_sex_anim_enabled_locked and persistent.v_sex_anim_enabled:
                show sc ariel dress rub2
            else:
                show sc arielcosplay a062
            a"(Then, all I would have to do is spread my legs and invite my [mc_a_rel] in.)"
            if not persistent.v_sex_anim_enabled_locked and persistent.v_sex_anim_enabled:
                show sc ariel dress rub3a
            else:
                show sc arielcosplay a063
            a"(Unable to resist the urge, he drives his face in...)"
            # She sticks a finger in, her hand still hiding everything
            if not persistent.v_sex_anim_enabled_locked and persistent.v_sex_anim_enabled:
                show sc ariel dress rub4
            else:
                show sc arielcosplay a064
            a"(Sticking his tongue deep inside as he rubs my clit with his big, strong hands...)"
            a"Uhhh."
            # Her hand reaches under her bra
            if not persistent.v_sex_anim_enabled_locked and persistent.v_sex_anim_enabled:
                show sc ariel dress breast fondle1
            else:
                show sc arielcosplay a065
            a"(His other hand grabbing my tits as he furiously sucks and licks my pussy...)"
            a"(Exploring the lips with his tongue, tracing every nook and cranny they offer...)"
            if not persistent.v_sex_anim_enabled_locked and persistent.v_sex_anim_enabled:
                show sc ariel dress rub5
            else:
                show sc arielcosplay a064
            a"(NGHH... Licking up all of the juices I release as he vigorously rubs my g-spot...)"
            a"Oh fuck yes [y_name], shove your fingers into my tight pussy!"
            a"(The next thing I know, he's removing his pants to reveal his rock hard member.)"
            if not persistent.v_sex_anim_enabled_locked and persistent.v_sex_anim_enabled:
                show sc ariel dress breast fondle1
            else:
                show sc arielcosplay a065
            a"Make your [a_mc_rel] crave your big cock!"
            stop sound fadeout 1.0
            stop music fadeout 1.0
            scene black
            with dissolve
            if not persistent.v_sex_anim_enabled_locked and persistent.v_sex_anim_enabled:
                show sc ariel dress rub6
                with dissolve
            else:
                show sc arielcosplay a066
                with dissolve
            play music "sound effects/01/Whispering Heart1.mp3" loop fadein 1.0
            play sex2 "sound effects/01/sex/ariel_moan_loop2.ogg" loop fadein 1.0
            a"(He grabs my ass and readies his dick to reach the inner depths of my tight virgin hole.)"
            a"(And with one big thrust, he makes a woman out of me...)"
            if not persistent.v_sex_anim_enabled_locked and persistent.v_sex_anim_enabled:
                show sc ariel dress rub8
            else:
                show sc arielcosplay a068
            a"Oh fuck yes!"
            a"(He repeatedly rams his cock deep inside of me!)"
            if not persistent.v_sex_anim_enabled_locked and persistent.v_sex_anim_enabled:
                show sc ariel dress rub7
            else:
                show sc arielcosplay a067
            a"(Over and over again. His throbbing manhood making my legs tremble with each thrust!)"
            a"Oh god!"
            stop sex2 fadeout 1.0
            play sex1 "sound effects/01/sex/ariel_climax.mp3"
            if not persistent.v_sex_anim_enabled_locked and persistent.v_sex_anim_enabled:
                show sc ariel dress rub8
            else:
                show sc arielcosplay a068
            a"That's it [y_name] pump your big dick right into me!"
            a"Make me cum all over it!"
            a"I want to feel your warm seed shoot inside of me so bad [y_name]!"
            if not persistent.v_sex_anim_enabled_locked and persistent.v_sex_anim_enabled:
                show sc ariel dress rub9
            else:
                show sc arielcosplay a067
            a"I'm...{w} going... {w} to..."
            a"NGH!" with vpunch
            if not persistent.v_sex_anim_enabled_locked and persistent.v_sex_anim_enabled:
                show sc ariel dress rub8
            else:
                show sc arielcosplay a068
            with vpunch
            a"OH YES! FUCK ME, [y_name!u]!"
            if not persistent.v_sex_anim_enabled_locked and persistent.v_sex_anim_enabled:
                show sc ariel dress rub10
            else:
                show sc arielcosplay a069
            with vpunch
            a"Uhhh!"
            show sc arielcosplay a070
            with hpunch
            a"Oh god."
            stop sex1 fadeout 1.0
            a"That was... {w}wonderful."
            play sex1 "sound effects/01/sex/female_moaning01.mp3"
            show sc arielcosplay a071
            a"Mmm..."
            play sound "sound effects/01/Door_Knock_Sound_Effect_Free.mp3"
            show sc arielcosplay a072
            if persistent.v_sounds_text_on == True:
                "(Knock, knock, knock)"
            else:
                pause 1.6
            show sc arielcosplay a073
            with hpunch
            a"(OH SHIT!)"
            mc"Are you okay [a_name]?"
            stop sound fadeout 1.0
            show sc arielcosplay a001
            mc"I thought I heard you call my name?"
            show sc arielcosplay a074
            a"NO!"
            a"I MEAN YES! Yes, I'm... I'm fine!"
            show sc arielcosplay a075
            mc"(Hmm... I could've sworn she called my name.)"
            show sc arielcosplay a076
            a"(Oh my god, I cannot believe he heard that!)"
            a"(To think that he nearly caught me like this...)"
            a"(And what if he had walked in on me?)"
            a"(Was it wrong to have such lewd thoughts about [y_name]?)"
            show sc arielcosplay a077
            a"(However, I wonder how he would've reacted, seeing me fingering myself while I'm fantasising about his big dick filling me with his cream...)"
            show sc arielcosplay a077a
            a"(As he fucks me all night long...)"
            a"NGHH..."
            show sc arielcosplay a078
            a"(How about another round, \"[y_name]\"?)"
            $ v_ep01_ariel_fantasy_counter += 1
            $ persistent.replay_ariel_fantasy = False
            stop music fadeout 1.0
            scene onlayer anim_layer
            with { "anim_layer": dissolve}
    #screen goes blank
    stop music fadeout 1.0
    scene black
    with dissolve
    scene black
    with Pause (2)
    $ renpy.end_replay()
    jump lb_ep01_13_03_MC_Evening_Visit2

label lb_ep01_13_03_Bella_evening_yoga:
    #evening yoga helps to remove the fatigue of the day's strain and makes one fresh and calm
    #The MC knocks on Bella's door
    play sound "sound effects/01/Door_Knock_Sound_Effect_Free.mp3"
    show sc bellayoga y091
    with dissolve
    if persistent.v_sounds_text_on == True:
        "(Knock, knock, knock)"
    else:
        pause 1.0
    b"Who is it?"
    stop sound fadeout 1.0
    show sc bellayoga y093
    mc"It's [y_name]."
    show sc bellayoga y092
    b"Come in."
    play sound "sound effects/01/door_close_soft.mp3"
    play music "sound effects/01/Breathe In Calm.mp3" loop fadein 1.0
    show sc bellayoga y001
    with dissolve
    mc"(Hopefully, she's in a good mood for a change.)"
    #The MC enters her room and finds Bella doing yoga
    stop sound fadeout 1.0
    show sc bellayoga y002
    mc"(Oh!)"

    #Yoga links
    #https://www.daz3d.com/z-yoga-and-stretching-pose-mega-set
    #https://www.daz3d.com/fg-yoga-pose-collection-for-genesis-9-and-8-female
    #https://www.daz3d.com/fg-yoga-pose-collection-vol-02-for-genesis-9-and-8-female
    #https://www.daz3d.com/z-advanced-yoga-and-stretching-pose-mega-set-for-genesis-9-and-8-female


    #Bella Yoga position #1 - https://pixhost.to/show/28/449474183_screenshot-2024-02-28-at-11-19-35-am.jpg

    #She has her eyes closed
    show sc bellayoga y004
    b"What can I do for you?"
    show sc bellayoga y002
    mc"Are you doing yoga? At this time of night?"
    mc"Why not first thing in the morning?"
    #She opens her eyes
    show sc bellayoga y004
    b"Yoga in the morning makes a person work better at one's vocation."
    show sc bellayoga y005
    b"In the evening it removes the fatigue of the day's strain and makes one calm and relaxed before going to bed."
    #Bella Yoga position #2 - https://pixhost.to/show/28/449474185_screenshot-2024-02-28-at-11-19-50-am.jpg
    show sc bellayoga y007
    mc"Did you read all that in a yoga manual?"
    show sc bellayoga y073
    b"It's common knowledge, [y_name]."
    b"You may think yoga is a joke but I take it very seriously."
    show sc bellayoga y077
    mc"Yeah, I can see that."

    #Bella Yoga position #3 - https://pixhost.to/show/28/449474190_screenshot-2024-02-28-at-11-20-05-am.jpg
    show sc bellayoga y075
    with dissolve
    b"So, why are you here?"
    show sc bellayoga y010
    mc"I was just wondering if you spoke with [mc_vic_address] about the job we did today?"
    show sc bellayoga y075
    b"No, I didn't get a chance to."
    show sc bellayoga y073
    b"Besides, I don't think he'll care. At least, not until I've forged that painting."
    #Bella Yoga position #4 - https://pixhost.to/show/28/449474186_screenshot-2024-02-28-at-11-19-55-am.jpg
    show sc bellayoga y006
    with dissolve
    mc"(God damn...)"
    #Show behind Bella so we can see her ass in yoga pants
    mc"(Are these actual yoga poses or is she doing this intentionally to see how I'll react?)"
    show sc bellayoga y008
    b"So where did you run off to earlier tonight?"
    show sc bellayoga y009
    b"Still chasing after that one-night-stand who ditched you?"
    show sc bellayoga y021
    mc"Some of us aren't that desperate."
    #Bella shoots him a snide look
    show sc bellayoga y023
    mc"No, I might have a lead on the flash drive."
    #Bella Yoga position #6 - https://pixhost.to/show/28/449474195_screenshot-2024-02-28-at-11-20-47-am.jpg
    show sc bellayoga y024
    b"That's good."
    show sc bellayoga y025
    b"And when you get it back, maybe you won't allow some random skank to distract you so you lose it again."
    show sc bellayoga y026
    mc"What do you mean?"
    # or  mc"Excuse me?"
    show sc bellayoga y027
    b"Oh come on, [y_name]. You can't help yourself."
    show sc bellayoga y028
    b"Whenever you go anywhere, you're the first person to notice a girl wearing a thong or if they're not wearing a bra."
    show sc bellayoga y029
    b"Just last week you commented on that woman who you referred to as \"having headlights that could poke your eye out\"!"
    if v_ep01_06_02_Tattoo_Parlour_Tattoo_Response == "crude":
        b"And of course let's not forget that little scene at the tattoo parlour."
    show sc bellayoga y030
    mc"I just call it as I see it."
    show sc bellayoga y046
    mc"So sue me!"
    show sc bellayoga y031
    b"Do you know what your problem is? You have no self-control."
    show sc bellayoga y032
    b"You think with your head, and usually the wrong one!"
    show sc bellayoga y033
    mc"Bullshit. I have great self-control."
    show sc bellayoga y034
    b"Oh really?"

    #Bella Yoga position #5 - https://pixhost.to/show/28/449474188_screenshot-2024-02-28-at-11-20-02-am.jpg

    #She faces the MC so we can see her hanging cleavage
    show sc bellayoga y035
    mc"(Fuck! Now I know that she's been baiting me ever since I set foot in her room.)"
    show sc bellayoga y037
    mc"(Don't look! Don't look!!)"

    #[Look / Resist]
    menu:
        "Look":
            #The MC zeroes in on her cleavage
            show sc bellayoga y036
            with vpunch
            mc"(Fuck!!)"
            show sc bellayoga y039
            mc"(Dammit! Maybe she has a point.)"
            show sc bellayoga y043
            b"A-ha! I knew it!"
            show sc bellayoga y044
            b"I didn't even have to try that hard."
            show sc bellayoga y042
            b"It's no wonder you lost that drive."
            show sc bellayoga y033
            mc"Yeah, whatever..."
            #GO TO > “Final Part of the Scene"

        "Resist"(wt="Best option"):

            #BONUS POSES if the player chooses this option

            #The MC continues to look at Bella's face
            show sc bellayoga y046
            mc"See? I have complete control."
            show sc bellayoga y047
            b"Is that so?"
            show sc bellayoga y048
            b"Hmm... Maybe I was wrong."

            #ONE BONUS RENDER OF BELLA (IN HER YOGA OUTFIT OR IN THE RESTAURANT) ADDED TO THE PHOTO GALLERY FOR HER PROFILE
            #Show the MC's face
            show sc bellayoga y049
            mc"(Why do I get the feeling that this is not over?)"

            #Bella changes position

            #Yoga position #7 - https://pixhost.to/show/28/449474193_screenshot-2024-02-28-at-11-20-24-am.jpg
            show sc bellayoga y050
            with dissolve
            mc"(Oh shit...)"

            #[Look closer / Resist]
            menu:
                "Look closer":
                    show sc bellayoga y049
                    mc"(Dammit... One quick close-up can't hurt, right?)"
                    #The MC zeroes in between her legs
                    show sc bellayoga y053
                    with vpunch
                    mc"(Fuck!!)"
                    #Bella catches his staring while in this position - https://pixhost.to/show/28/449474193_screenshot-2024-02-28-at-11-20-24-am.jpg
                    show sc bellayoga y055
                    b"A-ha! I knew it!"
                    show sc bellayoga y056
                    b"Same old, [y_name]. He can't help but buckle under the pressure."
                    show sc bellayoga y057
                    b"It's no wonder you lost that drive."
                    show sc bellayoga y033
                    mc"Yeah, whatever..."
                    #GO TO > “Final Part of the Scene"

                "Resist"(wt="Best option"):
                    show sc bellayoga y058
                    mc"(No! She may look insanely hot in that tight, tight outfit.)"
                    show sc bellayoga y059
                    mc"(But I can't let her get the better of me.)"
                    mc"(That's exactly what she wants.)"
                    #ONE BONUS RENDER OF BELLA (IN HER YOGA OUTFIT OR IN THE RESTAURANT) ADDED TO THE PHOTO GALLERY FOR HER PROFILE
                    show sc bellayoga y061
                    b"It's okay to admit that you have a problem, [y_name]. A weakness."
                    show sc bellayoga y062
                    mc"And what's my supposed weakness?"
                    #show Bella's face
                    show sc bellayoga y063
                    b"Hot women... And you're a sucker for a pretty face..."
                    #Bella turns and caresses her backside
                    show sc bellayoga y064
                    b"A tight ass..."
                    #Bella cups both of her breasts
                    show sc bellayoga y065
                    b"Firm, succulent breasts..."
                    show sc bellayoga y066
                    b"It's your Achilles heel."
                    show sc bellayoga y011
                    with dissolve
                    b"Just admit it."
                    show sc bellayoga y013
                    b"You can't resist."



                    #Bella moves into this position

                    #Yoga position #8 - https://pixhost.to/show/28/449474193_screenshot-2024-02-28-at-11-20-24-am.jpg

                #[Give in / Resist]
                    menu:
                        "Give in":
                            show sc bellayoga y067
                            mc"(There's no sense fighting it anymore.)"
                            #The MC zeroes in Bella's ass
                            show sc bellayoga y017
                            mc"(Good Lord...)"
                            show sc bellayoga y015
                            mc"(Maybe she has a point.)"
                            #Bella catches his staring while in this position - https://pixhost.to/show/28/449474193_screenshot-2024-02-28-at-11-20-24-am.jpg
                            show sc bellayoga y019
                            b"A-ha! I knew it!"
                            show sc bellayoga y020
                            b"I knew you would cave!"
                            #Bella rolls her eyes
                            show sc bellayoga y022
                            mc"(Dammit!)"
                            #Bella sits up and faces the MC
                            show sc bellayoga y019
                            b"It's no wonder you lost that drive."
                            show sc bellayoga y033
                            mc"Yeah, whatever..."
                            #GO TO > “Final Part of the Scene"

                        "Resist"(wt="Best option"):
                            show sc bellayoga y070
                            mc"(I've come this far, but she's not winning no matter what she tries.)"
                            $ rewards_unlock ("bella",9)
                            #ONE BONUS RENDER OF BELLA (IN HER YOGA OUTFIT OR IN THE RESTAURANT) ADDED TO THE PHOTO GALLERY FOR HER PROFILE
                            #Bella sits up and faces the MC
                            show sc bellayoga y073
                            with dissolve
                            b"Hmm... Maybe I underestimated you, [y_name]."
                            show sc bellayoga y075
                            mc"Yeah, you certainly did."
                            #Bella smirks
                            show sc bellayoga y077
                            b"Hmm..."

    #"Final Part of the Scene"
    show sc bellayoga y080
    with dissolve
    b"So anyway, if there's nothing else to discuss, I'm gonna take a shower."
    #Bella starts walking towards the bathroom and then stops at the door so we can see her ass
    b"And by the way..."
    #Bella looks down at the MC's crotch
    show sc bellayoga y081
    b"You might want to take care of that before you go to bed."
    show sc bellayoga y084
    mc"Huh?"
    #The MC looks down and sees he has an obvious erection
    show sc bellayoga y083
    with vpunch
    mc"(Oh!!)"
    mc"(Shit! I didn't even notice!)"
    show sc bellayoga y085
    b"Sweet wet dreams, [b_mc_address]."
    play sound "sound effects/01/sexy_female_laugh2.mp3"
    show sc bellayoga y086
    b"Hahaha!"
    #Bella enters the bathroom and closes the door behind her
    mc"(SON OF A BITCH!!)"
    stop sound fadeout 1.0
    play sound2 "sound effects/01/door_close_soft.mp3"
    show sc bellayoga y088
    with dissolve
    mc"(Maybe I really don't have any self-control when it comes to attractive women.)"
    stop sound2 fadeout 1.0
    show sc bellayoga y090
    mc"(Fuck!)"
    stop music fadeout 1.0
    #screen goes blank
    scene black
    with dissolve
    scene black
    with Pause (2)
    jump lb_ep01_13_03_MC_Evening_Visit2
