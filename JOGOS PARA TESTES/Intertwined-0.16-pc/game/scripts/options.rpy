## Basics ######################################################################

define config.name = "Intertwined" # The name of the game.
define config.version = "0.16" # The version of the game.
define config.save_directory = "Intertwined_NyxVN" # save directory

## Console and developer mode ###################################################
define config.console = False
define config.developer = False

## Steam ########################################################################

define config.rollback_length = 48

## Sounds and music ############################################################

define config.has_sound = True
define config.has_music = True
define config.has_voice = False

define config.main_menu_music = "Music/Alessio Acierno - Intertwined.mp3"

## Transitions #################################################################

define config.enter_transition = Dissolve(.15)
define config.exit_transition = Dissolve(.15)
define config.intra_transition = Dissolve(.15)
define config.after_load_transition = None
define config.end_game_transition = None
define config.window_show_transition = Dissolve(.1)
define config.window_hide_transition = Dissolve(.1)

## Steam helpers ###############################################################

init python:

    def is_steam_build():
        # True when this process was launched through the Steam client.
        try:
            import os
            for var in (
                "SteamClientLaunch",
                "SteamGameId",
                "SteamOverlayGameId",
                "SteamAppId",
                "SteamEnv",
            ):
                if os.environ.get(var):
                    return True
        except Exception:
            pass
        try:
            return achievement.steam is not None
        except Exception:
            return False

    def is_steam_running():
        # True only when the Steamworks SDK initialized successfully at
        # startup.
        try:
            return achievement.steam is not None
        except Exception:
            return False

## Window management ###########################################################

define config.window = "auto"

define config.has_autosave = True
define config.autosave_slots = 24
define config.quicksave_slots = 8

## Icon ########################################################################

define config.window_icon = "gui/window_icon.png"

init python:
    persistent.alt_menu_bg = True