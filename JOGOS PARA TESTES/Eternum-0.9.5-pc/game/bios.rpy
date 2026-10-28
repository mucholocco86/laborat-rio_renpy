
init python:
    class Heart:
        def __init__(self, hearts2, hearts3, hearts4, hearts5, hearts6):
            # How many love points are needed to unlock 2 hearts in the bios screen
            self.hearts2 = hearts2

            # How many love points are needed to unlock 3 hearts in the bios screen
            self.hearts3 = hearts3

            # How many love points are needed to unlock 4 hearts in the bios screen
            self.hearts4 = hearts4

            # How many love points are needed to unlock 5 hearts in the bios screen
            self.hearts5 = hearts5

            # How many love points are needed to unlock 6 hearts in the bios screen
            self.hearts6 = hearts6

#
# Threshold of love points to unlock hearts in the bios screen
#
define girls_hearts = {
    "annie"    : Heart(  0,   7,  12,  19,  -1),
    "nancy"    : Heart(  0,   5,   9,  13,  -1),
    "penelope" : Heart(  6,   8,  13,  18,  -1),
    "dalia"    : Heart(  4,   7,  10,  15,  -1), 
    "luna"     : Heart(  5,   8,  16,  23,  -1),
    "alex"     : Heart(  4,   7,  14,  17,  -1),
    "nova"     : Heart(  4,   8,  13,  17,  -1),
    "calypso"  : Heart(  1,   1,  13,  -1,  -1), 
    }

#
# Background image in the bios screen
# (can change during the playthrough)
#
default bios_background = {
    "annie"    : "annie_bios",
    "nancy"    : "nancy_bios",
    "penelope" : "penelope_bios",
    "dalia"    : "dalia_bios",
    "luna"     : "luna_bios",
    "alex"     : "alex_bios",
    "nova"     : "nova_bios",
    }

# screen bios(girl):
#     modal True
#     style_prefix "points"

#     # Love points of the current girl
#     default loc_points = getattr(store, girl + "_points")


#     # Bios screen background (1920 x 1080)
#     add bios_background[girl]


#     # Girl image on the left side (1920 x 1080)
#     imagebutton:
#         idle "lk_" + girl + str(looks[girl][current_look])
#         hover Transform("lk_" + girl + str(looks[girl][current_look]), matrixcolor=BrightnessMatrix(0.1))
#         focus_mask True
#         action Show("look_choice", girl=girl)


#     #
#     # Number of hearts to unlock
#     #
#     hbox:
#         pos (854, 420)
#         spacing -10

#         # First heart
#         add "bios_heart_on"

#         # Second heart
#         if girls_hearts[girl].hearts2 != -1 and loc_points >= girls_hearts[girl].hearts2:
#             add "bios_heart_on"
#         else:
#             add "bios_heart_off"

#         # Third heart
#         if girls_hearts[girl].hearts3 != -1 and loc_points >= girls_hearts[girl].hearts3:
#             add "bios_heart_on"
#         else:
#             add "bios_heart_off"

#         # Fourth heart
#         if girls_hearts[girl].hearts4 != -1 and loc_points >= girls_hearts[girl].hearts4:
#             add "bios_heart_on"
#         else:
#             add "bios_heart_off"

#         # Fifth heart
#         if girls_hearts[girl].hearts5 != -1 and loc_points >= girls_hearts[girl].hearts5:
#             add "bios_heart_on"
#         else:
#             add "bios_heart_off"

#         # Sixth heart
#         if girls_hearts[girl].hearts6 != -1 and loc_points >= girls_hearts[girl].hearts6:
#             add "bios_heart_on"
#         else:
#             add "bios_heart_off"


#     #
#     # Return button
#     #
#     imagebutton:
#         idle "returnp"
#         hover "returnp2"
#         align (1.0, 1.0)
#         keysym "game_menu"
#         if renpy.variant("small"):
#             action Return()
#         else:
#             action Hide('bios', transition=dissolve)

#     #
#     # Gallery button
#     #
#     imagebutton:
#         idle "galleryp"
#         hover "galleryp2"
#         xalign 1.0
#         yalign 0.315
#         action [ Play("soundlow", audio.neon),
#                 SetVariable("filter_scene", "all"),
#                 SetVariable("filter_girl", girl),
#                 Show("gallery", transition=dissolve) ]


#     #
#     # Shortcuts to cycle girl's looks
#     #
#     # Next look
#     key [ "input_right", "rollforward", "skip" ]:
#         action If( current_look == len(looks[girl])-1, SetVariable("current_look", 0),  SetVariable("current_look", current_look + 1) )

#     # Previous look
#     key [ "input_left", "rollback" ]:
#         action If( current_look == 0, SetVariable("current_look", len(looks[girl])-1), SetVariable("current_look", current_look - 1) )


# style points_image_button:
#     hover_sound audio.neon
