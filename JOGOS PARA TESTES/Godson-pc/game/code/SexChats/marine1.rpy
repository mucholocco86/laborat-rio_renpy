default choicemee1 = False
default choicemee2 = False
default choicemee3 = False
default choicemee4 = False
default choicemyy1 = False
default choicemyy2 = False
default choicemyy3 = False
default choicemyy4 = False
default choicemzz1 = False
default choicemzz2 = False
default choicemzz3 = False

label marinechat1:

    menu:



        "Your slutty dumb bitch pussy is great! Fucking stupid bitch!" if not choicemee1:

            mar "Ah! Your dick is crazy too, [playerName]!"
            mar "It's more hot and huge without a condom! I love raw sex!"
            mar "I feel like I'm...losing my mind right now!"

            $ choicemee1 = True
            $ chat_hovered = False
            window hide
            call screen buttonsmarine1

        "Holy shit, Marnie! I never knew you were such a dumb slut!" if not choicemee4:

            mar "Y-Yes! I'm sorry! You're seeing a side of me I didn't want to show!"
            mar "The truth is, I love getting fucked raw......I've been going crazy without it!"
            mar "I want your cock, [playerName]! Fuck me harder!"

            $ choicemee4 = True
            $ chat_hovered = False
            window hide
            call screen buttonsmarine1

        "STUPID FUCKING MILF WHORE!! FUCKING CUM TOILET!!" if not choicemee3:

            mar "Y-Yes! Thank you! I'm nothing more than a cum toilet for [playerName]'s cock!"
            mar "I want your cock everyday! Fuck me however you want!! "

            $ choicemee3 = True
            $ chat_hovered = False
            window hide
            call screen buttonsmarine1
        "*Go Back.*":

            $ chat_hovered = False
            window hide
            call screen buttonsmarine1
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
