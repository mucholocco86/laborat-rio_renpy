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
            value = renpy.python.py_eval(self.name, renpy.store.__dict__)
            if isinstance(value, bool):
                return 'boolean'
            elif isinstance(value, int):
                return 'int'
            elif isinstance(value, float):
                return 'float'
            elif isinstance(value, list):
                return 'list'
            elif isinstance(value, dict):
                return 'dict'
            elif isinstance(value, basestring):
                return 'string'
            return 'unknown'

        def getChild(self, childVarName):
            parentValue = renpy.python.py_eval(self.name, renpy.store.__dict__)
            if isinstance(parentValue, list) and isinstance(childVarName, int):
                return Var(self.name + '[' + str(childVarName) + ']')
            elif isinstance(parentValue, dict):
                return Var(self.name + '[' + repr(childVarName) + ']')
            return Var(self.name + '.' + str(childVarName))

        def delete(self):
            parentPath, keyExpression = self.name.split('[', 1)
            key = renpy.python.py_eval(keyExpression[:-1], renpy.store.__dict__)
            parent = renpy.python.py_eval(parentPath, renpy.store.__dict__)
            del parent[key]

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

    class CreateVar:
        def __init__(self, varName, varVal, varType, onSuccess, screenErrorVariable, overwrite=False):
            self.varName = varName
            self.varVal = varVal
            self.varType = varType
            self.onSuccess = onSuccess
            self.screenErrorVariable = screenErrorVariable
            self.overwrite = overwrite

        def __call__(self):
            varName = self.varName() if callable(self.varName) else self.varName
            varVal = self.varVal() if callable(self.varVal) else self.varVal
            varType = self.varType() if callable(self.varType) else self.varType
            overwrite = self.overwrite() if callable(self.overwrite) else self.overwrite

            if not overwrite and hasattr(renpy.store, varName):
                renpy.store.SetScreenVariable(self.screenErrorVariable, 'A variable with this name already exists')()
                return

            isFrozen = VarsStore.isFrozen(varName)
            try:
                settableValue = None
                if varType == 'string':
                    settableValue = varVal
                elif varType == 'boolean':
                    settableValue = bool(varVal)
                elif varType == 'int' and Search.isInt(varVal):
                    settableValue = int(varVal)
                elif varType == 'float' and Search.isFloat(varVal):
                    settableValue = float(varVal)

                if settableValue:
                    if isFrozen: VarsStore.unfreeze(varName)
                    setattr(renpy.store, varName, settableValue)
                    self.onSuccess()
                else:
                    print("0x52: No valid value for {} (varType: {})".format(varName, varType))
                    renpy.store.SetScreenVariable(self.screenErrorVariable, 'Invalid value for variable type')()
            except Exception as e:
                print('0x52: Couldn\'t set value for "{}". {}'.format(varName, e))
                renpy.store.SetScreenVariable(self.screenErrorVariable, 'Failed to set variable. Check log for details')()
            finally:
                if isFrozen: VarsStore.freeze(varName)



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


# Save/load test: save the URM-style scalar edit, mutate it, then reload the
# native Ren'Py save. The marker lives in the test runner module, outside the
# game stores serialized by the save.
default urm_save_load_context_before = None

label urm_edit_save_load_start:
    if renpy.test.testexecution.urm_probe_save_load_reentered:
        jump urm_edit_save_load_verify

    $ urm_save_load_context_before = renpy.game.context().rollback
    $ renpy.game.context().rollback = True
    $ urm_rollback_value = 10
    $ renpy.checkpoint("before-save-load-edit")

    if renpy.can_load("urm-probe-edit-roundtrip"):
        $ renpy.unlink_save("urm-probe-edit-roundtrip")

    show screen urm_edit_probe
    pause 0.5

    $ print("SAVELOAD_BEFORE_SAVE", urm_rollback_value)
    $ renpy.save("urm-probe-edit-roundtrip")

    if renpy.test.testexecution.urm_probe_save_load_reentered:
        jump urm_edit_save_load_verify

    $ renpy.test.testexecution.urm_probe_save_load_reentered = True
    $ urm_rollback_value = 123
    $ print("SAVELOAD_BEFORE_LOAD", urm_rollback_value)
    $ renpy.load("urm-probe-edit-roundtrip")


label urm_edit_save_load_verify:
    $ print("SAVELOAD_AFTER_LOAD", urm_rollback_value)
    "Save/load restored value: [urm_rollback_value]."
    return


testcase urm_edit_save_load_roundtrip:
    $ renpy.test.testexecution.urm_probe_save_load_reentered = False
    run Jump("urm_edit_save_load_start")
    "Apply manual edit"
    label urm_edit_save_load_verify
    assert urm_rollback_value == 99
    assert urm_save_load_context_before is False
    assert renpy.test.testexecution.urm_probe_save_load_reentered is True
    $ renpy.quit()


# Container probe models URM_add_item -> SetVarValue -> Var.setValue(append)
# using a Ren'Py-compiled list, which should be a RevertableList.
default urm_rollback_list = [10]
default urm_list_context_before = None
default urm_list_route = 0

screen urm_list_edit_probe():
    modal True
    zorder 200

    frame:
        xalign 0.5
        yalign 0.5

        textbutton "Append item via reduced URM action":
            action [
                Hide("urm_list_edit_probe"),
                urm_probe_urm.SetVarValue(
                    urm_probe_urm.Var("urm_rollback_list"),
                    None,
                    None,
                    "20",
                    overruleVarType="int",
                    operator="append",
                ),
            ]

label urm_edit_container_rollback_start:
    $ urm_list_context_before = renpy.game.context().rollback
    $ renpy.game.context().rollback = True
    $ urm_list_route = 0
    $ urm_rollback_list = [10]
    $ renpy.checkpoint("before-container-edit")

    show screen urm_list_edit_probe
    pause 0.5

    menu:
        "Container route once":
            $ urm_list_route = 1

    menu:
        "Container route twice":
            $ urm_list_route = 2

    $ print("CONTAINER_ROLLBACK_PRE", list(urm_rollback_list), urm_list_route)
    $ renpy.rollback(force=False, checkpoints=3, label="urm_edit_container_rollback_verify")

label urm_edit_container_rollback_verify:
    $ print("CONTAINER_ROLLBACK_AT_VERIFY", list(urm_rollback_list), urm_list_route)
    "Container rollback restored list: [urm_rollback_list]."
    return

testcase urm_edit_container_rollback:
    run Jump("urm_edit_container_rollback_start")
    "Append item via reduced URM action"
    "Container route once"
    "Container route twice"
    label urm_edit_container_rollback_verify
    assert list(urm_rollback_list) == [10]
    assert urm_list_route == 0
    assert urm_list_context_before is False
    $ renpy.quit()


# Dictionary child probe models Var.getChild + SetVarValue editing an item.
default urm_rollback_dict = {"a": 10}
default urm_dict_context_before = None
default urm_dict_route = 0

screen urm_dict_edit_probe():
    modal True
    zorder 200

    frame:
        xalign 0.5
        yalign 0.5

        textbutton "Edit dictionary item via reduced URM action":
            action [
                Hide("urm_dict_edit_probe"),
                urm_probe_urm.SetVarValue(
                    urm_probe_urm.Var("urm_rollback_dict"),
                    None,
                    None,
                    "20",
                    overruleVarType="int",
                    varChildKey="a",
                ),
            ]

label urm_edit_dict_rollback_start:
    $ urm_dict_context_before = renpy.game.context().rollback
    $ renpy.game.context().rollback = True
    $ urm_dict_route = 0
    $ urm_rollback_dict = {"a": 10}
    $ renpy.checkpoint("before-dictionary-edit")

    show screen urm_dict_edit_probe
    pause 0.5

    menu:
        "Dictionary route once":
            $ urm_dict_route = 1

    menu:
        "Dictionary route twice":
            $ urm_dict_route = 2

    $ print("DICT_ROLLBACK_PRE", dict(urm_rollback_dict), urm_dict_route)
    $ renpy.rollback(force=False, checkpoints=3, label="urm_edit_dict_rollback_verify")

label urm_edit_dict_rollback_verify:
    $ print("DICT_ROLLBACK_AT_VERIFY", dict(urm_rollback_dict), urm_dict_route)
    "Dictionary rollback restored dictionary item."
    return

testcase urm_edit_dict_rollback:
    run Jump("urm_edit_dict_rollback_start")
    "Edit dictionary item via reduced URM action"
    "Dictionary route once"
    "Dictionary route twice"
    label urm_edit_dict_rollback_verify
    assert dict(urm_rollback_dict) == {"a": 10}
    assert urm_dict_route == 0
    assert urm_dict_context_before is False
    $ renpy.quit()


# Deletion probe models Var.delete for a list index and dictionary key.
default urm_delete_list = [10, 20]
default urm_delete_dict = {"a": 10, "b": 20}
default urm_delete_context_before = None
default urm_delete_route = 0

screen urm_delete_items_probe():
    modal True
    zorder 200

    frame:
        xalign 0.5
        yalign 0.5

        textbutton "Delete list index and dictionary key":
            action [
                Hide("urm_delete_items_probe"),
                Function(urm_probe_urm.Var("urm_delete_list").getChild(0).delete, _update_screens=False),
                Function(urm_probe_urm.Var("urm_delete_dict").getChild("a").delete),
            ]

label urm_delete_items_rollback_start:
    $ urm_delete_context_before = renpy.game.context().rollback
    $ renpy.game.context().rollback = True
    $ urm_delete_route = 0
    $ urm_delete_list = [10, 20]
    $ urm_delete_dict = {"a": 10, "b": 20}
    $ renpy.checkpoint("before-container-delete")

    show screen urm_delete_items_probe
    pause 0.5

    menu:
        "Delete route once":
            $ urm_delete_route = 1

    menu:
        "Delete route twice":
            $ urm_delete_route = 2

    $ print("DELETE_ROLLBACK_PRE", list(urm_delete_list), dict(urm_delete_dict), urm_delete_route)
    $ renpy.rollback(force=False, checkpoints=3, label="urm_delete_items_rollback_verify")

label urm_delete_items_rollback_verify:
    $ print("DELETE_ROLLBACK_AT_VERIFY", list(urm_delete_list), dict(urm_delete_dict), urm_delete_route)
    "Container deletion rollback verification."
    return

testcase urm_delete_container_items_rollback:
    run Jump("urm_delete_items_rollback_start")
    "Delete list index and dictionary key"
    "Delete route once"
    "Delete route twice"
    label urm_delete_items_rollback_verify
    assert list(urm_delete_list) == [10, 20]
    assert dict(urm_delete_dict) == {"a": 10, "b": 20}
    assert urm_delete_route == 0
    assert urm_delete_context_before is False
    $ renpy.quit()


# CreateVar probe mirrors the converted class's typed conversion and
# truthiness gate. The modal screen captures its native SetScreenVariable errors.
default urm_create_context_before = None

screen urm_createvar_probe():
    modal True
    zorder 200
    default errorMessage = None

    frame:
        xalign 0.5
        yalign 0.5

        vbox:
            spacing 8
            text "CreateVar falsy-value probe"
            text "[errorMessage]" if errorMessage
            textbutton "Create integer zero":
                action urm_probe_urm.CreateVar("urm_created_zero", "0", "int", Hide("urm_createvar_probe"), "errorMessage")
            textbutton "Create boolean false":
                action urm_probe_urm.CreateVar("urm_created_false", False, "boolean", Hide("urm_createvar_probe"), "errorMessage")
            textbutton "Create empty string":
                action urm_probe_urm.CreateVar("urm_created_empty", "", "string", Hide("urm_createvar_probe"), "errorMessage")
            textbutton "Create integer seven":
                action urm_probe_urm.CreateVar("urm_created_seven", "7", "int", Hide("urm_createvar_probe"), "errorMessage")

label urm_createvar_probe_start:
    $ urm_create_context_before = renpy.game.context().rollback
    $ renpy.game.context().rollback = True
    $ renpy.store.__dict__.pop("urm_created_zero", None)
    $ renpy.store.__dict__.pop("urm_created_false", None)
    $ renpy.store.__dict__.pop("urm_created_empty", None)
    $ renpy.store.__dict__.pop("urm_created_seven", None)
    $ renpy.checkpoint("before-createvar-falsy-probe")
    show screen urm_createvar_probe
    pause 0.5

label urm_createvar_probe_done:
    "CreateVar probe completed."
    return

testcase urm_createvar_falsy_runtime:
    run Jump("urm_createvar_probe_start")
    "Create integer zero"
    assert not hasattr(renpy.store, "urm_created_zero")
    "Create boolean false"
    assert not hasattr(renpy.store, "urm_created_false")
    "Create empty string"
    assert not hasattr(renpy.store, "urm_created_empty")
    "Create integer seven"
    label urm_createvar_probe_done
    assert urm_created_seven == 7
    assert urm_create_context_before is False
    $ renpy.quit()
