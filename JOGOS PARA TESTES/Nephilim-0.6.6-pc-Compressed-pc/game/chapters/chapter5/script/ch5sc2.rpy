label ch5sc2:

    window hide dissolve
    play music forest_1 fadein 1.0
    #stop music fadeout 1.0
    scene black with Dissolve (2.0)
    $ renpy.pause(1)
    scene ch5sc04_000 with Dissolve(1.5)
    $ renpy.pause()
    scene ch5sc04_001 with dissolve
    am "Ugh! Can you believe Mother and Father both agreed to this?!"
    fr "U-Uhm, yes-"
    am "It was rhetorical, Frida!"
    fr "S-Sorry!"
    scene ch5sc04_002 with dissolve
    am "Why couldn’t they just hire someone from our royal guard?"
    am "Instead of that oaf! Urgh!"
    scene ch5sc04_003 with dissolve
    fr "Oaf? Why do you call him such?"
    am "Hmph!"
    fr "They've tried hiring several men from the royal guard. You’ve sent them all away."
    scene ch5sc04_004 with dissolve
    am "He stumbled into me at the market. Knocked me flat on my ass!"
    am "And then he has the nerve to show up here thinking he can protect me?! Ugh!"
    scene ch5sc04_003 with dissolve
    fr "I don’t think he purposely walked into you? H-He seems really kind."
    scene ch5sc04_002 with dissolve
    am "Kind?! Frida, whose side are you on?"
    am "Wait... How do you know that he's kind?"
    scene ch5sc04_001 with dissolve
    fr "I... I had to bring him a towel after the chamberlain made him bathe before his audience."
    with vpunch
    am "{b}WHAT?!{/b} That lecherous oaf!"
    am "I knew he was up to no good!"
    scene ch5sc04_004 with dissolve
    am "I’ll have him thrown into the dungeons for making you do such a thing!"
    scene ch5sc04_003 with dissolve
    fr "Please don't."
    fr "It- It wasn’t him."
    fr "The chamberlain ordered me to do it. [mc] was just as surprised."
    scene ch5sc04_005 with dissolve
    am "So..."
    am "He didn't act like a pervert with you?"
    scene ch5sc04_006 with dissolve
    fr "Not at all! He was actually kind."
    fr "I think he was trying to make me feel comfortable after he noticed how nervous I was."
    fr "He didn’t try anything perverted. He even said I didn’t have to do it."
    amt "He was willing to be dirty during his audience to avoid making Frida uncomfortable? Hmh..."
    scene ch5sc04_007 with dissolve
    am "Good... That’s good."
    am "At least he is somewhat civilized for a commoner."
    scene ch5sc04_008 with dissolve
    am "Did you... get a good look at him?"
    scene ch5sc04_009 with dissolve
    fr "G-Good look at him? I... I- Uhh..."
    scene ch5sc04_010 with dissolve
    am "Did he look capable? Is he athletic? Did he seem strong?"
    scene ch5sc04_009 with dissolve
    fr "*Blushing* I... Uhhh... Y-Yes. V-very much so."
    fr "I-I mean... He has... a toned physique?"
    fr "D-Defined muscles... S-Scars all over his torso and back."
    scene ch5sc04_010 with dissolve
    am "Scars?"
    fr "*Nods* Mhm-hm."
    am "What were they like?"
    scene ch5sc04_011 with dissolve
    fr "{b}BIG!{/b} Uh... I mean..."
    fr "They looked like large claw marks that run deep, and a few blade cuts too."
    scene ch5sc04_010 with dissolve
    am "Interesting."
    am "He looks the same age as me, how on earth did he manage to get so many scars?"
    scene ch5sc04_011 with dissolve
    fr "He... Must’ve been through a lot of horrible things... to get such scars."
    scene ch5sc04_010 with dissolve
    am "Hmh. Thank you, Frida."
    am "That will be all for tonight."
    scene ch5sc04_001 with dissolve
    fr "Goodnight, Miss Amelia! Purest of dreams to you."
    am "You too, Frida."
    scene ch5sc04_012 with dissolve
    $ renpy.pause()
    scene ch5sc04_013 with dissolve
    $ renpy.pause()
    am "*Sigh* I still don’t get why they insist on me having a bodyguard..."
    scene ch5sc04_014 with dissolve
    am "I’m about to celebrate my 20th name day. I don’t need someone watching over me! Ugh!"
    am "Especially that oaf! ... He’s a commoner!"
    am "How is {b}HE{/b} supposed to protect me?!"
    scene ch5sc04_015 with dissolve
    am "Frida seems to think highly of him. But she used to be a commoner too."
    am "I’m sure her impression of him is clouded by pity. Definitely."
    scene ch5sc04_016 with dissolve
    am "I bet he’ll run away crying at the first sign of trouble, just like all the others."
    am "Maybe I'll turn up my attitude and he'll quit. Then they'll see I don't need a babysitter..."
    am "Frida said he had a bunch of scars... but he probably got them running away from fights!"
    scene ch5sc04_017 with dissolve
    am "..."
    am "He did help me up after I fell down in the market... but he was the reason I fell down in the first place."
    am "And Frida said he treated her well. But it would've been stupid of him to try anything lewd right here in the palace..."
    am "Whatever... I’ll have to think of a way to make him quit."
    scene black with Dissolve(2)
    #play music forest_1 fadein 1.0
    stop music fadeout 1.0
    scene ch5sc04_018 with dissolve
    play music feels_1 fadein 1.0
    #stop music fadeout 1.0

    ####Animation####
    scene el_sleep4 with dissolve
    $ renpy.pause(3, hard=True)
    scene ch5sc04_018 with dissolve
    scene ch5sc04_019 with dissolve
    mct "{i}Hmrh... Did she steal the blanket again?{/i}"
    scene ch5sc04_020 with dissolve
    mct "{i}What’s she doing over there?{/i}"
    mct "{i}She’s crying?{/i}"
    scene ch5sc04_021 with dissolve
    el "*Sobbing quietly*"
    scene ch5sc04_022 with dissolve
    el "*Sobbing quietly*"
    scene ch5sc04_023 with dissolve
    "You sit down beside her and hold onto her gently."
    mct "{i}She’s shaking. I hate seeing her like this... I feel... helpless in moments like these.{/i}"
    scene ch5sc04_024 with dissolve
    if samarah_alive == True:
        scene ch5sc04_024 with dissolve
        mct "{i}She's been through so much emotional turmoil lately.{/i}"
        mct "{i}Seeing Selena again caught her off-guard, and then she had to fight every fibre of her being to let her go.{/i}"
        mct "{i}Sometimes she's so headstrong that I forget how fragile she is.{/i}"
        mct "{i}She's endured so much from a young age, her parents weren't killed... they abandoned her.{/i}"
        mct "{i}She's had to find a way to keep on living for all those years. I can't imagine how that felt for a young girl...{/i}"
        mct "{i}Now that her emotions are heightened, it's all boiling over.{/i}"
        scene ch5sc04_025 with dissolve
        el "*Sobs* I... I’m a horrible person! I-I couldn't forgive her in the end!"
        el "*Sobs* And every time I walk past someone, I just want to tear open their necks and drain their blood!"
        with vpunch
        el "*Sobs* I can’t! I c-can’t! I can’t be like this!"
        el "No-n-no-No, no! {b}NO!{/b}"
        scene ch5sc04_026 with dissolve
        mc "Hey..."
        mc "It’ll be alright. You will be okay... I promise."


    else:
        scene ch5sc04_024 with dissolve
        mct "{i}She’s struggling with the guilt of having taken a life. Doesn’t matter that it was Selena.{/i}"
        mct "{i}Eliza’s compassion is the most genuine I’ve ever seen, and now she has taken a life.{/i}"
        scene ch5sc04_025 with dissolve
        el "*Sobs* I... I’m a killer!"
        with vpunch
        el "*Sobs* I can’t! I c-can’t! I can’t be like this!"
        el "No-n-no-No, no! {b}NO!{/b}"
        el "*Sobs* I killed her! I killed Selena. And I enjoyed it! I... it felt good!"
        scene ch5sc04_026 with dissolve
        mc "Hey... It’ll be alright."
        mc "You will be okay... I promise."
        if eldark >= 2:
            scene ch5sc04_025 with dissolve
            el "I... enjoyed it."
            el "Hurting her felt... empowering."
            el "*Voice breaks* No... it's not okay... I shouldn't feel this way!"

        else:
            scene ch5sc04_025 with dissolve

    scene ch5sc04_025 with dissolve
    el "*Shaky voice* None of this is okay!"
    el "You... you can’t promise me that everything will be fine!"
    el "*Shaky voice* Nothing is fine! I'm a monster! I-I don't think I can do this!"
    scene ch5sc04_024 with dissolve
    mct "{i}Fuck. This isn’t good... her emotions are overwhelming her.{/i}"
    mct "{i}I can’t let this go on. If she gives up fighting against it, she'll end up going feral.{/i}"
    mct "{i}From what Lucid said, this happens to a lot of vampires.{/i}"
    mct "{i}If they experience too much emotional distress, they can just shut down and become mindless.{/i}"
    scene ch5sc04_026 with dissolve
    mc "Listen, I have an idea."
    mc "It’s a long shot, but I need you to go stay with Sylph and Dalen, okay?"
    scene ch5sc04_025 with dissolve
    el "*Sobs* S-Sylph and Dalen? ... W-Why?"
    scene ch5sc04_026 with dissolve
    mc "I'm going to try and contact Lucid."
    mc "Sylph and Dalen will be able to watch over you."
    scene ch5sc04_027 with dissolve
    el "*Sobs* O-Okay... W-Will you be long?"
    scene ch5sc04_028 with dissolve
    mc "I’m not sure."
    mc "Just promise me you'll stay with them until I return?"
    scene ch5sc04_027 with dissolve
    el "Okay, I promise."
    scene ch5sc04_028 with dissolve
    mc "Good girl."
    mc "Let’s get dressed and I’ll take you there."
    scene black with Dissolve(2)
    "You take Eliza to the guild and leave her in the care of Sylph and Dalen."
    scene ch5sc04_029 with Dissolve(2)
    mct "{i}*Sigh* Hopefully this works.{/i}"
    scene ch5sc04_030 with dissolve
    mct "{i}Lucid? I need... I need your help.{/i}"
    scene ch5sc04_031 with dissolve
    mct "{i}I’m at a loss and you’re the only one I can think of that can possibly help.{/i}"
    mct "{i}If you can hear me... please... answer me.{/i}"
    scene ch5sc04_032 with dissolve
    mc "..."
    mct "{i}*Sigh* What was I expecting?{/i}"
    mct "{i}It was worth a try. Maybe Dalen can come up with something?{/i}"
    scene ch5sc04_033 with dissolve
    mct "{i}Huh?{/i}"
    ####Animation####
    scene ani_sum1 with dissolve
    mct "{i}Somethings happening. She heard me?{/i}"
    mct "{i}I feel... light? Weightless... Just like when I touched the Chalice of Vitality.{/i}"
    #play music darknight_4 fadein 1.0
    stop music fadeout 1.0
    scene black with dissolve
    $ renpy.pause(1.5)
    play music explore_1 fadein 1.0
    #stop music fadeout 1.0
    scene ch4sc15_020 with Dissolve(1.5)
    mct "*Groans* Urrhh... I don’t think I’ll ever get used to this transportation magic."
    scene ch4sc15_021 with dissolve
    mct "This looks familiar..."
    scene ch4sc15_022 with dissolve
    mct "It’s definitely her."
    mct "Is this how she intends to greet me every time?"
    scene ch4sc15_023 with dissolve
    ld "Look who’s finally awake!"
    ld "About time too! I was getting bored!"
    scene ch4sc15_026 with dissolve
    mc "Lucid... How long was I out?"
    scene ch4sc15_027 with dissolve
    ld "Two minutes! Tsk!"
    scene ch4sc15_025 with dissolve
    ld "It’s rude to keep a lady waiting, you know?"
    scene ch4sc15_024 with dissolve
    mc "A lady? Is that what you are?"
    ld "..."
    mc "Do ladies always greet their visitors with that kind of attitude?"
    scene ch4sc15_025 with dissolve
    ld "I believe I greeted you with a pleasant view..."
    scene ch4sc15_026 with dissolve
    mct "That she did."
    mc "Sorry. You’re right, it was a pleasant greeting."
    scene ch4sc15_023 with dissolve
    ld "Glad you liked it! I expected you might!"
    ld "Now, tell your au-... Ahem."
    ld "Tell me what can I do for you?"
    scene ch4sc15_027 with dissolve
    ld "*Sighs* I suspect the view wasn't why you called for my aid."
    scene ch4sc15_026 with dissolve
    mc "No... Not quite."
    mc "I need your help."
    scene ch4sc15_027 with dissolve
    ld "My help?"
    scene ch4sc15_022 with dissolve
    ld "Come! Let’s go somewhere better suited for talking!"
    "With a snap of her fingers Lucid transports the two of you."
    scene black with Dissolve(2)
    #play music darknight_4 fadein 1.0
    stop music fadeout 1.0
    scene ch5sc04_035 with Dissolve(2)
    $ renpy.pause()
    play music home_2 fadein 1.0
    #stop music fadeout 1.0
    scene ch5sc04_036 with dissolve
    ld "Much better! Wouldn’t you agree?"
    scene ch5sc04_037 with dissolve
    mc "Sure. Where are we, though?"
    mc "I assume we're still in your realm. The Inferno Isles, you called it?"
    scene ch5sc04_038 with dissolve
    ld "Correct! My own little place in the cosmos."
    ld "Do you like it?"
    scene ch5sc04_037 with dissolve
    mc "I haven’t spent enough time here to form an opinion."
    scene ch5sc04_039 with dissolve
    ld "Mhph."
    scene ch5sc04_038 with dissolve
    ld "We’ll just have to change that."
    ld "I’ll take the blame since I practically kicked you out the door last time."
    scene ch5sc04_040 with dissolve
    ld "But not today! Today there's no rush!"
    ld "You can stay here with me as long as you desire."
    ld "We're long overdue for some quality time. Mhhm..."
    scene ch5sc04_037 with dissolve
    mc "I appreciate that."
    mc "But I'm facing a difficult situation..."
    scene ch5sc04_041 with dissolve
    mc "..."
    ld "Uh-oh. That face simply won’t do!"
    ld "As your au- Goddess! I will help you."
    scene ch5sc04_040 with dissolve
    ld "What do you desire? A feast worthy of a king? The ability to fly as a dragon?"
    ld "Chests filled with jewels and gold? Eternal life?"
    scene ch5sc04_042 with dissolve
    ld "Seven virgins worshiping at your feet, ready to fulfill every desire you could imagine?"
    ld "Say the word, and I’ll make it so!"
    scene ch5sc04_043 with dissolve
    mc "*Chuckles* Hah, thanks."
    mc "I might take you up on that sometime."
    scene ch5sc04_042 with dissolve
    ld "Mhm-Hm! Which one?"
    scene ch5sc04_043 with dissolve
    mc "Ahem, anyway..."
    scene ch5sc04_044 with dissolve
    ld "Boooh!"
    ld "I’ll get it out of you another time."
    scene ch5sc04_043 with dissolve
    ldt "He would've totally picked the seven virgins! Heh-heh-heh!"
    scene ch5sc04_044 with dissolve
    ld "Tell me, then."
    ld "What's bothering you?"
    scene ch5sc04_037 with dissolve
    mc "My friend... Eliza."
    mc "She's the one I wanted to help with your artifact."
    mc "The transition... her emotions... it’s all overwhelming her."
    scene ch5sc04_045 with dissolve
    mc "Whenever I think we're making strides towards her gaining control-"
    mc "-Something happens, and her guilt comes washing over her like a tidal wave."
    scene ch5sc04_044 with dissolve
    ld "Vampirism is not to be taken lightly."
    ld "I warned you last time we spoke."
    ld "Some individuals take to it quickly, they revel in their new found powers."
    scene ch5sc04_046 with dissolve
    ld "Others... they are too burdened by their emotions."
    ld "Vampires are apex predators."
    ld "And if a predator feels guilty about their own instincts... about their own survival..."
    scene ch5sc04_044 with dissolve
    ld "Well, I’m sure you can imagine what inner turmoil and stress that causes."
    scene ch5sc04_041 with dissolve
    mc "Mhm..."
    mct "She's right, I've thought the same thing, Eliza shouldn't feel guilty about having to eat."
    mct "Eliza has such a pure heart, having to hurt others to stay alive is not aligning with who she is."
    scene ch5sc04_045 with dissolve
    mc "So, that’s it then?"
    mc "There’s nothing to be done? She’s condemned to this burden forever?"
    mc "I’m assuming you can’t just snap your fingers and undo it?"
    scene ch5sc04_046 with dissolve
    ld "Correct... I may be all-powerful, but as I warned you, vampirism is permanent."
    scene ch5sc04_044 with dissolve
    ld "All my creations, they’re like... children to me. My children."
    scene ch5sc04_046 with dissolve
    ld "During the Abyss wars, some 3000 years ago... I lost so many of my children."
    ld "Succubusses, Imps, Ashspawn, Dragons, Hellhounds, Eyes of the Inferno, and many others..."
    scene ch5sc04_047 with dissolve
    ld "They were slaughtered by the thousands, by the Abyss lords."
    ld "And their foul minions."
    ld "So I decided to create new children who wouldn’t die so easily... Vampires."
    scene ch5sc04_048 with dissolve
    ld "Then I'd never have to feel the pain of losing my children again."
    ld "And hopefully, the nightmares of hearing their agonized screams would fade."
    scene ch5sc04_037 with dissolve
    mc "But vampires can still be killed, can't they?"
    mc "Might be difficult, but you said it yourself last time."
    scene ch5sc04_048 with dissolve
    ld "My siblings... the other Divines."
    ld "They willed it so..."
    scene ch5sc04_047 with dissolve
    ld "*Mimics* ‘Lucid, you’re tampering with mortals, it’s forbidden’..."
    scene ch5sc04_048 with dissolve
    with vpunch
    ld "They didn’t even try to understand my pain!"
    ld "All they cared about were their precious rules... Tsk."
    scene ch5sc04_049 with dissolve
    mc "Hey... I’m sorry you had to endure that."
    mc "I understand the pain of losing family... It never goes away, not truly."
    ##Choice##
    menu:
        "Be understanding.":
            scene ch5sc04_050 with dissolve
            mc "A mother will do anything to protect her children, it’s your instinct."
            mc "You just did what you thought would help them survive. I'd do the same."
            mc "In a way, I already did when I gave your artifact to Eliza. I chose for her to live forever."
            mc "I didn't want to endure a world without her."
            scene ch5sc04_051 with dissolve
            ld "[mc]... I... Thank you."
            ld "You’re kind... And warm."
            $ lucid_trust += 2
            "Lucid is genuinely surprised at how kind you are to her, her trust has increased by {size=+3}{b}{color=#2bff8b}2{/color}{/b}{/size}."

        "Tell her to suck it up.":
            scene ch5sc04_050 with dissolve
            mc "You’re one of the mightiest beings in the cosmos: one of the seven divines."
            mc "So suck it up. Sitting here moping about it won’t bring them back. Nothing will."
            mc "I had to learn that the hard way myself... and I was just a kid."
            scene ch5sc04_051 with dissolve
            ld "*Sighs heavily* You’re right..."

    scene black with Dissolve(2)
    "You comfort her a little while until she manages to gather herself."
    scene ch5sc04_052 with Dissolve(2)
    ld "Okay! I think I know something we can do for your Eliza."
    ld "Keep in mind, this is just an idea. I have no notion whether it will work or not."
    scene ch5sc04_053 with dissolve
    mc "I’ll do it. Whatever it is."
    scene ch5sc04_052 with dissolve
    ld "Nothing like this has been attempted before... But, you’re not exactly ordinary."
    ld "You may just be able to do it... if you get some guidance."
    scene ch5sc04_054 with dissolve
    mc "For some reason, I trust you completely."
    mc "I'll accept your guidance."
    scene ch5sc04_055 with dissolve
    ld "It’s simple!"
    ld "You trust me because we’re fam-"
    scene ch5sc04_056 with dissolve
    "She stops herself mid-sentence."
    ld "..."
    scene ch5sc04_057 with dissolve
    ld "Because I’m your goddess."
    ld "A-Anyway... I’m not the one who'll be guiding you."
    scene ch5sc04_054 with dissolve
    mc "You’re not? Then who?"
    scene ch5sc04_052 with dissolve
    ld "Maia."
    ld "She's the only one who would be qualified for what I have in mind."
    scene ch5sc04_053 with dissolve
    mc "Maia?"
    scene ch5sc04_058 with dissolve
    ld "You don’t know about her?"
    ld "She’s usually quite popular amongst mortals."
    scene ch5sc04_054 with dissolve
    mc "Never heard of her."
    mc "Is she one of the divines?"
    scene ch5sc04_059 with dissolve
    with vpunch
    ld "Marvelous! *Snickers* Simply brilliant!"
    scene ch5sc04_055 with dissolve
    ld "That was glorious! No, she isn’t one of the divines."
    ld "Maia, Maiden of Purity. She’s a Celestial."
    scene ch5sc04_054 with dissolve
    mc "Celestial?"
    scene ch5sc04_058 with dissolve
    ld "By the inferno!"
    ld "You really don’t know your deities do you?"
    scene ch5sc04_052 with dissolve
    ld "I suppose I can give you a quick rundown of the hierarchy of gods."
    ld "You really should know, given who you are..."
    scene ch5sc04_053 with dissolve
    mc "Thank you. I haven’t exactly studied at the academy or anything."
    mc "Been on the road most of my life and fighting for survival. Didn’t leave much time for studying deities."
    scene ch5sc04_058 with dissolve
    ld "Yet, here you are, sitting with one."
    ld "Okay, listen carefully!"
    scene ch5sc04_060 with dissolve
    ld "Hmh... I suppose I’ll start from the top!"
    ld "With my siblings and I."
    scene black with Dissolve(1.5)
    scene divines01 with Dissolve(1.5)
    ld "I’ll start with Azir. Mortals often worship him to gain his favor in endeavors concerning wealth."
    ld "Accordingly, they often refer to him as ‘The Golden One’."
    ld "He rules over the realm known as 'The Shimmering Sands'."
    ld "It's a vast desert realm, filled with riches hidden beneath its sandy dunes."
    mc "Sounds fancy."
    ld "Meh! It’s overrated, if you ask me. Besides... what does he even need all that wealth for?"
    scene divines02 with dissolve
    ld "Okay, let’s move on to Malpheon."
    ld "He’s a bit of a grump. He is known as the ‘Guardian of the Deep’"
    ld "The realm where he lives is called ‘The Caverns of Life’. It's a vast network of caverns interconnected with thousands of passageways."
    ld "It's said that the crystals from his realm contain potent magical properties."
    ld "Dwarves and stonemasons revere him greatly. They hope to gain his favor through digging for gems or building structures."
    mc "Heh... Borri and Gibson would love this guy."
    ld "Who? Anyway... Let’s move on."
    scene divines03 with dissolve
    ld "Next we have-... Yours truly!"
    ld "Cute as a button! Right?"
    mc "Definitely."
    ld "Heh-Hehh-Heheh!"
    ld "As you know, we're here in my realm called ‘The Inferno Isles’, where I live."
    ld "And the title I'm often given is ‘Mother of the Damned’ Tsk! Mortals have no taste."
    ld "Somehow, they find my children frightening. But I don’t see it! I think they’re cute."
    ld "Vampires... Dragons... Hellhounds... Ashspawns... Imps... Succubuses... and many more!"
    ld "Tell me those aren’t cute and cuddly?"
    mc "Uhm... sure?"
    ld "I knew you'd see it my way!"
    ld "Okay, let’s move on again."
    scene divines04 with dissolve
    ld "Up next is Raze, ‘Lord of Chaos’. Ugh! He's the black sheep of the family."
    ld "I might be a little mischievous at times, but he revels in chaos and trickery!"
    ld "He can be so annoying to deal with."
    ld "Anyway, he lives in ‘The Sunless Realms’. His realm was so dark after its creation that he..."
    ld "Created his own sun. It's known as the ‘Chaos star’. Mortals who worship him usually get what they ask for."
    ld "But often not in the way they'd imagined it. He likes to trick his subjects for his own amusemen..."
    mc "Sounds like a charmer."
    ld "If he tries to trick you, let me know. I’ll happily incinerate him!"
    scene divines05 with dissolve
    ld "Up next, we have Kinesis, ‘The Eternal’."
    ld "He rules over a realm known as ‘The Beyond’. It's a vast cosmic realm that constantly moves through space."
    ld "His followers believe that all magic has its roots in 'The Beyond' and, by extension, Kinesis himself."
    mc "Is it true?"
    ld "No. It’s true that his realm is potent in magic and many mortals are able to draw power from it."
    ld "But there’s magic in all the realms, and it takes many different forms."
    ld "You can probably guess that his followers and worshippers are those who seek advancement in magic."
    ld "He totally has a magical stick up his bum, though! He's way too serious for my liking!"
    with vpunch
    ld "Not once in our 6.000 years has he laughed at my jokes! {b}NOT ONCE!{/b}"
    mc "*Chuckles*"
    ld "That’s not funny! That's literally since the creation of Midomir itself..."
    ld "Okay, next..."
    scene divines06 with dissolve
    ld "My dear sister! Andromeda, ‘Mistress of the Moon’, ‘Sister of the stars’, ‘The Arcane Queen’."
    ld "Those are just a few of the countless titles her worshippers bestow upon her."
    ld "She resides in a realm of cosmic wonder known as Arcanium."
    ld "Arcanium is filled with glinting stars, brightly-colored nether-clouds, eternal night, and arcane energy."
    ld "Like Kinesis, she's also a matron to sorceresses, mages and wizards alike."
    ld "Usually her followers dabble in arcane mysteries or seek cosmic knowledge."
    ld "And she is my favorite sibling! Kind and understanding, she always has my back when Raze gets annoying."
    ld "*Snickering* One time, she bound him within a star and kept him there for a century!"
    ld "All because he was being mean to me."
    mc "A century? ... Remind me not to get on her bad side."
    ld "Fear not, she doesn’t have one. Only a protective side!"
    ld "And with that, you now know a little about ‘{b}The Pantheon of the Divines{/b}’."
    mc "That was only six, though? Aren’t there supposed to be seven of you?"
    scene ch5sc04_056 with dissolve
    ld "..."
    mc "Who's the seventh?"
    scene ch5sc04_057 with dissolve
    ld "I can’t... It’s not for me to tell."
    scene ch5sc04_056 with dissolve
    mc "Huh... Well, it’s okay. I'll find out some other time."
    scene ch5sc04_057 with dissolve
    ld "Yeah, he doesn’t want you to know just yet..."
    ld "Even me talking to you like this... will be frowned upon."
    scene ch5sc04_056 with dissolve
    mc "Frowned upon? Why wouldn’t you be allowed to talk to me? Aren’t you an almighty divine?"
    ld "..."
    scene ch5sc04_057 with dissolve
    ld "Yes... but there are rules."
    ld "He... he doesn’t think you are ready yet."
    scene ch5sc04_056 with dissolve
    mct "{i}Now she’s got me curious. Who in the five hells is ‘he’? And why is she obeying him?{/i}"
    mct "{i}Aren’t they siblings?{/i}"
    scene ch5sc04_057 with dissolve
    ld "Sorry... I’ve tried to tell him you should be included. But no luck."
    ld "You’re not mad at me, right?"
    scene ch5sc04_053 with dissolve
    mc "No, I’m not mad. I’m definitely both curious and disappointed about all the secrecy..."
    mc "But I don’t hold it against you. You’ve always been welcoming towards me."
    scene ch5sc04_055 with dissolve
    ld "Of course!"
    ld "We’re fam- friends! We’re friends!"
    scene ch5sc04_058 with dissolve
    ld "I’m afraid that’s all the deity lessons we have time for today."
    ld "Next time, we’ll look further down the hierarchy."
    ld "For now, I’ll send you to Maia so that you can help your friend."
    scene ch5sc04_061 with dissolve
    ld "*Mwaahh*"
    "Lucid’s warm, rosy lips rest on your forehead as you slowly doze off..."
    #play music darknight_4 fadein 1.0
    stop music fadeout 1.0
    scene black with Dissolve(2)
    #play music relax_1 fadein 1.0
    #stop music fadeout 1.0
    scene ch5sc04_062 with Dissolve(2)
    "When you awaken you find yourself in a new location."
    mct "{i}Ugrh... I’ll never get used to that. Where am I now?{/i}"
    scene ch5sc04_063 with dissolve
    play music relax_1 fadein 1.0
    #stop music fadeout 1.0
    mct "{i}Huh, someone's here? Must be her, Maia.{/i}"
    ####Animation####
    scene maia1 with dissolve
    $ renpy.pause(15.2)
    #$ renpy.pause(6, hard=True)
    scene ch5sc04_064 with dissolve
    mct "It’s her."
    mct "She’s the one Lucid wanted me to speak with."
    scene ch5sc04_065 with dissolve
    $ renpy.pause()
    scene ch5sc04_066 with dissolve
    $ renpy.pause()
    scene ch5sc04_067 with dissolve
    $ renpy.pause()
    scene ch5sc04_068 with dissolve
    mct "Definitely her."
    mct "Everything about her is goddess-like."
    scene ch5sc04_069 with dissolve
    mc "Maia? I’ve come to-"
    scene ch5sc04_070 with dissolve
    mai "Lucid sent you."
    scene ch5sc04_068 with dissolve
    mc "Yes. How did you-"
    scene ch5sc04_070 with dissolve
    mai "Her mischievous scent is all over you."
    scene ch5sc04_071 with dissolve
    mai "Approach and I'll cleanse you."
    mct "{i}*Sigh* Guess I'd better do as she wants. I need her help after all.{/i}"
    scene ch5sc04_072 with dissolve
    "As you approach her, she rests her palm gently below your chin, looking into your eyes."
    mai "There’s no mistaking it, you’re {b}‘his’{/b} son."
    scene ch5sc04_073 with dissolve
    mc "Who are you talking about? Whose son?"
    scene ch5sc04_072 with dissolve
    mai "We've met before..."
    mai "The day you came into this world."
    scene ch5sc04_073 with dissolve
    mc "You... you were there?"
    mc "What? ... How? Why?"
    scene ch5sc04_072 with dissolve
    mai "I was there at the request of your father."
    mai "He wanted me to confirm that you were pure of heart."
    mai "He was pleased when I affirmed that you were the purest soul I’d ever encountered."
    scene ch5sc04_074 with dissolve
    mai "However... Today, standing before me... I sense turmoil in your emotions."
    scene ch5sc04_075 with dissolve
    mai "You are conflicted."
    mai "You seek balance between what must be done, and what is right."
    scene ch5sc04_074 with dissolve
    mai "Whether you'll remain the child that was promised..."
    scene ch5sc04_075 with dissolve
    mai "Or lose yourself to the darkness that enshrouds you... remains to be seen."
    scene ch5sc04_076 with dissolve
    mc "The child that was promised? I don’t follow."
    scene ch5sc04_075 with dissolve
    mai "The child of prophecy."
    mai "The one who is destined to either save the world... or bring about its end."
    scene ch5sc04_076 with dissolve
    mc "That’s ridiculous."
    mc "I’m just here to help my friend."
    scene ch5sc04_072 with dissolve
    mai "Mh-Hm, for now."
    mai "Come, sit with me."
    scene ch5sc04_077 with dissolve
    $ renpy.pause()
    mct "{i}She knows my father... my actual father?{/i}"
    scene ch5sc04_078 with dissolve
    mct "{i}She certainly lives up to being classified as a goddess...{/i}"
    scene ch5sc04_079 with dissolve
    mai "Please, join me."
    mai "We have much to discuss."
    scene ch5sc04_080 with dissolve
    $ renpy.pause()
    scene ch5sc04_081 with dissolve
    $ renpy.pause()
    scene ch5sc04_082 with dissolve
    mc "Where are we?"
    mc "It’s pretty clear we’re not in Lucid’s realm."
    scene ch5sc04_083 with dissolve
    mai "You’re back in Midomir."
    mai "The highlands of Luxeron, to be specific."
    scene ch5sc04_084 with dissolve
    mai "Well, currently we’re floating above the highlands in one of my gardens of purity."
    mc "You don’t have your own realm like Lucid?"
    mai "Heavens! No, only the Divines have that luxury."
    mai "The rest of us have to settle for making Midomir our home."
    scene ch5sc04_083 with dissolve
    mai "We also have access to small pocket realms within the divine realms."
    mai "For example I have several sky-gardens in the High-Heavens."
    mai "I like it here on Midomir though, and it allows me to be closer to my followers."
    scene ch5sc04_082 with dissolve
    mc "Lucid mentioned your worshippers call you ‘Maiden of Purity’?"
    scene ch5sc04_083 with dissolve
    mai "That is one of my titles, bestowed upon me by those who follow my teachings."
    mai "Usually priests, clerics and healers."
    scene ch5sc04_085 with dissolve
    mc "I’ve never really been taught about deities and such."
    mc "Lucid gave me a quick lesson about the divines."
    mc "But nothing about other deities and gods."
    mc "So forgive my ignorance, but how does it work?"
    scene ch5sc04_086 with dissolve
    mai "That is most surprising, given who you are."
    mai "I’m afraid it’s more complicated than one conversation can convey."
    mai "But one of the basics of godhood-"
    scene ch5sc04_087 with dissolve
    mai "-Is that mortals put their faith in us."
    mai "They pray to us, believe in us, and they devote themselves to us."
    scene ch5sc04_086 with dissolve
    mai "In return, we use our powers to bestow our blessings, charms, and good fortune on our worshippers."
    scene ch5sc04_087 with dissolve
    mai "And when the time comes for our devotees to part with this world, we claim their soul."
    scene ch5sc04_088 with dissolve
    mc "Their soul?"
    mc "I’ve absorbed souls before..."
    scene ch5sc04_089 with dissolve
    mai "Yes, you would have."
    mai "Although, we gods are only able to claim the souls of those who belong to our faith."
    scene ch5sc04_088 with dissolve
    mc "Interesting. When I absorb a soul, I feel myself become... more?"
    mc "I'm not exactly sure how to describe it."
    mc "I feel stronger and my senses increase. Sometimes, I even gain new abilities."
    scene ch5sc04_089 with dissolve
    mai "We too grow in power as we gain souls, although we don’t acquire new abilities like you."
    scene ch5sc04_088 with dissolve
    mc "So the more followers a deity has..."
    scene ch5sc04_087 with dissolve
    mai "The stronger they become."
    scene ch5sc04_084 with dissolve
    mc "I see. What happens if a faith dies out?"
    mai "..."
    scene ch5sc04_090 with dissolve
    mai "That... results in the deity perishing. They cease to exist."
    scene ch5sc04_091 with dissolve
    mc "Sorry. I didn’t mean to pry."
    mai "..."
    ###Choice###
    menu:
        "Comfort her.":
            scene ch5sc04_092 with dissolve
            $ renpy.pause()
            scene ch5sc04_093 with dissolve
            $ renpy.pause()
            mc "I know what it's like to lose someone. I won’t press you on the matter."
            mai "I... I appreciate that."
            scene ch5sc04_093a with dissolve
            mct "{i}Woah? This feeling... It's... familiar to me!{/i}"
            mc "Your skin... it’s almost like it’s radiating sunlight."
            scene ch5sc04_093 with dissolve
            $ renpy.pause(1)
            scene ch5sc04_092 with dissolve
            mc "Sorry."
            mai "It’s okay."
            mai "It... it felt pleasant."
            $ maia_trust += 2
            "Maia enjoyed your comfort, her trust has increased by {size=+3}{b}{color=#2bff8b}2{/color}{/b}{/size}."
            mai "Where were we? ... Oh, right."

        "Leave her be.":
            scene ch5sc04_091 with dissolve
            mct "{i}It’s clearly a sore spot for her. I'd better let her gather herself.{/i}"

    scene ch5sc04_090 with dissolve
    mai "*Sigh* You should know these things."
    mai "It’s only happened a handful of times throughout the ages."
    mai "But it’s always a great loss when it happens."
    scene ch5sc04_087 with dissolve
    mai "Let’s change the subject."
    mai "Why have you sought me out?"
    scene ch5sc04_085 with dissolve
    mc "My friend..."
    mc "She recently became a vampire and now her emotions are overwhelming her."
    mc "Lucid said she couldn’t do anything about it."
    mc "But that I could, with your guidance."
    scene ch5sc04_089 with dissolve
    mai "*Sigh* Typical Lucid."
    mai "Leaving it up to others to clean up her mess."
    scene ch5sc04_088 with dissolve
    mc "Please."
    mc "I know I’m asking a lot and that you don’t owe me anything. But it’s important to me."
    scene ch5sc04_085 with dissolve
    mai "Hmh..."
    scene ch5sc04_087 with dissolve
    mai "Alright! Alright..."
    mai "I can’t say no those endearing eyes."
    scene ch5sc04_086 with dissolve
    mai "I’ll help."
    mai "But what you’re asking me to do... what Lucid wants, it hasn't been done before."
    mai "I can’t promise that it'll work."
    mai "And more importantly... you could potentially hurt or even kill your friend trying."
    scene ch5sc04_088 with dissolve
    mc "Kill? What exactly do I need to do?"
    scene ch5sc04_089 with dissolve
    mai "You will have to purify your friend."
    mai "But purification is usually only performed on mortals who are possessed by dark spirits."
    mai "It's not intended for vampires."
    mai "We’ll have to modify the purification so that it is specific to a vampire."
    scene ch5sc04_088 with dissolve
    mc "Sounds simple enough."
    scene ch5sc04_090 with dissolve
    mai "Simple? Altering magic is not something to be taken lightly."
    mai "One error, and things will turn grim real quick."
    mai "When altering magic, it's usually necessary to practice time and again."
    mai "And preferably, test it on several test subjects first."
    scene ch5sc04_086 with dissolve
    mai "I’ll go out on a limb and presume you don’t have a dozen vampires volunteering?"
    scene ch5sc04_085 with dissolve
    mc "*Sigh* Not quite... But I do have a natural affinity for magic."
    mc "Given what's at stake, I will only need one attempt."
    mai "..."
    "The Goddess remains silent as she contemplates how to proceed."
    scene ch5sc04_089 with dissolve
    mai "Lie down."
    scene ch5sc04_088 with dissolve
    mc "What? Right here?"
    mai "*Nods*"
    scene ch5sc04_092 with dissolve
    "She motions for you to rest your head in her lap."
    scene ch5sc04_094 with dissolve
    "As you lean back and rest, she gently runs her hand through your hair and caresses your chest."
    scene ch5sc04_095 with dissolve
    mai "*Soft voice* That’s it, close your eyes and open your other senses."
    scene ch5sc04_094 with dissolve
    mct "I’ve never felt this relaxed before."
    mct "Everything about her presence is soothing."
    scene ch5sc04_095 with dissolve
    mai "*Soft voice* Feel the world around you, let your senses absorb everything."
    scene ch5sc04_094 with dissolve
    mc "*Exhales deeply*"
    scene ch5sc04_095 with dissolve
    mai "*Soft voice* Now, I’ll share some of my essence with you."
    mai "*Soft voice* This will allow you to perform purifying magic."
    mai "*Soft voice* Do you accept this gift? Do you... accept me?"
    scene ch5sc04_094 with dissolve
    mct "For some reason, I trust her. I feel completely at ease in her presence."
    mct "I feel like... I know her somehow? That we're... connected?"
    mct "{i}Lucid wouldn’t have sent me here if I couldn’t trust Maia.{/i}"
    scene ch5sc04_096 with dissolve
    mc "I accept your gift, your guidance... I accept you, Maia."
    scene ch5sc04_097 with dissolve
    mai "*Soft voice* I entrust you with my essence, sacred and pure. May you always use it to protect those in need."
    scene ch5sc04_098 with dissolve
    mai "*Soft voice* Feel it become one with you. Let it merge with every fiber of your being."
    mai "*Soft voice* Rest now... I’ll watch over you now as I did when you were but a child."
    scene black with Dissolve(1)
    scene ch5sc04_099 with Dissolve(1)
    mai "*Humming* Lay down your head and I’ll sing~"
    scene ch5sc04_100 with dissolve
    mai "*Humming* I’ll sing you to sleep... I’ll sing you awake~"
    scene ch5sc04_101 with dissolve
    mai "*Humming* Bless your path ahead~"
    scene ch5sc04_099 with dissolve
    mai "*Humming* Bless you with love that only a mother knows~"
    scene ch5sc04_100 with dissolve
    mai "*Humming* May you fly... Fly far to the fields of fortune~"
    scene ch5sc04_101 with dissolve
    mai "*Humming* May you find all that your heart desires~"
    scene ch5sc04_099 with dissolve
    mai "*Humming* May you find kindness in all who you meet~"
    scene ch5sc04_100 with dissolve
    mai "*Humming* May there always be angels to watch over you~"
    scene ch5sc04_101 with dissolve
    mai "*Humming* To guard you and keep you safe from harm~"
    mai "..."
    scene ch5sc04_102 with dissolve
    mai "My love... My sweet... My everything."
    scene black with Dissolve(1.5)
    scene ch5sc04_102 with Dissolve(2)
    "Several hours later..."
    scene ch5sc04_103 with dissolve
    mct "{i}She's so warm. And gentle.{/i}"
    scene ch5sc04_104 with dissolve
    mc "Hnh... Was I out for long?"
    scene ch5sc04_105 with dissolve
    mai "It’s been a few hours since I shared my essence with you."
    scene ch5sc04_106 with dissolve
    mc "Sorry. I didn’t mean to fall asleep on you like that."
    mc "I just felt so... calm? I don’t know."
    scene ch5sc04_105 with dissolve
    mai "I’ll forgive you."
    scene ch5sc04_106 with dissolve
    mc "Why do I feel so tranquil near you? Is it one of your abilities?"
    mc "I feel completely at peace..."
    scene ch5sc04_105 with dissolve
    mai "I feel it too. It’s exactly the same as when I watched over you as a child."
    mai "I was never allowed to interact with you, but I watched over you for the first five years of your life."
    scene ch5sc04_104 with dissolve
    $ renpy.pause(1.5)
    scene ch5sc04_105 with dissolve
    mai "I watched you grow, explore, learn, play. I..."
    scene ch5sc04_107 with dissolve
    "Maia's expression changes as she cuts herself off."
    mai "..."
    mc "You watched over me for five years? Why did you... stop?"
    scene ch5sc04_108 with dissolve
    mai "Your father."
    mai "He... He forbade me to continue watching over you."
    scene ch5sc04_107 with dissolve
    mc "Why? ... I remember now. Sometime around my fifth birthday... it was the first time I'd felt cold."
    mc "Like... like there was something missing. I didn’t pay much attention to it at the time."
    mc "But now, being close to you... this is the feeling that disappeared back then. A warm, soothing presence."
    scene ch5sc04_108 with dissolve
    mai "My connection to you grew too strong. Your father thought it would be a problem..."
    mai "Thus, the one who had ordered me to look over you... was also the one to take me away."
    scene ch5sc04_107 with dissolve
    mct "{i}My father... He’s the reason I lost that warmth in my life?{/i}"
    mct "{i}Maia is clearly upset about the situation too. She also lost something dear to her that day.{/i}"
    scene ch5sc04_106 with dissolve
    mc "Maia, thank you... for watching over me."
    "As you acknowledge her, her face brightens once more."
    scene ch5sc04_105 with dissolve
    mai "Oh? You don’t have to thank me. I... I just did what was required of me."
    mct "{i}That might have been how it started, but it obviously meant more to her than just a ‘task’.{/i}"
    scene ch5sc04_106 with dissolve
    mc "No matter what you say, I’m still grateful."
    scene ch5sc04_105 with dissolve
    mai "What am I to do with you? You’re not supposed to make a goddess blush..."
    mai "Come, time to get up! I still have to teach you the spell to purify your friend."
    scene black with Dissolve(1)
    scene ch5sc04_109 with Dissolve(1)
    mai "Okay, pay attention now."
    mai "Purifying a person or creature is a demanding process."
    scene ch5sc04_110 with dissolve
    mai "I’ll show you how to create a Purifying sphere. Then it will be your turn to try."
    scene ch5sc04_111 with dissolve
    mai "Like this! You have to gather energy in each of your palms. Then you need to activate it and merge it together between your hands."
    mai "Each purification is unique. That’s what the runes are for, they determine the effect."
    mai "This one will be specific to your situation, purifying a vampire."
    scene ch5sc04_112 with dissolve
    mc "What will this do exactly? Will it remove her vampirism?"
    mai "No. She will remain a vampire, a purified vampire. The only one of her kind."
    scene ch5sc04_109 with dissolve
    mai "Her abilities, strength, speed, everything will remain as before, but it should remove her bloodlust."
    mai "She won’t be controlled by her hunger anymore. But she will still have to drink blood to survive, your blood."
    scene ch5sc04_112 with dissolve
    mc "My blood?"
    mai "As the one who purifies her, it will create an unbreakable link between the two of you."
    mc "What happens if she don't have access to my blood for a while?"
    scene ch5sc04_109 with dissolve
    mai "She will begin to desiccate. It happens to regular vampires as well if they don't feed regularly."
    mai "Basically their bodies shut down slowly, until they finally become immobilized and fall into a deep slumber."
    scene ch5sc04_112 with dissolve
    mc "So if we're apart for a while, it won't kill her?"
    mai "No, she won't die. A desiccated vampire can be awoken by feeding them blood, in her case, your blood specifically."
    mai "Typically the desiccation process takes about a week from the last feeding to begin."
    mct "{i}Hmh, if I have to part with her in the future for more than a week, I'll have to provide her with some vials of my blood.{/i}"
    mct "{i}That way she can continue as normal even if we are seperated for periods of time.{/i}"
    mc "You say my blood specifically?"
    scene ch5sc04_109 with dissolve
    mai "She won't crave mortal blood any more. Her body will reject it even if she tries to consume it."
    mai "The only way for her to survive and gain the nourishment she needs, will be from you."
    mct "{i}I didn’t expect this... It would mean that Eliza won’t have to feel guilty about hurting others anymore.{/i}"
    mct "{i}Feeding from me won’t be an issue, I can easily regenerate. This might work.{/i}"
    scene ch5sc04_112 with dissolve
    mai "I like that look of determination in your eyes. Because now it’s your turn to try."
    mai "It should be rather intuitive for you, now that you've absorbed some of my essence."
    scene ch5sc04_113 with dissolve
    mai "Remember, just let the energy gather in your palms."
    mct "{i}Hmh... I can feel the energy, but nothing seems to be happening.{/i}"
    scene ch5sc04_114 with dissolve
    mai "Trust your instincts."
    mai "When performing purification magic, your mind needs to be in a state of tranquility."
    mai "Search within you for something that brings you serenity."
    scene ch5sc04_115 with dissolve
    mai "Do you feel this?"
    mc "Yes."
    mai "That is the feeling you’re looking for. When you find it, focus on manifesting it."
    scene ch5sc04_116 with dissolve
    "A warm tingling sensation builds between your hands, and Maia bites her lip with anticipation."
    scene ch5sc04_117 with dissolve
    with vpunch
    mai "*Excitedly* Yes! That’s it! Good job!"
    mai "It’s beautiful. I’m so proud of you, sweetie!"
    scene ch5sc04_118 with dissolve
    with vpunch
    mai "I can’t believe you were able to manifest it that quickly!"
    mai "You were just wonderful! You’ve grown up so... so fast."
    scene ch5sc04_119 with dissolve
    mct "{i}She’s hugging me tightly... I’m being hugged by a literal goddess...{/i}"
    mct "{i}She’s not letting go either. Not that I want her to...{/i}"
    scene ch5sc04_120 with dissolve
    $ renpy.pause()
    mai "..."
    mc "I take it I did well?"
    scene ch5sc04_121 with dissolve
    mai "Mhm-Hm... Extraordinarily well! It takes years to learn for even the most gifted clerics and priests!"
    mai "I’m... very impressed."
    scene ch5sc04_120 with dissolve
    mc "Is that why you’re holding on to me so tightly?"
    scene ch5sc04_122 with dissolve
    "Maia realizes she’s been hugging you intimately in her excitement."
    scene ch5sc04_123 with dissolve
    $ renpy.pause(1)
    scene ch5sc04_122 with dissolve
    $ renpy.pause(1)
    scene ch5sc04_123 with dissolve
    $ renpy.pause(1)
    scene ch5sc04_122 with dissolve
    $ renpy.pause(1)
    scene ch5sc04_124 with dissolve
    with vpunch
    mai "{b}HEAVENS!{/b} What am I doing!?"
    mai "P-Please, forgive me. It was highly inappropriate for me to do that!"
    scene ch5sc04_125 with dissolve
    mc "It’s okay, you didn’t do me any harm. It felt nice... You’re incredibly warm."
    mai "..."
    mc "I enjoyed it. If I hadn't, I would've asked you to stop."
    scene ch5sc04_126 with dissolve
    mai "[mc]... Thank you, it’s kind of you to say."
    mai "I... I'd better send you back now. You have everything you need to help your friend."
    scene ch5sc04_125 with dissolve
    mc "Thank you for your guidance, Maia. I hope I haven’t caused you any trouble..."
    scene ch5sc04_126 with dissolve
    mai "You’re welcome. But now, you must leave."
    scene ch5sc04_127 with dissolve
    mai "Here... I’ll make a portal for you."
    scene ch5sc04_128 with dissolve
    with vpunch
    mai "It will take you back to Luxenford."
    scene ch5sc04_129 with dissolve
    mc "Okay... Once more, I apologize for making you feel uncomfortable. That wasn’t my intention."
    scene ch5sc04_130 with dissolve
    $ renpy.pause()
    scene ch5sc04_131 with dissolve
    mai "..."
    mai "You could never make me feel uncomfortable."
    scene ch5sc04_132 with dissolve
    mai "All these years. How you’ve grown... Strong, willful, beautiful."
    mai "*Sighs heavily* Castiel... I won’t forgive this."
    mai "Forcing me to... part with him for the second time."
    scene ch5sc04_133 with dissolve
    mai "..."
    scene black with Dissolve(2)
    #play music explore_1 fadein 1.0
    stop music fadeout 1.0
    scene ch5sc05_001 with Dissolve(1.5)
    play music explore_1 fadein 1.0
    scene ch5sc05_001 with dissolve
    $ renpy.pause()
    scene ch5sc05_002 with dissolve
    $ renpy.pause()
    scene ch5sc05_003 with dissolve
    $ renpy.pause()
    scene ch5sc05_004 with dissolve
    $ renpy.pause()
    scene ch5sc05_004b with dissolve
    uk "Mommy! Look! A man just appeared out of thin air!"
    wo "Sweetie, Mommy doesn’t have time for your fantasies right now."
    scene ch5sc05_005 with dissolve
    mct "{i}Ugh... I feel lightheaded. Don’t imagine I'll be a fan of portals anytime soon.{/i}"
    mct "{i}I'd better go find Eliza. The sooner we attempt this purification, the better.{/i}"
    scene ch5sc05_004 with dissolve
    uk "Mommy! He really is magic! You never believe me!"
    scene ch5sc05_006 with dissolve
    $ renpy.pause()
    scene black with Dissolve(1.5)
    scene ch5sc05_007 with Dissolve(1.5)
    br "Hah! The bugger really said that?"
    ml "He thought I was there to court his daughter, but I was just trying to deliver a package from Sylph."
    br "Hah! And he really chased you all the way into the street?"
    ml "Yeah... I didn't even manage to collect the payment. Fortunately, the daughter caught up to me and paid."
    scene ch5sc05_008 with dissolve
    br "Oi, [mc]! Finally yer here! Heard ye got a fancy shmancy contract guardin t’princess?”"
    scene ch5sc05_009 with dissolve
    mc "Hey guys. I’m afraid the princess is less than thrilled about it."
    mc "Have either of you seen Eliza? I have some news for her."
    scene ch5sc05_008 with dissolve
    br "Aye, the lass was around just a few moments ago."
    br "Maybe she went t' Dalen’s office, or maybe she's helping Sylph sort contracts in the next room?"
    scene ch5sc05_010 with dissolve
    with vpunch
    $ renpy.pause()
    scene ch5sc05_011 with dissolve
    $ renpy.pause()
    scene ch5sc05_012 with dissolve
    with vpunch
    el "*Squeals* Aiiiyh! Y-You knew!?"
    scene ch5sc05_013 with dissolve
    mc "Mh-Hm. I sensed your devious intentions the moment I walked through the door."
    if eliza_path == True:
        scene ch5sc05_012 with dissolve
        el "*Giggles* Oh yeah? Did you also sense this?"
        scene ch5sc05_014 with dissolve
        with vpunch
        el "Mhmm!"
        scene ch5sc05_014 with dissolve
        $ renpy.pause(1)
        scene ch5sc05_015 with dissolve
        $ renpy.pause(1)
        scene ch5sc05_014 with dissolve
        $ renpy.pause(1)
        scene ch5sc05_015 with dissolve
        $ renpy.pause(1)
        scene ch5sc05_016 with dissolve
        bth "......."
        scene ch5sc05_017 with dissolve
        br "C’mon lad, Sylph needed our help with... eh... boxes!"
        ml "R-Right! Barrels! Let’s go."
        scene ch5sc05_015 with dissolve
        $ renpy.pause(1)
        scene ch5sc05_014 with dissolve
        $ renpy.pause(1)
        el "*Softly moans* Nnnhhh... *Kiss* Mwh... *Lick* Nhnh-Mmnh!"
        scene ch5sc05_015 with dissolve
        mct "{i}Heh... I’ve missed you too, kitten.{/i}"
        scene ch5sc05_012 with dissolve
        el "How... How's that for devious intentions?"
        mc "I take it back. Your intentions are pure of heart."
        scene ch5sc05_014 with dissolve
        el "*Mwah!*"
        scene ch5sc05_012 with dissolve
        el "*Giggles softly* Missed you!"
        scene ch5sc05_014 with dissolve
        el "*Mwah!* Sheee... The purest intentions! Mhhm..."
        scene ch5sc05_012 with dissolve
        mc "Speaking of pure, let’s head to the tavern. I’ve learnt something that might help you."

    else:
        scene ch5sc05_012 with dissolve
        el "*Giggles* I have the purest of intentions, I’ll have you know!"
        mc "Speaking of pure, let’s head to the tavern. I’ve learnt something that might help you."

    scene black with Dissolve(1.5)
    scene ch5sc03_113 with Dissolve(2)
    el "Wait... So you’re telling me you spent the day with not one... but TWO goddesses?!"
    scene ch5sc05_018 with dissolve
    mc "I know... It sounds unbelievable."
    scene ch5sc05_019 with dissolve
    el "Yeah... If you weren’t the one telling me directly, I wouldn’t believe it."
    el "How did it even happen? What were they like? Did you learn anything?"
    scene ch5sc05_018 with dissolve
    mc "*Chuckles* Calm down, one question at a time."
    scene ch5sc05_020 with dissolve
    el "Mhph... Okay."
    el "Let’s start with how you managed to meet two... {b}TWO{/b} goddesses?"
    scene ch5sc05_021 with dissolve
    mc "Well, I had the idea to call out to Lucid, given she was the only one I'd met at the time."
    mc "And also because she is the one who created vampires in the first place."
    mc "Of course, I had no idea if it would even work. But seeing the state you were in this morning..."
    scene ch5sc05_022 with dissolve
    mc "I was desperate. It was worth a shot. Next thing I knew, I felt something envelop me."
    mc "It was like a warm blanket, but light as air. I must’ve passed out, 'cause when I awoke I was with Lucid."
    scene ch5sc05_021 with dissolve
    mc "Apparently, she'd heard my plea and decided to transport me to her realm, the Inferno Isles."
    scene ch5sc05_020 with dissolve
    el "A different realm? I... how?"
    scene ch5sc05_021 with dissolve
    mc "I don't know. Let’s just chalk it up to her being an all powerful divine?"
    mc "Whenever I’m around her, I get this weird feeling inside me."
    scene ch5sc05_020 with dissolve
    el "Like what?"
    scene ch5sc05_021 with dissolve
    mc "Like... family?"
    mc "The best way to describe it is how I used to feel when I was at home with my parents."
    scene ch5sc05_020 with dissolve
    el "Really? That is strange."
    el "Do you think... you’re related somehow?"
    scene ch5sc05_023 with dissolve
    mc "I don’t know."
    mc "Anything is possible, I suppose."
    scene ch5sc05_020 with dissolve
    el "Was she able to help?"
    scene ch5sc05_023 with dissolve
    mc "Not exactly."
    mc "She couldn't do anything herself, but she sent me to another goddess, Maia."
    scene ch5sc05_024 with dissolve
    with vpunch
    el "Maia, Maiden of Purity?! Heavens! You’ve actually met her?"
    mc "Judging by your reaction, I assume you know of her?"
    el "Of course! Didn’t you?! She's the goddess of purity, love and fertility!"
    el "Mother often prayed at her shrines in hopes of getting pregnant again."
    scene ch5sc05_025 with dissolve
    "Eliza’s interest has been piqued, and she eagerly awaits the continuation of your story."
    mct "{i}She’s cute when she gets all excited.{/i}"
    scene ch5sc05_026 with dissolve
    mc "Okay. So, Lucid sent me to Maia to receive her guidance."
    scene ch5sc05_025 with dissolve
    mc "She was surprisingly welcoming."
    mc "I don’t know what I expected... maybe I imagined she'd be more aloof?"
    scene ch5sc05_026 with dissolve
    mc "But as soon as we started talking, I could sense she was genuinely filled with a warm kindness."
    scene ch5sc05_025 with dissolve
    mc "It turns out, she'd been watching over me from when I was born."
    mc "At the behest of my father, apparently."
    scene ch5sc05_027 with dissolve
    el "Y-Your father? Your angel-father?"
    scene ch5sc05_026 with dissolve
    mc "Yeah... Apparently she was supposed to keep an eye out for any signs of darkness within me."
    scene ch5sc05_025 with dissolve
    mc "But around my fifth birthday, he ordered her to stop watching over me."
    scene ch5sc05_027 with dissolve
    el "W-What?! Why?"
    el "That doesn't seem right."
    scene ch5sc05_028 with dissolve
    mc "She wouldn’t say... But I could feel the heaviness of her emotions when she told me."
    scene ch5sc05_027 with dissolve
    el "Well, yeah. Think about it. If she'd been watching over you since your birth..."
    el "She had probably developed some sort of motherly bond with you, no?"
    scene ch5sc05_028 with dissolve
    mc "Hmh... I didn't think of that."
    mc "But we’re getting off-topic."
    mc "After talking for a while, she shared some of her essence with me."
    mc "She wanted me to be able to perform purification magic."
    mc "And apparently, having her essence makes this much easier."
    scene ch5sc05_027 with dissolve
    el "You have the essence of a goddess within you now?"
    el "T-That’s... wild."
    scene ch5sc05_026 with dissolve
    mc "Just a small amount. It helped me to attune to her purification magic in minutes."
    scene ch5sc05_025 with dissolve
    mc "Even she was surprised. She said it takes even her most devout worshippers years to do."
    scene ch5sc05_029 with dissolve
    el "Well... you are pretty amazing."
    scene ch5sc05_021 with dissolve
    mc "Heh, thanks. It’s always been easy for me to learn magic, even when I don’t fully understand it."
    mc "It’s like my body attunes itself to different types of magic quickly. And then I can intuitively use that magic."
    scene ch5sc05_022 with dissolve
    el "That’s how you were able to learn wind magic from Rin, right?"
    mc "Yeah. She was quite surprised when I manifested wind during our first session."
    scene ch5sc05_024 with dissolve
    with vpunch
    el "Rin!! I completely forgot to tell you! I met her! Me and Borri, when you were gone at sea."
    el "I'm so sorry! I-I completely forgot all about it!"
    scene ch5sc05_021 with dissolve
    mc "Rin's here? In the capital?"
    el "*Nods*"
    mc "That's curious. Her village, Nakajima and family are located far from civilization."
    mc "Deep within the Sen'ju region."
    scene ch5sc05_027 with dissolve
    el "You're not mad at me?"
    scene ch5sc05_028 with dissolve
    mc "Mad at you? For forgetting that you met someone in the midst of everything that's been going on?"
    mc "Of course I'm not mad at you..."
    mc "If Rin is really here In Luxenford, I'm sure we'll run into her."
    scene ch5sc05_029 with dissolve
    el "Okay... Phew!"
    el "I was worried you'd be angry with me."
    scene ch5sc05_020 with dissolve
    el "So, why did you need to learn purification magic?"
    el "I’m sure it’s great, but what does it have to do with our situation?"
    scene ch5sc05_023 with dissolve
    mc "I need it to purify you."
    mc "Maia deemed this to be our best option, since there's no way to cure vampirism."
    scene ch5sc05_024 with dissolve
    el "Purify me? What does that mean?"
    el "If it can’t cure me, what will it do? Will it hurt?"
    scene ch5sc05_028 with dissolve
    mc "The way I understood it, is that it will modify the vampiric cells in your body."
    mc "You'll stop craving blood from mortals and your bloodlust will be gone."
    scene ch5sc05_027 with dissolve
    el "That sounds... almost too good to be true."
    el "How can I be a vampire, but not need blood?"
    scene ch5sc05_028 with dissolve
    mc "You will still need blood... mine."
    scene ch5sc05_024 with dissolve
    el "Yours?!"
    el "You’re okay with that?"
    scene ch5sc05_025 with dissolve
    mc "Of course I am. I'd do anything for you."
    mc "If drinking my blood means you get to live without guilt..."
    mc "Or having to worry about hurting someone because of the craving..."
    scene ch5sc05_026 with dissolve
    mc "Then that's a price I'll pay any day."
    scene ch5sc05_022 with dissolve
    el "So to summarize. I'll still be a pureblood vampire, just like before, but without the bloodlust?"
    el "I'll still have my strength, speed, and senses? And eternal youth?"
    scene ch5sc05_021 with dissolve
    mc "You'll remain as you are right now, beautiful and fierce."
    elt "Heavens! I feel like I'm going to melt when he looks at me so directly..."
    scene ch5sc05_020 with dissolve
    el "The only major change is that I will need your blood instead of regular blood?"
    scene ch5sc05_023 with dissolve
    mc "Yeah, Maia said that if you try to ingest the blood of mortals after being purified, your body will reject it."
    mc "And it should also remove your bloodlust, even if you haven't fed in a while."
    scene ch5sc05_029 with dissolve
    el "Drinking your blood does sound much more appealing, if I’m honest."
    scene ch5sc05_026 with dissolve
    mc "*Chuckles* Easy, kitten, better withdraw your fangs until after we purify you."
    scene ch5sc05_020 with dissolve
    el "How do we do it? Can we do it here? Now?"
    scene ch5sc05_018 with dissolve
    mc "We'll do it now, but first I want to be clear, there's no certainty doing this."
    mc "I was warned that it could hurt you or possibly kill you."
    scene ch5sc05_020 with dissolve
    el "So I just lie down and we'll begin?"
    scene ch5sc05_021 with dissolve
    mc "Eliza... This is serious."
    scene ch5sc05_022 with dissolve
    el "I'm not worried in the slightest. First of all, you're amazing and if you didn't belive this would work-"
    el "Then you would never even suggest it. Secondly, I believe in you and your ability to make it happen."
    el "Thirdly, if this means I can get my life back, that I get to live a normal life again?"
    el "Then that is something I'm willing to risk my life for."
    scene ch5sc05_022 with dissolve
    mc "Stubborn as usual I see."
    scene ch5sc05_029 with dissolve
    el "You know it better than anyone, so you better stop arguing and get to work!"
    scene ch5sc05_021 with dissolve
    mc "*Sigh* Yeah. The sooner we get on with it, the better. Lie down and we’ll begin."
    scene ch5sc05_022 with dissolve
    el "O-Okay. Is what I’m wearing fine? Or should I be... you know... nude?"
    mc "Let’s go with nude."
    mc "We don’t want your clothes interfering with the magic."
    scene ch5sc05_029 with dissolve
    el "No... we certainly don’t! *Smirks*"
    el "How do you want me?"
    scene ch5sc05_026 with dissolve
    mc "On your back, legs straight and arms by your side."
    elt "Mhm... I could get used to him ordering me around like that."
    #play music darknight_4 fadein 1.0
    stop music fadeout 1.0
    scene black with dissolve
    "Eliza removes her clothes and follows your instructions."
    play music forest_1 fadein 1.0
    #stop music fadeout 1.0
    scene ch5sc05_030 with dissolve
    el "I’m nervous... Just a little bit."
    mc "Don’t be. I won’t let anything bad happen to you."
    scene ch5sc05_031 with dissolve
    el "Promise?"
    scene ch5sc05_032 with dissolve
    mc "Promise."
    mc "According to Maia, nothing like this has ever been attempted before."
    mc "So, I can’t know how it will feel or if it hurts. Just, be brave for me?"
    scene ch5sc05_031 with dissolve
    el "O-Okay... I’ll try. For you."
    scene ch5sc05_033 with dissolve
    el "I trust you."
    el "Even if it hurts... just keep going. I want this. I need this."
    scene ch5sc05_034 with dissolve
    el "T-That tickles! *Giggling*"
    scene ch5sc05_035 with dissolve
    mc "Sorry. I need to keep my hands close to your skin so that I can tell whether the magic is taking effect."
    if eliza_path == True:
        scene ch5sc05_034 with dissolve
        el "It’s okay, I like having them on me... a lot."
        el "I always feel safe with you."
    else:
        scene ch5sc05_034 with dissolve
        el "It’s okay. I trust you."

    scene ch5sc05_035 with dissolve
    mc "Here goes..."
    "You begin focusing your energy into the palm of your right hand."
    scene ch5sc05_036 with dissolve
    with vpunch
    el "*Moans* {b}Ahhh!{/b}"
    el "*Gasps* Heavens! That... feels funny!"
    mct "{i}At least we know she’s not in pain ...{/i}"
    mct "{i}I’ll use both hands then.{/i}"
    scene ch5sc05_037 with dissolve
    with vpunch
    el "*Moans* {b}OOHHH! NNNHH!{/b} T-That’s warm! Sooo... warm."
    scene ch5sc05_038 with dissolve
    el "*Moans* Aiiyh! W-What is that? {b}AHH! MMNHH{/b}... It feels so... intense!"
    scene el_sleep5 with dissolve
    mc "This? This is just me focusing the purification for maximum effect."
    el "*Moans* Yes! Ahhhnhh... I feel it! [mc]! I feel it!"
    el "*Moans* It’s... AHH! It’s like you’re massaging my breast! MMNH-AHH!"
    mc "I promise I’m not touching... The magic is just doing it’s thing."
    el "*Moans* F-Fuuck! Keep doing that! {b}Ah-MHH!{/b}"
    mct "{i}Damn, she’s really enjoying it... Too bad it’s already done.{/i}"
    ####Choice####
    menu:
        "Keep purifying her breast until she orgasms. ({color=#ff8cdd}Romance{/color})":
            scene ch5sc05_038 with dissolve
            mct "I'd be lying if I said this isn’t a huge turn on, seeing her this blissful."
            $ eliza_path = True
            scene el_sleep5 with dissolve
            mc "Kitten, this will be a little intense. I’m going to thoroughly purify your breast."
            el "Y-Yes! Please... Mhhh!!"
            scene el_sleep6 with dissolve
            el "*Soft moan* G-Gentle... Ahhm! The way... the magic is brushing against my nipple- Ahhh-AH!"
            el "*Moans* {b}Y-YES!{/b} Ahhhh... Pl-Please do it! I’m at your mercyyyy!"
            el "*Moans* Mhh-Purify me! Ahh-Ahh! Yes... [mc]..."
            scene el_sleep5 with dissolve
            el "{b}*Moans* OH!! [mc]! YES!!{/b} I feel it! I feel you! {b}AHHHHHHH!{/b}"
            with vpunch
            el "{b}*Moans* Aiiiyhh!! YES!!!{/b}"
            with vpunch
            scene ch5sc05_038 with dissolve
            el "*Panting heavily* That was... incredible! I-I feel so refreshed!"
            scene ch5sc05_037 with dissolve
            mc "Good. We’re done, so just rest up. Once you wake up, everything will be better."
            scene ch5sc05_035 with dissolve
            el "I... I lov-... ZzZz... Yuhh..."
            scene ch5sc05_039 with dissolve
            mc "Sweet dreams, kitten. I'll head to the guild for a bit. Just rest up."
            el "*Mumbling* Mnhh... Ohkayh... Nnghh..."
            scene black with Dissolve(2)

        "Stop and move on. ({color=#2bff8b}Friendship{/color})":
            scene ch5sc05_038 with dissolve
            mc "Okay, let’s give your breast a rest. You’re almost done."
            scene ch5sc05_037 with dissolve
            el "*Panting* Pheew... That was... wild."
            el "I feel so... S-So... tire... tired."
            scene ch5sc05_035 with dissolve
            mc "Rest up. When you wake up, everything will be better."
            scene ch5sc05_039 with dissolve
            mc "I'm heading to the guild for a bit. You just rest."
            el "*Whoozy* Ooohkaay... resst... ZzzZz."
            scene black with Dissolve(2)

    scene black with dissolve
    #play music darknight_4 fadein 1.0
    stop music fadeout 1.0
    scene ch4sc06_001a with Dissolve(2)
    play music explore_1 fadein 1.0
    #stop music fadeout 1.0
    scene ch4sc06_001a with dissolve
    evr "*Laughter*"
    al "Flynn! That didn’t happen!"
    br "Aye! There’s no such thing as a deck-captain!"
    fy "I’m telling you, guys! They entrusted me with the safety of the entire ship!"
    scene ch4sc06_002a with dissolve
    fy "If it hadn’t been for me, the deck-captain, there’s no telling what would’ve happened that day."
    fy "The seas were rough like never before. The winds blew through our sails like a hurricane!"
    fy "We were surrounded by enemies on all fronts, but I kept calm and held my ground!"
    evr "*Laughing*"
    scene ch4sc06_001a with dissolve
    fy "Arh... My tales of heroism are wasted on you guys!"
    fy "I’ll save 'em for those who truly appreciate them."
    scene ch4sc06_003a with dissolve
    al "Would those happen to be the wenches at the tavern who have no choice but to listen as they pour your ale?"
    scene ch4sc06_002a with dissolve
    fy "Bah! You jest only because you haven’t seen any real adventure yet, sweet Alice."
    scene ch4sc06_004a with dissolve
    fy "[mc]! There you are!"
    fy "Come, tell these nonbelievers that I was, in fact, deck-captain of the Bloody Banshee!"
    scene ch4sc06_005a with dissolve
    mc "I’m afraid that Flynn speaks the truth."
    mc "Kira herself promoted him. He's the only deck-captain anywhere on the Cerulean sea."
    scene ch4sc06_001a with dissolve
    fy "See! I told you guys, true story!"
    evr "*Laughing*"
    scene ch4sc06_005a with dissolve
    mc "So, what is everyone doing here?"
    mc "Thought you’d be busy at the Seafarers Guild, Flynn."
    scene ch4sc06_006a with dissolve
    mc "And Alice? I thought you’d be neck deep in your studies."
    scene ch4sc06_004a with dissolve
    fy "It’s true."
    fy "There's much to do for a renowned seafarer such as myself, but I was asked to come."
    scene ch4sc06_007a with dissolve
    al "Sylph asked us all to meet here."
    al "She wouldn’t say what it's about... which only piqued my curiosity!"
    scene ch4sc06_008 with dissolve
    sy "Ah, [mc]! You’re here, great!"
    sy "Saves me the trouble of sending one of them to fetch you."
    scene ch4sc06_009 with dissolve
    mc "Isn’t it quite late to be gathering everyone?"
    mc "What are you up to, Sylph?"
    scene ch4sc06_010 with dissolve
    al "Yeah. Spill the beans already, Sylph!"
    al "You refused to say anything until [mc] got here."
    menu:
        "Grab Alice’s ass. ({color=#ff8cdd}Romance{/color})":
            scene ch4sc06_011a with dissolve
            $ renpy.pause()
            scene ch4sc06_011b with dissolve
            al "*Whispers* {size=-10}{b}W-What are you doing?!{/b}{/size}"
            scene ch4sc06_011c with dissolve
            mc "*Whispers* {size=-10}{b}Touching your cute little ass.{/b}{/size}"
            scene ch4sc06_011b with dissolve
            al "*Whispers* {size=-10}{b}S-Stop it! *Gasps* Mnhh! It’s way too risky!{/b}{/size}"
            scene ch4sc06_011c with dissolve
            mc "*Whispers* {size=-10}{b}The way you're leaning back into my hand says something different.{/b}{/size}"
            mc "*Whispers* {size=-10}{b}You're quite the handful, Alice.{/b}{/size}"
            scene ch4sc06_011b with dissolve
            al "*Whispers* {size=-10}{b}Mnhh... You're... Bad, mhh.{/b}{/size}"
            scene ch4sc06_011c with dissolve
            mc "*Whispers* {size=-10}{b}Your body knows what it wants.{/b}{/size}"
            mc "*Whispers* {size=-10}{b}Your ass fits perfectly in my hand... So perky and firm.{/b}{/size}"
            scene ch4sc06_011b with dissolve
            al "*Whispers* {size=-10}{b}Ahh... D-Don’t... Say such... lewd things.{/b}{/size}"
            $ alice_path = True
            scene ch4sc06_011c with dissolve
            $ renpy.pause(1)
            scene ch4sc06_011b with dissolve
            $ renpy.pause(1)
            scene ch4sc06_011c with dissolve
            $ renpy.pause(1)
            scene ch4sc06_011b with dissolve
            $ renpy.pause(1)
            $ alice_trust += 2
            "Alice enjoyed being groped by you, her trust has increased by {size=+3}{b}{color=#2bff8b}5{/color}{/b}{/size}."


        "Don't (Neutral)":
            scene black with dissolve

    scene ch4sc06_011 with dissolve
    fy "I must say, I’m intrigued. What do you have for us, little fae?"
    scene ch4sc06_012 with dissolve
    sy "Little fae? Hnnrh... I’m not little. I’m... I’m fun-sized!"
    scene ch4sc06_013 with dissolve
    br "Aye, don’t listen te this bugger. Yer perfectly sized, lass!"
    scene ch4sc06_014 with dissolve
    sy "Hnngh!"
    fy "Please forgive me, Sylph. When I called you little, I really meant cute!"
    fy "You’re the most beautiful fae I’ve ever seen!"
    scene ch4sc06_015 with dissolve
    sy "I’m the only fae you’ve ever seen!"
    scene ch4sc06_016 with dissolve
    evr "*Laughing*"
    fy "Tiny detail! ... *Chuckles* Alright, you got me there!"
    scene ch4sc06_017 with dissolve
    sy "*Laughs* Heh-heh-heh!"
    scene ch4sc06_018 with dissolve
    sy "So! Are you guys ready to be amazed?"
    sy "My reveal is sure to dazzle your pants off!"
    scene ch4sc06_019 with dissolve
    fy "You bet we are!! Dazzle us!"
    scene ch4sc06_018 with dissolve
    sy "*Excitedly* Four words!"
    scene ch4sc06_020 with dissolve
    sy "Grand Eggtastic Scavenger hunt!"
    sy "Or, as I’ve so cleverly dubbed it, the Great Eggathlon!"
    scene ch4sc06_010 with dissolve
    al "A scavenger hunt? What are we looking for?"
    scene ch4sc06_020 with dissolve
    sy "Eggs! Enchanted eggs, to be specific!"
    sy "So if you think you can just bring any regular egg... {b}WRONG!{/b}"
    scene ch4sc06_021 with dissolve
    fy "*Heavy sigh* There goes my plan..."
    scene ch4sc06_009 with dissolve
    mc "Sylph... you really brought us here to search for eggs?"
    scene ch4sc06_022 with dissolve
    al "Oh c’mon! It’ll be fun!"
    al "Just like how we used to search for oddly shaped pine cones when we were young!"
    scene ch4sc06_011 with dissolve
    fy "Oh yeah!"
    fy "I remember this one pine cone that looked like my balls! Perfectly round!"
    scene ch4sc06_016 with dissolve
    evr "*Laughs*"
    scene ch4sc06_017 with dissolve
    sy "That’s... certainly interesting! But hopefully these won’t look anything like... your balls."
    scene ch4sc06_011 with dissolve
    fy "Why do you look so disappointed, Sylph?"
    scene ch4sc06_015 with dissolve
    with vpunch
    sy "Say that one more time and I'll give you actual pine cone balls!"
    fy "*Gulps* S-Sorry!"
    scene ch4sc06_018 with dissolve
    sy "So... Whaddya say?"
    sy "Are you guys up for putting your adventuring skills to the test?"
    scene ch4sc06_019 with dissolve
    fy "You'd better believe it! I’m great at finding things!"
    ml "Sure, sounds fun!"
    scene ch4sc06_023 with dissolve
    br "Aye... Sounds like a fun outing!"
    sy "I know, right? It’s been a yearly tradition in our guild since we founded it!"
    scene ch4sc06_022 with dissolve
    al "I call dibs on [mc]! We’ll be the best team!"
    scene ch4sc06_020 with dissolve
    sy "Sorry, Alice. But there aren't any teams."
    scene ch4sc06_018 with dissolve
    sy "This is a solo endeavor."
    sy "Each of you will have to find your own enchanted egg."
    scene ch4sc06_019 with dissolve
    fy "What happens if we find someone else’s egg?"
    scene ch4sc06_020 with dissolve
    sy "You’ll be electrocuted!"
    scene ch4sc06_015 with dissolve
    with vpunch
    sy "So don’t even think about any funny business!"
    scene ch4sc06_021 with dissolve
    fy "Yikes. She’s pretty scary for such a small thing."
    scene ch4sc06_023 with dissolve
    br "Lass, how do we know which egg is ours?"
    sy "The likelihood of you finding someone else’s egg is incredibly low."
    sy "You'll each be given your own clue-"
    scene ch4sc06_020 with dissolve
    sy "-Which is specific to your egg only."
    scene ch4sc06_010 with dissolve
    al "Since this is a scavenger hunt... will there be prizes?"
    scene ch4sc06_011 with dissolve
    fy "Oh, please say it’s a full evening ticket to ‘The Velvet Pearl’ or ‘Midnight’s Delights’!"
    scene ch4sc06_015 with dissolve
    sy "Keep dreaming, junior!"
    sy "There won’t be any midnight delights or velvet pearls when I’m through with you."
    scene ch4sc06_016 with dissolve
    fy "I was merely jesting..."
    evr "*Laughs*"
    scene ch4sc06_018 with dissolve
    sy "Yes, there will be prizes for anyone who finds their egg. It’s not a race either."
    sy "All that matters is that you find your egg, and bring it back here before dawn for your reward."
    scene ch4sc06_020 with dissolve
    sy "Okay. One by one, speak with me at the door as you leave and I’ll give you your clue!"
    scene black with dissolve
    scene ch4sc06_024 with dissolve
    sy "*Inaudible whisper*"
    scene ch4sc06_025 with dissolve
    sy "*Inaudible whisper*"
    scene ch4sc06_026 with dissolve
    al "*Whispers* {size=-10}{b}I’ll wait for you outside, okay?{/b}{/size}"
    scene ch4sc06_027 with dissolve
    mc "*Whispers* {size=-10}{b}We aren’t allowed to work together.{/b}{/size}"
    scene ch4sc06_026 with dissolve
    al "*Whispers* {size=-10}{b}I know, but I have something I want to show you.{/b}{/size}"
    scene ch4sc06_028 with dissolve
    sy "*Inaudible whisper*"
    scene ch4sc06_029 with dissolve
    sy "Okay, your clue is..."
    scene ch4sc06_030 with dissolve
    sy "I rest near the sky but I'm afraid of heights-"
    sy "Come rescue me, oh great adventurer, before a gust of wind claims me."
    scene ch4sc06_031 with dissolve
    mc "You really put a lot of effort into this, huh?"
    syt "{i}He... He noticed?{/i}"
    scene ch4sc06_032 with dissolve
    sy "Sure did! I’m thrilled beyond belief that we're able to continue our traditions with you guys!"
    scene ch4sc06_029 with dissolve
    sy "Things were looking mighty grim at the start of the year, but then you guys came along."
    scene ch4sc06_032 with dissolve
    sy "And now, look at how our little family has grown!"
    sy "The guild is prosperous for the first time in a long time!"
    sy "We’ve all come together and put in a lot of work, I’m... I’m really glad you’re back."
    scene ch4sc06_033 with dissolve
    sy "I should have said that the moment you got back."
    sy "Let’s talk once you find the egg? Just the two of us."
    scene ch4sc06_031 with dissolve
    mc "Let’s do that."
    mc "We’re overdue for some one on one time."
    scene ch4sc06_033 with dissolve
    sy "Yes!! I’d like that very much!"
    scene ch4sc06_032 with dissolve
    sy "Now, go find your egg!"
    sy "And I'll make sure to have your reward ready for you."
    scene black with Dissolve(1.5)
    #play music darknight_4 fadein 1.0
    stop music fadeout 1.0
    scene ch4sc06_034 with Dissolve(1.5)
    play music explore_2 fadein 1.0
    #stop music fadeout 1.0
    $ renpy.pause()
    scene ch4sc06_035 with dissolve
    mc "There you are."
    mc "What did you want to show me?"
    scene ch4sc06_036 with dissolve
    al "I won’t be able to show you here. Come with me?"
    scene ch4sc06_037 with dissolve
    mc "Consider me intrigued..."
    scene ch4sc06_038 with dissolve
    al "..."
    mc "I remember that look."
    mc "You’re up to something mischievous."
    scene ch4sc06_039 with dissolve
    al "It’s better if I just show you... let’s go!"
    scene ch4sc06_040 with dissolve
    mc "Where are we going, Alice? Sylph said we have to find the eggs before dawn..."
    al "Exactly! That leaves us with plenty of time for a little detour!"
    scene ch4sc06_041 with dissolve
    mct "{i}Her hand is a little sweaty, is she... nervous?{/i}"
    mct "{i}We held hands so often when we were younger... this feels different.{/i}"
    scene ch4sc06_040 with dissolve
    mc "Okay, lead on."
    al "Don’t worry. It’s going to be awesome! You’ll see!"
    #play music feels_1 fadein 1.0
    stop music fadeout 1.0
    scene black with Dissolve(1.5)
    scene ch5sc03_147 with Dissolve(1.5)
    play music forest_1 fadein 1.0
    #stop music fadeout 1.0
    $ renpy.pause(1.5)
    scene ch4sc06_042 with dissolve
    al "Tadaa! What do you think?"
    mc "It’s a nice room... But why are you showing me a room at the academy?"
    scene ch4sc06_043 with dissolve
    al "Guess! *Giggles softly*"
    scene ch4sc06_044 with dissolve
    mc "Wait... Don’t tell me this is-... {b}YOUR ROOM?{/b}"
    scene ch4sc06_045 with dissolve
    al "Winner, winner! Someone buy this man a fancy dinner!"
    al "Isn't it great? It's all mine!"
    scene ch4sc06_046 with dissolve
    with vpunch
    mc "Alice! This is amazing! I’m... I’m happy for you!"
    al "*Giggling* Aiiih! [mc]! Careful, hahaha!"
    scene ch4sc06_047 with dissolve
    mc "But... how? There’s no way you can afford this?"
    scene ch4sc06_048 with dissolve
    al "My professor, Miss Venetos, she promoted me to assistant student and arranged for me to get this room."
    al "Pretty cool, huh?"
    scene ch4sc06_049 with dissolve
    mc "Yeah. I’m proud of you, Alice. Your hard work is paying off."
    al "..."
    al_t "{i}I love being in his arms like this...{/i}"
    scene ch4sc06_050 with dissolve
    al "Maybe... I could get a reward? You know, for doing so well?"
    scene ch4sc06_051 with dissolve
    mc "You’ve definitely earned it. What would you like?"
    al "......"
    scene ch4sc06_050 with dissolve
    al "*Blushing* A... kiss?"
    ####Choice####
    menu:
        "Kiss her lips. ({color=#ff8cdd}Romance{/color})":
            scene ch4sc06_047 with dissolve
            mc "Come here you little cutie."
            $ alice_path = True
            scene ch4sc06_047a with dissolve
            al "MMhhh-... Mh-Mh!"
            mct "{i}Her lips are made for kissing... large and perfectly soft.{/i}"
            scene ch4sc06_047b with dissolve
            al "Ahmmm... Mmhh... *Muuawh*"
            mct "{i}She’s so eager... I guess she was hoping I’d kiss her on the lips.{/i}"
            scene ch4sc06_047 with dissolve
            al "Yum!"
            mc "Happy with your reward?"
            al "I think we both know the answer... Come, you have to try the bed!"
            scene ch4sc06_047c with dissolve
            mc "Alright. But first ... *Mwah*"
            al "*Giggles* H-Hey that tickles!"
            $ alice_trust += 5
            "Alice's trust has increased by {size=+3}{b}{color=#2bff8b}5{/color}{/b}{/size}."
            scene black with Dissolve(1)

        "Kiss her cheek. ({color=#2bff8b}Friendly{/color})":
            scene ch4sc06_047c with dissolve
            mc "*Kiss*"
            al "*Giggles* H-Hey that tickles!"
            al "Let’s lie down on my bed! You have to feel how soft it is!"
            scene black with Dissolve(1)

    scene ch4sc06_052 with Dissolve(1)
    al "Ahhh... Isn’t this bed amazing?"
    scene ch4sc06_053 with dissolve
    mc "Sure, it’s pretty comfortable."
    mc "But size-wise... well, I’m halfway off the bed."
    scene ch4sc06_052 with dissolve
    al "Pish-Posh! It could easily fit two people!"
    scene ch4sc06_053 with dissolve
    mc "*Chuckles* Suuuure! I bet it doesn’t even fit you and your tiny bum."
    mc "You'll probably end up on the floor half the time."
    scene ch4sc06_054 with dissolve
    with vpunch
    al "H-Hey! Take that back!"
    al "Insulting my lovely bed {b}WHILE{/b} lying on it? Meanie!"
    scene ch4sc06_055 with dissolve
    mc "Why would I take it back? I’ve only spoken the truth! *Chuckles*"
    scene ch4sc06_056 with dissolve
    with vpunch
    al "Okay! That’s it, mister! You’ve asked for it!"
    al "You’ve clearly forgotten that I was the uncrowned tickle champion back in Riverside!"
    scene ch4sc06_057 with dissolve
    al "And there will be no mercy for anyone who insults my precious bed!"
    al "Not even childhood friends!"
    mc "*Chuckles* Heyyy! Hahah! Don’t! hahah-"
    scene ch4sc06_058 with dissolve
    al "How do you like that? {b}HMM?{/b}"
    scene ch4sc06_057 with dissolve
    al "Say you’re sorry! I'm not getting off until you apologize! *Tickles*"
    scene ch4sc06_058 with dissolve
    mc "*Laughs* Sorry for what? Speaking the truth?! Hahaha!"
    scene ch4sc06_057 with dissolve
    al "Your truth is a big fat lie!"
    al "*Giggles* And you'd better gobble it right up!"
    scene ch4sc06_058 with dissolve
    mct "{i}With the way she’s wiggling on me, I’ll end up with a raging erection...{/i}"
    scene ch4sc06_057 with dissolve
    mct "{i}Better apologize before she notices.{/i}"
    scene ch4sc06_058 with dissolve
    mc "Alright! Alright! You win! Hahah! I’m sorry I called your bed tiny."
    scene ch4sc06_059 with dissolve
    al "I knew you'd see reason."
    al "Even if it took a little convincing."
    scene ch4sc06_060 with dissolve
    mc "I forgot how ruthless you can be. You really showed me no mercy."
    al "*Snickers* Heheh."
    mct "{i}She’s really grown into a beautiful woman...{/i}"
    scene ch4sc06_061 with dissolve
    al "Do I have something on my face? You’re staring..."
    ####Choice####
    menu:
        "Just admiring your beauty. ({color=#ff8cdd}Romance{/color})":
            scene ch4sc06_060 with dissolve
            $ alice_trust += 3
            mc "Just enjoying the sight of the beautiful girl who’s lying on top of me."
            "Alice's feelings for you grows with every moment and compliment, her trust has increased by {size=+3}{b}{color=#2bff8b}3{/color}{/b}{/size}."
            scene ch4sc06_061 with dissolve
            al "Oh yeah?"
            al "She must be quite the looker if you're the one admiring her."
            $ alice_path = True
            scene ch4sc06_062 with dissolve
            $ renpy.pause()
            scene ch4sc06_063 with dissolve
            $ renpy.pause()
            mc "Mhm... There’s a lot to admire."
            mc "Like this perfect, shapely little ass of yours."
            al "Ahnngh... I feel your admiration... Nngh."
            al "W-What else do you admire?"
            scene ch4sc06_060 with dissolve
            mc "I admire your oak brown eyes whenever I catch them looking in my direction."
            scene ch4sc06_061 with dissolve
            al "Heh-Heh... They tend to do that often..."
            scene ch4sc06_060 with dissolve
            mc "Mhm... I’ve noticed."
            mc "Let’s not forget your lips... So-"
            scene ch4sc06_064 with dissolve
            al "..."
            #play music darknight_4 fadein 1.0
            stop music fadeout 1.0
            scene ch4sc06_065 with dissolve
            al "*Mwah* Mnh-mhhh..."
            play music lewd_1 fadein 1.0
            #stop music fadeout 1.0
            scene al_lewd2 with dissolve
            "While you attempt to finish praising her, she kisses you repeatedly."
            "And holds your hand behind your head while she caresses your chest with the other."
            "Soft gentle lips press and move against yours, again and again."
            al "*Sucking* Mnnhhhh..."
            mc "So tasty... Mh."
            mc "So soft..."
            al "*Kiss* Mmnghh! *Suck* Ahnngh!"
            mc "Like they were made for me... Mhh."
            al "*Kiss* Th-They... Mnnhh! Arrhh youurs... Mnghh *Suck*"
            mct "{i}I love how she kisses me so eagerly. So warm and full of longing.{/i}"
            mct "{i}Every touch of her wet lips, every time our tongues entwine, the hungry suction of her mouth...{/i}"
            mct "{i}She loves me deeply.{/i}"
            al "*Suck* Mmnhh! [mc]-... Ahhhh... *Kiss* I- I want you to- Mnngh... See me..."
            scene ch4sc06_066 with dissolve
            al "*Heavy breathing* Do you... do you want to see?"
            mc "You mean...?"
            scene ch4sc06_065 with dissolve
            $ renpy.pause(1)
            scene ch4sc06_066 with dissolve
            al "Yes, naked."
            scene ch4sc06_065 with dissolve
            $ renpy.pause(1)
            scene ch4sc06_066 with dissolve
            mc "I want to see you, Alice."
            scene ch4sc06_065 with dissolve
            al "*Kiss* Nngh..."
            scene ch4sc06_066 with dissolve
            al "O-Okay... I’ll let you see me. All of me."
            scene ch4sc06_065 with dissolve
            mc "*Kiss* Mhm..."
            scene ch4sc06_066 with dissolve
            mc "Go... My eyes won’t waver."
            al "*Panting* They'd better not..."
            scene black with dissolve
            scene ch4sc06_067 with Dissolve(1)
            al "Stay put! I won’t take long..."
            mct "{i}Heh... She looks good on top of me.{/i}"
            scene ch4sc06_068 with dissolve
            al "Are you... looking?"
            mc "Mhm-Hm."
            al "G-Good!"
            scene ch4sc06_069 with dissolve
            al "Hnngh!"
            mct "{i}It’s been a long time coming... Yet, it feels exciting to watch her undress herself for me.{/i}"
            scene ch4sc06_070 with dissolve
            mc "Alice ... Are you sure you don’t need my help with that?"
            al "*Giggles* I’m quite sure. Tempting as that sounds. Just lie back and watch me."
            scene ch4sc06_071 with dissolve
            mc "Mhm... You're stunning."
            mc "Have I told you that I like what you did with your hair?"
            scene ch4sc06_072 with dissolve
            al "Thank you, I wasn’t sure if you'd noticed..."
            mc "It suits you."
            scene ch4sc06_073 with dissolve
            al "..."
            mc "Feeling shy?"
            scene ch4sc06_074 with dissolve
            al "N-No... Just a tad nervous... I’m about to let you see me as... as a woman."
            mc "Hey... You don’t have to. If you aren’t ready, that won’t upset me."
            scene ch4sc06_075 with dissolve
            al "..."
            scene ch4sc06_076 with dissolve
            al "I want to... I’ve wanted this ever since you came back to Riverside."
            "As Alice locks eyes with you, her nervousness turns into excitement for what is about to happen."
            scene ch4sc06_077 with dissolve
            al "Are you... happy with what you see?"
            mc "Alice... My pants have never felt this tight. All because of you."
            scene ch4sc06_078 with dissolve
            al "Heh-Heh! Good! That’s the effect I wanted to have on you..."
            al "Then I should probably be a good childhood friend and make sure you see everything..."
            scene ch4sc06_079 with dissolve
            mc "Gods have been good to you, Alice. You’re perfect."
            al "Oh? You like my ass that much?"
            mc "Saying I like it, would be the understatement of the century."
            scene ch4sc06_078 with dissolve
            al "*Giggles* Okay, okay! I’m going to blush like a tomato if you keep talking like that."
            mc "That ship has already sailed, I’m afraid."
            scene ch4sc06_080 with dissolve
            al "Mhm... You’re a little overdressed for the occasion. You said your pants were tight?"
            al "Then it's probably best if we remove them..."
            scene ch4sc06_081 with dissolve
            mc "Mh-Hm. Why don’t you come over here and give me a hand?"
            scene ch4sc06_082 with dissolve
            al "You’re saying such lewd things. I’m your childhood friend..."
            mc "Don’t pretend your thoughts aren’t just as carnal."
            scene ch4sc06_083 with dissolve
            al "I suppose I can’t deny that."
            al "After all, I've thought about us being naked together... countless times."
            al "I'd be a bad childhood friend if I didn’t help you undress, right?"
            mc "Yeah... A very bad one."
            al "Say no more. Let’s get these pesky pants off."
            scene ch4sc06_084 with dissolve
            with vpunch
            "Alice slips your pants off and your hardened cock springs free as the constricting item is removed."
            al "Ahh! N-No wonder you said it felt tight..."
            al "Does this mean... that you like me?"
            mc "Very much."
            scene ch4sc06_085 with dissolve
            al "Could I... you know... touch it?"
            mc "That’s what a good friend would do."
            scene ch4sc06_086 with dissolve
            "Alice curiously grabs your shaft and kneels down in front of you, your tip resting against her breast."
            al "Ahhnh... Woah! It’s really warm... and firm."
            scene ch4sc06_087 with dissolve
            al "You know... I've heard girls gossip about men's... this thing... before."
            mc "Mnhhh..."
            scene ch4sc06_086 with dissolve
            al "But I always had the impression they're the size of two fingers."
            al "Yours is much bigger than that..."
            scene ch4sc06_087 with dissolve
            mc "I suppose I’m above average... Mnhhh..."
            scene ch4sc06_086 with dissolve
            al "It’s my first time seeing one... but I'm sure you must be."
            scene ch4sc06_087 with dissolve
            al "Do you like it when I hold it? It feels good in my hands."
            scene ch4sc06_086 with dissolve
            mc "Mnhh... Yes... It feels great."
            scene ch4sc06_087 with dissolve
            al "C-Can I... stroke it?"
            scene al_lewd3 with dissolve
            "Despite asking politely, she doesn’t wait for an answer."
            mc "Ahh... Alice... Fuck."
            "She moves her hand slowly but with a firm grip, carefully letting your tip graze her soft breasts."
            al "I’m not hurting you, am I?"
            mc "No... Definitely not... Ahhnh... It feels amazing."
            al "The girls at the academy were talking about how it feels good for a guy when his... is being stimulated."
            mc "Y-You’re... stimulating it alright. MMh."
            al "Good! Good... I want you to feel what I feel."
            al "It makes me a little nervous, though. I've been preparing myself using my fingers lately..."
            al "But now that I see it’s this big... it can’t possibly fit inside me, can it?"
            mc "Mhh... It can. Your body will slowly adjust to the size and your juices will help it slide inside."
            with vpunch
            al "*{b}Grip tightens{/b}* Gosh! You’re saying such indecent things to me... Mmhm."
            al "It makes me want to do all sorts of lewd things with you..."
            al "One of the girls said she once took a guy in her mouth?"
            mc "It’s called a blowjob. Where a woman uses her mouth to give pleasure to her partner."
            al "It sounds naughty. But weirdly enticing at the same time... Would you like it if I did that?"
            mc "Alice... do you feel how my cock is throbbing in your hand?"
            al "Mhm yeah... it’s quite intense."
            mc "That is my body screaming for you to do it."
            al "R-Really? You want to be in my mouth that badly?"
            scene ch4sc06_088 with dissolve
            al "I can’t lie... I’m curious to see what it tastes like."
            mc "Oh? Have you thought about having me in your mouth before?"
            scene ch4sc06_089 with dissolve
            al "Once or twice... *Kiss*"
            scene ch4sc06_088 with dissolve
            al "What do I do?"
            mc "Just do whatever comes natural to you: kissing, licking, sucking."
            al "*Deep breath* Okay... I can do this."
            scene ch4sc06_089 with dissolve
            "Alice’s pillowy soft lips press gently against your throbbing tip as she maintains a firm grip on your shaft."
            al "Mmmhpf... Mhh-Nnnghh..."
            scene al_lewd4 with dissolve
            al "*Suck* *Suck* Mnh!"
            mc "Ahhmh... That’s it... Keep sucking like that, Alice."
            al "*Slurp* Mnnh! *Lick* Nnnhnnh-mmhh!"
            mct "{i}Damn... She’s a natural. Her lips feel like soft suction cups...{/i}"
            scene al_lewd5 with dissolve
            "She keeps sucking your cock without respite, staying enthusiastically latched onto it."
            al "*Moans* Mmmnh! *Suck* Nngh... I-luhve yhur cohck!"
            mc "Hnngh... Can’t even stop to speak? Mhm... Then keep sucking like a good little childhood friend."
            al "*Moans* I will! Mmhh! *Lick*"
            mc "That’s it, Alice. Enjoy it... savor every inch of me. You’re incredible."
            al "Mhmh! I-... Mnnh! Luvh you... soh mhuch! Mmnh!"
            scene ch4sc06_090 with dissolve
            al "*Soft moan* Mnnhh..."
            al "*Panting* Haaahh..."
            scene ch4sc06_091 with dissolve
            al "Yum! I really like this! Should I keep sucking your cock?"
            scene ch4sc06_092 with dissolve
            mct "{i}Heh, she’s really into it now. She's not even shy about saying cock anymore.{/i}"
            mct "{i}Or about grasping me so firmly...{/i}"
            mc "Why don’t you come up here and let me take care of you for a bit?"
            scene ch4sc06_091 with dissolve
            al "N-No! I-I want to make you cum! I want your cock to feel happy!"
            scene ch4sc06_092 with dissolve
            mc "*Chuckles* You want my cock to feel happy?"
            al "*Nods*"
            scene ch4sc06_093 with dissolve
            al "Yes! All the time! ... Sabrina once told me that the best way to a man's heart is to keep his cock happy."
            scene ch4sc06_092 with dissolve
            mc "*Chuckles* Heh... That sounds like something she'd say. I’m not going to argue against her logic."
            scene ch4sc06_093 with dissolve
            al "So, I can continue to make your cock happy? Make you happy?"
            scene ch4sc06_094 with dissolve
            mc "By all means, Alice. I’ll be generous and allow it."
            scene ch4sc06_093 with dissolve
            al "My, my... So kind and thoughtful of you! Heheh."
            scene ch4sc06_095 with dissolve
            al "*Mwah* Mhh-mhh."
            "She gently sucks your tip a few times before giving it one last kiss."
            scene ch4sc06_093 with dissolve
            al "There is something else I want to try. You like my breasts, right?"
            scene ch4sc06_096 with dissolve
            mc "Yeah, they are perky and supple... And your nipples look nice and hard."
            al "Then I think you will enjoy this. They are really sensitive, especially when I think about us together..."
            scene ch4sc06_097 with dissolve
            al "*Squishes breasts* This should make both of us very... happy."
            scene al_lewd6 with dissolve
            mc "*Grunts* Mmh... Alice... You’re amazing, you know that, right?"
            al "You think so? Mmh... Good. Ahh... You're amazing too!"
            mc "Your breasts are perfect for this... Even though they aren’t the biggest, their shape and firmness... ahh."
            al "That’s it. Keep enjoying my breasts. Mnh-Mhh! They fit so well around your cock."
            al "*Soft moan* You feel so warm and hard between my breasts. You must really like them! Ahhhnngh..."
            scene al_lewd7 with dissolve
            al "*Moans* I’m Ahhnh... I’m going to make sure you’re taken care of..."
            al "*Soft moan* Mhh [mc]! Is your cock feeling good? Is it happy?"
            mc "F-Fuck Alice... Ahhh! K-Keep doing that..."
            al "*Giggles* I’ll Mh-Mh... take that as Ahhhh ... big yes. Mh!"
            al "Think of all the years we could’ve been doing this..."
            al "*Moans* How- Ahh... everyone back in Riverside... Ahmm Nnhh! ... would’ve been shocked..."
            al "*Soft moan* About our Nnhh... scandalous behavior. How shameful we must be to do this outside of marriage..."
            al "My mother would lock me in my room for weeks if she knew what I was doing right now..."
            al "Acting on my shameful and indecent desires... with my childhood friend! {b}AHH-AHH!{/b}"
            mc "F-Fuck... Alice! I’m cumming! Ahhh..."
            with vpunch
            scene ch4sc06_097 with dissolve
            $ renpy.pause(1.5)
            scene ch4sc06_098 with dissolve
            with vpunch
            $ renpy.pause(2)
            scene ch4sc06_099 with dissolve
            mc "{b}*Moans* F-Fuck! Ahh-Alice!!{/b}"
            with vpunch
            $ renpy.pause(0.5)
            with vpunch
            $ renpy.pause(0.5)
            with vpunch
            mc "*Heavy breathing* Alice ... That was incredible. Fuck..."
            al "{b}MHH!!{/b} *Suck* Mnngh! Nngh! *Suck* Mmhhhhhmmm..."
            scene ch4sc06_100 with dissolve
            mc "Damn... I completely filled your mouth, huh?"
            al "Hnghh! Mmhh!"
            mct "{i}Maybe I should have warned her... It’s her first time doing something like this, afterall.{/i}"
            mc "You can spit-"
            scene ch4sc06_101 with dissolve
            al "{b}MHH!-NHH!{/b}"
            mc "*Chuckles* You’re such a little cutie."
            scene ch4sc06_102 with dissolve
            al "*Gulp*"
            scene ch4sc06_103 with dissolve
            al "*Gulps again*"
            scene ch4sc06_104 with dissolve
            "She presents her mouth with no trace of your cum left."
            al "Aaaaah..."
            mc "You keep surprising me, Alice."
            scene ch4sc06_105 with dissolve
            al "That... will take some getting used to."
            scene ch4sc06_106 with dissolve
            mc "Did it taste bad?"
            scene ch4sc06_107 with dissolve
            al "Not bad. Hmh... just, a new flavor. I thought it was supposed to taste salty?"
            al "But what I just had in my mouth... Your cum? ... It had a sweetness to it."
            scene ch4sc06_108 with dissolve
            al "I think I liked it. I'll have to taste it a few more times to be certain."
            scene ch4sc06_106 with dissolve
            mc "*Chuckles* A few more times, huh?"
            scene ch4sc06_107 with dissolve
            al "Mh-Hm, quite a few more..."
            scene ch4sc06_108 with dissolve
            al "This big fella will have to become well acquainted with my mouth."
            mc "Come here."
            scene ch4sc06_109 with dissolve
            al "Gosh... I can’t believe I... we, just did that."
            al "That was so impulsive of us. So naughty and lewd..."
            scene ch4sc06_110 with dissolve
            mc "Do you regret it?"
            scene ch4sc06_111 with dissolve
            al "What? {b}NO!{/b}"
            scene ch4sc06_112 with dissolve
            al "I told you. I’ve wanted this for a long time..."
            scene ch4sc06_111 with dissolve
            al "It’s just... My mother would lose her shit if she knew what we just did."
            scene ch4sc06_110 with dissolve
            mc "That she would. I remember she always yelled at us when we ran out to play."
            mc "She thought I would be a bad influence on you."
            scene ch4sc06_113 with dissolve
            al "And she was right! *Giggles*"
            al "I just... sucked your cock outside of marriage."
            scene ch4sc06_114 with dissolve
            al "I’ve soiled myself."
            al "Given into my desires and become a lecherous woman..."
            scene ch4sc06_115 with dissolve
            mc "Those are your mother’s words. That isn’t our reality, Alice."
            mc "Her beliefs and morals don't rule our lives."
            mc "You love me, right?"
            scene ch4sc06_116 with dissolve
            al "Mhm! More than anything."
            scene ch4sc06_118 with dissolve
            mc "Then it doesn't matter if we’re married, or not."
            mc "At least, not in my eyes."
            scene ch4sc06_116 with dissolve
            al "I suppose you’re right."
            al "We can still have these feelings for each other without marriage."
            scene ch4sc06_118 with dissolve
            mc "You just showed me that you love me, that you care for me, and that you want to make me happy."
            mc "And guess what? You did."
            scene ch4sc06_116 with dissolve
            al "You really understand what to say to make me feel better. You always did."
            scene ch4sc06_117 with dissolve
            al "You make my heart beat really fast..."
            scene ch4sc06_118 with dissolve
            mc "We can’t have you be the only one with a fluttering heart, can we?"
            scene ch4sc06_117 with dissolve
            al "No. That would be rude. And we wouldn’t want that, would we?"
            scene ch4sc06_119 with dissolve
            mc "Certainly not..."
            scene ch4sc06_120 with dissolve
            al "I know just the thing to make your pulse match mine..."
            scene ch4sc06_121 with dissolve
            al "*Mwaahh*"
            "Alice presses her soft lips against yours in a tender kiss."
            scene ch4sc06_121a with dissolve
            mct "Damn... The way her mouth captures mine completely as we kiss..."
            mct "And how she holds onto me like this..."
            mct "{i}It makes me feel a surge of wonderful emotions.{/i}"
            scene ch4sc06_121 with dissolve
            al "*Soft moaning* Mmmh... Mh-Hnh... *Kiss* Mmhh-... *Lick*"
            scene ch4sc06_120 with dissolve
            al "How’s that? Pulse quicker?"
            scene ch4sc06_122 with dissolve
            mc "I’ll say. You’ve become quite the kisser."
            scene ch4sc06_123 with dissolve
            al "It’s easy when you've thought about it countless times over the years..."
            al "So many times, I’ve imagined you coming back to Riverside."
            al "And that you'd take me in your arms... and kiss me at last."
            scene ch4sc06_122 with dissolve
            mc "Really? I vividly remember you slapping me angrily..."
            scene ch4sc06_123 with dissolve
            al "You deserved it! ... Sorry. I didn’t slap you too hard, right?"
            mc "You already apologized when we were at the bridge in Riverside."
            mc "And no. You hit like a girl."
            scene ch4sc06_124 with dissolve
            al "*Soft kiss* Hey... you wanting another?"
            mc "*Chuckles* Mercy. We’re too comfortable right now to be wrestling about."
            scene ch4sc06_123 with dissolve
            al "Yeah... I like this."
            al "This is what I’ve dreamt about for so long. It almost doesn’t feel real."
            mc "Well, I don’t think either of us are asleep. So, I don't think we're dreaming."
            al "Good. Good. Do you think... would your parents have approved of me?"
            scene ch4sc06_124 with dissolve
            al "*Kisses softly*"
            mc "Mama and Papa loved you, Alice. You know that."
            al "I know. But still... it’s different when children grow up."
            scene ch4sc06_125 with dissolve
            mc "If they were still here, they'd definitely embrace you and tell you not to worry your pretty face."
            al "Nnngh. Okay, yes... I know."
            scene ch4sc06_126 with dissolve
            mc "My sweet Alice. Get some rest. I’ve gotta go find my egg."
            scene ch4sc06_125 with dissolve
            al "Ohkaay... Hnngh! Thanks for tonight... I loved it."
            scene ch4sc06_126 with dissolve
            mc "I’m the one who should be thanking you. You were amazing."
            mc "You wanted to make me happy and you definitely did."
            scene ch4sc06_125 with dissolve
            al "Ghood... Nest time ih-... even happhier!"
            mct "{i}Heh... She can barely speak. I guess it is quite late, and she just experienced a lot.{/i}"
            scene black with Dissolve(2)
            scene ch4sc06_127 with Dissolve(2)
            mc "Don’t sleep too long. You've gotta find your egg before dawn, remember?"
            al "*Moans* Mh-Hmm..."
            #play music darknight_4 fadein 1.0
            stop music fadeout 1.0
            scene black with Dissolve(1)


        "Just thinking about something. ({color=#2bff8b}Friendship{/color})":
            scene ch4sc06_060 with dissolve
            mc "No, no. Just thinking about the clue Sylph gave me."
            scene ch4sc06_061 with dissolve
            al "Oh, yeah. I’m not too worried about mine. It’s somewhere in my classroom for sure!"
            scene ch4sc06_060 with dissolve
            mc "Speaking of clues... I'd better get going. I don’t want to be the last one finding their egg."
            mc "But thank you for showing me your room, Alice. It's something you should be proud of."
            scene ch4sc06_061 with dissolve
            al "I totally am! ... See you later, then. And good luck with your egg!"
            #play music darknight_4 fadein 1.0
            stop music fadeout 1.0



    scene black with Dissolve(2)
    $ renpy.pause(1)

    if irene_alive == True:
        scene ir2 with Dissolve(1)
        $ renpy.pause()
        play music home_2 fadein 1.0
        #stop music fadeout 1.0
        scene ir4 with Dissolve(1)
        $ renpy.pause()
        scene ir5 with Dissolve(1)
        $ renpy.pause(0.5)
        ir "*Snickers*"
        scene ir6 with Dissolve(1)
        $ renpy.pause(0.5)
        ri "Hmm."
        scene ir7 with Dissolve(1)
        $ renpy.pause()
        scene ir8 with Dissolve(1)
        $ renpy.pause()
        scene ir9 with Dissolve(1)
        $ renpy.pause()
        scene ir10
        $ renpy.pause()
        scene ir11 with dissolve
        $ renpy.pause(1.5, hard=True)
        scene ir12
        with vpunch
        $ renpy.pause(0.5)
        ri "Hngh!"
        ri "Society of Shadows."
        scene ir13 with Dissolve(1)
        $ renpy.pause(0.5)
        ir "Heh! Nicely deduced..."
        ir "You're intuitive considering you're a deranged psychopath who killed her own shadow-sisters in coldblood."
        ri "Lies."
        ir "They told me you wouldn't own up to what you did... either way, you're done."
        scene ir14 with Dissolve(1)
        with vpunch
        $ renpy.pause(0.5)
        ir "Bringing you in will ensure my graduation as a Shadow-sister! Hiyhh!"
        ri "Society sent initiate? Hm."
        scene ir15 with Dissolve(1)
        with vpunch
        ir "*Groans* Argh!"
        ri "Sending initiate, desperate? Hm."
        scene ir16 with Dissolve(1)
        with vpunch
        ir "Ugh!"
        scene ir17 with Dissolve(1)
        ri "Leave me... alone."
        ir "*Coughing* W-What the hell was that kick? Hnngh... you adjusted mid air?"
        scene ir18 with Dissolve(1)
        ir "They won't stop coming for you..."
        ir "If not me, they'll send someone else, as many as it takes until they get what they want!"
        ri "Hm."
        scene ir19 with Dissolve(1)
        ir "*Under her breath* She's... letting me live?"
        ir "*Under her breath* What kind of murderous psychopath let's her opponent live?!"
        ir "*Under her breath* Tsk! No matter... I cannot fail my initiation."
        scene ir20 with Dissolve(1)
        with vpunch
        ir "I've been given a mission, failure isn't an option! Die!"
        ri "Hm."
        scene ir21 with Dissolve(1)
        ri "Persistent."
        ir "You'll answer for your crimes against the society!"
        scene ir22 with dissolve
        with vpunch
        ir "*Groans* Urgh!"
        scene ir23 with dissolve
        $ renpy.pause(3.5, hard=True)
        scene ir24
        ri "Had potential."
        ri "Hm."
        scene ir25 with Dissolve(1)
        ri "Maybe?"
        scene ir26 with Dissolve(1)
        ri "Will see."
        scene ir27 with Dissolve(1)
        ir "*Groans* Hnnghh..."
        ir "W-What... happened?"
        scene ir28 with Dissolve(1)
        ir "She... used magic? Ughh... my head is spinning."
        ir "I was out cold... she could've finished me off easily... why spare me?"
        ir "The society won't be happy with my failure... but I'm clearly outmatched."
        scene black with Dissolve(2)
        $ renpy.pause(1)

    else:
        scene black with dissolve
        $ renpy.pause(0.2)

    scene ch4sc06_128 with Dissolve(1)
    $ renpy.pause(0.5)
    play music home_2 fadein 1.0
    #stop music fadeout 1.0
    mct "{i}Hmh... Sylph’s clue was...{/i}"
    mct "{i}I rest near the sky but I'm afraid of heights. Come rescue me, oh great adventurer, before a gust of wind claims me.{/i}"
    mct "{i}I have an idea about where it might be.{/i}"
    scene black with Dissolve(1)
    scene ch4sc06_129 with Dissolve(1)
    mct "{i}The highest tower in Luxenford. It's part of the east-wing of the royal palace.{/i}"
    mct "{i}I guess I'd better get climbing...{/i}"
    scene black with Dissolve(1)
    scene ch4sc06_130 with Dissolve(1)
    mct "{i}Who could have guessed that all those tree-climbing adventures with Alice and Flynn would pay off so well?{/i}"
    mct "{i}Certainly never expected them to translate into climbing the royal palace!{/i}"
    scene ch4sc06_131 with dissolve
    mct "{i}Okay, let’s see. If I were a troublesome little fae, where would I hide an enchanted egg?{/i}"
    scene ch4sc06_132 with dissolve
    mct "{i}Hmh... No.{/i}"
    scene ch4sc06_133 with dissolve
    mct "{i}Only rubble here...{/i}"
    scene ch4sc06_134 with dissolve
    mct "{i}Couple of broken bottles. Some rags. Nothing ...{/i}"
    scene ch4sc06_135 with dissolve
    mct "{i}*Sigh* Where in the five hells is it?{/i}"
    scene ch4sc06_135a with dissolve
    mct "{i}Wait... What’s that? There’s a faint glow coming from the rubble over there.{/i}"
    scene ch4sc06_136 with dissolve
    mct "{i}Hah! Found ya.{/i}"
    scene ch4sc06_137 with dissolve
    mct "{i}You’re coming with me, buddy.{/i}"
    mct "{i}Sylph better have a good reward for sending me all the way up here.{/i}"
    scene ch4sc06_138 with dissolve
    with vpunch
    pam "What in all that’s holy are {b}YOU{/b} doing here?!"
    scene ch4sc06_139 with dissolve
    mc "Amelia?"
    mct "{i}Shit... this looks bad.{/i}"
    scene ch4sc06_140 with dissolve
    pam "It’s 'Princess Amelia' to you, scoundrel!"
    scene ch4sc06_141 with dissolve
    pam "I knew you were a good-for-nothing, common charlatan!"
    scene ch4sc06_141 with dissolve
    pam "You may have tricked my parents into thinking you're just a regular bodyguard with good intentions..."
    scene ch4sc06_140 with dissolve
    pam "But I know your kind! Doing anything to get close to the royal family in hopes of gaining our favor."
    scene ch4sc06_139 with dissolve
    mc "It’s not what it looks like-"
    scene ch4sc06_140 with dissolve
    pam "Spare me your excuses! You have no business here, especially at this hour!"
    pam "What are your intentions? Stealing from us, maybe? Or perving at the maids while they’re asleep?"
    scene ch4sc06_141 with dissolve
    pam "Disgusting! Eck!"
    scene ch4sc06_140 with dissolve
    pam "I can’t believe I was being nice to you!"
    scene ch4sc06_141 with dissolve
    pam "I even allowed my handmaiden to talk me into giving you a chance!"
    pam "Just wait til I summon the guards."
    scene ch4sc06_142 with dissolve
    with vpunch
    mc "{b}Amelia!!{/b}"
    mc "Can I talk now?"
    scene ch4sc06_143 with dissolve
    pam "I-I suppose. If you must."
    pam "Explain yourself, oaf."
    scene ch4sc06_139 with dissolve
    mc "I’m not here to steal from you, or to perv on anyone..."
    scene ch4sc06_144 with dissolve
    mc "I’m here on behalf of my guild."
    mc "I was looking for an object they'd hidden up here."
    scene ch4sc06_140 with dissolve
    pam "Why would they hide an object here?"
    pam "The palace is off-limits to commoners without an invitation."
    scene ch4sc06_144 with dissolve
    mc "It's part of a scavenger hunt. Apparently, it’s a yearly tradition that our members participate in."
    mc "We each have an object to find, and mine happened to be hidden up here."
    scene ch4sc06_143 with dissolve
    pam "So... you’re not here with ill intent?"
    pam "You weren't trying to spy on the ladies of court?"
    scene ch4sc06_139 with dissolve
    mc "Amelia, I swear I’m not here to cause any trouble."
    scene ch4sc06_145 with dissolve
    pam "Hmpfh! ..."
    scene ch4sc06_146 with dissolve
    pam "It’s Princess Amelia to you!"
    scene ch4sc06_145 with dissolve
    mc "Sorry if I frightened you, Princess Amelia."
    pam "..."
    scene ch4sc06_147 with dissolve
    pam "Fine! ... I won’t report you to the guards."
    pam "But don’t think to make a habit out of this!"
    pam "It’s only thanks to my kindness that you aren’t being thrown into the dungeon."
    scene ch4sc06_144 with dissolve
    mc "Thank you."
    mc "That’s very generous of you."
    scene ch4sc06_147 with dissolve
    pam "If any of the servants or guards had seen you, they wouldn’t have stopped to ask questions."
    scene ch4sc06_144 with dissolve
    mc "I know. I owe you one, Am... Princess."
    scene ch4sc06_145 with dissolve
    pam "..."
    scene ch4sc06_146 with dissolve
    pam "Tomorrow. First light."
    scene ch4sc06_145 with dissolve
    mc "What?"
    scene ch4sc06_147 with dissolve
    pam "I want to go shopping before the streets become too busy."
    pam "You’ll accompany me."
    scene ch4sc06_148 with dissolve
    mc "You want me to... join you?"
    pam "..."
    pam "......."
    scene ch4sc06_149 with dissolve
    with vpunch
    pam "I don’t {b}‘WANT’{/b} you to join me! That’s ridiculous."
    scene ch4sc06_141 with dissolve
    pam "I simply need your services..."
    pam "You’re my bodyguard, and I need someone to carry my stuff."
    scene ch4sc06_139 with dissolve
    mc "Great."
    mc "So I’m your maid now?"
    scene ch4sc06_140 with dissolve
    pam "Keep moaning about it and I'll find you a proper maid outfit to wear."
    scene ch4sc06_144 with dissolve
    mc "Fine, fine."
    mc "I’ll accompany you to the market tomorrow."
    scene ch4sc06_147 with dissolve
    pam "At first light."
    pam "And don’t be late!"
    scene ch4sc06_150 with dissolve
    pam "You'd best get out of here before someone sees you."
    pam "Oh, can I trust that you can get down on your own?"
    pam "I'm not about to allow you to walk through the castle at this hour."
    scene ch4sc06_151 with dissolve
    mc "Sure, Princess..."
    mct "She’s a real piece of work. Although, she could have reacted even worse."
    mct "The fact she was willing to take me on my word shows she trusts me to an extent."
    mct "She has a point, though. I'd better get out of here."
    #play music darknight_4 fadein 1.0
    stop music fadeout 1.0
    scene ch4sc06_152 with dissolve
    play music summon_3 fadein 1.0
    #stop music fadeout 1.0
    mc "*Sigh* I’ve never jumped from this far up before. I could soften the landing using wind magic or..."
    mc "Maybe this would be a good opportunity to test some of Onyx’s abilities?"
    mc "Onyx?"
    ox "Yes, master?"
    mc "Can you handle a landing from this height?"
    ox "Hah! Easily! I can’t believe you'd question my abilities like that."
    scene ch4sc06_153 with dissolve
    with vpunch
    mc "Let’s do it then!"
    scene mc_landing1 with dissolve
    $ renpy.pause(2.0)
    scene ch4sc06_154 with dissolve
    $ renpy.pause()
    scene ch4sc06_155
    with vpunch
    $ renpy.pause()
    mc "Good job, Onyx. I didn’t even feel that landing."
    ox "You’re welcome, master. It's my top priority to keep you unharmed so our symbiosis can continue."
    mc "Right. Will you be able to handle landings from any height?"
    ox "Yes, my cells will materialize and cushion your landing to varying degrees, depending on your movement speed and weight."
    ox "Of course, your body is already extremely durable compared to other hosts I’ve had."
    scene ch4sc06_156 with dissolve
    mc "Yeah, I imagine it is. Let’s get this egg back to Sylph."
    ox "Right. What do you think your reward will be?"
    scene ch4sc06_157 with dissolve
    mc "I’m not sure. But after all this, it'd better be damn good."
    #play music darknight_4 fadein 1.0
    stop music fadeout 1.0
    scene black with Dissolve(1.5)
    "Sylph greets you eagerly as you enter the guild."
    play music forest_1 fadein 1.0
    #stop music fadeout 1.0
    scene ch4sc06_029 with dissolve
    sy "Finally! You’re back!"
    scene ch4sc06_031 with dissolve
    mc "Finally? Did the others finish already?"
    scene ch4sc06_032 with dissolve
    sy "No, you’re the first one! Now, let’s see it!"
    scene ch4sc06_031 with dissolve
    mc "Sure, here you go."
    "Sylph takes a quick glance at the egg."
    scene ch4sc06_029 with dissolve
    sy "You really found it! Well done!"
    scene ch4sc06_031 with dissolve
    mc "You hid it at the top of the royal palace..."
    scene ch4sc06_030 with dissolve
    sy "Did I? I wasn’t too sure which one I hid where..."
    mc "Sylph..."
    scene ch4sc06_032 with dissolve
    sy "The important thing, is that you completed your task and that I had the utmost faith in you!"
    scene ch4sc06_031 with dissolve
    mc "*Sighs heavily* You do realize I now have to play bodyguard for the princess ... in just a few hours?"
    scene ch4sc06_029 with dissolve
    sy "The princess? Why? I thought you weren’t due to start until later in the week?"
    scene ch4sc06_031 with dissolve
    mc "Yeah... Well, she caught me red-handed. So, it was either appease her or spend the night in a cell."
    scene ch4sc06_030 with dissolve
    sy "I suppose I didn’t account for you being caught... Heh-Heh. My bad!"
    scene ch4sc06_032 with dissolve
    sy "But look at the bright side! Now you get to spend more time with the princess! Yup!"
    scene ch4sc06_031 with dissolve
    mc "How is that a bright side? She’s impossible to get along with..."
    scene ch4sc06_029 with dissolve
    sy "Well, try to get through to her? I’m sure she can’t be all bad!"
    sy "You realize being in the good graces of the royal family comes with a lot of perks, yeah?"
    scene ch4sc06_033 with dissolve
    sy "It can open a lot of doors for you personally, and for the overall prosperity of the guild."
    scene ch4sc06_031 with dissolve
    mc "Hmh. I suppose you’ve got a point."
    scene ch4sc06_032 with dissolve
    sy "I knew you’d see reason! Yup!"
    scene ch4sc06_031 with dissolve
    mc "Yeah, yeah. So, did you want to talk about what’s been bothering you?"
    scene ch4sc06_033 with dissolve
    sy "Uh-Huh! In fact, I was hoping you’d be the first one back so we could have a moment alone."
    sy "Follow me!"
    scene black with Dissolve(1)
    "Sylph leads you down a hallway with several doors. She opens the one at the end, and you both go downstairs."
    scene ch4sc06_158 with Dissolve(1)
    sy "*Excitedly* Come! Come! We’re almost there!"
    scene ch4sc06_159 with dissolve
    mc "Sylph... Where are we going? Are you leading me into some sort of dungeon?"
    scene ch4sc06_158 with dissolve
    sy "*Giggling* Dungeon? Yes! My secret sex dungeon! Heh-heh-heh!"
    sy "I've prepared it just for you! Prepare to be my slave! Heh-heh-heh!"
    scene ch4sc06_160 with dissolve
    mc "*Sighs* Sylph..."
    sy "Kidding! Boo! Now, come on. I have something to show you!"
    "You follow Sylph to the back of the room."
    scene ch4sc06_161 with dissolve
    sy "Tadaa! Whatcha think?"
    scene ch4sc06_162 with dissolve
    sy "Isn’t it cute? Sit, sit!"
    scene ch4sc06_163 with dissolve
    mc "Sure, it’s... cute? But why down here in the basement?"
    sy "Aiiyh! These stools are pretty cold!"
    scene ch4sc06_164 with dissolve
    mc "Well, we are in a basement... and you aren’t known for excessive clothing, so..."
    scene ch4sc06_165 with dissolve
    sy "My, my! Been keeping an eye on how I dress, have you? Mhm-Hmm!"
    scene ch4sc06_164 with dissolve
    mc "You know what I mean..."
    scene ch4sc06_165 with dissolve
    sy "Mhm, I do. I like a man who pays attention."
    scene ch4sc06_164 with dissolve
    sy "And to answer your question, I chose the basement 'cause we can be alone here."
    scene ch4sc06_165 with dissolve
    sy "Without being... interrupted."
    scene ch4sc06_164 with dissolve
    mc "Don’t people come down here to get stuff?"
    scene ch4sc06_166 with dissolve
    sy "I’m the only one who handles storage in the guild. Besides, ever since the guild declined..."
    sy "We've barely used some of our facilities."
    scene ch4sc06_167 with dissolve
    mc "Facilities?"
    scene ch4sc06_166 with dissolve
    sy "We used to have all sorts of facilities available."
    scene ch4sc06_168 with dissolve
    sy "Like this storage cellar for all sorts of goods, for example."
    scene ch4sc06_169 with dissolve
    sy "Or the dining hall we use for feasts, social gatherings, or just keeping our hungry adventurers fed!"
    scene ch4sc06_166 with dissolve
    sy "And then there are the dormitories, where ranked members of the guild can stay."
    scene ch4sc06_169 with dissolve
    sy "There's even a small yard out back that we used for combat practise."
    sy "With the way things have been going since you joined, I hope we’ll soon be able to restore those areas eventually."
    scene ch4sc06_170 with dissolve
    mc "With all the work everyone's been putting in, I have a feeling we’ll get the guild back in top shape in no time."
    scene ch4sc06_168 with dissolve
    sy "Yes! You’re right! That’s what I keep telling everyone!"
    sy "Soon we'll be better than ever before!"
    scene ch4sc06_170 with dissolve
    mc "I’ve even noticed a decent increase in non-ranking adventurers taking on the smaller contracts."
    scene ch4sc06_169 with dissolve
    sy "Yeah, word has been spreading about the guild's improving health. And that's drawn lots of newcomers!"
    scene ch4sc06_170 with dissolve
    mc "It's nice. Being able to talk with you like this again..."
    scene ch4sc06_167 with dissolve
    mc "I felt like I'd lost a friend when you were avoiding me."
    sy "..."
    scene ch4sc06_166 with dissolve
    sy "You never lost me... I just needed a little time."
    sy "I’m sorry. I should’ve just talked about how I was feeling as soon as you came back."
    scene ch4sc06_170 with dissolve
    mc "It’s okay. We’re talking now, and that’s what matters."
    mc "Eliza told me a little about what upset you. But I'd like to hear about it from you."
    scene ch4sc06_171 with dissolve
    sy "Mhm. Okay. I suppose we can’t dance around it forever."
    scene ch4sc06_172 with dissolve
    #play music darknight_4 fadein 1.0
    stop music fadeout 1.0
    sy "When Eliza told me that you were half-angel..."
    play music feels_3 fadein 1.0
    #stop music fadeout 1.0
    scene ch4sc06_173 with dissolve
    sy "It triggered some memories and deep emotions within me that I thought I had long-since buried."
    scene ch4sc06_172 with dissolve
    sy "But they all came rushing to the surface. The guy I..."
    scene ch4sc06_173 with dissolve
    sy "My friend... turns out to be the same kind of being as one that once caused me so much pain and anguish."
    scene ch4sc06_174 with dissolve
    mc "What happened to cause you such turmoil, Sylph?"
    scene ch4sc06_175 with dissolve
    sy "When I was just a young fae, something... terrible happened to my home. To my whole village."
    sy "We lived deep in a secluded forest, like most fae communities. We had nothing but peace and an idyllic life for many centuries."
    scene ch4sc06_172 with dissolve
    sy "But one day, it all changed. One of us became obsessed with dark magic..."
    scene ch4sc06_173 with dissolve
    sy "Chaos magic, to be specific. She became fixated on trying to bring her stillborn child back to life."
    scene ch4sc06_175 with dissolve
    sy "We all tried to convince her not to go near that type of magic. It only ever brings horror."
    scene ch4sc06_172 with dissolve
    sy "But she was so consumed by her grief, and we suspected that she kept practicing the magic in secret."
    scene ch4sc06_166 with dissolve
    sy "One day, I went exploring and gathering edibles in the surrounding area, as I so often did back then."
    scene ch4sc06_175 with dissolve
    sy "And that turned out to be what saved me. Because that was the day... that everything ended."
    sy "While I was on my way back, I saw a sudden, massive golden explosion in the distance."
    sy "It shook the ground, the trees, and everything in-between."
    scene ch4sc06_172 with dissolve
    sy "I flew as fast as I could! It felt like my wings would fall off. But when I arrived..."
    scene ch4sc06_173 with dissolve
    sy "I remember how my heart sank to the bottom of my belly. Everything was just... gone."
    scene ch4sc06_175 with dissolve
    sy "Our houses... the trees... everything had been vaporized. Only a few scattered and charred fragments remained."
    scene ch4sc06_176 with dissolve
    with vpunch
    sy "Everyone... My friends... M-My family!"
    sy "All that was left were a few smoking husks, unrecognizable, lifeless burned bodies."
    sy "That’s when I saw him. A being clad all in white and gold, with large feathery wings..."
    scene ch4sc06_173 with dissolve
    sy "He shone with a blinding golden aura."
    sy "When he turned, I was suddenly transfixed by the intensity of his gaze. I couldn’t move at all..."
    scene ch4sc06_172 with dissolve
    sy "He didn’t say anything... He just looked at me."
    sy "And then he launched himself into the sky and disappeared into the clouds."
    scene ch4sc06_174 with dissolve
    mc "Sylph, I..."
    scene ch4sc06_171 with dissolve
    sy "I know it wasn't you, [mc]. And you would never do that. Eliza quickly made me realize that."
    sy "But I've been afraid about what you might be capable of doing if provoked..."
    scene ch4sc06_167 with dissolve
    mc "I can’t believe an Angel did that. Aren’t they supposed to be good? Just? Righteous?"
    scene ch4sc06_166 with dissolve
    sy "I doubt anyone really knows what they are. Or what motivates them. So many different cultures have their own ideas about what Angels are."
    scene ch4sc06_169 with dissolve
    sy "I did a lot of research over the decades afterwards."
    sy "I desperately wanted to understand."
    scene ch4sc06_171 with dissolve
    sy "*Sigh* But they aren’t common beings. What little I could find out, described them..."
    sy "As beings utterly devoted to order. Dedicated and ruthless warriors of light."
    scene ch4sc06_172 with dissolve
    sy "Their ultimate goal is to fight chaos."
    sy "Be it creatures of chaos, or any magic that derives from the ‘Abyss’"
    scene ch4sc06_170 with dissolve
    mc "So the fae that succumbed to chaos magic, she drew him there?"
    scene ch4sc06_171 with dissolve
    sy "Uh-huh. Only he didn’t settle for taking just her."
    sy "Instead, he destroyed everything and everyone in one massive blast."
    scene ch4sc06_173 with dissolve
    sy "I guess he didn’t want to take any chances."
    sy "And it cost me everything I'd ever known and loved."
    scene ch4sc06_174 with dissolve
    mc "You’ve been on your own ever since?"
    scene ch4sc06_173 with dissolve
    sy "Yup... Until I met Dalen."
    sy "We bumped into each other during his adventuring days on Elfwyr."
    scene ch4sc06_172 with dissolve
    sy "He was the first human that ever showed me any kindness or respect."
    scene ch4sc06_171 with dissolve
    sy "So, I stuck by him, and we became a team."
    sy "When we finally decided to settle in Luxenford, and we formed the guild."
    scene ch4sc06_164 with dissolve
    mc "Dalen mentioned that fae aren’t always treated well by other races. How come?"
    sy "It mostly boils down to our magical capabilities. We’re often sold as slaves..."
    scene ch4sc06_165 with dissolve
    sy "Sometimes rich lords acquire captured fae for their own sick pleasures."
    sy "Other times, wizards or mages buy us for their experiments so they can learn about our magic."
    scene ch4sc06_164 with dissolve
    sy "Which is why most fae live in secluded areas, far away from civilization."
    scene ch4sc06_170 with dissolve
    mc "I hate that this happened to you, Sylph."
    mc "I hope you know that I won’t let anything bad happen to you."
    scene ch4sc06_171 with dissolve
    sy "I know... Thank you, [mc]."
    scene ch4sc06_172 with dissolve
    sy "But now you know why I needed some time to collect myself and gather my feelings."
    scene ch4sc06_167 with dissolve
    #play music darknight_4 fadein 1.0
    stop music fadeout 1.0
    sy "..."
    play music forest_1 fadein 1.0
    #stop music fadeout 1.0
    mc "Completely understandable. Come over here and give me a hug."
    scene ch4sc06_177 with dissolve
    sy "*Hugs tightly* Hnngh!"
    mc "Better?"
    sy "Mhm-Hm! *Hugs* Mhhh."
    scene ch4sc06_178 with dissolve
    sy "So-so."
    scene ch4sc06_177 with dissolve
    mc "Just so-so?"
    scene ch4sc06_178 with dissolve
    sy "Yuuup! *Giggles* You’ll have to squeeze harder if you want a better rating! Yup, yup!"
    scene ch4sc06_179 with dissolve
    sy "Iiiyh! Ten outta ten!!! Iiihh!"
    mc "That’s more like it."
    scene ch4sc06_180 with dissolve
    sy "[mc]... I've really missed you!"
    sy "Did you... did you miss me as well?"
    ####Choice####
    scene major_choice with dissolve
    menu:
        "Show her with a kiss. ({color=#ff8cdd}Romance Lock-in{/color})":
            scene ch4sc06_181 with dissolve
            mc "Come here."
            $ sylph_relationship = True
            scene ch4sc06_182 with dissolve
            sy "*Kiss* Mnhh!!"
            scene ch4sc06_183 with dissolve
            sy "*Mwah* {b}MH-MH!!{/b} Mhhh..."
            scene sy_lewd1 with dissolve
            mct "{i}She’s tasty... incredibly fruity. And she smells of spring leaves.{/i}"
            sy "*Mwah* Ahhh... Yhuup-Mhm! You really-Nnghh... Mhissed me! *Kiss*"
            sy "*Kiss* I chan’t believe Ahhngh... We’re kissingh! Mhm!"
            mc "*Kiss* Believe it... *Kiss* You taste amazing."
            $ sylph_path = True
            sy "*Mwah* Kheep kissingh me! Mhm! I can... *Kiss* taste the magic on your lips! Ahhh..."
            scene sy_lewd1 with dissolve
            "Sylph eagerly sucks and plays with your tongue, rubbing hers against yours."
            mct "{i}If she keeps this up, I won’t be able to hold back ...{/i}"
            sy "*Moans softly* Ahhnnhh... I love kissing you! Mhm! Mhore! I want more!"
            sy "*Kiss* Keep your hands on me... *Mwah* I love how it makes my skin tingle... Ah-Ah..."
            scene sy_lewd3 with dissolve
            sy "*Moans softly* No more... No more holding back... Mhm..."
            mc "*Kiss* You really missed me, huh?"
            sy "*Mwah* Nhooo... Mhm... Just... Ahhh ... more kiss... *Mwah*"
            sy "*Kiss* [mc], I need you. *Mwah* I wanted us to be alone so we could... Ahh..."
            mc "*Kiss* Keep talking."
            sy "*Soft moan* I- I want you... I want to know what you taste like! *Mwah* What you feel like... Mhm!"
            mc "*Kiss* Then... get naked for me. Show me that little fae body of yours."
            sy "*Mwah* As you-Mhm-Mh! As you wish."
            scene ch4sc06_184 with dissolve
            sy "D-Don’t look, okay?"
            scene ch4sc06_185 with dissolve
            mc "I’m not looking away."
            scene ch4sc06_184 with dissolve
            sy "I knew you'd say something lecherous... Fine! You can look..."
            scene ch4sc06_185 with dissolve
            mc "What’s made you so shy?"
            scene ch4sc06_186 with dissolve
            sy "It’s not everyday I get naked for someone! Okay?"
            scene ch4sc06_187 with dissolve
            mc "Sylph... Is this your first time... ever? In 120+ years?"
            scene ch4sc06_186 with dissolve
            sy "Nhoo... I’m experienced! I have plenty of lewdness under my belt! Yuup!"
            scene ch4sc06_187 with dissolve
            mc "Sylph..."
            scene ch4sc06_188 with dissolve
            sy "*Sigh* Fine... It’s my... my first time being naked with someone."
            scene ch4sc06_187 with dissolve
            mc "Why would you try to hide that?"
            scene ch4sc06_188 with dissolve
            sy "Guys don’t like that, right?"
            sy "You want someone who knows everything about pleasing you."
            scene ch4sc06_187 with dissolve
            mc "*Chuckles* Fuck that."
            scene ch4sc06_188 with dissolve
            sy "What do you mean?"
            scene ch4sc06_187 with dissolve
            mc "I can’t speak on behalf of anyone else, but for me, it’s the opposite. I much prefer you this way."
            scene ch4sc06_189 with dissolve
            mc "That means I get to be your first. The first man to see you, to touch you, to feel you."
            mc "And pleasuring a man isn't exactly a higher science. I’m sure you will catch on quickly."
            scene ch4sc06_190 with dissolve
            sy "I want to learn... with you."
            "Sylph begins to undo her dress, slowly. Making sure you see everything."
            scene ch4sc06_191 with dissolve
            sy "My heart is beating like... like really fast! Yuup!"
            mc "That’s normal. You’re excited, and your body and mind is anticipating what’s about to happen."
            scene ch4sc06_192 with dissolve
            sy "Are you getting naked too? I’d... I’d love to see you."
            mc "I can’t rightfully refuse a request like that from a naked fae, can I?"
            sy "*Giggles* No! You couldn’t! That would be ill-advised, considering she handles your paycheck!"
            scene ch4sc06_193 with dissolve
            sy "Now! Drop those clothes and let me enjoy the view! *Giggling*"
            mc "*Chuckles* I like the confidence."
            scene ch4sc06_194 with dissolve
            sy "Yuup! That is soooo... Mhm-mhm!"
            sy "I find you oddly appealing!"
            scene ch4sc06_195 with dissolve
            mc "Oddly?"
            sy "Yup-Yup! Fae aren’t usually attracted to male species. Except for Nymphs: they like everyone."
            scene ch4sc06_194 with dissolve
            mc "Poor male fae..."
            sy "Male fae? *Giggles*"
            sy "There's no such thing, silly! Our species is female only."
            scene ch4sc06_195 with dissolve
            mc "What? Then how do you...?"
            scene ch4sc06_196 with dissolve
            sy "Make babies?"
            sy "In our world, it’s called a union. When two fae love each other, and wish to create offspring..."
            scene ch4sc06_197 with dissolve
            sy "They merge their magics. This forms an embryo which is infused with their combined magic."
            sy "It takes about a month for the embryo to hatch, and a new fae is born."
            scene ch4sc06_198 with dissolve
            mc "That’s... different."
            scene ch4sc06_196 with dissolve
            sy "Different? That's just how our species is."
            sy "Did you think every species are like humans?"
            scene ch4sc06_198 with dissolve
            mc "I suppose I never thought about it."
            mc "But I guess it makes sense that it would be different."
            scene ch4sc06_196 with dissolve
            sy "Yuup. In fae society, it’s frowned upon to choose a partner that isn’t fae."
            scene ch4sc06_197 with dissolve
            sy "Because we can’t procreate with other species, it's considered selfish if we don’t partner with another fae."
            scene ch4sc06_198 with dissolve
            mc "So you’re pressured into only being with your own species?"
            scene ch4sc06_194 with dissolve
            sy "Sort of... Though, it’s not a huge deal. It’s just what we know and expect."
            sy "And plenty of fae do choose other mates, especially if they aren't living in a fae community."
            scene ch4sc06_198 with dissolve
            mc "Have you ever been with a fae, then?"
            scene ch4sc06_194 with dissolve
            sy "No... Remember, I was still young when my community was obliterated..."
            sy "I haven't met another fae since then, and I’ve never been attracted to anyone."
            scene ch4sc06_196 with dissolve
            sy "Until you. When I first met you, your peculiar magic felt incredible appealing to me."
            scene ch4sc06_197 with dissolve
            sy "Being born from magic, fae are highly sensitive to it. And your magic feels very... enticing."
            scene ch4sc06_196 with dissolve
            sy "At first, I thought you were just a hard-ass knucklehead with sexy magic..."
            scene ch4sc06_198 with dissolve
            mc "*Chuckles* Sexy magic?"
            scene ch4sc06_195 with dissolve
            sy "Yuup! Very sexy ... You'd make most fae wet just by being near them."
            scene ch4sc06_196 with dissolve
            sy "But as I got to know you, and I saw how much you care about those in your circle..."
            scene ch4sc06_197 with dissolve
            sy "You became more and more appealing. Until one day, I caught myself..."
            scene ch4sc06_199 with dissolve
            sy "*Giggles* Heh-heh-heh..."
            mc "Go on. Finish what you were about to say."
            sy "*Mumbles* I was... touching myself, thinking about... *Whispers* you."
            mc "I didn’t catch that. Mind repeating it?"
            scene ch4sc06_200 with dissolve
            sy "About YOU! Geez! Why do you have to make me say it like that?"
            scene ch4sc06_198 with dissolve
            mc "How about you show me?"
            scene ch4sc06_197 with dissolve
            sy "Show you?"
            scene ch4sc06_198 with dissolve
            mc "Yeah, instead of telling me. Show me what you were thinking about when you were touching yourself."
            scene ch4sc06_199 with dissolve
            sy "I... I suppose I could do that. Okay! Yuup! Good idea!"
            scene ch4sc06_200 with dissolve
            #play music darknight_4 fadein 1.0
            stop music fadeout 1.0
            sy "The first thing I started thinking about was..."
            scene ch4sc06_201 with dissolve
            play music lewd_1 fadein 1.0
            #stop music fadeout 1.0
            sy "First I started thinking about your warm lips..."
            sy "I wanted to run my fingertips across them."
            sy "They're so full and inviting. I wanted desperately to feel them touch my own."
            sy "I'd bring myself close to you, just like this, while my perky breasts squish against you."
            scene ch4sc06_202 with dissolve
            sy "Then I'd guide your face towards mine and we would meld in a loving kiss."
            sy "*Mwah*"
            scene ch4sc06_201 with dissolve
            sy "We'd break our kiss slowly, but only for a few seconds before we engaged each other again."
            scene ch4sc06_202 with dissolve
            sy "*Mwaah* *Muuah*"
            scene ch4sc06_201 with dissolve
            sy "And again..."
            scene ch4sc06_202 with dissolve
            sy "*Mwaah* Mnhh! *Moans* Mmmnhh..."
            sy "We would... Mmh... feel each others hearts... Nngh... racing as we kissed."
            scene ch4sc06_203 with dissolve
            sy "My appetite would only grow, and I'd begin to explore your powerful body with my little lips."
            sy "*Kiss*"
            scene ch4sc06_204 with dissolve
            sy "My lips would caress your hardened chest while my breasts rub against you."
            mc "*Moans* Fuck Sylph... Keep going."
            sy "My tiny fingers would run down your sides, and you'd hear me softly moaning in-between our kisses."
            scene ch4sc06_205 with dissolve
            sy "I'd slowly make my way down your chest, brushing my hard nipples against your battle-scars..."
            sy "*Moans* [mc]... I’m so wet already... Nngh!"
            mc "Keep going, Sylph. You’re amazing... I can even feel the magic at the tip of your lips."
            scene ch4sc06_206 with dissolve
            sy "*Lick* I would mhmh... tease your nipple with my wet tongue... *Lick*"
            scene ch4sc06_207 with dissolve
            mc "Ahhh... Sylph..."
            scene ch4sc06_206 with dissolve
            sy "*Licks* Your moans would tell me how sensitive your nipples are ... *Lick*"
            scene ch4sc06_207 with dissolve
            sy "*Moans* Mhm... Slightly salty, but I quite like them! *Lick*"
            sy "After enjoying your nipples, I'd feel encouraged by our passion and move further down."
            scene ch4sc06_208 with dissolve
            sy "Both of us would know where I’m heading, and neither of us wants me to stop."
            scene ch4sc06_209 with dissolve
            sy "I'd be about to break the sacred traditions of my species... for love, and devious desire."
            sy "*Lick* Mmhh... I'd toss away everything I’ve been taught... for the one man I hold these feelings for."
            scene ch4sc06_210 with dissolve
            sy "I'd stop at the edge of your pants and look up to you for approval."
            mc "Gods, you're one sexy little fairy..."
            "Smiling at her, you nod your approval."
            sy "I have to admit... I’ve been very curious about seeing it..."
            scene ch4sc06_211 with dissolve
            with vpunch
            sy "*Gasps* Earth-Mother!! Is this thing real?! You’re so big... Gaia herself would be pleased..."
            sy "R-Really big! Yuup!"
            scene ch4sc06_212 with dissolve
            "After recovering from the shock of seeing you, her passion and curiosity take the lead once more."
            sy "It’s so warm and... firm? Uh! It's throbbing?!"
            mc "Means it’s happy with what you’re doing..."
            sy "Oh? Then I'd better keep doing stuff to it! Lots of stuff..."
            scene ch4sc06_213 with dissolve
            with vpunch
            mc "*Moans* Ahh... Fuck..."
            mct "{i}She just took it in like that? She’s really determined...{/i}"
            mct "{i}I'm completely stretching her tight little mouth, Mhhh...{/i}"
            sy "*Muffled moan* MHNH! Mpfhhh! Mhmh..."
            scene ch4sc06_214 with dissolve
            mc "Don’t rush it. Your mouth is tiny. Relax your jaw, and take some time to adjust until you are comfortable."
            sy "Mhm-mhh... *Licks* Nnhh..."
            mc "Ahh... That’s it. Use plenty of spit."
            scene sy_lewd4 with dissolve
            "Sylph covers your tip in spit by rubbing her tongue gently all over it."
            mc "*Moans* Fuck... The way you twist your mouth around my cock..."
            sy "*Muffled moan* Mnnhh... Mh-Nhn! *Lick* Mmhn-*Suck*"
            $ renpy.pause()
            scene sy_lewd5 with dissolve
            "She hungrily speeds up, twisting her mouth and licking your tip."
            mc "*Moan* Ahhnh... Sylph... that’s fucking... incredible."
            sy "Mhm! Nngh! Amhh-Ahh-Mhmmmm!"
            mc "You’re really getting into it. Try going a little deeper."
            $ renpy.pause()
            scene sy_lewd6 with dissolve
            mc "*Moans* Ahh... Fuck Sylph. That’s it... that feels amazing."
            "Responding to your moans, she eagerly and attentively sucks and licks as she pushes you further."
            "Your cock is quickly covered in her saliva as she passionately uses her little mouth on you."
            $ renpy.pause()
            scene sy_lewd7 with dissolve
            sy "*Sucking passionately* Mhm! Mhm! Nnnhhhnhh!"
            with vpunch
            mc "Sylph I’m... I’m going to... almost there."
            "Hearing that, she tightens her mouth and keeps sucking as she takes you as deep as she can."
            with vpunch
            "She clearly wants to taste your cum and to fill her mouth with your seed."
            mc "Damn... Your first time and you want all of it? Naughty little fae..."
            with vpunch
            "Her tight little mouth and intense sucking forces you to orgasm."
            with vpunch
            scene ch4sc06_215 with dissolve
            with vpunch
            mc "Gods... You took all of it?"
            sy "*muffled* MHM! Mh-Mh!"
            mc "Be a good fae and swallow it, then."
            sy "*Muffled* mnnhh... Nnhgh... *Gulp*"
            scene ch4sc06_216 with dissolve
            "She presents you with a clean mouth."
            mc "Well done. I’m impressed."
            scene ch4sc06_217 with dissolve
            sy "*Proudly* Aaaahh."
            mct "{i}Heh... She’s so proud of herself.{/i}"
            mc "You were amazing. How did you learn all that?"
            scene ch4sc06_218 with dissolve
            sy "I’ve been practicing on my fingers... heh-heh!"
            sy "I've been hoping this day would come and I wanted to be prepared."
            scene ch4sc06_219 with dissolve
            mc "You’re quite the naughty little fae, aren’t you?"
            scene ch4sc06_218 with dissolve
            sy "Well, I needed to be ready for this moment, didn’t I?"
            scene ch4sc06_219 with dissolve
            mc "*Chuckles* You definitely delivered. Ready for more?"
            scene ch4sc06_218 with dissolve
            sy "Hold your horses, handsome. This is all you’re getting tonight."
            scene ch4sc06_219 with dissolve
            mc "Sylph... that’s mean."
            sy "*Smirks* Heh-heh-heh!"
            scene ch4sc06_218 with dissolve
            sy "You’re saying I didn’t satisfy you?"
            scene ch4sc06_219 with dissolve
            mc "You did, but-"
            scene ch4sc06_218 with dissolve
            sy "Nuh! Not happening! I’m not giving my first time to you in a musty old storage room."
            scene ch4sc06_219 with dissolve
            mc "When you put it like that... *Sigh* I’ll be patient."
            scene ch4sc06_212 with dissolve
            sy "Good... Your patience will be rewarded, I promise. Don’t worry, I won’t make you wait long."
            sy "I’m going to have a lot of fun with this guy... I can feel it."
            sy "Let’s put him back... Bye, big fella!"
            scene ch4sc06_210 with dissolve
            "Sylph hoists your pants back up from your ankles and fastens them at your waist."
            sy "There you go... My handsome adventurer."
            scene ch4sc06_209 with dissolve
            sy "Mhm..."
            scene ch4sc06_208 with dissolve
            sy "Nnngh..."
            "Sylph continues to move upwards, slowly kissing and licking and taking her time with it."
            scene ch4sc06_207 with dissolve
            $ renpy.pause()
            scene ch4sc06_206 with dissolve
            $ renpy.pause()
            scene ch4sc06_205 with dissolve
            $ renpy.pause()
            scene ch4sc06_204 with dissolve
            $ renpy.pause()
            scene ch4sc06_203 with dissolve
            $ renpy.pause()
            scene ch4sc06_202 with dissolve
            "She grabs your neck and gently pulls you down to her soft lips for a tender kiss."
            sy "*Mwah* Mnhm-Mhh..."
            scene ch4sc06_201 with dissolve
            sy "Simply delicious!"
            sy "This will have to be our thing from now on..."
            scene ch4sc06_202 with dissolve
            mc "*Mwah* What? being naked in the guild's cellar?"
            sy "*Kiss* Nuh-uh, silly! Mhm... Us... being naughty together!"
            scene ch4sc06_201 with dissolve
            sy "I can’t wait to put these handsome lips to use elsewhere..."
            scene ch4sc06_200 with dissolve
            sy "But! That’s for another time! Yuup!"
            scene ch4sc06_199 with dissolve
            sy "Ohh... Next time... MH! Yuup... Mnhh."
            sy "The things I’m going to do to [mc]... The things I’ll let him do to me..."
            scene ch4sc06_198 with dissolve
            mc "Sylph... I can hear you."
            scene ch4sc06_196 with dissolve
            sy "R-Right! Heh-heh-heh! I-I was fully aware! Yuup!"
            scene ch4sc06_197 with dissolve
            sy "Let's get dressed! Sit down with me?"
            #play music darknight_4 fadein 1.0
            stop music fadeout 1.0
            scene black with Dissolve(1.5)
            scene ch4sc06_191 with dissolve
            play music forest_1 fadein 1.0
            #stop music fadeout 1.0
            sy "There we go. Less tempting, that’s for sure!"
            mc "I preferred you without clothes."
            scene ch4sc06_190 with dissolve
            sy "And you’re calling me naughty? You’ve quite the appetite!"
            scene ch4sc06_189 with dissolve
            mc "Hard not to feel hungry when you’ve had a taste of something delicious."
            scene ch4sc06_185 with dissolve
            sy "..."
            scene ch4sc06_184 with dissolve
            sy "Let’s sit... I’m feeling weak in my knees..."
            mc "You’re levitating."
            sy "Figure of speech!"
            scene black with Dissolve(2)

        "Tell her you missed her. ({color=#2bff8b}Friendship Lock-in{/color})":
            scene ch4sc06_181 with dissolve
            mc "Missed you? So-so, I suppose."
            scene ch4sc06_180 with dissolve
            sy "That’s not funny! Not in the slightest! Hmfph!"
            scene ch4sc06_178 with dissolve
            sy "You’re a big meanie! Yup!"
            scene ch4sc06_181 with dissolve
            mc "Of course I missed you. You’re my favorite fairy, after all."
            scene ch4sc06_178 with dissolve
            sy "Yuup! That I am! *Giggle*"
            sy "Hey! I’m the only fairy you know!"
            scene ch4sc06_177 with dissolve
            mc "*Chuckles* Come on, let’s sit back down."
            scene ch4sc06_178 with dissolve
            sy "Just a biiiit more! *Hugs*"
            scene ch4sc06_177 with dissolve
            mc "Alright, alright."
            #play music darknight_4 fadein 1.0
            stop music fadeout 1.0
            scene black with Dissolve(1.5)


    scene ch4sc06_163 with Dissolve(1.5)
    play music forest_1 fadein 1.0
    #stop music fadeout 1.0
    mc "Now, what's my reward for completing the scavenger hunt?"
    scene ch4sc06_168 with dissolve
    sy "Your reward is..."
    scene ch4sc06_220 with dissolve
    sy "Tadaa! A mystery bag!"
    mct "*Sigh* I better try not to look disappointed. Could be something useful."
    scene ch4sc06_164 with dissolve
    mc "Thank you, what’s in it?"
    scene ch4sc06_165 with dissolve
    sy "Open it and see!"
    scene ch4sc06_221 with dissolve
    mc "Woah, Sylph. One, two, three, six... eighteen? Eighteen silver coins?"
    sy "Yuup! All yours!"
    mc "I can’t take this. It’s too much."
    scene ch4sc06_168 with dissolve
    sy "You can, and you will. I’ve personally saved them up for you."
    scene ch4sc06_170 with dissolve
    mc "Why? What about yourself?"
    scene ch4sc06_169 with dissolve
    sy "I’ll manage. I got inspired when I saw how hard Eliza was working towards your goal."
    scene ch4sc06_171 with dissolve
    sy "I want to contribute to that goal, to your goal as well."
    scene ch4sc06_170 with dissolve
    mc "Sylph... I don’t know what to say? Thank you."
    scene ch4sc06_173 with dissolve
    sy "I’ve never worked towards anything besides getting-by and the well-being of the guild."
    scene ch4sc06_171 with dissolve
    sy "But after you left, Eliza found her purpose and finally dragged herself out of her despair."
    sy "She's been so determined and worked so hard to achieve your goal."
    scene ch4sc06_166 with dissolve
    sy "I... I wanted to be part of that."
    scene ch4sc06_167 with dissolve
    sy "..."
    mc "Sylph..."
    scene ch4sc06_170 with dissolve
    mc "You're already part of it. From the moment we became members, you’ve been nothing but a friend and ally to us."
    mc "Even without this generous gesture, you'll always have a place with us."
    scene ch4sc06_168 with dissolve
    sy "Y-You really mean that?"
    sy "Like actually?"
    scene ch4sc06_165 with dissolve
    mc "You'd better fucking believe it."
    scene ch4sc06_164 with dissolve
    mc "I rarely make room in my life for people to matter. But you are one of those that do."
    scene ch4sc06_165 with dissolve
    sy "Gosh... [mc]. You matter to me too! Lots and lots!"
    $ sylph_trust += 5
    "Sylph's trust has increased by {size=+3}{b}{color=#2bff8b}5{/color}{/b}{/size}."
    scene ch4sc06_164 with dissolve
    mc "I’m glad. And thank you for this, Sylph."
    mc "Eliza will be thrilled to hear we just got one step closer."
    scene ch4sc06_168 with dissolve
    sy "No problem! Should we wrap up for tonight, then?"
    sy "I still have to wait for the others."
    scene ch4sc06_170 with dissolve
    mc "Yeah, let's wrap up."
    mc "Eliza should still be resting from the purification ritual."
    scene ch4sc06_171 with dissolve
    sy "Do you think it worked?"
    scene ch4sc06_170 with dissolve
    mc "Hard to say until she wakes up."
    mc "But it felt like it was working."
    scene ch4sc06_171 with dissolve
    sy "I really hope so."
    sy "She puts on a brave face, but she's really struggling with having to feed on people."
    scene ch4sc06_169 with dissolve
    sy "Go home and rest."
    sy "Don't forget you have to be up in a few hours to meet the princess."
    scene ch4sc06_170 with dissolve
    mc "Crap... I'd forgotten about that."
    mc "*Sigh* No rest for the wicked, I guess."
    scene ch4sc06_160 with dissolve
    sy "*Giggles* Definitely not! Nuh! See you soon! Nighty-night!"
    scene ch4sc06_159 with dissolve
    mc "Heh... Goodnight."
    #play music darknight_4 fadein 1.0
    stop music fadeout 1.0
    scene black with Dissolve(2)
    stop music fadeout 1.0
    jump ch5sc07
