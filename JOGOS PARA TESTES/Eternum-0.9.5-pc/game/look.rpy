
default current_look = 0

default looks = {
    "annie"    : [0],
    "nancy"    : [0],
    "penelope" : [0],
    "dalia"    : [0],
    "luna"     : [0],
    "alex"     : [0],
    "nova"     : [0]
    }

define max_looks = {
    "annie"    : nb_looks("lk_annie"),
    "nancy"    : nb_looks("lk_nancy"),
    "penelope" : nb_looks("lk_penelope"),
    "dalia"    : nb_looks("lk_dalia"),
    "luna"     : nb_looks("lk_luna"),
    "alex"     : nb_looks("lk_alex"),
    "nova"     : nb_looks("lk_nova")
    }

init -20 python:
    #
    # Counts the number of looks for a girl
    # (counts all Renpy images with the following name: <root><number>)
    #  root: Usually something like "lk_luna", "lk_dalia", ...
    #  number: A number from 0 to infinite
    #
    def nb_looks(root):
        nb_looks = 0

        while renpy.has_image( root + str(nb_looks) ):
            nb_looks += 1

        return nb_looks

    #
    # Function used to unlock a look for a girl during the playthrough
    #
    # Example: $ unlock_look("dalia", 2)  (corresponds to the file "lk_dalia2.webp" in "images/bios" folder)
    #          $ unlock_look("nancy", 5)  (corresponds to the file "lk_nancy5.webp" in "images/bios" folder)
    #
    def unlock_look(girl, look):
        if look not in looks[girl]:
            store.looks[girl].append(look)


transform look_size:
    crop (40, 0, 786, 1080)
    zoom 0.3
    on idle:
        matrixcolor BrightnessMatrix(0.0)
    on hover:
        matrixcolor BrightnessMatrix(0.2)


screen look_choice(girl):
    style_prefix "lookchoice"
    modal True

    # Dark barely transparent background
    add Solid("#000000e6")

    vpgrid:
        align (0.5, 0.5)
        cols 5
        spacing 20
        draggable True
        mousewheel True
        ymaximum 1012

        scrollbars "vertical"

        # Since we have scrollbars, we have to position the side, rather
        # than the vpgrid proper.
        # side_xalign 0.9
        side_spacing 20

        for i in range(0, max_looks[girl]):
            imagebutton:
                at look_size
                if i in looks[girl]:
                    #
                    # This look has been unlocked
                    #
                    idle "lk_" + girl + str(i)
                    hover_sound audio.neon
                    selected False
                    action [ SetVariable("current_look", looks[girl].index(i)), Hide("look_choice") ]
                else:
                    idle "look_locked"

    key "game_menu" action Hide("look_choice")


style lookchoice_vscrollbar is vscrollbar:
    unscrollable "hide"
