








screen tooltip(n=1, time=7.0):
    zorder 10
    $ dic = {
        1: "A kinder path has opened before you. GOOD!",
        2: "Something darker has taken root within you. EVIL!",
        3: "Desire now guides your path. SEX ADDICT!",
        4: "Marnie has been added to your contacts.",
        5: "Marnie noticed the way you looked at her.",
        6: "Marnie will remember your compassion.",
        7: "Marnie will remember your cruelty.",
        8: "Marnie will remember that you backed away.",
        9: "Marnie will remember your kiss.",
        10: "Jennifer noticed that you followed her.",
        11: "Jennifer will remember that you resisted her.",
        12: "Jennifer will remember what you chose to call her.",
        13: "Lorraine will remember this.",
        14: "Lorraine will remember that you intruded.",
        15: "Lorraine will remember your praise.",
        16: "You uncovered part of Lorraine's secret.",
        17: "Lorraine will remember what happened between you.",
        18: "Yuni will remember your first impression.",
        19: "Yuni will remember that you resisted her.",
        20: "Yuni will remember that you accepted her title.",
        21: "Yuni will remember that you helped with her video.",
        22: "Yuni will remember that you refused to help.",
        23: "Yuni will remember your failed music choice.",
        24: "Martha will remember how you treated her.",
        25: "Henry will remember that you agreed to help.",
        26: "Henry will remember that you stood by and watched.",
        27: "Marnie will remember that you intervened.",
        28: "Henry will remember that you attacked his boss.",
        29: "Marnie will remember your explanation.",
        30: "Marnie will remember what happened afterward.",
        31: "Nina will remember your patience.",
        32: "Nina will remember how you pressured her.",
        33: "Nina will remember that you crossed the line.",
        34: "Henry will remember your help.",
        35: "Lorraine will remember your honesty.",
        36: "Nina has been added to your contacts.",
        37: "Nina is now your girlfriend.",
        38: "Nina now hates you.",
        39: "Gianna will remember that you paid her.",
        40: "Gianna will remember your indecent proposition.",
        41: "Gianna will remember that you demanded a preview.",
        42: "Myles and Gianna learned what you truly are.",
        43: "Myles will remember that you claimed Martha.",
        44: "Myles will remember that.",
        45: "Martha will remember your invitation to dance."
    }
    frame maximum 800,200 at move_tooltip xpadding 40 ypadding 30:
        text dic.get(n, "") align .5,.45
    $ screen_name = renpy.current_screen().screen_name
    timer time action Hide(screen_name)

init python:
    def show_tooltip(n=1):
        renpy.hide_screen('tooltip')
        renpy.show_screen('tooltip', n=n)


init python:
    def player_msg(text):
        msg(text, who=0)




init:
    $ name = u'not sDextra'
define nm = DynamicCharacter("name")




label groupchat_or_dialogue:
    menu:
        "Group Chat":
            $ groupchat_enable = True
            jump lb_groupchat
        "Dialogue":
            $ groupchat_enable = False
            jump dialogue






screen chel_image():
    zorder 10000
    add "gui/chel.jpg" at Transform(xalign=0.9, yalign=0.5)
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
