label changenicks:
    if dap.name.firstname != "Daphne":
        $ dap.nick = dap.name.firstname
    if eri.name.firstname != "Erika":
        $ eri.nick = eri.name.firstname
    if emm.name.firstname != "Emma":
        $ emm.nick = emm.name.firstname
    return
label c00Renames:
    if dap.name.firstname != "Daphne":
        $ dap.nick = dap.name.firstname
    else:
        $ dap.nick = "Daph"
    if emm.name.firstname != "Emma":
        $ emm.nick = emm.name.firstname
    else:
        $ emm.nick = "Emm"
    if eri.name.firstname != "Erika":
        $ eri.nick = eri.name.firstname
    else:
        $ eri.nick = "Eri"       
    return
