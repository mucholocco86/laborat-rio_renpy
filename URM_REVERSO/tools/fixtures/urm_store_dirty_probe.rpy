# Isolated Ren'Py 7.4.11 probe for the nested dirty-flag behavior
# identified in converted URM classes/vars.rpy and classes/URMFiles.rpy.
# This is a reduced reproduction, not the original URM runtime.

init python:
    from collections import OrderedDict

    class DirtyProbeURMFileStore(OrderedDict):
        def __init__(self, data=None, unsaved=False):
            OrderedDict.__init__(self, data or {})
            self.unsaved = unsaved

        def __setitem__(self, key, value):
            OrderedDict.__setitem__(self, key, value)
            self.unsaved = True

        def __delitem__(self, key):
            if key in self:
                OrderedDict.__delitem__(self, key)
                self.unsaved = True

    class DirtyProbeVarsStore:
        def __init__(self, store, watched_store=None):
            self.store = store
            self.watched_store = watched_store if watched_store is not None else DirtyProbeURMFileStore()

        def has(self, name):
            return name in self.store

        def remember(self, name):
            self.store[name] = OrderedDict([("name", name)])

        def freeze(self, name):
            if not self.has(name):
                self.remember(name)
            self.store[name]["frozen"] = True

        def unfreeze(self, name):
            if self.has(name) and "frozen" in self.store[name]:
                del self.store[name]["frozen"]

        def monitor(self, name):
            if not self.has(name):
                self.remember(name)
            self.store[name]["monitor"] = True

        def unmonitor(self, name):
            if self.has(name) and "monitor" in self.store[name]:
                del self.store[name]["monitor"]

        def watch(self, name):
            self.watched_store[name] = OrderedDict([("name", name)])

        def ignore(self, name, when):
            if not self.has(name):
                self.remember(name)
            if "ignored" in self.store[name]:
                self.store[name]["ignored"].append(when)
            else:
                self.store[name]["ignored"] = [when]
            self.store.unsaved = True

        def unignore(self, name, when):
            if self.has(name) and "ignored" in self.store[name]:
                if when in self.store[name]["ignored"]:
                    self.store[name]["ignored"].remove(when)
                if not self.store[name]["ignored"]:
                    del self.store[name]["ignored"]
                self.store.unsaved = True


testcase urm_dirty_tracking_nested_metadata:
    $ urm_dirty_store = DirtyProbeURMFileStore({"affection": OrderedDict([("name", "Affinity")])}, unsaved=False)
    $ urm_dirty_watched_store = DirtyProbeURMFileStore(unsaved=False)
    $ urm_dirty_vars = DirtyProbeVarsStore(urm_dirty_store, urm_dirty_watched_store)

    $ urm_dirty_vars.freeze("affection")
    $ print("URM_DIRTY_PROBE_FREEZE_EXISTING", urm_dirty_store.unsaved, dict(urm_dirty_store["affection"]))
    assert not urm_dirty_store.unsaved

    $ urm_dirty_store.unsaved = False
    $ urm_dirty_vars.unfreeze("affection")
    $ print("URM_DIRTY_PROBE_UNFREEZE_EXISTING", urm_dirty_store.unsaved, dict(urm_dirty_store["affection"]))
    assert not urm_dirty_store.unsaved

    $ urm_dirty_store.unsaved = False
    $ urm_dirty_vars.monitor("affection")
    $ print("URM_DIRTY_PROBE_MONITOR_EXISTING", urm_dirty_store.unsaved, dict(urm_dirty_store["affection"]))
    assert not urm_dirty_store.unsaved

    $ urm_dirty_store.unsaved = False
    $ urm_dirty_vars.unmonitor("affection")
    $ print("URM_DIRTY_PROBE_UNMONITOR_EXISTING", urm_dirty_store.unsaved, dict(urm_dirty_store["affection"]))
    assert not urm_dirty_store.unsaved

    $ urm_dirty_store.unsaved = False
    $ urm_dirty_vars.watch("affection")
    $ print("URM_DIRTY_PROBE_WATCH_ROOT", urm_dirty_watched_store.unsaved)
    assert urm_dirty_watched_store.unsaved

    $ urm_dirty_store.unsaved = False
    $ urm_dirty_vars.ignore("affection", "path")
    $ print("URM_DIRTY_PROBE_IGNORE_EXPLICIT", urm_dirty_store.unsaved)
    assert urm_dirty_store.unsaved

    $ urm_dirty_store.unsaved = False
    $ urm_dirty_vars.unignore("affection", "path")
    $ print("URM_DIRTY_PROBE_UNIGNORE_EXPLICIT", urm_dirty_store.unsaved)
    assert urm_dirty_store.unsaved

    $ urm_dirty_store.unsaved = False
    $ urm_dirty_vars.freeze("new_variable")
    $ print("URM_DIRTY_PROBE_FREEZE_NEW", urm_dirty_store.unsaved, dict(urm_dirty_store["new_variable"]))
    assert urm_dirty_store.unsaved
    $ renpy.quit()
