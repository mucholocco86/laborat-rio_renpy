default qm_profiles_disabled = False

init 10 python:
    def getQuickMenuButtons ():
        quickMenuButtonList = {}
        if persistent.quickmenuButtonsRollBackFwd:
            quickMenuButtonList.update ({
                _("Atrás") : ("Back", [ Rollback () ]),
                _("Adelante") : ("Fwd", [ RollForward () ])
            })
        if persistent.quickmenuButtonsSkip:
            quickMenuButtonList.update ({
                _("Avance Auto.") : ("A.Fwd", [ Preference ("auto-forward", "toggle") ]),
                _("Saltar") : ("Skip", [ SelectedIf (Skip (fast = True, confirm = True)) ])
            })
        if persistent.quickmenuButtonsHistory:
            quickMenuButtonList.update ({ _("Historial") : ("History", [ ShowMenu ("History") ]) })
        if persistent.quickmenuButtonsQSaveQLoad:
            quickMenuButtonList.update ({ _("Grabar R.") : ("Q.Save", [ QuickSave () ]) })
        if persistent.quickmenuButtonsSaveLoad:
            quickMenuButtonList.update ({
                _("Grabar") : ("Game Save", [ ShowMenu ("GameSave") ]),
                _("Cargar") : ("Game Load", [ ShowMenu ("GameLoad") ])
            })
        if persistent.quickmenuButtonsQSaveQLoad:
            quickMenuButtonList.update ({ _("Cargar R.") : ("Q.Load", [ QuickLoad () ]) })
        quickMenuButtonList.update ({ 
            _("Config") : ("Settings", [ ]),   # leave empty, will be set in QuickMenu screen
        })
        if not qm_profiles_disabled:
            quickMenuButtonList.update ({ 
                _("Perfiles") : ("Profiles", [ ShowMenu ("Profiles") ])
            })
        if persistent.quickmenuButtonsQuit:
            quickMenuButtonList.update ({ _("Salir") : ("Quit", [ Quit (confirm = True) ]) })
        return quickMenuButtonList