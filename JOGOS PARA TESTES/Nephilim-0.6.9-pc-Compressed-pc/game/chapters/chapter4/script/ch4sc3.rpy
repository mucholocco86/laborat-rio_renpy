label ch4sc3:

    window hide dissolve
    play music home_2 fadein 1.0
    scene black with Dissolve (1.5)
    scene ch4sc3_001 with Dissolve(2)
    $ renpy.pause()
    mct "*Sigh* Who else could know what to do about Eliza’s condition?"
    mct "."
    mct ".."
    mct "..."
    scene ch4sc3_002 with dissolve
    mct "Magic! Of course! Sylph will know what to do."
    scene ch4sc3_003 with dissolve
    mct "She has to know something that can help Eliza!"
    stop music fadeout 2
    scene black with Dissolve(2)
    $ renpy.pause(1.3)
    scene ch4sc3_004 with Dissolve(2)
    play music forest_1 fadein 1.0
    sy "There was this big brute of an ogre and and and..."
    scene ch4sc3_005 with dissolve
    sy "The horrible ogre was just about to munch down on the innocent fae!"
    scene ch4sc3_004 with dissolve
    sy "But! Get this! A charming and dashing guy shows up, clad all in black!"
    scene ch4sc3_005 with dissolve
    sy "And so this guy-"
    scene ch4sc3_006 with dissolve
    da "[mc]."
    scene ch4sc3_007 with dissolve
    with vpunch
    sy "What?! No, not him-"
    scene ch4sc3_008 with dissolve
    sy "I mean, sure he is totally handsome and his heavenly blue eyes could charm even Princess Amelia!"
    sy "And sure, he happens to dress in all black ... Buuut!"
    scene ch4sc3_009 with dissolve
    sy "T-That is just a coincidence! Yes, a coincidence!"
    scene ch4sc3_006 with dissolve
    da "No, Sylph... [mc]’s here."
    scene ch4sc3_010 with dissolve
    $ renpy.pause()
    scene ch4sc3_011 with dissolve
    da "What’s wrong? You look pretty shaken."
    da "I'm sure you wouldn't be here at this hour if it weren't serious, you can tell us."
    scene ch4sc3_012 with dissolve
    $ renpy.pause(0.5)
    syt "Something's wrong!"
    syt "His eyes... they're red!"
    scene ch4sc3_013 with dissolve
    "Sylph rushes up from the counter, placing both of her tiny hands on your cheeks."
    sy "Heey... what's happened? Y-Your eyes... They’ve changed."
    sy "[mc]. Please, tell me. I'll help!"
    scene ch4sc3_014 with dissolve
    mc "I-I... Eliza, she’s..."
    scene ch4sc3_015 with dissolve
    sy "What happened? Is she okay?"
    sy "Please tell me? I'll do whatever I can."
    scene ch4sc3_014 with dissolve
    mc "She’s alive. *Sighs heavily* But-..."
    mc "Her legs... she's lost all feeling in her legs."
    scene ch4sc3_016 with dissolve
    with vpunch
    mc "It was him!"
    mc "He... he crippled her!"
    scene ch4sc3_017 with dissolve
    "Sylph feels your anger surfacing and she instinctively caresses your cheeks, her flowery scent surrounding you."
    scene ch4sc3_018 with dissolve
    da "Woah, woah... take a deep breath."
    da "Tell us exactly what happened."
    scene black with Dissolve(2)
    $ renpy.pause(0.5)
    scene ch4sc3_019 with Dissolve(2)
    "You spend the next hour recapping what happened this evening in vivid detail..."
    "Hoping that either of them might know something that could help."
    scene ch4sc3_020 with dissolve
    da "*Sigh* He didn’t intend to kill her, he was toying with you."
    da "Testing you."
    scene ch4sc3_021 with dissolve
    mc "What do you mean? How would you even know?"
    scene ch4sc3_020 with dissolve
    da "At first it was only a suspicion, but targeting you like this?"
    da "Now I know. I know exactly who’s after you... Taron."
    scene ch4sc3_021 with dissolve
    mc "Taron? This is the first I’ve heard of him."
    scene ch4sc3_020 with dissolve
    da "That's intentional. He usually has lackeys doing his bidding..."
    da "Trust me, [mc]. He's bad news. And if he'd wanted to kill Eliza, she'd already be dead."
    scene ch4sc3_022 with dissolve
    da "He would’ve specifically targeted her lower back to cripple her."
    da "To hurt you. To let you know that he’s in control."
    scene ch4sc3_023 with dissolve
    mc "Not even the divines themselves could stop me from doing what I intend to do to him."
    mc "Fuck... And you know him, Dalen?"
    ###Choice###
    menu:
        "Be inquisitive. ({color=#ffee54}Leadership{/color})":
            scene ch4sc3_021 with dissolve
            mc "Dalen, I need answers... you know what this man has done."
            mc "If you want me to trust you, then you need to be straight with me."
            mc "How do you know all this, Dalen? What's your connection to this 'Taron'?"
            scene ch4sc3_022 with dissolve
            da "*Sigh* He..."
            "Your attempt to convince Dalen to reveal information about Taron was a {b}success!{/b} {size=+3}{b}{color=#ffee54}Leadership{/color}{/b}{/size} has increased by {size=+3}{b}{color=#2bff8b}1{/color}{/b}{/size}."
            da "He, Oren, and I... we used to be friends."
            scene ch4sc3_023 with dissolve
            with vpunch
            mc "Friends?!"
            $ leadership += 1
            mc "What the hell, Dalen!"
            scene ch4sc3_020 with dissolve
            da "Emphasis on 'used to be.'"
            da "The three of us met when we were young."
            scene ch4sc3_022 with dissolve
            da "We were all training at the royal academy. Each of us easily surpassed the other students..."
            da "So our instructors decided to put us in a special unit."
            scene ch4sc3_024 with dissolve
            da "We quickly became known as 'Trinity' among the other cadets."
            da "An unbeatable trio who took out the king's worst offenders."
            scene ch4sc3_022 with dissolve
            da "But after we graduated we all drifted apart..."
            da "Oren married his sweetheart, Ellen and moved to Whitehills."
            da "I visited him once after Eliza was born. She was only two summers old at the time."
            da "Such a lively girl, though. She was running after Oren wherever he went..."
            scene ch4sc3_024 with dissolve
            da "As for Taron... He went to work as an elite mercenary directly under the command of the Knight-Commander."
            da "They usually took on the most dangerous and rewarding missions."
            scene ch4sc3_022 with dissolve
            da "Taron has mostly kept to himself, although I've seen him several times since we split from the academy."
            da "But each time I've encountered him, he's seemed less and less like the kid I graduated alongside."
            scene ch4sc3_020 with dissolve
            da "And I sought adventure. I wanted to see the world outside the capital walls."
            da "I spent several years traveling, until I finally had my fill of murky caves, rugged mountains and old ruins."
            da "Eventually, I decided to return to Luxenford to establish the adventurer’s guild here."
            scene ch4sc3_024 with dissolve
            da "As for what caused Taron to become... whatever he's become, I have no idea."
            da "He’s become cold and calculating. He ruthlessly manipulates people to his own ends. And he’s cunning."
            scene ch4sc3_022 with dissolve
            da "I’ve tried to catch him red-handed several times. But to no avail. He uses lackeys to do his bidding."
            scene ch4sc3_024 with dissolve
            da "He covers his tracks well."
            scene ch4sc3_023 with dissolve
            mc "This time he didn’t use lackeys. He assaulted Eliza himself."
            scene ch4sc3_021 with dissolve
            mc "*Sigh* We need to find a way to help Eliza."

        "Persuade him to tell you more. ({color=#2bff8b}Persuasion{/color})":
            scene ch4sc3_021 with dissolve
            mc "This is the man who... killed my parents... who has been chasing me and Oren..."
            mc "Please tell me Dalen, I need to know..."
            $ persuasion += 1
            mc "How do you know all this, Dalen? What's your connection to this 'Taron'?"
            scene ch4sc3_022 with dissolve
            da "*Sigh* He..."
            "Your attempt to persuade Dalen to give you information about Taron was {b}successful!{/b} {size=+3}{b}{color=#2bff8b}Persuasion{/color}{/b}{/size} has increased by {size=+3}{b}{color=#2bff8b}1{/color}{/b}{/size}."
            da "He, Oren, and I... we used to be friends."
            scene ch4sc3_023 with dissolve
            with vpunch
            mc "Friends?!"
            mc "What the hell, Dalen!"
            scene ch4sc3_020 with dissolve
            da "Emphasis on 'used to be.'"
            da "The three of us met when we were young."
            scene ch4sc3_022 with dissolve
            da "We were all training at the royal academy. Each of us easily surpassed the other students..."
            da "So our instructors decided to put us in a special unit."
            scene ch4sc3_024 with dissolve
            da "We quickly became known as 'Trinity' among the other cadets."
            da "An unbeatable trio who took out the king's worst offenders."
            scene ch4sc3_022 with dissolve
            da "But after we graduated we all drifted apart..."
            da "Oren married his sweetheart, Ellen and moved to Whitehills."
            da "I visited him once after Eliza was born. She was only two summers old at the time."
            da "Such a lively girl, though. She was running after Oren wherever he went..."
            scene ch4sc3_024 with dissolve
            da "As for Taron... He went to work as an elite mercenary directly under the command of the Knight-Commander."
            da "They usually took on the most dangerous and rewarding missions."
            scene ch4sc3_022 with dissolve
            da "Taron has mostly kept to himself, although I've seen him several times since we split from the academy."
            da "But each time I've encountered him, he's seemed less and less like the kid I graduated alongside."
            scene ch4sc3_020 with dissolve
            da "And I sought adventure. I wanted to see the world outside the capital walls."
            da "I spent several years traveling, until I finally had my fill of murky caves, rugged mountains and old ruins."
            da "Eventually, I decided to return to Luxenford to establish the adventurer’s guild here."
            scene ch4sc3_024 with dissolve
            da "As for what caused Taron to become... whatever he's become, I have no idea."
            da "He’s become cold and calculating. He ruthlessly manipulates people to his own ends. And he’s cunning."
            scene ch4sc3_022 with dissolve
            da "I’ve tried to catch him red-handed several times. But to no avail. He uses lackeys to do his bidding."
            scene ch4sc3_024 with dissolve
            da "He covers his tracks well."
            scene ch4sc3_023 with dissolve
            mc "This time he didn’t use lackeys. He assaulted Eliza himself."
            scene ch4sc3_021 with dissolve
            mc "*Sigh* We need to find a way to help Eliza."

        "Leave it be. (Neutral)":
            scene ch4sc3_021 with dissolve
            mc "You’ll have to tell me exactly how you know all this, Dalen..."
            mc "Another time..."
            mc "First, we have to cure Eliza."

    scene ch4sc3_025 with dissolve
    mc "Sylph, is there anything you can do to help Eliza?"
    mc "Any spell to make her walk again?"
    scene ch4sc3_026 with dissolve
    sy "."
    sy "..."
    "Sylph seems hesitant..."
    scene ch4sc3_027 with dissolve
    sy "I’m sorry, [mc]."
    sy "I’m not capable of performing any magic like that."
    scene ch4sc3_026 with dissolve
    sy "..."
    syt "I cannot provide what he asks... it's dark magic..."
    syt "Last time a fae performed dark magic... I-... I lost everything."
    syt "We need another solution... one that does not mean certain doom for everyone."
    scene ch4sc3_025 with dissolve
    mc "We have to do something!"
    mc "I-I can’t leave her like this."
    scene ch4sc3_023 with dissolve
    mc "This happened because this psycho wanted to get to me, she doesn’t deserve this!"
    scene ch4sc3_024 with dissolve
    da "Calm yourself, [mc]."
    da "I might know of a way to cure her."
    scene ch4sc3_020 with dissolve
    da "But... It'll be a large undertaking to even attempt it, let alone succeed."
    scene ch4sc3_023 with dissolve
    mc "Failure is not an option, Dalen."
    mc "I’ll do whatever it takes to cure her."
    scene ch4sc3_020 with dissolve
    da "*Sigh* I know you will."
    scene ch4sc3_024 with dissolve
    da "So, let me get straight to it."
    da "I once heard about an artifact said to be blessed by Lucid, one of the seven divines."
    scene ch4sc3_022 with dissolve
    da "It is supposed to have healing powers strong enough to even bring the dead back to life..."
    scene ch4sc3_021 with dissolve
    mc "T-The dead?"
    scene ch4sc3_028 with dissolve
    sy "Whau!! You’ve never told me about this!"
    scene ch4sc3_029 with dissolve
    da "For good reason. It’s only been a tale passed down from the higher ups at the academy... a legend."
    da "Nobody has actually seen it... nobody alive, at least."
    scene ch4sc3_030 with dissolve
    da "So, there’s no way to know for sure if it even exists."

    scene ch4sc3_031 with dissolve
    $ renpy.pause()
    ####Animation####
    show mc_closeup_1 with fade
    $ renpy.pause(2, hard=True)
    mct "Mama ... Papa ... I-"
    mct "I could see you again."
    mct "There’s so much I want to tell you... All the crazy shit I’ve been through since that night."
    mct "All the weird creatures I’ve encountered... all the different people, with their quirks and all."
    mct "Speaking of people, I met this girl... stubborn as a mule."
    mct "As beautiful as a fairy tale princess."
    mct "We’ve been through so much together in such a short amount of time. I can’t help but feel drawn to her."
    mct "She was thrown into this with me that night. Without either of us knowing it at the time..."
    mct "I want to make sure she has a good life... a happy life."
    scene ch4sc3_031 with dissolve
    mct "Her name is Eliza. She’s..."
    ###Choice###
    menu:
        "She’s my best friend.":
            scene ch4sc3_031 with dissolve
            mct "I’ve grown fond of her. It’s been... interesting having a friend again."
            mct "I can rely on her. But I let her down when she needed me the most."
            mct "Now she’s hurt and I have to fix it. I have to."
        "She’s my girl.":
            scene ch4sc3_031 with dissolve
            mct "I’ve never cared about anyone like I do for her. And she just got injured badly..."
            mct "But I’m going to fix it. And when I do... I’m going to take her on a date just like she's been talking about."


    scene ch4sc3_024 with dissolve
    da "I know what you’re thinking, [mc]. Don’t go down that rabbit hole. The artifact is rumored to be a chalice."
    da "The deceased would have to drink from it in order to be brought back to life."
    scene ch4sc3_020 with dissolve
    da "And I assume you don’t exactly have the bodies of your parents readily available?"
    scene ch4sc3_021 with dissolve
    mc "No... but..."
    scene ch4sc3_020 with dissolve
    da "We also don’t know the extent of the power the artifact holds."
    scene ch4sc3_022 with dissolve
    da "Does it even exist? If it does, is it single use? Would it work on the dead, or only the living?"
    scene ch4sc3_028 with dissolve
    sy "All valid questions... But I do believe it exists! All legends spring from somewhere, right?"
    scene ch4sc3_023 with dissolve
    mc "If this chalice is real, and it can cure Eliza, I have to find it. I need to."
    scene ch4sc3_025 with dissolve
    mc "Does either of you know its location?"
    scene ch4sc3_024 with dissolve
    da "I don’t know for certain, but it was rumored to have been lost on an island called... Isla de Inmortui."
    da "The Island of Undead, to be specific."
    scene ch4sc3_032 with dissolve
    with vpunch
    sy "Un-d-d-dead?! That doesn’t sound very welcoming..."
    sy "I-I don't think we should mess with something like that! It could be dangerous!"
    scene ch4sc3_023 with dissolve
    mc "It doesn’t matter, I will go."
    "As the words leave your mouth. Sylph grabs your face again."
    scene ch4sc3_015 with dissolve
    sy "No! You can’t seriously consider going to such a place?!"
    sy "Y-Y-You could get hurt! Or, Earth Mother forbid... even worse! You could die!"
    scene ch4sc3_013 with dissolve
    sy "Inmortui! Means undying! Seems like a good reason to stay far away."

    ###Choice###
    menu:
        "Reassure her. ({color=#87e1fa}Charisma{/color})":
            scene ch4sc3_014 with dissolve
            mc "Hey... don’t worry, Sylph."
            mc "Nothing will happen to me, I promise."
            scene ch4sc3_015 with dissolve
            sy "You can’t promise that!"
            sy "You can’t know for sure!"
            "She squeezes your cheeks firmly, not wanting to let go."
            scene ch4sc3_016 with dissolve
            mc "Yes I can. Eliza is hurt because of me..."
            scene ch4sc3_014 with dissolve
            mc "Sylph, you can sense magic, yeah?"
            scene ch4sc3_013 with dissolve
            sy "Uh-huh! uh-huh! I can! Why?"
            scene ch4sc3_016 with dissolve
            mc "Do it. Sense my magic."
            mc "It will tell you all you need to know."
            scene ch4sc3_017 with dissolve
            $ renpy.pause()
            scene ch4sc3_017b with dissolve
            "The warmth of her hands increases against your skin as she begins."
            scene ch4sc3_017c with dissolve
            "She stares intently into your eyes, as if she can see your magic through them."
            "You feel a slight tingling in your cheeks where her hands rest."
            "Her magic and your own meet for the first time. It's an odd sensation you haven't felt before."
            scene ch4sc3_017 with dissolve
            $ renpy.pause(0.5)
            sy "..."
            $ charisma += 1
            "Letting Sylph feel your magic, successfully managed to calm her, {b}{color=#87e1fa}Charisma{/color}{/b} has increased by {size=+3}{b}{color=#2bff8b}1{/color}{/b}{/size}."
            scene ch4sc3_015 with dissolve
            sy "*Sigh* You’re right... there’s no way you'll fail to bring her this cure."
            sy "I still don’t like it!"
            scene ch4sc3_014 with dissolve
            mc "How about this? When I get back... you can give me a proper scolding for not heeding your advice."
            scene ch4sc3_015 with dissolve
            sy "*Whispers* {size=-7}{b}I’ll settle for a biiiig hug... The biggest ever!{/b}{/size}"
            scene ch4sc3_014 with dissolve
            mc "*Whispers* {size=-7}{b}You’ve got a deal. One big-ass hug for Sylph upon my return.{/b}{/size}"
            scene ch4sc3_017 with dissolve
            "Sylph feels calm again, knowing what awaits her upon your return has relaxed her, her trust has increased by {size=+3}{b}{color=#2bff8b}3{/color}{/b}{/size}."
            $ sylph_trust += 3


        "Dismiss her concerns. ({color=#fc584c}Intimidation{/color})":
            scene ch4sc3_016 with dissolve
            mc "Sylph, back off."
            mc "Stop worrying about me. I can handle myself."
            mc "I’ve been up against worse odds and I’m still here. I couldn't care less if I had to venture into the five hells."
            mc "There’s no fucking way I'll die before killing the bastard that did this and finding a cure for Eliza."
            scene ch4sc3_015 with dissolve
            sy "*Shaky voice* [mc]-... I-..."
            $ intimidation += 1
            "Your directness in the matter successfully intimidated Sylph to back off. {b}{color=#fc584c}Intimidation{/color}{/b} has increased by {size=+3}{b}{color=#2bff8b}1{/color}{/b}{/size}."
            sy "*Sigh* Fine... have it your way."
            sy "But I don’t think it's a good idea!"
            $ sylph_trust -= 1
            "Sylph does not like that you dismissed her concerns, her trust has decreased by {size=+3}{b}{color=#f00}1{/color}{/b}{/size}."


    scene ch4sc3_018 with dissolve
    da "Nobody has ever set foot on that island and returned, hence the name."
    scene ch4sc3_023 with dissolve
    mc "I don’t care, Dalen."
    mc "I’m not afraid. If anything tries to stop me..."
    scene ch4sc3_020 with dissolve
    da "*Sigh* I know better than to try and stop you... she’s Oren’s daughter."
    da "I want her to be cured as well... I can't stand knowing Taron has harmed her like this."
    da "I'll pull some strings and arrange for passage on a ship."
    scene ch4sc3_024 with dissolve
    da "Come back here in the morning."
    da "We’ll plan your journey together."
    scene ch4sc3_021 with dissolve
    mc "Dalen... thank you."
    scene ch4sc3_020 with dissolve
    da "You should know... the journey will be long..."
    da "You're about to get a real taste of what it means to be an adventurer... make sure to say your goodbyes."
    da "You should expect to be at sea for several moons."
    scene ch4sc3_032 with dissolve
    sy "Wha?! Several?! But-"
    scene ch4sc3_021 with dissolve
    mc "Noted. I'll make preparations for the journey, and give my friends a heads up."
    mc "I’ll see you tomorrow at first light."
    scene black with Dissolve(1.5)
    "Dalen heads to his office and you head for the door."
    scene ch4sc3_033 with Dissolve(1.5)
    sy "[mc]!"
    scene ch4sc3_034 with dissolve
    mc "Sylph? What is it?"
    scene ch4sc3_035 with dissolve
    "You feel her small hands grab onto yours and gently place something in your palm."
    sy "Please take this! It will protect you from the bad things..."
    sy "This flower contains magical properties from the Earth Mother's tree."
    sy "If you bring it back to me..."
    sy "We’ll make it bloom... together."
    scene ch4sc3_036 with dissolve
    mc "Thank you, Sylph. I’ll be sure to bring it back to you."
    scene ch4sc3_037 with dissolve
    $ renpy.pause()
    scene ch4sc3_038 with dissolve
    $ renpy.pause()
    scene ch4sc3_039 with dissolve
    $ renpy.pause()
    scene ch4sc3_040 with dissolve
    "Sylph stops just before her small lips connect with yours and you feel her warm breath tickle your lips."

    ###Choice###
    menu:
        "Kiss her. ({color=#ff8cdd}Romance{/color})":
            scene ch4sc3_041 with dissolve
            "Her upper lip carefully grazes yours and her breathing intensifies."
            scene ch4sc3_042 with dissolve
            "As you tilt your head, she playfully caresses your lips with hers."
            "Her hand remains firm at the back of your neck as she begins to kiss you as delicately as a flower."
            scene ch4sc3_043 with dissolve
            $ renpy.pause()
            sy "*Mwahh* Mhnnhh!"
            $ sylph_path = True
            ####Animation####
            show sy_kiss1 with fade
            $ renpy.pause(2, hard=True)
            "Her small lips are warm and tingling with magic. An intoxicating sensation you haven’t felt before."
            sy "Mhhhh... MhMh! *Soft moans* Mhhww!"
            "She keeps kissing you, making sure there’s no space between your lips."
            "She wants to be close to you... She longs for it."
            "Her delicate kisses keeps increasing in intensity, as do her moans."
            "Until she finally pulls away."
            $ sylph_kiss = True
            scene ch4sc3_042 with dissolve
            sy "Mmhwaa..."
            scene ch4sc3_036 with dissolve
            mc "What’s that for?"
            scene ch4sc3_039 with dissolve
            sy "Just something for good luck."
            sy "Here, let me give you some more..."
            scene ch4sc3_040 with dissolve
            $ renpy.pause()
            scene ch4sc3_041 with dissolve
            $ renpy.pause()
            scene ch4sc3_042 with dissolve
            $ renpy.pause()
            scene ch4sc3_043 with dissolve
            $ renpy.pause()

        "Turn her down. ({color=#2bff8b}Friendship{/color})":
            scene ch4sc3_040 with dissolve
            mc "Sylph, no."
            mc "It’s not a good idea... it's not the time for this."
            scene ch4sc3_039 with dissolve
            sy "R-Right... I’m sorry, silly, silly me."
            sy "I thought you might’ve felt the same about me... the way our magic connects..."
            scene ch4sc3_036 with dissolve
            mc "Don’t be sorry... it takes courage to show how you feel."
            mc "I just can’t return your feelings, at least not at this moment."
            scene ch4sc3_037 with dissolve
            sy "..."
            scene ch4sc3_038 with dissolve
            $ renpy.pause()
            scene ch4sc3_039 with dissolve
            sy "I-I... thank you ,[mc]."
            sy "That does make sense, when you put it like that."
            sy "Please make sure you come back..."

    scene black with Dissolve(2)
    stop music fadeout 2
    $ renpy.pause(0.5)
    jump ch4sc4
