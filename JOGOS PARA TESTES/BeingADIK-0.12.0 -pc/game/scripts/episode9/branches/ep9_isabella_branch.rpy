label ep9_bella_branch_label:
scene ep9_bella_branch1 with dissolve
mc "(Bella's gonna be here any minute now...)"
mc "(She's the only guest coming in this way. I hope it wasn't stupid inviting her.)"
mc "(I want to spend more time with her, but sneaking around like this won't work in the long run.)"
scene ep9_bella_branch57 with dissolve
$ renpy.pause()
play music "music/ep8/licensed_music/track65.mp3"
scene ep9_bella_branch3 with dissolve
isa "Do you realize how that would look?"
scene ep9_bella_branch2 with dissolve
isa "A faculty member among students at a party, which we don't allow?"
scene ep9_bella_branch4 with dissolve
mc "Parties, you know...gatherings are ok; it's the alcohol you don't allow."
mc "I don't know how that helps to make my case for it, but it's gotta count for something."
scene ep9_bella_branch5 with dissolve
isa "I can't come."
scene ep9_bella_branch6 with dissolve
mc "I want you there."
mc "Didn't you ever have Halloween parties back in college?"
scene ep9_bella_branch7 with dissolve
isa "Of course, we had them."
scene ep9_bella_branch8 with dissolve
mc "Don't you want to relive that? It's a perfect chance for it."
mc "Also, you know what's great about a Halloween party, right?"
scene ep9_bella_branch9 with dissolve
mc "You get to dress up. You can hide your face, and no one would know it was you."
scene ep9_bella_branch10 with dissolve
isa "[name]! Don't touch that mask."
scene ep9_bella_branch11 with dissolve
mc "I'm not [name]. I'm someone else."
scene ep9_bella_branch13 with dissolve
isa "I got your point. Now, please put it back."
scene ep9_bella_branch12 with dissolve
mc "Not until you tell me you'll come to our party."
scene ep9_bella_branch13 with dissolve
isa "Fine, I'll come! Happy?"
scene ep9_bella_branch12 with dissolve
mc "Uga Buga happy!"
scene ep9_bella_branch13 with dissolve
isa "But the moment I feel something's wrong, I'll leave."
scene ep9_bella_branch14 with dissolve
mc "We can lock ourselves in my room at any time. I promise."
scene ep9_bella_branch15 with dissolve
isa "*{i}Sigh{/i}* Can we move on? This isn't why I asked you to come over."
isa "I need to talk to you about something."
if affinity == "DIK":
    scene ep9_bella_branch16 with dissolve
    mc "Oh, no... Are you breaking up with me?"
    scene ep9_bella_branch15 with dissolve
    isa "I'm trying to be serious here."
    scene ep9_bella_branch16 with dissolve
    mc "You're almost always serious, though."
else:
    scene ep9_bella_branch16 with dissolve
    mc "What's the matter?"
scene ep9_bella_branch15 with dissolve
isa "Something happened with Jill, and it's not good."
scene ep9_bella_branch16 with dissolve
mc "Oh...?"
scene ep9_bella_branch17 with dissolve
isa "Apparently, during our date, we were being too careless. She...um... She saw us."
scene ep9_bella_branch16 with dissolve
mc "She saw us...doing what?"
scene ep9_bella_branch17 with dissolve
isa "She saw us on the dining room table."
scene ep9_bella_branch18 with dissolve
$ renpy.pause()

scene ep9_bella_branch28b with dissolve
play sound "sound_effects/door_knock.mp3"
isa "Jill? I know you're in there. Please, open up. It's me."

if ep9_jill_mood == 3:
    scene ep9_bella_branch27 with dissolve
    ji "Bella! Go away!"
    scene ep9_bella_branch28 with dissolve
    isa "What's wrong?"
    scene ep9_bella_branch27 with dissolve
    ji "What's wrong!? Are you joking!?"
    scene ep9_bella_branch28 with dissolve
    isa "No, I'm not joking. I don't understand. What's got you this upset?"
    scene ep9_bella_branch29 with dissolve
    ji "You're having sex with [name]!"
    scene ep9_bella_branch30 with dissolve
    isa "..."
    scene ep9_bella_branch32 with dissolve
    ji "I saw you going at it on your dining table like animals!"
    scene ep9_bella_branch31 with dissolve
    isa "Oh my God..."
    isa "Jill, can we please go inside? I'll explain."
    scene ep9_bella_branch32 with dissolve
    ji "Yes, please. Explain why you're sleeping with the guy I'm dating."
    if ep3_bella_came_around:
        ji "Not just the guy I've been dating, but the guy you encouraged me to date."
    else:
        ji "Not just the guy I've been dating, but the guy you said wasn't good enough for me to date."
    scene ep9_bella_branch34 with dissolve
    ji "The guy I liked and thought would be my...my..."
    scene ep9_bella_branch35 with dissolve
    isa "Jill..."
    isa "You weren't supposed to find out this way. I was going to tell you as soon as possible, I swear."
    isa "[name] and I agreed we would tell you about it."
    scene ep9_bella_branch36 with dissolve
    ji "Were you going to tell me? Gee, thanks! That makes it all better!"
    scene ep9_bella_branch37 with dissolve
    ji "I can't believe you did this to me. I mean...you? Seriously?"
    ji "Out of all the people I'm close to in my life, you're the last one I thought would betray me. Ever!"
    scene ep9_bella_branch46 with dissolve
    isa "I'm so sorry... I should have told you sooner, but I've been trying to fight my feelings."
    isa "And it got to the point where I couldn't fight them anymore."
    scene ep9_bella_branch37 with dissolve
    ji "Your feelings? Your feelings for [name]?"
    ji "How long has this been going on!?"
    scene ep9_bella_branch47 with dissolve
    isa "I...I don't know. I mean, what you saw was the first time - well, the night before that was the first time."
    isa "And there'd been some attraction earlier, but-"
    scene ep9_bella_branch37 with dissolve
    ji "So, you've known this for how long exactly?"
    scene ep9_bella_branch48 with dissolve
    isa "I've been fighting this since before you even dated him."
    isa "I didn't plan for this to happen."
    scene ep9_bella_branch38 with dissolve
    ji "Before I dated him!? And you never told me..."
    ji "It's so wrong."
    scene ep9_bella_branch50 with dissolve
    isa "What?"
    scene ep9_bella_branch38 with dissolve
    ji "I mean...aren't you his teacher now? And you're so much older than him!"
    scene ep9_bella_branch39 with dissolve
    ji "And you're my best friend...or you were my best friend."
    scene ep9_bella_branch46 with dissolve
    isa "Jill... I'm so sorry."
    isa "If you're not ok with this, I'll stop. I'll stop it right now."
    isa "I'd never give you up for him."
    scene ep9_bella_branch39 with dissolve
    ji "This is not about whether you should stop or not. This is about you going behind my back like that in the first place."
    ji "You could have told me so much earlier, and you didn't."
    scene ep9_bella_branch49 with dissolve
    isa "..."
    scene ep9_bella_branch48 with dissolve
    isa "You're right. There's no excuse for it."
    scene ep9_bella_branch40 with dissolve
    ji "You're always lecturing me about how to behave and think. Telling me I'm naive and that I should grow up and become a better person by your standards."
    scene ep9_bella_branch50 with dissolve
    isa "I don't tell you that."
    scene ep9_bella_branch40 with dissolve
    ji "It's implied in the way you say it. It makes me feel like I'm not good enough at times."
    ji "And as it turns out..."
    ji "You're the one who's been doing wrong."
    scene ep9_bella_branch50 with dissolve
    isa "After all this time together and knowing what I've been through, I thought you'd understand me better."
    scene ep9_bella_branch41 with dissolve
    ji "You know what? I would have."
    ji "But you didn't tell me about it. And you watched me fall for the guy..."
    scene ep9_bella_branch51 with dissolve
    $ renpy.pause()
    scene ep9_bella_branch52 with dissolve
    $ renpy.pause()
else:
    scene ep9_bella_branch27b with dissolve
    ji "Bella... What do you want?"
    scene ep9_bella_branch28 with dissolve
    isa "What's wrong?"
    scene ep9_bella_branch27b with dissolve
    ji "Are you joking?"
    scene ep9_bella_branch28 with dissolve
    isa "No, I'm not joking. I don't understand. You've never avoided me like this in the past."
    scene ep9_bella_branch29b with dissolve
    ji "I saw you having sex with [name]."
    scene ep9_bella_branch30 with dissolve
    isa "..."
    scene ep9_bella_branch32b with dissolve
    ji "I was coming over to talk to you, and there you were... Having sex on your dining table."
    scene ep9_bella_branch31 with dissolve
    isa "Oh my God..."
    isa "Jill, can we please go inside? I'll explain."
    scene ep9_bella_branch32b with dissolve
    ji "I don't know what to feel."
    ji "At first, I was shocked and confused."
    if ep3_bella_came_around:
        ji "Then I felt betrayed because you've been sleeping with the guy you encouraged me to date."
    else:
        ji "Then I felt betrayed because you've been sleeping with the guy I dated, who you said wasn't good enough for me to date."
    scene ep9_bella_branch33 with dissolve
    ji "And then I felt weirded out. I mean, you're his teacher, and there's a pretty big age gap."
    scene ep9_bella_branch32b with dissolve
    ji "And now I'm back to feeling...annoyed with both of you."
    ji "And I can't wrap my head around it... Why didn't you tell me?"
    scene ep9_bella_branch35b with dissolve
    isa "I'm so sorry... I should have told you sooner, but I've been trying to fight my feelings."
    isa "And it got to the point where I couldn't fight them anymore."
    scene ep9_bella_branch36b with dissolve
    ji "Your feelings?"
    ji "How long has this been going on?"
    scene ep9_bella_branch53 with dissolve
    isa "I...I don't know. I mean, what you saw was the first time - well, the night before that was the first time."
    isa "And I'd felt some attraction earlier, but-"
    scene ep9_bella_branch42 with dissolve
    ji "So, you've known this for how long exactly?"
    scene ep9_bella_branch53 with dissolve
    isa "I've been fighting this since before you even dated him."
    isa "I didn't plan for this to happen."
    scene ep9_bella_branch55 with dissolve
    isa "Jill... I'm so sorry."
    isa "If you're not ok with this, I'll stop. I'll stop it right now."
    isa "I'd never give you up for him."
    scene ep9_bella_branch43 with dissolve
    ji "This is not about whether you should stop or not."
    ji "You didn't trust me enough to tell me this in the first place, and you knew I was dating him."
    ji "You could have told me so much earlier, and you didn't... Don't you understand how that makes me feel?"
    scene ep9_bella_branch54 with dissolve
    isa "..."
    scene ep9_bella_branch53 with dissolve
    isa "You're right. There's no excuse for it."
    scene ep9_bella_branch44 with dissolve
    ji "You're always lecturing me about how to behave and think."
    ji "Telling me I'm naive and that I should grow up and become a better person by your standards."
    scene ep9_bella_branch53 with dissolve
    isa "I don't tell you that."
    scene ep9_bella_branch44 with dissolve
    ji "It's implied in the way you say it. It makes me feel like I'm not good enough at times."
    ji "And as it turns out..."
    ji "You're the one who's been doing wrong things."
    scene ep9_bella_branch53 with dissolve
    isa "After all this time together and seeing what I've been through, I thought you'd understand me better."
    scene ep9_bella_branch45 with dissolve
    ji "You know what? I would have."
    ji "But you didn't tell me about it. And I tell you about everything."
    scene ep9_bella_branch43 with dissolve
    if ep6_jill_lewd:
        ji "What scares me the most is that I was close to falling for him..."
        ji "What would that have been like? When you never told me that you wanted him?"
    else:
        ji "What would you have done if I had fallen for him when you knew that you wanted him all this time?"
    scene ep9_bella_branch54 with dissolve
    isa "..."
    scene ep9_bella_branch43 with dissolve
    ji "I need to be alone for a while."
    scene ep9_bella_branch53 with dissolve
    isa "I'm so sorry."
    scene ep9_bella_branch56 with dissolve
    $ renpy.pause()
$ guideSuggestedPage = 55
scene ep9_bella_branch18 with dissolve
$ renpy.pause()
scene ep9_bella_branch16 with dissolve
if ep9_jill_mood == 3:
    mc "What the hell? Are you alright?"
else:
    mc "Are you alright?"
scene ep9_bella_branch19 with dissolve
isa "No."
scene ep9_bella_branch20 with dissolve
$ renpy.pause()
scene ep9_bella_branch21 with dissolve
mc "Have you talked since?"
isa "I've been writing to her to say I'm sorry, but she hasn't replied."
scene ep9_bella_branch22 with dissolve
mc "This explains why she's been avoiding me too..."
mc "I should try to talk to her."
mc "What you said to her... That you'd end this for her... Is that what you want?"
scene ep9_bella_branch23 with dissolve
isa "I wouldn't have a choice. Without Jill, I..."
isa "Jill means the world to me."
scene ep9_bella_branch22 with dissolve
mc "This is all my fault."
scene ep9_bella_branch23 with dissolve
if ep9_jill_mood == 3:
    isa "It's not. It's my fault too."
else:
    isa "It's not. It's my fault."
scene ep9_bella_branch22 with dissolve
mc "I shouldn't have dated her at the same time. Then none of this would have happened."
scene ep9_bella_branch24 with dissolve
if ep9_jill_mood == 3:
    isa "You don't know that. Maybe she'd have gotten feelings for you even so."
    isa "Even though it felt wrong, I should have told her about my feelings for you earlier."
else:
    isa "No, it's because I was scared. I didn't dare to voice my feelings for you to her earlier."
scene ep9_bella_branch25 with dissolve
mc "You've got feelings for me?"
scene ep9_bella_branch24 with dissolve
isa "Of course, I have."
scene ep9_bella_branch25 with dissolve
if persistent.mod_wtenabled: 
                        $mod_choices = ["(+Isabella)","(+Maya)","(-DIK)","(+DIK)","(Sandy scene)","(Sarah scene)","","","","","","" ]
                        #[mod_gr][mod_choices[0]]
menu:
    "I feel the same [mod_gr][mod_choices[0]]":
        $ RPisabella += 2
        mc "I have feelings for you too."
    "That's nice":
        mc "Wow... That's nice."
scene ep9_bella_branch26 with dissolve
$ renpy.pause()
stop music fadeout 3
$ new_bio("Isabella", "Bella talked to Jill, but it turned into a fight. It made Bella very sad.")
$ new_bio("Jill", "Bella talked to Jill, but it turned into a fight. It made Bella very sad.")
scene ep9_bella_branch57 with dissolve
mc "(...)"

play music "music/ep9/diks_spooky_halloween.mp3"
scene ep9_bella_branch58 with dissolve
mc "Bella..."
scene ep9_bella_branch59 with dissolve
isa "Hi. Is it safe?"
scene ep9_bella_branch60 with dissolve
mc "Yeah, the door's locked. Come on in."
menu:
    "Kiss her":
        scene ep9_bella_branch63 with dissolve
        mc "*{i}Smack{/i}*"
        scene ep9_bella_branch61 with dissolve
        isa "You seem relaxed."
        scene ep9_bella_branch62 with dissolve
        mc "Believe me; I'm not. This party has been hectic up until now."
        mc "But seeing you calms me down."
    "Hug her":
        scene ep9_bella_branch64 with dissolve
        mc "I'm so happy you came."
        scene ep9_bella_branch61 with dissolve
        isa "I went back and forth but eventually decided to come."

scene ep9_bella_branch65 with dissolve
isa "So, your costume... It doesn't leave much to the imagination."
scene ep9_bella_branch66 with dissolve
mc "If Spartans wore shirts, I would have."
if ep3_wearHelmet:
    scene ep9_bella_branch67 with dissolve
    isa "It must be nice to wear a helmet without a penis on it."
    scene ep9_bella_branch66 with dissolve
    mc "Haha! Very."
scene ep9_bella_branch69 with dissolve
isa "You look good."
scene ep9_bella_branch70 with dissolve
isa "I hope this costume idea works out. If it doesn't, I will leave."
scene ep9_bella_branch71 with dissolve
mc "It will work out. Did you bring makeup?"
scene ep9_bella_branch70 with dissolve
isa "I did. Where's the costume?"
scene ep9_bella_branch71 with dissolve
mc "I'll get it. I hope the size is right."
scene ep9_bella_branch70 with dissolve
isa "So, how do we get into the bathroom?"
scene ep9_bella_branch71 with dissolve
mc "I'll make sure the coast is clear."

scene ep9_bella_branch72 with wipeleft
mc "Do you need any help?"
isa "Not with this."
scene ep9_bella_branch73 with dissolve
mc "How hard can it be? It's scary makeup. Any makeup I would apply would look scary."
scene ep9_bella_branch74 with dissolve
isa "I don't doubt that."
scene ep9_bella_branch75 with dissolve
mc "Will you be ok at the party? I mean, you don't know the people here."
scene ep9_bella_branch74 with dissolve
isa "I think I recognize more people than you think."
scene ep9_bella_branch75 with dissolve
mc "It's pretty cool. If you think about it, you have double costumes. You're a college student dressed as a mummy."
scene ep9_bella_branch76 with dissolve
isa "Don't worry. While I'd appreciate your company tonight, don't feel like you have to babysit me when you have things to deal with."
scene ep9_bella_branch77 with dissolve
mc "I didn't tell anyone you were coming, but you can probably talk to Sage, Maya, Josy, and maybe Jill."
isa "Is Jill coming?"
mc "It seems so. I spotted her on the invite list."
scene ep9_bella_branch78 with dissolve
isa "I doubt she wants to talk to me."
scene ep9_bella_branch79 with dissolve
mc "She can't ignore you forever... It's gonna be good between you two again, right?"
isa "..."
scene ep9_bella_branch78 with dissolve
isa "I'll try to talk to her."
scene ep9_bella_branch80 with dissolve
isa "What do you think?"
scene ep9_bella_branch81 with dissolve
menu:
    "Scary":
        mc "You look scary."
        scene ep9_bella_branch83 with dissolve
        isa "I promise not to bite."
        scene ep9_bella_branch82 with dissolve
        mc "Mummies aren't zombies. I think I will be fine if you nibble a bit on me."
    "Hot":
        mc "You look weirdly hot."
        scene ep9_bella_branch83 with dissolve
        isa "Hot? I look like a scary clown."
        if affinity == "DIK":
            scene ep9_bella_branch82 with dissolve
            mc "A hot and scary clown with big tits."
            scene ep9_bella_branch84 with dissolve
            isa "*{i}Sigh{/i}* [name]..."
        else:
            scene ep9_bella_branch82 with dissolve
            mc "Well, I like it!"
            scene ep9_bella_branch83 with dissolve
            isa "Is the bar this low for you?"
    "Joke":
        scene ep9_bella_branch82 with dissolve
        mc "That it would be hilarious if you wore that to work."

scene ep9_bella_branch80 with dissolve
isa "People will still see it's me with this."
scene ep9_bella_branch85 with dissolve
mc "Yeah, but not when you're wearing the costume on top of the makeup."
scene ep9_bella_branch80 with dissolve
isa "You'll have to help me with it."
scene ep9_bella_branch86 with dissolve
mc "Not a problem... This part is for your head. With this on, you're already unrecognizable."
scene ep9_bella_branch87 with dissolve
mc "Yes, like that. And pull this part over your mouth."

scene ep9_bella_branch88 with dissolve
mc "Yep, this looks good. Unrecognizable!"
scene ep9_bella_branch89 with dissolve
mc "And this is the top."
isa "Am I supposed to wear that without anything underneath?"
mc "I think so, yeah."
scene ep9_bella_branch90 with dissolve
mc "*{i}Grunts{/i}*"
scene ep9_bella_branch91 with dissolve
$ renpy.pause()
scene ep9_bella_branch92 with dissolve
mc "Hngn..."
isa "Quit your moaning..."
menu:
    "Behave":
        mc "It's hard..."
    "Touch them":
        scene anim_bella_tits_ep9 with dissolve
        mc "How do you expect me to do that?"
        isa "*{i}Sigh{/i}*"
scene ep9_bella_branch93 with dissolve
mc "Oh, man..."
scene ep9_bella_branch94 with dissolve
isa "*{i}Sigh{/i}* Go ahead..."
scene ep9_bella_branch95 with dissolve
menu:
    "Kiss":
        mc "I mean... You probably enjoy it too."
        scene anim_bella_tits2_ep9 with dissolve
        isa "Probably not nearly as much as you, but yes."
        mc "*{i}Smack{/i}*"
        isa "[name]... This is hardly the place for it."
    "Fondle":
        mc "I mean... You probably enjoy it too."
        scene anim_bella_tits3_ep9 with dissolve
        isa "Men's fascination with breasts has always baffled me."
    "Behave":
        mc "No, no. I can behave."
        isa "Your loss."

scene ep9_bella_branch96 with dissolve
mc "And here are the...bottoms."
scene ep9_bella_branch97 with dissolve
isa "Turn around."
mc "Come on... I'll behave."
scene ep9_bella_branch98 with dissolve
isa "..."
scene ep9_bella_branch99 with dissolve
mc "Here you go."
scene ep9_bella_branch100 with dissolve
isa "There. What's next?"
scene ep9_bella_branch101 with dissolve
mc "These go around your arms..."
mc "And these must be for your legs and feet."
scene ep9_bella_branch102 with dissolve
mc "Everything seems to fit."
isa "Yes, I believe the size is right. What now?"
mc "That's...all of it."
scene ep9_bella_branch103 with dissolve
isa "What? It can't be. What about the torso?"
mc "There's...nothing more for it."
scene ep9_bella_branch104 with dissolve
isa "[name], I can't wear this. It's too revealing."
isa "My asscheeks aren't fully covered."
$ guideSuggestedPage = 56
scene ep9_bella_branch105 with dissolve
mc "Here, let me check..."
scene ep9_bella_branch106 with dissolve
menu:
    "Fondle":
        scene ep9_bella_branch107 with dissolve
        mc "*{i}Grunts{/i}*"
        isa "Stop that!"
    "Behave":
        mc "Most of it is covered."
mc "Don't worry. You'll be fine wearing this."
scene ep9_bella_branch108 with dissolve
isa "Maybe I can put on a bathrobe or something?"
mc "Yeah, because mummies also wear those after showers."
mc "Don't be stupid. It would defeat the purpose of your costume."
mc "No one knows it's you. Also, I know that you won't be alone looking like that."
isa "Like what?"
if persistent.mod_wtenabled: 
                        $mod_choices = ["(+Isabella)","(+Maya)","(-DIK)","(+DIK)","(Sandy scene)","(Sarah scene)","","","","","","" ]
                        #[mod_gr][mod_choices[0]]
menu:
    "Underdressed":
        mc "You know... Underdressed."
        scene ep9_bella_branch109 with dissolve
        isa "I'm not going."
        mc "Bella, don't worry! Last year I heard most came as slutty nurses or something. You're fine!"
        scene ep9_bella_branch110 with dissolve
        isa "God... I'm a slutty mummy... Aren't I?"
        scene ep9_bella_branch109 with dissolve
        mc "You look great!"
    "Hot":
        mc "You know... Hot."
        scene ep9_bella_branch109 with dissolve
        isa "Aha... Good to know that there will be other hot chicks at your party."
        mc "Yeah!"
        scene ep9_bella_branch111 with dissolve
        $ renpy.pause()
    "Joke":
        mc "Like me. We're both leaving little to the imagination."
        scene ep9_bella_branch109 with dissolve
        isa "Ugh... This won't work."
    "Dodge the bullet ({font=fonts/collegiate.ttf}CHICK{/font} affinity) [mod_gr][mod_choices[0]]" if affinity == "CHICK":
        $ RPisabella += 1
        mc "I meant you have nothing to worry about. It's Halloween, and costumes like these are expected."
        scene ep9_bella_branch110 with dissolve
        isa "Are you sure?"
        mc "Absolutely!"
        scene ep9_bella_branch109 with dissolve
stop music fadeout 3
mc "Let's go. Trust me. The light is very dim."
scene ep9_bella_branch112 with dissolve
$ mphone_music_genre = 2
$ mphone_play_songs(["music/ep9/licensed_music/track115.mp3"])
isa "The decorations look nice."
scene ep9_bella_branch113 with dissolve
mc "Don't they? We rented a lot of them from this prop store."
mc "And we spent a long time making sure the mansion looked scary."
mc "Most of it, anyway. We limited the party to some rooms."
scene ep9_bella_branch114 with dissolve
isa "That camera in your room, what is it for?"
scene ep9_bella_branch115 with dissolve
mc "You know, taking pictures of people in their costumes."
mc "We should take one together later!"
scene ep9_bella_branch114 with dissolve
isa "We can do that. But right now, I need a drink if I'm gonna be able to pretend I'm a student."
scene ep9_bella_branch115 with dissolve
mc "I know the place to get one."
if ep9_body_shots or ep9_drinking_competition:
    jump ep9_diks_ph1_drinking_event_label

label ep9_bella_drink_cont_label:
play music "music/ep9/halloween_again.mp3"
scene ep9_bella_branch116 with dissolve
de "[mc_de_up]! Come! Sit down."
scene ep9_bella_branch117 with dissolve
de "And...hm... Who did you bring? I can't even guess..."
de "Is it Heather?"
scene ep9_bella_branch118 with dissolve
mc "No, it's not Heather. It's a mummy."
scene ep9_bella_branch119 with dissolve
de "Seriously, who are you?"
scene ep9_bella_branch120 with dissolve
isa "*{i}Low voice{/i}* A thirsty mummy."
scene ep9_bella_branch118 with dissolve
mc "It's Halloween, Derek. Let's have some mystery about who's who."
scene ep9_bella_branch121 with dissolve
de "Ah! Say no more! You're right, [mc_de]. You gotta appreciate people staying in character."
de "I don't know who that ghost out there is, either. But damn, she can drink!"
de "So...? What will it be?"
scene ep9_bella_branch122 with dissolve
mc "These drink names... Um... What do you recommend?"
de "Honestly, they're all horrible. But I'll make you something good."
scene ep9_bella_branch123 with dissolve
isa "Vodka fanny bullets?"
scene ep9_bella_branch124 with dissolve
de "Oh! A lady of culture?"
scene ep9_bella_branch125 with dissolve
mc "Don't go there."
scene ep9_bella_branch126 with dissolve
de "I recognize your voice... Damn... This is gonna kill me."
de "It's hard to tell if someone you knew is here since everyone is wearing costumes."
de "I've mistaken Leon for Lily at least three times already."
de "Did you see the HOTs yet?"
scene ep9_bella_branch128 with dissolve
mc "No, not yet. They should be here soon, though."
scene ep9_bella_branch127 with dissolve
de "Did you hear that Maya's with them now?"
scene ep9_bella_branch128 with dissolve
mc "Did she decide on that? Last I heard, she hadn't."
scene ep9_bella_branch127 with dissolve
de "Well, she's got the clothes and everything. I think it's only a matter of time."
scene ep9_bella_branch129 with dissolve
de "Here you go. Enjoy!"
scene ep9_bella_branch130 with dissolve
isa "These are...strong."
de "I'm still learning."
scene ep9_bella_branch131 with dissolve
mc "I think you're getting better. This drink both looks and tastes nice."
scene ep9_bella_branch132 with dissolve
de "Thanks! I've been reading up during class. Neither Philip nor Isabella caught me viewing videos instead of reading."
scene ep9_bella_branch134 with dissolve
isa "You don't say."
scene ep9_bella_branch133 with dissolve
de "Haha! Yeah, it's so fucking easy. I sneak my phone inside the book and pretend to read."
de "And then I nod and pretend to listen when they look my way."
scene ep9_bella_branch131 with dissolve
mc "Derek, uh... So... What's new with you?"
scene ep9_bella_branch132 with dissolve
de "Hold on, [mc_de]. I'm in the middle of explaining my tricks."
scene ep9_bella_branch133 with dissolve
de "Another thing I do is put a wireless headphone in one of my ears to listen to videos. I put my palm over the ear to cover it."
de "That way, I don't have to listen to them yap about what you can learn in five minutes if you just read the fucking book for yourself."
scene ep9_bella_branch135 with dissolve
de "I swear, there are so many ways to fool them. Another easy one is-"
scene ep9_bella_branch136
"The HOTs! The HOTs! They're finally here!"
scene ep9_bella_branch133 with dissolve
stop music fadeout 3
de "Let's continue this later. We need to check out the HOTs!"
jump ep9_wave2_label

label ep9_bella_lewd2_label:
if _in_replay:
    hide screen new_phone_screen
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
    $ ep9_jm_sad = False
    $ mphone_music_genre = 2
    $ ep8_jill_state = 0
$ mphone_play_songs(["music/ep9/licensed_music/track121.mp3"])

if ep9_jm_sad:
    scene ep9_bella_lewd1 with dissolve
    mc "*{i}Sigh{/i}*"
    scene ep9_bella_lewd2 with dissolve
    isa "What's wrong?"
    scene ep9_bella_lewd3 with dissolve
    mc "I had to deliver bad news to a couple of girls I've been dating."
    scene ep9_bella_lewd2 with dissolve
    isa "Funny."
    scene ep9_bella_lewd3 with dissolve
    mc "I'm serious."
    scene ep9_bella_lewd5 with dissolve
    isa "You are?"
    scene ep9_bella_lewd5b with dissolve
    mc "Yeah. I'd postponed it because they weren't in a good place before."
    mc "It felt like I would be piling more bad stuff on top of it, but I realized that dodging them and waiting for a perfect moment did the same."
    scene ep9_bella_lewd5c with dissolve
    isa "I'm confused. It sounds like you three were dating each other."
    scene ep9_bella_lewd5b with dissolve
    mc "Yeah, we were."
    scene ep9_bella_lewd5c with dissolve
    isa "I have a hunch... May I ask who they were?"
    scene ep9_bella_lewd5b with dissolve
    mc "I feel like I shouldn't tell because they are keeping their relationship a secret."
    scene ep9_bella_lewd5c with dissolve
    isa "Josy and Maya?"
    scene ep9_bella_lewd5d with dissolve
    mc "Promise not to tell anyone."
    scene ep9_bella_lewd5c with dissolve
    isa "I won't."
    scene ep9_bella_lewd5d with dissolve
    mc "How did you know?"
    scene ep9_bella_lewd5c with dissolve
    isa "Based on my conversations with them tonight and the drinking games..."
    isa "...it was clear to me that they think highly of you. And call it intuition, but it felt like there was something more to the words they were saying."
    scene ep9_bella_lewd5d with dissolve
    mc "It sucks... I never wanted to hurt them."
    mc "But I can't keep dating them because I'm sure I want to be with you."
    scene ep9_bella_lewd5c with dissolve
    isa "I can tell why they would be hurt. You seem to have a good impact on people."
    isa "Despite some of your flaws, you're a wonderful person."
    scene ep9_bella_lewd5d with dissolve
    mc "My flaws?"
    scene ep9_bella_lewd5c with dissolve
    isa "It was a compliment."
    scene ep9_bella_lewd5d with dissolve
    mc "Wrapped in an insult. What are my flaws?"
    scene ep9_bella_lewd5c with dissolve
    isa "You're a bit too sensitive and impulsive at times."
    scene ep9_bella_lewd5d with dissolve
    mc "Like when?"
    scene ep9_bella_lewd5c with dissolve
    isa "Like now."
    scene ep9_bella_lewd5d with dissolve
    mc "Oh... Haha..."
    mc "I'll try to work on it."
    scene ep9_bella_lewd5c with dissolve
    isa "Just be who you are, [name]."
    jump ep9_bella_lewd2b_label

scene ep9_bella_lewd1 with dissolve
$ wt_ep9_end_pick="Bella"
mc "*{i}Yawns{/i}*"
scene ep9_bella_lewd2 with dissolve
isa "Tired?"
scene ep9_bella_lewd3 with dissolve
if ep9_jm_sad or ep8_jill_state == 1:
    mc "Yeah, this party took a toll on me. It's been fun. It's been sad. It's been scary..."
    mc "So many emotions at once."
else:
    mc "Yeah, this party took a toll on me. It's been a great one...mostly."
mc "And now it's done. People are dropping off, one after another."
scene ep9_bella_lewd2 with dissolve
isa "Pussies."
scene ep9_bella_lewd4 with dissolve
mc "Haha! Aren't you hardcore?"
scene ep9_bella_lewd5 with dissolve
isa "I can go all night."
scene ep9_bella_lewd4 with dissolve
mc "You can?"
scene ep9_bella_lewd5 with dissolve
isa "No, I'm getting tired too."
label ep9_bella_lewd2b_label:
scene ep9_bella_lewd4 with dissolve
mc "Do you want to stay the night?"
scene ep9_bella_lewd5 with dissolve
isa "I want to evaluate your bed, so yes."
scene ep9_bella_lewd4 with dissolve
mc "It's not as good as yours."
mc "Shall we?"
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
scene ep9_bella_lewd6 with wipeleft
isa "I can't believe I made it the entire night."
scene ep9_bella_lewd7 with dissolve
mc "Were you serious about leaving early if you hadn't?"
scene ep9_bella_lewd8 with dissolve
isa "Oh, I was. When Sage found out it was me, I was on my way."
scene ep9_bella_lewd9 with dissolve
mc "Good thing she stopped you from leaving, huh?"
scene ep9_bella_lewd10 with dissolve
isa "I'll never hear the end of this night. Frankly, my biggest concern is your classmates."
scene ep9_bella_lewd11 with dissolve
mc "Who? Josy and Maya?"
scene ep9_bella_lewd12 with dissolve
isa "What kind of a teacher drinks shots with their students?"
scene ep9_bella_lewd11 with dissolve
mc "The best kind?"
scene ep9_bella_lewd12 with dissolve
isa "What kind of a teacher plays drinking games of a predominantly sexual nature with their students?"
scene ep9_bella_lewd11 with dissolve
mc "Uh... I think you're gonna have to tell me what I missed out on."
scene ep9_bella_lewd12 with dissolve
isa "That Sage, I tell you... Every question she aimed at me had a sexual undertone."
isa "And that only seemed to spur Josy on."
scene ep9_bella_lewd11 with dissolve
mc "And that's why you drank a lot?"
scene ep9_bella_lewd13 with dissolve
isa "I'm not going to tell my students my favorite sexual position or how many times I've had anal sex."
scene ep9_bella_lewd11 with dissolve
mc "Haha! They asked that!?"
scene ep9_bella_lewd10 with dissolve
isa "And I drank to all of it."
scene ep9_bella_lewd11 with dissolve
mc "Hey, I wanna know those things too."
scene ep9_bella_lewd13 with dissolve
isa "Well... You're my student too."
scene ep9_bella_lewd11 with dissolve
mc "Right..."
mc "Did you...uh...get around to checking that handbook yet?"
scene ep9_bella_lewd14 with dissolve
isa "No, I've been preoccupied with work and distracted by my issues with Jill... I'll do it next week."
stop music fadeout 3
scene ep9_bella_lewd15 with dissolve
$ renpy.pause()
scene ep9_bella_lewd16 with dissolve
mc "*{i}Smack{/i}*"
scene ep9_bella_lewd17 with dissolve
play music "music/ep6/licensed_music/track35.mp3"
isa "[name]..."
isa "*{i}Sigh{/i}*"
isa "Are we being...stupid?"
scene ep9_bella_lewd18 with dissolve
mc "A bit... But we're also being true to ourselves."
mc "Even though we had to jump through hoops to make it work, tonight proved it to me."
mc "I want to be with you."
scene ep9_bella_lewd19 with dissolve
mc "I want to talk to you, get close to you, dance with you..."
scene ep9_bella_lewd20 with dissolve
isa "Do you know how to waltz?"
scene ep9_bella_lewd21 with dissolve
mc "No."
scene ep9_bella_lewd20 with dissolve
isa "It's fine. You can do it the easy way too."
isa "Hold me."
scene ep9_bella_lewd22 with dissolve
isa "Let's rock back and forth like this, slowly."
mc "Is this the waltz?"
isa "Not quite. But it's better... It's more...sensual."
mc "I feel calm from doing it."
$ renpy.pause(13)
show screen click_to_continue_screen with dissolve
$ renpy.pause(2)
hide screen click_to_continue_screen with dissolve
$ renpy.pause()
stop music fadeout 3
scene ep9_bella_lewd23 with dissolve
isa "How about you put some music on for us?"
scene ep9_bella_lewd24 with dissolve
play music "music/ep9/licensed_music/track131.mp3"
queue music ["music/ep9/licensed_music/track132.mp3","music/ep9/licensed_music/track121.mp3","music/ep9/licensed_music/track131.mp3"]
hide screen new_phone_screen
isa "That's not exactly what I had in mind."
scene ep9_bella_lewd25 with dissolve
mc "Sorry, it's the playlist I had for the party."
mc "What do you want to listen to?"
scene ep9_bella_lewd24 with dissolve
isa "You know what? Keep playing it."
isa "I can dance to this too."
scene ep9_bella_lewd26 with dissolve
$ renpy.pause()
scene ep9_bella_lewd27 with dissolve
$ renpy.pause()
scene ep9_bella_lewd28 with dissolve
isa "Are you not going to join me?"
scene ep9_bella_lewd29 with dissolve
mc "I enjoy watching you do it."
scene ep9_bella_lewd30 with dissolve
mc "How do you still have so much energy left?"
scene ep9_bella_lewd31 with dissolve
isa "It must be a combination of the alcohol and this night with you."
scene ep9_bella_lewd32 with dissolve
isa "I can't put my finger on it... I feel like I'm 18 again."
scene ep9_bella_lewd33 with Dissolve(2)
$ renpy.pause()
scene ep9_bella_lewd34 with Dissolve(2)
$ renpy.pause()
scene ep9_bella_lewd35 with Dissolve(2)
$ renpy.pause()

scene ep9_bella_lewd36 with dissolve
mc "I would have loved to meet 18-year-old Bella."
scene ep9_bella_lewd37 with dissolve
isa "You were an infant back then."
scene ep9_bella_lewd36 with dissolve
mc "But now... It's like I have two 18-year-old Bellas."
scene ep9_bella_lewd38 with dissolve
isa "Haha!"
scene ep9_bella_lewd39 with dissolve
isa "Strip with me."
scene ep9_bella_lewd40 with dissolve
mc "Now, that's something I will join."
scene ep9_bella_lewd41 with dissolve
mc "All the way, huh?"
scene ep9_bella_lewd42 with dissolve
isa "Mhm..."
scene ep9_bella_lewd43 with dissolve
isa "*{i}Smack{/i}*"
scene ep9_bella_lewd44 with dissolve
$ renpy.pause()
scene ep9_bella_lewd45 with dissolve
$ renpy.pause()
scene anim_bella_dance_ep9 with dissolve
mc "You look good dancing like that."
mc "(She's so into it. It's like she's in a trance, haha...)"
mc "(Her sexy ass is jiggling all over the place. Damn...)"
mc "Dance closer to me..."
pause
scene anim_bella_dance2_ep9 with dissolve
mc "Mmmhff!!"
isa "Close enough?"
mc "*{i}Muffled{/i}* Just the way I like it."
isa "Does this make you horny? Having my ass squishing your face?"
mc "Yeah..."
isa "Then take it... Eat it..."
pause
label ep9_bella_lewd2a_loop_label:
menu:
    "Eat ass":
        scene anim_bella_lick_ep9 with dissolve
        isa "Hngn... Oh? You went there?"
        isa "Hnnn... [mc_isabella]..."
        jump ep9_bella_lewd2a_loop_label
    "Finger pussy":
        scene anim_bella_finger_ep9 with dissolve
        isa "Hngn... Yes, [mc_isabella]... Warm me up for you..."
        isa "Not too fast, ok? Starting slow feels much better for me."
        jump ep9_bella_lewd2a_loop_label
    "Continue":
        $ renpy.pause(0.5)
pause

scene ep9_bella_lewd46 with dissolve
isa "I've been waiting all night for this."
scene ep9_bella_lewd47 with dissolve
isa "*{i}Spits{/i}*"
scene anim_bella_hj2_ep9 with dissolve
mc "You have?"
isa "Well... After making out in the library, at least... That really got me going."
pause
scene anim_bella_hj_ep9 with dissolve
mc "Yeah, that was so hot. We should do that again."
isa "I couldn't do everything I wanted to do to you earlier... But now I'm going to."
pause

scene ep9_bella_lewd48 with dissolve
isa "Come here..."
scene ep9_bella_lewd49 with dissolve
label ep9_bella_lewd2_loop_label:
menu:
    "Handjob":
        scene anim_bella_hj3_ep9 with dissolve
        mc "*{i}Suck suck{/i}*"
        isa "Yes... Suck on my nipple, [mc_isabella]..."
        isa "You've got such a big and hard cock..."
        mc "*{i}Suck suck{/i}* Do what you want with it."
        isa "Oh, I will."
        isa "It's throbbing in my hand... And here I was thinking that you wouldn't have the energy for this."
        pause
        jump ep9_bella_lewd2_loop_label
    "Footjob":
        scene ep9_bella_lewd52c with dissolve
        mc "Can I?"
        isa "I'm not sure what you're referring to, but go ahead."
        scene ep9_bella_lewd52d with dissolve
        isa "Aha... You little weirdo."
        scene anim_bella_footjob_ep9 with dissolve
        mc "Is it that weird?"
        isa "As long as it feels good to you."
        mc "Fuck... Your feet are so smooth."
        isa "You're so kinky...and naughty..."
        pause
        jump ep9_bella_lewd2_loop_label
    "Blowjob":
        scene anim_bella_bj1_ep9 with dissolve
        isa "*{i}Suck suck{/i}*"
        mc "Ahhh... You're doing that so fucking good... Almost too good..."
        mc "It looks effortless... Why does that make it even hotter?"
        mc "I don't wanna cum early... Fuck..."
        pause
        scene ep9_bella_lewd51 with dissolve
        isa "*{i}Suck suck{/i}*"
        isa "(You make me feel so...young...)"
        scene ep9_bella_lewd50 with Dissolve(2.0)
        isa "*{i}Suck suck{/i}*"
        scene anim_bella_bj2_ep9 with dissolve
        mc "Ah... [isabella]... Suck my cock..."
        mc "You're loving it, aren't you?"
        isa "*{i}Suck suck{/i}* Mhm..."
        mc "Take it..."
        pause
        jump ep9_bella_lewd2_loop_label
    "Continue":
        $ renpy.pause(0.5)

scene ep9_bella_lewd53 with dissolve
isa "[mc_isabella]..."
isa "How do you want me?"
scene ep9_bella_lewd54 with dissolve
mc "Fuck... How do I even begin?"
$ tmpInt = 0
$ tmpBool3 = False
label ep9_bella_lewd2_loop2_label:
menu:
    "Doggystyle":
        $ tmpInt += 1
        scene ep9_bella_lewd54c with dissolve
        mc "Ok... Go like that. I wanna fuck you from behind."
        scene ep9_bella_lewd54b2 with dissolve
        $ renpy.pause()
        scene ep9_bella_lewd54b with dissolve
        mc "Ahhh..."
        isa "Mmm..."
        scene anim_bella_doggy1_ep9 with dissolve
        mc "This is such a sexy view, [isabella]..."
        isa "Push it all the way in..."
        mc "I am. It's not big enough for you?"
        isa "Hngn... It is... I just want to make sure you give me all of it."
        mc "It doesn't hurt when it's all in there?"
        isa "*{i}Moans{/i}* It's a good kind of pain..."
        pause
        scene anim_bella_doggy2_ep9 with dissolve
        mc "How can you stay arched like that for this long?"
        isa "Thank yoga for it."
        mc "Thank you, yoga!"
        pause
        jump ep9_bella_lewd2_loop2_label
    "Side":
        $ tmpInt += 1
        scene ep9_bella_lewd54d with dissolve
        mc "Lift your leg for me."
        scene anim_bella_side_ep9 with dissolve
        isa "*{i}Moans{/i}* Fuck me, [mc_isabella]."
        mc "I've been waiting all night for the chance to."
        isa "Mhm."
        pause
        scene anim_bella_side2_ep9 with dissolve
        isa "Yes, right there."
        pause
        jump ep9_bella_lewd2_loop2_label
    "From behind":
        $ tmpInt += 1
        scene anim_bella_doggy3_ep9 with dissolve
        isa "*{i}Moans{/i}* [mc_isabella]..."
        mc "(It seems like she's enjoying this a lot.)"
        mc "(That's good... My dick is tingling...)"
        pause
        scene anim_bella_doggy4_ep9 with dissolve
        mc "(Her wet pussy...and the way her ass is slapping against me...)"
        mc "(I could cum right now if I wanted to...)"
        pause
        jump ep9_bella_lewd2_loop2_label
    "Reverse cowgirl":
        $ tmpInt += 1
        scene ep9_bella_lewd54e with dissolve
        isa "Sit down. I want to ride you."
        scene ep9_bella_lewd54f with dissolve
        mc "Reversed?"
        isa "Yeah, I want to show you my hip rolls."
        scene ep9_bella_lewd54g with dissolve
        mc "Fuck..."
        scene anim_bella_rev1_ep9 with dissolve
        isa "*{i}Moans{/i}* The secret is to roll the hips while you're fully inside of me."
        mc "It feels way too good... Do you want me to finish like this?"
        isa "If you have to cum, you cum. But I'm not done with you yet."
        pause
        scene anim_bella_rev2_ep9 with dissolve
        mc "I can hold out a bit longer...I think."
        isa "Mhm..."
        pause
        if not tmpBool3:
            $ tmpBool3 = True
            scene bg anim_bella_slip_ep9 movie with dissolve
            mc "Fuck, it's so good..."
            isa "Ahhh! Wrong hole!"
            pause
            scene ep9_bella_lewd55 with dissolve
            isa "Ow! Ow! Ow!"
            scene ep9_bella_lewd56 with dissolve
            mc "Oh shit! Sorry!"
            scene ep9_bella_lewd57 with dissolve
            isa "*{i}Moans{/i}* Hngn... Ahhh..."
            scene ep9_bella_lewd58 with dissolve
            isa "I wasn't prepared for that..."
            isa "Did you do that on purpose?"
            scene ep9_bella_lewd59 with dissolve
            mc "Huh? Me? No, that was your fault. I slipped when you humped me."
            scene ep9_bella_lewd58 with dissolve
            isa "All right..."
        jump ep9_bella_lewd2_loop2_label
    "Cowgirl":
        $ tmpInt += 1
        scene anim_bella_ride1_ep9 with dissolve
        mc "Fuck me, [isabella]..."
        isa "Oh... [mc_isabella]..."
        pause
        scene ep9_bella_lewd60 with vpunch
        isa "*{i}Moans{/i}* Fuck!"
        scene ep9_bella_lewd60 with vpunch
        isa "Yes!"
        mc "Nice... Took you a while."
        scene anim_bella_ride2_ep9 with dissolve
        isa "No, that was rather fast."
        mc "Oh? And now you're back at it again. Were you always this energetic?"
        isa "I used to be even more."
        mc "I can't even imagine what that would have been like."
        pause
        scene ep9_bella_lewd55b with dissolve
        isa "But I still got it in me."
        scene anim_bella_ride3_ep9 with dissolve
        mc "Yeah, I can tell."
        pause
        scene anim_bella_ride4_ep9 with dissolve
        pause
        jump ep9_bella_lewd2_loop2_label
    "Cum" if tmpInt > 2:
        mc "I'm gonna...cum..."

menu:
    "In mouth":
        scene anim_bella_bj1_ep9 with dissolve
        mc "Get ready... Here it comes."
        scene ep9_bella_lewd61 at vpunch, cum1
        $ renpy.pause(0.5)
        scene ep9_bella_lewd61 at vpunch, cum1
        $ renpy.pause(0.5)
        scene ep9_bella_lewd61 at vpunch, cum1
        mc "Ahhh!!!"
        scene ep9_bella_lewd62 with dissolve
        $ renpy.pause()
        scene ep9_bella_lewd63 with dissolve
        isa "*{i}Gulp{/i}*"
        scene ep9_bella_lewd63b with dissolve
        isa "*{i}Lick lick{/i}*"
    "Facial":
        scene anim_bella_bj1_ep9 with dissolve
        mc "Get ready... Here it comes."
        scene anim_bella_bj_cum_ep9 with vpunch
        mc "Ahhh!!!"
        pause
        scene ep9_bella_lewd64 with dissolve
        mc "Wow... That's hot as fuck and a complete mess - both at once."
        scene ep9_bella_lewd64b with dissolve
        isa "You don't happen to have a towel in here, do you?"
        scene ep9_bella_lewd64 with dissolve
        mc "I'll get one for you."
    "On tits and belly":
        scene anim_bella_cum_ep9 with vpunch
        mc "Ahhh!!!"
        isa "Yes! Cum, [mc_isabella]! Cum!"
        scene ep9_bella_lewd65 with dissolve
        $ renpy.pause()
    "On ass":
        scene anim_bella_doggy4_ep9 with dissolve
        mc "I wanna cum all over your ass, [isabella]."
        isa "Do it. Cum! Cum all over me."
        scene ep9_bella_lewd66 at vpunch, cum2
        $ renpy.pause(0.5)
        scene ep9_bella_lewd66 at vpunch, cum2
        $ renpy.pause(0.5)
        scene ep9_bella_lewd66 at vpunch, cum2
        mc "Ahhh!!!"
        scene ep9_bella_lewd67 with dissolve
        $ renpy.pause()
    "Creampie":
        scene anim_bella_rev2_ep9 with dissolve
        mc "Can I cum inside?"
        isa "Yes, [mc_isabella]. I want to feel you ejaculate deep inside of me."
        scene ep9_bella_lewd68 at vpunch, cum1
        $ renpy.pause(0.5)
        scene ep9_bella_lewd68 at vpunch, cum1
        $ renpy.pause(0.5)
        scene ep9_bella_lewd69 at vpunch, cum1
        mc "Ahhh!!!"
        scene ep9_bella_lewd70 with dissolve
        $ renpy.pause()

scene ep9_bella_lewd71 with dissolve
mc "*{i}Phew{/i}* I don't know about you, but that was all the energy I had left in the tank."
isa "Mhm. Same..."
scene ep9_bella_lewd72 with dissolve
mc "What's that saying? I came, I saw, I conquered?"
scene ep9_bella_lewd73 with dissolve
isa "Veni, vidi, vici."
scene ep9_bella_lewd72 with dissolve
mc "Ah! Yes. Veni, vidi, vici..."
scene ep9_bella_lewd75 with dissolve
isa "Firstly, that's Latin, not Doric Greek, like Spartans spoke."
isa "Secondly, you're not Caesar. Thirdly, that's not how you use it."
isa "And finally... You didn't conquer anything."
scene ep9_bella_lewd74 with dissolve
mc "Veni?"
scene ep9_bella_lewd73 with dissolve
isa "Veni, too. Twice."
scene ep9_bella_lewd72 with dissolve
mc "Veni, veni?"
scene ep9_bella_lewd73 with dissolve
isa "Just stop."
scene ep9_bella_lewd72 with dissolve
mc "Ahh... That was a great end to this night. I needed it."
scene ep9_bella_lewd73 with dissolve
isa "It was. Will you be able to fall asleep?"
scene ep9_bella_lewd76 with dissolve
mc "*{i}Yawns{/i}* Within minutes from now. Having sex this late made me tired."
scene ep9_bella_lewd75 with dissolve
isa "I know that I wasn't optimistic about this night. But you nailed it."
scene ep9_bella_lewd76 with dissolve
mc "I'm happy that you trusted me. And moreover, that you had fun."
scene ep9_bella_lewd77 with dissolve
isa "This was likely the only party I'll be able to attend. You realize that, don't you?"
scene ep9_bella_lewd78 with dissolve
mc "Yeah... I have a hard time picturing more costume parties before next Halloween..."
scene ep9_bella_lewd79 with dissolve
$ renpy.pause()

$ renpy.end_replay()
$ persistent.ep9_lewd_isabella2 = True
$ calcScenes()
$ new_bio("Isabella", "I had sex with Bella in my room after the Halloween party, and she spent the night.")
$ mphone_stats_add_girl_s3("isabella","You had sex with Bella after the Halloween party in episode 9.")
stop music fadeout 3
show screen new_phone_screen
if "Bella" not in wt_ep9_scenes:
    $wt_ep9_scenes.append("Bella")

if wt_ep9_branch_numbers != 1:
    "See other scenes?"
    menu:
          "Josy & Maya" if branchMayaJosy and "Josy" not in wt_ep9_scenes:
            if "Josy" not in wt_ep9_scenes:
                $wt_ep9_scenes.append("Josy")
            jump ep9_jm_committing_label
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

label ep9_ending_isabella_label:
scene ep9_ending_isabella0 with dissolve
$ renpy.pause()
scene ep9_ending_isabella1 with dissolve
$ renpy.pause()
scene ep9_ending_isabella2 with dissolve
$ renpy.pause()
scene ep9_ending_isabella3 with dissolve
$ renpy.pause()
scene ep9_ending_isabella4 with dissolve
isa "Good morning."
scene ep9_ending_isabella5 with dissolve
mc "Morning."
mc "So? Was I right about the bed?"
scene ep9_ending_isabella4 with dissolve
isa "It's better than a mattress on the floor."
scene ep9_ending_isabella5 with dissolve
mc "But not as good as yours?"
scene ep9_ending_isabella6 with dissolve
isa "I slept very well in it."
scene ep9_ending_isabella7 with dissolve
$ renpy.pause()
scene ep9_ending_isabella8 with dissolve
mc "Can we stay here all day?"
isa "I fear not."
scene ep9_ending_isabella9 with dissolve
dikcs "*{i}Sings{/i}* She fucked a DIK! He came real quick! And now she does the walk!"
dikcs "*{i}Sings{/i}* What walk!?"
mc "Fuck..."
scene ep9_ending_isabella10 with dissolve
isa "They're doing that thing again."
scene ep9_ending_isabella11 with dissolve
mc "Yeah. You should leave through the window unless you want to wear your costume again."
scene ep9_ending_isabella10 with dissolve
isa "I think that's the best choice too."
scene ep9_ending_isabella12 with dissolve
$ renpy.pause()
scene ep9_ending_isabella13 with dissolve
mc "I'll call you."
scene ep9_ending_isabella14 with dissolve
isa "*{i}Smack{/i}*"
scene ep9_ending_isabella15 with dissolve
$ renpy.pause()
scene ep9_ending_isabella16 with dissolve
ni "Morning... Uh... Someone's in the bathroom..."
scene ep9_ending_isabella17 with dissolve
$ renpy.pause()
$ new_bio("Nick", "Nick saw me kiss Bella after I tried to sneak her out of my room.")
$ new_bio("Isabella", "Nick saw me kiss Bella after I tried to sneak her out of my room.")
jump ep9_ending2_label
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
