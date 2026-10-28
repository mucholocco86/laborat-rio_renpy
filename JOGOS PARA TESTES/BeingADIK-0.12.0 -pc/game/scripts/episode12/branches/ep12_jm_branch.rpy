label ep12_jm_break_label:
$ guideSuggestedPage = 229
$ breakup.append("Josy")
$ breakup.append("Maya")
play music "music/ep9/licensed_music/track128.mp3"
scene ep12_jm_break1 with dissolve
mc "(I'm doing it... I need to let them know about Zoey.)"
mc "(Fuck... This is going to hurt.)"
scene ep12_jm_break2 with wipeleft
$ renpy.pause()
scene ep12_jm_break3 with dissolve
$ renpy.pause()
scene ep12_jm_break4 with dissolve
my "I...don't quite understand."
scene ep12_jm_break5 with dissolve
mc "I want to be with Zoey."
scene ep12_jm_break4 with dissolve
my "Does this have anything to do with us? Like..."
my "Did we do something wrong?"
scene ep12_jm_break5 with dissolve
mc "You haven't done anything wrong. You've been wonderful."
mc "Being with you two has been one of the best things that has ever happened to me."
scene ep12_jm_break6 with dissolve
my "That makes me even more confused."
scene ep12_jm_break5 with dissolve
mc "I'm in love with Zoey. I think I've always been in love with her."
mc "And she told me she loves me."
scene ep12_jm_break7 with dissolve
mc "It would be unfair to you to still be together when I know that's not what I truly want."
mc "And there was no easy way to tell you this."
if check_mlove():
    $ ep12_maya_hurt = True
    scene ep12_jm_break8 with dissolve
    my "You're not in love with me... Are you?"
    scene ep12_jm_break9 with dissolve
    mc "I... I love who you are and what we have had together..."
    mc "But no... I don't love you in that way."
    scene ep12_jm_break10 with dissolve
    my "..."
else:
    scene ep12_jm_break11 with dissolve
    my "I...uh... How do I put this?"
    my "Josy and I have been talking about us, but there are many things left to say."
    scene ep12_jm_break12 with dissolve
    my "I haven't let you two know this yet, but I've also felt unsure about our relationship."
    my "Hearing you say that you love Zoey makes it clear to me..."
    my "I love you, [name]. But I think I love you more as a friend..."
    scene ep12_jm_break11 with dissolve
    my "Even though we've had this great time together, with a lot of fun, deep talks, and amazing sex..."
    my "That final...click - or what you want to call it - hasn't happened yet for me."
    scene ep12_jm_break12 with dissolve
    my "But you've meant a lot to me, in so many different ways."
    my "I don't want it to be over..."
scene ep12_jm_break5 with dissolve
mc "I'm so sorry... It pains me to tell you this, but I have to be honest."
if check_jlove():
    $ ep12_josy_hurt = True
    scene ep12_jm_break18 with dissolve
    js "*{i}Sobs{/i}*"
    mc "Josy..."
    scene ep12_jm_break17 with dissolve
    js "I can't believe you."
    js "You couldn't have let us know that you were in love with your ex-girlfriend earlier?"
    scene ep12_jm_break16 with dissolve
    if ep9_mad_at_zoey:
        mc "I didn't know that I was in love with her. I was mad at her. I didn't think that meant I loved her."
    else:
        mc "I didn't know that I was in love with her. I tried to get over her, but apparently I never did."
    scene ep12_jm_break15 with dissolve
    js "And instead, you toyed with our emotions. You made me fall for you."
    js "What kind of a person does this?"
else:
    scene ep12_jm_break13 with dissolve
    js "This was never going to work out...was it?"
    scene ep12_jm_break14 with dissolve
    mc "What do you mean?"
    scene ep12_jm_break13 with dissolve
    js "There was always something standing in our way."
    js "If it wasn't parents or problems, it was us."
    scene ep12_jm_break14 with dissolve
    mc "We've had a lot against us, there's no denying that... But I gave it my all."
    scene ep12_jm_break15 with dissolve
    js "Did you? Really?"
scene ep12_jm_break19 with dissolve
if ep12_maya_hurt:
    my "Josy... Cut him some slack. It hurts, but it wasn't on purpose."
    my "We said no strings attached, remember?"
else:
    my "Josy... Cut him some slack. We said no strings attached, remember?"
scene ep12_jm_break20 with dissolve
js "You're the one who said that. I never liked the idea."
js "Just because you were unsure and dating a guy was new to you, it didn't mean I felt the same about it."
js "And besides, that was months ago... Things change with time."
scene ep12_jm_break21 with dissolve
my "..."
if ep12_josy_hurt:
    scene ep12_jm_break22 with dissolve
    js "So... *{i}Sniffles{/i}* This is it?"
    js "Is it over like that?"
else:
    scene ep12_jm_break23 with dissolve
    js "I guess this is it then."
scene ep12_jm_break24 with dissolve
mc "I don't know what else to say... I hope we can stay friends."
scene ep12_jm_break23 with dissolve
js "I don't want that."
scene ep12_jm_break24 with dissolve
mc "Josy... Please, don't say that."
if ep12_josy_hurt:
    scene ep12_jm_break15 with dissolve
    js "In what universe do you think I would want to stay friends with you after this?"
    js "You broke my heart!"
else:
    scene ep12_jm_break22 with dissolve
    js "I don't think I can do it, [name]."
scene ep12_jm_break11 with dissolve
my "I think it would be best if you left, [name]."
scene ep12_jm_break9 with dissolve
mc "I'm so sorry."
stop music fadeout 3
scene ep12_jm_break25 with dissolve
$ renpy.pause()

if ep12_josy_hurt:
    $ new_bio("Josy", "I broke up with Josy and Maya to be with Zoey. Josy seemed hurt by it.")
else:
    $ new_bio("Josy", "I broke up with Josy and Maya to be with Zoey. Josy took it well, but she didn't think she could stay my friend after this.")
if ep12_maya_hurt:
    $ new_bio("Maya", "I broke up with Josy and Maya to be with Zoey. Maya seemed hurt by it.")
else:
    $ new_bio("Maya", "I broke up with Josy and Maya to be with Zoey. Maya admitted that she didn't feel the final click.")

if branchJill:
    jump ep12_jill_room_label
jump ep12_bd_label

label ep12_jm_z_label:
scene ep12_jm_z1 with dissolve
mc "(I'm gonna let them know about Zoey.)"
play music "music/ep9/licensed_music/track128.mp3"
scene ep12_jm_z2 with wipeleft
js "She told you she loves you?"
scene ep12_jm_z3 with dissolve
mc "Yes."
scene ep12_jm_z2 with dissolve
js "Out of the blue like that?"
scene ep12_jm_z3 with dissolve
mc "I think she realized she loved me earlier and had to tell me now."
scene ep12_jm_break12 with dissolve
my "What did you do?"
scene ep12_jm_z4 with dissolve
mc "What I just told you. I turned her down."
scene ep12_jm_break12 with dissolve
my "I meant before that. What did you do to make her feel that way?"
scene ep12_jm_z4 with dissolve
mc "Are you implying that I led her on? Because I didn't."
scene ep12_jm_break11 with dissolve
my "It was just a question. I'm trying to make sense of it all."
scene ep12_jm_z4 with dissolve
mc "We've hung out occasionally, and I've just been myself around her."
scene ep12_jm_z6 with dissolve
js "I don't know what to think about this."
js "People have crushes on others all the time, but this is someone close to you who told you she loved you."
js "Like Maya, I'm curious why it happened."
scene ep12_jm_z7 with dissolve
mc "Zoey and I never called each other boyfriend and girlfriend, but I consider her my ex-girlfriend."
mc "And we didn't end our relationship like a normal couple. It was abruptly ended during a time when she was grieving her grandmother."
scene ep12_jm_z8 with dissolve
mc "Maybe for her, the relationship was put on pause. And now, when she returned, she realized it."
mc "And maybe, she needs some more time to accept that we're not a couple anymore. Whereas I did that when she left."
mc "And that's why we are on different pages now."
scene ep12_jm_z5 with dissolve
my "So, in a way, you gave her the breakup talk you never had."
scene ep12_jm_z4 with dissolve
mc "I haven't thought about it that way, but you're right... It felt like closure."
mc "But it's weird, because I see her as my friend now. And I'm at the stage where I've begun letting her back into my life as such."
scene ep12_jm_z9 with dissolve
js "Friends with an ex, huh?"
scene ep12_jm_z8 with dissolve
mc "Do you think that's weird?"
scene ep12_jm_z12 with dissolve
$ renpy.pause()
scene ep12_jm_z6 with dissolve
js "*{i}Sigh{/i}* No. It happens all the time."
js "But it depends on what kind of friendship it will be."
js "I mean, if the feelings for each other were completely gone-"
scene ep12_jm_z7 with dissolve
mc "They are. I don't feel that way about her anymore."
scene ep12_jm_z6 with dissolve
js "But her feelings for you are still there."
js "If both of your feelings were gone, then I could see a friendship work."
js "But as it is now, maybe it won't."
scene ep12_jm_z7 with dissolve
mc "Well, what do you think would happen?"
scene ep12_jm_z5 with dissolve
my "It's not about what would or wouldn't happen. It's more about how your friendship would even work out."
my "Putting myself in her shoes, I don't think I could stay friends with you after this."
scene ep12_jm_z4 with dissolve
mc "Why not?"
scene ep12_jm_break12 with dissolve
my "To see you every day and have you treat me like a friend while I'm in love with you..."
my "Ugh... Put me out of my misery already."
scene ep12_jm_z6 with dissolve
js "Yep. I know I would feel like that."
scene ep12_jm_z7 with dissolve
mc "Fuck... When did it get this complicated?"
mc "She's my childhood friend... She's someone who's meant the world to me growing up."
scene ep12_jm_z6 with dissolve
js "I've had friends like that too."
scene ep12_jm_z7 with dissolve
mc "Where are they now?"
scene ep12_jm_z9 with dissolve
js "After graduation, everyone pretty much went their separate ways. We still keep in touch in DMs, but it's not the same anymore."
js "I think that's a part of life. Sometimes... You outgrow each other."
scene ep12_jm_z10 with dissolve
mc "I don't know what to do now..."
scene ep12_jm_z11 with dissolve
my "We can't answer for you, [name]."
stop music fadeout 3
if check_mlove() and check_jlove():
    scene ep12_jm_z16 with dissolve
elif check_mlove():
    scene ep12_jm_z15 with dissolve
elif check_jlove():
    scene ep12_jm_z14 with dissolve
else:
    scene ep12_jm_z13 with dissolve
$ renpy.pause()
$ new_bio("Josy", "I told Josy and Maya about what happened with Zoey and they took it well. They could relate to the situation better than I thought they would.")
$ new_bio("Maya", "I told Josy and Maya about what happened with Zoey and they took it well. They could relate to the situation better than I thought they would.")

if branchJill:
    jump ep12_jill_room_label

jump ep12_bd_label

label ep12_jsolo_cont_label:
scene ep12_jsolo24 with dissolve
ir "And what about you two?"
ir "How long have you been together? How did you meet?"
scene ep12_jsolo2 with dissolve
mc "Oh, that's a long story. I'm not sure how to tell it..."
scene ep12_jsolo29 with dissolve
js "We met at my summer job."
scene ep12_jsolo19 with dissolve
ir "At the minimart?"
scene ep12_jsolo29 with dissolve
js "We worked together all summer, but didn't talk much until it was time for him to head to college."
js "Little did we know, we both had crushes on each other."
scene ep12_jsolo30 with dissolve
js "We went on a couple of dates, I guess you can call it..."
js "When I felt down, thinking I wouldn't get into college, he showed up to support me."
js "We had a spark between us early on, and it continued to grow, despite the hardships we faced along the way."
scene ep12_jsolo19 with dissolve
ir "What hardships? Have you had trouble?"
scene ep12_jsolo29 with dissolve
js "I don't want to get into details, but we had some tough times in college."
js "But he was always there for me, and I was there for him."
scene ep12_jsolo30 with dissolve
js "That's why I felt like I wanted you to meet him. I guess you can say that it's gotten serious between us... Right, [name]?"
scene ep12_jsolo25 with dissolve
if ep11_josy_love != 2:
    jump ep12_jsolo_choice_label
menu:
    "You can say that":
        label ep12_jsolo_choice_label:
        if tc > 4 and not persistent.no_cheater:
            mc "Um..."
            scene ep12_jsolo24 with dissolve
            ir "Haha, you're putting him on the spot here."
        else:
            mc "You can say that."
            mc "It's my first serious relationship."
            scene ep12_jsolo31 with dissolve
            $ renpy.pause()
            scene ep12_jsolo24 with dissolve
            ir "What a nice story."
    "I love her":
        mc "I'd take it further than that."
        scene ep12_jsolo26 with dissolve
        mc "I love your daughter."
        scene ep12_jsolo31 with dissolve
        $ renpy.pause()
        scene ep12_jsolo27 with dissolve
        ir "I admire your candor. It's brave to say that to your girlfriend's mother. Especially at your age."
        scene ep12_jsolo26 with dissolve
        mc "Well, that's how I feel."
        scene ep12_jsolo30 with dissolve
        js "I love him too."
        scene ep12_jsolo24 with dissolve

if (tc < 5 or persistent.no_cheater) or ep11_josy_love > 0:
    ir "I think you two make a beautiful couple."
    ir "You're tall and handsome and compliment Josephine's looks well."
    scene ep12_jsolo28 with dissolve
    ir "You look aesthetic together."
scene ep12_jsolo32 with dissolve
cli "Well, I feel it's time for coffee. Anyone else?"
scene ep12_jsolo36 with dissolve
js "This late? Um. I'll pass."
scene ep12_jsolo32 with dissolve
cli "[name]?"
scene ep12_jsolo33 with dissolve
mc "Sure. Make it half a cup."
scene ep12_jsolo34 with dissolve
js "I need to use the restroom. Will you be ok?"
scene ep12_jsolo35 with dissolve
mc "I think I'll manage, haha."
scene ep12_jsolo37 with dissolve
$ renpy.pause()
scene ep12_jsolo38 with dissolve
ir "She's headstrong, my little girl. I'm glad to see that she knows what she wants with her business."
scene ep12_jsolo40 with dissolve
mc "I don't understand much of it, but it seems to make her happy, and that makes me happy too."
scene ep12_jsolo41 with dissolve
$ renpy.pause()
if tc < 5 or persistent.no_cheater:
    scene ep12_jsolo42 with dissolve
else:
    scene ep12_jsolo42b with dissolve
$ renpy.pause()
scene ep12_jsolo43 with dissolve
$ renpy.pause()
if ep12_josy_defend_count > 0:
    scene ep12_jsolo44 with dissolve
    ir "I like you. You're quite forward and not the silent type."
    scene ep12_jsolo45 with dissolve
    mc "What do you mean?"
    scene ep12_jsolo44 with dissolve
    ir "Speaking up for Josephine like that. I got the sense that you were protecting her."
    scene ep12_jsolo45 with dissolve
    mc "No offense, but I thought some of Clive's comments were uncalled for."
    scene ep12_jsolo46 with dissolve
    ir "None taken. Clive is protective of me as well. You share that admirable trait."
    scene ep12_jsolo47 with dissolve
    mc "You don't strike me as someone who needs protection."
    scene ep12_jsolo46 with dissolve
    ir "Neither does Josephine."
    scene ep12_jsolo48 with dissolve
    mc "She might not need it, but I think she likes to know that I'm in her corner supporting her."
else:
    scene ep12_jsolo44 with dissolve
    ir "You seem like the quiet but supportive type."
    scene ep12_jsolo45 with dissolve
    mc "I'm not that quiet."
    scene ep12_jsolo44 with dissolve
    ir "Well, you bit your tongue, but I could tell that Clive's comments bugged you."
    scene ep12_jsolo45 with dissolve
    mc "What good would pointing it out have done? It would have created an awkward atmosphere."
    scene ep12_jsolo46 with dissolve
    ir "I get it. It's your first time meeting your girlfriend's mother. You want to appear polite."
    ir "For some people, it takes a while to get comfortable. There's nothing wrong with it."
    scene ep12_jsolo48 with dissolve
    mc "I feel comfortable here. You've been welcoming."
    mc "And trust me, if it was something serious and Josy needed me to speak up, I would."
scene ep12_jsolo49 with dissolve
ir "It makes me happy that she's found someone who takes good care of her."
ir "Your relationship came as a surprise to me. I wasn't even aware that she was dating."
ir "She doesn't talk to me about her dating life. I've felt out of the loop with her."
scene ep12_jsolo47 with dissolve
mc "Do you spend a lot of time together?"
scene ep12_jsolo50 with dissolve
ir "Not these days. I wish I had more time to spend with her, but time is a luxury."
scene ep12_jsolo51 with dissolve
mc "A few minutes ago, I heard someone describe that your time brings value to a company."
mc "Your time also brings value to your relationship with Josy."
scene ep12_jsolo46 with dissolve
if ep12_josy_defend_count > 0:
    ir "Touché."
else:
    ir "Look who's found his voice. Touché."
scene ep12_jsolo52 with dissolve
ir "I'd love to spend more time with her, but she's been living with Pete - my ex-husband - and she doesn't visit that often."
ir "That makes it harder to be present."
scene ep12_jsolo53 with dissolve
mc "I get it, but you could always call her more. Send her more texts and share what you're up to, and maybe she'll do the same."
if ep11_josy_solo:
    mc "And if I could suggest something else..."
    scene ep12_jsolo54 with dissolve
    mc "Don't call her when you're busy at work. To me, you came across as not listening while you were talking to us on the phone."
    mc "Granted, it was just an observation made from one phone call, but I noticed it bugged her..."
    mc "...and that was my first impression of you."
scene ep12_jsolo55 with dissolve
ir "..."
scene ep12_jsolo56 with dissolve
js "Hey. Missed me?"
scene ep12_jsolo57 with dissolve
mc "Always."
scene ep12_jsolo58 with dissolve
js "What are we talking about?"
scene ep12_jsolo59 with dissolve
ir "We've shared some valuable insights with each other."
scene ep12_jsolo60 with dissolve
ir "Hold on tight to this one. He's a keeper."
if (tc < 5 or persistent.no_cheater) or ep11_josy_love > 0:
    scene ep12_jsolo61 with dissolve
    $ renpy.pause()

if ep12_josy_defend_count > 0:
    $ new_bio("Josy", "I visited Josy's mom Iris over Christmas. I defended Josy in the conversation, and Iris liked that.")
else:
    $ new_bio("Josy", "I visited Josy's mom Iris over Christmas. I let Josy stand up for herself in the conversation.")

$ renpy.music.stop(channel="sfx2", fadeout=3)
scene ep12_jsolo62 with wiperight
js "Goodnight!"
scene ep12_jsolo63 with dissolve
js "I hope you don't regret coming here."
scene ep12_jsolo64 with dissolve
mc "I don't. I've had a good time. But..."
scene ep12_jsolo65 with dissolve
js "But what?"
scene ep12_jsolo66 with dissolve
mc "Some of the things said tonight bugged me, that's all."
scene ep12_jsolo67 with dissolve
js "Was it what Clive said?"
scene ep12_jsolo66 with dissolve
mc "He tried to find something negative in everything you said, and your mom seemed oblivious that her words hurt you."
mc "At first, I thought she was trying to make you feel bad on purpose."
scene ep12_jsolo68 with dissolve
js "No, no. That's just Mom."
js "She is blunt and hard to please, but she does compliment me too."
js "She was excited about my company. I think it reminded her of her own journey."
scene ep12_jsolo66 with dissolve
mc "But she didn't like it when you rejected her advice."
scene ep12_jsolo69 with dissolve
js "I don't want to do it her way; I want to do it mine."
scene ep12_jsolo66 with dissolve
mc "I totally get that, but it didn't seem like she did."
scene ep12_jsolo68 with dissolve
js "As I said, she's hard to please. That's her personality; don't read too much into it."
scene ep12_jsolo66 with dissolve
mc "I saw another side to her, too. So, it wasn't all bad."
scene ep12_jsolo67 with dissolve
js "But you're right about Clive. He's a walking guilt trip machine."
js "I think he's protective of Mom, and he can't stand Dad. I think he still views him as competition, which is ridiculous."
js "And since I love Dad, maybe Clive lumps me together with him."
scene ep12_jsolo68 with dissolve
js "I don't know what it is, but it annoys me."
js "He does love and care for Mom, so I'm thankful for that."
scene ep12_jsolo69 with dissolve
js "I thought it was sweet that Mom was interested in our relationship."
scene ep12_jsolo70 with dissolve
mc "It was. It was the first time we talked about us like that to someone."
scene ep12_jsolo68 with dissolve
js "I didn't want to be dodgy when I told her about our past. Did you get the feeling that I was?"
scene ep12_jsolo66 with dissolve
mc "I think you handled it great."
mc "I mean, I wish we could have told her about Maya, but..."
scene ep12_jsolo68 with dissolve
js "I think her reaction would have been way different if we had."
scene ep12_jsolo66 with dissolve
mc "No kidding... It would."
mc "How long do you intend to keep it from her? Do you plan on ever telling her?"
scene ep12_jsolo71 with dissolve
js "..."
scene ep12_jsolo68 with dissolve
js "*{i}Sigh{/i}* Why can't everything be normal?"
js "It felt so good being with you tonight."
scene ep12_jsolo69 with dissolve
js "We could talk openly about our relationship and not be scared to be ourselves. That's what I want."
scene ep12_jsolo70 with dissolve
mc "I know. We don't have to think about it now. Let's end the night on a good note."
scene ep12_jsolo74 with dissolve
mc "This apartment is quite something. How successful is Iris?"
scene ep12_jsolo68 with dissolve
js "I don't want to brag, but she's influential."
js "Have you ever heard of IM Couture?"
scene ep12_jsolo70 with dissolve
mc "Nope. That sounds like Greek to me."
scene ep12_jsolo68 with dissolve
js "Couture is actually French. The IM part is her initials."
scene ep12_jsolo70 with dissolve
mc "Is she French?"
scene ep12_jsolo69 with dissolve
js "Haha, no. It's a concept in fashion."
js "The clothes her company designs are high quality, and they don't mass-produce anything they make."
scene ep12_jsolo72 with dissolve
js "Mom's business idea is to create fashion for rich people."
js "A single bra can cost you anywhere from $300 to $700."
scene ep12_jsolo73 with dissolve
mc "For a bra!? Holy shit. What about panties?"
scene ep12_jsolo72 with dissolve
js "Those are sold separately for a price not that far off."
js "You couldn't guess what they charge for the dresses."
js "I think the most expensive piece of clothing they ever sold was for over one hundred grand."
scene ep12_jsolo73 with dissolve
mc "Who would buy something for that much money?"
scene ep12_jsolo72 with dissolve
js "Rich people and celebrities will."
js "Mom's brand is not that expensive compared to the upper echelon of the fashion industry."
js "It's just high enough not to be affordable by the middle class."
scene ep12_jsolo66 with dissolve
mc "Oh... How do you feel about that?"
scene ep12_jsolo68 with dissolve
js "Hm? Do you feel like it's not right?"
scene ep12_jsolo66 with dissolve
mc "To charge that much for clothes? And also, with intention of preventing non-rich people from buying it. Hell no. Do you?"
scene ep12_jsolo68 with dissolve
js "I get what you mean, but that's how some businesses work. Her brand can be seen as a status symbol, and that sells."
js "I don't wear her brand. I've never worn it."
js "She once gave me a blouse for Christmas, but I told her I couldn't wear it."
scene ep12_jsolo66 with dissolve
mc "Because of your principles?"
scene ep12_jsolo69 with dissolve
js "No, because I was scared that I'd spill something on it and ruin it."
js "Knowing that her clothes cost that much, I could never feel comfortable wearing them."
scene ep12_jsolo68 with dissolve
js "But it doesn't matter how we feel about her business."
js "Someone will do the job because there's demand, and she decided to be a supplier."
js "And like it or not, she is successful doing it."
js "And the price range set aside... Her clothes are beautiful, and she's super-talented."
scene ep12_jsolo69 with dissolve
js "Wanna see some of the clothes she designs?"
scene ep12_jsolo73 with dissolve
mc "Sure. Maybe it will help change my mind."
scene ep12_jsolo75 with dissolve
js "This is a dress she's been working on."
scene ep12_jsolo76 with dissolve
mc "It's pretty, but also see-through."
scene ep12_jsolo77 with dissolve
js "I know. I think someone ordered it for a gala."
scene ep12_jsolo78 with dissolve
js "And she also has boxes of new underwear in here."
mc "Any $300 bras in them?"
scene ep12_jsolo77 with dissolve
js "Probably in all of them."
scene ep12_jsolo79 with dissolve
mc "I bet you'd look like a million bucks wearing those."
scene ep12_jsolo80 with dissolve
js "..."
scene ep12_jsolo81 with dissolve
js "I have an idea. Get ready for bed and wait for me in the bedroom."
scene ep12_jsolo80 with dissolve
mc "What's the idea?"
stop music fadeout 3
scene ep12_jsolo81 with dissolve
js "You'll see."

label ep12_jsolo_lewd_label:
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
    $ ep11_josy_love = 2
play music "music/ep3/dc_love_go_go.mp3"
queue music ["music/ep3/some_obsession.mp3","music/ep3/dc_love_go_go.mp3"]
$ renpy.sound.play("sound_effects/season3/fireplace.mp3", channel="sfx2", loop=True)
hide screen new_phone_screen
scene ep12_jsolo_lewd1 with dissolve
$ renpy.pause()
scene ep12_jsolo_lewd2 with dissolve
js "Are you ready?"
scene ep12_jsolo_lewd3 with dissolve
mc "I think I am. But for what?"
scene ep12_jsolo_lewd4 with dissolve
js "Josephine Taylor presents: The IM Couture Fashion Show."
js "Live from this bedroom."
scene bg anim_josy_pan_ep12 movie with dissolve
js "Josephine is wearing the latest lingerie design from IM Couture."
js "If you ever wondered what rich people look like in the bedroom, look no further."
pause
scene ep12_jsolo_lewd5 with dissolve
js "The intricate seams are made from the highest quality material."
scene ep12_jsolo_lewd6 with dissolve
js "And as the Couture name implies, everything you see is handmade."
scene ep12_jsolo_lewd7 with dissolve
mc "That's handmade? I see what you mean by no mass production."
scene ep12_jsolo_lewd8 with dissolve
js "Haha! So, what do you think?"
scene ep12_jsolo_lewd9 with dissolve
mc "I think I want to rip those clothes off you, but I can't afford it."
scene ep12_jsolo_lewd10 with dissolve
js "Hahaha!"
scene ep12_jsolo_lewd11 with dissolve
mc "You look stunning in them."
scene ep12_jsolo_lewd12 with dissolve
js "Do you get why people spend that much money on these?"
scene ep12_jsolo_lewd13 with dissolve
mc "No. I think you'd look as amazing in something cheaper too."
mc "It's not the clothes that make you look that good, it's you."
scene ep12_jsolo_lewd14 with dissolve
$ renpy.pause()
scene ep12_jsolo_lewd12 with dissolve
js "You're so sweet."
js "I should put these back..."
scene ep12_jsolo_lewd13 with dissolve
mc "Now?"
scene ep12_jsolo_lewd15 with dissolve
js "You make a good point, but..."
scene ep12_jsolo_lewd16 with dissolve
js "Let's do it... But don't get any stains on them."
scene ep12_jsolo_lewd17 with dissolve
mc "Don't worry. I'll have them off in no time."
play sound "sound_effects/clothes.mp3"
scene bg anim_josy_clothes_ep12 movie with dissolve
pause
scene ep12_jsolo_lewd18 with dissolve
$ renpy.pause()
scene ep12_jsolo_lewd19 with dissolve
$ renpy.pause()
scene ep12_jsolo_lewd20 with dissolve
label ep12_jsolo_lewd_loop_label:
menu:
    "Caress her":
        scene anim_josy_caress_ep12 with dissolve
        mc "I like the feeling of the bra."
        js "Mmm... Be careful now."
        pause
        jump ep12_jsolo_lewd_loop_label
    "Kiss her":
        scene anim_josy_kiss_ep12 with dissolve
        js "*{i}Smack{/i}* Hngn..."
        pause
        scene anim_josy_kiss2_ep12 with dissolve
        js "*{i}Moans{/i}*"
        pause
        jump ep12_jsolo_lewd_loop_label
    "Tease her nipple":
        scene anim_josy_nipple_ep12 with dissolve
        mc "This bra is basically nothing. I could feel your nipples through it."
        js "Yeah, it's delicate."
        pause
        jump ep12_jsolo_lewd_loop_label
    "Continue":
        scene ep12_jsolo_lewd21 with dissolve
        $ renpy.pause()

scene ep12_jsolo_lewd22 with dissolve
mc "The bra was nice, but this is better..."
scene ep12_jsolo_lewd23 with dissolve
$ renpy.pause()

label ep12_jsolo_lewd_loop2_label:
menu:
    "Pinch nipple":
        scene anim_josy_nipple_pinch_ep12 with dissolve
        pause
        jump ep12_jsolo_lewd_loop2_label
    "Suck nipple":
        scene anim_josy_nipple_suck_ep12 with dissolve
        js "*{i}Soft moan{/i}*"
        pause
        jump ep12_jsolo_lewd_loop2_label
    "Pleasure her":
        scene anim_josy_fondle_ep12 with dissolve
        js "I'm so turned on by you."
        mc "I know what you mean. I got rock hard fingering you."
        pause
        scene anim_josy_fondle2_ep12 with dissolve
        js "*{i}Moans{/i}*"
        pause
        jump ep12_jsolo_lewd_loop2_label
    "Lick panties":
        scene ep12_jsolo_lewd24 with dissolve
        mc "Can I lick it?"
        js "Hm... I don't think you should."
        scene anim_josy_lick_ep12 with dissolve
        mc "*{i}Lick lick{/i}* Just for a little bit."
        js "*{i}Moans{/i}* Fuck! [mc_josy]..."
        pause
        scene anim_josy_lick2_ep12 with dissolve
        js "Hngn... You're so good at that."
        pause
        jump ep12_jsolo_lewd_loop2_label
    "Spank ass":
        scene bg anim_josy_spank_ep12 movie with dissolve
        js "*{i}Gasps{/i}* Mmm... [mc_josy]..."
        mc "Your ass looks amazingly naughty."
        pause
        scene bg anim_josy_spank2_ep12 movie with dissolve
        js "What makes it naughty?"
        mc "The thought of knowing you borrowed that expensive underwear without asking."
        pause
        scene bg anim_josy_spank3_ep12 movie with dissolve
        js "Haha... I am a bit naughty."
        pause
        jump ep12_jsolo_lewd_loop2_label
    "Continue":
        scene ep12_jsolo_lewd25 with dissolve
        js "It's getting hot in here... I think it's time."
        scene ep12_jsolo_lewd26 with dissolve
        mc "Hey... What about me?"
        scene ep12_jsolo_lewd27 with dissolve
        js "What about you?"
        scene ep12_jsolo_lewd26 with dissolve
        mc "I'm not quite ready yet..."
        scene ep12_jsolo_lewd28 with dissolve
        js "From the looks of it, you are."
        scene ep12_jsolo_lewd29 with dissolve
        js "But don't worry. I will take good care of you."

$ tmpInt = 0
label ep12_jsolo_lewd_loop3_label:
menu:
    "Handjob":
        $ tmpInt += 1
        scene anim_josy_hj1_ep12 with dissolve
        js "Not ready, he said. Your cock is throbbing in my hands."
        mc "You have that effect on me, [josy]."
        pause
        scene anim_josy_hj2_ep12 with dissolve
        js "Hngn... I thought you wanted {b}me{/b} to give {b}you{/b} pleasure."
        mc "Why not both?"
        js "*{i}Moans{/i}* Because I cum too fast with you,. You know that."
        pause
        jump ep12_jsolo_lewd_loop3_label
    "Blowjob":
        $ tmpInt += 1
        scene anim_josy_bj1_ep12 with dissolve
        js "*{i}Suck suck{/i}*"
        mc "Fuck... The warmth of your mouth on top of all that teasing..."
        mc "If you're not careful, I'll cum early tonight."
        pause
        scene anim_josy_bj2_ep12 with dissolve
        js "*{i}Suck lick{/i}* I'll be gentle."
        mc "Hngn... Being gentle might also make me cum fast. Fuck, [josy]..."
        pause
        jump ep12_jsolo_lewd_loop3_label
    "Thighjob":
        $ tmpInt += 1
        scene anim_josy_tj1_ep12 with dissolve
        mc "Damn, you're squeezing it good..."
        mc "Too good. Fuck!"
        pause
        scene anim_josy_tj2_ep12 with dissolve
        js "Think of something else."
        mc "How can I? All I can think of is those sexy thighs of yours milking my cock."
        pause
        jump ep12_jsolo_lewd_loop3_label
    "Continue" if tmpInt > 1:
        scene anim_josy_tease1_ep12 with dissolve
        mc "Mmm... I want you."
        js "Nuh-uh. Not yet."
        mc "I wanna slide inside you."
        pause
        scene anim_josy_tease2_ep12 with dissolve
        js "*{i}Moans{/i}* Be still or you will. I'm so goddamned wet."
        mc "Let me slide in..."
        js "When I tell you it's ok, you may."
        mc "I want it now..."
        pause

js "Put it in, [mc_josy]..."
scene bg anim_josy_insert_ep12 movie with dissolve
js "*{i}Moans{/i}* Yes! Yes!"
pause
scene anim_josy_ride1_ep12 with dissolve
mc "Ride me, [josy]!"
js "Be mindful... They are on the other side of the apartment, but it doesn't mean we can be as loud as we want."
pause
scene anim_josy_ride2_ep12 with dissolve
mc "I'm trying, but it's too fucking good."
js "*{i}Moans{/i}*"
pause
$ tmpInt = 0
$ tmpBool3 = False
$ tmpBool = False
label ep12_jsolo_lewd_loop4_label:
menu:
    "Cowgirl":
        $ tmpInt += 1
        scene anim_josy_ride1_ep12 with dissolve
        pause
        scene anim_josy_ride2_ep12 with dissolve
        pause
        jump ep12_jsolo_lewd_loop4_label
    "Doggystyle":
        $ tmpInt += 1
        scene anim_josy_doggy1_ep12 with dissolve
        pause
        scene anim_josy_doggy2_ep12 with dissolve
        pause
        if not tmpBool:
            $ tmpBool = True
            scene ep12_jsolo_lewd46 with vpunch
            js "*{i}Moans{/i}* Ahhh! Fuck! I'm cumming!"
            scene ep12_jsolo_lewd47 with vpunch
            js "*{i}Moans{/i}*"
            mc "Haha... What happened to keeping it down?"
            scene ep12_jsolo_lewd48 with dissolve
            js "*{i}Gasps{/i}* Was I that loud?"
            scene ep12_jsolo_lewd47 with dissolve
            mc "I hope not, but you were louder than me."
        jump ep12_jsolo_lewd_loop4_label
    "Lifting":
        $ tmpInt += 1
        scene anim_josy_lift1_ep12 with dissolve
        js "Fuck me, [mc_josy]..."
        pause
        scene anim_josy_lift2_ep12 with dissolve
        mc "Damn... Your ass is so tight in my hands..."
        pause
        jump ep12_jsolo_lewd_loop4_label
    "Standing":
        $ tmpInt += 1
        scene anim_josy_stand1_ep12 with dissolve
        js "*{i}Moans{/i}* Don't hold anything back now... I want all of you."
        mc "I'm giving you everything I got."
        js "Mmm... Good."
        pause
        scene anim_josy_stand2_ep12 with dissolve
        js "Ahh... I love this... Hngn..."
        pause
        jump ep12_jsolo_lewd_loop4_label
    "Prone (Anal)":
        $ tmpInt += 1
        if not tmpBool3:
            $ currentEvent = "ep12_josy_lewd_anal3_label"
            scene ep12_jsolo_lewd36 with dissolve
            jump ep12_anal_intro_label
        label ep12_josy_lewd_anal3_label:
        scene anim_josy_prone1_ep12 with dissolve
        js "*{i}Moans{/i}* Oh, fuck! Hngn..."
        mc "It's so tight."
        js "Yeah, I could have used a buttplug tonight."
        pause
        scene anim_josy_prone2_ep12 with dissolve
        mc "I think you're doing great without it. Does it hurt?"
        js "Not as much as last time."
        pause
        jump ep12_jsolo_lewd_loop4_label
    "Piledriver (Anal)":
        $ tmpInt += 1
        if not tmpBool3:
            $ currentEvent = "ep12_josy_lewd_anal1_label"
            scene ep12_jsolo_lewd37 with dissolve
            jump ep12_anal_intro_label
        label ep12_josy_lewd_anal1_label:
        scene anim_josy_pile1_ep12 with dissolve
        js "Oh, fuck! Oh, God! Ahhh..."
        mc "Keep it down a bit..."
        js "How can I, when you're fucking me like this?"
        pause
        scene anim_josy_pile2_ep12 with dissolve
        js "*{i}Moans{/i}*"
        pause
        jump ep12_jsolo_lewd_loop4_label
    "Cowgirl (Anal)":
        $ tmpInt += 1
        if not tmpBool3:
            $ currentEvent = "ep12_josy_lewd_anal2_label"
            scene ep12_jsolo_lewd38 with dissolve
            jump ep12_anal_intro_label
        label ep12_josy_lewd_anal2_label:
        scene anim_josy_ride3_ep12 with dissolve
        js "Hngn... I want you to cum for me, [mc_josy]. Can you cum for me?"
        pause
        scene anim_josy_ride4_ep12 with dissolve
        mc "You want me to cum now?"
        js "Mhm... Cum, [mc_josy]... Cum for me."
        pause
        jump ep12_jsolo_lewd_loop4_label
    "Cum" if tmpInt > 3:
        mc "I'm gonna cum..."
        menu:
            "Creampie":
                scene anim_josy_stand1_ep12 with dissolve
                js "I know you want to cum for me."
                js "Show me how much pleasure I give you."
                scene anim_josy_stand3_ep12 at hpunch, cum2
                mc "Ahh!"
                js "*{i}Moans{/i}*"
                scene ep12_jsolo_lewd30 with dissolve
                $ renpy.pause()
            "Creampie (Anal)":
                scene anim_josy_ride3_ep12 with dissolve
                js "Cum inside, me [mc_josy]."
                scene anim_josy_ride5_ep12 at vpunch, cum2
                mc "Ahh!"
                js "*{i}Moans{/i}*"
                pause
                scene ep12_jsolo_lewd31 with dissolve
                $ renpy.pause()
            "On ass (Anal)":
                scene anim_josy_prone1_ep12 with dissolve
                mc "I wanna cum all over you."
                js "I know you want to cum for me."
                js "Show me how much pleasure I give you."
                pause
                scene ep12_jsolo_lewd32 at hpunch, cum2
                $ renpy.pause(0.5)
                scene ep12_jsolo_lewd32 at hpunch, cum2
                $ renpy.pause(0.5)
                scene ep12_jsolo_lewd32 at hpunch, cum2
                mc "Ahh!"
                scene ep12_jsolo_lewd33 with dissolve
                js "Mmm... Yes..."
            "In mouth":
                scene anim_josy_bj1_ep12 with dissolve
                js "*{i}Suck suck{/i}*"
                mc "Fuck, I'm gonna cum in your mouth."
                scene ep12_jsolo_lewd34 at hpunch, cum1
                $ renpy.pause(0.5)
                scene ep12_jsolo_lewd34 at hpunch, cum1
                $ renpy.pause(0.5)
                scene ep12_jsolo_lewd34 at hpunch, cum1
                mc "Ahh! Fuck!"
                scene ep12_jsolo_lewd35 with dissolve
                js "Mmm..."
        jump ep12_jsolo_lewd_after_label

label ep12_anal_intro_label:
$ tmpBool3 = True
js "You're not going for that hole without lube, are you?"
mc "I want it..."
scene ep12_jsolo_lewd39 with dissolve
js "Say you have the best girlfriend ever."
scene ep12_jsolo_lewd40 with dissolve
mc "Oh, I do!"
mc "I can't believe you brought that to your mom's place."
scene ep12_jsolo_lewd39 with dissolve
js "Only because I knew you were coming."
scene ep12_jsolo_lewd40 with dissolve
mc "Obviously. But still."
scene ep12_jsolo_lewd39 with dissolve
js "Take it slow... I'm still not used to this."
$ renpy.jump(currentEvent)

label ep12_jsolo_lewd_after_label:
scene ep12_jsolo_lewd42 with dissolve
$ renpy.pause()
scene ep12_jsolo_lewd41 with dissolve
$ renpy.pause()
scene ep12_jsolo_lewd43 with dissolve
js "I hope we didn't ruin the underwear."
scene ep12_jsolo_lewd44 with dissolve
mc "Iris can probably sell them as slightly used."
scene ep12_jsolo_lewd43 with dissolve
js "Haha! Eww."
scene ep12_jsolo_lewd44 with dissolve
mc "Thanks for the fashion show. It was the best one I've been to."
if ep11_josy_love == 2:
    scene ep12_jsolo_lewd43 with dissolve
    js "I love you."
$ renpy.music.stop(channel="sfx2", fadeout=3)
stop music fadeout 3
scene ep12_jsolo_lewd45 with dissolve
$ renpy.pause()
$ renpy.end_replay()
$ persistent.ep12_lewd_josy = True
$ calcScenes()
$ mphone_stats_add_girl_s3("josy","You had sex with Josy at her mom's place in episode 12.")
if not persistent.ep12_card15 or not persistent.ep12_card16:
    if not persistent.ep12_card15:
        $ persistent.ep12_card15 = True
        $ persistent.rew_2d_unlocked += 1
        $ persistent.chat_new_rewards = True
        $ calcRenders()
    if not persistent.ep12_card16:
        $ persistent.ep12_card16 = True
        $ persistent.rew_2d_unlocked += 1
        $ persistent.chat_new_rewards = True
        $ calcRenders()
    show screen srmsg
    $ renpy.pause(3)
    hide screen srmsg
$ mgallery_add_photo("ep12_josy_solo_pic1")
$ mgallery_add_photo("ep12_josy_solo_pic2")
$ mgallery_add_photo("ep12_josy_solo_pic3")
show screen new_phone_screen
jump ep12_ret_label

label ep12_pre_ret_label:
show screen new_phone_screen
play music "music/ep11/licensed_music/track172.mp3"
scene ep12_pre_ret1 with wipeleft
mc "(Home sweet home...)"
play sound "sound_effects/cellphone.mp3"
scene ep12_pre_ret2 with dissolve
"*{i}Phone rings{/i}*"
mc "Hey, Maya. Great timing; I just returned to the DIKs."
scene ep12_pre_ret3 with dissolve
my "Oh, you're back already?"
scene ep12_pre_ret2 with dissolve
mc "Yeah. I'm gonna check out the venue for our New Year's Eve party today and get a workout in."
scene ep12_pre_ret3 with dissolve
my "You're gonna love it. I went there already with Sage."
my "How was Christmas?"
if ep12_jsolo:
    scene ep12_pre_ret4 with dissolve
    mc "I had a nice time with Dad, and I...went to visit Josy yesterday."
    scene ep12_pre_ret5 with dissolve
    my "At her mom's place?"
    scene ep12_pre_ret4 with dissolve
    mc "Yeah. I got to meet Iris and Clive."
    scene ep12_pre_ret5 with dissolve
    my "Oh... I wasn't aware that you did that."
    scene ep12_pre_ret7 with dissolve
    mc "I know... Josy wanted me to meet her mom and...you know how it is with our parents."
    scene ep12_pre_ret6 with dissolve
    my "I hope you had a nice visit then."
    my "..."
else:
    scene ep12_pre_ret8 with dissolve
    mc "I had a great time with Dad. It felt nice to unwind together with him."
    mc "How about you?"
    scene ep12_pre_ret9 with dissolve
    my "I can't complain."
my "Would you like to get together tonight?"
scene ep12_pre_ret8 with dissolve
mc "Sure. Do you want me to swing by?"
scene ep12_pre_ret9 with dissolve
my "Yeah, I'm running some errands today, but after that I'll be in my dorm."
if not ep12_jsolo:
    scene ep12_pre_ret4 with dissolve
    mc "Is Josy coming?"
    scene ep12_pre_ret5 with dissolve
    my "I believe she's at Pete's celebrating Christmas today."
    scene ep12_pre_ret2 with dissolve
    mc "Then we'll have some quality time together, you and I."
    mc "See you soon, then."
else:
    scene ep12_pre_ret10 with dissolve
    mc "What kind of errands?"
    scene ep12_pre_ret9 with dissolve
    my "I'm picking up some clothes that I ordered and buying some decor for the party. It was one of my responsibilities."
    scene ep12_pre_ret10 with dissolve
    mc "All the decor?"
    scene ep12_pre_ret9 with dissolve
    my "No, just some of it. I got a list."
    scene ep12_pre_ret2 with dissolve
    mc "Good luck with it, and I'll see you tonight."
scene ep12_pre_ret3 with dissolve
my "Can't wait!"
jump ep12_ret2_label

label ep12_msolo_label:
show screen new_phone_screen
play music "music/ep12/licensed_music/track221.mp3"
queue music ["music/ep12/licensed_music/track220.mp3","music/ep12/licensed_music/track221.mp3"]
scene ep12_msolo1 with wipeleft
mc "I'm here."
scene ep12_msolo2 with dissolve
mc "Whoa... I didn't expect to walk in on this."
scene ep12_msolo3 with dissolve
my "Help me!"
scene ep12_msolo4 with dissolve
mc "Uh oh... What now?"
scene ep12_msolo3 with dissolve
my "I don't know what to do..."
scene ep12_msolo4 with dissolve
mc "What's wrong?"
scene ep12_msolo5 with dissolve
my "I can't decide what to wear for New Year's Eve."
scene ep12_msolo6 with dissolve
mc "What? *{i}Sigh{/i}* That's it!?"
scene ep12_msolo5 with dissolve
my "What?"
scene ep12_msolo6 with dissolve
mc "I thought you were in real trouble or something; my heart skipped a beat."
scene ep12_msolo7 with dissolve
my "I'm sorry... But I can't decide, and I'm freaking out about it. See, I ordered two dresses, and I like them both."
scene ep12_msolo8 with dissolve
mc "Then wear them both."
scene ep12_msolo7 with dissolve
my "They're for the New Year's Eve party. I'm not sure I'll have use for them at another party."
scene ep12_msolo8 with dissolve
mc "Then wear the first one for half of the party and change into the second one for the other half."
scene ep12_msolo10 with dissolve
my "You're not funny."
scene ep12_msolo9 with dissolve
mc "Haha! I wouldn't mind seeing that."
mc "Come on. Laugh!"
scene ep12_msolo11 with dissolve
mc "What are you going to do? You bought them already."
scene ep12_msolo12 with dissolve
my "I'll return the one I don't use."
scene ep12_msolo11 with dissolve
mc "Try them on for me. I'll help you decide."
play sound "sound_effects/clothes.mp3"
scene ep12_msolo13 with dissolve
$ renpy.pause()
scene ep12_msolo14 with dissolve
mc "Ok. It's easy. That one! Yes!"
scene ep12_msolo15 with dissolve
my "You haven't even seen the other one."
scene ep12_msolo14 with dissolve
mc "I don't need to see it. This one looks amazing on you."
scene ep12_msolo15 with dissolve
my "You think? It doesn't show well because it's dark in here, but it sparkles more than you'd think in the right light."
scene ep12_msolo16 with dissolve
mc "Don't worry; I can tell. It screams New Year's Eve!"
scene ep12_msolo17 with dissolve
my "I'm happy that you're so enthused, but I'm still going to show you the other one."
scene ep12_msolo18 with dissolve
mc "No need. I won't change my mind."
play sound "sound_effects/clothes.mp3"
scene ep12_msolo19 with dissolve
$ renpy.pause()
scene ep12_msolo20 with dissolve
mc "Oh, fuck... I see what your problem is. That one is super-good too... It's so you!"
scene ep12_msolo21 with dissolve
my "Gah! I thought you wouldn't change your mind."
scene ep12_msolo22 with dissolve
mc "Well, how can I not? It's fancy, but not too fancy."
mc "Your panties show in it, though."
scene ep12_msolo23 with dissolve
my "I'm obviously not going to wear this underwear to the party. And I have some accessories I'd wear too."
scene ep12_msolo24 with dissolve
mc "The fit is great, and you're beautiful in it."
scene ep12_msolo23 with dissolve
my "Then you get my problem. I like them both."
scene ep12_msolo24 with dissolve
mc "Then maybe you should-"
scene ep12_msolo25 with dissolve
my "I'm not wearing both!"
scene ep12_msolo26 with dissolve
mc "Hahaha!"
mc "Which one are you leaning toward?"
scene ep12_msolo27 with dissolve
my "I think this one..."
my "But I always wanted to wear something as sexy as the other one."
play sound "sound_effects/clothes.mp3"
scene ep12_msolo28 with dissolve
my "I'm scared I'm playing it safe wearing the burgundy dress. Because, as you said, the dress is me."
scene ep12_msolo29 with dissolve
menu:
    "Wear the golden dress":
        scene ep12_msolo30 with dissolve
        $ maya_shiny_dress = True
        mc "If that's how you feel, I think you should try something new."
        mc "Yes, that dress is you. But the other one looked so good on you."
        scene ep12_msolo31 with dissolve
        mc "And if you dreamt of wearing something like it, there's no better party for it than New Year's Eve."
        scene ep12_msolo33 with dissolve
        my "You're right! I'll be daring for once... The golden dress it is!"
    "Wear the burgundy dress":
        $ maya_shiny_dress = False
        scene ep12_msolo30 with dissolve
        mc "Grammatically incorrect as it is, I think your top says it all. Be yourself."
        mc "You should wear what you feel comfortable in. Yes, the golden dress is sexy, but the other one is too."
        scene ep12_msolo31 with dissolve
        mc "You look more mature in it, and it is stunning."
        scene ep12_msolo33 with dissolve
        my "You're right! I don't want to risk spending an evening feeling uncomfortable in the golden dress."
        my "I should listen to my gut feeling and go with the burgundy one."
my "Thank you so much for the help."
scene ep12_msolo31 with dissolve
mc "Does that mean I can borrow the other dress?"
scene ep12_msolo32 with dissolve
my "Pff! Someone is in a jokey mood today."
scene ep12_msolo34 with dissolve
mc "I guess I'm happy to be back. It has started to feel like home here."
scene ep12_msolo35 with dissolve
my "I know what you mean. But I thought you'd stay for longer at your dad's."
scene ep12_msolo34 with dissolve
if ep11_fighter:
    mc "I would have, but there's the party, and I'm having that fighting competition the day after tomorrow."
    mc "You can still come, right?"
    scene ep12_msolo35 with dissolve
    my "I wouldn't miss it. I'll come watch together with Sage and Josy."
    scene ep12_msolo34 with dissolve
    mc "It's scary having you there to watch me fight, but I feel good knowing I have some people cheering me on."
    scene ep12_msolo36 with dissolve
    my "Haha! Oh, you'll hear me! I'll scream as loudly as I can for you."
elif ep11_music:
    mc "I would have, but there's the party, and I'm performing at the faculty party the day after tomorrow."
    mc "So, I need to practice some more for it."
    scene ep12_msolo35 with dissolve
    my "And here I am stealing your free night."
    scene ep12_msolo37 with dissolve
    if tc < 5 or persistent.no_cheater:
        mc "You're worth it."
    else:
        mc "This, right here, makes it worth it."
else:
    mc "I would have, but there are the party preparations and all. Also, it's nice to have some peace and quiet before classes start again."
    scene ep12_msolo35 with dissolve
    my "Yeah, those are the reasons why I'm back too."
scene ep12_msolo38 with dissolve
mc "I'm gonna let you in on something personal if you don't mind..."
scene ep12_msolo39 with dissolve
my "I'd never mind that."
scene ep12_msolo38 with dissolve
mc "I've read Mom's diary over these last few months, and I reached a point in it that...um..."
mc "It didn't shine a good light on Dad."
scene ep12_msolo40 with dissolve
mc "He and Mom got together while he was hired to work for her dad, and he overstepped some boundaries..."
mc "He hooked up with Mom in her room and plenty of times during work."
scene ep12_msolo41 with dissolve
mc "When my grandpa found out about it, Dad beat him."
scene ep12_msolo43 with dissolve
my "What?"
scene ep12_msolo41 with dissolve
mc "It was because he got fired for what he did to Mom. But still... It's something Dad never told me."
mc "I've been in fights too, and I know what it feels like... But I have never hit an adult like that."
scene ep12_msolo42 with dissolve
mc "Maybe it's hypocritical of me to feel this way, but it didn't sit right with me."
scene ep12_msolo43 with dissolve
my "Did you ask Neil about it?"
scene ep12_msolo41 with dissolve
mc "I did. He said he wasn't proud of what he did, and that he ended up getting sued for it, too."
mc "He also told me he gave me Mom's diary so I could see his story from her point of view."
mc "And that he did it because he was scared to tell me the harsh reality he's protected me from..."
scene ep12_msolo42 with dissolve
mc "That made me scared to read further..."
mc "Because to me, you know... Dad is the most amazing person I know."
mc "And I'd hate it if this diary told me otherwise."
scene ep12_msolo41 with dissolve
mc "Do you think I'm overreacting?"
scene ep12_msolo44 with dissolve
my "If I got it right, your dad wants to tell you things, but he doesn't feel like he can."
my "And now that you know what those things are, you're questioning if you want to hear the full story."
scene ep12_msolo41 with dissolve
mc "Yeah... My family is just Dad, you know?"
scene ep12_msolo44 with dissolve
my "You're not in touch with your grandparents at all, right?"
scene ep12_msolo41 with dissolve
mc "No. I've never even met my grandpa. I don't even know what he looks like."
mc "And there's no one to meet on my Dad's side, so... It's just us."
scene ep12_msolo45 with dissolve
my "Then I get why you feel protective of Neil. By not reading further, he'd stay the same to you."
scene ep12_msolo42 with dissolve
mc "Exactly."
scene ep12_msolo44 with dissolve
my "But I can't help but wonder what it is he couldn't tell you."
scene ep12_msolo41 with dissolve
mc "It was about the fight and the lawsuit."
scene ep12_msolo43 with dissolve
my "Are you sure?"
scene ep12_msolo41 with dissolve
mc "No. But I don't want to know more..."
scene ep12_msolo45 with dissolve
my "If you already made up your mind about it, go with that instinct."
scene ep12_msolo40 with dissolve
mc "But it hasn't been all bad, though... I've gotten to know Mom more. I've enjoyed that."
scene ep12_msolo45 with dissolve
my "It sounds to me like you need to think about this some more. And the good thing about that is that there's nothing that stops you."
my "If you ever want to continue reading, you can always pick up from where you left off."
scene ep12_msolo44 with dissolve
my "Patrick hasn't always been the best Dad to me, but I think that our last talk about his feelings helped our relationship a lot."
my "Maybe you'll be surprised how your relationship with Neil can improve further. I mean, you're not a kid anymore."
scene ep12_msolo45 with dissolve
my "If he protected you from reality when you were a kid, it makes sense to me."
my "And now that you're older, maybe you can return the favor by understanding why he had to do it."
scene ep12_msolo41 with dissolve
mc "..."
mc "That makes sense. But I don't know..."
mc "The past is the past. And he seemed relieved when I told him how much he mattered to me and that I didn't want the diary to change that."
scene ep12_msolo45 with dissolve
my "I'm sure you'll find a way forward. Thanks for sharing."
scene ep12_msolo46 with dissolve
mc "How was Christmas with Patrick?"
scene ep12_msolo47 with dissolve
my "It went surprisingly well. We got into a discussion, but we didn't fight."
my "Mom wasn't feeling her best, so she had to rest a lot. It left us with ample time to talk in private."
scene ep12_msolo46 with dissolve
mc "What did you guys talk about?"
scene ep12_msolo48 with dissolve
my "Believe it or not, we talked about Josy."
my "After he saw her at Bella's, he wanted to know why we still hung out."
scene ep12_msolo49 with dissolve
my "When he first brought her up, my heart rate increased. Considering Josy was the cause of one of our bigger fights back in high school, I thought it was bound to happen again."
my "But it didn't..."
scene ep12_msolo50 with dissolve
mc "Why was the fight about Josy back then?"
scene ep12_msolo48 with dissolve
my "It happened during my graduation. Josy and I were happy school had ended, and we shared some celebratory hugs and kisses when we thought no one was watching us."
my "But Dad had been looking for me, and he found us together doing that."
scene ep12_msolo53 with dissolve
my "He pulled me away from her and lashed out at me. He was shocked to learn that I was into girls, and he said nasty things to me."
my "Later, he also forced me not to see Josy again. And yeah, you can probably guess the rest."
scene ep12_msolo51 with dissolve
mc "That explains why you worried about it happening again."
scene ep12_msolo53 with dissolve
my "Yeah. I went into defensive mode when he brought her up. But there was no need for it."
scene ep12_msolo52 with dissolve
my "..."
scene ep12_msolo53 with dissolve
my "I don't know what's happened to him. I don't think he has come around on my sexuality, but..."
my "Maybe there's something inside him that finally clicked."
scene ep12_msolo54 with dissolve
if not ep10_got_contracts:
    my "Still, I didn't dare tell him that we're in a relationship."
else:
    my "After Dad brought Josy up... I was so close to telling him the truth about her, but I chose not to."
my "I prefer Dad like he was this Christmas."
my "It reminded me of the good old days, when we grew up."
scene ep12_msolo51 with dissolve
if not ep10_got_contracts:
    mc "So, you're not going to tell him?"
else:
    mc "So, you think you won't tell him?"
scene ep12_msolo53 with dissolve
if not ep10_got_contracts:
    my "In a perfect world, I could tell him the truth about Josy."
    my "But the world is not perfect, and neither is anyone in it."
else:
    my "There's more to it than just telling him about her. I didn't want to ruin the nice moment we had with it."
scene ep12_msolo51 with dissolve
mc "I get it..."
scene ep12_msolo63 with dissolve
mc "*{i}Groans{/i}*"
my "What?"
scene ep12_msolo65 with dissolve
mc "Your laundry basket..."
scene ep12_msolo53 with dissolve
my "What about it?"
scene ep12_msolo55 with dissolve
mc "I...uh...may recently have remembered the full extent of that night."
scene ep12_msolo56 with dissolve
my "What night? Oh!"
scene ep12_msolo57 with dissolve
mc "Can I say how sorry I am for any permanent damage I may have caused?"
scene ep12_msolo58 with dissolve
my "Haha! You may. Frankly, I hoped you wouldn't remember what you did."
my "I had almost forgotten about it. And it's taken a lot out of me to do so."
scene ep12_msolo57 with dissolve
mc "It was the alcohol."
scene ep12_msolo58 with dissolve
my "No shit! I know you wouldn't have done that back then if you were sober."
scene ep12_msolo57 with dissolve
mc "You see, we were at the strip club before I came back here."
mc "And I got properly drunk."
scene ep12_msolo59 with dissolve
mc "I think I ordered a lot of shots for Tommy and me, but he told me he couldn't drink them because of his diabetes..."
mc "So, I ended up drinking them on my own."
scene ep12_msolo64 with dissolve
mc "And I don't know why I thought it was funny, but...I...um..."
mc "I danced naked in the stripper cage and got thrown out because of it."
scene ep12_msolo58 with dissolve
my "So, that's why..."
scene ep12_msolo59 with dissolve
mc "Yeah..."
play sound "sound_effects/whoosh_2.mp3"
if ep3_mallHelmet:
    scene ep12_msolo66
else:
    scene ep12_msolo67
mc "YOU JUST GO LIKE THIS, MAYA!"
scene ep12_msolo68 with dissolve
my "[name]... Go to sleep."
if ep3_mallHelmet:
    scene ep12_msolo71 with dissolve
else:
    scene ep12_msolo70 with dissolve
mc "SLEEP? HELL NO!"
scene anim_helicopter_ep12 with dissolve
mc "THIS HELICOPTER IS TAKING OFF! WHUMP-WHUMP-WHUMP!"
scene ep12_msolo60
my "Then you got dizzy from doing the helicopter and puked."
scene ep12_msolo59 with dissolve
mc "Yeah... Sorry about that part."
scene ep12_msolo60 with dissolve
my "You know, it was the first lap dance I ever got."
my "I didn't hate it, but it was super-weird."
scene ep12_msolo58 with dissolve
my "And it was an impressive helicopter. I'll give you that."
if ep3_mallHelmet:
    scene ep12_msolo60 with dissolve
    my "But you missed one thing with your story."
    play sound "sound_effects/whoosh_2.mp3"
    scene ep12_msolo69
    mc "SEE! NOW YOU'RE THE DIK PLEDGE! MAYBE I'LL PLEDGE THE HOTS!"
    scene ep12_msolo59
    mc "I took the helmet off!?"
    scene ep12_msolo53 with dissolve
    my "You did. And you made me wear it."
    if not ep3_BellaLewd:
        scene ep12_msolo61 with dissolve
        mc "Oh no... I broke the rules of Hell Week."
        scene ep12_msolo60 with dissolve
        my "Yup. But that's a secret that will stay with me."
        scene ep12_msolo61 with dissolve
        mc "I'm so disappointed in myself..."
        scene ep12_msolo62 with dissolve
        my "That's the part you're disappointed about? What about the helicopter?"
        scene ep12_msolo59 with dissolve
        mc "That's just shame."
    else:
        scene ep12_msolo59 with dissolve
else:
    scene ep12_msolo59 with dissolve
mc "Anyway... I'm so sorry."
scene ep12_msolo60 with dissolve
my "Do you remember why you slept under the bed too? Because that's the only part I couldn't figure out."
scene ep12_msolo55 with dissolve
mc "I don't remember that part, and I don't think I'll ever will... My head was spinning after the dance."
scene ep12_msolo58 with dissolve
my "Haha! I forgive you. Now, let us both bury that memory deep inside our heads, never to be remembered again."
scene ep12_msolo59 with dissolve
mc "Deal!"
label ep12_maya_lewd_label:
if _in_replay:
    if persistent.name == None:
        $ name = "MC"
    else:
        $ name = persistent.name
    if persistent.mc_maya == None:
        $ mc_maya = name
    else:
        $ mc_maya = persistent.mc_maya
    if persistent.maya == None:
        $ maya = "Maya"
    else:
        $ maya = persistent.maya
    play music "music/ep12/licensed_music/track221.mp3"
    queue music ["music/ep12/licensed_music/track220.mp3","music/ep12/licensed_music/track221.mp3"]
    scene ep12_msolo59 with dissolve
hide screen new_phone_screen
mc "Oh, I brought something with me."
scene ep12_maya_lewd1 with dissolve
my "Haha! Alright, I see where you're going with this."
scene ep12_maya_lewd2 with dissolve
mc "Do you mind?"
scene ep12_maya_lewd3 with dissolve
my "No, no. A promise made must be a promise kept."
my "What else do you want me to wear with this?"
scene ep12_maya_lewd4 with dissolve
mc "What...else?"
scene ep12_maya_lewd5 with dissolve
my "Figures."
scene ep12_maya_lewd4 with dissolve
mc "You don't have to do it now if you don't want to."
scene ep12_maya_lewd6 with dissolve
my "You seem to be in the mood for it, and I think I can get there."
my "But maybe you should have waited a bit before suggesting it. Keeping some space between the helicopter talk and sex would do you good."
scene ep12_maya_lewd7 with dissolve
mc "You're right... It was bad timing."
scene ep12_maya_lewd8 with dissolve
my "You were saying?"
scene ep12_maya_lewd9 with dissolve
$ renpy.pause()
scene ep12_maya_lewd10 with dissolve
mc "Nothing. Nothing at all. Continue."
scene ep12_maya_lewd11 with dissolve
my "There..."
scene ep12_maya_lewd12 with dissolve
my "No, wait..."
play sound "sound_effects/clothes.mp3"
scene ep12_maya_lewd13 with dissolve
my "There."
scene ep12_maya_lewd14 with dissolve
mc "You put a lot of thought into this gift, I can tell."
scene ep12_maya_lewd15 with dissolve
my "Haha! Yes. I sure did."
scene ep12_maya_lewd16 with dissolve
my "That smile..."
scene ep12_maya_lewd17 with dissolve
mc "I can't help it."
scene ep12_maya_lewd16 with dissolve
my "I know how you get."
my "Well, I promised that you could feel it. Go ahead..."
scene anim_maya_legs_ep12 with dissolve
mc "Mmm... It's so smooth."
my "This really turns you on, huh?"
mc "So bad. You never have to think about what to give me for Christmas or my birthday ever again. Just do this every time."
my "Haha! Thanks for the idea."
pause
scene ep12_maya_lewd18 with dissolve
mc "So... Do you wanna?"
scene ep12_maya_lewd19 with dissolve
my "I'm not naked for nothing."
scene ep12_maya_lewd20 with dissolve
my "*{i}Smack{/i}*"
scene ep12_maya_lewd21 with dissolve
mc "*{i}Smack{/i}*"
scene ep12_maya_lewd22 with dissolve
mc "*{i}Smack{/i}*"
my "Mmm..."
scene ep12_maya_lewd23 with dissolve
mc "*{i}Smack{/i}*"
my "*{i}Soft moan{/i}*"
scene ep12_maya_lewd24 with dissolve
mc "*{i}Smack{/i}*"
scene ep12_maya_lewd25 with dissolve
my "Oh, fuck... [mc_maya]..."
label ep12_maya_lewd_loop1_label:
menu:
    "Lick her pussy":
        scene anim_maya_lick_ep12 with dissolve
        my "*{i}Moans{/i}* Yes... You're so good with your tongue, [mc_maya]."
        pause
        jump ep12_maya_lewd_loop1_label
    "Finger her pussy":
        scene anim_maya_finger_ep12 with dissolve
        my "Mmm... You're making me want your dick now..."
        mc "That's good."
        my "I want to please you before I get it though."
        pause
        jump ep12_maya_lewd_loop1_label
    "Eat her ass":
        scene anim_maya_ass_ep12 with dissolve
        my "Mmm... I can see where this is going..."
        mc "*{i}Lick lick{/i}* Do you mind?"
        my "Nuh-uh... It was great last time."
        pause
        jump ep12_maya_lewd_loop1_label
    "Continue":
        scene ep12_maya_lewd26 with dissolve
        my "Hey, why am I the only one naked?"
play sound "sound_effects/clothes.mp3"
scene ep12_maya_lewd27 with dissolve
mc "Happy?"
scene ep12_maya_lewd28 with dissolve
my "Mhm..."
label ep12_maya_lewd_loop2_label:
menu:
    "Blowjob":
        scene anim_maya_bj1_ep12 with dissolve
        my "*{i}Suck suck suck{/i}*"
        pause
        scene anim_maya_bj2_ep12 with dissolve
        mc "Yes... Suck it, [maya]."
        my "*{i}Suck glug{/i}*"
        pause
        jump ep12_maya_lewd_loop2_label
    "Footjob":
        scene anim_maya_fj1_ep12 with dissolve
        my "Haha... How do the stockings feel against your dick, [mc_maya]?"
        pause
        scene anim_maya_fj2_ep12 with dissolve
        mc "It feels like I'm in heaven."
        pause
        jump ep12_maya_lewd_loop2_label
    "Assjob":
        scene anim_maya_assjob_ep12 with dissolve
        my "Here's a little taste of what's to come..."
        pause
        scene anim_maya_assjob2_ep12 with dissolve
        mc "Oh, fuck... I'm ready for it, [maya]. I'm so ready."
        my "Yeah? Do you want to fuck me?"
        pause
        jump ep12_maya_lewd_loop2_label
    "Continue":
        my "I want you, [mc_maya]..."

$ tmpInt = 0
$ tmpBool = False
label ep12_maya_lewd_loop_label:
menu:
    "Missionary":
        $ tmpInt += 1
        scene anim_maya_miss1_ep12 with dissolve
        my "*{i}Moans{/i}* Yes! Fuck me, [mc_maya]."
        pause
        scene anim_maya_miss2_ep12 with dissolve
        my "Give me your cock. Penetrate me hard."
        pause
        scene anim_maya_miss3_ep12 with dissolve
        my "You're so hot, [mc_maya]..."
        pause
        jump ep12_maya_lewd_loop_label
    "Cowgirl":
        $ tmpInt += 1
        scene anim_maya_ride1_ep12 with dissolve
        mc "Ahh... That feels so nice."
        my "I love riding your cock."
        pause
        scene anim_maya_ride2_ep12 with dissolve
        mc "You're so good at it."
        my "Well, that's thanks to you and the practice we've had together."
        mc "I think we should train your riding skills even harder."
        my "Haha, I wouldn't mind that. *{i}Moans{/i}*"
        pause
        jump ep12_maya_lewd_loop_label
    "Reverse cowgirl":
        $ tmpInt += 1
        scene anim_maya_rev1_ep12 with dissolve
        my "Yeah, that's right... *{i}Moans{/i}* Just sit there and let me do the work."
        my "I'll get that cum shooting out of you in no time."
        pause
        scene anim_maya_rev2_ep12 with dissolve
        mc "If I keep looking at your hot ass, you will. You're so unbelievably hot, [maya]."
        pause
        jump ep12_maya_lewd_loop_label
    "Lifting":
        $ tmpInt += 1
        scene anim_maya_lift1_ep12 with dissolve
        my "Hngn... Yes... Do it like that."
        my "I'm not too heavy, right?"
        mc "You're light as a feather, [maya]. Relax and enjoy yourself. Let me worry about the rest."
        pause
        scene anim_maya_lift2_ep12 with dissolve
        my "*{i}Moans{/i}* I am relaxed..."
        if not tmpBool:
            my "In fact, I... I think... I think I'm..."
            $ tmpBool = True
            scene ep12_maya_lewd29 with vpunch
            my "Ahhh!"
            scene ep12_maya_lewd30 with vpunch
            my "*{i}Moans{/i}*"
            scene ep12_maya_lewd31 with vpunch
            my "Fuck!!! Ahhh... I'm cumming, [mc_maya]!"
            scene ep12_maya_lewd32 with dissolve
            mc "Wow, you came from that? I wasn't even going fast."
            scene ep12_maya_lewd31 with dissolve
            my "*{i}Phew{/i}* Yeah... It was the slow part that did it for me."
            my "You rarely need to go fast to make a girl cum, you know? You just gotta hit the right spot and keep at it."
            scene ep12_maya_lewd32 with dissolve
            mc "That's good to know."
            scene ep12_maya_lewd31 with dissolve
            my "I bet you could cum from slow sex too."
        else:
            pause
        jump ep12_maya_lewd_loop_label
    "Doggystyle (Anal)":
        $ tmpInt += 1
        scene anim_maya_doggy1_anal_ep12 with dissolve
        my "Ahh... You're fucking me so good, [mc_maya]."
        pause
        scene anim_maya_doggy2_anal_ep12 with dissolve
        my "I can't wait for you to cum for me."
        pause
        jump ep12_maya_lewd_loop_label
    "Cowgirl (Anal)":
        $ tmpInt += 1
        scene anim_maya_ride1_anal_ep12 with dissolve
        my "*{i}Moans{/i}* Do you like it when I go like this?"
        mc "Fuck yes, I do."
        pause
        scene anim_maya_ride2_anal_ep12 with dissolve
        mc "Damn... You're going pretty fast there."
        my "Yeah... I think I've gotten a hang of it."
        mc "You don't say... Fuck... Mmm..."
        pause
        jump ep12_maya_lewd_loop_label
    "Missionary (Anal)":
        $ tmpInt += 1
        scene anim_maya_miss1_anal_ep12 with dissolve
        my "Yes... Fuck it, [mc_maya]."
        my "Fuck my ass!"
        pause
        scene anim_maya_miss2_anal_ep12 with dissolve
        my "*{i}Moans{/i}* Yes... Like that."
        pause
        jump ep12_maya_lewd_loop_label
    "Cum" if tmpInt > 2:
        mc "[maya]... I'm gonna cum."
        menu:
            "Creampie":
                scene anim_maya_lift1_ep12 with dissolve
                my "Cum for me, [mc_maya]!"
                scene ep12_maya_lewd29 at vpunch, cum1
                $ renpy.pause(0.5)
                scene ep12_maya_lewd29 at vpunch, cum1
                $ renpy.pause(0.5)
                scene ep12_maya_lewd33 at vpunch, cum1
                $ renpy.pause()
                scene ep12_maya_lewd34 with dissolve
                $ renpy.pause()
            "On pussy":
                scene anim_maya_miss1_ep12 with dissolve
                my "Cum for me, [mc_maya]!"
                scene ep12_maya_lewd35 at vpunch, cum2
                $ renpy.pause(0.5)
                scene ep12_maya_lewd35 at vpunch, cum2
                $ renpy.pause(0.5)
                scene ep12_maya_lewd35 at vpunch, cum2
                $ renpy.pause()
                scene ep12_maya_lewd36 with dissolve
                $ renpy.pause()
            "On ass (Anal)":
                scene anim_maya_doggy2_anal_ep12 with dissolve
                my "Cum for me, [mc_maya]!"
                scene ep12_maya_lewd37 at vpunch, cum2
                $ renpy.pause(0.5)
                scene ep12_maya_lewd37 at vpunch, cum2
                $ renpy.pause(0.5)
                scene ep12_maya_lewd37 at vpunch, cum2
                $ renpy.pause()
                scene ep12_maya_lewd38 with dissolve
                $ renpy.pause()
            "Creampie (Anal)":
                scene anim_maya_miss2_anal_ep12 with dissolve
                my "Cum for me, [mc_maya]!"
                scene ep12_maya_lewd39 at vpunch, cum1
                $ renpy.pause(0.5)
                scene ep12_maya_lewd39 at vpunch, cum1
                $ renpy.pause(0.5)
                scene ep12_maya_lewd39 at vpunch, cum1
                $ renpy.pause()
                scene ep12_maya_lewd40 with dissolve
                $ renpy.pause()
            "Facial":
                scene anim_maya_bj2_ep12 with dissolve
                my "Cum for me, [mc_maya]!"
                scene ep12_maya_lewd41 at vpunch, cum3
                $ renpy.pause(0.5)
                scene ep12_maya_lewd41 at vpunch, cum3
                $ renpy.pause(0.5)
                scene ep12_maya_lewd41 at vpunch, cum3
                $ renpy.pause()
                scene ep12_maya_lewd42 with dissolve
                $ renpy.pause()

$ renpy.end_replay()
$ persistent.ep12_lewd_maya = True
$ calcScenes()
$ mphone_stats_add_girl_s3("maya","You had sex with Maya in her dorm in episode 12.")

if not persistent.ep12_card17 or not persistent.ep12_card18:
    if not persistent.ep12_card17:
        $ persistent.ep12_card17 = True
        $ persistent.rew_2d_unlocked += 1
        $ persistent.chat_new_rewards = True
        $ calcRenders()
    if not persistent.ep12_card18:
        $ persistent.ep12_card18 = True
        $ persistent.rew_2d_unlocked += 1
        $ persistent.chat_new_rewards = True
        $ calcRenders()
    show screen srmsg
    $ renpy.pause(3)
    hide screen srmsg

scene ep12_maya_lewd43 with dissolve
$ renpy.pause()
scene ep12_maya_lewd44 with dissolve
my "Satisfied?"
scene ep12_maya_lewd45 with dissolve
mc "You're the best..."
scene ep12_maya_lewd44 with dissolve
my "No, you are."
scene ep12_maya_lewd46 with dissolve
mc "Come here..."
scene ep12_maya_lewd48 with dissolve
my "You're not about to do the helicopter again, are you?"
scene ep12_maya_lewd47 with dissolve
mc "Hey! What happened to burying that memory!?"
scene ep12_maya_lewd49 with dissolve
my "HAHAHA! I think it just became a core memory of our relationship now!"
my "WHUMP-WHUMP-WHUMP!"
scene ep12_maya_lewd50 with dissolve
stop music fadeout 3
mc "RAWR!"
my "HAHAHA!"
$ mgallery_add_photo("ep12_maya_solo_pic1")
$ mgallery_add_photo("ep12_maya_solo_pic2")
$ mgallery_add_photo("ep12_maya_solo_pic3")
$ new_bio("Maya", "I spent some time alone with Maya in her dorm. We joked around, shared personal stories and were intimate.")
jump ep12_zbret_label

# Decompiled by unrpyc {v1.3.2}: https://github.com/CensoredUsername/unrpyc dev-branch
