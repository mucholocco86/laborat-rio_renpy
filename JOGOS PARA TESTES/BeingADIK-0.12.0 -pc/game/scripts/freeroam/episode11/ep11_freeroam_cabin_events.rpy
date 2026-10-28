label ep11_trip_label:

if branchIsabella and branchJill:

    "scrappy" "Play the cabin trip with?"
    menu:
       "Isabella":
         $tmp_mod2="Isabella"
       
       "Jill":
         $tmp_mod2="Jill"

elif branchIsabella:
       $tmp_mod2="Isabella"

elif branchJill:
    $tmp_mod2="Jill"
play music "music/ep1/winter_sunshine.mp3"
scene ep11_trip1
show screen ep10_snow_screen
with fade
$ renpy.pause()
scene ep11_trip2
hide screen ep10_snow_screen
with dissolve
mc "Are we there yet?"
scene ep11_trip4 with dissolve
ji "I told you it was a long drive."
scene ep11_trip2 with dissolve
mc "Yeah, but I didn't picture it being this long."
scene ep11_trip4 with dissolve
ji "Luckily for you, we're almost there."
scene ep11_trip3 with dissolve
mc "The thing is, you said that an hour ago, and now I have trust issues."
scene ep11_trip5 with dissolve
ji "Haha, but we are almost there. There's only one more left turn on this road before we're there."
scene ep11_trip6 with dissolve
isa "That one, right?"
scene ep11_trip5 with dissolve
ji "Yes, there it is. See, I told you we were almost there."
scene ep11_trip2 with dissolve
mc "How long do we have to drive on that road, though?"
scene ep11_trip5 with dissolve
ji "We're almost there, haha."
$ phone_bars_zero = True
scene ep11_trip7
show screen ep10_snow_screen
with dissolve
ji "Look, there it is. And that's Bianca's parent's car."
isa "It's beautiful. What a comfy-looking cabin."
mc "Wow, it's not at all how I had pictured it."
play sound "sound_effects/season3/car_door.mp3"
scene ep11_trip8 with dissolve
ji "You're going to love it here. I've only been here one time, but it was the best."
scene ep11_trip9 with dissolve
bia "Hey, everyone! Welcome!"
scene ep11_trip10 with dissolve
bia "How was your trip? Did you remember how to find the place?"
scene ep11_trip11 with dissolve
ji "I remembered. It was a fun trip, but longer for some than others."
scene ep11_trip12 with dissolve
mc "I'm some. It was a long one, yeah. But I'm happy to be here."
scene ep11_trip13 with dissolve
bia "Me too! We're gonna have so much fun!"
scene ep11_trip14 with dissolve
bia "Oh! Before I forget. The reception is crap out here."
bia "You can find a sweet spot in this area if you're lucky, but I've never gotten more than a single bar."
bia "I hope you're not expecting any important calls."
scene ep11_trip18 with dissolve
isa "Zero bars. I might as well turn the phone off until Sunday."
scene ep11_trip14 with dissolve
bia "Yeah, and don't panic. It's a 20-minute drive to the nearest town if you need it."
if not ep9_told_jill:
    scene ep11_trip17 with dissolve
    ji "Is Matthew here?"
    scene ep11_trip16 with dissolve
    bia "He had to cancel. Can you believe it?"
    bia "He had a work meeting tomorrow. There was some crisis he had to manage."
    bia "It sucks for him, but I wasn't going to skip this trip."
    scene ep11_trip17 with dissolve
    ji "Aw, that's too bad."

scene ep11_trip15 with dissolve
bia "Let's get inside. I want to show the newcomers the place."
$ renpy.sound.play("sound_effects/season3/fireplace.mp3", channel="sfx2", loop=True)
scene ep11_trip19
hide screen ep10_snow_screen
with wipeleft
bia "This is it! Our humble family cabin."
scene ep11_trip20 with dissolve
bia "Ok, it's not that humble. It's modern."
bia "But its size makes it somewhat humble."
scene ep11_trip21 with dissolve
bia "It's not a big place, but it has what we need."
scene ep11_trip22 with dissolve
bia "Also, beware of this stupid beam; you might hit your head on it if you're not careful."
scene ep11_trip23 with dissolve
bia "So, this is it. You have the kitchen and dining room over there."
scene ep11_trip24 with dissolve
bia "This is the \"after-ski area\", as Dad loves to call it. It's hands down the best spot in the cabin."
bia "Whenever you see the fire needs it, go ahead and stoke it."
scene ep11_trip28 with dissolve
isa "This both smells and sounds lovely."
scene ep11_trip30 with dissolve
bia "Doesn't it? My family loves gathering around the fire at night."
scene ep11_trip25 with dissolve
bia "Up that ladder, you'll find a smaller guest room. It's for sleeping purposes only since it's so small."
scene ep11_trip26 with dissolve
bia "Behind that door, you will find the master bedroom, toilet, and shower. It's inconvenient since you must pass through the bedroom to get there."
bia "And that's pretty much the place."
scene ep11_trip31 with dissolve
bia "No, wait! We also have a sauna and hot tub outside. You guys brought bathing suits, right?"
scene ep11_trip32 with dissolve
mc "It's outside? But it's freezing."
scene ep11_trip33 with dissolve
bia "Have you ever sat in the sauna and bathed in the snow before?"
scene ep11_trip32 with dissolve
mc "No? Who does that? The closest thing I can think of is losing in a snowball fight."
scene ep11_trip34 with dissolve
ji "You're either going to love or hate it. It's quite the experience."
scene ep11_trip29 with dissolve
isa "I'm going to enjoy watching that."
if branchJill and tmp_mod2=="Jill":
    scene ep11_trip27 with dissolve
    bia "Jill and [name], you guys can take the big bedroom, and I'll bunk up with Bella in the small one."
    bia "Is that ok for everyone?"
    scene ep11_trip28 with dissolve
    isa "That will work fine."
    scene ep11_trip39 with dissolve
else:
    scene ep11_trip35 with dissolve
    bia "I'm not quite sure how we should split the rooms. Any suggestions?"
    scene ep11_trip36 with dissolve
    ji "I think [name] and Bella want a room of their own."
    scene ep11_trip37 with dissolve
    bia "Oh?"
    scene ep11_trip38 with dissolve
    bia "Oh!"
    scene ep11_trip40 with dissolve
    bia "Uhh... Ok, you two take the master bedroom, and Jill and I bunk in the other one."
    scene ep11_trip38 with dissolve
    bia "Sorry, I had no idea that you two were..."
    scene ep11_trip41 with dissolve
    isa "It's...nothing we flaunt."
    scene ep11_trip39 with dissolve
    bia "I think it's great. I love both of you guys."

bia "I hope you guys already ate dinner. I thought we could end the night with some cocoa and then get up bright and early for a day full of fun."
bia "Jill, can you help me in the kitchen?"
scene ep11_trip42 with dissolve
$ renpy.pause()
if branchIsabella and tmp_mod2=="Isabella":
    scene ep11_trip43 with dissolve
    $ renpy.pause()
    scene ep11_trip44 with dissolve
    $ renpy.pause()
    scene ep11_trip45 with dissolve
    mc "Our first trip together. Feels nice, doesn't it?"
    scene ep11_trip46 with dissolve
    isa "It does feel nice to get away with you."
    scene ep11_trip45 with dissolve
    mc "You don't mind the company, right?"
    scene ep11_trip46 with dissolve
    isa "Of course not."
    scene ep11_trip47 with dissolve
    isa "I admit I felt a tad nervous when Bianca realized that we..."
    isa "That we are together."
    scene ep11_trip48 with dissolve
    isa "But it also feels good because it means we can be ourselves out here and not hide."
    scene ep11_trip49 with dissolve
    mc "I must admit I felt better when I thought it was ok for us to have a relationship."
    scene ep11_trip51 with dissolve
    isa "..."
    scene ep11_trip48 with dissolve
    isa "Let's enjoy the good feeling we get here this weekend, ok?"
    scene ep11_trip49 with dissolve
    mc "Sure. That's why I'm here."
    scene ep11_trip50 with dissolve
    $ renpy.pause()
    scene ep11_trip52 with dissolve
    isa "*{i}Smack{/i}*"
else:
    scene ep11_trip53 with dissolve
    $ renpy.pause()
    scene ep11_trip54 with dissolve
    isa "This would be a nice place to live, don't you think?"
    scene ep11_trip55 with dissolve
    mc "Out here? Far from everyone? I'm not sure."
    mc "I think it's nice for the weekend, but I'd get lonely."
    scene ep11_trip54 with dissolve
    isa "Hm, yes. Maybe a bigger community wouldn't hurt, but this place has its charms."
    scene ep11_trip56 with dissolve
    mc "If you're moving, can I have your house?"
    scene ep11_trip57 with dissolve
    isa "That would be something, eh?"
    scene ep11_trip58 with dissolve
    mc "I'd take good care of your pool."
    scene ep11_trip57 with dissolve
    isa "You better."
    scene ep11_trip58 with dissolve
    mc "With a place like yours, I wouldn't ever think about moving. It's the perfect house, in my opinion."
    scene ep11_trip59 with dissolve
    isa "You're too sweet. I love it too, but one can still dream of having a place like this."
    scene ep11_trip58 with dissolve
    mc "Are you thinking about getting a holiday cabin?"
    scene ep11_trip57 with dissolve
    isa "I'm not made out of money, [name]. It's just a dream."
    isa "I bet you have those."
    scene ep11_trip58 with dissolve
    mc "Naturally."
scene ep11_trip60 with dissolve
bia "Cocoa time! Don't burn yourselves; it's hot as hell!"
scene ep11_trip61 with dissolve
ji "Here you go. I wasn't sure if you liked marshmallows in yours. But I thought the cup suited you."
scene ep11_trip62 with dissolve
mc "Haha! This is great, thanks."
scene ep11_trip63 with dissolve
bia "How do you like the place, [name]?"
scene ep11_trip64 with dissolve
mc "It's cozy, but it sure gets dark early."
scene ep11_trip65 with dissolve
bia "Haha, yep! You better not wander off far outside. In a couple of hours, it will be pitch black."
bia "But if you do wander off, luckily, the cabin lights up like a beacon."
scene ep11_trip66 with dissolve
mc "Don't worry. I have no plans on heading outside tonight."
scene ep11_trip67 with dissolve
mc "Bella, haha. You have whipped cream on your nose."
isa "Oh?"
scene ep11_trip68 with dissolve
ji "It's going to be fun to ski tomorrow!"
scene ep11_trip69 with dissolve
mc "For you, maybe. I'm horrible at it."
scene ep11_trip70 with dissolve
ji "Maybe you're great at it but don't know it yet?"
scene ep11_trip69 with dissolve
mc "When does that ever happen with anything?"
scene ep11_trip72 with dissolve
isa "You might do well at it. You've got a good balance from martial arts and are in good shape."
scene ep11_trip73 with dissolve
bia "And if you suck, we have a snowmobile you could use instead."
scene ep11_trip68 with dissolve
ji "Haha, don't tell him that. He's going to opt for it."
scene ep11_trip76 with dissolve
mc "I'd love to try the snowmobile!"
scene ep11_trip74 with dissolve
bia "Actually, I think it broke. Or ran out of gas. Or maybe both."
scene ep11_trip75 with dissolve
mc "Haha, nice try. I wanna ride it for sure."
scene ep11_trip68 with dissolve
ji "See what you did? Now, we don't get the pleasure to see [name] fall in the snow skiing."
scene ep11_trip71 with dissolve
mc "Hey, you thought I'd be great at it!"
ji "Hahaha!"
stop music fadeout 3
scene ep11_trip77 with dissolve
$ renpy.pause()
$ renpy.music.stop(channel="sfx2", fadeout=3)

play music "music/ep11/licensed_music/track173.mp3"
scene ep11_trip79 with fade
$ renpy.pause()
if branchJill  and tmp_mod2=="Jill":
    scene ep11_trip78 with dissolve
    $ renpy.pause()
    scene ep11_trip80 with dissolve
    $ renpy.pause()
    scene ep11_trip81 with dissolve
    $ renpy.pause()
    scene ep11_trip82 with dissolve
    ji "Good morning."
    scene ep11_trip83 with dissolve
    mc "No... Is it morning already?"
    scene ep11_trip82 with dissolve
    ji "We said bright and early."
    scene ep11_trip83 with dissolve
    mc "I could use two more hours..."
    scene ep11_trip82 with dissolve
    ji "If you do, those two hours get deducted from snowmobile time."
    scene ep11_trip84 with dissolve
    mc "Ok, I'm up!"
    scene ep11_trip85 with dissolve
    ji "Haha!"
    scene ep11_trip86 with dissolve
    ji "I'm looking forward to today. I've been waiting for this moment with you."
    ji "To be able to turn you around on winter. I feel like I will be able to do that today."
    scene ep11_trip87 with dissolve
    mc "Are you that confident that I will like it?"
    scene ep11_trip86 with dissolve
    ji "I am."
    scene ep11_trip87 with dissolve
    mc "I love seeing you confident."
    scene ep11_trip88 with dissolve
    ji "Let's see if the others are awake."
elif branchIsabella  and tmp_mod2=="Isabella":
    scene ep11_trip90 with dissolve
    $ renpy.pause()
    scene ep11_trip89 with dissolve
    $ renpy.pause()
    scene ep11_trip91 with dissolve
    isa "[name]?"
    scene ep11_trip89 with dissolve
    mc "Mmm... Yeah?"
    scene ep11_trip91 with dissolve
    isa "Wake up."
    scene ep11_trip92 with dissolve
    mc "Woke up a little earlier for me, huh?"
    scene ep11_trip93 with dissolve
    isa "You wish. It's time to head up. I heard Jill and Bianca wake up already."
    scene ep11_trip92 with dissolve
    mc "I feel like it's too early. I'm gonna need some more sleep."
    scene ep11_trip93 with dissolve
    isa "Maybe you can take a nap later in the afternoon. Let's make the most out of this day."
    scene ep11_trip94 with dissolve
    mc "*{i}Yawns{/i}* Yeah, you're right."

if branchJill  and tmp_mod2=="Jill":
    scene ep11_trip95 with dissolve
else:
    scene ep11_trip96 with dissolve
bia "Good morning, guys! Breakfast is served. Help yourselves."
scene ep11_trip97 with dissolve
bia "Did you sleep well?"
scene ep11_trip98 with dissolve
mc "Like a log. I closed my eyes for one second, and suddenly, it was time to get up."
scene ep11_trip99 with dissolve
bia "We were just discussing ski boots. What size shoes are you? 9, 9.5?"
scene ep11_trip98 with dissolve
mc "No. More like 10.5 or 11. It depends on the shoe."
scene ep11_trip100 with dissolve
bia "No way they are that big. Show me."
scene ep11_trip98 with dissolve

if persistent.mod_wtenabled: 
                        $mod_choices = ["(+Jill)","(+Isabella)","(-DIK)","(+DIK)","(For Bianca path)","(-5 Josy)","","","","","","" ]
                        #[mod_gr][mod_choices[0]]
                        #\n{size=-4}[m_c1][mod_choices[1]][m_c2][mod_choices[4]]

menu:
    "Show her \n{size=-4}[m_c1][mod_choices[0]][m_c3][mod_choices[4]]":
        $ RPjill += 1
        $ ep11_bianca_feet = True
        scene ep11_trip101 with dissolve
        mc "Yep, they are. I have a wide foot. It can be hard to find shoes that fit for me."
        scene ep11_trip102 with dissolve
        bia "Whoa, no kidding! Hahaha! They don't look that big from a glance, but they are."
        scene ep11_trip103 with dissolve
    "Don't show her \n{size=-4}[m_c2][mod_choices[1]]":
        $ RPisabella += 1
        mc "They're big, trust me."
        scene ep11_trip99 with dissolve
        bia "Alright."
bia "We have a few pairs here; I'm hoping one of them will be your size. My Dad and uncles keep some boots here for skiing."
bia "If they don't fit, we'll have to head into town."
scene ep11_trip104 with dissolve
mc "Or I'll ride the snowmobile all day. Win-win."
scene ep11_trip105 with dissolve
ji "And here I was, hoping he'd forget about that snowmobile."
scene ep11_trip106 with dissolve
bia "I promise you'll get to ride it. But you're not getting out of skiing."

scene ep11_trip107
show screen ep10_snow_screen
with wipeleft
ji "Did you find ones that fit?"
scene ep11_trip108 with dissolve
mc "They are tight, but yeah, they fit."
scene ep11_trip110 with dissolve
isa "Looking good, [name]. Those sunglasses will at least make you look cool when you fall."
scene ep11_trip111 with dissolve
mc "Well, you gotta crash with style."
scene ep11_trip112 with dissolve
ji "Shall we head for the tracks?"
scene ep11_trip108 with dissolve
mc "The tracks?"
scene ep11_trip113 with dissolve
isa "Ski trails. You wouldn't want to ski through snow without them."
scene ep11_trip109 with dissolve
bia "They loop around these woods with several nice stops along the way."
bia "We'll get to see nature and great views today."
scene ep11_trip112 with dissolve
ji "Are you getting excited?"
scene ep11_trip108 with dissolve
mc "I have zero expectations, but it sounds good."
scene ep11_trip114 with wipeleft
bia "Put your skis on! It's go time."
play sound "sound_effects/season3/skiing.mp3"
scene ep11_trip115 with dissolve
bia "Woho!"
scene ep11_trip116 with dissolve
mc "And off she goes."
scene ep11_trip117 with dissolve
ji "Don't feel stressed. That's what's good about a track. It leads us to the same place."
scene ep11_trip118 with dissolve
isa "And besides, we don't want to crash into each other. It's smart to keep some distance."

if branchJill  and tmp_mod2=="Jill":
    play sound "sound_effects/season3/skiing.mp3"
    scene ep11_trip119 with dissolve
    isa "Have fun, guys. I'll get out of your hair."
    scene ep11_trip120 with dissolve
    ji "You don't have to wait for me. I'll catch up."
    scene ep11_trip121 with dissolve
    mc "Ok, but I don't think there will be much to catch up to. I've never done this before."
    scene ep11_trip122 with dissolve
    ji "Try your best to move forward and we'll take it from there."
    scene ep11_trip123 with dissolve
    $ renpy.pause()
    scene ep11_trip124 with dissolve
    ji "How's your balance?"
    mc "I feel sluggish."
    scene ep11_trip125 with dissolve
    ji "You don't have to move your feet a lot."
    ji "Bend your knees and lean forward. Let your body work together with your arms."
    scene ep11_trip126 with dissolve
    $ renpy.pause()
    scene ep11_trip127 with dissolve
    mc "I think I got it."
    play sound "sound_effects/season3/skiing.mp3"
    scene ep11_trip128 with dissolve
    mc "Whoa!"
    scene ep11_trip129 with dissolve
    ji "Be careful. It's easy to lose your balance."
    scene ep11_trip127 with dissolve
    mc "I can tell. It will take me some time to get used to this."
    scene ep11_trip125 with dissolve
    ji "Take it at your own pace."
    scene ep11_trip130 with dissolve
    mc "They're already so far ahead. I can't even see them anymore."
    ji "Haha, don't worry about them. Focus on having a good time."
    scene ep11_trip131 with dissolve
    $ renpy.pause()
    scene ep11_trip132 with dissolve
    mc "This view is pretty good."
    scene ep11_trip133 with dissolve
    ji "Not too shabby, huh?"
    scene ep11_trip134 with dissolve
    mc "Nope. But I can already feel the burn in my arms."
    scene ep11_trip135 with dissolve
    ji "Try to use your body more. That way, your arms won't get as tired."
    ji "And don't forget to glide. You don't have to rush forward."
    scene ep11_trip136 with dissolve
    mc "Uh oh... There's a slope incoming."
    scene ep11_trip135 with dissolve
    ji "That's great! Just focus on keeping your balance and let the slope carry you forward. Lean into it; don't stand straight."
    scene ep11_trip137 with dissolve
    mc "Whoa!"
    play sound "sound_effects/season3/skiing.mp3"
    scene ep11_trip140 with dissolve
    mc "No! No! No!"
    scene ep11_trip139 with dissolve
    ji "Don't stand straight!"
    scene ep11_trip138 with dissolve
    play sound "sound_effects/season3/snow_fall.mp3"
    mc "AH!!!"
    scene ep11_trip141 with vpunch
    ji "Hahaha! Are you ok?"
    scene ep11_trip142 with dissolve
    mc "I could have hurt myself badly and you're laughing at me."
    scene ep11_trip143 with dissolve
    ji "Are you badly hurt?"
    scene ep11_trip142 with dissolve
    mc "No, I'm fine."
    scene ep11_trip144 with dissolve
    ji "Haha! It looked too funny."
    scene ep11_trip145 with dissolve
    mc "I couldn't keep my balance at all."
    scene ep11_trip146 with dissolve
    ji "The slope was a new thing for you. Try it again and don't go too fast."
    scene ep11_trip147 with dissolve
    ji "We all fall sometimes. Honestly, I'm impressed you lasted this long."
    ji "My first time, I fell on my butt once every minute."
    scene ep11_trip148 with dissolve
    mc "Thanks, that feels better to hear."
    scene ep11_trip147 with dissolve
    ji "Granted, I was five years old at the time, but still."
    scene ep11_trip148 with dissolve
    mc "Ok, enough out of you."
    scene ep11_trip149 with dissolve
    ji "Hahaha! Let's get back at it."
else:
    play sound "sound_effects/season3/skiing.mp3"
    scene ep11_trip150 with dissolve
    ji "I'm going to catch up with Bianca. See you guys later!"
    scene ep11_trip151 with dissolve
    mc "Ok, here we go..."
    scene ep11_trip152 with dissolve
    isa "What level of amateur are you?"
    scene ep11_trip151 with dissolve
    mc "Was that an insult or a question?"
    scene ep11_trip152 with dissolve
    isa "A question, of course."
    isa "Do you know how to move forward?"
    scene ep11_trip153 with dissolve
    mc "I've seen how it's done, but that's about it."
    mc "I guess I use my arms to push myself forward."
    scene ep11_trip154 with dissolve
    isa "You will fatigue if you only use your arms. Bend your knees and activate your core, too."
    scene ep11_trip155 with dissolve
    play sound "sound_effects/season3/skiing.mp3"
    isa "There you go."
    mc "Hey, it's working."
    scene ep11_trip156 with dissolve
    isa "You can also skate by alternating right and left, like when you're running."
    isa "Don't lift your feet, though. Keep the skis glued to the ground and slide forward."
    scene ep11_trip157 with dissolve
    mc "This is tricky. I feel like I'm super slow."
    isa "It's not a race. Enjoy yourself."
    scene ep11_trip158 with dissolve
    $ renpy.pause()
    scene ep11_trip132 with dissolve
    mc "I gotta say, this view is great. Have you done this a lot?"
    scene ep11_trip159 with dissolve
    isa "Not as often as I'd like, but I've been on ski trips before."
    isa "I prefer to ski downhill, but this has its appeal too. It's much more relaxing."
    isa "It's fun and you get free exercise while you're at it."
    scene ep11_trip160 with dissolve
    mc "Uh oh... There's a slope incoming."
    scene ep11_trip161 with dissolve
    isa "Don't skate on the slope. Focus on keeping your balance and rest your arms."
    scene ep11_trip162 with dissolve
    mc "Bella, it's going too fast!"
    scene ep11_trip161 with dissolve
    isa "Don't stand up straight! You will fall!"
    scene ep11_trip163 with dissolve
    play sound "sound_effects/season3/snow_fall.mp3"
    mc "AHHH!!!"
    scene ep11_trip164 with hpunch
    isa "Are you taking a break already?"
    scene ep11_trip142 with dissolve
    mc "I fell on my ass... Ow..."
    scene ep11_trip165 with dissolve
    isa "Don't panic next time. Keep leaning into it and you won't fall like that."
    scene ep11_trip166 with dissolve
    mc "I was going pretty damned fast."
    scene ep11_trip165 with dissolve
    isa "Not really."
    scene ep11_trip167 with dissolve
    isa "Do it again. There's still some slope left to go."

if branchJill  and tmp_mod2=="Jill":
    scene ep11_trip168 with wipeleft
else:
    scene ep11_trip169 with wipeleft
bia "There you are!"
scene ep11_trip170 with dissolve
bia "We were worried we had lost you. We were about to turn back to search."
scene ep11_trip171 with dissolve
mc "This is exhausting. It's way more intense than running."
scene ep11_trip172 with dissolve
isa "You're activating new muscles; it's understandable."
stop music fadeout 3
scene ep11_trip170 with dissolve
bia "At least you made it here. Now, you get to enjoy a break at the perfect spot."
play music "music/ep11/licensed_music/track174.mp3"
$ tmp_list = [False, False, False, False]
label ep11_trip_break_label:
$ renpy.block_rollback()
if False not in tmp_list:
    scene ep11_trip173 with dissolve
    bia "Who wants lunch?"
    scene ep11_trip178 with dissolve
    ji "Me, please."
    scene ep11_trip174 with dissolve
    bia "Let's eat and then work on getting back home."
    bia "It usually takes longer to get back than to get here."
    scene ep11_trip175 with dissolve
    bia "And with some of us going slower, I think we shouldn't wait too long."
    scene ep11_trip176 with dissolve
    stop music fadeout 3
    mc "You can say my name, you know?"
    scene ep11_trip177 with dissolve
    $ renpy.pause()
    jump ep11_freeroam_cabin_intro_label

scene ep11_trip_main with dissolve

if not tmp_list[0]:
    $ ui.imagebutton("ep11_trip_bianca_idle", "ep11_trip_bianca_hover", clicked=ui.returns("bianca"), xpos=0, ypos=0, focus_mask=True)
if not tmp_list[1]:
    $ ui.imagebutton("ep11_trip_mc_idle", "ep11_trip_mc_hover", clicked=ui.returns("mc"), xpos=0, ypos=0, focus_mask=True)
if not tmp_list[2]:
    $ ui.imagebutton("ep11_trip_jill_idle", "ep11_trip_jill_hover", clicked=ui.returns("jill"), xpos=0, ypos=0, focus_mask=True)
if not tmp_list[3]:
    $ ui.imagebutton("ep11_trip_bella_idle", "ep11_trip_bella_hover", clicked=ui.returns("bella"), xpos=0, ypos=0, focus_mask=True)

$ result = ui.interact()
if result == "bianca":
    jump ep11_trip_view_label
elif result == "jill":
    jump ep11_trip_jill_label
elif result == "bella":
    jump ep11_trip_bella_label
elif result == "mc":
    jump ep11_trip_pic_label


label ep11_trip_view_label:
$ renpy.block_rollback()
$ tmp_list[0] = True
scene ep11_trip179 with dissolve
$ renpy.pause()
scene ep11_trip180 with dissolve
mc "This view is incredible."
scene ep11_trip181 with dissolve
bia "It's amazing, isn't it? It's hard to grow tired of it."
scene ep11_trip182 with dissolve
mc "Have you been here a lot?"
scene ep11_trip181 with dissolve
bia "Yeah, many times. My family shares the cabin. Everyone helps out with it."
bia "It has become a tradition to stay here a few times every year."
scene ep11_trip182 with dissolve
mc "It's so beautiful. You're lucky to have this."
scene ep11_trip183 with dissolve
bia "It's a privilege, for sure. I won't forget that."
scene ep11_trip184 with dissolve
$ renpy.pause()
jump ep11_trip_break_label

label ep11_trip_pic_label:
$ renpy.block_rollback()
$ tmp_list[1] = True

scene ep11_trip185 with dissolve
mc "(I should take some pictures while we're here.)"

$ tmpInt = 0
scene ep11_trip186 with dissolve
if not persistent.mod_wtenabled:
    call screen epi_camera_screen([["Full-body shot",840,250,790,430],["Close up shot",1440,100,1420,40],["Pervy shot",1470,400,1450,560]])
else:
    call screen epi_camera_screen([["Full-body shot",840,250,790,430],["Close up shot",1440,100,1420,40],["Pervy shot\n{size=-14}[m_c2](-Jill)",1470,400,1450,560]])
if tmpInt == 1:
    mc "Jill! Over here."
    scene ep11_trip187 with dissolve
    ji "What are you up to?"
    scene ep11_trip188 with dissolve
    mc "I'm taking some pictures to remember this trip."
    scene ep11_trip187 with dissolve
    ji "Good idea! Now I want some pictures too."
    play sound "sound_effects/interlude/camera_shutter.mp3"
    $ mgallery_add_photo("ep11_jill_trip_1a")
    scene ep11_jill_trip_1a with dissolve
    $ renpy.pause()
elif tmpInt == 2:
    mc "Jill! Over here."
    scene ep11_trip187 with dissolve
    ji "What are you up to?"
    scene ep11_trip188 with dissolve
    mc "I'm taking some pictures to remember this trip by."
    scene ep11_trip187 with dissolve
    ji "Good idea! Now I want some pictures too."
    play sound "sound_effects/interlude/camera_shutter.mp3"
    $ mgallery_add_photo("ep11_jill_trip_1b")
    scene ep11_jill_trip_1b with dissolve
    mc "Smile!"
elif tmpInt == 3:
    $ dk(1)
    $ RPjill -= 1
    play sound "sound_effects/interlude/camera_shutter.mp3"
    $ mgallery_add_photo("ep11_jill_trip_1c")
    scene ep11_jill_trip_1c with dissolve
    $ renpy.pause()
    scene ep11_trip189 with dissolve
    ji "What are you taking a picture of?"
    scene ep11_trip190 with dissolve
    mc "Uh... A bit of everything."
    scene ep11_trip191 with dissolve
    ji "Mhm... *{i}Sigh{/i}*"

$ tmpInt = 0
scene ep11_trip192 with dissolve
if persistent.mod_wtenabled:
    call screen epi_camera_screen([["Full-body shot",1040,350,980,520],["Close up shot",1560,110,1520,40],["Pervy shot\n{size=-4}[m_c2](-2 Isabella)",1525,415,1520,580]])
else:
    call screen epi_camera_screen([["Full-body shot",1040,350,980,520],["Close up shot",1560,110,1520,40],["Pervy shot",1525,415,1520,580]])




if tmpInt == 1:
    scene ep11_trip196 with dissolve
    mc "Bella! Strike a pose."
    $ mgallery_add_photo("ep11_bella_trip_1a")
    play sound "sound_effects/interlude/camera_shutter.mp3"
    scene ep11_bella_trip_1a with dissolve
    $ renpy.pause()
    scene ep11_trip197 with dissolve
    isa "Can you send me the pictures you take?"
    scene ep11_trip198 with dissolve
    mc "Sure."
elif tmpInt == 2:
    scene ep11_trip197 with dissolve
    isa "Taking pictures, are you?"
    scene ep11_trip198 with dissolve
    if branchJill:
        mc "I wanted a nice shot of you."
    else:
        mc "I wanted a nice shot of you. You look so cute in that hat."
    play sound "sound_effects/interlude/camera_shutter.mp3"
    $ mgallery_add_photo("ep11_bella_trip_1b")
    scene ep11_bella_trip_1b with dissolve
    $ renpy.pause()
elif tmpInt == 3:
    $ dk(1)
    play sound "sound_effects/interlude/camera_shutter.mp3"
    scene ep11_trip193 with dissolve
    $ renpy.pause()
    scene ep11_trip194 with dissolve
    isa "Taking pictures, are you?"
    scene ep11_trip195 with dissolve
    mc "Yep."

scene ep11_trip197 with dissolve
isa "Want me to take one of you?"
scene ep11_trip198 with dissolve
mc "Yeah! Take a nice one of me when I stand over here."

if tmpInt == 3:
    $ RPisabella -= 2
    scene ep11_trip199 with dissolve
    isa "(Just as I thought. I'm deleting this one.)"
    if mphone_app_gallery_photos_list[0] == "ep11_jill_trip_1c":
        $ RPisabella -= 3
        $ mphone_app_gallery_photos_list.remove("ep11_jill_trip_1c")
        isa "(Of Jill too... *{i}Sigh{/i}*)"

$ tmpInt = 0
scene ep11_trip200 with dissolve
call screen epi_camera_screen([["Full-body shot",740,450,680,620],["Close up shot",130,80,80,250],["Artistic shot",1000,100,1000,40]])
play sound "sound_effects/interlude/camera_shutter.mp3"
if tmpInt == 1:
    $ mgallery_add_photo("ep11_mc_trip_1a")
    scene ep11_mc_trip_1a with dissolve
    $ renpy.pause()
elif tmpInt == 2:
    $ mgallery_add_photo("ep11_mc_trip_1b")
    scene ep11_mc_trip_1b with dissolve
    $ renpy.pause()
elif tmpInt == 3:
    $ mgallery_add_photo("ep11_mc_trip_1c")
    scene ep11_mc_trip_1c with dissolve
    $ renpy.pause()

scene ep11_trip201 with dissolve
isa "All done."

scene ep11_trip202 with dissolve
menu:
    "[m_c1]Take one of Bianca":
        mc "Bianca? Can I get a picture of you?"
        scene ep11_trip203 with dissolve
        bia "Oh! Of course! I want one, too."
        scene ep11_trip204 with dissolve
        call screen epi_camera_screen([["Full-body shot",460,170,410,350],["Close up shot",1120,110,1090,40],["Both of you",1460,500,1420,680]])
        if tmpInt == 1:
            $ mgallery_add_photo("ep11_bianca_trip_1a")
            $ ep11_bianca_pic = 1
            play sound "sound_effects/interlude/camera_shutter.mp3"
            scene ep11_bianca_trip_1a with dissolve
            $ renpy.pause()
            scene ep11_trip205 with dissolve
            bia "Did it come out good? I didn't blink, did I?"
            scene ep11_trip206 with dissolve
            mc "No, you look good."
        elif tmpInt == 2:
            $ mgallery_add_photo("ep11_bianca_trip_1b")
            $ ep11_bianca_pic = 2
            play sound "sound_effects/interlude/camera_shutter.mp3"
            scene ep11_bianca_trip_1b with dissolve
            $ renpy.pause()
            scene ep11_trip205 with dissolve
            bia "Did it come out good? I didn't blink, did I?"
            scene ep11_trip206 with dissolve
            mc "No, you look good."
        elif tmpInt == 3:
            $ ep11_bianca_pic = 3
            scene ep11_trip207 with dissolve
            bia "Oh! Good idea, let's take one together."
            $ mgallery_add_photo("ep11_bianca_trip_1c")
            play sound "sound_effects/interlude/camera_shutter.mp3"
            scene ep11_bianca_trip_1c with dissolve
            $ renpy.pause()
        scene ep11_trip208 with dissolve
        bia "Haha! Here! Let me see it!"
        $ RPjill += 1
        scene ep11_trip209 with dissolve
        bia "Stop hogging it!"
        scene ep11_trip210 with dissolve
        $ renpy.pause()
    "Ignore Bianca":
        $ ep11_bianca_pic = 0

scene ep11_trip211 with dissolve
bia "Hey! How about a group picture?"
scene ep11_trip212 with dissolve
ji "Oh! That will be fun."
scene ep11_trip213 with dissolve
mc "I'll put it on a timer."
scene ep11_trip214 with dissolve
bia "You don't have to do that with those phones. It's enough if everyone screams cheese."
scene ep11_trip213 with dissolve
mc "I didn't know that."
scene ep11_trip215 with dissolve
ji "Everyone ready?"
$ mgallery_add_photo("ep11_group_trip_1a")
scene ep11_group_trip_1a with dissolve
play sound "sound_effects/interlude/camera_shutter.mp3"
"CHEEESE!!!"
scene ep11_trip216 with dissolve
bia "I got snow in my eyes; I think I blinked. Let's take another one!"
scene ep11_trip218 with dissolve
mc "I'm sure it's fine."
scene ep11_trip216 with dissolve
bia "No! It would be a waste if we didn't look good in the picture."
scene ep11_trip217 with dissolve
mc "(Haha! A waste, huh? I'm gonna channel Mom for this one.)"
$ mgallery_add_photo("ep11_group_trip_1b")
scene ep11_group_trip_1b with dissolve
play sound "sound_effects/interlude/camera_shutter.mp3"
"CHEEESE!!!"
scene ep11_trip216 with dissolve
bia "That was better, I think."
scene ep11_trip218 with dissolve
mc "Haha, doubt it."

jump ep11_trip_break_label

label ep11_trip_jill_label:
$ renpy.block_rollback()
$ tmp_list[2] = True
if branchJill  and tmp_mod2=="Jill":
    scene ep11_trip219 with dissolve
    mc "The trip here was worth it."
    scene ep11_trip220 with dissolve
    ji "Enjoying winter yet?"
    scene ep11_trip221 with dissolve
    mc "You know what? I think I'm getting there."
    scene ep11_trip222 with dissolve
    $ renpy.pause()
    scene ep11_trip223 with dissolve
    ji "I'm happy I get to share this with you. It means a lot to me."
    scene ep11_trip224 with dissolve
    $ renpy.pause()
else:
    scene ep11_trip225 with dissolve
    mc "The trip here was definitely worth it."
    scene ep11_trip226 with dissolve
    ji "It sounds like someone is starting to come around on winter."
    scene ep11_trip227 with dissolve
    mc "I think I'm getting there."
    scene ep11_trip228 with dissolve
    ji "Somehow, I knew you'd like it. You just needed to experience something new."
    scene ep11_trip229 with dissolve
    $ renpy.pause()
jump ep11_trip_break_label

label ep11_trip_bella_label:
$ renpy.block_rollback()
$ tmp_list[3] = True
scene ep11_trip230 with dissolve
mc "You know, skiing isn't that bad? I think I've gotten the hang of it."
scene ep11_trip231 with dissolve
isa "Good. Because I talked to Bianca and you'll need some skills for what's up next."
scene ep11_trip230 with dissolve
mc "What's that?"
scene ep11_trip231 with dissolve
isa "You're looking at it."
scene ep11_trip232 with dissolve
isa "To get back to the cabin, we need to go downhill all the way to the bottom. And this hill is the only way down."
mc "ARE YOU KIDDING ME!?"
scene ep11_trip233 with dissolve
mc "Bianca! Is that true? Do I have to ski downhill to get back home?"
scene ep11_trip234 with dissolve
bia "Yep. Sure is."
scene ep11_trip235 with dissolve
mc "I struggle to hold the skis parallel to each other. And I fell multiple times getting here."
mc "I think my ass is getting bruises."
scene ep11_trip233 with dissolve
mc "There's no way I can do that!"
scene ep11_trip236 with dissolve
"*{i}Laughter{/i}*"
scene ep11_trip235 with dissolve
ji "You guys are so mean to him."
scene ep11_trip236 with dissolve
mc "You're joking... Thanks... I thought you were serious."
scene ep11_trip234 with dissolve
bia "You're welcome to go down there if you want, but we'd need to call out for a rescue team if you do."
scene ep11_trip237 with dissolve
mc "Ok... Good one. You got me."
jump ep11_trip_break_label

label ep11_freeroam_cabin_intro_label:
scene ep11_freeroam_cabin1
hide screen ep10_snow_screen
with wipeleft
play music "music/ep_interlude/licensed_music/track109.mp3"
queue music ["music/ep2/winter.mp3","music/ep8/licensed_music/track61.mp3","music/ep_interlude/licensed_music/track109.mp3"]
mc "*{i}Phew{/i}* Finally..."
scene ep11_freeroam_cabin2 with dissolve
isa "I had a great time, but it does feel good to be back inside."
scene ep11_freeroam_cabin4 with dissolve
bia "It's cold in here. Jill, would you mind starting a fire?"
scene ep11_freeroam_cabin3 with dissolve
ji "Not a problem. I'm on it."
scene ep11_freeroam_cabin4 with dissolve
bia "And don't shower yet; I have something planned."
scene ep11_freeroam_cabin2 with dissolve
isa "Then I'll start preparing dinner."
scene ep11_freeroam_cabin4 with dissolve
bia "Excellent. I have to do some preparations outside. I'll be back when I'm done."
jump ep11_freeroam_cabin_label

label ep11_cabin_jill_event_label:
scene ep11_cabin_jill_event1 with dissolve
$ renpy.pause()
scene ep11_cabin_jill_event2 with dissolve
mc "What a day... I'm beat."
if branchJill  and tmp_mod2=="Jill":
    scene ep11_cabin_jill_event5 with dissolve
    ji "You did great today. I'm so proud of you."
    scene ep11_cabin_jill_event2 with dissolve
    mc "You're proud of me? What for?"
    scene ep11_cabin_jill_event5 with dissolve
    ji "You dared to try new things just like that."
    scene ep11_cabin_jill_event6 with dissolve
    ji "It made me very happy. My feelings for you grew when I saw it."
    scene ep11_cabin_jill_event2 with dissolve
    mc "Because I sucked at skiing?"
    scene ep11_cabin_jill_event5 with dissolve
    ji "Because of how you handled yourself when you were outside of your comfort zone."
    scene ep11_cabin_jill_event6 with dissolve
    ji "I found it attractive."
    scene ep11_cabin_jill_event2 with dissolve
    mc "Even when I fell down?"
    scene ep11_cabin_jill_event5 with dissolve
    ji "Haha, you fell a few times, but you got up and at it again."
    scene ep11_cabin_jill_event7 with dissolve
    $ renpy.pause()
    scene ep11_cabin_jill_event8 with dissolve
    mc "Thanks for bringing me here. It's a shame we have to leave tomorrow."
    scene ep11_cabin_jill_event9 with dissolve
    ji "Yeah, the day flew by. But we still have some quality time left tonight."
    if "ep11_cabin_bianca_event_label" in event_list:
        ji "And you still have a snowmobile to ride, don't you?"
        scene ep11_cabin_jill_event8 with dissolve
        mc "Oh, yeah! I gotta ask Bianca about that."
    else:
        scene ep11_cabin_jill_event9 with dissolve
        ji "Was it fun riding the snowmobile?"
        scene ep11_cabin_jill_event8 with dissolve
        mc "So much fun!"
    scene ep11_cabin_jill_event10 with dissolve
    ji "Oh, I just remembered. I forgot to tell you about something."
else:
    scene ep11_cabin_jill_event3 with dissolve
    ji "Did you have fun?"
    scene ep11_cabin_jill_event2 with dissolve
    mc "Lots."
    scene ep11_cabin_jill_event3 with dissolve
    ji "I'm glad."
    scene ep11_cabin_jill_event2 with dissolve
    mc "How about you?"
    scene ep11_cabin_jill_event4 with dissolve
    ji "Yes, I love skiing. And I've missed this place. It brought back some nice memories."
    scene ep11_cabin_jill_event11 with dissolve
    ji "The fire got pretty hot. Haha..."
    scene ep11_cabin_jill_event12 with dissolve
    $ renpy.pause()
    if ep9_b_kissed_jill:
        scene ep11_cabin_jill_event14 with dissolve
        $ renpy.pause()
        scene ep11_cabin_jill_event15 with dissolve
        $ renpy.pause()
    scene ep11_cabin_jill_event13 with dissolve
    mc "So, what's new with you?"

scene ep11_cabin_jill_event16 with dissolve
ji "I got offered to play piano at a party."
scene ep11_cabin_jill_event17 with dissolve
mc "A party?"
scene ep11_cabin_jill_event16 with dissolve
ji "At an annual faculty Christmas party. Staff, sponsors and others will be there."
ji "They usually have some entertainment, and I was asked to play for them."
if ep8_recital_failed:
    scene ep11_cabin_jill_event18 with dissolve
    ji "After what happened at my recital, I felt like it was a question out of pity."
    scene ep11_cabin_jill_event19 with dissolve
    mc "Come on, that can't be why they asked you."
    scene ep11_cabin_jill_event18 with dissolve
    ji "Maybe it wasn't, but it's what I keep thinking. I don't think I will go through with it."
    scene ep11_cabin_jill_event19 with dissolve
    mc "Are you scared you won't be able to do it?"
    scene ep11_cabin_jill_event18 with dissolve
    ji "Yes. What do you think I should do?"
    scene ep11_cabin_jill_event19 with dissolve
    menu:
        "Encourage her":
            mc "I think you should give it another try. It's what you want, and if there's another chance to do it, why not?"
            scene ep11_cabin_jill_event20 with dissolve
            ji "I just don't want to panic again. And I can feel that I will."
            ji "But this time, it will be a smaller audience, and it won't be on a stage - it will be background entertainment."
            ji "I'd sit there playing music while they talk to each other. I barely think they'd stop to listen."
            scene ep11_cabin_jill_event19 with dissolve
            mc "Isn't that perfect? If you're not the center of attention, maybe it won't be as stressful."
            scene ep11_cabin_jill_event18 with dissolve
            ji "Perhaps."
            scene ep11_cabin_jill_event19 with dissolve
            mc "And if it's background entertainment only, you could walk away whenever."
            scene ep11_cabin_jill_event20 with dissolve
            ji "It's still scary. But I know I have to push myself... I want to."
            scene ep11_cabin_jill_event21 with dissolve
            ji "The recital was so scary for me. My entire body and mind screamed no."
            ji "I've regretted it a lot. If I had another shot at it, I would have forced myself to play."
            scene ep11_cabin_jill_event22 with dissolve
            mc "Then do it now. It's your chance."
            scene ep11_cabin_jill_event20 with dissolve
            ji "We'll see."
            scene ep11_cabin_jill_event19 with dissolve
            mc "You're a great pianist, regardless of whether you perform or not."
        "Listen to your gut":
            mc "I think you should listen to your gut. What does it tell you?"
            scene ep11_cabin_jill_event20 with dissolve
            ji "It tells me the same thing that it did at the recital. My body and mind scream no."
            ji "But I've regretted it a lot. That I never went up on stage to perform."
            ji "I know I was ready to do it, but I didn't get to show everyone that I could do it."
            scene ep11_cabin_jill_event18 with dissolve
            ji "Right now, I feel torn. I don't want to fail again because that would feel like a nail in the coffin."
            ji "But I want to try it again."
            scene ep11_cabin_jill_event19 with dissolve
            mc "Only you can decide if you want to do it or not."
            mc "Don't feel forced to prove a point. You're a great pianist, regardless of whether you perform or not."
    scene ep11_cabin_jill_event23 with dissolve
    $ renpy.pause()
else:
    scene ep11_cabin_jill_event17 with dissolve
    mc "That's great news! Are you doing it?"
    scene ep11_cabin_jill_event24 with dissolve
    ji "Yes, I am. I want to feel that high again."
    ji "It's still scary, but I know I can do it, thanks to you."
    scene ep11_cabin_jill_event25 with dissolve
    mc "I just gave you the encouragement you needed. You did all the work."
    scene ep11_cabin_jill_event26 with dissolve
    ji "No. You did more than that."
    ji "And I'll never forget it."
    scene ep11_cabin_jill_event27 with dissolve
    $ renpy.pause()
    if branchJill or ep9_b_kissed_jill:
        scene ep11_cabin_jill_event28 with dissolve
    else:
        scene ep11_cabin_jill_event29 with dissolve
    ji "..."

$ task_list[1] = ""
$ new_bio("Jill", "Jill got asked to perform at the faculty's Christmas party.")
if task_list[0] == "" and task_list[1] == "" and task_list[2] == "":
    $ task_list[3] = "Go to the fireplace"
    $ event_list.append("ep11_cabin_sauna_event_label")
$ updateTaskList()
jump endEvent

label ep11_cabin_bianca_event_label:
scene ep11_bianca_event1 with dissolve
bia "Almost..."
scene ep11_bianca_event2 with dissolve
bia "Hngn... Come on... Come on..."
mc "Taking a selfie?"
scene ep11_bianca_event3 with dissolve
bia "Haha, no! I'm trying to get a bar, but today is a bad day."
bia "Screw it. My phone will have to wait until tomorrow."
scene ep11_bianca_event4 with dissolve
mc "Is it important?"
scene ep11_bianca_event5 with dissolve
bia "Not really. I wanna check if I got any messages or missed calls."
scene ep11_bianca_event6 with dissolve
bia "Whoa!!!"
play sound "sound_effects/season3/snow_trip.mp3"
scene ep11_bianca_event7 with hpunch
bia "Wow! Quick thinking."
scene ep11_bianca_event8 with dissolve
mc "All good?"
scene ep11_bianca_event7 with dissolve
bia "Yeah, thanks!"
scene ep11_bianca_event9 with dissolve
bia "Oh! [name]! I almost forgot. Follow me."
$ renpy.sound.play("sound_effects/season3/snowmobile2.mp3", channel="sfx1", loop=True)
scene ep11_bianca_event10 with dissolve
bia "Cool, huh!?"
mc "Wow! So cool."
scene ep11_bianca_event11 with dissolve
bia "Wanna take it for a spin before it gets too dark?"
mc "Will you let me borrow it? I never rode one before."
bia "Sure! But I'm coming with you. I can't risk you getting lost."
bia "I know these woods well. You'll need a guide."
scene ep11_bianca_event12 with dissolve
bia "Hop on behind me and I'll show you."
mc "Sure. Sounds fun."
scene ep11_bianca_event13 with dissolve
bia "Don't tell Dad we did this."
mc "Why? Is he protective of it?"
scene ep11_bianca_event14 with dissolve
bia "No, but this one isn't made for two persons. But we can still do it if you're careful."
mc "Ok, where should I put my arms?"
scene ep11_bianca_event15 with dissolve
bia "You have to wrap them around me, or you'll fall off."
bia "And don't be shy; grip tightly. This thing goes WRRRROOOOM!"
mc "It does?"
scene ep11_bianca_event16 with dissolve
$ renpy.sound.play("sound_effects/season3/snowmobile3.mp3", channel="sfx3", loop=False)
"WRRRRRRRRROOOOOOMMM!!!"
bia "WOHO!!!"
$ renpy.sound.play("sound_effects/season3/snowmobile1.mp3", channel="sfx2", loop=False)
scene ep11_bianca_event17 with dissolve
$ renpy.pause()
scene ep11_bianca_event18 with dissolve
mc "I thought you said we had to drive carefully!"
scene ep11_bianca_event19 with dissolve
bia "Haha! I said you had to drive it carefully. I know what I'm doing."
scene ep11_bianca_event20 with dissolve
mc "I didn't think it would be this fast!"
bia "Oh, it goes even faster! But I saw how you fell in the snow earlier today; I don't want to overdo it."
mc "How thoughtful..."
scene ep11_bianca_event21 with dissolve
$ renpy.pause()
$ renpy.music.stop(channel="sfx3", fadeout=3)
$ renpy.music.stop(channel="sfx2", fadeout=3)
$ renpy.music.stop(channel="sfx1", fadeout=3)
scene ep11_bianca_event22 with dissolve
bia "Haha, are you doing ok?"
scene ep11_bianca_event23 with dissolve
mc "Yeah! That was fun as hell!"
scene ep11_bianca_event24 with dissolve
mc "I bet you ride this all the time."
scene ep11_bianca_event25 with dissolve
bia "Oh, yeah! You know it."
scene ep11_bianca_event26 with dissolve
bia "I always have a blast when I'm here. There are so many things to do that you can't back home."
scene ep11_bianca_event27 with dissolve
mc "Then, I take it you're here often."
scene ep11_bianca_event28 with dissolve
bia "Not as often as I'd like. And, of course, the weather isn't always this good."
if ep9_told_jill:
    scene ep11_bianca_event29 with dissolve
    bia "Matty and I used to come here, just the two of us."
    scene ep11_bianca_event27 with dissolve
    mc "Sounds romantic."
    scene ep11_bianca_event29 with dissolve
    bia "Yeah, it was. That fucking lunkhead made a big mistake."
    scene ep11_bianca_event30 with dissolve
    bia "Being here alone with someone is great."
else:
    bia "Matty and I have been here for a few years, just the two of us."
    scene ep11_bianca_event27 with dissolve
    mc "Sounds romantic."
    scene ep11_bianca_event30 with dissolve
    bia "Haha, very. Being here alone with someone is great."
bia "I mean, there aren't many other places where you can walk around nude and bathe naked in the sauna and hot tub without prying eyes."
scene ep11_bianca_event32 with dissolve
mc "Haha, you do that?"
scene ep11_bianca_event30 with dissolve
bia "All the time, haha! And other things, too."
bia "But that would be oversharing."
scene ep11_bianca_event32 with dissolve
mc "It already is. Now I know you had sex in the sauna."
scene ep11_bianca_event31 with dissolve
bia "And the hot tub."
scene ep11_bianca_event32 with dissolve
mc "Yikes."
mc "Not on this snowmobile, I hope."
$ guideSuggestedPage = 178
scene ep11_bianca_event33 with dissolve
bia "Haha! No, not on this snowmobile. Although, I bet you could. The seat is perfect for it."
scene ep11_bianca_event34 with dissolve
bia "Yeah, you'd probably go like this. Haha!"
scene ep11_bianca_event35 with dissolve

if persistent.mod_wtenabled: 
                        $mod_choices = ["(For Bianca path)","(+Cheater)","(-DIK)","(+DIK)","(+5 Josy)","(-5 Josy)","","","","","","" ]
                        #[mod_gr][mod_choices[0]]
                        #\n{size=-4}[m_c1][mod_choices[1]][m_c2][mod_choices[4]]

menu:
    "Stop her":
        scene ep11_bianca_event45 with dissolve
        mc "Yeah. It sounds like that's the way to do it."
        mc "Ok, it's my turn to drive!"
        $ renpy.sound.play("sound_effects/season3/snowmobile2.mp3", channel="sfx1", loop=True)
        scene ep11_bianca_event41 with dissolve
        bia "Hell yeah! You saw how I did it, right?"
    "Play along \n{size=-4}[m_c1][mod_choices[0]][m_c2][mod_choices[1]]":
        $ tc += 1
        $ ep11_bianca_flirt = True
        scene ep11_bianca_event36 with dissolve
        mc "Yeah, I can see this working for sure."
        scene ep11_bianca_event38 with dissolve
        $ renpy.pause()
        scene ep11_bianca_event37 with dissolve
        bia "Haha! Yep, that's how you'd do it."
        scene ep11_bianca_event40 with dissolve
        bia "We should be heading back."
        scene ep11_bianca_event39 with dissolve
        mc "My turn to drive, yeah?"
        scene ep11_bianca_event40 with dissolve
        bia "Yep."
        $ renpy.sound.play("sound_effects/season3/snowmobile2.mp3", channel="sfx1", loop=True)
        scene ep11_bianca_event41 with dissolve
        bia "You saw how I did it, right?"
mc "Yeah, I think so."
mc "Ok... Here we go!"
scene ep11_bianca_event42 with dissolve
$ renpy.pause()
scene ep11_bianca_event43 with dissolve
bia "You can use the throttle more than that."
mc "I'm a slow starter."
scene ep11_bianca_event44 with dissolve
$ renpy.sound.play("sound_effects/season3/snowmobile1.mp3", channel="sfx2", loop=False)
bia "Haha, I'll say."

$ renpy.music.stop(channel="sfx3", fadeout=3)
$ renpy.music.stop(channel="sfx2", fadeout=3)
$ renpy.music.stop(channel="sfx1", fadeout=3)
scene ep11_bianca_event46 with dissolve
mc "Thanks for the ride! It was awesome."
scene ep11_bianca_event47 with dissolve
bia "My pleasure! I'm just happy I got to take it out for a spin."
scene ep11_bianca_event48 with dissolve
bia "Oh! A bar!"
bia "No, wait! Almost!"

$ task_list[2] = ""
if task_list[0] == "" and task_list[1] == "" and task_list[2] == "":
    $ task_list[3] = "Go to the fireplace"
    $ event_list.append("ep11_cabin_sauna_event_label")
$ updateTaskList()

if ep11_bianca_flirt:
    $ new_bio("Bianca", "Bianca and I rode a snowmobile together. The mood got flirty.")
else:
    $ new_bio("Bianca", "Bianca and I rode a snowmobile together. The mood got flirty, but I did my best to stop it from escalating.")
jump endEvent

label ep11_cabin_bella_event_label:
scene ep11_cabin_bella_event1 with dissolve
mc "Do you need my help?"
scene ep11_cabin_bella_event2 with dissolve
isa "No, thanks. Dinner will be quick work. I was asked to keep it simple, and I did."
isa "Wine?"
scene ep11_cabin_bella_event3 with dissolve
mc "Sure."
scene ep11_cabin_bella_event4 with dissolve
isa "I can't believe it's almost Christmas. December has felt like a blur."
scene ep11_cabin_bella_event5 with dissolve
mc "Yeah. This entire semester went by fast."
mc "And come spring, you're not my English teacher anymore."
scene ep11_cabin_bella_event4 with dissolve
isa "But I'll be your teacher in Introduction to College Research."
scene ep11_cabin_bella_event5 with dissolve
mc "Is it a hard class?"
scene ep11_cabin_bella_event6 with dissolve
isa "It depends on who you ask. Many students find it dull and uninspiring."
scene ep11_cabin_bella_event7 with dissolve
mc "Way to hype me up for it."
scene ep11_cabin_bella_event6 with dissolve
isa "But it's essential for the work you'll do later in college. I wouldn't knock it."
scene ep11_cabin_bella_event8 with dissolve
mc "Do you get any winter break, or is it just us?"
scene ep11_cabin_bella_event9 with dissolve
isa "I'll get some days off, yes. But I have other duties to carry out between semesters."
isa "What will you be doing on your break?"
scene ep11_cabin_bella_event8 with dissolve
if branchIsabella  and tmp_mod2=="Isabella":
    mc "Hopefully, I'll be spending lots of time with you."
    scene ep11_cabin_bella_event9 with dissolve
    isa "Aren't you going back home?"
    scene ep11_cabin_bella_event8 with dissolve
    mc "I'll go back home for a few days, but I think I'll return to my frat before the next semester starts."
    scene ep11_cabin_bella_event10 with dissolve
    isa "I see. Yes, I'm available."
else:
    mc "I haven't thought that far ahead yet. Since I have nothing to study - unless I wanna cram some chemistry - I'll likely have some time off."
    mc "I'll go back home for a few days, but I think I'll be back in the frat before next semester starts."
    scene ep11_cabin_bella_event10 with dissolve
isa "I look forward to our Christmas party."
scene ep11_cabin_bella_event11 with dissolve
mc "Me too! That was a great idea."
scene ep11_cabin_bella_event14 with dissolve
isa "Thank Sage for sparking it. I hope she's doing fine."
scene ep11_cabin_bella_event12 with dissolve
mc "Yeah... It's tough for her, I can tell."
scene ep11_cabin_bella_event10 with dissolve
isa "Is there something you'd like for Christmas?"
scene ep11_cabin_bella_event11 with dissolve
mc "Me? Why? Are you getting me something?"
scene ep11_cabin_bella_event10 with dissolve
isa "I was just curious."
scene ep11_cabin_bella_event11 with dissolve
mc "Well, if that's the case..."
if branchIsabella and tmp_mod2=="Isabella":
    scene ep11_cabin_bella_event18 with dissolve
    mc "All I want for Christmas is..."
    mc "...a snowmobile."
    scene ep11_cabin_bella_event15 with dissolve
    isa "Haha, shut it."
    scene ep11_cabin_bella_event16 with dissolve
    mc "And make it a fast one!"
    scene ep11_cabin_bella_event15 with dissolve
    isa "I'm not getting you a snowmobile. Lower your expectations."
    scene ep11_cabin_bella_event16 with dissolve
    mc "Haha, ok. Then no. I don't need anything for Christmas."
    mc "I'm happy I get to celebrate it twice this year!"
else:
    mc "I wouldn't mind a bump in my grades."
    scene ep11_cabin_bella_event13 with dissolve
    isa "Do you realize by asking me that you're doing something unethical?"
    if ep8_midterms_cheated == "DIK":
        isa "And given what we talked about with the midterm tests..."
    scene ep11_cabin_bella_event11 with dissolve
    mc "It was just a joke."
    mc "I don't need anything for Christmas."
    mc "I'm happy I get to celebrate it twice this year!"
scene ep11_cabin_bella_event17 with dissolve
$ renpy.pause()

$ task_list[0] = ""
if task_list[0] == "" and task_list[1] == "" and task_list[2] == "":
    $ task_list[3] = "Go to the fireplace"
    $ event_list.append("ep11_cabin_sauna_event_label")
$ updateTaskList()
jump endEvent

label ep11_cabin_sauna_event_label:
play sound "sound_effects/season3/champagne_pop.mp3"
$ renpy.sound.play("sound_effects/table_slam.mp3", channel="sfx3", loop=False)
$ renpy.sound.play("sound_effects/season3/fireplace.mp3", channel="sfx2", loop=True)
scene ep11_cabin_sauna_event1 with vpunch
bia "Guys! It's time!"
scene ep11_cabin_sauna_event2 with dissolve
ji "To party?"
play sound "sound_effects/bottle_pour.mp3"
scene ep11_cabin_sauna_event3 with dissolve
bia "Hell yes! Drinks are on me."
scene ep11_cabin_sauna_event4 with dissolve
isa "Champagne? You shouldn't have. I opened a bottle of white wine in the kitchen."
scene ep11_cabin_sauna_event5 with dissolve
bia "We'll get to that bottle too."
play sound "sound_effects/bottle_clink.mp3"
scene ep11_cabin_sauna_event6 with dissolve
bia "Cheers to an amazing trip with a buttload of snow fun! I'm so happy you guys came to share this weekend with me."
scene ep11_cabin_sauna_event7 with dissolve
isa "I think I speak for everyone when I say the pleasure was ours."
scene ep11_cabin_sauna_event8 with dissolve
"Cheers!"
scene ep11_cabin_sauna_event9 with dissolve
isa "It's so good."
scene ep11_cabin_sauna_event10 with dissolve
ji "This Champagne goes straight to your head. My face feels warm already, haha."
scene ep11_cabin_sauna_event11 with dissolve
bia "I hope you guys are ready. Do you know what time it is?"
scene ep11_cabin_sauna_event12 with dissolve
mc "Didn't you say it was party time?"
scene ep11_cabin_sauna_event13 with dissolve
bia "Haha! Yes! But also..."
bia "It's sauna time! And [name] promised he would jump naked into the snow."
scene ep11_cabin_sauna_event14 with dissolve
isa "Now that I'd like to see."
scene ep11_cabin_sauna_event12 with dissolve
mc "I did not promise that."
scene ep11_cabin_sauna_event15 with dissolve
ji "Hahaha! It does sound like something you would promise."
scene ep11_cabin_sauna_event12 with dissolve
mc "No way! Naked in the snow? I'd turn into a popsicle."
scene ep11_cabin_sauna_event14 with dissolve
isa "Let's start with the sauna and see if he dares."
scene ep11_cabin_sauna_event13 with dissolve
bia "It's heating up as we speak, and I don't want to be the only one in there. So, you guys better get changed."
$ renpy.music.stop(channel="sfx2", fadeout=3)
if branchJill  and tmp_mod2=="Jill":
    scene ep11_cabin_sauna_event16 with dissolve
    ji "Haha! This will be so much fun."
    scene ep11_cabin_sauna_event17 with dissolve
    mc "You're not gonna jump into the snow, right?"
    scene ep11_cabin_sauna_event18 with dissolve
    ji "I've done it before."
    scene ep11_cabin_sauna_event19 with dissolve
    mc "No way... Is that a thing?"
    scene ep11_cabin_sauna_event20 with dissolve
    ji "It sounds crazy, I know."
    scene ep11_cabin_sauna_event22 with dissolve
    mc "So, you're gonna do it?"
    scene ep11_cabin_sauna_event21 with dissolve
    ji "I might."
    scene ep11_cabin_sauna_event22 with dissolve
    mc "Naked!?"
    scene ep11_cabin_sauna_event21 with dissolve
    ji "Haha! No, that's just you."
    scene ep11_cabin_sauna_event22 with dissolve
    mc "Jill, I'm not doing it. And also..."
    scene ep11_cabin_sauna_event23 with dissolve
    mc "I love seeing you naked, and that swimsuit looks ridiculously hot on you. I needed to get that out of my system."
    scene ep11_cabin_sauna_event24 with dissolve
    ji "Have some more Champagne, will you?"
    stop music fadeout 3
    scene ep11_cabin_sauna_event25 with dissolve
    ji "*{i}Smack{/i}*"
else:
    scene ep11_cabin_sauna_event26 with dissolve
    mc "Bella, I'm not jumping into the snow."
    scene ep11_cabin_sauna_event27 with dissolve
    isa "Fine. Then, I'll have to push you."
    scene ep11_cabin_sauna_event26 with dissolve
    mc "Ha-ha."
    scene ep11_cabin_sauna_event28 with dissolve
    isa "Or make you ski again. That seems to have you lying face down in the snow in minutes."
    scene ep11_cabin_sauna_event29 with dissolve
    mc "Ok, you got me there. But I'm not gonna do it."
    scene ep11_cabin_sauna_event30 with dissolve
    isa "We'll see. It wouldn't be the first time you're naked in public."
    scene ep11_cabin_sauna_event29 with dissolve
    mc "You got too much ammunition to use against me..."
    scene ep11_cabin_sauna_event31 with dissolve
    isa "You only have yourself to blame for that."
    stop music fadeout 3
    scene ep11_cabin_sauna_event32 with dissolve
    isa "*{i}Smack{/i}*"

play music "music/ep9/licensed_music/track123.mp3"
queue music ["music/ep11/licensed_music/track164.mp3","music/ep10/licensed_music/track136.mp3","music/ep11/licensed_music/track163.mp3","music/ep10/licensed_music/track137.mp3"]
scene ep11_cabin_sauna_event33
show screen ep10_snow_screen
with wipeleft
ji "It's freezing! Hurry!"
scene ep11_cabin_sauna_event34 with dissolve
mc "You girls are crazy!"
scene ep11_cabin_sauna_event35 with dissolve
bia "Haha! You'll be warm in no time once we get into the sauna!"
scene ep11_cabin_sauna_event36
hide screen ep10_snow_screen
show screen sauna_screen
with dissolve
bia "Ahhh!!! Now, that's what I'm talking about."
scene ep11_cabin_sauna_event37 with dissolve
isa "Much, much better."
scene ep11_cabin_sauna_event38 with dissolve
mc "No!!!"
scene ep11_cabin_sauna_event39 with dissolve
ji "What's wrong?"
scene ep11_cabin_sauna_event40 with dissolve
mc "I left my glass inside. I don't want to run back out there."
scene ep11_cabin_sauna_event41 with dissolve
isa "Just drink out of the bottle."
scene ep11_cabin_sauna_event40 with dissolve
mc "I can't do that, can I?"
scene ep11_cabin_sauna_event42 with dissolve
bia "Sure, you can!"
scene ep11_cabin_sauna_event43 with dissolve
bia "Have a seat, everyone!"
scene ep11_cabin_sauna_event44 with dissolve
mc "Considering what you said earlier, where do I dare to sit?"
scene ep11_cabin_sauna_event45 with dissolve
bia "Haha! SHHH!!!"
bia "You can sit anywhere; I was only joking around."
scene ep11_cabin_sauna_event48 with dissolve
ji "It must have been an embarrassing joke. You seem flustered."
scene ep11_cabin_sauna_event47 with dissolve
bia "I joked with [name] that Matty and I did things in the sauna."
scene ep11_cabin_sauna_event49 with dissolve
isa "Ah, yes. \"Joked\"."
isa "Now I wonder where it's safe to sit, too."
scene ep11_cabin_sauna_event46 with dissolve
bia "It's safe to sit wherever you want. I promise!"
scene ep11_cabin_sauna_event50 with dissolve
bia "But if you're gonna obsess about it, you should avoid sitting where I'm sitting."
scene ep11_cabin_sauna_event51 with dissolve
ji "I knew it... Bianca..."
scene ep11_cabin_sauna_event52 with dissolve
bia "What? Like you guys never did it in weird places. I bet you did."
scene ep11_cabin_sauna_event51 with dissolve
ji "I'm not answering that."
if branchJill and tmp_mod2=="Jill":
    scene ep11_cabin_sauna_event53 with dissolve
    bia "...because we'd know where you've done it with [name]?"
    scene ep11_cabin_sauna_event54 with dissolve
    ji "I'm not engaging."
else:
    scene ep11_cabin_sauna_event52 with dissolve
    bia "I already know your answer. I'm talking about these two."
    scene ep11_cabin_sauna_event55 with dissolve
    isa "You're not asking about me and [name], are you?"
    scene ep11_cabin_sauna_event56 with dissolve
    bia "No, I meant either or."

scene ep11_cabin_sauna_event57 with dissolve
bia "[name]? Where was it?"
scene ep11_cabin_sauna_event58 with dissolve
menu:
    "I'm not answering that":
        mc "Yeah, I'm not answering that."
        if branchJill:
            scene ep11_cabin_sauna_event59 with dissolve
            ji "I don't mind."
            scene ep11_cabin_sauna_event60 with dissolve
            mc "No, but I'm keeping that to myself."
        else:
            scene ep11_cabin_sauna_event61 with dissolve
            isa "Chicken."
            scene ep11_cabin_sauna_event62 with dissolve
            mc "Tsk."
    "In a treehouse":
        mc "In a treehouse in some stranger's garden."
        if branchJill:
            scene ep11_cabin_sauna_event59 with dissolve
            ji "*{i}Sigh{/i}* You would engage."
            scene ep11_cabin_sauna_event60 with dissolve
            mc "I didn't want Bianca to feel like she was the only one sharing."
        else:
            scene ep11_cabin_sauna_event63 with dissolve
            isa "That is a weird place. It beats the sauna."
        scene ep11_cabin_sauna_event57 with dissolve
        bia "A treehouse? Nice. I bet that was quite the experience."
        scene ep11_cabin_sauna_event58 with dissolve
        mc "You could say that."

scene ep11_cabin_sauna_event56 with dissolve
bia "What about you?"
scene ep11_cabin_sauna_event64 with dissolve
isa "In a library."
scene ep11_cabin_sauna_event56 with dissolve
bia "Wow! A public library?"
scene ep11_cabin_sauna_event65 with dissolve
ji "Which library?"
scene ep11_cabin_sauna_event64 with dissolve
isa "Not on B&R. This was back in college."
scene ep11_cabin_sauna_event56 with dissolve
bia "I knew I wasn't the only one with these kinds of stories."
scene ep11_cabin_sauna_event66 with dissolve
label ep11_sauna_loop_label:
menu:
    "Relax for a while":
        scene ep11_cabin_sauna_event67 with dissolve
        $ renpy.pause()
        scene ep11_cabin_sauna_event68 with dissolve
        $ renpy.pause()
        scene ep11_cabin_sauna_event69 with dissolve
        $ renpy.pause()
        jump ep11_sauna_loop_label
    "Check Jill out":
        scene ep11_cabin_sauna_event70 with dissolve
        $ renpy.pause()
        scene ep11_cabin_sauna_event71 with dissolve
        $ renpy.pause()
        scene ep11_cabin_sauna_event72 with dissolve
        $ renpy.pause()
        scene ep11_cabin_sauna_event73 with dissolve
        $ renpy.pause()
        jump ep11_sauna_loop_label
    "Check Bella out":
        scene ep11_cabin_sauna_event75 with dissolve
        $ renpy.pause()
        scene ep11_cabin_sauna_event74 with dissolve
        $ renpy.pause()
        scene ep11_cabin_sauna_event76 with dissolve
        $ renpy.pause()
        scene ep11_cabin_sauna_event77 with dissolve
        $ renpy.pause()
        jump ep11_sauna_loop_label
    "Check Bianca out":
        scene ep11_cabin_sauna_event78 with dissolve
        $ renpy.pause()
        scene ep11_cabin_sauna_event79 with dissolve
        $ renpy.pause()
        scene ep11_cabin_sauna_event80 with dissolve
        $ renpy.pause()
        scene ep11_cabin_sauna_event81 with dissolve
        $ renpy.pause()
        jump ep11_sauna_loop_label
    "Leave the sauna":
        scene ep11_cabin_sauna_event82 with dissolve
        ji "Alcohol and sauna were a bad idea..."
scene ep11_cabin_sauna_event83 with dissolve
isa "Haha, it does get to your head a lot faster."
scene ep11_cabin_sauna_event84 with dissolve
bia "Are you guys feeling dizzy too?"
scene ep11_cabin_sauna_event85 with dissolve
mc "Yeah, I shouldn't feel drunk already, but I do."
scene ep11_cabin_sauna_event84 with dissolve
bia "We can move it to the hot tub. But before we do, we gotta settle the score."
bia "Who's bathing in the snow, and who's never getting invited here again?"
scene ep11_cabin_sauna_event86 with dissolve
isa "I knew there was a catch to this weekend. It seemed too good to be true."
scene ep11_cabin_sauna_event87 with dissolve
ji "You guys don't have to do it unless you want to try it."
scene ep11_cabin_sauna_event89 with dissolve
bia "Well, [name] promised he'd do it naked-"
scene ep11_cabin_sauna_event85 with dissolve
mc "I did not promise that."
scene ep11_cabin_sauna_event88 with dissolve
ji "Haha, maybe it was you who promised that?"
scene ep11_cabin_sauna_event90 with dissolve
bia "Hey, I'm no prude."
scene ep11_cabin_sauna_event91 with dissolve
ji "No way!"
scene ep11_cabin_sauna_event92 with dissolve
$ renpy.pause()
scene ep11_cabin_sauna_event93 with dissolve
isa "Party time, was it?"
scene ep11_cabin_sauna_event94 with dissolve
bia "Someone has to get it started, no?"
scene ep11_cabin_sauna_event95 with dissolve
bia "Come on, guys! The hot tub is calling our names."
scene ep11_cabin_sauna_event96
hide screen sauna_screen
show screen ep10_snow_screen
with dissolve
bia "Snow! Here we come!"
play sound "sound_effects/season3/snowball2.mp3"
scene ep11_cabin_sauna_event97 with vpunch
bia "Hahaha!"
scene ep11_cabin_sauna_event98 with dissolve
mc "Wow, you did it!"
scene ep11_cabin_sauna_event99 with dissolve
bia "Oh my God! It's freezing cold!"
scene ep11_cabin_sauna_event100 with dissolve
ji "Did you just realize that?"
play sound "sound_effects/water_splash.mp3"
scene ep11_cabin_sauna_event101 with vpunch
bia "Brrr!!! Ahhh! Hahaha!"
scene ep11_cabin_sauna_event102 with dissolve
ji "Feeling better?"
scene ep11_cabin_sauna_event103 with dissolve
bia "Much! But don't tell me I did that for nothing!"
scene ep11_cabin_sauna_event104 with dissolve
$ renpy.pause()
scene ep11_cabin_sauna_event105 with dissolve
ji "Bella?"
scene ep11_cabin_sauna_event106 with dissolve
isa "This is a once-in-a-lifetime experience, Jill. Let's live a little."
scene ep11_cabin_sauna_event107 with dissolve
ji "But naked?"
scene ep11_cabin_sauna_event108 with dissolve
isa "Yes. Butt naked. It's just us here, and I don't think it's fair to Bianca to let her do it alone."
scene ep11_cabin_sauna_event109 with dissolve
bia "Haha! Yes! That's what I'm talking about! Woho!"
play sound "sound_effects/season3/snowball2.mp3"
scene ep11_cabin_sauna_event110 with vpunch
isa "Ahhh!!!"
scene ep11_cabin_sauna_event111 with dissolve
ji "Haha! What was that!? Are you regretting your experience?"
play sound "sound_effects/water_splash.mp3"
scene ep11_cabin_sauna_event112 with vpunch
isa "Brrrrr!!! Now, I'm not."
scene ep11_cabin_sauna_event113 with dissolve
bia "It's the best, isn't it?"
scene ep11_cabin_sauna_event114 with dissolve
isa "I wouldn't call it that, but it's better than I thought."
scene ep11_cabin_sauna_event115 with dissolve
mc "At this point, we have to."
scene ep11_cabin_sauna_event117 with dissolve
"*{i}Chanting{/i}* Jill! Jill! Jill!"
scene ep11_cabin_sauna_event116 with dissolve
ji "Are you doing it?"
scene ep11_cabin_sauna_event115 with dissolve
mc "Ladies first."
scene ep11_cabin_sauna_event118 with dissolve
isa "Come on, Jill! Everyone's waiting."
scene ep11_cabin_sauna_event119 with dissolve
ji "Screw you, guys!"
scene ep11_cabin_sauna_event120 with dissolve
bia "Yes! WOHO! GO JILL!"
scene ep11_cabin_sauna_event121 with dissolve
ji "Ok... Here goes!"
play sound "sound_effects/season3/snowball2.mp3"
scene ep11_cabin_sauna_event122 with vpunch
ji "Ahhh!!!"
"Hahaha!"
scene ep11_cabin_sauna_event123 with dissolve
ji "It's SO cold!!!"
scene ep11_cabin_sauna_event124 with dissolve
bia "Did {b}you{/b} just realize that?"
scene ep11_cabin_sauna_event125 with dissolve
isa "You did it!"
scene ep11_cabin_sauna_event126 with dissolve
ji "Never tell me I won't do things like this again. Haha!"
scene ep11_cabin_sauna_event127 with dissolve
bia "I have never been more proud of you."
scene ep11_cabin_sauna_event128 with dissolve
bia "Now, only one spring chicken remains."
scene ep11_cabin_sauna_event130 with dissolve
mc "Is it that cold? Because I'm already freezing here."
scene ep11_cabin_sauna_event129 with dissolve
isa "Buck up, buckle down, and find out."
scene ep11_cabin_sauna_event131 with dissolve
isa "Wooo!"
scene ep11_cabin_sauna_event132 with dissolve
$ renpy.pause()
scene ep11_cabin_sauna_event133 with dissolve
$ renpy.pause()
if branchIsabella:
    scene ep11_cabin_sauna_event136 with dissolve
    $ renpy.pause()
    scene ep11_cabin_sauna_event137 with dissolve
    isa "Well... Yeah."
if branchJill:
    scene ep11_cabin_sauna_event134 with dissolve
    $ renpy.pause()
    scene ep11_cabin_sauna_event135 with dissolve
    ji "I know what you are about to say, and you better close that pie hole."
play sound "sound_effects/season3/snowball2.mp3"
scene ep11_cabin_sauna_event138 with vpunch
mc "Holy shit! It's so cold!"
scene ep11_cabin_sauna_event139 with dissolve
bia "You couldn't tell, haha."
scene ep11_cabin_sauna_event140 with dissolve
mc "This hot tub better be hot!"
scene ep11_cabin_sauna_event141 with dissolve
ji "It's very nice. My head is still cold, but the warmth against my body makes up for it."
scene ep11_cabin_sauna_event142 with dissolve
isa "Mmm... It's so relaxing."
scene ep11_cabin_sauna_event143 with dissolve
bia "I didn't think you guys would do it. You're badass!"
$ guideSuggestedPage = 179
$ tmp_list = [False, False, False, False]
scene ep11_cabin_sauna_event144 with dissolve
label ep11_sauna_loop2_label:
if False not in tmp_list:
    jump ep11_sauna_cont_label
menu:
    "Relax for a while":
        $ tmp_list[0] = True
        scene ep11_cabin_sauna_event145
        show screen ep10_snow_screen
        with dissolve
        $ renpy.pause()
        scene ep11_cabin_sauna_event146 with dissolve
        $ renpy.pause()
        scene ep11_cabin_sauna_event147 with dissolve
        $ renpy.pause()
        scene ep11_cabin_sauna_event148 with dissolve
        $ renpy.pause()
        jump ep11_sauna_loop2_label
    "Sneak a peek":
        menu ep11_sauna_peek_loop_label:
            "Jill":
                scene ep11_cabin_sauna_event149
                show screen ep10_snow_screen
                with dissolve
                $ renpy.pause()
                scene ep11_cabin_sauna_event150 with dissolve
                $ renpy.pause()
                scene ep11_cabin_sauna_event151
                hide screen ep10_snow_screen
                with dissolve
                $ renpy.pause()
                jump ep11_sauna_peek_loop_label
            "Bella":
                scene ep11_cabin_sauna_event152
                show screen ep10_snow_screen
                with dissolve
                $ renpy.pause()
                scene ep11_cabin_sauna_event153 with dissolve
                $ renpy.pause()
                scene ep11_cabin_sauna_event154
                hide screen ep10_snow_screen
                with dissolve
                $ renpy.pause()
                jump ep11_sauna_peek_loop_label
            "Bianca":
                scene ep11_cabin_sauna_event155
                show screen ep10_snow_screen
                with dissolve
                $ renpy.pause()
                scene ep11_cabin_sauna_event156 with dissolve
                $ renpy.pause()
                scene ep11_cabin_sauna_event157
                hide screen ep10_snow_screen
                with dissolve
                $ renpy.pause()
                jump ep11_sauna_peek_loop_label
            "Go back":
                jump ep11_sauna_loop2_label
    "Talk to Jill" if not tmp_list[1]:
        $ tmp_list[1] = True
        if branchJill:
            scene ep11_cabin_sauna_event158
            show screen ep10_snow_screen
            with dissolve
            mc "Are you comfortable?"
            scene ep11_cabin_sauna_event159 with dissolve
            ji "I am."
            scene ep11_cabin_sauna_event160 with dissolve
            mc "You are?"
            scene ep11_cabin_sauna_event159 with dissolve
            ji "Weird, huh?"
            scene ep11_cabin_sauna_event160 with dissolve
            mc "I was gonna say."
            scene ep11_cabin_sauna_event159 with dissolve
            ji "I think it's the alcohol."
            scene ep11_cabin_sauna_event161 with dissolve
            $ renpy.pause()
            scene ep11_cabin_sauna_event162 with dissolve
            $ renpy.pause()
            scene ep11_cabin_sauna_event163 with dissolve
            bia "Keep your hands above surface level, Jill. No funny business in the hot tub."
            scene ep11_cabin_sauna_event164 with dissolve
            ji "As if."
            scene ep11_cabin_sauna_event165
            hide screen ep10_snow_screen
            with dissolve
            $ renpy.pause()
            scene ep11_cabin_sauna_event166
            show screen ep10_snow_screen
            with dissolve
            ji "*{i}Whispers{/i}* You heard her. No funny business."
            scene ep11_cabin_sauna_event167 with dissolve
            mc "I think that only applied to you."
            scene ep11_cabin_sauna_event170 with dissolve
            bia "[name]? No funny business."
            scene ep11_cabin_sauna_event171 with dissolve
            ji "I told you."
            scene ep11_cabin_sauna_event168 with dissolve
            isa "Is he having problems keeping his hands to himself?"
            scene ep11_cabin_sauna_event169 with dissolve
            mc "No, I'm being a good boy."
            scene ep11_cabin_sauna_event172 with dissolve
            ji "*{i}Cough{/i}* Lies."
            scene ep11_cabin_sauna_event173 with dissolve
            mc "Aren't you supposed to be on my side?"
            ji "Hahaha!"
            scene ep11_cabin_sauna_event174 with dissolve
            bia "That does it. If you can't behave around Jill, I'm gonna have to sit between you."
            scene ep11_cabin_sauna_event176 with dissolve
            ji "Haha, what are you doing!?"
            scene ep11_cabin_sauna_event175 with dissolve
            bia "I'm the fun police."
            scene ep11_cabin_sauna_event178 with dissolve
            $ renpy.pause()
            scene ep11_cabin_sauna_event177 with dissolve
            $ renpy.pause()
            scene ep11_cabin_sauna_event179
            hide screen ep10_snow_screen
            with dissolve
            
            if persistent.mod_wtenabled: 
                        $mod_choices = ["(More Bianca options)","(-Sage)","(-DIK)","(+DIK)","(+5 Josy)","(-5 Josy)","","","","","","" ]
                        #[mod_gr][mod_choices[0]]
                        #\n{size=-4}[m_c1][mod_choices[1]][m_c2][mod_choices[4]]
            
            menu:
                "Push her away":
                    label ep11_bianca_help_label:
                    play sound "sound_effects/water_splash.mp3"
                    scene ep11_cabin_sauna_event193
                    show screen ep10_snow_screen
                    with hpunch
                    mc "No police allowed on this side of the hot tub!"
                    scene ep11_cabin_sauna_event194 with dissolve
                    ji "Hahaha!"
                    scene ep11_cabin_sauna_event192 with dissolve
                    bia "You bastard! Haha!"
                "Sit still \n{size=-4}[m_c1][mod_choices[0]]":
                    $ ep11_bianca_dick = 1
                    scene ep11_cabin_sauna_event180
                    show screen ep10_snow_screen
                    with dissolve
                    ji "The fun police? We haven't done anything wrong."
                    scene ep11_cabin_sauna_event181
                    hide screen ep10_snow_screen
                    with dissolve
                    $ renpy.pause()
                    scene ep11_cabin_sauna_event182
                    show screen ep10_snow_screen
                    with dissolve
                    bia "Woah! Uh..."
                    bia "Right, you are! Carry on!"
                    scene ep11_cabin_sauna_event183 with dissolve
                    ji "Nuh-uh! Where do you think you're going?"
                    scene ep11_cabin_sauna_event184
                    hide screen ep10_snow_screen
                    with dissolve
                    $ renpy.pause()
                    scene ep11_cabin_sauna_event185
                    show screen ep10_snow_screen
                    with dissolve
                    bia "[name]? Help me out here?"
                    if not ((ep11_bianca_feet or ep11_bianca_pic > 0) and ep11_bianca_flirt):
                        jump ep11_bianca_help_label
                    scene ep11_cabin_sauna_event186 with dissolve
                    
                    if persistent.mod_wtenabled: 
                        $mod_choices = ["(+3 DIK)","(+5 Cheater)","(-DIK)","(+DIK)","(+5 Josy)","(-5 Josy)","","","","","","" ]
                        #[mod_gr][mod_choices[0]]
                        #\n{size=-4}[m_c1][mod_choices[1]][m_c2][mod_choices[4]]
                    
                    menu:
                        "Help her out":
                            jump ep11_bianca_help_label
                        "Tease her \n{size=-4}[m_c1][mod_choices[0]][m_c2][mod_choices[1]]":
                            $ ep11_bianca_dick = 2
                            $ dk(3)
                            $ tc += 5
                            scene ep11_cabin_sauna_event187 with dissolve
                            mc "Help a cop? No, I don't work that way."
                            scene ep11_cabin_sauna_event188 with dissolve
                            bia "Oh, really?"
                            scene ep11_cabin_sauna_event189 with dissolve
                            $ renpy.pause()
                            play sound "sound_effects/water_splash.mp3"
                            scene ep11_cabin_sauna_event190 with vpunch
                            ji "Haha! Ok, you're free to go, officer!"
                            scene ep11_cabin_sauna_event191 with dissolve
                            $ renpy.pause()
                            $ new_bio("Bianca", "I got a bit too close to Bianca in the hot tub. Jill and Isabella didn't notice, but Bianca did.")
        else:
            scene ep11_cabin_sauna_event195
            show screen ep10_snow_screen
            with dissolve
            ji "Haha, this feels weird."
            scene ep11_cabin_sauna_event196 with dissolve
            mc "Bathing naked?"
            scene ep11_cabin_sauna_event197 with dissolve
            ji "No, not that. The snow."
            ji "It feels weird feeling snow fall on my face while I'm perfectly comfy neck below."
            ji "And how the fresh and cold air - which was way too cold before - now feels great because the hot tub is so warm."
            scene ep11_cabin_sauna_event198 with dissolve
            mc "When you put it like that, it does feel weird."
            scene ep11_cabin_sauna_event200 with dissolve
            isa "So, does bathing naked with three others feel fine?"
            scene ep11_cabin_sauna_event199 with dissolve
            ji "Yes, I think it's the alcohol. But also that you guys started it."
            ji "I wouldn't have done it if everyone wasn't on board. I know that much."
            scene ep11_cabin_sauna_event200 with dissolve
            isa "I'm surprised that [name] was the last one to do it. Since he promised to do it, I thought he'd be first."
            scene ep11_cabin_sauna_event201 with dissolve
            mc "*{i}Sigh{/i}* Screw you, Bianca."
            bia "Hahaha!"
        jump ep11_sauna_loop2_label
    "Talk to Bella" if not tmp_list[2]:
        $ tmp_list[2] = True
        scene ep11_cabin_sauna_event202
        show screen ep10_snow_screen
        with dissolve
        mc "Can I have some?"
        scene ep11_cabin_sauna_event203 with dissolve
        isa "Of course. I've been hogging the bottle, haven't I?"
        scene ep11_cabin_sauna_event204 with dissolve
        mc "I can't blame you."
        if branchIsabella:
            scene ep11_cabin_sauna_event205 with dissolve
            isa "Enjoying yourself?"
            scene ep11_cabin_sauna_event204 with dissolve
            mc "Haha, I mean... How could I not?"
            scene ep11_cabin_sauna_event206 with dissolve
            isa "Typical."
            scene ep11_cabin_sauna_event207 with dissolve
            mc "It wasn't my idea. Hell, you stripped down and jumped in before I did."
            mc "Maybe I should say \"typical\" to you. Are you enjoying {b}yourself{/b}?"
            scene ep11_cabin_sauna_event208 with dissolve
            isa "I am, but not for the same perverted reasons you are."
            isa "Well, maybe a bit."
            scene ep11_cabin_sauna_event212 with dissolve
            isa "*{i}Whispers{/i}* You do look very enticing like this. And knowing I'm an arm's length away from your cock below the surface is exciting."
            scene ep11_cabin_sauna_event213 with dissolve
            mc "You can't talk like that to me right now. Jeez... Parts of me won't be below the surface if you do."
            mc "It will come popping up like a whack-a-mole."
            scene ep11_cabin_sauna_event212 with dissolve
            isa "Haha, don't worry. I'll whack it."
            scene ep11_cabin_sauna_event213 with dissolve
            mc "I'd rather see you jack it."
            scene ep11_cabin_sauna_event212 with dissolve
            isa "Now, who's talking dirty?"
            scene ep11_cabin_sauna_event213 with dissolve
            mc "Again, you started it. You know I'm easy to spur on."
            mc "If we were here alone, I'd make you sit in my lap."
            scene ep11_cabin_sauna_event212 with dissolve
            isa "I don't think sitting in front of you is out of the question, though."
            scene ep11_cabin_sauna_event214 with dissolve
            isa "Just keep your hands reasonably to yourself."
            if ep9_b_kissed_jill:
                scene ep11_cabin_sauna_event216b with dissolve
            else:
                scene ep11_cabin_sauna_event216 with dissolve
            bia "Aw, look at you two."
            scene ep11_cabin_sauna_event215 with dissolve
            isa "I hope we're not making you two feel awkward."
            if ep9_b_kissed_jill:
                scene ep11_cabin_sauna_event216b with dissolve
            else:
                scene ep11_cabin_sauna_event216 with dissolve
            bia "Like you could in this hot tub."
            scene ep11_cabin_sauna_event217 with dissolve
            $ renpy.pause()
            scene ep11_cabin_sauna_event218 with dissolve
            mc "This feels nice."
            scene ep11_cabin_sauna_event219 with dissolve
            isa "One might even say it feels romantic...if it weren't for that hard thing pressed against my back."
            scene ep11_cabin_sauna_event222 with dissolve
            mc "Can you feel that?"
            scene ep11_cabin_sauna_event220 with dissolve
            isa "Yes. And for your information, I can also feel it when you spoon me in bed. But I choose not to bring attention to it."
            scene ep11_cabin_sauna_event221 with dissolve
            mc "And for {b}your{/b} information, I can't control it. I just can't."
            scene ep11_cabin_sauna_event220 with dissolve
            isa "It's ok, [name]. I don't mind it."
            scene ep11_cabin_sauna_event222 with dissolve
            mc "It's a compliment to you, really."
            isa "I wouldn't take it that far, but ok."
            scene ep11_cabin_sauna_event217 with dissolve
            $ renpy.pause()
        else:
            mc "I wonder what my classmates would say if they saw us now."
            scene ep11_cabin_sauna_event205 with dissolve
            isa "That's a thought I don't want to entertain."
            scene ep11_cabin_sauna_event204 with dissolve
            mc "It's just a fun thought. I would never tell them."
            scene ep11_cabin_sauna_event206 with dissolve
            isa "I wouldn't be in this hot tub if I thought you would."
            scene ep11_cabin_sauna_event207 with dissolve
            if ep5_like_champagne:
                mc "This Champagne tastes even better than the one I had at the preps' party."
            else:
                mc "This Champagne is very good. I didn't think I would like it, but here we are."
            scene ep11_cabin_sauna_event208 with dissolve
            isa "Look at you becoming a snob with a refined taste."
            scene ep11_cabin_sauna_event211 with dissolve
            ji "Refined taste? Haha! I once watched [name] put ketchup on ramen noodles."
            scene ep11_cabin_sauna_event209 with dissolve
            isa "I retract my statement."
            scene ep11_cabin_sauna_event210 with dissolve
            mc "I told you! We were out of hot sauce."
            scene ep11_cabin_sauna_event211 with dissolve
            ji "Hahaha!"
        jump ep11_sauna_loop2_label
    "Talk to Bianca" if not tmp_list[3]:
        $ tmp_list[3] = True
        scene ep11_cabin_sauna_event223
        show screen ep10_snow_screen
        with dissolve
        isa "Oh, this bottle is already done for."
        scene ep11_cabin_sauna_event225 with dissolve
        ji "Didn't you bring the wine?"
        scene ep11_cabin_sauna_event224 with dissolve
        isa "I left it in the sauna. I'll fetch it."
        scene ep11_cabin_sauna_event226 with dissolve
        bia "Never fret! I feared that bottle wouldn't last us, so I put one over here. Haha!"
        
        if persistent.mod_wtenabled: 
                        $mod_choices = ["(+3 DIK)","(+5 Cheater)","(-DIK)","(+DIK)","(+5 Josy)","(-5 Josy)","","","","","","" ]
                        #[mod_gr][mod_choices[0]]
                        #\n{size=-4}[m_c1][mod_choices[1]][m_c2][mod_choices[4]]
        
        menu:
            "Avert your eyes \n{size=-4}[m_c1][mod_choices[2]]":
                $ dk(-1)
                scene ep11_cabin_sauna_event227 with dissolve
                $ renpy.pause()
            "Look closer \n{size=-4}[m_c1][mod_choices[3]]":
                $ dk(1)
                scene ep11_cabin_sauna_event228 with dissolve
                $ renpy.pause()
        play sound "sound_effects/season3/champagne_pop.mp3"
        scene ep11_cabin_sauna_event229 with vpunch
        bia "There we go!"
        bia "[name], do you want some?"
        scene ep11_cabin_sauna_event230 with dissolve
        menu:
            "Sure":
                mc "Sure."
                scene ep11_cabin_sauna_event231 with dissolve
                bia "Open up."
                scene ep11_cabin_sauna_event232 with dissolve
                isa "This spells disaster."
                play sound "sound_effects/bottle_pour.mp3"
                scene ep11_cabin_sauna_event233 with dissolve
                mc "*{i}Glug glug{/i}* This reminds me of Hell Week."
                scene ep11_cabin_sauna_event234 with dissolve
                ji "Is that so?"
                scene ep11_cabin_sauna_event233 with dissolve
                mc "*{i}Glug glug{/i}* Yeah, the boys used to force us to drink like this."
                scene ep11_cabin_sauna_event235 with dissolve
                isa "Not naked, I assume."
                scene ep11_cabin_sauna_event234 with dissolve
                ji "Haha!"
            "No thanks":
                mc "No thanks. Maybe later."
        jump ep11_sauna_loop2_label
    "Continue" if not False in tmp_list:
        $ renpy.pause(0.5)

label ep11_sauna_cont_label:
scene ep11_cabin_sauna_event236
show screen ep10_snow_screen
with dissolve
bia "I'm so proud of you, Jill. I didn't think you'd have the guts to bathe in the snow like that."
scene ep11_cabin_sauna_event237 with dissolve
ji "Did you forget I did that last winter?"
scene ep11_cabin_sauna_event236 with dissolve
bia "I meant naked! That's the part I can't believe."
if branchIsabella:
    bia "Especially when [name] is with us."
scene ep11_cabin_sauna_event237 with dissolve
ji "You've always had a talent for pushing my boundaries."
scene ep11_cabin_sauna_event238 with dissolve
isa "That sounds like a good friend to me."
scene ep11_cabin_sauna_event240 with dissolve
bia "Jill is crazier than you'd think."
scene ep11_cabin_sauna_event241 with dissolve
ji "I'm not, though."
scene ep11_cabin_sauna_event240 with dissolve
bia "Oh, really? Did you guys know Jill and I once made out for fun?"
scene ep11_cabin_sauna_event237 with dissolve
ji "Bianca..."
scene ep11_cabin_sauna_event239 with dissolve
mc "I did not know that. How did that happen?"
scene ep11_cabin_sauna_event242 with dissolve
ji "Why are you encouraging her?"
scene ep11_cabin_sauna_event239 with dissolve
mc "Because it sounded like a story I'd like to hear."
scene ep11_cabin_sauna_event242 with dissolve
ji "There's not much of a story to it."
scene ep11_cabin_sauna_event243 with dissolve
bia "It's one hell of a story!"
scene ep11_cabin_sauna_event237 with dissolve
ji "Overselling it."
scene ep11_cabin_sauna_event236 with dissolve
bia "How would you tell it, then?"
scene ep11_cabin_sauna_event237 with dissolve
ji "I wouldn't tell it at all."
if ep7_jill_lewd:
    scene ep11_cabin_sauna_event243 with dissolve
    bia "[name], I told you about the barn parties Jill and I had, right?"
    scene ep11_cabin_sauna_event244 with dissolve
    mc "You tried to, at least."
scene ep11_cabin_sauna_event240 with dissolve
bia "Anyway, Jill and I used to party together at her family's barn."
scene ep11_cabin_sauna_event241 with dissolve
ji "We were teenagers. We didn't know what party meant back then."
scene ep11_cabin_sauna_event240 with dissolve
bia "Right. It was mostly us listening to music, reading magazines, and fake smoking."
scene ep11_cabin_sauna_event238 with dissolve
isa "Fake smoking?"
scene ep11_cabin_sauna_event237 with dissolve
ji "Bianca smoked paper from the magazines because she made it look like a cigarette."
scene ep11_cabin_sauna_event240 with dissolve
bia "It hurt my throat a lot! But stupid me thought it was cool at the time, haha."
scene ep11_cabin_sauna_event243 with dissolve
bia "But after Jill turned 18, I decided it was time for us to party for real."
scene ep11_cabin_sauna_event238 with dissolve
isa "18? So, this story isn't that old."
scene ep11_cabin_sauna_event240 with dissolve
bia "No, but it feels like a long time ago."
bia "So, I swiped a big bottle of Dad's liquor for our party and we had some of it."
scene ep11_cabin_sauna_event245 with dissolve
ji "It tasted horrible. We couldn't drink or stomach it."
scene ep11_cabin_sauna_event243 with dissolve
bia "Yeah, so we figured we had to mix it with something."
bia "We mixed it with sodas the next time, and it tasted way better."
scene ep11_cabin_sauna_event240 with dissolve
bia "Jill got drunk from it. She drank way more than I did."
scene ep11_cabin_sauna_event241 with dissolve
ji "Not way more. I just got intoxicated faster than you."
scene ep11_cabin_sauna_event243 with dissolve
bia "And with this drunken look, she started asking me questions about guys and stuff."
scene ep11_cabin_sauna_event237 with dissolve
ji "I did not!"
scene ep11_cabin_sauna_event236 with dissolve
bia "You did! You asked me how it was like to make out with a guy."
scene ep11_cabin_sauna_event246 with dissolve
ji "I don't recall."
scene ep11_cabin_sauna_event248 with dissolve
bia "But I do. And I told her it was like eating ice cream, but only if the kiss was good."
bia "And then she asked me if I would kiss her so she could know what I meant."
scene ep11_cabin_sauna_event246 with dissolve
ji "You're making it up."
scene ep11_cabin_sauna_event248 with dissolve
bia "I'm not."
scene ep11_cabin_sauna_event250 with dissolve
mc "So, you two kissed?"
scene ep11_cabin_sauna_event247 with dissolve
ji "[name], stop picturing it."
scene ep11_cabin_sauna_event248 with dissolve
bia "Oh, yes. We kissed. And it tasted like ice cream. Right, Jill?"
scene ep11_cabin_sauna_event246 with dissolve
ji "I've stopped listening by now."
scene ep11_cabin_sauna_event248 with dissolve
bia "It did, [name]. Totally did."
scene ep11_cabin_sauna_event249 with dissolve
if branchJill:
    mc "Oh, I know it does. I believe you."
else:
    mc "I bet."
scene ep11_cabin_sauna_event253 with dissolve
isa "Is anyone else getting hungry?"
scene ep11_cabin_sauna_event241 with dissolve
ji "Yes, I'm starting to."
scene ep11_cabin_sauna_event253 with dissolve
isa "Then maybe it is time."
scene ep11_cabin_sauna_event254 with dissolve
mc "Um... In like five minutes or so."
scene ep11_cabin_sauna_event251 with dissolve
ji "Why five?"
scene ep11_cabin_sauna_event255 with dissolve
isa "[name]..."
scene ep11_cabin_sauna_event252 with dissolve
bia "Maybe we let him have five minutes here while we make a run for it?"
scene ep11_cabin_sauna_event254 with dissolve
mc "I think you have to."
scene ep11_cabin_sauna_event257 with dissolve
ji "One-two-three-GO!"
scene ep11_cabin_sauna_event256 with dissolve
mc "Why can't you behave? You're embarrassing us."
stop music fadeout 3
scene black
hide screen ep10_snow_screen
with Fade(1,1,1)
$ renpy.pause(3)
$ new_bio("Bianca", "We bathed nude in the snow and hot tub at Bianca's family cabin.")
$ new_bio("Jill", "We bathed nude in the snow and hot tub at Bianca's family cabin.")
$ new_bio("Isabella", "We bathed nude in the snow and hot tub at Bianca's family cabin.")

label ep11_cabin_fire_event_label:
$ renpy.sound.play("sound_effects/season3/fireplace.mp3", channel="sfx2", loop=True)
play music "music/ep11/silent_night.mp3"
if branchJill and tmp_mod2=="Jill":
    scene ep11_cabin_fire_event1 with dissolve
else:
    scene ep11_cabin_fire_event28 with dissolve
$ renpy.pause()
if branchJill and tmp_mod2=="Jill":
    scene ep11_cabin_fire_event2 with dissolve
else:
    scene ep11_cabin_fire_event29 with dissolve
$ renpy.pause()
if branchJill and tmp_mod2=="Jill":
    scene ep11_cabin_fire_event3 with dissolve
else:
    scene ep11_cabin_fire_event30 with dissolve
$ renpy.pause()
if branchJill and tmp_mod2=="Jill":
    scene ep11_cabin_fire_event4 with dissolve
    $ renpy.pause()
else:
    scene ep11_cabin_fire_event31 with dissolve
    $ renpy.pause()
    scene ep11_cabin_fire_event32 with dissolve
    $ renpy.pause()
if branchJill and tmp_mod2=="Jill":
    scene ep11_cabin_fire_event5 with dissolve
else:
    scene ep11_cabin_fire_event34 with dissolve
ji "I could fall asleep right here."
scene ep11_cabin_fire_event6 with dissolve
bia "Yup. I'm full, drunk and perfectly content."
if branchJill and tmp_mod2=="Jill":
    scene ep11_cabin_fire_event7 with dissolve
else:
    scene ep11_cabin_fire_event33 with dissolve
isa "Thank you so much for this weekend, Bianca. It was a much-needed break from daily life."
scene ep11_cabin_fire_event6 with dissolve
bia "Anytime. I couldn't have asked for better company."

label ep11_cabin_end_label:
if branchJill and tmp_mod2=="Jill":
    scene ep11_cabin_fire_event8 with dissolve
    isa "I think I'm going to brush my teeth and hit the sack."
    scene ep11_cabin_fire_event9 with dissolve
    mc "Sign me up for that. I'm beat..."
    scene ep11_cabin_fire_event10 with dissolve
    ji "Go ahead. We'll be right behind you."
    scene ep11_cabin_fire_event11 with dissolve
    bia "We will?"
    scene ep11_cabin_fire_event12 with dissolve
    ji "I wanted to tell you something in private."
    scene ep11_cabin_fire_event16 with dissolve
    bia "About what?"
    scene ep11_cabin_fire_event12 with dissolve
    ji "That story you told them in the hot tub was awkward for me."
    scene ep11_cabin_fire_event16 with dissolve
    bia "Come on, it wasn't that bad."
    scene ep11_cabin_fire_event13 with dissolve
    ji "No, but..."
    ji "Swear you won't be all {i}you{/i} tomorrow and bring this up."
    scene ep11_cabin_fire_event16 with dissolve
    bia "Bring what up?"
    scene ep11_cabin_fire_event12 with dissolve
    ji "One time, Bella and I were hanging out at her place, and we had some wine and went to bed."
    scene ep11_cabin_fire_event17 with dissolve
    bia "Oh my God. What did you do in bed with her!? Not what I'm thinking, right?"
    scene ep11_cabin_fire_event14 with dissolve
    ji "What are you thinking?"
    scene ep11_cabin_fire_event17 with dissolve
    bia "Oh, it's perverted."
    scene ep11_cabin_fire_event14 with dissolve
    ji "Then no."
    scene ep11_cabin_fire_event15 with dissolve
    ji "We did what you and I did in that barn."
    scene ep11_cabin_fire_event18 with dissolve
    bia "Shut up!"
    scene ep11_cabin_fire_event19 with dissolve
    ji "It's hard to describe it. We had such a great night together, with deep and meaningful talks..."
    ji "We got tipsy, and when we got into bed, we hugged for a while."
    ji "And then, before I knew what I was doing, we kissed."
    scene ep11_cabin_fire_event20 with dissolve
    bia "No way you did that. How did you do it?"
    scene ep11_cabin_fire_event19 with dissolve
    ji "I don't know. It was...a few very long kisses and hugs."
    ji "It felt nice in a weird way. But we stopped because we realized it was wrong."
    scene ep11_cabin_fire_event20 with dissolve
    bia "So, you have a history with her?"
    scene ep11_cabin_fire_event21 with dissolve
    ji "It wasn't about attraction. It was about comfort."
    ji "She needed it, and I think I needed it, too. And we got it in the wrong way from each other."
    scene ep11_cabin_fire_event22 with dissolve
    bia "I swear, whenever I think you will always be this vanilla girl in a sundress, you surprise me with something new."
    bia "Like today with the hot tub and now with this. You're blowing my mind here, Jill."
    scene ep11_cabin_fire_event23 with dissolve
    ji "Well, now you know. Don't go around making any innuendos, though. Bella doesn't like it when I bring it up."
    ji "And I needed you to know so you don't continue pushing that button. I could tell she felt awkward about it, too."
    scene ep11_cabin_fire_event22 with dissolve
    bia "So, you made out with another one of your friends? Big deal. That happens a lot at parties."
    bia "Do you know how common threesomes are? Especially in college?"
    scene ep11_cabin_fire_event23 with dissolve
    ji "This was different from that. Let's leave this discussion at that, ok?"
    scene ep11_cabin_fire_event22 with dissolve
    bia "Hm... Are you sure that's all there was to it? I'm sensing something here..."
    scene ep11_cabin_fire_event23 with dissolve
    ji "I'm going to bed now."
    scene ep11_cabin_fire_event25 with dissolve
    bia "Wait. Don't I get a goodnight kiss?"
    scene ep11_cabin_fire_event24 with dissolve
    ji "That's not funny."
    scene ep11_cabin_fire_event25 with dissolve
    bia "It's not a joke; I want one."
    scene ep11_cabin_fire_event26 with dissolve
    ji "*{i}Smack{/i}*"
    scene ep11_cabin_fire_event27 with dissolve
    bia "Hahaha!"
    ji "Haha! Don't test me!"
    scene ep11_cabin_fire_event24 with dissolve
    ji "Good night, Bianca."
    $ phone_clear_jump_label = "ep11_jill_lewd_label"
else:
    scene ep11_cabin_fire_event36 with dissolve
    isa "Sleep well, you two. That's it for us."
    mc "Good night."
    scene ep11_cabin_fire_event34 with dissolve
    ji "Good night!"
    scene ep11_cabin_fire_event35 with dissolve
    bia "G'night!"
    $ phone_clear_jump_label = "ep11_bella2_lewd_label"
$ renpy.music.stop(channel="sfx2", fadeout=3)
jump end_freeroam

label ep11_jill_lewd_label:
if _in_replay:
    if persistent.name == None:
        $ name = "MC"
    else:
        $ name = persistent.name
    if persistent.mc_jill == None:
        $ mc_jill = name
    else:
        $ mc_jill = persistent.mc_jill
    if persistent.jill == None:
        $ jill = "Jill"
    else:
        $ jill = persistent.jill
    $ ep11_jill_tease = False
    play music "music/ep11/silent_night.mp3"
hide screen new_phone_screen

scene ep11_jill_lewd4 with dissolve
ji "I don't know how, but this bed looks even more inviting tonight."
scene ep11_jill_lewd5 with dissolve
mc "Are you as tired as I am?"
scene ep11_jill_lewd6 with dissolve
ji "It was a long day and night. The energy skiing didn't drain was lost in the sauna and hot tub."
scene ep11_jill_lewd7 with dissolve
mc "Yeah, we did a lot today. I can feel it in every muscle. I'm gonna be sore tomorrow."
scene ep11_jill_lewd8 with dissolve
ji "If I wasn't tired, I'd offer you a massage."
scene ep11_jill_lewd9 with dissolve
mc "It's fine. My body is more than relaxed right now. The hot tub made sure of it."
scene ep11_jill_lewd10 with dissolve
ji "How crazy was that?"
scene ep11_jill_lewd11 with dissolve
mc "Pretty crazy, yeah. I won't be able to look you girls in the eyes tomorrow."
scene ep11_jill_lewd10 with dissolve
ji "Haha, you think?"
scene ep11_jill_lewd11 with dissolve
mc "Nah, it was fun. I thought everyone was daring to do that."
mc "I feel like I'll remember this day forever."
scene ep11_jill_lewd12 with dissolve
ji "So? Winter. How would you rate it now?"
scene ep11_jill_lewd13 with dissolve
mc "Thanks to you, it's pretty good."
scene ep11_jill_lewd14 with dissolve
ji "I did it! Haha!"
scene ep11_jill_lewd13 with dissolve
mc "You sure did. Thank you for this."
scene ep11_jill_lewd15 with dissolve
ji "You're welcome."
scene ep11_jill_lewd24 with dissolve
ji "*{i}Smack{/i}*"
scene ep11_jill_lewd25 with dissolve
ji "*{i}Smack{/i}*"
scene ep11_jill_lewd16 with dissolve
mc "Mmm..."
ji "Oh no... You're not horny, are you?"
scene ep11_jill_lewd17 with dissolve
mc "I'm trying not to be. I know you're tired, but when you're lying on top of me like this..."
scene ep11_jill_lewd18 with dissolve
ji "You should have said so earlier... Now I'm too tired."
scene ep11_jill_lewd17 with dissolve
mc "When should I have said it? In the hot tub?"
scene ep11_jill_lewd18 with dissolve
ji "Haha, no! But I had a hunch that you were."
scene ep11_jill_lewd19 with dissolve
mc "I tried to keep it to myself."
scene ep11_jill_lewd20 with dissolve
ji "Ok. It's unfair to have you sit through all that and then head straight to sleep."
scene ep11_jill_lewd21 with dissolve
mc "You don't have to if you're tired."
scene ep11_jill_lewd22 with dissolve
ji "I was horny back there too. Shh!"
scene ep11_jill_lewd23 with dissolve
mc "Haha! No way!"
scene ep11_jill_lewd22 with dissolve
ji "I kept it to myself as well. Not bad, huh?"
scene ep11_jill_lewd24 with dissolve
ji "*{i}Smack{/i}*"
scene ep11_jill_lewd26 with dissolve
mc "Was it because of Bianca's barn story or me?"
scene ep11_jill_lewd27 with dissolve
ji "Haha, don't ruin this. It was because of you, of course."
scene ep11_jill_lewd28 with dissolve
ji "Yes, Bianca and I had some fun times together, but another time, we got caught drinking by Mom, and she got mad at us."
ji "She scolded us and even told on Bianca."
ji "So, it wasn't always those kind of stories."
scene ep11_jill_lewd29 with dissolve
mc "You don't have to feel ashamed because of that story. I enjoyed it."
scene ep11_jill_lewd30 with dissolve
ji "I bet you did."
scene ep11_jill_lewd31 with dissolve
ji "[mc_jill]?"
scene ep11_jill_lewd32 with dissolve
mc "Yeah?"
scene ep11_jill_lewd33 with dissolve
ji "Do you want to...fuck me?"
scene ep11_jill_lewd34 with dissolve
mc "Just when I thought that winter couldn't get any better."
scene ep11_jill_lewd35 with dissolve
ji "Hahaha!"
scene ep11_jill_lewd36 with dissolve
$ renpy.pause()
scene anim_jill_tits_ep11 with dissolve
mc "*{i}Smack lick{/i}*"
label ep11_jill_lewd_loop_label:
menu:
    "Kiss her":
        scene anim_jill_kiss_ep11 with dissolve
        pause
        scene anim_jill_kiss2_ep11 with dissolve
        pause
        jump ep11_jill_lewd_loop_label
    "Kiss her neck":
        scene ep11_jill_lewd37 with dissolve
        mc "*{i}Smack{/i}*"
        ji "Mmm..."
        jump ep11_jill_lewd_loop_label
    "Lick her tits":
        scene anim_jill_tits_ep11 with dissolve
        mc "*{i}Smack lick{/i}*"
        pause
        jump ep11_jill_lewd_loop_label
    "Continue":
        $ renpy.pause(0.5)

scene ep11_jill_lewd38 with dissolve
$ renpy.pause()
scene ep11_jill_lewd39 with dissolve
$ renpy.pause()
scene ep11_jill_lewd40 with dissolve
$ renpy.pause()
label ep11_jill_lewd_loopb_label:
menu:
    "Finger her":
        scene anim_jill_finger_ep11 with dissolve
        pause
        scene anim_jill_finger2_ep11 with dissolve
        pause
        scene ep11_jill_lewd41 with dissolve
        ji "Mmmphff..."
        jump ep11_jill_lewd_loopb_label
    "Lick her":
        scene anim_jill_lick_ep11 with dissolve
        mc "*{i}Lick lick{/i}*"
        jump ep11_jill_lewd_loopb_label
    "Tease her butthole":
        scene anim_jill_tease_ep11 with dissolve
        if not ep11_jill_tease:
            ji "*{i}Moans{/i}* What are you doing with your finger?"
            mc "*{i}Lick lick{/i}* Relax and see if you like it or not."
        pause
        if not ep11_jill_tease:
            $ ep11_jill_tease = True
            mc "How is it?"
            scene ep11_jill_lewd42 with dissolve
            ji "It got me confused at first. And then..."
            ji "No, I think I'm still confused. I'm sorry..."
            scene anim_jill_tease_ep11 with dissolve
            mc "Don't be sorry. It's new to you."
        jump ep11_jill_lewd_loopb_label
    "Continue":
        $ renpy.pause(0.5)

scene anim_jill_bj_ep11 with dissolve
mc "You're getting good at that... I like it when you go for it without being asked."
ji "*{i}Suck suck glug glug{/i}*"
pause

$ tmpInt = 0
label ep11_jill_lewd_loop2_label:
menu:
    "Blowjob":
        scene anim_jill_bj_ep11 with dissolve
        ji "*{i}Suck suck glug glug{/i}*"
        pause
        jump ep11_jill_lewd_loop2_label
    "Missionary":
        $ tmpInt += 1
        scene anim_jill_miss1_ep11 with dissolve
        pause
        scene anim_jill_miss2_ep11 with dissolve
        pause
        jump ep11_jill_lewd_loop2_label
    "Cowgirl":
        $ tmpInt += 1
        scene anim_jill_ride1_ep11 with dissolve
        pause
        scene anim_jill_ride2_ep11 with dissolve
        pause
        jump ep11_jill_lewd_loop2_label
    "Doggystyle":
        $ tmpInt += 1
        scene anim_jill_doggy1_ep11 with dissolve
        ji "Hnn... Fuck me, [mc_jill]."
        pause
        scene anim_jill_doggy2_ep11 with dissolve
        mc "Fuck, you feel so good, [jill]."
        pause
        jump ep11_jill_lewd_loop2_label
    "Sideways":
        $ tmpInt += 1
        scene anim_jill_side_ep11 with dissolve
        pause
        jump ep11_jill_lewd_loop2_label
    "Embracing":
        $ tmpInt += 1
        scene anim_jill_hold1_ep11 with dissolve
        pause
        scene anim_jill_hold2_ep11 with dissolve
        pause
        scene anim_jill_hold3_ep11 with dissolve
        pause
        jump ep11_jill_lewd_loop2_label
    "Standing":
        $ tmpInt += 1
        scene anim_jill_stand1_ep11 with dissolve
        pause
        jump ep11_jill_lewd_loop2_label
    "Cum" if tmpInt > 2:
        menu:
            "On ass":
                scene anim_jill_doggy2_ep11 with dissolve
                mc "[jill]... I'm gonna cum."
                pause
                scene ep11_jill_lewd45 at vpunch, cum2
                $ renpy.pause(0.5)
                scene ep11_jill_lewd45 at vpunch, cum2
                $ renpy.pause(0.5)
                scene ep11_jill_lewd45 at vpunch, cum2
                $ renpy.pause()
                scene ep11_jill_lewd46 with dissolve
                $ renpy.pause()
            "Creampie":
                scene anim_jill_doggy2_ep11 with dissolve
                mc "[jill]... I'm gonna cum."
                if tmpInt > 4:
                    ji "Keep going. I'm cumming too... Ahh..."
                    scene ep11_jill_lewd43b with vpunch
                    $ renpy.pause(0.5)
                    scene ep11_jill_lewd43b with vpunch
                    $ renpy.pause(0.5)
                    scene ep11_jill_lewd43b with vpunch
                    ji "*{i}Moans{/i}*"
                scene ep11_jill_lewd43 at vpunch, cum1
                $ renpy.pause(0.5)
                scene ep11_jill_lewd43 at vpunch, cum1
                $ renpy.pause(0.5)
                scene ep11_jill_lewd43 at vpunch, cum1
                $ renpy.pause()
                scene ep11_jill_lewd44 with dissolve
                $ renpy.pause()
            "On belly":
                scene anim_jill_miss1_ep11 with dissolve
                mc "[jill]... I'm gonna cum."
                pause
                scene ep11_jill_lewd47 at vpunch, cum2
                $ renpy.pause(0.5)
                scene ep11_jill_lewd47 at vpunch, cum2
                $ renpy.pause(0.5)
                scene ep11_jill_lewd47 at vpunch, cum2
                $ renpy.pause()
                scene ep11_jill_lewd48 with dissolve
                $ renpy.pause()

scene ep11_jill_lewd49 with dissolve
ji "*{i}Exhales{/i}* So good... Mmm..."
scene ep11_jill_lewd50 with dissolve
mc "Yeah. We're getting good at this."
scene ep11_jill_lewd49 with dissolve
ji "I'll say."
scene ep11_jill_lewd50 with dissolve
mc "Haha..."
scene ep11_jill_lewd51 with dissolve
ji "What's funny?"
scene ep11_jill_lewd52 with dissolve
mc "Usually, I'm the tired one. Now you look half asleep."
scene ep11_jill_lewd51 with dissolve
ji "Yes, I feel I could fall asleep on the spot."
scene ep11_jill_lewd52 with dissolve
mc "Thanks again for this amazing weekend."
scene ep11_jill_lewd53 with dissolve
ji "You too."
scene ep11_jill_lewd54 with dissolve
$ renpy.pause()

$ renpy.end_replay()
$ persistent.ep11_lewd_jill = True
$ calcScenes()
$ mphone_stats_add_girl_s3("jill","You had sex with Jill in Bianca's family cabin in episode 11.")
show screen new_phone_screen
scene ep11_jill_lewd1 with dissolve
$ renpy.pause()
scene ep11_jill_lewd2 with dissolve
bia "So... These walls are thin."
scene ep11_jill_lewd3 with dissolve
isa "Sure are."
scene ep11_jill_lewd2 with dissolve
bia "Earplugs?"
scene ep11_jill_lewd3 with dissolve
isa "Yes, please."

jump ep11_trip_end_label

label ep11_bella2_lewd_label:
if _in_replay:
    if persistent.name == None:
        $ name = "MC"
    else:
        $ name = persistent.name
    if persistent.mc_isabella == None:
        $ mc_isabella = name
    else:
        $ mc_isabella = persistent.mc_isabella
    if persistent.isabella == None:
        $ isabella = "Isabella"
    else:
        $ isabella = persistent.isabella
    $ affinity = "CHICK"
    play music "music/ep11/silent_night.mp3"
    $ RPisabella = 0

hide screen new_phone_screen

scene ep11_bella2_lewd17 with dissolve
mc "I don't want to return home tomorrow. I want to stay here for at least another week."
scene ep11_bella2_lewd18 with dissolve
isa "It's been an amazing trip. Spending this quality time with you is something I've wished for."
scene ep11_bella2_lewd19 with dissolve
mc "Did it feel weird to be here with Jill and Bianca to you?"
scene ep11_bella2_lewd20 with dissolve
isa "It did at first, but today, it felt natural."
scene ep11_bella2_lewd21 with dissolve
mc "It's a shame we weren't alone in the hot tub."
scene ep11_bella2_lewd22 with dissolve
isa "Ha!"
scene ep11_bella2_lewd23 with dissolve
mc "What's ha?"
scene ep11_bella2_lewd22 with dissolve
isa "Don't pretend it was horrible to be alone with three girls, naked in a hot tub."
isa "Your eyes were as excited as when we watched that adult movie together."
scene ep11_bella2_lewd24 with dissolve
mc "Yeah, but I couldn't do what I wanted with you in that hot tub. So, that sucked."
scene ep11_bella2_lewd25 with dissolve
isa "Did you ever have sex underwater? Because it sounds better than what it is."
scene ep11_bella2_lewd26 with dissolve
isa "The friction gets weird, and it never lives up to the fantasy."
scene ep11_bella2_lewd27 with dissolve
mc "Who said anything about having sex underwater?"
scene ep11_bella2_lewd28 with dissolve
isa "Oh... I thought you were talking about sex."
isa "Given the dirty talk in the hot tub, it didn't occur to me that you were thinking about something more romantic."
if affinity == "CHICK":
    scene ep11_bella2_lewd27 with dissolve
    mc "Well, I thought it would have been nice to make out in the hot tub. Doing that in front of Jill and Bianca would have been awkward."
    scene ep11_bella2_lewd28 with dissolve
    isa "Mmm... That sounds nice."
else:
    scene ep11_bella2_lewd27 with dissolve
    mc "Again, you misunderstand me. You don't have to be underwater to have sex in a hot tub."
    mc "You can sit on the edge of it, too, and move around when you fuck."
    scene ep11_bella2_lewd28 with dissolve
    isa "I suppose you can do that too, yes."
scene ep11_bella2_lewd30 with dissolve
isa "*{i}Smack{/i}*"
scene ep11_bella2_lewd27 with dissolve
mc "Are you in the mood or too tired?"
scene ep11_bella2_lewd28 with dissolve
isa "Both. But I'd hate it if we spent this lovely weekend in this cabin without having sex at least once."
scene ep11_bella2_lewd29 with dissolve
mc "Haha, that sounds like something I would say. I'm happy you're horny too."
scene ep11_bella2_lewd31 with dissolve
isa "We'll have to keep it down. Don't moan too loudly."
mc "That's a big thing to ask for, but I'll try."
label ep11_bella2_lewd_loop_label:
menu:
    "Kiss her":
        scene anim_bella_kiss_ep11 with dissolve
        isa "*{i}Smack{/i}* Mmm..."
        pause
        jump ep11_bella2_lewd_loop_label
    "Lick her tits":
        scene anim_bella_tits_ep11 with dissolve
        mc "*{i}Lick lick{/i}*"
        pause
        jump ep11_bella2_lewd_loop_label
    "Lick her pussy":
        scene anim_bella_lick_ep11 with dissolve
        mc "*{i}Lick lick{/i}*"
        isa "*{i}Moans{/i}*"
        mc "You taste so good."
        pause
        jump ep11_bella2_lewd_loop_label
    "Continue":
        $ renpy.pause(0.5)

$ tmpInt = 0
$ tmpBool3 = False
label ep11_bella_lewd_loop2_label:
menu:
    "Blowjob":
        scene anim_bella_bj1_ep11 with dissolve
        mc "I love how you suck my dick. Suck it harder..."
        isa "*{i}Suck suck{/i}*"
        mc "Fuck, yes! Like that. Damn..."
        pause
        jump ep11_bella_lewd_loop2_label
    "Missionary":
        $ tmpInt += 1
        scene anim_bella_miss1_ep11 with dissolve
        isa "*{i}Moans{/i}* Fuck me, [mc_isabella]. Shove your fat cock inside me."
        pause
        scene anim_bella_miss2_ep11 with dissolve
        isa "*{i}Suck suck{/i}*"
        mc "Yeah, give me that smoldering, sexy look. Fuck, I could cum from looking into your eyes."
        pause
        scene anim_bella_miss3_ep11 with dissolve
        mc "You feel so fucking good, [isabella]."
        pause
        jump ep11_bella_lewd_loop2_label
    "Embracing":
        $ tmpInt += 1
        scene anim_bella_ride1_ep11 with dissolve
        mc "*{i}Suck suck{/i}*"
        isa "*{i}Moans{/i}* You love sucking on my tits, don't you?"
        mc "Yeah, I love it."
        pause
        scene anim_bella_ride2_ep11 with dissolve
        isa "Suck on them, [mc_isabella]. Just don't cum too early when you do."
        pause
        scene anim_bella_ride3_ep11 with dissolve
        mc "*{i}Suck suck{/i}*"
        pause
        jump ep11_bella_lewd_loop2_label
    "Cowgirl":
        $ tmpInt += 1
        scene anim_bella_ride4_ep11 with dissolve
        isa "Your cock is so deep inside me..."
        pause
        scene anim_bella_ride5_ep11 with dissolve
        if tmpInt > 4 and not tmpBool3:
            $ tmpBool3 = True
            isa "[mc_isabella], I'm cumming... I'm cumming!"
            scene ep11_bella2_lewd33 with vpunch
            $ renpy.pause(0.5)
            scene ep11_bella2_lewd33 with vpunch
            $ renpy.pause(0.5)
            scene ep11_bella2_lewd34 with vpunch
            $ renpy.pause(0.5)
            scene ep11_bella2_lewd34 with vpunch
            isa "*{i}Moans{/i}*"
            scene ep11_bella2_lewd35 with dissolve
            $ RPisabella += 1
            isa "You're so good in bed..."
        elif tmpBool3:
            isa "You're so good in bed..."
        else:
            isa "I feel like I'm on the verge of cumming from this... But not yet."
        pause
        jump ep11_bella_lewd_loop2_label
    "Reverse cowgirl":
        $ tmpInt += 1
        scene anim_bella_rev1_ep11 with dissolve
        mc "Ride me like that. I wanna see your ass bounce."
        isa "*{i}Moans{/i}* It feels so good, [mc_isabella]."
        pause
        jump ep11_bella_lewd_loop2_label
    "Prone":
        $ tmpInt += 1
        scene anim_bella_prone1_ep11 with dissolve
        isa "Fuck me, [mc_isabella]."
        pause
        scene anim_bella_prone2_ep11 with dissolve
        mc "If I had some lube, I'd stick it in your ass."
        isa "*{i}Moans{/i}* I wouldn't be able to keep my voice down if you did."
        pause
        jump ep11_bella_lewd_loop2_label
    "Standing":
        $ tmpInt += 1
        scene anim_bella_stand1_ep11 with dissolve
        isa "Are you getting close to cumming, [mc_isabella]?"
        mc "With you, I always am."
        pause
        scene anim_bella_stand2_ep11 with dissolve
        pause
        jump ep11_bella_lewd_loop2_label
    "Cum" if tmpInt > 2:
        mc "Ok... I can't hold it in for longer. I gotta cum."
        menu:
            "Creampie":
                scene anim_bella_ride1_ep11 with dissolve
                isa "Cum inside me, [mc_isabella]. Burst deep inside me."
                mc "*{i}Suck suck{/i}* Hnnnn..."
                scene ep11_bella2_lewd36 at vpunch, cum1
                $ renpy.pause(0.5)
                scene ep11_bella2_lewd36 at vpunch, cum1
                $ renpy.pause(0.5)
                scene ep11_bella2_lewd36 at vpunch, cum1
                mc "Hngn... Ahh... Fuck!"
                scene ep11_bella2_lewd37 with dissolve
                mc "I came so damned hard inside you. Sucking on your tit while doing it was amazing..."
            "In mouth":
                isa "Cum in my mouth, [mc_isabella]."
                scene anim_bella_bj1_ep11 with dissolve
                mc "Fuck... I'm so close. Keep going..."
                isa "*{i}Suck suck suck suck{/i}*"
                scene ep11_bella2_lewd38 at vpunch, cum2
                $ renpy.pause(0.5)
                scene ep11_bella2_lewd38 at vpunch, cum2
                $ renpy.pause(0.5)
                scene ep11_bella2_lewd38 at vpunch, cum2
                mc "Hngn... Ahh... Fuck!"
                scene ep11_bella2_lewd39 with dissolve
                mc "You don't even realize how sexy you are right now."
            "On ass":
                isa "I know how I want you to cum."
                scene anim_bella_cum_ep11 with dissolve
                mc "Oh my God, what are you doing?"
                isa "I'm gonna squeeze that cum out of you. And you're gonna burst all over my ass."
                mc "Fuck, this feels so damn good..."
                scene anim_bella_cum2_ep11 with vpunch
                mc "Fuck! Ahhh!"
                pause
                scene ep11_bella2_lewd32 with dissolve
                mc "Wow... That was hot and scary at the same time."

scene ep11_bella2_lewd40 with dissolve
isa "Ahh... This was a perfect weekend."
scene ep11_bella2_lewd41 with dissolve
mc "It already was perfect, but somehow you made it better."
scene ep11_bella2_lewd42 with dissolve
isa "*{i}Smack{/i}*"
$ renpy.end_replay()
$ persistent.ep11_lewd_bella2 = True
$ calcScenes()
$ mphone_stats_add_girl_s3("isabella","You had sex with Bella in Bianca's family cabin in episode 11.")
scene ep11_bella2_lewd44 with dissolve
mc "I wish I could end every night like this with you."
scene ep11_bella2_lewd43 with dissolve
isa "With sex?"
scene ep11_bella2_lewd44 with dissolve
if affinity == "CHICK":
    mc "In bed with you."
else:
    mc "Yeah, but also in bed with you like this."
scene ep11_bella2_lewd43 with dissolve
isa "It would be something."
isa "If you want, we can try to do this more often at my place. How about we do more sleepovers during the week?"
scene ep11_bella2_lewd44 with dissolve
mc "If you don't mind me riding to campus with you, I'd love to."
scene ep11_bella2_lewd43 with dissolve
isa "I'd have to drop you off before campus to avoid questions, but sure. We'll make it work."
show screen new_phone_screen

scene ep11_bella2_lewd1 with dissolve
$ renpy.pause()
scene ep11_bella2_lewd2 with dissolve
ji "Perhaps you should have told them about how thin these walls are."
scene ep11_bella2_lewd8 with dissolve
bia "If you think now is a good time to do that, go ahead."
scene ep11_bella2_lewd3 with dissolve
ji "No, I'm not going in there."

scene ep11_bella2_lewd9 with dissolve
bia "Is it awful hearing this for you? I mean, given your history with him."
scene ep11_bella2_lewd2 with dissolve
ji "I'm trying not to think about that right now. And it's awkward to hear Bella moan, too."
scene ep11_bella2_lewd8 with dissolve
bia "Haha, yeah. But for different reasons."
scene ep11_bella2_lewd4 with dissolve
$ renpy.pause()
scene ep11_bella2_lewd13 with dissolve
bia "Right?"
scene ep11_bella2_lewd2 with dissolve
ji "Huh? Yes!"
scene ep11_bella2_lewd4 with dissolve
$ renpy.pause()
scene ep11_bella2_lewd5 with dissolve
ji "Or...kind of."
scene ep11_bella2_lewd2 with dissolve
ji "In the hot tub, that story you told them was awkward for me."
scene ep11_bella2_lewd9 with dissolve
bia "Come on, it wasn't that bad."
scene ep11_bella2_lewd2 with dissolve
ji "No, but..."
ji "Swear you won't be all {i}you{/i} tomorrow and bring this up."
scene ep11_bella2_lewd9 with dissolve
bia "Bring what up?"
scene ep11_bella2_lewd5 with dissolve
ji "One time when Bella and I had been hanging out at her place, we had some wine and went to bed."
scene ep11_bella2_lewd10 with dissolve
bia "Oh my God. What did you do in bed with her!? Not what I'm thinking, right?"
scene ep11_bella2_lewd2 with dissolve
ji "What are you thinking?"
scene ep11_bella2_lewd10 with dissolve
bia "Oh, it's perverted."
scene ep11_bella2_lewd2 with dissolve
ji "Then no."
scene ep11_bella2_lewd3 with dissolve
ji "We did what you and I did in that barn."
scene ep11_bella2_lewd11 with dissolve
bia "Shut up!"
scene ep11_bella2_lewd3 with dissolve
ji "It's hard to describe it. We had such a great night together, with deep and meaningful talks..."
ji "We got tipsy, and when we got into bed, we hugged for a while."
ji "And then, before I knew what I was doing, we kissed."
scene ep11_bella2_lewd11 with dissolve
bia "No way you did that. How did you do it?"
scene ep11_bella2_lewd6 with dissolve
ji "I don't know. It was...a few very long kisses and hugs."
ji "It felt nice in a weird way. But we stopped because we realized it was wrong."
scene ep11_bella2_lewd12 with dissolve
bia "So, you have a history with her too?"
scene ep11_bella2_lewd2 with dissolve
ji "It wasn't about attraction. It was about comfort."
ji "She needed it, and I think I needed it, too. And we got it in the wrong way from each other."
scene ep11_bella2_lewd12 with dissolve
bia "I swear, whenever I think you will always be this vanilla girl in a sundress, you surprise me with something new."
bia "Like today with the hot tub and now with this. You're blowing my mind here, Jill."
scene ep11_bella2_lewd6 with dissolve
ji "Well, now you know. Don't go around making any innuendos. Bella doesn't like it when I bring it up."
scene ep11_bella2_lewd8 with dissolve
bia "So, you made out with another one of your friends? Big deal. That happens a lot at parties."
bia "Do you know how common threesomes are? Especially in college?"
scene ep11_bella2_lewd6 with dissolve
ji "This was different from that. Let's leave this discussion at that, ok?"
scene ep11_bella2_lewd8 with dissolve
bia "Hm... Are you sure that's all there was to it? I'm sensing something here..."
bia "And you bringing that up when you're in bed with me... What does that mean?"
scene ep11_bella2_lewd7 with dissolve
ji "Stop it."
scene ep11_bella2_lewd8 with dissolve
bia "If I hug you now, will you kiss me?"
scene ep11_bella2_lewd14 with dissolve
ji "*{i}Smack{/i}*"
scene ep11_bella2_lewd15 with dissolve
bia "Hahaha!"
ji "Haha, don't test me!"
scene ep11_bella2_lewd16 with dissolve
$ renpy.pause()
jump ep11_trip_end_label

label ep11_trip_end_label:

if branchIsabella and branchJill:

    "scrappy" "Do you want to see the other cabin trip path?"
    menu:
        "Yes":
            jump ep11_trip_label
        "No. Continue the game.":
            pass

$ phone_bars_zero = False
stop music fadeout 3
scene black with Fade(1,1,1)
$ renpy.pause(3)
$ new_bio("Bianca", "We had a great time together on the cabin trip.")
if branchJill:
    $ new_bio("Jill", "We had a great time together on the cabin trip. Jill got to show me that winter could be fun.")
else:
    $ new_bio("Jill", "We had a great time together on the cabin trip.")
if branchIsabella:
    $ new_bio("Isabella", "We had a great time together on the cabin trip. It was nice being together as a couple without worrying about who saw us kissing.")
else:
    $ new_bio("Isabella", "We had a great time together on the cabin trip.")
jump ep11_franz_label
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
