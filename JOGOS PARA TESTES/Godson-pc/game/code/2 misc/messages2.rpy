label marnie_talk:


    if good or supergood:
        jump marnie2nd




    $ marnie_first_night_invite_route = ""

    mc_nvl "Would you mind coming up to my room? I've got something I'd like to talk about. Maybe even a few more questions."
    marnie_nvl "Oh! Um... right now, love? Oh dear..."
    marnie_nvl "Well, the thing is... I've already tucked myself in for the night."
    marnie_nvl "And I’m not exactly... presentable at the moment, if you catch my meaning..."

    menu(nvl=True):
        "What do you mean?":


            $ secret1 = True

            mc_nvl "What do you mean?"
            marnie_nvl "Erm... let’s just say I’m in a bit of a... personal state."
            marnie_nvl "It’s how I unwind, you know? End of the day, all stretched out and comfy."
            marnie_nvl "I don’t think it’s the kind of sight you’d expect unless you’re into wide open door policies."
        "I don't understand, what's the issue?":


            $ secret1 = True

            mc_nvl "I don't understand, what's the issue?"
            marnie_nvl "Well, it's a bit awkward to explain. I’ve got this little night-time habit..."
            marnie_nvl "Let’s just say it doesn’t involve pajamas. Or clothes at all, really."

    marnie_nvl "I'm sorry if that sounds confusing."
    marnie_nvl "I just don’t quite know how to say it but..."
    marnie_nvl "Do you, um... know what exhibitionism is?"

    menu(nvl=True):
        "I've heard the term, yeah.":


            mc_nvl "I've heard the term, yeah. Why?"
            marnie_nvl "Well... I sort of... dabble in it?"
            marnie_nvl "Only in private, mind. Just me, myself, and the occasional... leg mirror."
            marnie_nvl "So yeah, I’m not exactly dressed for company. Unless that company likes nipples."
        "No, what is that?":


            mc_nvl "No, what is that?"
            marnie_nvl "Oh! Erm... well, it’s like a lifestyle thing."
            marnie_nvl "Some people, like me, get a kick out of being... naked. Not just indoors either, anywhere."
            marnie_nvl "It’s not for show, really. It’s for me. For how it makes me feel brave and a little bit wicked."
        "Is that something you're into?":


            mc_nvl "Is that something you're into?"
            marnie_nvl "Yeah... I think I am. I never said it out loud before."
            marnie_nvl "It’s just part of how I relax. Sometimes lying back, legs up, and all."
            marnie_nvl "Didn’t think this would come up in conversation, but here we are!"

    marnie_nvl "We can still have our little chat tomorrow if it’s not something urgent."

    menu(nvl=True):
        "So, you're butt-naked in bed right now?":


            mc_nvl "So, you're butt-naked in bed right now?"
            marnie_nvl "Wh-what? I mean, yes! I wouldn't say it like that but... yeah. Ass out, tits loose, full pussy breeze."
            marnie_nvl "It's how I wind down! Nothing pervy...well, maybe a little. Okay, a lot."

    marnie_nvl "Anyway, we should both get some rest, hmm?"
    marnie_nvl "Sleep tight now, and if you dream of me, make it a dirty one."


    if sexaddict:
        jump sexaddictext
    elif evil and marniemakeout and marniestare:
        jump eviltext
    else:
        jump marnie2nd



label eviltext:

    menu(nvl=True):
        "Wait, I don't believe you are naked.":

            $ triedtogetmarnieupstairs = True

            mc_nvl "Wait a second. I'm not sure I believe this."
            marnie_nvl "That I'm actually naked right now? Or that we actually made-out downstairs?"
            marnie_nvl "Because both are true, unfortunately. I was trying to say goodnight like a normal married woman, and then my brain started replaying your tongue in my mouth."
            marnie_nvl "That's why I ran, by the way. Not because I hated it. Because I liked it too much, and I already know what happens when I tell myself something doesn't count."
            marnie_nvl "Also, no. I'm not sending a picture. I'm naked, I'm flustered, and I'm already being stupid enough without leaving evidence on a phone."
            jump sexaddictext

label sexaddictext:


    menu(nvl=True):
        "I don't believe you're naked. Prove it.":

            $ triedtogetmarnieupstairs = True

            mc_nvl "I don't believe you're naked."
            marnie_nvl "Oh bloody hell, I knew you were going to say that."
            marnie_nvl "No, I'm not sending a picture. I may say filthy things without meaning to, but I'm not daft enough to put my bare tits and bits into a message Henry could find."
            marnie_nvl "And if you mean proving it another way... then you're not really asking for proof, are you?"
            if marniemakeout:
                marnie_nvl "You're asking if I'll sneak upstairs naked after kissing you while my husband sleeps downstairs."
            else:
                marnie_nvl "You're asking if I'll sneak upstairs naked while my husband sleeps downstairs, just to prove I meant what I said."

            jump marnie_evil_proof_branch


label marnie_evil_proof_branch:

    menu(nvl=True):
        "Come upstairs naked. No picture, no evidence.":


            mc_nvl "Then come upstairs naked. No picture, no evidence."
            marnie_nvl "That is a horrible argument."
            marnie_nvl "A horribly tempting argument, which makes it worse."
            marnie_nvl "A picture stays forever, but walking upstairs would only be a few quiet steps, wouldn't it? Just me, the hallway, your door, and one very bad decision."
            marnie_nvl "But if I come up there naked, don't pretend this is innocent. We both know exactly what you want to do to me."

            jump marnie_evil_desire_menu
        "I want to fuck you, Marnie.":


            mc_nvl "I want to fuck you, Marnie. Stop pretending you don't want it."
            marnie_nvl "Jesus..."
            marnie_nvl "You don't soften a single word, do you?"
            marnie_nvl "The worst part is that my body likes hearing it. My brain is panicking, my conscience is screaming, and my stupid body is acting like you just said something romantic."
            marnie_nvl "But wanting it and doing it are not the same thing. Sex is the line. After George, I promised myself I would never cross that line again."

            jump marnie_evil_boundary_menu
        "If you're scared, just say it.":


            mc_nvl "If you're scared, just say you're scared."
            marnie_nvl "Fine. I'm scared."
            if marniemakeout:
                marnie_nvl "I'm scared because I know I'm not as strong as I pretend to be. I'm scared because I kissed you once and nearly melted against you like a silly slut by the stairs."
            else:
                marnie_nvl "I'm scared because I know I'm not as strong as I pretend to be. I'm scared because I've been lying here imagining what I might do if I walked into your room and saw you waiting for me."
            marnie_nvl "I'm scared because Henry trusts me more than I deserve sometimes, and because I already have one old mistake living in the walls of this family."
            marnie_nvl "And I'm scared because part of me still wants to get out of this bed and let you look at every inch of me."

            jump marnie_evil_guilt_menu


label marnie_evil_wanted_branch:

    menu(nvl=True):
        "You liked being wanted.":


            mc_nvl "You liked being wanted. Let me make you feel it again."
            marnie_nvl "I did like it."
            marnie_nvl "God help me, I liked it so much it made me angry. Henry walks past me like I'm furniture half the time, and then you look at me once like I'm something worth ruining yourself over."
            marnie_nvl "I shouldn't need that. I shouldn't be this hungry for it."
            if marniemakeout:
                marnie_nvl "But when you kissed me, I felt like a woman again, not just Henry's wife standing around saying daft things with big tits."
            else:
                marnie_nvl "But the way you looked at me downstairs, and the way you're talking to me now, makes me feel like a woman again, not just Henry's wife standing around saying daft things with big tits."

            jump marnie_evil_desire_menu
        "You wanted me staring at your tits.":


            mc_nvl "You wanted me staring at your tits in the kitchen."
            marnie_nvl "I shouldn't admit this."
            marnie_nvl "But yes. A little."
            marnie_nvl "I saw your eyes drop, and instead of covering myself, I moved just enough to make it worse. I told myself I was being playful, but that was a lie."
            marnie_nvl "I wanted to see if you were still looking. And you were."

            jump marnie_evil_desire_menu
        "Then keep pretending. Don't come.":


            mc_nvl "Then keep pretending. Stay downstairs with Henry."
            marnie_nvl "That was cruel."
            marnie_nvl "Maybe deserved, but still cruel."
            if marniemakeout:
                marnie_nvl "I am trying to stay downstairs with Henry. That's exactly what I'm doing right now, lying beside him while texting the man I kissed."
            else:
                marnie_nvl "I am trying to stay downstairs with Henry. That's exactly what I'm doing right now, lying beside him while texting a man who's trying to coax me upstairs naked."
            marnie_nvl "If you're trying to shame me into behaving, it might work. If you're trying to make me admit I want to misbehave, it already has."

            jump marnie_evil_guilt_menu


label marnie_evil_desire_menu:

    menu(nvl=True):
        "Come upstairs and let me look at you.":


            mc_nvl "Come upstairs and let me look at you properly."
            marnie_nvl "Just look?"
            marnie_nvl "No, don't answer that. I know it wouldn't stay at looking, and I know I wouldn't want it to."
            marnie_nvl "The thought of standing in your room with nothing on while you stare at me like that is making my stomach twist in a very stupid, very dirty way."
            marnie_nvl "But if I come up, there have to be rules. Real ones."



            jump marnie_evil_boundary_menu
        "Tell me what you want me to do to you.":


            mc_nvl "Tell me what you want me to do to you."
            marnie_nvl "That's unfair."
            marnie_nvl "Because if I type it, it becomes real, and if it becomes real, I can't pretend I'm just being silly."
            if marniemakeout:
                marnie_nvl "I want your mouth on me again. I want your hands where Henry hasn't put his in ages. I want to feel wanted so badly it makes me forget to be ashamed."
            else:
                marnie_nvl "I want to know what your mouth would feel like on me. I want your hands where Henry hasn't put his in ages. I want to feel wanted so badly it makes me forget to be ashamed."
            marnie_nvl "But I don't want to say the one thing you're waiting for, because if I say I want your cock, I might not be smart enough to stop you."

            jump marnie_evil_boundary_menu
        "You're already cheating. Stop hiding.":


            mc_nvl "You're already cheating. Stop hiding behind rules."
            marnie_nvl "I know."
            marnie_nvl "I hate that I know."
            marnie_nvl "But I need the rule anyway. Maybe it's stupid, maybe it's hypocritical, but it's the only wall I've got left in my head."
            marnie_nvl "If I tell myself sex is the line, then maybe I can come close to the fire without throwing my whole life into it."

            jump marnie_evil_boundary_menu


label marnie_evil_guilt_menu:

    menu(nvl=True):
        "I know you want me though.":


            mc_nvl "I know you want me though."
            marnie_nvl "That's exactly what makes it dangerous."
            marnie_nvl "If it's a mistake, I can cry later and say I lost my head. If it's a choice, then I have to admit I wanted it before I ever left the bed."
            if marniemakeout:
                marnie_nvl "And I do want something. I want the kiss again. I want your hands on me. I want to feel that filthy little spark I felt downstairs."
            else:
                marnie_nvl "And I do want something. I want to know what that first kiss would feel like. I want your hands on me. I want to feel that filthy little spark I've been imagining since we started texting."
            marnie_nvl "But I cannot let it become sex. I can't do that to Henry again."

            jump marnie_evil_boundary_menu
        "Come upstairs whore.":


            mc_nvl "You can feel guilty tomorrow. Come upstairs tonight you whore."
            marnie_nvl "That is such a wicked thing to say."
            marnie_nvl "And the awful part is, it works on the selfish little part of me that wants one night where I don't think, don't cook, don't explain, don't behave."
            marnie_nvl "But tomorrow still exists. Henry still exists. My marriage still exists."
            marnie_nvl "So if I come up, it is not for sex. Say what you want about me, but I need that line."

            jump marnie_evil_boundary_menu
        "Then stay there.":


            mc_nvl "Then stay there. I don't want half of you."
            marnie_nvl "Then you can't have me."
            marnie_nvl "Because half of me is all I know how to offer without falling apart."
            marnie_nvl "I wanted you tonight. I still do. But if you need me to walk upstairs already agreeing to be fucked, I can't."
            marnie_nvl "Goodnight, [playerName]. Please don't make me weaker than I already feel."
            jump marnie2nd


label marnie_evil_boundary_menu:

    marnie_nvl "Listen carefully, because I'm only going to say this while I still have enough sense to say it."
    marnie_nvl "I will come upstairs, and I already know what we're going to do."
    marnie_nvl "But listen, no sex. Not because I don't want it. I do, and that's the problem."
    marnie_nvl "Kissing, touching, mouths, hands... I can tell myself those are terrible but survivable. Actual fucking is the line I can't cross."
    marnie_nvl "If you push me too hard on that, I won't come upstairs. Or I'll come up and run straight back out like an idiot."

    menu(nvl=True):

        "{image=evil} Fine. No sex. (Lie)" if evil and marniemakeout and not sexaddict:

            $ marnie_first_night_invite_route = "evil"
            $ sexwithmarnie = True
            $ fooledaroundwithmarnie = False
            mc_nvl "Fine. No sex. Everything else is enough."
            marnie_nvl "Don't say 'everything else' like that."
            marnie_nvl "It makes my brain start listing things, and none of them are ladylike."
            marnie_nvl "But... alright. If you mean it, if you actually mean you'll respect that line, then maybe I can breathe long enough to stand up."
            marnie_nvl "We need more rules, though. Because if I walk in and you look at me the way you did downstairs, I might forget half my own name."

            jump marnie_evil_rules_menu
        "No. If you come up, I'm fucking you.":


            mc_nvl "No. If you come up, I'm fucking you."
            marnie_nvl "Then I'm not coming."
            marnie_nvl "I may be horny, lonely, and thicker than a brick when I'm flustered, but I'm not walking into a room where my only rule is already being broken."
            marnie_nvl "Part of me likes that you want me that badly. A bigger part of me knows I would hate myself by morning."
            marnie_nvl "Goodnight. I mean it this time."
            jump marnie2nd

        "{image=sexaddict} If you change your mind..." if sexaddict:

            $ marnie_first_night_invite_route = "sexaddict"
            $ sexwithmarnie = False
            $ fooledaroundwithmarnie = True
            mc_nvl "If you change your mind upstairs, that's your choice."
            marnie_nvl "That's..."
            marnie_nvl "Dangerously reasonable."
            marnie_nvl "Fine. If anything changes, it comes from me, not because you cornered me, begged me, or shoved the thought into my head while my tits are already out."
            marnie_nvl "God, I cannot believe I'm negotiating adultery like it's a dinner menu."

            jump marnie_evil_rules_menu


label marnie_evil_rules_menu:

    marnie_nvl "Rules, then."
    marnie_nvl "Quiet. No waking Henry, no marks where anyone can see, no ripping anything, and no actual sex unless I clearly say otherwise."
    marnie_nvl "Also, if I panic, you let me panic. No laughing, no calling me stupid, even if I am being very, very stupid."
    marnie_nvl "And I need to know how I'm supposed to walk up there, because right now I'm sitting in bed naked with the sheet around my waist like some guilty statue."

    menu(nvl=True):
        "I want you bare when you open the door.":


            mc_nvl "Come naked. I want you bare when you open the door."
            marnie_nvl "Bloody hell..."
            marnie_nvl "You really are trying to kill me, aren't you?"
            marnie_nvl "Walking through the hallway completely naked might make me lose my nerve before I even reach your room. But the thought of you waiting there, knowing I'm coming with nothing on..."
            marnie_nvl "No. I need one more second before I decide that."

            jump marnie_evil_final_barrier
        "Wear whatever makes you brave.":


            mc_nvl "Wear whatever makes you brave. I just want you in my room."
            marnie_nvl "That's almost sweet."
            marnie_nvl "Still dirty, obviously, because I know exactly why you want me in your room."
            marnie_nvl "But giving me a choice makes this feel less like I'm being dragged by the stupid wet part of my brain."
            marnie_nvl "Maybe I'll bring the sheet. Maybe nothing. Maybe something tiny enough to count as clothing only if a judge is feeling generous."

            jump marnie_evil_final_barrier


label marnie_evil_final_barrier:

    marnie_nvl "I'm sitting up now."
    marnie_nvl "Henry didn't move. He's still asleep, and I can hear him breathing like nothing in the world is happening."
    marnie_nvl "My heart is going mad. My body is worse. I feel guilty, excited, ashamed, wanted, and so bloody stupid I could scream into a pillow."
    marnie_nvl "If I stand up, this becomes real. So choose your next words carefully."

    menu(nvl=True):
        "Come upstairs, I want you.":


            mc_nvl "Come upstairs, Marnie. I want you, and I'll keep your rule."
            marnie_nvl "Okay."
            marnie_nvl "That was the right thing to say, damn you."
            marnie_nvl "I'm getting up. If Henry wakes, I'm going to the bathroom. If I lose my nerve, I'm blaming you forever."
            marnie_nvl "Leave the door unlocked. And don't look smug when I come in, or I swear I'll turn around with my tits still out."
            if marnie_first_night_invite_route == "evil":
                $ sexwithmarnie = True
                $ fooledaroundwithmarnie = False
            elif marnie_first_night_invite_route == "sexaddict":
                $ sexwithmarnie = False
                $ fooledaroundwithmarnie = True
            elif fooledaroundwithmarnie or sexaddict:


                $ marnie_first_night_invite_route = "sexaddict"
                $ sexwithmarnie = False
                $ fooledaroundwithmarnie = True
            elif sexwithmarnie or (evil and marniemakeout):


                $ marnie_first_night_invite_route = "evil"
                $ sexwithmarnie = True
                $ fooledaroundwithmarnie = False
            else:


                jump marnie_evil_boundary_menu
            jump marniem2
        "I'm gonna fuck you.":


            mc_nvl "Come upstairs so I can break that little rule of yours. I'll fuck your brains out."
            marnie_nvl "No."
            marnie_nvl "That just woke my brain up, unfortunately."
            marnie_nvl "I wanted to come. I really did. But if you're already talking about breaking the one thing I begged you not to break, then I know exactly what happens in that room."
            marnie_nvl "Goodnight, [playerName]. I'm putting the phone down before I let my body answer instead of my head."
            jump marnie2nd
        "Stay there if you're too scared.":


            mc_nvl "Stay there if you're too scared."
            marnie_nvl "Maybe I should."
            marnie_nvl "Maybe being scared is the only sensible thing I've felt all night."
            marnie_nvl "I wanted you to make me feel wanted, not small. And right now I feel like if I come up, I'll have to prove something instead of wanting it for myself."
            marnie_nvl "So I'm staying here. Goodnight."
            jump marnie2nd

    call history_save from _call_history_save_1
    return
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
