style text_timer:
    size 30
    color "#FFF"
    outlines [(2, "#000", 0, 0)]

init python:
    elapsed_time = 0.0
    pause_stopwatch = False  # Initialize pause_stopwatch variable
    paused_stopwatch_value = 0.0  # Define paused_stopwatch_value variable at the top level

    def text_stopwatch( st, at,
                        time_scale=1.0,
                        text_format="{seconds:02d}:{milliseconds:03d}" ):

        global elapsed_time, pause_stopwatch

        if pause_stopwatch:  # Check if stopwatch should be paused
            return Text(text_format.format(seconds=int(elapsed_time % 60), milliseconds=int((elapsed_time % 1) * 1000)), style='text_timer'), .1

        elapsed = st * time_scale
        elapsed_time = elapsed

        parts_dict = {
            'seconds': int(elapsed % 60),
            'milliseconds': int((elapsed % 1) * 1000),
        }

        return Text(text_format.format(**parts_dict), style='text_timer'), .1

screen text_timer(time_scale=1.0):
    fixed:
        xpos 0.407
        hbox:
            text "Thought Process: " style "text_timer"
            add DynamicDisplayable(text_stopwatch, time_scale=time_scale)

screen paused_text_timer(paused_stopwatch_value):
    fixed:
        xpos 0.5
        ypos 0.5
        hbox:
            text "Thought Process" yalign 0.5 style "text_timer"
            text "{:02d}:{:03d}".format(
                int(paused_stopwatch_value % 60),
                int((paused_stopwatch_value % 1) * 1000)
            ) style "text_timer"

