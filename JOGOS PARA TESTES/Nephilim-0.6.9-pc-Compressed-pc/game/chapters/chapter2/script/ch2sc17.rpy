#Start Chaper
label ch2sc17:

    #play music morning_1

    # start scene 2
        window hide dissolve
        play music home_1 fadein 2.0
        scene black with Dissolve (2.0)
        scene ch2sc17_01 with Dissolve(2.0)
        $ renpy.pause(1)
        mct "I didn’t see Gibs at the tavern last night. Maybe he doesn’t even live here anymore?"
        scene ch2sc17_02 with dissolve
        $ renpy.pause(0.5)
        mct "I wonder how he's doing?"
        mct "He was always a big softy on the inside... The thing with my parents though..."
        scene ch2sc17_03 with dissolve
        mct "That must have hit him hard."
        mct "He and papa were best friends ever since their youth, and he adored mama."
        scene ch2sc17_04 with dissolve
        mct "So often I've wanted to visit you and tell you everything Gibs."
        mct "I-I..."
        scene ch2sc17_05 with dissolve
        mct "Arhh! Whatever."
        mct "What's done is done, nobody can change the past..."
        scene black with Dissolve(1.5)
        $ renpy.pause(1)
        scene ch2sc17_06 with Dissolve(1.5)
        $ renpy.pause(0.5)
        scene ch2sc17_07 with dissolve
        mct "*Chuckles* His place still looks the same."
        scene ch2sc17_08 with dissolve
        mct "Here goes nothing."
        scene ch2sc17_09 with dissolve
        $ renpy.pause()
        scene ch2sc17_10 with dissolve
        mc "Hey Gibs! Are you here old man?"
        scene ch2sc17_09 with dissolve
        $ renpy.pause(0.5)
        scene ch2sc17_10 with dissolve
        $ renpy.pause(0.5)
        scene ch2sc17_09 with dissolve
        $ renpy.pause(0.5)
        scene ch2sc17_10 with dissolve
        $ renpy.pause(0.5)
        scene ch2sc17_11 with dissolve
        mct "Rats! I was hoping to speak to him before we left."
        scene ch2sc17_12 with dissolve
        mct "Since he isn’t here... hmm... I’ll go ask Clark if he knows anything."
        scene ch2sc17_13 with dissolve
        $ renpy.pause()
        scene ch2sc17_14 with dissolve
        $ renpy.pause()
        scene ch2sc17_15 with dissolve
        $ renpy.pause(0.5)
        gb "Huh?"
        gb "[mc]! It’s really you?"
        scene ch2sc17_17 with dissolve
        $ renpy.pause(1)
        scene ch2sc17_18 with dissolve
        mc "Hey, Old Bear."
        scene ch2sc17_19 with dissolve
        with vpunch
        gb "Come here, you little rascal!"
        scene ch2sc17_20 with dissolve
        mct "Oh no... brace for impact!"
        scene ch2sc17_21 with dissolve
        $ renpy.pause(0.5)
        gb "Haha! You're just going to stand there!? Give me a hug!"
        scene ch2sc17_22 with dissolve
        with vpunch
        $ renpy.pause(1)
        scene ch2sc17_23 with dissolve
        gb "That’s it! Hah-hah-hah!"
        gb "Give old Gibson a good squeeze!"
        scene ch2sc17_24 with dissolve
        mc "Hrrraahh!"
        mc "C-Cant brea... breathe."
        scene ch2sc17_23 with dissolve
        gb "I can’t believe you’re really here!"
        gb "I never believed for a second that you were dead! Your aunt Maya was right!"
        gb "That gorgeous aunt of yours made sure I never stopped believing... she was convinced you couldn't be dead!"
        scene ch2sc17_24 with dissolve
        mc "D-Definitely not dead. Hrhhh!"
        mc "But I will be if you don’t stop squeezing so tightly."
        scene ch2sc17_25 with dissolve
        gb "Oh! Sorry, sorry! *Chuckles* Heh-heh! I forget my own strength."
        scene ch2sc17_26 with dissolve
        mc "*Winded* You don’t say."
        mc "What in the five hells have you been eating?"
        scene ch2sc17_25 with dissolve
        gb "What can I say, working with steel at the forge all day gives a man strength!"
        scene ch2sc17_27 with dissolve
        mc "*Chuckles* It’s good to see you, Gibs... damn, my ribs."
        gb "Hah! They'll pop back into place soon enough! It's great to see you kid!"
        scene ch2sc17_28 with dissolve
        gb "Come, come! I want to hear everything!"

        if harem_path == True:
            gb "I bet a young lad like yourself have got quite the war-stories to tell!"
            gb "And by war-stories I mean, details about your female conquests!"
            scene ch2sc17_29 with dissolve
            gb "Come! I need to sit down, I bet you've already got yourself a harem, oh to be young again!"
            mct "What is it with everyone thinking I'm building a harem? I'm just enjoying myself..."

        else:
            gb "Join me inside, I'm sure we'll need to sit for this!"
            scene ch2sc17_29 with dissolve
            mc "*Sigh* ..."

        scene ch2sc17_30 with dissolve
        gb "Please, take a seat. We have a lot to catch up on."
        scene ch2sc17_31 with dissolve
        gb "So, ten whole summers, huh? Where do we even begin?"
        scene ch2sc17_33 with dissolve
        mc "I’ll just start from the night everything happened..."
        scene ch2sc17_33 with dissolve
        "You spend a few hours recapping the last ten years, and the recent events after Oren’s death and meeting Eliza."
        scene ch2sc17_34 with dissolve
        $ renpy.pause(1.5)
        scene ch2sc17_35 with dissolve
        $ renpy.pause(1.5)
        scene ch2sc17_33 with dissolve
        $ renpy.pause(1.5)
        scene ch2sc17_34 with dissolve
        $ renpy.pause(1.5)
        scene ch2sc17_35 with dissolve
        $ renpy.pause(1.5)
        scene ch2sc17_36 with dissolve
        gb "."
        gb ".."
        scene ch2sc17_37 with dissolve
        gb "Blazes, kid! You’ve been through one hell of a ride."
        scene ch2sc17_38 with dissolve
        gb "Being taken away by a stranger, right as Eric & Lily were killed..."
        scene ch2sc17_39 with dissolve
        gb "Spending several moons on the road, traveling to the far east."
        scene ch2sc17_40 with dissolve
        gb "Finding this hidden 'Nakajima village' in the middle of a dense tropical forest."
        scene ch2sc17_41 with dissolve
        gb "Meeting people from the Sen'ju region... I've never even met anyone from there."
        gb "Except from traveling merchants."
        scene ch2sc17_42 with dissolve
        gb "I remember, clear as day, how you'd always pester Eric, your father, about becoming an adventurer."
        scene ch2sc17_43 with dissolve
        gb "It seems adventure found you all on its own."
        scene ch2sc17_33 with dissolve
        mc "It’s only just starting."
        scene ch2sc17_38 with dissolve
        gb "You’re not staying?"
        gb "*Sighs* But... you're finally home, I thought..."
        scene ch2sc17_34 with dissolve
        mc "No... Eliza and I have a long journey ahead of us."
        mc "Lingering here in Riverside any longer won’t do me any good."
        scene ch2sc17_42 with dissolve
        gb "You’re a young man now, [mc]."
        gb "Part of that means making your own path in this world. You always went on and on about traveling..."
        scene ch2sc17_43 with dissolve
        gb "I guess that part became a reality at least."
        scene ch2sc17_39 with dissolve
        gb "I was hoping you'd be able to stay a while longer. It would be good to have you around."
        gb "*Quietly* {size=-10}{b}Not to mention, I'd love for you to meet Asta... I'm sure you'd be great friends...{/b}{/size}"
        scene ch2sc17_35 with dissolve
        mc "Sorry to disappoint, Gibs. There’s something I have to do..."
        mc "Something I can't achieve here in Riverside."
        scene ch2sc17_44 with dissolve
        gb "Heavens! You’re not seeking revenge are you?"
        scene ch2sc17_45 with dissolve
        with vpunch
        gb "Please tell me you aren't that bullheaded..."
        scene ch2sc17_46 with dissolve
        $ renpy.pause()
        scene ch2sc17_47 with dissolve
        mc "I have to. For them."
        scene ch2sc17_44 with dissolve
        gb "Kid... that’s the last thing they'd want."
        gb "Eric and Lily, they'd want you to be safe, to live your life."
        scene ch2sc17_47 with dissolve
        mc "It’s not about what they would have wanted, Gibs. I-I need this."
        scene ch2sc17_47 with dissolve
        mc "It’s the only thing that has kept me going all these years."
        mc "The only thing that has kept me from shattering into pieces..."
        scene ch2sc17_36 with dissolve
        $ renpy.pause()
        scene ch2sc17_39 with dissolve
        gb "I... I understand. I guess it'd be pointless to ask you to be careful, eh?"
        scene ch2sc17_50 with dissolve
        mc "Pretty much."
        scene ch2sc17_49 with dissolve
        gb "In that case, I’ll simply ask that you finish what you’ve set out to do."
        scene ch2sc17_45 with dissolve
        gb "Just don’t let it consume you... revenge can change a person. Make sure to surround yourself with good people."
        scene ch2sc17_49 with dissolve
        gb "People you can trust, people who will bring joy and light into your life."
        scene ch2sc17_50 with dissolve
        mc "I-I’ll try, Gibs."
        scene ch2sc17_45 with dissolve
        with vpunch
        gb "I swear by the Divines, kid. If this is the last time I see you, I’ll beat you to a pulp!"
        scene ch2sc17_53 with dissolve
        mc "*Chuckle* I’ll see you again someday, Old Bear."
        scene ch2sc17_51 with dissolve
        gb "Blazes... come here, Little Bear!"
        mc "No! No more hugs. I'm still recovering from earlier."
        scene ch2sc17_42 with dissolve
        gb "Next time I see you, then!"
        mc "Alright, alright."
        scene ch2sc17_54 with dissolve
        gb "And don’t underestimate whoever it is. Your father was a capable warrior."
        gb "He may have worked as a carpenter here in Riverside, but we both trained with sword and shield during our youth."
        gb "And your mother..."
        scene ch2sc17_55 with dissolve
        gb "Lily, she was one of the most powerful arcane sorceresses I’ve ever seen."
        gb "A renowned member of the Mage's guild."
        gb "Whoever could do that to them... has to be insanely powerful."
        scene ch2sc17_56 with dissolve
        mc "He's the one who should be afraid."
        scene ch2sc17_57 with dissolve
        gb "I don’t doubt it kid. Just..."
        scene ch2sc17_58 with dissolve
        gb "Just make sure you come back."
        scene ch2sc17_59 with dissolve
        mc "I will, Gibs."
        mc "I still want to hear all the stories you have about my parents... so you can be sure I’ll return."
        scene ch2sc17_60 with dissolve
        $ renpy.pause()
        scene ch2sc17_61 with dissolve
        gb "Farewell, Little Bear. May the divines light your path."
        gb "And don't do anything foolish!"
        scene ch2sc17_62 with dissolve
        mct "Goodbye old friend..."
        scene ch2sc17_63 with Dissolve(2)
        $ renpy.pause(1)
        scene ch2sc17_64 with dissolve
        gbt "They would be so proud of you."
        gbt "Eric... Lily... are you guys seeing this from the afterlife? Your little boy has become a man."
        gbt "*Sighs* I better head back inside, nails and hinges don't forge themselves."
        scene ch2sc10_200 with Dissolve(2)
        $ renpy.pause(1)
        astt "He's cute."
        astt "Little bear? Hmm?"
        astt "I wonder who he is? I haven't seen him around Riverside before..."
        scene ch2sc10_201 with Dissolve(1.5)
        $ renpy.pause(1)
        astt "He was speaking to daddy for quite a while..."
        astt "Do they know each other? But he's so young... he can't be much older than me? Maybe a year or two."
        astt "I'm turning 19 in two weeks, maybe... maybe daddy could invite him?"
        scene ch2sc10_202 with Dissolve(1.5)
        $ renpy.pause(1)
        astt "There's not been any cute boys in Riverside since I arrived from Luxenford..."
        astt "If he's friends with daddy, surely daddy would approve of him? *Giggles* I'm getting ahead of myself!"
        astt "I haven't even met him!"
        scene ch2sc10_203 with Dissolve(1.5)
        gb "*Calling out* Asta, sweetie? Are you nearby? I could use a bucket of water for dousing the steel."
        ast "*Shouts* Yes, I'll go fetch a fresh bucket daddy!"
        gb "That's my girl! Don't fill it too much, otherwise you won't be able to carry it."
        scene black with Dissolve(2)
        stop music fadeout 2.0
        jump ch2sc18
