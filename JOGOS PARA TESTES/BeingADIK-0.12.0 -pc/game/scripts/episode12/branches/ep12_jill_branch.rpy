label ep12_jill_break_label:
$ breakup.append("Jill")
play music "music/ep9/licensed_music/track128.mp3"
scene ep12_jill_break1 with dissolve
ji "[name]? I'm here."
scene ep12_jill_break2 with dissolve
mc "That was fast."
scene ep12_jill_break4 with dissolve
ji "I rushed back home. There was something in the sound of your voice that had me worried."
ji "Are you doing well? Is this about last night?"
scene ep12_jill_break3 with dissolve
mc "Yesterday was rough, but it's not about that... You should sit down."
scene ep12_jill_break5 with dissolve
$ renpy.pause()
scene ep12_jill_break7 with dissolve
ji "What's wrong?"
scene ep12_jill_break12 with dissolve
mc "How do I say this?"
mc "*{i}Sigh{/i}* I'm an asshole..."
scene ep12_jill_break6 with dissolve
mc "Remember Zoey?"
scene ep12_jill_break8 with dissolve
ji "Yes?"
scene ep12_jill_break6 with dissolve
mc "I'm still in love with her. And she loves me too."
scene ep12_jill_break9 with dissolve
$ renpy.pause()
scene ep12_jill_break10 with dissolve
ji "*{i}Scoffs{/i}*"
ji "I knew it."
scene ep12_jill_break11 with dissolve
mc "You knew it?"
scene ep12_jill_break13 with dissolve
ji "Damn you, [name]."
scene ep12_jill_break14 with dissolve
mc "Jill, don't leave. Can we talk about it?"
scene ep12_jill_break16 with dissolve
ji "What is there to say? It's over, isn't it?"
scene ep12_jill_break17 with dissolve
ji "All this time together... Every meaningful moment..."
ji "And you throw that away for what?"
scene ep12_jill_break14 with dissolve
mc "It wasn't easy. And you're right. The time I've spent with you has been so special to me..."
mc "...but I gotta listen to my heart."
scene ep12_jill_break18 with dissolve
ji "Yeah. Listen to your heart, [name]."
ji "Listen to your heart while you crush mine."
scene ep12_jill_break19 with dissolve
mc "Jill..."
ji "*{i}Sobs{/i}*"
scene ep12_jill_break20 with dissolve
ji "I can't breathe."
scene ep12_jill_break15 with dissolve
mc "I'm so sorry."
scene ep12_jill_break21 with dissolve
ji "You reassured me that nothing was going on between you two."
ji "I trusted you... Do you know how that makes me feel? To blindly trust you and have you betray that trust?"
scene ep12_jill_break14 with dissolve
mc "I didn't plan for it to happen. I didn't even know I felt that way about her."
mc "But then she told me how she felt about me, and I knew it by then... That I felt the same."
scene ep12_jill_break22 with dissolve
ji "Was it that easy for you? Really?"
ji "Wasn't I worth a moment of hesitation? No afterthought?"
scene ep12_jill_break14 with dissolve
mc "It doesn't mean that you mean nothing to me, Jill."
mc "It's love. There is no reasoning or logic when it comes to love."
scene ep12_jill_break22 with dissolve
ji "Oh, spare me the clichés."
scene ep12_jill_break23 with dissolve
$ renpy.pause()
stop music fadeout 3
scene ep12_jill_break24 with dissolve
$ renpy.pause()
$ new_bio("Jill", "I broke up with Jill to be with Zoey. Understandably, Jill didn't receive the news well.")

if branchMayaJosy:
    if branchZoey and not wt_ep11_zoey_kiss_others:
        jump ep12_jm_break_label
    else:
        jump ep12_jm_z_label

jump ep12_bd_label

label ep12_jill_room_label:
play music "music/ep11/licensed_music/track172.mp3"
if ep11_jill_style == 1:
    scene ep12_jill_room1a with dissolve
elif ep11_jill_style == 2:
    scene ep12_jill_room1b with dissolve
elif ep11_jill_style == 3:
    scene ep12_jill_room1c with dissolve
else:
    scene ep12_jill_room1 with dissolve
ji "[name]? I'm here."
scene ep12_jill_room2 with dissolve
mc "I was wondering when you'd show up."
if ep11_jill_style == 1:
    scene ep12_jill_room3a with dissolve
elif ep11_jill_style == 2:
    scene ep12_jill_room3b with dissolve
elif ep11_jill_style == 3:
    scene ep12_jill_room3c with dissolve
else:
    scene ep12_jill_room3 with dissolve
ji "I tried my best to hurry. You sounded somber in your voice."
ji "Are you doing well? Is this about last night?"
if ep11_jill_style == 1:
    scene ep12_jill_room4a with dissolve
elif ep11_jill_style == 2:
    scene ep12_jill_room4b with dissolve
elif ep11_jill_style == 3:
    scene ep12_jill_room4c with dissolve
else:
    scene ep12_jill_room4 with dissolve
mc "I didn't mean to worry you with my call. Yeah, yesterday did a number on me. I'm still reeling from it."
if ep11_jill_style == 1:
    scene ep12_jill_room5a with dissolve
elif ep11_jill_style == 2:
    scene ep12_jill_room5b with dissolve
elif ep11_jill_style == 3:
    scene ep12_jill_room5c with dissolve
else:
    scene ep12_jill_room5 with dissolve
ji "That's understandable. I'm also feeling quite low today."
if ep11_jill_style == 1:
    scene ep12_jill_room4a with dissolve
elif ep11_jill_style == 2:
    scene ep12_jill_room4b with dissolve
elif ep11_jill_style == 3:
    scene ep12_jill_room4c with dissolve
else:
    scene ep12_jill_room4 with dissolve
mc "Wanna talk about it?"
if ep11_jill_style == 1:
    scene ep12_jill_room5a with dissolve
elif ep11_jill_style == 2:
    scene ep12_jill_room5b with dissolve
elif ep11_jill_style == 3:
    scene ep12_jill_room5c with dissolve
else:
    scene ep12_jill_room5 with dissolve
ji "No... Not today."
$ guideSuggestedPage = 229
if ep11_jill_style > 0:
    if ep11_jill_style == 1:
        scene ep12_jill_room6a with dissolve
    elif ep11_jill_style == 2:
        scene ep12_jill_room6b with dissolve
    else:
        scene ep12_jill_room6c with dissolve
    mc "Hey... You're wearing the outfit I picked out for you."
    if ep11_jill_style == 1:
        scene ep12_jill_room7a with dissolve
    elif ep11_jill_style == 2:
        scene ep12_jill_room7b with dissolve
    else:
        scene ep12_jill_room7c with dissolve
    ji "I am. Do you still like it?"
    if ep11_jill_style == 1:
        scene ep12_jill_room6a with dissolve
    elif ep11_jill_style == 2:
        scene ep12_jill_room6b with dissolve
    else:
        scene ep12_jill_room6c with dissolve
    if persistent.mod_wtenabled: 
                        $mod_choices = ["(+5 Maya)","(-5 Maya)","(-DIK)","(+DIK)","(+5 Josy)","(-5 Josy)","","","","","","" ]
                        #[mod_gr][mod_choices[0]]
                        #\n{size=-4}[m_c1][mod_choices[1]][m_c2][mod_choices[4]]
    menu:
        "Warms my heart \n{size=-4}[m_c1][mod_choices[2]]":
            $ dk(-1)
            mc "It warms my heart to see you wear it."
        "You're hot":
            mc "You're so hot in it. It suits you perfectly."
    mc "Did you wear it all day?"
    if ep11_jill_style == 1:
        scene ep12_jill_room8a with dissolve
    elif ep11_jill_style == 2:
        scene ep12_jill_room8b with dissolve
    else:
        scene ep12_jill_room8c with dissolve
    ji "Mhm..."
    if ep11_jill_style == 1:
        scene ep12_jill_room6a with dissolve
    elif ep11_jill_style == 2:
        scene ep12_jill_room6b with dissolve
    else:
        scene ep12_jill_room6c with dissolve
    mc "That makes me very happy."
    if ep11_jill_style == 1:
        scene ep12_jill_room10a with dissolve
    elif ep11_jill_style == 2:
        scene ep12_jill_room10b with dissolve
    else:
        scene ep12_jill_room10c with dissolve
    ji "My parents weren't as thrilled about it."
    if ep11_jill_style == 1:
        scene ep12_jill_room11a with dissolve
    elif ep11_jill_style == 2:
        scene ep12_jill_room11b with dissolve
    else:
        scene ep12_jill_room11c with dissolve
    mc "Did you go to see them? What did they say?"
    if ep11_jill_style == 1:
        scene ep12_jill_room10a with dissolve
    elif ep11_jill_style == 2:
        scene ep12_jill_room10b with dissolve
    else:
        scene ep12_jill_room10c with dissolve
    ji "I don't want to get into it. The look on Mom's face when she saw what I was wearing underneath my coat was enough."
    if ep11_jill_style == 1:
        scene ep12_jill_room9a with dissolve
    elif ep11_jill_style == 2:
        scene ep12_jill_room9b with dissolve
    else:
        scene ep12_jill_room9c with dissolve
    mc "You look great, Jill."
    if ep11_jill_style == 1:
        scene ep12_jill_room8a with dissolve
    elif ep11_jill_style == 2:
        scene ep12_jill_room8b with dissolve
    else:
        scene ep12_jill_room8c with dissolve
    ji "Thank you, [name]."

scene ep12_jill_room12 with dissolve
mc "So... What's that?"
if ep11_jill_style == 1:
    scene ep12_jill_room7a with dissolve
elif ep11_jill_style == 2:
    scene ep12_jill_room7b with dissolve
elif ep11_jill_style == 3:
    scene ep12_jill_room7c with dissolve
else:
    scene ep12_jill_room7 with dissolve
ji "It's the second part of your gift, and that's why it took me a while to get here."
ji "I picked it up today, and that's why it was a secret."
if ep11_jill_style == 1:
    scene ep12_jill_room6a with dissolve
elif ep11_jill_style == 2:
    scene ep12_jill_room6b with dissolve
elif ep11_jill_style == 3:
    scene ep12_jill_room6c with dissolve
else:
    scene ep12_jill_room6 with dissolve
mc "That's a big gift... Can I open it?"
if ep11_jill_style == 1:
    scene ep12_jill_room7a with dissolve
elif ep11_jill_style == 2:
    scene ep12_jill_room7b with dissolve
elif ep11_jill_style == 3:
    scene ep12_jill_room7c with dissolve
else:
    scene ep12_jill_room7 with dissolve
ji "You may."
play sound "sound_effects/season3/latch.mp3"
if ep11_jill_style == 1:
    scene ep12_jill_room13a with dissolve
elif ep11_jill_style == 2:
    scene ep12_jill_room13b with dissolve
elif ep11_jill_style == 3:
    scene ep12_jill_room13c with dissolve
else:
    scene ep12_jill_room13 with dissolve
$ renpy.pause()

scene ep12_jill_room14 with dissolve
mc "This is Lana's guitar."
mc "Are you for real?"
if ep11_jill_style == 1:
    scene ep12_jill_room15a with dissolve
elif ep11_jill_style == 2:
    scene ep12_jill_room15b with dissolve
elif ep11_jill_style == 3:
    scene ep12_jill_room15c with dissolve
else:
    scene ep12_jill_room15 with dissolve
ji "It was her guitar. And now it's yours."
ji "The purpose of that guitar is to create music. Like the poster, you'd put the guitar to a much better use."
ji "Hold on, I left something out here, too."
if ep11_jill_style == 1:
    scene ep12_jill_room16a with dissolve
elif ep11_jill_style == 2:
    scene ep12_jill_room16b with dissolve
elif ep11_jill_style == 3:
    scene ep12_jill_room16c with dissolve
else:
    scene ep12_jill_room16 with dissolve
mc "The speaker too... Jill... This is too much. What an incredible gift."
if ep11_jill_style == 1:
    scene ep12_jill_room17a with dissolve
elif ep11_jill_style == 2:
    scene ep12_jill_room17b with dissolve
elif ep11_jill_style == 3:
    scene ep12_jill_room17c with dissolve
else:
    scene ep12_jill_room17 with dissolve
ji "It's not going to sound much without it. Haha!"
scene ep12_jill_room18 with dissolve
mc "How did you convince your parents to part with this?"
mc "You told me Lana's room was treated as a sanctuary."
if ep11_jill_style == 1:
    scene ep12_jill_room19a with dissolve
elif ep11_jill_style == 2:
    scene ep12_jill_room19b with dissolve
elif ep11_jill_style == 3:
    scene ep12_jill_room19c with dissolve
else:
    scene ep12_jill_room19 with dissolve
ji "I had a long talk with them and explained how I felt."
ji "They always promised me that I could have some of her belongings when and if I wanted."
if ep11_jill_style == 1:
    scene ep12_jill_room20a with dissolve
elif ep11_jill_style == 2:
    scene ep12_jill_room20b with dissolve
elif ep11_jill_style == 3:
    scene ep12_jill_room20c with dissolve
else:
    scene ep12_jill_room20 with dissolve
ji "I told them I wanted to give you these things as a gift to show you how much you mean to me."
ji "Eventually, they agreed. But they asked me not to give away more of her things in return."
if ep11_jill_style == 1:
    scene ep12_jill_room21a with dissolve
elif ep11_jill_style == 2:
    scene ep12_jill_room21b with dissolve
elif ep11_jill_style == 3:
    scene ep12_jill_room21c with dissolve
else:
    scene ep12_jill_room21 with dissolve
mc "I can't accept this. It's too much."
if ep11_jill_style == 1:
    scene ep12_jill_room20a with dissolve
elif ep11_jill_style == 2:
    scene ep12_jill_room20b with dissolve
elif ep11_jill_style == 3:
    scene ep12_jill_room20c with dissolve
else:
    scene ep12_jill_room20 with dissolve
ji "I want you to have it."

if ep11_jill_style == 1:
    scene ep12_jill_room21a with dissolve
elif ep11_jill_style == 2:
    scene ep12_jill_room21b with dissolve
elif ep11_jill_style == 3:
    scene ep12_jill_room21c with dissolve
else:
    scene ep12_jill_room21 with dissolve
mc "That's such a beautiful gesture from you. I'm touched..."
scene ep12_jill_room22 with dissolve
mc "You even put new strings on it."
ji "The guy in the shop did."
mc "I can't believe this. My own custom Strutter. What a dream."
scene ep12_jill_room23 with dissolve
mc "Hm... The back panel of the speaker is loose."
if ep11_jill_style == 1:
    scene ep12_jill_room24a with dissolve
elif ep11_jill_style == 2:
    scene ep12_jill_room24b with dissolve
elif ep11_jill_style == 3:
    scene ep12_jill_room24c with dissolve
else:
    scene ep12_jill_room24 with dissolve
ji "Is it broken?"
scene ep12_jill_room25 with dissolve
mc "No, just loose. I can probably tighten the screws for it."
mc "Wait... There's something lodged in there."
if ep11_jill_style == 1:
    scene ep12_jill_room24a with dissolve
elif ep11_jill_style == 2:
    scene ep12_jill_room24b with dissolve
elif ep11_jill_style == 3:
    scene ep12_jill_room24c with dissolve
else:
    scene ep12_jill_room24 with dissolve
ji "Inside the speaker? What is it?"
scene ep12_jill_room26 with dissolve
mc "Um... I'm guessing this wasn't part of the gift."
if ep11_jill_style == 1:
    scene ep12_jill_room28a with dissolve
elif ep11_jill_style == 2:
    scene ep12_jill_room28b with dissolve
elif ep11_jill_style == 3:
    scene ep12_jill_room28c with dissolve
else:
    scene ep12_jill_room28 with dissolve
ji "What is that? Is that...?"
scene ep12_jill_room27 with dissolve
mc "I think it's weed."
if ep11_jill_style == 1:
    scene ep12_jill_room29a with dissolve
elif ep11_jill_style == 2:
    scene ep12_jill_room29b with dissolve
elif ep11_jill_style == 3:
    scene ep12_jill_room29c with dissolve
else:
    scene ep12_jill_room29 with dissolve
ji "She kept drugs in the speaker..."
scene ep12_jill_room26 with dissolve
mc "I'm sorry..."
if ep11_jill_style == 1:
    scene ep12_jill_room29a with dissolve
elif ep11_jill_style == 2:
    scene ep12_jill_room29b with dissolve
elif ep11_jill_style == 3:
    scene ep12_jill_room29c with dissolve
else:
    scene ep12_jill_room29 with dissolve
ji "I wasn't aware that she kept that at home. But it makes sense that's where she'd hide it..."
ji "Mom and Dad would look everywhere else for it."
scene ep12_jill_room26 with dissolve
mc "She found a good hiding spot."
if ep11_jill_style == 1:
    scene ep12_jill_room30a with dissolve
elif ep11_jill_style == 2:
    scene ep12_jill_room30b with dissolve
elif ep11_jill_style == 3:
    scene ep12_jill_room30c with dissolve
else:
    scene ep12_jill_room30 with dissolve
ji "You should throw that out."
if ep11_jill_style == 1:
    scene ep12_jill_room32a with dissolve
elif ep11_jill_style == 2:
    scene ep12_jill_room32b with dissolve
elif ep11_jill_style == 3:
    scene ep12_jill_room32c with dissolve
else:
    scene ep12_jill_room32 with dissolve
mc "This wasn't what killed her."
if ep11_jill_style == 1:
    scene ep12_jill_room31a with dissolve
elif ep11_jill_style == 2:
    scene ep12_jill_room31b with dissolve
elif ep11_jill_style == 3:
    scene ep12_jill_room31c with dissolve
else:
    scene ep12_jill_room31 with dissolve
ji "Those are still her drugs."
if ep11_jill_style == 1:
    scene ep12_jill_room33a with dissolve
elif ep11_jill_style == 2:
    scene ep12_jill_room33b with dissolve
elif ep11_jill_style == 3:
    scene ep12_jill_room33c with dissolve
else:
    scene ep12_jill_room33 with dissolve
mc "Don't feel down. You learned something new about your sister today."
if ep11_jill_style == 1:
    scene ep12_jill_room34a with dissolve
elif ep11_jill_style == 2:
    scene ep12_jill_room34b with dissolve
elif ep11_jill_style == 3:
    scene ep12_jill_room34c with dissolve
else:
    scene ep12_jill_room34 with dissolve
ji "Well... That's true."
if tc < 5 or persistent.no_cheater:
    if ep11_jill_style == 1:
        scene ep12_jill_room35a with dissolve
    elif ep11_jill_style == 2:
        scene ep12_jill_room35b with dissolve
    elif ep11_jill_style == 3:
        scene ep12_jill_room35c with dissolve
    else:
        scene ep12_jill_room35 with dissolve
    $ renpy.pause()
    if ep11_jill_style == 1:
        scene ep12_jill_room36a with dissolve
    elif ep11_jill_style == 2:
        scene ep12_jill_room36b with dissolve
    elif ep11_jill_style == 3:
        scene ep12_jill_room36c with dissolve
    else:
        scene ep12_jill_room36 with dissolve
    ji "I want to hear you play."

stop music fadeout 3
play sound "sound_effects/season3/feedback.mp3"
scene ep12_jill_room37 with dissolve
mc "Alright. Let's take this bad girl for a ride."

play music "music/ep12/riffing_on_lana2.mp3"
if ep11_jill_style == 1:
    scene ep12_jill_room38a with dissolve
elif ep11_jill_style == 2:
    scene ep12_jill_room38b with dissolve
elif ep11_jill_style == 3:
    scene ep12_jill_room38c with dissolve
else:
    scene ep12_jill_room38 with dissolve
$ renpy.pause()
if ep11_jill_style == 1:
    scene ep12_jill_room39a with dissolve
elif ep11_jill_style == 2:
    scene ep12_jill_room39b with dissolve
elif ep11_jill_style == 3:
    scene ep12_jill_room39c with dissolve
else:
    scene ep12_jill_room39 with dissolve
ji "It has a beautiful sound."
scene ep12_jill_room40 with dissolve
mc "It really does. And such a small and tight neck."
mc "It's so smooth and easy to grip. And that tone..."
stop music fadeout 3
mc "I can imagine how this would sound with a full band..."
play music "music/ep12/riffing_on_lana1.mp3"
scene ep12_jill_room41 with dissolve
ji "Playing it like that makes you sound like a blues musician."
scene ep12_jill_room42 with dissolve
mc "Oh, I'm not good enough to be compared to those."
mc "Did you know that some great guitarists name their guitars? Like, Lucille for one."
if ep11_jill_style == 1:
    scene ep12_jill_room43a with dissolve
elif ep11_jill_style == 2:
    scene ep12_jill_room43b with dissolve
elif ep11_jill_style == 3:
    scene ep12_jill_room43c with dissolve
else:
    scene ep12_jill_room43 with dissolve
ji "Oh, yeah? Are you thinking of naming yours?"
scene ep12_jill_room42 with dissolve
mc "Yeah. I think I'll call this guitar \"Lana\", if you don't mind."
if ep11_jill_style == 1:
    scene ep12_jill_room44a with dissolve
elif ep11_jill_style == 2:
    scene ep12_jill_room44b with dissolve
elif ep11_jill_style == 3:
    scene ep12_jill_room44c with dissolve
else:
    scene ep12_jill_room44 with dissolve
ji "I love that."
stop music fadeout 3
if ep11_jill_style == 1:
    scene ep12_jill_room45a with dissolve
elif ep11_jill_style == 2:
    scene ep12_jill_room45b with dissolve
elif ep11_jill_style == 3:
    scene ep12_jill_room45c with dissolve
else:
    scene ep12_jill_room45 with dissolve
$ renpy.pause()
$ new_bio("Jill", "Jill gave me Lana's guitar for Christmas. I found some weed hidden in the speaker and Jill got upset from learning about it.")

jump ep12_bd_label

label ep12_jill_solo_label:
play music "music/ep9/tremolo.mp3"
scene ep12_jill_solo2 with wipeleft
ji "You made it through your first semester at B&R. Regardless of how the tests went, that's a milestone."
scene ep12_jill_solo1 with dissolve
mc "What kind of milestone is it if I have to retake the classes?"
scene ep12_jill_solo2 with dissolve
ji "I think that's your mind playing tricks on you. I remember doubting myself after every test when I came here."
scene ep12_jill_solo3 with dissolve
mc "I'd feel more comfortable seeing the answers to the tests... When do they publish those?"
scene ep12_jill_solo4 with dissolve
ji "It depends on the teacher. In some cases, they publish them the same day, but in others you'll have to wait."
ji "I've also had tests where they didn't publish the answers at all."
scene ep12_jill_solo3 with dissolve
mc "Until then, I'm Schrodinger's student. I could have passed or failed the tests, but I won't know until I get the results."
scene ep12_jill_solo5 with dissolve
ji "Think positive thoughts. And hey, it's winter break now!"
scene ep12_jill_solo3 with dissolve
mc "True. And no one can take that away from us."
mc "What about you? How did it go?"
scene ep12_jill_solo4 with dissolve
ji "I had an essay due this week, and today I had a test for my Macroeconomics II class."
ji "I'm happy with my performance. I know I missed a couple of questions on the test, but I should pass it even so."
scene ep12_jill_solo3 with dissolve
mc "You seem confident in that."
scene ep12_jill_solo4 with dissolve
ji "I am. I mean, you either know something or you don't. You're not going to be able to guess an answer correctly at this level."
scene ep12_jill_solo3 with dissolve
mc "You will, if there are multiple choice questions."
scene ep12_jill_solo5 with dissolve
ji "They stopped including those in tests during sophomore year - at least for us."
ji "Now, almost every question requires a lengthier answer. You're lucky if you can get away with writing a sentence or two."
scene ep12_jill_solo3 with dissolve
mc "Well done, then."
scene ep12_jill_solo5 with dissolve
ji "Thank you."

scene ep12_jill_solo9 with dissolve
mc "Um... There's something I've been meaning to tell you since our Christmas party."
scene ep12_jill_solo6 with dissolve
ji "At Bella's?"
scene ep12_jill_solo8 with dissolve
mc "No. The one at the DIKs."
mc "You see... Something happened to me, and I've waited to get a chance to tell you."
mc "But there was always something that stopped me from telling you. I didn't want to ruin the good moments we had by bringing it up."
scene ep12_jill_solo7 with dissolve
ji "What happened?"
if tc < 5 or persistent.no_cheater:
    scene ep12_jill_solo8 with dissolve
    mc "You don't have to worry. Let me start by saying that."
    scene ep12_jill_solo7 with dissolve
    ji "Ok?"
scene ep12_jill_solo8 with dissolve
mc "*{i}Sigh{/i}* Zoey told me that she's in love with me. And she tried to rekindle our relationship."
scene ep12_jill_solo10 with dissolve
ji "She what!?"
scene ep12_jill_solo11 with dissolve
mc "And I told her it was too late for that."
scene ep12_jill_solo10 with dissolve
ji "Back up, please. This is not something you tell me in parts. I want to know everything she said; tell me every single detail."
scene ep12_jill_solo11 with dissolve
mc "She came to the party, and we had a good time as friends. She mentioned she needed to talk to me, and we went to my room for a private chat."
mc "She started reminiscing about our youth and about how we met."
mc "That conversation led her to say that she realized she was in love with me."
if zoey_dik:
    mc "Then she tried to kiss me."
scene ep12_jill_solo13 with dissolve
mc "I was stunned... I stopped her and told her that I was in a relationship."
mc "But that didn't seem to deter her. She tried to convince me to have a change of heart."
scene ep12_jill_solo12 with dissolve
mc "And I told her it was too late for that."
mc "She got upset and felt stupid for putting herself out there."
mc "And then she left. I haven't heard from her since."
scene ep12_jill_solo14 with dissolve
ji "Wow..."
ji "I've been worried that this would happen."
scene ep12_jill_solo12 with dissolve
mc "You have?"
scene ep12_jill_solo14 with dissolve
ji "From the moment you told me you two got back together as friends, there was a little voice in the back of my head that whispered bad things."
ji "What if [name] falls in love with her again? What if it's more than just a friendship?"
scene ep12_jill_solo15 with dissolve
ji "But I didn't dare to voice my concerns to you because I didn't want you to think I didn't trust you."
scene ep12_jill_solo13 with dissolve
mc "You've been uncomfortable about that all this time, huh? Sage actually told me about it."
scene ep12_jill_solo14 with dissolve
ji "She did? I told her that in confidence..."
scene ep12_jill_solo12 with dissolve
mc "She let me know in a good way, though. She asked me to treat you right and be more mindful."
mc "Sage had your back."
scene ep12_jill_solo16 with dissolve
ji "Oh... That's sweet of her."
if tc < 5 or persistent.no_cheater:
    scene ep12_jill_solo19 with dissolve
    mc "You don't have to worry about Zoey stealing me from you. I'm all yours."
    mc "Zoey is just my friend."
else:
    scene ep12_jill_solo12 with dissolve
    mc "Either way, Zoey is just my friend."
if tc < 5 or persistent.no_cheater:
    scene ep12_jill_solo18 with dissolve
else:
    scene ep12_jill_solo14 with dissolve
ji "Do you think she wants to stay your friend now that you rejected her?"
ji "Won't that be awkward for you two?"
if tc < 5 or persistent.no_cheater:
    scene ep12_jill_solo17 with dissolve
else:
    scene ep12_jill_solo12 with dissolve
mc "Uh... It might be awkward, but what else can we do? I mean, she's still my childhood friend."
if tc < 5 or persistent.no_cheater:
    scene ep12_jill_solo18 with dissolve
else:
    scene ep12_jill_solo15 with dissolve
ji "But that's not all that she is nowadays. She's also your ex-girlfriend and, more recently, someone who loves you more than a friend."
if tc < 5 or persistent.no_cheater:
    scene ep12_jill_solo17 with dissolve
else:
    scene ep12_jill_solo12 with dissolve
mc "I know, but... *{i}Sigh{/i}* That's not how I look at her."
mc "Does it still make you uncomfortable that I'm her friend?"

if tc < 5 or persistent.no_cheater:
    scene ep12_jill_solo20 with dissolve
else:
    scene ep12_jill_solo15 with dissolve
ji "Honestly... Now even more so than before."
if tc < 5 or persistent.no_cheater:
    scene ep12_jill_solo21 with dissolve
    mc "All I need you to know is that I'm not in love with Zoey. I don't feel that way about her anymore."
    mc "And I think that I have proved that."
    scene ep12_jill_solo22 with dissolve
    ji "I agree, and I appreciate that you told me."
    ji "It wasn't easy to hear, and I'm sure it wasn't easy for you to tell me."
    ji "But I feel good about how you handled it. That makes me more confident in our relationship."
    scene ep12_jill_solo23 with dissolve
    mc "Can we talk about something else? I don't want to ruin this evening anymore."
    scene ep12_jill_solo22 with dissolve
    ji "It's not ruined."
    scene ep12_jill_solo24 with dissolve
    ji "*{i}Smack{/i}*"
    scene ep12_jill_solo25 with dissolve
    mc "Oh! Tell me about your meeting with Jonathan."
else:
    scene ep12_jill_solo13 with dissolve
    if ep12_bianca_lewd:
        mc "(Then you're not gonna like hearing about Bianca... Fuck... What am I even doing with Jill?)"
    else:
        mc "(Jill... If this is how you react to me rejecting Zoey... *{i}Sigh{/i}* Relationships are hard...)"
    mc "Can we talk about something else?"
    mc "Maybe you can tell me about your meeting with Jonathan or something."

if tc < 5 or persistent.no_cheater:
    scene ep12_jill_solo27 with dissolve
else:
    scene ep12_jill_solo15 with dissolve
    ji "Sure... Um..."
    scene ep12_jill_solo16 with dissolve
ji "We had a long talk about the campaign I wanted to start for Lana."
ji "And right now, the idea is that I'll set up a foundation honoring her memory."
if tc < 5 or persistent.no_cheater:
    scene ep12_jill_solo26 with dissolve
else:
    scene ep12_jill_solo11b with dissolve
mc "How does that work?"
if tc < 5 or persistent.no_cheater:
    scene ep12_jill_solo28 with dissolve
else:
    scene ep12_jill_solo11c with dissolve
ji "Well, a foundation can be many things. In this case, I want it to help youth in situations like my sister's."
ji "I want to raise awareness about the risks of substance abuse and inform teenagers how they can get help if they need it."
if tc < 5 or persistent.no_cheater:
    scene ep12_jill_solo27 with dissolve
ji "Jonathan and I talked about hosting seminars and speaking at high schools, among other things."
if tc < 5 or persistent.no_cheater:
    scene ep12_jill_solo26 with dissolve
else:
    scene ep12_jill_solo11b with dissolve
mc "It sounds like hard work."
if tc < 5 or persistent.no_cheater:
    scene ep12_jill_solo28 with dissolve
else:
    scene ep12_jill_solo11c with dissolve
ji "It is. But it's also something I really want to do."
if tc < 5 or persistent.no_cheater:
    scene ep12_jill_solo26 with dissolve
    mc "Can I help in any way?"
    scene ep12_jill_solo27 with dissolve
    ji "You want to help me?"
    scene ep12_jill_solo26 with dissolve
    mc "I'm not sure if I can, but if there's anything I can do - absolutely!"
    scene ep12_jill_solo27 with dissolve
    ji "You're so sweet! Thank you."
    ji "I'll let you know if something comes to mind."
else:
    scene ep12_jill_solo11b with dissolve
    mc "You should go for it then."
    scene ep12_jill_solo14b with dissolve

ji "Right now, I'm at the stage of defining what it will be and gathering information on how to do it."
if tc < 5 or persistent.no_cheater:
    scene ep12_jill_solo28 with dissolve
ji "Speaking of Lana... When I visited to pick up her guitar for you, I also brought some of her clothes back with me."
if tc < 5 or persistent.no_cheater:
    scene ep12_jill_solo26 with dissolve
else:
    scene ep12_jill_solo14c with dissolve
mc "Lana's clothes?"
if tc < 5 or persistent.no_cheater:
    scene ep12_jill_solo29 with dissolve
else:
    scene ep12_jill_solo14b with dissolve
ji "Yes. I don't know why I did it, but I wanted to try them on."
ji "I think it was because of you and our time at the mall."
if tc < 5 or persistent.no_cheater:
    scene ep12_jill_solo30 with dissolve
else:
    scene ep12_jill_solo14c with dissolve
mc "Have you ever tried them on before?"
if tc < 5 or persistent.no_cheater:
    scene ep12_jill_solo29 with dissolve
else:
    scene ep12_jill_solo14b with dissolve
ji "No, I never did. Well, except for her hat. Oh! And one of her hoodies I used to find comfort in when I was younger."
ji "I brought that one with me, too."
ji "Wanna see?"
if tc < 5 or persistent.no_cheater:
    scene ep12_jill_solo30 with dissolve
else:
    scene ep12_jill_solo14c with dissolve
mc "Sure! Bring on the fashion show."
scene ep12_jill_solo31 with dissolve
ji "It's hardly a fashion show, and it's not my style at all!"
scene ep12_jill_solo32 with dissolve
mc "Hey, don't say that. Leave it for the judge."

scene ep12_jill_solo33 with dissolve
ji "This was her hoodie and her hat."
scene ep12_jill_solo34 with dissolve
mc "Wow... I remember the picture you showed me of her."
mc "You look even more like her now."
scene ep12_jill_solo36 with dissolve
ji "Do you think?"
scene ep12_jill_solo35 with dissolve
mc "I do."
scene ep12_jill_solo33 with dissolve
ji "But I can't pull this off as well as she did."
scene ep12_jill_solo34 with dissolve
mc "Don't say that. I think you can. You look cool wearing it!"
scene ep12_jill_solo35 with dissolve
ji "(Haha... Maybe I can pull it off!?)"
scene ep12_jill_solo36 with dissolve
ji "Oh! And I also brought something else."
ji "Hold on for a second while I get changed. No peeking!"
scene ep12_jill_solo32 with dissolve
mc "No peeking? I've seen you naked many times."
scene ep12_jill_solo37 with dissolve
ji "Haha! I mean, I don't want you to see the clothes until I'm fully dressed. That will ruin the element of surprise."
play sound "sound_effects/clothes.mp3"
scene ep12_jill_solo38 with dissolve
ji "There! You can look!"
scene ep12_jill_solo39 with dissolve
mc "Whoa! Did she wear that?"
scene ep12_jill_solo40 with dissolve
ji "Yeah. We're not the same size in some parts."
scene ep12_jill_solo41 with dissolve
mc "You filled that out well. Wow..."
ji "Haha! Stop it!"
scene ep12_jill_solo42 with dissolve
mc "No, but seriously... You look so good."
scene ep12_jill_solo43 with dissolve
ji "[name], I'm not used to wearing clothes like this."
ji "If you look at my wardrobe, you'd know."
scene ep12_jill_solo42 with dissolve
mc "I don't have to look at your wardrobe; I've seen what you wear."
if tc < 5 or persistent.no_cheater:
    scene ep12_jill_solo44 with dissolve
    mc "And I'm not disrespecting your usual clothes because you always look beautiful..."
    mc "I'm simply saying that you could wear this too."
scene ep12_jill_solo45 with dissolve
ji "Can you imagine me wearing this to class or walking around campus in it?"
scene ep12_jill_solo44 with dissolve
mc "I can."
scene ep12_jill_solo45 with dissolve
ji "Everyone would turn their heads, wouldn't they?"
scene ep12_jill_solo42 with dissolve
mc "They sure would. It's winter."
scene ep12_jill_solo43 with dissolve
ji "Ha-ha... I didn't mean it like that. I meant, they would notice the contrast of my usual self."
scene ep12_jill_solo46 with dissolve
mc "Yeah, that too. But who gives a crap about what people think?"
mc "I don't dress the way I do for others. I don't even give much thought to what I wear. Clothes are just clothes."
scene ep12_jill_solo47 with dissolve
ji "So, you think I should wear this?"
scene ep12_jill_solo46 with dissolve
mc "Would you want to wear it?"
scene ep12_jill_solo49 with dissolve
ji "..."
scene ep12_jill_solo48 with dissolve
ji "I think I look good."
ji "But I'm unsure... It's a scary thought. It feels like I'm doing something forbidden."
scene ep12_jill_solo50 with dissolve
mc "Who forbade you to wear clothes like that?"
ji "..."
scene ep12_jill_solo51 with dissolve
ji "Take a guess."
scene ep12_jill_solo52 with dissolve
mc "Your parents?"
scene ep12_jill_solo51 with dissolve
ji "Mom wouldn't like it..."
ji "That's why it feels like it's forbidden."
scene ep12_jill_solo52 with dissolve
mc "I see. Do you know that for sure?"
scene ep12_jill_solo54 with dissolve
ji "Yes... I do. In fact, when I picked up your gift and these clothes, we got into an argument."
ji "They worry about me."
scene ep12_jill_solo52 with dissolve
mc "Worry how?"
scene ep12_jill_solo54 with dissolve
if ep11_jill_style == 0:
    ji "They raised some concerns about you and our relationship."
else:
    ji "They saw how I dressed when I showed up, and they raised some concerns about you and our relationship."
ji "I think they are scared that I'm going to turn into my sister."
scene ep12_jill_solo52 with dissolve
mc "Huh? Because of me?"
scene ep12_jill_solo51 with dissolve
ji "I think they see Jonathan in you, and they see Lana in me."
scene ep12_jill_solo52 with dissolve
mc "So, they don't like me? That's tough to hear."
scene ep12_jill_solo51 with dissolve
ji "It's not that they don't like you. It's more that they get flashbacks to how it was when Lana dated Jonathan."
ji "I think it's uncalled for. But they are scarred from the trauma."
ji "So... If I dress like this, I know they would get increasingly concerned."
scene ep12_jill_solo53 with dissolve
mc "Well... Your Mom doesn't go to B&R."
mc "I see this as you doing something for yourself. And there is nothing wrong with that."
scene ep12_jill_solo55 with dissolve
ji "..."
scene ep12_jill_solo56 with dissolve
ji "You like this, right?"
scene ep12_jill_solo55 with dissolve
mc "Yes, but I like you in your usual clothes too."
mc "Men shouldn't tell women what to wear."
mc "Holy fuck... I think gender studies rubbed off on me."
scene ep12_jill_solo58 with dissolve
ji "Hahaha!"
scene ep12_jill_solo57 with dissolve
ji "But you're right about it."
scene ep12_jill_solo56 with dissolve
ji "No one should tell me what to wear except me."
stop music fadeout 3
scene ep12_jill_solo59 with dissolve
$ renpy.pause()
$ mgallery_add_photo("ep12_jill_solo_pic1")
$ mgallery_add_photo("ep12_jill_solo_pic2")
$ mgallery_add_photo("ep12_jill_solo_pic3")
$ new_bio("Jill", "I told Jill about what happened with Zoey and she got even more concerned about my friendship to Zoey.")
$ new_bio("Jill", "Jill tried on Lana's old clothes for me. She seemed to like wearing them, even though they weren't her style.")

if (not branchZoey or wt_ep11_zoey_kiss_others)  and branchIsabella and not breakup:
    $ guideSuggestedPage = 253
    jump ep12_bella_solo_label
elif ((not branchZoey or wt_ep11_zoey_kiss_others) and branchSage) and (ep11_sage_love == 2 or RPsage >= 22) and not breakup:
    $ guideSuggestedPage = 254
    jump ep12_sage_solo_label
else:
    jump ep12_dikmas_label

jump ep12_dikmas_label

# Decompiled by unrpyc {v1.3.2}: https://github.com/CensoredUsername/unrpyc dev-branch
