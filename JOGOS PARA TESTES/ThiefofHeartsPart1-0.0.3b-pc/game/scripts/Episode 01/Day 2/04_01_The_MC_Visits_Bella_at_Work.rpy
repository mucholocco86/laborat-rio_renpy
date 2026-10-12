init:
    $ v_ep01_04_01_Bella_Photo_Number = 1
    $ v_ep01_04_01_Bella_Photo_Talking_1 = False
    $ v_ep01_04_01_Bella_Photo_Talking_2 = False
    $ v_ep01_04_01_Bella_Photo_Talking_3 = False
    $ v_ep01_04_01_Bella_Photo_Talking_4 = False
    $ v_ep01_04_01_Bella_Photo_Talking_5 = False
    $ v_ep01_04_01_Bella_Photo_Talking_6 = False
    $ v_ep01_04_01_Bella_Photo_Talking_7 = False
    $ v_ep01_04_01_Bella_Work_Date = False
    $ v_ep01_04_01_Bella_Stay_Or_Leave = "Leave"

    image sc bella work visit butt wiggle1:
        "sc bellaworkvisit b021a" with Dissolve(0.2, alpha=True)
        pause 1.0
        "sc bellaworkvisit b021b" with Dissolve(0.2, alpha=True)
        pause 1.0
        repeat

    image sc bella work visit butt wiggle2:
        "sc bellaworkvisit b026a" with Dissolve(0.2, alpha=True)
        pause 1.0
        "sc bellaworkvisit b026b" with Dissolve(0.2, alpha=True)
        pause 1.0
        repeat

    image sc bella work visit police leaving1:
        "sc bellaworkvisit b048" with Dissolve(0.2, alpha=True)
        pause 1.0
        "sc bellaworkvisit b049" with Dissolve(0.2, alpha=True)
        pause 1.0
        "sc bellaworkvisit b050" with Dissolve(0.2, alpha=True)
        pause 1.0
        "sc bellaworkvisit b051" with Dissolve(0.2, alpha=True)
        pause 1.0
        "sc bellaworkvisit b052" with Dissolve(0.2, alpha=True)

    image sc bella work visit police leaving2:
        "sc bellaworkvisit b049" with Dissolve(0.2, alpha=True)
        pause 1.0
        "sc bellaworkvisit b050" with Dissolve(0.2, alpha=True)
        pause 1.0
        "sc bellaworkvisit b051" with Dissolve(0.2, alpha=True)
        pause 1.0
        "sc bellaworkvisit b052" with Dissolve(0.2, alpha=True)

    image sc bella phone1:
        "sc bellaworkvisit b109" with Dissolve(0.2, alpha=True)
        pause 1.0
        "sc bellaworkvisit b110" with Dissolve(0.2, alpha=True)

    image sc bella spider mc:
        "sc bellaworkvisit b097-mc1" with Dissolve(0.2, alpha=True)
        pause 0.5
        "sc bellaworkvisit b097-mc2" with Dissolve(0.2, alpha=True)
        pause 0.5
        repeat

init python:
    from datetime import datetime
    now = datetime.now()
    bw_h_hours = now.strftime("%H:%M")
    def acn_ep01_04_01_Bella_Work_change_hour():
        now = datetime.now()
        globals() ["bw_h_hours"] = now.strftime("%H:%M")
        renpy.restart_interaction()

screen scr_ep01_04_01_Bella_Phone_Horizontal:
    zorder -10 # These should look like part of the scene, so they should go under things like the music player if they overlap
    add "sc bellaworkvisit b128"
    timer 0.30 action acn_ep01_04_01_Bella_Work_change_hour repeat False
    text "[bw_h_hours]" xalign 0.125 yalign 0.2 outlines [ (absolute(2), "#000", absolute(0), absolute(0)) ]

    textbutton "LOCK PHONE":
        text_outlines [ (absolute(6), "#000", absolute(0), absolute(0)) ]
        xalign 0.5
        yalign 0.1
        focus_mask True
        action [Play("sound", "sound effects/01/phone_lock.mp3"),Hide("scr_ep01_04_01_Bella_Phone_Horizontal"),Jump("lb_ep01_04_01_Bella_Phone_Put_Down")]

    imagebutton:
        idle "gui/bella_phone_icons/Contacts.png" xalign 0.865 yalign 0.23 focus_mask True
        action [Hide("scr_ep01_04_01_Bella_Phone_Horizontal"),Jump("lb_ep01_04_01_Bella_Phone_Contacts")]

    imagebutton:
        idle "gui/bella_phone_icons/Browser.png" xalign 0.865 yalign 0.415 focus_mask True
        action [Hide("scr_ep01_04_01_Bella_Phone_Horizontal"),Jump("lb_ep01_04_01_Bella_Phone_Browser")]

    imagebutton:
        idle "gui/bella_phone_icons/Text.png" xalign 0.865 yalign 0.595 focus_mask True
        action [Hide("scr_ep01_04_01_Bella_Phone_Horizontal"),Jump("lb_ep01_04_01_Bella_Phone_Text")]

    imagebutton:
        idle "gui/bella_phone_icons/Phone.png" xalign 0.865 yalign 0.775 focus_mask True
        action [Jump("lb_ep01_04_01_Bella_Phone_Phone")]

    imagebutton:
        idle "gui/bella_phone_icons/Calculator.png" xalign 0.125 yalign 0.30 focus_mask True
        action [Jump("lb_ep01_04_01_Bella_Phone_Calculator")]

    imagebutton:
        idle "gui/bella_phone_icons/Calendar.png" xalign 0.225 yalign 0.30 focus_mask True
        action [Jump("lb_ep01_04_01_Bella_Phone_Calendar")]

    imagebutton:
        idle "gui/bella_phone_icons/Camera.png" xalign 0.325 yalign 0.30 focus_mask True
        action [Jump("lb_ep01_04_01_Bella_Phone_Camera")]

    imagebutton:
        idle "gui/bella_phone_icons/Mail.png" xalign 0.425 yalign 0.30 focus_mask True
        action [Jump("lb_ep01_04_01_Bella_Phone_Mail")]

    imagebutton:
        idle "gui/bella_phone_icons/Notes.png" xalign 0.525 yalign 0.30 focus_mask True
        action [Jump("lb_ep01_04_01_Bella_Phone_Notes")]

    imagebutton:
        idle "gui/bella_phone_icons/Photos.png" xalign 0.625 yalign 0.30 focus_mask True
        action [Jump("lb_ep01_04_01_Bella_Phone_Photos")]

    imagebutton:
        idle "gui/bella_phone_icons/Paint.png" xalign 0.725 yalign 0.30 focus_mask True
        action [Jump("lb_ep01_04_01_Bella_Phone_Paint")]

screen scr_ep01_04_01_Bella_Phone_Contacts:
    textbutton "HOME":
        text_outlines [ (absolute(6), "#000", absolute(0), absolute(0)) ]
        xalign 0.5
        yalign 0.1
        focus_mask True
        action [Hide("scr_ep01_04_01_Bella_Phone_Contacts"),Jump("lb_ep01_04_01_Bella_Phone_Start")]

screen scr_ep01_04_01_Bella_Phone_Browser:
    textbutton "HOME":
        text_outlines [ (absolute(6), "#000", absolute(0), absolute(0)) ]
        xalign 0.5
        yalign 0.1
        focus_mask True
        action [Hide("scr_ep01_04_01_Bella_Phone_Browser"),Jump("lb_ep01_04_01_Bella_Phone_Start")]

screen scr_ep01_04_01_Bella_Phone_Text(v_ep01_04_01_Bella_Photo_Image):
    add v_ep01_04_01_Bella_Photo_Image
    textbutton "HOME":
        text_outlines [ (absolute(6), "#000", absolute(0), absolute(0)) ]
        xalign 0.5
        yalign 0.1
        focus_mask True
        action [Hide("scr_ep01_04_01_Bella_Phone_Text"),Jump("lb_ep01_04_01_Bella_Phone_Start")]

screen scr_ep01_04_01_Bella_Phone_Phone:
    zorder -10 # These should look like part of the scene, so they should go under things like the music player if they overlap
    timer 0.30 action acn_ep01_04_01_Bella_Work_change_hour repeat False
    text "[bw_h_hours]" xalign 0.44 yalign 0.023 size 24 outlines [(absolute(2), "#000", absolute(0), absolute(0))]

    textbutton "HOME":
        text_outlines [ (absolute(6), "#000", absolute(0), absolute(0)) ]
        xalign 0.5
        yalign 0.1
        focus_mask True
        action [Hide("scr_ep01_04_01_Bella_Phone_Phone"),Jump("lb_ep01_04_01_Bella_Phone_Start")]

screen scr_ep01_04_01_Bella_Phone_Calendar:
    textbutton "HOME":
        text_outlines [ (absolute(6), "#000", absolute(0), absolute(0)) ]
        xalign 0.5
        yalign 0.1
        focus_mask True
        action [Hide("scr_ep01_04_01_Bella_Phone_Calendar"),Jump("lb_ep01_04_01_Bella_Phone_Start")]

screen scr_ep01_04_01_Bella_Phone_Camera:
    textbutton "HOME":
        text_outlines [ (absolute(6), "#000", absolute(0), absolute(0)) ]
        xalign 0.5
        yalign 0.1
        focus_mask True
        action [Hide("scr_ep01_04_01_Bella_Phone_Camera"),Jump("lb_ep01_04_01_Bella_Phone_Start")]

screen scr_ep01_04_01_Bella_Phone_Mail:
    textbutton "HOME":
        text_outlines [ (absolute(6), "#000", absolute(0), absolute(0)) ]
        xalign 0.5
        yalign 0.1
        focus_mask True
        action [Hide("scr_ep01_04_01_Bella_Phone_Mail"),Jump("lb_ep01_04_01_Bella_Phone_Start")]

screen scr_ep01_04_01_Bella_Phone_Notes:
    textbutton "HOME":
        text_outlines [ (absolute(6), "#000", absolute(0), absolute(0)) ]
        xalign 0.5
        yalign 0.1
        focus_mask True
        action [Hide("scr_ep01_04_01_Bella_Phone_Notes"),Jump("lb_ep01_04_01_Bella_Phone_Start")]

screen scr_ep01_04_01_Bella_Phone_Photo(v_ep01_04_01_Bella_Photo_Image,v_ep01_04_01_Bella_Photo_NoSay):
    add v_ep01_04_01_Bella_Photo_Image
    if v_ep01_04_01_Bella_Photo_NoSay:
        textbutton "HOME":
            text_outlines [ (absolute(6), "#000", absolute(0), absolute(0)) ]
            xalign 0.5
            yalign 0.1
            focus_mask True
            action [SetVariable("v_ep01_04_01_Bella_Photo_Number",1), Hide("scr_ep01_04_01_Bella_Phone_Photo"),Jump("lb_ep01_04_01_Bella_Phone_Start")]

        if v_ep01_04_01_Bella_Photo_Number > 1:
            textbutton "SWIPE LEFT":
                text_outlines [ (absolute(6), "#000", absolute(0), absolute(0)) ]
                xalign 0.1
                yalign 0.5
                focus_mask True
                action [SetVariable("v_ep01_04_01_Bella_Photo_Number",v_ep01_04_01_Bella_Photo_Number - 1), Hide("scr_ep01_04_01_Bella_Phone_Photo"),Jump("lb_ep01_04_01_Bella_Phone_Photos")]

        if v_ep01_04_01_Bella_Photo_Number < 7:
            textbutton "SWIPE RIGHT":
                text_outlines [ (absolute(6), "#000", absolute(0), absolute(0)) ]
                xalign 0.9
                yalign 0.5
                focus_mask True
                action [SetVariable("v_ep01_04_01_Bella_Photo_Number",v_ep01_04_01_Bella_Photo_Number + 1), Hide("scr_ep01_04_01_Bella_Phone_Photo"),Jump("lb_ep01_04_01_Bella_Phone_Photos")]

screen scr_ep01_04_01_Bella_Phone_Error:
    zorder -10 # These should look like part of the scene, so they should go under things like the music player if they overlap
    add "sc bellaworkvisit b128"
    timer 0.30 action acn_ep01_04_01_Bella_Work_change_hour repeat False
    text "[bw_h_hours]" xalign 0.125 yalign 0.2 outlines [ (absolute(2), "#000", absolute(0), absolute(0)) ]

    imagebutton:
        idle "gui/bella_phone_icons/Contacts.png" xalign 0.865 yalign 0.23 focus_mask True
        action NullAction()

    imagebutton:
        idle "gui/bella_phone_icons/Browser.png" xalign 0.865 yalign 0.415 focus_mask True
        action NullAction()

    imagebutton:
        idle "gui/bella_phone_icons/Text.png" xalign 0.865 yalign 0.595 focus_mask True
        action NullAction()

    imagebutton:
        idle "gui/bella_phone_icons/Phone.png" xalign 0.865 yalign 0.775 focus_mask True
        action NullAction()

    imagebutton:
        idle "gui/bella_phone_icons/Calculator.png" xalign 0.125 yalign 0.30 focus_mask True
        action NullAction()

    imagebutton:
        idle "gui/bella_phone_icons/Calendar.png" xalign 0.225 yalign 0.30 focus_mask True
        action NullAction()

    imagebutton:
        idle "gui/bella_phone_icons/Camera.png" xalign 0.325 yalign 0.30 focus_mask True
        action NullAction()

    imagebutton:
        idle "gui/bella_phone_icons/Mail.png" xalign 0.425 yalign 0.30 focus_mask True
        action NullAction()

    imagebutton:
        idle "gui/bella_phone_icons/Notes.png" xalign 0.525 yalign 0.30 focus_mask True
        action NullAction()

    imagebutton:
        idle "gui/bella_phone_icons/Photos.png" xalign 0.625 yalign 0.30 focus_mask True
        action NullAction()

    imagebutton:
        idle "gui/bella_phone_icons/Paint.png" xalign 0.725 yalign 0.30 focus_mask True
        action NullAction()

    imagebutton:
        idle "gui/bella_phone_icons/Error.png" xalign 0.5 yalign 0.5 focus_mask True
        action [Hide("scr_ep01_04_01_Bella_Phone_Error"),Jump("lb_ep01_04_01_Bella_Phone_Start")]


label lb_ep01_04_01_Bella_Work_1:
    #Thief Of Hearts - Ep 1 Scene 04-01 - Bella scene
    #This scene belongs to the Bella option. The scene starts with the MC arriving at Bella’s workplace, the local clothing shop.
    #She gets mad at him for visiting her at her workplace, but the MC manages to convince her to talk about the side job.
    #The MC leaves the place with his first mission on the Bella path.
    #NOTE: The Extra scene option is only available in this scene if the player chooses to visit Bella as either their first or second option.
    #They will have the chance to get bonus renders of her if they make the right choice(s).
    #SCENE BEGINS
    #scene starts with the MC entering Bella’s place of work
    #she stands behind the counter, looking at her phone - there are only two shoppers in there, looking at clothes
    #scene description - https://glamadelaide.com.au/wp-content/uploads/2021/06/rspca-feature-image-2.jpg
    play sound "sound effects/01/convenience_store_ring.mp3"
    play music "sound effects/01/Lost in the Aisles.mp3" loop fadein 1.0
    scene sc bellaworkvisit b001
    with dissolve
    mc"(It’s quiet, which is unsurprising.)"
    stop sound fadeout 1.0
    show sc bellaworkvisit b002
    mc"(At least there should be no problems talking with [b_name] uninterrupted.)"
    #the MC goes to the counter to speak with Bella"
    show sc bellaworkvisit b003
    mc"Hey [mc_b_address], what’s up?"
    #she looks up and notices him and is not happy he’s here"
    show sc bellaworkvisit b004
    with faster_dissolve
    b"[y_name]!"
    show sc bellaworkvisit b005
    b"What the hell are you doing here??"
    show sc bellaworkvisit b006
    mc"We need to talk."
    show sc bellaworkvisit b007
    mc"I didn’t get a chance to speak to you before you left the house this morning because I slept in."
    show sc bellaworkvisit b008
    b"Not my problem."
    show sc bellaworkvisit b009
    b"Besides, you shouldn’t have come here."
    show sc bellaworkvisit b010
    b"The word on the street is the cops are patrolling the area and asking people if they have any information about the job we pulled yesterday."
    show sc bellaworkvisit b011
    b"So your presence is only bound to make things worse if they come in here and see us together."
    show sc bellaworkvisit b012
    mc"Relax... I was in disguise, remember?"
    show sc bellaworkvisit b013
    b"Yeah, but I wasn’t."
    b"And if they’ve figured out that I wasn’t a real waitress, then I could be totally screwed."
    show sc bellaworkvisit b014
    b"So scram before I have to kick your ass out of here myself."
    show sc bellaworkvisit b015
    mc"Look, I just need a few minutes of your time and then I’m gone."
    show sc bellaworkvisit b016
    mc"Besides, [mc_vic_address] wants us to discuss the tattoo parlours in town after you finish your shift."
    show sc bellaworkvisit b017
    mc"And I really want to be part of this big job he has in the works so I {b}have{/b} to get that flash drive back."
    show sc bellaworkvisit b018
    b"Ugh... Fine."
    show sc bellaworkvisit b019
    b"But know this... I’m only helping you because he asked me to."
    b"And I also don’t want to get in any more trouble with him."
    show sc bellaworkvisit b020
    mc"Works for me."
    $ task_addnew("Go with "+b_name+" to the Tattoo Parlour",4)
    show sc bellaworkvisit b021
    if not persistent.v_sex_anim_enabled_locked and persistent.v_sex_anim_enabled:
        show sc bella work visit butt wiggle1 onlayer anim_layer
    b"Okay, so I looked at the tattoo design you drew up last night."
    b"I made a call to one place, and sent an email to the other and managed to rule out both as possibilities."
    show sc bellaworkvisit b022
    b"But the third parlour... Well, it looks like that the girl at the party could have had her tattoo done there."
    show sc bellaworkvisit b023
    b"Or at the very least, the artist should be able to tell us where it came from or where she was inked."
    show sc bellaworkvisit b024
    b"And maybe even what the meaning of it."
    scene onlayer anim_layer
    show sc bellaworkvisit b025
    if not persistent.v_sex_anim_enabled_locked and persistent.v_sex_anim_enabled:
        show sc bella work visit butt wiggle2 onlayer anim_layer
    mc"All right, it’s a start."
    show sc bellaworkvisit b026
    mc"So what time should I meet you?"
    scene onlayer anim_layer
    show sc bellaworkvisit b027
    b"My shift finishes at three o’clock, so wait for me outside at the back of the store. Then I’ll take you to this place."
    show sc bellaworkvisit b028
    mc"Okay, I’ll be there."
    show sc bellaworkvisit b019
    b"Anything else?"
    show sc bellaworkvisit b020
    mc"Yeah... What were you looking at on your phone?"
    show sc bellaworkvisit b029
    b"Huh?"
    show sc bellaworkvisit b030
    b"Oh, it’s nothing."
    show sc bellaworkvisit b031
    mc"Are you sure about that? You seem pretty invested in it, whatever it was."
    show sc bellaworkvisit b019
    b"You’re not going to let this rest until I tell you, are you?"
    show sc bellaworkvisit b020
    mc"No chance."
    show sc bellaworkvisit b019
    b"Hmm... Okay, I’ll tell you."
    show sc bellaworkvisit b032
    b"Well, if you must know, [vic_name] has asked me to do a few things which I think are related to this big job he is planning."
    show sc bellaworkvisit b033
    mc"Has he given you any details about the job?"
    show sc bellaworkvisit b034
    b"No, none at all."
    b"The only thing he wants me to do is to create a forgery of a painting from some German artist."
    show sc bellaworkvisit b035
    mc"What painting?"
    show sc bellaworkvisit b036
    b"See for yourself."
    #She shows the MC pictures on her phone. MC takes her phone and starts going through the pictures Victor sent her. MC says that looks complicated to forge.
    #show the MC flicking through a few images - https://www.replicapropstore.com/cdn/shop/products/mockup-5acb4c59_1200x.jpg?v=1572782081 - https://pixhost.to/show/608/443345367_screenshot-2024-02-04-at-11-40-25-am.jpg - https://pixhost.to/show/608/443345382_screenshot-2024-02-04-at-11-41-21-am.jpg
    show sc bellaworkvisit b037
    mc"Hmm..."
    show sc bellaworkvisit b038
    mc"Well, this is an interesting painting. Very eye-catching."
    show sc bellaworkvisit b039
    b"I thought you’d like it, you little perv."
    show sc bellaworkvisit b038
    mc"Guilty as charged."
    show sc bellaworkvisit b040
    mc"This looks like it could be quite complicated to forge, even for you."
    mc"Especially when taking a closer look at the color changes over time and some surface cracking."
    show sc bellaworkvisit b041
    b"You’re right, though the main obstacle for me is finding the right paints and brushes I need to make it look authentic."
    b"And he hasn’t given me much time to get it done."
    show sc bellaworkvisit b029
    b"The things I need are very expensive. After extensive research, there are only a few art schools in town that could have the right tools for me to make the replica."
    show sc bellaworkvisit b042
    mc"Do you know which schools?"
    show sc bellaworkvisit b030
    b"Yeah, they’re all located in the rich area of town where security is much tighter and harder to get around."
    show sc bellaworkvisit b031
    mc"Hmm..."

    #Offer to help / Take time to consider

    menu:
        "Offer to help"(wt="You will have a 'Special Date' scene with [b_name] at the park + Task Point"):
            show sc bellaworkvisit b021
            show sc bella work visit butt wiggle1 onlayer anim_layer
            b"Look, working with you goes against every fibre of my being."
            show sc bellaworkvisit b022
            b"But this is important to [vic_mc_rel], so it’s important to me. And it would also be for the good of the [private_group], of course."
            scene onlayer anim_layer
            show sc bellaworkvisit b024
            b"I want you to help me get these things, [y_name]. I mean you do owe me, considering I’m helping you to find this tattoo parlour and the girl who has the flash drive."
            $ v_ep01_task02_girls_tattoo_counter += 1
            show sc bellaworkvisit b028
            mc"(Damn, she’s right.)"
            show sc bellaworkvisit b026
            show sc bella work visit butt wiggle2 onlayer anim_layer
            mc"Well, if it’s for the good of the [private_group], then fine, I’ll help you."
            scene onlayer anim_layer
            show sc bellaworkvisit b029
            b"Cool."
            $ v_ep01_04_01_Bella_Work_Date = True

        "Take time to consider":
            show sc bellaworkvisit b025
            mc"(I could offer to help her, but I'd rather stew over this for a bit longer.)"
            show sc bellaworkvisit b028
            mc"(And I don't want [b_name] to think I'm a sucker for helping her.)"
            show sc bellaworkvisit b023
            mc"(Even though I'm intrigued by the task.)"

    #NEW TASK ADDED - Help Bella procure items for the painting forgery
    #*EXTRA SCENE OPTION: Only available if the player chooses to visit Bella either first or second.
    #If the player chooses to visit her last, the automatic choice here will be the "Leave the store" option below.
    #[Leave the store / Hang around]
    if v_ep01_work_visit_options_1 == "[b_name]" or v_ep01_work_visit_options_2 == "[b_name]":
        menu:
            "Leave the store":
                $ v_ep01_04_01_Bella_Stay_Or_Leave = "Leave"
                jump lb_ep01_04_01_Bella_Work_3
            "Hang around"(wt="Best option"):
                show sc bellaworkvisit b032
                b"Anyway, get going, [y_name]. There’s no reason for you to be here any longer."
                $ rewards_unlock ("bella",1)
                show sc bellaworkvisit b033
                mc"(And there’s the bitchy [mc_b_address] that I know.)"
                mc"Fine, I’m going."
                stop music fadeout 1.0
                #the MC turns and sees the female officer outside Bella’s store
                show sc bellaworkvisit b053a
                with hpunch
                mc"Shit..."
                stop sound fadeout 1.0
                show sc bellaworkvisit b054
                b"What is it now?"
                show sc bellaworkvisit b053
                mc"Look outside."
                #Bella sees the officer outside her store
                show sc bellaworkvisit b055
                b"Oh, fuck!"
                show sc bellaworkvisit b056
                mc"It looks like she might come in here and ask you some questions."
                show sc bellaworkvisit b034
                b"What am I going to do? What if she recognises me from the party yesterday?"
                show sc bellaworkvisit b035
                mc"All right, calm down."
                mc"This is what you’re going to do."
                show sc bellaworkvisit b057
                mc"Go and hide in the changing room. I’ll pretend I’m the staff working here today."
                mc"Once she’s gone, I’ll let you know."
                show sc bellaworkvisit b058
                b"That won’t work you idiot!"
                b"What if she checks back there?"
                show sc bellaworkvisit b059
                mc"She’s not going to do that. I’ll make sure of it."
                show sc bellaworkvisit b060
                b"What are you going to do?"
                mc"Don’t worry so much. If things get dicey, I’ll handle it."
                show sc bellaworkvisit b061
                mc"Now move that tight ass of yours and go and hide!"
                show sc bellaworkvisit b062
                b"Da fuq??"
                #the MC shoots her a serious look
                show sc bellaworkvisit b063
                mc"..."
                show sc bellaworkvisit b064
                b"All right, all right. I’m going."
                #Bella is pissed off at the MC talking to her like that - being demanding"
                #she leaves and hides out in the changing room"
                #show the back of her ass as she says this next part"
                show sc bellaworkvisit b065
                b"(Did he seriously just call my ass, tight?)"
                #Bella’s expression changes to annoyed"
                show sc bellaworkvisit b066
                b"(Even if it is, it’s none of his goddamn business.)"
                play sound "sound effects/01/convenience_store_ring.mp3"
                #the female officer enters the store
                play music "sound effects/01/Seducing the Officer.mp3" loop fadein 1.0
                show sc bellaworkvisit b067
                "..."
                mc"(Well, hello Señorita!)"
                mc"(Where have you been all my life?)"
                #the officer talks to one of the customers in the store and holds up an image with a face on it
                #show a closer render of that image on the sheet
                stop sound fadeout 1.0
                show sc bellaworkvisit b068
                mc"(Oh shit!)"
                show sc bellaworkvisit b069
                mc"(It looks like she has an image of [b_name] on that picture. If she finds her in the changing room, then we are screwed.)"
                mc"(Hopefully that couple didn't get a good look at [b_name] while they've been in the store.)"
                #the female officer approaches the counter where the MC is"
                show sc bellaworkvisit b070
                officer"Hi there. Are you the manager?"
                show sc bellaworkvisit b071
                mc"I sure am. What can I do for you?"
                #she gives a sceptical look
                show sc bellaworkvisit b072
                officer"Hmm... Aren’t you a little young to be running a clothing store, Sir?"
                show sc bellaworkvisit b073
                mc"I’m certainly young. But what I meant was, I’m the manager on duty today."
                show sc bellaworkvisit b074
                mc"The regular manager is off work today, sick. She should be back tomorrow."
                show sc bellaworkvisit b075
                officer"So there’s nobody else working here today?"
                show sc bellaworkvisit b076
                mc"Nope, im working by myself today."
                # or  mc"Just me, myself and I"  (mc being snarky)
                show sc bellaworkvisit b077
                officer"I see."
                show sc bellaworkvisit b074
                mc"Can I help you with something?"
                show sc bellaworkvisit b078
                officer"I’m investigating a robbery."
                officer"I’m asking members of the public to see if they can help by identifying certain people who attended a local gathering yesterday."
                show sc bellaworkvisit b079
                mc"Sure thing, officer...?"
                show sc bellaworkvisit b078
                officer"Justice."
                show sc bellaworkvisit b080
                mc"Seriously? That’s your surname?"
                #or  mc"Seriously?  That's your lastname"  (US english version)
                show sc bellaworkvisit b081
                off_justice"Yeah, yeah, yeah. I know all the jokes so don’t even think about it."
                show sc bellaworkvisit b082
                mc"I don’t suppose you’d want to hear about my great idea for what you and I could do with those handcuffs, do you Officer Justice?"
                show sc bellaworkvisit b081
                off_justice"No, I don’t."
                show sc bellaworkvisit b083
                off_justice"Anyway, have you seen this woman?"
                #she hands him a blurry image of Bella dressed as the waitress from a security camera
                show sc bellaworkvisit b084
                mc"Hmm... No, I can’t say that I have. The picture is a little blurry to see her face clearly."
                show sc bellaworkvisit b085
                off_justice"It’s the best image we could pull from the cameras."
                mc"Who is she?"
                show sc bellaworkvisit b086
                off_justice"We’re not sure."
                off_justice"But we’re hoping to find her so we can ask her questions related to the robbery."
                #or off_justice"But we’re hoping to find her so we can ask her some questions."
                show sc bellaworkvisit b087
                mc"I wish I could help you further, but no I haven’t seen her before."
                mc"However, I’d say she works in a diner going by the outfit she’s wearing."
                show sc bellaworkvisit b088
                off_justice"That was my first thought."
                off_justice"However, the head chef said she wasn’t on the catering staff so we suspect that she may have been in disguise and not an actual waitress."
                # or off_justice"However, the head chef said she wasn’t on the catering staff so we suspect the outfit was just for show, and she's not an actual waitress"
                show sc bellaworkvisit b089
                off_justice"Do you sell any wigs or outfits similar to what she is wearing in that image?"
                show sc bellaworkvisit b090
                mc"We get all kinds of stuff coming through the store on any given day, but I can tell you that I haven’t sold anything like that recently."
                show sc bellaworkvisit b091
                off_justice"You wouldn’t happen to be hiding anything from me, would you Sir?"
                show sc bellaworkvisit b092
                mc"Of course not, officer, but I’d be happy to drop my pants so you can do a proper search if you like?"
                show sc bellaworkvisit b093
                off_justice"I’ll pass."
                show sc bellaworkvisit b094
                mc"Can’t blame a guy for trying. Especially when the officer I’m talking to has {b}fine{/b} written all over her."
                #the MC gives a cheeky grin - the officer ignores his last comment
                show sc bellaworkvisit b095
                off_justice"You look familiar. Have we met before?"
                off_justice"And before you ask, that was a serious question, not a pickup line."
                show sc bellaworkvisit b092
                mc"Nah, I don’t think so."
                show sc bellaworkvisit b096
                if persistent.v_anim_enabled:
                    show sc bella spider mc onlayer anim_layer
                else:
                    show sc bellaworkvisit b097-mc1 onlayer anim_layer
                mc"But I have been told that I look like that Tim Holland guy."
                #the MC poses and smiles
                show sc bellaworkvisit b097
                off_justice"Yeah, you wish."
                scene onlayer anim_layer
                show sc bellaworkvisit b098
                off_justice"(He’s a cocky little shit, but... I do admire his confidence.)"
                show sc bellaworkvisit b099
                off_justice"If you don’t mind, I’m going to take a look around."
                show sc bellaworkvisit b100
                mc"Is that really necessary?"
                mc"As you can see, we’re not very busy."
                show sc bellaworkvisit b101
                off_justice"Just standard procedure, Sir."
                off_justice"Unless of course, there’s something you want to tell me... You know, to save me the trouble."
                mc"(Shit... How do I talk my way out of this one?)"
                stop music fadeout 1.0
                show sc bellaworkvisit b102
                off_justice"I’ll do a quick check of the store and then I’ll get out of your hair."
                #the officer starts to move towards the changing room door
                show sc bellaworkvisit b103
                mc"(We are so fucked.)"
                #the officer’s walkie-talkie goes off - she gets a call just as she’s about to check the changing room
                show sc bellaworkvisit b104
                play sound "sound effects/01/police_radio_alert.ogg"
                dispatcher"{i}*BEEP* *BEEP* *BEEP* *BEEP*{/i}{w=2.2}\n{i}Code 3, all available units. Officers requesting backup to a shots fired call. 246 suspect is fleeing the scene at the corner of Welsh and Adler.{/i}"
                #"Calling all units. Armed and dangerous man in the vicinity..."
                #other officers call out on the walkie-talkie from the crime scene
                stop sound fadeout 1.0
                show sc bellaworkvisit b105
                dis_officer"WE NEED BACKUP! THERE’S SO MUCH BLOOD!!" with hpunch
                show sc bellaworkvisit b106
                off_justice"(Goddammit! Can’t those two idiots go {b}one{/b} damm day without screwing up?)"
                #the officer talks into the W-T
                show sc bellaworkvisit b107
                off_justice"10-4. I’m a few blocks away. Heading to the location now, over."
                #the officer leaves the store and gives the MC a smug look before she leaves
                show sc bellaworkvisit b108
                mc"(Holy shit... That was close.)"
                #show the door to the changing room door
                play sound "sound effects/01/police_siren_loop.ogg" fadein 1.0 loop
                if persistent.v_anim_enabled:
                    show sc bella work visit police leaving2
                    mc"(A few more seconds and she would have found [b_name] in there.)"
                    stop sound fadeout 3.0
                    #the MC looks at the officer exiting the store
                    mc"(I better wait until she’s driven off before I tell [b_name] the coast is clear.)"
                    mc"(It’s concerning that this woman is potentially looking for us. I’ll have to keep an eye out for her in the future.)"
                else:
                    show sc bellaworkvisit b049
                    mc"(A few more seconds and she would have found [b_name] in there.)"
                    stop sound fadeout 5.0
                    show sc bellaworkvisit b050
                    mc"(I better wait until she’s driven off before I tell [b_name] the coast is clear.)"
                    $ task_addpoi("Officer Justice - Local Law Enforcement",2)
                    show sc bellaworkvisit b051
                    mc"(It’s concerning that this woman is potentially looking for us. I’ll have to keep an eye out for her in the future.)"
                $ task_addpoi("Officer Justice - Local Law Enforcement",2)
                #the MC looks under the counter and notices Bella’s phone which is still unlocked
                if persistent.v_anim_enabled:
                    show sc bella phone1
                    mc"(Hmm... What do we have here? It’s [b_name]’s phone. And she’s left it unlocked.)"
                else:
                    show sc bellaworkvisit b109
                    mc"(Hmm... What do we have here?)"
                    show sc bellaworkvisit b110
                    mc"(It’s [b_name]’s phone. And she’s left it unlocked.)"
                #mc"(It’s [b_name]’s phone. And she’s left it unlocked.)"
                menu:
                    "Lock it":
                        play sound "sound effects/01/phone_lock.mp3"
                        show sc bellaworkvisit b111
                        pause 0.8
                        show sc bellaworkvisit b109
                        mc"(I have better things to do than snoop through her phone.)"
                        #the MC locks her phone and the screen of the phone goes blank
                        #go down to "scene continues"
                        stop sound fadeout 1.0
                        jump lb_ep01_04_01_Bella_Work_2
                    "Go through her phone"(wt="Best option"):
                        play music "sound effects/01/Too Cool.mp3" loop fadein 1.0
                        show sc bellaworkvisit b110
                        mc"(I wonder if she was looking at something other than the the painting and lied to me about the mission that [mc_vic_address] is planning, or if there are details on here about it?)"
                        #show Bella’s home screen and make it possible for the player to click on the "Text Message" app - https://is1-ssl.mzstatic.com/image/thumb/Purple126/v4/b7/90/1b/b7901b0d-32aa-dc55-6899-8c2c8d8c21d3/AppIcon-0-0-1x_U007emarketing-0-0-0-10-0-0-sRGB-0-0-0-GLES2_U002c0-512MB-85-220-0-0.png/1200x630wa.png"
                        #the MC checks the text messages exchanged between her and Victor - he scrolls through the messages they’ve exchanged"
                        jump lb_ep01_04_01_Bella_Phone_Start

                label lb_ep01_04_01_Bella_Phone_Start:
                    call screen scr_ep01_04_01_Bella_Phone_Horizontal

                label lb_ep01_04_01_Bella_Phone_Contacts:
                    call screen scr_ep01_04_01_Bella_Phone_Error

                label lb_ep01_04_01_Bella_Phone_Browser:
                    call screen scr_ep01_04_01_Bella_Phone_Error

                label lb_ep01_04_01_Bella_Phone_Text:
                    show screen scr_ep01_04_01_Bella_Phone_Text("sc bellaworkvisit b129") onlayer master
                    mc"(Hmm... There’s nothing here about it. No discussions, no details.)"

                    mc"(Maybe she deleted them as a precaution.)"
                    call screen scr_ep01_04_01_Bella_Phone_Text("sc bellaworkvisit b129") onlayer master
                    #mc"(I’ll check the images app)"

                label lb_ep01_04_01_Bella_Phone_Phone:
                    call screen scr_ep01_04_01_Bella_Phone_Error

                label lb_ep01_04_01_Bella_Phone_Calculator:
                    call screen scr_ep01_04_01_Bella_Phone_Error

                label lb_ep01_04_01_Bella_Phone_Calendar:
                    call screen scr_ep01_04_01_Bella_Phone_Error

                label lb_ep01_04_01_Bella_Phone_Camera:
                    call screen scr_ep01_04_01_Bella_Phone_Error

                label lb_ep01_04_01_Bella_Phone_Mail:
                    call screen scr_ep01_04_01_Bella_Phone_Error

                label lb_ep01_04_01_Bella_Phone_Notes:
                    call screen scr_ep01_04_01_Bella_Phone_Error

                label lb_ep01_04_01_Bella_Phone_Photos:
                    if v_ep01_04_01_Bella_Photo_Number == 1:
                        #show Bella’s home screen and make it possible for the player to click on the "Images app" - https://support.apple.com/content/dam/edam/applecare/images/en_US/psp_heros/mini-hero-photos.image.large_2x.png"
                        #the MC clicks on the images app and sees the nude painting again"
                        #scene sc bellaworkvisit b130
                        show screen scr_ep01_04_01_Bella_Phone_Photo("sc bellaworkvisit b130",False) onlayer master
                        if v_ep01_04_01_Bella_Photo_Talking_1 == False:
                            show sc bellaworkvisit b130
                            mc"(It’s a nice painting, I must admit.)"
                            mc"(I wonder if [b_name] would ever pose like that for an artist?)"
                            mc"(It’s a shame that I can’t draw or paint for shit, otherwise, I’d ask her to model for me, haha!)"
                            #MC giving a sarcastic face for the line below
                            hide screen scr_ep01_04_01_Bella_Phone_Photo
                            show sc bellaworkvisit b137
                            mc"(Yeah, I’m sure that would go down well.)"
                            $ v_ep01_04_01_Bella_Photo_Talking_1 = True
                        call screen scr_ep01_04_01_Bella_Phone_Photo("sc bellaworkvisit b130",True) onlayer master
                    elif v_ep01_04_01_Bella_Photo_Number == 2:
                        show screen scr_ep01_04_01_Bella_Phone_Photo("sc bellaworkvisit b131",False) onlayer master
                        if v_ep01_04_01_Bella_Photo_Talking_2 == False:
                            mc"(Hello... What do we have here?)"
                            $ v_ep01_04_01_Bella_Photo_Talking_2 = True
                        call screen scr_ep01_04_01_Bella_Phone_Photo("sc bellaworkvisit b131",True) onlayer master
                    elif v_ep01_04_01_Bella_Photo_Number == 3:
                        show screen scr_ep01_04_01_Bella_Phone_Photo("sc bellaworkvisit b132",False) onlayer master
                        if v_ep01_04_01_Bella_Photo_Talking_3 == False:
                            mc"(Damn... I wonder why she took these. And for whose benefit?)"
                            $ v_ep01_04_01_Bella_Photo_Talking_3 = True
                        call screen scr_ep01_04_01_Bella_Phone_Photo("sc bellaworkvisit b132",True) onlayer master
                    elif v_ep01_04_01_Bella_Photo_Number == 4:
                        #the MC flicks through the photos backwards - right to left and sees a selfie of Bella in her nightie kneeling or lying on her bed
                        show screen scr_ep01_04_01_Bella_Phone_Photo("sc bellaworkvisit b133",False) onlayer master
                        if v_ep01_04_01_Bella_Photo_Talking_4 == False:
                            mc"(It's so many levels of wrong seeing my [b_mc_rel] like this, but for some reason it's giving me serious wood.)"
                            $ v_ep01_04_01_Bella_Photo_Talking_4 = True
                        call screen scr_ep01_04_01_Bella_Phone_Photo("sc bellaworkvisit b133",True) onlayer master
                    elif v_ep01_04_01_Bella_Photo_Number == 5:
                        #the MC flicks through the photos backwards - left to right and sees a selfie of Bella in her underwear kneeling or lying on her bed
                        show screen scr_ep01_04_01_Bella_Phone_Photo("sc bellaworkvisit b134",False) onlayer master
                        if v_ep01_04_01_Bella_Photo_Talking_5 == False:
                            with vpunch
                            mc"(Fuck... me...)"
                            $ v_ep01_04_01_Bella_Photo_Talking_5 = True
                        call screen scr_ep01_04_01_Bella_Phone_Photo("sc bellaworkvisit b134",True) onlayer master
                    elif v_ep01_04_01_Bella_Photo_Number == 6:
                        #the MC flicks through the photos backwards - left to right and sees a selfie of Bella, topless, but her arm is covering her breasts - kneeling or lying on her bed)
                        show screen scr_ep01_04_01_Bella_Phone_Photo("sc bellaworkvisit b135",False) onlayer master
                        if v_ep01_04_01_Bella_Photo_Talking_6 == False:
                            mc"(With the way these images are going, surely the next one will be...)"
                            $ v_ep01_04_01_Bella_Photo_Talking_6 = True
                        call screen scr_ep01_04_01_Bella_Phone_Photo("sc bellaworkvisit b135",True) onlayer master
                    else:
                        #the MC flicks through the photos backwards - left to right and sees a humorous meme - https://pixhost.to/show/610/443358573_phone_meme.jpg"
                        show screen scr_ep01_04_01_Bella_Phone_Photo("sc bellaworkvisit b136",False) onlayer master
                        if v_ep01_04_01_Bella_Photo_Talking_7 == False:
                            mc"(Huh?)"
                            mc"(Damn, that’s the last of her images!)"
                            $ v_ep01_04_01_Bella_Photo_Talking_7 = True
                        call screen scr_ep01_04_01_Bella_Phone_Photo("sc bellaworkvisit b136",True) onlayer master
                    #the MC locks her phone and places it back under the counter
                    #scene continues
                    #THREE BONUS RENDERS OF BELLA (THREE NEW IMAGES OF HER IN LINGERIE ON HER BED) ADDED TO THE PHOTO GALLERY FOR HER

                label lb_ep01_04_01_Bella_Phone_Paint:
                    scene sc bellaworkvisit b128
                    call screen scr_ep01_04_01_Bella_Phone_Error

        label lb_ep01_04_01_Bella_Phone_Put_Down:
            show sc bellaworkvisit b111
            pause 0.8
            show sc bellaworkvisit b109
            pause 0.8

        label lb_ep01_04_01_Bella_Work_2:
            stop music fadeout 1.0
            play music "sound effects/01/Lost in the Aisles.mp3" loop fadein 1.0
            show sc bellaworkvisit b112
            mc"(All right, I’ll go and get [b_name] to let her know that the officer has left.)"
            #the MC stands outside the changing room.
            show sc bellaworkvisit b113
            mc"You can come out now, [mc_b_address]."
            #she opens the curtain
            show sc bellaworkvisit b114
            b"Is she gone?"
            show sc bellaworkvisit b115
            mc"Yeah, a few minutes ago."
            mc"You have no idea how close we came to getting caught."
            show sc bellaworkvisit b116
            b"I was totally freaking out, even though I couldn’t exactly hear what the two of you discussed."
            show sc bellaworkvisit b117
            b"What did she ask to you?"
            show sc bellaworkvisit b118
            mc"She had an image of you from the security footage at the party."
            mc"But luckily, the picture was blurry and I’m pretty sure they’ll have a hard time getting a positive ID."
            show sc bellaworkvisit b119
            b"That’s a relief."
            show sc bellaworkvisit b120
            mc"We should probably tell [mc_vic_address] about this."
            show sc bellaworkvisit b121
            b"No! Please don’t."
            b"I don’t want him thinking I made an error yesterday."
            show sc bellaworkvisit b122
            mc"Hmm... So you’re asking me to keep a secret for you, huh? Especially after the mistakes I made."
            show sc bellaworkvisit b123
            b"Please... [y_name]."
            show sc bellaworkvisit b124
            mc"Fine, I won’t say anything."
            mc"But only because it would make things more difficult for both of us if he knew about this."
            show sc bellaworkvisit b125
            b"Thanks."
            show sc bellaworkvisit b126
            mc"But you owe me {b}BIG{/b} for this."
            show sc bellaworkvisit b117
            b"I’m sure we can figure something out."
            show sc bellaworkvisit b118
            mc"Oh, we will."
            show sc bellaworkvisit b127
            mc"Okay, well, I guess I’ll see you at three. Back of the store?"
            show sc bellaworkvisit b114
            b"Make sure you’re there."
            show sc bellaworkvisit b127
            mc"I will be..."
            $ v_ep01_04_01_Bella_Stay_Or_Leave = "Stay"
            stop music fadeout 1.0
            #the MC leaves the store
            #screen goes blank
            #END SCENE
            scene black
            with dissolve
            scene black
            with Pause (2)
            jump lb_ep01_04_01_Bella_Work_4

label lb_ep01_04_01_Bella_Work_3:
    show sc bellaworkvisit b028
    mc"Okay, well, I guess I’ll see you at three. Back of the store?"
    show sc bellaworkvisit b027
    b"Make sure you’re there."
    show sc bellaworkvisit b028
    mc"I will be."
    stop music fadeout 1.0
    #the MC leaves the store
    #screen goes blank
    scene black
    with dissolve
    scene black
    with Pause (2)
    #The MC is now outside the shop
    show sc bellaworkvisit b043
    with dissolve
    mc"(That wasn’t anywhere near as painful as I thought it would be.)"
    #he sees a patrol car parked on the other side of the street
    show sc bellaworkvisit b044
    with hpunch
    mc"(Oh shit!)"
    #the police inspector who was at the crime scene the day before is patrolling the area on foot and talking to people in the street
    show sc bellaworkvisit b045
    mc"(I think that's the officer that was at the house yesterday. Is she onto us?)"
    show sc bellaworkvisit b046
    mc"(Well, I should have nothing to worry about, but if she goes in [b_name]’s store and recognises her from the party, then we'll be screwed.)"
    #the MC sees the officer get into her car
    play sound "sound effects/01/police_radio_alert.ogg"
    dispatcher"{i}*BEEP* *BEEP* *BEEP* *BEEP*{/i}{w=2.2}\n{i}Code 3, all available units. Officers requesting backup to a shots fired call. 246 suspect is fleeing the scene at the corner of Welsh and Adler.{/i}"
    #"Calling all units. Armed and dangerous man in the vicinity..."
    #other officers call out on the walkie-talkie from the crime scene
    stop sound fadeout 1.0
    show sc bellaworkvisit b047a
    dis_officer"WE NEED BACKUP! THERE’S SO MUCH BLOOD!!" with hpunch
    #the officer talks into the car
    show sc bellaworkvisit b047
    off_justice"10-4. I’m a few blocks away. Heading to the location now, over."
    #the police car drives off
    if persistent.v_anim_enabled:
        show sc bella work visit police leaving1
        mc"(Oh... She’s leaving, and it look like she’s in a hurry too.)"
        mc"(That was lucky.)"
        mc"(Still, it’s a bit of a problem that this officer is looking for us.)"
        $ task_addpoi("Officer Justice - Local Law Enforcement",2)
        mc"(I’ll have to keep an eye out for her...)"
    else:
        show sc bellaworkvisit b048
        mc"(Oh... She’s leaving, and it look like she’s in a hurry too.)"
        show sc bellaworkvisit b049
        mc"(That was lucky.)"
        play sound "sound effects/01/police_siren_loop.ogg" fadein 1.0 loop
        show sc bellaworkvisit b050
        mc"(Still, it’s a bit of a problem that this officer is looking for us.)"
        $ task_addpoi("Officer Justice - Local Law Enforcement",2)
        show sc bellaworkvisit b051
        mc"(I’ll have to keep an eye out for her...)"
    stop sound fadeout 2.0
    scene black
    with dissolve
    scene black
    with Pause (2)
    scene sc bellaworkvisit b052
    with dissolve
    #screen goes blank
    #END SCENE
    jump lb_ep01_04_01_Bella_Work_4


label lb_ep01_04_01_Bella_Work_4:
    #TEMP MENU UNTIL INTERACTABLE MENU MADE
    show sc mctown m02
    if(v_ep01_work_visit_options_3 == ""):
        show sc mctown m02
        with dissolve
        mc"(Okay, where to next?)"
        menu:
            "Clothing Store ([b_name])" if (v_ep01_work_visit_options_1 != "[b_name]" and v_ep01_work_visit_options_2 != "[b_name]"):
                #"If the player clicks on the CLOTHING STORE (scene with BELLA)"
                if v_ep01_work_visit_options_2 == "":
                    $ v_ep01_work_visit_options_2 = "[b_name]"
                else:
                    $ v_ep01_work_visit_options_3 = "[b_name]"
                scene black
                with dissolve
                pause 2.0
                jump lb_ep01_04_01_Bella_Work_1

            "Computer Shop ([a_name])" if (v_ep01_work_visit_options_1 != "[a_name]" and v_ep01_work_visit_options_2 != "[a_name]"):
                #"If the player clicks on the COMPUTER SHOP (scene with ARIEL)"
                if v_ep01_work_visit_options_2 == "":
                    $ v_ep01_work_visit_options_2 = "[a_name]"
                else:
                    $ v_ep01_work_visit_options_3 = "[a_name]"
                #the screen will go blank and take the player to the computer shop
                scene black
                with dissolve
                pause 2.0
                jump lb_ep01_05_01_Ariel_Work_1

            "Restaurant ([v_name])" if (v_ep01_work_visit_options_1 != "[v_name]" and v_ep01_work_visit_options_2 != "[v_name]"):
                #"If the player clicks on the RESTAURANT (scene with Vivian)"
                if v_ep01_work_visit_options_2 == "":
                    $ v_ep01_work_visit_options_2 = "[v_name]"
                else:
                    $ v_ep01_work_visit_options_3 = "[v_name]"
                #the screen will go blank and take the player to the restaurant"
                scene black
                with dissolve
                pause 2.0
                jump lb_ep01_06_01_Vivian_Work_1
    else:
        jump lb_ep01_06_02_Tattoo_Parlour_1
