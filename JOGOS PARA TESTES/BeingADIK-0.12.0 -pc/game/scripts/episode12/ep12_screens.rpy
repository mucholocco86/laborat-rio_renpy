label nm_dead_fish_label:
mc "(It's just this poor fella left... The rest are all dead. I won't let you die, though... I think I can handle one fish...)"
$ renpy.jump(fish_label)

screen ep12_render_screen(x):
    tag ep12_render_screen
    modal False
    imagebutton:
        focus_mask True
        idle "ep12_card_"+ x +"_idle"
        hover "ep12_card_"+ x +"_hover"
        action (Function(unlock_ep12_render,x),Hide("ep12_render_screen"))

init python:
    def unlock_ep12_render(x):
        if x == "cam1" and not persistent.ep12_cardcam1:
            persistent.ep12_cardcam1 = True
            persistent.rew_cam_unlocked += 1
        elif x == "cam2" and not persistent.ep12_cardcam2:
            persistent.ep12_cardcam2 = True
            persistent.rew_cam_unlocked += 1
        elif x == "cam3" and not persistent.ep12_cardcam3:
            persistent.ep12_cardcam3 = True
            persistent.rew_cam_unlocked += 1
        elif x == "cam4" and not persistent.ep12_cardcam4:
            persistent.ep12_cardcam4 = True
            persistent.rew_cam_unlocked += 1
        elif x == "cam5" and not persistent.ep12_cardcam5:
            persistent.ep12_cardcam5 = True
            persistent.rew_cam_unlocked += 1
        elif x == "cam6" and not persistent.ep12_cardcam6:
            persistent.ep12_cardcam6 = True
            persistent.rew_cam_unlocked += 1
        elif x == "cam7" and not persistent.ep12_cardcam7:
            persistent.ep12_cardcam7 = True
            persistent.rew_cam_unlocked += 1
        elif x == "cam8" and not persistent.ep12_cardcam8:
            persistent.ep12_cardcam8 = True
            persistent.rew_cam_unlocked += 1
        elif x == "cam9" and not persistent.ep12_cardcam9:
            persistent.ep12_cardcam9 = True
            persistent.rew_cam_unlocked += 1
        elif x == "cam10" and not persistent.ep12_cardcam10:
            persistent.ep12_cardcam10 = True
            persistent.rew_cam_unlocked += 1
        elif x == "cam11" and not persistent.ep12_cardcam11:
            persistent.ep12_cardcam11 = True
            persistent.rew_cam_unlocked += 1
        elif x == "cam12" and not persistent.ep12_cardcam12:
            persistent.ep12_cardcam12 = True
            persistent.rew_cam_unlocked += 1
        elif x == "cam13" and not persistent.ep12_cardcam13:
            persistent.ep12_cardcam13 = True
            persistent.rew_cam_unlocked += 1
        elif x == "cam14" and not persistent.ep12_cardcam14:
            persistent.ep12_cardcam14 = True
            persistent.rew_cam_unlocked += 1
        elif x == "cam15" and not persistent.ep12_cardcam15:
            persistent.ep12_cardcam15 = True
            persistent.rew_cam_unlocked += 1
        elif x == "cam16" and not persistent.ep12_cardcam16:
            persistent.ep12_cardcam16 = True
            persistent.rew_cam_unlocked += 1
        elif x == "cam17" and not persistent.ep12_cardcam17:
            persistent.ep12_cardcam17 = True
            persistent.rew_cam_unlocked += 1
        elif x == "cam18" and not persistent.ep12_cardcam18:
            persistent.ep12_cardcam18 = True
            persistent.rew_cam_unlocked += 1
        elif x == "cam19" and not persistent.ep12_cardcam19:
            persistent.ep12_cardcam19 = True
            persistent.rew_cam_unlocked += 1
        
        persistent.chat_new_rewards = True
        calcRenders()
        renpy.show_screen("srmsg")
        return

    def dj_play_music(x):
        global ep12_dj_counter
        ep12_dj_counter += 1
        if steamAchievements and ep12_dj_counter >= 500 and ep12_dj_counter < 550 and not config.console and not config.developer:
            achievement.grant("IDS3_46")
            achievement.Sync()
        if x == 0:
            renpy.sound.play("sound_effects/season3/dj/dj_clap.mp3",channel="dj1", loop=False)
        elif x == 1:
            renpy.sound.play("sound_effects/season3/dj/dj_drop.mp3",channel="dj2", loop=False)
        elif x == 2:
            renpy.sound.play("sound_effects/season3/dj/dj_horn.mp3",channel="dj3", loop=False)
        elif x == 3:
            renpy.sound.play("sound_effects/season3/dj/dj_kick.mp3",channel="dj4", loop=False)
        elif x == 4:
            renpy.sound.play("sound_effects/season3/dj/dj_heavy_hit.mp3",channel="dj5", loop=False)
        elif x == 5:
            renpy.sound.play("sound_effects/season3/dj/dj_riser.mp3",channel="dj6", loop=False)
        elif x == 6:
            renpy.sound.play("sound_effects/season3/dj/dj_spin.mp3",channel="dj7", loop=False)
        elif x == 7:
            renpy.sound.play("sound_effects/season3/dj/dj_bass.mp3",channel="dj8", loop=False)
        elif x == 8:
            renpy.sound.play("sound_effects/season3/dj/dj_scratch1.mp3",channel="dj9", loop=False)
        elif x == 9:
            renpy.sound.play("sound_effects/season3/dj/dj_scratch2.mp3",channel="dj10", loop=False)
        elif x == 10:
            renpy.sound.play("sound_effects/season3/dj/dj_scratch3.mp3",channel="dj11", loop=False)
        elif x == 11:
            renpy.sound.play("sound_effects/season3/dj/dj_scratch4.mp3",channel="dj12", loop=False)
        elif x == 12:
            renpy.sound.play("sound_effects/season3/dj/dj_scratch5.mp3",channel="dj13", loop=False)
        elif x == 13:
            renpy.sound.play("sound_effects/season3/dj/dj_scratch6.mp3",channel="dj14", loop=False)
        return

    def dj_cheers():
        track = renpy.random.randint(1,3)
        if track == 1:
            renpy.sound.play("sound_effects/season3/dj/dj_audience1.mp3",channel="dj15", loop=False)
        elif track == 2:
            renpy.sound.play("sound_effects/season3/dj/dj_audience2.mp3",channel="dj16", loop=False)
        elif track == 3:
            renpy.sound.play("sound_effects/season3/dj/dj_audience3.mp3",channel="dj17", loop=False)
        return
    def fight_cheers(trans,st,at):
        track = renpy.random.randint(1,3)
        if track == 1:
            renpy.sound.play("sound_effects/season3/dj/dj_audience1.mp3",channel="dj15", loop=False)
        elif track == 2:
            renpy.sound.play("sound_effects/season3/dj/dj_audience2.mp3",channel="dj16", loop=False)
        elif track == 3:
            renpy.sound.play("sound_effects/season3/dj/dj_audience3.mp3",channel="dj17", loop=False)
        return

    def dj_interrupt_check():
        global ep12_dj_interrupted
        global ep12_dj_counter
        if ep12_dj_counter > 50:
            ep12_dj_interrupted = 1
        else:
            ep12_dj_counter = 0
        return
    def dj_reset():
        global dj_keydown_a
        global dj_keydown_s
        global dj_keydown_d
        global dj_keydown_f
        global dj_keydown_j
        global dj_keydown_k
        global dj_keydown_l
        global dj_keydown_space
        global dj_keydown_q
        global dj_keydown_w
        global dj_keydown_e
        global dj_keydown_r
        global dj_keydown_t
        global dj_keydown_y
        global dj_keydown_p
        global dj_keydown_o
        dj_keydown_a = False
        dj_keydown_s = False
        dj_keydown_d = False
        dj_keydown_f = False
        dj_keydown_j = False
        dj_keydown_k = False
        dj_keydown_l = False
        dj_keydown_space = False
        dj_keydown_q = False
        dj_keydown_w = False
        dj_keydown_e = False
        dj_keydown_r = False
        dj_keydown_t = False
        dj_keydown_y = False
        dj_keydown_p = False
        dj_keydown_o = False
        return

image dj_musicbars:
    "dj_musicbars1" with Dissolve(0.2, alpha=True)
    pause 0.3
    "dj_musicbars2" with Dissolve(0.2, alpha=True)
    pause 0.3
    "dj_musicbars3" with Dissolve(0.2, alpha=True)
    pause 0.3
    "dj_musicbars4" with Dissolve(0.2, alpha=True)
    pause 0.3
    "dj_musicbars5" with Dissolve(0.2, alpha=True)
    pause 0.3
    "dj_musicbars6" with Dissolve(0.2, alpha=True)
    pause 0.3
    "dj_musicbars7" with Dissolve(0.2, alpha=True)
    pause 0.3
    repeat

style mphone_dj_bar_style:
    font "fonts/candara.ttf"
    size 28 * persistent.scale_factor
    color "#ffffff"
    outlines [ (absolute(2), "#000", absolute(1), absolute(1)) ]

init:
    default dj_keydown_a = False
    default dj_keydown_s = False
    default dj_keydown_d = False
    default dj_keydown_f = False
    default dj_keydown_j = False
    default dj_keydown_k = False
    default dj_keydown_l = False
    default dj_keydown_space = False
    default dj_keydown_q = False
    default dj_keydown_w = False
    default dj_keydown_e = False
    default dj_keydown_r = False
    default dj_keydown_t = False
    default dj_keydown_y = False
    default dj_keydown_p = False
    default dj_keydown_o = False

screen ep12_drugs_screen:
    tag ep12_drugs_screen
    modal False
    add "drugs_filter_image"

screen redacted_screen:
    key "mouseup_2" action NullAction()

    modal False tag redacted_screen
    imagebutton:
        focus_mask True
        idle "redacted_idle"
        hover "redacted_idle"
        if red_int < 5:
            action (Show("redacted_screen2"), SetVariable("red_int",red_int+1), Function(play_redacted))
        elif red_int < 105:
            action (Show("redacted_screen3"), SetVariable("red_int",105))
        else:
            action NullAction()

screen redacted_screen2:
    tag redacted_screen2
    modal False
    key "mouseup_2" action NullAction()
    timer 2 action Hide("redacted_screen2") repeat True
    add "redacted_noise" at redacted_transform2
    add "redacted_flicker" at redacted_transform
    add "redacted_flicker2" at redacted_transform
    if red_int == 2:
        add "redacted_text1" at redacted_transform2
        add "redacted_text1b" at redacted_transform2
    elif red_int == 3:
        add "redacted_text2" at redacted_transform2
        add "redacted_text2b" at redacted_transform2
    elif red_int == 4:
        add "redacted_text3" at redacted_transform2
        add "redacted_text3b" at redacted_transform2


screen redacted_screen3:
    tag redacted_screen3
    modal True
    key "mouseup_2" action NullAction()
    timer 60 action Hide("redacted_screen3") repeat True
    add "anim_redacted"

image redacted_text1:
    "red_text1"
image redacted_text1b:
    "red_text1b"
image redacted_text2:
    "red_text2"
image redacted_text2b:
    "red_text2b"
image redacted_text3:
    "red_text3"
image redacted_text3b:
    "red_text3b"

transform redacted_transform:
    alpha 0.0
    choice:
        ease 0.1 alpha 0.5
    choice:
        ease 0.1 alpha 0.2
    choice:
        ease 0.1 alpha 0.8
    choice:
        ease 0.1 alpha 0.6
    choice:
        ease 0.1 alpha 0.9
    choice:
        ease 0.1 alpha 0.1
    ease 0.1 alpha 0.0
    repeat
transform redacted_transform2:
    alpha .7
    choice:
        ease 0.1 alpha 0.5
    choice:
        ease 0.1 alpha 0.2
    choice:
        ease 0.1 alpha 0.8
    choice:
        ease 0.1 alpha 0.6
    choice:
        ease 0.1 alpha 0.9
    choice:
        ease 0.1 alpha 0.1
    ease 0.1 alpha 0.7
    repeat
image redacted_noise:
    "red_noise1"
    pause 0.1
    "red_noise2"
    pause 0.1
    "red_noise3"
    pause 0.1
    "red_noise4"
    pause 0.1
    repeat
image redacted_flicker:
    "redacted_fr0"
    pause 0.05
    "redacted_fr1"
    pause 0.05
    repeat

image redacted_flicker2:
    "redacted_fr0b"
    pause 0.09
    "redacted_fr1b"
    pause 0.09
    repeat

screen ep12_dj_screen:
    tag ep12_dj_screen
    modal True

    add "dj_turntable_idle"
    add "dj_musicbar"
    add "dj_musicbars"
    key ["keyup_K_SPACE"] action SetVariable("dj_keydown_space", False)
    key ["keydown_K_SPACE"] action (Function(dj_play_music,3), SetVariable("dj_keydown_space", True))
    key ["keyup_K_a"] action SetVariable("dj_keydown_a", False)
    key ["keydown_K_a"] action (Function(dj_play_music,4), SetVariable("dj_keydown_a", True))
    key ["keyup_K_s"] action SetVariable("dj_keydown_s", False)
    key ["keydown_K_s"] action (Function(dj_play_music,6), SetVariable("dj_keydown_s", True))
    key ["keyup_K_d"] action SetVariable("dj_keydown_d", False)
    key ["keydown_K_d"] action (Function(dj_play_music,1), SetVariable("dj_keydown_d", True))
    key ["keyup_K_f"] action SetVariable("dj_keydown_f", False)
    key ["keydown_K_f"] action (Function(dj_play_music,0), SetVariable("dj_keydown_f", True))
    key ["keyup_K_j"] action SetVariable("dj_keydown_j", False)
    key ["keydown_K_j"] action (Function(dj_play_music,2), SetVariable("dj_keydown_j", True))
    key ["keyup_K_k"] action SetVariable("dj_keydown_k", False)
    key ["keydown_K_k"] action (Function(dj_play_music,5), SetVariable("dj_keydown_k", True))
    key ["keyup_K_l"] action SetVariable("dj_keydown_l", False)
    key ["keydown_K_l"] action (Function(dj_play_music,7), SetVariable("dj_keydown_l", True))
    key ["keyup_K_q"] action SetVariable("dj_keydown_q", False)
    key ["keydown_K_q"] action (Function(dj_play_music,8), SetVariable("dj_keydown_q", True))
    key ["keyup_K_w"] action SetVariable("dj_keydown_w", False)
    key ["keydown_K_w"] action (Function(dj_play_music,9), SetVariable("dj_keydown_w", True))
    key ["keyup_K_e"] action SetVariable("dj_keydown_e", False)
    key ["keydown_K_e"] action (Function(dj_play_music,10), SetVariable("dj_keydown_e", True))
    key ["keyup_K_r"] action SetVariable("dj_keydown_r", False)
    key ["keydown_K_r"] action (Function(dj_play_music,11), SetVariable("dj_keydown_r", True))
    key ["keyup_K_t"] action SetVariable("dj_keydown_t", False)
    key ["keydown_K_t"] action (Function(dj_play_music,12), SetVariable("dj_keydown_t", True))
    key ["keyup_K_y"] action SetVariable("dj_keydown_y", False)
    key ["keydown_K_y"] action (Function(dj_play_music,13), SetVariable("dj_keydown_y", True))
    key ["keyup_K_o"] action SetVariable("dj_keydown_o", False)
    key ["keydown_K_o"] action (Return(), Jump("ep12_np_dj2_label"), SetVariable("dj_keydown_o", True))
    key ["keyup_K_p"] action SetVariable("dj_keydown_p", False)
    key ["keydown_K_p"] action (Function(mphone_next_song), SetVariable("dj_keydown_p", True))



    if ep12_dj_interrupted == 0:
        timer 10 repeat True action Function(dj_interrupt_check)
    elif ep12_dj_interrupted == 1:
        timer 0.5 repeat False action (Return(),Jump("ep12_np_dj_interrupted_label"))

    timer 30 repeat True action Function(dj_cheers)

    hbox:
        spacing 8 * persistent.scale_factor
        xalign 0.22
        yalign 0.5
        vbox:
            xminimum 650 * persistent.scale_factor
            xmaximum 650 * persistent.scale_factor
            yalign 0.5
            xoffset 16 * persistent.scale_factor
            $ tmpBool = False
            for x in range(0,len(persistent.mphone_music_list)):
                if renpy.music.get_playing() == persistent.mphone_music_list[x][1]:
                    $ tmpList = persistent.mphone_music_list[x][0].split(" - ", 1)
                    text "{color=ffed00}Now playing{/color}" style "mphone_dj_bar_style"
                    text "%s - %s" % (tmpList[1], tmpList[0]) style "mphone_dj_bar_style"
                    $ tmpBool = True
            if not tmpBool:
                text "-" style "mphone_dj_bar_style"
                text "-" style "mphone_dj_bar_style"

    imagebutton:
        focus_mask True
        if dj_keydown_f:
            idle "dj_clap_hover"
        else:
            idle "dj_clap_idle"
        hover "dj_clap_hover"
        action Function(dj_play_music,0)
    imagebutton:
        focus_mask True
        if dj_keydown_d:
            idle "dj_drop_hover"
        else:
            idle "dj_drop_idle"
        hover "dj_drop_hover"
        action Function(dj_play_music,1)
    imagebutton:
        focus_mask True
        if dj_keydown_j:
            idle "dj_horn_hover"
        else:
            idle "dj_horn_idle"
        hover "dj_horn_hover"
        action Function(dj_play_music,2)
    imagebutton:
        focus_mask True
        if dj_keydown_space:
            idle "dj_kick_hover"
        else:
            idle "dj_kick_idle"
        hover "dj_kick_hover"
        action Function(dj_play_music,3)
    imagebutton:
        focus_mask True
        if dj_keydown_a:
            idle "dj_heavy_hit_hover"
        else:
            idle "dj_heavy_hit_idle"
        hover "dj_heavy_hit_hover"
        action Function(dj_play_music,4)
    imagebutton:
        focus_mask True
        if dj_keydown_k:
            idle "dj_riser_hover"
        else:
            idle "dj_riser_idle"
        hover "dj_riser_hover"
        action Function(dj_play_music,5)
    imagebutton:
        focus_mask True
        if dj_keydown_s:
            idle "dj_spin_hover"
        else:
            idle "dj_spin_idle"
        hover "dj_spin_hover"
        action Function(dj_play_music,6)
    imagebutton:
        focus_mask True
        if dj_keydown_l:
            idle "dj_stop_hover"
        else:
            idle "dj_stop_idle"
        hover "dj_stop_hover"
        action Function(dj_play_music,7)
    imagebutton:
        focus_mask True
        if dj_keydown_q:
            idle "dj_turntable_q_hover"
        else:
            idle "dj_turntable_q_idle"
        hover "dj_turntable_q_hover"
        action Function(dj_play_music,8)
    imagebutton:
        focus_mask True
        if dj_keydown_w:
            idle "dj_turntable_w_hover"
        else:
            idle "dj_turntable_w_idle"
        hover "dj_turntable_w_hover"
        action Function(dj_play_music,9)
    imagebutton:
        focus_mask True
        if dj_keydown_e:
            idle "dj_turntable_e_hover"
        else:
            idle "dj_turntable_e_idle"
        hover "dj_turntable_e_hover"
        action Function(dj_play_music,10)
    imagebutton:
        focus_mask True
        if dj_keydown_r:
            idle "dj_turntable_r_hover"
        else:
            idle "dj_turntable_r_idle"
        hover "dj_turntable_r_hover"
        action Function(dj_play_music,11)
    imagebutton:
        focus_mask True
        if dj_keydown_t:
            idle "dj_turntable_t_hover"
        else:
            idle "dj_turntable_t_idle"
        hover "dj_turntable_t_hover"
        action Function(dj_play_music,12)
    imagebutton:
        focus_mask True
        if dj_keydown_y:
            idle "dj_turntable_y_hover"
        else:
            idle "dj_turntable_y_idle"
        hover "dj_turntable_y_hover"
        action Function(dj_play_music,13)
    imagebutton:
        focus_mask True
        if dj_keydown_o:
            idle "dj_quit_hover"
        else:
            idle "dj_quit_idle"
        hover "dj_quit_hover"
        action (Return(), Jump("ep12_np_dj2_label"))
    imagebutton:
        focus_mask True
        if dj_keydown_p:
            idle "dj_next_song_hover"
        else:
            idle "dj_next_song_idle"
        hover "dj_next_song_hover"
        action Function(mphone_next_song)

init:

    $ renpy.music.register_channel("dj1", "sfx")
    $ renpy.music.register_channel("dj2", "sfx")
    $ renpy.music.register_channel("dj3", "sfx")
    $ renpy.music.register_channel("dj4", "sfx")
    $ renpy.music.register_channel("dj5", "sfx")
    $ renpy.music.register_channel("dj6", "sfx")
    $ renpy.music.register_channel("dj7", "sfx")
    $ renpy.music.register_channel("dj8", "sfx")
    $ renpy.music.register_channel("dj9", "sfx")
    $ renpy.music.register_channel("dj10", "sfx")
    $ renpy.music.register_channel("dj11", "sfx")
    $ renpy.music.register_channel("dj12", "sfx")
    $ renpy.music.register_channel("dj13", "sfx")
    $ renpy.music.register_channel("dj14", "sfx")
    $ renpy.music.register_channel("dj15", "sfx")
    $ renpy.music.register_channel("dj16", "sfx")
    $ renpy.music.register_channel("dj17", "sfx")
    $ renpy.music.register_channel("sex1", mixer="sex_sounds", movie=True)
    $ renpy.music.register_channel("sex2", mixer="sex_sounds", movie=True)
    $ renpy.music.register_channel("sex3", mixer="sex_sounds", movie=True)
    $ renpy.music.register_channel("sex4", mixer="sex_sounds", movie=True)
    $ renpy.music.register_channel("sex5", mixer="sex_sounds", movie=True)
    $ renpy.music.register_channel("sex6", mixer="sex_sounds", movie=True)
    $ renpy.music.register_channel("sex7", mixer="sex_sounds", movie=True)
    $ renpy.music.register_channel("sex8", mixer="sex_sounds", movie=True)
    $ renpy.music.register_channel("sex9", mixer="sex_sounds", movie=True)
    $ renpy.music.register_channel("sex10", mixer="sex_sounds", movie=True)
    $ renpy.music.register_channel("sex11", mixer="sex_sounds", movie=True)
    $ renpy.music.register_channel("sex12", mixer="sex_sounds", movie=True)
    $ renpy.music.register_channel("sex13", mixer="sex_sounds", movie=True)
    $ renpy.music.register_channel("sex14", mixer="sex_sounds", movie=True)
    $ renpy.music.register_channel("sex15", mixer="sex_sounds", movie=True)
    $ renpy.music.register_channel("sex16", mixer="sex_sounds", movie=True)
    $ renpy.music.register_channel("sex17", mixer="sex_sounds", movie=True)
    $ renpy.music.register_channel("sex18", mixer="sex_sounds", movie=True)
    $ renpy.music.register_channel("sex19", mixer="sex_sounds", movie=True)
    $ renpy.music.register_channel("sex20", mixer="sex_sounds", movie=True)
    $ renpy.music.register_channel("sex21", mixer="sex_sounds", movie=True)

init -1 python:
    def play_redacted():
        if renpy.random.randint(0,10)<3:
            renpy.play("sound_effects/season3/redacted1.mp3", "sfx3")
        elif renpy.random.randint(0,10)<5:
            renpy.play("sound_effects/season3/redacted2.mp3", "sfx3")
        else:
            renpy.play("sound_effects/season3/redacted3.mp3", "sfx3")

    def play_cum1(trans,st,at):
        renpy.play("sound_effects/season3/cum1.mp3", channel = "sex21")
    def play_cum2(trans,st,at):
        renpy.play("sound_effects/season3/cum2.mp3", channel = "sex21")
    def play_cum3(trans,st,at):
        renpy.play("sound_effects/season3/cum3.mp3", channel = "sex21")

transform cum1:
    function play_cum1
transform cum2:
    function play_cum2
transform cum3:
    function play_cum3
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
