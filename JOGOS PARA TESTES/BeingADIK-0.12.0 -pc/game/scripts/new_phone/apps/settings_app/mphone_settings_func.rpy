init python:

    def mphone_change_notification():
        global mphone_notifications
        global current_notification_sound
        
        if current_notification_sound + 1 < len(mphone_notifications):
            current_notification_sound += 1
        else:
            current_notification_sound = 0
        renpy.play(mphone_notifications[current_notification_sound][1], "sfx1")
        return

    def mphone_settings_set_new_names():
        global name
        global roosterNickMCCustom
        global rooster_nick_list
        global settings_name
        global settings_rooster_nickname
        
        if len(settings_name.replace(" ","")) > 0:
            name = settings_name
            persistent.name = name
        if len(settings_rooster_nickname.replace(" ","")) > 0:
            roosterNickMCCustom = settings_rooster_nickname
        rooster_nick_list[0][1] = "[name]@[roosterNickMCCustom]"
        
        return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
