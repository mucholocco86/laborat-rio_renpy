label ep10_jill_intro_label:
scene ep10_jill_intro1 with dissolve
$ renpy.pause()
scene ep10_jill_intro2 with dissolve
$ renpy.pause()
scene ep10_jill_intro3 with dissolve
$ renpy.pause()
scene ep10_jill_intro4 with dissolve
ji "Thanks for the party yesterday."
ji "I'm amazed at how great it was. You guys must have worked so hard to make it happen."
if (minigames and pp_current_party_happiness[3] > 2) or (not minigames and pp_current_party_happiness[3] == 1):
    scene ep10_jill_intro6 with dissolve
    jb "Yeah, it was one of the great ones. My throat is sore today. I laughed and talked way too much."
    scene ep10_jill_intro10 with dissolve
    mc "It was a team effort. It wouldn't have been good without you guys."
elif (minigames and pp_current_party_happiness[3] > 1) or (not minigames and pp_current_party_happiness[3] == 0):
    scene ep10_jill_intro6 with dissolve
    jb "Yeah, it was all right. I had a good time."
    scene ep10_jill_intro10 with dissolve
    mc "Me too. It was fun!"
else:
    scene ep10_jill_intro7 with dissolve
    jb "That's good. It was okay-ish, for me. I honestly wish we did more with it."
    scene ep10_jill_intro8 with dissolve
    mc "Sorry about that. I did my best."
    scene ep10_jill_intro9 with dissolve
    jb "You'll get better at it."

scene ep10_jill_intro11 with dissolve
le "My skin's all itchy after wearing that makeup."
le "I don't know how girls do it."
scene ep10_jill_intro5 with dissolve
ji "Is it itchy? Maybe you had an allergic reaction to it."
scene ep10_jill_intro11 with dissolve
le "I won't try it again, so I'll never know."
scene ep10_jill_intro15 with dissolve
jb "Whatever happened to Jamie last night?"
if (ep8_leons_side and not ep9_leons_side) or (not ep8_leons_side and ep9_leons_side):
    scene ep10_jill_intro12 with dissolve
    le "He changed costumes for me and we ended up having a great end to the night."
    scene ep10_jill_intro13 with dissolve
    mc "That's nice. I'm happy you guys made up."
    scene ep10_jill_intro11 with dissolve
    le "Yeah... It felt like old times."
    le "But I'm still bummed out we had to fight again."
    le "Fucking Dany... Ugh... She's a pain in the ass."
else:
    scene ep10_jill_intro11 with dissolve
    le "Pff... He left with Dany. I don't know what's wrong with him these days."
    le "Or...I do know what's wrong with him. Dany is what's wrong with him."
le "Girlfriends... They can be toxic."
scene ep10_jill_intro14 with dissolve
le "No offense to you guys."
scene ep10_jill_intro13 with dissolve
if persistent.mod_wt_enabled: 
                    $mod_choices = ["(+Jill)","(-Isabella)","(-DIK)","(+DIK)","(Sage or Sarah scene)","(Sarah scene)","","","","","","" ]
                    #[m_c1][mod_choices[0]]
menu:
    "None taken [m_c1][mod_choices[0]]":
        $ RPjill += 1
        mc "None taken. There's nothing toxic about Jill."
        scene ep10_jill_intro16 with dissolve
        ji "..."
    "We have to accept it":
        mc "There's nothing we can do about it but accept his choices."
        scene ep10_jill_intro14 with dissolve
        le "I'll never be able to accept Dany."
scene ep10_jill_intro17 with dissolve
jb "How did you two happen?"
scene ep10_jill_intro18 with dissolve
mc "Us? Well, I met her when I first arrived here and it didn't take us long to start dating."
mc "But it wasn't until recently we got together as a couple."
scene ep10_jill_intro19 with dissolve
mc "Hey, Rusty. How's it going?"
scene ep10_jill_intro20 with dissolve
rs "Hey... I'm battling a nasty hangover."
scene ep10_jill_intro22 with dissolve
ji "Hi, Rusty."
scene ep10_jill_intro21 with dissolve
rs "Hi."
rs "So, you two...huh?"
scene ep10_jill_intro23 with dissolve
ji "Mhm."
scene ep10_jill_intro24 with dissolve
rs "[name] is a hell of a guy."
scene ep10_jill_intro25 with dissolve
rs "Ugh... Nope. This hangover needs coffee and solitude."
rs "Later, guys."
scene ep10_jill_intro26 with dissolve
mc "How are you feeling? Any hangover?"
scene ep10_jill_intro27 with dissolve
ji "I have a slight headache, but it's not too bad. What about you?"
scene ep10_jill_intro26 with dissolve
mc "I'm feeling pretty fine."
mc "But I can't say I'm excited for the day. We have a lot to clean."
scene ep10_jill_intro27 with dissolve
ji "I can stay and help out."
scene ep10_jill_intro26 with dissolve
mc "No, it's fine. The HOTs will help us."
scene ep10_jill_intro29 with dissolve
de "[mc_de_up]?"
scene ep10_jill_intro30 with dissolve
mc "Morning, or whatever it is."
scene ep10_jill_intro29 with dissolve
de "A word?"
scene ep10_jill_intro30 with dissolve
mc "Sure."
scene ep10_jill_intro28 with dissolve
mc "*{i}Smack{/i}* I'll be right back."
scene ep10_jill_intro31 with dissolve
$ renpy.pause()
if assman:
    scene ep10_jill_intro33b with dissolve
    ji "So, um... Why do you call him that?"
    scene ep10_jill_intro33 with dissolve
    jb "Call him what?"
    scene ep10_jill_intro33b with dissolve
    ji "Ass man."
    scene ep10_jill_intro33 with dissolve
    jb "It's only Derek who does and I don't know why. I wouldn't put too much weight on it if I were you."
    jb "Derek and [name] are very close. That kind of banter happens."
    scene ep10_jill_intro33b with dissolve
    ji "Ah, I see."
scene ep10_jill_intro33 with dissolve
if ep9_winner == "Jill":
    jb "By the way, your banana costume was awesome. I was cheering loudly for you to win."
else:
    jb "By the way, your banana costume was awesome."
scene ep10_jill_intro32 with dissolve
if ep9_winner == "Jill":
    ji "Haha, you did? I have no idea what to do with that trophy, but I guess I should feel flattered to have won."
else:
    ji "Oh, thank you. It wasn't easy to wear all night, but it was funny."
ji "[name] told me you baked the cakes for yesterday."
scene ep10_jill_intro33 with dissolve
jb "Yeah, I did."
scene ep10_jill_intro32 with dissolve
ji "They were delicious. Do you bake a lot?"
$ new_bio("Jill", "The morning after Halloween, Jill tried to bond with my friends during breakfast.")
jump ep10_dik2_intro_label

label ep10_jill_solo_label:
play music "music/ep4/gentle_theme_guitar.mp3"
if ep8_midterms_cheated == "DIK":
    scene ep10_jill_solo2 with wipeleft
    mc "I'm here. Sorry for keeping you waiting."
    scene ep10_jill_solo3 with dissolve
    ji "It's ok."
else:
    scene ep10_jill_solo1 with wipeleft
    mc "I've been waiting to be alone with you."

scene ep10_jill_solo4 with dissolve
mc "Come here."
scene ep10_jill_solo5 with dissolve
mc "I need you today."
scene ep10_jill_solo6 with dissolve
ji "[name], wait... Before we kiss, I need to talk to you about something."
scene ep10_jill_solo5 with dissolve
mc "Oh? This isn't about your STD test, right?"
scene ep10_jill_solo6 with dissolve
ji "*{i}Scoffs{/i}* No."

if ep9_told_jill:
    scene ep10_jill_solo5 with dissolve
    mc "Is it about Bianca?"
    scene ep10_jill_solo6 with dissolve
    ji "Not that either."

scene ep10_jill_solo7 with dissolve
mc "Ok. What's up?"
scene ep10_jill_solo8 with dissolve
ji "*{i}Sigh{/i}* I saw the posters on campus today."
ji "I believe you're on them. I mean, I recognized you from them..."
scene ep10_jill_solo7 with dissolve
mc "Yeah, I know. It sucks... Someone is spreading the pictures we have on a wall in the mansion."
mc "Maybe you saw them at Halloween?"
scene ep10_jill_solo8 with dissolve
ji "No, I didn't. I mean, I think I saw some of the pictures, but I didn't pay attention to them until today."
ji "I'm sorry they spread like that. It must be uncomfortable for you."
scene ep10_jill_solo7 with dissolve
mc "Yeah, it is. But I can't do much about it but tear them down."
mc "I bet you feel embarrassed about it, too."
scene ep10_jill_solo9 with dissolve
ji "Yes, I was speechless when I realized it was you."
ji "But that mask you wore helped a bit. At least, people won't know it's you in that picture as easily as I did."
scene ep10_jill_solo7 with dissolve
mc "I can only hope."
scene ep10_jill_solo8 with dissolve
ji "This must be hard for you to deal with."
scene ep10_jill_solo7 with dissolve
mc "It's not what I wished would happen, but it did. I hope it won't keep going for longer than today."
scene ep10_jill_solo10 with dissolve
ji "I'll do my best to support you."
scene ep10_jill_solo11 with dissolve
mc "Thank you."
scene ep10_jill_solo12 with dissolve
ji "However... There was another picture that caught my eye...and I need you to be honest with me."
scene ep10_jill_solo29 with dissolve
ji "This one is from our mansion. Isn't it?"
ji "That's Tybalt's bed."
mc "Yeah. You called it. It's a Hell Week thing at the DIKs."
scene ep10_jill_solo13 with dissolve
ji "And those masks... They look like burglars, don't they?"
ji "It led me to think about a break-in we had at the start of the semester when two burglars entered our mansion and stole things from us."
ji "This was during the time you had your Hell Week."
scene ep10_jill_solo14 with dissolve
ji "Is there anything you'd like to tell me?"
scene ep10_jill_solo15 with dissolve
mc "..."
mc "I'm sorry... It was before I knew you."
scene ep10_jill_solo14 with dissolve
ji "[name]..."
scene ep10_jill_solo15 with dissolve
mc "We had to do it for Hell Week. They wanted us to take funny pictures in Tybalt's room. And we had to enter through your room."
mc "Your window was open."
scene ep10_jill_solo13 with dissolve
ji "Did you steal from me and Tybalt?"
scene ep10_jill_solo15 with dissolve
mc "What? No!"
mc "Wait... Derek stole Tybalt's mounted deer head."
if ep2_stole_money:
    $ RPjill -= 5
    mc "And oh... I may have taken some of your money, but it wasn't a lot and it was just lying there."
    scene ep10_jill_solo16 with dissolve
    ji "Wasn't a lot...? Are you justifying the amount you stole from me? And because something lies somewhere, it's ok to take it?"
    scene ep10_jill_solo15 with dissolve
    mc "No... Fuck, I don't know why I did that. I didn't think clearly. I'll pay you back."

scene ep10_jill_solo14 with dissolve
if ep2_stole_money:
    ji "It's not about the money, [name]. It's more about the underwear you stole and the feeling you left me feel."
else:
    ji "You stole my underwear and left me feeling horrible."
ji "I had trouble sleeping because I felt like my privacy was violated."
scene ep10_jill_solo15 with dissolve
mc "No! I never did that. Tybalt must have stolen those."
scene ep10_jill_solo14 with dissolve
ji "Oh, [name]..."
scene ep10_jill_solo15 with dissolve
mc "I'm telling you the truth! When we were escaping through your window, we saw Tybalt in here. He was standing right over there!"
mc "It looked like he was smelling underwear from your dresser. He saw us and called on security, not that he'd ever admit that."
scene ep10_jill_solo17 with dissolve
mc "Jill... You have to believe me."
mc "I did a shitty thing because of Hell Week, and I should have told you sooner, but part of me wanted to forget about it."
mc "And after getting to know you, I didn't think it mattered anymore."
scene ep10_jill_solo15 with dissolve
mc "That person who did those things wasn't me. It's not who I am."
mc "I didn't steal your underwear. Come on. You can't believe that."
mc "With everything Tybalt has done to you and me... You have to see through him by now."
scene ep10_jill_solo18 with dissolve
mc "And you know me. Don't you? You trust me, right?"
scene ep10_jill_solo14 with dissolve
ji "I trust you, but this makes me feel weird."
scene ep10_jill_solo18 with dissolve
mc "I'm so sorry. If you want, I can show you the pictures we took."
mc "I don't want you to have any questions about this if you have any doubts."
mc "We can call Derek, and he'll tell you the same story. He was there with me."
scene ep10_jill_solo14 with dissolve
ji "[name], it's too late for you to tell me this. I found out on my own. You should have told me a lot sooner."
scene ep10_jill_solo15 with dissolve
mc "..."
mc "You're right. I should have. And I'd like to think that I would have told you eventually. Not that it helps."
scene ep10_jill_solo18 with dissolve
mc "I'm sorry. Can you forgive me?"
scene ep10_jill_solo19 with dissolve
ji "Of course, I can."
ji "And I believe you. If I couldn't trust you, I wouldn't be with you."
ji "But I had to ask because this entire day I've walked around thinking that there was something you didn't tell me..."
ji "...and I was right."
scene ep10_jill_solo20 with dissolve
ji "But hearing you tell the story, I have no reason to doubt you."
ji "I can see it in your eyes. You're telling me the truth."
scene ep10_jill_solo21 with dissolve
mc "Thank you... I really am."
mc "I did a lot of bad things during Hell Week."
scene ep10_jill_solo22 with dissolve
ji "I don't need to know what you did. I know that fraternity hazing is a bad thing."
ji "And you're allowed to have secrets, as long as our relationship isn't built on lies."
scene ep10_jill_solo23 with dissolve
$ renpy.pause()

scene ep10_jill_solo24 with dissolve
$ renpy.pause()
scene ep10_jill_solo25 with dissolve
ji "Don't look so sad. You can kiss me now."
scene ep10_jill_solo24 with dissolve
mc "..."
scene ep10_jill_solo25 with dissolve
ji "[name]?"
scene ep10_jill_solo26 with dissolve
mc "Jill, I don't want to ruin this relationship. I want this to work. I don't feel good about myself right now."
scene ep10_jill_solo28 with dissolve
ji "*{i}Smack{/i}*"
scene ep10_jill_solo25 with dissolve
ji "That's because you're a good person at heart and have a conscience."
scene ep10_jill_solo27 with dissolve
ji "But maybe next time...you can figure out a way not to break in here."
scene ep10_jill_solo26 with dissolve
mc "I'll hammer it in that your room and privacy are off-limits."

scene ep10_jill_solo30 with dissolve
$ renpy.pause()
scene ep10_jill_solo31 with dissolve
$ renpy.pause()
scene ep10_jill_solo32 with dissolve
mc "What about you? Are you ok?"
scene ep10_jill_solo33 with dissolve
ji "I thought the problems surrounding us would disappear after we became a couple, but I guess that was naive."
scene ep10_jill_solo36 with dissolve
mc "I don't think either of us could have anticipated this."
scene ep10_jill_solo33 with dissolve
ji "It's been a wild day. It's fair to say there have been lots of surprises."
ji "What Josy and Maya told me...that was another big one."
if ep9_jm_sad:
    scene ep10_jill_solo34 with dissolve
    ji "Can you help me wrap my head around something...?"
    scene ep10_jill_solo36 with dissolve
    mc "Around what?"
    scene ep10_jill_solo34 with dissolve
    ji "You told me you dated Josy and broke up with her... But Josy said she's with Maya..."
    scene ep10_jill_solo36 with dissolve
    mc "Do you remember that I said I broke up with two girls?"
    scene ep10_jill_solo33b with dissolve
    ji "Was Maya the other one?"
    scene ep10_jill_solo36 with dissolve
    mc "Yeah... We three dated each other... It's hard to explain it, but if you want to, I can do it."
    scene ep10_jill_solo33b with dissolve
    ji "Maybe another time... Um..."
    scene ep10_jill_solo35 with dissolve
    mc "Jill... I know you might feel weird about this, but what should matter is that you're the only one for me now. Ok?"
    scene ep10_jill_solo33b with dissolve
    ji "Still..."
    ji "I feel sad for Maya... It can't be an easy situation for her."
    scene ep10_jill_solo36 with dissolve
    mc "I've known about it for quite some time and I want to help her with her problems."
else:
    scene ep10_jill_solo36 with dissolve
    mc "Yeah, I've known about it for quite some time."
    mc "It's such a bad situation for Maya, and I want to help her with it."
scene ep10_jill_solo34 with dissolve
if ep9_jm_sad:
    ji "I can see that..."
else:
    ji "I can see that. I think that's wonderful of you."
ji "But I'm honestly concerned. What you guys plan to do doesn't sound very...safe or legal."
scene ep10_jill_solo35 with dissolve
mc "What else can we do? If you have a suggestion, I'm all ears."
scene ep10_jill_solo34 with dissolve
ji "No, I don't have any suggestions. That's why I didn't speak up at the library."
ji "This whole thing worries me... What if something bad happens at Thanksgiving? Will you guys be ok?"
scene ep10_jill_solo35 with dissolve
mc "I see it like this... Worst case scenario, we get caught and thrown out."
scene ep10_jill_solo34 with dissolve
ji "What if he reports you for rummaging around in his office?"
scene ep10_jill_solo36 with dissolve
mc "Do you think what he's doing to Maya sounds legal? Because to me, it sounds like extortion."
scene ep10_jill_solo33b with dissolve
ji "I don't want you to end up doing something you will regret. That's all."
ji "Given what we just talked about, with the break-in... Can't you see why I'm concerned?"
scene ep10_jill_solo35 with dissolve
mc "I see it, but it's not the same thing. This is for a good cause."
mc "This is the first time I felt like we can make a real difference for Maya."
scene ep10_jill_solo36 with dissolve
mc "And I promise I won't take any unnecessary risks. I'm not looking to get into trouble."
mc "If I find out that it's impossible to get the contract during dinner, I won't do it. Ok?"
scene ep10_jill_solo34 with dissolve
ji "Ok... Be careful."
scene ep10_jill_solo36 with dissolve
mc "*{i}Sigh{/i}*"
scene ep10_jill_solo33 with dissolve
ji "Sorry, I didn't mean to put more stress on your shoulders."
scene ep10_jill_solo36 with dissolve
mc "..."
if ep9_jm_sad:
    mc "And I didn't think coming here tonight would do that. Being with you is the best thing I know."
    scene ep10_jill_solo35 with dissolve
    mc "And today, I found so many ways to ruin it...yet you're still lying here next to me. And I ask myself why."
    mc "I don't feel like I deserve you."
    scene ep10_jill_solo33 with dissolve
    ji "You're my boyfriend and I'm your girlfriend. It's not a promise we've made lightly to each other."
    ji "You're allowed to have a past and you're allowed to make mistakes... And even if things you tell me feel weird for me, you haven't ruined anything."
    ji "You're being open and honest with me and that means a lot."
    ji "Weird or not... I want you here next to me because being with you is one of the best things I know too. And I'm done with letting that get affected by others."
    scene ep10_jill_solo32 with dissolve
    mc "Thanks, Jill... That feels comforting to hear."
else:
    mc "And I didn't think coming here tonight would do that. Being with you is the best thing I know. It's usually more relaxing."
scene ep10_jill_solo37 with dissolve
ji "I can help you relax more if you want."
scene ep10_jill_solo38 with dissolve
mc "How?"
scene ep10_jill_solo39 with dissolve
ji "My Mom used to run her fingers through my hair like this when I was young. It always made me feel sleepy."
scene ep10_jill_solo40 with dissolve
mc "That does feel good."
stop music fadeout 3
scene ep10_jill_solo41 with dissolve
$ renpy.pause()
play music "music/ep10/yoga_for_dummies.mp3"
scene ep10_jill_solo42 with dissolve
ji "You've got to be kidding me!"
scene ep10_jill_solo43 with dissolve
mc "What the hell is that?"
scene ep10_jill_solo42 with dissolve
ji "What do you think it is?"
play sound "sound_effects/season3/window_open.mp3"
scene ep10_jill_solo44 with vpunch
ji "Hey! Do you have to do this tonight? Isn't it enough that you do this in the mornings?"
scene ep10_jill_solo45 with dissolve
$ renpy.pause()
scene ep10_jill_solo46 with dissolve
ji "And he ignores me... Great."
scene ep10_jill_solo47 with dissolve
mc "Want me to say something to him?"
scene ep10_jill_solo48 with dissolve
ji "No. The moment's gone."
scene ep10_jill_solo49 with dissolve
mc "Maybe we should call it a night?"
scene ep10_jill_solo48 with dissolve
ji "No. I don't want him to win... He'll get what he wants if you leave."
scene ep10_jill_solo49 with dissolve
mc "If you want, we can go back to my place."
scene ep10_jill_solo50 with dissolve
ji "Is that what we will resort to every time this happens?"
scene ep10_jill_solo51 with dissolve
mc "No, but I really don't have the energy to deal with him tonight. And I have to get back and discuss the posters with my brothers..."
if ep9_jm_sad or ep2_stole_money:
    scene ep10_jill_solo52b with dissolve
    ji "Then, you should leave."
    scene ep10_jill_solo53b with dissolve
    mc "Are you sure you don't want to come back with me?"
    scene ep10_jill_solo52b with dissolve
    ji "It sounds like you will be busy and it would give me time to digest everything you told me tonight. It was a lot for one day."
    stop music fadeout 3
    scene ep10_jill_solo53b with dissolve
    mc "Ok, you do that... Thanks for being so understanding."
else:
    scene ep10_jill_solo52 with dissolve
    ji "Ok... I'll come with you."
    scene ep10_jill_solo51 with dissolve
    mc "Are you sure?"
    stop music fadeout 3
    scene ep10_jill_solo52 with dissolve
    ji "Yes. I want to be with you tonight."

$ new_bio("Jill", "Jill confronted me about Hell Week, and I told her what happened. She believed me, but it felt like I had disappointed her by doing what I did.")
jump ep10_mc_room_label

label ep10_jb_label:
$ guideSuggestedPage = 122
play music "music/ep6/licensed_music/track35.mp3"
scene ep10_jb1 with wipeleft
$ renpy.pause()
scene ep10_jb2 with dissolve
mc "How are we going to do it?"
scene ep10_jb3 with dissolve
ji "I haven't made up my mind yet."
scene ep10_jb4 with dissolve
mc "Huh? Don't you want to tell her?"
scene ep10_jb5 with dissolve
ji "What? Yes, we're telling her, but I don't know the best way to do it."
ji "I'm trying to put myself in her shoes... What would I want to hear if I were Bianca?"
ji "But all that's making me realize is that there is no good way to tell her this."
scene ep10_jb4 with dissolve
mc "Yeah, she will be bummed out no matter what."
scene ep10_jb5 with dissolve
ji "It's important that we show her our support and that we're here for her."
ji "She will need to feel how much we love and care about her."
scene ep10_jb4 with dissolve
mc "Ok...um...I barely know her, but I'll try my best."
play sound "sound_effects/door_knock.mp3"
"*{i}Doorknock{/i}*"
scene ep10_jb6 with dissolve
bia "Silly Jilly! It's me!"
scene ep10_jb7 with dissolve
ji "Hi, Bianca!"
scene ep10_jb8 with dissolve
bia "[name]! I didn't expect to see you here."
scene ep10_jb9 with dissolve
bia "But I should get used to seeing you wherever Jill goes these days, huh?"
scene ep10_jb10 with dissolve
mc "No, I promise you'll have some alone time with Jill in the future."
scene ep10_jb9 with dissolve
bia "I didn't mean it's bad that you're here. I'm happy to see you."
bia "And thanks for the party again! How amazing was that?"
scene ep10_jb10 with dissolve
mc "It was pretty damn amazing."
scene ep10_jb9 with dissolve
bia "Right!?"
scene ep10_jb11 with dissolve
bia "And, of course, Jill doesn't agree with us. I thought you had a good time."
scene ep10_jb12 with dissolve
ji "I did, but... Um... [name]?"
scene ep10_jb13 with dissolve
mc "Do you want me to...?"
scene ep10_jb14 with dissolve
bia "What are you two up to?"
scene ep10_jb15 with dissolve
ji "Bianca, let's sit down."
scene ep10_jb16 with dissolve
bia "Ok? What's up?"
scene ep10_jb17 with dissolve
ji "We have to tell you something. I wish it weren't this way, but sadly it is."
ji "Matthew is cheating on you."
scene ep10_jb18 with dissolve
bia "Matty?"
scene ep10_jb19 with dissolve
bia "..."
scene ep10_jb18 with dissolve
bia "No way."
scene ep10_jb19 with dissolve
ji "[name]?"
scene ep10_jb20 with dissolve
mc "At the Halloween party, I walked around and checked on everyone..."
mc "And when I went into Rusty's room, I saw Matthew making out with Olivia."
scene ep10_jb21 with dissolve
bia "Olivia!?"
scene ep10_jb22 with dissolve
ji "I'm so sorry, Bianca."
scene ep10_jb23 with dissolve
bia "You must be mistaken. Olivia is with Andy, and Matty would never do that to me."
scene ep10_jb24 with dissolve
mc "I wish I were mistaken, but I confronted Matthew about it, and he got mad and told me to shut up about it."
mc "Sorry, Bianca, but it's the truth."
scene ep10_jb25 with dissolve
bia "..."
scene ep10_jb26 with dissolve
bia "I thought I saw him put his arm around her this summer at our party."
bia "I dismissed it as him being drunk and overly friendly."
bia "Has he been cheating on me with her all this time?"
scene ep10_jb27 with dissolve
ji "We don't know that. What [name] saw at the Halloween party is the only thing we know for sure."
scene ep10_jb26 with dissolve
bia "Olivia!?"
bia "She's supposed to be his friend."
scene ep10_jb24 with dissolve
mc "What do you mean by that?"
scene ep10_jb24b with dissolve
ji "Matthew and Olivia knew each other from before. That's why we hung out as a group with them."
scene ep10_jb28 with dissolve
bia "I wanna punch something!"
scene ep10_jb29 with dissolve
ji "Bianca... I understand how mad you must feel right now."
scene ep10_jb30 with dissolve
bia "You're damned right I'm mad! I'm gonna punch him! How could he do this to me?"
bia "And her? *{i}Grunts{/i}* That two-faced bitch!"
bia "She comes into my home and steals my guy? She's fucking done too!"
scene ep10_jb29 with dissolve
ji "Bianca. Come sit down again. This isn't you."
ji "You're bigger than that. You're such a good person."
scene ep10_jb31 with dissolve
bia "*{i}Sobs{/i}*"
scene ep10_jb32 with dissolve
ji "It's going to be ok. Screw Matthew. And screw Olivia too."
scene ep10_jb33 with dissolve
mc "(Damn... I feel so uncomfortable in these situations...)"
if persistent.mod_wt_enabled: 
                    $mod_choices = ["(+Jill)","(-Isabella)","(-DIK)","(+DIK)","(Sage or Sarah scene)","(Sarah scene)","","","","","","" ]
                    #[m_c1][mod_choices[0]]
menu:
    "Put arm around Bianca [m_c1][mod_choices[0]]":
        $ RPjill += 1
        scene ep10_jb34 with dissolve
        mc "He's not worthy of you. Who in their right mind would cheat on you?"
        scene ep10_jb35 with dissolve
        bia "Are you sure that you saw it? Could you be mistaken? I mean, you were drinking a lot. Even if there's a small possibility-"
        scene ep10_jb34 with dissolve
        mc "I wouldn't say this to you if I wasn't sure. You deserved to know it."
        mc "That Matthew hasn't got the balls to tell you and go around your back like this..."
        mc "...it says a lot about him."
        scene ep10_jb35 with dissolve
        bia "He's like cancer!"
        scene ep10_jb34 with dissolve
        mc "Jill and I, we're here for you. No matter what happens, ok?"
        scene ep10_jb36 with dissolve
        $ renpy.pause()
        scene ep10_jb35 with dissolve
        bia "You guys are my true friends."
    "Let Jill handle it":
        scene ep10_jb32 with dissolve
        ji "I'm so sorry, Bianca. I didn't want to upset you, but I had to."
        scene ep10_jb33 with dissolve
        bia "You don't have to feel guilty. You guys haven't done anything wrong."
        bia "You guys are my true friends."
        scene ep10_jb32 with dissolve
        ji "We are. And we are here for you. No matter what happens."

scene ep10_jb37 with fade
$ renpy.pause()
scene ep10_jb38 with dissolve
bia "What should I do now? I have my entire life in that house with him and now I feel disgusted by returning to it."
scene ep10_jb40 with dissolve
ji "You should get the truth from Matthew first. The other decisions will come to you after."
ji "And if you need a place to stay for a couple of days, my bed is big enough for both of us."
scene ep10_jb38 with dissolve
bia "I can't believe I bought a fucking house together with that asshole."
scene ep10_jb40 with dissolve
ji "It will be all right. I'm sure your parents will help out with that too."
scene ep10_jb38 with dissolve
bia "Things moved way too fast for us. I'm such an idiot."
scene ep10_jb39 with dissolve
mc "There's nothing idiotic about it. You followed your heart doing those things."
scene ep10_jb38 with dissolve
bia "I feel like a fool. I feel violated and disgusted."
scene ep10_jb40 with dissolve
ji "Matthew is the fool."
scene ep10_jb38 with dissolve
bia "He is."
bia "I'm going back home now."
scene ep10_jb40 with dissolve
ji "How can we help?"
scene ep10_jb38 with dissolve
bia "I don't need any help. I know what I have to do."
bia "Oh... Can you give me a ride there?"
scene ep10_jb40 with dissolve
ji "Of course."
scene ep10_jb39 with dissolve
mc "Do you want me to come?"
scene ep10_jb40 with dissolve
ji "No, you don't have to. I've got this."
ji "Thank you, [name]. You helped me a lot by being here."
stop music fadeout 3
scene ep10_jb38 with dissolve
bia "Jill, let's go. I'm ready to kick his ass."
$ new_bio("Jill", "Jill asked me to tell Bianca about what I saw Matthew do with Olivia during Halloween, and I did.")
$ new_bio("Bianca", "I told Bianca that Matthew was cheating on her with Olivia. Jill and I tried to console her when she got angry and upset.")

if branchIsabella and wt_ep9_branch_numbers != 1:
    jump ep10_bsolo_label

jump ep10_zoey_hangout_label

label ep10_jill_fam_label:
play music "music/ep8/licensed_music/track61.mp3"
scene ep10_jill_fam1 with wipeleft
$ renpy.pause()
scene ep10_jill_fam2 with dissolve
mc "Nervous?"
mc "Jill?"
scene ep10_jill_fam3 with dissolve
ji "Huh? What was that?"
scene ep10_jill_fam4 with dissolve
mc "I asked if you were nervous. You haven't talked a lot during the ride so far."
scene ep10_jill_fam3 with dissolve
ji "I'm sorry. I guess I am more nervous than I thought I was."
ji "I've never brought someone home like this."
scene ep10_jill_fam4 with dissolve
mc "What are you worried about?"
scene ep10_jill_fam3 with dissolve
ji "That you'd be embarrassed."
scene ep10_jill_fam7 with dissolve
mc "That's so funny. That's my exact worry, too, but that you'd be embarrassed about me."
mc "I haven't done this before either and based on what I know about your family..."
mc "I'm worried I won't fit in."
scene ep10_jill_fam2 with dissolve
ji "..."
mc "Some words of encouragement? Jill?"
scene ep10_jill_fam3 with dissolve
ji "I want to reassure you, but truthfully, I don't know how they will react."
ji "I remember when Lana brought her boyfriend back home."
ji "It was one of the things that started the fights between her and Dad."
scene ep10_jill_fam4 with dissolve
mc "Oh... How was her boyfriend?"
scene ep10_jill_fam3 with dissolve
ji "He was young and stupid and had an attitude about him."
ji "He's not the same person today. He's changed for the better after Lana passed."
ji "Um..."
scene ep10_jill_fam5 with dissolve
ji "You're not like him. But we both know we're from different walks of life."
ji "And since I don't have any other frame of reference..."
scene ep10_jill_fam2 with dissolve
mc "You worry."
scene ep10_jill_fam7 with dissolve
stop music fadeout 3
mc "It will be fine. I'll try to be on my best behavior."
scene ep10_jill_fam6 with dissolve
$ renpy.pause()
$ guideSuggestedPage = 127
scene ep10_jill_fam8 with dissolve
play music "music/ep5/licensed_music/track14.mp3"
ji "We're here!"
scene ep10_jill_fam9 with dissolve
"Hi, sweetheart."
scene ep10_jill_fam10 with dissolve
ji "Hi, Mom!"
scene ep10_jill_fam11 with dissolve
"And this must be [name]."
scene ep10_jill_fam13 with dissolve
mc "Yes, and that would make you..."

if persistent.mod_wt_enabled: 
                    $mod_choices = ["(+Jill)","(-Jill)","(-DIK)","(+DIK)","(Sage or Sarah scene)","(Sarah scene)","","","","","","" ]
                    #[m_c1][mod_choices[0]]

menu:
    mc "(Crap! What the fuck was her name! I'm blanking here!)"
    "Amalie [m_c1][mod_choices[1]]":
        $ RPjill -= 1
        mc "...Amalie."
        scene ep10_jill_fam11 with dissolve
        jim "Almost. Amelia."
        mc "(Damn...)"
    "Amelie [m_c1][mod_choices[1]]":
        $ RPjill -= 1
        mc "...Amelie."
        scene ep10_jill_fam11 with dissolve
        jim "Almost. Amelia."
        mc "(Damn...)"
    "Amelia [m_c1][mod_choices[0]]":
        $ RPjill += 1
        mc "...Amelia."
        scene ep10_jill_fam11 with dissolve
        jim "Indeed, I am."
    "Mrs. Royce":
        mc "...Mrs. Royce."
        scene ep10_jill_fam11 with dissolve
        jim "Oh, please. Call me Amelia."
        scene ep10_jill_fam12 with dissolve
        mc "Amelia, it is!"
        mc "(*{i}Phew{/i}* Nice save!)"
        scene ep10_jill_fam11 with dissolve
jim "Welcome. I must admit I was quite surprised when Jill told me she was bringing a guy home with her."
scene ep10_jill_fam14 with dissolve
ji "Yes, it is out of the ordinary, but I wanted you and Dad to meet [name]."
ji "Speaking of Dad, where is he?"
scene ep10_jill_fam15 with dissolve
jim "Geoff!? Are you joining us?"
scene ep10_jill_fam16 with dissolve
ge "Hold your horses, Amelia. I'm coming."
scene ep10_jill_fam17 with dissolve
ge "There she is! My little Jillybean!"
scene ep10_jill_fam18 with dissolve
ge "Welcome home!"
scene ep10_jill_fam19 with dissolve
ge "And who is this lad?"
scene ep10_jill_fam20 with dissolve
ji "Dad, I told you I'd be bringing company. This is [name]."
scene ep10_jill_fam19 with dissolve
ge "Right, right, right!"
scene ep10_jill_fam21 with dissolve
ge "[name]! Bring it in here."
ge "Welcome! We're happy to have you."
mc "(Whoa! Is that alcohol I smell...?)"
if ep5_questions_event:
    scene ep10_jill_fam22 with dissolve
    ge "Say, you look familiar. Have we met before?"
    scene ep10_jill_fam23 with dissolve
    mc "(Oh, shit! It took me a while, but I recognize him.)"
    play sound "sound_effects/whoosh_2.mp3"
    scene ep10_jill_fam135
    mc "(At the prep party we crashed... Was that Jill's dad!?)"
    scene ep10_jill_fam23 with dissolve
    mc "(Hopefully, he doesn't remember that. It would be embarrassing having to explain it.)"
    mc "N-no... I don't think so."
    if not ep8_recital_failed:
        scene ep10_jill_fam24 with dissolve
        jim "You're right, Geoff. I recognize him, too..."
elif not ep8_recital_failed:
    scene ep10_jill_fam24 with dissolve
    jim "Hm... I recognize you from somewhere..."
    jim "But I can't put my finger on it."
if not ep8_recital_failed:
    scene ep10_jill_fam25 with dissolve
    jim "Jill's recital. You're the one who assisted Jill, aren't you?"
    scene ep10_jill_fam22 with dissolve
    if ep5_questions_event:
        ge "Oh! Is that it?"
    else:
        ge "Oh! Is that right?"
    scene ep10_jill_fam26 with dissolve
    ji "Yes. This is him."
    scene ep10_jill_fam25 with dissolve
    jim "Well, that's lovely."
else:
    scene ep10_jill_fam25 with dissolve
    jim "It's lovely having you over."
jim "Please make yourselves comfortable. Let me get your jacket and coat."
$ guideSuggestedPage = 128
scene ep10_jill_fam27 with dissolve
mc "(There's something off about Amelia.)"
mc "(It's as if her expressions don't match her words. I can't figure out if she is excited or bored by this.)"
mc "(And Geoff... I can't be mistaken, he's drunk.)"
scene ep10_jill_fam28 with dissolve
ji "Um... Are you ok?"
scene ep10_jill_fam29 with dissolve
mc "What's up with your dad?"
scene ep10_jill_fam30 with dissolve
ji "You noticed it too..."
scene ep10_jill_fam29 with dissolve
mc "I could smell it on his breath. He's been drinking."
scene ep10_jill_fam30 with dissolve
ji "I'm so ashamed."
ji "He isn't always like this. I didn't think he'd be drinking today."
scene ep10_jill_fam31 with dissolve
jim "Your sister's birthday isn't far off. Did you forget?"
scene ep10_jill_fam32 with dissolve
ji "Of course, I haven't."
scene ep10_jill_fam33 with dissolve
jim "[name], please excuse us for a moment."
scene ep10_jill_fam34 with dissolve
mc "(Oof... Uncomfortable...)"
scene ep10_jill_fam35 with dissolve
ge "[name]! Sit down. I got you something to drink."
scene ep10_jill_fam36 with dissolve
mc "I'm fine, thanks."
scene ep10_jill_fam37 with dissolve
ge "Are you sure?"
scene ep10_jill_fam36 with dissolve

if persistent.mod_wt_enabled: 
                    $mod_choices = ["(+Jill)","(-Jill)","(-DIK)","(+DIK)","(Sage or Sarah scene)","(Sarah scene)","","","","","","" ]
                    #[m_c1][mod_choices[0]]

menu:
    "Yeah":
        mc "Yeah, thanks."
    "I'm not 21 [m_c1][mod_choices[2]]":
        $ dk(-1)
        mc "I'm not 21."
        scene ep10_jill_fam37 with dissolve
        ge "Oh, sorry! I thought you were."
scene ep10_jill_fam38 with dissolve
ge "*{i}Deep breath{/i}*"
ge "Excuse me; I didn't catch your full name."
scene ep10_jill_fam39 with dissolve
mc "Oh, it's [name] [lname]."
scene ep10_jill_fam40 with dissolve
ge "Ah. Tell me, [lname]. Are you into horses?"
scene ep10_jill_fam39 with dissolve
mc "Sorry, I'm not."
scene ep10_jill_fam40 with dissolve
ge "You don't have to be sorry about that. That's actually good!"
ge "I could use the company around here of someone who doesn't like them, haha!"
scene ep10_jill_fam41 with dissolve
ge "See, Amelia loves horses. She spends a lot of her day with them."
ge "I never understood their charm. They smell and crave so much care and attention."
scene ep10_jill_fam39 with dissolve
mc "Did you ever ride one?"
scene ep10_jill_fam40 with dissolve
ge "Yes, of course. I've ridden plenty, but I don't enjoy it."
ge "It's mostly been for the girls."
scene ep10_jill_fam39 with dissolve
mc "The girls?"
scene ep10_jill_fam41 with dissolve
ge "Amelia, Jill and Lana."
scene ep10_jill_fam39 with dissolve
mc "Ah! Those girls."
scene ep10_jill_fam42 with dissolve
ge "..."
scene ep10_jill_fam39 with dissolve
mc "If not horses, what are you into?"
scene ep10_jill_fam40 with dissolve
ge "Oh, you stole my question right in front of me. Haha!"
scene ep10_jill_fam41 with dissolve
ge "I'm into vehicles. Predominantly cars, motorbikes and boats. I'm a bit of a collector."
ge "Do you own an automobile?"
scene ep10_jill_fam39 with dissolve
mc "No, I have a bike - a bicycle, that is - back home at Dad's place, but that's my only vehicle."
scene ep10_jill_fam40 with dissolve
ge "You haven't had your first car yet? Oh, you're going to be in for a treat."
ge "Much like your first love, you never forget your first car."
scene ep10_jill_fam43 with dissolve
ge "The Maverick... Ah... The things we did together. Freedom, capital F."
scene ep10_jill_fam41 with dissolve
ge "Where are my manners? You haven't seen the place yet, have you?"
ge "Let me give you the grand tour."
scene ep10_jill_fam39 with dissolve
mc "Oh... Sure!"
scene ep10_jill_fam44 with dissolve
mc "(Maybe I should have waited for Jill, but this seems harmless enough.)"
scene ep10_jill_fam45 with dissolve
ge "This is Jill's bedroom. She doesn't stay here often these days, but it's still hers whenever she comes home to visit."
scene ep10_jill_fam46 with dissolve
mc "That sounds like my dad. He insists on keeping my room as it was before I left for college."
mc "It's only been a few months since I moved out, but I don't think he'll ever change it."
scene ep10_jill_fam47 with dissolve
ge "That's parents for you. He sounds like a good man."
scene ep10_jill_fam46 with dissolve
mc "Yeah, he's my role model."
scene ep10_jill_fam48 with dissolve
ge "Down the hall is the master bedroom, but I'll spare you that room."
ge "I wouldn't want you to be too uncomfortable, hehe."
ge "Let's continue upstairs."
scene ep10_jill_fam49 with dissolve
mc "What's that room?"
ge "*{i}Grunts{/i}*"
scene ep10_jill_fam50 with dissolve
mc "(Huh? Oh! Maybe that was Lana's room... Fuck... Me and my stupid mouth.)"
scene ep10_jill_fam51 with dissolve
ge "And up here is my favorite place. Nothing beats this view."
scene ep10_jill_fam52 with dissolve
mc "Wow! What a view!"
scene ep10_jill_fam53 with dissolve
ge "You can see the stables from here. Down there."
scene ep10_jill_fam54 with dissolve
ge "And on the other side is where the sun sets."
scene ep10_jill_fam55 with dissolve
mc "It's amazing. Thanks for showing me."
scene ep10_jill_fam56 with dissolve
$ renpy.pause()
scene ep10_jill_fam58 with dissolve
ge "I never followed up on that question from earlier, did I?"
ge "What are you into, [lname]?"
scene ep10_jill_fam59 with dissolve
mc "I like martial arts. I've been practicing kickboxing since I was young."
scene ep10_jill_fam58 with dissolve
ge "Kickboxing? That sounds violent."
scene ep10_jill_fam59 with dissolve
mc "It's mostly for self-defense. When I was a kid, I was bullied at school."
mc "My dad taught me kickboxing to be able to defend myself."
scene ep10_jill_fam60 with dissolve
ge "Bullies. *{i}Sigh{/i}* They are horrible."
ge "I bet Jillybean can relate an awful lot to your history."
scene ep10_jill_fam59 with dissolve
mc "Yeah, I think she can. We do have a lot in common."
scene ep10_jill_fam58 with dissolve
ge "You do? Enlighten me."
scene ep10_jill_fam57 with dissolve
mc "We're both into music. I've played the guitar since I was young."
scene ep10_jill_fam58 with dissolve
ge "That makes sense. I can see why music is mutual ground for you two."
scene ep10_jill_fam61 with dissolve
ji "There you are! We've been looking all over for you."
scene ep10_jill_fam63 with dissolve
ge "I was giving [lname] the grand tour and getting to know him."
scene ep10_jill_fam62 with dissolve
ji "Ok. Um, Dad. Mom needs you downstairs."
scene ep10_jill_fam63 with dissolve
ge "As always. I'll be right back."
scene ep10_jill_fam64 with dissolve
ji "I'm sorry about that."
scene ep10_jill_fam65 with dissolve
mc "There's nothing to be sorry about."
mc "Yeah, he's a bit drunk, but he's not being rude to me. It's the opposite; he's being very friendly."
scene ep10_jill_fam69 with dissolve
ji "That's how he gets when he drinks - overly friendly."
ji "It's not the real him."
ji "I talked to Mom about it just now. He's been depressed lately. More so than usual..."
scene ep10_jill_fam68 with dissolve
ji "I wish he didn't have to resort to alcohol...but it doesn't matter what we say or do."
ji "We've had interventions in the past, but..."
ji "This is what I meant when I said he's changed."
scene ep10_jill_fam67 with dissolve
ji "He's carrying this deep sorrow for what happened with Lana, and instead of facing it...he never did."
ji "And Mom...she... *{i}Sniff{/i}*"
ji "Mom's trying her best, but she's almost given up on him."
scene ep10_jill_fam66 with dissolve
mc "Are you ok?"
scene ep10_jill_fam67 with dissolve
ji "This is not how I wanted today to go. I wanted to present you to my parents and have a happy day with you."
ji "Instead, they pretty much force me to tell you all of this. Because you deserve an explanation and I don't want you to regret coming here with me."
scene ep10_jill_fam66 with dissolve
mc "Jill..."
mc "Whose family is perfect? Trust me, no one's perfect."
mc "Don't worry about this. It doesn't ruin this day. It's still a big day for both of us."
scene ep10_jill_fam65 with dissolve
mc "It's the next step in our relationship and I'm happy to take it."
mc "I got to see how you lived, and your dad showed me your room."
scene ep10_jill_fam70 with dissolve
ji "Haha, he did?"
scene ep10_jill_fam65 with dissolve
mc "Yeah, he did. By the way, the room upstairs from it...was that your sister's?"
scene ep10_jill_fam70 with dissolve
ji "Yes. Did he show you it?"
scene ep10_jill_fam65 with dissolve
mc "No, we walked past it."
scene ep10_jill_fam71 with dissolve
ji "Do you want to see it?"
scene ep10_jill_fam65 with dissolve
stop music fadeout 5
mc "Would that be ok? Considering..."
scene ep10_jill_fam70 with dissolve
ji "I want you to see it."
scene ep10_jill_fam72 with dissolve
play music "music/ep8/licensed_music/track66.mp3"
$ renpy.pause()
scene ep10_jill_fam73 with dissolve
$ renpy.pause()
scene ep10_jill_fam74 with dissolve
ji "This is my sister. Her spirit still lives here."
scene ep10_jill_fam75 with dissolve
mc "Wow..."
mc "This room is totally different from all the other rooms."
scene ep10_jill_fam76 with dissolve
ji "Yes. It's a sanctuary for Lana now."
ji "When they clean her room, they even put the books and records back as they were to keep it the same as it used to be."
scene ep10_jill_fam77 with dissolve
ji "How do you feel standing in here?"
scene ep10_jill_fam78 with dissolve
mc "How do I explain it? It makes me feel weird and sad."
mc "It feels like I'm in someone's room that I know."
scene ep10_jill_fam79 with dissolve
mc "Look! I have this album! It's from my favorite band. I wear their T-shirts all the time."
scene ep10_jill_fam81 with dissolve
ji "You have things in common..."
scene ep10_jill_fam80 with dissolve
mc "I see the posters, her belongings, and style... It feels like I know her, in a sense."
mc "What I mean is that it's hard to imagine that she's not with us anymore."
scene ep10_jill_fam81 with dissolve
ji "Right?"
ji "That's exactly how I feel, too."
ji "One look at her things and I get transported back in time."
scene ep10_jill_fam82 with dissolve
ji "I can see her sitting on that bean bag chair, listening to music."
scene ep10_jill_fam83 with dissolve
ji "I used to jump in her bed because Mom didn't let me do it in mine."
ji "But Lana never minded it."
scene ep10_jill_fam84 with dissolve
mc "Whoa!"
ji "What is it?"
mc "Is that a custom Strutter!? Did she play?"
scene ep10_jill_fam86 with dissolve
ji "Mom and Dad encouraged her to play an instrument and she chose that guitar."
ji "But I think she played it twice before she quit and never touched it again."
scene ep10_jill_fam85 with dissolve
ji "The strings snapped quite some time ago and no one has touched it since then."
mc "That's such a shame. It looks so cool and those guitars aren't cheap. I could never afford one like that."
scene ep10_jill_fam87 with dissolve
mc "Is this her?"
ji "Yes."
mc "You look so much alike."
scene ep10_jill_fam89 with dissolve
ji "Really!? Do you mean that?"
scene ep10_jill_fam87 with dissolve
mc "Yeah, if you were the same age, you could be twins."
mc "If you put on her clothes, I could barely tell the difference."
ji "I could never wear clothes like hers."
scene ep10_jill_fam88 with dissolve
mc "Did you ever try?"
scene ep10_jill_fam90 with dissolve
ji "No. Haha, I mean... It's not me."
ji "When I was young, Mom and Dad bought me clothes, and that's the style I've kept as I grew older."
ji "It would feel weird to wear something like that, I think."
scene ep10_jill_fam91 with dissolve
ji "But one of her belongings I kept for myself was her hat. It has a cute pin of a cat on it."
ji "She used to wear it a lot, and in my last memory of her, she wore it..."
ji "Sometimes, when I think about her, I put it on and feel much stronger. It's my little secret."
scene ep10_jill_fam92 with dissolve
mc "And now it's mine too."
scene ep10_jill_fam93 with dissolve
jim "*{i}Cough{/i}* Lunch is served."
scene ep10_jill_fam95 with dissolve
ji "Oh! I was showing [name] Lana's room and telling him more about her."
scene ep10_jill_fam94 with dissolve
$ renpy.pause()
scene ep10_jill_fam96 with dissolve
ji "Sorry, [name]."
stop music fadeout 3
mc "You don't have to keep saying that. Let's have lunch."
scene ep10_jill_fam97 with dissolve
$ renpy.pause()
play music "music/ep6/licensed_music/track35.mp3"
scene ep10_jill_fam98 with dissolve
jim "[name]. Tell me about yourself. Are you in college, too?"
scene ep10_jill_fam99 with dissolve
mc "Yes. Yes, I am. I'm a freshman studying engineering."
scene ep10_jill_fam100 with dissolve
ge "Engineering? In what field?"
scene ep10_jill_fam101 with dissolve
mc "The scientific kind."
scene ep10_jill_fam100 with dissolve
ge "The world needs scientists!"
scene ep10_jill_fam101 with dissolve
mc "It's always been fascinating to me."
scene ep10_jill_fam98 with dissolve
jim "Jill told me you're from here or nearby, at least. Who are your family?"
scene ep10_jill_fam99 with dissolve
mc "It's just me and my dad. We're a small family."
scene ep10_jill_fam98 with dissolve
jim "What's your dad's name?"
scene ep10_jill_fam99 with dissolve
mc "It's Neil [lname]. He works as a carpenter."
scene ep10_jill_fam100 with dissolve
ge "Oh! Where at? Maybe we've hired them."
scene ep10_jill_fam101 with dissolve
mc "Kovak's Carpentry."
scene ep10_jill_fam100 with dissolve
ge "Oh, they are reputable! I've heard of them, but I've never had the pleasure of working with them."
ge "A practical dad with an academic son. He must feel proud!"
scene ep10_jill_fam101 with dissolve
mc "Yeah, he's very proud that I got accepted to college."
scene ep10_jill_fam98 with dissolve
jim "And your mother?"
scene ep10_jill_fam107 with dissolve
ji "Mom..."
scene ep10_jill_fam99 with dissolve
mc "It's fine. She died at childbirth."
scene ep10_jill_fam98 with dissolve
jim "I'm sorry to hear that."
scene ep10_jill_fam98 with dissolve
jim "So... Any siblings?"
scene ep10_jill_fam99 with dissolve
mc "No, I'm an only child. Dad didn't find someone else after Mom, so..."
scene ep10_jill_fam107 with dissolve
ji "Perhaps we could talk about something else?"

scene ep10_jill_fam99 with dissolve
mc "I love your home. How long have you lived here?"
scene ep10_jill_fam98 with dissolve
jim "Oh, my. How long has it been? I want to say...19 years?"
scene ep10_jill_fam106 with dissolve
jim "Geoff? Help me out here."
scene ep10_jill_fam103 with dissolve
ge "Yes, yes. 19. That sounds about right."
scene ep10_jill_fam100 with dissolve
ge "I got the tip from my friend - eh, back then, business associate - Maynard."
scene ep10_jill_fam115 with dissolve
ji "Maynard is Bianca's dad."
scene ep10_jill_fam100 with dissolve
ge "He heard the place was for sale and it was pretty much a steal."
ge "Finding a buyer for extravagant properties like this usually takes time, and the previous owner had to make a quick sale for financial reasons."
ge "And that's how we ended up here."
scene ep10_jill_fam101 with dissolve
mc "I don't mean to be rude or ignorant, but would you tell me what the Royces do?"
mc "Is it academy only or...?"
scene ep10_jill_fam100 with dissolve
ge "Ah. I know what you are thinking. Burgmeister and Royce, haha."
ge "I come from the line of Royces, but we don't have much to do with your college these days."
ge "We do a small part as board members but mostly branch out with other work."
scene ep10_jill_fam98 with dissolve
jim "Geoff and I have found personal success in our real estate company."
jim "That's what we spend our weekdays on mostly."
scene ep10_jill_fam102 with dissolve
ge "It used to be hard, but it's easy living these days."
ge "With the right kind of people below you, work does itself."
scene ep10_jill_fam100 with dissolve
ge "And one day, Jillybean will be next in line for the CEO spot."
scene ep10_jill_fam114 with dissolve
mc "Oh? Really?"
scene ep10_jill_fam115 with dissolve
ji "After I get my education, I will get a position at our family's company to start with."
ji "We'll see how far it takes me."
scene ep10_jill_fam113 with dissolve
ge "Haha, you don't have to be modest, Jillybean."
ge "Someone will have to run the company when we're too old for it."
scene ep10_jill_fam112 with dissolve
ji "Yes, but I'd like that to be because of my skills and merits, not nepotism."
scene ep10_jill_fam98 with dissolve
jim "How about you, [name]? What do you see yourself doing in 10 years from now?"
scene ep10_jill_fam107 with dissolve
ji "This sounds awfully much like one of your business interviews."
scene ep10_jill_fam111 with dissolve
jim "I'm just making conversation."
scene ep10_jill_fam99 with dissolve
mc "When I think about work...nothing pops up in my head. I figured getting a broad education would give me time to figure it out."
scene ep10_jill_fam100 with dissolve
ge "Any business classes on that curriculum of yours, [lname]?"
scene ep10_jill_fam101 with dissolve
mc "Maybe. Jill has been recommending me to take one."
scene ep10_jill_fam108 with dissolve
ji "Mom. Dad. There is a reason I wanted to bring [name] with me back home today."
ji "Now that you've gotten to know him a bit better, I wanted to let you know that...um..."
scene ep10_jill_fam109 with dissolve
ji "[name] is not just my friend. He is my boyfriend. And I wanted you to hear it from us like this."
scene ep10_jill_fam110 with dissolve
jim "Oh?"
scene ep10_jill_fam104 with dissolve
ge "Your boyfriend?"
scene ep10_jill_fam110 with dissolve
jim "This was certainly news you sprung upon us."
scene ep10_jill_fam99 with dissolve
mc "I'm very interested in your daughter. Uh... She means a lot to me; we've grown quite close quickly."
scene ep10_jill_fam98 with dissolve
jim "I suppose I should welcome you into our family."
scene ep10_jill_fam112 with dissolve
ji "Dad?"
scene ep10_jill_fam105 with dissolve
ge "Yes. Yes. [lname]! Welcome!"
ge "Please take good care of Jillybean."
scene ep10_jill_fam108 with dissolve
ji "[name] is taking the best care of me, Dad. He's been fantastic to me and that's why we're sitting here today."
ji "I know this might feel like sudden news to you, but believe me when I say this isn't sudden to me."
scene ep10_jill_fam109 with dissolve
ji "I've grown attached to [name] since the day we met."
scene ep10_jill_fam104 with dissolve
ge "Well, that settles that, then."
ge "Excuse me, I have to use the restroom."
scene ep10_jill_fam116 with dissolve
jim "Coffee?"
stop music fadeout 3
scene ep10_jill_fam117 with dissolve
ji "..."
play music "music/ep8/licensed_music/track72.mp3"
scene ep10_jill_fam118 with fade
$ renpy.pause()
scene ep10_jill_fam119 with dissolve
$ renpy.pause()
scene ep10_jill_fam120 with dissolve
ji "*{i}Sigh{/i}*"
scene ep10_jill_fam121 with dissolve
mc "It wasn't a complete disaster."
scene ep10_jill_fam122 with dissolve
ji "I'm so sorry."
scene ep10_jill_fam121 with dissolve
mc "Stop saying that. It's not your fault."
scene ep10_jill_fam122 with dissolve
ji "They will be happy for us. We have to give them time to understand it."
scene ep10_jill_fam123 with dissolve
mc "Your mother seemed to take it well. She didn't seem thrilled, but she didn't seem bothered by it either."
scene ep10_jill_fam124 with dissolve
ji "Can we please keep this day to ourselves?"
scene ep10_jill_fam123 with dissolve
mc "No one else needs to know anything about it."
scene ep10_jill_fam124 with dissolve
ji "Thank you. You're amazing."
scene ep10_jill_fam125 with dissolve
mc "You are."
mc "I don't mean to insult your parents with this, but I can't believe you turned out the way you did."
scene ep10_jill_fam126 with dissolve
ji "..."
mc "*{i}Smack{/i}*"
scene ep10_jill_fam127 with dissolve
ji "They are good people, [name]. They are."
ji "Maybe next time, they will feel more comfortable around us."
scene ep10_jill_fam128 with dissolve
mc "Totally. It's hard to judge someone from a single lunch."
scene ep10_jill_fam127 with dissolve
ji "When can I meet your dad?"
scene ep10_jill_fam128 with dissolve
mc "We'll make plans for it."
scene ep10_jill_fam129 with dissolve
$ renpy.pause()
scene ep10_jill_fam127 with dissolve
ji "So... Now that we've talked to my parents about us..."
ji "Do you want to let others know? Or would you rather wait until we tell your dad?"
scene ep10_jill_fam128 with dissolve
mc "Dad isn't on social media, but I'll tell him the next time I see him."
mc "I don't see why that should stop us from being official if you want it."
scene ep10_jill_fam127 with dissolve
ji "How should we do it? Do we change our relationship status to \"in a relationship\" or...?"
scene ep10_jill_fam130 with dissolve
mc "Yeah. And we can post a picture of us too."
scene ep10_jill_fam131 with dissolve
ji "Haha... I'm getting nervous."
scene ep10_jill_fam130 with dissolve
mc "It's a big step."
scene ep10_jill_fam131 with dissolve
ji "It is."
ji "Let's take it."
scene ep10_jill_fam132 with dissolve
$ renpy.pause(0.5)
scene white
play sound "sound_effects/camera_shutter.mp3"
$ renpy.pause(0.5)
scene ep10_jill_fam132 with dissolve
$ renpy.pause()
scene ep10_jill_fam133 with dissolve
ji "*{i}Smack{/i}*"

scene ep10_jill_fam131 with dissolve
ji "So... Do you want to do something else today?"
scene ep10_jill_fam130 with dissolve
mc "I can spend the rest of the day with you, if you'd like. What do you have in mind?"
scene ep10_jill_fam131 with dissolve
ji "I was thinking we could take a relaxing bath together before dinner."
stop music fadeout 3
scene ep10_jill_fam130 with dissolve
mc "A bath sounds great..."
$ mgallery_add_photo("ep10_jill_solo_pic1")
$ mgallery_add_photo("ep10_jill_solo_pic2")
$ new_bio("Jill", "I met Jill's parents for lunch at their place. Jill was upset that it didn't match her expectations for different reasons.")
$ new_bio("Jill", "Jill and I announced our relationship on social media.")


label ep10_jill_lewd_label:
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
hide screen new_phone_screen
play music "music/ep4/relax.mp3"
scene ep10_jill_solo53 with dissolve
ji "Is it hot enough for you?"
scene ep10_jill_solo54 with dissolve
mc "Yeah, it is. We only have a small bathtub at our place. This one is so much better."
scene ep10_jill_solo55 with dissolve
ji "It's big for one person, but I do like it."
scene ep10_jill_solo56 with dissolve
mc "Oh, yeah. This is the stuff."
scene ep10_jill_solo57 with dissolve
ji "You're always so comfortable with yourself."
scene ep10_jill_solo58 with dissolve
mc "With myself? Do you mean with my body?"
scene ep10_jill_solo59 with dissolve
ji "Yes. You didn't even feel weird removing your clothes in front of me. You just ripped them right off."
ji "And here I am, pondering if it's too bright in here and whether I should dim the lights or not."
scene ep10_jill_solo58 with dissolve
mc "You think too much."
scene ep10_jill_solo60 with dissolve
ji "Aha, what does that say about you?"
scene ep10_jill_solo61 with dissolve
mc "Well, yeah. When I'm relaxed, I hardly think at all."
scene ep10_jill_solo62 with dissolve
mc "Get in here with me. I've seen your beautiful body naked before, you know?"
scene ep10_jill_solo63 with dissolve
ji "Oh, God. Stop it."
scene ep10_jill_solo64 with dissolve
mc "You're so cute when you're blushing."
scene bg anim_jill_strip_ep10 movie with dissolve
$ renpy.pause()
mc "Damn... I feel like I'm the luckiest guy alive."
scene ep10_jill_solo65 with dissolve
if name == "Lucky":
    ji "It's easy to feel lucky with a name like yours."
else:
    ji "Maybe you should name yourself lucky?"
scene ep10_jill_solo66 with dissolve
$ renpy.pause()
scene ep10_jill_solo67 with dissolve
$ renpy.pause()
scene ep10_jill_solo68 with dissolve
ji "*{i}Deep breath{/i}*"
scene ep10_jill_solo69 with dissolve
ji "This is relaxing..."
scene ep10_jill_solo70 with dissolve
mc "Yeah, totally."
scene ep10_jill_solo71 with dissolve
ji "Although, parts of you still seem...tense."
scene ep10_jill_solo72 with dissolve
mc "Shit... Sorry."
ji "I have barely touched you."
scene ep10_jill_solo73 with dissolve
mc "I'm telling you. Luckiest guy alive sitting right over here."
scene ep10_jill_solo74 with dissolve
ji "Well, Mr. Lucky. Maybe that problem of yours will go away if you try to relax a bit harder."
scene ep10_jill_solo75 with dissolve
$ renpy.pause()
scene ep10_jill_solo76 with dissolve
mc "Are you aware that you're teasing me now? If so, bravo."
scene ep10_jill_solo77 with dissolve
ji "Am I?"
scene ep10_jill_solo78 with dissolve
mc "Well, you were."
scene ep10_jill_solo77 with dissolve
ji "Is that why it's still hard?"
scene ep10_jill_solo80 with dissolve
mc "Yeah."
scene ep10_jill_solo79 with dissolve
ji "What's got you aroused?"
scene ep10_jill_solo80 with dissolve
mc "You, of course."
scene ep10_jill_solo79 with dissolve
ji "I get that, but what about me? Like I told you, I didn't do anything."
scene ep10_jill_solo80 with dissolve
mc "I don't want to make you uncomfortable by talking about it."
scene ep10_jill_solo81 with dissolve
ji "I did promise you to try to get comfortable with it. Remember?"
scene ep10_jill_solo80 with dissolve
mc "Ok... What got me excited when you got in was..."
menu:
    "Your wet and soapy breasts":
        mc "The thought of your wet and soapy breasts."
        scene ep10_jill_solo82 with dissolve
        ji "Oh my."
        scene ep10_jill_solo83 with dissolve
        mc "Seeing them glisten like that from the water and suds awakens something in me."
        play sound "sound_effects/season3/pool_wash.mp3"
        scene anim_jill_wash_ep10 with dissolve
        ji "Haha... So... Washing them like this does something for you?"
        pause
    "Your soapy ass":
        mc "The thought of your soapy ass."
        scene ep10_jill_solo82 with dissolve
        ji "Oh my."
        scene ep10_jill_solo83 with dissolve
        mc "I hope that doesn't sound too vulgar, but I can't help it."
        mc "I take one look at it and...it awakens something in me."
        play sound "sound_effects/season3/pool_wash.mp3"
        scene anim_jill_wash3_ep10 with dissolve
        ji "Haha... So... Washing it like this does something for you?"
        pause
    "Your soapy body":
        mc "The thought of your soapy body."
        scene ep10_jill_solo82 with dissolve
        ji "Oh my."
        scene ep10_jill_solo83 with dissolve
        mc "It's perfect, and I don't know where to rest my eyes."
        mc "They keep wandering all over and...it awakens something in me."
        play sound "sound_effects/season3/pool_wash.mp3"
        scene anim_jill_wash2_ep10 with dissolve
        ji "Haha... So... Washing it like this does something for you?"
        pause

mc "Are you kidding me?"
scene ep10_jill_solo84 with dissolve
mc "It awakens that guy. He's pretty hard to hide."
scene ep10_jill_solo85 with dissolve
ji "Thanks for letting me know."
scene ep10_jill_solo86 with dissolve
mc "Haha, that's it?"
scene ep10_jill_solo85 with dissolve
ji "I don't know what else to say."
scene ep10_jill_solo86 with dissolve
mc "What about you? Did you feel something special when you watched me get in?"
scene ep10_jill_solo87 with dissolve
ji "No, not really."
scene ep10_jill_solo88 with dissolve
mc "Ouch."
scene ep10_jill_solo89 with dissolve
ji "Oh! Sorry! I didn't mean I felt nothing."
scene ep10_jill_solo90 with dissolve
mc "Hey, if you don't feel something, you don't feel something."
scene ep10_jill_solo89 with dissolve
ji "Stop it. That's not what I meant."
ji "I meant... It's different for me."
scene ep10_jill_solo91 with dissolve
ji "You tell me that you get aroused from seeing my body, but for me, it's not seeing your body that does things."
ji "Even if I appreciate your body, it's more how you act around me, treat and talk to me..."
ji "I guess you can say that you're good at that and that it...turns me on?"
scene ep10_jill_solo93 with dissolve
mc "Was that a question or a statement?"
scene ep10_jill_solo92 with dissolve
ji "It turns me on. Ok?"
scene ep10_jill_solo91 with dissolve
ji "And I think you're good with your hands."
ji "I think you're good at everything when it comes to making love."
ji "And you have soft lips."
scene ep10_jill_solo93 with dissolve
mc "I'm impressed. You did it. And thank you for those compliments."
scene ep10_jill_solo95 with dissolve
ji "It feels so weird for me to talk to you about these things. I don't even say them out loud to myself."
scene ep10_jill_solo94 with dissolve
mc "No, no. You were very good at it!"
mc "It means a lot that you put yourself out there and tried your best just now."
scene ep10_jill_solo95 with dissolve
ji "See. This is what I'm talking about. This turns me on."
scene ep10_jill_solo96 with dissolve
ji "But then I feel Mr. Lucky Junior down there pressing against my thigh and cheek and I feel weird again."
mc "He doesn't want to go away."
ji "Haha! He so does not."
scene ep10_jill_solo97 with dissolve
mc "I'd rather that you grab it than poke it."
ji "I wasn't sure if I could reach out and grab it like that. It felt like I should start slow or ask first."
scene ep10_jill_solo98 with dissolve
mc "Yeah, but poking it feels weird. Starting slow can be grasping it gently and kissing my neck."
scene ep10_jill_solo99 with dissolve
ji "That doesn't feel slow to me."
scene ep10_jill_solo98 with dissolve
mc "Trust me. Do that and see how it feels."
scene anim_jill_hj_ep10 with dissolve
ji "*{i}Smack{/i}*"
mc "Yeah... You got it."
ji "My stomach is fluttering from this."
mc "Mine too..."
ji "Does it feel good below the water?"
mc "It's not as good as above water, but it's a nice start."
pause
scene ep10_jill_solo100 with dissolve
mc "Do you like holding it?"
ji "Yes. It's very large. It's interesting."

scene ep10_jill_solo101 with dissolve
mc "Go ahead..."
scene anim_jill_hj2_ep10 with dissolve
mc "How does this make you feel?"
ji "I feel...aroused."
mc "That's good. Me too."
ji "Well, obviously."
pause
scene anim_jill_hj3_ep10 with dissolve
mc "Is there anything special you'd like to do to me?"
ji "Special how?"
mc "Do you have any fantasies or stuff you'd like to try?"
ji "I don't know. Do you?"
mc "I can think of many things I want to do with you."
mc "If I tell you, I hope you take it the right way."
ji "I'll try. Tell me about them."
scene anim_jill_hj2_ep10 with dissolve
menu:
    "Blowjob":
        $ tmpInt = 0
        mc "I want you to feel comfortable enough to give me a blowjob. To feel your mouth suck on my dick..."
    "Assjob":
        $ tmpInt = 1
        mc "It would feel amazing to get an assjob from you. Like, if you put your asscheeks against my dick and started grinding."
    "Boobjob":
        $ tmpInt = 2
        mc "I would love to see you work your breasts all over my dick, massaging it with them."
mc "I think that would be hot."
ji "I can't believe how easily you bring that up."
mc "Believe me, it took practice to get comfortable doing it."
scene ep10_jill_solo102 with dissolve
ji "Oh..."
scene ep10_jill_solo103 with dissolve
ji "I think I could try doing that for you if you promise you won't laugh."
scene ep10_jill_solo104 with dissolve
mc "Jill, I would never laugh at you for doing that. No way. I'd appreciate the hell out of your effort."

if tmpInt == 0:
    jump ep10_jill_blowjob_label
elif tmpInt == 1:
    jump ep10_jill_assjob_label
else:
    jump ep10_jill_boobjob_label


label ep10_jill_blowjob_label:
scene ep10_jill_solo105 with dissolve
ji "Maybe it's a stupid question, but does it feel better if I lick it or put it in my mouth?"
scene ep10_jill_solo106 with dissolve
mc "Both feel great, but the mouth feels the best."
mc "But the tongue is great for teasing me with."
scene ep10_jill_solo105 with dissolve
ji "I'm confused. Which is it?"
scene ep10_jill_solo106 with dissolve
mc "Start licking it for a bit, and put it in your mouth when you're ready."
scene anim_jill_bj_ep10 with dissolve
ji "*{i}Lick lick{/i}*"
pause
mc "Do you wanna put your mouth around it?"
ji "I'll try."
mc "Watch your teeth and you'll do fine."
scene anim_jill_bj2_ep10 with dissolve
ji "*{i}Suck suck{/i}*"
mc "Oh, fuck... That feels amazing."
ji "*{i}Suck suck{/i}* Should it be deeper inside my mouth?"
mc "Only if you can handle it. Work it with your hand, too, when you suck on it."
pause
scene anim_jill_bj3_ep10 with dissolve
ji "*{i}Suck suck{/i}* Like this?"
mc "Yeah... You have no idea how good that feels."
mc "Wow, you're going deeper, too..."
pause
scene anim_jill_bj4_ep10 with dissolve
mc "Don't take this the wrong way, but you're doing way better than I expected."
mc "There's only so much I can ask for, but can you go faster and hold your hand still at the root of my dick?"
pause
scene anim_jill_bj5_ep10 with dissolve
mc "Yeah, like that. Push the skin all back with your hand."
ji "*{i}Suck suck{/i}*"
pause
scene anim_jill_bj6_ep10 with dissolve
mc "Fuck... I could explode in your mouth from this."
ji "!!!"
mc "Don't worry. I won't! I'm just letting you know how great it feels."
pause
scene anim_jill_bj7_ep10 with dissolve
ji "*{i}Suck suck{/i}*"
pause

menu:
    "Assjob":
        mc "Can you give me an assjob? Like, if you put your asscheeks against my dick and start grinding."
        scene ep10_jill_solo107 with dissolve
        ji "Let me know if I'm doing it wrong."
        jump ep10_jill_assjob_label
    "Boobjob":
        mc "Would you be comfortable massaging my dick with your breasts?"
        scene ep10_jill_solo109 with dissolve
        ji "I can try... I can tell that you like them a lot."
        jump ep10_jill_boobjob_label
    "Continue":
        jump ep10_jill_cont_label

label ep10_jill_assjob_label:
scene anim_jill_assjob_ep10 with dissolve
mc "Yeah, push your ass against me like that and grind up, down and all around."
ji "And this feels good to you?"
mc "Very. The soap makes it better. Your ass is all wet and slippery."
mc "It makes it feel even softer when you push it against me like that."
pause
scene anim_jill_assjob2_ep10 with dissolve
mc "Does it feel weird doing it?"
ji "[mc_jill], I've never done anything like this before. It does feel weird..."
ji "...but knowing that you enjoy it makes it feel good, too. I can't explain it."
ji "I guess I would say I don't mind doing it because it makes you happy."
mc "It does way more than make me happy. It makes me horny as hell."
pause
menu:
    "Do it faster":
        mc "Go a bit faster if you can."
        scene anim_jill_assjobb_ep10 with dissolve
        ji "Like that?"
        mc "Yes... Fuck, that's good."
        pause
    "You're doing great":
        mc "You're doing great."
scene anim_jill_assjob3_ep10 with dissolve
mc "You have such an amazing ass."
ji "[mc_jill]..."
mc "You do."
ji "You're going to make me blush again saying those things."
mc "Haha! I will still say it. Your ass is amazing, [jill]."
pause
scene ep10_jill_solo108 with dissolve
mc "Doing it like this would feel great, too."
scene anim_jill_assjob4_ep10 with dissolve
pause
scene anim_jill_assjob5_ep10 with dissolve
pause
scene anim_jill_assjob6_ep10 with dissolve
pause

menu:
    "Blowjob":
        mc "Can you give me a blowjob?"
        scene ep10_jill_solo110 with dissolve
        ji "I can try."
        jump ep10_jill_blowjob_label
    "Boobjob":
        mc "Would you be comfortable massaging my dick with your breasts?"
        scene ep10_jill_solo109 with dissolve
        ji "I can try... I can tell that you like them a lot."
        jump ep10_jill_boobjob_label
    "Continue":
        jump ep10_jill_cont_label

label ep10_jill_boobjob_label:
scene anim_jill_boobjob3_ep10 with dissolve
ji "If I go like this, does it feel good?"
mc "Yeah. It's teasing me like crazy. It makes me wanna push your breasts tighter together and fuck them."
ji "Oh! Um..."
mc "Was that too graphic?"
ji "I don't know how to respond to that."
mc "That's ok. But that's what I'd like to do. Or maybe you could do it?"
ji "How?"
mc "You're up for it?"
ji "Yes."
pause
scene anim_jill_boobjob_ep10 with dissolve
mc "Push them together over my dick like that. Fuck... Yes..."
ji "Like that?"
mc "Yeah. That's amazing. Are you good?"
ji "It's fine. It doesn't hurt."
pause
scene anim_jill_boobjob2_ep10 with dissolve
ji "*{i}Heavy breathing{/i}*"
mc "Are you ok?"
ji "Seeing you up close like this..."
ji "I get aroused from it."
mc "I could cum all over your tits, but I gotta show some restraint. I don't want this to be over already."
pause

menu:
    "Blowjob":
        mc "Can you give me a blowjob?"
        scene ep10_jill_solo110 with dissolve
        ji "I can try."
        jump ep10_jill_blowjob_label
    "Assjob":
        mc "Can you give me an assjob? Put your asscheeks against my dick and start grinding."
        scene ep10_jill_solo107 with dissolve
        ji "Let me know if I'm doing it wrong."
        jump ep10_jill_assjob_label
    "Continue":
        jump ep10_jill_cont_label


label ep10_jill_cont_label:
scene ep10_jill_solo111 with dissolve
mc "I loved that you did that for me."
mc "Now, what about your fantasies? You gave me something I wanted. Let me do the same for you."
scene ep10_jill_solo112 with dissolve
ji "After doing that, I don't think I can say anything that even comes close. My fantasies aren't even...um..."
scene ep10_jill_solo111 with dissolve
mc "It doesn't have to come close. I want to know what you think about when it comes to sex."
mc "You've gotta have some ideas and thoughts, right?"
scene ep10_jill_solo112 with dissolve
ji "Of course, I have thoughts, but-"
scene ep10_jill_solo111 with dissolve
mc "Hey, no buts. Say what you think."
scene ep10_jill_solo112 with dissolve
ji "It's going to sound odd."
scene ep10_jill_solo111 with dissolve
mc "More odd than what I told you to do to me?"
scene ep10_jill_solo113 with dissolve
ji "Maybe not, but I'm not used to talking to you like this."
scene ep10_jill_solo111 with dissolve
mc "I know you're not. And we're getting better at it together now."
scene ep10_jill_solo114 with dissolve
ji "..."
scene ep10_jill_solo115 with dissolve
ji "I've been picturing you..."
scene ep10_jill_solo114 with dissolve
mc "Yes?"
scene ep10_jill_solo116 with dissolve
ji "God, I'm already blushing."
scene ep10_jill_solo117 with dissolve
mc "What am I doing in your fantasy?"
scene ep10_jill_solo118 with dissolve
ji "You're inside of me."
scene ep10_jill_solo117 with dissolve
mc "What part of me?"
scene ep10_jill_solo118 with dissolve
ji "Your penis."
scene ep10_jill_solo117 with dissolve
mc "Uh-huh? What else?"
scene ep10_jill_solo118 with dissolve
ji "You're not all the way inside. You're still and not moving one inch."
ji "And you're rubbing me down there. At the same time. Gently. Very gently."
scene ep10_jill_solo119 with dissolve
ji "And as you rub me... I slowly push you deeper inside of me at my own pace."
ji "And when you're fully inside you go faster with your hand."
ji "And I orgasm from it."
scene ep10_jill_solo118 with dissolve
ji "What do you think?"
scene ep10_jill_solo117 with dissolve
mc "I got even harder picturing it. That's an awesome fantasy."
scene ep10_jill_solo120 with dissolve
ji "No way."
scene ep10_jill_solo117 with dissolve
mc "Let's do it! In what position?"
scene ep10_jill_solo121 with dissolve
ji "Maybe if you sit on the edge like that, and I slowly back into you?"
scene bg anim_jill_insert_ep10 movie with dissolve
ji "*{i}Moans{/i}* Remember, just the tip."
mc "I'll do whatever you want me to."
scene ep10_jill_solo122 with dissolve
ji "Ok... You can start rubbing me now."
scene anim_jill_rub_ep10 with dissolve
mc "Is this slow enough?"
ji "Yes. *{i}Slow deep breath{/i}*"
ji "And if you don't mind... Could you say things to me?"
mc "Dirty talk?"
ji "Yes, but romantic...if it's not too much to ask for."
mc "I'll try."
pause
scene anim_jill_rub2_ep10 with dissolve
mc "Um... I guess I never practiced talking romantically in bed... I'm not quite sure what to say."
ji "Tell me romantic things you'd like to do with me."
mc "Oh! I'd like to kiss your neck and work my way down your entire body with my lips."
mc "And holding you in my arms, I like that a lot. Feeling your body closely against mine... Your warmth... Your soft skin... Your fragrance."
mc "It makes me calm and wild at the same time."
pause
scene bg anim_jill_insert2_ep10 movie with dissolve
ji "*{i}Moans{/i}*"
scene anim_jill_rub3_ep10 with dissolve
mc "Being with you like this feels so right."
ji "The way you hold me makes me feel safe... I want to be yours."
mc "You are mine. And I'm yours, too."
ji "Hngnn... I feel..."
pause
scene ep10_jill_solo123 with vpunch
$ renpy.pause(0.5)
scene ep10_jill_solo123 with vpunch
$ renpy.pause(0.5)
scene ep10_jill_solo123 with vpunch
ji "*{i}Moans{/i}* Ahhh..."
scene ep10_jill_solo124b with dissolve
ji "Wow..."
scene ep10_jill_solo124 with dissolve
ji "*{i}Phew{/i}*"
ji "I didn't think I would, but I reached climax... Just like I wanted to."
ji "You were great."
scene ep10_jill_solo125 with dissolve
mc "That was hot... I could feel how you trembled as you came."
scene ep10_jill_solo124 with dissolve
ji "My entire body was fluttering, not just my stomach this time..."
ji "Wow... My knees feel weak."

scene anim_jill_ride1_ep10 with dissolve
ji "*{i}Moans{/i}* You're not done yet, right?"
mc "No... I've been holding back. When you came, I was kinda close."
ji "That's ok. I don't mind doing this."
mc "I'm sure I wouldn't mind if I could orgasm twice, either."
ji "Twice!? Haha, no... I couldn't do that."
pause
scene anim_jill_ride2_ep10 with dissolve
mc "Your ass cheeks pressing against me feels so hot."
mc "They're soft, wet and slippery... It makes me go crazy."
ji "*{i}Moans{/i}*"
ji "Please let me know if you want me to do something else."
pause

$ tmpInt = 0
label ep10_jill_lewd_loop_label:
menu:
    "Reverse cowgirl":
        $ tmpInt += 1
        scene anim_jill_ride1_ep10 with dissolve
        mc "Ride me, [jill]."
        ji "*{i}Moans{/i}* Am I going too fast?"
        mc "No, you're going kinda slow."
        pause
        scene anim_jill_ride2_ep10 with dissolve
        ji "Oh, is it too slow?"
        mc "Slow is good too. It makes me even hornier."
        pause
        jump ep10_jill_lewd_loop_label
    "Doggystyle":
        $ tmpInt += 1
        scene ep10_jill_solo138 with dissolve
        mc "Put your arms up on the sink. I wanna fuck you from behind."
        scene ep10_jill_solo139 with dissolve
        $ renpy.pause()
        scene anim_jill_doggy1_ep10 with dissolve
        ji "*{i}Moans{/i}* Ahh..."
        mc "God, this feels amazing. I want you, [jill]."
        pause
        scene anim_jill_doggy2_ep10 with dissolve
        mc "You have such an amazing ass. I can't get enough of it."
        menu:
            "Slap it":
                play sound "sound_effects/slap.mp3"
                scene ep10_jill_solo134 with vpunch
                ji "Ahh!"
                scene ep10_jill_solo135 with dissolve
                ji "(Wow... What was that?)"
                scene anim_jill_doggy2_ep10 with dissolve
                pause
            "Don't slap it":
                pause
        jump ep10_jill_lewd_loop_label
    "Missionary":
        $ tmpInt += 1
        scene anim_jill_miss1_ep10 with dissolve
        mc "Damn, you're sexy. I can't believe I get to do this with you."
        ji "Haha, I can't believe I'm having sex in here with you, either."
        pause
        scene anim_jill_miss2_ep10 with dissolve
        mc "It's such a hot sight, seeing you like this. I could cum in an instant."
        ji "Mhm..."
        pause
        jump ep10_jill_lewd_loop_label
    "Standing":
        $ tmpInt += 1
        scene anim_jill_stand1_ep10 with dissolve
        ji "*{i}Moans{/i}* Oh, [mc_jill]..."
        mc "Oh, [jill]."
        ji "Penetrate me."
        mc "I am."
        ji "I mean..."
        mc "Ask me to fuck you."
        ji "I can't say that."
        mc "You can. You don't have to look at me. Just say it."
        pause
        scene anim_jill_stand2_ep10 with dissolve
        ji "Fuck me, [mc_jill]..."
        mc "That's so hot to hear from you. Wow..."
        ji "Fuck me."
        mc "Shit, I'm so close now..."
        pause
        jump ep10_jill_lewd_loop_label
    "Cum" if tmpInt > 2:
        mc "[jill], I'm gonna cum... Can I do it how I want?"
        ji "Yes, show me what you like."
        menu:
            "Facial":
                scene ep10_jill_solo140 with dissolve
                ji "(What's happening?)"
                mc "I'm gonna cum on your face, ok?"
                ji "Uh... What do I do?"
                mc "Stick out your tongue for me."
                scene anim_jill_cum1_ep10 with dissolve
                ji "(My heart is beating so fast... Is he going to orgasm over my face?)"
                pause
                scene anim_jill_cum2_ep10 with dissolve
                mc "Ahh!!!"
                ji "Oh my God!"
                scene ep10_jill_solo141 with dissolve
                mc "*{i}Phew{/i}* Wow..."
                mc "Are you all right?"
                scene ep10_jill_solo142 with dissolve
                ji "Surprised... But yes... I'm ok."
                ji "That was...new."
                scene ep10_jill_solo141 with dissolve
                mc "I hope you didn't mind."
                scene ep10_jill_solo142 with dissolve
                ji "No, it's just that I...um..."
                ji "I didn't think you were going to do that."
                scene ep10_jill_solo141 with dissolve
                mc "It was so hot to me...maybe I should have prepared you more for it?"
                scene ep10_jill_solo143 with dissolve
                ji "I would have hesitated a bit if you had told me that in advance. Haha..."
                ji "But it's fine. I was surprised, that's all."
                scene ep10_jill_solo142 with dissolve
                ji "Can I clean it off?"
                scene ep10_jill_solo141 with dissolve
                mc "Yeah, yeah. Of course."
            "On tits":
                mc "Can I shoot it over your tits while you massage it like you did before?"
                scene anim_jill_boobjob2_ep10 with dissolve
                ji "Like this?"
                mc "Yes, keep going like that. I'm going to cum over your chest..."
                ji "Ok, I want you to do that."
                pause
                scene anim_jill_boobjob_cum_ep10 with hpunch
                mc "Ahh!!!"
                ji "Huh? Oh, wow!"
                pause
                scene ep10_jill_solo131 with dissolve
                ji "Haha... Did I make you do that?"
                mc "Haha, you sure did."
                scene ep10_jill_solo132 with dissolve
                ji "I'm happy I could make you enjoy it."
                scene ep10_jill_solo133 with dissolve
                mc "Oh, this entire bath has been more than enjoyable. It's been amazing."
            "Creampie":
                scene anim_jill_miss1_ep10 with dissolve
                mc "I wanna shoot my load inside you... I want to feel you around my cock as I fill you up."
                ji "That's so hot, [mc_jill]... Go ahead and do it."
                mc "Tell me to do it. Tell me to fill you up."
                ji "Fill me up, [mc_jill]. Cum inside me."
                pause
                scene ep10_jill_solo126 at vpunch, cum1
                $ renpy.pause(0.5)
                scene ep10_jill_solo126 at vpunch, cum1
                $ renpy.pause(0.5)
                scene ep10_jill_solo126 at vpunch, cum1
                mc "Ahh!!!"
                scene ep10_jill_solo127 with dissolve
                ji "Hngn... I can feel it. It's so warm..."
                scene ep10_jill_solo128 with dissolve
                ji "Oh, no! It's going to drip on the carpet!"
                scene ep10_jill_solo129 with dissolve
                mc "Sorry... It's already too late for that."
                mc "Don't worry, I'll clean it up."
                scene ep10_jill_solo130 with dissolve
                ji "Hahaha..."
            "On ass":
                scene anim_jill_doggy1_ep10 with dissolve
                mc "I wanna cum all over your ass."
                ji "Ok. You can do that."
                mc "Tell me to do it. Tell me to cum over it."
                ji "Cum on my ass, [mc_jill]."
                mc "Yeah..."
                ji "Cum all over it."
                scene ep10_jill_solo136 at vpunch, cum3
                $ renpy.pause(0.5)
                scene ep10_jill_solo136 at vpunch, cum3
                $ renpy.pause(0.5)
                scene ep10_jill_solo136 at vpunch, cum3
                mc "Ahh!!!"
                scene ep10_jill_solo137 with dissolve
                mc "Damn... That was so good... Wow..."

scene ep10_jill_solo144 with dissolve
$ renpy.pause()
scene ep10_jill_solo145 with dissolve
ji "*{i}Exhales{/i}* Mmm... There's nothing like a relaxing bath."
scene ep10_jill_solo146 with dissolve
mc "Well, it's either the sex or the bath that made me feel relaxed."
scene ep10_jill_solo145 with dissolve
ji "Perhaps it was both?"
scene ep10_jill_solo146 with dissolve
mc "Maybe... But most likely the sex."
scene ep10_jill_solo145 with dissolve
ji "Haha... Tsk."

scene ep10_jill_solo147 with dissolve
ji "Would you like to spend the night?"
scene ep10_jill_solo149 with dissolve
mc "I'd love to. As long as Tybalt doesn't annoy us again."
scene ep10_jill_solo148 with dissolve
ji "Yeah... It's getting on my nerves so much."
scene ep10_jill_solo149 with dissolve
mc "But this time I'm not letting him win."
stop music fadeout 3
scene ep10_jill_solo150 with dissolve
mc "*{i}Smack{/i}*"

$ renpy.end_replay()
$ persistent.ep10_lewd_jill = True
$ calcScenes()
$ new_bio("Jill", "We had sex in the bathroom. She felt much more comfortable being sexual with me and wanted to try new things.")
$ mphone_stats_add_girl_s3("jill","You had sex with Jill in the hot tub in episode 10.")
$ mgallery_add_photo("ep10_jill_solo_pic0")
show screen new_phone_screen


if branchMayaJosy:
    jump ep10_mj_solo_label

if branchSage:
    jump ep10_sage_solo_label

if branchAlone and ep9_riona_choice == "DIK":
    jump ep10_rio_solo_label    

    
if ep10_dating_nora:
    jump ep10_nora_date_label
    
if branchIsabella:
    jump ep10_bella_solo_label    


    
if ep10_date_nicole and not ep10_cancel_date_nicole:
    jump ep10_nicole_date_label

jump ep10_science_label
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
