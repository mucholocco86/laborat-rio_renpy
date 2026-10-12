
style text_current_tasks:
    color "#ca688d"
    outlines [(2, "#642f43", 1, 1)]

style text_current_tasks:
    color "#ca688d"
    outlines [(2, "#642f43", 1, 1)]

style text_people_of_interest:
    color "#cd8ceb"
    outlines [(2, "#48426b", 1, 1)]

style text_future_tasks:
    color "#f09c52"
    outlines [(2, "#7d5949", 1, 1)]

style text_current_tasks_task:
    color "#393939"


style text_current_tasks_task:
    variant "small"
    color "#393939"
    size 30





init:

    $ v_stats_task_1 = ""
    $ v_stats_task_2 = ""
    $ v_stats_task_3 = ""
    $ v_stats_task_4 = ""
    $ v_stats_task_5 = ""
    $ v_stats_task_6 = ""
    $ v_stats_task_7 = ""
    $ v_stats_task_8 = ""
    $ v_stats_task_9 = ""
    $ v_stats_task_10 = ""
    $ v_stats_task_11 = ""
    $ v_stats_task_12 = ""
    $ v_stats_task_13 = ""


    $ v_stats_task_14 = ""
    $ v_stats_task_15 = ""
    $ v_stats_task_16 = ""
    $ v_stats_task_17 = ""
    $ v_stats_task_18 = ""
    $ v_stats_task_19 = ""
    $ v_stats_task_20 = ""
    $ v_stats_task_21 = ""
    $ v_stats_task_22 = ""
    $ v_stats_task_23 = ""
    $ v_stats_task_24 = ""
    $ v_stats_task_25 = ""
    $ v_stats_task_26 = ""




    $ v_stats_task_1_completed = False
    $ v_stats_task_2_completed = False
    $ v_stats_task_3_completed = False
    $ v_stats_task_4_completed = False
    $ v_stats_task_5_completed = False
    $ v_stats_task_6_completed = False
    $ v_stats_task_7_completed = False
    $ v_stats_task_8_completed = False
    $ v_stats_task_9_completed = False
    $ v_stats_task_10_completed = False
    $ v_stats_task_11_completed = False
    $ v_stats_task_12_completed = False
    $ v_stats_task_13_completed = False


    $ v_stats_task_14_completed = False
    $ v_stats_task_15_completed = False
    $ v_stats_task_16_completed = False
    $ v_stats_task_17_completed = False
    $ v_stats_task_18_completed = False
    $ v_stats_task_19_completed = False
    $ v_stats_task_20_completed = False
    $ v_stats_task_21_completed = False
    $ v_stats_task_22_completed = False
    $ v_stats_task_23_completed = False
    $ v_stats_task_24_completed = False
    $ v_stats_task_25_completed = False
    $ v_stats_task_26_completed = False



    $ v_stats_poi_1 = ""
    $ v_stats_poi_2 = ""
    $ v_stats_poi_3 = ""
    $ v_stats_poi_4 = ""
    $ v_stats_poi_5 = ""
    $ v_stats_poi_6 = ""
    $ v_stats_poi_7 = ""
    $ v_stats_poi_8 = ""

    $ v_stats_future_tasks_1 = ""
    $ v_stats_future_tasks_2 = ""
    $ v_stats_future_tasks_3 = ""
    $ v_stats_future_tasks_4 = ""
    $ v_stats_future_tasks_5 = ""
    $ v_stats_future_tasks_6 = ""
    $ v_stats_future_tasks_7 = ""
    $ v_stats_future_tasks_8 = ""



default v_stats_task_1_rating = "empty"
default v_stats_task_2_rating = "empty"
default v_stats_task_3_rating = "empty"
default v_stats_task_4_rating = "empty"
default v_stats_task_5_rating = "empty"
default v_stats_task_6_rating = "empty"
default v_stats_task_7_rating = "empty"
default v_stats_task_8_rating = "empty"
default v_stats_task_9_rating = "empty"
default v_stats_task_10_rating = "empty"
default v_stats_task_11_rating = "empty"
default v_stats_task_12_rating = "empty"
default v_stats_task_13_rating = "empty"


default v_stats_task_14_rating = "empty"
default v_stats_task_15_rating = "empty"
default v_stats_task_16_rating = "empty"
default v_stats_task_17_rating = "empty"
default v_stats_task_18_rating = "empty"
default v_stats_task_19_rating = "empty"
default v_stats_task_20_rating = "empty"
default v_stats_task_21_rating = "empty"
default v_stats_task_22_rating = "empty"
default v_stats_task_23_rating = "empty"
default v_stats_task_24_rating = "empty"
default v_stats_task_25_rating = "empty"
default v_stats_task_26_rating = "empty"





default v_tasks_notification_popup = True

init python:

    def task_addnew(task_name,number,**kwargs):
        var_name = "v_stats_task_"+str(number)
        var_notify = kwargs.get ("notify")
        if not kwargs or var_notify:
            renpy.notify("Task added: "+task_name)
        setattr(store, var_name, task_name)


    def task_completed(number,rating,**kwargs):
        var_name = "v_stats_task_"+str(number)
        task_name = getattr(store,var_name)
        task_completed = var_name+"_completed"
        task_rating = "v_stats_task_"+str(number)+"_rating"
        if not kwargs or var_notify:
            renpy.notify("Task completed: "+task_name)
        setattr(store, task_completed, True)
        setattr(store, task_rating,rating)



    def task_addpoi(poi_name,number,**kwargs):
        var_name = "v_stats_poi_"+str(number)
        if not kwargs or var_notify:
            renpy.notify("People of Interest added: "+poi_name)
        setattr(store, var_name, poi_name)

    def task_addfuturetask(task_name,number,**kwargs):
        var_name = "v_stats_future_tasks_"+str(number)
        var_notify = kwargs.get ("notify")
        if not kwargs or var_notify:
            renpy.notify("Future Task added: "+task_name)
        setattr(store, var_name, task_name)


init:
    $ v_stats_tasks_tab = 0

screen scr_mm_tasks_menu:
    key "game_menu" action [Hide("scr_mm_tasks_menu",dissolve),renpy.restart_interaction, SetVariable('quick_menu', False)]

    imagebutton idle "bg_stats_screen" action NullAction()

    add "black" alpha 0.7

    add "bg_tasks_layout"

    text _("{size=40}Current Tasks{/size}") xalign 0.22 yalign 0.01 style "text_current_tasks"

    text _("{size=40}People of Interest{/size}") xalign 0.81 yalign 0.01 style "text_people_of_interest"

    text _("{size=40}Future Tasks{/size}") xalign 0.79 yalign 0.51 style "text_future_tasks"

    if v_stats_tasks_tab == 0:
        imagebutton auto "tasks_arrow_right_%s" action SetVariable("v_stats_tasks_tab",1) xalign 0.4 yalign 0.98
    if v_stats_tasks_tab == 1:
        imagebutton auto "tasks_arrow_left_%s" action SetVariable("v_stats_tasks_tab",0) xalign 0.3 yalign 0.98




    vbox:
        xpos 80
        ypos 100

        if v_stats_tasks_tab == 0:
            hbox:
                if v_stats_task_1_completed:
                    text "{s}[v_stats_task_1]{/s}" style "text_current_tasks_task"
                else:
                    text "[v_stats_task_1]" style "text_current_tasks_task"
                if not v_stats_task_1 == "":
                    imagebutton:
                        idle "bg_tasks_check_" + v_stats_task_1_rating ypos -10 xpos 10

            hbox:
                if v_stats_task_2_completed:
                    text "{s}[v_stats_task_2]{/s}" style "text_current_tasks_task"
                else:
                    text "[v_stats_task_2]" style "text_current_tasks_task"

                if not v_stats_task_2 == "":
                    imagebutton:
                        idle "bg_tasks_check_" + v_stats_task_2_rating ypos -10 xpos 10
            hbox:
                if v_stats_task_3_completed:
                    text "{s}[v_stats_task_3]{/s}" style "text_current_tasks_task"
                else:
                    text "[v_stats_task_3]" style "text_current_tasks_task"

                if not v_stats_task_3 == "":
                    imagebutton:
                        idle "bg_tasks_check_" + v_stats_task_3_rating ypos -10 xpos 10
            hbox:
                if v_stats_task_4_completed:
                    text "{s}[v_stats_task_4]{/s}" style "text_current_tasks_task"
                else:
                    text "[v_stats_task_4]" style "text_current_tasks_task"

                if not v_stats_task_4 == "":
                    imagebutton:
                        idle "bg_tasks_check_" + v_stats_task_4_rating ypos -10 xpos 10
            hbox:
                if v_stats_task_5_completed:
                    text "{s}[v_stats_task_5]{/s}" style "text_current_tasks_task"
                else:
                    text "[v_stats_task_5]" style "text_current_tasks_task"

                if not v_stats_task_5 == "":
                    imagebutton:
                        idle "bg_tasks_check_" + v_stats_task_5_rating ypos -10 xpos 10
            hbox:
                if v_stats_task_6_completed:
                    text "{s}[v_stats_task_6]{/s}" style "text_current_tasks_task"
                else:
                    text "[v_stats_task_6]" style "text_current_tasks_task"

                if not v_stats_task_6 == "":
                    imagebutton:
                        idle "bg_tasks_check_" + v_stats_task_6_rating ypos -10 xpos 10
            hbox:
                if v_stats_task_7_completed:
                    text "{s}[v_stats_task_7]{/s}" style "text_current_tasks_task"
                else:
                    text "[v_stats_task_7]" style "text_current_tasks_task"

                if not v_stats_task_7 == "":
                    imagebutton:
                        idle "bg_tasks_check_" + v_stats_task_7_rating ypos -10 xpos 10
            hbox:
                if v_stats_task_8_completed:
                    text "{s}[v_stats_task_8]{/s}" style "text_current_tasks_task"
                else:
                    text "[v_stats_task_8]" style "text_current_tasks_task"

                if not v_stats_task_8 == "":
                    imagebutton:
                        idle "bg_tasks_check_" + v_stats_task_8_rating ypos -10 xpos 10
            hbox:
                if v_stats_task_9_completed:
                    text "{s}[v_stats_task_9]{/s}" style "text_current_tasks_task"
                else:
                    text "[v_stats_task_9]" style "text_current_tasks_task"

                if not v_stats_task_9 == "":
                    imagebutton:
                        idle "bg_tasks_check_" + v_stats_task_9_rating ypos -10 xpos 10
            hbox:
                if v_stats_task_10_completed:
                    text "{s}[v_stats_task_10]{/s}" style "text_current_tasks_task"
                else:
                    text "[v_stats_task_10]" style "text_current_tasks_task"

                if not v_stats_task_10 == "":
                    imagebutton:
                        idle "bg_tasks_check_" + v_stats_task_10_rating ypos -10 xpos 10
            hbox:
                if v_stats_task_11_completed:
                    text "{s}[v_stats_task_11]{/s}" style "text_current_tasks_task"
                else:
                    text "[v_stats_task_11]" style "text_current_tasks_task"

                if not v_stats_task_11 == "":
                    imagebutton:
                        idle "bg_tasks_check_" + v_stats_task_11_rating ypos -10 xpos 10

            hbox:
                if v_stats_task_12_completed:
                    text "{s}[v_stats_task_12]{/s}" style "text_current_tasks_task"
                else:
                    text "[v_stats_task_12]" style "text_current_tasks_task"

                if not v_stats_task_12 == "":
                    imagebutton:
                        idle "bg_tasks_check_" + v_stats_task_12_rating ypos -10 xpos 10
            hbox:
                if v_stats_task_13_completed:
                    text "{s}[v_stats_task_13]{/s}" style "text_current_tasks_task"
                else:
                    text "[v_stats_task_13]" style "text_current_tasks_task"

                if not v_stats_task_13 == "":
                    imagebutton:
                        idle "bg_tasks_check_" + v_stats_task_13_rating ypos -10 xpos 10


        if v_stats_tasks_tab == 1:
            hbox:
                if v_stats_task_14_completed:
                    text "{s}[v_stats_task_14]{/s}" style "text_current_tasks_task"
                else:
                    text "[v_stats_task_14]" style "text_current_tasks_task"
                if not v_stats_task_14 == "":
                    imagebutton:
                        idle "bg_tasks_check_" + v_stats_task_14_rating ypos -10 xpos 10

            hbox:
                if v_stats_task_15_completed:
                    text "{s}[v_stats_task_15]{/s}" style "text_current_tasks_task"
                else:
                    text "[v_stats_task_15]" style "text_current_tasks_task"
                if not v_stats_task_15 == "":
                    imagebutton:
                        idle "bg_tasks_check_" + v_stats_task_15_rating ypos -10 xpos 10

            hbox:
                if v_stats_task_16_completed:
                    text "{s}[v_stats_task_16]{/s}" style "text_current_tasks_task"
                else:
                    text "[v_stats_task_16]" style "text_current_tasks_task"
                if not v_stats_task_16 == "":
                    imagebutton:
                        idle "bg_tasks_check_" + v_stats_task_16_rating ypos -10 xpos 10

            hbox:
                if v_stats_task_17_completed:
                    text "{s}[v_stats_task_17]{/s}" style "text_current_tasks_task"
                else:
                    text "[v_stats_task_17]" style "text_current_tasks_task"
                if not v_stats_task_17 == "":
                    imagebutton:
                        idle "bg_tasks_check_" + v_stats_task_17_rating ypos -10 xpos 10

            hbox:
                if v_stats_task_18_completed:
                    text "{s}[v_stats_task_18]{/s}" style "text_current_tasks_task"
                else:
                    text "[v_stats_task_18]" style "text_current_tasks_task"
                if not v_stats_task_18 == "":
                    imagebutton:
                        idle "bg_tasks_check_" + v_stats_task_18_rating ypos -10 xpos 10

            hbox:
                if v_stats_task_19_completed:
                    text "{s}[v_stats_task_19]{/s}" style "text_current_tasks_task"
                else:
                    text "[v_stats_task_19]" style "text_current_tasks_task"
                if not v_stats_task_19 == "":
                    imagebutton:
                        idle "bg_tasks_check_" + v_stats_task_19_rating ypos -10 xpos 10

            hbox:
                if v_stats_task_20_completed:
                    text "{s}[v_stats_task_20]{/s}" style "text_current_tasks_task"
                else:
                    text "[v_stats_task_20]" style "text_current_tasks_task"
                if not v_stats_task_20 == "":
                    imagebutton:
                        idle "bg_tasks_check_" + v_stats_task_20_rating ypos -10 xpos 10

            hbox:
                if v_stats_task_21_completed:
                    text "{s}[v_stats_task_21]{/s}" style "text_current_tasks_task"
                else:
                    text "[v_stats_task_21]" style "text_current_tasks_task"
                if not v_stats_task_21 == "":
                    imagebutton:
                        idle "bg_tasks_check_" + v_stats_task_21_rating ypos -10 xpos 10

            hbox:
                if v_stats_task_22_completed:
                    text "{s}[v_stats_task_22]{/s}" style "text_current_tasks_task"
                else:
                    text "[v_stats_task_22]" style "text_current_tasks_task"
                if not v_stats_task_22 == "":
                    imagebutton:
                        idle "bg_tasks_check_" + v_stats_task_22_rating ypos -10 xpos 10

            hbox:
                if v_stats_task_23_completed:
                    text "{s}[v_stats_task_23]{/s}" style "text_current_tasks_task"
                else:
                    text "[v_stats_task_23]" style "text_current_tasks_task"
                if not v_stats_task_23 == "":
                    imagebutton:
                        idle "bg_tasks_check_" + v_stats_task_23_rating ypos -10 xpos 10


            hbox:
                if v_stats_task_24_completed:
                    text "{s}[v_stats_task_24]{/s}" style "text_current_tasks_task"
                else:
                    text "[v_stats_task_24]" style "text_current_tasks_task"
                if not v_stats_task_24 == "":
                    imagebutton:
                        idle "bg_tasks_check_" + v_stats_task_24_rating ypos -10 xpos 10

            hbox:
                if v_stats_task_25_completed:
                    text "{s}[v_stats_task_25]{/s}" style "text_current_tasks_task"
                else:
                    text "[v_stats_task_25]" style "text_current_tasks_task"
                if not v_stats_task_25 == "":
                    imagebutton:
                        idle "bg_tasks_check_" + v_stats_task_25_rating ypos -10 xpos 10

            hbox:
                if v_stats_task_26_completed:
                    text "{s}[v_stats_task_26]{/s}" style "text_current_tasks_task"
                else:
                    text "[v_stats_task_26]" style "text_current_tasks_task"
                if not v_stats_task_26 == "":
                    imagebutton:
                        idle "bg_tasks_check_" + v_stats_task_26_rating ypos -10 xpos 10


    vbox:
        xpos 1060
        ypos 100
        hbox:
            text "[v_stats_poi_1]" style "text_current_tasks_task"

        hbox:
            text "[v_stats_poi_2]" style "text_current_tasks_task"

        hbox:
            text "[v_stats_poi_3]" style "text_current_tasks_task"

        hbox:
            text "[v_stats_poi_4]" style "text_current_tasks_task"

        hbox:
            text "[v_stats_poi_5]" style "text_current_tasks_task"

        hbox:
            text "[v_stats_poi_6]" style "text_current_tasks_task"

        hbox:
            text "[v_stats_poi_7]" style "text_current_tasks_task"

        hbox:
            text "[v_stats_poi_8]" style "text_current_tasks_task"




    vbox:
        xpos 1060
        ypos 600
        hbox:
            text "[v_stats_future_tasks_1]" style "text_current_tasks_task"

        hbox:
            text "[v_stats_future_tasks_2]" style "text_current_tasks_task"

        hbox:
            text "[v_stats_future_tasks_3]" style "text_current_tasks_task"

        hbox:
            text "[v_stats_future_tasks_4]" style "text_current_tasks_task"

        hbox:
            text "[v_stats_future_tasks_5]" style "text_current_tasks_task"

        hbox:
            text "[v_stats_future_tasks_6]" style "text_current_tasks_task"

        hbox:
            text "[v_stats_future_tasks_7]" style "text_current_tasks_task"

    imagebutton:
        xalign 0.01
        yalign 0.98
        auto "btn_mm_back_%s" action [Hide("scr_mm_tasks_menu",dissolve),renpy.restart_interaction, SetVariable('quick_menu', False)]

    imagebutton:
        xalign 0.98
        yalign 0.98
        auto "btn_mm_exit_%s" action [Hide("scr_mm_tasks_menu",dissolve),Hide("scr_mm_main",dissolve),renpy.restart_interaction, SetVariable('quick_menu', True), SetVariable('v_mm_open', False)]
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
