label lb_ep02_03_02_The_Group_Has_Breakfast:
    #SCENE BEGINS
    #The scene begins with the MC going down the stairs

    scene sc vicangryj 001
    with dissolve
    mc"(Uh... What a horrible sleep.)"

    show sc vicangryj 002
    mc"(And now it's time for me to face the music.)"
    #The MC enters the kitchen, where it's deserted

    show sc vicangryj 003
    mc"(Or perhaps not.)"
    #Victor appears behind him
    play music "sound effects/02/Griphop.mp3"
    show sc vicangryj 004
    vic"So, he finally shows."
    #The MC turns around and sees Victor with his hands on his hip

    show sc vicangryj 005
    vic"You were out late again last night, [y_name], after curfew, and now your time is up."


    menu:
        "Stand up for yourself"(wt="Best option"):
            show sc vicangryj 006
            vic"You failed me yet again and-"
            show sc vicangryj 013
            mc"Hey! Can it, old man!"
            show sc vicangryj 008
            mc"How about you drop the tough man act before you look even more stupid?"
            show sc vicangryj 022
            vic"Excuse me??"
            #Victor is on the verge of losing his shit

        "Rude reply":
            show sc vicangryj 006
            vic"You failed me yet again and-"
            show sc vicangryj 031
            mc"Fuck off, [mc_vic_address]!"
            show sc vicangryj 013
            mc"How about you drop the tough man act before you look even more stupid?"
            show sc vicangryj 022
            vic"Excuse me??"
            #Victor is on the verge of losing his shit

        "Do nothing":
            show sc vicangryj 011
            mc"(Great... Here we go again.)"
            show sc vicangryj 006
            vic"You failed me yet again and-"

    #scene continues

    show sc vicangryj 012
    mc"Here..."
    #He throws the drive and Victor catches it

    show sc vicangryj 010
    with dissolve
    mc"I got the damn drive back, despite you criticising me all the time."

    show sc vicangryj 014
    vic"Oh..."

    show sc vicangryj 015
    mc"Is that it? Any more insults that you want to throw at me?"
    #The MC holds his hands up out to the side, questioning Victor

    show sc vicangryj 024
    vic"How did you get it?"
    #Victor questions the MC

    show sc vicangryj 017
    mc"That's not important right now."
    #the MC is a little calmer now

    show sc vicangryj 018
    mc"What's important is that we have it, and you can let me in on this next heist."
    #a slightly different expression to the one above

    show sc vicangryj 019
    mc"That was the deal, remember?"
    #He looks at Victor sternly

    show sc vicangryj 020
    vic"I know what I said."
    #Victor replies but doesn't make eye contact with the MC

    show sc vicangryj 021
    mc"And to sweeten the pot, I also managed to swipe a keycard from the security guard at the art gallery."

    show sc vicangryj 022
    vic"When the hell did you go there?"

    show sc vicangryj 023
    mc"The other day, with [mc_v_address!c]."

    show sc vicangryj 009
    vic"You two seem to be spending a lot of time together."
    show sc vicangryj 010
    mc"No more than usual."

    show sc girlscomesdownk 021
    mc"(He could be right though.)"
    #the MC thinking

    show sc vicangryj 027
    mc"(We have been hanging out a lot.)"

    show sc vicangryj 024
    vic"If I include you in this next mission, you will need to be flawless."
    #He looks at him with the same expression as above

    show sc vicangryj 029
    vic"No unlocked doors, no having to chase after people to retrieve stolen items."
    #a slightly different expression to the one above

    show sc vicangryj 030
    vic"You may have completed your task, but I still have my concerns."
    #he points at the MC and looks at him sternly

    show sc vicangryj 031a
    mc"Oh come on, this is horseshit!"
    #the MC gets angry and throws his hands up

    show sc vicangryj 032
    mc"And I couldn't give a fuck about your, \"concerns\"."
    #the MC makes quotation marks with his fingers
    show sc vicangryj 033
    mc"So you either be a man of your word, or there will be no reason for anyone to believe anything that comes out of your mouth."
    #reuse the same render as above
    show sc vicangryj 024
    vic"Listen up you little shit... Nobody speaks to me like that, especially in my own house."
    #reuse the same render as above
    show sc vicangryj 032
    mc"Yeah, well... All this week you've treated me like a nobody."
    #reuse the same render as above
    show sc vicangryj 033
    play sound "sound effects/02/sound_from_upstairs_effect.mp3" noloop
    mc"And this nobody is still here. I'm not going anywhere."
    #An intense stare-off is interrupted when the stairs rattle
    #SOUND EFFECT from UPSTAIRS
    show sc vicangryj 034
    mc"That will be the girls."
    #the MC looks towards the stairs
    show sc vicangryj 023
    mc"I can't imagine that you'll go back on your word now, huh?"
    #The MC looks cockily with an evil grin at Victor
    show sc vicangryj 030
    vic"{i}(*Whispering*){/i}\nThis isn't over."
    #Victor leans in close and whispers to the MC
    show sc vicangryj 037
    mc"{i}(*Whispering*){/i}\nI'm glad we agree on that."
    #Victor sees the girls coming down the stairs
    show sc vicangryj 038
    vic"..."
    stop music fadeout 1.0
    #Victor grimaces
    #screen continues with the next doc
    jump lb_ep02_03_03_Victor_makes_the_MC_part_of_the_next_heist
    #END SCENE

