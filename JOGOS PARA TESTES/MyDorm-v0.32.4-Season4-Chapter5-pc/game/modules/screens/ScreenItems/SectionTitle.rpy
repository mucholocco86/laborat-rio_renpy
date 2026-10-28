screen SectionTitle(labelText, vpgridCols = 3, start = 1, editable = False):
    hbox:
        label labelText style "SectionTitle"
        if isinstance (editable, TGCharacter) and editable in [ mar, emm, nor, dap, eri ]:
            button:
                action [ ShowMenu ("ProfilesEditCharacterName", editable) ]
                text "\u270F":
                    at renameTransform
                    color "#ffffff"
                    hover_color "#6b8ba0"
                    size int (TextLargeFontSize * 2)
    for index in range (start, vpgridCols):
        null