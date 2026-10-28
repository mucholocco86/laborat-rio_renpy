default choicela1 = False
default choicela2 = False
default choicela3 = False
default choicela4 = False
default choicela5 = False
default choicela6 = False
default choicela7 = False
default choicela8 = False
default choicela9 = False
default choicela10 = False
default choicela11 = False
default choicela12 = False

label lorrainechat1:


    menu:



        "Dumb bitch! Take this cock you SLUT!" if not choicela1:

            lor "E-Excuse me! D....Don't talk to me.....like that!"
            lor "W-Watch....your mouth!"
            $ choicela1 = True
            $ chat_hovered = False
            $ angry_counter += 1
            if angry_counter >= 2:
                jump stopscene1
            window hide
            call screen buttonslorraine1

        "FUCK this is some good MILF pussy!" if not choicela2:

            lor "Y-Yes! I'm glad you....like it!"
            lor "F..Fuck me harder, [playerName]! I want....to feel you cock....deep inside me!"
            $ choicela2 = True
            $ chat_hovered = False
            window hide
            call screen buttonslorraine1

        "You like that, bitch!?" if not choicela3:

            lor "N-No! Don't....talk to me....like that!"
            $ choicela3 = True
            $ chat_hovered = False
            $ angry_counter += 1
            if angry_counter >= 2:
                jump stopscene1
            window hide
            call screen buttonslorraine1
        "*Go Back.*":

            $ chat_hovered = False
            window hide
            call screen buttonslorraine1
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
