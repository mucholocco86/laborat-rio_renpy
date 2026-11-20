screen JK_Icon(icon, color=None, hover_color=None, size=None, xalign=None, outlines=None):
    style_prefix "JK"

    frame style "JK_default":
        has hbox
        if icon:
            text icon style 'JK_Icon':
                if color:
                    color color
                if hover_color:
                    hover_color hover_color
                if size:
                    size JK.scaled(size)
                if xalign:
                    xalign xalign
                if outlines:
                    outlines outlines
        transclude
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
