label lb_ep01_intro_tutorial_01:
    call screen scr_ep01_intro_tutorial_01

label lb_ep01_intro_tutorial_02:
    call screen scr_ep01_intro_tutorial_02

label lb_ep01_intro_tutorial_02a:
    call screen scr_ep01_intro_tutorial_02a

label lb_ep01_intro_tutorial_02aa:
    call screen scr_ep01_intro_tutorial_02aa

label lb_ep01_intro_tutorial_02aaa:
    call screen scr_ep01_intro_tutorial_02aaa

label lb_ep01_intro_tutorial_02aaaa:
    call screen scr_ep01_intro_tutorial_02aaaa

label lb_ep01_intro_tutorial_02aaaaa:
    call screen scr_ep01_intro_tutorial_02aaaaa

label lb_ep01_intro_tutorial_02b:
    call screen scr_ep01_intro_tutorial_02b

label lb_ep01_intro_tutorial_02bb:
    call screen scr_ep01_intro_tutorial_02bb

label lb_ep01_intro_tutorial_02c:
    call screen scr_ep01_intro_tutorial_02c

label lb_ep01_intro_tutorial_02cc:
    call screen scr_ep01_intro_tutorial_02cc

label lb_ep01_intro_tutorial_02ccc:
    call screen scr_ep01_intro_tutorial_02ccc

label lb_ep01_intro_tutorial_03:
    call screen scr_ep01_intro_tutorial_03

label lb_ep01_intro_tutorial_03a:
    call screen scr_ep01_intro_tutorial_03a

label lb_ep01_intro_tutorial_03b:
    call screen scr_ep01_intro_tutorial_03b

label lb_ep01_intro_tutorial_04:
    call screen scr_ep01_intro_tutorial_04

label lb_ep01_intro_tutorial_04a:
    call screen scr_ep01_intro_tutorial_04a

label lb_ep01_intro_tutorial_04b:
    call screen scr_ep01_intro_tutorial_04b

label lb_ep01_intro_tutorial_04c:
    call screen scr_ep01_intro_tutorial_04c

label lb_ep01_intro_tutorial_05:
    call screen scr_ep01_intro_tutorial_05

label lb_ep01_intro_tutorial_05a:
    call screen scr_ep01_intro_tutorial_05a

label lb_ep01_intro_tutorial_05b:
    call screen scr_ep01_intro_tutorial_05b

label lb_ep01_intro_tutorial_05c:
    call screen scr_ep01_intro_tutorial_05c

label lb_ep01_intro_tutorial_05d:
    call screen scr_ep01_intro_tutorial_05d

label lb_ep01_intro_tutorial_05e:
    call screen scr_ep01_intro_tutorial_05e

label lb_ep01_intro_tutorial_05f:
    call screen scr_ep01_intro_tutorial_05f

label lb_ep01_intro_tutorial_06:
    call screen scr_ep01_intro_tutorial_06

label lb_ep01_intro_tutorial_06a:
    call screen scr_ep01_intro_tutorial_06a

label lb_ep01_intro_tutorial_07:
    call screen scr_ep01_intro_tutorial_07

label lb_ep01_intro_tutorial_07a:
    call screen scr_ep01_intro_tutorial_07a

label lb_ep01_intro_tutorial_08:
    call screen scr_ep01_intro_tutorial_08

label lb_ep01_intro_tutorial_08a:
    call screen scr_ep01_intro_tutorial_08a

label lb_ep01_intro_tutorial_08b:
    call screen scr_ep01_intro_tutorial_08b

label lb_ep01_intro_tutorial_08c:
    call screen scr_ep01_intro_tutorial_08c

label lb_ep01_intro_tutorial_08d:
    call screen scr_ep01_intro_tutorial_08d

label lb_ep01_intro_tutorial_08e:
    call screen scr_ep01_intro_tutorial_08e

label lb_ep01_intro_tutorial_09:
    show sc mansionoutside o158
    mc "And that's pretty much it!"
    stop music fadeout 1.0
    play ambient "sound effects/01/truck_interior_sound_effect.ogg" loop fadein 1.0
    jump lb_ep01_01_04_intro_continue


play music "sound effects/01/Airport Lounge.mp3" loop fadein 1.0
screen scr_ep01_intro_tutorial_01:
    modal True
    imagebutton idle "intro_tutorial_01" action [Hide("scr_ep01_intro_tutorial_01",dissolve),Jump("lb_ep01_intro_tutorial_02")]

    frame:
        yalign 0.6
        has vbox
        text "{size=40}Starting from left to right...{/size}" style "char_info_description"
        text "{size=40}This FIRST icon contains the various {u}Tasks{/u} you will be set during each episode.{/size}" style "char_info_description"

screen scr_ep01_intro_tutorial_02:
    modal True
    imagebutton idle "intro_tutorial_02" action [Hide("scr_ep01_intro_tutorial_02",dissolve),Jump("lb_ep01_intro_tutorial_02a")]

    frame:
        yalign 0.3
        has vbox
        text "{size=40}There will be different missions throughout the game that you will be expected to complete.{/size}" style "char_info_description"



screen scr_ep01_intro_tutorial_02a:
    modal True
    imagebutton idle "intro_tutorial_02a" action [Hide("scr_ep01_intro_tutorial_02a",dissolve),Jump("lb_ep01_intro_tutorial_02aa")]

    frame:
        yalign 0.5
        has vbox
        text "{size=40}New tasks will be listed on the left-side of this screen, under {u}Current Tasks{/u}.{/size}" style "char_info_description"
        text "{size=40}And when each task has been achieved, they will be checked off, and we will move on to the next task.{/size}" style "char_info_description"



screen scr_ep01_intro_tutorial_02aa:
    modal True
    imagebutton idle "intro_tutorial_02a" action [Hide("scr_ep01_intro_tutorial_02aa",dissolve),Jump("lb_ep01_intro_tutorial_02aaa")]

    frame:
        yalign 0.5
        has vbox
        text "{size=40}As you can see, the first task has been listed and checked off already as we just completed it.{/size}" style "char_info_description"
        text "{size=40}So, I guess some congratulations are in order!{/size}" style "char_info_description"


screen scr_ep01_intro_tutorial_02aaa:
    modal True
    imagebutton idle "intro_tutorial_02a" action [Hide("scr_ep01_intro_tutorial_02aaa",dissolve),Jump("lb_ep01_intro_tutorial_02aaaa")]

    frame:
        yalign 0.5
        has vbox
        text "{size=40}Also, you will be given a grading for how well you did with each task.{/size}" style "char_info_description"
        text "{size=40}Current tasks will require you to choose five (sometimes four) correct options during the game,{/size}" style "char_info_description"
        text "{size=40}if you want to be graded with an A+.{/size}" style "char_info_description"

screen scr_ep01_intro_tutorial_02aaaa:
    modal True
    imagebutton idle "intro_tutorial_02a" action [Hide("scr_ep01_intro_tutorial_02aaaa",dissolve),Jump("lb_ep01_intro_tutorial_02aaaaa")]

    frame:
        yalign 0.5
        has vbox
        text "{size=40}If you miss one of the options for a task, then you'll be given an A. {/size}" style "char_info_description"
        text "{size=40}If you miss two, you will get a B, and so on.{/size}" style "char_info_description"
        text "{size=40}In order to change your score so you get an A+ for every task in each update, you will need to go back and change one or more of your decisions that refer to the set task.{/size}" style "char_info_description"


screen scr_ep01_intro_tutorial_02aaaaa:
    modal True
    imagebutton idle "intro_tutorial_02a" action [Hide("scr_ep01_intro_tutorial_02aaaaa",dissolve),Jump("lb_ep01_intro_tutorial_02b")]

    frame:
        yalign 0.5
        has vbox
        text "{size=40}If you have the Walkthrough or In-Game Walkthrough, that will be a big help.{/size}" style "char_info_description"
        text "{size=40}Look for the words 'Task Point' if you have the In-Game Walkthrough on when the options come up.{/size}" style "char_info_description"
        text "{size=40}An on-screen notification will pop up during your play through when a new Current Task is added.{/size}" style "char_info_description"



screen scr_ep01_intro_tutorial_02b:
    modal True
    imagebutton idle "intro_tutorial_02b" action [Hide("scr_ep01_intro_tutorial_02b",dissolve),Jump("lb_ep01_intro_tutorial_02bb")]

    frame:
        yalign 0.5
        has vbox
        text "{size=40}At the top-right of this screen, you will see a {u}People of Interest{/u} section.{/size}" style "char_info_description"


screen scr_ep01_intro_tutorial_02bb:
    modal True
    imagebutton idle "intro_tutorial_02b" action [Hide("scr_ep01_intro_tutorial_02bb",dissolve),Jump("lb_ep01_intro_tutorial_02c")]

    frame:
        yalign 0.5
        has vbox
        text "{size=40}Each time you meet a new character in the story, or someone who could be a potential{/size}" style "char_info_description"
        text "{size=40}problem for you in the future, they will be listed here.{/size}" style "char_info_description"
        text "{size=40}There will be an on-screen notification during your play through when a new person of interest{/size}" style "char_info_description"
        text "{size=40}has been added.{/size}" style "char_info_description"

screen scr_ep01_intro_tutorial_02c:
    modal True
    imagebutton idle "intro_tutorial_02c" action [Hide("scr_ep01_intro_tutorial_02c",dissolve),Jump("lb_ep01_intro_tutorial_02cc")]

    frame:
        yalign 0.5
        has vbox
        text "{size=40}The last section is for {u}Future Tasks{/u}.{/size}" style "char_info_description"


screen scr_ep01_intro_tutorial_02cc:
    modal True
    imagebutton idle "intro_tutorial_02c" action [Hide("scr_ep01_intro_tutorial_02cc",dissolve),Jump("lb_ep01_intro_tutorial_02ccc")]

    frame:
        yalign 0.3
        has vbox
        text "{size=40}An on-screen notification will let you know when they have been added here during each update.{/size}" style "char_info_description"
        text "{size=40}You will be required to finish these tasks in future episodes of the story.{/size}" style "char_info_description"


screen scr_ep01_intro_tutorial_02ccc:
    modal True
    imagebutton idle "intro_tutorial_02c" action [Hide("scr_ep01_intro_tutorial_02ccc",dissolve),Jump("lb_ep01_intro_tutorial_03")]

    frame:
        yalign 0.3
        has vbox
        text "{size=40}Right now you might be thinking, {i}What if I don't complete a task?{/i}{/size}" style "char_info_description"
        text "{size=40}Well, you don't want to know. So let's not allow that to happen, okay?{/size}" style "char_info_description"

screen scr_ep01_intro_tutorial_03:
    modal True
    imagebutton idle "intro_tutorial_03" action [Hide("scr_ep01_intro_tutorial_03",dissolve),Jump("lb_ep01_intro_tutorial_03a")]

    frame:
        yalign 0.6
        has vbox
        text "{size=40}The SECOND icon is all about your {u}Contacts{/u} info...{/size}" style "char_info_description"


screen scr_ep01_intro_tutorial_03a:
    modal True
    imagebutton idle "intro_tutorial_03a" action [Hide("scr_ep01_intro_tutorial_03a",dissolve),Jump("lb_ep01_intro_tutorial_03b")]

    frame:
        yalign 0.6
        has vbox
        text "{size=40}It contains the biography and details for all the main characters in the story.{/size}" style "char_info_description"

screen scr_ep01_intro_tutorial_03b:
    modal True
    imagebutton idle "intro_tutorial_03b" action [Hide("scr_ep01_intro_tutorial_03b",dissolve),Jump("lb_ep01_intro_tutorial_04")]

    frame:
        yalign 0.6
        has vbox
        text "{size=40}If you click on {u}Redefine Relationships{/u}, you can change your relationship to the other main characters.{/size}" style "char_info_description"
        text "{size=40}You can also change your name as well as the other main characters names.{/size}" style "char_info_description"

screen scr_ep01_intro_tutorial_04:
    modal True
    imagebutton idle "intro_tutorial_04" action [Hide("scr_ep01_intro_tutorial_04",dissolve),Jump("lb_ep01_intro_tutorial_04a")]

    frame:
        yalign 0.6
        has vbox
        text "{size=40}The THIRD icon contains the various {u}Relationship{/u} stats and it keeps track of the progress that you have made with all the main love interests in the story.{/size}" style "char_info_description"


screen scr_ep01_intro_tutorial_04a:
    modal True
    imagebutton idle "intro_tutorial_04a" action [Hide("scr_ep01_intro_tutorial_04a",dissolve),Jump("lb_ep01_intro_tutorial_04b")]

    frame:
        yalign 0.8
        has vbox
        text "{size=40}The more hearts that you gain, the better your chances of strengthening your relationship with someone, or...{/size}" style "char_info_description"


screen scr_ep01_intro_tutorial_04b:
    modal True
    imagebutton idle "intro_tutorial_04a" action [Hide("scr_ep01_intro_tutorial_04b",dissolve),Jump("lb_ep01_intro_tutorial_04c")]

    frame:
        yalign 0.8
        has vbox
        text "{size=40}...getting some very {i}'special treatment'{/i} from one or more of these fine ladies.{/size}" style "char_info_description"


screen scr_ep01_intro_tutorial_04c:
    modal True
    imagebutton idle "intro_tutorial_04a" action [Hide("scr_ep01_intro_tutorial_04c",dissolve),Jump("lb_ep01_intro_tutorial_05")]

    frame:
        yalign 0.8
        has vbox
        text "{size=40}Check out the 'Sexual Progress' tab every so often to see what I mean!{/size}" style "char_info_description"




screen scr_ep01_intro_tutorial_05:
    modal True
    imagebutton idle "intro_tutorial_05" action [Hide("scr_ep01_intro_tutorial_05",dissolve),Jump("lb_ep01_intro_tutorial_05a")]

    frame:
        yalign 0.8
        has vbox
        text "{size=40}The FOURTH icon is what we call {u}The Vault{/u}.{/size}" style "char_info_description"


screen scr_ep01_intro_tutorial_05a:
    modal True
    imagebutton idle "intro_tutorial_05a" action [Hide("scr_ep01_intro_tutorial_05a",dissolve),Jump("lb_ep01_intro_tutorial_05b")]

    frame:
        yalign 0.5
        has vbox
        text "{size=40}This is basically a \"Cheats\" section.{/size}" style "char_info_description"


screen scr_ep01_intro_tutorial_05b:
    modal True
    imagebutton idle "intro_tutorial_05a" action [Hide("scr_ep01_intro_tutorial_05b",dissolve),Jump("lb_ep01_intro_tutorial_05c")]

    frame:
        yalign 0.8
        has vbox
        text "{size=40}In this section, various MrDots Games tier members will be given a number code{/size}" style "char_info_description"
        text "{size=40}to unlock various extras in the game.{/size}" style "char_info_description"



screen scr_ep01_intro_tutorial_05c:
    modal True
    imagebutton idle "intro_tutorial_05a" action [Hide("scr_ep01_intro_tutorial_05c",dissolve),Jump("lb_ep01_intro_tutorial_05d")]

    frame:
        yalign 0.8
        has vbox
        text "{size=40}For $10+ tier members, you will have access to any Secret or Hidden Scenes in each update.{/size}" style "char_info_description"



screen scr_ep01_intro_tutorial_05d:
    modal True
    imagebutton idle "intro_tutorial_05a" action [Hide("scr_ep01_intro_tutorial_05d",dissolve),Jump("lb_ep01_intro_tutorial_05e")]

    frame:
        yalign 0.8
        has vbox
        text "{size=40}The next tier up will unlock the In-Game Walkthrough ($15).{/size}" style "char_info_description"
        text "{size=40}And the highest tier ($20+) will unlock all the Sex Animations, Rolling Images{/size}" style "char_info_description"
        text "{size=40}and the Extra Lewd Images in the {u}Achievements{/u} section.{/size}" style "char_info_description"


screen scr_ep01_intro_tutorial_05e:
    modal True
    imagebutton idle "intro_tutorial_05a" action [Hide("scr_ep01_intro_tutorial_05e",dissolve),Jump("lb_ep01_intro_tutorial_05f")]

    frame:
        yalign 0.5
        has vbox
        text "{size=40}Higher tiers will automatically unlock the lower ones...{/size}" style "char_info_description"
        text "{size=40}i.e. If you are on the $20 tier, you will get the{/size}" style "char_info_description"
        text "{size=40}In-Game Walkthrough and game Cheats.{/size}" style "char_info_description"

screen scr_ep01_intro_tutorial_05f:
    modal True
    imagebutton idle "intro_tutorial_05a" action [Hide("scr_ep01_intro_tutorial_05f",dissolve),Jump("lb_ep01_intro_tutorial_06")]

    frame:
        yalign 0.5
        has vbox
        text "{size=40}These will be available for those of you on the higher tiers.{/size}" style "char_info_description"


screen scr_ep01_intro_tutorial_06:
    modal True
    imagebutton idle "intro_tutorial_06" action [Hide("scr_ep01_intro_tutorial_06",dissolve),Jump("lb_ep01_intro_tutorial_06a")]

    frame:
        yalign 0.5
        has vbox
        text "{size=40}The FIFTH icon is the {u}Achievements{/u} section.{/size}" style "char_info_description"

screen scr_ep01_intro_tutorial_06a:
    modal True
    imagebutton idle "intro_tutorial_06a" action [Hide("scr_ep01_intro_tutorial_06a",dissolve),Jump("lb_ep01_intro_tutorial_07")]

    frame:
        yalign 0.5
        has vbox
        text "{size=40}You'll find all the Bonus Images of each love interest{/size}" style "char_info_description"
        text "{size=40}that we have hidden across each episode of the story.{/size}" style "char_info_description"
        text "{size=40}It will tell you exactly how many there are to find and each image {/size}" style "char_info_description"
        text "{size=40}will be unveiled in this gallery once you've located them.{/size}" style "char_info_description"


screen scr_ep01_intro_tutorial_07:
    modal True
    imagebutton idle "intro_tutorial_07" action [Hide("scr_ep01_intro_tutorial_07",dissolve),Jump("lb_ep01_intro_tutorial_07a")]

    frame:
        yalign 0.5
        has vbox
        text "{size=40}The SIXTH icon is the {u}Replay and Fantasy Scenes Gallery{/u}.{/size}" style "char_info_description"



screen scr_ep01_intro_tutorial_07a:
    modal True
    imagebutton idle "intro_tutorial_07a" action [Hide("scr_ep01_intro_tutorial_07a",dissolve),Jump("lb_ep01_intro_tutorial_08")]

    frame:
        yalign 0.5
        has vbox
        text "{size=40}When you find any of the 'HOT' or 'FANTASY' scenes during each update,{/size}" style "char_info_description"
        text "{size=40}they will automatically be stored in this section.{/size}" style "char_info_description"
        text "{size=40}This will allow you to view these scenes again and again!{/size}" style "char_info_description"


screen scr_ep01_intro_tutorial_08:
    modal True
    imagebutton idle "intro_tutorial_08" action [Hide("scr_ep01_intro_tutorial_08",dissolve),Jump("lb_ep01_intro_tutorial_08a")]

    frame:
        yalign 0.5
        has vbox
        text "{size=40}And the LAST icon is for the {u}Wallpaper{/u} images that you can select as your {/size}" style "char_info_description"
        text "{size=40}background image while you're in this menu screen, including the one you can see here.{/size}" style "char_info_description"

screen scr_ep01_intro_tutorial_08a:
    modal True
    imagebutton idle "intro_tutorial_08a" action [Hide("scr_ep01_intro_tutorial_08a",dissolve),Jump("lb_ep01_intro_tutorial_08b")]

    frame:
        yalign 0.5
        has vbox
        text "{size=40}We've already added in some wonderful renders that you can choose from.{/size}" style "char_info_description"

screen scr_ep01_intro_tutorial_08b:
    modal True
    imagebutton idle "intro_tutorial_08b" action [Hide("scr_ep01_intro_tutorial_08b",dissolve),Jump("lb_ep01_intro_tutorial_08c")]

    frame:
        yalign 0.5
        has vbox
        text "{size=40}We will be adding more images with each game update.{/size}" style "char_info_description"

screen scr_ep01_intro_tutorial_08c:
    modal True
    imagebutton idle "intro_tutorial_08b" action [Hide("scr_ep01_intro_tutorial_08c",dissolve),Jump("lb_ep01_intro_tutorial_08d")]

    frame:
        yalign 0.5
        has vbox
        text "{size=40}You can even change the color gradient at the bottom of the screen.{/size}" style "char_info_description"


screen scr_ep01_intro_tutorial_08d:
    modal True
    imagebutton idle "intro_tutorial_08c" action [Hide("scr_ep01_intro_tutorial_08d",dissolve),Jump("lb_ep01_intro_tutorial_09")]

    frame:
        yalign 0.5
        has vbox
        text "{size=40}Like so.{/size}" style "char_info_description"


screen scr_ep01_intro_tutorial_08e:
    modal True
    imagebutton idle "intro_tutorial_08c" action [Hide("scr_ep01_intro_tutorial_08e",dissolve),Jump("lb_ep01_intro_tutorial_09")]

    frame:
        yalign 0.5
        has vbox
        text "{size=40}And that's pretty much it!{/size}" style "char_info_description"
stop music fadeout 1.0
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
