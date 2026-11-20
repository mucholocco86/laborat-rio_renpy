label endSeasonSix:
    scene blank with dissolve
    call screen save
    $ partSixFinished = 1
    $ renpy.force_autosave()
    show text "{size=200}SAVE NOW!{/size}" at truecenter
    "Moonbox" "SAVE NOW! The next update will come as a separate version to keep it under 5GB. Save now, you'll need this save to play part 7."
    "Moonbox" "You've reached the end of this update. Thanks for playing. Rollback to the \"Save now\" and save if you haven't. It's the only save that will work in part 7."
    "Moonbox" "Last chance."
    return
    