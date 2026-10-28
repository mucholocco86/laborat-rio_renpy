label startInterlude:
if steamConfig:
    $ state = "ep_interlude_steam"
else:
    $ state = "ep_interlude"
call rpc from _call_rpc
scene black
stop music fadeout 3
$ renpy.pause(2)

label epi_intro_label:
$ guideSuggestedPage = 37
#if (nonPatreonConfig or steamConfig):
#    show screen keymap_screen_s3
play music "music/ep_interlude/licensed_music/track108.mp3"
$ renpy.sound.play("sound_effects/interlude/bike_skate.mp3", channel="sfx1", loop=True)
scene anim_bike_intro_epi with dissolve
pause
scene epi_intro1 with dissolve
zo "Faster!"
scene epi_intro2 with dissolve
mc "This is as fast as I can go!"
zo "No, it's not!"
mc "It is!"
scene epi_intro3 with dissolve
if persistent.mod_wt_enabled:  
    $mod_choices = ["{size=44}(Zoey CHICK)","{size=44}(Zoey DIK)","","","","","","","","","","" ]
call screen zoey_choice_screen("Encourage him \n[mod_gr][mod_choices[0]]",1000,100, "Such a girl! \n[mod_gr][mod_choices[1]]",1250,550)
$ tmp_choice = tmp_choice
if tmp_choice == 1:
    $ zdik(-1)
    zo "I know you have it in you! You're faster than this!"
    scene epi_intro4 with dissolve
    mc "You want me to give it my all?"
    scene epi_intro3 with dissolve
    zo "Hell yeah! Faster!"
else:
    $ zdik(1)
    zo "You pedal like a girl!"
    scene epi_intro4 with dissolve
    mc "Well, it's a girl's bike. Maybe that's why."
    scene epi_intro3 with dissolve
    zo "Come on! Faster!"
scene epi_intro5 with dissolve
$ renpy.music.stop(channel="sfx1", fadeout=3)
$ renpy.pause()
scene epi_intro6 with dissolve
$ renpy.pause()
scene epi_intro7 with dissolve
$ renpy.pause()
scene anim_zoey_room_epi with dissolve
pause
scene epi_intro8 with dissolve
$ renpy.pause()
scene epi_intro9 with dissolve
$ renpy.pause()
scene epi_intro10 with dissolve
zo "Not that one. Play the one from yesterday."
scene epi_intro12 with dissolve
mc "I don't remember exactly."
scene epi_intro11 with dissolve
zo "You do."
scene epi_intro13 with dissolve
mc "Haha, this again, dammit. Are you ever going to stop doing that?"
scene epi_intro15 with dissolve
zo "What of it?"
scene epi_intro13 with dissolve
mc "I don't remember what song you mean..."
mc "...and when I say I don't know or remember something, you can't say \"You do\"."
mc "Because I don't!"
scene epi_intro16 with dissolve
zo "Yeah, but you do."
scene epi_intro14 with dissolve
$ renpy.pause()
scene epi_intro16 with dissolve
zo "It was funky, and you went something like this with your face."
scene epi_intro18 with dissolve
$ renpy.pause()
scene epi_intro13 with dissolve
mc "I went like that?"
scene epi_intro16 with dissolve
zo "Yeah, like you always do when you play something tricky."
scene epi_intro13 with dissolve
mc "Well, I don't remember what song it was."
scene epi_intro17 with dissolve
zo "But-"
scene epi_intro13 with dissolve
mc "And don't say I do."
scene epi_intro17b with dissolve
zo "*{i}Mumbles{/i}* You do, though."
scene epi_intro19 with dissolve
zo "Whatever. Beer?"
mc "Nah."
scene epi_intro24 with dissolve
zmom "No, I understand, but that doesn't explain-"
scene epi_intro25 with dissolve
zmom "Please, listen to me. She writes all of this down on a notepad on her walker."
zmom "She has perfect control over her meds. If you look in that notepad, you'll-"
scene epi_intro26 with dissolve
zmom "You did? No, that can't be."
zmom "Ok... I'll be there. No, it's fine. Yes, tomorrow."
scene epi_intro27 with dissolve
zmom "I'll have Bobby cover my shift."
zmom "Tell her I'm coming when she wakes up, ok? Bye."
scene epi_intro28 with dissolve
zo "What's wrong with Grandma?"
scene epi_intro29 with dissolve
zmom "Jesus. Zoey... You startled me."
scene epi_intro32 with dissolve
zo "What's wrong with her? Something happened, I can tell."
scene epi_intro29 with dissolve
zmom "Your grandma must have confused her medicine. Aunt Joline found her on the floor when she checked up on her."
if persistent.mod_wt_enabled:  
    $mod_choices = ["\n(Zoey CHICK)","\n(Zoey DIK)","","","","","","","","","","" ]
call screen zoey_choice_screen("Is she all right? [mod_gr][mod_choices[0]]",820,380, "What the fuck!? [mod_gr][mod_choices[1]]",750,100)
if tmp_choice == 1:
    $ zdik(-1)
    scene epi_intro32 with dissolve
    zo "Is she all right?"
    scene epi_intro30 with dissolve
    zmom "She's unconscious, but she's in good hands."
else:
    $ zdik(1)
    scene epi_intro32 with dissolve
    zo "No fucking way! What the hell happened?"
    scene epi_intro30 with dissolve
    zmom "They don't know yet."
zmom "She's in the hospital at the moment. They are doing some kind of tox screening to find out what she ate."
zmom "I'm going there tomorrow; I'll be taking a day off from work."
scene epi_intro33 with dissolve
zo "I'm going, too."
scene epi_intro31 with dissolve
zmom "No, you're not. You have school tomorrow morning."
scene epi_intro33 with dissolve

if persistent.mod_wt_enabled:  
    $mod_choices = ["\n{size=44}(Zoey CHICK)","\n{size=44}(Zoey DIK)","","","","","","","","","","" ]
#[mod_gr][mod_choices[0]]
call screen zoey_choice_screen("{size=-5}Nana is important!{/size}[mod_gr][mod_choices[0]]",500,100, "Fuck school![mod_gr][mod_choices[1]]",550,370)
if tmp_choice == 1:
    $ zdik(-1)
    zo "Come on, Mom! This is way more important than trigonometry!"
    scene epi_intro31 with dissolve
    zmom "This isn't negotiable. And everything will be fine."
else:
    $ zdik(1)
    zo "Fuck school! It's one fucking class."
    scene epi_intro31 with dissolve
    zmom "Language, Zoey..."
scene epi_intro34 with dissolve
zmom "Is that my beer?"
scene epi_intro35 with dissolve
zmom "How many times have I told you now?"
zmom "No alcohol in this house until you're 21."
scene epi_intro36 with dissolve
if persistent.mod_wt_enabled:  
    $mod_choices = ["\n{size=44}(Zoey CHICK)","\n{size=44}(Zoey DIK)","","","","","","","","","","" ]
    #[mod_gr][mod_choices[0]]
call screen zoey_choice_screen("Talk back[mod_gr][mod_choices[1]]",920,100, "Apologize[mod_gr][mod_choices[0]]",890,350)
if tmp_choice == 1:
    $ zdik(1)
    zo "You got some high hopes thinking I'll be here when I'm 21."
    scene epi_intro35 with dissolve
    zmom "Graduate, and then you can drink."
    scene epi_intro36 with dissolve
else:
    $ zdik(-1)
    zo "21? Really?"
    scene epi_intro35 with dissolve
    zmom "Graduate, and then you can drink."
    scene epi_intro36 with dissolve
    zo "All right, I'm sorry."
zo "Mom, listen. Fuck the beer. What about Grandma?"
scene epi_intro37 with dissolve
zmom "School comes first. I'll tell her you said hi."
scene epi_intro38 with dissolve
zo "Not \"hi\"..."
scene epi_intro39 with dissolve
zo "..."
stop music fadeout 3
scene epi_intro38 with dissolve
zo "Tell her I said, \"Love ya\"."
scene epi_intro40 with dissolve
$ renpy.pause()
play music "music/ep_interlude/licensed_music/track94.mp3"
scene epi_intro20 with dissolve
$ renpy.pause()
scene epi_intro22 with dissolve
mc "What's wrong?"
scene epi_intro21 with dissolve
$ guideSuggestedPage = 38
if persistent.mod_wt_enabled:  
    $mod_choices = ["\n{size=44}(Zoey CHICK)","\n{size=44}(Zoey DIK)","","","","","","","","","","" ]
    #[mod_gr][mod_choices[0]]
call screen zoey_choice_screen("Not your business[mod_gr][mod_choices[1]]",450,100, "Nothing[mod_gr][mod_choices[0]]",1350,100)
if tmp_choice == 1:
    $ zdik(1)
    zo "It's none of your business."
    scene epi_intro22 with dissolve
    mc "Ok, uh..."
else:
    $ zdik(-1)
    zo "Nothing."
    scene epi_intro22 with dissolve
mc "Was it this song?"
scene epi_intro23 with dissolve
zo "Yeah. See...?"
zo "You did know."
scene epi_intro23a with dissolve
$ renpy.pause(10)
show screen click_to_continue_screen with dissolve
$ renpy.pause(2)
hide screen click_to_continue_screen with dissolve
$ renpy.pause()

scene 2d_jacob_screen_main with dissolve
show screen episode_title_screen
$ renpy.pause(5)

label epi_zoey_pre_lewd_label:
scene epi_zoey_lewd1 with dissolve
$ renpy.pause()
scene epi_zoey_lewd2 with dissolve
zo "You're good at math, right?"
scene epi_zoey_lewd6 with dissolve
mc "I'm decent."
scene epi_zoey_lewd2 with dissolve
zo "Trigonometry. You know it?"
scene epi_zoey_lewd6 with dissolve
mc "In spring, I will. Is that the class you failed?"
scene epi_zoey_lewd3 with dissolve
zo "Yeah... My stumble on the finish line."
scene epi_zoey_lewd7 with dissolve
mc "You'll make it sometime. You're not in a rush anywhere, are you?"
scene epi_zoey_lewd4 with dissolve
zo "If I were... Would you come with me?"
scene epi_zoey_lewd7 with dissolve
mc "Where are we going?"
scene epi_zoey_lewd4 with dissolve
zo "I don't know. Somewhere hot, maybe? Miami?"
scene epi_zoey_lewd7 with dissolve
mc "What's in Miami?"
scene epi_zoey_lewd5 with dissolve
zo "Beaches and parties, duh."
scene epi_zoey_lewd6 with dissolve
mc "Sounds fun. I'm in."
scene epi_zoey_lewd5 with dissolve
zo "You're not in."
scene epi_zoey_lewd7 with dissolve
mc "I am."
scene epi_zoey_lewd4 with dissolve
zo "What about college?"
scene epi_zoey_lewd7 with dissolve
mc "Yeah, but don't they have that there?"
scene epi_zoey_lewd4 with dissolve
zo "Yeah, probably."
zo "Can we eat at your place tonight?"
scene epi_zoey_lewd6 with dissolve
mc "Didn't your mom come home yet?"
scene epi_zoey_lewd8 with dissolve
zo "She said she was gonna be gone for a day, but who knows?"
zo "She's prolly only making sure Grandma's ok."
scene epi_zoey_lewd6 with dissolve
mc "And your dad?"
scene epi_zoey_lewd9 with dissolve
zo "Stepdad, dude. I hate when you call him \"Dad\"."
scene epi_zoey_lewd7 with dissolve
mc "It's easier to say."
scene epi_zoey_lewd9 with dissolve
zo "Call him Floyd, then."
zo "He's hauling cargo somewhere. Who cares where he is?"
scene epi_zoey_lewd7 with dissolve
mc "Anyway... We can eat at my place tonight. I'll let Dad know."
label epi_zoey_lewd_label:
if _in_replay:
    if persistent.name == None:
        $ name = "MC"
    else:
        $ name = persistent.name
    $ affinity = "NEUTRAL"
    play music "music/ep_interlude/licensed_music/track94.mp3"
scene epi_zoey_lewd4 with dissolve
zo "Do that later. We got the house to ourselves for once. Wanna go crazy?"
scene epi_zoey_lewd7 with dissolve
mc "Crazy how?"
scene epi_zoey_lewd4 with dissolve
zo "Off the top of my head, I'm thinking we put some ShitFaced on and dilute another one of Mom's bottles."
scene epi_zoey_lewd7 with dissolve
mc "I don't think it would be a great idea to show up to dinner drunk. Dad would probably tell Alison we'd been drinking."
scene epi_zoey_lewd10 with dissolve
if persistent.mod_wt_enabled:  
    $mod_choices = ["\n{size=44}(Zoey CHICK)","\n{size=44}(Zoey DIK)","","","","","","","","","","" ]
    #[mod_gr][mod_choices[0]]
call screen zoey_choice_screen("What a snitch[mod_gr][mod_choices[1]]",1450,350, "You're right[mod_gr][mod_choices[0]]",1400,100)
if tmp_choice == 1:
    $ zdik(1)
    zo "Neil's such a snitch."
    if affinity == "DIK":
        scene epi_zoey_lewd7 with dissolve
        mc "Fuck you."
        scene epi_zoey_lewd4 with dissolve
        zo "Hey, mellow. He's the best; I was joking."
    else:
        scene epi_zoey_lewd6 with dissolve
        mc "Name a parent who isn't."
        scene epi_zoey_lewd4 with dissolve
        zo "I wouldn't be. I'd let my kid do whatever they wanted."
        scene epi_zoey_lewd6 with dissolve
        mc "That doesn't sound completely right."
        scene epi_zoey_lewd4 with dissolve
        zo "Whatever..."
else:
    $ zdik(-1)
    zo "You're probably right about that."
    zo "Parents got such boners for rules, but you bet your ass they didn't follow them when they were young."
    scene epi_zoey_lewd6 with dissolve
    mc "Maybe they want us to be better than they were?"
    scene epi_zoey_lewd4 with dissolve
    zo "Wishful thinking. Oh, well..."
zo "No drinking it is."
zo "What about metal and fuck?"
scene epi_zoey_lewd11 with dissolve
mc "Shit... You're right... No one's at home."
scene epi_zoey_lewd10 with dissolve
zo "You can moan loudly for once."
scene epi_zoey_lewd12 with dissolve
mc "Yeah, because that's {b}so{/b} hot..."
scene epi_zoey_lewd10 with dissolve
zo "I wanna hear you do it. You're always so quiet."
zo "It's like you're not having fun or something."
scene epi_zoey_lewd12 with dissolve
mc "You're joking again, I hope."
stop music fadeout 3
scene epi_zoey_lewd13 with dissolve
zo "Prove it. If the music's louder than your moans, you lose."
scene epi_zoey_lewd14 with dissolve
play music "music/ep_interlude/licensed_music/track95.mp3"
queue music ["music/ep_interlude/licensed_music/track96.mp3","music/ep_interlude/licensed_music/track95.mp3"]
$ renpy.pause()
scene epi_zoey_lewd15 with dissolve
mc "HAHA! TURN IT DOWN A NOTCH!"
scene epi_zoey_lewd16 with dissolve
zo "MOAN FOR ME!"
scene epi_zoey_lewd17 with dissolve
mc "*{i}MOAN{/i}*"
scene epi_zoey_lewd19 with dissolve
zo "HAHA! What the fuck was that?"
zo "Are you turned on or imitating a cow?"
scene epi_zoey_lewd18 with dissolve
mc "Way to help me feel sexy about it..."
scene epi_zoey_lewd20 with dissolve
zo "Come on, baby. Go like this..."
scene epi_zoey_lewd21 with dissolve
zo "*Moans* Uhnnn hnnn..."
scene epi_zoey_lewd22 with dissolve
mc "Fuck, that's hot."
scene epi_zoey_lewd23 with dissolve
$ renpy.pause()
scene epi_zoey_lewd24 with dissolve
mc "Haha, my pants just got tighter."
scene epi_zoey_lewd25 with dissolve
zo "Fucking remove them, then. Don't expect me to drop my panties until I see my meaty friend."
scene epi_zoey_lewd26 with dissolve
mc "Drop them a little bit while I undress?"
scene epi_zoey_lewd27 with dissolve
zo "Like this...?"
scene epi_zoey_lewd28 with dissolve
mc "Keep going..."
scene epi_zoey_lewd29 with dissolve
zo "You better lose that underwear now."
mc "They're off..."
scene epi_zoey_lewd30 with dissolve
zo "Awesome..."
scene epi_zoey_lewd31 with dissolve
zo "Now, where's my moan?"
scene anim_zoey_tease_epi with dissolve
mc "*{i}Moan{/i}*"
zo "Haha, ok, you don't have to moan."
mc "Hey, I'm trying here."
zo "I know you are, baby. How about if you talk dirty to me instead?"
pause
scene anim_zoey_tease2_epi with dissolve
mc "Um..."
zo "What's wrong?"
mc "Nothing."
zo "It's not about last time, is it?"
mc "You laughed at me; that leaves scars."
zo "I didn't laugh at you. It just took me by surprise."
pause
scene anim_zoey_tease3_epi with dissolve
zo "I think it's so hot that you finally say what you like in bed. That's what a girl wants to hear, you know?"
zo "We want you to tell us what you like and take charge."
mc "It's just embarrassing."
zo "Embarrassing? We're both completely nude. And look at yourself. You don't have anything to be embarrassed about."
zo "I swear you could rule the world with this thing if you just grew some bigger balls to go with it."
mc "Haha! Ok, I'll try to do better."
zo "You're always doing great; just talk more to me."
pause

call screen zoey_choice_screen("Blowjob",400,100, "Eat me",1250,100)

if tmp_choice == 1:
    zo "I wanna give you a blowjob, [name]. I wanna suck your dick and feel it all around in my mouth."
    zo "I wanna have my tongue massage the head as I bop my head up and down."
    mc "Yeah! I want that too. Do that."
    zo "Do what? Say it..."
    mc "Suck my cock, Zoey..."
    zo "Mmm... There you go!"
    label epi_z_sex_choice1_label:
    scene anim_zoey_bj1_epi with dissolve
    zo "*{i}Suck suck{/i}*"
    mc "Hnnn... Keep going. You know just how to do that."
    zo "*{i}Suck suck{/i}* Mhm... Mmm..."
    pause
    scene anim_zoey_bj2_epi with dissolve
    mc "I always like how wet you get. It never feels like I'm the only one who is horny with you."
    zo "*{i}Schlurp{/i}* You make it easy to get turned on, [name]. You have a gift."
    pause
    scene anim_zoey_bj3_epi with dissolve
    zo "*{i}Suck glug{/i}*"
    zo "(This cock... I swear, I can't get enough of it.)"
    pause
    call screen zoey_choice_screen("Eat me",1300,100, "Continue",1400,350)
    if tmp_choice == 1:
        zo "*{i}Suck suck{/i}* Tell me you wanna eat me."
        mc "I want to eat you, Zoey."
        jump epi_z_sex_choice2_label
else:

    zo "I want you to eat me, [name]. Put your fat tongue to use all over my pussy."
    zo "I want to feel your warm breath against me as you dig in like it's your last meal."
    mc "Yes! I want that too. Let's do that."
    zo "Let's do what? Say it..."
    mc "I want to lick your pussy, Zoey."
    zo "Yes! That's it. Keep talking like that to me."
    label epi_z_sex_choice2_label:
    scene anim_zoey_cunn1_epi with dissolve
    mc "*{i}Lick lick{/i}*"
    zo "*{i}Moans{/i}* Yes! Eat me, [name]."
    zo "That's the spot. Remember what I taught you."
    pause
    scene anim_zoey_cunn2_epi with dissolve
    zo "Fuck... You're getting so good at this."
    zo "Who've you been training on?"
    mc "*{i}Lick lick{/i}* Haha, no one."
    zo "You sure? I know Lisa's been eyeing you."
    mc "Yeah, right."
    pause
    call screen zoey_choice_screen("Blowjob",1200,700, "Continue",1500,800)
    if tmp_choice == 1:
        zo "I wanna suck your cock, [name]..."
        mc "*{i}Lick lick{/i}* Ok. Come over here and do it."
        jump epi_z_sex_choice1_label

scene epi_zoey_lewd32 with dissolve
zo "Put your cock inside me, baby. Go slowly..."
scene epi_zoey_lewd33 with dissolve
zo "*{i}Moans{/i}*"
scene epi_zoey_lewd34 with dissolve
mc "Fuck... It feels so good..."
mc "The best part is knowing we're alone."
zo "Don't jinx it."
mc "I'm not."
scene anim_zoey_side1_epi with dissolve
zo "*{i}Smack{/i}* Mhm..."
zo "(I love how he takes charge and holds my hand still.)"
zo "(He's gentle, but it feels like he's doing what he wants now.)"
pause
scene anim_zoey_side2_epi with dissolve
zo "It's always so insane to me that you're only halfway in now."
mc "Haven't you gotten used to it?"
zo "I'm not sure you can ever get used to it. Knowing there's more to push in is hot as fuck to me."
pause
scene anim_zoey_side3_epi with dissolve
mc "*{i}Smack{/i}* Are you ready for the rest of me?"
zo "Not yet... I really like this. Keep going."
pause
scene anim_zoey_side4_epi with dissolve
zo "*{i}Smack{/i}*"
zo "(He's such a good kisser. I shouldn't blow his ego up too much, though. I don't want him to become a douche.)"
pause
call screen zoey_choice_screen("Doggystyle",100,100, "{size=-%d}Let him take control{/size}" % (10 * persistent.scale_factor),150,400)
scene epi_zoey_lewd35 with dissolve
zo "Ok, I'm ready for it."
if tmp_choice == 1:
    zo "Give it to me from behind, baby."
    label epi_z_sex_choice3_label:
    scene epi_zoey_lewd36 with dissolve
    mc "You have such a great ass."
    zo "I know you like it, but it never gets tiring to hear it."
    scene anim_zoey_doggy1_epi with dissolve
    zo "*{i}Moans{/i}* Yes! Fuck me, [name]! Harder!"
    mc "Yes! I'm gonna fuck you hard, Zoey."
    zo "That's it! Talk to me."
    pause
    scene anim_zoey_doggy2_epi with dissolve
    mc "I love watching your ass jiggle like that."
    zo "Nice! You're getting better at this."
    zo "Fuck me. Use me. I'm yours, [name]."
    pause
    call screen zoey_choice_screen("{size=-%d}Let him take control{/size}" % (10 * persistent.scale_factor),300,100, "Continue",1250,100)
    if tmp_choice == 1:
        jump epi_z_sex_choice4_label
else:
    zo "How do you want me?"
    label epi_z_sex_choice4_label:
    scene epi_zoey_lewd37 with dissolve
    zo "You want me in your lap? What's this?"
    scene epi_zoey_lewd38 with dissolve
    mc "It's something new I came up with."
    scene anim_zoey_ride1_epi with dissolve
    zo "*{i}Moans{/i}* Oh, damn! Fuck!"
    mc "*{i}Suck suck{/i}* Do you like it?"
    zo "Fuck yeah! It's so hot how you lift me up and down. You're so strong!"
    pause
    scene anim_zoey_ride2_epi with dissolve
    zo "Mmm... Your cock is hitting all the right places."
    zo "Go easier on my nipple, though."
    mc "Mmphff... Sorry."
    zo "It's fine; just don't suck on it too hard."
    pause
    call screen zoey_choice_screen("Doggystyle",50,100, "Continue",100,400)
    if tmp_choice == 1:
        zo "[name]... Fuck me from behind..."
        jump epi_z_sex_choice3_label

scene anim_zoey_miss1_epi with dissolve
zo "Yes! *{i}Moans{/i}* Give all of it to me!"
zo "Show me what you're made of."
pause
scene anim_zoey_miss2_epi with hpunch
zo "*{i}Moans{/i}* Ahhh!!! [name]!!! I'm coming!!!"
mc "(Damn, that's hot. I can feel how she's trembling down there.)"
mc "(Everything got wetter and hotter just now...)"
pause
scene anim_zoey_miss3_epi with dissolve
mc "Zoey... I..."
zo "What is it, baby? Tell me."
mc "I'm getting really close..."
zo "Cum for me, baby."
pause
call screen zoey_choice_screen("Cum inside",100,40, "Cum outside",1500,40)
if tmp_choice == 1:
    zo "Cum inside of me. I know how much you like that."
    mc "Ok... I'm gonna do it..."
    zo "My pussy wants it, [name]. Cum!"
    scene epi_zoey_lewd39 at vpunch, cum2
    $ renpy.pause(0.5)
    scene epi_zoey_lewd39 at vpunch, cum2
    $ renpy.pause(0.5)
    scene epi_zoey_lewd39 at vpunch, cum2
    mc "Ahhh!!!"
    scene epi_zoey_lewd40 with dissolve
    zo "Wow... There you go."
else:
    zo "Cum outside this time."
    mc "Where?"
    zo "Wherever you want to."
    scene epi_zoey_lewd41 at vpunch, cum2
    $ renpy.pause(0.5)
    scene epi_zoey_lewd41 at vpunch, cum2
    $ renpy.pause(0.5)
    scene epi_zoey_lewd41 at vpunch, cum2
    mc "Ahhh!!!"
    scene epi_zoey_lewd42 with dissolve
    zo "Dude, that's so much cum. You haven't fapped in a while, have you?"
    mc "Haha, two days ago, maybe?"
    zo "Damn, only two days?"

scene epi_zoey_lewd43 with dissolve
zo "You suck at moaning, but with that happy stick, who the fuck cares?"
scene epi_zoey_lewd44 with dissolve
mc "Thanks, I guess."
scene epi_zoey_lewd43 with dissolve
zo "Beer?"
scene epi_zoey_lewd45 with dissolve
mc "We can't be drunk if we're going to my place, remember?"
scene epi_zoey_lewd46 with dissolve
zo "You fuckin' lightweight. I said beer, not shots."
scene epi_zoey_lewd45 with dissolve
mc "Still... I'll pass."
scene epi_zoey_lewd46 with dissolve
zo "Well, I'm getting one."
stop music fadeout 3
$ renpy.end_replay()
$ persistent.epi_lewd_zoey = True
$ calcScenes()

scene epi_zoey_after_lewd1 with dissolve
$ renpy.pause()
scene epi_zoey_after_lewd2 with dissolve
zo "Haha... He mooed like a cow. Hilarious."
scene epi_zoey_after_lewd3 with dissolve
zo "Oh... Mom."
zo "You're back?"
scene epi_zoey_after_lewd7 with dissolve
zmom "Zoey..."
scene epi_zoey_after_lewd4 with dissolve
zo "The beer? I know, I suck. I'm-"
play music "music/ep_interlude/licensed_music/track97.mp3"
scene epi_zoey_after_lewd8 with dissolve
zmom "Grandma passed away."
scene epi_zoey_after_lewd5 with dissolve
$ renpy.pause()
scene epi_zoey_after_lewd6 with dissolve
zo "Nana's dead?"
scene epi_zoey_after_lewd9 with dissolve
$ renpy.pause()
scene epi_zoey_after_lewd10 with dissolve
zo "No... No. But you said... You said everything was all right."
scene epi_zoey_after_lewd12 with dissolve
zmom "I know. I'm so sorry!"
scene epi_zoey_after_lewd11 with dissolve
$ renpy.pause()

label epi_zoey_grandma_label:
scene epi_zoey_grandma1 with fade
pri "Doris was a warm and gentle spirit. She was undoubtedly loved by everyone here today."
scene epi_zoey_grandma4 with dissolve
pri "When someone dear passes, we're left with many questions and a void that only they could fill."
scene epi_zoey_grandma5 with dissolve
pri "As long as you keep memories of Doris, she's never truly gone."
scene epi_zoey_grandma3 with dissolve
$ renpy.pause()
scene epi_zoey_grandma16 with dissolve
zo "NANA! NANA! LOOK!"
scene epi_zoey_grandma18 with dissolve
do "I'm watching, dear. What are you playing today?"
scene epi_zoey_grandma17 with dissolve
zo "I'm surfing!"
scene epi_zoey_grandma18 with dissolve
do "Is that right? How does that work?"
scene epi_zoey_grandma17 with dissolve
zo "You have a board that you stand on like this!"
zo "And you try to stay on it, and then there are big waves that come from everywhere!"
scene epi_zoey_grandma18 with dissolve
do "I think that sounds super. Are you going to be a surfer when you grow up?"
scene epi_zoey_grandma17 with dissolve
zo "Yes! I'm gonna be the best!"
scene epi_zoey_grandma6 with dissolve
zmom "Happy birthday, sweetie!"
scene epi_zoey_grandma7 with dissolve
zmom "It's a sweater, and I know you said you didn't want any clothes..."
zmom "But the ones you wear have holes in them, so I thought you could use it."
scene epi_zoey_grandma8 with dissolve
zo "Thanks, Mom..."
scene epi_zoey_grandma9 with dissolve
do "And this one is from Albert and me. Bless his heart. I know he would want to be here with us today, and I think he is looking down at you and smiling."
do "You've grown up to be such a wonderful spirit."
scene epi_zoey_grandma11 with dissolve
sdad "That doesn't describe someone struggling in school and frequently getting detention."
scene epi_zoey_grandma12 with dissolve
zmom "Not today. Please."
scene epi_zoey_grandma10 with dissolve
do "Wonderful. And don't you forget it."
scene epi_zoey_grandma13 with dissolve
zo "Wow! A skateboard!"
scene epi_zoey_grandma10 with dissolve
do "It's not quite a surfboard, but the store clerk assured me it was a good way to start for a young girl."
scene epi_zoey_grandma11 with dissolve
sdad "A surfboard? This again..."
sdad "It's not an occupation, Zoey. It's a hobby at best."
scene epi_zoey_grandma15 with dissolve
zo "Yeah? And a truck just goes back and forth between places."
zo "Tell me again. How did school do you any good!?"
scene epi_zoey_grandma12 with dissolve
zmom "I said not today."
scene epi_zoey_grandma10 with dissolve
do "Don't listen to him. You can make it into whatever you set your mind to."
scene epi_zoey_grandma14 with dissolve
zo "Love ya, Nana."
stop music fadeout 20
scene epi_zoey_grandma2 with dissolve
$ renpy.pause()

label epi_sadness_label:
$ renpy.sound.play("sound_effects/rain_inside.mp3", channel="sfx1", loop=True)
scene epi_sadness1 with dissolve
$ renpy.pause()
scene epi_sadness2 with dissolve
$ renpy.pause()
scene epi_sadness3 with dissolve
$ renpy.pause()
scene epi_sadness4 with dissolve
$ renpy.pause()
scene epi_sadness5 with dissolve
zmom "Zoey? You have to eat something."
if persistent.mod_wt_enabled:  
    $mod_choices = ["\n{size=44}(Zoey CHICK)","\n{size=44}(Zoey DIK)","","","","","","","","","","" ]
#[mod_gr][mod_choices[0]]
call screen zoey_choice_screen("Answer[mod_gr][mod_choices[0]]",1270,320, "Ignore[mod_gr][mod_choices[1]]",1200,80)

if tmp_choice == 1:
    $ zdik(-1)
    scene epi_sadness6b with dissolve
    zo "I'm not hungry."
    scene epi_sadness5 with dissolve
    zmom "You might feel that way, but eating will be good for you."
    zmom "Have a few bites, at least."
else:
    $ zdik(1)
    scene epi_sadness6 with dissolve
    zo "..."
    scene epi_sadness6c with dissolve
    zmom "..."

scene epi_sadness7 with dissolve
zmom "[name] was here before when you were asleep. He wanted you to have these."
zmom "I'll put them on your desk."
scene epi_sadness8 with dissolve
$ renpy.pause(1)
scene epi_sadness9 with dissolve
$ renpy.pause()
scene epi_sadness10 with dissolve
$ renpy.pause()
scene epi_sadness11 with dissolve
$ renpy.pause()
scene epi_sadness12 with dissolve
$ renpy.pause()
scene epi_sadness13 with dissolve
$ renpy.pause()
scene epi_sadness14 with dissolve
$ renpy.pause()
$ renpy.music.stop(channel="sfx1", fadeout=3)
scene epi_sadness15 with dissolve
$ renpy.pause()

label epi_leaving_label:
scene epi_leaving1 with fade
play music "music/ep7/licensed_music/track48.mp3"
$ renpy.pause()
scene anim_leaving_skate_epi with dissolve
$ renpy.pause()
scene epi_leaving2 with dissolve
$ renpy.pause()
scene epi_leaving3 with dissolve
zo "Are you sure you can't come? Just...hop on the train with me."
scene epi_leaving4 with dissolve
mc "I want to, but I can't. I wanna graduate first..."
scene epi_leaving5 with dissolve
zo "..."
mc "And you can't wait until next summer?"
scene epi_leaving6 with dissolve
zo "[name]... I can't find it in me to finish that class."
zo "I don't feel anything anymore..."
zo "I need to do this."
scene epi_leaving5 with dissolve
mc "For your grandma?"
scene epi_leaving6 with dissolve
zo "She was the only one who believed in me and my dreams."
zo "It's for her, but it's also for me."
zo "I need to feel something again."
scene epi_leaving7 with dissolve
mc "I understand..."
play sound "sound_effects/interlude/train_stop.mp3"
scene epi_leaving8 with dissolve
$ renpy.pause()
scene epi_leaving12 with dissolve
zo "So... That's my ride."
scene epi_leaving13 with dissolve
mc "Yeah..."
mc "How do we do this?"
scene epi_leaving14 with dissolve
zo "I don't know. I suck at goodbyes."
zo "Casual wave?"
scene epi_leaving15 with dissolve
$ renpy.pause()
scene epi_leaving16 with dissolve
zo "Or this..."
scene epi_leaving17 with dissolve
$ renpy.pause()
scene epi_leaving18 with dissolve
mc "Just so you know..."
mc "Your grandma isn't the only one who believes in you."
scene epi_leaving19 with dissolve
zo "..."
scene epi_leaving20 with dissolve
mc "Let me know when you get there."
scene epi_leaving21 with dissolve
zo "Yeah, I will. And if you see Mom, once in a while..."
scene epi_leaving20 with dissolve
mc "I'll drop by and talk to her from time to time."
scene epi_leaving21 with dissolve
if persistent.mod_wt_enabled:  
    $mod_choices = ["\n{size=44}(Zoey CHICK)","\n{size=44}(Zoey DIK)","","","","","","","","","","" ]
#[mod_gr][mod_choices[0]]
call screen zoey_choice_screen("Appreciate it[mod_gr][mod_choices[0]]",1450,350, "Don't have to[mod_gr][mod_choices[1]]",1400,100)
if tmp_choice == 1:
    $ zdik(-1)
    zo "Thanks... I really appreciate that."
    scene epi_leaving20 with dissolve
    mc "It's not a problem."
else:
    $ zdik(1)
    zo "You don't have to do that. A simple hi is enough."
    scene epi_leaving20 with dissolve
    mc "No, I want to."
scene epi_leaving25 with dissolve
$ renpy.pause()
scene epi_leaving25b with dissolve
$ renpy.pause()
play sound "sound_effects/interlude/train_leave.mp3"
scene epi_leaving25c with dissolve
$ renpy.pause()
scene epi_leaving26 with dissolve
$ renpy.pause()
stop music fadeout 3
$ renpy.sound.play("sound_effects/interlude/train_ride.mp3", channel="sfx1", loop=True)
scene epi_leaving27 with dissolve
zo "Shitballs..."
scene epi_leaving28 with dissolve
$ renpy.pause()
scene epi_leaving29 with dissolve
$ renpy.pause()
scene epi_leaving30 with dissolve
$ renpy.music.stop(channel="sfx1", fadeout=3)
play music "music/ep_interlude/licensed_music/track98.mp3"
$ renpy.pause()
scene anim_train_ride_epi with dissolve
pause
scene epi_leaving31 with dissolve
$ renpy.pause()
scene epi_leaving32 with dissolve
if minigames:
    $ renpy.pause(0.5)
    scene zoey_drawing_tutorial with dissolve
    $ renpy.pause()
    scene epi_leaving32 with dissolve
    jump epi_drawing_game1_label
    label epi_after_drawing1_label:
else:
    $ renpy.pause()
    scene epi_leaving33 with dissolve
    $ renpy.pause()
scene epi_leaving34 with dissolve
$ renpy.pause()
scene epi_leaving35 with dissolve
$ renpy.pause()
scene epi_leaving36 with dissolve
cn "Ticket, please."
scene epi_leaving37 with dissolve
$ renpy.pause()
scene epi_leaving38 with dissolve
show screen notebook_button_screen
call screen notebook_tutorial_screen
scene epi_leaving38 with dissolve
$ renpy.pause()
scene epi_leaving39 with dissolve
$ renpy.pause()
$ text_message_screen_list = []
$ text_message_screen_list.append(["Zoey","Train's rolling fine. It's a start.",False])
$ text_message_screen_list.append(["%s" % name,"Now would be a good time to remember that you forgot to pack something.",True])
$ tmpInt = 0
show screen text_message_screen
$ renpy.pause()
play sound "sound_effects/interlude/zoey_message.mp3"
$ tmpInt += 1
$ renpy.pause(1)
if persistent.mod_wt_enabled:  
    $mod_choices = ["\n{size=44}(Zoey CHICK)","\n{size=44}(Zoey DIK)","","","","","","","","","","" ]
#[mod_gr][mod_choices[0]]
call screen zoey_choice_screen("LOL! Asshole![mod_gr][mod_choices[1]]",1450,350, "Don't scare me[mod_gr][mod_choices[0]]",1400,100)
if tmp_choice == 1:
    $ zdik(1)
    $ text_message_screen_list.append(["Zoey","LOL! Asshole!",False])
else:
    $ zdik(-1)
    $ text_message_screen_list.append(["Zoey","LOL! Don't scare me like that!",False])
scene epi_leaving40 with dissolve
$ tmpInt += 1
$ renpy.pause()
hide screen text_message_screen

$ tmpInt = 0
$ text_message_screen_list = []
$ text_message_screen_list.append(["Zoey","As long as I've got my wallet, phone, and notebook, anything that I missed I can live without.",False])
$ text_message_screen_list.append(["%s" % name,"Ok.",True])
$ text_message_screen_list.append(["Zoey","I'll probably freak out if my charger's missing, though...",False])
$ text_message_screen_list.append(["Zoey","I guess I can get a new one if I forgot it.",False])
$ text_message_screen_list.append(["%s" % name,"Yeah.",True])
show screen text_message_screen
$ renpy.pause()
scene epi_leaving41 with dissolve
$ tmpInt += 1
$ renpy.pause()
$ tmpInt += 1
$ renpy.pause()
$ tmpInt += 1
$ renpy.pause()
$ tmpInt += 1
scene epi_leaving42 with dissolve
$ renpy.pause(1)
if persistent.mod_wt_enabled:  
    $mod_choices = ["\n{size=44}(Zoey CHICK)","\n{size=44}(Zoey DIK)","","","","","","","","","","" ]
#[mod_gr][mod_choices[0]]
call screen zoey_choice_screen("You ok?[mod_gr][mod_choices[0]]",1450,350, "I'm excited![mod_gr][mod_choices[1]]",1400,100)
hide screen text_message_screen
if tmp_choice == 1:
    $ zdik(-1)
    $ tmpInt = 0
    $ text_message_screen_list = []
    $ text_message_screen_list.append(["Zoey","You ok?",False])
    $ text_message_screen_list.append(["%s" % name,"I'm fine. Kinda difficult to type right now.",True])
    $ text_message_screen_list.append(["Zoey","Not home yet?",False])
    $ text_message_screen_list.append(["%s" % name,"I'm walking.",True])
    $ text_message_screen_list.append(["Zoey","Haha. You never could do two things at once.",False])
else:
    $ zdik(1)
    $ tmpInt = 0
    $ text_message_screen_list = []
    $ text_message_screen_list.append(["Zoey","I'm so fucking excited about this!",False])
    $ text_message_screen_list.append(["%s" % name,"I'm happy for you.",True])
    $ text_message_screen_list.append(["Zoey","Thanks. I knew you'd understand. You're the best.",False])
    $ text_message_screen_list.append(["%s" % name,"=)",True])
    $ text_message_screen_list.append(["Zoey","Talk soon!",False])

scene epi_leaving27b with dissolve
show screen text_message_screen
$ renpy.pause()
scene epi_leaving28b with dissolve
$ tmpInt += 1
$ renpy.pause()
$ tmpInt += 1
$ renpy.pause()
$ tmpInt += 1
$ renpy.pause()
$ tmpInt += 1
$ renpy.pause()
hide screen text_message_screen
scene epi_leaving29b with dissolve
$ renpy.pause()

stop music fadeout 3
scene epi_leaving27b with dissolve
$ tmpInt = 0
$ text_message_screen_list = []
$ text_message_screen_list.append(["Zoey","l8r sk8r",False])
show screen text_message_screen
$ renpy.pause()
hide screen text_message_screen

label epi_san_diego_label:
play music "music/ep_interlude/licensed_music/track99.mp3"
scene epi_san_diego1 with dissolve
zo "{i}San Diego...{/i}"
zo "{i}Everyone's last guess to where you're going when you say you're heading to California.{/i}"
zo "{i}Hey, it's still California! It's cheaper than LA, but you get the same waves, if not better.{/i}"
zo "{i}Maybe it's bullshit, but that's what the website said.{/i}"
scene epi_san_diego2 with dissolve
zo "{i}The first question my friends asked me was if I was going to Tijuana.{/i}"
zo "{i}I heard there's a crossing near the border that's one-way only. Drive down that road, and you're fucked - or you're going to Mexico - whichever way you'd rather look at it.{/i}"
zo "{i}And to answer their question... No, I don't plan on visiting Mexico.{/i}"
zo "{i}Then again, I didn't plan to come here either. It just kinda happened.{/i}"
scene epi_san_diego3 with dissolve
zo "{i}Grandma... You shouldn't have left me that money. All of your savings will go to waste because of me.{/i}"
zo "{i}Well, at least the part that you gave to me. I can't believe I got more than Joline...{/i}"
zo "{i}The look on her face was...uh... Never mind...{/i}"
zo "{i}You always encouraged me with my dreams... And dreams do cost money.{/i}"
scene epi_san_diego4 with dissolve
zo "{i}I promise to make that money last as long as I can. I'm not here for a vacation.{/i}"
zo "{i}I just need to...{/i}"
zo "{i}Find some purpose in life.{/i}"
zo "{i}And also, to fucking find out if my awesome skateboarding skills translate to a board with no wheels cruising big-ass ocean waves.{/i}"
scene epi_san_diego5 with dissolve
zo "{i}I couldn't have picked a better month to come here. Surfing season is here!{/i}"
zo "{i}It'll last until November. That gives me time to figure it out.{/i}"
zo "{i}The best part of it all...is the freedom.{/i}"
zo "{i}I love her, but Mom's rules never did anything good for me.{/i}"
scene epi_san_diego6 with dissolve
zo "{i}Now, this is Freedom. Capital F.{/i}"
zo "{i}Alone in a new city.{/i}"
zo "{i}No Mom here to tell me what I can't do.{/i}"
stop music
scene epi_san_diego7
host "No alcohol."
scene epi_san_diego8 with dissolve
zo "'scuse me, can you repeat that?"
play music "music/ep_interlude/licensed_music/track100.mp3"
scene epi_san_diego7 with dissolve
host "You cannot drink unless you're 21. That cannot be news to you, darling."
if persistent.mod_wt_enabled:  
    $mod_choices = ["\n{size=44}(Zoey CHICK)","\n{size=44}(Zoey DIK)","","","","","","","","","","" ]
#[mod_gr][mod_choices[0]]
call screen zoey_choice_screen("I am 21",450,100, "{size=-%d}Drink in my room{/size}" % (5 * persistent.scale_factor),1350,100)
scene epi_san_diego8 with dissolve
if tmp_choice == 1:
    $ zdik(1)
    zo "But I am 21."
    scene epi_san_diego7 with dissolve
    host "If that's not the case, it's going to get awkward when I ask for your ID in a minute."
    scene epi_san_diego9 with dissolve
    zo "Fuck..."
else:
    $ zdik(-1)
    zo "What if I do it in my room?"
    scene epi_san_diego7 with dissolve
    host "No, that's prohibited too."
    scene epi_san_diego9 with dissolve
    zo "Ugh..."

show epi_san_diego11_nocard
if not persistent.epi_card1:
    show screen epi_render_screen("1")
with dissolve
host "You'll have to wear this red wristband when you're in the bar, and we have a collaboration with other hostels and bars in the area..."
host "...so, my advice is to always keep that wristband on."
show epi_san_diego10
hide screen epi_render_screen
with dissolve
zo "Shitballs..."
scene epi_san_diego12 with dissolve
$ renpy.pause()
scene epi_san_diego13 with dissolve
$ renpy.pause()
scene epi_san_diego14 with dissolve
$ renpy.pause()
scene epi_san_diego15 with dissolve
zo "(I'm finally here...)"
zo "(I need to find some fucking friends who can score me beer.)"
scene epi_san_diego16 with dissolve
$ text_message_screen_list = []
$ text_message_screen_list.append(["Zoey","The train didn't derail. I'm safe and sound, livin' life in SD.",False])
$ text_message_screen_list.append(["%s" % name,"That's good news. Found the hostel ok?",True])
$ text_message_screen_list.append(["Zoey","Yep. It's a hostel, all right - or was it a prison? I keep forgetting since I have to wear this fucking wristband when I'm here.",False])
$ text_message_screen_list.append(["%s" % name,"A wristband? What for?",True])
$ text_message_screen_list.append(["Zoey","Drinking rules. Green wristband says you can party. Red says your life still sucks. Mine's red.",False])
$ tmpInt = 0
show screen text_message_screen
$ renpy.pause()
play sound "sound_effects/interlude/zoey_message.mp3"
$ tmpInt += 1
$ renpy.pause()
$ tmpInt += 1
$ renpy.pause()
$ tmpInt += 1
scene epi_san_diego17 with dissolve
$ renpy.pause()
$ tmpInt += 1
$ renpy.pause()
hide screen text_message_screen

$ text_message_screen_list = []
$ text_message_screen_list.append(["%s" % name,"You'll figure it out.",True])
$ text_message_screen_list.append(["Zoey","True that.",False])
$ text_message_screen_list.append(["%s" % name,"How's the hostel?",True])
$ text_message_screen_list.append(["Zoey","Cleaner than both of our rooms. It has a weird smell, though.",False])
$ text_message_screen_list.append(["Zoey","I have to share the room with whoever drops by. Kinda lame. Need to find something more...solitary.",False])
$ tmpInt = 0
scene epi_san_diego18 with dissolve
show screen text_message_screen
$ renpy.pause()
$ tmpInt += 1
$ renpy.pause()
$ tmpInt += 1
$ renpy.pause()
$ tmpInt += 1
$ renpy.pause()
$ tmpInt += 1
$ renpy.pause()
hide screen text_message_screen

$ text_message_screen_list = []
$ text_message_screen_list.append(["%s" % name,"It's your first day. I'm sure you will.",True])
$ text_message_screen_list.append(["Zoey","Aight. I'm gonna check out the neighborhood. l8r sk8ter",False])
$ tmpInt = 0
show screen text_message_screen
$ renpy.pause()
$ tmpInt += 1

$ renpy.pause()
hide screen text_message_screen

label epi_surf_label:
scene epi_surf1 with dissolve
zo "{i}Surfing class - day one... It's...uh... It's something.{/i}"
zo "{i}You know when you get taught how to ski, and they tell you to either go \"pizza\" or \"French fries\" to learn how to position your skis?{/i}"
scene epi_surf2 with dissolve
zo "{i}When you surf, you go \"banana\". It's kind of the first state used when you paddle.{/i}"
zo "{i}We didn't start off in the water, though. You start learning on land. We barely got wet during the first lesson.{/i}"
zo "{i}We learned about paddling, the surfboard anatomy, popping up to stand on the board, and the surfing stance. All of this we got taught on the sand.{/i}"
scene epi_surf3 with dissolve
zo "{i}The instructor also taught us about setup, dangers, tides, flags, and a shitload of other information...{/i}"
zo "{i}Surprisingly little was actually about how to ride the waves.{/i}"
scene epi_surf4 with dissolve
zo "{i}But that's what surfing is. It's much more than actually riding the waves. You don't even stand up on your board most of the time.{/i}"
zo "{i}It's very different from what I came here thinking.{/i}"
scene epi_surf5 with dissolve
stop music fadeout 3
zo "{i}Anyway, the first rule of surfing over here is always surf with a buddy.{/i}"
zo "{i}So, I had to find one...{/i}"
play music "music/ep_interlude/licensed_music/track101.mp3"
scene epi_surf6 with dissolve
em "Emma. You?"
scene epi_surf7 with dissolve
zo "Zoey."
scene epi_surf8 with dissolve
em "Cool name! You don't sound like you're from here."
scene epi_surf7 with dissolve
zo "I wish I were, but nah. You?"
scene epi_surf8 with dissolve
em "Born on the beach, die on the beach."
scene epi_surf9 with dissolve
zo "You've had this all your life, and you're only learning to surf now? What gives?"
scene epi_surf12 with dissolve
em "Have you ever heard of home blindness?"
scene epi_surf9 with dissolve
zo "Nope, never."
scene epi_surf12 with dissolve
em "I met a tourist who taught me about it."
em "He came here and was all like, \"Wow, this city is so amazing! I bet you're swimming and surfing daily\"."
scene epi_surf13 with dissolve
em "And I was like, \"Nope. I don't, actually\"."
scene epi_surf12 with dissolve
em "So, being home blind is how you spend your life living somewhere, and you get so used to it that you don't see what's awesome about it."
em "It took a pasty-ass tourist to teach me to love my hometown. So, now..."
em "I'm learning how to surf!"
scene epi_surf10 with dissolve
zo "Sounds awesome."
zo "For me, I always wanted to do it, but there are no waves where I come from."
zo "So, the skateboard's been my board of choice."
scene epi_surf14 with dissolve
em "Well, you found the waves."
if persistent.mod_wt_enabled:  
    $mod_choices = ["\n{size=44}(Zoey CHICK)","\n{size=44}(Zoey DIK)","","","","","","","","","","" ]
#[mod_gr][mod_choices[0]]
call screen zoey_choice_screen("Love your tats[mod_gr][mod_choices[1]]",800,60, "Too many tattoos[mod_gr][mod_choices[0]]",1450,60)
if tmp_choice == 1:
    $ zdik(-1)
    scene epi_surf15 with dissolve
    zo "I love your tats."
    em "My tits?"
    scene epi_surf11 with dissolve
    zo "Your tats...tattoos. There's so much cool art on your body."
    scene epi_surf12 with dissolve
    em "Haha, oh yeah! Thanks."
else:
    $ zdik(1)
    $ emma_joke = True
    scene epi_surf11 with dissolve
    zo "Damn, do you even have skin? You're like 90%% tattoos."
    scene epi_surf12b with dissolve
    em "HAHA! More like 80%%! I guess I got carried away at some point."
em "It's what I do to get by. I ink others, not myself. Well, sometimes myself, but much less these days."
scene epi_surf10 with dissolve
zo "You're a tattoo artist?"
scene epi_surf16 with dissolve
em "Yep. I do tattoos and piercings. My friend opened up a studio not far from here and brought me on board."
em "We're pretty small, but it's a living, and we tattoo each other for free."
scene epi_surf17 with dissolve
if persistent.mod_wt_enabled:  
    $mod_choices = ["\n{size=44}(Zoey CHICK)","\n{size=44}(Zoey DIK)","","","","","","","","","","" ]
#[mod_gr][mod_choices[0]]
call screen zoey_choice_screen("Joke[mod_gr][mod_choices[1]]",900,100, "Sounds dope[mod_gr][mod_choices[0]]",950,370)
if tmp_choice == 1:
    scene epi_surf11 with dissolve
    $ zdik(1)
    zo "You must be running him out of business if all that was for free."
    scene epi_surf18 with dissolve
    em "If we go out of business, it'll be because we don't get enough customers, not because we get bored and do each other."
else:
    $ zdik(-1)
    scene epi_surf10 with dissolve
    zo "Sounds dope."
    scene epi_surf16 with dissolve
    em "Totally is."
scene epi_surf19 with dissolve
em "I spotted your notebook. You draw too, don't you?"
zo "Sketches and doodles, mostly. And a lot of words... I'm hardly an artist."
scene epi_surf20 with dissolve
zo "I like to keep myself busy when things are dull, so I bring it with me."
scene epi_surf22 with dissolve
em "Can I see some of it?"
scene epi_surf21 with dissolve
if persistent.mod_wt_enabled:  
    $mod_choices = ["\n{size=44}(Zoey CHICK)","\n{size=44}(Zoey DIK)","","","","","","","","","","" ]
#[mod_gr][mod_choices[0]]
call screen zoey_choice_screen("Um... Why?[mod_gr][mod_choices[1]]",720,100, "Kinda personal[mod_gr][mod_choices[0]]",1500,100)
if tmp_choice == 1:
    $ zdik(1)
    zo "Um... Why?"
    scene epi_surf22 with dissolve
    em "Curiosity."
    em "Come on, show me!"
    scene epi_surf21 with dissolve
    zo "Um..."
else:
    $ zdik(-1)
    zo "Some writings are kinda personal. No offense."
    scene epi_surf22 with dissolve
    em "Hey, none taken."
scene epi_surf24 with dissolve
zo "Here. I made this one a few months back."
em "That one looks sick! Who is it?"
scene epi_surf23 with dissolve
zo "My...um... My best friend."
scene epi_surf25 with dissolve
em "You didn't bring him with you?"
scene epi_surf26 with dissolve
zo "Nah, it's just me."
scene epi_surf27 with dissolve
em "Your surf buddy's gotcha. I'll show you around. Are you looking for work, or are you just cruising?"
scene epi_surf28 with dissolve
zo "Not yet, but I was gonna. Do you got any?"
scene epi_surf27 with dissolve
em "We've been talking about hiring a part-timer for the reception. Can you handle bookings and shit?"
$ guideSuggestedPage = 40
scene epi_surf28 with dissolve
if persistent.mod_wt_enabled:  
    $mod_choices = ["\n{size=44}(Zoey CHICK)","\n{size=44}(Zoey DIK)","","","","","","","","","","" ]
#[mod_gr][mod_choices[0]]
call screen zoey_choice_screen("Yes[mod_gr][mod_choices[0]]",800,100, "Joke[mod_gr][mod_choices[1]]",850,370)
if tmp_choice == 1:
    $ zdik(-1)
    zo "I've never done it before, but I can try."
    scene epi_surf27 with dissolve
    stop music fadeout 3
    em "Awesome."
else:
    $ zdik(1)
    zo "Handle bookings and shit? I can do both of those."
    scene epi_surf27 with dissolve
    stop music fadeout 3
    em "Haha, gross!"

label epi_studio_label:
play music "music/ep_interlude/licensed_music/track102.mp3"
scene epi_studio1 with wipeleft
em "This is it. Our little shop."
zo "You're just called \"Tattoos\"?"
scene epi_studio2 with dissolve
em "That was Bret's idea. \"The customer knows what they'll get. No questions about it.\""
scene epi_studio3 with dissolve
zo "Yeah, but you don't call a restaurant \"Food\". You need to brand it."
zo "Also, didn't you say you do piercings? Where's that in the name?"
scene epi_studio4 with dissolve
em "Tell that to Bret."
scene epi_studio5 with dissolve
bre "Tell what to Bret?"
scene epi_studio6 with dissolve
em "This is Zoey. She thinks your store name sucks ass."
scene epi_studio8 with dissolve
bre "Ouch!"
scene epi_studio7 with dissolve
if persistent.mod_wt_enabled:  
    $mod_choices = ["\n{size=44}(Zoey CHICK)","\n{size=44}(Zoey DIK)","","","","","","","","","","" ]
#[mod_gr][mod_choices[0]]
call screen zoey_choice_screen("It could be better[mod_gr][mod_choices[0]]",200,100, "It sucks[mod_gr][mod_choices[1]]",150,350)
if tmp_choice == 1:
    $ zdik(-1)
    zo "I mean... It could be better."
else:
    $ zdik(1)
    zo "I didn't say that. But yeah..."
    zo "It sucks ass."
scene epi_studio9 with dissolve
bre "You can both suck ass. I'm proud of it."
scene epi_studio10 with dissolve
bre "Wait, you're not a customer, are you?"
scene epi_studio11 with dissolve
em "If she were, you just told her to suck ass."
scene epi_studio12 with dissolve
zo "Yeah, what the hell? You just lost my business, Bret."
scene epi_studio13 with dissolve
bre "What a fine business it would have been. You're a blank canvas, aren't you?"
bre "Untouched by the needle. *{i}Whistles{/i}*"
scene epi_studio14 with dissolve
bre "I'll be your first if you'll let me."
scene epi_studio15 with dissolve
if persistent.mod_wt_enabled:  
    $mod_choices = ["\n{size=44}(Zoey CHICK)","\n{size=44}(Zoey DIK)","","","","","","","","","","" ]
#[mod_gr][mod_choices[0]]
call screen zoey_choice_screen("Ignore him[mod_gr][mod_choices[0]]",700,100, "Talk back[mod_gr][mod_choices[1]]",670,350)
if tmp_choice == 1:
    $ zdik(-1)
    scene epi_studio17 with dissolve
    em "Jesus, Bret. Dial it back, will you?"
    scene epi_studio18 with dissolve
else:
    $ zdik(1)
    scene epi_studio16 with dissolve
    zo "Keep your \"needle\" away from me."
    scene epi_studio18 with dissolve
em "Zoey's new in town. She's in my surfing class, and she's my surf buddy."
em "I told her we might have some work for her. How about it?"
scene epi_studio19 with dissolve
bre "You're really forcing me to hire an assistant?"
scene epi_studio20 with dissolve
em "I'm friggin' tired of running between the counter and a customer."
em "They always show up when we're busy too."
em "So, yeah! Zoey will book 'em, and we'll ink and pierce 'em."
scene epi_studio21 with dissolve
bre "Do you have any work experience or something? Ever handled money or customers?"
scene epi_studio22 with dissolve
zo "Nah, you said it best before. I'm a blank canvas."
zo "But what's great about that is that you can write or draw whatever you want on it."
scene epi_studio23 with dissolve
em "She'll figure it out. We managed to make Jonah work, didn't we?"
scene epi_studio24 with dissolve
jon "I'm within earshot, guys. The needle only makes so much noise."
scene epi_studio25 with dissolve
bre "We can try it, but no promises yet. Sound good?"
scene epi_studio26 with dissolve
zo "As long as I can still go to surfing class, I'm down for it."
bre "Awesome!"

label epi_night_label:
scene epi_night1 with wipeleft
$ renpy.pause()
scene epi_night2 with dissolve
zo "(A new bag... I wonder whose it is.)"
scene epi_night3 with dissolve
zo "(Ah, a red wristband. Another lost soul.)"
stop music fadeout 20
scene epi_night4 with dissolve
$ text_message_screen_list = []
$ text_message_screen_list.append(["Zoey","Had a rad day. Started my class and landed a job - maybe.",False])
$ text_message_screen_list.append(["%s" % name,"Is surfing just as easy as skating?",True])
$ text_message_screen_list.append(["Zoey","Since when did you think skating is easy? You can barely stand on a board.",False])
$ text_message_screen_list.append(["%s" % name,"I meant for you. :P",True])
$ text_message_screen_list.append(["Zoey","Haven't gotten to the good stuff yet, but next lesson, it will happen. And LOL, I missed your fake emojis.",False])
$ tmpInt = 0
$ renpy.pause()
scene epi_night5 with dissolve
show screen text_message_screen
$ renpy.pause()
play sound "sound_effects/interlude/zoey_message.mp3"
$ tmpInt += 1
$ renpy.pause()
$ tmpInt += 1
$ renpy.pause()
$ tmpInt += 1
$ renpy.pause()
scene epi_night6 with dissolve
$ tmpInt += 1
$ renpy.pause()
hide screen text_message_screen

$ text_message_screen_list = []
$ text_message_screen_list.append(["Zoey","I should get a wetsuit and a board of my own, too. They said you could borrow one, but I'd rather have my own gear.",False])
$ text_message_screen_list.append(["%s" % name,"Sounds like you've got a lot going on for you...",True])
$ tmpInt = 0
show screen text_message_screen
$ renpy.pause()
$ tmpInt += 1
$ renpy.pause(1)
scene epi_night7 with dissolve
if persistent.mod_wt_enabled:  
    $mod_choices = ["\n{size=44}(Zoey CHICK)","\n{size=44}(Zoey DIK)","","","","","","","","","","" ]
#[mod_gr][mod_choices[0]]
call screen zoey_choice_screen("Sure do[mod_gr][mod_choices[1]]",1400,400, "Show concern[mod_gr][mod_choices[0]]",1400,100)
if tmp_choice == 1:
    $ zdik(1)
    $ text_message_screen_list.append(["Zoey","Sure do. I like it so far.",False])
    $ text_message_screen_list.append(["%s" % name,"It's past bedtime over here, so...",True])
    $ text_message_screen_list.append(["Zoey","Damn. Right. I forgot. Goodnight!",False])
else:
    $ zdik(-1)
    $ text_message_screen_list.append(["Zoey","What's up with the three dots?",False])
    $ text_message_screen_list.append(["%s" % name,"Nothing. It's past bedtime over here, so...",True])
    $ text_message_screen_list.append(["Zoey","Damn. Right. I forgot. Goodnight!",False])
$ tmpInt += 1
$ renpy.pause()
$ tmpInt += 1
$ renpy.pause()
$ tmpInt += 1
$ renpy.pause()
hide screen text_message_screen

scene epi_night8 with dissolve
$ renpy.pause()

label epi_work_label:
play music "music/ep_interlude/licensed_music/track100.mp3"
scene anim_work_epi with fade
$ renpy.pause()
scene epi_work1 with dissolve
bre "How's it going, Zoey?"
scene epi_work2 with dissolve
zo "Same as it did an hour ago. Nothing yet. Are you sure the phone works?"
scene epi_work3 with dissolve
bre "Haha, yeah, it works."
scene epi_work4 with dissolve
zo "And the e-mail, too?"
scene epi_work5 with dissolve
zo "Oh, we got one!"
scene epi_work6 with dissolve
zo "No, wait. It was a penis enlargement mail. Is this your personal inbox, Bret?"
scene epi_work7 with dissolve
bre "Ha-ha. They must have mixed the address up with Jonah's."
scene epi_work8 with dissolve
jon "Bret's such a bully. And stop lying; you've tattooed my dick. You couldn't forget my salami, even if you tried."
scene epi_work12 with dissolve
zo "Haha! Wait! You tattooed his dick?"
scene epi_work13 with dissolve
bre "Yeah, I did. It was the shortest tattoo session I've ever had. Hahah!"
scene epi_work15 with dissolve
jon "Fuck. You."
scene epi_work10b with dissolve
zo "Why would you tattoo your dick?"
scene epi_work9 with dissolve
jon "To make it look like a dragon."
scene epi_work10b with dissolve
zo "Chicks dig that?"
scene epi_work9b with dissolve
jon "Dunno about that, but guys do."
scene epi_work10 with dissolve
zo "Oh, sorry."
scene epi_work9 with dissolve
jon "No worries. I tend to fly under people's gaydars."
scene epi_work10b with dissolve
zo "Bret must be a brave man to tattoo your privates."
scene epi_work9 with dissolve
jon "Haha, nah. He knows he's ugly as fuck to me. I couldn't get a boner if I tried from that mug."
scene epi_work11 with dissolve
zo "Hahaha!"
scene epi_work14 with dissolve
bre "This mug? Come on. I'm a tanned catch in tighter pants than a European, and you know it."
scene epi_work15 with dissolve
jon "Weird flex, but ok."
scene epi_work16 with dissolve
$ renpy.pause()
scene epi_work17 with dissolve
zo "Holy shit, guys! We got a live one."
zo "Hey, welcome to...Tattoos. Can I help you?"
scene epi_work18 with dissolve
cs "I wanna get a skull on my calf - something like this."
scene epi_work19 with dissolve
zo "Oh... You drew this?"
cs "It's just a rough sketch. I thought you'd help me improve it a bit."
scene epi_work20 with dissolve
zo "Sure thing. Maybe we could do something like this...for you?"
if minigames:
    hide screen notebook_button_screen
    $ renpy.pause(0.5)
    jump epi_drawing_game2_label
    label epi_after_drawing2_label:
    show screen notebook_button_screen
scene epi_work21 with dissolve
zo "How about this? What do you think?"
scene epi_work22 with dissolve
cs "Yeah, that looks cool."
scene epi_work23 with dissolve
zo "Jonah! You're good with skulls, right?"
jon "I'm the best at skulls."
zo "Got a customer for you."
jon "Send him over."
scene epi_work24 with dissolve
cs "Thanks for the help."
zo "Don't mention it."
scene epi_work25 with dissolve
em "Mornin'! And damn, what a pretty sight seeing you sit there!"
zo "Sup, Emma."
scene epi_work26 with dissolve
jon "Bret!"
bre "Coming!"
scene anim_work3_epi with dissolve
em "How's it going?"
zo "Is it always this slow?"
em "It varies. Most customers drop in unannounced, so you've gotta have a strong waiting game to stay sane."
zo "Really? Why is that?"
em "Most drop-in customers are tourists looking to get a memento."
em "And for other customers, we do have some serious competition in the area."
em "We're not exactly people's first choice. Don't tell Bret I said that."
scene epi_work27 with dissolve
bre "Zoey... You drew this?"
scene epi_work28 with dissolve
if persistent.mod_wt_enabled:  
    $mod_choices = ["\n{size=44}(Zoey CHICK)","\n{size=44}(Zoey DIK)","","","","","","","","","","" ]
#[mod_gr][mod_choices[0]]
call screen zoey_choice_screen("Good, huh?[mod_gr][mod_choices[1]]",370,100, "Yeah[mod_gr][mod_choices[0]]",1350,100)
if tmp_choice == 1:
    $ zdik(1)
    zo "Good, huh?"
else:
    $ zdik(-1)
    zo "Yeah, I just tweaked his idea a bit."
scene epi_work27 with dissolve
bre "This is as good as any of what we draw. I mean, anything that Jonah and Ems draw."
scene epi_work30 with dissolve
em "Hey! What the hell!?"
scene epi_work31 with dissolve
em "Wait... This one is actually very good."
bre "Do you draw a lot, Zoey?"
scene epi_work28 with dissolve
zo "I sketch a lot in my notebook, but that's about it."
$ guideSuggestedPage = 41
scene epi_work32 with dissolve
bre "Sketch some more stuff while you wait for work. If it looks good, we could use it for stencils and inspiration for the customers."
scene epi_work28 with dissolve
if persistent.mod_wt_enabled:  
    $mod_choices = ["\n{size=44}(Zoey CHICK)","\n{size=44}(Zoey DIK)","","","","","","","","","","" ]
#[mod_gr][mod_choices[0]]
call screen zoey_choice_screen("Pay me for it[mod_gr][mod_choices[1]]",370,100, "Sounds fun[mod_gr][mod_choices[0]]",1350,100)
if tmp_choice == 1:
    $ zdik(1)
    zo "If it comes with a pay raise, I will."
    scene epi_work32 with dissolve
    bre "It should compensate for the time you're just sitting there."
    scene epi_work29 with dissolve
    zo "As if that's my fault. Do you even advertise?"
    scene epi_work32 with dissolve
    bre "Yeah, we're out there."
    scene epi_work33 with dissolve
    jon "Haha, we're not \"out there\"."
    bre "Shut up."
    scene epi_work34 with dissolve
    em "Sensitive..."
else:
    $ zdik(-1)
    zo "Hey, that sounds fun."
    scene epi_work32 with dissolve
    bre "Stoked!"
scene epi_work35 with fade
cs "Thanks again! Look how good it came out!"
scene epi_work36 with dissolve
zo "That looks badass, dude. Rock on!"
zo "Jonah, how much!?"
jon "$120!"
scene epi_work37 with dissolve
cs "Keep the extra. I loved your sketch!"
scene epi_work38 with dissolve
em "It looks like she's doing fine, don't you think?"
scene epi_work39 with dissolve
bre "It's just one day so far, but I'm not gonna lie..."
bre "The girl's got potential."
stop music fadeout 3
scene epi_work40 with dissolve
$ renpy.pause()

label epi_surf_2nd_label:
play music "music/ep_interlude/licensed_music/track103.mp3"
scene epi_surf_2nd1 with wipeleft
ins "Learn to read the waves, everyone. Remember what we talked about."
ins "Find the peak and the shoulder of the wave. It's all about finding the perfect gradient."
scene epi_surf_2nd3 with dissolve
em "How's that banana working out for you?"
scene epi_surf_2nd4 with dissolve
if persistent.mod_wt_enabled:  
    $mod_choices = ["\n{size=44}(Zoey CHICK)","\n{size=44}(Zoey DIK)","","","","","","","","","","" ]
#[mod_gr][mod_choices[0]]
call screen zoey_choice_screen("Had better ones[mod_gr][mod_choices[1]]s",700,100, "Back hurts[mod_gr][mod_choices[0]]",750,350)
if tmp_choice == 1:
    $ zdik(1)
    zo "I've had better bananas."
    scene epi_surf_2nd5 with dissolve
    em "Haven't we all?"
    scene epi_surf_2nd4 with dissolve
    zo "The water's getting kind of cold."
else:
    zo "Not good. My back hurts!"
    scene epi_surf_2nd1 with dissolve
    ins "Did I hear someone say their back hurts? Remember, don't start paddling until you spot a wave."
    scene epi_surf_2nd4 with dissolve
    zo "The water's getting kind of cold too."
scene epi_surf_2nd5 with dissolve
em "What do you think the wetsuit's for?"
scene epi_surf_2nd2 with dissolve
ins "See!? A nice wave is heading our way. BANANA AND PADDLE!"
ins "Keep up with the wave!"
scene epi_surf_2nd6 with dissolve
zo "Hngn... Come on..."
scene epi_surf_2nd7 with dissolve
ins "You got it, Zoey! Pop up when you're ready for it!"
scene epi_surf_2nd8 with dissolve
$ renpy.pause()
scene epi_surf_2nd9 with dissolve
$ renpy.pause()
scene epi_surf_2nd10 with dissolve
zo "Whoa!"
play sound "sound_effects/water_splash.mp3"
scene epi_surf_2nd11 with vpunch
$ renpy.pause()
scene epi_surf_2nd1 with dissolve
ins "That was a nice try, Zoey, but you need to go slower and lower with your pop up."
scene epi_surf_2nd12 with dissolve
zo "How?"
scene epi_surf_2nd1 with dissolve
ins "Go to the prone position first and catch your balance before completing the pop up."
ins "And when you're standing up, stand with a lower stance so you don't lose your balance. You were standing kind of straight."
scene epi_surf_2nd13 with dissolve
zo "{i}I don't remember how many tries it took... Some say that going from wakeboarding to surfing is easy...{/i}"
zo "{i}But from skateboarding to surfing... Not so much. At least not for me.{/i}"
scene epi_surf_2nd14 with dissolve
zo "{i}Seeing how others managed to surf within a couple of attempts didn't boost my confidence.{/i}"
scene epi_surf_2nd15 with dissolve
zo "{i}It just got me frustrated. Fuck! I was supposed to be good at this.{/i}"
zo "{i}It's like learning how to walk all over again.{/i}"
play sound "sound_effects/interlude/sand.mp3"
scene epi_surf_2nd16 with vpunch
zo "Ugh!"
scene epi_surf_2nd17 with dissolve
em "You are fuming. Did it get to ya?"
if persistent.mod_wt_enabled:  
    $mod_choices = ["\n{size=44}(Zoey CHICK)","\n{size=44}(Zoey DIK)","","","","","","","","","","" ]
#[mod_gr][mod_choices[0]]
call screen zoey_choice_screen("I'm fine[mod_gr][mod_choices[0]]",1400,100, "I'm pissed[mod_gr][mod_choices[1]]",1400,350)
if tmp_choice == 1:
    $ zdik(-1)
    scene epi_surf_2nd18 with dissolve
    zo "I'm fine..."
    scene epi_surf_2nd19 with dissolve
    em "That would be easier to believe if I couldn't hear your teeth grinding."
    scene epi_surf_2nd18 with dissolve
    zo "I don't know what happened out there. I have great balance..."
else:
    $ zdik(1)
    scene epi_surf_2nd18 with dissolve
    zo "I'm pissed at myself, Emma. I've got great balance! I don't know what happened out there."
scene epi_surf_2nd19 with dissolve
em "You'll get it eventually. It takes practice."
scene epi_surf_2nd20 with dissolve
if persistent.mod_wt_enabled:  
    $mod_choices = ["\n{size=44}(Zoey CHICK)","\n{size=44}(Zoey DIK)","","","","","","","","","","" ]
#[mod_gr][mod_choices[0]]
call screen zoey_choice_screen("Right...[mod_gr][mod_choices[0]]",1350,350, "Talk back[mod_gr][mod_choices[1]]",1400,100)
if tmp_choice == 1:
    $ zdik(-1)
    zo "Yeah, I know you're right... But I'm frustrated with myself."
    scene epi_surf_2nd19 with dissolve
    em "You need to cool off, girl."
else:
    $ zdik(1)
    zo "You did two successful rides. If I knew you better, I'd tell you to shut up."
    scene epi_surf_2nd19 with dissolve
    em "You need to cool off, girl."
scene epi_surf_2nd20 with dissolve
zo "No, thanks. The water was cold enough. I need to get a hot shower and drink a virgin drink in my virgin hostel with all the other virgins."
scene epi_surf_2nd21 with dissolve
stop music fadeout 3
em "No. You go take that shower, and then you'll meet me for a night out. Bret and Jonah are coming, too. It'll be fun!"

label epi_bar_label:
play music "music/ep_interlude/licensed_music/track104.mp3"
scene epi_bar1 with wipeleft
zo "{i}Yeah, it would be fun. If I was allowed to drink anything other than milk... Pff...{/i}"
zo "{i}I never thought I'd say this, but I was starting to miss sneaking one of Mom's cold beers.{/i}"
scene epi_bar2 with dissolve
em "Zoey! Over here!"
scene epi_bar3 with dissolve
zo "Hey, guys. So, this is the local waterhole of choice?"
scene epi_bar4 with dissolve
jon "It's the only bar in this area that plays our kind of music."
scene epi_bar5 with dissolve
zo "ShitFaced? No way!"
bre "You're a fan too?"
zo "Um, hell yeah! Since I was like eight and didn't know what it meant."
scene epi_bar6 with dissolve
zo "I hate to admit it, but if there is one thing my stepdad did right, it was buying records."
scene epi_bar14 with dissolve
bt "So what will it be, friends?"
scene epi_bar16 with dissolve
em "The usual."
jon "You know what I like. Surprise me!"
scene epi_bar17 with dissolve
zo "I'll have a..."
scene epi_bar18 with vpunch
bre "Two beers for us!"
scene epi_bar15 with dissolve
bt "You got it."
scene epi_bar19 with dissolve
bre "How old are you?"
scene epi_bar20 with dissolve
zo "19..."
scene epi_bar21 with dissolve
bre "Jeez... Hide that fucking wristband. It's a universal language here."
scene epi_bar22 with dissolve
jon "Is something universal if it's local?"
scene epi_bar23 with dissolve
bre "Fuck off, smartass."
scene epi_bar24 with dissolve
zo "I forgot... I have to wear it at the hostel."
scene epi_bar7 with dissolve
bre "You live in a hostel?"
scene epi_bar26 with dissolve
jon "That's gotta be expensive."
scene epi_bar25 with dissolve
zo "It was either a hostel or the street. But I'm looking for a place to rent."
scene epi_bar33 with dissolve
em "You should look into studio apartments. There are a bunch of them available after the surfing season's over."
scene epi_bar29 with dissolve
zo "And until then?"
scene epi_bar26 with dissolve
jon "You'll have to look harder for one."
scene epi_bar25 with dissolve
zo "So, where do you guys live?"
scene epi_bar27 with dissolve
em "She's scouting us for a place to crash. Quick, think of lies to tell her."
scene epi_bar30 with dissolve
zo "Pff! Was not."
scene epi_bar8 with dissolve
bre "I live above the tattoo studio. You can crash there if you want."
scene epi_bar28 with dissolve
em "Aha! Really? You've gotta have it in for Zoey because you never let me do that."
scene epi_bar32 with dissolve
bre "Ems..."
scene epi_bar31 with dissolve
zo "The hostel's cool with me until I find someplace else."
scene epi_bar34 with dissolve
bt "Beers and drinks; here you go."
scene epi_bar35 with dissolve
bt "I was gonna say it before, but that's a nice hair color."
bt "I've always wanted to try blue, but it's scary taking that leap."
scene epi_bar36 with dissolve
if persistent.mod_wt_enabled:  
    $mod_choices = ["\n{size=44}(Zoey CHICK)","\n{size=44}(Zoey DIK)","","","","","","","","","","" ]
#[mod_gr][mod_choices[0]]
call screen zoey_choice_screen("Not for everyone[mod_gr][mod_choices[1]]",720,100, "Encourage her[mod_gr][mod_choices[0]]",700,380)
if tmp_choice == 1:
    $ zdik(1)
    $ epi_blue_hair = False
    zo "It's not for everyone."
    scene epi_bar35 with dissolve
    bt "Yeah, and that's what keeps me from doing it."
else:
    $ zdik(-1)
    $ epi_blue_hair = True
    zo "Just go for it. If it doesn't work out, you can change it again."
    scene epi_bar35 with dissolve
    bt "Haha, that's true!"
scene epi_bar37 with dissolve
bre "What the hell? Are you reading tonight?"
scene epi_bar38 with dissolve
bre "Entrepreneurial Finance... What the fuck is that?"
jon "You tell me; you pronounced the words right."
scene epi_bar40 with dissolve
em "Wait! Jonah can read? Then why am I the only one doing lettering tattoos?"
scene epi_bar39 with dissolve
jon "Because lettering tattoos and tribals are the most boring tattoos you can make."
jon "This line of work is my ticket to scoliosis, so I'm not gonna bother with that kind of ink."
scene epi_bar12 with dissolve
bre "Seriously, though. What's this for? You going to college or something?"
scene epi_bar41 with dissolve
jon "Who knows? I find these things interesting."
jon "And maybe if you did too, the studio would be profitable."
scene epi_bar47 with dissolve
em "Holy fuck, what a nerd burn."
scene epi_bar13 with dissolve
bre "Haha! Sit and spin, fucker!"
bre "Or don't. You'd probably like that."
scene epi_bar42 with dissolve
jon "Zoey, help me out here. You're bright. You're going to college someday too, right?"
if persistent.mod_wt_enabled:  
    $mod_choices = ["\n{size=44}(Zoey CHICK)","\n{size=44}(Zoey DIK)","","","","","","","","","","" ]
#[mod_gr][mod_choices[0]]
call screen zoey_choice_screen("Help him out[mod_gr][mod_choices[0]]",600,100, "Don't look at me[mod_gr][mod_choices[1]]",600,350)
scene epi_bar44 with dissolve
if tmp_choice == 1:
    $ zdik(-1)
    zo "Don't listen to these numbskulls. You do you, Jonah. As for college, I haven't even graduated high school yet."
else:
    $ zdik(1)
    zo "Dude, I can't defend your choice to bring a book on finance to a rock pub."
    zo "And I'm not that bright; I haven't even graduated high school yet."
scene epi_bar46 with dissolve
em "Kindred spirits!"
scene epi_bar9 with dissolve
bre "For real?"
scene epi_bar45 with dissolve
zo "I flunked my trig class and haven't found the motivation to complete it."
scene epi_bar43 with dissolve
jon "That's a bummer."
scene epi_bar11 with dissolve
bre "Math! Who needs it?"
scene epi_bar48 with dissolve
em "You need it."
scene epi_bar49 with dissolve
bre "Oh, please! All you need is a calculator and someone to do your bookkeeping to run a business."
stop music fadeout 3
bre "Let the number crunchers do their job, and you can do yours."
play music "music/ep_interlude/licensed_music/track105.mp3"
scene epi_bar50 with dissolve
zo "Oh shit! It's this song!"
bre "Huh?"
scene epi_bar10 with dissolve
zo "It's from one of their B-sides! I fucking love it!"
scene epi_bar9 with dissolve
bre "I'm a fan, but I don't know this one."
scene epi_bar10 with dissolve
zo "Yes, you do!"
scene epi_bar9 with dissolve
bre "Nope. I don't know it."
scene epi_bar51 with dissolve
zo "But you...do-hahaha!"
scene epi_bar54 with dissolve
em "Did she get a beer or one of your umbrella drinks?"
scene epi_bar55 with dissolve
jon "Drink-shame me all you want, but these are delicious. You wish you were girl enough to order one."
scene epi_bar9 with dissolve
bre "What's so funny?"
scene epi_bar51 with dissolve
zo "Haha! It's nothing - just an inside joke thingy."
stop music fadeout 3
scene epi_bar52 with dissolve
$ renpy.pause()
scene epi_bar53 with dissolve
$ renpy.pause()

label epi_tattoo_label:
play music "music/ep_interlude/licensed_music/track100.mp3"
scene epi_tattoo1 with fade
bre "It's straight, right?"
jon "Straighter than me."
scene epi_tattoo2 with dissolve
em "Yeah, it looks fine."
$ guideSuggestedPage = 42
scene epi_tattoo3 with dissolve
bre "You didn't drink anything today or yesterday?"
call screen zoey_choice_screen("{size=-%d}Is that a problem?{/size}" % (5 * persistent.scale_factor),100,100, "Nope",50,400)
scene epi_tattoo4 with dissolve
if tmp_choice == 1:
    zo "Is that a problem?"
    scene epi_tattoo5 with dissolve
    bre "You're gonna bleed like a pig if you did."
    scene epi_tattoo4 with dissolve
    zo "Ok. I didn't drink anything."
else:
    zo "Not alcohol, no."
scene epi_tattoo5 with dissolve
bre "Good. Since it's your first one, I'm gonna push you down a bit harder when I start."
scene epi_tattoo6 with dissolve
zo "Huh?"
scene epi_tattoo5 with dissolve
bre "We do it all the time with the newbies. I don't know how you'll react to the needle, and I don't want you to jerk so I mess up the line."
scene epi_tattoo6 with dissolve
zo "Ok... Does it hurt, though?"
scene epi_tattoo7 with dissolve
em "Think of it as pressing a knife against your skin and slowly dragging it back and forth."
scene epi_tattoo8 with dissolve
zo "Uh... That sounds like it would hurt a lot."
scene epi_tattoo7 with dissolve
em "No, not that kind of a knife. A cutlery knife, you know?"
scene epi_tattoo8 with dissolve
zo "Yeah, but still-"
play sound "sound_effects/interlude/tattoo_gun1.mp3"
scene epi_tattoo9 with vpunch
zo "Ah! Shit! That startled me!"
zo "Hngn! Hey..."
scene epi_tattoo10 with dissolve
zo "Ok, it's not too bad."
scene epi_tattoo11 with dissolve
bre "Are you good?"
scene epi_tattoo10 with dissolve
zo "Yeah."
scene epi_tattoo11 with dissolve
bre "The needle will hurt more when I go against the bones - just a heads up."
scene epi_tattoo10 with dissolve
zo "Ok."
scene epi_tattoo12 with dissolve
bre "So, who's the tattoo for?"
scene epi_tattoo13 with dissolve
zo "It's something I drew."
scene epi_tattoo12 with dissolve
bre "Yeah? What about the text? It's kind of morbid."
bre "\"Your wings were ready, but my heart was not.\""
scene epi_tattoo13 with dissolve
zo "It's for my grandma. I don't wanna talk about her when we're doing this."
zo "It won't be the needle that makes me cry if we do."
scene epi_tattoo14 with dissolve
bre "Gotcha. I wanted to do a tattoo like this for my dog, but I never did. Damn, I miss that mutt."
scene epi_tattoo15 with dissolve
zo "Never got another dog?"
scene epi_tattoo14 with dissolve
bre "No. I couldn't bring myself to get one."
bre "I don't wanna go through that pain ever again. It was way worse than losing a relative."
bre "But maybe that says more about my family than it does about my dog."
scene epi_tattoo10 with dissolve
zo "I wouldn't know. I never had any pets."
play sound "sound_effects/interlude/tattoo_gun1.mp3"
scene epi_tattoo16 with dissolve
bre "Bone."
zo "Ouch!"
zo "Yeah, that hurts..."
scene epi_tattoo17 with dissolve
em "I'm heading home. You'll be ok without me?"
scene epi_tattoo18 with dissolve
bre "Jonah's still here, ain't he?"
scene epi_tattoo19 with dissolve
jon "I'm leaving too."
scene epi_tattoo18 with dissolve
bre "What is this? Half-day Friday?"
scene epi_tattoo19 with dissolve
jon "Whatever you say, workaholic!"
scene epi_tattoo18 with dissolve
bre "Flip the sign and lock the door, will you?"
scene epi_tattoo20 with dissolve
zo "You're staying extra for me?"
scene epi_tattoo21 with dissolve
bre "I don't mind it. You've done such a great job, so I thought you'd earned this."
scene epi_tattoo22 with dissolve
zo "That's not a way to weasel out of paying me, I hope."
scene epi_tattoo23 with dissolve
bre "Haha! Not really. I thought we could extend your hours a bit."
bre "Customers have been diggin' your work. I tattooed two of your stencils this week."
scene anim_tattoo_epi with dissolve
zo "Whoa, that's so cool."
zo "Isn't it an odd feeling that you get paid to scar people for life?"
zo "Like, right now, there are a bunch of people walking around with things I drew on a piece of paper."
zo "They liked it so much that they wanted it permanently on their skin... It's sick, right?"
bre "It's just a piece of skin. People put too much value on their bodies."
zo "Well, we only get one body."
bre "Are you having second thoughts about this tattoo? Because it's kind of too late for that."
scene epi_tattoo22 with dissolve
zo "Haha, no. I guess what I wanted to say is that it's...pretty cool. The work you do."
zo "You're creating walking pieces of art."
scene epi_tattoo23 with dissolve
bre "It's the only work I know how to do. I bought my first tattoo gun when I was 14."
bre "My older brother helped me get one."
bre "Ems and I started making shitty tattoos on each other for practice."
if persistent.mod_wt_enabled:  
    $mod_choices = ["\n{size=44}(Zoey CHICK)","\n{size=44}(Zoey DIK)","","","","","","","","","","" ]
#[mod_gr][mod_choices[0]]
call screen zoey_choice_screen("I can tell[mod_gr][mod_choices[1]]",1520,250, "Which ones?[mod_gr][mod_choices[0]]",1450,20)
if tmp_choice == 1:
    scene epi_tattoo22 with dissolve
    $ zdik(1)
    zo "I can tell. Those tattoos on your hands are horrible."
    scene epi_tattoo26 with dissolve
    bre "What? I was talking about the ones on my legs."
    scene epi_tattoo25 with dissolve
    zo "Oh..."
    zo "Is it pointless trying to undo the damage?"
    scene epi_tattoo24 with dissolve
    bre "Yeah, and I already pegged you as a straight shooter."
    bre "Not everyone tells you how it is to your face, you know?"
    scene epi_tattoo22 with dissolve
    zo "At least you get to wear gloves when you work."
    scene epi_tattoo24 with dissolve
    bre "Yeah, you can always cover your tattoos up if you want to. Most of them, anyway."
else:
    $ zdik(-1)
    scene epi_tattoo22 with dissolve
    zo "Which ones?"
    scene epi_tattoo24 with dissolve
    bre "The ones on my legs. They are just legs, and you can cover the tattoos with pants if you want to."
    scene epi_tattoo22 with dissolve
    zo "Not with the kind of pants you're wearing."
    scene epi_tattoo24 with dissolve
    bre "Haha, I'll give you that one."
scene epi_tattoo22 with dissolve
zo "You're making me feel better about getting tattoos... Thanks."
scene epi_tattoo24 with dissolve
bre "Ask Ems and Jonah, and I'm sure they'll do a couple for you too. If you're looking to get more, I mean."
scene epi_tattoo22 with dissolve
zo "I gotta say that the feeling is pretty nice. It hurts, but I kind of like it."
scene epi_tattoo24 with dissolve
bre "Yeah, that sounds like someone who wants to get more of 'em for sure."
bre "The pain is half the experience."
scene epi_tattoo28 with dissolve
zo "Haha, that's so dark..."
scene epi_tattoo24 with dissolve
bre "Just like anal."
scene epi_tattoo29 with dissolve
zo "Uh..."
scene epi_tattoo24 with dissolve
bre "Too far, haha. Sorry, I have shitty humor."
bre "But it's true. You'll see."
scene epi_tattoo28 with dissolve
zo "I hope you're still talking about tattoos."
scene epi_tattoo24 with dissolve
bre "So, do you got a boyfriend back in...wherever it was you came from?"
scene epi_tattoo27 with dissolve
zo "Huh? Uh..."
zo "Did you just segue from talking about anal to asking if I have a boyfriend?"
scene epi_tattoo24 with dissolve
bre "Innocent question. I swear."
scene epi_tattoo30 with dissolve
zo "Well, there's this guy, but I don't know..."
zo "Lately, it's been kind of weird between us."
scene epi_tattoo31 with dissolve
zo "I think he blames me a bit for leaving too fast."
zo "We talked about going places together for a while, you know, after graduating."
zo "But he's still in school and couldn't come here with me, and I had to come here for...myself."
scene epi_tattoo32 with dissolve
bre "Sounds complicated."
scene epi_tattoo30 with dissolve
zo "Not really. He's as simple as they get."
scene epi_tattoo32 with dissolve
bre "Oof... I'd kill myself if a girlfriend described me like that."
scene epi_tattoo31 with dissolve
zo "It's not an insult. He's pretty much drama-free."
zo "We'd been best friends for years before we started to...you know."
scene epi_tattoo32 with dissolve
bre "Know what?"
if persistent.mod_wt_enabled:  
    $mod_choices = ["\n{size=44}(Zoey CHICK)","\n{size=44}(Zoey DIK)","","","","","","","","","","" ]
#[mod_gr][mod_choices[0]]
call screen zoey_choice_screen("Fuck",230,100, "{size=-%d}Discover our bodies{/size}" % (5 * persistent.scale_factor),150,350)
scene epi_tattoo31 with dissolve
if tmp_choice == 1:
    $ zdik(1)
    zo "Fuck."
else:
    $ zdik(-1)
    zo "Discover our bodies."
scene epi_tattoo24 with dissolve
bre "I hear you. That sounds like Ems and me."
scene epi_tattoo27 with dissolve
zo "You and Ems? Are you...together?"
scene epi_tattoo24 with dissolve
bre "Not anymore. It's been a while."
bre "I set up the studio while she went off doing her things in Vegas. We eventually got back together for work, but that's it."
bre "We're still best friends, though."
scene epi_tattoo30 with dissolve
zo "I get the feeling I'm drifting apart from...him."
zo "He's pretty short in his messages to me. He doesn't seem to share my joy."
scene epi_tattoo32 with dissolve
bre "If he got bummed out when you left, can you blame him?"
scene epi_tattoo31 with dissolve
zo "Um, yeah? He's my best friend."
scene epi_tattoo32 with dissolve
bre "See it like this... If he was something more than that, then maybe he's having a harder time getting over you than you have getting over him."
scene epi_tattoo30 with dissolve
zo "Getting over each other? No, you've got it wrong. We weren't in a relationship. We are best friends who happened to fuck a lot."
scene epi_tattoo32 with dissolve
bre "You agreed on that?"
scene epi_tattoo31 with dissolve
zo "It was more of a silent agreement. The kind that you understood with time. I fucking hate talking about feelings."
zo "And he's a bit of a softie at times. That makes me uncomfortable."
scene epi_tattoo32 with dissolve
bre "All right... And then you left before ending it with him?"
scene epi_tattoo31 with dissolve
zo "Yeah? So?"
scene epi_tattoo32 with dissolve
bre "You know what? It's not my place to say these things to you. I only speak from my own experience when Ems left me for a while."
scene epi_tattoo33 with dissolve
zo "..."
scene epi_tattoo31 with dissolve
zo "How was it for you when that happened?"
scene epi_tattoo32 with dissolve
bre "I could have handled it better."
bre "I got drunk and drunk-texted her. That only made it worse."
bre "When I sobered up, I realized I had to stop doing that, so I did."
bre "I feared the damage was already done, though. She didn't write me anything for a long time."
scene epi_tattoo24 with dissolve
bre "She gave me a like or two on Rooster once in a while. Hit me up with some short comments. But for the better part of it, she stayed away."
bre "It's not something a best friend would do, but she actually did me a favor. It allowed me to get over her and focus on work."
scene epi_tattoo27 with dissolve
zo "What happened after she came back?"
scene epi_tattoo24 with dissolve
bre "Believe it or not, it was like pressing play on your favorite ShitFaced song that you paused for a long time."
bre "The song was as good, if not even better, than before."
scene epi_tattoo32 with dissolve
bre "We didn't really talk about our hookups or get back together in any other way than friends - and, well, co-workers."
bre "Knowing how it turned out, I owe her a lot for doing what she did to me. I think it saved me in a sense."
scene epi_tattoo33 with dissolve
stop music fadeout 3
zo "..."
scene epi_tattoo34 with fade
play music "<from 3.5>music/ep_interlude/licensed_music/track109.mp3"
bre "Ok... I think you'll like this. Are you ready to see the new you?"
scene epi_tattoo35 with dissolve
zo "Yeah, I'm dying to. It started to hurt a lot more toward the end."
scene epi_tattoo36 with dissolve
bre "Yeah, the adrenaline wears off after this long of a session."
scene epi_tattoo37 with dissolve
bre "What do you think?"
scene epi_tattoo38 with dissolve
zo "..."
scene epi_tattoo39 with dissolve
zo "I love it."
scene epi_tattoo38 with dissolve
bre "I can tell."
scene epi_tattoo40 with dissolve
zo "Grandma would have loved this..."
scene epi_tattoo41 with dissolve
bre "She sounds like a cool grandma."
scene epi_tattoo40 with dissolve
zo "Yeah... She's the reason I'm here today."
zo "She wanted me to... *{i}Sobs{/i}*"
zo "...go my own way through life..."
zo "...and not listen to what everyone else wanted for me."
zo "She passed away before she got to see me do it."
scene epi_tattoo41 with dissolve
bre "That's rough..."
scene epi_tattoo42 with dissolve
bre "Come with me. Let's put some plastic on that tattoo and get a drink."
bre "You shouldn't drink after you get tattooed, but one beer won't hurt."
scene epi_tattoo43_nocard
if not persistent.epi_card2:
    show screen epi_render_screen("2")
with fade
$ renpy.pause()
show epi_tattoo44
hide screen epi_render_screen
with dissolve
$ renpy.pause()
scene epi_tattoo45 with dissolve
$ renpy.pause()
scene epi_tattoo46 with dissolve
zo "What the fuck am I doing here, Bret?"
scene epi_tattoo48 with dissolve
bre "I ask myself that question every day."
scene epi_tattoo47 with dissolve
zo "You've got something going on here. You've got your business, your own place, and your friends."
scene epi_tattoo48 with dissolve
bre "It took me a lifetime to get here, and I'm still stuck where life began."
bre "If I were brave like you, I'd leave it all behind for something new, too."
scene epi_tattoo49 with dissolve
bre "When you get stuck in a place for too long..."
bre "You lose the will to do something about it."
bre "Every day, it's the same thing."
scene epi_tattoo50 with dissolve
bre "Wake up, eat, shit, shower..."
bre "...rub one out..."
bre "Head down one floor and sit hunched over strangers."
bre "My back is killing me, my posture is becoming shit, and the money will last month-to-month with a little icing on the top."
scene epi_tattoo51 with dissolve
bre "*{i}Scoffs{/i}*"
scene epi_tattoo52 with dissolve
bre "And what scares me the most about it..."
bre "I think this is as good as it will get."
scene epi_tattoo53 with dissolve
bre "I think that right now, at this very moment... These are my golden years."
bre "Ten years from now, I will reminisce about when I sat on my rooftop drinking beer with a blue-haired teenager, talking about life."
bre "And I will call it \"the good old days\"."
scene epi_tattoo54 with dissolve
bre "Of course, Jonah will be long since gone. He'll have left us for whatever he wants to do with his life."
bre "He's the smartest guy I know - but don't tell him I told you that because I will deny ever having said it. Haha..."
bre "He's so talented too. I can't believe he works with me. But it won't be for long..."
scene epi_tattoo55 with dissolve
bre "And Ems... Ems... I don't know what she wants or where she's going."
bre "I used to think she wanted me, and now she talks about everything but me."
bre "I think it's some kind of identity crisis..."
bre "...I'm probably having one too."
scene epi_tattoo53 with dissolve
bre "Because..."
bre "...what the fuck am I doing here, Zoey?"
scene epi_tattoo56 with dissolve
zo "To me... It sounds like you're living life."
zo "You have this place with a beautiful view and the ocean breeze at night..."
scene epi_tattoo57 with dissolve
zo "If I could bottle a smell... *{i}Inhales{/i}*"
zo "...this would be it."
scene epi_tattoo58 with dissolve
zo "And you get to wake up to sunshine every morning."
zo "And get this... If you wanna go take a swim, you have the largest fucking ocean in the world a five-minute walk away."
zo "Or seven minutes if you're wearing those tight shorts."
scene epi_tattoo59 with dissolve
zo "You also get to work with what you love and what you're good at. And you really are good at it!"
zo "Sure, it seems like your body won't like your job in time, but that can be said about almost any job, can't it?"
zo "To me, it sounds like you suffer from home blindness."
scene epi_tattoo60 with dissolve
bre "Haha... Home blindness... Did Ems teach you that one?"
scene epi_tattoo61 with dissolve
zo "She did."
bre "..."
scene epi_tattoo62 with dissolve
bre "It's a good fucking expression."
scene epi_tattoo61 with dissolve
bre "*{i}Inhales{/i}*"
stop music fadeout 3
bre "*{i}Exhales{/i}*"
scene epi_tattoo62 with dissolve
bre "You're right... This is a great place to be."

label epi_hostel_label:
scene epi_hostel1 with fade
play music "music/ep8/licensed_music/track72.mp3"
$ renpy.pause()
scene epi_hostel2 with dissolve
$ renpy.pause()
scene epi_hostel3 with dissolve
$ renpy.pause()
scene epi_hostel4 with dissolve
$ renpy.pause()
scene epi_hostel6 with dissolve
$ renpy.pause()
scene epi_hostel5 with dissolve
$ renpy.pause()
scene epi_hostel9 with dissolve
mc "I'm telling you, I don't know how to draw!"
scene epi_hostel10 with dissolve
zo "But you do!"
scene epi_hostel11 with dissolve
mc "Haha! I don't!"
scene epi_hostel10 with dissolve
zo "Can't you at least try? For me?"
scene epi_hostel12 with dissolve
mc "You know I'm gonna end up ruining another page."
scene epi_hostel13 with dissolve
zo "Ruin away!"
scene epi_hostel14 with dissolve
mc "What do you want me to draw?"
scene epi_hostel15 with dissolve
zo "Whatever comes to mind!"
mc "Um... I'm drawing a blank."
scene epi_hostel16 with dissolve
zo "How about if I play the guitar, and you draw me playing it?"
scene epi_hostel17 with dissolve
mc "You can't play the guitar."
scene epi_hostel18 with dissolve
zo "I can! And you can draw!"
mc "We're probably at the same level, me with the pen and you with the guitar."
scene epi_hostel19 with dissolve
zo "I think we're both better than we think!"
zo "Now, how do you play this fucking thing?"
scene epi_hostel20 with dissolve
mc "You don't know any chords?"
zo "Dude, it all looks the same to me."
scene epi_hostel21 with dissolve
zo "You curl up your hand to make it look like my nana's hand, and somehow you make beautiful sounds."
scene epi_hostel22 with dissolve
zo "It shouldn't be so hard... Like... This!"
mc "Haha, what the fuck even is that?"
zo "It's the Z-chord!"
mc "You do know your music."
scene epi_hostel23 with dissolve
zo "If you spent more time drawing and less time being sarcastic, you'd be a pro by now."
scene epi_hostel24 with dissolve
mc "Fine, I'm drawing!"
scene epi_hostel25 with dissolve
zo "Behold! The Z-chord!"
play sound "sound_effects/interlude/zchord.mp3"
scene epi_hostel26 with vpunch
mc "Hahaha!"
zo "Haha! It sounds abstract as fuck!"
scene epi_hostel27 with dissolve
mc "If that's another word for shit, I agree."
play sound "sound_effects/interlude/zchord.mp3"
scene epi_hostel28 with dissolve
zo "The Z-chord!"
scene epi_hostel27 with dissolve
mc "If every guitar player announced their chords before they played them, no one would listen to music."
play sound "sound_effects/interlude/zchord.mp3"
scene epi_hostel29 with dissolve
zo "*{i}Sings{/i}*"
zo "[name]! He is such a dork!"
zo "He eats chocolate bars with a fork."
mc "I did that {b}one time{/b} as a joke."
play sound "sound_effects/interlude/zchord.mp3"
scene epi_hostel30 with dissolve
zo "His dick is big; his balls are less prominent."
zo "They are like two bowling balls next to the Washington Monument."
mc "What the fuck is this song, Zoey?"
play sound "sound_effects/interlude/zchord.mp3"
scene epi_hostel31 with dissolve
zo "This is an ode! An ode to your big dick!"
mc "Ok, that's enough."
play sound "sound_effects/interlude/zchord.mp3"
scene epi_hostel32 with dissolve
zo "Z-chord!"
zo "Thank you! Thank you! I'll be here all week."
mc "I'm finished."
scene epi_hostel33 with dissolve
zo "Goodie! Let me see what you got!"
scene epi_hostel34 with dissolve
mc "I did my best."
scene epi_hostel35 with dissolve
zo "Suddenly, I have a deeper understanding of cavemen's drawings."
mc "Hahaha!"
scene epi_hostel36 with dissolve
zo "*{i}Smack{/i}*"
scene epi_hostel37 with dissolve
mc "Hey. What was that for?"
scene epi_hostel38 with dissolve
zo "I...just felt like doing that."
scene epi_hostel6 with dissolve
$ renpy.pause()
stop music fadeout 3
scene epi_hostel7 with dissolve
$ renpy.pause()
scene epi_hostel8 with dissolve
$ renpy.pause()

label epi_passing_time_label:
scene epi_passing_time1 with fade
play music "music/ep_interlude/licensed_music/track106.mp3"
zo "{i}Surfing did get easier with time.{/i}"
scene epi_passing_time2 with dissolve
zo "{i}It took more practice than I'd like to admit...but I finally did it.{/i}"
scene epi_passing_time3 with dissolve
zo "{i}I rode the waves, even if it meant paddling for 10 minutes to surf for 10 seconds... I did it.{/i}"
scene epi_passing_time4 with dissolve
zo "{i}And after I got done with class, I had my other board waiting for me.{/i}"
scene epi_passing_time5 with dissolve
zo "{i}I felt kinda guilty for preferring it over the surfboard.{/i}"
scene epi_passing_time6 with dissolve
zo "{i}But at least with this board, I was good at riding something in San Diego.{/i}"
scene epi_passing_time7 with dissolve
zo "{i}I stopped writing [name] daily after the first few months...{/i}"
zo "{i}It began with a one-day break from writing him...{/i}"
scene epi_passing_time8 with dissolve
zo "{i}Then it was two...and before even knowing it...{/i}"
zo "{i}Two weeks had passed before he decided to reach out.{/i}"
scene epi_passing_time9 with dissolve
zo "{i}He told me about school and what he'd been up to.{/i}"
zo "{i}How my mom was doing fine and that she told him to say hi.{/i}"
scene epi_passing_time10 with dissolve
zo "{i}Little did he realize that I was talking to my mom more often than him for the first time in my adult life.{/i}"
scene epi_passing_time11 with dissolve
zo "{i}The words Bret told me about Ems echoed inside my head.{/i}"
zo "{i}And if there was even the tiniest chance that [name] felt more about us than he let me know...{/i}"
scene epi_passing_time12 with dissolve
zo "{i}...I hoped that I was doing him a favor by not making him remember me every day.{/i}"
zo "{i}I think it worked.{/i}"
if epi_blue_hair:
    scene epi_passing_time13b with dissolve
else:
    scene epi_passing_time13 with dissolve
zo "{i}We followed each other on Rooster. Again, I did what Ems did. I gave [name] a like or two once in a while.{/i}"
zo "{i}He didn't really post much. He isn't the kind of guy who needs to be seen or validated by others.{/i}"
zo "{i}That's one of the reasons why he's the best.{/i}"
scene epi_passing_time14 with dissolve
zo "{i}I found a studio apartment, and it was perfect.{/i}"
zo "{i}It was big and kinda expensive, but at least I didn't have to share a room with strangers anymore.{/i}"
zo "{i}That red wristband couldn't have come off faster.{/i}"
scene epi_passing_time15 with dissolve
zo "{i}But truth be told, I had a spare green wristband that I swiped from a tourist who was leaving town.{/i}"
zo "{i}It worked great at places where I wasn't well-known.{/i}"
zo "{i}I blame my blue hair for being recognizable. I did have some bar-related wristband incidents that I'm not proud of.{/i}"

scene epi_passing_time16 with dissolve
zo "{i}Bret's fears became a reality when Jonah applied for college.{/i}"
zo "{i}He had to hire a new tattoo artist - Jenna - she wasn't the best, but she sure was fun.{/i}"
scene epi_passing_time17 with dissolve
zo "{i}I'd never met a girl who could finish a whole bottle of tequila by herself and burp the alphabet before I met her.{/i}"
scene epi_passing_time18 with dissolve
zo "{i}As surfing season ended, I decided to pick up my studies. That fucking trigonometry class might suck balls, but I wasn't going to be its bitch.{/i}"
zo "{i}Thank fuck for online classes! I graduated.{/i}"
scene epi_passing_time19 with dissolve
zo "{i}But there's something about printing your diploma that doesn't feel as good as the whole Pomp and Circumstance deal.{/i}"
zo "{i}It would have been a sweeter feeling if Mom and [name] were there to see it...{/i}"
scene epi_passing_time20 with dissolve
zo "{i}I know that they would have been as happy as me about it.{/i}"
zo "{i}And also that they'd pester me about applying for college. I guess that's why I chose to graduate, but still... I'm not Jonah.{/i}"
scene epi_passing_time21 with dissolve
zo "{i}But Jonah did teach me a few things about college. That dude should be like a guidance counselor or something...{/i}"
zo "{i}He showed me these classes in graphic design that seemed fun.{/i}"
zo "{i}I had to do something else aside from working at Tattoos when I couldn't surf. So, I applied for a course.{/i}"
scene epi_passing_time22 with dissolve
zo "{i}But it turns out I'm not good enough to get accepted for anything over here.{/i}"
zo "{i}Any joy I actually felt from graduating was gone after that.{/i}"
scene epi_passing_time23 with dissolve
zo "{i}I ended up spending a lot of time with Bret. If not under his needle or on his balcony, then at the local waterhole.{/i}"
zo "{i}We got really close...{/i}"
scene epi_passing_time24 with dissolve
zo "{i}No. Not that kind of close.{/i}"
zo "{i}Well... It might have looked like it, but...{/i}"
stop music fadeout 3
zo "{i}Fuck... Here's where it got messy.{/i}"

label epi_solo_ems_label:
$ nb_state = 1
$ max_notebook_pages = 4
$ currentNotebookPage = 0
play music "music/ep7/licensed_music/track49.mp3"
scene epi_solo_ems4 with dissolve
$ ui.imagebutton("notebook_btn_alert", "notebook_btn_alert", clicked=ui.returns("OK"), xalign=0.0205, yalign=0.021)
if notifications:
    play sound "sound_effects/message.mp3"
$ renpy.pause()
zo "Hey! What's up with all the photos?"
scene epi_solo_ems7 with dissolve
em "I'm documenting our bodies. Duh!"
scene epi_solo_ems5 with dissolve
zo "Uh... What the hell is that supposed to mean?"
scene epi_solo_ems8 with dissolve
em "When you grow old, like 40 or something..."
em "You're gonna want to have pics like these."
scene epi_solo_ems5 with dissolve
zo "Pff... So I can see how hot I used to look?"
zo "That's depressing!"
scene epi_solo_ems9 with dissolve
em "It's not depressing. It's fun."
em "You're gonna remember these pics and laugh about that bitching time you had with Emma on that beach trip."
scene epi_solo_ems6 with dissolve
zo "So, the pics are for romanticizing?"
scene epi_solo_ems10 with dissolve
em "Not only. You're gonna look at your body and think, \"Damn, girl! I got out of shape! I need to head out for a run.\""
em "They'll be highly motivational."
scene epi_solo_ems11 with dissolve
em "Here. Do me. I want some non-selfie ones."
scene epi_solo_ems12 with dissolve
zo "You asked for it."
scene epi_solo_ems13 with dissolve
zo "That's the pose you're going with?"
em "What's wrong with it?"
scene epi_solo_ems15 with dissolve
zo "I'm just making sure that this is the pose that will make you wanna go out for a run in...how many years from now?"
scene epi_solo_ems14 with dissolve
em "That's for me to know and for you to shut up about."
scene epi_solo_ems15 with dissolve
zo "Haha. Ok..."
scene epi_solo_ems14 with dissolve
em "Come on! My back is starting to hurt. Snap some hot shots!"
$ tmpInt = 0
scene epi_solo_ems16 with dissolve
call screen epi_camera_screen([["Lower-body shot",740,450,680,620],["Full-body shot",1470,500,1420,680],["Upper-body shot",1250,100,1190,40]])
play sound "sound_effects/interlude/camera_shutter.mp3"
if tmpInt == 1:
    scene epi_solo_ems16a with dissolve
elif tmpInt == 2:
    scene epi_solo_ems16b with dissolve
elif tmpInt == 3:
    scene epi_solo_ems16c with dissolve

zo "These pictures are pretty lewd."

$ tmpInt = 0
scene epi_solo_ems17 with dissolve
em "Great! Keep going!"
call screen epi_camera_screen([["Lower-body shot",640,630,580,800],["Full-body shot",1200,150,1150,75],["Tit-focused shot",1300,450,1240,630],["Artistic shot",650,70,635,10]])
play sound "sound_effects/interlude/camera_shutter.mp3"
if tmpInt == 1:
    scene epi_solo_ems17a with dissolve
elif tmpInt == 2:
    scene epi_solo_ems17b with dissolve
elif tmpInt == 3:
    scene epi_solo_ems17c with dissolve
elif tmpInt == 4:
    scene epi_solo_ems17d with dissolve
$ renpy.pause()

$ tmpInt = 0
scene epi_solo_ems18 with dissolve
call screen epi_camera_screen([["Ass-focused shot",540,550,480,480],["Tit-focused shot",1070,400,1020,580],["Artistic shot",1220,100,1210,40]])
play sound "sound_effects/interlude/camera_shutter.mp3"
if tmpInt == 1:
    scene epi_solo_ems18b with dissolve
elif tmpInt == 2:
    scene epi_solo_ems18a with dissolve
elif tmpInt == 3:
    scene epi_solo_ems18c with dissolve
$ renpy.pause()

scene epi_solo_ems19 with dissolve
em "I want a couple without the top, too."
scene epi_solo_ems20 with dissolve
zo "Really? There are people over there, you know."
scene epi_solo_ems21 with dissolve
em "Exactly. They are over {b}there{/b}. Hurry up."
$ tmpInt = 0
scene epi_solo_ems22 with dissolve
call screen epi_camera_screen([["Side shot",480,550,480,480],["Front shot",1080,400,1075,580],["Artistic shot",1220,100,1210,40]])
play sound "sound_effects/interlude/camera_shutter.mp3"
if tmpInt == 1:
    scene epi_solo_ems22a with dissolve
elif tmpInt == 2:
    scene epi_solo_ems22b with dissolve
elif tmpInt == 3:
    scene epi_solo_ems22c with dissolve

$ renpy.pause()

scene epi_solo_ems23 with dissolve
em "Now for the final one."
$ tmpInt = 0
scene epi_solo_ems24 with dissolve
call screen epi_camera_screen([["Close-up shot",540,550,500,710],["Upper-body shot",1100,200,1050,380],["Artistic shot",400,300,400,240]])
play sound "sound_effects/interlude/camera_shutter.mp3"
if tmpInt == 1:
    scene epi_solo_ems24a with dissolve
elif tmpInt == 2:
    scene epi_solo_ems24b with dissolve
elif tmpInt == 3:
    scene epi_solo_ems24c with dissolve

zo "Done. Now, let's not do that again."
scene epi_solo_ems25 with dissolve
em "Lemme see 'em!"
zo "Here... I hope they aren't too tacky for you. Then again, you chose to go topless."
scene epi_solo_ems26 with dissolve
em "Too tacky? Look at me! I look hot!"
scene epi_solo_ems27 with dissolve
zo "I dare you to send one of these to someone."
scene epi_solo_ems28 with dissolve
em "How much?"
zo "It's a dare, not a bet."
em "I'm not sending them for nothing."
scene epi_solo_ems29 with dissolve
zo "How about a dollar?"
scene epi_solo_ems30 with dissolve
em "A dollar? Is that what my body's worth in your eyes? The price of a cheap burger?"
scene epi_solo_ems31 with dissolve
zo "Two...dollars?"
scene epi_solo_ems30 with dissolve
em "I'll do it if I can take pictures of you."
scene epi_solo_ems32 with dissolve
zo "One picture."
em "Two."
zo "Ok. Deal."
em "So... Who do I send these to?"
call screen zoey_choice_screen("A guy",800,100, "A girl",850,350)

show epi_solo_ems33_nocard
if not persistent.epi_card3:
    show screen epi_render_screen("3")
with dissolve

if tmp_choice == 1:
    zo "Some guy, of course."
    em "You think? Hm... Jonah, maybe?"
    call screen zoey_choice_screen("Jonah",1000,350, "Bret",1100,600)
    if tmp_choice == 1:
        $ emma_picture = 0
        show epi_solo_ems34
        hide screen epi_render_screen
        with dissolve
        zo "Yeah, let's go with Jonah."
    else:
        $ emma_picture = 1
        show epi_solo_ems35
        hide screen epi_render_screen
        with dissolve
        zo "Jonah? What a cop-out. That's like ordering a pepperoni pizza for a vegan - pointless."
        scene epi_solo_ems37 with dissolve
        em "I'm pretty sure that vegan would be pissed off."
        scene epi_solo_ems35 with dissolve
        zo "Send it to Bret."
        scene epi_solo_ems38 with dissolve
        em "To Bret? Now that's a dare..."
        scene epi_solo_ems35 with dissolve
        zo "You can bail if you want..."
        scene epi_solo_ems37 with dissolve
        em "If I do this... I'll need you to pose for three pictures."
        scene epi_solo_ems34 with dissolve
        zo "Haha, deal."
    scene epi_solo_ems39 with dissolve
    em "Haha, and sent! I told you I'd do it."
else:
    $ emma_picture = 2
    zo "I don't know, to some girl?"
    em "I got it! Jenna!"
    zo "She's working today. You're gonna make her lose focus if you send those to her."
    show epi_solo_ems37
    hide screen epi_render_screen
    with dissolve
    em "You think?"
    scene epi_solo_ems35 with dissolve
    zo "Don't you?"
    scene epi_solo_ems37 with dissolve
    em "Are you talking about...you know?"
    scene epi_solo_ems35 with dissolve
    zo "That she's into girls? Yeah?"
    scene epi_solo_ems38 with dissolve
    em "She is! Isn't she?"
    scene epi_solo_ems36 with dissolve
    zo "I think she might be. She's tough to read."
    scene epi_solo_ems39 with dissolve
    em "We'll find out with this pic."
    scene epi_solo_ems34 with dissolve
    zo "Haha! You really sent it!"
    scene epi_solo_ems39 with dissolve
    em "I told you I'd do it."
scene epi_solo_ems34 with dissolve
zo "I didn't think you'd go through with it."
scene epi_solo_ems40 with dissolve
em "You're not backing out of our deal, are you?"
scene epi_solo_ems41 with dissolve
zo "I'm not gonna do those poses you did. They were kinda nasty."
scene epi_solo_ems40 with dissolve
em "You're calling me nasty? What a bitch."

scene epi_solo_ems42 with dissolve
em "Pose for me, Zoey!"
play sound "sound_effects/interlude/camera_shutter.mp3"
scene epi_solo_ems1 with dissolve
em "Meh... Do you call that posing?"
scene epi_solo_ems42 with dissolve
em "Can't you give me a little bit nasty? These pics won't make you go for a run 20 years from now."
zo "This is so stupid."
em "Lose the top and show off your ass or something. You owe me."
play sound "sound_effects/interlude/camera_shutter.mp3"
scene epi_solo_ems2 with dissolve
em "Yes! Way better!"
if emma_picture == 1:
    scene epi_solo_ems3 with dissolve
    play sound "sound_effects/interlude/camera_shutter.mp3"
    em "And the third picture... There!"


scene epi_solo_ems43 with dissolve
zo "Now that I know you have zero inhibitions, I'll never dare you again."
scene epi_solo_ems44 with dissolve
em "I've got inhibitions. But dares are fun! They can lead to fun times."
em "Just look how awesome these pics turned out!"
scene epi_solo_ems45 with dissolve
zo "Ugh, no. What the hell, Emma...?"
em "You don't like them?"
zo "I mean, I look hot, but they are just...weird."
scene epi_solo_ems44 with dissolve
em "Tell me that in 20 years."
scene epi_solo_ems45 with dissolve
zo "Meh. I don't want those around for that long. Delete them."
scene epi_solo_ems46 with dissolve
em "Come on."
scene epi_solo_ems45 with dissolve
zo "Emma."
scene epi_solo_ems46 with dissolve
em "Fine..."
play sound "sound_effects/interlude/zoey_message.mp3"
"*{i}Phone message{/i}*"
if emma_picture == 0:
    scene epi_solo_ems47 with dissolve
    em "HAHA! Jonah just sent me a pic of his dragon!"
    zo "Yikes. That's a sad and wrinkly dragon!"
    em "Hahaha!"
elif emma_picture == 1:
    scene epi_solo_ems48 with dissolve
    zo "Is it Bret?"
    scene epi_solo_ems49 with dissolve
    em "No... It was something else."
else:
    scene epi_solo_ems47 with dissolve
    em "Wow... I think she's into girls, all right."
    scene epi_solo_ems50 with dissolve
    zo "And those are her tits..."
    em "Pretty nice, eh?"
    zo "Yeah, I'd run for those tits."

scene epi_solo_ems51 with dissolve
em "Did you get your sleeve filled in recently?"
zo "Yeah. Looks better now, right?"
if emma_joke:
    em "You're getting there. You're like 20%% tattoos now."
    scene epi_solo_ems52 with dissolve
    zo "Yeah... I think that was my last one, though."
    scene epi_solo_ems55 with dissolve
    em "Huh? So, I'm not gonna get to make one for you?"
    scene epi_solo_ems52 with dissolve
    zo "I don't wanna get carried away."
else:
    em "Sure does."
    scene epi_solo_ems56 with dissolve
    em "When are you gonna let me tattoo you?"
    scene epi_solo_ems52 with dissolve
    zo "I think I'm done getting tattoos. I don't want to get carried away."
scene epi_solo_ems55 with dissolve
em "Wow! So, you let Bret make that chest piece and that owl..."
em "And Jonah and Jenna get to work on your sleeve..."
em "Why do you hate me?"
scene epi_solo_ems53 with dissolve
zo "You never asked me to let you do one."
scene epi_solo_ems56 with dissolve
em "You never asked {b}me{/b}! And I'm asking you now!"
scene epi_solo_ems53 with dissolve
zo "I think I'm set. Or maybe a small one on my leg?"
scene epi_solo_ems55 with dissolve
em "A small one on your leg? What an insult."
scene epi_solo_ems52 with dissolve
zo "What can I tell you? I don't want more."
scene epi_solo_ems56 with dissolve
em "What about piercings? I can do your tongue."
scene epi_solo_ems53 with dissolve
zo "Hm... Maybe..."
scene epi_solo_ems56 with dissolve
em "Or your nipples?"
scene epi_solo_ems54 with dissolve
zo "My nipples?"
scene epi_solo_ems57 with dissolve
em "Yeah, it's hot. You'll love it."
em "Guys go crazy for them, and they get more erect than normal nipples."
scene epi_solo_ems54 with dissolve
zo "I don't know. I'll have to think about it. I mean, you don't even have them."
zo "Does it hurt to have them made?"
stop music fadeout 3
scene epi_solo_ems57 with dissolve
em "No. It doesn't hurt one bit."

label epi_ems_label:
play music "music/ep5/licensed_music/track6.mp3"
scene epi_ems1 with vpunch
zo "Fucking owwww!"
scene epi_ems2 with dissolve
zo "FUCK, FUCK, FUCK!!!"
em "Really? Was it worse than the first one?"
scene epi_ems3 with dissolve
zo "Yeah, I think I anticipated the pain more."
scene epi_ems4 with dissolve
em "I thought you'd become a pain junkie by now. What gives?"
scene epi_ems3 with dissolve
zo "To sum up, tattoos - fuck, yes. Titty piercings - f-f-fuck!"
scene epi_ems5 with dissolve
bre "Ems, did you see where I- Whoa..."
scene epi_ems6 with dissolve
$ renpy.pause()
scene epi_ems7 with dissolve
zo "That's one way to get him to shut up, huh?"
scene epi_ems8 with dissolve
em "Seems like it."
scene epi_ems9 with dissolve
zo "So, how long until this heals?"
scene epi_ems10 with dissolve
em "Err... It can take months up to a year, but just follow our instruction pamphlet."
scene epi_ems11 with dissolve
zo "Cool. Thanks for doing-"
scene epi_ems13 with dissolve
em "Zoey..."
em "Is there something going on between you and Bret?"
scene epi_ems12 with dissolve
zo "Me and Bret? No? Did he say something?"
scene epi_ems14 with dissolve
em "Are you fucking him?"
scene epi_ems17 with dissolve
zo "Um... Fucking him?"
zo "The dude's like ten years older than me."
scene epi_ems14 with dissolve
em "So?"
scene epi_ems17 with dissolve
zo "It's kinda grody. Also, he's my boss. Even grodier."
scene epi_ems15 with dissolve
em "What about all those Rooster posts and how you act in each other's comment sections..."
em "You're clearly flirting! Constantly! It's like watching a married couple!"
scene epi_ems17 with dissolve
zo "Stalk much? We're just having fun together."
scene epi_ems18 with dissolve
zo "Ems, I only have you guys here. Of course, I'm gonna hang out with you a lot."
zo "It doesn't mean that something is going on."
zo "Why's this a big deal to you?"
scene epi_ems16 with dissolve
em "It's not a big deal."
scene epi_ems17 with dissolve
zo "It sure seems so. You're angrily asking me if I'm fucking him."
zo "What's going on between you two?"
scene epi_ems19 with dissolve
em "Fuck off."
zo "Whoa... What just happened?"
scene epi_ems20 with dissolve
em "Maybe it's him who likes you, then. But whatever it is..."
em "I'm telling you, don't fucking date him, ok?"
scene epi_ems21 with dissolve
zo "Whoa..."
scene epi_ems20 with dissolve
em "I don't fuck your ex, and you don't fuck mine."
scene epi_ems22 with dissolve
zo "I don't dig your fucking tone!"
zo "You can't tell me what to do. And more importantly, don't fucking accuse your friend of doing that."
scene epi_ems23 with dissolve
zo "What the fuck...? Emma!?"
scene epi_ems24 with dissolve
$ renpy.pause()
scene epi_ems25 with dissolve
bre "Hey! Sorry about walking in on you..."
bre "Where's Ems? I need to ask her something."
scene epi_ems26 with dissolve
zo "She bounced."
scene epi_ems25 with dissolve
bre "Ah, fuck. I'll have to call her, then."
scene epi_ems27 with dissolve
zo "Dude, something's wrong with her."
scene epi_ems28 with dissolve
bre "With Ems?"
scene epi_ems27 with dissolve
zo "Yeah! She got pissed off at me for no reason."
zo "Or, well, she thought there was a reason, but there is none. Her mood flipped 180, and now she's mad as hell."
scene epi_ems31 with dissolve
bre "Did you last here for this long without seeing her lose her temper?"
bre "It's nothing to worry about, Zoey. I wouldn't take it personally."
scene epi_ems29 with dissolve
zo "Don't take it personally? Really?"
zo "She pretty much accused me of fucking you."
scene epi_ems28 with dissolve
bre "Oh... Why?"
scene epi_ems29 with dissolve
zo "You tell me."
scene epi_ems28 with dissolve
bre "I mean, you and I have been spending a lot of time together..."
bre "...but as friends, right?"
scene epi_ems29 with dissolve
zo "What do you mean \"right\"? Of course, as friends."
zo "I told her no and that it was grody."
scene epi_ems31 with dissolve
bre "Grody? Wow."
bre "Is it the red hair?"
scene epi_ems30 with dissolve
zo "No, but it doesn't do you any favors."
scene epi_ems31 with dissolve
bre "Kick me when I'm down, will ya?"
scene epi_ems27 with dissolve
zo "Bret. Get a grip."
scene epi_ems28 with dissolve
bre "I'll talk to her about it, ok?"
scene epi_ems30 with dissolve
zo "Ok... I'm heading home. I have some nipples to take care of."
scene epi_ems32 with dissolve
bre "Yeah, hehe."
scene epi_ems27 with dissolve
zo "Dude, how old are you? Still laughing at tits..."
scene epi_ems32 with dissolve
bre "Tits will always be funny, Zoey. You wouldn't get it."
stop music fadeout 3
scene epi_ems33 with dissolve
zo "Grody."
scene epi_ems34 with wipeleft
play music "music/ep_interlude/licensed_music/track110.mp3"
$ renpy.pause()

play sound "sound_effects/season2/vibrate.mp3"
scene epi_ems35 with dissolve
$ renpy.pause()
scene epi_ems36 with dissolve
$ text_message_screen_list = []
$ text_message_screen_list.append(["Jonah","Zoey. You better check Rooster.",True])
$ text_message_screen_list.append(["Zoey","Sup, Dragon Lord. What about it?",False])
$ text_message_screen_list.append(["Jonah","Emma just posted something about you.",True])
$ tmpInt = 0
show screen text_message_screen
play sound "sound_effects/interlude/zoey_message.mp3"
$ renpy.pause()
$ tmpInt += 1
$ renpy.pause()
scene epi_ems37 with dissolve
$ tmpInt += 1
$ renpy.pause()
hide screen text_message_screen
scene epi_ems38b with dissolve
zo "What the fuck!?"
scene epi_ems39 with wiperight
zo "Fucking pick up!"
scene epi_ems41 with dissolve
em "I don't wanna talk to you."
scene epi_ems39 with dissolve
zo "Why the fuck are those pictures on Rooster!? You said you deleted them!"
scene epi_ems41 with dissolve
em "Yeah? And you said you didn't fuck Bret!"
em "Looks like we're both liars!"
scene epi_ems40 with dissolve
zo "I didn't-!"
"*{i}Click{/i}*"
zo "Fuck!"
$ text_message_screen_list = []
$ text_message_screen_list.append("Wow! Is that you, Zoey?")
$ text_message_screen_list.append("TITS!")
$ text_message_screen_list.append("What a whore!")
$ text_message_screen_list.append("Slut!")
$ text_message_screen_list.append("A friend stealing your ex? That's disgusting!")
$ text_message_screen_list.append("Is it just me, or are those tits saggy for her age?")
$ text_message_screen_list.append("Haha! Oh my God! Zoey!")
$ tmpInt = 0
scene epi_ems42 with dissolve
show screen rooster_texts_screen
$ renpy.pause()
$ tmpInt += 1
$ renpy.pause()
$ tmpInt += 1
$ renpy.pause()
$ tmpInt += 1
$ renpy.pause()
$ tmpInt += 1
$ renpy.pause()
$ tmpInt += 1
$ renpy.pause()
$ tmpInt += 1
$ renpy.pause()
hide screen rooster_texts_screen


play sound "sound_effects/door_break.mp3"
scene epi_ems43 with hpunch
zo "Hey! What the fuck, Emma!? Delete that post! Now!"
$ guideSuggestedPage = 44
scene epi_ems44 with dissolve
em "Yeah!? I'll do that when you unfuck Bret, you skank!"
scene epi_ems45 with dissolve
if persistent.mod_wt_enabled:  
    $mod_choices = ["\n{size=44}(Zoey CHICK)","\n{size=44}(Zoey DIK)","","","","","","","","","","" ]
#[mod_gr][mod_choices[0]]
call screen zoey_choice_screen("Calm her down[mod_gr][mod_choices[0]]",1200,100, "Take her phone[mod_gr][mod_choices[1]]",1250,350)
if tmp_choice == 1:
    $ zdik(-1)
    $ emma_calm = True
    scene epi_ems68 with dissolve
    zo "I already told you I didn't fuck him. What the hell is wrong with you!?"
    scene epi_ems46 with dissolve
    em "Liar! Bret didn't deny it."
    scene epi_ems69 with dissolve
    zo "Emma... Calm down."
    zo "My friends and family can see that post!"
    zo "Don't you realize what you're doing to me?"
    stop music fadeout 3
    scene epi_ems47 with dissolve
    em "..."
    scene epi_ems69 with dissolve
    play music "music/ep6/licensed_music/track21.mp3"
    zo "Let's talk. Ok?"
    scene epi_ems47 with dissolve
    call screen zoey_choice_screen("{size=-%d}What did Bret say?{/size}" % (14 * persistent.scale_factor),150,100, "I didn't fuck him",200,350)
    if tmp_choice == 1:
        zo "What did Bret tell you?"
        scene epi_ems46 with dissolve
        em "I told you! I asked him if he was into you, and he didn't deny it!"
        scene epi_ems47 with dissolve
        zo "There's nothing to deny. It's so stupid! We're just friends."
    else:
        zo "I keep telling you I didn't fuck him."
        zo "You know me. I have no problem speaking my mind. Why would I lie?"
        scene epi_ems48 with dissolve
        em "Jeez! Why would you lie? It's exactly what someone who did it would do."
        scene epi_ems47 with dissolve
        zo "I'm not lying! Bret and I are just friends."
    scene epi_ems48 with dissolve
    em "Yeah, right."
    if emma_picture == 1:
        em "You know what his first question was after I sent him that picture of me?"
        em "He asked me if it was you who snapped it."
    scene epi_ems47 with dissolve
    if emma_picture == 1:
        zo "Yeah? So?"
    zo "What is this about, really?"
    zo "Do you still want him or something?"
    scene epi_ems49 with dissolve
    em "What!?"
    scene epi_ems50 with dissolve
    zo "I can't think of any other reason why you'd lash out at me like this."
    scene epi_ems49 with dissolve
    em "You're so fucking wrong!"
    scene epi_ems70 with dissolve
    zo "I've been nothing but nice to you. Don't you think I'd at least check with you first if I were going to date him?"
    zo "I wouldn't hurt you like that."
    scene epi_ems51 with dissolve
    em "..."
    scene epi_ems52 with dissolve
    em "Ok! I fucking love him! Is that what you want to hear?"
    em "And it's not just about you. I don't wanna see anyone date him."
    scene epi_ems53 with dissolve
    em "When I left town for Vegas, he didn't even care!"
    em "I thought I meant more to him than that."
    scene epi_ems54 with dissolve
    em "We've been friends since we were kids and lived next door to each other."
    em "I leave, and he doesn't even give a fuck?"
    scene epi_ems55 with dissolve
    em "It was just me calling him! And one day, I just said \"Fuck it\" to see if he'd pick up the phone or send me a text."
    em "And what did I get from that? Nothing!"
    em "Not a single call. Not even a fucking text saying he missed me or anything."
    scene epi_ems53 with dissolve
    em "And then, when I return home..."
    em "He treats me like a friend. Like I'm some pal he hasn't seen in a while, and that's it."
    scene epi_ems54 with dissolve
    em "He didn't even kiss me."
    scene epi_ems71 with dissolve
    zo "I think... I see where it went wrong."
    scene epi_ems56 with dissolve
    zo "Bret told me about the two of you when I first came here."
    zo "And you should probably ask him for his side of the story..."
    zo "...because it's not at all what you think it is."
    scene epi_ems57 with dissolve
    em "It's not?"
    scene epi_ems56 with dissolve
    zo "He was trying to get over you. It hurt him when you left."
    zo "He thought that you did him a favor by not calling him. You know, so that he could move on."
    scene epi_ems57 with dissolve
    em "That's not what I wanted."
    scene epi_ems56 with dissolve
    zo "He thinks it was."
    scene epi_ems58 with dissolve
    em "Bret..."
    em "*{i}Sobs{/i}*"
    scene epi_ems59 with dissolve
    $ renpy.pause()
    scene epi_ems60 with dissolve
    zo "I don't know what his feelings are for you today."
    zo "I suck balls at talking about feelings, so I never bothered to ask."
    scene epi_ems61 with dissolve
    zo "Bret and I are close, but we're just friends. I swear."
    scene epi_ems62 with dissolve
    em "Oh my God... What have I done to you?"
    scene epi_ems63 with dissolve
    em "The pictures!"
    scene epi_ems64 with dissolve
    em "They're gone!"
    if persistent.mod_wt_enabled:  
        $mod_choices = ["\n{size=44}(Zoey CHICK)","\n{size=44}(Zoey DIK)","","","","","","","","","","" ]
    #[mod_gr][mod_choices[0]]
    call screen zoey_choice_screen("It is too late[mod_gr][mod_choices[1]]",100,100, "Thank you[mod_gr][mod_choices[0]]",70,350)
    scene epi_ems65 with dissolve
    if tmp_choice == 1:
        $ zdik(1)
        zo "It's way too late to be sorry for it. My friends have already seen them."
        scene epi_ems66 with dissolve
    else:
        $ zdik(-1)
        zo "Thank you, Emma..."
        scene epi_ems66 with dissolve
    em "I'm so fucking sorry! I don't know what came over me!"
    stop music fadeout 3
    em "I just- *{i}Sobs{/i}*"
    scene epi_ems67 with dissolve
    $ renpy.pause()
    jump epi_eb_label
else:
    $ zdik(1)
    $ emma_calm = False
    scene epi_ems72 with dissolve
    $ renpy.pause()
    scene epi_ems73 with dissolve
    $ renpy.pause()
    play sound "sound_effects/shove.mp3"
    scene epi_ems74 with vpunch
    em "No! Give me that!"
    scene epi_ems75 with dissolve
    zo "Fuck you! You can't put me on Rooster like that!"
    zo "Do you have any idea of what you're doing to my life!?"
    play sound "sound_effects/shove.mp3"
    scene epi_ems76 with hpunch
    $ renpy.pause()
    scene epi_ems77 with dissolve
    zo "Ouch... What the...?"
    scene epi_ems78 with dissolve
    em "Get the fuck out! Now!"
    scene epi_ems79 with dissolve
    $ renpy.pause()
    play sound "sound_effects/shove.mp3"
    scene epi_ems80 with hpunch
    zo "Not without that phone!"
    scene epi_ems81 with dissolve
    em "Hey! Stop!"
    play sound "sound_effects/door_slam.mp3"
    scene epi_ems82 with hpunch
    play sound "sound_effects/door_lock.mp3"
    em "Give me back my phone!"
    play sound "sound_effects/door_bang.mp3"
    scene epi_ems83 with hpunch
    em "Zoey! Open up!"
    scene epi_ems84 with dissolve
    em "Zoey! Give it a fucking rest! That's my phone!"
    scene epi_ems85 with dissolve
    zo "Yeah!? And those are my nude pictures you posted, bitch!"
    scene epi_ems84 with dissolve
    em "You fucking whore! You won't be able to unlock the phone anyway!"
    scene epi_ems85 with dissolve
    zo "Yeah, it's not like I've been working next to you for all this time and seen you use 4321 as the code daily! Fucking original!"
    play sound "sound_effects/door_bang.mp3"
    scene epi_ems83 with hpunch
    em "ZOEY!!!"
    scene epi_ems86 with dissolve
    zo "(Fucking deleted that shit!)"
    zo "(And the gallery too!)"
    if persistent.mod_wt_enabled:  
        $mod_choices = ["\n{size=44}(Zoey CHICK)","\n{size=44}(Zoey DIK)","","","","","","","","","","" ]
    #[mod_gr][mod_choices[0]]
    call screen zoey_choice_screen("Get revenge",1300,100, "{size=-%d}Be a bigger person{/size}" % (5 * persistent.scale_factor),1420,350)
    if tmp_choice == 1:
        $ zdik(1)
        $ emma_cluck = True
        scene epi_ems87 with dissolve
        zo "Let's see how you like having your nude pictures on Rooster... You fucking bitch."
    else:
        $ zdik(-1)
        $ emma_cluck = False
        scene epi_ems87 with dissolve
        zo "There. Gone!"
    scene epi_ems86 with dissolve
    em "I'm gonna kick your ass!"
    if emma_cluck:
        play sound "sound_effects/season2/flush.mp3"
        scene epi_ems88 with dissolve
        zo "Whoops! Dropped your phone!"
        em "Zoey!!!"
    else:
        scene epi_ems89 with dissolve
        zo "..."
    em "I'm getting my toolbox! You hear me!?"
    stop music fadeout 3
    play sound "sound_effects/interlude/bark.mp3"
    scene epi_ems90 with dissolve
    jump epi_after_label

label epi_eb_label:
play music "music/ep_interlude/licensed_music/track112.mp3"
scene epi_eb1 with dissolve
zo "{i}I was furious about that post. And I don't know what came over me...{/i}"
zo "{i}I was so close to just snatching her phone, but instead, I talked to her about it.{/i}"
scene epi_eb2 with dissolve
zo "{i}And it's probably for the better. I don't see myself patching it up with Emma if I hadn't tried to calm her down that night.{/i}"
scene epi_eb3 with dissolve
zo "{i}I haven't fully forgiven her for what she did, but I kinda understand her better now.{/i}"
zo "{i}Love does crazy things with your head.{/i}"
scene epi_eb4 with dissolve
zo "{i}It hadn't occurred to me that she still had feelings for Bret.{/i}"
zo "{i}In a way, Emma and I are more alike than I'd like to admit.{/i}"
zo "{i}We both suck at expressing ourselves. She does get angrier than me when she tries to, though.{/i}"
scene epi_eb5 with dissolve
zo "{i}She eventually told Bret about her feelings for him.{/i}"
zo "{i}It took a lot of liquid courage, and the timing was kinda bad.{/i}"
scene epi_eb6 with dissolve
em "I think I love you."
scene epi_eb10 with dissolve
bre "Haha, I love you too."
scene epi_eb7 with dissolve
em "Nooo... You don't get it!"
em "I love you!"
scene epi_eb10 with dissolve
bre "And I love you!"
scene epi_eb7 with dissolve
em "Aargh! You still don't get it!"
scene epi_eb8 with dissolve
em "Why didn't you fight for me? When I went to Vegas..."
em "You didn't fight for me."
scene epi_eb11 with dissolve
$ renpy.pause()
scene epi_eb12 with dissolve
$ renpy.pause()
scene epi_eb13 with dissolve
bre "You love me?"
scene epi_eb8 with dissolve
em "That's what I'm trying to tell you!"
em "You never called me or anything. Why?"
scene epi_eb13 with dissolve
bre "No, you stopped calling me."
scene epi_eb8 with dissolve
em "To see if you would call me!"
scene epi_eb13 with dissolve
bre "I don't get it."
scene epi_eb8 with dissolve
em "I wished you had called me."
scene epi_eb13 with dissolve
bre "I- I didn't think you wanted me to."
scene epi_eb8 with dissolve
em "I wanted you to."
scene epi_eb13 with dissolve
bre "Then why did you leave?"
scene epi_eb9 with dissolve
em "I was bored! I wanted to try something new. I thought that working in a casino would be the coolest thing ever, but it sucks when you have to be sober."
em "People keep spitting on you when they get too drunk. The cards get all sticky."
scene epi_eb13 with dissolve
bre "I thought you were over me."
scene epi_eb14 with dissolve
em "*{i}Smack{/i}* I wasn't..."
scene epi_eb15 with dissolve
em "Fuck me. Hard. Like you used to in the past."
scene epi_eb16
jon "So... We're gonna head out."
scene epi_eb17 with dissolve
em "No, stay!"
jon "Hard pass."
em "Not you. Zoey! Stay!"
scene epi_eb18 with dissolve
zo "Nah, I should bounce, too. You should prolly talk some more."
scene epi_eb19 with dissolve
em "Zoey, I think... I think I might be getting back together with him."
scene epi_eb23 with dissolve
bre "Ems-"
scene epi_eb21 with dissolve
em "Shh! Girl talk over here! Ok?"
scene epi_eb22 with dissolve
zo "If that's what you guys want, go for it."
scene epi_eb19 with dissolve
em "Do you think it's a bad idea?"
scene epi_eb22 with dissolve
zo "I think you should have this talk when you're sober, or at least when Bret's not half-asleep."
scene epi_eb19 with dissolve
em "Have you ever had a threesome?"
scene epi_eb22 with dissolve
zo "I see where this is going, but no... Take care, Ems."
scene epi_eb19 with dissolve
em "You never did fuck him, did you?"
scene epi_eb22 with dissolve
zo "Finally, you're catching on."
scene epi_eb20 with dissolve
em "Haha..."
label epi_eb_lewd_label:
if _in_replay:
    play music "music/ep_interlude/licensed_music/track112.mp3"
scene epi_eb24 with dissolve
em "*{i}Smack{/i}*"
scene epi_eb25 with dissolve
bre "*{i}Smack{/i}*"
scene epi_eb26 with dissolve
em "Mmm..."
scene epi_eb27 with dissolve
jn "Don't mind me, guys. Hump ahoy!"

scene epi_eb30 with dissolve
zo "{i}What happened after I left, that's their business.{/i}"
zo "{i}I wish that were the case... Emma called me one hour later with the deets.{/i}"
zo "{i}Apparently, it went something like this.{/i}"

scene anim_eb_doggy_epi with dissolve
em "Fuck me, Bret!"
bre "My head is fucking spinning, Ems."
scene anim_eb_doggy2_epi with dissolve
em "Do you got whiskey dick? It's a bit softer than I remember."
bre "I'll get there..."
pause

scene anim_eb_bj_epi with dissolve
em "Come, baby. Let me make it harder for you."
em "*{i}Suck suck{/i}*"
pause
scene anim_eb_bj2_epi with dissolve
em "*{i}Schlurp smack{/i}* Mmppfhh... That's it..."
pause
scene anim_eb_bj3_epi with dissolve
bre "It's getting hard, Ems!"
em "Hell yeah, it is!"
scene epi_eb29 with dissolve
jn "Yay! Go, Bret!"


scene epi_eb33 with dissolve
em "Whoa, that's the wrong hole!"
bre "Huh?"
em "Bret! That's my asshole."
scene epi_eb28 with dissolve
jn "Oh, no... Not in the asshole."

scene epi_eb34 with dissolve
em "Damn... Ok... Keep going."

scene anim_eb_anal_epi with dissolve
em "Hngn..."
pause
scene anim_eb_anal2_epi with dissolve
em "I've fucking missed you so much."
bre "Huh?"
em "Fuck me, Bret! Fuck me!"
pause
scene anim_eb_anal3_epi with dissolve
em "HARDER! FUCK MY ASS!"
jn "Yay!"
pause

scene epi_eb35 with dissolve
em "Hey, you're going soft again."
scene epi_eb36 with dissolve
bre "Well... The old man is staring at me."

stop music fadeout 3
scene epi_eb37 with dissolve
zo "{i}Yeah... I should have hung up the phone.{/i}"

scene epi_eb31 with dissolve
play music "music/ep_interlude/licensed_music/track111.mp3"
zo "{i}They were drunk and had some fun. I was happy for them.{/i}"
zo "{i}But when I saw them avoid talking about it in the days that followed...{/i}"
zo "{i}...I felt like they regretted it.{/i}"
zo "{i}I wasn't expecting them to get back together overnight, but they seemed to be in denial.{/i}"
zo "{i}I found it stupid. Going by the awkward moments, they both clearly remembered it.{/i}"
scene epi_eb32 with dissolve
jn "Whiskey-dick Bret!"
zo "{i}And if they didn't, they had Jenna to remind them about it.{/i}"
$ renpy.end_replay()
$ persistent.epi_lewd_eb = True
$ calcScenes()

scene epi_summer1 with dissolve
zo "{i}Hopefully, they'd revisit the topic another night. But I don't know what happened.{/i}"
zo "{i}And frankly, there were other big things on my mind.{/i}"
zo "{i}And I couldn't run from those thoughts any longer.{/i}"

jump epi_summer_label


label epi_after_label:
zo "{i}I didn't handle that situation well...{/i}"
zo "{i}But if you put two firecrackers in a barrel, you will get a bigger explosion.{/i}"
play music "music/ep_interlude/licensed_music/track111.mp3"
scene epi_eb2 with dissolve
zo "{i}Work was awkward as fuck after that day.{/i}"
zo "{i}Emma was staring daggers at me daily, and any time Bret asked her what was wrong, she'd ignore him.{/i}"
scene epi_after3b with dissolve
zo "{i}What the hell was her problem!?{/i}"
zo "{i}No one reposted the pictures of me, at least. I got some DMs from friends about it...{/i}"
zo "{i}They asked me why I had those pictures of myself to begin with.{/i}"
scene epi_after5 with dissolve
zo "{i}At least I looked kinda hot in the pictures... It makes me feel a bit better about it, but I wouldn't wish this on anyone.{/i}"
scene epi_after6 with dissolve
zo "{i}I talked to both Jonah and Bret about it.{/i}"
zo "{i}Jonah was very supportive.{/i}"
zo "{i}He tried to explain what probably went wrong. He didn't take Emma's side, but he wasn't shitting on her either.{/i}"
scene epi_after7 with dissolve
zo "{i}I'll take his word for it that there's something more to Emma than she lets on. But I'll never see it.{/i}"
zo "{i}I don't want anything to do with her after this.{/i}"
scene epi_after8 with dissolve
zo "{i}As for Bret... He lost some of my respect after I told him about what Emma did...{/i}"
zo "{i}He just wants everyone to be happy all the time, and while that's a nice thought, it's not how life is.{/i}"
zo "{i}In a room full of 100 people, you're bound to make both friends and enemies, and the rest just become a bunch of whatevers.{/i}"
scene epi_after9 with dissolve
zo "{i}Bret wanted us to kiss and make up. And the more he pushed for it, the more annoyed I got.{/i}"
zo "{i}He's still an awesome dude, but he's too wishy-washy at times.{/i}"
scene epi_after10 with dissolve
zo "{i}There was no way that Emma would apologize to me after that.{/i}"
if emma_cluck:
    zo "{i}The cluck I posted with her pics nailed the coffin and put it in wet cement.{/i}"
scene epi_summer1 with dissolve
zo "{i}But it didn't matter...{/i}"
zo "{i}Because, all of this put aside, there were other big things on my mind.{/i}"
zo "{i}And I couldn't run from those thoughts any longer.{/i}"
jump epi_summer_label

label epi_summer_label:
hide screen notebook_button_screen
scene epi_summer2 with dissolve
if minigames:
    $ renpy.pause(0.5)
    jump epi_drawing_game3_label
    label epi_after_drawing3_label:
else:
    $ renpy.pause()

if minigames and steamAchievements and not config.console and not config.developer:
    if len(epi_draw_scores) == 3 and epi_draw_scores[0]=="s" and epi_draw_scores[1]=="s" and epi_draw_scores[2]=="s":
        $ achievement.grant("IDS3_18")
        init:
            $ achievement.register("IDS3_18")
        $ achievement.Sync()

scene epi_summer3 with dissolve
$ renpy.pause()
play sound "sound_effects/door_knock.mp3"
"*{i}Doorknock{/i}*"
scene epi_summer4 with dissolve
zo "Who is it!?"
scene epi_summer5 with dissolve
bre "Hey! It's just me."
bre "I was in the area."
scene epi_summer6 with dissolve
zo "You were?"
scene epi_summer7 with dissolve
bre "Well... It's lunchtime, and you didn't show up for work today..."
scene epi_summer13 with dissolve
zo "Sorry... I was going to, but I didn't get out of bed until just now."
scene epi_summer8 with dissolve
bre "..."
scene epi_summer9 with dissolve
bre "Fuck work... We haven't even had a single customer today."
bre "Wanna go to the beach instead? It looks like you could use it."
scene epi_summer11 with dissolve
zo "I don't know. I kinda feel like doing nothing today."
scene epi_summer10 with dissolve
bre "Is something wrong?"
scene epi_summer11 with dissolve
zo "Lately... Yeah."
scene epi_summer10 with dissolve
if emma_calm:
    bre "It's not about Ems again, right?"
else:
    bre "It's not the thing with Ems, right?"
scene epi_summer12 with dissolve
if emma_calm:
    zo "No, I'm way over that post."
else:
    zo "No, I couldn't give less of a shit about her."
scene epi_summer7 with dissolve
bre "Then, what's bugging you?"
scene epi_summer11 with dissolve
zo "Where do I start...?"
scene epi_summer7 with dissolve
bre "Somewhere... Anywhere?"
scene epi_summer11 with dissolve
zo "I'm running out of money."
scene epi_summer10 with dissolve
bre "Shit... I know the pay is bad, but I'll see what I can do about it-"
scene epi_summer13 with dissolve
zo "No, don't. I know you're already stretching your budget more than you can afford."
scene epi_summer9 with dissolve
bre "I wish I could tell you no to that, but you already know the nasty truth."
scene epi_summer10 with dissolve
bre "Well, you could look for another job. Don't let me keep you from it."
bre "There would be no hard feelings if you did."
scene epi_summer13 with dissolve
zo "It's not just about the money."
scene epi_summer10 with dissolve
bre "Then what is it?"
scene epi_summer14 with dissolve
zo "When I came here, I wanted to pursue a dream, you know?"
zo "Thanks to my grandma, I could give it a go, but the money she left me didn't last as long as I thought it would..."
scene epi_summer15 with dissolve
zo "And that makes me feel like I've wasted it all."
zo "I'm not a surfer. And Floyd was right; I can't make any money off it."
scene epi_summer16 with dissolve
zo "I honestly like it way less than I thought I would."
scene epi_summer17 with dissolve
zo "I love the skateboard she got me. Not just because it reminds me of her but because it's something I'm good at."
zo "Just like drawing... That's also something I'm great at!"
scene epi_summer18 with dissolve
zo "The waves aren't me. This apartment isn't me. The reception of your tattoo studio isn't me."
zo "{b}This{/b} isn't me."
scene epi_summer19 with dissolve
zo "And it fucking hurts. Because all this time, I thought that it was me."
zo "I wanted it to be me. And now..."
scene epi_summer20 with dissolve
zo "I fucking let her down. *{i}Sobs{/i}*"
scene epi_summer21 with dissolve
bre "Hey..."
scene epi_summer22 with dissolve
zo "I miss her so fucking much, Bret."
zo "It still hurts. And I didn't even get to say goodbye to her."
scene epi_summer23 with dissolve
zo "Everyone I've talked to says that time will take care of it, but it's not doing that for me!"
zo "I feel so much more alone than I ever did when she was alive."
scene epi_summer24 with dissolve
$ renpy.pause()
scene epi_summer25 with dissolve
bre "I didn't know your grandma, but based on the stories you've told me about her..."
bre "I can't imagine that she'd feel let down by you not liking it here."
bre "She wanted you to pursue what made you happy in life, didn't she?"
scene epi_summer27 with dissolve
zo "That's all she ever wanted for me."
scene epi_summer25 with dissolve
bre "You jumped on a train, leaving your old life behind for this because you thought you wanted it."
bre "And when you realize that it isn't what you wanted, her wish for you doesn't change, does it?"
scene epi_summer26 with dissolve
bre "She'd still want you to go for whatever you want next."
bre "And you should keep doing that."
bre "If I were your grandma, I would have been proud as fuck."
scene epi_summer28 with dissolve
zo "*{i}Sniffs{/i}* Haha... If you were my grandma..."
zo "Thanks, Bret..."
scene epi_summer29 with dissolve
bre "So, what do you feel? What are you dreaming of right now?"
scene epi_summer30 with dissolve
$ renpy.pause()
scene epi_summer31 with dissolve
zo "I dream..."
zo "I dream of going back home."
scene epi_summer32 with dissolve
bre "Wow..."
bre "You're gonna make me cry, too, you know."
scene epi_summer33 with dissolve
bre "How can I say that I want you to do that while knowing how much I will miss you?"
scene epi_summer34 with dissolve
zo "I know."
if emma_calm:
    zo "You've meant so much to me, Bret. You, Jonah, and Ems are the reasons why it's hard to leave."
else:
    zo "You've meant so much to me, Bret. You and Jonah are the reasons why it's hard to leave."
scene epi_summer33 with dissolve
bre "The good old days..."
scene epi_summer34 with dissolve
zo "I think you still have a few good years in you."
scene epi_summer33 with dissolve
bre "Promise you'll call once in a while."
scene epi_summer34 with dissolve
zo "Call? I'll fucking come back to visit. You know it."
zo "And we can meet up somewhere too, you know."
scene epi_summer35 with dissolve
zo "Here..."
zo "I drew this for you."
scene epi_summer36 with dissolve
bre "Bret's Metal and Ink?"
zo "In case you wanted a different name or whatever."
scene epi_summer37 with dissolve
bre "Zoey... I love it. Thanks."
stop music fadeout 3
scene epi_summer38 with dissolve
$ renpy.pause()

label epi_train_home_label:
play music "music/ep_interlude/licensed_music/track107.mp3"
scene epi_summer41 with dissolve
zo "{i}And here we are...{/i}"
zo "{i}I gave it my all, but it wasn't as good as young Zoey dreamt it would be when she played with a wooden plank as a surfboard as her grandma cheered her on.{/i}"
scene epi_summer42 with dissolve
zo "{i}In reality, the waves swallowed me and my surfboard whole before I learned how to ride them.{/i}"
zo "{i}I will always bear those feelings with me.{/i}"
zo "{i}The feeling of how I hated being a loser when I fell off the surfboard.{/i}"
scene epi_summer43 with dissolve
zo "{i}The feeling of how I didn't enjoy surfing and how cold the water was.{/i}"
zo "{i}The wonderful feeling of skating back home to take a hot shower after a day of pretending I was a banana in the ocean.{/i}"
zo "{i}The people I met and how much they came to mean to me.{/i}"
scene bg anim_zoey_spot_epi movie with dissolve
zo "{i}But ultimately...the feeling that I was missing something I couldn't put my finger on.{/i}"
zo "{i}The feeling I tried so hard to push back and ignore.{/i}"
pause
scene epi_summer44 with dissolve
$ renpy.pause()
scene epi_summer39 with dissolve
zo "{i}Home blindness.{/i}"
if emma_calm:
    zo "{i}It took a black-haired badass, a shaven teddy bear, and a red-haired, tight-pants-wearing goofball to teach me to love my hometown and the people in it.{/i}"
else:
    zo "{i}It took a black-haired bitch, a shaven teddy bear, and a red-haired, tight-pants-wearing goofball to teach me to love my hometown and the people in it.{/i}"
scene epi_summer40 with dissolve
zo "{i}So, now...{/i}"
zo "{i}I'm heading back home.{/i}"

label epi_ending_label:
scene epi_ending1 with dissolve
$ renpy.pause()
scene epi_ending2 with dissolve
$ renpy.pause()
scene epi_ending3 with dissolve
$ renpy.pause()
scene epi_ending4 with dissolve
$ renpy.pause()
scene epi_ending5 with dissolve
$ renpy.pause()
scene epi_ending6 with dissolve
$ renpy.pause()
scene epi_ending7 with dissolve
$ renpy.pause()
scene epi_ending8 with dissolve
$ renpy.pause()
scene epi_ending9 with dissolve
$ renpy.pause()
scene epi_ending10 with dissolve
$ renpy.pause()
scene ep8_ending17 with dissolve
$ renpy.pause()
scene ep8_ending18 with dissolve
$ renpy.pause()
scene ep8_ending19 with dissolve
$ renpy.pause()
scene bg anim_ending_zoey_ep8 movie with dissolve
$ renpy.pause()
stop music fadeout 5

$ chat_new_tasks = False
$ current_task = ""
$ freeRoamID = ""
$ loopMusic = False
$ pack_quest_available = False
$ disabled_apps = ["music","brawler","tripletile","shuffle","vault"]
$ task_list = [""]
$ optional_task_list = [""]
$ map_system_list = []
$ mphone_contacts_clear()
$ updateTaskList()
$ mphone_rooster_clear()
$ mphone_pack_quest_clear()
$ map_fast_travel_enabled = True
hide screen map_screen
hide screen map_minimap_screen
$ randInt = renpy.random.randint(0, 17)

label mc_ending_epi_label:
scene epi_ending20 with dissolve
$ disabled_apps = []
$ disabled_apps.append("settings")
show screen new_phone_screen
if persistent.golden_phone and persistent.golden_phone_skin_enabled:
    $ ui.imagebutton("mphone_btn_golden_hover", "mphone_btn_golden_hover", clicked=ui.returns("OK"), xalign=0.02, yalign=0.0198)
else:
    $ ui.imagebutton("mphone_btn_hover", "mphone_btn_hover", clicked=ui.returns("OK"), xalign=0.02, yalign=0.0198)
$ renpy.pause(2)
$ renpy.pause()
scene epi_ending21 with dissolve
$ renpy.pause()
if branchSage and ep4_fuckedJade:
    scene epi_ending22b with dissolve
    $ renpy.pause()
elif ep4_fuckedJade or branchSage:
    scene epi_ending22a with dissolve
    $ renpy.pause()
else:
    scene epi_ending22 with dissolve
    $ renpy.pause()
play sound "sound_effects/cellphone.mp3"
"*{i}Cellphone rings{/i}*"
show epi_ending23_nocard
if not persistent.epi_card4:
    show screen epi_render_screen("4")
with dissolve
mc "Dad. Now is not a good time for me. I-"
show epi_ending24
hide screen epi_render_screen
with dissolve
mc "Wait, what!?"
mc "S-she's back? Why?"
scene epi_ending25 with dissolve
mc "Uh... I guess..."
scene epi_ending26 with dissolve
mc "..."
scene epi_ending27 with dissolve
mc "Give her my new number."
mc "Yeah, my old phone is switched off."
scene epi_ending28 with dissolve
mc "Hey..."
mc "Is she ok?"
scene epi_ending29 with dissolve
$ renpy.pause()
scene epi_ending28 with dissolve
mc "I see."
play sound "sound_effects/door_bang.mp3"
scene epi_ending31 with vpunch
sa "[name]! You better fucking open up!"
scene epi_ending30 with dissolve
mc "Dad, I gotta go."
stop music
scene black
$ renpy.pause(2)
if zoey_dk >= 0:
    $ zoey_dik = True
else:
    $ zoey_dik = False
label interlude_save_here_label:
hide screen new_phone_screen
$ persistent.episode_interlude = True

if steamAchievements:
    $ achievement.grant("IDS3_01")
    init:
        $ achievement.register("IDS3_01")
    $ achievement.Sync()
    call check_steam_achievements_label from _call_check_steam_achievements_label_1

if renpy.loadable("scripts/episode9/update9.rpyc"):
    scene epi_episode_endb
else:
    scene epi_episode_end

$ renpy.pause()

scene black
label interludeEndLabel:
if renpy.loadable("scripts/episode9/update9.rpyc"):
    jump startUpdate9
else:
    jump endOfVersionInterlude

label endOfVersionInterlude:
$ qM = persistent.quick_menu
$ persistent.quick_menu = 0
jump game_credits
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
