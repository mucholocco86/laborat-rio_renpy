init python:

    def mphone_bios_change_sort_filter():
        global mphone_bios_sort_by
        global mphone_bios_sort_by_idx
        if mphone_bios_sort_by_idx + 1 < len(mphone_bios_sort_by):
            mphone_bios_sort_by_idx += 1
        else:
            mphone_bios_sort_by_idx = 0
        return

    def new_bio(who,what):
        global mphone_bios_chars_list
        global chat_new_bios
        if mphone_bios_chars_list == []:
            update_bios_list()
        for x in mphone_bios_chars_list:
            if x[0] == who:
                if any(what in s for s in x[3]):
                    return
                x[3].append(what)
                x[4] += 1
                chat_new_bios = True
                return
        return

    def check_if_new_bio():
        global mphone_bios_chars_list
        global chat_new_bios
        chat_new_bios = False
        for x in mphone_bios_chars_list:
            if x[4] > 0:
                chat_new_bios = True
                return
        return

    def update_bios_list():
        global mphone_bios_chars
        global mphone_bios_chars_list
        
        for x in range(0,len(mphone_bios_chars)):
            tmp_list = []
            for y in mphone_bios_chars[x][3]:
                tmp_list.append(y)
            mphone_bios_chars_list.append([mphone_bios_chars[x][0],mphone_bios_chars[x][1],mphone_bios_chars[x][2],tmp_list,0])
        mphone_bios_chars = []
        return


    def getBioText():
        global mphone_bios_chars_list
        global mphone_current_bios_char
        
        bio_text = ""
        for x in range(0,len(mphone_bios_chars_list[mphone_current_bios_char][3])):
            if x >= len(mphone_bios_chars_list[mphone_current_bios_char][3]) - mphone_bios_chars_list[mphone_current_bios_char][4]:
                bio_text += "{color=#ffed00}• %s{/color}\n\n" % mphone_bios_chars_list[mphone_current_bios_char][3][x]
            else:
                bio_text += "• %s\n\n" % mphone_bios_chars_list[mphone_current_bios_char][3][x]
        
        if len(mphone_bios_chars_list[mphone_current_bios_char][3]) < 11:
            for x in range(0,11-len(mphone_bios_chars_list[mphone_current_bios_char][3])):
                bio_text += "\n\n"
        return bio_text
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
