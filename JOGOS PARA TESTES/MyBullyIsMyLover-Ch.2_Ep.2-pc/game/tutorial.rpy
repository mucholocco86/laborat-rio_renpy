label tutorial:
    stop music fadeout 2
    scene ntuts1
    with dissolve
    $ renpy.pause()
    scene ntuts2
    with dissolve
    un "Hmm?"
    play music 'audio/GoodAndBad.mp3'
    scene ntuts3
    with dissolve
    un "Oh, a new player!"
    image ntutsss:
        "ntuts4.jpg"
        pause 3.0
        "ntuts5.jpg"
        pause .2
        repeat
    show ntutsss
    with dissolve
    un "Well, hey there, mate!"
    un "So, ya chose to give the game a go, hey?"
    un "Ain't that sweet of ya?"
    un "But quite a ripper choice I must say!"
    un "...Who am I and why am I talkin' like this?"
    n "First up, my name is Naomi. I'm different from the rest of the characters in this game, you see?"
    n "But I'll try and talk to ya more normal way now, 'kay?"
    n "...Why am I different, ya ask?"
    scene ntuts6
    with dissolve
    n "That's because I'm the developer of the game!"
    scene ntuts7
    with dissolve
    n "......"
    n "Hm? Ya think I'm kiddin'?"
    scene ntuts8
    with dissolve
    n "Well..."
    n "Yer right, mate. I'm sure not the developer of the game. Haha!"
    image ntutsss2:
        "ntuts9.jpg"
        pause 3.0
        "ntuts10.jpg"
        pause .2
        repeat
    show ntutsss2
    with dissolve
    n "But, NiiChan told me to talk to ya before ya dive down into the actual story and set yer expectations movin' forward."
    n "The game isn't that complicated, I'd say, it's fairly simple."
    n "Most of the choices in-game consists of just two options. There will be three or probably more, but that will rarely happen."
    n "If yer okay about playing a simple game and just want to enjoy the story, then good on ya~! Haha!"
    n "Ya might think this is an actual revenge game 'cuz of what the title suggests, but sorry to say that it is not."
    n "So if yer looking for revenge, this one is not for ya to play, mate. Ya might wanna close the game now."
    n "Also, this game has some anime vibe to it. It is subjective, but ya may find the stories cliche."
    n "That's how NiiChan wants it to be, so if yer not into these things, please refrain from movin' further into the game."
    n "One more thing for ya to know, is that this game is not yer typical all lovey-dovey kind of game. That'd be boring."
    n "There will be characters you'll hate at the start, but everything is there for a reason. Ya won't know how to love if ya dunno how to hate, right?"
    scene ntuts11
    with dissolve
    n "Okie-dokie~! My time is almost up!"
    scene ntuts12
    with dissolve
    n "Opps! Just before I go, a menu button will appear at the top right corner of the screen once yer into the actual game."
    n "You'll find tons of things in there, including game setting, love points for each character and a lot more."
    n "And hey, I totally recommend to try NiiChan's other game called 'Sicae'."
    n "Both games are hugely connected to each other and there is a lot of information here that might confuse ya later on, so I encourage ya to try it out."
    scene ntuts13
    with dissolve
    n "Alrighty then, let's get started! I'll see ya later~!"
    n "Catch'ya, mate!"

    scene black
    with Dissolve(2.0)
    jump ep1
