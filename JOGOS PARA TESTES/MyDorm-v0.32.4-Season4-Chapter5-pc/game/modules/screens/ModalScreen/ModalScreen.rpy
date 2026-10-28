screen ModalScreen (closeAction=[ Return () ], backgroundColor=MenuScreenModalBackgroundColor):
    modal True
    frame:
        style "ModalScreenFrame"
        button:
            action closeAction
            if backgroundColor:
                background Solid (backgroundColor)
            style "ModalScreenButton"