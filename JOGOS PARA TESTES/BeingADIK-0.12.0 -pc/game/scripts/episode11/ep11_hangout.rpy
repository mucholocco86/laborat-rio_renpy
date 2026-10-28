label ep11_ho_main_label:
$ renpy.block_rollback()
play music "music/ep11/licensed_music/track163.mp3"
queue music ["music/ep11/licensed_music/track164.mp3","music/ep11/licensed_music/track163.mp3"]

if ep10_got_contracts:
    scene ep11_ho_main with dissolve
else:
    scene ep11_hob_main with dissolve


show white_screen with dissolve
show text "{font=fonts/collegiate.ttf}{size=+%d}{color=#fe961b}Hangout:{/color} Isabella's home{/size}{/font}" % (40 * persistent.scale_factor):
    yalign 0.84
    xalign 0.5
$ renpy.pause()
hide text
hide white_screen
$ tmp_list = [False, False, False, False, False, False]

label ep11_ho2_main_label:

$ renpy.block_rollback()
$ currentFreeRoamLabel = "ep11_ho2_main_label"

if False not in tmp_list:
    jump ep11_ho_end_label
if not tmp_list[0]:
    if ep10_got_contracts:
        scene ep11_ho_main with dissolve
    else:
        scene ep11_hob_main with dissolve
else:
    if ep10_got_contracts:
        scene ep11_ho_mainb with dissolve
    else:
        scene ep11_hob_mainb with dissolve

if not tmp_list[0]:
    $ ui.imagebutton("ep11_ho_sage_idle", "ep11_ho_sage_hover", clicked=ui.returns("sage"), xpos=0, ypos=0, focus_mask=True)
if not tmp_list[1]:
    if not tmp_list[0]:
        if ep10_got_contracts:
            $ ui.imagebutton("ep11_ho_bella_idle", "ep11_ho_bella_hover", clicked=ui.returns("bella"), xpos=0, ypos=0, focus_mask=True)
        else:
            $ ui.imagebutton("ep11_hob_bella_idle", "ep11_hob_bella_hover", clicked=ui.returns("bella"), xpos=0, ypos=0, focus_mask=True)
    else:
        if ep10_got_contracts:
            $ ui.imagebutton("ep11_ho_bellab_idle", "ep11_ho_bellab_hover", clicked=ui.returns("bella"), xpos=0, ypos=0, focus_mask=True)
        else:
            $ ui.imagebutton("ep11_hob_bellab_idle", "ep11_hob_bellab_hover", clicked=ui.returns("bella"), xpos=0, ypos=0, focus_mask=True)
if (ep9_jm_sad and tmp_list[1]) or not ep9_jm_sad:
    if not tmp_list[2]:
        if not tmp_list[0]:
            if ep10_got_contracts:
                $ ui.imagebutton("ep11_ho_josy_idle", "ep11_ho_josy_hover", clicked=ui.returns("josy"), xpos=0, ypos=0, focus_mask=True)
            else:
                $ ui.imagebutton("ep11_hob_josy_idle", "ep11_hob_josy_hover", clicked=ui.returns("josy"), xpos=0, ypos=0, focus_mask=True)
        else:
            if ep10_got_contracts:
                $ ui.imagebutton("ep11_ho_josyb_idle", "ep11_ho_josyb_hover", clicked=ui.returns("josy"), xpos=0, ypos=0, focus_mask=True)
            else:
                $ ui.imagebutton("ep11_hob_josyb_idle", "ep11_hob_josyb_hover", clicked=ui.returns("josy"), xpos=0, ypos=0, focus_mask=True)
if not tmp_list[3]:
    if not tmp_list[0]:
        if ep10_got_contracts:
            $ ui.imagebutton("ep11_ho_maya_idle", "ep11_ho_maya_hover", clicked=ui.returns("maya"), xpos=0, ypos=0, focus_mask=True)
        else:
            $ ui.imagebutton("ep11_hob_maya_idle", "ep11_hob_maya_hover", clicked=ui.returns("maya"), xpos=0, ypos=0, focus_mask=True)
    else:
        if ep10_got_contracts:
            $ ui.imagebutton("ep11_ho_mayab_idle", "ep11_ho_mayab_hover", clicked=ui.returns("maya"), xpos=0, ypos=0, focus_mask=True)
        else:
            $ ui.imagebutton("ep11_hob_mayab_idle", "ep11_hob_mayab_hover", clicked=ui.returns("maya"), xpos=0, ypos=0, focus_mask=True)
if not tmp_list[4]:
    if not tmp_list[0]:
        if ep10_got_contracts:
            $ ui.imagebutton("ep11_ho_derek_idle", "ep11_ho_derek_hover", clicked=ui.returns("derek"), xpos=0, ypos=0, focus_mask=True)
        else:
            $ ui.imagebutton("ep11_hob_derek_idle", "ep11_hob_derek_hover", clicked=ui.returns("derek"), xpos=0, ypos=0, focus_mask=True)
    else:
        if ep10_got_contracts:
            $ ui.imagebutton("ep11_ho_derekb_idle", "ep11_ho_derekb_hover", clicked=ui.returns("derek"), xpos=0, ypos=0, focus_mask=True)
        else:
            $ ui.imagebutton("ep11_hob_derekb_idle", "ep11_hob_derekb_hover", clicked=ui.returns("derek"), xpos=0, ypos=0, focus_mask=True)

if tmp_list[0] and not tmp_list[5]:
    $ ui.imagebutton("ep11_ho_jill_idle", "ep11_ho_jill_hover", clicked=ui.returns("jill"), xpos=0, ypos=0, focus_mask=True)


$ result = ui.interact()
if result == "josy":
    if ep9_jm_sad:
        jump ep11_ho_josy2_label
    else:
        jump ep11_ho_josy_label
elif result == "maya":
    jump ep11_ho_maya_label
elif result == "derek":
    jump ep11_ho_derek_label
elif result == "sage":
    jump ep11_ho_sage_label
elif result == "bella":
    jump ep11_ho_bella_label
elif result == "jill":
    jump ep11_ho_jill_label


label ep11_ho_end_label:
stop music fadeout 3
scene ep11_ho_end with dissolve
$ renpy.pause()
jump ep11_quinn_dt_label

label ep11_ho_sj_label:
if ep10_got_contracts:
    scene ep11_ho_sj1 with dissolve
    sa "Come here, you lovable little you."
    scene ep11_ho_sj2 with dissolve
    js "Had some wine, huh?"
    scene ep11_ho_sj1 with dissolve
    sa "I'm so happy for you guys."
    scene ep11_ho_sj2 with dissolve
    js "Aw, thanks. It feels surreal."
    scene ep11_ho_sj3 with dissolve
    sa "We did it! We're such a dream team."
    if ep8_told_josy_chad:
        scene ep11_ho_sj7 with dissolve
        js "You have to tell me all about it."
        scene ep11_ho_sj5 with dissolve
        sa "I'm gonna, but so much happened."
        sa "Some of it was so fucking sad, too. I mean, Maya's mom... *{i}Sigh{/i}*"
        scene ep11_ho_sj6 with dissolve
        js "Yeah..."
        scene ep11_ho_sj4 with dissolve
        sa "But we pushed through and worked as a team."
        sa "Until [name] got so determined and did it by himself."
        sa "But most of it was teamwork, I think. I helped out, didn't I?"
        scene ep11_ho_sj7 with dissolve
        js "Of course, you did. And you've been so supportive of us... Thank you."
        scene ep11_ho_sj8 with dissolve
        sa "Aw, come here!"
    else:
        scene ep11_ho_sj4 with dissolve
        sa "Technically, those guys are the dream team. But we helped out too, didn't we?"
        scene ep11_ho_sj7 with dissolve
        js "Of course, you did. And you've been so supportive of us... Thank you."
        scene ep11_ho_sj8 with dissolve
        sa "Aw, come here!"
else:
    scene ep11_ho_sj10 with dissolve
    sa "Come here, you lovable little you."
    sa "Let me hug you."
    scene ep11_ho_sj11 with dissolve
    js "Sorry if I'm killing the mood, but it's been a long day."
    scene ep11_ho_sj12 with dissolve
    sa "It sure has."
    sa "Are you not drinking more?"
    scene ep11_ho_sj11 with dissolve
    js "No, I don't want to overdo it. It doesn't feel right."
    scene ep11_ho_sj12 with dissolve
    sa "They say you shouldn't drink when you're sad, but I don't get why not. It makes you feel happier."
    scene ep11_ho_sj11 with dissolve
    js "For a moment, maybe."
    scene ep11_ho_sj16 with dissolve
    sa "Here's to many moments!"
    scene ep11_ho_sj15 with dissolve
    js "..."
    scene ep11_ho_sj13 with dissolve
    if ep8_told_josy_chad:
        sa "What kills me is that we were so close..."
    else:
        sa "What kills me is that they were so close..."
    sa "So close."
    scene ep11_ho_sj15 with dissolve
    js "..."
    scene ep11_ho_sj13 with dissolve
    sa "And we've got nothing to show for it."
    sa "It's the same as it was yesterday, but worse."
    scene ep11_ho_sj14 with dissolve
    js "Not if you ask Maya."
    scene ep11_ho_sj9 with dissolve
    sa "And we had such a great idea, too..."

if not ep8_told_josy_chad:
    jump ep11_ho2_main_label

if ep10_got_contracts:
    scene ep11_ho_sj17 with dissolve
    sa "And what about you? You were the mastermind behind it all!"
else:
    scene ep11_ho_sj19 with dissolve
    sa "And you were the mastermind behind it all!"
if ep10_got_contracts:
    scene ep11_ho_sj21 with dissolve
else:
    scene ep11_ho_sj20 with dissolve
js "Me? Was I?"
scene ep11_ho_sj18 with dissolve
sa "Yes! It was your idea, remember?"
sa "We didn't know how to do it, and you were like, \"Epic brain moment incoming\"!"
if ep10_got_contracts:
    scene ep11_ho_sj17 with dissolve
else:
    scene ep11_ho_sj19 with dissolve
sa "A beard? That was such a good idea. How did you even come up with it?"
if ep10_got_contracts:
    scene ep11_ho_sj21 with dissolve
else:
    scene ep11_ho_sj20 with dissolve
js "Oh, that... [name] was like... Uh..."
if ep10_got_contracts:
    scene ep11_ho_sj17 with dissolve
else:
    scene ep11_ho_sj19 with dissolve
sa "How?"
scene ep11_ho_sj22 with dissolve
js "I...don't know. It just came to me."
if ep10_got_contracts:
    scene ep11_ho_sj17 with dissolve
    sa "It was amazing!"
else:
    scene ep11_ho_sj19 with dissolve
    sa "It was so good. If only it had worked..."
jump ep11_ho2_main_label

label ep11_ho_maya_label:
$ tmp_list[3] = True
scene ep11_ho_maya1 with dissolve
my "[name]..."
my "How can I possibly thank you enough for what you have done for me?"
scene ep11_ho_maya2 with dissolve
if ep10_got_contracts:
    mc "You don't owe me anything, Maya. I'm happy everything will work out. I know you've still got things to deal with, but..."
else:
    mc "You don't owe me anything, Maya. I'm happy you've figured things out. I know you've still got things to deal with, but..."
scene ep11_ho_maya3 with dissolve
my "I know. Me too."
scene ep11_ho_maya2 with dissolve
mc "Let me know if you want to discuss what happened between you and Patrick..."
scene ep11_ho_maya4 with dissolve
my "..."
scene ep11_ho_maya5 with dissolve
mc "I get that it's hard for you and Derek to open up about it."
my "It's been hard, yes. I haven't been able to tell anyone about it, but I've wanted to for so long."
mc "Has Patrick always been this way?"
scene ep11_ho_maya6 with dissolve
my "He's been angry for many years."
my "Especially when he feels like he's losing control over a situation."
my "I push his buttons a lot when I speak up for Mom, but he doesn't always know how to deal with her, which makes me mad."
scene ep11_ho_maya7 with dissolve
mc "That's not a reason for him to abuse you like that. In fact, there's no reason for it."
scene ep11_ho_maya6 with dissolve
my "What he does is... Well, you saw what he did."
my "I wasn't lying when I said he doesn't hit me. But he can grab my arm pretty hard or shove me when he argues... I don't like that."
my "When I was younger, I questioned myself a lot. Like, maybe I did something wrong to deserve it."
my "But I don't think I always did."
scene ep11_ho_maya7 with dissolve
mc "Why haven't you told anyone about it?"
scene ep11_ho_maya8 with dissolve
my "Because it doesn't happen all the time."
my "But mostly because it feels like I would be turning on my family if I did."
my "And I don't want to turn on my family like Dad turned on me."
scene ep11_ho_maya7 with dissolve
mc "For your mom's sake?"
scene ep11_ho_maya6 with dissolve
my "For Mom, too. Yes."
if ep10_patrick_choice == "DIK":
    scene ep11_ho_maya8 with dissolve
    my "Why did you punch him?"
    scene ep11_ho_maya7 with dissolve
    mc "I got so mad when I realized what he'd put you through."
    mc "I wanted to hurt him for hurting you."
    scene ep11_ho_maya10 with dissolve
    my "..."
    scene ep11_ho_maya7 with dissolve
    mc "But after I did, I saw you still care for him... And I felt terrible."
    mc "I couldn't understand how you could still defend him until I talked to Derek."
    scene ep11_ho_maya6 with dissolve
    my "What did Derek say?"
    scene ep11_ho_maya7 with dissolve
    mc "That it's because he's still your dad."
    mc "I try to picture my dad ever doing that to me and how I would react in the same situation, but I can't relate to it."
    mc "Because that's not what a parent should be like to begin with."
    scene ep11_ho_maya10 with dissolve
    my "..."
    scene ep11_ho_maya8 with dissolve
    my "I wish you hadn't done it. But I understand why you did."
elif ep10_patrick_choice == "NEUTRAL":
    scene ep11_ho_maya8 with dissolve
    my "I've never seen anyone stand up to Dad the way you did."
    my "I was scared about how he would react when you called him out like that."
    my "And then he backed off... I think he realized that he did something wrong."
    scene ep11_ho_maya7 with dissolve
    mc "You think?"
    scene ep11_ho_maya6 with dissolve
    my "Then again, I've been hoping he would realize that long ago. Maybe I'm being naive again..."
else:
    scene ep11_ho_maya9 with dissolve
    my "Thank you for handling it so well...when I argued with Dad."
    my "I feel like you disarmed him and made him feel regret."
    my "But maybe that's wishful thinking..."
    scene ep11_ho_maya7 with dissolve
    mc "I was torn about how to act. I was boiling mad on the inside, but it didn't feel like getting angry would accomplish anything."
    mc "And in that split second, I had to think about how it could have affected you. I didn't want to make it worse."

if ep10_patrick_choice != "CHICK":
    scene ep11_ho_maya7 with dissolve
    mc "I hope I didn't make things worse for you by doing that..."
    scene ep11_ho_maya8 with dissolve
    my "I don't think you did. I hope it was a wake-up call for him."
    scene ep11_ho_maya7 with dissolve
    mc "I hope so, too."

scene ep11_ho_maya5 with dissolve
$ renpy.pause()
if branchJill:
    scene ep11_ho_maya11 with dissolve
    $ renpy.pause()
    scene ep11_ho_maya13 with dissolve
    $ renpy.pause()
if branchIsabella:
    scene ep11_ho_maya12 with dissolve
    $ renpy.pause()
    scene ep11_ho_maya13 with dissolve
    $ renpy.pause()
if branchSage:
    scene ep11_ho_maya15 with dissolve
    $ renpy.pause()
    scene ep11_ho_maya14 with dissolve
    $ renpy.pause()

scene ep11_ho_maya16 with dissolve
my "Have I ever told you why I chose to study social work?"
scene ep11_ho_maya17 with dissolve
mc "No, you haven't."
scene ep11_ho_maya16 with dissolve
my "It's because I want to help families in similar situations as mine."
my "I never asked for help, yet that's my calling because I can understand the pain and suffering involved."
scene ep11_ho_maya18 with dissolve
my "And maybe I will have an easier time spotting that it's happening to someone than others would."
my "And I also know that these situations are rarely just black and white. There's a shade of gray that's hard for many to understand."
my "I think you need that kind of understanding to deal with this."
scene ep11_ho_maya16 with dissolve
if ep10_got_contracts:
    if branchMayaJosy:
        my "And now, thanks to you, I get to study it and figure out who I am with you and Josy."
    else:
        my "And now, thanks to you, I get to study it and figure out who I am with Josy."
    my "I want to feel and decide for myself without the layer of fear that Dad would find out."
    scene ep11_ho_maya19 with dissolve
    menu:
        "I'm there for you":
            scene ep11_ho_maya17 with dissolve
            mc "And you truly deserve it. I want to be there with you when you turn this next page."
            if ep10_feelingsForMaya:
                scene ep11_ho_maya22 with dissolve
                my "I want that, too..."
                scene ep11_ho_maya23 with dissolve
                mc "Good..."
            else:
                scene ep11_ho_maya20 with dissolve
                my "You will be."
        "Josy wants that, too":
            scene ep11_ho_maya17 with dissolve
            mc "And you truly deserve it. It's what Josy has wanted for you, too. She's put up with a lot for you."
            scene ep11_ho_maya21 with dissolve
            my "..."
            if ep10_feelingsForMaya:
                scene ep11_ho_maya22 with dissolve
                my "Is that what you feel and want, though?"
                scene ep11_ho_maya23 with dissolve
                mc "Well... You know how I feel about you. But all I want is for you to be happy."
            scene ep11_ho_maya20 with dissolve
            my "Thank you, [name]."
else:
    my "That's why college means a lot to me. And while Dad tries to control my life choices, college is my choice and mine alone."
    my "If I find a way to endure until college is over, I can have anything I want after."
    scene ep11_ho_maya18 with dissolve
    my "And when I look at Mom and see how she endures her suffering... Day after day, she's constantly fighting..."
    my "It's unbelievable how she can keep going, but somehow she manages."
    my "I want to keep going, too. And unlike Mom, I see the day when I can be free ahead of me. So, if I keep going for longer, eventually, it'll be over."
    scene ep11_ho_maya16 with dissolve
    my "And that's why I choose to continue this way."
    my "I'm unsure if Josy can accept that...and it sucks that we still have to hide. But college means too much to me to give it up."
    scene ep11_ho_maya19 with dissolve
    menu:
        "I'll support you":
            scene ep11_ho_maya17 with dissolve
            mc "This will be hard for Josy. I know it."
            mc "As for me, I'll support you in whatever you choose. Even if you'd backpedal in the future, ok?"
            if ep10_feelingsForMaya:
                scene ep11_ho_maya22 with dissolve
                my "You would, wouldn't you?"
                scene ep11_ho_maya23 with dissolve
                mc "All I want is for you to be happy."
        "Don't forget Josy's feelings":
            scene ep11_ho_maya17 with dissolve
            mc "It's great that you know what you want, but don't forget Josy's feelings."
            mc "She's supported you so much and wants to find ways for this to work, too."
            mc "And while you've come to terms with that nothing will change, it feels like she will have a much harder time accepting that."
            scene ep11_ho_maya21 with dissolve
            my "..."
            scene ep11_ho_maya22 with dissolve
            my "I'm not going to forget about her. And I will talk with her."
            my "I'm pushing through with college, and I want to find a way to push through with us, too. I think..."
            scene ep11_ho_maya23 with dissolve
            mc "Good... You should."
            if ep10_feelingsForMaya:
                scene ep11_ho_maya22 with dissolve
                my "You think so?"
                scene ep11_ho_maya23 with dissolve
                mc "Well... You know how I feel about you. But all I want is for you to be happy."
    scene ep11_ho_maya20 with dissolve
    my "Thank you, [name]."
$ new_bio("Maya", "Maya told me she chose to study social work because she saw it as her calling.")
jump ep11_ho2_main_label

label ep11_ho_josy_label:
$ tmp_list[2] = True
if ep10_got_contracts:
    scene ep11_ho_josy11 with dissolve
    mc "How are you feeling?"
    scene ep11_ho_josy12 with dissolve
    js "How am I feeling? I lack the vocabulary to describe it."
    js "\"Relieved\" is one of the words I'd use. \"Surprised\" is another."
    scene ep11_ho_josy13 with dissolve
    mc "Yeah, it was surprising that Patrick lied to Maya like that. But maybe it shouldn't have been, considering how he treats her."
else:
    scene ep11_ho_josy1 with dissolve
    mc "How are you feeling?"
    scene ep11_ho_josy2 with dissolve
    js "Like I'm a ship at sea with my sails up, but there's nor wind nor motion."
    scene ep11_ho_josy1 with dissolve
    mc "That's a vivid description of it..."
    scene ep11_ho_josy3 with dissolve
    js "I flipped through one of Bella's books while we were waiting for you guys to return."
    js "I feel deflated, [name]. And even more so after hearing that Maya wants to call it quits."
    scene ep11_ho_josy4 with dissolve
    js "All this time, whenever I saw her smile after we failed - like we did at the Burkes..."
    js "I thought she was coping, not coming to terms with it."
    scene ep11_ho_josy5 with dissolve
    $ renpy.pause()
    scene ep11_ho_josy6 with dissolve
    js "What am I going to do, [name]? I must be cursed, just like that mariner who shot the albatross."
    scene ep11_ho_josy7 with dissolve
    mc "The what?"
    scene ep11_ho_josy6 with dissolve
    js "Forget it..."
    scene ep11_ho_josy5 with dissolve
    menu:
        "Think about what you want":
            scene ep11_ho_josy8 with dissolve
            mc "Why don't you think about what you want?"
            mc "I know how hard it's been for you to hide the relationship in the past. If this is what's in store for Maya's future, you need to think about what it means for you."
            if branchMayaJosy:
                mc "And what it means for us three."
                scene ep11_ho_josy10 with dissolve
                js "I'm not giving up on us three. No way! We just started."
                scene ep11_ho_josy8 with dissolve
                mc "Well, there you have it."
                scene ep11_ho_josy9 with dissolve
                js "But I didn't expect Maya to give up on fighting for herself. It feels out of the blue to me, but it wasn't sudden to her."
            else:
                scene ep11_ho_josy9 with dissolve
                js "It means more fights between us, doesn't it? Because that's what it has meant in the past."
                scene ep11_ho_josy8 with dissolve
                mc "It doesn't mean it will be that way in the future."
                scene ep11_ho_josy9 with dissolve
                js "I didn't expect Maya to give up fighting for herself. It feels out of the blue to me, but it wasn't to her."
            scene ep11_ho_josy8 with dissolve
            mc "She deserves to be happy. And so do you."
        "Support Maya":
            scene ep11_ho_josy8 with dissolve
            mc "Try to understand and support her through this."
            scene ep11_ho_josy9 with dissolve
            js "I've always been supportive of her, [name]."
            scene ep11_ho_josy8 with dissolve
            mc "I know you have. And now she needs it more than ever."
            scene ep11_ho_josy9 with dissolve
            js "I didn't expect Maya to give up fighting for herself. It feels out of the blue to me, but it wasn't sudden to her."
scene ep11_ho_josy14 with dissolve
js "How was Patrick abusing her? What did you see?"
scene ep11_ho_josy15 with dissolve
mc "He grabbed her arm hard and shook her as he yelled at her. Maya stood up for her mom because she felt Patrick didn't know how to treat her."
mc "And it's not the first time he's done that to Maya and Derek."
scene ep11_ho_josy16 with dissolve
js "..."
scene ep11_ho_josy14 with dissolve
js "Did you know about this before?"
scene ep11_ho_josy15 with dissolve
mc "No. She never told me, but it dawned on me as I saw it happening. I think she tried to tell me in the past."
scene ep11_ho_josy14 with dissolve
js "She never told me either. And I thought we shared everything."
scene ep11_ho_josy16 with dissolve
menu:
    "You hid me from each other":
        scene ep11_ho_josy15 with dissolve
        mc "Not everything. Both of you hid me from each other."
        scene ep11_ho_josy17 with dissolve
        js "Yeah, but this...? It's hard to see why she'd keep it from me. It hurts."
    "It surprised you, huh?":
        scene ep11_ho_josy15 with dissolve
        mc "It surprised you, huh?"
        scene ep11_ho_josy17 with dissolve
        js "It hurt me... Both that Patrick would do that to her and that she never told me."
scene ep11_ho_josy15 with dissolve
mc "I don't think I should speak on Maya's behalf."
mc "Ask her about this when you see fit."
if ep10_got_contracts:
    scene ep11_ho_josy21 with dissolve
    js "I will, but not tonight. I want her to have this victory."
    scene ep11_ho_josy22 with dissolve
    mc "It's a victory for you, too."
    scene ep11_ho_josy21 with dissolve
    js "Believe me, I'm trying my best to enjoy it."
    if branchMayaJosy:
        scene ep11_ho_josy24 with dissolve
        js "You're awesome..."
        scene ep11_ho_josy23 with dissolve
        $ renpy.pause()
else:
    scene ep11_ho_josy16 with dissolve
    $ renpy.pause()
    scene ep11_ho_josy15 with dissolve
    mc "Can I do something for you?"
    if branchMayaJosy:
        scene ep11_ho_josy20 with dissolve
        js "Hold me for a while?"
        scene ep11_ho_josy23 with dissolve
        $ renpy.pause()
    elif ep10_feelingsForJosy:
        scene ep11_ho_josy18 with dissolve
        js "Like what?"
        scene ep11_ho_josy19 with dissolve
        mc "Whatever you need. If I can help you see things clearly or figure out how you feel..."
        scene ep11_ho_josy18 with dissolve
        js "Thanks, but you already have."
        scene ep11_ho_josy19 with dissolve
        mc "Ok... Good."
        scene ep11_ho_josy23 with dissolve
        js "(More than you'd ever know.)"
    else:
        scene ep11_ho_josy14 with dissolve
        js "Not at the moment."
        scene ep11_ho_josy15 with dissolve
        mc "Ok, I'll be here when you need me."
$ new_bio("Josy", "Josy had a hard time understanding why Maya hid Patrick's domestic abuse from her.")
jump ep11_ho2_main_label

label ep11_ho_josy2_label:
$ tmp_list[2] = True
scene ep11_ho_josy25 with dissolve
js "I need to talk to you."
stop music fadeout 5
scene ep11_ho_josy26 with dissolve
mc "Wanna go somewhere private?"
play music "music/ep1/windswept.mp3"
scene ep11_ho_josy27 with dissolve
$ renpy.pause()
scene ep11_ho_josy28
show screen ep10_snow_screen
with dissolve
mc "..."
scene ep11_ho_josy29
hide screen ep10_snow_screen
with dissolve
$ renpy.pause()
scene ep11_ho_josy30 with dissolve
js "..."
scene ep11_ho_josy31 with dissolve
if ep10_got_contracts:
    js "Thank you for helping Maya."
    scene ep11_ho_josy32 with dissolve
    mc "You're welcome."
    mc "It wasn't just for Maya. It was for you too."
    scene ep11_ho_josy33 with dissolve
    js "I know."
else:
    js "I know things didn't work out as planned tonight...but thanks for trying."
    scene ep11_ho_josy32 with dissolve
    mc "I feel like I failed her... And I feel like I failed you."
    scene ep11_ho_josy33 with dissolve
    js "You're not just talk, though. You tried your best."

scene ep11_ho_josy34 with dissolve
js "I'm still mad at you."
scene ep11_ho_josy35 with dissolve
mc "I know."
mc "And you have every right to be mad."
mc "But I hope that one day, someday, any day, you won't be. And that we can patch things up between us."
mc "I'm still sad about us and how it ended."
scene ep11_ho_josy36 with dissolve
js "You should be. You missed out on something real, I hope you know."
scene ep11_ho_josy35 with dissolve
mc "..."
scene ep11_ho_josy36 with dissolve
js "I can't promise I will ever be ok with what you did. But I'm not blind..."
js "I see what you're doing. I see how much you care."
scene ep11_ho_josy39 with dissolve
js "Fuck!"
scene ep11_ho_josy37 with dissolve
js "..."
scene ep11_ho_josy38 with dissolve
js "I am grateful for that. But I am also still very mad."
scene ep11_ho_josy40 with dissolve
$ renpy.pause()
if branchJill and not branchMayaJosy:
    scene ep11_ho_josy38 with dissolve
    js "It will be hard to see you together with Jill."
    js "*{i}Sigh{/i}*"
elif branchSage and not branchMayaJosy:
    scene ep11_ho_josy38 with dissolve
    js "It will be hard to see you together with Sage."
    js "*{i}Sigh{/i}*"
elif branchIsabella and not branchMayaJosy:
    scene ep11_ho_josy38 with dissolve
    js "It will be hard to see you together with Bella."
    scene ep11_ho_josy44 with dissolve
    mc "Did...Maya tell you?"
    scene ep11_ho_josy41 with dissolve
    js "So, Maya knows..."
    js "No. I overheard Jill and Bella talking about it."
    js "I can't even find the words to discuss that with you; frankly, I don't want to."
    scene ep11_ho_josy43 with dissolve
    mc "Can you avoid spreading it...please?"
    scene ep11_ho_josy42 with dissolve
    js "*{i}Sigh{/i}* From the looks of it, I have to."
    scene ep11_ho_josy43 with dissolve
    mc "Thank you..."

scene ep11_ho_josy45 with dissolve
js "How was Patrick abusing Maya?"
mc "He grabbed her arm real hard and shook her as he yelled at her. Maya was standing up for her mom because she felt Patrick didn't know how to treat her."
mc "And it's not the first time he's done that to Maya and Derek."
scene ep11_ho_josy46 with dissolve
js "..."
scene ep11_ho_josy47 with dissolve
js "Did you know about this?"
scene ep11_ho_josy46 with dissolve
mc "No. She never told me, but it dawned on me as I saw it happening. I think she tried to tell me in the past."
scene ep11_ho_josy48 with dissolve
js "She never told me either. And I thought we shared everything."
scene ep11_ho_josy46 with dissolve
menu:
    "You hid me from each other":
        mc "Not everything. Both of you hid me from each other."
        scene ep11_ho_josy47 with dissolve
        js "Yeah, but this...? It's hard to see why she'd keep it from me. It hurts."
    "It surprised you, huh?":
        mc "It surprised you, huh?"
        scene ep11_ho_josy47 with dissolve
        js "It hurt me... Both that Patrick would do that to her and that she never told me."
scene ep11_ho_josy46 with dissolve
mc "I don't think I should speak on Maya's behalf about this."
mc "Ask her about it when you see fit."
if ep10_got_contracts:
    scene ep11_ho_josy48 with dissolve
    js "I will, but not tonight. I want her to have this victory."
    scene ep11_ho_josy46 with dissolve
    mc "It's a victory for you too."
    scene ep11_ho_josy48 with dissolve
    js "I'm trying to enjoy it."
scene ep11_ho_josy49 with dissolve
$ renpy.pause()
scene ep11_ho_josy50 with dissolve
mc "Thank you for talking to me again. You're strong for doing that."
scene ep11_ho_josy51 with dissolve
js "Right..."
stop music fadeout 3
scene ep11_ho_josy50 with dissolve
mc "You might not feel like it, but really... You are."
scene ep11_ho_josy52 with dissolve
$ renpy.pause()
play music "music/ep11/licensed_music/track163.mp3"
queue music ["music/ep11/licensed_music/track164.mp3","music/ep11/licensed_music/track163.mp3"]
$ new_bio("Josy", "Josy had a hard time understanding why Maya hid Patrick's domestic abuse from her.")
$ new_bio("Josy", "Josy thanked me for helping Maya and her. She told me she was still mad, but at least she talked to me.")
jump ep11_ho2_main_label

label ep11_ho_bella_label:
$ tmp_list[1] = True
if ep10_got_contracts:
    scene ep11_ho_bella1 with dissolve
    isa "Do I want to know how you managed to get a hold of those papers, or would that make me your accomplice?"
    scene ep11_ho_bella3 with dissolve
    mc "We left their house, but I went back there and snuck inside without Patrick noticing me."
    mc "I went into his office and rummaged around, but in a delicate way. I wasn't throwing any papers around and tried my best not to leave a trace."
    if affinity == "DIK":
        mc "There was even a blank whiteboard in there that I almost drew a cock on, but I stopped myself from doing it."
        scene ep11_ho_bella4 with dissolve
        isa "Oh, you poor thing."
        scene ep11_ho_bella3 with dissolve
        mc "I know, right?"
        if ep8_maya_lewd:
            mc "I've already learned my lesson about messing around with whiteboards."
            scene ep11_ho_bella5 with dissolve
            isa "Hm?"
            scene ep11_ho_bella6 with dissolve
            mc "Nothing..."
        else:
            scene ep11_ho_bella6 with dissolve
    else:
        scene ep11_ho_bella6 with dissolve
    mc "He has a lot of binders, and I went through several of them before finding the right one."
    mc "I read through a bunch of papers before I located the contract, and then I left without him knowing I was there."
    mc "You should have seen me; I was a smooth operator."
    scene ep11_ho_bella5 with dissolve
    isa "Ok, this does make me your accomplice. I will pretend I didn't hear a word of what you just said."
    scene ep11_ho_bella6 with dissolve
    mc "It felt scummy, but I had to do it for Maya."
    scene ep11_ho_bella7 with dissolve
    isa "You're a wonderful friend to have - larceny put aside."
    scene ep11_ho_bella6 with dissolve
    mc "Haha! You're right. I am pretty damned wonderful."
    scene ep11_ho_bella8 with dissolve
    isa "Ok, now you're pushing it."
    $ new_bio("Isabella", "Bella praised me for helping Maya.")
else:
    scene ep11_ho_bella2 with dissolve
    isa "Do you want to talk about it?"
    scene ep11_ho_bella9 with dissolve
    mc "About how I failed to do what Maya trusted me to do? Not really."
    scene ep11_ho_bella11 with dissolve
    isa "You're being overly harsh on yourself."
    scene ep11_ho_bella9 with dissolve
    mc "I feel like I let her down. It was harder than I thought it would be."
    scene ep11_ho_bella11 with dissolve
    isa "Things don't always go according to plan, and while it sounded good in theory, there was always a risk that something would go wrong."
    scene ep11_ho_bella10 with dissolve
    mc "Yeah, but it sucks... I was right there. It was almost within reach, but I couldn't get it."
    scene ep11_ho_bella12 with dissolve
    isa "There are likely other ways to solve this that don't involve theft."
    scene ep11_ho_bella9 with dissolve
    mc "Yeah, but she doesn't want to risk anything for her mom's sake."
    scene ep11_ho_bella12 with dissolve
    isa "What do you mean?"
    scene ep11_ho_bella9 with dissolve
    mc "Her mom, Helen, is chronically ill and depends on Patrick. Maya fears confronting him about this will make her parents' relationship worse."
    scene ep11_ho_bella10 with dissolve
    mc "Even though Patrick treats Maya badly, she still thinks about what's best for her family."
    mc "How is she able to do that? I don't think I could do it."
    scene ep11_ho_bella11 with dissolve
    isa "That says a lot about her. Putting others before herself like that."
    scene ep11_ho_bella9 with dissolve
    mc "It sure does."
    scene ep11_ho_bella12 with dissolve
    isa "Anyway, you can't expect to be able to solve everyone's problems. You're only human."
    scene ep11_ho_bella11 with dissolve
    isa "The important thing is that you care and show compassion. That's what she needs now and will remember."
    isa "And if you want to help Maya more, put your energy into making her college stay a happy one. I think it can be."
    $ new_bio("Isabella", "Bella tried to comfort me after I failed to help Maya with the contract.")

if branchIsabella:
    scene ep11_ho_bella13 with dissolve
    mc "How were things on your end tonight?"
    scene ep11_ho_bella14 with dissolve
    isa "It was a slow night waiting for you guys."
    scene ep11_ho_bella13 with dissolve
    mc "Did you talk to Jill, or was it hard getting a chance to do it?"
    scene ep11_ho_bella15 with dissolve
    isa "We...um...talked some."
    scene ep11_ho_bella16 with dissolve
    mc "Did it go well?"
    scene ep11_ho_bella15 with dissolve
    isa "Mhm. More or less. We had a good talk."
    scene ep11_ho_bella16 with dissolve
    mc "Good... I'm glad."
    scene ep11_ho_bella17 with dissolve
    isa "..."
jump ep11_ho2_main_label

label ep11_ho_sage_label:
$ tmp_list[0] = True
scene ep11_ho_sage1 with dissolve
sa "This song is so good..."
scene ep11_ho_sage2 with dissolve
$ renpy.pause()
scene ep11_ho_sage3 with dissolve
sa "Maya, dance with me!"
if ep10_got_contracts:
    scene ep11_ho_sage4 with dissolve
    my "Maybe later. I'm enjoying my wine here."
    scene ep11_ho_sage3 with dissolve
    sa "Drink faster!"
    scene ep11_ho_sage4 with dissolve
    my "Who drinks wine fast?"
    scene ep11_ho_sage3 with dissolve
    sa "Good point! We should make sangrias!"
else:
    scene ep11_ho_sage5 with dissolve
    my "I'm not in a dancing mood tonight."
    scene ep11_ho_sage3 with dissolve
    sa "Dancing makes you feel happier even when you're sad, just like wine!"
    scene ep11_ho_sage5 with dissolve
    my "Maybe later."

scene ep11_ho_sage6 with dissolve
sa "Jill, get your butt up here and show me your best moves."
scene ep11_ho_sage7 with dissolve
ji "None of my moves are that good."
scene ep11_ho_sage8 with dissolve
sa "Come on, that's horse crap! I'm sure you've got some killer ones. I saw you dance on Halloween!"
scene ep11_ho_sage9 with dissolve
sa "Look, even Bella is dancing."
scene ep11_ho_sage10 with dissolve
isa "What? Did you think of me as the least likely to dance?"
scene ep11_ho_sage11 with dissolve
sa "Haha! Not anymore!"
scene ep11_ho_sage12 with dissolve
$ renpy.pause()
if ep8_told_josy_chad:
    scene ep11_ho_sage13 with dissolve
    sa "Hubby!"
    de "Hey..."
    scene ep11_ho_sage14 with dissolve
    de "Listen, I owe you an apology for earlier. You did great today."
    de "And I...uh... Perhaps I'm more likely to have a friend who's a girl than I thought."
    scene ep11_ho_sage15 with dissolve
    sa "Thanks, hubby!"
scene ep11_ho_sage16 with dissolve
sa "Guys! Guys! We should do this every weekend!"
scene ep11_ho_sage17 with dissolve
isa "Every weekend? I'm not in college anymore."
scene ep11_ho_sage16 with dissolve
sa "No, but for real! We should party and celebrate things together!"
if not ep10_got_contracts:
    sa "Not that tonight is a celebration, but you get my drift."
scene ep11_ho_sage18 with dissolve
ji "What are you talking about?"
scene ep11_ho_sage16 with dissolve
sa "Christmas! We should celebrate Christmas! And New Year's! And birthdays!!!"
scene ep11_ho_sage17 with dissolve
isa "I'm sure you celebrate that with family and relatives."
scene ep11_ho_sage19 with dissolve
sa "*{i}Groans{/i}*"

scene ep11_ho_sage20 with dissolve
sa "[name]! If you don't dance, you're a party pooper."
scene ep11_ho_sage21 with dissolve
mc "Are you still dancing?"
if ep10_got_contracts:
    mc "You can dance extra for me. It's nice to see that you're having fun."
else:
    mc "You can dance extra for me; I'm not feeling it tonight."
if ep10_got_contracts:
    scene ep11_ho_sage22 with dissolve
    sa "You did amazing tonight, [name]. Like, wow."
    sa "I hoped you'd make it, but I was still surprised when you did."
    scene ep11_ho_sage23 with dissolve
    mc "Yeah, I got lucky."
    scene ep11_ho_sage22 with dissolve
    sa "You didn't get lucky. Don't give luck any credit; it was all you!"
    if not ep8_told_josy_chad:
        sa "Derek recounted how you did it, and I was in awe."
    sa "You've got such big balls for doing that."
else:
    scene ep11_ho_sage22 with dissolve
    sa "Chin up. You did all that you could. No one blames you for this."
    scene ep11_ho_sage23 with dissolve
    mc "I blame myself."
    scene ep11_ho_sage22 with dissolve
    sa "Then you should listen to what we tell you. It's not your fault."

scene ep11_ho_sage24 with dissolve
sa "Come here."
scene ep11_ho_sage26 with dissolve
sa "I'm so happy we're all here like this."
if ep10_got_contracts:
    sa "Everyone is helping out and being there for each other. I think that's amazing."
else:
    sa "Even if it didn't go according to plan, we're still here for each other. I think that's amazing."
scene ep11_ho_sage25 with dissolve
mc "That does feel good."
scene ep11_ho_sage26 with dissolve
sa "We're like a big, true family."
scene ep11_ho_sage27 with dissolve
sa "*{i}Sniffles{/i}*"
mc "Sage?"
scene ep11_ho_sage28 with dissolve
mc "(She's trembling...)"
scene ep11_ho_sage29 with dissolve
mc "Follow me."
stop music fadeout 5
scene ep11_ho_sage30 with dissolve
$ renpy.pause()
play music "music/ep5/inspiring.mp3"
scene ep11_ho_sage33 with dissolve
mc "How are you? What's wrong?"
scene ep11_ho_sage34 with dissolve
sa "It's my parents. They're getting divorced."
scene ep11_ho_sage35 with dissolve
mc "What? Oh, no..."
if ep4_fuckedJade:
    scene ep11_ho_sage36 with dissolve
    mc "(This doesn't have anything to do with me...right?)"
    scene ep11_ho_sage35 with dissolve
mc "What happened?"
scene ep11_ho_sage34 with dissolve
sa "They've always been fighting. It's something I've seen like a million times."
sa "And I've heard Mom threaten Dad with divorce when she got mad, but I never thought it would happen."
scene ep11_ho_sage37 with dissolve
sa "It was just empty threats like, \"If you don't shut up, I'll turn this car around, and we're not going\"."
sa "But now it is happening for real, and I don't know what to do about it."
scene ep11_ho_sage38 with dissolve
mc "What can I tell you...?"
mc "These things happen. And it's sad when it affects kids, but..."
mc "If they've been fighting a lot, they're unhappy, right?"
scene ep11_ho_sage39 with dissolve
sa "I think so, yeah. I can't remember the last time I heard Dad laugh."
scene ep11_ho_sage38 with dissolve
mc "Then, which is better: being unhappy and staying together or splitting up and trying to find happiness?"
scene ep11_ho_sage39 with dissolve
sa "I know what you're saying, but for me, it hurts so damned much because..."
scene ep11_ho_sage40 with dissolve
sa "*{i}Exhales{/i}*"
sa "I didn't think I'd lose two families in my lifetime."
sa "I thought this family was my forever one - the one I deserved."
scene ep11_ho_sage38 with dissolve
mc "You haven't lost them. They're still your family."
mc "Even if things will be different, your mom is still your mom, and your dad is still your dad."
scene ep11_ho_sage41 with dissolve
$ renpy.pause()
scene ep11_ho_sage42 with dissolve
mc "And unfortunately, your brother is still your brother."
scene ep11_ho_sage43 with dissolve
sa "Hahaha!"
scene ep11_ho_sage44 with dissolve
if affinity == "DIK":
    mc "Chin up. You're not alone."
else:
    if ep8_told_josy_chad:
        mc "It's ok to feel sad. I could tell that something was bothering you today. And let me say I'm amazed you managed to pull through like you did."
    else:
        mc "It's ok to feel sad. I could tell that something was bothering you today. And let me say how strong you are for still wanting to come here."
    mc "You're strong as hell, Sage. Don't forget that. You'll be able to handle this, ok?"
    scene ep11_ho_sage45 with dissolve
    mc "And if you need my shoulder, ear, or anything... I'm always here for you."
if branchSage:
    $ ep11_kissed_sage = True
    scene anim_sage_kiss_ep11 with dissolve
    sa "*{i}Smack{/i}* Mmm..."
    pause
    scene ep11_ho_sage52 with dissolve
    sa "I'm so happy I met you. Thank you, [name]. Thank you."
    if affinity != "DIK":
        scene ep11_ho_sage53 with dissolve
        mc "*{i}Smack{/i}*"
    scene ep11_ho_sage51 with dissolve
    mc "I know something that might take your mind off things..."
    mc "What if you came back home with me tomorrow? You could meet Dad and see where I grew up."
    scene ep11_ho_sage52 with dissolve
    sa "I'd like that."
    scene ep11_ho_sage51 with dissolve
    mc "Yeah?"
    scene ep11_ho_sage52 with dissolve
    sa "Yes."
    scene ep11_ho_sage46 with dissolve
    $ renpy.pause()
    scene ep11_ho_sage48 with dissolve
    mc "Wanna head back?"
    stop music fadeout 3
    scene ep11_ho_sage47 with dissolve
    sa "Yeah."
else:
    if branchIsabella or branchAlone:
        scene ep11_ho_sage54 with dissolve
        if branchIsabella:
            $ renpy.pause()
            jump ep11_ho_stop_kiss_label
        else:
            if persistent.mod_wtenabled:
                        $mod_choices = ["(Kissed Sage)","(-DIKS)","(-DIK)","(+DIK)","(+5 Josy)","(-5 Josy)","","","","","","" ]
                        #[mod_gr][mod_choices[0]]
                        #\n{size=-4}[m_c1][mod_choices[1]][m_c2][mod_choices[4]]
                        if not branchAlone:
                           $ mod_choices[6]="(+Cheater)"
                           $ mod_choices[7]="(+5 Cheater)"
            menu:
                "Stop her":
                    label ep11_ho_stop_kiss_label:
                    scene ep11_ho_sage49 with dissolve
                    mc "Oh... Um... Not in that way."
                    scene ep11_ho_sage50 with dissolve
                    sa "I'm sad and drunk. I'm looking for comfort; can't you give me that?"
                    scene ep11_ho_sage49 with dissolve
                    mc "I can. But not in that way..."
                    scene ep11_ho_sage46 with dissolve
                    $ renpy.pause()
                    scene ep11_ho_sage47 with dissolve
                    sa "Ok..."
                "Kiss her back \n{size=-4}[m_c1][mod_choices[0]]":
                    $ ep11_kissed_sage = True
                    scene anim_sage_kiss_ep11 with dissolve
                    sa "*{i}Smack{/i}* Mmm..."
                    pause
                    scene ep11_ho_sage50 with dissolve
                    sa "Um... Sorry... I'm sad, drunk, and looking for comfort... I shouldn't use you like this."
                    scene ep11_ho_sage49 with dissolve
                    mc "It's ok."
                    scene ep11_ho_sage46 with dissolve
                    $ renpy.pause()
            scene ep11_ho_sage48 with dissolve
            mc "Wanna head back?"
            stop music fadeout 3
            scene ep11_ho_sage47 with dissolve
            sa "Yeah."
    else:
        scene ep11_ho_sage46 with dissolve
        $ renpy.pause()
        scene ep11_ho_sage47 with dissolve
        sa "Thank you, [name]."
        scene ep11_ho_sage48 with dissolve
        mc "Wanna head back?"
        stop music fadeout 3
        scene ep11_ho_sage47 with dissolve
        sa "Yeah."

play music "music/ep11/licensed_music/track164.mp3"
queue music ["music/ep11/licensed_music/track163.mp3","music/ep11/licensed_music/track164.mp3"]
scene ep11_ho_sage31 with dissolve
isa "Sage? Are you ok?"
scene ep11_ho_sage32 with dissolve
sa "No. I'm sorry for weirding you guys out tonight."
scene ep11_ho_sage31 with dissolve
isa "Come here. You didn't weird anyone out. Tell me what's wrong."
$ new_bio("Sage", "Sage told me her parents were getting divorced and that she felt like she was losing her family.")
jump ep11_ho2_main_label

label ep11_ho_derek_label:
$ tmp_list[4] = True
scene ep11_ho_derek1 with dissolve
mc "Feeling better?"
scene ep11_ho_derek2 with dissolve
de "Yeah."
de "Maybe it's pompous to say cheers with wine, but...cheers."
play sound "sound_effects/bottle_clink.mp3"
scene ep11_ho_derek3 with dissolve
mc "At least it's less pompous than cheering with Earl Teabag. Cheers!"
scene ep11_ho_derek2 with dissolve
de "Good ole Earl... Speaking of him, I like that top hat... But it's hard finding opportunities to wear it."
scene ep11_ho_derek4 with dissolve
mc "Bro, you wore a dildo helmet to school... Just wear that stupid top hat whenever you want."
scene ep11_ho_derek5 with dissolve
de "Man's got a point."
scene ep11_ho_derek6 with dissolve
mc "Where's your head at tonight?"
if ep10_got_contracts:
    scene ep11_ho_derek7 with dissolve
    de "I haven't had enough time to process everything. But my gut says things will be good."
else:
    scene ep11_ho_derek8 with dissolve
    de "You know how I feel about it all. I'll support her no matter what she decides."
scene ep11_ho_derek6 with dissolve
mc "Are you worried that something will happen with your dad?"

scene ep11_ho_derek8 with dissolve
de "I've been worried since I came here. I've learned how to live with that feeling."
scene ep11_ho_derek6 with dissolve
mc "Now that I know you're not here to study, I will feel less bad about not sitting next to you in class."
scene ep11_ho_derek7 with dissolve
de "You do you, [mc_de]. I don't want you to feel like I'm dragging you down with me if you want to be a nerd."
de "But I'll still save you a seat while I'm here."
scene ep11_ho_derek9 with dissolve
$ renpy.pause()

scene ep11_ho_derek14 with dissolve
isa "It is snowing a lot."
scene ep11_ho_derek10 with dissolve
mc "I hope it stops snowing before we leave because I didn't bring a jacket."
scene ep11_ho_derek15 with dissolve
isa "Why wouldn't you bring a jacket? You could get pneumonia."
scene ep11_ho_derek10 with dissolve
mc "Because I'm wearing this warm sweater, and it wasn't cold when we left earlier today."
scene ep11_ho_derek15 with dissolve
isa "But it's cold now. Did you not think that this would take you all evening?"
scene ep11_ho_derek11 with dissolve
de "Hey, back off him! I only brought a vest, and that's not much better."
scene ep11_ho_derek16 with dissolve
isa "So, your defense of [name] is that you make stupid choices, too?"
scene ep11_ho_derek12 with dissolve
de "You're goddamned right."
scene ep11_ho_derek16 with dissolve
isa "You're lucky I care enough to drive anyone who needs it back home."
scene ep11_ho_derek13 with dissolve
de "Then you shouldn't drink more wine."
de "Kind of irresponsible, don't you think?"
show ep11_ho_derek17
if not persistent.ep11_cardly3:
    show screen ep11_render_screen("ly3")
with dissolve
isa "Or maybe I'll finish this bottle of wine and drive you back home tomorrow."
show ep11_ho_derek6
hide screen ep11_render_screen
with dissolve
mc "Bro, don't push it... I need to get back home tonight."
scene ep11_ho_derek7 with dissolve
de "It's fine; I'll drive you. I'm just having small sips."
jump ep11_ho_sj_label

label ep11_ho_jill_label:
$ tmp_list[5] = True
scene ep11_ho_jill1 with dissolve
if ep10_got_contracts:
    mc "I want to thank you for offering to help Maya with her loans."
    scene ep11_ho_jill2 with dissolve
    ji "It's not a problem. I'd just be giving her advice on how to do it."
    scene ep11_ho_jill1 with dissolve
    mc "Yeah, but your support means a lot to her."
else:
    mc "I want to thank you for your help."
    scene ep11_ho_jill2 with dissolve
    ji "It doesn't quite feel like I've helped her."
    scene ep11_ho_jill1 with dissolve
    mc "I know what you mean, but your support means a lot to her."
scene ep11_ho_jill2 with dissolve
ji "Thanks. As does yours; it's easy to tell."
if branchJill and ep9_jm_sad:
    scene ep11_ho_jill3 with dissolve
    ji "I feel weird since I know that you've...dated her. But I can see why you care."
    ji "You've got a big heart."
    scene ep11_ho_jill4 with dissolve
    mc "And for you being able to look past what she's been to me..."
    mc "It's quite amazing."
    scene ep11_ho_jill3 with dissolve
    ji "I trust you. That's why I can do that."
    scene ep11_ho_jill5 with dissolve
    mc "Thank you."


scene ep11_ho_jill6 with dissolve
mc "What were you guys up to tonight?"
scene ep11_ho_jill7 with dissolve
ji "It was such a slow night. We had dinner, but mostly, we were waiting for you to show up."
ji "It wasn't a traditional Thanksgiving by any means, but Thanksgiving has always felt weird to me."
scene ep11_ho_jill6 with dissolve
if branchJill:
    mc "Because of Lana?"
    scene ep11_ho_jill7 with dissolve
    ji "Yes."
else:
    mc "Why's that?"
    scene ep11_ho_jill7 with dissolve
    ji "Because of my sister."
ji "Her birthday is in December. She passed away the week before it."
scene ep11_ho_jill8 with dissolve
ji "For a holiday with the purpose of giving thanks, it has felt like a yearly slap in the face to my family."
ji "There hasn't been much to be thankful for. That's why we don't celebrate it."
scene ep11_ho_jill14 with dissolve
mc "I thought you said you celebrated it with Bella."
scene ep11_ho_jill7 with dissolve
ji "I did say that. We managed to turn it into something good."
ji "Together, we realized there are things to be thankful for, even when hurting."
scene ep11_ho_jill15 with dissolve
ji "And it's good to appreciate the little things in life."
ji "In my memories of my sister, the little things we did together ended up being the big things I remember her for."
scene ep11_ho_jill6 with dissolve
mc "That sounds sweet."
if branchJill:
    scene ep11_ho_jill16 with dissolve
    ji "Would you like to come with me when I visit her grave?"
    scene ep11_ho_jill17 with dissolve
    mc "Are you sure you'd want that? It sounds like it's personal to you."
    scene ep11_ho_jill16 with dissolve
    ji "It is. But she never got to meet you. And this is as close as it gets."
    ji "It would mean a lot to me."
    scene ep11_ho_jill17 with dissolve
    mc "I wouldn't want to miss it."
    scene ep11_ho_jill13 with dissolve
    $ renpy.pause()
    scene ep11_ho_jill18 with dissolve
    ji "What about your Thanksgivings? Tell me. How have they been?"
    scene ep11_ho_jill19 with dissolve
    mc "They've been ordinary and laid back. Dad and I usually share a good meal, but that's pretty much it."
    scene ep11_ho_jill18 with dissolve
    ji "You don't watch the game or something?"
    scene ep11_ho_jill19 with dissolve
    mc "No TV, remember?"
    scene ep11_ho_jill20 with dissolve
    ji "I...don't remember you telling me that."
    scene ep11_ho_jill19 with dissolve
    mc "Oh, I'm sorry. I thought I did. I never had one growing up."
    scene ep11_ho_jill21 with dissolve
    ji "Ah... It would be hard to watch the game without one."
    scene ep11_ho_jill22 with dissolve
    mc "Haha, yeah."
    scene ep11_ho_jill23 with dissolve
    mc "Um... Here's a thought... Would you like to come back home with me tomorrow?"
    scene ep11_ho_jill25 with dissolve
    ji "For your Thanksgiving celebration?"
    scene ep11_ho_jill24 with dissolve
    mc "\"Celebration\" is a strong word for it. But yeah, I'm sure Dad would love to meet you."
    scene ep11_ho_jill25 with dissolve
    ji "I'd be delighted to, if it's ok with this short notice."
    scene ep11_ho_jill24 with dissolve
    mc "Yeah, it won't be a problem. Trust me."
    mc "I'll be staying over until Sunday; are you up for that?"
    scene ep11_ho_jill26 with dissolve
    ji "Oh... I made plans with Sage on Saturday."
    scene ep11_ho_jill27 with dissolve
    mc "With Sage?"
    scene ep11_ho_jill26 with dissolve
    ji "Yes, I'm sorry. But I can stay overnight, at least."
    scene ep11_ho_jill27 with dissolve
    mc "That will work, too."
    scene ep11_ho_jill25 with dissolve
    ji "Great!"
    scene ep11_ho_jill24 with dissolve
    mc "You and Sage, huh? What are you two up to?"
    scene ep11_ho_jill28 with dissolve
    ji "She wanted me to show her where I get my nails done, and I suggested we could make a day out of it."
    scene ep11_ho_jill29 with dissolve
    mc "That's so nice of you. She could use it."
    mc "I mean, not that her nails are ugly, but she could use some time off thinking about her parents."
    scene ep11_ho_jill30 with dissolve
    ji "Haha, [name]... I got what you meant."
    scene ep11_ho_jill31 with dissolve
    mc "Ok. Good."
    $ new_bio("Jill", "Jill asked me to come with her to Lana's grave to \"meet\" Lana.")
elif branchIsabella:
    if ep9_b_kissed_jill:
        scene ep11_ho_jill16 with dissolve
        ji "Would you like to come with me when I visit her grave?"
        scene ep11_ho_jill17 with dissolve
        mc "You'd...want me to come?"
        scene ep11_ho_jill7 with dissolve
        ji "It would mean a lot to me to show you."
        scene ep11_ho_jill17 with dissolve
        mc "If it's important to you, I wouldn't want to miss it."
        scene ep11_ho_jill13 with dissolve
        $ renpy.pause()
        $ new_bio("Jill", "Jill asked me to come with her to Lana's grave to \"meet\" Lana.")
    scene ep11_ho_jill7 with dissolve
    ji "I'm happy I came here tonight."
    scene ep11_ho_jill13 with dissolve
    mc "I am, too. And Bella as well, I'm sure."
    scene ep11_ho_jill8 with dissolve
    ji "We've been through a lot together, her and I."
    ji "I would never have guessed that you'd be the test of our friendship."
    scene ep11_ho_jill9 with dissolve
    mc "I feel bad about that. It was never my intention to cause issues between you."
    scene ep11_ho_jill8 with dissolve
    ji "I know."
    if ep9_b_kissed_jill:
        scene ep11_ho_jill10 with dissolve
        $ renpy.pause()
        scene ep11_ho_jill11 with dissolve
        $ renpy.pause()
    scene ep11_ho_jill12 with dissolve
    ji "I'm not going to lose her. That's what I have decided."
    scene ep11_ho_jill13 with dissolve
    $ renpy.pause()
else:
    scene ep11_ho_jill13 with dissolve
    $ renpy.pause()
jump ep11_ho2_main_label

label ep11_ho_main_party_label:
$ renpy.block_rollback()

if ep11_bp_won_bella:
    scene ep11_main2_party129 with dissolve
else:
    scene ep11_main2_party128 with dissolve

show white_screen with dissolve
show text "{font=fonts/collegiate.ttf}{size=+%d}{color=#fe961b}Hangout:{/color} Isabella's home{/size}{/font}" % (40 * persistent.scale_factor):
    yalign 0.84
    xalign 0.5
$ renpy.pause()
hide text
hide white_screen
$ tmp_list = [False, False, False, False, False]

label ep11_ho2_main_party_label:

$ renpy.block_rollback()
$ currentFreeRoamLabel = "ep11_ho2_main_party_label"

if False not in tmp_list:
    jump ep11_main2_party_end_label
if ep11_bp_won_bella:
    scene ep11_main2_party129 with dissolve

    if not tmp_list[0]:
        $ ui.imagebutton("ep11_ho_party_sageb_idle", "ep11_ho_party_sageb_hover", clicked=ui.returns("sage"), xpos=0, ypos=0, focus_mask=True)
    if not tmp_list[1]:
        $ ui.imagebutton("ep11_ho_party_mayab_idle", "ep11_ho_party_mayab_hover", clicked=ui.returns("maya"), xpos=0, ypos=0, focus_mask=True)
    if not tmp_list[2]:
        $ ui.imagebutton("ep11_ho_party_josyb_idle", "ep11_ho_party_josyb_hover", clicked=ui.returns("josy"), xpos=0, ypos=0, focus_mask=True)
    if not tmp_list[3]:
        $ ui.imagebutton("ep11_ho_party_jillb_idle", "ep11_ho_party_jillb_hover", clicked=ui.returns("jill"), xpos=0, ypos=0, focus_mask=True)
    if not tmp_list[4]:
        $ ui.imagebutton("ep11_ho_party_ball_idle", "ep11_ho_party_ball_hover", clicked=ui.returns("ball"), xpos=0, ypos=0, focus_mask=True)
else:

    scene ep11_main2_party128 with dissolve

    if not tmp_list[0]:
        $ ui.imagebutton("ep11_ho_party_sage_idle", "ep11_ho_party_sage_hover", clicked=ui.returns("sage"), xpos=0, ypos=0, focus_mask=True)
    if not tmp_list[1]:
        $ ui.imagebutton("ep11_ho_party_maya_idle", "ep11_ho_party_maya_hover", clicked=ui.returns("maya"), xpos=0, ypos=0, focus_mask=True)
    if not tmp_list[2]:
        $ ui.imagebutton("ep11_ho_party_josy_idle", "ep11_ho_party_josy_hover", clicked=ui.returns("josy"), xpos=0, ypos=0, focus_mask=True)
    if not tmp_list[3]:
        $ ui.imagebutton("ep11_ho_party_jill_idle", "ep11_ho_party_jill_hover", clicked=ui.returns("jill"), xpos=0, ypos=0, focus_mask=True)
    if not tmp_list[4]:
        $ ui.imagebutton("ep11_ho_party_ball_idle", "ep11_ho_party_ball_hover", clicked=ui.returns("ball"), xpos=0, ypos=0, focus_mask=True)

$ result = ui.interact()
if result == "sage":
    jump ep11_ho_party_sage_label
elif result == "maya":
    jump ep11_ho_party_maya_label
elif result == "josy":
    jump ep11_ho_party_josy_label
elif result == "jill":
    jump ep11_ho_party_jill_label
elif result == "ball":
    jump ep11_ho_party_ball_label

label ep11_ho_party_sage_label:
$ guideSuggestedPage = 220
$ tmp_list[0] = True
if ep11_bp_won_bella:
    scene ep11_main2_party130 with dissolve
    sa "Congrats..."
    if branchSage:
        scene ep11_main2_party131 with dissolve
        mc "And to you as well!"
        scene ep11_main2_party130 with dissolve
        sa "Meh. Who am I covering up for? It's not like they are new to you."
    else:
        scene ep11_main2_party131 with dissolve
        mc "You're not shy tonight."
        scene ep11_main2_party130 with dissolve
        sa "Please... I tan topless, and now I'm among friends."
else:
    scene ep11_main2_party147 with dissolve
    sa "To think that if you sucked less, you would have been in a room full of exposed breasts."
    scene ep11_main2_party148 with dissolve
    mc "You don't have to rub it in."
if ep11_bp_won_bella:
    scene ep11_main2_party132 with dissolve
else:
    scene ep11_main2_party150 with dissolve
sa "Thanks for showing up tonight. I know you said you wanted to be here, but you left a big party."
sa "It's nice that you came, even if it was because of an underwear pic we sent."
if ep11_bp_won_bella:
    scene ep11_main2_party133 with dissolve
else:
    scene ep11_main2_party149 with dissolve
if branchSage:
    mc "The party was fun, but I missed you girls. And I knew I'd have a lot of fun with all of you, too."
else:
    mc "The party was fun, but I missed you. And I knew I'd have a lot of fun with all of you, too."
if ep11_bp_won_bella:
    scene ep11_main2_party132 with dissolve
else:
    scene ep11_main2_party150 with dissolve
sa "Did anything crazy happen at your party?"
if ep11_bp_won_bella:
    scene ep11_main2_party133 with dissolve
else:
    scene ep11_main2_party149 with dissolve
if branchSage:
    mc "(There's no way I'll tell her about what happened with Zoey tonight. That would ruin this party...)"
mc "Just the usual. I'm sure there will be many stories to catch up on tomorrow."
if ep11_bp_won_bella:
    scene ep11_main2_party132 with dissolve
else:
    scene ep11_main2_party150 with dissolve
sa "You'll have a story of your own to tell."
if ep11_bp_won_bella:
    scene ep11_main2_party133 with dissolve
else:
    scene ep11_main2_party149 with dissolve
mc "Haha, nah. This story won't leave this room."
if branchSage and ep11_camila_opportunity:
    if ep11_bp_won_bella:
        scene ep11_main2_party134 with dissolve
    else:
        scene ep11_main2_party152 with dissolve
    mc "About that Camila thing... You weren't for real, right?"
    if ep11_bp_won_bella:
        scene ep11_main2_party135 with dissolve
    else:
        scene ep11_main2_party151 with dissolve
    sa "Why? Were you?"
    if ep11_bp_won_bella:
        scene ep11_main2_party134 with dissolve
    else:
        scene ep11_main2_party152 with dissolve
    if ep8_sq_lewd:
        mc "No, I thought you two were just teasing. But then again, given the threesome with Quinn... I wasn't sure."
    else:
        mc "No, I thought you two were just teasing."
    if ep11_bp_won_bella:
        scene ep11_main2_party135 with dissolve
    else:
        scene ep11_main2_party151 with dissolve
    sa "I mean... If we're just talking about sex... It would be pretty cool."
    sa "You know I'm not opposed to threesomes..."
    if ep11_bp_won_bella:
        scene ep11_main2_party137 with dissolve
    else:
        scene ep11_main2_party153 with dissolve
    sa "And you also wanted me to surprise you in bed..."
    sa "But you're my boyfriend now... That changes things."
    if ep11_bp_won_bella:
        scene ep11_main2_party134 with dissolve
    else:
        scene ep11_main2_party152 with dissolve
    mc "Are you considering it?"
    if ep11_bp_won_bella:
        scene ep11_main2_party135 with dissolve
    else:
        scene ep11_main2_party151 with dissolve
    sa "Wanna ask her?"
    if ep11_bp_won_bella:
        scene ep11_main2_party134 with dissolve
    else:
        scene ep11_main2_party152 with dissolve
    if persistent.mod_wtenabled: 
                        $mod_choices = ["(Sage/Camila threesome)","(+Josy)","(-DIK)","(+DIK)","(+5 Josy)","(-5 Josy)","","","","","","" ]
                        #[mod_gr][mod_choices[0]]
                        #\n{size=-4}[m_c1][mod_choices[1]][m_c2][mod_choices[4]]
    menu:
        "Let's do it \n{size=-4}[m_c1][mod_choices[0]]":
            $ ep11_sage_camila_lewd = True
            mc "I'm up for it if you are. Let's do it."
            if ep11_bp_won_bella:
                scene ep11_main2_party136 with dissolve
            else:
                scene ep11_main2_party154 with dissolve
            sa "So... I'll ask her."
            if ep11_bp_won_bella:
                scene ep11_main2_party134 with dissolve
            else:
                scene ep11_main2_party152 with dissolve
            mc "Tonight?"
            if ep11_bp_won_bella:
                scene ep11_main2_party135 with dissolve
            else:
                scene ep11_main2_party151 with dissolve
            sa "Yeah, why not? We can leave and meet up with her later."
            if ep11_bp_won_bella:
                scene ep11_main2_party134 with dissolve
            else:
                scene ep11_main2_party152 with dissolve
            mc "Go ahead and ask her..."
            if ep11_bp_won_bella:
                scene ep11_main2_party135 with dissolve
            else:
                scene ep11_main2_party151 with dissolve
            sa "I'll text her."
            if ep11_bp_won_bella:
                scene ep11_main2_party134 with dissolve
            else:
                scene ep11_main2_party152 with dissolve
            mc "I wonder if she'll say yes."
            if ep11_bp_won_bella:
                scene ep11_main2_party138 with dissolve
            else:
                scene ep11_main2_party154 with dissolve
            if ep7_camila_lewd or ep7_rica_lewd or ep5_fuckedCamila or ep3_fuckedCamilaAndMona or ep1_lewd_camila_quinn or quinn_shop_spicy_lvl > 0:
                sa "I'm pretty sure she won't mind it. And I think you know it too."
            else:
                sa "She has literally told me she thinks you're hot, so I doubt she will turn it down."
        "No":
            mc "No. But the fantasy of it is hot."
            if ep11_bp_won_bella:
                scene ep11_main2_party135 with dissolve
            else:
                scene ep11_main2_party151 with dissolve
            sa "Yeah. It is."
            $ new_bio("Sage", "I declined Sage's offer of a threesome with Camila.")

if branchSage and not ep11_sage_camila_lewd:
    if ep11_bp_won_bella:
        scene ep11_main2_party142 with dissolve
        $ renpy.pause()
        scene ep11_main2_party143 with dissolve
        mc "It's hard for me to stay normal when you look like that..."
        scene ep11_main2_party144 with dissolve
        sa "I figured that's why you sat near the pillows. In case you have to cover yourself up."
        scene ep11_main2_party143 with dissolve
        mc "Haha! You got me."
        scene ep11_main2_party144 with dissolve
        sa "Is it because of me or them, though? Hm..."
        scene ep11_main2_party143 with dissolve
        if affinity == "DIK":
            mc "Sage, it's a room full of exposed breasts... I have to be careful."
            scene ep11_main2_party145 with dissolve
            sa "Haha! I can't blame you. Even I get a kick from it."
        else:
            mc "Of course, it's because of you."
            scene ep11_main2_party145 with dissolve
            sa "Sweet, but I don't buy it. Hell, even I get a kick from it."
        sa "I assume this is how orgies start."
        scene ep11_main2_party146 with dissolve
        mc "Let's not go there."
        scene ep11_main2_party145 with dissolve
        sa "Why not? The pillow is right there."
        scene ep11_main2_party146 with dissolve
        mc "Stop teasing me."
        scene ep11_main2_party139 with dissolve
        my "Excuse me, but did you say orgy?"
        scene ep11_main2_party140 with dissolve
        sa "Hahaha!"
        scene ep11_main2_party141 with dissolve
        mc "Sage is drunk. Forget what you heard."
    else:
        $ guideSuggestedPage = 221
        scene ep11_main2_party155 with dissolve
        $ renpy.pause()
        scene ep11_main2_party156 with dissolve
        sa "Promise me one thing..."
        scene ep11_main2_party157 with dissolve
        mc "What?"
        scene ep11_main2_party156 with dissolve
        sa "That this is the only time I have to cuddle with you wearing that."
        scene ep11_main2_party158 with dissolve
        menu:
            "I promise":
                scene ep11_main2_party157 with dissolve
                mc "Oh, I promise. You don't have to worry about that."
                scene ep11_main2_party156 with dissolve
                sa "Good."
            "Don't you like it?":
                scene ep11_main2_party160 with dissolve
                mc "Why? Don't you like it?"
                sa "Oh my God... I need bleach for my eyes."
                scene ep11_main2_party159 with dissolve
                mc "Haha!"
            "Joke":
                scene ep11_main2_party157 with dissolve
                mc "Unless something awakens inside me..."
                if ep8_told_josy_chad:
                    scene ep11_main2_party156 with dissolve
                    sa "Oh no... That makes it two for two..."
                    scene ep11_main2_party157 with dissolve
                    mc "Haha, what?"
                scene ep11_main2_party156 with dissolve
                sa "The minute that alarm sounds, I'm ripping these off you."
else:
    if ep11_bp_won_bella:
        scene ep11_main2_party136 with dissolve
        sa "Haha!"
        scene ep11_main2_party134 with dissolve
        mc "What?"
        scene ep11_main2_party135 with dissolve
        sa "I can see your eyes wandering the room."
        scene ep11_main2_party134 with dissolve
        mc "Well, yeah... They have to wander because if I fixate too long on something, I'll... You know?"
        scene ep11_main2_party135 with dissolve
        sa "I figured that's why you sit near the pillows. In case you have to cover yourself up."
        scene ep11_main2_party134 with dissolve
        mc "Haha! You got me."
        scene ep11_main2_party138 with dissolve
        sa "Don't feel too bad about it. Hell, even I get a kick from this."
        scene ep11_main2_party134 with dissolve
        mc "You do?"
        scene ep11_main2_party138 with dissolve
        sa "I assume this is how orgies start."
        scene ep11_main2_party134 with dissolve
        mc "Let's not go there."
        scene ep11_main2_party138 with dissolve
        sa "Why not? The pillow is right there."
        scene ep11_main2_party134 with dissolve
        mc "Stop teasing me."
        scene ep11_main2_party139 with dissolve
        my "Excuse me, but did you say orgy?"
        scene ep11_main2_party140 with dissolve
        sa "Hahaha!"
        scene ep11_main2_party141 with dissolve
        mc "Sage is drunk. Forget what you heard."
jump ep11_ho2_main_party_label

label ep11_ho_party_maya_label:
$ tmp_list[1] = True

if ep11_bp_won_bella:
    scene ep11_main2_party161 with dissolve
    my "How's it going over here?"
    scene ep11_main2_party162 with dissolve
    mc "Oh, I'm having a great time."
    scene ep11_main2_party161 with dissolve
    my "You are? I figured it would be torture for you."
    scene ep11_main2_party162 with dissolve
    mc "How come?"
    scene ep11_main2_party163 with dissolve
    my "Uh... All the nudity."
    scene ep11_main2_party164 with dissolve
    mc "Well, if that's torture for me, it's torture for you too."
    scene ep11_main2_party163 with dissolve
    my "Haha! Not really."
    scene ep11_main2_party164 with dissolve
    mc "You don't get excited by breasts?"
    scene ep11_main2_party165 with dissolve
    my "It's not that simple for me. Is it that simple for you?"
    scene ep11_main2_party164 with dissolve
    mc "Yes. Sometimes, that's all it takes."
    scene ep11_main2_party165 with dissolve
    my "Good thing we're covering ourselves up, then."
    scene ep11_main2_party166 with dissolve
    my "Well, except Sage."
    scene ep11_main2_party167 with dissolve
    my "*{i}Whispers{/i}* And I don't know if you have noticed, but both Bella and Jill are having trouble covering themselves up."
    scene ep11_main2_party168 with dissolve
    my "*{i}Whispers{/i}* I think it's because they have too big boobs or that they are too drunk. Or maybe it's a combination of the two."
    scene ep11_main2_party169 with dissolve
    mc "And you're whispering because...?"
    scene ep11_main2_party170 with dissolve
    my "To let you know."
    scene ep11_main2_party169 with dissolve
    mc "I figured you'd tell them to cover up better."
    scene ep11_main2_party170 with dissolve
    my "Haha, where's the fun in that?"
    scene ep11_main2_party171 with dissolve
    mc "Maybe you get more excited by breasts than you think."
    scene ep11_main2_party173 with dissolve
    mc "And if you're wondering...you're not doing a good job of covering yours."
    my "Haha, shoot! Well, my arms are cramping up from it."
    scene ep11_main2_party171 with dissolve
    mc "Maybe they deserve a break?"
    if branchMayaJosy:
        scene ep11_main2_party172 with dissolve
        my "Ok!"
        scene ep11_main2_party174 with dissolve
        sa "Yes! Go, Maya! That's what I'm talking about."
        sa "We're all girls here."
        scene ep11_main2_party175 with dissolve
        my "[name] isn't."
        scene ep11_main2_party174 with dissolve
        sa "Did you see him in a bra? Hahaha!"
    else:
        scene ep11_main2_party170 with dissolve
        my "Nice try!"
else:
    scene ep11_main2_party176 with dissolve
    my "How's it going for you?"
    scene ep11_main2_party177 with dissolve
    mc "It's the longest hour ever."
    scene ep11_main2_party176 with dissolve
    my "Yeah? Is it torture?"
    scene ep11_main2_party177 with dissolve
    mc "The thong is torture; the bra is just inconvenient."
    scene ep11_main2_party178 with dissolve
    mc "I bet you're having the time of your life."
    mc "A room full of girls in underwear..."
    scene ep11_main2_party179 with dissolve
    my "Haha, it sounds like that would be more your dream than mine."
    scene ep11_main2_party178 with dissolve
    mc "Yeah, but in that dream, I wouldn't be wearing this."
    scene ep11_main2_party179 with dissolve
    my "You can't win them all. But you should be happy with what you got."
    scene ep11_main2_party178 with dissolve
    mc "I am. Despite the outcome, I'm having a great time."

jump ep11_ho2_main_party_label

label ep11_ho_party_josy_label:
$ tmp_list[2] = True
if ep11_bp_won_bella:
    scene ep11_main2_party180 with dissolve
else:
    scene ep11_main2_party187 with dissolve
isa "What do you write about?"
if ep11_bp_won_bella:
    scene ep11_main2_party183 with dissolve
else:
    scene ep11_main2_party190 with dissolve
js "About everything that comes to mind. It's mostly about me, my thoughts, things I enjoy, and fashion."
if ep11_bp_won_bella:
    scene ep11_main2_party180 with dissolve
else:
    scene ep11_main2_party187 with dissolve
isa "I think it's brave of you to put yourself out there to that many people."
if ep11_bp_won_bella:
    scene ep11_main2_party184 with dissolve
else:
    scene ep11_main2_party191 with dissolve
js "It's not that many, but it's more than I thought there would be. I don't know what I did right, but it must be something."
if ep11_bp_won_bella:
    scene ep11_main2_party185 with dissolve
else:
    scene ep11_main2_party192 with dissolve
isa "Could it be that you inspire others? That you're someone to look up to. Or maybe you're that good at writing?"
if ep11_bp_won_bella:
    scene ep11_main2_party186 with dissolve
else:
    scene ep11_main2_party193 with dissolve
js "I don't know. But I'm happy because I've found something I love to do."
if ep11_bp_won_bella:
    scene ep11_main2_party181 with dissolve
else:
    scene ep11_main2_party188 with dissolve
isa "If you don't mind, share the link with me. I'd love to give it a read, a follow, or whatever it's called."
if ep11_bp_won_bella:
    scene ep11_main2_party184 with dissolve
else:
    scene ep11_main2_party191 with dissolve
js "Sure, I'd be happy to."
js "What about you? You obviously read a lot, but have you ever written anything?"
if ep11_bp_won_bella:
    scene ep11_main2_party181 with dissolve
else:
    scene ep11_main2_party188 with dissolve
isa "No, I don't think I would be good at it."
if ep11_bp_won_bella:
    scene ep11_main2_party184 with dissolve
else:
    scene ep11_main2_party191 with dissolve
js "How do you know unless you try it?"
if ep11_bp_won_bella:
    scene ep11_main2_party182 with dissolve
else:
    scene ep11_main2_party189 with dissolve
isa "I know the words, the styles, what I like and don't...but I fear I lack the imagination."
isa "And imagination is key when writing something interesting, wouldn't you agree?"
if ep11_bp_won_bella:
    scene ep11_main2_party183 with dissolve
else:
    scene ep11_main2_party190 with dissolve
js "It depends on what you're writing. But for fiction, yeah, I agree."

jump ep11_ho2_main_party_label

label ep11_ho_party_jill_label:
$ tmp_list[3] = True
if ep11_bp_won_bella:
    scene ep11_main2_party194 with dissolve
else:
    scene ep11_main2_party211 with dissolve
ji "How did we end up like this tonight?"
if ep11_bp_won_bella:
    scene ep11_main2_party199 with dissolve
else:
    scene ep11_main2_party206 with dissolve
sa "I'll tell you how. It's all because of that dude."

if ep11_bp_won_bella:
    scene ep11_main2_party195 with dissolve
    ji "You're right. It is all his fault."
else:
    scene ep11_main2_party212 with dissolve
    ji "Is dude the right word?"
    scene ep11_main2_party213 with dissolve
    sa "Hahaha! You're right! It's not."
    scene ep11_main2_party210 with dissolve
ji "I can't remember when I last had this much fun."
ji "I can tell that Bella feels the same way."
if ep11_bp_won_bella:
    scene ep11_main2_party200 with dissolve
else:
    scene ep11_main2_party205 with dissolve
sa "This was a great idea."
sa "And if I could get out of the party tomorrow, I'd be happy."
if ep11_bp_won_bella:
    scene ep11_main2_party194 with dissolve
else:
    scene ep11_main2_party211 with dissolve
ji "Another party?"
if ep11_bp_won_bella:
    scene ep11_main2_party201 with dissolve
else:
    scene ep11_main2_party204 with dissolve
sa "An obligation is what I'd call it. You know, sorority things?"
if ep11_bp_won_bella:
    scene ep11_main2_party195 with dissolve
else:
    scene ep11_main2_party210 with dissolve
ji "What is it like being in a sorority?"
if ep11_bp_won_bella:
    scene ep11_main2_party201 with dissolve
else:
    scene ep11_main2_party204 with dissolve
sa "Oh, it's...great. Most of the time. It's when you get responsibilities that it starts to eat away at you."
if ep11_bp_won_bella:
    scene ep11_main2_party196 with dissolve
else:
    scene ep11_main2_party209 with dissolve
ji "I see. But I bet it must be a lot of fun for you, Josy, and Maya."
if ep11_bp_won_bella:
    scene ep11_main2_party202 with dissolve
else:
    scene ep11_main2_party203 with dissolve
sa "Are you considering joining?"
if ep11_bp_won_bella:
    scene ep11_main2_party197 with dissolve
else:
    scene ep11_main2_party208 with dissolve
ji "Oh, definitely not. It's not for me."
if ep11_bp_won_bella:
    scene ep11_main2_party202 with dissolve
else:
    scene ep11_main2_party203 with dissolve
sa "Why not? I think you'd like it."
if ep11_bp_won_bella:
    scene ep11_main2_party196 with dissolve
else:
    scene ep11_main2_party209 with dissolve
ji "I'd enjoy parts of it, but the whole sorority thing is not for me. I'm sure my parents would freak out, haha."
if ep11_bp_won_bella:
    scene ep11_main2_party201 with dissolve
else:
    scene ep11_main2_party204 with dissolve
sa "What I'm hearing is it's not for your parents."
if ep11_bp_won_bella:
    scene ep11_main2_party197 with dissolve
else:
    scene ep11_main2_party208 with dissolve
ji "Well, yes. But it's not for me either. And besides, it's too late for me to consider it."
if ep11_bp_won_bella:
    scene ep11_main2_party201 with dissolve
else:
    scene ep11_main2_party204 with dissolve
sa "Ok, but I thought you sounded curious about it just now."
if ep11_bp_won_bella:
    scene ep11_main2_party196 with dissolve
else:
    scene ep11_main2_party209 with dissolve
ji "Don't get me wrong; I was."
ji "Lately, I've felt like I've been venturing outside of my comfort zone."
ji "This entire night should speak for itself."
if ep11_bp_won_bella:
    scene ep11_main2_party202 with dissolve
else:
    scene ep11_main2_party203 with dissolve
sa "Now that I know you're somewhat interested in it, I'll invite you to our parties and include you more."
if ep11_bp_won_bella:
    scene ep11_main2_party196 with dissolve
else:
    scene ep11_main2_party209 with dissolve
ji "Oh, I don't know about that."
if ep11_bp_won_bella:
    scene ep11_main2_party202 with dissolve
else:
    scene ep11_main2_party203 with dissolve
sa "Trust me. You'll like it, and we would love to have you."
if ep11_bp_won_bella:
    scene ep11_main2_party198 with dissolve
else:
    scene ep11_main2_party207 with dissolve
$ renpy.pause()
jump ep11_ho2_main_party_label

label ep11_ho_party_ball_label:
$ tmp_list[4] = True
$ guideSuggestedPage = 221
if ep11_bp_won_bella:
    scene ep11_main2_party214 with dissolve
    $ renpy.pause()
    scene ep11_main2_party215 with dissolve
    
    if persistent.mod_wtenabled: 
                        $mod_choices = ["(Sage/Camila threesome)","(+Josy)","(-DIK)","(+DIK)","(+5 Josy)","(-5 Josy)","","","","","","" ]
                        #[mod_gr][mod_choices[0]]
                        #\n{size=-4}[m_c1][mod_choices[1]][m_c2][mod_choices[4]]
    
    menu:
        "Throw it at Bella \n{size=-4}[m_c1][mod_choices[3]]":
            $ dk(1)
            scene ep11_main2_party216 with dissolve
            mc "Bella! Think fast!"
            play sound "sound_effects/season3/ping_pong_bounce.mp3"
            scene ep11_main2_party217 with vpunch
            $ renpy.pause()
            scene ep11_main2_party218 with dissolve
            isa "Nice try. You'd have to throw something bigger to make me remove my hand."
            scene ep11_main2_party219 with dissolve
            mc "Bigger, eh?"
            scene ep11_main2_party218 with dissolve
            isa "And that wasn't a challenge."
        "Throw it at Josy \n{size=-4}[m_c1][mod_choices[3]]":
            $ dk(1)
            scene ep11_main2_party220 with dissolve
            mc "Josy! Think fast!"
            play sound "sound_effects/season3/ping_pong_bounce.mp3"
            scene ep11_main2_party221 with vpunch
            js "Ahh!!!"
            scene ep11_main2_party222 with dissolve
            js "What are you doing!? Stop that."
        "Throw it at Jill \n{size=-4}[m_c1][mod_choices[3]]":
            $ dk(1)
            scene ep11_main2_party223 with dissolve
            mc "Jill! Think fast!"
            play sound "sound_effects/season3/ping_pong_bounce.mp3"
            scene ep11_main2_party224 with vpunch
            ji "Oh!?"
            scene ep11_main2_party225 with dissolve
            ji "[name]!"
            scene ep11_main2_party226 with dissolve
            my "That's so mean."
        "Don't throw it \n{size=-4}[m_c1][mod_choices[2]]":
            $ dk(-1)
else:
    scene ep11_main2_party227 with dissolve
    mc "Hey, does anyone wanna play me for the bra and panties? I'll take any bet."
    scene ep11_main2_party229 with dissolve
    isa "Nope. We're done playing tonight. You'll have to wait this one out."
    scene ep11_main2_party231 with dissolve
    ji "You can do it, [name]. It will be over soon."
    scene ep11_main2_party230 with dissolve
    js "I bet that thong is starting to feel comfortable now, haha."
    scene ep11_main2_party228 with dissolve
    mc "It's not. It's chafing. I have a newfound appreciation for how you girls do this."
jump ep11_ho2_main_party_label
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
