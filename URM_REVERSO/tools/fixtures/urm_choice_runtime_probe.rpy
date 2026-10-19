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
    _frozen_names = set()
    _monitored_names = set()

    class VarsStore:
        @staticmethod
        def isFrozen(varName):
            return varName in _frozen_names

        @staticmethod
        def unfreeze(varName):
            _frozen_names.discard(varName)

        @staticmethod
        def freeze(varName):
            _frozen_names.add(varName)

        @staticmethod
        def isMonitored(varName):
            return varName in _monitored_names

        @staticmethod
        def monitor(varName):
            _monitored_names.add(varName)

        @staticmethod
        def unmonitor(varName):
            _monitored_names.discard(varName)

    class Notifications:
        @staticmethod
        def add(**kwargs):
            renpy.store.urm_notify_probe_records.append(
                (kwargs.get("label"), kwargs.get("text"), kwargs.get("prevVal"), kwargs.get("newVal"))
            )

    class StoreMonitor:
        @staticmethod
        def handleVarChange(varName, oldVal, newVal):
            if VarsStore.isFrozen(varName):
                if newVal != oldVal:
                    Var(varName).setValue(str(oldVal))
                return False
            elif VarsStore.isMonitored(varName):
                if not renpy.get_screen("URM_modify_value") and oldVal != newVal:
                    Notifications.add(label="Variable changed", text=varName, prevVal=oldVal, newVal=newVal)
            return True

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
            if errorMessage:
                text "[errorMessage]"
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


# Save/load probe for mutated RevertableList and RevertableDict objects.
default urm_save_container_list = [10]
default urm_save_container_dict = {"a": 10}
default urm_save_container_context_before = None

screen urm_save_container_probe():
    modal True
    zorder 200

    frame:
        xalign 0.5
        yalign 0.5

        textbutton "Apply list and dictionary edits":
            action [
                Hide("urm_save_container_probe"),
                urm_probe_urm.SetVarValue(
                    urm_probe_urm.Var("urm_save_container_list"),
                    None,
                    None,
                    "20",
                    overruleVarType="int",
                    operator="append",
                ),
                urm_probe_urm.SetVarValue(
                    urm_probe_urm.Var("urm_save_container_dict"),
                    None,
                    None,
                    "20",
                    overruleVarType="int",
                    varChildKey="a",
                ),
            ]

label urm_save_load_containers_start:
    if renpy.test.testexecution.urm_probe_container_save_reentered:
        jump urm_save_load_containers_verify

    $ urm_save_container_context_before = renpy.game.context().rollback
    $ renpy.game.context().rollback = True
    $ urm_save_container_list = [10]
    $ urm_save_container_dict = {"a": 10}

    if renpy.can_load("urm-probe-container-roundtrip"):
        $ renpy.unlink_save("urm-probe-container-roundtrip")

    show screen urm_save_container_probe
    pause 0.5

    $ print("CONTAINER_SAVE_BEFORE_SAVE", list(urm_save_container_list), dict(urm_save_container_dict))
    $ renpy.save("urm-probe-container-roundtrip")

    if renpy.test.testexecution.urm_probe_container_save_reentered:
        jump urm_save_load_containers_verify

    $ renpy.test.testexecution.urm_probe_container_save_reentered = True
    $ urm_save_container_list.append(30)
    $ urm_save_container_dict["a"] = 30
    $ print("CONTAINER_SAVE_BEFORE_LOAD", list(urm_save_container_list), dict(urm_save_container_dict))
    $ renpy.load("urm-probe-container-roundtrip")

label urm_save_load_containers_verify:
    $ print("CONTAINER_SAVE_AFTER_LOAD", list(urm_save_container_list), dict(urm_save_container_dict))
    "Container save/load verification complete."
    return

testcase urm_save_load_containers_roundtrip:
    $ renpy.test.testexecution.urm_probe_container_save_reentered = False
    run Jump("urm_save_load_containers_start")
    "Apply list and dictionary edits"
    label urm_save_load_containers_verify
    assert list(urm_save_container_list) == [10, 20]
    assert dict(urm_save_container_dict) == {"a": 20}
    assert urm_save_container_context_before is False
    assert renpy.test.testexecution.urm_probe_container_save_reentered is True
    $ renpy.quit()


# Reduced StoreMonitor hook probe.
# It contrasts the native SetVariable action (which uses Ren'Py's
# __set_field helper) with the URM-style SetVarValue assignment
# (which writes directly to the store module).
default urm_monitor_probe_hits = 0
default urm_monitor_probe_value = 10
default urm_monitor_probe_method = None

init python:
    import types

    def urm_monitor_probe_injected_set_field(obj, name, value, *args, **kwargs):
        renpy.store.urm_monitor_probe_hits += 1
        if renpy.store.urm_monitor_probe_enabled:
            old_value = getattr(obj, name)
            if not urm_probe_urm.StoreMonitor.handleVarChange(name, old_value, value):
                return None
        return renpy.store.urm_monitor_probe_original_set_field(obj, name, value, *args, **kwargs)

    def urm_monitor_probe_install():
        for method_name in ('_m1_00action_data__set_field', '_set_field'):
            if hasattr(renpy.store, method_name):
                original_method = getattr(renpy.store, method_name)
                renpy.store.urm_monitor_probe_original_set_field = types.FunctionType(
                    original_method.func_code,
                    original_method.func_globals,
                    original_method.func_name,
                    original_method.func_defaults,
                    original_method.func_closure,
                )
                original_method.func_code = urm_monitor_probe_injected_set_field.func_code
                renpy.store.urm_monitor_probe_method = method_name
                return method_name

        raise Exception("No SetField helper found in the SDK store.")

label urm_monitor_probe_start:
    $ urm_monitor_probe_hits = 0
    $ urm_monitor_probe_value = 10
    $ urm_monitor_probe_install()
    $ print("STOREMONITOR_HOOK_METHOD", urm_monitor_probe_method)

    # Ren'Py's native variable action delegates to __set_field.
    $ renpy.store.SetVariable("urm_monitor_probe_value", 20)()
    $ print("STOREMONITOR_AFTER_NATIVE_SETVARIABLE", urm_monitor_probe_hits, urm_monitor_probe_value)

    # The reduced URM action uses exec + setattr(store, ...), not SetVariable.
    $ urm_probe_urm.SetVarValue(
        urm_probe_urm.Var("urm_monitor_probe_value"),
        None,
        None,
        "30",
    )()
    $ print("STOREMONITOR_AFTER_URM_SET", urm_monitor_probe_hits, urm_monitor_probe_value)
    jump urm_monitor_probe_verify

label urm_monitor_probe_verify:
    $ print("STOREMONITOR_ASSERTIONS", urm_monitor_probe_method, urm_monitor_probe_hits, urm_monitor_probe_value)
    $ assert urm_monitor_probe_method in ("_m1_00action_data__set_field", "_set_field")
    $ assert urm_monitor_probe_hits == 1
    $ assert urm_monitor_probe_value == 30
    $ renpy.quit()

testcase urm_storemonitor_assignment_hook:
    run Jump("urm_monitor_probe_start")


# Reduced callback timing probe. This installs a small python_callbacks
# observer that mirrors the StoreMonitor's checkpoint request and non-cycling
# StoreDict delta read, without loading the URM package itself.
default urm_callback_probe_enabled = False
default urm_callback_probe_rollback_mode = False
default urm_callback_probe_context_before = None
default urm_callback_probe_value = 10
default urm_callback_probe_stage = "init"
default urm_callback_probe_count = 0
default urm_callback_probe_events = []
default urm_callback_probe_count_before_action = None
default urm_callback_probe_count_after_action = None
default urm_callback_probe_saw_edit = False
default urm_callback_probe_old_value = None
default urm_callback_probe_new_value = None

init python:
    def urm_callback_probe_callback():
        if not renpy.store.urm_callback_probe_enabled:
            return

        context = renpy.game.context()
        changes = renpy.store.__dict__.get_changes(False)
        if isinstance(changes, tuple):
            changes = changes[0]

        renpy.store.urm_callback_probe_count += 1
        has_value_delta = "urm_callback_probe_value" in changes
        old_value = changes.get("urm_callback_probe_value", None)
        new_value = renpy.store.urm_callback_probe_value
        event = (
            renpy.store.urm_callback_probe_stage,
            new_value,
            context.current,
            context.force_checkpoint,
            renpy.game.log.force_checkpoint,
            has_value_delta,
            old_value,
        )
        renpy.store.urm_callback_probe_events.append(event)
        print("CALLBACK_PROBE_EVENT", renpy.store.urm_callback_probe_count, event)

        if has_value_delta and new_value == 99:
            renpy.store.urm_callback_probe_saw_edit = True
            renpy.store.urm_callback_probe_old_value = old_value
            renpy.store.urm_callback_probe_new_value = new_value

        # Mirrors the StoreMonitor's request; Context.run transfers it later.
        context.force_checkpoint = True

    def urm_callback_probe_before_action():
        renpy.store.urm_callback_probe_count_before_action = renpy.store.urm_callback_probe_count
        print("CALLBACK_PROBE_BEFORE_SCREEN_ACTION", renpy.store.urm_callback_probe_count, renpy.store.urm_callback_probe_value)

    def urm_callback_probe_after_action():
        renpy.store.urm_callback_probe_count_after_action = renpy.store.urm_callback_probe_count
        print("CALLBACK_PROBE_AFTER_SCREEN_ACTION", renpy.store.urm_callback_probe_count, renpy.store.urm_callback_probe_value)
        if renpy.store.urm_callback_probe_count_after_action != renpy.store.urm_callback_probe_count_before_action:
            raise Exception("python_callbacks ran during the screen action.")
        if renpy.store.urm_callback_probe_value != 99:
            raise Exception("URM-style screen edit did not set the probe value.")

screen urm_callback_probe_screen():
    modal True
    zorder 200

    frame:
        xalign 0.5
        yalign 0.5

        textbutton "Apply callback timing edit":
            action [
                Function(urm_callback_probe_before_action, _update_screens=False),
                Hide("urm_callback_probe_screen"),
                urm_probe_urm.SetVarValue(
                    urm_probe_urm.Var("urm_callback_probe_value"),
                    None,
                    None,
                    "99",
                ),
                Function(urm_callback_probe_after_action, _update_screens=False),
            ]

label urm_callback_probe_start:
    $ urm_callback_probe_enabled = False
    $ urm_callback_probe_value = 10
    $ urm_callback_probe_stage = "install"
    $ urm_callback_probe_count = 0
    $ urm_callback_probe_events = []
    $ urm_callback_probe_count_before_action = None
    $ urm_callback_probe_count_after_action = None
    $ urm_callback_probe_saw_edit = False
    $ urm_callback_probe_old_value = None
    $ urm_callback_probe_new_value = None
    if urm_callback_probe_rollback_mode:
        $ urm_callback_probe_context_before = renpy.game.context().rollback
        $ renpy.game.context().rollback = True
        $ renpy.checkpoint("before-callback-screen-edit")
    $ renpy.config.python_callbacks.append(urm_callback_probe_callback)

    $ urm_callback_probe_enabled = True
    $ urm_callback_probe_stage = "screen_open"
    show screen urm_callback_probe_screen
    pause 0.5

    $ urm_callback_probe_stage = "after_edit_python_body"
    $ print("CALLBACK_PROBE_AFTER_NEXT_PYTHON_NODE", urm_callback_probe_count, urm_callback_probe_value, urm_callback_probe_saw_edit, urm_callback_probe_old_value, urm_callback_probe_new_value)
    $ assert urm_callback_probe_count_after_action == urm_callback_probe_count_before_action
    $ assert urm_callback_probe_count > urm_callback_probe_count_after_action
    $ assert urm_callback_probe_value == 99
    $ print("CALLBACK_PROBE_RESULT", urm_callback_probe_count, urm_callback_probe_saw_edit, urm_callback_probe_old_value, urm_callback_probe_new_value, list(urm_callback_probe_events))
    if urm_callback_probe_rollback_mode:
        $ print("CALLBACK_PROBE_BEFORE_ROLLBACK", urm_callback_probe_value, urm_callback_probe_saw_edit, renpy.game.log.force_checkpoint)
        $ renpy.rollback(force=True, checkpoints=1, label="urm_callback_probe_rollback_verify")
    else:
        $ renpy.quit()

label urm_callback_probe_rollback_verify:
    $ print("CALLBACK_PROBE_AFTER_ROLLBACK", urm_callback_probe_value)
    "Callback and rollback verification."
    return

testcase urm_storemonitor_callback_after_screen_edit:
    run Jump("urm_callback_probe_start")
    "Apply callback timing edit"


label urm_callback_probe_rollback_start:
    $ urm_callback_probe_rollback_mode = True
    jump urm_callback_probe_start

testcase urm_storemonitor_callback_with_gameplay_rollback:
    run Jump("urm_callback_probe_rollback_start")
    "Apply callback timing edit"
    label urm_callback_probe_rollback_verify
    assert urm_callback_probe_value == 10
    $ renpy.quit()


# Freeze probe: compare the native intercepted SetField route to direct
# URM-style Var.setValue and the callback's later frozen-value restoration.
default urm_monitor_freeze_enabled = False
default urm_monitor_probe_enabled = False
default urm_freeze_probe_rollback_mode = False
default urm_freeze_probe_value = 10
default urm_freeze_probe_callback_count = 0
default urm_freeze_probe_callback_delta = False
default urm_freeze_probe_callback_old = None
default urm_freeze_probe_callback_value_before = None
default urm_freeze_probe_value_after_native = None
default urm_freeze_probe_value_after_urm_edit = None
default urm_freeze_probe_is_frozen_after_edit = False
default urm_freeze_probe_is_frozen_after_callback = False

init python:
    def urm_freeze_probe_callback():
        if not renpy.store.urm_monitor_freeze_enabled:
            return

        changes = renpy.store.__dict__.get_changes(False)
        if isinstance(changes, tuple):
            changes = changes[0]

        renpy.store.urm_freeze_probe_callback_count += 1
        if "urm_freeze_probe_value" in changes:
            old_value = changes["urm_freeze_probe_value"]
            new_value = renpy.store.urm_freeze_probe_value
            renpy.store.urm_freeze_probe_callback_delta = True
            renpy.store.urm_freeze_probe_callback_old = old_value
            renpy.store.urm_freeze_probe_callback_value_before = new_value
            print("FREEZE_PROBE_CALLBACK_BEFORE", old_value, new_value, urm_probe_urm.VarsStore.isFrozen("urm_freeze_probe_value"))
            urm_probe_urm.StoreMonitor.handleVarChange("urm_freeze_probe_value", old_value, new_value)
            print("FREEZE_PROBE_CALLBACK_AFTER", renpy.store.urm_freeze_probe_value, urm_probe_urm.VarsStore.isFrozen("urm_freeze_probe_value"))

        renpy.game.context().force_checkpoint = True

screen urm_freeze_probe_screen():
    modal True
    zorder 200

    frame:
        xalign 0.5
        yalign 0.5

        textbutton "Apply direct URM edit while frozen":
            action [
                Hide("urm_freeze_probe_screen"),
                urm_probe_urm.SetVarValue(
                    urm_probe_urm.Var("urm_freeze_probe_value"),
                    None,
                    None,
                    "30",
                ),
            ]

label urm_freeze_probe_start:
    $ urm_monitor_freeze_enabled = False
    $ urm_freeze_probe_value = 10
    $ urm_freeze_probe_callback_count = 0
    $ urm_freeze_probe_callback_delta = False
    $ urm_freeze_probe_callback_old = None
    $ urm_freeze_probe_callback_value_before = None
    $ urm_probe_urm._frozen_names.clear()
    $ urm_probe_urm.VarsStore.freeze("urm_freeze_probe_value")
    if urm_freeze_probe_rollback_mode:
        $ renpy.game.context().rollback = True
        $ renpy.checkpoint("before-frozen-urm-edit")
    $ urm_monitor_probe_install()
    $ urm_monitor_freeze_enabled = True
    $ renpy.config.python_callbacks.append(urm_freeze_probe_callback)
    $ print("FREEZE_PROBE_BEFORE_NATIVE", urm_freeze_probe_value, urm_probe_urm.VarsStore.isFrozen("urm_freeze_probe_value"))
    $ renpy.store.SetVariable("urm_freeze_probe_value", 20)()
    $ urm_freeze_probe_value_after_native = urm_freeze_probe_value
    $ print("FREEZE_PROBE_AFTER_NATIVE", urm_freeze_probe_value_after_native, urm_probe_urm.VarsStore.isFrozen("urm_freeze_probe_value"))
    $ assert urm_freeze_probe_value == 10
    show screen urm_freeze_probe_screen
    pause 0.5
    $ urm_freeze_probe_value_after_urm_edit = urm_freeze_probe_value
    $ urm_freeze_probe_is_frozen_after_edit = urm_probe_urm.VarsStore.isFrozen("urm_freeze_probe_value")
    $ print("FREEZE_PROBE_AFTER_URM_EDIT", urm_freeze_probe_value_after_urm_edit, urm_freeze_probe_is_frozen_after_edit)
    $ print("FREEZE_PROBE_AFTER_CALLBACK", urm_freeze_probe_callback_count, urm_freeze_probe_callback_delta, urm_freeze_probe_callback_old, urm_freeze_probe_callback_value_before, urm_freeze_probe_value, urm_probe_urm.VarsStore.isFrozen("urm_freeze_probe_value"))
    $ assert urm_freeze_probe_value_after_urm_edit in (10, 30)
    $ assert urm_freeze_probe_is_frozen_after_edit
    $ assert urm_freeze_probe_callback_count > 0
    if urm_freeze_probe_rollback_mode:
        $ print("FREEZE_PROBE_BEFORE_ROLLBACK", urm_freeze_probe_value, urm_freeze_probe_callback_delta, renpy.game.log.force_checkpoint)
        $ renpy.rollback(force=True, checkpoints=1, label="urm_freeze_probe_rollback_verify")
    else:
        $ assert urm_freeze_probe_callback_delta
        $ assert urm_freeze_probe_callback_old == 10
        $ assert urm_freeze_probe_value == 10
        $ assert urm_probe_urm.VarsStore.isFrozen("urm_freeze_probe_value")
        $ renpy.quit()

label urm_freeze_probe_rollback_start:
    $ urm_freeze_probe_rollback_mode = True
    jump urm_freeze_probe_start

label urm_freeze_probe_rollback_verify:
    $ print("FREEZE_PROBE_AFTER_ROLLBACK", urm_freeze_probe_value, urm_probe_urm.VarsStore.isFrozen("urm_freeze_probe_value"))
    "Freeze rollback verification."
    return

testcase urm_storemonitor_freeze_native_vs_urm:
    run Jump("urm_freeze_probe_start")
    "Apply direct URM edit while frozen"

testcase urm_storemonitor_freeze_with_gameplay_rollback:
    run Jump("urm_freeze_probe_rollback_start")
    "Apply direct URM edit while frozen"
    label urm_freeze_probe_rollback_verify
    assert urm_freeze_probe_value == 10
    assert urm_probe_urm.VarsStore.isFrozen("urm_freeze_probe_value")
    $ renpy.quit()


# Monitor-notification probes. These measure the synchronous native helper hook
# separately from later StoreMonitor-style callback processing.
default urm_notify_probe_value = 10
default urm_notify_probe_records = []
default urm_notify_probe_enabled = False
default urm_notify_rollback_mode = False
default urm_notify_native_rollback_mode = False
default urm_notify_probe_count_before_action = None
default urm_notify_probe_count_after_action = None
default urm_notify_probe_callback_delta = False
default urm_notify_probe_callback_old = None
default urm_notify_probe_callback_new = None

init python:
    def urm_notify_probe_callback():
        if not renpy.store.urm_notify_probe_enabled:
            return

        changes = renpy.store.__dict__.get_changes(False)
        if isinstance(changes, tuple):
            changes = changes[0]

        if "urm_notify_probe_value" in changes:
            old_value = changes["urm_notify_probe_value"]
            new_value = renpy.store.urm_notify_probe_value
            renpy.store.urm_notify_probe_callback_delta = True
            renpy.store.urm_notify_probe_callback_old = old_value
            renpy.store.urm_notify_probe_callback_new = new_value
            print("NOTIFY_PROBE_CALLBACK_BEFORE", old_value, new_value, len(renpy.store.urm_notify_probe_records))
            urm_probe_urm.StoreMonitor.handleVarChange("urm_notify_probe_value", old_value, new_value)
            print("NOTIFY_PROBE_CALLBACK_AFTER", len(renpy.store.urm_notify_probe_records))

        renpy.game.context().force_checkpoint = True

    def urm_notify_probe_before_action():
        renpy.store.urm_notify_probe_count_before_action = len(renpy.store.urm_notify_probe_records)
        print("NOTIFY_PROBE_BEFORE_ACTION", renpy.store.urm_notify_probe_count_before_action)

    def urm_notify_probe_after_action():
        renpy.store.urm_notify_probe_count_after_action = len(renpy.store.urm_notify_probe_records)
        print("NOTIFY_PROBE_AFTER_ACTION", renpy.store.urm_notify_probe_count_after_action, renpy.store.urm_notify_probe_records)

screen urm_notify_native_screen():
    modal True
    zorder 200

    frame:
        xalign 0.5
        yalign 0.5

        textbutton "Change monitored variable natively":
            action [
                Function(urm_notify_probe_before_action, _update_screens=False),
                Hide("urm_notify_native_screen"),
                SetVariable("urm_notify_probe_value", 20),
                Function(urm_notify_probe_after_action, _update_screens=False),
            ]

screen urm_notify_urm_screen():
    modal True
    zorder 200

    frame:
        xalign 0.5
        yalign 0.5

        textbutton "Change monitored variable through URM":
            action [
                Function(urm_notify_probe_before_action, _update_screens=False),
                Hide("urm_notify_urm_screen"),
                urm_probe_urm.SetVarValue(
                    urm_probe_urm.Var("urm_notify_probe_value"),
                    None,
                    None,
                    "30",
                ),
                Function(urm_notify_probe_after_action, _update_screens=False),
            ]

label urm_notify_native_start:
    $ urm_notify_probe_value = 10
    $ urm_notify_probe_records = []
    $ urm_notify_probe_callback_delta = False
    $ urm_notify_probe_callback_old = None
    $ urm_notify_probe_callback_new = None
    $ urm_probe_urm._monitored_names.clear()
    $ urm_probe_urm.VarsStore.monitor("urm_notify_probe_value")
    if urm_notify_native_rollback_mode:
        $ renpy.game.context().rollback = True
        $ renpy.checkpoint("before-monitored-native-edit")
    $ urm_monitor_probe_install()
    $ urm_monitor_probe_enabled = True
    $ urm_notify_probe_enabled = True
    $ renpy.config.python_callbacks.append(urm_notify_probe_callback)
    show screen urm_notify_native_screen
    pause 0.5
    $ print("NOTIFY_PROBE_NATIVE_FINAL", urm_notify_probe_value, list(urm_notify_probe_records), urm_notify_probe_callback_delta, urm_notify_probe_callback_old, urm_notify_probe_callback_new)
    $ assert urm_notify_probe_count_after_action >= 1
    $ assert urm_notify_probe_value == 20
    $ assert len(urm_notify_probe_records) >= 1
    if urm_notify_native_rollback_mode:
        $ print("NOTIFY_PROBE_NATIVE_BEFORE_ROLLBACK", urm_notify_probe_value, list(urm_notify_probe_records), urm_notify_probe_callback_delta, renpy.game.log.force_checkpoint)
        $ renpy.rollback(force=True, checkpoints=1, label="urm_notify_native_rollback_verify")
    else:
        $ assert urm_notify_probe_callback_delta
        $ assert urm_notify_probe_callback_old == 10
        $ assert urm_notify_probe_callback_new == 20
        $ renpy.quit()

label urm_notify_native_rollback_start:
    $ urm_notify_native_rollback_mode = True
    jump urm_notify_native_start

label urm_notify_native_rollback_verify:
    $ print("NOTIFY_PROBE_NATIVE_AFTER_ROLLBACK", urm_notify_probe_value, list(urm_notify_probe_records), urm_notify_probe_callback_delta)
    "Native monitor rollback verification."
    return

testcase urm_storemonitor_native_notification:
    run Jump("urm_notify_native_start")
    "Change monitored variable natively"

testcase urm_storemonitor_native_notification_with_rollback:
    run Jump("urm_notify_native_rollback_start")
    "Change monitored variable natively"
    label urm_notify_native_rollback_verify
    assert urm_notify_probe_value == 10
    $ renpy.quit()

label urm_notify_urm_start:
    $ urm_notify_probe_value = 10
    $ urm_notify_probe_records = []
    $ urm_notify_probe_callback_delta = False
    $ urm_notify_probe_callback_old = None
    $ urm_notify_probe_callback_new = None
    $ urm_probe_urm._monitored_names.clear()
    $ urm_probe_urm.VarsStore.monitor("urm_notify_probe_value")
    if urm_notify_rollback_mode:
        $ renpy.game.context().rollback = True
        $ renpy.checkpoint("before-monitored-urm-edit")
    $ urm_monitor_probe_install()
    $ urm_monitor_probe_enabled = True
    $ urm_notify_probe_enabled = True
    $ renpy.config.python_callbacks.append(urm_notify_probe_callback)
    show screen urm_notify_urm_screen
    pause 0.5
    $ print("NOTIFY_PROBE_URM_FINAL", urm_notify_probe_value, list(urm_notify_probe_records), urm_notify_probe_callback_delta, urm_notify_probe_callback_old, urm_notify_probe_callback_new, urm_monitor_probe_hits)
    $ assert urm_notify_probe_count_after_action == 0
    $ assert urm_notify_probe_value == 30
    $ assert urm_monitor_probe_hits == 0
    if urm_notify_rollback_mode:
        $ print("NOTIFY_PROBE_URM_BEFORE_ROLLBACK", urm_notify_probe_value, list(urm_notify_probe_records), urm_notify_probe_callback_delta, renpy.game.log.force_checkpoint)
        $ renpy.rollback(force=True, checkpoints=1, label="urm_notify_rollback_verify")
    else:
        $ assert urm_notify_probe_callback_delta
        $ assert urm_notify_probe_callback_old == 10
        $ assert urm_notify_probe_callback_new == 30
        $ assert len(urm_notify_probe_records) == 1
        $ renpy.quit()

label urm_notify_rollback_start:
    $ urm_notify_rollback_mode = True
    jump urm_notify_urm_start

label urm_notify_rollback_verify:
    $ print("NOTIFY_PROBE_URM_AFTER_ROLLBACK", urm_notify_probe_value, list(urm_notify_probe_records), urm_notify_probe_callback_delta)
    "Monitor rollback verification."
    return

testcase urm_storemonitor_urm_notification:
    run Jump("urm_notify_urm_start")
    "Change monitored variable through URM"

testcase urm_storemonitor_urm_notification_with_rollback:
    run Jump("urm_notify_rollback_start")
    "Change monitored variable through URM"
    label urm_notify_rollback_verify
    assert urm_notify_probe_value == 10
    $ renpy.quit()


# Lifecycle probe for the URM notification object graph.
# Mirrors x52NonPicklable from framework/modules/01utils.rpy and the
# Notification(s) list owner from classes/notifications.rpy.
init python in urm_probe_urm:
    class ProbeX52NonPicklable(python_object):
        def __setstate__(self, d):
            pass

        def __getstate__(self):
            return {}

        def __getnewargs__(self):
            return ()

        def __iter__(self):
            return None

        def itervalues(self):
            return None

    class ProbeNotification(ProbeX52NonPicklable):
        def __init__(self, notification_owner, label, text=None):
            self.notification_owner = notification_owner
            self.label = label
            self.text = text

    class ProbeNotificationsClass(ProbeX52NonPicklable):
        def __init__(self):
            self.notifications = []

        def add(self, label, text=None):
            notification = ProbeNotification(self, label, text)
            self.notifications.append(notification)

        def clear(self):
            self.notifications = []

    ProbeNotifications = ProbeNotificationsClass()

    def timeout_remove(notification):
        import time
        time.sleep(0.35)
        ProbeNotifications.notifications.remove(notification)
        renpy.store.urm_x52_timeout_done = True


label urm_x52_notification_object_rollback_start:
    $ renpy.game.context().rollback = True
    $ assert not isinstance(urm_probe_urm.ProbeNotifications, renpy.python.NoRollback)
    $ assert isinstance(urm_probe_urm.ProbeNotifications.notifications, renpy.python.RevertableList)
    $ print("X52_NOTIFICATION_PRE", type(urm_probe_urm.ProbeNotifications).__name__, type(urm_probe_urm.ProbeNotifications.notifications).__name__, len(urm_probe_urm.ProbeNotifications.notifications), isinstance(urm_probe_urm.ProbeNotifications, renpy.python.NoRollback))
    $ renpy.checkpoint("before-x52-notification-append")
    $ urm_probe_urm.ProbeNotifications.add("Variable changed", "urm_notification_probe")
    $ print("X52_NOTIFICATION_AFTER_ADD", len(urm_probe_urm.ProbeNotifications.notifications), urm_probe_urm.ProbeNotifications.notifications[0].label)
    $ renpy.rollback(force=True, checkpoints=1, label="urm_x52_notification_object_rollback_verify")


label urm_x52_notification_object_rollback_verify:
    $ print("X52_NOTIFICATION_AFTER_ROLLBACK", type(urm_probe_urm.ProbeNotifications.notifications).__name__, len(urm_probe_urm.ProbeNotifications.notifications))
    python:
        if len(urm_probe_urm.ProbeNotifications.notifications) != 1:
            raise Exception("Expected init-only notification list to retain one entry after rollback.")
    $ renpy.quit()


testcase urm_x52_nonpicklable_notification_list_rollback:
    run Jump("urm_x52_notification_object_rollback_start")


default urm_x52_notification_root = None


label urm_x52_notification_rooted_rollback_start:
    $ renpy.game.context().rollback = True
    $ urm_x52_notification_root = urm_probe_urm.ProbeNotifications
    $ renpy.checkpoint("after-x52-notification-root-registration")
    $ urm_probe_urm.ProbeNotifications.add("Variable changed", "rooted_notification_probe")
    $ print("X52_NOTIFICATION_ROOTED_AFTER_ADD", len(urm_probe_urm.ProbeNotifications.notifications))
    $ renpy.rollback(force=True, checkpoints=1, label="urm_x52_notification_rooted_rollback_verify")


label urm_x52_notification_rooted_rollback_verify:
    $ print("X52_NOTIFICATION_ROOTED_AFTER_ROLLBACK", type(urm_probe_urm.ProbeNotifications.notifications).__name__, len(urm_probe_urm.ProbeNotifications.notifications), urm_x52_notification_root is urm_probe_urm.ProbeNotifications)
    python:
        if len(urm_probe_urm.ProbeNotifications.notifications) != 0:
            raise Exception("Expected rooted notification list to restore its empty checkpoint state.")
        if urm_x52_notification_root is not None:
            raise Exception("Expected the temporary store root itself to roll back to None.")
    $ renpy.quit()


testcase urm_x52_rooted_notification_list_rollback:
    run Jump("urm_x52_notification_rooted_rollback_start")


# A visible screen holding the notification action may be another rollback root.
screen urm_x52_notification_overlay_probe():
    vbox:
        for notif in urm_probe_urm.ProbeNotifications.notifications:
            textbutton notif.label action notif


label urm_x52_notification_screen_rollback_start:
    $ renpy.game.context().rollback = True
    $ renpy.checkpoint("before-x52-notification-screen-add")
    $ urm_probe_urm.ProbeNotifications.add("Variable changed", "screen_notification_probe")
    show screen urm_x52_notification_overlay_probe
    pause 0.1
    $ print("X52_NOTIFICATION_SCREEN_BEFORE_ROLLBACK", len(urm_probe_urm.ProbeNotifications.notifications), renpy.get_screen("urm_x52_notification_overlay_probe") is not None)
    $ renpy.rollback(force=True, checkpoints=1, label="urm_x52_notification_screen_rollback_verify")


label urm_x52_notification_screen_rollback_verify:
    $ print("X52_NOTIFICATION_SCREEN_AFTER_ROLLBACK", len(urm_probe_urm.ProbeNotifications.notifications), renpy.get_screen("urm_x52_notification_overlay_probe") is not None)
    python:
        if len(urm_probe_urm.ProbeNotifications.notifications) != 0:
            raise Exception("Expected a visible notification action to keep the list reachable for rollback.")
    $ renpy.quit()


testcase urm_x52_displayed_notification_list_rollback:
    run Jump("urm_x52_notification_screen_rollback_start")


# clear() probe mirrors NotificationsClass.clear(): replace the owner's list
# attribute rather than mutating the existing RevertableList in place.
label urm_x52_notification_clear_rollback_start:
    $ renpy.game.context().rollback = True
    $ urm_probe_urm.ProbeNotifications.notifications = []
    $ urm_probe_urm.ProbeNotifications.add("Before clear", "clear_rollback_probe")
    show screen urm_x52_notification_overlay_probe
    pause 0.1
    $ renpy.checkpoint("before-x52-notification-clear")
    $ print("X52_NOTIFICATION_CLEAR_BEFORE", len(urm_probe_urm.ProbeNotifications.notifications), renpy.get_screen("urm_x52_notification_overlay_probe") is not None)
    $ urm_probe_urm.ProbeNotifications.clear()
    $ renpy.restart_interaction()
    $ renpy.rollback(force=True, checkpoints=1, label="urm_x52_notification_clear_rollback_verify")


label urm_x52_notification_clear_rollback_verify:
    $ print("X52_NOTIFICATION_CLEAR_AFTER_ROLLBACK", len(urm_probe_urm.ProbeNotifications.notifications), renpy.get_screen("urm_x52_notification_overlay_probe") is not None)
    python:
        # The reduced owner derives from the built-in object, like x52NonPicklable.
        # Its attribute replacement is not a RevertableObject mutation.
        if len(urm_probe_urm.ProbeNotifications.notifications) != 0:
            raise Exception("Expected clear() attribute replacement to remain empty after rollback in this reduced model.")
    $ renpy.quit()


testcase urm_x52_notification_clear_rollback:
    run Jump("urm_x52_notification_clear_rollback_start")


# remove() probe mutates the existing RevertableList in place, unlike clear().
label urm_x52_notification_remove_rollback_start:
    $ renpy.game.context().rollback = True
    $ urm_probe_urm.ProbeNotifications.notifications = []
    $ urm_probe_urm.ProbeNotifications.add("Before remove", "remove_rollback_probe")
    show screen urm_x52_notification_overlay_probe
    pause 0.1
    $ renpy.checkpoint("before-x52-notification-remove")
    $ print("X52_NOTIFICATION_REMOVE_BEFORE", len(urm_probe_urm.ProbeNotifications.notifications), renpy.get_screen("urm_x52_notification_overlay_probe") is not None)
    $ urm_probe_urm.ProbeNotifications.notifications.remove(urm_probe_urm.ProbeNotifications.notifications[0])
    $ renpy.restart_interaction()
    $ renpy.rollback(force=True, checkpoints=1, label="urm_x52_notification_remove_rollback_verify")


label urm_x52_notification_remove_rollback_verify:
    $ print("X52_NOTIFICATION_REMOVE_AFTER_ROLLBACK", len(urm_probe_urm.ProbeNotifications.notifications), renpy.get_screen("urm_x52_notification_overlay_probe") is not None)
    python:
        if len(urm_probe_urm.ProbeNotifications.notifications) != 1:
            raise Exception("Expected RevertableList.remove() mutation to be restored by rollback in the reduced model.")
    $ renpy.quit()


testcase urm_x52_notification_remove_rollback:
    run Jump("urm_x52_notification_remove_rollback_start")


# Timeout probe: the list mutation is performed inside invoke_in_thread.
default urm_x52_timeout_done = False

label urm_x52_notification_timeout_rollback_start:
    $ renpy.game.context().rollback = True
    $ urm_x52_timeout_done = False
    $ urm_probe_urm.ProbeNotifications.notifications = []
    $ urm_probe_urm.ProbeNotifications.add("Timed notification", "timeout_rollback_probe")
    show screen urm_x52_notification_overlay_probe
    pause 0.1
    $ renpy.checkpoint("before-x52-notification-timeout-remove")
    $ renpy.invoke_in_thread(urm_probe_urm.timeout_remove, urm_probe_urm.ProbeNotifications.notifications[0])
    python:
        import time
        deadline = time.time() + 5.0
        while not urm_x52_timeout_done and time.time() < deadline:
            time.sleep(0.05)
        if not urm_x52_timeout_done:
            raise Exception("Timeout worker did not complete within the probe deadline.")
    $ renpy.rollback(force=True, checkpoints=1, label="urm_x52_notification_timeout_rollback_verify")


label urm_x52_notification_timeout_rollback_verify:
    $ print("X52_NOTIFICATION_TIMEOUT_AFTER_ROLLBACK", len(urm_probe_urm.ProbeNotifications.notifications), urm_x52_timeout_done)
    python:
        if len(urm_probe_urm.ProbeNotifications.notifications) != 1:
            raise Exception("Expected the timeout-thread remove() to be restored by rollback in the reduced model.")
    $ renpy.quit()


testcase urm_x52_notification_timeout_rollback:
    run Jump("urm_x52_notification_timeout_rollback_start")


# Same-session save/load probe for the init-created notification owner.
# Save while the URM-shaped notification list is reachable through a visible
# action, mutate it after save, then load and report the restored graph.
label urm_x52_notification_save_load_start:
    if renpy.session.get("_urm_x52_notification_save_reentered", False):
        jump urm_x52_notification_save_load_verify

    $ renpy.game.context().rollback = True
    $ urm_probe_urm.ProbeNotifications.notifications = []
    $ urm_probe_urm.ProbeNotifications.add("Saved notification", "before-load")
    show screen urm_x52_notification_overlay_probe
    pause 0.1

    if renpy.can_load("urm-probe-x52-notification-roundtrip"):
        $ renpy.unlink_save("urm-probe-x52-notification-roundtrip")

    $ print("X52_NOTIFICATION_SAVE_BEFORE", type(urm_probe_urm.ProbeNotifications).__name__, type(urm_probe_urm.ProbeNotifications.notifications).__name__, [n.label for n in urm_probe_urm.ProbeNotifications.notifications])
    $ renpy.save("urm-probe-x52-notification-roundtrip")

    if renpy.session.get("_urm_x52_notification_save_reentered", False):
        jump urm_x52_notification_save_load_verify

    $ renpy.session["_urm_x52_notification_save_reentered"] = True
    $ urm_probe_urm.ProbeNotifications.clear()
    $ urm_probe_urm.ProbeNotifications.add("Post-save notification", "before-load")
    $ print("X52_NOTIFICATION_SAVE_MUTATED_AFTER", [n.label for n in urm_probe_urm.ProbeNotifications.notifications])
    $ renpy.load("urm-probe-x52-notification-roundtrip")

label urm_x52_notification_save_load_verify:
    python:
        owner = urm_probe_urm.ProbeNotifications
        notifications = getattr(owner, "notifications", None)
        if notifications is None:
            result_type = "missing"
            result_labels = []
        else:
            result_type = type(notifications).__name__
            result_labels = [getattr(n, "label", "<missing-label>") for n in notifications]
        print("X52_NOTIFICATION_SAVE_AFTER_LOAD", type(owner).__name__, result_type, result_labels, renpy.get_screen("urm_x52_notification_overlay_probe") is not None)
    $ renpy.quit()

testcase urm_x52_notification_save_load_roundtrip:
    $ renpy.session.pop("_urm_x52_notification_save_reentered", None)
    run Jump("urm_x52_notification_save_load_start")
