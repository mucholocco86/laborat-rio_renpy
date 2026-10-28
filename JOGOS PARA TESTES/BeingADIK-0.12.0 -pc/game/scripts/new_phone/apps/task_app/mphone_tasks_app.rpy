screen mphone_tasks_app_screen:
    tag mphone_tasks_app_screen
    modal True
    key "mousedown_4" action NullAction()
    key "mousedown_5" action NullAction()
    fixed:
        at mphone_app_transform
        add "mphone_tasks_app_bg"

    if persistent.golden_phone and persistent.golden_phone_skin_enabled:
        add "mphone_shell_gold"
    else:
        add "mphone_shell"

    fixed:
        at mphone_app_transform

        imagebutton at mphone_off_transform:
            idle "mphone_off_circle_idle"
            hover "mphone_off_circle_hover"
            action Hide("mphone_tasks_app_screen")
            xalign 0.5
            yalign mphone_off_yalign
        key "mouseup_2" action Hide("mphone_tasks_app_screen")
        vbox:
            xalign 0.5
            yalign 0.5
            if len(task_list) > 0:
                text "Tasks" style "mphone_task_text_big_style" xalign 0.5
                $ tmpBool = False
                for x in task_list:
                    if x != "":
                        text "%s" % x style "mphone_task_text_style" xalign 0.5
                        $ tmpBool = True
                if not tmpBool:
                    if "\n" in current_task:
                        text "%s" % current_task style "mphone_task_text_style" xalign 0.5 text_align 0.5
                    else:
                        text "%s" % current_task style "mphone_task_text_style" xalign 0.5
            else:
                text "Tasks" style "mphone_task_text_big_style" xalign 0.5
                text "No tasks available" style "mphone_task_text_style" xalign 0.5

            if len(optional_task_list) > 0:
                text "Optional Tasks" style "mphone_task_text_big_style" xalign 0.5
                $ tmpBool = False
                for x in optional_task_list:
                    if x != "":
                        text "%s" % x style "mphone_task_text_style" xalign 0.5
                        $ tmpBool = True
                if not tmpBool:
                    text "No optional tasks available" style "mphone_task_text_style" xalign 0.5

        add "mphone_fg"
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
