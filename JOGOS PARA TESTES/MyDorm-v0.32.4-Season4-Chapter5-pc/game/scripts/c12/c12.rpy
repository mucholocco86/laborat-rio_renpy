label endOfPart1:
    $ importedSaveFromPart1 = True
    trop "Gracias por jugar My Dorm — Parte 1."
    jump part2

label endOfPart1_EN:
    $ importedSaveFromPart1 = True
    trop "Gracias por jugar My Dorm — Parte 1."
    jump part2

label endOfPart1_ES:
    $ importedSaveFromPart1 = True
    trop "Gracias por jugar My Dorm — Parte 1."
    jump part2

# clearing old labels to pass the return stack of part
#label c12:                  # label that added to the stack for last chapter of part 1
#    return
label _call_c12:
    return

label c12_EN:               # label that added to the stack for last chapter of part 1
    return
label _call_c12_EN:
    return

label c12_ES:               # label that added to the stack for last chapter of part 1
    return
label _call_c12_ES:
    return

label _call_endOfPart1:     # export label of part 1 that switches between EN/ES
    return

label _call_endOfPart1_EN:  # English save export label
    return

label _call_endOfPart1_ES:  # Spanish save export label
    return

# The following labels are probably don't need to be "cleared", but I add them just in case
label _call_c12Llam:            # label that added c12 to the stack
    return
label c12Llam:
    return
label _call_fin_juego:          # label used as end of version/content language switcher for c12
    return
label fin_juego:
    return
