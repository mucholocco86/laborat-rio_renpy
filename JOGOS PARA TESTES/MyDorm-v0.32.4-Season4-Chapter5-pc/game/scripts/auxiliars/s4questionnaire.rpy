label s3q:
    scene c13s000_lesbian with dissolve
    jam "Vamos con las preguntas sobre tus elecciones en la tercera temporada."
    if emm._var("route"):
        scene c07s011_435a with dissolve
        call mrS3_emm_hadAnal from _call_mrS3_emm_hadAnal_3
    scene c28s005_360a with dissolve
    call mrS3_ama_route from _call_mrS3_ama_route_11
    scene c02s004_010 with dissolve:
        yalign 1.0
        linear 5.0 yalign 0.0
    if nor._var("route"):
        call mrS3_nor_nick from _call_mrS3_nor_nick_1
    scene c28s004_625a
    call mrS3_eva_route from _call_mrS3_eva_route_14
    if eva._var("route"):
        call mrS3_eva_choking from _call_mrS3_eva_choking_1
        call mrS3_eva_pregnant from _call_mrS3_eva_pregnant_1
        if eva._var("pregnant"):
            $ eva._var("undiscoveredPregnancy", True)
    scene c09s013_275 with dissolve
    call mrS3_lis_route from _call_mrS3_lis_route_12
    scene c23s002_350e with dissolve
    call mrS3_pat_name from _call_mrS3_pat_name
    scene c02s008_099a with dissolve
    if mar._var("route"):
        call mrS3_mar_anal from _call_mrS3_mar_anal
        if mar._var("anal"):
            call mrS3_mar_rimjob from _call_mrS3_mar_rimjob
    scene c23s007_190a with dissolve
    call mrS3_bet_route from _call_mrS3_bet_route_7
    if bet._var("route"):
        call mrS3_bet_pregnant from _call_mrS3_bet_pregnant_1
        if bet._var("pregnant"):
            $ bet._var("undiscoveredPregnancy", True)
    scene c24s003_115a with dissolve
    if kia._var("route"):
        call mrS3_kia_pregnant from _call_mrS3_kia_pregnant_1
        if kia._var("pregnant"):
            $ kia._var("undiscoveredPregnancy", True)
        call mrS3_kia_watersports from _call_mrS3_kia_watersports
    scene c09s013_205 with dissolve
    call mrS3_kim_route from _call_mrS3_kim_route_4
    scene c02s013_030c with dissolve
    if meg._var("route"):
        call mrS3_meg_anal from _call_mrS3_meg_anal
    scene c09s010_575b
    if deb._var("route"):
        call mrS3_deb_pregnant from _call_mrS3_deb_pregnant_1
        if deb._var("pregnant"):
            $ deb._var("undiscoveredPregnancy", True)
    scene c09s015_020 with dissolve
    if mad._var("route"):
        call mrS3_mad_fart from _call_mrS3_mad_fart
    return
label mrS3_pat_name:
    menu qCharlotteName:
        "¿Miraste la foto del expediente de la chica nueva?"
        "Sí.":
            $ pat.name.first_name = renpy.input (_("¿Qué nombre pone en el borrón de tinta?"), default = "Charlotte")
            $ pat.nick = renpy.input (_("El apodo también está emborronado ¿Qué crees que pone?"), default = "Charlie")
            $ persistent.patName = pat.name.first_name
            $ persistent.patNick = pat.nick
            $ mc._var("lookedCharlotte", True)
        "No.":
            $ mc._var("lookedCharlotte", False)
            $ persistent.patName = "Charlotte"
            $ persistent.patNick = "Charlie"
    return
label mrS3_pat_file:
    menu qCharlotteFile:
        "¿Miraste la foto del expediente de la chica nueva?"
        "Sí.":
            $ mc._var("lookedCharlotte", True)
        "No.":
            $ mc._var("lookedCharlotte", False)
    return
label mrS3_mar_anal:
    menu qMarAnal:
        "¿Tuviste sexo anal con [mar]?"
        "Sí.":
            $ mar._var("anal", True)
        "No.":
            $ mar._var("anal", False)
    return
label mrS3_mar_rimjob:
    menu qMarRimjob:
        "¿Le comiste el culo a [mar]?"
        "Sí.":
            $ mar._var("rimjob", True)
        "No.":
            $ mar._var("rimjob", False)
    return
label mrS3_kia_watersports:
    menu qKiaWatersports:
        "¿Activaste el fetiche de orina con [kia]?"
        "Sí.":
            $ kia._var("urination", True)
        "No.":
            $ kia._var("urination", False)
    return
label mrS3_meg_anal:
    menu qMegAnal:
        "¿Tuviste sexo anal con [meg]?"
        "Sí.":
            $ meg._var("anal", True)
        "No.":
            $ meg._var("anal", False)
    return
label mrS3_mee_icecream:
    menu:
        "¿Qué dijiste sobre el helado hecho con leche materna de [mee]?"
        "Me encantaría probarlo." (wt = wt1):
            $ mee._var("iceCream", True)
        "No es que lo vaya a probar, pero me parece bien." (wt = wt2):
            $ mee._var("iceCream", False)
    return
label mrS3_kat_waffle:
    menu:
        "¿Le diste un trozo de gofre a [kat] durante vuestra no-cita?"
        "Sí.":
            $ kat.rp (30)
            $ kat._var("waffle" , True)
        "No.":
            $ kat._var("waffle" , False)
    return
label mrS3_Daniels:
    $ wt1 = _("[mc] decidirá el destino de Daniels.")
    $ wt2 = _("[ama], [eva], y Aaron decidirán el destino de Daniels")
    menu:
        "¿Qué le dijiste a Aaron sobre el destino de Daniels, el antiguo jefe de NTR?"
        "También atacó a mi familia." (wt=wt1):
            $ mc._var("Daniels", True)
        "Lo considero lógico." (wt=wt2):
            $ mc._var("Daniels", False)
    return
label mrS3_mad_fart:
    menu:
        "¿Te tiraste un pedo en el baño de [mad.nick]?"
        "Sí.":
            $ mad._var("fart", True)
        "No.":
            $ mad._var("fart", False)
    return
