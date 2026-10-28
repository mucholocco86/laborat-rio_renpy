init python:
    def mphone_count_notifications():
        global mphone_contact_list
        global mphone_notification_count
        global mphone_new_contact_event
        global mphone_shop_active
        mphone_shop_active = False
        mphone_notification_count = 0
        for x in mphone_contact_list:
            if x[1].find("_shop") == -1:
                if x[1] != "NONE":
                    mphone_notification_count += 1
                if x[2]:
                    mphone_notification_count += 1
            else:
                mphone_shop_active = True
        if mphone_notification_count > 0:
            mphone_new_contact_event = True
        else:
            mphone_new_contact_event = False
        return

    def mphone_contacts_clear():
        global mphone_chat_history_list
        global mphone_contact_list
        for x in mphone_chat_history_list:
            x[1] = 0
            x[4] = " "
        for x in mphone_contact_list:
            x[1] = "NONE"
            x[2] = False
        return

    def new_phone_call(who,jumplabel):
        global mphone_contact_list
        
        for x in range(0,len(mphone_contact_list)):
            if mphone_contact_list[x][0] == who:
                mphone_contact_list[x][1] = jumplabel
        return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
