label ep10_sage_intro_label:
$ guideSuggestedPage = 92
scene ep10_dik_intro1 with dissolve
$ renpy.pause()
scene ep10_dik_intro2 with dissolve
mc "I thought you left."
scene ep10_dik_intro3 with vpunch
mc "Whoa!"
mc "Uh... Hey... What's up?"
scene ep10_dik_intro4 with dissolve
tm "You fucked the HOTs' president."
scene ep10_dik_intro5 with dissolve
menu:
    "Yes":
        mc "Her name is Sage, and what about it?"
        scene ep10_dik_intro4 with dissolve
        tm "This is awesome."
        scene ep10_dik_intro5 with dissolve
    "No":
        mc "No, I didn't."
        scene ep10_dik_intro4 with dissolve
        tm "Aw. You're trying to hide it, too."
        tm "She told me you did, so there's no point in denying it."
        scene ep10_dik_intro5 with dissolve
    "Who? Me?":
        mc "Who? Me?"
        tm "Mhm."
mc "What do you want, Tommy?"
scene ep10_dik_intro6 with dissolve
tm "I want you to share all the details. Leave nothing to the imagination."
tm "How did you fuck her? Is she into freaky shit?"
tm "Did you stick your Willy Wonka in her chocolate factory?"
scene ep10_dik_intro7 with dissolve
mc "I won't tell you any of that."
scene anim_plug_jiggle_ep10 with dissolve
tm "You know you want to."
mc "I really don't."
scene ep10_dik_intro8 with dissolve
tm "Come on, bro! That's what you do with your pals."
scene ep10_dik_intro9 with dissolve

if persistent.mod_wt_enabled: 
                    $mod_choices = ["(+Maya)","(+Josy)","(-DIK)","(+DIK)","(-Maya)","(-Josy)","","","","","","" ]
                    #[m_c1][mod_choices[0]]

menu:
    "Share with him [m_c1][mod_choices[3]]":
        $ dk(1)
        $ ep10_tommy_reply = 1
        mc "*{i}Sigh{/i}* Ok. What do you want to know?"
        scene ep10_dik_intro10 with dissolve
        tm "Where do I even start?"
    "We're pals now?":
        $ ep10_tommy_reply = 2
        mc "We're pals now?"
        scene ep10_dik_intro10 with dissolve
    "That's private [m_c1][mod_choices[2]]":
        $ ep10_tommy_reply = 3
        $ dk(-1)
        mc "It is? To me, that seems private."
        scene ep10_dik_intro10 with dissolve
        tm "Hell no, there's nothing private about that."
tm "How much did her asshole gape? Was there any shit on your cock after? Does she squirt?"
scene ep10_dik_intro11 with dissolve
mc "Tommy..."
scene ep10_dik_intro12 with dissolve
tm "Heather squirts. The first time she did, it shocked me."
scene ep10_dik_intro13 with dissolve
tm "The feeling of it was like taking a piss against the wind. You know that misty spray that will hit you back in the face?"
scene ep10_dik_intro14 with dissolve
mc "This is...oversharing."
scene ep10_dik_intro13 with dissolve
tm "But the second time she did it, it was more like when you get a haircut in a salon and they use that water bottle on you."
tm "And after that, it's like getting ready for a night out and you put on perfume. It starts to smell nice and you've gotten used to it."
scene ep10_dik_intro14 with dissolve
mc "Dude...stop it."
scene ep10_dik_intro12 with dissolve
tm "Squirting rocks, bro. So, did she?"
scene ep10_dik_intro14 with dissolve
if ep10_tommy_reply == 3:
    mc "My answer is the same as before: I won't tell you any of it."
elif ep10_tommy_reply == 2:
    mc "I won't tell you anything like that."
elif ep10_tommy_reply == 1:
    mc "Not really."

scene ep10_dik_intro15 with dissolve
tm "Well, give me something! You fucked upwards, bro!"
scene ep10_dik_intro16 with dissolve
mc "What do you mean?"
scene ep10_dik_intro15 with dissolve
tm "You're a freshman, and you managed to bang a senior who's a sorority president."
tm "And now she tells us she'll bring more girls in here to fuck you."
tm "How do you do that?"
scene ep10_dik_intro16 with dissolve
mc "Uh..."
scene ep10_dik_intro15 with dissolve
tm "My first thought was that it's your dick size, but I've got a meaty one, too, and I don't get the same treatment as easily."
tm "What other tricks do you use?"
if ep10_tommy_reply == 1:
    scene ep10_dik_intro16 with dissolve
    mc "I'm not using any tricks. I'm just being myself. And yeah, I fucked her ass."
    scene ep10_dik_intro17 with dissolve
    tm "How much did you have to beg her to do that?"
    scene ep10_dik_intro18 with dissolve
    mc "I didn't have to beg. She wanted me to do it. When I returned to my room, she was in there waiting for me with that butt plug in her ass."
else:
    scene ep10_dik_intro16 with dissolve
    mc "I...uh..."
    mc "I fucked her ass. Happy?"
scene ep10_dik_intro17 with dissolve
tm "Oh, wow!"
tm "What a wonderful day."
tm "She can take a dick that big, huh?"
scene ep10_dik_intro18 with dissolve
if ep10_tommy_reply == 1:
    mc "Maybe this was a mistake..."
else:
    mc "This was a mistake."
scene ep10_dik_intro15 with dissolve
tm "Hell no, it wasn't!"
tm "John Boy never tells me something new, I don't wanna hear anything about Jamie's purple monster... I still regret hearing that her carpet doesn't match the drapes."
tm "Jacob doesn't always share his stories, Rusty is Rusty, Nick barely fucks, and Derek and I aren't there yet."
scene ep10_dik_intro17 with dissolve
tm "Leon told me some great tales, but now we have you!"
tm "And I'm here for it."
scene ep10_dik_intro18 with dissolve
if ep10_tommy_reply == 1:
    mc "Maybe we can do this another time when I'm not hungover and naked?"
else:
    mc "Maybe another time?"
scene ep10_dik_intro17 with dissolve
tm "Oh, definitely."
scene ep10_dik_intro19 with dissolve
tm "By the way, you have to tell Sage to bring the HOTs here for cleaning again. We kinda ruined it."
scene ep10_dik_intro20 with dissolve
mc "I don't know what you mean by that, but ok."
scene ep10_dik_intro21 with dissolve
mc "Tommy? The butt plug..."
scene ep10_dik_intro22 with dissolve
tm "Oh, right!"
scene ep10_dik_intro23 with dissolve
tm "*{i}Sniff sniff{/i}*"
scene ep10_dik_intro24 with vpunch
$ renpy.pause()
scene ep10_dik_intro25 with dissolve
$ renpy.pause()
$ new_bio("Tommy", "Tommy found out I'm having sex with Sage, and he wanted me to tell him all the details, while he overshared lots of his past experiences.")
jump ep10_dik_intro_label

label ep10_sage_chill_label:
scene ep10_sage_chill1 with wipeleft
sa "I'm exhausted."
mc "Same."
play music "music/ep7/licensed_music/track54.mp3"
queue music ["music/ep7/licensed_music/track58.mp3","music/ep8/licensed_music/track61.mp3","music/ep7/licensed_music/track54.mp3"]
scene ep10_sage_chill2 with dissolve
sa "Music, check! Let's get into bed already."
scene ep10_sage_chill3 with dissolve
mc "About bed, you left your toy at my place."
scene ep10_sage_chill4 with dissolve
sa "Right. Give it to me whenever."
scene ep10_sage_chill3 with dissolve
mc "By the way, Tommy found it when he woke me up. He knows we...did that."
scene ep10_sage_chill4 with dissolve
sa "So?"
scene ep10_sage_chill3 with dissolve
mc "I thought you wanted to know."
scene ep10_sage_chill5 with dissolve
sa "I'm pretty sure he wasn't surprised by it after what I told them when I walked out to their walk of shame."
scene ep10_sage_chill6 with dissolve
mc "You seemed to have impressed them."
scene ep10_sage_chill5 with dissolve
sa "I'm sure they won't be singing that song to me next time."
scene ep10_sage_chill6 with dissolve
mc "That's good. I want you to feel comfortable when you stay at my place."
scene ep10_sage_chill5 with dissolve
sa "Speaking of being comfortable... Come here."
scene ep10_sage_chill6 with dissolve
mc "I'm too tired for sex."
scene ep10_sage_chill7 with dissolve
sa "That's not what I wanted to do."
scene ep10_sage_chill8 with dissolve
mc "Oh. I thought it was."
scene ep10_sage_chill7 with dissolve
sa "Why?"
scene ep10_sage_chill8 with dissolve
mc "Because we've been doing that a lot lately."
scene ep10_sage_chill7 with dissolve
sa "Yeah? We've been horny. What's wrong with that?"
scene ep10_sage_chill8 with dissolve
mc "I don't wanna start a stupid fight. Sorry for assuming that you wanted sex."
scene ep10_sage_chill5 with dissolve
sa "Lie down on me."
scene ep10_sage_chill11 with dissolve
mc "This feels nice."
scene ep10_sage_chill10 with dissolve
sa "Good."
scene ep10_sage_chill9 with dissolve
mc "But I gotta say this still feels awfully close to sex."
scene ep10_sage_chill10 with dissolve
sa "You never know when to quit, do you?"
scene ep10_sage_chill11 with dissolve
mc "You're right. I don't know when to quit when it comes to you."
mc "I'm not trying to piss you off with what I say or do, you know?"
mc "You're very quick to anger."
scene ep10_sage_chill12 with dissolve
sa "That's not something new. And you know why."
scene ep10_sage_chill13 with dissolve
mc "I'm not trying to change you into someone you're not, but will this be a big issue between us?"
mc "Last night, I was worried about opening my mouth and ruining the party for you. So, I played it safe and focused on having fun with you."
scene ep10_sage_chill14 with dissolve
sa "It doesn't always have to be serious, does it? Why can't it be about having a good time?"
sa "Would you really like it if everything we did was having serious talks? Don't you want to chill out and have fun with me too?"
scene ep10_sage_chill15 with dissolve
mc "Of course, I want that. And we're still learning how each other works."
mc "But I worry about this a lot."
scene ep10_sage_chill16 with dissolve
mc "If I say something hurtful or mean, I get why you'd be angry with me, but I don't wanna feel scared of asking you questions or bringing you bad news."
mc "I don't mean to hurt you with what I ask or say. And I don't think staying silent not to risk upsetting you will work for me."
scene ep10_sage_chill17 with dissolve
sa "I'm sorry, but some of your questions hit too close to home."
sa "You're asking me things no one else does, and you do it so easily."
sa "And when I don't have an easy answer or don't want to answer or even think about it...I get mad."
scene ep10_sage_chill18 with dissolve
mc "..."
scene ep10_sage_chill17 with dissolve
sa "It's not you, [name]. It's my problem."
scene ep10_sage_chill18 with dissolve
mc "What can I do to make it better?"
scene ep10_sage_chill19 with dissolve
sa "I don't want you to feel worried about asking me stuff. That hurts to hear."
sa "That's not what I want for us."
sa "Be patient with me... I might get mad at times, but you know I still lo..."
scene ep10_sage_chill20 with dissolve
sa "...like you."
scene ep10_sage_chill21 with dissolve
mc "What was that?"
scene ep10_sage_chill22 with vpunch
sa "I fucking misspoke, ok?"
scene ep10_sage_chill23 with dissolve
mc "..."
scene ep10_sage_chill24 with dissolve
mc "I like you too. And what you're doing with your fingers. It makes me sleepy."
scene ep10_sage_chill25 with dissolve
$ renpy.pause()
scene ep10_sage_chill26 with dissolve
$ renpy.pause()
if ep9_jm_sad:
    scene ep10_sage_chill28 with dissolve
    mc "I need to tell you something, but I'm not sure if this is the right moment for it."
    scene ep10_sage_chill29 with dissolve
    sa "Go ahead. I'm listening."
    scene ep10_sage_chill28 with dissolve
    mc "I don't know where to start or how to say this, but..."
    mc "*{i}Sigh{/i}*"
    mc "I've been dating Josy and Maya, and I broke up with them last night because I wanna be with you."
    scene ep10_sage_chill30 with dissolve
    sa "What?"
    scene ep10_sage_chill31 with dissolve
    mc "It's a long story. And parts of it started even before I came to college."
    scene ep10_sage_chill30 with dissolve
    sa "Tell me what I need to know."
    scene ep10_sage_chill32 with fade
    $ renpy.pause()
    scene ep10_sage_chill33 with dissolve
    sa "[name]... This is horrible."
    scene ep10_sage_chill35 with dissolve
    mc "Yeah, I know. I feel terrible about it."
    scene ep10_sage_chill33 with dissolve
    sa "I knew you guys had some history, but after learning about her and Josy, I didn't think more about it."
    sa "But now I get what Maya told me last night about kissing you..."
    sa "It sounds like you hurt them."
    scene ep10_sage_chill35 with dissolve
    mc "I did. Josy doesn't even want to be my friend anymore."
    mc "I don't know what to do."
    mc "And now I've also put you in a bad spot with both of them."
    scene ep10_sage_chill33 with dissolve
    sa "I can't ignore this. I have to talk to them about it."
    scene ep10_sage_chill35 with dissolve
    mc "And say what?"
    scene ep10_sage_chill34 with dissolve
    sa "I don't know. Something!"
    sa "If Josy doesn't want to be your friend, how can I expect her to stay mine?"
    scene ep10_sage_chill35 with dissolve
    mc "I'm so sorry for this mess. I never knew it would come to this."
    mc "And I ruined another good moment with you..."
    scene ep10_sage_chill34 with dissolve
    sa "Are you feeling ok?"
    scene ep10_sage_chill35 with dissolve
    mc "No. I try to keep a straight face, but I'm hurting a lot."
    mc "They mean a lot to me."
    scene ep10_sage_chill34 with dissolve
    sa "Lie down on me again."
    scene ep10_sage_chill36 with dissolve
    $ renpy.pause()
    stop music fadeout 5
    scene ep10_sage_chill37 with dissolve
    sa "It will be alright, [name]. Thanks for telling me about it. I definitely needed to know it."
    scene ep10_sage_chill38 with dissolve
    $ renpy.pause()
    $ new_bio("Sage", "I told Sage about dating Josy and Maya and how they felt when I broke up with them. She was surprised and concerned about whether she could stay friends with them.")
else:
    stop music fadeout 3
    scene ep10_sage_chill27 with dissolve
    $ renpy.pause()
$ new_bio("Sage", "I told Sage about my concerns when it comes to bringing her bad news and asking her sensitive questions. It felt good to bring it up, and she seemed understanding.")
jump ep10_ip_label

label ep10_sage_mj_label:
play music "music/ep5/subtle_break.mp3"
scene ep10_sage_mj1 with wiperight
sa "When Maya told me about you two, I only thought that [name] supported you."
sa "I didn't understand his part in this and that he was dating you."
scene ep10_sage_mj2 with dissolve
js "It's not you who I'm mad at; it's him."
scene ep10_sage_mj7 with dissolve
sa "Yes. And that puts me in an awkward position."
sa "Can I do anything to help? I don't want this to be a problem between all of us."
scene ep10_sage_mj2 with dissolve
js "You can't help. There's nothing you can do to make this better."
scene ep10_sage_mj7 with dissolve
sa "There's got to be something I can do."
scene ep10_sage_mj2 with dissolve
js "Even if you dumped him and slapped him in the face, it wouldn't undo what he did."
js "There's nothing you can do about it."
scene ep10_sage_mj7 with dissolve
sa "He is upset about this. When he told me about it, I could tell he was hurting a great deal."
sa "He didn't do any of this on purpose. And neither did I."
sa "It just happened."
scene ep10_sage_mj4 with dissolve
my "You can blame me, if it helps. When we were talking about us three, I was the one who suggested to have no strings attached, remember?"
scene ep10_sage_mj3 with dissolve
js "I remember. And I told [name] I didn't agree with you two on that. I should have spoken up earlier."
js "I knew that he dated and this was a risk, but after being with him like we were together..."
js "Doing the things we did. Having so much fun and the intimacy... I thought he was as sure about us as I was about him."
scene ep10_sage_mj2 with dissolve
js "I think that's what hurts the most. I thought he was falling in love with me and never realized it was the opposite."
scene ep10_sage_mj5 with dissolve
my "..."
scene ep10_sage_mj7 with dissolve
sa "I'm so sorry. I understand why this hurts like hell for you two."
scene ep10_sage_mj6 with dissolve
my "This wasn't for nothing, right?"
scene ep10_sage_mj8 with dissolve
sa "What do you mean?"
scene ep10_sage_mj6 with dissolve
my "We felt strongly for him, and now he's with you."
my "I want to know that it wasn't for nothing."
scene ep10_sage_mj8 with dissolve
sa "I like him a lot. He's been there for me and made me open up about things I rarely talked about."
sa "He cares a lot about me, and even when I don't treat him well, he somehow manages to care."
scene ep10_sage_mj9 with dissolve
sa "And when he told me he wanted to date me and to make something more out of what we had..."
sa "I felt...weird."
scene ep10_sage_mj6 with dissolve
my "Weird?"
scene ep10_sage_mj9 with dissolve
sa "For the first time in my life, I felt that someone genuinely desired me for more than my body."
sa "That someone desired to be with me because of who I was."
scene ep10_sage_mj8 with dissolve
sa "*{i}Clears throat{/i}*"
sa "I didn't know I needed that."
scene ep10_sage_mj7 with dissolve
sa "From the sounds of it, I'm not quite where you were with him... You know... Emotionally."
sa "Maybe I will be someday... But...yeah...it wasn't for nothing."
stop music fadeout 3
sa "And after hearing what you just said, I realize it was a harder choice for him than I thought."
scene ep10_sage_mj1 with dissolve
$ renpy.pause()
jump ep10_yoga_label

label ep10_sage_mj2_label:
play music "music/ep5/subtle_break.mp3"
scene ep10_sage_mj1 with wiperight
sa "When Maya told me about you two, I only thought that [name] supported you."
sa "I didn't understand his part in this and that he was dating you."
scene ep10_sage_mj2 with dissolve
if branchJill:
    js "Yeah, well, he was. And now he dumped us like we didn't matter to him to be with Jill."
else:
    js "Yeah, well, he was. And now he dumped us like we didn't matter to him to be with someone else."

scene ep10_sage_mj7 with dissolve
if pathSage or ep7_pathSage:
    sa "Not that long ago, he gave me a similar speech. We weren't dating, but...um...or were we? I don't know."
    sa "Anyway, being rejected always sucks, but you can't force someone to stay with you. Believe me, I've tried."
else:
    sa "Being rejected always sucks, but in the end, you can't force someone to stay with you. Trust me, I've tried."
sa "Can I do anything to help? I don't want this to be a problem since we're close with him."
scene ep10_sage_mj2 with dissolve
js "You can't help. There's nothing you can do to make this better."
scene ep10_sage_mj7 with dissolve
sa "There's got to be something I can do."
scene ep10_sage_mj2 with dissolve
js "Even if you slapped him in the face, it wouldn't undo what he did."
js "There's nothing you can do about it."
scene ep10_sage_mj7 with dissolve
sa "To me, he seems upset about this. He's pretty easy to read and I could see it in his eyes when we all got together."
sa "I don't think he did any of this on purpose."
scene ep10_sage_mj4 with dissolve
my "You can blame me if it helps. When we were talking about us three, I was the one who suggested to have no strings attached, remember?"
scene ep10_sage_mj3 with dissolve
js "I remember. And I told [name] I didn't agree with you two on that. I should have spoken up earlier."
js "I knew that he dated and this was a risk, but after being with him like we were together..."
js "Doing the things we did. Having so much fun and the intimacy... I thought he was as sure about us as I was about him."
scene ep10_sage_mj2 with dissolve
js "I think that's what hurts the most. I thought he was falling in love with me and never realized it was the opposite."
scene ep10_sage_mj5 with dissolve
my "..."
scene ep10_sage_mj7 with dissolve
sa "I'm so sorry. Take it from someone who's been through a breakup recently..."
sa "Even though it hurts and you don't know what to do at first...it will get better."
if pathSage or ep7_pathSage:
    scene ep10_sage_mj6 with dissolve
    my "We felt strongly for him... That's the hardest part. Letting go of those feelings."
    my "Did...you feel that way about him, too?"
    scene ep10_sage_mj8 with dissolve
    sa "I like him a lot. He's been there for me and he made me open up about things I rarely talked about."
    sa "He cares a lot about me, and even when I don't treat him well, he somehow manages to care."
    scene ep10_sage_mj9 with dissolve
    sa "And when he told me he wanted to date someone else..."
    sa "I felt...weird."
    scene ep10_sage_mj6 with dissolve
    my "Weird?"
    scene ep10_sage_mj9 with dissolve
    sa "Yeah, weird... Like... I don't know how to describe it."
    sa "I was ok with it, but a part of me felt sad."
    sa "Because for the first time in my life, I felt that someone genuinely cared for me. But then he let me go."
    scene ep10_sage_mj8 with dissolve
    sa "*{i}Clears throat{/i}*"
    sa "I didn't realize that I would feel that way about him."
    scene ep10_sage_mj7 with dissolve
    sa "After hearing what you just said, I realize he has that effect on people."
    sa "From the sounds of it, I wasn't quite where you were with him... You know... Emotionally."
    sa "But...yeah...I care about him, too."
    stop music fadeout 3
    sa "And, sorry, but I'm not surprised that we weren't the only ones who did."
else:
    stop music fadeout 3
scene ep10_sage_mj1 with dissolve
$ renpy.pause()
jump ep10_yoga_label

label ep10_sage_solo_label:
play music "music/ep7/good_old_days.mp3"
queue music ["music/ep2/simple_ballad.mp3","music/ep4/optimistic.mp3","music/ep7/good_old_days.mp3"]
scene ep10_sage_solo1 with wipeleft
cam "If you want to talk about it, I'm all ears."
scene ep10_sage_solo13 with dissolve
sa "Me too."
scene ep10_sage_solo9 with dissolve
he "Thanks, but I don't. I need to process it and think."
scene ep10_sage_solo2 with dissolve
cam "Totally. I'm just saying that venting always helps me."
scene ep10_sage_solo11 with dissolve
he "Drinking usually solves my problems. Cheers..."
scene ep10_sage_solo14 with dissolve
sa "[name] is coming soon. Do you want us to give you space?"
scene ep10_sage_solo10 with dissolve
he "No, it's nice to have distractions too. I don't mind."
scene ep10_sage_solo3 with dissolve
cam "I heard that you two are dating now. When did that happen?"
scene ep10_sage_solo15 with dissolve
if pathSage:
    sa "We started being fuck buddies and then he wanted something more... So, uh... I guess we're dating now."
    sa "But without the actual dating part, I guess. We haven't done that."
else:
    sa "We are, or...um...we're not. We've not been on one yet. But we've been sleeping together a lot."
scene ep10_sage_solo3 with dissolve
cam "Why haven't you been on one?"
scene ep10_sage_solo16 with dissolve
sa "There's been too much going on lately to get time for it. We haven't talked much about it either and I'm not sure what he's expecting."
sa "Did you girls ever take the initiative for a date?"
scene ep10_sage_solo4 with dissolve
cam "No, it's always been the guy who did it for me."
scene ep10_sage_solo11 with dissolve
he "Same. Except with Tommy. He never took me on one, so I had to do it."
he "It would have been nice to be surprised sometime."
scene ep10_sage_solo15 with dissolve
sa "Yeah, so that's where I'm at with him. I should talk to him about it."
sa "He mentioned wanting to take me on dates, cuddle, do sleepovers, and have long talks into the night."
scene ep10_sage_solo18 with dissolve
cam "Aw."
he "Ugh. Fuck you, that's too cute. Even for you."
scene ep10_sage_solo17 with dissolve
sa "Haha, even for me?"
scene ep10_sage_solo12 with dissolve
he "Isn't it?"
scene ep10_sage_solo15 with dissolve
sa "He pushes me out of my comfort zone a lot with those things."
sa "If it were up to me, we'd order a pizza, grab some beers and probably fuck."
scene ep10_sage_solo19 with dissolve
sa "But I don't think that's what he's looking for - hell, I'm not even sure what I'm looking for. But if I have to plan a date for us..."
sa "I don't think I could match his expectations. What would you do if you were me?"
if ep7_camila_lewd or ep7_rica_lewd or ep5_fuckedCamila or ep3_fuckedCamilaAndMona or ep1_lewd_camila_quinn or quinn_shop_spicy_lvl > 0:
    $ sage_dik += 1
    scene ep10_sage_solo5 with dissolve
    cam "What you're describing isn't the [name] I know. It sounds like you know him in a different way than me, so I have no clue."
    scene ep10_sage_solo20 with dissolve
    sa "In what way do you know him?"
    scene ep10_sage_solo7 with dissolve
    cam "Uh... Forget it. I don't know him."
    scene ep10_sage_solo20 with dissolve
    sa "You know him {i}that{/i} way, huh?"
    scene ep10_sage_solo6 with dissolve
    cam "It was before you dated him, I swear. It didn't mean anything."
    scene ep10_sage_solo20 with dissolve
    if affinity == "DIK":
        sa "I'd say I'm surprised, but I'm not."
    elif affinity == "NEUTRAL":
        sa "That's kinda surprising... But I can't blame you."
    else:
        sa "I never would have guessed you did that with him."
    sa "It's cool. Um... Thanks for telling me."
    scene ep10_sage_solo12 with dissolve
    he "It seems Cammy would suggest pizza and riding his dick as a date, too."
    scene ep10_sage_solo8 with dissolve
    cam "That's so cold."
    scene ep10_sage_solo21 with dissolve
    sa "Haha! Total bitch comment."
else:
    scene ep10_sage_solo6 with dissolve
    cam "I've never been in that situation, so I couldn't tell you."
    scene ep10_sage_solo12 with dissolve
    he "Pizza and riding his dick sounds like the dates I've been on, so I can't come up with something much better than that."
$ guideSuggestedPage = 128
scene ep10_sage_solo22 with dissolve
mc "Hey!"
scene ep10_sage_solo23 with dissolve
sa "Now hush."
scene ep10_sage_solo24 with dissolve
mc "You're making me miss summer..."
scene ep10_sage_solo25 with dissolve
sa "How? Is it the pool, drinks or the bikini?"
scene ep10_sage_solo26 with dissolve


if persistent.mod_wt_enabled: 
                    $mod_choices = ["(+Maya)","(+Josy)","(-DIK)","(+DIK)","(-Maya)","(-Josy)","","","","","","" ]
                    #[m_c1][mod_choices[0]]

menu:
    "All of it":
        mc "All of it. I'm loving it."
    "Bikini [m_c1][mod_choices[3]]":
        $ dk(1)
        mc "Mostly the bikini."
        if ep7_camila_lewd or ep7_rica_lewd or ep5_fuckedCamila or ep3_fuckedCamilaAndMona or ep1_lewd_camila_quinn or quinn_shop_spicy_lvl > 0:
            scene ep10_sage_solo29 with dissolve
            cam "*{i}Whispers{/i}* That sounds like the [name] I know."
scene ep10_sage_solo25 with dissolve
sa "This time of year is when this pool doesn't seem like a bad idea."
sa "It's a thunderstorm outside, but down here you couldn't tell."
scene ep10_sage_solo26 with dissolve
mc "Unless you get electrocuted from the lightning."
scene ep10_sage_solo27 with dissolve
sa "Why would you say that?"
scene ep10_sage_solo28 with dissolve
mc "I'm kidding; it's probably safe. I don't think lightning can get you down here."
mc "Although, a girl from my class back in high school sat by her computer as the outlet exploded during a thunderstorm."
mc "So, you never know."
scene ep10_sage_solo30 with dissolve
sa "Fucking jump into the pool already. That way, I'm taking you with me when I die from electrocution."
scene ep10_sage_solo31 with dissolve
$ renpy.sound.play("sound_effects/water_pool.mp3", channel="sfx2", loop=True)
mc "Is it just you girls here today?"
scene ep10_sage_solo32 with dissolve
sa "Yeah, it's just us. And don't get any naughty ideas."
scene ep10_sage_solo33 with dissolve
mc "I won't. I can be around you in a swimsuit without getting them."
scene ep10_sage_solo34 with dissolve
sa "I don't think you can."
mc "That's so unfair... I don't have anything similar I can do to tease you."
if (ep10_jm_solo == "Maya" or ep10_jm_solo=="Maya Josy"):
    scene ep10_sage_solo34b with dissolve
    mc "*{i}Whispers{/i}* But I guess I could try this..."
    scene ep10_sage_solo34c with dissolve
    sa "What are you doing?"
    scene ep10_sage_solo34b with dissolve
    mc "*{i}Whispers{/i}* Peanut butter sandwich."
    scene ep10_sage_solo34c with dissolve
    sa "Uh... Is that supposed to be sexy?"
    scene ep10_sage_solo33 with dissolve
    mc "Oh, well... I tried."
else:
    scene ep10_sage_solo35 with dissolve
    mc "A totally random question; showing you my balls wouldn't make you horny, would it?"
    scene ep10_sage_solo36 with dissolve
    sa "Hahaha!"
    sa "If you don't know the answer to that question, you need serious help."
scene ep10_sage_solo32 with dissolve
sa "Honestly, the sexiest thing you can do for me is to be yourself. I find it hot when you're confident."
scene ep10_sage_solo33 with dissolve
mc "I see."
scene ep10_sage_solo38 with dissolve
$ renpy.pause()
scene ep10_sage_solo37 with dissolve
sa "Fake confidence, however... It's a total turnoff."
$ renpy.music.stop(channel="sfx2", fadeout=3)
scene ep10_sage_solo39 with dissolve
cam "Wanna help her out with him?"
scene ep10_sage_solo40 with dissolve
if ep7_camila_lewd or ep7_rica_lewd or ep5_fuckedCamila or ep3_fuckedCamilaAndMona or ep1_lewd_camila_quinn or quinn_shop_spicy_lvl > 0:
    he "If you fucked him, I don't think you should push it."
    scene ep10_sage_solo41 with dissolve
    cam "Sage didn't seem too bothered by it."
    if ep7_camila_lewd or ep7_rica_lewd or ep5_fuckedCamila or ep3_fuckedCamilaAndMona or quinn_shop_spicy_lvl > 0:
        cam "And I'm surprised you haven't used one of your pluses on him."
        scene ep10_sage_solo40 with dissolve
        if ep9_heather_lewd == 1:
            he "Meh. If he wasn't with Sage now, I bet I could."
        else:
            he "Meh."
    else:
        cam "And besides, we didn't fuck, I just played with his cock a bit."
        scene ep10_sage_solo40 with dissolve
        he "Wow, that makes it so much better. Not."
    he "What do you have in mind?"
else:
    he "What do you have in mind?"
scene ep10_sage_solo42 with dissolve
cam "[name]! I already know some, but I'm dying to know more about you. What are your hobbies?"
scene ep10_sage_solo45 with dissolve
mc "My hobbies? Uh... I like to play the guitar and martial arts."
scene ep10_sage_solo42 with dissolve
cam "Did you ever play guitar together with Sage?"
if ep2SageGuitarTeacher:
    scene ep10_sage_solo43 with dissolve
    mc "Yeah, I've actually been teaching her the basics of it. But it's been a while since last time."
    scene ep10_sage_solo46 with dissolve
    sa "We should do it again soon if you're up for it."
    scene ep10_sage_solo42 with dissolve
    cam "Wow! If you ask me, that sounds like such a fun thing to do together as a date. Right, Heather?"
else:
    scene ep10_sage_solo46 with dissolve
    sa "I asked him to teach me how to play once, but he said no."
    scene ep10_sage_solo42 with dissolve
    cam "What!? Why did you say no? Don't you wanna teach her?"
    scene ep10_sage_solo47 with dissolve
    mc "Do you still wanna?"
    scene ep10_sage_solo46 with dissolve
    sa "Yeah, if you're up for it."
    scene ep10_sage_solo42 with dissolve
    cam "You should totally do that together. That sounds like a fun date, if you ask me. Right, Heather?"
scene ep10_sage_solo44 with dissolve
he "I'd prefer the pizza date."
scene ep10_sage_solo42 with dissolve
cam "Or maybe you can do something Sage likes to do for a date?"
scene ep10_sage_solo48 with dissolve
sa "Thanks, Camila. That's quite enough."
scene ep10_sage_solo49 with dissolve
mc "I think Camila is trying to get us talking about dating."
scene ep10_sage_solo50 with dissolve
sa "I didn't put her up to it, I swear."
scene ep10_sage_solo49 with dissolve
mc "Since it brought us to the topic of it... What about it?"
scene ep10_sage_solo51 with dissolve
sa "Do you still want to?"
scene ep10_sage_solo52 with dissolve

if persistent.mod_wt_enabled: 
                    $mod_choices = ["(-Sage)","(+Josy)","(-DIK)","(+DIK)","(-Maya)","(-Josy)","","","","","","" ]
                    #[m_c1][mod_choices[0]]

menu:
    "Of course":
        mc "Of course, I still want it."
        scene ep10_sage_solo51 with dissolve
        sa "Me too."
    "Joke [m_c1][mod_choices[0]]":
        $ RPsage -= 1
        mc "No, I've grown tired of you."
        scene ep10_sage_solo51b with dissolve
        sa "Tsk. Yeah, right."
        scene ep10_sage_solo52 with dissolve
        mc "But yeah, I still want to."
        scene ep10_sage_solo51 with dissolve
        sa "Me too."
scene ep10_sage_solo53 with dissolve
mc "What's something you'd like to do?"
scene ep10_sage_solo54 with dissolve
sa "I'm open to suggestions, but I'm having a hard time coming up with ideas."
scene ep10_sage_solo53 with dissolve
mc "Do you have any hobbies or interests that I don't know about?"
scene ep10_sage_solo54 with dissolve
sa "Probably plenty, yeah. But I'm not like you, who's like completely devoted to them."
scene ep10_sage_solo53 with dissolve
mc "Plenty? Tell me about them."
scene ep10_sage_solo55 with dissolve
sa "When I was young, my parents wanted me to be more social, and I wanted to keep to myself."
sa "They forced me to try new things to get me out of my shell."
scene ep10_sage_solo53 with dissolve
mc "They forced you?"
scene ep10_sage_solo55 with dissolve
sa "Yeah, they did. They said it was good for me, and they were right. It was good for me."
sa "Mom made me try these group activities to see if I would develop an interest in anything."
sa "But I realized in time that it wasn't about the hobby itself. It was about people skills and personal growth that mattered to her."
scene ep10_sage_solo57 with dissolve
sa "I was signed up for music lessons, but my brother teased me for it and I didn't even attend the first lesson before I quit."
scene ep10_sage_solo55 with dissolve
sa "Mom kept pushing for me to do stuff, and that's how I tried golfing."
sa "But Mom quickly learned that I was a sore loser and that my language and behavior didn't fit the sport."
scene ep10_sage_solo53 with dissolve
mc "Haha! Were you swearing a lot when playing?"
scene ep10_sage_solo54 with dissolve
sa "Fuck yeah, I did. I swore and threw my clubs when I missed the shots."
sa "Ironically. I could throw the clubs further than I could hit that fucking ball."
sa "Such a stupid sport... I wish I didn't suck at it, though."
scene ep10_sage_solo55 with dissolve
sa "And after golf didn't work out, Mom made me try something less competitive."
scene ep10_sage_solo53 with dissolve
mc "What's that?"
scene ep10_sage_solo54 with dissolve
sa "Birdwatching."
scene ep10_sage_solo53 with dissolve
if ep3_choseSage:
    mc "Wait... So, those binoculars you own...?"
    scene ep10_sage_solo55 with dissolve
    sa "I know you think it's stupid, but they were meant for birdwatching."
else:
    mc "Wait... So, those binoculars you own... Were they meant for birdwatching?"
    scene ep10_sage_solo55 with dissolve
    sa "Originally... Yeah, they were."
    sa "It's just that I haven't used them for that in a long time."
if ep3_choseSage:
    scene ep10_sage_solo56 with dissolve
    mc "I don't think it's stupid, but it definitely sounded like an excuse for spying on your ex-boyfriend."
    scene ep10_sage_solo55 with dissolve
    sa "Well, it was both. But I haven't used them for birdwatching in a long time."

sa "As you may already have guessed, birdwatching wasn't for me either."
sa "I think it was around this time I realized that I liked to compete, but Mom didn't want me to be angry as it didn't help my social game."
scene ep10_sage_solo56 with dissolve
mc "If you're competitive, I can't think of any sport that wouldn't bring that side out of you."
scene ep10_sage_solo55 with dissolve
sa "Neither could she. But that's how I eventually ended up in the tabletop club."
scene ep10_sage_solo53 with dissolve
mc "Is that like board games?"
scene ep10_sage_solo54 with dissolve
sa "It's that and much more."
sa "It was fun, it was competitive, and it was incredibly social."
sa "I made a lot of friends in that club and had a lot of fun."
scene ep10_sage_solo53 with dissolve
mc "Did you manage to keep your temper when playing?"
scene ep10_sage_solo54 with dissolve
sa "Haha, nope. I won a lot because I always tried to cheat."
sa "And I know my friends let it slide a few times, but when they didn't, I would sulk."
sa "But they always made it fun and managed to lighten my mood."
scene ep10_sage_solo53 with dissolve
mc "It sounds like you found your true hobby."
scene ep10_sage_solo54 with dissolve
sa "I already told you I'm not as devoted as you are. I didn't stick with it for too long."
sa "Eventually, I stopped going, and the friends I made I'd meet outside of the club."
sa "But yeah, it was a fun hobby for a while."
scene ep10_sage_solo53 with dissolve
mc "I don't know much about board games, just the usual dice games and that landlord game where you play as a shoe or something."
scene ep10_sage_solo55 with dissolve
sa "That's something that annoys me when people talk about board games. They always mention the \"classics\" as if they are the best games."
sa "Any true player would tell you they are the worst games and that there is another world of games to discover beyond them."
sa "And I think, if people only did venture into that world, they'd love board games too."
scene ep10_sage_solo53 with dissolve
mc "Well, that settles it. You have to show me some. Do you have any games here?"
scene ep10_sage_solo54 with dissolve
sa "No. Well, we probably have some, but they are the fucking classics. That wouldn't prove my point."
scene ep10_sage_solo59 with dissolve
sa "Heather? Do we have any good board games?"
scene ep10_sage_solo60 with dissolve
he "Do those exist?"
scene ep10_sage_solo54 with dissolve
sa "Case in point."
scene ep10_sage_solo61 with dissolve
cam "We have that Dots game."
scene ep10_sage_solo60 with dissolve
he "I wouldn't play that unless I was hammered or horny."
scene ep10_sage_solo59 with dissolve
sa "Yeah, it's not fun and I don't think [name] would be good at it."
scene ep10_sage_solo58 with dissolve
mc "Huh? I would beat all of you at Dots."
mc "What's Dots?"
scene ep10_sage_solo62 with wipeleft
he "Sage. Left foot on blue...or...left hand on green."
scene ep10_sage_solo63 with dissolve
sa "Blue it is."
scene ep10_sage_solo64 with dissolve
sa "How's it going, [name]? You're looking shaky."
scene ep10_sage_solo65 with dissolve
mc "You've been lucky with your options so far."
scene ep10_sage_solo66 with dissolve
cam "Haha! We're not lucky. You were kinda stupid with yours."
scene ep10_sage_solo64 with dissolve
sa "Yeah, it's a real amateur move, choosing to place a hand early on. Always pick a foot over a hand unless you're forced."
scene ep10_sage_solo67 with dissolve
if affinity == "DIK":
    mc "Yeah, but... I'm not complaining."
else:
    mc "Live and learn."
scene ep10_sage_solo68 with dissolve
he "[name]. Right hand on blue, or left foot on blue."
scene ep10_sage_solo69 with dissolve
mc "I'm not getting up from here, am I?"
sa "You could, but the odds are that you're screwed."
scene ep10_sage_solo70 with dissolve
he "Cammy. Left foot on pink or right hand on green."
scene ep10_sage_solo71 with dissolve
cam "Feet, all the way."
scene ep10_sage_solo72 with dissolve
he "Sage. Right hand on green or left hand on yellow."
scene ep10_sage_solo73 with dissolve
sa "Oh no! Now it got hard. [name] covers all green, but yellow might make me lose my balance."
mc "I think it's about time you used your hands."
scene ep10_sage_solo74 with dissolve
sa "All right, there we go. This boxes you in more too, you know?"
scene ep10_sage_solo75 with dissolve
mc "I've been down here for ages now. I've gotten comfortable."
scene ep10_sage_solo77 with dissolve
he "[name]. Lucky skip! Remove a limb or stay put. What do you wanna do?"
mc "If I remove something, I'll fall over. I'm gonna stay put."
scene ep10_sage_solo76 with dissolve
sa "I thought we were playing the game, not skipping turns."
scene ep10_sage_solo75 with dissolve
mc "Mocking me won't work."
scene ep10_sage_solo76 with dissolve
sa "*{i}Chicken noises{/i}*"
scene ep10_sage_solo75 with dissolve
mc "It must be hard playing a game where you can't cheat."
scene ep10_sage_solo77 with dissolve
he "Cammy. Right hand on blue, or right hand on yellow."
scene ep10_sage_solo79 with dissolve
cam "Such crappy choices. I'll go for yellow."
scene ep10_sage_solo78 with dissolve
mc "(Oh no...)"
$ guideSuggestedPage = 129
scene ep10_sage_solo80 with dissolve
sa "How's it going there, shaky?"
mc "I'm trying not to fall."
sa "You probably shouldn't get a boner, either."
$ ep10_dots_attitude = 0

if persistent.mod_wt_enabled: 
                    $mod_choices = ["(-Sage)","(+Josy)","(-DIK)","(+DIK)","(-Maya)","(-Josy)","","","","","","" ]
                    #[m_c1][mod_choices[0]]
                    if not ep9_sage_vanilla:
                        "scrappy" "Here you'll gain +Threesome points which can later lead to Camila x Sage threesome (You'll need 2 points atleast)." 
                        $ mod_choices[4]="(+Threesome)"
menu:
    "No promises [m_c1][mod_choices[3]][m_c2][mod_choices[4]]":
        $ dk(1)
        $ ep10_dots_attitude += 1
        mc "I'm making no promises."
    "I'm focusing here [m_c1][mod_choices[2]]":
        $ dk(-1)
        mc "I'm focusing here, Sage."
        sa "Haha!"
scene ep10_sage_solo81 with dissolve
he "You guys are a pizza and a six-pack short of a perfect date."
scene ep10_sage_solo82 with dissolve
"Hahaha!"
mc "What?"
sa "It's an inside joke."
scene ep10_sage_solo81 with dissolve
he "Sage. Lucky skip!"
scene ep10_sage_solo83 with dissolve
sa "Yes! Much more comfortable. *{i}Phew{/i}*"
scene ep10_sage_solo81 with dissolve
he "And with that, we enter the final phase. There will be only one choice from now on and no more lucky skips."
scene ep10_sage_solo84 with dissolve
sa "Now the game starts for real."
he "[name]. Right hand on pink."
scene ep10_sage_solo85 with dissolve
mc "It's already on pink."
sa "Then, you have to move it to another pink dot."
mc "I can't see where another pink is!"
he "There is one right next to your hand, toward the pool."
scene ep10_sage_solo86 with dissolve
mc "Here?"
he "Yes, you got it!"
sa "Heather, don't help him! That's cheating."
he "Cammy. Right foot on blue."
scene ep10_sage_solo87 with dissolve
cam "That was a lucky one."
he "Sage. Right foot on pink."
scene ep10_sage_solo88 with dissolve
sa "Ok, so I have to move it here, then. Hngn..."
scene ep10_sage_solo89 with dissolve
cam "Haha! Was that a groan?"
scene ep10_sage_solo90 with dissolve
sa "*{i}Whispers{/i}* I've got the balance, but my legs are cramping up... Help me out here. [name] can't win."
sa "*{i}Whispers{/i}* Push down on him."
scene ep10_sage_solo89 with dissolve
cam "*{i}Whispers{/i}* Are you sure?"
scene ep10_sage_solo90 with dissolve
sa "*{i}Whispers{/i}* Trust me. He'll lose focus in an instant."
scene ep10_sage_solo91 with dissolve
mc "Um... Cammy? What are you doing over there?"
scene anim_dots_ep10 with dissolve
cam "I'm struggling to keep my balance, [name]."
menu:
    "Enjoy it [m_c2][mod_choices[4]]":
        $ ep10_dots_attitude += 1
        mc "It doesn't feel like it's that, but all right. Hngn..."
    "Ask her to stop":
        mc "Well, can you try to keep your balance...uh...higher up?"
scene ep10_sage_solo92 with dissolve
$ renpy.pause()
play sound "sound_effects/shove.mp3"
scene ep10_sage_solo93 with vpunch
mc "Hngn... Hey!"
scene ep10_sage_solo94 with dissolve
sa "Yes! I win!"
scene ep10_sage_solo95 with dissolve
mc "I see that you found a way to cheat, after all."
cam "Hahaha!"
scene ep10_sage_solo96 with dissolve
sa "Whoops! Lost my balance."
mc "Mpfhhh!!!"
sa "Huh? What was that? I can't hear you."
scene ep10_sage_solo97 with dissolve
cam "Um... Sage?"
sa "Looks like we got him going there..."
scene ep10_sage_solo81 with dissolve
he "Are you guys done humping each other?"
scene ep10_sage_solo98 with dissolve
sa "Yeah, I believe we're done. Thanks for the game."
scene ep10_sage_solo99 with dissolve
mc "That was fun..."
scene ep10_sage_solo100 with dissolve
sa "Dots is not why I like tabletop games, but I had fun too. Feeling ok?"
scene ep10_sage_solo99 with dissolve
menu:
    "Got too excited by you two \n{size=-4}[m_c2][mod_choices[4]]":
        $ ep10_dots_attitude += 1
        mc "I got too excited by you two, but I'm feeling good. I think I was showing a bit of...you know?"
    "Embarrassed [m_c1][mod_choices[2]]":
        $ dk(-1)
        mc "I'm embarrassed that I was showing, but yeah."
scene ep10_sage_solo100 with dissolve
sa "It's not the first time you've been \"showing\" lately."
scene ep10_sage_solo99 with dissolve
mc "What do you mean?"
scene ep10_sage_solo101 with dissolve
sa "I was alluding to those posters on campus."
scene ep10_sage_solo99 with dissolve
mc "Oh, yeah."
scene ep10_sage_solo101 with dissolve
sa "So... Any luck with finding out who's posting them?"
scene ep10_sage_solo102 with dissolve
mc "Nope. No one's admitting they know anything."
scene ep10_sage_solo101 with dissolve
sa "How are you managing it?"
scene ep10_sage_solo102 with dissolve
mc "I'm doing ok. The others are doing worse than me."
mc "What about you? How do you feel?"
scene ep10_sage_solo101 with dissolve
sa "To see your cock plastered all over campus?"
scene ep10_sage_solo102 with dissolve
mc "Yeah. Does it bother you?"
scene ep10_sage_solo103 with dissolve
sa "I don't think too much about it. Sure, many know it's you, but there were already rumors floating about you."
if ep7_ruined_presentation:
    sa "Plus, it already made an appearance on my brother's slideshow in an auditorium full of students."
    sa "I guess you can say I've gotten used to seeing it in public."
scene ep10_sage_solo102 with dissolve
mc "If it could all go away, I'd be happy. But it seems pointless to fight it."
scene ep10_sage_solo104 with dissolve
sa "As a guy with a big dick, I'm guessing it's not the worst thing that could happen to you."
sa "I'm lucky I've reeled you in, huh?"
scene ep10_sage_solo105 with dissolve
mc "Haha, reeled me in? We're dating. You'll have to keep reeling."
scene ep10_sage_solo101 with dissolve
sa "Do you wanna get it over and done with?"
scene ep10_sage_solo102 with dissolve
mc "The date?"
scene ep10_sage_solo101 with dissolve
sa "Yeah. It feels like the longer we wait, the bigger the expectations become."
sa "And I talked to Cammy and Heather about this before. I wouldn't know what to do if I had to plan it for us."
scene ep10_sage_solo102 with dissolve
mc "How about we keep it classic, just like that Dots game?"
scene ep10_sage_solo103 with dissolve
sa "Classic is boring, isn't it?"
scene ep10_sage_solo102 with dissolve
mc "We had fun playing Dots. We could have fun on a classic date, too."
scene ep10_sage_solo101 with dissolve
sa "What's classic to you?"
scene ep10_sage_solo105 with dissolve
mc "A dinner and a movie, maybe?"
scene ep10_sage_solo104 with dissolve
sa "That could work. When do you wanna do it?"
scene ep10_sage_solo105 with dissolve
mc "I need to check my calendar, but definitely soon. If you're available, that is."
scene ep10_sage_solo104 with dissolve
sa "I'll make time for it."
stop music fadeout 3
scene ep10_sage_solo106 with dissolve
$ renpy.pause()
$ new_bio("Sage", "Sage told me about her youth and past hobbies, and we decided to go out on our first official date.")
$ new_bio("Camila", "Camila helped me and Sage talk about dating. And while playing Dots together, Sage used her to cheat in an arousing way.")



if branchAlone and ep9_riona_choice == "DIK":
    jump ep10_rio_solo_label    

if ep10_dating_nora:
    jump ep10_nora_date_label
    

    
if branchIsabella:
    jump ep10_bella_solo_label

if ep10_date_nicole and not ep10_cancel_date_nicole:
    jump ep10_nicole_date_label




jump ep10_science_label

label ep10_sage_date_label:
play music "music/ep10/date_night.mp3"
scene ep10_sage_date2 with dissolve
sa "How do I look?"
scene ep10_sage_date6 with dissolve
qu "Dolled up."
scene ep10_sage_date5 with dissolve
sa "Is that bad?"
scene ep10_sage_date6 with dissolve
qu "It depends on who you ask."
scene ep10_sage_date11 with dissolve
ly "You look like a million bucks. So gorgeous!"
scene ep10_sage_date3 with dissolve
sa "Is it not too much?"
scene ep10_sage_date6 with dissolve
qu "It depends on where you're going."
scene ep10_sage_date10 with dissolve
ly "She's obviously going out on a date."
scene ep10_sage_date7 with dissolve
qu "Then it depends on who you're going with."
scene ep10_sage_date5 with dissolve
sa "I'm going out with [name]."
if ep8_quinn_lewd:
    scene ep10_sage_date8 with dissolve
    qu "..."
scene ep10_sage_date9 with dissolve
qu "Then it's way too much."
scene ep10_sage_date10 with dissolve
ly "Haha, it's not too much at all."
scene ep10_sage_date12 with dissolve
ly "Although..."
scene ep10_sage_date3 with dissolve
sa "Although, what?"
scene ep10_sage_date13 with dissolve
ly "You're rocking a sexy cleavage. That necklace detracts from it, don't you think?"
scene ep10_sage_date3 with dissolve
sa "It's the necklace I bought for these earrings."
scene ep10_sage_date11 with dissolve
ly "Personally, I'd wear a choker necklace or nothing at all."
scene ep10_sage_date4 with dissolve
sa "Nothing at all? Do you think it's better without it?"
scene ep10_sage_date14 with dissolve
ly "Your cleavage is your accessory, babe. Trust me on this."
scene ep10_sage_date15 with dissolve
ly "See! Even more stunning."
scene ep10_sage_date16 with dissolve
sa "Thank you, Lily."
sa "Ok. I'm ready."
scene ep10_sage_date9 with dissolve
qu "Or, you go back in there and slap on a T-shirt and sweatpants to match his standards."
scene ep10_sage_date10 with dissolve
ly "Don't make her second-guess her outfit."
scene ep10_sage_date9 with dissolve
qu "Then she shouldn't have asked me for advice."
scene ep10_sage_date17 with dissolve
ly "Off you go. Shoo!"

scene ep10_sage_date18 with dissolve
ly "Are you nervous?"
scene ep10_sage_date20 with dissolve
sa "Yes, and I don't know why."
sa "I've already done so much with [name] that this should feel completely normal."
sa "But because it's our \"first date\", it feels weird somehow."
scene ep10_sage_date19 with dissolve
ly "It sounds like someone caught feelings."
scene ep10_sage_date20 with dissolve
sa "No, it's not that. Uh..."
sa "Aren't the earrings too much for dinner and a movie?"
scene ep10_sage_date19 with dissolve
ly "Nope. There's nothing wrong with looking pretty for a night out."
scene ep10_sage_date21 with dissolve
play sound "sound_effects/message.mp3"
$ tmpInt = 0
$ tmpInt2 = 0
$ text_message_screen_list = []
$ text_message_screen_list.append(["%s" % name,"I'm outside. mphone_emoji_smile",False])
$ mphone_scene_to_chat("Sage",text_message_screen_list)
"*{i}Phone message{/i}*"
scene ep10_sage_date20 with dissolve
sa "Ok, that's him. I gotta leave."
scene ep10_sage_date19 with dissolve
ly "Enjoy yourself. And don't forget..."
ly "If you're looking to smash, order something light for dinner and avoid fizzy drinks."

scene bg anim_sage_pan_ep10 movie with dissolve
pause
$ guideSuggestedPage = 133
scene ep10_sage_date22 with dissolve

if persistent.mod_wt_enabled: 
                    $mod_choices = ["(-Sage)","(+Josy)","(-DIK)","(+DIK)","(-Maya)","(-Josy)","","","","","","" ]
                    #[m_c1][mod_choices[0]]

menu:
    "I underdressed [m_c1][mod_choices[0]]":
        $ RPsage -= 1
        mc "Oh, I think I underdressed."
        scene ep10_sage_date23 with dissolve
        sa "Dammit. I knew it was too much."
        scene ep10_sage_date24 with dissolve
        mc "No, no. It's not. You're so...so..."
        scene ep10_sage_date23 with dissolve
        sa "What's the adjective?"
        scene ep10_sage_date22 with dissolve
        mc "Beautiful."
    "Wow, look at you":
        mc "Wow, look at you."
        scene ep10_sage_date23 with dissolve
        sa "It's not too much, is it?"
        scene ep10_sage_date22 with dissolve
        mc "Not at all. You look beautiful."

if ep8_mansion_won:
    if affinity == "DIK":
        scene ep10_sage_date26 with dissolve
        mc "Get in."
    else:
        play sound "sound_effects/season3/car_door.mp3"
        scene ep10_sage_date25 with dissolve
        $ renpy.pause()
else:
    scene ep10_sage_date27 with dissolve
    mc "After you."
    scene ep10_sage_date28 with dissolve
    sa "Where am I going?"
    scene ep10_sage_date27 with dissolve
    mc "We'll have to take the bus."
    scene ep10_sage_date33 with wipeleft
    jump ep10_sage_date2_label

scene ep10_sage_date29 with dissolve
sa "Did Rusty let you borrow his ride?"
scene ep10_sage_date30 with dissolve
mc "Yeah, he said I can borrow it whenever I want. But I've been saving it for special moments like tonight."
scene ep10_sage_date29 with dissolve
sa "It beats taking the bus."
scene ep10_sage_date30 with dissolve
mc "Yeah, could you imagine? Looking pretty like that and taking the bus, I'd be embarrassed."
scene ep10_sage_date31 with dissolve
$ renpy.pause()
scene ep10_sage_date33 with wiperight

label ep10_sage_date2_label:
$ renpy.pause(2)
scene ep10_sage_date32 with dissolve
$ renpy.pause()
scene ep10_sage_date34 with dissolve
$ renpy.pause()
scene ep10_sage_date35 with dissolve
mc "..."
scene ep10_sage_date36 with dissolve
sa "..."
scene ep10_sage_date37 with dissolve
mc "So... Um..."
mc "Wanna talk about why this feels weird or should we pretend it's not?"
scene ep10_sage_date38 with dissolve
sa "*{i}Exhales{/i}* Thank you! It does feel weird, doesn't it?"
sa "And I've been nervous all day. Me! Nervous! Hah!"
scene ep10_sage_date39 with dissolve
mc "Why do you think that is?"
scene ep10_sage_date40 with dissolve
sa "I've got no fucking clue."
sa "We've spent time together and had sex before this. It shouldn't feel weird."
scene ep10_sage_date41 with dissolve
sa "I mean, I let you fuck my ass last time, and {b}this{/b} is what feels weird?"
if ep7_accept_madame:
    scene ep10_sage_date42 with dissolve
else:
    scene ep10_sage_date42b with dissolve
wa "Um... Can I start you off with some drinks?"
if ep7_accept_madame:
    scene ep10_sage_date43 with dissolve
else:
    scene ep10_sage_date43b with dissolve
mc "Uh... Yes! I'll have a cola."
scene ep10_sage_date44 with dissolve
sa "Same... Thank you."
scene ep10_sage_date45 with dissolve
sa "Wait! No fizzy drinks. I want water."
scene ep10_sage_date46 with dissolve
sa "Do you think he heard me?"
scene ep10_sage_date47 with dissolve

if persistent.mod_wt_enabled: 
                    $mod_choices = ["(-Sage)","(+Josy)","(-DIK)","(+DIK)","(-Maya)","(-Josy)","","","","","","" ]
                    #[m_c1][mod_choices[0]]

menu:
    "Everyone heard you [m_c1][mod_choices[3]]":
        $ dk(1)
        mc "Yeah, I think everyone heard you."
    "Which part of it? [m_c1][mod_choices[3]]":
        $ dk(1)
        mc "Which part of it? About the butt sex or the cola?"
    "I think so":
        mc "I think so."
scene ep10_sage_date48 with dissolve
sa "Ugh... I'm embarrassing us, aren't I?"
scene ep10_sage_date49 with dissolve
menu:
    "You need to relax [m_c1][mod_choices[2]]":
        $ dk(-1)
        mc "I think you need to relax. Take a deep breath and maybe avoid talking about anal sex while we're here."
        scene ep10_sage_date50 with dissolve
        sa "I'm so sorry. Aren't you nervous too?"
    "Yes, but it's funny [m_c1][mod_choices[3]]":
        $ dk(1)
        mc "Haha, yes. But I find it funny. You're usually calm and collected. I haven't seen this side of you before."
        scene ep10_sage_date50 with dissolve
        sa "Ugh... Aren't you nervous too?"
scene ep10_sage_date51 with dissolve
mc "No, I'm not nervous, but it feels different than usual."
$ guideSuggestedPage = 134
scene ep10_sage_date50 with dissolve
sa "It's because it's a big step, dude. Normally, you date someone and later find out if the guy is someone you want around."
sa "But now, it's like I've got that figured out already and am sealing the deal with the date."
scene ep10_sage_date51 with dissolve
menu:
    "The date isn't sealing any deals":
        mc "Oh, maybe that's why you're nervous? I don't look at it like that at all."
        scene ep10_sage_date50 with dissolve
        sa "You don't?"
        scene ep10_sage_date51 with dissolve
        mc "No. It's a new thing for us, but it's not sealing any deals."
        mc "I see it as us figuring each other out more. Digging deeper and seeing if we've had it right from the start or not."
        mc "I think I already know a great deal about you, but I want to learn more."
    "Not the biggest step we took":
        mc "Oh, maybe that's why you're nervous? I don't look at it like that at all."
        scene ep10_sage_date50 with dissolve
        sa "You don't?"
        scene ep10_sage_date51 with dissolve
        mc "No. It's a new thing for us, but we've taken way bigger steps together before."
        mc "I mean, we've had a lot of sex, we've kissed in public, we've spent many nights together..."
        mc "If you think about it, having dinner and watching a movie together is nothing compared to what we've already done."
mc "Don't put too much pressure on yourself tonight. That's all I'm asking."
scene ep10_sage_date52 with dissolve
sa "Ok, that's a big relief. *{i}Phew{/i}*"
sa "You know, I canceled the cola because Lily told me you shouldn't fuck when you've been drinking fizzy drinks. Haha!"
scene ep10_sage_date53 with dissolve
wa "Your...water."
scene ep10_sage_date54 with dissolve
$ renpy.pause()
scene ep10_sage_date55 with dissolve
sa "I'll never return to this place again..."
scene ep10_sage_date56 with dissolve
mc "Haha, if you think that's bad, you should take a glance behind you. But be sneaky about it..."
scene ep10_sage_date57 with dissolve
sa "Huh? What am I looking at?"
mc "See that guy there?"
sa "Yeah, what about him?"
scene ep10_sage_date58 with dissolve
mc "Well, he didn't show up alone. And now his date isn't there."
sa "What's weird about that?"
mc "Check under the table."
scene ep10_sage_date59 with dissolve
sa "Oh my God!"
mc "Haha! Right?"
scene ep10_sage_date60 with dissolve
sa "No way she is doing that!"
scene ep10_sage_date61 with dissolve
mc "At least the waiter hasn't caught her yet. But we did."
scene ep10_sage_date62 with dissolve
$ renpy.pause()

scene ep10_sage_date63 with wiperight
mc "You mentioned you made a lot of friends playing tabletop games."
mc "Are any of those friends still around?"
scene ep10_sage_date65 with dissolve
sa "Many moved away, but some are. None of them go to B&R."
sa "Well, Lizzy did, but she graduated."
sa "I occasionally meet up with a few of them for game nights, but it's been a while since the last time."
scene ep10_sage_date64 with dissolve
sa "That's one thing I hate about growing up, by the way."
sa "How it's harder to make time for your friends. It's a real struggle to do something you did daily or weekly back when you were young."
scene ep10_sage_date63 with dissolve
mc "It's not easy when people move away."
scene ep10_sage_date64 with dissolve
sa "Even if they're still in town, it gets hard. We all make new friends, and our time and attention get divided even further."
sa "And who's to say what happens after college? Maybe I even won't stay in touch with my HOT sisters."
sa "That would suck so bad, but I've seen it happen with the HOTs who've graduated before me. Some are practically ghosts today."
scene ep10_sage_date63 with dissolve
mc "I don't think there's much you can do about it. People are shaping their lives after their dreams, education and jobs, and they just end up somewhere."
scene ep10_sage_date66 with dissolve
sa "I'll tell you what you can do about it. You can grab hold of people you want in your life and let them know."
scene ep10_sage_date67 with dissolve
mc "Physically or...?"
scene ep10_sage_date68 with dissolve
sa "Haha, no. Like, you fight for them to make you a part of their future."
sa "If there's a friend you don't want to lose, let them know."
scene ep10_sage_date69 with dissolve
mc "Who are you doing it with? Who's your best friend?"
scene ep10_sage_date66 with dissolve
sa "Lizzy was my best friend when we were young, but we're not that close anymore."
sa "These days... I have a lot of friends - some closer than others - but I don't think I have a best friend."
scene ep10_sage_date67 with dissolve
mc "So, you're not planning to grab hold of anyone after college, then?"
scene ep10_sage_date70 with dissolve
sa "I don't have a clear picture, when I think about my future after next semester."
sa "It's scary and exciting at the same time. I feel like I could move anywhere in the world and create something of my own."
scene ep10_sage_date66 with dissolve
sa "But I don't like the idea of starting over completely. That's what scares me."
sa "And at the same time, if I got too close to someone now, maybe I'd feel like I couldn't move away and do those things... And that's scary too."
sa "Do you ever think about that?"
scene ep10_sage_date69 with dissolve
mc "I try not to. I feel like I just got here and will be here for quite some time."
mc "For me, the scary part is not knowing what I want to do after college."
mc "I figured signing up for engineering would give me a broad enough education to figure it out."
scene ep10_sage_date70 with dissolve
sa "So, you're doing your master's degree here?"
scene ep10_sage_date67 with dissolve
mc "Maybe, or I'll just stick with the bachelor's degree."
scene ep10_sage_date66 with dissolve
sa "Then you won't be an engineer."
scene ep10_sage_date67 with dissolve
mc "It's just a title."
scene ep10_sage_date70 with dissolve
sa "True, but those titles make a difference in the real world. You can negotiate way higher salaries with them."
sa "I have a Ph.D. friend who got a 25%% extra starting wage because of her title. She didn't even have any work experience in that field."
scene ep10_sage_date67 with dissolve
mc "She probably has to make up for the years of not getting paid while studying for it."
scene ep10_sage_date66 with dissolve
sa "Yeah, of course, but that wage scales in time if you're negotiating correctly."
scene ep10_sage_date71 with dissolve
sa "Sorry, I shouldn't talk about business on our date."
scene ep10_sage_date67 with dissolve
mc "I don't mind. I think it's attractive that you're passionate about things."
scene ep10_sage_date71 with dissolve
sa "You do?"
scene ep10_sage_date69 with dissolve
if affinity == "DIK":
    mc "Yeah. I don't think it's that common with girls."
    scene ep10_sage_date66 with dissolve
    sa "To be passionate? Are you mental? Because you're not saying that guys are more passionate, are you?"
    scene ep10_sage_date67 with dissolve
    mc "Not romantically passionate, but with hobbies, yeah. I think, in general, guys are way more passionate than girls and that some girls blend into each other."
    scene ep10_sage_date71 with dissolve
    sa "Ok, you have to explain yourself now. I've learned enough from my Mom to know that this topic would trigger a lengthy discussion."
    scene ep10_sage_date72 with dissolve
    mc "Oh, believe me. I would have liked to discuss this in her class, but I didn't get the chance to."
    scene ep10_sage_date73 with dissolve
    sa "So, how do girls blend into each other?"
    scene ep10_sage_date72 with dissolve
    mc "You don't have to look far to see it. You'd see it everywhere if you browse girls' profiles on Swyper or Rooster."
    mc "Under hobbies, they list the same things. Working out, listening to music, partying and being with friends and family."
    scene ep10_sage_date73 with dissolve
    sa "I would list those things, too. What's your point?"
    scene ep10_sage_date74 with dissolve
    mc "Those are things that most people enjoy doing, barring gender. And that's what I mean when I say that they blend into each other."
    mc "It's rare to find a girl who lists something different, like archery or mountain climbing."
    mc "And it's not that I find girls boring because they don't, but I find girls like you extra attractive."
    scene ep10_sage_date75 with dissolve
    sa "Because I like to yap about school and work?"
    scene ep10_sage_date76 with dissolve
    mc "No, because you're passionate about something and it shows. It makes you unique and interesting."
    scene ep10_sage_date75 with dissolve
    sa "I'm unsure if I should feel flattered or insulted on behalf of all the girls you think are all alike."
    scene ep10_sage_date77 with dissolve
    mc "*{i}Sigh{/i}* It wasn't an insult. You can be passionate about those other things too... I probably didn't explain it well enough."
    scene ep10_sage_date78 with dissolve
    sa "Haha! I see your point, and I don't agree with everything you said. But you're avoiding the safe topics, and I like that a lot."
    sa "Mom would eat you alive in this conversation."
    scene ep10_sage_date79 with dissolve
    if ep4_fuckedJade:
        mc "(In more ways than one.)"
    else:
        mc "Haha, I bet she would."
else:
    mc "Yeah. I like that you have goals and motivations in life."
    scene ep10_sage_date67 with dissolve
    mc "You're smart, determined and feel hungry to learn and grow as a person."
    mc "Sometimes I feel like I'm dating out of my league."
    scene ep10_sage_date73 with dissolve
    sa "Do you think I'm out of your league?"
    scene ep10_sage_date69 with dissolve
    mc "It's been pointed out to me that you are. I didn't think so at first, but the more I reflect on it... I believe others might be right about it."
    mc "I mean, I'm a freshman who was a nobody when I came here and you're a senior sorority president."
    scene ep10_sage_date67 with dissolve
    mc "You're smart in a field I know nothing about and you're on your way to make plans for a future that seemingly can be anything you want."
    mc "Whereas I know nothing about my future and dread to plan it..."
    mc "When I think about you like that, you feel out of my league. It's intimidating but also so damned attractive."

    scene ep10_sage_date70 with dissolve
    sa "Those are some high thoughts you have about me..."
    sa "And you're not out of my league. That's stupid. Don't sell yourself short like that."
    scene ep10_sage_date71 with dissolve
    sa "Because I look at you and I see things I want to be too. And you're younger than me and have already accomplished some of those things."
    sa "And that's something I find attractive about you."
    scene ep10_sage_date74 with dissolve
    mc "Thanks..."
    scene ep10_sage_date75 with dissolve
    sa "I told you I like when you're confident, but I also like that you allow yourself to feel insecure and vulnerable."
    scene ep10_sage_date76 with dissolve
    mc "Yeah, well, I'm only human..."

scene ep10_sage_date78 with dissolve
sa "Shall we leave for the movies?"
scene ep10_sage_date79 with dissolve
mc "Yeah, let's."

scene ep10_sage_date0 with fade
$ renpy.pause()
scene ep10_sage_date1 with dissolve
$ renpy.pause()
scene ep10_sage_date81 with dissolve
$ renpy.pause()
scene ep10_sage_date80 with dissolve
$ renpy.pause()
scene ep10_sage_date82 with dissolve
sa "Why do people watch movies on dates?"
sa "Why spend the time being silent next to someone you wanna bang?"
scene ep10_sage_date83 with dissolve
mc "Haha. That's a good question."
mc "Maybe they want to see the movie and be on a date too? Even if the date sucks, they still get a movie out of it."
scene ep10_sage_date82 with dissolve
sa "To me, a movie is something you watch with your friends when you don't feel like talking or doing something else."
scene ep10_sage_date83 with dissolve
mc "I only suggested it because I struggled to come up with something better."
scene ep10_sage_date84 with dissolve
sa "Oh, it's fine."
scene ep10_sage_date83 with dissolve
mc "I'm having a great time."
scene ep10_sage_date84 with dissolve
sa "To be clear, I didn't say it sucks being here with you. I was just thinking about the stupid things people do on dates."
scene ep10_sage_date83 with dissolve
mc "Honestly, I'd much rather spend the night talking with you than watching a movie."
mc "But at least I get to sit close to you."
if ep9_sage_vanilla:
    scene ep10_sage_date85 with dissolve
    $ renpy.pause()
    scene ep10_sage_date86 with dissolve
    $ renpy.pause()
scene ep10_sage_date87 with dissolve
mc "When did this night stop feeling weird to you?"
scene ep10_sage_date88 with dissolve
sa "I think it was when we started talking like we always do. It made me feel comfortable again."
sa "It still feels different than usual but in a good way."
scene ep10_sage_date87 with dissolve
mc "Good."
scene ep10_sage_date88 with dissolve
sa "I'm happy we did this."
scene ep10_sage_date87 with dissolve
mc "Me too. I've felt comfortable around you too."
scene ep10_sage_date89 with dissolve
sa "You're not scared of me now, are you?"
scene ep10_sage_date87 with dissolve
mc "Haha, no."
scene ep10_sage_date89 with dissolve
sa "I take it you're not holding back on any questions you're scared to ask me."
scene ep10_sage_date87 with dissolve
mc "Not tonight."
scene ep10_sage_date88 with dissolve
sa "Good... You feel relaxed. I like that."
scene ep10_sage_date90 with dissolve
$ renpy.pause()
scene ep10_sage_date91 with dissolve
sa "*{i}Smack{/i}*"
scene ep10_sage_date92 with dissolve
$ renpy.pause()
scene ep10_sage_date87 with dissolve
mc "Do you want some of my popcorn?"
scene ep10_sage_date93 with dissolve
sa "No, thanks. I've got my soda."
scene ep10_sage_date95 with dissolve
mc "I thought you weren't having any tonight."
scene ep10_sage_date93 with dissolve
sa "I wasn't. But since we were doing the whole classic date and all, I figured I wouldn't sleep with you tonight."
scene ep10_sage_date94 with dissolve
mc "I'm missing out on sex because of the date, huh?"
scene ep10_sage_date95 with dissolve
mc "It's ok with me. I wanted to go out on a date with you. It wasn't for sex to begin with."
scene ep10_sage_date93 with dissolve
sa "Yes, that's what I realized. And I'm fine with it."
scene ep10_sage_date96 with dissolve
sa "Although..."
scene ep10_sage_date95 with dissolve
mc "Although, what?"
if not ep9_sage_vanilla:
    label ep10_sage_lewd_label:
    if _in_replay:
        if persistent.name == None:
            $ name = "MC"
        else:
            $ name = persistent.name
        if persistent.mc_sage == None:
            $ mc_sage = name
        else:
            $ mc_sage = persistent.mc_sage
        if persistent.sage == None:
            $ sage = "Sage"
        else:
            $ sage = persistent.sage
        $ ep4_sageLikeDaringSex = True
        $ ep4_fuckedSage = True
        play music "music/ep10/date_night.mp3"
    hide screen new_phone_screen
    scene ep10_sage_lewd1 with dissolve
    sa "I've thought of ways to surprise you."
    scene ep10_sage_lewd2 with dissolve
    mc "Surprise me with what?"
    scene ep10_sage_lewd1 with dissolve
    sa "There's this thing I realized I'd like to try tonight...but I don't want to ruin our date with it."
    scene ep10_sage_lewd2 with dissolve
    menu:
        "Save it for another time" if not _in_replay:
            show screen new_phone_screen
            mc "If it's about sex, I'd rather keep the date as it is."
            scene ep10_sage_lewd3 with dissolve
            sa "Yes, you're right. My mind wandered, that's all."
            jump ep10_sage_date3_label
        "[mod_gr]You wouldn't ruin the date":
            $ ep10_sage_lewd = True
            mc "You wouldn't ruin the date. As far as I'm concerned, this date was a success and I'm very happy with it."
            scene ep10_sage_lewd3 with dissolve
            sa "I am, too."
            scene ep10_sage_lewd4 with dissolve
            sa "Seeing what that girl did at the restaurant made me think of it..."
            mc "Is this the surprise?"
            scene ep10_sage_lewd5 with dissolve
            sa "Maybe you'll figure it out."
            scene ep10_sage_lewd6 with dissolve
            $ renpy.pause()
            play sound "sound_effects/zipper.mp3"
            scene ep10_sage_lewd7 with dissolve
            "*{i}Pants unzip{/i}*"
            scene anim_sage_bj1_ep10 with dissolve
            pause
            scene anim_sage_bj2_ep10 with dissolve
            sa "*{i}Suck suck{/i}*"
            mc "I can't believe you're doing that in here."
            sa "*{i}Suck suck{/i}* Mmm... Keep your eyes on what's happening around you and let me deal with this problem you're having."
            mc "You caused the problem."
            sa "*{i}Suck suck{/i}* I'll solve it too."
            pause
            scene anim_sage_bj3_ep10 with dissolve
            mc "I did not expect you to do this."
            if ep4_fuckedSage:
                if ep4_sageLikeDaringSex:
                    sa "*{i}Suck suck{/i}* I know you like this. You've told me you did. And you also told me I could surprise you."
                else:
                    sa "*{i}Suck suck{/i}* I know you're not a fan of public sex, but you told me I could surprise you."
            else:
                sa "*{i}Suck suck{/i}* You have yourself to blame. You told me I could surprise you."
            mc "Keep sucking... It's so good."
            pause
            scene anim_sage_bj4_ep10 with dissolve
            sa "*{i}Suck shlurp{/i}*"
            mc "(Her lips are so tight around my cock. She's sucking on it hard too.)"
            pause
            scene anim_sage_bj5_ep10 with dissolve
            mc "Sage... I'm gonna cum."
            pause
            scene anim_sage_bj_cum_ep10 with vpunch
            mc "Ahhh... Fuck..."
            pause
            scene ep10_sage_lewd8 with dissolve
            sa "*{i}Gulp{/i}*"
            scene ep10_sage_lewd9 with dissolve
            sa "*{i}Lick lick{/i}*"
            scene ep10_sage_lewd10 with dissolve
            $ renpy.pause()
            scene ep10_sage_lewd11 with dissolve
            mc "What was that?"
            scene ep10_sage_lewd13 with dissolve
            sa "Just something that will have you bragging to your brothers about."
            scene ep10_sage_lewd12 with dissolve
            mc "You're unbelievable."
            scene ep10_sage_lewd13 with dissolve
            sa "Yup."
            scene ep10_sage_lewd12 with dissolve
            $ renpy.pause()
            $ renpy.end_replay()
            show screen new_phone_screen
            $ persistent.ep10_lewd_sage = True
            $ calcScenes()
            $ mphone_stats_add_girl_s3("sage","Sage gave you a blowjob in the movie theater in episode 10.")
else:
    scene ep10_sage_date93 with dissolve
    sa "Never mind."
    label ep10_sage_date3_label:
    scene ep10_sage_date97 with dissolve
    $ renpy.pause()
    scene ep10_sage_date98 with dissolve
    $ renpy.pause()

scene ep10_sage_date99 with Fade(2,2,2)
$ renpy.pause()
scene ep10_sage_date100 with dissolve
sa "I guess here's where the night ends."
scene ep10_sage_date101 with dissolve
mc "Yeah. Back where it started."
scene ep10_sage_date100 with dissolve
sa "I had an awesome night with you. Thanks for everything."
scene ep10_sage_date101 with dissolve
mc "Me too."
scene ep10_sage_date102 with dissolve
sa "So... How do classic dates end these days?"
scene ep10_sage_date101 with dissolve
mc "In my mind, it would end with a kiss if it was good."
scene ep10_sage_date104 with dissolve
sa "*{i}Smack{/i}*"
scene ep10_sage_date105 with dissolve
sa "That's corny. But it was a great one."
scene ep10_sage_date102 with dissolve
sa "I guess you don't ask a guy to stay the night on a classic date."
if ep10_sage_lewd:
    scene ep10_sage_date101 with dissolve
    mc "Technically, you don't blow them in a movie theater, either."
    scene ep10_sage_date103 with dissolve
    sa "Hahaha!"
else:
    scene ep10_sage_date101 with dissolve
    mc "Yeah, I guess that's right."
scene ep10_sage_date100 with dissolve
sa "I'll see you tomorrow..."
stop music fadeout 5
scene ep10_sage_date106 with dissolve
$ renpy.pause()
scene ep10_sage_date106b with dissolve
$ renpy.pause()
$ mgallery_add_photo("ep10_sage_date_pic1")
$ mgallery_add_photo("ep10_sage_date_pic2")

if ep10_sage_lewd:
    $ new_bio("Sage", "Sage and I had a great classic date together. It started off weird, but as the night progressed, we found we were enjoying each other's company more than before. And, oh... She gave me a blowjob in the movie theater.")
else:
    $ new_bio("Sage", "Sage and I had a great classic date together. It started off weird, but as the night progressed, we found we were enjoying each other's company more than before.")
jump ep10_sb2_label

label ep10_bbq_sage_lewd_label:
if _in_replay:
    if persistent.name == None:
        $ name = "MC"
    else:
        $ name = persistent.name
    if persistent.mc_sage == None:
        $ mc_sage = name
    else:
        $ mc_sage = persistent.mc_sage
    if persistent.sage == None:
        $ sage = "Sage"
    else:
        $ sage = persistent.sage
    play music "music/ep8/licensed_music/track72.mp3"
hide screen new_phone_screen
scene ep10_bbq_sage_lewd1 with dissolve
mc "There you are. Are you leaving?"
scene ep10_bbq_sage_lewd2 with dissolve
sa "No, but I waved off some of the girls."
scene ep10_bbq_sage_lewd3 with dissolve
sa "*{i}Smack{/i}* Come here."
scene ep10_bbq_sage_lewd4 with dissolve
mc "Seems like you got in the mood..."
scene ep10_bbq_sage_lewd5 with dissolve
sa "I partly blame the alcohol... But also...you look fucking hot tonight."
scene ep10_bbq_sage_lewd4 with dissolve
mc "Is it the beard?"
scene ep10_bbq_sage_lewd5 with dissolve
sa "I think that might be it. You look dirty in it."
scene ep10_bbq_sage_lewd4 with dissolve
mc "Dirty? Yeah, I don't like it much either."
scene ep10_bbq_sage_lewd6 with dissolve
sa "Dirty, as in hot. Not as in filthy."
sa "Filthy can also be hot, but you get my drift."
scene ep10_bbq_sage_lewd7 with dissolve
mc "Oh, thanks! I still don't like it. It itches a lot."
mc "Would you cry a river if I shaved it off?"
scene ep10_bbq_sage_lewd6 with dissolve
sa "Hey, it's your body. Why did you even grow it in the first place?"
scene ep10_bbq_sage_lewd7 with dissolve
mc "No reason."
scene ep10_bbq_sage_lewd8 with dissolve
sa "You're lying to me. Why?"
scene ep10_bbq_sage_lewd7 with dissolve
mc "I guess I wanted to prove a point."
scene ep10_bbq_sage_lewd8 with dissolve
sa "And what point would a beard prove?"
scene ep10_bbq_sage_lewd7 with dissolve
mc "You know those posters of me...?"
scene ep10_bbq_sage_lewd9 with dissolve
sa "The no body hair comment? Aw, come on. Is that why?"
scene ep10_bbq_sage_lewd10 with dissolve
mc "I got self-conscious about it. It's not a big deal."
scene ep10_bbq_sage_lewd9 with dissolve
sa "Did you take that much offense from that comment?"
scene ep10_bbq_sage_lewd10 with dissolve
mc "Facial and body hair...those are some manly things. It seems like most guys my age have it."
mc "And I didn't start shaving until after puberty because not much is growing anywhere."
scene ep10_bbq_sage_lewd9 with dissolve
sa "You're right to have your feelings on this. I can't tell you not to be self-conscious about something, but let me tell you one thing..."
sa "I think many would kill to have a body like yours."
sa "You're hot and fit, and I don't even want to bring out measuring tape for that thing between your legs because it would scare me to find out how big it is."
scene ep10_bbq_sage_lewd12 with dissolve
sa "So, what? You're not growing body hair? Is that your flaw?"
sa "You don't have to shave your chest, back and armpits a lot. That's not a bad trade."
sa "And you're still young. I bet it will grow a lot in all kinds of places when you get older, and then you'll think about these days and miss how it used to be."
sa "That's what I think."
scene ep10_bbq_sage_lewd11 with dissolve
mc "Thanks. That makes me feel better..."
mc "Please, don't tell anyone about this."
scene ep10_bbq_sage_lewd13 with dissolve
sa "I would never do that to you."
scene ep10_bbq_sage_lewd12 with dissolve
sa "Damn... Now you've gone from hot to adorable."
sa "I don't think I can have sex with adorable."
scene ep10_bbq_sage_lewd11 with dissolve
mc "Sex? Out here?"
scene ep10_bbq_sage_lewd12 with dissolve
sa "I wanna stay with you tonight in your tent."
scene ep10_bbq_sage_lewd11 with dissolve
mc "You do? I thought you girls were mocking it."
scene ep10_bbq_sage_lewd12 with dissolve
sa "We were. But it's kind of like an adventure, and I wanna do that with you."
if ep10_sage_lewd:
    sa "I keep thinking about how hot it was to blow you in the movie theater. So, why not try banging in a tent? Am I right?"
    scene ep10_bbq_sage_lewd11 with dissolve
    mc "Yeah, but the tent is just a piece of fabric. People are gonna overhear us."
else:
    sa "You were so sweet during our date. And lately, I've felt extra horny around you."
    sa "So, if you want to...I figured we could bang in your tent. What do you say?"
    scene ep10_bbq_sage_lewd11 with dissolve
    mc "That sounds hot, but the tent is just a piece of fabric. People are gonna overhear us."
scene ep10_bbq_sage_lewd14 with dissolve
sa "Who will overhear us? Aside from some of your brothers, no one's left."
stop music fadeout 3
sa "The music is still loud... I say, let's go for it."
scene ep10_bbq_sage_lewd15 with wipeleft
play music "music/ep8/licensed_music/track74.mp3"
mc "This tent is pretty small."
scene ep10_bbq_sage_lewd16 with dissolve
sa "*{i}Smack{/i}* So, what? I want to be close to you."
scene ep10_bbq_sage_lewd17 with dissolve
mc "Yeah, but I thought it would be hard to fuck in here."
scene ep10_bbq_sage_lewd18 with dissolve
sa "There's nothing hard about it. Me on top. You on top. Who cares?"
sa "Put it in and gyrate your hips and we'll have a good time."
scene ep10_bbq_sage_lewd19 with dissolve
sa "I wanna put all of you inside of me until we're closer than we've ever been before."
label ep10_bbq_sage_lewd_loop_label:
menu:
    "69":
        scene ep10_bbq_sage_lewd20 with dissolve
        sa "I wanna taste you..."
        scene ep10_bbq_sage_lewd21 with dissolve
        $ renpy.pause()
        scene anim_sage_69_ep10 with dissolve
        sa "*{i}Suck suck{/i}*"
        pause
        scene anim_sage_69b_ep10 with dissolve
        mc "*{i}Lick lick{/i}*"
        pause
        jump ep10_bbq_sage_lewd_loop_label
    "Boobjob":
        scene ep10_bbq_sage_lewd22 with dissolve
        mc "Let me fuck your tits..."
        scene anim_sage_boobjob1_ep10 with dissolve
        mc "Your tits are the best..."
        sa "You love to use them, don't you?"
        pause
        scene anim_sage_boobjob2_ep10 with dissolve
        mc "Yeah, I fucking do..."
        sa "Use them, [mc_sage]. They're yours."
        pause
        jump ep10_bbq_sage_lewd_loop_label
    "Continue":
        scene ep10_bbq_sage_lewd23 with dissolve
        sa "I need you to fuck me, [mc_sage]."

$ tmpInt = 0
$ tmpBool3 = False
scene ep10_bbq_sage_lewd24 with dissolve
label ep10_bbq_sage_lewd_loop2_label:
menu:
    "Her on top":
        $ tmpInt += 1
        scene anim_sage_ride1_ep10 with dissolve
        sa "God... *{i}Moans{/i}*"
        sa "*{i}Smack{/i}* I fucking love to ride you."
        pause
        scene anim_sage_ride2_ep10 with dissolve
        mc "Ride me, [sage]."
        sa "Yeah? You want your slut to ride your cock?"
        mc "Yeah, ride it like that."
        pause
        jump ep10_bbq_sage_lewd_loop2_label
    "Missionary":
        $ tmpInt += 1
        scene ep10_bbq_sage_lewd25 with dissolve
        $ renpy.pause()
        scene ep10_bbq_sage_lewd26 with dissolve
        $ renpy.pause()
        scene ep10_bbq_sage_lewd27 with dissolve
        $ renpy.pause()
        scene anim_sage_miss1_ep10 with dissolve
        sa "*{i}Moans{/i}* Fuck, that feels good."
        mc "Yeah... Fucking in a tent works better than I thought it would."
        sa "I told you."
        pause
        scene anim_sage_miss2_ep10 with dissolve
        sa "You make me so wet."
        mc "Yeah, I can tell. When I'm sliding in and out of you, I feel my cock gets covered in it."
        sa "Mmm... Keep fucking me like that..."
        pause
        scene anim_sage_miss3_ep10 with dissolve
        sa "Give it to me, [mc_sage]..."
        mc "Yeah? Does my slut want it?"
        sa "Yes... Your fuck slut needs it bad."
        pause
        scene anim_sage_miss4_ep10 with dissolve
        sa "*{i}Moans{/i}* I love it when you go deep. No one can do it like you, [mc_sage]."
        pause
        jump ep10_bbq_sage_lewd_loop2_label
    "Doggystyle":
        $ tmpInt += 1
        scene ep10_bbq_sage_lewd28 with dissolve
        $ renpy.pause()
        scene anim_sage_doggy1_ep10 with dissolve
        sa "Yes! Fuck me, [mc_sage]! Fuck me hard!"
        pause
        menu:
            "Stick it in her ass":
                $ tmpBool3 = True
                scene ep10_bbq_sage_lewd29 with dissolve
                sa "*{i}Moans{/i}* Ahhh... Damn, I should have brought my toy for this."
                scene ep10_bbq_sage_lewd30 with dissolve
                mc "I'll make it work without it."
                scene ep10_bbq_sage_lewd31 with dissolve
                sa "Hngn... Fuck... That's so... Tight..."
                scene anim_sage_doggy1_anal_ep10 with dissolve
                mc "Yeah, fuck... I fucking love it."
                sa "Go easy on me, [mc_sage]."
                pause
                scene anim_sage_doggy2_anal_ep10 with dissolve
                sa "*{i}Moans{/i}* Oh, [mc_sage]... What are you doing to me?"
                pause
            "Stick to vaginal":
                $ tmpBool3 = False
                scene anim_sage_doggy2_ep10 with dissolve
                sa "*{i}Moans{/i}* That feels amazing... Harder!"
                pause
        jump ep10_bbq_sage_lewd_loop2_label
    "Cum" if tmpInt > 2:
        mc "[sage]... I'm getting close."
        menu:
            "Facial":
                scene anim_sage_cum1_ep10 with dissolve
                sa "Cum on my face, [mc_sage]. I want your cum..."
                pause
                scene ep10_bbq_sage_lewd32 at vpunch, cum2
                $ renpy.pause(0.5)
                scene ep10_bbq_sage_lewd32 at vpunch, cum2
                $ renpy.pause(0.5)
                scene ep10_bbq_sage_lewd32 at vpunch, cum2
                mc "Ahh..."
                scene ep10_bbq_sage_lewd33 with dissolve
                $ renpy.pause()
            "Creampie":
                scene anim_sage_miss2b_ep10 with dissolve
                sa "Get your release inside of me, [mc_sage]."
                sa "I want your cum to fill me up."
                scene ep10_bbq_sage_lewd34b at vpunch, cum1
                $ renpy.pause(0.5)
                scene ep10_bbq_sage_lewd34b at vpunch, cum1
                $ renpy.pause(0.5)
                scene ep10_bbq_sage_lewd34b at vpunch, cum1
                mc "Ahh..."
                scene ep10_bbq_sage_lewd34 with dissolve
                sa "That's so hot... I came when you did that."
            "On tits":
                scene anim_sage_boobjob1_ep10 with dissolve
                sa "Cum on my tits, [mc_sage]. I want it... I need it!"
                pause
                scene ep10_bbq_sage_lewd35 at vpunch, cum2
                $ renpy.pause(0.5)
                scene ep10_bbq_sage_lewd35 at vpunch, cum2
                $ renpy.pause(0.5)
                scene ep10_bbq_sage_lewd35 at vpunch, cum2
                mc "Ahh..."
                scene ep10_bbq_sage_lewd36 with dissolve
                sa "Mmm... There you go."
            "On ass":
                if tmpBool3:
                    scene anim_sage_doggy2_anal_ep10 with dissolve
                else:
                    scene anim_sage_doggy2_ep10 with dissolve
                mc "I wanna shoot it on your ass..."
                sa "Do it, [mc_sage]. Cover my slutty ass with your cum. Cum!!!"
                scene ep10_bbq_sage_lewd37 at vpunch, cum3
                $ renpy.pause(0.5)
                scene ep10_bbq_sage_lewd37 at vpunch, cum3
                $ renpy.pause(0.5)
                scene ep10_bbq_sage_lewd37 at vpunch, cum3
                mc "Ahh..."
                scene ep10_bbq_sage_lewd38 with dissolve
                mc "It's covered in it, alright."
                sa "Haha, yeah. I can definitely feel that."

scene ep10_bbq_sage_lewd39 with dissolve
mc "So, let's hear it. Why wasn't it 5 out of 5 this time?"
scene ep10_bbq_sage_lewd40 with dissolve
sa "Hahaha!"
scene ep10_bbq_sage_lewd42 with dissolve
sa "You were right about the beard being itchy. You scratched me a lot with it."
scene ep10_bbq_sage_lewd43 with dissolve
mc "Oh, I'm sorry."
scene ep10_bbq_sage_lewd42 with dissolve
sa "It's fine, I can take it. But it wasn't 5 out of 5 because of it."
scene ep10_bbq_sage_lewd39 with dissolve
mc "I'm not gonna bother to ask you to review me anymore. You're a tough critic."
scene ep10_bbq_sage_lewd40 with dissolve
sa "Haha, I just know what I want."
scene ep10_bbq_sage_lewd39 with dissolve
mc "Screw you, at least I had a 5 out of 5 time."
scene ep10_bbq_sage_lewd41 with dissolve
sa "Hahaha!"
scene ep10_bbq_sage_lewd40 with dissolve
sa "The night isn't over yet. And if this tent gets as cold as I think it will, I will use you again to raise the temperature."
stop music fadeout 3
scene ep10_bbq_sage_lewd44 with dissolve
sa "*{i}Smack{/i}*"
scene ep10_bbq_jm_end_event15 with dissolve
$ renpy.pause()

$ renpy.end_replay()
$ persistent.ep10_lewd_sage2 = True
$ calcScenes()
show screen new_phone_screen
$ new_bio("Sage", "Sage spent the night together with me in my tent. We had sex and shared an overall great night.")
$ mphone_stats_add_girl_s3("sage","You had sex with Sage in your tent after the DIKs' Thanksgiving party in episode 10.")
$ mgallery_add_photo("ep10_sage_bbq_pic")
play music "music/ep8/licensed_music/track72.mp3"


if wt_ep9_branch_numbers != 1:
    
            "End the night with?"
            if persistent.mod_wt_enabled: 
                    $mod_choices = ["(Bella scene)","(+Josy)","(-DIK)","(+DIK)","(+Derek)","(-Josy)","","","","","","" ]
                    #[m_c1][mod_choices[0]]
            menu:
                "Jill" if branchJill:
                    $ep10_wt_end_bbq="Jill"
                    jump ep10_bbq_jill_end_event_label
                "Josy & Maya" if branchMayaJosy:
                    $ep10_wt_end_bbq="Josy"
                    jump ep10_bbq_jm_end_event_label
                "Isabella" if branchIsabella:
                    $ep10_wt_end_bbq="Bella"
                    jump ep10_party_eval_label
                    
                "Sage" if branchSage:
                    $ep10_wt_end_bbq="Sage"
                    jump ep10_party_eval_label
                "Lily" if ep10_rolling:
                    $ep10_wt_end_bbq="Lily"
                    scene ep10_after_bbq1 with dissolve
                    ly "No way... Is this where you're sleeping?"
                    scene ep10_after_bbq3 with dissolve
                    mc "Since I put up the tent and all, I figured why not?"
                    mc "Wanna join?"
                    scene ep10_after_bbq2 with dissolve
                    ly "I don't think so. I can hear my bed calling my name from here."
                    scene ep10_after_bbq3 with dissolve
                    mc "I can't blame you. This night will get cold."
                    mc "But now that most seem to be leaving, I'm gonna turn in."
                    scene ep10_after_bbq4 with dissolve
                    ly "What the hell... Make some room for me."
                    scene ep10_after_bbq5 with dissolve
                    mc "For real?"
                    scene ep10_after_bbq6 with dissolve
                    ly "I don't want you to freeze to death."
                    scene ep10_after_bbq5 with dissolve
                    mc "Ah, so you're gonna keep me warm?"
                    scene ep10_after_bbq6 with dissolve
                    ly "Don't make me regret it."
                    scene ep10_after_bbq7 with dissolve
                    if ep9_spoon_lily:
                        mc "I thought the rules said no spooning."
                    else:
                        mc "So, the rules are ok with spooning?"
                    scene ep10_after_bbq8 with dissolve
                    ly "Only to assert dominance, remember?"
                    scene ep10_after_bbq7 with dissolve
                    mc "Dominance against what? A bear?"
                    scene ep10_after_bbq9 with dissolve
                    ly "Haha! Yes! If a bear shows up, he'll get scared shitless seeing us like this."
                    ly "Also, grope my tits or something and it won't feel like spooning."
                    scene ep10_after_bbq10 with dissolve
                    mc "Hahaha."
                    scene ep10_after_bbq9 with dissolve
                    ly "And wipe that smile off your face. I can feel it in the back of my skull."
                    scene ep10_after_bbq11 with dissolve
                    $ renpy.pause()
                    $ new_bio("Lily", "At the DIKs' Thanksgiving party, I ended the night in my tent together with Lily. It surprised me that she was cool with it, since it didn't feel like it was a part of our rolling deal.")
                    jump ep10_party_eval_label



jump ep10_party_eval_label
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
