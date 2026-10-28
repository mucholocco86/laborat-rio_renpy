default bonus_scene1_open = False #REBECCA

default bonus_scene2_handjob_first = True
default bonus_scene2_thighjob_first = True
default bonus_scene2_handjob = False
default bonus_scene2_thighjob = False

default bonus_scene2 = False #QUEEN

default bonus_scene2_handjob2 = True

default bonus_scene2_cum_first = False

default bonus_scene3 = False #DIANA
default bonus_scene3_vsex = False
default bonus_scene3_asex = False

image bonus2_q_handjob1 = Movie(play="images/bonus_scene/queen_bonus1/bonus2_q_handjob1.webm", loop=True)
image bonus2_q_handjob2 = Movie(play="images/bonus_scene/queen_bonus1/bonus2_q_handjob2.webm", loop=True)
image bonus2_q_thighjob = Movie(play="images/bonus_scene/queen_bonus1/bonus2_q_thighjob.webm", loop=True)

label bonus_scene2_handjob:
    $ bonus_scene2_handjob = True
    $ bonus_scene2_handjob2 = False
    $ bonus_scene2_thighjob = False
    scene black with Dissolve(0.3)
    show bonus2_q_handjob1 with dissolve
    if bonus_scene2_handjob_first:
        $ bonus_scene2_handjob_first = False
        mc "Fuck... I can feel how wet you are just from rubbing against your pussy."
        q "Hah~ You're already desperate to get back inside me, aren't you?"
        sensation "Her gloved hand grips your cock tightly, slick with her own juices as she strokes you."
        if not mc_maia_left:
            q "Mmm~ Even after you already came once, you're still so hard... Maia is truly blessed to have a husband like you."
        else:
            q "Mmm~ Even after ejaculating once, you're still rock hard..."
            
        q "You're holding my foot up to your face. Are you doing that on purpose?"

        if mc_liked_feet:
            mc "Ahhn... Yeah, I am. I want to stare at your feet while I tease your dripping pussy."
            q "*laughs* How interesting~ So [mc] has a thing for feet... I never paid much attention to my servants' feet, but I imagine Maia's would drive you wild."
        else:
            mc "Ahhn..."
            q "No answer? *chuckles* The pleasure must have taken your breath away."

        q "Ahhn~ Hah... Go back to mating with me properly, [mc]. You've teased me enough..."
        sensation "Her slick pussy juices coat your cock, dripping down onto the mattress. You feel her shuddring slightly as you glide from her hole to her clit."

    else:
        sensation "You thrust between her soft thighs, her soaked pussy lips rubbing against your shaft."
        q "Ahmm~ Nnnh~ You're going to make me squirt, [mc]... *chuckles* Last time I let go, we had to change the sheets."
        mc "I couldn't care less... Aghn... Watching you cum would push me over the edge!"
        q "C-Careful what you wish for... I can feel myself swelling up. If you continue at this pace, I might not be able to hold back."
        perception "She lets out a sharp moan as your cock grazes her clit."
    
    $ bonus_scene2_cum_first = True
    call screen scene13_choice04 with dissolve

label bonus_scene2_handjob2:
    $ bonus_scene2_handjob = False
    $ bonus_scene2_handjob2 = True
    $ bonus_scene2_thighjob = False
    scene black with Dissolve(0.3)
    show bonus2_q_handjob2 with dissolve
    q "The head is the most sensetive part... You're leaking quite a lot."
    mc "Ahhn~! Your gloves feel really good!"
    call screen scene13_choice04 with dissolve

label bonus_scene2_thighjob:
    $ bonus_scene2_thighjob = True
    $ bonus_scene2_handjob2 = False
    $ bonus_scene2_handjob = False

    scene black with Dissolve(0.3)
    show bonus2_q_thighjob with dissolve
    if bonus_scene2_thighjob_first:
        $ bonus_scene2_thighjob_first = False
        sensation "You press your cock between her soft, warm thighs. Her dripping pussy slowly coats your shaft."
        mc "Ahhn! You're squeezing me so tightly!"
        q "Of course~ The whole point is to make the man spill his seed, isn't it?"
        q "Though in this case... your seed would go to waste."
        mc "Your Majesty! It's never a waste if I'm with you!"
        q "*chuckles* Such a smooth talker."
        sensation "Her ass presses back against you, soft and plush."

    else:
        sensation "You thrust between her slick thighs again, now even wetter from her leaking pussy."
        q "Still not satisfied with my thighs, I see?"
        mc "I'll never get enough... Your soft thighs... your dripping pussy... I'm in heaven!"
        q "*laughs* How easy it is to please a man. Simply show him your rear and he will follow you to the grave."
        mc "Aghn... You're not wrong."
        perception "You rock your hips, trying desperately not to slip inside her."
        q "Go on then... spill your seed, [mc]! Watching your thick member slide between my thighs is driving me crazy... I feel like I'm going to leak everywhere!"

    $ bonus_scene2_cum_first = True
    call screen scene13_choice04 with dissolve

default bonus_scene2_cum = False
label bonus_scene2_cum:
    $ bonus_scene2_cum = True
    mc "I'm close!"
    if bonus_scene2_handjob or bonus_scene2_handjob2:
        sensation "Her pussy is dripping uncontrollably now, practically gushing with every stroke."
        q "A-Are you about to release?"
        mc "I'm going to cover your breasts!"
        play sound "se_sfx/sex/sex_cum5.mp3" 
        scene bonus_scene2_s1 with vpunch
        sensation "Pleasure surges through you as thick ropes of cum erupt from your cock, painting her large breasts and collarbone in messy white streaks."
        q "Ahh~! It's so hot...! I'm— I'm—!"
        play sound "se_sfx/sex/sex_cum4.mp3" 
        scene bonus_scene2_s2 with vpunch
        sensation "Her pussy spasms violently as a small spurt of clear liquid shoots out, splashing against the underside of your cock."
        scene bonus_scene2_s3 with Dissolve(1.0)
        q "Hahh... Ahh... I actually came just from you rubbing against me... I thought that was impossible without penetration."
        mc "I was focusing on your clit the whole time. You didn't notice?"
        q "Aha... so that's why I felt that urge every time you thrust..."
        mc "..."
        q "Nevertheless... I'm covered in your essance, and you're covered in mine. A fair trade, wouldn't you say?"
        mc "*chuckles* Yeah... I'd say so."
    else:
        sensation "Her thighs squeeze tightly around you as her pussy flutters wildly, clearly on the verge of squirting."
        q "Go on, [mc]! Spill it all out!"
        play sound "se_sfx/sex/sex_cum5.mp3" 
        scene bonus_scene2_s4 with vpunch
        mc "Ahnng!"
        play sound "se_sfx/sex/sex_cum4.mp3" 
        scene bonus_scene2_s5 with vpunch
        sensation "You thrust one final time between her soft thighs and explode, thick ropes of cum shooting onto the floor—some even splashing on her legs."
        q "Hah~! So much even for the second time..."
        scene bonus_scene2_s6 with Dissolve(1.0)
        sensation "She gently rocks her thighs back and forth, milking every last drop from you."
        mc "Ahh... Your thighs feel incredible. I could barely hold myself together."
        q "*chuckles* Of course they do. I've kept this body in excellent shape over the years... though it was only for appearances."
        q "Until now, it seems."
        mc "God... I wish I could lay with you every night, Your Majesty."
        q "Careful now. Don't fall in love with me too quickly."
        q "I'm afraid this can't continue forever, [mc]. I have responsibilities... and so will you in the future. We can't keep doing this indefinitely."
    $ renpy.end_replay()
    jump scene14


default is_diana_vsex_cowgirl_first = True

default is_diana_vsex_cowgirl_sec = False

image is_diana_anim_vsex4 = Movie(play="images/bonus_scene/diana_bonus1/is_diana_anim_vsex4.webm", loop=True)
image is_diana_anim_asex5 = Movie(play="images/bonus_scene/diana_bonus1/is_diana_anim_asex5.webm", loop=True)

label is_diana_vsex_cowgirl:
    $ is_diana_anim_vsex1 = False
    $ is_diana_anim_vsex2 = False
    $ is_diana_anim_vsex3 = False
    $ bonus_scene3_vsex = True

    scene black with Dissolve(0.3)
    show is_diana_anim_vsex4 with dissolve
    if is_diana_vsex_cowgirl_first:
        $ is_diana_vsex_cowgirl_first = False
        $ is_diana_vsex_cowgirl_sec = True
        perception "Diana pushes you onto your back and climbs on top of you, straddling your hips."
        di "Mmm... Time for me to take charge, darling. I want you deep in my pussy now."
        di "Fhnnm~ Fuck... You're stretching me so nicely. I love this position... I get to control exactly how deep you go."
        mc "Shit, Diana... You're soaking wet."
        di "Ahhn~! Watch me fuck you properly~"
        di "Just lie back and enjoy the ride, darling."
        mc "Ahhnn! You'll make me spill inside you at this rate..."
        sensation "Diana rides you even harder, slamming herself down onto your cock with wild abandon. Her pussy clenches and flutters around you as she chases her pleasure."
    elif is_diana_vsex_cowgirl_sec:
        $ is_diana_vsex_cowgirl_sec = False
        perception "Her body shudders violently as another orgasm overtakes her. Her juices coat your shaft and drip down your balls."
        di "Fuuuck~ Right there! You're hitting so deep in my cunt... Keep stretching me out just like that!"
        di "I want every inch! Pound my greedy pussy from below if you can~ Make me feel it in my womb!"
        mc "You're riding me like you've been starving for this."
        di "Yes~! I have been. Use me. Fill my insatiable pussy~"
        if diana_pregnant:
            mc "You want me to breed you again!?"
        else:
            mc "You want me to breed you!?"
        if mc_harem_diana and mc_convince_diana_pregnancy:
            di "Yes~! Don't pull out! Pump me full. I want your cum leaking down my thighs when I walk later~ Give it to me!"
            mc "Fine! I'll give it to you! Hell, I'll give you twins!"
        else:
            di "No! I'm just dirty talking to you, darling. Trying to make you feel like heaven~"
    else:
        di "Ahhnn~ Mfhnnn~ Yes! Fuck me deep, baby~"

    call screen is_diana_vsex_choice01 with dissolve

default is_diana_asex_pile_first = True

default is_diana_asex_pile_sec = False

    
label is_diana_asex_pile:

    $ bonus_scene3_asex = True
    $ is_diana_anim_asex1 = False
    $ is_diana_anim_asex2 = False
    $ is_diana_anim_asex3 = False

    scene black with Dissolve(0.3)
    show is_diana_anim_asex5 with dissolve
    if is_diana_asex_pile_first:
        $ is_diana_asex_pile_first = False
        $ is_diana_asex_pile_sec = True
        perception "Diana lies beneath you, flushed and glistening with sweat, her heavy breasts pressed against her own chest. Her eyes are half-lidded with pleasure."
        di "Fhnnm~ In this position, I can feel it go even deeper!"
        mc "Fuck, Diana! You're still so tight!"
        di "Ahhn~! Of course I am... I've been saving this hole for someone who knows how to use it. Mmm! Harder, darling~ Don't hold back on me."
        sensation "You drive into her with deep, powerful thrusts. Her puckered hole grips you like a vice, hot and slick."
        di "Fuuuck~ Right there! You're hitting so deep! I can feel you all the way in my belly... Keep pounding my fucking ass just like that!"
        di "Fuck my ass deeper~! I want to feel you for days~ Make this slutty ass yours!"
        mc "You want me to fill this hole?"
        di "Yes~! Don't pull out! Fill me up. I want to feel you throb inside my ass when you cum. Give it to me~"
        mc "Fine. I'll ruin your hole. You'll remember the shape of my cock for weeks!"
    elif is_diana_asex_pile_sec:
        $ is_diana_asex_pile_sec = False
        di "Yes! Just like that! Don't think, just fuck me~! I'm so close... Make me cum with that thick cock buried in my ass!"
        sensation "Her walls flutter wildly around you. The combination of the degrading dirty talk and the merciless angle quickly pushes her over the edge."
        di "Please! Humiliate me~! Destroy me~! Fuck me~! Use me like I'm nothing but a toy~"
        mc "Where is this coming from?"
        di "Mhnn~ W-What?"
        mc "I feel like you want to be abused. Do you actually like it this rough, or... is there something else going on?"
        di "Shut the fuck up and make me cum from my ass~!"
        mc "A-Alright..."
        perception "Her head falls back with a broken cry, her body shuddering as the pleasure overtakes her again."
    else:
        di "Ahhmm~ Yess~! Fuck~ I love how you're using my asshole so carelessly! Soo depraved~!"

    call screen is_diana_asex_controls with dissolve