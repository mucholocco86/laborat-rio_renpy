
label ch3sc2:




    window hide dissolve
    play music tavern_2 fadein 1.0
    scene ss68 with Dissolve (2.0)
    $ renpy.pause()
    scene ch3sc02_001 with Dissolve(2.0)
    $ renpy.pause(0.7)
    el "I wonder why we need a city-pass?"
    el "We didn’t hear any mention of it earlier on our travels."
    scene ch3sc02_002 with dissolve
    mc "It could be a recent thing."
    mc "Maybe something has happened recently that travelers wouldn't know about?"
    scene ch3sc02_003 with dissolve
    el "We'd better remember to get ours at the guild. We might have gotten lucky this time."
    el "I suspect not every guard is easily manipulated."
    scene ch3sc02_004 with dissolve
    el "You handled it well back there, but..."
    if intimidation >= 1:
        el "We can't rely on you intimidating the guards."

    else:
        el "We can't rely on you persuading the guards with your charms."

    el "Milton was rather easy to sway, I doubt all the guards will be though."
    scene ch3sc02_005 with dissolve
    el "And I can't emphasize how much I don't want to see the inside of a cell."
    scene ch3sc02_006 with dissolve
    mc "Are you doubting my social skills? You’re the one teaching me."
    mc "I was using what my teacher has bestowed upon me. *Chuckles*"
    scene ch3sc02_007 with dissolve
    el "And you’ve definitely been improving! But don’t get cocky on me, mister!"
    scene ch3sc02_008 with dissolve
    mc "You said it yourself, the student will surpass the teacher."
    scene ch3sc02_009 with dissolve
    el "I-I... I was... that’s not the same! Urrh!"
    el "You still have a long way to go. Especially when it comes to dealing with nobles."
    el "So don't go getting too confident just yet."
    scene ch3sc02_010 with dissolve
    el "Come on! Let’s just find the guild hall."
    mc "Shouldn't be much further, I was told it'd be near the plaza we passed thirty minutes ago."
    scene black with Dissolve(1.5)
    $ renpy.pause(1)
    scene ss16 with Dissolve(1.5)
    $ renpy.pause(0.5)
    "Your intel proved correct, the two of you arrive at the guild headquarters fifteen minutes later."
    scene ch3sc02_011 with Dissolve(1.5)
    $ renpy.pause(1)
    el "Phew! I was starting to think we wouldn't find it before sundown."
    scene ch3sc02_012 with dissolve
    mc "You're being dramatic... It only took us two, maybe three hours from the city-gates."
    mc "With the amount of winding streets and tall buildings, it's hard to navigate as newcomers."
    stop music fadeout 2.0
    scene black with Dissolve(1.5)
    $ renpy.pause(1)
    play music home_1 fadein 1.0
    scene ch3sc02_013 with Dissolve(1.5)
    $ renpy.pause(0.5)
    mct "Cozy. Although a little worn down..."
    mct "I kinda expected it to be more... lively?"
    scene ch3sc02_014 with dissolve
    el "This place is amazing! Can you believe we’re really here? {size=+3}{b}The Adventurers Guild!{/b}{/size}"
    el "You've just set foot in the place you always dreamed about as a youngster!"
    scene ch3sc02_015 with dissolve
    mc "Let’s not get too excited just yet..."
    mc "It doesn’t even look like anyone's here."
    scene ch3sc02_016 with dissolve
    el "Hello, anyone here?"
    scene ch3sc02_017 with dissolve
    $ renpy.pause()
    scene ch3sc02_018 with dissolve
    $ renpy.pause()
    scene ch3sc02_019 with dissolve
    with vpunch
    "Scrambling noises"
    scene ch3sc02_020 with dissolve
    el "Huh!? Did you hear that? I think it came from behind the counter."
    scene ch3sc02_021 with dissolve
    mc "Go on, check it out."
    scene ch3sc02_022 with dissolve
    el "W-Who me? N-No way! You go!"
    el "It c-could be something dangerous!"
    scene ch3sc02_021 with dissolve
    mc "Something dangerous? We're inside a building, Eliza."
    scene ch3sc02_022 with dissolve
    el "P-Please? One time a giant field rat charged me from behind a sack of wheat in Mother's cabin."
    el "I didn't sleep for days!"
    scene ch3sc02_021 with dissolve
    mc "Alright, alright. I'll check it out."
    scene ch3sc02_023 with dissolve
    mc "*Sigh* ..."
    scene ch3sc02_024 with dissolve
    $ renpy.pause(2)
    scene ch3sc02_025 with dissolve
    $ renpy.pause(2)
    scene ch3sc02_026 with dissolve
    "As you get closer to the desk, the rustling sound increases. Clearly, something is behind the counter."
    scene ch3sc02_027 with dissolve
    with vpunch
    uk "{b}Hi!{/b} Welcome to the Adventurers Guild!"
    uk "What can I do for the two of you?"
    scene ch3sc02_028 with dissolve
    mc "You’re a fae!"
    scene ch3sc02_029 with dissolve
    elt "{b}F-F-F-Fae?!{/b}"
    scene ch3sc02_030 with dissolve
    uk "Correct! I’m a fae! Good eyes!"
    scene ch3sc02_031 with dissolve
    uk "Can you guess which kind of fae, by any chance?"
    uk "Forest fairy? Pixie? Nymph? Sprite? Or perhaps I'm a Aquafii?"
    scene ch3sc02_032 with dissolve
    mc "Sorry, no."
    mc "I have no notion what the differences between the specific kinds of fae are."
    mc "You're my first fae."
    scene ch3sc02_033 with dissolve
    uk "{b}His first{/b}, he says! *Giggles* Interesting, very interesting!"
    scene ch3sc02_031 with dissolve
    uk "It’s not surprising at all. We aren’t the most common creatures in Midomir."
    scene ch3sc02_030 with dissolve
    uk "People used to hunt us and keep us in magically sealed cages to take advantage of our magic."
    scene ch3sc02_033 with dissolve
    uk "So, naturally, my kind grew wary of humans."
    uk "And we spread out far across Midomir, seeking shelter in secluded areas."
    scene ch3sc02_034 with dissolve
    mc "Does that mean you're hiding in here?"
    scene ch3sc02_031 with dissolve
    uk "By Earth-mother's roots! No, not hiding. Dalen, the guildmaster..."
    uk "He took me in. He's provided for me for over a decade by now."
    uk "In return, I manage the desk and daily tasks of the recruits here at the guild."
    scene ch3sc02_034 with dissolve
    mc "I’m [mc], and this is-"
    scene ch3sc02_035 with dissolve
    el "Eliza! Nice to meet you!"
    scene ch3sc02_031 with dissolve
    sy "I’m Sylphina, but everyone just calls me Sylph."
    sy "I'm a Forest fairy, or 'Fae' for short."
    scene ch3sc02_036 with dissolve
    sy "If you guys are here to put up a request or a bounty, please fill in the form over there."
    scene ch3sc02_037 with dissolve
    el "Actually, we’re here to join!"
    scene ch3sc02_038 with dissolve
    sy "Oh, oh! My goodness! New recruits!"
    scene ch3sc02_039 with dissolve
    sy "It’s so lovely to meet you! You’re actually the first recruits we've had this year."
    scene ch3sc02_040 with dissolve
    mc "We’re the first? How come?"
    scene ch3sc02_038 with dissolve
    sy "Who’s to say? Dalen, our leader, seems to think there’s foul play involved."
    sy "I'm inclined to believe him as well. Dalen has good instincts."
    scene ch3sc02_041 with dissolve
    el "Foul play? That doesn’t sound good."
    scene ch3sc02_038 with dissolve
    sy "Yeah, he thinks someone is intimidating potential recruits."
    scene ch3sc02_039 with dissolve
    sy "He can probably tell you more about it when you meet him."
    scene ch3sc02_041 with dissolve
    el "*Whispers* {size=-10}{b}We should definitely keep an eye out for anything suspicious while we’re in the capital.{/b}{/size}"
    scene ch3sc02_042 with dissolve
    mc "*Whispers* {size=-10}{b}Mhhmm. Stay alert.{/b}{/size}"
    scene ch3sc02_041 with dissolve
    el "*Whispers* {size=-10}{b}Me? I'm always alert. You stay alert!{/b}{/size}"
    scene ch3sc02_042 with dissolve
    mc "*Whispers* {size=-10}{b}You wouldn't know a threat if it stared you in the face.{/b}{/size}"
    scene ch3sc02_041 with dissolve
    el "*Whispers* {size=-10}{b}Rude! I would see it coming a mile away!{/b}{/size}"
    el "*Whispers* {size=-10}{b}I remember someone who got tricked by mean bandits.{/b}{/size}"
    scene ch3sc02_042 with dissolve
    mc "*Whispers* {size=-10}{b}I was just testing them.{/b}{/size}"
    scene ch3sc02_041 with dissolve
    el "*Whispers* {size=-10}{b}Mhhmm. What about the time I ambushed you by the campfire?{/b}{/size}"
    scene ch3sc02_042 with dissolve
    mc "*Whispers* {size=-10}{b}That was-{/b}{/size}"
    scene ch3sc02_036 with dissolve
    sy "You guys can go meet Dalen now. He'll be glad to see new recruits."
    scene ch3sc02_039 with dissolve
    sy "I have a feeling this is the beginning of something wonderful!"
    scene ch3sc02_032 with dissolve
    mc "Thank you, Sylph."
    scene ch3sc02_033 with dissolve
    sy "No worries! I’m so excited to finally have new recruits!"
    scene ch3sc02_043 with dissolve
    sy "Please come see me if you have any questions, or when you’re ready for your first quest!"
    stop music fadeout 2.0
    scene black with Dissolve(1.5)
    jump ch3sc3
