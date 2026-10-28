screen ep7_cluck_photo_tybalt1:
    tag ep7_cluck_photo_tybalt1
    key "mouseup_2" action Hide("ep7_cluck_photo_tybalt1")
    add "[persistent.img_dir]/phone_content/episode_interlude/ep7_cluck_photo_tybalt1.png"
    vbox xalign 0.5 yalign 0.5:
        imagebutton:
            focus_mask True
            idle Transform ("[persistent.img_dir]/rewards/general/invisible_rew_button.png")
            hover Transform ("[persistent.img_dir]/rewards/general/invisible_rew_button.png")
            action Hide("ep7_cluck_photo_tybalt1")

screen ep7_cluck_photo_derek:
    tag ep7_cluck_photo_derek
    key "mouseup_2" action Hide("ep7_cluck_photo_derek")
    add "[persistent.img_dir]/phone_content/episode_interlude/ep7_cluck_photo_derek.png"
    vbox xalign 0.5 yalign 0.5:
        imagebutton:
            focus_mask True
            idle Transform ("[persistent.img_dir]/rewards/general/invisible_rew_button.png")
            hover Transform ("[persistent.img_dir]/rewards/general/invisible_rew_button.png")
            action Hide("ep7_cluck_photo_derek")

screen ep7_cluck_photo_leon:
    tag ep7_cluck_photo_leon
    key "mouseup_2" action Hide("ep7_cluck_photo_leon")
    add "[persistent.img_dir]/phone_content/episode_interlude/ep7_cluck_photo_leon.png"
    vbox xalign 0.5 yalign 0.5:
        imagebutton:
            focus_mask True
            idle Transform ("[persistent.img_dir]/rewards/general/invisible_rew_button.png")
            hover Transform ("[persistent.img_dir]/rewards/general/invisible_rew_button.png")
            action Hide("ep7_cluck_photo_leon")

screen ep7_cluck_photo_jimmy:
    tag ep7_cluck_photo_jimmy
    key "mouseup_2" action Hide("ep7_cluck_photo_jimmy")
    add "[persistent.img_dir]/phone_content/episode_interlude/ep7_cluck_photo_jimmy.png"
    vbox xalign 0.5 yalign 0.5:
        imagebutton:
            focus_mask True
            idle Transform ("[persistent.img_dir]/rewards/general/invisible_rew_button.png")
            hover Transform ("[persistent.img_dir]/rewards/general/invisible_rew_button.png")
            action Hide("ep7_cluck_photo_jimmy")

screen ep7_cluck_photo_jamie:
    tag ep7_cluck_photo_jamie
    key "mouseup_2" action Hide("ep7_cluck_photo_jamie")
    add "[persistent.img_dir]/phone_content/episode_interlude/ep7_cluck_photo_jamie.png"
    vbox xalign 0.5 yalign 0.5:
        imagebutton:
            focus_mask True
            idle Transform ("[persistent.img_dir]/rewards/general/invisible_rew_button.png")
            hover Transform ("[persistent.img_dir]/rewards/general/invisible_rew_button.png")
            action Hide("ep7_cluck_photo_jamie")

screen ep7_cluck_photo_ashley:
    tag ep7_cluck_photo_ashley
    key "mouseup_2" action Hide("ep7_cluck_photo_ashley")
    add "[persistent.img_dir]/phone_content/episode_interlude/ep7_cluck_photo_ashley.png"
    vbox xalign 0.5 yalign 0.5:
        imagebutton:
            focus_mask True
            idle Transform ("[persistent.img_dir]/rewards/general/invisible_rew_button.png")
            hover Transform ("[persistent.img_dir]/rewards/general/invisible_rew_button.png")
            action Hide("ep7_cluck_photo_ashley")

screen ep7_cluck_photo_sage:
    tag ep7_cluck_photo_sage
    key "mouseup_2" action Hide("ep7_cluck_photo_sage")
    add "[persistent.img_dir]/phone_content/episode_interlude/ep7_cluck_photo_sage.png"
    vbox xalign 0.5 yalign 0.5:
        imagebutton:
            focus_mask True
            idle Transform ("[persistent.img_dir]/rewards/general/invisible_rew_button.png")
            hover Transform ("[persistent.img_dir]/rewards/general/invisible_rew_button.png")
            action Hide("ep7_cluck_photo_sage")

screen ep7_cluck_photo_mc:
    tag ep7_cluck_photo_mc
    key "mouseup_2" action Hide("ep7_cluck_photo_mc")
    add "[persistent.img_dir]/phone_content/episode_interlude/ep7_cluck_photo_mc.png"
    vbox xalign 0.5 yalign 0.5:
        imagebutton:
            focus_mask True
            idle Transform ("[persistent.img_dir]/rewards/general/invisible_rew_button.png")
            hover Transform ("[persistent.img_dir]/rewards/general/invisible_rew_button.png")
            action Hide("ep7_cluck_photo_mc")

screen ep7_cluck_photo_jill:
    tag ep7_cluck_photo_jill
    key "mouseup_2" action Hide("ep7_cluck_photo_jill")
    add "[persistent.img_dir]/phone_content/episode_interlude/ep7_cluck_photo_jill.png"
    vbox xalign 0.5 yalign 0.5:
        imagebutton:
            focus_mask True
            idle Transform ("[persistent.img_dir]/rewards/general/invisible_rew_button.png")
            hover Transform ("[persistent.img_dir]/rewards/general/invisible_rew_button.png")
            action Hide("ep7_cluck_photo_jill")

screen ep7_cluck_photo_isabella:
    tag ep7_cluck_photo_isabella
    key "mouseup_2" action Hide("ep7_cluck_photo_isabella")
    add "[persistent.img_dir]/phone_content/episode_interlude/ep7_cluck_photo_isabella.png"
    vbox xalign 0.5 yalign 0.5:
        imagebutton:
            focus_mask True
            idle Transform ("[persistent.img_dir]/rewards/general/invisible_rew_button.png")
            hover Transform ("[persistent.img_dir]/rewards/general/invisible_rew_button.png")
            action Hide("ep7_cluck_photo_isabella")

screen ep7_cluck_photo_riona:
    tag ep7_cluck_photo_riona
    key "mouseup_2" action Hide("ep7_cluck_photo_riona")
    add "anim_riona_cluck_ep7" at truecenter
    vbox xalign 0.5 yalign 0.5:
        imagebutton:
            focus_mask True
            idle Transform ("[persistent.img_dir]/rewards/general/invisible_rew_button.png")
            hover Transform ("[persistent.img_dir]/rewards/general/invisible_rew_button.png")
            action Hide("ep7_cluck_photo_riona")

image anim_riona_cluck_ep7 = Movie(play="%s/phone_content/episode_interlude/anim_riona_cluck_ep7.webm" % persistent.img_dir, channel = "sex1")
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
