# Isolated runtime probe for the URM Choice action during fixed rollback.
# rollback_is_fixed is set directly to model the UI state; this fixture does
# not claim to exercise rollback across a real fix_rollback boundary.

default urm_fixed_probe_route = None
default urm_fixed_probe_block_all = False
default urm_fixed_probe_before = None
default urm_fixed_probe_native_a_sensitive = None
default urm_fixed_probe_native_b_sensitive = None
default urm_fixed_probe_after = None

init python:
    def urm_fixed_probe_select(label, index):
        renpy.game.log.rollback_is_fixed = False
        return renpy.ui.ChoiceReturn(label, index)()

screen urm_fixed_choice_overlay():
    modal True
    zorder 300

    frame:
        xalign 0.5
        yalign 0.5

        vbox:
            spacing 12
            text "Fixed rollback selection probe"
            textbutton "URM select route A":
                action [
                    Hide("urm_fixed_choice_overlay"),
                    Function(urm_fixed_probe_select, "Route A", 0, _update_screens=False),
                ]

label urm_fixed_choice_probe_start:
    $ urm_fixed_probe_route = None
    $ renpy.game.context().rollback = True
    $ renpy.store._rollback = True
    $ renpy.config.fix_rollback_without_choice = urm_fixed_probe_block_all
    $ renpy.game.log.rollback_is_fixed = True

    $ urm_fixed_probe_before = renpy.game.log.rollback_is_fixed
    $ urm_fixed_probe_native_a_sensitive = renpy.ui.ChoiceReturn("Route A", 0).get_sensitive()
    $ urm_fixed_probe_native_b_sensitive = renpy.ui.ChoiceReturn("Route B", 1).get_sensitive()
    $ print("FIXED_CHOICE_PRE", urm_fixed_probe_block_all, urm_fixed_probe_before, urm_fixed_probe_native_a_sensitive, urm_fixed_probe_native_b_sensitive)

    show screen urm_fixed_choice_overlay

    menu:
        "Native route A":
            $ urm_fixed_probe_route = "A"

        "Native route B":
            $ urm_fixed_probe_route = "B"

    $ urm_fixed_probe_after = renpy.game.log.rollback_is_fixed
    $ print("FIXED_CHOICE_POST", urm_fixed_probe_block_all, urm_fixed_probe_route, urm_fixed_probe_after)

    if urm_fixed_probe_route == "A":
        "Fixed rollback probe selected route A."
    else:
        "Fixed rollback probe selected route B."

label urm_fixed_choice_probe_done:
    return


testcase urm_fixed_choice_urm_override_default:
    $ urm_fixed_probe_block_all = False
    run Jump("urm_fixed_choice_probe_start")
    "URM select route A"
    "Fixed rollback probe selected route A."
    label urm_fixed_choice_probe_done
    assert urm_fixed_probe_before is True
    assert urm_fixed_probe_native_a_sensitive is False
    assert urm_fixed_probe_native_b_sensitive is False
    assert urm_fixed_probe_route == "A"
    assert urm_fixed_probe_after is False
    $ renpy.quit()


testcase urm_fixed_choice_urm_override_block_all:
    $ urm_fixed_probe_block_all = True
    run Jump("urm_fixed_choice_probe_start")
    "URM select route A"
    "Fixed rollback probe selected route A."
    label urm_fixed_choice_probe_done
    assert urm_fixed_probe_before is True
    assert urm_fixed_probe_native_a_sensitive is False
    assert urm_fixed_probe_native_b_sensitive is False
    assert urm_fixed_probe_route == "A"
    assert urm_fixed_probe_after is False
    $ renpy.quit()
