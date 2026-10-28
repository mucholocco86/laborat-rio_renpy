label marnie_message_label:


    if good or supergood:
        jump marnie2nd

    $ nvl_list = marnie_history
    $ open_text = "Marnie"

    menu(nvl=True):
        "Hey.":


            mc_nvl "Hey, you there?"
            marnie_nvl "Ah, yes. I'm still up."
            marnie_nvl "Is everything alright?"
            marnie_nvl "What's wrong?"
            jump thebag1
        "You still awake?":


            mc_nvl "Hey Marnie, you still awake?"
            marnie_nvl "Indeed, I am."
            marnie_nvl "Everything okay on your end?"
            marnie_nvl "What's wrong??"
            jump thebag1
label thebag1:

    menu(nvl=True):
        "Can you come to my room?":

            jump marnie_talk
        "I have a few questions...":

            jump marnie_questions


    call history_save from _call_history_save
    return

label marnie_questions:

    $ goddd = "{image=sexaddict} Ever cheated on your husband?"

    menu(nvl=True):

        "Why do you talk the way you do?" if not marns:

            mc_nvl "Marnie, can I ask you something? Why do you talk the way you do? I mean... you say a lot of really sexual stuff. Do you even realize it?"
            marnie_nvl "Oh! Ohhh... that. Right. Yeah, you aren't the first person to say this..."
            marnie_nvl "I dunno, I guess it just... stuck. Ever since I was, like, fifteen or sixteen, men have been telling me how I should talk."
            marnie_nvl "Y’know, 'Say this instead', 'sounds cuter that way', or 'don’t bother learning big words', or 'just say pussy like you mean it'. Stuff like that."
            marnie_nvl "Look, I know I’m not very bright, love. Never was. But all the men I met in my life, they’d light up whenever I said something a bit dirty, especially when I didn’t even know it was dirty!"
            marnie_nvl "One told me to stop saying 'intercourse' and just say 'fuck,' ‘cause that was the right way to say it. So I did! I mean, why not?"
            marnie_nvl "Some even trained me, sorta. Told me what words to say during sex or when flirting, like a little script. And they always said it made me more...smarter or whatever."
            marnie_nvl "Oh, and I can't forget the guy who taught me about Suck n Fuck! I had no idea what that meant, but I now know men think you're pretty smart if you tell them you know how to Suck n Fuck!"
            marnie_nvl "So now I just talk like this. Not all the time. I don’t even notice anymore. It just comes out! I’m not trying to be filthy, it’s just my normal now, sort of."
            marnie_nvl "Sorry if it’s weird! I didn’t mean to come across like a daft, I just...that’s how I learned to talk, really. I thought it was helping."

            menu(nvl=True):
                "Thanks for telling me. That uh, explains a lot.":


                    mc_nvl "Thanks for being honest. That actually explains a lot."
                    marnie_nvl "Aww, you’re sweet. Most people just nod and unzip when I start talking like that."
                    marnie_nvl "Nice to know someone’s actually listening, even if my mouth does get a bit... carried away."
                    marnie_nvl "Any other questions?"
                    $ marns = True
                    jump marnie_questions
                "It will not bother me. I like how you talk.":


                    mc_nvl "It doesn’t bother me. I like how you talk."
                    marnie_nvl "Do you really? Even when I say stuff like 'cockwarming' without thinking?"
                    marnie_nvl "Good! ‘Cause I’ve got loads more where that came from."
                    marnie_nvl "Any other questions?"
                    $ marns = True
                    jump marnie_questions
                "So, groomed into talking like a whore. Got it.":


                    mc_nvl "So, basically you were groomed into talking like a whore."
                    marnie_nvl "Groomed?? Oh no no! I mean, they were all lovely!"
                    marnie_nvl "They just gave me tips, y’know? Told me I was sexier when I acted a bit dumb and dirty. So I leaned into it!"
                    marnie_nvl "I didn’t mind at all. I thought they were being helpful!"
                    marnie_nvl "Any other questions?"
                    $ marns = True
                    jump marnie_questions

        "So, you're married, right?" if not marne:

            mc_nvl "So, you're married to Henry?"
            marnie_nvl "Oh! Yes, that’s my Henry! He’s my husband. We’ve been married forever....well, twenty-seven years, but it feels like longer."
            marnie_nvl "He’s right here, actually. On the other side of the bed. Say hi, Henry! …Oh, he's sleeping...."
            marnie_nvl "He stormed out earlier, upset about my therapy, but he came back."
            marnie_nvl "We’re very happy together. He’s my best friend, really. We talk about everything. Watch the same shows. Even pee with the door open sometimes. THAT level of close."
            marnie_nvl "And the sex? It’s good! It is. He’s got a lovely cock, sort of like a polite cucumber. Sturdy but respectful. He knows what he’s doing, most nights."
            marnie_nvl "But if I’m being honest... it’s not always *mind-blowing.* Sometimes I lie there and think about what I’m going to eat tomorrow while he’s doing his thing."
            marnie_nvl "Still, he tries....."
            marnie_nvl "Anyway! I'm not complaining! I mean, could it be better? Sure! Do I fantasize about other things? Maybe. Do I love him to death and keep fucking him anyway? Sure do."
            marnie_nvl "Any other questions?"
            $ marne = True
            jump marnie_questions



        "[goddd]" if sexaddict:

            mc_nvl "Ever cheated on your husband? I mean, other than with George. You can tell me, I'll keep it a secret."
            mc_nvl "Maybe something sneaky or accidental?"
            marnie_nvl "Oh! Erm… well, not on purpose, no! I mean, I’m a loyal wife! I don’t go sneaking about!"
            marnie_nvl "But now that you mention it... there was that thing at the grocery store."
            marnie_nvl "This man once offered to help me bag my apples, and I said, 'Sure, you can handle my melons too while you’re at it,' and then he followed me to my car..."
            marnie_nvl "...and somehow we ended up in the back seat with his face between my thighs!"
            marnie_nvl "Oh, and there was that one guy who came to fix our dryer. I offered him a beer while I was bending over to check the lint trap, and he said, 'I got something you can clean out', so I... well, I thought he meant laundry!"
            marnie_nvl "Before I knew it, my panties were round' my knees and he was saying he loved my house calls. I still paid him and thanked him though, so it wasn’t like... cheating-cheating."
            marnie_nvl "And there was a party once, Henry couldn’t go, he was sick....and I was feeling tipsy, and someone asked if I wanted to try a hands-free back massage."
            marnie_nvl "I said yes, cause my neck was sore. Didn’t know hands-free meant his cock was gonna do all the work..."
            marnie_nvl "But like I said! I didn’t plan any of it! These things just kinda happen sometimes, and I always feel bad after... but also a bit wobbly and satisfied too, so it’s a bit confusing."

            menu(nvl=True):
                "Goddamn.... You're worse than I thought.":


                    mc_nvl "Goddamn, Marnie. You’re worse than I thought."
                    marnie_nvl "I KNOW!! I don’t mean to be! I’m just... easily flattered, I guess?"
                    marnie_nvl "But I’ve been good mom lately! I haven’t fucked anyone who isn’t Henry in a long time."
                    marnie_nvl "Anyway, any other questions?"
                    $ marnt = True
                    jump marnie_questions
        "*Go back*":

            jump thebag1



    call history_save_ from _call_history_save_
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
