
label ch3sc1:

    window hide dissolve
    scene black with Dissolve (2.0)
    scene nephilim_ch3 with Dissolve(2.0)
    play music outdoors_3 fadein 1.0
    $ renpy.pause(2, hard=True)
    $ renpy.pause()
    scene black with Dissolve (2.0)
    $ renpy.pause(1.5)
    scene ss46 with Dissolve (2.0)
    $ renpy.pause()
    scene ch3sc01_001 with Dissolve(2.0)
    $ renpy.pause()
    scene ch3sc01_002 with dissolve
    $ renpy.pause()
    scene ch3sc01_003 with dissolve
    "As the two of you approach the city gates, a guard suddenly appears from behind the gate."
    scene ch3sc01_004 with dissolve
    gd "{b}Halt!{/b} State your business here."
    scene ch3sc01_005 with dissolve
    $ renpy.pause()
    scene ch3sc01_006 with dissolve
    mc "We’re here to join the Adventurers Guild."
    scene ch3sc01_004 with dissolve
    gd "City is off-limits at the moment unless you have a {b}city-pass{/b}."
    scene ch3sc01_007 with dissolve
    mct "Great... Just fucking great."
    mct "I’ll have to convince him to let us pass somehow."
    menu:
        "Attempt to persuade the guard. ({color=#87e1fa}Charisma{/color})" if True:
            scene ch3sc01_006 with dissolve
            "{size=+3}{b}Success!{/b}{/size} Your {color=#87e1fa}Charisma{/color} has increased by {size=+3}{b}{color=#2bff8b}1{/color}{/b}{/size}."
            $ charisma += 1
            mc "What’s your name?"
            scene ch3sc01_008 with dissolve
            gd "Milton."
            scene ch3sc01_009 with dissolve
            mc "Milton, we’ve been on the road for the better part of a week now, traveling here from Riverside."
            mc "We wish to become adventurers and help others."
            scene ch3sc01_010 with dissolve
            mc "Don’t turn us away."
            mc "If you would be so generous as to allow us entry, we would like to get a city-pass and head straight for the guild."
            mc "We have an important meeting with the guildmaster and if we're late he won't be pleased..."
            scene ch3sc01_006 with dissolve
            mc "So if you let us pass, we'll be happy to put in a good word for you with the guildmaster."
            scene ch3sc01_011 with dissolve
            ml "Hmm..."
            ml "Lord Dalen is a renowned knight and respected guildmaster, being in his good graces is nothing to sneeze at."
            scene ch3sc01_008 with dissolve
            ml "Alright sir."
            ml "But we’ll be keeping an eye on you. Make sure you register for a pass immediately."
            scene ch3sc01_009 with dissolve
            mc "Sure, that’s not a problem. Where can we get a city-pass?"
            scene ch3sc01_008 with dissolve
            ml "You’ll get a pass when you sign up with the guild."
            ml "All guilds have city-passes they hand out to their recruits."
            scene ch3sc01_012 with dissolve
            mc "Thank you, Milton."
            scene ch3sc01_013 with dissolve
            el "Thank you so much! I was afraid you'd turn us away..."
            el "You are a true guard, Milton!"
            scene ch3sc01_014 with dissolve
            ml "Oh, eh..."
            ml "Thank you, miss!"
            $ ml_intim = False
            ml "It's an honor to have you within our gates, I believe you'll make fine adventurers."
            scene ch3sc01_008 with dissolve
            ml "And don't forget to mention me to Lord Dalen!"
            scene ch3sc01_013 with dissolve
            el "You bet! We'll make sure to put in a good word for you!"
            scene black with Dissolve(2)
            jump ch3sc2

        "Attempt to intimidate the guard. ({color=#fc584c}Intimidation{/color})" if True:
            scene ch3sc01_007 with dissolve
            "{size=+3}{b}Success!{/b}{/size} Your {color=#fc584c}Intimidation{/color} has increased by {size=+3}{b}{color=#2bff8b}1{/color}{/b}{/size}."
            $ intimidation += 1
            scene ch3sc01_015 with dissolve
            mc "*Sigh* ..."
            scene ch3sc01_016 with dissolve
            mc "Listen here, guard. We’re here to see Dalen, the head of the Adventurers Guild."
            mc "He's awaiting our arrival and we’re already late."
            $ ml_intim = True
            scene ch3sc01_017 with dissolve
            mc "Do you want to tell him that you’re the reason we’re late for our meeting?"
            mc "Or should I do you that kindness?"
            scene ch3sc01_014 with dissolve
            gd "No, I-"
            scene ch3sc01_019 with dissolve
            mc "Then you'd better let us through. He’s not known for his patience."
            mc "I'd hate for you to lose your position as gateguard over this."
            scene ch3sc01_018 with dissolve
            $ renpy.pause()
            scene ch3sc01_014 with dissolve
            gd "R-Right away, sir! I’m sorry for any inconvenience."
            gd "Please see to it that you pick up the city-pass at the guild."
            scene ch3sc01_021 with dissolve
            mc "Will do."
            mc "Now why don't you run along? We don't need an escort."
            scene ch3sc01_020 with dissolve
            $ renpy.pause()
            scene ch3sc01_022 with dissolve
            el "*Whispers* {size=+3}{b}Heavens! Are you crazy?! What if he didn’t back down? We’d be knee deep in trouble!{/b}{/size}"
            scene ch3sc01_023 with dissolve
            mc "Sometimes you gotta live a little."
            scene ch3sc01_024 with dissolve
            el "*Relieved sigh* Hhaah... I’m just happy you pulled it off."
            stop music fadeout 2.0
            scene black with Dissolve(2)
            jump ch3sc2
