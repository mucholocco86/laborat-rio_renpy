label ep11_jmc_label:
scene ep11_jmc1 with dissolve
js "Good morning, [name]."
scene ep11_jmc2 with dissolve
my "Whoa... If you were a cartoon, a dark cloud would be above your head."
scene ep11_jmc3 with dissolve
mc "Good morning..."
scene ep11_jmc4 with dissolve
js "I get it... You need coffee! We're on our way to get some. You should tag along."
scene ep11_jmc3 with dissolve
mc "No, I'm good."
scene ep11_jmc5 with dissolve
js "How was your weekend?"
scene ep11_jmc3 with dissolve
mc "It was...ok. Wait, it wasn't ok. It was pretty bad."
mc "The DIKs had a huge fight yesterday."
scene ep11_jmc7 with dissolve
my "Oh? What happened?"
scene ep11_jmc8 with dissolve
mc "I don't feel like talking about it. Maybe later."
scene ep11_jmc5 with dissolve
js "That sucks. But at least you got to see your dad, right?"
scene ep11_jmc6 with dissolve
mc "Yeah...about that. It wasn't the best either."
mc "*{i}Sigh{/i}*"
scene ep11_jmc3 with dissolve
mc "I told him about you girls and us. But I felt like he didn't understand what we were doing together."
mc "He said it doesn't sound like a relationship and that I will end up hurting you because there are two of you."
scene ep11_jmc7 with dissolve
my "Did you explain it well enough for him to understand?"
scene ep11_jmc8 with dissolve
mc "I tried to, but Dad was skeptical about it."
mc "He said that women do not always tell guys how they feel or that they lie or pretend about it."
mc "He questioned whether our feelings were mutual or not."
scene ep11_jmc3 with dissolve
mc "Before telling him about us, I would never have guessed he'd react that way."
mc "I thought he would be happy and supportive, but he was confused and worried about me hurting you two."
mc "It bummed me out."
scene ep11_jmc7 with dissolve
my "Well... I know how that feels."
my "I want to say I am surprised, too, but I'm not."
scene ep11_jmc9 with dissolve
my "At times, we don't even understand what this is ourselves. How can we expect our parents to understand?"
scene ep11_jmc10 with dissolve
mc "Yeah, but I was excited about telling him about us. I wanted to bring you two back home with me and meet him."
mc "Now I feel like I can't do that at all. It feels like it's ruined."
if ep9_prep_truce:
    scene ep11_jmc11 with dissolve
else:
    scene ep11_jmc11b with dissolve
js "..."
scene ep11_jmc12 with dissolve
js "I couldn't bring both of you back home either."
js "Not without having to lie about us."
js "I get why you feel it's ruined."
scene ep11_jmc13 with dissolve
mc "Yeah... Is this what it will have to be for us?"
mc "Will our parents never understand us?"
scene ep11_jmc7 with dissolve
my "Maybe your dad will come around? It was a big shock to him."
scene ep11_jmc3 with dissolve
mc "Sorry for bumming you out with this. I'm feeling low today..."
scene ep11_jmc5 with dissolve
js "Can we do something?"
scene ep11_jmc3 with dissolve
mc "No, thanks. There's nothing you can do. I need some time and space to sulk for a while."
scene ep11_jmc14 with dissolve
my "Poor [name]..."
scene ep11_jmc15 with dissolve
js "I know. He speaks so fondly about his dad all the time. This must have hurt him a lot."
$ new_bio("Maya", "I told Josy and Maya about how Dad reacted to hearing about our relationship. Maya wasn't surprised.")
$ new_bio("Josy", "I told Josy and Maya about how Dad reacted to hearing about our relationship. Josy was understanding.")

if branchAlone and ep10_rolling:
    jump ep11_lily_campus_label
if branchAlone and ep8_quinn_lewd:
    jump ep11_quinn_campus_label

jump ep11_jade_campus_label

label ep11_jsolo_label:
$ ep11_josy_solo = True
$ ep11_maya_solo = False
play music "music/ep11/licensed_music/track187.mp3"
queue music ["music/ep11/licensed_music/track189.mp3","music/ep11/licensed_music/track187.mp3"]
scene ep11_jsolo1 with wipeleft
$ renpy.pause()
scene ep11_jsolo2 with dissolve
$ renpy.pause()
scene ep11_jsolo5b with dissolve
$ renpy.pause()
scene ep11_jsolo5 with dissolve
$ renpy.pause()
scene ep11_jsolo3 with dissolve
js "So? What do you think?"
scene ep11_jsolo4 with dissolve
mc "So, this is what you've been up to?"
scene ep11_jsolo3 with dissolve
js "Mhm..."
scene ep11_jsolo4 with dissolve
mc "I'm relieved."
scene ep11_jsolo3 with dissolve
js "What do you mean?"
scene ep11_jsolo6 with dissolve
mc "I thought you were distancing yourself for some other reason, maybe because you didn't feel good. Like I haven't been feeling like myself either."
scene ep11_jsolo7 with dissolve
js "Honestly, you're not far off with that assumption."
js "That's pretty much how all of this started."
scene ep11_jsolo8 with dissolve
js "I felt down one day and started searching for ways to feel better about myself and things to do."
js "I want to be different...but I feel lost."
scene ep11_jsolo6 with dissolve
mc "Different how?"
scene ep11_jsolo7 with dissolve
js "I'm not sure, but I think this will help me figure it out."
scene ep11_jsolo9 with dissolve
mc "Then I think it's great that you're doing something for yourself."
mc "It's good to have hobbies."
scene ep11_jsolo10 with dissolve
js "It's more than a hobby to me. I want this to be me."
js "Something that makes me stand out. You know, not something basic?"
scene ep11_jsolo11 with dissolve
$ renpy.pause()
scene ep11_jsolo12 with dissolve
mc "This isn't about what that guy said to you, right?"
scene ep11_jsolo13 with dissolve
js "What guy?"
scene ep11_jsolo14 with dissolve
mc "That guy from the Halloween party."
scene ep11_jsolo13 with dissolve
js "No, he's got nothing to do with this."
scene ep11_jsolo14 with dissolve
mc "Are you sure? Because I remember you telling me that he called you that - \"basic\". And I've never heard you refer to yourself as such."
scene ep11_jsolo13 with dissolve
js "Whatever. It's not about him. I mean..."
js "Maybe he set off this whirlpool of emotions I'm feeling, but it's not all about what he said."
scene ep11_jsolo15 with dissolve
js "Many other things in my life are causing me to ask questions."
js "All this is about what I've realized about myself and what I'm trying to say with this blog."
scene ep11_jsolo16 with dissolve
mc "Well, I think the blog is a great idea if you're doing it for the right reasons."
mc "Because if this is about proving a point to someone that doesn't matter, then you're giving them a whole lot of power over you."
scene ep11_jsolo15 with dissolve
js "It is for the right reasons."
js "I feel like all this creativity is bubbling inside me, and I have found an outlet for it."
scene ep11_jsolo17 with dissolve
mc "Ok, I hear you. I wanted to make sure because I care about you."
mc "You bought a lot of clothes, huh?"
scene ep11_jsolo18 with dissolve
js "I dipped into my savings, but it's ok."
scene ep11_jsolo17 with dissolve
mc "What do you do with the clothes after you've taken pictures of them?"
scene ep11_jsolo19 with dissolve
js "I haven't given it much thought yet. At the moment, I guess I'm stockpiling everything..."
js "I'll use some of it again, but far from all of it."
scene ep11_jsolo18 with dissolve
js "I could sell the clothes, but that would make Heather right about what I'm doing here..."
scene ep11_jsolo20 with dissolve
mc "Well... You should sell some of it. I mean... Yikes."
scene ep11_jsolo21 with dissolve
js "What?"
scene ep11_jsolo22 with dissolve
mc "What do you mean by \"what\"? Look at this thing. Why would you buy this?"
scene ep11_jsolo23 with dissolve
js "It's cute, and it made me happy."
scene ep11_jsolo22 with dissolve
mc "Yeah, but you wouldn't use this one."
scene ep11_jsolo24 with dissolve
js "I so would."
scene ep11_jsolo25 with dissolve
mc "I'll say it... It's horrible. I hate it."
scene ep11_jsolo26 with dissolve
js "Stop it! That duck is cute, haha!"
scene ep11_jsolo27 with dissolve
mc "It's a kid's bag."
scene ep11_jsolo28 with dissolve
js "No, it's not. You don't understand fashion."
scene ep11_jsolo29 with dissolve
js "Quack quack!"
scene ep11_jsolo30 with dissolve
mc "Haha, get it away from me."
scene ep11_jsolo31 with dissolve
mc "Who's helping you take all those pictures for your blog?"
scene ep11_jsolo32 with dissolve
js "No one. I've used a tripod for it. But I admit it's limiting what I can shoot. I wish I had someone to take take pictures of me."
scene ep11_jsolo31 with dissolve
mc "What about Maya?"
scene ep11_jsolo33 with dissolve
js "I...uh...haven't included her in this yet. And until today, I hadn't included you either, so..."
scene ep11_jsolo34 with dissolve
mc "She'd probably enjoy it. I bet she also knows what makes a good photo, given how many movies she's watched."
scene ep11_jsolo32 with dissolve
js "What about you? You helped out with the camera during Halloween."
scene ep11_jsolo34 with dissolve
mc "Oh, yeah. I have mad skills pushing a button on a camera that Elena and Jacob set up."
scene ep11_jsolo32 with dissolve
js "But you know how to use a camera. I mean, your phone has one."
scene ep11_jsolo35 with dissolve
mc "I can snap a photo of you, but I'm not looking to become your part-time photographer."
scene ep11_jsolo36 with dissolve
js "Can we do it now?"
scene ep11_jsolo37 with dissolve
mc "We can, but if that's what you're wearing, you're the one who doesn't understand fashion."
scene ep11_jsolo38 with dissolve
js "Says the guy wearing a shirt with a \"Classic American Motorcycles\" print."
mc "I can wear this because I don't claim to understand fashion."
scene ep11_jsolo39 with dissolve
js "Hm... If a girl wore that shirt, it would be a cool casual look. I may have to borrow it."
scene ep11_jsolo40 with dissolve
mc "Great, now I'm wearing girls' clothes."
scene ep11_jsolo41 with dissolve
js "Haha! You're not. And I'm obviously getting changed for the photos."
js "I have a winter outfit I'd love to get some pictures of. We could head outside and do it."
scene ep11_jsolo42 with dissolve
js "I'd do it myself, but bringing the tripod with me and all... It becomes quite a project."
scene ep11_jsolo40 with dissolve
mc "Ok, on one condition."
scene ep11_jsolo41 with dissolve
js "The duck bag stays here."
scene ep11_jsolo40 with dissolve
mc "This is why you're the best; I didn't even have to say it."
scene ep11_jsolo43 with dissolve
js "Hahaha!"
scene ep11_jsolo44
show screen ep10_snow_screen
with wipeleft
js "I thought this was a great spot for some pictures; wouldn't you agree?"
scene ep11_jsolo45 with dissolve
mc "Probably, yeah."
scene ep11_jsolo46 with dissolve
js "Trust me. This place has great potential."
scene ep11_jsolo47 with dissolve
mc "You'll have to tell me what to do. I'd hate to disappoint you after lugging the tripod with us."
scene ep11_jsolo48 with dissolve
js "It's like when I take pictures of myself. I always take way more than I need, then delete most of them."
js "I'd feel elated if we could get one or two good-looking pictures from this."
scene ep11_jsolo47 with dissolve
mc "Go ahead. Where do you want me?"
scene ep11_jsolo49 with dissolve
js "Let's start with the trees as background."
scene ep11_jsolo50 with dissolve
js "You can start shooting whenever you want. That camera can store thousands of photos, so don't be shy."
scene ep11_jsolo51 with dissolve
mc "I'll click away, then."
scene ep11_jsolo52 with dissolve
$ renpy.pause()
scene ep11_jsolo53 with dissolve
$ renpy.pause()
scene ep11_jsolo54 with dissolve
js "What do you think?"
scene ep11_jsolo53 with dissolve
mc "I'm not quite feeling it..."
scene ep11_jsolo55 with dissolve
js "What would make it better?"
$ tmpInt = 0
scene ep11_jsolo56 with dissolve
call screen epi_camera_screen([["Against tree",1200,250,1180,410],["Side shot",400,500,410,440],["Close-up",540,100,550,265]])
if tmpInt == 1:
    $ ep11_josy_pic[0] = 0
    mc "Stand by that tree; I think that would look good in a picture."
    play sound "sound_effects/interlude/camera_shutter.mp3"
    scene ep11_jsolo62 with dissolve
    mc "Yes, that's it. Much better."
    scene ep11_jsolo63 with dissolve
    mc "Beautiful."
elif tmpInt == 2:
    $ ep11_josy_pic[0] = 1
    mc "Turn to the side. Maybe the picture will look better if you're not facing the camera."
    scene ep11_jsolo60 with dissolve
    mc "Relax your arms..."
    play sound "sound_effects/interlude/camera_shutter.mp3"
    scene ep11_jsolo61 with dissolve
    mc "Yes, nice."
    mc "I'm no photographer, but I think we're onto something with this one."
elif tmpInt == 3:
    $ ep11_josy_pic[0] = 2
    mc "If I get close, the photo might come out good."
    scene ep11_jsolo57 with dissolve
    mc "Look into the camera."
    play sound "sound_effects/interlude/camera_shutter.mp3"
    scene ep11_jsolo58 with dissolve
    mc "Yeah, I like this. Your eyes look pretty in it."
    scene ep11_jsolo59 with dissolve
    js "Thanks. Make sure you shoot some of the entire outfit, too."

scene ep11_jsolo64 with dissolve
mc "What next? Hm... Maybe by the lake?"
scene ep11_jsolo65 with dissolve
js "It sounds like you're enjoying it too."
scene ep11_jsolo66 with dissolve
mc "It's not boring."
scene ep11_jsolo65 with dissolve
js "Another way of saying it is \"it's fun\"."
scene ep11_jsolo66 with dissolve
mc "Haha, ok. It's fun. Somewhat."
mc "Come on, I want the lake in the background now."
scene ep11_jsolo67 with dissolve
js "The wooden boards are slippery..."
scene ep11_jsolo68 with dissolve
mc "Don't fall into the water now. That ice doesn't look too sturdy."
scene ep11_jsolo69 with dissolve
js "Whoa!"
mc "Careful!"
scene ep11_jsolo70 with dissolve
js "Haha! I told you it was slippery."
scene ep11_jsolo71 with dissolve
js "I think I'm in position. Do your thing!"
scene ep11_jsolo72 with dissolve
$ tmpInt = 0
call screen epi_camera_screen([["Full-body shot",840,250,790,430],["From behind",1440,100,1420,40],["Close-up",1470,400,1480,560]])
if tmpInt == 1:
    $ ep11_josy_pic[1] = 0
    scene ep11_jsolo73 with dissolve
    mc "I think I'll capture a full-body shot of you."
    scene ep11_jsolo77 with dissolve
    play sound "sound_effects/interlude/camera_shutter.mp3"
    mc "Awesome, I think we got it."
elif tmpInt == 2:
    $ ep11_josy_pic[1] = 1
    scene ep11_jsolo73 with dissolve
    mc "Can you turn around and admire the view?"
    scene ep11_jsolo78 with dissolve
    js "Oh, good thinking!"
    play sound "sound_effects/interlude/camera_shutter.mp3"
    scene ep11_jsolo79 with dissolve
    play sound "sound_effects/interlude/camera_shutter.mp3"
    mc "Beautiful!"
elif tmpInt == 3:
    $ ep11_josy_pic[1] = 2
    scene ep11_jsolo73 with dissolve
    mc "I'm gonna get in close for this one."
    scene ep11_jsolo74 with dissolve
    play sound "sound_effects/interlude/camera_shutter.mp3"
    $ renpy.pause()
    scene ep11_jsolo75 with dissolve
    play sound "sound_effects/interlude/camera_shutter.mp3"
    mc "Maybe one from further away, too..."
    scene ep11_jsolo76 with dissolve
    js "Snap as many as you'd like. I'll pick the ones I like after."

scene ep11_jsolo80 with dissolve
js "Set up the camera on the tripod. I'd love to have a photo of us."
scene ep11_jsolo81 with dissolve
js "Put it on interval mode. That way, we get loads of shots and don't have to run back and forth to it."
mc "I think this is it..."
play sound "sound_effects/interlude/camera_shutter.mp3"
mc "Yeah, it started."
scene ep11_jsolo82 with dissolve
js "Come here."
scene ep11_jsolo83 with dissolve
mc "Are these going on your blog, too?"
scene ep11_jsolo84 with dissolve
js "No."
scene ep11_jsolo83 with dissolve
mc "Why? Am I not pretty enough for it?"
scene ep11_jsolo84 with dissolve
js "You're very pretty, but these are just for us."
scene ep11_jsolo85 with dissolve
$ renpy.pause()
scene ep11_jsolo86 with dissolve
$ renpy.pause()
play sound "sound_effects/interlude/camera_shutter.mp3"
scene ep11_jsolo88 with dissolve
$ renpy.pause()
scene ep11_jsolo89 with dissolve
mc "Do you think that's enough photos?"
if check_jlove():
    scene ep11_jsolo90 with dissolve
    js "Just a few more..."
    scene ep11_jsolo91 with dissolve
    js "*{i}Smack{/i}*"
    scene ep11_jsolo92 with dissolve
    js "*{i}Smack{/i}*"
    scene ep11_jsolo94 with dissolve
    $ renpy.pause()
    scene ep11_jsolo93 with dissolve
    $ renpy.pause()
else:
    scene ep11_jsolo90 with dissolve
    js "It's plenty, for sure."
$ guideSuggestedPage = 176
scene ep11_jsolo95 with dissolve
js "Thank you for helping me with this."
mc "I did have fun."
js "So, you'd do it again?"
scene ep11_jsolo96 with dissolve
mc "I guess \"part-time photographer\" would look good on my resume."
scene ep11_jsolo97 with dissolve
js "Haha, you never know."
play sound "sound_effects/cellphone.mp3"
scene ep11_jsolo98 with dissolve
"*{i}Phone rings{/i}*"
js "Oh... It's Mom... I wonder why she's calling."
scene ep11_jsolo99 with dissolve
mc "You could answer her and find out."
scene ep11_jsolo100 with dissolve
js "Do you want to meet her?"
scene ep11_jsolo99 with dissolve
mc "Hm?"
scene ep11_jsolo100 with dissolve
js "I can start a video chat and introduce you."
js "I know it's hard for us to meet each other's parents, but how about it?"
scene ep11_jsolo99 with dissolve
mc "Um... Sure. You better pick up fast, though."
scene ep11_jsolo101 with dissolve
js "Mom? Hey!"
js "I'm fine. How about you?"
js "Uh-huh. Yeah, I'm outdoors taking some pictures for my blog."
scene ep11_jsolo102 with dissolve
js "No, I haven't told you about it. It's pretty new."
js "Hey, there's someone I'd like you to meet. Can we switch to video?"
scene ep11_jsolo103 with dissolve
js "Can you see us?"
scene ep11_jsolo112 with dissolve
ir "Yes, I can see you fine. Who's your friend?"
scene ep11_jsolo104 with dissolve
js "This is [name]. We have classes together and have known each other since before college."
js "And... He's my boyfriend."
scene ep11_jsolo139 with dissolve
ir "Oh? Are you two in a relationship?"
scene ep11_jsolo138 with dissolve
js "Yes, that's what I meant by \"boyfriend\", haha."
mc "Hi! Iris, was it? It's nice to finally meet you. Well, see you, technically."
scene ep11_jsolo112 with dissolve
ir "Likewise. I would have preferred to meet you in person, but here we are."
scene ep11_jsolo138 with dissolve
js "It's been hard to find time to visit during the semester."
scene ep11_jsolo112 with dissolve
ir "We're not that far away, are we?"
scene ep11_jsolo105 with dissolve
js "Well, that argument goes both ways."
scene ep11_jsolo112 with dissolve
ir "We're both busy, then. How are your studies?"
scene ep11_jsolo142 with dissolve
js "The first semester is almost done. I'm doing ok. We have finals soon, and-"
scene ep11_jsolo143 with dissolve
ir "Jenna. I'm in a meeting. Give me five minutes."
scene ep11_jsolo140 with dissolve
ir "Sorry, sweetheart. What was that?"
scene ep11_jsolo105 with dissolve
js "I said I'm doing ok."
scene ep11_jsolo112 with dissolve
ir "I assume you'll tell me all about it over Christmas."
scene ep11_jsolo138 with dissolve
js "Uh..."
scene ep11_jsolo141 with dissolve
ir "Don't tell me you forgot it's our turn to have you over this year."
scene ep11_jsolo138 with dissolve
js "No, I'll be there."
scene ep11_jsolo112 with dissolve
ir "What did you say about a blog? What's that about?"
scene ep11_jsolo106 with dissolve
js "I've started a blog, and we're taking pictures for it. Fashion photography and such."
scene ep11_jsolo139 with dissolve
ir "Fashion photography? Why haven't you told me?"
scene ep11_jsolo138 with dissolve
js "I would have, but it's pretty new and not primarily about fashion."
scene ep11_jsolo140 with dissolve
ir "I've often told you I would have loved to see you model for us."
ir "I mean, when you were a young teen. When you model as an adult, you need to be taller."
scene ep11_jsolo138 with dissolve

if persistent.mod_wtenabled: 
                        $mod_choices = ["(+Josy)","(-Josy)","(-DIK)","(+DIK)","(+5 Josy)","(-5 Josy)","","","","","","" ]
                        #[mod_gr][mod_choices[0]]
                        #\n{size=-4}[m_c1][mod_choices[1]][m_c2][mod_choices[4]]

menu:
    "She's a great model \n{size=-4}[m_c1][mod_choices[0]]":
        $ RPjosy += 1
        scene ep11_jsolo107 with dissolve
        mc "You're missing out. Your daughter is a great model."
        scene ep11_jsolo140 with dissolve
        ir "Your boyfriend is very cute."
    "That's rude \n{size=-4}[m_c1][mod_choices[1]]":
        $ RPjosy -= 1
        scene ep11_jsolo108 with dissolve
        mc "Wow, that's rude..."
        js "[name], don't..."
        scene ep11_jsolo141 with dissolve
        ir "There's nothing rude about it. It's a fact that Josephine is shorter than your average woman."
        scene ep11_jsolo110 with dissolve
        js "Except that I'm not that short. I'm 5'5."
        scene ep11_jsolo112 with dissolve
        ir "I stand corrected. I should have said shorter than the average model."
        scene ep11_jsolo140 with dissolve
    "Say nothing":
        scene ep11_jsolo109 with dissolve
        mc "..."
        scene ep11_jsolo140 with dissolve
ir "If you're serious about this blog, I take it you've registered it as a business. Because that's where you're going with it, isn't it?"
scene ep11_jsolo138 with dissolve
js "I haven't gotten that far yet. Currently, I'm producing some material for it, writing pieces I think people would like to read, and covering some winter fashion - that's all."
scene ep11_jsolo140 with dissolve
ir "You have to start somewhere, and I'm impressed. I always knew you had it in you."
ir "But don't make bad choices along the way. Register your business and get the bookkeeping up to date as soon as possible."
ir "All the clothes and materials you use are deductible from your income."
scene ep11_jsolo138 with dissolve
js "I know all those things already. But I haven't gotten around to it."
scene ep11_jsolo112 with dissolve
ir "I'd love to hear all about this over Christmas. Listen, I have to go; I have a client meeting."
ir "It was nice to meet you, [name]. Hopefully, we'll get a chance to meet in person soon."
scene ep11_jsolo138 with dissolve
mc "Eh... You too. Bye."
scene ep11_jsolo111 with dissolve
js "Bye, Mom."

scene ep11_jsolo113 with dissolve
js "And that's Mom... What do you think?"
menu:
    "Focus on the positives":
        scene ep11_jsolo114 with dissolve
        mc "She seems to care about you. And I felt that her interest in your blog was genuine."
        scene ep11_jsolo115 with dissolve
        js "Yeah... I guess."
    "Focus on the negatives":
        scene ep11_jsolo114 with dissolve
        mc "She was rather blunt and treated the call like another meeting."
        scene ep11_jsolo115 with dissolve
        js "Yeah, she did..."
scene ep11_jsolo116 with dissolve
js "She's a fashion designer and runs her own company. She designs rather expensive clothes."
js "She's talented at it, but...um... Sometimes, I feel like that's all she does."
scene ep11_jsolo117 with dissolve
mc "Managing a company must be time-consuming."
scene ep11_jsolo116 with dissolve
js "Oh yeah. I'm happy she's successful, but our relationship paid a price due to her work."
js "She means well but tends to forget that I'm her daughter."
scene ep11_jsolo117 with dissolve
mc "At least she wanted to have you over for Christmas."
scene ep11_jsolo116 with dissolve
js "I prefer to be with Dad, but yeah. It's her turn this year."
js "But I'll have a mini-Christmas with Dad too, so it's fine."
scene ep11_jsolo118 with dissolve
js "Hey... You got to meet my mom. Sort of."
scene ep11_jsolo119 with dissolve
mc "I did... That's a nice step forward for us."
scene ep11_jsolo118 with dissolve
js "See? We can meet parents after all."
scene ep11_jsolo120 with dissolve
mc "Maya wasn't here with us... That's the core issue."
mc "Dad wouldn't have had a problem if it was just you with me, either."
scene ep11_jsolo121 with dissolve
$ renpy.pause()
scene ep11_jsolo122 with dissolve
js "Don't take this the wrong way, but I like it when it's just us."
js "I feel like our talks are deeper when we're alone."
scene ep11_jsolo123 with dissolve
js "I mean, about you and me. When we talk about us and such."
scene ep11_jsolo120 with dissolve
$ renpy.pause()
scene ep11_jsolo121 with dissolve
$ renpy.pause()
scene ep11_jsolo123 with dissolve
js "[name]? Do you like me?"
scene ep11_jsolo124 with dissolve
mc "You know that I like you. You know about the crush I've had on you."
scene ep11_jsolo123 with dissolve
js "Has it grown bigger and bigger with time, or is it about the same...?"
scene ep11_jsolo124 with dissolve
if tc > 3:
    jump ep11_j_nolove_label
menu:
    "[m_c1]I love you":
        scene ep11_jsolo126 with dissolve
        mc "It's grown bigger."
        scene ep11_jsolo132 with dissolve
        $ renpy.pause()
        scene ep11_jsolo133 with dissolve
        mc "I'm at the point where I'm confident about what I feel for you."
        scene ep11_jsolo125 with dissolve
        js "You are?"
        scene ep11_jsolo126 with dissolve
        mc "..."
        mc "Josy..."
        scene ep11_jsolo127 with dissolve
        mc "I love you."
        if check_jlove():
            $ ep11_josy_love = 2
            scene ep11_jsolo129 with dissolve
            js "I love you, too."
            scene ep11_jsolo130 with dissolve
            $ renpy.pause()
            scene ep11_jsolo131 with dissolve
            js "I do. I can feel it."
            scene ep11_jsolo134 with dissolve
            $ renpy.pause()
            scene ep11_jsolo135 with dissolve
            $ renpy.pause()
            scene ep11_jsolo136 with dissolve
            $ renpy.pause()
        else:
            $ ep11_josy_love = 1
            scene ep11_jsolo128 with dissolve
            js "Wow... You do?"
            scene ep11_jsolo127 with dissolve
            mc "Yeah, I do."
            scene ep11_jsolo128 with dissolve
            js "I... I'm not sure what to say..."
            scene ep11_jsolo127 with dissolve
            mc "You don't have to be sure. I know you're going through some stuff now."
            mc "If you're unsure about me, don't say it until you are."
    "Don't say it yet":
        label ep11_j_nolove_label:
        $ ep11_josy_love = 0
        mc "It's grown, yeah."
        scene ep11_jsolo125 with dissolve
        js "That's good."
        scene ep11_jsolo126 with dissolve
        mc "And I hope it continues to grow."
stop music fadeout 3
scene ep11_jsolo137 with dissolve
$ renpy.pause()

$ new_bio("Josy", "Josy showed me her blog, and we went outside to snap some pictures for it. I ended up being introduced to her mom, Iris.")
if ep11_josy_love == 2:
    $ new_bio("Josy", "I told Josy I loved her, and she said she loved me, too.")
elif ep11_josy_love == 1:
    $ new_bio("Josy", "I told Josy I loved her, but she didn't say she loved me back.")

if ep11_josy_pic[0] == 0:
    $ mgallery_add_photo("ep11_jsolo62")
    $ mgallery_add_photo("ep11_jsolo63")
elif ep11_josy_pic[0] == 1:
    $ mgallery_add_photo("ep11_jsolo60")
    $ mgallery_add_photo("ep11_jsolo61")
else:
    $ mgallery_add_photo("ep11_jsolo57")
    $ mgallery_add_photo("ep11_jsolo58")
if ep11_josy_pic[1] == 0:
    $ mgallery_add_photo("ep11_jsolo77")
elif ep11_josy_pic[1] == 1:
    $ mgallery_add_photo("ep11_jsolo78")
    $ mgallery_add_photo("ep11_jsolo79")
else:
    $ mgallery_add_photo("ep11_jsolo74")
    $ mgallery_add_photo("ep11_jsolo75")

$ mgallery_add_photo("ep11_jsolo87")

if wt_ep11_maya_josy:
    jump ep11_msolo_label

elif branchIsabella or branchJill:
    show screen new_phone_screen
    jump ep11_trip_label

jump ep11_franz_label

label ep11_msolo_label:
$ guideSuggestedPage = 177
play music "music/ep11/licensed_music/track188.mp3"
$ ep11_josy_solo = False
$ ep11_maya_solo = True
scene ep11_msolo1
show screen ep10_snow_screen
with wipeleft
$ renpy.pause()
scene ep11_msolo2
hide screen ep10_snow_screen
with dissolve
mc "Where did you get the idea from?"
scene ep11_msolo3 with dissolve
my "I walked by here the other week and thought that it could be fun for us to try it."
scene ep11_msolo2 with dissolve
mc "It's been years since I skated."
scene ep11_msolo3 with dissolve
my "You've done it before?"
scene ep11_msolo4 with dissolve
mc "A few times during activity days at school, yeah."
mc "I wasn't very good at it."
scene ep11_msolo5 with dissolve
my "It's like riding a bike for me. Whenever I put the skates on, I remember how to do it."
scene ep11_msolo6 with dissolve
mc "So, why didn't Josy come with us?"
scene ep11_msolo7 with dissolve
my "I asked her. I said, \"Let's go rent skates together\"..."
my "...and she was like, \"No... I'm busy\"."
scene ep11_msolo8 with dissolve
my "But she didn't tell me with what. I don't know what's up with that."
my "Is it just me, or has she been withdrawn lately?"
scene ep11_msolo9 with dissolve
mc "She has, yeah."
scene ep11_msolo8 with dissolve
my "Hm..."
scene ep11_msolo10 with dissolve
mc "It's her loss. No bruises or broken bones for her."
scene ep11_msolo11 with dissolve
my "Haha! I like your confidence."
play sound "sound_effects/season3/ice_skate1.mp3"
scene ep11_msolo12
show screen ep10_snow_screen
with dissolve
mc "Whoa..."
scene ep11_msolo13 with dissolve
my "It's not like riding a bike for you, I see."
play sound "sound_effects/season3/ice_skate2.mp3"
scene ep11_msolo14 with dissolve
mc "I'll get there."
scene ep11_msolo15 with dissolve
my "Wanna hold my hand?"
scene ep11_msolo16 with dissolve
$ renpy.pause()
scene ep11_msolo17 with dissolve
$ renpy.pause(10)
show screen click_to_continue_screen with dissolve
$ renpy.pause(2)
hide screen click_to_continue_screen with dissolve
$ renpy.pause()
scene ep11_msolo18 with dissolve
girl "You two are so cute. I wish I had a boyfriend to skate with."
scene ep11_msolo19 with dissolve
my "Haha... Thanks."
scene ep11_msolo20 with dissolve
my "I'm impressed. No bone fractures or bruised skin yet."
scene ep11_msolo21 with dissolve
mc "I'm impressed too! It's a bit shaky here and there, and there were a couple of close calls, but I'm still standing."
mc "When did you learn to skate? Was it also in school?"
scene ep11_msolo22 with dissolve
my "No, but we used to skate after school. And Mom and Dad took us skating, too."
scene ep11_msolo23 with dissolve
mc "Did your mom skate?"
scene ep11_msolo24 with dissolve
my "She did when she was younger. And when we were kids, she put on skates once for us."
my "Mom has always pushed herself through the illness."
my "She shouldn't have stood on skates and let Dad drag her around, but she did it..."
my "...even though she couldn't stand or walk properly."
scene ep11_msolo25 with dissolve
my "She never lost the \"I can do it\" attitude. It always amazed me."
my "If we would wanna ride on a roller coaster, she'd be the first to say \"Let's do it\"."
scene ep11_msolo26 with dissolve
my "Dad had to talk her out of things like that a lot."
my "Her mind wanted to do stuff, but her body wouldn't let her. And she'd possibly hurt more from trying."
scene ep11_msolo27 with dissolve
my "Dad only meant well and tried to protect her, but she got annoyed and mad at him."
my "I think she was mad at her body but took it out on him."
play sound "sound_effects/season3/ice_skate2.mp3"
scene ep11_msolo28 with dissolve
$ renpy.pause()
scene ep11_msolo29
hide screen ep10_snow_screen
with dissolve
mc "Maya? What are you thinking?"
scene ep11_msolo30 with dissolve
my "It's a genetic illness. Mom got it as an adult..."
my "What if I get it too?"
scene ep11_msolo31 with dissolve
mc "Don't think that way."
scene ep11_msolo30 with dissolve
my "I can't help not to."
scene ep11_msolo32 with dissolve
my "Look at my hands. Are they supposed to look like this at my age, or is this an early sign?"
menu:
    "They look like hands":
        mc "They look like hands to me."
        my "Come on. Can't you tell they look different than normal hands?"
    "It's cold outside":
        mc "It's cold outside."
        my "No, they always look like this. And they are sensitive to cold. They stiffen up easily."
scene ep11_msolo33 with dissolve
mc "You're overanalyzing it. Some diseases can skip a generation. Nothing is certain."
scene ep11_msolo34 with dissolve
my "So, I'd be passing it along to my kids?"
scene ep11_msolo33 with dissolve
mc "Maybe it skips two generations? Or maybe you're not even carrying the genes for it."
scene ep11_msolo34 with dissolve

if persistent.mod_wtenabled and tc > 3:
   "scrappy" "You have to many cheater points to progress your relationship with Maya here."

my "Part of me thinks that you should stay away from me."
scene ep11_msolo33 with dissolve
mc "Why's that?"
scene ep11_msolo35 with dissolve
my "I don't want to see you end up like Dad. I don't want to be the reason for that."
if tc > 3:
    jump ep11_m_nolove_label
scene ep11_msolo37 with dissolve
menu:
    "[m_c1]Declare your love":
        scene ep11_msolo39 with dissolve
        mc "It would be amazing if we could choose what our lives would look like."
        mc "To decide to stay healthy and happy until we die. Who wouldn't want that?"
        scene ep11_msolo40 with dissolve
        mc "But you can't decide to be healthy all your life. Even if you eat the right things and exercise plenty, your body may have different plans."
        mc "And to live in fear of that happening to you or someone else... You'd live your entire life in fear because even if you turned out healthy, you'd always ask, \"But what if\"?"
        scene ep11_msolo41 with dissolve
        mc "So that fear isn't going to stop me from being with you."
        mc "And it's way too late for me to stay away from you."
        scene ep11_msolo42 with dissolve
        mc "Because I'm in love with you."
        scene ep11_msolo43 with dissolve
        my "Do you love me?"
        if check_mlove():
            $ ep11_maya_love = 2
            scene ep11_msolo48 with dissolve
            mc "I can feel it... I do."
            scene ep11_msolo49 with dissolve
            my "I..."
            scene ep11_msolo50 with dissolve
            my "I love you too."
            scene ep11_msolo51 with dissolve
            $ renpy.pause()
            scene ep11_msolo52 with dissolve
            $ renpy.pause()
            stop music fadeout 3
            scene ep11_msolo53
            show screen ep10_snow_screen
            with dissolve
            $ renpy.pause()
        else:
            $ ep11_maya_love = 1
            my "You shouldn't."
            scene ep11_msolo44 with dissolve
            mc "But I do."
            mc "I'm not running away."
            scene ep11_msolo45 with dissolve
            my "You say that now, but you never know."
            scene ep11_msolo44 with dissolve
            mc "But I know this. Trust me."
            scene ep11_msolo46 with dissolve
            $ renpy.pause()
            stop music fadeout 3
            scene ep11_msolo47
            show screen ep10_snow_screen
            with dissolve
            $ renpy.pause()
    "Don't do it":
        label ep11_m_nolove_label:
        $ ep11_maya_love = 0
        scene ep11_msolo36 with dissolve
        mc "I'm not running away because of fear of the future."
        scene ep11_msolo35 with dissolve
        my "You say that now, but you never know."
        scene ep11_msolo36 with dissolve
        mc "But I know this. Trust me."
        stop music fadeout 3
        scene ep11_msolo38
        show screen ep10_snow_screen
        with dissolve
        $ renpy.pause()
$ new_bio("Maya", "Maya and I spent some time together ice skating. She told me more about her mom, Helen, and her fears about getting Helen's illness.")
$ mgallery_add_photo("ep11_msolo_pic1")
if ep11_maya_love == 2:
    $ mgallery_add_photo("ep11_msolo_pic2")
    $ new_bio("Maya", "I told Maya I loved her, and she said she loved me, too.")
elif ep11_maya_love == 1:
    $ new_bio("Maya", "I told Maya I loved her, but she didn't say she loved me back.")

if branchIsabella or branchJill:
    show screen new_phone_screen
    jump ep11_trip_label
    
jump ep11_franz_label

label ep11_jm_prelewd_label:
play music "music/ep11/jingle_balls.mp3"
scene ep11_jm_prelewd0 with dissolve
$ renpy.pause()
scene ep11_jm_prelewd1 with dissolve
my "Did you buy all this to cheer him up?"
js "We tried hugs, kisses, and talking about it, but it still seems to be bothering him."
scene ep11_jm_prelewd2 with dissolve
my "Of course, it still bothers him. Those thoughts are in his head, even though Neil apologized."
my "We can't change that with a box of sex toys."
scene ep11_jm_prelewd3 with dissolve
my "And definitely not with...this? What even is this?"
scene ep11_jm_prelewd4 with dissolve
js "I'm not looking to make things magically better, but I still want to try and cheer him up."
js "That's what he'd do for us if we were feeling down."
scene ep11_jm_prelewd5 with dissolve
my "I don't think he would buy toys to cheer us up."
scene ep11_jm_prelewd4 with dissolve
js "I know he wouldn't because it wouldn't work on us. But it might work on him."
scene ep11_jm_prelewd6 with dissolve
my "I know he can be horny, but I don't think this is one of the times when sex will solve it."
scene ep11_jm_prelewd7 with dissolve
js "Again, I'm not looking to solve it. I want to show him we care."
scene ep11_jm_prelewd8 with dissolve
my "And how will a paddle do that?"
scene ep11_jm_prelewd12 with dissolve
js "Before you tell me this was a stupid idea, I can't return them, and I spent like $200."
scene ep11_jm_prelewd9 with dissolve
my "You spent that much on sex toys!?"
scene ep11_jm_prelewd13 with dissolve
js "And these outfits."
scene ep11_jm_prelewd10 with dissolve
my "Remind me why you wanted to save money on Halloween clothes again."
scene ep11_jm_prelewd14 with dissolve
js "I was never going to wear this for Halloween. It's for [name], and I think he's worth it."
js "Can you do this for him together with me? I was already hesitant about buying these, and now I'm starting to feel like this was a bad idea."
scene ep11_jm_prelewd11 with dissolve
my "Ok. I'll play along. I see what you're trying to do."
my "If there is a chance that this will cheer him up, it's worth a try."
scene ep11_jm_prelewd14 with dissolve
js "Thank you."
js "Ok... So, the nipple tape might hurt a tad."
stop music fadeout 3
scene ep11_jm_prelewd15 with dissolve
my "The what now?"

label ep11_jm_lewd_label:
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
$ guideSuggestedPage = 181
play music "music/ep3/dc_love_go_go.mp3"
queue music ["music/ep3/some_obsession.mp3","music/ep3/dc_love_go_go.mp3"]
hide screen new_phone_screen
scene ep11_jm_lewd1 with wipeleft
js "Eyes closed!"
mc "Yeah, they are. But what about the door?"
scene ep11_jm_lewd2 with dissolve
my "I've got it. Remove your clothes, keep your eyes closed, and follow Josy."
scene ep11_jm_lewd3 with dissolve
js "Sit."
scene ep11_jm_lewd4 with dissolve
mc "Is there a chair here?"
scene ep11_jm_lewd3 with dissolve
js "Sit down on it."
scene ep11_jm_lewd5 with dissolve
mc "Can I open my eyes now?"
scene ep11_jm_lewd6 with dissolve
my "Uh-huh. Go ahead."
mc "Great, because I'm dying to know what the dare is..."
scene ep11_jm_lewd7 with dissolve
mc "Fuck me..."
scene ep11_jm_lewd8 with dissolve
js "Our plans exactly."
scene ep11_jm_lewd9 with dissolve
mc "I'm...at a loss for words. What is all this?"
scene ep11_jm_lewd10 with dissolve
js "Just some outfits and toys we got to surprise you with."
scene ep11_jm_lewd11 with dissolve
my "Josy and I talked, and she- {b}we{/b} thought this was a surefire way to cheer you up. And it was our turn to dare you something, so..."
scene ep11_jm_lewd12 with dissolve
mc "Haha, I didn't realize you knew me that well."
mc "But outfits? Toys? Where did you even get all this from?"
scene ep11_jm_lewd13 with dissolve
js "Um... Charity."
scene ep11_jm_lewd14 with dissolve
mc "Charity?"
scene ep11_jm_lewd13 with dissolve
js "It was for a good cause."
scene ep11_jm_lewd14 with dissolve
mc "You lost me."
scene ep11_jm_lewd15 with dissolve
js "Never mind that. Let's have some fun together."
scene ep11_jm_lewd16 with dissolve
mc "Wow... That's a lot of toys."
js "It was a package deal."
scene ep11_jm_lewd17 with dissolve
my "I'm not sure what all that is, but I think we'll have fun. Won't we?"
scene ep11_jm_lewd18 with dissolve
mc "I know I will. Those outfits are turning me on."
scene ep11_jm_lewd19 with dissolve
js "Yeah? What do you like better? Front or back?"
menu:
    "Front":
        scene ep11_jm_lewd21 with dissolve
        mc "There's something about your tits that makes me go crazy for the front."
    "Back":
        scene ep11_jm_lewd22 with dissolve
        mc "Definitely your hot asses. Wow."
    "Both":
        scene ep11_jm_lewd20 with dissolve
        mc "Both sides are equally hot... Damn."
scene ep11_jm_lewd23 with dissolve
mc "So... What's in the box?"
scene ep11_jm_lewd24 with dissolve
my "Haha. What's in the box!? Get it?"
scene ep11_jm_lewd26 with dissolve
js "What?"
scene ep11_jm_lewd25 with dissolve
my "Never mind... What's in the box...?"
scene ep11_jm_lewd27 with dissolve
js "This one is for slapping butts!"
scene ep11_jm_lewd28 with dissolve
mc "Not my butt, I hope."
scene ep11_jm_lewd29 with dissolve
js "Well, the butt plugs are for butts too. How about one?"
scene ep11_jm_lewd30 with dissolve
mc "Funny. I'll pass."
scene ep11_jm_lewd31 with dissolve
mc "Wait... Butt plugs... Lube? Are you saying what I think you are?"
js "They were part of the package, but I don't know. I've never tried one before and thought it could be fun."
scene ep11_jm_lewd32 with dissolve
my "Yeah, I'm not promising anything. But I'll try it if you will."
scene ep11_jm_lewd33 with dissolve
mc "You'll try anal sex?"
scene ep11_jm_lewd34 with dissolve
my "I meant the butt plug thing."
scene ep11_jm_lewd35 with dissolve
js "But it's used to prepare you for anal sex, you know?"
scene ep11_jm_lewd37 with dissolve
my "Are all the toys in there used anally?"
scene ep11_jm_lewd36 with dissolve
js "That one probably isn't."
scene ep11_jm_lewd37 with dissolve
my "Probably... Great."
scene ep11_jm_lewd36 with dissolve
js "No...wait. Yeah, it is."
js "We should have talked more about the dare before we brought him here...shouldn't we?"
scene ep11_jm_lewd38 with dissolve
js "You know how the vibrator works, though."
scene ep11_jm_lewd39 with dissolve
my "Uh-huh. And this? It's not a butt ball, right?"
js "Haha! No! That one goes in your mouth to keep you quiet."
scene ep11_jm_lewd40 with dissolve
my "Haha, I'm gonna put it in yours."
play sound "sound_effects/slap.mp3"
scene ep11_jm_lewd41 with hpunch
js "Ow!!!"
scene ep11_jm_lewd42 with dissolve
mc "Paddle works!"
scene ep11_jm_lewd43 with dissolve
js "And hurts! Damn!"
scene ep11_jm_lewd44 with dissolve
mc "It was because you weren't prepared for it. Let me try it again."
scene ep11_jm_lewd45 with dissolve
my "Wait... When did you remove your clothes?"
scene ep11_jm_lewd46 with dissolve
mc "About the time you said anal."
play sound "sound_effects/slap.mp3"
scene ep11_jm_lewd47 with hpunch
js "Ow! Fuck! NO! Still hurts when you're prepared!"
scene ep11_jm_lewd48 with dissolve
my "And you don't think these will?"
scene ep11_jm_lewd49 with dissolve
js "Not with lube."
scene ep11_jm_lewd48 with dissolve
my "Right... Ok. Show me how you do it then."
scene ep11_jm_lewd49 with dissolve
js "Hold on. Not yet. We have to remove our panties first."
scene ep11_jm_lewd50 with dissolve
mc "Yeah, and I'm not done spanking butts with this. [maya], do you want one?"
scene ep11_jm_lewd51 with dissolve
my "Not if you're gonna spank me hard with it."
scene ep11_jm_lewd50 with dissolve
mc "I mean...it's a spanking. How soft can you go before it just becomes me rubbing you with the paddle?"
scene ep11_jm_lewd52 with dissolve
my "Ok, do what you want with it then."
mc "Yeah, you have been a bad girl, haven't you?"
play sound "sound_effects/slap.mp3"
scene ep11_jm_lewd53 with hpunch
"*{i}SMACK{/i}*"
scene ep11_jm_lewd54 with vpunch
my "*{i}Gasps{/i}* Hngn! Fuck!"
scene ep11_jm_lewd55 with dissolve
my "Whoa... Ok, it wasn't too bad. Josy was exaggerating."
scene ep11_jm_lewd56 with dissolve
js "Was not."
scene ep11_jm_lewd57 with dissolve
mc "Let's see... I didn't even use my right hand for it last time."
play sound "sound_effects/slap.mp3"
scene ep11_jm_lewd58 with hpunch
"*{i}SMACK{/i}*"
scene ep11_jm_lewd59 with vpunch
js "OW!!! Fuck!!!"
my "Hahaha!"
scene ep11_jm_lewd60 with dissolve
js "My asscheek is all red!"
my "Yeah, it is. It looks hot, doesn't it?"
mc "Yeah... Do you want some color on yours, too?"
scene ep11_jm_lewd61 with dissolve
my "Take another look. Mine is even redder than hers."
mc "That's so sexy."
scene ep11_jm_lewd62 with dissolve
$ renpy.pause()
scene ep11_jm_lewd63 with dissolve
mc "Shit... Give me a piece of that ass..."
scene ep11_jm_lewd64 with dissolve
my "You want it, huh?"
mc "Like you wouldn't believe."
scene ep11_jm_lewd65 with dissolve
js "Are you ready for the butt plug?"
scene ep11_jm_lewd66 with dissolve
my "Wait! Am I going first?"
scene ep11_jm_lewd67 with dissolve
js "I think it'll be better to see how it's done before attempting it myself."
scene ep11_jm_lewd66 with dissolve
my "And what makes you think that I have the experience to do it?"
scene ep11_jm_lewd67 with dissolve
js "I don't, but I'll know how to do it if we do you first."
scene ep11_jm_lewd68 with dissolve
my "That sounds like a bogus excuse. Don't forget the lube."
my "And also, if I say stop, you stop."
scene ep11_jm_lewd69 with dissolve
js "Ok, the safe word is...hm...mistletoe!"
scene ep11_jm_lewd70 with dissolve
my "This feels weird already..."
scene bg anim_jm_bp1_ep11 movie with dissolve
my "Hnhnnn... Easy... Easy..."
my "Fuck! Stop! Mistletoe!!!"
pause
scene ep11_jm_lewd71 with dissolve
js "What do you want me to do? It's in there already."
my "It is?"
js "How does it feel?"
scene ep11_jm_lewd72 with dissolve
my "Very unusual."
scene ep11_jm_lewd73 with dissolve
mc "I think it looks hot!"
play sound "sound_effects/slap.mp3"
scene ep11_jm_lewd74 with hpunch
my "Ow!!! Fuck!"
scene ep11_jm_lewd75 with dissolve
my "Haha! Stop it with that paddle."
scene ep11_jm_lewd76fr with dissolve
my "Alright, Ms. Supervisor. You're up!"
scene ep11_jm_lewd77 with dissolve
js "Um... Was yours this big?"
scene ep11_jm_lewd76b with dissolve
my "They were the same size."
scene ep11_jm_lewd77 with dissolve
js "How would you know? This one looks bigger."
scene ep11_jm_lewd78 with dissolve
my "Because I checked before, knowing that you'd give me the bigger one if there were one."
my "They're the same size. Show him your pretty butt already."
scene ep11_jm_lewd79 with dissolve
mc "Yeah... Put that in her."
scene ep11_jm_lewd81 with dissolve
my "I hope this is enough lube. It feels...tight."
scene ep11_jm_lewd80 with dissolve
js "That's because it is tight. Damn you, Arieth! I just wanted to be nice, and now I'm paying for it in more ways than one."
scene bg anim_jm_bp2_ep11 movie with dissolve
my "Look! It's working."
js "Ahhh!!! Mistletoe! Mistletoe!!!"
pause
scene ep11_jm_lewd82 with dissolve
my "Hahaha! Wow, I didn't think you could do that."
scene ep11_jm_lewd83 with dissolve
js "Why the hell did you describe this as unusual? It's unpleasant!"
my "You'll get used to it."
play sound "sound_effects/slap.mp3"
scene ep11_jm_lewd84 with vpunch
js "AHH!! Fuck!"
scene ep11_jm_lewd85 with dissolve
js "[name]! Stop it!"
scene ep11_jm_lewd86 with dissolve
mc "Haha, sorry! I'm having a good time with it."
scene ep11_jm_lewd87 with dissolve
js "Your good time ends now."
scene ep11_jm_lewd88 with dissolve
mc "Why are you cuffing me?"
scene ep11_jm_lewd89 with dissolve
js "I was going to cuff Maya, but after you spanked me so much, I thought this would be better for the sake of my butt."
scene ep11_jm_lewd90 with dissolve
mc "As long as I get to cuff you later, I'm in."
scene ep11_jm_lewd91 with dissolve
mc "So... What are you going to do to me?"
scene ep11_jm_lewd92 with dissolve
js "Haha, wipe that smile off your face. You're cuffed now. We make the rules."
scene ep11_jm_lewd93 with dissolve
my "We do? Like what?"
scene ep11_jm_lewd92 with dissolve
js "First, we're going to show him our asses. And since he can't touch us when he's cuffed, we will make him beg for us to do something."
scene ep11_jm_lewd94 with dissolve
mc "Ok, remove these cuffs."
scene ep11_jm_lewd95 with dissolve
js "Nuh-uh. They will stay on, and you'll have to look at us without touching."
mc "Mistletoe."
js "This isn't an emergency; you can't use that word unless it is."
mc "What's the word for what I wanna do to you then?"
scene ep11_jm_lewd96 with dissolve
js "What do you wanna do?"
mc "I wanna go to town on you girls. You're so sexy..."
my "Nope. There will be no town to go to. You can sit there with your boner and watch us."
scene ep11_jm_lewd97 with dissolve
js "Come here, Maya. Let's tease him for real."
scene anim_jm_kiss_ep11 with dissolve
my "*{i}Smack{/i}*"
js "Mmm..."
mc "Oh... That's so hot, girls. Fuck... I wish that were me."
pause
scene ep11_jm_lewd97 with dissolve
js "What do you say, Maya? Wanna make out some more or let him have something?"
scene ep11_jm_lewd98 with dissolve
my "Hm... I don't know. I love making out with you."
my "I think I wanna make out some more..."
scene ep11_jm_lewd97 with dissolve
js "Let's make out on his cock."
scene anim_jm_kiss2_ep11 with dissolve
my "*{i}Smack{/i}* Yes... An excellent idea."
js "*{i}Lick smack{/i}*"
mc "Fuck... Yes... More tongues..."
pause
scene ep11_jm_lewd99 with dissolve
js "Come here..."
scene anim_jm_scissor_ep11 with dissolve
my "*{i}Moans{/i}* Yes... Rub it like that."
js "Mmm... That's so good. Push against me more... Yes. Hngn..."
pause
scene anim_jm_scissor2_ep11 with dissolve
js "*{i}Moans{/i}* Yes... Yes."
mc "Hey... What about me?"
js "What about you?"
mc "Come on... I'm not just gonna watch, am I?"
js "Hm? Maybe."
pause
scene ep11_jm_lewd100 with dissolve
js "Put your foot up here."
scene anim_jm_mast_ep11 with dissolve
my "Yes... Mmm... A little bit faster. Yes..."
mc "Come on... Give that to me."
my "Quiet. Shut up and watch."
mc "Fuck..."
js "You heard her. Shut up and watch."
js "This is how you take care of her. Watch and learn."
my "Hnnngnn..."
pause
scene ep11_jm_lewd101 with vpunch
my "Ahhh..."
scene ep11_jm_lewd102 with vpunch
my "Yes! Yes!!!"
scene ep11_jm_lewd103 with dissolve
js "All nice and wet... And all [mc_josy] can do is watch..."
scene ep11_jm_lewd104 with dissolve
my "Give him a little taste."
mc "*{i}Suck suck{/i}*"
my "Yes. Lap it up."
scene ep11_jm_lewd105 with dissolve
js "It's hot seeing you like this."
scene ep11_jm_lewd106 with dissolve
my "Just wait until I make you get off. I think I'll use [mc_maya] as the tool for that job."
scene ep11_jm_lewd107 with dissolve
my "Straddle him, but don't put it far in yet. Just the tip."
my "Look at his eyes, Josy. Can you see how much he wants you?"
scene ep11_jm_lewd108 with dissolve
js "He looks horny to me."
my "Yeah, I bet this is killing him."
my "This is what he's been waiting for."
scene ep11_jm_lewd109 with dissolve
my "For your wet pussy to envelop his cock."
my "But this is all he's getting."
scene ep11_jm_lewd110 with dissolve
mc "No, come on... Give me more... Please?"
scene ep11_jm_lewd111 with dissolve
my "Nope. I told you I was using you as a tool."
my "Besides, there are so many toys in this box that I bet Josy wants to try."
scene ep11_jm_lewd112 with dissolve
my "This one shouldn't be a stranger to any of us."
play sound "sound_effects/season2/vibrator.mp3"
scene ep11_jm_lewd113 with hpunch
js "Ahhh... God, that feels good."
play sound "sound_effects/season3/tape.mp3"
scene ep11_jm_lewd114 with dissolve
my "(Hngn... That kinda hurt...)"
scene ep11_jm_lewd115 with dissolve
my "You talk too much. Shut your mouth, Josy."
scene ep11_jm_lewd116 with dissolve
js "*{i}Smack{/i}* Mmmphhh!"
my "There you go."
scene anim_jm_vibrate_ep11 with dissolve
js "*{i}Muffled moans{/i}*"
mc "I can feel those vibrations, too. It's a damn good feeling when I'm inside you."
my "That's the good thing about Josy. She's easy to get off if you know how to do it."
my "A tit in her mouth, a dick in her pussy, and a vibrator going nuts on her clit will have her get off in no time."
js "*{i}Moans{/i}* Ahhhh!!!"
pause
play sound "sound_effects/season2/vibrator.mp3"
scene ep11_jm_lewd117 with vpunch
js "Ahhh! Fuck! Mistletoe! That vibrator! AHHH!!!"
scene ep11_jm_lewd118 with vpunch
js "FUCK! Ahh... Oh my God... That was so...good..."
scene ep11_jm_lewd119 with dissolve
my "See? I told you she'd get off."
my "Does that make you feel horny, [mc_maya]? Watching her cum all over your cock while you want nothing more than to be deeper inside her?"
mc "Yeah, these cuffs are killing me. Is it my turn now?"
play sound "sound_effects/season3/tape.mp3"
scene ep11_jm_lewd120 with dissolve
my "Beg me for it, and maybe I'll give you something."
scene ep11_jm_lewd121 with dissolve
mc "I wanna fuck her... Let me fuck her."
my "I'm not gonna let you fuck her..."
scene bg anim_jm_insert_ep11 movie with dissolve
my "But I'll have her fuck you."
js "*{i}Moans{/i}*"
pause
scene anim_jm_ride1_ep11 with dissolve
my "Is that what you want, [mc_maya]? Her riding your cock like that?"
js "*{i}Moans{/i}* Fuck..."
pause
scene anim_jm_ride2_ep11 with dissolve
js "Hngn... It's extra tight with this thing in my butt."
mc "Yeah, it is."
pause

scene ep11_jm_lewd122 with dissolve
my "Let me try it. But I wanna do it like this..."

scene anim_jm_ride3_ep11 with dissolve
my "*{i}Moans{/i}* Yeah... You weren't kidding. It is tighter."
mc "You feel so good..."
my "So do you."
pause

scene anim_jm_ride4_ep11 with dissolve
mc "Please... Remove the handcuffs... You've teased me enough. I wanna fuck you now."
js "Yeah, I think it's time. Right, Maya?"
my "Hngn... Ok. Remove them."
pause
play sound "sound_effects/season3/tape.mp3"
scene ep11_jm_lewd123 with hpunch
js "*{i}Gasps{/i}*"
scene ep11_jm_lewd124 with dissolve
js "Hey! If that's how you'll do it, I'll put the handcuffs back on."
scene ep11_jm_lewd125 with dissolve
mc "Nah, you won't."
scene anim_jm_bj_ep11 with dissolve
js "*{i}Lick smack{/i}*"
mc "You girls are amazing. You got me so fucking hard."
my "*{i}Lick lick suck{/i}*"
pause
scene anim_jm_bjb_ep11 with dissolve
label ep11_jm_lewd_bj1_label:
pause
menu:
    "Put it in Maya's mouth":
        label ep11_jm_lewd_bj2_label:
        scene anim_jm_bj2_ep11 with dissolve
        js "Do you like how she's doing that?"
        mc "Fuck, yes."
        scene anim_jm_bj2b_ep11 with dissolve
        my "*{i}Suck suck glug{/i}*"
        pause
        menu:
            "Let them share it":
                scene anim_jm_bj_ep11 with dissolve
                jump ep11_jm_lewd_bj1_label
            "Put it in Josy's mouth":
                jump ep11_jm_lewd_bj3_label
            "Continue":
                $ renpy.pause(0.5)
    "Put it in Josy's mouth":
        label ep11_jm_lewd_bj3_label:
        scene anim_jm_bj3_ep11 with dissolve
        js "*{i}Suck suck{/i}* Mmm..."
        my "*{i}Suck suck{/i}*"
        pause
        scene anim_jm_bj3b_ep11 with dissolve
        pause
        menu:
            "Let them share it":
                scene anim_jm_bj_ep11 with dissolve
                jump ep11_jm_lewd_bj1_label
            "Put it in Maya's mouth":
                jump ep11_jm_lewd_bj2_label
            "Continue":
                $ renpy.pause(0.5)
    "Continue":
        $ renpy.pause(0.5)

scene ep11_jm_lewd126 with dissolve
mc "Show me your sexy asses..."
mc "Damn..."
scene ep11_jm_lewd127 with dissolve
js "Are you planning on pulling them out?"
mc "I'm thinking about it, yeah."
my "Do it carefully so it doesn't hurt."
scene bg anim_jm_bp3_ep11 movie with dissolve
js "Hngn... Fuck!"
my "Ahhh..."
pause
scene ep11_jm_lewd128 with dissolve
mc "That's so hot..."
js "I've been thinking... Just because those toys fit, I don't think your cock will."
mc "Can I try?"
scene ep11_jm_lewd129 with dissolve
js "What do you think, Maya?"
my "This is as good a time as any for it. If it doesn't work, it doesn't work."
js "You'll have to go first."
scene ep11_jm_lewd130 with dissolve
mc "I'll take it slow. I've put extra lube on it."
scene ep11_jm_lewd131 with dissolve
mc "Are you ready?"
my "Yes."
scene ep11_jm_lewd132 with dissolve
my "No, wait!"
my "Don't go too fast, ok?"
scene ep11_jm_lewd133 with dissolve
mc "I won't."
scene bg anim_jm_anal_insert_ep11 movie with dissolve
my "Hngn... Slower... Ok... I think it's working. Ahh..."
pause
scene ep11_jm_lewd134 with dissolve
js "You did it? No way!"
my "I think so."
mc "Yeah, you did."
scene ep11_jm_lewd135 with dissolve
my "That toy must have helped a lot. It wasn't as bad as I thought it would be."
scene ep11_jm_lewd136 with dissolve
js "Does it feel good or weird?"
scene ep11_jm_lewd135 with dissolve
my "Pretty weird, but I think you can help me make it feel good if you get what I mean."
scene anim_jm_anal_m1_ep11 with dissolve
js "I got you."
mc "Your ass feels so good, [maya]."
my "Fuck me, [mc_maya]..."
pause
scene anim_jm_anal_m2_ep11 with dissolve
my "Hngnn..."
pause
scene ep11_jm_lewd137 with dissolve
my "*{i}Phew{/i}* Do you think you can do it too?"
scene ep11_jm_lewd138 with dissolve
js "I...uh...don't think so."
scene ep11_jm_lewd139 with dissolve
my "Give it a try. It's not as hard as you'd think."
scene ep11_jm_lewd140 with dissolve
my "Wow, that looks super tight."
mc "Tell me about it... How did she even get the toy in?"
scene ep11_jm_lewd141 with dissolve
js "Guys... This won't work."
scene ep11_jm_lewd142 with dissolve
js "*{i}Moans{/i}* Hnnghhh!!! Ahh!!!"
scene ep11_jm_lewd143 with dissolve
my "You can't go deeper, right?"
mc "I'm trying to, but it's too tight."
scene anim_jm_anal_j1_ep11 with dissolve
js "[mc_josy]! It's too tight. Ahh..."
mc "Maybe it will get better soon? It kind of works."
js "I don't think it will. It hurts."
pause
scene ep11_jm_lewd144 with dissolve
mc "Damn... I'll stop."
scene ep11_jm_lewd145 with dissolve
my "Hm... What about if we try it with this one first?"
my "It's not as thick as your cock."
scene ep11_jm_lewd146 with dissolve
mc "How do you use that one?"
my "I think I have to put it up my ass..."
mc "Are you up for it?"
scene ep11_jm_lewd147 with dissolve
my "I'm pretty damned horny now."
my "Hngn... Yeah, like that."
scene ep11_jm_lewd148 with dissolve
mc "That looks so weird."
my "It does, doesn't it?"
js "Are you going to put that in me?"
scene ep11_jm_lewd149 with dissolve
my "Let me try."
scene ep11_jm_lewd150 with dissolve
my "Hey, it works."
js "*{i}Moans{/i}* Ahhh..."
scene ep11_jm_lewd151 with dissolve
mc "That's hot."
scene ep11_jm_lewd152 with dissolve
mc "Here... Take this."
js "Mmpphfff..."
scene anim_jm_anal_j3_ep11 with dissolve
my "You're taking it pretty well now."
js "*{i}Suck suck{/i}* Hngn... *{i}Moans{/i}*"
pause
scene anim_jm_anal_j4_ep11 with dissolve
mc "I never thought I'd be doing this with you."
my "Haha, me neither. She has herself to blame for going nuts when buying these toys."
pause
scene anim_jm_anal_j2_ep11 with dissolve
mc "It looks like she likes it to me."
js "*{i}Moans{/i}*"
pause
scene ep11_jm_lewd153 with dissolve
my "How does it feel?"
js "Hnn... Let me try his cock again... But I still doubt he can fit it inside my ass."
my "What if you do it while on top of him? Maybe that will help."
scene ep11_jm_lewd154 with dissolve
js "Guide it inside me."
scene ep11_jm_lewd155 with dissolve
my "I've got it. Focus on pushing down on him."
scene ep11_jm_lewd156 with dissolve
js "Hngn... Fuck... It's still super tight."
mc "More, [josy]... You've got this."
scene bg anim_jm_anal_insert2_ep11 movie with dissolve
js "*{i}Moans{/i}* Ahhh... Is it in yet?"
mc "Almost..."
js "This is as far as I can take it."
my "Hey, it looks good."
scene anim_jm_anal_j5_ep11 with dissolve
js "*{i}Moans{/i}* Hold me while I do this. I don't wanna slip."
my "You're not gonna slip. Go ahead and fuck him."
pause
scene anim_jm_anal_j6_ep11 with dissolve
pause
scene ep11_jm_lewd157 with dissolve
js "I think I've gotten used to this now... *{i}Phew{/i}*"
scene ep11_jm_lewd158 with dissolve
my "Ok, [mc_maya]... We're yours. How do you want us?"
$ tmpInt = 0
$ tmpBool3 = False
label ep11_jm_lewd_loop_label:
menu:
    "Blowjob":
        scene anim_jm_bj_ep11 with dissolve
        label ep11_jm_lewd_bj1b_label:
        pause
        menu:
            "Put it in Maya's mouth":
                label ep11_jm_lewd_bj2b_label:
                scene anim_jm_bj2_ep11 with dissolve
                pause
                scene anim_jm_bj2b_ep11 with dissolve
                my "*{i}Suck suck glug{/i}*"
                pause
                menu:
                    "Put it between them":
                        scene anim_jm_bj_ep11 with dissolve
                        jump ep11_jm_lewd_bj1b_label
                    "Put it in Josy's mouth":
                        jump ep11_jm_lewd_bj3b_label
                    "Continue":
                        jump ep11_jm_lewd_loop_label
            "Put it in Josy's mouth":
                label ep11_jm_lewd_bj3b_label:
                scene anim_jm_bj3_ep11 with dissolve
                js "*{i}Suck suck{/i}* Mmm..."
                my "*{i}Suck suck{/i}*"
                pause
                scene anim_jm_bj3b_ep11 with dissolve
                pause
                menu:
                    "Put it between them":
                        scene anim_jm_bj_ep11 with dissolve
                        jump ep11_jm_lewd_bj1b_label
                    "Put it in Maya's mouth":
                        jump ep11_jm_lewd_bj2b_label
                    "Continue":
                        jump ep11_jm_lewd_loop_label
            "Continue":
                jump ep11_jm_lewd_loop_label
        jump ep11_jm_lewd_loop_label
    "Doggystyle (Maya)":
        $ tmpInt += 1
        scene anim_jm_anal_m1_ep11 with dissolve
        pause
        scene anim_jm_anal_m2_ep11 with dissolve
        pause
        jump ep11_jm_lewd_loop_label
    "Missionary (Josy)":
        $ tmpInt += 1
        if not tmpBool3:
            $ jumpLabel = "ep11_jm_lewd_cont3_label"
            jump ep11_jm_lewd_gag_label
            label ep11_jm_lewd_gag_label:
            $ tmpBool3 = True
            scene ep11_jm_lewd159 with dissolve
            mc "Could you wear this?"
            scene ep11_jm_lewd161 with dissolve
            js "I can't scream the safe word if I do."
            scene ep11_jm_lewd160 with dissolve
            mc "Don't worry, it will be hot. I'm not gonna restrain you."
            scene ep11_jm_lewd161 with dissolve
            js "Ok. I'll give it a shot."
            scene ep11_jm_lewd162 with dissolve
            mc "Yeah... That looks hot."
            scene ep11_jm_lewd163 with dissolve
            $ renpy.jump(jumpLabel)
            label ep11_jm_lewd_cont3_label:

        mc "Get on the bed for me."
        scene anim_jm_anal_miss1_ep11 with dissolve
        pause
        scene anim_jm_anal_miss2_ep11 with dissolve
        pause
        scene bg anim_jm_anal_miss3b_ep11 movie with dissolve
        pause
        jump ep11_jm_lewd_loop_label
    "Prone (Josy)":
        $ tmpInt += 1
        if not tmpBool3:
            $ jumpLabel = "ep11_jm_lewd_cont1_label"
            jump ep11_jm_lewd_gag_label
            label ep11_jm_lewd_cont1_label:

        mc "Get on the bed for me."
        scene anim_jm_anal_prone1_ep11 with dissolve
        mc "I'm gonna push you down like this, ok?"
        js "*{i}Muffled{/i}* Ok..."
        pause
        scene anim_jm_anal_prone2_ep11 with dissolve
        pause
        scene ep11_jm_lewd164 with dissolve
        my "I have an idea..."
        scene ep11_jm_lewd165 with dissolve
        my "Let's see how you like this."
        play sound "sound_effects/season2/vibrator.mp3"
        scene anim_jm_anal_prone3_ep11 with dissolve
        js "Hngn... *{i}Moans{/i}*"
        my "Yeah, you're loving it. Aren't you?"
        js "Hngn... Mmm..."
        pause
        scene anim_jm_anal_prone1_ep11 with dissolve
        my "Do you like it when I increase its speed?"
        play sound "sound_effects/season2/vibrator.mp3"
        js "Hnnnn..."
        pause
        scene ep11_jm_lewd166 with hpunch
        my "[mc_maya], she's cumming!"
        scene ep11_jm_lewd167 with hpunch
        js "Hngnnnn!!!"
        scene ep11_jm_lewd168 with dissolve
        mc "Are you ok?"
        scene ep11_jm_lewd169 with dissolve
        js "[mc_josy]... I came so fucking hard; I didn't know what to do..."
        scene ep11_jm_lewd168 with dissolve
        mc "That's so sexy."
        scene ep11_jm_lewd169 with dissolve
        js "Fuck..."
        jump ep11_jm_lewd_loop_label
    "Standing (Maya)":
        $ tmpInt += 1
        scene anim_jm_anal_stand1_ep11 with dissolve
        pause
        scene anim_jm_anal_stand2_ep11 with dissolve
        pause
        scene anim_jm_anal_stand3_ep11 with dissolve
        pause
        scene anim_jm_anal_stand4_ep11 with dissolve
        pause
        jump ep11_jm_lewd_loop_label
    "Cowgirl (Maya)":
        $ tmpInt += 1
        scene anim_jm_anal_ride1_ep11 with dissolve
        pause
        scene anim_jm_anal_ride2_ep11 with dissolve
        pause
        scene anim_jm_anal_ride3_ep11 with dissolve
        pause
        jump ep11_jm_lewd_loop_label
    "Reverse cowgirl (Josy)":
        $ tmpInt += 1
        if not tmpBool3:
            $ jumpLabel = "ep11_jm_lewd_cont2_label"
            jump ep11_jm_lewd_gag_label
            label ep11_jm_lewd_cont2_label:

        mc "Come here."
        scene anim_jm_anal_rev_ep11 with dissolve
        pause
        scene anim_jm_anal_rev2_ep11 with dissolve
        pause
        jump ep11_jm_lewd_loop_label
    "Cum" if tmpInt > 2 and tmpBool3:
        menu:
            "Facial":
                scene anim_jm_cum3_ep11 with dissolve
                pause
                scene ep11_jm_lewd172 at vpunch, cum2
                $ renpy.pause(0.5)
                scene ep11_jm_lewd172 at vpunch, cum2
                $ renpy.pause(0.5)
                scene ep11_jm_lewd172 at vpunch, cum2
                mc "Fuck!!!"
                scene ep11_jm_lewd173 with dissolve
                $ renpy.pause()
                scene ep11_jm_lewd174 with dissolve
                $ renpy.pause()
                scene ep11_jm_lewd175 with dissolve
                $ renpy.pause()
                scene ep11_jm_lewd176 with dissolve
                $ renpy.pause()
            "Creampie Josy (Anal)":
                scene anim_jm_anal_rev2_ep11 with dissolve
                pause
                scene ep11_jm_lewd170 at vpunch, cum1
                $ renpy.pause(0.5)
                scene ep11_jm_lewd170 at vpunch, cum1
                $ renpy.pause(0.5)
                scene ep11_jm_lewd170 at vpunch, cum1
                mc "Fuck!!!"
                scene bg anim_jm_cum2_ep11 movie with dissolve
                pause
            "Creampie Maya (Anal)":
                scene anim_jm_anal_stand2_ep11 with dissolve
                pause
                scene ep11_jm_lewd171 at vpunch, cum1
                $ renpy.pause(0.5)
                scene ep11_jm_lewd171 at vpunch, cum1
                $ renpy.pause(0.5)
                scene ep11_jm_lewd171 at vpunch, cum1
                mc "Fuck!!!"
                scene bg anim_jm_cum_ep11 movie with dissolve
                pause

stop music fadeout 3
scene ep11_jm_lewd177 with dissolve
$ renpy.pause()
scene ep11_jm_lewd178 with dissolve
play music "music/ep11/silent_night.mp3"
mc "That was...insanely hot."
mc "I can't believe you girls did that for me."
scene ep11_jm_lewd179 with dissolve
js "Technically, you did it for us since it was your dare... But I take it you liked it."
scene ep11_jm_lewd180 with dissolve
mc "I loved it..."
mc "I hope you won't hurt in places after this."
scene ep11_jm_lewd181 with dissolve
my "I'm not gonna lie; I think we will be sore."
scene ep11_jm_lewd183 with dissolve
js "I know I will be."
scene ep11_jm_lewd182 with dissolve
my "It was a fun box you got for us."
scene ep11_jm_lewd179 with dissolve
js "Haha! I'm surprised we put it all to use."
scene ep11_jm_lewd180 with dissolve
mc "Which toy was your favorite?"
scene ep11_jm_lewd184 with dissolve
js "It was hot being cuffed and gagged. It felt scary at first..."
js "But I knew I could trust you two. So, it went from scary to sexy pretty fast."
scene ep11_jm_lewd182 with dissolve
my "You looked so hot with it in your mouth."
scene ep11_jm_lewd184 with dissolve
js "What about you and that outfit?"
scene ep11_jm_lewd185 with dissolve
my "Yeah, I will keep this one around. I feel powerful wearing it."
my "That was the best part of this for me. It was like I stepped into a character."
my "I just went with it, haha!"
scene ep11_jm_lewd186 with dissolve
mc "You were both amazing... It was such a struggle not to cum too fast."
scene ep11_jm_lewd187 with dissolve
js "We're happy that you're happy. That was the point of this."
scene ep11_jm_lewd188 with dissolve
my "Yeah, we wanted to cheer you up."
scene ep11_jm_lewd189 with dissolve
mc "Sorry if I've been a downer lately."
scene ep11_jm_lewd187 with dissolve
if _in_replay or check_jlove():
    js "We get why. But we also wanted to remind you of what makes us great together."
    js "And I'm not talking about what we did tonight."
else:
    js "We get why. Your dad means a lot to you."
scene ep11_jm_lewd189 with dissolve
if _in_replay or check_jlove():
    mc "I know. And that's what I've been sad about."
    mc "I wanted Dad to see that we three are great together, too."
    mc "But if it takes a while for him to see it...so be it."
    mc "Eventually, he will. He has to."
else:
    mc "He'll understand it at some point... He has to."
if _in_replay or (check_mlove() and check_jlove()):
    scene ep11_jm_lewd191 with dissolve
    my "*{i}Smack{/i}*"
    js "*{i}Smack{/i}*"
elif check_mlove():
    scene ep11_jm_lewd190 with dissolve
    my "*{i}Smack{/i}*"
elif check_jlove():
    scene ep11_jm_lewd192 with dissolve
    js "*{i}Smack{/i}*"

scene ep11_jm_lewd193 with dissolve
mc "Are you keeping all these toys?"
js "I doubt I can return them after tonight."
my "This room looks like a warzone with them scattered all over the place."
js "Haha! Sure does."
scene ep11_jm_lewd194 with dissolve
mc "I think I've come up with a new dare."
scene ep11_jm_lewd196 with dissolve
my "Already?"
scene ep11_jm_lewd195 with dissolve
mc "Yep. And you wanted to cheer me up, no?"
js "I can't believe you're taking advantage of that."
mc "Well, I have a good dare in mind. But the question is...for who?"
$ renpy.end_replay()
$ persistent.ep11_lewd_jm = True
$ calcScenes()
$ new_bio("Josy", "Josy and Maya tried to cheer me up by daring me to have anal sex with them. It worked like a charm.")
$ new_bio("Maya", "Josy and Maya tried to cheer me up by daring me to have anal sex with them. It worked like a charm.")
$ mphone_stats_add_girl_s3("maya","You had sex with Josy and Maya in Maya's dorm in episode 11.")
$ mphone_stats_add_girl_s3("josy","You had sex with Josy and Maya in Maya's dorm in episode 11.")

stop music fadeout 3

if persistent.mod_wtenabled: 
                        $mod_choices = ["(Possible Josy points)","(-Josy)","(-DIK)","(+DIK)","(+5 Josy)","(-5 Josy)","","","","","","" ]
                        #[mod_gr][mod_choices[0]]
                        #\n{size=-4}[m_c1][mod_choices[1]][m_c2][mod_choices[4]]

menu:
    "Dare Josy \n{size=-4}[m_c1][mod_choices[0]]":
        $ ep11_josy_dare = True
    "Dare Maya":
        $ ep11_josy_dare = False
if branchSage:
    jump ep11_ssolo_label
show screen new_phone_screen
jump ep11_math_label
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
