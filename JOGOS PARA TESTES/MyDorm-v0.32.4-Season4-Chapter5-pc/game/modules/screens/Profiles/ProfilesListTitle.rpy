screen ProfilesListTitle(thisTitle, gridSize = 5, marginLeft = 0, marginTop = 0, marginRight = 0, marginBottom = 0, editable = False):
    modal True
    vpgrid style "MenuVPGrid":
        cols 1
        use SectionTitle (thisTitle, gridSize, editable = editable)
        margin (marginLeft * 2, marginRight * 2, marginRight * 2, marginRight * 2)
        pos (marginLeft, marginTop)
        xspacing MenuGridSpacing
        xysize (1.0 - marginLeft * 2, 1.0 - marginLeft * 4)
        yspacing MenuGridSpacing * 2