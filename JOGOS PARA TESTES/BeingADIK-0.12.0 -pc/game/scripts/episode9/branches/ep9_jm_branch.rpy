label ep9_jm_branch_label:
play music "music/ep9/halloween_again.mp3"
scene ep9_jill_branch1 with dissolve
de "[mc_de_up]! Come, sit down!"
scene ep9_jill_branch2 with dissolve
label ep9_jm_branch_label_wt:
mc "Why are you in here when everyone's out there?"
scene ep9_jill_branch3 with dissolve
de "People come and go. Sometimes you need a break from the party, and I offer that space."
de "You being here is a sign that it's working."
scene ep9_jill_branch4 with dissolve
mc "I'm just waiting for the HOTs to show up, so I'm walking around checking things out."
scene ep9_jill_branch5 with dissolve
de "You're a control freak, aren't you?"
scene ep9_jill_branch6 with dissolve
mc "Me? Nah. I just want the best for the party and everyone."
scene ep9_jill_branch7 with dissolve
de "So, no sign of my sis yet?"
scene ep9_jill_branch6 with dissolve
mc "Not yet."
scene ep9_jill_branch8 with dissolve
de "Here you go, [mc_de]."
mc "Thanks."
scene ep9_jill_branch9 with dissolve
mc "Can I let you in on something?"
scene ep9_jill_branch10 with dissolve
de "Sure. What is it?"
scene ep9_jill_branch9 with dissolve
mc "You know how I've been dating your sis and Josy?"
scene ep9_jill_branch14 with dissolve
de "(This asshole keeps rubbing that one in...)"
mc "I'm hoping you'll be ok with it, even if I know it hurts to think about me doing stuff to your sister."
scene ep9_jill_branch13 with dissolve
de "Get out!"
scene ep9_jill_branch14 with dissolve
mc "Look. I want to let you know that I've made up my mind about dating them."
scene ep9_jill_branch13 with dissolve
de "You're dumping them?"
scene ep9_jill_branch15 with dissolve
mc "No, it's the opposite. I realized that I only wanna be with them."
scene ep9_jill_branch16 with dissolve
de "And you invited your ex to the party."
scene ep9_jill_branch15 with dissolve
mc "Let it go, dude. This is good news, right?"
scene ep9_jill_branch16 with dissolve
de "You're telling me you're gonna be exclusive?"
scene ep9_jill_branch15 with dissolve
mc "Yeah, something like that."
scene ep9_jill_branch16 with dissolve
de "But in secret?"
scene ep9_jill_branch15 with dissolve
mc "Well, obviously."
scene ep9_jill_branch10 with dissolve
de "And they want this too?"
scene ep9_jill_branch12 with dissolve
mc "That's the thing... I haven't told them yet."
mc "It's been on the tip of my tongue for what feels like forever. Like last week when we went shopping for their costumes..."
stop music fadeout 3
scene ep9_jm_branch61 with dissolve
$ renpy.pause()
play music "music/ep8/licensed_music/track67.mp3"
scene ep9_jm_branch62 with dissolve
js "What about these? Funny, huh?"
scene ep9_jm_branch64 with dissolve
my "A stick as a costume? It's very lame."
$ guideSuggestedPage = 59
scene ep9_jm_branch63 with dissolve
js "We can get several and change between them."
if persistent.mod_wtenabled: 
                        $mod_choices = ["(+Josy)","(+Maya)","(-DIK)","(+DIK)","(Sandy scene)","(Sarah scene)","","","","","","" ]
                        #[mod_gr][mod_choices[0]]
menu:
    "Kinda funny [mod_gr][mod_choices[0]]":
        $ ep9_josy_side = True
        $ RPjosy += 1
        scene ep9_jm_branch70 with dissolve
        mc "They are kinda funny. It looks pretty good, and you won't have a problem drinking because of the costume."
        scene ep9_jm_branch65 with dissolve
        my "You guys can't be for real. It's the laziest excuse for a Halloween costume ever!"
    "Pretty lame [mod_gr][mod_choices[1]]":
        $ ep9_josy_side = False
        $ RPmaya += 1
        scene ep9_jm_branch71 with dissolve
        mc "Come on, Josy. Those are lame."
        js "Well, sorry. I'm trying to keep us on a low budget."

scene ep9_jm_branch66 with dissolve
my "A Halloween party is supposed to be fun! It's your chance to dress up as anything you can imagine!"
my "You can be a princess! You can be a dragon! The sky's the limit!"
scene ep9_jm_branch72 with dissolve
js "Haha! It feels like you're about to burst out into a musical number."
scene ep9_jm_branch69 with dissolve
my "What are you going as, [name]?"
scene ep9_jm_branch76 with dissolve
mc "I got my costume the other day. It's a Spartan costume, like a gladiator or something."
scene ep9_jm_branch66 with dissolve
my "See!? That's a good costume!"
scene ep9_jm_branch73 with dissolve
js "Let's look around some more and tell me what you like then."
scene ep9_jm_branch67 with dissolve
if ep9_josy_side:
    my "These are pretty expensive..."
else:
    my "Well, you're right about the prices. These are pretty expensive..."
scene ep9_jm_branch74 with dissolve
js "So...? $2 costume stick?"
scene ep9_jm_branch77 with dissolve
my "Haha! No! Not a costume stick."
scene ep9_jm_branch78 with dissolve
js "[name], help me make the sale... Please?"
scene ep9_jm_branch79 with dissolve
if ep9_josy_side:
    mc "I thought about it some more and don't see it happening. Maya's right..."
else:
    mc "You can't buy these, Josy. Come on."
mc "I think most will be somewhat ambitious with their costumes, or I hope so."
mc "You don't wanna be the person who didn't dress up enough for the party, do you?"
scene ep9_jm_branch68 with dissolve
js "It's just a party. It feels weird justifying paying $80 for something you'd wear once."
scene ep9_jm_branch80 with dissolve
my "We could always sell the costumes afterward."
scene ep9_jm_branch82 with dissolve
js "I don't think there's a high demand for costumes a day after Halloween."
scene ep9_jm_branch80 with dissolve
my "I think it's worth trying. If we could sell them for at least 50%% off, we could afford to get something better."
scene ep9_jm_branch81 with dissolve
my "Oh! What about those?"
mc "Very nice!"
scene ep9_jm_branch83 with dissolve
js "Or..."
scene ep9_jm_branch84 with dissolve
my "If you say costume stick one more time, I'm gonna slap your ass with it."
js "Hahaha!"
scene ep9_jm_branch3 with dissolve
if persistent.mod_wtenabled: 
                        $mod_choices = ["(+Josy)","(+Maya)","(-DIK)","(+DIK)","(Sandy scene)","(Sarah scene)","","","","","","" ]
                        #[mod_gr][mod_choices[0]]
menu:
    "Mod: Both":
        $ep9_wt_jm=True
        jump ep9_wt_m
        
    "Go with Maya [mod_gr][mod_choices[1]]":
        label ep9_wt_m:
        $ RPmaya += 2
        scene ep9_jm_branch4 with dissolve
        my "What are you doing?"
        scene ep9_jm_branch5 with dissolve
        mc "I...thought you needed my help."
        scene ep9_jm_branch7 with dissolve
        my "With what?"
        scene ep9_jm_branch6 with dissolve
        mc "Dressing?"
        scene ep9_jm_branch7 with dissolve
        my "Dressing?"
        scene ep9_jm_branch6 with dissolve
        mc "Undressing?"
        scene ep9_jm_branch8 with dissolve
        my "Undressing!?"
        scene ep9_jm_branch9 with dissolve
        mc "I'll be out there if you need me."
        scene ep9_jm_branch10 with dissolve
        $ renpy.pause()
        scene ep9_jm_branch11 with dissolve
        my "You can stay. Weirdo."
        scene ep9_jm_branch12 with dissolve
        menu:
            "Sit silently and watch":
                scene ep9_jm_branch13 with dissolve
                $ renpy.pause()
                scene ep9_jm_branch14 with dissolve
                $ renpy.pause()
                scene ep9_jm_branch15 with dissolve
                my "Really?"
                scene ep9_jm_branch16 with dissolve
                mc "What?"
                scene ep9_jm_branch15 with dissolve
                my "I can see your eyes, dude. And yet, not a word? Not even a grunt?"
                scene ep9_jm_branch16 with dissolve
                menu:
                    "Practice makes perfect":
                        mc "It's not the first time you've undressed in front of me. What can I say? Practice makes perfect."
                        scene ep9_jm_branch17 with dissolve
                        my "You need to practice a bit more, though. Your eyes have been glued to my butt since I removed my pants."
                        scene ep9_jm_branch18 with dissolve
                        mc "No, I refuse to learn that skill."
                        scene ep9_jm_branch17 with dissolve
                        my "Stupid."
                    "Grunt":
                        mc "Do you want me to? Because I can."
                        scene ep9_jm_branch21 with dissolve
                        mc "HNGH!!! AAHH!! OH MY GOD, MAYA!"
                        scene ep9_jm_branch19 with dissolve
                        my "Hey! Shush! Not like that!"
                        js "Um... What are you guys doing over there?"
                        scene ep9_jm_branch20 with dissolve
                        my "[name] is being socially awkward; that's what's happening."
                        mc "Hahaha!"
            "Make idle conversation":
                mc "Excited about Halloween?"
                scene ep9_jm_branch17 with dissolve
                my "I am. It makes it extra exciting knowing you've planned it."
                my "I can't wait to see what you came up with."
                my "How many are coming to the party?"
                scene ep9_jm_branch18 with dissolve
                mc "I don't know yet. The guest list keeps growing. At some point, we'll have to say it's enough."
                scene ep9_jm_branch17 with dissolve
                my "Yeah, I bet you have to be careful about that. Word of mouth travels fast, and I heard a lot of students talking about the party."
        scene ep9_jm_branch22 with dissolve
        $ renpy.pause()
        scene ep9_jm_branch23 with dissolve
        my "This looks nice, doesn't it?"
        scene ep9_jm_branch24 with dissolve
        mc "Very nice; it's a great costume."
        scene ep9_jm_branch25 with dissolve
        js "So, we're not doing these?"
        scene ep9_jm_branch26 with dissolve
        my "Haha! Get out!"
        scene ep9_jm_branch27 with dissolve
        js "What do you think?"
        scene ep9_jm_branch28 with dissolve
        my "You're beautiful."
        stop music fadeout 3
        scene ep9_jm_branch29 with dissolve
        $ renpy.pause()
        $ new_bio("Maya", "I went with Maya into the fitting booth.")
        if ep9_wt_jm:
           jump ep9_wt_j
    "Go with Josy [mod_gr][mod_choices[0]]":
        label ep9_wt_j:
        $ RPjosy += 2
        scene ep9_jm_branch30 with dissolve
        js "Uh oh. No dirty thoughts, ok?"
        scene ep9_jm_branch31 with dissolve
        mc "When have I ever?"
        scene ep9_jm_branch32 with dissolve
        if ep8_josy_lewd:
            js "At the gym, for one."
            scene ep9_jm_branch33 with dissolve
            mc "What? Like that one was my fault. Your ass looked too hot in those pants."
            scene ep9_jm_branch32 with dissolve
            js "You're gonna have a hard time handling this, then."
            scene ep9_jm_branch34 with dissolve
            js "Joking aside... I'm trying to make Maya feel better by playing along and not making a big deal about what happened with Sage's family and all."
        else:
            js "Tsk..."
            scene ep9_jm_branch34 with dissolve
            js "Listen, I'm trying to make Maya feel better by playing along and not making a big deal about what happened with Sage's family and all."
        scene ep9_jm_branch35 with dissolve
        mc "I can see that. I hate that we can't ignore it forever, but it feels good when we don't focus on it."
        scene ep9_jm_branch36 with dissolve
        js "All I'm saying is, let's make this a great party for her."
        scene ep9_jm_branch37 with dissolve
        mc "Absolutely. For all of us."

        scene ep9_jm_branch38 with dissolve
        menu:
            "Try to look away":
                scene ep9_jm_branch48 with dissolve
                $ renpy.pause()
                scene ep9_jm_branch50 with dissolve
                js "What are you doing?"
                scene ep9_jm_branch51 with dissolve
                mc "Trying my best to not get dirty thoughts."
                scene ep9_jm_branch50 with dissolve
                js "You look constipated."
                scene ep9_jm_branch51 with dissolve
                mc "Yeah, it's a struggle."
                scene ep9_jm_branch52 with dissolve
                js "I'm impressed, but you'll never make it."
                scene ep9_jm_branch47 with dissolve
                mc "No, no... I...will. Fuck..."
                js "Haha! Knew it!"
            "Check her out":
                scene ep9_jm_branch39 with dissolve
                $ renpy.pause()
                scene ep9_jm_branch40 with dissolve
                $ renpy.pause()
                scene ep9_jm_branch41 with dissolve
                js "You have no shame, huh?"
                scene ep9_jm_branch42 with dissolve
                mc "It's like an eclipse, you know? You know you shouldn't look directly at it, but you wanna."
                scene ep9_jm_branch43 with dissolve
                js "You're only making it harder for yourself."
                scene ep9_jm_branch44 with dissolve
                mc "You're telling me..."
                scene ep9_jm_branch45 with dissolve
                js "It must suck to be a guy sometimes, eh? To not be able to control yourself."
                scene ep9_jm_branch46 with dissolve
                mc "I can control myself, but I choose not to."


        scene ep9_jm_branch53 with dissolve
        js "How do I look?"
        scene ep9_jm_branch54 with dissolve
        mc "It fits you. Are you...um...?"
        js "What?"
        scene ep9_jm_branch55 with dissolve
        mc "Are you gonna wear stockings with that or...?"
        scene ep9_jm_branch56 with dissolve
        js "Dirty thoughts, huh?"
        scene ep9_jm_branch57 with dissolve
        my "They fit!"
        js "They do!"
        scene ep9_jm_branch58 with dissolve
        my "Yes. This is it. This is totally it!"
        scene ep9_jm_branch59 with dissolve
        js "Unless..."
        my "Haha! Fucking give me that!"
        stop music fadeout 3
        scene ep9_jm_branch60 with dissolve
        $ renpy.pause()
        $ new_bio("Josy", "I went with Josy into the fitting booth.")

scene ep9_jill_branch9 with dissolve
play music "music/ep9/halloween_again.mp3"
mc "I'm bursting to tell them, but I want the moment to be perfect. So, I'm working on it."
mc "Tonight might be the night."
scene ep9_jill_branch17 with dissolve
de "Are you asking me for my blessing?"
scene ep9_jill_branch18 with dissolve
mc "No?"
scene ep9_jill_branch17 with dissolve
de "Are you sure? You kinda should."
scene ep9_jill_branch18 with dissolve
mc "Do I have your blessing?"
scene ep9_jm_branch1 with dissolve
de "My brother is gonna be my brother-in-law!"
scene ep9_jm_branch2 with dissolve
mc "Dude, that sounds so weird."
scene ep9_jill_branch17 with dissolve
de "You have my blessing, [mc_de]. At least for now. And as long as you keep whatever you three do to yourselves."


if wt_ep9_branch_numbers > 1 and branchSage:
    jump ep9_sage_branch_label
    
if wt_ep9_branch_numbers > 1 and branchAlone:
    jump ep9_others_branch_label
    
if wt_ep9_branch_numbers > 1 and branchIsabella:
    mc "(I need to get back to my room...)"
    mc "I need to check on something real quick."
    jump ep9_bella_branch_label
scene ep9_jill_branch19 with dissolve
stop music fadeout 3
"The HOTs! The HOTs! They're finally here!"
de "Fuck yes! Let's go check it out!"
jump ep9_wave2_label


label ep9_jm_committing_label:
scene ep9_jm_committing1 with dissolve
js "There he is!"
my "[name]! Haha! Josy got to make drinks in Derek's bar! She made one for you!"
scene ep9_jm_committing2 with dissolve
mc "Is this safe to drink?"
scene ep9_jm_committing3 with dissolve
js "Haha! Nope! I have no idea what it is!"
scene ep9_jm_committing4 with dissolve
my "It's horrible! It's like half alcohol!"
scene ep9_jm_committing5 with dissolve
mc "Haha! Yum..."
mc "Wanna go somewhere and talk?"
scene ep9_jm_committing6 with dissolve
my "Sure. Sofas?"
scene ep9_jm_committing5 with dissolve
mc "I was thinking of someplace more private."

if len(wt_ep9_scenes) < 2:

    $ renpy.sound.play("sound_effects/crickets.mp3", channel="sfx1", loop=True)
    $ renpy.sound.play("sound_effects/season3/bus.mp3", channel="sfx2", loop=False)
    scene ep9_ending18 with dissolve
    $ renpy.pause()
    scene ep9_ending20 with dissolve
    $ renpy.pause()
    scene ep9_ending19 with dissolve
    $ renpy.pause()
    stop music fadeout 3
    $ renpy.music.stop(channel="sfx1", fadeout=3)
    $ renpy.music.stop(channel="sfx2", fadeout=3)
    scene ep9_ending21 with dissolve
    $ renpy.pause()
scene ep9_jm_committing7 with wipeleft
play music "music/ep9/licensed_music/track129.mp3"
queue music ["music/ep8/licensed_music/track61.mp3","music/ep9/licensed_music/track129.mp3"]
my "People are starting to leave, aren't they?"
scene ep9_jm_committing8 with dissolve
mc "Yeah. The party will keep going all night, but it's running on fumes now."
mc "Did you have fun?"
scene ep9_jm_committing7 with dissolve
my "I had a great time. I needed this party."
scene ep9_jm_committing9 with dissolve
js "Me too. You've done such a great job with it!"
scene ep9_jm_committing8 with dissolve
mc "Yeah? What did you like the most?"
scene ep9_jm_committing9 with dissolve
js "The decorations! This place looked totally different."
scene ep9_jm_committing10 with dissolve
my "Don't hate me, but I loved the pumpkin muffins the most."
js "Haha! The muffins!? Really?"
my "They were SO good!"
scene ep9_jm_committing8 with dissolve
mc "Haha! There's a whole container of them left in the fridge if you want some."
scene ep9_jm_committing7 with dissolve
my "Thanks, but I've had enough for tonight."
scene ep9_jm_committing9 with dissolve
js "How was your night?"
scene ep9_jm_committing8 with dissolve
mc "I have mixed feelings about it. At the start, I wasn't very relaxed."
mc "But the longer the party went on, the more fun I had - barring a few incidents."
mc "And at the end of it, I had a great time, especially now that I get to end the night with you two."
scene ep9_jm_committing11 with dissolve
$ renpy.pause()
scene ep9_jm_committing8 with dissolve
mc "I wanna tell you two something. It's been on my mind for a while now, and I can't think of a better time to say it than tonight."
mc "I've been waiting for this moment..."

scene ep9_jm_committing12 with dissolve
my "Why are you smiling?"
js "Wanna tell us what?"
scene ep9_jm_committing8 with dissolve
mc "I'm off the market now. I want to commit to us."
scene ep9_jm_committing12 with dissolve
js "What?"
my "Commit to us...how?"
scene ep9_jm_committing8 with dissolve
mc "You know... Stop dating others and only be with you two."
scene ep9_jm_committing13 with dissolve
mc "If I put it like this, I feel that my strings are beginning to attach."
scene ep9_jm_committing14 with dissolve
my "You're fully on board now?"
scene ep9_jm_committing13 with dissolve
mc "I'm jumping on the train and will ride it wherever it goes."
scene ep9_jm_committing15 with dissolve
js "Really!?"
scene ep9_jm_committing13 with dissolve
mc "Yes. Are you two with me?"
scene ep9_jm_committing16 with dissolve
my "Haha! Choo-choo!"
js "CHOO-CHOO!"
play sound "sound_effects/shove.mp3"
scene ep9_jm_committing17 with hpunch
$ renpy.pause()
scene ep9_jm_committing18 with dissolve
js "I can't believe this!"
scene ep9_jm_committing19 with dissolve
mc "I'm so happy you feel the same way."
scene ep9_jm_committing20 with dissolve
my "Do I have a girlfriend and a boyfriend now?"
my "Maybe I'm luckier than I thought I was all this time."
scene ep9_jm_committing21 with dissolve
js "We all are."
scene ep9_jm_committing22 with dissolve
mc "I'm luckier than you. I have TWO girls."
scene ep9_jm_committing23 with dissolve
my "Oh, yeah? My boyfriend would kick your ass. He's really strong."
scene ep9_jm_committing21 with dissolve
js "And my boyfriend is better than your boyfriend. He's in a frat, and he's got an amazing body."
scene ep9_jm_committing22 with dissolve
mc "Is this gonna be a thing?"
scene ep9_jm_committing23 with dissolve
my "We have to celebrate this somehow."
scene ep9_jm_committing21 with dissolve
js "Can we please go and do what I've waited all night to do?"
scene ep9_jm_committing23 with dissolve
my "She wants us to go to bed."
scene ep9_jm_committing24 with dissolve
mc "You're that tired?"
scene ep9_jm_committing25 with dissolve
js "We won't be sleeping."
scene ep9_jm_committing22 with dissolve
mc "My room or yours?"
scene ep9_jm_committing23 with dissolve
my "Definitely your room."
stop music fadeout 3
scene ep9_jm_committing25 with dissolve
js "Yep, it's the closest, and I can't wait."

label ep9_jm_lewd_label:
if _in_replay:
    hide screen new_phone_screen
    if persistent.name == None:
        $ name = "MC"
    else:
        $ name = persistent.name
    if persistent.mc_maya == None:
        $ mc_maya = name
    else:
        $ mc_maya = persistent.mc_maya
    if persistent.mc_josy == None:
        $ mc_josy = name
    else:
        $ mc_josy = persistent.mc_josy
    if persistent.josy == None:
        $ josy = "Josy"
    else:
        $ josy = persistent.josy
    if persistent.maya == None:
        $ maya = "Maya"
    else:
        $ maya = persistent.maya
hide screen new_phone_screen
play music "music/ep9/licensed_music/track121.mp3"
queue music ["music/ep9/licensed_music/track124.mp3","music/ep9/licensed_music/track121.mp3"]
scene ep9_jm_lewd1 with dissolve
js "Finally."
scene ep9_jm_lewd2 with dissolve
mc "You're not wasting any time."
scene ep9_jm_lewd3 with dissolve
my "This evening has felt like a big foreplay, with all the teasing and whatnot."
js "[name] wearing the least out of everyone didn't help."
scene ep9_jm_lewd4 with dissolve
mc "The least? Come on; that can't be true... What about...um?"
scene ep9_jm_lewd5 with dissolve
js "I'm telling you, you were the nudest person at the party tonight."
scene ep9_jm_lewd4 with dissolve
mc "No, what about the strippers or that girl who went topless?"
scene ep9_jm_lewd6 with dissolve
my "They came more dressed than you; I think that's the point."
scene ep9_jm_lewd4 with dissolve
mc "Derek showed his ass the entire night."
scene ep9_jm_lewd5 with dissolve
js "That doesn't count, and the rest of him was covered."
scene ep9_jm_lewd4 with dissolve
mc "I'm sure I'm missing someone..."
scene ep9_jm_lewd6 with dissolve
my "Stop thinking about that."
scene ep9_jm_lewd7 with dissolve
js "Yeah. All I care about now is that you're the least-dressed guy in this room."
scene ep9_jm_lewd8 with dissolve
my "Haha! Totally!"
scene anim_mj_panty_grind_ep9 with dissolve
js "Let's tease him a bit..."
my "Hngn... I can feel it through my panties. Is it hard already?"
js "It's rarely a problem with [name], I think."
pause
scene ep9_jm_lewd9 with dissolve
my "I could easily cum from doing this..."
scene anim_mj_panty_grind2_ep9 with dissolve
mc "You think?"
my "I think it's the alcohol or something... I'm so turned on right now."
mc "Josy talking about sexy stuff all night probably hasn't helped."
pause
scene ep9_jm_lewd10 with dissolve
js "I wanna feel something against me too..."
js "I wish you had two cocks, one for each of us."
scene ep9_jm_lewd11 with dissolve
my "I have an idea... It's kinda what you and I do together. Remove your bottoms."
scene ep9_jm_lewd12 with dissolve
my "Let's take one leg each."
scene ep9_jm_lewd13 with dissolve
js "I see what you're getting at."
scene anim_jm_hj1_ep9 with dissolve
js "Hnnn... Yes, this works..."
mc "Fuck... Why is this so hot?"
my "Do you like it?"
pause
scene anim_jm_hj2_ep9 with dissolve
mc "Feeling your moist pussies grind my legs only makes me harder..."
js "Your dick is throbbing right now."
my "Yeah, it totally is."
pause

scene ep9_jm_lewd14 with dissolve
js "Wanna leave the wings on?"
scene ep9_jm_lewd15 with dissolve
my "Sure. I mean, it's Halloween."
scene ep9_jm_lewd14 with dissolve
js "Ok, let's do it."
scene ep9_jm_lewd16 with dissolve
mc "I want you..."
scene ep9_jm_lewd17 with dissolve
js "You're gonna have us."
scene ep9_jm_lewd18 with dissolve
my "Both of us. All to yourself."
scene ep9_jm_lewd17 with dissolve
js "How should we start?"
scene ep9_jm_lewd16 with dissolve
label ep9_mj_lewd_loop_label:
menu:
    "Handjob":
        scene ep9_jm_lewd19 with dissolve
        js "Let me feel it again..."
        scene anim_jm_hj4_ep9 with dissolve
        my "That looks good... Right, [mc_maya]?"
        mc "Hngn..."
        pause
        scene ep9_jm_lewd20 with dissolve
        js "He's not gonna answer you. He's fully into it."
        scene anim_jm_hj5_ep9 with dissolve
        js "When you massage the head like this, it's the best for him."
        my "Really?"
        js "Yeah, it's so sensitive, but you can still grab it pretty hard."
        pause
        scene anim_jm_hj3_ep9 with dissolve
        js "Also, what you're doing to his balls must feel pretty good."
        mc "Yeah... It's heaven."
        my "[mc_maya] is being a bit naughty with his hands..."
        js "Is he grabbing your ass too?"
        pause
        scene ep9_jm_lewd21 with dissolve
        my "Yeah, but his thumb is teasing my asshole..."
        js "He is? Do you like it?"
        scene ep9_jm_lewd22 with dissolve
        my "I don't know... It's different... Maybe... Hngn... Yeah..."
        jump ep9_mj_lewd_loop_label
    "Lick dick":
        scene anim_jm_lick1_ep9 with dissolve
        my "*{i}Lick smack{/i}*"
        js "*{i}Lick lick{/i}* Mmm..."
        js "We wanna please your dick, [mc_josy]..."
        js "Look at us using our tongues on it."
        pause
        scene anim_jm_lick2_ep9 with dissolve
        my "*{i}Lick smack{/i}*"
        js "You're all glossy and wet now..."
        pause
        jump ep9_mj_lewd_loop_label
    "Blowjob":
        scene ep9_jm_lewd23 with dissolve
        js "Maya, I wanna see you suck on it."
        scene ep9_jm_lewd24 with dissolve
        my "Yeah?"
        js "Show me how far you can take it..."
        scene ep9_jm_lewd25 with dissolve
        js "Oh, nice... That's about how far I can take it."
        scene ep9_jm_lewd26 with dissolve
        my "*{i}Glug{/i}*"
        js "No way! That deep? Without gagging?"
        scene anim_jm_bj1_ep9 with dissolve
        my "*{i}Glug suck{/i}* Mmphhfff!"
        js "Wow! That's so impressive! How are you doing that?"
        js "Isn't she great, [mc_josy]?"
        pause
        scene anim_jm_bj2_ep9 with dissolve
        mc "I can feel her throat... It's amazing!"
        js "You gotta teach me how to do that, Maya."
        my "*{i}Glug suck{/i}*"
        pause
        jump ep9_mj_lewd_loop_label
    "Continue":
        $ renpy.pause(0.5)

scene ep9_jm_lewd27 with dissolve
js "It looked like you were ready to bust there for a second."
scene ep9_jm_lewd28 with dissolve
mc "Almost, but I'm good..."
mc "Turn around and let me return the favor."
scene ep9_jm_lewd29 with dissolve
label ep9_mj_lewd_loop2_label:
menu:
    "Finger them":
        scene ep9_jm_lewd30 with dissolve
        js "Hngn!"
        scene ep9_jm_lewd31 with dissolve
        js "Ahh!! Fuck!"
        mc "That's so warm..."
        scene ep9_jm_lewd32 with dissolve
        my "Oh, damn..."
        scene ep9_jm_lewd33 with dissolve
        my "Hngnn..."
        scene anim_jm_finger_ep9 with dissolve
        mc "You're both wet and tight... Fuck..."
        js "I love your finger inside of me. Right, Maya?"
        my "Huh? I... I can't focus... It's too good."
        js "Focus on his finger going in and out of you."
        js "Doesn't it feel amazing?"
        my "*{i}Moans{/i}* Yes..."
        pause
        jump ep9_mj_lewd_loop2_label
    "Eat pussies":
        scene anim_jm_pussy_ep9 with dissolve
        js "Yes... Use your tongue on me..."
        js "Don't stop... Don't..."
        pause
        scene ep9_jm_lewd34 with vpunch
        $ renpy.pause(0.5)
        scene ep9_jm_lewd34 with vpunch
        js "*{i}Moans{/i}* Fuck!"
        scene ep9_jm_lewd35 with dissolve
        js "You made me cum with your tongue, [mc_josy]."
        scene ep9_jm_lewd36 with dissolve
        mc "I could tell... You taste so good."
        scene anim_jm_pussy2_ep9 with dissolve
        my "*{i}Moans{/i}* Is it my turn now? Damn..."
        js "I want you to cum too, Maya."
        my "From his tongue?"
        js "Yes. Look into my eyes as he licks you."
        js "Yeah, you're getting close, aren't you?"
        js "You're trembling... [mc_josy], she's almost there now. Don't stop!"
        pause
        scene ep9_jm_lewd37 with vpunch
        $ renpy.pause(0.5)
        scene ep9_jm_lewd37 with vpunch
        $ renpy.pause(0.5)
        scene ep9_jm_lewd37 with vpunch
        my "Oh, wow! *{i}Moans{/i}*"
        scene ep9_jm_lewd38 with dissolve
        js "That's two for two!"
        jump ep9_mj_lewd_loop2_label
    "Tease assholes":
        scene ep9_jm_lewd39 with dissolve
        js "What are you doing?"
        my "Is it supposed to feel like this?"
        scene ep9_jm_lewd40 with dissolve
        js "It's kinda...interesting."
        scene ep9_jm_lewd41 with dissolve
        my "Yeah... But also... *{i}Exhales{/i}* Hngn..."
        scene ep9_jm_lewd42 with dissolve
        my "*{i}Gasps{/i}*"
        my "Easy..."
        js "I think she's enjoying it."
        scene ep9_jm_lewd40 with dissolve
        mc "What about you?"
        js "Can you do one in each at the same time?"
        scene ep9_jm_lewd43 with dissolve
        mc "Like that?"
        js "Yeah. I like that..."
        mc "Rock 'n' roll..."
        js "Hngn... What?"
        mc "Nothing..."
        scene anim_jm_asshole_ep9 with dissolve
        mc "This is pretty hot..."
        js "I'm surprised you went for our buttholes."
        mc "Yeah?"
        js "Don't get any ideas..."
        mc "Ideas? Like...anal sex?"
        js "Yes. Like anal sex."
        mc "Yeah, I do. Thanks for asking."
        js "Haha, shut up."
        my "Hngn..."
        pause
        jump ep9_mj_lewd_loop2_label
    "Eat assholes":
        scene anim_jm_rim_ep9 with dissolve
        my "OH! [mc_maya]!"
        js "Look at that... It looks hot."
        my "Hngn..."
        mc "*{i}Lick lick{/i}*"
        js "Keep going, [mc_josy]. She's enjoying this a lot."
        my "Try it on her too. I know you'll like it."
        js "Ok, if you want."
        pause
        scene anim_jm_rim2_ep9 with dissolve
        mc "*{i}Lick lick{/i}*"
        my "How is it?"
        js "I think everything's making me horny tonight. This is nuts..."
        my "Do you like how he swivels his tongue around it?"
        js "Yeah... Why haven't we tried this before?"
        my "Haha! I don't know!"
        pause
        jump ep9_mj_lewd_loop2_label
    "Continue":
        $ renpy.pause(0.5)

scene ep9_jm_lewd28 with dissolve
mc "Ok, I can't take this anymore. I gotta have you!"
scene ep9_jm_lewd27 with dissolve
js "We're yours."
$ tmpInt = 0
scene ep9_jm_lewd28 with dissolve
label ep9_mj_lewd_loop3_label:
menu:
    "Doggystyle":
        menu:
            "Maya":
                $ tmpInt += 1
                scene ep9_jm_lewd44 with dissolve
                mc "I wanna fuck you so bad..."
                my "Do it..."
                scene ep9_jm_lewd45 with dissolve
                my "*{i}Moans{/i}*"
                scene anim_jm_doggy1_ep9 with dissolve
                mc "[maya]... You're so tightly wrapped around my cock."
                my "Oh, [mc_maya]..."
                pause
                scene anim_jm_doggy2_ep9 with dissolve
                mc "You look so beautiful like that, [josy]."
                js "It's hot watching you fuck her..."
                pause
                scene anim_jm_doggy3_ep9 with dissolve
                my "*{i}Lick lick{/i}*"
                pause
            "Josy":
                $ tmpInt += 1
                scene ep9_jm_lewd47 with dissolve
                js "Put it in me, [mc_josy]."
                mc "I'm gonna..."
                scene ep9_jm_lewd46 with dissolve
                js "Hnghnnn..."
                scene anim_jm_doggy4_ep9 with dissolve
                my "Your face is all red, [mc_maya]."
                mc "Huh? Oh? It is? It must be the alcohol and horniness..."
                pause
                scene anim_jm_doggy5_ep9 with dissolve
                my "She feels good, doesn't she?"
                mc "So good..."
                js "*{i}Moans{/i}*"
                pause
        jump ep9_mj_lewd_loop3_label
    "Missionary (Josy)":
        $ tmpInt += 1
        scene ep9_jm_lewd48 with dissolve
        mc "You two drive me insane..."
        scene anim_jm_miss1_ep9 with dissolve
        my "Don't cum already, [mc_maya]."
        js "Yeah... *{i}Moans{/i}* Not yet."
        pause
        scene anim_jm_miss2_ep9 with dissolve
        mc "Don't worry... Not...yet... I think the alcohol helps."
        pause
        scene anim_jm_miss3_ep9 with hpunch
        js "Ahh!!! Fuck!"
        js "It's so deep, [mc_josy]."
        pause
        jump ep9_mj_lewd_loop3_label
    "Reverse cowgirl":
        menu:
            "Maya":
                $ tmpInt += 1
                scene anim_jm_rev1_ep9 with dissolve
                js "Fuck her, [mc_josy]."
                mc "This feels amazing..."
                my "*{i}Moans{/i}* Don't go all the way."
                pause
                scene anim_jm_rev2_ep9 with dissolve
                js "It's not all the way, trust us."
                my "Hngn... Ok..."
                pause
                scene anim_jm_rev3_ep9 with dissolve
                js "You should try watching it up close, Maya. It's so sexy..."
                my "*{i}Moans{/i}*"
                pause
            "Josy":
                $ tmpInt += 1
                scene anim_jm_rev4_ep9 with dissolve
                js "*{i}Moans{/i}* [mc_josy], I love riding your cock."
                pause
                scene anim_jm_rev5_ep9 with dissolve
                my "I don't get how you can take all of it that easily."
                js "You do it too. *{i}Moans{/i}* Trust me... I'm being fully stretched out here. Nothing about this is easy."
                pause
                scene anim_jm_rev6_ep9 with dissolve
                pause
        jump ep9_mj_lewd_loop3_label
    "Riding (Both)":
        $ tmpInt += 1
        js "Haha, I wish there was a way for both of us to fuck him."
        my "I have an idea..."
        scene ep9_jm_lewd49 with dissolve
        my "How about this?"
        js "Um... How will this work?"
        my "Just give it a try."
        scene anim_jm_double1_ep9 with dissolve
        js "Fuck... It works! Hngnn..."
        my "Right?"
        js "Yeah, he rubs me right... What about you?"
        my "I'm getting the tip of his dick in me..."
        js "Oh, not enough?"
        my "Honestly, his tip is probably a normal-sized dick."
        js "Hahaha!"
        pause
        jump ep9_mj_lewd_loop3_label
    "Swap between them":
        $ tmpInt += 1
        scene anim_jm_double2_ep9 with dissolve
        my "I never knew sharing him like this would feel so good."
        js "*{i}Smack{/i}* Uh-huh."
        mc "We've missed out on this by fucking in those public places."
        mc "My own bed feels like a breath of fresh air."
        my "*{i}Smack{/i}* Haha..."
        pause
        jump ep9_mj_lewd_loop3_label
    "Cowgirl (Maya)":
        $ tmpInt += 1
        scene anim_jm_ride1_ep9 with dissolve
        my "Yes, right there... Mmmm... [mc_maya]..."
        mc "*{i}Lick lick{/i}*"
        js "Your wet and warm tongue feels amazing, [mc_josy]."
        pause
        jump ep9_mj_lewd_loop3_label
    "Standing (Josy)":
        $ tmpInt += 1
        scene anim_jm_tease_ep9 with dissolve
        mc "Your petite ass is so hot, [josy]..."
        js "Haha, I don't care how much you butter me up... Stick to the right hole, ok?"
        scene anim_jm_stand2_ep9 with dissolve
        mc "Like I could ever get tired of this one..."
        pause
        scene anim_jm_stand1_ep9 with dissolve
        js "*{i}Smack{/i}* Mmm..."
        pause
        scene anim_jm_stand3_ep9 with dissolve
        pause
        jump ep9_mj_lewd_loop3_label
    "Cum" if tmpInt > 2:
        mc "Girls... I'm about to cum..."
        menu:
            "Facial":
                scene anim_jm_cum_ep9 with dissolve
                my "It took you a long time..."
                js "It's finally time for it, huh? I've been waiting, [mc_josy]."
                pause
                scene anim_jm_cum2_ep9 with dissolve
                js "You're really close now, aren't you?"
                my "Look into my eyes, [mc_maya]..."
                js "Cum, [mc_josy]! Cum!!!"
                pause
                scene ep9_jm_lewd50 at vpunch, cum2
                $ renpy.pause(0.5)
                scene ep9_jm_lewd50 at vpunch, cum2
                $ renpy.pause(0.5)
                scene ep9_jm_lewd51 at vpunch, cum2
                mc "Fuck!!!"
            "Creampie (Maya)":
                scene anim_jm_doggy1_ep9 with dissolve
                mc "Can I cum inside of you, [maya]?"
                my "Sure... Do it, [mc_maya]."
                scene ep9_jm_lewd52 at vpunch, cum1
                $ renpy.pause(0.5)
                scene ep9_jm_lewd52 at vpunch, cum1
                $ renpy.pause(0.5)
                scene ep9_jm_lewd52 at vpunch, cum1
                mc "Ahhh..."
                scene ep9_jm_lewd53 with dissolve
                js "Wow... You're making me jealous here."
                mc "Come here."
                scene ep9_jm_lewd54 with dissolve
                js "*{i}Lick lick{/i}* Haha... Mmm..."
            "Creampie (Josy)":
                scene anim_jm_doggy5_ep9 with dissolve
                mc "I'm gonna cum, [josy]..."
                js "Let me feel it... Fill me up, [mc_josy]."
                scene ep9_jm_lewd55 at vpunch, cum1
                $ renpy.pause(0.5)
                scene ep9_jm_lewd55 at vpunch, cum1
                $ renpy.pause(0.5)
                scene ep9_jm_lewd55 at vpunch, cum1
                mc "Ahhh, fuck!"
                scene ep9_jm_lewd56 with dissolve
                js "Oh my God... [mc_josy]... *{i}Phew{/i}*"
            "On their tits":
                scene anim_jm_cum_ep9 with dissolve
                my "It took you a long time..."
                js "It's finally time for it, huh? I've been waiting, [mc_josy]."
                pause
                scene anim_jm_cum2_ep9 with dissolve
                js "You're really close now, aren't you?"
                my "Look into my eyes, [mc_maya]..."
                js "Cum, [mc_josy]! Cum!!!"
                pause
                scene ep9_jm_lewd50 at vpunch, cum2
                $ renpy.pause(0.5)
                scene ep9_jm_lewd50 at vpunch, cum2
                $ renpy.pause(0.5)
                scene ep9_jm_lewd57 with dissolve
                $ renpy.pause()

$ renpy.end_replay()
$ persistent.ep9_lewd_jm = True
$ calcScenes()
$ new_bio("Josy", "I told Josy and Maya that I was ready to commit to them, and we had a threesome in my room.")
$ new_bio("Maya", "I told Josy and Maya that I was ready to commit to them, and we had a threesome in my room.")
$ mphone_stats_add_girl_s3("maya","You had a threesome with Josy and Maya after the Halloween party in episode 9.")
$ mphone_stats_add_girl_s3("josy","You had a threesome with Josy and Maya after the Halloween party in episode 9.")
show screen new_phone_screen
if not persistent.ep9_card4:
    $ persistent.ep9_card4 = True
    $ persistent.rew_2d_unlocked += 1
    $ persistent.chat_new_rewards = True
    $ calcRenders()
if not persistent.ep9_card5:
    $ persistent.ep9_card5 = True
    $ persistent.rew_2d_unlocked += 1
    $ persistent.chat_new_rewards = True
    $ calcRenders()
if not persistent.ep9_card6:
    $ persistent.ep9_card6 = True
    $ persistent.rew_2d_unlocked += 1
    $ persistent.chat_new_rewards = True
    $ calcRenders()
if not persistent.ep9_card7:
    $ persistent.ep9_card7 = True
    $ persistent.rew_2d_unlocked += 1
    $ persistent.chat_new_rewards = True
    $ calcRenders()
stop music fadeout 3
scene ep9_jm_lewd58 with dissolve
js "That was amazing..."
play music "music/ep9/tremolo.mp3"
my "It was beyond amazing! Mindblowingly super-duper awesome!"
scene ep9_jm_lewd59 with dissolve
mc "Wow... *{i}Phew{/i}*"
mc "Looked like you enjoyed it, Maya."
scene ep9_jm_lewd60 with dissolve
my "I think it was because it was both of you at the same time."
my "We haven't done it like this before. You know, without the pressure of getting caught."
scene ep9_jm_lewd63 with dissolve
js "Haha! How weird is that?"
js "Since we started doing things together, we've gone through a picnic blanket, a forest, and a hot tub before we tried the bed."
$ tmpInt = 0
if ep8_maya_lewd:
    $ tmpInt += 1
if ep5_followed_maya:
    $ tmpInt += 1
if ep7_solo_maya:
    $ tmpInt += 1
if ep3_mayaLewd:
    $ tmpInt += 1
if ep9_maya_lewd:
    $ tmpInt += 1

$ tmpInt2 = 0

if ep8_josy_lewd:
    $ tmpInt2 += 1
if ep5_followed_josy:
    $ tmpInt2 += 1
if ep7_solo_josy:
    $ tmpInt2 += 1
if ep7_josy_lewd:
    $ tmpInt2 += 1
if ep7_left_with_josy:
    $ tmpInt2 += 1

if tmpInt > 0:
    if (ep7_solo_maya or ep5_followed_maya or ep3_mayaLewd):
        scene ep9_jm_lewd60 with dissolve
        my "We did try the bed together, too."
        scene ep9_jm_lewd59 with dissolve
        if ep7_solo_maya and ep5_followed_maya and ep3_mayaLewd:
            mc "Yeah. Like three times?"
        elif (ep7_solo_maya and ep5_followed_maya) or (ep3_mayaLewd and ep5_followed_maya) or (ep7_solo_maya and ep3_mayaLewd):
            mc "Yeah. A couple of times."
        else:
            mc "Yeah, we did."
        scene ep9_jm_lewd60 with dissolve
        if ep9_maya_lewd:
            my "Haha! And almost your couch tonight."
    elif ep9_maya_lewd:
        scene ep9_jm_lewd60 with dissolve
        my "Haha! We almost tried your couch tonight."
    if ep8_maya_lewd:
        scene ep9_jm_lewd60 with dissolve
        my "We even went through a classroom together! Haha!"
        scene ep9_jm_lewd63 with dissolve
        js "A classroom?"
        scene ep9_jm_lewd62 with dissolve
        my "Not just a classroom. Our classroom. During the dorm party. Hahaha!"
        scene ep9_jm_lewd65 with dissolve
        js "Oh my God!"
        scene ep9_jm_lewd60 with dissolve
    my "But that's about all I can add to that. What about you?"
else:
    my "Yeah. Very weird. But you two have probably already done it, no?"

if tmpInt2 == 0 and tmpInt > 0:
    scene ep9_jm_lewd63 with dissolve
    js "You've done more together with Maya than me, it seems."
    scene ep9_jm_lewd61 with dissolve
    my "Oh."
    $ RPmaya += 3
    $ RPjosy -= 3
else:
    scene ep9_jm_lewd63 with dissolve
    if tmpInt2 > 4:
        js "Well... I don't think I can recall all the times."
    elif tmpInt2 > 3:
        js "Well... It's been quite a few times."
    else:
        js "Well... I haven't got a lot to add."
    if tmpInt2 > tmpInt + 1:
        js "A bit more than you two, I think."
        $ RPmaya -= 3
        $ RPjosy += 3
    elif tmpInt2 < tmpInt:
        js "It sounds like you've been at it more."
        $ RPmaya += 3
        $ RPjosy -= 3
    else:
        js "It sounds like we're about even."
        $ RPmaya += 3
        $ RPjosy += 3
$ guideSuggestedPage = 88
scene ep9_jm_lewd64 with dissolve
if persistent.mod_wtenabled: 
                        $mod_choices = ["(Jade scene)","(+Maya/Josy)","(-DIK)","(+DIK)","(Sandy scene)","(Sarah scene)","","","","","","" ]
                        #[mod_gr][mod_choices[0]]
menu:
    "It's all about opportunity":
        mc "It's been all about opportunity. And if you're horny, you're horny, and you go for it."
        scene ep9_jm_lewd63 with dissolve
        js "Yeah..."
        scene ep9_jm_lewd60 with dissolve
        my "You're right about that."
    "Bad to keep count [mod_gr][mod_choices[1]]":
        $ RPjosy += 1
        $ RPmaya += 1
        mc "I think it's bad to keep count. I mean, it's not a competition between us."
        mc "Let's go with the flow and see what happens."
        scene ep9_jm_lewd63 with dissolve
        js "Yeah, I agree with that."
        scene ep9_jm_lewd60 with dissolve
        my "Well said. I think we all agree on how awesome tonight was."

scene ep9_jm_lewd58 with dissolve
js "So..."
js "We're so not gonna be able to sell these costumes second-hand now."
my "Come on; they're only slightly used."
js "No, I think they are thoroughly beyond used."


scene ep9_jm_bed1 with fade
my "This party was the best one ever."
scene ep9_jm_bed2 with dissolve
js "Totally."
scene ep9_jm_bed3 with dissolve
mc "I feel like we're gonna sleep all day tomorrow."
scene ep9_jm_bed2 with dissolve
js "It will be a wasted day, but at least it will start great waking up together."
scene ep9_jm_bed3 with dissolve
mc "Earlier tonight... You cornered me with a question...about Zoey..."
scene ep9_jm_bed4 with dissolve
mc "It made me think about how I should have shared it with you."
scene ep9_jm_bed6 with dissolve
my "It's ok, [name]."
scene ep9_jm_bed9 with dissolve
js "We didn't want you to feel bad about it. We were curious, that's all."
scene ep9_jm_bed5 with dissolve
mc "I know this might feel weird to you, but she was my best friend and..."
mc "Even though she hurt me by leaving, I've missed her a lot."
if ep9_mad_at_zoey:
    mc "I'm trying my best to forgive her...but it's hard for me."
scene ep9_jm_bed4 with dissolve
mc "That said...us three..."
mc "We're what's important in my life now."
scene ep9_jm_bed7 with dissolve
my "[name]... I trust you."
scene ep9_jm_bed10 with dissolve
js "Like you said... Us three is what's important."
js "We all have a past. I guess I'm happy we got to learn more about you. Both the good and the bad."
scene ep9_jm_bed5 with dissolve
mc "What about you two?"
scene ep9_jm_bed8 with dissolve
my "What about us?"
scene ep9_jm_bed12 with dissolve
mc "I want to know something new about you before we sleep too."
scene ep9_jm_bed11 with dissolve
js "Like what?"
scene ep9_jm_bed12 with dissolve
mc "Maya Bailey... Josephine-"
scene ep9_jm_bed11 with dissolve
js "Come on... Josy! Don't be a Steve."
scene ep9_jm_bed12 with dissolve
mc "Josy Taylor..."
scene ep9_jm_bed13 with dissolve
mc "I know about Patrick, and I know about Pete..."
mc "What about your mothers? Who are they?"
scene ep9_jm_bed14 with dissolve
js "My mother?"
js "Her name is Iris. Iris Moore; it used to be Taylor before the divorce. I think I told you a bit about her."
js "She lives not that far away from here but still far enough to not see her too often."
scene ep9_jm_bed15 with dissolve
js "When my parents got divorced, I chose to be with my dad."
js "Mom got pretty upset by that, but she accepted it."
scene ep9_jm_bed16 with dissolve
js "She found a new guy...ugh... Clive. He always makes comments that guilt-trip me into feeling sad about my choice to stay with Dad."
js "As if my mom is a victim and I'm the criminal."
scene ep9_jm_bed15 with dissolve
js "It makes me not want to visit her a lot."
js "I call her occasionally, but she's fairly busy with work anyway. She runs her own company."
js "She's not the most stereotypical mom... I wish it were different, but I have a hard time seeing why my dad even chose to be with her in the first place."
scene ep9_jm_bed17 with dissolve
mc "That sounds rough."
scene ep9_jm_bed15 with dissolve
js "I'm fine. I've lived with it for quite some time, and time makes you look at it differently."
js "I was sadder about it when I was younger. Now I can see that they never made sense together."
scene ep9_jm_bed14 with dissolve
js "Something I think we three have in common is our mothers, in a sense."
js "We've all got weird \"mother situations\"."
scene ep9_jm_bed18 with dissolve
mc "Oh? That means..."
scene ep9_jm_bed19 with dissolve
my "*{i}Sigh{/i}*"
my "I don't think I want to talk about this tonight."
scene ep9_jm_bed20 with dissolve
js "You have a perfect opportunity for it now."
js "[name] wants to know, and I think he'd understand you better if he knew this."
scene ep9_jm_bed19 with dissolve
my "I'm drunk. I feel like I'm gonna cry if I start talking about it."
my "Can we leave it for another time? I don't want to ruin this night."
scene ep9_jm_bed21 with dissolve
mc "If you don't feel like talking about it, it can wait."
mc "I'm sorry that it's a hard subject for you."
scene ep9_jm_bed19 with dissolve
my "I love my mom. Her name is Helen."
my "I think that's what I can share at the moment."
scene ep9_jm_bed20 with dissolve
if persistent.mod_wtenabled: 
                        $mod_choices = ["(Jade scene)","(+Maya)","(-DIK)","(+DIK)","(Sandy scene)","(Sarah scene)","","","","","","" ]
                        #[mod_gr][mod_choices[0]]
menu:
    "Hug Maya [mod_gr][mod_choices[1]]":
        $ RPmaya += 1
        scene ep9_jm_bed22 with dissolve
        my "Oh, dude... Not ok."
        scene ep9_jm_bed23 with dissolve
        mc "I'm just hugging you."
        scene ep9_jm_bed24 with dissolve
        my "Thank you..."
        my "Can we go to sleep or something?"
        scene ep9_jm_bed23 with dissolve
        mc "Yeah. Let's get some rest."
    "Let her get out of it":
        scene ep9_jm_bed21 with dissolve
        mc "Thanks, Maya. I learned something new about you. That's all I asked for."
        mc "Let's get some sleep."
scene ep9_jm_bed13 with dissolve
mc "Good night, girls. My girls... Wow..."
stop music fadeout 3
$ new_bio("Josy", "I learned a bit more about Josy's mother.")
$ new_bio("Maya", "Maya's mother is a sensitive topic for her, it seems.")

if "Josy" not in wt_ep9_scenes:
    $wt_ep9_scenes.append("Josy")

if wt_ep9_branch_numbers != 1:
    "See other scenes?"
    menu:
          
          "Jill" if branchJill and "Jill" not in wt_ep9_scenes:
            if "Jill" not in wt_ep9_scenes:
                $wt_ep9_scenes.append("Jill")
            jump ep9_jill_lewd2_label
          "Sage" if branchSage and "Sage" not in wt_ep9_scenes:
                if "Sage" not in wt_ep9_scenes:
                   $wt_ep9_scenes.append("Sage")
                jump ep9_sage_hunt_label
          "Isabella" if branchIsabella and "Bella" not in wt_ep9_scenes:
                if "Bella" not in wt_ep9_scenes:
                    $wt_ep9_scenes.append("Bella")
                jump ep9_bella_lewd2_label
          "Quinn" if branchAlone and ep8_quinn_lewd and "Quinn" not in wt_ep9_scenes:
                
                $ep9_quinn_lewd=True
                
                if "Quinn" not in wt_ep9_scenes:
                    $wt_ep9_scenes.append("Quinn")
                jump ep9_quinn_lewd_label
          "Lily & Nicole" if branchAlone and (envyLikesYou or ep7_lily_lewd) and "Lily" not in wt_ep9_scenes:
                $ep9_lily_nicole_lewd=True
                
                if "Lily" not in wt_ep9_scenes:
                    $wt_ep9_scenes.append("Lily")
                jump ep9_lily_nicole_lewd_label
          "Melanie & Sarah" if branchAlone and (ep6_sarah_lewd or ep8_sarah_lewd or ep8_melanie_lewd or ep4_fuckedMelanie) and "Sarah" not in wt_ep9_scenes:
                
                $ep9_sarah_melanie_lewd=True
                if "Sarah" not in wt_ep9_scenes:
                    $wt_ep9_scenes.append("Sarah")
                jump ep9_sm_lewd_label
          "Continue the game":
              pass
              
if wt_ep9_branch_numbers != 1:
    "End the night with?"
    
    if persistent.mod_wtenabled: 
                        $mod_choices = ["(+DIKs)","(+Maya)","(-DIK)","(+DIK)","(Sandy scene)","(Sarah scene)","","","","","","" ]
                        #[mod_gr][mod_choices[0]]
                        if envyLikesYou:
                            $mod_choices[6]="[m_c1](Progress Nicole path)"
    
    menu:
         "Josy & Maya" if "Josy" in wt_ep9_scenes:
            $wt_ep9_end_pick="Maya"
         "Jill"  if "Jill" in wt_ep9_scenes:
            $wt_ep9_end_pick="Jill"
         "Sage"  if "Sage" in wt_ep9_scenes:
            $wt_ep9_end_pick="Sage"
         "Isabella" if "Bella" in wt_ep9_scenes:
            $wt_ep9_end_pick="Bella"
         "Quinn" if "Quinn" in wt_ep9_scenes:
            $wt_ep9_end_pick="Quinn"
         "Lily & Nicole [mod_choices[6]]" if "Lily" in wt_ep9_scenes:
            $wt_ep9_end_pick="Lily"
         "Melanie & Sarah" if "Sarah" in wt_ep9_scenes:
            $wt_ep9_end_pick="Sarah"
         "Tara & Tiffani & Gina":
            $ep9_tiffani_gina_tara=True
            $wt_ep9_end_pick="Other"


jump ep9_ending_label

label ep9_ending_maya_josy_label:
scene ep9_ending_maya_josy1 with dissolve
$ renpy.pause()
scene ep9_ending_maya_josy2 with dissolve
$ renpy.pause()
scene ep9_ending_maya_josy3 with dissolve
$ renpy.pause()
scene ep9_ending_maya_josy4 with dissolve
$ renpy.pause()
scene ep9_ending_maya_josy5 with dissolve
js "*{i}Whispers{/i}* Morning."
scene ep9_ending_maya_josy6 with dissolve
my "Hi..."
scene ep9_ending_maya_josy5 with dissolve
js "Shh... Don't wake him up."
scene ep9_ending_maya_josy6 with dissolve
my "Oh..."
my "He looks to be sleeping heavily."
scene ep9_ending_maya_josy5 with dissolve
js "I did too. Best sleep I've had in a while."
scene ep9_ending_maya_josy7 with dissolve
my "It was a great night... For many reasons."
scene ep9_ending_maya_josy5 with dissolve
js "Very."
js "How are you feeling?"
scene ep9_ending_maya_josy6 with dissolve
my "A slight headache... Derek got the good genes when it comes to hangovers. You?"
scene ep9_ending_maya_josy5 with dissolve
js "It's not too bad."
js "I have some pills for your headache in my handbag if you want them."
scene ep9_ending_maya_josy6 with dissolve
my "Yeah, I could use some. Where's your bag?"
scene ep9_ending_maya_josy5 with dissolve
js "It should be by the front door."
scene ep9_ending_maya_josy8 with dissolve
js "We don't have to do anything today, right?"
scene ep9_ending_maya_josy9 with dissolve
my "We should help out with cleaning, I think. This place is probably a big mess after last night."
scene ep9_ending_maya_josy10 with dissolve
js "Oh, yeah. I forgot."
scene ep9_ending_maya_josy11 with dissolve
my "I'll be right back."
scene ep9_ending_maya_josy12 with dissolve
$ renpy.pause()
scene ep9_ending_maya_josy13 with dissolve
js "Oh, fuck!"
scene ep9_ending_maya_josy14 with dissolve
js "Maya! Don't-!"
my "Huh!?"
scene ep9_ending_maya_josy16
le "*{i}Sings{/i}* She fucked a DIK! He came real quick! And now she does the waaaalk!"
scene ep9_ending_maya_josy17 with dissolve
tm "..."
scene ep9_ending_maya_josy15 with dissolve
$ renpy.pause()
jump ep9_ending2_label
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
