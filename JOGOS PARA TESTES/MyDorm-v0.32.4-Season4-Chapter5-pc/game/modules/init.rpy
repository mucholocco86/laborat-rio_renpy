# defaultSettings from config.rpy
default persistent.family                       = False
default persistent.intro                        = True
default persistent.lang                         = defaultSettings ["lang"]
default persistent.lactation                    = defaultSettings ["lactation"]
default persistent.lesbian                      = defaultSettings ["lesbian"]
default persistent.pregnancy                    = defaultSettings ["pregnancy"]
default persistent.urination                    = defaultSettings ["urination"]
default persistent.walkthrough                  = defaultSettings ["walkthrough"]
default persistent.choicePosition               = defaultSettings ["choicePosition"]
#default persistent.dialogueBoxHeight            = 200
default persistent.dialogueBoxHeight            = defaultSettings ["dialogueBoxHeight"]
default persistent.dialogueBoxOpacity           = defaultSettings ["dialogueBoxOpacity"]
#if defaultSettings ["dialogueBoxWidth"] < 10:
#default persistent.dialogueBoxWidth         = 1920
#else:
default persistent.dialogueBoxWidth             = defaultSettings ["dialogueBoxWidth"]
default persistent.dialogueWhoOutlineColor      = defaultSettings ["dialogueWhoOutlineColor"]
default persistent.dialogueWhoOutlineOpacity    = defaultSettings ["dialogueWhoOutlineOpacity"]
default persistent.dialogueWhoOutlineThickness  = defaultSettings ["dialogueWhoOutlineThickness"]
default persistent.dialogueWhoSize              = defaultSettings ["dialogueWhoSize"]
default persistent.dialogueWhatColorNormal      = defaultSettings ["dialogueWhatColorNormal"]
default persistent.dialogueWhatColorThoughts    = defaultSettings ["dialogueWhatColorThoughts"]
default persistent.dialogueWhatOutlineColor     = defaultSettings ["dialogueWhatOutlineColor"]
default persistent.dialogueWhatOutlineOpacity   = defaultSettings ["dialogueWhatOutlineOpacity"]
default persistent.dialogueWhatOutlineThickness = defaultSettings ["dialogueWhatOutlineThickness"]
default persistent.dialogueWhatSize             = defaultSettings ["dialogueWhatSize"]
default persistent.menuButtonShowIcons          = defaultSettings ["menuButtonShowIcons"]
default persistent.menuButtonShowText           = defaultSettings ["menuButtonShowText"]
default persistent.menuButtonSize               = defaultSettings ["menuButtonSize"]
default persistent.quickmenuButtonsHistory      = defaultSettings ["quickmenuButtonsHistory"]
default persistent.quickmenuButtonsRollBackFwd  = defaultSettings ["quickmenuButtonsRollBackFwd"]
default persistent.quickmenuButtonsSkip         = defaultSettings ["quickmenuButtonsSkip"]
default persistent.quickmenuButtonQSaveQLoad    = defaultSettings ["quickmenuButtonsQSaveQLoad"]
default persistent.quickmenuButtonSaveLoad      = defaultSettings ["quickmenuButtonsSaveLoad"]
default persistent.quickmenuButtonQuit          = defaultSettings ["quickmenuButtonsQuit"]
default persistent.quickmenuHidden              = defaultSettings ["quickmenuHidden"]
default persistent.quickmenuOutlineColor        = defaultSettings ["quickmenuOutlineColor"]
default persistent.quickmenuOutlineOpacity      = defaultSettings ["quickmenuOutlineOpacity"]
default persistent.quickmenuOutlineThickness    = defaultSettings ["quickmenuOutlineThickness"]
default persistent.quickmenuPosition            = defaultSettings ["quickmenuPosition"]
default persistent.quickmenuShowIcons           = defaultSettings ["quickmenuShowIcons"]
default persistent.quickmenuShowText            = defaultSettings ["quickmenuShowText"]
default persistent.quickmenuSize                = defaultSettings ["quickmenuSize"]
define config.allow_underfull_grids            = True

init python:
    config.file_slotname_callback               = fileSlotIndexName
    config.autosave_prefix_callback             = autoSavePrefix
    config.save_json_callbacks.append (saveJSONcallback00)
    labelsSeen                                  = []

# Characters and profile data
init -100 python:
    characters = [ "Emma", "Martha" ]
    Profile_data = {}
    for character in characters:
        Profile_data.update ({ character : {} })

init 100 python:
    myDormMenu = MyDormMenu ()
    pages = [ "About", "Buttons", "Confirmations", "GameSaveLoad", "Help", "HelpMenu", "History", "MenuButtons", "Profiles", "QuickMenu", "Settings", "SettingsMenu" ]
    contentPages = [ "About", "HelpTabGamepad", "HelpTabKeyboard", "HelpTabMouse" ]
