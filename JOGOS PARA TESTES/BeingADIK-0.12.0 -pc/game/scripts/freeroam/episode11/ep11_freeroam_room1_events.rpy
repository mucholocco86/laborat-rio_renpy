label ep11_freeroam_room1_intro_label:
$ mphone_music_genre = 3
$ mphone_play_songs(["music/ep9/relaxed.mp3"])
scene ep11_freeroam_room1 with dissolve
mc "..."
play sound "sound_effects/season2/basket_net.mp3"
scene ep11_freeroam_room2 with dissolve
$ renpy.sound.play("sound_effects/season2/basketball.mp3", channel="sfx2", loop=False)
mc "Hey. Do you have time? I feel we need to talk."
scene ep11_freeroam_room3 with dissolve
$ renpy.pause()
scene ep11_freeroam_room4 with dissolve
jb "Did you see that Nick left?"
scene ep11_freeroam_room3 with dissolve
mc "Where did he go?"
scene ep11_freeroam_room4 with dissolve
jb "I haven't the foggiest idea. I got back after class and wanted to check up on him, but he was gone."
jb "He took most of his belongings with him. It doesn't feel like he's coming back."
scene ep11_freeroam_room3 with dissolve
menu:
    "Good riddance":
        $ ep11_nick_attitude += 2
        scene ep11_freeroam_room5 with dissolve
        mc "Good riddance. Tommy had the right idea to banish him."
        scene ep11_freeroam_room6 with dissolve
        jb "I get why you're mad at Nick. You took some big blows yesterday..."
        $ new_bio("Nick", "I told John Boy it felt good that Nick didn't return to the frat.")
        $ new_bio("John Boy", "I told John Boy it felt good that Nick didn't return to the frat.")
    "I understand why":
        scene ep11_freeroam_room5 with dissolve
        mc "I understand why. I didn't want to come back here today, either."
        scene ep11_freeroam_room6 with dissolve
        jb "I can't blame you. You took some big blows yesterday..."
        $ new_bio("Nick", "I told John Boy I understood why Nick didn't return to the frat.")
        $ new_bio("John Boy", "I told John Boy I understood why Nick didn't return to the frat.")
if ep9_heather_lewd == 2:
    scene ep11_freeroam_room5 with dissolve
    mc "Listen... I should have told you the truth about Heather, but I couldn't do it."
    mc "You put me on the spot with that conversation, and I didn't know what to say."
    mc "I did a bad thing at that party."
    scene ep11_freeroam_room6 with dissolve
    jb "I understand why you didn't tell me, but I thought you trusted me more than that."
    jb "I'm not gonna lie to you. It hurt."
    scene ep11_freeroam_room5 with dissolve
    mc "You were talking about telling Tommy, and I panicked."
    if not ep11_tommy_admit and ep9_heather_lewd == 2 and ep10_nick_response == 4:
        scene ep11_freeroam_room7 with dissolve
        jb "I get it... But you trusted Nick with it. Not that it did you any good. So..."
        scene ep11_freeroam_room5 with dissolve
        mc "Yeah..."
    else:
        scene ep11_freeroam_room7 with dissolve
        jb "But you told Tommy."
        scene ep11_freeroam_room5 with dissolve
        mc "I had to. I didn't want Nick to get the full blame. Not that it did me any good."
scene ep11_freeroam_room7 with dissolve
jb "The things Nick said... There was a lot to digest."
scene ep11_freeroam_room6 with dissolve
jb "I wanna be upfront with you. I don't have cock envy."
jb "I made the mistake of telling him about some of my fantasies; that's all."
scene ep11_freeroam_room5 with dissolve
if ep8_elena_shot:
    mc "You already told me those things at the barbecue, so it wasn't news."
else:
    mc "What you fantasize about is up to you."
scene ep11_freeroam_room8 with dissolve
jb "Yeah, but I'm embarrassed... I don't want you to feel uncomfortable around me."
scene ep11_freeroam_room5 with dissolve
mc "I don't."
mc "I'm more worried that everyone in the frat secretly hates me."
scene ep11_freeroam_room7 with dissolve
jb "No one hates you."
scene ep11_freeroam_room5 with dissolve
if ep9_heather_lewd == 2:
    mc "Nick seems to, and Tommy should."
else:
    mc "Nick seems to."
mc "I was trying to help the frat out, not make myself look like a leader or a saint."
scene ep11_freeroam_room7 with dissolve
jb "I think those were Nick's words. They weren't mine, and I haven't heard anyone speak badly about what you did."
scene ep11_freeroam_room9 with dissolve
jb "Are you kidding me? Look at what you made us do."
if ep8_mansion_won:
    jb "Not only did you improve the mansion, you helped improve us."
else:
    jb "Not only did you try to improve the mansion, you helped improve us."

scene ep11_freeroam_room11 with dissolve
mc "Thanks... I needed to hear that."
if ep9_heather_lewd == 2:
    menu:
        "[m_c1]Apologize to him":
            $ ep11_apologize_jb = True
            mc "I'm sorry that I hurt you. It wasn't about you, though. I trust you."
            scene ep11_freeroam_room10 with dissolve
            jb "Thanks."
            $ new_bio("John Boy", "After the fight, I tried to talk it out with John Boy and explain why I didn't tell him about Heather. I apologized for hurting him.")
        "Don't apologize":
            $ ep11_apologize_jb = False
            $ new_bio("John Boy", "After the fight, I tried to talk it out with John Boy and explain why I didn't tell him about Heather.")
else:
    $ new_bio("John Boy", "After the fight, I tried to talk it out with John Boy.")
scene ep11_freeroam_room5 with dissolve
mc "I'm gonna talk to the rest when I get a chance."
mc "Things aren't what we thought they were with everything said last night."
scene ep11_freeroam_room12 with dissolve
jb "What do you mean?"
scene ep11_freeroam_room5 with dissolve
mc "I'm still figuring things out, but there has been some development."
mc "Tara wants us to apologize to her friends for one, and she claims they didn't post that cluck."
mc "And since Nick claims he didn't either, it doesn't make things any clearer."
mc "I'll let you know when I have more information."
if ep11_apologize_jb or ep9_heather_lewd != 2:
    scene ep11_freeroam_room13 with dissolve
    $ renpy.pause()
$ new_bio("John Boy", "He seemed bummed out that Nick had left the DIKs.")
jump ep11_freeroam_room1_label

label ep11_fr1_bella_call_label:
scene ep11_fr1_bella_call1 with dissolve
isa "Hi, [name]."
scene ep11_fr1_bella_call2 with dissolve
mc "Hey. I didn't get a chance to talk to you after English class, but I wanted to thank you for everything this weekend."
scene ep11_fr1_bella_call3 with dissolve
isa "It wasn't much, but I'm happy I could help."
isa "And I have to say, it's quite a colorful group of friends you have."
scene ep11_fr1_bella_call2 with dissolve
mc "You're one of us now."
scene ep11_fr1_bella_call4 with dissolve
isa "You think so?"
scene ep11_fr1_bella_call5 with dissolve
mc "Aren't you?"
scene ep11_fr1_bella_call6 with dissolve
if branchIsabella:
    isa "I suppose I am. Teacher, mentor, friend, us..."
else:
    isa "I suppose I am. Teacher, mentor, friend..."
isa "We've gotten quite close. It's something I didn't anticipate."
scene ep11_fr1_bella_call5 with dissolve
mc "You're needed. It felt like your place was a home where we could be ourselves and bond more."
scene ep11_fr1_bella_call6 with dissolve
isa "I'm glad."
isa "I've been thinking about what Sage said about celebrating more together."
scene ep11_fr1_bella_call7 with dissolve
isa "Would it be weird if we had a small Christmas party at my place?"
isa "It doesn't have to be on Christmas Eve, but getting together before that and maybe eating and talking would make everyone feel nice."
scene ep11_fr1_bella_call8 with dissolve
mc "I think that's a great idea. Are you up for it? I know how much effort it takes to host a party."
scene ep11_fr1_bella_call7 with dissolve
isa "I think I'll manage. Can I count on you to show up for it?"
scene ep11_fr1_bella_call9 with dissolve
mc "Unless my teacher forces me to study."
scene ep11_fr1_bella_call10 with dissolve
isa "I have a feeling she won't. I can't speak on behalf of Philip, though."
isa "But maybe your finals will pose a problem. I know how busy it gets in December for students."
scene ep11_fr1_bella_call9 with dissolve
mc "I'm sure we can make room for one dinner. We have to eat anyway. I'm up for it. Go ahead and check with the rest."
scene ep11_fr1_bella_call10 with dissolve
isa "I'll do that."
scene ep11_fr1_bella_call9 with dissolve
mc "Talk soon."
$ new_bio("Isabella", "After Sage sparked the idea of a Christmas party, Bella invited me to one at her place.")
$ task_list[3] = ""
$ updateTaskList()
jump endEvent

label ep11_fr1_sage_call_label:
scene ep11_fr1_sage_call1 with dissolve
$ renpy.pause()
if branchSage:
    scene ep11_fr1_sage_call9 with dissolve
    sa "Hey..."
    scene ep11_fr1_sage_call2 with dissolve
    mc "Hey... About last time..."
    scene ep11_fr1_sage_call11 with dissolve
    sa "Really? You're doing this over the phone?"
    scene ep11_fr1_sage_call2 with dissolve
    mc "Want me to come over?"
    scene ep11_fr1_sage_call11 with dissolve
    sa "On second thought, the phone is great. It gives me the choice to hang up on you."
    scene ep11_fr1_sage_call12 with dissolve
    
    if persistent.mod_wtenabled:
                        $mod_choices = ["(-2 Sage)","(-DIKS)","(-DIK)","(+DIK)","(+5 Josy)","(-5 Josy)","","","","","","" ]
                        #[mod_gr][mod_choices[0]]
                        #\n{size=-4}[m_c1][mod_choices[1]][m_c2][mod_choices[4]]
                        if not branchAlone:
                           $ mod_choices[6]="(+Cheater)"
                           $ mod_choices[7]="(+5 Cheater)"
    
    menu:
        "Apologize \n{size=-4}[m_c2][mod_choices[2]]":
            $ dk(-1)
            mc "I'm sorry for the way we ended the weekend. Everything was going great. Dad absolutely loved you, and I had to ruin it."
            mc "But I didn't do it on purpose."
            $ new_bio("Sage", "I apologized to Sage for how the weekend back home ended.")
        "Haven't done anything wrong \n{size=-4}[m_c1][mod_choices[0]][m_c2][mod_choices[3]]":
            $ dk(1)
            $ RPsage -= 2
            mc "I haven't done anything wrong."
            scene ep11_fr1_sage_call11 with dissolve
            sa "Yeah, I'm hanging up."
            scene ep11_fr1_sage_call2 with dissolve
            mc "Sage, let's talk about it. I don't want or need to have bad tension between us."
            mc "Why is it that you're this upset?"
            $ new_bio("Sage", "I told Sage that I hadn't done anything wrong with Zoey. She didn't like hearing that.")

    scene ep11_fr1_sage_call11 with dissolve
    sa "You talked to me about meeting your ex while I was stuck with you at your dad's place."
    scene ep11_fr1_sage_call3 with dissolve
    mc "Would it have been better if I didn't tell you that I was going to see her?"
    scene ep11_fr1_sage_call13 with dissolve
    sa "Do you want me to be honest? You're not gonna like it."
    scene ep11_fr1_sage_call14 with dissolve
    mc "Of course, I want to hear what you think."
    scene ep11_fr1_sage_call13 with dissolve
    sa "I don't even get why you feel like you have to see her at all."
    sa "To me, that screams you're not done with each other."
    scene ep11_fr1_sage_call3 with dissolve
    mc "I told you how I see it..."
    scene ep11_fr1_sage_call15 with dissolve
    sa "Yes, and I don't buy it."
    sa "Sure, you can be \"friends\" with your ex. Friends, as in you put up with having them around and make minor efforts with that friendship."
    sa "But you can't become someone's best friend after breaking up. That's just a convenient lie for something else."
    if ep9_derek_better_friend:
        scene ep11_fr1_sage_call5 with dissolve
        mc "She's not my best friend. That's Derek."
        scene ep11_fr1_sage_call15 with dissolve
        sa "Well... Yeah...but... Still, dude. Don't you see what I mean by any of this?"
    scene ep11_fr1_sage_call3 with dissolve
    mc "So, are you telling me I shouldn't see her at all?"
    scene ep11_fr1_sage_call16 with dissolve
    sa "I'm not saying that. My God! How can you be this oblivious to how I feel?"
    sa "You're usually great at it."
    scene ep11_fr1_sage_call3 with dissolve
    mc "Then what do you want?"
    scene ep11_fr1_sage_call17 with dissolve
    sa "I want you to understand how uncomfortable it makes me feel that you still spend time alone with her."
    scene ep11_fr1_sage_call5 with dissolve
    mc "I can tell that you feel that way now."
    mc "But you gotta understand, she was my first and only girlfriend. Sage, I have almost no experience with this..."
    scene ep11_fr1_sage_call18 with dissolve
    mc "And I have to say, I don't see it your way. You can stay good friends with your ex, especially when it wasn't a real relationship."
    mc "I meant it when I said she helped me get through bad times."
    mc "The friend she was to me when I was a kid helped me become who I am today. She's always been my support ever since I was bullied and didn't have any friends."
    scene ep11_fr1_sage_call2 with dissolve
    mc "I don't want you to worry about me and Zoey. We're just talking... In fact, it's been hard to do so since she returned."
    if ep9_mad_at_zoey:
        mc "I've been mad at her, and I'm not even sure if I can get over what she did."
    scene ep11_fr1_sage_call19 with dissolve
    sa "[name], it's her that I don't trust."
    scene ep11_fr1_sage_call20 with dissolve
    
    if persistent.mod_wtenabled:
                        $mod_choices = ["(+Sage)","(-DIKS)","(-DIK)","(+DIK)","(+5 Josy)","(-5 Josy)","","","","","","" ]
                        #[mod_gr][mod_choices[0]]
                        #\n{size=-4}[m_c1][mod_choices[1]][m_c2][mod_choices[4]]
                        if not branchAlone:
                           $ mod_choices[6]="(+Cheater)"
                           $ mod_choices[7]="(+5 Cheater)"
    
    menu:
        "You gotta trust me":
            scene ep11_fr1_sage_call5 with dissolve
            mc "Yeah, but you have to trust me. Isn't that how a relationship works?"
            mc "Zoey doesn't intend to get back together with me, and even if she did, it doesn't mean she calls the shots."
            mc "I have free will, and I chose to be with you."
            $ new_bio("Sage", "I told Sage that she had to trust me with Zoey.")
        "I understand that \n{size=-4}[m_c1][mod_choices[0]]":
            $ RPsage += 1
            mc "That's fair. I understand that."
            scene ep11_fr1_sage_call21 with dissolve
            sa "You do?"
            scene ep11_fr1_sage_call22 with dissolve
            mc "You don't know her like I do. If I were in your shoes, I would be suspicious, too."
            sa "..."
            $ new_bio("Sage", "I told Sage that I understood why she had trust issues with Zoey.")
    scene ep11_fr1_sage_call23 with dissolve
    sa "Why didn't you say these things when we started this argument!?"
    scene ep11_fr1_sage_call3 with dissolve
    mc "I didn't think it would turn into this big fight."
    if affinity == "DIK":
        mc "Is jealousy a big thing with you? Will I have to worry about talking to other girls, too?"
    else:
        mc "I think it's sweet that you're jealous; it shows that you care."
        mc "But...don't let it get to you. I don't want to feel like I can't talk to other girls."
    scene ep11_fr1_sage_call23 with dissolve
    sa "That's so not what this is, [name]."
    sa "Coming from the relationship with Chad that ended after a similar fight... It scares me."
    scene ep11_fr1_sage_call3 with dissolve
    mc "Fuck... I didn't even think about that."
    scene ep11_fr1_sage_call23 with dissolve
    sa "I'm not saying that you're cheating on me, but..."
    sa "That's something I didn't think Chad would do either."
    scene ep11_fr1_sage_call5 with dissolve
    mc "I'm not Chad, you know?"
    scene ep11_fr1_sage_call24 with dissolve
    sa "I know you're not."
    if jade_state > 0:
        scene ep11_fr1_sage_call4 with dissolve
        mc "(I'm worse than him...)"
        if ep4_toldDerekAboutJade:
            mc "(I ruined your family, and you don't even know it...)"
        else:
            mc "(I've managed to betray you before we even became a couple...)"
        mc "(What am I doing with her...?)"
    else:
        scene ep11_fr1_sage_call5 with dissolve
        mc "Promise to talk to me when you feel like this."
        mc "And I'll promise to think more about your feelings before I blurt things out."
        scene ep11_fr1_sage_call25 with dissolve
        sa "Deal..."
        sa "Now, the phone feels like a bad choice. I wanna hug you..."
        scene ep11_fr1_sage_call6 with dissolve
        mc "Me too. I'm happy we could talk it out."

    scene ep11_fr1_sage_call5 with dissolve
    mc "Speaking of Chad... There's a twofold reason why I called."
    mc "I need to get a hold of him. Can I have his number?"
    scene ep11_fr1_sage_call26 with dissolve
    sa "In what universe would you need his number?"
    scene ep11_fr1_sage_call5 with dissolve
    mc "I'm trying to sort out some arguments between the frats, and I think Chad can give me some answers."
    scene ep11_fr1_sage_call26 with dissolve
    sa "I'll share his contact info with you, but good luck trying to get any answers from him. He's a shut book."
    sa "No... Not just a shut book. He's like one of those diaries that teenage girls have with a lock on that they hide under their pillow."
    scene ep11_fr1_sage_call3 with dissolve
    mc "It's worth a try. You and I aren't the only ones who have been fighting."
    mc "The DIKs had a big one last night."
    scene ep11_fr1_sage_call27 with dissolve
    sa "About what?"
    scene ep11_fr1_sage_call3 with dissolve
    mc "It started with Heather cheating on Tommy with Nick, and then it became an even bigger fight because of other things."
    scene ep11_fr1_sage_call27 with dissolve
    sa "I suspected that would get ugly... Heather told me what she did..."
    sa "But what can you do? They set themselves up for that with their kind of relationship."
    scene ep11_fr1_sage_call2 with dissolve
    mc "Yeah... Nick left the DIKs today, and I'm not sure if he will return."
    scene ep11_fr1_sage_call26 with dissolve
    sa "He left?"
    scene ep11_fr1_sage_call5 with dissolve
    mc "It wasn't the only thing he was accused of. Like I said, it turned bigger."
    scene ep11_fr1_sage_call28 with dissolve
    if False:
        sa "Want me to come over?"
        scene ep11_fr1_sage_call3 with dissolve
        mc "No... Please don't. I'm busy...uh... I'll talk to you another time, ok?"
        scene ep11_fr1_sage_call29 with dissolve
        sa "Alright..."
        scene ep11_fr1_sage_call8 with dissolve
        mc "(Who am I kidding? I need to talk to someone about Sage...)"
        mc "(But one problem at a time... It must wait until I've dealt with the DIKs.)"
    else:
        sa "Ok, that settles it. This is too much for a phone call. I'm coming over."
        scene ep11_fr1_sage_call5 with dissolve
        mc "Are you sure?"
        scene ep11_fr1_sage_call28 with dissolve
        sa "Yeah, I still want that hug."
        scene ep11_fr1_sage_call6 with dissolve
        mc "Haha, ok. I'll be here."
else:
    scene ep11_fr1_sage_call10 with dissolve
    sa "[name]! What's up?"
    scene ep11_fr1_sage_call2 with dissolve
    mc "Too much."
    scene ep11_fr1_sage_call30 with dissolve
    sa "Uh oh. What did you do?"
    if jade_state > 0:
        scene ep11_fr1_sage_call4 with dissolve
        if ep4_toldDerekAboutJade:
            mc "(I ruined your family by fucking your mom.)"
        elif jade_state == 1:
            mc "(Started a sexual relationship with your mom that may have impacted your parents' relationship.)"
        else:
            mc "(Things with your mom that may have resulted in your parents' divorce.)"
    scene ep11_fr1_sage_call3 with dissolve
    mc "Believe it or not, but it's not so much me this time."
    mc "The DIKs had a big fight last night."
    scene ep11_fr1_sage_call27 with dissolve
    sa "About what?"
    scene ep11_fr1_sage_call3 with dissolve
    mc "It started with Heather cheating on Tommy with Nick, then it turned into an even bigger fight because of other things."
    scene ep11_fr1_sage_call27 with dissolve
    sa "I suspected that would get ugly... Heather told me what she did..."
    sa "But what can you do? They set themselves up for that with their kind of relationship."
    scene ep11_fr1_sage_call2 with dissolve
    mc "Yeah... Nick left the DIKs today, and I'm not sure if he will come back."
    scene ep11_fr1_sage_call26 with dissolve
    sa "He left?"
    scene ep11_fr1_sage_call5 with dissolve
    mc "It wasn't the only thing he was accused of. Like I said, it turned bigger."
    scene ep11_fr1_sage_call27 with dissolve
    sa "Damn... That sounds bad."
    scene ep11_fr1_sage_call5 with dissolve
    mc "Yeah, that's why I'm calling. I need your help with something."
    scene ep11_fr1_sage_call31 with dissolve
    sa "I doubt I can do much to help, but if you think otherwise... What do you need?"
    scene ep11_fr1_sage_call5 with dissolve
    mc "I need Chad's number."
    scene ep11_fr1_sage_call26 with dissolve
    sa "How do you go from Nick leaving the DIKs to asking me about Chad's number?"
    scene ep11_fr1_sage_call5 with dissolve
    mc "It would take me a long time to explain, and I am not even sure if I'm on the right track."
    mc "But I need to talk to him because he has some answers I need."
    scene ep11_fr1_sage_call26 with dissolve
    sa "I'll share his contact info with you, but good luck trying to get any answers from him. He's a shut book."
    sa "No... Not just a shut book. He's like one of those diaries that teenage girls have with a lock on that they hide under their pillow."
    scene ep11_fr1_sage_call3 with dissolve
    mc "It's a slim chance, but I have to try. Sitting around doing nothing won't help us."
    mc "So, how are you feeling today?"
    scene ep11_fr1_sage_call32 with dissolve
    sa "I feel like I embarrassed myself at Bella's."
    scene ep11_fr1_sage_call5 with dissolve
    mc "Come on, you didn't."
    scene ep11_fr1_sage_call32 with dissolve
    sa "It was stupid of me to drink that much when I had a hard time keeping my feelings to myself all day."
    scene ep11_fr1_sage_call5 with dissolve
    mc "That one, I won't argue. But everyone understood what you're going through."
    scene ep11_fr1_sage_call28 with dissolve
    sa "Did they ever... I can't believe how sweet they were to me."
    scene ep11_fr1_sage_call6 with dissolve
    mc "Feels good, huh? You're not alone in this."
    scene ep11_fr1_sage_call28 with dissolve
    sa "Yeah. Thank you."
    if branchJill:
        scene ep11_fr1_sage_call6 with dissolve
        mc "And thanks for stealing my girlfriend yesterday."
        scene ep11_fr1_sage_call34 with dissolve
        sa "Haha! You're welcome. If it makes you feel better, we had a great time."
        sa "But boy, did you fuck up or what?"
        scene ep11_fr1_sage_call7 with dissolve
        mc "I did?"
        scene ep11_fr1_sage_call35 with dissolve
        sa "Why the hell are you running off to your ex like that when you're with Jill?"
        scene ep11_fr1_sage_call3 with dissolve
        mc "That's not what it was."
        mc "Wait... Did Jill say I did that?"
        scene ep11_fr1_sage_call35 with dissolve
        sa "She told me what you told her, and I said it was ok to feel weird about it."
        scene ep11_fr1_sage_call7 with dissolve
        mc "What are you doing?"
        scene ep11_fr1_sage_call26 with dissolve
        sa "What am I doing? Look in the mirror."
        scene ep11_fr1_sage_call5 with dissolve
        mc "As I told Jill, Zoey is a childhood friend."
        scene ep11_fr1_sage_call35 with dissolve
        sa "And an ex-girlfriend. Stop being a moron, [name]. Can't you see why that would make Jill feel uncomfortable?"
        scene ep11_fr1_sage_call5 with dissolve
        mc "I didn't get the feeling she was completely against it. She seemed to understand why I was still seeing Zoey."
        scene ep11_fr1_sage_call33 with dissolve
        sa "Oh, [name]. It amazes me how you can be both emotionally smart and stupid."
        sa "Don't neglect my girl's feelings, ok?"
        scene ep11_fr1_sage_call7 with dissolve
        mc "She's your girl now?"
        scene ep11_fr1_sage_call34 with dissolve
        sa "Hell yeah, she is. And if you're not behaving, I will steal her from you."
        scene ep11_fr1_sage_call6 with dissolve
        mc "As much as I'd like to see you try, I am behaving."
        scene ep11_fr1_sage_call33 with dissolve
        sa "Good. I know it's not my place to speak for her, but she feels too shy to say it to you. Be more mindful."
        scene ep11_fr1_sage_call5 with dissolve
        mc "Thanks for letting me know. I had no idea she felt that way about it. I will."
        mc "Did you deal with your family yet?"
        scene ep11_fr1_sage_call32 with dissolve
        sa "No, but I'll deal with them soon. I know I can't escape it."
        $ new_bio("Sage", "Sage told me to care more about Jill's feelings after I had missed that Jill was upset about Zoey.")
        $ new_bio("Jill", "Sage told me to care more about Jill's feelings after I had missed that Jill was upset about Zoey.")
    else:
        scene ep11_fr1_sage_call5 with dissolve
        mc "Did you deal with it yesterday?"
        scene ep11_fr1_sage_call33 with dissolve
        sa "No. Jill and I had our nails done."
        scene ep11_fr1_sage_call5 with dissolve
        mc "Oh? You two hung out?"
        scene ep11_fr1_sage_call33 with dissolve
        sa "Yeah, she offered to show me the place where she frequents. We made a date out of it."
        sa "It was a nice distraction. She's a lot of fun."
        scene ep11_fr1_sage_call6 with dissolve
        mc "That's nice."
        scene ep11_fr1_sage_call32 with dissolve
        sa "I'll deal with my family soon. I know I can't escape it."
    sa "Good luck with Chad."
    scene ep11_fr1_sage_call6 with dissolve
    mc "Thanks again."
    if jade_state > 0:
        scene ep11_fr1_sage_call8 with dissolve
        mc "(Who am I kidding? I need to talk to someone about Sage...)"
        mc "(But one problem at a time... It must wait until I've dealt with the DIKs.)"

$ new_bio("Sage", "Sage gave me Chad's number but told me not to expect any answers from him.")
$ task_list[0] = "Contact Chad"
$ updateTaskList()
$ mphone_contact_list.insert(1,["Chad","NONE",False])
$ mphone_chat_history_list.insert(1,["Chad",0,[],[]," ",0])
$ new_chat_msg("Chad",False,1)

jump endEvent

label ep11_fr1_end_label:
$ tmpInt = 0
$ tmpInt2 = 0
$ text_message_screen_list = []
$ text_message_screen_list.append(["Isabella","Jill and Sage said yes. Derek was busy pleasuring himself when I called... I think I will handle this communication via text message from now on.",True])
$ text_message_screen_list.append(["%s" % name,"Derek...",False])
$ text_message_screen_list.append(["Isabella","Quite the character, that one.",True])
$ text_message_screen_list.append(["%s" % name,"Imagine living with him. mphone_emoji_smile",False])
hide screen new_phone_screen
scene ep11_fr1_end1 with dissolve
show screen text_message_screen
play sound "sound_effects/interlude/zoey_message.mp3"
$ renpy.pause()
scene ep11_fr1_end2 with dissolve
$ tmpInt += 1
$ renpy.pause()
$ tmpInt += 1
$ renpy.pause()
$ tmpInt += 1
$ renpy.pause()
hide screen text_message_screen
$ mphone_scene_to_chat("Isabella",text_message_screen_list)
if (not branchSage or (branchSage and jade_state > 0)) and not ep4_toldDerekAboutJade:
    stop music fadeout 3
scene ep11_fr1_end3 with dissolve
$ renpy.pause()
show screen new_phone_screen
if ep4_toldDerekAboutJade:
    scene ep11_fr1_end4 with dissolve
    mc "Rusty?"
    scene ep11_fr1_end5 with dissolve
    mc "(He's still in school.)"
    scene ep11_fr1_end6 with dissolve
    $ renpy.pause()
    play sound "sound_effects/season3/type1.mp3"
    scene ep11_fr1_end7 with dissolve
    mc "(The DIK evaluation pictures and videos are still here in Derek's and my folder...)"
    mc "(It's too late for it now, but I don't care. I'm deleting that video before it causes more damage.)"
    play sound "sound_effects/season3/type2.mp3"
    scene ep11_fr1_end8 with dissolve
    mc "(Rusty restricted access to most folders after the Rooster incident... Only the folder owners have access... But even if access weren't restricted, I doubt I'd find anything useful.)"
    mc "(If the video leaked after Rusty changed the permissions, it means it was either Rusty or Derek who sent that...)"
    mc "(But I trust both of them. The video must have leaked before that...)"
    mc "(The pictures sent to Chad and Dawe are likely in the other guys' folders. But I can't access any of them...)"
    if not branchSage or (branchSage and jade_state > 0):
        stop music fadeout 3
    scene ep11_fr1_end9 with dissolve
    $ renpy.pause()

if not branchSage:
    jump ep11_zoey_call_label
scene ep11_fr1_sage_end1 with dissolve
$ renpy.pause()
scene ep11_fr1_sage_end2 with dissolve
$ renpy.pause()
scene ep11_fr1_sage_end3 with dissolve
sa "I'm sorry for that stupid fight."
scene ep11_fr1_sage_end2 with dissolve
mc "Me too. I don't want to fight with you."
scene ep11_fr1_sage_end4 with dissolve
sa "Let's move past it."
sa "So... Tell me what happened yesterday."
if affinity == "DIK":
    stop music fadeout 3
scene ep11_fr1_sage_end5 with dissolve
mc "Let's sit down in my room."
if affinity != "DIK":
    $ RPsage += 1
    mc "But first..."
    scene ep11_fr1_sage_end8 with dissolve
    mc "I don't know a lot about nails or cosmetics, but they look pretty."
    mc "They match your eyes."
    stop music fadeout 3
    scene ep11_fr1_sage_end6 with dissolve
    sa "I can't believe you noticed... Thank you."
    scene ep11_fr1_sage_end7 with dissolve
    $ renpy.pause()
jump ep11_zoey_call_label

label ep11_fr_room_jacob_label:
scene ep11_fr_room_jacob1 with dissolve
jac "Good, you're here."
scene ep11_fr_room_jacob2 with dissolve
mc "Yeah, I am."
scene ep11_fr_room_jacob3 with dissolve
jac "I had to make sure you hadn't left."
scene ep11_fr_room_jacob2 with dissolve
mc "Like Nick?"
scene ep11_fr_room_jacob3 with dissolve
jac "I was here when he bounced. I tried to stop him, but he was still fuming."
jac "He grabbed what he could carry and was gone without saying a word."
scene ep11_fr_room_jacob4 with dissolve
mc "He needs to cool down..."
scene ep11_fr_room_jacob5 with dissolve
jac "I don't think that would matter. The guy single-handedly managed to trash this mansion worse than the jocks did with his words and actions."
scene ep11_fr_room_jacob6 with dissolve
mc "Do you think he had a part in what they did?"
scene ep11_fr_room_jacob5 with dissolve
jac "With his room being left untouched?"
jac "Maybe Nick did clean it up and his windows were spared for some reason."
jac "I don't know what to believe. How do you make sense of a big mess?"
scene ep11_fr_room_jacob7 with dissolve
jac "I can't even believe what I heard him say last night."
jac "The guy was always laid back and chill. Sure, he had his views, issues, and such, but he was never pushy about anything."
scene ep11_fr_room_jacob8 with dissolve
jac "Seeing him snap like he did... It was like he was a completely different dude."
jac "Throwing people under the bus left and right like that..."
scene ep11_fr_room_jacob9 with dissolve
menu:
    "He can't be trusted":
        $ ep11_nick_attitude += 1
        mc "Yeah. It shows he can't be trusted. He was ready to take everyone down with him."
        $ new_bio("Nick", "I told Jacob that Nick couldn't be trusted.")
    "He felt cornered":
        mc "It doesn't excuse what he said, but he must have felt cornered. Everyone handles that kind of situation differently."
        $ new_bio("Nick", "I told Jacob that Nick must have felt cornered during the fight.")

scene ep11_fr_room_jacob12 with dissolve
jac "Bro, I'm not cool with what he said, but I won't try to defend myself. I told him those things about Heather and Zoey."
jac "I told him I'd plow Zoey like a Canadian driveway in December."
scene ep11_fr_room_jacob9 with dissolve
if ep10_zoey_jacob:
    mc "You don't have to make it worse, Jacob. I'm aware of it, and you know I was ok with it, too."
else:
    mc "You don't have to make it worse, Jacob. I'm aware of it."
scene ep11_fr_room_jacob8 with dissolve
jac "Still. I'm putting it out there because I don't want things to be said behind your back like that. I have no problem saying those things to your face."
jac "And I don't know who the hell told him we're jealous about your dick and shit...but it's not me. I have zero problems with my cock."
scene ep11_fr_room_jacob9 with dissolve
mc "What about bossing you guys around...? Did I do that?"
scene ep11_fr_room_jacob11 with dissolve
jac "Yeah, you were a mean Karen bitch about that."
jac "How dare you tell us to work and help out? You should have sucked it up and done all of it by yourself."
scene ep11_fr_room_jacob10 with dissolve
mc "Hahaha..."
scene ep11_fr_room_jacob11 with dissolve
jac "Nah. You've always been a good one in my book. Ever since I met you, I knew there was something special I liked about you."
jac "Sure, I have had some doubts recently, but thinking about it, you haven't proven me wrong on anything I originally thought about you."
jac "Don't let what Nick said get to you."
jac "We cool, yeah?"
scene ep11_fr_room_jacob10 with dissolve
mc "Yeah. We're cool."
play sound "sound_effects/season2/fistbump.mp3"
scene ep11_fr_room_jacob13 with hpunch
$ renpy.pause()
$ new_bio("Jacob", "I patched things up with Jacob after the fight.")
$ task_list[1] = ""
$ updateTaskList()
jump endEvent

label ep11_fish_label:
scene ep11_fish1 with dissolve
$ ft_nick_money = ft_money
$ ft_money = 0
mc "(So, if Nick's gone... That means you guys need me more than ever.)"
mc "(Nick was in charge of the budget... So, that money is lost.)"
mc "(And we're back to square one. Fuck... Can I even afford to keep you guys alive?)"
jump endEvent

label ep11_gifts_label:
mc "(I wanna buy some Christmas gifts this year, but I don't think I can afford a lot.)"
mc "(I've got some time to plan, but not a lot. I should start putting money aside for the Christmas shopping now.)"
$ renpy.block_rollback()
call screen giftMsgScreen
$ renpy.pause(0.5)


$ specialMessage = "{size=-%d}Click the notepad to plan Christmas gifts further.{/size}" % (5 * persistent.scale_factor)
show screen specialmsglong
$ renpy.pause(3)
hide screen specialmsglong
$ task_list[2] = ""
$ updateTaskList()
$ currentFreeRoamLabel = "ep11_library_desk2_label"
jump endEvent

label ep11_derek_shop:
$ renpy.block_rollback()
$ phone_call_enabled = False
if assman:
    scene ep11_derek_shop1b with dissolve
else:
    scene ep11_derek_shop1 with dissolve
de "Hey... Kinda in the middle of something here."
if assman:
    scene ep11_derek_shop2 with dissolve
else:
    scene ep11_derek_shop2b with dissolve
mc "I just wanted to ask you for some study advice."
de "What do you need?"
show screen newmoneymsg
call screen shop_derek_screen
$ renpy.pause(0.5)
hide screen newmoneymsg
de "Fuck, I gotta go."
jump endEvent

label ep11_magnar_shop:
$ renpy.block_rollback()
$ phone_call_enabled = False
scene ep11_magnar_shop1 with dissolve
mg "How is everything, [name]? Need something?"
scene ep11_magnar_shop2 with dissolve
show screen newmoneymsg
call screen shop_magnar_screen
$ renpy.pause(0.5)
hide screen newmoneymsg
scene ep11_magnar_shop1 with dissolve
mg "Take care."
jump endEvent

label ep11_madame_label_shop:
stop music fadeout 3
scene black with fade
$ renpy.pause(2)
scene ep7_madame_1 with dissolve
play music "music/ep7/licensed_music/track53.mp3"
queue music ["music/ep7/licensed_music/track53.mp3","music/ep6/licensed_music/track34.mp3"]
md "If it isn't [name]..."
scene ep7_madame_2 with dissolve
md "Welcome back, love. How can [madame] satisfy you?"
if "Visit Madame Rose" in optional_task_list:
    $ optional_task_list.remove("Visit Madame Rose")
    $ updateTaskList()
jump ep11_madame_label

label ep11_madame_label:
$ currentEvent = "ep11_madame_label"
scene anim_madame_main_ep7 with dissolve
label ep11_madame_loop_label:
show screen newmoneymsg
menu:
    "Dances":
        menu:
            "Exotic dance #1":
                hide screen newmoneymsg
                jump ep7_madame_dance1_label
            "Back":
                jump ep11_madame_loop_label
    "Teasing":
        menu:
            "[ep7_madame_options_list[1][0]]" if (ep7_madame_options_list[1][0] == "Groping {color=#36ca2b}${/color}" and money > 0) or ep7_madame_options_list[1][0] != "Groping {color=#36ca2b}${/color}":
                if ep7_madame_options_list[1][0] == "Groping {color=#36ca2b}${/color}":
                    jump ep7_madame_buy_groping_label
                hide screen newmoneymsg
                jump ep7_madame_groping_label
            "[ep7_madame_options_list[1][1]]" if (ep7_madame_options_list[1][1] == "Suck tits {color=#36ca2b}$$${/color}" and money > 2) or ep7_madame_options_list[1][1] != "Suck tits {color=#36ca2b}$$${/color}":
                if ep7_madame_options_list[1][1] == "Suck tits {color=#36ca2b}$$${/color}":
                    jump ep7_madame_buy_suck_tits_label
                hide screen newmoneymsg
                jump ep7_madame_suck_tits_label
            "[ep7_madame_options_list[1][2]]" if (ep7_madame_options_list[1][2] == "Lick pussy {color=#36ca2b}$$${/color}" and money > 2) or ep7_madame_options_list[1][2] != "Lick pussy {color=#36ca2b}$$${/color}":
                if ep7_madame_options_list[1][2] == "Lick pussy {color=#36ca2b}$$${/color}":
                    jump ep8_madame_buy_pussylick_label
                hide screen newmoneymsg
                jump ep8_madame_pussylick_label
            "Back":
                jump ep11_madame_loop_label
    "Lewd scenes":
        menu:
            "[ep7_madame_options_list[2][0]]" if (ep7_madame_options_list[2][0] == "Blowjob {color=#36ca2b}$$$${/color}" and money > 3) or ep7_madame_options_list[2][0] != "Blowjob {color=#36ca2b}$$$${/color}":
                if ep7_madame_options_list[2][0] == "Blowjob {color=#36ca2b}$$$${/color}":
                    jump ep7_madame_buy_bj_label
                hide screen newmoneymsg
                jump ep7_madame_bj_label
            "[ep7_madame_options_list[2][1]]" if (ep7_madame_options_list[2][1] == "Assjob {color=#36ca2b}$$$${/color}" and money > 3) or ep7_madame_options_list[2][1] != "Assjob {color=#36ca2b}$$$${/color}":
                if ep7_madame_options_list[2][1] == "Assjob {color=#36ca2b}$$$${/color}":
                    jump ep8_madame_buy_assjob_label
                hide screen newmoneymsg
                jump ep8_madame_assjob_label
            "[ep7_madame_options_list[2][2]]" if (ep7_madame_options_list[2][2] == "Footjob {color=#36ca2b}${/color}" and money > 0) or ep7_madame_options_list[2][2] != "Footjob {color=#36ca2b}${/color}":
                if ep7_madame_options_list[2][2] == "Footjob {color=#36ca2b}${/color}":
                    jump ep10_madame_footjob_buy_label
                hide screen newmoneymsg
                jump ep10_madame_footjob_lewd_label
            "[ep7_madame_options_list[2][3]]" if (ep7_madame_options_list[2][3] == "Boobjob {color=#36ca2b}$${/color}" and money > 1) or ep7_madame_options_list[2][3] != "Boobjob {color=#36ca2b}$${/color}":
                if ep7_madame_options_list[2][3] == "Boobjob {color=#36ca2b}$${/color}":
                    jump ep10_madame_boobjob_buy_label
                hide screen newmoneymsg
                jump ep10_madame_boobjob_lewd_label
            "[ep7_madame_options_list[2][4]]" if (ep7_madame_options_list[2][4] == "Vaginal sex {color=#36ca2b}$$$${/color}" and money > 3) or ep7_madame_options_list[2][4] != "Vaginal sex {color=#36ca2b}$$$${/color}":
                if ep7_madame_options_list[2][4] == "Vaginal sex {color=#36ca2b}$$$${/color}":
                    jump ep10_madame_fuck_buy_label
                hide screen newmoneymsg
                jump ep10_madame_fuck_lewd_label
            "[ep7_madame_options_list[2][5]]" if (ep7_madame_options_list[2][5] == "Anal sex {color=#36ca2b}$$$$${/color}" and money > 4) or ep7_madame_options_list[2][5] != "Anal sex {color=#36ca2b}$$$$${/color}":
                if ep7_madame_options_list[2][5] == "Anal sex {color=#36ca2b}$$$$${/color}":
                    jump ep11_madame_anal_buy_label
                hide screen newmoneymsg
                jump ep11_madame_anal_lewd_label
            "Back":
                jump ep11_madame_loop_label
    "Done":
        hide screen newmoneymsg
        stop music fadeout 3
        mc "I think I better be going."
        scene ep7_madame_16 with dissolve
        md "It's sad to see you go, but I look forward to your next visit."
        $ mphone_next_song()
        jump endEvent

label ep11_madame_anal_buy_label:
$ renpy.block_rollback()
$ mny(-5)
$ ep7_madame_options_list[2][5] = "Anal sex"
hide screen newmoneymsg
mc "Can I fuck your ass? I'd pay a lot to do it."
scene ep7_madame_16 with dissolve
md "With that big cock... Hm... I don't know."
scene anim_madame_main_ep7 with dissolve
mc "I won't be too rough. I promise."
scene ep7_madame_16 with dissolve
md "Ok... For {color=#36ca2b}$$$$${/color}, I'll let you penetrate it."
jump ep11_madame_anal_lewd_label

label ep11_madame_anal_lewd_label:
if _in_replay:
    hide screen new_phone_screen
    if persistent.name == None:
        $ name = "MC"
    else:
        $ name = persistent.name
    $ madame = "Madame"
    play music "music/ep7/licensed_music/track53.mp3"
    queue music ["music/ep7/licensed_music/track53.mp3","music/ep6/licensed_music/track34.mp3"]
    hide screen new_phone_screen

scene ep7_madame_16 with dissolve
md "If I can make a suggestion, we could use the pole to fuck. I have some tricks I'd like to show you."
md "Or, if you'd like, I'd happily sit down on that huge cock of yours, too."
md "How do you prefer me?"
scene anim_madame_main_ep7 with dissolve
menu:
    "Use the pole":
        mc "You piqued my curiosity with the pole. Show me what you got."
        jump ep11_madame_anal_lewd_pole_label
    "Madame on top":
        mc "I'd love to have you sit down on me with your incredible ass."
        jump ep11_madame_anal_lewd_top_label


label ep11_madame_anal_lewd_pole_label:
scene ep11_madame_anal_lewd2 with dissolve
md "Come over here."
md "I've spent years pole dancing and have picked up a thing or two while doing it."
scene ep11_madame_anal_lewd3 with dissolve
md "*{i}Moans{/i}*"
scene anim_madame_anal5_ep11 with dissolve
pause
scene anim_madame_anal6_ep11 with dissolve
pause
scene anim_madame_anal7_ep11 with dissolve
pause
scene anim_madame_anal8_ep11 with dissolve
pause

menu:
    "Madame on top":
        jump ep11_madame_anal_lewd_top_label
    "Cum":
        menu:
            "Creampie":
                scene ep11_madame_anal_lewd6 at vpunch, cum1
                $ renpy.pause(0.5)
                scene ep11_madame_anal_lewd6 at vpunch, cum1
                $ renpy.pause(0.5)
                scene ep11_madame_anal_lewd6 at vpunch, cum1
                mc "Fuck!!! Ahh..."
                scene ep11_madame_anal_lewd7 with dissolve
                md "Mmm... I can feel that warm sticky cum all inside my ass."
            "On ass":
                scene anim_madame_anal6_ep11 with dissolve
                pause
                scene ep11_madame_anal_lewd4 at vpunch, cum2
                $ renpy.pause(0.5)
                scene ep11_madame_anal_lewd4 at vpunch, cum2
                $ renpy.pause(0.5)
                scene ep11_madame_anal_lewd4 at vpunch, cum2
                mc "Fuck!!! Ahh..."
                scene ep11_madame_anal_lewd5 with dissolve
                md "Mmm... I can feel that warm sticky cum all over my ass."
        md "I take it I satisfied you."
        mc "That's an understatement... Fuck... That was so good."

jump ep11_madame_anal_after_label

label ep11_madame_anal_lewd_top_label:
scene ep11_madame_anal_lewd1 with dissolve
md "Mmm... Let [madame] put that cock in for you."
md "I know I hesitated when you asked me to do this, but don't overthink it."
md "Your satisfaction is my guarantee."
scene anim_madame_anal1_ep11 with dissolve
md "*{i}Moans{/i}* Fuck my ass."
pause
scene anim_madame_anal2_ep11 with dissolve
pause
scene anim_madame_anal3_ep11 with dissolve
pause
scene anim_madame_anal4_ep11 with dissolve
pause

menu:
    "Use pole":
        jump ep11_madame_anal_lewd_pole_label
    "Cum":
        scene anim_madame_anal3_ep11 with dissolve
        $ renpy.pause()
        scene ep11_madame_anal_lewd8 at vpunch, cum1
        $ renpy.pause(0.5)
        scene ep11_madame_anal_lewd8 at vpunch, cum1
        $ renpy.pause(0.5)
        scene ep11_madame_anal_lewd8 at vpunch, cum1
        mc "Fuck!!! Ahh..."
        scene ep11_madame_anal_lewd9 with dissolve
        md "Mmm... I can feel that warm sticky cum all inside my ass."
        md "I take it I satisfied you."
        mc "That's an understatement... Fuck... That was so good."
        jump ep11_madame_anal_after_label

label ep11_madame_anal_after_label:
$ renpy.end_replay()
$ persistent.ep11_lewd_madame = True
$ calcScenes()
$ renpy.jump(currentEvent)
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
