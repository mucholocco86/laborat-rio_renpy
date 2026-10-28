label epi_drawing_game1_label:
$ drw_timer = 0
$ drw_fail = 0

$ renpy.block_rollback()
call screen epi_drawing_game_ready_screen
$ ztime = time.time()
$ drw_pos = []
$ drw_pos.append([488,410])
$ renpy.block_rollback()
call screen epi_drawing_game_screen
$ drw_pos = []
$ drw_pos.append([1000,800])
$ drw_pos.append([900,750])
$ drw_pos.append([1100,750])
$ renpy.block_rollback()
play sound "sound_effects/interlude/sketch.mp3"
call screen epi_drawing_game_screen
$ drw_pos = []
$ drw_pos.append([100,100])
$ drw_pos.append([220,220])
$ drw_pos.append([80,230])
$ drw_pos.append([190,20])
$ renpy.block_rollback()
play sound "sound_effects/interlude/sketch.mp3"
call screen epi_drawing_game_screen
$ drw_pos = []
$ drw_pos.append([1800,400])
$ drw_pos.append([1700,300])
$ drw_pos.append([500,500])
$ drw_pos.append([1750,200])
$ drw_pos.append([800,400])
$ renpy.block_rollback()
play sound "sound_effects/interlude/sketch.mp3"
call screen epi_drawing_game_screen
$ drw_pos = []
$ drw_pos.append([200,600])
$ drw_pos.append([400,400])
$ drw_pos.append([500,500])
$ drw_pos.append([600,600])
$ drw_pos.append([280,540])
$ drw_pos.append([200,700])
$ drw_pos.append([180,200])
$ renpy.block_rollback()
play sound "sound_effects/interlude/sketch.mp3"
call screen epi_drawing_game_screen
$ drw_pos = []
$ drw_pos.append([800,100])
$ drw_pos.append([700,150])
$ drw_pos.append([900,150])
$ drw_pos.append([850,200])
$ drw_pos.append([880,300])
$ drw_pos.append([400,450])
$ drw_pos.append([800,400])
$ drw_pos.append([300,100])
$ renpy.block_rollback()
play sound "sound_effects/interlude/sketch.mp3"
call screen epi_drawing_game_screen
$ drw_pos = []
$ drw_pos.append([1800,500])
$ drw_pos.append([1700,200])
$ drw_pos.append([1700,300])
$ drw_pos.append([1700,400])
$ drw_pos.append([1700,500])
$ drw_pos.append([1700,600])
$ drw_pos.append([1700,700])
$ drw_pos.append([1700,100])
$ renpy.block_rollback()
play sound "sound_effects/interlude/sketch.mp3"
call screen epi_drawing_game_screen
$ drw_pos = []
$ drw_pos.append([50,50])
$ renpy.block_rollback()
play sound "sound_effects/interlude/sketch.mp3"
call screen epi_drawing_game_screen
$ drw_pos = []
$ drw_pos.append([1800,50])
$ drw_pos.append([1000,5])
$ drw_pos.append([1700,50])
$ drw_pos.append([1700,120])
$ drw_pos.append([1800,200])
$ drw_pos.append([1000,400])
$ drw_pos.append([1400,400])
$ renpy.block_rollback()
play sound "sound_effects/interlude/sketch.mp3"
call screen epi_drawing_game_screen
$ drw_pos = []
$ drw_pos.append([200,800])
$ renpy.block_rollback()
play sound "sound_effects/interlude/sketch.mp3"
call screen epi_drawing_game_screen
play sound "sound_effects/interlude/sketch.mp3"
$ epi_draw_scores = []

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
scene epi_leaving33 with dissolve
$ renpy.block_rollback()
call screen drawing_screen_rank(0.05,0.9)

if epi_draw_scores[-1] == "s":
    if not persistent.epi_card5:
        $ unlock_epi_render(5)
    jump epi_after_drawing1_label

call screen zoey_choice_screen("Retry",670,100, "Continue",1500,100)
if tmp_choice == 1:
    $ epi_draw_scores.pop()
    zo "(Hm... That doesn't look right...)"
    scene epi_leaving32 with dissolve
    jump epi_drawing_game1_label
else:
    jump epi_after_drawing1_label


screen drawing_screen_rank(x1, y1):
    tag drawing_screen_rank
    modal True
    imagebutton at drw_blob1_transform:
        xalign x1
        yalign y1
        idle "drw_blob1_spr"
        hover "drw_blob1_spr"
        action Return()
    imagebutton at drw_blob2_transform:
        xalign x1
        yalign y1
        idle "drw_blob2_spr"
        hover "drw_blob2_spr"
        action Return()
    imagebutton at drw_blob3_transform:
        xalign x1
        yalign y1
        idle "drw_blob3_spr"
        hover "drw_blob3_spr"
        action Return()
    if epi_draw_scores[-1] != "s":
        imagebutton at drw_rank_transform:
            xalign x1
            yalign y1
            idle "drw_rank_" + epi_draw_scores[-1]
            hover "drw_rank_" + epi_draw_scores[-1]
            action Return()
    else:
        imagebutton at drw_rank_s_transform:
            xalign x1
            yalign y1
            idle "drw_rank_s"
            hover "drw_rank_s"
            action Return()
    imagebutton:
        idle "drw_empty"
        hover "drw_empty"
        action Return()

image drw_blob1_spr:
    "drw_blob1"
    zoom 1.0
    ease 1.5 zoom 1.008
    ease 1.5 zoom 1.00
    repeat
image drw_blob2_spr:
    "drw_blob2"
    zoom 1.0
    ease 1.0 zoom 1.008
    ease 1.0 zoom 1.00
    repeat
image drw_blob3_spr:
    "drw_blob3"
    zoom 1.0
    ease 1.5 zoom 0.995
    ease 0.5 zoom 1.00
    repeat

transform drw_blob1_transform:
    zoom 0.0
    pause 0.2
    function play_paint_splash_epi
    ease 0.1 zoom 1.0
transform drw_blob2_transform:
    zoom 0.0
    pause 0.5
    function play_paint_splash2_epi
    ease 0.1 zoom 1.0
transform drw_blob3_transform:
    zoom 0.0
    pause 1.0
    function play_paint_splash_epi
    ease 0.1 zoom 1.0
transform drw_rank_transform:
    zoom 0.0
    pause 1.5
    function play_paint_splash2_epi
    ease 0.1 zoom 1.0
transform drw_rank_s_transform:
    zoom 0.0
    pause 1.5
    function play_paint_bling_epi
    ease 0.1 zoom 1.0

screen epi_drawing_game_screen:
    tag epi_drawing_game_screen
    modal True

    imagebutton:
        xpos drw_pos[0][0] * persistent.scale_factor
        ypos drw_pos[0][1] * persistent.scale_factor
        idle "drw_blue_idle"
        hover "drw_blue_hover"
        action Return()

    for i in range(1,len(drw_pos)):
        imagebutton:
            xpos drw_pos[i][0] * persistent.scale_factor
            ypos drw_pos[i][1] * persistent.scale_factor
            idle "drw_red_glow"
            hover "drw_red_glow"
            action NullAction()
        imagebutton:
            focus_mask True
            xpos drw_pos[i][0] * persistent.scale_factor
            ypos drw_pos[i][1] * persistent.scale_factor
            idle "drw_red_idle"
            hover "drw_red_hover"
            hovered (SetVariable("drw_fail",drw_fail + 1),Return())
            action NullAction()

screen epi_drawing_game_ready_screen:
    tag epi_drawing_game_ready_screen
    modal True
    timer 3 repeat False action Return()
    imagebutton at drw_blob1_transform:
        idle "drw_ready_blob1"
        hover "drw_ready_blob1"
        action Return()
    imagebutton at drw_blob2_transform:
        idle "drw_ready_blob2"
        hover "drw_ready_blob2"
        action Return()
    imagebutton at drw_blob3_transform:
        idle "drw_ready_blob3"
        hover "drw_ready_blob3"
        action Return()
    text "Get ready!" style "drw_ready_style" xalign 0.5 yalign 0.5 at drw_rank_transform


style drw_ready_style:
    font "fonts/daisy.ttf"
    size 100 * persistent.scale_factor
    color "#ffffff"
    outlines [(2, "#000000", 0, 0)]
    text_align 0.5


init -1 python:
    def play_paint_splash_epi(trans, st, at):
        renpy.play("sound_effects/interlude/paint_splash.mp3", "sfx1")
    def play_paint_splash2_epi(trans, st, at):
        renpy.play("sound_effects/interlude/paint_splash2.mp3", "sfx1")
    def play_paint_bling_epi(trans, st, at):
        renpy.play("sound_effects/interlude/paint_bling.mp3", "sfx1")
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
