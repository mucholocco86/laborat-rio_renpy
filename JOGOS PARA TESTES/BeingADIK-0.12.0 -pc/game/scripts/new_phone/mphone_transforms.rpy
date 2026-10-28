transform mphone_show_transform:
    xalign 0.5 yalign 0.5
    on show:
        yoffset 1080 * persistent.scale_factor
        easein 0.2 yoffset 0
    on hide:
        yoffset 0
        easein 0.2 yoffset 1080 * persistent.scale_factor

transform mphone_bg_transform:
    on show:
        alpha 0.0
        easein 0.2 alpha 1.0
    on hide:
        alpha 1.0
        easein 0.2 alpha 0.0

transform mphone_app_zoom:
    zoom 0.4

transform mphone_off_transform:
    zoom 0.15

transform mphone_gallery_transform:
    zoom 0.5

transform mphone_app_transform:
    on show:
        zoom 0 xalign 0.5 yalign 0.5
        easein 0.2 zoom 1.0
    on hide:
        zoom 1.0 xalign 0.5 yalign 0.5
        easein 0.2 zoom 0.0

transform mphone_show_transform_alt:
    on show:
        zoom 0.0 xalign 0.5 yalign 0.5
        linear 0.1 alpha 1.0
        zoom 1.0

transform mphone_rotate_90cw_zoom:
    rotate 90
    zoom 0.3
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
