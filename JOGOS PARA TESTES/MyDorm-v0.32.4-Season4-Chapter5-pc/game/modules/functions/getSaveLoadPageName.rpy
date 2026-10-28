init python:
    def getSaveLoadPageName (page):
        global persistent
        if page in ("auto", "quick"):
            page = _("Guardado automático") if page == "auto" else _("Guardado rápido")
        elif page in ():
            page = "Import"
        else:
            page = _("Página de guardado") + " " + str (page)
        return page