label ep11_freeroam_room2_intro_label:
$ mphone_music_genre = 3
$ mphone_play_songs(["music/ep11/jingle_balls.mp3"])
scene ep11_freeroam_room2_intro1 with Fade(1,1,1)
mc "(Finals week... I have some time off before the exams. I'll make sure I study more, but not tonight...)"
if not branchAlone and ep11_zoey_kiss == 2:
    mc "(Tonight is Bella's Christmas party... Give me strength to get through this one unscathed.)"
else:
    scene ep11_freeroam_room2_intro2 with dissolve
    mc "(Tonight is Bella's Christmas party... It's gonna be fun!)"

scene ep11_freeroam_room2_intro3 with dissolve
if ep11_zoey_kiss == 2:
    mc "(Zoey has been on my mind since Friday...)"
    if branchAlone:
        mc "(I can't deny it. I still have feelings for her. I still love her.)"
    else:
        mc "(I shouldn't have kissed her...but I can't deny it. I still have feelings for her. I still...love her.)"
        mc "(When did my life get this messy?)"
else:
    mc "(I've thought a lot about Zoey since Friday, and I made the right call...)"
    if ep11_zoey_kiss == 1:
        mc "(I may have some lingering feelings for her, but it's not the love I used to feel for her anymore.)"
    else:
        mc "(I'm not in love with her anymore.)"
    mc "(I wonder how she's doing, though... It was rough telling her that.)"

jump ep11_freeroam_room2_label

label ep11_zoey_joy_label:
scene ep11_zoey_joy1 with dissolve
$ renpy.pause()
scene ep11_zoey_joy2 with dissolve
$ renpy.pause()
scene ep11_zoey_joy3 with vpunch
zo "*{i}Happy scream{/i}*"
jump endEvent

label ep11_fr_gift_label:
scene ep11_fr_gift with dissolve
mc "(I stink at wrapping gifts... How do you even get good at it?)"

if ep11_gift_list[0] > 0:
    if ep11_gift_list[0] == 1:
        scene ep11_fr_gift1 with dissolve
        mc "(I think Derek's going to like his gift. It's an inside joke, but he'll hopefully get it.)"
    else:
        scene ep11_fr_gift2 with dissolve
        mc "(I think Derek's going to love his gift. It totally suits him. It will be a pain to wrap.)"
if ep11_gift_list[1] > 0:
    scene ep11_fr_gift3 with dissolve
    if ep11_gift_list[1] == 1:
        mc "(Bella's gift is a bit of a joke. I'm hoping it will get a laugh.)"
    else:
        mc "(I hope Bella will love her gift. They would look good on her.)"
    if branchIsabella and ep11_zoey_kiss == 2:
        mc "(And no...you didn't spend extra on her because of Zoey... You didn't.)"
        mc "(How do I even break up with her? Fuck... I've made such a mess.)"
if ep11_gift_list[2] > 0:
    scene ep11_fr_gift4 with dissolve
    if ep11_gift_list[2] == 1:
        if branchJill:
            mc "(This is a nice gift for Jill.)"
        else:
            mc "(I hope Jill will enjoy her gift.)"
    else:
        mc "(This gift is perfect for Jill. At least, I think so...)"
    if branchJill and ep11_zoey_kiss == 2:
        mc "(And no...you didn't spend extra on her because of Zoey... You didn't.)"
        mc "(How do I even break up with her? Fuck... I've made such a mess.)"
if ep11_gift_list[3] > 0:
    scene ep11_fr_gift5 with dissolve
    if ep11_gift_list[3] == 1:
        mc "(It's hard shopping for girls. Josy will know best what to do with this; it is a nice gift.)"
    else:
        mc "(It's hard shopping for girls. Josy will know best what to do with this; it is a great gift.)"
    if branchMayaJosy and ep11_zoey_kiss == 2:
        scene ep11_fr_gift6 with dissolve
        mc "(With guilt written all over it...)"
    if ep11_gift_list[4] == 0 and branchMayaJosy:
        if not branchMayaJosy or not ep11_zoey_kiss == 2:
            scene ep11_fr_gift6 with dissolve
        mc "(I'm so stupid... I didn't get anything for Maya.)"
if ep11_gift_list[4] > 0:
    scene ep11_fr_gift7 with dissolve
    if ep11_gift_list[4] == 1:
        mc "(It's not the most expensive gift, but it's right up Maya's alley.)"
    else:
        mc "(Maya will love this gift; I know it.)"
    if branchMayaJosy and ep11_zoey_kiss == 2:
        scene ep11_fr_gift6 with dissolve
        mc "(Guilty... Guilty... Guilty...)"
    if ep11_gift_list[3] == 0 and branchMayaJosy:
        if not branchMayaJosy or not ep11_zoey_kiss == 2:
            scene ep11_fr_gift6 with dissolve
        mc "(Fuck, I'm so stupid... I didn't get anything for Josy.)"
if ep11_gift_list[5] > 0:
    scene ep11_fr_gift8 with dissolve
    if ep11_gift_list[5] == 1:
        if branchSage and ep11_zoey_kiss < 2:
            mc "(Sage will appreciate this one.)"
        else:
            mc "(It's not the best brand, but hopefully, Sage will enjoy it.)"
    else:
        if branchSage:
            mc "(This gift will mean something to Sage...)"
        else:
            mc "(I know Sage will love this. It's perfect.)"
    if branchSage and ep11_zoey_kiss == 2:
        mc "(But does that even matter now? How do I even break up with her? Fuck... I've made such a mess.)"

scene ep11_fr_gift9 with dissolve
mc "(Alright... Done!)"
if branchSage and ep11_gift_list[5] == 0:
    scene ep11_fr_gift10 with dissolve
    if ep11_zoey_kiss == 2:
        mc "(I didn't get Sage a gift for Christmas... But does that even matter?)"
        mc "(How do I even break up with her? Fuck... I've made such a mess.)"
    else:
        mc "(I didn't get Sage a gift for Christmas... What was I thinking?)"
elif branchIsabella and ep11_gift_list[1] == 0:
    scene ep11_fr_gift10 with dissolve
    if ep11_zoey_kiss == 2:
        mc "(I didn't get Bella a gift for Christmas... But does that even matter?)"
        mc "(How do I even break up with her? Fuck... I've made such a mess.)"
    else:
        mc "(I didn't get Bella a gift for Christmas... What was I thinking?)"
elif branchJill and ep11_gift_list[2] == 0:
    scene ep11_fr_gift10 with dissolve
    if ep11_zoey_kiss == 2:
        mc "(I didn't get Jill a gift for Christmas... But does that even matter?)"
        mc "(How do I even break up with her? Fuck... I've made such a mess.)"
    else:
        mc "(I didn't get Jill a gift for Christmas, but she said it was ok... I think I made a big mistake... Fuck.)"
elif branchMayaJosy and ep11_gift_list[3] == 0 and ep11_gift_list[4] == 0:
    scene ep11_fr_gift10 with dissolve
    if ep11_zoey_kiss == 2:
        mc "(I didn't get Josy or Maya any gifts for Christmas... But does that even matter?)"
        mc "(How do I even break up with them? Fuck... I've made such a mess.)"
    else:
        mc "(I didn't get Josy or Maya any gifts for Christmas... What was I thinking?)"
elif 0 in ep11_gift_list:
    scene ep11_fr_gift10 with dissolve
    mc "(I didn't buy gifts for everyone, but what's done is done.)"
elif ep11_zoey_kiss != 2 or branchAlone:
    scene ep11_fr_gift11 with dissolve
    mc "(I feel like Santa - bringing everyone gifts.)"

$ task_list[0] = ""
$ updateTaskList()
jump endEvent

label ep11_fr2_end_label:
stop music fadeout 3
if not branchAlone and ep11_zoey_kiss == 2:
    scene ep11_fr2_end1 with dissolve
    mc "(Off to the party... This might be the last one we all spend together...)"
else:
    scene ep11_fr2_end2 with dissolve
    mc "(Off to the party!)"
jump ep11_md_label
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
