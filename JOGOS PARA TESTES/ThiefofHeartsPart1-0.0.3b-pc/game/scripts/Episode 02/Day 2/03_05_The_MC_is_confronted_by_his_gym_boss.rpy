label lb_ep02_03_05_The_MC_is_confronted_by_his_gym_boss:
    #SCENE BEGINS
    #show the MC arriving at work in his uniform and Harry is standing behind the counter
    play ambient "sound effects/01/gymnasium_ambience1.ogg" loop fadein 1.0
    scene sc gymboss g01
    with dissolve
    pause 1.0
    #gym ambience required here
    show sc gymboss g02
    with dissolve
    mc"Hey Harry."
    #MC gets to the counter where Harry is
    show sc gymboss g03
    ha"Hey man. Thanks for getting here so fast."
    #Harry responds enthusiastically
    show sc gymboss g06
    mc"So what was so important that it couldn't wait until my shift actually started?"
    #MC not impressed
    show sc gymboss g05
    ha"Yeah, um... You probably want to chat to the boss about that, buddy."
    #Harry is calm but concerned
    show sc gymboss g03
    ha"There was an incident here overnight that he wants to talk to you about."
    #Use a slightly different expression to the above
    show sc gymboss g02
    mc"Incident? What incident?"
    #the MC looks confused
    show sc gymboss g03
    ha"Like I said, he wants to talk to you, and he told me not saying anything else."
    #reuse a render from above
    show sc gymboss g04
    ha"He also told me to send you to his office as soon as you arrive."
    #reuse a render from above
    show sc gymboss g06
    mc"(Shit... What have I done now?)"
    #MC thinking and he looks concerned
    mc"All right, well, wish me luck."
    #He looks back up at Harry, worried
    show sc gymboss g05
    ha"Always, dude."
    #Show the MC walking away from Harry still looking worried
    show sc gymboss g08
    with dissolve
    pause 1.0
    show sc gymboss g09
    with dissolve
    pause 1.0
    $ renpy.music.set_volume(0.0, 1.0, channel="ambient")
    #screen goes blank
    scene black
    with dissolve
    scene black
    with Pause (2)



    #the scene returns with the MC knocking on his boss's office door
    $ renpy.music.set_volume(0.3, 1.0, channel="ambient")
    play music "sound effects/02/Airport Lounge.mp3" loop fadein 1.0
    show sc gymboss g10
    with dissolve
    mc"You wanted to see me, boss?"
    show sc gymboss g11
    boss"Yeah... Take a seat."
    #The boss has a laptop on his desk
    #the boss is a fit, gym freak type - make him like Ben Stiller in Dodgeball - https://pixhost.to/show/327/496625361_000.jpg
    #Discuss with Dots about the design and assets for the boss (Kasami)
    show sc gymboss g15
    mc"What's this all about? Why did I have to come in early?"
    #The MC sits on the other side of the desk, speaking to the boss
    show sc gymboss g14
    boss"We'll get to that shortly, [lastname]."
    #He leans forward, elbows on the table with his hands like this - https://pixhost.to/show/337/496707836_00.jpg
    #The Boss refers to the MC by his last name rather than his first - something he does with his staff
    show sc gymboss g16
    boss"First off, I need to know what you got up to after you finished your last shift."
    #the Boss sits back and looks composed
    show sc gymboss g26a
    mc"My last shift?"
    #show the Boss with his mouth closed, listening to the MC
    show sc gymboss g27
    mc"Um... I worked here with Harry until closing time."
    #reuse a render from above
    show sc gymboss g14
    boss"And after that?"
    #reuse a render from above
    show sc gymboss g15
    mc"We uh, we went to a club in town for a few drinks, Sir."
    #reuse a render from above
    show sc gymboss g18
    boss"I see."
    #the Boss thinks while speaking
    show sc gymboss g16
    boss"So you didn't go home or anywhere else?"
    #reuse a render from above
    show sc gymboss g27
    mc"No, we changed clothes here and then I didn't get home until the next morning."
    #reuse a render from above
    show sc gymboss g26a
    mc"Sorry, but I'm not really sure where you're going with this."
    #the MC looks confused as he replies to his boss
    show sc gymboss g13
    boss"I'm going to need to see your staff security pass, [lastname]."
    #The boss stands up and to the side of his desk
    show sc gymboss g27
    mc"My pass?"
    #reuse a render from above
    show sc gymboss g29
    mc"Oh, okay."
    #He takes his wallet out and goes through it
    show sc gymboss g31
    mc"Hmm..."
    #show the MC's open wallet
    show sc gymboss g15
    mc"Um... I don't have it."
    #reuse a render from above
    show sc gymboss g31
    mc"(Wait, this is my replacement wallet.)"
    #reuse a render from above
    show sc gymboss g30
    mc"(Oh, fuck!!)"
    #reuse a render from above
    show sc gymboss g28
    mc"(Those girls stole my security passkey as well!)"
    #the MC looks stunned, closed mouth
    show sc gymboss g18
    boss"Is there anything else you wanna mention?"
    #reuse a render from above
    show sc gymboss g16
    boss"The more you tell me, the better."
    #reuse a render from above
    show sc gymboss g27
    mc"Okay, but this wasn't my fault."
    #the MC replies while looking worried
    show sc gymboss g20
    mc"Harry and I met these girls at the club we went to the other night..."


    #These lines if the player slept with just Mikayla
    if v_ep01_09_01_Mikayla_Sex_path == True:
        mc"And by the morning, they robbed both of us blind."
        #reuse a render from above
        show sc gymboss g26a
        mc"They took our phones, wallets..."
        #reuse a render from above
        show sc gymboss g27
        mc"They even stole our clothes!!"
        #reuse a render from above
        show sc gymboss g18
        boss"Oh..."
        #reuse a render from above
        show sc gymboss g23
        with dissolve
        boss"So you both went home with uh..."
        #reuse a render from above
        show sc gymboss g26a
        mc"The girls?"
        #reuse a render from above
        show sc gymboss g23
        boss"Yeah..."
        #reuse a render from above
        show sc gymboss g26a
        mc"Yes, we did, boss."
        #reuse a render from above
        show sc gymboss g24
        boss"Nice work, [lastname]...."
        #The Boss has a satisfied grin on his face
        show sc gymboss g20
        mc"Thank you, boss."
        #reuse a render from above
        show sc gymboss g18
        boss"Err, anyway..."
        #His grin changes back to a serious look

    #These lines if the player slept with just Tasha
    if v_ep01_09_01_Tasha_Sex_path == True:
        mc"And by the morning, they robbed both of us blind."
        #reuse a render from above
        show sc gymboss g26a
        mc"They took our phones, wallets..."
        #reuse a render from above
        show sc gymboss g27
        mc"They even stole our clothes!!"
        #reuse a render from above
        show sc gymboss g18
        boss"Oh..."
        #reuse a render from above
        show sc gymboss g23
        with dissolve
        boss"So you both went home with uh..."
        #reuse a render from above

        show sc gymboss g26a
        mc"The girls?"
        #reuse a render from above
        show sc gymboss g23
        boss"Yeah..."
        #reuse a render from above
        show sc gymboss g26a
        mc"Yes, we did, boss."
        #reuse a render from above
        show sc gymboss g24
        boss"Nice work, [lastname]...."
        #The Boss has a satisfied grin on his face
        show sc gymboss g20
        mc"Thank you, boss."
        #reuse a render from above
        show sc gymboss g18
        boss"Err, anyway..."
        #His grin changes back to a serious look




    #These lines if the player slept with both Mikayla and Tasha (threesome path)"
    if v_ep01_09_01_Tasha_and_Mikayla_Sex_path == True:
        show sc gymboss g26a
        mc"And by the morning, they had robbed me blind."
        #reuse a render from above
        show sc gymboss g27
        mc"They took my phone, my wallet, and even my clothes!!"
        #reuse a render from above
        show sc gymboss g16
        boss"What about Harry? Where was he?"
        #reuse a render from above
        show sc gymboss g15
        mc"Um... He got pretty drunk and I had to send him home in a cab."
        #reuse a render from above
        show sc gymboss g23
        with dissolve
        boss"Oh... So you went home with uh..."
        #reuse a render from above
        show sc gymboss g26a
        mc"Both girls?"
        #reuse a render from above
        show sc gymboss g23
        boss"Yeah..."
        #reuse a render from above
        show sc gymboss g27
        mc"Yes, I did."
        #reuse a render from above
        show sc gymboss g24
        boss"Nice work [lastname]."
        #The Boss has a satisfied grin on his face
        show sc gymboss g20
        mc"Thank you, boss."
        #reuse a render from above
        show sc gymboss g18
        boss"Err, anyway..."
        #his grin changes back to a serious look


    #Scene continues
    show sc gymboss g14
    boss"The reason I called you in early is because we had a break-in overnight."
    #reuse a render from above
    show sc gymboss g16
    boss"Our security cameras picked up two people in disguise, cleaning out our main tills and fleeing out the back entrance of the gym."
    #reuse a render from above
    show sc gymboss g26a
    mc"Holy shit! Really?"
    #reuse a render from above
    show sc gymboss g18
    boss"Yeah... We can't confirm their identities but we know that they were two females."
    #reuse a render from above
    show sc gymboss g32
    boss"Here, see for yourself."
    #the boss spins his laptop towards the MC. It shows an image of the girls in disguise, robbing money from the cash till. They both have masks on to cover their faces
    #Maybe ask Dots or Mistress how to show CCTV footage to make this image look more authentic
    show sc gymboss g33
    pause 1.5
    with vpunch
    mc"(Son of a bitch...)"
    #the MC knows that the girls are Mikayla and Tasha and looks surprised
    show sc gymboss g34
    mc"(It's them!)"
    show sc gymboss g27
    mc"Well, just because we got robbed doesn't necessarily mean it happened {i}because{/i} I was robbed."
    show sc gymboss g16
    boss"True, but after what you just told me, it doesn't sound good either."
    #reuse a render from above
    show sc gymboss g19
    mc"(Oh crap... This just keeps getting worse.)"
    #reuse a render from above
    mc"So, does that mean that I'm fired?"
    #the MC looks worried
    show sc gymboss g21
    boss"Huh? No, not at all."
    #The Boss puts both of his hands up and looks relaxed
    show sc gymboss g18
    boss"You're one of my best workers, kid."
    #reuse a render from above
    show sc gymboss g15
    boss"This is just a case of extreme misfortune."
    #reuse a render from above
    show sc gymboss g14
    boss"I've already taken the liberty of updating all pass cards so the old ones are now useless."
    #reuse a render from above
    show sc gymboss g32
    boss"That way, those girls won't be able to break in again."
    #reuse a render from above
    show sc gymboss g16
    boss"Harry will issue you with a new pass."
    #reuse a render from above
    show sc gymboss g28
    mc"That's a relief."
    show sc gymboss g27
    mc"So are we good then?"
    #thd MC looks relieved
    show sc gymboss g18
    boss"Not exactly."
    #reuse a render from above
    show sc gymboss g16
    boss"My boss has been chewing my ass off about this."
    #reuse a render from above
    show sc gymboss g17
    boss"You can see that I don't have any bit of it left, don't you?"
    #the Boss turns to his side so we can see his ass, and he looks pissed off still
    show sc gymboss g15
    mc"Ah, yeah, sorry about that."
    #reuse a render from above
    show sc gymboss g14
    boss"Anyway, the money that was taken from the till needs to be made up."
    #reuse a render from above
    show sc gymboss g16
    boss"So I need you to work some overtime this week to cover the difference."
    #reuse a render from above
    show sc gymboss g18
    boss"Otherwise, I'm going to have to let you go."
    #reuse a render from above
    show sc gymboss g16
    boss"So what's it going to be?"
    #reuse a render from above
    show sc gymboss g19
    mc"(He knows this is my fault but he's also doing me a solid by not turning me in.)"
    #reuse a render from above
    mc"I'll work whatever hours you need me to, boss."
    #The MC replies to his boss in a confident way
    show sc gymboss g21
    boss"Very good."
    # The boss is happy
    show sc gymboss g24
    boss"Also, let McGuire know that I've made changes to next week's roster."
    show sc gymboss g20
    mc"Sure thing, I'll tell Harry when I see him."
    show sc gymboss g18
    boss"Don't let this happen again kid, because I won't be able to cover for you a second time."
    #reuse a render from above
    show sc gymboss g15
    mc"Thanks, Mister Stiller. I mean, boss."
    mc"I won't let you down again..."
    #reuse a render from above
    #the MC leaves his office
    #(screen goes blank)"
    stop music fadeout 1.0
    $ renpy.music.set_volume(0.0, 1.0, channel="ambient")
    stop ambient fadeout 1.0
    scene black
    with dissolve
    scene black
    with Pause (2)
    jump lb_ep02_03_06_The_MC_talks_with_Harry_at_the_gym
    #END SCENE

