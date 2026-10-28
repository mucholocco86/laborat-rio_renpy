label ep10_freeroam_bbq_intro_label:
$ mphone_music_genre = 2
$ mphone_play_songs(["music/ep10/licensed_music/track140.mp3","music/ep10/licensed_music/track137.mp3","music/ep10/licensed_music/track136.mp3"])
scene anim_bbq_intro_ep10 with fade
$ renpy.pause()

$ renpy.sound.play("sound_effects/season2/sizzle.mp3", channel="sfx2", loop=False)
if ep10_pp_meat == 2:
    scene ep10_freeroam_bbq1 with dissolve
    $ renpy.pause()
    $ renpy.music.stop(channel="sfx2", fadeout=3)
    scene ep10_freeroam_bbq4 with dissolve
    if minigames:
        $ specialMessage = "DIKs' happiness decreased!"
        $ pp_happiness_level[0] = max(pp_happiness_level[0]-4,0)
        $ pp_happiness_level[2] = max(pp_happiness_level[2]-4,0)
        $ pp_happiness_level[3] = max(pp_happiness_level[3]-4,0)
        $ pp_happiness_level[4] = max(pp_happiness_level[4]-4,0)
        $ pp_happiness_level[6] = max(pp_happiness_level[6]-4,0)
        $ mphone_pp_history_list.append("• The {color=ffed00}Hot Dogs{/color} activity decreased Derek's happiness by {color=ff0000}4%{/color}.")
        $ mphone_pp_history_list.append("• The {color=ffed00}Hot Dogs{/color} activity decreased Jamie's happiness by {color=ff0000}4%{/color}.")
        $ mphone_pp_history_list.append("• The {color=ffed00}Hot Dogs{/color} activity decreased John Boy's happiness by {color=ff0000}4%{/color}.")
        $ mphone_pp_history_list.append("• The {color=ffed00}Hot Dogs{/color} activity decreased Leon's happiness by {color=ff0000}4%{/color}.")
        $ mphone_pp_history_list.append("• The {color=ffed00}Hot Dogs{/color} activity decreased Rusty's happiness by {color=ff0000}4%{/color}.")
        show screen specialmsg
    jb "We're just having hot dogs? What a letdown."
    hide screen specialmsg

    if ep10_pp_alcohol == 2:
        scene ep10_freeroam_bbq5 with dissolve
        if minigames:
            $ specialMessage = "DIKs' happiness decreased!"
            $ pp_happiness_level[0] = max(pp_happiness_level[0]-4,0)
            $ pp_happiness_level[2] = max(pp_happiness_level[2]-4,0)
            $ pp_happiness_level[5] = max(pp_happiness_level[5]-4,0)
            $ pp_happiness_level[6] = max(pp_happiness_level[6]-4,0)
            $ pp_happiness_level[7] = max(pp_happiness_level[7]-4,0)
            $ mphone_pp_history_list.append("• The {color=ffed00}B.Y.O.B.{/color} activity decreased Derek's happiness by {color=ff0000}4%{/color}.")
            $ mphone_pp_history_list.append("• The {color=ffed00}B.Y.O.B.{/color} activity decreased Jamie's happiness by {color=ff0000}4%{/color}.")
            $ mphone_pp_history_list.append("• The {color=ffed00}B.Y.O.B.{/color} activity decreased Nick's happiness by {color=ff0000}4%{/color}.")
            $ mphone_pp_history_list.append("• The {color=ffed00}B.Y.O.B.{/color} activity decreased Rusty's happiness by {color=ff0000}4%{/color}.")
            $ mphone_pp_history_list.append("• The {color=ffed00}B.Y.O.B.{/color} activity decreased Tommy's happiness by {color=ff0000}4%{/color}.")
            show screen specialmsg
        tm "Do you wanna talk about a letdown? Why the fuck did we have to bring our own booze?"
    elif ep10_pp_alcohol == 1:
        scene ep10_freeroam_bbq5 with dissolve
        if minigames:
            $ specialMessage = "DIKs' happiness increased slightly!"
            $ pp_happiness_level[0] = min(pp_happiness_level[0]+2,100)
            $ pp_happiness_level[7] = min(pp_happiness_level[7]+2,100)
            $ mphone_pp_history_list.append("• The {color=ffed00}Leftover Alcohol{/color} activity increased Derek's happiness by {color=00ff00}+2%{/color}.")
            $ mphone_pp_history_list.append("• The {color=ffed00}Leftover Alcohol{/color} activity increased Tommy's happiness by {color=00ff00}+2%{/color}.")
            show screen specialmsg
        tm "Do you wanna talk about a letdown? Why are we drinking leftover liquor from Halloween?"
    else:
        scene ep10_freeroam_bbq6 with dissolve
        if minigames:
            $ specialMessage = "DIKs' happiness increased!"
            $ pp_happiness_level[0] = min(pp_happiness_level[0]+2,100)
            $ pp_happiness_level[2] = min(pp_happiness_level[2]+2,100)
            $ pp_happiness_level[5] = min(pp_happiness_level[5]+2,100)
            $ pp_happiness_level[6] = min(pp_happiness_level[6]+2,100)
            $ pp_happiness_level[7] = min(pp_happiness_level[7]+2,100)
            $ mphone_pp_history_list.append("• The {color=ffed00}New Alcohol{/color} activity increased Derek's happiness by {color=00ff00}+2%{/color}.")
            $ mphone_pp_history_list.append("• The {color=ffed00}New Alcohol{/color} activity increased Jamie's happiness by {color=00ff00}+2%{/color}.")
            $ mphone_pp_history_list.append("• The {color=ffed00}New Alcohol{/color} activity increased Nick's happiness by {color=00ff00}+2%{/color}.")
            $ mphone_pp_history_list.append("• The {color=ffed00}New Alcohol{/color} activity increased Rusty's happiness by {color=00ff00}+2%{/color}.")
            $ mphone_pp_history_list.append("• The {color=ffed00}New Alcohol{/color} activity increased Tommy's happiness by {color=00ff00}+2%{/color}.")
            show screen specialmsg
        tm "Who cares? At least they didn't fuck up the drinks."
elif ep10_pp_meat == 1:
    scene ep10_freeroam_bbq2 with dissolve
    $ renpy.pause()
    $ renpy.music.stop(channel="sfx2", fadeout=3)
    scene ep10_freeroam_bbq4 with dissolve
    if minigames:
        $ specialMessage = "DIKs' happiness increased slightly!"
        $ pp_happiness_level[0] = min(pp_happiness_level[0]+2,100)
        $ pp_happiness_level[4] = min(pp_happiness_level[4]+2,100)
        $ mphone_pp_history_list.append("• The {color=ffed00}BBQ Pork{/color} activity increased Derek's happiness by {color=00ff00}+2%{/color}.")
        $ mphone_pp_history_list.append("• The {color=ffed00}BBQ Pork{/color} activity increased Leon's happiness by {color=00ff00}+2%{/color}.")
        show screen specialmsg
    jb "I know I shouldn't bitch, but this meat is kinda crappy."
    hide screen specialmsg
    if ep10_pp_alcohol == 2:
        scene ep10_freeroam_bbq5 with dissolve
        if minigames:
            $ specialMessage = "DIKs' happiness decreased!"
            $ pp_happiness_level[0] = max(pp_happiness_level[0]-4,0)
            $ pp_happiness_level[2] = max(pp_happiness_level[2]-4,0)
            $ pp_happiness_level[5] = max(pp_happiness_level[5]-4,0)
            $ pp_happiness_level[6] = max(pp_happiness_level[6]-4,0)
            $ pp_happiness_level[7] = max(pp_happiness_level[7]-4,0)
            $ mphone_pp_history_list.append("• The {color=ffed00}B.Y.O.B.{/color} activity decreased Derek's happiness by {color=ff0000}4%{/color}.")
            $ mphone_pp_history_list.append("• The {color=ffed00}B.Y.O.B.{/color} activity decreased Jamie's happiness by {color=ff0000}4%{/color}.")
            $ mphone_pp_history_list.append("• The {color=ffed00}B.Y.O.B.{/color} activity decreased Nick's happiness by {color=ff0000}4%{/color}.")
            $ mphone_pp_history_list.append("• The {color=ffed00}B.Y.O.B.{/color} activity decreased Rusty's happiness by {color=ff0000}4%{/color}.")
            $ mphone_pp_history_list.append("• The {color=ffed00}B.Y.O.B.{/color} activity decreased Tommy's happiness by {color=ff0000}4%{/color}.")
            show screen specialmsg
        tm "At least you're getting food. Why the fuck did we have to bring our own booze?"
    elif ep10_pp_alcohol == 1:
        scene ep10_freeroam_bbq5 with dissolve
        if minigames:
            $ specialMessage = "DIKs' happiness increased slightly!"
            $ pp_happiness_level[0] = min(pp_happiness_level[0]+2,100)
            $ pp_happiness_level[7] = min(pp_happiness_level[7]+2,100)
            $ mphone_pp_history_list.append("• The {color=ffed00}Leftover Alcohol{/color} activity increased Derek's happiness by {color=00ff00}+2%{/color}.")
            $ mphone_pp_history_list.append("• The {color=ffed00}Leftover Alcohol{/color} activity increased Tommy's happiness by {color=00ff00}+2%{/color}.")
            show screen specialmsg
        tm "That's not the only thing that's crappy. Why are we drinking leftover liquor from Halloween?"
    else:
        scene ep10_freeroam_bbq6 with dissolve
        if minigames:
            $ specialMessage = "DIKs' happiness increased!"
            $ pp_happiness_level[0] = min(pp_happiness_level[0]+2,100)
            $ pp_happiness_level[2] = min(pp_happiness_level[2]+2,100)
            $ pp_happiness_level[5] = min(pp_happiness_level[5]+2,100)
            $ pp_happiness_level[6] = min(pp_happiness_level[6]+2,100)
            $ pp_happiness_level[7] = min(pp_happiness_level[7]+2,100)
            $ mphone_pp_history_list.append("• The {color=ffed00}New Alcohol{/color} activity increased Derek's happiness by {color=00ff00}+2%{/color}.")
            $ mphone_pp_history_list.append("• The {color=ffed00}New Alcohol{/color} activity increased Jamie's happiness by {color=00ff00}+2%{/color}.")
            $ mphone_pp_history_list.append("• The {color=ffed00}New Alcohol{/color} activity increased Nick's happiness by {color=00ff00}+2%{/color}.")
            $ mphone_pp_history_list.append("• The {color=ffed00}New Alcohol{/color} activity increased Rusty's happiness by {color=00ff00}+2%{/color}.")
            $ mphone_pp_history_list.append("• The {color=ffed00}New Alcohol{/color} activity increased Tommy's happiness by {color=00ff00}+2%{/color}.")
            show screen specialmsg
        tm "Who cares? At least they didn't fuck up the drinks."
else:
    scene ep10_freeroam_bbq3 with dissolve
    $ renpy.pause()
    $ renpy.music.stop(channel="sfx2", fadeout=3)
    scene ep10_freeroam_bbq7 with dissolve
    if minigames:
        $ specialMessage = "DIKs' happiness increased!"
        $ pp_happiness_level[0] = min(pp_happiness_level[0]+2,100)
        $ pp_happiness_level[1] = min(pp_happiness_level[1]+2,100)
        $ pp_happiness_level[3] = min(pp_happiness_level[3]+2,100)
        $ pp_happiness_level[4] = min(pp_happiness_level[4]+2,100)
        $ pp_happiness_level[6] = min(pp_happiness_level[6]+2,100)
        $ mphone_pp_history_list.append("• The {color=ffed00}BBQ Quality Meat{/color} activity increased Derek's happiness by {color=00ff00}+2%{/color}.")
        $ mphone_pp_history_list.append("• The {color=ffed00}BBQ Quality Meat{/color} activity increased Jacob's happiness by {color=00ff00}+2%{/color}.")
        $ mphone_pp_history_list.append("• The {color=ffed00}BBQ Quality Meat{/color} activity increased John Boy's happiness by {color=00ff00}+2%{/color}.")
        $ mphone_pp_history_list.append("• The {color=ffed00}BBQ Quality Meat{/color} activity increased Leon's happiness by {color=00ff00}+2%{/color}.")
        $ mphone_pp_history_list.append("• The {color=ffed00}BBQ Quality Meat{/color} activity increased Rusty's happiness by {color=00ff00}+2%{/color}.")
        show screen specialmsg
    jb "Those steaks look delicious! You guys went the extra mile for us, didn't you?"
    if minigames:
        hide screen specialmsg
    if ep10_pp_alcohol == 2:
        scene ep10_freeroam_bbq5 with dissolve
        if minigames:
            $ specialMessage = "DIKs' happiness decreased!"
            $ pp_happiness_level[0] = max(pp_happiness_level[0]-4,0)
            $ pp_happiness_level[2] = max(pp_happiness_level[2]-4,0)
            $ pp_happiness_level[5] = max(pp_happiness_level[5]-4,0)
            $ pp_happiness_level[6] = max(pp_happiness_level[6]-4,0)
            $ pp_happiness_level[7] = max(pp_happiness_level[7]-4,0)
            $ mphone_pp_history_list.append("• The {color=ffed00}B.Y.O.B.{/color} activity decreased Derek's happiness by {color=ff0000}4%{/color}.")
            $ mphone_pp_history_list.append("• The {color=ffed00}B.Y.O.B.{/color} activity decreased Jamie's happiness by {color=ff0000}4%{/color}.")
            $ mphone_pp_history_list.append("• The {color=ffed00}B.Y.O.B.{/color} activity decreased Nick's happiness by {color=ff0000}4%{/color}.")
            $ mphone_pp_history_list.append("• The {color=ffed00}B.Y.O.B.{/color} activity decreased Rusty's happiness by {color=ff0000}4%{/color}.")
            $ mphone_pp_history_list.append("• The {color=ffed00}B.Y.O.B.{/color} activity decreased Tommy's happiness by {color=ff0000}4%{/color}.")
            show screen specialmsg
        tm "And now I get why this is a B.Y.O.B. party. [name] blew the budget on food. Such a bitch move..."
    elif ep10_pp_alcohol == 1:
        scene ep10_freeroam_bbq5 with dissolve
        if minigames:
            $ specialMessage = "DIKs' happiness increased slightly!"
            $ pp_happiness_level[0] = min(pp_happiness_level[0]+2,100)
            $ pp_happiness_level[7] = min(pp_happiness_level[7]+2,100)
            $ mphone_pp_history_list.append("• The {color=ffed00}Leftover Alcohol{/color} activity increased Derek's happiness by {color=00ff00}+2%{/color}.")
            $ mphone_pp_history_list.append("• The {color=ffed00}Leftover Alcohol{/color} activity increased Tommy's happiness by {color=00ff00}+2%{/color}.")
            show screen specialmsg
        tm "But why are we drinking leftover liquor from Halloween? Didn't you have any money to spare on drinks?"
    else:
        scene ep10_freeroam_bbq6 with dissolve
        if minigames:
            $ specialMessage = "DIKs' happiness increased!"
            $ pp_happiness_level[0] = min(pp_happiness_level[0]+2,100)
            $ pp_happiness_level[2] = min(pp_happiness_level[2]+2,100)
            $ pp_happiness_level[5] = min(pp_happiness_level[5]+2,100)
            $ pp_happiness_level[6] = min(pp_happiness_level[6]+2,100)
            $ pp_happiness_level[7] = min(pp_happiness_level[7]+2,100)
            $ mphone_pp_history_list.append("• The {color=ffed00}New Alcohol{/color} activity increased Derek's happiness by {color=00ff00}+2%{/color}.")
            $ mphone_pp_history_list.append("• The {color=ffed00}New Alcohol{/color} activity increased Jamie's happiness by {color=00ff00}+2%{/color}.")
            $ mphone_pp_history_list.append("• The {color=ffed00}New Alcohol{/color} activity increased Nick's happiness by {color=00ff00}+2%{/color}.")
            $ mphone_pp_history_list.append("• The {color=ffed00}New Alcohol{/color} activity increased Rusty's happiness by {color=00ff00}+2%{/color}.")
            $ mphone_pp_history_list.append("• The {color=ffed00}New Alcohol{/color} activity increased Tommy's happiness by {color=00ff00}+2%{/color}.")
            show screen specialmsg
        tm "I see where the money you could have spent on a better venue went. But I'm not gonna complain when food and drinks are this good."
if minigames:
    hide screen specialmsg
    $ pp_update_happiness_icons()

scene ep10_freeroam_bbq8 with dissolve
mc "How's the food coming along?"
if branchMayaJosy:
    scene ep10_freeroam_bbq9 with dissolve
    tm "Pff..."
    scene ep10_freeroam_bbq10 with dissolve
    jb "Is he still mad at you?"
    scene ep10_freeroam_bbq11 with dissolve
    mc "Yeah, he's not letting it go, it seems."
scene ep10_freeroam_bbq12 with dissolve
jm "It's almost time for dinner. Bring the boys together."
scene ep10_freeroam_bbq13 with dissolve
if ep10_pp_meat == 2:
    jb "I'll do it. Don't burn those hot dogs."
else:
    jb "I'll do it. You tend to that meat."
if ep10_pp_meat == 2:
    scene ep10_freeroam_bbq14 with dissolve
elif ep10_pp_meat == 1:
    scene ep10_freeroam_bbq15 with dissolve
else:
    scene ep10_freeroam_bbq16 with dissolve
mc "Looking good, Jamie."
scene ep10_freeroam_bbq17 with dissolve
jm "Thanks. I'm glad John Boy left, he was watching me like a hawk."
scene ep10_freeroam_bbq18 with dissolve
mc "Haha, I bet he was."
scene ep10_freeroam_bbq19 with dissolve
jm "I'm looking forward to tonight. It's gonna be fun to hang with the bros."
scene ep10_freeroam_bbq18 with dissolve
mc "The HOTs are over there and I believe some people are showing up later."
scene ep10_freeroam_bbq19 with dissolve
jm "Yeah, but still, I like hanging out with the guys."
scene ep10_freeroam_bbq18 with dissolve
if branchMayaJosy:
    mc "Yeah. If Tommy doesn't pout all night, it will be fun."
else:
    mc "Yeah, it will be fun."
scene ep10_freeroam_bbq20 with dissolve
jac "[name], is it true?"
scene ep10_freeroam_bbq21 with dissolve
mc "What's it?"
scene ep10_freeroam_bbq20 with dissolve
jac "Zoey's dropping by later?"
scene ep10_freeroam_bbq21 with dissolve
if not ep10_zoey_hangout:
    mc "Yeah, she might. Apparently, Tommy invited her to the party."
else:
    mc "Yeah, she might. Apparently, both Tommy and I invited her to the party."
scene ep10_freeroam_bbq20 with dissolve
jac "Awesome!"
scene ep10_freeroam_bbq19 with dissolve
jm "Hey, that's cool. I didn't get the chance to talk to her at Halloween, but the guys have been raving about her."
scene ep10_freeroam_bbq18 with dissolve
mc "She sure made an impression on them."
if branchJill:
    scene ep10_freeroam_bbq19 with dissolve
    jm "What about your girl? Is she coming?"
    scene ep10_freeroam_bbq18 with dissolve
    mc "Yeah, she's dropping by later too."
scene ep10_freeroam_bbq22 with dissolve
le "Jamie? Is it true? Dany's not coming?"
scene ep10_freeroam_bbq23 with dissolve
jm "No, she has to take care of Franz. He's sick."
scene ep10_freeroam_bbq22 with dissolve
if ep10_pp_activity == 0:
    if minigames:
        $ specialMessage = "All DIKs' happiness increased!"
        $ pp_happiness_level[0] = min(pp_happiness_level[0]+2,100)
        $ pp_happiness_level[1] = min(pp_happiness_level[1]+2,100)
        $ pp_happiness_level[2] = min(pp_happiness_level[2]+2,100)
        $ pp_happiness_level[3] = min(pp_happiness_level[3]+2,100)
        $ pp_happiness_level[4] = min(pp_happiness_level[4]+2,100)
        $ pp_happiness_level[5] = min(pp_happiness_level[5]+2,100)
        $ pp_happiness_level[6] = min(pp_happiness_level[6]+2,100)
        $ pp_happiness_level[7] = min(pp_happiness_level[7]+2,100)
        $ mphone_pp_history_list.append("• The {color=ffed00}Beer Pong{/color} activity increased all DIKs' happiness by {color=00ff00}+2%{/color}.")
        show screen specialmsg
    le "Awesome! Then it means there will be tits showing during Beer Pong!"
    if minigames:
        hide screen specialmsg
        $ pp_update_happiness_icons()
else:
    if minigames:
        $ specialMessage = "DIKs' happiness decreased!"
        $ pp_happiness_level[0] = max(pp_happiness_level[0]-4,0)
        $ pp_happiness_level[1] = max(pp_happiness_level[1]-4,0)
        $ pp_happiness_level[2] = max(pp_happiness_level[2]-4,0)
        $ pp_happiness_level[3] = max(pp_happiness_level[3]-4,0)
        $ pp_happiness_level[4] = max(pp_happiness_level[4]-4,0)
        $ pp_happiness_level[5] = max(pp_happiness_level[5]-4,0)
        $ pp_happiness_level[6] = max(pp_happiness_level[6]-4,0)
        $ pp_happiness_level[7] = max(pp_happiness_level[7]-4,0)
        $ mphone_pp_history_list.append("• Having {color=ffed00}Nothing{/color} as an activity decreased all DIKs' happiness by {color=ff0000}4%{/color}.")
        show screen specialmsg
    le "Awesome! But now I kinda wish we were playing Beer Pong."
    if minigames:
        hide screen specialmsg
        $ pp_update_happiness_icons()

scene ep10_freeroam_bbq116 with dissolve
sa "If anyone's freezing, there are blankets near the DIKs' tents."
scene ep10_freeroam_bbq117 with dissolve
sar "They're actually going to sleep out here?"
scene ep10_freeroam_bbq131 with dissolve
sa "We'll see about that. For their own good, I hope they won't."
scene ep10_freeroam_bbq135 with dissolve
qu "Worst idea for a party ever. Barbecues are for the summer."
scene ep10_freeroam_bbq132 with dissolve
sa "We're not having a barbecue, we're having an outdoor pizza party."
scene ep10_freeroam_bbq136 with dissolve
qu "Because everyone's too lazy to cook."
scene ep10_freeroam_bbq121 with dissolve
el "Don't be a downer. It is what you make it out to be. Right, Arieth?"
scene ep10_freeroam_bbq122 with dissolve
ar "It's not a party because I can't drink!"
ar "And apparently, it doesn't matter if I eat jello shots either."
scene ep10_freeroam_bbq123 with dissolve
ar "This sucks! Being pregnant sucks!"
ar "Soon, I'll be fat and I won't fit in the bikini I bought for Spring break!"
ar "And I'll get stretchmarks all over my tummy!"
scene ep10_freeroam_bbq143 with dissolve
$ renpy.pause()

if ep10_pp_meat == 2:
    scene ep10_freeroam_bbq24 with dissolve
    jac "I don't care that it's just hot dogs, eating outdoors makes everything delicious."
else:
    scene ep10_freeroam_bbq25 with dissolve
    jac "This food is delicious!"
scene ep10_freeroam_bbq26 with dissolve
le "Eat all you want, bros. This night's for you."
scene ep10_freeroam_bbq27 with dissolve
jm "Where's Tommy?"
scene ep10_freeroam_bbq29 with dissolve
rs "Probably off doing his thing."
scene ep10_freeroam_bbq30 with dissolve
mc "Are there any specific traditions for DIKs' Thanksgiving?"
scene ep10_freeroam_bbq31 with dissolve
rs "We figured it would be a nice way for pledges to show appreciation for their elders after their welcoming here."
rs "But as far as traditions go, we don't exactly have any yet."
scene ep10_freeroam_bbq32 with dissolve
ni "We talked about doing the whole \"What are you thankful for?\" thing, but Tommy thought it was gay."
scene ep10_freeroam_bbq33 with dissolve
tm "It is gay."
tm "\"What are you thankful for?\""
scene ep10_freeroam_bbq34 with dissolve
tm "Oh, I'm thankful for my meaty penis and another year without STDs. Pff..."
scene ep10_freeroam_bbq28 with dissolve
jm "Oh, we're doing it? In that case, I'm thankful for-"
scene ep10_freeroam_bbq34 with dissolve
tm "We're not doing it. I was mocking it."
tm "The only thing we should be thankful for tonight is our brotherhood. That's the reason why we're sitting here, freezing our asses off."
scene ep10_freeroam_bbq28 with dissolve
jm "I was gonna say that I am thankful for that. And I'm also thankful for not being a father this year. That was quite the scare."
if ep10_pp_meat == 2:
    scene ep10_freeroam_bbq24 with dissolve
    jac "I'm thankful for these hot dogs."
else:
    scene ep10_freeroam_bbq25 with dissolve
    jac "If we're doing this, I'm thankful for this great meal you guys have cooked."
scene ep10_freeroam_bbq32 with dissolve
ni "I'm thankful that it's not snowing. I was worried it would."
scene ep10_freeroam_bbq35 with dissolve
tm "Are we really doing this...?"

scene ep10_freeroam_bbq142 with dissolve
qu "*{i}Whispers{/i}* Under the table. I brought the shrooms for you."
scene ep10_freeroam_bbq137 with dissolve
ly "Awesome, awesome..."
scene ep10_freeroam_bbq140 with dissolve
qu "But I must warn you...you should wait until later before you have some."
qu "And start small with one, ok? It's high-quality shit."
scene ep10_freeroam_bbq138 with dissolve
ly "Oh, they're not for me. They're for the DIKs."
scene ep10_freeroam_bbq141 with dissolve
qu "What are you up to?"
scene ep10_freeroam_bbq138 with dissolve
ly "Well, Tommy didn't plan their party..."
ly "...but he asked me to make sure it didn't suck and to fix some entertainment for them."
scene ep10_freeroam_bbq139 with dissolve
ly "And what's more entertaining than seeing someone trip?"
scene ep10_freeroam_bbq141 with dissolve
qu "You're not gonna sneak that into their food or something, right?"
scene ep10_freeroam_bbq139 with dissolve
ly "Fun idea, but I'm not that horrible. Now, if you excuse me... I have a gift to bring."

scene ep10_freeroam_bbq36 with dissolve
rs "And I'm thankful for you guys, too."
if ep10_pp_activity == 0:
    scene ep10_freeroam_bbq37 with dissolve
else:
    scene ep10_freeroam_bbq37b with dissolve
tm "Gay. Gay... So gay."
scene ep10_freeroam_bbq38 with dissolve
if ep10_pp_meat == 2:
    ly "Good evening, boys. I don't want to disturb your literal sausage party..."
    ly "But I bring a gift for Tommy."
else:
    ly "Good evening, boys. I don't want to disturb your sausage party, but I bring a gift for Tommy."
scene ep10_freeroam_bbq40 with dissolve
tm "Hahaha! No way!"
scene ep10_freeroam_bbq39 with dissolve
ly "Enjoy! Not more than one each, ok? They're highly potent. If it's your first time, half will probably do."
scene ep10_freeroam_bbq45 with dissolve
rs "Those aren't normal mushrooms, are they?"
scene ep10_freeroam_bbq41 with dissolve
tm "Don't give me that look, I told her to surprise us. I didn't ask her for drugs."
scene ep10_freeroam_bbq46 with dissolve
ni "Those will get you fucked up."
scene ep10_freeroam_bbq41 with dissolve
tm "Come on! Don't say you guys never wanted to try them."
scene ep10_freeroam_bbq46 with dissolve
ni "I mean...weed is one thing, but this is a whole other step."
scene ep10_freeroam_bbq41 with dissolve
tm "I'm not eating one on my own. Someone has to do it with me."
tm "There are plenty of shrooms in this bag... I'm having one. Who else is?"
scene ep10_freeroam_bbq47 with dissolve
tm "Jacob?"
scene ep10_freeroam_bbq48 with dissolve
jac "Uh... Nah. Sorry, bro. Not tonight."
scene ep10_freeroam_bbq43 with dissolve
tm "John Boy! You're having one. Think of the amazing sex you'll have with Elena while tripping."
scene ep10_freeroam_bbq50 with dissolve
jb "I don't think so..."
scene ep10_freeroam_bbq44 with dissolve
tm "This is horse shit."
scene ep10_freeroam_bbq41 with dissolve
tm "Leon. Jamie. You two need it."
scene ep10_freeroam_bbq49 with dissolve
le "Why do we need it?"
scene ep10_freeroam_bbq42 with dissolve
tm "Because you two have been bitching about each other like girls for weeks now, and I'm sick of hearing about it."
tm "Smoke some peace pipe, share a shroom...you know?"
tm "Also, it's DIKs' Thanksgiving, and I would be very thankful if you guys did this."
scene ep10_freeroam_bbq51 with dissolve
$ mc_info = ["{size=-%d}Eat a shroom{/size}" % persistent.scale_factor,"ep10_bbq_shroom_label","{size=-%d}Don't eat a shroom{/size}" % persistent.scale_factor,"ep10_bbq_no_shroom_label","{size=-%d}Discourage use of shrooms{/size}" % persistent.scale_factor,"ep10_bbq_avoid_shroom_label",ep4_smoked_weed]
show screen major_choice_screen
$ renpy.pause()

label ep10_bbq_shroom_label:
$ ep10_shroom_choice = "DIK"
scene ep10_freeroam_bbq52 with dissolve
mc "I'll have one. Come on, guys, this will be fun!"
if branchMayaJosy:
    if ep10_pp_activity == 0:
        scene ep10_freeroam_bbq54 with dissolve
    else:
        scene ep10_freeroam_bbq54b with dissolve
    tm "Fuck you."
    scene ep10_freeroam_bbq53 with dissolve
    mc "I thought you said we should smoke some peace pipe. Was that all talk?"
    if ep10_pp_activity == 0:
        scene ep10_freeroam_bbq55 with dissolve
    else:
        scene ep10_freeroam_bbq55b with dissolve
    tm "See! Even sisterfucker here will have one."
else:
    if ep10_pp_activity == 0:
        scene ep10_freeroam_bbq55 with dissolve
    else:
        scene ep10_freeroam_bbq55b with dissolve
    tm "See! Even [name] will have one."
scene ep10_freeroam_bbq57 with dissolve
jm "Ok, I'll have the smallest one."
scene ep10_freeroam_bbq56 with dissolve
tm "Share one with Leon."
scene ep10_freeroam_bbq46 with dissolve
ni "If you guys are doing it...all right."
$ new_bio("You", "I chose to have a shroom at the DIKs' Thanksgiving, and I may have encouraged others to have one too.")
jump ep10_bbq_shroom_cont_label

label ep10_bbq_no_shroom_label:
$ ep10_shroom_choice = "NEUTRAL"
scene ep10_freeroam_bbq53 with dissolve
mc "I'm not gonna have one."
if branchMayaJosy:
    if ep10_pp_activity == 0:
        scene ep10_freeroam_bbq54 with dissolve
    else:
        scene ep10_freeroam_bbq54b with dissolve
    tm "I didn't ask you. Did I, sisterfucker?"
else:
    if ep10_pp_activity == 0:
        scene ep10_freeroam_bbq55 with dissolve
    else:
        scene ep10_freeroam_bbq55b with dissolve
    tm "I knew you wouldn't. Don't let that stop you, bros."
scene ep10_freeroam_bbq57 with dissolve
jm "Ok, I'll have the smallest one."
scene ep10_freeroam_bbq56 with dissolve
tm "Share one with Leon."
scene ep10_freeroam_bbq46 with dissolve
ni "If you guys are doing it...all right."
$ new_bio("You", "I didn't eat a shroom at the DIKs' Thanksgiving.")
jump ep10_bbq_shroom_cont_label

label ep10_bbq_avoid_shroom_label:
$ ep10_shroom_choice = "CHICK"
scene ep10_freeroam_bbq53 with dissolve
mc "Think twice, guys. Don't feel pressured to take them."
mc "And don't let him guilt-trip you into doing something you don't want to."
if ep10_pp_activity == 0:
    scene ep10_freeroam_bbq54 with dissolve
else:
    scene ep10_freeroam_bbq54b with dissolve
if branchMayaJosy:
    tm "Shut up, sisterfucker!"
else:
    tm "Shut up! No shrooms for you."
scene ep10_freeroam_bbq57 with dissolve
jm "Yeah, I'm with [name] on this one. I'll pass."
scene ep10_freeroam_bbq49 with dissolve
le "Give me a small one."
scene ep10_freeroam_bbq46 with dissolve
ni "If you guys are doing it...all right."
$ new_bio("You", "I didn't eat a shroom at the DIKs' Thanksgiving, and I tried to discourage my brothers from having one, with little success.")
jump ep10_bbq_shroom_cont_label

label ep10_bbq_shroom_cont_label:
scene ep10_freeroam_bbq59 with dissolve
tm "Derek! You're having one, right?"
scene ep10_freeroam_bbq60 with dissolve
de "I feel like I shouldn't...but at the same time..."
de "I kinda want this experience."
scene ep10_freeroam_bbq58 with dissolve
jb "When you put it like that...what the hell."

scene ep10_freeroam_bbq61 with dissolve
tm "That's the spirit! Eat up, bros!"
if ep10_shroom_choice != "CHICK":
    scene ep10_freeroam_bbq63 with dissolve
else:
    scene ep10_freeroam_bbq62 with dissolve
$ renpy.pause()
scene ep10_freeroam_bbq65 with dissolve
$ renpy.pause()

if ep10_shroom_choice == "DIK":
    scene ep10_freeroam_bbq67 with dissolve
    mc "Down the rabbit hole we go."
else:
    scene ep10_freeroam_bbq66 with dissolve
    mc "I guess this means we'll have to look out for you guys tonight."

scene ep10_freeroam_bbq70 with dissolve
jac "Pray for a good trip, dudes."
scene ep10_freeroam_bbq68 with dissolve
rs "You guys are crazy..."
scene ep10_freeroam_bbq73 with dissolve
tm "Wanna hear something else that's crazy?"
tm "Guess which HOT is preggers."
scene ep10_freeroam_bbq75 with dissolve
jm "Someone's pregnant!?"
if ep10_pp_activity == 0:
    scene ep10_freeroam_bbq74 with dissolve
else:
    scene ep10_freeroam_bbq74b with dissolve
tm "Here's a clue..."
tm "It's easy to get pregnant when you're filled to the brim with cum 24/7."
scene ep10_freeroam_bbq71 with dissolve
jac "Arieth's pregnant!?"
scene ep10_freeroam_bbq73 with dissolve
tm "Yes! And she's keeping it."
scene ep10_freeroam_bbq77 with dissolve
ni "No way! Who's the father?"
if ep10_pp_activity == 0:
    scene ep10_freeroam_bbq74 with dissolve
else:
    scene ep10_freeroam_bbq74b with dissolve
tm "Haha, that's the best part! She thinks it's Dawe that knocked her up."
tm "But for all we know, it could be anyone!"
scene ep10_freeroam_bbq71 with dissolve
jac "Did she get pregnant recently?"
scene ep10_freeroam_bbq73 with dissolve
tm "I'm guessing she's a couple of months in or so. That should narrow it down."
scene ep10_freeroam_bbq79 with dissolve
$ renpy.pause()
scene ep10_freeroam_bbq80 with dissolve
le "That doesn't narrow it down, does it?"
le "What if it's mine?"
scene ep10_freeroam_bbq75 with dissolve
jm "It could be mine! I don't want another baby scare!"
scene ep10_freeroam_bbq77 with dissolve
ni "It could be mine too..."
scene ep10_freeroam_bbq73 with dissolve
tm "I'm sure I'm safe. Rusty? You too, right?"
scene ep10_freeroam_bbq69 with dissolve
rs "Yeah. It's definitely not mine."
scene ep10_freeroam_bbq73 with dissolve
tm "Unless she saved our cum in the freezer! Haha!"
scene ep10_freeroam_bbq69 with dissolve
rs "*{i}Shudders{/i}* Don't do that to me."
if ep4_derekFuckedArieth:
    scene ep10_freeroam_bbq81 with dissolve
    jac "Bro... It could be either of us."
    scene ep10_freeroam_bbq82 with dissolve
    de "Hell no! I'm not gonna be a baby-daddy!"
    de "And jokes on you, Jacob! I came in her asshole!"
else:
    scene ep10_freeroam_bbq72 with dissolve
    jac "Fuck... I knew I should have worn a rubber."
scene ep10_freeroam_bbq80 with dissolve
le "Ugh... This is like Russian roulette, but worse."
if ep10_pp_activity == 0:
    scene ep10_freeroam_bbq74 with dissolve
else:
    scene ep10_freeroam_bbq74b with dissolve
tm "Eh. I don't know why you're this upset about it. She claims it's Dawe's kid."
tm "She's delusional. I doubt she'll even do a paternity test."
tm "What this is, is a teaching moment."
scene ep10_freeroam_bbq83 with dissolve
tm "And the lesson is..."
tm "If you have a choice..."
scene ep10_freeroam_bbq84 with dissolve
tm "...always creampie the ass. The asshole is the only hole you can trust."
scene ep10_freeroam_bbq72 with dissolve
jac "What about the mouth?"
scene ep10_freeroam_bbq73 with dissolve
tm "That works too."
tm "See! We're learning!"
scene ep10_freeroam_bbq76 with dissolve
jm "Dany doesn't want it up the ass and said I had to take a dildo up mine to keep it equal."
jm "But I told her having anal sex is already about equality since both men and women have assholes."
jm "She shouldn't have bought that, but she did."
scene ep10_freeroam_bbq85 with dissolve
tm "Hahaha!"
scene ep10_freeroam_bbq87 with dissolve
rs "Is it just me who doesn't like anal sex that much?"
rs "I tried it a few times, but it doesn't do much for me. Sure, it's tight, but I get too hung up on that it's someone's asshole I'm fucking."
scene ep10_freeroam_bbq73 with dissolve
tm "Yes, you're the weird one. Anal sex rocks."
tm "In fact, everything with the asshole does."
scene ep10_freeroam_bbq88 with dissolve
jb "Like what? Rimjobs?"
scene ep10_freeroam_bbq86 with dissolve
tm "Oh, hell yeah! Rimjobs! Give me!"
if ep9_sarah_melanie_lewd:
    scene ep10_freeroam_bbq66 with dissolve
    if ep9_sm_like_rim:
        mc "I've tried getting rimmed, and I kinda liked it."
    else:
        mc "I've tried getting rimmed, but I hated it."
    scene ep10_freeroam_bbq89 with dissolve
    jac "Oh! Are we talking about getting rimmed? I thought Tommy meant to give it."
else:
    scene ep10_freeroam_bbq89 with dissolve
    jac "Wait... Give me? Are we talking about getting rimmed? I thought you meant to give it."
if ep10_pp_activity == 0:
    scene ep10_freeroam_bbq74 with dissolve
else:
    scene ep10_freeroam_bbq74b with dissolve
tm "Give it, get it. It's all good."
scene ep10_freeroam_bbq90 with dissolve
de "Is it nice to get it?"
scene ep10_freeroam_bbq94 with dissolve
tm "You never got it? A warm and wet tongue in your asshole as she reaches around and works your dick... It's the best."
if ep10_pp_meat == 2:
    scene ep10_freeroam_bbq92 with dissolve
    jb "Why did it have to be hot dogs...?"
scene ep10_freeroam_bbq90 with dissolve
de "Do girls like giving it?"
scene ep10_freeroam_bbq89 with dissolve
jac "Hell no. There's no way they like to give rimjobs. Nuh-uh."
scene ep10_freeroam_bbq93 with dissolve
tm "The kinky ones do. Want me to hook you guys up with one?"
scene ep10_freeroam_bbq90 with dissolve
de "I've done a lot of weird things, but that's something that never crossed my mind."
scene ep10_freeroam_bbq93 with dissolve
tm "You should try it. You should totally try it."
scene ep10_freeroam_bbq91 with dissolve
le "Haha, the HOTs would be disgusted if they heard us talking about this."
scene ep10_freeroam_bbq78 with dissolve
ni "Yeah. There's no way girls would ever discuss rimjobs and anal sex over dinner."

scene ep10_freeroam_bbq118 with dissolve
sar "And then he went like this."
scene ep10_freeroam_bbq119 with dissolve
sar "Euuuuwrrahhhhggg."
"*{i}Laughter{/i}*"
scene ep10_freeroam_bbq144 with dissolve
sa "Hahaha! Sarah's in the lead with that one. Hands down the weirdest cum face so far. Who can beat her?"
scene ep10_freeroam_bbq145 with dissolve
el "John Boy usually goes like this."
"*{i}Laughter{/i}*"

scene ep10_freeroam_bbq146 with dissolve
ash "Haha, Anthony looks something like this..."
"*{i}Laughter{/i}*"
scene ep10_freeroam_bbq124 with dissolve
ar "Haha! That's spot on!"
scene ep10_freeroam_bbq147 with dissolve
ash "..."

scene ep10_freeroam_bbq120 with dissolve
ml "I bet Arieth got some good ones."
scene ep10_freeroam_bbq125 with dissolve
ar "Oh, girl. Don't get me started."
show ep10_freeroam_bbq126
if not persistent.ep10_cardzo18:
    show screen ep10_render_screen("zo18")
with dissolve
ar "Dawe goes like this!"
show ep10_freeroam_bbq127 with dissolve
$ renpy.pause()
show ep10_freeroam_bbq128
if not persistent.ep10_cardzo18:
    hide screen ep10_render_screen
    show screen ep10_render_screen("zo18b")
with dissolve
ar "Jacob goes like this!"
show ep10_freeroam_bbq148
hide screen ep10_render_screen
with dissolve
ar "This is John!"
ar "This is Alex!"
ar "This is Jack!"
ar "Rob goes like this!"
scene ep10_freeroam_bbq129 with dissolve
ar "Tommy goes like this."
scene ep10_freeroam_bbq152 with dissolve
he "Hey!"
scene ep10_freeroam_bbq130 with dissolve
ar "Oh, did I do it wrong?"
scene ep10_freeroam_bbq133 with dissolve
sa "Uh... Haha... Maybe that's it for funny cum faces?"
scene ep10_freeroam_bbq118 with dissolve
sar "Yeah, let's settle for agreeing that they all look ugly when they cum."
scene ep10_freeroam_bbq134 with dissolve
sa "And with those words, I'd like to shift the topic to why we're here tonight."
sa "And raise my cup and say welcome back to the sisterhood, Maya. We've missed you."
scene ep10_freeroam_bbq149 with dissolve
"*{i}Applause{/i}*"
scene ep10_freeroam_bbq150 with dissolve
my "Thanks, everyone."
my "Um... I'm sorry for going back and forth on this. I've been dealing with some personal stuff lately."
my "But let me just say that I'm happy to be back."
scene ep10_freeroam_bbq151 with dissolve
my "During these last weeks, I've gotten closer to some of you and I hope that I can continue to grow friendships with the rest of you as well."
my "So... Thank you. And to the HOTs!"

scene ep10_freeroam_bbq95 with dissolve
rs "But why did you go to a yoga class?"
scene ep10_freeroam_bbq96 with dissolve
if branchJill:
    mc "I went with Jill for one."
    if ep10_pp_activity == 0:
        scene ep10_freeroam_bbq97 with dissolve
    else:
        scene ep10_freeroam_bbq97b with dissolve
    tm "Whipped!"
    if ep10_pp_activity == 0:
        scene ep10_freeroam_bbq98 with dissolve
    else:
        scene ep10_freeroam_bbq98b with dissolve
    mc "Is it whipped to do stuff that your girlfriend likes? Get out of here."
else:
    mc "Because my friends wanted me to come."
scene ep10_freeroam_bbq99 with dissolve
le "But it's yoga... That's for chicks. Isn't that like stretching in weird positions and shit?"
le "That's not exercise."
scene ep10_freeroam_bbq100 with dissolve
mc "Yes, and no. It's different from what I usually do and, honestly, it's not for me."
mc "But it's not all bad."
scene ep10_freeroam_bbq101 with dissolve
jac "You wouldn't catch me dead at one of those classes, is all I'm saying."
scene ep10_freeroam_bbq96 with dissolve
if affinity == "DIK":
    mc "Yeah? Well, I was at the back of the class, right?"
    mc "And if you've ever seen a girl in yoga pants, you'd be amazed to see a bunch of them in front of you."
else:
    mc "That's your call. The only upside to it, I guess, is that there are a lot of girls there."
    scene ep10_freeroam_bbq101 with dissolve
    jac "In yoga pants?"
    scene ep10_freeroam_bbq96 with dissolve
    mc "Yeah. I was at the back of the class and they all had some nice outfits."
scene ep10_freeroam_bbq100 with dissolve
le "..."
scene ep10_freeroam_bbq99 with dissolve
le "Do they bend over in front of you?"
scene ep10_freeroam_bbq100 with dissolve
mc "Yeah, that's pretty much yoga."
scene ep10_freeroam_bbq104 with dissolve
jm "And your face is like...right there... Near their asses?"
scene ep10_freeroam_bbq105 with dissolve
mc "Well, yeah. Kinda."
scene ep10_freeroam_bbq99 with dissolve
le "That sounds hot..."
scene ep10_freeroam_bbq102 with dissolve
jac "Dude, why are you rocking back and forth like that?"
scene ep10_freeroam_bbq103 with dissolve
le "I don't know. Am I?"
scene ep10_freeroam_bbq102 with dissolve
jac "Ah... It's the mushrooms... They're kicking in, huh?"
scene anim_derek_trip_ep10 with dissolve
jac "Derek? You've been silent. Are you ok?"
de "Yeah, yeah. I'm fine. I'm doing great."
$ mphone_music_genre = 2
$ mphone_play_songs(["music/ep10/licensed_music/track134.mp3", "music/ep10/licensed_music/track147.mp3"])
scene ep10_freeroam_bbq106 with dissolve
mc "Are you sure? You look pale."
scene ep10_freeroam_bbq107 with dissolve
rs "Want something to drink?"
scene ep10_freeroam_bbq106 with dissolve
mc "I'll get you some water, bro."
scene ep10_freeroam_bbq108 with dissolve
ni "Bro, I don't wanna alarm you..."
if ep10_shroom_choice == "CHICK":
    stop music fadeout 3
ni "But you have a huge erection."

if ep10_shroom_choice == "DIK":
    scene ep10_freeroam_bbq112 with dissolve
    mc "Whoa..."
    scene ep10_freeroam_bbq113 with dissolve
    mc "What's up with my shoes? They're so...light."
    scene ep10_freeroam_bbq114 with dissolve
    mc "WOW! I can jump so fucking high, guys!"
    scene ep10_freeroam_bbq115 with dissolve
    mc "Over the tree tops!"

if ep10_shroom_choice != "CHICK":
    scene ep10_freeroam_bbq109 with vpunch
    jm "AHHH!!!"
    jb "What's wrong?"
    jm "What is that thing!?"
    scene ep10_freeroam_bbq110 with dissolve
    jb "It's a potato."
    scene ep10_freeroam_bbq111 with vpunch
    jm "AHHHH!!!"
    if ep10_shroom_choice != "DIK":
        stop music fadeout 3
    jb "AHH!!!"

if ep10_shroom_choice != "DIK":
    $ mphone_play_songs(["music/ep10/licensed_music/track147.mp3"])

jump ep10_freeroam_bbq_label

label ep10_bbq_bella_event_label:
stop music fadeout 3
scene ep10_bbq_bella_event1 with dissolve
$ renpy.pause()
play music "music/ep9/relaxed.mp3"
play sound "sound_effects/cellphone.mp3"
if ep10_shroom_choice == "DIK":
    scene ep10_bbq_bella_event2 with dissolve
    mc "Huh? This conch is playing a beautiful melody."
    scene ep10_bbq_bella_event3 with dissolve
    mc "Hello?"
    scene ep10_bbq_bella_event5 with dissolve
    isa "[name], it's me. I don't want to interrupt your party. Are you free to talk?"
    scene ep10_bbq_bella_event4 with dissolve
    mc "*{i}Mumbles{/i}* The mermaid is calling my name."
    scene ep10_bbq_bella_event6 with dissolve
    mc "Yes, what do you want, oh beautiful creature?"
    scene ep10_bbq_bella_event7 with dissolve
    $ renpy.pause()
    scene ep10_bbq_bella_event8 with dissolve
    isa "How much did you have to drink?"
    scene ep10_bbq_bella_event7 with dissolve
    mc "All the nectar of the ocean."
    scene ep10_bbq_bella_event8 with dissolve
    isa "Ok. I doubt you will remember this by tomorrow, from the sound of it."
    scene ep10_bbq_bella_event9 with dissolve
    mc "No. I'm listening."
    scene ep10_bbq_bella_event10 with dissolve
    isa "I've thought about Thanksgiving and all."
    isa "Jill and I have spent the last few Thanksgivings together. And now she has expressed that she wants to try to talk again."
    isa "But we're both feeling lost about what to do tomorrow and know you guys might need our help. I suggested that we get together and help in the ways we can at my place."
    isa "I hope that's ok with you."
    scene ep10_bbq_bella_event9 with dissolve
    mc "Can you teach me how to sing like you?"
    scene ep10_bbq_bella_event11 with dissolve
    isa "Aaaand I'm calling you tomorrow with this information instead."
    isa "[name]. Don't drink too much tonight. Ok? Take care of yourself."
    scene ep10_bbq_bella_event9 with dissolve
    mc "Yes."
    scene ep10_bbq_bella_event10 with dissolve
    isa "Bye."
    stop music fadeout 3
    scene ep10_bbq_bella_event9 with dissolve
    mc "Farewell, my beautiful mermaid."
else:
    scene ep10_bbq_bella_event12 with dissolve
    "*{i}Cellphone rings{/i}*"
    scene ep10_bbq_bella_event13 with dissolve
    isa "[name], it's me. I don't want to interrupt your party. Are you free to talk?"
    scene ep10_bbq_bella_event14 with dissolve
    mc "I'm free. I'm actually taking a break from it. I wandered down to the jetty by the nearby lake."
    mc "I wish you were here with me."
    scene ep10_bbq_bella_event13 with dissolve
    isa "That sounds peaceful. And you lucked out with the weather tonight, too."
    scene ep10_bbq_bella_event14 with dissolve
    mc "We sure did. It's cold, but the fire keeps everyone warm."
    scene ep10_bbq_bella_event13 with dissolve
    isa "Are you still planning on spending the night in a tent?"
    scene ep10_bbq_bella_event15 with dissolve
    mc "Honestly, no. But I put it up and everything."
    mc "I'd rather spend the night in your bed."
    scene ep10_bbq_bella_event16 with dissolve
    isa "Me too."
    scene ep10_bbq_bella_event15 with dissolve
    mc "Did you want something?"
    scene ep10_bbq_bella_event16 with dissolve
    isa "Yes. I've thought about Thanksgiving and all."
    isa "Jill and I have spent the last few Thanksgivings together. And now she has expressed that she wants to try to talk again."
    isa "But we're both feeling lost about what to do tomorrow and know you guys might need our help. I suggested that we get together and help in the ways we can at my place."
    scene ep10_bbq_bella_event17 with dissolve
    isa "I hope that it doesn't make it feel weird for you somehow."
    scene ep10_bbq_bella_event14 with dissolve
    mc "No, I think that sounds great. Jill mentioned she wanted to give you two another try and I'm all for it."
    mc "And I know Maya will be thankful for any extra help she can get tomorrow."
    scene ep10_bbq_bella_event16 with dissolve
    isa "I'll be there for you."
    isa "[name]. Don't drink too much tonight. Ok? Take care of yourself."
    scene ep10_bbq_bella_event15 with dissolve
    mc "Don't worry about me."
    scene ep10_bbq_bella_event13 with dissolve
    isa "Talk to you tomorrow."
    stop music fadeout 3
    scene ep10_bbq_bella_event14 with dissolve
    mc "Good night, Bella."

$ new_chat_msg("Isabella",True,3)
$ mgallery_add_photo("chat_bella_pic1_ep10_zoomed")
$ task_list[0] = ""
$ updateTaskList()
$ mphone_next_song()
jump endEvent

label ep10_bbq_ufo_event_label:
stop music fadeout 3
$ renpy.sound.play("sound_effects/season3/forest_soundscape.mp3", channel="sfx3", loop=True)
$ renpy.sound.play("sound_effects/season3/tractor_beam1.mp3", channel="sfx2", loop=True)
scene ep10_bbq_ufo_event1 with dissolve
mc "What is that bright light?"
scene ep10_bbq_ufo_event2 with dissolve
$ renpy.pause()
scene ep10_bbq_ufo_event3 with dissolve
"STEP INTO THE LIGHT, CHILD."
scene ep10_bbq_ufo_event4 with dissolve
mc "I can see clearly now."
play sound "sound_effects/season3/tractor_beam2.mp3"
scene bg anim_tractor_beam_ep10 movie with dissolve
mc "Whoa! I'm floating!"
pause
$ renpy.music.stop(channel="sfx3", fadeout=3)
$ renpy.music.stop(channel="sfx2", fadeout=3)
scene ep10_bbq_ufo_event9 with dissolve
$ renpy.sound.play("sound_effects/season3/ship1.mp3", channel="sfx1", loop=True)
mc "No anal probe! Please! No anal probe!"
scene ep10_bbq_ufo_event10 with dissolve
"ACCEPT! THE CANDY!"
scene ep10_bbq_ufo_event11 with dissolve
mc "Candy? What about the anal probe?"
mc "Oh my God! Are you gonna shove candy up my asshole?"
scene ep10_bbq_ufo_event12 with dissolve
"..."
$ renpy.music.stop(channel="sfx1", fadeout=0)
$ renpy.sound.play("sound_effects/season3/forest_soundscape.mp3", channel="sfx3", loop=True)
scene ep10_bbq_ufo_event5
$ renpy.pause()
scene ep10_bbq_ufo_event6 with dissolve
mc "Aliens! Come back! Give me more candy!"
scene ep10_bbq_ufo_event7 with dissolve
mc "ALIENS!"
scene ep10_bbq_ufo_event8 with dissolve
$ renpy.music.stop(channel="sfx3", fadeout=3)
mc "They exist."
$ mphone_next_song()
jump endEvent

label ep10_bbq_dc_event_label:
scene ep10_bbq_dc_event1 with dissolve
de "Let me sink this one. It's all I need!"
scene ep10_bbq_dc_event15 with dissolve
cam "You're gonna miss it! Just like all other shots before it."
scene ep10_bbq_dc_event1 with dissolve
de "But not this one."
if ep10_shroom_choice == "DIK":
    scene ep10_bbq_dc_event3 with dissolve
    mc "GOOD LUCK, DEREK!"
else:
    scene ep10_bbq_dc_event2 with dissolve
    mc "Good luck, Derek. You can do it."
scene ep10_bbq_dc_event4 with dissolve
de "I don't need luck, [mc_de]. I need skill."
play sound "sound_effects/season3/ping_pong_bounce.mp3"
scene ep10_bbq_dc_event16 with vpunch
cam "Missed it!"
scene ep10_bbq_dc_event5 with dissolve
de "[name] shook the table."
scene ep10_bbq_dc_event6 with dissolve
mc "I did not."
scene ep10_bbq_dc_event7 with dissolve
de "You did! How am I supposed to hit the cup when you do?"
de "It's like playing Jenga with a Parkinson's patient."
play sound "sound_effects/season3/ping_pong_splash.mp3"
scene ep10_bbq_dc_event9 with vpunch
"*{i}Splash{/i}*"
scene ep10_bbq_dc_event17 with dissolve
cam "I win! Haha! Lose the underwear!"
scene ep10_bbq_dc_event8 with dissolve
de "..."
scene anim_derek_fluff_ep10 with dissolve
cam "Um... What are you doing?"
de "It's cold outside. If I'm showing everyone it, it needs some fluffing."
scene ep10_bbq_dc_event18 with dissolve
cam "You know what? Don't show it. Let's call it a draw."
scene ep10_bbq_dc_event19 with dissolve
cam "[name]? Do you want to get your ass beaten?"
scene ep10_bbq_dc_event20 with dissolve
menu:
    "Play Beer Pong with her":
        $ renpy.pause(0.5)
    "Don't play":
        if ep10_shroom_choice == "DIK":
            mc "I AM NEEDED ELSEWHERE!"
        else:
            mc "Not now. I'll let you keep your clothes this time."
        $ task_list[11] = ""
        if branchIsabella:
            $ event_list.append("ep10_bbq_final_phase")
        if ep10_riona_date:
            if "ep10_bbq_rio_event_label" not in event_list:
                $ event_list.append("ep10_bbq_rio_event_label")
                if ep10_shroom_choice == "DIK":
                    $ task_list[1] = "Find the shapeshifter"
                else:
                    $ task_list[1] = "Find Riona"
        if branchJill and ep10_shroom_choice == "DIK":
            $ event_list.append("ep10_bbq_guitar_high_event_label")
            $ task_list[6] = "Play the Bard's song"
        $ updateTaskList()
        jump endEvent

if ep10_shroom_choice == "DIK":
    mc "Yes."
else:
    if affinity == "DIK":
        mc "You can spank me any day, Cammy."
        mc "Oh, you meant at Beer Pong?"
    else:
        mc "By you? Are you sure you want to lose your clothes? Like Derek said, it's cold outside."
scene ep10_bbq_dc_event21 with dissolve
cam "Standard rules. Loser strips all the way."
scene ep10_bbq_dc_event22 with dissolve
ri "Haha, you're playing with fire. You got lucky against Derek, but you might end up butt naked playing against [name]."
if ep10_shroom_choice == "DIK":
    scene ep10_bbq_dc_event10 with dissolve
    cam "Call me crazy, but I think I won't."
    scene ep10_bbq_dc_event11 with dissolve
    isa "What's the matter, [name]? Never saw a sexy ping pong ball before?"
    scene ep10_bbq_dc_event10 with dissolve
    mc "Balla?"
else:
    scene ep10_bbq_dc_event23 with dissolve
    cam "If there's anyone who will be butt naked by the end of this game, it's him."

scene ep10_bbq_dc_event24 with dissolve
cam "All right, [name]. Show me what you got."
if ep10_shroom_choice == "DIK":
    scene ep10_bbq_dc_event12 with dissolve
    $ renpy.pause()
    play sound "sound_effects/season3/ping_pong_bounce.mp3"
    scene ep10_bbq_dc_event25 with hpunch
    "*{i}Laughter{/i}*"
    cam "Wrong cups, [name]."
    scene bp_camila_off_6_ep10 with dissolve
    $ renpy.pause()
    play sound "sound_effects/season3/ping_pong_splash.mp3"
    scene ep10_bbq_dc_event31 with vpunch
    "*{i}Splash{/i}*"
    cam "Woho! Time to drink, [name]!"
    scene ep10_bbq_dc_event26 with dissolve
    ri "Ok, I take it back. My money's on you."
    play sound "sound_effects/season3/ping_pong_bounce.mp3"
    scene ep10_bbq_dc_event27 with hpunch
    cam "No shit?"
    scene ep10_bbq_dc_event13 with wipeleft
    cam "Move that cup! Move that cup!"
    scene ep10_bbq_dc_event28 with dissolve
    ri "Hahaha! This is mean and funny at the same time!"
    scene ep10_bbq_dc_event14 with dissolve
    cam "Yay!!!"
    if not ep7_becky_lewd:
        bc "It is him..."
    scene ep10_bbq_dc_event29 with dissolve
    cam "Hahaha! Thank you! I win!"
    cam "That was so weak."
    scene ep10_bbq_dc_event30 with dissolve
    cam "By the way, this is what you missed out on. Haha!"
    $ new_bio("Camila", "I played Beer Pong with her but ended up losing. At least that's what people tell me. I don't even remember it.")
else:
    hide screen new_phone_screen
    if minigames and not bp_tut_ep10_seen and (tutorials or not persistent.bp_tutorial):
        menu:
            "Watch tutorial":
                $ bp_tut_ep10_seen = True
                $ bp_dlg = 0
                $ bp_jump_label = "ep10_bp_match_camila_label"
                show screen bp_tut_screen
                pause
                $ persistent.bp_tutorial = True
            "Skip tutorial":
                $ renpy.pause(0.5)

    label ep10_bp_match_camila_label:
    hide screen new_phone_screen
    $ renpy.block_rollback()
    $ bp_init_game("Camila","ep10", "ep10_after_bp_camila_label")
    if minigames:
        show screen bp_screen
    else:
        show screen bp_screen_nm
    pause

    label ep10_after_bp_camila_label:
    show screen new_phone_screen
    if bp_player_won:
        $ ep10_bp_won_camila = True
        if minigames:
            scene ep10_bbq_dc_event32
            hide screen bp_screen
            with dissolve
        else:
            scene ep10_bbq_dc_event32
            hide screen bp_screen_nm
            with dissolve
        cam "No!!! I can't believe I lost."
        scene ep10_bbq_dc_event34 with dissolve
        ri "Haha! You only have yourself to blame."
        scene ep10_bbq_dc_event32 with dissolve
        cam "Do I have to remove my panties now?"
        scene ep10_bbq_dc_event34 with dissolve
        ri "You knew the rules when you challenged him."
        scene ep10_bbq_dc_event35 with dissolve
        cam "Whose side are you on?"
        scene ep10_bbq_dc_event33 with dissolve
        
        if persistent.mod_wt_enabled: 
                    $mod_choices = ["(-Sage)","(+Josy)","(-DIK)","(+DIK)","(-Maya)","(-Josy)","","","","","","" ]
                    #[m_c1][mod_choices[0]]
                    if not branchAlone:
                        $mod_choices[6]="(+Cheater)"
                        
                    if branchAlone and wt_ep9_branch_numbers != 1:
                        $mod_choices[6]="(+Cheater)"
        menu:
            "Show me the goods [m_c1][mod_choices[3]][m_c2][mod_choices[6]]":
                $ dk(2)
                if not branchAlone:
                    $ tc += 1
                if branchAlone and wt_ep9_branch_numbers != 1:
                    $ tc += 1
                mc "Rules are rules, Cammy. I doubt you'd spare me if you won."
                scene ep10_bbq_dc_event32 with dissolve
                cam "Haha! Fine! Take a look because I won't keep them off for long."
                scene ep10_bbq_dc_event38 with dissolve
                $ renpy.pause()
                scene ep10_bbq_dc_event39 with dissolve
                $ renpy.pause()
                scene ep10_bbq_dc_event36 with dissolve
                cam "That's all you get."
                scene ep10_bbq_dc_event37 with dissolve
                mc "Nice!"
                $ new_bio("Camila", "I played Beer Pong with her and won! And I made her strip as punishment.")
            "You don't have to strip [m_c1][mod_choices[2]]":
                $ dk(-2)
                mc "It's fine, Cammy. You don't have to remove them."
                scene ep10_bbq_dc_event34 with dissolve
                ri "You're lucky that [name] is a big softie."
                ri "Either that or he doesn't want to see you naked, haha!"
                scene ep10_bbq_dc_event35 with dissolve
                cam "Screw you! Haha!"
                $ new_bio("Camila", "I played Beer Pong with her and won! But I was nice about it, and she didn't have to strip.")
        scene ep10_bbq_dc_event36 with dissolve
        cam "Thanks for the game, [name]. I'll know better before I challenge you next time."
    else:
        if minigames:
            scene ep10_bbq_dc_event13
            hide screen bp_screen
            with dissolve
        else:
            scene ep10_bbq_dc_event13
            hide screen bp_screen_nm
            with dissolve
        cam "I won! Show me what you're hiding!"
        scene ep10_bbq_dc_event14 with dissolve
        mc "Damn it..."
        cam "Wowza! That's what I'm talking about."
        bc "Totally..."
        scene ep10_bbq_dc_event29 with dissolve
        cam "Want a rematch?"
        scene ep10_bbq_dc_event40 with dissolve
        menu:
            "Rematch":
                mc "Yeah, let's do it."
                jump ep10_bp_match_camila_label
            "Eat the loss":
                mc "Nah, I've shown enough skin for tonight."
                $ new_bio("Camila", "I played Beer Pong with her but ended up losing.")

$ task_list[11] = ""
if branchIsabella:
    $ event_list.append("ep10_bbq_final_phase")
if ep10_riona_date:
    if "ep10_bbq_rio_event_label" not in event_list:
        $ event_list.append("ep10_bbq_rio_event_label")
        if ep10_shroom_choice == "DIK":
            $ task_list[1] = "Find the shapeshifter"
        else:
            $ task_list[1] = "Find Riona"
if branchJill and ep10_shroom_choice == "DIK":
    $ event_list.append("ep10_bbq_guitar_high_event_label")
    $ task_list[6] = "Play the Bard's song"
$ updateTaskList()

jump endEvent

label ep10_bbq_guitar_jm_event_label:
scene ep10_bbq_guitar_jm_event1 with dissolve
js "Aw, you brought your guitar..."
scene ep10_bbq_guitar_jm_event2 with dissolve
mc "Isn't that what you should do when there's a bonfire?"
stop music fadeout 3
scene ep10_bbq_guitar_jm_event3 with dissolve
my "I've seen it in movies, but never experienced it in real life."
play music "music/ep10/pineapple_pizza.mp3"
$ renpy.sound.play("sound_effects/season3/bonfire.mp3", channel="sfx2", loop=True)
scene ep10_bbq_guitar_jm_event7 with dissolve
$ renpy.pause(10)
show screen click_to_continue_screen with dissolve
$ renpy.pause(2)
hide screen click_to_continue_screen with dissolve
$ renpy.pause()
scene ep10_bbq_guitar_jm_event4 with dissolve
my "Beautiful. So beautiful."
scene ep10_bbq_guitar_jm_event5 with dissolve
js "Yeah, I loved that."
js "This party was such a great idea."
scene ep10_bbq_guitar_jm_event2 with dissolve
mc "Yeah, I'm happy with it. I enjoy planning parties."
stop music fadeout 3
$ renpy.music.stop(channel="sfx2", fadeout=3)
mc "It's challenging but also rewarding seeing people enjoy themselves."
scene ep10_bbq_guitar_jm_event6 with dissolve
$ renpy.pause()
$ mphone_next_song()
$ optional_task_list[0] = ""

if branchMayaJosy and "ep10_bbq_guitar_jm_event_label" in event_list:
    $ optional_task_list[0] = "Play guitar by the fire"
    
if "ep10_bbq_guitar_others_event_label" in event_list and branchAlone:
    $ optional_task_list[0] = "Play guitar by the fire"
    
if branchSage and "ep10_bbq_guitar_s_event_label" in event_list:
   $ optional_task_list[0] = "Play guitar by the fire"


$ updateTaskList()
jump endEvent

label ep10_bbq_guitar_s_event_label:
$ renpy.sound.play("sound_effects/season3/bonfire.mp3", channel="sfx2", loop=True)
scene ep10_bbq_guitar_s_event1 with dissolve
sa "Ooh la la. Look at you."
mc "What?"
scene ep10_bbq_guitar_s_event2 with dissolve
sa "I see what you're doing. Who are you looking to impress with your guitar?"
scene ep10_bbq_guitar_s_event3 with dissolve
mc "You, of course."
if "ep10_bbq_s_event_label" in event_list:
    scene ep10_bbq_guitar_s_event4 with dissolve
    sa "You've already got me, though."
    scene ep10_bbq_guitar_s_event5 with dissolve
    stop music fadeout 3
    sa "I mean, you haven't got me, but- You... Shut up and play something."
else:
    scene ep10_bbq_guitar_s_event4 with dissolve
    stop music fadeout 3
    sa "I see. Go ahead and impress me then."
play music "music/ep10/pineapple_pizza.mp3"
scene ep10_bbq_guitar_s_event13 with dissolve
$ renpy.pause(10)
show screen click_to_continue_screen with dissolve
$ renpy.pause(2)
hide screen click_to_continue_screen with dissolve
$ renpy.pause()
scene ep10_bbq_guitar_s_event6 with dissolve
sa "Ok, I gotta say that you're nailing the ambiance with it."
scene ep10_bbq_guitar_s_event7 with dissolve
mc "Yeah. I felt so too. Party music is great, but I wanted to play something like this for everyone. That's why I brought the guitar."
scene ep10_bbq_guitar_s_event6 with dissolve
sa "Looking around I see a lot of people who seem to be enjoying themselves..."
scene ep10_bbq_guitar_s_event8 with dissolve
sa "And Derek, who's trying to have sex with a tree for an unknown reason."
scene ep10_bbq_guitar_s_event12 with dissolve
de "NO! I don't care what you think. We're in love!"
scene ep10_bbq_guitar_s_event6 with dissolve
sa "That aside, this is a nice moment."
scene ep10_bbq_guitar_s_event9 with dissolve
$ renpy.pause()
stop music fadeout 3
$ renpy.music.stop(channel="sfx2", fadeout=3)
scene ep10_bbq_guitar_s_event10 with dissolve
sa "*{i}Smack{/i}*"
scene ep10_bbq_guitar_s_event11 with dissolve
$ renpy.pause()
$ mphone_next_song()
$ optional_task_list[0] = ""

if branchMayaJosy and "ep10_bbq_guitar_jm_event_label" in event_list:
    $ optional_task_list[0] = "Play guitar by the fire"
    
if "ep10_bbq_guitar_others_event_label" in event_list and branchAlone:
    $ optional_task_list[0] = "Play guitar by the fire"
    
if branchSage and "ep10_bbq_guitar_s_event_label" in event_list:
   $ optional_task_list[0] = "Play guitar by the fire"
$ updateTaskList()
jump endEvent

label ep10_bbq_guitar_j_event_label:
play music "music/ep10/pineapple_pizza.mp3"
$ renpy.sound.play("sound_effects/season3/bonfire.mp3", channel="sfx2", loop=True)
scene ep10_bbq_guitar_j_event1 with dissolve
$ renpy.pause()
scene ep10_bbq_guitar_j_event2 with dissolve
$ renpy.pause(10)
show screen click_to_continue_screen with dissolve
$ renpy.pause(2)
hide screen click_to_continue_screen with dissolve
$ renpy.pause()
scene ep10_bbq_guitar_j_event3 with dissolve
ji "There you are."
scene ep10_bbq_guitar_j_event4 with dissolve
ji "I've been trying to reach you, but you didn't answer your phone."
scene ep10_bbq_guitar_j_event5 with dissolve
mc "Oh? Sorry, it's been pretty loud out here. I didn't hear it ring."
scene ep10_bbq_guitar_j_event4 with dissolve
ji "It's fine. It was easy to find you. Like you said, it's loud. I could hear you before I even entered the forest."
ji "Are you having fun?"
scene ep10_bbq_guitar_j_event5 with dissolve
mc "Yeah, I think most are."
mc "Some have a bit more fun than others."
scene ep10_bbq_guitar_j_event4 with dissolve
ji "Oh? Are they too drunk already?"
scene ep10_bbq_guitar_j_event5 with dissolve
mc "Well, some of the DIKs ate funny mushrooms. So, if you see them doing weird stuff, that's why."
scene ep10_bbq_guitar_j_event6 with dissolve
ji "They're on drugs?"
scene ep10_bbq_guitar_j_event7 with dissolve
mc "Yeah. I think it's harmless, but I'm keeping an eye out for them."
scene ep10_bbq_guitar_j_event6 with dissolve
ji "Harmless? I don't think so, but it's good that you're looking after them..."
ji "I wasn't aware that you guys did that."
scene ep10_bbq_guitar_j_event7 with dissolve
mc "It's not something they brag about, since it's drugs."
mc "But yeah, it happens. It's usually just weed, but tonight Lily brought us some mushrooms."
scene ep10_bbq_guitar_j_event6 with dissolve
ji "You don't do drugs, right?"
scene ep10_bbq_guitar_j_event7 with dissolve
if ep4_smoked_weed:
    mc "I've tried weed, but I didn't eat any mushrooms."
    scene ep10_bbq_guitar_j_event8 with dissolve
    ji "Oh... You should be careful with that."
    scene ep10_bbq_guitar_j_event7 with dissolve
    mc "Tommy says alcohol is much more dangerous than weed."
    scene ep10_bbq_guitar_j_event8 with dissolve
    ji "*{i}Sigh{/i}*"
else:
    mc "No. Never. It's not for me."
    scene ep10_bbq_guitar_j_event4 with dissolve
    ji "That's good..."

scene ep10_bbq_guitar_j_event9 with dissolve
mc "How are you tonight?"
scene ep10_bbq_guitar_j_event10 with dissolve
ji "I'm fine."

label ep10_bbq_guitar_j_event2_label:
if ep10_shroom_choice == "DIK":
    scene ep10_bbq_guitar_j_event3b with dissolve
    ji "There you are. I've been trying to reach you, but you didn't answer your phone."
    scene ep10_bbq_guitar_j_event3c with dissolve
    mc "Jill..."
    mc "Is it really you?"
    scene ep10_bbq_guitar_j_event31 with dissolve
    ji "It's me."
    ji "How are you? You look a little bit...weird."
    scene ep10_bbq_guitar_j_event32 with dissolve
    mc "I'm totally fine now that you're here."
    scene ep10_bbq_guitar_j_event33 with dissolve
    ji "Ok, you're drunk. Haha."
    ji "It seems like many already are. Are you guys having fun?"
    scene ep10_bbq_guitar_j_event32 with dissolve
    mc "It's fun. It's scary. And pretty sexy. It's a bit of everything."
    mc "But enough about that."
    scene ep10_bbq_guitar_j_event34 with dissolve
    mc "How are {b}you{/b}?"
    scene ep10_bbq_guitar_j_event10 with dissolve
    ji "Haha, I'm fine."

scene ep10_bbq_guitar_j_event11 with dissolve
ji "Oh! No. I'm not fine, I'm both better than fine and at the same time way worse."
scene ep10_bbq_guitar_j_event12 with dissolve
mc "Good and bad news?"
scene ep10_bbq_guitar_j_event13 with dissolve
ji "You can say that. So, I got mad at Tybalt again and went down to the bar to get some space."
ji "And I ran into Trent."
scene ep10_bbq_guitar_j_event12 with dissolve
mc "I don't know who that is."
scene ep10_bbq_guitar_j_event13 with dissolve
ji "He's one of Tybalt's closest friends. I'm sure you've seen him."
ji "Anyway, I recalled something that Tybalt told me, back when he blamed you for causing a fire in our mansion."
ji "It involved Trent, and it wasn't flattering, so I asked him about it."
scene ep10_bbq_guitar_j_event14 with dissolve
ji "It turns out, Tybalt was lying once again and used Trent in his lies. Trent didn't like that very much."
ji "So, we went upstairs to Tybalt's room to have a chat and the next 20 seconds I would like to have erased from my memory."
scene ep10_bbq_guitar_j_event12 with dissolve
mc "What happened?"
scene ep10_bbq_guitar_j_event14 with dissolve
ji "Tybalt and his {i}teeny-tiny Tybbie{/i} were having intercourse with a fruit I'll never be able to enjoy again."
scene ep10_bbq_guitar_j_event13 with dissolve
ji "And, oh, my stolen underwear - for one - was decorating said fruit."
ji "The underwear you told me he stole. You were right. You were absolutely right."
scene ep10_bbq_guitar_j_event12 with dissolve
mc "That's so fucking creepy..."
scene ep10_bbq_guitar_j_event13 with dissolve
ji "It is."
scene ep10_bbq_guitar_j_event12 with dissolve
mc "What did you guys do?"
scene ep10_bbq_guitar_j_event14 with dissolve
ji "I kicked him between his legs."
scene ep10_bbq_guitar_j_event15 with dissolve
mc "Haha! Wait! You what?"
scene ep10_bbq_guitar_j_event16 with dissolve
ji "It was an impulse. I was so mad! All the lies and then he's doing that from across the hall."
ji "I felt so disgusted and humiliated!"
scene ep10_bbq_guitar_j_event17 with dissolve
ji "I left and he had a heated argument with Trent."
ji "After which Trent came to me and told me he's on my side, if we bring this up to the disciplinary committee."
scene ep10_bbq_guitar_j_event18 with dissolve
mc "What would happen if you did that?"
scene ep10_bbq_guitar_j_event17 with dissolve
ji "Tybalt would likely be removed as President. His entire world would shatter."
scene ep10_bbq_guitar_j_event18 with dissolve
menu:
    "You should do it":
        $ ep10_tybalt_mercy = False
        mc "Oh, hell yes! Do that. Let's get rid of him."
        scene ep10_bbq_guitar_j_event17 with dissolve
        ji "It is tempting, but I don't want to ruin him. I just want him to leave me alone and stop trying to provoke me."
        $ new_bio("Jill", "I encouraged Jill to report Tybalt to the disciplinary committee.")
    "Show him some mercy":
        $ ep10_tybalt_mercy = True
        if ep10_shroom_choice == "DIK":
            mc "Whoa... I wouldn't want my world to shatter. Into like a million pieces..."
            mc "Don't do it, Jill. Show him mercy."
        else:
            mc "I don't like the guy and he's a fucking creep for doing that, on top of everything else he does..."
            mc "...but you should show him some mercy. Don't you think?"
        mc "You're better than him."
        scene ep10_bbq_guitar_j_event17 with dissolve
        ji "That's what I'm leaning toward. I don't want to ruin him. I just want him to leave me alone and stop trying to provoke me."
        $ new_bio("Jill", "I asked Jill to show Tybalt some mercy. Yes, he did a horrible thing, but ruining his life over it is a bit over the top.")
ji "Trent told me Tybalt's feeling upset about what happened, so I think it will have an effect without me telling the committee about it."
ji "But we'll see... I haven't ruled it out yet, and I don't want to talk to him about it because I'm still mad."
scene ep10_bbq_guitar_j_event18 with dissolve
mc "Are you afraid you will kick him in the balls again?"
scene ep10_bbq_guitar_j_event19 with dissolve
ji "Hahaha! Yes!"
scene ep10_bbq_guitar_j_event20 with dissolve
ji "I was wearing pointy heels. And I must have hit him with the tip of my toes because he screamed and cried so loud."
scene ep10_bbq_guitar_j_event21 with dissolve
mc "Ouch! Getting kicked in the balls hurts like hell."
scene ep10_bbq_guitar_j_event20 with dissolve
ji "Yeah, I know. It's not the first time I've done it to someone."
scene ep10_bbq_guitar_j_event21 with dissolve
mc "You've done it before?"
scene ep10_bbq_guitar_j_event20 with dissolve
ji "When I was a kid, my sister told me it was a good way to do it to defend myself."
scene ep10_bbq_guitar_j_event21 with dissolve
mc "Jill, you can't go around kicking guys in their balls."
if ep10_shroom_choice == "DIK":
    mc "Even though it does sound kinda fun..."
scene ep10_bbq_guitar_j_event19 with dissolve
ji "Haha! That's so not what I'm doing."
scene ep10_bbq_guitar_j_event21 with dissolve
mc "Jill the Ball Kicker."
scene ep10_bbq_guitar_j_event19 with dissolve
ji "Stop it."
scene ep10_bbq_guitar_j_event21 with dissolve
mc "Please, don't ever do that to me."
scene ep10_bbq_guitar_j_event20 with dissolve
ji "I would never."
scene ep10_bbq_guitar_j_event22 with dissolve
sa "Jill! I thought that was you!"
if ep10_shroom_choice == "DIK":
    scene ep10_bbq_guitar_j_event23b with dissolve
else:
    scene ep10_bbq_guitar_j_event23 with dissolve
ji "Oh, hi!"
scene ep10_bbq_guitar_j_event24 with dissolve
sa "[name], why didn't you tell me she got here?"
if ep10_shroom_choice == "DIK":
    scene ep10_bbq_guitar_j_event26 with dissolve
    mc "Wait a minute! Sage!"
    mc "Did you always have red hair!?"
    scene ep10_bbq_guitar_j_event27 with dissolve
    sa "Jill, I'm gonna steal you from [name] for a bit."
    sa "Come! It's drinks and girl talk time."
    scene ep10_bbq_guitar_j_event28 with dissolve
    mc "It's red like fire!"
    scene ep10_bbq_guitar_j_event29 with dissolve
    sa "Pull yourself together, [name]. Drugs are bad for you, ok?"
    scene ep10_bbq_guitar_j_event30 with dissolve
    ji "Drugs?"
    stop music fadeout 3
    $ renpy.music.stop(channel="sfx2", fadeout=3)
    sa "The boys ate mushrooms. They're out here tripping all over the place."
else:
    scene ep10_bbq_guitar_j_event25 with dissolve
    mc "She just showed up."
    scene ep10_bbq_guitar_j_event24 with dissolve
    sa "Well, I'm stealing her from you for a bit."
    stop music fadeout 3
    $ renpy.music.stop(channel="sfx2", fadeout=3)
    scene ep10_bbq_guitar_j_event27 with dissolve
    sa "Come! It's drinks and girl talk time."

$ task_list[6] = ""
if "jill_block" in event_list:
    $ event_list.remove("jill_block")
    if "ep10_bbq_jsolo_event_label" in event_list:
        if ep10_shroom_choice == "DIK":
            $ task_list[9] = "Talk to the rogue"
        else:
            $ task_list[9] = "Talk to Josy"
            
$ task_list[6] = ""
if branchSage:
    $ event_list.append("ep10_bbq_s_event_label")
    if ep10_shroom_choice == "DIK":
        $ task_list[6] = "Talk to Princess Nadia"
    else:
        $ task_list[6] = "Talk to Sage"
$ updateTaskList()

if "nick_block" in event_list:
    if not "ep10_bbq_jill2_event_label" in event_list:
        $ event_list.append("ep10_bbq_jill2_event_label")
        if ep10_shroom_choice == "DIK":
            $ task_list[3] = "Talk to Rusty"
        else:
            $ task_list[3] = "Talk to Jill"
$ mphone_music_genre = 2
$ mphone_play_songs(["music/ep10/licensed_music/track147.mp3"])
$ updateTaskList()
jump endEvent

label ep10_bbq_guitar_others_event_label:
play music "music/ep10/pineapple_pizza.mp3"
$ renpy.sound.play("sound_effects/season3/bonfire.mp3", channel="sfx2", loop=True)
scene ep10_bbq_guitar_others_event1 with dissolve
$ renpy.pause()
scene ep10_bbq_guitar_others_event2 with dissolve
$ renpy.pause(10)
show screen click_to_continue_screen with dissolve
$ renpy.pause(2)
hide screen click_to_continue_screen with dissolve
$ renpy.pause()
scene ep10_bbq_guitar_others_event3 with dissolve
sy "Your G string is out of tune."
scene ep10_bbq_guitar_others_event4 with dissolve
mc "Yeah, a bit. It's because of the cold."
mc "Do you play guitar?"
scene ep10_bbq_guitar_others_event3 with dissolve
sy "Clarinet. But I have perfect pitch."
scene ep10_bbq_guitar_others_event4 with dissolve
mc "No way! I wish I had it."
scene ep10_bbq_guitar_others_event3 with dissolve
sy "You seem to do fine enough without it."
scene ep10_bbq_guitar_others_event5 with dissolve
bc "[name]. That was like pineapple on pizza."
bc "Amazingly good."
scene ep10_bbq_guitar_others_event6 with dissolve
sar "Just say you wanna sit on his dick already."
stop music fadeout 3
$ renpy.music.stop(channel="sfx2", fadeout=3)
scene ep10_bbq_guitar_others_event7 with dissolve
bc "Shh! Shut up!"
$ optional_task_list[0] = ""

if branchMayaJosy and "ep10_bbq_guitar_jm_event_label" in event_list:
    $ optional_task_list[0] = "Play guitar by the fire"
    
if "ep10_bbq_guitar_others_event_label" in event_list and branchAlone:
    $ optional_task_list[0] = "Play guitar by the fire"
    
if branchSage and "ep10_bbq_guitar_s_event_label" in event_list:
   $ optional_task_list[0] = "Play guitar by the fire"


$ updateTaskList()
$ mphone_music_genre = 2
$ mphone_play_songs(["music/ep10/licensed_music/track147.mp3"])
jump endEvent

label ep10_bbq_guitar_high_event_label:
$ renpy.sound.play("sound_effects/season3/bonfire.mp3", channel="sfx2", loop=True)
scene ep10_bbq_guitar_high_event1 with dissolve
$ renpy.pause()
stop music fadeout 3
scene ep10_bbq_guitar_high_event2 with dissolve
mc "All right! This song goes out to everyone who's feeling lonely tonight."
play music "music/ep10/bonfire_fiasco.mp3"
scene ep10_bbq_guitar_high_event3 with dissolve
$ renpy.pause(10)
show screen click_to_continue_screen with dissolve
$ renpy.pause(2)
hide screen click_to_continue_screen with dissolve
$ renpy.pause()
scene ep10_bbq_guitar_high_event4 with dissolve
mc "DON'T BE LONELY ANYMOOOOORE! WHATEVER THEY SAY, YOU'RE BEAUTIFUL!"
stop music fadeout 3
if not branchJill:
    $ renpy.music.stop(channel="sfx2", fadeout=3)
scene ep10_bbq_guitar_high_event5 with dissolve
jm "*{i}Sobs{/i}*"
$ mphone_music_genre = 2
$ mphone_play_songs(["music/ep10/licensed_music/track147.mp3"])
if not branchJill:
    $ optional_task_list[0] = ""
    $ updateTaskList()
if branchJill:
    jump ep10_bbq_guitar_j_event2_label
jump endEvent

label ep10_bbq_eh_event_label:
scene ep10_bbq_eh_event1 with dissolve
el "Sweetie..."
scene ep10_bbq_eh_event2 with dissolve
he "It's the only thing I can do now. I've thought about it a lot and I don't see another option."
he "I don't think he'll ever change."
scene ep10_bbq_eh_event1 with dissolve
el "I get what you mean. Perhaps he would if you told him that you were uncomfortable with it?"
el "Can't you at least try?"
scene ep10_bbq_eh_event3 with dissolve
he "I could, but I also think it would be good to get some time alone without him. Maybe that will allow me to think clearly."
he "And you know what? This last week, we've barely talked at all. And he doesn't even pick up on the vibes between us."
scene ep10_bbq_eh_event2 with dissolve
he "He's either ignoring them or he's totally oblivious. And I don't know which is worse."
scene ep10_bbq_eh_event1 with dissolve
el "Think about it some more, please? It's a big decision. I don't want you to regret it."
scene ep10_bbq_eh_event2 with dissolve
he "*{i}Sigh{/i}*"

$ optional_task_list[1] = ""
jump endEvent

label ep10_bbq_at_event_label:
scene ep10_bbq_at_event1 with dissolve
ar "And so they divide it into something called trimester. And there are like three of them."
ar "But I guess that depends... If you're having twins or triplets, there may be even more."
scene ep10_bbq_at_event2 with dissolve
ar "And they say that the first trimester is super-important for the kid's development and I think this is where something went wrong with Dawe's penis."
ar "That's why it's super-mega-duper-important for me to only eat big meals during these months."
scene ep10_bbq_at_event5 with dissolve
ar "And if I'm understanding it correctly, I can drink alcohol in the second trimester because it's not as important what you do by then."
scene ep10_bbq_at_event8 with dissolve
el "Arieth... No."
scene ep10_bbq_at_event3 with dissolve
ar "Are you sure?"
scene ep10_bbq_at_event8 with dissolve
el "100%% sure."
scene ep10_bbq_at_event3 with dissolve
ar "God! This is so confusing! I have these weird cravings for things like whiskey and cheese. But it sucks when you can't eat and drink them."
scene ep10_bbq_at_event8 with dissolve
el "You're allowed to eat cheese."
scene ep10_bbq_at_event4 with dissolve
ar "And you're telling me now!?"
ar "What else have I been missing!?"
scene ep10_bbq_at_event2 with dissolve
ar "I'm not even sure what a trimester is. Why don't they call it a semester? That's something I can grasp."
scene ep10_bbq_at_event6 with dissolve
ar "And, this is a sensitive topic, but I'm not sure if I have to start stretching my vagina yet, either."
ar "Have you seen the size of a baby's head?"
scene ep10_bbq_at_event7 with dissolve
ar "They are like this big! And that's not a size I've had before."
scene ep10_bbq_at_event2 with dissolve
ar "I tried to look it up online, but people on the internet are surprisingly mean and unwilling to post helpful answers when I ask about it."
$ optional_task_list[2] = ""
$ updateTaskList()
jump endEvent

label ep10_bbq_rio_event_label:
scene ep10_bbq_rio_event1 with dissolve
ri "[name]? Is that you?"
if ep10_shroom_choice == "DIK":
    scene ep10_bbq_rio_event2 with dissolve
    mc "I think so! Why!?"
    scene ep10_bbq_rio_event3 with dissolve
    ri "Whoa... Calm down, [name]. It's me."
    scene ep10_bbq_rio_event4 with dissolve
    mc "But what about the dinosaurs?"
    scene ep10_bbq_rio_event3 with dissolve
    ri "Maybe you should sit down for a while?"
    scene ep10_bbq_rio_event5 with dissolve
    mc "I think that I'm experiencing something because of the drugs, Rio."
    scene ep10_bbq_rio_event6 with dissolve
    ri "No shit. You should be careful with that."
    scene ep10_bbq_rio_event5 with dissolve
    mc "I shouldn't have eaten that mushroom, Rio. Things are fucking scaring me, right now."
    scene ep10_bbq_rio_event7 with dissolve
    ri "Give it a few more hours and it will wear off."
    scene ep10_bbq_rio_event5 with dissolve
    mc "You've tried it?"
    scene ep10_bbq_rio_event7 with dissolve
    ri "Well, duh. Many times."
    scene ep10_bbq_rio_event5 with dissolve
    mc "I don't see why you would try it more than once. I have all these quests to go on tonight and little time to do them."
    scene ep10_bbq_rio_event7 with dissolve
    ri "Relax. You don't have to do anything tonight. Just sit down on your butt and breathe."
    scene ep10_bbq_rio_event8 with dissolve
    ri "There you go. Think happy thoughts."
    ri "Put that branch away."
    scene ep10_bbq_rio_event9 with dissolve
    mc "But it's got +5 attack damage against trolls."
    scene ep10_bbq_rio_event8 with dissolve
    ri "Put it aside for a moment, [name]. I've got all the spells needed to protect you."
    ri "Remember... Relax... Happy thoughts."
    scene ep10_bbq_rio_event10 with dissolve
    mc "*{i}Deep breaths{/i}*"
    mc "Why are we sitting here?"
    scene ep10_bbq_rio_event11 with dissolve
    ri "I needed a break from people."
    ri "It was too loud and noisy over there."
    scene ep10_bbq_rio_event12 with dissolve
    ri "Maybe it's a stupid question, but are you guys having a good time?"
    scene ep10_bbq_rio_event13 with dissolve
    mc "Huh? Yeah. Yeah. We ate booze and drank some food."
    mc "Then a gnome stole some cheese from us."
    mc "Then we talked about sex and Arieth's pregnancy."
    scene ep10_bbq_rio_event14 with dissolve
    ri "Isn't it crazy? I can't believe she's keeping it. She's gonna have to drop out of college next year."
    scene ep10_bbq_rio_event13 with dissolve
    mc "Yeah. Yeah."
    scene ep10_bbq_rio_event15 with dissolve
    ri "Since when do you have a beard?"
    scene ep10_bbq_rio_event13 with dissolve
    mc "I grow it."
    scene ep10_bbq_rio_event15 with dissolve
    ri "Is this a new style of yours or...?"
    scene ep10_bbq_rio_event13 with dissolve
    mc "No, I just felt that I had to do it..."
    scene ep10_bbq_rio_event17 with dissolve
    mc "Rio, I can't grow body hair. What's wrong with me?"
    scene ep10_bbq_rio_event14 with dissolve
    ri "Aw. Nothing's wrong with you."
    scene ep10_bbq_rio_event17 with dissolve
    mc "I tried but almost nothing's coming."
    mc "I get some lonely strands on my chest but it looks horrible so I shave them."
    scene ep10_bbq_rio_event16 with dissolve
    mc "And my pubes. My pubes! They look weird. So, I shave them too."
    scene ep10_bbq_rio_event14 with dissolve
    ri "That poster got to you, didn't it?"
    ri "Your brothers said it didn't."
    scene ep10_bbq_rio_event16 with dissolve
    mc "What do I do, Rio?"
    scene ep10_bbq_rio_event14 with dissolve
    ri "First off, you should mellow out for a few hours until the drugs wear off."
    ri "After that, if you're still feeling like this, come talk to me about it again and I'll help you deal with it."
    scene ep10_bbq_rio_event12 with dissolve
    ri "Let me just say that you don't need body hair to be a man, [name]."
    ri "When I looked at that picture of you in the poster, do you know what I saw?"
    scene ep10_bbq_rio_event18 with dissolve
    mc "*{i}Whisper{/i}* Dinosaurs?"
    scene ep10_bbq_rio_event14 with dissolve
    ri "No. I saw a poor attempt at body shaming someone who shouldn't feel any shame."
    ri "And I know for a fact that others felt the same as me."
    scene ep10_bbq_rio_event12 with dissolve
    ri "They were clutching at straws because they didn't find anything else to fault you with."
    ri "You're good the way you are, [name]. Don't let it get to you."
    scene ep10_bbq_rio_event19 with dissolve
    ri "*{i}Smack{/i}*"
else:
    scene ep10_bbq_rio_event22 with dissolve
    mc "Yeah, it's me. I thought I saw you take off. You're not leaving already, right?"
    scene ep10_bbq_rio_event23 with dissolve
    ri "No, I needed a break from the party. It's too noisy for me, right now."
    ri "It felt good to get some space and enjoy this place by myself for a little bit."
    scene ep10_bbq_rio_event24 with dissolve
    mc "It is loud and crazy over there, yeah."
    mc "I'm glad people are having fun, but I'm not so sure about the drugs they're taking."
    scene ep10_bbq_rio_event25 with dissolve
    ri "Mushrooms aren't that bad, but it kinda depends on what mood you're in when you're taking them."
    ri "If you see someone having a bad trip and hallucinating, there's not much you can do but to try and calm them down until it wears off."
    scene ep10_bbq_rio_event26 with dissolve
    mc "It sounds like you've got experience with it."
    scene ep10_bbq_rio_event25 with dissolve
    ri "I've tried it many times, so yeah. It's nice, but I had some bad nights with it too."
    ri "Once, I thought I was locked inside of a big shoe box and couldn't get out."
    ri "What really happened was that Quinn locked us inside of her room when we took the shrooms, so we didn't go wander off when we were high."
    scene ep10_bbq_rio_event26 with dissolve
    if ep4_smoked_weed:
        mc "That sounds scary. I'm happy I passed on it."
    else:
        mc "That doesn't sound fun at all. I don't get why people do drugs like that."
    scene ep10_bbq_rio_event25 with dissolve
    if ep4_smoked_weed:
        ri "Yeah, if it's your first time, I wouldn't do it out here."
    else:
        ri "It's fun experimenting. You drink alcohol, don't you? This is just another way of warping your senses. It's fun."
    scene ep10_bbq_rio_event27 with dissolve
    mc "Anyway... Help me keep an eye out for them tonight. I don't want anything to happen to them."
    scene ep10_bbq_rio_event25 with dissolve
    ri "They're in good company, but sure."
    scene ep10_bbq_rio_event28 with dissolve
    ri "Hey... Since when do you grow a beard?"
    scene ep10_bbq_rio_event27 with dissolve
    mc "I'm trying something new. Do you like it?"
    scene ep10_bbq_rio_event12 with dissolve
    ri "It looks weird on you. Maybe I'll get used to it, but I like you better clean-shaven. Sorry..."
    scene ep10_bbq_rio_event13 with dissolve
    mc "Thank you. I do too."
    scene ep10_bbq_rio_event12 with dissolve
    ri "Then why are you growing it?"
    scene ep10_bbq_rio_event13 with dissolve
    mc "No reason."
    scene ep10_bbq_rio_event14 with dissolve
    ri "This doesn't have anything to do with those posters, does it?"
    scene ep10_bbq_rio_event13 with dissolve
    mc "How did you know? You just saw through me."
    scene ep10_bbq_rio_event14 with dissolve
    ri "Because it isn't you. And your brothers told me you were among the few who didn't get affected by the pictures."
    ri "I guess that made me open my eyes more to see if that was the case or if you were hiding some of the pain."
    scene ep10_bbq_rio_event16 with dissolve
    mc "They aren't completely wrong. I'm lucky they didn't write my name on it and that my face was concealed."
    mc "But somehow those words they wrote cut deeper than I thought they would."
    scene ep10_bbq_rio_event29 with dissolve
    mc "I don't get a lot of body hair, and the little I get I shave."
    mc "I guess those words made me overanalyze if that's a bad thing in people's minds or not. I only thought it was me who had a problem with it."
    scene ep10_bbq_rio_event12 with dissolve
    ri "You don't need body hair to be a man, [name]."
    ri "When I looked at that picture of you in the poster, do you know what I saw?"
    scene ep10_bbq_rio_event14 with dissolve
    ri "I saw a poor attempt at body shaming someone who shouldn't feel any shame."
    ri "And I know for a fact that others felt the same as me."
    scene ep10_bbq_rio_event12 with dissolve
    ri "They were clutching at straws because they didn't find anything else to fault you with."
    ri "You're good the way you are, [name]. Don't let it get to you."
    scene ep10_bbq_rio_event19 with dissolve
    ri "*{i}Smack{/i}*"
scene ep10_bbq_rio_event20 with dissolve
$ renpy.pause()
scene ep10_bbq_rio_event21 with dissolve
$ renpy.pause()
scene ep10_bbq_rio_event13 with dissolve
mc "Thanks, Rio..."
mc "I realize I look stupid with the beard, but I wanted to give it a try."
mc "The next time I do it, it won't be for these reasons."
scene ep10_bbq_rio_event30 with dissolve
ri "I haven't been able to stop thinking about the arcade since we went there."
scene ep10_bbq_rio_event31 with dissolve
if ep10_shroom_choice == "DIK":
    mc "Oh! The arcade! Yes! That was such a great time!"
else:
    mc "Me neither! I had so much fun."
scene ep10_bbq_rio_event12 with dissolve
ri "Honestly, I can't remember when I had that much fun."
ri "When are we doing it again?"
scene ep10_bbq_rio_event13 with dissolve
mc "Oh, definitely sometime soon. I just need to stock up on quarters before we go."
scene ep10_bbq_rio_event12 with dissolve
ri "It can get expensive if you do it like we did it every time."
scene ep10_bbq_rio_event13 with dissolve
mc "It was a great date."
scene ep10_bbq_rio_event32 with dissolve
ri "Did I bum you out when I left without doing stuff to you?"
scene ep10_bbq_rio_event33 with dissolve
mc "What do you mean?"
scene ep10_bbq_rio_event32 with dissolve
ri "Like, were you expecting me to blow you after or something?"
scene ep10_bbq_rio_event33 with dissolve
mc "What!? Not at all. Where did you come up with that?"
scene ep10_bbq_rio_event32 with dissolve
ri "So, you just wanted to hang out with me and do whatever I wanted to do?"
scene ep10_bbq_rio_event33 with dissolve
mc "That's why I tagged along."
scene ep10_bbq_rio_event32 with dissolve
ri "I kept telling myself that's what it was, too. That you wanted to hang out with me."
ri "But after I came back home, I was unsure and thought that couldn't possibly be it."
ri "How fucked up am I, [name]?"
scene ep10_bbq_rio_event33 with dissolve
mc "That's what it was. Everything doesn't have to be about sex."
mc "Just because I want to sleep with you doesn't mean I don't want to hang out with you too."
if ep10_shroom_choice == "DIK":
    scene ep10_bbq_rio_event12 with dissolve
    ri "That's not the shrooms talking, right?"
    scene ep10_bbq_rio_event33 with dissolve
    mc "No, it's not. It's me."
scene ep10_bbq_rio_event34 with dissolve
$ renpy.pause()
scene ep10_bbq_rio_event19 with dissolve
ri "*{i}Smack{/i}*"
scene ep10_bbq_rio_event36 with dissolve
ri "But what if I want the sex too?"
ri "Like, if I acknowledge that it's not the reason you'd be spending time with me, but still want it. That's not fucked up, is it?"
scene ep10_bbq_rio_event35 with dissolve
mc "I know I put that idea into your head, to play hard to get..."
mc "But that doesn't mean that I don't want to be able to get you at all."
mc "I think you should have sex if it's with someone you think is worth having it with."
mc "And I hope that you think that someone is me. And if it's not, then I'll try harder to show you I'm worth it."
scene ep10_bbq_rio_event36 with dissolve
ri "I admit, flirting with guys in front of you was fun because I wanted to see the effect it had on you."
ri "But it was mean because I already knew you were worth it. You're absolutely worth it."
scene anim_riona_kiss_ep10 with dissolve
pause
scene ep10_bbq_rio_event37 with dissolve
ri "If there only were a bed out here, I'd show you how much you're worth it."
scene ep10_bbq_rio_event38 with dissolve
mc "My tent is back there."
scene ep10_bbq_rio_event37 with dissolve
ri "Along with everyone else. It's too early to use your tent for that."
scene ep10_bbq_rio_event38 with dissolve
mc "Ok... I don't know about you but this bench is soft enough for me."
scene ep10_bbq_rio_event37 with dissolve
if ep10_shroom_choice == "DIK":
    ri "That's gotta be the shrooms talking."
else:
    ri "You want it that bad, huh?"
scene ep10_bbq_rio_event38 with dissolve
if ep10_shroom_choice == "DIK":
    mc "It probably is."
else:
    mc "Yeah."
stop music fadeout 3
scene ep10_bbq_rio_event37 with dissolve
ri "Ok, fuck it."

label ep10_riona_lewd_label:
if _in_replay:
    if persistent.name == None:
        $ name = "MC"
    else:
        $ name = persistent.name

    if persistent.mc_riona == None:
        $ mc_riona = name
    else:
        $ mc_riona = persistent.mc_riona
    if persistent.riona == None:
        $ riona = "Riona"
    else:
        $ riona = persistent.riona
    $ ep10_shroom_choice = "CHICK"
hide screen new_phone_screen
play music "music/ep9/licensed_music/track121.mp3"
queue music ["music/ep9/licensed_music/track132.mp3","music/ep9/licensed_music/track121.mp3"]
$ ep10_riona_lewd = True

scene anim_riona_kiss_ep10 with dissolve
ri "*{i}Smack{/i}* Mmm..."
mc "Your lips are so soft."
pause

scene ep10_riona_lewd1 with dissolve
if ep10_shroom_choice == "DIK":
    mc "Whoa... That's so beautiful."
else:
    mc "Won't you get cold?"
scene ep10_riona_lewd2 with dissolve
if ep10_shroom_choice == "DIK":
    ri "That's right, [mc_riona]. Happy thoughts are good for you."
else:
    ri "You'll keep me warm."
scene ep10_riona_lewd3 with dissolve
mc "Hope no one walks this way."
scene ep10_riona_lewd4 with dissolve
ri "If they do, does it matter?"
scene ep10_riona_lewd5 with dissolve
mc "True. They've all seen my junk anyway."
ri "Haha!"
menu:
    "Get pleasured":
        label ep10_rio_lewd_pleasured_label:
        menu:
            "Handjob":
                scene anim_riona_hj1_ep10 with dissolve
                mc "Yeah... Rub it slowly."
                ri "I'll take good care of you, [mc_riona]."
                ri "It's so smooth, thick and warm."
                ri "You shouldn't be ashamed of your cock. It's perfect, [mc_riona]."
                pause
                jump ep10_rio_lewd_pleasured_label
            "Blowjob":
                scene anim_riona_bj2_ep10 with dissolve
                ri "*{i}Lick lick suck suck{/i}*"
                ri "*{i}Suck suck{/i}* Do you like it?"
                pause
                if ep10_shroom_choice == "DIK":
                    scene anim_riona_bj1b_ep10 with dissolve
                    mc "..."
                    ri "*{i}Suck suck{/i}* [name]?"
                    mc "Yeah. Yeah... Totally."
                    pause
                else:
                    scene anim_riona_bj1_ep10 with dissolve
                    mc "Yeah, a lot. Your mouth feels so warm when it's cold outside."
                    pause
                jump ep10_rio_lewd_pleasured_label
            "Pleasure her":
                jump ep10_rio_lewd_pleasure_label
            "Continue":
                $ renpy.pause(0.5)
    "Pleasure her":
        label ep10_rio_lewd_pleasure_label:
        menu:
            "Lick pussy":
                scene anim_riona_cunn1_ep10 with dissolve
                ri "Mmm... [mc_riona]. You know how to do that, don't you?"
                ri "(If I only had my vibrator... It would have felt amazing to have it vibrate on my clit as he did this.)"
                pause
                scene anim_riona_cunn2_ep10 with dissolve
                mc "*{i}Lick lick{/i}*"
                pause
                jump ep10_rio_lewd_pleasure_label
            "Lick asshole":
                scene anim_riona_cunn3_ep10 with dissolve
                ri "Someone's feeling kinky, huh?"
                mc "*{i}Lick lick{/i}*"
                pause
                jump ep10_rio_lewd_pleasure_label
            "Finger pussy":
                scene anim_riona_finger1_ep10 with dissolve
                ri "Put that fat finger inside me..."
                ri "*{i}Moans{/i}* Yeah... Do that motion."
                pause
                scene anim_riona_finger2_ep10 with dissolve
                ri "(That's odd... That feels...good.)"
                ri "(I like how he's doing that. But it would be better if he turned it around to hit the G spot...)"
                ri "*{i}Moans{/i}*"
                pause
                jump ep10_rio_lewd_pleasure_label
            "Finger asshole":
                scene ep10_riona_lewd6 with dissolve
                ri "Use some spit on your finger."
                scene anim_riona_finger3_ep10 with dissolve
                ri "Warming me up, huh?"
                mc "Yeah..."
                pause
                jump ep10_rio_lewd_pleasure_label
            "Get pleasured":
                jump ep10_rio_lewd_pleasured_label
            "Continue":
                $ renpy.pause(0.5)

scene ep10_riona_lewd11 with dissolve
ri "Put it in, [mc_riona]."
scene ep10_riona_lewd12 with dissolve
$ renpy.pause()

scene ep10_riona_lewd13 with dissolve
ri "Yes, right there... Get inside me."

scene anim_riona_miss1_ep10 with dissolve
ri "This feels right..."
mc "Yeah... You're so warm and tight, [riona]."
pause
scene anim_riona_miss3_ep10 with dissolve
ri "You've wanted to fuck me for a while now, haven't you?"
mc "Yeah. I hate how I cockblocked myself at Halloween. But I hope something good came out of it."
pause
scene anim_riona_miss2_ep10 with dissolve
ri "Maybe it did... Enjoy it now, [mc_riona]. Enjoy my holes."
pause

$ tmpInt = 0
label ep10_rio_lewd_loop_label:
menu:
    "Reverse cowgirl (Anal)":
        $ tmpInt += 1
        scene anim_riona_rev1_ep10 with dissolve
        mc "Ride me, [riona]."
        ri "This bench isn't that bad after all."
        pause
        scene anim_riona_rev2_ep10 with dissolve
        ri "I don't even feel it's cold anymore. All I feel is your hard cock filling me up."
        ri "And I bet I'll feel even warmer if you pump your seed into me. *{i}Moans{/i}*"
        pause
        jump ep10_rio_lewd_loop_label
    "Doggystyle":
        $ tmpInt += 1
        menu:
            "Vaginal":
                scene anim_riona_doggy1_ep10 with dissolve
                ri "Fuck my pussy, [mc_riona]. Fuck it hard."
                pause
                scene anim_riona_doggy2_anal_ep10 with dissolve
                mc "Damn... You're squeezing, aren't you?"
                ri "Uh-huh. I want you to feel how tight I can get for you."
                pause
                scene anim_riona_doggy2_ep10 with dissolve
                mc "That's unfair... I'm already big enough for it to be tight as hell."
                ri "I bet this is like torture for you, then."
                mc "Yeah, the best kind of torture. Fuck..."
                pause
            "Anal":
                scene anim_riona_doggy1_anal_ep10 with dissolve
                ri "*{i}Moans{/i}* Fuck, [mc_riona]!"
                mc "Is it too hard?"
                ri "I can take it. But looking at you, I shouldn't be able to. Fuck you're big, [mc_riona]."
                pause
                scene anim_riona_doggy2_anal_ep10 with dissolve
                mc "It feels like I'm in heaven."
                ri "Haha... Well, if that isn't the best rating you can get, I don't know what is."
                ri "Fuck my ass, [mc_riona]. Pound it!"
                pause
                scene anim_riona_doggy3_anal_ep10 with dissolve
                ri "Hngn... Yes! That's more like it! Fuck my ass!"
                pause
                scene anim_riona_doggy4_anal_ep10 with dissolve
                ri "*{i}Moans{/i}*"
                pause
        jump ep10_rio_lewd_loop_label
    "Standing (Anal)":
        $ tmpInt += 1
        scene anim_riona_stand1_ep10 with dissolve
        ri "Hngn... Hngn... Yes! Hngn... Fuck!"
        ri "Go deep! Go hard!"
        mc "You love it, don't you?"
        ri "Yes! I love it! I love your cock, [mc_riona]."
        ri "Harder! Break me!"
        mc "Fuck! Ahhh..."
        pause
        jump ep10_rio_lewd_loop_label
    "Against tree":
        $ tmpInt += 1
        scene anim_riona_stand2_ep10 with dissolve
        ri "Give it to me, [mc_riona]."
        mc "Fuck... I hope we're not being too loud."
        ri "Don't worry about it. They're blasting music over there. We can moan and scream as loud as we want to over here."
        pause
        scene anim_riona_stand3_ep10 with dissolve
        ri "*{i}Moans{/i}* You're fucking me so good, [mc_riona]."
        pause
        jump ep10_rio_lewd_loop_label
    "Facing her":
        $ tmpInt += 1
        scene anim_riona_miss1_ep10 with dissolve
        ri "Mhm... Mhm... Yes... Like that..."
        pause
        scene anim_riona_miss2_ep10 with dissolve
        pause
        scene anim_riona_miss3_ep10 with dissolve
        ri "Fuck me, [mc_riona]. Fuck my pussy!"
        pause
        jump ep10_rio_lewd_loop_label
    "Cum" if tmpInt > 2:
        mc "I can't hold it any longer... I have to cum."
        menu:
            "Facial":
                scene anim_riona_cum_ep10 with dissolve
                ri "Cum all over my face, [mc_riona]. Give it to me!"
                pause
                scene ep10_riona_lewd14 at vpunch, cum2
                $ renpy.pause(0.5)
                scene ep10_riona_lewd14 at vpunch, cum2
                $ renpy.pause(0.5)
                scene ep10_riona_lewd14 at vpunch, cum2
                $ renpy.pause()
                scene ep10_riona_lewd15 with dissolve
                $ renpy.pause()
            "Creampie":
                menu:
                    "Pussy":
                        scene anim_riona_doggy1_ep10 with dissolve
                        ri "Cum inside of my pussy, [mc_riona]. Let me feel the warmth of your cum."
                        scene ep10_riona_lewd7 at vpunch, cum1
                        $ renpy.pause(0.5)
                        scene ep10_riona_lewd7 at vpunch, cum1
                        $ renpy.pause(0.5)
                        scene ep10_riona_lewd7 at vpunch, cum1
                        $ renpy.pause()
                        scene ep10_riona_lewd8 with dissolve
                        $ renpy.pause()
                    "Ass":
                        scene anim_riona_doggy1_anal_ep10 with dissolve
                        ri "Cum inside of my ass, [mc_riona]. Let me feel the warmth of your cum."
                        scene ep10_riona_lewd10 at vpunch, cum1
                        $ renpy.pause(0.5)
                        scene ep10_riona_lewd10 at vpunch, cum1
                        $ renpy.pause(0.5)
                        scene ep10_riona_lewd10 at vpunch, cum1
                        $ renpy.pause()
                        scene ep10_riona_lewd9 with dissolve
                        $ renpy.pause()
            "On tits":
                scene anim_riona_cum_ep10 with dissolve
                ri "Shoot it all over my tits. Give me that pearl necklace."
                pause
                scene ep10_riona_lewd16 at vpunch, cum3
                $ renpy.pause(0.5)
                scene ep10_riona_lewd16 at vpunch, cum3
                $ renpy.pause(0.5)
                scene ep10_riona_lewd16 at vpunch, cum3
                $ renpy.pause()
                scene ep10_riona_lewd17 with dissolve
                $ renpy.pause()

scene ep10_bbq_rio_event39 with dissolve
$ renpy.pause()
scene ep10_bbq_rio_event40 with dissolve
$ renpy.pause()
scene ep10_bbq_rio_event41 with dissolve
$ renpy.pause()
scene ep10_bbq_rio_event42 with dissolve
if ep10_shroom_choice == "DIK":
    ri "We should probably get back to the party."
    scene ep10_bbq_rio_event43 with dissolve
    mc "Whoa... Everything's spinning."
    scene ep10_bbq_rio_event44 with dissolve
    stop music fadeout 3
    ri "Don't wander off alone into the woods, [name]. Stay with the others."
else:
    stop music fadeout 3
    ri "We should probably get back to the party."
    scene ep10_bbq_rio_event44 with dissolve
    $ renpy.pause()

$ renpy.end_replay()
$ persistent.ep10_lewd_riona = True
$ calcScenes()
$ new_bio("Riona", "I had sex with Riona at the DIKs' Thanksgiving, and we had a nice heart-to-heart about dating.")
$ mphone_stats_add_girl_s3("riona","You had sex with Riona during the DIKs' Thanksgiving party in episode 10.")
show screen new_phone_screen
$ event_list.append("ep10_bbq_final_phase")
$ currentFreeRoamLabel = "ep10_bbq_main_label"
$ task_list[1] = ""
$ updateTaskList()
$ mphone_next_song()
jump endEvent

label ep10_bbq_sy_event_label:
if ep10_shroom_choice == "DIK":
    scene ep10_bbq_sy_event1 with dissolve
    mc "There she is! The wicked witch of the magic forest!"
    mc "Quick! I don't have time to explain. Give me your bra!"
    scene ep10_bbq_sy_event2 with dissolve
    sy "Holy fuck, you drunkard! Is the peroxisome count in your body zero? How does one get this fucked up at a laid-back barbecue party?"
    scene ep10_bbq_sy_event3 with dissolve
    mc "She speaks in tongues. I will need to find some kind of a thesaurus to continue my quest."
    play sound "sound_effects/slap.mp3"
    scene ep10_bbq_sy_event6 with hpunch
    mc "Ow!"
    scene ep10_bbq_sy_event3 with dissolve
    mc "Her hit is effective. It does 5 damage."
    scene anim_sally_stroke_ep10 with dissolve
    sy "*{i}Sigh{/i}* Seriously, what's wrong with you tonight?"
    mc "I don't know. Help me."
    sy "Stop stroking me."
    scene ep10_bbq_sy_event3 with dissolve
    mc "Yeah. You're right! That feels better, Sally."
    scene ep10_bbq_sy_event4 with dissolve
    sy "Wait a minute... You're not drunk. You're on drugs."
    scene ep10_bbq_sy_event3 with dissolve
    mc "I ate something I shouldn't have, Sally."
    scene ep10_bbq_sy_event2 with dissolve
    sy "Figures. For someone who's studying engineering, you're remarkably dumb."
    scene ep10_bbq_sy_event3 with dissolve
    mc "Aw. You know what I'm studying? I didn't think you cared, Sally."
    scene ep10_bbq_sy_event2 with dissolve
    sy "I don't. But some people won't shut up about you."
    sy "How you got popular among girls from a dick pic I'll never know."
    scene ep10_bbq_sy_event3 with dissolve
    mc "I think it's got something to do with the size, Sally."
    scene ep10_bbq_sy_event7 with dissolve
    mc "It's like this big, Sally."
    scene ep10_bbq_sy_event8 with dissolve
    sy "Stop repeating my name like that."
    scene ep10_bbq_sy_event7 with dissolve
    mc "I forgot what I'm doing with my hands, Sally."
    scene ep10_bbq_sy_event8 with dissolve
    sy "At least you're not stroking me anymore."
    scene anim_sally_stroke_ep10 with dissolve
    sy "Seriously. Cut the crap, [name]."
    scene ep10_bbq_sy_event3 with dissolve
    mc "Ok. Ok. Ok. I got it."
    mc "Are you enjoying science class, Sally?"
    scene ep10_bbq_sy_event5 with dissolve
    sy "It's not the best. And before you start, it's not because it's hard."
    sy "I regret my choice of lab partner. Ron's annoying me like crazy these days."
    scene ep10_bbq_sy_event3 with dissolve
    if ep8_revenge == "CHICK":
        mc "Ron? Oh, that guy. I hardly know him."
    elif ep8_revenge == "NEUTRAL":
        mc "Ron? Oh, that guy. Haha! Derek threw piss at him once."
        scene ep10_bbq_sy_event3b with dissolve
        sy "Haha! He sure did."
    else:
        mc "Ron? Oh, that guy. Haha! Derek and I threw piss at him once."
        scene ep10_bbq_sy_event3b with dissolve
        sy "Haha! You sure did."
    scene ep10_bbq_sy_event3 with dissolve
    mc "Maybe you can change lab partners, Sally."
    scene ep10_bbq_sy_event2 with dissolve
    sy "Yeah? To who? You? I'd rather do the experiments on my own, but nooooo... Dr. Jenkins said that would be wasting precious chemicals."
    sy "It's so stupid. We're just mixing cheap salts, acids and bases. With what we pay for our education, you'd think they'd have a budget for that."
    scene ep10_bbq_sy_event3 with dissolve
    mc "We could brew a potion in there next time!"
    scene ep10_bbq_sy_event11 with dissolve
    $ renpy.pause()
    scene ep10_bbq_sy_event9 with dissolve
    mc "Right, Sally?"
    mc "Huh!? She vanished. Whoa..."
    $ event_list.append("sally_block")
else:
    scene ep10_bbq_sy_event1b with dissolve
    mc "So, Sally... When are you joining the HOTs?"
    scene ep10_bbq_sy_event2 with dissolve
    sy "Um... Never?"
    scene ep10_bbq_sy_event3 with dissolve
    mc "Ah, they didn't want you..."
    scene ep10_bbq_sy_event2 with dissolve
    sy "Pff! I would never bother to apply."
    scene ep10_bbq_sy_event3 with dissolve
    mc "Yet you've been to many parties with them."
    scene ep10_bbq_sy_event2 with dissolve
    sy "So? I can party with whomever I want."
    scene ep10_bbq_sy_event3 with dissolve
    mc "You don't have to get mad at me. I'm happy to see you here tonight."
    scene ep10_bbq_sy_event4 with dissolve
    sy "Yeah, right."
    scene ep10_bbq_sy_event3 with dissolve
    mc "No, I am. We constantly run into each other at parties and now we're even in the same class."
    mc "How about we start over with each other? Somehow, we've gotten off on the wrong foot."
    scene ep10_bbq_sy_event5 with dissolve
    sy "Yeah, whatever."
    scene ep10_bbq_sy_event3 with dissolve
    mc "So... Are you enjoying science class?"
    scene ep10_bbq_sy_event5 with dissolve
    sy "It's not the best. And before you start, it's not because it's hard."
    sy "I regret my choice of lab partner. Ron's annoying me like crazy these days."
    scene ep10_bbq_sy_event3 with dissolve
    if ep8_revenge == "CHICK":
        mc "Ron? Oh, that guy. I hardly know him."
    elif ep8_revenge == "NEUTRAL":
        mc "Ron? Oh, that guy. If it helps, Derek threw piss at him once."
        scene ep10_bbq_sy_event3b with dissolve
        sy "Haha! He sure did."
    else:
        mc "Ron? Oh, that guy. If it helps, Derek and I threw piss at him once."
        scene ep10_bbq_sy_event3b with dissolve
        sy "Haha! You sure did."
    scene ep10_bbq_sy_event3 with dissolve
    mc "Maybe you can change lab partners."
    scene ep10_bbq_sy_event5 with dissolve
    sy "I'd rather do the experiments on my own, but nooooo... Dr. Jenkins said that would be wasting precious chemicals."
    sy "It's so stupid. We're just mixing cheap salts, acids and bases. With what we pay for our education, you'd think they'd have a budget for that."
    scene ep10_bbq_sy_event3 with dissolve
    mc "Sometimes, you're forced to work with students you don't like. That was basically my Gender studies class in a nutshell."
    scene ep10_bbq_sy_event5 with dissolve
    sy "I'm not a stranger to that, it's just...ugh..."
    if ep10_pp_activity == 0:
        scene ep10_bbq_sy_event3 with dissolve
        mc "Cheer up. Wanna do something fun? How about some Beer Pong?"
        scene ep10_bbq_sy_event2 with dissolve
        sy "Beer Pong? And strip naked in front of you? No thanks."
        scene ep10_bbq_sy_event3 with dissolve
        if affinity == "DIK":
            if branchAlone:
                mc "That sounds like you're lacking confidence in your skills or assets. But you shouldn't."
            else:
                mc "That sounds like you're lacking confidence in your skills."
        else:
            if branchAlone:
                mc "We could play with those rules, but we don't have to."
            else:
                mc "Haha, no. We don't have to play with those rules."
    else:
        scene ep10_bbq_sy_event3 with dissolve
        mc "I get it. Let me know if I can help you with it somehow."
    scene ep10_bbq_sy_event2 with dissolve
    sy "Are you hitting on me or something?"
    sy "Like everyone on campus, I've seen your penis and I'm not interested."
    scene ep10_bbq_sy_event3 with dissolve
    if affinity == "DIK":
        mc "Scared?"
    else:
        mc "Ouch..."
    scene ep10_bbq_sy_event2 with dissolve
    sy "How you got popular among girls from a dick pic I'll never know."
    scene ep10_bbq_sy_event3 with dissolve
    if affinity == "DIK":
        mc "It's probably because of the size of it."
    else:
        mc "I thought we were starting over, but I guess we're back to this dynamic..."
    scene ep10_bbq_sy_event5 with dissolve
    sy "Whatever! I'm not interested."
    scene ep10_bbq_sy_event3 with dissolve
    if affinity == "DIK":
        mc "All right... I'm not gonna waste more time here. See you!"
    else:
        mc "All right... Have a nice evening, Sally."
    scene ep10_bbq_sy_event10 with dissolve
    $ renpy.pause()
$ new_bio("Sally", "I tried my best to talk to Sally without pissing her off. It didn't go well.")

$ task_list[2] = ""
$ updateTaskList()
jump endEvent

label ep10_bbq_jacob_event_label:
$ guideSuggestedPage = 137
if ep10_shroom_choice == "DIK":
    scene ep10_bbq_jacob_event1 with dissolve
    jac "[name]?"
    play sound "sound_effects/slap.mp3"
    scene ep10_bbq_jacob_event2 with hpunch
    $ renpy.pause()
    scene ep10_bbq_jacob_event5 with dissolve
    jac "Hey, stop that!"
    scene ep10_bbq_jacob_event6 with dissolve
    mc "The mosquitos are everywhere!"
    scene ep10_bbq_jacob_event4 with dissolve
    jac "Damn, is there anyone at home in there?"
    scene ep10_bbq_jacob_event6 with dissolve
    mc "I'm right here, Jackoff."
    scene ep10_bbq_jacob_event7 with dissolve
    jac "Did you just call me jackoff?"
    scene ep10_bbq_jacob_event6 with dissolve
    mc "..."
    scene ep10_bbq_jacob_event8 with dissolve
    jac "Bro, listen... I know this might seem like a weird question and all, but I gotta ask you something."
    jac "It's about Zoey..."
    scene ep10_bbq_jacob_event6 with dissolve
    mc "I'm listening."
    scene ep10_bbq_jacob_event8 with dissolve
    jac "I've been chatting her up tonight, and over the past few weeks, we've texted a lot."
    scene ep10_bbq_jacob_event6 with dissolve
    mc "Zoey's got blue hair."
    scene ep10_bbq_jacob_event7 with dissolve
    jac "Yeah, she sure does..."
    jac "Anyway, I think we're kinda hitting it off."
    scene ep10_bbq_jacob_event6 with dissolve
    mc "I like you too, Jackoff."
    scene ep10_bbq_jacob_event7 with dissolve
    jac "*{i}Sigh{/i}* Yeah, I like you, bro."
    jac "But, I meant me and Zoey. I think we're hitting it off."
    scene ep10_bbq_jacob_event8 with dissolve
    jac "Since you're like her ex or something..."
    jac "It's not cool for me to act on it, but if it's ok with you..."
    jac "...would you be ok with it if I did?"
    scene ep10_bbq_jacob_event6 with dissolve
    mc "Did what?"
    scene ep10_bbq_jacob_event8 with dissolve
    jac "If I made a move on her."
    scene ep10_bbq_jacob_event6 with dissolve
    menu:
        "It's ok":
            $ ep10_zoey_jacob = True
            play sound "sound_effects/slap.mp3"
            scene ep10_bbq_jacob_event2 with hpunch
            jac "Ow!"
            scene ep10_bbq_jacob_event9 with dissolve
            mc "It's ok."
            scene ep10_bbq_jacob_event7 with dissolve
            jac "Then why are you slapping me?"
            scene ep10_bbq_jacob_event6 with dissolve
            mc "I am?"
            scene ep10_bbq_jacob_event10 with dissolve
            jac "Man... Thanks, bro. It means a lot that you're cool with it."
        "Don't do it":
            $ ep10_zoey_jacob = False
            play sound "sound_effects/slap.mp3"
            scene ep10_bbq_jacob_event3 with hpunch
            jac "Ow!"
            scene ep10_bbq_jacob_event9 with dissolve
            mc "Don't do it."
            scene ep10_bbq_jacob_event8 with dissolve
            jac "Really? Is it because it's fresh between you two? Haven't you moved on?"
            scene ep10_bbq_jacob_event6 with dissolve
            if branchAlone:
                mc "I just don't want you to do that."
            else:
                mc "Yeah, but... I just don't want you to do that."
            scene ep10_bbq_jacob_event8 with dissolve
            jac "Aight... I hear you."
            jac "Damn... But what if she comes on to me, bro?"
            scene ep10_bbq_jacob_event6 with dissolve
            mc "..."
            play sound "sound_effects/slap.mp3"
            scene ep10_bbq_jacob_event3 with vpunch
            jac "Ow! [name], I got it!"
            scene ep10_bbq_jacob_event5 with dissolve
            jac "You slap harder than you think, dude."
            jac "Sorry, [name]. Forget I asked, ok? It was stupid."
else:
    scene ep10_bbq_jacob_event13 with dissolve
    jac "[name]?"
    scene ep10_bbq_jacob_event6 with dissolve
    mc "Hey. How's it going?"
    scene ep10_bbq_jacob_event8 with dissolve
    jac "Bro, listen... I know this might seem like a weird question and all, but I gotta ask you something."
    jac "It's about Zoey..."
    scene ep10_bbq_jacob_event6 with dissolve
    mc "What about her?"
    scene ep10_bbq_jacob_event8 with dissolve
    jac "I've been chatting her up tonight, and over the past few weeks, we've texted a lot."
    jac "I think we're kinda hitting it off."
    scene ep10_bbq_jacob_event6 with dissolve
    mc "You are?"
    scene ep10_bbq_jacob_event8 with dissolve
    jac "I think so. Since you're like her ex or something..."
    jac "It's not cool for me to act on it, but if it's ok with you..."
    jac "...would you be ok with it if I did?"
    scene ep10_bbq_jacob_event6 with dissolve
    mc "Did what exactly?"
    scene ep10_bbq_jacob_event8 with dissolve
    jac "If I made a move on her. It's totally cool if you say no. I wouldn't hold it against you."
    scene ep10_bbq_jacob_event6 with dissolve
    menu:
        "It's ok":
            $ ep10_zoey_jacob = True
            mc "Uh... Sure, um... It's ok."
            mc "We're not together now and, if she likes you, what I think shouldn't stop you."
            scene ep10_bbq_jacob_event10 with dissolve
            jac "Man... Thanks, bro. It means a lot that you're cool with it."
        "Don't do it":
            $ ep10_zoey_jacob = False
            mc "Um... I'm gonna say no to this. Please, don't do it."
            scene ep10_bbq_jacob_event8 with dissolve
            jac "Really? Is it because it's fresh between you two? Haven't you moved on?"
            scene ep10_bbq_jacob_event6 with dissolve
            if branchAlone:
                mc "I'm not sure yet... But I don't want you to do that."
            else:
                mc "Yeah, but... I don't want you to do that."
            mc "I feel sick thinking that you would. I'm sorry..."
            scene ep10_bbq_jacob_event8 with dissolve
            jac "Aight... I hear you. I suspected you weren't cool with it. Thought I'd check first."
            jac "Damn... But what if she comes on to me, bro?"
            scene ep10_bbq_jacob_event6 with dissolve
            mc "I can't tell you guys what to do. But since you're asking me like this..."
            mc "All I can say is that I wouldn't want you to do it. I think it would hurt a lot seeing it."
            scene ep10_bbq_jacob_event11 with dissolve
            jac "Sorry, [name]. Forget I asked, ok? It was stupid."
scene ep10_bbq_jacob_event12 with dissolve
mc "(She's interested in Jacob now? My stomach kinda turned hearing that.)"
if ep10_zoey_jacob:
    mc "(But if that's what she wants...I'm not gonna stop her.)"

if ep10_zoey_jacob:
    $ new_bio("Jacob", "Jacob asked me if I was cool with him hooking up with Zoey. I told him I was. I didn't want to make that choice for Zoey if that was something she wanted.")
else:
    $ new_bio("Jacob", "Jacob asked me if I was cool with him hooking up with Zoey. I told him I wasn't.")
$ event_list.append("ep10_bbq_nick_event_label")
$ event_list.append("jacob_block")
$ task_list[4] = ""
if ep10_shroom_choice == "DIK":
    $ task_list[3] = "Find the leprechaun"
else:
    $ task_list[3] = "Talk to Nick"
$ updateTaskList()

jump endEvent

label ep10_bbq_jz_event_label:
scene ep10_bbq_jz_event1 with dissolve
jac "I never thought school was that fun, but college is way different."
jac "I spend most of my days in classes I actually enjoy."
jac "Sure, there are some mandatory classes that stink, but as a whole college rocks. You'd love it here!"
scene ep10_bbq_jz_event4 with dissolve
zo "Sounds like it. Not living with your parents and partying all the time sounds tempting."
scene ep10_bbq_jz_event2 with dissolve
jac "Yeah, these parties happen all the time. Every weekend there's something going on somewhere, you know?"
scene ep10_bbq_jz_event5 with dissolve
zo "Awesome."
zo "But I'm not sure about anything these days. I'm still trying to figure myself out."
zo "I never thought it would be this hard to know what I wanted to do with my life, especially after being dead set on surfing."
scene ep10_bbq_jz_event6 with dissolve
zo "Hm... Maybe that's why it's hard? Being so sure of myself, and never opening my eyes to new stuff..."
scene ep10_bbq_jz_event2 with dissolve
jac "If you have hobbies you love, trying to earn money from them is the way to go, if you ask me."
jac "Imagine doing what you love for a living. That's what I aim at."
scene ep10_bbq_jz_event4 with dissolve
zo "Yeah, you got a good idea going on with that. But what if you can't attain it? What if it's too far-fetched?"
scene ep10_bbq_jz_event3 with dissolve
jac "Like what?"
scene ep10_bbq_jz_event5 with dissolve
zo "Like, all you wanted to do is draw all day, but the pieces you draw aren't that special that people wanna buy them."
scene ep10_bbq_jz_event3 with dissolve
jac "You have to be smart about it. You could turn that art into prints for posters or clothes."
jac "You can work for commission or team up with someone who needs an artist. You don't have to narrow down your thinking that way."
jac "Use others so you can do what you want. You can be a part of something bigger, but still do what you wanna do."
scene ep10_bbq_jz_event5 with dissolve
zo "Wow... That makes a lot of sense. I guess I've been too hung up on managing everything on my own and to work for myself, instead of seeing those possibilities."
scene ep10_bbq_jz_event2 with dissolve
jac "They teach you all about it here is all I'm saying."
scene ep10_bbq_jz_event4 with dissolve
zo "Thanks, Jacob. Really."
scene ep10_bbq_jz_event2 with dissolve
jac "Hey, anytime."
scene ep10_bbq_jz_event7 with dissolve
$ renpy.pause()

if ep10_zoey_jacob:
    scene ep10_bbq_jz_event13 with dissolve
    zo "Uh... What are you doing?"
    scene ep10_bbq_jz_event11 with dissolve
    jac "I figured we were vibing and all. We've gotten closer since we met at Halloween, and if you don't do something about that, you usually end up being friendzoned."
    scene ep10_bbq_jz_event8 with dissolve
    zo "Ah... Listen, I gotta tell you..."
    zo "I think you're an awesome guy and we have stuff in common, like hobbies and such, but I'm not feeling the same vibes that you are."
    scene ep10_bbq_jz_event11 with dissolve
    jac "You're not? Damn... I thought you were. You've been so easy to talk to and interested in everything I said."
    scene ep10_bbq_jz_event9 with dissolve
    zo "I'm just being myself. I think you're interesting and fun to hang around, but not in that way."
    scene ep10_bbq_jz_event11 with dissolve
    jac "Fuck... I feel like a fucking clown... Sorry, Zoey."
    jac "I thought I felt something. It's probably the alcohol in combination with wanting there to be something."
    scene ep10_bbq_jz_event9 with dissolve
    zo "No harm done, dude. You gotta take your shots, right?"
    zo "But also, you're friends with [name]. Hooking up with someone he's close to, I would never do that to him."
    scene ep10_bbq_jz_event12 with dissolve
    jac "Me neither, but he was cool with it, so, I figured I'd give it a shot."
    scene ep10_bbq_jz_event8 with dissolve
    zo "He was cool with you hitting on me?"
    scene ep10_bbq_jz_event12 with dissolve
    jac "I asked him before about it. I wouldn't do it without checking with him."
    jac "But never mind. Let's forget this happened, ok?"
    stop music fadeout 3
    scene ep10_bbq_jz_event8 with dissolve
    zo "Yeah..."
    scene ep10_bbq_jz_event10 with dissolve
    $ renpy.pause()
else:
    scene ep10_bbq_jz_event11 with dissolve
    jac "Damn..."
    scene ep10_bbq_jz_event8 with dissolve
    zo "What's wrong?"
    scene ep10_bbq_jz_event11 with dissolve
    jac "You shouldn't look at me like that."
    scene ep10_bbq_jz_event8 with dissolve
    zo "Like how?"
    scene ep10_bbq_jz_event11 with dissolve
    jac "Zoey, I promised [name] I wouldn't hook up with you. If you're looking at me smiling like that, I feel you'd make me break that promise and I don't want that."
    scene ep10_bbq_jz_event9 with dissolve
    zo "I'm not sure what signals you think I'm sending you over here, but I'm just being friendly with you."
    scene ep10_bbq_jz_event11 with dissolve
    jac "Yeah, right. We've been vibing since Halloween and it's so easy to talk to you."
    jac "There's obviously something going on between us, but I can't do it."
    scene ep10_bbq_jz_event9 with dissolve
    zo "I hate to burst your bubble, but this is how I am. I haven't been flirting with you."
    zo "You're an interesting and friendly dude and we get along and share some hobbies, but that's all there is."
    scene ep10_bbq_jz_event12 with dissolve
    jac "Oh?"
    scene ep10_bbq_jz_event9 with dissolve
    zo "Sorry..."
    scene ep10_bbq_jz_event11 with dissolve
    jac "I feel like a fucking clown... Sorry, Zoey."
    jac "I thought I felt something. It's probably the alcohol in combination with wanting there to be something."
    scene ep10_bbq_jz_event9 with dissolve
    zo "No harm done, dude. You gotta take your shots, right?"
    zo "But also, you're friends with [name]. Hooking up with someone he's close to, I would never do that to him."
    scene ep10_bbq_jz_event12 with dissolve
    jac "No, I totally get that. He didn't want me to do it either, I promised him I wouldn't do anything."
    scene ep10_bbq_jz_event8 with dissolve
    zo "He asked you not to hit on me?"
    scene ep10_bbq_jz_event12 with dissolve
    jac "Nah, well... I asked him if he was cool with it earlier tonight and he said he didn't want me to do it, so..."
    jac "But never mind. Let's forget this happened, ok?"
    stop music fadeout 3
    scene ep10_bbq_jz_event8 with dissolve
    zo "Yeah..."
    scene ep10_bbq_jz_event10 with dissolve
    $ renpy.pause()

play music "music/ep10/bonfire.mp3"
scene ep10_bbq_jz_event9 with dissolve
zo "I need a break. I drank a lot of these."
scene ep10_bbq_jz_event14 with dissolve
$ renpy.pause()
scene ep10_bbq_jz_event15 with dissolve
$ renpy.pause()
scene ep10_bbq_jz_event16 with dissolve
$ renpy.pause()
if branchMayaJosy:
    scene ep10_bbq_jz_event23 with dissolve
elif branchSage:
    scene ep10_bbq_jz_event26 with dissolve
elif branchJill:
    scene ep10_bbq_jz_event27 with dissolve
elif branchAlone:
    scene ep10_bbq_jz_event31 with dissolve
else:
    scene ep10_bbq_jz_event30 with dissolve
$ renpy.pause()
if ep10_zoey_jacob:
    scene ep10_bbq_jz_event18 with dissolve
else:
    scene ep10_bbq_jz_event17 with dissolve
$ renpy.pause()
if branchMayaJosy:
    scene ep10_bbq_jz_event24 with dissolve
elif branchSage:
    scene ep10_bbq_jz_event25 with dissolve
elif branchJill:
    scene ep10_bbq_jz_event28 with dissolve
elif branchAlone:
    scene ep10_bbq_jz_event32 with dissolve
else:
    scene ep10_bbq_jz_event29 with dissolve
$ renpy.pause()
scene ep10_bbq_jz_event19 with dissolve
$ renpy.pause()
scene ep10_bbq_jz_event33 with dissolve
$ renpy.pause()
scene ep10_bbq_jz_event34 with dissolve
$ renpy.pause()
scene ep10_bbq_jz_event20 with dissolve
$ renpy.pause()
scene ep10_bbq_jz_event35 with dissolve
$ renpy.pause()
scene ep10_bbq_jz_event36 with vpunch
$ renpy.pause()
scene ep10_bbq_jz_event37 with dissolve
$ renpy.pause()
scene ep10_bbq_jz_event38 with dissolve
$ renpy.pause()
scene ep10_bbq_jz_event39 with dissolve
$ renpy.pause()
scene ep10_bbq_jz_event40 with dissolve
$ renpy.pause()
scene ep10_bbq_jz_event41 with dissolve
$ renpy.pause()
scene ep10_bbq_jz_event21 with dissolve
zo "Oh, fuck..."
scene ep10_bbq_jz_event22 with dissolve
$ renpy.pause()
$ renpy.sound.play("sound_effects/season3/zoey_intro.mp3", channel="sfx1", loop=False)
scene bg anim_zoey_run_ep10 movie with dissolve
$ renpy.pause()
zo "Fuck! Shitballs! Fuck!"
$ renpy.music.stop(channel="sfx1", fadeout=5)
stop music fadeout 5
scene ep10_bbq_jz_event_end with dissolve
$ renpy.pause()
scene black with Fade(2,1,1)
$ renpy.pause(4)
jump ep10_after_bbq_label

label ep10_bbq_jill2_event_label:
$ guideSuggestedPage = 137
if ep10_shroom_choice == "DIK":
    scene ep10_bbq_jill2_event37 with dissolve
    rs "Are you ok, [name]?"
    scene ep10_bbq_jill2_event38 with dissolve
    mc "Yeah... I think so. It's been a scary night, but I think the mushroom has finally lost its effect on me."
    scene ep10_bbq_jill2_event37 with dissolve
    rs "Good. You did some stupid shit."
    scene ep10_bbq_jill2_event38 with dissolve
    mc "Oh... Sorry."
    scene ep10_bbq_jill2_event39 with dissolve
    rs "No need to apologize to me."
    scene ep10_bbq_jill2_event38 with dissolve
    mc "Jill... Excuse me, I need to check up on her."

scene ep10_bbq_jill2_event40 with dissolve
$ renpy.pause()
scene ep10_bbq_jill2_event41 with dissolve
mc "Having fun?"
scene ep10_bbq_jill2_event42 with dissolve
ji "Haha, very much so."
scene ep10_bbq_jill2_event41 with dissolve
mc "What are you girls talking about?"
scene ep10_bbq_jill2_event43 with dissolve
sa "It's girl talk, [name]. It doesn't concern you."
scene ep10_bbq_jill2_event41 with dissolve
mc "Well, that makes me wanna know even more what you're talking about."
scene ep10_bbq_jill2_event43 with dissolve
sa "I think [name] is missing his girlfriend."
scene ep10_bbq_jill2_event42 with dissolve
ji "Do you want to join?"
scene ep10_bbq_jill2_event41 with dissolve
mc "I wanted to show you something, but we can do it later."
if ep9_jm_sad:
    scene ep10_bbq_jill2_event44 with dissolve
    $ renpy.pause()
scene ep10_bbq_jill2_event42 with dissolve
ji "I could use a leg stretcher."
scene ep10_bbq_jill2_event43 with dissolve
sa "Bring her back after, [name]. We're not done here."
scene ep10_bbq_jill2_event45 with dissolve
ji "Where are you taking me?"
stop music fadeout 3
mc "There's a jetty by the lake I wanted to show you."
scene ep10_bbq_jill2_event1 with dissolve
$ renpy.sound.play("sound_effects/season3/forest_soundscape.mp3", channel="sfx3", loop=True)
$ renpy.pause()
play music "music/ep4/romantic_piano.mp3"
scene ep10_bbq_jill2_event2 with dissolve
$ renpy.pause()
if ep10_shroom_choice == "DIK":
    scene ep10_bbq_jill2_event3 with dissolve
    ji "Feeling like yourself again?"
    scene ep10_bbq_jill2_event4 with dissolve
    mc "Yeah, I am. Sorry about that. I shouldn't have been persuaded to eat a mushroom with the others."
    scene ep10_bbq_jill2_event5 with dissolve
    ji "..."
    scene ep10_bbq_jill2_event6 with dissolve
    ji "I don't like that you're using drugs, [name]."
    scene ep10_bbq_jill2_event4 with dissolve
    mc "I'm not doing it that often. But I wanted to try it. And now that I have, I think I won't do it again."
    mc "It wasn't enjoyable at all."
    scene ep10_bbq_jill2_event3 with dissolve
    ji "Good. You should be careful. I wouldn't want something bad to happen to you."
    scene ep10_bbq_jill2_event4 with dissolve
    mc "I'm right here, Jill."
    scene ep10_bbq_jill2_event6 with dissolve
    ji "Please... Don't do that again. For me?"
    scene ep10_bbq_jill2_event5 with dissolve
    menu:
        "[mod_gr]I promise":
            $ ep10_jill_promise = True
            scene ep10_bbq_jill2_event4 with dissolve
            mc "I promise. It was just a stupid thing I wanted to try."
        "I'll try":
            $ ep10_jill_promise = False
            scene ep10_bbq_jill2_event4 with dissolve
            mc "I'll try, but I can't promise anything."
    mc "I'm not gonna start using drugs regularly, if that's what you're worried about."
    scene ep10_bbq_jill2_event8 with dissolve
    $ renpy.pause()
    scene ep10_bbq_jill2_event6 with dissolve
    ji "Ok."
else:
    scene ep10_bbq_jill2_event7 with dissolve
    ji "Your friends have been acting weird all night."
    scene ep10_bbq_jill2_event9 with dissolve
    mc "Yeah, I know. But they'll come to their senses soon enough. I think the effect of the drugs is wearing off."
    scene ep10_bbq_jill2_event8 with dissolve
    ji "..."

scene ep10_bbq_jill2_event10 with dissolve
$ renpy.pause()
scene ep10_bbq_jill2_event11 with dissolve
ji "This is a beautiful place. It makes me wish it was summer again, so we could take a swim."
scene ep10_bbq_jill2_event12 with dissolve
mc "Yeah. Are you cold?"
scene ep10_bbq_jill2_event11 with dissolve
ji "A bit. It was nice sitting by the bonfire."
scene ep10_bbq_jill2_event13 with dissolve
mc "Better?"
scene ep10_bbq_jill2_event14 with dissolve
$ renpy.pause()
scene ep10_bbq_jill2_event15 with dissolve
ji "They say it will snow soon."
mc "Hopefully, it won't be as bad as last year."
ji "You never know..."
mc "And then spring is around the corner, and before we know it, it's hot again."
scene ep10_bbq_jill2_event16 with dissolve
ji "Yeah. What are you looking forward to the most? Winter or Spring?"
scene ep10_bbq_jill2_event17 with dissolve
mc "Spring. Hands down."
scene ep10_bbq_jill2_event16 with dissolve
ji "Oh, that's right. You hate winter."
scene ep10_bbq_jill2_event17 with dissolve
mc "Compared to spring and summer, yeah."
mc "I'm looking forward to spring and spring break. I've heard some fun things about it."
mc "And I take it you're the other way around, since you hate spring break."
scene ep10_bbq_jill2_event18 with dissolve
ji "I don't hate spring break, I just don't do it the way everyone else does."
ji "And I do look forward to winter. I'm hoping you'll change your mind about it."
ji "Because I bet I can make you see that it's more fun than you think it is."
scene ep10_bbq_jill2_event19 with dissolve
mc "I'm not sure you can, but we can make a deal if you want."
scene ep10_bbq_jill2_event18 with dissolve
ji "What kind of a deal?"
scene ep10_bbq_jill2_event19 with dissolve
mc "If I try to come around on winter stuff, you try to come around on spring break."
scene ep10_bbq_jill2_event18 with dissolve
ji "Haha, why?"
scene ep10_bbq_jill2_event19 with dissolve
mc "The same reason you told me. I bet I can make you see that it's more fun than you think it is."
scene ep10_bbq_jill2_event20 with dissolve
$ renpy.pause()
scene ep10_bbq_jill2_event18 with dissolve
ji "Ok... Deal."
scene ep10_bbq_jill2_event17 with dissolve
mc "Really?"
scene ep10_bbq_jill2_event18 with dissolve
ji "Yes."
scene ep10_bbq_jill2_event17 with dissolve
mc "Oh, you don't know what you're in for."
scene ep10_bbq_jill2_event18 with dissolve
ji "Haha, I can only imagine."
ji "What else will you change my mind on, I wonder."
scene ep10_bbq_jill2_event19 with dissolve
mc "Hm... Maybe music?"
scene ep10_bbq_jill2_event18 with dissolve
ji "Will you make me hate music?"
scene ep10_bbq_jill2_event19 with dissolve
mc "No, I will make you like bands I love. And I know which one to start with..."
mc "The same band your sister liked."
scene ep10_bbq_jill2_event21 with dissolve
ji "You're pushing all the right buttons now, aren't you?"
scene ep10_bbq_jill2_event22 with dissolve
mc "I can see it in your eyes. I know you want to like it."
scene ep10_bbq_jill2_event23 with dissolve
ji "The last time I heard it was when I was young, and back then it didn't sound much like music to me."
ji "They were kind of screaming and played fast and aggressive."
scene ep10_bbq_jill2_event22 with dissolve
mc "You're musically gifted. I'm sure if you listened to the melodies of the instruments and vocals you will hear what I hear."
scene ep10_bbq_jill2_event21 with dissolve
ji "Ok. I'll be open-minded then. You're welcome to change my mind."
scene ep10_bbq_jill2_event24 with dissolve
mc "Maybe I should play the music through proper speakers...but I kinda wanna see you react to it now."
scene ep10_bbq_jill2_event25 with dissolve
ji "Go ahead. Pick their best song."
scene ep10_bbq_jill2_event24 with dissolve
mc "Their best song!? You can't possibly ask me to pick one ShitFaced song. They have countless hits!"
scene ep10_bbq_jill2_event25 with dissolve
ji "No pressure, [name]. But you only get one chance to change my mind."
scene ep10_bbq_jill2_event26 with dissolve
mc "Haha, you're so enjoying this."
scene ep10_bbq_jill2_event24 with dissolve
mc "Ok. This is one of my favorites. Make sure you really listen to it."
mc "Try to love it, ok?"
stop music fadeout 3
scene ep10_bbq_jill2_event25 with dissolve
ji "I will try."
play music "music/ep_interlude/licensed_music/track105.mp3"
scene ep10_bbq_jill2_event27 with dissolve
$ renpy.pause()
scene ep10_bbq_jill2_event28 with dissolve
$ renpy.pause()
scene ep10_bbq_jill2_event29 with dissolve
$ renpy.pause()
scene ep10_bbq_jill2_event30 with dissolve
mc "What do you think?"
scene ep10_bbq_jill2_event31 with dissolve
ji "Did my sister listen to this?"
scene ep10_bbq_jill2_event30 with dissolve
mc "It's from the album of her poster, so odds are she did."
scene ep10_bbq_jill2_event31 with dissolve
ji "It's different than I remember. It's...aggressive, but still catchy."
ji "And you're right, there are some melodies in there."
scene ep10_bbq_jill2_event32 with dissolve
ji "Hahaha, this is so Lana."
scene ep10_bbq_jill2_event33 with dissolve
mc "Sometimes it takes a while to get into it, but keep listening to it and it will grow on you."
mc "That's how I started with some bands that I didn't think I would like. And eventually, I became a fan of them."
mc "I know it's different than the classical music you enjoy, but maybe you would love this music if you start listening more to it."
scene ep10_bbq_jill2_event34 with dissolve
ji "Not everything has to be Chopin."
ji "Thank you for showing me. I think I will have to give it a proper listening to another day."
scene ep10_bbq_jill2_event33 with dissolve
mc "That's all I'm asking."
stop music fadeout 3
scene ep10_bbq_jill2_event35 with dissolve
ji "*{i}Smack{/i}*"
scene ep10_bbq_jill2_event36 with dissolve
$ renpy.pause()
$ renpy.music.stop(channel="sfx3", fadeout=3)

$ task_list[3] = ""

if ep10_shroom_choice == "DIK":
    $ new_bio("Jill", "Jill was concerned about me when she realized I had eaten a shroom. She asked me not to do drugs again.")
if ep10_pp_activity == 0:
    if ep10_shroom_choice != "DIK":
        $ task_list[5] = "Play Beer Pong"
    else:
        $ task_list[5] = "Throw the white sphere"
    $ event_list.append("ep10_bbq_bpj_event_label")
    $ new_bio("Jill", "Jill and I talked about her sister and seasons. I made her listen to some of my - and Lana's - favorite music.")
else:
    $ event_list.append("ep10_bbq_final_phase")
    $ new_bio("Jill", "Jill and I talked about her sister and seasons. I made her listen to some of my - and Lana's - favorite music.")
    
if "ep10_bbq_bps_event_label" in event_list or "ep10_bbq_bpjo_event_label" in event_list or "ep10_bbq_bpj_event_label" in event_list:
    if ep10_shroom_choice != "DIK":
        $ task_list[5] = "Play Beer Pong"
    else:
        $ task_list[5] = "Throw the white sphere"
        
if ("ep10_bbq_bps_event_label" in event_list or "ep10_bbq_bpjo_event_label" in event_list or "ep10_bbq_bpj_event_label" in event_list) and "ep10_bbq_2dg_event_label" in event_list:
    if ep10_shroom_choice != "DIK":
        $ task_list[5] = "Play Beer Pong\nGo to the forest"
    else:
        $ task_list[5] = "Throw the white sphere\nGo to the forest"
        
if ("ep10_bbq_bps_event_label" not in event_list and "ep10_bbq_bpjo_event_label" not in event_list and "ep10_bbq_bpj_event_label" not in event_list) and "ep10_bbq_2dg_event_label" in event_list:
    if ep10_shroom_choice != "DIK":
        $ task_list[5] = "Go to the forest"
    else:
        $ task_list[5] = "Go to the forest"
$ updateTaskList()
$ mphone_next_song()
jump endEvent

label ep10_bbq_jb_event_label:
$ guideSuggestedPage = 136
scene ep10_bbq_jb_event1 with dissolve
jb "[name]!"
if ep10_shroom_choice == "DIK":
    scene ep10_bbq_jb_event2 with dissolve
    mc "JB! How are you?"
else:
    scene ep10_bbq_jb_event3 with dissolve
    mc "How is the trip?"
scene ep10_bbq_jb_event4 with dissolve
jb "I gave a fork a staredown for like an hour."
jb "Why do forks come with different numbers of prongs? And if you have many prongs and they meld together, do you know what you get?"
jb "A spoon, [name]! It becomes a spoon!"
scene ep10_bbq_jb_event5 with dissolve
if ep10_shroom_choice == "DIK":
    mc "Whoa!"
else:
    mc "That's quite the epiphany."
scene ep10_bbq_jb_event6 with dissolve
jb "Right!?"
jb "Have you seen Elena? I gotta tell her about it."
scene ep10_bbq_jb_event7 with dissolve
mc "She's somewhere around here."
if not ep8_elena_shot:
    scene ep10_bbq_jb_event6 with dissolve
    jb "I gotta find her! She needs to know about this."
else:
    scene ep10_bbq_jb_event6 with dissolve
    jb "Elena tells me you two are close."
    jb "I wanted to say how happy that makes me to hear."
    scene ep10_bbq_jb_event7 with dissolve
    mc "Yeah, we kinda are. She's such a fun person to be around."
    scene ep10_bbq_jb_event6 with dissolve
    jb "She is fun! And caring. And sexy."
    jb "I think I got horny talking to you about her."
    scene ep10_bbq_jb_event7 with dissolve
    mc "Go do something about it, bro. I can't help you with that."
    if ep10_shroom_choice == "DIK":
        mc "Hell, I have so many quests to go on that I don't know where to start."
    scene ep10_bbq_jb_event8 with dissolve
    jb "On a scale of one to ten. One being the highest. How sexy is Elena?"
    scene ep10_bbq_jb_event7 with dissolve
    menu:
        "[mod_gr]She's hot":
            $ ep10_jb_elena_hot = True
            if ep10_shroom_choice == "DIK":
                mc "Like 500! Very hot!"
            else:
                mc "Oh, she's a total one if one is the highest."
            scene ep10_bbq_jb_event8 with dissolve
            jb "Yeah! Don't take offense now, but I gotta ask you this."
            jb "Would you ever fuck someone like Elena?"
            scene ep10_bbq_jb_event7 with dissolve
            mc "If both of us were single, I can't see why I wouldn't."
            scene ep10_bbq_jb_event8 with dissolve
            jb "And what if she's not?"
        "She's not my type":
            $ ep10_jb_elena_hot = False
            if ep10_shroom_choice == "DIK":
                scene ep10_bbq_jb_event13 with dissolve
                mc "..."
            else:
                mc "She's a great girl and objectively she's good-looking, but she's not my type."
            scene ep10_bbq_jb_event9 with dissolve
            jb "Aw... You don't like her that way?"
            scene ep10_bbq_jb_event10 with dissolve
            mc "Does it bum you out?"
            scene ep10_bbq_jb_event9 with dissolve
            jb "A bit. I was gonna ask you if you'd like to do something with us."
    scene ep10_bbq_jb_event7 with dissolve
    mc "What are you asking me?"
    scene ep10_bbq_jb_event11 with dissolve
    jb "Forget it. It's the mushroom talking."
    jb "But if you think it would be fun, there could be ways to make it happen."
    scene ep10_bbq_jb_event7 with dissolve
    if branchAlone:
        mc "I wouldn't fuck your girlfriend, John Boy."
    else:
        mc "I wouldn't fuck your girlfriend, John Boy. Also, I'm not available."
    scene ep10_bbq_jb_event6 with dissolve
    jb "Hey! Don't say no before you think some more about it."
    jb "Sharing is caring, isn't it? And something about picturing her taking a huge cock like yours makes me puff up."
    scene ep10_bbq_jb_event7 with dissolve
    mc "Uh..."
    scene ep10_bbq_jb_event12 with dissolve
    jb "Shh... Think about it."
    $ new_bio("John Boy", "John Boy asked me if I found Elena hot and floated the idea of having a threesome with her, or maybe he just wanted me to fuck her. I don't know what it was, but it was weird.")

$ task_list[4] = ""
if not "ep10_bbq_z_event_label" in event_list:
    $ event_list.append("ep10_bbq_z2_event_label")
    if ep10_shroom_choice == "DIK":
        $ task_list[4] = "Talk to the blueberry"
    else:
        $ task_list[4] = "Talk to Zoey"
$ updateTaskList()

jump endEvent

label ep10_bbq_nick_event_label:
$ guideSuggestedPage = 137
scene ep10_bbq_nick_event1 with dissolve
if ep10_shroom_choice == "DIK":
    mc "I can see the rainbow now. Are you the leprechaun?"
    scene ep10_bbq_nick_event2 with dissolve
    ni "Is the mushroom affecting you too?"
    scene ep10_bbq_nick_event3 with dissolve
    mc "It's such an unpleasant effect. Closing my eyes doesn't help."
    scene ep10_bbq_nick_event2 with dissolve
    ni "Yeah. I'm drinking beers to numb the effect."
    ni "Sitting down and talking might help. That's why I'm still here. I'm too scared to move."
    scene ep10_bbq_nick_event3 with dissolve
    mc "Ok."
    scene ep10_bbq_nick_event4 with dissolve
    ni "Sit down on the bench, [name]."
    scene ep10_bbq_nick_event5 with dissolve
    mc "Nick, please help me."
    scene ep10_bbq_nick_event6 with dissolve
    ni "Let's talk about something... Try to focus, [name]."
    ni "Are you celebrating Thanksgiving tomorrow?"
    scene ep10_bbq_nick_event7 with dissolve
    mc "No, I've got plans. I told Dad we would celebrate it this weekend. You?"
    scene ep10_bbq_nick_event6 with dissolve
    ni "Yeah, I'm going back home to see my family - Mom, Dad and my sis."
    scene ep10_bbq_nick_event8 with dissolve
    ni "It will be fun seeing them, and I don't wanna waste it by showing up with a hangover... I hope the mushroom doesn't have any lasting effects."
    scene ep10_bbq_nick_event7 with dissolve
    mc "That mushroom is already inside of me, making its way down to my intestines as we speak."
    mc "I hope it will be over by tomorrow..."
    scene ep10_bbq_nick_event9 with dissolve
    ni "Tommy said it would be over in a few hours."
    scene ep10_bbq_nick_event7 with dissolve
    mc "Good... Good."
    scene ep10_bbq_nick_event9 with dissolve
    ni "Not that I'd know, since I'm probably too drunk."
    ni "So, what's important enough for you to postpone Thanksgiving?"
    scene ep10_bbq_nick_event7 with dissolve
    mc "It's a secret. I can't talk about it."
    scene ep10_bbq_nick_event9 with dissolve
    ni "A secret, huh? Don't you wanna share stuff with me?"
    scene ep10_bbq_nick_event7 with dissolve
    mc "I bet even you have secrets."
    scene ep10_bbq_nick_event8 with dissolve
    ni "Well, who hasn't? I've been feeling like shit lately."
    scene ep10_bbq_nick_event18 with dissolve
    mc "How come?"
    scene ep10_bbq_nick_event10 with dissolve
    ni "..."
    scene ep10_bbq_nick_event8 with dissolve
    jump ep10_bbq_nick_event2_label
else:
    mc "Are you still drinking beer?"
    scene ep10_bbq_nick_event6 with dissolve
    ni "Yeah. I've been drinking to numb the effect of the mushroom."
    ni "But...fuck...I promised myself I wouldn't overdo it tonight."
    scene ep10_bbq_nick_event7 with dissolve
    mc "Big day tomorrow?"
    scene ep10_bbq_nick_event6 with dissolve
    ni "I'm going back home to see my family - Mom, Dad and my sis."
    scene ep10_bbq_nick_event7 with dissolve
    mc "That's nice."
    scene ep10_bbq_nick_event8 with dissolve
    ni "It will be fun seeing them, and I don't wanna waste it by showing up with a hangover... I hope the mushroom doesn't have any lasting effects."
    scene ep10_bbq_nick_event7 with dissolve
    mc "When you put it like that, I should take it easy tonight too."
    scene ep10_bbq_nick_event9 with dissolve
    ni "Yeah? Big family Thanksgiving?"
    scene ep10_bbq_nick_event7 with dissolve
    mc "Nah, I'll be back home to celebrate it with Dad this weekend. But I have something else tomorrow."
    mc "I'm helping some friends with a thing."
    scene ep10_bbq_nick_event9 with dissolve
    ni "Must be important if you're doing it at Thanksgiving."
    scene ep10_bbq_nick_event7 with dissolve
    mc "Sorry, I can't talk about it. It's personal stuff and it's not my thing to tell someone about."
    scene ep10_bbq_nick_event9 with dissolve
    ni "A secret, huh? Don't you wanna share stuff with me?"
    scene ep10_bbq_nick_event7 with dissolve
    mc "I bet even you have secrets."
    scene ep10_bbq_nick_event8 with dissolve
    ni "Well, who hasn't? I've been feeling like shit lately."
    scene ep10_bbq_nick_event7 with dissolve
    mc "How come?"
    scene ep10_bbq_nick_event8 with dissolve
    label ep10_bbq_nick_event2_label:
    ni "Let's just say that I've been in love with a girl who doesn't even see me for the last couple of years."
    scene ep10_bbq_nick_event11 with dissolve
    mc "Is that a secret?"
    scene ep10_bbq_nick_event12 with dissolve
    ni "She's in a relationship with someone and there's nothing I can do about it."
    scene ep10_bbq_nick_event11 with dissolve
    mc "Ouch... I've had crushes like that too. It sucks."
    mc "You haven't managed to move on after two years?"
    scene ep10_bbq_nick_event8 with dissolve
    ni "It's not simple to do that when she's constantly around."
    ni "Recently, I crossed a line I didn't think I would cross."
    ni "She confided in me and one thing led to another..."
    scene ep10_bbq_nick_event12 with dissolve
    ni "At Halloween, I ended up in bed with her. We were both drunk and part of me has wanted to do that since the beginning, but...fuck..."
    scene ep10_bbq_nick_event11 with dissolve
    mc "(Is he...talking about Heather?)"
    mc "Dude... Is it Heather?"
    scene ep10_bbq_nick_event16 with dissolve
    ni "Fuck... Me and my stupid mouth."
    scene ep10_bbq_nick_event17 with dissolve
    mc "It is Heather... Are you in love with her!?"
    scene ep10_bbq_nick_event16 with dissolve
    ni "From the first moment I saw her. Even before she got together with Tommy."
    ni "And now that I did this with her... I..."
    scene ep10_bbq_nick_event12 with dissolve
    ni "How can I go on pretending that I didn't do it around him?"
    scene ep10_bbq_nick_event11 with dissolve
    if ep9_heather_lewd == 2:
        menu:
            "I did it too":
                $ ep10_nick_response = 4
                mc "Since you're sharing this secret with me, I'll do the same with you."
                mc "Because I can't take it back either..."
                scene ep10_bbq_nick_event13 with dissolve
                ni "You had sex with Heather too?"
                scene ep10_bbq_nick_event11 with dissolve
                mc "Almost. She gave me a blowjob and a titjob at Halloween in Leon's room."
                mc "She did it to get back at Tommy for fucking girls without checking with her first."
                scene ep10_bbq_nick_event14 with dissolve
                ni "Yes! That's exactly it."
                ni "But she told me that after we already fucked."
                scene ep10_bbq_nick_event8 with dissolve
                ni "She came up to me and was upset about something. We sat down and talked, and she poured her heart out."
                ni "I told her how I felt for her and we started making out."
                scene ep10_bbq_nick_event12 with dissolve
                ni "I took her back up to my room and we had sex. She even fell asleep in my arms after."
                ni "And when we woke up, she felt so much remorse and told me she did it because of how Tommy's been treating her."
                ni "She said that night would be our secret, but I don't think she can keep that. She regretted everything and even cried before she left."
                scene ep10_bbq_nick_event8 with dissolve
                ni "I've felt horrible since. She fucking used me..."
                ni "Having sex with her is something I've dreamt of, but it ended up being this big disappointment."
                if ep10_shroom_choice == "DIK":
                    scene ep10_bbq_nick_event19 with dissolve
                else:
                    scene ep10_bbq_nick_event20 with dissolve
                mc "I feel you."
                scene ep10_bbq_nick_event12 with dissolve
                ni "Are you going to tell Tommy what you did?"
                scene ep10_bbq_nick_event11 with dissolve
                mc "He'd kill me... But I can't lie, I feel shitty about it."
                scene ep10_bbq_nick_event15 with dissolve
                ni "Well, no one else knows... At least, that's good."
                scene ep10_bbq_nick_event11 with dissolve
                mc "John Boy kinda knows that something's up. He saw Heather leave that morning, but he wasn't sure if it was from your room or Jacob's."
                if ep10_shroom_choice == "DIK":
                    mc "I don't think I should decide this when I'm tripping. I'm not entirely sure I'm having this conversation with you."
                else:
                    mc "I fear this isn't something we'll be able to hide from Tommy... So, maybe it's best that we tell him together."
                    mc "But it's not a decision I will make when I'm drunk and Tommy's over there hallucinating."
                scene ep10_bbq_nick_event8 with dissolve
                ni "Fuck... I don't wanna tell him. I shouldn't even have told you about this."
                $ new_bio("Nick", "Nick told me he fucked Heather and that he's in love with her. I told him that she used me at Halloween.")
            "Don't tell Tommy":
                jump ep10_bbq_nick_choice1_label
            "You need to tell Tommy":
                jump ep10_bbq_nick_choice2_label
    else:
        if ep9_heather_lewd == -1:
            menu:
                "Don't tell Tommy":
                    jump ep10_bbq_nick_choice1_label
                "You need to tell Tommy":
                    jump ep10_bbq_nick_choice2_label
        menu:
            "She tried to use me too":
                $ ep10_nick_response = 1
                mc "She tried to use me at our Halloween party too. We had a pretty good talk about it in Leon's room."
                mc "Well, it was clear that she wanted to do more than just talk."
                mc "And she wanted to do it to get back at Tommy for fucking girls without checking with her first."
                scene ep10_bbq_nick_event14 with dissolve
                ni "Yes! That's exactly it."
                ni "But she told me that after we already fucked."
                scene ep10_bbq_nick_event8 with dissolve
                ni "She came up to me and was upset about something. We sat down and talked, and she poured her heart out."
                ni "I told her how I felt for her and we started making out."
                scene ep10_bbq_nick_event12 with dissolve
                ni "I took her back up to my room and we had sex. She even fell asleep in my arms after."
                ni "And when we woke up, she felt so much remorse and told me she did it because of how Tommy's been treating her."
                ni "She said that night would be our secret, but I don't think she can keep that. She regretted everything and even cried before she left."
                scene ep10_bbq_nick_event8 with dissolve
                ni "I've felt horrible since. She fucking used me..."
                ni "Having sex with her is something I've dreamt of, but it ended up being this big disappointment."
                if ep10_shroom_choice == "DIK":
                    scene ep10_bbq_nick_event19 with dissolve
                else:
                    scene ep10_bbq_nick_event20 with dissolve
                mc "I feel you."
                scene ep10_bbq_nick_event12 with dissolve
                ni "I can't tell Tommy what I did... He'd kill me."
                scene ep10_bbq_nick_event11 with dissolve
                if ep10_shroom_choice == "DIK":
                    mc "Well, I can't make that choice for you."
                else:
                    mc "Well, I can't make that choice for you. And I can only imagine how pissed off he will get if you tell him."
                scene ep10_bbq_nick_event16 with dissolve
                ni "Fuck... I shouldn't even have told you about this."
                scene ep10_bbq_nick_event11 with dissolve
                mc "John Boy kinda knows that something's up. He saw Heather leave that morning, but he wasn't sure if it was from your room or Jacob's."
                mc "I fear this isn't something you'll be able to hide from Tommy... So, maybe it's best that you tell him."
                if ep10_shroom_choice == "DIK":
                    mc "But it's not a decision you should make when everyone is tripping."
                    mc "I'm not entirely sure I'm having this conversation with you."
                else:
                    mc "But it's not a decision you should make when you're drunk and tripping, and Tommy's over there hallucinating."
                $ new_bio("Nick", "Nick told me he fucked Heather and that he's in love with her. I told him that she tried to use me at Halloween.")
            "Don't tell Tommy":
                label ep10_bbq_nick_choice1_label:
                $ ep10_nick_response = 2
                mc "You can't tell Tommy about that. He would kill you."
                scene ep10_bbq_nick_event12 with dissolve
                ni "I know! He'd at least beat the living shit out of me."
                scene ep10_bbq_nick_event11 with dissolve
                mc "Maybe Heather will tell him, maybe she won't. You should talk to her about it."
                scene ep10_bbq_nick_event16 with dissolve
                ni "I did, but...fuck. I shouldn't have told you about this."
                scene ep10_bbq_nick_event17 with dissolve
                mc "I won't tell Tommy. But, damn..."
                $ new_bio("Nick", "Nick told me he fucked Heather and that he's in love with her. I advised him not to tell Tommy about it.")
            "You need to tell Tommy":
                label ep10_bbq_nick_choice2_label:
                $ ep10_nick_response = 3
                mc "You need to tell Tommy about this."
                if ep9_heather_lewd == 2:
                    mc "(And I probably should too... Fuck...)"
                scene ep10_bbq_nick_event12 with dissolve
                ni "Are you crazy!? He'd beat the living shit out of me."
                scene ep10_bbq_nick_event11 with dissolve
                mc "What if he finds this out from Heather? That would make it worse."
                scene ep10_bbq_nick_event8 with dissolve
                ni "*{i}Sigh{/i}* Yeah, but I can't tell him..."
                ni "Fuck... I shouldn't even have told you about this."
                scene ep10_bbq_nick_event17 with dissolve
                mc "I won't tell Tommy, if that's what you're worried about. But damn..."
                $ new_bio("Nick", "Nick told me he fucked Heather and that he's in love with her. I advised him to tell Tommy about it.")
$ task_list[3] = ""
$ event_list.append("nick_block")
if branchJill and not "ep10_bbq_guitar_j_event_label" in event_list:
    if not "ep10_bbq_jill2_event_label" in event_list:
        $ event_list.append("ep10_bbq_jill2_event_label")
        if ep10_shroom_choice == "DIK":
            $ task_list[3] = "Talk to Rusty"
        else:
            $ task_list[3] = "Talk to Jill"

$ updateTaskList()
jump endEvent

label ep10_bbq_lily_jetty_event_label:
if ep10_shroom_choice == "DIK":
    scene ep10_bbq_lily_jetty_event28 with dissolve
else:
    scene ep10_bbq_lily_jetty_event28b with dissolve
ly "[name]. Let's go. I need you."
if ep10_shroom_choice == "DIK":
    scene ep10_bbq_lily_jetty_event30 with dissolve
    mc "The entire kingdom needs me, Lily. I need to find the fairest maiden in town and something to beat her over the head with."
    scene ep10_bbq_lily_jetty_event31 with dissolve
    ly "Come. I'll help you with that."
else:
    scene ep10_bbq_lily_jetty_event29 with dissolve
    mc "Are you gonna be ok, Leon?"
    le "These cups are fucking magical!"
    scene ep10_bbq_lily_jetty_event30 with dissolve
    mc "Where are we going?"
    scene ep10_bbq_lily_jetty_event31 with dissolve
    ly "It's a no-questions-asked kinda thing."
scene ep10_bbq_lily_jetty_event32 with dissolve
$ renpy.pause()
scene ep10_bbq_lily_jetty_event33 with dissolve
$ renpy.pause()
stop music fadeout 3
if branchAlone and ep8_quinn_lewd:
    scene ep10_bbq_lily_jetty_event34 with dissolve
else:
    scene ep10_bbq_lily_jetty_event35 with dissolve
$ renpy.pause()

play music "music/ep4/guitar_melancholy.mp3"
if ep10_shroom_choice == "DIK":
    scene ep10_bbq_lily_jetty_event1 with dissolve
    ly "How are you enjoying the mushroom, cutie?"
    scene ep10_bbq_lily_jetty_event2 with dissolve
    mc "I'm not enjoying this at all, Lily. Will it pass soon? I keep seeing weird things."
    scene ep10_bbq_lily_jetty_event3 with dissolve
    ly "It will be over soon. It usually lasts a few hours."
    ly "Did you eat a lot of food before having it?"
    scene ep10_bbq_lily_jetty_event2 with dissolve
    mc "Yeah. Was I not supposed to?"
    scene ep10_bbq_lily_jetty_event3 with dissolve
    ly "You did good. It can get even worse on an empty stomach."
    scene ep10_bbq_lily_jetty_event2 with dissolve
    mc "I don't see the appeal of this at all."
    scene ep10_bbq_lily_jetty_event4 with dissolve
    ly "It depends on what state of mind you're in. Maybe you're not feeling that well to begin with?"
    scene ep10_bbq_lily_jetty_event2 with dissolve
    mc "I'm doing ok, but I've had a lot of thoughts lately. And some stress here and there."
    scene ep10_bbq_lily_jetty_event5 with dissolve
    ly "Try not to think too much about it now."
else:
    scene ep10_bbq_lily_jetty_event1 with dissolve
    ly "Why didn't you have a mushroom, cutie?"
    scene ep10_bbq_lily_jetty_event6 with dissolve
    mc "I was scared to try it, and seeing how some of my brothers react to it, I believe it was justified."
    mc "Beer seems like the more reliable option. You always know what effect you'll get, unless you overdo it."
    scene ep10_bbq_lily_jetty_event5 with dissolve
    ly "It would have been fun to watch you tripping, but it's ok."
    ly "I respect you for saying no to something you don't want."
scene ep10_bbq_lily_jetty_event7 with dissolve
mc "Are you girls having a nice party?"
scene ep10_bbq_lily_jetty_event8 with dissolve
ly "It's not my jam, but it's a party. And I like that it's more chill than usual."
ly "I've been meaning to kick back and relax some, and tonight I can."
scene ep10_bbq_lily_jetty_event7 with dissolve
mc "Did you have a lot on your schedule?"
scene ep10_bbq_lily_jetty_event8 with dissolve
ly "Yeah. I've worked extra when I could. It's getting hard to keep up with both college and the work, on top of everything else."
ly "I was hoping I would manage it better than I am, but it's starting to get to me."
scene ep10_bbq_lily_jetty_event7 with dissolve
mc "Do you have to work as much as you do?"
scene ep10_bbq_lily_jetty_event9 with dissolve
ly "I don't have to, but it's an opportunity of a lifetime for me, so I do it."
scene ep10_bbq_lily_jetty_event7 with dissolve
mc "You're ambitious, I gotta give you that."
scene ep10_bbq_lily_jetty_event8 with dissolve
ly "Like you aren't? I've heard how hard you've been busting your ass with the DIKs."
if ep7_pinkrose:
    ly "And you're also working extra cleaning the club."
else:
    ly "And you're working extra too, right?"
scene ep10_bbq_lily_jetty_event7 with dissolve
mc "Yeah, but it's not as much as you do and I don't make nearly as much, I'm guessing."
scene ep10_bbq_lily_jetty_event8 with dissolve
ly "Do you wanna know how much I make?"
scene ep10_bbq_lily_jetty_event7 with dissolve
mc "Would you tell me?"
scene ep10_bbq_lily_jetty_event9 with dissolve
ly "If you promise not to tell anyone."
scene ep10_bbq_lily_jetty_event7 with dissolve
mc "Sure."
scene ep10_bbq_lily_jetty_event9 with dissolve
ly "It varies a lot, so it's hard to say how much it will be each month."
ly "But on an average night, I make somewhere between $300 to $700."
scene ep10_bbq_lily_jetty_event7 with dissolve
mc "For one night!?"
scene ep10_bbq_lily_jetty_event8 with dissolve
ly "There are slow nights too, when it's less."
ly "But if it's a very good night, with specials or if there's a big event happening like a bachelor's party, it gets better."
ly "I once cleared nearly $3000."
scene ep10_bbq_lily_jetty_event7 with dissolve
mc "Why the hell do you even wanna be in college?"
scene ep10_bbq_lily_jetty_event10 with dissolve
ly "Haha! Right?"
scene ep10_bbq_lily_jetty_event7 with dissolve
mc "For real... Why?"
scene ep10_bbq_lily_jetty_event9 with dissolve
ly "Because I have other goals in life than earning money."
ly "You don't choose to study healthcare if you don't."
scene ep10_bbq_lily_jetty_event7 with dissolve
mc "What goals?"
scene ep10_bbq_lily_jetty_event9 with dissolve
ly "I have some stuff to prove. To my parents. To everyone."
scene ep10_bbq_lily_jetty_event7 with dissolve
mc "Wanna talk about it?"
scene ep10_bbq_lily_jetty_event11 with dissolve
ly "..."
scene ep10_bbq_lily_jetty_event12 with dissolve
ly "No."
ly "But I think it's cool that you're interested. No one asks me about it."
scene ep10_bbq_lily_jetty_event13 with dissolve
mc "I don't know if those kind of talks are part of the whole rolling thing, but I wanna let you know that I don't mind them."
scene ep10_bbq_lily_jetty_event14 with dissolve
ly "[name], stop it."
scene ep10_bbq_lily_jetty_event13 with dissolve
mc "Stop what?"
scene ep10_bbq_lily_jetty_event14 with dissolve
ly "You're trying to turn this into something more meaningful than the shallow deal it is."
ly "I'm not comfortable with that."
scene ep10_bbq_lily_jetty_event13 with dissolve
mc "I don't see why it only has to be shallow. Don't you want to get to know me better too?"
scene ep10_bbq_lily_jetty_event15 with dissolve
ly "You're so not playing by the rules."
scene ep10_bbq_lily_jetty_event13 with dissolve
mc "The rules aren't clear, Lily. I thought we made our own rules as we go?"
mc "There's nothing wrong with getting to know each other."
scene ep10_bbq_lily_jetty_event15 with dissolve
ly "I don't want you to fall for me. Is that clear enough?"
scene ep10_bbq_lily_jetty_event13 with dissolve
mc "Yeah, I get it. And I won't."
scene ep10_bbq_lily_jetty_event14 with dissolve
ly "So, don't do those things."
scene ep10_bbq_lily_jetty_event13 with dissolve
mc "I can talk about these things without falling for you. Maybe it's you who can't?"
scene ep10_bbq_lily_jetty_event15 with dissolve
ly "I'm a stripper, [name]."
ly "I do things without falling for people all the time."
scene ep10_bbq_lily_jetty_event13 with dissolve
mc "All right, you win."
scene ep10_bbq_lily_jetty_event14 with dissolve
ly "[name]..."
ly "I can only do the things I do {b}because{/b} I haven't fallen for someone."
ly "Do you get it?"
scene ep10_bbq_lily_jetty_event13 with dissolve
mc "Oh..."
scene ep10_bbq_lily_jetty_event14 with dissolve
ly "Yeah."
scene ep10_bbq_lily_jetty_event16 with dissolve
$ renpy.pause()
scene ep10_bbq_lily_jetty_event17 with dissolve
$ renpy.pause()
scene ep10_bbq_lily_jetty_event18 with dissolve
mc "I'm not sure what to say now."
scene ep10_bbq_lily_jetty_event19 with dissolve
ly "You don't have to say anything. This wasn't why I grabbed you for this walk."
ly "I wanted to flaunt you in front of the other girls and give you a blowjob as thanks or something."
scene ep10_bbq_lily_jetty_event20 with dissolve
mc "Sorry, if I ruined it. I wanted to get to know you more."
scene ep10_bbq_lily_jetty_event19 with dissolve
ly "Yeah, I can clearly see that you want that. And it's not a bad thing, it's the opposite."
ly "I want us to be on the same page if this is going to work."
scene ep10_bbq_lily_jetty_event20 with dissolve
mc "I'll try to be more aloof with you, if that's what you need."
scene ep10_bbq_lily_jetty_event19 with dissolve
ly "Yeah, it is. Thanks..."
scene ep10_bbq_lily_jetty_event20 with dissolve
mc "Well... I guess there's only one way to fix this."
scene ep10_bbq_lily_jetty_event19 with dissolve
ly "How?"
scene ep10_bbq_lily_jetty_event21 with dissolve
mc "By sticking to your plan."
mc "I'm gonna shut up and let you suck my cock."
scene ep10_bbq_lily_jetty_event22 with dissolve
ly "Hahaha!"
ly "Ok, you got me with that one."

label ep10_lily_lewd_label:
if _in_replay:
    if persistent.name == None:
        $ name = "MC"
    else:
        $ name = persistent.name
    $ ep10_shroom_choice = "DIK"
    play music "music/ep4/guitar_melancholy.mp3"
hide screen new_phone_screen
scene ep10_bbq_lily_jetty_event23 with dissolve
mc "Wanna head back there?"
scene ep10_bbq_lily_jetty_event24 with dissolve
ly "Yeah."
scene ep10_bbq_lily_jetty_event25 with dissolve
ly "I mean...unless?"
scene ep10_bbq_lily_jetty_event26 with dissolve
mc "You don't have to, I wanted to make you laugh."
scene ep10_bbq_lily_jetty_event25 with dissolve
ly "Yeah, but I wasn't joking when I said I was gonna do it."
stop music fadeout 3
scene ep10_bbq_lily_jetty_event27 with dissolve
mc "If it doesn't break some rule...why not?"

play music "music/ep3/dc_love_go_go.mp3"
scene ep10_lily_lewd1 with dissolve
mc "Now I feel creepy for making that joke."
scene ep10_lily_lewd2 with dissolve
ly "That's good. It made me like you less."
scene ep10_lily_lewd3 with dissolve
mc "Oh? Yay, I guess."
scene ep10_lily_lewd2 with dissolve
ly "You're awesome, [name]."
scene anim_lily_hj_ep10 with dissolve
ly "And this thing you're rocking is awesome too."
ly "Oh. A heads up... Becky wants to fuck you bad."
mc "Huh? Becky?"
ly "Yep. You've gotten popular from that dick pic and if there's something that girl craves it's attention."
mc "Oh... I don't know what I feel about that."
pause
scene ep10_lily_lewd4 with dissolve
ly "Do what you want with it. But wear a rubber with her if you do."
ly "I hear she gets around."
scene anim_lily_bj1_ep10 with dissolve
ly "*{i}Suck suck{/i}* Mmm..."
pause
scene anim_lily_bj2_ep10 with dissolve
pause
scene ep10_lily_lewd5 with dissolve
mc "Fuck, that's good..."

scene ep10_lily_lewd6 with dissolve
ly "Up you go. I'm gonna get you off good."

scene anim_lily_bj3_ep10 with dissolve
ly "*{i}Suck suck{/i}*"
pause
scene anim_lily_bj4_ep10 with dissolve
pause

scene anim_lily_bj5_ep10 with dissolve
pause

scene anim_lily_bj4_ep10 with dissolve
ly "*{i}Suck suck{/i}* Are you close?"
mc "Yeah... Very."
mc "Inside or outside?"
ly "King's choice."
menu:
    "In mouth":
        mc "I'd love to cum in your mouth, Lily."
        scene bg anim_lily_cum_ep10 movie with vpunch
        pause
        menu:
            "Spit out":
                mc "You can spit it out."
                scene ep10_lily_lewd11 with dissolve
                ly "*{i}Spits{/i}*"
                scene ep10_lily_lewd10 with dissolve
                $ renpy.pause()
            "Swallow it":
                scene ep10_lily_lewd7 with dissolve
                ly "*{i}Gulp{/i}*"
                scene ep10_lily_lewd8 with dissolve
                ly "*{i}Lick lick{/i}*"
                scene ep10_lily_lewd9 with dissolve
                ly "Ah... That was a mouthful."
    "Facial":
        mc "I'm gonna ruin your makeup with my choice..."
        ly "Don't worry about it."
        scene anim_lily_cum2_ep10 with dissolve
        pause
        scene ep10_lily_lewd12 with dissolve
        mc "Fuck, that's hot..."
        scene ep10_lily_lewd13 with dissolve
        ly "You know it, king."

scene ep10_lily_lewd14 with dissolve
mc "Thanks for that... It was relaxing. "
scene ep10_lily_lewd16 with dissolve
if ep10_shroom_choice == "DIK":
    ly "I think that mushroom is wearing off. You seem to be yourself."
    scene ep10_lily_lewd15 with dissolve
    mc "It comes and goes. But I feel it more when I stand up."
    mc "Maybe its effect is less than before, but my vision is still not 100%%."
    stop music fadeout 3
    scene ep10_lily_lewd16 with dissolve
    ly "Give it another hour, [name]."
else:
    ly "Do you think your brothers are back to normal yet?"
    scene ep10_lily_lewd15 with dissolve
    mc "I hope so. That way I can stop worrying about them."
    stop music fadeout 3
    scene ep10_lily_lewd16 with dissolve
    ly "Give it another hour and I'm sure they'll feel better."

$ renpy.end_replay()
$ persistent.ep10_lewd_lily = True
$ calcScenes()
$ new_bio("Lily", "Lily explained to me why she didn't want us to do romantic things together and get to know each other at a deeper level. It sounded like she was trying to protect herself from it. I let her give me a blowjob to deflect the talk. It sounds weird, but I think it worked.")
$ mphone_stats_add_girl_s3("lily","Lily gave you a blowjob during the DIKs' Thanksgiving party in episode 10.")
$ mgallery_add_photo("ep10_bbq_lily_pic1")
$ mphone_next_song()
$ task_list[7] = ""
$ updateTaskList()
show screen new_phone_screen
jump endEvent

label ep10_bbq_santa_event_label:
scene ep10_bbq_santa_event1 with dissolve
mc "Huh?"
scene ep10_bbq_santa_event2 with dissolve
mc "Oh no! Santa!!!"
scene ep10_bbq_santa_event3 with dissolve
mc "Send help! Santa's drowning!"
scene ep10_bbq_santa_event4 with vpunch
mc "HERE!!! SANTA!!!"
mc "Get the buoy!"
play sound "sound_effects/water_splash.mp3"
scene ep10_bbq_santa_event5 with dissolve
mc "Santa can't swim..."
mc "Christmas is no more..."
jump endEvent

label ep10_bbq_lroll_event_label:
scene ep10_bbq_lroll_event4 with dissolve
ml "What's up with you and [name]? I didn't know you were together."
scene ep10_bbq_lroll_event1 with dissolve
ly "Don't be gross. We're not together."
scene ep10_bbq_lroll_event5 with dissolve
sa "What's gross about that? He's a great guy."
scene ep10_bbq_lroll_event6 with dissolve
sar "Haven't you seen his stock market value on campus lately?"
sar "It would have been even higher if that dick pic showed his face."
scene ep10_bbq_lroll_event2 with dissolve
ly "I'm not saying he's gross, come on. I'm obviously talking about Mel insinuating it's a relationship. That's so not what it is."
scene ep10_bbq_lroll_event6 with dissolve
sar "Keep telling yourself that, I've seen it with my own eyes. He's got you hooked."
scene ep10_bbq_lroll_event2 with dissolve
ly "Girl, you don't know what you saw. I'm his bitch, and he's my bitch too."
scene ep10_bbq_lroll_event3 with dissolve
ly "That doesn't make it a relationship. I'm more like a HOT ambassador, forging bonds with a DIK one."
ly "It will bring mutual recognition for both our sorority and his fraternity. It's a win-win."
scene ep10_bbq_lroll_event6 with dissolve
sar "Yeah, and you're seen with the current hot guy on campus. I see what you're doing."
scene ep10_bbq_lroll_event2 with dissolve
ly "Keep reaching. I was with him before those posters came to light."
ly "I'm not like Becky, who's only into him because he's popular."
scene ep10_bbq_lroll_event7 with dissolve
bc "Hey! I was into him way before it was cool, too."
if ep7_becky_lewd:
    bc "In fact, he was into {b}me{/b} before it was cool. And I mean all of him was into me. In my mouth. Verbatim!"
else:
    bc "And I'm pretty sure he'd like to be into me too. If I start flirting with him, he's gonna wanna fuck me, I'm sure."
scene ep10_bbq_lroll_event2 with dissolve
ly "Pff! You think that makes me jealous or something? Please..."
ly "He could stick his cock into any of you girls, but he knows who his queen is. He always will."
scene ep10_bbq_lroll_event5 with dissolve
sa "It sounds like you're using him."
scene ep10_bbq_lroll_event8 with dissolve
ly "Not at all. He knows what it is."
jump ep10_bbq_lily_jetty_event_label

label ep10_bbq_jillvar_event_label:
$ guideSuggestedPage = 136
if ep10_shroom_choice == "DIK":
    scene ep10_bbq_jillvar_event1b with dissolve
    mc "Elf girl? I'm surprised to see you here."
else:
    scene ep10_bbq_jillvar_event1 with dissolve
    mc "Jill? I'm surprised to see you here."
if ep10_shroom_choice == "DIK":
    scene ep10_bbq_jillvar_event2b with dissolve
    ji "Um... Hey, [name]. Sage invited me."
else:
    scene ep10_bbq_jillvar_event2 with dissolve
    ji "Hey, [name]. Sage invited me."
ji "I hope you don't think it's weird that I'm spending time with your friends."
if ep10_shroom_choice == "DIK":
    scene ep10_bbq_jillvar_event3b with dissolve
else:
    scene ep10_bbq_jillvar_event3 with dissolve
mc "No, not at all. I think it's great that you girls get along."
mc "It's been a while... How have you been?"
if ep10_shroom_choice == "DIK":
    scene ep10_bbq_jillvar_event2b with dissolve
else:
    scene ep10_bbq_jillvar_event2 with dissolve
ji "I've been doing all right."
ji "However, I believe I owe you an apology."
if ep10_shroom_choice == "DIK":
    scene ep10_bbq_jillvar_event3b with dissolve
else:
    scene ep10_bbq_jillvar_event3 with dissolve
mc "For what?"
if ep10_shroom_choice == "DIK":
    scene ep10_bbq_jillvar_event4b with dissolve
else:
    scene ep10_bbq_jillvar_event4 with dissolve
ji "For not trusting you."
ji "I got mad at Tybalt again and went down to the bar to get some space. And I ran into Trent."
if ep10_shroom_choice == "DIK":
    scene ep10_bbq_jillvar_event6b with dissolve
else:
    scene ep10_bbq_jillvar_event6 with dissolve
mc "I don't know who that is."
if ep10_shroom_choice == "DIK":
    scene ep10_bbq_jillvar_event5b with dissolve
else:
    scene ep10_bbq_jillvar_event5 with dissolve
ji "He's one of Tybalt's closest friends. I'm sure you've seen him."
ji "Anyway, I recalled something that Tybalt told me, back when he blamed you for causing a fire in our mansion."
ji "It involved Trent, and it wasn't flattering, so I asked him about it."
if ep10_shroom_choice == "DIK":
    scene ep10_bbq_jillvar_event4b with dissolve
else:
    scene ep10_bbq_jillvar_event4 with dissolve
ji "It turns out, Tybalt was lying once again and used Trent in his lies. Trent didn't like that."
ji "So, we went upstairs to Tybalt's room to have a chat and the next 20 seconds I would like to have erased from my memory."
if ep10_shroom_choice == "DIK":
    scene ep10_bbq_jillvar_event6b with dissolve
else:
    scene ep10_bbq_jillvar_event6 with dissolve
mc "What happened?"
if ep10_shroom_choice == "DIK":
    scene ep10_bbq_jillvar_event4b with dissolve
else:
    scene ep10_bbq_jillvar_event4 with dissolve
ji "Tybalt and his {i}teeny-tiny Tybbie{/i} were having intercourse with a fruit I'll never be able to enjoy again."
if ep10_shroom_choice == "DIK":
    scene ep10_bbq_jillvar_event5b with dissolve
else:
    scene ep10_bbq_jillvar_event5 with dissolve
ji "And, oh, my stolen underwear - for one - was decorating said fruit."
ji "The underwear you told me he stole. You were right. You were absolutely right."
if ep10_shroom_choice == "DIK":
    scene ep10_bbq_jillvar_event6b with dissolve
else:
    scene ep10_bbq_jillvar_event6 with dissolve
mc "That's so fucking creepy..."
if ep10_shroom_choice == "DIK":
    scene ep10_bbq_jillvar_event5b with dissolve
else:
    scene ep10_bbq_jillvar_event5 with dissolve
ji "It is."
if ep10_shroom_choice == "DIK":
    scene ep10_bbq_jillvar_event6b with dissolve
else:
    scene ep10_bbq_jillvar_event6 with dissolve
mc "What did you guys do?"
if ep10_shroom_choice == "DIK":
    scene ep10_bbq_jillvar_event5b with dissolve
else:
    scene ep10_bbq_jillvar_event5 with dissolve
ji "I kicked him between the legs."
if ep10_shroom_choice == "DIK":
    scene ep10_bbq_jillvar_event6b with dissolve
else:
    scene ep10_bbq_jillvar_event6 with dissolve
mc "Haha! Wait! You what?"
if ep10_shroom_choice == "DIK":
    scene ep10_bbq_jillvar_event4b with dissolve
else:
    scene ep10_bbq_jillvar_event4 with dissolve
ji "It was an impulse. I was so mad! All the lies and then he's doing that from across the hall."
ji "I felt disgusted and humiliated!"
if ep10_shroom_choice == "DIK":
    scene ep10_bbq_jillvar_event5b with dissolve
else:
    scene ep10_bbq_jillvar_event5 with dissolve
ji "I left and he had a heated argument with Trent."
ji "After which Trent came to me and told me he's on my side, if we bring this up to the disciplinary committee."
if ep10_shroom_choice == "DIK":
    scene ep10_bbq_jillvar_event6b with dissolve
else:
    scene ep10_bbq_jillvar_event6 with dissolve
mc "What would happen if you did?"
if ep10_shroom_choice == "DIK":
    scene ep10_bbq_jillvar_event4b with dissolve
else:
    scene ep10_bbq_jillvar_event4 with dissolve
ji "Tybalt would likely be removed as President. His entire world would shatter."
if ep10_shroom_choice == "DIK":
    scene ep10_bbq_jillvar_event6b with dissolve
else:
    scene ep10_bbq_jillvar_event6 with dissolve
menu:
    "You should do it":
        $ ep10_tybalt_mercy = False
        mc "Oh, hell yes! Do that. Let's get rid of him."
        if ep10_shroom_choice == "DIK":
            scene ep10_bbq_jillvar_event4b with dissolve
        else:
            scene ep10_bbq_jillvar_event4 with dissolve
        ji "It is tempting, but I don't want to ruin him. I just want him to leave me alone and stop trying to provoke me."
        $ new_bio("Jill", "I encouraged Jill to report Tybalt to the disciplinary committee.")
    "Show him some mercy":
        $ ep10_tybalt_mercy = True
        if ep10_shroom_choice == "DIK":
            mc "Whoa... I wouldn't want my world to shatter. Into like a million pieces..."
            mc "Don't do it, Jill. Show him mercy."
        else:
            mc "I don't like the guy and he's a fucking creep for doing that, on top of everything else he does..."
            mc "...but you should show him some mercy. Don't you think?"
        mc "You're better than him."
        if ep10_shroom_choice == "DIK":
            scene ep10_bbq_jillvar_event4b with dissolve
        else:
            scene ep10_bbq_jillvar_event4 with dissolve
        ji "That's what I'm leaning toward. I don't want to ruin him. I just want him to leave me alone and stop trying to provoke me."
        $ new_bio("Jill", "I asked Jill to show Tybalt some mercy. Yes, he did a horrible thing, but ruining his life over it is a bit over the top.")
ji "Trent told me Tybalt's feeling upset about what happened, so I think it will have an effect without me telling the committee about it."
ji "But we'll see... I haven't ruled it out yet, and I don't want to talk to him about it because I'm still mad."
if ep10_shroom_choice == "DIK":
    scene ep10_bbq_jillvar_event7b with dissolve
else:
    scene ep10_bbq_jillvar_event7 with dissolve
ji "Anyway... I'm sorry for doubting you."
if ep10_shroom_choice == "DIK":
    scene ep10_bbq_jillvar_event6b with dissolve
else:
    scene ep10_bbq_jillvar_event6 with dissolve
mc "I understand why you did... I crossed a line with what I did. I'm sorry too."
mc "Are we...cool?"
if ep10_shroom_choice == "DIK":
    scene ep10_bbq_jillvar_event7b with dissolve
else:
    scene ep10_bbq_jillvar_event7 with dissolve
ji "We're good, [name]."
if branchIsabella:
    ji "Tomorrow's Thanksgiving and these last years I've spent it with Bella."
    ji "Thinking about it being different this year has been weighing me down a lot."
    ji "I've decided to talk to her again."
    if ep10_shroom_choice == "DIK":
        scene ep10_bbq_jillvar_event6b with dissolve
    else:
        scene ep10_bbq_jillvar_event6 with dissolve
    mc "That makes me happy to hear."
    if ep10_shroom_choice == "DIK":
        scene ep10_bbq_jillvar_event7b with dissolve
    else:
        scene ep10_bbq_jillvar_event7 with dissolve
    ji "I'm not promising anything, but..."
    if ep10_shroom_choice == "DIK":
        scene ep10_bbq_jillvar_event6b with dissolve
    else:
        scene ep10_bbq_jillvar_event6 with dissolve
    mc "I understand. And still, I appreciate it."

if ep10_shroom_choice == "DIK":
    scene ep10_bbq_jillvar_event8b with dissolve
else:
    scene ep10_bbq_jillvar_event8 with dissolve
sa "Jill! Finally! We've been waiting for you."

if ep10_shroom_choice == "DIK":
    scene ep10_bbq_jillvar_event9 with dissolve
    mc "Sage... I get it now. It's an herb!"
    scene ep10_bbq_jillvar_event10 with dissolve
    if branchSage:
        sa "Pull yourself together, cutie. Drugs are bad for you, ok?"
    else:
        sa "Pull yourself together, [name]. Drugs are bad for you, ok?"
    if ep10_shroom_choice == "DIK":
        scene ep10_bbq_jillvar_event11b with dissolve
    else:
        scene ep10_bbq_jillvar_event11 with dissolve
    ji "Drugs?"
    scene ep10_bbq_jillvar_event12 with dissolve
    sa "The boys ate mushrooms. They're out here tripping all over the place."
else:
    scene ep10_bbq_jillvar_event12b with dissolve
sa "Come! It's drinks and girl talk time."

if "jill_block" in event_list:
    $ event_list.remove("jill_block")
    if "ep10_bbq_jsolo_event_label" in event_list:
        if ep10_shroom_choice == "DIK":
            $ task_list[9] = "Talk to the rogue"
        else:
            $ task_list[9] = "Talk to Josy"

$ task_list[6] = ""
if branchSage:
    $ event_list.append("ep10_bbq_s_event_label")
    if ep10_shroom_choice == "DIK":
        $ task_list[6] = "Talk to Princess Nadia"
    else:
        $ task_list[6] = "Talk to Sage"
$ updateTaskList()

if "ep10_bbq_jsolo_event_label" in event_list:
    if not persistent.ep10_cardsa6:
        scene ep10_bbq_bathroom_qj_card with dissolve
    else:
        scene ep10_bbq_bathroom_qj with dissolve
elif "ep10_bbq_q_event_label" in event_list or "ep10_bbq_q_pos" in event_list:
    if not persistent.ep10_cardsa6:
        scene ep10_bbq_bathroom_q_card with dissolve
    else:
        scene ep10_bbq_bathroom_q with dissolve
else:
    if not persistent.ep10_cardsa6:
        scene ep10_bbq_bathroom_card with dissolve
    else:
        scene ep10_bbq_bathroom with dissolve

jump endEvent

label ep10_bbq_z2_event_label:
if ep10_shroom_choice == "DIK":
    scene ep10_bbq_z2_event1 with dissolve
    zo "Seriously... How are you tonight?"
    scene ep10_bbq_z2_event3 with dissolve
    mc "I made a mistake."
    scene ep10_bbq_z2_event4 with dissolve
    zo "Was it the drugs? It doesn't look like you're enjoying yourself."
    scene ep10_bbq_z2_event3 with dissolve
    mc "I'm seeing things, Zoey."
    stop music fadeout 3
    scene ep10_bbq_z2_event4 with dissolve
    zo "Let's get away for a while. Talk to me, and I'll help you snap out of it."
else:
    scene ep10_bbq_z2_event2 with dissolve
    zo "How are you tonight?"
    scene ep10_bbq_z2_event6 with dissolve
    mc "Aside from having to babysit my brothers, I'm having fun. What about you?"
    stop music fadeout 3
    scene ep10_bbq_z2_event5 with dissolve
    zo "Yeah, me too. Can we go somewhere and talk?"

play music "music/ep9/tremolo.mp3"
$ renpy.sound.play("sound_effects/season3/bonfire.mp3", channel="sfx2", loop=True)
if not ep10_zoey_hangout:
    scene ep10_bbq_z2_event7 with dissolve
    zo "I wasn't sure if I should have come here."
    zo "It felt weird getting an invite from the DIKs when it wasn't from you."
    scene ep10_bbq_z2_event8 with dissolve
    mc "I heard that Tommy invited you, and by then I didn't think it mattered if I did it too."
    scene ep10_bbq_z2_event9 with dissolve
    zo "But are you cool with me being here? Hanging with your friends and all."
    scene ep10_bbq_z2_event8 with dissolve
    mc "I don't control you, Zoey. You can be friends with whoever you want to be friends with."
    scene ep10_bbq_z2_event9 with dissolve
    zo "A part of me feels like I'm pushing myself back into your life when you're not sure you want me in it."
    zo "I hate that feeling."
    scene ep10_bbq_z2_event8 with dissolve
    mc "I never said I didn't want you in my life... But I have a hard time forgiving you."
    mc "I have a hard time forgiving myself, too. I keep beating myself up over it."
    scene ep10_bbq_z2_event9 with dissolve
    zo "Forgive yourself for what?"
    scene ep10_bbq_z2_event8 with dissolve
    mc "I think I wouldn't feel this bummed out and angry if I never lied to you about how I felt in the first place."
    mc "Maybe it would have been easier to say how I felt instead of pretending things were fine?"
    mc "And now that I thought I had moved on, seeing you brings those feelings back. That's why I get mad."
else:
    scene ep10_bbq_z2_event7 with dissolve
    zo "Thanks for the invite. I didn't realize you guys were re-enacting a college horror movie in the woods."
    zo "I would have brought popcorn if I knew."
    scene ep10_bbq_z2_event10 with dissolve
    mc "There are marshmallows if you want them."
    scene ep10_bbq_z2_event11 with dissolve
    zo "I'll pass. Those are too sugary."
    scene ep10_bbq_z2_event12 with dissolve
    zo "About last time... When I left, it kinda felt like a weird tension in the air between us."
    if zoey_dik:
        zo "You started getting sentimental and I felt I could have handled it better."
    else:
        zo "I should have let you get sentimental. But I didn't wanna feel those feelings at the time."
    zo "Instead, I went into panic mode and tried to keep it cool."
    scene ep10_bbq_z2_event13 with dissolve
    mc "Yeah, I know."
    scene ep10_bbq_z2_event12 with dissolve
    zo "But I've thought about it a lot, and even though it's probably gonna hurt again..."
    zo "I'm ready to talk about it more, if you are."
    scene ep10_bbq_z2_event13 with dissolve
    mc "About what?"
    scene ep10_bbq_z2_event12 with dissolve
    zo "Like...more about how you felt when I left. If there is anything left for you to say."
    scene ep10_bbq_z2_event13 with dissolve
    mc "Well... I get mad thinking about that moment at the station."
    mc "I have a hard time forgiving myself. I keep beating myself up over it."
    scene ep10_bbq_z2_event14 with dissolve
    zo "Forgive yourself for what?"
    scene ep10_bbq_z2_event15 with dissolve
    mc "I think I wouldn't have felt bummed out and angry if I never lied to you about how I felt in the first place."
    mc "Maybe it would have been easier to say how I felt instead of pretending things were fine?"

scene ep10_bbq_z2_event16 with dissolve
zo "Let's go back in time together."
scene ep10_bbq_z2_event17 with dissolve
if ep10_shroom_choice == "DIK":
    mc "I might be hallucinating tonight, but even so, I know you can't go back in time."
else:
    mc "We can't go back in time, Zoey."
scene ep10_bbq_z2_event18 with dissolve
zo "We can. Look. We're at the train station again and I'm about to leave."
$ renpy.music.stop(channel="sfx2", fadeout=3)
scene ep10_bbq_z2_event25 with dissolve
zo "We're sitting here in silence, not saying shit because I don't know what to say and you're obviously feeling bad."
scene ep10_bbq_z2_event26 with dissolve
zo "And instead of this long moment of silence while waiting for that train, you start talking to me."
zo "And you say the things you really wanna say. The things you didn't say. The things you could have said."
scene ep10_bbq_z2_event28 with dissolve
$ renpy.pause()
scene ep10_bbq_z2_event27 with dissolve
mc "Um... Ok... I'd say..."
mc "Zoey. I don't want you to leave. Don't leave me here alone."
scene ep10_bbq_z2_event29 with dissolve
zo "I have to leave, [name]. I can't stay here because it's driving me crazy."
zo "All I think about is my grandma and the dreams I told her about. The dreams she supported me in and wanted me to fulfill."
scene ep10_bbq_z2_event27 with dissolve
mc "I understand that, but if you leave me here...you take away the only good thing I have in my life aside from Dad."
mc "You take away someone who I thought would be my future."
$ renpy.sound.play("sound_effects/season3/bonfire.mp3", channel="sfx2", loop=True)
scene ep10_bbq_z2_event19 with dissolve
zo "..."
scene ep10_bbq_z2_event20 with dissolve
zo "[name]... What are you saying?"
scene ep10_bbq_z2_event19 with dissolve
mc "I didn't realize it back then...what we had together."
mc "And I still have a hard time to call it what it was."
mc "I've been in constant denial and kept telling myself that it was just the best friendship I ever had. But I knew it was something more than that."
mc "You weren't just my friend. You were my girlfriend."
mc "And looking at you today, I know that deep down...you were my first love."
scene ep10_bbq_z2_event21 with dissolve
zo "..."
scene ep10_bbq_z2_event22 with dissolve
$ renpy.pause()
scene ep10_bbq_z2_event19 with dissolve
mc "If I had said that... Would you have stayed?"
scene ep10_bbq_z2_event21 with dissolve
zo "..."
scene ep10_bbq_z2_event22 with dissolve
$ renpy.pause()
scene ep10_bbq_z2_event23 with dissolve
mc "You know what? Don't answer..."
if ep9_mad_at_zoey:
    if ep10_shroom_choice == "DIK":
        mc "This is too much for me... I gotta do something else or I'll ruin this night even further."
    else:
        mc "This is too much for me... I gotta do something else or I'll ruin this night."
else:
    mc "We shouldn't have done this tonight... You were right to cut me off last time."
    mc "Sorry, but this is too much for me... I gotta do something else or I'll ruin this night."
$ renpy.music.stop(channel="sfx2", fadeout=3)
stop music fadeout 3
scene ep10_bbq_z2_event24 with dissolve
$ renpy.pause()
$ currentFreeRoamLabel = "ep10_bbq_diks_fire_label"
$ mphone_next_song()
$ new_bio("Zoey", "Zoey wanted me to open up about my feelings for her, and I did. She seemed stunned when I told her that she was my first love.")
$ event_list.append("ep10_bbq_jacob_event_label")
if ep10_shroom_choice == "DIK":
    $ task_list[4] = "Fend off mosquitos"
else:
    $ task_list[4] = "Talk to Jacob"

jump endEvent

label ep10_bbq_z_event_label:
scene ep10_bbq_z_event1 with dissolve
zo "DIKs! What's up?"
scene ep10_bbq_z_event2 with dissolve
jac "Zoey!"
play sound "sound_effects/table_slam.mp3"
scene ep10_bbq_z_event3 with vpunch
le "Everybody, calm the fuck down!"
scene ep10_bbq_z_event4 with dissolve
$ renpy.pause()
play sound "sound_effects/running.mp3"
scene ep10_bbq_z_event5 with dissolve
$ renpy.pause()
scene ep10_bbq_z_event6 with dissolve
zo "What's up with him?"
scene ep10_bbq_z_event8 with dissolve
rs "He ate something."
scene ep10_bbq_z_event7 with dissolve
zo "Ok... And him?"
scene ep10_bbq_z_event9 with dissolve
jac "He...ate something too."
scene ep10_bbq_z_event10 with dissolve
zo "Good thing I'm not hungry. I'd hate to trip balls in the forest."
if ep10_shroom_choice == "DIK":
    scene ep10_bbq_z_event11 with dissolve
    zo "[name]? Hello?"
    scene ep10_bbq_z_event13 with dissolve
    mc "Hi..."
    scene ep10_bbq_z_event12 with dissolve
    zo "Lemme guess. You ate something."
    scene ep10_bbq_z_event13 with dissolve
    mc "I did."
else:
    scene ep10_bbq_z_event17 with dissolve
    zo "Hey... Good to see you. You didn't eat something too, right?"
    scene ep10_bbq_z_event16 with dissolve
    mc "Only a good meal."
scene ep10_bbq_z_event17 with dissolve
zo "What's up with the beard? I've never seen you look this scruff."
scene ep10_bbq_z_event14 with dissolve
mc "I'm trying something new."
scene ep10_bbq_z_event17 with dissolve
zo "I'm surprised by it. I didn't think you could grow one."
if ep10_shroom_choice == "DIK":
    scene ep10_bbq_z_event15 with dissolve
    mc "But I can, ok!? I can too grow body hair! A lot of it!"
    scene ep10_bbq_z_event18 with dissolve
    zo "Hey, mellow."
    scene ep10_bbq_z_event19 with dissolve
    jac "Don't mind him. He's not himself tonight. Have a drink with us."
else:
    scene ep10_bbq_z_event14 with dissolve
    mc "Yeah, well...I can."
    scene ep10_bbq_z_event19 with dissolve
    jac "Wanna have a drink with us?"
scene ep10_bbq_z_event20 with dissolve
zo "Sure, why not?"
zo "And while we're drinking, I have some questions about those Halloween photos. They look the bomb!"
scene ep10_bbq_z_event21 with dissolve
rs "Tell me about it! Jacob and Elena did such a great job with them."
$ task_list[3] = ""

if not "ep10_bbq_jb_event_label" in event_list:
    $ event_list.append("ep10_bbq_z2_event_label")
    if ep10_shroom_choice == "DIK":
        $ task_list[4] = "Talk to the blueberry"
    else:
        $ task_list[4] = "Talk to Zoey"

$ updateTaskList()
jump endEvent

label ep10_bbq_s_event_label:
scene ep10_bbq_s_event1 with dissolve
sa "It looks like you did it again, [name]."
if ep10_shroom_choice == "DIK":
    scene ep10_bbq_s_event3 with dissolve
    mc "I swear, it was the gnome! I didn't touch the cheese."
    scene ep10_bbq_s_event4 with dissolve
    sa "[name]... I know it's your choice, but why are you taking drugs?"
    scene ep10_bbq_s_event3 with dissolve
    mc "I thought it would be fun, but it's not."
    scene ep10_bbq_s_event4 with dissolve
    sa "Be careful, ok? You don't have to play Simon Says with Tommy."
    scene ep10_bbq_s_event3 with dissolve
    mc "Hold me..."
    scene ep10_bbq_s_event5 with dissolve
    sa "Come here, I got you."
    sa "I was talking about the party, [name]. The party is great."
    scene ep10_bbq_s_event6 with dissolve
    mc "Oh. Thank you."
else:
    scene ep10_bbq_s_event2 with dissolve
    mc "You think?"
    scene ep10_bbq_s_event5 with dissolve
    sa "Yeah, you did great."
    scene ep10_bbq_s_event6 with dissolve
    mc "Thank you, Sage."
mc "How's your end of the party going?"
scene ep10_bbq_s_event5 with dissolve
sa "Maya's having fun and that's what matters. It makes me glad."
if ep9_jm_sad:
    scene ep10_bbq_s_event7 with dissolve
    sa "I tried talking to her and Josy about you."
    scene ep10_bbq_s_event8 with dissolve
    mc "How did that go?"
    scene ep10_bbq_s_event7 with dissolve
    sa "Josy doesn't hold anything against me. But boy is she feeling blue."
    sa "I can tell that you obviously meant a great deal to her. And that makes me feel guilty."
    scene ep10_bbq_s_event11 with dissolve
    sa "With Maya, it was easier, but again...I feel guilty."
    if ep9_jill_mood == 1:
        scene ep10_bbq_s_event8 with dissolve
        mc "Since I saw you talking to Jill... Um... Her too."
        scene ep10_bbq_s_event10 with dissolve
        sa "You've gotta be kidding me."
        sa "How many have you dated!?"
        scene ep10_bbq_s_event9 with dissolve
        mc "Don't judge me, I was dating around. But I told you that I wanted to be with you."
    else:
        scene ep10_bbq_s_event9 with dissolve
        mc "I'm sorry... I was dating around. But I told you that I wanted to be with you."
    scene ep10_bbq_s_event7 with dissolve
    sa "I'll make it work somehow, but I can't fight your battle with Josy for you."
    scene ep10_bbq_s_event8 with dissolve
    mc "I know. I'm not asking you to. I need to find a way to make her forgive me."
    mc "And I hope you understand why I'm doing it."
    scene ep10_bbq_s_event7 with dissolve
    sa "You'll figure it out."
scene ep10_bbq_s_event13 with dissolve
$ renpy.pause()
scene ep10_bbq_s_event11 with dissolve
sa "I'm worried about tomorrow."
scene ep10_bbq_s_event12 with dissolve
mc "You and me both. And probably the others too."
mc "Imagine not being able to trust your dad..."
scene ep10_bbq_s_event11 with dissolve
sa "Did you know about Maya's mom?"
scene ep10_bbq_s_event12 with dissolve
mc "Yeah, Derek told me recently."
scene ep10_bbq_s_event11 with dissolve
sa "Maya told me about her a while back. And I could feel the pain in her words."
sa "I may not have either of my biological parents in my life, but based on what she told me, I believe she has it worse."
sa "To be forced to witness your mom suffer and deteriorate like that and be completely helpless."
sa "How do you even cope with it?"
scene ep10_bbq_s_event27 with dissolve
mc "I don't know how Maya does it, but Derek seems to cover his pain with laughter and jokes."
mc "I joke around a lot too, and it does help. But I think for me, talking about it helps defuse it."
sa "And I'm the fucking opposite. I bury it so I don't have to think about it."
scene ep10_bbq_s_event12 with dissolve
mc "That's why you and I clash sometimes."
scene ep10_bbq_s_event11 with dissolve
sa "But we don't have to. I thought more about how you worry that communication will be a problem for us."
sa "I believe that's the reason why none of my previous relationships worked out."
scene ep10_bbq_s_event14 with dissolve
sa "I mean, not because this is a relationship, but..."
scene ep10_bbq_s_event15 with dissolve
mc "You don't think it is?"
scene ep10_bbq_s_event16 with dissolve
sa "Why? Do you?"
scene ep10_bbq_s_event15 with dissolve
mc "We've only been on one date, but I think we have some kind of a relationship."
mc "But if you think it's too early to say we do, I'm fine with that too."
scene ep10_bbq_s_event16 with dissolve
sa "You said the R word..."
scene ep10_bbq_s_event15 with dissolve
mc "You said it first."
scene ep10_bbq_s_event17 with dissolve
sa "Isn't it too early to say it is?"
sa "Doesn't it make it sound like it's not genuine if it happened this fast?"
scene ep10_bbq_s_event15 with dissolve
mc "Why can't good things happen fast? Bad things happen in an instant."
scene ep10_bbq_s_event17 with dissolve
sa "Because it scares people off when it happens too fast. Like it's too good to be true."
scene ep10_bbq_s_event18 with dissolve
mc "This is when I would say something cheesy like \"you are too good to be true\", but I won't."

scene ep10_bbq_s_event19 with dissolve
sa "Fuck you, you're so corny."
scene ep10_bbq_s_event18 with dissolve
mc "Fuck you, too."
scene ep10_bbq_s_event20 with dissolve
sa "Well... I guess I have a boyfriend..."
scene ep10_bbq_s_event21 with dissolve
mc "And you're telling me now? What's wrong with you?"
mc "See, I made a joke at a bad time again."
scene ep10_bbq_s_event22 with dissolve
sa "Forget it."
scene ep10_bbq_s_event23 with dissolve
mc "Come here... My girl."
scene ep10_bbq_s_event24 with dissolve
sa "I'm your girl?"
scene ep10_bbq_s_event23 with dissolve
mc "You're my girl."
scene ep10_bbq_s_event24 with dissolve
if ep10_shroom_choice == "DIK":
    sa "And you're not just saying that because a gnome ate some cheese?"
    scene ep10_bbq_s_event23 with dissolve
    mc "He stole it. He didn't eat it."
    scene ep10_bbq_s_event24 with dissolve
    sa "Well, you better remember this tomorrow, or we're gonna have a problem."
    scene ep10_bbq_s_event25 with dissolve
    mc "This is the happiest moment I've had the entire evening, I'm sure I will remember it."
else:
    sa "You're mine too."
    scene ep10_bbq_s_event23 with dissolve
    mc "I'm your girl?"
    scene ep10_bbq_s_event24 with dissolve
    sa "Only when you cry."
    scene ep10_bbq_s_event25 with dissolve
    mc "Haha! I don't cry that often."

scene ep10_bbq_s_event26 with dissolve
$ renpy.pause()

$ new_bio("Sage", "Sage and I agreed that we're a couple. She felt a bit iffy about it happening this fast, but in the end, she couldn't deny that we've reached that point in our relationship.")
$ task_list[6] = ""
if ep10_pp_activity == 0:
    if ep10_shroom_choice != "DIK":
        $ task_list[5] = "Play Beer Pong"
    else:
        $ task_list[5] = "Throw the white sphere"
    $ event_list.append("ep10_bbq_bps_event_label")
    
    
    if "ep10_bbq_bps_event_label" in event_list or "ep10_bbq_bpjo_event_label" in event_list or "ep10_bbq_bpj_event_label" in event_list:
        if ep10_shroom_choice != "DIK":
            $ task_list[5] = "Play Beer Pong"
        else:
            $ task_list[5] = "Throw the white sphere"
            
    if ("ep10_bbq_bps_event_label" in event_list or "ep10_bbq_bpjo_event_label" in event_list or "ep10_bbq_bpj_event_label" in event_list) and "ep10_bbq_2dg_event_label" in event_list:
        if ep10_shroom_choice != "DIK":
            $ task_list[5] = "Play Beer Pong\nGo to the forest"
        else:
            $ task_list[5] = "Throw the white sphere\nGo to the forest"
            
    if ("ep10_bbq_bps_event_label" not in event_list and "ep10_bbq_bpjo_event_label" not in event_list and "ep10_bbq_bpj_event_label" not in event_list) and "ep10_bbq_2dg_event_label" in event_list:
        if ep10_shroom_choice != "DIK":
            $ task_list[5] = "Go to the forest"
        else:
            $ task_list[5] = "Go to the forest"
    
else:
    $ event_list.append("ep10_bbq_final_phase")
$ updateTaskList()
jump endEvent

label ep10_bbq_bps_event_label:
scene ep10_bbq_bps_event1 with dissolve
sa "Why isn't anyone playing?"
scene ep10_bbq_bps_event2 with dissolve
mc "I think it's because Camila made everyone strip."
scene ep10_bbq_bps_event3 with dissolve
cam "Don't hate the player, hate the game! WOOO!!!"
scene ep10_bbq_bps_event1 with dissolve
sa "Wanna play?"
scene ep10_bbq_bps_event4 with dissolve
mc "Why? Are you not cold enough with your clothes on?"
scene ep10_bbq_bps_event5 with dissolve
sa "*{i}Hisses{/i}* He already starts to trash talk."
scene ep10_bbq_bps_event6 with dissolve
mc "I wouldn't want everyone at the party to see my girl nude, would I?"
scene ep10_bbq_bps_event5 with dissolve
sa "You don't have to worry about that. Because they will be seeing my guy nude, and that's ok because most already did."
scene ep10_bbq_bps_event7 with dissolve
mc "Damn, that stings..."
sa "Hahaha!"
scene ep10_bbq_bps_event8 with dissolve
mc "You're going down."

hide screen new_phone_screen
if minigames and not bp_tut_ep10_seen and (tutorials or not persistent.bp_tutorial):
    menu:
        "Watch tutorial":
            $ bp_tut_ep10_seen = True
            $ bp_dlg = 0
            $ bp_jump_label = "ep10_bp_match_sage_label"
            show screen bp_tut_screen
            pause
            $ persistent.bp_tutorial = True
        "Skip tutorial":
            $ renpy.pause(0.5)
label ep10_bp_match_sage_label:
$ renpy.block_rollback()
$ bp_init_game("Sage","ep10","ep10_bp_after_sage_label")
if minigames:
    show screen bp_screen
else:
    show screen bp_screen_nm
pause

label ep10_bp_after_sage_label:
show screen new_phone_screen
if bp_player_won:
    if minigames:
        scene ep10_bbq_bps_event9
        hide screen bp_screen
        with dissolve
    else:
        scene ep10_bbq_bps_event9
        hide screen bp_screen_nm
        with dissolve
    mc "Oh, my... Look what happened."
    scene ep10_bbq_bps_event10 with dissolve
    sa "I know you're not gonna make me do this."
    scene ep10_bbq_bps_event9 with dissolve
    mc "I wasn't, but then you started trash-talking me."
    mc "And now I think it's showtime."
    scene ep10_bbq_bps_event11 with dissolve
    sa "Fine! Take a look. I'm not embarrassed."
    sa "The HOTs have seen me before anyway."
    scene ep10_bbq_bps_event12 with dissolve
    
    if persistent.mod_wt_enabled: 
                    $mod_choices = ["(+Maya)","(+Josy)","(-DIK)","(+DIK)","(-Maya)","(-Josy)","","","","","","" ]
                    #[m_c1][mod_choices[0]]
    
    
    menu:
        "Warn her about Jacob [m_c1][mod_choices[2]]":
            $ tmpBool3 = True
            $ dk(-1)
            mc "You should cover yourself up before Jacob gets a good look, then."
        "Don't warn her [m_c1][mod_choices[3]]":
            $ tmpBool3 = False
            $ dk(1)
            mc "Jacob hasn't."
    scene ep10_bbq_bps_event18 with dissolve
    jac "Whoa..."
    scene ep10_bbq_bps_event13 with vpunch
    sa "Ahh!!!"
    if not tmpBool3:
        mc "Hahaha!"
        scene ep10_bbq_bps_event16 with dissolve
        el "That's so mean, [name]."
        scene ep10_bbq_bps_event17 with dissolve
        mc "What? She wanted to play!"
    else:
        scene ep10_bbq_bps_event16 with dissolve
        el "That's so mean, [name]."
        scene ep10_bbq_bps_event17 with dissolve
        mc "What? At least I warned her. And she wanted to play!"
    scene ep10_bbq_bps_event14 with dissolve
    sa "I didn't think you'd win."
    scene ep10_bbq_bps_event15 with dissolve
    mc "Did you think I would lose on purpose? Come on!"
    $ new_bio("Sage", "Sage and I played Beer Pong, and I beat her ass without showing her any mercy.")
else:
    if minigames:
        scene ep10_bbq_bps_event21
        hide screen bp_screen
        with dissolve
    else:
        scene ep10_bbq_bps_event21
        hide screen bp_screen_nm
        with dissolve
    sa "I won! Uh-huh! I won! Uh-huh!"
    scene ep10_bbq_bps_event19 with dissolve
    cam "Move those hands, [name]! WOOO!!!"
    scene ep10_bbq_bps_event20 with dissolve
    mc "You're drunk, Cammy."
    scene ep10_bbq_bps_event19 with dissolve
    cam "That doesn't make me wanna see it less!"
    scene ep10_bbq_bps_event22 with dissolve
    mc "*{i}Sigh{/i}* All right. Here it is."
    cam "In all its glory! Show us your butt!"
    scene ep10_bbq_bps_event19 with dissolve
    cam "Who threw another log on the fire? It's getting hot here! WOO!!!"
    scene ep10_bbq_bps_event20 with dissolve
    sa "Haha, ok. That's enough, Cammy."
    scene ep10_bbq_bps_event19 with dissolve
    cam "WHOOP WHOOP!"
    scene ep10_bbq_bps_event23 with dissolve
    sa "Good game. *{i}Smack{/i}*"
    mc "Yeah, for you. Nicely played."
    $ new_bio("Sage", "Sage and I played Beer Pong, and she made me strip in front of people.")

$ task_list[5] = ""


if "ep10_bbq_bps_event_label" in event_list or "ep10_bbq_bpjo_event_label" in event_list or "ep10_bbq_bpj_event_label" in event_list:
    if ep10_shroom_choice != "DIK":
        $ task_list[5] = "Play Beer Pong"
    else:
        $ task_list[5] = "Throw the white sphere"
        
if ("ep10_bbq_bps_event_label" in event_list or "ep10_bbq_bpjo_event_label" in event_list or "ep10_bbq_bpj_event_label" in event_list) and "ep10_bbq_2dg_event_label" in event_list:
    if ep10_shroom_choice != "DIK":
        $ task_list[5] = "Play Beer Pong\nGo to the forest"
    else:
        $ task_list[5] = "Throw the white sphere\nGo to the forest"
        
if ("ep10_bbq_bps_event_label" not in event_list and "ep10_bbq_bpjo_event_label" not in event_list and "ep10_bbq_bpj_event_label" not in event_list) and "ep10_bbq_2dg_event_label" in event_list:
    if ep10_shroom_choice != "DIK":
        $ task_list[5] = "Go to the forest"
    else:
        $ task_list[5] = "Go to the forest"

$ event_list.append("ep10_bbq_final_phase")
$ updateTaskList()
jump endEvent

label ep10_bbq_msolo_event_label:
scene ep10_bbq_msolo_event1 with dissolve
if ep10_shroom_choice == "DIK":
    mc "Happy birthday."
    scene ep10_bbq_msolo_event4 with dissolve
    my "It's not my birthday."
    scene ep10_bbq_msolo_event3 with dissolve
    mc "What are you celebrating again?"
    scene ep10_bbq_msolo_event2 with dissolve
    my "Becoming a HOT. You know that."
    scene ep10_bbq_msolo_event3 with dissolve
    mc "Oh, yeah!"
else:
    mc "Happy HOT day."
    scene ep10_bbq_msolo_event2 with dissolve
    my "Happy HOT day to you too."
    scene ep10_bbq_msolo_event3 with dissolve

if ep10_pp_activity == 0:
    mc "Played any Beer Pong?"
    scene ep10_bbq_msolo_event4 with dissolve
    my "I have very little interest in flashing my tits to everyone."
    scene ep10_bbq_msolo_event3 with dissolve
    mc "Ah, you lack confidence in your Beer Pong skills."
    scene ep10_bbq_msolo_event2 with dissolve
    my "No, I lack confidence in showing my body naked to this many clothed people."
    scene ep10_bbq_msolo_event3 with dissolve
    mc "You shouldn't. You have a great body."
    scene ep10_bbq_msolo_event4 with dissolve
    my "[name]. What are you doing?"
    scene ep10_bbq_msolo_event3 with dissolve
    if ep10_shroom_choice == "DIK":
        mc "I don't know. I'm not myself right now."
    else:
        mc "I don't know. I'm drunk."
else:
    scene ep10_bbq_msolo_event3 with dissolve

if ep10_feelingsForMaya:
    mc "About what happened at my place... Um..."
    mc "I wish I had something to blame it on, but what it comes down to is that I shouldn't have said those things to begin with."
    mc "I'm sorry that I made you uncomfortable."
    scene ep10_bbq_msolo_event6 with dissolve
    my "Don't feel sorry."
    my "I'm the sorry one. I shouldn't have reacted the way I did."
    my "I got mad at you because you told me your feelings."
    scene ep10_bbq_msolo_event5 with dissolve
    my "I didn't know what to do with my own feelings at that point, and I felt cornered."
    my "I still don't know what to feel. And I've tried to push it aside because I don't want to think about it."
    scene ep10_bbq_msolo_event6 with dissolve
    my "All I can say is that... I don't think I would have reacted that way, if I didn't reciprocate."
    my "And I shouldn't even say that. Fuck..."
    scene ep10_bbq_msolo_event5 with dissolve
    my "I need some time to process this."
    scene ep10_bbq_msolo_event7 with dissolve
    mc "I get that... Take all the time you need."
    scene ep10_bbq_msolo_event5 with dissolve
    my "What about you?"
    scene ep10_bbq_msolo_event7 with dissolve
    mc "I'll keep doing what I've tried all this time... To move on."
    mc "Maybe one day I'll be able to do it."
    scene ep10_bbq_msolo_event8 with dissolve
    $ renpy.pause()
else:
    scene ep10_bbq_msolo_event5 with dissolve
    my "Tomorrow's the big day."
    scene ep10_bbq_msolo_event3 with dissolve
    mc "What are your thoughts?"
    scene ep10_bbq_msolo_event4 with dissolve
    my "I'm scared, but I feel motivated to do it too."
    my "I feel like something is finally happening."
    scene ep10_bbq_msolo_event5 with dissolve
    my "*{i}Phew{/i}* I hope it goes according to plan."
    scene ep10_bbq_msolo_event3 with dissolve
    mc "It will."
    scene ep10_bbq_msolo_event2 with dissolve
    my "Yeah. You're right. It will."
    scene ep10_bbq_msolo_event3 with dissolve
    mc "Try your best to enjoy this night."
    scene ep10_bbq_msolo_event2 with dissolve
    my "Oh, I am. I'm having a great time. And everyone's so nice to me."
    scene ep10_bbq_msolo_event9 with dissolve
    $ renpy.pause()

$ task_list[8] = ""
$ updateTaskList()
jump endEvent

label ep10_bbq_jsolo_event_label:
scene ep10_bbq_jsolo_event1 with dissolve
mc "Having fun?"
scene ep10_bbq_jsolo_event2 with dissolve
js "I am. What about you?"
scene ep10_bbq_jsolo_event1 with dissolve
if ep10_shroom_choice == "DIK":
    mc "I ate a mushroom and I'm seeing things..."
    scene ep10_bbq_jsolo_event3 with dissolve
    js "I don't wanna act like I'm your parent, but you shouldn't do drugs, [name]."
    js "Bad things could happen to you."
    scene ep10_bbq_jsolo_event1 with dissolve
    mc "I know, but I wanted to try it with my brothers."
else:
    mc "It's ok. It would have been better if the boys didn't take drugs. But I'm trying to enjoy it."
    scene ep10_bbq_jsolo_event2 with dissolve
    js "Yeah, what's up with that? Was it Tommy's idea?"
    scene ep10_bbq_jsolo_event1 with dissolve
    mc "Something like it."
scene ep10_bbq_jsolo_event4 with dissolve
mc "How have you been?"
if ep10_feelingsForJosy:
    scene ep10_bbq_jsolo_event3 with dissolve
    js "I wish I knew. It's been a haze and I try not to think about it too much."
    js "Because every time I do, I feel bad about myself."
    js "I feel bad about what I did, said and how I feel."
    js "What about you?"
    scene ep10_bbq_jsolo_event1 with dissolve
    mc "Part of me feels relieved that I told you what I felt."
    mc "And then there's another part that regrets it because of Maya."
    scene ep10_bbq_jsolo_event3 with dissolve
    js "Maya... Yeah..."
    js "She still doesn't know anything. And she's in a place where I can't talk to her about it."
    scene ep10_bbq_jsolo_event1 with dissolve
    mc "Yeah, I get it. But is there ever going to be a good time to tell her?"
    scene ep10_bbq_jsolo_event3 with dissolve
    js "Nope. There won't be. But there will be less worse times for it."
    js "At least, I hope."
    scene ep10_bbq_jsolo_event5 with dissolve
    js "[name]... Tomorrow has to go well. I don't know what I'll do if it doesn't."
    scene ep10_bbq_jsolo_event4 with dissolve
    mc "I'll do my best."
    scene ep10_bbq_jsolo_event7 with dissolve
    
    if persistent.mod_wt_enabled: 
                    $mod_choices = ["(+Maya)","(+Josy)","(-DIK)","(+DIK)","(-Maya)","(-Josy)","","","","","","" ]
                    #[m_c1][mod_choices[0]]
    
    menu:
        "Kiss forehead [m_c1][mod_choices[3]][m_c2][mod_choices[1]]":
            $ dk(2)
            $ RPjosy += 1
            scene ep10_bbq_jsolo_event9 with dissolve
            mc "*{i}Smack{/i}*"
            scene ep10_bbq_jsolo_event10 with dissolve
            js "(Don't tilt your head up to his. Don't do it. Don't.)"
            scene ep10_bbq_jsolo_event11 with dissolve
            $ renpy.pause()
        "Just hug her [m_c1][mod_choices[2]]":
            $ dk(-1)
            scene ep10_bbq_jsolo_event8 with dissolve
            $ renpy.pause()
else:
    scene ep10_bbq_jsolo_event3 with dissolve
    js "Do you mean since I put on lingerie and told you I had feelings for you?"
    js "And when you said you didn't feel that way about me anymore."
    js "I've been great..."
    scene ep10_bbq_jsolo_event4 with dissolve
    mc "..."
    scene ep10_bbq_jsolo_event3 with dissolve
    js "I'm at a stage where I don't know what to do, [name]."
    js "I don't want to do anything rash, so, I'm letting days pass and see if I feel anything different from the day before."
    js "But so far... Nope. I'm feeling pretty much the same as I did when I told you. And it sucks."
    scene ep10_bbq_jsolo_event1 with dissolve
    mc "Yeah... I understand that it must be hard for you. But I don't want it to become something that stops us from talking."
    scene ep10_bbq_jsolo_event3 with dissolve
    js "I feel embarrassed for saying and doing that. And you saying that I shouldn't feel embarrassed wouldn't help."
    scene ep10_bbq_jsolo_event1 with dissolve
    mc "Do you want me to do something embarrassing? Would that help?"
    scene ep10_bbq_jsolo_event2 with dissolve
    js "Haha, no. I don't think it would."
    scene ep10_bbq_jsolo_event5 with dissolve
    js "I'm sorry, [name]. But I don't feel happy with myself at the moment. And I don't think you can do anything to help me with that."
    js "But I don't want to stop talking to you either. Even though I feel like I want to sink through the floor at times when I remember that night."
    scene ep10_bbq_jsolo_event3 with dissolve
    js "We'll survive. Won't we?"
    scene ep10_bbq_jsolo_event4 with dissolve
    mc "We will."
    scene ep10_bbq_jsolo_event6 with dissolve
    $ renpy.pause()

$ task_list[9] = ""
$ updateTaskList()
jump endEvent

label ep10_bbq_1dg_event_label:
scene ep10_bbq_1dg_event1 with dissolve
my "Tommy is completely gone."
js "I know. I checked up on him before to make sure he was all right, but I couldn't make much sense of it."
js "I hope Heather will watch him because I don't want to waste this night doing it."
if ep10_shroom_choice == "DIK":
    scene ep10_bbq_1dg_event8 with dissolve
    my "It's bad enough that [name] ate a mushroom too."
    scene ep10_bbq_1dg_event2 with dissolve
    js "He did?"
    scene ep10_bbq_1dg_event8 with dissolve
    my "He sure did."
    scene ep10_bbq_1dg_event2 with dissolve
    js "Well, that would explain a lot."
else:
    scene ep10_bbq_1dg_event8 with dissolve
    if ep10_shroom_choice != "CHICK":
        my "At least [name] didn't cave."
    else:
        my "At least [name] didn't cave. He even tried to talk them out of it."
    scene ep10_bbq_1dg_event3 with dissolve
    js "That's good. That's one less person to worry about."

scene ep10_bbq_1dg_event9 with dissolve
my "Did you hear that he's sleeping in a tent tonight?"
scene ep10_bbq_1dg_event3 with dissolve
js "Haha, yeah! He's nuts for doing that."
js "I bet he'll bail like the rest."
scene ep10_bbq_1dg_event9 with dissolve
my "I don't think he will bail. Not if he's still drunk by then."
scene ep10_bbq_1dg_event3 with dissolve
js "You're not gonna stay with him in that tent, right?"
scene ep10_bbq_1dg_event9 with dissolve
my "Would you?"
scene ep10_bbq_1dg_event3 with dissolve
js "And freeze my butt off? No."
scene ep10_bbq_1dg_event10 with dissolve
my "What if I dared you to?"
scene ep10_bbq_1dg_event2 with dissolve
js "You're not using a dare on me like that. It's not even comparable to what you did in class."
scene ep10_bbq_1dg_event10 with dissolve
my "Hmm... Maybe it's not... But then again, maybe it is?"
scene ep10_bbq_1dg_event2 with dissolve
js "It's not. You got dared to kiss him, I'd get dared to survive in the wilderness."
scene ep10_bbq_1dg_event9 with dissolve
my "Tsk. But, I have to dare you something. It's my turn."
scene ep10_bbq_1dg_event4 with dissolve
js "Pick something else."
scene ep10_bbq_1dg_event10 with dissolve
my "Hm... Ok, I dare you to..."
if ep10_pp_activity == 0:
    my "...play Beer Pong with [name]."
    scene ep10_bbq_1dg_event4 with dissolve
    js "Huh? How is that a dare?"
    scene ep10_bbq_1dg_event9 with dissolve
    my "Camila told me they're playing the strip version of it."
    scene ep10_bbq_1dg_event5 with dissolve
    js "Oh... If I lose, I'd have to remove all my clothes?"
    scene ep10_bbq_1dg_event10 with dissolve
    my "That's the dare."
    scene ep10_bbq_1dg_event5 with dissolve
    js "That one is even worse than sleeping in the tent!"
    scene ep10_bbq_1dg_event10 with dissolve
    my "You can't get another veto. But, it's the Dare Game. You can duck out if you're scared."
    scene ep10_bbq_1dg_event6 with dissolve
    js "..."
    scene ep10_bbq_1dg_event7 with dissolve
    js "I'm not going to be the first one to pass on a dare."
    scene ep10_bbq_1dg_event9 with dissolve
    my "So, you'll do it?"
    scene ep10_bbq_1dg_event4 with dissolve
    js "The problem is, I don't think [name] will do it."
    scene ep10_bbq_1dg_event9 with dissolve
    my "Let's ask him later."
else:
    scene ep10_bbq_1dg_event10 with dissolve
    my "...jump up on [name], wrap your legs around him and make out until he tells you to stop."
    scene ep10_bbq_1dg_event5 with dissolve
    js "Until he tells me to stop?"
    scene ep10_bbq_1dg_event10 with dissolve
    my "Yeah, I wanna see how long it takes for that to happen."
    my "And if I know him, I bet it will be a while. Which makes it an interesting dare."
    scene ep10_bbq_1dg_event4 with dissolve
    js "That's the dare?"
    scene ep10_bbq_1dg_event10 with dissolve
    my "That's the dare. But, it's the Dare Game. You can duck out if you're scared."
    scene ep10_bbq_1dg_event6 with dissolve
    js "..."
    scene ep10_bbq_1dg_event7 with dissolve
    js "I'm not going to be the first one to pass on a dare."
    scene ep10_bbq_1dg_event11 with dissolve
    my "He's right over there. But you should probably wait until less people are around."
    js "I've got this."

    scene ep10_bbq_1dg_event12 with dissolve
    js "[name]?"
    play sound "sound_effects/shove.mp3"
    scene ep10_bbq_1dg_event13 with hpunch
    mc "Whoa! Josy?"
    scene anim_josy_kiss_ep10 with dissolve
    js "*{i}Smack{/i}* Mmmm!"
    mc "Mmpphh... Huh?"
    pause
    scene ep10_bbq_1dg_event17 with dissolve
    my "(Haha! I knew it! He's not letting go that easily! She's going to feel so uncomfortable soon.)"
    scene anim_josy_kiss_ep10 with dissolve
    js "(Why isn't he stopping me? He's enjoying it way too much...)"
    js "(Fuck... He's getting hard!)"
    mc "(Hey, if she wants this, who am I to stop it? I'll let her say when enough is enough.)"
    js "(He's not stopping! I gotta do something to make him stop.)"
    pause
    scene ep10_bbq_1dg_event14 with dissolve
    js "(I know! I'll pinch him!)"
    scene ep10_bbq_1dg_event15 with dissolve
    mc "Ow!!!"
    js "There we go. Thank you!"
    scene ep10_bbq_1dg_event16 with dissolve
    mc "What the hell was that about?"
    scene ep10_bbq_1dg_event15 with dissolve
    js "I can't talk about it now, but it was a dare."
    scene ep10_bbq_1dg_event18 with dissolve
    my "Hahaha! I can't believe you did that."
    scene ep10_bbq_1dg_event19 with dissolve
    ml "You guys are so fucking cool together. You make me miss what I had back in high school."
    scene ep10_bbq_1dg_event20 with dissolve
    my "Oh, yeah! Mel had a relationship with a friend and a guy back in high school."
    scene ep10_bbq_1dg_event21 with dissolve
    js "You did?"
    scene ep10_bbq_1dg_event19 with dissolve
    ml "Yeah! Let's sit down and I'll tell you about it."

if ep10_pp_activity == 0:
    if ep10_shroom_choice != "DIK":
        $ task_list[5] = "Play Beer Pong"
    else:
        $ task_list[5] = "Throw the white sphere"
    $ event_list.append("ep10_bbq_bpjo_event_label")
else:
    $ event_list.append("ep10_bbq_final_phase")
    $ event_list.append("ep10_bbq_2dg_event_label")
    if ep10_shroom_choice != "DIK":
        $ task_list[5] = "Go to the forest"
    else:
        $ task_list[5] = "Explore the forest"
$ task_list[8] = ""
$ updateTaskList()

jump endEvent

label ep10_bbq_bpj_event_label:
scene ep10_bbq_bpj_event1 with dissolve
ji "Is that some kind of a drinking game?"
scene ep10_bbq_bpj_event2 with dissolve
mc "Yeah, it's Beer Pong. Never heard of it?"
scene ep10_bbq_bpj_event1 with dissolve
ji "Oh! Yes, I've heard of it. But I have never played it."
scene ep10_bbq_bpj_event2 with dissolve
mc "Would you like to?"
scene ep10_bbq_bpj_event1 with dissolve
ji "I'm afraid I wouldn't be good at it and end up drinking too much."
scene ep10_bbq_bpj_event2 with dissolve
mc "Yeah, that could happen. And the way we play it, there's stripping involved too."
scene ep10_bbq_bpj_event3 with dissolve
ji "Well, if that's the case, then I definitely don't want to play it."
scene ep10_bbq_bpj_event4 with dissolve
mc "We don't have to play with those rules. And you can always stop drinking if you don't want to do it anymore."
scene ep10_bbq_bpj_event5 with dissolve
ji "I don't know..."
scene ep10_bbq_bpj_event4 with dissolve
mc "We should play. You need to experience this at least once in college."
scene ep10_bbq_bpj_event5 with dissolve
ji "Is that so? You'll have to show me how to do it."
scene ep10_bbq_bpj_event4 with dissolve
mc "Sure thing!"

hide screen new_phone_screen
if minigames and not bp_tut_ep10_seen and (tutorials or not persistent.bp_tutorial):
    menu:
        "Watch tutorial":
            $ bp_tut_ep10_seen = True
            $ bp_dlg = 0
            $ bp_jump_label = "ep10_bp_match_jill_label"
            show screen bp_tut_screen
            pause
            $ persistent.bp_tutorial = True
        "Skip tutorial":
            $ renpy.pause(0.5)
label ep10_bp_match_jill_label:
$ renpy.block_rollback()
$ bp_init_game("Jill","ep10","ep10_bp_after_jill_label")
if minigames:
    show screen bp_screen
else:
    show screen bp_screen_nm
pause

label ep10_bp_after_jill_label:
show screen new_phone_screen
if bp_player_won:
    if minigames:
        scene ep10_bbq_bpj_event6
        hide screen bp_screen
        with dissolve
    else:
        scene ep10_bbq_bpj_event6
        hide screen bp_screen_nm
        with dissolve
    mc "I won!"
    scene ep10_bbq_bpj_event8 with dissolve
    ly "And this is where you should have been completely nude."
    scene ep10_bbq_bpj_event6 with dissolve
    mc "Yeah, you got lucky tonight."
    scene ep10_bbq_bpj_event7 with dissolve
    ji "Thanks. I feel nauseous from drinking the beer."
    ji "I think that's all I'll play tonight."
    scene ep10_bbq_bpj_event18 with dissolve
    mc "You did great."
    mc "*{i}Smack{/i}*"
    $ new_bio("Jill", "I won at Beer Pong against Jill, but she wasn't comfortable playing with the strip rules.")
else:
    if minigames:
        scene ep10_bbq_bpj_event11
        hide screen bp_screen
        with dissolve
    else:
        scene ep10_bbq_bpj_event11
        hide screen bp_screen_nm
        with dissolve
    ji "Did I win?"
    scene ep10_bbq_bpj_event6 with dissolve
    mc "Yes, you did."
    scene ep10_bbq_bpj_event9 with dissolve
    ly "And now, [name] has to show us his goods."
    scene ep10_bbq_bpj_event7 with dissolve
    ji "No no! You don't have to do that."
    scene ep10_bbq_bpj_event20 with dissolve
    bc "Come on! Show it!"
    scene ep10_bbq_bpj_event12 with dissolve
    ji "[name]..."
    scene ep10_bbq_bpj_event13 with dissolve
    menu:
        "Show it":
            mc "You shouldn't have won if you didn't want me to show it."
            scene ep10_bbq_bpj_event16 with dissolve
            mc "Woo!!!"
            scene ep10_bbq_bpj_event14 with dissolve
            ji "Hahaha! Oh my God! What are you doing?"
            scene ep10_bbq_bpj_event16 with dissolve
            mc "And that's how you play Beer Pong."
            scene ep10_bbq_bpj_event15 with dissolve
            ji "Haha... I think that's all I'll play tonight."
            $ new_bio("Jill", "I lost at Beer Pong against Jill and showed my dick to people watching.")
        "Don't show it":
            scene ep10_bbq_bpj_event17 with dissolve
            mc "Jill gave me a free pass, and I'll take it."
            scene ep10_bbq_bpj_event10 with dissolve
            ly "What a waste of a game."
            scene ep10_bbq_bpj_event21 with dissolve
            bc "Aw, come on!"
            scene ep10_bbq_bpj_event19 with dissolve
            ji "*{i}Smack{/i}* Thanks."
            $ new_bio("Jill", "I lost at Beer Pong against Jill but didn't show my dick to people watching.")

$ task_list[5] = ""

if "ep10_bbq_bps_event_label" in event_list or "ep10_bbq_bpjo_event_label" in event_list or "ep10_bbq_bpj_event_label" in event_list:
    if ep10_shroom_choice != "DIK":
        $ task_list[5] = "Play Beer Pong"
    else:
        $ task_list[5] = "Throw the white sphere"
        
if ("ep10_bbq_bps_event_label" in event_list or "ep10_bbq_bpjo_event_label" in event_list or "ep10_bbq_bpj_event_label" in event_list) and "ep10_bbq_2dg_event_label" in event_list:
    if ep10_shroom_choice != "DIK":
        $ task_list[5] = "Play Beer Pong\nGo to the forest"
    else:
        $ task_list[5] = "Throw the white sphere\nGo to the forest"
        
if ("ep10_bbq_bps_event_label" not in event_list and "ep10_bbq_bpjo_event_label" not in event_list and "ep10_bbq_bpj_event_label" not in event_list) and "ep10_bbq_2dg_event_label" in event_list:
    if ep10_shroom_choice != "DIK":
        $ task_list[5] = "Go to the forest"
    else:
        $ task_list[5] = "Go to the forest"

$ event_list.append("ep10_bbq_final_phase")
$ updateTaskList()
jump endEvent

label ep10_bbq_bpjo_event_label:
scene ep10_bbq_bpjo_event1 with dissolve
js "[name]? I want to play Beer Pong with you."
scene ep10_bbq_bpjo_event2 with dissolve
mc "You? Why?"
scene ep10_bbq_bpjo_event3 with dissolve
js "Because Maya dared me to."
scene ep10_bbq_bpjo_event2 with dissolve
mc "Oh! Haha! That's a good dare."
scene ep10_bbq_bpjo_event4 with dissolve
my "Right! I guess it's a dare for you too, in a way. But not really because I don't think Josy would win."
scene ep10_bbq_bpjo_event5 with dissolve
js "Hey!"
scene ep10_bbq_bpjo_event2 with dissolve
mc "Haha! Did you ever play before?"
scene ep10_bbq_bpjo_event3 with dissolve
js "No, but how hard can it be to throw a ball into a cup?"
scene ep10_bbq_bpjo_event2 with dissolve
mc "You'll see how hard it is. Let's play."
scene ep10_bbq_bpjo_event8 with dissolve
my "This got interesting."
scene ep10_bbq_bpjo_event6 with dissolve
ml "I overheard you guys saying you'll play. I'm so gonna watch this."
scene ep10_bbq_bpjo_event7 with dissolve
my "Who do you think will win?"
scene ep10_bbq_bpjo_event6 with dissolve
ml "My money's on [name], but I hope Josy can beat him. It would be way funnier."

hide screen new_phone_screen
if minigames and not bp_tut_ep10_seen and (tutorials or not persistent.bp_tutorial):
    menu:
        "Watch tutorial":
            $ bp_tut_ep10_seen = True
            $ bp_dlg = 0
            $ bp_jump_label = "ep10_bp_match_josy_label"
            show screen bp_tut_screen
            pause
            $ persistent.bp_tutorial = True
        "Skip tutorial":
            $ renpy.pause(0.5)
label ep10_bp_match_josy_label:
$ renpy.block_rollback()
$ bp_init_game("Josy","ep10","ep10_bp_after_josy_label")
if minigames:
    show screen bp_screen
else:
    show screen bp_screen_nm
pause

label ep10_bp_after_josy_label:
show screen new_phone_screen
if bp_player_won:
    if minigames:
        scene ep10_bbq_bpjo_event9
        hide screen bp_screen
        with dissolve
    else:
        scene ep10_bbq_bpjo_event9
        hide screen bp_screen_nm
        with dissolve
    mc "Sorry, but you lose. And what a way to lose..."
    scene ep10_bbq_bpjo_event10 with dissolve
    js "I'm not removing my panties for this."
    scene ep10_bbq_bpjo_event15 with dissolve
    my "It's part of the dare. Did you come this far to stop at the finish line?"
    scene ep10_bbq_bpjo_event17 with dissolve
    js "Whose side are you on!?"
    scene ep10_bbq_bpjo_event16 with dissolve
    my "Hahaha!"
    scene ep10_bbq_bpjo_event11 with dissolve
    js "I'll do this quick."
    scene ep10_bbq_bpjo_event12 with dissolve
    $ renpy.pause()
    scene ep10_bbq_bpjo_event14 with dissolve
    mc "Woho!!! Way to go, Josy!"
    scene ep10_bbq_bpjo_event13 with dissolve
    js "Shh!!! Not so loud!"
    scene ep10_bbq_bpjo_event15 with dissolve
    my "You can put your clothes back on. You won the dare."
    scene ep10_bbq_bpjo_event18 with dissolve
    js "Thank you!"
    $ new_bio("Josy", "Josy got dared to play Beer Pong against me, and I beat her hard. She had to strip in front of people and felt embarrassed.")
else:
    if minigames:
        scene ep10_bbq_bpjo_event22
        hide screen bp_screen
        with dissolve
    else:
        scene ep10_bbq_bpjo_event22
        hide screen bp_screen_nm
        with dissolve
    js "I win!"
    scene ep10_bbq_bpjo_event20 with dissolve
    ml "I can't believe it! She did it."
    my "This went in a whole other direction than I thought it would."
    scene ep10_bbq_bpjo_event22 with dissolve
    js "Haha! It sure did! But I still won that dare, didn't I?"
    my "You did what I asked, so yes."
    js "[name]? Why are you covering it?"
    scene ep10_bbq_bpjo_event23 with dissolve
    mc "Do I have to show it? Melanie is right there."
    scene ep10_bbq_bpjo_event21 with dissolve
    ml "I sure am."
    scene ep10_bbq_bpjo_event24 with dissolve
    mc "Take a good look because this is all you're getting."
    js "Yay! Haha!"
    my "Hahaha!"
    $ new_bio("Josy", "Josy got dared to play Beer Pong against me, and somehow I lost to her. I ended up showing people my dick as a part of the game.")
scene ep10_bbq_bpjo_event19 with dissolve
ml "You guys are so fucking cool together. You make me miss what I had back in high school."
scene ep10_bbq_bpjo_event25 with dissolve
my "Oh, yeah! Mel was in a relationship with a friend and a guy back in high school."
scene ep10_bbq_bpjo_event26 with dissolve
js "You were?"
scene ep10_bbq_bpjo_event19 with dissolve
ml "Yeah! Let me tell you about it."

$ event_list.append("ep10_bbq_2dg_event_label")
if ep10_shroom_choice != "DIK":
    $ task_list[5] = "Go to the forest"
else:
    $ task_list[5] = "Explore the forest"
$ event_list.append("ep10_bbq_final_phase")
$ updateTaskList()
jump endEvent

label ep10_bbq_nora_event_label:
play sound "sound_effects/cellphone.mp3"
if ep10_shroom_choice == "DIK":
    scene ep10_bbq_nora_event5 with dissolve
    mc "The rock is speaking to me..."
    scene ep10_bbq_nora_event4 with dissolve
    mc "Hello?"
    scene ep10_bbq_nora_event6 with dissolve
else:
    scene ep10_bbq_nora_event1 with dissolve
    "*{i}Cellphone rings{/i}*"
    mc "Hello?"
    scene ep10_bbq_nora_event11 with dissolve

no "[name], it's Nora."
no "I've pondered what to do with us, now that you're a student in my class, but it's a tough decision."
if ep10_shroom_choice == "DIK":
    scene ep10_bbq_nora_event7 with dissolve
    mc "Whoa, Nora..."
else:
    scene ep10_bbq_nora_event2 with dissolve
    mc "Straight to business, huh?"
if ep10_shroom_choice == "DIK":
    scene ep10_bbq_nora_event8 with dissolve
else:
    scene ep10_bbq_nora_event12 with dissolve
no "I have come to a conclusion."
no "It's simply too complicated to date someone I'm teaching, and I have to inform you that I can't date you anymore."
if ep10_shroom_choice == "DIK":
    scene ep10_bbq_nora_event7 with dissolve
    mc "Wait...what? Are you joking?"
else:
    scene ep10_bbq_nora_event2 with dissolve
    mc "You're joking, right?"
if ep10_shroom_choice == "DIK":
    scene ep10_bbq_nora_event8 with dissolve
else:
    scene ep10_bbq_nora_event12 with dissolve
no "I'm afraid I'm not. It's against our rules unless it's disclosed, but that's not something I'm willing to do."
no "I'd be putting my career in jeopardy and would have to find a way around grading your lab report."
no "It involves letting my superiors know about you, and even Professor Willcock would have to learn about it."
no "Sure, it is mitigated by the fact that we met before knowing it would come to this, but as much as it pains me, I cannot continue."
if ep10_shroom_choice == "DIK":
    scene ep10_bbq_nora_event7 with dissolve
else:
    scene ep10_bbq_nora_event3 with dissolve
mc "..."
if ep10_shroom_choice == "DIK":
    scene ep10_bbq_nora_event9 with dissolve
else:
    scene ep10_bbq_nora_event13 with dissolve
no "[name]? Are you still there?"
if ep10_shroom_choice == "DIK":
    scene ep10_bbq_nora_event7 with dissolve
else:
    scene ep10_bbq_nora_event3 with dissolve
mc "You seem to have figured it out, so, I don't know what I can say to change your mind."
mc "I don't want you to risk your job, but it sucks that we have to stop seeing each other because of something we didn't know about."
mc "I thought we had a good connection."
if ep10_shroom_choice == "DIK":
    scene ep10_bbq_nora_event8 with dissolve
else:
    scene ep10_bbq_nora_event12 with dissolve
no "We do. We have a great rapport, and I didn't expect to have much in common with someone of your age."
if ep10_nora_kids:
    no "All things considered, I beat myself up for having to make this call."
    no "I wish our relationship had progressed even further to be able to dare go the other route, but I have to stay realistic."
    no "There is too much at stake, and at the stage I'm at in my life, I can't afford to gamble with my profession."
else:
    no "But we also have some key differences, and when I consider everything about us, it doesn't add up in the long haul."
if ep10_shroom_choice == "DIK":
    scene ep10_bbq_nora_event7 with dissolve
else:
    scene ep10_bbq_nora_event14 with dissolve
mc "What if we keep it a secret? That could work."
if ep10_shroom_choice == "DIK":
    scene ep10_bbq_nora_event9 with dissolve
else:
    scene ep10_bbq_nora_event13 with dissolve
no "It could never work. Things like these don't remain secret for long."
no "All it takes is one mistake and it's out there."
no "And honestly, are you telling me that you haven't told anyone about us?"
if ep10_shroom_choice == "DIK":
    scene ep10_bbq_nora_event7 with dissolve
else:
    scene ep10_bbq_nora_event3 with dissolve
mc "Ok... I see what you mean."
mc "Since you're this determined to end it, I don't think I have anything else to say..."
if ep10_shroom_choice == "DIK":
    scene ep10_bbq_nora_event8 with dissolve
else:
    scene ep10_bbq_nora_event12 with dissolve
no "I'm sorry, [name]. I truly am."
if ep10_shroom_choice == "DIK":
    scene ep10_bbq_nora_event7 with dissolve
else:
    scene ep10_bbq_nora_event14 with dissolve
if persistent.mod_wt_enabled: 
                    $mod_choices = ["(-DIKs)","(+Josy)","(-DIK)","(+DIK)","(-Maya)","(-Josy)","","","","","","" ]
                    #[m_c1][mod_choices[0]]
menu:
    "[m_c1]Don't give up":
        $ ep10_nora_encourage = True
        mc "Me too. I wish you didn't give up on me this easily, but it's your call."
        mc "I hope you'll think some more about it and change your mind."
        $ new_bio("Nora", "Nora called me and said she couldn't continue to date me because of the teacher-student relationship we have. I asked her to rethink her decision, but she felt decided on it.")
    "I get it":
        $ ep10_nora_encourage = False
        mc "Don't be. I get it."
        mc "I won't ask you to change your mind and you have obviously thought about this a lot."
        mc "I guess I'll see you in class..."
        $ new_bio("Nora", "Nora called me and said she couldn't continue to date me because of the teacher-student relationship we have. I told her I understood what she was getting at, even though I didn't want to stop seeing her like that.")
if ep10_shroom_choice == "DIK":
    scene ep10_bbq_nora_event10 with dissolve
else:
    scene ep10_bbq_nora_event12 with dissolve
no "Bye, [name]."

$ task_list[10] = ""
$ updateTaskList()
jump endEvent

label ep10_bbq_q_event_label:
scene ep10_bbq_q_event1 with dissolve
qu "This kumbaya bullshit is getting dull. I need a smoke. Walk with me."
scene ep10_bbq_q_event2 with dissolve
mc "You don't like the party, huh?"
scene ep10_bbq_q_event3 with dissolve
qu "I don't like the wilderness. I need to at least see concrete on the horizon or I get anxious."
scene ep10_bbq_q_event4 with dissolve
mc "You're a weirdo. It's nice getting away from that for a while."
scene ep10_bbq_q_event3 with dissolve
qu "Oh, yeah. The area a whole 10-minute walk away from campus feels refreshing."
scene ep10_bbq_q_event4 with dissolve
mc "What's funnier: You making fun of it or you getting an anxiety attack from something you ridiculed?"
scene ep10_bbq_q_event5 with dissolve
qu "Nice try. It's not an anxiety attack, I just don't like it."
scene ep10_bbq_q_event6 with dissolve
if ep10_shroom_choice == "DIK":
    qu "I'd offer you a hit, but I think you've had enough for tonight."
    scene ep10_bbq_q_event7 with dissolve
    mc "I can handle it."
    scene ep10_bbq_q_event8 with dissolve
    qu "I heard you were looking for a gnome or something. I don't think you can handle more."
    scene ep10_bbq_q_event7 with dissolve
    mc "I can."
    scene ep10_bbq_q_event8 with dissolve
    qu "Come here."
else:
    qu "Want a hit?"
    scene ep10_bbq_q_event7 with dissolve
    mc "No, I'm good."
    scene ep10_bbq_q_event8 with dissolve
    qu "Don't be such a baby. Come here."
scene ep10_bbq_q_event9 with dissolve
$ renpy.pause()
scene ep10_bbq_q_event10 with dissolve
$ renpy.pause()
scene ep10_bbq_q_event11 with dissolve
$ renpy.pause()
scene ep10_bbq_q_event12 with dissolve
qu "Bet you like it when I'm your bong."
scene ep10_bbq_q_event13 with dissolve
mc "I can see why smoking is addictive if you do it like this."
scene ep10_bbq_q_event7 with dissolve
mc "Do you give yourself a discount?"
scene ep10_bbq_q_event14 with dissolve
qu "On weed? Of course. I gotta have some perks."
scene ep10_bbq_q_event7 with dissolve
mc "So... What's your goal with it?"
mc "Selling drugs, I mean."
scene ep10_bbq_q_event14 with dissolve
qu "To make money."
scene ep10_bbq_q_event15 with dissolve
mc "Money for college?"
scene ep10_bbq_q_event16 with dissolve
qu "Money can be used for a lot of things."
scene ep10_bbq_q_event17 with dissolve
mc "Sure, but I'm curious what you're going for. Like, if you wanted to cover your tuition or make some extra on the side."
scene ep10_bbq_q_event16 with dissolve
qu "It's just something I do. I'm not like the rest of you."
scene ep10_bbq_q_event17 with dissolve
mc "Are you uncomfortable talking about it?"
scene ep10_bbq_q_event18 with dissolve
qu "Look, it's not for college. College is the means to an end."
qu "I do what I have to do, to be allowed to stay, but I'm not planning on sticking around for the duration."
scene ep10_bbq_q_event19 with dissolve
mc "Huh? Are you dropping out?"
scene ep10_bbq_q_event18 with dissolve
qu "Eventually, yeah. It's pointless staying here for too long. But for the moment being, it works out for me."
scene ep10_bbq_q_event19 with dissolve
mc "What about the HOTs?"
scene ep10_bbq_q_event18 with dissolve
qu "What about them?"
scene ep10_bbq_q_event19 with dissolve
mc "You're the vice president. I thought you were aiming for the top spot after Sage leaves."
scene ep10_bbq_q_event20 with dissolve
qu "She doesn't know about my plans or what I do. Let's keep it that way, ok?"
qu "And there's nothing that says I have to stay at B&R."
qu "We'll see... Maybe it's for less than a year, maybe it's for longer, but I don't know yet."
scene ep10_bbq_q_event18 with dissolve
qu "I've thought about leading the HOTs and doing things the way I wanted to..."
qu "...but looking at all the bullshit Sage has to deal with every week - every shitty rule she has to follow..."
qu "Having power should be fun, but I think that position would make my stay here worse."
qu "And unlike others, I don't aim to use it as a bullet point on my resume. Fuck that."
scene ep10_bbq_q_event19 with dissolve
mc "..."
scene ep10_bbq_q_event20 with dissolve
qu "What's wrong?"
scene ep10_bbq_q_event19 with dissolve
mc "It makes me sad to hear you say that. I was hoping that you'd stick around for longer."
scene ep10_bbq_q_event20 with dissolve
qu "I'm not skipping town. I'd just be elsewhere."
scene ep10_bbq_q_event19 with dissolve
mc "Yeah, but still... I'd miss you here."
scene ep10_bbq_q_event21 with dissolve
qu "Stop that."
scene ep10_bbq_q_event19 with dissolve
mc "But I would."
scene ep10_bbq_q_event21 with dissolve
qu "Stop crying. I could still crash your stupid parties."
scene ep10_bbq_q_event19 with dissolve
mc "But it would feel different not having you around every day."
scene ep10_bbq_q_event18 with dissolve
qu "I'm not here to study, [name]. You need to get that into your head and be cool with it."
qu "Nothing lasts forever. Everything changes at some point."
qu "You lose friends, you lose family, and yet you're still ok as long as you push on."
scene ep10_bbq_q_event21 with dissolve
qu "Always be brave. Always have pride."
scene ep10_bbq_q_event19 with dissolve
mc "Is this your motivational speech?"
scene ep10_bbq_q_event18 with dissolve
qu "I don't want you to bitch about me leaving, like it's the end of the fucking world. It's bound to happen sometime anyway."
scene ep10_bbq_q_event19 with dissolve
mc "Until that day comes, I'm gonna try my hardest to make you stay longer."
scene ep10_bbq_q_event21 with dissolve
qu "That's...pathetic."
scene ep10_bbq_q_event22 with dissolve
mc "Can I have another hit? Hold the joint."
scene ep10_bbq_q_event23 with dissolve
$ renpy.pause()
scene ep10_bbq_q_event24 with dissolve
$ renpy.pause()
scene ep10_bbq_q_event26 with dissolve
qu "Get back to singing campfire songs, you pretty little choir boy."
scene ep10_bbq_q_event25 with dissolve
mc "I'm sure you'll sit down with us when we start roasting marshmallows."
scene ep10_bbq_q_event27 with dissolve
qu "Eww! I can't believe I kissed you."

$ new_bio("Quinn", "Quinn told me she's not planning on staying in college for long and that her goal with selling drugs is to make lots of money.")
$ task_list[7] = ""
if ep10_rolling:
    if ep10_shroom_choice == "DIK":
        $ task_list[7] = "Find your queen"
    else:
        $ task_list[7] = "Find Lily"
    $ event_list.append("ep10_bbq_lroll_event_label")
$ currentFreeRoamLabel = "ep10_bbq_bench_label"

$ updateTaskList()
$ mgallery_add_photo("ep10_bbq_quinn_pic1")
jump endEvent

label ep10_bbq_2dg_event_label:
scene ep10_bbq_2dg_event1 with dissolve
mc "So, about that dare..."
scene ep10_bbq_2dg_event2 with dissolve
js "It was Maya's idea."
scene ep10_bbq_2dg_event3 with dissolve
my "Sure was."
scene ep10_bbq_2dg_event1 with dissolve
mc "I didn't think we would still be playing, but does that mean it's my turn?"
scene ep10_bbq_2dg_event2 with dissolve
js "Nope, I think it's my turn since I got dared, right?"
mc "Oh..."
scene ep10_bbq_2dg_event4 with dissolve
my "Why? Did you have a good one?"
scene ep10_bbq_2dg_event5 with dissolve
mc "No, but I could have come up with something."
scene ep10_bbq_2dg_event6 with dissolve
my "I almost dared Josy to sleep in your tent tonight because she doesn't want to."
scene ep10_bbq_2dg_event5 with dissolve
mc "Why? That wasn't a bad dare."
scene ep10_bbq_2dg_event7 with dissolve
js "Are you joking? Don't you know how cold it will get overnight?"
scene ep10_bbq_2dg_event5 with dissolve
mc "We have the bonfire that will keep going for a while."
scene ep10_bbq_2dg_event7 with dissolve
js "For a while, yes. What about after that?"
js "I'm telling you, you will freeze your butt off if you sleep there tonight."
scene ep10_bbq_2dg_event5 with dissolve
mc "You're a wuss."
scene ep10_bbq_2dg_event8 with dissolve
js "*{i}Gasp{/i}* I'm not a wuss! I'm tough! I just completed a dare!"
scene ep10_bbq_2dg_event9 with dissolve
my "Haha! Yeah, but still...you're kind of a wuss."
scene ep10_bbq_2dg_event11 with dissolve
js "If you two are sooo brave..."
js "I dare you to..."
scene ep10_bbq_2dg_event10 with dissolve
my "Oh no..."
scene ep10_bbq_2dg_event12 with dissolve
js "[name]! I dare you to have sex with...uh...behind the porta potties."
scene ep10_bbq_2dg_event13 with dissolve
mc "With who? With Maya?"
scene ep10_bbq_2dg_event14 with dissolve
js "I was gonna say with Maya, but I stopped myself mid-sentence because I want it too. Haha!"
scene ep10_bbq_2dg_event9 with dissolve
my "We can't all have sex behind the toilets."
scene ep10_bbq_2dg_event15 with dissolve
js "No, you're right. Someone would have to keep watch..."
js "Let's tag team it!"
scene ep10_bbq_2dg_event16 with dissolve
mc "This is sounding less like a dare, and more like something both of you wanna do."
scene ep10_bbq_2dg_event12 with dissolve
js "Well, then I dare you to do it."
scene ep10_bbq_2dg_event13 with dissolve
mc "Does it mean I get to dare you next?"
scene ep10_bbq_2dg_event14 with dissolve
js "Yes."
scene ep10_bbq_2dg_event13 with dissolve
mc "Ok, I'll do it."
stop music fadeout 3
scene ep10_bbq_2dg_event16 with dissolve
mc "But also, psych! I would do it without the dare too. Haha!"

label ep10_jm_lewd_label:
if _in_replay:
    if persistent.name == None:
        $ name = "MC"
    else:
        $ name = persistent.name
    if persistent.mc_josy == None:
        $ mc_josy = name
    else:
        $ mc_josy = persistent.mc_josy
    if persistent.josy == None:
        $ josy = "Josy"
    else:
        $ josy = persistent.josy
    if persistent.mc_maya == None:
        $ mc_maya = name
    else:
        $ mc_maya = persistent.mc_maya
    if persistent.maya == None:
        $ maya = "Maya"
    else:
        $ maya = persistent.maya

play music "music/ep9/licensed_music/track126.mp3"
hide screen new_phone_screen

scene ep10_jm_lewd1 with wipeleft
js "Question is... Who goes back there first?"
scene ep10_jm_lewd2 with dissolve
menu:
    "Foreplay with Maya":
        scene ep10_jm_lewd3 with hpunch
        mc "Maya, let's go!"
        my "Whoa! Haha! Ok."
        scene ep10_jm_lewd4 with dissolve
        js "I'll warn you if someone comes, ok?"

        scene ep10_jm_lewd18 with dissolve
        mc "You girls are crazy..."
        scene ep10_jm_lewd19 with dissolve
        my "Haha! I blame Josy for this. But I'm not going to wuss out before she does."
        scene anim_jm_hj1_ep10 with dissolve
        my "*{i}Smack{/i}*"
        my "You're not hard yet."
        mc "It's cold outside, but I'm getting there."
        pause


        scene ep10_jm_lewd23 with dissolve
        my "Yeah, it's cold, but I know something that's warm."
        scene ep10_jm_lewd22 with dissolve
        my "Do you want me to put it in my mouth?"
        scene ep10_jm_lewd21 with dissolve
        mc "Yeah, suck on it."

        scene ep10_jm_lewd20 with dissolve
        mc "Fuck..."

        scene anim_jm_bj1_ep10 with dissolve
        my "*{i}Suck suck{/i}*"
        mc "Ah, yes... Like that. Now, that's warm."
        pause
        scene anim_jm_bj2_ep10 with dissolve
        my "*{i}Suck glug{/i}* Mmpphhff..."
        mc "Damn, now you've got me going."
        pause

        scene ep10_jm_lewd24 with dissolve
        my "Haha, good... I'm gonna swap with Josy or else I'll end up keeping you all to myself."

        scene ep10_jm_lewd5 with dissolve
        my "He's ready for you. Get back there."

        scene ep10_jm_lewd29 with dissolve
        js "I got wet overhearing you guys moaning..."
        scene ep10_jm_lewd30 with dissolve
        js "You gotta put it in me, [mc_josy]... I want it now."
        $ tmpInt = 0
        label ep10_jm_lewd_loop_label:
        menu:
            "From behind":
                $ tmpInt += 1
                scene anim_jm_doggy1_ep10 with dissolve
                pause
                scene anim_jm_doggy2_ep10 with dissolve
                pause
                jump ep10_jm_lewd_loop_label
            "Facing her":
                $ tmpInt += 1
                scene anim_jm_miss1_ep10 with dissolve
                pause
                scene anim_jm_miss2_ep10 with dissolve
                pause
                jump ep10_jm_lewd_loop_label
            "Switch to Maya" if tmpInt > 0:
                $ renpy.pause(0.5)

        scene ep10_jm_lewd6 with dissolve
        my "Is it my turn yet?"
        scene ep10_jm_lewd7 with dissolve
        js "Yeah, get back there."

        scene ep10_jm_lewd25 with dissolve
        my "Good, I was worried I wouldn't get another turn. Haha!"
        scene ep10_jm_lewd26 with dissolve
        label ep10_jm_lewd_loop2b_label:
        menu:
            "From behind":
                scene ep10_jm_lewd27 with dissolve
                my "Put it in me, [mc_maya]."
                scene anim_jm_doggy3_ep10 with dissolve
                pause
                scene anim_jm_doggy4_ep10 with dissolve
                pause
                scene anim_jm_doggy5_ep10 with dissolve
                pause
                jump ep10_jm_lewd_loop2b_label
            "Facing her":
                scene anim_jm_miss3_ep10 with dissolve
                pause
                scene anim_jm_miss4_ep10 with dissolve
                pause
                jump ep10_jm_lewd_loop2b_label
            "Get ready to cum":
                mc "I think I'm about to cum..."
                my "Josy, he's close!"
    "Foreplay with Josy":

        scene ep10_jm_lewd11 with dissolve
        mc "It was your idea, you're gonna start us off."
        scene ep10_jm_lewd12 with dissolve
        my "I'll keep a lookout."

        scene ep10_jm_lewd28 with dissolve
        mc "You girls are crazy..."
        scene ep10_jm_lewd29 with dissolve
        js "Haha, and I think you love it."

        scene anim_jm_bj3_ep10 with dissolve
        js "*{i}Suck suck{/i}*"
        pause
        scene anim_jm_bj4_ep10 with dissolve
        js "*{i}Suck suck{/i}* Mmppffhhh..."
        pause
        scene ep10_jm_lewd6 with dissolve
        my "You guys have to be more quiet."
        scene ep10_jm_lewd7 with dissolve
        js "You're up. He's rock hard."

        scene ep10_jm_lewd31 with dissolve
        my "She wasn't kidding... You're good to go, aren't you?"
        scene ep10_jm_lewd32 with dissolve
        mc "Yeah... What about you?"
        scene ep10_jm_lewd25 with dissolve
        my "Believe me... Hearing you guys moan like that, I'll get there fast. How do you want me?"
        scene ep10_jm_lewd26 with dissolve
        $ tmpInt = 0
        label ep10_jm_lewd_loop2_label:
        menu:
            "From behind":
                $ tmpInt += 1
                scene ep10_jm_lewd27 with dissolve
                my "Put it in me, [mc_maya]."
                scene anim_jm_doggy3_ep10 with dissolve
                pause
                scene anim_jm_doggy4_ep10 with dissolve
                pause
                scene anim_jm_doggy5_ep10 with dissolve
                pause
                jump ep10_jm_lewd_loop2_label
            "Facing her":
                $ tmpInt += 1
                scene anim_jm_miss3_ep10 with dissolve
                pause
                scene anim_jm_miss4_ep10 with dissolve
                pause
                jump ep10_jm_lewd_loop2_label
            "Switch to Josy" if tmpInt > 0:
                $ renpy.pause(0.5)

        scene ep10_jm_lewd9 with dissolve
        js "Guys?"
        scene ep10_jm_lewd10 with dissolve
        my "*{i}Moans{/i}* Is someone coming?"
        scene ep10_jm_lewd9 with dissolve
        js "No, but I want to."
        scene ep10_jm_lewd8 with dissolve
        my "Go get him."

        scene ep10_jm_lewd29 with dissolve
        js "Finally! I got soo horny overhearing you guys moaning..."
        scene ep10_jm_lewd30 with dissolve
        label ep10_jm_lewd_loopb_label:
        menu:
            "From behind":
                scene anim_jm_doggy1_ep10 with dissolve
                pause
                scene anim_jm_doggy2_ep10 with dissolve
                pause
                jump ep10_jm_lewd_loopb_label
            "Facing her":
                scene anim_jm_miss1_ep10 with dissolve
                pause
                scene anim_jm_miss2_ep10 with dissolve
                pause
                jump ep10_jm_lewd_loopb_label
            "Get ready to cum":
                mc "I think I'm about to cum..."
                js "Maya, get back here!"

scene anim_jm_bj5_ep10 with dissolve
pause
scene ep10_jm_lewd33 at vpunch, cum2
$ renpy.pause(0.5)
scene ep10_jm_lewd33 at vpunch, cum2
$ renpy.pause(0.5)
scene ep10_jm_lewd33 at vpunch, cum2
mc "FUCK!!! Ahhh!!!"
scene ep10_jm_lewd34 with dissolve
mc "Wow... You girls are unbelievable, especially when you're together."

scene ep10_jm_lewd35 with dissolve
js "We made a big mess. Haha!"
scene ep10_jm_lewd36 with dissolve
my "That was so hot... We went for it, didn't we?"
scene ep10_jm_lewd37 with dissolve
js "Oh, no... No one's watching the front."
scene ep10_jm_lewd34 with dissolve
mc "Let me do it. Help each other clean up."
scene ep10_jm_lewd38 with dissolve
js "Haha! *{i}Lick lick{/i}* I'll help you get that off."
my "Hahaha!"

scene ep10_jm_lewd13 with dissolve
js "All good?"
scene ep10_jm_lewd14 with dissolve
mc "Yep... All is good."
scene ep10_jm_lewd15 with dissolve
my "Maybe we shouldn't get back all at once?"
scene ep10_jm_lewd14 with dissolve
mc "You girls go ahead, I'll stay behind for a few minutes."
mc "And also... I dare both of you to sleep together with me in my tent tonight."
scene ep10_jm_lewd17 with dissolve
js "What? No..."
scene ep10_jm_lewd16 with dissolve
stop music fadeout 3
mc "Think about it on your walk back. There's bound to be a dare that one of you won't do. Right?"

$ renpy.end_replay()
$ persistent.ep10_lewd_jm = True
$ calcScenes()
$ new_bio("Josy", "The Dare Game lives on, and because of it, I had public sex with Josy and Maya at the DIKs' Thanksgiving party.")
$ new_bio("Maya", "The Dare Game lives on, and because of it, I had public sex with Josy and Maya at the DIKs' Thanksgiving party.")
$ mphone_stats_add_girl_s3("josy","You had sex with Josy and Maya at the DIKs' Thanksgiving party in episode 10.")
$ mphone_stats_add_girl_s3("maya","You had sex with Josy and Maya at the DIKs' Thanksgiving party in episode 10.")
show screen new_phone_screen
$ task_list[5] = ""


if "ep10_bbq_bps_event_label" in event_list or "ep10_bbq_bpjo_event_label" in event_list or "ep10_bbq_bpj_event_label" in event_list:
    if ep10_shroom_choice != "DIK":
        $ task_list[5] = "Play Beer Pong"
    else:
        $ task_list[5] = "Throw the white sphere"
        
if ("ep10_bbq_bps_event_label" in event_list or "ep10_bbq_bpjo_event_label" in event_list or "ep10_bbq_bpj_event_label" in event_list) and "ep10_bbq_2dg_event_label" in event_list:
    if ep10_shroom_choice != "DIK":
        $ task_list[5] = "Play Beer Pong\nGo to the forest"
    else:
        $ task_list[5] = "Throw the white sphere\nGo to the forest"
        
if ("ep10_bbq_bps_event_label" not in event_list and "ep10_bbq_bpjo_event_label" not in event_list and "ep10_bbq_bpj_event_label" not in event_list) and "ep10_bbq_2dg_event_label" in event_list:
    if ep10_shroom_choice != "DIK":
        $ task_list[5] = "Go to the forest"
    else:
        $ task_list[5] = "Go to the forest"


$ updateTaskList()
$ mphone_next_song()
jump endEvent

label ep10_bbq_jm_end_event_label:
scene ep10_bbq_jm_end_event1 with dissolve
js "People are starting to leave. We should get some rest for tomorrow too."
scene ep10_bbq_jm_end_event3 with dissolve
mc "Yeah, we need to be alert tomorrow."
scene ep10_bbq_jm_end_event2 with dissolve
my "Yep, I didn't even drink that much tonight."
scene ep10_bbq_jm_end_event8 with dissolve
mc "I guess it's time for us to get some shuteye. After you, girls."
scene ep10_bbq_jm_end_event5 with dissolve
js "Come on... Weren't you joking about that dare?"
scene ep10_bbq_jm_end_event4 with dissolve
mc "It's not that bad to sleep in a tent."
scene ep10_bbq_jm_end_event5 with dissolve
js "It's not the tent that I mind, it's the month. I saw frost on the grass this week and they say it will snow soon."
scene ep10_bbq_jm_end_event3 with dissolve
mc "Don't be a baby. It's right there, next to the fire. And I have a nice blanket in there."
mc "Also, I'm going to sleep in my clothes and we'll keep each other warm."
mc "If anything, I think it will get too hot."
scene ep10_bbq_jm_end_event6 with dissolve
js "Maya, say something. He's poking holes in my argument here."
scene ep10_bbq_jm_end_event7 with dissolve
my "I'm convinced as it is. I'm staying here tonight."
scene ep10_bbq_jm_end_event6 with dissolve
js "You're supposed to be on my side."
scene ep10_bbq_jm_end_event7 with dissolve
my "Don't you remember the last time we spent the night in a tent together?"
scene ep10_bbq_jm_end_event6 with dissolve
js "It wasn't in November!"
scene ep10_bbq_jm_end_event9 with dissolve
my "I think Josy chickened out on the dare. [name], let's get in there."
mc "Haha, I knew she would cave at some point. But I didn't think it would be something as stupid as this."
scene ep10_bbq_jm_end_event10 with dissolve
js "If I get pneumonia from this, I'm never listening to you two ever again."
scene ep10_bbq_jm_end_event11 with dissolve
my "Changed your mind, did you?"
scene ep10_bbq_jm_end_event12 with dissolve
js "I've never been good with peer pressure. And I'm not losing this chicken race that [name] started."
scene ep10_bbq_jm_end_event13 with dissolve
mc "Haha, don't worry. You'll like it here. It's only for a night."
scene ep10_bbq_jm_end_event14 with dissolve
js "I'm counting on you to keep me warm. And for once, I don't mean it in a sexual way."
my "Hahaha!"
scene ep10_bbq_jm_end_event15 with dissolve
$ renpy.pause()
jump ep10_party_eval_label

label ep10_bbq_jill_end_event_label:
scene ep10_bbq_jill_end_event1 with dissolve
ji "I was going to head back home soon, and the girls told me you're sleeping here overnight."
scene ep10_bbq_jill_end_event2 with dissolve
mc "Yeah, I will. It took us a couple of hours putting these tents up, so it would be a waste not to."
mc "You're welcome to join me if you want."
scene ep10_bbq_jill_end_event3 with dissolve
ji "Oh, I don't know. I didn't bring anything for a sleepover."
scene ep10_bbq_jill_end_event2 with dissolve
mc "What do you need? Pillow and blanket? Because I got them."
scene ep10_bbq_jill_end_event3 with dissolve
ji "Won't it get cold?"
scene ep10_bbq_jill_end_event2 with dissolve
mc "Why is that everyone's remark?"
scene ep10_bbq_jill_end_event4 with dissolve
ji "Because it's cold. Haha!"
scene ep10_bbq_jill_end_event2 with dissolve
mc "The bonfire is hot and it will hopefully last overnight."
scene ep10_bbq_jill_end_event3 with dissolve
ji "If you're sure."
scene ep10_bbq_jill_end_event2 with dissolve
mc "If we wake up in the middle of the night and we're freezing, we head back to my place immediately. Ok?"
scene ep10_bbq_jill_end_event5 with dissolve
ji "After you."
scene ep10_bbq_jill_end_event6 with dissolve
mc "Have you camped a lot?"
scene ep10_bbq_jill_end_event7 with dissolve
ji "Not a lot. You?"
scene ep10_bbq_jill_end_event6 with dissolve
mc "Nope."
scene ep10_bbq_jill_end_event7 with dissolve
ji "Yet you're confident this will work out fine."
scene ep10_bbq_jill_end_event6 with dissolve
mc "Sometimes you gotta live a little."
scene ep10_bbq_jill_end_event7 with dissolve
if ep10_shroom_choice == "DIK":
    ji "I think you've lived an awful lot tonight."
else:
    ji "I suppose."
scene ep10_bbq_jill_end_event8 with dissolve
ji "Please, don't get mad if I wake you up shuddering."
scene ep10_bbq_jill_end_event9 with dissolve
mc "I promise."
mc "Thanks for doing this for me. Everyone saying it was a stupid idea..."
mc "It kinda made me feel bad for planning it."
scene ep10_bbq_jill_end_event8 with dissolve
ji "Don't feel bad. You did great."
ji "I've had a good time and some fun conversations."
ji "You should sleep. Tomorrow is a big day for you."
scene ep10_bbq_jill_end_event9 with dissolve
mc "Yeah..."
scene ep10_bbq_jill_end_event10 with dissolve
ji "Please, be safe."
scene ep10_bbq_jill_end_event9 with dissolve
mc "I'll try my best."
stop music fadeout 3
scene ep10_bbq_jm_end_event15 with dissolve
$ renpy.pause()
jump ep10_party_eval_label
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
