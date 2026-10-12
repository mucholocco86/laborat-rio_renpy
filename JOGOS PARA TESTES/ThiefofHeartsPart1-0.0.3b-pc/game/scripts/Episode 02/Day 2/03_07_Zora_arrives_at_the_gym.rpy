init python:
    def image_sequence(base, image_list, pause_time):
        for img in image_list:
            renpy.show(base+" "+img)
            renpy.transition(dissolve)
            renpy.pause(pause_time)


init:
    image anim_ep02_zora_nc_shower_grinding1 = Movie(channel="anim_ep02_zora_nc_shower_grinding1", play="images/extras/Episode 02/anim_ep02_zora_nc_shower_grinding1.webm")
    image anim_ep02_zora_nc_shower_mast_close1 = Movie(channel="anim_ep02_zora_nc_shower_mast_close1", play="images/extras/Episode 02/anim_ep02_zora_nc_shower_mast_close1.webm")
    image anim_ep02_zora_nc_shower_mast1 = Movie(channel="anim_ep02_zora_nc_shower_mast1", play="images/extras/Episode 02/anim_ep02_zora_nc_shower_mast1.webm")
    image anim_ep02_zora_nc_shower_jerkoff1 = Movie(channel="anim_ep02_zora_nc_shower_jerkoff1", play="images/extras/Episode 02/anim_ep02_zora_nc_shower_jerkoff1.webm")
    image anim_ep02_zora_nc_shower_grinding_close1 = Movie(channel="anim_ep02_zora_nc_shower_grinding_close1", play="images/extras/Episode 02/anim_ep02_zora_nc_shower_grinding_close1.webm")
    image anim_ep02_zora_nc_shower_solo1 = Movie(channel="anim_ep02_zora_nc_shower_solo1", play="images/extras/Episode 02/anim_ep02_zora_nc_shower_solo1.webm")
    $ v_ep02_day2_zora_gym_family = False
    $ v_ep02_day2_zora_gym_boyfriend = False
    $ v_ep02_day2_zora_gym_work = False

    $ v_ep02_day2_gym_session_girls = "Zora"
    $ v_ep02_day2_hugging_zora_back = False
    $ v_ep02_03_07_fitness_session_with_zora_counter = 0

    $ v_ep01_zora_respect_counter = 0
    $ v_ep01_zora_cocky_counter = 0
    $ v_ep01_zora_arrogant_counter = 0
    $ v_ep02_zora_fantasy_counter = 0
    $ v_ep02_task10_zora_fitness_session = 0
    $ v_ep02_zora_aa_tasks_counter = 0

    image sc zoragym nc dick rub:
        "sc zoragym z220" with Dissolve(0.2, alpha=True)
        pause 0.8
        "sc zoragym z219" with Dissolve(0.2, alpha=True)
        pause 0.8
        repeat


label lb_ep02_03_07_Zora_arrives_at_the_gym:
    #SCENE BEGINS
    centered "A little while later...{w=2.0}{nw}" with dissolve
    show text "A little while later..."
    scene bg black with Dissolve(1)
    pause 1.0
    #This text with a back screen behind it
    #show the MC behind the counter, looking at the laptop screen
    play ambient "sound effects/01/gymnasium_ambience3.ogg" loop fadein 1.0
    scene sc zoragym z001
    with dissolve
    ha"So, did you find out who your first session is with?"
    #Harry walks towards where the MC is standing

    #These options come up on the screen - [Zora / Juliet]
    menu:
        "Zora":
            $ v_ep02_day2_gym_session_girls = "Zora"
            #START WITH THESE LINES IF THE PLAYER CHOOSES ZORA FIRST
            show sc zoragym z002
            mc"Yeah, that girl Zora is booked for the early session."
            show sc zoragym z003
            mc"She should be here any minute now."
            show sc zoragym z004
            mc"And I'll have an hour with Juliet after lunch."
            show sc zoragym z005
            ha"Sweet."
            ha"Would you like any help with either?"
            show sc zoragym z003
            mc"Nah, I'm sure I'll be able to handle both."
            show sc zoragym z009
            zora"Hello?"
            #The guys turn and see that Zora has entered the gym
            show sc zoragym z008
            mc"Hey Zora."
            show sc zoragym z005
            ha"Hello, m'lady."
            show sc zoragym z003
            mc"I'm sure you've already met Harry."
            show sc zoragym z013
            zora"Yeah, he helped me get signed up when I was here last."
            show sc zoragym z014
            ha"It was a pleasure to assist you."
            show sc zoragym z002
            mc"Don't you have somewhere to be, Harry?"
            show sc zoragym z001
            ha"Oh, right..."
            show sc zoragym z005
            ha"Well... You two crazy kids have fun."
            show sc zoragym z006
            ha"I'll just be over... here."
            #Harry points away from where they are
            show sc zoragym z011
            zora"Is he okay?"
            show sc zoragym z010
            mc"He's fine. He's just a few screws short of a complete toolbox, if you know what I mean?"
            show sc zoragym z014
            mc"But overall, Harry is harmless."
            mc"It's great to see you again."
            show sc zoragym z013
            zora"Yeah, you too."
            show sc zoragym z015
            mc"So anyway, head on over there to the changing rooms and when you're ready, I'll meet you by the exercise machines."
            show sc zoragym z009
            zora"All right, I'll see you soon..."
            #Zora smiles and then leaves
            #screen goes blank
            stop ambient fadeout 1.0
            scene black
            with dissolve
            scene black
            with Pause (2)
            jump lb_ep02_03_07_Zora_arrives_at_the_gym_1

        "Juliet":
            $ v_ep02_day2_gym_session_girls = "Juliet"
            #START WITH THESE LINES IF THE PLAYER CHOOSES JULIET FIRST
            show sc zoragym z002
            mc"Yeah, that girl Juliet is booked for the early session."
            show sc zoragym z003
            with dissolve
            mc"She should be here any minute now."
            show sc zoragym z004
            mc"And I'll have an hour with Zora after lunch."
            show sc zoragym z005
            ha"Sweet."
            ha"Would you like any help with either?"
            show sc zoragym z003
            mc"Nah, I'm sure I'll be able to handle both."
            show sc julietgym j002
            ju"Ahem?"
            #The guys turn to see that Juliet has entered the gym
            #Make sure she wears an outfit that covers most of her back
            show sc julietgym j004
            mc"Oh, hey Juliet."
            show sc zoragym z005
            ha"Hello, m'lady."
            show sc zoragym z003
            mc"You remember Harry, yeah?"
            show sc julietgym j003
            ju"How could I forget?"
            #Her response towards Harry is cold
            show sc zoragym z005
            ha"Welcome back to our wonderful establishment."
            show sc zoragym z002
            mc"Um... Don't you have somewhere to be, buddy?"
            show sc zoragym z001
            ha"Oh, right..."
            show sc zoragym z005
            ha"Well... You two crazy kids have fun."
            show sc zoragym z006
            ha"I'll just be over... here."
            #Harry points away from where they are.
            show sc julietgym j004
            mc"Sorry about that."
            mc"Harry's a few screws short of a complete toolbox, if you know what I mean?"
            show sc julietgym j001
            mc"But he means well."
            show sc julietgym j002
            ju"I'm sure he does."
            show sc zoragym z179
            mc"So... Are you all pumped and ready for our session?"
            show sc julietgym j003
            ju"As I'll ever be."
            #Juliet's demeanour is still plain - no smiling
            show sc julietgym j004
            mc"All right, well, after you've changed, I'll be over by the exercise machines."
            show sc julietgym j007
            with dissolve
            ju"Sure..."
            #Juliet gives the MC a blank stare and then leaves
            #screen goes blank
            stop ambient fadeout 1.0
            scene black
            with dissolve
            scene black
            with Pause (2)
            jump lb_ep02_03_08_The_MCs_private_session_with_Juliet




label lb_ep02_03_07_Zora_arrives_at_the_gym_1:

            #the scene returns with the MC looking over the weight machines
            play ambient "sound effects/01/gymnasium_ambience1.ogg" loop fadein 1.0
            show sc zoragym z016
            with dissolve
            zora"[y_name]?"
            $ task_addnew("Beginners workout session with Zora",10)
            #Zora calls the MC who turns his gaze towards her - https://pixhost.to/show/51/497065801_img_3482.png
            show sc zoragym z017
            mc"Oh, hey again."
            $ task_addfuturetask("",3,notify=False)
            #ROLLING WIP OF ZORA - https://pixhost.to/show/51/497065666_img_3454.jpg
            #Options here for the MC to react to Zora's choice of attire
            show sc zoragym z018
            mc"Nice outfit."
            $ zora_known = True
            $ persistent.zora_gallery_unlocked = True
            show sc zoragym z019
            zora"Thanks."
            show sc zoragym z020
            zora"Though I wasn't sure if it would be appropriate."
            show sc zoragym z021
            zora"It's not overly flattering."
            show sc zoragym z022
            mc"What do you mean?"
            show sc zoragym z021
            zora"I don't know..."
            show sc zoragym z020
            zora"I think maybe I should be wearing an exercise bra."
            zora"What do you think?"
            show sc zoragym z021
            zora"Do you think I look ridiculous in this?"
            #Possible options to add here

            show sc zoragym z022
            mc"Nonsense."
            show sc zoragym z023
            mc"You'll fit right in with just about any of our gym regulars."
            #Zora smiles
            show sc zoragym z025
            mc"Let's get you started over here."
            zora"Okay."
            #the MC and Zora stand in an unoccupied space on the floor, away from the machines
            show sc zoragym z026
            with dissolve
            mc"The main thing you want to do before you start is stretch."
            show sc zoragym z027
            mc"We'll begin by bending our knees slightly, so we can warm up the muscles in our legs."
            mc"Just copy me."
            show sc zoragym z030
            zora"Okay."
            #montage of the MC and Zora stretching their legs, knees and hips - but show images of Zora and her various body parts stretching
            play music "sound effects/02/Feel The Beat1.mp3" loop fadein 1.0
            $ image_sequence("sc zoragym", ["z032", "z033", "z034", "z035", "z036", "z037"], 1.5)

            pause 2.0
            show sc zoragym z029
            with dissolve
            mc"Very good, Zora. Now let's work on our arms and upper body."
            #a second montage of the MC and Zora stretching their upper body this time - but show images of Zora and her various body parts stretching

            $ image_sequence("sc zoragym", ["z038", "z040"], 1.5)

            show sc zoragym z041
            zora"Like this?"
            #And finally this pose - https://cdn.shopify.com/s/files/1/1647/4455/files/armstretch2.jpg?6539592647138061018 / https://d1s9j44aio5gjs.cloudfront.net/2016/07/Arm_Stretches_For_Warming_Up.jpg

            show sc zoragym z043
            mc"Yeah, perfect."
            show sc zoragym z039
            mc"So while we're stretching, tell me a bit about yourself."
            show sc zoragym z041
            zora"What would you like to know?"
            jump lb_ep02_03_07_Zora_arrives_at_the_gym_menu

            #[Family / Boyfriend / Work]
            #the player can choose these options in any order
            #the scene will continue once all three options have been played

label lb_ep02_03_07_Zora_arrives_at_the_gym_menu:

            if v_ep02_day2_zora_gym_family == True and v_ep02_day2_zora_gym_boyfriend == True and v_ep02_day2_zora_gym_work == True:
                jump lb_ep02_03_07_Zora_arrives_at_the_gym_continues
            menu:
                "Family" if v_ep02_day2_zora_gym_family == False:
                    $ v_ep02_day2_zora_gym_family = True
                    show sc zoragym z044
                    mc"What's your family like? Do you have any brothers or sisters?"
                    show sc zoragym z046
                    zora"Oh... Yeah, they're okay I guess."
                    zora"They're always busy with work, especially my Dad."
                    show sc zoragym z047
                    mc"What kind of work does he do?"
                    show sc zoragym z046
                    zora"He's the branch manager at Edge City Bank."
                    show sc zoragym z044
                    mc"Really?"
                    show sc zoragym z045
                    zora"You've heard of it?"
                    show sc zoragym z044
                    mc"I um... Yeah, I think I've seen an advertisement for it on TV."
                    mc"Their slogan is something like, {i}Where Your Money Feels at Home{/i}."
                    show sc zoragym z045
                    zora"That's the one."
                    show sc zoragym z046
                    zora"And no siblings. I'm an only child."
                    show sc zoragym z048
                    mc"Sorry to hear that."
                    show sc zoragym z049
                    zora"Don't be."
                    show sc zoragym z050
                    zora"Sometimes I prefer my own company."
                    show sc zoragym z051
                    mc"I hear that."
                    mc"So, your family is pretty well off then?"
                    show sc zoragym z049
                    zora"Well, our house is on Main Street."
                    show sc zoragym z051
                    if myloacl == "en_US":
                        mc"(If the city was a monopoly board then Zora and her parents own Park Place.)"
                    else:
                        mc"(If the city was a monopoly board then Zora and her parents own Mayfair.)"
                    show sc zoragym z050
                    zora"Any other questions?"
                    jump lb_ep02_03_07_Zora_arrives_at_the_gym_menu


                "Boyfriend" if v_ep02_day2_zora_gym_boyfriend == False:
                    $ v_ep02_day2_zora_gym_boyfriend = True
                    show sc zoragym z047
                    mc"Are you seeing anyone?"
                    show sc zoragym z046
                    zora"Seeing anyone?"
                    show sc zoragym z047
                    mc"Yeah, you know, \"dating\"? Putting yourself out there?"
                    show sc zoragym z046
                    zora"Oh, well, no... I'm not."
                    zora"Why do you ask?"
                    show sc zoragym z047
                    mc"It's a pretty normal question to ask, I think."
                    show sc zoragym z046
                    zora"Really?"
                    show sc zoragym z045
                    zora"So you wouldn't mind me asking you the same question?"
                    show sc zoragym z044
                    mc"Sure... Go for it."
                    show sc zoragym z045
                    zora"Well, are you?"
                    show sc zoragym z044
                    mc"Nope, I'm free as a bird."
                    show sc zoragym z049
                    zora"But you have your eye on someone, don't you?"
                    show sc zoragym z048
                    mc"Well, I'm a young man who works in a gym and who sometimes goes out to clubs and bars."
                    mc"So it's kind of hard not to."
                    show sc zoragym z050
                    zora"Do you also check out the girls when you're here at work?"
                    show sc zoragym z048
                    mc"Yeah, of course."
                    show sc zoragym z049
                    zora"Even girls that you have private sessions with?"
                    show sc zoragym z048
                    mc"Oh, sorry Zora, I didn't mean it to sound like that."
                    #Laughing Sound Effect
                    play sound "sound effects/01/sexy_female_laugh2.mp3" noloop
                    show sc zoragym z050
                    zora"Hahaha!"
                    zora"Don't worry, [y_name], I'm just messing with you."
                    show sc zoragym z051
                    mc"Damn..."
                    mc"I walked right into that one!"
                    #Zora smiles
                    show sc zoragym z050
                    zora"Is there anything else you would like to know?"
                    jump lb_ep02_03_07_Zora_arrives_at_the_gym_menu

                "Work" if v_ep02_day2_zora_gym_work == False:
                    $ v_ep02_day2_zora_gym_work = True
                    show sc zoragym z044
                    mc"Where do you work?"
                    show sc zoragym z046
                    zora"Oh, just at a quiet little cafe near home."
                    show sc zoragym z044
                    mc"Do you like it?"
                    show sc zoragym z046
                    zora"It's okay. I mean it's not my dream job but I'm just working there until I graduate from college."
                    show sc zoragym z044
                    mc"Oh yeah? What are you studying?"
                    show sc zoragym z045
                    zora"I'm six months away from getting my D.V.M. degree."
                    show sc zoragym z044
                    mc"D.V.M.?"
                    show sc zoragym z046
                    zora"My Doctor of Veterinary Medicine degree."
                    show sc zoragym z047
                    mc"Oh, so you're studying so you can become a vet."
                    show sc zoragym z049
                    zora"One day, I hope."
                    show sc zoragym z050
                    mc"That's pretty cool."
                    show sc zoragym z049
                    zora"If only my parents thought so."
                    zora"They wanted me to study law or to become what they believe is a \"real\" doctor."
                    show sc zoragym z048
                    mc"Well, I think it's great that you're doing what you want."
                    mc"You're choosing your own path."
                    show sc zoragym z051
                    mc"It's admirable."
                    show sc zoragym z050
                    zora"Thanks, [y_name]."
                    zora"Any other questions that you would like to ask me?"
                    jump lb_ep02_03_07_Zora_arrives_at_the_gym_menu


label lb_ep02_03_07_Zora_arrives_at_the_gym_continues:

            #scene continues
            show sc zoragym z051
            mc"No, that will do."
            show sc zoragym z048
            mc"Um... We should probably continue on with our session."
            show sc zoragym z052
            with dissolve
            mc"Now we're going to stretch the muscles in our back and hips."
            show sc zoragym z053
            mc"Here is the barbell that we are going to use."
            show sc zoragym z054
            mc"Don't worry, the plates aren't heavy, so you should be able to manage."
            show sc zoragym z056
            zora"What's the best way to do this?"
            show sc zoragym z059
            mc"Watch me..."
            show sc zoragym z060
            mc"Make sure to bend your knees slightly like we did with our stretches."
            #The MC gets into the correct position to lift the barbell
            show sc zoragym z061
            mc"Keep your back and legs straight when lifting..."
            #the MC reaches down to grab the barbell
            show sc zoragym z062
            mc"And keep your eyes faced forward when you come back up."
            show sc zoragym z063
            with dissolve
            pause 1.0
            #The MC looks forward when lifting the barbell above his head
            show sc zoragym z063a
            with dissolve
            pause 0.5
            mc"And voila!"
            #He bends back down and lowers the barbell to the floor
            show sc zoragym z059
            mc"Did you get all that?"
            show sc zoragym z057
            zora"Yeah, I think so."
            show sc zoragym z054
            mc"Okay, whenever you're ready."
            show sc zoragym z064
            with dissolve
            mc"And don't forget to breathe."
            #show a montage of Zora bending over and lifting the barbell - put small-sized round plates on each end

            $ image_sequence("sc zoragym", ["z065", "z066", "z069", "z070", "z071"], 1.5)

            #https://pixhost.to/show/51/497065587_248.jpg
            #Zora lifts the barbell above her head
            show sc zoragym z072
            with dissolve
            zora"How was that?"
            show sc zoragym z074
            mc"Y-yeah..."

            #[Good / Great / Outstanding]
            menu:
                "Good"(wt="Bonus image"):
                    show sc zoragym z074
                    mc"Very good, Zora."
                    show sc zoragym z076
                    mc"You're a natural."
                    show sc zoragym z075
                    zora"Thanks."
                    $ rewards_unlock ("zora",1)

                "Great"(wt="Best option + Task Point"):
                    show sc zoragym z074
                    mc"That was great, Zora."
                    $ v_ep02_task10_zora_fitness_session += 1
                    show sc zoragym z076
                    mc"You're a natural."
                    $ v_ep01_zora_respect_counter += 1
                    show sc zoragym z075
                    zora"Thanks." #+1 ZORA POINT
                    $ v_ep02_03_07_fitness_session_with_zora_counter += 1

                "Outstanding":
                    show sc zoragym z074
                    mc"That was outstanding, Zora."
                    show sc zoragym z073
                    zora"Oh, come on [y_name]."
                    show sc zoragym z072
                    zora"It wasn't that amazing."
                    $ v_ep01_zora_arrogant_counter += 1
                    show sc zoragym z074
                    mc"Maybe not, but I'm just trying to keep you motivated."
                    show sc zoragym z073
                    zora"I see..."


            #scene continues
            show sc zoragym z073
            zora"Can I ask you something before we continue?"
            #she holds the barbells down by her side
            show sc zoragym z074
            mc"Shoot."
            show sc zoragym z072
            zora"Aside from working here at the gym, what do you do in your spare time?"
            show sc zoragym z074
            mc"Oh.. What do you mean?"
            show sc zoragym z072
            zora"Do you go to college, do you have another job? Or do you take a knitting class?"
            show sc zoragym z080
            mc"First of all, I'm more of a crochet kind of guy."
            show sc zoragym z076
            mc"And when I'm not doing that, I mainly spend time around the house, or keeping fit."
            show sc zoragym z078
            mc"Or hanging out with Harry."
            show sc zoragym z075
            zora"Why do I get the feeling you're not telling me everything?"
            show sc zoragym z078
            mc"Well, just like a girl, even a guy gets to have his own secrets."
            show sc zoragym z075
            zora"Touché..."
            show sc zoragym z076
            mc"Let's move on..."
            show sc zoragym z081
            with dissolve
            mc"Now I want you to take the dumbbell weights and then we'll do two to three sets of around twelve to fifteen reps."
            show sc zoragym z082
            mc"Have you ever done this before?"
            show sc zoragym z083
            zora"Yeah, but not very well."
            show sc zoragym z085
            mc"Again, just follow my lead."
            #show the MC and Zora both living the dumbbells

            #Zora exercise #2 - lifting weights chest height then halfway above her head, then all the way above her head
            $ image_sequence("sc zoragym", ["z086", "z087", "z088", "z089"], 1.5)

            show sc zoragym z090
            with dissolve
            mc"Now you try."
            
            $ image_sequence("sc zoragym", ["z091", "z092", "z095", "z096", "z091", "z092", "z095"], 1.5)

            #https://pixhost.to/show/51/497065801_img_3482.png
            #Zora lifts the weight to around chest height like the image link above

            #https://pixhost.to/show/51/497065666_img_3454.jpg
            #Zora lifts the weight halfway above her head like the image link above

            #https://pixhost.to/show/51/497065670_img_3459.png

            #Zora lifts the weight all the way above her head like the image link above
            show sc zoragym z097
            with dissolve
            mc"Very good, Zora."
            show sc zoragym z098
            mc"How do your arms feel after that?"

            show sc zoragym z093
            zora"A little sore, especially my shoulders."

            #[The burn / Help her / Ice]
            menu:
                "The burn":
                    show sc zoragym z098
                    mc"That's normal."
                    show sc zoragym z097
                    mc"You've gotta feel the burn! You feel it so deep!"
                    show sc zoragym z096
                    mc"But you'll get used to it."
                    show sc zoragym z093
                    zora"Yeah, I guess."

                "Help her"(wt="Best option + Task Point"):
                    show sc zoragym z098
                    mc"Do you mind if I check something?"
                    show sc zoragym z083
                    zora"Oh, sure, go right ahead."
                    show sc zoragym z099
                    with dissolve
                    mc"Now don't be alarmed, I'm just going to put some pressure on your shoulder."
                    #the MC stands behind Zora and puts his hands on her shoulders
                    show sc zoragym z100
                    with dissolve
                    zora"Uhh..."
                    $ v_ep02_task10_zora_fitness_session += 1
                    #The MC presses his digits into her shoulders
                    show sc zoragym z102
                    mc"Does that feel better?"
                    show sc zoragym z105
                    zora"A little."
                    show sc zoragym z106
                    mc"We might need to use lighter weights."
                    $ v_ep01_zora_respect_counter += 1
                    show sc zoragym z107
                    mc"I don't want you to not be able to lift your arms by the time you leave here."
                    #+1 ZORA POINT
                    $ v_ep02_03_07_fitness_session_with_zora_counter += 1

                "Ice"(wt="Bonus image"):
                    show sc zoragym z098
                    mc"I'm just going to check something."
                    show sc zoragym z099
                    with dissolve
                    zora"Nghh..."
                    show sc zoragym z100
                    zora"That's a little painful whatever you're doing, [y_name]."
                    show sc zoragym z103
                    with dissolve
                    mc"Don't worry, you'll get used to it."
                    $ v_ep01_zora_cocky_counter += 1
                    show sc zoragym z099
                    mc"If the pain persists when you get home, I recommend putting some ice on it for ten to fifteen minutes."
                    show sc zoragym z100
                    zora"Oh, okay."
                    $ rewards_unlock ("zora",2)


            show sc zoragym z090
            with dissolve
            mc"How about we try something else."
            show sc zoragym z119
            with dissolve
            mc"This time, hold the dumbbells down by your side, and move up onto the step and then back down again."
            show sc zoragym z120
            mc"Do you think you can manage that?"
            show sc zoragym z084
            zora"Sure, I got this."
            #Zora exercise #3 - step and lifting weights
            $ image_sequence("sc zoragym", ["z108", "z109", "z110", "z111", "z112a", "z111", "z112", "z113", "z108", "z109", "z110", "z112a", "z113", "z112"], 1.5)
            
            stop music fadeout 1.0
            #screen goes blank
            scene black
            with dissolve
            scene black
            with Pause (2)


            play music "sound effects/02/Punch The Sky.mp3" loop fadein 1.0
            show sc zoragym z114
            with dissolve
            zora"Wow... I think I'm starting to get a sweat on."
            #Show a couple of beads of sweat dripping down from Zora's forehead
            #[Nothing / Fitness / Good ]
            menu:
                "Nothing":
                    show sc zoragym z115
                    mc"That's nothing."
                    mc"We've barely scratched the surface."
                    show sc zoragym z116
                    zora"Um, okay..."
                    show sc zoragym z115
                    zora"(That was a little rude of him.)"
                    $ v_ep01_zora_arrogant_counter += 1
                    mc"All right, let's try something different."
                    mc"Come with me..."
                    #screen goes blank
                    stop ambient fadeout 1.0
                    scene black
                    with dissolve
                    scene black
                    with Pause (2)


                "Fitness":
                    show sc zoragym z116
                    zora"Is that a good thing?"
                    show sc zoragym z115
                    mc"People who are very fit sweat more than those who aren't."
                    show sc zoragym z111
                    mc"However, if fit people like myself and less-fit people like you are performing the same task..."
                    mc"Then you would be the one to sweat more because you have to expend more energy to perform the same task."
                    show sc zoragym z112
                    mc"Does that make sense?"
                    show sc zoragym z116
                    zora"Oh, I guess so..."
                    show sc zoragym z115
                    zora"(Was that his way of calling me fat?)"
                    $ v_ep01_zora_cocky_counter += 1
                    mc"All right, let's try something different."
                    mc"Come with me..."
                    stop ambient fadeout 1.0
                    scene black
                    with dissolve
                    scene black
                    with Pause (2)

                "Good"(wt="Best option + Task Point"):
                    show sc zoragym z115
                    mc"That was very good, Zora."
                    show sc zoragym z116
                    zora"How so?"
                    show sc zoragym z112
                    mc"Sweating simply means that your basal metabolic rate is higher, and you are exerting enough energy to make your muscles work harder."
                    show sc zoragym z113
                    mc"Which is ideally what we want."
                    show sc zoragym z116
                    mc"Great job!" #+1 ZORA POINT
                    $ v_ep02_03_07_fitness_session_with_zora_counter += 1
                    show sc zoragym z117
                    zora"Thanks!"
                    $ v_ep01_zora_respect_counter += 1
                    #Zora smiles
                    mc"All right, let's try something different."
                    $ v_ep02_task10_zora_fitness_session += 1
                    mc"Come with me..."
                    stop ambient fadeout 1.0
                    scene black
                    with dissolve
                    scene black
                    with Pause (2)

            play ambient "sound effects/01/gymnasium_ambience2.ogg" loop fadein 0.2
            #the scene returns with the MC and Zora. Zora sits on this LAT pull-down bar machine  - https://pixhost.to/show/51/497066152_img_e4836.jpg
            show sc zoragym z123
            with dissolve
            zora"So I just pull the bar down as far as I can go, right?"
            show sc zoragym z119
            mc"Yes, but don't overdo it."
            show sc zoragym z118
            mc"Just work at a slow pace when pulling downward, and keep your grip tight when you're releasing the weight."
            show sc zoragym z124
            mc"I've locked the plates in at a weight that is manageable."
            mc"Keep going until I tell you to stop."
            show sc zoragym z119
            mc"Okay?"
            show sc zoragym z121
            zora"Sure, I think I'll be fine."

            $ image_sequence("sc zoragym", ["z126","z126a","z126","z125","z126","z126a","z126","z127","z128","z125","z126","z126a","z126","z125","z126","z126a"], 1.5)
#            #Montage of images showing Zora using the LAT bar machine - show her from different angles, including a nice cleavage shot

            scene black
            with dissolve
            scene black
            with Pause (2)
            show sc zoragym z120
            mc"And that should do it."
            #Zora releases the bar so the weights clank as they drop to the bottom

            #She looks even sweatier now. Her nipples show through her exercise top.
            show sc zoragym z121
            zora"Oh my..."
            zora"That was tougher than I was expecting."
            show sc zoragym z123
            zora"How am I doing so far?"

            #[Exceptional / Not bad/ Fitness]
            menu:
                "Exceptional"(wt="Best option + Task Point"):
                    show sc zoragym z129
                    mc"You've been exceptional, Zora."
                    $ v_ep02_task10_zora_fitness_session += 1
                    show sc zoragym z124
                    mc"I know you might be tired and you probably can't wait to get out of here, but at least you've made the first step."
                    show sc zoragym z122
                    mc"Just like you said you wanted to when we first met."
                    show sc zoragym z121
                    zora"You remembered!"
                    $ v_ep01_zora_respect_counter += 1
                    #She's happy and smiling
                    show sc zoragym z122
                    mc"When you talk, I listen." #+1 ZORA POINT
                    $ v_ep02_03_07_fitness_session_with_zora_counter += 1


                "Not bad"(wt="Bonus image"):
                    show sc zoragym z122
                    mc"Not bad for a first session, Zora."
                    show sc zoragym z124
                    mc"But of course, they'll only get more difficult the more that we have together."
                    mc"Do you think you'll be up for it?"
                    $ rewards_unlock ("zora",3)
                    show sc zoragym z121
                    zora"Yeah, I definitely want to come back and learn more from you."
                    show sc zoragym z122
                    mc"That's what I like to hear!"

                "Finish":
                    show sc zoragym z124
                    mc"Well, we're not quite finished yet."
                    mc"Perhaps it's best to ask once our session has concluded."
                    show sc zoragym z123
                    zora"Oh, okay..."
                    show sc zoragym z118
                    mc"All right, one last exercise before we wrap things up."
            stop music fadeout 1.0
            stop ambient fadeout 1.0
            #screen goes blank
            scene black
            with dissolve
            scene black
            with Pause (2)

            play ambient "sound effects/01/gymnasium_ambience2.ogg" loop fadein 1.0
            #Show the MC and Zora standing near the soft-matted area - like this https://pixhost.to/show/51/497065595_382195695_844665927314539_4682325040903072739_n.jpg
            show sc zoragym z137
            with dissolve
            zora"What do you want me to do?"
            show sc zoragym z135
            mc"We're just going to wind things down with some basic stretches."
            mc"Allow me to demonstrate."
            #The MC gets on his hands and knees while Zora watches him
            show sc zoragym z141
            mc"So start with your legs together, your hands pressed to the mat and placed slightly outside where your shoulders are."
            show sc zoragym z143
            mc"Then keep your head up, make sure your back is straight, and hoist your backside up slightly."
            show sc zoragym z144
            zora"Oh... Seriously?"
            show sc zoragym z146
            mc"Yeah... Go for it!"
            mc"And when you're ready, try lifting your back leg up in the air, as it will work your thigh muscles."
            mc"And make sure to hold it there for a few seconds and then change to your other leg."
            show sc zoragym z145
            zora"Oh... kay..."
            #Zora exercise #5 - on all fours, stretching

            play music "sound effects/02/Push Through The Pain.mp3" loop fadein 1.0
            $ image_sequence("sc zoragym", ["z147","z148","z149","z150","z149","z150","z149","z150"], 1.5)            

            show sc zoragym z145
            with dissolve
            zora"How was that?"
            #https://pixhost.to/show/51/497065595_382195695_844665927314539_4682325040903072739_n.jpg
            show sc zoragym z146
            mc"Perfect!"
            show sc zoragym z147
            mc"Keep going."
            show sc zoragym z148
            zora"All right..."
            #https://pixhost.to/show/51/497065593_380726996_844665953981203_10631733350338771_n.jpg
            #zora then changes legs - show some hot angles of her ass from behind
            #Change the standing point of the MC when you change the images of Zora
            #You don't have to show all of the MC in the same shot, you can just show his feet or half his body to show he's moving around while she's stretching

            #montage of Zora stretching, changing legs - show images of her legs up, and then both on the matt again

            #https://pixhost.to/show/51/497065649_ariel_winter_instagram_zq6s7hta-sized.jpg
            #https://pixhost.to/show/51/497065639_ariel_winter_instagram_7kqyx1oq-sized.jpg

            #https://pixhost.to/show/51/497065967_img_4302.jpg
            #https://pixhost.to/show/51/497065948_img_4301.jpg

            #https://pixhost.to/show/51/497065987_img_4303.jpg
            #https://pixhost.to/show/51/497066005_img_4305.jpg

            #[Check out her ass / Glance at her tits / Help her]

            menu:
                "Check out her ass"(wt="Bonus image"):
                    show sc zoragym z152
                    with dissolve
                    pause 1.0
                    mc"(She may think she's unfit, but she has one hell of an ass on her!)"
                    $ v_ep01_zora_cocky_counter += 1
                    show sc zoragym z153
                    with dissolve
                    pause 1.0
                    #show Zora's ass while she's on all fours and the MC standing behind her
                    show sc zoragym z156
                    with dissolve
                    mc"Let me adjust your posture here."
                    show sc zoragym z157
                    zora"Um... Okay."
                    show sc zoragym z158
                    zora"(Hmm... Was he just checking out my butt?)"
                    $ rewards_unlock ("zora",4)
                    #Show Zora's face with the MC standing behind her
                    show sc zoragym z161
                    zora"(If so, that's not very professional.)"
                    #she looks concerned
                    show sc zoragym z156
                    mc"All right, you should be all set to go again."
                    show sc zoragym z152
                    with dissolve
                    pause 1.0
                    show sc zoragym z153
                    with dissolve
                    pause 1.0
                    stop ambient fadeout 1.0
                    stop music fadeout 1.0
                    scene black
                    with dissolve
                    scene black
                    with Pause (2)

                "Glance at her tits":
                    show sc zoragym z154
                    mc"(From this angle, it's impossible for me to not take a look at those delicious titties hanging down.)"
                    $ v_ep01_zora_arrogant_counter += 1
                    #show Zora's hanging cleavage while she's on all fours and the MC is standing in front of her
                    show sc zoragym z156
                    mc"Let me just fix your posture here."
                    show sc zoragym z157
                    zora"Um... Okay."
                    show sc zoragym z158
                    zora"(Hmm... Was he just looking at my chest?)"
                    #Show Zora's face looking up at the MC as he looks away
                    show sc zoragym z161
                    zora"(If so, that's not very professional.)"
                    #she looks concerned
                    show sc zoragym z156
                    mc"All right, you should be all set to go again."
                    show sc zoragym z154
                    with dissolve
                    pause 1.0
                    stop ambient fadeout 1.0
                    stop music fadeout 1.0
                    scene black
                    with dissolve
                    scene black
                    with Pause (2)

                "Help her"(wt="Best option + Task Point"):
                    show sc zoragym z155
                    mc"Wait, don't move."
                    #Zora continues to stretch
                    #the MC kneels next to her
                    show sc zoragym z156
                    mc"Okay, just keep still."
                    show sc zoragym z157
                    zora"Oh..."
                    #the MC places a hand on her lower back
                    show sc zoragym z159
                    zora"What are you doing that for?"
                    show sc zoragym z158
                    mc"To stop you from raising your back too high. It needs to be down."
                    show sc zoragym z161
                    mc"Focus on extending your hips, and thrusting them towards the floor."
                    #Zora continues to stretch
                    show sc zoragym z160
                    zora"Like this?"
                    #zora shifts her stomach down and her ass up
                    show sc zoragym z157
                    mc"I um... Yeah, perfect." #+1 ZORA POINT
                    $ v_ep02_03_07_fitness_session_with_zora_counter += 1
                    #the MC is momentarily distracted when he notices Zora's ass as it lifts up
                    show sc zoragym z156
                    mc"All right, you should be all set to go again."
                    $ v_ep02_task10_zora_fitness_session += 1
                    show sc zoragym z151
                    with dissolve
                    pause 1.0
                    show sc zoragym z152
                    with dissolve
                    pause 1.0
                    show sc zoragym z153
                    with dissolve
                    pause 1.0
                    show sc zoragym z154
                    with dissolve
                    pause 1.0
                    #screen goes blank
                    stop ambient fadeout 1.0
                    stop music fadeout 1.0
                    scene black
                    with dissolve
                    scene black
                    with Pause (2)

            play ambient "sound effects/01/gymnasium_ambience3.ogg" loop fadein 0.2
            show sc zoragym z162
            with dissolve
            #https://pixhost.to/show/51/497066014_img_4307.jpg
            #https://pixhost.to/show/51/497066036_img_4310.jpg
            mc"And now you can relax..."
            #show the MC looking down at Zora as she continues to stretch while on all fours
            show sc zoragym z166
            zora"Oh, thank God... I'm so exhausted."
            #Zora falls and rolls over onto her back, looking up at the MC
            show sc zoragym z165
            with dissolve
            mc"How do you feel aside from that?"
            mc"Do you feel good about training with me?"
            show sc zoragym z162
            mc"Do you regret coming here?"
            show sc zoragym z164
            zora"Oh no, not at all."
            #Zora sits up as she responds to the MC
            show sc zoragym z171
            with dissolve
            zora"It was tough at times, like I expected it to be..."
            #She now stands
            show sc zoragym z169
            zora"But in no way do I regret coming here."
            show sc zoragym z167
            zora"You're a good trainer, [y_name]."
            zora"Thank you for being my teacher."
            show sc zoragym z173
            mc"Oh!"
            #Zora shocks the MC by hugging him

            #[Stay professional / Hug her back]
            menu:
                "Stay professional":
                    #This will be the automatic option if the player has 3 Zora Points or LESS
                    #The Player can still choose this option if they have more than 3 Zora Points
                    show sc zoragym z170
                    mc"You're welcome, Zora."
                    #the MC breaks the hug and responds
                    show sc zoragym z171
                    zora"Oh, I'm sorry."
                    zora"I didn't mean to invade your personal space."
                    show sc zoragym z170
                    mc"Nah, that's okay."
                    mc"I just don't want any of the other clients in the gym thinking that I'm playing favorites."
                    show sc zoragym z167
                    play sound "sound effects/01/sexy_female_laugh1.mp3"
                    zora"Haha!"
                    stop sound fadeout 1.0
                    ##laughing sound effect
                    zora"No problem at all."
                    show sc zoragym z169
                    zora"Anyway, I'm as sweaty as a pig so if our session is done, I'm gonna have a shower if that's okay?"
                    show sc zoragym z172
                    mc"No, please, don't mind me."
                    show sc zoragym z168
                    mc"I'll be at the front counter when you're done."
                    mc"I'll also need you to sign out before you leave."
                    show sc zoragym z167
                    zora"Okay, I'll see you there shortly..."
                    stop ambient fadeout 1.0
                    #Zora smiles at the MC then leaves
                    #screen goes blank
                    scene black
                    with dissolve
                    scene black
                    with Pause (2)

                    #scene returns with the MC looking at Zora while she prepares to leave
                    play ambient "sound effects/01/gymnasium_ambience1.ogg" loop fadein 1.0
                    show sc zoragym z011
                    with dissolve
                    zora"It looks like I'm all done."
                    show sc zoragym z012
                    zora"So, when are you free again?"
                    show sc zoragym z179
                    mc"I have some session times available later this week if you're available?"
                    show sc zoragym z013
                    zora"Yeah, I should be able to get here."
                    zora"I can book the session with you through the gym's website, can't I?"
                    show sc zoragym z014
                    mc"That's right."
                    mc"Just make sure to select me as your instructor."
                    show sc zoragym z009
                    zora"I will."
                    zora"And thanks again for training me."
                    show sc zoragym z179
                    mc"You're welcome."
                    show sc zoragym z008
                    mc"But just remember..."
                    mc"This is only the beginning."
                    show sc zoragym z013
                    zora"Bye [y_name]..."
                    #screen goes blank
                    stop ambient fadeout 1.0
                    scene black
                    with dissolve
                    scene black
                    with Pause (2)
                    #GO TO >
                    #"Juliet" (if the player has not had a session with Juliet yet)
                    #or
                    #"The MC finishes his shift" (if the player has done sessions with both girls)

                "Hug her back"(wt="Best option"):
                    $ v_ep02_day2_hugging_zora_back = True
                    #The Player will get this option if they have more than 3 Zora Points
                    show sc zoragym z174
                    mc"Hey, you're welcome."
                    zora"Mmm..."
                    #+1 ZORA HEART GAINED
                    $ v_ep02_03_07_fitness_session_with_zora_counter += 1
                    show sc zoragym z177
                    mc"It was a pleasure to train you, Zora."
                    show sc zoragym z176
                    zora"Yeah, but I'm sure you'd rather be training some fit, hottie instead, right?"
                    show sc zoragym z175
                    mc"Huh? What are you talking about?"
                    show sc zoragym z169
                    zora"Let's be honest, [y_name]."
                    show sc zoragym z171
                    zora"I know I'm fat and ugly. I've seen how guys look at me."
                    zora"They avoid me like the plague."
                    show sc zoragym z172
                    mc"All right... You listen to me, and listen good."
                    mc"You are not ugly, and you are not fat."
                    show sc zoragym z170
                    mc"Are you low on fitness and confidence? Probably."
                    mc"But that's why you're here, and why I'm going to help you."
                    show sc zoragym z172
                    mc"And even if you didn't want my help, I wouldn't look at you or treat you any differently to any other girl."
                    mc"Only stupid assholes do that."
                    show sc zoragym z168
                    mc"You're just as pretty as the rest of them."
                    mc"After being in your presence only a couple of times, this is what I believe."
                    show sc zoragym z174
                    zora"Oh, [y_name]."
                    #Zora hugs the MC again
                    show sc zoragym z176
                    zora"Thank you, you don't know what this means to me to hear you say that."
                    show sc zoragym z177
                    mc"You're welcome."
                    show sc zoragym z175
                    mc"And hopefully, we can do this again sometime soon."
                    show sc zoragym z167
                    zora"I'd like that very much."
                    #Zora steps back to face the MC when she speaks
                    show sc zoragym z169
                    zora"Anyway, I'm as sweaty as a pig so if our session is done, I'm gonna have a shower if that's okay?"
                    show sc zoragym z172
                    mc"No, please, don't mind me."
                    show sc zoragym z168
                    mc"I have a few things to attend to right now, but come and see me at the front counter when you're done."
                    show sc zoragym z170
                    mc"I'll need you to sign out before you leave."
                    show sc zoragym z167
                    zora"Okay, I'll see you there shortly..."
                    stop ambient fadeout 1.0
                    #Zora smiles at the MC then leaves
                    #screen goes blank
                    scene black
                    with dissolve
                    scene black
                    with Pause (2)

            stop sound fadeout 1.0

            #scene returns with the MC wondering around in the changing room areas - he's in between the men's and women's changing rooms
            if v_ep02_day2_hugging_zora_back == True:
                play ambient "sound effects/01/Shower_Sound_Effect_In_High_Quality.ogg" loop fadein 1.0
                play music "sound effects/01/Velvet Touch2.mp3" loop fadein 1.0
                show sc zoragym z180
                show screen scr_secret_icon("v_secrets_ep02_03_07_1") onlayer ontop
                with { "ontop": dissolve}
                mc"(I wonder if Harry is finished cleaning in here.)"
                #Sound of the shower running in the women's changing room
                show sc zoragym z181
                with dissolve
                mc"(Oh shit! Zora's still in here!)"

                #[Spy on her / Leave]
                menu:
                    "Spy on her"(wt="Best option"):
                        #the MC peeks his head around the corner, making sure he's not seen
                        show screen scr_secret_hotspot ("sc zoragym z182","1099, 279, 49, 96","v_secrets_ep02_03_07_1")
                        show sc zoragym z182
                        with dissolve
                        pause
                        #show the MC with his mouth open
                        #show a behind shot of Zora showering
                        #ROLLING SCREEN OF ZORA FROM BEHIND
                        hide screen scr_secret_hotspot
                        show sc zoragym z183
                        with dissolve
                        mc"Fuck me..."
                        mc"(She might be a little overweight, but that's not stopping me from getting wood!)"
                        #the MC grabs his crotch

                        #[Keep staring / Leave]
                        menu:
                            "Keep staring"(wt="Best option"):
                                show sc zoragym z184
                                with dissolve
                                pause
                                #Zora turns around and covers her vagina with one hand and a breast with the other - so we see one naked breast

                                #ROLLING SCREEN OF ZORA'S FRONT
                                show sc zoragym z185
                                with dissolve
                                mc"(Yep, there's definitely a lot of potential here.)"
                                show sc zoragym z181
                                with dissolve
                                mc"(I better get out of here before she sees me...)"
                                #show the MC leaving
                                #screen goes blank
                                stop music fadeout 2.0
                                stop ambient fadeout 2.0
                                scene black
                                with dissolve
                                scene black
                                with Pause (2)
                            "Leave":
                                show sc zoragym z181
                                with dissolve
                                mc"(I better get out of here before she sees me...)"
                                #show the MC leaving
                                #screen goes blank
                                stop music fadeout 2.0
                                stop ambient fadeout 2.0
                                scene black
                                with dissolve
                                scene black
                                with Pause (2)
                        hide screen scr_secret_icon onlayer ontop
                        with { "ontop": dissolve}

                        if persistent.v_secrets_enabled and persistent.v_secrets_ep02_03_07_1:
                            $ v_ep02_zora_fantasy_counter +=1
                            jump lb_ep02_03_07_zora_fantasy_scene
                        else:
                            jump lb_ep02_03_07_Zora_arrives_at_the_gym_final


                    "Leave":
                        show sc zoragym z181
                        with dissolve
                        mc"(I better get out of here before she sees me...)"
                        stop ambient fadeout 2.0
                        stop music fadeout 2.0
                        #show the MC leaving
                        #screen goes blank
                        scene black
                        with dissolve
                        scene black
                        with Pause (2)

            hide screen scr_secret_icon onlayer ontop
            with { "ontop": dissolve}
            jump lb_ep02_03_07_Zora_arrives_at_the_gym_final


label lb_ep02_03_07_Zora_arrives_at_the_gym_final:
            if v_ep02_day2_gym_session_girls == "Juliet":
                jump lb_ep02_03_08_The_MC_finishes_his_shift_at_the_gym
            else:
                #START WITH THESE LINES IF THE PLAYER CHOOSES JULIET SECOND
                #The scene returns with the MC standing behind the counter by himself
                centered "A little while later...{w=2.0}{nw}" with dissolve
                show text "A little while later..." #THESE LINES ARE NOT DUPLICATES. Needed to fade the text in and out!
                scene bg black with Dissolve(1)
                pause 1.0
                play ambient "sound effects/01/gymnasium_ambience1.ogg" loop fadein 1.0
                show sc julietgym j002
                with dissolve
                ju"Ahem?"
                #The MC turns to see that Juliet has entered the gym
                #Make sure she wears an outfit that covers most of her back
                show sc julietgym j004
                mc"Oh, hey Juliet."
                show sc julietgym j003
                ju"[y_name]."
                show sc zoragym z179
                mc"So... Are you all pumped and ready for our session?"
                show sc julietgym j002
                ju"As I'll ever be."
                #Juliet's demeanour is still plain - no smiling
                show sc julietgym j001
                mc"All right, well, after you've changed, I'll be over by the exercise machines."
                show sc julietgym j007
                with dissolve
                ju"Sure..."
                #Juliet gives the MC a blank stare and then leaves
                #screen goes blank
                stop ambient fadeout 1.0
                scene black
                with dissolve
                scene black
                with Pause (2)
                jump lb_ep02_03_08_The_MCs_private_session_with_Juliet



#START OF THE ZORA NON-CANON SCENE

label lb_ep02_03_07_zora_fantasy_scene:
            if not _in_replay:
                scene img_secret_scene_overlay onlayer anim_layer
                with { "anim_layer": dissolve}
            else:
                show screen scr_end_replay
            #show Zora back in the shower - show that it's a non-canon scene at the top of the screen
            #Shower sound effect
            play ambient "sound effects/01/Shower_Sound_Effect_In_High_Quality.ogg" loop fadein 1.0
            play music "sound effects/01/Midday_Mischief_with_Vivian.mp3" loop fadein 1.0
            show sc zoragym z189
            with dissolve
            zora"(Oh God, this is so naughty.)"
            show sc zoragym z188
            zora"(I really shouldn't be doing this...)"
            with fast_dissolve
            if not persistent.v_sex_anim_enabled_locked and persistent.v_sex_anim_enabled:
                scene anim_ep02_zora_nc_shower_solo1:
                    size (config.screen_width, config.screen_height)
            elif True:
                show sc zoragym z186
                with dissolve
                pause 1.0
            with flash(0.25, 0, 0.75, "#fff")
            zora"Mmm..."
            #Zora's hand moves down between her legs, touching her vagina
            #zora has her eyes closed
            $ image_sequence("sc zoragym", ["z187", "z188", "z189", "z190"], 1.5)
            show sc zoragym z191
            with dissolve
            mc"Room for one more?"
            #The MC calls from behind her
            show sc zoragym z192
            with dissolve
            zora"That'd be swell."
            #she looks over her shoulder and smiles as she replies
            #show the MC entering the shower while Zora continues to wash herself
            show sc zoragym z193
            mc"I don't think you washed yourself properly."
            show sc zoragym z194
            with dissolve
            mc"You still look a little sweaty."
            show sc zoragym z195
            with dissolve
            zora"Care to help me out with that?"
            show sc zoragym z212
            mc"It would be my pleasure."
            #Zora smiles
            #The MC steps in behind Zora, pressing his erection against her
            show sc zoragym z196
            zora"Oh yeah, those need cleaning."
            #the MC reaches around to cup and fondle her breasts in his hands
            show sc zoragym z213
            mc"Yeah, they're nice and dirty."
            #Animation of the MC playing with her breasts
            show sc zoragym z212
            mc"Allow me to give you a thorough rubdown."
            show sc zoragym z197
            with dissolve
            mc"Mmm..."
            #the MC kisses the side of her neck while she has her eyes closed and still smiling
            if not persistent.v_sex_anim_enabled_locked and persistent.v_sex_anim_enabled:
                scene anim_ep02_zora_nc_shower_grinding1:
                    size (config.screen_width, config.screen_height)
            elif True:
                show sc zoragym z198
            zora"Mmm..."
            if not persistent.v_sex_anim_enabled_locked and persistent.v_sex_anim_enabled:
                scene anim_ep02_zora_nc_shower_grinding_close1:
                    size (config.screen_width, config.screen_height)
            elif True:
                show sc zoragym z198
            zora"Ohh yes!"
            show sc zoragym z199
            mc"How are things now?"
            #show his cock between her ass cheeks
            show sc zoragym z206
            zora"Y-yeah... Much better."
            show sc zoragym z207
            mc"And what about down here?"
            #show the MC's hand between her legs, covering her pussy, the other still cups her breast
            show sc zoragym z211
            mc"Does this need some attention too?"
            #Zora places her hand on top of the MC's hand which is between her legs
            if not persistent.v_sex_anim_enabled_locked and persistent.v_sex_anim_enabled:
                scene anim_ep02_zora_nc_shower_mast_close1:
                    size (config.screen_width, config.screen_height)
            elif True:
                show sc zoragym z210
            zora"NGHH..."
            show sc zoragym z207
            zora"You probably shouldn't be doing that."
            if not persistent.v_sex_anim_enabled_locked and persistent.v_sex_anim_enabled:
                scene anim_ep02_zora_nc_shower_mast1:
                    size (config.screen_width, config.screen_height)
            elif True:
                show sc zoragym z223
            zora"You're my instructor, after all."
            zora"I wouldn't want you to lose your job over this."
            show sc zoragym z222
            zora"It could be dangerous."
            if not persistent.v_sex_anim_enabled_locked and persistent.v_sex_anim_enabled:
                scene anim_ep02_zora_nc_shower_jerkoff1:
                    size (config.screen_width, config.screen_height)
            elif True:
                show sc zoragym z224
            mc"You're right."
            show sc zoragym z218
            mc"I shouldn't be using my fingers to clean your pussy."
            show sc zoragym z219
            with vpunch
            mc"I'll use my dick instead."
            pause 1.0
            show  sc zoragym nc dick rub
            with dissolve
            pause 4.0
            show sc zoragym z221
            with dissolve
            pause 1.0
            #screen shakes as the MC places his cock between Zora's thighs so it rubs against her pussy
            show sc zoragym z226
            zora"OH GOD!!"
            #she exclaims
            #Animation of the MC thrusting his cock between her thighs and against her pussy
            show sc zoragym z227
            mc"You love it, don't you Zora?"
            show sc zoragym z223
            zora"Oh yes... It feels incredible."
            show sc zoragym z224
            mc"You want to feel me on the inside too, huh?"
            show sc zoragym z223
            zora"I um..."
            #she has her mouth slightly open, hesitant
            show sc zoragym z225
            zora"Mmm..."
            show sc zoragym z214
            mc"Well..."
            show sc zoragym z215
            mc"Allow me to teach you a new lesson..."
            #The MC grabs his cock and we see him move it towards her pussy from behind
            #IMPORTANT: Show this from a side angle, so we can't see the head of his cock pressing against the opening of her pussy.

            #a flash on the screen to show she was fantasising about the MC in the shower with her
            #show Zora's eyes shoot open
            show sc zoragym z203
            with flash(0.25, 0, 0.75, "#fff")
            with vpunch
            zora"OHHH!"
            if not persistent.v_sex_anim_enabled_locked and persistent.v_sex_anim_enabled:
                scene anim_ep02_zora_nc_shower_solo1:
                    size (config.screen_width, config.screen_height)
            elif True:
                show sc zoragym z204
            zora"Oh my, oh geez..."
            show sc zoragym z205
            with dissolve
            pause 1.0
            #Zora looks around, and realises that she had been masturbating in the women's gym locker room shower
            show sc zoragym z186
            with dissolve
            zora"(I gotta stop reading those erotic romance novels...)"
            scene onlayer anim_layer
            stop music fadeout 1.0
            stop ambient fadeout 1.0
            scene black
            with dissolve
            scene black
            with Pause (2)
            $ persistent.replay_ep02_zora_shower_fantasy = False
            $ renpy.end_replay()
            #The screen zooms out - Zora continues to wash herself as the screen fades out

            #END OF THE ZORA NON-CANON SCENE

            centered "A little while later...{w=2.0}{nw}" with dissolve
            show text "A little while later..." #THESE LINES ARE NOT DUPLICATES. Needed to fade the text in and out!
            scene bg black with Dissolve(1)
            pause 1.0
            play ambient "sound effects/01/gymnasium_ambience3.ogg" loop fadein 1.0
            #scene returns with the MC looking at Zora while she prepares to leave
            show sc zoragym z011
            with dissolve
            zora"Okay, looks like I'm all done."
            show sc zoragym z012
            zora"So, when are you free again?"
            show sc zoragym z179
            mc"I have some session times available later this week if you're available?"
            show sc zoragym z013
            zora"Yeah, I should be able to get here."
            zora"I can book the session with you through the gym's website, can't I?"
            show sc zoragym z014
            mc"That's right."
            mc"Just make sure to select me as your instructor."
            show sc zoragym z009
            zora"I will."

            if v_ep02_task10_zora_fitness_session == 5:
                $ task_completed(10,"aa")
                $ v_ep02_zora_aa_tasks_counter +=1
            if v_ep02_task10_zora_fitness_session == 4:
                $ task_completed(10,"a")
            if v_ep02_task10_zora_fitness_session == 3:
                $ task_completed(10,"b")
            if v_ep02_task10_zora_fitness_session == 2:
                $ task_completed(10,"c")
            if v_ep02_task10_zora_fitness_session <= 1:
                $ task_completed(10,"d")

            zora"And thanks again for training me."
            show sc zoragym z179
            mc"You're welcome."
            if v_ep02_03_07_fitness_session_with_zora_counter >= 5:
                $ zora_love_level +=1
            show sc zoragym z008
            mc"But just remember..."
            mc"This is only the beginning."
            show sc zoragym z013
            zora"Bye [y_name]..."
            #screen goes blank
            stop ambient fadeout 1.0
            scene black
            with dissolve
            scene black
            with Pause (2)
            jump lb_ep02_03_07_Zora_arrives_at_the_gym_final




