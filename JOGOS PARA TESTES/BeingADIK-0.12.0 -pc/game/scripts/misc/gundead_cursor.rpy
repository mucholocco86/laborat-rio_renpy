screen gundead_screen:
    tag gundead_screen
    modal False
    add TrackGDCursor("[persistent.img_dir]/ep10/arcade/gundead_crosshair.png")
screen gundead_screen_civ:
    tag gundead_screen_civ
    modal False
    timer 4.5 action (Hide("gundead_screen_civ"),Jump("ep10_gundead_civ_alive_label"))
screen gundead_splat_screen:
    tag gundead_splat_screen
    modal False
    add "gundead_splat1"
    timer 0.2 action Hide("gundead_splat_screen")
screen gundead_splat2_screen:
    tag gundead_splat2_screen
    modal False
    add "gundead_splat2"
    timer 0.2 action Hide("gundead_splat2_screen")
screen gundead_screen_boss:
    tag gundead_screen_boss
    modal False
    imagebutton:
        idle "gd_hbb"
        hover "gd_hbb"
        xalign 0.5
        yalign 0.5
        action (Play("sfx1","sound_effects/season3/gunshot.mp3", loop=False),SetVariable("tmpInt",tmpInt+1))
screen gundead_screen_win:
    tag gundead_screen_win
    modal False
    add "gundead_ol1" at gd_transform
    add "gundead_ol2" at gd_transform
    text "INSERT COIN TO CONTINUE" style "gd_style" xalign 0.5 yalign 0.8

style gd_style:
    font "fonts/candara.ttf"
    size 50 * persistent.scale_factor
    color "#c4bcb6"
    outlines [ (absolute(1), "#090909", absolute(1), absolute(1)) ]

screen gundead_screen_loss:
    tag gundead_screen_loss
    modal False
    add "gundead_ol1" at gd_transform
    add "gundead_ol3" at gd_transform
    text "INSERT COIN TO RETRY" style "gd_style" xalign 0.5 yalign 0.8

transform gd_transform:
    zoom 1.0
    choice:
        easein 0.5 zoom 1.01
    choice:
        easein 0.7 zoom 1.02
    easein 0.5 zoom 1.0
    repeat

screen gundead_screen_zombies:
    tag gundead_screen_zombies
    modal False
    if not False in tmpList:
        timer 0.1 action Jump("ep10_gundead_3_label")
    if tmpList[0]:
        add "gd_hb1b"
    else:
        imagebutton:
            idle "gd_hb1"
            hover "gd_hb1"
            xalign 0.05
            yalign 1.0
            action SetDict(tmpList,0,True)
    if tmpList[1]:
        add "gd_hb2b"
    else:
        imagebutton:
            idle "gd_hb2"
            hover "gd_hb2"
            xalign 0.3
            yalign 0.4
            action SetDict(tmpList,1,True)
    if tmpList[2]:
        add "gd_hb3b"
    else:
        imagebutton:
            idle "gd_hb3"
            hover "gd_hb3"
            xalign 0.475
            yalign 0.8
            action SetDict(tmpList,2,True)
    if tmpList[3]:
        add "gd_hb4b"
    else:
        imagebutton:
            idle "gd_hb4"
            hover "gd_hb4"
            xalign 0.48
            yalign 0.3
            action SetDict(tmpList,3,True)
    if tmpList[4]:
        add "gd_hb5b"
    else:
        imagebutton:
            idle "gd_hb5"
            hover "gd_hb5"
            xalign 0.7
            yalign 0.4
            action SetDict(tmpList,4,True)


init python:

    class TrackGDCursor(renpy.Displayable):
        
        def __init__(self, child):
            
            super(TrackGDCursor, self).__init__()
            
            self.child = renpy.displayable(child)
            
            self.x = None
            self.y = None
        
        def render(self, width, height, st, at):
            
            rv = renpy.Render(width, height)
            
            if self.x < 0 or self.y  < 0 or self.x > config.screen_width or self.y > config.screen_height:
                
                return rv
            
            if self.x is not None:
                cr = renpy.render(self.child, width, height, st, at)
                cw, ch = cr.get_size()
                rv.blit(cr, (self.x - cw / 2, self.y - ch / 2))
            
            return rv
        
        def event(self, ev, x, y, st):
            
            if (x != self.x) or (y != self.y):
                self.x = x
                self.y = y
                renpy.redraw(self, 0)
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
