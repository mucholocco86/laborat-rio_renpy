label ep9_jill_branch_label:
play music "music/ep9/halloween_again.mp3"
scene ep9_jill_branch1 with dissolve
de "[mc_de_up]! What will it be?"
scene ep9_jill_branch2 with dissolve
mc "Surprise me."
scene ep9_jill_branch3 with dissolve
de "Hm... Are you sure?"
scene ep9_bella_branch122 with dissolve
mc "No. Strike that. I'll have a Pumpkin spice vodka."
scene ep9_jill_branch3 with dissolve
de "A horrible choice. Utterly horrible."
scene ep9_jill_branch4 with dissolve
mc "Then, why do you have it?"
scene ep9_bella_branch122 with dissolve
de "It's \"Today only\" for a reason."
mc "Fine, I'll have that rum drink instead."
scene ep9_jill_branch3 with dissolve
de "An even worse choice."
scene ep9_jill_branch4 with dissolve
mc "Make me whatever, then."
scene ep9_jill_branch5 with dissolve
de "Having fun yet?"
scene ep9_jill_branch6 with dissolve
mc "Yeah, but it feels like we're all waiting for more to show up."
scene ep9_jill_branch7 with dissolve
de "And by \"more\", do you mean the HOTs?"
scene ep9_jill_branch6 with dissolve
mc "Yeah, them too."
scene ep9_jill_branch7 with dissolve
de "Who else?"
scene ep9_jill_branch6 with dissolve
mc "How much have you had to drink?"
scene ep9_jill_branch7 with dissolve
de "Not a lot yet."
scene ep9_jill_branch8 with dissolve
mc "So, you can keep a secret?"
de "I mean...I'll try."
scene ep9_jill_branch9 with dissolve
mc "I'm waiting for Jill."
scene ep9_jill_branch10 with dissolve
de "How's that a secret?"
scene ep9_jill_branch9 with dissolve
mc "We're not official yet, but she's my girlfriend."

if pathMayaJosy and wt_ep9_branch_numbers < 2:
    scene ep9_jill_branch13 with dissolve
    de "What about my sis and Josy?"
    scene ep9_jill_branch11 with dissolve
    mc "..."
    scene ep9_jill_branch12 with dissolve
    mc "I feel horrible about it... I haven't found the perfect moment to tell them yet."
    scene ep9_jill_branch13 with dissolve
    de "[name]..."
    scene ep9_jill_branch14 with dissolve
    mc "Wow... You're calling me by my name."
    scene ep9_jill_branch13 with dissolve
    de "You have to tell them."
    scene ep9_jill_branch12 with dissolve
    mc "I know I have to, but you know what Maya is going through."
    mc "I can't just blurt it out, can I?"
    scene ep9_jill_branch13 with dissolve
    de "To me, you should. The longer you wait, the more it's gonna hurt."
    de "You're already in a relationship and haven't told them."
    scene ep9_jill_branch14 with dissolve
    mc "I know... It fucking sucks."
    scene ep9_jill_branch16 with dissolve
elif ep5_feelingsForJosy or ep5_feelingsForMaya:
    scene ep9_jill_branch11 with dissolve
    if ep5_feelingsForJosy:
        de "What about your feelings for Josy?"
    else:
        de "What about your feelings for my sis?"
    scene ep9_jill_branch15 with dissolve
    mc "Look, this is how it is now."
    mc "Jill and I dated and grew close, and I've been falling for her."
    scene ep9_jill_branch16 with dissolve
    de "I see..."
else:
    scene ep9_jill_branch15 with dissolve
    de "..."
    scene ep9_jill_branch16 with dissolve
de "And why did you invite your ex again?"
scene ep9_jill_branch15 with dissolve
mc "Dude... Stop it. I told you why."
scene ep9_jill_branch17 with dissolve
de "Sorry... The first word out of my mouth should have been congratulations."
de "Really. I'm happy for you, [mc_de]."
de "But more importantly... Are you happy?"
scene ep9_jill_branch9 with dissolve
mc "I think so."
scene ep9_jill_branch10 with dissolve
de "You {i}think{/i} so?"
scene ep9_jill_branch9 with dissolve
mc "It's my first real relationship where we both know that we're in one."
scene ep9_jill_branch16 with dissolve
de "And that doesn't make you happy?"
scene ep9_jill_branch18 with dissolve
mc "It does, but I'm not sure how it's supposed to feel, and she asked me to do something I wasn't comfortable with."
scene ep9_jill_branch17 with dissolve
de "Tell me about it."
scene ep9_jill_branch18 with dissolve
mc "So, we had sex for the first time, right? And I didn't wear a condom."
scene ep9_jill_branch16 with dissolve
de "Nor should you. Who even wears one in this day and age?"
de "Women want to be respected. There's no greater respect you can bestow upon them than granting them the choice of what to do with your seed. Unfiltered and everything."
stop music fadeout 3
scene ep9_jill_branch9 with dissolve
mc "Well, it set off a discussion..."
label ep9_jill_lewd_label:
if _in_replay:
    hide screen new_phone_screen
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
hide screen new_phone_screen
play music "music/ep9/passing_time.mp3"
scene ep9_jill_branch20 with dissolve
ji "I'd love to!"
scene ep9_jill_branch21 with dissolve
mc "Really?"
scene ep9_jill_branch22 with dissolve
ji "Yes, I love Halloween!"
scene ep9_jill_branch21 with dissolve
mc "Do you like dressing up for it?"
scene ep9_jill_branch22 with dissolve
ji "I do it much less these days, but I did it with my sister when we were young."
ji "This sounds so fun!"
scene ep9_jill_branch23 with dissolve
mc "What are you going as? Do you have any ideas?"
scene ep9_jill_branch24 with dissolve
ji "A couple have sprung to mind just now. What about you?"
scene ep9_jill_branch23 with dissolve
mc "I have a few options but haven't decided yet."
scene ep9_jill_branch24 with dissolve
ji "Don't tell me the options; I want to be surprised."
scene ep9_jill_branch23 with dissolve
mc "Haha, ok. I'll try not to disappoint."
scene ep9_jill_branch25 with dissolve
ty "OF COURSE, RICH! LET'S HAVE A NIGHT OUT WITH ONLY THE CHAPS!"
scene ep9_jill_branch26 with dissolve
ji "Ugh..."
mc "Is Tybalt still causing you problems?"
scene ep9_jill_branch27 with dissolve
ji "Not problems, but he's annoying me like crazy these days."
ji "He's overly loud so I notice him. He laughs hard with his friends when I'm close and pretends he doesn't care about me."
scene ep9_jill_branch28 with dissolve
mc "Sounds harmless to me. I'm happy I can use the front door from now on."
mc "My climbing days are over."
scene ep9_jill_branch29 with dissolve
ji "Yes, but I can't help that I feel more comfortable in your room than here."
scene ep9_jill_branch30 with dissolve
mc "I don't blame you. Although I should introduce you to my brothers so you don't have to come through my window."
scene ep9_jill_branch31 with dissolve
ji "You will. There are so many thoughts in my mind right now that I don't want to rush into things."
scene ep9_jill_branch30 with dissolve
mc "Rush into things? You're my girlfriend."
scene anim_jill_branch_ep9 with dissolve
ji "Haha, yes, I am. And it feels lovely hearing you say that."
ji "I get like a rush of blood in my head when you call me that."
mc "Have you had a boyfriend before?"
ji "Not a real one."
mc "Imaginary?"
ji "I didn't mean that. I meant, like a proper one."
ji "When you're a kid, it's different; they don't count. Those relationships last a week or so."
scene ep9_jill_branch32 with dissolve
mc "You're more experienced with relationships than me."
scene ep9_jill_branch33 with dissolve
ji "You've never had a relationship? I find that hard to believe."
scene ep9_jill_branch34 with dissolve
mc "I've had one, kinda."
scene ep9_jill_branch35 with dissolve
ji "\"Kind of\" doesn't cut it."
scene ep9_jill_branch34 with dissolve
mc "Anyway..."
scene ep9_jill_branch35 with dissolve
ji "Don't worry. I'm not gonna tease you."
scene ep9_jill_branch36 with dissolve
mc "Sitting like this...you are."
scene ep9_jill_branch37 with dissolve
ji "Um... Haha... I think I can feel that I am."
play sound "sound_effects/shove.mp3"
scene ep9_jill_branch38 with vpunch
ji "Haha! Hey!"
scene ep9_jill_branch39 with dissolve
mc "What? I thought you wanted to wrestle."
scene anim_jill_kiss_ep9 with dissolve
mc "*{i}Smack{/i}*"
ji "Um...[name]?"
mc "*{i}Smack{/i}* Yeah?"
ji "While we're on this topic... There's something I've wanted to ask you."
ji "It's not easy for me to bring this up, but I have to, or I'd never get it out of my head."
scene ep9_jill_branch41 with dissolve
mc "What is it?"
scene ep9_jill_branch40 with dissolve
ji "When we...you know?"
scene ep9_jill_branch41 with dissolve
mc "Am I supposed to guess now?"
scene ep9_jill_branch40 with dissolve
ji "You know?"
scene ep9_jill_branch41 with dissolve
mc "I don't. Ate food?"
scene ep9_jill_branch42 with dissolve
ji "No! You know... In your room."
scene ep9_jill_branch41 with dissolve
mc "When we hung out?"
scene ep9_jill_branch40 with dissolve
ji "When we had...sex."
scene ep9_jill_branch43 with dissolve
mc "Yeah, I knew what you meant."
scene ep9_jill_branch44 with dissolve
ji "You're horrible."
mc "Haha, sorry!"
scene ep9_jill_branch40 with dissolve
ji "You didn't wear any protection."
scene ep9_jill_branch41 with dissolve
mc "You're asking me about that now? It's a bit late..."
scene ep9_jill_branch40 with dissolve
ji "I've obviously taken care of it after. But I meant that I'm not sure that's a good thing to keep doing."
scene ep9_jill_branch41 with dissolve
mc "Do you want me to wear a condom?"
scene ep9_jill_branch40 with dissolve
ji "Well, yes."
scene anim_jill_kiss_ep9 with dissolve
mc "Can't you start eating pills or something?"
ji "Um... Well, I could..."
mc "Problem solved!"
ji "What about STDs?"
mc "I don't have those."
ji "Are you sure? When was the last time you got tested?"
scene ep9_jill_branch45 with dissolve
mc "I mean, I've never tested myself, but I'm clean. I just know."
scene ep9_jill_branch46 with dissolve
ji "I'm sorry, but I can't accept that answer."
scene ep9_jill_branch45 with dissolve
mc "What about you?"
scene ep9_jill_branch46 with dissolve
ji "What about me? I was a virgin. Anything I'd have gotten would have come from you."
scene ep9_jill_branch45 with dissolve
mc "Yeah, or like...toilet seats or something?"
scene ep9_jill_branch47 with dissolve
ji "I'll start taking pills if you want to keep doing it without protection."
ji "But to compromise, we should get tested first. I'll do it too."
scene ep9_jill_branch48 with dissolve
mc "I don't know..."
scene ep9_jill_branch47 with dissolve
ji "Or we can use a condom."
scene ep9_jill_branch49 with dissolve
mc "I know I should use a condom, but it feels much better without one."
mc "There's something about using a condom that feels like eating candy with the wrapper still on, you know?"
scene ep9_jill_branch50 with dissolve
ji "I can't relate to that at all."
scene ep9_jill_branch48 with dissolve
mc "Ok, fine. Let's get tested. Together."
scene ep9_jill_branch51 with dissolve
ji "*{i}Smack{/i}*"
scene ep9_jill_branch52 with dissolve
ji "*{i}Soft moan{/i}*"
scene ep9_jill_branch53 with dissolve
$ renpy.pause()
scene ep9_jill_branch54 with dissolve
$ renpy.pause()
scene ep9_jill_branch55 with dissolve
ji "Um... We shouldn't... Unless... Do you have a condom?"
scene ep9_jill_branch56 with dissolve
mc "*{i}Mumbles{/i}* I should have listened to Dad..."
scene ep9_jill_branch55 with dissolve
ji "What?"
scene ep9_jill_branch56 with dissolve
mc "I can go get one."
scene ep9_jill_branch55 with dissolve
ji "Or...we can cuddle."
if persistent.mod_wtenabled: 
                        $mod_choices = ["(Jill scene)","(+Maya)","(-DIK)","(+DIK)","(Sandy scene)","(Sarah scene)","","","","","","" ]
                        #[mod_gr][mod_choices[0]]
menu:
    "Cuddle" if not _in_replay:
        scene ep9_jill_branch72 with dissolve
        mc "I can't say no to that."
        scene ep9_jill_branch73 with dissolve
        ji "It's nice, huh?"
        stop music fadeout 3
        scene ep9_jill_branch74 with dissolve
        mc "Yeah... I mean... Yes, it is."
        scene ep9_jill_branch17 with dissolve
        show screen new_phone_screen
        $ mphone_next_song()
        de "Hey, there's nothing wrong with cuddling."
        scene ep9_jill_branch18 with dissolve
        mc "How do you manage to surprise me all the time?"
        scene ep9_jill_branch16 with dissolve
        de "What? There's nothing wrong with it. Who doesn't wanna be held?"
        scene ep9_jill_branch18 with dissolve
        mc "I like it too. I just didn't think you did."
        scene ep9_jill_branch16 with dissolve
        de "But I get what you're hinting at..."
    "Try sexy stuff [mod_gr][mod_choices[0]]":

        $ ep9_jill_lewd = True
        scene ep9_jill_branch57 with dissolve
        mc "Um... There are many ways you can have sex without having to worry about getting pregnant and whatnot."
        scene ep9_jill_branch58 with dissolve
        ji "I'm not quite sure I follow."
        scene ep9_jill_branch57 with dissolve
        mc "We can use hands and mouths, and you know...rub stuff."
        scene ep9_jill_branch58 with dissolve
        ji "Mouths? Uh..."
        ji "Call me crazy, but I feel it will lead to more."
        scene ep9_jill_branch57 with dissolve
        mc "It won't. Trust me."
        scene ep9_jill_branch59 with dissolve
        ji "Unnn... Ok..."
        scene ep9_jill_branch60 with dissolve
        $ renpy.pause()
        scene ep9_jill_branch61 with dissolve
        $ renpy.pause()
        scene ep9_jill_branch62 with dissolve
        ji "Mmm... [mc_jill]..."
        scene anim_jill_tits_ep9 with dissolve
        mc "Your breasts are amazing..."
        ji "Haha... Um... Thanks?"
        pause

        scene ep9_jill_branch63 with dissolve
        ji "What are you doing?"
        mc "I'll show you."
        scene ep9_jill_branch64 with dissolve
        ji "[mc_jill]... I don't think this is going to work..."
        mc "It will..."
        scene ep9_jill_branch65 with dissolve
        ji "You're already pushing against me, and I don't think we'll be able to resist."
        scene ep9_jill_branch66 with dissolve
        mc "Uh... But..."
        mc "How about if I do this?"
        scene ep9_jill_branch67 with dissolve
        ji "Are you going to rub against me like that?"
        scene ep9_jill_branch68 with dissolve
        mc "Yeah. If you keep your thighs together, it will feel good for both of us."

        scene anim_jill_thigh_ep9 with dissolve
        mc "Like...so..."
        ji "*{i}Soft moan{/i}* [mc_jill]..."
        mc "It's good, huh?"
        ji "Uh-huh..."
        pause
        scene anim_jill_thigh2_ep9 with dissolve
        mc "Damn, I wish I was inside you..."
        ji "See, I told you this would happen. We should stop."
        mc "No, I can resist that urge. I promise."
        pause
        scene anim_jill_thigh3_ep9 with dissolve
        ji "(You might... But what about me? God... This feels so good.)"
        mc "Your panties feel so soft against my dick."
        ji "Huh? Oh... That's good."
        pause

        scene ep9_jill_branch68b with dissolve
        mc "Let me try this for a while..."
        scene anim_jill_asscheeks_ep9 with dissolve
        mc "Yeah... Fuck... Your asscheeks are perfect for this."
        pause
        scene anim_jill_asscheeks2_ep9 with dissolve
        mc "I like this a lot..."
        ji "I'm glad."
        mc "Oh... This probably doesn't do anything for you, right?"
        ji "That's fine. Go ahead."
        pause
        scene anim_jill_asscheeks3_ep9 with dissolve
        mc "What if I do this at the same time?"
        ji "Hngn..."
        pause
        scene ep9_jill_branch68a with dissolve
        mc "Better, huh?"
        ji "*{i}Moan{/i}* Yes..."
        scene anim_jill_asscheeks3_ep9 with dissolve
        mc "Which do you prefer? This or how we did it before?"
        scene ep9_jill_branch68c with dissolve
        mc "Jill?"
        ji "(Why does this feel so good? Is it because it reminds me of when I do it?)"
        ji "Hnnn..."
        scene ep9_jill_branch68d with vpunch
        ji "Ahhhh!"
        scene ep9_jill_branch68d with vpunch
        ji "Hngnnnn... [mc_jill]!"
        scene ep9_jill_branch68e with vpunch
        ji "*{i}Phew{/i}* This..."
        mc "Wow! You came!"
        ji "I can't believe that worked so well."
        scene ep9_jill_branch68f with dissolve
        mc "I knew it would. Can I go back to the other position? I liked it a bit better."
        scene anim_jill_thigh_ep9 with dissolve
        ji "Do you think you will be able to...um...?"
        mc "To cum?"
        ji "Yeah."
        scene anim_jill_thigh4_ep9 with dissolve
        mc "If I go a bit faster like this... Yeah... This is gonna do it."
        pause
        mc "Ok... I'm close. Get ready..."
        ji "To do what?"
        mc "Just...be ready..."
        scene anim_jill_thigh_cum_ep9 with vpunch
        mc "Ahh!!!"
        pause
        scene ep9_jill_branch69 with dissolve
        ji "Oh... That was...something new."
        scene ep9_jill_branch70 with dissolve
        mc "Were you uncomfortable?"
        scene ep9_jill_branch71 with dissolve
        ji "A bit, maybe."
        ji "Sorry..."
        scene ep9_jill_branch70 with dissolve
        mc "Don't be sorry. I remember it took me quite a few times before I got comfortable doing it."
        stop music fadeout 3
        scene ep9_jill_branch71 with dissolve
        ji "Right..."
        $ renpy.end_replay()
        $ persistent.ep9_lewd_jill = True
        $ calcScenes()

        scene ep9_jill_branch17 with dissolve
        show screen new_phone_screen
        $ mphone_next_song()
        de "Condoms suck!"
        scene ep9_jill_branch18 with dissolve
        mc "Well... I wish I kept one in my pocket."
        scene ep9_jill_branch16 with dissolve

de "It sounds like you're missing out on a lot of early relationship sex."
$ new_bio("Jill", "Jill wanted me to take an STD test before continuing to have sex without a condom.")
if ep9_jill_lewd:
    $ new_bio("Jill", "Jill didn't want to have sex without a condom, so we ended up trying new things together.")
    $ mphone_stats_add_girl_s3("jill","You had fun with Jill on her bed in episode 9.")
scene ep9_jill_branch18 with dissolve
mc "We did get tested."
scene ep9_jill_branch17 with dissolve
de "And?"
if wt_ep9_branch_numbers > 1 and branchMayaJosy:
    jump ep9_jm_branch_label_wt
if wt_ep9_branch_numbers > 1 and branchSage:
    jump ep9_sage_branch_label
    
if wt_ep9_branch_numbers > 1 and branchAlone:
    jump ep9_others_branch_label
    
if wt_ep9_branch_numbers > 1 and branchIsabella:
    mc "(I need to get back to my room...)"
    mc "Need to check on something real quick."
    jump ep9_bella_branch_label
scene ep9_jill_branch19 with dissolve
stop music fadeout 3
"The HOTs! The HOTs! They're finally here!"
mc "Let me tell you about it later. Looks like the party is starting for real."



jump ep9_wave2_label

label ep9_jillsolo_label:
scene ep9_jillsolo1 with dissolve
ji "Ahhhh... The breeze. So good..."
ji "This costume doesn't breathe."
scene ep9_jillsolo2 with dissolve
gs "How about you take it off and let your body feel the air too?"
scene ep9_jillsolo3 with dissolve
ji "Oh. I'm not wearing much under."
scene ep9_jillsolo2 with dissolve
gs "That was what I was assuming."
scene ep9_jillsolo4 with dissolve
mc "All right, time for you to leave. Window or railing, your choice."
gs "Damn, what a cockblock."
scene ep9_jillsolo5 with dissolve
gs "How about you? Wanna see my Hallo-wiener?"
isa "No, thanks. I'm more of a Hallo-salami girl."
scene ep9_jillsolo6 with dissolve
bia "Haha! He won't be using that line again."
scene ep9_jillsolo7 with dissolve
ji "Can we stay out here for a while?"
scene ep9_jillsolo8 with dissolve
mc "As long as you want to."
scene ep9_jillsolo9 with dissolve
bia "How do you turn these speakers on?"
scene ep9_jillsolo10 with dissolve
mc "I don't think you can. Or, I don't know... Do you want music?"
scene ep9_jillsolo11 with dissolve
ji "Oh! I know! Why don't you play something for us on your guitar?"
scene ep9_jillsolo12 with dissolve
mc "Sure. I'll need to go get it. I'll be right back."
scene ep9_jillsolo13 with dissolve
isa "*{i}Phew{/i}*"
ji "Sweaty?"
isa "I'd gladly trade my mask for your banana costume."
scene ep9_jillsolo14 with dissolve
ji "Oh, I don't think you would. I'm wearing nothing underneath it, and I'm still overheating."
scene ep9_jillsolo15 with dissolve
ji "So... Bella, there's something I want to tell you, and it can't wait any longer since I want you to hear it from me and before everybody else."
scene ep9_jillsolo17 with dissolve
isa "I knew it..."
isa "You're not dressed as a banana tonight; you're a plantain."
scene ep9_jillsolo15 with dissolve
ji "Haha! I'm being serious here."
scene ep9_jillsolo17 with dissolve
isa "I'm sorry. What is it?"
scene ep9_jillsolo15 with dissolve
ji "[name] and I... We have decided to be boyfriend and girlfriend."
if ep7_bella_lewd:
    scene ep9_jillsolo18 with dissolve
    isa "..."
    scene ep9_jillsolo19 with dissolve
    isa "That's...amazing!"
    scene ep9_jillsolo16 with dissolve
    ji "Right? It feels so good."
    ji "We want to be official soon, but it's a bit scary."
else:
    scene ep9_jillsolo20 with dissolve
    isa "You have?"
    scene ep9_jillsolo16 with dissolve
    ji "Yes. We want to be official soon, but it's a bit scary."
scene ep9_jillsolo21 with dissolve
isa "It's an exciting experience. To announce your feelings to the world."
isa "You deserve it, Jill. I'm ecstatic for you."
scene ep9_jillsolo22 with dissolve
ji "Bella... Thank you."
ji "Do you think...that I should tell my parents first? You know, before I tell everyone else."
scene ep9_jillsolo20 with dissolve
isa "These are modern times, Jill. You don't need to have your parents' approval."
scene ep9_jillsolo15 with dissolve
ji "It's not about approval. It's respectful, no?"
ji "They haven't even met him; I'm sure they will have questions. And if I don't tell them before we announce it..."
ji "That might feel a bit wrong."
scene ep9_jillsolo20 with dissolve
isa "You seem to have the answer already. You should tell them."
scene ep9_jillsolo23 with dissolve
mc "Tell who what?"
scene ep9_jillsolo24 with dissolve
isa "Congratulations, [name]."
if ep7_bella_lewd:
    scene ep9_jillsolo25 with dissolve
else:
    scene ep9_jillsolo26 with dissolve
mc "Oh... Thank you, Bella. She told you, huh?"
scene ep9_jillsolo24 with dissolve
isa "I trust that you'll take good care of her."
scene ep9_jillsolo26 with dissolve
mc "Or risk upsetting you? No thanks. I'll do my best."
scene ep9_jillsolo27 with dissolve
ji "[name], as I just said to Bella, I think we should hold off on announcing it to everyone until I talk to my parents."
scene ep9_jillsolo28 with dissolve
mc "Ok. But what about my friends?"
scene ep9_jillsolo27 with dissolve
ji "That's fine. I mean, official, as in everyone."
scene ep9_jillsolo28 with dissolve
mc "Like, social media people and such?"
scene ep9_jillsolo27 with dissolve
ji "Yes. If you don't mind?"
scene ep9_jillsolo28 with dissolve
mc "That's not a problem."
mc "Um... Celebrate with some music?"
scene ep9_jillsolo29 with dissolve
bia "Yes! Finally."
if not ep8_recital_failed:
    bia "I've wanted to hear you play again since Jill's recital."
    bia "It blew us away. Like wow!"
    scene ep9_jillsolo28 with dissolve
    mc "Thanks. No pressure now, then... I kinda wish I hadn't drunk before this."
else:
    scene ep9_jillsolo28 with dissolve
    mc "But I must warn you. I'm a tad drunk, so it might not sound that good."
scene ep9_jillsolo27 with dissolve
ji "Knowing you, it will sound amazing."
stop music fadeout 3
scene ep9_jillsolo30 with dissolve
mc "I wrote this one myself. It's nothing special, but it fits this moment."
play music "music/ep9/tremolo.mp3"
scene ep9_jillsolo31 with dissolve
$ renpy.pause(13)
show screen click_to_continue_screen with dissolve
$ renpy.pause(2)
hide screen click_to_continue_screen with dissolve
$ renpy.pause()
$ guideSuggestedPage = 73
scene ep9_jillsolo32 with dissolve
ji "That was beautiful."
scene ep9_jillsolo33 with dissolve
bia "Wow..."
scene ep9_jillsolo34 with dissolve
isa "Say, Bianca... Don't we have to...?"
bia "Yes. Totally. Um..."
bia "Bella and I are gonna go to the bathroom and..."
scene ep9_jillsolo35 with dissolve
bia "Meh. Who cares? They're not even listening."
scene ep9_jillsolo36 with dissolve
ji "*{i}Smack{/i}*"
scene ep9_jillsolo37 with dissolve
ji "Play it again."
scene ep9_jillsolo38 with dissolve
$ renpy.pause()
scene ep9_jillsolo39 with dissolve
ji "[name]...?"
scene ep9_jillsolo40 with dissolve
mc "Yes?"
scene ep9_jillsolo39 with dissolve
ji "Would you like to meet my parents?"
scene ep9_jillsolo40 with dissolve
if persistent.mod_wtenabled: 
                        $mod_choices = ["(-Jill)","(+Maya)","(-DIK)","(+DIK)","(Sandy scene)","(Sarah scene)","","","","","","" ]
                        #[mod_gr][mod_choices[0]]
menu:
    "Of course":
        mc "Of course. I'd love to."
        scene ep9_jillsolo41 with dissolve
        ji "I'm glad. I believe they will wanna meet you after I tell them about us."
    "Do I have to? [mod_gr][mod_choices[0]]":
        $ RPjill -= 1
        mc "Parents? Um... Do I have to?"
        scene ep9_jillsolo39 with dissolve
        ji "You don't want to?"
        scene ep9_jillsolo40 with dissolve
        mc "Uh... Sure, I can meet them, but I've never done that with a girl before ."
        scene ep9_jillsolo39 with dissolve
        ji "I think you should meet them. I believe they will wanna meet you after I tell them about us."
ji "And...I'd love to meet your dad."
scene ep9_jillsolo40 with dissolve
mc "My dad?"
scene ep9_jillsolo39 with dissolve
ji "If that's fine with you."
scene ep9_jillsolo40 with dissolve
mc "My dad's the best person I know. Of course, I want you to meet him."
mc "I hope you're not easily embarrassed. He jokes around a lot and..."
scene ep9_jillsolo41 with dissolve
ji "You don't have to worry about that."
ji "He must be the best dad ever. He raised you."
scene ep9_jillsolo40 with dissolve
mc "Yeah... He's the best."
mc "I mean, I'm sure your dad is great too, but-"
scene ep9_jillsolo43 with dissolve
ji "My dad... He's not the best."
scene ep9_jillsolo44 with dissolve
mc "Huh?"
scene ep9_jillsolo43 with dissolve
ji "God, why did I say it like that?"
ji "I meant that he's...um..."
scene ep9_jillsolo45 with dissolve
ji "*{i}Sigh{/i}* This is pretty personal..."
ji "Can you promise not to tell anyone about this?"
scene ep9_jillsolo44 with dissolve
mc "Your secrets are my secrets."
scene ep9_jillsolo43 with dissolve
ji "My father used to be amazing. He was the perfect dad..."
ji "He played with me, taught me how to do things, and always encouraged me to learn."
scene ep9_jillsolo45 with dissolve
ji "But...after Lana passed...he..."
ji "He struggled a lot. It's been hard for him to accept that she is gone."
ji "And... He blames himself for it."
scene ep9_jillsolo43 with dissolve
ji "He tries to hide it, but... He never forgave himself for what he did."
scene ep9_jillsolo44 with dissolve
mc "What did he do?"
scene ep9_jillsolo43 with dissolve
ji "He turned her away from home."
ji "She didn't act as he wanted and refused to change for him."
ji "And he thinks that if he had only tried harder, she wouldn't have left, and she'd still be alive today."
scene ep9_jillsolo45 with dissolve
ji "He started drinking to hide his sorrow. And...um..."
ji "He just changed in many ways."
scene ep9_jillsolo43 with dissolve
ji "Sorry... I think that's enough for tonight. I didn't want to bum you out, but I wanted to tell you."
stop music fadeout 5
scene ep9_jillsolo40 with dissolve
menu:
    "I'm happy you did":
        mc "I'm happy you did."
        scene ep9_jillsolo36 with dissolve
        mc "*{i}Smack{/i}*"
        scene ep9_jillsolo39 with dissolve
    "Hold her":
        scene ep9_jillsolo46 with dissolve
        $ renpy.pause()
        scene ep9_jillsolo47 with dissolve
ji "Life's not always easy."
scene ep9_jillsolo40 with dissolve
mc "Yeah. You don't have to convince me of that."
scene ep9_jillsolo41 with dissolve
ji "But meeting you...and being with you..."
ji "It makes me forget about all of that."
scene ep9_jillsolo42 with dissolve
ji "All thse dark thoughts and the burden I bear..."
ji "They get replaced with excitement and anticipation. Like, \"will you call me today\"? Or \"I wonder what your next text will be\"."
ji "I really like that feeling."
scene ep9_jillsolo41 with dissolve
ji "I've never felt like that before."
scene ep9_jillsolo40 with dissolve
menu:
    "Me neither":
        mc "I've never felt like this, either. It's pretty amazing..."
        scene ep9_jillsolo36 with dissolve
        ji "*{i}Smack{/i}*"
    "You deserve it":
        mc "You deserve to feel that way. And I'll try to make you feel that way every day."
        scene ep9_jillsolo36 with dissolve
        ji "*{i}Smack{/i}*"

scene ep9_jillsolo41 with dissolve
ji "Want to head back inside?"
scene ep9_jillsolo40 with dissolve
mc "Yeah, I think Bella and Bianca will be missing our company by now."
scene ep9_jillsolo41 with dissolve
ji "Haha! Who wouldn't?"
$ new_bio("Jill", "Jill told me about her father. Apparently, the death of her sister changed him.")
$ mphone_next_song()
jump ep9_freeroam_diks_ph3_label

label ep9_jill_lewd2_label:
if _in_replay:
    hide screen new_phone_screen
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
    $ mphone_music_genre = 2
$ mphone_play_songs(["music/ep9/licensed_music/track132.mp3"])
scene ep9_jill_lewd2 with fade
$ renpy.pause()
scene ep9_jill_lewd1 with dissolve
bia "I'm off, guys! Thanks for the amazing party, [name]!"
mc "Thanks for coming. I'll make sure to invite you to our next one."
scene ep9_jill_lewd3 with dissolve
bia "Hey! I might take you up on that."
scene ep9_jill_lewd4 with dissolve
ji "Bye, Bianca."
scene ep9_jill_lewd5 with dissolve
ji "Most people seem to be leaving."
scene ep9_jill_lewd6 with dissolve
mc "Did Bella leave too?"
scene ep9_jill_lewd5 with dissolve
ji "Yeah, a while back. We couldn't find you, so she told me to thank you."
scene ep9_jill_lewd6 with dissolve
mc "I can't blame people for dropping off; it's getting very late or kinda early."
scene ep9_jill_lewd7 with dissolve
ji "I'm getting tired myself."
scene ep9_jill_lewd6 with dissolve
mc "Yeah? Are you leaving too?"
scene ep9_jill_lewd5 with dissolve
ji "If you don't mind, I thought I could stay here tonight."
scene ep9_jill_lewd6 with dissolve
mc "Let's drink some water and lock ourselves in my room for the night. How does that sound?"
scene ep9_jill_lewd5 with dissolve

if _in_replay:
    stop music fadeout 3
ji "That sounds like a perfect way to end the night."
if not _in_replay and len(wt_ep9_scenes) < 2:
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
hide screen new_phone_screen
scene ep9_jill_lewd8 with dissolve
ji "I've been waiting all night to get out of this costume."
play music "music/ep7/licensed_music/track54.mp3"
queue music ["music/ep6/licensed_music/track23.mp3","music/ep6/licensed_music/track25.mp3","music/ep7/licensed_music/track54.mp3"]
scene ep9_jill_lewd9 with dissolve
mc "I'm impressed you have worn it until now. It must have been exhausting."
ji "It was! But it's not like I had a choice."
scene ep9_jill_lewd10 with dissolve
mc "Yeah, if only you could have removed parts of it."
scene ep9_jill_lewd11 with dissolve
ji "Finally, I can. It's been way too hot."
scene ep9_jill_lewd12 with dissolve
mc "Too hot indeed... Damn..."
ji "What?"
scene ep9_jill_lewd13 with dissolve
mc "That's what you've been wearing underneath all this time?"
scene ep9_jill_lewd14 with dissolve
ji "Yeah."
scene ep9_jill_lewd12 with dissolve
mc "It's so sexy..."
ji "Haha, what?"
scene ep9_jill_lewd15 with dissolve
mc "It is! Look at you."
scene ep9_jill_lewd16 with dissolve
ji "How much did you have to drink?"
mc "That's not relevant."
scene ep9_jill_lewd17 with dissolve
ji "So, you like what I'm wearing?"
mc "A lot."
scene ep9_jill_lewd18 with dissolve
mc "Who knew you had to peel the banana to get to the good stuff?"
scene ep9_jill_lewd19 with dissolve
ji "Hahaha! You're so stupid!"
scene ep9_jill_lewd20 with dissolve
ji "*{i}Smack{/i}*"
scene ep9_jill_lewd21 with dissolve
mc "I know you're tired, but..."
mc "What do you say about getting rid of the last energy in our systems?"
scene ep9_jill_lewd22 with dissolve
ji "What do you have in mind?"
scene ep9_jill_lewd21 with dissolve
mc "Now that I've tested clean and all..."
mc "...and you've started with pills...right?"
scene ep9_jill_lewd22 with dissolve
ji "Right..."
scene ep9_jill_lewd21 with dissolve
mc "Do you wanna?"
scene ep9_jill_lewd20 with dissolve
ji "*{i}Smack{/i}*"
scene ep9_jill_lewd22 with dissolve
ji "Yes."
scene ep9_jill_lewd23 with dissolve
ji "Oh, you're so strong."
scene ep9_jill_lewd24 with dissolve
mc "You're not heavy at all."
scene ep9_jill_lewd25 with dissolve
$ renpy.pause()
scene ep9_jill_lewd26 with dissolve
$ renpy.pause()
scene ep9_jill_lewd27 with dissolve
$ renpy.pause()
scene ep9_jill_lewd29 with dissolve
ji "Oh... Wait..."
scene ep9_jill_lewd28 with dissolve
mc "What?"
scene ep9_jill_lewd29 with dissolve
ji "Do you have a condom?"
scene ep9_jill_lewd28 with dissolve
mc "Uh... But... But..."
scene ep9_jill_lewd30 with dissolve
ji "Got you. Haha."
scene ep9_jill_lewd31 with dissolve
mc "Don't toy with me like that."
scene ep9_jill_lewd32 with dissolve
mc "No, don't remove those."
ji "No?"
mc "Can you keep them on for me?"
scene ep9_jill_lewd33 with dissolve
ji "You do like what I'm wearing."
scene ep9_jill_lewd34 with dissolve
mc "You don't know the half of it."
scene ep9_jill_lewd33 with dissolve
ji "Is it the stockings or...?"
scene ep9_jill_lewd34 with dissolve
mc "Yeah, it's all of it."
scene ep9_jill_lewd35 with dissolve
mc "I love how smooth they feel...and they look so hot on you."
scene ep9_jill_lewd36 with dissolve
mc "What do you want me to do to you?"
ji "Um... Whatever is fine with you."
scene ep9_jill_lewd37 with dissolve
mc "Well, I wanna..."
$ tmpInt = 0
label ep9_jill_lewd_loop_label:
menu:
    "...go down on you":
        $ tmpInt += 1
        scene ep9_jill_lewd38 with dissolve
        mc "...go down on you."
        scene anim_jill_lick_ep9 with dissolve
        mc "*{i}Lick lick{/i}*"
        ji "*{i}Soft moan{/i}*"
        mc "You taste so good, [jill]..."
        pause
        menu:
            "Add a finger":
                scene anim_jill_lick2_ep9 with dissolve
                mc "Do you like this?"
                ji "Oh... [mc_jill]..."
                ji "(He is so good with his tongue... And his thick finger feels wonderful inside me.)"
                ji "(Oh, God... He's moving it up toward my G-spot... How did he know to do it like that?)"
                ji "(He must know so much more about sex than I thought he did... It's kind of intimidating...)"
                ji "(I barely know what to do with his penis, and here he is...perfectly penetrating me with his finger...)"
                ji "(Not too fast... It's slow... Almost a rhythmic pace...)"
                pause
            "Lick her asshole":
                scene anim_jill_lick3_ep9 with dissolve
                mc "*{i}Lick lick{/i}* I hope you don't mind this..."
                ji "Hngn..."
                ji "(What's he doing that for? This feels weird...)"
                ji "(Maybe because it's a new feeling? It kind of tickles...)"
                ji "Hnngn..."
                pause
        mc "Mmm... Now I wanna..."
        jump ep9_jill_lewd_loop_label
    "...rub you with my dick":
        $ tmpInt += 1
        scene ep9_jill_lewd39 with dissolve
        mc "...rub you with my dick."
        scene anim_jill_rub_ep9 with dissolve
        ji "On the outside?"
        mc "Yeah... I know I can put it in, but I want to tease you first."
        ji "(And does it ever? I feel like I'm about to burst...)"
        ji "Hngnn..."
        mc "It's good, huh?"
        pause
        scene anim_jill_rub2_ep9 with dissolve
        mc "You're so nice and smooth when you're freshly shaven. My dick moves so easily against your pussy."
        ji "(My cheeks are about to explode... I'm overheating... Even more so than when wearing that stupid banana costume.)"
        ji "(Is it supposed to feel this way? How have I missed out on this...?)"
        ji "(If I could go back in time, I'd tell myself to kiss him when I first met him. But I'd probably scare him away if I did that.)"
        pause
        mc "Mmm... Now I wanna..."
        jump ep9_jill_lewd_loop_label
    "...feel your feet around my dick":
        $ tmpInt += 1
        scene ep9_jill_lewd40 with dissolve
        mc "...feel your feet around my dick."
        scene ep9_jill_lewd41 with dissolve
        ji "Oh?"
        scene anim_jill_feet_ep9 with dissolve
        ji "(His penis is so stiff... I didn't know guys liked to do this...)"
        ji "(Am I that naive? Is this normal? If I ask, he might get embarrassed...)"
        ji "(But he wouldn't do this if he didn't like it... I think...)"
        pause
        mc "Mmm... Now I wanna..."
        jump ep9_jill_lewd_loop_label
    "...do something else" if tmpInt > 1:
        mc "...do something else with you."

scene ep9_jill_lewd42 with dissolve
mc "Here..."
scene ep9_jill_lewd43 with dissolve
ji "Um... What do you want me to do?"
scene ep9_jill_lewd44 with dissolve
$ tmpInt = 0
label ep9_jill_lewd_loop2_label:
menu:
    "Handjob":
        $ tmpInt += 1
        scene ep9_jill_lewd45 with dissolve
        mc "Touch me..."
        scene ep9_jill_lewd46 with dissolve
        mc "You don't have to be afraid of gripping it."
        mc "You can grip the base pretty hard before it starts to hurt."
        scene anim_jill_hj1_ep9 with dissolve
        mc "Yeah, like that. The head is sensitive, so be a bit careful with it."
        ji "Am I doing this right?"
        mc "Yes... Keep doing it."
        ji "(I have no clue what I'm doing with this... If he says I'm doing it right, I'll have to trust that.)"
        ji "(It feels like I am hurting him, gripping it this hard. But he seems to be enjoying it.)"
        pause
        jump ep9_jill_lewd_loop2_label
    "Boobjob":
        $ tmpInt += 1
        mc "Can I put my dick between your tits?"
        scene ep9_jill_lewd43 with dissolve
        ji "You wanna what?"
        scene ep9_jill_lewd44 with dissolve
        mc "If you're ok with it, I want to feel your tits against my dick."
        scene ep9_jill_lewd43 with dissolve
        ji "You'll have to show me what you mean by that."
        scene ep9_jill_lewd47 with dissolve
        mc "Like this..."
        scene anim_jill_boobjob1_ep9 with dissolve
        mc "Yeah... This feels great."
        ji "It does?"
        mc "Yeah, it's so good. Your breasts are so soft."
        ji "(It's arousing seeing him up close like this...)"
        ji "(But I don't get the deal with what he's doing.)"
        pause
        scene ep9_jill_lewd48 with dissolve
        ji "Hngn..."
        scene anim_jill_boobjob2_ep9 with dissolve
        mc "You're wet, [jill]."
        ji "Yes. You're very hard."
        ji "(Why did I say that? That sounded stupid...)"
        ji "*{i}Moans{/i}*"
        pause
        jump ep9_jill_lewd_loop2_label
    "Kiss it":
        $ tmpInt += 1
        scene ep9_jill_lewd49 with dissolve
        mc "Do you want to taste it?"
        scene ep9_jill_lewd50 with dissolve
        ji "I've never done that before."
        scene ep9_jill_lewd49 with dissolve
        mc "You can kiss it, lick it or put it in your mouth. Just watch your teeth if you do."
        scene ep9_jill_lewd51 with dissolve
        mc "Try licking it a bit."
        scene anim_jill_mouth_ep9 with dissolve
        ji "*{i}Lick lick{/i}*"
        ji "(It's...salty.)"
        ji "(And warm.)"
        ji "(I wonder if I'm doing it right? He's not complaining...)"
        pause
        scene anim_jill_mouth2_ep9 with dissolve
        ji "*{i}Smack smack{/i}*"
        mc "Yeah... Oh... That feels good. You're doing great."
        ji "(I am?)"
        pause
        jump ep9_jill_lewd_loop2_label
    "Continue" if tmpInt > 1:
        $ renpy.pause(0.5)

scene ep9_jill_lewd52 with dissolve
mc "How do you want to do it?"
scene ep9_jill_lewd53 with dissolve
ji "How do you?"
scene ep9_jill_lewd52 with dissolve
mc "I can do it in any way you want. Last time we did it, was there something in particular you enjoyed?"
scene ep9_jill_lewd53 with dissolve
ji "Uh..."
scene ep9_jill_lewd54 with dissolve
mc "Was it all bad?"
scene ep9_jill_lewd55 with dissolve
ji "No! It was good!"
ji "Very good! I don't know what to suggest, that's all."
scene ep9_jill_lewd52 with dissolve
mc "Do you want me to take the lead?"
scene ep9_jill_lewd53 with dissolve
ji "If you don't mind."
scene ep9_jill_lewd52 with dissolve
mc "Not at all."
scene ep9_jill_lewd56 with dissolve
mc "Are you ready?"
ji "Mhm..."
scene bg anim_jill_insert_ep9 movie with dissolve
ji "*{i}Moans{/i}*"
mc "It feels so good to be back inside of you..."
$ renpy.pause()
$ tmpInt = 0
jump ep9_jill_lewd_loop3b_label
label ep9_jill_lewd_loop3_label:

if persistent.mod_wtenabled:
    if not ep9_jill_orgasm:
        $mod_choices[1]="(Pick this)"
    else:
        $mod_choices[1]=""

menu:
    "Missionary":
        $ tmpInt += 1
        label ep9_jill_lewd_loop3b_label:
        scene anim_jill_miss_ep9 with dissolve
        mc "You're so sexy with those stockings on."
        mc "I'm gonna have to focus so I don't cum too early."
        ji "(I hope I will be able to reach orgasm this time with him. I don't want him to feel like it's not good for me...)"
        if ep9_jill_lewd:
            ji "(I could orgasm from his hand, so at least there's that...)"
        ji "(I'm overthinking this... Relax!)"
        ji "(It feels so good. He looks so hot on top of me...)"
        ji "(His abs are amazing... I wonder if he'd feel weird if I touched them.)"
        pause
        scene ep9_jill_lewd57 with dissolve
        ji "(Maybe for a little bit...)"
        mc "Oh, you want me to stop?"
        ji "Huh? No. I was just...um..."
        mc "Let's try something different."
        jump ep9_jill_lewd_loop3_label
    "Doggystyle":
        $ tmpInt += 1
        scene anim_jill_doggy_ep9 with dissolve
        ji "(We're totally in sync... It's a perfect rhythm... It's like music.)"
        ji "(I move back toward him, and he plunges deep into me.)"
        ji "(It feels so good... I wish I could look into his beautiful eyes while doing this.)"
        pause
        scene anim_jill_doggy2_ep9 with dissolve
        mc "You feel amazing, [jill]. Don't take this the wrong way, but your ass is so big and soft."
        mc "But it's fit too... I can't find the words to describe it. I wanna grab and squeeze it while I fuck you."
        ji "(Wow... He's so good at expressing himself like that... I feel embarrassed, but blood rushed to my head as he said those things about me.)"
        ji "*{i}Moans{/i}*"
        pause
        jump ep9_jill_lewd_loop3_label
    "Standing [mod_gr][mod_choices[1]]":
        $ tmpInt += 1
        scene ep9_jill_lewd58 with dissolve
        mc "Lift your leg up like that."
        scene anim_jill_standing_ep9 with dissolve
        mc "Have you ever tried standing up like this?"
        ji "Um... You know that I haven't."
        mc "Right, but I meant like when you're masturbating."
        ji "(I can't tell him what I do when I masturbate... Can I?)"
        ji "No, I never tried it."
        ji "Mmm..."
        mc "Feels good, doesn't it?"
        ji "Mhm..."
        ji "(How does he know all of these positions? He's got so much experience...)"
        pause
        scene anim_jill_standing2_ep9 with dissolve
        mc "God, your pussy feels so tight. I'm getting closer and closer..."
        ji "(It is very tight... I can feel it too. There's a lot of friction, and the way he's doing it is rubbing my clitoris so well...)"
        if not ep9_jill_orgasm:
            ji "(I think I'll be able to reach a climax this way...)"
            ji "(Yeah... If he keeps this up for a minute or so, I might...)"
            show screen ep9_jill_orgasm_timer
            if persistent.mod_wtenabled :
               $renpy.notify("Wait here for a few seconds")
               
        pause
        if not ep9_jill_orgasm:
            hide screen ep9_jill_orgasm_timer
        jump ep9_jill_lewd_loop3_label
        label ep9_jill_lewd_loop3c_label:
        hide screen ep9_jill_orgasm_timer
        $ ep9_jill_orgasm = True
        scene ep9_jill_lewd59 with hpunch
        $ renpy.pause(0.5)
        scene ep9_jill_lewd59 with hpunch
        $ renpy.pause(0.5)
        scene ep9_jill_lewd59 with hpunch
        ji "Ah!!!"
        scene ep9_jill_lewd60 with dissolve
        mc "You came..."
        scene ep9_jill_lewd61 with dissolve
        ji "Mhm..."
        scene ep9_jill_lewd60 with dissolve
        mc "You should have told me it felt that good for you."
        scene ep9_jill_lewd61 with dissolve
        ji "Sorry, I drifted off and enjoyed it for a while."
        scene ep9_jill_lewd60 with dissolve
        mc "That's great."
        jump ep9_jill_lewd_loop3_label
    "Reverse cowgirl":
        $ tmpInt += 1
        mc "Can you be on top for a while?"
        scene ep9_jill_lewd62 with dissolve
        ji "Like this?"
        scene anim_jill_rev_ep9 with dissolve
        mc "Yes. Let's move together now."
        ji "(Oh... This feels good... He's coming at it from another angle now...)"
        ji "Hngnn..."
        ji "(He's so deep too... Maybe I shouldn't go all the way down? Or does he like that?)"
        pause
        scene anim_jill_rev2_ep9 with dissolve
        mc "Keep it up. Ride me, [jill]... Ride me hard."
        pause
        jump ep9_jill_lewd_loop3_label
    "Cum" if tmpInt > 1:
        mc "Ok... I'm gonna cum..."
        ji "Oh?"
        menu:
            "On ass":
                scene anim_jill_doggy2_ep9 with dissolve
                mc "I'm gonna cum all over your ass, ok?"
                ji "Ok."
                scene ep9_jill_lewd65 at vpunch, cum2
                $ renpy.pause(0.5)
                scene ep9_jill_lewd65 at vpunch, cum2
                $ renpy.pause(0.5)
                scene ep9_jill_lewd65 at vpunch, cum2
                mc "Ahhh..."
                scene ep9_jill_lewd66 with dissolve
                mc "Fuck..."
            "On pussy":
                scene anim_jill_miss_ep9 with dissolve
                mc "I'm gonna cum all over your pussy..."
                scene ep9_jill_lewd67 at vpunch, cum2
                $ renpy.pause(0.5)
                scene ep9_jill_lewd67 at vpunch, cum2
                $ renpy.pause(0.5)
                scene ep9_jill_lewd67 at vpunch, cum2
                mc "Ahhh..."
                scene ep9_jill_lewd68 with dissolve
                mc "Fuck..."
            "On tits":
                scene anim_jill_cum_tits_ep9 with dissolve
                mc "I wanna cum on your tits..."
                ji "On my chest? Ok..."
                scene ep9_jill_lewd71 at vpunch, cum2
                $ renpy.pause(0.5)
                scene ep9_jill_lewd71 at vpunch, cum2
                $ renpy.pause(0.5)
                scene ep9_jill_lewd71 at vpunch, cum2
                mc "Ahhh..."
                scene ep9_jill_lewd72 with dissolve
                mc "Fuck..."
            "Inside":
                scene anim_jill_rev_ep9 with dissolve
                mc "I'm gonna cum inside of you..."
                ji "That's fine."
                scene ep9_jill_lewd63 at vpunch, cum1
                $ renpy.pause(0.5)
                scene ep9_jill_lewd63 at vpunch, cum1
                $ renpy.pause(0.5)
                scene ep9_jill_lewd63 at vpunch, cum1
                mc "Ahhh..."
                scene ep9_jill_lewd64 with dissolve
                mc "Fuck..."
            "On feet":
                scene anim_jill_feet_ep9 with dissolve
                mc "I wanna cum on your feet..."
                ji "On my feet?"
                mc "Can I? Your stockings might get ruined."
                ji "Go ahead..."
                scene ep9_jill_lewd69 at vpunch, cum3
                $ renpy.pause(0.5)
                scene ep9_jill_lewd69 at vpunch, cum3
                $ renpy.pause(0.5)
                scene ep9_jill_lewd69 at vpunch, cum3
                mc "Ahhh..."
                scene ep9_jill_lewd70 with dissolve
                mc "Fuck... That's too hot..."

scene ep9_jill_lewd73 with dissolve
mc "Damn... That was so good for me... I've missed having sex with you."
scene ep9_jill_lewd74 with dissolve
ji "It was good for me too."
if ep9_jill_orgasm:
    scene ep9_jill_lewd73 with dissolve
    mc "Yeah, I could tell when you came. That was sexy as hell..."
    scene ep9_jill_lewd74 with dissolve
    ji "It felt too good... I just...exploded. Haha..."
    scene ep9_jill_lewd73 with dissolve
    mc "I'm happy you came. At first, I wasn't sure if you were enjoying what I was doing."
    stop music fadeout 3
    scene ep9_jill_lewd74 with dissolve
    ji "Oh... But I did..."
else:
    scene ep9_jill_lewd73 with dissolve
    mc "Really?"
    scene ep9_jill_lewd74 with dissolve
    ji "Yes. It felt very good."
    scene ep9_jill_lewd73 with dissolve
    mc "Good... I wasn't sure."
    stop music fadeout 3
    scene ep9_jill_lewd75 with dissolve
    ji "Oh... I did enjoy it a lot."

$ renpy.end_replay()
$ persistent.ep9_lewd_jill2 = True
$ calcScenes()
show screen new_phone_screen
play music "music/ep9/tremolo.mp3"
scene ep9_jill_lewd76 with dissolve
ji "Do you...um..."
ji "Do you find it bad that I'm not as vocal as you during...?"
scene ep9_jill_lewd77 with dissolve
menu:
    "You'll get there":
        mc "You'll get there someday. I wasn't very vocal at the beginning, either."
        mc "It took me a while to get comfortable talking during sex. And I can honestly still feel a bit stupid saying things..."
        mc "But I find it hot, so don't be scared if you want to talk."
        scene ep9_jill_lewd76 with dissolve
        ji "I'll try."
    "I wish you were":
        mc "It's not bad, but I wish that you were."
        mc "Sexy talk is hot, so don't be scared to try it."
        scene ep9_jill_lewd76 with dissolve
        ji "I'll do my best to get better at it then."
ji "But I don't know what to say."
scene ep9_jill_lewd77 with dissolve
mc "It doesn't have to be hard. Say what you feel. Let me know if something feels good or bad or if the speed is too slow or fast..."
mc "What you like me to do, what you like to do to me... There are a lot of things you can say."
scene ep9_jill_lewd78 with dissolve
ji "I'm blushing thinking about it. The thought of saying it out loud... *{i}Phew{/i}*"
scene ep9_jill_lewd77 with dissolve
mc "I'll help you get comfortable with it if you promise to try your best. Deal?"
scene ep9_jill_lewd76 with dissolve
ji "Ok."
scene ep9_jill_lewd77 with dissolve
mc "And you will get comfortable. Give it time."

if swyper_rejected_by_ida:
    scene ep9_jill_lewd79 with dissolve
    ji "Maybe this is a stupid question, but... What was that about before?"
    ji "The thing with the Santa girl?"
    scene ep9_jill_lewd80 with dissolve
    mc "Oh, that..."
    mc "Well, I was using this dating app called Swyper."
    mc "And I got a match with her, but she was using her friend's pictures in her profile."
    scene ep9_jill_lewd79 with dissolve
    ji "I see. But what about what she said?"
    scene ep9_jill_lewd80 with dissolve
    mc "What of it?"
    scene ep9_jill_lewd79 with dissolve
    ji "She called you names and said you were horrible to her...and a bully. What was that about?"
    scene ep9_jill_lewd80 with dissolve
    if persistent.mod_wtenabled: 
                        $mod_choices = ["(-Jill)","(+Maya)","(-DIK)","(+DIK)","(Sandy scene)","(Sarah scene)","","","","","","" ]
                        #[mod_gr][mod_choices[0]]
    menu:
        "She's lying":
            mc "Just like she was lying about who she was on that dating app, she's lying about me."
            scene ep9_jill_lewd81 with dissolve
            ji "So, you didn't treat her badly?"
            scene ep9_jill_lewd80 with dissolve
            mc "I don't remember what I said exactly, but I ticked her off when I figured out she was a catfish."
            scene ep9_jill_lewd79 with dissolve
            ji "Ok."
            scene ep9_jill_lewd80 with dissolve
        "It's my fault":
            mc "It could be my fault. I probably made her mad when I realized she was a catfish."
            mc "She wasn't taking the dating app seriously, so I felt I didn't have to take her seriously either."
            scene ep9_jill_lewd80 with dissolve
            mc "I was using the app for the right reasons, and she wasn't. That made me irritated."
            scene ep9_jill_lewd79 with dissolve
            ji "I can understand that."
            scene ep9_jill_lewd80 with dissolve
        "I don't know [mod_gr][mod_choices[0]]":
            $ RPjill -= 1
            mc "I don't know."
            scene ep9_jill_lewd81 with dissolve
            ji "You don't know? Did she call you that for no reason?"
            scene ep9_jill_lewd80 with dissolve
            mc "I don't know why she called me that."
            mc "There's something wrong with her. To use her friend's pictures like that and fool guys on that dating app..."
            mc "I mean, who does that?"
            scene ep9_jill_lewd81 with dissolve
            ji "Do you think she was ashamed of herself?"
            scene ep9_jill_lewd80 with dissolve
            mc "Maybe. I wouldn't have matched with her if she used her real pictures; I can tell you that much."

    mc "Why are you asking?"
    scene ep9_jill_lewd81 with dissolve
    ji "It shocked me to hear someone call you those names in front of all those people. It doesn't align with what I think of you at all."
    ji "So, I wanted to talk to you about how she and I could have such polar opposite views of the same person."
    scene ep9_jill_lewd80 with dissolve
    mc "It was a bit embarrassing, but it worked out all right."
    scene ep9_jill_lewd79 with dissolve
    ji "Yeah."

if ep9_jm_sad:
    scene ep9_jill_lewd82 with dissolve
    ji "So... How do you feel now about what happened with those girls you mentioned?"
    ji "Do you want to talk about it?"
    scene ep9_jill_lewd80 with dissolve
    mc "No. Not really."
    mc "I'm trying to...put it out of my mind. I feel very guilty."
    scene ep9_jill_lewd80 with dissolve
    ji "..."
    scene ep9_jill_lewd82 with dissolve
    ji "Can I just say how much I appreciate you for doing that?"
    scene ep9_jill_lewd80 with dissolve
    mc "I should have done it earlier, but I didn't want it still hanging there when we went public."
    scene ep9_jill_lewd81 with dissolve
    ji "That's what I appreciate. It feels like you are serious about us, like you said you were."
    ji "It couldn't have been easy for you to do that tonight."
    ji "And I want you to know that if you had told me about it beforehand, I wouldn't have pushed you to tell our friends tonight."
    ji "I feel a bit guilty too."
    scene ep9_jill_lewd80 with dissolve
    mc "It's not you who should feel guilty. I've made my choices and mistakes on my own."
    mc "And even though I'm sad about this, I had to do it to be truly happy with you. And that's what counts."
    scene ep9_jill_lewd83 with dissolve
    ji "Was it...Josy?"
    scene ep9_jill_lewd80 with dissolve
    mc "..."
    mc "It was."
    scene ep9_jill_lewd83 with dissolve
    ji "That's why I feel guilty."
    scene ep9_jill_lewd84 with dissolve
    mc "She cried...and she ran away from me."
    mc "I'm unsure if she'll want to talk to me again after this."
    scene ep9_jill_lewd85 with dissolve
    ji "Now I'm sad too."
    scene ep9_jill_lewd95 with dissolve
    $ renpy.pause(0.5)
    scene ep9_jill_lewd95b with dissolve
    $ renpy.pause(0.5)
    scene ep9_jill_lewd95 with dissolve
    $ renpy.pause()
    scene ep9_jill_lewd86 with dissolve
    mc "This was one hell of a night..."
    scene ep9_jill_lewd87 with dissolve
    ji "It was both good and bad. Mostly good..."
    scene ep9_jill_lewd86 with dissolve
    mc "You had fun, right?"
else:
    scene ep9_jill_lewd87 with dissolve
    ji "This party was something else..."
    ji "From what I could tell, everyone was having so much fun."
    scene ep9_jill_lewd86 with dissolve
    mc "Including you?"

scene ep9_jill_lewd87 with dissolve
ji "Yes. I've never been to a party like this one before. Weirdly, it reminded me of the times Bianca and I had our parties."
scene ep9_jill_lewd88 with dissolve
mc "Oh, yes. Your private parties with Bianca in the barn, right?"
scene ep9_jill_lewd87 with dissolve
ji "It was mostly outdoors, but yes."
scene ep9_jill_lewd88 with dissolve
mc "I like Bianca. She's very fun."
scene ep9_jill_lewd89 with dissolve
ji "She is, isn't she? It was such a shame that Olivia got sick."
scene ep9_jill_lewd88 with dissolve
if persistent.mod_wtenabled: 
                        $mod_choices = ["(Pick if you want)","(+Maya)","(-DIK)","(+DIK)","(Sandy scene)","(Sarah scene)","","","","","","" ]
                        #[mod_gr][mod_choices[0]]
menu:
    "[mod_gr]Tell Jill what you saw":
        $ ep9_told_jill = True
        if ep9_jm_sad:
            mc "I hate to pile on with sad news, but... I saw something happen tonight. It involves Matthew and Olivia."
        else:
            mc "About that... I saw something happen tonight. It involves Matthew and Olivia."
        scene ep9_jill_lewd90 with dissolve
        ji "Oh? Tell me."
        scene ep9_jill_lewd80 with dissolve
        mc "I saw them making out."
        scene ep9_jill_lewd90 with dissolve
        ji "Matthew? And...Olivia?"
        ji "You're joking, right?"
        scene ep9_jill_lewd92 with dissolve
        mc "I wish I were. They pretended as if nothing had happened when I walked into the room."
        mc "And after I told them I saw what they did, Matthew got mad at me and told me not to tell anyone about it."
        scene ep9_jill_lewd91 with dissolve
        ji "Is that why they left early...?"
        scene ep9_jill_lewd92 with dissolve
        mc "I believe so..."
        scene ep9_jill_lewd91 with dissolve
        ji "Oh my God... Bianca..."
        scene ep9_jill_lewd92 with dissolve
        mc "..."
        mc "We need to tell her...right?"
        scene ep9_jill_lewd91 with dissolve
        ji "She will be devastated. They're living together... And then there's Andy... Oh, no..."
        scene ep9_jill_lewd92 with dissolve
        if ep9_jm_sad:
            mc "I hate that I keep ruining your night with this, but I couldn't keep this from you."
        else:
            mc "I hate that I had to ruin your night with this, but I couldn't keep this from you."
        scene ep9_jill_lewd91 with dissolve
        ji "How do I tell Bianca this?"
        scene ep9_jill_lewd93 with dissolve
        $ renpy.pause()
        $ new_bio("Jill", "I told Jill about Matthew cheating on Bianca with Olivia.")
    "Don't tell Jill about Matthew":
        $ ep9_told_jill = False
        mc "Yeah... That was a real bummer..."
        scene ep9_jill_lewd94 with dissolve
        $ renpy.pause()
        $ new_bio("Jill", "I didn't tell Jill about Matthew cheating on Bianca with Olivia.")

$ new_bio("Jill", "I had sex with Jill after the Halloween party, and she stayed the night.")
$ mphone_stats_add_girl_s3("jill","You had sex with Jill after the Halloween party in episode 9.")

if not persistent.ep9_card2:
    $ persistent.ep9_card2 = True
    $ persistent.rew_2d_unlocked += 1
    $ persistent.chat_new_rewards = True
    $ calcRenders()
if not persistent.ep9_card3:
    $ persistent.ep9_card3 = True
    $ persistent.rew_2d_unlocked += 1
    $ persistent.chat_new_rewards = True
    $ calcRenders()
stop music fadeout 3

if "Jill" not in wt_ep9_scenes:
    $wt_ep9_scenes.append("Jill")



if wt_ep9_branch_numbers != 1:
    "See other scenes?"
    menu:
          "Josy & Maya" if branchMayaJosy and "Josy" not in wt_ep9_scenes:
            if "Josy" not in wt_ep9_scenes:
                $wt_ep9_scenes.append("Josy")
            jump ep9_jm_committing_label
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

label ep9_ending_jill_label:
scene ep9_ending_jill1 with dissolve
$ renpy.pause()
scene ep9_ending_jill2 with dissolve
$ renpy.pause()
scene ep9_ending_jill3 with dissolve
ji "Morning."
scene ep9_ending_jill4 with dissolve
mc "Morning, beautiful."
scene ep9_ending_jill5 with dissolve
ji "Yeah, right. I feel like such a mess."
scene ep9_ending_jill4 with dissolve
mc "You're my mess."
scene ep9_ending_jill5 with dissolve
ji "Thanks for a wonderful night and party."
scene ep9_ending_jill4 with dissolve
mc "I'm happy you showed up. I was worried you wouldn't enjoy it since it's different from what you're used to."
scene ep9_ending_jill5 with dissolve
ji "Different can be good. I'm happy to see how you live and who you spend your time with."
ji "I understand you a bit better now."
scene ep9_ending_jill4 with dissolve
mc "What do you mean?"
scene ep9_ending_jill6 with dissolve
ji "Why you want to stay here, for one. And I've seen that you can be yourself even when you're around your friends."
scene ep9_ending_jill4 with dissolve
mc "We didn't talk to them a lot together, though."
scene ep9_ending_jill5 with dissolve
ji "Now that we're gonna be official... We should."
ji "I want to get to know your friends."
scene ep9_ending_jill4 with dissolve
mc "They aren't like your friends, you know."
scene ep9_ending_jill5 with dissolve
ji "It doesn't matter. They can be whatever they are."
ji "You are you. That's what matters."
scene ep9_ending_jill8 with dissolve
dikcs "*{i}Sings{/i}* She fucked a DIK! He came real quick! And now she does the walk!"
dikcs "*{i}Sings{/i}* What walk!?"
mc "Fuck..."
scene ep9_ending_jill7 with dissolve
ji "What's wrong?"
scene ep9_ending_jill4 with dissolve
mc "They have this tradition... It's pretty bad."
mc "They make fun of the girls who spend the night with someone as they walk home."
scene ep9_ending_jill7 with dissolve
ji "That's not nice... Um... Maybe I should take the window?"
scene ep9_ending_jill4 with dissolve
mc "You can't do that every time you spend the night here. Sooner or later, they'll find a way to get you."
mc "And I wanna be able to have breakfast with you and stuff."
scene ep9_ending_jill7 with dissolve
ji "So... What should I do?"
scene ep9_ending_jill4 with dissolve
mc "Put on some of my clothes and wait here. I'll fix this."
scene ep9_ending_jill9 with dissolve
dikcs "YAY!!!"
scene ep9_ending_jill10 with dissolve
mc "It's me."
scene ep9_ending_jill14 with dissolve
tm "Well? We're waiting for whoever it is in your room."
scene ep9_ending_jill10 with dissolve
mc "The girl you're waiting for is my girlfriend."
scene ep9_ending_jill15 with dissolve
rs "You've got a girlfriend?"
tm "Bullshit!"
scene ep9_ending_jill11 with dissolve
mc "Nope. It's not bullshit. It's real, and it's happening."
mc "I'm not letting her walk out to this because that would scare her away and be demeaning to her."
scene ep9_ending_jill14 with dissolve
tm "That's kind of the point of this. It's tradition!"
scene ep9_ending_jill11 with dissolve
mc "Well, you're gonna have to stop that tradition for her."
scene ep9_ending_jill14 with dissolve
tm "No way! Every girl gets it."
scene ep9_ending_jill20 with dissolve
mc "Not my girl."
scene ep9_ending_jill16 with dissolve
le "We don't do it for girlfriends. I mean, Heather and Elena don't get it these days."
le "Plus, he's kinda sucking the fun out of it."
scene ep9_ending_jill17 with dissolve
rs "It's ok, Tommy. Let this one slide."
scene ep9_ending_jill11 with dissolve
mc "Great. I appreciate it! Let me introduce you to her instead."
scene ep9_ending_jill12 with dissolve
mc "Everyone. This is my girlfriend. Jill."
mc "Jill, meet some of my friends."
scene ep9_ending_jill13 with dissolve
ji "Good morning..."
scene ep9_ending_jill18 with dissolve
le "*{i}Whispers{/i}* Jill Royce? That's fucking huge."
scene ep9_ending_jill19 with dissolve
$ renpy.pause()
$ new_bio("Jill", "I introduced Jill to some of the DIKs after the Halloween party.")
jump ep9_ending2_label
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
