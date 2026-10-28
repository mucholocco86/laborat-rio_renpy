init 50:
    screen SettingsSay (who, what, marginTop):
        style_prefix "say"
        window:
            id "window"
            background Frame (Transform ("gui/textbox.png", alpha = persistent.dialogueBoxOpacity), 15, 15)
            frame:
                background Solid ("#fff")
                xysize (1.0, 1.0)
            if who is not None:
                window:
                    id "namebox"
                    style "namebox"
                    text who id "who" color "#000"
            text what id "what" color "#000"

        ## If there's a side image, display it above the text. Do not display on the
        ## phone variant - there's no room.
            if not renpy.variant("small"):
                add SideImage() xalign 0.0 yalign 1.0