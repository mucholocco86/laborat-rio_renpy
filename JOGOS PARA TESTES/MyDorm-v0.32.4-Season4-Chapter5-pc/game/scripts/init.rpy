default importedSaveFromPart1 = False   # check for import is made in after_load
label part2:
    label start:
    if not importedSaveFromPart1:
        call startS3 from _call_startS3
        call questionnaire from _call_questionnaire
    else:
        call c21 from _call_c21
        call c22 from _call_c22
        call c23 from _call_c23
        call c24 from _call_c24
        call c25 from _call_c25
        call c26 from _call_c26
        call c27 from _call_c27
        #call patchImportFromPart1 from _call_patchImportFromPart1
    #call c13 from _call_c13
    #call c14 from _call_c14
    #call c15 from _call_c15
    #call c16 from _call_c16
    #call c17 from _call_c17
    #call c18 from _call_c18
    #call c19 from _call_c19

    #call c21 from _call_c21
    #call c22 from _call_c22
    #call c23 from _call_c23
    #call c24 from _call_c24
    #call c25 from _call_c25
    #call c26 from _call_c26
    #call c27 from _call_c27
    call c28 from _call_c28
    call c29 from _call_c29
    call c30 from _call_c30
    call c31 from _call_c31
    call c32 from _call_c32
    call c33 from _call_c33
    # add a call for the *next* version here, that works as the current "save here label"
    return

label startS4:
    call questionnaire from _call_questionnaire_1
    call c28 from _call_c28_1
    call c29 from _call_c29_1
    call c30 from _call_c30_1
    call c31 from _call_c31_1
    call c32 from _call_c32_1
    call c33 from _call_c33_1
