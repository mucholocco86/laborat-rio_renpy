init python:
    def play_car_hump(trans,st,at):
        renpy.play("sound_effects/season3/car_hump.mp3","sfx1")
    def play_party_horn(trans,st,at):
        renpy.play("sound_effects/season3/party_horn.mp3","sfx1")
    def play_books_crash(trans,st,at):
        renpy.play("sound_effects/door_break.mp3","sfx1")
    def play_ko_sfx(trans,st,at):
        renpy.play("sound_effects/season3/ko_sfx.mp3","sfx1")

    def check_ilove():
        global RPisabella
        if RPisabella > 12:
            return True
        else:
            return False

    def check_jilove():
        global RPjill
        if RPjill > 20:
            return True
        else:
            return False

    def showNotificationMsg(msg):
        global specialMessage
        specialMessage = msg
        renpy.show_screen("specialmsg")
        return

# Decompiled by unrpyc {v1.3.2}: https://github.com/CensoredUsername/unrpyc dev-branch
