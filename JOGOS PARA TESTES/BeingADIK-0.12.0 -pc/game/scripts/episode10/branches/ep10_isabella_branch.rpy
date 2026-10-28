label ep10_isabella_intro_label:
scene ep10_isabella_intro1 with dissolve
mc "..."
scene ep10_isabella_intro2 with dissolve
mc "You should leave. I'll take care of this."
scene ep10_isabella_intro3 with dissolve
mc "Hey, Nick..."
scene ep10_isabella_intro4 with dissolve
ni "Hey. So... What was that about?"
scene ep10_isabella_intro5 with dissolve
menu:
    "It was nothing":
        $ ep10_nick_questions[0] = 0
        mc "It was nothing."
        scene ep10_isabella_intro6 with dissolve
        ni "That kiss didn't look like nothing. And you don't make someone exit from the window without reason."
        scene ep10_isabella_intro5 with dissolve
        mc "Fuck... You weren't supposed to see that."
    "Do you know her?":
        $ ep10_nick_questions[0] = 1
        mc "Do you know who that is?"
        scene ep10_isabella_intro4 with dissolve
        ni "Yeah, of course. She's the librarian. Was she at our party?"
        scene ep10_isabella_intro5 with dissolve
        mc "Yeah... You weren't supposed to see that."
mc "Maybe it's a big thing to ask, but can you keep this a secret?"
mc "It would mean a lot if you did."
scene ep10_isabella_intro6 with dissolve
ni "Sure... Uh... I didn't see anything."
scene ep10_isabella_intro5 with dissolve
mc "Can you promise you won't tell anyone about it?"
scene ep10_isabella_intro6 with dissolve
ni "It's not a problem. Are you with her or something?"
scene ep10_isabella_intro5 with dissolve
menu:
    "Just a friend":
        $ ep10_nick_questions[1] = 0
        mc "She's just a friend."
        scene ep10_isabella_intro4 with dissolve
        ni "A friend who stayed the night in your room?"
        ni "Come on, you don't have to lie to me."
        scene ep10_isabella_intro5 with dissolve
        mc "I don't know what she is. But I want to have the time to figure it out without everyone knowing about it."
        scene ep10_isabella_intro4 with dissolve
        ni "Right."
    "Just sex":
        $ ep10_nick_questions[1] = 1
        mc "It's just sex. There's nothing more to it than that, but I don't want to embarrass her by spreading it."
        scene ep10_isabella_intro6 with dissolve
        ni "I can't believe you're banging the librarian. That's wild."
        scene ep10_isabella_intro5 with dissolve
        mc "Yeah..."
        scene ep10_isabella_intro6 with dissolve
        ni "But given how you and Derek almost completed Hell Week perfectly, I'm not surprised."
    "Kinda":
        $ ep10_nick_questions[1] = 2
        mc "Y-yeah. Kinda... And it's hard to let people in on it because of... Well, you get why."
        scene ep10_isabella_intro6 with dissolve
        ni "Yeah, totally."
        ni "I've actually seen her here before. And I thought it was weird the first time, but it's cool."
        ni "Who am I to judge?"
        scene ep10_isabella_intro5 with dissolve
        mc "*{i}Phew{/i}* Thanks... You have no idea how much I appreciate that."
        mc "Sneaking around isn't my thing, but it's our only option."
        scene ep10_isabella_intro4 with dissolve
        ni "Bringing her here is a risky move. It's not like you live alone."
        scene ep10_isabella_intro5 with dissolve
        mc "Yeah, I might have to rethink some things."

scene ep10_isabella_intro7 with dissolve
ni "I'm gonna head back in there."
scene ep10_isabella_intro5 with dissolve
mc "Thanks again, bro."
hide screen new_phone_screen
$ tmpInt = 0
$ tmpInt2 = 0
$ text_message_screen_list = []
$ text_message_screen_list.append(["%s" % name,"I cleared it up with Nick. He promised he wouldn't tell anyone about us.",False])
$ text_message_screen_list.append(["Isabella","Are you sure you can trust him?",True])
scene ep10_isabella_intro8 with dissolve
show screen text_message_screen
play sound "sound_effects/interlude/zoey_message.mp3"
$ renpy.pause()

$ tmpInt += 1
$ renpy.pause()
menu:
    "Yes":
        $ text_message_screen_list.append(["%s" % name,"Yes. I can trust him. But we should be more careful.",False])
        $ text_message_screen_list.append(["Isabella","Ok. I feel queasy thinking about this, but I have no choice but to let you handle it.",True])
        $ text_message_screen_list.append(["%s" % name,"Drive safely. Talk later.",False])
        $ tmpInt += 1
        $ renpy.pause()
        $ tmpInt += 1
        $ renpy.pause()
        $ tmpInt += 1
        $ renpy.pause()
    "Not sure":
        $ text_message_screen_list.append(["%s" % name,"I feel that I can trust him, but I'm not 100% sure. I will talk to him more about it later to make sure he's still cool with it. We should be more careful.",False])
        $ text_message_screen_list.append(["Isabella","Ok... Do that.",True])
        $ text_message_screen_list.append(["%s" % name,"Drive safely. Talk later.",False])
        $ tmpInt += 1
        $ renpy.pause()
        $ tmpInt += 1
        $ renpy.pause()
        $ tmpInt += 1
        $ renpy.pause()

hide screen text_message_screen
$ mphone_scene_to_chat("Isabella",text_message_screen_list)
$ tmpInt = 0
$ text_message_screen_list = []
scene ep10_isabella_intro9 with dissolve
mc "(Fuck...)"
$ new_bio("Nick", "Nick told me he wouldn't tell anyone about seeing Bella and I kiss.")
jump ep10_dik_intro_label

label ep10_bsolo_label:
$ guideSuggestedPage = 122
play music "music/ep4/optimistic.mp3"
scene ep10_bsolo1 with wipeleft
$ renpy.pause()
scene ep10_bsolo2 with dissolve
$ renpy.pause()
scene ep10_bsolo3 with dissolve
isa "I admit I was skeptical about you studying today, but you proved me wrong."
scene ep10_bsolo4 with dissolve
mc "I take my studies very seriously."
scene ep10_bsolo5 with dissolve
mc "Just kidding. I do what I have to do, but that's about it."
mc "And I have to compensate for sitting next to Derek in class; he tends to distract me."
scene ep10_bsolo6 with dissolve
if ep8_midterms_cheated == "DIK":
    isa "Given what happened during your midterm exam, you should take it seriously."
isa "The attitude you set for yourself in college is the one that you will bring with you into your work life."
scene ep10_bsolo7 with dissolve
mc "Uh-huh. And what attitude did you bring with you?"
scene ep10_bsolo8 with dissolve
isa "Oh, I was ambitious."
scene ep10_bsolo9 with dissolve
mc "Right... Was the OMG motto \"ambition\"?"
scene ep10_bsolo10 with dissolve
isa "Ok, maybe not the first year, but I got there eventually."
scene ep10_bsolo9 with dissolve
mc "Partied too much?"
scene ep10_bsolo10 with dissolve
isa "I refuse to be judged by you."
scene ep10_bsolo13 with dissolve
isa "So... Chemistry, is it?"
if minigames:
    menu:
        "English":
            mc "Some, but now it's mostly your class."
            $ bonusPercentageEnglish += 10
            "+10%% score on your next English test.\nYour total bonus for the next test is [bonusPercentageEnglish]%%."
        "Math":
            mc "Some, but now it's mostly math."
            $ bonusPercentageMath += 10
            "+10%% score on your next Math test.\nYour total bonus for the next test is [bonusPercentageMath]%%."
        "Science":
            mc "Yep. I have lots to learn."
            $ sm_studied += 1
            $ tmpInt = sm_studied*5
            "+5%% time on your next lab experiment.\nYour total bonus time for the next experiment is [tmpInt]%%."
            $ tmpInt = 0
scene ep10_bsolo11 with dissolve
if minigames:
    mc "Did you ever take a chemistry class?"
else:
    mc "Yeah. Did you ever take a chemistry class?"
scene ep10_bsolo12 with dissolve
isa "No, I was awful at science. I found it uninspiring, and I never quite got it."
scene ep10_bsolo11 with dissolve
mc "It's tricky, but I like it. At least, I think I do."
mc "I guess it's pointless to ask you for help with it."
scene ep10_bsolo12 with dissolve
isa "Yes, I fear you'd end up dumber if you did."
isa "I'll be right back. I need to check the front desk."
if assman:
    scene ep10_bsolo14 with dissolve
else:
    scene ep10_bsolo15 with dissolve
$ renpy.pause()
scene ep10_bsolo16 with dissolve
mc "(She forgot her glasses.)"
scene ep10_bsolo17 with dissolve
mc "(Let's find out how blind she is.)"
scene ep10_bsolo18 with dissolve
$ renpy.pause()
scene ep10_bsolo20 with dissolve
$ renpy.pause()
scene ep10_bsolo22 with dissolve
$ renpy.pause()
scene ep10_bsolo21 with dissolve
mc "(Huh?)"
scene ep10_bsolo19 with dissolve
mc "(I can't tell any difference.)"
scene ep10_bsolo23 with dissolve
mc "(Wait a minute...)"
scene ep10_bsolo24 with dissolve
mc "(Hahaha! These are plastic!)"
mc "(Why is she wearing these if they don't do anything for her eyesight?)"
scene ep10_bsolo25 with dissolve
isa "I won't bother you when you're studying, but if you're up for lunch soon, I know a place we could go off-campus."
scene ep10_bsolo26 with dissolve
mc "Absolutely!"
scene ep10_bsolo27 with dissolve
isa "I'm glad that makes you happy."
scene ep10_bsolo26 with dissolve
mc "Oh, I'm a happy guy, alright."
scene ep10_bsolo27 with dissolve
isa "Ok..."
scene ep10_bsolo28 with dissolve
mc "Bella. You forgot your glasses."
scene ep10_bsolo29 with dissolve
isa "Oh, thank you..."
scene ep10_bsolo30 with dissolve
isa "What?"
scene ep10_bsolo31 with dissolve
mc "I bet you need them for work."
scene ep10_bsolo32 with dissolve
isa "Yes, I do."
scene ep10_bsolo31 with dissolve
mc "I bet you do."
mc "It's gonna be pretty hard to read without them, huh?"
scene ep10_bsolo32 with dissolve
isa "You tried them on."
scene ep10_bsolo31 with dissolve
mc "Hahaha! Why do you have fake glasses?"
scene ep10_bsolo32 with dissolve
isa "They aren't fake. It's a genuine brand."
scene ep10_bsolo31 with dissolve
mc "With genuine plastic in them."
scene ep10_bsolo33 with dissolve
isa "Very funny."
scene ep10_bsolo34 with dissolve
mc "Why, though? I didn't see you wear them until you started teaching English."
scene ep10_bsolo33 with dissolve
isa "It's a look. I don't expect you to understand it."
scene ep10_bsolo34 with dissolve
mc "Ah! You want to appear more mature. Is that it?"
scene ep10_bsolo33 with dissolve
isa "Is that how I come off?"
scene ep10_bsolo34 with dissolve
mc "Yeah. Without them, you look younger, I guess."
mc "And when you wear them, you make me want to behave."
scene ep10_bsolo35 with dissolve
isa "Yet you don't."
scene ep10_bsolo34 with dissolve
mc "Hahaha, you wear fake glasses."
scene ep10_bsolo35 with dissolve
stop music fadeout 3
isa "Forget about lunch. I'll ask a co-worker instead."
scene ep10_bsolo36 with dissolve
$ renpy.pause()
$ guideSuggestedPage = 122
play music "music/ep7/licensed_music/track49.mp3"
scene ep10_bsolo37 with wipeleft
$ renpy.pause()
scene ep10_bsolo38 with dissolve
mc "Nice place. It's not too lively, even during lunch hours."
scene ep10_bsolo39 with dissolve
isa "It's mostly takeout. I figured it was a good place for us to eat."
scene ep10_bsolo45 with dissolve
mc "Are you worried about having lunch with me?"
scene ep10_bsolo40 with dissolve
isa "Aren't you?"
scene ep10_bsolo45 with dissolve
menu:
    "No":
        mc "No. I don't see why I should be worried. Teachers eat lunch with their students on campus, too."
        mc "If anything, it's weirder eating off-campus."
    "A bit":
        mc "Yeah, a bit. But I don't know why. We hung out and had lunch before we...you know?"
scene ep10_bsolo40 with dissolve
isa "At least we can talk more freely here."
isa "So, about your frat mate... Is there any development I should know about?"
scene ep10_bsolo45 with dissolve
mc "Nick? No, he hasn't said a word about us. And I've checked with him two times."
mc "I thought he'd at least mention it to one of our brothers, but...nope. He's keeping a tight lid on it."
scene ep10_bsolo39 with dissolve
isa "That's good."
scene ep10_bsolo45 with dissolve
mc "And the thing you were supposed to check... Did you do it yet?"
scene ep10_bsolo40 with dissolve
isa "The handbook?"
scene ep10_bsolo45 with dissolve
mc "Yes."
scene ep10_bsolo40 with dissolve
isa "Don't worry about it."
scene ep10_bsolo46 with dissolve
mc "You checked it. What did it say?"
scene ep10_bsolo47 with dissolve
isa "It's ok."
scene ep10_bsolo46 with dissolve
mc "It is? What's in there about it?"
scene ep10_bsolo40 with dissolve
isa "The lines are blurry, but let's not be concerned."
isa "We'll be fine if we keep this between us and try our best to act normal on campus."
scene ep10_bsolo45 with dissolve
mc "That's amazing... Wow! I was kinda expecting the worst."
mc "I thought you'd have to stop seeing me, but I'm so happy this can continue."
scene ep10_bsolo40 with dissolve
isa "Me too."
scene ep10_bsolo41 with dissolve
mc "Now that we've dealt with that...I guess we can start focusing on each other differently."
scene ep10_bsolo39 with dissolve
isa "Like how?"
scene ep10_bsolo45 with dissolve
mc "Getting to know each other and all."
scene ep10_bsolo39 with dissolve
isa "I think we've done a decent job of that in the past."
scene ep10_bsolo45 with dissolve
mc "Sure, sure. But there are things we've yet to learn."
mc "Like...um... How long have you been working at B&R?"
scene ep10_bsolo42 with dissolve
isa "A little bit over two years."
scene ep10_bsolo45 with dissolve
mc "Huh? Not longer? I thought you'd been here for at least five or maybe even ten years."
scene ep10_bsolo40 with dissolve
isa "No, I worked at another library before that. Uh..."
isa "It's a sensitive topic for me."
scene ep10_bsolo45 with dissolve
mc "Ok. Well, two years is nothing. You fit in very well here."
scene ep10_bsolo39 with dissolve
isa "I do like it here."
isa "The teaching I could do without, but the library work I enjoy."
scene ep10_bsolo45 with dissolve
mc "Sorry that our class isn't that great to teach at times."
scene ep10_bsolo42 with dissolve
isa "It's not your class that's the issue. It's me."
isa "I'm sure everyone has to endure activities or people they could live without at work, and teaching is that for me."
isa "It's not that I hate it, but it's not what I pictured myself doing."
isa "And lately, I've been given increased responsibilities for classes, which is a bummer."
scene ep10_bsolo45 with dissolve
mc "Yeah? What was your dream job?"
scene ep10_bsolo42 with dissolve
isa "During my first job interviews after college, they liked to ask what I pictured myself doing in five years, and I was naive back then."
isa "I answered wholeheartedly, in a way that didn't scream \"prospective long-term employee\"."
isa "After I realized they weren't going to hire someone who said they wanted to start their own business - a small bookshop or similar - I changed my answer to something more pleasing."
scene ep10_bsolo45 with dissolve
mc "Is that what you dreamt of? To start your own business?"
scene ep10_bsolo39 with dissolve
isa "I didn't want something big, just something that I could manage on my own or perhaps with the help of my husband."
isa "I know bookshops are going extinct in this digital age, but there are ways you could adapt."
isa "And as an avid reader, I strongly advocate reading paperback books instead of tablets."
scene ep10_bsolo42 with dissolve
isa "Books have a feeling that cannot be replaced by modern technology."
isa "Even though audiobooks have gained popularity, I assume there will be enough demand for books during my lifetime to make it work."
isa "So, I think that kind of store would suit me well."
scene ep10_bsolo45 with dissolve
mc "It sounds like you've got the complete picture of it."
scene ep10_bsolo42 with dissolve
isa "In my mind, it was a vivid dream."
scene ep10_bsolo45 with dissolve
mc "How come it never happened?"
scene ep10_bsolo42 with dissolve
isa "For many different reasons... I had little work experience, for a start. And I lacked the funds to get it going."
isa "But mostly... The idea of diving in headfirst scared me. There were days when I was close to doing it."
isa "But as I researched what it would require of me, I felt overwhelmed and scared."
scene ep10_bsolo43 with dissolve
isa "Having a full-time job with a secure employer is not something most are willing to gamble with."
isa "And other factors came into play too at that time..."
isa "And so, it never happened."
scene ep10_bsolo45 with dissolve
mc "Do you still dream of it?"
scene ep10_bsolo44 with dissolve
isa "No... I let go of that dream quite some time ago."
isa "It's a mere memory of who I used to be."
isa "Life didn't turn out the way I expected it to."
isa "But the important thing for me right now is that I'm still here, doing my best."
scene ep10_bsolo45 with dissolve
mc "I'm sure many like you didn't get to do what they dreamt of, or maybe their dreams changed with time."
mc "I'm not sure what I dream of, and thinking too much about the future scares me."
mc "Being in college is nice and all, but after these years...then what? Will I have even figured myself out by then?"
scene ep10_bsolo39 with dissolve
isa "I know that feeling all too well."
isa "My best advice would be to enjoy every moment you feel happy because one day you will look back at those moments and they will keep you warm inside."
scene ep10_bsolo45 with dissolve
mc "That's some nice advice."
scene ep10_bsolo48 with dissolve
isa "Thanks for lunch."
scene ep10_bsolo49 with dissolve
if affinity == "CHICK":
    mc "It was my pleasure."
else:
    mc "Well, we had to eat, and it was pretty good."
mc "By the way... When can I stay at your place again?"
scene ep10_bsolo48 with dissolve
isa "My weekend is wide open. Unless you have another party to attend, you can stop by."
scene ep10_bsolo49 with dissolve
mc "I have plans on Friday, but Saturday works."
mc "I don't think there will be another big party until Thanksgiving."
stop music fadeout 3
scene ep10_bsolo48 with dissolve
isa "Saturday it is."
scene ep10_bsolo50 with dissolve
$ renpy.pause()
$ mgallery_add_photo("ep10_bella_solo_pic0")
$ new_bio("Isabella", "I had lunch with Bella, and she told me she dreamt of starting her own business when she was younger.")
jump ep10_zoey_hangout_label

label ep10_bella_solo_label:
$ guideSuggestedPage = 128
play music "music/ep7/licensed_music/track49.mp3"
queue music ["music/ep7/licensed_music/track54.mp3","music/ep7/licensed_music/track49.mp3"]
scene ep10_bella_solo0 with wipeleft
$ renpy.pause()
scene ep10_bella_solo0b with dissolve
$ renpy.pause()
scene ep10_bella_solo1 with dissolve
$ renpy.pause()
scene ep10_bella_solo2 with dissolve
mc "You have a lot of channels..."
mc "I thought it would end at some point, but it keeps going."
scene ep10_bella_solo3 with dissolve
isa "You don't have to browse through all of them."
scene ep10_bella_solo2 with dissolve
mc "What do you wanna watch?"
scene ep10_bella_solo4 with dissolve
isa "It doesn't matter to me. But I'd rather spend the night talking to you than watching a movie."
scene ep10_bella_solo2 with dissolve
mc "Then it does matter what I choose."
scene ep10_bella_solo3 with dissolve
isa "Again. You don't have to browse through all of them."
scene ep10_bella_solo17d with dissolve
mc "There are so many crappy channels that I don't know what's good to watch."
scene ep10_bella_solo17c with dissolve
mc "Whoa! What are these channels?"
scene ep10_bella_solo5 with dissolve
isa "These are obviously the adult ones."
scene ep10_bella_solo6 with dissolve
mc "Why do you have these?"
scene ep10_bella_solo7 with dissolve
isa "I don't know. They must be included in the package."
scene ep10_bella_solo6 with dissolve
mc "Yeah, right."
scene ep10_bella_solo7 with dissolve
isa "I don't usually browse this far when I decide to watch TV, and I don't watch these channels."
scene ep10_bella_solo8 with dissolve
isa "Should I be concerned that you've stopped browsing all of a sudden?"
scene ep10_bella_solo9 with dissolve
mc "Well, you said it didn't matter what I chose."
scene ep10_bella_solo8 with dissolve
isa "Oh, come on. This is not what you're choosing."
scene ep10_bella_solo9 with dissolve
mc "It's not a movie. That's the only thing you said you didn't wanna watch."
scene ep10_bella_solo10 with dissolve
isa "[name]. I can't eat to this. Wine, cheese, and porn don't go well together."
scene anim_bella_porn2_ep10 with dissolve
mc "Wow! Look at them go."
isa "[name]? Are you even listening?"
scene ep10_bella_solo12 with dissolve
mc "Yeah, I am. But I'm fascinated by this."
mc "Look at the guy! That's gotta hurt for the girl, right?"
scene ep10_bella_solo13 with dissolve
isa "I suppose. But when there's a camera pointed at you and you agreed to get paid to do it, little would stop you."
scene ep10_bella_solo12 with dissolve
mc "Oh, really? You seem to know a lot about it."
scene ep10_bella_solo14 with dissolve
isa "Women do things in bed for men that they don't necessarily like."
isa "They fake orgasms and go along with their partner's weird kinks."
isa "It's not hard to imagine this girl pushing through this scene because she gets paid for it."
scene ep10_bella_solo12 with dissolve
mc "The girl might not enjoy it, but I bet the guy does."
scene ep10_bella_solo13 with dissolve
isa "Much like us watching this channel."
scene ep10_bella_solo15 with dissolve
mc "Here. You can choose what you want to watch."
scene ep10_bella_solo16 with dissolve
isa "If it goes against your principles to shut off porn, fine."
scene ep10_bella_solo17 with dissolve
mc "And what the hell is this?"
scene ep10_bella_solo17a with dissolve
isa "This is my kind of porn."
mc "She's not that hot."
isa "Oh, shut it."
isa "In every episode, they help couples decorate one of their rooms and give tips and tricks about how you can do something to spruce up yours."
scene ep10_bella_solo18 with dissolve
mc "..."
scene ep10_bella_solo19 with dissolve
mc "This sucks..."
mc "I can't eat to this."
scene ep10_bella_solo20 with dissolve
isa "Haha! Well, we're not watching porn during TV night. Find a way to deal with it."
scene ep10_bella_solo21 with dissolve
$ renpy.pause()
scene anim_bella_rub_ep10 with dissolve
isa "You don't have to do that."
mc "I know. But it's nice, no?"
isa "Mmm... Very. You never realize how much you want a foot massage until you get one."
mc "Consider it my apology."
scene ep10_bella_solo22 with dissolve
isa "For putting on porn?"
scene ep10_bella_solo23 with dissolve
mc "No. For how I behaved during yoga class."
mc "I was stupid. I shouldn't have mocked something you like."
scene ep10_bella_solo22 with dissolve
isa "I didn't expect you to love it."
isa "But I also didn't expect you to look at girls' butts that much either."
scene ep10_bella_solo23 with dissolve
mc "What are you supposed to do when you're at the back of the class and girls bend over in front of you?"
scene ep10_bella_solo24 with dissolve
isa "Oh, [name]..."
scene ep10_bella_solo25 with dissolve
mc "Look. You don't know the effect yoga pants have on guys. There's something magical about them."
mc "If it makes you feel better, I would have stared at your ass if you were in front of me."
scene ep10_bella_solo26 with dissolve
isa "You suck at apologies."
scene ep10_bella_solo25 with dissolve
mc "Well, it's true! It wasn't about the girls in front of me. It was about tight yoga pants and butts."
mc "It's in my blood, Bella. Don't you think cavemen loved butts too?"
scene ep10_bella_solo26 with dissolve
isa "Keep going. I'd love to spot when you realize you should have stopped talking."
scene ep10_bella_solo27 with dissolve
mc "Wouldn't you look at my ass if I bent before you?"
scene ep10_bella_solo26 with dissolve
isa "Mhm. Sure. I'd be staring for hours."
scene ep10_bella_solo27 with dissolve
mc "..."
mc "I'm sorry."
scene ep10_bella_solo28 with dissolve
isa "Are you done?"
scene ep10_bella_solo27 with dissolve
mc "Yeah. We don't have to do that again."
scene ep10_bella_solo29 with dissolve
isa "I wasn't born yesterday. I know men look, but maybe not as blatantly as you did. Let's drop it."
scene ep10_bella_solo30 with dissolve
mc "Ok..."
mc "So... Did you ever play Beer Pong back in college?"
scene ep10_bella_solo29 with dissolve
isa "Why do you ask?"
scene ep10_bella_solo30 with dissolve
if ep10_pp_activity == 0:
    mc "We're gonna have it at our next party. I think it will be fun."
else:
    mc "We considered having it at our next party, but I decided against it. Now I'm thinking it was a mistake to skip it."
scene ep10_bella_solo29 with dissolve
isa "If you never played Beer Pong, you didn't go to college. That's my opinion on it."
scene ep10_bella_solo31 with dissolve
mc "Ah, did you like playing it?"
scene ep10_bella_solo32 with dissolve
isa "I was the Beer Pong champ. Guys hated playing me because I always won."
scene ep10_bella_solo31 with dissolve
mc "Sarcasm?"
scene ep10_bella_solo33 with dissolve
isa "What? No! I was the Beer Pong champ!"
scene ep10_bella_solo32 with dissolve
isa "I beat most I played. And if they were stupid, they challenged me to a rematch."
isa "I'd ruin their nights because of how much they were forced to drink."
scene ep10_bella_solo31 with dissolve
mc "Haha! No way! That's cool."
mc "Did you guys play the strip version or just the regular one?"
scene ep10_bella_solo32 with dissolve
isa "Both. But my clothes never came off."
scene ep10_bella_solo31 with dissolve
mc "Damn, I'd love to challenge you."
scene ep10_bella_solo32 with dissolve
isa "Are you any good at it?"
scene ep10_bella_solo31 with dissolve
mc "I think I would be, yeah. I haven't played it much, but it's not a hard game."
scene ep10_bella_solo34 with dissolve
isa "Which shot is your favorite?"
scene ep10_bella_solo35 with dissolve
mc "Uh... Oh, you mean if I like to shoot bounce shots?"
scene ep10_bella_solo34 with dissolve
isa "It sounds like I'm talking to an amateur, for sure."
scene ep10_bella_solo35 with dissolve
mc "Tsk! I think you're exaggerating your skills."
scene ep10_bella_solo36 with dissolve
isa "..."
scene ep10_bella_solo37 with dissolve
isa "Are you challenging the Beer Pong champ?"
scene ep10_bella_solo38 with dissolve
mc "I mean, I think I could beat you. Not that we'd know; there's no table here."
scene ep10_bella_solo37 with dissolve
isa "I have cups and a ping pong ball in the garage. There's a table in the dining room."
isa "So, I'll ask you again. Are you challenging me?"
scene ep10_bella_solo38 with dissolve
mc "We're watching TV, so..."
scene ep10_bella_solo40 with dissolve
isa "The winner gets to decide what we're watching."
scene ep10_bella_solo39 with dissolve
mc "Well, I guess we'll be watching porn in about 20 minutes from now."
scene ep10_bella_solo40 with dissolve
isa "After I'm done with you, you'll learn how to choose flowers for a vase to make your living room pop."
scene ep10_bella_solo39 with dissolve
mc "I'd say that sounds like trash talk, but it doesn't sound like trash talk."

scene ep10_bella_solo41 with wipeleft
isa "The cups are in place. I'll let you start so you have no excuse when you lose."
scene ep10_bella_solo42 with dissolve
mc "We're playing the strip version, right?"
stop music fadeout 3
scene ep10_bella_solo43 with dissolve
isa "If you're eager to show me your penis while we're at it, I won't mind."

play music "music/ep8/licensed_music/track71.mp3"

hide screen new_phone_screen
if minigames and not bp_tut_ep10_seen and (tutorials or not persistent.bp_tutorial):
    menu:
        "Watch tutorial":
            $ bp_tut_ep10_seen = True
            $ bp_dlg = 0
            $ bp_jump_label = "ep10_bp_match_isabella_label"
            show screen bp_tut_screen
            pause
            $ persistent.bp_tutorial = True
        "Skip tutorial":
            $ renpy.pause(0.5)
label ep10_bp_match_isabella_label:
$ renpy.block_rollback()
$ bp_init_game("Isabella","ep10","ep10_bp_after_isabella_label")
if minigames:
    show screen bp_screen
else:
    show screen bp_screen_nm
pause

label ep10_bp_after_isabella_label:
play music "music/ep7/licensed_music/track54.mp3"
queue music ["music/ep7/licensed_music/track49.mp3","music/ep7/licensed_music/track54.mp3"]
if bp_player_won:
    if minigames:
        scene ep10_bbq_bpi_event1
        hide screen bp_screen
        with dissolve
    else:
        scene ep10_bbq_bpi_event1
        hide screen bp_screen_nm
        with dissolve
    show screen new_phone_screen
    mc "Did I just beat the self-proclaimed Beer Pong champ?"
    scene ep10_bbq_bpi_event2 with dissolve
    isa "..."
    mc "I'll take that silence as a \"Yes, you did\"!"
    mc "Man, I didn't know I was this good at Beer Pong."
    scene ep10_bbq_bpi_event3 with dissolve
    mc "And what a night this will be, too! First, I get to see you naked; then we'll spend the evening watching porn."
    isa "..."
    scene ep10_bbq_bpi_event9 with dissolve
    isa "Best out of three?"
    scene ep10_bbq_bpi_event10 with dissolve
    mc "Haha! Nope! You can't make up new rules after losing."
    mc "Let me say that I am honored to be the first ever to have you strip during Beer Pong."
    scene ep10_bbq_bpi_event11 with dissolve
    isa "Fine. I hope you're happy."
    mc "Yeah, I am. This is turning into a hell of a night."
    scene ep10_bbq_bpi_event10 with dissolve
    $ renpy.pause()
    scene ep10_bbq_bpi_event12 with dissolve
    mc "Ahh... Wine, cheese, and porn - the perfect combination! My night is complete."
    scene ep10_bbq_bpi_event13 with dissolve
    $ renpy.pause()
    scene ep10_bbq_bpi_event14 with dissolve
    mc "But I don't want to ruin yours, so here you go."
    scene ep10_bella_solo17b with dissolve
    isa "No, no. You won. Go ahead."
    scene ep10_bbq_bpi_event15 with dissolve
    mc "No, I'm serious. We're not just gonna watch TV anyway, and I don't want you to sulk all night because you lost."
    mc "And who knows? Maybe my room could use some more flowers."
    mc "And you changed my mind about this chick; she is kinda hot."
    scene ep10_bbq_bpi_event16 with dissolve
    isa "So, you've never played Beer Pong before...? Are you at least good at ball sports?"
    scene ep10_bbq_bpi_event15 with dissolve
    mc "I can kick and throw a ball, but I don't think I'm that good at it. I must have been lucky tonight."
else:
    if minigames:
        scene ep10_bbq_bpi_event4
        hide screen bp_screen
        with dissolve
    else:
        scene ep10_bbq_bpi_event4
        hide screen bp_screen_nm
        with dissolve
    show screen new_phone_screen
    isa "And that's why I am the champ."
    scene ep10_bbq_bpi_event5 with dissolve
    mc "Wow, you weren't exaggerating. You are very good."
    scene ep10_bbq_bpi_event6 with dissolve
    isa "If you had only listened, you wouldn't have to show me your genitals and spend the evening watching a show aimed at a predominantly feminine audience."
    scene ep10_bbq_bpi_event7 with dissolve
    mc "It's not like you haven't seen it before."
    scene ep10_bbq_bpi_event6 with dissolve
    isa "It's not about that. It's the humiliation I enjoy."
    scene ep10_bbq_bpi_event7 with dissolve
    mc "Were you this horrible back in college?"
    scene ep10_bbq_bpi_event6 with dissolve
    isa "Less talking, more showing me your penis."
    scene ep10_bbq_bpi_event8 with dissolve
    mc "Fine, I feel humiliated..."
    scene ep10_bbq_bpi_event6 with dissolve
    isa "Good boy. Now that we've settled that you can lose to a girl, let's have you finish that foot rub."
    scene ep10_bbq_bpi_event7 with dissolve
    mc "Good luck getting another one from me."
    scene ep10_bbq_bpi_event17 with dissolve
    isa "*{i}Breathes slowly{/i}* Mmm..."
    isa "It feels good that I still got it."
    scene ep10_bbq_bpi_event18 with dissolve
    mc "Yeah, you definitely do... I thought you were joking, but it's pretty hot that you're that good at it."
    scene ep10_bella_solo17b with dissolve
    mc "This show, though... If I show you my dick again, can we watch something else?"
    isa "No. Let me have my victory."
    scene ep10_bbq_bpi_event18 with dissolve
    mc "Haha, fine... I'll shut up and watch."
    mc "Maybe my room could use some more flowers."

label ep10_isabella_lewd_label:
if _in_replay:
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
        $ isabella  = persistent.isabella
    play music "music/ep7/licensed_music/track54.mp3"

hide screen new_phone_screen
scene ep10_isabella_lewd1 with dissolve
$ renpy.pause()
scene anim_bella_arm_ep10 with dissolve
mc "This is nice... I like it when you do that."
isa "Good. I like to do it."
pause
scene ep10_isabella_lewd2 with dissolve
isa "And I like you. Even when you push my buttons."
scene ep10_isabella_lewd3 with dissolve
menu:
    "Stroke her arm":
        scene ep10_isabella_lewd4 with dissolve
        $ renpy.pause()
    "Kiss her forehead":
        scene ep10_isabella_lewd5 with dissolve
        mc "*{i}Smack{/i}*"
scene ep10_isabella_lewd6 with dissolve
$ renpy.pause(13)
show screen click_to_continue_screen with dissolve
$ renpy.pause(2)
hide screen click_to_continue_screen with dissolve
$ renpy.pause()

scene ep10_isabella_lewd7 with dissolve
$ renpy.pause()
scene anim_bella_porn1_ep10 with dissolve
mc "What are you doing?"
isa "I've seen that episode before. We can watch this instead."
scene ep10_isabella_lewd8 with dissolve
mc "You don't have to do this. I was just having fun with you."
scene ep10_isabella_lewd9 with dissolve
isa "I'm not doing it ironically. Maybe you'll learn something from this channel, too."
scene anim_bella_porn1_ep10 with dissolve
wom "Fuck my asshole, sexy!"
mc "Whoa... That's graphic."
isa "She certainly seems to be enjoying it."
mc "Him too. Wow... Are you into this?"
scene ep10_isabella_lewd9 with dissolve
isa "That's rather on the nose."
scene ep10_isabella_lewd8 with dissolve
mc "A \"no\", then."
scene ep10_isabella_lewd10 with dissolve
isa "I'll be right back."
scene ep10_isabella_lewd11 with dissolve
mc "Bella, we don't have to watch it."
scene ep10_isabella_lewd12 with dissolve
isa "No, no. It's not that. Keep watching."
scene ep10_isabella_lewd13 with dissolve
mc "(She needs a sarcasm sign or something... Does she want me to change it or not?)"
scene ep10_isabella_lewd14 with dissolve
mc "(That looks hot... But boy, does it feel weird to watch porn alone like this, with live candles and all.)"
scene ep10_isabella_lewd15 with dissolve
stop music fadeout 3
mc "(Bella was right about the cheese... It doesn't taste as good now.)"
isa "[name]...?"
play music "music/ep8/licensed_music/track85.mp3"
queue music ["music/ep9/licensed_music/track131.mp3","music/ep8/licensed_music/track85.mp3"]
scene bg anim_bella_pan_ep10 movie with dissolve
pause
scene ep10_isabella_lewd17 with dissolve
isa "Enjoying your show?"
scene ep10_isabella_lewd16 with dissolve
mc "What's going on?"
scene ep10_isabella_lewd18 with dissolve
isa "Not much. I thought I'd slip into something more comfortable."
scene ep10_isabella_lewd19 with dissolve
isa "Watch your porn."
scene ep10_isabella_lewd20 with dissolve
mc "You're way more arousing than the porn."
scene ep10_isabella_lewd19 with dissolve
isa "Finally, a good answer."
scene ep10_isabella_lewd21 with dissolve
mc "You are. I'm getting hard looking at you..."
scene ep10_isabella_lewd22 with dissolve
isa "Watch the porn."
scene ep10_isabella_lewd23 with dissolve
$ renpy.pause()
scene ep10_isabella_lewd24 with dissolve
isa "Remove your pants and underwear for me."
scene ep10_isabella_lewd25 with dissolve
mc "What's that for?"
scene ep10_isabella_lewd26 with dissolve
isa "Shh..."
scene anim_bella_hj_ep10 with dissolve
mc "Oh, God..."
isa "Haha..."
pause
scene anim_bella_hj2_ep10 with dissolve
isa "Do you like how he's fucking her ass like that? Pinning her down and making her beg for it?"
mc "I'm not even watching..."
isa "Open your eyes and do it."
mc "Ok... Yeah, that looks hot."
pause
scene ep10_isabella_lewd27 with dissolve
$ renpy.pause()
scene ep10_isabella_lewd28 with dissolve
$ renpy.pause()
scene ep10_isabella_lewd29 with dissolve
$ renpy.pause()
scene ep10_isabella_lewd30 with dissolve
$ renpy.pause()
scene anim_bella_boobs1_ep10 with dissolve
mc "You probably prefer the foot massage, but I definitely prefer this."
isa "I'm not remotely surprised."
pause
scene anim_bella_boobs2_ep10 with dissolve
mc "*{i}Lick lick{/i}*"
pause
scene anim_bella_kiss_ep10 with dissolve
isa "*{i}Smack lick{/i}*"
pause
scene ep10_isabella_lewd31 with dissolve
wom "Yes! Spank my ass, sexy!"
scene ep10_isabella_lewd32 with dissolve
$ renpy.pause()
scene ep10_isabella_lewd33 with dissolve
$ renpy.pause()
scene anim_bella_grind1_ep10 with dissolve
mc "Fuck... You're such a tease, [isabella]."
isa "Mhm... Spank my ass, sexy..."
pause
play sound "sound_effects/slap.mp3"
scene ep10_isabella_lewd34 with vpunch
isa "Hngn..."
scene ep10_isabella_lewd35 with dissolve
$ renpy.pause()
scene anim_bella_grind2_ep10 with dissolve
pause
play sound "sound_effects/shove.mp3"
scene ep10_isabella_lewd36 with hpunch
$ renpy.pause()
scene anim_bella_boobjob1_ep10 with dissolve
pause
scene anim_bella_boobjob2_ep10 with dissolve
pause
scene ep10_isabella_lewd37 with dissolve
$ renpy.pause()
scene anim_bella_bj1_ep10 with dissolve
isa "*{i}Suck suck{/i}* Mmmppfff..."
mc "Fuck, [isabella]... You're testing my limits here."
isa "*{i}Suck glug suck{/i}*"
pause
scene ep10_isabella_lewd38 with dissolve
mc "Whoa... Stop... It was almost over right there for me, haha..."
scene ep10_isabella_lewd39 with dissolve
isa "I see..."
isa "You're going to have to earn your break, then."
scene ep10_isabella_lewd40 with dissolve
mc "Mmppfff!!!"
isa "Yes... Eat my ass..."
isa "Because this time, it won't be an \"accident\" when you enter it."
scene anim_bella_cunn1_ep10 with dissolve
isa "Mmm... *{i}Moans{/i}* Yes... [mc_isabella]... Use your tongue on me."
mc "*{i}Lick lick{/i}*"
pause
scene ep10_isabella_lewd41 with dissolve
isa "*{i}Moans{/i}* Yes..."

scene ep10_isabella_lewd42 with dissolve
isa "Here."
mc "Whoa..."
scene ep10_isabella_lewd43 with dissolve
isa "Do you know how to use it?"
mc "I mean, I can probably guess where it goes."
scene ep10_isabella_lewd44 with dissolve
isa "That's not good enough. Follow my command to the letter."
isa "Pour some oil on your hand first and insert one finger."
scene ep10_isabella_lewd45 with dissolve
menu:
    "Insert a finger in her pussy":
        scene ep10_isabella_lewd46 with dissolve
        isa "*{i}Moans{/i}* Not there..."
        scene ep10_isabella_lewd45 with dissolve
        $ renpy.pause()
        scene ep10_isabella_lewd47 with dissolve
        isa "Yes... There."
    "Insert a finger in her ass":
        scene ep10_isabella_lewd47 with dissolve
        isa "*{i}Moans{/i}*"
scene ep10_isabella_lewd48 with dissolve
isa "Hngn... Yes... Good."
isa "Pull it out and put in the toy, but only do it a few beads at a time."
scene ep10_isabella_lewd49 with dissolve
mc "Like this?"
scene bg anim_bella_beads_ep10 movie with dissolve
isa "Hngn... Yes. One more bead. Keep going...slowly..."
mc "There... I'm out of beads."
scene ep10_isabella_lewd50 with dissolve
isa "Hngnnn..."
isa "*{i}Exhales{/i}*"
isa "Pull it out in a slow but steady motion. Let it take a while to pull it out."
scene bg anim_bella_beads2_ep10 movie with dissolve
isa "Yes... Hngn... Like that... *{i}Moans{/i}*"
pause
scene ep10_isabella_lewd51 with dissolve
isa "*{i}Breathes heavily{/i}* Ok..."
scene ep10_isabella_lewd52 with dissolve
isa "You've had your break, and I've had my warm-up."
isa "Now... Slowly insert your cock. And I mean slowly!"
scene ep10_isabella_lewd53 with dissolve
mc "Slowly... I got it."
scene ep10_isabella_lewd54 with dissolve
$ renpy.pause()
scene bg anim_bella_insert_ep10 movie with dissolve
isa "Yes... Mmm... *{i}Moans{/i}* Ahhh!!! FUCK!"
pause
scene ep10_isabella_lewd55 with dissolve
isa "Please, tell me that's all of it."
scene ep10_isabella_lewd56 with dissolve
mc "It's like 75%% or so."
isa "Fuck, why do you have to be this big? God!"
mc "You love my size."
scene ep10_isabella_lewd55 with dissolve
isa "Do not put in more than that..."
scene ep10_isabella_lewd57 with dissolve
mc "Then what do you want me to do?"
isa "Pull out slowly and go back in. But not more than 75%% or whatever the hell it is."
scene anim_bella_anal1_ep10 with dissolve
mc "I'll try..."
isa "Ahhh... Fuck!"
mc "I'm doing as you told me to."
isa "I know. Do it like that. *{i}Moans{/i}*"
isa "This will take me a while to get used to."
pause
scene anim_bella_anal2_ep10 with dissolve
mc "It looked easier on TV than it is in reality."
isa "That woman wasn't taking one of this size... Fuck..."
mc "It feels fucking awesome, [isabella]... Like wow... You're so tight."
isa "Yes... It's too tight. Hngn..."
pause
scene ep10_isabella_lewd58 with dissolve
isa "Ok... Stop!"
scene ep10_isabella_lewd59 with dissolve
mc "We don't have to do this if it hurts."
scene ep10_isabella_lewd60 with dissolve
isa "No, we're doing it. Sit down."
isa "It will be easier if I can control how much of it I want. And I need more oil."
scene ep10_isabella_lewd61 with dissolve
mc "Go ahead..."
scene ep10_isabella_lewd62 with dissolve
isa "*{i}Moans{/i}*"
scene anim_bella_anal3_ep10 with dissolve
mc "Fuck, your ass both looks and feels amazing."
pause
scene anim_bella_anal4_ep10 with dissolve
mc "Oh my God... It's all the way in now. You know that, right?"
isa "Yes... This position works better for me... *{i}Moans{/i}*"
mc "Fuck, it's so tight... So, so tight..."
isa "You're not close to cumming again yet, are you?"
mc "I'm doing everything I can not to..."
isa "Good. Because this is far from over."
pause
scene ep10_isabella_lewd63 with dissolve
isa "Now... How do I want you...?"
$ tmpInt = 0
$ tmpBool = False
label ep10_bella_lewd_loop_label:
menu:
    "Missionary (Anal)":
        $ renpy.music.stop(channel="sfx2", fadeout=1)
        $ tmpInt += 1
        $ tmpBool = False
        scene anim_bella_anal1_ep10 with dissolve
        isa "Let's try this again. Hngn..."
        pause
        scene anim_bella_anal2_ep10 with dissolve
        isa "You're so big, [mc_isabella]... *{i}Moans{/i}*"
        pause
        jump ep10_bella_lewd_loop_label
    "Doggystyle (Anal)":
        $ tmpInt += 1
        $ tmpBool = False
        $ renpy.sound.play("sound_effects/season3/bella_slap.mp3", channel="sfx2", loop=True)
        scene anim_bella_doggy1_anal_ep10 with dissolve
        mc "*{i}Grunts{/i}*"
        isa "What's that I'm hearing?"
        mc "I'm trying my best to hold back, but I've been edging a lot."
        isa "*{i}Moans{/i}* You're not getting another break."
        mc "I'll find a way to hold it back... I need to fuck your ass more."
        pause
        jump ep10_bella_lewd_loop_label
    "Prone (Anal)":
        $ renpy.music.stop(channel="sfx2", fadeout=1)
        $ tmpInt += 1
        $ tmpBool = False
        scene anim_bella_prone_ep10 with dissolve
        mc "Oh my God! This is the tightest you've ever been around my cock."
        isa "*{i}Moans{/i}* Yes... It's good that you're using the oil. Fuck..."
        pause
        scene anim_bella_prone2_ep10 with dissolve
        mc "Your ass is unbelievably hot."
        isa "If only I was wearing yoga pants now, huh?"
        mc "What? Haha, no!"
        isa "Enjoy it, [mc_isabella]. I know you want it."
        isa "Fuck me. Fuck me hard!"
        pause
        jump ep10_bella_lewd_loop_label
    "Reverse cowgirl (Anal)":
        $ renpy.music.stop(channel="sfx2", fadeout=1)
        $ tmpInt += 1
        $ tmpBool = False
        scene anim_bella_anal3_ep10 with dissolve
        isa "Sit there, and don't move."
        mc "Ride my cock, [isabella]."
        pause
        scene anim_bella_anal4_ep10 with dissolve
        mc "Fuck, just like that."
        isa "Hngn... Yes... *{i}Moans{/i}*"
        pause
        jump ep10_bella_lewd_loop_label
    "Cowgirl (Anal)":
        $ renpy.music.stop(channel="sfx2", fadeout=1)
        $ tmpInt += 1
        $ tmpBool = True
        scene anim_bella_ride1_anal_ep10 with dissolve
        isa "Mmm... I'm gonna ride your cock until you cum in my asshole."
        mc "No, you won't."
        isa "Yes, I will."
        pause
        scene anim_bella_ride3_anal_ep10 with dissolve
        mc "God..."
        isa "See? I'm telling you. You're going to cum while your hard cock penetrates my ass as I ride you."
        pause
        jump ep10_bella_lewd_loop_label
    "Sideways (Anal)":
        $ renpy.music.stop(channel="sfx2", fadeout=1)
        $ tmpInt += 1
        $ tmpBool = False
        scene anim_bella_side_anal1_ep10 with dissolve
        isa "Yes, give it to me, [mc_isabella]. Fuck my ass..."
        isa "*{i}Moans{/i}* I want it..."
        pause
        jump ep10_bella_lewd_loop_label
    "From below (Anal)":
        $ renpy.music.stop(channel="sfx2", fadeout=1)
        $ tmpInt += 1
        $ tmpBool = False
        scene anim_bella_below_anal1_ep10 with dissolve
        mc "Damn... You're flexible."
        isa "*{i}Moans{/i}* You shouldn't be surprised."
        mc "Yeah, but it still amazes me. This is fucking hot..."
        isa "Enjoy it while it lasts. I can't hold this forever."
        pause
        scene anim_bella_below_anal2_ep10 with dissolve
        mc "I'm gonna make the most out of it."
        isa "Yes... Thrust your cock into my ass, [mc_isabella]."
        pause
        jump ep10_bella_lewd_loop_label
    "Standing (Anal)":
        $ renpy.music.stop(channel="sfx2", fadeout=1)
        $ tmpInt += 1
        $ tmpBool = False
        scene anim_bella_stand1_ep10 with dissolve
        isa "Ahh... Yes... *{i}Moans{/i}*"
        mc "Does it still hurt?"
        isa "No, it stopped hurting a while back. Hngn..."
        pause
        scene anim_bella_stand2_ep10 with dissolve
        pause
        jump ep10_bella_lewd_loop_label
    "Piledriver (Anal)":
        $ renpy.music.stop(channel="sfx2", fadeout=1)
        $ tmpInt += 1
        $ tmpBool = False
        scene anim_bella_pile1_ep10 with dissolve
        isa "Yes, [mc_isabella]! Yes! Pound my ass... Give it to me."
        pause
        scene anim_bella_pile2_ep10 with dissolve
        isa "Get in there... Deep. *{i}Moans{/i}*"
        pause
        jump ep10_bella_lewd_loop_label
    "Cum" if tmpInt > 3:
        mc "Fuck... Fuck... I'm gonna cum!"
        menu:
            "In mouth":
                $ renpy.music.stop(channel="sfx2", fadeout=1)
                scene anim_bella_cum1_ep10 with dissolve
                isa "*{i}Suck glug glug{/i}*"
                mc "I'm doing it... I'm cumming..."
                pause
                scene ep10_isabella_lewd67 at vpunch, cum1
                $ renpy.pause(0.5)
                scene ep10_isabella_lewd67 at vpunch, cum1
                $ renpy.pause(0.5)
                scene ep10_isabella_lewd67 at vpunch, cum1
                mc "Ahhh!"
                scene ep10_isabella_lewd68 with dissolve
                mc "Bella... You're amazing..."
            "Facial":
                $ renpy.music.stop(channel="sfx2", fadeout=1)
                scene anim_bella_cum1_ep10 with dissolve
                isa "*{i}Suck glug glug{/i}*"
                mc "I'm doing it... I'm cumming..."
                pause
                scene ep10_isabella_lewd69 at vpunch, cum2
                $ renpy.pause(0.5)
                scene ep10_isabella_lewd69 at vpunch, cum2
                $ renpy.pause(0.5)
                scene ep10_isabella_lewd69 at vpunch, cum2
                mc "Ahhh!"
                scene ep10_isabella_lewd70 with dissolve
                mc "Bella... You're amazing..."
            "Prone creampie":
                $ renpy.music.stop(channel="sfx2", fadeout=1)
                scene anim_bella_prone2_ep10 with dissolve
                mc "I wanna cum inside your asshole."
                isa "Do it, [mc_isabella]. Cum how you want to. Fill me up."
                pause
                scene ep10_isabella_lewd64 at vpunch, cum1
                $ renpy.pause(0.5)
                scene ep10_isabella_lewd64 at vpunch, cum1
                $ renpy.pause(0.5)
                scene ep10_isabella_lewd64 at vpunch, cum1
                mc "Ahhh!!!"
                scene ep10_isabella_lewd65 with dissolve
                mc "Fuck! That's so amazing... Damn..."
            "Cowgirl creampie":
                $ renpy.music.stop(channel="sfx2", fadeout=1)
                scene anim_bella_ride1_anal_ep10 with dissolve
                if tmpBool:
                    isa "I told you I would make you cum from this."
                isa "Cum, [mc_isabella]... Cum inside my asshole."
                pause
                scene anim_bella_ride2_anal_ep10 with vpunch
                mc "Ahh!!!"
                isa "Yes! Cum! Release it."
                pause
                scene ep10_isabella_lewd66 with dissolve
                mc "Fuck! That's so amazing... Damn..."

$ renpy.music.stop(channel="sfx2", fadeout=1)
scene ep10_isabella_lewd71 with dissolve
$ renpy.pause()
scene ep10_isabella_lewd72 with dissolve
isa "I take it you liked that."
scene ep10_isabella_lewd73 with dissolve
mc "What gave it away?"
mc "I didn't know you were into that. I never would have guessed."
scene ep10_isabella_lewd72 with dissolve
isa "It's good that it's not obvious. Who knows? I might be into a lot of things you wouldn't guess."
scene ep10_isabella_lewd74 with dissolve
mc "Like what?"
scene ep10_isabella_lewd72 with dissolve
isa "Oh, [name]."
scene ep10_isabella_lewd73 with dissolve
mc "You're teasing me now, aren't you?"
scene ep10_isabella_lewd74 with dissolve
mc "I enjoyed that a lot... Sorry if it hurt you at first."
scene ep10_isabella_lewd72 with dissolve
isa "Only at first."
isa "I should get a medal for being able to do that with you."
scene ep10_isabella_lewd74 with dissolve
mc "I guess I could have put less of it in."
scene ep10_isabella_lewd72 with dissolve
isa "I know you're big, but it was the first time I felt you were freakishly big."
scene ep10_isabella_lewd73 with dissolve
mc "Hey! I'm not a freak."
scene ep10_isabella_lewd72 with dissolve
isa "In bed, you kind of are. And also a bit during yoga classes."
scene bg anim_bella_cock_slap_ep10 movie with dissolve
mc "Don't call me a freak."
isa "Hey!?"
scene ep10_isabella_lewd75 with dissolve
stop music fadeout 3
mc "Hahaha!"
isa "Hahaha!"

$ renpy.end_replay()
$ persistent.ep10_lewd_isabella = True
$ calcScenes()
$ new_bio("Isabella", "During TV night with Bella, we ended up having anal sex on her couch while watching porn.")
$ mphone_stats_add_girl_s3("isabella","You had anal sex with Bella at her place in episode 10.")

$ mgallery_add_photo("ep10_bella_solo_pic1")
$ mgallery_add_photo("ep10_bella_solo_pic2")
show screen new_phone_screen





    
if ep10_date_nicole and not ep10_cancel_date_nicole:
    jump ep10_nicole_date_label

jump ep10_science_label


label ep10_bbq_isabella_end_label:
scene ep10_bbq_isabella_end1 with dissolve
mc "(I should get to bed, but this tent doesn't look inviting.)"
scene ep10_bbq_isabella_end2 with dissolve
mc "(I'd much rather be with her... I can't go to her now, can I?)"
mc "(It's just a bus ride away, but still...)"
mc "(Screw it. I'm going.)"
scene ep10_bbq_isabella_end3 with dissolve
mc "(And you're coming with me.)"
scene ep10_bbq_isabella_end4 with wipeleft
$ renpy.pause()
scene ep10_bbq_isabella_end5 with dissolve
$ renpy.pause()
play sound "sound_effects/cellphone.mp3"
scene ep10_bbq_isabella_end6 with dissolve
"*{i}Phone rings{/i}*"
scene ep10_bbq_isabella_end7 with dissolve
isa "*{i}Groans{/i}*"
scene ep10_bbq_isabella_end8 with dissolve
isa "[name]? What's the matter? Are you ok?"
scene ep10_bbq_isabella_end9 with dissolve
mc "Did I wake you?"
scene ep10_bbq_isabella_end8 with dissolve
isa "Yes. Are you ok?"
scene ep10_bbq_isabella_end9 with dissolve
mc "Can you come downstairs? I'm outside."
stop music fadeout 3
scene ep10_bbq_isabella_end8 with dissolve
isa "You're here?"
scene ep10_bbq_isabella_end11 with dissolve
$ renpy.pause()
play music "music/ep10/pineapple_pizza.mp3"
scene ep10_bbq_isabella_end12 with dissolve
$ renpy.pause(10)
show screen click_to_continue_screen with dissolve
$ renpy.pause(2)
hide screen click_to_continue_screen with dissolve
$ renpy.pause()
stop music fadeout 3
play sound "sound_effects/interlude/bark.mp3"
scene ep10_bbq_isabella_end13 with dissolve
"*{i}Dog barks{/i}*"
mc "Oh, shit!"
scene ep10_bbq_isabella_end14 with dissolve
isa "You should probably stop that. Come inside."
play music "music/ep8/licensed_music/track72.mp3"
scene ep10_bbq_isabella_end15 with dissolve
isa "What are you doing here at this hour?"
scene ep10_bbq_isabella_end16 with dissolve
mc "I missed you. I didn't wanna spend my night alone in a tent."
mc "I also thought I could make this another apology for my recent behavior."
scene ep10_bbq_isabella_end15 with dissolve
isa "Waking me up in the middle of the night is a pretty bad apology."
isa "I'm torn between feeling annoyed and happy about this awakening."
scene ep10_bbq_isabella_end16 with dissolve
mc "I'm sorry."
scene ep10_bbq_isabella_end17 with dissolve
isa "But now that you're here, let's jump into bed."
isa "But no funny business; I'm way too tired for it."
scene ep10_bbq_isabella_end10 with dissolve
isa "Did you have a good night?"
scene ep10_bbq_isabella_end18 with dissolve
mc "It was ok. Some highs and some lows. But at least I get to end it with you."
mc "What have you been up to?"
scene ep10_bbq_isabella_end19 with dissolve
isa "Not much. I spent the evening reading and went to bed early."
scene ep10_bbq_isabella_end20 with dissolve
$ renpy.pause()
scene ep10_bbq_isabella_end21 with dissolve
isa "What are you looking at?"
scene ep10_bbq_isabella_end22 with dissolve
isa "Oh..."
scene ep10_bbq_isabella_end23 with dissolve
$ renpy.pause()
scene ep10_bbq_isabella_end24 with dissolve
$ renpy.pause()
scene ep10_bbq_isabella_end25 with dissolve
isa "Why don't you ask me about him?"
scene ep10_bbq_isabella_end26 with dissolve
mc "I've tried in the past. But I know it's something you don't want to discuss, or you would have brought it up."
isa "..."
scene ep10_bbq_isabella_end25 with dissolve
isa "So, it's out of respect?"
scene ep10_bbq_isabella_end26 with dissolve
mc "Yes. I want to know...but I don't want to force it out of you. And Jill once told me I shouldn't ask about it either."
mc "And she seemed serious about it."
scene ep10_bbq_isabella_end25 with dissolve
isa "Jill..."
scene ep10_bbq_isabella_end26 with dissolve
$ renpy.pause()
scene ep10_bbq_isabella_end27 with dissolve
isa "I've told you this before. I am still married to him. James..."
scene ep10_bbq_isabella_end28 with dissolve
mc "I know."
scene ep10_bbq_isabella_end27 with dissolve
isa "Legally, I'm married. But...he hasn't been my husband for a long time."
isa "I don't know where he is."
scene ep10_bbq_isabella_end29 with dissolve
isa "*{i}Sigh{/i}*"
scene ep10_bbq_isabella_end30 with dissolve
mc "Maybe we shouldn't have this talk when we're going to sleep?"
scene ep10_bbq_isabella_end29 with dissolve
isa "There will never be a good time for this talk, [name]."
isa "And it's not you, it's me. I struggle when I try to talk about him, and God knows I've tried."
scene ep10_bbq_isabella_end30 with dissolve
mc "Has he been gone for long?"
scene ep10_bbq_isabella_end27 with dissolve
isa "I've been waiting for him to come home for what feels like an eternity. But it's been around three years now since he left."
scene ep10_bbq_isabella_end28 with dissolve
mc "Ok, I gotta ask... Since you're still married and all... What about us and our relationship?"
scene ep10_bbq_isabella_end25 with dissolve
isa "[name]... I don't know. I can't answer that."
isa "All I know is that you make me feel things I haven't felt in years."
isa "You make me feel things that I am ashamed of. It's like I'm not allowed to feel them."
scene ep10_bbq_isabella_end27 with dissolve
isa "I feel like what we are doing is wrong for many reasons..."
isa "But how can something that's wrong feel this good? And even if it is wrong, this is how I want to feel."
scene ep10_bbq_isabella_end28 with dissolve
isa "..."
scene ep10_bbq_isabella_end29 with dissolve
isa "And James...he's... He's been missing for a long time now."
isa "He - *{i}Breathes heavily{/i}* - left and... *{i}Breathes heavily{/i}* I didn't want him to leave, and they said he could still be alive, but..."
isa "No one knows where he is."
scene ep10_bbq_isabella_end31 with dissolve
isa "*{i}Hyperventilates{/i}*"
scene ep10_bbq_isabella_end32 with dissolve
mc "Come here..."
scene ep10_bbq_isabella_end33 with dissolve
isa "*{i}Sobs{/i}*"
mc "(Fuck... She's upset now... I have no clue how to deal with this... What do I say?)"
mc "W-we don't have to talk about this."
mc "You've shared some of it with me tonight. And I'm happy you did."
mc "Even though you're not sure about anything... I'm sure I want to be with you."
scene ep10_bbq_isabella_end35 with dissolve
$ renpy.pause()
scene ep10_bbq_isabella_end34 with dissolve
isa "I feel like I've been constantly drowning, [name]."
isa "I'm deep down in the abyss, and everything is pitch black."
isa "Yet, I keep holding my breath somehow."
scene ep10_bbq_isabella_end36 with dissolve
isa "And when I met you, I realized I was drowning less with time."
isa "It's like you're the air I need."
scene ep10_bbq_isabella_end34 with dissolve
isa "Please... Stay with me."
scene ep10_bbq_isabella_end35 with dissolve
mc "I'm not going anywhere."
stop music fadeout 3
scene ep10_bbq_isabella_end37 with dissolve
$ renpy.pause()

scene black with fade
$ renpy.pause(2)
play music "music/ep9/licensed_music/track120.mp3"
scene ep10_pre_tgb1 with dissolve
mc "Hnn..."
scene ep10_pre_tgb2 with dissolve
mc "Ahhh... Wha... Hnnn..."
scene ep10_pre_tg41 with dissolve
tm "[name]! Open up wide!"
mc "AHHH!! IS IT ANOTHER SHOT?"
tm "Derek! Do it!"
scene ep10_pre_tg42 with dissolve
mc "No! Get that cock away from me!"
de "Hahaha!"

play sound "sound_effects/whoosh_2.mp3"
scene ep10_pre_tg43
mc "Dad taught me everything I know. He knows all kinds of stuff."
scene ep10_pre_tg44 with dissolve
tm "That's fucking cool."
play sound "sound_effects/whoosh_2.mp3"
scene ep10_pre_tg45
mc "Why don't you like me?"
scene ep10_pre_tg46 with dissolve
tm "I do! We're bonding here, aren't we?"
scene ep10_pre_tg45 with dissolve
mc "You're drunk! Where are the shots?"

play sound "sound_effects/whoosh_2.mp3"
scene ep10_pre_tg47
mc "I'M HAVING THE BEST TIME OF MY LIFE!"

play sound "sound_effects/whoosh_2.mp3"
scene ep10_pre_tg39
rs "[name], you can't take your clothes off in the club like that."
scene ep10_pre_tg40 with dissolve
mc "*{i}Sobs{/i}* I just wanted to dance for them!"

play sound "sound_effects/whoosh_2.mp3"
$ renpy.sound.play("sound_effects/season2/puke.mp3", channel="sfx3", loop=False)
scene ep10_pre_tg48 with vpunch
mc "*{i}Pukes{/i}*"
my "How much did you drink?"
stop music
scene ep10_pre_tgb3 with vpunch
isa "[name]?"
mc "Huh!?"
play music "music/ep9/relaxed.mp3"
scene ep10_pre_tgb4 with dissolve
mc "Ugh..."
isa "Ugh, huh? That doesn't sound like a good start to this morning."
mc "Oh, good morning... No, I'm fine."
isa "Are you sure?"
scene ep10_pre_tgb5 with dissolve
mc "Give me some coffee, and I will be."
scene ep10_pre_tgb6 with dissolve
mc "Oh, you're dressed already?"
scene ep10_pre_tgb7 with dissolve
isa "You slept in. I've been up and about for a few hours."
isa "In that time, I've talked to both Jill and Sage about today."
scene ep10_pre_tgb8 with dissolve
mc "Oh? Why Sage?"
scene ep10_pre_tgb10 with dissolve
isa "Maybe you forgot what I told you last night. But I've invited them here today, and we'll be helping you guys out the best we can."
scene ep10_pre_tgb8 with dissolve
mc "I remember."
scene ep10_pre_tgb7 with dissolve
isa "You don't have much time. Let's get you some coffee, and I'll drive you back home."
scene ep10_pre_tgb5 with dissolve
mc "Oh, yeah... I gotta help clean up at the campsite too. I'd appreciate that ride."
scene ep10_pre_tgb9 with dissolve
isa "And I appreciate that you showed up last night. Not at first, but after."
scene ep10_pre_tgb11 with dissolve
mc "Yeah... I'm happy we talked more about that. It's been in the back of my mind for a long time."
scene ep10_pre_tgb8 with dissolve
$ renpy.pause()
scene ep10_pre_tgb7 with dissolve
isa "Promise me you'll be safe today. And don't do something stupid or...something you'd probably do."
scene ep10_pre_tgb8 with dissolve
mc "Heh... I'll try."
stop music fadeout 3
scene ep10_pre_tgb7 with dissolve
isa "Well... Up you go."

$ new_bio("Isabella", "Bella tried to talk to me about James, but it was very hard for her to discuss her marriage.")
jump ep10_tg_label
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
