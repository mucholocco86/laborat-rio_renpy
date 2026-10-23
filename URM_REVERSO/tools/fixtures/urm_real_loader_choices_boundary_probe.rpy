# Full URM loader probe: original package copied unchanged into a disposable game.
# Ren'Py 7.4.11; tests whether the real URM Choices notification opens its screen
# while the game is in a real fixed rollback boundary.

default urm_real_loader_probe_route = None

label urm_real_loader_choices_boundary_start:
    $ urm_real_loader_probe_route = None
    $ x52URM.Settings.seenWelcome = 2
    $ x52URM.Settings.warningDisabled = True
    $ x52URM.Settings.autoUpdateCheck = False
    $ x52URM.Settings.lastLoadedFile = None
    $ x52URM.Settings.showChoicesNotification = True
    $ x52URM.Settings.showWatchPanel = False
    $ x52URM.States.updateNotificationShown = True
    $ renpy.config.fix_rollback_without_choice = False
    $ renpy.game.context().rollback = True
    $ renpy.store._rollback = True
    $ x52URM.afterLoad()
    $ print("REAL_URM_PROBE_READY", x52URM.Choices.isDisplayingChoice,
            renpy.in_fixed_rollback(), renpy.can_rollback())

    menu:
        "Native route A":
            $ urm_real_loader_probe_route = "A"

        "Native route B":
            $ urm_real_loader_probe_route = "B"

    $ renpy.fix_rollback()
    $ print("REAL_URM_AFTER_MENU", urm_real_loader_probe_route,
            renpy.in_fixed_rollback(), renpy.roll_forward_info(),
            x52URM.Choices.isDisplayingChoice,
            renpy.game.log.fixed_rollback_boundary)

    if urm_real_loader_probe_route == "A":
        "Fixed boundary probe route A."
    else:
        "Fixed boundary probe route B."

label urm_real_loader_choices_boundary_done:
    return


testcase urm_real_loader_choices_boundary_runtime:
    run Jump("urm_real_loader_choices_boundary_start")
    "Native route B"
    "Fixed boundary probe route B."
    type PAGEUP
    type PAGEUP
    "Choices detected"
    type alt_c
    "Choices"
    type alt_1
    type RETURN
    "Fixed boundary probe route A."
    label urm_real_loader_choices_boundary_done
    assert urm_real_loader_probe_route == "A"
    $ print("REAL_URM_CHOICES_RESULT", urm_real_loader_probe_route,
            renpy.in_fixed_rollback(), renpy.roll_forward_info(),
            renpy.can_rollback())
    $ renpy.quit()
