init +100 python:
    def _hasPatch ():
        patchFiles = [ "family", "patch", "patched" ]
        patchFileExtensions = [ "", "rpy", "rpyc", "txt" ]
        for patchFile in patchFiles:
            for patchFileExtension in patchFileExtensions:
                if patchFileExtension != "":
                    patchFileExtension = "." + patchFileExtension
                for prefix in [ "", "_" ]:
                    if renpy.loadable (prefix + patchFile + patchFileExtension):
                        return True
        return False
    hasPatch = _hasPatch ()
    if not hasPatch:
        persistent.family = False