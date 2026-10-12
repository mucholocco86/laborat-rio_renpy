init:
    image anim_ep_02_the_calm_before_the_storm = Movie(channel="movies_with_sound", loop=False, fadeout=1.0, play='images/extras/Episode 02/anim_ep_02_the_calm_before_the_storm.webm', image=Crop((0,0,1920,1080), "#000"))

label lb_ep02_01_01_Team_Meeting_Without_The_MC:
    #SCENE BEGINS
    #text on the screen, with a balcony background
    $ renpy.music.set_volume(1.0, 0.0, channel="music")
    $ v_review_episode = 2
    scene black
    with dissolve
    scene black
    with Pause (3)
    if persistent.v_anim_enabled:
        scene anim_ep_02_the_calm_before_the_storm:
            size (config.screen_width, config.screen_height)
        pause 7.0
    else:
        show ep02 calm before storm
        with dissolve
        pause 3.0
    scene black
    with dissolve
    scene black
    with dissolve
    pause 1.0
    centered "Meanwhile, back at the house...{w=2.0}{nw}" with dissolve
    show text "Meanwhile, back at the house..." #THESE LINES ARE NOT DUPLICATES. Needed to fade the text in and out!
    scene bg black with Dissolve(1)
    pause 1.0
    if v_stats_task_4_rating == "aa":
        $ v_ep01_06_02_Tattoo_Parlour_Tattoo_Response = "crude"

    #screen fades and leads into the opening scene
    #(The scene begins with the girls sitting at the kitchen table, they look worried)
    #the girls all wear casual clothing - Ariel wears her glasses
    #(There are items on the table showing some of the things they stole - the green dress (Vivian),
    #Ariel's security cards, Bella's art stuff - painting stuff, brushes)

    #(Ariel speaks to Vivian)
    play music "sound effects/02/Family Gathering.mp3" loop fadein 1.0
    scene sc ep2groupmeeting m001
    with dissolve
    a"Have you heard from [y_name]? Has he called?"
    show sc ep2groupmeeting m002
    v"No, sweetheart. Not since lunchtime."
    show sc ep2groupmeeting m008
    a"I hope he's okay."
    #same Ariel render as above
    show sc ep2groupmeeting m001
    a"[vic_name] will be home any minute now."
    show sc ep2groupmeeting m004
    b"Where do you think he could be?"
    show sc ep2groupmeeting m005
    v"He's probably out looking for that flash drive."
    show sc ep2groupmeeting m006
    b"He's going to run out of time."
    #same Ariel render as above
    show sc ep2groupmeeting m008
    a"What are we going to do?"
    show sc ep2groupmeeting m009
    v"I'll see if I can get a hold of him."
    stop music fadeout 1.0
    #Vivian calls the MC, and puts the phone to her ear
    # The dial tone for the call
    play sound "sound effects/01/Phone_call_dialling_sound_effect.mp3" loop
    show sc ep2groupmeeting m010
    with dissolve
    "..."
    "... ..."
    stop sound fadeout 1.0
    show sc ep2groupmeeting m011
    mc"{i}You've reached the answering service for [y_name]. Please leave a message, after the beep.{/i}"
    #Vivian looks concerned
    show sc ep2groupmeeting m012
    v"[y_name], it's [mc_v_address!c]."
    #Vivian looks surprised
    show sc ep2groupmeeting m013
    mc"{i}HEY! I said {b}after{/b} the beep!{/i}"
    #Vivian looks confused
    show sc ep2groupmeeting m014
    v"Huh??"
    play sound "sound effects/02/beep_sound_effect.mp3" noloop
    "(BEEP!)"
    #beeping sound
    show sc ep2groupmeeting m015
    v"Um... [y_name], it's [mc_v_address!c]."
    show sc ep2groupmeeting m016
    v"Where are you? Did you forget that we had a team meeting at the house this evening?"
    #same Vivian render as above
    v"Please call me back as soon as possible, it's important. [vic_name] will be home shortly, sweetheart."
    #slightly different expression for this last line
    #the call ends
    show sc ep2groupmeeting m017
    b"Was that his answering machine?"
    show sc ep2groupmeeting m018
    v"I'm afraid so."
    show sc ep2groupmeeting m019
    b"Oh, geez... This is not good."
    show sc ep2groupmeeting m017
    b"[mc_vic_address] is going to lose his shit!"
    #same Bellal render as above
    play sound "sound effects/01/Door_Opening.mp3" noloop
    if persistent.v_sounds_text_on == True:
        "(Door opens)"
    else:
        scene sc ep2groupmeeting m020
        with dissolve
        pause 1.5

    #the front door opens, and Victor arrives home - show him entering the front door
    play music "sound effects/01/Cool Vibes.mp3" loop fadein 1.0
    show sc ep2groupmeeting m021
    with faster_dissolve
    v"Oh!"
    #Vivian looks towards the front door
    show sc ep2groupmeeting m022
    v"That will be [vic_name] now."
    #Vivian looks at the two girls
    show sc ep2groupmeeting m023
    v"Remember, don't speak unless you're spoken to."
    #(Victor arrives in the main room where the girls are)
    #Ariel looks really worried
    show sc ep2groupmeeting m025
    a"(Oh no... I can feel my nerves jangling.)"
    show sc ep2groupmeeting m026
    a"([y_name]... Where are you??)"
    show sc ep2groupmeeting m024
    with dissolve
    pause 1.0
    show sc ep2groupmeeting m027
    with dissolve
    vic"Evening, all."
    #Victor sees the stuff on the table - he stands at the end of the table while the girls sit for the rest of this scene
    show sc ep2groupmeeting m028
    vic"Is this what I think it is?"
    #victor looks impressed
    show sc ep2groupmeeting m029
    v"Yes, [vic_name]."
    show sc ep2groupmeeting m030
    v"I was able to get the dress that you requested, and also some wigs."
    #same render as above
    show sc ep2groupmeeting m031
    b"And I managed to steal the supplies I need to make that painting."
    show sc ep2groupmeeting m032
    vic"Very good. And what about you, [a_name]?"
    #he turns to Ariel
    show sc ep2groupmeeting m033
    a"I um... I got the cards that you asked for, [mc_vic_address]."
    show sc ep2groupmeeting m034
    vic"Do you mean to tell me that you did that all by yourself?"
    #Vic looks sceptical

    #Ariel bows her head down as she responds
    show sc ep2groupmeeting m035
    a"Um, no..."
    a"I uh... I had some help. From [y_name]."
    #Ariel looks up at Victor
    show sc ep2groupmeeting m034
    vic"Is that right?"
    show sc ep2groupmeeting m038
    b"He also helped me out with getting these items from the art school."
    show sc ep2groupmeeting m039
    v"Same here. He created a distraction in the theatre so I could get in and out of the clothing room unnoticed."
    show sc ep2groupmeeting m040
    v"That's great, right?"
    #Vivian looks hopeful
    show sc ep2groupmeeting m037
    vic"All of you got everything that we need, that's the main thing."
    #same render as above
    show sc ep2groupmeeting m018a
    v"(He still won't acknowledge [y_name] and the great work that he's done.)"
    #the girls seem disappointed that Victor hasn't acknowledged the MC
    show sc ep2groupmeeting m041
    vic"By the way, where is [y_name]?"
    show sc ep2groupmeeting m044
    v"He's not here, [vic_name]."
    show sc ep2groupmeeting m045
    vic"What!?"
    vic"What do you mean he's not here?"
    #Victor looks pissed
    show sc ep2groupmeeting m046
    b"We think he's still out looking for the flash drive."
    show sc ep2groupmeeting m047
    vic"That boy's not going to make it back in time."
    show sc ep2groupmeeting m048
    v"But you said that he still has time."
    show sc ep2groupmeeting m045
    vic"He has until tomorrow morning at the very latest."
    show sc ep2groupmeeting m050
    vic"And I know what I said."
    show sc ep2groupmeeting m052
    vic"But I also know a failed mission when I see one."
    #Victor starts to get angry
    show sc ep2groupmeeting m037
    vic"Anyway, he still should be present for our team meeting, regardless."
    show sc ep2groupmeeting m034
    vic"Had he not lost the drive in the first place, we wouldn't be having this discussion."
    #slightly different render to the above
    show sc ep2groupmeeting m053
    v"I tried calling him, but he didn't answer. I think he could be in trouble."
    show sc ep2groupmeeting m055
    vic"That's not our problem [v_name]!"
    #Victor gets angry
    show sc ep2groupmeeting m050
    vic"Don't you get it? The kid is a liability, a burden, our weak link."
    #same render as above
    show sc ep2groupmeeting m047
    vic"And weak links need to be cut off."
    show sc ep2groupmeeting m056
    v"No, you can't do that."
    show sc ep2groupmeeting m057
    vic"Don't tell me what I can and can't do, woman!"
    show sc ep2groupmeeting m045
    vic"The number of chances I've given [y_name]... Let's be honest, he'll never be good enough to be part of our future heists."
    #slightly different render to above
    show sc ep2groupmeeting m058
    vic"And the worst thing about it is, I gave him another chance because I stupidly listened to you. To all three of you!"
    #They all bow their heads and look disappointed
    show sc ep2groupmeeting m059
    a"I... I could track his phone, to find out where he is."
    show sc ep2groupmeeting m043
    vic"No..."
    #same render as above
    show sc ep2groupmeeting m061
    vic"Where [y_name] is right now is none of your concern. That goes for you as well, [b_name]."
    show sc ep2groupmeeting m062
    vic"If you all have so much faith in [y_name], then he'll get out of whatever situation he's in and be back here with the flash drive by tomorrow morning."
    vic"Sooner, if he has any respect for me or any of you."
    # or
    #vic"Sooner, if he has any respect for me or the [private_group]."
    #slightly different render to above
    show sc ep2groupmeeting m063
    vic"Now let there be no more talk about this."
    #slightly different render to above
    show sc ep2groupmeeting m064
    vic"We need to discuss the next heist and start putting plans in place..."
    #slightly different render to above
    #final shot of Victor talking to all three girls - no dialogue, screen to fade
    #(screen goes blank)"
    stop music fadeout 1.0
    scene black
    with dissolve
    scene black
    with Pause (2)
    jump lb_ep02_01_02_The_MC_is_kidnapped_by_the_Apex_Legion
    #END SCENE
