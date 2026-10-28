label ep10_derek2_shop:
$ renpy.block_rollback()
$ phone_call_enabled = False
scene ep10_derek2_shop1 with dissolve
de "Are you ready to leave already? Or is this about something else?"
scene ep10_derek2_shop2 with dissolve
show screen newmoneymsg
call screen shop_derek_screen
$ renpy.pause(0.5)
hide screen newmoneymsg
scene ep10_derek2_shop1 with dissolve
de "Later, bro!"
jump endEvent

label ep10_magnar2_shop:
$ renpy.block_rollback()
$ phone_call_enabled = False
scene ep10_magnar2_shop1 with dissolve
mg "[name]! How is everything?"
scene ep10_magnar2_shop2 with dissolve
show screen newmoneymsg
call screen shop_magnar_screen
$ renpy.pause(0.5)
hide screen newmoneymsg
scene ep10_magnar2_shop1 with dissolve
mg "Happy Thanksgiving, [name]!"
jump endEvent
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
