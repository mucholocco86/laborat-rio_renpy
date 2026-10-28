label numberOfPregnanciesS3 (Emm, Eva, Mad, Ama, Kim, Kat, Deb, Lis, Bet, Kia):
    $ mc._var("numberOfPregnancies", 0, "set")
    if sai._var("pregnant"):
        $ mc._var("numberOfPregnancies", 1)
    if mar._var("pregnant"):
        $ mc._var("numberOfPregnancies", 1)
    if Emm:
        if emm._var("pregnant"):
            $ mc._var("numberOfPregnancies", 1)
    if eri._var("pregnant"):
        $ mc._var("numberOfPregnancies", 1)
    if nor._var("pregnant"):
        $ mc._var("numberOfPregnancies", 1)
    if sca._var("pregnant"):
        $ mc._var("numberOfPregnancies", 1)
    if eil._var("pregnant"):
        $ mc._var("numberOfPregnancies", 1)
    if sam._var("pregnant"):
        $ mc._var("numberOfPregnancies", 1)
    if sim._var("pregnant"):
        $ mc._var("numberOfPregnancies", 1)
    if oma._var("pregnant"):
        $ mc._var("numberOfPregnancies", 1)
    if Eva:
        if eva._var("pregnant"):
            $ mc._var("numberOfPregnancies", 1)
    if Mad:
        if mad._var("pregnant"):
            $ mc._var("numberOfPregnancies", 1)
    if meg._var("pregnant"):
        $ mc._var("numberOfPregnancies", 1)
    if Ama:
        if ama._var("pregnant"):
            $ mc._var("numberOfPregnancies", 1)
    if Kim:
        if kim._var("pregnant"):
            $ mc._var("numberOfPregnancies", 1)
    if Kat:
        if kat._var("pregnant"):
            $ mc._var("numberOfPregnancies", 1)
    if Deb:
        if deb._var("pregnant"):
            $ mc._var("numberOfPregnancies", 1)
    if Lis:
        if lis._var("pregnant"):
            $ mc._var("numberOfPregnancies", 1)
    if Bet:
        if bet._var("pregnant"):
            $ mc._var("numberOfPregnancies", 1)
    if Kia:
        if kia._var("pregnant"):
            $ mc._var("numberOfPregnancies", 1)
    return
label version28:
    $ vers = __("Version 0.28")
    if not vers == "Version 0.28":
        $ renpy.quit()
    return
