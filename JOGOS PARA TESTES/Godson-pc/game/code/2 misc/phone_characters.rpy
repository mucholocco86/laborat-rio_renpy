define nvl_mode = "phone"
define myles_nvl = Character("Myles", kind=nvl, callback=Phone_ReceiveSound)
define dev_nvl = Character("JAY", kind=nvl, callback=Phone_ReceiveSound)
define marnie_nvl = Character("Marnie", kind=nvl, callback=Phone_ReceiveSound)


define character_icons = {
    "Myles": "gui/myles_icon.png",
    "Marnie": "gui/landlord_icon.png",
    
}

define config.adv_nvl_transition = None
define config.nvl_adv_transition = None

init:
    default myles_message_shown = False
    default marnie_message_shown = False
    default dev_message_shown = False
    default open_text = ""
    default myles_history = []
    default marnie_history = []
    default other_character_history = []
    default dev_history = []

init python:
    global player_money
    player_money = 500

init -2 python:
    def pay_pizza():
        global player_money
        payment = 45
        steps = 45  
        num_steps = payment // steps  
        for _ in range(num_steps):
            player_money -= steps
        if player_money < 0:  
            player_money = 0




init python:

    def honee_message():
        if not honee_message_shown:
            renpy.call_in_new_context('honee_message_label')
            global honee_message_shown
            honee_message_shown = True
        else:
            renpy.call_in_new_context('honee_conversation')

    def marnie_message():
        if not landlord_message_shown:
            renpy.call_in_new_context('landlord_message_label')
            global landlord_message_shown
            landlord_message_shown = True
        else:
            renpy.call_in_new_context('landlord_conversation')

    def dev_message():
        if not dev_message_shown:
            renpy.call_in_new_context('dev_message_label')
            global dev_message_shown
            dev_message_shown = True
        else:
            renpy.call_in_new_context('dev_conversation')


label honee_conversation:
    $ nvl_list = myles_history
    $ open_text = "Myles"
    $ nvl_narrator = Character(None, kind=nvl)
    nvl_narrator ""
    $ nvl_list.pop()
    call history_save from _call_history_save_5
    return

label marnie_conversation:
    $ nvl_list = marnie_history
    $ open_text = "Marnie"
    $ nvl_narrator = Character(None, kind=nvl)
    nvl_narrator ""
    $ nvl_list.pop()
    call history_save from _call_history_save_6
    return

label dev_conversation:
    $ nvl_list = dev_history
    $ open_text = "JAY"
    $ nvl_narrator = Character(None, kind=nvl)
    nvl_narrator ""
    $ nvl_list.pop()
    call history_save from _call_history_save_10
    return


label history_save:
    if open_text == "Myles":
        $ myles_history = nvl_list
    elif open_text == "Marnie":
        $ marnie_history = nvl_list
    elif open_text == "CHEESECAKE":
        $ dev_history = nvl_list
    return
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
