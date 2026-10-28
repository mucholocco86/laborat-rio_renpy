init -97 python:

    def varvar (characterProfile, characterField, characterValue):
        characterProfile._var (characterField, characterValue)

    def varvarget (characterProfile, characterField):
        return characterProfile._var (characterField)

    def varfunc (characterProfile, characterFunc, characterValue):
        getattr (characterProfile, characterFunc)(characterValue)

    class MyDorm:

        availableModules = []
        modules = [ "MyDormDecisions", "MyDormFamily" ]

        def __init__ (self):
            for myDormModule in self.modules:
                self.registerModule (myDormModule)

        def isAvailable (self, moduleName):
            if isinstance (moduleName, str):
                return moduleName in self.availableModules
            return False

        def registerModule (self, myDormModule):
            moduleTest = myDormModule + "Module"
            if moduleTest in globals ():
                if globals ()[moduleTest]:
                    self.availableModules.append (myDormModule)
                return True
            return False

        def toggleFamily (self):
            if "bet" in globals ():
                global bet, dap, emm, eri, mar, mc, mee, nor
                if persistent.family:
                    ### delete proxy roles
                    bet.roles.delete (_("la \"tía abuela\" de [dap], [emm], [eri] y [mc]"))

                    dap.roles.delete (_("la \"prima\" de [emm] y [mc]"))
                    dap.roles.delete (_("la \"hermana\" de [eri]"))
                    dap.roles.delete (_("la \"hija\" de [nor]"))
                    dap.roles.delete (_("la \"nieta\" de [mee]"))
                    dap.roles.delete (_("la \"gran sobrina\" de [bet]"))
                    dap._var ("traits, physical", dap._var ("traits, physical").replace (",clon", ""), intention = "set")
                    #dap._var ("traits, physical", _("clon"), "del", list)

                    emm.roles.delete (_("la \"hermana\" de [mc]"))
                    emm.roles.delete (_("la \"prima\" de [dap] y [eri]"))
                    emm.roles.delete (_("la \"hija\" de [mar]"))
                    emm.roles.delete (_("la \"nieta\" de [mee]"))
                    emm.roles.delete (_("la \"gran sobrina\" de [bet]"))
                    emm._var ("traits, physical", emm._var ("traits, physical").replace (",clon", ""), intention = "set")
                    #emm._var ("traits, physical", _("clon"), "del", list)

                    eri.roles.delete (_("la \"prima\" de [emm] y [mc]"))
                    eri.roles.delete (_("la \"hermana\" de [dap]"))
                    eri.roles.delete (_("la \"hija\" de [nor]"))
                    eri.roles.delete (_("la \"nieta\" de [mee]"))
                    eri.roles.delete (_("la \"gran sobrina\" de [bet]"))
                    eri._var ("traits, physical", eri._var ("traits, physical").replace (",clon", ""), intention = "set")
                    #eri._var ("traits, physical", _("clon"), "del", list)

                    mar.roles.delete (_("la \"madre\" de [emm] y [mc]"))
                    mar.roles.delete (_("la \"tía\" de [dap] y [eri]"))

                    mee.roles.delete (_("la \"abuela\" de [dap], [emm], [eri] y [mc]"))

                    nor.roles.delete (_("la \"tía\" de [emm] y [mc]"))
                    nor.roles.delete (_("la \"madre\" de [dap] y [eri]"))
                    
                    ### add regular roles

                    bet.roles.addRole (_("la tía abuela de [dap], [emm], [eri] y [mc]"))

                    dap.roles.addRole (_("la prima de [emm] y [mc]"), True)
                    dap.roles.addRole (_("la hermana de [eri]"))
                    dap.roles.addRole (_("la hija de [nor]"))
                    dap.roles.addRole (_("la nieta de [mee]"))
                    dap.roles.addRole (_("la gran sobrina de [bet]"))

                    emm.roles.addRole (_("la hermana de [mc]"), True)
                    emm.roles.addRole (_("la prima de [dap] y [eri]"))
                    emm.roles.addRole (_("la hija de [mar]"))
                    emm.roles.addRole (_("la nieta de [mee]"))
                    emm.roles.addRole (_("la gran sobrina de [bet]"))

                    eri.roles.addRole (_("la prima de [emm] y [mc]"), True)
                    eri.roles.addRole (_("la hermana de [dap]"))
                    eri.roles.addRole (_("la hija de [nor]"))
                    eri.roles.addRole (_("la nieta de [mee]"))
                    eri.roles.addRole (_("la gran sobrina de [bet]"))

                    mar.roles.addRole (_("la madre de [emm] y [mc]"), True)
                    mar.roles.addRole (_("la tía de [dap] y [eri]"))

                    mee.roles.addRole (_("la abuela de [dap], [emm], [eri] y [mc]"))

                    nor.roles.addRole (_("la tía de [emm] y [mc]"), True)
                    nor.roles.addRole (_("la madre de [dap] y [eri]"))

                    mar.name.mcSName = _("Mamá")
                    nor.rel = _("Tía ")
                    nor.relmc = _("tu sobrino")
                else:
                    ### delete proxy roles
                    bet.roles.delete (_("la tía abuela de [dap], [emm], [eri] y [mc]"))

                    dap.roles.delete (_("la prima de [emm] y [mc]"))
                    dap.roles.delete (_("la hermana de [eri]"))
                    dap.roles.delete (_("la hija de [nor]"))
                    dap.roles.delete (_("la nieta de [mee]"))
                    dap.roles.delete (_("la gran sobrina de [bet]"))

                    emm.roles.delete (_("la hermana de [mc]"))
                    emm.roles.delete (_("la prima de [dap] y [eri]"))
                    emm.roles.delete (_("la hija de [mar]"))
                    emm.roles.delete (_("la nieta de [mee]"))
                    emm.roles.delete (_("la gran sobrina de [bet]"))

                    eri.roles.delete (_("la prima de [emm] y [mc]"))
                    eri.roles.delete (_("la hermana de [dap]"))
                    eri.roles.delete (_("la hija de [nor]"))
                    eri.roles.delete (_("la nieta de [mee]"))
                    eri.roles.delete (_("la gran sobrina de [bet]"))

                    mar.roles.delete (_("la madre de [emm] y [mc]"))
                    mar.roles.delete (_("la tía de [dap] y [eri]"))

                    mee.roles.delete (_("la abuela de [dap], [emm], [eri] y [mc]"))

                    nor.roles.delete (_("la tía de [emm] y [mc]"))
                    nor.roles.delete (_("la madre de [dap] y [eri]"))

                    ### add regular roles

                    bet.roles.addRole (_("la \"tía abuela\" de [dap], [emm], [eri] y [mc]"))

                    dap.roles.addRole (_("la \"prima\" de [emm] y [mc]"), True)
                    dap.roles.addRole (_("la \"hermana\" de [eri]"))
                    dap.roles.addRole (_("la \"hija\" de [nor]"))
                    dap.roles.addRole (_("la \"nieta\" de [mee]"))
                    dap.roles.addRole (_("la \"gran sobrina\" de [bet]"))
                    dap._var ("traits, physical", dap._var ("traits, physical") + "," + _("clon"), intention = "set")

                    emm.roles.addRole (_("la \"hermana\" de [mc]"), True)
                    emm.roles.addRole (_("la \"prima\" de [dap] y [eri]"))
                    emm.roles.addRole (_("la \"hija\" de [mar]"))
                    emm.roles.addRole (_("la \"nieta\" de [mee]"))
                    emm.roles.addRole (_("la \"gran sobrina\" de [bet]"))
                    emm._var ("traits, physical", emm._var ("traits, physical") + "," + _("clon"), intention = "set")
                    # emm._var ("traits, physical", _("clon"), "add", list) #   this does some BS

                    eri.roles.addRole (_("la \"prima\" de [emm] y [mc]"), True)
                    eri.roles.addRole (_("la \"hermana\" de [dap]"))
                    eri.roles.addRole (_("la \"hija\" de [nor]"))
                    eri.roles.addRole (_("la \"nieta\" de [mee]"))
                    eri.roles.addRole (_("la \"gran sobrina\" de [bet]"))
                    eri._var ("traits, physical", eri._var ("traits, physical") + "," + _("clon"), intention = "set")
                    # eri._var ("traits, physical", _("clon"), "add", list) #   this does some BS

                    mar.roles.addRole (_("la \"madre\" de [emm] y [mc]"), True)
                    mar.roles.addRole (_("la \"tía\" de [dap] y [eri]"))

                    mee.roles.addRole (_("la \"abuela\" de [dap], [emm], [eri] y [mc]"))

                    nor.roles.addRole (_("la \"tía\" de [emm] y [mc]"), True)
                    nor.roles.addRole (_("la \"madre\" de [dap] y [eri]"))

                    mar.name.mcSName = str (mar.name)
                    nor.rel = ""
                    nor.relmc = _("prácticamente tu sobrino")