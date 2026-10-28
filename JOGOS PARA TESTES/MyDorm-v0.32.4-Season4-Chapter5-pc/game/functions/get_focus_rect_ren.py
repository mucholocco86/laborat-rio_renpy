import renpy

"""renpy
init -999 python:
"""

def get_focus_rect ():
    focus_coordinates = renpy.focus_coordinates ()
    if focus_coordinates [0] is None:
        return { "x" : 0, "y" : 0, "width" : 0, "height" : 0, }
    return {
        "x" : int (focus_coordinates [0]),
        "y" : int (focus_coordinates [1]),
        "width" : int (focus_coordinates [2]),
        "height" : int (focus_coordinates [3]),
    }