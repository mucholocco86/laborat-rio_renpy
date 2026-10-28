transform fleft(wait = 0):

    subpixel True
    

    xoffset -250
    alpha 0.0
    blur 25
    pause wait * persistent.motion
    easein_quint (0.5 * persistent.motion) alpha 1.0 xoffset 0 blur 0

transform fbottom(wait = 0):

    subpixel True
    
    perspective True
    matrixtransform RotateMatrix(0, 90, 0)
    yoffset 150
    alpha 0.0
    blur 25
    pause wait * persistent.motion
    easein_quint (0.5 * persistent.motion) alpha 1.0 yoffset 0 blur 0 matrixtransform RotateMatrix(0, 0, 0)

transform pp2_fl(wait = 0):

    subpixel True
    

    xoffset -250
    alpha 0.0
    blur 25
    easein_quint (0.5 * persistent.motion) alpha 1.0 blur 0 xoffset 0

transform pp2_fade_in(wait = 0):

    subpixel True
    

    alpha 0.0
    blur 25
    easein_quint (0.5 * persistent.motion) alpha 1.0 blur 0

transform pp2_fb(wait = 0):

    subpixel True
    

# on show:
    yoffset -560
    perspective True
    matrixtransform RotateMatrix(-180, 0, 0)
    alpha 0.0
    blur 5
    pause wait * persistent.motion
    easein_quint (1 * persistent.motion) alpha 1.0 yoffset 0 blur 0 matrixtransform RotateMatrix(0, 0, 0)

    on idle:
        easein_quint (0.5 * persistent.motion) yoffset 0
    
    on hover:
        easein_quint (0.5 * persistent.motion) yoffset 15

transform hearts_h():

    subpixel True
    
    xoffset -1080
    alpha .0
    blur 25
    pause 0.05
    easein_quint (0.5 * persistent.motion) alpha 1.0 xoffset 0 blur 0

transform background_m():

    subpixel True
    

    blur 25
    xalign 0.5
    yalign 0.5
    xzoom 1.5
    yzoom 1.5
    ease_quint (1.5 * persistent.motion) blur 0 xzoom 1.0 yzoom 1.0

transform top_m(wait = 0):

    subpixel True
    

    yoffset -500
    blur 5
    alpha 0.0
    xalign 0.5
    yalign 0.5
    xzoom 1.5
    yzoom 1.5
    pause wait * persistent.motion
    easein_quint (1.0 * persistent.motion) alpha 1.0 yoffset 0 blur 0 xzoom 1.0 yzoom 1.0

transform exit_m(wait = 0):

    subpixel True
    

    xalign 0.5
    yalign 0.5
    xzoom 0.0
    yzoom 0.0
    # zoom 0.0
    blur 5
    alpha 0.0
    pause wait * persistent.motion
    easein_quint (1.0 * persistent.motion) alpha 1.0 xzoom 1.0 yzoom 1.0 blur 0

transform socials_t(wait = 0):

    subpixel True
    

    yoffset 500
    blur 5
    alpha 0.0
    pause wait * persistent.motion
    ease_quint (1.0 * persistent.motion) alpha 1.0 yoffset 0 blur 0

transform label_t():

    subpixel True
    
    yoffset -500
    blur 5
    alpha 0.0
    xalign 0.5
    yalign 0.5
    xzoom 1.5
    yzoom 1.5
    easein_quint (1.0 * persistent.motion) alpha 1.0 yoffset 0 blur 0 xzoom 1.0 yzoom 1.0


transform mm_hover_zoom():

    subpixel True
    
    xycenter (.5, .5)
    align    (.5, .5)

    zoom 1.0
    
    on idle:
        easein_quint (.5 * persistent.motion) zoom 1.0
    on hover:
        easein_quint (.5 * persistent.motion) zoom 1.1

transform BAPR():

    subpixel True
    
    easein_quint (.5 * persistent.motion) alpha 1.0
transform BDPR():

    subpixel True
    
    easein_quint (.5 * persistent.motion) alpha .0 
transform BNT():
    alpha .0

transform quit_bb(wait = 0):

    subpixel True

    xycenter (.5, .5)
    align    (.5, .5)

    alpha  .0
    offset (0, 1080)
    blur    25
    zoom   .0

    pause wait * persistent.motion

    easein_quint (.75 * persistent.motion) alpha 1.0 offset (0, 0) blur 0 zoom 1.0

transform quit_yes():

    subpixel True
    

    matrixcolor ColorizeMatrix('#1c2129', '#1c2129')

    on idle:
        linear (.5 * persistent.motion) matrixcolor ColorizeMatrix('#1c2129', '#1c2129')
    on hover:
        linear (.5 * persistent.motion) matrixcolor ColorizeMatrix('#1c2129', '#ff6961')

transform quit_no():

    subpixel True
    
    
    matrixcolor ColorizeMatrix('#1c2129', '#1c2129')

    on idle:
        linear (.5 * persistent.motion) matrixcolor ColorizeMatrix('#1c2129', '#1c2129')
    on hover:
        linear (.5 * persistent.motion) matrixcolor ColorizeMatrix('#1c2129', '#00ffcc')