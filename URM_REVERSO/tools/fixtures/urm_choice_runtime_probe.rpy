# Isolated Ren'Py 7.4.11 runtime probe.
# This reproduces the narrow URMChoice.Action contract without loading or
# modifying URM source files, Wells files, or the SDK.

default urm_probe_result = None
default urm_probe_enabled = False

init python:
    def urm_probe_select(label, index):
        # Mirrors URMChoice.Action: clear fixed rollback, then return the
        # structural menu index through ChoiceReturn.
        renpy.game.log.rollback_is_fixed = False
        return renpy.ui.ChoiceReturn(label, index)()

screen urm_probe():
    modal True
    zorder 200

    frame:
        xalign 0.5
        yalign 0.5

        vbox:
            spacing 12
            text "Isolated URM Choice action probe"

            textbutton "Select hidden route":
                action [
                    Hide("urm_probe"),
                    Function(urm_probe_select, "Hidden route", 1, _update_screens=False),
                ]


label urm_probe_start:
    $ urm_probe_result = None

    if urm_probe_enabled:
        show screen urm_probe

    menu:
        "Native visible route":
            $ urm_probe_result = "native-visible"
            jump urm_probe_done

        "Hidden route" if False:
            $ urm_probe_result = "forced-hidden"
            jump urm_probe_done


label urm_probe_done:
    "Probe route: [urm_probe_result]."
    return


testcase urm_native_visible_route:
    run Jump("urm_probe_start")
    "Native visible route"
    label urm_probe_done
    assert urm_probe_result == "native-visible"
    $ renpy.quit()


testcase urm_force_condition_false:
    $ urm_probe_enabled = True
    run Jump("urm_probe_start")
    "Select hidden route"
    label urm_probe_done
    assert urm_probe_result == "forced-hidden"
    $ renpy.quit()


default urm_rollback_value = 10
default urm_rollback_context_before = None

init python in urm_probe_urm:
    class VarsStore:
        @staticmethod
        def isFrozen(varName):
            return False

        @staticmethod
        def unfreeze(varName):
            pass

        @staticmethod
        def freeze(varName):
            pass

    class SearchClass:
        def isInt(self, value):
            try:
                int(value)
                return True
            except:
                return False

        def isFloat(self, value):
            try:
                float(value)
                return True
            except:
                return False

    Search = SearchClass()

    class Var:
        def __init__(self, varName, storeDict=None):
            self._m1_vars__varName = varName
            self._m1_vars__storeDict = storeDict

        @property
        def name(self):
            return self._m1_vars__varName

        @property
        def isEditable(self):
            return not bool(self._m1_vars__storeDict)

        @property
        def varType(self):
            value = getattr(renpy.store, self.name)
            if isinstance(value, bool):
                return 'boolean'
            elif isinstance(value, int):
                return 'int'
            elif isinstance(value, float):
                return 'float'
            elif isinstance(value, basestring):
                return 'string'
            return 'unknown'

        def getChild(self, childVarName):
            return Var(self.name + '.' + str(childVarName))

        def setValue(self, newValue, overruleVarType=None, operator='=', varChildKey=None):
            if not self.isEditable: return False
            if callable(newValue): newValue = newValue()
            if callable(overruleVarType): overruleVarType = overruleVarType()
            if callable(operator): operator = operator()
            if callable(varChildKey): varChildKey = varChildKey()

            settableVar = self if not varChildKey else self.getChild(varChildKey)

            varType = overruleVarType or settableVar.varType
            isFrozen = VarsStore.isFrozen(self._m1_vars__varName)
            try:
                settableValue = None
                if varType == 'string':
                    settableValue = '"""'+newValue+'"""'
                elif varType == 'boolean':
                    settableValue = str(bool(newValue))
                elif varType == 'int' and Search.isInt(newValue):
                    settableValue = str(int(newValue))
                elif varType == 'float' and Search.isFloat(newValue):
                    settableValue = str(float(newValue))

                if settableValue:
                    if isFrozen: VarsStore.unfreeze(self._m1_vars__varName)

                    if operator == 'append':
                        exec('renpy.store.'+settableVar.name+'.append('+settableValue+')')
                    else:
                        exec('renpy.store.'+settableVar.name+operator+settableValue)
                    return True
                else:
                    print("0x52: No valid value for {} (varType: {})".format(settableVar.name, varType))
            except Exception as e:
                print("0x52: Couldn't set value for "+settableVar.name+'. '+str(e))
                pass
            finally:
                if isFrozen: VarsStore.freeze(self._m1_vars__varName)
            return False

    class SetVarValue:
        def __init__(self, var, onSuccess, screenErrorVariable, *args, **kwargs):
            self.var = var
            self.onSuccess = onSuccess
            self.screenErrorVariable = screenErrorVariable
            self.args = args
            self.kwargs = kwargs

        def __call__(self):
            if self.var.setValue(*self.args, **self.kwargs):
                if callable(self.onSuccess):
                    self.onSuccess()
            elif self.screenErrorVariable:
                renpy.store.SetScreenVariable(self.screenErrorVariable, 'Unable to set variable, the value is probably invalid')()


screen urm_edit_probe():
    modal True
    zorder 200

    frame:
        xalign 0.5
        yalign 0.5

        textbutton "Apply manual edit":
            action [
                Hide("urm_edit_probe"),
                urm_probe_urm.SetVarValue(urm_probe_urm.Var("urm_rollback_value"), None, None, "99"),
            ]


label urm_edit_rollback_start:
    # The Ren'Py test runner uses a main-menu context with rollback disabled.
    # Enable it only in this disposable fixture to model gameplay.
    $ urm_rollback_context_before = renpy.game.context().rollback
    $ renpy.game.context().rollback = True
    $ renpy.checkpoint("before-manual-edit")
    show screen urm_edit_probe
    pause 0.5
    $ renpy.rollback(force=True, checkpoints=1, label="urm_edit_rollback_verify")


label urm_edit_rollback_verify:
    $ print("ROLLBACK_VALUE_AT_VERIFY", urm_rollback_value)
    "Rollback restored value: [urm_rollback_value]."
    return


testcase urm_manual_edit_rollback:
    run Jump("urm_edit_rollback_start")
    "Apply manual edit"
    label urm_edit_rollback_verify
    assert urm_rollback_value == 10
    assert urm_rollback_context_before is False
    $ renpy.quit()


# Normal rollback test: same reduced URM edit action, followed by two native
# menu interactions. This uses force=False and restores across both choices.
default urm_ordinary_route = 0
default urm_ordinary_context_before = None

label urm_edit_ordinary_rollback_start:
    # The test harness enters from the main menu. Enable gameplay rollback
    # only in this disposable fixture, matching the prior probe.
    $ urm_ordinary_context_before = renpy.game.context().rollback
    $ renpy.game.context().rollback = True
    $ urm_ordinary_route = 0
    $ renpy.checkpoint("before-ordinary-edit")

    show screen urm_edit_probe
    pause 0.5

    menu:
        "Advance once":
            $ urm_ordinary_route = 1

    menu:
        "Advance twice":
            $ urm_ordinary_route = 2

    $ print("ORDINARY_ROLLBACK_PRE", urm_rollback_value, urm_ordinary_route)
    $ print("ORDINARY_ROLLBACK_GATES", renpy.store._rollback, renpy.game.context().rollback, renpy.config.rollback_enabled)
    $ renpy.rollback(force=False, checkpoints=3, label="urm_edit_ordinary_rollback_verify")


label urm_edit_ordinary_rollback_verify:
    $ print("ORDINARY_ROLLBACK_AT_VERIFY", urm_rollback_value, urm_ordinary_route)
    "Ordinary rollback restored value: [urm_rollback_value]."
    return


testcase urm_edit_ordinary_rollback:
    run Jump("urm_edit_ordinary_rollback_start")
    "Apply manual edit"
    "Advance once"
    "Advance twice"
    label urm_edit_ordinary_rollback_verify
    assert urm_rollback_value == 10
    assert urm_ordinary_route == 0
    assert urm_ordinary_context_before is False
    $ renpy.quit()


# Native input test: K_PAGEUP is sent by the Ren'Py test harness while the
# game is in an ordinary say interaction. The SDK underlay maps rollback to
# renpy.rollback with its default force=False.
default urm_key_route = 0
default urm_key_context_before = None

label urm_edit_key_rollback_start:
    $ urm_key_context_before = renpy.game.context().rollback
    $ renpy.game.context().rollback = True
    $ urm_key_route = 0
    $ renpy.checkpoint("before-key-rollback-edit")

    show screen urm_edit_probe
    pause 0.5

    menu:
        "Key route once":
            $ urm_key_route = 1

    menu:
        "Key route twice":
            $ urm_key_route = 2

    $ print("NATIVE_KEY_BEFORE", urm_rollback_value, urm_key_route)
    "Reached the state after two choices."
    return


testcase urm_edit_native_key_rollback:
    run Jump("urm_edit_key_rollback_start")
    "Apply manual edit"
    "Key route once"
    "Key route twice"
    "Reached the state after two choices."
    type PAGEUP
    $ print("NATIVE_KEY_AFTER_1", urm_rollback_value, urm_key_route)
    type PAGEUP
    $ print("NATIVE_KEY_AFTER_2", urm_rollback_value, urm_key_route)
    type PAGEUP
    $ print("NATIVE_KEY_AFTER_3", urm_rollback_value, urm_key_route)
    assert urm_rollback_value == 10
    assert urm_key_route == 0
    assert urm_key_context_before is False
    $ renpy.quit()
