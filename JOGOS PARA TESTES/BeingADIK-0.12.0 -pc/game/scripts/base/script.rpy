label start:
scene black
jump season3_header_patch_label

label continue_season3_label:
$ renpy.block_rollback()
if persistent.episode_interlude:
    menu:
        "Do you want to play the Interlude?"
        "Play the Interlude":
            jump startInterlude
        "Skip to episode 9":
            scene epi_ems44 with dissolve
            menu:
                "Did Zoey calm Emma down or take her phone?"
                "Calmed her down":
                    $ emma_calm = True
                    $ emma_cluck = False
                    $ zoey_dik = False
                "Took her phone":
                    $ emma_calm = False
                    $ emma_cluck = True
                    $ zoey_dik = True
    if (nonPatreonConfig or steamConfig) and renpy.loadable("walkthrough/season3/walkthrough_season3.rpyc"):
        show screen keymap_screen_s3
    jump interlude_save_here_label
else:
    jump startInterlude
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
