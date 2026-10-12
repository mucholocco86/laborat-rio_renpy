label ch7sc9:

    window hide dissolve
    scene ss61 with Dissolve (1.5)
    $ renpy.pause()
    scene black with Dissolve (1.5)
    $ renpy.pause(0.5)
    scene ch7sc05_331 with Dissolve(1.5)
    play music relax_2 fadein 1.0
    #stop music fadeout 1.0
    $ renpy.pause(0.8)
    am "*Whimpers* Nnhh… no…"
    scene ch7sc05_332 with dissolve
    am "*Whines* S-Stay away… no… I-..."
    am "*Whimpers* I’ll tell him! Hnngh… he will end you! Hnnghh…"
    scene ch7sc05_334 with dissolve
    with vpunch
    am "{b}*Squeals* Aahhh!{/b}"
    am "I’m completely covered in sweat… again… *Sighs*"
    am "I had hoped these nightmares would go away…"
    scene ch7sc05_333 with dissolve
    mc "Did the cutest princess in all of Luxeron just squeal from a bad dream?"
    am "*Gasps* [mc]!?"
    am "D-Did you hear?"
    mc "Yeah I was already approaching your door and I heard you squeal."
    scene ch7sc05_334 with dissolve
    am "Sorry… I hope I didn’t frighten you?"
    am "You don’t have to worry about me… I’m a mess right now…"
    scene ch7sc05_333 with dissolve
    am "*Gasps* [mc]! W-What are you doing!?"
    mc "What does it look like I’m doing? I’m approaching you."
    am "B-But I’m covered in sweat! A-And only wearing my nightgown!?"
    scene ch7sc05_340 with dissolve
    am "I… I need a bath and perfume before you get close to me!"
    am "A-And a change of clothing!"
    scene ch7sc07_305 with dissolve
    mc "None of those things matter to me."
    mc "Are you okay?"
    "Amelia nods gently and you catch her staring at your lips."
    scene ch7sc07_306 with dissolve
    am "T-Thank you… for not letting me send you away."
    am "Your hair is different? Did you cut it?"
    scene ch7sc07_307 with dissolve
    mc "Eliza did, do you like it?"
    scene ch7sc07_306 with dissolve
    am "Mmh, I do."
    am "You look… handsome."
    scene ch7sc07_307 with dissolve
    mc "You don’t look terrible yourself… considering you just awoke from a nightmare."
    scene ch7sc07_306 with dissolve
    am "I’m a mess… but that’s sweet of you to say."
    scene ch7sc07_307 with dissolve
    mc "How long have these nightmares been happening?"
    mc "Have you told anyone about them? Maybe the clerics could give you milk of the poppy?"
    scene ch7sc07_306 with dissolve
    am "I’ve only told Frida… they’re not normal nightmares, more like vivid dreams or… visions."
    scene ch7sc07_308 with dissolve
    am "[mc], I-... I’d like to talk to you about it… will you stay a while?"
    mc "I’m not going anywhere."
    am "Thank you… you’re one of the only people I really trust with this…"
    scene ch7sc07_309 with dissolve
    am "These dreams… they have something to do with my ring…"
    mc "Your ring?"
    mc "Hmm… I do sense potent magic from it… maybe it's enchanted?"
    scene ch7sc07_310 with dissolve
    am "You can sense magic? Is it hostile?"
    mc "No, it doesn’t feel hostile, it’s hard to pinpoint, but I don’t think it’s dangerous."
    am "Oh? That’s a relief…"
    scene ch7sc07_309 with dissolve
    am "Something happened a little while ago… after one of my… dreams."
    am "Frida had just left after comforting me, and I stood by the window looking up at the night sky."
    scene ch7sc07_310 with dissolve
    am "Then suddenly my ring began to glow? And I was wrapped in what felt like a warm soothing blanket?"
    am "Then everything went dark… and I found myself in some sort of other dimension?"
    mc "Other dimension?"
    scene ch7sc07_309 with dissolve
    am "I don’t know… it’s all a little hazy to be honest, but that’s what it felt and looked like."
    am "It could all have been in my mind… but this ring… it’s special."
    mct "It has to be one of the ten enchanted rings that was used to take down Balthazar during the 1st Era."
    mct "But it doesn't have the malicious feeling that Blackheart's ring had."

    if amelia_relationship == True:
        scene ch7sc07_311 with dissolve
        mc "A special ring for a special girl."
        am "[mc]... don’t look at me like that… especially when holding me…"
        mc "How am I looking at you?"
        am "You know how… as if you’re about to kiss me…"
        scene ch7sc07_312 with dissolve
        mc "What a preposterous notion…"
        am "Y-Yeah… it would be outrageous if you did something like that while I’m covered in sweat…"
        mc "You’re not covered in sweat… only pheromones… your scent is incredible."
        scene ch7sc07_313 with dissolve
        am "Is this why you came to my room? To seduce me?"
        mc "Maybe… is it working?"
        am "Maybe… *Whimpers softly* Nnhh… I’ve missed your caress."
        am "Just… one kiss… okay?"
        mc "One kiss."
        scene ch7sc07_314 with dissolve
        am "Nnhh… just one…"
        "Amelia leans back into you, giving herself over to your embrace and her soft, delicate upper lip gently touches yours."
        "Both of you are fully aware this is the kiss… the kiss neither of you will break away from…"
        scene ch7sc07_315 with dissolve
        gw "Amelia? Are you still awake? I’d love to chat some more."
        with vpunch
        am "*Gasps* G-Gwen!? I-I’m not decent! Don’t come in!"
        mc "*Inhales* Mmmh… fuck… you smell incredible."
        gw "Amelia I’m coming in!"
        gw "I’ve seen you being indecently dressed all throughout our lives!"
        scene ch7sc07_316 with dissolve
        am "[mc]! S-Stop it! You need to get out of here! Gwen can’t see you!"
        mc "Can’t I just hide until she leaves?"
        am "No… we can’t risk it!"
        am "If word got out about what we were about to do… you’d be executed!"
        am "Please… go! The window!"
        mc "Okay I will... we'll talk more about your ring later, alright?"
        mc "I don't think you should be worried about it but we definitely need to learn more."
        am "Y-Yes! I'd like that a lot! Please... go quickly!"
        scene ch7sc07_317 with dissolve
        gw "Amelia? Are you talking to someone? I'm coming in!"
        am "One moment! I'm not decent!"

    else:
        scene ch7sc07_317 with dissolve
        gw "Amelia? You up? I’d like to chat."
        am "Gwen!? Uh! One moment! I’m indecent!"
        gw "I’m coming in, I’ve seen you indecent plenty of times!"
        am "[mc] she can’t see you in here! Quickly! The window!"
        scene ch7sc07_316 with dissolve
        mc "Okay I will... we'll talk more about your ring later, alright?"
        mc "I don't think you should be worried about it but we definitely need to learn more."
        am "Y-Yes! I'd like that a lot! Please... go quickly!"
        scene ch7sc07_317 with dissolve
        gw "Amelia? Are you talking to someone? I'm coming in!"
        am "One moment! I'm not decent!"

    scene black with Dissolve (2)
    stop music fadeout 1.0
    $ renpy.pause(0.8)
    play music relax_2 fadein 1.0
    scene ch7sc07_318 with Dissolve(2)
    $ renpy.pause(0.8)
    gw "Amelia? What’s all the commotion in here?"
    gw "I could’ve sworn I heard noises?"
    mct "That was close… looks like I made it out just in time…"
    mct "So that’s Princess Gwen? Amelia’s cousin, Christine’s daughter and Quinn’s sister."
    mct "I’m starting to get the hang of the royal lineage… anyways I better get out of here."
    scene ch7sc07_319 with dissolve
    gw "Amelia! You’re a total mess!"
    gw "You’re covered in sweat from head to toe… what have you been doing!?"
    scene ch7sc07_320 with dissolve
    am "Nothing! I just had a nightmare… I woke up like this."
    gw "Goodness! I’ll have the maids draw you a bath right away!"
    am "I appreciate the gesture, but I’m okay, I’ll just wipe myself down with a cloth."
    scene ch7sc07_321 with dissolve
    am "You said you came to chat? What about?"
    gw "Oh it wasn’t to chat about any one thing… just to catch up."
    gw "I don’t really know anyone here other than you and my brother, but he’s constantly pining after Adeline."
    scene ch7sc07_322 with dissolve
    am "Adeline? I don’t think I’ve had the pleasure of meeting her."
    gw "Ugh… my dear brother’s latest girlfriend, he’s totally head over heels for her…"
    gw "She couldn’t care less about him though… she’s clearly just dating him cause he’s a prince."
    scene ch7sc07_323 with dissolve
    am "Nothing strange about that, I don’t think anyone would put up with Quinn if he wasn’t a prince."
    gw "*Snickers* Amelia! He’s your cousin!"
    scene ch7sc07_324 with dissolve
    am "Don’t pretend like you don’t see it!"
    gw "*Giggling* I guess my brother is a bit of a dimwitted weasel from time to time…"
    scene ch7sc07_323 with dissolve
    am "All the time!"
    am "I still remember him trying to crawl under my mother’s skirt at dinner once and she promptly stepped on his hand."
    scene ch7sc07_324 with dissolve
    gw "Goodness! He was whining about that incident for an entire year!"
    gw "He’s quite pathetic for a prince… maybe he’s been spoiled too much?"
    am "There’s not much ‘man’ in Quinn… that’s for sure!"
    scene ch7sc07_325 with dissolve
    gw "Mhm-hm! Not like the one who leapt out of your window when I entered the room."
    am "I-I don’t know what you’re talking about? You’re seeing-"
    gw "Ah-Ah! I know what I saw… I only managed to see his back but…"
    gw "it was definitely a man… tall, dark and handsome."
    am "We’re done here! You may leave, I wish to be alone."
    scene black with Dissolve (2)
    stop music fadeout 1.0
    $ renpy.pause(0.8)
    scene ch7sc08_001 with Dissolve(2)
    play music forest_1 fadein 1.0
    #stop music fadeout 1.0
    $ renpy.pause(0.8)
    mct "It shouldn’t be too late, I think I’ll pay Alice a visit…"
    mct "It’s been a while since I’ve checked in on her… she’s been quite busy with her alchemy classes."
    scene ch7sc08_002 with dissolve
    gwt "That’s definitely him!"
    gwt "Good thing Amelia kicked me out when she did, otherwise I wouldn’t have caught him before he left."
    scene ch7sc08_003 with dissolve
    gwt "So he’s the mystery guy that was in Amelia’s room… while she was half-naked and covered in sweat…"
    gwt "Spicy… and daring… I didn’t think my sweet cousin had it in her."
    gwt "I can’t blame her… look at that back… he has a hot back. *Snickers*"
    scene ch7sc08_004 with dissolve
    gwt "I’ll need him to turn around…"
    gwt "Hmm… that should work."
    scene ch7sc08_005 with dissolve
    gwt "Oh my… how did that happen? *Snickers*"
    scene ch7sc08_001 with dissolve
    with vpunch
    gw "{b}*Squeals*{/b} Aiiyh! Owh! Owhh…"
    scene ch7sc08_006 with dissolve
    mc "Hmm?"
    gw "Owh… I’m such a klutz!"
    mct "That’s Princess Gwen? Did she follow me here?"
    scene ch7sc08_007 with dissolve
    mc "Hey… are you okay?"
    gw "W-Who are you!? I’ll call the guards!"
    scene ch7sc08_008 with dissolve
    mc "Settle down, I’m one of the guards… Amelia’s bodyguard to be specific."
    mc "I’ll ask again, are you okay?"
    gw "Oh… I guess I am? I didn’t see where I was walking…"
    scene ch7sc08_009 with dissolve
    gw "Before I knew it I stumbled into this vase that was placed on the table there."
    gw "My ankle might’ve been twisted during the fall… it’s a little sore."
    scene ch7sc08_010 with dissolve
    mc "Here… let’s see if you can put any weight on it… the floor is no place for a princess."
    gw "Y-You know who I am? T-Thank you, this is most kind of you…?"
    scene ch7sc08_011 with dissolve
    mc "Lord [mc], but just call me [mc]."
    gw "[mc]... I haven’t heard that name before… a unique name for a unique man."
    mc "*Scoffs* I’m not that unique… c’mon, let’s get you on your feet."
    scene ch7sc08_012 with dissolve
    gw "Thank you… you act more like a prince than my brother…"
    gw "*Under her breath* {size=-10}{b}By the gods you’re handsome…{/b}{/size}"
    mc "I don’t imagine it takes a lot to be more prince-like than your brother…"
    scene ch7sc08_013 with dissolve
    gw "*Snickers* Careful… you’re only a lord, if anyone heard you insulting a prince, it would be a permanent stay in the dungeons."
    mc "I’ll be fine, I have a feeling you won’t tell on me."
    gw "No… I wouldn’t."
    scene ch7sc08_014 with dissolve
    gw "*Whimpers* Owh-owh! I guess it really is twisted…"
    gw "W-What do I do? I can’t walk back to my room like this?"
    mc "*Sighs* In the spirit of being prince-like… here…"
    scene ch7sc08_015 with dissolve
    gw "*Gasps* Oh my! Oh you’re bold!"
    gw "First you make fun of the prince…"
    gw "Then you put hands on his sister… *giggling* I’ve never met a man who dared such a thing."
    scene ch7sc08_016 with dissolve
    mc "I can be quite daring…"
    gw "*Quietly* {size=-10}{b}I can see why Amelia is so smitten…{/b}{/size}"
    mc "Hmm?"
    gw "I said, I can see that."

    if harem_path == True:
        scene ch7sc08_016a with dissolve
        mct "*Chuckles* She has no idea just how daring I can be..."
        mct "I could add her to my harem... a princess or two wouldn't hurt."
        mct "Besides Bennen already foolishly made the remark of giving her and her mother to me."
        mct "Maybe I'll take him up on his offer, even if made in jest."
        mct "Hells... maybe I'll even take his throne while I'm at it."
        mct "After what he did to Merida... I have no faith in him as a king."
        mct "I'll just have to wait for the timing to be right... then he'll pay for harming Merida."
        scene ch7sc08_016 with dissolve
        mc "Think you can handle me, Princess?"
        gw "*Snickers softly* Mh-hm..."

    else:
        pass

    scene ch7sc08_017 with dissolve
    gw "In the spirit of you being daring… let’s put that notion to the test?"
    gw "I dare you… to carry me to my bedroom."
    mc "Carrying a beautiful princess to her bedroom? *Chuckles* Child’s play."
    scene ch7sc08_018 with dissolve
    gw "I didn’t say the dare stops at my bedroom… *Snickers*"
    mc "Seems like I’ve got my hands on a cheeky princess…"
    gw "I have a feeling you can handle a cheeky woman."
    scene ch7sc08_017 with dissolve
    gw "You better get going… the faster we get to my room, the faster you find out what the next dare is."
    mc "Right away, Your Highness."
    scene black with Dissolve (1.5)
    $ renpy.pause(0.5)
    "You carry Gwen through the halls, avoiding guard patrols along the way and eventually make it to the royal wing."
    scene ch7sc08_019 with Dissolve(1.5)
    $ renpy.pause(0.8)
    mc "This is your room?"
    gw "Mhm-hm! The one to the left is my mother’s. Quinn and Adeline’s room is further down the hall."
    gw "Nicely done on avoiding the guards, you’re quite agile, even when holding me."
    scene ch7sc08_020 with dissolve
    mc "*Chuckles* You almost got us caught several times… with all that giggling…"
    gw "You can’t expect a woman to hold back all her giggles when she’s being carried by a man for the first time."
    scene ch7sc08_019 with dissolve
    mc "First time huh?"
    gw "First time. You think I’d let just any man put his hands on me?"
    scene ch7sc08_020 with dissolve
    mc "No… you don’t strike me as the type who’d settle for just anyone."
    gw "I’m glad to see you’ve gotten to know me a little on the way here."
    scene ch7sc08_019 with dissolve
    gw "Now for your next dare… I dare you to… carry me into my bed."
    mc "I had a feeling you would say that…"
    scene ch7sc08_020 with dissolve
    gw "I can’t walk with my ankle being twisted… I guess this dare was obvious."
    scene ch7sc08_021 with dissolve
    gw "*Giggling* Y-You’re really doing it!?"
    mc "You thought I wouldn’t? Grab the door handle, princess."
    gw "Heavens… you must have giant balls… entering a princess’s private chambers… very well, then."
    scene black with Dissolve (1.5)
    $ renpy.pause(0.5)
    scene ch7sc08_022 with Dissolve(1.5)
    $ renpy.pause(0.8)
    mc "So this is how a princess lives?"
    gw "I know, I know… it’s a little messy, we only just recently arrived."
    gw "I’ll have it organized in a few days once I get settled."
    scene ch7sc08_023 with dissolve
    mc "Here we are…"
    gw "Mmh… you managed to protect my ankle all the way to my bed, you truly are a capable bodyguard."
    gw "Careful when you put me down… I’m not wearing panties."
    scene ch7sc08_024 with dissolve
    mc "Is that so? I guess I’m not the only one who has a daring personality."
    gw "You got that right… mmh… you know how to handle a woman… how to touch her."
    scene ch7sc08_025 with dissolve
    mc "I know my way around a woman’s body."
    "You gently apply pressure to the bottom of Gwen’s delicate foot."
    gw "*Moans softly* Oh-Ohhh… oh that’s… so good… you really do know a woman’s body…"
    mct "I shouldn’t be able to apply this amount of pressure without causing her pain if her ankle was hurt…"
    scene ch7sc08_026 with dissolve
    gw "I didn’t ask you to stop… why did you?"
    gw "My body was starting to tingle in all the right places…"

    ####Ability check####
    if charisma >= 23:
        scene ch7sc08_027 with dissolve
        mc "I don’t know what you’re up to, but you lied to me… your ankle isn’t hurt in the slightest."
        mc "I don’t care for games… especially those played by nobles with no regard for others."
        gw "It wasn’t like that… I was just curious about you!"
        gw "I acted impulsively to have an excuse to get to know you… you can’t say you didn’t enjoy it?"
        scene ch7sc08_027a with dissolve
        gw "There's a spark between us... I know it, I know you felt it too!"
        gw "It was silly of me to pretend to be hurt... I admit it, okay?"
        gw "But I wanted to get to know you, and the idea just came to my mind and I acted upon it."
        scene ch7sc08_027b with dissolve
        gw "To tell you the truth... this is new to me... being interested in a man."
        gw "I'm not saying I like you or anything... just that I feel curious about you."
        scene ch7sc08_027c with dissolve
        mc "You're right... there is something of a spark between us."
        mc "And I'm rather curious about you too..."
        mc "In the spirit of getting to know each other, let's put this little stunt of yours behind us."
        "Gwen's face lights up with a soft smile, she seems genuinely happy to hear your words."
        scene ch7sc08_027a with dissolve
        gw "Thank you! I was hoping you'd see reason behind my actions!"
        gw "You better take your leave for tonight... but I'm looking forward to our next encounter."
        scene ch7sc08_027c with dissolve
        mc "Me too, sweet dreams... Princess."

    elif leadership >= 22:
        scene ch7sc08_027 with dissolve
        mc "I don’t know what you’re up to, but you lied to me… your ankle isn’t hurt in the slightest."
        mc "I don’t care for games… especially those played by nobles with no regard for others."
        gw "It wasn’t like that… I was just curious about you!"
        gw "I acted impulsively to have an excuse to get to know you… you can’t say you didn’t enjoy it?"
        mc "I don't enjoy being lied to, no."
        mc "You're a princess, Gwen. You're at the top of the social hierarchy, act like it."
        scene ch7sc08_027b with dissolve
        gw "*Sighs deeply* You're right... I know you are..."
        gw "I'm always told to set a good example. But what does that mean—what does that even look like?"
        scene ch7sc08_027c with dissolve
        mc "It starts with respecting others, even those below your own standing."
        mc "To lead, you must inspire others to follow."
        mc "You have a strong personality, one which could be fit to lead others well."
        mc "But only if you do it truthfully and by being yourself."
        scene ch7sc08_027a with dissolve
        gw "[mc]...."
        gw "You truly mean this? That I have what it takes to... lead others?"
        scene ch7sc08_027c with dissolve
        mc "I do... but it's not an easy thing to do, and it won't happen over night."
        mc "But start with being honest, and take it one step at a time."
        mc "If you make an actual effort, then I will be happy to call you a friend."
        "Gwen's face lights up with a soft smile, she didn't expect this response from you."

    elif persuasion >= 14:
        scene ch7sc08_027 with dissolve
        mc "I don’t know what you’re up to, but you lied to me…"
        mc "Your ankle isn’t hurt in the slightest."
        mc "Normally I like playing games… but only if both parties have fun doing it."
        gw "It wasn’t like that… I was just curious about you!"
        gw "I acted impulsively to have an excuse to get to know you… you can’t say you didn’t enjoy it?"
        scene ch7sc08_027a with dissolve
        gw "When we flirted... you liked the game as well... I know you did."
        gw "Yes I may have started it off a little questionable... but it got the ball rolling!"
        scene ch7sc08_027c with dissolve
        mc "You're right... I liked playing with you, but I like it better if you're honest with me."
        mc "You can lie to others all you like, but if you want to play with me... you'll be honest."
        "Gwen nods with a smile, she likes the idea of getting to play with you in the future."
        scene ch7sc08_027a with dissolve
        gw "Honesty... just between us? Deal."
        gw "You better leave for tonight... while I think of our next... game. *Snickers softly*"
        scene ch7sc08_027c with dissolve
        mc "*Chuckles* I already look forward to it. Princess."


    elif intimidation >= 15:
        scene ch7sc08_027 with dissolve
        mc "I don’t know what you’re up to, but you lied to me… your ankle isn’t hurt in the slightest."
        mc "I don’t care for games… especially those played by nobles with no regard for others."
        gw "It wasn’t like that… I was just curious about you!"
        gw "I acted impulsively to have an excuse to get to know you… you can’t say you didn’t enjoy it?"
        mc "Goodnight Gwen."
        gw "[mc]- wait!"
        scene ch7sc08_027d with dissolve
        with vpunch
        mc "Don't ever lie to me again."
        mc "You won't like the result... Princess."
        gw "..."
        scene ch7sc08_027b with dissolve
        gw "Did you just-"
        scene ch7sc08_027d with dissolve
        mc "I did."
        mc "I'll see you around and next time... you'll be honest."
        "Gwen nods in disbelief of your balls, threatening a princess so nonchalantly."

    else:
        mc "Goodnight Gwen."
        gw "[mc]- wait!"

    scene black with Dissolve (2)
    stop music fadeout 1.0
    $ renpy.pause(0.8)
    "You take your leave, having had enough of royal affairs for one evening, you head to the academy in search of Alice."


    if irene_alive == True:
        scene ss89 with Dissolve (1.5)
        $ renpy.pause()
        play music summon_3 fadein 2.0
        scene black with Dissolve (1.5)
        $ renpy.pause(0.5)
        scene ir34 with Dissolve (8)
        $ renpy.pause()
        scene ir35 with Dissolve (1.5)
        $ renpy.pause()
        scene ir36 with Dissolve (1.5)
        $ renpy.pause()
        scene ir37 with Dissolve (1.5)
        $ renpy.pause()
        irt "How much longer must I wait…"
        irt "How much longer before… I’m able to avenge Alana?"
        irt "She won’t find peace in the afterlife until I’ve eliminated the reason for her death…"
        irt "Rin…"
        irt "Viperia is right, Rin is the one responsible for Alana’s death… I need to be the one to kill her."
        irt "She bested me last time… due to my own foolishness…"
        irt "This time I’m prepared… I’ve been training day and night… I’m… ready."
        irt "Alana…"
        irt "I won’t fail you… I… promise."
        scene ir38 with Dissolve (1.5)
        vi "Ah, there you are."
        vi "I bring exciting news little one."
        scene ir115 with dissolve
        ir "Viperia, I thought we didn’t have a training session until later?"
        ir "Why are you disturbing me?"
        scene ir116 with dissolve
        vi "*Snickers* Mhmm…"
        ir "Speak!"
        scene ir117 with dissolve
        vi "You seriously need to chill out, you’ll never avenge sweet Alana with that attitude."
        vi "Have you learned nothing from all our training?"
        scene ir118 with dissolve
        ir "I have learned everything I need to know to end Rin… why are we prolonging the matter?"
        scene ir117 with dissolve
        vi "Didn’t I just announce I came here with exciting news?"
        scene ir119 with dissolve
        vi "It’s time, little one."
        vi "We’ve stopped sending members after her, to give her a false sense of security."
        vi "Instead we’ve been observing her habits… taking note of her locations…"
        scene ir117 with dissolve
        vi "She will be isolated, the perfect time to strike… pack your stuff, we’re leaving in an hour."
        scene ir115 with dissolve
        ir "This better not be another one of your tricks…"
        vi "No tricks, the time for your vengeance has come."
        scene ir120 with dissolve
        vi "Meet me at the front gate in an hour, we’ll bring an entourage of shadow-brothers with us."
        vi "We’re leaving nothing to chance this time… as long as Rin remains alive… she remains a stain on our record."
        vi "We’re removing this stain once and for all."
        scene black with Dissolve (1.5)
        $ renpy.pause(0.5)
        stop music fadeout 1.0


    else:
        pass

    scene ss22 with Dissolve (1.5)
    stop music fadeout 1.0
    $ renpy.pause()
    scene black with Dissolve (1.5)
    $ renpy.pause(0.5)
    play music relax_2 fadein 2.0
    scene ch7sc08_028 with Dissolve (2)
    $ renpy.pause(0.8)
    al "*Hums* Mh-nh-hn-hm…"
    al "Juuuuust a little dash of dried Willow-leaves."
    scene ch7sc08_029 with dissolve
    al "Perfect! This is the blue hue Professor Venetos talked about in class!"
    al "Now it just has to brew for a short while before I fill it into bottles."
    scene ch7sc08_030 with dissolve
    mc "*Clears throat* Found you at long last."
    al "[mc]! Hii!!"
    al "Looks like you found me!"
    scene ch7sc08_031 with dissolve
    al "You’ve been looking for me?"
    mc "Yeah, I went to your dormitory but you weren’t there, so I started checking around the classrooms."

    if charisma >= 18:
        mc "You look great, is that a new top?"
        al "It is! Thank you for noticing… you look dashing as well I might add."
        al "I like what you’ve done with your hair."

    else:
        pass

    mc "Well… am I not going to get a hug?"
    scene ch7sc08_032 with dissolve
    al "Of course! Incoming! *Giggling happily*"
    mc "Come here you!"
    scene ch7sc08_033 with dissolve
    with vpunch
    mc "Hnngh! That’s more like it…"
    al "I’m so glad you came to see me! But I’m getting alchemy dust all over you…"
    mc "A hug from you Alice is worth all the alchemy dust in this entire room."
    scene ch7sc08_034 with dissolve
    al "In that case… I’ll keep hugging you for a while!"
    mc "I wouldn’t have it any other way…"

    if alice_path == True:
        scene ch7sc08_035 with dissolve
        al "Mmmh!"
        al "Missed you… mmh…"
        scene ch7sc08_034 with dissolve
        mc "Missed you too."
        al "I’m really glad you came to see me…"
        scene ch7sc08_035 with dissolve
        al "Mmmh!"
        mc "You already said that… mmh…"
        scene ch7sc08_034 with dissolve
        al "Then it must be true! *Giggles softly*"
        al "Kiss me again."
        scene ch7sc08_035 with dissolve
        mc "Mmh… you’re cute."
        al "I love you… I love you so much… mmh… you’re such a good kisser."
        scene ch7sc08_034 with dissolve
        mc "*Chuckles* I’ve had prac-"
        al "Uh-uh! Don’t say it! I don’t want to think about all the women who helped make you kiss this good…"
        scene ch7sc08_035 with dissolve
        al "Mmh! Mmh… I just want to experience your lips and tongue… for myself… mmhh…"
        mc "You’re not half bad yourself… mmh… I love the taste and feel of your big lips."
        scene ch7sc08_034 with dissolve
        al "Good… you’ve already claimed me so they’re yours until the end of our days… mmh."
        mc "Just the way I like it."


    else:
        pass

    mc "How are you doing? It’s been a while since we saw each other."
    scene ch7sc08_036 with dissolve
    al "I’m doing well, just been so occupied with my classes here at the Academy."
    mc "Oh yeah? What have you been studying as of late?"
    scene ch7sc08_034 with dissolve
    al "Currently we’re learning about various water-based elixirs and potions."
    al "Such as… Water-breathing elixirs, Sea-glider stamina elixirs and Poro-weed potions."
    scene ch7sc08_036 with dissolve
    mc "It’s good to see you so interested in all of this."
    al "Professor Venetos is such a brilliant teacher, she makes it easy to digest but also keeps us on point."
    scene ch7sc08_034 with dissolve
    mc "I believe I met her during Amelia’s nameday celebrations, she seemed nice."
    scene ch7sc08_036 with dissolve
    al "She is! She can be a little direct, especially in class, but she’s also kind and understanding."
    mc "Sounds like you look up to her quite a bit?"
    scene ch7sc08_034 with dissolve
    al "How could I not?"
    al "She’s a great mentor and she knows a lot, I can only hope to be as well-versed in alchemy as her one day."
    scene ch7sc08_037 with dissolve
    mc "You will be, with how ambitiously you’ve been studying, you’ll become one of the greatest alchemist of our time."
    al "Stop it… I doubt that… you… you really think so?"
    mc "Mmh, I know so."
    al "[mc]... thank you, it means the world to me knowing that you believe in me."
    scene ch7sc08_036 with dissolve
    mc "I always will."
    mc "Now, what were you up to when I arrived? Isn’t it kind of late to be working on a project?"
    scene ch7sc08_034 with dissolve
    al "I couldn’t sleep and then I finally came up with the solution for the elixir we were learning about!"
    al "So I just had to come here and make it! I couldn’t possibly wait until class tomorrow…"
    scene ch7sc08_033 with dissolve
    al "In fact, it should be ready about now!"
    scene ch7sc08_038 with dissolve
    al "Come! You can help me pour it into bottles!"
    mc "*Chuckles* Great… what did I get myself into?"
    al "Nothing you can’t handle! Come, come!"
    al "There should already be bottles on the table over here."
    scene ch7sc08_039 with dissolve
    mc "You’ve already brewed the pink ones?"
    al "No they are from previous batches, they aren’t finished elixirs but mix-ins."
    al "We’re filling the empty bottles with the brew I’ve got here."
    scene ch7sc08_040 with dissolve
    mc "Sounds simple enough."
    al "Mhm, it is! The hard part is brewing the mixture."
    al "I’ll bring you a little at a time to fill into the bottles."
    mct "*Chuckles* Heh… it’s good to see her like this, she’s totally in her element."
    scene ch7sc08_041 with dissolve
    al "You just have to hold em still like this."
    "Alice gently touches your hand and guides it into a steady position for her to pour the brew."
    al "Don’t move, I don’t want to spill it on you."
    mc "What would happen if you did?"
    scene ch7sc08_042 with dissolve
    al "You would be erect for four hours."
    mc "Wait… really? What the hell is this potion?"
    al "It’s an endurance potion, in its current state it would be sexual endurance."
    al "We need to add the mix-in from the pink stuff to turn it into muscle endurance."
    scene ch7sc08_041 with dissolve
    al "Now keep your hands steady for me to pour the liquid."
    mc "Four hour erection if I don’t… no pressure. *Chuckles*"

    if alice_path == True:
        al "I’m going to keep one of these for when you finally take me on a date."
        mc "Oh boy… you sure you can handle that?"
        scene ch7sc08_042 with dissolve
        al "Oh I’m sure… it works on women too, I’ll drink it with you."
        al "We’ll do things during those four hours you couldn’t even imagine doing with women who haven't been ‘boosted’."
        scene ch7sc08_041 with dissolve
        al "Now steady hands mister! *Snickers*"
        scene black with Dissolve (1.5)
        $ renpy.pause(0.5)


    else:
        scene black with Dissolve (1.5)
        $ renpy.pause(0.5)

    "You and Alice make short work of filling the bottles in just fifteen minutes."
    scene ch7sc08_043 with Dissolve (1.5)
    $ renpy.pause(0.5)
    al "Great work! We make a good team."
    mc "That we do… thank you for not spilling any of that on me."
    al "Now you just got to add a few droplets of the pink mix-in to each elixir and they’ll be done."
    scene ch7sc08_044 with dissolve
    al "You can handle that while I put away the brew."
    mc "Sure… shouldn’t be a problem."
    al "Best assistant ever! *Giggling* I need you to visit me more often!"
    scene ch7sc08_045 with dissolve
    mc "This was a one time thing… don’t get any ideas…"
    al "We both know you’ll come visit me again… right?"
    mc "Right… fine, I suppose it wasn’t the worst thing in the world."
    scene ch7sc08_046 with dissolve
    al "Phew! This thing was heavier than I remember."
    mc "You could’ve let me carry it."
    scene ch7sc08_047 with dissolve
    al "Nonsense! I’m perfectly capable of doing this, I’ve done it many times when you aren’t here."
    al "But if you really want to put your muscles to work, I have a few tasks for you-"
    scene ch7sc08_048 with dissolve
    al "Yoouuu- [mc]! No!"
    al "Not that pink one!"
    scene ch7sc08_049 with dissolve
    with vpunch
    al "Quickly! Get down!"
    scene ch7sc08_050 with dissolve
    with vpunch
    mc "Hnngh! Damn girl!?"
    al "Hold your breath until the smoke dissipates!"
    scene ch7sc08_051 with dissolve
    al "Don’t breathe!"
    mc "Mmmh-mmhfffhh…"
    "Alice keeps a tight grip around your mouth, ensuring you don’t accidentally inhale."
    scene ch7sc08_052 with dissolve
    al "It should be gone now… phew… that was close."
    mc "Mmffh… mhhh…"
    scene ch7sc08_053 with dissolve
    al "Sorry… that almost ended badly… if we had inhaled those fumes we’d been delirious for a couple of hours."
    "You feel Alice’s gentle touch as she investigates you, carefully running her delicate fingers around your face and hair."
    al "Please tell me you’re okay?"
    scene ch7sc08_054 with dissolve
    mc "I’m okay…"
    mc "You really jumped me to get me out of the way? You could’ve gotten hurt."
    scene ch7sc08_053 with dissolve
    al "I didn’t even think… I just wanted you out of harm's way."
    scene ch7sc08_055 with dissolve
    al "I forgot one of the mix-ins isn’t compatible with this brew… I should’ve removed it before I even started."
    al "You almost got hurt because of me…"
    scene ch7sc08_054 with dissolve
    mc "Don’t be silly… I could’ve asked if it was the correct mix-in, besides… it wouldn't have harmed me."
    scene ch7sc08_053 with dissolve
    al "I know you can heal… that doesn’t mean I want you to get hurt… especially because of me."
    al "I understand if you don’t want to help me brew again in the future…"
    scene ch7sc08_054 with dissolve
    mc "I’d be happy to. If anything this just added to the excitement."
    scene ch7sc08_055 with dissolve
    al "You’re crazy…"
    al "Next time I’ll be better prepared… this was a little too exciting…"
    scene ch7sc08_056 with dissolve
    al "*Sighs* We should probably get up?"
    scene ch7sc08_054 with dissolve
    mc "Nah… I’m good."
    scene ch7sc08_053 with dissolve
    al "*Giggling* What? You’re good?"
    scene ch7sc08_054 with dissolve
    mc "Mhm… I’m good right here."
    scene ch7sc08_056 with dissolve
    al "Alright then… I suppose I can’t argue against being held by you…"
    scene ch7sc08_055 with dissolve
    al "How're things at Haven? Are Cassandra and Gina settling in alright?"
    scene ch7sc08_057 with dissolve
    mc "Yeah, they have begun furnishing their homes, they seem to be enjoying themselves."
    mc "I wasn't sure how Gina would adjust, but keeping her occupied seemed to have done her some good."
    scene ch7sc08_056 with dissolve
    al "What she went through… I bet she’ll welcome anything that doesn’t give her time to think about… all that."
    scene ch7sc08_054 with dissolve
    mc "Yeah… I hope being friends with Cassandra and Eliza will help her get through it."
    scene ch7sc08_053 with dissolve
    al "Being friends with you is also a factor, you’re the man who saved her… twice."
    al "You will play a big role in her recovery, especially mentally… you represent her future, a safe future."
    scene ch7sc08_054 with dissolve
    mc "I don’t know Alice… I’m not sure how to help her…"
    scene ch7sc08_056 with dissolve
    al "You don’t have to do any one thing… just be there for her."
    al "She just needs to know you’re there to support her, to listen to her… for her to lean on should she need it."
    scene ch7sc08_055 with dissolve
    al "Just be yourself and it’ll be enough… it always is."
    scene ch7sc08_057 with dissolve
    mc "I hope you’re right… she deserves a better life."
    scene ch7sc08_055 with dissolve
    al "You’ve already given her exactly that, now you just need to keep doing it until she understands it isn’t just temporary."
    al "Once she comes to terms with this being her new life… that’s when I believe she’ll fully heal."
    scene ch7sc08_057 with dissolve
    mc "Since when did you become such a scholar in the human psyche?"
    scene ch7sc08_053 with dissolve
    al "Since I had to endure you and Flynn as a child… you were fascinating subjects! *Snickers*"
    scene ch7sc08_054 with dissolve
    mc "Alright… times up, I’ve gotta get home and rest… it’s been quite the day."
    scene ch7sc08_053 with dissolve
    al "You… could spend the night at my dorm?"
    al "I wouldn’t mind… my bed is big enough for us both."

    ####Choice####
    menu:
        "Spend the night with Alice. ({color=#ff8cdd}Romance{/color})":
            scene ch7sc08_054 with dissolve
            mc "You know… your bed certainly sounds better than having to run all the way back to Haven."
            scene ch7sc08_055 with dissolve
            al "It does… doesn’t it?"
            al "My bed has a rule though…"
            scene ch7sc08_057 with dissolve
            mc "Hmm? Do tell."
            scene ch7sc08_056 with dissolve
            al "*Quietly* {size=-10}{b}We must sleep naked…{/b}{/size}"
            mc "Hmm?"
            scene ch7sc08_055 with dissolve
            al "Naked, the rule is we sleep… naked."
            al "And cuddles are mandatory!"
            scene ch7sc08_057 with dissolve
            mc "Naked cuddles? Now that’s something I can get behind."
            "Alice giggles softly at the thought of you being behind her."
            scene ch7sc08_055 with dissolve
            al "Let’s not waste anymore time here… my bed awaits us!"
            scene black with Dissolve (2)
            #play music morning_1 fadein 1.0
            stop music fadeout 1.0
            $ renpy.pause(0.8)
            play music lewd_1 fadein 1.0
            scene ch5sc13_045 with Dissolve (2)
            #stop music fadeout 1.0
            with vpunch
            $ renpy.pause(0.5)
            al "*Moans softly* Aahh… You know my body so well… mmh."
            scene ch5sc13_046 with dissolve
            mc "You have a great body Alice… mmh… warm, soft and slender… mmh."
            scene ch5sc13_047 with dissolve
            al "*Moans* Aahh… the way you’re pressing against me… mmh… I love it…"
            al "I love you… mmh… let me be yours…"

            if alice_path == True:
                scene ch5sc13_048 with dissolve
                al "P-Please… it’s been so long… we haven’t been intimate since your return from Aruna…"
                mc "I’m sorry for making you wait this long… mmh… are you ready?"
                al "Y-Yes… mmh…"

            else:
                pass

            scene ch5sc13_048 with dissolve
            al "Please be gentle tonight, I’m a little sore, I fingered myself for over an hour this morning- Mmh…"
            scene al_lewd10 with fade
            $ renpy.pause(2, hard=True)
            al "*Moans* Ahhh! Oh… Ohhh! This is sooooo much better than my fingers… mmmh!"
            mc "Fuck Alice… you’re tight… even when just dipping my tip inside of you."
            al "Mmh… I needed this… I needed you…"
            al "Ahhh… yes… I feel you… make love to me… Nnnhh!"
            mc "I can’t wait for our date… mmh… that sex-enhancing elixir is going to be wild…"
            mc "I have a feeling sharing that with you… my long-lost childhood friend… is going to be something we won’t forget."
            $ renpy.pause()
            scene al_lewd9 with fade
            $ renpy.pause(2, hard=True)
            with vpunch
            al "Aiiyhh! D-Don’t say such lewd things out loud… you’re going to make me cum!"
            mc "Mmh! I love how tight it makes you when I call you my childhood friend."
            with vpunch
            al "Aiiyh! [mc]! I’m warning you! I’m going to make us cum!"
            al "Ahh… you feel so good… mmh… we’re childhood friends… making love… mmh… we’re… one! AHhHhh!"
            $ renpy.pause()
            with vpunch
            scene ch5sc13_050 with dissolve
            al "Heavens! You went so deep and filled me! Mmhghh!"
            scene ch5sc13_045 with dissolve
            "Enjoying the feeling of you inside of her, your smell, the weight of your masculine frame pinning her down-"
            "-And the primal, natural sensation of your joint climax spilling out of her, she eagerly kisses you."
            al "Mmmghh… thank you… d-don’t pull out…"
            scene ch5sc13_046 with dissolve
            mc "Mmh… I won’t, turn to your side… I believe I promised you a naked cuddle?"
            al "Mmgh-mmh… yes… you did… mmh… careful not to pull out!"
            scene ch7sc08_058 with dissolve
            al "*Giggling happily* Mmh! This is exactly what I had in mind for naked cuddles!"
            $ alice_path = True
            al "Us naked, together in my bed… your warm hands on my breast… your… cock, inside of me."
            mc "*Chuckles* Mmmh…"
            scene ch7sc08_059 with dissolve
            al "Admit it… you’re happy… right?"
            scene ch7sc08_060 with dissolve
            mc "I’m happy, Alice."
            mc "I’m happy right here with you."
            scene ch7sc08_059 with dissolve
            al "I hoped you would say that… mmh…"
            al "I really look forward to our date."
            scene ch7sc08_060 with dissolve
            mc "It’ll be everything you wish for… I promise."
            scene ch7sc08_059 with dissolve
            al "I have no doubt… as long as we’re together, it’ll be amazing."
            al "Speaking of together… my mom wrote me recently, asking about how I was settling into the big city."
            al "I was thinking… instead of writing her back… I’d go back to Riverside and visit her."
            scene ch7sc08_060 with dissolve
            mc "Mmh, I’ve been thinking about doing a small trip back to Riverside, I’d like to see Gibson and Maya."
            scene ch7sc08_059 with dissolve
            al "Yeah… I’ve heard, that’s why I’m bringing it up… we could make it a group trip?"
            scene ch7sc08_060 with dissolve
            mc "I like the sound of that… how about we go once things calm down a little?"
            mc "I know Luna really wants to come with us to Riverside, now that Cassandra is doing better it might be time."
            scene ch7sc08_059 with dissolve
            al "Yeah, I’d love to show her around Riverside. Okay!"
            al "We make a trip for everyone! Sabrina and Flynn want to come too I know that for certain!"
            scene ch7sc08_060 with dissolve
            mc "Sounds good… now, let’s get some rest."
            mc "Thank you for an amazing night, Alice."
            scene ch7sc08_059 with dissolve
            al "Goodnight handsome! *Giggling*"
            al "And you never have to thank me... I want this as much as you... I need this as much as you."

        "Return to Haven for a night’s rest. ({color=#2bff8b}Friendship{/color})":
            scene ch7sc08_054 with dissolve
            mc "Sorry, I better sleep at Haven, I haven’t gotten to spend much time there as of yet."
            $ alice_path = False
            mc "I’m sure Cassandra and Gina would feel more comfortable with me being there."
            scene ch7sc08_053 with dissolve
            al "Right… I think they would as well, goodnight then?"
            scene ch7sc08_054 with dissolve
            mc "Goodnight Alice, I’ll see you around."
            scene ch7sc08_053 with dissolve
            al "Oh! Before you leave, I wanted to let you know we have been talking about going back home."
            al "Just for a little visit and check up on everyone in Riverside."
            al "You should come! Gibson... Maya... I know they'd love to see you!"
            scene ch7sc08_054 with dissolve
            mc "Yeah... I would like to see them again... maybe... maybe I'll join."
            mc "It would have to be when things calm down a little though."
            scene ch7sc08_053 with dissolve
            al "Of course! We've just been talking about it, nothing is planned yet!"
            al "Okay, that's all! Goodnight!"

    scene black with Dissolve(2)
    #play music explore_2 fadein 1.0
    stop music fadeout 1.0
    $ renpy.pause(0.8)
    scene ss47 with Dissolve(2)
    $ renpy.pause()
    scene ss19 with Dissolve(2)
    $ renpy.pause()
    play music forest_1 fadein 2.0
    scene ch7sc08_061a with Dissolve(2)
    $ renpy.pause(0.8)
    cas "Sweetie, there's something I've been meaning to talk to you about."
    cas "It's important and not something we should just brush over..."
    lu "I know I talk about him a lot... it's just that I want to be at the guild with him!"
    scene ch7sc08_061 with Dissolve(2)
    $ renpy.pause(0.8)
    mct "Looks like Luna’s here? I guess she’s been dying to check on her mom."
    lu "I wish I could attend class with him! I hate that I have to stay away just because of… Rose! Tsk!"
    lu "Mother? What’s got you smiling like that-"
    scene ch7sc08_062 with dissolve
    "Cassandra answers her by pointing in your direction as you approach."
    lu "What are you pointing at-"
    scene ch7sc08_063 with dissolve
    lu "[mc]! Yay!"
    lu "We’ve been waiting for you!"
    scene ch7sc08_064 with dissolve
    mc "Oh? I could get used to having a couple of beautiful women waiting for me."
    scene ch7sc08_063 with dissolve
    lu "A gentleman is not supposed to make women wait you know? *Giggles*"
    scene ch7sc08_065 with dissolve
    lu "Can you believe him?"
    cas "*Snickers* It seems we better teach him a lesson, wouldn’t you say, darling?"
    lu "Are you thinking what I’m thinking? *Giggling*"
    mc "What are you-"
    scene ch7sc08_066 with dissolve
    with vpunch
    bth "{size=+10}{b}Magic lesson!{/b}{/size}"
    mc "*Chuckles* Magic lesson?"
    lu "It’ll be fun!"
    cas "Not to mention it’ll be good for you to learn a few things now that you’re attending the guild."
    scene ch7sc08_065 with dissolve
    lu "Is there anywhere around Haven we can practice magic?"
    cas "Mhm-hm, I know a few spots that would be suitable, follow me."
    lu "Wait... you wanted to talk to me about something before [mc] arrived?"
    cas "I did and still do, but now's not the time, we will talk later sweetie."
    lu "Alright! Then let's get going! Is it far from here?"
    scene ch7sc08_067 with dissolve
    cas "It’s not too far, there’s a small clearing in the woods nearby."
    lu "Just wait until you see [mc] in action mom! He’s great!"
    cas "Oh I have a feeling he won’t disappoint sweetie…"

    if luna_relationship == True:
        scene ch7sc08_068 with dissolve
        cas "Your boyfriend is handsome, he’s respectful, and he’s kind…"
        cas "But as your mother… it’s my responsibility to see if he…"
        cas "Measures up in all areas of life… *Snickers*"
        lu "[mc] is awesome! Measure him all you want, mom!"
        lu "You’ll see he’s worthy of your only daughter!"

    else:
        pass

    scene black with Dissolve(2)
    stop music fadeout 1.0
    $ renpy.pause(0.8)
    "You and Luna follow Cassandra into the woods surrounding Haven, only five minutes later you arrive."
    play music forest_1 fadein 1.0
    #stop music fadeout 1.0
    scene ch7sc08_069 with Dissolve(2)
    $ renpy.pause(0.8)
    lu "Woah! This place is neat! Did you set all this up?"
    cas "I did, I anticipated we would need an area to practice magic at some point."
    cas "So I’ve spent a bit of time gathering some basic supplies I thought would be useful to us out here."
    scene ch7sc08_070 with dissolve
    mc "This is honestly pretty cool, Cassandra."
    mc "So, what’s the plan for today?"
    cas "I’m thinking we’ll start with one of the fundamentals that novices at the guild learn."
    cas "Magic duels!"
    scene ch7sc08_071 with dissolve
    lu "C’mon slowpoke! I’m eager to beat you in our first magic duel! *Giggling*"
    cas "Go on, take your spot on the stool opposite Luna and I’ll explain the rules."
    scene ch7sc08_072 with dissolve
    lu "Can we begin? I can’t wait to show him his first magic duel!"
    cas "Not so fast sweetie… why don’t you explain the rules to [mc] before you begin?"
    scene ch7sc08_073 with dissolve
    lu "*Snickers* …"
    mct "*Chuckles* I know that look… she’s up to some mischief over there…"
    scene ch7sc08_074 with dissolve
    mc "What are you up to? It’s not going to work…"
    lu "Who me? Oh don’t you worry about little ol’ me! *Giggles*"
    scene ch7sc08_075 with dissolve
    lu "*Whispers* {size=-10}{b}Ashi… ven… itu…{/b}{/size}"
    lu "So! Rule number one… always try to anticipate your opponent’s next move."
    scene ch7sc08_076 with dissolve
    lu "Rule number two… you’ve got to keep a close eye on your opponent."
    lu "Your eyes should be glued to their body… watching for the slightest movement…"
    scene ch7sc08_077 with dissolve
    mc "Keeping my eyes on my opponent today isn’t an issue…"
    lu "*Snickers* …"
    scene ch7sc08_076 with dissolve
    lu "I had a feeling you wouldn’t mind that rule…"
    scene ch7sc08_077 with dissolve
    mc "What’s rule number three?"
    scene ch7sc08_076 with dissolve
    lu "Rule number three is…"
    lu "Forget the previous rules and knock your opponent off!"
    scene ch7sc08_078 with dissolve
    with vpunch
    mc "Arhh! Luna!"
    lu "Gotchu! *Snickers*"
    scene ch7sc08_079 with dissolve
    cas "Luna! Apologize right now young lady!"
    lu "But moooom!"
    cas "Don’t Mom me!"
    cas "This is [mc]'s first lesson and you’re using a sneak attack like that?"
    scene ch7sc08_080 with dissolve
    mc "*Chuckles* It’s alright Cassandra, I knew she was up to something…"
    mc "In fact… I’m glad she chose this approach, even if she’s just messing around."
    mc "Attempting to get the upperhand on your opponent early on in a battle is often a good strategy."
    scene ch7sc08_072 with dissolve
    cas "Very well… since nobody was hurt… we’ll let this slide."
    cas "As I’m sure you just gathered, in a magic duel, the goal is to knock your opponent off balance."
    cas "In your case, knock each other off your stool… last one standing is the winner."
    mc "Yeah, I thought as much… okay, let’s do this."
    cas "On my count… 3…2…1…"
    scene ch7sc08_081 with dissolve
    with vpunch
    cas "Begin!"
    lu "Incinerum!"
    scene ch7sc08_082 with dissolve
    with vpunch
    lu "{b}*Squeals* AiiyhH! [mc]!{/b}"
    mct "*Chuckles* Got her."
    scene ch7sc08_083 with dissolve
    with vpunch
    lu "Owh! M-Mooom! Tell him not to dodge my fireballs!"
    cas "*Snickers* You deserved that one honey… after your previous sneak-attack I won’t play favorites."
    cas "Now get back up and try again."

    if luna_relationship == True:
        scene ch7sc08_084 with dissolve
        lu "Easy for you to say… you’re not the one who’ll have a bruised butt…"
        scene ch7sc08_085 with dissolve
        with vpunch
        "Immediately upon hearing she might’ve gotten hurt, you rush to her side."
        mc "Hey… you okay?"
        lu "[mc]...?"
        "Luna looks up to you in awe, clearly surprised and pleased you came to her aid."
        lu "I-I’m fine… thank you though… for checking on me."
        scene ch7sc08_086 with dissolve
        mc "*Chuckles* What are boyfriends for?"
        lu "They’re for… kissing their girlfriends! *Giggles*"
        lu "But with my mom right over there… I’ll settle for your help getting back up."
        mc "*Chuckles* Very well, let’s do another round, cutie."


    else:
        pass

    scene ch7sc08_072 with dissolve
    lu "Mom, can we go all out now? Pleeeeaaase?"
    cas "I don’t know honey… someone could get hurt."
    scene ch7sc08_080 with dissolve
    mc "Don’t worry Cassandra, as you know, I can heal us if anything goes wrong."
    scene ch7sc08_079 with dissolve
    cas "*Sighs* Alright then… fine… go all out if you so desire."
    scene ch7sc08_072 with dissolve
    lu "Yay! Thank you mom!"
    lu "We won’t attack with lethal force obviously, but I really want to knock him on his butt!"
    mct "Hmm, how do I want to approach this next round?"

    ###Skill choice###
    menu:
        "{color=#df0dff}Wisdom{/color}":
            cas "On my count… 3…2…1…"
            scene ch7sc08_087 with dissolve
            with vpunch
            cas "Begin!"
            lu "Incerium-conflux!"
            $ wisdom += 1
            mct "That fireball is larger than the previous one, and it has too much energy to be dodged, I’ll have to block it."
            scene ch7sc08_088 with dissolve
            with vpunch
            mct "Made it just in time… damn, I can feel the heat through the wall…"
            scene ch7sc08_089 with dissolve
            lu "*Quietly* {size=-10}{b}Arcanium, salvo-arcanis!{/b}{/size}"
            scene ch7sc08_088 with dissolve
            with vpunch
            lu "Salvo-arcanium!"
            scene ch7sc08_090 with dissolve
            with vpunch
            mct "Fuck! She swapped to an arcane-style barrage in the midst of casting fireballs? She’s good!"
            with vpunch
            scene ch7sc08_091 with dissolve
            with vpunch
            mct "Dammit! She broke through my earth-barrier!?"
            scene ch7sc08_092 with dissolve
            mct "With the speed of her arcane barrage, I’ll only get one chance to counter-attack."
            mct "I have to ensure she is knocked off."
            scene ch7sc08_093 with dissolve
            mct "Here we go! Onyx get ready, we won’t be able to dodge her attack!"
            scene ch7sc08_094 with dissolve
            with vpunch
            "Luna’s missiles quickly re-targets your footing as they get closer, but Onyx manages to grab hold of you."
            ox "Master! Knock her off!"
            mc "On it!"
            scene ch7sc08_095 with dissolve
            lu "You’re going down! Onyx won’t be able to hold you up after my next barrage!"
            scene ch7sc08_096 with dissolve
            with vpunch
            lu "{b}*Squeals* Aiiyhh!!{/b}"
            "Completely trusting Onyx to keep you in place, you push your windburst forward, striking Luna with precision."
            ox "Hah! Nicely done, master!"
            scene ch7sc08_097 with dissolve
            lu "{size=+10}{b}*Screams* Aiiyh-aahh!{/b}{/size}"
            scene ch7sc08_098 with dissolve
            with vpunch
            mc "Don’t worry I got you!"
            scene ch7sc08_099 with dissolve
            lu "*Gasps* [mc]... you saved me?"
            cas "Looks like we’ve got a winner."
            lu "Y-Yeah… I admit defeat."
            "You managed to outsmart Luna with your spellcasting, your {b}{color=#df0dff}Wisdom{/color}{/b} has increased by {size=+3}{b}{color=#2bff8b}1{/color}{/b}{/size}."


        "{color=#ff8400}Strength{/color}":
            scene ch7sc08_093 with dissolve
            with vpunch
            mc "Let’s see if she can handle a full-force frontal!"
            "Luna seems to have the same idea as you as she sends forth a full barrage of arcane missiles."
            mc "Fuck! They’re going to reach me before my wind connects, I need more force!"
            scene ch7sc08_100 with dissolve
            with vpunch
            $ strength += 1
            mc "She won’t be able to withstand this!"
            scene ch7sc08_101 with dissolve
            with vpunch
            lu "{b}*Squeals* AiiyhH! [mc]!{/b} I’m going to fall!"
            scene ch7sc08_097 with dissolve
            lu "{b}*Screams* Aiiyh-aahh!{/b}"
            scene ch7sc08_098 with dissolve
            with vpunch
            mc "Don’t worry I got you!"
            scene ch7sc08_099 with dissolve
            lu "*Gasps* [mc]... you saved me?"
            cas "Looks like we’ve got a winner."
            lu "Y-Yeah… I admit defeat."
            "You managed to force Luna off her balance, your {b}{color=#ff8400}Strength{/color}{/b} has increased by {size=+3}{b}{color=#2bff8b}1{/color}{/b}{/size}."


        "{color=#745099}Stealth{/color}":
            scene ch7sc08_073 with dissolve
            mct "I’ll go with a stealthy approach, she won’t realize what happened until she’s on the ground."
            mc "Well, little witch? Aren’t you going to knock me on my ass?"
            scene ch7sc08_076 with dissolve
            lu "You want to give me the benefit of attacking first? Alrighty then!"
            lu "Just remember you asked for it when you’re on your butt!"
            scene ch7sc08_102 with dissolve
            with vpunch
            lu "Hnnyaah! Incinerum!"
            lu "You might want to dodge!"
            scene ch7sc08_103 with dissolve
            mct "Just like I practiced with Rin… wait for the very last moment…"
            with vpunch
            mct "Now!"
            scene ch7sc08_104 with dissolve
            with vpunch
            lu "Huh!? Where did he go!?"
            scene ch7sc08_105 with dissolve
            with vpunch
            lu "{b}*Squeals* Aiiiyh-aiiyhH! [mc]!!{/b}"
            mc "Do you surrender? You’re at my mercy!"
            with vpunch
            lu "*Giggling uncontrollably* Hahah! N-No! S-Stooppp! Hahahah! Tickling isn’t fair!! Mooooom!"
            cas "Sorry sweetie… I think he’s got you… *Snickers*"
            $ stealth += 1
            mc "Hear that? That’s the sound of my victory."
            lu "Hahaha! Okay! Okaaaay! You win! No-No more! Hahaha!"
            "You won the duel by getting Luna off the stool, your {b}{color=#745099}Stealth{/color}{/b} has increased by {size=+3}{b}{color=#2bff8b}1{/color}{/b}{/size}."

    scene ch7sc08_106 with dissolve
    cas "Alright you two… I think that’s enough dueling for today."
    cas "Why don’t you join me over here for our next exercise?"
    scene ch7sc08_107 with dissolve
    lu "What are we doing? Shooting bottles?"
    cas "That’s exactly what we’re doing, it’s a good exercise to practice precision."
    cas "Let’s finish setting up the bottles. Make sure to alternate between glass and clay."
    cas "[mc], if you could bring over the bottles, we’ll place them, then the two of you can begin."
    scene ch7sc08_108 with dissolve
    cas "I like seeing you like this…"
    lu "Hmm? Like what?"
    cas "Happy."
    lu "I have a lot of reasons to be happy as of late…"
    scene ch7sc08_109 with dissolve
    cas "Do you love him?"
    lu "Moooom!"
    cas "Do you love him sweetie?"

    if luna_relationship == True:
        lu "*Nods* Mhm… I love him."
        cas "It’s an incredible feeling, isn’t it? Falling in love for the first time."
        scene ch7sc08_110 with dissolve
        lu "It really is… I can’t put my finger on it, I just want to be with him all the time…"
        lu "He makes me happy… playful… curious…"
        cas "I’m glad sweetie, as your mother, seeing you become a young woman fills me with joy."
        cas "And having someone like [mc] in your life will only help you grow."

    else:
        lu "Mom! We’re just friends!"
        cas "I know sweetie… doesn’t mean you can’t love him as a friend."
        scene ch7sc08_110 with dissolve
        lu "I guess I do? I trust him more than anyone…"
        cas "I’m glad sweetie, having someone like that in your life will only help you grow."

    scene ch7sc08_111 with dissolve
    lu "I’d like that… to keep growing with [mc]."
    lu "I feel like we can learn a lot from each other."
    cas "I believe you can, and will."
    lut "Mother hasn't been in love since father left... I wonder if she misses it?"
    cas "Now I think that’s enough targets, let’s begin."
    scene black with Dissolve(2)
    stop music fadeout 1.0
    $ renpy.pause(0.8)
    play music relax_2 fadein 1.0
    #stop music fadeout 1.0
    scene ch7sc08_112 with Dissolve(2)
    $ renpy.pause(0.8)
    cas "Alright you two, the stage has been set, we’ll have a good old fashioned shoot-off."
    lu "*Snickers* [mc] knows I’m great at these!"
    mc "Yeah… I do remember our last shoot-off at the guild."
    scene ch7sc08_113 with dissolve
    lu "It was a lot of fun!"
    lu "I wouldn’t mind another shoot-off like that with you…"

    if luna_relationship == True:
        lu "Especially given how it ended… *Snickers*"
        mc "It’s imprinted vividly into my mind… mmh."


    else:
        pass

    scene ch7sc08_114 with dissolve
    cas "Let’s have [mc] begin, I’d like to see him in action."
    lu "Sure! I like the advantage of going second."
    cas "Great, let’s give [mc] some space. Please take a few steps back as well [mc], we don’t want this to be too easy."
    scene ch7sc08_115 with dissolve
    mc "Here should be good?"
    cas "Yes, sweetie, that’s a perfect distance, your goal is to knock down the clay bottles without hitting the glass ones."
    scene ch7sc08_116 with dissolve
    cas "Seeing your duel with Luna… I look forward to seeing how precise you can be."
    cas "Spellcasting isn’t always about potency or brute force, but also about finesse."
    scene ch7sc08_117 with dissolve
    mct "Okay… precision… finesse… let’s see."
    mct "I’ll go with wind… my earth-affinity isn’t remotely close enough to being this precise."
    scene ch7sc08_118 with dissolve
    mct "Just a small gust…"
    mct "The trick is not to knock over the glass bottles."
    scene ch7sc08_119 with dissolve
    with vpunch
    mct "Dammit! I hit two glass bottles!"
    scene ch7sc08_120 with dissolve
    lu "*Clapping* Brilliant! Well done!"
    lu "Looks like I’ll win this easily! I know exactly what I want for my prize!"
    scene ch7sc08_121 with dissolve
    cas "Shush young lady!"
    cas "As I recall it took you about a full year before you managed to avoid hitting the glass bottles?"
    lu "Moooom! Don’t throw me under the wagon in front of [mc]!"
    cas "That’s what you get for teasing him!"
    scene ch7sc08_122 with dissolve
    cas "Don’t mind her… as I stated, it took her almost a year of constant practice to get this precise."
    cas "Would you like me to guide you sweetie?"

    ####Choice####
    menu:
        "Sure, I’d like that. ({color=#ff8cdd}Romance{/color})":
            mc "I’d be a fool to decline the help of an experienced sorceress such as you, Cassandra."
            cas "*Giggling* Very well, prepare yourself as before, and I’ll stand with you."
            scene ch7sc08_117 with dissolve
            mc "Like this?"
            scene ch7sc08_123 with dissolve
            cas "Yes sweetie, this will do nicely, I quite like your stance."
            "You feel the soft warmth of Cassandra’s shapely breast brushing against your arm as she gently caresses you."
            cas "Last time you used a gust of wind, you had the right idea but we need to achieve better control of the impact."
            scene ch7sc08_124 with dissolve
            cas "Here… allow me to feel your arm honey."
            cas "Hmmm… yes… there it is… the potent magic I’ve grown so fond of…"
            scene ch7sc08_125 with dissolve
            lu "Mom! Are you going to teach him or grope him!?"
            lu "I don’t remember you ever teaching any students like this at the guild!"
            scene ch7sc08_124 with dissolve
            cas "Honey be quiet and wait your turn, teaching [mc] is both important and… an intimate process."
            cas "Besides… I’m not the guildmaster any longer, which means [mc] isn’t my student."
            cas "Okay, you’re ready… let your magic flow freely and let my touch and voice guide you."
            scene ch7sc08_126 with dissolve
            cas "Oh my… I feel you sweetie… mmh… do you feel me?"
            mc "I do… mmh, your touch is quite delicate."
            cas "Push your wind through your arm and forward to your index finger, just like last time."
            scene ch7sc08_127 with dissolve
            cas "Wonderful! You’re truly a man to behold… mmh…"
            cas "That’s it… feel me… push it through your hand and concentrate it at your finger."
            scene ch7sc08_128 with dissolve
            cas "Perfect honey! Now keep it steady."
            cas "You’re unique as a demi-god, you don’t need to use incantations or spells, you can just ‘feel’ and shape your magic."
            cas "Last time you used a small gust of wind, but it has too wide of an area of effect on impact."
            cas "This time, I want you to think about using the wind as a nimble projectile… feel it, shape it…"
            cas "You’re ready… I believe in you, you can do this… go on."
            scene ch7sc08_129 with dissolve
            with vpunch
            cas "Perfect sweetie! Oh you’re just wonderful! I knew you could do it!"
            $ cas_path = True
            mc "*Chuckles* All thanks to your guidance… you’re a great teacher."
            scene ch7sc08_130 with dissolve
            "You feel Cassandra wrap herself around you in excitement, completely forgetting that Luna is watching."
            cas "I knew you had it in you! But just one attempt to get it right? You’re truly incredible!"
            mc "Mmmh... you smell good."
            cas "*Soft giggle* Do I? I like that you noticed-"
            scene ch7sc08_125 with dissolve
            lu "Mother!"

            if luna_relationship == True:
                lu "That’s enough!"
                with vpunch
                lu "Your smothering {b}MY{/b} boyfriend with your breasts!"
                scene ch7sc08_125a with dissolve
                lut "She looks so... happy."
                lut "I can't remember the last time I've seen her this carefree and playful..."
                lut "But I can't let her have all the fun! He's mine!"
                scene ch7sc08_131 with dissolve
                lu "Hmph! Arcani, Levitum!"
                scene ch7sc08_130 with dissolve
                cas "Just a little longer sweetie! Didn’t you see how well he did?"
                scene ch7sc08_132 with dissolve
                with vpunch
                cas "*Gasps* L-Luna! Put me down!"
                lu "Sorry mom, but you did this to yourself! You’re in timeout."
                cas "Sweetie! This is not fair! I don't have my magic!"
                scene ch7sc08_131 with dissolve
                lu "Yeah? I wasn't aware! *Snickers*"
                lu "Now, it’s my turn."
                lu "I have a prize to win!"
                scene ch7sc08_133 with dissolve
                lu "You just sit over there and watch me beat [mc]!"
                "As Luna reaches you, she gently takes your hand. while covering the view so her mom can’t see."
                mct "*Chuckles* What is she up to?"
                mc "*Whispers* {size=-10}{b}What are you-{/b}{/size}"
                scene ch7sc08_134 with dissolve
                "Before you finish your sentence, Luna has already guided your hand to her breast, keeping it in place as you grope her."
                lu "Who has your favorite breasts? Me or my mom?"
                scene ch7sc08_135 with dissolve
                mc "Fuck… you naughty little witch… I won’t lie… your mom has amazing breasts."
                mc "A gene she has definitely passed on to you… you’ve even got her beat… I prefer yours."
                scene ch7sc08_134 with dissolve
                lu "Mmh… with the way you're touching me… I believe you’re telling the truth… you definitely prefer mine."
                lu "Remember that the next time my mom tries to smother you with her breasts! *Snickers*"
                scene ch7sc08_135 with dissolve
                mc "*Chuckles* Is my little witch jealous?"
                "You feel Luna hold her hand firmly pressed into her breast."
                scene ch7sc08_134 with dissolve
                lu "She might be… now, watch me beat you in bottle shooting!"
                lu "I haven’t decided on what I want as my prize… but I’m sure I’ll think of something…"

            else:
                scene ch7sc08_125 with dissolve
                lu "O-Okay that’s enough! It’s my turn now!"


        "I’m good, thanks though. ({color=#2bff8b}Friendship{/color})":
            mc "I appreciate the offer, but I’d like to be able to do this on my own."
            scene ch7sc08_117 with dissolve
            cas "Of course sweetie, I believe you can do it, just keep focusing on not applying too much force."
            scene ch7sc08_118 with dissolve
            mct "Okay… not too much force… easier said than done."
            scene ch7sc08_119 with dissolve
            with vpunch
            mct "Dammit!"
            scene ch7sc08_120 with dissolve
            lu "*Snickers* Looks like we’ll be here a while!"
            lu "I don’t remember you missing this terribly when we were shooting bottles at the guild?"
            scene ch7sc08_121 with dissolve
            cas "Keep talking smack young lady…"
            cas "I have plenty of stories to share with him about your early days starting out too!"
            cas "Little Miss Singed-Eyebrows."
            scene ch7sc08_125 with dissolve
            $ cas_path = False
            with vpunch
            lu "Y-You wouldn’t!"
            lu "T-That was a one time thing!"
            lu "A-Anyway! I think it’s my turn now! Maybe it’ll help when he sees me in action."


    scene ch7sc08_136 with Dissolve(2)
    $ renpy.pause(0.8)
    lu "I have no intention of losing this shoot-off."
    mc "Oh? You’re going with arcane this time? Last time you used fire as I recall?"
    lu "I’ve been practicing… fire is far too volatile for precision tasks like this."
    scene ch7sc08_137 with dissolve
    lu "Arcani, rih, levitum!"
    scene ch7sc08_138 with dissolve
    mc "Impressive, certainly more accurate than your fireballs last time."
    lu "You think this is impressive? Watch this then… Arcani, duh, levi-tum!"
    scene ch7sc08_139 with dissolve
    $ renpy.pause()
    scene ch7sc08_140 with dissolve
    $ renpy.pause()
    "Luna makes quick work of the task, without even so much as wobbling the glass bottles."
    mc "Okay… that’s… honestly impressive."
    lu "You think so?"
    mc "Yeah, you’ve really improved."
    scene ch7sc08_141 with dissolve
    lu "[mc]... thank you for saying that…"
    lu "You’ll surpass my precision swiftly, want to do another round?"
    scene ch7sc08_140 with dissolve
    mc "Sure thing, first you’ll have to put the bottles back down though."
    lu "*Snickers* Right! One moment… Arcani, roh, doh, levitum!"
    scene ch7sc08_139 with dissolve
    $ renpy.pause()
    scene ch7sc08_137 with dissolve
    $ renpy.pause()
    scene ch7sc08_136 with dissolve
    $ renpy.pause()
    scene ch7sc08_133 with dissolve
    lu "There we go! Now it’s your turn!"
    lu "I want to see if you learned anything from watching me!"
    scene black with Dissolve(2)
    $ renpy.pause(0.8)
    "You spend the rest of the afternoon practicing magic with Luna and Cassandra before the three of you head back to Haven."
    stop music fadeout 1.0
    scene ss29 with Dissolve(2)
    $ renpy.pause()
    scene ss12 with Dissolve(2)
    $ renpy.pause()
    scene black with Dissolve(2)
    $ renpy.pause(0.8)
    play music explore_1 fadein 1.0
    scene ch7sc08_142 with Dissolve(2)
    $ renpy.pause(0.8)
    ec "Sister, did Ria and Alyze bring back any news from their trip to Arugoh?"
    riv "They reported that there hadn’t been any signs of activity at the campsite of our expedition group at Arugoh."
    riv "It only looks like their camp had been set up, but not much else."
    ec "That means…"
    scene ch7sc08_143 with dissolve
    riv "We know not what it means… they have Kisha with them."
    riv "She alone is more than enough to handle anything the jungle throws at them."
    scene ch7sc08_144 with dissolve
    ec "Then why haven’t they been active at their campsite?"
    ec "Kisha of all people knows the importance of having that campsite to operate from."
    ec "No… something has happened to them."
    scene ch7sc08_143 with dissolve
    riv "Sister… let us not jump to conclusions, everyone partaking in this expedition are solid huntresses."
    riv "Believe in them, they need that."
    scene ch7sc08_145 with dissolve
    ec "*Sighs* You’re right… at the moment, believing in them is all we can do."
    riv "Hey… it’s okay, they’ll be alright."
    ec "I… I wish he was here."
    riv "You miss him dearly, don’t you?"
    ec "*Exhales deeply* Mhm… I feel empty without his presence."
    scene ch7sc08_146 with dissolve
    riv "He will return to us… I know it."
    riv "I… feel it."
    ec "You miss him too… I know you do, yet… you remain so strong in his absence?"
    riv "I channel my feelings into my sparring, I have since I left A’nai all those years ago…"
    scene ch7sc08_147 with dissolve
    riv "Come."
    riv "Join me outside at the arena."
    ec "At the arena? What are you-"
    riv "We’re going to spar, for as long as it takes until your resolve returns."
    scene black with Dissolve(2)
    $ renpy.pause(0.8)
    stop music fadeout 1.0
    scene ss98 with Dissolve(2)
    $ renpy.pause()
    scene black with Dissolve(2)
    play music relax_2 fadein 1.0
    $ renpy.pause(0.8)
    scene ch7sc08_148 with Dissolve(2)
    $ renpy.pause(0.8)
    cas "Home, sweet home."
    lu "Mom! I can’t believe you’ve fully furnished it already?"
    lu "This is incredible! Kitchen, dining area, seating area, and a bedroom to boot!?"
    scene ch7sc08_149 with dissolve
    cas "After months in Taron’s cells and then several weeks in hideouts, this home has certainly been a blessing."
    cas "I can’t take all the credit though… I had the help of a lovely young man."
    scene ch7sc08_150 with dissolve
    lu "So I’ve been told!"

    if luna_relationship == True:
        lu "You’re lucky your daughter has such a wonderful boyfriend! *Giggling*"
        lu "Speaking of my amazing and handsome boyfriend, you better put those away!"
        cas "*Snickers* Mh-hm…"
        lu "D-Don’t snicker! Go put on something… I’ll prep dinner with [mc] in the meanwhile."
        scene ch7sc08_151 with dissolve
        cas "Very well, I look forward to having my beautiful and totally not jealous daughter and her handsome boyfriend cook dinner."
        lu "I’m not jealous! And we’re going to make the best dinner, period!"


    else:
        lu "What’s for dinner? All this magic practice has left me starving."
        scene ch7sc08_151 with dissolve
        cas "That’s up to you and [mc], I’ll go change out of this outfit, it’s a little sweaty, you guys are in charge of dinner."
        lu "Okay, brace yourself for an amazing meal!"

    scene ch7sc08_152 with dissolve
    mc "So, what should we make?"
    lu "Uhhmmm! This being my first time in here, I don’t really know what she has available."
    mc "Alright, let’s just see what we can find, it doesn’t need to be anything fancy."
    scene ch7sc08_153 with dissolve
    lu "{size=+10}{b}*Excitedly* Cute!{/b}{/size}"
    mc "Hmm?"
    lu "This is kinda cute, don’t you think?"
    scene ch7sc08_154 with dissolve
    mc "What is?"
    lu "You know, us? Cooking together?"
    scene ch7sc08_153 with dissolve
    mc "*Chuckles* I suppose? I guess it’s our first time cooking a meal together."
    lu "Exactly! As I said… cute!"
    mc "…"
    scene ch7sc08_154 with dissolve
    lu "Need help with those potatoes?"
    scene ch7sc08_153 with dissolve
    mc "*Chuckles* I think I can handle a few potatoes."
    scene ch7sc08_154 with dissolve
    lu "Are you sure?"
    lu "After seeing your precision during training today… we might end up with mashed potatoes!"
    mc "*Chuckles* Mind your carrots… or I’ll mash you."
    scene ch7sc08_153 with dissolve
    lu "Oooooh! Promise!?"
    mc "Yeah I had a feeling that wouldn’t work…"
    scene black with Dissolve(2)
    stop music fadeout 1.0
    $ renpy.pause(0.8)
    play music mmm_elven_forest fadein 1.0
    "You and Luna finish preparing dinner and Cassandra joins the two of you after having changed."
    scene ch7sc08_155 with Dissolve(2)
    $ renpy.pause(0.8)
    lu "*Giggling* I can’t believe we managed all this!?"
    lu "We didn’t even use magic!"
    scene ch7sc08_156 with dissolve
    mc "*Chuckles* I’m still convinced you did something arcane-ish when you almost burnt the sausages."
    lu "*Snickers* I considered it! But I swear I didn’t! I wanted this to… just be done by us."
    scene ch7sc08_157 with dissolve
    mc "I look forward to getting a taste…"
    cas "*Giggling* As do I."
    cas "It smells absolutely heavenly in here."
    scene ch7sc08_158 with dissolve
    lu "Come, come! Sit with us! Dinner is ready!"
    scene ch7sc08_159 with dissolve
    cas "Mmh… you two really made all this? Color me impressed."

    if charisma >= 20:
        scene ch7sc08_158 with dissolve
        mc "You look great, Cassandra."
        mc "That robe really suits you."
        scene ch7sc08_159 with dissolve
        cas "This little thing? Oh it’s nothing… just a nightrobe I’ve had laying about."
        cas "But I appreciate the compliment all the same."
        scene ch7sc08_160 with dissolve
        cas "It’s nice to be noticed once in a while…"
        mc "Trust me… you’re definitely being noticed."
        cas "I can’t tell if you’re hungry for the food or… something else? *Giggles*"

        if luna_relationship == True:
            scene ch7sc08_158 with dissolve
            lu "H-Hey! That’s enough! He’s hungry for food!"
            lu "Now sit down! Stop enticing him with your perfect breasts!"
            mc "*Chuckles* Let’s eat."
            scene ch7sc08_159 with dissolve
            cas "Hmm… should I sit by [mc], my handsome landlord? Or by my beautiful daughter?"
            lu "You’re sitting with me, and that’s final! Hmpfh!"
            scene ch7sc08_158 with dissolve
            lut "Hmpfh! I told her to put her breasts away not wear something even more seductive!"
            lut "Oh it's on mother... two can play this game..."
            lut "And I will win every time... he's my boyfriend not yours!"


        else:
            scene ch7sc08_160 with dissolve
            lu "Okay that’s gross! Now sit down and let’s eat!"

    elif luna_relationship == True:
        scene ch7sc08_158 with dissolve
        mc "You look great, Cassandra."
        lut "Hmpfh! I told her to put her breasts away not wear something even more seductive!"
        lut "Oh it's on mother! Two can play this game..."


    else:
        pass

    scene ch7sc08_159 with dissolve
    cas "I can’t wait to taste what you two have come up with, the entire house is filled with the aroma."
    scene ch7sc08_161 with dissolve
    cas "Mmh… it’s been a while since I’ve had a cold ale, this really hits the spot."
    lu "Cold ales are the best! I’m not really into wines… they’re either too sweet or too sour."
    scene ch7sc08_162 with dissolve
    lu "And ales have foam! *Snickers*"
    cas "I think you’ve got that trait from me honey… I do love the foam from ales."
    mc "*Chuckles* The witches of Haven enjoy foam, I’ll take note."
    scene ch7sc08_163 with dissolve
    cas "How did your first class at the guild go?"
    cas "Did you manage to attend any of the classes Rose has been teaching?"
    lu "*Crunches carrot* Mmh."
    scene ch7sc08_164 with dissolve
    mc "Yeah, I believe it was a class for advanced object manipulation?"
    mc "Rose was the one teaching it, and I attended alongside a couple of other students."
    lu "*Crunches carrot* Mmh."
    scene ch7sc08_163 with dissolve
    cas "Oh I see, I believe Celine and Lina are in that class?"
    scene ch7sc08_164 with dissolve
    mc "Yeah, and a guy called Wiz, but he failed the task, it sounded like Rose sent him back to a beginner class."
    cas "*Snickers* …"
    scene ch7sc08_163 with dissolve
    cas "That sounds like something she would do."
    cas "Since your goal is to get closer to Rose and impress her, I suggest you keep taking her classes."
    scene ch7sc08_165 with dissolve
    lu "Does he really have to attend her classes?"
    lu "That big-titted cow can be impressed by him from word of mouth by the other teachers!"
    scene ch7sc08_166 with dissolve
    cas "Luna! That’s enough."
    cas "Don’t use language like that, you’re a grown woman."
    cas "And need I remind you that Rose is your godmother?"
    scene ch7sc08_165 with dissolve
    lu "Ugh! Don’t remind me! After what she’s doing she’s nothin-"
    scene ch7sc08_166 with dissolve
    cas "I said that’s enough!"
    cas "Rose has not done this out of malicious intent, I am certain of it."
    cas "There's a reason I spent the majority of my life with her and trusted her enough to name her your godmother."
    cas "Taron is using her, he has something on her… we just need proof and make her realise she’s on the wrong side."
    scene ch7sc08_165 with dissolve
    lu "Fine, fine! But I still don’t like her as of right now!"
    lu "Can I have another carrot, please."
    scene ch7sc08_164 with dissolve
    mc "I can definitely see both sides."
    mc "Luna is furious that someone close to the two of you used that trust to betray and harm her mom."
    mc "And Cassandra, you’re quick to forgive as you believe her actions aren’t of her own accord."
    scene ch7sc08_163 with dissolve
    cas "He’s right honey… we should try to be a little more understanding of each other’s view of the situation."
    lu "*Crunches carrot* Mhm-hm! Ih… ahgree."
    cas "It’s a rare thing…"
    cas "A man being this young and yet, carries extensive wisdom, certainly that beyond a twenty year old."
    scene ch7sc08_164 with dissolve
    mc "I tend to chalk it up to having traveled far and wide, which has pushed me to meet a large variety of people."
    scene ch7sc08_167 with dissolve
    mc "But I’m not always this wise, when it comes to my own personal decisions…"
    mc "I often let my emotions cloud my judgement when it comes to personal matters."
    scene ch7sc08_168 with dissolve
    cas "That happens to all of us, the older you get and the more life experience you accumulate…"
    cas "The less you will be driven impulsively by your emotions."
    cas "But it never truly goes away. Even at my old age, I am not safe from emotion-based decisions."
    scene ch7sc08_167 with dissolve
    mc "You know better than to bring up your age in front of me… you’re only 35."
    mc "That means you’re about in the middle of your prime."
    scene ch7sc08_168 with dissolve
    cas "*Giggles softly* That’s sweet of you to say, honey."
    cas "I guess I don’t have it as bad as most women, at least my aging is slowed down considerably thanks to being a mage."
    scene ch7sc08_162 with dissolve
    lu "Let’s cheer to aging slowly!"
    cas "I’ll certainly drink to that! *Snickers*"
    mc "And I’ll be happy to drink to the thought of having you two around for well over a century."
    scene ch7sc08_169 with dissolve
    cas "So, [mc], now that you’ve had a class with Lina and Celine… what’s your impression of them?"
    lu "*Slurps* Mmmmhhh…"
    scene ch7sc08_170 with dissolve
    mc "Well, I didn’t get much of a chance to talk with them, but I did get to watch them in action."
    mc "They both managed to complete the task, in their own impressive ways."
    scene ch7sc08_169 with dissolve
    cas "I imagine it was rather easy for Celine?"
    scene ch7sc08_170 with dissolve
    mc "You’d be correct, Celine’s magic was flawless, while Lina struggled, but she managed to overcome her disadvantage."
    mc "Which was also an impressive feat if you ask me."
    scene ch7sc08_169 with dissolve
    cas "It certainly is, in the world of spellcasting each element has its advantages and disadvantages."
    cas "For example, in a match between an equally matched water vs fire mage, the water mage wins due to elemental advantage."
    cas "However, if the firemage is more powerful, they can overcome their inherent disadvantage and win."
    scene ch7sc08_170 with dissolve
    mc "Yeah… I was taught this at an early age, from my friend, Rin."
    mc "She’s the one who’s taught me most of what I know about magic."
    scene ch7sc08_163 with dissolve
    cas "She’s the one from the Sen’ju region? Nakajima I believe?"
    cas "If so, I’d love to meet her some time. Luna and I quite like the Sen’ju region."
    scene ch7sc08_164 with dissolve
    mc "I know she’s around these parts but I haven’t encountered her yet…"
    mc "I haven't attempted to seek her out, she will come to me when she is ready."
    mc "And when she does, I hope I can convince her to join us here at Haven, I’d love to have her back in my life."
    scene ch7sc08_163 with dissolve
    cas "She was the first woman you ever loved… wasn’t she?"
    scene ch7sc08_164 with dissolve
    mc "Yeah… she was."
    mc "How did you-"
    scene ch7sc08_169 with dissolve
    cas "A woman’s intuition is a powerful entity."
    cas "The way your eyes light up when you speak of her, she has a special place in your heart."
    scene ch7sc08_170 with dissolve
    mc "Mmh, she does."
    scene ch7sc08_167 with dissolve
    mc "I look forward to being reunited with her."
    mc "It’s been a little over two years since I left Nakajima and Rin..."
    mc "I’m curious as to what she’s been up to."
    scene ch7sc08_168 with dissolve
    cas "I have a feeling she’s just as excited and curious to reunite with you."
    scene ch7sc08_170 with dissolve
    mc "What makes you say that?"
    scene ch7sc08_169 with dissolve
    cas "[mc], as a woman who’s had the pleasure of having you in her life, I can confidently say…"
    cas "This Rin… she longs to be back in your life, trust me."
    scene ch7sc08_170 with dissolve
    mc "*Chuckles* Thank you, you have a way of making me believe anything you say."
    cas "*Giggling* Mhmh…"

    if luna_relationship == True:
        lut "I love how well mother gets along with [mc]... she's so relaxed when he's here."
        lut "But I can't let her steal my thunder! Nuh-uh!"
        lut "*Slurphs ale* I have an idea!"
        scene ch7sc08_170a with dissolve
        lu "Baaaabe! Look at you!"
        mc "Hmm? What is it gorgeous?"
        lu "Goodness you're a mess! You've spilled some sauce on your new elven shirt!"
        scene ch7sc08_170b with dissolve
        lu "It's lucky you have a girlfriend who's so observant!"
        cast "*Giggles softly* Sweet daughter... so obvious."
        cast "I love seeing her fight for his attention, she truly loves him."
        scene ch7sc08_170c with dissolve
        lu "Here babe... allow me."
        lu "I'll get it off your shirt so it doesn't stain."
        scene ch7sc08_170d with dissolve
        mc "*Chuckles* Oh? That's kind of you, even though Nuel mentioned this fabric doesn't-"
        scene ch7sc08_170c with dissolve
        lu "Shush you! Just let your favorite witch take care of you."
        scene ch7sc08_170d with dissolve
        mc "Well thank you then babe... I guess it's better to keep it clean regardless."
        scene ch7sc08_170c with dissolve
        mc "Mmh... you smell good tonight."
        scene ch7sc08_170d with dissolve
        lu "I do, don't I? *Giggles softly*"
        scene ch7sc08_170e with dissolve
        lu "There you go handsome... now you're as good as new!"
        lu "*Whispers* {size=-10}{b}Make sure you stare at my ass while I walk back to my seat... it belongs to you.{/b}{/size}"
        mc "*Whispers* {size=-10}{b}My eyes will be glued to your perky little butt... always.{/b}{/size}"
        scene black with Dissolve(2)


    else:
        pass

    scene ch7sc08_162 with Dissolve(2)
    cas "So, what are your plans for the evening?"
    lu "I’m going to go hangout with Eliza, we’re going to have a little girl’s night while [mc] goes to seduce Rose at her favorite bar."
    mc "*Chuckles* I am?"
    scene ch7sc08_171 with dissolve
    lu "Mhm-hm, I don’t like the idea of sending you into her arms…"
    lu "But we have already planned for this, this will be our best approach."
    lu "Earn her favor during classes, and then establish an emotional connection during social encounters."
    scene ch7sc08_172 with dissolve
    cas "I don’t much like the thought of him having to emotionally connect with her either…"
    cas "But I admit, it does seem like a solid plan."
    cas "Rose has not had a man in just about as long as myself, about two decades…"
    cas "So I know how desperate she must feel, couple that with [mc]’s charm, she’ll be swayed, I’m certain of it."
    scene ch7sc08_171 with dissolve
    lu "Ugh… I hate that I come up with such good plans…"

    if luna_relationship == True:
        lu "I don’t even want to think about my boyfriend having to show affection to that big-titted co-"
        lu "-To… her!"
        lu "I better go see Eliza, she always knows what to say."
        scene ch7sc08_172 with dissolve
        cas "You do that honey, [mc] and I will clean up here before he goes to see Rose."
        scene ch7sc08_173 with dissolve
        lu "Okay, thank you…"
        lu "[mc]... meet me outside?"
        mc "Sure."
        scene black with Dissolve(2)
        stop music fadeout 1.0
        $ renpy.pause(0.8)
        play music intro_1 fadein 1.0
        scene ch7sc08_174 with Dissolve(2)
        $ renpy.pause(0.8)
        lu "…"
        scene ch7sc08_175 with dissolve
        mc "It’s beautiful out here at night, huh?"
        lu "*Nods* Mhm-hm."
        mc "You know you don’t have to worry about me charming Rose… I’m not going to fall in love with her."
        scene ch7sc08_176 with dissolve
        lu "Eeeuuw! *Giggling*"
        lu "I think it’s time you stop talking about Rose… and kiss your girlfriend."
        scene ch7sc08_177 with dissolve
        lu "*Whimpers softly* Aahh… baaaabe… I didn’t tell you to grab my breast! *Giggles*"
        mc "You did… a kiss between girlfriend and boyfriend always includes full-body enjoyment."
        lu "Mmhh… you’re lucky I love it when you touch me…"
        lu "Please kiss me already… I’ve been dying to kiss you all day…"
        scene ch7sc08_178 with dissolve
        lu "*Kisses softly* Mmhm-mffhh… I love you."
        mc "Mmh… I love you too, Luna."
        scene ch7sc08_177 with dissolve
        mc "You’re my little witch, my girl."
        scene ch7sc08_178 with dissolve
        lu "*Mwah* Nnngh! Always will be!"
        lu "You better let go of my breast… I believe you have a big-titted cow to seduce…"
        scene ch7sc08_177 with dissolve
        mc "I wish I didn’t… hers might be bigger… but yours are my favorite."
        lu "Promise?"
        mc "Mmh… I promise."
        lu "Good! Now go, help my mom clean up, I’ll go catch up with Eliza."


    else:
        scene ch7sc08_173 with dissolve
        lu "I’ll tell Eliza you said hi!"
        mc "*Chuckles* You do that, I’ll see you around… little witch."
        lu "Bye-byeee!"

    scene black with Dissolve(2)
    stop music fadeout 1.0
    $ renpy.pause(0.8)
    play music mmm_elven_forest fadein 1.0
    scene ch7sc08_179 with Dissolve(2)
    $ renpy.pause(0.8)
    cas "Darling, can you bring over the last dishes?"
    mc "Dishes coming right up."

    ####Choice#####
    menu:
        "Be playful ({color=#ff8cdd}Romance{/color})":
            scene ch7sc08_180 with dissolve
            cas "*Gasps* [mc]! T-This isn’t doing the dishes! *Giggling* S-Stop it…"
            mc "I’d much rather be doing this… mmh… you smell like a goddess."
            cas "Young man! *Giggling* You’re sniffing me now!? Do I… do I really smell like a goddess?"
            scene ch7sc08_181 with dissolve
            mc "*Inhales* Mmmh… you do, both your scent and the feel of your feminine body is that of a goddess."
            mc "And I would know... having met several goddesses."
            cas "Goodness… your words… your touch… I’ve been longing for this all day… but it’s wrong sweetie…"
            cas "I’m old enough to be your mother…"

            if luna_relationship == True:
                scene ch7sc08_182 with dissolve
                cas "Not to mention I am your girlfriend’s mother."
                cas "This behavior… touching me like this… mmh… it’s highly inappropriate…"
                scene ch7sc08_181 with dissolve
                mc "Is it? To my knowledge, mothers and daughters often share the same man."
                mc "You often see it with women who become widowed, and their daughter finds herself a proper man…"
                scene ch7sc08_182 with dissolve
                mc "The widowed mother will engage in affectionate behavior with her daughter's man, to be claimed by him as well."
                scene ch7sc08_181 with dissolve
                cas "Goodness… your words carry truth, this is common behavior…"
                scene ch7sc08_182 with dissolve
                cas "I wish you weren’t aware… it would make rejecting you so much simpler… mmh…"
                mc "If you agree it’s normal for us to be affectionate with one another… then let me claim you."
                cas "I can’t let you do that… mmh… not yet honey… it’s not the right time tonight."

            else:
                pass

            scene ch7sc08_183 with dissolve
            cas "*Moans* Aahh… oh [mc]... don’t… don’t pull my nipple like that… mmh…"
            mc "*Licks edge of ear* You don’t want me to pull your sensitive nipple? Your moans say otherwise… mmh."
            cas "My damn moans… betraying me in your embrace… mmh…"
            scene ch7sc08_182 with dissolve
            cas "W-Why’d you stop?"
            mc "I just wanted to give your nipple a little taste of what’s to come…"
            cas "Mmh… you definitely succeeded in making them excited…"
            scene ch7sc08_181 with dissolve
            mc "Did I only make your nipples excited? Or is the rest of you just as excited?"
            cas "I think the answer is clear as day… aahh… I can’t wait to become yours… mmh…"
            scene ch7sc08_182 with dissolve
            mc "Soon Cassandra… soon we won’t be able to hold back any longer…"
            cas "With you acting like this… I won’t be able to resist you much longer…"
            scene ch7sc08_181 with dissolve
            cas "The thought of you being my man… of me becoming your woman… it makes me feel things… emotions…"
            cas "Emotions I never thought I’d get to experience."
            scene ch7sc08_180 with dissolve
            mc "You deserve to feel all of it… mmh… but we’ll have to settle for this embrace for tonight."
            mc "It’s time I head out… I have a much less enticing woman to charm tonight."
            cas "I wish it weren’t so… I wish you could stay here… with me… all night… mmh."
            cas "Go sweetie… before I lock the door and take you to bed."
            scene black with Dissolve(2)
            stop music fadeout 1.0
            $ renpy.pause(0.8)

            "You reluctantly release Cassandra and take your leave."
            play music morning_1 fadein 1.0


        "Just get the dishes done ({color=#2bff8b}Friendship{/color})":
            scene black with Dissolve(2)
            stop music fadeout 1.0
            $ renpy.pause(0.8)
            "You bring the dishes to Cassandra and the two of you make short work of them."
            play music morning_1 fadein 1.0

    scene ch7sc08_184 with Dissolve(2)
    $ renpy.pause(0.8)
    cas "Bye-bye honey! Thank you for a lovely dinner!"
    cas "Please be careful tonight! I know you’re good with women but still… Rose can be tricky."
    mc "*Chuckles* She's not the first man-eater I've come across, I'll be fine."
    scene black with Dissolve(2)
    $ renpy.pause(0.8)
    scene ch7sc08_185 with Dissolve(2)
    $ renpy.pause(0.8)
    lut "Their house is so nice! Just like the sen’ju houses I’ve seen depicted in architectural books."
    lut "Eliza mentioned they’ve chosen a bit of Sen’ju themed furniture as well, I can’t wait to see what that’s like."
    scene ch7sc08_186 with dissolve
    lu "*Calls out* Elizaaaa? You home?"
    el "Luna? You bet! Come, come!"
    scene ch7sc08_187 with dissolve
    el "Hey giiirl!"
    lu "*Gasps in awe* Eliza… I can’t believe what you’ve done with the place!"
    scene ch7sc08_188 with dissolve
    el "*Giggling* I’m glad you like it! I know you’re into Sen’ju things, so your approval means we’ve done something right!"
    lu "What’s right is that pajamas on you girl! By the arcane… you look smashing!"
    scene ch7sc08_189 with dissolve
    el "This little thing? *Giggling* I suppose it is cute!"
    lu "Where did you get it? I need one for my pajamas collection!"
    scene ch7sc08_190 with dissolve
    el "I bought it at Fabulous Fabrics, my friend Nuel owns the store, it’s made of elven silk."
    lu "Elven silk… huh… that’s expensive! And incredibly soft!"
    scene ch7sc08_191 with dissolve
    el "It sure is! I can’t go back to regular pajamas after wearing this…"
    lu "I bet! I’m not even wearing it and… I love it!"
    scene ch7sc08_189 with dissolve
    el "*Giggles* If you want, we can go shopping at Nuel’s store some time?"
    lu "R-Really!? I’d like that!"
    scene ch7sc08_192 with dissolve
    lu "I’m so happy! I love shopping! But I haven’t had time with all that's been going on with my mom."
    el "Now that [mc] is on the case, I’m sure we can find time for a little shopping spree. *Giggles*"
    lu "Mhm-hm! Yes please!"
    scene ch7sc08_193 with dissolve
    lu "One of these days, the sooner the better! I neeeeed these pajamas!"
    el "*Snickers* Nuel has a large selection, you’ll see!"
    el "Speaking of seeing… how about I show you the rest of the house?"
    lu "*Squeezes tightly* Yes please!"
    scene black with Dissolve(2)
    stop music fadeout 1.0
    $ renpy.pause(0.8)
    scene ss29 with Dissolve(2)
    $ renpy.pause()
    play music relax_2 fadein 1.0
    scene ch7sc08_194 with Dissolve(2)
    $ renpy.pause(0.8)
    mct "This should be the bar which Rose frequents according to Luna."
    mct "Doesn’t look like Rose is here though, good… if I showed up after her, it could look intentional."
    mct "But being here before her, it only seems like a coincidence."
    scene ch7sc08_195 with dissolve
    mc "Miss, one large ale, please."
    ib "One large ale for the handsome young man coming right up, oh and please call me Bree."
    scene ch7sc08_196 with dissolve
    mc "*Chuckles* Handsome huh? Do you attempt to charm all young men, Bree?"
    ib "I call em as I see em, and with looks like yours, not to mention being well dressed…"
    scene ch7sc08_197 with dissolve
    ib "You’re going to be popular around here."
    ib "Here you are sir, one large ale to wet your hopefully… large appetite."
    scene ch7sc08_198 with dissolve
    mc "I’m known to have an insatiable appetite… for… certain things."
    mc "What makes you think I’ll be popular in your bar?"
    scene ch7sc08_200 with dissolve
    ib "Oh I don’t know… maybe the fact you’re handsome, clearly boasting a well-built physique…"
    scene ch7sc08_199 with dissolve
    ib "You have full, inviting lips… piercing blue eyes, a manly haircut… not to mention…"
    scene ch7sc08_200 with dissolve
    ib "My most frequent clientele are mature women, either widowed, bored of their husbands or single by choice."
    scene ch7sc08_199 with dissolve
    ib "Which makes them seek out my establishment in pursuit of a young stallion… such as you."
    scene ch7sc08_200 with dissolve
    ib "I have a hunch… you’re just enough of a stallion to make such women… ravenous."
    scene ch7sc08_198 with dissolve
    mc "*Chuckles* Okay… I can see why you’d favor my chances here."
    mc "I’m [mc] by the way."
    scene ch7sc08_201 with dissolve
    ib "[mc]... mmh, an appealing name."
    ib "Tell me, [mc]... do you find older women… alluring?"
    scene ch7sc08_202 with dissolve
    mct "Hmm, I better flirt a little with her… after all, she is supposedly friendly with Rose according to Luna."
    mc "Yeah… I’ve travelled far and wide, and one thing I’ve picked up on which seems to be true wherever I go…"
    mc "Is that mature women all over the kingdom share a certain… allure."
    scene ch7sc08_201 with dissolve
    ib "Mmhh… that we do…. that… we… do."
    ib "A mature woman holds knowledge our sweet youth can only dream of when it comes to… being with a man."
    scene ch7sc08_202 with dissolve
    mc "I agree… having been with both younger women and mature women…"
    mc "I’d take a night with a woman in her prime, over ten nights with a younger woman."
    scene ch7sc08_201 with dissolve
    ib "Oh my… *Giggles* You certainly have a way of… speaking your mind."
    ib "A most attractive quality… one often not found in younger men… they’re usually more… timid."
    scene ch7sc08_203 with dissolve
    ib "Don’t forget… there are certain… heavy… perks let’s say, to being with an older woman."
    ib "Tell me… what’s the oldest you’ve taken to bed?"
    scene ch7sc08_204 with dissolve
    mc "My oldest… hmm… it would have to be when I was just 18, I took a woman to bed who was around 38 at the time."
    mc "She kind of… taught me the ways of treating a woman’s body."
    mc "She gave me experience, a lot of it, more than any young man could dare hope for at that age."
    scene ch7sc08_203 with dissolve
    ib "Mmhh… that explains it… your confidence… it has been instilled by a mature woman from an early age."
    ib "You know… mature women only get better with age…"
    scene ch7sc08_201 with dissolve
    ib "Would you… ever consider being with someone… beyond 45?"
    scene ch7sc08_202 with dissolve
    mc "Beyond 45? Are you thinking 50’s? I wouldn’t have any issues honestly."
    scene ch7sc08_201 with dissolve
    ib "50’s? No… not quite…"
    scene ch7sc08_203 with dissolve
    ib "I’m thinking more like… someone in her 60’s, fully matured… deep into her prime."
    ib "A woman who knows her own body intimately, desperately longing to share it with a one of a kind man."

    ####Choice####
    menu:
        "Let’s drive it home. ({color=#ff8cdd}Romance{/color})":
            scene ch7sc08_204 with dissolve
            mc "A woman such as you described… is a woman I’d happily take to bed and… claim."
            ib "Mmhh…"
            mc "If I were to find myself such a woman… I’d enjoy her several times throughout the night… again… and again."
            scene ch7sc08_203 with dissolve
            ib "*Moans softly* Nnhh… what a thought… mmh…"
            ib "I believe a woman like that… would love to spend her life taking care of your needs…"
            ib "Riding her young stallion… satisfying his every desire… it would become her life's purpose."
            scene ch7sc08_204 with dissolve
            mc "That’s the kind of woman whose desires I’d never deny…"
            ib "*Giggles softly* Mhm-hmm…"
            "Bree is enjoying your sexual back and forth, her trust has increased by {size=+3}{b}{color=#2bff8b}3{/color}{/b}{/size}."
            $ ib_trust += 3
            scene ch7sc08_200 with dissolve
            ib "Oh! Would you look at that… your ale must've gone stale… I’ll bring you a refill, on the house."
            scene ch7sc08_205 with dissolve
            mc "Much appreciated… Bree."
            ib "I won’t act like its all in the matter of selflessness… as I mentioned earlier…"
            ib "You being here is… something my regular clientele will find alluring, which means they’ll return more often."
            scene ch7sc08_197 with dissolve
            ib "So, putting your ales on the house is a cheap investment. *Snickers*"
            ib "I only wish I could offer you ale with my special flavor added…"
            ib "But I’m afraid that’s only something I offer in… private… to someone who’s earned it."
            scene ch7sc08_198 with dissolve
            $ ib_path = True
            mc "Special flavor? Consider me intrigued… I guess I’ll have to earn it then."
            scene ch7sc08_199 with dissolve
            ib "*Giggles* Oh I hope you manage to do so… it’s been so… so… long."

        "Break off the flirtation. ({color=#2bff8b}Friendship{/color})":
            scene ch7sc08_198 with dissolve
            mc "I think that’s too much of an age difference for my tastes."
            scene ch7sc08_199 with dissolve
            $ ib_path = False
            ib "I see… that’s a shame, but I understand…"
            ib "At least you will have no shortage of women in their 30’s, 40’s and even 50’s in here."

    scene ch7sc08_206 with dissolve
    ib "Rose!"
    ib "Lovely to see you here tonight, Arazalian red as usual?"
    scene ch7sc08_207 with dissolve
    ro "Evening Bree."
    ro "Arazalian red would be lovely, thank you."
    scene ch7sc08_208 with dissolve
    ro "Hmm?"
    mc "Hey… fancy meeting you here."
    scene ch7sc08_209 with dissolve
    ro "[mc]? Are you following me?"
    scene ch7sc08_208 with dissolve
    mc "*Chuckles* Don’t flatter yourself, you may be gorgeous, but I’m already two ales deep."
    scene ch7sc08_209 with dissolve
    ro "Sorry, that was a little rude of me to assume such a thing… I guess I’m a little on edge."
    scene ch7sc08_210 with dissolve
    mc "Apology accepted, I guess I came here because I’m a little on edge myself."
    ro "*Gulps gently* Mmhh…"
    scene ch7sc08_211 with dissolve
    mc "Either that’s an incredible wine… or you really needed the alcohol."
    ro "Mmhh… both… mmh…"
    scene ch7sc08_212 with dissolve
    ro "Have you ever had Arazalia red?"
    ro "It’s imported from the vineyards in southern Arazalia."
    ro "They let it mature for at least ten years before they even export it."
    scene ch7sc08_213 with dissolve
    mc "I can’t say that I have… I’m honestly more of an ale type of a guy."
    mc "Although I do enjoy wine from time to time, is Arazalia red bitter or sweet?"
    scene ch7sc08_212 with dissolve
    ro "Why don’t you try…"
    scene ch7sc08_214 with dissolve
    ro "Here… you can taste mine, that way you won’t have to pay for a full glass in case you don’t enjoy it."
    mc "You’re okay with me drinking from your glass?"
    ro "*Scoffs lightly* I don’t mind… I’ve only had one sip."
    scene ch7sc08_215 with dissolve
    mc "I certainly don’t mind either… very well, bottoms up."
    ro "*Nods* Mmh."
    scene ch7sc08_216 with dissolve
    mc "Mmhh… surprisingly sweet?"
    ro "*Giggling* I’m a woman after all… we tend to favor sweet things."
    scene ch7sc08_217 with dissolve
    ro "So, did you enjoy it? Or was it too sweet for you?"
    scene ch7sc08_218 with dissolve
    mc "Honestly… pretty good."
    mc "Which berry or fruit is it based on?"
    scene ch7sc08_217 with dissolve
    ro "Arazalia red is based on a local berry from Arazalia’s deepest desert dunes, Azuberries, which only grows there."
    ro "They’re incredibly sweet, so the wine doesn’t need any additional sweeteners."
    scene ch7sc08_218 with dissolve
    mc "You know your wines."
    mc "Great taste in wine… incredibly beautiful... excellent leader of a guild... quite the woman, Rose."
    scene ch7sc08_217 with dissolve
    ro "*Scoffs lightly* Oh please… I’m 35, single, admonished by my family…"
    ro "The guild duties keep me somewhat busy, but in my spare time? It gets lonely at times…"
    ro "Diving into various hobbies keeps me occupied."
    scene ch7sc08_219 with dissolve
    ro "Bree, two more Arazalian reds, please."
    ib "Two Arazalian reds, coming right up."
    mc "Rose-"
    scene ch7sc08_220 with dissolve
    ro "Don’t… don’t try to play the man and deny this just because a woman is paying."
    ro "This is on me, a welcome gift from your guildmaster, to her intriguing and talented new student."
    scene ch7sc08_221 with dissolve
    mct "*Chuckles* Perfect… now, let’s play it off to make her insist."
    mc "Rose… I don’t know… Arazalian red is expensive and I would feel indebted to you-"
    scene ch7sc08_220 with dissolve
    ro "*Giggling* I wouldn’t mind having a man such as you… indebted to me."
    scene ch7sc08_221 with dissolve
    "You feel Rose’s gentle touch run along your forearm and onto your hand."
    scene ch7sc08_222 with dissolve
    ro "Something tells me… you’re a man who will work hard to earn his way out of a debt… mmh."
    ro "Please… accept my gift? Unless… you don’t wish to share a drink with me?"
    scene ch7sc08_223 with dissolve
    mc "I think we both know I’d love to share a drink with a woman of your caliber… very well."
    mc "I’ll accept your generosity."
    scene ch7sc08_222 with dissolve
    ro "*Giggling* Good! I wouldn’t have it any other way."
    ro "You’re… very interesting, [mc]."
    ro "Touching your arm like this… I can feel the magic coursing through your veins… truly incredible."
    scene ch7sc08_223 with dissolve
    mc "You’re not fooling anyone either, you know?"
    scene ch7sc08_222 with dissolve
    ro "*Giggles softly* No?"
    scene ch7sc08_223 with dissolve
    mc "No… I can sense your magic through your touch… you’re no slouch yourself."
    scene ch7sc08_222 with dissolve
    ro "You become more interesting by the minute, I usually keep my magic suppressed unless I’m casting."
    ro "You seem to… rile up my magic? I’d even say it feels like a light tingling… mmh."
    scene ch7sc08_221 with dissolve
    mc "A light tingling huh? I’d like to believe that is because you’re touching me and not from the wine."
    ro "*Snickers* Mmh…"
    scene ch7sc08_220 with dissolve
    ro "It takes more than half a glass of wine to make me… tingle."
    ro "Which means… it must be you."
    scene ch7sc08_224 with dissolve
    ib "Here you go darlings, two glasses of Arazalian red for my long time patron and her handsome suitor."
    ro "Thank you Bree, you’re an absolute doll."
    ro "And he might be handsome but he isn’t my suitor… he’s my student at the guild."
    scene ch7sc08_225 with dissolve
    ib "Deepest apologies for assuming… he definitely seems like the type of man you’d enjoy."
    ro "Who says I’m not enjoying him? *Snickers*"
    scene ch7sc08_226 with dissolve
    ro "He’s quickly becoming my… favorite student."
    uk "Bree! Three ales!"
    ib "Three ales coming right up!"
    scene ch7sc08_227 with dissolve
    mc "*Chuckles* Favorite student? Either my competition is horrid or-"
    scene ch7sc08_228 with dissolve
    ro "-Or you’re special. *Giggles lightly*"
    ro "Whether you’re the best at magic, I’ll have to discover through your attendance."
    ro "But you’re certainly the best looking. *Snickers*"
    scene ch7sc08_227 with dissolve
    mc "*Chuckles* My guildmaster finds me attractive? Interesting."
    ro "*Scoffs* Mhm-hm…"
    scene ch7sc08_228 with dissolve
    ro "Let’s have some wine before your head inflates to the size of the sphere of magnitude."
    scene ch7sc08_229 with dissolve
    mc "Speaking of the sphere…"
    mc "You’ve seen my test results, haven’t you?"
    scene ch7sc08_230 with dissolve
    ro "Mhm, I have."
    mc "And yet… you haven’t brought it up?"
    ro "No… I haven’t."
    scene ch7sc08_229 with dissolve
    ro "[mc], your secret is safe with me… should you wish to tell the others about you… then that is up to you."
    mct "Perfect, she is looking to create trust between us."
    mc "Very well, Rose. I’ll trust you, you have been nothing but welcoming towards me."
    scene ch7sc08_230 with dissolve
    ro "I promise… this will remain between us."
    ro "The others might catch on though, Celine and Lina are quite intelligent."
    scene ch7sc08_229 with dissolve
    mc "If they do, it’s not a big deal, but I would like the chance to tell them on my terms when I know them better."
    scene ch7sc08_231 with dissolve
    ro "I know what you mean…"
    ro "Secrets can weigh heavy on one's soul."
    scene ch7sc08_232 with dissolve
    mc "Sounds like you speak from experience?"
    scene ch7sc08_231 with dissolve
    ro "I do… but let’s not focus on my regrets tonight."
    scene ch7sc08_232 with dissolve
    mc "I won’t pry, I’m sure you’ll confide in me if you ever feel comfortable enough, if not, that’s okay."
    scene ch7sc08_231 with dissolve
    ro "Could you stop being so bloody perfect? *Giggling* You’re making it hard for me…"
    ro "To… resist… my emotions… my desires…"
    scene ch7sc08_232 with dissolve
    mc "I’m a firm believer that a woman should never withhold her desires, especially in the company of a proper man."
    ro "*Whimpers softly* Mmhm…"
    scene ch7sc08_231 with dissolve
    ro "Is that what you are [mc]? A proper man?"
    scene ch7sc08_232 with dissolve
    mc "I’d say so, until I’m alone with a woman who has earned my desire… then I become anything but proper."
    ro "*Giggles softly* Mmhm…"
    scene ch7sc08_231 with dissolve
    ro "That sounds… exactly like the type of man I’m looking for…"
    ro "Someone respectful and protective but also capable of tearing off my clothes whenever he desires me."
    ro "Goodness… listen to what I’m saying… it must be the wine, I’ve already had two glasses."
    scene ch7sc08_232 with dissolve
    mc "A woman like you can definitely handle a third, how about a glass on me this time?"
    scene ch7sc08_231 with dissolve
    ro "I really shouldn’t…"
    scene ch7sc08_232 with dissolve
    "Rose gently caresses your hand as she contemplates a third glass."

    if leadership >= 20:
        scene ch7sc08_223 with dissolve
        mc "You're incredibly hardworking, both from what I can tell and what I hear from others."
        mc "You lead the guild with ambition and care, you strive to be the best you can be."
        mc "Not just for yourself, but for the overall wellbeing of the guild and it's members."
        scene ch7sc08_222 with dissolve
        ro "Mmh... you've really paid attention to me..."
        scene ch7sc08_223 with dissolve
        mc "I have... you're a woman worthy of my interest, Rose."
        mc "I find a woman with a strong sense of self and leadership qualities very appealing."
        mc "I think we should have another glass and continue to enjoy our night, don't you?"
        scene ch7sc08_222 with dissolve
        ro "Mmh... I find your suggestion... irresistible."
        "Rose finds your ability to guide the conversation appealing, she takes note of your leadership ability."

    else:
        pass

    scene ch7sc08_219 with dissolve
    ro "Bree, two more, please."
    ib "Two more Arazalian reds? The two of you must be hitting it off?"
    ro "He’s not just easy on the eyes… but easy to talk to as well."
    scene ch7sc08_220 with dissolve
    ro "So yes… I’d say we’re hitting it off. *Giggles*"
    scene ch7sc08_221 with dissolve
    mct "I have her giggling at the thought of spending time with me, this is going better than I had expected."
    mc "I have to agree, you’re lovely to talk to Rose… we’ve been chatting for well over an hour at this point."
    scene ch7sc08_222 with dissolve
    ro "It’s been closer to… two hours."
    scene ch7sc08_223 with dissolve
    mc "*Chuckles* Is that so? That’s crazy…"
    scene ch7sc08_222 with dissolve
    ro "Mhm-hm… time has a way of getting away from you when you’re… immersed with someone who you enjoy."
    ro "Someone who can make you forget the weight of your day to day decisions and responsibilities."
    scene ch7sc08_223 with dissolve
    mc "Is that what I am? Someone who can take your mind off the bad things?"
    scene ch7sc08_222 with dissolve
    ro "Mmh… I’ll just say this, I haven’t had a single bad thought since seeing you in here."
    ro "*Snickers* Okay, that wasn’t true! I’ve had several… bad thoughts… but they all involve you… being tied up."
    scene ch7sc08_223 with dissolve
    mc "*Chuckles* Now you’re sending my mind spiraling…"
    mc "In these bad thoughts of yours… am I tied up in a dungeon or… to your bed?"
    scene ch7sc08_222 with dissolve
    ro "*Giggling* That’s for me to know… and for you to… discover."
    ro "If you prove to be the quality of man I’m starting to sense you to be."
    scene ch7sc08_220 with dissolve
    ro "And my senses rarely let me down."
    scene ch7sc08_221 with dissolve
    mc "Bree, two more Arazalian reds for this beauty of a woman and myself."
    ro "*Giggling softly* Mmh…"
    ib "Coming right up!"
    scene ch7sc08_220 with dissolve
    ro "Do you really find me beautiful? This isn’t the first time you’ve called me that."
    scene ch7sc08_221 with dissolve
    mc "Rose… how do I put this… I’m struggling to take my eyes off you whenever we’re in each others vicinity."
    mc "Tonight even more so than previously."
    "Rose gently squeezes your forearm as a sign of accepting your compliment."
    scene ch7sc08_224 with dissolve
    ib "Here you are, these are the last Arazalian reds for tonight."
    ro "You’re cutting us off? *Scoffs lightly*"
    ib "I am, otherwise this handsome young man will end up carrying you home."
    ro "*Snickers* I fear I fail to see why that would be such a bad thing."
    scene ch7sc08_225 with dissolve
    ib "*Giggling* I knew you would say something like that! I’m afraid that wasn’t the only reason, this was my last casket of Arazalian red."
    ro "*Sighs* I guess we’ll have to enjoy this last glass thoroughly then."
    scene ch7sc08_226 with dissolve
    ib "Aboslutely! You better savor every last drop, it’ll be around a week until next delivery."
    ro "Oh, with company as magnificent as this, we’ll savor it… isn’t that right, [mc]?"
    scene ch7sc08_227 with dissolve
    mc "You’ve got that right, I can’t think of anyone else I’d rather savor this last glass with."
    ro "*Giggles* Mh-hm."
    scene ch7sc08_228 with dissolve
    ro "I feel like… maybe we should cheer to something?"
    ro "To commend what has been a most lovely evening."
    scene ch7sc08_227 with dissolve
    mc "You know… you’re right."

    if charisma >= 20:
        mc "An evening like this… with a woman like you… has certainly been better than meeting a random woman for the night."
        mc "As I said earlier, there’s no other woman I’d rather share this glass with tonight."
        scene ch7sc08_228 with dissolve
        ro "Stop it… you talking like that… while looking at me like this…"
        ro "It does things to a woman…"
        scene ch7sc08_227 with dissolve
        mc "If only you knew the things I imagine doing to you. *Chuckles*"
        ro "*Snickers* Mmhh…"
        mc "Let’s toast to us, fate has put us on each others paths, and I look forward to discovering why."
        scene ch7sc08_228 with dissolve
        ro "Mhm… I sense a magical future… remind me to thank fate if I ever meet her."
        ro "Cheers!"
        scene ch7sc08_227 with dissolve
        mc "To a magical future. Cheers!"


    else:
        mc "A little toast does seem in order, how about…"
        mc "To new experiences and a magical future, now that I’m with your guild."
        scene ch7sc08_228 with dissolve
        ro "I like it, to a magical future then…"

    scene ch7sc08_211 with dissolve
    ro "*Gulps gently* Mhmffhhh… it tastes so much sweeter with a man like you nearby."
    mc "It’s delicious… like the woman next to me, I’m sure."
    scene ch7sc08_229 with dissolve
    ro "Careful [mc], I’m still your guildmaster."
    mc "And you’re still as gorgeous and downright attractive."
    scene ch7sc08_230 with dissolve
    ro "Goodness… what am I to do with you?"
    mc "You could invi-"
    scene ch7sc08_233 with dissolve
    ro "You feel Rose run her hand up your arm, placing it on your chest."
    ro "Don’t… don’t finish that sentence, please."
    ro "I fear… I wouldn’t refuse you if you actually said it out loud."
    scene ch7sc08_234 with dissolve
    ro "It’s too soon… not to mention highly inappropriate."
    ro "You have no idea how badly I’d like to invite you back to my place…"
    scene ch7sc08_233 with dissolve
    ro "I believe you’re the man I’ve been waiting for… and yet… I need to restrain myself due to circumstances. *Sighs*"
    scene ch7sc08_235 with dissolve
    mc "It’s okay Rose, it won’t become any less taboo but…"
    mc "Getting to know each other better will just make our night of passion that much better when it happens."
    scene ch7sc08_233 with dissolve
    ro "You speak with such confidence…"
    ro "Do you really believe you can win my affections?"
    scene ch7sc08_234 with dissolve
    ro "It takes more than a handsome face and a little magical talent to earn my love."
    scene ch7sc08_235 with dissolve
    mc "Good, I like to earn my woman’s love and respect."
    ro "*Giggles softly* Mmh…"
    scene ch7sc08_234 with dissolve
    ro "You’re doing well… in that regard."
    scene ch7sc08_233 with dissolve
    ro "Just… keep doing what you’ve been doing…"
    ro "Then I have a feeling even I… your own guildmaster… won’t be able to resist you."
    scene ch7sc08_235 with dissolve
    mc "I’ll toast to that… winning your affection."
    scene ch7sc08_234 with dissolve
    ro "Cheers to you earning… me."
    scene ch7sc08_211 with dissolve
    ro "Mmhm… even better than before… mmh…"
    mc "The thought of us… together… must be making your tastebuds sensitive."
    ro "*Gulps softly* Don’t… say such things… mmh… so good."
    scene ch7sc08_231 with dissolve
    ro "Phew… that tasted incredible."
    ro "At this point… I’ll have to invite you to join me here again once Bree has gotten the next shipment of Arazalian red."
    scene ch7sc08_232 with dissolve
    mc "I wouldn’t be opposed to joining you for more evenings like this."
    scene ch7sc08_231 with dissolve
    ro "I came here to unwind after a bothersome day… too much paperwork…"
    ro "And here you are… turning my entire day around with a few hours of joyful chatting."
    scene ch7sc08_232 with dissolve
    mc "If only I had known this was your favorite bar… I’d have come here a long time ago."
    ro "*Snickers* Mmh…"
    scene ch7sc08_231 with dissolve
    ro "I’m afraid this is the end of our lovely evening, I better get home."
    ro "I’ll see you in class one of these days?"
    scene ch7sc08_232 with dissolve
    mc "Mhm, you will… here, I’ll walk you home."
    scene ch7sc08_231 with dissolve
    ro "Thank you, I appreciate the gesture, but you will not be walking me home…"
    ro "We both know how that will end… as I said, it’s too soon."
    scene ch7sc08_232 with dissolve
    mc "Alright, alright… I don’t like you walking home on your own, but I have a feeling you can handle yourself."
    scene ch7sc08_231 with dissolve
    ro "I can indeed… maybe next time… I’ll let you walk me home."
    ro "See you in class…"
    scene black with Dissolve(2)
    #play music explore_2 fadein 1.0
    stop music fadeout 1.0
    $ renpy.pause(0.8)
    scene ch7sc08_236 with Dissolve(2)
    play music forest_1 fadein 1.0
    #stop music fadeout 1.0
    $ renpy.pause(0.8)
    mct "*Sighs* That went well, certainly better than expected."
    mct "It was surprisingly easy to talk to her, our flirting came natural."
    scene ch7sc08_237 with dissolve
    mct "It’s a shame she’s in cahoots with Taron…"
    mct "If she is being somewhat genuine in our interactions she would make a good ally."
    mct "Not to mention she’s powerful, she’s probably about as strong as Cassandra, if Cassandra had her magic."
    scene ch7sc08_238 with dissolve
    mct "She spoke of regrets… it’s likely to do with her reason for betraying Cassandra and Luna."
    mct "It seems she has taken a liking to me though, both as a student at the guild and as a potential romantic partner."
    scene ch7sc08_239 with dissolve
    mct "No matter how sweet or flirty she is with me, I’ll have to remember she is currently an enemy."
    mct "She could even be on to me for all I know and her kindness is all an act to get me to lower my guard."
    scene ch7sc08_237 with dissolve
    mct "We could both be playing each other…"
    mct "But Taron hasn’t used her against me, at least that I know of…"
    scene ch7sc08_238 with dissolve
    mct "It could be he has other uses for her and she isn’t aware of me."
    mct "One thing is for certain, I can’t let it slip that I know either Luna or Cassandra, that would be a dead giveaway."
    scene ch7sc08_239 with dissolve
    mct "I’ll keep applying my charm for now and see how it goes."
    mct "But if it comes to it, I won’t have an issue with a more… direct approach."
    scene ch7sc08_240 with dissolve
    ib "[mc]? *Snickers* Hellooo?"
    ib "You good? You’re kind of spacing out."
    scene ch7sc08_241 with dissolve
    mc "Hmm? Oh, Bree."
    mc "Sorry, what did you say? I was a bit lost in thought."
    scene ch7sc08_242 with dissolve
    ib "I was just saying how lovely it was to see you with Rose tonight."
    ib "She’s been coming here for over a decade, and I’ve never seen her give any man the time of day."
    scene ch7sc08_243 with dissolve
    mc "Really? Huh… I kind of thought she would’ve been a bit of a maneater."
    mc "She’s definitely gorgeous enough to get pretty much any man she wants."
    scene ch7sc08_242 with dissolve
    ib "She sure is… and believe me, it isn’t for lack of suitors attempting to win her over."
    ib "And I know how lonesome it can be as a single woman… we naturally seek companionship in a man."
    scene ch7sc08_244 with dissolve
    ib "So the fact she has kept rejecting men for years… it was finally nice to see her let loose and enjoy herself for once."
    ib "She actually smiled and giggled… seems I was right about you… you did become popular here tonight."
    scene ch7sc08_245 with dissolve
    mc "I enjoyed myself in her company, I had only seen her as my guildmaster previously."
    mc "Seeing her here tonight, she felt different, like a woman I’d love to spend time with."
    scene ch7sc08_244 with dissolve
    ib "I believe she feels the same way about you, Rose doesn’t bother with any man, not even for a few minutes."
    ib "And here you are… having kept her interest for well over three hours."
    scene ch7sc08_245 with dissolve
    mc "Time really did fly by…"
    scene ch7sc08_244 with dissolve
    ib "I might be biased as I’m her friend but… Rose needs a good man in her life."
    scene ch7sc08_242 with dissolve
    ib "A man who can balance out the weight and pressure of her daily life as a guildmaster."
    ib "I’m afraid that’s all the advice we have time for tonight, it’s about time I close up and get some rest."
    scene ch7sc08_243 with dissolve
    mc "Sure, I appreciate your insight, Bree."
    mc "Do you need help closing?"
    scene ch7sc08_242 with dissolve
    ib "You’re sweet, but I’ll be fine… you should head home and rest as well."
    ib "I hope to see you around here again sometime?"
    scene ch7sc08_244 with dissolve
    ib "If not for Rose…"
    ib "Then perhaps for me? *Giggles softly*"
    scene ch7sc08_245 with dissolve
    mc "*Chuckles* Maybe for both?"
    mc "One mature woman is a blessing, but two? That’s a slice of paradise."
    "Bree looks at you with a glint in her eye, she likes your confidence."
    scene ch7sc08_244 with dissolve
    ib "Don’t get ahead of yourself young man… but I certainly wouldn’t mind you coming by whenever you feel like it."
    scene ch7sc08_242 with dissolve
    ib "Goodnight, [mc]."
    scene ch7sc08_243 with dissolve
    mc "Goodnight, Bree. And thank you for the free ale earlier."
    scene black with Dissolve(2)
    #play music explore_2 fadein 1.0
    stop music fadeout 1.0
    $ renpy.pause(0.8)
    scene ss29 with Dissolve(2)
    $ renpy.pause()
    scene black with Dissolve(2)
    $ renpy.pause(0.8)
    play music darknight_4 fadein 2.0
    #stop music fadeout 1.0
    scene ch6sc07_143 with Dissolve(2)
    $ renpy.pause(0.8)
    ri "*Panting* Hnngh… last encounter… almost… got me."
    ri "Heavily outnumbered… need to be… careful."
    scene ch6sc07_144 with dissolve
    tg "There she is! Get her! Quit running and accept your fate!"
    ri "!!"
    scene ch7sc08_246 with dissolve
    with vpunch
    ri "*Groans* Hnngh!"
    tg "She’s getting slower! She must be low on stamina! Don’t let her get away this time!"
    scene ch7sc08_247 with dissolve
    tg "I can’t believe how agile she still is!? We’ve been chasing her for hours!"
    tg "Don’t just stand there! Press the attack!"
    scene ch7sc08_248 with dissolve
    vi "You’ve done well evading us tonight… but as you can see, we’ve got you surrounded."
    vi "I’m afraid this is the end of the road for you sweetie."
    vi "I nicked you with my kunai earlier… surprisingly you’re still able to walk, even dodge our attacks?"
    scene ch7sc08_249 with dissolve
    vi "Last time we fought… you succumbed to my venom."
    vi "This time… it barely slows you down? Don’t tell me…"
    vi "You’ve been raising your tolerance since then?"
    scene ch7sc08_250 with dissolve
    vi "No matter… you’re still severely weakened by it. Get her!"
    tg "You shouldn’t have betrayed us! This is what you get!"
    scene ch7sc08_251 with dissolve
    ri "Not good… risk falling unconscious…"
    ri "Barely any… mana left… must… subdue them all."
    scene ch7sc08_252 with dissolve
    ri "*Groans* Hurts to move… not immune to her venom…"
    scene ch7sc08_253 with dissolve
    ri "No… I’m… too weak? I… can’t… hnnghh…"
    scene black with Dissolve(2)
    #play music explore_2 fadein 1.0
    stop music fadeout 1.0
    $ renpy.pause(0.8)
    play music intro_1 fadein 1.0
    #stop music fadeout 1.0
    scene ch7sc08_254 with Dissolve(2)
    $ renpy.pause(0.8)
    mct "*Inhales* Nothing like a bit of fresh air to clear one's mind."
    mct "I made good progress with Rose tonight…"
    mct "We’ll see how it plays out, if push comes to shove, I’ll force her to dissolve the hex she’s placed on Cassandra."
    scene ch7sc08_255 with dissolve
    mct "I would prefer if we can make an ally of her."
    mct "Turning her to our side, possibly without Taron knowing… could be a potent advantage."
    $ renpy.pause(0.7)
    with vpunch
    $ renpy.pause(0.7)
    scene ch7sc08_256 with dissolve
    with vpunch
    mct "What the hell was that?"
    with vpunch
    mct "This feeling… it’s her- Rin."

    if dark >= 10:
        scene ch7sc08_257 with dissolve
        mct "She’s hurt!"
        scene ch7sc08_258b with dissolve
        with vpunch
        $ renpy.pause()
        scene ch7sc08_258 with dissolve
        $ renpy.pause()

    else:
        scene ch7sc08_257b with dissolve
        mct "She’s hurt!"
        scene ch7sc08_258b with dissolve
        with vpunch
        $ renpy.pause()
        scene ch7sc08_258 with dissolve
        $ renpy.pause()

    scene black with Dissolve(2)
    #play music explore_2 fadein 1.0
    stop music fadeout 1.0
    $ renpy.pause(0.8)
    play music darknight_4 fadein 2.0
    #stop music fadeout 1.0
    scene ch7sc08_251 with Dissolve(2)
    $ renpy.pause(0.8)
    ri "Needs to work… can’t… afford to lose."
    scene ch7sc08_259 with dissolve
    ri "*Groans* Aah! Movements… too slow!"
    tg "You really thought you could escape the society forever? I’ve been waiting for this!"
    scene ch7sc08_260 with dissolve
    ri "N-Not good! Can’t defend!"
    scene ch7sc08_261 with dissolve
    with vpunch
    ri "*Groans* Urh!"
    tg "Nice one, brother! A kick like that to the noggin? She’ll have a headache for days!"
    scene ch7sc08_249 with dissolve
    vi "Grab her and let’s be done with this."
    tg "You heard Viperia brothers! Grab the betrayer!"
    scene ch7sc08_262 with dissolve
    tg "I don’t know what possessed you to betray the society, sister."
    tg "But you’re not going to like what’s in store for you back at headquarters."
    tg "She doesn’t look too good, think your kick gave her a concussion?"
    tg "Nah, it’s due to exhaustion from using up all her mana trying to escape us for the last couple of hours with that wind magic."
    #play music explore_2 fadein 1.0
    stop music fadeout 1.0
    ri "Please… let… me go…"
    play music dark_3 fadein 1.0
    #stop music fadeout 1.0
    scene ch7sc08_262b with dissolve
    with vpunch
    $ renpy.pause(0.5)
    with vpunch
    scene ch7sc08_263 with dissolve
    tg "What the-"
    scene ch7sc08_263b with dissolve
    with vpunch
    $ renpy.pause(0.5)
    with vpunch
    scene ch7sc08_264 with dissolve
    rit "This… feeling… he… came."
    scene ch7sc08_265 with dissolve
    rit "It’s… him."
    rit "He… came for-... me? Hnngh…"
    scene ch7sc08_266 with dissolve
    rit "Nnghh…"
    scene ch7sc08_267 with dissolve
    tg "He killed them! You’ll pay for this!"
    vi "Would you look at that… seems like we’ve got ourselves a little hero entering the mix. *Scoffs*"
    vi "Kill him and grab Rin, we’ve wasted enough time in this wretched city."
    scene ch7sc08_268 with dissolve
    tg "Sorry buddy! But you shouldn’t have interfered in society business!"
    scene ch7sc08_269 with dissolve
    with vpunch
    tg "ARrgh!?"
    tg "What the fuck is this goo!? I-I can’t move!?"
    scene ch7sc08_266 with dissolve
    $ renpy.pause()
    scene ch7sc08_270 with dissolve
    $ renpy.pause()
    "Rin whimpers in relief as she passes out upon feeling the comfort of your touch."
    mc "..."
    scene ch7sc08_271 with dissolve
    mc "......."
    tg "I can’t move! The more I try the firmer this goo latches on!"
    scene ch7sc08_272 with dissolve
    mc "..."
    scene ch7sc08_273 with dissolve
    tg "What in the hells is this!? Some sort of illusion magic!?"
    tg "Our blades can’t cut it! What kind of freak are you!?"
    scene ch7sc08_274 with dissolve
    tg "Release us! You’ll regret this!"
    tg "You’re some freak of nature! This isn’t any magic I’ve seen before!"
    scene ch7sc08_275 with dissolve
    tg "*Cries in agony* ArrHHH! I’m being stretched!! AhHRHh! My bones are going to snap!!"
    tg "Stop it! What are you doing to him!?"
    scene ch7sc08_276 with dissolve
    with vpunch
    "The sound of bones cracking, limbs snapping and deep agonizing screams fill the otherwise quiet night."
    "Onyx strengthens her grasp, not only snapping his arms out of their joints, but crushing his bones beneath the skin."

    if irene_alive == True:
        scene ch7sc08_277 with dissolve
        vi "*Muffled* Mmf-mffh!"
        ir "Hnngh! Be quiet and stop struggling!"
        vi "*Muffled* Mmffhh! B-Bitch! Fffghh! Backstabbing whore- Ffhhh! Our Shadow-brothers are dying-"
        ir "I’m not backstabbing you, I’m saving your life!"
        ir "Calm down and I’ll release you."
        scene ch7sc08_278 with dissolve
        vi "*Coughs quietly* Hnnh… fuck… I’ve taught you well… that was a good chokehold."
        vi "What are you saying though? I had a perfect opportunity to strike him down."
        ir "No you didn’t!"
        scene ch7sc08_279 with dissolve
        ir "You wouldn’t have stood a chance! You saw how he immobilized our Shadow-brothers without even flinching!"
        vi "You speak as if you are familiar with this man?"
        scene ch7sc08_280 with dissolve
        ir "I-... I am, I’ve met him before… he’s the one who killed Rammus and… spared me."
        vi "He’s the one who killed Rammus? Didn’t you say he was a demon?"
        scene ch7sc08_279 with dissolve
        ir "I did- I mean… I don’t know!? He could do things like no ordinary man would be able to do."
        ir "The way he moves… the way he endures attacks… he can’t be human, I know that much!"
        scene ch7sc08_280 with dissolve
        ir "And if he becomes aware of our presence, we’ll die as well as our Shadow-brothers."
        vi "Fuck… hnngh… I don’t like it… but you’re right… he’s tearing them apart without breaking a sweat."
        scene ch7sc08_279 with dissolve
        ir "Just observe him, okay? Silently from the shadows, I don’t want to return to the society without you."
        scene ch7sc08_280 with dissolve
        vi "Fine… fine! We’ll observe him."


    else:
        scene ch7sc08_281 with dissolve
        vit "Fuck… it’s a good thing I trusted my gut, hiding instead of attacking was definitely the right choice."
        vit "The way he’s dismantling my Shadow-brothers… he’s not even breaking a sweat or flinching."
        vit "He is more than we’re equipped to handle tonight."
        with vpunch
        tg "AarrghhH!! I-I can’t feel my arms!"

    scene ch7sc08_282 with dissolve
    tg "P-Please! Stop it! Show mercy!"
    tg "We were only following our orders! That girl you’re holding is a contract!"
    tg "You’ve broken our arms and legs! We’re powerless to pursue you!"

    ####Choice####
    menu:
        "Let them live. ({color=#87e1fa}Light Path{/color})":
            scene ch7sc08_283b with dissolve
            mc "..."
            $ light += 2
            tg "P-Please! Spare us! W-We’ll return to the society and deny any future contracts on her!"
            scene ch7sc08_283 with dissolve
            mc "..."
            "You nod in agreement."
            tg "T-Thank you! W-Won't come after her again! F-Fuck this!"
            "Your {color=#87e1fa}light morality{/color} has increased by  {size=+3}{b}{color=#2bff8b}2{/color}{/b}{/size}."

        "Crush them completely. ({color=#fc584c}Dark Path{/color})":
            scene ch7sc08_283a with dissolve
            "..."
            "Onyx is able to sense your bloodlust."
            ox "Yes master!"
            scene ch7sc08_282 with dissolve
            tg "P-Please! Stop it! Show mercy-"
            scene ch7sc08_284 with dissolve
            with vpunch
            $ dark += 2
            bth "{size=+10}{b}*Blood-curdling screams* AArhgh! Ahhrrhh!! Hhrh-hh-hhggh…{/b}{/size}"
            with vpunch
            "In an instant, Onyx fully crushes their bodies, turning their bones to powder and obliterating their internal organs."
            "Your {color=#f00}dark morality{/color} has increased by  {size=+3}{b}{color=#2bff8b}2{/color}{/b}{/size}."

    scene ch7sc08_285 with dissolve
    #play music explore_2 fadein 1.0
    stop music fadeout 1.0
    $ renpy.pause()
    play music intro_1 fadein 1.0
    #stop music fadeout 1.0
    scene ch7sc08_286 with dissolve
    $ renpy.pause()
    scene ch7sc08_287 with dissolve
    $ renpy.pause()
    scene ch7sc08_288 with dissolve
    $ renpy.pause()
    scene ch7sc08_289 with dissolve
    $ renpy.pause()
    scene ch7sc08_290 with dissolve
    $ renpy.pause()
    scene ch7sc08_291 with dissolve
    $ renpy.pause()
    scene ch7sc08_292 with dissolve
    $ renpy.pause()
    scene black with Dissolve(2)
    #play music explore_2 fadein 1.0
    stop music fadeout 1.0
    $ renpy.pause(0.5)
    scene black with Dissolve(2)
    stop music fadeout 1.0
    $ renpy.pause()
    #"{color=#00ff00}End of v0.6.8 {b}PLEASE SAVE YOUR GAME HERE! OR A FEW IMAGES BACK!{/b}{/color}"
    #"{color=#00ff00}End of v0.6.8 {b}PLEASE SAVE YOUR GAME HERE! OR A FEW IMAGES BACK!{/b}{/color}"
    scene black with dissolve
    $ renpy.pause(0.1)
    stop music fadeout 1.0
    #jump endofversion
    jump ch7sc10
