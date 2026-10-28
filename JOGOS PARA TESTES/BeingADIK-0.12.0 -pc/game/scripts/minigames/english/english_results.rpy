label eng_results_label:
$ renpy.block_rollback()
scene desk_bg
hide screen english_screen
with dissolve

if englishResult == 100:
    $ ui.imagebutton("classes_perfect", "classes_perfect", clicked=ui.returns("NULL"), xalign=0.49, yalign=0.14)
elif englishResult + bonusPercentageEnglish >= 90- (englishBoost*5):
    $ ui.imagebutton("classes_great", "classes_great", clicked=ui.returns("NULL"), xalign=0.49, yalign=0.14)
elif englishResult + bonusPercentageEnglish >= 70 - (englishBoost*5):
    $ ui.imagebutton("classes_good", "classes_good", clicked=ui.returns("NULL"), xalign=0.49, yalign=0.14)
else:
    $ ui.imagebutton("classes_fail", "classes_fail", clicked=ui.returns("NULL"), xalign=0.49, yalign=0.14)

$ ui.imagebutton("classes_you_scored", "classes_you_scored", clicked=ui.returns("NULL"), xalign=0.49, yalign=0.305)

if persistent.scale_factor == 1:
    show text "{font=fonts/bradhitc.ttf}{color=#2b2b2b}{size=+50}[englishResult] + {color=#26ef4b}[bonusPercentageEnglish]{/color}%{/size}{/color}{/font}":
        yalign 0.4
else:
    show text "{font=fonts/bradhitc.ttf}{color=#2b2b2b}{size=+100}[englishResult] + {color=#26ef4b}[bonusPercentageEnglish]{/color}%{/size}{/color}{/font}":
        yalign 0.4
stop music fadeout 3

if eng_rew:
    $ ui.imagebutton("classes_special_render", "classes_special_render", clicked=ui.returns("NULL"), xalign=0.48, yalign=0.6)

if englishResult + bonusPercentageEnglish >= 70 - (englishBoost*5):
    if eng_cheated:
        $ ui.imagebutton("classes_with_cheating", "classes_with_cheating", clicked=ui.returns("NULL"), xalign=0.48, yalign=0.7)
    else:
        $ ui.imagebutton("classes_without_cheating", "classes_without_cheating", clicked=ui.returns("NULL"), xalign=0.48, yalign=0.7)

if branchIsabella:
    $ ui.imagebutton("classes_heart", "classes_heart", clicked=ui.returns("NULL"))



if steamAchievements and englishResult + bonusPercentageEnglish >= 70 - (englishBoost*5) and not config.console and not config.developer:
    if eng_cheated:
        $ achievement.grant("NOTSOHONORABLESTUDENT")
        init:
            $ achievement.register("NOTSOHONORABLESTUDENT")
    else:
        $ achievement.grant("HONORABLESTUDENT")
        init:
            $ achievement.register("HONORABLESTUDENT")
    $ achievement.Sync()
else:
    if steamAchievements and not config.console and not config.developer:
        $ achievement.grant("FISFORFAILURE")
        init:
            $ achievement.register("FISFORFAILURE")
        $ achievement.Sync()

if englishResult + bonusPercentageEnglish < 70 - (englishBoost*5):
    $ ui.imagebutton("classes_failed_test", "classes_failed_test", clicked=ui.returns("NULL"), xalign=0.48, yalign=0.7)
stop music fadeout 3
$ bonusPercentageEnglish = 0
$ renpy.pause()
hide text
show screen new_phone_screen
$ quick_menu = tmpMenu
$ renpy.jump(eng_jump_label)
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
