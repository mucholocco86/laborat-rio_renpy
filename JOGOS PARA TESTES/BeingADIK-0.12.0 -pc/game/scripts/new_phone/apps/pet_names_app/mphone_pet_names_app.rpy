screen mphone_pet_names_app_screen:
    tag mphone_pet_names_app_screen
    modal True
    fixed:
        at mphone_app_transform
        add "mphone_pet_names_bg"
        add AlphaBlend("mphone_screen_alpha", Frame(Null(), 10 * persistent.scale_factor, 10 * persistent.scale_factor), "mphone_silver_spr_big", alpha=True)
        add AlphaBlend("mphone_screen_alpha", Frame(Null(), 10 * persistent.scale_factor, 10 * persistent.scale_factor), "mphone_silver_spr_medium", alpha=True)
        add AlphaBlend("mphone_screen_alpha", Frame(Null(), 10 * persistent.scale_factor, 10 * persistent.scale_factor), "mphone_silver_spr_small", alpha=True)

    if persistent.golden_phone and persistent.golden_phone_skin_enabled:
        add "mphone_shell_gold"
    else:
        add "mphone_shell"
    key "mousedown_4" action NullAction()
    key "mousedown_5" action NullAction()
    key "mouseup_2" action (SetVariable("mphone_current_pet_name",""),SetVariable("pet_reset",""),Function(mphone_pet_name_set_func),Hide("mphone_pet_names_app_screen"))
    fixed:
        at mphone_app_transform

        imagebutton at mphone_off_transform:
            idle "mphone_off_circle_idle"
            hover "mphone_off_circle_hover"
            action (SetVariable("mphone_current_pet_name",""),SetVariable("pet_reset",""),Function(mphone_pet_name_set_func),Hide("mphone_pet_names_app_screen"))
            xalign 0.5
            yalign mphone_off_yalign

        text "{size=+%d}Pet names{/size}" % (20 * persistent.scale_factor) style "mphone_pet_name_text_style" xalign 0.5 yalign 0.2
        vpgrid:
            xoffset -20 * persistent.scale_factor
            xalign 0.5
            yalign 0.45
            spacing -5 * persistent.scale_factor
            mousewheel False
            draggable False
            cols 3
            text "                              " style "mphone_pet_name_text_style"
            text "You call her" style "mphone_pet_name_text_style2"
            text "She calls you" style "mphone_pet_name_text_style2"
            text "Camila" style "mphone_pet_name_text_style2" xoffset 50 * persistent.scale_factor
            if mphone_current_pet_name == "camila":
                input:
                    style "mphone_pet_name_text_style" default "[camila]" value VariableInputValue('camila') length 12
            else:
                textbutton "[camila]" text_style "mphone_pet_name_text_button_style" action SetVariable("mphone_current_pet_name","camila") xoffset -6 * persistent.scale_factor yoffset -6 * persistent.scale_factor

            if mphone_current_pet_name == "mc_camila":
                input:
                    style "mphone_pet_name_text_style" default "[mc_camila]" value VariableInputValue('mc_camila') length 12
            else:
                textbutton "[mc_camila]" text_style "mphone_pet_name_text_button_style" action SetVariable("mphone_current_pet_name","mc_camila") xoffset -6 * persistent.scale_factor yoffset -6 * persistent.scale_factor

            text "Cathy" style "mphone_pet_name_text_style2" xoffset 50 * persistent.scale_factor
            if mphone_current_pet_name == "cathy":
                input:
                    style "mphone_pet_name_text_style" default "[cathy]" value VariableInputValue('cathy') length 12
            else:
                textbutton "[cathy]" text_style "mphone_pet_name_text_button_style" action SetVariable("mphone_current_pet_name","cathy") xoffset -6 * persistent.scale_factor yoffset -6 * persistent.scale_factor
            if mphone_current_pet_name == "mc_cathy":
                input:
                    style "mphone_pet_name_text_style" default "[mc_cathy]" value VariableInputValue('mc_cathy') length 12
            else:
                textbutton "[mc_cathy]" text_style "mphone_pet_name_text_button_style" action SetVariable("mphone_current_pet_name","mc_cathy") xoffset -6 * persistent.scale_factor yoffset -6 * persistent.scale_factor

            text "Isabella" style "mphone_pet_name_text_style2" xoffset 50 * persistent.scale_factor
            if mphone_current_pet_name == "isabella":
                input:
                    style "mphone_pet_name_text_style" default "[isabella]" value VariableInputValue('isabella') length 12
            else:
                textbutton "[isabella]" text_style "mphone_pet_name_text_button_style" action SetVariable("mphone_current_pet_name","isabella") xoffset -6 * persistent.scale_factor yoffset -6 * persistent.scale_factor
            if mphone_current_pet_name == "mc_isabella":
                input:
                    style "mphone_pet_name_text_style" default "[mc_isabella]" value VariableInputValue('mc_isabella') length 12
            else:
                textbutton "[mc_isabella]" text_style "mphone_pet_name_text_button_style" action SetVariable("mphone_current_pet_name","mc_isabella") xoffset -6 * persistent.scale_factor yoffset -6 * persistent.scale_factor

            text "Jade" style "mphone_pet_name_text_style2" xoffset 50 * persistent.scale_factor
            if mphone_current_pet_name == "jade":
                input:
                    style "mphone_pet_name_text_style" default "[jade]" value VariableInputValue('jade') length 12
            else:
                textbutton "[jade]" text_style "mphone_pet_name_text_button_style" action SetVariable("mphone_current_pet_name","jade") xoffset -6 * persistent.scale_factor yoffset -6 * persistent.scale_factor
            if mphone_current_pet_name == "mc_jade":
                input:
                    style "mphone_pet_name_text_style" default "[mc_jade]" value VariableInputValue('mc_jade') length 12
            else:
                textbutton "[mc_jade]" text_style "mphone_pet_name_text_button_style" action SetVariable("mphone_current_pet_name","mc_jade") xoffset -6 * persistent.scale_factor yoffset -6 * persistent.scale_factor

            text "Jill" style "mphone_pet_name_text_style2" xoffset 50 * persistent.scale_factor
            if mphone_current_pet_name == "jill":
                input:
                    style "mphone_pet_name_text_style" default "[jill]" value VariableInputValue('jill') length 12
            else:
                textbutton "[jill]" text_style "mphone_pet_name_text_button_style" action SetVariable("mphone_current_pet_name","jill") xoffset -6 * persistent.scale_factor yoffset -6 * persistent.scale_factor
            if mphone_current_pet_name == "mc_jill":
                input:
                    style "mphone_pet_name_text_style" default "[mc_jill]" value VariableInputValue('mc_jill') length 12
            else:
                textbutton "[mc_jill]" text_style "mphone_pet_name_text_button_style" action SetVariable("mphone_current_pet_name","mc_jill") xoffset -6 * persistent.scale_factor yoffset -6 * persistent.scale_factor

            text "Josy" style "mphone_pet_name_text_style2" xoffset 50 * persistent.scale_factor
            if mphone_current_pet_name == "josy":
                input:
                    style "mphone_pet_name_text_style" default "[josy]" value VariableInputValue('josy') length 12
            else:
                textbutton "[josy]" text_style "mphone_pet_name_text_button_style" action SetVariable("mphone_current_pet_name","josy") xoffset -6 * persistent.scale_factor yoffset -6 * persistent.scale_factor
            if mphone_current_pet_name == "mc_josy":
                input:
                    style "mphone_pet_name_text_style" default "[mc_josy]" value VariableInputValue('mc_josy') length 12
            else:
                textbutton "[mc_josy]" text_style "mphone_pet_name_text_button_style" action SetVariable("mphone_current_pet_name","mc_josy") xoffset -6 * persistent.scale_factor yoffset -6 * persistent.scale_factor

            text "Maya" style "mphone_pet_name_text_style2" xoffset 50 * persistent.scale_factor
            if mphone_current_pet_name == "maya":
                input:
                    style "mphone_pet_name_text_style" default "[maya]" value VariableInputValue('maya') length 12
            else:
                textbutton "[maya]" text_style "mphone_pet_name_text_button_style" action SetVariable("mphone_current_pet_name","maya") xoffset -6 * persistent.scale_factor yoffset -6 * persistent.scale_factor
            if mphone_current_pet_name == "mc_maya":
                input:
                    style "mphone_pet_name_text_style" default "[mc_maya]" value VariableInputValue('mc_maya') length 12
            else:
                textbutton "[mc_maya]" text_style "mphone_pet_name_text_button_style" action SetVariable("mphone_current_pet_name","mc_maya") xoffset -6 * persistent.scale_factor yoffset -6 * persistent.scale_factor

            text "Quinn" style "mphone_pet_name_text_style2" xoffset 50 * persistent.scale_factor
            if mphone_current_pet_name == "quinn":
                input:
                    style "mphone_pet_name_text_style" default "[quinn]" value VariableInputValue('quinn') length 12
            else:
                textbutton "[quinn]" text_style "mphone_pet_name_text_button_style" action SetVariable("mphone_current_pet_name","quinn") xoffset -6 * persistent.scale_factor yoffset -6 * persistent.scale_factor
            if mphone_current_pet_name == "mc_quinn":
                input:
                    style "mphone_pet_name_text_style" default "[mc_quinn]" value VariableInputValue('mc_quinn') length 12
            else:
                textbutton "[mc_quinn]" text_style "mphone_pet_name_text_button_style" action SetVariable("mphone_current_pet_name","mc_quinn") xoffset -6 * persistent.scale_factor yoffset -6 * persistent.scale_factor

            text "Riona" style "mphone_pet_name_text_style2" xoffset 50 * persistent.scale_factor
            if mphone_current_pet_name == "riona":
                input:
                    style "mphone_pet_name_text_style" default "[riona]" value VariableInputValue('riona') length 12
            else:
                textbutton "[riona]" text_style "mphone_pet_name_text_button_style" action SetVariable("mphone_current_pet_name","riona") xoffset -6 * persistent.scale_factor yoffset -6 * persistent.scale_factor
            if mphone_current_pet_name == "mc_riona":
                input:
                    style "mphone_pet_name_text_style" default "[mc_riona]" value VariableInputValue('mc_riona') length 12
            else:
                textbutton "[mc_riona]" text_style "mphone_pet_name_text_button_style" action SetVariable("mphone_current_pet_name","mc_riona") xoffset -6 * persistent.scale_factor yoffset -6 * persistent.scale_factor

            text "Sage" style "mphone_pet_name_text_style2" xoffset 50 * persistent.scale_factor
            if mphone_current_pet_name == "sage":
                input:
                    style "mphone_pet_name_text_style" default "[sage]" value VariableInputValue('sage') length 12
            else:
                textbutton "[sage]" text_style "mphone_pet_name_text_button_style" action SetVariable("mphone_current_pet_name","sage") xoffset -6 * persistent.scale_factor yoffset -6 * persistent.scale_factor
            if mphone_current_pet_name == "mc_sage":
                input:
                    style "mphone_pet_name_text_style" default "[mc_sage]" value VariableInputValue('mc_sage') length 12
            else:
                textbutton "[mc_sage]" text_style "mphone_pet_name_text_button_style" action SetVariable("mphone_current_pet_name","mc_sage") xoffset -6 * persistent.scale_factor yoffset -6 * persistent.scale_factor


        if pet_reset == "resets" and mphone_current_pet_name == "":
            textbutton "Click again to reset pet names" text_style "mphone_pet_name_text_button_style" action Function(mphone_pet_name_reset_func) xalign 0.5 yalign 0.8
        else:
            textbutton "Reset pet names" text_style "mphone_pet_name_text_button_style" action (SetVariable("mphone_current_pet_name",""),SetVariable("pet_reset", "resets")) xalign 0.5 yalign 0.8

        add "mphone_fg"
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
