image mainmenu_anim = Movie(play="images/custom_gui/global/mainmenu/mainmenu_anim2.webm", loop=True)
default persistent.select_language_first = True
label splashscreen:
    if persistent.select_language_first:
        show screen language_selector_popup with dissolve
    call screen warning_screen with dissolve
    return

screen main_menu():
    tag menu

    on "show" action [Play("music", "images/custom_gui/global/mainmenu/mainmenu_song.mp3", fadein=2.0, loop=True)]  #  , Function(renpy.music.set_volume, 0.2, delay=0)
    on "hide" action [Stop("music", fadeout=2.0)]
    
    add "mainmenu_anim" at fade_in
    add "mainmenu_static" at fade_in
        
    
    imagebutton auto "newgame_%s":
        focus_mask True
        action [Start(), Hide("main_menu")]
    text "New Game":
        size 89.94 color "#fff" font "candara_bold.ttf" xpos 280 ypos 460 xanchor 0.5 yanchor 0.5
    
    imagebutton auto "load2_%s":
        focus_mask True
        action ShowMenu("load")
    text "Load":
        size 89.94 color "#fff" font "candara_bold.ttf" xpos 283 ypos 625 xanchor 0.5 yanchor 0.5
    
    imagebutton auto "gallery2_%s":
        focus_mask True
        action [
            SetVariable("in_gallery_gui_main", True), 
            Hide("main_menu"),
            Jump("scene_image_gallery")
        ]
    text "Gallery":
        size 89.94 color "#fff" font "candara_bold.ttf" xpos 283 ypos 783 xanchor 0.5 yanchor 0.5

    imagebutton auto "options2_%s":
        focus_mask True
        action ShowMenu("preferences")
    text "Options":
        size 89.94 color "#fff" font "candara_bold.ttf" xpos 280 ypos 950 xanchor 0.5 yanchor 0.5
    
    imagebutton auto "exit2_%s":
        focus_mask True
        action Quit()
    text "Exit":
        size 89.94 color "#fff" font "candara_bold.ttf" xpos 282 ypos 1125 xanchor 0.5 yanchor 0.5
    
    imagebutton auto "discord_%s":
        focus_mask True
        hovered SetVariable("screen_tooltip", "Start a New Game")
        unhovered SetVariable("screen_tooltip", "")
        action OpenURL("https://discord.gg/xWAETWkGVB")
    
    imagebutton auto "patreon_%s":
        focus_mask True
        hovered SetVariable("screen_tooltip", "Support us on Patreon!")
        unhovered SetVariable("screen_tooltip", "")
        action OpenURL("https://www.patreon.com/c/Kabuki_")


default persistent.textbox_opacity = 1.0

init python:
    def dynamic_textbox(st, at):
        return Transform(
            Image("gui/textbox2.png", xalign=0.5, yalign=1.0),
            alpha=persistent.textbox_opacity
        ), 0.1

default Opacity = 100
default seen_opacity_note = False
image game_intro = Movie(play="images/1_opening/scene01/game_intro.webm", loop=False)

label start:

label scene01:
    $ persistent.select_language_first = False
    show game_intro with dissolve 
    $ renpy.pause(4.15, hard=True)
    $ pregnancy_time = 30
    $ mc_karma = 5
    $ cycle = 0
    $ karma_updated = True
    $ diana_game_start = True
    scene 1_s00 with Fade(0.5,0.5,0.5)
    ""
    play music "nature.mp3" fadein 3.0 loop
    scene 1_s01 with Fade(1.0,1.0,1.0)
    ""
    scene 1_s02 with dissolve
    ""
    scene 1_s03 with dissolve
    ""
    scene 1_s04 with dissolve
    mcn "{i}Nngh...{/i}"
    scene 1_s05 with dissolve
    stop music fadeout 2.0
    mcn "{i}*groan*{/i} Huh...?"
    scene 1_s06 with dissolve
    play music "battle01.mp3" fadein 1.0 loop
    ""
    scene 1_s07 with dissolve
    mcn "Wha—?"
    mcn "What the fuck are you?!"
    play sound "sound_effects/slash02.mp3" 
    scene 1_s08 with vpunch
    mcn "{i}Nghh!{/i}"
    scene 1_s08_2 with dissolve
    mcn "Hah...! Hahh...!"
    scene 1_s09 with dissolve
    mcn "Shit! Shit! Shit! Shit!"
    play sound "sound_effects/slash03wood.mp3" 
    scene 1_s10 with vpunch

    mcn "{i}Argh!{/i}"
    scene 1_s11 with dissolve
    mcn "Come on, legs... move, damn it!"
    mcn "Please—look, we can work this out!"
    play sound "sound_effects/metalhit.mp3"  
    stop music fadeout 2.0
    scene 1_s12 with vpunch
    pause 0.3
    scene 1_s13 with dissolve
    pause 0.5
    scene 1_s14 with dissolve
    play music "nature.mp3" fadein 1.0
    mcn "..."
    mcn "Huh?!"
    mcn "W-What happened?!"
    play sound "sound_effects/grass.mp3" fadein 0.1
    scene 1_s15 with dissolve
    mcn "Hah... hah..."
    mcn "Is it... dead?"
    mcn "Okay... I need to calm dow—"
    scene 1_s15 with vpunch
    mcn "UGH! My head!"
    mcn "Maybe if I just closed my eyes."
    scene black with fade
    stop music fadeout 1.0
    mcn "This... this is a dream, right? It has to be."
    mcn "Yeah. What else could it be? Monsters like that don't exist. I'm just... having a nightmare. That's all. A really, really vivid nightmare." 
    mcn "I'll wake up any moment now..."
    sensation "The warmth of the damp earth seeps into your skin. Blades of grass tickle between your toes—you're barefoot, you realize suddenly. Barefoot in the middle of nowhere."
    play music "nature.mp3" fadein 1.0 loop
    scene 1_s15 with Fade(0.5,0.5,0.5)
    mcn "Shit... This isn't working out."
    scene 1_s17 with dissolve
    mcn "Alright... First of all, where the hell am I?"
    env "Endless grassy plains stretch as far as the eye can see, broken only by the occasional rock or rolling hill. A gentle breeze carries the scent of earth and fresh grass, while the sun beats down, warm against your skin."
    scene 1_s16 with dissolve
    mcn "And what killed that ogre? A falling cage?" 
    mcn "Must be one of your victims... ironic, isn't it?"
    mcn "This isn't the time for jokes! I need to find someone... anyone!"

default mc_lied = False
default mc_truth = False

label scene02:
    #char1 "{size=30}Hey! You! "
    scene 1_s18 with dissolve
    mcn "...I should go look around. Standing here isn't going to help. Maybe there's a road nearby."
    scene 1_s19 with Dissolve(2.0)
    sensation "After a few minutes, the adrenaline fades entirely, replaced by a exhaustion that makes every step an effort."
    scene 1_s20 with Fade(1.5,1.0,1.0)
    mcn "Hahh... Ahh..."
    scene 1_s21 with Dissolve(2.0)
    mcn "A road?! Finally! HELP! IS ANYONE AROUND?!"
    mcn "Wait a minute! What the hell am I doing?!"
    mcn "This clearly isn't my world. There's no such thing as ogres where I come from. And the flora looks weird. I've never seen some of them. Everything feels similar yet... wrong."
    mcn "Either I've gone completely batshit insane... or I've actually been transported to another world!"
    mcn "Why am I trying to get back to civilization? Back to bills, and stress, and people who don't give a shit about me?"
    mcn "M-Maybe I should rethink this."
    mcn "..."
    scene 1_s21 with vpunch
    mcn "No no no! Shake off these weird ideas... no matter how tempting they are."
    mcn "Someone's coming!"
    scene 1_s22 with Dissolve(2.0)
    mcn "Hey you! Don't be scared, I'm not a pervert!"
    char1 "What in the world?"
    scene 1_s23 with Fade(0.5,0.5,0.5)
    char1 "Who are you?! And where are your clothes?! You're completely naked!"
    scene 1_s24 with dissolve
    mcn "Long story, but I really need help!"
    scene 1_s23 with dissolve
    char1 "You need to breathe first. Slow down. Tell me—were you attacked? Are you hurt?"
    scene 1_s24 with dissolve
    mcn "No... I mean, yes! There was this ogre and—"
    scene 1_s23 with dissolve
    char1 "Ogre?!"
    scene 1_s24 with dissolve
    mcn "Yes! Big bastard! Attacked me when I woke up, wherever 'here' is. I still can't tell if this is a dream or not, but—"
    scene 1_s23 with dissolve
    char1 "What happened to it? Is it still following you?"
    scene 1_s24 with dissolve
    mcn "It's dead. And I feel like you're not hearing me..."
    scene 1_s23 with dissolve
    char1 "It can't be... No one's killed an ogre in these parts for months. The last one took the entire adventurers' guild working together."
    char1 "Show me. Where did you two fight? I need to see it."
    scene 1_s24 with dissolve
    mcn "Fight? Uhh... fine. Come on. It isn't too far. Just promise me you'll help after."
    scene 1_s23 with dissolve
    d "If what you say is true, I'll help however I can. My name is Darius, by the way."
    scene 1_s24 with dissolve
    scene 2_s6_2 with Fade(2.0,1.0,2.0)
    perception "You lead him back through the rolling grass. The sun has shifted slightly, you've been walking longer than you thought. Darius follows, his hand resting on the hilt of his sword, his eyes moving in every direction."
    mcn "Fuck... I'm not used to this. *cough* It's right here. See for yourself."
    d "By the gods..."
    scene 2_s2 with Dissolve(1.5)
    d "You're telling me you killed him? Alone?"
    scene 2_s3 with dissolve
    mcn "Uhh..."
    scene 2_s2 with dissolve
    d "Do you have any idea what this means? The bounty on an ogre is fifty gold pieces. Fifty!"
    d "That's more than most people earn in a decade!"
    d "Who are you, really? What are you?"
    scene 2_s3 with dissolve
    scene 2_s10 with Dissolve(1.5)
    mcn "(What the hell do I tell this guy? This is clearly too important for him.)"
    mcn "(If I say I just woke up and got lucky, he'll think I'm a lunatic. If I claim credit, he might expect me to actually be a hero. Either way, I'm screwed.)"
    call screen scene2_choice1 with dissolve

    d "You're coming with me to Irda. The Queen will be extatic to hear this!"
    mcn "Irda? That's a city?"

    #choice2: Live the rest of your life as a hermit [End game]
    #mcn "Yeah, fuck that. I'm making the best out of this."
    #mcn "New world, new me."
    #perception "You head over the hills, away from the road, letting the wind carry the smell of wildflowers and damp soil into your lungs. The grass sways in waves, the sun warming your skin."
    #sensation "Each step feels lighter without the weight of expectations—just the sound of your bare feet brushing through the grass."
    #perception "Days blur into weeks. You fashion crude tools from stone and bone, learn where the berries grow sweetest, where the streams run cold and clear. Seasons turn, and your beard grows wild."
    #sensation "The summer sun burns your back as you fish in shallow water. The winter wind bites at your fingers as you huddle by a fire of crackling pine."
    #perception "Years pass in quiet solitude. You watch storms crawl across the horizon, see the first light of spring melt frost from the earth. Birds return each year like old friends."
    #sensation "Your muscles harden from chopping wood, your skin darkens under endless days of sun. Hunger is a stranger now; you know every edible root, every tree heavy with fruit."
    #perception "On your thirty-first year, spring comes late. The thawing river is swollen and loud with melted snow. You decide to cross it anyway, craving the berries on the far bank."
    #sensation "The water is colder than you expect, the current stronger. Stones shift under your feet."
    #perception "A branch bobs past you in the rushing water. The next moment, your footing slips. The world tilts, white water filling your ears."
    #sensation "The cold crushes your chest, steals the air from your lungs. Your hands grasp at nothing, your vision blurs."
    #perception "The sunlight above turns murky and distant. The current drags you into the dark."
    #perception "Everything fades, leaving only stillness and the slow embrace of the deep."
    
    call screen scene2_choice1 with dissolve

label scene2_choice1_truth:
    $ mc_truth = True
    scene 2_s3 with Dissolve(0.7)
    mcn "Honestly, I didn't do a thing. A falling cage took the ogre out—pure luck, really."
    play sound "sound_effects/karma_more.mp3" volume 0.2
    $ mc_karma += 1
    $ karma_more = True
    show screen stat_change with easeinright  
    scene 2_s11 with dissolve
    d "A cage? Oh, I guess that makes sense. These bastards tend to lock their victims in cages—sometimes for days, sometimes for weeks."
    d "The poor soul trapped inside must have rigged some kind of release. Or maybe the ogre itself triggered it."
    scene 2_s12 with dissolve
    d "However, it seems fate itself was on your side today. Some folks around here say that chance can mark a person as destined for greatness."
    hide screen stat_change with easeoutright
    $ karma_more = False
    scene 2_s5 with dissolve
    mcn "What are you on about? I just told you I didn't do anything."
    scene 2_s4 with dissolve
    d "Simply that sometimes, even luck can set you on the path to something extraordinary. The gods work in mysterious ways, my friend."
    d "A falling cage? At the exact moment an ogre was about to kill you? That's not luck. That's providence."
    scene 2_s5 with dissolve
    mcn "Look. I'm not a hero. I'm not 'destined' for anything. I'm just a guy who woke up in a field... naked and scared."
    scene 2_s4 with dissolve
    d "Don't worry, I believe you. No need to convince me. But I can't just leave you out here. Were you heading somewhere at least? A village? A town?"
    scene 2_s5 with dissolve
    mcn "No... not really. I don't even know where I am."
    scene 2_s12 with dissolve
    d "Then come with me! I'll take you to our city—Irda. It's not far, and you'll be safe there."
    scene 2_s13 with dissolve
    mcn "Thank you. I suppose there's nothing else for me to do here. Standing over a dead ogre isn't going to answer any of my questions."
    scene 2_s12 with dissolve
    stop music fadeout 1.0
    d "Very well!"
    scene 3_s1 with Fade(1.0,0.5,0.5)
    play music "2_opening_ride.mp3" fadein 3.0 loop
    d "Apologies for not fully introducing myself sooner—I'm Darius, Commander of the Guard for the city of Irda. And you?"

    $ name_valid = False
    while not name_valid:
        $ mcname = renpy.input("My name's ", length=32)
        $ mcname = mcname.strip() 
        if mcname:  
            $ name_valid = True
        else:
            "(Uhh... What was it again?)"

    $ persistent.name = mcname

    d "Good to meet you, [mc]! May I ask how you ended up here? *chuckles* It's not every day I find a naked stranger on the road."
    mc "Actually... I just woke up on that field about an hour ago. In the grass. With no idea how I got there."
    d "No memory of what occurred before? Forgive me, but you didn't just pass out drunk, were you?"
    d "It happens more often than you'd think—merchants celebrating a good sale, farmers at harvest festivals..."
    mc "No... My head hurts whenever I try to remember. It's like there's something there, fragments, but the moment I reach for them, they... slip away."
    d "I see. I hope you get your memories back soon. Head injuries can be tricky. I've seen soldiers take blows and forget their own names for weeks."
    scene 3_s2 with dissolve
    d "Do you at least remember where you hail from? I'm assuming you're not from around here, your accent is strange."
    mc "From—"
    scene 3_s2 with vpunch
    mc "Agh!"
    d "What's wrong? Were you hurt afterall?!"
    mc "Sorry, it's just my head..."
    d "Please, don't strain yourself further. It looks like you suffered an injury during your encounter."
    mc "Thank you... Uh... where exactly are we? I know you said Irda, but... I don't even know what continent this is."
    d "I didn't realize your amnesia was this bad. But to answer your question—we are on the continent of Illus."
    d "The kingdom of Irda is one of the larger powers in this region, bordered by mountains to the east and sea to the west."
    scene 3_s3 with dissolve
    d "And you're lucky I saw you. I rarely travel this path anymore due to the ogre. It's been terrorizing our outlying farms for months."
    mc "That ogre... Are they common in this world? Monsters like that?"
    d "In this world? *laughs* You talk like you came from the sky. But no, they usually keep to the wilds, deep in the mountains or the untamed forests, away from towns and cities."
    d "Well, except for the ogre that attacked you. The bastard had a nasty habit of attacking our farmers. A maneater."
    mc "What other... things roam around here? Just so I know what to expect."
    scene 3_s4 with dissolve
    d "You've got your share of orcs, goblins, forest folk, beastfolk, cave dwellers... and devils."
    d "Although, I've only heard tales of devils. Never seen one myself. They say they can take human form, so you never truly know who you're dealing with."
    mc "Devils?"
    d "Nothing to worry about. Just old stories... probably."
    d "Now, just a little farther. We're almost there!"
    scene 3_s5 with dissolve
    logic "Those ears—there's no mistaking it. An elf. And an archer, too. How stereotypical."
    mc "An elf!"
    d "Hmm? Got a thing for elves?"
    scene 3_s6 with dissolve
    mc "No, it's just... the first time I'm seeing one."
    mc "(Face to face anyways...)"
    d "First time, huh? You really aren't from around here. Elves are rare to see around these parts, but still... most {i}have{/i} seen one."
    d "You're quite the mystery, [mc]..."
    scene 3_s7 with dissolve
    d "Well, don't let their charm and beauty fool you. Elves have a way with words and with spells. Trouble follows them more often than not."
    mc "Hmm..."
    scene 3_s8 with Dissolve(2.0)
    d "And here we are! Irda. The greatest city in the northern kingdom!"
    stop music fadeout 2.0
    env "The shadow of a once-great city stands before you. The closer you get, the more an eerie quiet settles over you."
    jump scene04

label scene2_choice1_lie:
    $ mc_lied = True
    scene 2_s13 with Dissolve(0.7)
    mcn "Yes. Yes, I did. I killed it."
    play sound "sound_effects/karma_less.mp3" volume 0.2
    $ mc_karma -= 1
    $ karma_less = True
    show screen stat_change with easeinright  
    mcn "(Please don't let this blow up in my face... Please, please, please...)"
    scene 2_s12 with dissolve
    d "Ah! What a battle that must've been! An ogre, slain by a single man! I understand now why you're naked, such a fight would shred any ordinary garment."
    d "But worry not! I have spare clothes in my wagon. You can't very well meet her majesty looking like you just crawled out of a ditch."
    hide screen stat_change with easeoutright
    $ karma_more = False
    scene 2_s5 with Dissolve(0.4)
    mcn "Good to hear! I was starting to feel the breeze in uncomfortable places..."
    scene 2_s4 with Dissolve(0.4)
    d "Please, come with me to see our Queen. She'll be thrilled to meet a man of your caliber."
    d "An ogre slayer, here in our plains—it's been years since anyone managed such a feat."
    scene 2_s5 with Dissolve(0.4)
    jump scene2_lie_continue
    
label scene2_lie_continue:
    mcn "Queen?"
    mcn "...Well, I don't have anywhere else to go, so... lead the way."
    scene 2_s7 with Dissolve(0.4)
    d "Please, follow me! Unless, of course, there's something here you need to retrieve first? A weapon, a trophy of its head, perhaps?"
    d "Speaking of which, I don't see your sword? Or are you one of those magic users? You'd be the first I've met who kills ogres with spells."
    scene 2_s8 with Dissolve(0.4)
    mcn "(Magic?! This world has magic?!)"
    mcn "*ahem* My sword... broke. In the fight. It took everything I had to bring that thing down. I'm honestly surprised I'm still standing."
    scene 2_s7 with Dissolve(0.4)
    d "Ah, what a shame. A good blade, lost. Worry not—I'm certain her majesty will reward you with a new one fit for a hero."
    d "Whenever you're ready, I'll be waiting over there by the road. Take a moment to catch your breath, you have earned it."
    scene 2_s8 with Dissolve(0.4)
    scene 2_s9 with fade
    call screen interact_tutorial with dissolve
    $ interact_indicator = True
    call screen scene02_search with dissolve

label scene02_search_ogre:
    perception "The ogre's corpse sprawls across the mud, its massive frame marred by countless scars—testaments to battles long fought and lost. This beast has endured, survived... until now."
    call screen scene02_search with dissolve

label scene02_search_axe:
    mcn "(Firmly planted in the tree. No way I'm getting that out.)"
    call screen scene02_search with dissolve

label scene02_search_cage:
    mcn "(The cage that killed the ogre ... it fell from the tree. And there's a skeleton inside... poor guy.)"
    call screen scene02_search with dissolve

default persistent.name = "None"

label scene03:
    stop music fadeout 1.0
    mcn "Nothing useful here. Time to bounce."
    scene 3_s1 with wipeleft
    play music "2_opening_ride.mp3" fadein 3.0 loop
    d "Apologies for not fully introducing myself sooner—I'm Darius, Commander of the Guard for the city of Irda. And you?"
    
    $ name_valid = False
    while not name_valid:
        $ mcname = renpy.input("My name's ", length=32)
        $ mcname = mcname.strip() 
        if mcname:  
            $ name_valid = True
        else:
            "(Uhh... What was it again?)"
    
    $ persistent.name = mcname

    mc "My name's [mc]."
    d "Pleasure to meet you, [mc]! And where do you hail from? I'm assuming you're not from around here, your accent is strange."
    mc "From—"
    scene 3_s1 with vpunch
    mc "{i}Agh!{/i}"
    d "What's wrong? Are you hurt?!"
    mc "Sorry, it's just my head..."
    mc "For some reason, every time I try to think about home, it's like there's a wall blocking me..."
    scene 3_s2 with Dissolve(1.0)
    d "Please, don't strain yourself further. It looks like you suffered an injury during the fight."
    mc "Thank you... Uh... where exactly are we? I know you said Irda, but... I don't even know what continent this is."
    scene 3_s3 with Dissolve(1.0)
    d "I didn't realize your amnesia was this bad. But to answer your question—we are on the continent of Illus."
    d "The kingdom of Irda is one of the larger powers in this region, bordered by mountains to the east and sea to the west."
    mc "I see... (So my theory was correct.)"
    d "And you're lucky I saw you. I rarely travel this path anymore due to the ogre. It's been terrorizing our outlying farms for months."
    scene 3_s4 with Dissolve(1.0)
    mc "That ogre... Are they common in this world? Monsters like that?"
    d "In this world? *laughs* You talk like you came from the sky. But no, they usually keep to the wilds, deep in the mountains or the untamed forests, away from towns and cities."
    d "Well, except for the ogre that attacked you. The bastard had a nasty habit of attacking our farmers. A maneater."
    mc "What other... things roam around here? Just so I know what to expect."
    d "You've got your share of orcs, goblins, forest folk, beastfolk, cave dwellers... and devils."
    d "Although, I've only heard tales of devils. Never seen one myself. They say they can take human form, so you never truly know who you're dealing with."
    mc "Devils?"
    d "Nothing to worry about. Just old stories... probably."
    d "Now, just a little farther. We're almost there!"
    scene 3_s5 with dissolve
    logic "Those ears—there's no mistaking it. An elf. And an archer, too. How stereotypical."
    mc "An elf!"
    d "Hmm? Got a thing for elves?"
    scene 3_s6 with dissolve
    mc "No, it's just... the first time I'm seeing one."
    mc "(Face to face anyways...)"
    d "First time, huh? You really aren't from around here. Elves are rare to see around these parts, but still... most {i}have{/i} seen one."
    d "You're quite the mystery, [mc]..."
    scene 3_s7 with dissolve
    d "Well, don't let their charm and beauty fool you. Elves have a way with words and with spells. Trouble follows them more often than not."
    mc "Hmm..."
    scene 3_s8 with Dissolve(2.0)
    d "And here we are! Irda. The greatest city in the northern kingdom!"
    stop music fadeout 2.0
    env "The shadow of a once-great city stands before you. The closer you get, the more an eerie quiet settles over you."

label scene04:
    scene 4_s1 with Fade(0.5,1.0,0.5)
    play music "nature.mp3" fadein 1.0 loop
    d "Please wait here for a moment. I need to check in with the gate captain and see if the Queen is available. Shouldn't take long."
    scene 4_s2 with Dissolve(1.0)
    mc "..."
    scene 4_s24 with dissolve
    #mc looks around
    mc "(Only one guard? Either they're confident or desperate.)"
    scene 4_s25 with dissolve
    mc "(Hmm?)"
    scene 4_s26 with Dissolve(1.0)
    mc "(I swear I saw something watching me just now...)"
    #darius approaches
    #scene 4_s3 with Dissolve(0.4)
    if mc_lied:
        scene 4_s3 with Dissolve(1.0)
        d "I apologize, friend, but it seems her majesty isn't in the city today. She departed this morning with a small retinue."
        d "A shame. This news would surely ease her mind."
        scene 4_s4 with Dissolve(0.4)
        mc "Where'd she go?"
        scene 4_s3 with Dissolve(0.4)
        d "She traveled east to Nahraya, the desert city. There have been tensions along the border, she's hoping to smooth things over before they escalate into something worse."
        d "She should return by tomorrow, assuming the talks go well. You'll meet her then."
        scene 4_s5 with Dissolve(0.4)
        d "But worry not! I won't leave you without a place to sleep at least. I've already finished most of my work for the day, so I'll accompany you personally."
        d "Tell me, you don't have any coin on you at the moment, do you?"
        scene 4_s4 with Dissolve(0.4)
        mc "Coin? No, I didn't... I don't even have a tissue to my name."
        scene 4_s3 with Dissolve(0.4)
        d "Figured as much. Well, how about I get you a room in the brothel for tonight? It'll give you a place to rest and get your bearings."
        scene 4_s4 with Dissolve(0.4)
        mc "A brothel?!"
        scene 4_s3 with Dissolve(0.4)
        d "It's cheaper to rent a room there than a regular tavern, I hope you forgive me, but... we're in a bit of a rough period here. Coin is tight. Even for the Commander of the Guard."
        scene 4_s4 with Dissolve(0.4)
        mc "I get it. Beggars can't be choosers. But... why are you doing this for me?"
        scene 4_s3 with Dissolve(0.4)
        d "You rid us of that ogre, didn't you? I don't know where you're from, but in our city we treat those who help with respect. It's the least I can do."
        scene 4_s4 with Dissolve(0.4)
        mc "I see... Thank you, Darius."
        scene 4_s3 with Dissolve(0.4)
        d "Don't mention it."
        d "Come on. The brothel's not far, just past the market square."
    else:
        scene 4_s4 with Dissolve(0.4)
        mc "Something wrong?"
        scene 4_s3 with Dissolve(0.4)
        d "Not at all, friend. I just learned that Her Majesty isn't in the city today. She departed this morning for Nahraya on diplomatic mission to ease tensions along the border."
        d "She should return by tomorrow, but until then, the castle is effectively closed to visitors."
        scene 4_s4 with Dissolve(0.4)
        mc "Nahraya? Is that another city?"
        scene 4_s3 with Dissolve(0.4)
        d "Indeed. It's to the east, a city in the middle of the desert."
        d "Tell me, you don't have any coin on you at the moment, do you?"
        scene 4_s4 with Dissolve(0.4)
        mc "Coin? No, I don't... I don't even know what currency you use here."
        scene 4_s3 with Dissolve(0.4)
        d "Figured as much. Well, how about I get you a room in the brothel for tonight? It'll give you a place to rest and get your bearings."
        scene 4_s4 with Dissolve(0.4)
        mc "A brothel?!"
        scene 4_s3 with Dissolve(0.4)
        d "It's cheaper to rent a room there than a regular tavern, I hope you forgive me, but... we're in a bit of a rough period here. Coin is tight. Even for the Commander of the Guard."
        scene 4_s4 with Dissolve(0.4)
        mc "I get it. Beggars can't be choosers. But... why are you doing this for me? I'm just a stranger you found on the road."
        scene 4_s3 with Dissolve(0.4)
        d "I'm feeling rather generous today because of that ogre's death. We have been hunting that beast for months. Lost two good men to it."
        d "And today, I find it dead on the road, killed."
        d "Even if you weren't the one who swung the killing blow, you being there may have led to this outcome. I don't pretend to understand fate, but I do believe in giving credit where it's due."
        scene 4_s4 with Dissolve(0.4)
        mc "I see... Thank you, Darius. I wasn't expecting that."
        scene 4_s3 with Dissolve(0.4)
        d "Don't mention it. The world's a strange place. *chuckles* Sometimes luck is its own kind of strength."
        scene 4_s5 with Dissolve(0.4)
        d "Come on. The brothel's not far, just past the market square."

    scene 4_s4 with Dissolve(0.4)
    play music "city_ambience.mp3" fadein 2.0 loop
    scene 4_s1_2 with Fade(0.5,1.0,1.0)
    ""
    scene 4_s2_2 with Dissolve(0.7)
    kat_ "Darius! My man! The shield of Irda! The—"
    d "Hmm?"
    scene 4_s3_2 with dissolve
    d "{i}Tsk...{/i}Of all the people..."
    scene 4_s4_2 with dissolve
    kat_ "Hey, come on, aren't you glad to see me? It's been weeks! I've missed our little chats. The way you always look like you want to strangle me."
    scene 4_s5_2 with dissolve
    d "What do you want?"
    scene 4_s6_2 with dissolve
    kat_ "So cold! I'm wounded~ Can't a girl just invite her favorite commander to dinner without ulterior motives?"
    scene 4_s7_2 with dissolve
    d "Can't you see I'm busy?"
    scene 4_s8_2 with dissolve
    kat_ "...Right."
    d "Just spit it out. What's the problem this time?"
    scene 4_s9_2 with dissolve
    kat_ "Well, there's been a... teensy-weensy issue."
    scene 4_s10_2 with dissolve
    d "Of what kind?"
    scene 4_s11_2 with dissolve
    kat_ "Lord Reiner daughter's been kidnapped..."
    scene 4_s12_2 with vpunch
    d "What?!"
    scene 4_s12_2 with vpunch
    d "Where the {i}hell{/i} were you?! You were supposed to protect her!"
    scene 4_s13_2 with dissolve
    kat_ "Hey, don't pin this all on me! My partner was sick so I was working alone!"
    kat_ "One person can't guard an entire estate, Darius. You should've seen this coming! I told you we needed more people!"
    scene 4_s10_2 with dissolve
    d "Shut—"
    d "Ngh... Just leave. I'll handle it. *sigh* I knew I shouldn't have trusted some mercenary for this."
    scene 4_s11_2 with dissolve
    kat_ "Ouch..."
    kat_ "Anyway... uhh... what about me? Am I... you know..."
    scene 4_s10_2 with dissolve
    d "What about you?"
    scene 4_s11_2 with dissolve
    kat_ "Will I get in trouble for this? Like, real trouble? Dungeon trouble? 'Never see the sun again' trouble?"
    scene 4_s10_2 with dissolve
    d "I'll explain it to him. Just... go. Lay low for a day or two until I smooth this over."
    scene 4_s6_2 with dissolve
    kat_ "Aww! Thank you~! You're the best, Darius! I knew there was a soft heart under all that grump!"
    scene 4_s7_2 with dissolve
    d "..."
    impulse "Look at those tits... she's practically begging you to stare."
    call screen scene04_choice02 with dissolve

default kat_pervert = False
label scene04_choice02_peek:
    $ kat_pervert = True
    scene 4_s14_2 with dissolve
    perception "Your eyes linger on her chest—full, heavy, and slick with sweat. Her nipples press against the thin fabric of her armor, clearly outlined. It's hard not to notice."
    mc "(Wow... She's... uh. That's... that's a lot of confidence in that armor. Does it even help at all?)"
    mc "(I need to stop looking... I can't stop looking!)"
    kat_ "Eyes up here, pal."
    scene 4_s15_2 with dissolve
    mc "(Shit!)"
    kat_ "Damn, Darius. What were you doing with this pervert? Taking him to the dungeon, I assume?"
    scene 4_s16_2 with dissolve
    d "Just ignore her. She's trying to get a rise out of you."
    d "Come. We need to make a little detour first. Apparently there's been a kidnapping, and I have to clean up someone else's mess. Again."
    jump scene04_choice00_else

label scene04_choice02_intro:
    mc "Hi, I'm—"
    perception "Your voice cracks out, a dry, scratchy mess. Your throat feels like sandpaper."
    scene 4_s17_2 with dissolve
    kat_ "Save it. Unless it's work, then not interested."
    mc "..."
    scene 4_s18_2 with dissolve
    kat_ "Well, I'll be seeing you, Darius."
    scene 4_s16_2 with dissolve
    d "Unbelievable... The one person I needed to be competent, and she loses the most important charge in the city. "
    d "I apologize, friend. We need to make a little detour first. Apparently there's been a kidnapping, and I have to clean up someone else's mess. Again."
    jump scene04_choice00_else

label scene04_choice02_nothing:
    d "I apologize, friend. We need to make a little detour first. Apparently there's been a kidnapping, and I have to clean up someone else's mess. Again."
    jump scene04_choice00_else

label scene04_choice00_else:
    scene 4_s21_2 with fade
    mc "Where are we headed now?"
    d "I need to speak with Lord Reiner first. Shouldn't take long... I hope. If the Gods are merciful, he'll be too busy organizing search parties to spend much time shouting at me."
    mc "About his kidnapped daughter? Yeah, good luck with that... I can't imagine he's going to be in a good mood."
    d "{i}*sigh*{/i} Let's get this over with quick."
    scene 4_s19_2 with dissolve
    kat_ "{i}Hnnngggg~{/i} *giggles* {size=30}Good job, Alex. Now that the hard part's over, I might actually enjoy my day.{/size}"
    mc "That girl earlier... who was she? Besides a mercenary, I mean. She seemed... familiar with you."
    d "Her? A mercenary, nothing more. She's been in the city for a few years. Came from Nahraya, I think. Good with a blade."
    mc "That's... it? You don't seem too fond of her."
    d "I'm not. She's a troublemaker. If she wasn't one of the best swordhands in the city I would've—"
    scene 4_s20_2 with dissolve
    d "I wouldn't tolerate her. Simple as that."
    mc "Huh... Sounds personal. Did something happen between you two?"
    stop music fadeout 3.0
    d "It's not. Let's move. The guard post is just around the corner."
    play music "dungeon.mp3" fadein 3.0 loop
    scene 4_s1_3 with Fade(1.0,1.0,1.0)
    mc "Ugh... Smells awful. Do you actually work here?"
    d "{i}*chuckles*{/i} This isn't some noble's estate. Prisoners don't get scented oils and silk sheets. You get used to the smell after a while."
    d "My office is just up the stairs."
    scene 4_s2_3 with dissolve
    ruby_ "{i}Psst.{/i}"
    scene 4_s3_3 with dissolve
    mc "Huh?"
    scene 4_s4_3 with dissolve
    mc "Uh... What do you want?"
    d "Hmm?"
    stop music fadeout 3.0
    mc "Nothing... just thought I heard something."
    play music "fire.mp3" fadein 1.0 loop
    scene 4_s5_3 with dissolve
    d "Well, here we are. Home sweet home—for me, anyway. I spend more time in this office than I do in my own home."
    d "Go on, take a seat."
    scene 4_s13_3 with Dissolve(1.5)
    mc "What are you doing?"
    scene 4_s14_3 with dissolve
    d "Writing you a temporary citizenship card. You'll need it if you plan on going anywhere in the city."
    d "Now then, [mc]. Just a few quick questions, if you don't mind. Nothing too invasive, just what the clerks will need to process your application."
    scene 4_s13_3 with dissolve
    mc "Go ahead. I'll answer what I can."
    scene 4_s14_3 with dissolve
    d "Your name is [mc], correct? Or is that just what you go by? An alias, or a nickname?"
    scene 4_s13_3 with dissolve
    mc "*chuckles* It's my name."
    scene 4_s14_3 with dissolve
    d "Alright. And do you currently have an occupation, or remember having one? Before the memory loss, I mean."
    scene 4_s13_3 with dissolve
    mc "No... Nothing comes to mind. If I had a job before, it's gone now. Probably wasn't anything exciting anyway."
    scene 4_s14_3 with dissolve
    d "I see. What about marital status? Married? Single?"
    scene 4_s13_3 with dissolve
    call screen scene02_choice02 with dissolve

label scene02_choice02_op1:
    $ mc_marital = "single"
    mc "Single? Yeah. Definitely single."
    scene 4_s14_3 with dissolve
    d "Got it. *chuckles* Probably for the best, huh?"
    jump scene04_choice00_else2

label scene02_choice02_op2:
    $ mc_marital = "married"
    mc "Married? I... think so? Maybe? The word feels right, but I can't picture anyone."
    scene 4_s14_3 with dissolve
    d "You remember being married?"
    scene 4_s13_3 with dissolve
    mc "Well... no. Not really. I'm just helping you fill out the form. I don't actually know."
    scene 4_s14_3 with dissolve
    d "I see."
    jump scene04_choice00_else2

label scene02_choice02_op3:
    $ mc_marital = "divorced"
    mc "Divorced? That feels... maybe right? I honestly can't tell."
    scene 4_s14_3 with dissolve
    d "You remember being divorced but not why?"
    scene 4_s13_3 with dissolve
    mc "I don't remember anything. The word just popped into my head. Could be true, could be nonsense."
    d "Hmm..."
    jump scene04_choice00_else2

label scene04_choice00_else2:
    scene 4_s14_3 with dissolve
    d "Alright. And residency? Where were you living before... all this?"
    scene 4_s13_3 with dissolve
    mc "Uhh... Sorry, Darius. I've got nothing. Just the field I woke up in."
    scene 4_s14_3 with dissolve
    d "No recollection at all?"
    scene 4_s13_3 with dissolve
    mc "It's just... blank."
    scene 4_s14_3 with dissolve
    d "That's fine. We'll work with what we have. It wouldn't be the first time someone came to Irda wearing nothing."
    scene 4_s13_3 with dissolve
    scene 4_s15_3 with Dissolve(1.0)
    d "Here you go. Welcome to Irda, [mc]. You're now a temporary citizen of our fine city."
    mc "Thank you."
    scene 4_s7_3 with dissolve
    d "Remember, this is only temporary. You'll need to have it stamped and registered by the royal clerk to become an official citizen."
    scene 4_s6_3 with dissolve
    mc "Got it."
    scene 4_s7_3 with dissolve
    d "Good. Now... any questions for me? I imagine you've got plenty on your mind."
    scene 4_s6_3 with dissolve
    mc "So... this is where you keep prisoners? Your office is literally on the upper floor of a prison? Or a dungeon, as you call it."
    scene 4_s7_3 with dissolve
    d "Isn't it obvious? The cells are below, the administration is above. It means I can do my paperwork and keep an ear on the inmates at the same time."
    scene 4_s6_3 with dissolve
    mc "How many you got in here right now?"
    scene 4_s7_3 with dissolve
    d "Just two. A pickpocket who thought she could lift a nobleman's purse in broad daylight, and a debtor who couldn't pay his gambling tabs. Pretty quiet lately."
    $ scene04_choice05_talked = False
    d "It may be a while before Lord Reiner arrives. Is there anything else you'd like to know while we wait?"
    scene 4_s6_3 with dissolve
    mc "Actually, I've been wondering... if the ogre was such a threat to your farmers for months, why wasn't something done about it sooner? Anything?"
    scene 4_s7_3 with dissolve
    d "Well, there was a bounty. A substantial one. Fifty gold pieces, as I mentioned. The problem was that the reward never matched the risk."
    d "Seasoned guild members took one look at the casualty reports and laughed. Too much blood, too little coin."
    d "And considering it would require at least ten people, that comes to only five gold per person. Hardly worth the risk."
    scene 4_s6_3 with dissolve
    mc "And the rookies?"
    scene 4_s7_3 with dissolve
    d "Couldn't touch it. Guild rules. Eireen, the guild mistress is... protective. Some would say stubborn. She'd rather turn down crown coin than march green recruits to their deaths."
    scene 4_s6_3 with dissolve
    mc "Sounds like the court didn't press the issue very hard."
    scene 4_s7_3 with dissolve
    d "*chuckles* Let's just say the royal council and the adventurers' guild don't always see eye to eye. The ogre fell into the gap between them."
    d "Anything else on your mind?"
    scene 4_s6_3 with dissolve
    call screen scene04_choice05 with dissolve
    
label scene04_choice00_ask1:
    $ scene04_choice05_talked = True
    mc "This— the Queen, what's she like? You seem to hold her in pretty high regard."
    scene 4_s7_3 with dissolve
    d "Ah, Queen Hannah. The most respected ruler in Irda's history."
    d "And I don't say that as her Commander of the Guard, I say it as someone who's watched her lead this city through crisis after crisis with grace and steel in equal measure."
    d "She has high expectations, but she's fair to those who earn her trust."
    scene 4_s6_3 with dissolve
    mc "High expectations? What does that mean for someone like me?"
    scene 4_s12_3 with dissolve
    if mc_lied:
        d "Since you handled that ogre, she'll expect you to rise to similar challenges when needed."
        d "A man of your... capabilities doesn't get to rest on his laurels. Not in Irda. Not while there's work to be done."
        scene 4_s11_3 with dissolve
        mc "Wait, so she's going to send me out to fight ogres now?"
        scene 4_s7_3 with dissolve
        d "And who knows what else. Ogres, certainly. Perhaps goblin raiding parties."
        d "Think of it as an... opportunity. A chance to prove yourself and earn her majesty's favor."
        scene 4_s6_3 with dissolve
        mc "(Fuck...)"
        call screen scene04_choice05 with dissolve
    elif mc_truth:
        d "Don't worry, friend. Once I tell her you were lucky, I'm sure she won't send you to your death fighting ogres in her stead."
        d "Although, as I mentioned before, she does believe that even luck can set you on the path to something extraordinary."
        scene 4_s11_3 with dissolve
        mc "I hope you're right. I would really rather not go through that again."
        scene 4_s7_3 with dissolve
        d "{i}*laughs*{/i} I hear you."
        scene 4_s6_3 with dissolve
        call screen scene04_choice05 with dissolve

label scene04_choice00_ask2:
    $ scene04_choice05_talked = True
    mc "Back when we were on the carriage, you said something... harsh about that elf."
    scene 4_s8_3 with dissolve
    d "Ah... that."
    d "You're not wrong. My words were harsh."
    scene 4_s9_3 with dissolve
    mc "Do you have something against elves? Like, personally?"
    scene 4_s10_3 with dissolve
    d "Not elves, no. Not as a people. But the eastern tribes? The ones who raid our border settlements?"
    d "They've caused Irda more grief than I can count. Raids in the night. Ambushes on our supply caravans."
    scene 4_s9_3 with dissolve
    mc "So it's more about history than race?"
    scene 4_s8_3 with dissolve
    d "Indeed. War and blood and old grudges that should have died generations ago but somehow keep burning."
    d "History has a way of leaving scars. I try not to judge individuals... but habits die hard, you know?"
    scene 4_s9_3 with dissolve
    mc "I guess war doesn't bring out the best in anyone."
    scene 4_s8_3 with dissolve
    d "You said it, friend."
    scene 4_s9_3 with dissolve
    call screen scene04_choice05 with dissolve

label scene04_choice00_ask3:
    $ scene04_choice05_talked = True
    mc "I noticed the streets were... quieter than I expected. For a city this size, I mean. Where is everyone?"
    scene 4_s12_3 with dissolve
    d "Yes. Irda has struggled with population decline for years. And it's just... gotten worse."
    scene 4_s11_3 with dissolve
    mc "Why's that?"
    scene 4_s12_3 with dissolve
    d "Many of our men are stationed along trade routes or lost to border skirmishes. The western tribes, the southern raiders... they pick at our edges, slowly bleeding us dry."
    d "The young and able-bodied are conscripted, sent to the front, and not all of them come home. Those who do are often... changed."
    d "The elderly and women make up most of the population you see around."
    scene 4_s9_3 with dissolve
    mc "Has the Queen done anything to help change that?"
    scene 4_s8_3 with dissolve
    d "She has implemented policies to address it, but change takes time."
    scene 4_s9_3 with dissolve
    mc "Sounds like she has a lot on her plate."
    scene 4_s7_3 with dissolve
    d "Yet she never falters."
    scene 4_s6_3 with dissolve
    empathy "This man's devotion is unshakable. His eyes burn with a quiet, unwavering loyalty. He would charge into a storm of bullets... or arrows, in this case, if she so willed it."
    call screen scene04_choice05 with dissolve

label scene04_choice00_c:
    mc "That's all I need to know for now. Mind if I... take a look at the prisoners? While we wait?"
    scene 4_s7_3 with dissolve
    d "{i}*laughs*{/i} Curious, are you? All right, but don't get too close. These bastards bite."
    d "Especially her."
    scene 4_s6_3 with dissolve
    mc "Her?"
    scene 4_s7_3 with dissolve
    stop music fadeout 3.0
    d "You'll see."
    scene 4_s6_3 with dissolve
    play music "dungeon.mp3" fadein 1.0 loop
    scene 4_s1_4 with Fade(1.0,1.0,1.0)
    ""
    scene 4_s2_4 with Fade(0.5,0.5,0.5)
    mc "Is this the girl you were talking about?"
    d "Indeed. She's the pickpocket I told you about."
    d "She tried to steal a noble's purse in broad daylight, right in the middle of the market square."
    d "When he resisted, she pulled a knife. Not to kill, she claims. Just to scare him. But the court didn't see it that way."
    mc "How long's she gonna be locked up?"
    d "For as long as you and I draw breath, friend."
    mc "Forever?! Did she kill him?"
    scene 4_s3_4 with dissolve
    d "No. The man survived. Barely a scratch on him. But the man she tried to steal from holds a lot of power in this city."
    d "He has the ear of the council. He demanded she be made an example of, and the court... complied."
    mc "That isn't fair!"
    d "No. It isn't."
    mc "...What about the the oth—"
    scene 4_s4_4 with dissolve
    guard "Sir Darius! Lord Reiner's here to speak with you! He's waiting in the courtyard."
    scene 4_s41_4 with dissolve
    d "*sigh*... Well then, friend. I need to go. This conversation isn't going to be pleasant. Angry nobles are worse than angry ogres."
    mc "Of course. Take your time. I'll wait for you here."
    d "Thank you. And be careful. I'll be right back."
    scene 4_s5_4 with Fade(0.5,0.5,0.5)
    mc "(Now then...)"
    $ in_free_roam = True
    call screen free_roam_tutorial1 with dissolve
    call screen free_roam_tutorial2 with dissolve
    call screen free_roam_tutorial3 with dissolve
    call screen free_roam_tutorial4 with dissolve
    if mc_lied:
        $ mc_karma = 5
    $ current_objective = "I was thrown into this weird new world. From what \nI've seen so far, it's way less advanced than the one \nI came from. After an ogre attack, yeah a fucking \nogre!!! some guy named Darius helped me out and \nbrought me into this city. I got a few strange looks \nfrom people here. Yeah, sorry, but mr. reincarnated \nhero has arrived to save you all. That's how it usually \ngoes, right? Hopefully... And man, some of the girls \nhere are REALLY sexy. \n\nAnyway, I'm getting sidetracked. \nOne of the prisoners seems to want to talk. Might \nas well hear her out."

    if not karma_updated:
        $ karma_updated = True
        if mc_karma >= 100:
            $ mc_karma = 10
        elif mc_karma >= 90:
            $ mc_karma = 9
        elif mc_karma >= 80:
            $ mc_karma = 8
        elif mc_karma >= 70:
            $ mc_karma = 7
        elif mc_karma >= 60:
            $ mc_karma = 6
        elif mc_karma >= 50:
            $ mc_karma = 5
        elif mc_karma >= 40:
            $ mc_karma = 4
        elif mc_karma >= 30:
            $ mc_karma = 3
        elif mc_karma >= 20:
            $ mc_karma = 2
        elif mc_karma >= 10:
            $ mc_karma = 1
        else:
            $ mc_karma = 1
    if mc_karma > 10:
        $ mc_karma = 10
    if mc_karma < 1:
        $ mc_karma = 1
    call screen scene04_free_roam1 with dissolve

label scene04_free_roam1_right:
    if scene04_free_roam_coin:
        scene 4_s43_4 with dissolve
    else:
        scene 4_s7_4 with dissolve
    call screen scene04_free_roam3 with dissolve

label scene04_free_roam_coin:
    $ mc_coin += 1
    $ renpy.notify("You found 1 bronze coin!")
    play sound "sound_effects/coin_collect.mp3"
    $ scene04_free_roam_coin = False
    jump scene04_free_roam1_right

label scene04_free_roam3_down:
    scene 4_s5_4 with dissolve
    call screen scene04_free_roam1 with dissolve

label scene04_free_roam1_left:
    scene 4_s6_4 with dissolve
    call screen scene04_free_roam2 with dissolve

label scene04_free_roam4_right:
    if scene04_free_roam_poster:
        scene 4_s44_4 with dissolve
    else:
        scene 4_s42_4 with dissolve
    call screen scene04_free_roam6 with dissolve

label scene04_free_roam_poster:
    perception "A poster catches your eye—an illustration of a woman, scantily clad and posed suggestively. Whoever made this had a clear intent."
    $ persistent.reb_render1 = True
    play sound "sound_effects/render_unlock.mp3"
    $ renpy.notify("You unlocked a special render!")
    $ scene04_free_roam_poster = False
    jump scene04_free_roam4_right

label scene04_end_free_roam:
    ""

label scene04_free_roam1_up:
    scene 4_s8_4 with dissolve
    call screen scene04_free_roam4 with dissolve

label scene04_free_roam4_left:
    scene 4_s9_4 with dissolve
    call screen scene04_free_roam5 with dissolve

label scene04_free_roam4_up:
    mc "(I should talk to that girl.)"
    call screen scene04_free_roam4 with dissolve

label scene04_free_roam5_down:
    scene 4_s8_4 with dissolve
    call screen scene04_free_roam4 with dissolve

label scene04_free_raom_end0:
    call screen scene04_free_roam_end with dissolve
    call screen scene04_free_roam2 with dissolve

label scene04_free_roam_end:
    $ in_free_roam = False
    scene 4_s10_4 with Fade(1.0,1.0,1.0)
    mc "Hey, you called out to me earlier."
    scene 4_s11_4 with dissolve
    ruby_ "{i}Tch.{/i} Took your time getting over here..."
    ruby_ "But whatever. You listening? I need a favor."
    scene 4_s10_4 with dissolve
    mc "Uh... You want me to break you out?"
    scene 4_s11_4 with dissolve
    ruby_ "No, that's not what I mean."
    scene 4_s10_4 with dissolve
    mc "Then what do you want?"
    scene 4_s12_4 with dissolve
    ruby_ "My sister. She's out there, alone. No coin, no roof over her head—nothing. I need to know she's alive. That she's safe."
    scene 4_s13_4 with dissolve
    mc "I... why me?"
    scene 4_s12_4 with dissolve
    ruby_ "Because you're standing there and I'm here. And because you can."
    ruby_ "You also don't look like a noble's lapdog. And I've never seen you around here before. That means you're either new, or you don't answer to the bastards who run this place."
    ruby_ "Either way, that makes you my best damn option right now."
    ruby_ "I'll make it worth your time, whatever it takes. Just—please. She's all I've got left."
    scene 4_s13_4 with dissolve
    mc "Hold on... I already know why you're here, but can you tell me what happened from your perspective?"
    scene 4_s14_4 with dissolve
    ruby_ "That bastard who owned our place happened."
    ruby_ "After our father died, we scraped together what we could to rent a shitty little home. I promised I'd get the coin, but the moment he saw a chance to line his pockets, he threw us out on the street."
    scene 4_s15_4 with dissolve
    mc "And you went after him?"
    scene 4_s14_4 with dissolve
    ruby_ "Damn right, I did. I tried to steal from him, and now I'm in here while he's probably got a new tenant filling his purse."
    ruby_ "{i}*sigh*{/i} I don't give a shit about myself. But my sister... she's too innocent to be on her own. If he knew I was her only living relative, who knows what that bastard might do to her."
    scene 4_s15_4 with dissolve
    mc "Hmm..."
    call screen scene04_choice06 with dissolve

label scene04_choice07_tits:
    mc "Let me see your breasts."
    scene 4_s21_4 with dissolve
    ruby "Heh... I had a feeling you'd ask for something like that."
    scene 4_s22_4 with dissolve
    mc "Can't blame a man for asking that, right?"
    scene 4_s21_4 with dissolve
    ruby "Fine, you want a show, huh? Alright."
    scene 4_s23_4 with dissolve
    ""
    scene 4_s27_4 with dissolve
    ruby "Here."
    scene 4_s28_4 with dissolve
    mc "Not bad."
    ruby "I'd hope not. These are probably the nicest things in this shit ass dungeon."
    ruby "Well, had your fun? Or do you need a bit more to entertain you?"
    ruby "I can still go on... It's been a long fucking time since I had any fun."
    call screen scene04_choice08 with dissolve
    mc "I've had enough. Thanks, Ruby."
    scene 4_s21_4 with dissolve
    ruby "Huh? That's it?"
    scene 4_s22_4 with dissolve
    mc "Yup, I just wanted to see your breasts."
    scene 4_s21_4 with dissolve
    ruby "A-Alright...?"
    scene 4_s22_4 with dissolve
    mc "What's the matter?"
    scene 4_s21_4 with dissolve
    ruby "You've got a woman right here telling you she'll do {i}anything{/i}—hell, even suck you off—and you only wanted to see my breasts?"
    scene 4_s22_4 with dissolve
    mc "Yeah. Problem with that?"
    scene 4_s21_4 with dissolve
    ruby "*laughs* You're a strange man... but I like that."
    ruby "Thanks... uh—"
    scene 4_s22_4 with dissolve
    mc "It's [mc]."
    scene 4_s16_4 with Dissolve(1.0)
    ruby "Thanks, [mc]. I won't forget this. Not that there's much else to do in here anyway."
    scene 4_s17_4 with dissolve
    mc "I'll be seeing you, Ruby. Don't do anything stupid while you're in here."
    scene 4_s16_4 with dissolve
    ruby "Alright, mom. I'll try."
    scene 4_s17_4 with dissolve
    scene 4_s39_4 with Fade(0.5,1.0,0.5)
    d "Finished talking with her?"
    scene 4_s40_4 with dissolve
    mc "Mhm. She accepted it rather quickly."
    scene 4_s39_4 with dissolve
    d "What else can you do? It'll eat her up from the inside if she doesn't."
    d "Anyway, how are you holding up so far? Still can't remember anything?"
    scene 4_s40_4 with dissolve
    mc "No... And this weird feeling never left me since I woke up..."
    scene 4_s39_4 with dissolve
    d "You're just tired from all that walking. Come, let's get your a place to stay."
    scene 4_s40_4 with dissolve
    scene black with Fade(1.5,1.0,1.0)
    scene 4_s6 with dissolve
    play music "nature.mp3" fadein 1.0 loop
    d "Well, here we are..."  
    mc "This is the brothel?"  
    d "Indeed... Listen, I know you've been through a lot today. If you need time to think about everything, I won't push you."  
    d "But if you'd rather distract yourself, well... this place might help."  
    d "So, what do you say? Should I get you a room to rest, or do you want to... take your mind off things for a while?"
    call screen scene04_choice09 with dissolve
    mc "I think I'd rather just get some rest."  
    d "I understand. Come, I'll make sure you're settled in."
    $ mc_refused_diana = True  
    $ mc_went_rest_no_meet_diana = True
    jump scene06

label scene04_choice07_pussy:
    mc "Let me see your pussy."
    scene 4_s21_4 with dissolve
    ruby "Oh? I had a feeling you'd ask for something like that."
    scene 4_s22_4 with dissolve
    mc "Can't blame a man for asking that, right?"
    scene 4_s21_4 with dissolve
    ruby "Fine, you want a show, huh? Alright."
    scene 4_s24_4 with dissolve
    ""
    scene 4_s26_4 with dissolve
    ruby "Here."
    scene 4_s25_4 with dissolve
    mc "Damn, it's a jungle down there."
    ruby "Yeah, well... they don't exactly give me a sharp razor for... {i}reasons.{/i}"
    mc "That's fair."
    ruby "Well, had your fun? Or do you need a bit more to entertain you?"
    ruby "I can still go on... It's been a long fucking time since I had any fun."
    call screen scene04_choice08 with dissolve
    mc "I've had enough. Thanks, Ruby."
    scene 4_s21_4 with dissolve
    ruby "Huh? That's it?"
    scene 4_s22_4 with dissolve
    mc "Yup, I just wanted to see your pussy."
    scene 4_s21_4 with dissolve
    ruby "A-Alright...?"
    scene 4_s22_4 with dissolve
    mc "What's the matter?"
    scene 4_s21_4 with dissolve
    ruby "You've got a woman right here telling you she'll do {i}anything{/i}—hell, even suck you off—and you only wanted to see my pussy?"
    scene 4_s22_4 with dissolve
    mc "Yeah. Problem with that?"
    scene 4_s21_4 with dissolve
    ruby "*laughs* You're a strange man... but I like that."
    ruby "Thanks... uh—"
    scene 4_s22_4 with dissolve
    mc "It's [mc]."
    scene 4_s16_4 with Dissolve(1.0)
    ruby "Thanks, [mc]. I won't forget this. Not that there's much else to do in here anyway."
    scene 4_s17_4 with dissolve
    mc "I'll be seeing you, Ruby. Don't do anything stupid while you're in here."
    scene 4_s16_4 with dissolve
    ruby "Alright, mom. I'll try."
    scene 4_s17_4 with dissolve
    scene 4_s39_4 with Fade(0.5,1.0,0.5)
    d "Finished talking with her?"
    scene 4_s40_4 with dissolve
    mc "Mhm. She accepted it rather quickly."
    scene 4_s39_4 with dissolve
    d "What else can you do? It'll eat her up from the inside if she doesn't."
    d "Anyway, how are you holding up so far? Still can't remember anything?"
    scene 4_s40_4 with dissolve
    mc "No... And this weird feeling never left me since I woke up..."
    scene 4_s39_4 with dissolve
    d "You're just tired from all that walking. Come, let's get your a place to stay."
    scene 4_s40_4 with dissolve
    scene black with Fade(1.5,1.0,1.0)
    scene 4_s6 with dissolve
    play music "nature.mp3" fadein 1.0 loop
    d "Well, here we are..."  
    mc "This is the brothel?"  
    d "Indeed... Listen, I know you've been through a lot today. If you need time to think about everything, I won't push you."  
    d "But if you'd rather distract yourself, well... this place might help."  
    d "So, what do you say? Should I get you a room to rest, or do you want to... take your mind off things for a while?"
    call screen scene04_choice09 with dissolve
    mc "I think I'd rather just get some rest."  
    d "I understand. Come, I'll make sure you're settled in."
    $ mc_refused_diana = True  
    $ mc_went_rest_no_meet_diana = True
    jump scene06

label scene04_choice08_bj_nope:
    "You don't meet the requirements for this choice."
    call screen scene04_choice08 with dissolve
    

image ruby_bj1 = Movie(play="images/1_opening/scene04_4/ruby_bj1.webm", loop=True)
image ruby_bj2 = Movie(play="images/1_opening/scene04_4/ruby_bj2.webm", loop=True)
image ruby_bj3 = Movie(play="images/1_opening/scene04_4/ruby_bj3.webm", loop=True)
image ruby_bj4 = Movie(play="images/1_opening/scene04_4/ruby_bj4.webm", loop=True)

label scene04_choice08_bj:
    $ mcname = persistent.name
    if persistent.name == "None" or mcname == "None":
        while mcname == "None" or mcname == "":
            $ mcname = renpy.input("There was an issue with your name. Please rewrite your name:", length=32)
        $ persistent.name = mcname
    if not persistent.scene1_replay:
        $ persistent.scene1_replay = True
    $ mc_helped_ruby_after_sex2 = True
    $ mc_karma = 4
    mc "Yeah... I'm still not satisfied..."
    ruby "Of course not~"
    mc "On your knees, girl."
    ruby "Mmmm..."
    scene 4_s45_4 with Fade(0.5,0.5,0.5)
    ruby "You've got some nerve, you know that? But I guess I can respect a man who knows what he wants."
    scene 4_s47_4 with dissolve
    mc "Less talking, more sucking."
    scene 4_s46_4 with dissolve
    ruby "What the fuck?!"
    scene 4_s47_4 with dissolve
    mc "Something wrong?"
    scene 4_s46_4 with dissolve
    ruby "N-no... *gulp*"
    scene 4_s47_4 with dissolve
    stop music fadeout 3.0
    mc "Come on, you know what to do."
    play music "sex01.mp3" fadein 2.0 volume 0.2 loop
    show ruby_bj1 with dissolve
    mc "Fuck... You're too good at this."
    ruby "Shut up..."
    sensation "Her warm mouth engulfs your cock, the heat wrapping around you as her rough tongue glides along the underside."
    scene black with Dissolve(0.3)
    show ruby_bj2 with dissolve
    mc "Use your tongue more..."
    ruby "Mfhgmmm... {i}*gag*{/i} like this?!"
    sensation "She gets bolder, her tongue swirling, prodding, coaxing every reaction out of you."
    scene black with Dissolve(0.3)
    show ruby_bj3 with dissolve
    mc "Ah, fuck..."
    mc "That's it. Just a little longer..."
    scene black with Dissolve(0.3)
    show ruby_bj4 with dissolve
    ruby "{i}*gag* Mghhmm...{/i}"
    ruby "Do it... *gag* outside..."
    call screen scene04_choice08_2 with dissolve

label scene04_choice08_inside:
    mc "I'm cumming!"
    scene 4_s48_4 with vpunch
    play sound "se_sfx/blowjob/gag2.mp3" 
    show screen cum
    ruby "{i}Mhhmmmm!!{/i}"
    sensation "A shudder runs through you as you release, thick, hot streams of cum spilling into her mouth, coating her tongue."
    scene 4_s31_4 with vpunch
    play sound "se_sfx/blowjob/blowjob_cum1.mp3" 
    mc "{i}Hnggg!{/i}"
    hide screen cum
    perception "You grip the back of her head, holding her in place, making sure every last drop finds its way down her throat."
    ruby "*gag* Let go!"
    scene 4_s32_4 with fade
    ruby "{i}*cough* *cough*{/i}"
    $ mc_karma -= 1
    $ karma_less = True
    play sound "sound_effects/karma_less.mp3" volume 0.2
    show screen stat_change with easeinright 
    ruby "You sheriously ejaculated inshide my moush?!"
    mc "I thought you might be hungry."
    ruby "Shcrew you..."
    hide screen stat_change with easeoutright
    $ karma_less = False
    scene 4_s33_4 with dissolve
    ruby "{i}Ptoo.{/i}"
    mc "Hey, don't... Nevermind."
    scene black with fade
    ruby "Ah, shit! I got it your filthy seed on my breasts!"
    scene 4_s21_4 with dissolve
    ruby "So? Satisfied now or do you want to stick it in my ass too?"
    scene 4_s22_4 with dissolve
    mc "...I can?"
    scene 4_s21_4 with dissolve
    ruby "Don't push it. Well... maybe for another favor."
    scene 4_s22_4 with dissolve
    mc "I'll be seeing you, Ruby. Don't do anything stupid while you're in here."
    scene 4_s21_4 with dissolve
    ruby "Alright, mom. I'll try."
    $ renpy.end_replay()
    scene 4_s22_4 with dissolve
    scene 4_s39_4 with Fade(0.5,1.0,0.5)
    d "Finished talking with her?"
    scene 4_s40_4 with dissolve
    mc "Mhm. She accepted it rather quickly."
    scene 4_s39_4 with dissolve
    d "What else can you do? It'll eat her up from the inside if she doesn't."
    d "Anyway, how are you holding up so far? Still can't remember anything?"
    scene 4_s40_4 with dissolve
    mc "No... And this weird feeling never left me since I woke up..."
    scene 4_s39_4 with dissolve
    d "You're just tired from all that walking. Come, let's get your a place to stay."
    scene 4_s40_4 with dissolve
    scene black with Fade(1.5,1.0,1.0)
    scene 4_s6 with dissolve
    play music "nature.mp3" fadein 1.0 loop
    d "Well, here we are..."  
    mc "This is the brothel?"  
    d "Indeed... Listen, I know you've been through a lot today. If you need time to think about everything, I won't push you."  
    d "But if you'd rather distract yourself, well... this place might help."  
    d "So, what do you say? Should I get you a room to rest, or do you want to... take your mind off things for a while?"
    call screen scene04_choice09 with dissolve
    mc "I think I'd rather just get some rest."  
    d "I understand. Come, I'll make sure you're settled in."
    $ mc_refused_diana = True 
    $ mc_went_rest_no_meet_diana = True 
    jump scene06

label scene04_choice08_outside:
    mc "I'm cumming!"
    scene 4_s34_4 with vpunch
    show screen cum
    play sound "se_sfx/blowjob/facial1.mp3" 
    perception "Hot streams of cum shoot out and land on her face. She jolts with every spurt, yet makes no move to pull away."
    mc "{i}Hnggg!{/i}"
    scene 4_s35_4 with vpunch
    play sound "se_sfx/blowjob/facial2.mp3" 
    ruby "{i}Eww...{/i}"
    hide screen cum
    scene 4_s37_4 with fade
    ruby "Fucking hell... Just how much were you keeping in there?"
    scene 4_s38_4 with dissolve
    mc "I guess it's been a while, or maybe you're just that good."
    scene 4_s37_4 with dissolve
    ruby "*chuckles* Screw you..."
    ruby "So? Satisified now or do you want to stick it in my ass too?"
    scene 4_s38_4 with dissolve
    mc "...I can?"
    scene 4_s37_4 with dissolve
    ruby "Don't push it. Well... maybe for another favor."
    scene 4_s30_4 with Dissolve(1.0)
    mc "I'll be seeing you, Ruby. Don't do anything stupid while you're in here."
    scene 4_s29_4 with dissolve
    ruby "Alright, mom. I'll try."
    $ renpy.end_replay()
    scene 4_s30_4 with dissolve
    scene 4_s39_4 with Fade(0.5,1.0,0.5)
    d "Finished talking with her?"
    scene 4_s40_4 with dissolve
    mc "Mhm. She accepted it rather quickly."
    scene 4_s39_4 with dissolve
    d "What else can you do? It'll eat her up from the inside if she doesn't."
    d "Anyway, how are you holding up so far? Still can't remember anything?"
    scene 4_s40_4 with dissolve
    mc "No... And this weird feeling never left me since I woke up..."
    scene 4_s39_4 with dissolve
    d "You're just tired from all that walking. Come, let's get your a place to stay."
    scene 4_s40_4 with dissolve
    scene black with Fade(1.5,1.0,1.0)
    scene 4_s6 with dissolve
    play music "nature.mp3" fadein 1.0 loop
    d "Well, here we are..."  
    mc "This is the brothel?"  
    d "Indeed... Listen, I know you've been through a lot today. If you need time to think about everything, I won't push you."  
    d "But if you'd rather distract yourself, well... this place might help."  
    d "So, what do you say? Should I get you a room to rest, or do you want to... take your mind off things for a while?"
    call screen scene04_choice09 with dissolve
    mc "I think I'd rather just get some rest."  
    d "I understand. Come, I'll make sure you're settled in."
    $ mc_refused_diana = True  
    $ mc_went_rest_no_meet_diana = True
    jump scene06

label scene04_choice08_help_cum:
    stop music fadeout 3.0
    mc "Yup. I'll help."
    play music "dungeon.mp3" fadein 1.0 loop
    scene 4_s37_4 with dissolve
    ruby_ "Good... Just don't waste time. I can't stand thinking about what she's going through out there alone."
    scene 4_s38_4 with dissolve
    mc "Where can I find her?"
    scene 4_s37_4 with dissolve
    ruby_ "Southeast side of the market. She sells whatever scraps she can find—red dress, and a white scarf. You won't miss her."  
    scene 4_s38_4 with dissolve
    mc "(The market, huh? I guess I'll have to ask Darius for help.)"
    mc "I'll see what I can do."
    scene 4_s29_4 with fade
    ruby_ "...A-and listen—when you find her, don't tell her about me being in here. Just say Ruby's fine, out making coin."
    scene 4_s30_4 with dissolve
    mc "You want me to lie to her?"
    scene 4_s29_4 with dissolve
    ruby "I want her to have hope. Just tell her to find a woman named Cassandra—she helps the homeless. She'll know what it means."
    ruby "And please—don't tell anyone about this."  
    scene 4_s30_4 with dissolve
    mc "Got it."
    scene 4_s29_4 with dissolve
    ruby "Please. Promise me you'll do it?"
    scene 4_s30_4 with dissolve
    mc "I promise."
    jump scene04_choice08_help_continue

label scene04_choice08_help:
    mc "Yup. I'll help."
    scene 4_s11_4 with dissolve
    ruby_ "Good... Just don't waste time. I can't stand thinking about what she's going through out there alone."
    scene 4_s13_4 with dissolve
    mc "Where can I find her?"
    scene 4_s12_4 with dissolve
    ruby_ "Southeast side of the market. She sells whatever scraps she can find—red dress, and a white scarf. You won't miss her." 
    scene 4_s13_4 with dissolve    
    mc "(The market, huh? I guess I'll have to ask Darius for help.)" 
    mc "Got it. I'll see what I can do."
    scene 4_s16_4 with dissolve
    ruby_ "...A-and listen—when you find her, don't tell her about me being in here. Just say Ruby's fine, out making coin."
    scene 4_s17_4 with dissolve
    mc "You want me to lie to her?"
    scene 4_s16_4 with dissolve
    ruby "I want her to have hope. Just tell her to find a woman named Cassandra—she helps the homeless. She'll know what it means."
    ruby "And please—don't tell anyone about this."  
    scene 4_s17_4 with dissolve
    mc "Got it."
    scene 4_s16_4 with dissolve
    ruby "Please. Promise me you'll do it?"
    scene 4_s17_4 with dissolve
    mc "I promise."
    jump scene04_choice08_help_continue

label scene04_choice06_op2:
    $ mc_helped_ruby = True
    mc "That's awful. I'm sorry. I can't imagine being forced onto the streets like that."
    mc "I'll help you."
    scene 4_s16_4 with dissolve
    ruby_ "You will? Oh, thank you—thank you, thank you, thank you!"
    if mc_karma < 10:
        $ mc_karma += 1
    $ karma_more = True
    play sound "sound_effects/karma_more.mp3" volume 0.2
    show screen stat_change with easeinright 
    ruby_ "But please hurry. I can't bear the thought of her suffering any longer. I haven't seen her since they locked me away."
    scene 4_s17_4 with dissolve
    mc "Where can I find her?"
    scene 4_s16_4 with dissolve
    ruby_ "Southeast side of the market. She sells whatever scraps she can find—red dress, and a white scarf. You won't miss her." 
    hide screen stat_change with easeoutright
    $ karma_more = False
    scene 4_s17_4 with dissolve
    mc "(The market, huh? I guess I'll have to ask Darius for help.)"
    mc "Got it. I'll see what I can do."
    scene 4_s16_4 with dissolve
    ruby_ "Thank you... You have no idea how much this means to me. Every day away from her feels like a lifetime of regret."
    ruby_ "...A-And listen—when you find her, don't tell her about me being in here. Just say Ruby's fine, out making coin."
    scene 4_s17_4 with dissolve
    mc "You want me to lie to her?"
    scene 4_s16_4 with dissolve
    ruby "I want her to have hope. Just tell her to find a woman named Cassandra, she helps homeless people. She'll know what it means."
    ruby "And please don't tell anyone about this."  
    scene 4_s17_4 with dissolve
    mc "Why not?"
    scene 4_s16_4 with dissolve
    ruby "The guards may snitch if they knew I had a sister."
    scene 4_s17_4 with dissolve
    mc "I think Darius can be trusted, he helped me out when I was... naked and alone."
    scene 4_s16_4 with dissolve
    ruby "*laughs* Naked? What were you doing with that man?"
    scene 4_s17_4 with dissolve
    mc "It's complicated. Anyway, I got it."
    scene 4_s16_4 with dissolve
    ruby "Please. Promise me you'll do it?"
    scene 4_s17_4 with dissolve
    mc "I promise."
    jump scene04_choice08_help_continue

label scene04_choice08_help_continue:
    scene 4_s39_4 with Fade(1.0,1.0,1.0)
    d "Apologies for the wait. Shall we head out?"  
    scene 4_s40_4 with dissolve
    mc "Actually... would it be alright if we made a quick stop first? I need to help this girl out."  
    scene 4_s39_4 with dissolve 
    d "The prisoner? *chuckles* You're not planning on breaking her out, are you?"  
    scene 4_s40_4 with dissolve
    mc "No. She..."
    scene 4_s39_4 with dissolve 
    d "Tell me, I may be able to help. She's been wrongfully sentenced so this is the least I can do."
    scene 4_s40_4 with dissolve
    mc "You're a good man, Darius. Alright... I need to find her sister, she's supposedly at the market."
    scene 4_s39_4 with dissolve
    d "I see... Well, things have been rather quite recently and I'm free at the moment... Why not?"
    scene 4_s40_4 with dissolve
    mc "Thanks, I appreciate it."
    scene 4_s39_4 with dissolve
    d "Let's move."
    stop music fadeout 3.0
    scene 4_s40_4 with dissolve
    jump scene04_market

label scene04_choice06_op3:
    $ mc_didnt_help_ruby = True
    mc "Sorry but... I can't. It sounds too risky."
    scene 4_s20_4 with vpunch
    ruby_ "What?! Why!?"  
    play sound "sound_effects/karma_less.mp3" volume 0.2
    if mc_karma > 1:
        $ mc_karma -= 2
    $ karma_less = True
    show screen stat_change with easeinright
    scene 4_s19_4 with dissolve
    mc "I just don't want to get involved."  
    scene 4_s18_4 with dissolve
    ruby_ "Please, I'm begging you! I'll do anything—I just need to know if she's safe!"  
    hide screen stat_change with easeoutright
    $ karma_less = False
    ruby_ "Please... *sob*"  
    scene 4_s39_4 with Fade(1.0,1.0,2.0)
    d "Apologies for the wait. Shall we head out?" 
    scene 4_s40_4 with dissolve
    mc "Heading to that brothel now?" 
    scene 4_s39_4 with dissolve 
    d "You don't seem excited."
    scene 4_s40_4 with dissolve
    mc "I just never visited these kind of places before."
    scene 4_s39_4 with dissolve 
    d "Ah, I see. Well, if anything, we can just order some drinks."  
    scene 4_s40_4 with dissolve 
    mc "Alright, I'm pretty thirsty."  
    scene 4_s39_4 with dissolve 
    stop music fadeout 3.0
    d "*chuckles* Just follow me."  
    jump scene04_continue02

label scene04_market:
    scene 4_s1_5 with Fade(1.0,1.0,1.0)
    play music "market.mp3" fadein 1.0 loop
    d "Not even a day in the city and you're already lending a hand. I'm starting to see the makings of a hero."
    mc "A hero? Please... I was just being nice."
    d "Nice or not, it's still more than most would bother with."
    d "Anyway, this market is massive. Is there a part you're aiming for?"
    mc "Yeah. The southeastern side."
    d "The southeastern side? That's not the safest place... but alright, just stay close to me."  
    scene 4_s2_5 with Fade(0.5,0.5,0.5)
    ""
    scene 4_s3_5 with dissolve
    mc "(Shit. Where the hell is she?)"  
    d "Should we check the other alleys?"
    scene 4_s4_5 with dissolve  
    old_woman "Looking for someone, are we?"  
    stop music fadeout 3.0
    scene 4_s5_5 with dissolve
    mc "...Yes. Do you know what happened here? I'm looking for a girl."  
    play music "despair.mp3" fadein 1.0 loop
    scene 4_s6_5 with Dissolve(1.0)
    old_woman "Ahhh, her, you mean? Poor, poor thing..."  
    scene 4_s7_5 with dissolve
    mc "Did something happen to her?"  
    scene 4_s6_5 with dissolve
    old_woman "{i}Keh keh keh keh{/i}. Gone, she is. Taken in the dead of night... men, shadows, slavers, maybe. Dragged her off while she screamed and cried."  
    old_woman "And the people? They turned away. Not their problem, no. {i}Keh keh keh keh.{/i}"
    scene 4_s7_5 with dissolve
    mc "(Fuck. Ruby was right to worry. I promised her I'd check, and now...)"
    scene 4_s8_5 with Dissolve(1.0)
    d "Where did these men take her, ma'am? Any directions or descriptions you can give?"  
    scene 4_s6_5 with Dissolve(1.0)
    old_woman "Ohhh, far, far away by now. Another city, another Master, another life... If she's lucky."  
    scene 4_s10_5 with fade
    d "[mc], if she's outside the city walls, we're not likely to find her."
    scene 4_s9_5 with dissolve
    mc "There's got to be {i}something{/i} we can do for her. We can't just walk away."
    scene 4_s10_5 with dissolve
    d "{i}*sigh*{/i} I'm afraid not."  
    scene 4_s9_5 with dissolve
    mc "Why not?!" 
    scene 4_s10_5 with dissolve
    d "Slavery {i}is{/i} legal outside of our city. Irda abolished it within its walls decades ago, but the outlying territories?"
    d "They bow to no crown. If she had no family, no home, then she was a prime target. No one would stop them."
    scene 4_s9_5 with dissolve
    mc "{i}Tch.{/i} Goddammit..."  
    scene 4_s10_5 with dissolve
    d "I'm sorry it didn't end the way you hoped. But... if fate is kind, perhaps one day you'll cross paths again... and you could {i}buy{/i} her freedom."
    scene 4_s9_5 with dissolve
    mc "Let's just go."
    scene 4_s10_5 with dissolve
    d "Back to the dungeon?"
    scene 4_s9_5 with dissolve
    mc "She deserves to know."
    scene 4_s10_5 with dissolve
    d "...I see."
    scene 4_s7_5 with dissolve
    d "Thank you for the information, ma'am."  
    scene 4_s11_5 with dissolve
    old_woman "{i}Keh keh keh...{/i} Be careful, boy... kind hearts bleed the fastest."
    stop music fadeout 2.0
    scene 4_s1_3 with Fade(1.0,1.0,1.5)
    d "I'll wait for you in my office. Truth be told... I've never been good at explaining things like this. Giving comfort isn't my strong suit."
    mc "I understand. This one's on me."
    play music "dungeon.mp3" fadein 3.0 loop
    scene 4_s21_4 with Fade(1.0,1.0,1.0)
    ruby "You're back!"
    ruby "Did you find her?"
    scene 4_s22_4 with dissolve
    mc "About your sister..."
    scene 4_s11_4 with dissolve
    ruby "Tch... I don't like your tone already."
    ruby "Just tell me... is she alive?"
    scene 4_s10_4 with dissolve
    mc "She isn't dead."
    scene 4_s11_4 with dissolve
    ruby_ "*sigh* That's enough, then. Don't tell me anything more."
    ruby_ "If I start picturin' her situation, I won't be able to sleep at night."
    ruby_ "I taught her everything I could. Whatever's in front of her now... she'll survive it. She has to."
    scene 4_s10_4 with dissolve
    mc "Are you really satisfied with that?"
    scene 4_s21_4 with dissolve
    ruby "Call me Ruby. And yeah—I'll take what I can get. Don't worry, you've done more than enough for me."
    ruby "Now... for your reward. What'll it be? No coin, if that's what you're after, but... I'm sure we can find something else."
    scene 4_s22_4 with dissolve
    mc "Something else...?"
    scene 4_s21_4 with dissolve
    ruby "Oh, for fuck's sake. What else do you think I mean? Just say the word."
    scene 4_s22_4 with dissolve
    mc "Alright. Just confirming..."
    ruby "Heh~"
    call screen scene04_choice11 with dissolve
    mc "I don't need anything from you, Ruby."
    scene 4_s11_4 with dissolve
    ruby "Huh?"
    scene 4_s10_4 with dissolve
    mc "You just found out your sister's missing, and you still want to do this? Maybe take a moment to breathe first."
    ruby "..."
    scene 4_s21_4 with dissolve
    ruby "Are you homo?"
    scene 4_s22_4 with dissolve
    mc "W-What?"
    scene 4_s21_4 with dissolve
    ruby "You've got a woman right here telling you she'll do {i}anything{/i}—hell, even suck you off—and you're saying no?"
    scene 4_s22_4 with dissolve
    mc "Yeah. Problem with that?"
    scene 4_s21_4 with dissolve
    ruby "*laughs* You're a strange man... but I like that."
    play sound "sound_effects/karma_more.mp3" volume 0.2
    if mc_karma < 10:
        $ mc_karma += 1
    $ karma_more = True
    show screen stat_change with easeinright
    ruby "Thanks... uh—"
    scene 4_s22_4 with dissolve
    mc "It's [mc]."
    scene 4_s16_4 with Dissolve(1.0)
    hide screen stat_change with easeoutright
    $ karma_more = False
    ruby "Thanks, [mc]. I won't forget this. Not that there's much else to do in here anyway."
    scene 4_s17_4 with dissolve
    mc "I'll be seeing you, Ruby. Don't do anything stupid while you're in here."
    scene 4_s16_4 with dissolve
    ruby "Alright, mom. I'll try."
    scene 4_s17_4 with dissolve
    scene 4_s39_4 with Fade(0.5,1.0,0.5)
    d "Finished talking with her?"
    scene 4_s40_4 with dissolve
    mc "Mhm. She accepted it rather quickly."
    scene 4_s39_4 with dissolve
    d "What else can you do? It'll eat her up from the inside if she doesn't."
    d "Anyway, how are you holding up so far? Still can't remember anything?"
    scene 4_s40_4 with dissolve
    mc "No... And this weird feeling never left me since I woke up... Like I'm forgetting something really important. "
    scene 4_s39_4 with dissolve
    d "You're just tired from all that walking. Come, let's get you a place to stay."
    scene 4_s40_4 with dissolve
    scene black with Fade(1.5,1.0,1.0)
    scene 4_s6 with dissolve
    play music "nature.mp3" fadein 1.0 loop
    d "Well, here we are..."  
    mc "This is the brothel?"  
    d "Indeed. Not what you expected, hm? Vera runs a classy establishment. The scandal is all indoors."
    d "...Listen, I know you've been through a lot today. If you need time to think about everything, I won't push you."  
    d "But if you'd rather distract yourself, well... this place might help."  
    d "So, what do you say? Should I get you a room to rest, or do you want to... take your mind off things for a while?"
    call screen scene04_choice09 with dissolve
    mc "I think I'd rather just get some rest. It's been a long day."
    d "I understand. Come, I'll make sure you're settled in. I'll handle everything."
    $ mc_refused_diana = True  
    $ mc_went_rest_no_meet_diana = True
    jump scene06

label scene04_choice09_op2:
    mc "I'm fine. And honestly... a distraction wouldn't be so bad."  
    stop music fadeout 3.0 
    d "I won't judge. Sometimes, it's better to keep moving than to sit with your thoughts. Come on, I'll handle everything." 
    jump scene04_brothel

label scene04_continue02:
    scene 4_s6 with Fade(0.5,1.0,0.5)
    play music "nature.mp3" fadein 1.0 loop
    d "Phew! We're finally here."
    mc "This is the brothel?"  
    d "Yes. Today, we celebrate!"
    mc "Celebrate the ogre's death?"
    d "Indeed! The whole city will be ecstatic to hear the news once I'm allowed to share it. For now, we drink to your victory, my friend."
    mc "*chuckles* Alright then. Let's get it started."
    stop music fadeout 1.0 
    d "Come, friend! No sense wasting time."
    jump scene04_brothel

label scene04_brothel:
    play music "diana.mp3" fadein 3.0 loop
    #inside
    scene 4_s29 with Fade(1.0,1.0,1.0)
    d "Diana!"
    di "Coming~"
    scene 4_s28 with dissolve
    ""
    scene 4_s27 with dissolve
    di "Ah! How clumsy of me, please forgive me~"
    mc "..."
    scene 4_s8 with dissolve
    d "You had your turn asking questions back at the guard post. Now it's only fair I get mine."
    scene 4_s7 with dissolve
    mc "Alright. Go ahead."
    scene 4_s8 with dissolve
    d "Since you're indulging, I have to ask... what's your preference in a woman?"
    d "Don't be shy now. Every man has one."
    scene 4_s7 with dissolve
    call screen scene04_choice10 with dissolve

label scene04_choice10_ass:
    $ mc_liked_ass = True
    mc "I prefer the ass."
    scene 4_s8 with dissolve
    d "Ass, huh? Wait... do you mean the front part or the..."
    d "You know what, don't answer that."
    scene 4_s7 with dissolve
    jump scene04_brothel2
label scene04_choice10_tits:
    $ mc_liked_tits = True
    mc "What else but the breasts?"
    scene 4_s8 with dissolve
    d "*laughs* Now that's something we can both agree on! A man of taste! I knew there was a reason I liked you."
    scene 4_s7 with dissolve
    jump scene04_brothel2
label scene04_choice10_feet:
    $ mc_liked_feet = True
    mc "I like feet."
    scene 4_s9 with dissolve
    d "...I see."
    d "{i}*chuckles*{/i} You truly are full of surprises."
    scene 4_s10 with dissolve
    logic "There's nothing wrong with liking feet. Does he even know that the part of the brain responsible for recognizing genitals is right next to the one that processes feet?"
    jump scene04_brothel2
label scene04_choice10_personality:
    $ mc_liked_personality = True
    mc "Personality is the most important thing."
    scene 4_s10 with dissolve
    d "..."
    mc "What?"
    scene 4_s9 with dissolve
    d "It's always the ones who say that who care the least about it."
    scene 4_s10 with dissolve
    jump scene04_brothel2

label scene04_brothel2:
    d "Hmm..."
    scene 4_s9 with dissolve
    d "Hmm... Say, [mc]. You're clearly and outsider, maybe not even from this continent. But I get the feeling you're not in a hurry to find a way home."
    scene 4_s10 with dissolve
    mc "...Maybe I prefer being here."
    scene 4_s8 with dissolve
    d "Oh? That's not the answer I expected."
    scene 4_s7 with dissolve
    mc "What do you mean?"
    scene 4_s9 with dissolve
    d "Most people stuck in a place they don't belong spend every moment trying to leave. You, on the other hand... seem comfortable."
    scene 4_s7 with dissolve
    mc "Maybe {i}comfortable{/i} isn't the right word. But I'm not desperate to leave, either."
    mc "Wherever I came from... it doesn't feel like home anymore. Maybe it never did."
    scene 4_s9 with dissolve
    d "I see... Well, just know this city isn't as kind as it looks. It's beautiful, yes. And safer than most, but good fortune is hard to come by. Unless, of course, you fancy a career as a guard."
    scene 4_s7 with dissolve
    mc "Hmm... We'll see. I'm not ready to commit to a career path just yet."
    scene 4_s30 with dissolve
    if mc_lied:
        d "On the subject of that ogre... something about your story doesn't sit right with me."
        d "You're telling me a single outsider managed to fend off an ogre and walk away without a scratch? I may be a trusting man, but even I have my doubts."
        scene 4_s31 with dissolve
        mc "You think I'm lying?"
        scene 4_s32 with dissolve
        d "I don't know what to think, friend. But for now, I'll take you at your word. The Queen will be the judge."
        scene 4_s31 with dissolve
    if mc_truth:
        d "On the subject of that ogre... You're lucky to be standing here after an encounter like that. Not many live to tell the tale."
        scene 4_s31 with dissolve
        mc "Trust me, I thought I was done for."
        scene 4_s32 with dissolve
        d "And yet, you're here. Either the gods favor you... or you have a habit of surviving the impossible. Which is it?"
        scene 4_s31 with dissolve
        mc "*chuckles* A little bit of both, maybe."

    mc "What about you? Do you come to the brothel often? You seem to know the staff pretty well."
    scene 4_s30 with dissolve
    d "Believe it or not, this is my first time actually drinking here."
    scene 4_s7 with dissolve
    mc "First time, huh? That girl... Diana seemed to know your name."
    scene 4_s8 with dissolve
    d "{i}*chuckles*{/i} I'm not lying. And of course she knows who I am. I've hauled more drunkards out of here than I can count."
    d "The Commander of the Guard is a familiar face in every tavern and brothel in this city. Just not usually as a customer."
    scene 4_s7 with dissolve
    mc "I see."
    scene 4_s11 with dissolve
    d "Diana! Over here!"
    scene 4_s12 with dissolve
    di "Yes, sir Darius?"
    scene 4_s16 with dissolve
    d "Can you believe it, Diana? I managed to find you a customer at last. You should mark this day on your calendar."
    scene 4_s12 with dissolve
    di "Sir Darius, please... You'll give him the wrong impression."
    scene 4_s13 with dissolve
    d "Sorry, sorry. Take care of my friend here. He's earned it."
    mc "Darius?"
    scene 4_s20 with dissolve
    di "Follow me, darling. I'll show you to your room."
    scene 4_s19 with dissolve
    call screen scene04_choice03 with dissolve
    mc "Alright..."
    $ mc_refused_diana = False
    d "Well, friend, I'll leave you to it. Until tomorrow!"
    scene 4_s15 with dissolve
    mc "Take care, Darius. And uh... thanks. For everything."
    jump scene05_0

label scene05_0:
    $ mc_diana_talk_first = True
    scene 5_s38 with Fade(1.0,1.0,1.0)
    mc "Been working here long?"
    di "Hmm? Maybe. why do you ask?"
    di "Let me guess... you fell for me at first glance, and now you want to take me as your own! Sweep me away from this life of sin and labor!"
    mc "You've got quite the imagination."
    di "*chuckles* I wasn't. I only started about a month ago."
    stop music fadeout 2.0 
    scene 5_s42 with Fade(1.0,1.0,1.0)
    mc "So... what exactly are we doing here? I mean.... what's the... procedure?"
    play music "diana2.mp3" fadein 3.0 loop
    scene 5_s43 with dissolve
    di "Oh! First, we'll fill in our tax documents. Then we'll fix the broken roof tiles, there's a leak in the east wing that's been driving Vera mad."
    di "Then, if there's time, we'll organize the liquor racks."
    scene 5_s42 with dissolve
    mc "..."
    scene 5_s40 with dissolve
    di "What do you think, darling? Sound like a fun evening?"
    scene 5_s42 with dissolve
    mc "I think you're messing with me."
    scene 5_s43 with dissolve
    di "A little. I couldn't resist. Your face was so serious."
    di "*ahem* That aside—"
    di "I overheard your conversation with Sir Darius."
    scene 5_s42 with dissolve
    mc "Is that part of your job? Eavesdropping on customers?"
    scene 5_s43 with dissolve
    di "It is, actually. A good hostess knows what her guests need before they ask."
    di "So... you had a run-in with that ogre, huh? The one that's been terrorizing the farms for months? You're seriously lucky to get out alive. Most don't."
    di "Tell me—how did you manage it? I love these kinds of stories! The bloodier the better."
    scene 5_s42 with dissolve
    if mc_lied:
        mc "I managed to defeat it. Just me and the beast."
        scene 5_s40 with dissolve
        di "No way! On your own?!"
        scene 5_s39 with dissolve
        mc "Yes. If only you'd been there—our battle was legendary!"
        di "..."
        scene 5_s41 with dissolve
        di "*laughs* Pfft! No you didn't!"
        mc "...What's so funny?"
        scene 5_s40 with dissolve
        di "It's written all over you, dear. The way your eyes shifted. The way your voice got just a little too dramatic."
        di "{i}You're lying.{/i}"
        scene 5_s39 with dissolve
        mc "..."
        mc "Was I that obvious?"
        scene 5_s43 with dissolve
        di "Only to someone who's been trained to read people. Don't worry, your secret's safe with me."
        di "Trust me, I get it. You could get an audience with the Queen with that story. Maybe even get recruited into her service. A lie like that could change your life."
        scene 5_s42 with dissolve
        mc "Recruit me?"
        scene 5_s43 with dissolve
        di "Is that not your goal? Don't tell me you're planning on marrying the princess instead?"
        di "That's the other way to get close to the crown. Though it's a bit more complicated."
        scene 5_s42 with dissolve
        mc "Wait—you're saying I {i}can{/i} marry the princess? Like, that's an actual option?"
        scene 5_s43 with dissolve
        di "Well... it's a bit more complicated. She has to actually accept you first, but it's a start!"
        scene 5_s42 with dissolve
        mc "Hmm..."
        scene 5_s40 with dissolve
        di "Ooh~ What's going on in that head of yours?"
        scene 5_s39 with dissolve
        mc "Just... thinking about my options."
        scene 5_s43 with dissolve
        di "I still don't understand how it died. It {i}did{/i} die, right?"
        scene 5_s42 with dissolve
        mc "Yes. A cage... well, you already know—a cage fell on its head and killed it."
        scene 5_s43 with dissolve
        di "Oh..."
        scene 5_s42 with dissolve
        mc "Disappointed?"
        scene 5_s43 with dissolve
        di "Mhm. I was hoping for something more... extravagant."
        scene 5_s42 with dissolve
        mc "That's life."
        scene 5_s40 with dissolve
        di "*chuckles* Well, I suppose I've talked enough. Shall we?"
        scene 5_s39 with dissolve
    else:
        mc "It started attacking me, so I just kept running. Eventually it struck a tree, and that caused a cage to fall down."
        scene 5_s43 with dissolve
        di "A cage? Sorry, go on!"
        scene 5_s42 with dissolve
        mc "It was hanging from a branch. I think the ogre kept it there as a trophy or something."
        di "Mhm~?"
        mc "Anyway, it fell on its head and killed it. The sound its neck made... still gives me shivers."
        scene 5_s43 with dissolve
        di "Ouch. Deserved, I'd say. No one's mourning that thing."
        di "What happened after?"
        scene 5_s42 with dissolve
        mc "I... kept running until I found a road. I was terrified. I didn't stop until I was sure it wasn't getting up again."
        mc "That's where I met Darius. He found me naked on the side of the road"
        scene 5_s40 with dissolve
        di "I see. Then why's he treating you like his newlywed lover if you weren't the one to kill it?"
        scene 5_s39 with dissolve
        mc "He said something like, 'Even luck can set you on the road to greatness'. I think he believes the 'gods' put me there for a reason."
        scene 5_s40 with dissolve
        di "*laughs* That's Darius, alright. I think he's just trying to recruit you as a guard."
        scene 5_s39 with dissolve
        mc "Why would he do that?"
        scene 5_s40 with dissolve
        di "Why wouldn't he? You look like a capable young man—handsome, muscular... what's not to love?"
        di "*chuckles* Well, I suppose I've talked enough. Shall we?"
        scene 5_s39 with dissolve
    call screen scene05_choice05 with dissolve
        
label scene05_choice05_op2:
    mc "You're really beautiful, Diana."
    scene 5_s43 with dissolve
    di "Oh~! Trying to get me in the mood, are you? Flattery will get you everywhere, darling."
    scene 5_s42 with dissolve
    mc "Seriously. You're one of the most beautiful women I've ever seen. And I'm not just saying that because of... you know."
    scene 5_s40 with dissolve
    di "I see... thank you~ You're not too bad yourself, [mc]."
    scene 5_s39 with dissolve
    mc "This work you do... it's not permanent, is it?"
    scene 5_s43 with dissolve
    di "I mean... hopefully not. A girl's got dreams."
    scene 5_s42 with dissolve
    mc "Then maybe one day, I'll take you out of here. When things settle. When I figure out what I'm doing in this world."
    scene 5_s44 with dissolve
    di "Careful, [mc]... or I might actually start falling for you. *giggles* And that would be terribly inconvenient for both of us."
    di "*ahem* Now, just sit back and relax, darling. No more words."
    jump scene05

label scene05_choice05_op1:
    mc "Do your thing, girl."
    scene 5_s40 with dissolve
    di "*snickers* Straight to the point, fine by me."
    scene 5_s39 with dissolve
    jump scene05

label scene05_diana_scene:
    $ mc_replay_diana = True
    $ mc_diana_scene = True
    play music "night.mp3" fadein 1.5 volume 0.5 loop
    scene 5_s45 with Fade(1.0,1.0,2.0)
    di "Hahh... That was... ahh... wonderful, [mc]."
    di "Sorry for collapsing on you like this. I guess I'm just so tired from working all day."
    jump scene05_choice06_op1

label scene05_choice06_op2:
    scene 5_s47 with Dissolve(1.0)
    mc "You should leave, Diana. I think we're finished here."
    scene 5_s48 with dissolve
    di "Oh, come on... can't we at least cuddle first?"
    scene 5_s47 with dissolve
    mc "I'd rather sleep."
    scene 5_s48 with dissolve
    di "I... understand."
    scene 5_s34 with Fade(0.5,0.5,0.5)
    di "Sleep well, [mc]."
    scene 5_s33 with dissolve
    mc "You too, Diana."
    scene black with Fade(2.0,1.0,1.0)
    jump scene07

label scene05_choice06_op1:
    $ mc_harem_diana_chance = True
    scene 5_s46 with dissolve
    mc "It's all good. I don't mind it. I'm sure you're lighter than an ogre, anyway."
    scene 5_s45 with dissolve
    di "*giggles* Thank you~ I think this is the first time anyone's compared me favorably to a monster."
    di "*sigh* I can't believe it's been that long..."
    scene 5_s46 with dissolve
    mc "What do you mean?"
    scene 5_s45 with dissolve
    di "I mean... being with another man. Actually... being with someone."
    scene 5_s46 with dissolve
    mc "Seriously? Is that supposed to be a joke?"
    scene 5_s45 with dissolve
    di "I meant it."
    di "Most days I'm just pouring ale and cleaning tables. Vera hired me for exactly this, but it almost never happens."
    scene 5_s46 with dissolve
    mc "Are you saying you haven't been with anyone since you started working here?"
    scene 5_s45 with dissolve
    di "Pretty much. A whole month of smiling and flirting, and not a single dick in me."
    scene 5_s47 with dissolve
    mc "That's crazy. How come?"
    scene 5_s48 with dissolve
    di "Most of our customers are old men who can barely form a sentence through their drunken haze."
    di "They come here because the ale is cheap. The girls are just... decoration to them. And when they're sober enough, they just... *laughs* they treat me like their daughter."
    di "Some of them even band together to chase away any men who actually come here for my services."
    scene 5_s47 with dissolve
    mc "That's... oddly sweet. Your own personal army of drunk grandpas."
    scene 5_s48 with dissolve
    di "Oh, [mc]... but that's not how a brothel works. Vera is furious and threatens to fire me almost every day."
    scene 5_s47 with dissolve
    mc "Right..."
    scene 5_s48 with dissolve
    di "I'm an orphan, you know. Raised on these streets... and those old drunks are the closest thing I have to family."
    scene 5_s47 with dissolve
    mc "They really do care about you."
    scene 5_s48 with dissolve
    di "Maybe... but care can be a cage, too. I {i}chose{/i} to be here. I can't just keep leeching off people forever..."
    call screen scene05_choice07 with dissolve

label scene05_choice07_op1:
    scene 5_s47 with dissolve
    mc "That's not leeching, Diana. That's surviving."
    mc "You took the hand that was offered, and you're making the best of it. No shame in that."
    scene 5_s48 with dissolve
    di "*laughs* You make it sound noble. Like I'm some kind of hero for not starving to death."
    scene 5_s47 with dissolve
    mc "You're still standing, aren't you? Still dreaming. That's more than most can say."
    scene 5_s45 with Dissolve(1.5)
    di "...Thanks, [mc]. I didn't know I needed to hear that."
    scene 5_s46 with dissolve
    mc "Anytime. Now get some rest, you've earned it after your performance."
    scene black with Fade(2.0,1.0,1.0)
    if diana_game_start:
        jump scene07
    else:
        $ diana_game_start_end = True
        jump diana_sex_end

default diana_game_start_end = False
label scene05_choice07_op2:
    scene 5_s47 with dissolve
    mc "Sounds to me like you just need someone to keep you out of trouble."
    scene 5_s48 with dissolve
    di "Oh? And you're volunteering for the job?"
    scene 5_s47 with dissolve
    mc "Volunteering? No. I'm applying. Benefits include... this."
    scene 5_s50 with dissolve
    di "Hnn! [mc]?"
    scene 5_s49 with dissolve
    perception "You pull her closer to you, feeling her warmth seep into your skin, the scent of lilac lingering in her hair."
    scene 5_s50 with dissolve
    di "T-That's a bold application..."
    scene 5_s49 with dissolve
    mc "And I'm not leaving until I get approved. I'm very persistent."
    scene 5_s50 with dissolve
    di "Well, you {i}are{/i} persistent... and surprisingly warm."
    scene 5_s52 with dissolve
    di "Fine. Approved."
    scene 5_s51 with dissolve
    mc "Good. Now, sleep. Big day tomorrow."
    scene 5_s52 with dissolve
    di "Bossy already... And here I thought I was the one in charge."
    scene 5_s51 with dissolve
    mc "Goodnight, Diana."
    scene 5_s52 with dissolve
    di "Night, [mc]. Try to dream about me and not ogres~"
    scene 5_s51 with dissolve
    scene black with Fade(2.0,1.0,1.0)
    if diana_game_start:
        jump scene07
    else:
        $ diana_game_start_end = True
        jump diana_sex_end

label scene04_choice03_refuse:
    $ mc_refused_diana = True
    mc "Uh... I'd rather not right now. It's been a long day, and I'm not really... in the right headspace."  
    scene 4_s9 with dissolve
    d "Hmm? What's wrong? Were you tired after all? I thought a distraction might help, but if you'd rather not—"  
    scene 4_s10 with dissolve
    mc "I just need some time to gather my thoughts. After... well, all this."  
    scene 4_s9 with dissolve
    d "I see. I should have asked first. Forgive me, friend, I got carried away with the celebration."   
    scene 4_s21 with dissolve
    d "Sorry, Diana, maybe another time. You can keep the coin."
    scene 4_s22 with dissolve  
    di "Thank you, Sir."
    scene 4_s8 with dissolve
    d "Well, I'll leave you to rest. Until next time, [mc]!"
    scene 4_s7 with dissolve
    mc "Thanks, Darius. For everything."
    jump scene06

label scene05:
    $ mc_vera_diana_sex = True
    $ mcname = persistent.name
    if persistent.name == "None" or mcname == "None":
        while mcname == "None" or mcname == "":
            $ mcname = renpy.input("There was an issue with your name. Please rewrite your name:", length=32)
        $ persistent.name = mcname
    if not persistent.scene2_replay:
        $ persistent.scene2_replay = True
    
    stop music fadeout 3.0 
    scene 5_s1 with Fade(0.5,1.0,0.5)
    mc "..."
    scene 5_s2 with dissolve
    mc "(Holy shit!)"
    di "Like what you see?"
    scene 5_s3 with Dissolve(1.0)
    call screen scene05_choice01 with dissolve

label scene05_choice01_yes:
    mc "I do."
    scene 5_s4 with Dissolve(0.4)
    di "Go ahead then. They're all yours."
    scene 5_s5 with Dissolve(0.4)
    call screen interact_tutorial with dissolve 

label scene05_choice01_yes2:
    call screen scene05_is01 with dissolve

label scene05_is01_face:
    scene 5_s11 with dissolve
    ""
    play sound "se_sfx/blowjob/blowjob1.mp3"
    scene 5_s12 with vpunch
    mc "!!!"
    mc "(She's sucking my thumb off!)"
    scene 5_s5 with dissolve
    call screen scene05_is01 with dissolve

label scene05_is01_leftbob:
    scene 5_s6 with dissolve
    di "Mmn..."
    scene 5_s9 with dissolve
    di "Ah..."
    scene 5_s5 with dissolve
    call screen scene05_is01 with dissolve

label scene05_is01_rightbob:
    scene 5_s10 with dissolve
    di "Hnn..."
    scene 5_s5 with dissolve
    call screen scene05_is01 with dissolve

label scene05_is01_continue:
    scene 5_s4 with Dissolve(0.4)
    di "Mmm... Let's see what's down there~"
    jump scene05_hj

label scene05_choice01_small:
    mc "I prefer them a little bigger honestly."
    scene 5_s4 with Dissolve(0.4)
    di "Bigger?!"
    di "Can they even get bigger than this?"
    scene 5_s5 with Dissolve(0.4)
    mc "Oh, you bet."
    scene 5_s4 with Dissolve(0.4)
    di "These poor girls... I can't imagine the state of their backs."
    di "Give me your hand."
    scene 5_s7 with dissolve
    di "What do you think now?"
    scene 5_s8 with Dissolve(0.4)
    mc "I still need more convincing..."
    scene 5_s7 with Dissolve(0.4)
    di "{i}*laughs*{/i} Alright then."
    jump scene05_hj

label scene05_hj:
    scene 5_s13 with dissolve
    di "Let's see what's down there~"
    scene 5_s14 with dissolve
    di "{i}*gasp!*{/i}"
    scene 5_s15 with dissolve
    di "S-So big!"
    scene 5_s16 with dissolve
    di "You must be in pain, let me help."
    image diana_hj01 = Movie(play="images/1_opening/scene05/diana_hj01.webm", loop=True)
    image diana_hj01_faster = Movie(play="images/1_opening/scene05/diana_hj01_faster.webm", loop=True)
    image diana_hj02 = Movie(play="images/1_opening/scene05/diana_hj02.webm", loop=True)

    image diana_tj01 = Movie(play="images/1_opening/scene05/diana_tj01.webm", loop=True)
    image diana_tj01_faster = Movie(play="images/1_opening/scene05/diana_tj01_faster.webm", loop=True)
    image diana_tj02 = Movie(play="images/1_opening/scene05/diana_tj02.webm", loop=True)

    image diana_rtj01 = Movie(play="images/1_opening/scene05/diana_rtj01.webm", loop=True)
    image diana_rtj02 = Movie(play="images/1_opening/scene05/diana_rtj02.webm", loop=True)
    image diana_rtj02_faster = Movie(play="images/1_opening/scene05/diana_rtj02_faster.webm", loop=True)

    show diana_hj01 with dissolve
    ""
    #hide window
    scene black with Dissolve(0.3)
    hide screen delayed_sound_loop
    show screen delayed_sound_loop("se_sfx/rubbing3.mp3", delay=2.0)
    show diana_hj02 with dissolve
    di "Your balls look soo full..."
    jump scene05_tj
    $ renpy.pause(5.0, hard=True)
    
    #call screen scene05_choice02_hj with dissolve

default in_scene05 = False
label scene05_tj:
    hide screen delayed_sound_loop
    $ in_scene05 = True
    scene 5_s17 with fade
    di "How do you want to fuck me, baby? I'm all yours to use however you like for today~"
    di "If you intend on using my pussy then you must promise me not to ejaculate inside."
    scene 5_s35 with dissolve
    mc "I understand. Not the time for a baby, is it?"
    scene 5_s17 with dissolve
    di "Not yet~"
    scene 5_s35 with dissolve
    call screen scene05_choice03 with dissolve

label scene05_tj2:
    scene 5_s17 with dissolve
    di "Lie down~"
    scene 5_s18 with dissolve
    di "My breasts are {i}soo{/i} sweaty from working your dick. I'm gonna make you feel {i}really{/i} good."
    di "Threee, twoo, one..."
    scene 5_s27 with vpunch
    "*squich!*"
    mc "You're squeezing too hard!"
    scene 5_s19 with Dissolve(0.4)
    di "Look, your tip is barely showing."
    scene 5_s27 with dissolve
    show diana_tj01 with dissolve
    ""
    hide diana_tj01
    show diana_tj02 with dissolve
    di "How does it feel fucking my tits?"
    scene 5_s18 with dissolve
    di "Would you like getting your ass rimmed by a pretty girl?"
    scene 5_s28 with dissolve
    call screen scene04_choice04 with dissolve

label scene05_tj3:
    mc "Yes!"
    scene 5_s18 with dissolve
    di "Turn around and bend over for me then~"
    show diana_rtj01 with Fade(0.5,0.5,0.5)
    mc "Woah! This is new!"
    scene black with Dissolve(0.3)
    show diana_rtj02 with dissolve
    mc "Fuck... I can't hold it anymore!"
    di "It's fine, go ahead and ejaculate whenever~"
    $ is_diana_anim_tj1 = False
    $ is_diana_anim_tj2 = False
    $ is_diana_anim_tj3 = True
    call screen scene05_choice04 with dissolve

default scene05_no_rimming = False
label scene05_no_rimming:
    $ scene05_no_rimming = True
    $ is_diana_anim_tj1 = False
    $ is_diana_anim_tj2 = True
    $ is_diana_anim_tj3 = False
    mc "Hell no!"
    scene 5_s18 with dissolve
    di "No worries, I guess I'll have to keep my tongue in my mouth for now."
    show diana_tj01 with dissolve
    ""
    scene black with Dissolve(0.3)
    show diana_tj02 with dissolve
    di "Let's try something different. Get up, let me lay on the bed~"
    scene black with Fade(0.5,0.5,0.5)
    show is_diana_anim_tj2 with dissolve
    mc "Fuck... I can't hold it anymore!"
    di "It's fine, go ahead and ejaculate whenever~"
    call screen scene05_choice04 with dissolve


label scene05_choice02_tj_cum:
    if is_diana_anim_tj1:
        $ diana_cum_on_face = True
        perception"The friction of her soft, enveloping tits pushes you to the edge. Diana's eyes lock with yours, a sly, hungry smile playing on her lips as she feels your cock twitch and pulse between her mounds."
        scene black with Dissolve(0.3)
        show diana_tj01_faster with dissolve
        mc "I'm cumming!!!"
        scene 5_s19 with Dissolve(0.4)
        di "Let it all out! Cover my tits with your semen!"
        play sound "se_sfx/blowjob/facial2.mp3" 
        scene 5_s20 with vpunch
        mc "{i}Hngg!!{/i}"
        perception "Thick, hot ropes of cum shoot across her chest, painting her skin in glistening streaks. The first spurt lands on her face, the next splashes across her stiffened nipples, and the rest pools between her tits."
        play sound "se_sfx/blowjob/facial5.mp3" 
        scene 5_s21 with vpunch
        ""
        mc "Haah... Haah..."
        scene 5_s22 with dissolve
        di "Incredible! Did you save all that just for me?"
        scene 5_s24 with dissolve
        mc "Fuck... {i}you're{/i} incredible, Diana."
        scene 5_s23 with dissolve
        di "Me or my huge tits? Be more specific, darling."
        scene 5_s24 with dissolve
        mc "*chuckles* Both."
        scene 5_s23 with dissolve
        di "I bet you'll never find a woman with a bust this big."
        di "Not to mention the softness~ *giggles* You're fully justified in wanting to paint them with your stinky seed~"
        scene 5_s24 with dissolve
    elif is_diana_anim_tj2:
        mc "I'm cumming!!!"
        call screen is_diana_tj_choice03 with dissolve

    elif is_diana_anim_tj3:
        $ diana_cum_on_breasts = True
        sensation "The friction of her soft, enveloping tits is too much to bear, the warmth and pressure driving you closer and closer to the edge."
        mc "Ahh..."
        mc "I'm cumming!!!"
        di "Let it all out! Fill my tits with your semen!"
        play sound "se_sfx/blowjob/facial4.mp3" 
        scene 5_s29 with vpunch
        mc "{i}Hngg!!{/i}"
        sensation "Your cock throbs as the first spurt of cum shoots out, hot and thick. Her tongue darts around inside your anus encouraging you to release more."
        play sound "se_sfx/blowjob/facial2.mp3" 
        scene 5_s30 with vpunch
        ""
        mc "Haah... Haah..."
        scene 5_s32 with Fade(0.5,0.5,0.5)
        di "You ejaculated so much~! Was it because of my tongue?"
        scene 5_s31 with dissolve
        mc "You're suspiciously good at that..."
        scene 5_s32 with dissolve
        di "What? Finding your prostate and constantly teasing it with my wet tongue? Wasn't too hard."
        di "Maybe your little asshole is just that sensitive~"
        scene 5_s31 with dissolve
        mc "..."
        scene 5_s32 with dissolve
        di "Whatever it is—I'm ready for whenever you crave a tongue in your ass, darling."
        scene 5_s31 with dissolve
    $ renpy.end_replay()
    if not mc_diana_scene:
        jump scene05_diana_scene
    jump diana_sex_end

label after_diana_sex:
    $ is_diana_asex3_first = True
    $ is_diana_vsex3_first = True
    $ is_diana_anim_bj3_first = True
    scene black with Fade(0.5,1.0,0.5)
    if diana_cum_on_face:
        scene 5_s25 with dissolve
        di "You're welcome to come by anytime, big guy. I'll be here."
        scene 5_s26 with Dissolve(0.4)
        mc "The name's [mc]."
        mc "By the way, you still some of my cum on your face..."
        scene 5_s25 with Dissolve(0.4)
        di "Oh, I know~"
        di "Sleep well tonight."
    elif diana_cum_on_breasts:
        scene 5_s34 with dissolve
        di "You're welcome to come by anytime, big guy. I'll be here."
        scene 5_s33 with Dissolve(0.4)
        mc "The name's [mc]."
        mc "By the way, you still some of my cum on your breasts..."
        scene 5_s34 with Dissolve(0.4)
        di "Oh, I know~"
        di "Sleep well tonight."
    else:
        scene 5_s37 with dissolve
        di "You're welcome to come by anytime, big guy. I'll be here."
        scene 5_s36 with Dissolve(0.4)
        mc "The name's [mc]."
        scene 5_s37 with Dissolve(0.4)
        di "Pleasure to meet you, [mc]~"
        di "Sleep well tonight."
    scene black with Fade(0.5,0.5,0.5)
    $ diana_cum_on_face = False
    $ diana_cum_on_breasts = False

label scene06:
    scene 6_s1 with Fade(0.5,1.0,0.5)
    play music "night.mp3" fadein 2.0 volume 0.5 loop
    mc "..."
    if mc_helped_ruby:
        mc "(Damn... I really thought I'd find her. I don't know why I even care this much, but...)"
        mc "(Guess I just wanted to believe I could do something good right off the bat.)"
        mc "{i}*sigh*{/i} (Well, no use sulking now. Tomorrow's another day.)"
    mc "(Ogres, elves, medieval city, Darius...)"
    mc "(It's... it's real. I was actually transported to another world! I've only ever seen this happen on TV.)"
    mc "(But... why me? Did something happen back home? The last thing I remember is just... going to bed. Did I... die?)"
    scene 6_s2 with dissolve
    mc "(Ugh, my head still hurts...)"
    scene 6_s3 with dissolve
    mc "(The people that get transported to other worlds usually get some kind of overpowered skill, right?)"
    mc "(Let's see.)"
    scene 6_s4 with vpunch
    mc "Atomic slash!!!"
    scene 6_s5 with dissolve
    mc "..."
    scene 6_s6 with vpunch
    mc "Fireball!"
    scene 6_s7 with dissolve
    mc "Not magic, either..."
    scene 6_s11 with dissolve
    ""
    scene 6_s8 with dissolve
    mc "*inhale*"
    scene 6_s9 with vpunch
    mc "HAAAAAAAAAAAAAA!!!"
    if mc_went_rest_no_meet_diana:
        di "Sir? Is everything fine in there?"
        scene 6_s10 with dissolve
        mc "Ah, yeah! Sorry about the noise..."
        mc "*sigh* I'll figure it out tomorrow."
        di "May I come in?"
        mc "Sorry?"
        di "Can I come in? I want to talk to you."
        mc "Talk? About what?"
        di "There were rumours downstairs that you had a part in getting rid of the ogre."
        di "Please~?"
        call screen scene05_choice08 with dissolve
        mc "No. Please go away."
        di "I understand. I apologize for bothering you, sir."
        scene 6_s12 with Fade(0.5,1.0,0.5)
        mc "(Back in my world, I was... Maybe this world has something waiting for me. Something bigger.)"
        scene 6_s13 with dissolve
        stop music fadeout (3.0)
        mc "(I can't beleive I'm saying this but please don't make me wake up in my world. This... this might be my only chance to finally live my life how I wanted.)"
        scene black with Fade(0.5,1.0,0.5)
        jump scene07
    else:
        di "[mc], is everything fine in there?"
        scene 6_s10 with dissolve
        mc "Ah, yeah! Sorry about the noise..."
        mc "*sigh* I'll figure it out tomorrow."
        di "May I come in?"
        mc "Sorry?"
        di "Can I come in? I want to talk to you."
        mc "I already told you that I don't want your services, Diana."
        di "I know, I know. I just want to talk."
        di "Please~?"
        call screen scene05_choice08 with dissolve
        mc "My answer is still no, Diana."
        di "I understand. I apologize for bothering you, [mc]."
        scene 6_s12 with Fade(0.5,1.0,0.5)
        mc "(Back in my world, I was... Maybe this world has something waiting for me. Something bigger.)"
        scene 6_s13 with dissolve
        stop music fadeout (3.0)
        mc "(I can't beleive I'm saying this but please don't make me wake up in my world. This... this might be my only chance to finally live my life how I wanted.)"
        scene black with Fade(0.5,1.0,0.5)
        jump scene07

label scene05_choice08_op1:
    $ mc_diana_talk_first = True
    mc "Uhh... Fine. Come on in."
    scene 5_s42 with Fade(1.0,1.0,1.0)
    if mc_went_rest_no_meet_diana:
        mc "How did you hear that?"
        scene 5_s43 with dissolve
        d "News travel fast, sir. Especially in places like this."
        scene 5_s42 with dissolve
        mc "Drop the sir. It's [mc]."
        scene 5_s43 with dissolve
        d "*giggles* Very well, [mc]."
    else:
        mc "What is it?"
        scene 5_s43 with dissolve
        di "I overheard your conversation with Sir Darius."
        scene 5_s42 with dissolve
        mc "Is that part of your job?"
        scene 5_s43 with dissolve
        di "It is, actually. You had a run-in with that ogre, huh? You're seriously lucky to get out alive."
    di "Tell me—how did you manage it? I love these kinds of stories!"
    scene 5_s42 with dissolve
    if mc_lied:
        mc "I managed to defeat it."
        scene 5_s40 with dissolve
        di "No way! On your own?!"
        scene 5_s39 with dissolve
        mc "Yes. If only you'd been there—our battle was legendary!"
        di "..."
        scene 5_s41 with dissolve
        di "*laughs* Pfft! No you didn't!"
        mc "...What's so funny?"
        scene 5_s40 with dissolve
        di "It's written all over you, dear. {i}You're lying.{/i}"
        scene 5_s39 with dissolve
        mc "..."
        scene 5_s43 with dissolve
        di "Don't worry. Your secret's safe with me."
        di "Trust me, I get it. With that story, you could get an audience with the Queen—maybe even get recruited into her service."
        scene 5_s42 with dissolve
        mc "Recruit me?"
        scene 5_s43 with dissolve
        di "Isn't that your goal? Don't tell me you're planning on marrying the princess instead?"
        scene 5_s42 with dissolve
        mc "Wait—you're saying I {i}can{/i} marry the princess?"
        scene 5_s43 with dissolve
        di "Well... it's a bit more complicated. She has to actually accept you first, but it's a start!"
        scene 5_s42 with dissolve
        mc "Hmm..."
        scene 5_s40 with dissolve
        di "Ooh~ What's going on in that head of yours?"
        scene 5_s39 with dissolve
        mc "Don't worry about it."
        scene 5_s43 with dissolve
        di "I still don't understand how it died. It {i}did{/i} die, right?"
        scene 5_s42 with dissolve
        mc "Yes. A cage... well, you already know, a cage fell on its head and killed it."
        scene 5_s43 with dissolve
        di "Oh..."
        scene 5_s42 with dissolve
        mc "Disappointed?"
        scene 5_s43 with dissolve
        di "Mhm. I was hoping for something more... extravagant."
        scene 5_s42 with dissolve
        mc "That's life."
        scene 5_s40 with dissolve
        di "*chuckles* Well, I suppose I've talked enough. Please have a good night, [mc]."
        scene 5_s39 with dissolve
    else:
        mc "It started attacking me, so I just kept running. Eventually it struck a tree, and that caused a cage to fall down."
        scene 5_s43 with dissolve
        di "A cage? Sorry, go on!"
        scene 5_s42 with dissolve
        mc "It was hanging from a branch. I think the ogre kept it there as a trophy or something."
        di "Mhm~?"
        mc "Anyway, it fell on its head and killed it. The sound its neck made still gives me shivers."
        scene 5_s43 with dissolve
        di "Ouch. Deserved, I'd say."
        di "What happened after?"
        scene 5_s42 with dissolve
        mc "I... kept running until I found a road. That's where I met Darius."
        scene 5_s40 with dissolve
        di "I see. Then why's he treating you like his newlywed lover if you weren't the one to kill it?"
        scene 5_s39 with dissolve
        mc "He said something like, 'Even luck can set you on the road to greatness.'"
        scene 5_s40 with dissolve
        di "*laughs* That's Darius, alright. I think he's just trying to recruit you as a guard."
        scene 5_s39 with dissolve
        mc "Why would he do that?"
        scene 5_s40 with dissolve
        di "Why wouldn't he? You look like a capable young man—handsome, muscular... what's not to love?"
        di "*chuckles* Well, I suppose I've talked enough. Please have a good night, [mc]."
        scene 5_s39 with dissolve
    call screen scene05_choice10 with dissolve

label scene05_choice09_op3:
    mc "Good night, Diana."
    scene black with Fade(2.0,1.0,1.0)
    jump scene07

label scene05_choice10_op2:
    if mc_went_rest_no_meet_diana:
        mc "You're really beautiful, Diana. I kinda regret not sitting around with Darius a little."
    else:
        mc "You're really beautiful, Diana. I kinda regret not taking Darius's offer."
    scene 5_s43 with dissolve
    di "Oh~! Where did that come from?"
    scene 5_s42 with dissolve
    mc "Seriously, you're one of the most beautiful women I've ever seen."
    scene 5_s40 with dissolve
    di "I see... thank you~ You're not too bad yourself, [mc]"
    scene 5_s39 with dissolve
    mc "This work you do... it's not permanent, is it?"
    scene 5_s43 with dissolve
    di "I mean... hopefully not."
    scene 5_s42 with dissolve
    mc "Then maybe one day, I'll take you out of here."
    scene 5_s44 with dissolve
    di "C-Careful, [mc]... or I might actually start falling for you."
    scene 5_s42 with Dissolve(1.0)
    call screen scene05_choice09 with dissolve

label scene05_choice09_op1:
    mc "Are you free right now?"
    scene 5_s43 with dissolve
    di "O-Of course. Did you change your mind?"
    scene 5_s42 with dissolve
    mc "I did. I'd love to spend some time with you, Diana."
    scene 5_s40 with dissolve
    di "As you wish, darling. Just sit back and relax."
    scene 5_s39 with dissolve
    jump scene05

label scene05_choice09_op2:
    mc "Anyway... have a good night, Diana."
    scene 5_s43 with dissolve
    di "Aww... You're gonna leave me hanging after that?"
    scene 5_s42 with dissolve
    mc "*chuckles* Maybe another time."
    scene 5_s40 with dissolve
    di "Alright, I'll be waiting~"
    scene 5_s39 with dissolve
    scene black with Fade(1.5,1.0,0.5)
    jump scene07

label scene07:
    #play sound "sound_effects/knock.mp3" 
    "{i}*knock* *knock*{/i}"
    scene 7_s1 with Fade(0.5,1.0,0.5)
    play music "nature.mp3" fadein 3.0 loop
    mc "Ughh..."
    scene black with fade
    #play sound "sound_effects/knock.mp3" 
    "{i}*knock* *knock* *knock*{/i}"
    mc "..."
    mc "(Just five more minutes... please)."
    if not mc_refused_diana:
        di "Wake up, love."
        scene 7_s2 with fade
        mc "(Diana?)"
    alice_ "Wake up!"
    scene 7_s3 with vpunch
    mc "Huh!?"
    scene 7_s5 with Dissolve(0.4)
    alice_ "Rise and shine, sir! Kept me waiting long enough."
    scene 7_s4 with Dissolve(0.4)
    mc "What? Wh— who are you?"
    scene 7_s5 with Dissolve(0.4)
    alice "Lieutenant Alice of the Irda City Guard, second-in-command to Captain Darius, at your service! And you, sir, are late."
    scene 7_s4 with Dissolve(0.4)
    mc "Umm..."
    scene 7_s5 with Dissolve(0.4)
    alice "More importantly, you've been summoned for an audience with Her Majesty. Up you get. The Queen doesn't like to be kept waiting."
    scene 7_s4 with Dissolve(0.4)
    if mc_lied:
        mc "The Queen...? right, yeah."
        scene 7_s5 with Dissolve(0.4)
        alice "The whole city's buzzing about the mysterious stranger who killed the beast. Now get dressed. I'll be waiting outside."
        scene 7_s4 with Dissolve(0.4)
    else:
        mc "The Queen? What does she want from me?"
        scene 7_s5 with dissolve
        alice "Her Majesty heard the news and wants to meet you. Personally."
        scene 7_s4 with dissolve
        mc "But I didn't... *yawn* do anything..."
        scene 7_s5 with dissolve
        alice "Doesn't matter. Now up. I'll give you five minutes to make yourself presentable."
        scene 7_s4 with dissolve
    mc "Just... give me a second."
    scene 7_s7 with fade
    mc "*yawn*"

label scene07_free_roam:
    $ in_free_roam = True
    if not mc_refused_diana:
        $ current_objective = "According to the card I got yesterday, today should \nbe the 5th of Reed, 607 AE... Whatever the hell that \nmeans. Anyway, Darius did something I really didn't \nexpect, he took me to a BROTHEL. Seriously? \nI asked him what the hell we were doing there, and \nhe said he was just finding me a place to stay. \nYeah, sure. Still, it beats sleeping outside, so I can't \ncomplain. What really shocked me was that he paid a \nprostitute for me. Like it was the most normal \nthing in the world. I guess this kind of thing isn't \na big deal in their culture. \n\nWell... I took him up on it. I actually slept with her. \nShe was so fucking hot, her body was unreal, and \nthose breasts..."
    else:
        $ current_objective = "According to the card I got yesterday, today should \nbe the 5th of Reed, 607 AE... Whatever the hell that \nmeans. Anyway, Darius did something I really didn't \nexpect, he took me to a BROTHEL. Seriously? \nI asked him what the hell we were doing there, and \nhe said he was just finding me a place to stay. \nYeah, sure. Still, it beats sleeping outside, so I can't \ncomplain. What really shocked me was that he paid a \nprostitute for me. Like it was the most normal \nthing in the world. I guess this kind of thing isn't \na big deal in their culture. \n\nAnyway, I refused. Did he really think the first thing \nI'd do in this world is sleep with a prostitute? \nYeah, no thanks."
    scene 7_s17 with dissolve

    if not karma_updated:
        $ karma_updated = True
        if mc_karma >= 100:
            $ mc_karma = 10
        elif mc_karma >= 90:
            $ mc_karma = 9
        elif mc_karma >= 80:
            $ mc_karma = 8
        elif mc_karma >= 70:
            $ mc_karma = 7
        elif mc_karma >= 60:
            $ mc_karma = 6
        elif mc_karma >= 50:
            $ mc_karma = 5
        elif mc_karma >= 40:
            $ mc_karma = 4
        elif mc_karma >= 30:
            $ mc_karma = 3
        elif mc_karma >= 20:
            $ mc_karma = 2
        elif mc_karma >= 10:
            $ mc_karma = 1
        else:
            $ mc_karma = 1
    if mc_karma > 10:
        $ mc_karma = 10
    if mc_karma < 1:
        $ mc_karma = 1
    call screen scene07_free_roam1 with dissolve

label scene07_free_roam1_right:
    if scene07_free_roam_coin:
        scene 7_s18_2 with dissolve
    else:
        scene 7_s18 with dissolve
    call screen scene07_free_roam1_right with dissolve

label scene07_free_roam_coin:
    mc "(A silver coin? That's a lot, right? I really need to learn how currency works here.)"
    $ mc_coin += 10
    $ renpy.notify("You found 1 silver coin!")
    play sound "sound_effects/coin_collect.mp3"
    $ scene07_free_roam_coin = False
    jump scene07_free_roam1_right

label scene07_free_roam1_left:
    scene 7_s19 with dissolve
    call screen scene07_free_roam1_left with dissolve

label scene07_free_roam1_up:
    scene 7_s20 with dissolve
    call screen scene07_free_roam1_up with dissolve

label scene07_free_roam2_right:
    if scene07_free_roam_poster:
        scene 7_s21_2 with dissolve
    else:
        scene 7_s21 with dissolve
    call screen scene07_free_roam2_right with dissolve

label scene07_free_roam_poster:
    $ persistent.diana_render1 = True
    play sound "sound_effects/render_unlock.mp3"
    $ renpy.notify("You unlocked a special render!")
    $ scene07_free_roam_poster = False
    jump scene07_free_roam2_right

label scene07_free_roam_end:
    call screen scene07_free_roam_end with dissolve
    call screen scene07_free_roam1 with dissolve

label scene07_continue:
    $ in_free_roam = False
    scene black with Fade(0.5,1.0,0.5)
    play sound "sound_effects/door.mp3" 
    stop music fadeout (2.0)
    scene 7_s8 with fade
    play music "diana.mp3" fadein 3.0 loop
    ""
    scene 7_s9 with Dissolve(1.0)
    di "Good morning, Mr. Hero. Did you sleep well?"
    scene 7_s10 with Dissolve(0.4)
    mc "Hero?"
    if mc_went_rest_no_meet_diana and not mc_diana_talk_first:
        scene 7_s9 with Dissolve(0.4)
        di "Mhm. I overheard some of our customers talking about an ogre. Turns out someone got rid of it finally, and that someone is you."
        scene 7_s10 with Dissolve(0.4)
        mc "I see..."
        mc "The place seems... pretty lively. I hear shouting in the streets. And music, I think."
        scene 7_s9 with Dissolve(0.4)
        di "People are celebrating. Farmers were afraid to plant their crops. Children weren't allowed to play near the fields. And now... it's gone thanks to you."
        scene 7_s10 with Dissolve(0.4)
        mc "Was it really that big a deal?"
        scene 7_s11 with Dissolve(0.4)
        di "It certainly was, at least for the market district. You've made a lot of people very happy, [mc]. Even if you don't feel like a hero, they do."
        scene 7_s12 with Dissolve(0.4)
        di "And—oh! Let me introduce you to my boss, Vera. She owns this place. She's been dying to meet you ever since Darius told her who you were."
        scene 7_s13 with Dissolve(0.4)
        vera "Well, hello there!"
        scene 7_s14 with Dissolve(0.4)
        vera "My, my... aren't you a sight for red eyes!"
        vera "A real, live hero, right here in my establishment. I should charge extra for the privilege."
        mc "Ahaha... thanks."
        vera "I appreciate you helping us out. That ogre had my suppliers too scared to make deliveries."
        vera "Maybe next time you're here, you could... request Diana specifically? *scoff* She could definitely use the practice."
        scene 7_s15 with Dissolve(0.4)
        di "Ahaha! Thank you, Miss Vera, but I think [mc] is really busy right now."
        di "You'd better hurry, lieutenant Alice is waiting for you outside."
        scene 7_s16 with Dissolve(0.4)
        mc "Yeah, see you, Diana."
        stop music fadeout (3.0)

    elif mc_diana_talk_first:
        mc "Oh... yeah. The news finally got out, huh?"
        scene 7_s9 with dissolve
        di "Mhm. People are celebrating. Farmers were afraid to plant their crops. Children weren't allowed to play near the fields. And now... it's gone thanks to you."
        scene 7_s10 with Dissolve(0.4)
        mc "Was it really that big a deal?"
        scene 7_s11 with Dissolve(0.4)
        di "It certainly was, at least for the market district. You've made a lot of people very happy, [mc]. Even if you don't feel like a hero, they do."
        scene 7_s10 with dissolve
        mc "Well... you already know what truly happened, Diana."
        scene 7_s9 with dissolve
        di "I know, but why not take advantage of it?"
        di "The whole town recognizes you as a hero now. You could change your life if the Queen hires you under her service."
        scene 7_s10 with dissolve
        mc "I don't know..."
        scene 7_s9 with dissolve
        di "Don't like it, hm?"
        scene 7_s10 with dissolve
        mc "Fame can be a curse just as easily as it can be a blessing. I've read enough stories to know how that ends."
        scene 7_s9 with dissolve
        di "Still, I'm sure you can benefit from it somehow. Even if you don't want the spotlight, the Queen's favor is nothing to dismiss."
        scene 7_s12 with Dissolve(0.4)
        di "And—oh! Let me introduce you to my boss, Vera. She owns this place. She's been dying to meet you ever since Darius told her who you were."
        scene 7_s13 with Dissolve(0.4)
        vera "Well, hello there!"
        scene 7_s14 with Dissolve(0.4)
        vera "My, my... aren't you a sight for red eyes!"
        vera "A real, live hero, right here in my establishment. I should charge extra for the privilege."
        mc "Ahaha... thanks."
        if mc_vera_diana_sex:
            vera "I appreciate you finally requesting this girl. She's been here a month and hasn't so much as held a man's hand."
            vera "I was starting to think she'd taken a vow of chastity behind my back!"
        else:
            vera "I appreciate you helping us out. That ogre had my suppliers too scared to make deliveries."
            vera "Maybe next time you're here, you could... request Diana specifically? *scoff* She could definitely use the practice."
        scene 7_s15 with Dissolve(0.4)
        di "Ahaha! Thank you, Miss Vera, but I think [mc] is really busy right now."
        di "You'd better hurry, lieutenant Alice is waiting for you outside."
        scene 7_s16 with Dissolve(0.4)
        mc "Yeah, see you, Diana."
        stop music fadeout (3.0)

    else:
        scene 7_s9 with Dissolve(0.4)
        di "Mhm. I overheard you and Darius talking about an ogre. Turns out someone got rid of it finally, and that someone is you."
        scene 7_s10 with Dissolve(0.4)
        mc "I see..."
        mc "The place seems... pretty lively. I hear shouting in the streets. And music, I think."
        scene 7_s9 with Dissolve(0.4)
        di "Mhm. People are celebrating. Farmers were afraid to plant their crops. Children weren't allowed to play near the fields. And now... it's gone thanks to you."
        scene 7_s10 with Dissolve(0.4)
        mc "Was it really that big a deal?"
        scene 7_s11 with Dissolve(0.4)
        di "It certainly was, at least for the market district."
        scene 7_s12 with Dissolve(0.4)
        di "And—oh! Let me introduce you to my boss, Vera. She owns this place. She's been dying to meet you ever since Darius told her who you were."
        scene 7_s13 with Dissolve(0.4)
        vera "Well, hello there!"
        scene 7_s14 with Dissolve(0.4)
        vera "My, my... aren't you a sight for red eyes!"
        vera "A real, live hero, right here in my establishment. I should charge extra for the privilege."
        mc "Ahaha... thanks."
        if mc_vera_diana_sex:
            vera "I appreciate you finally requesting this girl. She's been here a month and hasn't so much as held a man's hand."
            vera "I was starting to think she'd taken a vow of chastity behind my back!"
        else:
            vera "I appreciate you helping us out. That ogre had my suppliers too scared to make deliveries."
            vera "Maybe next time you're here, you could... request Diana specifically? *scoff* She could definitely use the practice."
        scene 7_s15 with Dissolve(0.4)
        di "Ahaha! Thank you, Miss Vera, but I think [mc] is really busy right now."
        di "You'd better hurry, lieutenant Alice is waiting for you outside."
        scene 7_s16 with Dissolve(0.4)
        mc "Yeah, see you, Diana."
        stop music fadeout (3.0)

label scene08:
    $ in_scene05 = False
    scene 8_s2 with wipeleft
    play music "2_opening_ride.mp3" fadein 3.0  loop
    alice "Finally. I was starting to think you'd climbed out the window. Let's go."
    scene 8_s1 with dissolve
    mc "(Wow, she's really short... It's kinda cute.)"
    scene 8_s2 with dissolve
    alice "Something on your mind? You're staring."
    scene 8_s1 with dissolve
    mc "Before we go, can you tell me what the Queen wants from me? I'd like to know what I'm walking into."
    scene 8_s2 with dissolve
    alice "It's {i}Her Majesty{/i}, recruit. Don't forget it. You'll be addressing her directly soon enough, and she doesn't tolerate informality."
    scene 8_s1 with dissolve
    mc "Recruit? What's that supposed to mean?"
    scene 8_s2 with dissolve
    alice "Exactly what it sounds like. Her Majesty wants you to work for her—as a reward. A position in her service."
    scene 8_s1 with dissolve
    mc "...That's a reward? Darius told me that there was a fifty gold bounty on the ogre's head."
    scene 8_s2 with dissolve
    alice "Serving Her Majesty directly is the highest reward an outsider like you can get."
    alice "You'd have a roof over your head, food in your belly, and the protection of the crown. That's worth more than gold."
    scene 8_s1 with dissolve
    mc "I'm not so sure. I barely know this city. I don't even know if I'm staying."
    scene 8_s2 with dissolve
    alice "You look like a homeless man. You've got no coin, and you were sleeping in a dirty brothel because you couldn't afford an actual inn."
    scene 8_s1 with dissolve
    mc "...Ouch. That was unnecessary."
    scene 8_s2 with dissolve
    alice "This is your chance to actually become something. Now move."
    scene 8_s1 with dissolve
    mc "..."
    scene black with Fade(0.5,.0,0.5)
    scene 8_s4 with fade
    d "Ah, [mc]. Welcome. You clean up well... relatively speaking."
    mc "Hey, Darius. Thanks again for taking care of me yesterday."
    alice "Move it, recruit!"
    mc "(Sheesh...)"
    d "I'll take it from here, Lieutenant."
    d "Let's walk, [mc]. There are a few things we need to go over before you stand before Her Majesty."
    mc "You're getting me to the Queen?"
    d "Yes. But before we stand before Her Majesty, let's go over a few things."  
    mc "Hmm?"
    d "When we enter her presence, we bow. Show respect. Address her as 'Your Majesty'. No speaking unless she speaks to you first."  
    mc "Bow, respect, and don't talk back. Got it."  
    scene 8_s5 with Dissolve(1.0)
    d "You've shown good sense so far. But the throne room is different. The Queen is... formidable. Fair, but formidable."  
    mc "You worry too much. I know how to behave myself."
    d "*chuckles* Maybe. But I'd rather overprepare than be caught off guard."  
    mc "Fair enough."  
    d "Alright then. Let's get in, and remember: patience and humility go a long way. She values honesty above flattery, and competence above bravado."
    mc "I'm not big on humility, but I'll give it a shot."  
    stop music fadeout (3.0)
    d "Just keep your head straight. Let's go."  
    scene 8_s6 with fade
    play music "queen.mp3" fadein 2.0 loop
    perception "The throne room is... {i}quite large.{/i} The ceiling is so high you could fit a whole other building inside this one."
    logic "That's all you've got? 'Quite large'?"
    scene 8_s29 with dissolve
    perception "I can't think under pressure! Look at the princess, she's already glaring at you. The Queen is smiling, but that might be worse."
    scene 8_s7 with fade
    q "Welcome!"
    scene 8_s8 with dissolve
    m_ "..."
    scene 8_s9 with dissolve
    r_ "Hmph."
    d "{size=30}bow.{/size}"
    scene 8_s10 with dissolve
    mc "(Right!)"
    scene 8_s11 with dissolve
    d "Your Majesty."
    mc "(Hmm?)"
    scene 8_s12 with dissolve
    q "Ugh! That damn cat! Maia!"
    scene 8_s13 with dissolve
    m "Yes, Your Majesty! I-I'm so so sorry!"
    scene 8_s14 with dissolve
    m "I'll catch him, I swear. It's just that the kitchen door was open a-and—"
    scene 8_s30 with vpunch
    m "Blahh!"
    mc "Ouch..."
    scene 8_s15 with dissolve
    q "*sigh* Darius has informed me of your feat, [mc]."  
    scene 8_s15_2 with dissolve
    if mc_lied:
        mc "Thank yo—"
    elif mc_truth:
        mc "It was accidental—"
    d "*AHEM*"
    mc "..."
    scene 8_s15 with dissolve
    q "*chuckles* No need to be so tense, Darius."  
    scene 8_s15_2 with dissolve
    d "As you wish, Your Majesty."
    scene 8_s15 with dissolve
    q "[mc], I understand you've only just arrived, but I'm sure you can tell that our lands face great struggles."
    q "The ogre you vanquished was a particularly loathsome threat to our farmers on the eastern gate. With it gone, they may finally sleep in peace."
    q "You acted nobly, expecting no reward. That, in itself, is worthy of recognition."
    q "However, I do not believe in letting good deeds go unanswered."
    scene 8_s17 with dissolve
    r_ "Really, Mother? He doesn't deserve anything yet!"
    r_ "I mean, look at him! Do you really think he took down an ogre on his own? He must have used some trick."
    scene 8_s15_2 with dissolve
    if mc_truth:
        mc "Your... Majesty, if I may speak freely... you daughter, *ahem* princess is correct, it was pure accident. I didn't actually kill the ogre."
        mc "I just happened to be there."
        scene 8_s31 with dissolve
        r_ "Ha! See? I knew something was off here." 
        scene 8_s18 with dissolve
        q "Now, now, dear. That is no way to speak to our guest. Honesty is a virtue, not a failing. And you would do well to learn that appearances can be deceiving."
        scene 8_s15_2 with dissolve
        r "Hmph. Whatever."
        scene 8_s15 with dissolve
        q "Darius has already told me what transpired yesterday. I'm glad to hear you confirm it yourself."
        q "It takes courage to admit the truth when a lie would serve you better. That, too, is a kind of heroism." 
        q "However, I believe luck is a skill like any other."
        q "I have heard of some elven tribes using magic to increase certain probabilities. And I value men who can get things done—whatever their methods may be."  
        mc "(I don't know why I even try anymore... Everyone's determined to make me a hero whether I like it or not.)"  
    if mc_lied:
        mc "Thank you, Your Majesty. It was an honor to serve."  
        scene 8_s15 with dissolve
        q "Think nothing of it, hero. Bravery deserves recognition." 
        q "And yours was a rare stroke of fate indeed, to arrive in this land and almost immediately rid us of such a great menace."
        q "Tell me, how exactly did you accomplish it? An ogre is no small foe. What weapons or spells did you wield? What strategy did you employ?"
        scene 8_s15_2 with dissolve
        mc "(Shit... I wasn't prepared for this. What do I say? She'll see right through me if I keep lying!)"
        scene 8_s15 with dissolve
        d "*ahem* [mc] is quite modest, Your Majesty. When I found him, he was reluctant to even take credit."
        d "Surely there is no need to pry further."
        scene 8_s15_2 with dissolve
        q "Modest? A commendable trait, to be sure. So rare among warriors."
        q "Very well. I shall not press, though I do hope to hear the tale in full one day."
        scene 8_s15_2 with dissolve
        mc "(Thank you, Darius! I owe you for that one!)"

    scene 8_s16 with Dissolve(1.0)
    q "I am gifting you my finest maid, Maia. She will serve you, care for you, and provide you with companionship."
    q "You and Maia shall wed, breed, and give birth to strong children."
    q "Our population has declined for too long, and men of your skills are exactly what our kingdom requires."

    scene 8_s15_2 with Dissolve(1.0)
    mc "You're... wedding me?! To that... cat chasing lady?"
    scene 8_s15 with dissolve
    q "Indeed. A fortuitous meeting, wouldn't you say?"
    scene 8_s15_2 with dissolve
    mc "Can I at least talk to her first? See if she's actually okay with this?"
    scene 8_s15 with dissolve
    q "You may do as you wish with her. She is yours. Speak with her, court her, ignore her—the choice is yours. But the marriage will proceed."
    
    if mc_marital == "married":
        q "I know your citizenship card says you're already married, but Darius told me you claimed it was on the spur of the moment."
        q "Regardless, there's no shame in having more than one woman, it's even encouraged in times like these, I would say."
    
    scene 8_s15_2 with dissolve
    mc "(This world is insane. Completely, utterly insane.)"
    mc "Errm... Thank you, Your Majesty."
    mc "But how do you expect me to support her, Your Majesty? I have no place to live... or the coin."
    scene 8_s15 with dissolve
    q "We will speak of such matters later. For now, accept the gift in the spirit it was given."
    scene 8_s15_2 with dissolve
    mc "I don't wish to sound ungrateful, Your Majesty, but Darius also mentioned a bounty."
    scene 8_s15 with dissolve
    q "Your prize was marrying my maid, as well as the chance to work directly for me after the background assessment is done."
    scene 8_s15_2 with dissolve
    mc "(I see now why not many people took this task...)"
    mc "As you wish, Your Majesty."

    mc "Hmm..."
    scene 8_s9 with dissolve
    ""
    scene 8_s38 with dissolve
    logic "Stop. Whatever you're thinking, stop."
    scene 8_s39 with dissolve
    ""
    scene 8_s35 with dissolve
    mc "(Goddamnit! Calm down, buddy! She's {i}way{/i} out of your league. She's a princess and you're basically some random homeless guy!)"
    q "Something on your mind?"
    scene 8_s15_2 with dissolve
    impulse "This is it, son. It all comes down to this. You slay the bad guy, claim the glory, and then the princess is yours. The tale writes itself. It's destiny."
    desire "King [mc], ruler of Irda. It feels right."
    guilt "Do you even deserve this? You've done nothing to earn it. It's all luck. You've been skating by, but this ends now. You'll prove yourself or it all crumbles."
    mc "{i}Nghnnn...{/i}"
    scene 8_s15 with dissolve
    q "Is something the matter, [mc]? You seem to be lost in thought."
    scene 8_s15_2 with dissolve
    d "{size=30}[mc], What are you doing?! Answer the Queen!{/size}"
    call screen scene08_choice01 with dissolve

label scene08_choice01_op1_nope:
    $ mc_asked_wed_reb = False
    scene 8_s20 with vpunch
    mc "Ahhhhnmmmmghmm!!"
    perception "Your voice comes out as a mangled, incoherent mess."
    scene 8_s15 with dissolve
    q "Did you say something, [mc]? I didn't hear that. Could you repeat?"
    scene 8_s15_2 with dissolve
    mc "Mfhhmm!"
    impulse "Get yourself together. This is pathetic."
    r "Is he broken?"
    mc "(Fuck...)"
    d "Your Majesty, [mc] might be experiencing delayed shock from his encounter with the ogre."
    scene 8_s15 with dissolve
    q "I see... Well, hero. Please, take some time to rest and clean yourself up."
    q "I want you to meet me in my bedroom later for a private discussion."
    mc "Y-Your bedroom?"
    scene 8_s15_2 with dissolve
    d "I'll see to it, Your Majesty."
    scene 8_s36 with Fade(1.0,1.0,1.0)
    d "That went better than I expected. Well, except for the last part. Are you alright?"
    scene 8_s37 with dissolve
    mc "Sorry, I'd rather not talk about it... And come on, what were you so worried about?"
    scene 8_s36 with dissolve
    d "It's just... Her Majesty {i}is{/i} reasonable, but things can turn upside down very quickly."
    scene 8_s37 with dissolve
    mc "That so? I'll make sure not to anger her then."
    scene 8_s36 with dissolve
    d "That would be best. For both of us."
    d "Her Majesty ordered you to go to her bedroom. Come, I'll have a guard escort you to the baths first. You'll want to be presentable."
    scene 8_s37 with dissolve
    stop music fadeout (3.0)
    jump scene09_0

label scene08_choice01_op2:
    $ mc_asked_wed_reb = False
    mc "It's... nothing."
    scene 8_s15 with dissolve
    q "Hmm. Very well."
    q "And, hero, clean yourself up and meet me in my bedroom later for a private discussion."
    scene 8_s15_2 with dissolve
    mc "Uh... your bedroom?"
    scene 8_s15 with dissolve
    q "This meeting is concluded."
    scene 8_s36 with Fade(1.0,1.0,1.0)
    d "That went better than I expected."
    scene 8_s37 with dissolve
    mc "Come on, what were you so worried about?"
    scene 8_s36 with dissolve
    d "It's just... Her Majesty {i}is{/i} reasonable, but things can turn upside down very quickly."
    scene 8_s37 with dissolve
    mc "That so? I'll make sure not to anger her then."
    scene 8_s36 with dissolve
    d "That would be best. For both of us."
    d "Her Majesty ordered you to go to her bedroom. Come, I'll have a guard escort you to the baths first. You'll want to be presentable."
    scene 8_s37 with dissolve
    stop music fadeout (3.0)
    jump scene09_0
    
label scene09_0:
    scene 9_0_1 with Fade(1.5,1.0,1.0)
    ""
    m "M-Master?"
    scene 9_0_2 with Dissolve(1.0)
    play music "maia.mp3" fadein 3.0 loop
    mc "Oh, hey. You're Maia, right? Are you okay? Looked like you fell pretty hard back there."
    scene 9_0_3 with dissolve
    m "Y-Yes... Maia. I'm so sorry about that. Crumps... the cat, he's not supposed to be in there, I should have—"
    scene 9_0_2 with dissolve
    mc "Don't worry about it."
    mc "And did you hear what the Queen said? She's apparently... giving you to me. Makes it sound like you're just some piece of property."
    scene 9_0_3 with dissolve
    m "N-No! It's an honor to s-serve you, Master."
    scene 9_0_2 with dissolve
    mc "Really? You're just fine with this? Being handed off to a stranger?"
    scene 9_0_3 with dissolve
    m "Yes..."
    scene 9_0_2 with dissolve
    mc "You don't sound very sure."
    scene 9_0_3 with dissolve
    m "I-I just... didn't expect you to speak to me so casually. Most people... they don't. They only give me orders."
    scene 9_0_2 with dissolve
    mc "How else should I talk to you? I'd rather know you than {i}own{/i} you."
    scene 9_0_4 with dissolve
    m "T-That... would be nice."
    scene 9_0_5 with dissolve
    mc "Well, I already know your name... but what else should I know about you? What do you usually do around here?"
    scene 9_0_3 with dissolve
    m "I... I like to..."
    m "I'm sorry! I'm not very good at talking to strangers..."
    scene 9_0_2 with dissolve
    mc "Guess I'll have to stop being a stranger, then."
    m "Mmm..."
    mc "Heading somewhere?"
    scene 9_0_3 with dissolve
    m "I was about to bring some towels to the baths, actually. If the Queen's guests don't have towels, they complain, and then the steward yells, and then—"
    scene 9_0_2 with dissolve
    mc "Perfect timing. I was on my way there too."
    scene 9_0_4 with dissolve
    m "Then... shall I acompany you, Master?"
    scene 9_0_5 with dissolve
    mc "Only if you promise not to vanish before we can talk again. You look like you're about to crumple under the pressure."
    scene 9_0_4 with dissolve
    m "O-Of course. Shall we?"
    scene 9_0_5 with dissolve
    call screen scene09_choice0 with dissolve

label scene09_choice0_op1:
    mc "Careful, though. Walking into the baths together might give people the wrong idea."
    mc "The hero and the maid, sneaking off for a scandalous session..."
    scene 9_0_6 with dissolve
    m "A-Ah! I didn't... I mean—" 
    mc "Relax. I'm only teasing... unless you {i}want{/i} them to get the right idea."  
    scene 9_0_4 with dissolve
    m "*laughs* You're... different from what I expected, Master."
    scene 9_0_5 with dissolve
    mc "Different's not always bad."
    mc "Come on, let's get going."
    stop music fadeout 2.0 
    m "Mhmm~"  
    jump scene09_00

label scene09_choice0_op2:
    mc "Alright then, let's get moving before the water gets cold. Is it always this drafty?"  
    scene 9_0_4 with dissolve
    m "Of course, Master. The castle is old, the windows don't seal properly. In winter, we have to wear three layers just to serve breakfast."  
    m "And... thank you. F-For walking with me."
    scene 9_0_5 with dissolve
    stop music fadeout 2.0 
    mc "You're thanking me for that? Walking next to someone? That's a pretty low bar."
    jump scene09_00
 
label scene09_00:
    scene 9_00_1 with Fade(1.0,1.0,2.0)
    servant "Well, lookie here! Maia finally found herself a man! Never thought I'd see the day."
    servant "Doubt it. She's probably just escorting him. You know Maia, can't even make eye contact without tripping over her own feet."
    m "Ignore them... Please."
    servant "Oh? Not even going to defend yourself? Typical Maia. Quiet as a mouse. {i}Squeak, squeak.{/i}"
    servant "Maybe that's why the princess keeps her around. She's too timid to say no."
    servant "Or too useless to be trusted with real work."
    scene 9_00_3 with Dissolve(1.0)
    m "...Let's just keep going, Master. They're not worth it."
    scene 9_00_2 with dissolve
    servant "{i}Master{/i}? Pfft. Listen to her. Acting all fancy now."
    servant "Careful, Maia. If you mess this one up, you might not get another chance."
    scene 9_00_3 with dissolve
    m "Shut up..."
    scene 9_00_2 with dissolve
    call screen scene09_choice000 with dissolve 

default mc_stood_to_maia = False

label scene09_choice000_op1:
    $ mc_stood_to_maia = True
    scene 9_00_4 with Dissolve(1.0)
    mc "You two have something to say, say it to me."
    scene 9_00_5 with dissolve
    servant "W-We were just—"
    scene 9_00_4 with dissolve
    mc "Just what? Making yourselves feel better by picking on her?"
    mc "From where I'm standing, it looked like two people who should be working decided to spend their morning bullying a girl who's done nothing to them."
    scene 9_00_5 with dissolve
    servant "We didn't—"
    scene 9_00_4 with dissolve
    mc "Yeah, you did. And I'll tell you something for the future. The next time I hear either of you talk about her like that, we're going to have a serious problem."
    mc "And I don't mean a stern talking-to from whoever you answer to. I mean a problem with {i}me{/i}."
    servant "..."
    play sound "sound_effects/karma_more.mp3" volume 0.2
    if mc_karma < 10:
        $ mc_karma += 1
    $ karma_more = True
    show screen stat_change with easeinright
    m "Master... you didn't have to do that. They're just... they've always been like that."
    mc "Yeah, I did. I'm not letting anyone treat you like that."
    m "...Thank you."
    hide screen stat_change with easeoutright
    $ karma_more = False
    jump scene09

label scene09_choice000_op2:
    mc "Yeah, maybe you're right. I might've gotten the short end of the stick. The Queen didn't exactly give me a choice in the matter."
    servant "See? At least he's honest. Can't fault a man for speaking the truth."
    servant "Better watch your step, Maia. Sounds like your new 'master' isn't too impressed."
    m "..."
    mc "Relax. They were just having a bit of fun. No harm done."
    scene 9_00_3 with dissolve
    m "Maybe for them..."
    m "...I-I hope you don't think they're right, Master. I know I'm not... I'm not much. But I try. I try very hard."
    scene 9_00_2 with dissolve
    jump scene09

label scene09:
    scene 9_s1 with Fade(1.0,1.0,2.0)
    play music "bathhouse.mp3" fadein 2.0 loop
    ""
    scene 9_s2 with dissolve
    mc "This isn't too bad..."
    mc "(Maybe I {i}should{/i} take advantage of this.)"
    scene 9_s4 with Dissolve(1.0)
    mc "Are you just gonna stand there?"
    scene 9_s5 with dissolve
    m "I'm terribly sorry, Master. Is... is it alright if I join you?"
    m "I don't want to presume. I know some masters prefer to bathe alone, and if you'd rather I leave, I can just leave."
    scene 9_s6 with dissolve
    call screen scene09_choice00 with dissolve

label scene09_choice00_op1:
    mc "Of course it is! Get in."
    scene 9_s5 with dissolve
    m "As you wish, Master."
    scene 9_s6 with dissolve
    mc "And... you don't have to talk like that all the time. The whole 'Master' thing. I get that it's protocol, but when it's just us... [mc] is fine."
    scene 9_s5 with dissolve
    m "I-I couldn't possibly, Her Majesty would get angry at me..."
    scene 9_s6 with dissolve
    if mc_stood_to_maia:
        scene 9_s10 with Fade(1.0,1.0,1.0)
        m "Thank you for standing up for me back there, Master."
        m "No one's ever... I mean, people usually just ignore it. Or laugh."
        scene 9_s12 with dissolve
        mc "No problem. Is that a normal thing around here? Maids bullying each other?"
        scene 9_s10 with dissolve
        m "Not really... they mostly target me. The others get along fine. It's just... when I'm around..."
        scene 9_s12 with dissolve
        mc "Just you? Why? What did you ever do to them? Don't tell me you're secretly a menace..."
        scene 9_s10 with dissolve
        m "*giggles* B-Because I'm the princess's favorite! She's always requesting me for her personal errands."
        scene 9_s12 with dissolve
        mc "Ah, I see. Jealous brats. They can't take it out on the princess, so they take it out on you."
        scene 9_s11 with dissolve
        m "Mhm~"
        scene 9_s12 with dissolve
        mc "So? How's a pretty girl like you end up here?"
        scene 9_s10 with Dissolve(0.4)
        m "P-Pretty? Uhm... The princess, she took me in when I was young."
    else:
        scene 9_s9 with Fade(1.0,1.0,1.0)
        m "Umm... Master? Did you really mean it, back there? What you said to those servants?"
        scene 9_s7 with dissolve
        mc "Mean what?"
        scene 9_s9 with dissolve
        m "You said you 'might've gotten the short end of the stick.'"
        scene 9_s7 with dissolve
        mc "Ah... don't let it get to you. I was just playing along with them."
        mc "Sometimes it's easier to say what people want to hear than to start a fight."
        scene 9_s15 with dissolve
        m "Mmm..."
        scene 9_s7 with dissolve
        mc "Come on. You're not actually mad about that, are you?"
        scene 9_s9 with dissolve
        m "I-It's fine, Master... I understand. I'm not... I know I'm not much. You don't have to pretend."
        $ maia_love -= 10
        scene 9_s7 with Dissolve(0.4)
        mc "So? How's a pretty girl like you end up here?"
        scene 9_s10 with Dissolve(0.4)
        m "Uhm... The princess, she took me in when I was young."

    scene 9_s12 with Dissolve(0.4)
    mc "Do you mean the blond one, or is there another princess? Because she didn't seem like the kind type to me."
    scene 9_s10 with dissolve
    m "Princess Rebecca is very kind, Master! She always looks out for me. She just doesn't trust people easily."
    scene 9_s12 with dissolve
    mc "That so? Alright, I'll take your word for it. You know her better than I do."
    scene 9_s10 with dissolve
    m "W-Where will we live, Master?"
    scene 9_s12 with dissolve
    mc "Ah... well... That's a good question."
    scene 9_s10 with dissolve
    m "I hope it isn't too far away... I really want to keep seeing the princess."
    m "She gets lonely without me."
    scene 9_s12 with dissolve
    mc "I'm sure I'll figure that out soon enough. For now, let's just... enjoy the hot water. We can worry about housing later."
    jump scene09_choice01_nothing

label scene09_choice00_op2:
    $ mc_talk_maia_home = True
    mc "You can wait for me outside if you're not comfortable."
    scene 9_s5 with dissolve
    m "A-As you wish, Master."
    m "Do you want me to bring you something before I leave?"
    scene 9_s6 with dissolve
    mc "Actually, Maia. I don't really have a place to live. So I'm not sure where we'll be going after this."
    scene 9_s5 with dissolve
    m "R-Really?"
    scene 9_s6 with dissolve
    mc "Yeah. I'm new to this city... to this world, really."
    scene 9_s5 with dissolve
    m "Do you... want me to talk to Her Majesty about it?"
    scene 9_s6 with dissolve
    mc "Wait, you mean ask her to let me stay here? *chuckles* Can you really do that?"
    scene 9_s5 with dissolve
    m "Y-Yes! I mean... I can talk to Princess Rebecca, and then {i}she{/i} can tell Her Majesty."
    scene 9_s6 with dissolve
    mc "Nepotism. I like it."
    scene 9_s5 with dissolve
    m "Nepo...?"
    scene 9_s6 with dissolve
    mc "Forget it. I'd love that, Maia. At least for a while."
    scene 9_s5 with dissolve
    m "As you wish, Master."
    scene 9_s6 with dissolve
    scene 9_s2 with Fade(1.0,1.0,1.0)
    ""
    scene 9_s2 with Fade(2.0,1.0,2.0)
    mc "Alright, that's enough. I think I'm ready now."
    stop music fadeout 2.0 
    jump scene11

label scene09_choice01_grab:
    $ mc_talk_maia_home = True
    scene 9_s8 with dissolve
    m "Ahh! Master..."
    sensation "You cup one of her breasts, your fingers sinking into the pillowy softness. It's warmer and softer than anything you've ever touched. Her nipple stiffens, reacting to your touch."
    scene 9_s13 with dissolve
    mc "Sorry... I couldn't resist. I still can't believe you're my wife now. Just like that..."
    scene 9_s14 with dissolve
    m "I-It's fine..."
    scene 9_s14 with dissolve
    m "A-And... I'm sorry, Master... I don't really know what to do. I... once saw a maid and a guard doing it."
    scene 9_s13 with dissolve
    mc "And you've been curious ever since?"
    scene 9_s14 with dissolve
    m "Mhmm~ Will you... show me how?"
    scene 9_s13 with dissolve
    mc "First... let me get a good look at my new sexy wife."
    scene 9_s14 with dissolve
    m "Yes~"
    jump scene10

label scene09_choice01_nothing:
    scene 9_s10 with Dissolve(0.4)
    m "Master... what did you mean by you'll figure it out?"
    scene 9_s12 with Dissolve(0.4)
    mc "Honestly, Maia, I don't really have a place to stay yet."
    scene 9_s10 with Dissolve(0.4)
    m "R-Really?"
    scene 9_s12 with Dissolve(0.4)
    mc "Yeah. I'm new to this city... to this world, really."
    scene 9_s10 with Dissolve(0.4)
    m "Do you... want me to talk to Her Majesty about it?"
    scene 9_s12 with Dissolve(0.4)
    mc "*chuckles* Can you really do that? I mean, I've already told her about me not having a place to stay but she kinda brushed me off."
    scene 9_s10 with Dissolve(0.4)
    m "Y-Yes! I mean... I can talk to Princess Rebecca, and then {i}she{/i} can tell Her Majesty."
    scene 9_s12 with Dissolve(0.4)
    mc "Nepotism. I like it."
    scene 9_s10 with Dissolve(0.4)
    m "Nepo...?"
    scene 9_s12 with Dissolve(0.4)
    mc "Forget it. I'd love that, Maia. At least for a while."
    scene 9_s10 with Dissolve(0.4)
    m "As you wish, Master."
    scene 9_s12 with Dissolve(0.4)
    mc "Do you know what she's planning for me?"
    scene 9_s10 with Dissolve(0.4)
    m "Sorry, I don't understand, Master."
    scene 9_s12 with Dissolve(0.4)
    mc "The Queen. She said to come over to her quarters after the bath. And that Alice girl told me I'm to be recruited too."
    scene 9_s10 with Dissolve(0.4)
    m "O-Oh... No, sorry, I don't know."
    scene 9_s12 with Dissolve(0.4)
    mc "I guess I'll just have to find out for myself."
    scene 9_s11 with Dissolve(0.4)
    mc "(Damn... those breasts look incredible. I... I wonder how they would feel...)"
    m "..."
    mc "..."
    scene 9_s10 with Dissolve(0.4)
    m "Master? Do you... like me?"
    scene 9_s12 with Dissolve(0.4)
    mc "What's this all of a sudden?"
    scene 9_s10 with Dissolve(0.4)
    m "Your... cock. I-It's... getting bigger. I can see it under the water."
    scene 9_s12 with Dissolve(0.4)
    mc "So you noticed, huh? I was hoping the steam would cover it."
    mc "Yeah, Maia... you're just too beautiful. I don't think it's physically possible for anyone to react differently."
    scene 9_s10 with Dissolve(0.4)
    m "D-Do you... want to play? I could... try to help you. If you want. I know I'm supposed to... I mean, as your wife..."
    scene 9_s12 with Dissolve(0.4)
    mc "Oh, really? And how exactly would you do that?"
    scene 9_s10 with Dissolve(0.4)
    m "U-Umm... I... I can..."
    call screen scene09_choice01 with dissolve
    m "I'm sorry, Master... I don't really know what to do. I... once saw a maid and a guard doing it."
    m "I-I promise I wasn't spying! I was just... looking for something."
    scene 9_s12 with Dissolve(0.4)
    mc "And you've been curious ever since?"
    scene 9_s10 with Dissolve(0.4)
    m "Mhmm~ Will you... show me how? Please? I want to be a good wife. I want to learn."
    scene 9_s12 with Dissolve(0.4)
    mc "First... let me get a good look at my new sexy wife."
    scene 9_s10 with Dissolve(0.4)
    m "Yes~"
    scene 9_s11 with Dissolve(0.4)

label scene10:
    $ mcname = persistent.name
    if persistent.name == "None" or mcname == "None":
        while mcname == "None" or mcname == "":
            $ mcname = renpy.input("There was an issue with your name. Please rewrite your name:", length=32)
        $ persistent.name = mcname
    if not persistent.scene3_replay:
        $ persistent.scene3_replay = True
    scene 10_s1 with Fade(0.5,1.0,0.5)
    m "I'm sorry! I... I just don't know what I'm doing."
    scene 10_s2 with dissolve
    mc "Easy, Maia. No need to rush. We'll take our time, everyone starts somewhere."
    scene 10_s1 with dissolve
    m "Then... maybe you could tell me what you like? I want to learn... to be someone you enjoy being with."
    scene 10_s2 with dissolve
    mc "That's a dangerous thing to say to a man, you know."
    scene 10_s1 with dissolve
    m "I mean it. I... want to be good for you."
    scene 10_s2 with dissolve
    mc "(Damn... she's making it hard to think straight.)"
    call screen scene10_choice01 with dissolve

default showmouth01_first = True
default showtongue01_first = True
default test_throat01_first = True
default lookatchest01_first = True
default playnips01_first = True
default lookatpussy01_first = True
default spreadpussy01_first = True
default mastur01_cum = False
default mastur01_stop = False
default pee01_first = True
label scene10_choice01_lookatface:
    scene 10_s2 with dissolve
    call screen scene10_choice01 with dissolve

label scene10_choice01_showmouth:
    if showmouth01_first:
        mc "Show me your mouth."
        scene 10_s1 with dissolve
        m "Yes, Master."
        scene 10_s3 with dissolve
        m "Ahhhh... Ish this good, masher?"
        scene 10_s4 with dissolve
        mc "Yes, keep it open."
        scene 10_s3 with dissolve
        $ showmouth01_first = False
        call screen scene10_choice01 with dissolve
    else:
        scene 10_s3 with dissolve
        m "Ahhhh."
        scene 10_s4 with dissolve
        ""
        scene 10_s3 with dissolve
        call screen scene10_choice01 with dissolve

label scene10_choice01_showtongue:
    if showtongue01_first:
        scene 10_s5 with dissolve
        m "Yesh, masher."
        m "W-Will you... ushe my mouf... masher?"
        mc "I mean, if you'll let me."
        m "Of courshe ah will, mashter!"
        scene 10_s6 with dissolve
        m "Ahhnnn~"
        scene 10_s5 with dissolve
        $ showtongue01_first = False
        call screen scene10_choice01 with dissolve
    else:
        scene 10_s5 with dissolve
        m "Lhhnnn..."
        scene 10_s6 with dissolve
        ""
        scene 10_s5 with dissolve
        call screen scene10_choice01 with dissolve

label scene10_choice01_testthroat:
    if test_throat01_first:
        scene 10_s7 with dissolve
        m "*gag*"
        mc "Let me see your gag reflex."
        scene 10_s8 with dissolve
        m "*gag* Yesh... *gag* masher."
        image maia_mm01 = Movie(channel="movie_dp", play="images/1_opening/scene10/maia_mm01.webm", loop=True)
        show maia_mm01 with Dissolve(1.0)
        sensation "Your fingers glide in and out of her throat, met with the velvety slickness of her tongue. Warm saliva coats your skin, dripping down in thick strands as her throat flexes around you."
        $ test_throat01_first = False
        call screen scene10_choice01 with dissolve
    else:
        show maia_mm01 with dissolve
        call screen scene10_choice01 with dissolve

label scene10_choice01_lookatchest:
    if lookatchest01_first:
        scene 10_s10 with dissolve
        m "Do you... like my breasts, Master?"
        scene 10_s9 with dissolve
        $ lookatchest01_first = False
        call screen scene10_choice02 with dissolve
    else:
        scene 10_s9 with dissolve
        call screen scene10_choice01 with dissolve

label scene10_choice02_yes:
    mc "I do. They're perfect."
    scene 10_s10 with dissolve
    m "I hope mine are big enough for you. I heard some men won't settle for smaller breasts."
    scene 10_s9 with dissolve
    mc "They're more than enough."
    scene 10_s10 with dissolve
    m "I can't wait for the day when my breasts are full of... milk for our future children."
    scene 10_s9 with dissolve
    mc "*chuckles* Children? You want to have children... with me?"
    scene 10_s11 with dissolve
    m "O-Of course. Isn't that the purpose of getting married?"
    scene 10_s11_2 with dissolve
    call screen scene10_choice01 with dissolve

label scene10_choice02_likeass:
    mc "I like that cute butt of yours more."
    scene 10_s10 with dissolve
    m "*giggles* The Queen has told me I have... a well-rounded bottom. She sometimes even spanks me when I walk past her."
    m "Would... would you like me to show you?"
    scene 10_s9 with dissolve
    mc "This Queen is really something, huh?"
    scene 10_s11 with dissolve
    m "Yes, but she does it really hard. It hurts a lot afterwards..."
    scene 10_s11_2 with dissolve
    mc "..."
    call screen scene10_choice01 with dissolve

label scene10_choice01_playnips:
    if playnips01_first:
        mc "Show me how you play with your nipples."
        scene 10_s23 with dissolve
        m "Uhm... like this?"
        image maia_mt01 = Movie(channel="movie_dp", play="images/1_opening/scene10/maia_mt01.webm", loop=True)
        show maia_mt01 with Dissolve(1.0)
        mc "Yes, go on."
        m "..."
        mc "Does it not feel good?"
        m "It does! Just... you staring at me... makes it less good."
        m "I-I don't mean that in a bad way!"
        mc "*laughs* I understand, I guess we're just not used to seeing each other naked is all."
        $ playnips01_first = False
        call screen scene10_choice01 with dissolve
    else: 
        show maia_mt01 with Dissolve(1.0)
        m "Do you also feel good when you touch your nipples, Master?"
        mc "Well... not as much."
        call screen scene10_choice01 with dissolve

label scene10_choice01_lookathip:
    if lookatpussy01_first:
        scene 10_s12 with dissolve
        m "Do you like my pussy, Master?"
        scene 10_s13 with dissolve
        mc "Pussy... Cock... Who taught you these words?"
        scene 10_s14 with dissolve
        m "Should I not be s-saying that, Master?"
        scene 10_s13 with dissolve
        mc "No, it's fine. Just hearing those words come out of your mouth is... weird, and hot."
        scene 10_s12 with dissolve
        m "H-Hot?"
        scene 10_s13 with dissolve
        mc "Yeah. Keep talking."
        scene 10_s12 with dissolve
        m "U-Ummm... when you stare at my pussy... it starts to get really wet and warm."
        scene 10_s13 with dissolve
        mc "You're a natural."
        scene 10_s13 with dissolve
        $ lookatpussy01_first = False
        call screen scene10_choice01 with dissolve
    else:
        scene 10_s13 with dissolve
        call screen scene10_choice01 with dissolve
label scene10_choice01_spreadpussy:
    if spreadpussy01_first:
        mc "Spread your pussy. Let me see how it looks on the inside."
        play sound "se_sfx/sex/touch2.mp3" 
        scene 10_s15_2 with dissolve
        m "Like... like this, Master?"
        scene 10_s15 with dissolve
        mc "You... ever had a lover, Maia?"
        scene 10_s15_2 with dissolve
        m "No, Master. Y-You will be my first."
        scene 10_s15 with dissolve
        $ spreadpussy01_first = False
        call screen scene10_choice01 with dissolve
    else:
        play sound "se_sfx/sex/touch2.mp3" 
        scene 10_s15 with dissolve
        call screen scene10_choice01 with dissolve

label scene10_choice01_mastur:
    mc "Can you show me how you masturbate?"
    scene 10_s15_2 with dissolve
    m "T-That's a little embarrassing, but... as you wish."
    image maia_mp01 = Movie(channel="movie_dp", play="images/1_opening/scene10/maia_mp01.webm", loop=True)
    show maia_mp01 with Dissolve(1.0)
    m "Mmhnnn..."
    mc "..."
    m "M-Master, could you please stop staring so intensely?"
    mc "Incredible technique."
    m "Wh-What? You mean how I'm focusing on my bean?"
    mc "Exactly. How did you learn that?"
    m "I did on my own. I noticed that playing with my bean makes my juices come sooner."
    call screen scene10_choice03 with dissolve

label scene10_choice03_cum:
    m "I... I'm close, Master!"
    mc "Cum!"
    play sound "se_sfx/masturbate_female/6_masturbate_cum1.mp3"
    scene 10_s24 with vpunch
    m "Ahhhhh!!"
    play sound "se_sfx/blowjob/facial1.mp3" 
    scene 10_s25 with vpunch
    m "Hnngg!!!"
    scene 10_s29 with dissolve
    m "Hah... hah..."
    scene 10_s26 with dissolve
    m "Oh! I'm terribly sorry, Master! Did I drench you in my special juices?"
    scene 10_s30 with dissolve
    mc "It's fine, don't worry about it. As a matter of fact, I like it."
    m "Ehehe~"
    $ mastur01_cum = True
    call screen scene10_choice01 with dissolve

label scene10_choice03_stop:
    mc "Stop."
    scene 10_s22 with dissolve
    m "But... Master, please! I was really close..."
    scene 10_s21 with dissolve
    mc "No. Let's make it a rule that you only finish when I tell you to."
    scene 10_s22 with dissolve
    m "Yes, Master... I'm sorry."
    scene 10_s21 with dissolve
    $ mastur01_stop = True
    call screen scene10_choice01 with dissolve

label scene10_choice01_mastur_second:
    if mastur01_cum:
        scene 10_s18 with dissolve
        m "But Master... my... pussy is really sensitive right now."
        scene 10_s31 with dissolve
        mc "It'll feel even better when you push yourself over the edge again."
        scene 10_s18 with dissolve
        m "Yes, I understand..."
        $ mastur01_cum = False
        show maia_mp01 with Dissolve(1.0)
        call screen scene10_choice01 with dissolve
    
    elif mastur01_stop:
        scene 10_s18 with dissolve
        m "May I please finish now, Master?"
        scene 10_s31 with dissolve
        call screen scene10_choice04 with dissolve
    
    elif mastur01_cum == False:
        show maia_mp01 with Dissolve(1.0)
        call screen scene10_choice01 with dissolve

label scene10_choice01_mastur_second_cum:
    scene 10_s32 with dissolve
    m "Thank you, thank you, thank you!"
    show maia_mp01 with Dissolve(1.0)
    ""
    scene 10_s24 with vpunch
    m "Ahhhhh!!"
    scene 10_s25 with vpunch
    m "Hnngg!!!"
    scene 10_s29 with dissolve
    m "Hah... hah..."
    $ mastur01_cum = True
    $ mastur01_stop = False
    call screen scene10_choice01 with dissolve

label scene10_choice01_mastur_second_notyet:
    mc "No, not yet."
    scene 10_s18 with dissolve
    m "Hnngg... Master, you're so cruel..."
    scene 10_s31 with dissolve
    call screen scene10_choice01 with dissolve

label scene10_choice01_pee:
    if pee01_first:
        mc "Got the urge to pee?"
        scene 10_s15_2 with dissolve
        m "Hmm? No. Not really."
        scene 10_s15 with dissolve
        mc "Aww... I was hoping you'd pee for me."
        scene 10_s16 with dissolve
        m "M-Master?!"
        scene 10_s28 with dissolve
        mc "Nothing at all left in the tank?"
        scene 10_s16 with dissolve
        m "No... it's just... Is that really what you want?"
        scene 10_s28 with dissolve
        mc "Yes. And don't worry about me."
        scene 10_s15_2 with dissolve
        m "Then..."
        scene 10_s17 with dissolve
        m "Unnff..."
        scene 10_s18 with dissolve
        m "There isn't any left, Master."
        scene 10_s15 with dissolve
        mc "It's fine, you did good."
        $ pee01_first = False
        call screen scene10_choice01 with dissolve
    else:
        scene 10_s33 with dissolve
        m "I'm really sorry, Master. I would love to pee for you again, but there's nothing left..."
        m "I'll have to drink more water! Or... or juices!"
        scene 10_s15 with dissolve
        call screen scene10_choice01 with dissolve

label scene10_choice01_lookanus:
    scene 10_s15_2 with dissolve
    m "You're looking at my butthole!"
    m "You... you want to use it for your pleasure?"
    scene 10_s15 with dissolve
    mc "Would you be alright with that?"
    scene 10_s16 with dissolve
    m "Well... I can't get pregnant like that. You should insert your cock into my pussy if we want to make babies. A-At least, that's what I heard."
    scene 10_s15 with dissolve
    mc "*laughs* I know. I'm just looking for now."
    scene 10_s15_2 with dissolve
    m "*giggles* You're a pervert, Master."
    scene 10_s15 with dissolve
    call screen scene10_choice01 with dissolve


label scene10_choice01_finish:
    $ renpy.end_replay()
    scene 10_s13 with dissolve
    mc "Alright, I've seen enough."
    scene 10_s12 with dissolve
    m "*chuckles* What's the verdict, Master?"
    scene 10_s13 with dissolve
    mc "A perfect ten out of ten. Now, why don't we get serious?"
    scene 10_s12 with dissolve
    m "Are you going to use your cock on me, Master?"
    scene 10_s13 with dissolve
    mc "Keep talking like that and I will."
    m "Mhmm~"
    "*knock* *knock*"
    guard "Sir? Her Majesty is calling for you."
    scene 10_s13 with dissolve
    mc "Shit. I forgot about that."
    mc "I guess we'll just have to do this another time, Maia."
    scene 10_s12 with dissolve
    m "I-It's fine..."
    m "Shall I take you to the Queen, Master?"
    scene 10_s13 with dissolve
    mc "Yes, lead the way."
    $ renpy.end_replay()
    stop music fadeout (3.0)
    jump scene11

label scene11:
    scene black with Fade(0.5,1.0,0.5)
    scene 11_s1 with dissolve
    m "This is Her Majesty's chamber, Master."
    m "Is there anything else you need before I go?"
    scene 11_s2 with dissolve
    mc "No, that's all. Thank you, Maia."
    scene 11_s1 with dissolve
    m "Then I'll take my leave. But if you need anything at all, just call for me."
    scene 11_s3 with fade
    mc "(That ass is irresistible.)"
    call screen scene11_choice01 with dissolve

label scene11_choice01_slap:
    scene 11_s4 with dissolve
    perception "You lift your hand, fingers spread, anticipation tingling in your palm. Her ass remains there, unguarded, blissfully unaware of what's coming."
    play sound "sound_effects/slap01.mp3"
    scene 11_s5 with vpunch
    m "Ahh!"
    scene 11_s6 with dissolve
    m "Ahaha... Master... you have an odd way of showing your love..."
    scene 11_s7 with dissolve
    m "Owww..."
    mc "(Damn, that left quite the mark... did I overdo it?)"
    jump scene12

label scene12:
    $ mc_went_castle = True
    scene black with Fade(0.5,1.0,0.5)
    play music "queen.mp3" fadein 2.0 loop
    scene 12_s1 with dissolve
    q "Took your sweet time, didn't you?"
    scene 12_s18 with dissolve
    ""
    scene 12_s19 with dissolve
    mc "(Is that a statue?)"
    scene 12_s1 with dissolve
    mc "Yeah... sorry. The bath took longer than expected. I'm here now."
    scene 12_s1 with dissolve
    q "What kind of man are you, [mc]?"
    scene 12_s2 with dissolve
    if mc_lied:
        mc "The... kind who gets things done?"
        scene 12_s1 with dissolve
        q "Is that so?"
    if mc_truth:
        mc "What?"
    scene 12_s1 with dissolve
    if mc_lied:
        q "A stranger arrives from nowhere. No name, no history. Yet, within hours, he slays a beast that terrorized my lands for years."
        scene 12_s2 with dissolve
        mc "That's right."
        scene 12_s1 with dissolve
        q "And tell me, hero, how exactly did you manage such a feat? Or does your 'head still hurt'?"
        scene 12_s2 with dissolve
        mc "Skill. Luck. Does it matter?"
    if mc_truth:
        q "You arrive out of nowhere. You barely survive an encounter with an ogre, and by sheer luck, it dies."
        scene 12_s2 with dissolve
        q "Yet, here you stand, dressed as a hero, rewarded like a hero, and treated as one. Tell me, do you think that's fair?"
        mc "I never asked for any of this. I even told you—what happened was an accident."
        scene 12_s1 with dissolve
        q "Yes, and that troubles me."

    scene 12_s1 with dissolve
    q "Come here."
    scene 12_s3 with Dissolve(0.6)
    q "Kneel."
    scene 12_s4 with dissolve
    ""
    play sound "sound_effects/slap07.mp3"
    scene 12_s5 with vpunch
    pause 0.5
    scene 12_s6 with dissolve
    mc "What the hell?!"
    sensation "Your ears ring and your vision tilts—this was no mere slap. The sting sends a flash of memories rushing back, painful moments from your past, the kind that will {i}never{/i} fade."
    q "I'll ask again. Why are you here, and who sent you?"
    q "Are you really {i}some saint{/i} sent by the heavens? Or are you a spy, an assassin, a plant from one of my enemies?"
    scene 12_s7 with dissolve
    mc "(She's crazy! One minute she's giving me a wife, the next she's slapping me!)"
    mc "No one sent me! I don't even know how I got here!"
    scene 12_s6 with dissolve
    q "Is that so?"
    scene 12_s8 with Dissolve(1.0)
    q "Hmm... you don't have the look of a mercenary or an assassin. No... your skin is too soft."
    q "Your eyes are too honest. And your heart... it's beating far too quick for a trained killer."
    if mc_lied:
        q "Still you got rid of an ogre somehow..."
    scene 12_s9 with dissolve
    q "I suppose we'll find out soon enough who you really are. The truth has a way of surfacing, especially under pressure."
    q "I expect great things from you, [mc]. Now, get up."
    scene 12_s10 with Dissolve(1.5)
    q "Do it."
    scene 12_s11 with dissolve
    mc "Wait, wait, wait! I told you that I'm not here for anyone! I swear! I don't have an agenda! I don't even know what an agenda would be in this world!"
    scene 12_s12 with dissolve
    mc "Hnngg... please make it painless! If you're going to execute me, just... do it quick!"
    scene 12_s13 with dissolve
    mc "Huh?"
    q "*chuckles* Execute you? You're an interesting one, [mc]."
    scene 12_s14 with dissolve
    mc "Wha-?"
    scene 12_s15 with dissolve
    q "You claim you're not from here. You claim you have no agenda. So tell me again, [mc], what are you? A saint? A fool? A ghost?"
    mc "I don't know. I'm just... me. Whoever that is. Whoever I was before... he's gone. All I have is right now."
    q "Then let's find out what {i}you{/i} really are. Together."
    scene 12_s14 with dissolve
    mc "What do you mean?"
    scene 12_s15 with dissolve
    q "From this moment on, you're mine."
    q "And a man with no past and no future must at least prove he has something worth keeping him alive."
    q "Hesitate, and I'll take it as weakness. Fail, and I'll know you were never worth my time. Or... do you intend to keep pretending you're above all this?"
    mc "(Damn, this woman... she's terrifying. And kind of magnificent. Is it wrong to be a little attracted to someone who just slapped the shit out of you?)"
    mc "...Fine. There's nothing else for me to do anyway. I've got no home, no coin, no memories. Might as well see where this goes."
    q "Good."
    scene 12_s14 with dissolve
    mc "...What do I do now?"
    scene 12_s20 with Dissolve(1.0)
    q "You have nowhere to be, isn't that right?"
    scene 12_s21 with dissolve
    mc "I don't. Unless you count a brothel."
    scene 12_s20 with dissolve
    q "Even better. I can keep a close eye on you."
    scene 12_s21 with dissolve
    mc "Will you give me a place to stay at least? A room? Hell, I'll take a closet at this point."
    scene 12_s20 with dissolve
    q "Haven't I been generous enough, [mc]? I rewarded you with a maid and put you to work for me even though I'm still deeply suspicious of you."
    q "Many rulers would have thrown you in the dungeon and been done with it."
    q "Besides, you won't be needing sleep tonight. You'll go to the courtyard. I need to see what you're capable of... and perhaps shape it."
    scene 12_s21 with dissolve
    mc "I'm guessing I don't get a choice in the matter?"
    scene 12_s20 with dissolve
    q "You guess correctly. Now make haste—the day is already yawning."
    scene 12_s21 with dissolve
    mc "On it... Your Majesty."
    stop music fadeout (2.0)

label scene12_0:
    scene 12_0_1 with Fade(1.0,1.0,2.0)
    play music "nature.mp3" fadein 3.0 loop
    ""
    scene 12_0_2 with Fade(1.0,0.5,0.5)
    ""
    scene 12_0_3 with Dissolve(1.0)
    adam_ "Ah, you must be [mc]."
    scene 12_0_4 with dissolve
    mc "Hey. And you are?"
    scene 12_0_3 with dissolve
    adam "Adam. Captain of the Queen's training regimen."
    adam "I turn soft recruits into soldiers. So, you're the one who took down the ogre?"
    scene 12_0_4 with dissolve
    if mc_lied:
        mc "Supposedly? I did. That's what everyone keeps telling me, anyway."
        scene 12_0_3 with dissolve
        adam "Quite the feat. A monster that's killed seasoned hunters, and you brought it down alone."
        adam "We'll see if your sword arm lives up to your mouth."
        scene 12_0_4 with dissolve
    if mc_truth:
        mc "Luck was on my side yesterday. Nothing more."
        scene 12_0_3 with dissolve
        adam "Luck? You dabble in magic then? Prediction magic? Fate-weaving?"
        scene 12_0_4 with dissolve
        mc "Magic? No. Well... maybe? I'm not sure."

    mc "Couldn't you guys have handled it yourselves? You've got a whole army. Why was one monster such a problem?"
    scene 12_0_3 with dissolve
    adam "What, you think we were just sitting on our asses while it tore through our farms?"
    adam "We didn't have the manpower, plain and simple. Half our forces are stationed along the trade routes. The other half are spread thin protecting the borders."
    adam "The ogre was a problem, but not a 'recall the entire army' problem."
    scene 12_0_4 with dissolve
    mc "Then couldn't you have brought in people from outside your army?"
    scene 12_0_3 with dissolve
    adam "Like the guild lot? All of them refused. Claimed the reward was too low."
    adam "That's what they said, anyway. In truth? I think the real reason was that they were waiting for the bounty to go up."
    adam "Let the farmers suffer a bit longer, let the council get desperate, and suddenly that fifty gold becomes a hundred. Vultures, the lot of them. *Ptoo*."
    scene 12_0_4 with dissolve
    mc "Hmm... I still think you people were holding out for something. But whatever. I'm here to train."
    scene 12_0_5 with dissolve
    adam "We'll start before the elf shows up."
    scene 12_0_6 with dissolve
    mc "The elf?"
    scene 12_0_5 with dissolve
    adam "Ava, the royal examiner. She's a powerful mage. Can see your mana potential. Probably tell you if you're destined to be a hero or a house pet."
    scene 12_0_6 with dissolve
    mc "That's... useful. Hopefully I have some."
    scene 12_0_5 with dissolve
    adam "Hah! Don't get your hopes too high. We humans aren't exactly overflowing with it. Elves are born swimming in the stuff. Dwarves have their runes."
    adam "But humans? We get muscle and stubbornness. Unless you're a devil in disguise, of course. You're not a devil, are you?"
    scene 12_0_6 with dissolve
    mc "Let's get this over with, Adam. I've got a beautiful wife waiting for, and I'd rather not keep her waiting all day."
    scene 12_0_5 with dissolve
    adam "*chuckles* Finishing early depends on you."
    adam "Here."
    scene 12_0_7 with dissolve
    ""
    scene 12_0_9 with Dissolve(1.0)
    adam "Show me what you got."
    scene 12_0_8 with dissolve
    mc "Against you? No training dummy?"
    scene 12_0_9 with dissolve
    adam "The best experience comes from the real thing."
    if mc_lied:
        adam "Besides, you took down the ogre. We're way past training dummies at this point."
    scene 12_0_8 with dissolve
    mc "What about some protection? Do you see what I'm wearing compared to you? You've got armor. I've got... this shirt. Which isn't even mine."
    scene 12_0_9 with dissolve
    adam "Alright, fair point. Let's level the playing field then."
    scene 12_0_8 with dissolve
    scene 12_0_10 with Dissolve(1.0)
    ""
    play sound "sound_effects/woosh1.mp3"
    stop music fadeout 1.0 
    scene 12_0_11 with vpunch
    mc "H-How the hell?!"
    #mc "...Fine. Just don't cry when I hit you."
    adam "Let's begin!"
    play music "fight1.mp3" fadein 2.0 loop
    scene 12_0_12 with vpunch
    mc "Damn—!"
    adam "Too slow!"
    play sound "sound_effects/sword_clash2.mp3"
    scene 12_0_13 with vpunch
    adam "Hah! There it is—strength. But you're winding up like you're chopping firewood."
    adam "Rule one: your enemy won't stand still just because you want them to."
    scene 12_0_14 with vpunch
    mc "Tch—"
    adam "Rule two: big swings make big targets. You'd be dead three times over by now."
    mc "Maybe... but if I did hit you, you'd be paste."
    adam "True. But you've gotta land it first."
    scene 12_0_15 with Dissolve(1.0)
    adam "Not bad. You've got raw muscle. Now we just need to give it a brain."
    scene 12_0_16 with dissolve
    mc "So I'm a dumb sword right now?"
    scene 12_0_15 with dissolve
    adam "Exactly. And I'm gonna hammer some sense into that blade of yours."
    adam "Again."
    scene 12_0_16 with dissolve
    play sound "sound_effects/sword_clash3.mp3"
    scene 12_0_17 with vpunch
    adam "*laughs* That's the stuff! Keep swinging like that and maybe—"
    play sound "sound_effects/punch.mp3"
    scene 12_0_18 with vpunch
    adam "—you'll actually hit someone someday."
    mc "Nghn! Stop!"
    scene 12_0_15 with dissolve
    adam "What? You ain't getting a break if that's what you want. The enemy doesn't call time out."
    scene 12_0_16 with dissolve
    mc "I didn't know punches were allowed! You said sword training!"
    scene 12_0_15 with dissolve
    adam "In a life or death scenario, everything is permitted. You think a bandit's gonna bow and wait for you to catch your breath?"
    scene 12_0_16 with dissolve
    mc "...You're enjoying this way too much."
    scene 12_0_15 with dissolve
    adam "Best part of my day."
    adam "Pick it up. We're not done until you can at least keep me busy for more than ten seconds."
    scene 12_0_16 with dissolve
    scene 12_0_19 with Dissolve(2.0)
    yuuhi_stepfather "Yuuhi! Where did you go?"
    yuuhi_ "Coming!"
    stop music fadeout 2.0 
    scene 12_0_20 with Dissolve(2.0)
    ""
    play music "night.mp3" fadein 3.0 loop
    scene 12_0_21 with Dissolve(2.0)
    adam "Ahh... hah... If anything, you've got the stamina for this."
    adam "You've got a mean punch too. I think I'll be feeling that for days."
    scene 12_0_22 with dissolve
    mc "*cough* Thanks..."
    scene 12_0_23 with Dissolve(1.0)
    ava_ "Umm... I'm sorry—did I arrive at a bad time?"
    scene 12_0_24 with dissolve
    mc "Huh? No! Don't get the wrong idea!"
    adam "*laughs* Just sparring, sweetheart. That's all. Though he did get a few good licks in."
    scene 12_0_23 with dissolve
    ava_ "Right..."
    scene 12_0_24 with dissolve
    scene 12_0_25 with Dissolve(1.0)
    ava "*ahem* Hello, [mc]. I'm Ava. I'm the royal examiner for Her Majesty's new recruits."
    ava "My job is to assess each new recruit's mana. It's a standard procedure that every recruit has to undergo."
    scene 12_0_26 with dissolve
    mc "Hey! You're an elf, right? A real elf?!"
    scene 12_0_25 with dissolve
    ava "...Y-Yes?"
    scene 12_0_26 with dissolve
    adam "You seriously couldn't tell that?"
    mc "It's crazy seeing one of you this close. I mean, I've read about elves. But actually meeting one? That's different."
    mc "Can I... touch your ears?"
    scene 12_0_25 with dissolve
    ava "*chuckles* Ahaha... I'd really prefer if you didn't."
    ava "And I don't blame you for being excited, there's not many of us around here. Most of my kin prefer living in up north in Veilnirn."
    scene 12_0_26 with dissolve
    mc "So, the mana level check. How long would it take? Is it painful?"
    scene 12_0_25 with dissolve
    ava "Only a moment, I promise. Just stand still."
    scene 12_0_26 with dissolve
    mc "Alright, go ahead."
    play sound "sound_effects/magic1.mp3"
    scene 12_0_27 with Dissolve(1.0)
    ava "..."
    scene 12_0_28 with dissolve
    ava "That's... interesting."
    scene 12_0_27 with dissolve
    adam "Come on, lass. Don't keep us in suspense. Is he the next archmage or what?"
    scene 12_0_28 with dissolve
    ava "I umm..."
    scene 12_0_27 with dissolve
    mc "What is it?"
    scene 12_0_28 with dissolve
    ava "It can't be..."
    scene 12_0_27 with dissolve
    mc "Just tell me straight!"
    scene 12_0_28 with dissolve
    ava "I'm really sorry, [mc]... but you don't seem to possess any mana at all. Not a single spark. I've never seen a complete absence like this."
    scene 12_0_27 with dissolve
    mc "...Fuck. Seriously?"
    adam "Ah, don't let it eat at you. Steel's all you need anyway."
    ava "..."
    mc "Could you check again? Maybe you missed something? Maybe it's just... hiding?"
    scene 12_0_28 with dissolve
    ava "I'm sorry, [mc]. The results are clear. But—"
    scene 12_0_25 with Dissolve(1.0)
    ava "Your mana might simply be dormant!"
    scene 12_0_26 with dissolve
    mc "Dormant?"
    scene 12_0_25 with dissolve
    ava "Sometimes people live for decades without a single spark of magic, and then in the moment of extreme crisis it awakens."
    ava "There are documented cases. There was once a legendary mage who lived for two hundred years before—"
    scene 12_0_26 with vpunch
    mc "Two hundred years?!"
    scene 12_0_25 with dissolve
    ava "...Yes."
    scene 12_0_26 with dissolve
    mc "I'm sure you already know that humans don't exactly have that long. I'll be dead of old age before my 'dormant magic' decides to wake up."
    scene 12_0_25 with dissolve
    ava "Right... I forget sometimes."
    scene 12_0_30 with dissolve
    adam "Forget all that gloom. You did well for today. How about we end it here?"
    scene 12_0_29 with dissolve
    mc "That'd be good, I can barely feel my arms."
    scene 12_0_30 with dissolve
    adam "I'll see you here tomorrow, same time."
    scene 12_0_29 with vpunch
    mc "Tomorrow?!"
    scene 12_0_30 with dissolve
    adam "What? You thought that was it? You've got a long way to go, recruit."
    scene 12_0_29 with dissolve
    mc "*sigh* If I've got no magic, guess there's no choice."
    scene 12_0_30 with dissolve
    adam "That's the spirit!"
    scene 12_0_29 with dissolve
    scene 12_0_26 with Dissolve(1.0)
    mc "Thanks, Ava. Sorry you had to come out here for nothing."
    scene 12_0_25 with dissolve
    ava "It wasn't nothing. Farewell, [mc]. Sir Adam."
    scene 12_0_26 with dissolve
    scene 12_0_31 with Dissolve(2.0)
    adam "Got a fat ass, that one. Elves, I swear. They don't age, they don't sweat, and they walk like the world owes them a favor. Annoying. But you can't deny the view."
    mc "Seriously? Right after she helped us?"
    call screen scene12_choice01 with dissolve
    scene 12_0_29 with Dissolve(1.0)
    mc "..."
    scene 12_0_30 with dissolve
    adam "What? Don't tell me you didn't see it too."
    scene 12_0_29 with dissolve
    mc "*chuckles* See you tomorrow, Adam. I gotta... figure out where I'm sleeping tonight."
    scene 12_0_30 with dissolve
    adam "Wait, you don't have a place? I thought Her Majesty set you up with that maid... what's her name, Maia?"
    scene 12_0_29 with dissolve
    mc "She did. But we don't have anywhere to actually live. The Queen said we'd 'discuss it later'."
    scene 12_0_30 with dissolve
    adam "Damn... Listen, I'd offer you a bed, but... the wife—yeah, she'd probably have my head. Hope you understand."
    scene 12_0_29 with dissolve
    mc "I get it. Don't worry about it, I'll manage."
    scene 12_0_30 with dissolve
    adam "Well, there's always a tavern. Or a brothel, if you're short on coin and don't mind the company."
    adam "The Slick Worm is cheap and the beds are somewhat clean. Vera runs a tight ship."
    scene 12_0_29 with dissolve
    mc "Right... I'll keep that in mind."
    scene 12_0_30 with dissolve
    adam "Alright then. Good luck, recruit."
    scene 12_0_29 with dissolve
    jump scene13_0

label scene12_choice01_op1:
    scene 12_0_32 with Dissolve(1.0)
    mc "You're not kidding."
    adam "Heh. I got a good eye for these things. Twenty years of marriage doesn't make you blind, it just makes you discreet. You learn to appreciate from a distance."
    scene 12_0_29 with Dissolve(1.0)
    mc "*chuckles* See you tomorrow, Adam. I gotta... figure out where I'm sleeping tonight."
    scene 12_0_30 with dissolve
    adam "Wait, you don't have a place? I thought Her Majesty set you up with that maid... what's her name, Maia?"
    scene 12_0_29 with dissolve
    mc "She did. But we don't have anywhere to actually live. The Queen said we'd 'discuss it later'."
    scene 12_0_30 with dissolve
    adam "Damn... Listen, I'd offer you a bed, but... the wife—yeah, she'd probably have my head. Hope you understand."
    scene 12_0_29 with dissolve
    mc "I get it. Don't worry about it, I'll manage."
    scene 12_0_30 with dissolve
    adam "Well, there's always a tavern. Or a brothel, if you're short on coin and don't mind the company."
    adam "The Slick Worm is cheap and the beds are somewhat clean. Vera runs a tight ship."
    scene 12_0_29 with dissolve
    mc "Right... I'll keep that in mind."
    scene 12_0_30 with dissolve
    adam "Alright then. Good luck, recruit."
    scene 12_0_29 with dissolve

label scene13_0:
    scene 13_0_1 with Fade(1.0,1.0,1.5)
    mc "(Damn my pride... I should've asked him for coin.)"
    mc "(Whatever. I'll just head into town. There's got to be somewhere I can crash.)"
    scene 13_0_2 with Fade(2.0,1.0,1.0)
    perception "The market streets are dimly lit by scattered lanterns, their light flickering across cobblestone slick from a recent rain."
    mc "(Where to now? *sigh* I could've tried to find Maia, but I don't even know where she sleeps. Some husband I'm turning out to be.)"
    scene 13_0_3 with Dissolve(1.0)
    begger "Spare a coin for an old soldier, sir?"
    mc "Me and you both, buddy. I was about to ask you the same thing."
    begger "...Huh?"
    scene 13_0_4 with Fade(0.5,0.5,0.5)
    mc "This'll do! At least it's not the floor."
    if mc_went_castle:
        mc "(I hope Maia gets me a place at the castle... If not, then I'm not sure how I'll survive.)"
        mc "(I guess I could wait for the Queen to pay me too. She said I'm working for her now, right?)"
    scene 13_0_5 with Dissolve(2.0)
    mc "(I'm so tired... I could sleep for a week.)"
    ml_ "Ahh! A thief!"
    scene 13_0_6 with dissolve
    mc "A thief?! Where?!"
    play sound "sound_effects/punch2.mp3"
    scene 13_0_7 with vpunch
    mc "Agh!"
    scene 13_0_9 with Dissolve(1.0)
    mc "What the hell, lady?!"
    scene 13_0_8 with dissolve
    ml_ "Get away from my stall! I've had enough of you thugs trying to rob me blind!"
    scene 13_0_9 with dissolve
    mc "Your—? Oh. Sorry, I didn't know."
    scene 13_0_8 with dissolve
    ml_ "Execuse me?"
    scene 13_0_9 with dissolve
    mc "I just wanted to sleep. Didn't realize this... table was yours."
    ml_ "..."
    mc "I'm telling the truth. Check your stuff—I didn't take anything."
    scene 13_0_11 with dissolve
    ml_ "...I-I'm sorry. Are you hurt? I hit you pretty hard."
    scene 13_0_10 with dissolve
    mc "I'm fine. What about you? You're trembling."
    ml_ "Mhmm..."
    mc "You need to sit, you look like you'll fall over any second."
    stop music fadeout 2.0 
    scene 13_0_13 with Fade(0.5,0.5,0.5)
    ml "*sigh* I'm Nadia. And you are?"
    play music "side_event2.mp3" fadein 3.0 loop
    scene 13_0_12 with dissolve
    mc "[mc]. And, uh... damn. Your outfit. Just noticed."
    scene 13_0_13 with dissolve
    ml "Lovely, isn't it? Makes me look like a common streetwalker."
    scene 13_0_12 with dissolve
    mc "Not quite the word I'd use..."
    scene 13_0_13 with dissolve
    ml "It's just to draw in customers. A friend suggested it. Said I'd sell more milk if I looked... appealing."
    scene 13_0_12 with dissolve
    mc "You don't say. So, why were you shaking earlier?"
    scene 13_0_13 with dissolve
    ml "Truth is, [mc]... even after I sold my pride and wore this skimpy outfit, my business is failing. I'm barely breaking even. Most days I don't sell a single canister."
    scene 13_0_12 with dissolve
    mc "Why's that?"
    scene 13_0_13 with dissolve
    ml "A man named Abel showed up to me a while back. I'm sure you've heard of him—everyone in this district knows his name."
    scene 13_0_12 with dissolve
    mc "Haven't, no. I'm new here. Like {i}very{/i} new."
    scene 13_0_13 with dissolve
    ml "Really? Abel's the closest thing this market has to a king. And not the benevolent kind."
    scene 13_0_12 with dissolve
    mc "What's his deal? Is he extorting you?"
    scene 13_0_13 with dissolve
    ml "Not exaggerating—he basically owns this market. He demanded I pay him a cut just for selling my milk here."
    scene 13_0_12 with dissolve
    mc "And you refused?"
    scene 13_0_13 with dissolve
    ml "Exactly. He owns the shops, not the streets. I'm not giving that bastard a single copper for the privilege of standing on public cobblestone."
    scene 13_0_12 with dissolve
    mc "Good on you for standing up to him."
    scene 13_0_13 with dissolve
    ml "Heh. And look where it's gotten me... haven't sold a single canister since. Three weeks of standing here in this ridiculous outfit"
    scene 13_0_12 with dissolve
    mc "How's that possible? You're still here."
    scene 13_0_13 with dissolve
    ml "He has... methods to keep people away. He would tell his goons to spread lies, say that my milk is spoiled and all."
    ml "He will go even as far to threaten people who come near me."
    scene 13_0_12 with dissolve
    call screen scene13_choice05 with dissolve

label scene13_choice04_op2:
    mc "Sounds tough."
    scene 13_0_14 with Dissolve(1.0)
    ml "*chuckles* It is. Look at me, talking your ear off. You came here to sleep, and I've been dumping my problems on you for ten minutes."
    ml "You must think I'm pathetic. Sometimes you need to vent."
    scene 13_0_15 with dissolve
    mc "Hey, I don't mind it."
    scene 13_0_14 with dissolve
    ml "You know what? I feel better already. Guess I just needed someone to talk to."
    ml "Alright then. It's getting late—I should head home. What about you? Where are you staying?"
    scene 13_0_15 with dissolve
    mc "Actually... I don't have a place to stay for today. That's why I was sleeping here in the first place."
    scene 13_0_14 with dissolve
    ml "Oh... I see."
    ml "Well, why don't you come with me? My place isn't much, but it's definitely warmer."
    scene 13_0_15 with dissolve
    mc "Your place? You'd really do that?"
    scene 13_0_14 with dissolve
    ml "Mhm. Call it payback for hitting you on the head."
    scene 13_0_15 with dissolve
    mc "Thank you, Nadia—you just saved my back."
    scene 13_0_14 with dissolve
    ml "*chuckles* It's not far. Come on."
    scene 13_0_15 with dissolve
    scene 13_0_16 with Dissolve(2.0)
    ""
    jump scene13_00

label scene13_choice04_op1:
    $ mc_accept_helped_nadia = True
    mc "That's terrible! Where is he? I'll put some sense into him."
    scene 13_0_14 with Dissolve(1.0)
    ml "*laughs* Did you not hear me? He's too powerful. You'd be behind bars before you even got close."
    scene 13_0_15 with dissolve
    mc "I don't care. People like that make me sick."
    mc "They prey on the weak because no one ever fights back. Well, I'm here now. And I've got nothing to lose."
    ml "..."
    scene 13_0_14 with dissolve
    ml "[mc]... Before you do anything stupid, maybe we try the peaceful way first?"
    scene 13_0_15 with dissolve
    mc "You mean... talking to him?"
    scene 13_0_14 with dissolve
    ml "Mhm. I don't mind paying him now, but maybe you could convince him to lower his price. I'm too scared to go myself."
    ml "But you... you've got fire in your eyes. He might listen to you."
    scene 13_0_15 with dissolve
    mc "I'll do it."
    scene 13_0_14 with dissolve
    ml "Thank you, [mc]. You're too kind. And... I'm really sorry for hitting you earlier."
    scene 13_0_15 with dissolve
    mc "That? I took it like a champ. Don't worry about it."
    scene 13_0_14 with dissolve
    ml "*laughs* Alright then. I'll see you tomorrow? You know where to find me—same stall, same ridiculous outfit."
    scene 13_0_15 with dissolve
    mc "Actually... I don't have a place to stay for today. That's why I was sleeping here in the first place."
    scene 13_0_14 with dissolve
    ml "Oh... I see. Well, why don't you come with me? I've got a spare blanket or two."
    scene 13_0_15 with dissolve
    mc "Your place? You'd really do that?"
    scene 13_0_14 with dissolve
    ml "Mhm. I trust you."
    scene 13_0_15 with dissolve
    mc "Thank you, Nadia. You just saved my back."
    scene 13_0_14 with dissolve
    ml "*chuckles* It's not far. Come on."
    scene 13_0_15 with dissolve
    stop music fadeout 2.0 
    scene 13_0_16 with Dissolve(2.0)
    ""  
    jump scene13_00

label scene13_00:
    scene 13_0_17 with Fade(1.0,1.0,2.0)
    mc "Cozy."
    ml "You think? It's a mess, really. I keep meaning to organize, but the stall takes all my time."
    mc "You live here alone? No roommate? No... partner?"
    ml "Mhm. Still haven't found the one, as they say. Hard to meet people when you spend all day worrying about your failing business."
    scene 13_0_18 with dissolve
    ml "You can sleep there. Sorry I don't have an extra bed."
    mc "No, you've done more than enough. Thanks again, Nadia."
    ml "Don't mention it."
    scene 13_0_19 with Fade(0.5,0.5,0.5)
    sensation "The pile of blankets sinks under your weight, its warmth cradling you. Their faint floral scent make your eyelids heavier."
    ml "I'll put out the candles."
    mc "Alright. Good night, Nadia."
    scene 13_0_20 with Dissolve(2.0)
    ml "Good night."
    scene black with Fade(1.3,1.0,1.0)
    play music "nature.mp3" fadein 3.0 volume 0.5 loop
    scene 13_0_21 with Dissolve(2.0)
    perception "Sunlight spills through the window, stabbing your eyes awake. The distant chatter of market-goers mingles with the cheerful chirping of birds."
    scene 13_0_22 with Dissolve(2.0)
    mc "Ahh... *yawn*"
    scene 13_0_23 with Fade(0.5,0.5,0.5)
    mc "Morning, Nadia."
    ml "Mmmm..."
    call screen scene13_choice06 with dissolve

label scene13_choice05_op1:
    mc "You'll catch a cold like this."
    play sound "sound_effects/karma_more.mp3" volume 0.2
    if mc_karma < 10:
        $ mc_karma += 1
    $ karma_more = True
    show screen stat_change with easeinright
    scene 13_0_25 with Dissolve(1.0)
    mc "There you go."
    hide screen stat_change with easeoutright
    $ karma_more = False
    jump scene13_000

label scene13_choice05_op2:
    scene 13_0_24 with Dissolve(1.0)
    mc "..."
    play sound "sound_effects/karma_less.mp3" volume 0.2
    if mc_karma > 1:
        $ mc_karma -= 1
    $ karma_less = True
    show screen stat_change with easeinright
    mc "(I should leave before I get any ideas...)"
    impulse "You should start suckling on it like a baby."
    mc "(Yeah, like that.)"
    hide screen stat_change with easeoutright
    $ karma_less = False
    jump scene13_000

label scene13_000:
    scene 13_0_26 with Fade(1.5,0.5,0.5)
    mc "*yawn*"
    scene 13_0_27 with dissolve
    if mc_accept_helped_nadia:
        mc "(I should head back to the castle. Try to make some money from the Queen... and also talk to that Abel guy.)"
    else:
        mc "(I should head back to the castle. Try to make some money from the Queen...)"

    mc "(Ah, I forgot to tell her where I was going. Or leave a note. Or—)"
    play sound "sound_effects/clothing_rustle.mp3"
    "*rustle* *rustle*"
    mc "Huh?"
    stop music fadeout 2.0 
    scene 13_0_28 with Dissolve(1.5)
    ""
    play music "witch.mp3" fadein 3.0 loop
    scene 13_0_29 with Dissolve(1.5)
    ""
    scene 13_0_28 with Dissolve(1.5)
    mc "..."
    logic "Run."
    play sound "sound_effects/magic2.mp3"
    scene 13_0_30 with vpunch
    ""
    play sound "sound_effects/bodydrop.mp3"
    scene 13_0_31 with vpunch
    sensation "Before you could even react, your whole body turns numb. Your vision fades to black."
    stop music fadeout 2.0 
    scene black with Fade(2.0,1.0,1.0)
    scene 13_0_32 with Dissolve(1.0)
    ""
    play music "nature.mp3" fadein 1.0 loop
    scene 13_0_33 with Dissolve(1.0)
    girl "See? He's dead. We should call the guards before someone thinks we did it."
    scene 13_0_34 with dissolve
    yuuhi_ "He isn't! I just saw him breathing."
    scene 13_0_35 with dissolve
    mc "Wah!"
    scene 13_0_36 with vpunch
    mc "You! What the hell did you do to me?!"
    yuuhi_ "..."
    mc "Oh... sorry. You're not... you're not her."
    scene 13_0_38 with Fade(0.5,0.5,0.5)
    mc "Sorry about that. I thought you were someone else."
    scene 13_0_37 with dissolve
    yuuhi_ "*cough* It's fine. A-Are you alright? Should we bring a healer? You were just lying there in the middle of the alley."
    scene 13_0_38 with dissolve
    mc "There's no need for that. I think I just saw a witch... and she cast a spell on me. Knocked me out cold."
    girl "*laughs* He's weird."
    scene 13_0_37 with dissolve
    yuuhi_ "Did you say a witch? But witches aren't allowed here. The Queen banished them from the city."
    scene 13_0_38 with dissolve
    mc "Are they ever allowed anywhere? Seems like the kind of thing people say and witches ignore."
    mc "Anyway, she was dragging some poor guy with her."
    scene 13_0_37 with dissolve
    yuuhi_ "If that's really true then you should tell the guards."
    scene 13_0_38 with dissolve
    mc "I will. First thing when I get to the castle. Anyway, thanks for waking me up. What are you two doing out here?"
    scene 13_0_37 with dissolve
    yuuhi_ "I was on my way to deliver a shipment to the castle."
    scene 13_0_38 with dissolve
    mc "The castle?"
    mc "I'm going there too! Can I go with you? I still don't know my way around this city."
    scene 13_0_40 with dissolve
    stop music fadeout 2.0 
    yuuhi_ "A-Alright..."
    play music "side_event2.mp3" fadein 2.0 loop
    scene 13_0_39 with dissolve
    girl "Oooh~ I guess I'll leave you two alone, then. Take care, Yuuhi. Don't let the weird man lure you into any dark alleys."
    scene 13_0_40 with dissolve
    yuuhi_ "See you, Ria."
    scene 13_0_39 with dissolve
    scene 13_0_41 with Fade(0.5,0.5,0.5)
    yuuhi_ "Thank you for helping me carry all this."  
    yuuhi_ "But... a-are you sure you want to carry {i}all{/i} of it? I don't mind if we split them up between us. I might not look it, but I can handle myself well."  
    mc "Yeah... Don't worry. It's—ahh... light... work."  
    sensation "The crates dig into your arms with every step. Your back aches, but you force a grin."  
    yuuhi_ "Hehe~ You're so strong."
    scene 13_0_43 with Fade(1.0,1.0,2.0)
    yuuhi_ "Thanks again for helping me move this stuff... uhm..."
    scene 13_0_42 with dissolve
    mc "It's [mc]."
    scene 13_0_43 with dissolve
    yuuhi "Good to meet you, [mc]. I'm Yuuhi, at your service."  
    scene 13_0_42 with dissolve
    mc "Hey, Yuuhi. What service is that?"
    scene 13_0_43 with dissolve
    yuuhi "I'm a tailor! If you ever need new clothes, or armor repairs, or anything stitched or hemmed, you come to me."  
    yuuhi "I'll give you a discount since you helped me with the crates."
    scene 13_0_42 with dissolve
    mc "That's good to know. I might visit you one day."
    scene 13_0_43 with dissolve
    yuuhi "I look forward to that!"
    yuuhi "And umm... before you go. I saw you yesterday training in the courtyard with Captain Adam."  
    scene 13_0_42 with dissolve
    mc "Oh... that's embarrassing."  
    scene 13_0_44 with dissolve
    yuuhi "Why were you so far from the castle? *laughs* Was your fighting so abysmal they kicked you out? Did they throw you over the wall?"
    scene 13_0_45 with dissolve 
    mc "Haha, very funny. But no. I was just... taking a walk."
    scene 13_0_44 with dissolve
    yuuhi "Hehe~ Don't worry, I was only teasing."
    scene 13_0_45 with dissolve
    mc "Anyway, see you, Yuuhi. I gotta talk to the Queen."  
    scene 13_0_43 with dissolve
    yuuhi "Farewell! May your stitches never tear and your armor never rust!"  
    scene 13_0_42 with dissolve
    mc "...That's... oddly specific."
    scene 13_0_44 with dissolve  
    yuuhi "Tailor's blessing! You'll thank me later~"  
    stop music fadeout 2.0 
    scene 13_0_45 with dissolve 
    scene 13_0_46 with Fade(2.0,1.0,1.0)
    play music "nature.mp3" fadein 3.0 loop
    guard "Halt! Beyond this point lies the Queen's inner court. None may pass without leave."
    scene 13_0_47 with dissolve 
    mc "I need to see the Queen."
    scene 13_0_48 with dissolve 
    guard "Then show me your identification card and the letter of conduct. It must bear the seal of the royal chancery, approved by the clerk of the household."
    scene 13_0_47 with dissolve 
    mc "Uhh, I have the card but the letter..."
    scene 13_0_49 with dissolve 
    alice "Stand down, sergeant. This is the new recruit Her Magesty spoke for."
    scene 13_0_48 with dissolve 
    guard "As you command, Lieutenant. Pass, recruit. And mind your step in the Queen's presence."
    scene 13_0_47 with dissolve 
    mc "Thanks, Alice."
    stop music fadeout 1.0 
    scene 13_0_50 with Fade(1.0,1.0,1.0)
    play music "queen3.mp3" fadein 3.0 loop
    q "That district was {i}your{/i} responsibility, Darius."
    scene 13_0_51 with dissolve
    d "Yes, Your Majesty. I solemnly apologize. I shall—"
    scene 13_0_50 with dissolve
    q "Say it to the poor man who was kidnapped, to his family that are terrified, not me."
    q "I want her found by today. Not a second later. That witch has evaded us for too long."
    scene 13_0_52 with Dissolve(1.0)
    q "...Ah. [mc]."
    scene 13_0_53 with dissolve
    mc "Did I arrive at a bad time? I can come back later."
    d "I will do as you command, Your Majesty. The search is already underway."
    scene 13_0_52 with dissolve
    q "Halt, Darius."
    q "Adam has informed me of your training performance yesterday, [mc]. He gave me a full report this morning."
    scene 13_0_53 with dissolve
    mc "...And what did he say? Please tell me he mentioned the part where I actually hit him."
    scene 13_0_52 with dissolve
    q "That you did well. But I doubt he was fully honest. Adam has a kind heart. Too kind for a man in his position."
    q "He also mentioned you were exceptional in hand-to-hand combat. Boxing, he called it."
    scene 13_0_53 with dissolve
    mc "I think I might've had experience with boxing before... wherever I came from. It feels very familiar, like muscle memory."
    scene 13_0_52 with dissolve
    q "Hmm. A useful skill, but not enough. You still need to train with a sword."
    scene 13_0_53 with dissolve
    mc "I'm doing my best, Your Majesty."
    scene 13_0_52 with dissolve
    q "Ava also told me you show no magical potential. None whatsoever."
    scene 13_0_53 with dissolve
    mc "That's right..."
    scene 13_0_52 with dissolve
    q "However, she did sense something else—an enigma residing deep within you. Something hidden. Immense."
    q "She couldn't identify it, but she was... unsettled."
    scene 13_0_53 with dissolve
    mc "W-What do you mean? She didn't tell me any of this."
    scene 13_0_55 with Dissolve(1.0)
    q "She couldn't name it, only that it was too powerful to ignore."  
    scene 13_0_54 with dissolve
    mc "Then why didn't she tell me that herself?!"
    scene 13_0_55 with dissolve
    q "Perhaps she didn't recognize it at the time. Or perhaps she did and was too frightened to speak of it directly."  
    q "But it convinces me of one thing—you are indeed too valuable to cast aside."
    scene 13_0_54 with dissolve
    mc "(Would she really have thrown me away if I didn't have that?! I knew there was a catch. This Queen doesn't do charity.)"
    scene 13_0_55 with dissolve
    q "If you haven't heard, a young man was kidnapped recently. A baker's apprentice. The culprit is almost certainly Amelia the Witch."
    scene 13_0_54 with dissolve
    mc "Wait—I saw her! She attacked me this morning! Right after I stepped outside into the alley."  
    q "..."
    d "..."
    mc "Is something wrong? You're both looking at me like I just grew a second head."
    scene 13_0_55 with vpunch
    q "Why in the world didn't you stop her, [mc]?!"  
    scene 13_0_54 with dissolve
    mc "Stop her?! She hit me with a spell before I even moved. I blacked out on the spot."  
    mc "I didn't stand a chance."  
    scene 13_0_56 with Dissolve(1.0)
    q "*sigh* ...Then the fault is mine."  
    scene 13_0_57 with dissolve
    d "Your Majesty!? The fault fully lies with me—"  
    scene 13_0_56 with dissolve
    q "Enough, Darius. He was unprotected. If he'd been properly prepared, things might have gone differently."  
    scene 13_0_57 with dissolve
    d "..."
    scene 13_0_55 with dissolve
    q "That brings me to your first task, [mc]. You will go to the adventurers' guild and meet with Eireen."
    scene 13_0_54 with dissolve  
    mc "This is about the witch?"  
    scene 13_0_55 with dissolve
    q "Yes. I want {i}you{/i} to take responsibility for Amelia. Track her. Stop her, then bring her to justice."
    scene 13_0_54 with dissolve
    mc "Me? Did you not hear what I just said? She floored me in one second!"
    scene 13_0_55 with dissolve
    q "You were caught off guard. Next time, you won't be. And you'll have protection."  
    scene 13_0_54 with dissolve
    mc "Didn't you just say I had some hidden enigma inside me? That I was too valuable to lose? What if I die out there? What if she... turns me into a frog?"
    scene 13_0_52 with Dissolve(1.0)
    q "If you fall at the first stone, then the enigma within you was nothing but an illusion. But I don't believe that. Power must be proven, not sheltered."
    q "What good would it do me if you sat here under our protection?"
    scene 13_0_53 with dissolve
    mc "...Right. But that doesn't change the fact that she overwhelmed me instantly."
    scene 13_0_52 with dissolve
    q "Which is why, after Eireen, you will visit the Dean the blacksmith. His daughter is skilled in forging magic-resistant armor."
    q "She will craft you a set. With it, and with guidance, you will not fall so easily again."
    scene 13_0_53 with dissolve
    mc "I hope it's good enough. For my sake and yours."
    scene 13_0_58 with Dissolve(1.0)
    q "That aside, [mc]. Did you bed your wife yet?"
    scene 13_0_59 with dissolve
    mc "...Sorry?"
    scene 13_0_58 with dissolve
    q "Have you managed to put a child in her? Maia. The maid I gave you. Is she with child?"
    scene 13_0_59 with dissolve
    mc "That's... a very strange question. No. I haven't. I barely had time to spend with her."
    scene 13_0_58 with dissolve
    q "You kept me waiting so long yesterday. I assumed the two of you were rutting in the baths."
    scene 13_0_59 with dissolve
    mc "I can't just force myself on her... What if she doesn't even want it yet?"
    scene 13_0_58 with dissolve
    q "Do not speak to me of want. I gave you that girl for one reason alone: to sire strong heirs."
    q "Our population dwindles while our enemies multiply. Your wants and hers are secondary to the survival of this kingdom."
    q "Before you leave on your errand, see to her. Get her with child."
    scene 13_0_59 with dissolve
    mc "..."
    mc "As you command. But shouldn't I finish my task with the witch first?"
    scene 13_0_58 with dissolve
    q "That witch has unusual ways. She spares her captives, lets them loose after a time... though their minds are broken. A few days will not make a difference."
    q "You will also need to get your armor which will take time too."
    scene 13_0_59 with dissolve
    mc "I see. And one last thing your Majesty, where will we live after I do so? Surely you don't intend us to raise our children on the streets."
    scene 13_0_58 with dissolve
    q "If you manage this task, [mc] then I'll reward you with a place to stay. And to make up for my mistake, I'll allow you to stay with Maia for the time being."
    q "Now go. I'll have a guard escort you. Do not come back without a child in her womb."
    scene 13_0_59 with dissolve
    mc "...Got it."
    jump scene16

image queen_bj01 = Movie(play="images/1_opening/scene13/queen_bj01.webm", loop=True)
image queen_bj02 = Movie(play="images/1_opening/scene13/queen_bj02.webm", loop=True)
image queen_bj03 = Movie(play="images/1_opening/scene13/queen_bj03.webm", loop=True)

image queen_dsp01 = Movie(play="images/1_opening/scene13/queen_dsp01.webm", loop=True)
image queen_dsp01_faster = Movie(play="images/1_opening/scene13/queen_dsp01_faster.webm", loop=True)

image queen_dsp02 = Movie(play="images/1_opening/scene13/queen_dsp02.webm", loop=True)
image queen_dsp02_faster = Movie(play="images/1_opening/scene13/queen_dsp02_faster.webm", loop=True)

image queen_dsa01 = Movie(play="images/1_opening/scene13/queen_dsa01.webm", loop=True)
image queen_dsa01_faster = Movie(play="images/1_opening/scene13/queen_dsa01_faster.webm", loop=True)

image queen_dsa02 = Movie(play="images/1_opening/scene13/queen_dsa02.webm", loop=True)
image queen_dsa02_faster = Movie(play="images/1_opening/scene13/queen_dsa02_faster.webm", loop=True)

image queen_mp01 = Movie(play="images/1_opening/scene13/queen_mp01.webm", loop=True)
image queen_mp02 = Movie(play="images/1_opening/scene13/queen_mp02.webm", loop=True)

image queen_dsp03 = Movie(play="images/1_opening/scene13/queen_dsp03.webm", loop=True)
image queen_dsa03 = Movie(play="images/1_opening/scene13/queen_dsa03.webm", loop=True)


label scene13:
    $ mcname = persistent.name
    if persistent.name == "None" or mcname == "None":
        while mcname == "None" or mcname == "":
            $ mcname = renpy.input("There was an issue with your name. Please rewrite your name:", length=32)
        $ persistent.name = mcname
    if not persistent.scene4_replay:
        $ persistent.scene4_replay = True
    stop music fadeout 2.0 
    scene 12_s22 with Fade(1.0,1.0,1.0)
    mc "Your Majesty?"
    mc "Oh! You're already..."
    q "You have a habit of keeping me waiting, [mc]."
    mc "Sorry, I—"
    scene 12_s17 with Dissolve(1.0)
    q "Take off your pants."
    mc "A-Alright."
    scene 13_s1 with Fade(0.5,1.0,0.5)
    q "Impressive length, you were surely blessed!"
    scene 13_s2 with dissolve
    q "So...? Waiting for my approval?"
    q "Screw my mouth."
    show queen_bj01 with Dissolve(1.0)
    mc "(Ughh.. she's pretty good!)"
    q "Mmmghh... *slurp*"
    sensation "Her mouth devours your cock, her throat constantly contracting around your shaft as if she's trying to swallow it whole."
    scene black with Dissolve(0.3)
    show queen_bj02 with dissolve
    q "Mmhmm!"
    scene black with Dissolve(0.3)
    show queen_bj03 with Dissolve(1.0)
    sensation "Her tongue teases your frenulum relentlessly, knowing your weak spot and targeting it with precision."
    mc "(Fuck! Am I seriously going to cum already?!)"
    q "Hah~ What's wrong? Suprised by my experiance?"
    call screen scene13_choice01 with dissolve

label scene13_choice01_inside:
    mc "Hnngg...!"  
    play sound "se_sfx/blowjob/facial2.mp3" 
    scene 13_s3 with vpunch
    perception "Your cum shoots out onto her tongue, coating it thicker and whiter with each spurt."
    play sound "se_sfx/blowjob/facial3.mp3" 
    scene 13_s4 with vpunch  
    ""
    mc "Hahh..."
    scene 13_s5 with dissolve  
    "" 
    scene 13_s6 with dissolve
    play sound "se_sfx/blowjob/swallow3.mp3" 
    q "*gulp*"
    scene 13_s7 with dissolve
    q "Ahhhhhh."    
    scene 13_s8 with dissolve
    q "So much! Were you trying to impregnate my mouth?"
    q "But, we're not done yet."
    scene 13_s9 with dissolve
    mc "Huh?!"
    scene 13_s8 with dissolve
    q "I want to feel good too."
    scene 13_s9 with dissolve
    scene 13_s14 with fade
    q "Come."
    mc "(I'm fucking the Queen... Holy shit... I just realized how crazy this is.)"
    call screen scene13_choice02 with dissolve

label scene13_choice01_outside:
    mc "Hnngg...!" 
    play sound "se_sfx/blowjob/facial1.mp3" 
    scene 13_s10 with vpunch
    perception "You pull away from her endless teasing and aim at her face, thick, hot streams of your cum painting her in streaks of white."
    play sound "se_sfx/blowjob/facial2.mp3" 
    scene 13_s11 with vpunch  
    ""
    mc "Hahh..." 
    scene 13_s12 with dissolve
    q "So much! Were you trying to mark my face as yours?"
    q "But, we're not done yet."
    scene 13_s13 with dissolve
    mc "Huh?!"
    scene 13_s12 with dissolve
    q "I want to feel good too."
    scene 13_s14 with fade
    q "Come."
    mc "(I'm fucking the Queen... Holy shit! I just realized how crazy this is.)"
    call screen scene13_choice02 with dissolve

label scene13_choice02_vaginal:
    scene 13_s27 with fade
    q "Ahh~ You're stretching me so hard!"
    show queen_dsp01 with dissolve
    sensation "Her wet pussy welcomes your cock with a soft, parting kiss, enveloping you in warmth and slick pressure."
    q "Haahh~"
    q "You're so big! My womb will tear up!"
    scene black with Dissolve(0.3)
    show queen_dsp01_faster with dissolve
    q "YES! Ah~ hahh~... faster! Don't you dare slow down!"
    scene black with Dissolve(0.3)
    show queen_dsp02 with dissolve
    q "Ah~ hah~ hahh~"
    scene black with Dissolve(0.3)
    show queen_dsp02_faster with dissolve
    mc "(She's getting really tight!)"
    q "Haaahhh!!"
    play sound "se_sfx/masturbate_female/6_masturbate_cum1.mp3" 
    scene 13_s28 with vpunch
    pause 1.0
    play sound "se_sfx/masturbate_female/6_masturbate_cum1.mp3" 
    scene 13_s28 with vpunch
    q "Hah.. hah..."
    mc "(Did she just cum?)"
    scene black with Dissolve(0.3)
    show queen_dsp02 with dissolve
    q "Wait... ahhn~!"
    jump scene13_continue

default scene13_choice02_anal = False
default scene13_choice03_vagcum = False
default scene13_choice03_analcum = False

label scene13_choice02_anal:
    $ scene13_choice02_anal = True
    scene 13_s29 with fade
    q "Hmm? Are your eyes functioning properly? [mc], that's the wrong hole."
    mc "Have you never tried anal before, Your Majesty?"
    q "Well... We did experiment but it never appealed to me."
    mc "So... I cant?"
    q "*sigh* Just be gentle."
    sensation "Her ass feels impossibly tight, almost too tight. The walls of her anus gradually yield, opening up to take you in, a slow, deliberate surrender."
    scene 13_s30 with vpunch
    q "AHHHHHH!!!"
    q "You little bastard!! I told you to be gentle!"
    show queen_dsa01 with dissolve
    mc "Sorry, sorry! I was trying to push and it just... slipped. All at once."
    q "Ahh! My... ass!"
    scene black with Dissolve(0.3)
    show queen_dsa01_faster with dissolve
    q "Ah!... aah!... slower..."
    q "Angh... you're so deep!"
    scene black with Dissolve(0.3)
    show queen_dsa02 with dissolve
    q "Hngg... ah! Damn... my poor ass!"
    scene black with Dissolve(0.3)
    show queen_dsa02_faster with dissolve
    q "Slow... the hell... down!"
    q "Ahh! ah! hah~"
    jump scene13_continue

label scene13_continue:
    scene black with Dissolve(0.3)
    show queen_mp01 with Fade(0.5,0.5,0.5)
    q "Hah~ hahh~ ah~!"
    scene black with Dissolve(0.3)
    show queen_mp02 with dissolve
    ""
    scene black with Dissolve(0.3)
    show queen_dsp03 with Fade(0.5,0.5,0.5)
    q "Oh... Gods!"
    $ scene13_choice03_vagcum = True
    $ scene13_choice03_analcum = False

    $ scene13_choice03_cumbuttons = False
    $ scene13_choice03_enablebuttons = True
    call screen scene13_choice03 with dissolve

label scene13_choice03_vaginal:
    scene black with Dissolve(0.3)
    $ scene13_choice03_vagcum = True
    $ scene13_choice03_analcum = False
    show queen_dsp03 with dissolve
    hide queen_dsa03
    q "Ahnhgm~ Ahhaan~! It's so big!"
    call screen scene13_choice03 with dissolve

label scene13_choice03_anal:
    $ scene13_choice03_vagcum = False
    $ scene13_choice03_analcum = True
    scene black with Dissolve(0.3)
    if scene13_choice02_anal:
        show queen_dsa03 with dissolve
        hide queen_dsp03
        q "My ass again?!"
        q "Why?! I wanted it in my pussy!"
        q "Fuck~... you're churning up my insides!"
        call screen scene13_choice03 with dissolve

    else:
        show queen_dsa03 with dissolve
        hide queen_dsp03
        $ queen_anus_virgin = False
        q "Hey!! That's... the wrong hole!"
        q "Ah! Fuuuck!!"
        q "Slow... down!"
        q "You're tearing up my insides!"
        q "Hah! Ah! Hngg!"    
        call screen scene13_choice03 with dissolve

label scene13_choice03_analtwo:
    scene black with Dissolve(0.3)
    $ scene13_choice03_vagcum = False
    $ scene13_choice03_analcum = True
    show queen_dsa03 with dissolve
    hide queen_dsp03
    q "You're tearing me up! Gahnn~!"
    call screen scene13_choice03 with dissolve

label scene13_climax:
    if scene13_choice03_vagcum:
        if scene13_choice03_inside:
            $ queen_total_cum_in_pussy += 4.2
            mc "I'm cumming!"
            q "Ahh!"
            play sound "se_sfx/sex/sex_cum3.mp3" 
            if persistent.xray_mode:
                scene 13_s31_xray1 with vpunch
                sensation "You release deep inside her wet, seething pussy, feeling it pulse and contract around your cock, milking every last drop from you."
                play sound "se_sfx/sex/sex_cum4.mp3" 
                scene 13_s31_xray2 with vpunch
                pause 1.0
                mc "Hah... hah..."
                scene 13_s17_xray3 with Dissolve(1.0)
            else:
                scene 13_s31 with vpunch
                sensation "You release deep inside her wet, seething pussy, feeling it pulse and contract around your cock, milking every last drop from you."
                play sound "se_sfx/sex/sex_cum4.mp3" 
                scene 13_s31 with vpunch
                pause 1.0
                mc "Hah... hah..."
                scene 13_s17 with Dissolve(1.0)
            q "Huhhhh..."
            q "You ejaculated inside?!"
            mc "...Yeah?"
            q "*sigh* Well, I'm menopausal, so I don't think it will be an issue. Hopefully..."
            scene 13_s16 with dissolve
            mc "We're done though, right?"
            q "Done? We're done when {i}I{/i} say we're done. Now come, stick it in!"
            mc "Fuck..."
            $ bonus_scene2_handjob2 = True
            $ bonus_scene2_cum_first = False

            $ bonus_scene2 = False
            call screen scene13_choice04 with dissolve
        else:
            mc "I'm cumming!"
            q "Ahh!"
            play sound "se_sfx/blowjob/facial4.mp3" 
            scene 13_s22 with vpunch
            perception "You pull out from her tight pussy and aim for her back. Thick, hot streams of your seed spill out, coating her skin in glistening streaks."
            play sound "se_sfx/blowjob/facial5.mp3" 
            scene 13_s23 with vpunch
            pause 1.0
            mc "Hah... hah..."
            scene 13_s24 with dissolve
            q "Huhhhh..."
            q "Uhh... my womb will be sore for days..."
            scene 13_s26 with dissolve
            mc "We're done, right?"
            q "Done? We're done when {i}I{/i} say we're done. Now come, stick it in!"
            mc "Fuck..."
            $ bonus_scene2_handjob2 = True
            $ bonus_scene2_cum_first = False
            
            $ bonus_scene2 = False
            call screen scene13_choice04 with dissolve
    
    elif scene13_choice03_analcum:
        if scene13_choice03_inside:
            $ queen_total_cum_in_ass += 4.2
            mc "I'm cumming!"
            q "Ahh!"
            play sound "se_sfx/sex/sex_cum2.mp3" 
            scene 13_s32 with vpunch
            sensation "The heat and tightness of her ass push you to the edge, and with a groan, you release deep inside her, filling her rectum and colon completely."
            play sound "se_sfx/sex/sex_cum4.mp3" 
            scene 13_s32 with vpunch
            pause 1.0
            mc "Hah... hah..."
            scene 13_s15 with dissolve
            q "Huhhhh..."
            scene 13_s18 with dissolve
            ""
            scene 13_s15 with dissolve
            q "You ejaculated inside my anus?!"
            mc "Hah... yes..."
            q "*sigh* And why didn't you slow down when I asked you?"
            mc "..."
            q "Ugh... my anus will never be the same after this..."
            scene 13_s19 with dissolve
            mc "We're done though, right?"
            q "Done? We're done when {i}I{/i} say we're done. Now come, stick it in. This time, I want to be in my womb, preferably!"
            mc "Fuck..."
            $ bonus_scene2_handjob2 = True
            $ bonus_scene2_cum_first = False

            $ bonus_scene2 = False
            call screen scene13_choice04 with dissolve
        else:
            mc "I'm cumming!"
            q "Ahh!"
            play sound "se_sfx/blowjob/facial1.mp3" 
            scene 13_s20 with vpunch
            perception "You pull out from her tight ass and aim for her back. Thick, hot streams of your seed spill out, coating her skin in glistening streaks."
            play sound "se_sfx/blowjob/facial2.mp3" 
            scene 13_s21 with vpunch
            pause 1.0
            mc "Hah... hah..."
            scene 13_s25 with dissolve
            q "Huhhhh..."
            q "Why in the {i}hell{/i} did you insert it in my ass?!"
            mc "It was right there in front of me and I couldn't resist... sorry."
            q "Ugh! my anus will never be the same after this..."
            scene 13_s26 with dissolve
            mc "We're done, right?"
            q "Done? We're done when {i}I{/i} say we're done. Now come, stick it in. This time, I want to be in my womb, preferably!"
            mc "Fuck..."
            $ bonus_scene2_handjob2 = True
            $ bonus_scene2_cum_first = False

            $ bonus_scene2 = False
            call screen scene13_choice04 with dissolve        

label scene13_choice04_bj:
    $ bonus_scene2_cum_first = False
    $ bonus_scene2_handjob = False
    $ bonus_scene1_handjob2 = False
    $ bonus_scene1_thighjob = False
    scene black with Dissolve(0.3)
    show queen_bj01 with dissolve
    ""
    scene black with Dissolve(0.3)
    show queen_bj02 with dissolve
    call screen scene13_choice04 with dissolve

label scene13_choice04_glans:
    $ bonus_scene2_cum_first = False
    $ bonus_scene1_handjob = False
    $ bonus_scene1_handjob2 = False
    $ bonus_scene1_thighjob = False
    scene black with Dissolve(0.3)
    show queen_bj03 with dissolve
    call screen scene13_choice04 with dissolve

label scene13_choice04_ds_vaj:
    $ bonus_scene2_cum_first = False
    $ bonus_scene1_handjob = False
    $ bonus_scene1_handjob2 = False
    $ bonus_scene1_thighjob = False
    scene black with Dissolve(0.3)
    show queen_dsp01 with dissolve
    ""
    scene black with Dissolve(0.3)
    show queen_dsp02 with dissolve
    $ scene13_choice04_enablebuttons = True
    $ scene14_choice04_switch = False
    call screen scene13_choice04 with dissolve

label scene13_choice04_ds_anal:
    $ bonus_scene2_cum_first = False
    $ bonus_scene1_handjob = False
    $ bonus_scene1_handjob2 = False
    $ bonus_scene1_thighjob = False
    scene black with Dissolve(0.3)
    show queen_dsa01 with dissolve
    ""
    scene black with Dissolve(0.3)
    show queen_dsa02 with dissolve
    $ scene13_choice04_enablebuttons = True
    $ scene14_choice04_switch = False
    call screen scene13_choice04 with dissolve

label scene13_choice04_m:
    $ bonus_scene2_cum_first = False
    $ bonus_scene1_handjob = False
    $ bonus_scene1_handjob2 = False
    $ bonus_scene1_thighjob = False
    scene black with Dissolve(0.3)
    show queen_mp01 with dissolve
    ""
    scene black with Dissolve(0.3)
    show queen_mp02 with dissolve
    call screen scene13_choice04 with dissolve

label scene13_choice04_tds_vaj:
    $ bonus_scene2_cum_first = False
    $ bonus_scene1_handjob = False
    $ bonus_scene1_handjob2 = False
    $ bonus_scene1_thighjob = False
    scene black with Dissolve(0.3)
    show queen_dsp03 with dissolve
    $ scene13_choice04_enablebuttons = True
    $ scene14_choice04_switch2 = False
    call screen scene13_choice04 with dissolve

label scene13_choice04_tds_anal:
    $ bonus_scene2_cum_first = False
    $ bonus_scene1_handjob = False
    $ bonus_scene1_handjob2 = False
    $ bonus_scene1_thighjob = False
    scene black with Dissolve(0.3)
    show queen_dsa03 with dissolve
    $ scene13_choice04_enablebuttons = True
    $ scene14_choice04_switch2 = False
    call screen scene13_choice04 with dissolve

label scene14:
    if bonus_scene2_cum:
        $ bonus_scene2_cum = False
        scene black with Fade(0.5,1.0,0.5)
    else:
        scene black with Fade(0.5,1.0,0.5)
        mc "That's enough! I can't do it anymore..."
    $ renpy.end_replay()
    scene 14_s1 with dissolve
    q "...I see now that you are quite the man indeed."
    q "Not even my dear husband, may he rest in peace, could go for so long."
    q "You've earned my respect in terms of manhood."
    mc "..."
    scene 14_s2 with dissolve
    q "...Did you hear {i}any{/i} of that?"
    mc "..."
    scene 14_s3 with vpunch
    q "I'm talking to you!"
    scene 14_s4 with dissolve
    q "What's wrong?"
    scene 14_s5 with Dissolve(1.0)
    q "We'll... we'll continue this conversation later... Take a short rest."
    scene black with Fade(1.0,1.0,1.0)
    scene 14_s6 with dissolve
    play music "nature.mp3" fadein 3.0 loop
    mc "Uhh..."
    mc "Where the hell am I?"
    scene 14_s7 with dissolve
    mc "...Right."
    impulse "Look at her, sleeping so peacefully in your arms. How blissful she seems. Has she already forgotten what she did before? This bitch slapped you. Kill her. Kill her now."
    call screen scene14_choice03 with dissolve
    scene 14_s8 with fade
    mc "(Ngh... How long was I out?)"
    scene 14_s9 with dissolve
    mc "(Should I wake her? ...Nah. She's probably more tired than me. Just never the type to show it.)"
    mc "(I should head back to my room.)"
    jump scene53

label scene14_0:
    stop music fadeout 2.0 
    scene 14_s21 with Fade(0.5,1.0,0.5)
    ""
    scene 14_s10 with dissolve
    mc "(Shit, I'm already lost again... just how big is this place?!)"
    r "Aaahhh..."
    mc "(Hmm?)"
    scene 14_s11 with dissolve
    ""
    scene 14_s12 with dissolve
    r "Hhnnnhhh!"
    scene 14_s13 with dissolve
    guard "Princess."
    r "..."
    scene 14_s14 with dissolve
    ""
    scene 14_s15 with dissolve
    mc "(Ouch... It's like she's looking at a piece of trash.)"
    call screen scene14_choice01 with dissolve

label scene14_choice03_op1:
    $ persistent.mc_died_by_gaius = True
    stop music fadeout (1.0)
    logic "A distant memory surfaces of your past life. When you used to hide things beneath the bed. Secrets, tools, weapons."
    scene 14_s32 with dissolve
    sensation "Your hands fumble under the bed, brushing through layers of dust and the occasional strand of hair. Then, your fingertip grazes something. It's cold, rough, and unmistakably sharp."
    scene 14_s33 with dissolve
    ""
    play sound "sound_effects/unsheathe.mp3"
    scene black
    $ renpy.pause(2.0)
    env "In the shadowed silence of the castle room, a man stands over the sleeping Queen, a knife poised to strike. But in an instant, his motion halts. The knife slips from his hand, falling on the soft bed. Something else falls too—his head."
    scene 14_s34 with Fade(0.5,0.5,0.5)
    perception "Your vision blurs as you catch a glimpse of a figure before you. A man... clad in... iron... armor... his presence... towering... and... mer... mer... He's—"
    scene bad_ending1 with Dissolve(1.0)
    ""
    return

label scene14_choice01_peek:
    scene 14_s18 with dissolve
    mc "(Man! Just how big are they? E, F, G... or H cup?!)"
    mc "(I can understand why she might be angry all the time with that much weight on her back.)"
    r "Hey you."
    mc "(Fuck, did I get caught?)"
    jump scene14_reb

label scene14_choice01_bow:
    $ reb_love += 10
    scene 14_s30 with dissolve
    mc "Princess!"
    r "..."
    r "Hey you."
    jump scene14_reb

label scene14_reb:
    play music "reb.mp3" fadein 3.0 loop
    scene 14_s23 with dissolve
    mc "...Yeah?"
    scene 14_s22 with dissolve
    r "Tell me. What exactly is your goal here?"
    scene 14_s23 with dissolve
    mc "What do you mean?"
    scene 14_s22 with dissolve    
    r "Oh, please. Do you really think I don't know?"
    scene 14_s23 with dissolve
    mc "I seriously don't know what you're talking about."
    scene 14_s22 with dissolve 
    r "Stop acting like a dumbass. I know you're here to marry me."
    scene 14_s23 with dissolve
    mc "..."
    call screen scene14_choice04 with dissolve

label scene14_choice04_op1:
        $ mc_told_reb_harem = True
        mc "That's right. I want you, princess. You caught me."
        scene 14_s36 with dissolve
        r "I knew it! All you men are the same—do favors for my mother, impress the court, and suddenly you think you're entitled to my hand."
        scene 14_s35 with dissolve
        mc "Maybe... but I'm not just any man."
        scene 14_s36 with dissolve
        r "Oh? And what makes you so different from the hundreds who said the same thing?"
        scene 14_s35 with dissolve
        mc "For one, I'm willing to embarrass myself if it gets a smile out of you."
        scene 14_s39 with dissolve
        r "...W-What?"
        scene 14_s37 with vpunch
        mc "Look!"
        r "What in the world are you doing?! Get up before you crack your skull!"
        mc "One-arm handstand! Adam said I had good core strength. Might as well use it."
        r "What are you, a circus performer?!"
        mc "Impressive, isn't it?"
        scene 14_s38 with dissolve
        r "...Kinda."
        mc "(Oh man... I can totally see her panties like this.)"
        r "*laughs* Alright, that's enough. Get up before you break your neck."
        scene 14_s40 with dissolve
        mc "How was that, princess? Want me to carry you next? Not to brag, but I'm pretty strong."
        scene 14_s39 with dissolve
        r "Heh. I suppose you're fine... for now. At least you're entertaining, which is more than most of my suitors manage."
        scene 14_s40 with dissolve
        call screen scene14_choice05 with dissolve

label scene14_choice05_op1:
        $ mc_flirt1_reb = True
        mc "I wasn't lying when I said I want you, princess. That wasn't part of the act."
        scene 14_s39 with dissolve
        r "...You're bold, I'll give you that."
        scene 14_s40 with dissolve
        mc "Are you free sometime this week? I'd like to take you out. Not as a suitor. Just... as someone who thinks you're interesting."
        scene 14_s28 with dissolve
        r "Don't push it, [mc]."
        scene 14_s29 with dissolve
        mc "Still too early? I understand. But I won't stop coming for you. You're worth the wait."
        r "..."
        scene 14_s28 with dissolve
        r "I-I'm leaving. You have duties, I assume."
        scene 14_s29 with dissolve
        mc "Take care, princess. Sorry if I came on too strong."
        scene 14_s31 with Fade(1.0,1.0,1.0)
        mc "(Alright, back to exploring.)"
        jump scene15

label scene14_choice05_op2:
        mc "I have to leave now, princess."
        scene 14_s39 with dissolve
        r "Running already? Hmph. Fine. Don't let me keep you waiting."
        scene 14_s40 with dissolve
        scene 14_s31 with Fade(1.0,1.0,1.0)
        stop music fadeout 2.0 
        mc "(Alright, back to exploring.)"
        jump scene15

label scene14_choice04_op2:
    mc "That's not true."
    scene 14_s22 with dissolve 
    r "Stop denying it, I've seen the way you—"
    scene 14_s23 with dissolve 
    mc "I'm not denying anything. Relax, princess. Take a breath. I'm not after your hand or your throne or whatever else you think I'm scheming for."
    scene 14_s22 with dissolve 
    r "A-Are you seriously not after me? Everyone who comes to this court wants something. Usually it's me."
    scene 14_s23 with dissolve 
    mc "Swear it. Why would you think I was?"
    scene 14_s28 with dissolve 
    r "You know... everyone usually is. Since I was twelve, every visitor, every noble, every 'hero' who comes through those doors. They all want the same thing."
    scene 14_s29 with dissolve 
    mc "Don't get me wrong, you're beautiful. But maybe I don't need that kind of political baggage just yet."
    scene 14_s28 with dissolve 
    r "Tch... that's... understandable."
    r "I suppose you're fine... for now. We'll see how long that lasts."
    scene 14_s29 with dissolve 
    mc "Friends?"
    scene 14_s39 with dissolve 
    r "Don't push it, [mc]. You're not that charming."
    scene 14_s40 with dissolve 
    scene 14_s31 with Fade(1.0,1.0,1.0)
    mc "(Alright, back to exploring.)"
    jump scene15

label scene14_choice02_op1:
    $ mc_told_reb_about_sex = True
    mc "You really want me to say it?"
    r "..."
    mc "I had sex with your mom."
    scene 14_s24 with dissolve
    r "Wh—what... did you just say?" 
    mc "I—"  
    scene 14_s26 with dissolve
    r "I... {i}Nghnn...{/i} Shut up, I heard enough."  
    scene 14_s19 with vpunch
    mc "Ow!"
    scene 14_s20 with dissolve
    mc "Wait, Rebecca, listen..."
    r "No. I don't want to hear it."
    mc "(Shit... I shouldn't have said that.)"  
    r "Just... stay away from me, okay?"  
    mc "..."
    scene black with Fade(1.0,1.0,1.0)
    scene 14_s31 with dissolve
    mc "(Alright, back to exploring I guess.)"
    jump scene15

label scene14_choice02_op2:
    mc "I talked with your mother about what I should do next." 
    scene 14_s22 with dissolve
    r "Is that all what happened?"
    scene 14_s23 with dissolve
    mc "Yes."
    scene 14_s27 with dissolve
    r "*sigh* Thank the Gods..."
    mc "Something wrong?"
    scene 14_s28 with dissolve
    r "No."
    r "Just... don't make this more complicated than it needs to be."  
    scene 14_s29 with dissolve
    mc "I get it. I won't."  
    scene 14_s28 with dissolve
    r "You better..."
    scene 14_s29 with dissolve
    scene black with Fade(1.0,1.0,1.0)
    scene 14_s31 with dissolve
    stop music fadeout 3.0
    mc "(Alright, back to exploring I guess.)"

    #rebecca walks away

label scene15:
    scene black with Fade(0.5,1.0,0.5)
    play music "kitchen.mp3" fadein 2.0 loop
    scene 15_s1 with dissolve
    ""
    scene 15_s2 with dissolve
    mc "(The kitchen? I've really lost it now. How the hell did I end up in the kitchen?)"
    scene 15_s3 with dissolve
    mc "(Woah... Are those cat ears?!)"
    mc "*ahem* Hi!"
    ren_ "Look, I already told you, breakfast won't be ready until the bell rings. Some of us are actually working back here, and—"
    scene 15_s4 with dissolve
    ren_ "Oh! I'm terribly sorry, sir! Please forgive my manners! I thought you were one of the maids!"
    scene 15_s5 with dissolve
    mc "Don't worry about it."
    mc "Umm... are those ears real? I have to ask. They're just... very convincing, if they're not."
    scene 15_s6 with dissolve
    ren_ "Yes? They're real. I'm a demi-human. Beastfolk, specifically. We're not common in the citadel, or this continent in general."
    scene 15_s5 with dissolve
    mc "Can I touch them?"
    scene 15_s6 with dissolve
    ren_ "I'm... I... That's... Sir, that's quite forward..."
    scene 15_s5 with dissolve
    mc "Nevermind. Forget I asked. I can tell how uncomfortable you just got."
    scene 15_s6 with dissolve
    ren_ "T-Thank you, sir."
    ren "It's a pleasure to finally meet you. You can call me Ren. I'm one of the head cook's assistants. I specialize in pastries."
    scene 15_s5 with dissolve
    mc "You know who I am?"
    scene 15_s6 with dissolve
    ren "Yes, I heard Her Majesty talking about you yesterday. Word travels fast in a castle. She said you just... appeared out of nowhere?"  
    scene 15_s5 with dissolve
    mc "Something like that."
    scene 15_s6 with dissolve
    ren "Sounds like quite the story... but I suppose it's none of my business."
    scene 15_s5 with dissolve
    mc "Heh. Well, good to meet you too, Ren. Your ears are very... expressive."
    scene 15_s9 with dissolve
    ren "Thank you. And as I mentioned, breakfast won't be ready for a while, but if you're hungry, I can whip up something quick."
    scene 15_s10 with dissolve
    mc "No, that's not why I'm here. Actually... I'm kinda lost."
    scene 15_s7 with dissolve
    ren "*sigh* Tell me about it, sir. I've been working here for a year, and I still lose my way sometimes. This castle is like a maze. Where are you trying to go?"
    scene 15_s8 with dissolve
    mc "I'm actually trying to leave the castle."
    scene 15_s9 with dissolve
    ren "Ah, I see. Well, you're closer than you think. Right now, we're on the ground floor. Just head down the hallway you came through, turn right at the end, then take the second door on your left."  
    ren "That'll bring you to her majesty's courtroom. From there, it's a straight shot to the main entrance."
    scene 15_s10 with dissolve
    mc "Aha... Got it. Thanks a lot, Ren!"
    scene 15_s6 with dissolve
    ren "Don't mention it, sir. *giggles* Just don't get lost on your way back, eh?"  
    scene 15_s5 with dissolve
    jump scene19_0

label scene16:
    $ maia_sad = False
    $ maia_happy = True
    $ maia_love = 60
    scene black with Fade(1.0,1.0,2.0)
    stop music fadeout (3.0)
    scene 16_s1 with dissolve
    mc "(Finally... this castle is like a maze.)"  
    mc "(I guess it's intentionally built like that though? I remember learning that castles were—)"  
    m "Hnn~ Ahah~!"
    scene 16_s2 with dissolve
    mc "..."
    scene 16_s3 with dissolve
    m "Ahh~ hahh~... Dear husband! No... you're so naughty~..."
    mc "Maia?"
    scene 16_s4 with vpunch
    m "Ahh! M-Master! It's you..."
    mc "Hey, Maia. Did I catch you at a bad time?"
    scene 16_s5 with dissolve
    m "I... I'm sorry, Master. I didn't mean for you to see... I thought you were still with the Queen..."
    mc "What's wrong? tell me about it."
    scene 16_s6 with Fade(0.5,0.5,0.5)
    m "Y-yesterday when you... when we didn't... t-touch... I... My body felt... so hot after you left. I couldn't... I couldn't stop thinking about it."
    scene 16_s7 with dissolve
    m "Please, Master... I-I can't bear it anymore. I've never felt this empty. Will you... touch me? Take me? I need you inside me so badly it hurts."
    scene 16_s8 with dissolve
    call screen scene16_choice02 with dissolve

label scene16_choice02_op1:
    $ mc_maia_first_sex = True
    $ maia_virgin = False
    mc "The Queen actually told me to... impregnate you."
    scene 16_s7 with dissolve
    m "Y-Yes... I know."
    scene 16_s8 with dissolve
    mc "You knew?! And you're truly alright with this?"
    scene 16_s7 with dissolve
    m "O-Of course I am! It would be the greatest honor of my life to carry your child, Master. I have dreamed of serving my future husband in every way... but this?"
    m "To be filled by you... to swell with your heir... I would thank the Gods every morning and night for such a blessing."
    scene 16_s8 with dissolve
    mc "(She's too good at making me hard...)"
    mc "You don't have to ask twice. Come here, Maia."
    scene 16_s7 with dissolve
    m "H-Huh?"
    scene 16_s34 with vpunch
    perception "Before she can finish, you close the distance in two strides and push her back onto the bed. She yields instantly, melting beneath you with a sweet, broken moan."
    m "Mmmhn~ Master!"
    perception "Her lips part eagerly against yours, soft and sweet, her breath trembling as if she can barely contain herself."
    scene 16_s35 with dissolve
    sensation "Her warmth seeps into you, the taste of her mouth sending a shiver down your spine."
    scene 16_s36 with Dissolve(1.0)
    mc "Your lips are so soft, Maia."
    scene 16_s37 with dissolve
    m "M-Master... would it please you if I... used my mouth on you first? I want to taste you. I want to serve you properly."
    scene 16_s36 with dissolve
    mc "I'd like that. Show me how that pretty mouth feels."
    scene 16_s37 with dissolve
    m "As you wish, my Master."
    scene 16_s36 with dissolve
    jump scene27_sex

label scene16_choice02_op2:
    mc "(The Queen ordered me to impregnate her... That can wait for later. Right now...)"
    mc "I'm too tired, Maia. I helped this girl haul a big shipment and I think my back is little loose now..."
    mc "I'll just take a rest before I head out."
    scene 16_s9 with dissolve
    m "Oh... Of course, Master. I'm sorry for being so selfish. Please, rest as long as you need."
    scene 16_s10 with Fade(0.5,1.0,0.5)
    play music "fire.mp3" fadein 1.0 volume 0.5 loop
    mc "*sigh* (This is surprisingly cozy.))"
    scene 16_s11 with dissolve
    mc "(Huh?)"
    scene 16_s12 with dissolve
    mc "(This girl...)"
    scene 16_s13 with dissolve
    m "..."
    mc "(My balls are itching...)"
    scene 16_s14 with dissolve
    mc "..."
    scene 16_s15 with dissolve
    ""
    scene 16_s14 with dissolve
    ""
    scene 16_s15 with dissolve
    ""
    scene 16_s14 with dissolve
    ""
    scene 16_s15 with dissolve
    mc "(How badly is she aching? She's like a bitch in heat, barely holding herself back.)"
    call screen scene16_choice03 with dissolve

label scene16_choice03_op1:
    $ mc_calmed_maia = True
    mc "You need to calm down, Maia. I can feel how restless you are."
    scene 16_s16 with dissolve
    m "I-I'm sorry, Master. Am I bothering you?"
    scene 16_s17 with dissolve
    mc "A little. I have a long day ahead and I need to rest properly."
    scene 16_s16 with dissolve
    m "Y-Yes, Master. I apologize. I'll be quiet."
    scene 16_s17 with dissolve
    scene 16_s10 with Fade(1.0,1.0,1.0)
    mc "(I rested enough. Time to head out.)"
    m "Master?"
    scene 30_s2 with Fade(0.5,0.5,0.5)
    mc "What is it, Maia?"
    scene 30_s1 with dissolve
    m "Are you... leaving already?"
    scene 30_s2 with dissolve
    mc "Yeah. The Queen has ordered me to hunt down a witch. It won't be easy."
    scene 30_s8 with dissolve
    m "T-That's really dangerous, Master!"
    scene 30_s9 with dissolve
    mc "I know. But don't worry, I got it. Well... I hope so."
    scene 30_s8 with dissolve
    m "Please take care! I-If things get too dangerous then there's no shame in running away! Your life matters more than any hunt."
    scene 30_s9 with dissolve
    mc "*chuckles* I'll be careful. I'll see you soon, Maia."
    scene 18_s8 with dissolve
    m "Promise me you'll come back... Please."
    scene 18_s7 with dissolve
    mc "I promise."
    scene black with Fade(0.5,0.5,0.5)
    jump scene18_free_roam_main_0


label scene16_choice03_op2:
    $ mcname = persistent.name
    $ mc_punished_maia = True
    if persistent.name == "None" or mcname == "None":
        while mcname == "None" or mcname == "":
            $ mcname = renpy.input("There was an issue with your name. Please rewrite your name:", length=32)
        $ persistent.name = mcname
    if not persistent.scene5_replay:
        $ persistent.scene5_replay = True

    mc "(I wonder... just how far will she go if I push her a little?)"
    mc "Look at me, Maia."
    scene 16_s16 with dissolve
    m "Y-Yes, Master!"
    scene 16_s17 with dissolve
    mc "I'll show you my cock... but you're only allowed to look. No touching."
    mc "While you watch, you may touch yourself. That's all I'll allow for now."
    scene 16_s18 with dissolve
    m "Of course, Master! Thank you... thank you so much!"
    scene 16_s20 with dissolve
    m "Hnn~ ahh~ So big... so beautiful..."
    mc "(This is more fun than I expected.)"
    scene 16_s21 with dissolve
    ""
    scene 16_s20 with dissolve
    mc "Hey, Maia."
    scene 16_s22 with dissolve
    m "Y-yes, Master?"
    scene 16_s23 with dissolve
    mc "Tell me, Maia. What do you want me to do to you?"
    scene 16_s22 with dissolve
    m "I... I want you to have sex with me, Master... To take me hard and deep..."
    scene 16_s23 with dissolve
    mc "And?"
    scene 16_s24 with dissolve
    m "And... I want you to keep using me... as much and as often as you desire. Fill me every day if it pleases you..."
    scene 16_s25 with dissolve
    mc "Is that all?"
    scene 16_s24 with dissolve
    m "No... I want you to cum inside me... to flood me with your seed and give me lots of babies... Please, Master!"
    scene 16_s25 with dissolve
    mc "How wet is your pussy?"
    scene 16_s26 with dissolve
    m "It's leaking a lot, Master... It wants—no, it needs your cock..."
    scene 16_s27 with dissolve
    ""
    scene 16_s26 with dissolve
    m "M-Master... I'm... I'm going to—!"
    play sound "se_sfx/masturbate_female/6_masturbate_cum1.mp3"
    scene 16_s28 with vpunch
    m "HAAAAHHH!!!"
    play sound "se_sfx/masturbate_female/masturbate_cum2.mp3"
    scene 16_s28 with vpunch
    m "Hnghhhh!"
    scene 16_s29 with dissolve
    m "Hah... hah..."
    scene 16_s30 with dissolve
    m "Oh...! I'm so sorry, Master! I didn't wait for your permission to cum... I couldn't hold it..."
    scene 16_s31 with dissolve
    mc "..."
    call screen scene16_choice01 with dissolve

label scene16_choice01_op1:
    $ maia_virgin = False
    $ mc_spank_maia = True
    mc "I guess that means you need to be punished."
    play sound "sound_effects/karma_less.mp3" volume 0.2
    if mc_karma > 1:
        $ mc_karma -= 1
    $ karma_less = True
    show screen stat_change with easeinright
    m "..."
    scene 16_s30 with dissolve
    m "...Yes, Master..."
    hide screen stat_change with easeoutright
    $ karma_less = False
    scene 16_s31 with dissolve
    mc "Come here. Let's make sure you learn your lesson."
    jump scene17

label scene16_choice01_op2:
    $ mc_punished_maia = False
    mc "*chuckles* It's fine. You don't have to ask permission to cum every single time."
    mc "Just let it out when you need to."
    play sound "sound_effects/karma_more.mp3" volume 0.2
    if mc_karma < 10:
        $ mc_karma += 1
    $ karma_more = True
    show screen stat_change with easeinright
    scene 16_s32 with dissolve
    m "R-Really...? Thank you so much, Master. You're too kind to me..."
    scene 16_s33 with dissolve
    mc "Well? Feeling better now?"
    hide screen stat_change with easeoutright
    $ karma_more = False
    scene 16_s32 with dissolve
    m "Yes... so much better. Thank you for letting me ease the ache, even a little."
    scene 16_s33 with dissolve
    mc "Good. Now let me rest properly."
    scene 16_s32 with dissolve
    m "As you wish, Master!"
    scene 16_s33 with dissolve
    scene 16_s10 with Fade(1.0,1.0,1.0)
    call screen scene18_choice01 with dissolve
    mc "(I rested enough. Time to head out.)"
    m "Master?"
    scene 30_s2 with Fade(0.5,0.5,0.5)
    mc "What is it, Maia?"
    scene 30_s1 with dissolve
    m "Are you going somewhere?"
    scene 30_s2 with dissolve
    mc "I have to leave for now. The Queen tasked me with hunting down a witch."
    scene 30_s8 with dissolve
    m "T-That's really dangerous, Master!"
    scene 30_s9 with dissolve
    mc "I know. But don't worry, I got it. Well... I hope so."
    scene 30_s8 with dissolve
    m "Please take care! I-If things get too dangerous then there's no shame in running away!"
    scene 30_s9 with dissolve
    mc "*chuckles* I will. See you soon, Maia."
    scene 18_s8 with dissolve
    m "Promise me you will come back... Please."
    scene 18_s7 with dissolve
    mc "I promise."
    scene black with Fade(0.5,0.5,0.5)
    jump scene18_free_roam_main_0

label scene17:
    $ mcname = persistent.name
    scene 17_s1 with Fade(0.5,1.0,0.5)
    mc "Playing innocent earlier? I know you were teasing me with that needy body of yours."
    m "...Yes, Master."
    mc "You'll need punishment for that as well."
    m "I understand. Please punish your naughty wife, Master."
    scene 17_s2 with dissolve
    call screen scene17_choice01 with dissolve

default scene17_choice01_spankend = True
init:
    default scene17_spank_counter = 0
label scene17_choice01_spank:
    if scene17_spank_counter == 0:
        play sound "sound_effects/slap01.mp3"
        scene 17_s3 with vpunch
        m "Ah!"
        scene 17_s2 with dissolve
        $ scene17_spank_counter += 1
        call screen scene17_choice01 with dissolve

    elif scene17_spank_counter == 1:
        play sound "sound_effects/slap01.mp3"
        scene 17_s3 with vpunch
        m "Ow!"
        scene 17_s2 with dissolve
        $ scene17_spank_counter += 1
        call screen scene17_choice01 with dissolve
    
    elif scene17_spank_counter == 2:
        play sound "sound_effects/slap01.mp3"
        scene 17_s3 with vpunch
        m "Ahhh!"
        scene 17_s2 with dissolve
        $ scene17_spank_counter += 1
        call screen scene17_choice01 with dissolve
    #red = 4
    elif scene17_spank_counter == 3:
        play sound "sound_effects/slap01.mp3"
        scene 17_s5 with vpunch
        m "Owww!"
        scene 17_s4 with dissolve
        $ scene17_spank_counter += 1
        call screen scene17_choice01 with dissolve
    
    elif scene17_spank_counter == 4:
        play sound "sound_effects/slap01.mp3"
        scene 17_s5 with vpunch
        m "Master! Please... I'm sorry!"
        scene 17_s4 with dissolve
        $ scene17_spank_counter += 1
        call screen scene17_choice01 with dissolve
    
    elif scene17_spank_counter == 5:
        play sound "sound_effects/slap01.mp3"
        scene 17_s5 with vpunch
        m "Ahh~!"
        scene 17_s4 with dissolve
        $ scene17_spank_counter += 1
        call screen scene17_choice01 with dissolve
    #redder = 7
    elif scene17_spank_counter == 6:
        play sound "sound_effects/slap01.mp3"
        scene 17_s7 with vpunch
        m "AHH! Master!"
        scene 17_s6 with dissolve
        $ scene17_spank_counter += 1
        call screen scene17_choice01 with dissolve
    
    elif scene17_spank_counter == 7:
        play sound "sound_effects/slap01.mp3"
        scene 17_s7 with vpunch
        m "Hhhaahhh!"
        scene 17_s6 with dissolve
        $ scene17_spank_counter += 1
        call screen scene17_choice01 with dissolve
    
    elif scene17_spank_counter == 8:
        play sound "sound_effects/slap01.mp3"
        scene 17_s7 with vpunch
        m "Haaaahhh!"
        scene 17_s6 with dissolve
        call screen scene17_choice01 with dissolve

    
label scene17_choice01_fanus:
    if scene17_spank_counter <= 3:
        scene 17_s8 with dissolve
        m "Ah! Master!"
        mc "What?"
        m "Nothing... just p-please... be gentle..."
        play sound "se_sfx/sex/touch2.mp3" 
        scene 17_s9 with Dissolve(0.8)
        m "Nghh!"
        m "Ahh...! Master, it feels... weird..."
        play sound "se_sfx/sex/touch1.mp3" 
        scene 17_s8 with Dissolve(0.8)
        mc "Ever played with your ass before, Maia?"
        play sound "se_sfx/sex/touch2.mp3" 
        scene 17_s9 with Dissolve(0.8)
        m "Ughh... No, never..."
        play sound "se_sfx/sex/touch1.mp3" 
        scene 17_s8 with Dissolve(0.8)
        mc "I can tell. You're incredibly tight here."
        play sound "se_sfx/sex/touch2.mp3" 
        scene 17_s9 with Dissolve(0.8)
        m "Ahh!"
        play sound "se_sfx/sex/touch1.mp3" 
        scene 17_s8 with Dissolve(0.8)
        m "Ahh! Master...! It feels so strange... tingly..."
        mc "..."
        call screen scene17_choice02 with dissolve

    elif scene17_spank_counter < 7:
        scene 17_s10 with dissolve
        m "Ah! Master!"
        mc "What?"
        m "Nothing... just p-please... be gentle..."
        play sound "se_sfx/sex/touch2.mp3" 
        scene 17_s11 with Dissolve(0.8)
        m "Nghh!"
        m "Ahh...! Master, it feels... weird..."
        play sound "se_sfx/sex/touch1.mp3" 
        scene 17_s10 with Dissolve(0.8)
        mc "Ever played with your ass before, Maia?"
        play sound "se_sfx/sex/touch2.mp3" 
        scene 17_s11 with Dissolve(0.8)
        m "Ughh... No, never..."
        play sound "se_sfx/sex/touch1.mp3" 
        scene 17_s10 with Dissolve(0.8)
        mc "I can tell. You're incredibly tight here."
        play sound "se_sfx/sex/touch2.mp3" 
        scene 17_s11 with Dissolve(0.8)
        m "Ahh!"
        play sound "se_sfx/sex/touch1.mp3" 
        scene 17_s10 with Dissolve(0.8)
        m "Ahh! Master...! It feels so strange... tingly..."
        mc "..."
        call screen scene17_choice02 with dissolve
    
    elif scene17_spank_counter >= 7:
        scene 17_s12 with dissolve
        m "Ah! Master!"
        mc "What?"
        m "Nothing... just p-please... be gentle..."
        play sound "se_sfx/sex/touch2.mp3" 
        scene 17_s13 with Dissolve(0.8)
        m "Nghh!"
        m "Ahh...! Master, it feels... weird..."
        play sound "se_sfx/sex/touch1.mp3"
        scene 17_s12 with Dissolve(0.8)
        mc "Ever played with your ass before, Maia?"
        play sound "se_sfx/sex/touch2.mp3" 
        scene 17_s13 with Dissolve(0.8)
        m "Ughh... No, never..."
        play sound "se_sfx/sex/touch1.mp3"
        scene 17_s12 with Dissolve(0.8)
        mc "I can tell. You're incredibly tight here."
        play sound "se_sfx/sex/touch2.mp3" 
        scene 17_s13 with Dissolve(0.8)
        m "Ahh!"
        play sound "se_sfx/sex/touch1.mp3"
        scene 17_s12 with Dissolve(0.8)
        m "Ahh! Master...! It feels so strange... tingly..."
        mc "..."
        call screen scene17_choice02 with dissolve

label scene17_choice01_fanus_stop:
    if scene17_spank_counter <= 3:
        mc "If you're not comfortable, I can stop."
        m "Thank you, Master!"
        scene 17_s2 with dissolve
        call screen scene17_choice01 with dissolve
    
    elif scene17_spank_counter < 7:
        mc "If you're not comfortable, I can stop."
        m "Thank you, Master!"
        scene 17_s4 with dissolve
        call screen scene17_choice01 with dissolve

    elif scene17_spank_counter >= 7:
        mc "If you're not comfortable, I can stop."
        m "Thank you, Master!"
        scene 17_s6 with dissolve
        call screen scene17_choice01 with dissolve

default scene17_choice01_fingeronce = True
default keptdoinganus_dickhead = False
label scene17_choice01_fanus_keep:
    $ keptdoinganus_dickhead = True
    if scene17_spank_counter <= 3:
        play sound "se_sfx/sex/touch2.mp3" 
        scene 17_s9 with Dissolve(0.8)
        mc "Just relax."
        play sound "se_sfx/sex/touch1.mp3"
        scene 17_s8 with Dissolve(0.8)
        m "Hmfhmm!"
        play sound "se_sfx/sex/touch2.mp3" 
        scene 17_s9 with Dissolve(0.8)
        mc "There, all nice and stretched out."
        scene 17_s14 with Dissolve(0.8)
        m "Oww..."
        scene 17_s2 with dissolve
        call screen scene17_choice01 with dissolve

    elif scene17_spank_counter < 7:
        play sound "se_sfx/sex/touch2.mp3" 
        scene 17_s11 with Dissolve(0.8)
        mc "Just relax."
        play sound "se_sfx/sex/touch1.mp3"
        scene 17_s10 with Dissolve(0.8)
        m "Hmfhmm!"
        play sound "se_sfx/sex/touch2.mp3" 
        scene 17_s11 with Dissolve(0.8)
        mc "There, all nice and stretched out."
        scene 17_s14 with Dissolve(0.8)
        m "Oww..."
        scene 17_s4 with dissolve
        call screen scene17_choice01 with dissolve
    
    elif scene17_spank_counter >= 7:
        play sound "se_sfx/sex/touch2.mp3" 
        scene 17_s13 with Dissolve(0.8)
        mc "Just relax."
        play sound "se_sfx/sex/touch1.mp3"
        scene 17_s12 with Dissolve(0.8)
        m "Hmfhmm!"
        play sound "se_sfx/sex/touch2.mp3" 
        scene 17_s13 with Dissolve(0.8)
        mc "There, all nice and stretched out."
        scene 17_s14 with Dissolve(0.8)
        m "Oww..."
        scene 17_s6 with dissolve
        call screen scene17_choice01 with dissolve

label scene17_choice01_fpussy:
    if scene17_spank_counter <= 3:
        play sound "se_sfx/sex/touch3.mp3" 
        scene 17_s15 with Dissolve(0.8)
        m "Uh~..."
        play sound "se_sfx/sex/touch4.mp3" 
        scene 17_s16 with Dissolve(0.8)
        m "Ahh~... hahh~..."
        play sound "se_sfx/sex/touch3.mp3" 
        scene 17_s15 with Dissolve(0.8)
        mc "Hey, this is supposed to be a punishment. Why are you moaning?"
        play sound "se_sfx/sex/touch4.mp3" 
        scene 17_s16 with Dissolve(0.8)
        m "Y-yes, Master... I'm sorry."
        play sound "se_sfx/sex/touch3.mp3" 
        scene 17_s15 with Dissolve(0.8)
        m "Mfhm~"
        play sound "se_sfx/sex/touch4.mp3" 
        scene 17_s16 with Dissolve(0.8)
        m "Hgmm..."
        play sound "se_sfx/sex/touch3.mp3" 
        scene 17_s15 with Dissolve(0.8)
        mc "You're still doing it..."
        m "..."
        scene 17_s21 with dissolve
        mc "Maybe I need to spank you more."
        scene 17_s2 with dissolve
        call screen scene17_choice01 with dissolve

    elif scene17_spank_counter < 7:
        play sound "se_sfx/sex/touch3.mp3" 
        scene 17_s17 with Dissolve(0.8)
        m "Uh~..."
        play sound "se_sfx/sex/touch4.mp3" 
        scene 17_s18 with Dissolve(0.8)
        m "Ahh~... hahh~..."
        play sound "se_sfx/sex/touch3.mp3"
        scene 17_s17 with Dissolve(0.8)
        mc "Hey, this is supposed to be a punishment. Why are you moaning?"
        play sound "se_sfx/sex/touch4.mp3" 
        scene 17_s18 with Dissolve(0.8)
        m "Y-yes, Master... I'm sorry."
        play sound "se_sfx/sex/touch3.mp3"
        scene 17_s17 with Dissolve(0.8)
        m "Mfhm~"
        play sound "se_sfx/sex/touch4.mp3" 
        scene 17_s18 with Dissolve(0.8)
        m "Hgmm..."
        play sound "se_sfx/sex/touch3.mp3"
        scene 17_s17 with Dissolve(0.8)
        mc "You're still doing it..."
        m "..."
        scene 17_s21 with dissolve
        mc "Maybe I need to spank you more."
        scene 17_s4 with dissolve
        call screen scene17_choice01 with dissolve
    
    elif scene17_spank_counter >= 7:
        play sound "se_sfx/sex/touch3.mp3" 
        scene 17_s19 with Dissolve(0.8)
        m "Uh~..."
        play sound "se_sfx/sex/touch4.mp3"
        scene 17_s20 with Dissolve(0.8)
        m "Ahh~... hahh~..."
        play sound "se_sfx/sex/touch3.mp3"
        scene 17_s19 with Dissolve(0.8)
        mc "Hey, this is supposed to be a punishment. Why are you moaning?"
        play sound "se_sfx/sex/touch4.mp3"
        scene 17_s20 with Dissolve(0.8)
        m "Y-yes, Master... I'm sorry."
        play sound "se_sfx/sex/touch3.mp3"
        scene 17_s19 with Dissolve(0.8)
        m "Mfhm~"
        play sound "se_sfx/sex/touch4.mp3"
        scene 17_s20 with Dissolve(0.8)
        m "Hgmm..."
        play sound "se_sfx/sex/touch3.mp3"
        scene 17_s19 with Dissolve(0.8)
        mc "You're still doing it..."
        m "..."
        scene 17_s21 with dissolve
        mc "Maybe I need to spank you more."
        scene 17_s6 with dissolve
        call screen scene17_choice01 with dissolve

label scene17_continue:
    if keptdoinganus_dickhead or scene17_spank_counter > 5:
        mc "Alright, that's enough."
        $ renpy.end_replay()
        scene 17_s22 with Fade(0.5,1.0,0.5)
        m "*hic*..."
        mc "(Oh man... she's actually crying...)"
        call screen scene17_choice03 with dissolve
    
    else:
        mc "Alright, that's enough."
        $ renpy.end_replay()
        scene 16_s12 with Fade(0.5,1.0,0.5)
        mc "I hope you learned your lesson."
        scene 17_s27 with dissolve
        m "Yes, Master!"
        scene 16_s12 with dissolve
        mc "Good, you can go now."
        scene 16_s10 with Fade(1.0,1.0,1.0)
        call screen scene18_choice01 with dissolve
        mc "(I rested enough. Time to head out.)"
        m "Master?"
        scene 30_s2 with Fade(0.5,0.5,0.5)
        mc "What is it, Maia?"
        scene 30_s1 with dissolve
        m "A-Are you going somewhere?"
        scene 30_s2 with dissolve
        mc "I have to leave for now. The Queen tasked me with hunting down a witch."
        scene 30_s8 with dissolve
        m "T-That's really dangerous, Master!"
        scene 30_s9 with dissolve
        mc "I know. But don't worry, I got it. Well... I hope so."
        scene 30_s8 with dissolve
        m "Please take care! I-If things get too dangerous then there's no shame in running away!"
        scene 30_s9 with dissolve
        mc "*chuckles* I will. See you soon, Maia."
        scene 18_s8 with dissolve
        m "Promise me you will... come back."
        scene 18_s7 with dissolve
        mc "I promise."
        scene black with Fade(0.5,0.5,0.5)
        $ mc_punished_maia_little = True
        jump scene18_free_roam_main_0

label scene17_choice03_apologize:
    $ mc_apologized_maia = True
    mc "Come here..."
    scene 17_s23 with vpunch
    m "No, Master! Please! No more!"
    scene 17_s24 with dissolve
    mc "Hey, hey... Calm down. I'm not going to hurt you."
    scene 17_s26 with Fade(0.5,1.0,0.5)
    mc "I... I admit I went too far. That wasn't fair to you. I'm sorry."
    m "...*hic*"
    mc "I'll make it up to you, okay? I promise."
    scene 17_s25 with dissolve
    m "No, Master... *sniff* You don't have to..."
    scene 17_s26 with dissolve
    mc "That won't do. I'll get you something when I'm out. Something nice."
    scene 17_s25 with dissolve
    m "*sniff* Thank you... Master."
    scene 17_s26 with dissolve
    mc "I want you to be smiling now."
    scene 17_s25 with dissolve
    m "A-Alright... *sniff*"
    scene 17_s26 with dissolve
    scene 16_s10 with Fade(1.0,1.0,1.0)
    call screen scene18_choice01 with dissolve
    mc "(I rested enough. Time to head out.)"
    m "Master?"
    scene 30_s2 with Fade(0.5,0.5,0.5)
    mc "What is it, Maia?"
    scene 30_s1 with dissolve
    m "A-Are you going somewhere?"
    scene 30_s2 with dissolve
    mc "I have to leave for now. The Queen tasked me with hunting down a witch."
    scene 30_s8 with dissolve
    m "T-That's really dangerous, Master!"
    scene 30_s9 with dissolve
    mc "I know. But don't worry, I got it. Well... I hope so."
    scene 30_s8 with dissolve
    m "Please take care! I-If things get too dangerous then there's no shame in running away!"
    scene 30_s9 with dissolve
    mc "*chuckles* I will. See you soon, Maia."
    scene 18_s8 with dissolve
    m "Promise me you will... come back."
    scene 18_s7 with dissolve
    mc "I promise."
    scene black with Fade(0.5,0.5,0.5)
    jump scene18_free_roam_main_0
    
label scene17_choice03_go:
    $ mc_apologized_maia = False
    mc "You can go now."
    mc "I hope you learned your lesson."
    m "...*hic*"
    scene 16_s10 with Fade(1.0,1.0,1.0)
    call screen scene18_choice01 with dissolve
    mc "(I rested enough. Time to head out.)"
    jump scene18_free_roam_main_0

label scene18_free_roam_main_0:
    $ in_free_roam = True
    $ current_objective = "7th of Reed: \n\nA lot's happened in the last two days. The biggest \nthing? I'm married. Yeah, just like that, apparently \nI'm a married man now. The girl the Queen picked \nfor me is... interesting. \n\nShe's incredibly agreeable, maybe too agreeable. \nI swear, if I asked her to jump off the castle \nroof, she'd probably do it without a second thought. \nI don't know how to feel about that. Aside from the \nqueen basically forcing me work for her, things \nhave been going pretty well. I've got a wife, maybe \neven a place in the castle. Not bad for someone \nwho had nothing a few days ago. \n\nOh, and the Queen's daughter... insanely hot, but \nshe's definitely got that bratty attitude. Hopefully \nshe doesn't end up making my life harder."
    scene 18_s1 with dissolve

    if not karma_updated:
        $ karma_updated = True
        if mc_karma >= 100:
            $ mc_karma = 10
        elif mc_karma >= 90:
            $ mc_karma = 9
        elif mc_karma >= 80:
            $ mc_karma = 8
        elif mc_karma >= 70:
            $ mc_karma = 7
        elif mc_karma >= 60:
            $ mc_karma = 6
        elif mc_karma >= 50:
            $ mc_karma = 5
        elif mc_karma >= 40:
            $ mc_karma = 4
        elif mc_karma >= 30:
            $ mc_karma = 3
        elif mc_karma >= 20:
            $ mc_karma = 2
        elif mc_karma >= 10:
            $ mc_karma = 1
        else:
            $ mc_karma = 1
    if mc_karma > 10:
        $ mc_karma = 10
    if mc_karma < 1:
        $ mc_karma = 1
    call screen scene18_free_roam with dissolve

label scene18_free_roam_main:
    $ current_objective = "Current Objective: Leave the room or talk to Maia first."
    if mc_punished_maia_little:
        $ maia_sad = False
        $ maia_happy = True
        $ maia_love = 60
    elif not mc_punished_maia:
        $ maia_happy = True
        $ maia_sad = False
        $ maia_love = 70
    elif mc_punished_maia and not mc_apologized_maia:
        $ maia_happy = False
        $ maia_sad = True
        $ maia_love = 40
    elif mc_punished_maia and mc_apologized_maia:
        $ maia_sad = False
        $ maia_happy = True
        $ maia_love = 60

    $ in_scene18 = True
    $ all_options = True

    scene 18_s1 with dissolve
    call screen scene18_free_roam with dissolve

label scene18_free_roam_left:
    scene 18_s4 with dissolve
    call screen scene18_free_roam_up2 with dissolve

label scene18_free_roam_right:
    scene 18_s2 with dissolve
    call screen scene18_free_roam_right with dissolve

label scene18_free_roam_up:
    if scene18_poster:
        scene 18_s3_2 with dissolve
    else:
        scene 18_s3 with dissolve
    call screen scene18_free_roam_up with dissolve

label scene18_free_roam_poster:
    $ persistent.maia_render1 = True
    play sound "sound_effects/render_unlock.mp3"
    $ renpy.notify("You unlocked a special render!")
    $ scene18_poster = False
    jump scene18_free_roam_up

label scene18_free_roam_up2:
    if scene18_coin:
        scene 18_s5_2 with dissolve
    else:
        scene 18_s5 with dissolve
    call screen scene18_free_roam_up3 with dissolve

label scene18_free_roam_coin:
    $ mc_coin += 5
    $ renpy.notify("You found 5 bronze coins!")
    play sound "sound_effects/coin_collect.mp3"
    $ scene18_coin = False
    jump scene18_free_roam_up2

default in_scene18 = False
label scene18_free_roam_maia:
    mc "(I'll spend time with her later. I should head to the guild for now.)"
    call screen scene18_free_roam_up3 with dissolve

label scene18:
    call screen scene18_free_roam_end with dissolve
    jump scene18_free_roam_left


label scene19:
    $ maia_hj = False
    $ maia_tj = False
    $ maia_bj = False
    $ maia_sex = False
    $ maia_fj = False

    $ is_maia_bj3_second = True
    if scene18_coin:
        scene 18_s5_2 with Fade(1.0,1.0,1.0)
    else:
        scene 18_s5 with Fade(1.0,1.0,1.0)
    mc "(Time to go.)"
    $ maia_hj = False
    $ maia_tj = False
    $ maia_bj = False
    $ maia_sex = False
    $ maia_fj = False
    stop music fadeout 2.0
    scene black with Fade(1.0,1.0,1.0)
    play music "queen.mp3" fadein 2.0 loop
    scene 19_s9 with dissolve
    ""
    scene 18_s17 with dissolve
    q "Double the patrols near the southern districts. A lack of complaints doesn't mean there's no trouble—just that it's being hidden."
    guard "Understood, Your Majesty."
    scene 18_s18 with fade
    q "Ah, there you are. Already tired of wandering my halls?"
    scene 18_s19 with dissolve
    mc "Sorry for leaving like that, I just wanted to explore the castle."
    mc "Also... I hope this doesn't come off as rude..."
    scene 18_s18 with dissolve
    q "Oh? Please, don't hold back. I do so love honesty."
    scene 18_s19 with dissolve
    mc "You didn't seem particularly concerned about sleeping next to a man you barely knew..."
    scene 18_s18 with dissolve
    q "Tell me, do you think power comes from paranoia or control?"
    scene 18_s19 with dissolve
    mc "What?"
    scene 18_s18 with dissolve
    q "If I feared every unknown, I would be a prisoner in my own castle. True control is knowing the outcome before the game even begins."
    q "Had you drawn a blade against me last night, you would not have left that bed alive. Gaius was standing at the door the entire time."
    scene 18_s20 with dissolve
    mc "Gaius...? Oh. That guy..."
    mc "I figured he was a guard, but I didn't think—"
    q "—That he would end your life before you so much as sheathe your blade?"
    scene 18_s18 with dissolve
    q "Let this be a lesson, hero. The powerful do not gamble with their safety—they ensure the odds are always in their favor."
    q "But enough about last night. I have no use for a man who only looks backward. I need you to go see Eireen—she will tell you what comes next."
    scene 18_s19 with dissolve
    mc "Alright. Where is she?"
    scene 18_s18 with dissolve
    q "You really are lost, aren't you?"
    scene 18_s19 with dissolve
    mc "...Were you testing me this whole time?"
    scene 18_s18 with dissolve
    q "Testing? No. Confirming."
    q "Darius is outside the courtroom. Go. And try not to be a disappointment."
    if mc_asked_wed_reb:
        q "After all, you want to wed my daughter, no?"
        scene 18_s19 with dissolve
        mc "..."
    else:
        scene 18_s19 with dissolve
        mc "..."
    $ got_map = True
    scene 19_s1 with Fade(0.5,1.0,1.0)
    stop music fadeout 3.0

label scene19_0:
    $ mc_marital = "married"
    $ mc_card_reg = True
    $ mc_job = "royal_servant"
    $ mc_residency = "castle"
    $ in_free_roam = False
    stop music fadeout 2.0 
    scene 19_s10 with Fade(1.5,1.0,1.0)
    d "Ah, there you are. Hold up a moment, will you? I've been looking for you."
    play music "nature.mp3" fadein 1.0 loop
    scene 19_s2 with dissolve
    mc "Darius? What are you doing here?"
    scene 19_s1 with dissolve
    d "What am I doing here? I work here, [mc]."
    scene 19_s2 with dissolve
    mc "Right... but I meant {i}right now.{/i}"
    scene 19_s1 with dissolve
    d "*chuckles* I can tell by that look on your face you're lost. You've had the same expression since the moment I met you."
    scene 19_s2 with dissolve
    mc "...You're not wrong. I just got directions from a cat eared cook in the kitchen."
    scene 19_s1 with dissolve
    d "Which is why I'll be giving you this."
    scene 19_s3 with dissolve
    ""
    scene 19_s4 with dissolve
    d "Here. A map of the city. It's about time you learned the layout of Irda. You'll be moving around a lot, and it's better if you can stand on your own without relying on others."
    scene 19_s5 with dissolve
    ""
    scene 19_s2 with dissolve
    mc "Alright... looks straightforward enough. Thank you, Darius."
    scene 19_s1 with dissolve
    d "I've circled the adventurers' guild. Familiarize yourself with it. Trust me, you'll thank me later when you don't have to ask directions every five steps."
    scene 19_s6 with dissolve
    d "Oh, and I took care of your paperwork. Your citizenship card's been registered and updated. You're officially an Irdan now."
    scene 19_s7 with dissolve
    mc "No way, seriously? You just saved me hours of waiting at some government office."
    scene 19_s6 with dissolve
    d "*chuckles* It's my pleasure. And do take care of yourself out there."
    d "Especially with your task."  
    scene 19_s7 with dissolve
    mc "I'll take care of it."
    scene 19_s6 with dissolve
    d "I trust that you will. Her Majesty's orders can be harsh, but the reward is always worth it."  
    scene 19_s7 with dissolve
    mc "I hope so. Got nowhere else to go to if this doesn't work out."  
    scene 19_s6 with dissolve
    d "Then make sure it does. I'll be rooting for you, [mc]."  
    d "Farewell for now."  
    scene 19_s7 with dissolve
    scene 19_s8 with Fade(0.5,0.5,0.5)
    play sound "sound_effects/paperOpen.mp3"
    show screen scene19_choice01 with dissolve
    mc "(Okay so... this is the castle. And the guild is... past the citadel and the commercial district.)"
    mc "(Shit. That's really far.)"
    mc "(*sigh* Guess I better start walking.)"
    hide screen scene19_choice01 with dissolve

label scene20:
    $ in_scene18 = False
    stop music fadeout (3.0)
    scene black with fade
    scene 20_s1 with Fade(0.5,1.0,1.5)
    ""
    scene 20_s2 with dissolve
    mc "(This should be the place.)"
    scene 20_s3 with Fade(0.5,1.0,0.5)
    play music "guild.mp3" fadein 2.0 loop
    mc "(Oh, this definitely looks like a guild!)"
    scene 20_s4 with fade
    mc "(Alright, time to see what this place is all about.)"
    scene 20_s5 with dissolve
    mc "(An elven adventurer and his party... or is that his harem? The way those girls are looking at him, it could go either way.)"
    scene 20_s6 with dissolve
    mc "(Oh, It's Ava... and isn't that the girl I ran into before with Darius? The mercenary who lost Reiner's daughter.)"
    scene 20_s7 with dissolve
    mc "(And that guy in the corner... What's his deal? He still looks like a statue.)"
    scene 20_s8 with dissolve
    mc "(Alright, I think I've got a good read on everyone here. Time to make a move.)"
    scene 20_s4 with dissolve
    call screen scene20_choice01 with dissolve

label scene20_choice01_op1:
    scene 20_s21 with Fade(0.5,0.5,0.5)
    mc "Hello."
    perception "Before you stands a man—too beautiful, almost unnaturally so. The perfect image of a hero. The same can't be said for the two women beside him."
    empathy "That's not nice. No one chooses how they look when they're born."
    scene 20_s20 with dissolve
    orym_ "Ah, welcome! You must be the one everyone's been whispering about. The mysterious stranger who appeared out of nowhere."
    scene 20_s21 with dissolve
    mc "I guess? What exactly are they saying?"
    scene 20_s20 with dissolve
    orym_ "Oh, you know... word is you took down the ogre. Quite the feat, really. People can't stop talking about it."
    scene 20_s21 with dissolve
    mc "It's a long story. Not as impressive as the rumors make it sound."
    scene 20_s20 with dissolve
    orym_ "Oh, I'm sure. Must've been quite the spectacle, though. A single man against a beast that killed seasoned hunters? That's the stuff of ballads."
    orym "I'm Orym, by the way. And these lovely ladies here are Dana and Suzan."
    scene 20_s21 with dissolve
    mc "Nice to meet you."
    scene 20_s22 with dissolve
    dana "Hey."
    scene 20_s23 with dissolve
    suzan "Heeyyy~ You're cuter than I expected. The rumors didn't mention that part."
    scene 20_s20 with dissolve
    orym "So, what brings you to the guild today? Looking for another thrilling battle? Maybe another ogre to wrestle? Or perhaps something more... exotic?"
    scene 20_s21 with dissolve
    mc "I'm here to see Eireen. Just talking to people for now."
    scene 20_s20 with dissolve
    orym "Ah, gathering information, are we? Smart. You never know what juicy tidbits you might pick up in casual conversation."
    orym "Though, if you're hoping for some deep wisdom from Eireen, you might have better luck waiting until she's in a good mood. A rare occurrence, I might add."
    scene 20_s21 with dissolve
    mc "I'll take my chances."
    scene 20_s20 with dissolve
    orym "Fair enough. Just don't keep her waiting too long—she's not the most patient person. Then again, neither am I, so I completely understand."
    scene 20_s22 with dissolve
    dana "You're always talking, Orym. Let the man breathe. He didn't come here for a lecture."
    scene 20_s20 with dissolve
    orym "Hey, conversation is an art, Dana. Some of us are just better at it. It's not my fault I'm gifted."
    scene 20_s24 with dissolve
    suzan "You mean you just like hearing your own voice."
    scene 20_s25 with dissolve
    orym "*chuckles* That too."
    mc "Right. Well, good talking to you."
    scene 20_s20 with dissolve
    orym "Likewise. Let's do it again sometime—maybe after your next {i}grand{/i} adventure?"
    scene 20_s21 with dissolve
    scene 20_s4 with Fade(0.5,0.5,0.5)
    $ mc_talked_orym = True
    call screen scene20_choice01 with dissolve

label scene20_choice01_op2:
    if kat_pervert:
        scene 20_s10 with Fade(0.5,0.5,0.5)
        kat_ "It's the pervert!"
        scene 20_s16 with dissolve
        ava "Pervert?"
        scene 20_s17 with dissolve
        mc "Oh... That."
        mc "I was hoping you'd forgotten."
        scene 20_s12 with dissolve
        kat_ "It's fine. You're not the first guy to stare, and you won't be the last. At least you had the decency to look embarrassed about it."
        scene 20_s10 with dissolve
        kat_ "I'm Katherine. But you can call me Kat."
        kat "Sorry for not recognizing you back then. You're quite the man, eh?"
    else:
        scene 20_s12 with Fade(0.5,0.5,0.5)
        kat_ "It's you!"
        scene 20_s16 with dissolve
        ava "Hello, [mc]. It's good to see you again."
        scene 20_s17 with dissolve
        mc "Hey, Ava. And you were the one talking to Darius before, right? About Reiner's daughter? I never got your name properly."
        scene 20_s12 with dissolve
        kat_ "Katherine. But call me Kat."
        scene 20_s10 with dissolve
        kat "Sorry for not recognizing you back then. You're quite the man, eh?"
    scene 20_s11 with dissolve
    if mc_lied:
        mc "Ahaha... Thanks. It was nothing, really."
    elif mc_truth:
        mc "It's not what you think. A cage just so happened to fall on the ogre's head and—"
        scene 20_s13 with dissolve
        kat "A... cage? Is that some kind of summoning spell?"
        scene 20_s14 with dissolve
        ava "No."
    scene 20_s10 with dissolve
    kat "You know, I tried fighting an ogre once. Years ago, when I was young and stupid. Damn near got myself killed. If not for my girl here, I'd be ogre chow."
    scene 20_s13 with dissolve
    kat "Or maybe just dead? ...Do ogres eat people?"
    scene 20_s14 with dissolve
    ava "Yes. How do you not know that?"
    scene 20_s13 with dissolve
    kat "Hah! Guess I never stuck around long enough to find out."
    scene 20_s15 with dissolve
    kat "And oh, where are my manners. This here is Ava—my partner in crime. We've been working together for... what, three years now?"
    scene 20_s16 with dissolve
    ava "We've already met. I checked him for mana yesterday. At the castle."
    scene 20_s10 with dissolve
    kat "Ohhh~ And what did you find? Is he secretly a powerful mage? A devil in disguise?"
    scene 20_s16 with dissolve
    ava "It's... complicated. But I think there's something inside him. Not mana, but something else. I can't explain it."
    scene 20_s11 with dissolve
    mc "I wanted to ask you about that! When the Queen told me, I thought she was exaggerating. Is this really true? There's something... inside me?"
    scene 20_s16 with dissolve
    ava "Not entirely. What I saw is {i}really{/i} difficult to explain."
    scene 20_s10 with dissolve
    kat "Then I guess you'll find out the hard way one day, huh?"
    kat "Anyway, what'd the Queen give you? You're all official now, right?"
    scene 20_s17 with dissolve
    mc "She put me to work... and gave me a maid girl. Who also happens to be my wife now."
    scene 20_s10 with dissolve
    kat "Lucky bastard! A wife {i}and{/i} a job?"
    scene 20_s18 with dissolve
    mc "By the way, who's that person over there?"
    scene 20_s7 with dissolve
    kat "Forget it. Trying to make friends with Gaius is hopeless."
    mc "Why's that?"
    kat "No idea. Doesn't talk to anyone. And even if you did try to talk to him, he wouldn't respond. It's like he's in his own little world."
    mc "Strange..."
    scene 20_s10 with dissolve
    kat "Well, it was nice meeting ya! If you ever need a hand—or, you know, an ogre bait—you know where to find me."
    scene 20_s11 with dissolve
    mc "*laughs* I'll keep that in mind."
    scene 20_s4 with Fade(0.5,0.5,0.5)
    $ mc_talked_kat_first = True
    if mc_talked_eireen:
        jump scene21
    call screen scene20_choice01 with dissolve

label scene20_choice01_op3:
    scene 20_s26 with Fade(0.5,0.5,0.5)
    mc "Hey."
    scene 20_s27 with dissolve
    "..."
    mc "I saw you with the Queen. Are you like her bodyguard?"
    scene 20_s26 with Dissolve(1.0)
    mc "Not in the mood for a chat?"
    "..."
    mc "Does it not get hot in that suit all day?"
    "..."
    mc "Alright then... tough crowd."
    scene 20_s4 with Fade(0.5,0.5,0.5)
    $ mc_talked_gaius = True
    call screen scene20_choice01 with dissolve

label scene21:
    $ mc_talked_eireen = True
    if not mc_talked_kat_first:
        scene 20_s19 with dissolve
        kat_ "Oh!"
        mc "Hmm?"
        jump scene20_choice01_op2
    scene 20_s19 with dissolve
    ""
    scene 21_s1 with dissolve
    mc "You Eireen?"
    scene 21_s2 with dissolve
    eireen "Ah, you must be the one the Queen mentioned. [mc], right?"
    scene 21_s1 with dissolve
    mc "That's me. Got something for me?"
    scene 21_s2 with dissolve
    eireen "I do. And it's important, so listen up."
    eireen "We have been getting more and more reports of a witch kidnapping merchants or citizens who were unlucky enough to cross her path."
    eireen "But recently, she overstepped her boundaries—she abducted a man right here in our city, in broad daylight."
    scene 21_s1 with dissolve
    mc "I know. I was there when it happened. Do you know where she is?"
    scene 21_s2 with dissolve
    eireen "For once, yes. One of the men she released was lucid enough to describe her hideout."
    eireen "It took some coaxing, but we got a location out of him. She's holed up in the old king's forest, north of the citadel."
    scene 21_s1 with dissolve
    mc "How dangerous is she?"
    scene 21_s7 with dissolve
    eireen "She's not to be taken lightly. She doesn't kill her victims, that's the one mercy she seems to have, but that won't comfort you if she breaks your mind instead."
    scene 21_s8 with dissolve
    mc "*sigh* That doesn't sound promising."
    scene 21_s2 with dissolve
    eireen "Weren't you the one who slayed an ogre? This should be nothing in comparison."
    scene 21_s1 with dissolve
    if mc_lied:
        mc "But..."
        empathy "Maybe if you finally admitted the truth, they'd stop expecting so much from you."
        impulse "Or maybe shut up and prove them wrong. Nobody respects cowards."
    if mc_truth:
        mc "But I didn't... It was..."
        impulse "Just shut up and prove them wrong. Stop making excuses and do the job."
    mc "..."
    mc "Fine. I'll do it."
    scene 21_s14 with dissolve
    eireen "That's the spirit."
    scene 21_s15 with dissolve
    mc "Can I talk to the man who escaped? I want more details before I walk into this."
    scene 21_s14 with dissolve
    eireen "Well... you see, he's not in the best state of mind right now. Poor guy looks completely broken—shut himself off from everyone."
    eireen "Just sits in the corner of the infirmary and... masturbates. A lot."
    scene 21_s15 with dissolve
    mc "Masturbates?!"
    scene 21_s14 with dissolve
    eireen "Weird, I know. He just can't stop for some reason, but even after hearing that, it is absolutely crucial that you bring her back alive. Got it?"
    scene 21_s15 with dissolve
    mc "Alive. Got it."
    scene 21_s14 with dissolve
    eireen "Oh! And don't forget to swing by the blacksmith, Dean, before you head out. The Queen ordered custom armor and a sword for you."
    eireen "It's magically reinforced. Should give you some protection against Amelia's spells."
    scene 21_s8 with dissolve
    mc "Finally. I was getting tired of wearing rags."
    scene 21_s7 with dissolve
    eireen "Be careful, [mc]. Tasks like this are normally reserved for seasoned veterans with years of experience under their belts."
    eireen "But Her Majesty personally vouched for you. That is the {i}only{/i} reason I agreed to assign this mission."
    eireen "Do not make the Queen regret her faith in you. And do not make me regret listening to her."
    scene 21_s8 with dissolve
    mc "(Whoa... she's surprisingly kind.)"
    jump scene22

    eireen "Two days ago, lord Reiner got his daughter kidnapped by bandits while they were riding in the forest nearby."
    scene 21_s1 with dissolve
    mc "Bandits. Classic."
    scene 21_s5 with dissolve
    eireen "..."
    mc "Go on..."
    scene 21_s3 with dissolve
    eireen "Anyway... strange thing is, they didn't take any coin. Just her. Left her father with a nasty gash on his cranium, though."
    eireen "We sent out scouts, but they came back with nothing. Not a trace."
    scene 21_s1 with dissolve
    mc "Weird. No ransom demand?"
    scene 21_s2 with dissolve
    eireen "None so far."
    scene 21_s1 with dissolve
    mc "So where do I come in?"
    scene 21_s2 with dissolve
    eireen "You're going to find her. Lord Reiner isn't the kind of man you want to disappoint."
    scene 21_s1 with dissolve
    mc "If he's that important then why aren't more people looking for her?"
    eireen "There are. You're not the only one looking however if you manage to find her yourself you'll get the majority of the reward."
    mc "Any leads at least?"
    scene 21_s9 with dissolve
    eireen "Well... no one wants to say it outright, but some folks think she went to see the Queen of pleasure."
    scene 21_s4 with vpunch
    mc "Queen of pleasure?!"
    scene 21_s10 with dissolve
    eireen "Shhhhh!"
    mc "..."
    scene 21_s3 with dissolve
    eireen "But yes... The girl was... let's just say, not your typical noble's daughter."
    scene 21_s4 with dissolve
    mc "Ahuh... So, where do I find this... Queen?"
    scene 21_s2 with dissolve
    eireen "Hold on, I have a map of the place somewhere here."
    scene 21_s11 with dissolve
    eireen "Or was it here?"
    scene 21_s12 with dissolve
    eireen "No, not this one..."
    eireen "There you are!"
    scene 21_s13 with dissolve
    eireen "Here, The location is already marked."
    scene 21_s8 with dissolve
    mc "Got it. Is there... anything I should be worried about?"
    scene 21_s2 with dissolve
    eireen "Not really. The Queen of pleasure isn't hostile. She should be very understanding of our situation."
    eireen "Your job's simple. Go there, ask questions, and find out what she knows. If she's involved, bring the girl back. Alive."
    scene 21_s1 with dissolve
    mc "Got it."
    scene 21_s7 with dissolve
    eireen "Oh! One last thing—the Queen ordered custom armor and a sword for you. Swing by the blacksmith, Dean, before you head out."
    scene 21_s8 with dissolve
    mc "Finally, I was getting tired from wearing these rags."
    scene 21_s7 with dissolve
    eireen "That's all, try not to get yourself killed, hero~"
    scene 21_s8 with dissolve
    if mc_truth:
        mc "(Stop calling me that...)"
    elif mc_lied:
        mc "Got it."
    stop music fadeout (3.0)

label scene22:
    scene 22_s1 with Fade(0.5,1.0,1.5)
    mc "(Alright. Next stop, the blacksmith. Should be behind the market.)"
    scene 22_s2 with Fade(0.5,1.0,0.5)
    ""
    scene 22_s3 with fade
    play music "blacksmith.mp3" fadein 2.0 loop
    mc "*cough*... *cough*..."
    scene 22_s4 with dissolve
    mc "Hey! I'm [mc]. Eireen sent me."
    play sound "sound_effects/blacksmith_hit.mp3"
    scene 22_s5 with dissolve
    ""
    scene 22_s4 with dissolve
    ""
    play sound "sound_effects/blacksmith_hit.mp3"
    scene 22_s5 with dissolve
    mc "Hello...?"
    scene 22_s4 with dissolve
    ""
    play sound "sound_effects/blacksmith_hit.mp3"
    scene 22_s5 with dissolve
    ""
    scene 22_s4 with dissolve
    dean "Flame... Oh, flame..."
    play sound "sound_effects/blacksmith_hit.mp3"
    scene 22_s5 with dissolve
    mc "..."
    scene 22_s4 with dissolve
    mc "*ahem*! Excuse me! Mr. Dean?"
    scene 22_s6 with dissolve
    mc "...Do I go there?"
    scene 22_s5 with dissolve
    ""
    scene 22_s4 with dissolve
    ""
    play sound "sound_effects/blacksmith_hit.mp3"
    scene 22_s5 with dissolve
    mc "Right... Good talk."
    scene 22_s4 with dissolve
    mc "*sigh* Alright then..."
    stop music fadeout (3.0)
    scene 22_s7 with fade
    play music "yuuhi.mp3" fadein 2.0 volume 0.1 loop
    yuuhi "[mc]!"
    yuuhi "Welcome! Please come over and meet me on the other side of the counter."
    scene 22_s8 with dissolve
    mc "Hey, Yuuhi."
    scene 22_s9 with dissolve
    yuuhi "It's crazy, you actually made it past my Pops!"
    scene 22_s8 with dissolve
    mc "Huh? Is that a big deal?"
    scene 22_s10 with dissolve
    yuuhi "Oh, absolutely! He only lets the truly worthy step into his shop. The bravest warriors. The most legendary heroes. The ones destined for greatness~!"
    scene 22_s11 with dissolve
    mc "Really? Well... Guess I've got some potential after all."
    scene 22_s12 with dissolve
    yuuhi "Pfft, hahaha! Just kidding."
    scene 22_s10 with dissolve
    yuuhi "I just say that to everyone who comes through the wrong door. You were supposed to use the side door!"
    scene 22_s13 with dissolve
    mc "..."
    scene 22_s9 with dissolve
    yuuhi "Sorry, sorry! I'm sure you {i}do{/i} have potential."
    scene 22_s8 with dissolve
    jump scene22_choice01_funny

label scene22_choice01_angry:
    $ mc_screamed_yuuhi = True
    scene 22_s15 with vpunch
    stop music fadeout (1.0)
    mc "Go get me my armor, now."
    scene 22_s16 with dissolve
    yuuhi "Oh! Uh... it isn't ready yet, sir."
    scene 22_s15 with dissolve
    mc "Aren't ready?"
    scene 22_s16 with dissolve
    yuuhi "Y-yes, sir. We still have to take your measurements and all."
    scene 22_s15 with dissolve
    mc "How long will making my clothes take? I've got an important mission to get to."
    scene 22_s16 with dissolve
    yuuhi "About three days, sir."
    scene 22_s15 with dissolve
    mc "Well, let's get it over with."
    scene 22_s16 with dissolve
    yuuhi "Yes, sir! This way, please."
    jump scene23

label scene22_choice01_funny:
    mc "..."
    scene 22_s9 with dissolve
    yuuhi "Haha..."
    scene 22_s8 with dissolve
    mc "Look, Eireen mentioned you have some equipment ready?"
    scene 22_s9 with dissolve
    yuuhi "Oh, about that..."
    scene 22_s8 with dissolve
    mc "What's wrong?"
    scene 22_s9 with dissolve
    yuuhi "Nothing's wrong. I just need to take some measurements first. The armor has to be fitted precisely to your body, or it won't move right."
    yuuhi "Pops is forging the base plates, but I handle all the custom fitting and finishing work."
    scene 22_s8 with dissolve
    mc "Measurements? Fine. Let's get it over with."
    scene 22_s9 with dissolve
    yuuhi "This way, please."
    scene 22_s8 with dissolve
    stop music fadeout (3.0)
    jump scene23

label scene23:
    scene 23_s1 with Fade(0.5,1.0,0.5)
    yuuhi "Please undress whenever you feel comfortable."
    yuuhi "Down to your undergarments is fine. I need accurate measurements of your shoulders, chest, arms, and waist."
    scene 23_s2 with dissolve
    mc "Alright."
    scene 23_s3 with fade
    ""
    call screen scene23_choice03 with dissolve

label scene23_choice03_op1:
    yuuhi "Are you done?"
    mc "Yep. Ready when you are."
    scene 23_s30 with dissolve
    yuuhi "Alright! Let's begin. Don't worry, this won't take long."
    scene 23_s8 with Dissolve(1.0)
    sensation "Her touch is light but precise. The measuring tape snaps lightly against your skin as she notes each measurement in a small leather notebook."
    scene 23_s9 with Dissolve(1.0)
    ""
    scene 23_s7 with Dissolve(1.0)
    ""
    scene 23_s14 with dissolve
    yuuhi "Lastly, your hips and legs..."
    scene 23_s31 with dissolve
    ""
    scene 23_s32 with dissolve
    ""
    scene 23_s33 with dissolve
    yuuhi "And that's all! You can get dressed now. I have everything I need."
    scene 23_s34 with dissolve
    mc "You're pretty good at this!"
    scene 23_s33 with dissolve
    yuuhi "Thank you! I take my work seriously. Pops forges the metal, but I make sure it actually fits the person who's going to wear it."
    scene 23_s34 with dissolve
    scene 23_s35 with Fade(0.5,1.0,0.5)
    mc "How much do I owe you? Hopefully you accept debts..."
    scene 23_s36 with dissolve
    yuuhi "Don't worry about that, [mc]. It's already covered by the Queen. You won't have to pay a single gold."
    scene 23_s35 with vpunch
    mc "Gold?!"
    scene 23_s36 with dissolve
    yuuhi "Mhm. All in all, something like this would normally cost eleven gold and seven silver."
    yuuhi "Magic-resistant armor isn't cheap—especially when we weave actual runes into the plates."
    scene 23_s35 with dissolve
    mc "She's really betting on me, isn't she?"
    scene 23_s36 with dissolve
    yuuhi "She must see something in you. Or she's desperate. Either way, you get the best armor I've ever made. Lucky you~"
    scene 23_s35 with dissolve
    mc "So, how long till the armor's finished?"
    scene 23_s36 with dissolve
    yuuhi "Three days at most."
    scene 23_s35 with dissolve
    mc "Three days? Poor guy has to hang in there until then, I guess."
    scene 23_s21 with dissolve
    yuuhi "Poor guy? Who are you talking about?"
    scene 23_s23 with dissolve
    mc "The witch I told you about this morning, when you woke me up in the street. I've been tasked to hunt her down."
    mc "Apparently I'm the most suitable person in the kingdom for the job..."
    scene 23_s21 with dissolve
    yuuhi "So it {i}was{/i} real?"
    scene 23_s23 with dissolve
    mc "You really thought I was just lying there for no reason?"
    scene 23_s21 with dissolve
    yuuhi "That explains why the Queen requested magic-resistant plating."
    scene 23_s23 with dissolve
    mc "I also heard you're good at this... that wasn't just a compliment, was it?"
    scene 23_s17 with dissolve
    yuuhi "Of course not! My armor is the best in all of Irda! Pops taught me everything he knows, and I've improved on half his techniques."
    scene 23_s18 with dissolve
    mc "*chuckles* I'll take your word for it. Thanks, Yuuhi. See you in three days."
    scene 23_s36 with dissolve
    yuuhi "See you, [mc]!"
    scene 23_s15 with dissolve
    yuuhi "I-I mean... I wouldn't mind if you stopped by before then. You know... Just to say hi. The forge gets lonely with just me and Pops."
    scene 23_s16 with dissolve
    mc "Why? You think you'll finish it faster if I hover around?"
    scene 23_s15 with dissolve
    yuuhi "N-No, that's not what I meant!"
    scene 23_s16 with dissolve
    mc "Then what did you mean?"
    scene 23_s15 with dissolve
    yuuhi "F-Forget it! I have work to do!"
    scene 23_s16 with dissolve
    scene black with fade
    scene 26_s1 with Fade(1.0,1.0,1.0)
    play music "gameplay_night.mp3" fadein 3.0 loop
    mc "*sigh*..."
    mc "(Ever since I came to this world, I've had this faint sense of dread...)"
    scene 29_1_s52 with Fade(1.0,1.0,1.0)
    ""
    jump scene29

label scene23_choice03_op2:
    $ mc_take_off_pants_yuuhi = True
    play sound "sound_effects/clothing_rustle2.mp3"
    scene 23_s4 with dissolve
    yuuhi "Are you done?"
    mc "Yep."
    scene 23_s5 with vpunch
    yuuhi "Ahhh! [mc], you didn't need to remove {i}everything{/i}!"
    play sound "sound_effects/karma_less.mp3" volume 0.2
    if mc_karma > 1:
        $ mc_karma -= 1
    $ karma_less = True
    show screen stat_change with easeinright
    mc "Hey, these clothes don't come with underwear. I was wearing pants right over my junk."
    scene 23_s6 with dissolve
    yuuhi "Enhh... Uh... Well... you didn't have to remove your pants too..."
    $ karma_less = False
    hide screen stat_change with easeoutright
    yuuhi "L-Let's finish up quickly, then. Before my Pops walks in..."
    scene 23_s8 with Dissolve(1.0)
    sensation "Her touch is light but precise. The measuring tape snaps lightly against your skin as she notes each measurement in a small leather notebook."
    scene 23_s9 with Dissolve(1.0)
    ""
    scene 23_s7 with Dissolve(1.0)
    ""
    scene 23_s14 with dissolve
    yuuhi "Lastly, your hips and legs..."
    scene 23_s10 with dissolve
    yuuhi "{size=30}Oh God...{/size} *gulp*"
    scene 23_s11 with dissolve
    yuuhi "{size=30}Keep it together, Yuuhi..."
    scene 23_s12 with dissolve
    yuuhi "A-And that's all! You can get dressed now... please wear your pants back."
    scene 23_s13 with dissolve
    mc "You're pretty good at this!"
    scene 23_s12 with dissolve
    yuuhi "Thanks..."
    scene 23_s13 with dissolve
    scene 23_s35 with Fade(0.5,1.0,0.5)
    mc "How much do I owe you? Hopefully you accept debts..."
    scene 23_s36 with dissolve
    yuuhi "Don't worry about that, [mc]. It's already covered by the Queen. You won't have to pay a single gold."
    scene 23_s35 with vpunch
    mc "Gold?!"
    scene 23_s36 with dissolve
    yuuhi "Mhm. All in all, something like this would normally cost eleven gold and seven silver."
    yuuhi "Magic-resistant armor isn't cheap—especially when we weave actual runes into the plates."
    scene 23_s35 with dissolve
    mc "She's really betting on me, isn't she?"
    scene 23_s36 with dissolve
    yuuhi "She must see something in you. Or she's desperate. Either way, you get the best armor I've ever made. Lucky you~"
    scene 23_s35 with dissolve
    mc "So, how long till the armor's finished?"
    scene 23_s36 with dissolve
    yuuhi "Three days at most."
    scene 23_s35 with dissolve
    mc "Three days? Poor guy has to hang in there until then, I guess."
    scene 23_s21 with dissolve
    yuuhi "Poor guy? Who are you talking about?"
    scene 23_s23 with dissolve
    mc "The witch I told you about this morning, when you woke me up in the street. I've been tasked to hunt her down."
    mc "Apparently I'm the most suitable person in the kingdom for the job..."
    scene 23_s21 with dissolve
    yuuhi "So it {i}was{/i} real?"
    scene 23_s23 with dissolve
    mc "Mhm."
    scene 23_s21 with dissolve
    yuuhi "That explains why the Queen requested magic-resistant plating."
    scene 23_s23 with dissolve
    mc "I also heard you're good at this... that wasn't just a compliment, was it?"
    scene 23_s17 with dissolve
    yuuhi "Of course not! My armor is the best in all of Irda! Pops taught me everything he knows, and I've improved on half his techniques."
    scene 23_s18 with dissolve
    mc "*chuckles* I'll take your word for it. Thanks, Yuuhi. See you in three days."
    scene 23_s36 with dissolve
    yuuhi "See you, [mc]!"
    scene 23_s15 with dissolve
    yuuhi "I-I mean... I wouldn't mind if you stopped by before then. You know... Just to say hi. The forge gets lonely with just me and Pops."
    scene 23_s16 with dissolve
    mc "Why? You think you'll finish it faster if I hover around?"
    scene 23_s15 with dissolve
    yuuhi "N-No, that's not what I meant!"
    scene 23_s16 with dissolve
    mc "Then what did you mean?"
    scene 23_s15 with dissolve
    yuuhi "F-Forget it! I have work to do!"
    scene 23_s16 with dissolve
    scene black with fade
    scene 26_s1 with Fade(1.0,1.0,1.0)
    play music "gameplay_night.mp3" fadein 3.0 loop
    mc "*sigh*..."
    mc "(Ever since I came to this world, I've had this faint sense of dread...)"
    scene 29_1_s52 with Fade(1.0,1.0,1.0)
    ""
    jump scene29

label scene23_choice02_op2:
    mc "Sorry but no, I'm not interested in you."
    scene 23_s22 with dissolve
    yuuhi "Right! Of course... Haha..."
    scene 23_s23 with dissolve
    mc "Well, I'll be going now."
    scene 23_s21 with dissolve
    yuuhi "S-stay safe out there..."
    scene black with Fade(0.5,1.0,0.5)
    yuuhi "{size=30}Stupid! Stupid! Stupid!"
    jump scene26


label scene23_choice02_sure:
    scene 23_s15 with Fade(1.0,1.0,1.0)
    yuuhi "Now... take your pants off."
    scene 23_s16 with dissolve
    mc "Aww... you really want me to take off my armor already?"
    scene 23_s15 with dissolve
    yuuhi "[mc]!"
    scene 23_s16 with dissolve
    mc "Sorry, sorry. I just love teasing you."
    scene 23_s15 with dissolve
    yuuhi "Stop... Stop making fun of me..."
    scene 23_s16 with dissolve
    mc "But you're so cute when you're flustered."
    yuuhi "..."
    mc "Here. Pants off."
    scene 23_s24 with dissolve
    yuuhi "Oh-ho! Would you look at that! It seems I forgot a very important detail—silly me..."
    scene 23_s25 with dissolve
    mc "Which is...?"
    scene 23_s26 with dissolve
    yuuhi "Your... c-cock, [mc]. It needs to be measured as well. That's why your pants were fitting so tightly!"
    scene 23_s25 with dissolve
    mc "Really? First time I've heard of that."
    scene 23_s27 with dissolve
    yuuhi "Ahuh... And if you get, uh, erect during battle? It would be extra uncomfortable, no?"
    scene 23_s28 with dissolve
    mc "Erect during battle?! What kind of psycho do you think I am?"
    scene 23_s27 with dissolve
    yuuhi "I-It could happen unconditionally, too!"
    scene 23_s28 with dissolve
    mc "Hmm... you've got a point."
    scene 23_s27 with dissolve
    yuuhi "See! So will you... uhm... get hard so I can... accurately take the measurement?"
    scene 23_s28 with dissolve
    mc "It's kinda hard to do on command without any stimulation, you know."
    scene 23_s29 with dissolve
    yuuhi "Ah yes! I suppose that is correct!"
    yuuhi "D-Do you... want me to do something to make it easier?"
    scene 23_s28 with dissolve
    mc "Hmm... I don't know."
    scene 23_s27 with dissolve
    yuuhi "H-How about my breasts!? Breasts will surely get you erect!"
    scene 23_s28 with dissolve
    mc "You're so smart."

default yuuhi_lookchest = True
default yuuhi_lookass = False
default yuuhi_lookfeet = False
default yuuhi_lookass_first = True
default yuuhi_fingeranus_first = True
default yuuhi_fingerpussy_first = True
default yuuhi_lookfeet_first = True
default yuuhi_touchedfoot = False
default yuuhi_touchedfoot_first = True
default yuuhi_feettouch_first = True
default start_wiggle = False
default yuuhi_lick_first = True

label scene24:
    $ mcname = persistent.name
    if persistent.name == "None" or mcname == "None":
        while mcname == "None" or mcname == "":
            $ mcname = renpy.input("There was an issue with your name. Please rewrite your name:", length=32)
        $ persistent.name = mcname
    if not persistent.scene6_replay:
        $ persistent.scene6_replay = True
    scene 24_s1 with Fade(0.5,1.0,0.5)
    yuuhi "H-here!"
    yuuhi "Y-You c-can... touch, if you w-want."
    if not interact_indicator:
        $ interact_indicator = True
        call screen interact_tutorial with Dissolve(0.3)
    scene 24_s2 with dissolve
    call screen scene24_choice01 with dissolve

label scene24_choice01_lookchest:
    scene 24_s2 with dissolve
    call screen scene24_choice01 with dissolve

label scene24_choice01_lookass:
    if yuuhi_lookass_first:
        scene 24_s7 with dissolve
        yuuhi "H-how does my butt look?"
        mc "Looks sexy."
        scene 24_s8 with dissolve
        yuuhi "You can... put your finger in my butt, [mc]... I-if you want of course! And don't worry, it's clean..."
        mc "What about your pussy?"
        yuuhi "You can, but please not too deep... I'm saving myself until we get married."
        mc "Is that so? You're really gonna make me wait like that?"
        yuuhi "I'm really sorry, but... it's my Pops. He wouldn't allow it. When we get married... then you can take my virginity."
        yuuhi "Haha..."
        mc "You were really straightforward, asking me like that."
        yuuhi "Sorry... It's just that I don't really talk with guys like you, [mc]. Or guys my age in general."
        yuuhi "I don't know how these things normally go..."
        mc "No worries. I don't either."
        $ yuuhi_lookass_first = False
        $ yuuhi_saw_choice = True
        call screen scene24_choice02 with dissolve
    else:
        scene 24_s8 with dissolve
        call screen scene24_choice01 with dissolve

label scene24_choice02_op1:
    $ mc_told_yuuhi_maia = True
    mc "By the way... I already have a wife."
    yuuhi "H-Huh?! But you look so young."
    mc "Thanks. Do you have any issue with that?"
    yuuhi "Umm... It's fine I think. My Pops also has two wives."
    mc "Alright. Good."
    call screen scene24_choice02 with dissolve
label scene24_choice02_op2:
    mc "Why do you want to get married so badly?"
    yuuhi "It's very important to get married, [mc]! Did you know that only thirty percent of the women in our city are married?"
    mc "That low?"
    yuuhi "Terrible isn't it?! Most girls never even get a chance!"
    empathy "There's something she's not saying—something more personal behind her words."
    mc "Is that really the only reason?"
    yuuhi "I... I don't want to be alone, [mc]. I've always felt ignored by men..."
    yuuhi "Ever since school, and even now as an adult."
    mc "I see."
    call screen scene24_choice02 with dissolve
label scene24_choice02_op4:
    call screen scene24_choice01 with dissolve

label scene24_choice01_lookfeet:
    if yuuhi_lookfeet_first:
        scene 24_s10 with dissolve
        ""
        scene 24_s11 with dissolve
        yuuhi "Are... my feet really enough to get you hard, [mc]?"
        scene 24_s12 with dissolve
        mc "Oh, absolutely."
        $ yuuhi_lookfeet_first = False
        call screen scene24_choice01 with dissolve
    else:
        scene 24_s12 with dissolve
        call screen scene24_choice01 with dissolve

label scene24_rightbob:
    scene 24_s5 with dissolve
    yuuhi "Nnhh~"
    scene 24_s6 with dissolve
    yuuhi "Ahhh!"
    sensation "You pinch her nipple, and she jolts immediately. It feels firm yet soft under your touch."
    yuuhi "D-Don't pinch too hard... They're really sensitive."
    scene 24_s2 with dissolve
    call screen scene24_choice01 with dissolve

label scene24_leftbob:
    scene 24_s3 with dissolve
    yuuhi "Ahh~"
    perception "Her breasts aren't the largest you've seen, but they're perky, beautifully shaped, and perfectly fill your hand."
    scene 24_s4 with dissolve
    yuuhi "Mmmfm~"
    yuuhi "It feels really good~!"
    scene 24_s2 with dissolve
    call screen scene24_choice01 with dissolve

image yuuhi_fingeranus01 = Movie(play="images/2_chapter1/scene24/yuuhi_fingeranus01.webm", loop=True)
image yuuhi_fingerpussy01 = Movie(play="images/2_chapter1/scene24/yuuhi_fingerpussy01.webm", loop=True)
image yuuhi_feet01 = Movie(play="images/2_chapter1/scene24/yuuhi_feet01.webm", loop=True)
image yuuhi_feet02 = Movie(play="images/2_chapter1/scene24/yuuhi_feet02.webm", loop=True)
image yuuhi_jerkoff01 = Movie(play="images/2_chapter1/scene25/yuuhi_jerkoff01.webm", loop=True)

label scene24_choice03_anus:
    if yuuhi_fingeranus_first:
        scene 24_s9 with dissolve
        yuuhi "Nghh..."
        show yuuhi_fingeranus01 with dissolve
        hide yuuhi_fingerpussy01
        hide yuuhi_feet01
        yuuhi "Ahh... ngh..."
        mc "Are you okay?"
        yuuhi "Nghhh... I'm fine. It just feels strange having someone else touch me there..."
        sensation "You can feel her clenching hard around your finger, her body shuddering each time you push deeper."
        yuuhi "Ahnh~!"
        $ yuuhi_fingeranus_first = False
        call screen scene24_choice01 with dissolve
    else:
        show yuuhi_fingeranus01 with dissolve
        hide yuuhi_fingerpussy01
        hide yuuhi_feet01
        yuuhi "Nghh..."
        perception "Her body reacts intensely. She's clearly enjoying the attention on her ass despite her embarrassment."
        yuuhi "Ahnh~!"
        call screen scene24_choice01 with dissolve

label scene24_choice03_pussy:
    if yuuhi_fingerpussy_first:
        scene 24_s20 with dissolve
        yuuhi "Uhhh~..."
        show yuuhi_fingerpussy01 with dissolve
        hide yuuhi_fingeranus01
        hide yuuhi_feet01
        yuuhi "N-Not, Ahh~... Not too deep, Ah~... [mc]."
        sensation "Your finger is instantly coated in her warm wetness. She's absolutely dripping, whether from nervousness or genuine arousal, her body is responding eagerly to your touch."
        $ yuuhi_fingerpussy_first = False
        yuuhi "Mhmmm~"
        call screen scene24_choice01 with dissolve
    else:
        show yuuhi_fingerpussy01 with dissolve
        hide yuuhi_fingeranus01
        hide yuuhi_feet01
        yuuhi "Mhmmm~"
        yuuhi "{size=30}Yes, please~!{/size} Ahh~"
        call screen scene24_choice01 with dissolve

label scene24_feet:
    if yuuhi_touchedfoot_first:
        scene 24_s13 with dissolve
        mc "So soft..."
        scene 24_s22 with dissolve
        yuuhi "I take very good care of my feet, [mc]. I have to. Standing in the forge all day makes them ache if I don't."
        scene 24_s13 with dissolve
        $ yuuhi_touchedfoot_first = False
        call screen scene24_choice01 with dissolve
    else:
        scene 24_s13 with dissolve
        call screen scene24_choice01 with dissolve
        

label scene24_wiggle:
    show yuuhi_feet01 with dissolve
    hide yuuhi_fingeranus01
    hide yuuhi_fingerpussy01
    call screen scene24_choice01 with dissolve

label scene24_lick:
    if yuuhi_lick_first:
        scene 24_s14 with dissolve
        sensation "You run your tongue slowly along her arch. The taste is faintly salty with a warm, musky scent that makes your cock throb."
        yuuhi "Hah! [mc]! ...You're actually licking my foot!"
        scene 24_s15 with dissolve
        mc "Mhmm... Tashtes good."
        sensation "She wasn't lying—those soles are some of the softest you've ever felt. The scent of her feet drives you wild, getting you even harder than you thought possible."
        show yuuhi_feet02 with dissolve
        hide yuuhi_fingerpussy01
        hide yuuhi_fingeranus01
        hide yuuhi_feet01
        $ yuuhi_lick_first = False
        call screen scene24_choice01 with dissolve
    else:
        show yuuhi_feet02 with dissolve
        yuuhi "Hehe~"
        hide yuuhi_fingerpussy01
        hide yuuhi_fingeranus01
        hide yuuhi_feet01
        call screen scene24_choice01 with dissolve

label scene25:
    scene 25_s1 with fade       
    yuuhi "I-Is your penis hard now, [mc]?"
    scene 25_s2 with dissolve
    mc "Rock solid, thanks to your sexy body."
    scene 25_s1 with dissolve
    yuuhi "P-Perfect! Let's get started then..."
    scene 25_s3 with dissolve
    ""
    scene 25_s4 with dissolve
    mc "..."
    mc "Yuuhi?"
    mc "Yuuhi!"
    scene 25_s5 with vpunch
    yuuhi "Ah! I'm so sorry! I was..."
    scene 25_s6 with dissolve
    yuuhi "*ahem* W-we're done!"
    scene 25_s7 with dissolve
    mc "Finally."
    scene 25_s6 with dissolve
    yuuhi "By the way, [mc]..."
    scene 25_s7 with dissolve
    mc "What is it?"
    scene 25_s6 with dissolve
    yuuhi "I heard it's... not good for a man to stay like that after getting hard for so long. It can cause discomfort... or so I've been told."
    scene 25_s7 with dissolve
    mc "What do you propose?"
    scene 25_s6 with dissolve
    yuuhi "You know... You should let... your semen out."
    scene 25_s7 with dissolve
    mc "Ah..."
    scene 25_s5 with dissolve
    yuuhi "You can... let it out if you want! I-I don't mind!"
    scene 25_s8 with dissolve
    yuuhi "Ahhhhhhh~"
    mc "(Woah... Is she really inviting me to cum in her mouth?!)"
    mc "(This girl is freakier than I thought.)"
    show yuuhi_jerkoff01 with Dissolve(1.0)
    show screen delayed_sound_loop("se_sfx/rubbing4.mp3", delay=1.5)   
    call screen scene25_choice01 with dissolve

default scene25_choice02_swallow = False
default scene25_choice02_spit = False
default yuuhi_cuminside01 = False
default yuuhi_cumoutside01 = False
label scene25_choice01_inside:
    $ yuuhi_cuminside01 = True
    $ yuuhi_cumoutside01 = False
    hide screen delayed_sound_loop
    mc "HNNGGG!!"
    play sound "se_sfx/blowjob/facial2.mp3" 
    scene 25_s13 with vpunch
    ""
    play sound "se_sfx/blowjob/facial3.mp3" 
    scene 25_s14 with vpunch
    ""
    scene 25_s15 with dissolve
    mc "Hah... Wow, that was a lot."
    yuuhi "Ewww... It tashets horribre!"
    call screen scene25_choice02 with dissolve

label scene25_choice01_inside2:
    if scene25_choice02_swallow:
        $ yuuhi_total_cum_in_mouth += 4.1
        mc "You must swallow it."
        yuuhi "Why?!"
        mc "It's... I heard it's good for your health!"
        yuuhi "Rearry?"
        mc "Yep. Or so I've been told."
        yuuhi "O-Ogay..."
        scene 25_s16 with dissolve
        play sound "se_sfx/blowjob/swallow1.mp3" 
        yuuhi "*gulp*... *gag*..."
        yuuhi "*gulp* *gulp*"
        mc "Show me."
        scene 25_s17 with dissolve
        yuuhi "Ahhhh."
        mc "Good girl."
    if scene25_choice02_spit:
        mc "You can spit it out."
        yuuhi "Tshank you."
        scene 25_s18 with dissolve
        yuuhi "Ptoo..."
    $ renpy.end_replay()
    jump scene25_climax

label scene25_choice01_outside:
    $ yuuhi_cumoutside01 = True
    $ yuuhi_cuminside01 = False
    hide screen delayed_sound_loop
    mc "HNNGGG!!"
    play sound "se_sfx/blowjob/facial2.mp3" 
    scene 25_s11 with vpunch
    ""
    play sound "se_sfx/blowjob/facial3.mp3" 
    scene 25_s12 with vpunch
    ""
    $ renpy.end_replay()
    jump scene25_climax

label scene25_climax:
    if yuuhi_cuminside01:
            scene 25_s21 with Fade(0.5,1.0,0.5)
            mc "I guess we're done here."
            yuuhi "Mhmm..."
            scene 25_s22 with dissolve
            yuuhi "[mc]... you're going out to fight this witch, aren't you?"
            scene 25_s21 with dissolve
            mc "I am. Why? Worried about me?"
            scene 25_s23 with dissolve
            yuuhi "Of course I am! You're my boyfriend, not some wandering hero in a novel."
            scene 25_s26 with dissolve
            mc "Don't worry. If I die, I'll leave you all my riches... which amount to—"
            scene 25_s23 with dissolve
            yuuhi "That's not funny!"
            scene 25_s26 with dissolve
            mc "Alright, alright, I'm sorry. I promise I'll come back to you, safe and sound."
            scene 25_s23 with dissolve
            yuuhi "You better..."
            scene 25_s26 with dissolve
            mc "...Because if I don't, I know you'll haunt me in the afterlife."
            scene 25_s22 with dissolve
            yuuhi "*laughs* That's right!"
            scene 25_s21 with dissolve
            jump scene32_2

    elif yuuhi_cumoutside01:
            scene 25_s19 with Fade(0.5,1.0,0.5)
            mc "I guess we're done here."
            yuuhi "Mhmm..."
            scene 25_s20 with dissolve
            yuuhi "[mc]... you're going out to fight this witch, aren't you?"
            scene 25_s19 with dissolve
            mc "I am. Why? Worried about me?"
            scene 25_s24 with dissolve
            yuuhi "Of course I am! You're my boyfriend, not some wandering hero in a novel."
            scene 25_s25 with dissolve
            mc "Don't worry. If I die, I'll leave you all my riches... which amount to—"
            scene 25_s24 with dissolve
            yuuhi "That's not funny!"
            scene 25_s25 with dissolve
            mc "Alright, alright, I'm sorry. I promise I'll come back to you, safe and sound."
            scene 25_s24 with dissolve
            yuuhi "You better..."
            scene 25_s25 with dissolve
            mc "...Because if I don't, I know you'll haunt me in the afterlife."
            scene 25_s20 with dissolve
            yuuhi "*laughs* That's right!"
            scene 25_s19 with dissolve
            jump scene32_2

default scene26_choice01_accept = False
default scene26_choice01_refuse = False
default scene26_choice02_accept = False
default scene26_choice02_refuse = False
default scene26_choice03_sex = False
default scene26_choice03_smile = False
default scene26_choice04_sex = False
default scene26_choice04_busy = False

label scene26:
    scene black with fade
    scene 26_s2 with Fade(1.0,1.0,1.0)
    mc "(Phew... that was quite the walk. I should probably start using [horse] more often.)"
    play music "fire.mp3" fadein 1.0 loop
    scene 26_s3 with dissolve
    m "Oh! [mx]!"
    scene 26_s4 with Dissolve(1.5)
    m "Welcome home, [mx]! Did you take care of the witch?"
    scene 26_s5 with dissolve
    mc "I did. She was... weird. Not what I expected a witch to be."
    scene 26_s4 with dissolve
    m "Good. Good... I-I'm glad you're safe."
    scene 26_s5 with dissolve
    mc "Something wrong? You're fidgeting around... more than usual."
    scene 26_s4 with dissolve
    m "Umm... I have something to tell you. Y-You might be angry, but please don't be angry."
    scene 26_s5 with dissolve
    mc "You can trust me, Maia. Whatever it is, we'll figure it out."
    scene 26_s4 with dissolve
    m "I-I want to introduce you to Crumps!"
    m "He's been hiding under the bed all day because he knows he did something bad, but I think if you meet him properly, y-you'll understand!"
    scene 26_s8 with dissolve
    m "Come here, baby. It's okay. [mx] isn't going to hurt you."
    scene 26_s7 with dissolve
    play sound "sound_effects/meow.mp3"
    crumps "Mao."
    scene 26_s6 with dissolve
    m "He's my cat! Princess Rebecca gave him to me as a gift when I first came here..."
    scene 26_s9 with dissolve
    mc "That was nice of her. I didn't expect the princess to be so thoughtful. What's the problem then?"
    scene 26_s10 with dissolve
    m "Soo... Crumps did something bad. Something Her Majesty is very, very angry about."
    m "He broke Her Majesty's favorite vase... The one from king Nathaniel of Eurina."
    scene 26_s11 with dissolve
    mc "That's what cats do, I guess. They knock things over. It's practically their job."
    scene 26_s10 with dissolve
    m "A-And now she told me to get rid of him... She said if I didn't, she'd have the stablehands take him to the woods."
    m "He'd be all alone out there! He doesn't know how to hunt on his own, he'd starve!"
    scene 26_s13 with dissolve
    m "Well... U-Unless I keep him here. W-With us! In our quarters!"
    m "Soo, [mx]! Can we please keep him here? Please? I'll clean up after him. I'll make sure he doesn't break anything else."
    m "I promise he won't do anything like that anymore! Please, please, please! I don't want to get rid of him, [mx]!"
    m "I love him so, so much! He's my best friend! Besides the princess. And you!"
    scene 26_s12 with dissolve
    call screen scene26_choice01 with dissolve
    if scene26_choice01_accept:
        $ mc_didnt_accept_crumps = False
        $ karma_more = False
        if mc_karma < 10:
            $ mc_karma += 1
        if not mc_punished_maia:
            $ maia_love = 80
        else:
            $ maia_love = 70
        $ mc_accepted_crumps_first = True
        mc "Sure, I don't mind. The little fella can stay."
        scene 26_s25 with dissolve
        m "R-r-really?! You mean it?"
        play sound "sound_effects/karma_more.mp3" volume 0.2
        $ karma_more = True
        show screen stat_change with easeinright
        scene 26_s26 with dissolve
        mc "Yup. Someone's got to keep the mice out of the castle. And he's clearly important to you. How could I say no to that face?"
        scene 26_s27 with vpunch
        m "Thank you, thank you, thank you!"
        hide screen stat_change with easeoutright
        $ karma_more = False
        m "Crumps and I are so grateful, [mx]! We won't let you down!"
        m "I'll never forget this! Never, ever, ever! This is the kindest thing anyone's ever done for me, besides the princess taking me in!"
        scene 26_s28 with dissolve
        mc "(Woah!)"
        mc "(Damn, she's so heavy! My back's about to snap!)"
        scene 26_s29 with dissolve
        m "Y-You look really tired, [mx]. Your eyes are all droopy, and you're swaying a little. Did something happen with the witch?"
        m "Do you want to sleep? I'll keep you company!"
        scene 26_s30 with dissolve
        call screen scene26_choice03 with dissolve
        if scene26_choice03_smile:
            mc "I want to see your smile first. I've been thinking about it all day."
            scene 26_s31 with dissolve
            m "..."
            scene 26_s33 with dissolve
            m "[mx]... I..."
            scene 26_s32 with dissolve
            mc "You're so cute. You know that? I'm lucky to have you."
            scene 26_s33 with dissolve
            m "*giggles* [mc]... I want to stay with you forever!"
            scene 26_s32 with dissolve
            mc "Me too. Now come on. Let's get some sleep."
            mc "I need a soft bed and someone warm beside me. *wink* *wink*"
            scene 26_s33 with dissolve
            m "Mhm~"
            scene 26_s32 with dissolve
            scene 28_s9 with Fade(1.0,1.0,1.0)
            m "I'll keep you warm a-all night, [mx]."
            m "Good night. Sweet dreams!"
            scene 28_s10 with dissolve
            mc "Good night."
            scene black with Fade(1.0,1.0,1.0)
            m "{size=30}I love you.{/size}"
            jump free_roam_main_label

        elif scene26_choice03_sex:
            mc "Yeah, let's head to bed. I wanna sleep next to you."
            scene 26_s29 with dissolve
            m "Yes, [mx]! Right away! I'll fluff the pillows and turn down the blankets."
            scene 26_s30 with dissolve
            scene 28_s9 with Fade(1.0,1.0,1.0)
            m "I'll keep you warm a-all night, [mx]."
            m "Good night. Sweet dreams!"
            scene 28_s10 with dissolve
            mc "Good night."
            scene black with Fade(1.0,1.0,1.0)
            jump free_roam_main_label
            
    elif scene26_choice01_refuse:
        mc "I don't want any animals in my room."
        scene 26_s14 with dissolve
        m "...B-but... [mx]! Please! He's all I have! He's been with me through everything!"
        scene 26_s15 with dissolve
        mc "You heard what I said. The answer is no. Find somewhere else for him."
        scene 26_s16 with dissolve
        m "*sniff* I-I promise h-he w... won't cause any problems..."
        m "*hic* Please... [mx]..."
        scene 26_s17 with dissolve
        call screen scene26_choice02 with dissolve
        if scene26_choice02_accept:
            $ mc_accepted_crumps_second = True
            $ maia_love = 60
            $ mc_didnt_accept_crumps = False
            mc "*sigh* Fine, but do you promise to keep an eye on him at all times?"
            scene 26_s16 with dissolve
            m "Y-yes! I will! I promise! *hic*"
            scene 26_s17 with dissolve
            mc "Fine then."
            scene 26_s22 with dissolve
            m "*sniff* Thank you so much, [mx]! Crumps thanks you too!"
            scene 26_s24 with dissolve
            play sound "sound_effects/meow.mp3"
            crumps "Meow!"
            scene 26_s23 with dissolve
            mc "Behave yourself, buddy."
            mc "I'm heading to bed."
            scene 26_s22 with dissolve
            m "O-Of course, [mx]. I'll keep you warm."
            scene 26_s23 with dissolve
            scene 28_s9 with Fade(1.0,1.0,1.0)
            m "Good night. Thank you for letting him stay. Thank you for being patient with me. Thank you for... everything."
            scene 28_s10 with dissolve
            mc "Ahuh."
            scene black with Fade(1.0,1.0,1.0)
            jump free_roam_main_label

        elif scene26_choice02_refuse:
            $ maia_sad = True
            $ maia_happy = False
            $ maia_love = 30
            $ mc_didnt_accept_crumps = True
            if mc_karma > 1:
                $ mc_karma -= 1
            mc "I said no."
            play sound "sound_effects/karma_less.mp3" volume 0.2
            $ karma_less = True
            show screen stat_change with easeinright
            scene 26_s18 with vpunch
            m "Haaaaaaaaaaa!!! No! Please! You can't mean it!"
            m "[mx], you're so cruel! How can you be so heartless?!"
            $ karma_less = False
            hide screen stat_change with easeoutright
            scene 26_s19 with dissolve
            m "Fine! If Crumps goes, I go! We'll... we'll live in the garden!"
            m "*sniff* Don't bother waiting up! I hope you enjoy your empty room!"
            scene 26_s20 with dissolve
            mc "(She'll be back...)"
            scene 26_s21 with fade
            mc "*sigh* (I'm too tired for this.)"
            scene black with Fade(2.0,1.0,1.0)
            jump free_roam_main_label

image scene27_maia_kiss = Movie(play="images/2_chapter1/scene27/scene27_maia_kiss.webm", loop=True)
image scene27_maia_lick1 = Movie(play="images/2_chapter1/scene27/scene27_maia_lick1.webm", loop=True)
image scene27_maia_lick2 = Movie(play="images/2_chapter1/scene27/scene27_maia_lick2.webm", loop=True)
image scene27_maia_suck = Movie(play="images/2_chapter1/scene27/scene27_maia_suck.webm", loop=True)
image scene27_maia_deep = Movie(play="images/2_chapter1/scene27/scene27_maia_deep.webm", loop=True)
image scene27_maia_pus1 = Movie(play="images/2_chapter1/scene27/scene27_maia_pus1.webm", loop=True)
image scene27_maia_pus2 = Movie(play="images/2_chapter1/scene27/scene27_maia_pus2.webm", loop=True)
image scene27_maia_ass1 = Movie(play="images/2_chapter1/scene27/scene27_maia_ass1.webm", loop=True)
image scene27_maia_ass2 = Movie(play="images/2_chapter1/scene27/scene27_maia_ass2.webm", loop=True)

label scene27_sex:
    $ mcname = persistent.name
    if persistent.name == "None" or mcname == "None":
        while mcname == "None" or mcname == "":
            $ mcname = renpy.input("There was an issue with your name. Please rewrite your name:", length=32)
        $ persistent.name = mcname
    if not persistent.scene7_replay:
        $ persistent.scene7_replay = True
    stop music fadeout 3.0
    scene 27_s1 with Fade(1.0,1.0,1.0)
    m "*gulp* So big..."
    scene 27_s2 with dissolve
    m "What should I do, [mx]?"
    $ maia_oral_sex += 1
    scene 27_s3 with dissolve
    call screen scene27_sex with dissolve

default scene27_lick_first = True
default scene27_deep_first = True

label scene27_sex_kiss:
    $ maia_mouth_virgin = False   
    $ scene27_all_options = True
    $ scene27_suck = True
    $ scene27_deep = True
    scene black with Dissolve(0.3)
    show scene27_maia_kiss with dissolve
    m "Mwah!"
    sensation "Her lips press against your tip, the heat of her mouth radiating onto your sensitive skin."
    call screen scene27_sex with dissolve

label scene27_sex_lick:
    $ maia_mouth_virgin = False
    $ scene27_all_options = True
    $ scene27_suck = True
    $ scene27_deep = True
    if scene27_lick_first:
        scene black with Dissolve(0.3)
        show scene27_maia_lick2 with dissolve
        m "Dosh it feew goo, [mx]?"
        mc "You're doing well. Keep going."
        scene black with Dissolve(0.3)
        show scene27_maia_lick1 with dissolve
        m "Ahnn~"
        sensation "She begins to lick along your length with eager devotion. Her tongue is soft and curious."
        $ scene27_lick_first = False
        call screen scene27_sex with dissolve
    else:
        scene black with Dissolve(0.3)
        show scene27_maia_lick2 with dissolve
        m "It tashets shalty..."
        scene black with Dissolve(0.3)
        show scene27_maia_lick1 with dissolve
        m "Ahnn~"
        sensation "Her tongue glides softly under your tip, teasing and sending shivers of pleasure through you."
    call screen scene27_sex with dissolve

label scene27_sex_suck:
    $ maia_mouth_virgin = False
    $ scene27_all_options = True
    $ scene27_deep = True
    scene black with Dissolve(0.3)
    show scene27_maia_suck with dissolve
    m "Mmhmm~"
    sensation "She glides her mouth back and forth along your cock, her movements eager and devoted as she works to please you. Her tongue darts and swirls in random."
    call screen scene27_sex with dissolve

label scene27_sex_deep:
    $ maia_mouth_virgin = False
    $ scene27_all_options = True
    $ scene27_suck = True

    if scene27_deep_first:
        mc "Prepare your throat."
        m "Hmm?"
        play sound "se_sfx/blowjob/gag1.mp3" 
        scene 27_s25 with vpunch
        m "*gag*!... *cough*!"
        show scene27_maia_deep with dissolve
        m "*gag*"
        $ scene27_deep_first = False
        call screen scene27_sex with dissolve
    else:
        scene black with Dissolve(0.3)
        show scene27_maia_deep with dissolve
        m "*gag*... *gag*..."
        sensation "Her throat tightens around your cock, her uvula brushing against you as you thrust deeper into her mouth pussy."
        m "Mmnnh~!"
        call screen scene27_sex with dissolve

label scene27_cum_options:
    call screen scene27_sex_cum_options with dissolve

label scene27_sex_cuminside:
    if scene27_choose_cumsuck:
        $ maia_total_cum_in_mouth += 3.7
        mc "Take it all in your mouth!"
        play sound "se_sfx/blowjob/facial3.mp3" 
        scene 27_s19 with vpunch
        mc "Hnnggg!!"
        sensation "You burst, releasing your hot seed into her mouth. She takes it all, accepting every drop without hesitation, her lips sealed tightly around you."
        m "Mhnnggg!!"
        play sound "se_sfx/blowjob/facial5.mp3" 
        scene 27_s20 with vpunch
        m "Mhhmm..."
        scene 27_s21 with fade
        m "*gag* [mx]... wha do ah do?"
        call screen scene27_sex_swallow_spit with dissolve
        
    elif scene27_choose_cumdeep:
        $ maia_total_cum_in_mouth += 3.7
        mc "Take it all in your throat!"
        play sound "se_sfx/blowjob/gag2.mp3" 
        scene 27_s25 with vpunch
        mc "Hnnggg!!"
        sensation "You burst, releasing your hot seed deep into her throat. Her muscles tighten around you, each contraction pulling you deeper as she swallows every last drop."
        play sound "se_sfx/blowjob/blowjob_cum1.mp3" 
        scene 27_s26 with vpunch
        m "Mhmmn!"
        scene 27_s27 with fade
        m "*cough* *cough*"
        m "*cough* [mx]... I swallowed it all..."
        scene 27_s28 with dissolve
        m "I'm sorry... I-I had no choice, i-it was stuck in my throat!"
        scene 27_s29 with dissolve
        mc "Why are you apologizing? That was my intention anyway."
        scene 27_s13 with dissolve
        m "O-oh... D-did I do good then, [mx]?"
        scene 27_s14 with dissolve
        mc "Mhmm, good girl."
        scene 27_s13 with dissolve
        m "Hehe~"
        jump scene27_climax

label scene27_sex_cuminside2:
        if scene27_swallow:
            mc "Swallow it."
            m "Ogay..."
            scene 27_s22 with dissolve
            play sound "se_sfx/blowjob/swallow1.mp3" 
            m "*gulp*... *gag*"
            scene 27_s21 with dissolve
            m "theresh sho mush..."
            scene 27_s22 with dissolve
            play sound "se_sfx/blowjob/swallow2.mp3" 
            m "*gulp* *gulp*"
            mc "Show me."
            scene 27_s23 with dissolve
            m "Ahhh~"
            mc "Good girl."
            scene 27_s14 with dissolve
            m "Hmhmmm~"
            jump scene27_climax
        if scene27_spit:
            mc "You can spit it out."
            scene 27_s24 with dissolve
            m "Ptoo..."
            jump scene27_climax

label scene27_sex_cumoutside:
    mc "I'll cover that pretty face of yours!"
    play sound "se_sfx/blowjob/facial4.mp3" 
    scene 27_s4 with vpunch
    mc "Hnnggg!!"
    perception "Thick streaks of your seed splatter across her face, each line and droplet forming a stark, glistening contrast against her skin—like a painting come to life."
    play sound "se_sfx/blowjob/facial2.mp3" 
    scene 27_s5 with vpunch
    mc "Ahhngg!"
    jump scene27_climax

label scene27_climax:
    if scene27_cinside:
        scene 27_s15 with dissolve
        m "Wait... isn't that... what's used to get me pregnant, [mx]?"
        scene 27_s16 with dissolve
        mc "That's the stuff."
        scene 27_s15 with dissolve
        m "Then, [mx]! Wasn't it a w-waste to let me drink it all?"
        scene 27_s16 with dissolve
        mc "Not at all. I can make plenty more of it."
        scene 27_s17 with dissolve
        m "Woah!"
        m "I-If that's the case... then you can give me lots of it in my tummy whenever you want, Master."
        scene 27_s13 with dissolve
        m "Umm... So... is your cock ready again, [mx]?"
        scene 27_s14 with dissolve
        mc "Ready for what?"
        scene 27_s13 with dissolve
        m "T-To impregnate me, [mx]..."
        scene 27_s14 with dissolve
        call screen scene27_choice02 with dissolve
        if scene27_choice02_sex:
            mc "Get on the bed."
            scene 27_s17 with dissolve
            m "Yes, [mx]!"
            jump scene27_sex02
        elif scene27_choice02_enough:
            $ mc_talk_maia_first_sex = True
            $ renpy.end_replay()
            mc "I think I've had enough for now."
            scene 27_s15 with dissolve
            m "Oh... A-are you tired, [mx]?"
            scene 27_s16 with dissolve
            mc "I have to leave for now. The Queen tasked me with hunting down a witch."
            scene 27_s15 with dissolve
            m "T-That's really dangerous, Master!"
            scene 27_s16 with dissolve
            mc "I know. But don't worry, I got it. Well... I hope so."
            scene 27_s15 with dissolve
            m "Please take care! I-If things get too dangerous then there's no shame in running away!"
            scene 27_s16 with dissolve
            mc "*chuckles* I will. See you soon, Maia."
            scene 27_s17 with dissolve
            m "Promise me you will... come back."
            scene 27_s18 with dissolve
            mc "I promise."
            scene black with Fade(0.5,0.5,0.5)
            stop music fadeout 2.0 
            jump scene18_free_roam_main_0

    if scene27_coutside:
        scene 27_s6 with dissolve
        m "S-so much..."
        m "Is this... what's used to get me pregnant, [mx]?"
        scene 27_s7 with dissolve
        mc "That's the stuff."
        scene 27_s8 with dissolve
        m "But, [mx]! Wasn't that a w-waste to... shoot it all on my face?"
        scene 27_s9 with dissolve
        mc "Not at all. I can make plenty more of it."
        scene 27_s10 with dissolve
        m "Woah!"
        m "I-if that's the case, then you can give me lots of it on my face whenever, [mx]."
        scene 27_s6 with dissolve
        m "Umm... So... is your cock ready again, [mx]?"
        scene 27_s7 with dissolve
        mc "Ready for what?"
        scene 27_s6 with dissolve
        m "T-To impregnate me, [mx]..."
        scene 27_s7 with dissolve
        call screen scene27_choice02 with dissolve
        if scene27_choice02_sex:
            mc "Get on the bed."
            scene 27_s10 with dissolve
            m "Yes, [mx]!"
            jump scene27_sex02
        elif scene27_choice02_enough:
            $ mc_talk_maia_first_sex = True
            $ renpy.end_replay()
            mc "I think I've had enough for now."
            scene 27_s8 with dissolve
            m "Oh... A-are you tired, [mx]?"
            scene 27_s9 with dissolve
            mc "I have to leave for now. The Queen tasked me with hunting down a witch."
            scene 27_s8 with dissolve
            m "T-That's really dangerous, Master!"
            scene 27_s9 with dissolve
            mc "I know. But don't worry, I got it. Well... I hope so."
            scene 27_s8 with dissolve
            m "Please take care! I-If things get too dangerous then there's no shame in running away!"
            scene 27_s9 with dissolve
            mc "*chuckles* I will. See you soon, Maia."
            scene 27_s10 with dissolve
            m "Promise me you will... come back."
            scene 27_s12 with dissolve
            mc "I promise."
            scene black with Fade(0.5,0.5,0.5)
            stop music fadeout 2.0 
            jump scene18_free_roam_main_0

label scene27_sex02:
    scene 16_s38 with Fade(1.0,1.0,1.0)
    m "W-What do you want to do, Master?"
    call screen scene27_sex02 with dissolve

label scene27_sex02_op2:
    scene 16_s39 with Dissolve(1.5)
    perception "Her folds glisten in the warm candlelight. Pink, swollen, and dripping with arousal. The sight alone makes your cock twitch."
    mc "Relax, Maia... spread a little wider for me."
    scene 16_s41 with Dissolve(1.0)
    m "M-Master... ahh...!"
    sensation "Her heat is intoxicating—the faint sweetness on your tongue, her thighs trembling around your face."
    m "Nnnhhh~! T-Too much... I c-can't—!"
    perception "Her hips roll, timid at first, then desperate, chasing every flick of your tongue."
    scene 16_s42 with vpunch
    m "Aahhh~! Master! I-I'm cumming—!"
    scene 16_s39 with Dissolve(1.5)
    m "Hahh... Ahhn... Master! I'm sorry for getting it all on your face!"
    mc "It tastes sweet. Don't apologize for that."
    m "Hnn..."
    mc "Turn around for me."
    jump scene27_sex2

label scene27_sex02_op1:
    scene 16_s40 with Dissolve(1.5)
    perception "The shy curve of her rear is exposed as she shifts, pink and vulnerable, her breath shallow."
    m "H-Huh!? M-Master?! What are you?"
    mc "I want all of you, Maia."
    scene 16_s43 with Dissolve(1.0)
    m "But... th-there? It's embarrassing..."
    mc "Mmmmm..."
    sensation "Your tongue circles and teases until she shudders and gaspes."
    m "Aahhh~! S-Stop, it feels so weird... ahhnn~!"
    scene 16_s44 with dissolve
    perception "Her hands claw at the sheets, muffled cries spilling as she rocks back against your tongue without even realizing it."
    m "Mmmhhhnnn~! I-I can't take it...! Master!"
    scene 16_s39 with Dissolve(1.5)
    m "Hahh... Ahhn..."
    mc "Turn around for me."
    jump scene27_sex2

label scene27_sex2:
    scene 27_s30 with Fade(1.0,1.0,1.0)
    ""
    scene 27_s31 with dissolve
    m "[mx]... It's my first time, so please be g-gentle..."
    mc "I will, don't worry. But I still haven't decided where to start..."
    m "Where to start? You're not trying to breed me, [mx]?"
    mc "Well... Let me think."
    m "But Master... shouldn't we start making children? Her Majesty commanded it... and I... I want it so much."
    mc "You need to calm down about the whole 'making children' thing. We have time."
    m "O-Of course, Master... I will wait for your command first."
    m "I'm ready whenever you are, Master. Please... use me however you wish. My body belongs to you."
    call screen scene27_choice04 with dissolve

default scene27_vag_first = True
default scene27_anal_first = True

label scene27_choice04_vag:
    $ maia_pussy_virgin = False
    $ maia_pussy_sex += 1
    scene 27_s33 with fade
    m "Ahhn~"
    scene 27_s34 with dissolve
    m "S-slowly, [mx]..."
    $ scene27_slow = True
    jump scene27_choice04_vag2

    call screen scene27_choice05_vag with dissolve

label scene27_choice04_vag2:
    $ scene27_choice04_all_options2 = True
    if scene27_vag_first:
        $ maia_pussy_sex += 1
        $ scene27_vag_first = False
        if scene27_slow:
            play sound "se_sfx/sex/touch2.mp3" 
            scene 27_s35 with Dissolve(1.0)
            m "Mfhmmm~"
            show scene27_maia_pus1 with dissolve
            m "Ahh~ Ahn~"
            m "I-it feels... Ahh~... so good, [mx]!"
            sensation "Even though her pussy is soaked and dripping from serving your cock earlier, she's still as tight as a vice, gripping you with a relentless, almost desperate pressure."
            m "Ahh~ Ahn! It feels... Ahh~ so good, Master! I've wanted this for so long..."
            mc "You're incredibly tight, Maia. Even after how wet you got earlier."
            scene black with Dissolve(0.5)
            show scene27_maia_pus2 with dissolve
            mc "Shit! You're squeezing me so hard. Does it feel that good?"
            m "It does! It feels like my body was made for you... Hahh~! Master, please don't stop!"
            m "Master...! I'm going to cum again... Can I? Please let me cum on your cock!"
            call screen scene27_choice04 with dissolve
        elif scene27_allin:
            show scene27_maia_pus2 with dissolve
            
            call screen scene27_choice04 with dissolve
    else:
        scene black with Dissolve(0.5)
        show scene27_maia_pus1 with dissolve
        m "Ah~ Ahh! Ngh~"
        m "[mx]! Hah~"
        m "Y-You're so big... I can feel you opening me up..."
        scene black with Dissolve(0.5)
        show scene27_maia_pus2 with dissolve
        m "Ah~! Ahh! Ngh~ Master! Hah~ You're so deep... I can feel you hitting something inside me..."
        mc "That's your womb, Maia. This is where I'm going to put my children."
        m "Y-Yes! Please... fill my womb, Master... I want to carry your babies so badly... Ahh! Ah~!"
        call screen scene27_choice04 with dissolve


label scene27_choice04_anal:
    if not scene27_anal_first:
        jump scene27_choice04_anal2
    $ maia_anus_virgin = False                    
    $ maia_anal_sex += 1
    scene 27_s32 with fade
    m "M-My butt?!"
    mc "I've been waiting to dig in your ass for a long time, Maia."
    scene 27_s37 with dissolve
    m "I-I see... but, [mx]... Do it s-slowly please."
    $ scene27_slow = True
    jump scene27_choice04_anal2
    call screen scene27_choice05_ass with dissolve

label scene27_choice04_anal2:
    if scene27_anal_first:
        $ maia_anal_sex += 1
        $ scene27_anal_first = False
        if scene27_slow:
            play sound "se_sfx/sex/sex3.mp3" 
            scene 27_s35 with Dissolve(1.0)
            m "Ahh! Ah!"
            show scene27_maia_ass1 with dissolve
            $ scene27_anal_first = False
            m "Nghhh!"
            m "I-it feels... weird, [mx]!"
            scene black with Dissolve(0.3)
            show scene27_maia_ass2 with dissolve
            m "Ngh... Mhnn..." 
            m "Not too deep, [mx]!"
            sensation "Her ass wraps around you, her insides gripping you with an intense, almost overwhelming pressure. Her body shudders and relaxes with each thrust."
            mc "Does it hurt?"
            m "A little... but I don't want you to stop... I want to please you!"
            mc "Good girl. I'll be gentler."
            m "Ahhaaa~! Ah~! Hngnn... Thank you, Master... It's starting to feel... strange but good..."
            call screen scene27_choice04 with dissolve
        elif scene27_allin:
            call screen scene27_choice04 with dissolve

    else:
        scene black with Dissolve(0.5)
        show scene27_maia_ass1 with dissolve
        mc "Tell me how it feels."
        m "Ahhnn... My butt is being filled up~... Ngh! Your cock is so deep in my belly, Master...! It feels embarrassing... but I love that you're claiming this part of me too!"
        mc "You're getting wetter just from this. Such a naughty girl."
        m "I-I can't help it... Everything you do to me feels good now... Ah! Nghh~! Please... use my ass whenever you want... I'll train it for you..."
        mc "That's what I like to hear."
        scene black with Dissolve(0.5)
        show scene27_maia_ass2 with dissolve
        m "Master... I feel so full... Do you feel good inside me?"
        mc "You feel incredible."
        m "Then... please keep using me until you're satisfied. And when you're ready... I'm begging you... cum inside me. I want your seed deep in my womb."
        m "[mx]! Ah! Nghh~! I don't care if it's my first time... I want everything from you tonight!"
        call screen scene27_choice04 with dissolve

            
label scene27_choice04_cum_inside:
    if scene27_choice04_cum_inside_puss:
        $ maia_pussy_sex += 1
        $ maia_total_cum_in_pussy += 4.5
        mc "I'm close!"
        m "Do it inside, [mx]!"
        play sound "se_sfx/sex/sex_cum1.mp3" 

        if persistent.xray_mode:
            scene 27_s38_xray1 with vpunch
            mc "Get pregnant! Get pregnant! Get pregnant!"
            play sound "se_sfx/sex/sex_cum2.mp3" 
            scene 27_s38_xray2 with vpunch
            m "Ahhhh!"
            scene 27_s39_xray3 with Dissolve(1.0)
            mc "Hah... hah..."
            m "Hnn~ Ahhhh~ Master, you came so much... I can feel it all the way in my womb~ It's so warm~"
        else:
            scene 27_s38 with vpunch
            mc "Get pregnant! Get pregnant! Get pregnant!"
            play sound "se_sfx/sex/sex_cum2.mp3" 
            scene 27_s38 with vpunch
            m "Ahhhh!"
            scene 27_s39 with Dissolve(1.0)
            mc "Hah... hah..."
            m "Hnn~... Ahhhh~"
            m "[mx], you came so much... I can feel it all the way in my womb~"

        call pregnancy_check_maia from _call_pregnancy_check_maia
        scene 27_s45 with dissolve
        mc "How are you feeling? Was I being too rough?"
        m "Not at all, Master. I... I liked it. I liked feeling you lose control like that."
        mc "*chuckles* I'm glad to hear that."
        m "Oh! And umm... T-Thank you for your semen, Master! Hopefully, I can get pregnant now."
        m "A-And if I didn't get pregnant this time... then we can try again! As many times as you want. I don't mind at all."
        mc "You're a special kind of woman, Maia."
        m "I just want to make you happy... and give you strong, healthy children."
        $ renpy.end_replay()
        jump scene28

    elif scene27_choice04_cum_inside_ass:
        $ maia_anal_sex += 1
        $ maia_total_cum_in_ass += 4.5
        mc "I'm close!"
        m "Inside my butt?! M-Master!"
        play sound "se_sfx/sex/sex_cum2.mp3" 
        scene 27_s41 with vpunch
        mc "Nghhhh!!!"
        play sound "se_sfx/sex/sex_cum1.mp3" 
        scene 27_s41 with vpunch
        m "Hngnn!"
        scene 27_s40 with dissolve
        mc "Hah... hah..."
        mc "Wow, your butt is gaping, Maia."
        m "[mx], I can't seem to close it... It feels so open..."
        mc "It'll go back to normal after a while."
        m "I-I hope soo."
        m "It felt really weird, Master... But... I'm glad you enjoyed it."
        scene 27_s45 with dissolve
        mc "Was I being too rough?"
        m "N-No..."
        mc "You can be honest with me, Maia. I wont get mad at something like that."
        m "Thank you... It was a little rough. It hurt at first, but then it started feeling... strange and full."
        mc "I should have prepared you more. That was too quick. I'll be better next time."
        m "YYou'll... lick my butt next time to prepare it?"
        mc "*chuckles* That would be one way to do it."
        m "*giggles* Then... I wouldn't mind it at all."
        mc "Very well!"
        $ renpy.end_replay()
        jump scene28

default scene27_cameoutside_ye = False
label scene27_choice04_cum_outside:
    mc "I'm close!"
    if scene27_choice04_cum_inside_puss:
        $ maia_pussy_sex += 1
        m "Do it inside, [mx]!"
        play sound "se_sfx/blowjob/facial1.mp3" 
        scene 27_s42 with vpunch
        mc "Ahh!"
        play sound "se_sfx/blowjob/facial2.mp3" 
        scene 27_s43 with vpunch
        mc "Nghhh!"
        scene 27_s44 with dissolve
        mc "Hah... hah..."
        m "[mx]... Why didn't you finish inside me?"
        mc "Sorry. Covering your pretty ass was too appealing in the moment."
        m "But, [mx]..."
        mc "What?"
        m "I-It's nothing..."
        mc "Don't be sad. We can try again later. I promise."
        m "Oh, right! Yes, Master. I'll wait patiently... and I'll be even better next time."
        $ scene27_choice04_cum_inside_puss = False
        $ scene27_cameoutside_ye = True
        $ renpy.end_replay()
        jump scene28
    elif scene27_choice04_cum_inside_ass:
        $ maia_anal_sex += 1
        m "Ahhnn~! [mx]!"
        play sound "se_sfx/blowjob/facial1.mp3"
        scene 27_s42 with vpunch
        mc "Nghhh!"
        play sound "se_sfx/blowjob/facial2.mp3"
        scene 27_s43 with vpunch
        mc "Ahh!"
        scene 27_s44 with dissolve
        mc "Hah... hah..."
        m "[mx]... My butt feels weird... all empty and tingly now..."
        mc "Was I being too rough?"
        m "N-No..."
        mc "You can be honest with me, Maia. I wont get mad at something like that."
        m "Thank you... It was a little rough. It hurt at first, but then it started feeling... strange and full."
        mc "I should have prepared you more. That was too quick. I'll be better next time."
        m "YYou'll... lick my butt next time to prepare it?"
        mc "*chuckles* That would be one way to do it."
        m "*giggles* Then... I wouldn't mind it at all."
        mc "Very well!"
        $ renpy.end_replay()
        jump scene28

label scene28:
    $ mc_talk_maia_first_sex = True
    scene black with Fade(1.0,1.0,1.0)
    mc "Maia?"
    scene 28_s1 with dissolve
    play sound "se_sfx/blowjob/kiss2.mp3" 
    m "Mwah... Thank you..."
    if scene27_choice04_cum_inside_puss:
        scene 28_s2 with dissolve
        mc "(Woah...)"
        mc "Good girl!"
        mc "You continue to surprise me."
        scene 28_s3 with dissolve
        m "Thank you, Master."
        m "I will do my best to take care of our little baby."
        scene 28_s2 with dissolve
        mc "What if you didn't get pregnant?"
        scene 28_s4 with dissolve
        m "Like I said, we can just try again!"
        scene 28_s5 with dissolve
        mc "Hah... You're really something..."
        scene 28_s3 with dissolve
        m "...W-What now, [mx]?"   
        scene 28_s2 with dissolve
        mc "I have to leave for now. The Queen tasked me with hunting down a witch."
        scene 28_s4 with dissolve
        m "T-That's really dangerous, Master!"
        scene 28_s5 with dissolve
        mc "I know. But don't worry, I got it. Well... I hope so."
        scene 28_s4 with dissolve
        m "Please take care! I-If things get too dangerous then there's no shame in running away!"
        scene 28_s5 with dissolve
        mc "*chuckles* I will. See you soon, Maia."
        scene 28_s3 with dissolve
        m "Promise me you will... come back."
        scene 28_s2 with dissolve
        mc "I promise."
        stop music fadeout 2.0 
        scene black with Fade(0.5,0.5,0.5)
        jump scene18_free_roam_main_0

    elif scene27_choice04_cum_inside_ass:  
        scene 28_s2 with dissolve  
        mc "(Woah...)"
        mc "Good girl!"
        mc "You continue to surprise me."
        scene 28_s3 with dissolve
        m "Thank you, [mx]."
        scene 28_s6 with dissolve
        m "And it might take some time for my butt to heal before you can use it again..."
        scene 28_s7 with dissolve
        mc "Oh right, I did put you through that, huh..."
        scene 28_s4 with dissolve
        m "I-it's okay! I'll do anything for you, [mx]."
        scene 28_s5 with dissolve
        mc "Hah... You're really something..."
        scene 28_s3 with dissolve
        m "...W-what now, [mx]?"
        scene 28_s2 with dissolve
        mc "I have to leave for now. The Queen tasked me with hunting down a witch."
        scene 28_s4 with dissolve
        m "T-That's really dangerous, Master!"
        scene 28_s5 with dissolve
        mc "I know. But don't worry, I got it. Well... I hope so."
        scene 28_s4 with dissolve
        m "Please take care! I-If things get too dangerous then there's no shame in running away!"
        scene 28_s5 with dissolve
        mc "*chuckles* I will. See you soon, Maia."
        scene 28_s3 with dissolve
        m "Promise me you will... come back."
        scene 28_s2 with dissolve
        mc "I promise."
        scene black with Fade(0.5,0.5,0.5)
        stop music fadeout 2.0 
        jump scene18_free_roam_main_0

    elif scene27_cameoutside_ye:
        scene 28_s2 with dissolve
        mc "(Woah...)"
        mc "Good girl!"
        mc "You continue to surprise me."
        scene 28_s3 with dissolve
        m "Thank you, [mx]."
        scene 28_s4 with dissolve
        m "And e-even though you didn't ejaculate inside me, I'm sure we'll have many other chances!"
        scene 28_s5 with dissolve
        mc "Right..."
        scene 28_s3 with dissolve
        m "...W-what now, [mx]?"
        scene 28_s2 with dissolve
        mc "I have to leave for now. The Queen tasked me with hunting down a witch."
        scene 28_s4 with dissolve
        m "T-That's really dangerous, Master!"
        scene 28_s5 with dissolve
        mc "I know. But don't worry, I got it. Well... I hope so."
        scene 28_s4 with dissolve
        m "Please take care! I-If things get too dangerous then there's no shame in running away!"
        scene 28_s5 with dissolve
        mc "*chuckles* I will. See you soon, Maia."
        scene 28_s3 with dissolve
        m "Promise me you will... come back."
        scene 28_s2 with dissolve
        mc "I promise."
        scene black with Fade(0.5,0.5,0.5)
        jump scene18_free_roam_main_0

label scene28_with:
    mc "You tired?"
    scene 28_s4 with dissolve
    m "N-no! I'm not, [mx]! We can go again if you want..."
    scene 28_s5 with dissolve
    mc "Yes you are, I can hear it in your voice..."
    scene 28_s8 with dissolve
    m "..."
    mc "Come on, let's sleep."
    scene 28_s3 with dissolve
    m "Y-yes, [mx]!"
    scene 28_s10 with dissolve
    m "..."
    scene 28_s9 with dissolve
    m "Good night, [mx]."
    scene 28_s10 with dissolve
    mc "Good night."
    scene black with Fade(2.0,1.0,1.0)
    if maia_love >= 70:
        m "{size=30}I love you."
    else:
        m "..."
    $ renpy.end_replay()
    jump scene29

label scene28_refuse:
    mc "I'm going to bed. Let's continue this later, alright?"
    scene 28_s6 with dissolve
    m "Of course, [mx]..."
    scene 28_s7 with dissolve
    m "..."
    scene 28_s4 with dissolve
    m "Umm... [mx]?"
    scene 28_s5 with dissolve
    mc "Hmm?"
    scene 28_s4 with dissolve
    m "D-do... do you want to sleep t-together?"
    scene 28_s5 with dissolve
    mc "Maybe some other time."
    scene 28_s8 with dissolve
    m "..."
    scene 26_s21 with fade
    ""
    $ renpy.end_replay()
    scene black with Fade(2.0,1.0,1.0)
    jump scene29

default mc_market_first = True
label scene29:
    $ diana_game_start = False
    $ in_scene18 = False
    $ in_scene32 = False
    $ in_scene34 = False
    $ in_scene35 = False
    
    $ in_scene30 = True
    $ mc_didnt_accept_crumps = False
    if mc_punished_maia_little:
        $ maia_sad = False
        $ maia_happy = True
        $ maia_love = 60
    elif not mc_punished_maia:
        $ maia_happy = True
        $ maia_sad = False
        $ maia_love = 70
    elif mc_punished_maia and not mc_apologized_maia:
        $ maia_happy = False
        $ maia_sad = True
        $ maia_love = 40
    elif mc_punished_maia and mc_apologized_maia:
        $ maia_sad = False
        $ maia_happy = True
        $ maia_love = 60
    $ mc_armor_timer = 2
    stop music fadeout 2.0
    $ current_objective = "Current Objective: Explore the market"
    scene 29_s1 with Fade(1.0,1.0,1.0)
    ""
    scene 29_s2 with Dissolve(1.0)
    mc "(Where the hell? Oh, right...)"
    scene 29_s3 with Dissolve(1.0)
    ""
    scene 29_s4 with Dissolve(1.0)
    ""
    scene 29_s5 with Fade(0.5,0.5,0.5)
    mc "(Two days until I get my armor... might as well do something.)"
    mc "Hmm..."
    mc "Uh..."
    mc "Nnnnn..."
    scene 29_s6 with dissolve
    m "Is something bothering you, [mx]?"
    scene 29_s7 with dissolve
    mc "I don't know what to do."
    scene 29_s6 with dissolve
    m "Umm... I took a bath earlier so... If you're free, m-maybe we could have se—"
    scene 29_s8 with dissolve
    mc "I got it! I'd love to explore the market. I saw some interesting things there."
    if mc_accept_helped_nadia:
        mc "(I also promised Nadia to help her. Should see to that too.)"
    scene 29_s9 with dissolve
    m "Right... the market. That sounds... nice."
    scene 29_s8 with dissolve
    mc "Should I get you something, Maia?"
    scene 29_s9 with dissolve
    m "M-Me? Just your safety, [mx]."
    scene 29_s8 with dissolve
    mc "Enough with that. Come on, tell me! There's got to be something."
    scene 29_s9 with dissolve
    m "U-Um... I guess some fresh strawberries would be nice."
    scene 29_s8 with dissolve
    mc "Strawberries, got it. I'll get you some when I head out."
    if mc_coin <= 3:
        $ mc_coin += 10
        scene 29_s7 with dissolve
        mc "Wait... I barely have any coin. I still haven't been paid."
        scene 29_s6 with dissolve
        m "Oh... I see."
        scene 29_s7 with dissolve
        mc "Shit... I'm sorry, Maia. I can't even buy my wife strawberries."
        scene 29_s6 with dissolve
        m "No worries, [mx]. Here, take this."
        $ renpy.notify("You received 1 silver coin!")
        play sound "sound_effects/coin_collect.mp3"
        scene 29_s8 with dissolve
        mc "T-Thank you! I promise I'll pay you back!"
        scene 29_s9 with dissolve
        m "I-I don't mind it. My coin is yours too. That's what marriage means, isn't it?"
        scene 29_s8 with dissolve
        mc "You're just too good for me."
    scene 29_s9 with dissolve
    m "Thank you. And I'll be there by the window... in case you want to... talk, [mx]."
    $ mc_marital = "married"
    $ mc_card_reg = True
    $ mc_job = "royal_servant"
    $ mc_residency = "castle"
    $ yuuhi_harem_training_finished = False
    jump free_roam_main_label

label scene29_market:
    $ in_free_roam = True
    $ mc_market_first = False
    scene 29_s12 with Fade(2.0,1.0,1.0)
    play music "market2.mp3" fadein 3.0 volume 0.7 loop
    mc "(Now, where should I go?)"

label scene29_free_roam:
    scene 29_s13 with dissolve

    if not karma_updated:
        $ karma_updated = True
        if mc_karma >= 100:
            $ mc_karma = 10
        elif mc_karma >= 90:
            $ mc_karma = 9
        elif mc_karma >= 80:
            $ mc_karma = 8
        elif mc_karma >= 70:
            $ mc_karma = 7
        elif mc_karma >= 60:
            $ mc_karma = 6
        elif mc_karma >= 50:
            $ mc_karma = 5
        elif mc_karma >= 40:
            $ mc_karma = 4
        elif mc_karma >= 30:
            $ mc_karma = 3
        elif mc_karma >= 20:
            $ mc_karma = 2
        elif mc_karma >= 10:
            $ mc_karma = 1
        else:
            $ mc_karma = 1
    if mc_karma > 10:
        $ mc_karma = 10
    if mc_karma < 1:
        $ mc_karma = 1
    call screen scene29_free_roam with dissolve

label scene29_free_roam_right:
    scene 29_s14 with dissolve
    call screen scene29_free_roam_right with dissolve

label scene29_free_roam_left:
    if scene29_coin:
        scene 29_s15_2 with dissolve
    else:
        scene 29_s15 with dissolve
    call screen scene29_free_roam_left with dissolve

label scene29_coin:
    $ mc_coin += 10
    $ renpy.notify("You found 1 silver coin!")
    play sound "sound_effects/coin_collect.mp3"
    $ scene29_coin = False
    jump scene29_free_roam_left

label scene29_free_roam_up:
    scene 29_s16 with dissolve
    call screen scene29_free_roam_up with dissolve

label scene29_free_roam_right_up:
    scene 29_s17 with dissolve
    slady "Welcome, sir. See anything you like?"
    scene 29_s18 with dissolve
    call screen scene29_choice03 with dissolve

label scene29_free_roam_up_right:
    if scene29_poster:
        scene 29_s20_2 with dissolve
    else:
        scene 29_s20 with dissolve
    call screen scene29_free_roam_up_right with dissolve

label scene29_poster:
    $ persistent.kat_render1 = True
    play sound "sound_effects/render_unlock.mp3"
    $ renpy.notify("You unlocked a special render!")
    $ scene29_poster = False
    jump scene29_free_roam_up_right

default scene29_begger = True
label scene29_free_roam_up_left:
    if scene29_begger:
        $ scene29_begger = False
        scene 29_s21 with dissolve
        begger "Spare a coin for an old knight?"
        scene 29_s22 with dissolve
        mc "So you're a knight now?"
        scene 29_s21 with dissolve
        begger "...Ehh?"
        scene 29_s22 with dissolve
        call screen scene29_choice05 with dissolve
    else:
        scene 29_s23 with dissolve
        call screen scene29_free_roam_up_left with dissolve

label scene29_choice05_op1:
    if mc_coin >= 1:
        $ mc_coin -= 1
        play sound "sound_effects/karma_more.mp3" volume 0.2
        if mc_karma < 10:
            $ mc_karma += 1
        $ karma_more = True
        show screen stat_change with easeinright  
        perception "You toss him a coin, and it slips awkwardly between his legs, making a soft clink on the ground."
        scene 29_s21 with dissolve
        begger "*cough* Oh, bless you, sir! May fortune follow your steps."
        hide screen stat_change with easeoutright
        $ karma_more = False
        scene 29_s22 with dissolve
    else:
        perception "{color=#4A90E2}You pat your pockets, but they're disappointingly light.{/color}"
    jump scene29_free_roam_up_left

label scene29_choice05_op2:
    scene 29_s23 with Dissolve(1.0)
    perception "The man falls silent, his eyes cast downward again."
    jump scene29_free_roam_up_left

label scene29_free_roam_end:
    call screen scene29_free_roam_end with dissolve

label scene29_continue:
    $ in_free_roam = False
    scene 29_s24 with Fade(0.5,0.5,0.5)
    mc "Hmm?"
    scene 29_s25 with dissolve
    if mc_helped_ruby:
        mc "(Didn't Darius say that this isn't allowed in Irda? Or maybe this is something else?)"
    else:
        mc "(I guess that's common around here...)"
    scene 29_s26 with dissolve
    mc "(And there's Nadia. Hopefully her business is doing better now.)"
    mc "(I guess I could check her out... or see what that merchant's about.)"
    scene 29_s24 with dissolve
    call screen scene29_choice06 with dissolve

label scene29_choice06_op1:
    $ mc_met_nadia = True
    scene 29_1_s1 with Fade(0.5,0.5,0.5)
    ml "Get your fresh milk right here! Straight from the farm this morning!"
    mc "Hey, Nadia!"
    scene 29_1_s2 with dissolve
    ml "[mc]! You nearly gave me a heart attack this morning. I woke up and you weren't there."
    scene 29_1_s3 with dissolve
    mc "Ah, sorry. Had to slip out early."
    scene 29_1_s3_2 with dissolve
    ml "Of course. Everyone's got their own path these days."
    ml "Still... it's good to see you again. I was worried."
    scene 29_1_s3 with dissolve
    mc "Same here. How've you been? Business treating you any better?"
    scene 29_1_s3_2 with dissolve
    ml "We'll get to that... but first—what about you? Did you find a place to stay, or are you still wandering like a stray cat?"
    scene 29_1_s3 with dissolve
    mc "Actually, the Queen herself is letting me stay at the castle. I've got a room and everything."
    scene 29_1_s3_2 with vpunch
    ml "T-The Queen!? [mc]... you never told me you had ties to Her Majesty!"
    ml "I-I let a man connected to the royal court sleep on a bunch of blankets! I hit him with a broom!"
    scene 29_1_s3 with dissolve
    mc "*chuckles* It's a long story, but remember the ogre? The one that was terrorizing the farms?"
    scene 29_1_s3_2 with dissolve
    ml "Mhm. The whole market was buzzing about it. Even had a celebration."
    scene 29_1_s3 with dissolve
    if mc_lied:
        mc "Well, I was the one who brought it down."
    else:
        mc "I had... something to do with it."
    scene 29_1_s3_2 with dissolve
    ml "*laughs* Are you serious? Gods above, and to think I was housing the hero of the market this whole time."
    scene 29_1_s3 with dissolve
    if mc_lied:
        mc "Thank you. It's a lot to live up to. Everyone expects me to kill something else now..."
    else:
        mc "I'm no hero. Just stupid luck, really. But enough about me."
    mc "How's your little shop going?"
    scene 29_1_s9 with dissolve
    ml "*sigh* ...Afraid it's the same as always."
    ml "Barely any customers today. My canisters are still full and if they don't get sold soon they might spoil."
    ml "I can't afford to lose another batch. The last one I had to throw out cost me a week's earnings."
    scene 29_1_s10 with dissolve
    if mc_accept_helped_nadia:
        mc "Well, I promised to help, didn't I? Just point me in the direction of this Abel guy."
        scene 29_1_s9 with dissolve
        ml "[mc]... you still remember."
        scene 29_1_s10 with dissolve
        mc "Of course I do. I don't make promises I don't intend to keep."
        scene 29_1_s3_2 with dissolve
        ml "Thank you. Unfortunately, Able left the city the day after we met—off on some business, I think. But he left one of his goons in charge."
        ml "A man named Viktor. You can find him in the tavern over there. It's the biggest one in this district, can't miss it."
        scene 29_1_s3 with dissolve
        mc "Alright. Don't worry, Nadia. I've got this."
        scene 29_1_s3_2 with dissolve
        ml "Just... remember, [mc]. Talking. No violence. And if you can somehow bring the price down, I would be forever in your debt."
        scene 29_1_s3 with dissolve
        mc "Alright. Sit tight. I'll be back soon."
        jump scene29_choice06_op1_2
    else:
        mc "That's rough. That Able guy is still after you, huh?"
        scene 29_1_s9 with dissolve
        ml "Mhm... And, um... [mc]? Would you... ould you be so kind as to help me with that? I know it's a lot to ask. You've got your own problems."
        ml "But Abel's gone from the city for now and he left one of his men in charge. A man named Viktor."
        ml "Could you... maybe just go and tell him to stop pressing me? Tell him I'll pay."
        ml "I just need him to lower the cut. I can't afford what they're asking, I've barely got enough to feed myself. Please."
        scene 29_1_s10 with dissolve
        call screen scene29_choice00 with dissolve

label scene29_choice00_op1:
    $ mc_accept_helped_nadia = True
    mc "I'll do it."
    scene 29_1_s9 with dissolve
    ml "Ahh, [mc]... you have no idea how much this means. I've been losing sleep over this."
    scene 29_1_s10 with dissolve
    mc "Why not tell him yourself? Cut out the middleman?"
    scene 29_1_s9 with dissolve
    ml "I-I can't... I'm too scared, [mc]. The first time they approached, they threatened me so much that I broke down crying..."
    scene 29_1_s10 with dissolve
    mc "That's awful!"
    scene 29_1_s9 with dissolve
    ml "Even after hearing that, [mc]. Talking. No violence. And if you can somehow bring the price down, I would be forever in your debt."
    scene 29_1_s10 with dissolve
    mc "I understand."
    scene 29_1_s3_2 with dissolve
    ml "Thank you. That tavern is right over there. It's the biggest one in this district, you can't miss it."
    scene 29_1_s3 with dissolve
    mc "Alright. Sit tight. I'll be back soon."
    jump scene29_choice06_op1_2

label scene29_choice00_op2:
    mc "Sorry, Nadia. But I don't want to get involved. I already have so much on my plate."
    scene 29_1_s9 with dissolve
    ml "...I understand."
    ml "I shouldn't have asked in the first place. This isn't your burden to carry."
    scene 29_1_s10 with dissolve
    empathy "She forces a small smile to hide her disappointment."
    scene 29_1_s9 with dissolve
    ml "Still... thank you for at least listening."
    scene 29_1_s10 with dissolve
    mc "Take care of yourself, Nadia. Maybe things will get better on their own."
    scene 29_1_s9 with dissolve
    ml "You too... [mc]."
    scene 29_1_s10 with dissolve
    if not mc_met_reham:
        scene 29_s24 with dissolve
        call screen scene29_choice06 with dissolve
    else:
        jump free_roam_main_label
        
label scene29_choice06_op1_2:
    scene 29_1_s3_2 with dissolve
    ml "Actually, wait. Before you go—"  
    scene 29_1_s5 with Dissolve(1.0)
    perception "She reaches for a clean cup and one of her fresh canisters. She pours until the cup nearly brims."
    scene 29_1_s53 with Dissolve(1.0)
    ml "Drink. It's on me. I won't take no for an answer!"
    call screen scene29_choice000 with dissolve

label scene29_choice000_op1:
    if mc_coin > 0:
        $ mc_coin -= 1
        scene 29_1_s54 with dissolve
        mc "I can't just take it for free. You're struggling as it is."  
        scene 29_1_s53 with dissolve
        perception "You slide a bronze coin across the table."  
        play sound "sound_effects/karma_more.mp3" volume 0.2
        if mc_karma < 10:
            $ mc_karma += 1
        $ karma_more = True
        show screen stat_change with easeinright  
        scene 29_1_s54 with dissolve
        mc "Here. Is this enough for a cup?"  
        scene 29_1_s53 with dissolve
        ml "Aww... you really didn't have to, [mc]."  
        hide screen stat_change with easeoutright
        $ karma_more = False
        scene 29_1_s54 with dissolve
        mc "It's fine. Gotta support the local businesses somehow."  
        scene 29_1_s53 with dissolve
        scene 29_1_s6 with Dissolve(1.5)
        mc "*gulps* Ahh..."
        scene 29_1_s7 with dissolve
        ml "What do you think? Be honest."  
        scene 29_1_s3 with Dissolve(1.0)
        mc "Pretty good, actually. Would be a shame for it to just sit here and spoil."
        scene 29_1_s9 with dissolve
        ml "*sigh* Tell me about it... Every day I pour out what doesn't sell. It breaks my heart."
        scene 29_1_s10 with dissolve
        mc "Alright, I'm heading over there now. Time to have a chat with this Viktor fellow."
        scene 29_1_s3_2 with dissolve
        ml "Good luck!"
        scene 29_1_s3 with dissolve
        jump scene29_choice06_op1_3
    else:
        mc "(I don't even have a single coin to give her...)"
        call screen scene29_choice000 with dissolve

label scene29_choice000_op2:
    scene 29_1_s54 with dissolve
    mc "Thank you."
    scene 29_1_s6 with Dissolve(1.5)
    mc "*gulps* Ahh..."
    scene 29_1_s7 with dissolve
    ml "What do you think? Be honest."  
    scene 29_1_s3 with Dissolve(1.0)
    mc "Pretty good, actually. Would be a shame for it to just sit here and spoil."
    scene 29_1_s9 with dissolve
    ml "*sigh* Tell me about it... Every day I pour out what doesn't sell. It breaks my heart."
    scene 29_1_s10 with dissolve
    mc "Alright, I'm heading over there now. Time to have a chat with this Viktor fellow."
    scene 29_1_s3_2 with dissolve
    ml "Good luck!"
    scene 29_1_s3 with dissolve
    jump scene29_choice06_op1_3

label scene29_choice000_op3:
    $ mc_lactose_intolerant = True
    scene 29_1_s54 with dissolve
    mc "Sorry, Nadia, but no milk for me. Lactose intolerant."  
    scene 29_1_s53 with dissolve
    ml "Lactose... intolerant? I've never heard of that. Is it a curse? A disease?"  
    scene 29_1_s54 with dissolve
    mc "Something like that. My body and milk don't get along."
    scene 29_1_s53 with dissolve
    ml "Oh! Don't even worry about it. I'll remember that for next time."
    scene 29_1_s54 with dissolve
    mc "Alright, I'm heading over there now. Time to have a chat with this Viktor fellow."
    jump scene29_choice06_op1_3

label scene29_choice06_op1_3:
    stop music fadeout 1.0 
    scene 29_3_s1 with Fade(1.0,1.0,2.0)
    play music "side_event2.mp3" fadein 3.0 loop
    mc "Hmm? A clown girl?"
    scene 29_3_s2 with Fade(0.5,0.5,0.5)
    perception "She pulls off a few acrobatics that look way too practiced to be just for show. This girl's trained."
    mc "You're pretty good."
    scene 29_3_s3 with Dissolve(1.5)
    cg "Hahh... Ahhn... Th... thank you. *cough*"
    mc "Woah, are you sure you can continue like this? Maybe you should take a rest. You look like you're about to collapse."
    cg "..."
    tom_ "Hey! Can't you see she's working?"
    scene 29_3_s4 with Dissolve(1.0)
    mc "She's tired. Let her rest. Look at her, she can barely stand."
    scene 29_3_s6 with dissolve
    tom_ "You tired, girl?"
    scene 29_3_s7 with dissolve
    cg "No, sir! I'm fine. The show must go on."
    empathy "Her eyes flicker with fear before hardening into obedience."
    scene 29_3_s5 with dissolve
    tom_ "She's fine. See?"
    tom_ "Now—what d'you want?"
    scene 29_3_s4 with dissolve
    mc "I'm here to see Viktor. I was told he's in charge while Abel's away."
    scene 29_3_s5 with dissolve
    tom_ "Why? Who's asking?"
    scene 29_3_s4 with dissolve
    mc "Me. I came on behalf of that woman selling milk. Nadia. The one you've been harassing."
    scene 29_3_s5 with dissolve
    tom_ "Her? What, did she finally come to her senses? Took her long enough."
    scene 29_3_s4 with dissolve
    mc "I want you to stop harassing her. She wants to pay. She just needs fair terms."
    scene 29_3_s5 with dissolve
    tom_ "Not here. Follow me."
    scene 29_3_s4 with dissolve
    scene 29_3_s8 with Fade(1.0,1.0,2.0)
    env "The air is thick with the smell of ale, sweat, and smoke clinging to every wooden beam."
    tom_ "Vic, this man wants to talk to you. Says he's here about the milkmaid."
    tom_ "Sit."
    scene 29_3_s9 with Fade(0.5,0.5,0.5)
    vic "..."
    mc "I'm—"
    scene 29_3_s10 with dissolve
    vic "No need. I know who you are, [mc]."
    scene 29_3_s9 with dissolve
    mc "...Did you know that I was coming here?"
    scene 29_3_s10 with dissolve
    vic "The market talks. A celebration, an ogre dead. Nobody knew the hand behind it—"
    vic "—until whispers of an outsider under the Queen's roof reached our ears."
    scene 29_3_s9 with dissolve
    mc "Did your homework, I see."
    scene 29_3_s10 with dissolve
    vic "*chuckles* Nah. The truth always floats to the surface eventually."
    vic "And now here you are, sitting in front of me. My boss, Able, finds you... interesting."
    scene 29_3_s9 with dissolve
    mc "Me? Why?"
    scene 29_3_s14 with Dissolve(1.0)
    vic "I just told you why~ *gulp*"
    if mc_truth:
        mc "Well, your boss is mistaken. I didn't kill the ogre. Wrong place, wrong time, nothing more."
        scene 29_3_s10 with Dissolve(1.0)
        vic "Whether you did or didn't, I doubt Able will let such... potential... slip through his fingers."
    else:
        scene 29_3_s10 with dissolve
    vic "But enough about that. What is it you truly came here for?"
    scene 29_3_s9 with dissolve
    mc "I want you to stop harassing that woman selling milk. Nadia. She's terrified."
    mc "She can't run her business with your men threatening her customers and spreading lies about her."
    scene 29_3_s10 with dissolve
    vic "Nadia? Who...?"
    vic "Ah! The one with the... interesting outfit. She already refused Able's offer."
    scene 29_3_s9 with dissolve
    mc "She'll pay. So leave her be."
    scene 29_3_s10 with dissolve
    vic "Done."
    scene 29_3_s9 with dissolve
    mc "And I want you to lower the price for her. She can't afford what you're demanding."
    scene 29_3_s10 with dissolve
    vic "*chuckles* Done."
    vic "You know what? I feel like you care about her, so... She doesn't have to pay anything anymore."
    scene 29_3_s9 with dissolve
    mc "...Really? Just like that?"
    scene 29_3_s12 with Dissolve(1.0)
    vic "Why not? You'll find us very... accommodating, [mc]. Despite what the locals say."
    scene 29_3_s13 with dissolve
    mc "I don't believe it. No one gives something for nothing. What do you want in return?"
    scene 29_3_s12 with dissolve
    vic "Sharp. I simply want you to keep your ears open. When my boss returns, there will be work."
    scene 29_3_s13 with dissolve
    mc "What kind of work?"
    scene 29_3_s12 with dissolve
    vic "No need to rush. We'll discuss it when the time comes. Nothing binding. Just... a conversation. A handshake between friends."
    scene 29_3_s13 with dissolve
    mc "...Fine. But I'll choose which jobs to take, and which to refuse."
    scene 29_3_s12 with dissolve
    vic "Naturally. No one here deals in chains. Only handshakes."
    vic "So tell me, [mc]... Are you satisfied?"
    scene 29_3_s13 with dissolve
    call screen scene29_choice0000 with dissolve
    
label scene29_choice0000_op1:
    mc "I am."
    scene 29_3_s10 with dissolve
    vic "Perfect. Then we'll see each other, sooner or later. The city isn't as large as it seems."
    scene 29_3_s9 with dissolve
    mc "Right."
    jump scene29_choice06_op1_4

label scene29_choice0000_op2:
    $ mc_helped_petra = True
    mc "The girl outside..."
    scene 29_3_s10 with dissolve
    vic "The performer? What about her?"
    scene 29_3_s9 with dissolve
    mc "Yes. She's exhausted. I don't like how she's being treated."
    scene 29_3_s10 with dissolve
    vic "*tch* Poor girl. She should've told me so. I don't tolerate that kind of carelessness with my people."
    scene 29_3_s11 with dissolve
    play sound "sound_effects/karma_more.mp3" volume 0.2
    if mc_karma < 10:
        $ mc_karma += 1
    $ karma_more = True
    show screen stat_change with easeinright
    vic "Tom. Bring her in. A room, a bath, a proper meal. And Tom—no hands. Chop chop."
    scene 29_3_s9 with Dissolve(1.0)
    tom "Nghnn... Got it."
    hide screen stat_change with easeoutright
    $ karma_more = False
    scene 29_3_s10 with dissolve
    vic "Anything else?"
    scene 29_3_s9 with dissolve
    mc "That's all. For now."
    scene 29_3_s10 with dissolve
    vic "Good."
    vic "And did I ever mention how damn good you look, [mc]? It's the confidence. Really brings out your features."
    scene 29_3_s9 with dissolve
    mc "..."
    scene 29_3_s10 with dissolve
    vic "*chuckles* Relax, man. I'm just complementing you."
    scene 29_3_s9 with dissolve
    mc "Right... Thanks. I'll see myself out."
    stop music fadeout 2.0 
    jump scene29_choice06_op1_4

label scene29_choice06_op1_4:
    scene 29_s27 with Fade(1.0,1.0,1.0)
    play music "date1.mp3" fadein 3.0 loop
    mc "(Hmm? Where did she go?)"  
    scene 29_3_s15 with Fade(1.0,1.0,1.0)
    perception "You scan the market. Her stall sits empty—until you spot her pacing nervously near the well."  
    mc "(There!)"
    scene 29_3_s16 with Dissolve(2.0)
    ml "Shit! Shit! Shit! What if they hurt him? What if he never comes back? This is all my fault! I never should have asked—"
    mc "Nadia?"  
    scene 29_3_s17 with dissolve
    ml "Oh, it's you, [mc]... Thank the gods. Sorry, I didn't mean to worry you. Every minute felt like an hour."  
    scene 29_3_s18 with dissolve
    mc "What's wrong?"  
    scene 29_3_s17 with dissolve
    ml "I was too anxious. I couldn't sit still waiting for you."  
    ml "Anyway—tell me! How did it go? Will they let me keep selling?"  
    scene 29_3_s18 with dissolve
    mc "Actually... I've got good news."  
    empathy "Her breath catches, eyes wide, shoulders tense. She's bracing for the worst because the worst is all she's ever gotten."  
    mc "You don't need to pay anything."
    scene 29_3_s17 with vpunch
    ml "A-Are you serious?!" 
    scene 29_3_s18 with dissolve 
    mc "Yup. Not a single coin. You're free to sell without them bothering you."  
    scene 29_3_s17 with dissolve
    ml "But... why? Why show mercy all of a sudden?"  
    scene 29_3_s18 with dissolve
    mc "Well... turns out they already knew me. They said they want me to work with them, instead. A favor for a favor I guess."
    scene 29_3_s17 with dissolve
    ml "Oh no... [mc], I'm so sorry! This is my fault. I never should have dragged you into this!" 
    scene 29_3_s18 with dissolve
    mc "Hey, hey. Relax. It's nothing binding. I didn't sign my life away or anything."  
    scene 29_3_s17 with dissolve
    ml "Still... I should have known they'd try to recruit you. They're always looking for people with power."  
    scene 29_3_s18 with dissolve
    mc "Recruit me? What are they, a guild?"
    scene 29_3_s17 with dissolve
    ml "Not officially. In the eyes of the court, they're an {i}organization.{/i} But really? They're a gang."
    scene 29_3_s18 with dissolve
    mc "Let's not worry about that for now. I came back because I wanted to see you smile. That was the whole point."
    scene 29_3_s19 with dissolve
    perception "Her eyes glisten, a small laugh breaking through her nerves. She quickly wipes at her cheek with the back of her hand."
    scene 29_3_s20 with dissolve
    ml "Thank you... I don't know how I'm ever supposed to repay you, [mc]."
    scene 29_3_s19 with dissolve
    mc "Just happy to help."
    scene 29_3_s20 with dissolve
    ml "No. I won't accept that."
    ml "You did all this, and even risked dealing with people like them."
    scene 29_3_s19 with dissolve
    empathy "Her voice trembles, a mix of gratitude and confusion breaking through."
    scene 29_3_s17 with Dissolve(1.0)
    ml "But... I-I don't understand. What does this mean? Why you'd go through all that for me..."
    scene 29_3_s18 with dissolve
    call screen scene29_choice00000 with dissolve
    
label scene29_choice00000_op1:
    $ mc_harem_nadia = True
    scene 29_3_s22 with Dissolve(1.5)
    ml "Uh... [mc]? You're getting a little too close..."
    scene 29_3_s21 with dissolve
    mc "I did this because of you, Nadia."
    scene 29_3_s22 with dissolve
    ml "...W-What?"
    scene 29_3_s21 with dissolve
    mc "Yes, I wanted to help—but more than that, I did it for you."
    mc "You helped me when I had nothing. You gave me a place to sleep when I was out on the streets."
    mc "And somewhere between the line... I... I started to care. More than I expected."
    scene 29_3_s22 with dissolve
    ml "[mc]... I-I don't know how to feel about this. I never thought... I mean, you're a hero, a-and I'm just a milkmaid, and—"  
    scene 29_3_s21 with dissolve
    mc "You don't have to answer now. Take your time... but I've already made up my mind."  
    ml "..."
    scene 29_3_s22 with dissolve
    ml "I... I should go."
    scene 29_3_s21 with dissolve
    mc "Go? W-Where?"
    ml "..."
    scene 29_3_s23 with Fade(0.5,0.5,0.5)
    mc "(She needs space... I'll give her time. I should visit her again later.)"  
    begger "Tch. Amateur." 
    scene 29_s22 with Dissolve(1.5)
    mc "...What?"
    scene 29_s21 with dissolve
    begger "You're doing it wrong. All that flirting, all that sweet talk."  
    begger "The smart ones? They don't bother. No intimacy, no buildup. Straight to fucking."  
    scene 29_s22 with dissolve
    mc "Just shut up, man."  
    begger "..." 
    if not mc_met_reham:
        stop music fadeout 2.0 
        scene 29_s27 with Fade(1.0,1.0,1.0)
        mc "(I guess I could check out that merchant now.)"
        play music "market2.mp3" fadein 2.0 loop
        call screen scene29_choice06 with dissolve
    else:
        mc "(I'm tired. I guess I'll head back to the castle.)"
        scene black with Fade(1.0,1.0,1.0)
        jump free_roam_main_label

label scene29_choice00000_op2:
    $ mc_friend_nadia = True
    mc "I just wanted to help, that's all."  
    scene 29_3_s17 with dissolve
    ml "Is that really why?"  
    scene 29_3_s18 with dissolve
    mc "Yes. Don't think too much about it, Nadia."  
    scene 29_3_s20 with dissolve
    ml "...I see. Thank you. If anything—you're always welcome in my home, should you ever find yourself lost, [mc]."  
    scene 29_3_s19 with dissolve
    mc "I don't think I'll need to, but I appreciate it."  
    scene 29_3_s20 with dissolve
    ml "*laughs* Hopefully not. But still... you've just made yourself a lifelong friend!"  
    scene 29_3_s19 with dissolve
    mc "*chuckles* I'll take it."  
    mc "Anyway... I have to leave now. Will you be alright? Back to your stall, back to your business?"  
    scene 29_3_s20 with dissolve
    ml "Yes. Thanks to you, my business should survive! I'll actually be able to sell milk without looking over my shoulder every five minutes."  
    scene 29_3_s19 with dissolve
    mc "Good. See you, Nadia."  
    scene 29_3_s20 with dissolve
    ml "See you, [mc]! And don't forget to visit every once in a while—your drinks will always be on me!" 
    scene 29_3_s19 with dissolve
    if not mc_met_reham:
        stop music fadeout 2.0 
        scene 29_s24 with Fade(1.0,1.0,1.0)
        mc "(I guess I could check out that merchant now.)"
        play music "market2.mp3" fadein 2.0 loop
        call screen scene29_choice06 with dissolve
    else:
        mc "(I'm tired. I guess I'll head back to the castle.)"
        scene black with Fade(1.0,1.0,1.0)
        jump free_roam_main_label

label mc_harem_talk_nadia2:
    scene 29_1_s26 with Fade(1.0,1.0,1.0)
    perception "You position yourself behind her. She remains silent, waiting... anticipating your next move."
    impulse "Listen, champ. You see that tight little anus staring back at you? Yeah, that one. You know what to do. No warnings. No teasing. Just grab her hips and claim it. Make her feel it every inch of it."
    call screen scene29_choice09 with dissolve

default scene29_spank_count = 0
label scene29_choice09_op1:
    if scene29_spank_count == 0:
        play sound "sound_effects/slap01.mp3"
        scene 29_1_s27 with vpunch
        sensation "Your palm meets her ass with a sharp smack. The flesh ripples under your touch. Soft, yet firm, like it was made to be grabbed."
        ml "Ah! Hey! Why did you do that?"
        scene 29_1_s26 with dissolve
        $ scene29_spank_count += 1
        call screen scene29_choice09 with dissolve
    elif scene29_spank_count == 1:
        play sound "sound_effects/slap01.mp3"
        scene 29_1_s27 with vpunch
        ml "Ahh!"
        scene 29_1_s26 with dissolve
        $ scene29_spank_count += 1
        call screen scene29_choice09 with dissolve
    elif scene29_spank_count == 2:
        play sound "sound_effects/slap01.mp3"
        scene 29_1_s27 with vpunch
        ml "Ow!"
        scene 29_1_s26 with dissolve
        $ scene29_spank_count += 1
        call screen scene29_choice09 with dissolve
    elif scene29_spank_count == 3:
        play sound "sound_effects/slap01.mp3"
        scene 29_1_s27 with vpunch
        ml "Hngg! Is there a reason why you keep slapping my ass?!"
        scene 29_1_s26 with dissolve
        $ scene29_spank_count += 1
        call screen scene29_choice09 with dissolve
    elif scene29_spank_count == 4:
        play sound "sound_effects/slap01.mp3"
        scene 29_1_s27 with vpunch
        ml "Alright, that's enough!"
        scene 29_1_s26 with dissolve
        impulse "She is ready now, my liege. Plant your banner where no man has dared before. Right. In. Her. Ass."
        $ scene29_spank_count += 1
        call screen scene29_choice09 with dissolve

image is_nadia_anim_vsex1 = Movie(play="images/2_chapter1/scene29_1/29_anim_vsex1.webm", loop=True)
image is_nadia_anim_vsex2 = Movie(play="images/2_chapter1/scene29_1/29_anim_vsex2.webm", loop=True)
image is_nadia_anim_asex1 = Movie(play="images/2_chapter1/scene29_1/29_anim_asex1.webm", loop=True)
image is_nadia_anim_asex2 = Movie(play="images/2_chapter1/scene29_1/29_anim_asex2.webm", loop=True)

image is_nadia_anim_vsex1_faster = Movie(play="images/2_chapter1/scene29_1/29_anim_vsex1_faster.webm", loop=True)
image is_nadia_anim_vsex2_faster = Movie(play="images/2_chapter1/scene29_1/29_anim_vsex2_faster.webm", loop=True)
image is_nadia_anim_asex1_faster = Movie(play="images/2_chapter1/scene29_1/29_anim_asex1_faster.webm", loop=True)
image is_nadia_anim_asex2_faster = Movie(play="images/2_chapter1/scene29_1/29_anim_asex2_faster.webm", loop=True)

default is_nadia_anim_vsex1 = False
default is_nadia_anim_vsex2 = False
#default is_nadia_anim_vsex3 = False

default nadia_sex_pov_toggle = True
default nadia_sex_pos_toggle = True
####
default is_nadia_anim_asex1 = False
default is_nadia_anim_asex2 = False

default is_nadia_vsex_first = True
default is_nadia_asex_first = True

label scene29_choice09_op2:
    $ is_nadia_anim_asex1 = False
    $ is_nadia_anim_vsex1 = True
    scene 29_1_s30 with dissolve
    $ nadia_pussy_virgin = False
    sensation "Her pussy is slick, pulsing around you—warm, wet. She must have been anticipating this more than she'd ever admit."
    if not is_nadia_asex_first:
        ml "So now you go for my vagina? Couldn't you have started with that first?!"
        mc "I told you why."
    scene 29_1_s33 with dissolve
    ml "H-Hey... W-Wait... it's so... ngh!"
    scene 29_1_s30 with dissolve
    ""
    play sound "se_sfx/sex/sex2.mp3" 
    scene 29_1_s31 with dissolve
    ml "Ahh—! I-It's so... ngh... big!"
    mc "Just relax."
    show is_nadia_anim_vsex1 with dissolve
    ml "N-No, I mean... ngh! It's really filling me up...!"
    ml "Hahh... It's so much... I can f-feel everything..."
    mc "Good. I want you to feel every inch of me."
    $ is_nadia_vsex_first = False
    call screen scene29_nadia_sex with dissolve

label scene29_choice09_op3:
    $ is_nadia_anim_asex1 = True
    $ is_nadia_anim_vsex1 = False
    $ nadia_anus_virgin = False
    if not is_nadia_vsex_first:
        scene 29_1_s30 with dissolve
        ml "Huh? Why are you taking it out?"
    scene 29_1_s28 with dissolve
    sensation "Her anus clenches around you, heat radiating from within. It takes some effort to push in, but the tightness only fuels your desire."
    scene 29_1_s32 with dissolve
    ml "H-Hey! Where the hell are you putting that?!"
    scene 29_1_s28 with dissolve
    mc "Relax, I have to do this first."
    play sound "se_sfx/sex/sex5.mp3" 
    scene 29_1_s29 with dissolve
    ml "Huh? What do yo—AHHHH!!"
    show is_nadia_anim_asex1 with dissolve
    ml "Aaaaahhhhh!"
    ml "Ah! I-It's so... ngh... big! W-Why did you... ngh! Put it in my ass?!"
    play sound "sound_effects/karma_less.mp3" volume 0.2
    if mc_karma > 1:
        $ mc_karma -= 2
    $ karma_less = True
    show screen stat_change with easeinright
    mc "It's my condition... I can't get fully hard unless I start with the ass first."
    ml "W-What kind of—Ngh!—condition is that?!"
    logic "It's called a reverse arousal reflex."
    $ karma_less = False
    hide screen stat_change with easeoutright
    $ is_nadia_asex_first = False
    mc "Some rare disorder... 'reverse arousal reflex.' Doctor said there's no cure. Real tragedy, honestly."
    ml "Ngh... That... just sounds... ahhh! Ridiculous!"
    mc "Yeah, sorry. I'm just teasing you. Your ass just looked really inviting, Nadia."
    ml "I-I... I can't believe this...! Ngh!"
    call screen scene29_nadia_sex with dissolve

default scene29_in_sex1 = True
label is_nadia_vsex:
    if is_nadia_vsex_first:
        jump scene29_choice09_op2
    else:
        if scene29_in_sex1:
            jump is_nadia_sex1
        else:
            jump is_nadia_sex2

label is_nadia_asex:
    if is_nadia_asex_first:
        jump scene29_choice09_op3
    else:
        if scene29_in_sex1:
            jump is_nadia_sex1
        else:
            jump is_nadia_sex2

label is_nadia_sex1:
    $ scene29_in_sex1 = True
    $ scene29_in_sex2 = False
    if is_nadia_anim_vsex1 or is_nadia_anim_vsex2:
        $ is_nadia_anim_vsex1 = True
        $ is_nadia_anim_vsex2 = False
        scene black with Dissolve(0.3)
        show is_nadia_anim_vsex1 with dissolve
        ml "Ahhh~ Hah~ I... can't believe we're really doing this..."
        perception "Her body shudders with each thrust, gripping onto the moment, savoring every inch. She's in no rush for this to end."
        call screen scene29_nadia_sex with dissolve
    elif is_nadia_anim_asex1 or is_nadia_anim_asex2:
        $ is_nadia_anim_asex1 = True
        $ is_nadia_anim_asex2 = False
        scene black with Dissolve(0.3)
        show is_nadia_anim_asex1 with dissolve
        sensation "Her tightness slowly yields, molding around you, accepting you. Soon enough, she won't just endure it—she'll crave it."
        call screen scene29_nadia_sex with dissolve

label is_nadia_sex2:
    $ scene29_in_sex1 = False
    $ scene29_in_sex2 = True
    if is_nadia_anim_vsex1 or is_nadia_anim_vsex2:
        scene black with Dissolve(0.3)
        show is_nadia_anim_vsex2 with dissolve
        $ is_nadia_anim_vsex1 = False
        $ is_nadia_anim_vsex2 = True
        ml "Ahnnn~ Hah~"
        call screen scene29_nadia_sex with dissolve
    elif is_nadia_anim_asex1 or is_nadia_anim_asex2:
        $ is_nadia_anim_asex1 = False
        $ is_nadia_anim_asex2 = True
        scene black with Dissolve(0.3)
        show is_nadia_anim_asex2 with dissolve
        ml "Goddamn it... Ahh... Fuck..."
        call screen scene29_nadia_sex with dissolve

label is_nadia_sex_faster:
    #scene black with Dissolve(0.3)
    if is_nadia_anim_vsex1:
        show is_nadia_anim_vsex1_faster with dissolve
        hide is_nadia_anim_vsex1 with dissolve
        ml "Hah~ Ahh~ We don't... Nhnn~ Have to be quick..."
        call screen scene29_nadia_sex with dissolve
    elif is_nadia_anim_vsex2:
        show is_nadia_anim_vsex2_faster with dissolve
        hide is_nadia_anim_vsex2
        ml "Nhnn~ Please... F-Fill me up..."
        call screen scene29_nadia_sex with dissolve
    elif is_nadia_anim_asex1:
        show is_nadia_anim_asex1_faster with dissolve
        hide is_nadia_anim_asex1
        ml "Ahhh! Hah! My... ass!"
        call screen scene29_nadia_sex with dissolve
    elif is_nadia_anim_asex2:
        show is_nadia_anim_asex2_faster with dissolve
        hide is_nadia_anim_asex2
        ml "Remind... Ah! Why... are we even doing... Ahngg! This?"
        call screen scene29_nadia_sex with dissolve

label is_nadia_sex_cum_inside:
    if is_nadia_anim_vsex1 or is_nadia_anim_vsex2:
        sensation "You slide in and out of her, each thrust sending waves of pleasure coursing through your body. The rhythm builds, tension coils, and suddenly you can't hold back anymore. It's time."
        ml "Do it inside! Fill up my womb~!"
        if not is_nadia_asex_first:
            play sound "se_sfx/blowjob/facial4.mp3" 

            if persistent.xray_mode:
                scene 29_1_s31_xray1 with vpunch
                mc "Nhngg!"
                sensation "Powerful spurts shoot out from your cock and right into her uterus."
                play sound "se_sfx/blowjob/facial3.mp3" 
                scene 29_1_s37_xray2 with vpunch
                ml "Ahhh!"
                scene 29_1_s38_xray3 with dissolve
            else:
                scene 29_1_s31 with vpunch
                mc "Nhngg!"
                sensation "Powerful spurts shoot out from your cock and right into her uterus."
                play sound "se_sfx/blowjob/facial3.mp3" 
                scene 29_1_s37 with vpunch
                ml "Ahhh!"
                scene 29_1_s38 with dissolve

            ml "Ahhh! Hnnnnn~ So much... I can feel it all the way inside..."
            ml "Ahh... Hnnn..."
            call pregnancy_check_nadia from _pregnancy_check_nadia
            mc "You took so well, Nadia."
            ml "Bastard..."
            mc "...What?"
            scene 29_1_s45 with dissolve
            ml "Was penetrating my ass really neccessary?"
            scene 29_1_s46 with dissolve
            mc "I... Sorry."
            scene 29_1_s45 with dissolve
            ml "You're sorry?!"
            scene 29_1_s46 with dissolve
            perception "It felt like she was about to say something but stopped at the very last second."
            ml "*sigh*"
            scene 29_1_s41 with dissolve
            ml "I could've handled being screwed in one hole, but both? That was too much..."
            perception "Her slightly gaping ass twitches as she speaks."
            ml "Say something..."
            scene 29_1_s42 with dissolve
            mc "I'm sorry, Nadia."
            ml "..."
            scene 29_1_s41 with dissolve
            ml "*sigh* I'm not the type to hold grudges so... I'll forgive you."
            scene 29_1_s42 with dissolve
            mc "Thank you. I won't do it again."
            scene 29_1_s43 with dissolve
            ml "Hey... who said anything about not doing it again?"
            scene 29_1_s44 with dissolve
            mc "You mean...?"
            scene 29_1_s43 with dissolve
            ml "I... I might get used to it in the ass... *chuckles* Who knows?"
            scene 29_1_s44 with dissolve
            mc "In the case, I'll make sure that you do."
            scene 29_1_s41 with dissolve
            ml "Alright, calm down. My ass will be sore for days. So no butt stuff for a while."
            scene 29_1_s43 with dissolve
            ml "Anyway... you ejaculated inside my womb, and that's all that matters."  
            scene 29_1_s42 with dissolve
            mc "*chuckles* What if it didn't work though? We could try again now."  
            scene 29_1_s45 with dissolve
            ml "Again?! No, thank you. I don't think I can even stand after this..."
            perception "Her legs wobble, her body trembles, and her breathing is still unsteady. Yeah, she's not lying."
            scene 29_1_s41 with dissolve
            ml "I'll need a long, long rest."
            scene 29_1_s42 with dissolve
            mc "I get it. Take as long as you need. I'll come visit whenever I can."  
            scene 29_1_s43 with dissolve
            ml "V-Visiting? You... you won't be living with me?"  
            scene 29_1_s44 with dissolve
            mc "Sorry, Nadia. The Queen gave me a place at the castle. And I doubt she'll let me out of her sight even if I tried."  
            scene 29_1_s43 with dissolve
            ml "Aww... that's a shame. I would've loved to have you here... helping me with my business, keeping me company..."  
            ml "Sleeping together every night..."  
            scene 29_1_s44 with dissolve
            mc "We'll still be doing all of that. Just... when the time is right."  
            scene 29_1_s43 with dissolve
            ml "*sigh* I suppose there isn't much you can do about it." 
            ml "Then promise me this. Come visit me often, you hear?"  
            scene 29_1_s42 with dissolve
            mc "I will."
            perception "Her tired smile lingers as you pull yourself together. The warmth in her eyes tells you she meant every word."  
            mc "Anyway, I should go. It's getting late."  
            scene 29_1_s41 with dissolve
            ml "Mhmm... see you soon, [mc]. Don't make me wait too long." 
            scene 29_1_s42 with dissolve
            scene black with Fade(1.5,1.0,1.0)
            perception "You steal one last glance before closing the door. She's still slumped over the table, her breath coming in quick, uneven gasps. A mess, in more ways than one."
            $ renpy.end_replay()
            jump free_roam_main_label
        else:
            play sound "se_sfx/blowjob/facial4.mp3" 

            if persistent.xray_mode:
                scene 29_1_s31_xray1 with vpunch
                mc "Nhngg!"
                sensation "Powerful spurts shoot out from your cock and right into her uterus."
                play sound "se_sfx/blowjob/facial5.mp3" 
                scene 29_1_s37_xray2 with vpunch
                ml "Ahhh!"
                scene 29_1_s38_xray3 with dissolve
                ml "Hnnnnn~ So much... I can feel it all the way inside..."
            else:
                scene 29_1_s31 with vpunch
                mc "Nhngg!"
                sensation "Powerful spurts shoot out from your cock and right into her uterus."
                play sound "se_sfx/blowjob/facial5.mp3" 
                scene 29_1_s37 with vpunch
                ml "Ahhh!"
                scene 29_1_s38 with dissolve
                ml "Hnnnnn~ So much... I can feel it all the way inside..."

            ml "Ahh... hah..."
            call pregnancy_check_nadia from __pregnancy_check_nadia
            mc "Now we wait."
            ml "Y-Yes... I guess we do..."
            mc "Should we... go again? *chuckles* It might not have worked this time."
            scene 29_1_s43 with dissolve
            ml "Again?! No, thank you. I don't think I can even stand after this..."
            perception "Her legs wobble, her body trembles, and her breathing is still unsteady. Yeah, she's not lying."
            scene 29_1_s41 with dissolve
            ml "I'll need to take a long rest."
            scene 29_1_s42 with dissolve
            perception "Her pussy twitches, a few drops of your semen slipping down her thigh before dripping onto the floor."
            mc "I get it. Take as long as you need. I'll come visit whenever I can."  
            scene 29_1_s43 with dissolve
            ml "V-Visiting? You... you won't be living with me?"  
            scene 29_1_s44 with dissolve
            mc "Sorry, Nadia. The Queen gave me a place at the castle. And I doubt she'll let me out of her sight even if I tried."  
            scene 29_1_s43 with dissolve
            ml "Aww... that's a shame. I would've loved to have you here... helping me with my business, keeping me company..."  
            ml "Sleeping together every night..."  
            scene 29_1_s44 with dissolve
            mc "We'll still be doing all of that. Just... when the time is right."  
            scene 29_1_s43 with dissolve
            ml "*sigh* I suppose there isn't much you can do about it." 
            ml "Then promise me this. Come visit me often, you hear?"  
            scene 29_1_s42 with dissolve
            mc "I will."
            perception "Her tired smile lingers as you pull yourself together. The warmth in her eyes tells you she meant every word."  
            mc "Anyway, I should go. It's getting late."  
            scene 29_1_s41 with dissolve
            ml "Mhmm... see you soon, [mc]. Don't make me wait too long." 
            scene 29_1_s42 with dissolve
            scene black with Fade(1.5,1.0,1.0)
            perception "You steal one last glance before closing the door. She's still slumped over the table, her breath coming in quick, uneven gasps. A mess, in more ways than one."
            $ renpy.end_replay()
            jump free_roam_main_label
    if is_nadia_anim_asex1 or is_nadia_anim_asex2:
        $ mc_nadia_pregnant = False
        sensation "You slide in and out of her, each thrust sending waves of pleasure coursing through your body and only yours. The rhythm builds, tension coils, and suddenly you can't hold back anymore. It's time."
        play sound "se_sfx/blowjob/facial5.mp3" 
        scene 29_1_s34 with vpunch
        mc "Nhngg!"
        sensation "Powerful spurts shoot out from you cock and right into her colon." 
        play sound "se_sfx/blowjob/facial3.mp3" 
        scene 29_1_s35 with vpunch  
        ml "Ahhh!"
        sensation "Her anus clenched around your cock, it's unlikely she did this consciously. Regardless it further increases your desire."
        scene 29_1_s36 with dissolve
        ml "Hah.. ahh..."
        ml "HEY! Where the hell did you finish?!"
        mc "In your—"
        ml "YOU—You finished in my ass?!"
        mc "...Yeah."
        ml "What the hell is WRONG with you?! That was NOT the what i wanted!"
        mc "..."
        ml "Say something!"
        mc "I'm sorry, Nadia."
        ml "I cannot believe this... And you... Ngh! My ass..." 
        scene 29_1_s36 with dissolve
        perception "She exhales slowly, as if weighing the weight of her actions. Her anus clenches and releases frantically while thick seed drips down her thighs."
        sensation "The sight alone stirs something in you, heat pooling between your legs. Maybe you should look away before you get any ideas."
        ml "Look."
        scene 29_1_s44 with dissolve
        perception "Her voice is different this time. Lower, more serious."
        mc "...Yes?"
        scene 29_1_s43 with dissolve
        ml "I'll give you a second chance... just promise you won't play with me like this."
        scene 29_1_s44 with dissolve
        mc "I promise."
        ml "..."
        scene 29_1_s41 with dissolve
        ml "*sigh* I'm not the type to hold grudges so... I'll forgive you."
        scene 29_1_s42 with dissolve
        mc "Thank you. I won't put it in your ass again."
        scene 29_1_s43 with dissolve
        ml "Hey... who said anything about not doing it again?"
        scene 29_1_s44 with dissolve
        mc "You mean...?"
        scene 29_1_s43 with dissolve
        ml "I... I might get used to it in the ass... *chuckles* Who knows?"
        scene 29_1_s44 with dissolve
        mc "In the case, I'll make sure that you do."
        scene 29_1_s43 with dissolve
        ml "Alright, calm down. My ass will be sore for days. So no butt stuff for a while."
        scene 29_1_s44 with dissolve
        mc "Why don't I... you know... go again. In the right hole this time."
        scene 29_1_s43 with dissolve
        ml "Go again?! Do you really think I can handle another round after this?"
        perception "She squeezes her muscles in a desperate attempt to close up, but it's no use—more of your seed trickles down, pooling onto the floor."
        ml "I'll need to take a long, long rest."
        scene 29_1_s44 with dissolve
        mc "I get it. Take as long as you need. I'll come visit whenever I can."  
        scene 29_1_s43 with dissolve
        ml "V-Visiting? You... you won't be living with me?"  
        scene 29_1_s44 with dissolve
        mc "Sorry, Nadia. The Queen gave me a place at the castle. And I doubt she'll let me out of her sight even if I tried."  
        scene 29_1_s43 with dissolve
        ml "Aww... that's a shame. I would've loved to have you here... helping me with my business, keeping me company..."  
        ml "Sleeping together every night..."  
        scene 29_1_s44 with dissolve
        mc "We'll still be doing all of that. Just... when the time is right."  
        scene 29_1_s43 with dissolve
        ml "*sigh* I suppose there isn't much you can do about it." 
        ml "Then promise me this. Come visit me often, you hear?"  
        scene 29_1_s42 with dissolve
        mc "I will."
        perception "Her tired smile lingers as you pull yourself together. The warmth in her eyes tells you she meant every word."  
        mc "Anyway, I should go. It's getting late."  
        scene 29_1_s41 with dissolve
        ml "Mhmm... see you soon, [mc]. Don't make me wait too long." 
        scene 29_1_s42 with dissolve
        scene black with Fade(1.5,1.0,1.0)
        perception "You steal one last glance before closing the door. She's still slumped over the table, her breath coming in quick, uneven gasps. A mess, in more ways than one."
        $ renpy.end_replay()
        jump free_roam_main_label

default mc_flirted_slady = False
default mc_flirted_slady_twice = False
label scene29_choice03_op1:
    $ mc_flirted_slady = True
    mc "You."
    scene 29_s19 with dissolve
    slady "Huh? Oh... uh... that's very kind of you, sir, but I'm already married."
    slady "Anything else, perhaps?"
    scene 29_s18 with dissolve
    if maia_sad:
        mc "(I guess I could buy Maia some strawberries to get her to feel better.)"
    mc "What about strawberries then? The next best thing after you."
    perception "She shifts uncomfortably, her smile faltering."
    scene 29_s17 with dissolve
    slady "R-Right... three c coins a basket, sir."
    scene 29_s18 with dissolve
    call screen scene29_choice04 with dissolve

label scene29_choice03_op1_2:
    $ mc_flirted_slady_twice = True
    mc "You."
    scene 29_s19 with dissolve
    slady "Sir! That's enough! I already told you, I'm married. If you're not here to buy something, please leave." 
    scene 29_s18 with dissolve
    call screen scene29_choice04 with dissolve

label scene29_choice03_op2:
    mc "Do you have strawberries?"
    scene 29_s17 with dissolve
    slady "Of course, sir. Three bronze coins a basket."
    scene 29_s18 with dissolve
    call screen scene29_choice04 with dissolve

label scene29_strawberries:
    if mc_coin >= 3:
        $ mc_has_strawberries = True
        $ mc_coin -= 3
        mc "Here you go."
        scene 29_s17 with dissolve
        slady "Thank you, sir. Enjoy!"
        scene 29_s18 with dissolve
        $ renpy.notify("You got strawberries!")
        jump scene29_free_roam_right
    else:
        perception "{color=#4A90E2}You pat your pockets, but they're disappointingly light.{/color}"
        mc "Ah... Sorry, I changed my mind."
        scene 29_s17 with dissolve
        slady "No problem, sir."
        scene 29_s18 with dissolve
        jump scene29_free_roam_right

label scene29_free_roam_right_up_no:
    mc "(No reason to go there anymore, I already got the strawberries.)"
    jump scene29_free_roam_right

label scene29_nostrawberries:
    mc "Nevermind, I changed my mind."
    scene 29_s17 with dissolve
    slady "No problem, sir."
    scene 29_s18 with dissolve
    jump scene29_free_roam_right

label scene29_choice06_op2:
    $ mc_met_reham = True
    $ mc_met_slaver = True
    if not mc_not_interested_slaver:
        scene 29_2_s1 with Fade(0.5,0.5,0.5)
        mc "Hey."
        scene 29_2_s2 with dissolve
        sl "Ah, welcome, sir! You have a discerning eye, stopping here of all places."  
        scene 29_2_s1 with dissolve
        mc "What's going on here?"  
        scene 29_2_s2 with dissolve
        sl "A rare opportunity, that's what. This fine woman before you is Reham—straight from my homeland, where grace and discipline are considered valuable qualities in those who serve."
        scene 29_2_s1 with dissolve
    else:
        scene 29_2_s2 with dissolve
        sl "Welcome, sir! Have you changed your mind?"
        scene 29_2_s1 with dissolve
    call screen scene29_choice10 with dissolve

label scene29_choice10_op1:
    mc "Tell me more. What exactly are you selling here?"
    scene 29_2_s16 with dissolve
    sl "Ah! A man of curiosity. I admire that. Reham is a rare find—trained in the domestic arts, skilled in cooking and cleaning, and, should you desire, can bear you strong children."
    sl "She's young, healthy, and has been thoroughly vetted."
    sl "A most suitable companion for any man of status. Or any man who aspires to status."
    scene 29_2_s17 with dissolve
    mc "She's quiet."
    scene 29_2_s2 with dissolve
    sl "A sign of proper discipline, I assure you. She speaks when spoken to, as any well-trained maid should."
    sl "Would you care for a closer inspection, sir? I guarantee you won't find another with such poise in this city."
    sl "The local girls are too independent and headstrong. Reham here knows her place. It's refreshing, wouldn't you agree?"
    scene 29_2_s1 with dissolve
    mc "Just to confirm... she isn't doing this unwillingly, is she?"
    scene 29_2_s2 with dissolve
    sl "Not at all, sir! Reham is a maid, not a slave. While slavery is legal in many places, it seems to be strictly prohibited in this city."
    sl "She's here by contract, of her own free will. You're not buying a person, you're buying her service."
    scene 29_2_s1 with dissolve
    call screen scene29_choice0 with dissolve

label scene29_choice0_op1:
    $ mc_inspected_reham = True
    mc "(Might as well. If I'm going to consider this, I should at least see what I'm dealing with.)"
    mc "Fine, let's see."  
    scene 29_2_s2 with dissolve
    sl "By all means, sir, but remember—she is untouched in the most meaningful sense. A true rarity among those in service."
    sl "Most maids who reach her age have been... compromised in one way or another. Not Reham. She's been kept pure for a discerning buyer such as yourself."
    scene 29_2_s1 with dissolve
    if not interact_indicator:
        $ interact_indicator = True
        call screen interact_tutorial with Dissolve(0.3)
    jump scene29_choice11_op1

label scene29_choice0_op2:
    $ mc_talked_reham = True
    mc "I don't want to touch her. I just want to talk. Is that allowed?"
    scene 29_2_s16 with dissolve
    sl "She's clean, sir. Bathed and groomed this very morning. I assure you, she's quite—"
    scene 29_2_s17 with dissolve
    mc "That's not the reason. It just feels... wrong. Like I'm examining livestock."
    scene 29_2_s2 with dissolve
    sl "*chuckles* Wrong? Nonsense. Reham is here of her {i}own volition{/i}, I assure you."
    scene 29_2_s1 with dissolve
    mc "Still. I can't."
    scene 29_2_s2 with dissolve
    sl "Very well. She is trained for companionship too afterall."
    sl "Please, indulge yourself. I'll step aside, but please don't keep her too long, sir. Others may be interested, and time is coin."
    scene 29_2_s1 with dissolve
    scene 29_2_s3 with Fade(0.5,0.5,0.5)
    mc "Hey."
    scene 29_2_s24 with dissolve
    reham "Hello, sir. It's a pleasure to meet you."
    scene 29_2_s3 with dissolve
    mc "How are you holding up? This can't be easy... standing up there while people gawk at you."
    scene 29_2_s24 with dissolve
    reham "I am well, thank you for asking. The sun is a bit warm, but I've endured worse."
    scene 29_2_s3 with dissolve
    mc "And... how do you feel about all this? Him parading you around like this?"
    scene 29_2_s24 with dissolve
    reham "I do not mind. As he said, I chose this path. My circumstances made this the best option available. I have made peace with it."
    scene 29_2_s3 with dissolve
    mc "You really don't resent it?"
    scene 29_2_s24 with dissolve
    reham "I'd rather smile."
    scene 29_2_s3 with dissolve
    mc "...That's... admirable."
    mc "So... what do you do?"
    scene 29_2_s24 with dissolve
    reham "I can cook, clean, mend clothes. I can serve tea, play music. And... if you wished, I could serve you in other ways as well."
    scene 29_2_s3 with dissolve
    mc "That's very straightforward."
    scene 29_2_s24 with dissolve
    reham "I have no reason to hide what I am."
    scene 29_2_s3 with dissolve
    sl "A thousand apologies for intruding, sir, but business must move quickly. Others are waiting for a chance at her time."
    mc "I understand. Thank you for talking with me, Reham!"
    scene 29_2_s2 with Fade(0.5,0.5,0.5)
    sl "Before you go, sir. What do you think about Reham? A real beauty, isn't she?"
    scene 29_2_s1 with dissolve
    call screen scene29_choice11_3 with dissolve
    
label scene29_choice11_op1:
    $ mcname = persistent.name
    if persistent.name == "None" or mcname == "None":
        while mcname == "None" or mcname == "":
            $ mcname = renpy.input("There was an issue with your name. Please rewrite your name:", length=32)
        $ persistent.name = mcname
    if not persistent.scene8_replay:
        $ persistent.scene8_replay = True
    $ scene29_choice11_front = True
    $ scene29_choice11_back = False
    $ scene29_choice11_cheeks = False
    $ scene29_choice11_feet = False
    scene 29_2_s3 with fade
    call screen scene29_choice11 with dissolve

label scene29_choice11_lb:
    scene 29_2_s7 with dissolve
    perception "You position your hand beneath her breast, letting its weight settle against your fingers."
    scene 29_2_s8 with dissolve
    sl "Are you trying to gauge their heaviness, sir?"
    mc "Yes."
    logic "You have no idea what you're doing. You simply wanted to touch her breast."
    scene 29_2_s3 with dissolve
    call screen scene29_choice11 with dissolve

label scene29_choice11_rb:
    scene 29_2_s5 with dissolve
    ""
    scene 29_2_s6 with dissolve
    sensation "Her skin is soft, yielding beneath your touch. Her breast molds around your fingertips, shifting like a delicate mound of yummy jello."
    scene 29_2_s3 with dissolve
    call screen scene29_choice11 with dissolve

default scene29_choice11_face_first = True
label scene29_choice11_face:
    if scene29_choice11_face_first:
        mc "Can I see your mouth?"
        $ scene29_choice11_face_first = False
        scene 29_2_s4 with dissolve
        perception "Her lips part. Teeth, check. Tongue, check. Uvula, check. Everything is in order, sir!"
        impulse "Look at her. Smug. Comfortable. Sheltered."
        impulse "She has no scars. No broken teeth. No proof of suffering."
        impulse "You should change that."
        impulse "Teach her. Teach her what it means to be nothing."
        impulse "Break her. Show her you're not just some man. You're {i}the{/i} man. You're a God compared to her."
        impulse "Now punch her in the fucking jaw."
        call screen scene29_choice11_2 with dissolve
        stop music
        play sound "sound_effects/punch.mp3"
        scene black with vpunch
        perception "Your fist swings. She doesn't see it coming. Neither does the merchant."
        scene 29_2_s20 with Fade(0.5,0.5,0.5)
        env "In the old marketplace, a man stands with his fist clenched. A woman lies at his feet—unconscious... or maybe dead."
        play sound "sound_effects/bodydrop.mp3"
        scene 29_2_s21 with vpunch
        env "Before the man can process what he's done, he's tackled to the ground. Moments later, the guards surround him."
        scene 29_2_s22 with Fade(1.0,1.0,1.0)
        guard "[mc]? Get up. Your time is up. You're a free man now."
        scene 29_2_s23 with Fade(1.0,1.0,1.0)
        perception "You wander through the market and stop at the very place where you struck that woman all those years ago."
        perception "Out of the corner of your eye, you see someone. She's familiar."
        perception "It's Maia."
        if maia_happy:
            perception "She stares at you in disbelief, her face unreadable."
            empathy "But in her eyes, you catch a flicker of sadness. Pity."
            perception "The moment stretches—seconds feel like hours. Then, at last, she turns away. A man's voice calls for her. Her new husband? Her new Master?"
            empathy "It doesn't matter now."
            scene bad_ending1 with Dissolve(3.0)
            ""
        else:
            perception "She stares at you in disbelief, her face unreadable."
            empathy "You can spot a a cold unmistakable indifference. She has no remorse for you."
            perception "Then, at last, she turns away. A man's voice calls for her. Her new husband? Her new Master?"
            empathy "It doesn't matter now."
            scene bad_ending1 with Dissolve(3.0)
            ""
        return
    else:
        mc "Can I see your mouth?"
        scene 29_2_s4 with dissolve
        perception "Her lips part. Teeth, check. Tongue, check. Uvula, check. Everything is still in order, sir."
        scene 29_2_s3 with dissolve
    call screen scene29_choice11 with dissolve

default scene29_choice11_op2_first = True
label scene29_choice11_op2:
    $ scene29_choice11_front = False
    $ scene29_choice11_back = True
    $ scene29_choice11_feet = False
    $ scene29_choice11_cheeks = False
    if scene29_choice11_op2_first:
        mc "Can I see your ass?"
        scene 29_2_s9 with Fade(0.5,0.5,0.5)
        perception "The woman turns around and assumes a suggestive pose as if it's the most natural thing."
        scene 29_2_s10 with dissolve
        mc "I can't really see clearly what's under there."
        sl "I see. It would only be fair for you to get a proper, full assessment, sir."
        sl "Reham, would you be a dear and remove your clothing?"
        scene black with fade
        perception "It takes a moment before the woman begins to undress. Once bare, she assumes her previous pose, unfazed, as if baring herself were the most routine thing in the world."
        scene 29_2_s11 with dissolve
        sl "Thank you. Go ahead, sir."
        $ scene29_choice11_op2_first = False
        call screen scene29_choice11 with dissolve
    else:
        scene 29_2_s11 with fade
        call screen scene29_choice11 with dissolve

label scene29_choice11_ass:
    $ scene29_choice11_front = False
    $ scene29_choice11_back = False
    $ scene29_choice11_feet = False
    $ scene29_choice11_cheeks = True
    scene 29_2_s13 with dissolve
    perception "Her pussy and ass meet your gaze as you spread her cheeks apart."
    call screen scene29_choice11 with dissolve

label scene29_choice11_ipussy:
    perception "Her pussy bears no trace of masculinity. The folds are neat, untouched by time or hardship. A soft pink hue colors the delicate flesh, glistening faintly under the light."
    call screen scene29_choice11 with dissolve

label scene29_choice11_iass:
    perception "Her anus is small and unblemished, a faint wrinkle in the soft flesh. It twitches slightly under your gaze."
    call screen scene29_choice11 with dissolve

label scene29_choice11_op3:
    $ scene29_choice11_front = False
    $ scene29_choice11_back = False
    $ scene29_choice11_feet = True
    $ scene29_choice11_cheeks = False
    mc "Can I see your feet?"
    scene 29_2_s14 with fade
    perception "The woman lifts up her leg to show you her foot, you can see her swaying and staggering a bit."
    empathy "She can't hold this position for long."
    call screen scene29_choice11 with dissolve

label scene29_choice11_feet:
    scene 29_2_s15 with dissolve
    sensation "The sole of her foot feels rough and coarse, hardened from years of walking barefoot. Yet, with the right touch and a generous amount of lotion, it could become something capable of delivering great pleasure."
    scene 29_2_s14 with dissolve
    call screen scene29_choice11 with dissolve

default mc_not_interested_slaver = False
label scene29_choice10_op2:
    $ mc_not_interested_slaver = True
    mc "Not interested."
    scene 29_2_s18 with dissolve
    sl "A shame, truly. But I understand—such decisions require careful thought. If your mind ever wavers, sir, you'll find me right here." 
    sl "Reham won't be available forever, though. A woman of her quality always finds a buyer eventually."
    scene 29_2_s19 with dissolve
    mc "(No point lingering.)"
    if not mc_met_nadia:
        scene 29_s24 with dissolve
        call screen scene29_choice06 with dissolve
    else:
        mc "(I suppose that's enough for today. Time to return before I forget where the castle was.)"
        jump free_roam_main_label

default in_scene29 = False
label scene29_ending:
    play music "gameplay_night.mp3" fadein 2.0 loop
    $ in_scene29 = True
    scene 29_1_s50 with Fade(1.0,1.0,1.0)
    ""
    scene 29_1_s51 with Fade(1.0,1.0,1.0)
    ""
    scene 29_1_s52 with fade
    sensation "Your body sinks into the mattress, the fabric brushing against your skin with a silky smoothness."
    call screen scene_maia_sleep1 with dissolve

default in_scene30 = False
default in_scene30_2 = False

label scene29_choice11_op4:
    $ renpy.end_replay()
    $ mc_inspected_reham = True
    scene 29_2_s2 with fade
    sl "What do you think, sir? A real beauty, isn't she?"
    scene 29_2_s1 with dissolve
    call screen scene29_choice11_3 with dissolve

label scene29_choice11_good:
    mc "She's pretty good. I like her. She's honest and straightforward."
    scene 29_2_s16 with dissolve
    sl "Indeed! I knew you had a discerning eye. I can tell you're a man who recognizes quality when he sees it."
    sl "Shall we discuss a price then?"  
    scene 29_2_s17 with dissolve
    jump scene29_choice11_ugly

label scene29_choice11_fine:
    mc "I've seen better, but not too bad overall."
    scene 29_2_s2 with dissolve
    sl "I see, but worry not, sir! Reham is adaptable. You can still shape her into your perfect maid. With the right guidance, she'll exceed your expectations."
    sl "Shall we discuss a price?"  
    scene 29_2_s1 with dissolve
    jump scene29_choice11_ugly

label scene29_choice11_bad:
    $ reham_price = 100
    mc "She isn't my type, I'm not really into her."
    scene 29_2_s18 with dissolve
    sl "Ah, what a shame. I do appreciate your honesty, sir."
    scene 29_2_s19 with dissolve
    mc "Still, I'm curious. What's her price?"
    scene 29_2_s2 with dissolve
    sl "Reham... she's worth three gold coins. That's the honest price, given her training, her health, her untouched nature. But for you, sir—"
    sl "—I'll lower it to just one gold coin. A {i}rare{/i} opportunity. I don't offer this discount lightly."
    scene 29_2_s1 with dissolve
    logic "But in truth, she was always one gold coin."
    mc "One gold coin? That's... actually not as much as I expected."
    mc "(Wait, how much would that be in my world's currency?)"
    if mc_coin >= 100:
        mc "I do have the coin but I'll need to think about it."
    else:
        mc "Like I said, I don't have the coin, but I might come back later."
    scene 29_2_s2 with dissolve
    sl "I see... Well, do be hasty, sir. Opportunities like this don't last. A fine maid like her? Someone's bound to claim her soon."
    scene 29_2_s1 with dissolve
    mc "We'll see. I've got a lot on my plate right now."
    scene 29_2_s2 with dissolve
    sl "Thank you for coming, sir! Please, take care."
    scene 29_2_s1 with dissolve
    scene 29_s24 with Fade(0.5,0.5,0.5)
    if not mc_met_nadia:
        scene 29_s24 with Fade(0.5,0.5,0.5)
        mc "I still have time, might as well check Nadia out."
        call screen scene29_choice06 with dissolve
    else:
        jump free_roam_main_label

label scene29_choice11_ugly:
    $ reham_price = 200
    if mc_coin >= 200:
        mc "Go ahead."
    else:
        mc "I might not have the coin on me right now, but sure, go ahead. I'm curious."
    scene 29_2_s2 with dissolve
    sl "Reham... she's worth three gold coins. That's the honest price, given her training, her health, her untouched nature. But for you, sir—"
    sl "—I'll lower it to just two gold coin. A {i}rare{/i} opportunity. I don't offer this discount lightly."
    scene 29_2_s1 with dissolve
    logic "But in truth, she was always two gold coins, maybe even less."
    mc "Two gold coin?"
    mc "(Wait, how much would that be in my world's currency?)"
    if mc_coin >= 200:
        mc "I do have the coin but I'll need to think about it."
    else:
        mc "Like I said, I don't have the coin, but I might come back later."
    scene 29_2_s2 with dissolve
    sl "I see... Well, do be hasty, sir. Opportunities like this don't last. A fine maid like her? Someone's bound to claim her soon."
    scene 29_2_s1 with dissolve
    mc "We'll see. I've got a lot on my plate right now."
    scene 29_2_s2 with dissolve
    sl "Thank you for coming, sir! Please, take care."
    scene 29_2_s1 with dissolve
    if not mc_met_nadia:
        scene 29_s24 with Fade(0.5,0.5,0.5)
        mc "I still have time, might as well check Nadia out."
        call screen scene29_choice06 with dissolve
    else:
        jump free_roam_main_label

label free_roam_market:
    scene 29_s27 with Fade(0.5,0.5,0.5)
    play music "market2.mp3" fadein 3.0 volume 0.7 loop
    mc "(Nadia's gone... I guess I could check out that merchant for now.)"
    call screen scene29_choice06 with dissolve

label scene30:
    $ in_scene30 = True
    $ in_scene18 = False
    $ in_scene29 = False
    ###########################################################################################################################
    scene 29_s1 with Fade(2.0,1.0,1.0)
    stop music fadeout 2.0
    ""
    scene 29_s2 with dissolve
    ""
    scene 29_s3 with dissolve
    ""
    scene 29_s4 with dissolve
    mc "(She's always staring through that window...)"
    $ mc_masturbated = False
    $ mc_armor_timer = 2
    jump free_roam_main_label

label scene31:
    $ mc_got_armor = True
    $ in_scene30 = False
    scene 31_s21 with Fade(1.0,1.0,1.0)
    play music "nature.mp3" fadein 2.0 loop
    orym "Like I said—it was a huge one. Took everything I had to bring it down."
    orym "*laughs* And you know what happened after? I shoved my sword so far up its ass, it came out its mouth!"
    orym "The goblins scattered like roaches after that"
    yuuhi "Haha... that's... crazy."
    orym "So what about you, Yuuhi? My party's got room for one more. A pretty girl like you shouldn't be stuck in a forge all day."
    orym "I'd love to take you on—"
    scene 31_s22 with Dissolve(1.0)
    mc "Hey. What's going on here?"
    yuuhi "[mc]! Thank goodness!"
    scene 31_s24 with Dissolve(1.0)
    orym "Who—? Ah. The so-called hero of the town... for a day, I guess."
    orym "I heard the celebration's already dying down. People have short memories."
    orym "Hell of a mistake, friend. The ogre's dead, and barely anyone even knows it was you. You should have flaunted it. Put your face out there."
    scene 31_s23 with dissolve
    mc "I don't care about that. What I care about is you backing off. I don't think she's interested in your babbling."
    scene 31_s24 with dissolve
    orym "Oh? And who are you to say that? Is she your girl?"
    scene 31_s23 with dissolve
    call screen scene31_choice03 with dissolve
    
label scene31_choice03_op1:
    mc "Yes. She is. So back off."
    scene 31_s25 with dissolve
    orym "That true, sweetheart? You belong to this... newcomer?"
    scene 31_s26 with dissolve
    yuuhi "Y-Yes!"
    scene 31_s24 with dissolve
    orym "Then I'll just steal her from you. A woman like that deserves someone better than a one-day hero. Now move along before I make you."
    jump scene31_0

label scene31_choice03_op2:
    mc "No. But I do have business with her. The Queen's business. Which means you're interfering with royal affairs."
    scene 31_s24 with dissolve
    orym "Then you can wait your turn, can't you?"
    orym "We were having a conversation. A private one. Move along before I make you."

label scene31_0:
    scene 31_s23 with dissolve
    call screen scene31_choice02 with dissolve

label scene31_choice02_op1:
    $ mc_punch_orym = True
    mc "..."
    scene 31_s31 with dissolve
    orym "What are you—"
    play sound "sound_effects/punch.mp3"
    scene 31_s27 with vpunch
    perception "Your fist rockets forward, slamming square into his jaw with a satisfying crack."
    orym "Ahgh!"
    play sound "sound_effects/bodydrop.mp3"
    scene 31_s28 with vpunch
    orym "Y-You hit me! You actually fucking hit me!"
    orym "Do you have any idea who you're messing with?! I'm a ranked adventurer!"
    orym "I've killed more monsters than you've ever seen! I could buy and sell you with the coin in my pocket!"
    scene 31_s29 with dissolve
    perception "His voice wavers between outrage and disbelief. His eyes dart around as if hoping someone else saw."
    mc "Leave before I shove a sword so far up your ass it comes out your mouth... Wasn't that your line? I thought it was funny."
    scene 31_s28 with dissolve
    orym "Y-You...! You're lucky I don't have my sword right now. I'd— I'd cut you to ribbons! You'd be begging for mercy!"
    scene 31_s29 with dissolve
    mc "Still have some spirit, huh? Maybe I shouldn't have gone soft. But I'll make up for it now."
    scene 31_s30 with dissolve
    orym "Tch—! You think this is funny?! This isn't over, [mc]! I'll remember this!"
    orym "You'll regret it!"
    mc "Sheesh... For a guy who brags about killing monsters, he runs pretty fast."
    jump scene31_00
    
label scene31_choice02_op2:
    mc "What would the guild say if they knew you were harassing a girl? Eireen seems like the type who doesn't tolerate that kind of behavior."
    scene 31_s31 with dissolve
    orym "Harassing!? Don't be ridiculous. She's a friend. Aren't we, Yuuhi?."
    scene 31_s32 with dissolve
    yuuhi "..."
    mc "Yuuhi. Was he bothering you?"
    yuuhi "...Mhmm."
    empathy "Her voice is barely more than a whisper, but it's enough."
    mc "There. Straight from her mouth. Imagine the guild hearing that one of their own can't keep his hands to himself."
    orym "..."
    mc "Leave. Or I call the guards and make sure everyone hears what happened."
    scene 31_s31 with dissolve
    orym "Fine. [mc], wasn't it? The mysterious hero. The Queen's new pet."
    orym "I'll remember you."
    scene 31_s32 with dissolve
    mc "Good. That'll save me the trouble of introducing myself next time."  
    jump scene31_00

label scene31_00:
    scene 31_s33 with Dissolve(1.0)
    ""
    play sound "sound_effects/clothing_rustle.mp3"
    scene 31_s34 with vpunch
    yuuhi "[mc]!"
    yuuhi "Thank you! Thank you, thank you!"
    yuuhi "He always does this! Every time he comes to the forge, he corners me and says some stupid things."
    yuuhi "I told him so many times to stop but he just laughs and says I'm being 'cute'."
    mc "Don't worry, it's over. You're safe now."
    yuuhi "Mmm..."
    mc "Yuuhi... you're holding on pretty tight. I can't actually feel my ribs anymore."
    yuuhi "I... I just... I don't want to let go. Not yet."
    scene 31_s37 with Dissolve(1.0)
    yuuhi "..."
    scene 31_s35 with Dissolve(1.0)
    yuuhi "Mmmm~"
    mc "Uhh... Yuuhi?"
    scene 31_s36 with dissolve
    yuuhi "Oh! Sorry... haha, I... I thought maybe... you wanted to... I mean, after what you did, and the way you stood up for me, I thought maybe you'd..."
    scene 31_s37 with dissolve
    call screen scene31_choice04 with dissolve

label scene31_choice04_op1:
    $ mc_harem_yuuhi = True
    play sound "se_sfx/blowjob/kiss3.mp3" 
    scene 31_s40 with Dissolve(1.0)
    yuuhi "Mhnnn~"
    scene 31_s39 with dissolve
    yuuhi "W-We kissed! I can't believe it... I actually kissed someone."
    scene 31_s38 with dissolve
    mc "...Yeah. We did."
    scene 31_s39 with dissolve
    yuuhi "D-Does that mean... you're my boyfriend now?! Is that how this works?!"
    scene 31_s38 with dissolve
    mc "*laughs* I guess it does, huh?"
    scene 31_s39 with dissolve
    yuuhi "Ohhh my gods... this is real! This is actually real! I have a boyfriend! A real boyfriend that isn't fictional from a novel!"
    scene 31_s38 with dissolve
    mc "Calm down, Yuuhi. What's wrong?"
    scene 31_s39 with dissolve
    yuuhi "All my friends always teased me, saying I never would! Ria said I'd die old with nothing but my hammer for company!"
    scene 31_s38 with dissolve
    mc "Really? But you're so beautiful and hardworking. They must've been blind. Or jealous."
    scene 31_s36 with dissolve
    yuuhi "Hehe~ I can't wait to see their faces when I tell them! Ria's going to swallow her tongue."
    scene 31_s37 with dissolve
    mc "Save that victory lap for later. Let's finish our business first."
    scene 31_s36 with dissolve
    yuuhi "Right! The armor. It's ready. Come, boyfriend~!"
    stop music fadeout 2.0 
    scene 31_s37 with dissolve
    jump scene31_000

label scene31_choice04_op2:
    mc "Sorry, Yuuhi. But we're not... like that. I'm flattered. Really."
    scene 31_s36 with dissolve
    yuuhi "O-Of course! Haha... just forget I even did that. H-Heat of the moment. You know how it is..."
    scene 31_s37 with dissolve
    mc "Come on, let's get to the shop."
    stop music fadeout 2.0 
    yuuhi "Mhm..."
    jump scene31_000

label scene31_000:
    scene 31_s1 with Fade(1.5,1.0,1.0)
    play music "yuuhi.mp3" fadein 2.0 loop
    yuuhi "Let's see how you look with your new armor!"
    scene 31_s2 with dissolve
    mc "Let's do it."
    scene 31_s5 with Fade(0.5,0.5,0.5)
    ""
    scene 31_s4 with dissolve
    yuuhi "Looking good!"
    scene 31_s3 with dissolve
    mc "You're a genius!"
    scene 31_s1 with dissolve
    yuuhi "Hehe~ Thank you."
    yuuhi "Will you be heading out on an adventure to find that witch?"
    scene 31_s2 with dissolve
    mc "I think so! Feeling a lot more confident now that I have a sword and armor."
    scene 31_s6 with dissolve
    yuuhi "It's not the sword that protects you. It's how you use it!"
    scene 31_s2 with dissolve
    mc "Right."
    if mc_harem_yuuhi:
        scene 31_s15 with dissolve
        yuuhi "*ahem* Before you leave... Umm..."
        scene 31_s16 with dissolve
        mc "What is it?"
        scene 31_s15 with dissolve
        yuuhi "Since we're dating, I think I should get some... extra measurements in the, uh... crotch area... I want my partner to be safe..."
        scene 31_s16 with dissolve
        mc "Really now? The crotch area?"
        scene 31_s15 with dissolve
        yuuhi "Ahuh! You know, just to be sure... You never know what might happen, right?"
        scene 31_s16 with dissolve
        mc "Now that you say that, it {i}is{/i} kinda tight down there."
        scene 31_s15 with dissolve
        yuuhi "See? I knew it... N-Now follow me. Quick, before anyone notices."
        scene 31_s16 with dissolve
        mc "You're awfully secretive for just a few measurements."
        scene 31_s17 with dissolve
        yuuhi "I-It's not just measurements! I mean... it {i}is{/i}, but... not the boring kind!"
        scene 31_s18 with dissolve
        mc "Oh? Special tailoring service for your boyfriend, then?"
        scene 31_s15 with dissolve
        yuuhi "Don't call it that... you'll make me lose my nerve..."
        yuuhi "So... do you want me to or not?"
        scene 31_s16 with dissolve
        call screen scene31_choice05 with dissolve
    else:
        scene 31_s1 with dissolve
        yuuhi "Anything else? Perhaps a ten-foot-long axe, haha?"
        scene 31_s2 with dissolve
        call screen scene31_choice01 with dissolve

label scene31_choice05_op1:
    mc "Alright, alright. I'm coming."
    stop music fadeout 2.0 
    jump scene23_choice02_sure
    
label scene31_choice05_op2:
    mc "Maybe another time, Yuuhi. I need to head out. That poor guy has been waiting long enough."
    scene 31_s19 with dissolve
    yuuhi "...I understand. The mission comes first."
    yuuhi "But please promise me you'll be careful out there!"
    yuuhi "I don't want to lose my boyfriend so quickly!"
    scene 31_s20 with dissolve
    mc "I promise. See you, Yuuhi."
    stop music fadeout 2.0 
    jump scene32_2

label scene31_choice01_moti:
    if mc_harem_yuuhi:
        mc "I need some {i}motivation{/i}."
        scene 31_s7 with dissolve
        yuuhi "Oh? How can I... motivate you?"
        scene 31_s8 with dissolve
        mc "Show me something nice."
        scene 31_s7 with dissolve
        yuuhi "[mc]... you're so naughty~"
        scene 31_s9 with dissolve
        yuuhi "What about this? Do you feel {i}invigorated{/i} now?"
        scene 31_s10 with dissolve
        mc "I feel like I can take on the world!"
        scene 31_s9 with dissolve
        stop music fadeout 3.0
        yuuhi "Hehe~ Be careful out there, [mc]."
        scene 31_s10 with dissolve
    else:
        mc "I need some {i}motivation{/i}. If you know what I mean. *wink*"
        scene 31_s1 with dissolve
        yuuhi "Motivation? Umm... Oh! How about I tell you the tale of Gavlan the archer?"
        scene 31_s2 with dissolve
        curiosity "Hoo boy... I think we might be here for a while."
        mc "...Who?"
        scene 31_s1 with dissolve
        yuuhi "Gavlan the Archer! The greatest bowman to ever walk the land of Irda!"
        scene 31_s2 with dissolve
        mc "Uh-huh..."
        scene 31_s1 with dissolve
        yuuhi "The historians are conflicted on the date, but it was probably a millennia ago, when young Gavlan, then merely a humble farm boy, picked up a bow for the first time. Little did he know, that very bow would the reason for his rise!"
        yuuhi "At the age of twelve, he was recruited as a soldier, where he spent six grueling years perfecting his aim. By the time he was eighteen, he could shoot a sparrow out of the sky from over a hundred paces!"
        scene 31_s2 with dissolve
        mc "Fascinating..."
        scene 31_s1 with dissolve
        yuuhi "But wait, it gets better! You see, during the Siege of Irda by the Nahrayan forces, the enemy commander—Sir Belith the Cruel—stood atop the battlements, mocking the Queen's army! The battle seemed lost, but then—"
        yuuhi "—Gavlan nocked an arrow, took a deep breath, and in a single shot, he—"
        scene 31_s2 with dissolve
        mc "You know what? I suddenly feel very motivated. Thanks, Yuuhi!"
        scene 31_s1 with dissolve
        yuuhi "Huh? But I haven't even told you about the part where he single-handedly took down a small army using only—"
        scene 31_s2 with dissolve
        mc "Nope! Gotta go. Thanks again!"
        scene 31_s1 with dissolve
        stop music fadeout 3.0
        yuuhi "O-Oh... Alright then... Maybe next time!"
        scene 31_s2 with dissolve
    jump scene32_2

label scene31_choice01_no:
    mc "Nope. All set."
    scene 31_s1 with dissolve
    yuuhi "I see. Well, good luck out there!"
    scene 31_s2 with dissolve
    jump scene32_2

default in_scene32 = False
label scene32:
    $ in_scene32 = True
    stop music fadeout 2.0
    jump free_roam_main_label
    $ current_objective = "Current Objective: Talk to Eireen."
    
label scene32_2:
    $ in_scene32 = False
    play music "guild.mp3" fadein 2.0 loop
    scene 21_s1 with Fade(2.0,1.5,1.0)
    mc "Eireen, I got my armor, I'll be out now!"
    scene 21_s7 with dissolve
    eireen "Woah, hold on, [mc]."
    scene 21_s8 with dissolve
    mc "Hmm?"
    jump scene33




    scene 21_s7 with dissolve
    eireen "Actually, I need you to handle something more urgent right now."
    scene 21_s8 with dissolve
    mc "Is it more important than saving Lord Riener's daughter?"
    scene 21_s2 with dissolve
    eireen "Not really. Well, I doubt Lord Riener will be happy about this, but the word came straight from the Queen, so..."
    scene 21_s1 with dissolve
    mc "Alright, can I get more details?"
    scene 21_s2 with dissolve
    eireen "We have been getting more and more reports of a witch kidnapping adventurers who were unlucky enough to cross her path."
    eireen "Thankfully, we know where she's hiding—thanks to a man who somehow managed to escape her."
    scene 21_s1 with dissolve
    mc "Hold on... A witch now? I was fine with the Queen of pleasure since you said she was friendly, but a witch? Really?"
    scene 21_s2 with dissolve
    eireen "Something wrong?"
    scene 21_s1 with dissolve
    mc "Yes, there is. Isn't this a lot more dangerous?"
    scene 21_s7 with dissolve
    eireen "Oh, absolutely. She's not to be taken lightly."
    scene 21_s8 with dissolve
    mc "*sigh* I don't think you're understanding what I'm getting at here."
    scene 21_s2 with dissolve
    eireen "It doesn't matter. Like I said, the Queen is the one who asked me to change your task."
    scene 21_s1 with dissolve
    env "Somewhere in a castle not far from here, a woman wearing a crown sits atop her throne, sipping a glass of the finest wine, laughing about something."
    scene 21_s14 with dissolve
    eireen "Also, weren't you the one who slayed an ogre? This should be nothing in comparison."
    scene 21_s15 with dissolve
    if mc_lied:
        mc "But..."
        empathy "Maybe if you finally told the truth, they would understand. It's not too late."
        impulse "Or maybe you should stop acting like a fucking pussy."
    if mc_truth:
        mc "But I didn't... It was..."
        empathy "That's right. Maybe if you explained what happened again, they would finally understand."
        impulse "Or maybe you should stop acting like a fucking pussy."

    mc "Fuck it. Fine, but if I die, my blood is on her hands."
    scene 21_s14 with dissolve
    eireen "Right... Anyway, the witch is located in the forest south of our city."
    scene 21_s15 with dissolve
    mc "Can I talk to the guy first? I want to know more about what I'm dealing with."
    scene 21_s14 with dissolve
    eireen "Well... you see, he's not in the best state of mind right now. Poor guy looks completely broken—shut himself off from everyone."
    eireen "But even after hearing that, it is absolutely crucial that you bring her back alive. Got it?"
    scene 21_s15 with dissolve
    mc "Alright, I'll see to it.."

label scene33:
    scene 21_s7 with dissolve
    eireen "How exactly are you planning to get there? The old king's forest is miles from the city. Did you even look at the map I gave you?"
    scene 21_s8 with dissolve
    mc "Well... I'll just walk?"
    scene 21_s6 with dissolve
    eireen "You'd collapse halfway there. The forest is deep in the northern wilds, it's not a stroll through the market."
    scene 21_s1 with dissolve
    perception "She places two gold coins on the counter, their surfaces gleaming brilliantly, almost hypnotically."
    mc "Woah! What's this for? Am I already getting my salary?"
    scene 21_s2 with dissolve
    eireen "Head to the stables north of here and get yourself a horse if you don't want to die on the road."
    scene 21_s1 with dissolve
    mc "A horse? This is... a lot. Do I have to return this later?"
    scene 21_s7 with dissolve
    eireen "It's from the Queen. The last thing she gave you. Consider it her final... gesture of support. You're fully on your own now."
    scene 21_s8 with dissolve
    mc "So this is the send-off money..."
    scene 20_s4 with fade
    play sound "sound_effects/paperOpen.mp3"
    show screen irda_city_map with dissolve
    mc "(Alright, the stables are north of here. Just follow the main road, and...)"
    mc "(Fuck... another long walk.)"
    jump scene33_barn

label scene33_barn:
    hide screen irda_city_map with dissolve
    $ visited_barn = True
    play music "nature.mp3" fadein 2.0 loop
    scene 33_s1 with Fade(1.0,0.5,1.0)
    mc "Hah... hah... Why the hell is it so far away from the city?! Who puts a stable a mile from the nearest building? That's not convenient for anyone!"
    scene 33_s2 with fade
    ""
    play sound "sound_effects/barn_door.mp3"
    scene 33_s3 with dissolve
    mc "Hello? Anyone here?"
    mc "...I'm coming in!"
    scene 33_s4 with Dissolve(0.8)
    selene_ "Mmm, it tastes so good~"
    stop music fadeout 2.0
    mc "(What the fuck is happening here?!)"
    scene 33_s5 with dissolve
    mc "(Another elf! Wait, why is she topless?! Is this how... stable workers dress in this world?)"
    mc "*ahem* Hello!"
    scene 33_s6 with dissolve
    selene_ "Oh! Hello, sir! Didn't see ya there. I'll be right with ya!"
    play music "selene_temp.mp3" fadein 2.0  loop
    scene 33_s7 with fade
    mc "I'm looking for a horse. Are you the one to talk to?"
    scene 33_s8 with dissolve
    selene_ "Yessir, that'd be me! You can call me Serena. I run this place for my Master."
    selene "But I gotta tell ya, we're plum outta horses at the moment... well, 'cept this fine gal here."
    scene 33_s7 with dissolve
    mc "Alright, how much for her? She looks healthy."
    scene 33_s8 with dissolve
    selene "Two gold coins, sir, or two hundred coppers if ya'd rather. It may sound different, but it's actually the same price."
    scene 33_s7 with dissolve
    mc "So basically all I have..."
    mc "*sigh* Fine. I'll take her."
    scene 33_s9 with dissolve
    selene "A fine choice, sir! This mare's got spirit. She'll carry you through anything!"
    scene 33_s10 with dissolve
    mc "Uh... is there a reason why you're... topless?"
    scene 33_s9 with dissolve
    selene "Oh, that's my preference, sir. It gets terribly hot around here. We elves don't sweat, so we cool off by wearing as little as possible!"
    scene 33_s10 with dissolve
    mc "I... see."
    perception "You hand over the two gold coins, lingering for just a moment before kissing your fingertips goodbye."
    scene 33_s9 with dissolve
    selene "Pleasure doing business, sir! Come back anytime!"
    scene 33_s10 with dissolve
    scene 33_s11 with fade
    mc "Now, what should I name you?"
    scene 33_s12 with dissolve
    $ mchorse_default = "Kita Black"
    $ mchorse = renpy.input("What should I name her? (default: Kita Black)", length=32)
    $ mchorse = mchorse.strip() 
    if not mchorse:  
        $ mchorse = mchorse_default
    else:
        $ mchorse = mchorse.capitalize() 
    scene 33_s11 with dissolve       
    mc "Your name shall be, [horse]!"
    stop music fadeout 2.0
    mc "Come on, [horse]. Time to go forward!"
    scene 33_s12 with dissolve
    scene black with Fade(0.5,0.5,0.5)
    play music "images/custom_gui/global/mainmenu/mainmenu_song.mp3" fadein 2.0 loop
    show expression "chapter1_journey_main" at center  with dissolve

    window hide
    pause 0.5
    window show
    #""
    show chapter1_recap1 with dissolve
    if mc_lied:
        "You lied about slaying the ogre. A hero in words, if not in deeds."
    else:
        "You told the truth to Darius. Honesty is a sharp blade—use it wisely."
    show chapter1_recap2 with dissolve
    hide chapter1_recap1
    if mc_helped_ruby:
        "You agreed to help Ruby find her sister. A noble heart, or just another poor soul caught in someone else's mess?"
    else:
        "You turned Ruby away. She'll remember that. Whether that's a blessing or a curse remains to be seen."

    show chapter1_recap3 with dissolve
    hide chapter1_recap2
    if mc_liked_ass:
        "Your eyes linger southward. A connoisseur of the divine curvature. (Your preference is ass)"
    elif mc_liked_tits:
        "Your gaze is drawn upward—round and soft, like twin treasures of the flesh. (Your preference is breasts)"
    elif mc_liked_feet:
        "You walk a path few dare tread. A man of... peculiar tastes. (Your preference is feet)"
    elif mc_liked_personality:
        "You chose personality over flesh. A noble ideal—if only anyone believed you. (Your preference is personality)"
    else:
        "You didn't indulge with Darius in the brothel."

    show chapter1_recap5 with dissolve
    hide chapter1_recap4
    if mc_told_reb_harem:
        "You told Rebecca that you wanted her. Bold. A move worthy of a king... or a fool."
    else:
        "You told Rebecca that you weren't after her. Perhaps it's for the best."

    if mc_maia_first_sex:
        show chapter1_recap15 with dissolve
        hide chapter1_recap4
        if maia_pregnant:
            "You did as the Queen commanded and took Maia to bed. Her womb now blossoms because of it."
        else:
            "You did as the Queen commanded and took Maia to bed. Yet her womb remains empty, for now."
    else:
        if mc_calmed_maia:
            show chapter1_recap16 with dissolve
            hide chapter1_recap4
            "You calmed Maia when she was in heat. Maybe she just wasn't your type. Or maybe you prefer having her as a roommate rather than a wife."
        else:
            show chapter1_recap6 with dissolve
            hide chapter1_recap5
            if mc_punished_maia:
                "You chose discipline over mercy. Maia won't forget."
            else:
                "You decided not to punish Maia. Perhaps mercy is its own kind of power."

    show chapter1_recap7 with dissolve
    hide chapter1_recap6
    if mc_harem_yuuhi:
        "You accepted Yuuhi's proposal. Another name added to your ever-growing list of lovers."
    else:
        "You turned Yuuhi's proposal down. A rare act of restraint."
    
    if mc_lied:
        show chapter1_recap8 with dissolve
        hide chapter1_recap7
        if mc_told_maia_ogre_truth:
            "You spun a web of lies, but at least Maia knows the truth about the ogre."
        else:
            "You kept Maia in the dark about the ogre. Lies upon lies—just another day."

    if diana_harem_chance_talk_pepo:
        if mc_harem_diana:
            show chapter1_recap14 with dissolve
            hide chapter1_recap8
            "You told Diana she was your lover. Her smile said she believed you."
        elif mc_friend_diana:
            show chapter1_recap14 with dissolve
            hide chapter1_recap8
            "You told Diana you were just friends. A safer bond... for both of you."
        else:
            show chapter1_recap14 with dissolve
            hide chapter1_recap8
            "You told Diana there was nothing between you. Sometimes truth is the cruelest lie."
    else:
        show chapter1_recap14 with dissolve
        hide chapter1_recap8
        "During one of your visits, you noticed Diana glancing at you more than usual. Perhaps visiting her more often will encourage her to confess her true feelings."

    if mc_harem_yuuhi:
        show chapter1_recap9 with dissolve
        hide chapter1_recap8
        if mc_told_yuuhi_maia:
            "You confessed to Yuuhi about your wife. Honesty can be a dangerous game."
        else:
            "You kept Maia a secret from Yuuhi. Some truths are best whispered... or not spoken at all."

    show chapter1_recap13 with dissolve
    hide chapter1_recap10
    if mc_accept_helped_nadia:
        if mc_friend_nadia:
            "You chose to stand by Nadia, forging a bond she won't forget"
        elif mc_harem_nadia:
            "You confessed your love to Nadia—a gamble of the heart."
    else:
        "You left Nadia to her own struggles. Some doors close forever."

    show chapter1_recap12 with dissolve
    hide chapter1_recap11
    if not karma_updated:
        $ karma_updated = True
        if mc_karma >= 100:
            $ mc_karma = 10
        elif mc_karma >= 90:
            $ mc_karma = 9
        elif mc_karma >= 80:
            $ mc_karma = 8
        elif mc_karma >= 70:
            $ mc_karma = 7
        elif mc_karma >= 60:
            $ mc_karma = 6
        elif mc_karma >= 50:
            $ mc_karma = 5
        elif mc_karma >= 40:
            $ mc_karma = 4
        elif mc_karma >= 30:
            $ mc_karma = 3
        elif mc_karma >= 20:
            $ mc_karma = 2
        elif mc_karma >= 10:
            $ mc_karma = 1
        else:
            $ mc_karma = 1

    if mc_karma < 1:
        $ mc_karma = 1
    if mc_karma > 10:
        $ mc_karma = 10
    "You have [mc_coin] coins to your name, and your honor stands at [mc_karma] out of 10. Whatever that means."

    scene 34_s0 with Fade(0.5,0.5,0.5)
    ""
    stop music fadeout 2.0
    scene black with Fade(1.0,1.0,1.0)

default in_scene34 = False
label scene34_witch:
    window hide
    $ days_passed += 1
    $ mc_masturbated = False
    if mc_harem_yuuhi:
        $ yuuhi_sex_times = 2

    
    if maia_pregnant:
        $ maia_pregnancy_timer += 1
    if diana_pregnant:
        $ diana_pregnancy_timer += 1
    if yuuhi_pregnant:
        $ yuuhi_pregnancy_timer += 1
    
    $ speech_cycle += 1
    $ mc_met_witch = True
    $ in_scene34 = True
    scene 34_s1 with Fade(1.0,1.0,1.0)
    play music "night.mp3" fadein 1.0  loop
    ""
    scene 34_s2 with Fade(0.5,0.5,0.5)
    mc "(This must be the place, according to the map.)"
    scene 34_s3 with dissolve
    mc "Stay here, girl. I'll be back. If I'm not back in an hour... trot home."
    scene 34_s4 with Fade(0.5,0.5,0.5)
    ""
    scene 34_s5 with fade
    mc "(No one in sight...)"
    stop music fadeout 2.0
    amelia_ "Oh my~ Looking for me?"
    play music "witch.mp3" fadein 2.0 loop
    scene 34_s6 with vpunch
    mc "Who's there?! Show yourself!"
    amelia_ "Purr~ Right behind you."
    scene 34_s7 with dissolve
    ""
    scene 34_s8 with vpunch
    mc "Wha—How did you—?!"
    scene 34_s9 with dissolve
    amelia "Hmhmm... Aren't you going to attack, boy? I'm right here~"
    scene 34_s8 with dissolve
    mc "(Shit...)"
    scene 34_s10 with dissolve
    mc "HAAAAA!"
    play sound "sound_effects/poof.mp3"
    scene 34_s11 with vpunch
    mc "Huh?!"
    scene 34_s12 with dissolve
    mc "*cough* *cough* (Where the hell did all this smoke come from!?)"
    amelia "You're weak, your stance is sloppy, and your swing is too wide. Did Eireen run out of men to come search for me? She must be desperate to send you."
    scene 34_s13 with dissolve
    amelia "Try again."
    scene 34_s14 with dissolve
    mc "Shut up!"
    scene 34_s15 with dissolve
    ""
    scene 34_s16 with dissolve
    ""
    scene 34_s17 with dissolve
    mc "Wha—?"
    play sound "sound_effects/bodydrop.mp3"
    scene 34_s18 with vpunch
    mc "Arghh!"
    amelia "*chuckles* I see that you've some decent armor. Quality craftsmanship for sure."
    amelia "But alas, it means nothing against paralysis magic. The nerves don't care about enchantments."
    mc "Let me go!"
    amelia "Shhh... enough struggling, my dear. Let's get you inside."
    scene 34_s19 with dissolve
    amelia "You and I are going to have {i}so{/i} much fun."
    mc "Wh-what are you... doing..."
    scene black with Dissolve(1.5)
    sensation "Darkness creeps at the edge of your vision, your body buckles as her laughter follows you into oblivion."
    stop music fadeout 4.0
    scene black with Fade(2.0,0.5,1.0)

label scene34_witch2:
    scene 34_2_s1 with Fade(0.5,0.5,1.0)
    amelia "Rise and shine, my sweet~ Did you sleep well?"
    scene 34_2_s2 with dissolve
    mc "Ugh... My head... What the hell..."
    scene 34_2_s3 with fade
    mc "Where am I? What is this place?"
    scene 34_2_s4 with dissolve
    amelia "Welcome to my humble abode."
    mc "Yeah... Real cozy."
    mc "*sigh* I'm guessing you don't remember me."
    amelia "Hmm? Sorry, I'm not good with faces."
    mc "You attacked me. In the city. When you were dragging that poor guy."
    scene 34_2_s5 with dissolve
    amelia "Ohhh! So that was you~"
    amelia "My apologies, but I couldn't risk you blabbing to the guards, now could I?"
    scene 34_2_s4 with Dissolve(1.0)
    mc "But... you didn't kill me? Why? You had me unconscious."
    amelia "Kill you? Oh no, dear. Not my style. I much prefer... breaking minds."
    mc "...That's not better. Speaking of which, what happened to the guy you were dragging off?"
    amelia "Ugh! Don't remind me. I let him go just this morning. His seed was rancid, and that moaning of his? Like a dying mule. 'Eeehhh, eeehhh.' My ears still ache."
    mc "Wait—wait! His seed? Moaning? Were you... {i}milking{/i} this guy?"
    scene 34_2_s5 with dissolve
    amelia "*laughs* My, my! Aren't you a clever little fly caught in my web. Yes, extracting semen. Though I do like your word better. {i}Milking.{/i} *slurp*"
    scene 34_2_s6 with Dissolve(1.5)
    amelia "And you, darling, will be receiving the same treatment."
    scene 34_2_s7 with Dissolve(1.0)
    mc "A-Are you serious?! But why? Does semen make you more powerful or something?"
    scene 34_2_s9 with dissolve
    amelia "*chuckles* Oh, no. Power has nothing to do with it."
    amelia "I've been conducting this research for years. The spell requires a man's seed. It must be potent, fresh, and taken under... specific conditions."
    amelia "But I won't lie... over the years, I've grown to enjoy the process. Watching men thrash, hearing them whimper my name, begging to cum after days of denial~"
    amelia "At first they pretend to be strong. Stoic. Defiant. By the end of the week? They're nothing but eager little dispensers, ejaculating on command."
    scene 34_2_s7 with dissolve
    mc "A 'research'? What kind of lewd spell needs semen? Be honest, this is just a fetish for you..."
    mc "You're getting off on this stuff, aren't you?"
    scene 34_2_s8 with dissolve
    amelia "Call it what you like. All you need to know is I'll be {i}milking{/i} you day and night until I've drained every last drop."  
    amelia "Let's hope you taste better than the last disappointment."
    scene 34_2_s7 with dissolve
    mc "(This... isn't what I expected.)"
    mc "Listen, if semen is all you're after... we could work out some sort of arrangement. No cages, no shackles, no—"  
    scene 34_2_s9 with dissolve
    amelia "Oh, please. As if I'd fall for such a dull bargain."  
    scene 34_2_s7 with dissolve
    mc "No, seriously... I don't mind if we talked it out. I'm a very reasonable man..."
    scene 34_2_s8 with dissolve
    amelia "Enough. I'll return in an hour. Try not to bore me, darling."  
    scene 34_2_s10 with Dissolve(1.5)
    mc "*sigh* (...Well. Shit. Captured by a witch with a cum fetish.)"
    call screen scene34_witch2 with dissolve

label scene34_witch2_escape:
    scene 34_2_s2 with dissolve
    mc "(Screw this. No way I'm sticking around.)"
    scene 34_2_e_s1 with dissolve
    mc "(These ropes look loose. I bet I can wiggle my way out.)"
    scene 34_2_e_s2 with dissolve
    mc "(Hnggg!)"
    scene 34_2_e_s3 with vpunch
    mc "(Okay...)"
    scene 34_2_e_s4 with dissolve
    ""
    scene 34_2_e_s5 with Fade(0.5,0.5,0.5)
    mc "(Phew... now what?)"
    scene 34_2_e_s6 with Dissolve(1.5)
    ""
    scene 34_2_e_s7 with Dissolve(1.5)
    amelia "My beautiful darling, there isn't a day that goes by without me missing you by my side."
    amelia "One day, I will become powerful enough to bring you back. I swear on my name."
    scene 34_2_e_s8 with dissolve
    mc "(My sword!)"
    scene 34_2_e_s9 with Dissolve(1.0)
    if not karma_updated:
        $ karma_updated = True
        if mc_karma >= 100:
            $ mc_karma = 10
        elif mc_karma >= 90:
            $ mc_karma = 9
        elif mc_karma >= 80:
            $ mc_karma = 8
        elif mc_karma >= 70:
            $ mc_karma = 7
        elif mc_karma >= 60:
            $ mc_karma = 6
        elif mc_karma >= 50:
            $ mc_karma = 5
        elif mc_karma >= 40:
            $ mc_karma = 4
        elif mc_karma >= 30:
            $ mc_karma = 3
        elif mc_karma >= 20:
            $ mc_karma = 2
        elif mc_karma >= 10:
            $ mc_karma = 1
        else:
            $ mc_karma = 1
    if mc_karma > 10:
        $ mc_karma = 10
    if mc_karma < 1:
        $ mc_karma = 1
    call screen scene34_witch2_escape with dissolve

label scene34_witch2_alive:
    mc "(I guess I'm doing this...)"
    scene 34_2_e_s15 with fade
    ""
    play sound "sound_effects/punch.mp3"
    scene 34_2_e_s16 with vpunch
    ""
    play sound "sound_effects/bodydrop.mp3"
    scene 34_2_e_s17 with vpunch
    mc "..."
    mc "(Wow... That was easier than I thought.)"
    mc "(Without your magic staff, you're just a normal person, huh?)"
    mc "(Come on, let's get you back to Irda.)"
    scene 34_2_e_s19 with Fade(1.5,0.5,0.5)
    mc "Hah... haah..."
    mc "(Sorry, [horse]. Looks like you're gonna have to carry triple the weight this time...)"
    scene black with Fade(2.0,0.5,1.0)
    jump scene34_witch_finished

default quest_witch_amelia_dead_counted = False

label scene34_witch2_dead:
    mc "..."
    mc "(The quest said to bring her back alive...)"
    mc "(But she hurt so many people. This is for the better... right?)"
    scene 34_2_e_s10 with fade
    ""
    play sound "sound_effects/stab01.mp3"
    scene 34_2_e_s11 with vpunch
    if mc_karma > 1:
        $ mc_karma -= 3
    if mc_karma <= 0:
        $ mc_karma = 1
    $ quest_witch_amelia_dead_counted = True
    $ karma_less = True
    play sound "sound_effects/karma_less.mp3" volume 0.2
    show screen stat_change with easeinright
    amelia "Ughhhhh!"
    scene 34_2_e_s12 with dissolve
    ""
    hide screen stat_change with easeoutright
    $ karma_less = False
    scene 34_2_e_s13 with dissolve
    ""
    play sound "sound_effects/bodydrop.mp3"
    scene 34_2_e_s14 with vpunch
    mc "(Time to head back.)"
    scene 34_2_e_s18 with Fade(0.5,0.5,0.5)
    ""
    scene black with Fade(2.0,0.5,1.0)
    jump scene34_witch_finished


image scene34_hj1 = Movie(play="images/2_chapter1/scene34_witch2_concent/scene34_hj1.webm", loop=True)
image scene34_hj2 = Movie(play="images/2_chapter1/scene34_witch2_concent/scene34_hj2.webm", loop=True)
image scene34_hj3 = Movie(play="images/2_chapter1/scene34_witch2_concent/scene34_hj3.webm", loop=True)
image scene34_bj1 = Movie(play="images/2_chapter1/scene34_witch2_concent/scene34_bj1.webm", loop=True)
image scene34_bj2 = Movie(play="images/2_chapter1/scene34_witch2_concent/scene34_bj2.webm", loop=True)
image scene34_bj2_2 = Movie(play="images/2_chapter1/scene34_witch2_concent/scene34_bj2_2.webm", loop=True)
image scene34_tj1 = Movie(play="images/2_chapter1/scene34_witch2_concent/scene34_tj1.webm", loop=True)
image scene34_tj2 = Movie(play="images/2_chapter1/scene34_witch2_concent/scene34_tj2.webm", loop=True)

label scene34_witch2_consent:
    $ mcname = persistent.name
    if persistent.name == "None" or mcname == "None":
        while mcname == "None" or mcname == "":
            $ mcname = renpy.input("There was an issue with your name. Please rewrite your name:", length=32)
        $ persistent.name = mcname
    if not persistent.scene2_p2_replay:
        $ persistent.scene2_p2_replay = True
    scene 34_2_s10
    mc "I consent to anything you might do to me!"
    amelia "Whatever makes you feel better."
    scene 34_2_s2 with dissolve
    mc "..."
    scene black with Fade(0.5,0.5,1.5)
    play sound "sound_effects/door.mp3"
    scene 34_2_c_s1 with dissolve
    amelia "Ready or not, here I come~"
    scene 34_2_c_s2 with Dissolve(1.5)
    mc "What are you doing?"
    scene 34_2_c_s3 with Dissolve(1.0)
    mc "Woah..."
    scene 34_2_c_s4 with dissolve
    amelia "Let's begin."
    show scene34_hj1 with Dissolve(1.5)
    mc "Hey! You're gripping too hard!"
    mc "(Calm down. It's a handjob, I can take it...)"
    sensation "Her hand feels slick, slimy, like something more than sweat."
    logic "It isn't sweat—she's probably coated it in some sort of cream or lotion."
    amelia "Look into my eyes, darling. It'll make you feel better~"
    mc "Agh... You're too good at this..."
    amelia "I have lots of experience extracting semen. Now, no more talk. Just think about your cock and how good it will feel when you ejaculate~"
    show scene34_hj3 with Dissolve(1.5)
    hide scene34_hj1
    mc "Ngh..."
    mc "(Shit... I'm not gonna last long if she keeps playing with my balls!)"
    sensation "Her fingers gently knead your balls, the pressure subtle but firm, while her other hand teases the tip, sending shivers through your body."
    amelia "Do you like it when I massage your testicles? This is where all the tasty semen is stored."
    mc "Actually, that isn't true. It grows in the testicles but it isn't stored there..."
    amelia "I don't need you to lecture me on the male's anatomy. I know what I'm doing."
    mc "Ahhn... Fine."
    show scene34_hj2 with Dissolve(1.5)
    hide scene34_hj3
    mc "(Her fingers are fixated on my glans now... Fuck...)"
    sensation "Finally, her last move—constant teasing of the glans. Her slow, deliberate movements ironically drive you even crazier, each touch escalating the frustration."
    amelia "Oh my! Such a strong reaction~ Could I have found your weak spot?"
    mc "You did... Ahh..."
    amelia "Well, I already knew where your weak spot was. Don't worry, I'll be giving it lots of attention in the days to come."
    amelia "I'll even dedicate a whole day just for your glans, how about that?"
    mc "I can't... I'm close!"
    call screen scene34_witch2_consent_cum with dissolve
    scene 34_2_c_s5 with dissolve
    amelia "Ah, ah, ah! Not yet, darling."
    scene 34_2_c_s6 with dissolve
    mc "Wha-? Why did you stop?"
    scene 34_2_c_s7 with dissolve
    amelia "Oh, sweetheart, did you think that was all? I still need to nurture your semen."
    scene 34_2_c_s8 with dissolve
    mc "Nurture? What does that even mean?"
    scene 34_2_c_s5 with dissolve
    amelia "You'll see. It will be tastier that way. Just bear with me; it's all part of the approach."
    scene 34_2_c_s6 with dissolve
    mc "*sigh* I'm guessing you'll be doing this a lot..."
    scene 34_2_c_s5 with dissolve
    amelia "Mhm~ I'll be back in an hour."
    scene 34_2_c_s6 with dissolve
    mc "An hour!?"
    scene 34_2_c_s9 with Fade(1.0,0.5,0.5)
    mc "..."
    scene 34_2_c_s10 with dissolve
    mc "(It won't stop being erect...)"
    scene black with Fade(0.5,0.5,1.0)
    amelia "Are you ready, darling?"
    mc "*yawn* Huh...?"
    scene 34_2_c_s11 with vpunch
    amelia "Ahhhh~"
    scene 34_2_c_s12 with dissolve
    amelia "Nom~"
    show scene34_bj1 with Dissolve(1.5)
    hide scene34_hj2
    mc "(Damn, this is more intense than before...)"
    mc "Hey! (She's forcing her tongue down my urethra!)"
    sensation "You feel her tongue carefully probing its way into your urethra, while her tight, sealed lips tease the tip with intense pressure."
    mc "*laughs* So this is your next approach, huh?"
    amelia "Mhm~ *slurp*"
    show scene34_bj2_2 with Dissolve(1.5)
    hide scene34_bj1
    mc "Ahhh!"
    amelia "*slurp* *lick* Sho tashty~"
    show scene34_bj2 with Fade(0.5,0.5,0.5)
    hide scene34_bj2_2
    mc "Nghh!"
    sensation "She takes you deep into her throat, intentionally tightening her muscles around it."
    mc "Oh, god! It feels to good! I can't..."
    mc "I'm... I'm!"
    call screen scene34_witch2_consent_cum with dissolve
    scene 34_2_c_s15 with dissolve
    mc "For fuck's sake!"
    scene 34_2_c_s14 with dissolve
    amelia "Patience, darling. The best things take time."
    amelia "Be back in an hour~"
    scene 34_2_c_s13 with dissolve
    mc "You're driving me insane!"
    mc "(I don't know if I can take this anymore...)"
    scene black with Fade(0.5,0.5,0.5)
    amelia "This time, let's try something... softer."
    scene 34_2_c_s2 with dissolve
    mc "Huh... What is it this time?"
    scene 34_2_c_s16 with dissolve
    mc "What's that?"
    scene 34_2_c_s18 with dissolve
    amelia "I can feel your cock pulsating."
    amelia "Do you wish to ejaculate between my breasts?"
    scene 34_2_c_s19 with dissolve
    mc "I do!"
    amelia "Mhmmm~"
    mc "Just... please. I can't take it..."
    scene 34_2_c_s18 with dissolve
    amelia "Oh~? Where did that strong man go? You were running at me with full intent to kill when I ambushed you."
    scene 34_2_c_s19 with dissolve
    mc "T-That's not true. I was sent to capture you!"
    scene 34_2_c_s18 with dissolve
    amelia "Don't worry. Just provide me with lots of semen and I'll forgive you~"
    scene 34_2_c_s19 with dissolve
    show scene34_tj1 with Dissolve(1.5)
    hide scene34_bj2_2
    mc "Oh God... They're so slimy!"
    mc "(Fuck, I'm getting dizzy... Is it because of that... slime thing that she poured on her breasts?)"
    mc "Just please let me cum this time!"
    amelia "Ahh~ Just thinking about you covering my tits and face with your hot load makes me shiver~"
    amelia "You're a lucky man. Having soft, large tits enveloping your cock like this. Up... and down. Up... and down."
    mc "Get out of my head..."
    show scene34_tj2 with Dissolve(1.5)
    hide scene34_tj1
    amelia "Do you want me to open my mouth when you cum? Let all that tasty seed right into my throat~"
    amelia "Gulp, gulp~ *giggles* Right into my stomach. Will you be a good boy and cum for me?"
    mc "I can't hold it!"
    sensation "The weight of all that previous teasing, paired with the warmth and slickness of her breasts, sends electric shivers through your body. You're completely overwhelmed, unable to handle it any longer, both physically and mentally."
    call screen scene34_witch2_consent_cum with dissolve
    scene 34_2_c_s20 with dissolve
    amelia "No, not yet, big boy!"
    scene 34_2_c_s21 with dissolve
    mc "Oh, I am really starting to get angry with you Amelia..."
    scene 34_2_c_s20 with dissolve
    amelia "Oh~ You know my name? No introduction needed then."
    scene 34_2_c_s21 with dissolve
    mc "Too late for that."
    scene 34_2_c_s20 with dissolve
    amelia "*chuckles* I'll be bac-"
    scene 34_2_c_s21 with dissolve
    mc "Yeah, yeah. I get it..."
    amelia "Hmhmm~"
    scene 34_2_c_s22 with fade
    mc "(Just don't think about it... don't think about it...)"
    scene black with Fade(0.5,0.5,0.5)
    scene 34_2_c_s23 with fade
    mc "Hey! Is it time yet?"
    scene 34_2_c_s24 with dissolve
    amelia "Someone's impatient~"
    scene 34_2_c_s26 with dissolve
    ""
    scene 34_2_c_s27 with vpunch
    amelia "Oh my! I barely even touched you, and you look like you're ready to explode."
    scene 34_2_c_s25 with dissolve
    mc "Yeah, well, I {i}am{/i}."
    scene 34_2_c_s24 with dissolve
    amelia "Good. Good." 
    scene 34_2_c_s28 with Fade(0.5,0.5,0.5)
    amelia "Now, go ahead. Right into the bowl."
    scene 34_2_c_s29 with dissolve
    mc "The bowl? Seriously?"
    scene 34_2_c_s28 with dissolve
    amelia "Where else, silly? Now, do it for me, big boy!"
    scene 34_2_c_s29 with dissolve
    mc "..."
    scene 34_2_c_s30 with dissolve
    amelia "Come on! Do it!"
    amelia "do it for me big boy! Release all your seed!"
    amelia "Cum! Cum! Cum!"
    call screen scene34_witch2_consent_cum with dissolve
    play sound "se_sfx/blowjob/facial4.mp3" 
    scene 34_2_c_s31 with vpunch
    mc "NGGHHHH!!!"
    play sound "se_sfx/blowjob/facial5.mp3" 
    scene 34_2_c_s32 with vpunch
    mc "AGHHH!!!"
    play sound "se_sfx/blowjob/facial2.mp3" 
    scene 34_2_c_s33 with vpunch
    mc "Ahhhh!"
    scene 34_2_c_s34 with dissolve
    amelia "Good boy!"
    scene 34_2_c_s35 with dissolve
    mc "Haah... Haahh..."
    scene 34_2_c_s42 with dissolve
    amelia "Mmmm... Such potency~"
    scene 34_2_c_s37 with dissolve
    mc "I didn't know I could cum this much..."
    $ renpy.end_replay()
    scene 34_2_c_s36 with dissolve
    amelia "Oh, darling, this is still nothing. I once had a man hanging on for weeks."
    scene 34_2_c_s37 with dissolve
    mc "Weeks?! Umm..."
    scene 34_2_c_s36 with dissolve
    amelia "You should've seen that load. It was like a never-ending stream."
    amelia "A shame he ran off..."
    scene 34_2_c_s37 with dissolve
    mc "Haha... That's... uh... impressive?"
    scene 34_2_c_s36 with dissolve
    amelia "What's wrong, darling? Getting nervous?"
    scene 34_2_c_s37 with dissolve
    mc "You won't make {i}me{/i} wait for weeks, would you?"
    scene 34_2_c_s36 with dissolve
    amelia "Why not? In fact, that's exactly what I'm planning to do starting tomorrow. Take a rest today."
    scene 34_2_c_s37 with vpunch
    mc "Wait, wait, wait! I don't think I can take that. I'll go insane!"
    scene 34_2_c_s36 with dissolve
    amelia "Sorry, darling, but you don't get a say in the matter. Besides, breaking you {i}is{/i} part of the fun too."
    scene 34_2_c_s37 with dissolve
    mc "Okay... How about we strike a deal instead?"
    scene 34_2_c_s34 with dissolve
    amelia "A deal? You're not in a position to make deals, darling. But... go ahead. Humor me."
    scene 34_2_c_s35 with dissolve
    mc "Um, so how long do the guys you kidnap usually last before they... break?"
    scene 34_2_c_s34 with dissolve
    amelia "Oh, about two months... maybe three if they're particularly strong-willed."
    scene 34_2_c_s35 with dissolve
    mc  "And how often do you... capture someone?"
    scene 34_2_c_s38 with dissolve
    amelia "Hmm... not often. About one every four months. Why all the questions?"
    scene 34_2_c_s39 with dissolve
    mc "Because what you've got here is a terrible business plan! No passive income, no sustainability—"
    scene 34_2_c_s40 with dissolve
    amelia "Excuse me?!"
    scene 34_2_c_s41 with dissolve
    mc "Hear me out! Why don't you let {i}me{/i} provide you with my semen every now and then? That way, you won't have to kidnap men anymore."
    amelia "..."
    mc "Think about it—you'll have a steady supply, and you won't risk running into someone who could turn {i}you{/i} into the victim."
    scene 34_2_c_s40 with dissolve
    amelia "How do I know you're not tricking me?"
    scene 34_2_c_s41 with dissolve
    mc "Well... Uh..."
    scene 34_2_c_s38 with dissolve
    amelia "Hmm... I've been getting on in years and it's only a matter of time before I mess up and get caught."
    amelia "Fine. I am willing to make a deal."
    scene 34_2_c_s43 with dissolve
    amelia "However, I will cast a spell on your heart."
    scene 34_2_c_s39 with dissolve
    mc "Spell? What kind of spell?"
    scene 34_2_c_s38 with dissolve
    amelia "If I were to die, your heart will stop along with mine."
    scene 34_2_c_s39 with dissolve
    mc "Wait, what happens if you die by someone or something other than me?"
    scene 34_2_c_s36 with dissolve
    amelia "Then, I guess you're coming along with me, darling."
    scene 34_2_c_s37 with dissolve
    mc "Wow... okay... Deal. It beats my mind rotting in here I guess."
    scene 34_2_c_s44 with fade
    ""
    scene 34_2_c_s45 with fade
    ""
    scene 34_2_c_s46 with fade
    mc "Alright..."
    mc "Did you cast the spell already? You're pretty quick."
    scene 34_2_c_s47 with dissolve
    amelia "HAH!!"
    mc "You didn't, did you?"
    $ renpy.end_replay()
    call screen scene34_witch2_consent_after with dissolve

label scene34_witch2_consent_let:
    mc "Well, this is awkward, huh?"
    mc "It's all good though. Go ahead and do it..."
    scene 34_2_c_s48 with dissolve
    amelia "R-Really?"
    scene 34_2_c_s49 with dissolve
    mc "Sure..."
    scene 34_2_c_s50 with dissolve
    amelia "Huh... you're really don't mind dying with me..."
    scene 34_2_c_s51 with dissolve
    mc "I agreed to it, didn't I?"
    scene 34_2_c_s52 with dissolve
    amelia "You know what? I don't think I need to. You seem trustworthy. To a fault."
    scene 34_2_c_s53 with dissolve
    mc "Phew!"
    amelia "..."
    mc "Just to be sure, you won't be kidnapping any more people, right?"
    scene 34_2_c_s52 with dissolve
    amelia "Of course... As long as you keep providing me yourself."
    scene 34_2_c_s53 with dissolve
    mc "Fair enough. I'll head back to Irda and report what happened." 
    play sound "sound_effects/karma_more.mp3" volume 0.2
    if mc_karma < 10:
        $ mc_karma += 1
    $ karma_more = True
    show screen stat_change with easeinright  
    mc "I'll just say you ran off or something." 
    scene 34_2_c_s52 with dissolve
    amelia "Why are you doing this for me?" 
    hide screen stat_change with easeoutright
    $ karma_more = False
    scene 34_2_c_s53 with dissolve 
    mc "Dunno... I just feel like it."
    amelia "..."
    scene 34_2_e_s18 with Fade(0.5,0.5,0.5)
    ""
    scene black with Fade(2.0,0.5,1.0)
    jump scene34_witch_finished

label scene34_witch2_consent_attack:
    mc "Dumb bitch."
    scene 34_2_c_s54 with dissolve
    ""
    play sound "sound_effects/punch.mp3" volume 0.7
    scene 34_2_c_s55 with vpunch
    ""
    play sound "sound_effects/bodydrop.mp3" volume 0.7
    scene 34_2_c_s56 with vpunch
    mc "..."
    mc "Wow... That was easier than I thought."
    mc "Without your magic staff, you're just a normal person, huh?"
    mc "...Let's get you out of here."
    scene 34_2_c_s57 with Fade(0.5,0.5,0.5)
    mc "Hah... haah..."
    mc "Sorry, [horse]. Looks like you're gonna have to carry triple the weight this time..."
    scene black with Fade(2.0,0.5,1.0)
    jump scene34_witch_finished

label scene34_witch2_dead_fail:
    empathy "The thought flickers in your mind, fleeting and sharp, but it fades just as quickly. You know you can't—something inside you stops you from following through."
    call screen scene34_witch2_escape with dissolve
    
label scene34_witch_finished:
    $ cycle += 1
    play music "guild.mp3" fadein 3.0 loop
    scene irda_guild_night with Fade(0.5,0.5,0.5)
    ""
    scene 34_2_e_s20 with fade
    mc "Eireen, I'm back!"
    scene 21_s7 with Dissolve(0.8)
    eireen "Oh! That was quick. How did it go? Did you get her?"  
    if quest_witch_amelia_alive:
        if quest_witch_amelia_alive_free:
            scene 21_s8 with dissolve
            mc "Yes, you won't have to worry about any more kidnappings."
            scene 21_s2 with dissolve
            eireen "Huh? Is she not with you? You were supposed to bring her in for questioning. Her Majesty specifically requested—"  
            scene 21_s1 with dissolve
            mc "Yeah... she... ran off. Probably halfway to the next kingdom by now."
            scene 21_s6 with dissolve
            eireen "You didn't kill her, did you? Because if you killed her and you're covering it up—"
            scene 21_s5 with dissolve
            mc "No! I didn't! She's alive. Just... not here."
            scene 21_s3 with dissolve
            eireen "*sigh* Well, this complicates things. We needed her here to face justice for her crimes, you know?"
            scene 21_s4 with dissolve
            mc "Look, you won't be hearing any more from her. What's the issue? The problem is solved."
            scene 21_s3 with dissolve
            eireen "Try telling the victims that the witch who tortured them is still out there, free, because someone decided she wasn't worth pursuing."
            scene 21_s4 with dissolve
            mc "..." 
            scene 21_s6 with dissolve
            eireen "Whatever. You dealt with her, I suppose. But since she's not here to stand trial, you won't be getting the full reward."  
            scene 21_s5 with dissolve
            perception "She hands you five silver coins—duller, lacking the brilliant luster of the gold coins from earlier."
            $ mc_coin += 50
            mc "Better than nothing..."
            scene 21_s6 with dissolve
            eireen "Go ahead and take a rest for today, you've earned it."
            eireen "And [mc]? Next time, try to follow instructions. This is your only warning."
            scene 21_s5 with dissolve
            jump scene26
        else:
            scene 21_s8 with dissolve
            mc "She's outside, tied to my horse. She's not happy about it."
            scene 21_s7 with dissolve
            eireen "Alive, too? That's impressive."
            scene 21_s8 with dissolve
            mc "Yeah, well... she's not as powerful as I thought. Or as clever..."
            scene 21_s7 with dissolve
            eireen "Still, you managed to get the job done. The Queen will be pleased. The victims' families will have closure, and Amelia will finally face justice."
            eireen "Well done. Here's your reward."
            scene 21_s8 with dissolve
            perception "She hands you eight silver coins. Despite their number, they feel dull and unimpressive, lacking the brilliant luster of the gold coins from earlier."
            play sound "sound_effects/karma_more.mp3" volume 0.2
            if mc_karma < 10:
                $ mc_karma += 1
            $ mc_coin += 80
            $ karma_more = True
            show screen stat_change with easeinright  
            mc "Thanks. So, what happens to her now?"
            scene 21_s3 with dissolve
            eireen "The guards will take her to the dungeon. She'll rot there for the rest of her days, or until Her Majesty decides her fate."
            eireen "A fitting end, don't you think?"
            hide screen stat_change with easeoutright 
            $ karma_more = False
            scene 21_s4 with dissolve
            mc "I see... She won't escape? She's pretty slippery, so be careful."
            scene 21_s7 with dissolve
            eireen "There's a special dungeon designed for magic users only. Anti-magic wards. Enchanted shackles. She won't be casting any spells where she's going."
            eireen "Go ahead and take a rest for today, you've earned it."
            scene 21_s8 with dissolve
            jump scene26
    else:
        scene 21_s8 with dissolve
        mc "I did... but..."
        scene 21_s7 with dissolve
        eireen "What's wrong? You look like you've seen a ghost."
        scene 21_s8 with dissolve
        mc "She's dead. I killed her."
        scene 21_s3 with vpunch
        eireen "You {i}killed{/i} her?! The Queen's orders were explicit! We needed her alive!"
        scene 21_s4 with dissolve
        mc "She was dangerous, and it felt like the only way. It was her or me."
        scene 21_s3 with dissolve
        eireen "The only way?! That's convenient. Do you realize how much more useful she'd have been alive? {i}We needed her alive, hero{/i}."
        scene 21_s4 with dissolve
        mc "Look, I did what I had to. What's done is done. I can't bring her back, and I wouldn't if I could."
        eireen "..."
        scene 21_s6 with dissolve
        eireen "Ughh! Fine. But this complicates things for me, so I can't give you the full reward. Here's something for your trouble, but next time... {i}stick{/i} to the plan."
        eireen "The Queen's orders are not suggestions you can look past."
        scene 21_s5 with dissolve
        $ mc_coin += 10
        perception "She hands you a single silver coin. It feels unnaturally cold, almost as if it's leeching the warmth from your skin. Her hand retracts immediately, as if she's trying to avoid touching your skin."
        empathy "She's scared of you. What else are you capable of?"
        mc "Better than nothing, I guess."
        scene 21_s6 with dissolve
        eireen "Go ahead and take a rest for today, you've got more work tomorrow."
        eireen "And [mc]? Try not to kill the next target."
        scene 21_s5 with dissolve
        jump scene26
        
default yuuhi_harem_training_hj_first = True
default yuuhi_harem_training_hj_second = False
default yuuhi_harem_training_bj_first = False
default yuuhi_harem_training_bj_second = False

label yuuhi_harem_training:
    if yuuhi_harem_training_hj_first:
        scene 31_s15 with dissolve
        yuuhi "Umm... [mc]?"
        scene 31_s16 with dissolve
        mc "What's up?"
        scene 31_s15 with dissolve
        yuuhi "We're... a couple now, right?"  
        scene 31_s16 with dissolve
        mc "Yeah? Why, you changing your mind already?"
        scene 31_s17 with dissolve
        yuuhi "N-no! It's just... couples do couple things, don't they?"  
        scene 31_s16 with dissolve
        mc "That's... right? I don't really know what you're talking about."  
        scene 31_s15 with dissolve
        yuuhi "I'm talking about... sex."  
        scene 31_s16 with dissolve
        mc "...Oh." 
        scene 31_s15 with dissolve 
        yuuhi "I want us to... to try it."  
        scene 31_s16 with dissolve
        mc "But didn't you say you have to get married first?"  
        scene 31_s15 with dissolve
        yuuhi "Y-yes, but... there are other ways. Since my pussy is off-limits, I... I've been playing with my butt instead."  
        scene 31_s16 with dissolve
        mc "...Really?"
        scene 31_s15 with dissolve
        yuuhi "It feels good, [mc]! M-maybe even better than the pussy."  
        scene 31_s16 with dissolve
        mc "*chuckles* And here I thought you were just an innocent girl."  
        scene 31_s17 with dissolve
        yuuhi "I couldn't help it! What else could I do to... relieve myself?"  
        scene 31_s18 with dissolve
        mc "Fair point. Sometimes you just can't help it."  
        scene 31_s1 with dissolve
        yuuhi "See? And I know things aren't exactly... easy for you right now. Financially, I mean."
        scene 31_s2 with dissolve
        mc "Damn. Is it that obvious?"
        scene 31_s1 with dissolve
        yuuhi "Mmhm... so, I don't think you can buy me a ring anytime soon. But... that doesn't mean we can't have fun in other ways."  
        scene 31_s2 with dissolve
        mc "Hmm. Like what? You mean in the butt?"  
        scene 31_s15 with dissolve 
        yuuhi "Y-yes... but l-let's start slow."  
        scene 31_s16 with dissolve 
        mc "Slow is fine by me."  
        scene 31_s13 with dissolve
        yuuhi "And absolutely no sex in the pussy until we're married, promise!"  
        scene 31_s14 with dissolve
        mc "You have my word, princess."  
        scene 31_s13 with dissolve
        yuuhi "Then... maybe I can use my hands first."  
        scene 31_s14 with dissolve
        mc "A handy? I'll take it. Can't say no to that."  
        yuuhi "Mhmm~"
        jump yuuhi_harem_training2

    elif yuuhi_harem_training_hj_second:
        scene 31_s15 with dissolve
        yuuhi "Ready for another handy? Please say yes..."
        scene 31_s16 with dissolve
        scene black with Fade(1.0,0.5,0.5)
        stop music fadeout 3.0
        show is_yuuhi_anim_hj1 with dissolve
        ""
        scene is_yuuhi_hj4 with dissolve
        yuuhi "Does it feel good? Better than last time?"
        show is_yuuhi_anim_hj1 with dissolve
        ""
        scene is_yuuhi_hj4 with dissolve
        yuuhi "I-I learned something interesting... They say that staring at something... lewd while doing this makes it feel even better."
        scene is_yuuhi_hj5 with dissolve
        mc "Oh? Been researching how to break me?"
        scene is_yuuhi_hj4 with dissolve
        yuuhi "No. I just... want your voice to get all shaky like last time..."
        scene is_yuuhi_hj25 with vpunch
        yuuhi "L-LOOK AT MY BREASTS INSTEAD!"
        mc "Calm down!"
        show is_yuuhi_anim_hj1 with dissolve
        ""
        scene is_yuuhi_hj4 with dissolve
        yuuhi "A-are you ready to... pee?"
        scene is_yuuhi_hj25 with vpunch
        yuuhi "N-NOT PEE! E-EJACULATE! I MEANT EJACULATE!"
        mc "(My ears...)"
        show is_yuuhi_anim_hj1 with dissolve
        ""
        scene is_yuuhi_hj4 with dissolve
        yuuhi "What about now?"
        scene is_yuuhi_hj5 with dissolve
        mc "Less talking, more action..."
        scene is_yuuhi_hj4 with dissolve
        yuuhi "Ah! R-right, sorry."
        show is_yuuhi_anim_hj1 with dissolve
        $ yuuhi_hj_pov_toggle = True
        $ yuuhi_hj_pos_toggle = True
        call screen yuuhi_harem_training2_second_controls with dissolve
    elif yuuhi_harem_training_bj_first:
        stop music fadeout 2.0
        jump yuuhi_harem_training_bj_first
    elif yuuhi_harem_training_bj_second:
        stop music fadeout 2.0
        jump yuuhi_harem_training_bj_second
    elif yuuhi_harem_training_asex_first:
        stop music fadeout 2.0
        jump yuuhi_harem_training_asex_first

label yuuhi_harem_training2:
    scene is_yuuhi_hj1 with Fade(1.0,0.5,0.5)
    stop music fadeout 3.0
    yuuhi "I-I see that your... cock is already hard."
    scene is_yuuhi_hj2 with dissolve
    mc "Just happy to see you."
    scene is_yuuhi_hj1 with dissolve
    yuuhi "Ehee~"
    yuuhi "I haven't done this before, so... please be patient with me..."
    scene is_yuuhi_hj2 with dissolve
    mc "Don't worry. Just take your time."
    scene is_yuuhi_hj3 with dissolve
    yuuhi "It's so warm and... big..."
    yuuhi "{size=30}H-how does this even... fit inside someone?"
    mc "Yuuhi?"
    scene is_yuuhi_hj4 with dissolve
    yuuhi "Oh! S-sorry, I didn't mean to say that out loud!"
    yuuhi "Here I go..."
    show is_yuuhi_anim_hj1 with dissolve
    call screen yuuhi_harem_training2_controls with dissolve

label yuuhi_harem_training2_cum:
    mc "I'm close!"
    yuuhi "Eh?!"
    play sound "se_sfx/blowjob/facial1.mp3" 
    scene is_yuuhi_hj6 with vpunch
    mc "{i}Hnnnggg!!{/i}"
    play sound "se_sfx/blowjob/facial4.mp3" 
    scene is_yuuhi_hj7 with vpunch
    yuuhi "{i}Mfhmmm!{/i}"
    scene is_yuuhi_hj12 with dissolve
    mc "Hah... hah..."
    mc "You did great for your first time."
    scene is_yuuhi_hj10 with dissolve
    yuuhi "T-thank you..."
    yuuhi "I think... I might be able to do better next time."
    scene is_yuuhi_hj12 with dissolve
    mc "Next time, huh?"
    scene is_yuuhi_hj15 with dissolve
    yuuhi "O-oh! I mean... only if you want to, of course."
    yuuhi "And erm... can I wipe this off now?"
    scene is_yuuhi_hj16 with dissolve
    call screen yuuhi_harem_training2 with dissolve
    
label yuuhi_harem_training2_dwipe:
    if yuuhi_dep < 50:
        mc "Don't wipe my cum off."
        scene is_yuuhi_hj15 with dissolve
        yuuhi "Huh?! W-why would you want me to keep it on?"
        scene is_yuuhi_hj16 with dissolve
        mc "I like it, it looks good on you."
        scene is_yuuhi_hj14 with dissolve
        yuuhi "S-Sorry, [mc]. But I don't think I want to..."
        yuuhi "It feels weird and smells strange..."
        scene is_yuuhi_hj13 with dissolve
        mc "*chuckles* I suppose it will take time for you to get used to it."
        scene is_yuuhi_hj10 with dissolve
        yuuhi "*giggles* I don't know if I {i}want{/i} to get used to it~"
        scene is_yuuhi_hj12 with dissolve
        $ yuuhi_sex_times -= 1
    $ yuuhi_harem_training_hj_first = False
    $ yuuhi_harem_training_hj_second = True
    scene black with Fade(1.0,0.5,0.5)
    jump yuuhi_sex_end

label yuuhi_harem_training2_wipe:
    mc "You can wipe it off if you want."
    scene is_yuuhi_hj10 with dissolve
    yuuhi "Thank you... It feels so sticky and uncomfortable."
    scene is_yuuhi_hj12 with dissolve
    mc "You did great today."
    scene is_yuuhi_hj15 with dissolve
    yuuhi "I'll do even better next time, I promise!"
    scene is_yuuhi_hj16 with dissolve
    mc "Looking forward to it."
    scene black with Fade(1.0,0.5,0.5)
    $ yuuhi_harem_training_hj_first = False
    $ yuuhi_harem_training_hj_second = True
    $ yuuhi_sex_times -= 1
    jump yuuhi_sex_end

label yuuhi_harem_training_hj_second_cum:
    mc "I'm gonna...!"
    play sound "se_sfx/blowjob/facial4.mp3" 
    scene is_yuuhi_hj6 with vpunch
    mc "{i}Fuck!{/i}"
    play sound "se_sfx/blowjob/facial3.mp3" 
    scene is_yuuhi_hj7 with vpunch
    yuuhi "{i}Mhmmm...{/i}"
    scene is_yuuhi_hj10 with dissolve
    yuuhi "How was that?"
    scene is_yuuhi_hj12 with dissolve
    mc "It was fine, I guess."
    scene is_yuuhi_hj14 with dissolve
    yuuhi "Oh... Was I talking too much? I didn't mean to ruin the mood..."
    scene is_yuuhi_hj13 with dissolve
    mc "It's okay. You're still learning."
    scene is_yuuhi_hj14 with dissolve
    yuuhi "I see..."
    scene is_yuuhi_hj15 with dissolve
    yuuhi "I'll do better next time—I'll practice with a banan-"
    yuuhi "I-I mean—!"
    scene is_yuuhi_hj16 with dissolve
    mc "*chuckles* It's fine, do your thing."
    yuuhi "..."
    scene black with Fade(1.0,0.5,0.5)
    $ yuuhi_sex_times -= 1
    $ yuuhi_harem_training_hj_second = False
    $ yuuhi_harem_training_bj_first = True
    jump yuuhi_sex_end

label yuuhi_harem_training_bj_first:
    $ yuuhi_mouth_virgin = False
    mc "Yuuhi, let's tr-"
    scene 31_s15 with dissolve
    yuuhi "[mc]! Can I... suck it?"
    scene 31_s16 with dissolve
    mc "..."
    yuuhi "..."
    mc "What's with the sudden boost in confidence?"
    scene 31_s15 with dissolve
    yuuhi "I need to learn! A proper wife... should milk her husband dry... right?"
    scene 31_s16 with dissolve
    mc "Milk?! Who's teaching you these words?"
    scene 31_s15 with dissolve
    yuuhi "My friend, Ria. She seemed... experienced in these sort of things."
    yuuhi "I told her that I have a boyfriend now so she gave me a few pointers."
    yuuhi "Besides, the last two times weren't the best for you, so I want to make it up to you..."
    scene 31_s16 with dissolve
    mc "I wouldn't say it was awful..."
    mc "But hey, I can never say no to that."
    scene 31_s13 with dissolve
    yuuhi "Follow me~"
    scene 31_s14 with dissolve
    scene black with Fade(1.0,0.5,0.5)
    stop music fadeout 3.0
    scene is_yuuhi_bj1 with dissolve
    yuuhi "Haah... hah..."
    scene is_yuuhi_bj2 with dissolve
    yuuhi "{i}*Sniiifffff!*{/i}"
    mc "Don't do that..."
    scene is_yuuhi_bj3 with dissolve
    yuuhi "Sorry! It's just... when I gave you a handy before, the smell drove me crazy."
    yuuhi "It made my pussy feel weird..."
    yuuhi "I didn't even wash my hand after you left."
    scene is_yuuhi_bj4 with dissolve
    mc "I see..."
    scene is_yuuhi_bj5 with dissolve
    yuuhi "{i}*slurp*{/i}"
    scene is_yuuhi_bj6 with dissolve
    yuuhi "It tastes... strange."
    yuuhi "H-here I go."
    scene is_yuuhi_bj7 with dissolve
    ""
    scene is_yuuhi_bj8 with dissolve
    ""
    scene is_yuuhi_bj7 with dissolve
    ""
    scene is_yuuhi_bj8 with dissolve
    mc "(Oh man...)"
    scene is_yuuhi_bj3 with dissolve
    yuuhi "How does it feel?"
    scene is_yuuhi_bj4 with dissolve
    mc "Let me help you."
    yuuhi "Hmm?"
    scene is_yuuhi_bj9 with vpunch
    yuuhi "{i}Hnnnnggg!!! *gag*{/i}"
    mc "That's more like it."
    show is_yuuhi_anim_bj1 with dissolve
    yuuhi "{i}Agghhmmm!{/i}"
    yuuhi "{i}Mghmmgmmm!{/i}"
    call screen is_yuuhi_bj_controls_train1 with dissolve
    

label yuuhi_harem_training_bj_first_kiss:
    mc "Come here."
    scene is_yuuhi_bj39 with dissolve
    yuuhi "Mhmghh!"
    scene is_yuuhi_bj40 with dissolve
    ""
    scene is_yuuhi_bj41 with dissolve
    yuuhi "Uh... huhh... I..."
    scene is_yuuhi_bj42 with dissolve
    mc "I love you, Yuuhi."
    scene is_yuuhi_bj43 with dissolve
    yuuhi "[mc]!"
    scene is_yuuhi_bj44 with dissolve
    mc "It's true. From the moment I saw you, I knew you were the one for me."
    scene is_yuuhi_bj45 with vpunch
    mc "Yuuhi?"
    yuuhi "I need to go change my underwear!"
    mc "Hey! Your top is still here!"
    scene is_yuuhi_bj46 with dissolve
    mc "..."
    scene black with Fade(1.0,0.5,0.5)
    $ yuuhi_sex_times -= 1
    $ yuuhi_harem_training_bj_first = False
    $ yuuhi_harem_training_bj_second = True
    jump yuuhi_sex_end

label yuuhi_harem_training_bj_first_apologize:
    if is_yuuhi_bj_controls_train1_cum_outside:
        mc "I'm sorry, Yuuhi."
        scene is_yuuhi_bj31 with dissolve
        yuuhi "Y-you're sorry?"
        scene is_yuuhi_bj32 with dissolve
        mc "Yes. I pushed you too far."
        yuuhi "..."
        mc "As your future husband, I should've been more gentle with you."
        scene is_yuuhi_bj37 with dissolve
        yuuhi "No, it's fi—"
        scene is_yuuhi_bj38 with dissolve
        mc "I'll make it up to you. Thoroughly."
        scene is_yuuhi_bj37 with dissolve
        yuuhi "I-it's fine, [mc]! Really... Please don't worry about it."
        scene is_yuuhi_bj38 with dissolve
        mc "Thank you, I guess we're done with today's training then."
        scene is_yuuhi_bj37 with dissolve
        yuuhi "Yes~"
    else:
        mc "I'm sorry, Yuuhi."
        scene is_yuuhi_bj34 with dissolve
        yuuhi "Y-you're sorry?"
        scene is_yuuhi_bj33 with dissolve
        mc "Yes. I pushed you too far."
        yuuhi "..."
        mc "As your boyfriend, I should've been more gentle with you."
        scene is_yuuhi_bj35 with dissolve
        yuuhi "No, it's fi—"
        scene is_yuuhi_bj36 with dissolve
        mc "I'll make it up to you. Thoroughly."
        scene is_yuuhi_bj35 with dissolve
        yuuhi "I-it's fine, [mc]! Really... Please don't worry about it."
        scene is_yuuhi_bj36 with dissolve
        mc "Thank you, I guess we're done with today's training then."
        scene is_yuuhi_bj35 with dissolve
        yuuhi "Yes~"
        scene is_yuuhi_bj36 with dissolve
    scene black with Fade(1.0,0.5,0.5)
    $ yuuhi_sex_times -= 1
    $ yuuhi_harem_training_bj_first = False
    $ yuuhi_harem_training_bj_second = True
    jump yuuhi_sex_end

label is_yuuhi_bj_controls_train1_cum:
    call screen is_yuuhi_bj_controls_train1_cum with dissolve

label is_yuuhi_bj_controls_train1_cum_inside:
    play sound "se_sfx/blowjob/blowjob_cum1.mp3" 
    scene is_yuuhi_bj9 with vpunch
    mc "{i}Anghhh!{/i}"
    play sound "se_sfx/sex/sex_cum4.mp3" 
    scene is_yuuhi_bj10 with vpunch
    yuuhi "{i}Mggfhmmm!{/i}"
    scene is_yuuhi_bj11 with dissolve
    yuuhi "*cough!* *cough!* Ahhnngg..."
    scene is_yuuhi_bj12 with dissolve
    yuuhi "Ahhnngg..."
    mc "Good job, Yuuhi."
    scene is_yuuhi_bj18 with dissolve
    yuuhi "[mc]...!"
    scene is_yuuhi_bj17 with dissolve
    mc "Sorry, I thought I was helping you."
    scene is_yuuhi_bj18 with dissolve
    yuuhi "Helping? You shoved your whole... cock down my throat!"
    yuuhi "You should've warned me first!"
    scene is_yuuhi_bj17 with dissolve
    mc "..."
    $ yuuhi_total_cum_in_mouth += 3.94
    call screen is_yuuhi_bj_choice1 with dissolve

default is_yuuhi_bj_controls_train1_cum_outside = False
label is_yuuhi_bj_controls_train1_cum_outside:
    $ is_yuuhi_bj_controls_train1_cum_outside = True
    play sound "se_sfx/blowjob/facial4.mp3" 
    scene is_yuuhi_bj13 with vpunch
    yuuhi "*cough!* *cough!* Ahhnngg..."
    play sound "se_sfx/blowjob/facial2.mp3" 
    scene is_yuuhi_bj14 with vpunch
    mc "{i}Anghhh!{/i}"
    scene is_yuuhi_bj16 with dissolve
    mc "Good job, Yuuhi."
    scene is_yuuhi_bj15 with dissolve
    yuuhi "[mc]...!"
    scene is_yuuhi_bj16 with dissolve
    mc "Sorry, I thought I was helping you."
    scene is_yuuhi_bj15 with dissolve
    yuuhi "Helping? You shoved your whole... cock down my throat!"
    yuuhi "You should've warned me first!"
    scene is_yuuhi_bj16 with dissolve
    mc "..."
    call screen is_yuuhi_bj_choice1 with dissolve

label yuuhi_harem_training_bj_second:
    scene 31_s13 with dissolve
    yuuhi "[mc]... My throat is still sore from last time but I-I want to... taste it again. Properly this time..."
    scene 31_s14 with dissolve
    mc "Oh? Really?"
    yuuhi "Mhmm~"
    mc "I can't possibly deny my dear girlfriend, can I?"
    scene 31_s13 with dissolve
    yuuhi "You absolutely cannot~"
    scene 31_s14 with dissolve
    mc "Well... I suppose there's not much I can do about it now."
    stop music fadeout 3.0
    scene black with Fade(1.0,0.5,0.5)
    scene is_yuuhi_bj47 with dissolve
    yuuhi "I want you be rough this time, [mc]~"
    scene is_yuuhi_bj50 with dissolve
    mc "You know how to get me going."
    scene is_yuuhi_bj51 with dissolve
    yuuhi "I still can't get over how big it is..."
    mc "Open your mouth."
    scene is_yuuhi_bj52 with dissolve
    yuuhi "Ahhhh~"
    show is_yuuhi_anim_bj3 with dissolve
    yuuhi "{i}Ahhhh~! *gag*{/i}"
    yuuhi "{i}Mgfmmm!{/i}"
    call screen is_yuuhi_bj_controls_train2 with dissolve

label is_yuuhi_bj_controls_train2_cum:
    call screen is_yuuhi_bj_controls_train2_cum with dissolve

label is_yuuhi_bj_controls_train2_cum_inside:
    mc "I'm cumming!"
    yuuhi "{i}Mfhmm~{/i}"
    play sound "se_sfx/sex/sex_cum1.mp3" 
    scene is_yuuhi_bj53 with vpunch
    yuuhi "{i}Hfhmm!{/i}"
    play sound "se_sfx/sex/sex_cum2.mp3" 
    scene is_yuuhi_bj53 with vpunch
    mc "{i}Aghhh!{/i}"
    scene is_yuuhi_bj54 with dissolve
    yuuhi "I caugh et in ma moush~"
    scene is_yuuhi_bj55 with dissolve
    play sound "se_sfx/blowjob/swallow3.mp3" 
    yuuhi "{i}*gulp* *gulp* *gulp*{/i}"
    scene is_yuuhi_bj56 with dissolve
    yuuhi "Ahhhh~"
    scene is_yuuhi_bj60 with dissolve
    mc "Good girl. You're learning quick."
    scene is_yuuhi_bj59 with dissolve
    yuuhi "I'm so glad..."
    yuuhi "I... I barely slept last time..."
    scene is_yuuhi_bj60 with dissolve
    mc "Why's that?"
    scene is_yuuhi_bj59 with dissolve
    yuuhi "I kept... hnngh... thinking about you..."
    yuuhi "About... us."
    yuuhi "A-about claiming me... filling me..."
    yuuhi "W-when we're married... y-you'll fill me up every night, right? Deep inside my pussy..." 
    yuuhi "I. Cant. Wait..."
    scene is_yuuhi_bj60 with dissolve
    mc "..."
    yuuhi "..."
    scene is_yuuhi_bj63 with dissolve
    yuuhi "Ah! I-I mean—"
    scene is_yuuhi_bj45 with vpunch
    mc "..."
    scene is_yuuhi_bj46 with dissolve
    mc "(There she goes again...)"
    scene black with Fade(1.0,0.5,0.5)
    $ yuuhi_sex_times -= 1
    $ yuuhi_total_cum_in_mouth += 4.25
    $ yuuhi_harem_training_bj_second = False
    $ yuuhi_harem_training_asex_first = True
    jump yuuhi_sex_end

label is_yuuhi_bj_controls_train2_cum_outside:
    mc "I'm cumming!"
    yuuhi "{i}Mfhmm~{/i}"
    scene is_yuuhi_bj61 with vpunch
    mc "{i}Aghhh!{/i}"
    scene is_yuuhi_bj62 with vpunch
    yuuhi "{i}Mmmm~{/i}"
    scene is_yuuhi_bj57 with dissolve
    yuuhi "{i}*cough!* *cough!*{/i} Was I good? {i}*sniff*{/i}"
    scene is_yuuhi_bj58 with dissolve
    mc "You were really good."
    scene is_yuuhi_bj57 with dissolve
    yuuhi "I'm so glad..."
    yuuhi "I... I barely slept last time..."
    scene is_yuuhi_bj58 with dissolve
    mc "Why's that?"
    scene is_yuuhi_bj57 with dissolve
    yuuhi "I kept... hnngh... thinking about you..."
    yuuhi "About... us."
    yuuhi "A-about claiming me... filling me..."
    yuuhi "W-when we're married... y-you'll fill me up every night, right? Deep inside my pussy..." 
    yuuhi "I. Cant. Wait..."
    scene is_yuuhi_bj58 with dissolve
    mc "..."
    yuuhi "..."
    scene is_yuuhi_bj64 with dissolve
    yuuhi "Ah! I-I mean—"
    scene is_yuuhi_bj45 with vpunch
    mc "..."
    scene is_yuuhi_bj46 with dissolve
    mc "(There she goes again...)"
    scene black with Fade(1.0,0.5,0.5)
    $ yuuhi_sex_times -= 1
    $ yuuhi_harem_training_bj_second = False
    $ yuuhi_harem_training_asex_first = True
    jump yuuhi_sex_end

label yuuhi_harem_training_asex_first:
    scene 31_s15 with dissolve
    yuuhi "Um, [mc]? Can you come and look at my butthole?"
    scene 31_s16 with dissolve
    mc "..."
    mc "You {i}really{/i} need to work on your conversation openers."
    scene 31_s15 with dissolve
    yuuhi "I'm serious! Since my pussy is off-limits until we're married, I thought I should... you know, prepare my butt for you."
    yuuhi "And also because a-anal sex strengthens... hnngh... marital bonds..."
    scene 31_s16 with dissolve
    mc "Ahuh..."
    scene 31_s15 with dissolve
    yuuhi "But I haven't put anything back there larger than my fingers, so I asked my friend again."
    scene 31_s16 with dissolve
    mc "She's a bad influence on you... You should probably stop talking to her."
    scene 31_s15 with dissolve
    yuuhi "Come, I want to show you something."
    scene 31_s16 with dissolve
    scene black with Fade(1.0,0.5,0.5)
    scene is_yuuhi_asex1 with dissolve
    yuuhi "Look! I-I bought this from the market"
    mc "Whoa, is that a... buttplug?"
    yuuhi "Yes... Ria said it'd help me get ready for, um, butt stuff."
    yuuhi "But..."
    mc "Something wrong?"
    yuuhi "...It's stuck! Help meeee!"
    mc "Don't worry, I got it."
    scene is_yuuhi_asex3 with dissolve
    yuuhi "This is so embarrassing..."
    scene is_yuuhi_asex2 with dissolve
    yuuhi "Slowly, okay? Ow! Ow! Easy!"
    play sound "se_sfx/sex/touch1.mp3" 
    scene is_yuuhi_asex2 with vpunch
    "pop!"
    scene is_yuuhi_asex4 with dissolve
    yuuhi "{i}Haaaahhh...{/i}"
    scene is_yuuhi_asex5 with Fade(0.5,0.5,0.5)
    yuuhi "Thank you, I can finally breath now..."
    scene is_yuuhi_asex6 with dissolve
    call screen is_yuuhi_sex_choice1 with dissolve 

label is_yuuhi_sex_choice1_shove:
    $ yuuh_suck_plug = True
    mc "Open wide."
    scene is_yuuhi_asex5 with dissolve
    yuuhi "Wha—"
    scene is_yuuhi_asex7 with vpunch
    yuuhi "{i}Mghmm!{/i}"
    mc "Suck it clean."
    scene is_yuuhi_asex8 with dissolve
    yuuhi "Ew! Ew! Ew!"
    scene is_yuuhi_asex10 with dissolve
    mc "Relax, it was clean."
    scene is_yuuhi_asex9 with dissolve
    yuuhi "T-that's not the point!"
    scene is_yuuhi_asex10 with dissolve
    mc "Sorry..."
    scene is_yuuhi_asex11 with dissolve
    yuuhi "*sigh* I can't get mad at you... You're just... teasing me because you love me, right?"
    scene is_yuuhi_asex12 with dissolve
    mc "Yes! Well... because it's hot too. Seeing you suck on the buttplug you've been wearing."
    scene is_yuuhi_asex11 with dissolve
    yuuhi "Mhmm~"
    scene is_yuuhi_asex12 with dissolve
    mc "Now that's done, shall we?"
    scene is_yuuhi_asex11 with dissolve
    yuuhi "Yes..."
    scene is_yuuhi_asex12 with dissolve
    mc "Yes, what?"
    scene is_yuuhi_asex11 with dissolve
    yuuhi "Yes... sir?"
    scene is_yuuhi_asex12 with dissolve
    mc "That wasn't what I had in mind, but okay."
    mc "Face the wall, girl."
    scene black with Fade(1.0,0.5,0.5)
    yuuhi "Can you be less menacing, please?"
    jump yuuhi_harem_training_asex_first3

label yuuhi_harem_training_asex_first2:
    mc "Now that's done, shall we?"
    scene is_yuuhi_asex5 with dissolve
    yuuhi "O-okay..."
    scene is_yuuhi_asex6 with dissolve
    mc "Face the wall, girl."
    scene black with Fade(1.0,0.5,0.5)
    yuuhi "Can you be less menacing, please?"
    jump yuuhi_harem_training_asex_first3
    
label yuuhi_harem_training_asex_first3:
    scene is_yuuhi_asex27 with dissolve
    $ is_yuuhi_anim_asex1 = True
    yuuhi "{i}Agh!{/i} W-wait!"
    mc "What is it?"
    yuuhi "Umm... Could you say something romantic first?"
    mc "Romantic, huh? Fine... You're the most beautiful woman I've ever met. And trust me, I've met a lot of women. But none of them make my heart race like you do."
    if mc_told_yuuhi_maia:
        yuuhi "Wait—what? You've met a lot of women? [mc], but you only ever mentioned Maia—"
    else:
        yuuhi "Wait—what? You've met a lot of women? [mc], what's that supposed to mean—"
    show is_yuuhi_anim_asex2 with dissolve
    yuuhi "{i}AHH!!!{/i}"
    yuuhi "I-It's... soo big...!"
    mc "I should buy you a bigger plug one day." 
    yuuhi "T-too... full...!"
    call screen is_yuuhi_asex_controls_train1 with dissolve 

label is_yuuhi_asex_controls_train_cum:
    call screen is_yuuhi_asex_controls_train_cum with dissolve

label is_yuuhi_asex_controls_train_cum_inside:
    mc "I'm cumming!"
    play sound "se_sfx/sex/sex_cum5.mp3" 
    scene is_yuuhi_asex14 with vpunch
    yuuhi "{i}Amghhhh!{/i} T-too deep! It's— hnngh— stretching me open!"
    play sound "se_sfx/sex/sex_cum4.mp3" 
    scene is_yuuhi_asex14 with vpunch
    mc "{i}Nghhhhh!!{/i} Take it all!"
    scene is_yuuhi_asex15 with dissolve
    yuuhi "{i}Haaaa!{/i} I-I feel it... pooling inside..."
    mc "Hah... hah..."
    mc "You okay? Still breathing?"
    yuuhi "{i}*Hic...*{/i} Just... tired..."
    mc "Overdid it?"
    yuuhi "N-no! Don't worry, [mc]... As your future wife... I'll adapt over time..."
    mc "Don't go too hard on yourself... Anyway, training's over."
    yuuhi "How would you rate me?"
    mc "You have the tightest ass ever, Yuuhi. So it's a full mark for you."
    yuuhi "Hehe~ Well, I hope you don't stop coming now that my training's is over~ My butt hole will always be waiting for you." 
    scene black with Fade(1.0,0.5,0.5)
    perception "You cradle her shivering body until she can walk again, your cum seeping through her panties."
    $ is_yuuhi_sex_limit -= 1
    $ yuuhi_harem_training_bj_second = False
    $ yuuhi_harem_training_asex_first = False
    $ yuuhi_total_cum_in_ass += 4.87
    jump yuuhi_sex_end

label is_yuuhi_asex_controls_train_cum_outside:
    mc "I'm cumming!"
    play sound "se_sfx/blowjob/facial4.mp3" 
    scene is_yuuhi_sex16 with vpunch
    yuuhi "{i}Amghhhh!{/i}"
    play sound "se_sfx/blowjob/facial5.mp3" 
    scene is_yuuhi_sex17 with vpunch
    mc "{i}Nghhhhh!!{/i}"
    scene is_yuuhi_sex18 with dissolve
    yuuhi "{i}Haaaa!{/i} I-It's so... hot..."
    mc "Hah... hah..."
    mc "You okay?"
    yuuhi "I'm... fine..."
    mc "Did i over do it?"
    yuuhi "N-no! Don't worry, [mc]... Your future wife... will get used to it..."
    mc "Don't go too hard on yourself... Anyway, training's over."
    yuuhi "How would you rate me?"
    mc "You have the tightest ass ever, Yuuhi. So it's a full mark for you."
    yuuhi "Hehe~ Well, I hope you don't stop coming now that my training's is over~ My butt hole will always be waiting for you." 
    scene black with Fade(1.0,0.5,0.5)
    perception "You cradle her shivering body until she can walk again, your cum seeping through her panties."
    $ yuuhi_harem_training_bj_second = False
    $ yuuhi_harem_training_asex_first = False
    jump yuuhi_sex_end
 
default in_scene35 = False
label scene35:
    stop music fadeout 2.0
    $ mc_permission_reb = True
    $ in_scene34 = False
    $ in_scene35 = True
    scene 29_s1 with Fade(0.5,0.5,0.5)
    ""
    "*knock* *knock*"
    scene 29_s2 with dissolve
    m "Oh! Your Majesty! Welcome, please, have a seat! Would you like me to bring you something?"
    q "Thank you, Maia, but that won't be necessary. I won't be staying long."
    m "As you wish."
    mc "(Huh?)"
    scene 29_s3 with dissolve
    mc "(Oh shit!)"
    play music "side_event6.mp3" fadein 3.0 loop
    scene 35_s1 with fade
    mc "Your Majesty?"
    scene 35_s2 with dissolve
    q "Good morning, [mc]. I hope I haven't disturbed you too early. I need to speak with you about your recent task."
    scene 35_s1 with dissolve
    mc "Of course. I should've told you sooner but I didn't see you yesterday."
    scene 35_s2 with dissolve
    q "No worries. And yes, I wasn't available yesterday anyway."
    if quest_witch_amelia_dead:
        scene 35_s3 with dissolve
        q "I heard from Eireen that you killed her. Would you care to explain why?"
        scene 35_s4 with dissolve
        mc "It was the best course of action, Your Majesty. She was dangerous."
        scene 35_s3 with dissolve
        q "That was {i}not{/i} your decision to make, [mc]. The only reason I would accept this is if she was an imminent threat to your life."
        q "But according to Eireen, you were... calm. Far too calm when you spoke with her."
        scene 35_s4 with dissolve
        mc "I did what had to be done, Your Majesty."        
        q "..."
        scene 35_s3 with dissolve
        q "*sigh* Fine. But I will not tolerate another reckless mistake like this. Am I clear, [mc]?"
        scene 35_s4 with dissolve
        mc "...Understood."
        scene 35_s3 with dissolve
        q "Despite your failure on following basic instructions, I will still reward you. You may take permanent residence in Maia's room."
        scene 35_s4 with dissolve
        mc "Thank you, Your Magesty."
    elif not quest_witch_amelia_alive_free:
        scene 35_s2 with dissolve
        q "I heard you managed to capture her. Well done."
        scene 35_s1 with dissolve
        mc "Thank you."
        scene 35_s3 with dissolve
        q "I knew there was potential in you."
        q "I trust you will continue to carry out your duties with the same level of precision."
        scene 35_s4 with dissolve
        mc "I'll try my best."
        scene 35_s3 with dissolve
        q "Good. Now for your reward. You may take permanent residence in Maia's room."
        scene 35_s4 with dissolve
        mc "Thank you, Your Magesty."
    elif quest_witch_amelia_alive_free:
        scene 35_s3 with dissolve
        q "I heard from Eireen that you {i}let{/i} her go. Care to explain what she meant by that?"
        scene 35_s4 with dissolve
        mc "I... believed she wouldn't cause harm anymore. She gave me her word."
        scene 35_s3 with dissolve
        q "And you expect me to take her word for it?"
        scene 35_s4 with dissolve
        mc "I'm not a fighter, Your Majesty. Talking to her was the better choice."
        scene 35_s3 with dissolve
        q "So you took the diplomatic route this time? [mc], need I remind you that she is a criminal, not just some common troublemaker?"
        if maia_happy:
            scene 35_s5 with dissolve
            m "Y-Your Majesty..."
            scene 35_s6 with dissolve
            q "What is it, Maia?"
            scene 35_s7 with dissolve
            m "I'm certain that [mx] did the best he could."
            scene 35_s8 with dissolve
            q "Hmm? You seem more confident than usual, Maia."
            scene 35_s2 with dissolve
            q "Is this your influence, [mc]?"
            scene 35_s1 with dissolve
            mc "..."
            scene 35_s2 with dissolve
            q "*sigh* I suppose time will tell. But if this witch goes back on her word, I'll know exactly who to hold responsible. Won't I, [mc]?"
            q "Despite your mistake, I will still reward you. You may take permanent residence in Maia's room."
            scene 35_s4 with dissolve
            mc "Thank you, Your Majesty."
        else:
            q "Speak, [mc]. Do you have nothing to say?"
            scene 35_s4 with dissolve
            mc "I did the best I could, Your Majesty. I can assure you of that..."
            scene 35_s3 with dissolve
            q "*sigh* I suppose time will tell. But if this witch goes back on her word, I'll know exactly who to hold responsible. Won't I, [mc]?"
            q "Despite your mistake, I will still reward you. You may take permanent residence in Maia's room."
            scene 35_s4 with dissolve
            mc "Thank you, Your Majesty."
    scene 35_s14 with dissolve
    q "And what about you, Maia?"
    scene 35_s9 with dissolve
    m "Y-Yes, Your Majesty?"
    scene 35_s14 with dissolve
    q "How are things between you and your husband?"
    if maia_happy:
        scene 35_s7 with dissolve
        m "I'm doing very well, Your Majesty! [mx] is very kind to me!"
        scene 35_s8 with dissolve
        q "Is that so?"
        scene 35_s7 with dissolve
        m "Yes! I-I... love him!"
        scene 35_s8 with dissolve
        q "*chuckles* I see. Quite the budding relationship we have here."
        scene 35_s7 with dissolve
        m "A-And! H-He even let me keep Crumps!"
        scene 35_s8 with dissolve
        q "Oh, that devil cat? Glad he isn't roaming the courtroom anymore."
        scene 35_s2 with dissolve
        q "[mc], Maia may sound meek, but I assure you, she is more than capable."
        q "She had a difficult past—wandering the streets before my daughter found her. No matter how much I pried, she never spoke of it."
        q "But perhaps she will with you? I trust you'll continue treating her well."
        scene 35_s1 with dissolve
        mc "I will."
        scene 35_s2 with dissolve
        q "Lastly, how is your relationship with my daughter?"
        scene 35_s1 with dissolve
        mc "Rebecca? It's... almost nonexistent, to be honest."
        scene 35_s2 with dissolve
        q "I see. That won't do."
        scene 35_s3 with dissolve
        q "Rebecca may seem distant, but she's actually a very sensitive girl. I doubt she enjoys walking these halls with a man she barely knows."
        q "I want you to prove to her that you're someone she can trust."
        scene 35_s4 with dissolve
        mc "But... how?"
        scene 35_s3 with dissolve
        q "Have you tried simply talking to her?"
        scene 35_s4 with dissolve
        mc "I guess not..."
        scene 35_s3 with dissolve
        q "Then go. She's most likely on the roof right now, lost in one of her books."
        scene 35_s4 with dissolve
        mc "I'll try."
        scene 35_s3 with dissolve
        q "Good. It's crucial that you two at least become friends."
        scene 35_s4 with dissolve
    elif maia_sad:
        $ mc_maia_left = True
        $ mc_marital = "divorced"
        scene 35_s10 with dissolve
        m "I... I..."
        stop music fadeout 2.0 
        scene 35_s6 with dissolve
        q "What's wrong, Maia?"

        scene 35_s11 with dissolve
        m "I... I'm sorry, Your Majesty. I'll try... to be a better wife."
        scene 35_s12 with dissolve
        q "I see... It seems things aren't working out between you two."
        scene 35_s11 with dissolve
        m "N-No! Your Majesty, please... just... *sniff* give me more time... I'll try harder..."
        scene 35_s12 with dissolve
        q "There's no need, Maia. You've done enough."
        scene 35_s15 with dissolve
        q "Hero, I'll be taking Maia away. It seems you two weren't compatible after all. I'll handle the divorce arrangements."
        q "In the meantime, it looks like you'll be single. But I'm sure you'll find someone else out there if you haven't already."
        scene 35_s16 with dissolve
        mc "Thank you, Your Majesty..."
        scene 35_s12 with dissolve
        q "Leave, Maia. I will find you another place to stay. This room belongs to [mc] now."
        scene black with Fade(0.5,0.5,0.5)
        perception "She walks to the door, her hand reaching out to pull the handle. Without a glance back, she steps through and leaves the room, the door closing softly behind her."
        scene 35_s13 with fade
        q "Lastly, how is your relationship with my daughter?"
        scene 35_s17 with dissolve
        mc "Rebecca? It's... almost nonexistent, to be honest."
        scene 35_s13 with dissolve
        q "I see. That won't do."
        scene 35_s17 with dissolve
        mc "What do you mean?"
        scene 35_s13 with dissolve
        q "Rebecca may seem distant, but she's actually a very sensitive girl. I doubt she enjoys walking these halls with a man she barely knows."
        q "I want you to prove to her that you're someone she can trust."
        scene 35_s17 with dissolve
        mc "But... how?"
        scene 35_s13 with dissolve
        q "Have you tried simply talking to her?"
        scene 35_s17 with dissolve
        mc "I guess not..."
        scene 35_s13 with dissolve
        q "Then go. She's most likely on the roof right now, lost in one of her books."
        scene 35_s17 with dissolve
        mc "I'll try."
        scene 35_s13 with dissolve
        q "Good. It's crucial that you two at least become friends."
            
    if maia_sad and quest_witch_amelia_dead:
        q "That will be all. But I must say, this is quite concerning, [mc]."
        scene 35_s13 with dissolve
        mc "What do you mean, Your Majesty?"
        scene 35_s17 with dissolve
        q "You mistreat your wife and defied my orders by killing the witch, despite being explicitly told not to."
        scene 35_s13 with dissolve
        q "Tell me—what exactly are you planning? Have I mistakenly welcomed a monster into my castle?"
        scene 35_s17 with dissolve
        mc "..."
        scene 35_s13 with dissolve
        q "I'll be watching you, [mc]. Don't give me a reason to act."
        scene 35_s17 with dissolve
        mc "I understand."
        scene 35_s13 with dissolve
        q "*sigh* Once you're done with Rebecca. Visit Eireen for your next task, [mc]."
        scene 35_s17 with dissolve
        mc "Got it."
        scene 35_s13 with dissolve
        q "Good. Then I'll take my leave."
        scene 35_s17 with dissolve
        scene black with Fade(0.5,0.5,0.5)
        jump free_roam_main_label
    elif maia_sad and quest_witch_amelia_alive_free:
        scene 35_s13 with dissolve
        q "Once you're done with Rebecca. Visit Eireen for your next task, [mc]."
        scene 35_s17 with dissolve
        mc "Got it."
        scene 35_s13 with dissolve
        q "Good. Then I'll take my leave."
        scene 35_s17 with dissolve
        scene black with Fade(0.5,0.5,0.5)
        jump free_roam_main_label
    elif maia_sad and not quest_witch_amelia_alive_free:
        scene 35_s13 with dissolve
        q "Once you're done with Rebecca. Visit Eireen for your next task, [mc]."
        scene 35_s17 with dissolve
        mc "Got it."
        scene 35_s13 with dissolve
        q "Good. Then I'll take my leave."
        scene 35_s17 with dissolve
        scene black with Fade(0.5,0.5,0.5)
        jump free_roam_main_label
    elif maia_happy:
        scene 35_s2 with dissolve
        q "That will be all. I must say, you are growing on me, [mc]."
        scene 35_s1 with dissolve
        mc "What do you mean, Your Majesty?"
        scene 35_s2 with dissolve
        if not quest_witch_amelia_alive_free:
            q "This girl here loves you—I can see it in her eyes. And you managed to capture the witch as well."
            q "A fine job indeed."
        elif quest_witch_amelia_alive_free:
            q "This girl here loves you—I can see it in her eyes. And as for the witch... you handled the situation, even if not as I intended."
            q "Nevertheless, you got the job done."
        scene 35_s1 with dissolve
        mc "Thank you, your Majesty. I try me best."
    
    scene 35_s2 with dissolve
    q "Once you're done with Rebecca. Visit Eireen for your next task, [mc]."
    scene 35_s1 with dissolve
    mc "Got it."
    scene 35_s2 with dissolve
    q "Good. Then I'll take my leave."
    scene 35_s1 with dissolve
    scene black with Fade(0.5,0.5,0.5)
    jump free_roam_main_label

    #if maia_know_wed_reb:
        #scene 35_s19 with Fade(0.5,0.5,0.5)
        #mc "Maia, about me wanting to marry the princess, I—"
        #scene 35_s18 with dissolve
        #m "Y-you should do what Her Majesty asked you, [mx]..."
        #scene 35_s19 with dissolve
        #mc  "...Alright. But we'll talk about this later."
        #m "..."

label scene35_choice01_op1:
    scene 35_s21 with vpunch
    mc "PRINCESS!!!"
    scene 35_s22 with dissolve
    r "Shut up! What the hell are you screaming for?! Do you want the guards to think I'm being murdered?!"
    scene 35_s21 with dissolve
    mc "You didn't respond the first time..."
    jump scene35_continue

label scene35_choice01_op2:
    perception "You spot a small pebble resting peacefully on the ground and pick it up."
    scene 35_s23 with dissolve
    r "Ah!"
    scene 35_s24 with dissolve
    r "Did you just—?"
    scene 35_s25 with dissolve
    mc "I'm sorry! I didn't mean to hit you in the face!"
    scene 35_s24 with dissolve
    r "Try that again, and I'll throw you off the roof!"
    scene 35_s25 with dissolve
    mc "Got it."
    jump scene35_continue

label scene35_choice01_op3:
    scene 35_s26 with dissolve
    mc "Oh most elegant and noble princess, gracing us with her presence above the filthy mortals. Might one such as I dare to request an audience?"
    jump scene35_continue

label scene35_continue:
    if mc_told_reb_harem:
        scene 35_s22 with dissolve
        r "*sigh* What do you want? Don't tell me you came to propose."
        scene 35_s21 with dissolve
        mc "...And if I did?"
        scene 35_s22 with dissolve
        r "*scoff* Then I'd say no."  
        scene 35_s21 with dissolve
        mc "You're too mean, you know that? I'm just trying to be friendly."
        scene 35_s22 with dissolve
        r "Mean? Oh, I'm sorry! Should I be throwing flowers at your feet instead? Should I be swooning at the heroic stranger who caught my mother's eye?"
        scene 35_s21 with dissolve
        mc "No, but... maybe I could do something for you. Prove myself. Earn your trust." 
        scene 35_s22 with dissolve
        r "Forget it, [mc]. I'm too tired for games."
        r "I've been playing them my whole life. Every suitor. Every noble... *sigh* I'm tired."
        scene 35_s21 with dissolve
        mc "Then let's stop playing games. Tell me what's wrong. I'll fix it, whatever it is."  
        scene 35_s22 with dissolve
        r "You don't get it, do you? It's not something you can hammer straight like a bent nail. Some things just... stay broken." 
        scene 35_s21 with dissolve
        mc "*sigh* Can we at least be friends?"
        scene 35_s30 with dissolve
        r "Wait—was this her idea? Did she put you up to this?"
        scene 35_s31 with dissolve
        mc "...Yeah. She thought it would be good if we talked. She's worried about you."
        scene 35_s30 with dissolve
        r "Goddamn it... *sigh* Fine, I'll tell her we had a lovely little chat. Now leave. Please."
        scene 35_s31 with dissolve
        call screen scene35_choice02 with dissolve
    else:
        scene 35_s22 with dissolve
        r "*sigh* What do you want? If this is about the cat, Maia already apologized."
        scene 35_s21 with dissolve
        mc "I... came to talk."
        scene 35_s22 with dissolve
        r "Talk? What the hell can we possibly talk about?"
        scene 35_s30 with dissolve
        r "Wait—was this her idea? Did she put you up to this?"
        scene 35_s31 with dissolve
        mc "...Yeah. She thought it would be good if we talked. She's worried about you."
        scene 35_s30 with dissolve
        r "Goddamn it... *sigh* Fine, I'll tell her we had a lovely little chat. Now leave. Please."
        scene 35_s31 with dissolve
        call screen scene35_choice02 with dissolve

label scene35_choice02_op2:
    $ mc_reb_works_for_me = True
    mc "Works for me."
    jump free_roam_main_label

label scene35_choice02_op1:
    mc "Hold on, Rebecca. I actually do want to talk to you."
    mc "Not because the Queen asked. Because I'm tired of you looking at me like I'm an enemy..."
    scene 35_s30 with dissolve
    r "You're still on about that? I told you I'll handle it. Go!"
    scene 35_s31 with dissolve
    impulse "Spoiled brat."
    scene 35_s21 with dissolve
    mc "Can you at least listen to what I have to say?"
    r "..."
    mc "I want you to see me as someone you can rely on. Someone who's not trying to use you or marry you or manipulate you."
    r "..."
    mc "I really want to get to know you, Rebecca. The real you."
    scene 35_s28 with dissolve
    r "*scoffs* You sound so damn earnest. Do you say that to every girl who crosses your path?"  
    scene 35_s29 with dissolve
    mc "..."
    scene 35_s28 with dissolve
    r "*chuckles* Tch... You really don't give up, do you? Fine, then prove it." 
    scene 35_s29 with dissolve
    mc "Prove it?" 
    scene 35_s22 with dissolve
    r "Kiss my foot."  
    scene 35_s21 with dissolve
    mc "...What? I don't think I heard you correctly."  
    scene 35_s22 with dissolve
    r "On your knees. Kiss my foot and maybe I'll believe you."
    scene 35_s21 with dissolve
    mc "Are you serious?"  
    scene 35_s28 with dissolve
    r "Dead serious." 
    scene 35_s21 with dissolve
    mc "I fail to see how kissing your foot would—"
    scene 35_s28 with dissolve
    r "Will you do it or not?"
    scene 35_s21 with dissolve
    call screen scene35_choice03 with dissolve

default mc_kissed_reb_foot = False
label scene35_choice03_op1:
    $ mc_reb_works_for_me = False
    $ mc_kissed_reb_foot = True
    $ mc_friend_reb = True
    mc "Fine. If this is what it takes."
    scene black with Fade(0.5,0.5,0.5)
    mc "..."
    scene 35_s32 with fade
    perception "You kneel down, grip her shoe, and carefully take it off. She watches you with a smile."
    scene 35_s33 with fade
    r "*gasp!*"
    r "You... you did it!"
    scene 35_s35 with dissolve
    mc "Yeah? You asked me to."
    scene 35_s34 with dissolve
    r "Hahahaha! You actually did it! What the hell is wrong with you?! Do you not have any shame?"
    scene 35_s35 with dissolve
    empathy "She's clearly having a grand time with this, her laughter ringing out with a mix of disbelief and amusement."
    call screen scene35_choice04 with dissolve

label scene35_choice04_op1:
    scene 35_s36 with vpunch
    r "Ah! Hey! What the hell?!"
    sensation "Your tongue runs along the curve of her sole. It feels incredibly smooth under your touch, the skin soft and flawless. Her scent, a faint mix of soap and something uniquely her, fills your senses."
    scene 35_s37 with dissolve
    r "That tickles! Hahaha!"
    r "Here, feet boy. Suck on it. Since you're so eager."
    scene 35_s38 with dissolve
    sensation "You waste no time shoving her toes into your mouth, your tongue eagerly working its way between them. A strange, almost primal satisfaction washes over you, the act both humiliating and oddly thrilling."
    scene 35_s39 with dissolve
    r "Alright, that's enough. You've made your point."
    scene 35_s29 with Fade(0.5,0.5,0.5)
    perception "You stand up. She picks up her book immediately after, barely suppressing a smirk, as if you were just a brief distraction before returning to something more important."
    scene 35_s28 with dissolve
    r "That was fun. Did {i}you{/i} have fun, feet boy?"
    scene 35_s29 with dissolve
    mc "Why are you saying that? 'Feet boy'? Really?"
    scene 35_s28 with dissolve
    r "I mean, someone here is apparently obsessed with my feet."
    scene 35_s29 with dissolve
    mc "That's... I was just... being thorough."
    scene 35_s28 with dissolve
    r "Aww~ Is your shame finally catching up?"
    r "But seriously, that was something."
    scene 35_s29 with dissolve
    mc "So... are we good now?"
    scene 35_s28 with dissolve
    r "Good? Well... maybe."
    scene 35_s29 with dissolve
    mc "Alright! Progress! I'll start visiting you from now on!"
    scene 35_s22 with dissolve
    r "Huh?! Why?"
    scene 35_s21 with dissolve
    mc "Because I want to spend more time with you, duh."
    scene 35_s22 with dissolve
    r "...Whatever. Do what you want. You made it clear that I can't stop you."
    scene 35_s21 with dissolve
    mc "See you, Rebecca!"
    r "..."
    jump free_roam_main_label

label scene35_choice04_op2:
    scene 35_s29 with Fade(0.5,0.5,0.5)
    perception "You stand up. She picks up her book immediately after, barely suppressing a smirk, as if you were just a brief distraction before returning to something more important."
    mc "It was just a kiss..."
    scene 35_s28 with dissolve
    r "Just a kiss? Sure, keep telling yourself that."
    scene 35_s29 with dissolve
    mc "*sigh* So... are we good now?"
    scene 35_s28 with dissolve
    r "Good? Well... maybe."
    scene 35_s29 with dissolve
    mc "Alright! Progress! I'll start visiting you from now on!"
    scene 35_s22 with dissolve
    r "Huh?! Why?"
    scene 35_s21 with dissolve
    mc "Because I want to spend more time with you, duh."
    scene 35_s22 with dissolve
    r "...Whatever. Do what you want. You made it clear that I can't stop you."
    scene 35_s21 with dissolve
    mc "See you, Rebecca!"
    r "..."
    jump free_roam_main_label

label scene35_choice03_op2:
    $ mc_reb_works_for_me = False
    $ mc_friend_reb = True
    $ mc_refused_reb_feet = True
    mc "I'm not gonna do that."  
    scene 35_s22 with dissolve
    r "Fine. Then leave."  
    scene 35_s21 with dissolve
    mc "Come on! Is there literally {i}anything{/i} else I can do?"  
    r "..."  
    scene 35_s22 with dissolve
    r "*sigh* You really don't give up, do you?"  
    scene 35_s21 with dissolve
    mc "Never. Not until you finally accept me."  
    scene 35_s22 with dissolve
    r "Alright, fine. We're... friends. Happy now?"  
    scene 35_s21 with dissolve
    mc "Yup! You just made my day, Becky."
    scene 35_s22 with dissolve
    r "Becky? Don't ever call me that again." 
    scene 35_s21 with dissolve
    mc "Why not? It sounds cute." 
    scene 35_s22 with dissolve 
    r "...Just don't. It's... not appropriate."  
    scene 35_s21 with dissolve
    mc "Sorry, Becky. But I don't think I will."  
    scene 35_s22 with dissolve
    r "Ugh... You're insufferable... I regret this already." 
    scene 35_s21 with dissolve 
    mc "Heh. Well, I won't annoy you any further. Bye, Becky."  
    r "..."
    jump free_roam_main_label


default in_scene35_2 = False
default in_scene35_2_timer = 3
label scene35_part2:
    $ in_scene35 = False
    $ in_scene35_2 = True
    scene 21_s1 with Fade(1.5,0.5,1.5)
    play music "guild.mp3" fadein 2.0 loop
    mc "Eireen, the Queen asked me to talk to you."
    scene 21_s2 with dissolve
    eireen "Mhm. Listen up."
    eireen "About a week ago, lord Reiner got his daughter kidnapped by bandits while they were riding in the forest nearby. You may have heard about it."
    scene 21_s1 with dissolve
    mc "Bandits. Classic."
    scene 21_s5 with dissolve
    eireen "..."
    mc "Go on..."
    scene 21_s3 with dissolve
    eireen "Anyway... strange thing is, they didn't take any coin. Just her. Left her father with a nasty gash on his cranium, though."
    eireen "We sent out scouts, but they came back with nothing. Not a trace."
    scene 21_s1 with dissolve
    mc "Weird. No ransom demand?"
    scene 21_s2 with dissolve
    eireen "None so far. Which makes us think it wasn't a standard kidnapping. Someone took her for a reason, and that reason wasn't coin."
    scene 21_s1 with dissolve
    mc "So where do I come in?"
    scene 21_s2 with dissolve
    eireen "You're going to find her. Lord Reiner isn't the kind of man you want to disappoint."
    scene 21_s1 with dissolve
    mc "If he's that important then why aren't more people looking for her? Why give it to the new guy?"
    scene 21_s2 with dissolve
    eireen "There are. You're not the only one looking. Half the guards in the city have been assigned to the search."
    eireen "However, if you manage to find her yourself, you'll get the majority of the reward."
    scene 21_s1 with dissolve
    mc "Any leads at least?"
    scene 21_s9 with dissolve
    eireen "Well... no one wants to say it outright, but some folks think she went to see the Queen of Pleasure."
    scene 21_s4 with vpunch
    mc "Queen of Pleasure?! That's... that's a real title?"
    scene 21_s10 with dissolve
    eireen "Shhhhh!"
    mc "..."
    scene 21_s3 with dissolve
    eireen "But yes... The girl was... let's just say, not your typical noble's daughter. She prefered to stay in the dark."
    eireen "As a matter of fact, it's only recently that we learned he had a daughter."
    scene 21_s4 with dissolve
    mc "Ahuh... So, where do I find this... Queen? And what exactly does she do?"
    scene 21_s2 with dissolve
    eireen "Hold on, I have a map of the place somewhere here."
    scene 21_s11 with dissolve
    eireen "Or was it here?"
    scene 21_s12 with dissolve
    eireen "No, not this one..."
    eireen "There you are!"
    scene 21_s13 with dissolve
    eireen "Here. The location is already marked. It's an estate close to our southeastern border. It's a much longer trip than the one to the witch."
    scene 21_s8 with dissolve
    mc "Got it. Is there anything I should be worried about?"
    scene 21_s2 with dissolve
    eireen "Not really. The Queen of pleasure isn't hostile. She's a businesswoman, first and foremost."
    eireen "Your job's simple. Go there, ask questions, and find out what she knows. If she's involved, bring the girl back. Alive."
    scene 21_s1 with dissolve
    mc "Bring her alive. Got it."
    scene 21_s7 with dissolve
    eireen "That's all. Try not to get yourself injured, [mc]."  
    eireen "This task might take longer, but it shouldn't be as dangerous as your hunt for the witch was. Regardless, always proceed with caution."
    scene 21_s1 with dissolve
    mc "Longer? The witch hunt almost took me two days."
    mc "Do I have to leave right now? Can I at least say goodbye to a few people first?"
    scene 21_s2 with dissolve
    eireen "If you want to earn the wrath of Lord Reiner, then by all means."
    eireen "Not to mention that this task is of utmost importance to Her Majesty."
    scene 21_s1 with dissolve
    mc "..."
    scene 21_s6 with dissolve
    eireen "*sigh* Oh, don't look at me like that... Fine. Take three days. Prepare yourself if you want."
    scene 21_s5 with dissolve
    mc "I didn't think you cared about me that much."  
    scene 21_s7 with dissolve
    eireen "I care about everyone here. I wouldn't be able to sleep at night knowing I sent someone to their death."  
    eireen "Take three days to rest and prepare yourself... unless, of course, you think you're ready right now?"
    scene 21_s8 with dissolve
    call screen scene35_choice05 with dissolve

label scene35_choice05_op2:
    mc "I'll take some time first."
    scene 21_s2 with dissolve
    eireen "Alright, I'll postpone your assignment."
    scene 21_s1 with dissolve
    jump free_roam_main_label

label scene35_choice05_op1:
    mc "I'll go now. I'm ready."
    scene 21_s2 with dissolve
    stop music fadeout 2.0
    eireen "I see. This quest shouldn't be as dangerous as the witch's, but still. Take care."
    scene 21_s1 with dissolve
    jump scene35_fin

label scene35_fin:
    play music "river.mp3" fadein 2.0 loop
    scene 35_s40 with Fade(2.0,1.0,1.0)
    mc "A river? Why don't we take a little rest, [horse]?"
    scene 35_s41 with Fade(0.5,0.5,0.5)
    mc "*sigh*"
    call screen scene35_choice06 with dissolve

label scene35_choice06_op1:
    logic "You dig deep into your memories, but nothing comes up. It's like your last moments in the previous world has been wiped clean."
    empathy "Maybe it's best not to think about it."

label scene35_choice06_op2:
    mc "Had enough, [horse]? Come on, let's go."
    scene 35_s42 with fade
    play sound "sound_effects/watersplash.mp3" 
    "*splash* *splash*"
    scene 35_s43 with dissolve
    mc "Hmm?"
    scene 35_s44 with dissolve
    ""
    play sound "sound_effects/watersplash.mp3" 
    scene 35_s45 with dissolve
    mc "What the fuck is that!?"
    scene 35_s46 with vpunch
    mc "[horse]! No! Get back here!"
    mc "Goddamnit! Easy quest, my ass!"
    scene 35_s47 with dissolve
    play music "battle02.mp3" fadein 2.0 loop
    mc "Hah! Hahh!"
    scene 35_s48 with dissolve
    ""
    scene 35_s49 with dissolve
    mc "Hahh! Hah! Fuck!"
    scene 35_s50 with dissolve
    ""
    scene 35_s52 with dissolve
    mc "Goddamnit!"
    scene 35_s51 with dissolve
    ""
    scene 35_s52
    ""
    scene 35_s51
    ""
    play sound "sound_effects/bodydrop.mp3" 
    scene 35_s53 with vpunch
    alex_ "Ah!"
    scene 35_s54 with dissolve
    alex_ "What the—"
    alex_ "Hey! Watch where you're going!"
    mc "I could say the same to you!"
    mc "Wait—no time for that! I need help! There a weird thing chasing me!"
    scene 35_s55 with dissolve
    alex_ "A kelpyre? Can you fight?"
    mc "I have a dagger... but my sword is on my horse! She ran off when that thing showed up!"
    alex_ "Shit... Fine. Just stay back."
    scene 35_s56 with dissolve
    ""
    play sound "sound_effects/unsheathe2.mp3" 
    scene 35_s57 with dissolve
    ""
    scene 36_s1 with dissolve
    alex_ "Step back, it's gonna lunge."
    mc "Got it!"
    scene 36_s2 with dissolve
    ""
    play sound "sound_effects/slash03.mp3" 
    scene 36_s3 with vpunch
    ""
    play sound "sound_effects/bodydrop_grass.mp3" 
    scene 36_s4 with dissolve
    mc "...Wow."
    stop music fadeout 2.0
    alex_ "Did it get you with its claws? The scratches can fester."
    play music "river.mp3" fadein 1.0 loop
    mc "I'm fine. And damn—nice work! I've never seen anyone move that fast."
    scene 36_s5 with dissolve
    alex_ "Thanks. They're not very strong, more frightening than dangerous. It was probably chasing your horse, not you."
    scene 36_s6 with dissolve
    mc "Really?"
    scene 36_s5 with dissolve
    alex_ "They usually go after horses or other animals. Rarely attack humans unless they're desperate."
    scene 36_s6 with dissolve
    mc "I see... *sigh* Where did you go, [horse]... I hope she's okay."
    scene 36_s5 with dissolve
    alex_ "So... what are you doing out here? Did you get separated from your group?"
    scene 36_s6 with dissolve
    mc "No. I was on my way to—"
    mc "Wait. Maybe I shouldn't tell you this. Confidential information and all."
    scene 36_s5 with dissolve
    alex_ "Confi... what?"
    scene 36_s6 with dissolve
    mc "Forget it. Look, you saved my life, so... I was heading to meet this Queen of pleasure. She—"
    scene 36_s5 with dissolve
    alex_ "Queen of pleasure?!"
    scene 36_s6 with dissolve
    mc "Yeah, crazy name, right?"
    scene 36_s5 with dissolve
    alex_ "No, that's not what I meant. I was going to meet her too."
    scene 36_s6 with dissolve
    mc "Really? Well... what are the odds, huh?"
    scene 36_s9 with dissolve
    alex_ "You're not one of her followers, are you? Because if you're—"
    scene 36_s10 with dissolve
    mc "Whoa! Calm down. I don't even know anything about her."
    mc "I was just tasked with finding a girl. Supposedly, she fled there. Or was taken there."
    alex_ "..."
    scene 36_s6 with dissolve
    mc "..."
    mc "...Wanna travel together? I mean, at least until I find my horse."
    scene 36_s5 with dissolve
    alex_ "I... don't usually travel with others."
    scene 36_s8 with dissolve
    mc "Why not? Nothing wrong with a little company."
    scene 36_s7 with dissolve
    alex_ "I just don't."
    scene 36_s8 with dissolve
    mc "Okay, okay, fair enough. But still, there's strength in numbers, right?"
    alex_ "..."
    mc "Look, I won't slow you down. And once I find my horse, we can part ways if you want. No hard feelings. You go your way, I go mine."
    alex_ "..."
    scene 36_s7 with dissolve
    alex_ "Fine. But don't get too close to me. I'm not here to make friends."
    scene 36_s8 with dissolve
    mc "Uh... Alright?"
    scene 36_s5 with dissolve
    alex_ "The road ahead is long. We'll want to reach the tree line before dark."
    scene 36_s6 with dissolve
    mc "Wait, you're traveling on foot?"
    alex_ "Mhm."
    mc "No offense, but your horse didn't run away too, did it?"
    scene 36_s11 with dissolve
    stop music fadeout 2.0
    alex_ "Do ever stop talking?"
    mc "Sorry..."
    play music "2_opening_ride.mp3" fadein 1.0 loop
    scene 36_s12 with Fade(1.0,1.0,1.0)
    mc "I'm [mc]. What about you?"
    alex "Alex."
    mc "Good to meet you. I don't wanna sound weird, but I feel a lot safer with you around."
    mc "You took down that monster like it was nothing."
    alex "...Thanks?"
    alex "*ahem*"
    mc "Right, sorry. Personal space."
    scene 36_s15 with Fade(1.0,1.0,1.0)
    mc "Hey, should we have looted that... uh... water monster? It might have dropped something valuable."
    alex "Looted?"
    mc "You know, it might have dropped something interesting."
    alex "Dropped something? Oh, I see what you mean. Don't bother. Kelpyries aren't worth the trouble. Their meat's tough and bitter, and their hide's too rough to make anything useful."
    alex "The teeth, though... you could sell those. But you'll need to find a collector if you're serious about it."
    mc "Nevermind."
    scene 36_s16 with dissolve
    alex "We should make camp. We'll continue tomorrow."
    scene 36_s17 with dissolve
    mc "Hah... yeah... good... hahh... idea..."
    scene 36_s16 with dissolve
    alex "I'm gonna gather some firewood."
    scene 36_s17 with dissolve
    mc "I'll help."
    scene 36_s16 with dissolve
    alex "Also, do you have a tent? Bedroll? Supplies? You seem... unprepared."
    scene 36_s17 with dissolve
    mc "Shit... All my things were on [horse]... Everything. She's just out there somewhere, carrying my entire life."
    scene 36_s16 with dissolve
    alex "I have a spare roll."
    scene 36_s17 with dissolve
    mc "Dependable as always, Alex!"
    stop music fadeout 2.0
    alex "..."
    scene 36_s18 with Fade(1.0,1.0,1.0)
    play music "night_fire.mp3" fadein 1.0 loop
    mc "...Cool swords."
    scene 36_s19 with dissolve
    alex "Thanks."
    scene 36_s18 with dissolve
    mc "..."
    call screen scene36_choice01 with dissolve


label scene36_choice01_op1:
    if not scene36_choice1_continue:
        $ scene36_choice1_continue = True
    mc "You said you don't travel with others. Why's that? If you don't mind me asking."
    scene 36_s19 with dissolve
    alex "I just do. It's simpler."
    scene 36_s18 with dissolve
    mc "Fair enough. I won't pry, but I'm glad you made an exception for me. Even if it's just temporary."
    call screen scene36_choice01 with dissolve

label scene36_choice01_op2:
    if not scene36_choice1_continue:
        $ scene36_choice1_continue = True
    mc "Where are you from? Your accent is different from the people in Irda."
    scene 36_s19 with dissolve
    alex "Eurina. The kingdom to the west."
    scene 36_s18 with dissolve
    mc "Eurina? I saw it on my map, place looks pretty far. What's it like?"
    scene 36_s20 with dissolve
    alex "It's fine for the most part. Colder than here."
    alex "Way more stable than Irda. Politically. It's... orderly."
    mc "Sounds almost boring. No offense."
    scene 36_s18 with dissolve
    call screen scene36_choice01 with dissolve

label scene36_choice01_op3:
    if not scene36_choice1_continue:
        $ scene36_choice1_continue = True
    mc "Why are you heading to the Queen of Pleasure? Were you assigned the same task?"
    scene 36_s19 with dissolve
    alex "Task? No. I wasn't assigned anything. I don't work for your guild."
    alex "I... I just need something from her."
    scene 36_s18 with dissolve
    mc "Something?"
    scene 36_s19 with dissolve
    alex "Yes."
    scene 36_s18 with dissolve
    mc "...Not much of a talker, are you?"
    call screen scene36_choice01 with dissolve

label scene36_continue:
    mc "*yawn* I'm gonna get some sleep. What about you?"
    scene 36_s19 with dissolve
    alex "I'll... I need to take a leak first."
    scene 36_s18 with dissolve
    mc "Alright. Be careful."
    scene 36_s21 with Fade(1.0,1.0,1.0)
    perception "The night sky is filled with stars—a stark contrast to the city's sky. Strange constellations stretch across the dark, alien and unfamiliar."
    mc "(Wait... what city was that? I can almost see it... towers... lights... but it's gone. Just out of reach. Like everything else.)"
    play sound "sound_effects/grass.mp3" fadein 0.1
    "*rustle* *rustle*"
    scene 36_s22 with dissolve
    mc "Huh?"
    play sound "sound_effects/grass.mp3" fadein 0.1
    "*rustle* *rustle*"
    mc "Alex? Something wrong?"
    stop music fadeout 1.0
    scene 36_s23 with Fade(1.0,1.0,1.0)
    play music "night.mp3" fadein 1.0 loop
    alex "Uhh... Ah~... Shit!"
    mc "(What the hell is going on? Did she get attacked?)"
    scene 36_s24 with dissolve
    alex "Ahh~ Hah~ .... God..."
    mc "(Is she...?)"
    play sound "sound_effects/twig.mp3" fadein 0.1
    scene 36_s25 with dissolve
    mc "(Shit!)"
    scene 36_s26 with dissolve
    alex "Huh? Is someone there?"
    scene 36_s27 with dissolve
    alex "[mc]?! What the hell—!"
    mc "(Oh, fuck.)"
    mc "(Wait... what's that mark?!)"
    call screen scene36_choice02 with dissolve

label scene36_choice02_op1:
    $ persistent.alex_p = True
    $ persistent.alex_d = False
    scene 36_s28 with dissolve
    mc "A-Alex? What is that mark on your abdomen?"
    scene 36_s38 with dissolve
    alex "The hell are you staring for?! Go! Get out of here! NOW!"
    scene 36_s28 with dissolve
    mc "Sorry! I thought you were injured!"
    stop music fadeout 1.0
    jump scene36_continue2

label scene36_choice02_op2:
    $ persistent.alex_p = False
    $ persistent.alex_d = True
    scene 36_s29 with dissolve
    mc "A-Alex? Is that a...? You're a...?"
    scene 36_s30 with dissolve
    alex "The hell are you staring for?! Go! Get out of here! NOW!"
    scene 36_s29 with dissolve
    mc "Sorry! I thought you were injured!"
    stop music fadeout 1.0
    jump scene36_continue2

label scene36_continue2:
    scene 36_s31 with Fade(1.0,1.0,1.0)
    play music "night_fire.mp3" fadein 1.0 loop
    env "The cold air is thick with the scent of damp earth. The trees sway gently beneath the silver glow of the moon. The flame of the makeshift fire is slowly fading."
    scene 36_s32 with dissolve
    alex "..."
    mc "..."
    if persistent.alex_p:
        mc "Uh... I saw something weird on your body... A mark. It didn't look like a tattoo."
        alex "..."
        mc "You don't wanna talk about it?"
        alex "*sigh* It's the reason..."
        mc "Hmm? What do you mean?"
        alex "It's the reason I'm out here. The reason I'm heading to that Queen."
        alex "She cast this spell... or curse, more like."
        alex "She did something to me, and now I can't... I can't control..."
        mc "Curse? Why would she do that?"
        alex "Long story. It doesn't matter. What matters is I want her to remove it."
        mc "What does the curse do?"
        alex "You saw, didn't you? That mark..."
        alex "It makes me lose control my body. Especially when I see... men. The mark flares up, and suddenly I'm not myself anymore."
        mc "I get it. You don't have to explain."
        alex "Mhmm... I'm gonna sleep."
        alex "Please forget you saw anything."
        empathy "She sounds tired. Not just physically—something in her voice feels... heavy."
        mc "Alright. Good night."
    if persistent.alex_d:
        mc "Uh... Alex... You're a... guy?"
        alex "..."
        mc "You don't wanna talk about it?"
        alex "*sigh* It's the reason..."
        mc "Hmm? What do you mean?"
        alex "It's the reason I'm out here. The reason I'm heading to that Queen."
        alex "She did this to me. It's a spell... or a curse, more like."
        alex "She twisted my body. Changed it. Made it... wrong."
        mc "Curse? Why would she do that?"
        alex "Long story. It doesn't matter. What matters is I want her to remove it."
        mc "What does the curse do?"
        alex "You saw, didn't you? That mark... It makes me..."
        alex "I can't control my body. Especially when I see... men or women. The mark flares up, and suddenly I'm not myself anymore."
        mc "I get it. You don't have to explain."
        alex "Mhmm... I'm gonna sleep."
        alex "Please forget you saw anything."
        empathy "She sounds tired. Not just physically—something in her voice feels... heavy."
        mc "Alright. Good night."

    scene 36_s33 with Fade(1.0,1.0,1.0)
    mc "(What the hell am I doing here?)"
    scene 36_s34 with dissolve
    ""
    scene black with Fade(1.0,1.0,1.0)
    alex "Ahh~ Hah~..."
    scene 36_s34 with dissolve
    ""
    scene 36_s35 with dissolve
    mc "(She's still at it... Guess I didn't let her finish.)"
    mc "(I'm just going to lie here and pretend I'm deaf...)"
    call screen scene36_choice03 with dissolve

label scene36_choice03_op1:
    scene 36_s39 with dissolve
    mc "..."

label scene36_continue3:
    scene 36_s37 with Fade(1.0,1.0,1.0)
    alex "Hah! Ahhh~ Nghnn~"
    scene 36_s36 with dissolve
    mc "(For fuck's sake... How am I supposed to sleep like this?!)"
    scene 36_s35 with dissolve
    perception "Her body shudders with each moan. At this point, you're more annoyed than aroused."
    scene 36_s33 with Fade(1.0,1.0,1.0)
    alex "..."
    mc "(Is it finally over? Please let it be over.)"
    mc "*sigh*"
    scene 36_s37 with Dissolve(1.5)
    ""

image 37_alex_sex1 = Movie(play="images/3_chapter2/scene37/37_alex_sex1.webm", loop=True)
image 37_alex_sex1_faster = Movie(play="images/3_chapter2/scene37/37_alex_sex1_faster.webm", loop=True)
image 37_alex_sex2 = Movie(play="images/3_chapter2/scene37/37_alex_sex2.webm", loop=True)
image 37_alex_sex2_faster = Movie(play="images/3_chapter2/scene37/37_alex_sex2_faster.webm", loop=True)
image 37_alex_sex3d = Movie(play="images/3_chapter2/scene37/37_alex_sex3d.webm", loop=True)
image 37_alex_sex3d_faster = Movie(play="images/3_chapter2/scene37/37_alex_sex3d_faster.webm", loop=True)
image 37_alex_sex3p = Movie(play="images/3_chapter2/scene37/37_alex_sex3p.webm", loop=True)
image 37_alex_sex3p_faster = Movie(play="images/3_chapter2/scene37/37_alex_sex3p_faster.webm", loop=True)

image 37_alex_feet1 = Movie(play="images/3_chapter2/scene37/37_alex_feet1.webm", loop=True)
image 37_alex_feet2 = Movie(play="images/3_chapter2/scene37/37_alex_feet2.webm", loop=True)
image 37_alex_feet2_faster = Movie(play="images/3_chapter2/scene37/37_alex_feet2_faster.webm", loop=True)
image 37_alex_feet3 = Movie(play="images/3_chapter2/scene37/37_alex_feet3.webm", loop=True)
image 37_alex_feet3_faster = Movie(play="images/3_chapter2/scene37/37_alex_feet3_faster.webm", loop=True)

label scene37:
    stop music
    play music "MorningSun.mp3" loop
    scene 37_s1
    ""
    scene 37_s2 with dissolve
    ""
    scene 37_s3 with dissolve
    ""
    scene 37_s4 with dissolve
    ""
    scene 37_s5 with dissolve
    tv "You spill your soul into the sea long enough, and it forgets yer name."
    tv "He said he'd keep the light. But the storm took him instead."
    tv "Some men chase truth and find madness instead."
    alex "You're still watching this?"
    mc "Hey, it's a classic. It's comforting."
    scene 37_s7 with dissolve
    alex "Comforting? It's about two guys who went insane."
    alex "Anyway, dinner's your turn tonight."
    scene 37_s6 with dissolve
    mc "Fine, fine. What are we making?"
    scene 37_s7 with dissolve
    alex "Anything. I'm starving."
    alex "Imma take a shower."
    scene 37_s6 with dissolve
    mc "Yeah, you smell like shit."
    scene 37_s7 with dissolve
    alex "*laughs* screw you."
    play music "wind2.mp3" fadein 1.0 loop
    scene 37_s8 with Dissolve(1.0)
    ""
    scene 37_s9 with dissolve
    mc "Huh? Ah man... I really need to fix my sleep schedule."
    mc "*yawn* Alex? You back?"
    scene 37_s10 with Fade(0.5,0.5,0.5)
    mc "Sorry for not making anything today... I fell asleep. I'll make it up to you tomorrow."
    mc "(Hmm, What's that noise coming from?)"
    scene 37_s11 with dissolve
    mc "(Oh. You forgot to turn off the music, dummy.)"
    if not interact_indicator:
        $ interact_indicator = True
        call screen interact_tutorial with Dissolve(0.3)
    call screen scene37_phone with dissolve
    scene 37_s12 with dissolve
    mc "(You're welcome.)"
    scene 37_s13 with dissolve
    mc "(Alright, now what the hell do i do?)"
    stop music fadeout 2.0
    call screen scene37_choice01 with dissolve
    scene 37_s14 with Fade(1.0,1.0,1.0)
    play music "MorningSun.mp3" fadein 1.0 loop
    tv "In other news, a coastal couple has gone missing after weeks of isolation in their lighthouse residence. Authorities suspect exposure and deteriorating mental health."
    tv "Experts warn that prolonged isolation can lead to erratic behavior and emotional breakdowns."
    play sound "sound_effects/dooropen.mp3" fadein 0.1
    "*thud*"
    scene 37_s15 with dissolve
    mc "Alex? That you?"
    scene 37_s16 with Dissolve(1.5)
    mc "How'd it go?"
    scene 37_s17 with dissolve
    alex "They didn't even look at me... Just brushed me off."
    scene 37_s56 with dissolve
    alex "I tried so hard... I stayed up all night preparing."
    scene 37_s18 with dissolve
    mc "I know you did. You worked your ass off. They're just idiots for not seeing it."
    scene 37_s56 with dissolve
    alex "*sniff* What am I even doing? What are we even doing?"
    scene 37_s18 with dissolve
    mc "*sigh* Come here."
    scene 37_s19 with dissolve
    alex "Fuck this... I'm drinking a full bottle tonight."
    stop music fadeout 3.0
    mc "Already got you covered."
    scene 37_s20 with Fade(1.0,1.0,1.0)
    play music "sex01.mp3" fadein 2.0 volume 0.2 loop
    tv "No chat! I'm not gonna eat a cockroach!"
    tv "...Okay fine, I'll do it!"
    alex "I don't get why you keep watching this *hic* idiot... Isn't he like ninety now?"
    mc "He's funny. Kinda reminds me of—"
    scene 37_s21 with dissolve
    alex "You know what would be even funnier?"
    scene 37_s22 with dissolve
    mc "...What?"
    scene 37_s21 with dissolve
    alex "If you *hic* pinned me down and fucked my hole..."
    scene 37_s22 with dissolve
    mc "..."
    alex "..."

label scene37_alex_sex:
    $ mcname = persistent.name
    if persistent.name == "None" or mcname == "None":
        while mcname == "None" or mcname == "":
            $ mcname = renpy.input("There was an issue with your name. Please rewrite your name:", length=32)
        $ persistent.name = mcname
    if not persistent.scene1_p4_replay:
        $ persistent.scene1_p4_replay = True
    show 37_alex_sex1 with dissolve
    alex "*gasp* Fuck... ahh~ yesss..."
    alex "You have no idea... hahh~ how long I've wanted this..."
    alex "I've been... hnn~ thinking about it all day."
    scene black with Dissolve(0.3)
    show 37_alex_sex2 with dissolve
    alex "Don't stop. Please... just—don't stop~"
    mc "Nngh... Alex—"
    alex "Yes... just like that~"
    call screen scene37_choice02 with dissolve

label scene37_sex1:
    $ alex_sex_speed_toggle_37 = False
    $ scene37_sex1 = True
    $ scene37_sex2 = False
    scene black with Dissolve(0.3)
    show 37_alex_sex1 with dissolve
    alex "You like how tight it is, hmmm~?"
    call screen scene37_choice02 with dissolve

label scene37_sex2:
    $ alex_sex_speed_toggle_37 = False
    $ scene37_sex1 = False
    $ scene37_sex2 = True
    scene black with Dissolve(0.3)
    show 37_alex_sex2 with dissolve
    alex "Hnn~ Ahh!"
    call screen scene37_choice02 with dissolve

label scene37_choice02_faster:
    scene black with Dissolve(0.3)
    $ alex_sex_speed_toggle_37 = True
    if scene37_sex1:
        show 37_alex_sex1_faster with dissolve
        hide 37_alex_sex1
        alex "Yes! Yes! Yes~"
    else:
        show 37_alex_sex2_faster with dissolve
        hide 37_alex_sex2
        alex "Ahhh~ It's soo fuckinggg big!"
    call screen scene37_choice02 with dissolve

label scene37_choice02_slower:
    scene black with Dissolve(0.3)
    $ alex_sex_speed_toggle_37 = False
    if scene37_sex1:
        show 37_alex_sex1 with dissolve
        hide 37_alex_sex1_faster
    else:
        show 37_alex_sex2 with dissolve
        hide 37_alex_sex2_faster
    alex "Hnnggg~... Stop teasing me~"
    call screen scene37_choice02 with dissolve

label scene37_alex_cum1:
    mc "Ngh!"
    mc "I... I can't last much longer—"
    if persistent.alex_p:
        alex "Then cum. I want it. I want all of you."
        mc "I'm not wearing a condom—"
        alex "Just do it! I want your baby in my womb! Ahh~ Fill me up!"
        mc "Y-Your drunk... I... {i}We{/i} can't have a baby living like this..."
        alex "Fine! Then finish in my ass—just don't stop!"
        scene black with Dissolve(1.0)
        show 37_alex_sex3p with dissolve
    else:
        alex "No! Not yet!"
        alex "Fuck me harder! Fill my ass, just don't stop—please!"
        scene black with Dissolve(1.0)
        show 37_alex_sex3d with dissolve
        alex "Hah! I'm close! You're gonna make me cum from my ass!"
    call screen scene37_choice03 with dissolve

label scene37_choice03_faster:
    $ alex_sex_speed_toggle_37_2 = True
    scene black with Dissolve(0.3)
    if persistent.alex_p:
        show 37_alex_sex3p_faster with dissolve
        hide 37_alex_sex3p
    else:
        show 37_alex_sex3d_faster with dissolve
        hide 37_alex_sex3d
    alex "Haaaahhh!! Break me! Ruin me! Hnngh~"
    alex "Fill this tight little ass, baby~"    
    call screen scene37_choice03 with dissolve

label scene37_choice03_slower:
    $ alex_sex_speed_toggle_37_2 = False
    scene black with Dissolve(0.3)
    if persistent.alex_p:
        show 37_alex_sex3p with dissolve
        hide 37_alex_sex3p_faster
    else:
        show 37_alex_sex3d with dissolve
        hide 37_alex_sex3d_faster
    alex "Hnn~ pleeaaseee... fuck my asshole harder!"
    alex "You're hitting me so... nhnnn! deep!"
    call screen scene37_choice03 with dissolve

label scene37_alex_cum2:
    alex "I'm! I'm! I'm cumming!"
    show screen cum
    if persistent.alex_p:
        play sound "se_sfx/sex/sex_cum5.mp3" 
        scene 37_s26 with vpunch
        mc "Nghnn!"
        play sound "se_sfx/sex/sex_cum3.mp3" 
        scene 37_s27 with vpunch
        alex "Hnnnnnaa!!"
        scene 37_s28 with dissolve
        alex "Hah... Hahh..."
        alex "Hehe... fuck... It's leaking..."
        alex "I can... feel it sloshing in my tummy~"
        alex "Do you... love... ah..."
        alex "..."
        mc "Alex?"
        alex "*snore*"
        mc "Shit..."

    else:
        play sound "se_sfx/sex/sex_cum5.mp3" 
        scene 37_s23 with vpunch
        mc "Nghnn!"
        play sound "se_sfx/sex/sex_cum3.mp3" 
        scene 37_s24 with vpunch
        alex "Hnnnnnaaa!!"
        scene 37_s25 with dissolve
        alex "Hah... Hahh..."
        alex "Hehe... fuck... It's leaking..."
        alex "I can... feel it sloshing in my tummy~"
        alex "Do you... love... ah..."
        alex "..."
        mc "Alex?"
        alex "*snore*"
        mc "Shit..."
    hide screen cum
    $ renpy.end_replay()
    stop music fadeout 3.0
    call screen scene37_choice01 with dissolve
    scene 37_s29 with Fade(1.0,1.0,1.5)
    play music "river2.mp3" fadein 3.0 volume 0.5 loop
    ""
    scene 37_s30 with dissolve
    alex "You know, I used to come here as a kid. This place felt magical back then."
    scene 37_s31 with dissolve
    mc "Still kinda does... with you in it."
    scene 37_s30 with dissolve
    alex "*giggles* Ah, shut up... You're so cheesy."
    scene 37_s33 with dissolve
    ""
    scene 37_s34 with dissolve
    ""
    scene 37_s35 with dissolve
    stop music fadeout 3.0
    call screen scene37_choice01 with dissolve
    scene 37_s36 with Fade(2.0,1.0,1.0)
    play music "f_night.mp3" fadein 3.0 volume 0.3 loop
    ""
    scene 37_s37 with fade
    mc "Hey... you up for it tonight? It's been a while."
    scene 37_s39 with dissolve
    alex "Not really. Sorry, I'm just tired. The new job's been killing me."
    scene 37_s37 with dissolve
    mc "Oh... okay."
    scene 37_s38 with dissolve
    if mc_liked_feet:
        alex "...But if you really need it, you can use my feet. I know that's... something you like."
    else:
        alex "...But if you really need it, you can use my feet."
    scene 37_s40 with dissolve
    ""
    scene 37_s37 with dissolve
    mc "That's not what I want."
    scene 37_s39 with dissolve
    alex "I know."
    scene 37_s37 with dissolve
    call screen scene37_choice04 with dissolve

label scene37_choice04_op1:
    $ mcname = persistent.name
    if persistent.name == "None" or mcname == "None":
        while mcname == "None" or mcname == "":
            $ mcname = renpy.input("There was an issue with your name. Please rewrite your name:", length=32)
        $ persistent.name = mcname
    if not persistent.scene2_p4_replay:
        $ persistent.scene2_p4_replay = True
    mc "Fine. Feet it is."
    scene 37_s57 with Fade(0.5,0.5,0.5)
    mc "Did I ever tell you how soft your feet were?"
    show 37_alex_feet1 with dissolve
    alex "Mhmm..."
    mc "Seriously, they were made for this."
    alex "Ahuuh..."
    mc "...Can you help out a little?"
    alex "*sigh* Fine."
    scene 37_s41 with dissolve
    alex "Here, put your dick through."
    mc "Thanks!"
    show 37_alex_feet2 with dissolve
    alex "Just... finish on a tissue. I don't want it on my dress."
    mc "...You've been avoiding me lately. You wanna talk about it?"
    alex "Can we not do this now? My show's on."
    call screen scene37_feet with dissolve

label scene37_feet1:
    $ alex_feet_speed_toggle_37 = False
    $ scene37_feet1 = False
    $ scene37_feet2 = True
    scene black with Dissolve(0.3)
    show 37_alex_feet2 with dissolve
    alex "*yawn*"
    call screen scene37_feet with dissolve

label scene37_feet2:
    $ alex_feet_speed_toggle_37 = False
    $ scene37_feet1 = True
    $ scene37_feet2 = False
    scene black with Dissolve(0.3)
    show 37_alex_feet3 with dissolve
    call screen scene37_feet with dissolve

label scene37_feet_faster:
    $ alex_feet_speed_toggle_37 = True
    if scene37_feet1:
        show 37_alex_feet3_faster with dissolve
        hide 37_alex_feet3
        alex "Are you close?"
    else:
        show 37_alex_feet2_faster with dissolve
        hide 37_alex_feet2
        alex "My legs are getting tired. Can we finish up quick?"
    call screen scene37_feet with dissolve

label scene37_feet_slower:
    $ alex_feet_speed_toggle_37 = False
    if scene37_feet1:
        show 37_alex_feet3 with dissolve
        hide 37_alex_feet3_faster
        alex "Slower? Come on..."
    else:
        show 37_alex_feet2 with dissolve
        hide 37_alex_feet2_faster
        alex "Ugh..."
    call screen scene37_feet with dissolve

label scene37_choice04_op2:
    mc "...You've been avoiding me lately. You wanna talk about it?"
    scene 37_s39 with dissolve
    alex "Can we not do this now? My show's on."
    scene 37_s37 with dissolve
    mc "Fine."
    stop music fadeout 3.0
    call screen scene37_choice01 with dissolve
    jump scene37_continue

label scene37_alex_feet_cum:
    mc "I'm close!"
    alex "Then grab a—"
    show screen cum
    play sound "se_sfx/blowjob/facial1.mp3" 
    scene 37_s42 with vpunch
    mc "Nghh—agh!"
    hide screen cum
    play sound "se_sfx/blowjob/facial2.mp3" 
    scene 37_s43 with vpunch
    alex "Jesus! What the hell?!"
    scene 37_s44 with dissolve
    mc "Sorry! It just... happened!"
    alex "Fuck you..."
    mc "..."
    alex "*sigh* Sorry... Can you grab a tissue for me?"
    mc "Yeah."
    $ renpy.end_replay()
    stop music fadeout 3.0
    call screen scene37_choice01 with dissolve

label scene37_continue:
    scene 37_s45 with Fade(1.0,1.0,1.5)
    play music "MorningSun.mp3" fadein 1.0 loop
    ""
    scene 37_s46 with dissolve
    alex  "We can't keep living like this..."
    mc  "What do you mean?"
    alex "I mean this—us—barely scraping by. You haven't been working. I'm exhausted. It's like we're stuck in this hole, and every time I try to crawl out, you just... sit there."
    mc  "I didn't ask for this either. I'm trying, okay?"
    alex "I know... I know you are..."
    mc "It {i}will{/i} get better, okay?"
    alex "You've been saying that for months."
    mc "..."
    stop music fadeout 3.0
    call screen scene37_choice01 with dissolve
    scene 37_s47 with Fade(1.5,1.0,1.0)
    play music "breakup.mp3" fadein 2.0 loop
    ""
    scene 37_s48 with dissolve
    mc "So this is it?"
    alex "I need to find myself again... and I don't think I can do that here."
    mc "I still love you."
    alex "I know. That's what makes this harder."
    mc "..."
    alex "...I hope you find peace, too."
    scene 37_s58 with Dissolve(1.0)
    mc "..."
    call screen scene37_choice01 with dissolve
    scene 37_s49 with Fade(2.0,1.0,1.0)
    ""
    scene 37_s50 with dissolve
    ""
    scene 37_s51 with dissolve
    ""
    scene 37_s52 with dissolve
    call screen scene37_choice01 with dissolve
    scene 37_s53 with Fade(1.5,1.0,1.5)
    mc "I used to think this view made everything feel smaller."
    alex "And now?"
    mc "Now I just feel smaller."
    scene 37_s54 with dissolve
    alex "..."
    mc "..."
    mc "You're not... Y-You're..."
    scene 37_s55 with dissolve
    ex "What's wrong, [mc]?"
    scene black
    scene black with dissolve
    pause 0.2
    ex "How could you forget me?"
    scene 38_s1 with Fade(0.5,0.5,1.0)
    ""
    alex "Are you good?"
    scene 38_s4 with dissolve
    mc "Huh?"
    scene 38_s3 with dissolve
    alex "You were mumbling... and crying."
    scene 38_s4 with dissolve
    mc "...I'm fine. Just a dream."
    scene 38_s3 with dissolve
    alex "If you say so. Come on. Wash your face in the stream and let's move."
    scene 38_s4 with dissolve
    stop music fadeout 4.0
    mc "Just give me a minute."
    scene 38_s5 with Fade(0.5,0.5,0.5)
    ""
    scene 38_s6 with Fade(0.5,0.5,0.5)
    play sound "sound_effects/running_grass.mp3" fadein 0.1 volume 0.5
    "*rumble* *rumble*"
    mc "Do you hear that?"
    alex "Yes, and I don't like it."
    play sound "sound_effects/running_grass.mp3" fadein 0.1
    "*RUMBLE* *RUMBLE*"
    scene 38_s7 with dissolve
    alex "Watch out!"
    play music "powerup.mp3" fadein 3.0 loop
    scene 38_s8 with dissolve
    perception "A massive, fur-covered beast bursts from the trees, its eyes blazing with feral hunger."
    mc "It's fast!"
    scene 38_s9 with dissolve
    werewolf "HNAAAAAA!!!"
    play sound "sound_effects/sword_clash.mp3" fadein 0.1
    scene 38_s10 with vpunch
    alex "Ngh!"
    scene 38_s11 with dissolve
    werewolf "AGGHHHH!"
    scene 38_s12 with dissolve
    mc "Alex!"
    scene 38_s13 with dissolve
    werewolf "COPULATE! COPULATE! I MUST COPULATE!"
    scene 38_s14 with dissolve
    werewolf "*sniff* *sniff*"
    scene 38_s13 with dissolve
    werewolf "A MALE?"
    werewolf "NO MATTER. YOU WILL HAVE TO DO FOR NOW."
    scene 38_s28 with Dissolve(1.0)
    mc "*gulp* (Alright... calm down... just calm down... I'll wake up soon. This was all just a dream.)"  
    werewolf "HAHH... HAH..."
    scene 38_s29 with Dissolve(1.0)
    mc "No! This isn't right... I can't give up that easily again!"
    mc "Hah... ha... hahahahaha!"  
    scene 38_s30 with Dissolve(1.0)
    mc "Fine! You want my ass, huh?!"
    play sound "sound_effects/clothing_rustle.mp3"
    scene 38_s31 with vpunch
    mc "You're gonna have to earn it first!"
    scene 38_s32 with dissolve
    werewolf "FOOLISH HUMAN!"
    scene 38_s33 with dissolve
    perception "Left side, fast!"  
    logic "Guard. Step in, uppercut tight."
    play sound "sound_effects/punch.mp3"
    scene 38_s34 with vpunch
    werewolf "AGH!"
    scene 38_s35 with dissolve
    logic "Retract! Don't let him bite, counter left hook!"  
    play sound "sound_effects/punch2.mp3"
    scene 38_s37 with hpunch
    werewolf "RAHHHHH!"
    scene 38_s38 with dissolve
    werewolf "ENOUGH! YOU DIE NOW."
    scene 38_s39 with dissolve
    perception "High guard. Incoming overhead!"  
    logic "Close distance, smother. Grab wrist. Body shot, kidney line!"  
    scene 38_s40 with dissolve
    werewolf "IMPOSSIBLE! I AM THE ALPHA! I AM THE—"
    play sound "sound_effects/punch3.mp3"
    scene 38_s41 with vpunch
    mc "Ngh!"
    werewolf "AGHHH!"
    logic "Don't stop. Make him fold."  
    scene 38_s42 with dissolve
    werewolf "AAAHH!"
    play sound "sound_effects/punch3.mp3"
    scene 38_s41 with vpunch
    mc "WANT MORE?!"
    scene 38_s42 with dissolve
    mc "HAAAAAAAAA!"
    play sound "sound_effects/punch3.mp3"
    scene 38_s41 with vpunch
    werewolf "AGHNNN!"
    werewolf "I YEILD!"
    mc "You... what?"
    play sound "sound_effects/running_grass.mp3" fadein 0.1
    scene 38_s22 with dissolve
    mc "Hahh... ahh... Holy shit! I... I fought off a werewolf! With my bare hands!"
    mc "H-How? Fuck, my knuckles are wrecked..."  
    mc "Shit... Alex?!"
    mc "Alex! Where are you?"
    alex "I'm here!"
    stop music fadeout 3.0
    scene 38_s26 with Fade(1.0,1.0,1.0)
    mc "Are you okay?"
    play music "nature.mp3" fadein 1.0 loop
    scene 38_s25 with dissolve
    alex "I'm... ngh... fine."
    scene 38_s26 with dissolve
    mc "You don't look fine to me. You're bleeding."
    mc "I'll carry you, let's find someone who can help."
    scene 38_s25 with dissolve
    alex "Agh... I can still walk."
    alex "And... What happened back there? Did you kill that werewolf?"
    scene 38_s26 with dissolve
    mc "Don't worry about it, I fought it off. I don't know how, something just... clicked."
    mc "Let's get you somewhere safe."
    scene 38_s27 with Fade(1.0,1.0,1.0)
    mc "Look! There's a village over there."
    alex "A village? I have never seen this place before."
    mc "Maybe it's new?"
    alex "No way. These buildings look old."
    mc "Either way, we should ask for help. Come on, lean on me."
    stop music fadeout 3.0
    alex "Mhm..."
    scene 39_s1 with Fade(1.0,1.0,1.0)
    play music "market.mp3" fadein 1.0 loop
    mc "Someone's there."
    alex "Mhm... but where's everyone else? Place... ngh... feels like a tomb."
    mc "Let's just ask her."
    mc "Excuse me."
    scene 39_s2 with dissolve
    mc "We need some help. My friend here is injured and—"
    play sound "sound_effects/running_dirt.mp3"
    scene 39_s3 with vpunch
    alex "The hell is wrong with her?"
    mc "Maybe outsiders spook them."
    mc "Let's find someone else."
    scene 39_s4 with Fade(0.5,0.5,0.5)
    ""
    scene 39_s5 with dissolve
    alex "The door... ngh... It's opening."
    mc "Yeah."
    perception "An elderly couple hurries out the door, their faces lit with a warm, almost desperate kindness."
    scene 39_s6 with dissolve
    ysella_ "Welcome! Welcome! Please forgive Annette—she's not used to seeing outsiders."
    ysella "My name is Ysella, and this is my husband, Oswald. We are the elders of Halga."
    scene 39_s7 with dissolve
    oswald "It's a pleasure. We rarely receive guests."
    scene 39_s8 with dissolve
    mc "We need help, my friend is injured. A werewolf attacked us on the road."
    scene 39_s9 with dissolve
    ysella "Oh my, what happened to you, dear? A werewolf? How dreadful!"
    ysella "Go with Ymir to the lodge, she's our healer."
    scene 39_s15 with Dissolve(0.8)
    alex "Thank you..."
    scene 39_s6 with dissolve
    ysella "And what about you? You must be weary from the road. Come, let us treat you as well."
    scene 39_s8 with dissolve
    mc "Thanks, but..."
    scene 39_s11 with dissolve
    mc "Will you be fine, Alex?"
    scene 39_s10 with dissolve
    alex "Mhm. Don't take too long, alright? And get some supplies while you're at it."
    scene 39_s11 with dissolve
    mc "Got it."
    scene 39_s12 with dissolve
    ymir "Please, follow me."
    scene 39_s13 with dissolve
    alex "Don't touch me. I can walk on my own."
    scene 39_s12 with dissolve
    ymir "O-Of course... I aplogize."
    scene 39_s14 with dissolve
    mc "Calm down, Alex. How will they treat you if they can't touch you? Let the healer do her job."
    alex "..."
    mc "Bear with it, for now at least."
    mc "We're guests here. Let's not insult them before they've finished helping us."
    scene 39_s8 with dissolve
    mc "Alright, I suppose a short rest wouldn't hurt."
    scene 39_s6 with dissolve
    ysella "Wonderful! Please, follow us."
    scene 39_s16 with Fade(0.5,0.5,0.5)
    mc "What's going on here?"
    ysella "We were just having a community meeting. Everyone, you may leave. We will continue tonight."
    oswald "Please, take a seat."
    scene 39_s17 with fade
    ysella "..."
    oswald "..."
    perception "The old couple scour your body intensely, their gaze lingering on a specific part before suddenly jerking to the next."
    mc "Uh..."
    scene 39_s18 with dissolve
    oswald "Don't be shy. The harvest was generous this year."
    scene 39_s19 with dissolve
    mc "Thanks."
    scene 39_s17 with dissolve
    mc "What's this place called? I didn't see a sign on the road."
    scene 39_s20 with dissolve
    ysella "This is Halga. Our humble little home. We've been here for generations, since before the border wars."
    ysella "I must say, it's a pleasure to welcome outsiders! The goddess have smiled on us today."
    scene 39_s17 with dissolve
    mc "Appreciate the hospitality. We would be in a bad spot if you hadn't been here."
    scene 39_s20 with dissolve
    ysella "Tell me, traveler, what brings you to our quiet village? Were you seeking us out, or was it chance?"
    scene 39_s17 with dissolve
    mc "We just stumbled across it while we were looking for help."
    scene 39_s20 with dissolve
    ysella "Ah, of course. Most who find their way here do so for a reason. The Goddess guides them. She always does."
    scene 39_s17 with dissolve
    mc "What do you mean?"
    scene 39_s26 with dissolve
    oswald "The Goddess has a way of guiding those who are lost. They all find their way to Halga, sooner or later."
    scene 39_s21 with dissolve
    mc "This tastes... different."
    scene 39_s20 with dissolve
    ysella "It's special. Grown right here, under the watchful eyes of the Goddess."
    scene 39_s17 with dissolve
    mc "You keep talking about your goddess. Who is she?"
    scene 39_s26 with dissolve
    oswald "She watches over Halga and all who seek shelter within her grace. She has led you here, after all."
    scene 39_s20 with dissolve
    ysella "Even over you. Can you feel her? The warmth in the air? The peace in your heart? That is her doing."
    scene 39_s17 with dissolve
    mc "Uh-huh..."
    scene 39_s20 with dissolve
    ysella "Why don't you stay the night? Rest before continuing your journey."
    ysella "The road is dangerous after dark."
    scene 39_s17 with dissolve
    mc "I don't really have a choice, I need to wait for my friend to heal."
    scene 39_s20 with dissolve
    ysella "Wonderful! I'll have someone prepare a soft bed for you."
    ysella "In the meantime, why not take a rest? It must have been a long road."
    scene 39_s17 with dissolve
    mc "...I would love to have a bath. If that's possible."
    scene 39_s26 with dissolve
    oswald "Of course, I will send for Ymir to escort you to the bathhouse."
    scene 39_s17 with dissolve
    mc "Ymir? Isn't she taking care of Alex?"
    scene 39_s27 with dissolve
    ysella "No! Anyone but her. She's... not ready."
    scene 39_s28 with dissolve
    oswald "It's fine, dear. She won't repeat her mistake."
    scene 39_s27 with dissolve
    ysella "...Are you certain?"
    scene 39_s28 with dissolve
    oswald "Give her a second chance. The Goddess teaches forgiveness. We must listen."
    ysella "..."
    scene 39_s20 with dissolve
    ysella "I apologize, traveler. There's no need to fret—you're in good hands."
    scene 39_s17 with dissolve
    mc "Alright."
    scene 39_s20 with dissolve
    ysella "I don't believe I caught your name yet. What should we call our honored guest?"
    scene 39_s17 with dissolve
    mc "It's [mc]."
    scene 39_s20 with dissolve
    ysella "Thank you. You may go now."
    scene 39_s17 with dissolve
    mc "Where is—"
    scene 39_s22 with dissolve
    ymir "Shall we?"
    scene 39_s23 with dissolve
    mc "Woah—Uh... sure."
    call screen scene39_choice01 with dissolve


label scene39_choice01_op1:
    $ mc_looked_ymir = True
    scene 39_s24 with dissolve
    perception "Round, inviting, barely contained by the fabric clinging to her."
    scene 39_s23 with dissolve
    mc "Let's go..."
    jump scene40

label scene40:
    stop music fadeout 3.0
    scene 40_s1 with Fade(1.0,1.0,1.0)
    mc "How's Alex doing?"
    ymir "She's fine. I gave her a pain relief brew and wrapped her ribs."
    ymir "She's resting now. She was... resistant at first, but the herbs are strong. She'll sleep for a while."
    mc "Good to hear. Thank you for taking care of her."
    ymir "It's my duty."
    scene 40_s2 with Fade(0.5,0.5,0.5)
    mc "(Well, this is definitely a step down from the castle's bath...)"
    scene 40_s3 with dissolve
    mc "(Alright, where do I start with this?)"
    ymir "Would you like some help?"
    scene 40_s4 with dissolve
    mc "Help?"
    ymir "Mhmm."
    call screen scene40_choice01 with dissolve

label scene40_choice01_op2:
    $ mc_allowed_ymir = False
    mc "I'll handle it myself, but thanks. I'm not really used to... people helping me bathe."
    ymir "..."
    scene 40_s5 with dissolve
    ymir "As you wish."
    scene 40_s4 with dissolve
    perception "She lingers a moment before leaving. Something about her expression sticks with you."
    scene 40_s6 with dissolve
    ""
    scene 40_s7 with Fade(0.5,0.5,0.5)
    mc "*sigh* (This wasn't so bad after all... Just a quiet village. A little weird, but... harmless.)"
    scene black with fade
    "*knock* *knock*"
    scene 40_s63 with Fade(0.5,0.5,0.5)
    ysella "I apologize for the intrusion, [mc]. Are you finished? The water must be getting cold by now."
    scene 40_s64 with dissolve
    mc "No worries. I'm just getting dressed."
    scene 40_s63 with dissolve
    ysella "Very well. Let me take you to the lodge now. Your friend is there too."
    scene 40_s64 with dissolve
    jump scene41

label scene40_choice01_op1:
    $ mc_allowed_ymir = True
    mc "I don't mind some help. My hands are still sore from the fight."
    scene 40_s8 with dissolve
    mc "What are you—"
    scene 40_s9 with dissolve
    ymir "Is something wrong?"
    scene 40_s10 with dissolve
    mc "...No, there aren't."
    scene 40_s9 with dissolve
    ymir "Good."
    scene 40_s10 with dissolve
    scene 40_s11 with fade
    ""
    scene 40_s12 with Dissolve(0.8)
    ""
    scene 40_s13 with Dissolve(0.8)
    ymir "Your body... She'll be pleased."
    scene 40_s12 with Dissolve(0.8)
    mc "She? The goddess everyone keeps mentioning?"
    mc "What does she have to do with my body?"
    scene 40_s14 with Dissolve(0.8)
    mc "..."
    scene 40_s15 with Dissolve(0.8)
    ""
    scene 40_s16 with dissolve
    mc "Haa... Hey... That's getting a little—"
    ymir "This part needs cleaning too."
    mc "I understand, but..."
    scene 40_s17 with dissolve
    sensation "Her movements suddenly gets faster, your crotch feels like it's on fire from the constant rubbing."
    mc "Ow!"
    ymir "..."
    scene 40_s18 with dissolve
    mc "Stop that!"
    scene 40_s19 with dissolve
    mc "Hngg!"
    scene 40_s20 with vpunch
    mc "Ahh!"
    ymir "Hah... hahh..."
    ymir "Your... I need it. Please... just a little."
    scene 40_s21 with vpunch
    ""
    scene 40_s23 with dissolve
    mc "Wh-What are you doing?!"
    scene 40_s22 with dissolve
    if mc_looked_ymir:
        ymir "You think I haven't seen you staring at my breasts? Hah! I know you want this too."
    ymir "Just stay still. It'll feel good... I promise."
    scene 40_s23 with dissolve
    call screen scene40_choice02 with dissolve

label scene40_choice02_op1:
    $ mcname = persistent.name
    if persistent.name == "None" or mcname == "None":
        while mcname == "None" or mcname == "":
            $ mcname = renpy.input("There was an issue with your name. Please rewrite your name:", length=32)
        $ persistent.name = mcname
    if not persistent.scene3_p4_replay:
        $ persistent.scene3_p4_replay = True
    mc "Alright..."
    scene 40_s22 with dissolve
    ymir "It has been far too long... Hah... I've ached for this."
    scene 40_s23 with dissolve
    scene 40_s53 with Dissolve(0.8)
    ""
    scene 40_s54 with dissolve
    perception "She straddles your face, lowering herself until your lips meet the heat of her cheeks."
    ymir "Lick it! Taste me!"
    call screen scene40_choice03 with dissolve

label scene40_choice03_op1:
    scene 40_s55 with dissolve
    sensation "You part her lips with your tongue. Her nectar flows freely, coating your tongue with a deep, almost intoxicating flavor."
    ymir "MMfhmm~ Yes... That's it. Just like that, keep going. Fhnnmm~! Your tongue..."
    sensation "You probe deeper, curling your tongue inside her, your face drenched as her juices run down your chin."
    ymir "Ah! Hhnnn~ I can't—I'm going to!"
    play sound "se_sfx/masturbate_female/masturbate_cum2.mp3"
    scene 40_s57 with vpunch
    ymir "Haaaaaa!!!"
    perception "Her thighs clamp around your head as she cries out, her body trembling. You're overwhelmed by the sudden rush of her climax, warm and relentless against your face."
    scene 40_s58 with dissolve
    ymir "Goddess above... That felt so freeing."
    ymir "You've earned a reward, warrior. Let me take care of you now."
    scene 40_s24 with dissolve
    ""
    jump scene40_choice02_op1_continue

label scene40_choice03_op2:
    scene 40_s56 with dissolve
    perception "You press your tongue to her other hole, circling her tight rim. She stiffens in surprise."
    ymir "W-What are you... licking me there?!"
    sensation "You push forward, tasting her raw and intimate. Her body shudders as you slide your tongue past the resistance and into her heat."
    ymir "Mfhmm! Wh-Why does it feel that good...?"
    sensation "You fuck her with your tongue, each movement making her squirm and moan above you."
    ymir "Hnnn~ Fine... Just—don't stop!"
    ymir "Deeper! Push it in deeper! I'm... I'm close...!"
    play sound "se_sfx/masturbate_female/masturbate_cum2.mp3"
    scene 40_s57 with vpunch
    perception "Before you can prepare yourself, her body locks up. She lets out a scream as her climax crashes down. Your mouth and nose are smothered as she rides out every wave, breath ragged."
    ymir "Haaaaaa!!!"
    scene 40_s58 with dissolve
    ymir "Ahhh... Hnnn... That tongue of yours... That felt so freeing."
    ymir "You've more than earned a reward. Let me return the favor."
    scene 40_s24 with dissolve
    ""
    jump scene40_choice02_op1_continue
    
image 40_ymir_hj1 = Movie(play="images/3_chapter2/scene40/40_ymir_hj1.webm", loop=True)  
image 40_ymir_hj2 = Movie(play="images/3_chapter2/scene40/40_ymir_hj2.webm", loop=True) 
image 40_ymir_bj1 = Movie(play="images/3_chapter2/scene40/40_ymir_bj1.webm", loop=True)   
image 40_ymir_bj2 = Movie(play="images/3_chapter2/scene40/40_ymir_bj2.webm", loop=True)   

image 40_ymir_d_bj1 = Movie(play="images/3_chapter2/scene40/40_ymir_d_bj1.webm", loop=True)   
image 40_ymir_d_bj1_faster = Movie(play="images/3_chapter2/scene40/40_ymir_d_bj1_faster.webm", loop=True) 
image 40_ymir_d_bj2 = Movie(play="images/3_chapter2/scene40/40_ymir_d_bj2.webm", loop=True)   
image 40_ymir_d_bj2_faster = Movie(play="images/3_chapter2/scene40/40_ymir_d_bj2_faster.webm", loop=True)    

label scene40_choice02_op1_continue:
    show 40_ymir_hj1 with fade
    sensation "Her grip tightens around your cock, her hand rough and desperate against your skin."
    ymir "Come on. Let me see you fall apart for me."
    mc "Ah... You're going to fast!"
    scene black with Dissolve(0.3)
    show 40_ymir_hj2 with dissolve
    ymir "Keep looking at my bottom while I pleasure you. I want your eyes on me."
    ymir "It will feel really good! Just let it spurt when you're ready~"
    ymir "I haven't done this before but..."
    scene black with Dissolve(0.3)
    show 40_ymir_bj1 with dissolve
    sensation "Her wet mouth crashes down on your cock, the heat of it nearly unbearable."
    ymir "*slurp* Nhmmm~"
    mc "Why... ahh... are you doing this?"
    ymir "Mfhmm~"
    mc "Ahh..."
    ymir "*slurp* Prease... give it to me."
    scene black with Dissolve(0.3)
    show 40_ymir_bj2 with dissolve
    mc "Hnn—!"
    call screen scene40_choice04 with dissolve


label scene40_choice04_cum:
    show screen cum
    play sound "se_sfx/sex/sex_cum1.mp3" 
    scene 40_s25 with vpunch
    sensation "Hot seed spills from your cock and right into her greedy mouth. You can feel her throat contracting as she swallows every drop."
    play sound "se_sfx/blowjob/blowjob_cum1.mp3" 
    scene 40_s26 with vpunch
    ymir "Mffhmmm!!"
    hide screen cum
    scene 40_s27 with Dissolve(1.0)
    ymir "Mmmh~! So much!"
    mc "Hahh..."
    scene 40_s28 with dissolve
    ymir "On no! What have I done?!"
    play sound "sound_effects/door.mp3" fadein 0.1
    scene 40_s29 with dissolve
    ysella "*gasp* Ymir! What were you doing?"
    $ renpy.end_replay()
    jump scene40_finale

label scene40_choice02_op2:
    $ mcname = persistent.name
    if persistent.name == "None" or mcname == "None":
        while mcname == "None" or mcname == "":
            $ mcname = renpy.input("There was an issue with your name. Please rewrite your name:", length=32)
        $ persistent.name = mcname
    if not persistent.scene4_p4_replay:
        $ persistent.scene4_p4_replay = True
    mc "No."
    scene 40_s34 with Dissolve(0.8)
    perception "You rise to your feet, towering over her. Ymir blinks in surprise, a hint of nervousness breaking through her bravado."
    ymir "I told you to stay down!"
    impulse "Tear the fight out of her. Make her crawl. Make her beg to be allowed to breathe your air. Smash that spark in her eyes until there's nothing left but trembling obedience."
    scene 40_s35 with dissolve
    ymir "Ah! What are you— Let go!"
    mc "You need to be taught something first."
    scene 40_s36 with dissolve
    mc "Come here."
    ymir "Owww!"
    scene 40_s37 with dissolve
    ymir "Ahh!"
    scene 40_s38 with Fade(0.5,0.5,0.5)
    mc "What do you think you were doing, huh?"
    call screen scene40_choice05 with dissolve
    play sound "sound_effects/slap01.mp3"
    scene 40_s39 with vpunch
    ymir "Hnn!"
    scene 40_s38 with dissolve
    mc "You can't just act on impulse like that. Not with me."
    call screen scene40_choice05 with dissolve
    play sound "sound_effects/slap03.mp3"
    scene 40_s39 with vpunch
    ymir "I-I didn't mean—"
    scene 40_s38 with dissolve
    mc "Quiet. I want to {i}feel{/i} that apology."
    call screen scene40_choice05 with dissolve
    play sound "sound_effects/slap04.mp3"
    scene 40_s39 with vpunch
    ymir "Ahh!"
    perception "Her soft cries echo with every smack of your hand against her ass."
    scene 40_s38 with dissolve
    ymir "A-Ahh! I'm sorry... I'm sorry...!"
    call screen scene40_choice05 with dissolve
    play sound "sound_effects/slap03.mp3"
    scene 40_s40 with vpunch
    perception "Her ass grows red, trembling beneath your hand. Her whimpers start turning breathy."
    scene 40_s41 with dissolve
    ymir "Owww! My butt is getting really sore!"
    mc "Good. Then maybe it'll stick."
    call screen scene40_choice05 with dissolve
    play sound "sound_effects/slap05.mp3"
    scene 40_s40 with vpunch
    ymir "Ahnn! Please..."
    perception "Her voice gets even softer, almost on the verge of breaking into sops as your her ass gets redder and redder."
    scene 40_s41 with dissolve
    ymir "I... I don't know what came over me..."
    $ scene40_choice05_end = True
    call screen scene40_choice05 with dissolve
    play sound "sound_effects/slap01.mp3"
    scene 40_s40 with vpunch
    ymir "I'm sorry~! I'm sorry~! I'm sorry~!"
    scene 40_s41 with dissolve
    call screen scene40_choice05 with dissolve
    play sound "sound_effects/slap06.mp3"
    scene 40_s40 with vpunch
    ymir "Ahnnmm~!"
    scene 40_s41 with dissolve
    call screen scene40_choice05 with dissolve
    play sound "sound_effects/slap04.mp3"
    scene 40_s40 with vpunch
    ymir "Ahhaaaaaa~!"
    scene 40_s41 with dissolve
    call screen scene40_choice06 with dissolve

label scene40_choice06_op1:
    play sound "sound_effects/slap05.mp3"
    scene 40_s40 with vpunch
    ymir "Ahhaaaaaa~!"
    scene 40_s41 with dissolve
    call screen scene40_choice06 with dissolve

label scene40_d_continue:
    mc "Get up. I'm not done."
    mc "I want you to apologize to my dick too."
    ymir "Will you make me feel better>"
    scene 40_s42 with fade
    perception "She lowers herself to her knees in front of you, eyes flushed, ashamed—but obedient."
    ymir "..."
    mc "Kiss it."
    scene 40_s44 with dissolve
    ymir "Mmm."
    scene 40_s42 with dissolve
    mc "Come on, put your back into it!"
    scene 40_s44 with dissolve
    ymir "*mwah!*"
    empathy "She kisses your tip like she means it—reverent, needy, trying to prove herself."
    scene 40_s42 with dissolve
    mc "Hmm... It's still not enough."
    scene 40_s43 with dissolve
    ymir "I'll kiss it aga—"
    scene 40_s42 with dissolve
    mc "No need. I want you to suck it now."
    ymir "..."
    scene 40_s43 with dissolve
    ymir "Y-Yes..."
    scene 40_s45 with fade
    ymir "Hah... hah... It's so big..."
    mc "Get to it."
    $ scene40_7_pov1 = True
    show 40_ymir_d_bj1 with Dissolve(1.0)
    sensation "Her lips wrap around you, tongue swirling slowly. She bobs her head with growing rhythm, saliva dribbling from her chin."
    call screen scene40_choice07 with dissolve

label scene40_7_pov1:
    $ scene40_7_speed = False
    $ scene40_7_pov1 = True
    $ scene40_7_pov2 = False
    scene black with Dissolve(0.3)
    show 40_ymir_d_bj1 with dissolve
    ymir "Mfgmmm..."
    call screen scene40_choice07 with dissolve

label scene40_7_pov2:
    $ scene40_7_speed = False
    $ scene40_7_pov1 = False
    $ scene40_7_pov2 = True
    scene black with Dissolve(0.3)
    show 40_ymir_d_bj2 with dissolve
    ymir "Mmmmnn~"
    call screen scene40_choice07 with dissolve

label scene40_7_bj_faster:
    scene black with Dissolve(0.3)
    $ scene40_7_speed = True
    if scene40_7_pov1:
        show 40_ymir_d_bj1_faster with dissolve
        hide 40_ymir_d_bj1
        ymir "*gag* Aghmmmm!"
    else:
        show 40_ymir_d_bj2_faster with dissolve
        hide 40_ymir_d_bj2
        ymir "Ah can't go fashter... *gag*"
    call screen scene40_choice07 with dissolve

label scene40_7_bj_slower:
    scene black with Dissolve(0.3)
    $ scene40_7_speed = False
    if scene40_7_pov1:
        show 40_ymir_d_bj1 with dissolve
        hide 40_ymir_d_bj1_faster
        ymir "Mmmm... dosh it fee good?"
    else:
        show 40_ymir_d_bj2 with dissolve
        hide 40_ymir_d_bj2_faster
        ymir "Mhm~ *slurp*..."
    call screen scene40_choice07 with dissolve

label scene40_7_cum:
    mc "I'm close!"
    sensation "She tightens her throat with every movement, anticipating your climax."
    show screen cum
    play sound "se_sfx/blowjob/gag1.mp3" 
    scene 40_s46 with vpunch
    sensation "You grunt as your seed floods her mouth. She gags, startled, but you hold her head firm."
    ymir "Mfhhmmmm?!"
    hide screen cum
    play sound "se_sfx/blowjob/blowjob_cum1.mp3" 
    scene 40_s47 with vpunch
    ymir "*gag* Aghhnn!"
    mc "Don't swallow. Show me."
    scene 40_s48 with fade
    ymir "*cough* Ahhh... *gag*"
    mc "Good. Now swallow. All of it."
    scene 40_s49 with dissolve
    ymir "..."
    play sound "se_sfx/blowjob/swallow1.mp3" 
    ymir "*gulp* *gag* *gulp*"
    mc "Show me."
    scene 40_s50 with dissolve
    ymir "Ughh..."
    mc "Good girl. My cum is in your belly now."
    scene 40_s51 with dissolve
    mc "You're mine."
    ymir "..."
    mc "Say it."
    scene 40_s65 with dissolve
    ymir "I... I'm y-your woman..."
    scene 40_s52 with dissolve
    play sound "sound_effects/door.mp3" fadein 0.1
    ysella "*gasp* Ymir! What were you doing?"
    $ renpy.end_replay()
    jump scene40_finale

label scene40_finale:
    scene 40_s30 with Fade(0.5,0.5,0.5)
    ymir "I... I couldn't help it, Mother. It's... Please forgive me."
    ymir "The hunger... i-it came over me. I tried to resist, but he's so... he's so perfect. His body. His vitality. She would want me to—"
    scene 40_s31 with dissolve
    ysella "You greedy girl. He is not yours to claim."
    ysella "You must be punished for this! Your greed has shamed us."
    if not karma_updated:
        $ karma_updated = True
        if mc_karma >= 100:
            $ mc_karma = 10
        elif mc_karma >= 90:
            $ mc_karma = 9
        elif mc_karma >= 80:
            $ mc_karma = 8
        elif mc_karma >= 70:
            $ mc_karma = 7
        elif mc_karma >= 60:
            $ mc_karma = 6
        elif mc_karma >= 50:
            $ mc_karma = 5
        elif mc_karma >= 40:
            $ mc_karma = 4
        elif mc_karma >= 30:
            $ mc_karma = 3
        elif mc_karma >= 20:
            $ mc_karma = 2
        elif mc_karma >= 10:
            $ mc_karma = 1
        else:
            $ mc_karma = 1
    if mc_karma > 10:
        $ mc_karma = 10
    if mc_karma < 1:
        $ mc_karma = 1
    call screen scene40_choice08 with dissolve


label scene40_choice08_op1:
    if mc_karma <= 4:
        $ mc_punished_ymir = True
        mc "I'll punish her myself."
        scene 40_s32 with dissolve
        ysella "A-Are you certain, [mc]?"
        scene 40_s33 with dissolve
        mc "She crossed the line with me. It's only fair I settle it."
        scene 40_s32 with dissolve
        ysella "...Very well. How do you wish to discipline her?"
        scene 40_s33 with dissolve
        mc "Come here, Ymir. Stand in front of me."
        scene 40_s59 with dissolve
        ""
        play sound "sound_effects/slap01.mp3" fadein 0.1
        scene 40_s60 with vpunch
        ymir "Ahh!"
        ysella "..."
        scene 40_s61 with dissolve
        mc "There. We're even now."
        if mc_karma > 1:
            $ mc_karma -= 1
        $ karma_less = True
        play sound "sound_effects/karma_less.mp3" volume 0.2
        show screen stat_change with easeinright
        mc "Right?"
        ymir "Y-Yes... Thank you for your mercy."
        scene 40_s62 with dissolve
        ysella "Well... Let me take you to the lodge, [mc]. Your friend is there too."
        hide screen stat_change with easeoutright
        $ karma_less = False
        scene 40_s61 with dissolve
        jump scene41
    else:
        $ renpy.notify("Check failed!")
        empathy "You meet her fearful gaze. She flinches before you can even move. You lower your hand—you just can't bring yourself to hurt her."
        call screen scene40_choice08 with dissolve

label scene40_choice08_op2:
    $ mc_agree_punish_ymir = True
    scene 40_s33 with dissolve
    mc "She does need to be punished. This shouldn't happen again."
    scene 40_s32 with dissolve
    ysella "Yes, you're right. This... this has happened before, unfortunately."
    ysella "Ymir has always been... willful. Her appetites are too strong for her own good."
    scene 40_s33 with dissolve
    mc "All the more reason to ensure it doesn't happen again."
    scene 40_s32 with dissolve
    ysella "Indeed. I will see to her discipline personally. She will spend the night in the shrine, fasting and praying for forgiveness."
    scene 40_s33 with dissolve
    mc "Good. I don't want to see her again tonight. I need to check on Alex."
    scene 40_s32 with dissolve
    ysella "Come. Let me take you to her."
    scene 40_s33 with dissolve
    jump scene41

label scene40_choice08_op3:
    $ mc_forgive_ymir = True
    scene 40_s33 with dissolve
    mc "It's fine. Let it go."
    mc "She didn't actually hurt me. I think she's just... lonely."
    if mc_karma < 10:
        $ mc_karma += 1
    $ karma_more = True
    play sound "sound_effects/karma_more.mp3" volume 0.2
    show screen stat_change with easeinright
    scene 40_s32 with dissolve
    ysella "Forgive her, [mc]. She let desire cloud her duty."
    ysella "It is the curse of youth—to want so desperately that you forget yourself. But your mercy speaks well of you."
    ymir "Thank you..."
    ysella "Come. You must be exhausted. Let me take you to the lodge. Your friend is there too."
    scene 40_s33 with dissolve
    hide screen stat_change with easeoutright
    $ karma_more = False
    #mc and ysella arrive at a small cabin with only two beds

label scene41:
    scene 41_s1 with Fade(1.0,1.0,1.0)
    ""
    scene 41_s2 with Fade(0.5,0.5,0.5)
    ysella "I hope you don't mind the simple accommodations. As I said before, we are simple folk who only wish to live in peace."
    mc "It's fine. Beats sleeping outside."
    scene 41_s3 with dissolve
    if mc_allowed_ymir:
        ysella "And... [mc], I hope Ymir didn't startle you too badly at the baths."
        ysella "That girl has always been wilder than the rest of us. She means well, truly. Her heart is as fierce as her appetites."
        scene 41_s4 with dissolve
        mc "Oh, that?"
        mc "Well, I didn't really mind it."
        scene 41_s3 with dissolve
        ysella "Please forgive her boldness all the same. There are... reasons for her behavior."
        ysella "I will explain everything properly tomorrow morning, when the light is better and your thoughts are clearer."
        scene 41_s4 with dissolve
        jump scene41_continue
    else:
        scene 41_s3 with dissolve
        ysella "And... [mc], I hope Ymir didn't startle you at the baths. She told me what happened."
        ysella "I won't lie to you. I allowed her to accompany you because I thought... it might ease your burdens."
        scene 41_s4 with dissolve
        mc "I don't understand... are you saying you wanted her to fuck me?"
        scene 41_s3 with dissolve
        ysella "That's... one way to put it. She wasn't meant to go quite so far. Only to... loosen the tension in you."
        ysella "I wanted her to offer you comfort in the way our people sometimes do for honored guests."
        ysella "However, it's clear that she was too forthcoming or perhaps she wasn't to your liking."
        scene 41_s4 with dissolve
        mc "Why the hell would you send her to do something like that in the first place?"
        scene 41_s3 with dissolve
        ysella "I promise to explain everything come tomorrow morning. For now, you should rest."
        ysella "And if there's anything I can do to make up for her failure... you need only ask."
        scene 41_s4 with dissolve
        call screen scene41_choice01 with dissolve

label scene41_choice01_op1:
    $ mc_allowed_ysella = False
    mc "I'm alright, really."
    scene 41_s3 with dissolve
    ysella "I see. Please sleep well then, dear."
    scene 41_s4 with dissolve
    jump scene41_continue

image 41_hj0 = Movie(play="images/3_chapter2/scene41/41_hj0.webm", loop=True)  
image 41_hj1 = Movie(play="images/3_chapter2/scene41/41_hj1.webm", loop=True)  
image 41_hj1_faster = Movie(play="images/3_chapter2/scene41/41_hj1_faster.webm", loop=True)  
image 41_hj2 = Movie(play="images/3_chapter2/scene41/41_hj2.webm", loop=True)  
image 41_hj2_faster = Movie(play="images/3_chapter2/scene41/41_hj2_faster.webm", loop=True)  
label scene41_choice01_op2:
    $ mcname = persistent.name
    if persistent.name == "None" or mcname == "None":
        while mcname == "None" or mcname == "":
            $ mcname = renpy.input("There was an issue with your name. Please rewrite your name:", length=32)
        $ persistent.name = mcname
    if not persistent.scene5_p4_replay:
        $ persistent.scene5_p4_replay = True
    $ mc_allowed_ysella = True
    mc "I could use some comfort... As you said, Ymir wasn't my type. But {i}you{/i}..."
    scene 41_s5 with dissolve
    ysella "Yes... I understand completely."
    ysella "Then let me stay with you tonight."
    scene 41_s6 with Fade(0.5,0.5,0.5)
    ""
    scene 41_s7 with fade
    ysella "Lie down here, love."
    scene 41_s9 with fade
    perception "She gently guides your head into her lap, her thighs warm and soft around you. Her fingers slide through your hair, slow and steady, like she's taming something broken."
    scene 41_s8 with dissolve
    ysella "Would you like me to... ease the tension?"
    scene 41_s9 with dissolve
    mc "Tention?"
    scene 41_s8 with dissolve
    ysella "Yes."
    scene 41_s9 with dissolve
    mc "...Yeah."
    scene 41_s8 with dissolve
    ysella "Shh. Just relax."
    ysella "Let me see your member. I must ensure it wasn't tainted by her."
    scene 41_s9 with dissolve
    mc "Alright..."
    scene 41_s10 with dissolve
    ysella "It's so warm and hard... I will help you calm down."
    show 41_hj0 with Dissolve(1.0)
    ysella "Does this feel good?"
    mc "Mhmm."
    ysella "Good..."
    ysella "Focus on the pleasure, on the way your tip throbs for me."
    ysella "You're doing so well..."
    scene 41_s11 with dissolve
    ysella "Here, go ahead. Suckle on them, it will bring you comfort."
    scene 41_s12 with dissolve
    ysella "Mmmmm..."
    sensation "She brings her breasts to your lips, pressing them against your face. The skin is soft, the nipple hardening as your tongue glides over it."
    $ scene41_hj1 = True
    show 41_hj1 with Dissolve(1.0)
    ysella "Show me how much this big boy can ejaculate."
    sensation "Her hand wraps around your shaft—warm, slow, deliberate. She strokes with practiced ease, every motion sending a jolt straight through your core."
    ysella "Pretend that my hand is a womb and unload all your seed into it."
    mc "Ahnn..."
    ysella "Good boy... Let it out whenever you need to. I'm here for you."
    sensation "Her fingers curl tighter around your cock, jerking you with firm, wet strokes. Your hips twitch as her thumb swirls across your tip, smearing pre-cum around the sensitive tip."
    call screen scene41_choice02 with dissolve

label scene41_hj1:
    $ scene41_hj_speed = False
    $ scene41_hj1 = True
    $ scene41_hj2 = False
    scene black with Dissolve(0.3)
    show 41_hj1 with dissolve
    ysella "Mmm~ Just like that... Keep suckling, my sweet."
    call screen scene41_choice02 with dissolve

label scene41_hj2:
    $ scene41_hj_speed = False
    $ scene41_hj1 = False
    $ scene41_hj2 = True
    scene black with Dissolve(0.3)
    show 41_hj2 with dissolve
    ysella "Poor thing... You must be so pent up from your travels."
    call screen scene41_choice02 with dissolve

label scene41_hj_faster:
    scene black with Dissolve(0.3)
    $ scene41_hj_speed = True
    if scene41_hj1:
        show 41_hj1_faster with dissolve
        hide 41_hj1
        ysella "Feeling impatient? There's no need to rush, darling~ I'll stay with you until you feel better."
    else:
        show 41_hj2_faster with dissolve
        hide 41_hj2
        ysella "Do you like it when I tease the back of your tip? I know all of a man's weak spots~"
    call screen scene41_choice02 with dissolve

label scene41_hj_slower:
    scene black with Dissolve(0.3)
    $ scene41_hj_speed = False
    if scene41_hj1:
        show 41_hj1 with dissolve
        hide 41_hj1_faster
        ysella "There, there... Just let me take care of everything."
    else:
        show 41_hj2 with dissolve
        hide 41_hj2_faster
        ysella "Mmmm~ You're sucking hard... Are you getting close?"
    call screen scene41_choice02 with dissolve

label scene41_cum:
    mc "I'm close!"
    ysella "Good... Let it {i}all{/i} out, dear."
    show screen cum
    play sound "se_sfx/blowjob/facial1.mp3" 
    scene 41_s13 with vpunch
    mc "Nhnn!"
    play sound "se_sfx/blowjob/facial2.mp3" 
    scene 41_s14 with vpunch
    sensation "Your cock throbs hard before erupting—thick streams shoot across her fingers. She doesn't flinch."
    hide screen cum
    scene 41_s15 with dissolve
    ysella "Wonderful. This amount... it could surely fill a fertile womb. You did well, dear."
    scene 41_s16 with dissolve
    mc "Thank you..."
    scene 41_s15 with dissolve
    ysella "I hope your tension is gone now."
    ysella "Rest, love. Good night."
    scene 41_s16 with dissolve
    $ renpy.end_replay()
    jump scene41_continue

label scene41_continue:
    play music "night.mp3" fadein 1.0 loop
    scene 41_s17 with Fade(1.0,1.0,1.0)
    mc "*sigh*"
    scene 41_s18 with dissolve
    mc "Alex?"
    alex "..."
    scene 41_s17 with dissolve
    mc "(No more dreams, please.)"
    scene black with Fade(1.0,1.0,1.0)
    play sound "sound_effects/running_dirt.mp3" fadein 0.1
    "*pat* *pat* *pat*"
    scene 41_s19 with fade
    mc "Hmm—?"
    mc "What the hell...? Who's there?!"
    scene 41_s20 with dissolve
    annette "Oh—"
    annette "You're awake..." 
    scene 41_s21 with dissolve
    mc "..."
    mc "What are you doing?"
    scene 41_s23 with dissolve
    annette "I... I just came to check on you both. It's my duty to ensure you're comfortable."
    annette "Sorry if I startled you..."   
    scene 41_s22 with dissolve
    mc "What time is it?"  
    scene 41_s23 with dissolve
    annette "Still late. The moon is high. You should go back to sleep."  
    scene 41_s22 with dissolve
    mc "Wait... weren't you the one I saw when we first arrived here?"
    scene 41_s23 with dissolve
    annette "Yes."
    annette "Sorry I didn't greet you properly. I'm not really good with strangers..."  
    annette "Umm... I should go now."  
    annette "Sleep well."
    scene 41_s22 with dissolve
    scene 41_s17 with Fade(0.5,0.5,0.5)
    mc "(What is wrong with these people...)"
    stop music fadeout 3.0
    scene black with Fade(1.0,1.0,1.0)
    scene 41_s24 with Fade(1.0,1.0,2.0)
    play sound "sound_effects/rooster.mp3" fadein 0.1
    perception "A sharp screech cuts through the stillness—the rooster's cry, echoing from somewhere outside. The morning air feels damp, cool against your skin."
    scene 41_s25 with dissolve
    mc "*yawn*"
    mc "(Time to explore this weird village.)"
    play music "2_opening_ride.mp3" fadein 1.0 loop
    jump scene42