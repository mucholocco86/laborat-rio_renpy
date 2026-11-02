
label ch3sc10:

    window hide dissolve
    play music outdoors_2 fadein 1.0
    scene black with Dissolve (2.0)
    scene ss31 with Dissolve(2.0)
    $ renpy.pause()
    scene ch3sc10_001 with Dissolve(2.0)
    $ renpy.pause(1)
    mc "According to the instructions Sylph gave us, the stables should be around here."
    el "Yeah, she said about two miles west of the city-gate, feels like this would be about that far."
    scene ch3sc10_002 with dissolve
    $ renpy.pause(0.6)
    mc "Keep your eyes peeled for anything that looks like a barn or stable-like."
    scene ch3sc10_003 with dissolve
    el "Look!"
    el "I think that’s it over there."
    scene ch3sc10_004 with dissolve
    mc "Ah, finally..."
    mc "I thought we’d have to circle back."
    scene ch3sc10_005 with dissolve
    el "Don’t be silly, we’ve only walked a few miles!"
    scene ch3sc10_004 with dissolve
    mc "Let’s go check if the stable keeper is around."
    scene ch3sc10_007 with dissolve
    "The two of you scan the area for any signs of activity but nothing catches your eye."
    scene ch3sc10_008 with dissolve
    el "Hello, anybody here?"
    scene ch3sc10_009 with dissolve
    uk "Hi there!"
    scene ch3sc10_010 with dissolve
    uk "What can I do for you two?"
    scene ch3sc10_011 with dissolve
    uk "If you’re here to buy a horse, you'll have to wait..."
    uk "We don’t have any available for sale at the moment,as they've been relocated for their safety."
    uk "But we still have some saddles available."
    scene ch3sc10_012 with dissolve
    el "Actually, we’re here on behalf of the Adventurers Guild."
    el "You know, to save you."
    scene ch3sc10_013 with dissolve
    mc "We heard you were having trouble with wolves in the area?"
    mc "We just received your contract."
    scene ch3sc10_014 with dissolve
    uk "Oh, I didn’t expect anyone so soon!"
    uk "I only just sent out the request this morning."
    scene ch3sc10_015 with dissolve
    uk "Thank the Divines! That you guys could respond to it this soon."
    uk "The stable keeper has been worried for the horses ever since our mare was driven off."
    scene ch3sc10_014 with dissolve
    sl "I’m Selena by the way, Nice to meet you guys!"
    scene ch3sc10_016 with dissolve
    el "Nice to meet you, Selena."
    el "I’m Eliza, and my partner here is [mc]."
    scene ch3sc10_017 with dissolve
    mc "Nice to meet you, Selena."
    mc "So you're not the stable keeper then?"
    sl "Goodness, no. I'm working here as a stablemaiden, looking after the horses, grooming them and feeding them."
    scene ch3sc10_018 with dissolve
    sl "But enough about me, that's not what you came all the way out here for."
    sl "I suppose you two want to get right to work?"
    scene ch3sc10_019 with dissolve
    el "Yes! We're eager to solve this matter."
    el "Can you share any details about the recent attacks?"
    scene ch3sc10_020 with dissolve
    sl "Let's see..."
    sl "It started a few moons ago."
    scene ch3sc10_021 with dissolve
    sl "At first we just had a few encounters at the outskirts of the woods."
    sl "We didn’t think anything of it."
    scene ch3sc10_022 with dissolve
    el "Did they start getting closer to the stables?"
    scene ch3sc10_023 with dissolve
    $ renpy.pause(1)
    sl "*Exhales deeply* ..."
    scene ch3sc10_024 with dissolve
    sl "*Sigh* Yes... recently, they even managed to hunt and kill one of our horses that got loose."
    sl "It was our breeding mare."
    sl "Without her, it'll be a while before we can procure another and start breeding again."
    scene ch3sc10_025 with dissolve
    el "Oh, that's horrible..."
    el "Is that why you aren’t selling any at the moment?"
    scene ch3sc10_026 with dissolve
    sl "*Nods* Yes, we can’t afford to lose any more horses now..."
    sl "Otherwise we might not be able to breed any new offspring next season."
    sl "A-And no offspring means no income. We'd have to close down the stables."
    sl "That's why the stable keeper is relocating the horses to a nearby stable until the issue has been resolved."
    scene ch3sc10_027 with dissolve
    mc "Selena, can you show us the nearby area where you have seen the wolves?"
    scene ch3sc10_028 with dissolve
    sl "Oh. You mean go out there? To the woods?"
    scene ch3sc10_029 with dissolve
    mc "Yes, we’ll need to find them to deal with them."
    scene ch3sc10_30 with dissolve
    sl "I’m not too fond of going out there... there's wolves..."
    scene ch3sc10_31 with dissolve
    el "Don’t worry Selena, we’ll be there as well."
    el "If anything happens, we’ll handle it!"
    scene ch3sc10_32 with dissolve
    "Selena, clearly nervous and not reassured by Eliza, looks to you."
    ####Choice###
    menu:
        "Reassure her. ({color=#87e1fa}Charisma{/color})" if True:
            scene ch3sc10_027 with dissolve
            mc "Hey..."
            mc "I won’t let anything happen to you, Selena."
            mc "You'll be safe with me."
            $ charisma += 1
            scene ch3sc10_30 with dissolve
            sl "I guess you'd be right there with me... that does make me feel a bit safer."
            "Selena feels reassured by you, her trust has increased by {size=+3}{b}{color=#2bff8b}1{/color}{/b}{/size}."
            sl "O-Okay, I suppose I could show you."
            "You successfully reassured Selena, your {color=#87e1fa}Charisma{/color} has increased by {size=+3}{b}{color=#2bff8b}1{/color}{/b}{/size}."
            $ selena_trust += 1

        "Dismiss her. ({color=#ffee54}Leadership{/color})" if True:
            scene ch3sc10_029 with dissolve
            mc "Selena, we can't help you solve the problem if you don't show us."
            mc "Being scared of wolves is silly, especially with us here."
            $ leadership += 1
            mc "I'm here to do a job, now take me to the area so I can resolve this matter."
            scene ch3sc10_30 with dissolve
            sl "[mc]... O-Okay, yeah."
            sl "I'll trust in your direction, let's go, it isn't far."
            "You successfully took control of the situation, your {color=#ffee54}Leadership{/color} has increased by {size=+3}{b}{color=#2bff8b}1{/color}{/b}{/size}."

    scene ch3sc10_33 with dissolve
    sl "Follow me! It's not too far from here."
    scene ch3sc10_34 with dissolve
    $ renpy.pause()
    scene ch3sc10_35 with dissolve
    $ renpy.pause()
    scene ch3sc10_36 with dissolve
    sl "What are you looking for exactly?"
    scene ch3sc10_37 with dissolve
    mc "Signs of activity."
    mc "Like paw prints in the dirt, or tufts of fur stuck to branches. Anything that could give us a clue."
    sl "It’s around here we first spotted them, we've seen a grey-ish one and a black one."
    scene ch3sc10_38 with dissolve
    el "Be alert, Selena."
    el "If anything happens, let us handle it."
    scene ch3sc10_39 with dissolve
    sl "Will do, Eliza!"
    sl "Thank you guys... Really, I mean it."
    scene ch3sc10_40 with dissolve
    $ renpy.pause()
    scene ch3sc10_41 with dissolve
    mct "Hmh?"
    scene ch3sc10_42 with dissolve
    mct "..."
    stop music fadeout 2.0
    scene ch3sc10_43 with dissolve
    mc "You two, get down."
    scene ch3sc10_44 with dissolve
    play music darknight_3 fadein 1.0
    el "*Whispers* {size=-10}{b}Did you see anything?{/b}{/size}"
    scene ch3sc10_45 with dissolve
    mc "*Whispers* {size=-10}{b}I thought I heard something in the distance.{/b}{/size}"
    scene ch3sc10_46 with dissolve
    $ renpy.pause()
    scene ch3sc10_47 with dissolve
    el "*Whispers* {size=-10}{b}False alarm, I suppos-{/b}{/size}"
    scene ch3sc10_48 with dissolve
    with vpunch
    sl "{b}AaahhH!!{/b}"
    scene ch3sc10_49 with dissolve
    sl "{b}S-Stay back!! You beast!{/b}"
    scene ch3sc10_50 with dissolve
    $ renpy.pause()
    scene ch3sc10_51 with dissolve
    "*Snarls* Hrrh!"
    scene ch3sc10_52 with dissolve
    sl "*Nervous* {b}G-Guys! Help!{/b}"
    scene ch3sc10_53 with dissolve
    mc "Selena, don’t move a muscle."
    scene ch3sc10_54 with dissolve
    el "What should we do?"
    scene ch3sc10_55 with dissolve
    mc "..."
    ###Choice###
    menu:
        "Lure the wolf away. (Eliza's Preference)" if True:
            "Eliza’s trust has increased by {size=+3}{b}{color=#2bff8b}1{/color}{/b}{/size}."
            $ eliza_trust += 1
            scene ch3sc10_55 with dissolve
            mct "It’s risky, but I could try to lure the wolf away."
            mct "I hope this doesn’t backfire... the success of our quest depends on it."
            scene ch3sc10_56 with dissolve
            mc "Eliza, I’m going to attempt to lure the wolf away."
            mc "You’re in charge of getting Selena back to the stables safely."
            scene ch3sc10_57 with dissolve
            el "Okay! I won’t let you down."
            scene ch3sc10_58 with dissolve
            mc "Wait for me to be out of sight."
            mc "I’ll meet you back at the stables. Let’s go!"
            scene ch3sc10_59 with dissolve
            with vpunch
            $ renpy.pause()
            scene ch3sc10_60 with dissolve
            sl "{b}Careful [mc]!{/b}"
            scene ch3sc10_61 with dissolve
            mc "Here boy!"
            scene ch3sc10_62 with dissolve
            with vpunch
            sl "{b}Aaiiihh!{/b}"
            scene ch3sc10_63 with dissolve
            el "Hey, Selena..."
            el "They’re gone, it’s alright now."
            scene ch3sc10_64 with dissolve
            sl "A-Are you sure?"
            sl "That was so scary!"
            scene ch3sc10_65 with dissolve
            el "Yes, don’t worry, [mc] is amazing."
            el "It’ll take more than a hungry wolf to beat him."
            scene ch3sc10_66 with dissolve
            el "Come, let’s get you back to the stables, we'll be safe there while we wait for [mc]."
            scene black with Dissolve(1.5)
            $ renpy.pause(1.5)
            scene ch3sc10_67 with Dissolve(1.5)
            $ renpy.pause(0.5)
            mc "It’s just me and you now."
            mc "I don’t suppose you’ll agree to just return to the woods and leave the horses alone?"
            scene ch3sc10_68 with dissolve
            $ renpy.pause(1.5)
            scene ch3sc10_69 with dissolve
            "*Growls* Hhrrhh!"
            scene ch3sc10_70 with dissolve
            mc "..."
            scene ch3sc10_71 with dissolve
            mc "*Sigh* Let's see if what Rin taught me still works."
            scene black with Dissolve(2)
            $ renpy.pause(1)
            scene ch3rin1 with Dissolve(2)
            $ renpy.pause(1)
            ri "Look [mc]!"
            ri "We can practice on this cute little one over here."
            scene ch3rin2 with dissolve
            mc "*Sigh* Rin…"
            mc "The last five times we tried it didn’t work."
            scene ch3rin3 with dissolve
            ri "This time it will work!"
            ri "I know it will."
            scene ch3rin4 with dissolve
            ri "You almost had it last time remember?"
            ri "And this time I can feel it in my tummy! You will be able to do it!"
            ri "Close your eyes and remember what we practiced."
            scene ch3rin5 with dissolve
            $ renpy.pause(1)
            mct "*Exhales* Okay... just like we practiced."
            scene ch3rin6 with dissolve
            $ renpy.pause(1.2)
            scene ch3rin7 with dissolve
            "You feel Rin’s soft fingers run through the back of your hair until they reach your temples."
            ri "*Whispers* {size=-5}{b}Inhale deeply, tune out the sounds of the forest until all you hear is my voice and your heartbeat.{/b}{/size}"
            ri "*Whispers* {size=-5}{b}Feel the breeze on your skin as it flows through the woods.{/b}{/size}"
            ri "*Whispers* {size=-5}{b}Focus on your intentions for this little creature. You are his friend. He can trust you, and you him.{/b}{/size}"
            ri "*Whispers* {size=-5}{b}You are ready, [mc]. Open your eyes and bond with him.{/b}{/size}"
            scene ch3rin8 with dissolve
            $ renpy.pause(1.2)
            scene ch3rin9 with dissolve
            $ renpy.pause()
            scene black with Dissolve(2)
            $ renpy.pause(1.2)
            scene ch3sc10_71 with Dissolve(2)
            $ renpy.pause(1.2)
            mc "*Exhales deeply*"
            mct "Just like you taught me... Rin."
            scene ch3sc10_72 with dissolve
            $ renpy.pause()
            scene ch3sc10_73 with dissolve
            $ renpy.pause()
            scene ch3sc10_72 with dissolve
            stop music fadeout 2.0
            $ renpy.pause()
            scene ch3sc10_74 with dissolve
            play music chill_3 fadein 1.0
            "Suddenly the large Direwolf seems to give in to your authority and relaxes."
            scene ch3sc10_75 with dissolve
            mc "See? You can be a good puppy... we don’t have to hurt each other."
            mc "You're not as scary as you appear."
            mc "You were just hunting for food, weren't you?"
            scene ch3sc10_76 with dissolve
            mc "But you can’t hunt the horses anymore, okay buddy?"
            mc "It's causing trouble for the stables nearby, which will eventually lead to hiring of hunters."
            scene ch3sc10_77 with dissolve
            mc "I know, I know."
            mc "Horse thighs are probably very delicious to a Direwolf like yourself."
            scene ch3sc10_78 with dissolve
            mc "You’ll just have to hunt deer or rabbits from now on."
            uk "*Whines* Hiiih... hniihh..."
            scene ch3sc10_77 with dissolve
            mc "I’m [mc]. Do you have a name, buddy?"
            uk "*Whines* Hhniiih..."
            mc "No? We can’t have that, can we?"
            mc "You’ve been a bit of a troublemaker so far."
            scene ch3sc10_78 with dissolve
            mc "I guess *Trouble* is a suitable name, no?"
            scene ch3sc10_79 with dissolve
            trb "*Howls in acknowledgement* {b}AAaoooohh!!{/b}"
            scene ch3sc10_80 with dissolve
            mc "*Chuckles* Trouble it is, then!"
            mc "Go on, get out of here... maybe we’ll see each other again under better circumstances, Trouble."
            scene ch3sc10_81 with dissolve
            $ renpy.pause()
            scene ch3sc10_82 with dissolve
            $ renpy.pause()
            "Trouble turns to look at you, she seems to nod at you before she disappears into the woods."
            scene ch3sc10_83 with dissolve
            mct "*Chuckles* I guess I do have a soft spot after all."
            scene black with Dissolve(2)
            stop music fadeout 2.0
            $ renpy.pause(1)
            jump ch3sc11

        "Pretend to kill the wolf. (Selena's Preference)" if True:
            "Selena’s trust has increased by {size=+3}{b}{color=#2bff8b}1{/color}{/b}{/size}."
            $ selena_trust += 1
            scene ch3sc10_55 with dissolve
            mct "The only way to guarantee Selena’s safety is to eliminate the wolf."
            mct "Unless... maybe {b}'that'{/b} could work?"
            scene ch3sc10_56 with dissolve
            mc "I’ll handle the wolf. Don’t hesitate, otherwise it might kill Selena."
            mc "As soon as it focuses on me, you grab Selena and take her back to the stables."
            scene ch3sc10_57 with dissolve
            el "O-Okay. I won’t let you down."
            scene ch3sc10_60 with dissolve
            sl "Please, do something [mc]!"
            scene ch3sc10_61 with dissolve
            mc "Hey stinky-paws! Over here!"
            scene ch3sc10_62 with dissolve
            with vpunch
            $ renpy.pause(2)
            scene ch3sc10_63 with dissolve
            el "Hey, Selena. They’re gone. It’s alright now."
            scene ch3sc10_64 with dissolve
            sl "A-Are you sure?"
            scene ch3sc10_65 with dissolve
            el "Yes. Don’t worry, [mc] is amazing. It’ll take more than a hungry wolf to beat him.."
            scene ch3sc10_66 with dissolve
            el "Come. Let’s get back to the stables. We'll be safe there while we wait for [mc]."
            scene black with dissolve
            $ renpy.pause(1.5)
            scene ch3sc10_67 with dissolve
            mc "It’s just me and you now. I don’t suppose you’ll agree to just return to the woods and leave the horses alone?"
            scene ch3sc10_68 with dissolve
            $ renpy.pause(1.5)
            scene ch3sc10_69 with dissolve
            "*Growls*"
            scene ch3sc10_70 with dissolve
            mc "..."
            scene ch3sc10_71 with dissolve
            mc "I really don’t feel like killing an animal. It has just been hunting for food, as is natural for him."
            mc "*Sigh* Let's see if what Rin taught me still works."
            scene black with Dissolve(2)
            $ renpy.pause(1.2)
            scene ch3rin1 with dissolve
            ri "Look [mc]! We can practice on this cute little one over here."
            scene ch3rin2 with dissolve
            mc "*Sigh* Rin… The last five times we tried it didn’t work."
            scene ch3rin3 with dissolve
            ri "This time it will work!"
            ri "I know it will."
            scene ch3rin4 with dissolve
            ri "You almost had it last time remember? And this time I can feel it in my tummy. You will be able to do it!"
            ri "Close your eyes and remember what we practiced."
            scene ch3rin5 with dissolve
            $ renpy.pause(1.2)
            scene ch3rin6 with dissolve
            $ renpy.pause(1.2)
            scene ch3rin7 with dissolve
            "You feel Rin’s soft fingers run through the back of your hair until they reach your temples."
            ri "*Whispers* {size=-5}{b}Inhale deeply, tune out the sounds of the forest until all you hear is my voice and your heartbeat.{/b}{/size}"
            ri "*Whispers* {size=-5}{b}Feel the breeze on your skin as it flows through the woods.{/b}{/size}"
            ri "*Whispers* {size=-5}{b}Focus on your intentions for this little creature. You are his friend. He can trust you, and you him.{/b}{/size}"
            ri "*Whispers* {size=-5}{b}You are ready, [mc]. Open your eyes and bond with him.{/b}{/size}"
            scene ch3rin8 with dissolve
            $ renpy.pause(1.2)
            scene ch3rin9 with dissolve
            $ renpy.pause()
            scene black with Dissolve(2)
            $ renpy.pause(1.2)
            scene ch3sc10_72 with dissolve
            $ renpy.pause(2)
            scene ch3sc10_73 with dissolve
            $ renpy.pause(2)
            scene ch3sc10_72 with dissolve
            stop music fadeout 2.0
            $ renpy.pause(2)
            scene ch3sc10_74 with dissolve
            play music chill_3 fadein 1.0
            "Suddenly the large Direwolf seems to give in to your authority and relaxes."
            scene ch3sc10_75 with dissolve
            mc "See? You can be a good puppy. We don’t have to hurt each other."
            mc "You're not as scary as you appear. You were just hunting for food, weren't you?"
            scene ch3sc10_76 with dissolve
            mc "But you can’t hunt the horses anymore, okay buddy?"
            scene ch3sc10_77 with dissolve
            mc "I know, I know. Horse thighs are probably very delicious to a Direwolf like yourself."
            scene ch3sc10_78 with dissolve
            mc "You’ll just have to hunt deer or rabbits from now on."
            scene ch3sc10_77 with dissolve
            mc "I’m [mc]. Do you have a name, buddy?"
            mc "No? We can’t have that, can we? You’ve been a bit of a troublemaker so far."
            scene ch3sc10_78 with dissolve
            mc "I guess *Trouble* is a suitable name, no?"
            scene ch3sc10_79 with dissolve
            trb "*Howls* AAauuuuuuhh!!"
            scene ch3sc10_80 with dissolve
            mc "Trouble it is, then! Go on, get out of here. Maybe we’ll see each other again under better circumstances, Trouble."
            scene ch3sc10_81 with dissolve
            $ renpy.pause(2)
            scene ch3sc10_82 with dissolve
            $ renpy.pause(2)
            scene ch3sc10_83 with dissolve
            mct "Heh. I guess I do have a soft spot after all."
            scene black with Dissolve(1.5)
            stop music fadeout 2.0
            $ renpy.pause(1)
            jump ch3sc11
