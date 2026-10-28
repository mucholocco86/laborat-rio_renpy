label ep11_shome_label:
scene ep11_shome1 with wipeleft
$ renpy.pause()
scene ep11_shome2 with dissolve
sa "What a night... Your dad sure knows how to talk."
scene ep11_shome3 with dissolve
mc "I think he gets lonely being at home alone too much."
scene ep11_shome2 with dissolve
sa "Ah... He's not dating?"
scene ep11_shome4 with dissolve
mc "Dating? I'm not opening that door. He's never shown any interest in doing that."
scene ep11_shome5 with dissolve
sa "Why do you think that is?"
scene ep11_shome6 with dissolve
mc "I believe it's because of Mom, but I don't know for sure. We don't talk about it."
scene ep11_shome5 with dissolve
sa "That's sad... You two seem to talk about everything else. I find it odd that you can't talk to him about that."
scene ep11_shome6 with dissolve
mc "It's a sensitive topic."
mc "Trust me; nothing would make me happier than to see him date someone. But I'm not gonna force him to do that."
scene ep11_shome7 with dissolve
mc "Also, I think he's set in his ways by now. Even though he's lonely at home, he's got friends at work."
mc "It would take a lot for him to break his habits and start dating someone."
scene ep11_shome8 with dissolve
sa "Still, he's a great guy and not too old to date."
sa "It makes me sad that he has given up on that."
scene ep11_shome9 with dissolve
mc "Yeah... What can I say?"
scene ep11_shome10 with dissolve
sa "Anyway... Your dad is awesome."
scene ep11_shome11 with dissolve
mc "Told you."
scene ep11_shome12 with dissolve
sa "It seems like awesome runs in the family."
scene ep11_shome13 with dissolve
sa "*{i}Smack{/i}*"
scene ep11_shome14 with dissolve
sa "Thanks for bringing me here today. It completely took my mind off...you know?"
scene ep11_shome15 with dissolve
mc "I'm happy it did. Did you hear anything from your family?"
scene ep11_shome16 with dissolve
sa "I got a text from my brother crying about the divorce. If you think I'm upset...you should see him."
scene ep11_shome17 with dissolve
if affinity == "DIK" or not ep10_tybalt_mercy:
    $ RPsage -= 1
    mc "Good. He deserves to feel like shit."
    scene ep11_shome19 with dissolve
    sa "*{i}Groans{/i}* That's a bit..um..."
else:
    mc "Wow, I didn't know he had those emotions in him."
    scene ep11_shome16 with dissolve
sa "He's not crying because our family is splitting up; he's crying because it affects him and our reputation."
sa "And part of the crying was probably related to the sedatives after his surgery."
scene ep11_shome17 with dissolve
mc "Did he have surgery?"
scene ep11_shome18 with dissolve
sa "Mom told me he tore his scrotum somehow. I didn't want to ask more about it, but it was serious."
scene ep11_shome17 with dissolve
mc "Is he all right?"
scene ep11_shome18 with dissolve
sa "Yeah, he will be."
scene ep11_shome19 with dissolve
sa "Ugh... I will have to deal with Mom and Dad sooner rather than later, but taking a few days off from thinking about it has been good."
sa "Tomorrow, Jill will help me do that, too."
scene ep11_shome20 with dissolve
mc "I wasn't aware that you two hung out."
scene ep11_shome21 with dissolve
sa "We haven't been. But Jill's gonna show me where she gets her nails done, and we figured why not spend time together."
if ep9_jill_mood == 1:
    if not ep9_jm_sad:
        scene ep11_shome23 with dissolve
        mc "You know I dated her, right?"
        scene ep11_shome22 with dissolve
        sa "You did...? Oh..."
    else:
        scene ep11_shome22 with dissolve
    sa "I hope that doesn't make you feel weird."
    scene ep11_shome23 with dissolve
    mc "Me? What about you?"
    scene ep11_shome22 with dissolve
    sa "Well... It does. I'm not sure if I want to know this, but..."
    sa "Just answer me yes or no. Did you fuck her?"
    scene ep11_shome23 with dissolve
    mc "Fuck her? No. It didn't go that far."
    scene ep11_shome24 with dissolve
    sa "Then I'm good. Now I don't have to picture Jill riding your dick when I talk to her."
    scene ep11_shome25 with dissolve
    mc "Sage..."
    scene ep11_shome24 with dissolve
    sa "I'm joking."
    scene ep11_shome25 with dissolve
    mc "It's not funny."
    scene ep11_shome21 with dissolve
    sa "Anyway, I'm looking forward to spending more time with her. I like her."
else:
    sa "I'm looking forward to spending more time with her. I like her."
scene ep11_shome20 with dissolve
mc "Yeah, she's great."
scene ep11_shome22 with dissolve
sa "You don't feel bad that I'm leaving you here tomorrow, right?"
scene ep11_shome23 with dissolve
mc "Not at all. Enjoy yourself with Jill. I'll spend quality time with Dad and drop by Zoey, too."
scene ep11_shome26 with dissolve
sa "You're dropping by your ex-girlfriend tomorrow?"
scene ep11_shome27 with dissolve
mc "I'm dropping by my friend tomorrow."
scene ep11_shome26 with dissolve
sa "Your friend who you used to fuck."
scene ep11_shome27 with dissolve
mc "Who is now my friend."
mc "Sage... Zoey's been important to me for the better part of my life. Ever since my childhood, she's been there for me."
mc "I'm trying to stay friends with her now that she's back from San Diego, but it's tough because I feel she just left me here."
scene ep11_shome28 with dissolve
sa "I hear what you're saying, but it sounds like the moment your girlfriend leaves...you run off to your ex to spend time with her."
scene ep11_shome27 with dissolve
mc "That's not what it is."
sa "..."
scene ep11_shome28 with dissolve
sa "Another way to say that is that it's exactly what it is."
scene ep11_shome27 with dissolve
mc "You don't understand."
scene ep11_shome28 with dissolve
sa "No, you're the one who doesn't understand."
sa "Picture if our roles were reversed, yeah?"
scene ep11_shome29 with dissolve
sa "You're with me and my family and leave tomorrow to do whatever..."
sa "And the moment you leave, I run to Chad and spend time alone with him at his place."
scene ep11_shome27 with dissolve
mc "..."
mc "I don't think it's quite the same."
scene ep11_shome30 with dissolve
sa "It is!"
scene ep11_shome27 with dissolve
mc "It's not. Also, I wouldn't have a problem with that because I trust you."
scene ep11_shome30 with dissolve
sa "Oh, shut up! I trust you, too."
scene ep11_shome31 with dissolve
mc "Sage, I don't want to fight. I shouldn't have brought it up. Let's forget I said anything."
scene ep11_shome28 with dissolve
sa "So, you're not going to see her tomorrow?"
scene ep11_shome27 with dissolve
mc "I will."
scene ep11_shome32 with dissolve
sa "..."
scene ep11_shome33 with dissolve
mc "Goodnight?"
stop music fadeout 3
scene ep11_shome34 with dissolve
$ renpy.pause()
if "Sage" not in tmp_mod_list:
    $ new_bio("Sage", "Dad and Sage got along great when I brought her home to meet him.")
    $ new_bio("Sage", "I told Sage about Zoey and what she meant to me. To my surprise, it turned into a fight.")
    $ new_bio("Dad", "Dad and Sage got along great when I brought her home to meet him.")
    $ tmp_mod_list.append("Sage")
if wt_ep9_branch_numbers > 1:

    "scrappy" "Do you want to see this scene on other paths?"
    menu:
        "Yes":
            jump ep11_home_label
        "No. Continue the game.":
            pass

jump ep11_zoey_home_label

label ep11_sage_party_label:
play music "music/ep7/licensed_music/track48.mp3"
scene ep11_sage_party2 with dissolve
$ renpy.pause()
scene ep11_sage_party1 with dissolve
$ renpy.pause()
scene ep11_sage_party3 with dissolve
sa "Good, you're here."
scene ep11_sage_party4 with dissolve
if jade_state == 0:
    mc "I just got back from class. What's up?"
else:
    mc "I was, uh...hanging out with Derek. What's up?"
scene ep11_sage_party5 with dissolve
sa "I'll tell you what's up. You and me, all night."
scene ep11_sage_party6 with dissolve
mc "I can stay up until midnight or so, but all night is too much."
mc "You brought booze?"
scene ep11_sage_party7 with dissolve
sa "Yes, and I'm not leaving before this bottle is finished. You can either be a responsible boyfriend and help me drink it or have a fucked up girlfriend puking on your floor."
scene ep11_sage_party8 with dissolve
mc "What happened? This isn't you."
scene ep11_sage_party9 with dissolve
sa "I went back home today."
scene ep11_sage_party10 with dissolve
mc "And?"
scene ep11_sage_party11 with dissolve
sa "And I got caught in the middle of a fight."
sa "They never fought like that when Tybalt and I were present. Usually, we were at least in another room, and they had some limits on what they'd say..."
scene ep11_sage_party13 with dissolve
$ renpy.pause()
scene ep11_sage_party12 with dissolve
sa "Damn, that's good."
scene ep11_sage_party11 with dissolve
sa "But not this time."
scene ep11_sage_party14 with dissolve
mc "Shit... What did they say?"
scene ep11_sage_party15 with dissolve
sa "Mom called Dad a cheating slob whose only interests in life are money and work."
sa "She claimed that he never cared about me or Tybalt while I was there with them. And that he didn't even want us."
scene ep11_sage_party14 with dissolve
mc "Wow... Your mom said that!?"
scene ep11_sage_party15 with dissolve
sa "Dad called Mom a vampire, only that she doesn't suck blood; she sucks the life out of him."
sa "And that he never asked to be a father."
scene ep11_sage_party16 with dissolve
mc "Sage..."
scene ep11_sage_party17 with dissolve
sa "You're not drinking."
scene ep11_sage_party16 with dissolve
menu:
    "Drink with her":
        $ ep11_sage_sober = False
        scene ep11_sage_party18 with dissolve
        $ renpy.pause()
    "Stay sober":
        $ ep11_sage_sober = True
        mc "No, and I don't think you should drink either."
        scene ep11_sage_party15 with dissolve
        sa "If I don't drink, I'll feel worse."
        scene ep11_sage_party14 with dissolve
        mc "I don't think that's true, but if you want to drink, drink."
        mc "I'll be here for you all night."
scene ep11_sage_party19 with dissolve
sa "My father... My so-called role model never wanted to be my dad."
scene ep11_sage_party20 with dissolve
sa "No one wants to be my dad."
scene ep11_sage_party21 with dissolve
$ renpy.pause()
scene ep11_sage_party22 with dissolve

if persistent.mod_wtenabled: 
                        $mod_choices = ["(Possible Josy points)","(-Josy)","(-DIK)","(+DIK)","(+5 Josy)","(-5 Josy)","","","","","","" ]
                        #[mod_gr][mod_choices[0]]
                        #\n{size=-4}[m_c1][mod_choices[1]][m_c2][mod_choices[4]]

menu:
    "Sympathize [m_c1][mod_choices[2]]":
        $ dk(-1)
        scene ep11_sage_party23 with dissolve
        mc "How can I help you?"
        scene ep11_sage_party24 with dissolve
        sa "You already are. That's why I came here."
        scene ep11_sage_party25 with dissolve
        sa "You're my rock."
    "Joke [m_c1][mod_choices[3]]":
        $ dk(1)
        scene ep11_sage_party29 with dissolve
        mc "I...can be your daddy."
        scene ep11_sage_party27 with dissolve
        sa "What the hell is wrong with you?"
        scene ep11_sage_party28 with dissolve
        mc "Lots."
        scene ep11_sage_party26 with dissolve
        sa "I don't need you to be my daddy. I need you to be my rock."

if jade_state > 0:
    scene ep11_sage_party30 with dissolve
    mc "Your rock..."
stop music fadeout 3
scene ep11_sage_party31 with dissolve
sa "We need music."
play music "music/ep11/licensed_music/track178.mp3"
scene ep11_sage_party32 with dissolve
$ renpy.pause()
scene ep11_sage_party33 with dissolve
$ renpy.pause()
scene ep11_sage_party35 with dissolve
sa "Boobs are weird."
scene ep11_sage_party36 with dissolve
sa "These big lumps of fat are meant to feed a child..."
sa "And men go crazy for them."
scene ep11_sage_party37 with dissolve
mc "Some things you can't explain. It's evolutionary."
scene ep11_sage_party38 with dissolve
sa "Don't get me started on male boobs. They are even weirder."
sa "I mean, why the nipple? Why?"
sa "Show me your nipples."
scene ep11_sage_party37 with dissolve
mc "Huh? Why?"
scene ep11_sage_party38 with dissolve
sa "I need to see them."
scene ep11_sage_party39 with dissolve
mc "Happy?"
sa "Hahaha! They're so tiny!"
scene ep11_sage_party40 with dissolve
mc "What? They're not tiny."
scene ep11_sage_party41 with dissolve
sa "They're like bleached raisins."
scene ep11_sage_party42 with dissolve
mc "If you're gonna body shame me, you won't get to see my nipples."
scene ep11_sage_party43 with dissolve
sa "Look at mine!"
scene ep11_sage_party44 with dissolve
sa "They're both big."
scene ep11_sage_party45 with dissolve
mc "Yeah, I love your breasts."
sa "See! Right there! That's what I'm talking about."
sa "Look at how you get all excited for nothing."
scene ep11_sage_party46 with dissolve
mc "It's not for nothing. They're hot."
mc "Don't you get turned on by things?"
scene ep11_sage_party47 with dissolve
sa "Yeah, but not your tiny nipples. Hahaha!"
scene ep11_sage_party48 with dissolve
mc "You're wrong. They are beautiful..."
mc "And also, they do have a function. They are ticklish, and when a girl kisses them, it gets exciting."
scene ep11_sage_party49 with dissolve
sa "I get excited when you kiss mine. So, is it the same for you?"
scene ep11_sage_party50 with dissolve
mc "You've never kissed mine, but I think it would be nice."
scene ep11_sage_party49 with dissolve
sa "Show me those raisins again."
scene ep11_sage_party50 with dissolve
mc "Not if you're gonna call them that."
scene ep11_sage_party51 with dissolve
sa "Show me! I wanna lick them."
scene ep11_sage_party52 with dissolve
mc "You're so weird when you're drunk."
scene ep11_sage_party53 with dissolve
sa "Haha! I'm not joking! I'm gonna do it."
scene ep11_sage_party52 with dissolve
mc "I'm not stopping you. Go ahead."
scene ep11_sage_party54 with dissolve
sa "*{i}Lick lick{/i}*"
scene ep11_sage_party55 with dissolve
sa "Hahaha! It got all stiff. It's like it grew another mini-raisin on top of it."
scene ep11_sage_party54 with dissolve
sa "*{i}Lick lick{/i}*"
sa "Do you like that?"
mc "It's not unpleasant. And it does tickle."
scene ep11_sage_party56 with dissolve
sa "Hahaha!"
scene ep11_sage_party34 with dissolve
$ renpy.pause()
if ep11_sage_sober:
    scene ep11_sage_party57 with dissolve
else:
    scene ep11_sage_party57b with dissolve
$ renpy.pause()
scene ep11_sage_party58 with dissolve
sa "I shouldn't have drunk all that."
if not ep11_sage_sober:
    sa "I'm happy you helped out."
    scene ep11_sage_party59 with dissolve
    mc "I have classes tomorrow..."
    scene ep11_sage_party58 with dissolve
    sa "Yup..."
else:
    scene ep11_sage_party59 with dissolve
    mc "I'm not gonna say I told you so."
    scene ep11_sage_party58 with dissolve
    sa "You did tell me so."
scene ep11_sage_party60 with dissolve
sa "At least it helped."
scene ep11_sage_party61 with dissolve
mc "Did it?"
scene ep11_sage_party60 with dissolve
sa "For now..."
sa "Can I stay here tonight?"
scene ep11_sage_party61 with dissolve
mc "Always."
scene ep11_sage_party62 with dissolve
sa "My face feels funny..."
sa "I think I will go lie down in bed."
stop music fadeout 3
scene ep11_sage_party63 with dissolve
mc "Yeah, it's getting late."
play music "music/ep11/licensed_music/track184.mp3"
scene ep11_sage_party64 with fade
$ renpy.pause()
scene ep11_sage_party65 with dissolve
$ renpy.pause()
scene ep11_sage_party66 with dissolve
mc "Are you up already?"
scene ep11_sage_party67 with dissolve
sa "Yeah. I had to hurl..."
scene ep11_sage_party68 with dissolve
mc "Oh..."
scene ep11_sage_party69 with dissolve
sa "[name]?"
scene ep11_sage_party68 with dissolve
mc "Yeah?"
scene ep11_sage_party70 with dissolve
$ renpy.pause()
scene ep11_sage_party71 with dissolve
$ renpy.pause()
scene ep11_sage_party72 with dissolve
sa "About my family... My real family..."
sa "I don't know who my real dad is. And I don't think he knows I exist."
scene ep11_sage_party71 with dissolve
$ renpy.pause()
scene ep11_sage_party72 with dissolve
sa "And my birth mom couldn't take care of me. I don't know if it was her age or if she didn't have the means to do it..."
sa "But that's why I ended up in a foster home. I was about four or five years old at that time."
scene ep11_sage_party73 with dissolve
sa "I don't remember much of my birth mom. It's weird..."
sa "I don't remember her face, but I remember her presence."
scene ep11_sage_party74 with dissolve
sa "I remember...certain smells. Like burnt wood and pinecones, for some reason."
sa "And this warm cradling, smell you get from perfume on a jacket made out of fleece."
sa "I think we were outdoors a lot."
scene ep11_sage_party75 with dissolve
sa "I've often considered looking her up to find out who she is."
sa "But I can't even type her name in a browser. It's like a mental block preventing me from going further."
scene ep11_sage_party76 with dissolve
sa "I think I'm scared of learning more about her."
sa "And I don't know what I would do with whatever information I'd find."
scene ep11_sage_party74 with dissolve
sa "It's easier for me not to think about her. And to just remember the smells."
sa "Whenever I get a whiff that brings me back, I feel like it's...her. That she's watching over me."
sa "That she's taking care of me in the only way she can. Like a spirit."
scene ep11_sage_party73 with dissolve
sa "I want to believe that all she meant by putting me in foster care was good."
sa "And I wouldn't want to know that it was for another reason."
scene ep11_sage_party77 with dissolve
sa "And that's why I can't look her up."
scene ep11_sage_party78 with dissolve
mc "I can relate to that."
scene ep11_sage_party77 with dissolve
sa "You can? How?"
scene ep11_sage_party78 with dissolve
mc "Not to everything you said, but that part about looking your mother up..."
mc "I'd never done it either with Mom. Dad always told me stories about her, which was enough for me."
scene ep11_sage_party79 with dissolve
mc "But after reading her diary, I've become less afraid of learning new things about her."
mc "But I can't imagine how you feel not knowing anything. I bet it's tough..."
scene ep11_sage_party77 with dissolve
sa "Now you know."
sa "I haven't told anyone about this. And I mean no one."
sa "Mom and Dad know more than I do, but I have never asked them about it for the same reason."
if ep9_sage_vanilla or not ep10_sage_lewd:
    scene ep11_sage_party80 with dissolve
    $ renpy.pause()
    scene ep11_sage_party79 with dissolve
    mc "Thank you for telling me. It means a lot to me."
else:
    scene ep11_sage_party79 with dissolve
    mc "Thank you for telling me."
scene ep11_sage_party77 with dissolve
sa "I'm sorry it took me this long to say it."
scene ep11_sage_party78 with dissolve
if jade_state == 0:
    stop music fadeout 3
mc "Don't be. You had your reasons."

scene ep11_sage_party81 with dissolve
if jade_state > 0:
    mc "{i}Sage needed me to be her rock.{/i}"
    mc "{i}And there I was, still deciding what to do with her.{/i}"
    mc "{i}Imagining that there was a fourth option that would make everything ok.{/i}"
    stop music fadeout 3
    mc "{i}I wanted to be her rock.{/i}"
    mc "{i}But deep down, I knew that I could never be it.{/i}"
else:
    $ renpy.pause()
$ new_bio("Sage", "Sage got caught in a fight between Jade and Stephen and spent the night with me for comfort.")
$ new_bio("Sage", "Sage told me what she knew about her birth mom and why she didn't want to learn more about her.")
jump ep11_pass_time_label

label ep11_ssolo_label:
$ guideSuggestedPage = 181
play music "music/ep10/pineapple_pizza.mp3"
scene ep11_ssolo1 with wipeleft
sa "*{i}Groans{/i}*"
mc "You almost got it."
scene ep11_ssolo2 with dissolve
sa "Stop saying I got it! I'm nowhere close, and my hand hurts."
scene ep11_ssolo3 with dissolve
mc "But you almost have it."
scene ep11_ssolo4 with dissolve
sa "This F chord can F off!"
scene ep11_ssolo5 with dissolve
mc "Maybe that's enough practice for today."
scene ep11_ssolo6 with dissolve
play sound "sound_effects/cellphone.mp3"
"*{i}Phone rings{/i}*"
scene ep11_ssolo7 with dissolve
sa "Yeah?"
scene ep11_ssolo8 with dissolve
sa "Nothing. I'm hanging out with [name]."
sa "What? Now?"
scene ep11_ssolo9 with dissolve
sa "Uh... No, he didn't tell me anything about it either. Where's he going? And what about you?"
scene ep11_ssolo8 with dissolve
sa "Yeah, I get it."
sa "But I'm busy with [name] tonight."
scene ep11_ssolo10 with dissolve
sa "Alright, but I'm bringing him with me!"
sa "I don't care! He's my boyfriend! If you're gonna fight, then so be it. He already knows that you do."
scene ep11_ssolo11 with dissolve
sa "So what? Do you think it was fun for me last time?"
sa "You said horrible things to Dad!"
scene ep11_ssolo10 with dissolve
sa "Yeah. He said those things, too. I know."
sa "Stop yelling!"
scene ep11_ssolo8 with dissolve
sa "We'll be there soon. Bye."
scene ep11_ssolo12 with dissolve
mc "What's going on?"
scene ep11_ssolo13 with dissolve
sa "Dad was in the middle of moving out, and it caught Mom by surprise because he didn't mention that he was gonna."
sa "She wants me to be there helping out."
scene ep11_ssolo12 with dissolve
mc "Tonight?"
scene ep11_ssolo13 with dissolve
sa "Yeah. I know we're supposed to hang out, but it sounded urgent."
sa "I think Mom isn't handling it well. I need to be there."
scene ep11_ssolo14 with dissolve
mc "I heard you say \"we\"."
scene ep11_ssolo15 with dissolve
sa "Yeah, you don't mind, do you?"
scene ep11_ssolo16 with dissolve

if persistent.mod_wtenabled: 
                        $mod_choices = ["(+Sage)","(-Sage)","(-DIK)","(+DIK)","(+5 Josy)","(-5 Josy)","","","","","","" ]
                        #[mod_gr][mod_choices[0]]
                        #\n{size=-4}[m_c1][mod_choices[1]][m_c2][mod_choices[4]]

menu:
    "I don't mind \n{size=-4}[m_c1][mod_choices[0]]":
        $ RPsage += 1
        mc "No, I don't mind. Of course, I'll be there for you."
        stop music fadeout 3
        scene ep11_ssolo19 with dissolve
        sa "Thank you."
    "I'd rather not come with you":
        mc "Honestly, I'd rather not come with you. It sounds like it's private."
        scene ep11_ssolo15 with dissolve
        sa "You're a big part of my life, [name]. Are you telling me that you won't be there to support me when I need you?"
        scene ep11_ssolo16 with dissolve
        menu:
            "I'll come \n{size=-4}[m_c1][mod_choices[0]]":
                $ RPsage += 1
                mc "No, of course. I'll be there to support you; I'm coming with you."
                stop music fadeout 3
                scene ep11_ssolo19 with dissolve
                sa "Thank you."
            "I don't think I should \n{size=-4}[m_c1][mod_choices[1]]":
                $ RPsage -= 1
                mc "I don't think I should be there tonight."
                if jade_state == 0:
                    mc "With how you described it last time, I don't want to be caught in the middle of a fight."
                scene ep11_ssolo18 with dissolve
                sa "Do you think I want that? I need you, [name]."
                scene ep11_ssolo17 with dissolve
                stop music fadeout 3
                mc "..."
                mc "Ok, I'll come with you."

play music "music/ep11/licensed_music/track153.mp3"
scene ep11_ssolo20 with wiperight
$ renpy.pause()
scene ep11_ssolo21 with dissolve
ja "No, put that down! That is not his; it's mine!"
scene ep11_ssolo22 with dissolve
wo2 "I'm just following orders, ma'am. You'll have to take it up with your husband."
scene ep11_ssolo23 with dissolve
ja "He's not my husband! And don't you dare take my ornament!"
scene ep11_ssolo24 with dissolve
sa "Mom?"
scene ep11_ssolo25 with dissolve
ja "Where is Stephen!? Did you see him anywhere?"
scene ep11_ssolo27 with dissolve
sa "He's not here?"
scene ep11_ssolo26 with dissolve
ja "He's somewhere. And he sent these god-awful workers to move our belongings without consulting me."
scene ep11_ssolo27 with dissolve
sa "I'll try calling him."
scene ep11_ssolo28 with dissolve
mc "What can I do to help?"
scene ep11_ssolo29 with dissolve
sa "Stay with Mom. Try to calm her down."
if jade_state > 0:
    scene ep11_ssolo30 with dissolve
    mc "(I'd rather call your dad...)"
    scene ep11_ssolo31 with dissolve
    ja "What are you doing here?"
    scene ep11_ssolo30 with dissolve
    mc "I'm here because Sage wanted me to come with her."
    if ep4_toldDerekAboutJade:
        scene ep11_ssolo31 with dissolve
        ja "How stupid are you? Stephen could be here at any minute."
        ja "Do you want to expose what you have done to my daughter?"
        scene ep11_ssolo32 with dissolve
        mc "Should I have told her I couldn't come because of the love triangle I'm involved in with her mom and dad?"
        scene ep11_ssolo31 with dissolve
        ja "Do you find this amusing, you sick son of a bitch?"
        scene ep11_ssolo32 with dissolve
        mc "Not one bit. I'd undo everything if I could."
        scene ep11_ssolo31 with dissolve
        ja "I could strangle you."
    else:
        scene ep11_ssolo31 with dissolve
        ja "Do you find this amusing, you sick son of a bitch?"
        scene ep11_ssolo30 with dissolve
        mc "Not one bit."
else:
    scene ep11_ssolo33 with dissolve
    mc "(How do you expect me to do that?)"
    scene ep11_ssolo34 with dissolve
    ja "What are you doing here?"
    scene ep11_ssolo33 with dissolve
    mc "I'm here because Sage wanted me to come with her."
    scene ep11_ssolo34 with dissolve
    ja "Have you told her anything?"
    scene ep11_ssolo33 with dissolve
    mc "About what?"
    scene ep11_ssolo34 with dissolve
    ja "What happened between us in class."
    scene ep11_ssolo36 with dissolve
    mc "No. Because that's on your conscience, not mine."
    mc "I'm not letting that affect my relationship with Sage."
    scene ep11_ssolo35 with dissolve
    ja "Good. It better stay that way. Got it?"
    scene ep11_ssolo36 with dissolve
    mc "I don't care about you. I care about Sage."
    mc "Whatever you tried to do with me, it's water under the bridge."

scene ep11_ssolo37 with dissolve
sa "Good news. He's on his way over here."
scene ep11_ssolo38 with dissolve
if jade_state > 0:
    ja "*{i}Grunts{/i}*"
else:
    sa "How's it going?"
scene ep11_ssolo39 with dissolve
mc "She's...agitated."
scene ep11_ssolo40 with dissolve
sa "At least she hasn't started throwing things."
scene ep11_ssolo41 with dissolve
mc "She does that?"
scene ep11_ssolo42 with dissolve
sa "She did it last time."
sa "I can't believe he's moving out... It's really happening."
scene ep11_ssolo43 with dissolve
mc "Are you ok?"
scene ep11_ssolo42 with dissolve
sa "No, I'm not ok. This is my home..."
sa "Come, I wanna show you my room before it gets emptied."

scene ep11_ssolo44 with dissolve
sa "Not that it matters because, as you know, it's nothing like it was when I lived here."
scene ep11_ssolo45 with dissolve
mc "I can tell. I wouldn't have guessed this was your room."
scene ep11_ssolo46 with dissolve
sa "And soon, it will be someone else's room. This will be someone else's home."
sa "I wonder where Mom will move... I'm sure she's already panicking trying to figure that out."
scene ep11_ssolo47 with dissolve
sa "I wanted the first time you met my parents to be like how it was for me to meet Neil."
sa "But you already met them before you became my boyfriend. So, that moment is gone. And now everything is chaotic."
scene ep11_ssolo48 with dissolve
sa "That phone call with Mom before we came here was the first time I told her that you are my boyfriend."
sa "I didn't think I would be yelling at her when I told her about you, either."
scene ep11_ssolo49 with dissolve
$ renpy.pause()
if jade_state > 0:
    scene ep11_ssolo50 with dissolve
    mc "How is your relationship with your mom? How...important is it to you?"
    scene ep11_ssolo51 with dissolve
    sa "What do you mean? She's my mom. It's very important to me."
    sa "We don't always see eye to eye on things, but I love her."
    scene ep11_ssolo52 with dissolve
    sa "And even though Dad may not have wanted kids...or asked to be my father..."
    sa "I love him, too."

scene ep11_ssolo53 with dissolve
sa "I don't think Dad's reaction to hearing about you and me will be much better than Mom's."
scene ep11_ssolo54 with dissolve
mc "That's ok. I understand why it wouldn't."
scene ep11_ssolo53 with dissolve
sa "You must think my family is crazy."
scene ep11_ssolo54 with dissolve
mc "Name one family without issues."
scene ep11_ssolo55 with dissolve
sa "Yours."
scene ep11_ssolo54 with dissolve
mc "Uh... No. It depends on how you look at it. But we're far from perfect."
mc "And my family is basically Dad."
scene ep11_ssolo55 with dissolve
sa "What about other relatives?"
scene ep11_ssolo56 with dissolve
mc "Dad was an only child and left his parents during his teens. So, there are no grandparents or close relatives on his side of the family who are part of our lives."
mc "As for Mom's side... I go by what Dad has told me."
scene ep11_ssolo57 with dissolve
mc "Mom had no siblings, and her parents didn't get along with Dad."
mc "As a result, it's a small family."
scene ep11_ssolo58 with dissolve
sa "But also, not a lot of issues."
scene ep11_ssolo57 with dissolve
mc "Sure, that's something."
mc "But..."
scene ep11_ssolo58 with dissolve
sa "But what?"
scene ep11_ssolo56 with dissolve
mc "I feel like I've missed out on a lot because of it."
mc "Like not having grandparents or siblings..."
scene ep11_ssolo59 with dissolve
mc "I've got none of those family relations that most seem to have and take for granted."
mc "It would have been nice to have a bigger family."
mc "That's the issue with my family."
stop music fadeout 3
scene ep11_ssolo60 with dissolve
$ renpy.pause()
scene ep11_ssolo64 with dissolve
play music "music/ep9/tremolo.mp3"
sa "What about your future family?"
scene ep11_ssolo66 with dissolve
mc "My future family?"
scene ep11_ssolo65 with dissolve
sa "Yeah. What do you see when you close your eyes and imagine your future family? Try it."
scene ep11_ssolo61 with dissolve
sa "Tell me... What's going on in that pretty little head of yours?"
scene ep11_ssolo62 with dissolve
mc "Hm... I see..."
scene ep11_ssolo67 with dissolve
mc "Well, there's me and Dad. Surprisingly, in the future, we will still look the same as we do now. We haven't aged one bit."
sa "Uh-huh. What else?"
scene ep11_ssolo69 with dissolve
mc "There's a girl next to me. It could be my wife."
if ep11_sage_stance == 1 or ep11_sage_stance == 0:
    menu:
        "[m_c1]It could be you":
            $ ep11_sage_questions[0] = True
            scene ep11_ssolo68 with dissolve
            mc "It could be you."
        "I don't see her face":
            $ ep11_sage_questions[0] = False
            mc "I don't see her face."
else:
    $ ep11_sage_questions[0] = False
    mc "I don't see her face."
mc "We look happy together."
menu:
    "I see toys":
        $ ep11_sage_questions[1] = True
        scene ep11_ssolo70 with dissolve
        mc "I see toys on the floor."
    "I don't see any kids":
        $ ep11_sage_questions[1] = False
        mc "But I don't see any kids."
scene ep11_ssolo62 with dissolve
mc "And I see all these dark silhouettes around us. I think they're part of our family."
mc "They might be our close friends too."
mc "Yeah, we're not alone here. We're a big family."
scene ep11_ssolo63 with dissolve
$ renpy.pause()
if ep11_sage_questions[0]:
    if ep9_sage_vanilla or not ep10_sage_lewd or affinity != "DIK":
        scene ep11_ssolo73 with dissolve
        $ renpy.pause()
        scene ep11_ssolo75 with dissolve
        $ renpy.pause()
        stop music fadeout 3
        scene ep11_ssolo72 with dissolve
        sa "That sounds like a wonderful future family."
    else:
        scene ep11_ssolo71 with dissolve
        sa "It does sound like a nice future family, but is that how you feel?"
        scene ep11_ssolo74 with dissolve
        stop music fadeout 3
        mc "I think so..."
        scene ep11_ssolo71 with dissolve
        sa "Ok."
else:
    stop music fadeout 3
    scene ep11_ssolo71 with dissolve
    sa "That sounds like a nice future family."

play music "music/ep11/licensed_music/track153.mp3"
scene ep11_ssolo76 with dissolve
ja "You can't decide what to take without conferring with me!"
scene ep11_ssolo77 with dissolve
sa "Dad is here... Let's help out."
scene ep11_ssolo78 with dissolve
ja "What else have you ordered them to move? My wardrobe?"
scene ep11_ssolo79 with dissolve
sb "You're overreacting, as usual. They're moving my office, one of the bathrooms, the guest room-"
scene ep11_ssolo81 with dissolve
sa "*{i}Whispers{/i}* That's Tybalt's old room."
scene ep11_ssolo79 with dissolve
sb "-and the living room. You can keep the rest."
scene ep11_ssolo80 with dissolve
ja "Oh!? Can I keep the rest? Aren't you Mr. Wonderful!?"
scene ep11_ssolo82 with dissolve
sa "Mom, calm down. I know it's hard, but listen to what he's saying. Those are the rooms they are moving, and you'll still have the rest until you decide to move."
scene ep11_ssolo83 with dissolve
sa "I'm sure Dad still wants you to have dignity. Right, Dad?"
scene ep11_ssolo84 with dissolve
sb "You shouldn't have come here tonight."
sb "I know this is sudden, but I can't reason with your mother anymore. So, I won't bother doing it."
scene ep11_ssolo86 with dissolve
ja "Go to hell!"
scene ep11_ssolo85 with dissolve
sb "What are you doing here?"
scene ep11_ssolo87 with dissolve
sa "Mom asked me to come."
sa "Dad, this is my boyfriend. I'm sure you remember him from before."
scene ep11_ssolo85 with dissolve
if ep4_toldDerekAboutJade:
    sb "Your boyfriend?"
    stop music fadeout 3
    scene ep11_ssolo88 with dissolve
    sb "We are going to have a word, you and I. Follow me."
    scene ep11_ssolo89 with dissolve
    sa "Dad?"
    $ guideSuggestedPage = 182
    scene ep11_ssolo95 with dissolve
    sb "Close the door."
    play sound "sound_effects/door_close.mp3"
    scene ep11_ssolo96 with dissolve
    play music "music/ep10/licensed_music/track149.mp3"
    sb "That video you recorded..."
    scene ep11_ssolo97 with dissolve
    sb "Screwing my wife in my bed."
    sb "It ended up in my inbox."
    scene ep11_ssolo98 with dissolve
    $ renpy.pause()
    scene ep11_ssolo99 with dissolve
    sb "You fucked my wife, and now you're dating my daughter..."
    sb "You've got some serious nerve, kid. Or perhaps it's brain damage."
    sb "Are you doing this to provoke me? To elicit some response?"
    scene ep11_ssolo100 with dissolve
    $ renpy.pause()
    scene ep11_ssolo101 with dissolve
    sb "Although it was not your intention, that video was just what I needed."
    sb "That video has helped me greatly."
    sb "You, [name], have helped me greatly. By fucking my wife in my bed."
    scene ep11_ssolo102 with dissolve
    $ renpy.pause()
    scene ep11_ssolo103 with dissolve
    menu:
        "Shake his hand":
            scene ep11_ssolo105 with dissolve
            $ renpy.pause()
            scene ep11_ssolo106 with dissolve
            $ renpy.pause()
        "Don't shake his hand":
            scene ep11_ssolo104 with dissolve
            $ renpy.pause()
            scene ep11_ssolo107 with dissolve
            $ renpy.pause()
    scene ep11_ssolo108 with dissolve
    sb "But what are your intentions?"
    sb "Surely, they aren't hostile. Because I will tell you right now, there's nothing for you to gain from me, my wife, or my daughter by any of this."
    scene ep11_ssolo109 with dissolve
    sb "But there's a hell of a lot to lose."
    sb "And you are staring into the face of the judge, jury, and executioner."
    scene ep11_ssolo110 with dissolve
    $ renpy.pause()
    scene ep11_ssolo111 with dissolve
    sb "You know what? Don't tell me your intentions."
    sb "Let them be an enigma. I like to think there's a plan behind your actions that I can't quite comprehend."
    sb "At least you're wise enough to stay silent..."
    scene ep11_ssolo112 with dissolve
    sb "And I also think you should remain a man of few words. After all, speech is silver, but silence is golden."
    sb "So, that tape, this conversation, everything about you and my soon-to-be ex-wife... Remember..."
    scene ep11_ssolo113 with dissolve
    sb "Speech is silver; silence is golden."
    scene ep11_ssolo114 with dissolve
    $ renpy.pause()
    scene ep11_ssolo115 with dissolve
    sb "There's the door."
    stop music fadeout 3
    scene ep11_ssolo117 with dissolve
    $ renpy.pause()
    play music "music/ep11/licensed_music/track153.mp3"
    scene ep11_ssolo118 with dissolve
    sa "What did Dad want?"
    scene ep11_ssolo120 with dissolve
    mc "Uh..."
    scene ep11_ssolo119 with dissolve
    mc "He didn't want me to...talk about what happened tonight to anyone."
    mc "He asked me to keep it a secret. And I agreed."
    scene ep11_ssolo118 with dissolve
    sa "*{i}Sigh{/i}* And I thought he'd try getting to know you or apologize for meeting you under these circumstances..."
    scene ep11_ssolo121 with dissolve
    ja "*{i}Scoffs{/i}*"
    $ new_bio("Burke", "Stephen told me he knew about my affair with Jade and told me to keep quiet about it.")
else:
    sb "I can't deal with you two now."
    scene ep11_ssolo90 with dissolve
    $ renpy.pause()
    scene ep11_ssolo91 with dissolve
    sa "He doesn't even care..."
    if affinity == "CHICK":
        scene ep11_ssolo93 with dissolve
        mc "It's ok. It's in the heat of the moment. He's not thinking clearly."
    else:
        scene ep11_ssolo92 with dissolve
        mc "It's ok. It's in the heat of the moment. He's not thinking clearly."
    scene ep11_ssolo94 with dissolve
    sa "Where's Mom?"
    scene ep11_ssolo116 with dissolve
    $ renpy.pause()
    scene ep11_ssolo121 with dissolve
ja "Your father is an absolute jackass. I could write plenty of books about every poor choice he's ever made."
ja "His ego is boundless, thinking he's on top of the world. But he lacks tact and isn't all that bright."
scene ep11_ssolo124 with dissolve
sa "Mom, I know you're hurting, but I don't want to listen to you badmouthing Dad."
sa "He's still my dad, even if you claim he never wanted to be it."
scene ep11_ssolo122 with dissolve
ja "You heard him say it, too. I wasn't lying."
scene ep11_ssolo124 with dissolve
sa "Yeah, but how do you think that makes me feel?"
scene ep11_ssolo122 with dissolve
ja "Of course, it hurts. The truth always hurts. Stephen is hurtful!"
ja "But you deserve to hear it."
scene ep11_ssolo125 with dissolve
sa "Do I deserve to hear it? Do I deserve to hear that I'm unwanted?"
scene ep11_ssolo123 with dissolve
ja "No, that's not what I meant."
scene ep11_ssolo125 with dissolve
sa "I'm done, Mom. I can't listen to this anymore."
scene ep11_ssolo126 with dissolve
$ renpy.pause()

scene ep11_ssolo127 with dissolve
sa "*{i}Sobs{/i}*"
scene ep11_ssolo128 with dissolve
mc "Sage? Wanna leave?"
scene ep11_ssolo129 with dissolve
sa "Yeah."
scene ep11_ssolo130 with dissolve
sa "Thank you for being here with me. I couldn't have done this without you."
scene ep11_ssolo131 with dissolve
mc "Sure, you could. You're strong."
mc "Who knows what will come from these changes? Maybe it will all work out in the end."
scene ep11_ssolo132 with dissolve
stop music fadeout 3
sa "Let's go home."
scene ep11_ssolo133 with dissolve
$ renpy.pause()
$ new_bio("Sage", "Sage brought me home with her as support when her parents fought. She was upset about the situation but happy that I came with her.")
$ new_bio("Jade", "Jade wasn't handling her divorce well, but neither was Stephen.")
$ new_bio("Burke", "Jade wasn't handling her divorce well, but neither was Stephen.")
jump ep11_math_label

label ep11_sage_lewd_label:
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
    $ ep4_toldDerekAboutJade = False
    $ ep3_acceptedJade = False
    $ tc = 0
    $ RPsage = 22
    play music "music/ep11/oholynight.mp3"

hide screen new_phone_screen
$ guideSuggestedPage = 222
scene ep11_sage_lewd1 with dissolve
sa "You're not sleeping over there, right?"
scene ep11_sage_lewd2 with dissolve
mc "Why not?"
scene ep11_sage_lewd3 with dissolve
sa "I was thinking we could lie next to each other."
scene ep11_sage_lewd2 with dissolve
mc "I'm not sure if we'll fit."
scene ep11_sage_lewd3 with dissolve
sa "Spoon me for a little while?"
scene ep11_sage_lewd4 with dissolve
$ renpy.pause()
scene ep11_sage_lewd5 with dissolve
sa "Comfortable?"
scene ep11_sage_lewd6 with dissolve
mc "Very."
scene ep11_sage_lewd5 with dissolve
sa "Thanks for tonight."
scene ep11_sage_lewd6 with dissolve
mc "You too."
scene ep11_sage_lewd7 with dissolve
sa "Something I like about you..."
sa "You're not afraid to joke around at your own expense, and you make sure people are having a good time."
sa "Like tonight... We had a great night before you showed up, yet you made it even better."
scene ep11_sage_lewd8 with dissolve
sa "Everyone felt comfortable with you here. And that's coming from girls who didn't want to come to your party dressed in underwear."
scene ep11_sage_lewd9 with dissolve
mc "Thanks, I guess. I'm not sure if it's me. I think it's because we've all grown close."
mc "Everyone brings something to the table and stays friendly with each other."
scene ep11_sage_lewd8 with dissolve
sa "Yeah, and we joke around a lot. I think it's great. I love it."
scene ep11_sage_lewd9 with dissolve

if persistent.mod_wtenabled and tc > 4 and not ep4_toldDerekAboutJade:
   "scrappy" "You have too many cheater points to get the Sage scene here."

mc "I love it, too."
if ep4_toldDerekAboutJade or tc > 4:
    jump ep11_sage_lewd_label2
scene ep11_sage_lewd13 with dissolve

if persistent.mod_wtenabled: 
                        $mod_choices = ["(Sage)","(+Josy)","(-DIK)","(+DIK)","(+5 Josy)","(-5 Josy)","","","","","","" ]
                        #[mod_gr][mod_choices[0]]
                        #\n{size=-4}[m_c1][mod_choices[1]][m_c2][mod_choices[4]]

menu:
    "[m_c1]I love you":
        scene ep11_sage_lewd14 with dissolve
        mc "And..."
        scene ep11_sage_lewd15 with dissolve
        sa "And what?"
        scene ep11_sage_lewd16 with dissolve
        mc "And I love you."
        scene ep11_sage_lewd17 with dissolve
        $ renpy.pause()
        scene ep11_sage_lewd18 with dissolve
        $ renpy.pause()
        scene ep11_sage_lewd19 with dissolve
        $ renpy.pause()
        if RPsage >= 22:
            $ ep11_sage_love = 2
            scene ep11_sage_lewd20 with dissolve
            sa "I love you too."
            scene ep11_sage_lewd21 with dissolve
            $ renpy.pause()
        else:
            $ ep11_sage_love = 1
        scene ep11_sage_lewd22 with dissolve
        sa "*{i}Smack{/i}*"
        scene ep11_sage_lewd23 with dissolve
        $ renpy.pause()
    "Don't say it" if not _in_replay:
        label ep11_sage_lewd_label2:
        $ ep11_sage_love = 0
        scene ep11_sage_lewd8 with dissolve
        sa "Good night."
        scene ep11_sage_lewd11 with dissolve
        mc "Are you falling asleep like this?"
        stop music fadeout 3
        scene ep11_sage_lewd10 with dissolve
        sa "I think I am..."
        scene ep11_sage_lewd12 with dissolve
        $ renpy.pause()
        
        if wt_ep9_branch_numbers != 1:
           "scrappy" "Watch the scene again on other paths?"
           menu:
               "Yes":
                  jump wt_ep11_bella_party_label
               "No. Continue the game.":
                   if ep11_zoey_kiss == 2:
                        jump ep11_pp_zoey_end2b_label
                   else:
                        pass
        
        jump ep11_gift_label

scene anim_sage_kiss2_ep11 with dissolve
pause
scene anim_sage_kiss3_ep11 with dissolve
pause
scene anim_sage_finger_ep11 with dissolve
pause
scene anim_sage_finger2_ep11 with dissolve
pause
scene anim_sage_lick1_ep11 with dissolve
pause
scene anim_sage_lick2_ep11 with dissolve
pause
scene anim_sage_lick3_ep11 with dissolve
pause

$ tmpInt = 0
label ep11_sage_lewd_loop1_label:
menu:
    "Missionary":
        $ tmpInt += 1
        scene anim_sage_miss1_ep11 with dissolve
        pause
        scene anim_sage_miss2_ep11 with dissolve
        pause
        scene anim_sage_miss3_ep11 with dissolve
        pause
        scene anim_sage_miss4_ep11 with dissolve
        pause
        scene anim_sage_miss5_ep11 with dissolve
        pause
        jump ep11_sage_lewd_loop1_label
    "Cowgirl":
        $ tmpInt += 1
        scene anim_sage_ride1_ep11 with dissolve
        pause
        scene anim_sage_ride2_ep11 with dissolve
        pause
        scene anim_sage_ride3_ep11 with dissolve
        pause
        jump ep11_sage_lewd_loop1_label
    "Reverse cowgirl":
        $ tmpInt += 1
        scene anim_sage_rev1_ep11 with dissolve
        pause
        scene anim_sage_rev2_ep11 with dissolve
        pause
        scene anim_sage_rev3_ep11 with dissolve
        pause
        if ep11_sage_love == 2:
            scene ep11_sage_lewd34 with vpunch
            $ renpy.pause(0.5)
            scene ep11_sage_lewd34 with vpunch
            $ renpy.pause(0.5)
            scene ep11_sage_lewd34 with vpunch
            sa "Hnnn... Fuck... Ahh..."
            scene ep11_sage_lewd35 with dissolve
            sa "*{i}Moans{/i}* Fuck, [mc_sage]... Go easy on me. You just made me cum."
        jump ep11_sage_lewd_loop1_label
    "Blowjob":
        scene anim_sage_bj1_ep11 with dissolve
        pause
        jump ep11_sage_lewd_loop1_label
    "Doggystyle":
        $ tmpInt += 1
        scene anim_sage_doggy1_ep11 with dissolve
        pause
        scene anim_sage_doggy2_ep11 with dissolve
        pause
        scene anim_sage_doggy3_ep11 with dissolve
        pause
        jump ep11_sage_lewd_loop1_label
    "Standing":
        $ tmpInt += 1
        scene anim_sage_stand1_ep11 with dissolve
        pause
        scene anim_sage_stand2_ep11 with dissolve
        pause
        jump ep11_sage_lewd_loop1_label
    "Sideways":
        $ tmpInt += 1
        scene anim_sage_side1_ep11 with dissolve
        pause
        scene anim_sage_side2_ep11 with dissolve
        pause
        jump ep11_sage_lewd_loop1_label
    "Cum" if tmpInt > 4:
        mc "I'm cumming..."
        menu:
            "Facial":
                scene anim_sage_cum_ep11 with dissolve
                pause
                scene anim_sage_cum2_ep11 with dissolve
                pause
            "On ass":
                scene anim_sage_doggy2_ep11 with dissolve
                pause
                scene ep11_sage_lewd24 at vpunch, cum2
                $ renpy.pause(0.5)
                scene ep11_sage_lewd24 at vpunch, cum2
                $ renpy.pause(0.5)
                scene ep11_sage_lewd24 at vpunch, cum2
                mc "Ahh!"
                scene ep11_sage_lewd25 with dissolve
                $ renpy.pause()
            "Creampie":
                scene anim_sage_stand2_ep11 with dissolve
                pause
                scene ep11_sage_lewd26 at vpunch, cum1
                $ renpy.pause(0.5)
                scene ep11_sage_lewd26 at vpunch, cum1
                $ renpy.pause(0.5)
                scene ep11_sage_lewd26 at vpunch, cum1
                mc "Ahh!"
                scene ep11_sage_lewd27 with dissolve
                $ renpy.pause()
            "On belly":
                scene anim_sage_miss2_ep11 with dissolve
                pause
                scene ep11_sage_lewd28 at vpunch, cum2
                $ renpy.pause(0.5)
                scene ep11_sage_lewd28 at vpunch, cum2
                $ renpy.pause(0.5)
                scene ep11_sage_lewd28 at vpunch, cum2
                mc "Ahh!"
                scene ep11_sage_lewd29 with dissolve
                $ renpy.pause()

scene ep11_sage_lewd30 with dissolve
$ renpy.pause()
scene ep11_sage_lewd31 with dissolve
$ renpy.pause()
scene ep11_sage_lewd32 with dissolve
$ renpy.pause()
scene ep11_sage_lewd33 with dissolve
$ renpy.pause()

$ renpy.end_replay()
$ persistent.ep11_lewd_sage = True
$ calcScenes()
if ep11_sage_love == 2:
    $ new_bio("Sage", "I told Sage I loved her, and she reciprocated. We had sex on Bella's couch.")
else:
    $ new_bio("Sage", "I told Sage I loved her, and we had sex on Bella's couch.")
$ mphone_stats_add_girl_s3("sage","You had sex with Sage on Bella's couch in episode 11.")

if not persistent.ep11_card11:
    $ persistent.ep11_card11 = True
    $ persistent.rew_2d_unlocked += 1
    $ persistent.chat_new_rewards = True
    $ calcRenders()
    show screen srmsg
    $ renpy.pause(3)
    hide screen srmsg

if wt_ep9_branch_numbers != 1:
           "scrappy" "Watch the scene again on other paths?"
           menu:
               "Yes":
                  jump wt_ep11_bella_party_label
               "No. Continue the game.":
                   if ep11_zoey_kiss == 2:
                        jump ep11_pp_zoey_end2b_label
                   else:
                        pass    

jump ep11_gift_label

label ep11_sage2_lewd_label:
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
    if persistent.mc_camila == None:
        $ mc_camila = name
    else:
        $ mc_camila = persistent.mc_camila
    if persistent.camila == None:
        $ camila = "Camila"
    else:
        $ camila = persistent.camila
    $ sage_dik = 0
    play music "music/ep11/licensed_music/track178.mp3"
    queue music ["music/ep11/licensed_music/track177.mp3","music/ep11/licensed_music/track181.mp3","music/ep11/licensed_music/track178.mp3"]
hide screen new_phone_screen
$ sage_dik += 1
scene ep11_sage2_lewd1 with wipeleft
sa "Camila?"
scene ep11_sage2_lewd2 with dissolve
cam "No way! I thought you guys were joking."
scene ep11_sage2_lewd4 with dissolve
sa "Then why did you show up?"
scene ep11_sage2_lewd3 with dissolve
cam "In case you weren't."
cam "Are you sure about this?"
scene ep11_sage2_lewd5 with dissolve
sa "Yeah, I think we decided that we are."
sa "To be clear, this is a one-time thing."
scene ep11_sage2_lewd6 with dissolve
cam "It's just sex."
scene ep11_sage2_lewd7 with dissolve
$ renpy.pause()
scene ep11_sage2_lewd8 with dissolve
sa "*{i}Smack{/i}*"
scene ep11_sage2_lewd9 with dissolve
$ renpy.pause()
scene ep11_sage2_lewd10 with dissolve
sa "There is one rule..."
scene ep11_sage2_lewd11 with dissolve
cam "I won't tell anyone."
scene ep11_sage2_lewd10 with dissolve
sa "Ok, make it two rules."
sa "And no kissing him."
scene ep11_sage2_lewd11 with dissolve
cam "No kisses... Ok."
scene ep11_sage2_lewd12 with dissolve
sa "Come."
scene ep11_sage2_lewd13 with dissolve
$ renpy.pause()
scene ep11_sage2_lewd14 with dissolve
$ renpy.pause()
play sound "sound_effects/clothes.mp3"
scene ep11_sage2_lewd15 with dissolve
$ renpy.pause()
scene ep11_sage2_lewd16 with dissolve
sa "Who do you want to do it?"
scene ep11_sage2_lewd17 with dissolve
menu:
    "Blowjob from Sage":
        mc "You, of course."
        jump ep11_sage2_lewd_loop1a_label
    "Blowjob from Camila":
        mc "Let's have Camila do it."
        jump ep11_sage2_lewd_loop1b_label
    "Blowjob from both":
        mc "Both of you at the same time, of course."
        jump ep11_sage2_lewd_loop1c_label


label ep11_sage2_lewd_loop1_label:
menu:
    "Blowjob from Sage":
        label ep11_sage2_lewd_loop1a_label:
        scene anim_sc_bj1_ep11 with dissolve
        sa "*{i}Suck suck{/i}*"
        pause
        scene anim_sc_bj2_ep11 with dissolve
        sa "*{i}Glug glug{/i}*"
        cam "Look at her go. She knows how to do that, doesn't she?"
        mc "Yeah, she knows how I like it..."
        pause
        jump ep11_sage2_lewd_loop1_label
    "Blowjob from Camila":
        label ep11_sage2_lewd_loop1b_label:
        scene anim_sc_bj3_ep11 with dissolve
        cam "*{i}Suck suck{/i}*"
        sa "She's going deep, isn't she?"
        mc "It's hitting the back of her throat... Fuck..."
        pause
        scene anim_sc_bj4_ep11 with dissolve
        sa "I bet you didn't think you'd be sucking my boyfriend's dick tonight. Do you like it?"
        cam "Mmmppfh."
        sa "Yeah, you love it, don't you?"
        pause
        jump ep11_sage2_lewd_loop1_label
    "Blowjob from both":
        label ep11_sage2_lewd_loop1c_label:
        scene anim_sc_bj5_ep11 with dissolve
        sa "Do it together with me."
        cam "*{i}Lick lick{/i}*"
        mc "Ahh... Yes... It's so fucking hot seeing you both go at it like that."
        pause
        jump ep11_sage2_lewd_loop1_label
    "Continue":
        $ renpy.pause(0.5)

scene ep11_sage2_lewd18 with dissolve
sa "Alright, [mc_sage]... This is your surprise."
scene ep11_sage2_lewd19 with dissolve
mc "Merry Christmas..."
scene ep11_sage2_lewd20 with dissolve
sa "Make it count... What do you wanna do to us?"
scene ep11_sage2_lewd21 with dissolve
label ep11_sage2_lewd_loop2_label:
menu:
    "Spanking":
        scene ep11_sage2_lewd22 with dissolve
        mc "Such naughty girls need a good spanking."
        scene bg anim_sc_spank1_ep11 movie with dissolve
        sa "Ahh! Yes..."
        cam "Hngn..."
        mc "Yes, take it!"
        pause
        scene bg anim_sc_spank2_ep11 movie with dissolve
        mc "Your asses look so good together. I wanna fuck them both at the same time and shoot my load all over them."
        pause
        jump ep11_sage2_lewd_loop2_label
    "Finger them":
        menu:
            "Vaginal":
                scene anim_sc_finger1_ep11 with dissolve
                sa "Yes! Deeper, [mc_sage]. Push your fingers into our holes."
                cam "*{i}Moans{/i}*"
                pause
                scene anim_sc_finger2_ep11 with dissolve
                mc "Damn, you're both getting so wet already. I love it."
                pause
            "Anal":
                scene anim_sc_finger3_ep11 with dissolve
                sa "Yes! Deeper, [mc_sage]. Push your fingers into our holes."
                pause
                scene anim_sc_finger3b_ep11 with dissolve
                cam "*{i}Moans{/i}*"
                pause
                scene anim_sc_finger4_ep11 with dissolve
                mc "Those are some tight asses... It makes me wanna shove my cock in them."
                pause
        jump ep11_sage2_lewd_loop2_label
    "Eat Camila (Anal)":
        scene ep11_sage2_lewd23 with dissolve
        sa "Let's eat her out together. I'll take the front, and you'll take the back."
        scene anim_sc_eat1_ep11 with dissolve
        cam "Oh my fucking God! *{i}Moans{/i}* Ahhh!!!"
        sa "*{i}Lick suck munch{/i}*"
        pause
        scene ep11_sage2_lewd24 with dissolve
        cam "Mhm... Keep going... Fuck!"
        scene anim_sc_eat2_ep11 with dissolve
        mc "*{i}Lick lick{/i}*"
        cam "Yes, that's it... Hnnn..."
        pause
        jump ep11_sage2_lewd_loop2_label
    "Eat Sage":
        scene ep11_sage2_lewd25 with dissolve
        sa "I wanna feel your wet tongues in me at the same time."
        scene anim_sc_eat3_ep11 with dissolve
        cam "*{i}Lick lick{/i}*"
        sa "Yes, there we go... *{i}Moans{/i}* That's some good teamwork."
        scene anim_sc_eat3b_ep11 with dissolve
        mc "*{i}Lick lick{/i}*"
        sa "That feels so good..."
        mc "(Damn... Camila is pleasuring us both at the same time.)"
        pause
        jump ep11_sage2_lewd_loop2_label
    "Double assjob":
        scene ep11_sage2_lewd26 with dissolve
        mc "Can you try to massage my dick with your asses at the same time? Take one side of it each and squeeze it together."
        scene ep11_sage2_lewd27 with dissolve
        cam "Do you mean like this?"
        scene ep11_sage2_lewd28 with dissolve
        mc "Yeah, push them together hard and squat up and down..."
        scene anim_sc_assjob_ep11 with dissolve
        mc "Fuck... Yes... Exactly like that. Keep up the pressure."
        cam "Your boyfriend is into some weird stuff, haha."
        sa "You don't know the half of it. Haha!"
        pause
        scene anim_sc_assjob2_ep11 with dissolve
        pause
        jump ep11_sage2_lewd_loop2_label
    "Double titjob":
        scene ep11_sage2_lewd29 with dissolve
        mc "I wanna feel your tits on my cock at the same time."
        scene ep11_sage2_lewd30 with dissolve
        sa "Oh, we'll tease you if you want it."
        scene anim_sc_boobjob_ep11 with dissolve
        cam "Yeah, we got this..."
        mc "Mhm... That's it."
        sa "Shh... Relax and enjoy it."
        pause
        scene anim_sc_boobjob2_ep11 with dissolve
        sa "Feel how our nipples graze the tip of your dick."
        sa "The slight touch of it... So soft against your hard cock."
        pause
        jump ep11_sage2_lewd_loop2_label
    "Continue":
        $ renpy.pause(0.5)

scene ep11_sage2_lewd31 with dissolve
mc "Fuck, I can't stay cool anymore. I need to fuck you."
scene ep11_sage2_lewd32 with dissolve
sa "Are you up for anything, Camila?"
scene ep11_sage2_lewd33 with dissolve
cam "What do you mean by \"anything\"?"
scene ep11_sage2_lewd32 with dissolve
sa "Is there anything you won't do?"
scene ep11_sage2_lewd33 with dissolve
cam "If you mean like if he can fuck my ass, I'm ok with that."
scene ep11_sage2_lewd32 with dissolve
sa "It's up to [mc_sage] then to choose what he wants..."
$ tmpInt = 0
scene ep11_sage2_lewd34 with dissolve
label ep11_sage2_lewd_loop3_label:
menu:
    "Doggystyle (Sage)":
        $ tmpInt += 1
        scene anim_sc_doggy1_ep11 with dissolve
        sa "Hngn, yes! Fuck me, [mc_sage]!"
        cam "*{i}Moans{/i}*"
        sa "Is he doing something to you?"
        cam "Yeah. His finger is inside me... It feels so good, but I can't wait to have that cock penetrate me."
        pause
        scene anim_sc_doggy2_ep11 with dissolve
        sa "I'll let you have it after he fucks me some more... *{i}Moans{/i}*"
        pause
        jump ep11_sage2_lewd_loop3_label
    "Doggystyle (Camila, Anal)":
        $ tmpInt += 1
        scene ep11_sage2_lewd35 with dissolve
        sa "Push that cock inside her asshole, [mc_sage]. I wanna see if she can take it."
        scene ep11_sage2_lewd36 with dissolve
        cam "Hngn..."
        scene ep11_sage2_lewd37 with dissolve
        cam "Ahhh! Fuck! Yes..."
        scene anim_sc_doggy3_ep11 with dissolve
        cam "*{i}Moans{/i}*"
        sa "Damn... I didn't think you had it in you."
        cam "Hngn... I have it in me, alright - all of it."
        pause
        scene anim_sc_doggy4_ep11 with dissolve
        mc "Yeah, fucking take it, [camila]."
        pause
        jump ep11_sage2_lewd_loop3_label
    "Missionary (Sage)":
        $ tmpInt += 1
        scene anim_sc_miss3_ep11 with dissolve
        cam "You guys are so hot to watch..."
        mc "Yeah? Enjoying the view?"
        cam "Yeah, I get horny from watching you fuck her."
        pause
        scene anim_sc_miss4_ep11 with dissolve
        sa "*{i}Moans{/i}* He's got a hot body, hasn't he?"
        cam "Mhm... All that working out paid off. Damn..."
        pause
        scene anim_sc_miss5_ep11 with dissolve
        pause
        jump ep11_sage2_lewd_loop3_label
    "Missionary (Camila)":
        $ tmpInt += 1
        scene anim_sc_miss1_ep11 with dissolve
        sa "Yeah, fuck her, [mc_sage]. She wants it."
        sa "Give her the full length of your cock."
        cam "*{i}Moans{/i}* Yes! Yes! Give it..."
        pause
        scene anim_sc_miss2_ep11 with dissolve
        sa "Look how sexy she is. Enjoy her as much as you can, [mc_sage]. After tonight, you're all mine again."
        pause
        jump ep11_sage2_lewd_loop3_label
    "Reverse cowgirl (Sage, Anal)":
        $ tmpInt += 1
        scene ep11_sage2_lewd38 with dissolve
        sa "Mmm... I wanna feel you inside my ass."
        scene anim_sc_rev1_ep11 with dissolve
        sa "*{i}Moans{/i}* Hnnn..."
        mc "Fuck, that's tight..."
        pause
        scene anim_sc_rev2_ep11 with dissolve
        cam "*{i}Moans{/i}* Ride his cock hard... He's loving it."
        pause
        jump ep11_sage2_lewd_loop3_label
    "Cowgirl (Camila)":
        $ tmpInt += 1
        scene ep11_sage2_lewd39 with dissolve
        sa "Haha, this reminds me of Dots. Only this time..."
        scene ep11_sage2_lewd40 with dissolve
        sa "...he's fully inside you."
        scene anim_sc_ride1_ep11 with dissolve
        sa "Ride him... Ride him hard!"
        cam "*{i}Moans{/i}*"
        pause
        scene anim_sc_ride2_ep11 with dissolve
        cam "Fuck... [mc_camila]... I think I'm gonna cum..."
        sa "Make her cum, [mc_sage]! She deserves it."
        menu:
            "Make her cum":
                mc "Cum, [camila]... Cum on my dick!"
                scene ep11_sage2_lewd41 with vpunch
                cam "Ahhh!!!"
                scene ep11_sage2_lewd42 with vpunch
                cam "Holy... *{i}Moans{/i}*"
                scene ep11_sage2_lewd43 with dissolve
                cam "*{i}Phew{/i}* Fuck, [mc_camila]... Hngnn..."
            "Deny her":
                scene ep11_sage2_lewd45 with dissolve
                mc "No, she doesn't deserve it. Not yet..."
                scene ep11_sage2_lewd44 with dissolve
                cam "Hnnn... You tease."
                pause
        jump ep11_sage2_lewd_loop3_label
    "Standing (Sage, Anal)":
        $ tmpInt += 1
        scene anim_sc_stand1_ep11 with dissolve
        sa "Yes, give it to me. Give it..."
        cam "I hope no one walks in on us right now."
        sa "Haha, why not? We could make them join."
        cam "Oh, wow! Haha! You're horny as hell now, aren't you?"
        pause
        scene anim_sc_stand2_ep11 with dissolve
        sa "Hngnn... Yes... Fuck... I've been horny all night. The more the merrier, right?"
        pause
        scene anim_sc_stand3_ep11 with dissolve
        sa "[mc_sage]... You're fucking me so good... *{i}Moans{/i}*"
        pause
        jump ep11_sage2_lewd_loop3_label
    "Standing (Camila, Anal)":
        $ tmpInt += 1
        scene anim_sc_stand4_ep11 with dissolve
        cam "Fuck me, [mc_camila]... Fuck me!"
        sa "*{i}Suck suck{/i}* Mmmpff... Yes, fuck her ass, [mc_sage]. Fuck it good."
        pause
        scene anim_sc_stand5_ep11 with dissolve
        sa "*{i}Suck suck{/i}*"
        pause
        jump ep11_sage2_lewd_loop3_label
    "Cum" if tmpInt > 4:
        mc "I'm getting close... I wanna cum..."

menu:
    "Creampie (Sage)":
        scene anim_sc_doggy1_ep11 with dissolve
        sa "Cum inside me, [mc_sage]. Fill me with that hot stuff."
        scene ep11_sage2_lewd52 at vpunch, cum1
        $ renpy.pause(0.5)
        scene ep11_sage2_lewd52 at vpunch, cum1
        $ renpy.pause(0.5)
        scene ep11_sage2_lewd52 at vpunch, cum1
        mc "Ahh..."
        scene ep11_sage2_lewd53 with dissolve
        cam "Nothing for me?"
        sa "No one said that. Come here and give it a taste."
        scene ep11_sage2_lewd54 with dissolve
        cam "*{i}Smack lick{/i}*"
    "Facial":
        scene anim_sc_cum2_ep11 with dissolve
        sa "Shoot it all over us. Give us a taste of your cum, [mc_sage]."
        cam "Yes... Give me your cum."
        pause
        scene ep11_sage2_lewd48 at vpunch, cum3
        $ renpy.pause(0.5)
        scene ep11_sage2_lewd48 at vpunch, cum3
        $ renpy.pause(0.5)
        scene ep11_sage2_lewd48 at vpunch, cum3
        mc "Ahh..."
        scene ep11_sage2_lewd49 with dissolve
        cam "*{i}Lick lick{/i}*"
        sa "Mmm... *{i}Smack{/i}*"
        cam "It tastes so good..."
    "On asses":
        scene anim_sc_cum3_ep11 with dissolve
        sa "Shoot it all over our asses, [mc_sage]."
        cam "Yes... Cover us with your hot cum."
        pause
        scene ep11_sage2_lewd50 at vpunch, cum3
        $ renpy.pause(0.5)
        scene ep11_sage2_lewd50 at vpunch, cum3
        $ renpy.pause(0.5)
        scene ep11_sage2_lewd50 at vpunch, cum3
        mc "Ahh..."
        scene ep11_sage2_lewd51 with dissolve
        sa "That's a lot of cum on my ass. Did you even get any on yours?"
        cam "Haha, I could ask you the same because I am covered."
        sa "Haha! He must have been that horny then."
    "On tits":
        scene anim_sc_cum1_ep11 with dissolve
        sa "Shoot it all over our breasts, [mc_sage]."
        cam "Yes... Cover us with your hot cum."
        pause
        scene ep11_sage2_lewd46 at vpunch, cum3
        $ renpy.pause(0.5)
        scene ep11_sage2_lewd46 at vpunch, cum3
        $ renpy.pause(0.5)
        scene ep11_sage2_lewd46 at vpunch, cum3
        mc "Ahh..."
        scene ep11_sage2_lewd47 with dissolve
        sa "Now, that's what I call a pearl necklace."
        cam "Mmm..."

$ renpy.end_replay()
$ persistent.ep11_lewd_sage2 = True
$ calcScenes()
$ new_bio("Sage", "I had a threesome with Sage and Camila in the HOTs' living room.")
$ new_bio("Camila", "I had a threesome with Sage and Camila in the HOTs' living room.")
$ mphone_stats_add_girl_s3("sage","You had a threesome with Sage and Camila in the HOTs' living room in episode 11.")
$ mphone_stats_add_girl_s3("camila","You had a threesome with Sage and Camila in the HOTs' living room in episode 11.")
if not persistent.ep11_card12:
    $ persistent.ep11_card12 = True
    $ persistent.rew_2d_unlocked += 1
    $ persistent.chat_new_rewards = True
    $ calcRenders()

scene ep11_sage2_lewd55 with dissolve
cam "Thanks for this, guys... It was fun and exciting."
scene ep11_sage2_lewd56 with dissolve
sa "We're the ones who should thank you. It was hot, and you respected our boundaries."
scene ep11_sage2_lewd57 with dissolve
cam "Of course. Truth be told, I needed to get laid, so I didn't even hesitate when you asked."
cam "I'll be able to get a good night's sleep tonight."
scene ep11_sage2_lewd56 with dissolve
sa "Are you not going back to the party?"
scene ep11_sage2_lewd57 with dissolve
cam "I think it's about to die down. I already saw some leave before I left."
scene ep11_sage2_lewd58 with dissolve
cam "People wondered where you went, [name]."
scene ep11_sage2_lewd59 with dissolve
mc "Oh, they did? I hope they still had fun without me."
scene ep11_sage2_lewd61 with dissolve
sa "Do you need to head back there?"
scene ep11_sage2_lewd60 with dissolve
mc "No, I'm staying with you tonight."
scene ep11_sage2_lewd57 with dissolve
cam "I'm gonna prepare for bed. See you two tomorrow."

scene ep11_sage2_lewd62 with dissolve
mc "What a night... It didn't end up in any way I could have imagined."
scene ep11_sage2_lewd63 with dissolve
sa "Did the threesome feel weird to you?"
scene ep11_sage2_lewd62 with dissolve
mc "No, not at all."
stop music fadeout 3
scene ep11_sage2_lewd63 with dissolve
sa "Ok... Good."
scene ep11_sage2_lewd64 with dissolve
$ renpy.pause()

if wt_ep9_branch_numbers != 1:
           "scrappy" "Watch the scene again on other paths?"
           menu:
               "Yes":
                  jump wt_ep11_bella_party_label
               "No. Continue the game.":
                   if ep11_zoey_kiss == 2:
                        jump ep11_pp_zoey_end2b_label
                   else:
                        pass

jump ep11_gift_label
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
