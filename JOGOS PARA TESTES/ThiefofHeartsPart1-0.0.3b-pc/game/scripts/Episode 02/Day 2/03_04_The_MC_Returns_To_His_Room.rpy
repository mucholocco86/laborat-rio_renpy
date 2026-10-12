label lb_ep02_03_04_The_MC_Returns_To_His_Room:
    #SCENE BEGINS
    play music "sound effects/02/Sibling_Blues.mp3" loop fadein 1.0
    scene sc harrymisscalll 001
    with dissolve
    #show the MC is walking up the stairs after breakfast, thinking
    mc"([mc_v_address!c]'s breakfast really hit the spot. A great way to start my day.)"
    mc"(If only I could say for certain that the rest of it will go just as well.)"
    #The MC sees Bella standing outside his bedroom door, looking at him unamused
    show sc harrymisscalll 003
    mc"(Great...)"
    show sc harrymisscalll 002
    mc"(Oh well... It was nice while it lasted.)"
    #Be a smart-ass / Act normally
    menu:
        "Be a smartass"(wt="Bonus image"):
            show sc harrymisscalll 007
            mc"Are you stalking me? Because that would be super."
            show sc harrymisscalll 027
            b"Yeah, you wish."
            $ rewards_unlock ("bella",15)
        "Act normally":
            show sc harrymisscalll 004
            mc"[b_name]..."
            #the MC half-heartedly acknowledges her
    show sc harrymisscalll 005
    b"So, he finally included you in the upcoming heist. Congratulations."
    #she says this with very little enthusiasm
    show sc harrymisscalll 006
    b"You must be pretty proud of yourself."
    show sc harrymisscalll 007
    mc"I have to say that I am."
    #the MC looks happy with himself
    show sc harrymisscalll 008
    b"Just don't screw up like you did last time."
    show sc harrymisscalll 009
    mc"So we're back to this again, huh?"
    show sc harrymisscalll 010
    mc"One day you're sweet and kind like {i}Charlie Baileygates{/i}, the next minute you turn into that psycho, {i}Hank Evans{/i}."
    show sc harrymisscalll 011
    b"I don't know who either of those people are."
    b"Anyway, don't you go thinking for a second that we're best friends just because you helped me."
    show sc harrymisscalll 011a
    mc"We're on the same side, [b_name]."
    show sc harrymisscalll 013
    mc"Maybe you should focus more on that instead of whatever issues you have with me."
    show sc harrymisscalll 014
    b"Yeah, whatever."
    #Bella looks away from the MC
    show sc harrymisscalll 015a
    mc"What is your problem?"
    show sc harrymisscalll 016
    b"..."
    #Bella refuses to answer
    show sc harrymisscalll 017
    mc"Is this about last night after I came home?"
    show sc harrymisscalll 018
    b"I have no idea what you're talking about."
    #She refuses to make eye contact with him


    #Add these lines if the player has LESS than ONE HEART with BELLA
    if bella_love_level == 0:
        show sc harrymisscalll 019
        mc"You know, I can't believe you're still bothered by this other girl."
        show sc harrymisscalll 020
        mc"I'm not going through this shit with you again."
        show sc harrymisscalll 021
        mc"I have better things to do."
        show sc harrymisscalll 022
        mc"So excuse me. I'd like to go to my room if you don't mind."
        show sc harrymisscalll 023
        b"Fine, no one's stopping you."
        #She steps aside
        show sc harrymisscalll 024
        mc"(God, she can be downright annoying...)"
        #Show the MC entering his room while Bella watches him, looking at him snakily
        #Go Down to - SCENE CONTINUES
    else:
        if bella_heart_ep02_scene_03_let_her_leave == True:
            show sc harrymisscalll 019
            mc"You know, I can't believe you're still bothered by this other girl."
            show sc harrymisscalll 020
            mc"And I'm not going through this shit with you again."
            show sc harrymisscalll 021
            mc"I have better things to do."
            if bella_love_level == 1:
                #Add these lines if the player has ONE HEART with BELLA and they chose to "Let her leave" in Scene 02-03
                show sc harrymisscalll 022
                mc"Now if you'll excuse me, I'm going to my room."
            else:
                #Add these lines if the player has TWO HEARTS with BELLA and they chose to "Let her leave" in Scene 02-03
                show sc harrymisscalll 022
                mc"I'd like to go to my room if you don't mind."
            show sc harrymisscalll 023
            b"Fine, no one's stopping you."
            #She steps aside
            show sc harrymisscalll 024
            mc"(God, she can be downright annoying...)"
            #Show the MC entering his room while Bella watches him, looking at him in a snarky way with her arms folded
            #Go Down to - SCENE CONTINUES
        else:
            show sc harrymisscalll 025
            mc"Look, if this is about that other girl, then-"
            show sc harrymisscalll 026
            b"UGHH... Do you seriously think I'm bothered by that?"
            #she looks annoyed
            show sc harrymisscalll 027
            b"You really do have a one-track mind, don't you?"
            show sc harrymisscalll 028
            mc"Why are you even here?"
            show sc harrymisscalll 029
            b"I just wanted to tell you to look after yourself is all."
            if bella_love_level == 1:
                #Add these lines if the player has ONE HEART with BELLA and they chose to "Stop her" in Scene 02-03
                if bella_heart_ep02_scene_03_let_her_leave == False:
                    # Added here instead at the end of 02-03, otherwise this scene does not play right.
                    $ bella_love_level +=1
                show sc harrymisscalll 030
                mc"Oh... Okay."
                #the MC calms down
                show sc harrymisscalll 031
                mc"Thanks, I guess."
                show sc harrymisscalll 016
                mc"(Whatever I said to her last night must have had a positive effect.)"
                show sc harrymisscalll 022
                mc"Excuse me. I'd like to go to my room if that's okay?"
                show sc harrymisscalll 023
                b"Of course. Don't let me stop you."
                #She steps aside
                show sc harrymisscalll 047
                mc"(Hmm... Maybe she isn't half as annoying as I've made her out to be...)"
                #Show the MC entering his room while Bella watches him, with a sexy smile on her face and arms folded
                #Go Down to - SCENE CONTINUES
            else:
                #Add these lines if the player has TWO HEARTS with BELLA and they chose to "Stop her" in Scene 02-03
                show sc harrymisscalll 031
                mc"Is that it?"
                show sc harrymisscalll 034
                b"Yeah, why else would I be here?"
                show sc harrymisscalll 035
                mc"I see what's going on here..."
                #Bella looks away from the MC
                show sc harrymisscalll 033
                mc"This is because I kissed you."
                #Bella looks at the MC
                show sc harrymisscalll 030
                mc"You're still pissed about it, aren't you?"
                #reused a render from above
                show sc harrymisscalll 037
                mc"And you're here to slap my other cheek to even things out on either side of my face, right?"
                show sc harrymisscalll 038
                b"No, I just wanted to ask you..."
                show sc harrymisscalll 039
                b"Why did you do it?"
                #she innocently asks
                show sc harrymisscalll 030
                mc"Call it an impulse decision."
                show sc harrymisscalll 041
                b"Really? That's your reason?"
                show sc harrymisscalll 036
                mc"Well, maybe I had other reasons."
                show sc harrymisscalll 035
                mc"But they're for me to know, and for you to try and figure out."
                show sc harrymisscalll 043
                b"Other reasons? What other reasons?"
                #Bella looks at the MC, confused
                mc"(Man I love messing with her.)"
                #the MC has a grin on his face while Bella mulls things over
                show sc harrymisscalll 045
                mc"Now I'm going to my room, if you don't mind."
                show sc harrymisscalll 046
                b"Fine, be my guest."
                show sc harrymisscalll 005
                b"But I'm going to get those reasons out of you one way or another, [y_name]!"
                #She steps aside and still looks confused
                show sc harrymisscalll 047
                mc"(Haha... Knowing [b_name], she'll be thinking about that kiss for the rest of the day...)"
                #Show the MC entering his room with a big smile on his face while Bella watches him, with a sexy smirk on her face and arms folded
                #Go Down to - SCENE CONTINUES

    #SCENE CONTINUES
    stop music fadeout 1.0
    show sc harrymisscalll 048a
    with dissolve
    mc"(Finally, I might be able to relax before I have to go to work.)"
    play sound "sound effects/01/Cell_Phone_Ring_Sound_Effect_-_reduced.mp3" loop
    if persistent.v_sounds_text_on == True:
        "(Phone rings)"
    else:
        pause 2.0
    show sc harrymisscalll 048
    mc"(Of course, it's Harry.)"
    #The MC rolls his as he looks at his phone
    stop sound fadeout 1.0
    $ renpy.music.set_volume(0.2, 0.0, channel="ambient")
    play ambient "sound effects/01/gymnasium_ambience2.ogg" loop fadein 1.0
    show sc harrymisscalll 049
    mc"Hey Harry, what's up?"
    #the MC answers his phone
    $ renpy.music.set_volume(1.0, 0.2, channel="ambient")
    show sc harrymisscalll 050
    ha"Hey dude."
    show sc harrymisscalll 051
    ha"I don't suppose you could come in early for work?"
    $ renpy.music.set_volume(0.2, 0.0, channel="ambient")
    show sc harrymisscalll 052
    mc"Uh, sure. Any reason why?"
    $ renpy.music.set_volume(1.0, 0.2, channel="ambient")
    show sc harrymisscalll 053
    ha"It will take too long to explain over the phone, but the quicker you get here the better."
    $ renpy.music.set_volume(0.2, 0.0, channel="ambient")
    show sc harrymisscalll 054
    mc"Okay, I'll get there as soon as possible."
    show sc harrymisscalll 055
    mc"Bye."
    #the call ends and the MC has a thinking face, wondering why Harry wants him to come to work
    #(screen goes blank)"
    stop ambient fadeout 1.0
    $ renpy.music.set_volume(1.0, 1.0, channel="ambient")
    scene black
    with dissolve
    scene black
    with Pause (2)
    jump lb_ep02_03_05_The_MC_is_confronted_by_his_gym_boss
