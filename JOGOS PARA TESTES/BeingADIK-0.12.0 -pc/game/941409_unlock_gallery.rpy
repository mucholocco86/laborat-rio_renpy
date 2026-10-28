init python:
    for label in renpy.get_all_labels():
        renpy.game.persistent._seen_ever[label] = True
        renpy.game.seen_session[label] = True