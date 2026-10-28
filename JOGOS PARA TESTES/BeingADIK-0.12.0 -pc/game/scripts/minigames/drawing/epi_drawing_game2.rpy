label epi_drawing_game2_label:
$ drw_timer = 0
$ drw_fail = 0
$ renpy.block_rollback()
call screen epi_drawing_game_ready_screen

$ ztime = time.time()
$ drw_pos = []
$ drw_pos.append([800,300])
$ renpy.block_rollback()
call screen epi_drawing_game_screen
$ drw_pos = []
$ drw_pos.append([100,50])
$ drw_pos.append([100,170])
$ drw_pos.append([200,50])
$ renpy.block_rollback()
play sound "sound_effects/interlude/sketch.mp3"
call screen epi_drawing_game_screen
$ drw_pos = []
$ drw_pos.append([900,900])
$ drw_pos.append([1000,900])
$ drw_pos.append([900,800])
$ drw_pos.append([700,800])
$ renpy.block_rollback()
play sound "sound_effects/interlude/sketch.mp3"
call screen epi_drawing_game_screen
$ drw_pos = []
$ drw_pos.append([1800,50])
$ drw_pos.append([1800,300])
$ drw_pos.append([600,500])
$ drw_pos.append([1600,50])
$ drw_pos.append([800,400])
$ renpy.block_rollback()
play sound "sound_effects/interlude/sketch.mp3"
call screen epi_drawing_game_screen
$ drw_pos = []
$ drw_pos.append([100,800])
$ drw_pos.append([50,400])
$ drw_pos.append([100,500])
$ drw_pos.append([500,600])
$ drw_pos.append([780,540])
$ drw_pos.append([300,600])
$ drw_pos.append([1200,200])
$ renpy.block_rollback()
play sound "sound_effects/interlude/sketch.mp3"
call screen epi_drawing_game_screen
$ drw_pos = []
$ drw_pos.append([1000,500])
$ drw_pos.append([1200,500])
$ drw_pos.append([800,500])
$ drw_pos.append([1000,700])
$ drw_pos.append([1000,300])
$ drw_pos.append([850,550])
$ drw_pos.append([1100,200])
$ drw_pos.append([1100,800])
$ renpy.block_rollback()
play sound "sound_effects/interlude/sketch.mp3"
call screen epi_drawing_game_screen
$ drw_pos = []
$ drw_pos.append([150,400])
$ drw_pos.append([300,400])
$ drw_pos.append([500,400])
$ drw_pos.append([100,100])
$ drw_pos.append([200,200])
$ drw_pos.append([200,800])
$ drw_pos.append([400,800])
$ drw_pos.append([500,100])
$ renpy.block_rollback()
play sound "sound_effects/interlude/sketch.mp3"
call screen epi_drawing_game_screen
$ drw_pos = []
$ drw_pos.append([1600,600])
$ renpy.block_rollback()
play sound "sound_effects/interlude/sketch.mp3"
call screen epi_drawing_game_screen
$ drw_pos = []
$ drw_pos.append([200,200])
$ drw_pos.append([350,350])
$ drw_pos.append([400,200])
$ drw_pos.append([200,400])
$ drw_pos.append([50,50])
$ drw_pos.append([150,150])
$ drw_pos.append([900,450])
$ renpy.block_rollback()
play sound "sound_effects/interlude/sketch.mp3"
call screen epi_drawing_game_screen
$ drw_pos = []
$ drw_pos.append([1000,900])
$ renpy.block_rollback()
play sound "sound_effects/interlude/sketch.mp3"
call screen epi_drawing_game_screen
play sound "sound_effects/interlude/sketch.mp3"

$ ztime = time.time() - ztime

$ tmpInt = max(100-drw_fail*10-ztime*1,0)
if tmpInt > 90.0 and drw_fail == 0:
    $ epi_draw_scores.append("s")
elif tmpInt > 80.0 and drw_fail == 0:
    $ epi_draw_scores.append("a")
elif tmpInt > 70.0:
    $ epi_draw_scores.append("b")
elif tmpInt > 60.0:
    $ epi_draw_scores.append("c")
elif tmpInt > 50.0:
    $ epi_draw_scores.append("d")
elif tmpInt > 40.0:
    $ epi_draw_scores.append("e")
else:
    $ epi_draw_scores.append("f")
$ renpy.block_rollback()
scene epi_work21 with dissolve
$ renpy.block_rollback()
call screen drawing_screen_rank(0.05,0.9)

if epi_draw_scores[-1] == "s":
    if not persistent.epi_card6:
        $ unlock_epi_render(6)
    jump epi_after_drawing2_label

call screen zoey_choice_screen("Retry",300,100, "Continue",1400,100)
if tmp_choice == 1:
    $ epi_draw_scores.pop()
    zo "Wait. Let me try this..."
    scene epi_work20 with dissolve
    jump epi_drawing_game2_label
else:
    jump epi_after_drawing2_label
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
