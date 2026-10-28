screen QuickMenuKeyBinds ():
# Keybinds: lower and upper case for CAPSLOCK
    python:
        keysByLetter = {
            "b" : [ Rollback () ],
            "j" : [ ShowMenu ("History") ],
            "l" : [ ShowMenu ("Load") ],
            "n" : [ RollForward () ],
            "q" : [ Quit (confirm = True) ]
        }
        if not qm_profiles_disabled:
            keysByLetter.update ({ "p" : [ ShowMenu ("Profiles") ] })
        
    key "K_ESCAPE" action ShowMenu (myDormMenu.getCurrentTab ("Settings"))
    key "mouseup_3" action ShowMenu ("GameSave")
    for keyToPress, keyAction in keysByLetter.items ():
        key keyToPress.lower () action keyAction
        key keyToPress.upper () action keyAction