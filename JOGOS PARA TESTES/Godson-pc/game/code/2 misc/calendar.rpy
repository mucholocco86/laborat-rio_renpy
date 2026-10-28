




default calendar_from_day = "MONDAY"
default calendar_from_date = 3
default calendar_to_day = "TUESDAY"
default calendar_to_date = 4
default calendar_month_name = "JUNE"
default calendar_year = 2024
default calendar_weather = "CLEAR SKIES"
default calendar_temperature = "72°F"
default calendar_period = "MORNING"


transform godson_calendar_backdrop:
    alpha 0.0
    linear 0.35 alpha 1.0


transform godson_calendar_header:
    alpha 0.0
    yoffset -36
    pause 0.10
    easeout 0.35 alpha 1.0 yoffset 0


transform godson_calendar_old_date:
    alpha 0.0
    xoffset -180
    pause 0.20
    easeout 0.42 alpha 1.0 xoffset 0
    pause 0.78
    easein 0.32 alpha 0.0 xoffset -220


transform godson_calendar_old_label:
    alpha 0.0
    xoffset -90
    pause 0.28
    easeout 0.36 alpha 1.0 xoffset 0
    pause 0.76
    easein 0.28 alpha 0.0 xoffset -120


transform godson_calendar_new_date:
    alpha 0.0
    xoffset 240
    pause 1.32
    easeout 0.52 alpha 1.0 xoffset 0
    easeout 0.12 xoffset -12
    easein 0.12 xoffset 0


transform godson_calendar_new_label:
    alpha 0.0
    xoffset 100
    pause 1.48
    easeout 0.42 alpha 1.0 xoffset 0


transform godson_calendar_weather:
    alpha 0.0
    yoffset 50
    pause 2.00
    easeout 0.46 alpha 1.0 yoffset 0


transform godson_calendar_timeline:
    alpha 0.0
    yoffset 28
    pause 1.70
    easeout 0.38 alpha 1.0 yoffset 0


transform godson_calendar_signal:
    alpha 0.26
    ease 0.70 alpha 0.85
    ease 0.70 alpha 0.26
    repeat


transform godson_calendar_sweep:
    alpha 0.0
    xoffset -850
    pause 0.86
    linear 0.12 alpha 0.75
    linear 0.70 xoffset 4700 alpha 0.0


transform godson_calendar_final_pulse:
    alpha 0.0
    pause 1.86
    linear 0.10 alpha 0.36
    ease 0.55 alpha 0.95
    ease 0.70 alpha 0.48
    repeat


screen godson_day_transition(from_day, from_date, to_day, to_date, month_name, display_year, weather, temperature, period):


    modal True
    zorder 250

    $ from_number = "{:02d}".format(int(from_date))
    $ to_number = "{:02d}".format(int(to_date))

    timer 7.5 action Return()

    fixed:
        xsize config.screen_width
        ysize config.screen_height
        at godson_calendar_backdrop

        add Solid("#03070A")
        add Solid("#08121AEF"):
            xpos 120
            ypos 105
            xsize 3600
            ysize 1950



        add Solid("#13263180"):
            xpos 120
            ypos 105
            xsize 17
            ysize 1950

        add Solid("#3CDFFF"):
            xpos 120
            ypos 105
            xsize 17
            ysize 330
            at godson_calendar_signal

        add Solid("#10232D66"):
            xpos 2600
            ypos -260
            xsize 18
            ysize 2800
            rotate 18

        add Solid("#3CDFFF18"):
            xpos 2720
            ypos -260
            xsize 5
            ysize 2800
            rotate 18

        add Solid("#FFFFFF0A"):
            xpos 3000
            ypos -260
            xsize 390
            ysize 2800
            rotate 18


        add Solid("#3CDFFF"):
            xpos 0
            ypos 110
            xsize 12
            ysize 1935
            rotate 18
            at godson_calendar_sweep

        fixed:
            xpos 230
            ypos 190
            xsize 3380
            ysize 180
            at godson_calendar_header

            text "GODSON":
                xpos 0
                ypos 0
                font gui.interface_text_font
                size 64
                color "#FFFFFF"
                kerning 2

            text "DATE TRANSITION // NEXT DAY":
                xpos 4
                ypos 82
                font gui.interface_text_font2
                size 26
                color "#3CDFFF"
                kerning 6

            text str(display_year):
                xalign 1.0
                ypos 18
                font gui.interface_text_font2
                size 34
                color "#9FB0B8"
                kerning 3

            add Solid("#3CDFFF"):
                xpos 0
                ypos 142
                xsize 260
                ysize 6

            add Solid("#2C424D"):
                xpos 260
                ypos 144
                xsize 3120
                ysize 2


        fixed:
            xpos 390
            ypos 495
            xsize 1320
            ysize 910
            at godson_calendar_old_date

            text from_number:
                xalign 0.0
                yalign 0.0
                font gui.interface_text_font
                size 720
                color "#6E7F87"
                outlines [(4, "#00000066", 0, 6)]

        fixed:
            xpos 440
            ypos 1260
            xsize 1220
            ysize 230
            at godson_calendar_old_label

            text "PREVIOUS DAY":
                ypos 0
                font gui.interface_text_font2
                size 25
                color "#8999A0"
                kerning 5

            text "[from_day] // [month_name] [from_number]":
                ypos 55
                font gui.interface_text_font
                size 55
                color "#C0C9CD"
                kerning 1


        fixed:
            xpos 1730
            ypos 410
            xsize 1500
            ysize 1040
            at godson_calendar_new_date

            text to_number:
                xalign 0.5
                yalign 0.0
                font gui.interface_text_font
                size 850
                color "#F7FBFC"
                outlines [(9, "#3CDFFF2C", 0, 0), (3, "#071016E6", 0, 8)]


        fixed:
            xpos 1820
            ypos 1290
            xsize 1320
            ysize 150
            at godson_calendar_final_pulse

            add Solid("#3CDFFF"):
                xpos 0
                ypos 0
                xsize 1320
                ysize 4

            add Solid("#3CDFFF"):
                xpos 0
                ypos 0
                xsize 6
                ysize 92

        fixed:
            xpos 1845
            ypos 1320
            xsize 1300
            ysize 210
            at godson_calendar_new_label

            text "CURRENT DAY":
                ypos 0
                font gui.interface_text_font2
                size 25
                color "#3CDFFF"
                kerning 5

            text "[to_day] // [month_name] [to_number], [display_year]":
                ypos 55
                font gui.interface_text_font
                size 62
                color "#FFFFFF"
                kerning 1



        frame:
            xpos 2400
            ypos 1580
            xsize 1090
            ysize 285
            background Solid("#0B171ED9")
            padding (38, 28)
            at godson_calendar_weather

            add Solid("#3CDFFF"):
                xpos 0
                ypos 0
                xsize 7
                ysize 229

            text "☀":
                xpos 42
                ypos 12
                xsize 145
                text_align 0.5
                font "DejaVuSans.ttf"
                size 150
                color "#3CDFFF"
                outlines [(3, "#3CDFFF40", 0, 0)]

            vbox:
                xpos 235
                ypos 7
                spacing 10

                text "LOCAL WEATHER // [period]":
                    font gui.interface_text_font2
                    size 25
                    color "#7F929B"
                    kerning 4

                text weather:
                    font gui.interface_text_font
                    size 58
                    color "#FFFFFF"

                text "[temperature]  //  LOW WIND  //  NO RAIN":
                    font gui.interface_text_font2
                    size 29
                    color "#3CDFFF"
                    kerning 2



        fixed:
            xpos 390
            ypos 1690
            xsize 1770
            ysize 225
            at godson_calendar_timeline

            text "CALENDAR STATUS":
                xpos 0
                ypos 0
                font gui.interface_text_font2
                size 24
                color "#7D8E96"
                kerning 5

            add Solid("#2B3B43"):
                xpos 0
                ypos 104
                xsize 1660
                ysize 4

            add Solid("#596970"):
                xpos 2
                ypos 87
                xsize 38
                ysize 38

            add Solid("#3CDFFF"):
                xpos 1622
                ypos 81
                xsize 50
                ysize 50
                at godson_calendar_signal

            text "[from_day] [from_number]":
                xpos 0
                ypos 130
                font gui.interface_text_font2
                size 28
                color "#82929A"
                kerning 2

            text "[to_day] [to_number]":
                xalign 1.0
                ypos 130
                font gui.interface_text_font2
                size 28
                color "#3CDFFF"
                kerning 2

        text "THE STORY CONTINUES":
            xpos 3300
            ypos 1955
            xanchor 1.0
            font gui.interface_text_font2
            size 23
            color "#647780"
            kerning 5
            at godson_calendar_weather


label calendar:

    window hide
    scene black
    with Dissolve(0.35)

    call screen godson_day_transition(
        calendar_from_day,
        calendar_from_date,
        calendar_to_day,
        calendar_to_date,
        calendar_month_name,
        calendar_year,
        calendar_weather,
        calendar_temperature,
        calendar_period
    )

    scene black
    with Dissolve(0.45)
    return
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
