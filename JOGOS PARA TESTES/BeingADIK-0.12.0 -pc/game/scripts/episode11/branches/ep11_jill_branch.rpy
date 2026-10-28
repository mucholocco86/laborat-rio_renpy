label ep11_jhome_label:
scene ep11_jhome1 with dissolve
$ renpy.pause()
scene ep11_jhome2 with dissolve
mc "I'm so happy you came back home with me. You seemed to enjoy yourself tonight."
scene ep11_jhome3 with dissolve
ji "I did. Your dad is a lot of fun and caring."
scene ep11_shome4 with dissolve
mc "And embarrassing..."
scene ep11_jhome3 with dissolve
ji "I found it cute. I learned things about you that you wouldn't have shared with me."
scene ep11_jhome4 with dissolve
mc "He didn't scare you away with those stories, right?"
scene ep11_jhome5 with dissolve
ji "Like someone could ever scare me away from you."
scene ep11_jhome6 with dissolve
mc "It feels great that you've gotten to meet him."
scene ep11_jhome5 with dissolve
ji "It's a shame I have to leave tomorrow. I would have loved to get to know Neil even better."
scene ep11_jhome6 with dissolve
mc "There will be more times to come, won't there?"
scene ep11_jhome7 with dissolve
ji "I can't say why there wouldn't be."
scene ep11_jhome8 with dissolve
ji "Tell me, what are you doing for the rest of your weekend?"
scene ep11_jhome9 with dissolve
mc "Nothing much. We'll catch up more and relax."
mc "And I...uh... I plan to visit a friend tomorrow."
scene ep11_jhome11 with dissolve
ji "That's nice. You should. It's always fun to catch up with friends you don't see daily."
ji "When was the last time you saw him?"
scene ep11_jhome10 with dissolve
mc "Her. And she was at the BBQ party."
scene ep11_jhome11 with dissolve
ji "Oh? Who is it?"
scene ep11_jhome10 with dissolve
mc "I don't know if you talked to her. Her name is Zoey. She's got blue hair."
if ep9_winner == "Zoey":
    scene ep11_jhome11 with dissolve
    ji "Oh! She's the one who won the best costume at Halloween."
    scene ep11_jhome10 with dissolve
    mc "Yeah, that's her."
    scene ep11_jhome11 with dissolve
else:
    scene ep11_jhome11 with dissolve
    ji "I think I know who that is. I've seen her around."
ji "So, you two are friends from before?"
scene ep11_jhome14 with dissolve
mc "Since childhood. Zoey has helped me through rough times."
mc "When I was bullied at school, she became my best friend."
scene ep11_jhome12 with dissolve
ji "Aw, that's so sweet. I'd love to meet her."
scene ep11_jhome14 with dissolve
mc "Yeah, but... This is awkward."
mc "Look, I'm just gonna say it, ok? She was my first girlfriend, too."
scene ep11_jhome13 with dissolve
ji "Oh?"
scene ep11_jhome14 with dissolve
mc "It's complicated."
scene ep11_jhome15 with dissolve
ji "So, when you said you were visiting your friend tomorrow... You're actually visiting your ex-girlfriend."
scene ep11_jhome16 with dissolve
mc "She's both. But for most of my life, she's been my best friend."
mc "She recently came back into my life; she'd been living in San Diego for a while."
scene ep11_jhome17 with dissolve
ji "Ok."
scene ep11_jhome16 with dissolve
mc "Does this feel weird to you?"
scene ep11_jhome17 with dissolve
ji "It kind of does. Um..."
scene ep11_jhome16 with dissolve
mc "I'm telling you this because I don't want to hide it from you."
mc "And, trust me, there's nothing to hide either."
scene ep11_jhome15 with dissolve
ji "Ok..."
ji "Is she back to being your best friend or...?"
scene ep11_jhome16 with dissolve
if ep9_mad_at_zoey:
    mc "She left me suddenly, and I've been angry with her. But she meant a lot to me in the past."
else:
    mc "She means a lot to me. Her friendship, I mean."
mc "I'm trying to find out if we can still be friends or if it's too weird."
scene ep11_jhome17 with dissolve
ji "Well... You do you, then."
scene ep11_jhome16 with dissolve
mc "Thanks. I didn't want you to feel worried about it; I wanted to tell you about her."
stop music fadeout 3
scene ep11_jhome18 with dissolve
ji "..."
if "Jill" not in tmp_mod_list:
    $ new_bio("Jill", "Dad and Jill got along great when I brought her home to meet him.")
    $ new_bio("Jill", "I told Jill about Zoey and what she meant to me. She didn't have many questions about it.")
    $ new_bio("Dad", "Dad and Jill got along great when I brought her home to meet him.")
    $ tmp_mod_list.append("Jill")
if wt_ep9_branch_numbers > 1:

    "scrappy" "Do you want to see this scene on other paths?"
    menu:
        "Yes":
            jump ep11_home_label
        "No. Continue the game.":
            pass

jump ep11_zoey_home_label

label ep11_jgifts_label:
$ guideSuggestedPage = 224
play music "music/ep11/licensed_music/track160.mp3"
queue music["music/ep2/journey_of_hope.mp3","music/ep11/licensed_music/track161.mp3","music/ep11/licensed_music/track160.mp3"]
scene ep11_jgifts1 with wipeleft
$ renpy.pause()
scene ep11_jgifts2 with dissolve
mc "I like what they did with the mall."
scene ep11_jgifts3 with dissolve
mc "What?"
scene ep11_jgifts4 with dissolve
ji "I think you're cute."
scene ep11_jgifts3 with dissolve
mc "Why?"
scene ep11_jgifts4 with dissolve
ji "For wanting to go Christmas gift shopping like this."
scene ep11_jgifts5 with dissolve
if ep11_gift_list.count(0) > 3:
    mc "I have some great ones planned."
elif ep11_gift_list.count(0) > 1:
    mc "I don't have much to spend, just a little. And I wanna buy something for Dad."
else:
    mc "Just one for Dad. I don't have much to spend."
scene ep11_jgifts6 with dissolve
ji "Don't feel pressured to get me something. Really. You don't have to."
scene ep11_jgifts7 with dissolve

if persistent.mod_wtenabled: 
                        $mod_choices = ["(+Jill)","(-3 Jill)","(-DIK)","(+DIK)","(+5 Josy)","(-5 Josy)","","","","","","" ]
                        #[mod_gr][mod_choices[0]]
                        #\n{size=-4}[m_c1][mod_choices[1]][m_c2][mod_choices[4]]

menu:
    "Are you getting something for me?":
        mc "Are you getting something for me?"
        scene ep11_jgifts8 with dissolve
        ji "I'm not telling you."
        scene ep11_jgifts7 with dissolve
        mc "Aha, but it's ok for you to pry?"
        scene ep11_jgifts8 with dissolve
        ji "Haha! I'm not prying. I said you are cute for doing this."
        scene ep11_jgifts7 with dissolve
    "But I want to \n{size=-4}[m_c1][mod_choices[0]]" if ep11_gift_list[2] > 0:
        $ RPjill += 1
        mc "But I want to."
        scene ep11_jgifts8 with dissolve
        ji "Now you're even cuter."
        scene ep11_jgifts7 with dissolve
    "I wasn't going to \n{size=-4}[m_c1][mod_choices[1]]" if ep11_gift_list[2] == 0:
        $ RPjill -= 3
        mc "I wasn't going to... Should I have?"
        scene ep11_jgifts9 with dissolve
        ji "No...um... Don't force anything. It would make me feel bad."
        scene ep11_jgifts10 with dissolve
        mc "Ok."
mc "What are you getting today?"
scene ep11_jgifts11 with dissolve
ji "I'm considering purchasing some new clothes."
scene ep11_jgifts12 with dissolve
mc "Good thing you brought me with you then."
scene ep11_jgifts11 with dissolve
ji "Oh, yeah? How so?"
scene ep11_jgifts12 with dissolve
mc "To help you pick what to wear, of course."
scene ep11_jgifts13 with dissolve
ji "I'm not going to spend an hour trying on bras, [name]."
scene ep11_jgifts14 with dissolve
mc "Ha-ha. Let's not make any rash decisions before we see what they've got."
scene ep11_jgifts15 with wipeleft
ji "How about this one?"
scene ep11_jgifts16 with dissolve
mc "Don't you have one of those?"
scene ep11_jgifts17 with dissolve
ji "Not in this shade."
scene ep11_jgifts18 with dissolve
mc "I mean, sure, if you like it."
scene ep11_jgifts19 with dissolve
ji "You don't sound too convinced."
scene ep11_jgifts18 with dissolve
mc "How about you try something new? Something you wouldn't have picked if I wasn't here."
scene ep11_jgifts19 with dissolve
ji "Are you trying to get me to dress as someone I'm not?"
scene ep11_jgifts18 with dissolve
mc "Huh? No, I didn't mean it like that. But maybe you can try something new and see if you like it."
mc "I can see several things in here I'd like to see you try on."
label ep11_jill2_lewd_label:
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
    $ ep11_jill_style = 0
    $ RPjill = 0
    play music "music/ep11/licensed_music/track160.mp3"
    queue music["music/ep2/journey_of_hope.mp3","music/ep11/licensed_music/track161.mp3","music/ep11/licensed_music/track160.mp3"]
hide screen new_phone_screen
scene ep11_jgifts20 with dissolve
ji "I'm going to try on this dress. How about you pick something you'd like me to try and meet me by the dressing room?"
scene ep11_jgifts21 with dissolve
mc "Now we're talking."
scene ep11_jgifts22 with dissolve
mc "(Hm... Let's push her boundaries a bit.)"
scene ep11_jgifts23 with dissolve
mc "(Nice one. But that cleavage might be too much for her...)"
scene ep11_jgifts24 with dissolve
mc "(This outfit screams confidence. But the ripped jeans and holes in the shirt are definitely out of her comfort zone.)"
scene ep11_jgifts25 with dissolve
mc "(This isn't a revealing outfit. It's casual. But not Jill's kind of casual.)"
scene ep11_jgifts26 with dissolve
mc "(And those jeans make the butt look nice.)"
scene ep11_jgifts27 with dissolve
mc "(I don't think she'd choose any of these outfits for herself... But I think she'd look best in...)"
menu:
    "Left style":
        $ ep11_jill_style = 1
        scene ep11_jgifts23 with dissolve
        mc "(...in this one. Yeah, I wanna see her try this on.)"
    "Middle style":
        $ ep11_jill_style = 2
        scene ep11_jgifts24 with dissolve
        mc "(...in this one. Yeah, I wanna see her try this on.)"
    "Right style":
        $ ep11_jill_style = 3
        scene ep11_jgifts25 with dissolve
        mc "(...in this one. Yeah, I wanna see her try this on.)"
mc "(Yeah, she'll rock this one.)"
scene ep11_jgifts28 with dissolve
mc "Jill?"
play sound "sound_effects/shower_curtain.mp3"
scene ep11_jgifts29 with dissolve
ji "I'm in here. What do you think?"
scene ep11_jgifts30 with dissolve
mc "You're pretty. It's you in another color. So, it fits you."
scene ep11_jgifts31 with dissolve
ji "*{i}Sigh{/i}* I'm not getting it then."
scene ep11_jgifts30 with dissolve
mc "Sorry. I'm not trying to put you down, but do you need another one of those dresses?"
scene ep11_jgifts31 with dissolve
ji "No, you're right. But I like it and figured another shade wouldn't hurt."
scene ep11_jgifts32 with dissolve
mc "Then get it."
scene ep11_jgifts33 with dissolve
ji "I'm more interested in what you're carrying in your arms."
scene ep11_jgifts34 with dissolve
mc "Try these on. If you need another size, shout at me."
scene ep11_jgifts35 with dissolve
ji "Oh, dear..."
scene ep11_jgifts36 with dissolve
mc "Is the size good?"
scene ep11_jgifts37 with dissolve
ji "Yeah, but they're...tight."
scene ep11_jgifts36 with dissolve
mc "Too tight?"
scene ep11_jgifts37 with dissolve
ji "No. Maybe. Yes. I don't know."
ji "This doesn't feel like me."
scene ep11_jgifts36 with dissolve
mc "Hey, don't say that. Let me see it first."
play sound "sound_effects/shower_curtain.mp3"
if ep11_jill_style == 1:
    scene ep11_jgifts38a with dissolve
elif ep11_jill_style == 2:
    scene ep11_jgifts38b with dissolve
else:
    scene ep11_jgifts38c with dissolve
$ renpy.pause()
if ep11_jill_style == 1:
    scene ep11_jgifts39a with dissolve
elif ep11_jill_style == 2:
    scene ep11_jgifts39b with dissolve
else:
    scene ep11_jgifts39c with dissolve
$ renpy.pause()
if ep11_jill_style == 1:
    scene ep11_jgifts40a with dissolve
elif ep11_jill_style == 2:
    scene ep11_jgifts40b with dissolve
else:
    scene ep11_jgifts40c with dissolve
mc "Can you turn around?"
if ep11_jill_style == 1:
    scene ep11_jgifts41a with dissolve
elif ep11_jill_style == 2:
    scene ep11_jgifts41b with dissolve
else:
    scene ep11_jgifts41c with dissolve
ji "So? What do you think?"
if ep11_jill_style == 1:
    scene ep11_jgifts42a with dissolve
elif ep11_jill_style == 2:
    scene ep11_jgifts42b with dissolve
else:
    scene ep11_jgifts42c with dissolve
menu:
    "[m_c1]You look great":
        $ tmpBool3 = False
        mc "I think you look great."
        if ep11_jill_style == 1:
            scene ep11_jgifts43a with dissolve
            ji "It feels like my breasts are too...prominent in this."
        elif ep11_jill_style == 2:
            scene ep11_jgifts43b with dissolve
            ji "There are so many holes in these clothes. Don't they sell these without them?"
        else:
            scene ep11_jgifts43c with dissolve
            ji "I feel weird in this. And the jeans are very...tight."
        if ep11_jill_style == 1:
            scene ep11_jgifts44a with dissolve
        elif ep11_jill_style == 2:
            scene ep11_jgifts44b with dissolve
        else:
            scene ep11_jgifts44c with dissolve
        
        if persistent.mod_wtenabled: 
                        $mod_choices = ["(+Jill)","(-3 Jill)","(-DIK)","(+DIK)","(+5 Josy)","(-5 Josy)","","","","","","" ]
                        #[mod_gr][mod_choices[0]]
                        #\n{size=-4}[m_c1][mod_choices[1]][m_c2][mod_choices[4]]
        
        menu:
            "Reassure her \n{size=-4}[m_c1][mod_choices[0]]":
                $ RPjill += 1
                if ep11_jill_style == 1:
                    scene ep11_jgifts46a with dissolve
                    mc "There's more cleavage than you're used to, but don't worry about it."
                elif ep11_jill_style == 2:
                    scene ep11_jgifts46b with dissolve
                    mc "The holes are part of the design."
                else:
                    scene ep11_jgifts46c with dissolve
                    mc "It's a casual look. But both the hoodie and the jeans fit great!"
                mc "You look amazing in that outfit. You're probably feeling that way because it's new to you."
            "Joke":
                if ep11_jill_style == 1:
                    mc "That's why I like it."
                    scene ep11_jgifts45a with dissolve
                elif ep11_jill_style == 2:
                    mc "The holes are there for a reason."
                    scene ep11_jgifts45b with dissolve
                else:
                    mc "That's why I like it."
                    scene ep11_jgifts45c with dissolve
                ji "Bah."
                if ep11_jill_style == 1:
                    scene ep11_jgifts44a with dissolve
                elif ep11_jill_style == 2:
                    scene ep11_jgifts44b with dissolve
                else:
                    scene ep11_jgifts44c with dissolve
                mc "I'm joking, haha. But seriously, you look amazing in that outfit."
        mc "Have a look in the mirror."
        if ep11_jill_style == 1:
            scene ep11_jgifts47a with dissolve
        elif ep11_jill_style == 2:
            scene ep11_jgifts47b with dissolve
        else:
            scene ep11_jgifts47c with dissolve
        ji "Hm..."
        if ep11_jill_style == 1:
            scene ep11_jgifts48a with dissolve
        elif ep11_jill_style == 2:
            scene ep11_jgifts48b with dissolve
        else:
            scene ep11_jgifts48c with dissolve
        ji "Where would I wear this?"
        if ep11_jill_style == 1:
            scene ep11_jgifts49a with dissolve
        elif ep11_jill_style == 2:
            scene ep11_jgifts49b with dissolve
        else:
            scene ep11_jgifts49c with dissolve
        mc "At school?"
        if ep11_jill_style == 1:
            scene ep11_jgifts48a with dissolve
        elif ep11_jill_style == 2:
            scene ep11_jgifts48b with dissolve
        else:
            scene ep11_jgifts48c with dissolve
        ji "I don't think so."
        if ep11_jill_style == 1:
            scene ep11_jgifts49a with dissolve
        elif ep11_jill_style == 2:
            scene ep11_jgifts49b with dissolve
        else:
            scene ep11_jgifts49c with dissolve
        mc "When you're with me?"
        if ep11_jill_style == 1:
            scene ep11_jgifts50a with dissolve
        elif ep11_jill_style == 2:
            scene ep11_jgifts50b with dissolve
        else:
            scene ep11_jgifts50c with dissolve
        ji "I suppose..."
        ji "Do you think I look good in it? Don't say I do if you don't think so."
        if ep11_jill_style == 1:
            scene ep11_jgifts51a with dissolve
        elif ep11_jill_style == 2:
            scene ep11_jgifts51b with dissolve
        else:
            scene ep11_jgifts51c with dissolve
        menu:
            "Get that outfit":
                mc "You should get that outfit. You might not think it's you, but it is."
            "It's your choice":
                mc "It's your choice. If you're not comfortable with it, you shouldn't get it. But I think you look good in it."
        if ep11_jill_style == 1:
            scene ep11_jgifts52a with dissolve
        elif ep11_jill_style == 2:
            scene ep11_jgifts52b with dissolve
        else:
            scene ep11_jgifts52c with dissolve
        ji "This is something Lana would wear."
        ji "Ok, I'm getting it."
        if ep11_jill_style == 1:
            scene ep11_jgifts53a with dissolve
        elif ep11_jill_style == 2:
            scene ep11_jgifts53b with dissolve
        else:
            scene ep11_jgifts53c with dissolve
        mc "You are?"
        if ep11_jill_style == 1:
            scene ep11_jgifts54a with dissolve
        elif ep11_jill_style == 2:
            scene ep11_jgifts54b with dissolve
        else:
            scene ep11_jgifts54c with dissolve
        ji "I like that I can say that my boyfriend picked it out for me."
        ji "And while it's not me..."
        if ep11_jill_style == 1:
            scene ep11_jgifts55a with dissolve
        elif ep11_jill_style == 2:
            scene ep11_jgifts55b with dissolve
        else:
            scene ep11_jgifts55c with dissolve
        ji "Maybe in time, it could feel like it is."
        ji "For select occasions, of course."
        if ep11_jill_style == 1:
            scene ep11_jgifts53a with dissolve
        elif ep11_jill_style == 2:
            scene ep11_jgifts53b with dissolve
        else:
            scene ep11_jgifts53c with dissolve
        mc "Of course."
    "I don't know what I'm doing":
        $ tmpBool3 = True
        mc "Yeah, you're right. It's not you. I don't know what I'm doing."
        mc "But it was fun giving it a shot."
        if ep11_jill_style == 1:
            scene ep11_jgifts56a with dissolve
        elif ep11_jill_style == 2:
            scene ep11_jgifts56b with dissolve
        else:
            scene ep11_jgifts56c with dissolve
        ji "Yeah, where would I even wear this?"
        if ep11_jill_style == 1:
            ji "The clothes fit, but they make my breasts look...vulgar."
            scene ep11_jgifts57a with dissolve
        elif ep11_jill_style == 2:
            ji "The clothes fit, but they make my body look...vulgar."
            scene ep11_jgifts57b with dissolve
        else:
            ji "The clothes fit, but they're a completely different style from what I'm used to."
            scene ep11_jgifts57c with dissolve
        ji "This is something Lana would wear."
        ji "Hm... No. There's no point in dwelling on it. Neither of us is excited about this outfit. It's not for me."
        if ep11_jill_style == 1:
            scene ep11_jgifts53a with dissolve
        elif ep11_jill_style == 2:
            scene ep11_jgifts53b with dissolve
        else:
            scene ep11_jgifts53c with dissolve
        mc "Thanks for trying it on."
if ep11_jill_style == 1:
    scene ep11_jgifts58a with dissolve
elif ep11_jill_style == 2:
    scene ep11_jgifts58b with dissolve
else:
    scene ep11_jgifts58c with dissolve
ji "I appreciate what you're doing."
if ep11_jill_style == 1:
    scene ep11_jgifts59a with dissolve
elif ep11_jill_style == 2:
    scene ep11_jgifts59b with dissolve
else:
    scene ep11_jgifts59c with dissolve
ji "I feel bad for saying that you're trying to change me into someone I'm not."
ji "I realized that's something Mom would say when I wanted to try something she didn't want me to wear."
ji "I like what I wear, and I feel comfortable in my wardrobe..."
ji "But I can't help but wonder what I'd be like today if I'd had that chance to explore more when I was younger."
if ep11_jill_style == 1:
    scene ep11_jgifts58a with dissolve
elif ep11_jill_style == 2:
    scene ep11_jgifts58b with dissolve
else:
    scene ep11_jgifts58c with dissolve
ji "Hah, maybe I would have had a rebellious phase like Lana."
if ep11_jill_style == 1:
    scene ep11_jgifts60a with dissolve
elif ep11_jill_style == 2:
    scene ep11_jgifts60b with dissolve
else:
    scene ep11_jgifts60c with dissolve
mc "Hey... You're quite the rebel now, too. I mean...that dress in there...in white."
if ep11_jill_style == 1:
    scene ep11_jgifts61a with dissolve
elif ep11_jill_style == 2:
    scene ep11_jgifts61b with dissolve
else:
    scene ep11_jgifts61c with dissolve
ji "Haha! Quiet, you! Stop mocking me."
if ep11_jill_style == 1:
    scene ep11_jgifts64a with dissolve
elif ep11_jill_style == 2:
    scene ep11_jgifts64b with dissolve
else:
    scene ep11_jgifts64c with dissolve
ji "*{i}Smack{/i}*"
if ep11_jill_style == 1:
    scene ep11_jgifts62a with dissolve
elif ep11_jill_style == 2:
    scene ep11_jgifts62b with dissolve
else:
    scene ep11_jgifts62c with dissolve
$ renpy.pause()
if ep11_jill_style == 1:
    scene ep11_jgifts63a with dissolve
elif ep11_jill_style == 2:
    scene ep11_jgifts63b with dissolve
else:
    scene ep11_jgifts63c with dissolve
mc "What?"
if ep11_jill_style == 1:
    scene ep11_jgifts64a with dissolve
elif ep11_jill_style == 2:
    scene ep11_jgifts64b with dissolve
else:
    scene ep11_jgifts64c with dissolve
ji "*{i}Smack{/i}*"
if ep11_jill_style == 1:
    scene ep11_jgifts65a with dissolve
elif ep11_jill_style == 2:
    scene ep11_jgifts65b with dissolve
else:
    scene ep11_jgifts65c with dissolve
$ renpy.pause()
if ep11_jill_style == 1:
    scene ep11_jgifts66a with dissolve
elif ep11_jill_style == 2:
    scene ep11_jgifts66b with dissolve
else:
    scene ep11_jgifts66c with dissolve
$ renpy.pause()
play sound "sound_effects/shower_curtain.mp3"
if ep11_jill_style == 1:
    scene ep11_jgifts67a with dissolve
elif ep11_jill_style == 2:
    scene ep11_jgifts67b with dissolve
else:
    scene ep11_jgifts67c with dissolve
ji "[name]... What are you doing?"
if ep11_jill_style == 1:
    scene ep11_jgifts68c with dissolve
elif ep11_jill_style == 2:
    scene ep11_jgifts68b with dissolve
else:
    scene ep11_jgifts68c with dissolve
mc "You can't kiss me and look at me like that before you get in here to undress..."
mc "Feeling rebellious?"
if ep11_jill_style == 1:
    scene ep11_jgifts69a with dissolve
elif ep11_jill_style == 2:
    scene ep11_jgifts69b with dissolve
else:
    scene ep11_jgifts69c with dissolve
ji "[name]... Not in here."
if ep11_jill_style == 1:
    scene ep11_jgifts70c with dissolve
elif ep11_jill_style == 2:
    scene ep11_jgifts70b with dissolve
else:
    scene ep11_jgifts70c with dissolve
$ renpy.pause()
if tmpBool3:
    $ ep11_jill_style = 0
scene ep11_jgifts72 with dissolve
$ renpy.pause()
scene ep11_jgifts71 with dissolve
$ renpy.pause()
scene anim_jill2_tits_ep11 with dissolve
mc "*{i}Suck suck{/i}*"
ji "[mc_jill]... This isn't right..."
pause
scene anim_jill2_tits2_ep11 with dissolve
ji "Hnn..."
scene ep11_jgifts73 with dissolve
ji "..."
scene ep11_jgifts74 with dissolve
ji "*{i}Gasps{/i}*"
scene ep11_jgifts75 with dissolve
$ renpy.pause()
scene ep11_jgifts76 with dissolve
ji "Have you gone mad?"
scene ep11_jgifts77 with dissolve
ji "[mc_jill]... Wait."
scene ep11_jgifts78 with dissolve
mc "Ok... You're right... I got carried away."
scene ep11_jgifts79 with dissolve
ji "Only for a little bit, ok?"
scene ep11_jgifts78 with dissolve
mc "What?"
scene ep11_jgifts79 with dissolve
ji "F-fuck me."
scene ep11_jgifts80 with dissolve
$ renpy.pause()

scene ep11_lewd2_jill1 with dissolve
$ renpy.pause()
scene ep11_lewd2_jill2 with dissolve
$ renpy.pause()
scene ep11_lewd2_jill3 with dissolve
$ renpy.pause()
scene ep11_lewd2_jill4 with dissolve
$ renpy.pause()
scene ep11_lewd2_jill5 with dissolve
$ renpy.pause()
scene ep11_lewd2_jill6 with dissolve
ji "*{i}Gasps{/i}*"
scene ep11_lewd2_jill7 with dissolve
$ renpy.pause()

scene anim_jill2_stand1_ep11 with dissolve
pause
scene anim_jill2_stand2_ep11 with dissolve
pause

$ tmpInt = 0
label ep11_lewd2_jill_loop_label:
menu:
    "Blowjob":
        $ tmpInt += 1
        scene anim_jill2_bj1_ep11 with dissolve
        pause
        scene anim_jill2_bj2_ep11 with dissolve
        pause
        jump ep11_lewd2_jill_loop_label
    "Standing":
        $ tmpInt += 1
        scene anim_jill2_stand1_ep11 with dissolve
        pause
        scene anim_jill2_stand2_ep11 with dissolve
        pause
        jump ep11_lewd2_jill_loop_label
    "Reverse cowgirl":
        $ tmpInt += 1
        scene anim_jill2_rev1_ep11 with dissolve
        pause
        scene anim_jill2_rev2_ep11 with dissolve
        pause
        scene anim_jill2_rev3_ep11 with dissolve
        pause
        jump ep11_lewd2_jill_loop_label
    "Facing":
        $ tmpInt += 1
        scene anim_jill2_face1_ep11 with dissolve
        pause
        scene anim_jill2_face2_ep11 with dissolve
        pause
        scene anim_jill2_face3_ep11 with dissolve
        pause
        jump ep11_lewd2_jill_loop_label
    "Cum" if tmpInt > 2:
        menu:
            "Creampie":
                scene anim_jill2_stand1_ep11 with dissolve
                pause
                scene anim_jill2_stand2_ep11 with dissolve
                pause
                scene ep11_lewd2_jill8 at vpunch, cum1
                $ renpy.pause(0.5)
                scene ep11_lewd2_jill8 at vpunch, cum1
                mc "Fuck!"
                ji "*{i}Moans{/i}* Hngn... Not so loud."
                scene ep11_lewd2_jill9 at vpunch, cum1
                mc "It's too good."
                scene ep11_lewd2_jill10 with dissolve
                $ renpy.pause()
                scene ep11_lewd2_jill11 with dissolve
                $ renpy.pause()
            "In mouth":
                scene anim_jill2_bj1_ep11 with dissolve
                pause
                scene anim_jill2_bj2_ep11 with dissolve
                pause
                mc "[jill], I'm gonna cum in your mouth."
                scene ep11_lewd2_jill12 at vpunch, cum1
                $ renpy.pause(0.5)
                scene ep11_lewd2_jill12 at vpunch, cum1
                $ renpy.pause(0.5)
                scene ep11_lewd2_jill12 at vpunch, cum1
                mc "Fuck!"
                scene ep11_lewd2_jill13 with dissolve
                ji "Ah..."
                mc "That's hot..."
                scene ep11_lewd2_jill14 with dissolve
                ji "What do I do with it? Do I...spit it out?"
                scene ep11_lewd2_jill13 with dissolve
                mc "Haha... Or you can swallow it, and we don't leave a mess."
                scene ep11_lewd2_jill15 with dissolve
                ji "*{i}Gulp{/i}*"
                ji "Hmm..."
                mc "Did you swallow it? I was joking; you didn't have to do that."
                scene ep11_lewd2_jill16 with dissolve
                ji "I thought you were serious about the mess."
                scene ep11_lewd2_jill17 with dissolve
                mc "Well, it's good that you did it. It makes things easier."
                scene ep11_lewd2_jill18 with dissolve
                ji "We shouldn't push it further. We need to leave now."
            "On tits":
                scene anim_jill2_bj1_ep11 with dissolve
                pause
                scene anim_jill2_bj2_ep11 with dissolve
                pause
                mc "[jill], I'm gonna cum."

                scene ep11_lewd2_jill19 at vpunch, cum2
                $ renpy.pause(0.5)
                scene ep11_lewd2_jill19 at vpunch, cum2
                mc "Fuck!"
                ji "Shh... Not so loud."
                scene ep11_lewd2_jill20 at vpunch, cum2
                mc "It's too good."
                scene ep11_lewd2_jill21 with dissolve
                ji "What am I supposed to do now?"
                mc "Um... Wipe it off with the dress you tried on."
                scene ep11_lewd2_jill22 with dissolve
                ji "I can't do that!"
                scene ep11_lewd2_jill23 with dissolve
                mc "You can. Do it fast, and then we'll leave."

label ep11_lewd2_jill_cum_label:
scene ep11_lewd2_jill24 with dissolve
$ renpy.pause()
play sound "sound_effects/shower_curtain.mp3"
scene ep11_lewd2_jill25 with dissolve
$ renpy.pause()
scene ep11_lewd2_jill26 with dissolve
mc "All good?"
scene ep11_lewd2_jill27 with dissolve
ji "That was..."
scene ep11_lewd2_jill26 with dissolve
mc "Scary?"
scene ep11_lewd2_jill27 with dissolve
ji "Yes...but it was also arousing. Is that weird? I mean... What just happened?"
scene ep11_lewd2_jill26 with dissolve
mc "Haha! I have no clue, but you were so sexy for doing that with me."
stop music fadeout 3
scene ep11_lewd2_jill28 with dissolve
$ renpy.pause()
$ renpy.end_replay()
$ persistent.ep11_lewd_jill2 = True
$ calcScenes()
$ new_bio("Jill", "We had sex in a dressing room at the mall after trying on clothes. Jill found it arousing.")
$ mphone_stats_add_girl_s3("jill","You had sex with Jill in a dressing room at the mall in episode 11.")
jump ep11_jparty_label
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
