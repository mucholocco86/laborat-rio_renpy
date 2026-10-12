label lb_ep01_The_MC_goes_to_the_art_gallery:
    centered "The next morning...{w=2.0}{nw}" with dissolve
    show text "The next morning..." #THESE LINES ARE NOT DUPLICATES. Needed to fade the text in and out!
    scene bg black with Dissolve(1)
    pause 1.0
    #Show the MC and Vivian sitting in the car, checking out the art gallery from their seated positions - https://annarubin.com/wp-content/uploads/2019/08/pushkin-museum-gallery.jpg

    #https://www.daz3d.com/the-gallery

    #Make sure Vivian is wearing a necklace as it will have a built-in camera inside it

    #Setting - https://www.daz3d.com/art-exhibition-warehouse
    #https://www.daz3d.com/idg-frame-gallery
    #https://www.daz3d.com/modern-museum
    $ renpy.music.set_volume(0.3, 0.0, channel="ambient")
    play ambient "sound effects/01/street_sound_day_ambience.ogg" loop fadein 1.0
    play music "sound effects/01/Art of Today2.mp3" loop fadein 1.0
    scene sc artgallery a001
    with dissolve
    v"There it is."
    show sc artgallery a002
    mc"It seems a little quiet, don't you think?"
    mc"I haven't seen anyone go in there."
    show sc artgallery a006
    v"Maybe we can walk around inside if there aren't many people in there."
    show sc artgallery a005
    v"Do you have the passes for the gallery?"
    #The MC holds them up
    show sc artgallery a007
    mc"Yep, right here."
    show sc artgallery a008
    mc"[a_name] made them and they are all-access passes."
    mc"So we should be able to visit any part of the gallery."
    show sc artgallery a005
    v"That's great."
    show sc artgallery a010
    v"She also gave me this necklace."
    show sc artgallery a011
    v"It has a built-in camera installed."
    show sc artgallery a011b
    mc"Damn she's good, isn't she?"
    show sc artgallery a013
    v"The best!"
    show sc artgallery a014
    v"All right, let's go check it out..."
    stop music fadeout 1.0
    #screen goes blank
    scene black
    with dissolve

    #The MC and Vivian entering the front entrance of the gallery - https://pixhost.to/show/38/449564568_screenshot-2024-02-28-at-9-46-46-pm.jpg
    #Or - https://www.daz3d.com/modern-museum

    #There are only a few people inside and a couple of members of security standing still and watching everything going on
    $ renpy.music.set_volume(1.0, 1.0, channel="ambient")
    show sc artgallery a015a
    with dissolve
    pause 2.0
    show sc artgallery a015
    with dissolve
    pause 2.0
    scene black
    with dissolve
    pause 1.0
    stop ambient fadeout 1.0
    $ renpy.music.set_volume(1.0, 0.0, channel="ambient2")
    play ambient2 "sound effects/01/art_gallery_ambience.ogg" loop fadein 1.0
    show sc artgallery a016
    with dissolve
    v"You were right. It is rather quiet in here, but that's probably because they just opened and it's a weekday."
    #The MC speaks closely with Vivian so no one else can hear them
    mc"Hmm... It will make it harder for us to blend in."
    show sc artgallery a017
    v"Don't worry about that."
    show sc artgallery a019
    v"We're here to take as many details and information as possible, and then we'll be done."
    show sc artgallery a020
    v"For now, pretend that you're genuinely interested in art."
    show sc artgallery a018
    mc"Who's to say I'm not?"
    #The MC looks over some of the sculptures in -  https://www.daz3d.com/jepes-modern-majlis
    show sc artgallery a022
    mc"I mean, this one is pretty impressive!"
    show sc artgallery a023
    v"Can you imagine how much some of these pieces are worth?"
    #The MC looks around it for a price tag
    menu:
        "Be funny":
            mc"Well, I was trying to figure out where the price tag is on this piece but I can't find it."
            show sc artgallery a028
            v"Haha! [y_name], don't mess around."
        "Be serious":
            mc"I was just wondering the same thing."
            show sc artgallery a025
            v"Anyway..."
    show sc artgallery a029
    v"Remember the task."
    mc"I'm on it..."
    #The MC looks around and sees a security camera in the top corner of that room - https://media.gettyimages.com/id/523085694/photo/security-camera-at-art-gallery.jpg?s=612x612&w=gi&k=20&c=v0vwMIGtoKGkn3w1gezADahkOFXXBgATE4qnCFYWUTE=
    show sc artgallery a030
    with dissolve
    mc"(Hmm...)"
    mc"(There's a security camera in the top-right corner of the first room of the gallery.)"
    show sc artgallery a032
    mc"[mc_v_address!c]?"
    show sc artgallery a033
    mc"Up there."
    #Vivian looks up and sees it
    show sc artgallery a034
    v"Oh, good catch. I may not have even noticed had you not seen it."
    #Vivian faces her chest towards the camera so her hidden recorder will see it
    show sc artgallery a035
    mc"(Hopefully she's not making it too obvious what she's doing.)"
    #The security is distracted by Vivian's cleavage. His eyebrows raise
    show sc artgallery a177
    mc"(Then again, they could end up being the perfect diversion.)"
    show sc artgallery a039
    v"Come on, let's see if that painting is in the next room..."
    #screen goes blank
    stop ambient2 fadeout 1.0
    scene black
    with dissolve
    scene black
    with Pause (2)


    #The MC and Vivian, along with a few other keen art lovers are in a room mainly with paintings - https://c8.alamy.com/comp/2FWNRX5/visitors-are-studying-italian-baroque-paintings-in-the-julia-and-hans-rausing-room-at-the-national-gallery-london-uk-2FWNRX5.jpg
    #Again, another security guard watches as they
    play ambient "sound effects/01/art_gallery_ambience2.ogg" loop fadein 1.0
    show sc artgallery a040
    with dissolve
    mc"Do you see it?"
    show sc artgallery a041
    v"No, it's not here."
    v"I was certain it was in this room of the art gallery."
    #The MC sees a member of security guarding a closed-off section
    show sc artgallery a042
    mc"What about over there?"
    #Vivian looks at the security guard in front of the section - the room is roped off
    show sc artgallery a044
    v"Oh, it could be in that room where the guard is standing."
    show sc artgallery a045
    v"It would make sense as it's a very expensive painting."
    mc"(Hmm... Wasn't that guy just in the other room??)"
    show sc artgallery a047
    mc"Maybe you should ask him if we can go in?"
    show sc artgallery a069
    v"Me?"
    v"No, I don't think so."
    show sc artgallery a068
    v"There's a sign that says that it's closed to the public."
    menu:
        "Encourage her":
            show sc artgallery a065
            mc"Well... I'm sure you can put on the charm."
            show sc artgallery a050
            mc"I mean, the guy keeps taking sneaky glances at you."
            show sc artgallery a049
            v"Oh, stop it."
            show sc artgallery a067
            v"There's no way he'd be interested in an old bird like me."
            show sc artgallery a054
            mc"Really?"
            show sc artgallery a065
            mc"Take a look."
            #Vivian looks over at the security guy who is staring at Vivian and the MC
            show sc artgallery a068
            pause 1.0
            show sc artgallery a045
            pause 2.0
            show sc artgallery a069
            with dissolve
            v"Oh... He really is checking me out."
            show sc artgallery a070
            mc"You see? I told you so."
        "Think of an idea":
            show sc artgallery a069
            mc"Hmm..."
            mc"(How are we going to get in there?)"
            show sc artgallery a068
            v"Oh!"
            show sc artgallery a045
            pause 2.0
            show sc artgallery a065
            mc"What is it?"
            show sc artgallery a069
            v"The guard over there..."
            show sc artgallery a068
            v"I think he was checking me out."
            show sc artgallery a045
            mc"Really? That's great!"
            show sc artgallery a061
            v"What do you mean?"
            show sc artgallery a053
            mc"Maybe you could use your charm to persuade him into letting us in there."

    show sc artgallery a178
    with dissolve
    v"That's crazy!"
    v"What would I even say to him?"
    show sc artgallery a050
    mc"Just go with your gut. Show him how passionate you are about these paintings."
    mc"And maybe give him a little extra..."
    show sc artgallery a065
    mc"If you know what I mean?"
    #The MC winks
    show sc artgallery a068
    v"Oh!"
    show sc artgallery a045
    mc"I mean I'd do it, but he's clearly interested in you, [mc_v_address!c]."
    mc"It's no surprise because you're a complete knockout!"
    show sc artgallery a067
    v"Thank you, dear."
    show sc artgallery a069
    v"But no need to exaggerate."
    show sc artgallery a070
    v"All right..."
    #Vivian prepares herself
    show sc artgallery a051
    v"The worst he can say is no, right?"
    show sc artgallery a042
    mc"Exactly."
    #Vivian goes over to the security guard while the MC watches
    show sc artgallery a072
    with dissolve
    v"Hi there."
    show sc artgallery a073
    guard"Morning, ma'am."
    show sc artgallery a074
    v"I was wondering if we could take a look inside that room, if possible?"
    show sc artgallery a086
    guard"No can do."
    show sc artgallery a075
    guard"This is a private section for VIP members of the gallery. It's not open to the public."
    show sc artgallery a077
    v"I understand."
    show sc artgallery a078
    v"The thing is..."
    show sc artgallery a079
    v"I'm a huge art lover, it's my passion, and it would really make my entire year if I could see some of the truly remarkable pieces I know are in there."
    show sc artgallery a080
    guard"Hmm..."
    #Vivian looks at the MC when she says this next line
    show sc artgallery a082
    v"All I ask is that we have a few minutes to take a quick look."
    show sc artgallery a083
    v"Maybe there's something I can do for you?"
    #Vivian moves in close so the guard can see her huge cleavage
    mc"(Oh yeah... She's bringing the big guns out.)"
    mc"(This guy will cave quicker than a sandcastle at high tide.)"
    show sc artgallery a086
    guard"I'm sorry, miss, but you're wasting your time."
    show sc artgallery a076
    guard"There's really nothing that I can do."
    #Vivian puts her head down, disappointed
    show sc artgallery a088
    v"Oh..."
    show sc artgallery a089
    guard"However, if {b}he{/b} were to come over and ask me, then maybe I could give you both a few minutes to take a quick peek."
    #Vivian puts her head up in surprise
    show sc artgallery a078
    v"Oh! Are you referring to the young man that I'm with?"
    show sc artgallery a076
    guard"Uh-huh."
    show sc artgallery a091
    v"I see..."
    #The guard and Vivian both look at the MC
    show sc artgallery a093
    mc"(Why are they both looking at me?)"
    #Vivian calls the MC over
    show sc artgallery a095
    v"Can you come over here, [y_name]?"
    #The MC joins the guard and Vivian
    show sc artgallery a096
    with dissolve
    v"So um, the gentlemen would like you to ask him if we could see inside this gallery."
    show sc artgallery a097
    mc"How come?"
    #The MC looks at the guard who raises an eyebrow and smiles
    show sc artgallery a098
    mc"Oh..."
    #A look of realisation crosses the MC's face
    show sc artgallery a099
    mc"(OH!)"
    show sc artgallery a109
    mc"(So it's like that, huh?)"
    mc"(Wonders never cease.)"
    mc"(I have no choice, so I better play along.)"
    show sc artgallery a103
    mc"We understand that this room may be restricted, but if possible, we would really appreciate it if you let us in to see the paintings. Please?"
    show sc artgallery a102
    mc"And we will adhere to any guidelines and treat the artwork with the utmost care and reverence, Sir."
    show sc artgallery a104
    guard"Sure thing, guys."
    #The guard pulls the rope back
    show sc artgallery a106
    guard"Just make sure not to touch anything. And no photos."
    show sc artgallery a107
    v"Yes, Sir. Thank you so much."
    show sc artgallery a109
    mc"Yeah, thanks."
    #The guard smiles at the MC
    show sc artgallery a105
    guard"You're welcome."
    #Show the MC and Vivian walking past the guard before they enter the room
    #The MC walks nearest to where the guard is standing
    show sc artgallery a181
    with dissolve
    guard"By the way..."
    #The guard leans in close to the MC and sniffs him, close enough for him to steal something off him
    #Important for later in the scene after they leave the art gallery
    guard"Love the cologne that you're wearing."
    show sc artgallery a182
    mc"Uh, thanks man."
    #Show the MC and Vivian walking into the closed-off room
    show sc artgallery a110
    with dissolve
    pause 1.0
    show sc artgallery a111
    with dissolve
    v"I have a feeling he likes you."
    #The MC says this with a serious face
    show sc artgallery a112
    mc"This never happened."
    #Vivian laughs
    play sound "sound effects/01/sexy_female_laugh3.mp3"
    show sc artgallery a113
    v"Haha!"
    show sc artgallery a114
    v"It turns out that my [mc_v_rel] is not just a hit with the ladies."
    stop sound fadeout 1.0
    show sc artgallery a115
    v"Don't worry, I won't tell the others."
    show sc artgallery a116
    mc"Let's get what we need so we can get the hell out of here..."
    stop ambient fadeout 1.0
    #screen goes blank
    scene black
    with dissolve
    scene black
    with Pause (2)



    #The scene continues in a private room with higher-quality paintings
    play music "sound effects/01/Art of Today1.mp3" loop fadein 1.0
    show sc artgallery a117
    with dissolve
    v"Which one is it again?"
    show sc artgallery a118
    mc"This is the one [b_name] showed me on her phone."
    #Show this image in a frame - https://pixhost.to/show/50/449674566_sc-bellaworkvisit-b130.jpg
    show sc artgallery a123
    v"Wow... It's hard to believe this painting is several hundred years old."
    show sc artgallery a119
    mc"Yeah... I see why it's a good plan to get it out of here."
    show sc artgallery a121
    mc"And [b_name] can make her version look authentic."
    show sc artgallery a179
    v"Quickly. Take some photos with your phone before that guard comes in here."
    show sc artgallery a124
    mc"I'm doing that now."
    #The MC takes photos with his phone
    show sc artgallery a125
    mc"Hmm..."
    #Vivian looks around
    show sc artgallery a126
    v"I don't see any security cameras."
    #The MC continues to take photos with his phone
    show sc artgallery a127
    mc"No, but if you look carefully at the walls, it seems like they have laser scanners instead."
    play sound "sound effects/01/camera_phone_photo.mp3"
    show sc artgallery a128
    mc"They're probably off during the day."
    stop music fadeout 3.0
    stop sound fadeout 1.0
    #Vivian walks near the painting he's been taking photos of
    show sc artgallery a129
    v"We'll have to take note of that."
    #The MC looks through his phone camera at Vivian
    play music "sound effects/01/Canvas Dreams.mp3" loop fadein 1.0
    show sc artgallery a130
    mc"Beautiful..."
    play sound "sound effects/01/camera_phone_photo.mp3"
    show sc artgallery a130
    with flash(0.25, 0, 0.75, "#fff")
    pause 2.0
    #Photo clicks
    stop sound fadeout 1.0
    show sc artgallery a131
    with dissolve
    v"Did you just take a photo of me?"
    mc"Yeah, I did."
    show sc artgallery a133
    v"Oh, but my hair doesn't look good and I don't think I put enough makeup on."
    show sc artgallery a134
    mc"Nah, you look fine."
    show sc artgallery a135
    mc"Hold still so I can take another."
    #Vivian looks shy as the MC takes a photo of her
    show sc artgallery a136
    v"I don't know about this. I think we're pushing our luck."
    show sc artgallery a137
    v"We should stop."
    show sc artgallery a139
    mc"Okay..."
    mc"Just give me one last pose and then we can go."
    show sc artgallery a140
    v"[y_name]..."
    mc"I promise. Last pic."
    show sc artgallery a142
    v"Okay, but how should I pose?"

    #[Front / Side / Back]
    menu:
        "Front":
            show sc artgallery a143
            mc"Just stay as you are, and don't forget to smile."
            show sc artgallery a144
            v"Like this?"
            #Vivian poses like this - https://ichef.bbci.co.uk/news/976/cpsprodpb/13410/production/_88046887_ap_scars2.jpg
            play sound "sound effects/01/camera_phone_photo.mp3"
            with flash(0.25, 0, 0.75, "#fff")
            mc"Perfect!"
            stop sound fadeout 1.0
            #phone clicks

        #[Take one more / That's enough]
            menu:
                "Take one more":
                    #Bonus image of Vivian if the player chooses this option - it will be the same bonus image for all three "Take one more" options
                    show sc artgallery a145
                    mc"(One more will do.)"
                    mc"(I better put my phone on silent so she doesn't hear the click this time.)"
                    #The MC takes a quick photo of Vivian's cleavage
                    show sc artgallery a148
                    with flash(0.25, 0, 0.75, "#fff")
                    mc"And done!"

                    #ONE BONUS RENDER OF VIVIAN (IN HER OUTFIT IN THE SPECIAL ROOM) ADDED TO THE PHOTO GALLERY FOR HER PROFILE

                    #GO DOWN TO >  #scene continues

                "That's enough":
                    #scene continues
                    show sc artgallery a149
                    v"There, are you happy now?"
                    mc"I am."

        "Side":
            show sc artgallery a144
            mc"Just stay as you are, and turn a bit to the side."
            mc"And don't forget to smile."
            show sc artgallery a151
            v"Like this?"
            #Vivian poses like this - https://people.com/thmb/UGoeJmgvrLTT4TtzSXLM3rFE88Q=/1500x0/filters:no_upscale():max_bytes(150000):strip_icc():focal(216x0:218x2)/ariel-winter-01-435-2-1e2193265e3e4252bd6d654f7ffa1c8e.jpg
            play sound "sound effects/01/camera_phone_photo.mp3"
            mc"Perfect!"
            with flash(0.25, 0, 0.75, "#fff")
            stop sound fadeout 1.0
            #phone clicks

        #[Take one more / That's enough]
            menu:
                "Take one more":

                    #Bonus image of Vivian if the player chooses this option - it will be the same bonus image for all three "Take one more" options
                    show sc artgallery a145
                    mc"(One more will do.)"
                    show sc artgallery a151
                    mc"(I better put my phone on silent so she doesn't hear the click this time.)"
                    #The MC takes a quick photo of Vivian's thighs and legs
                    show sc artgallery a148c
                    with flash(0.25, 0, 0.75, "#fff")
                    mc"And done!"

                    #ONE BONUS RENDER OF VIVIAN (IN HER OUTFIT IN THE SPECIAL ROOM) ADDED TO THE PHOTO GALLERY FOR HER PROFILE

                    #GO DOWN TO >  #scene continues

                "That's enough":
                    show sc artgallery a149
                    v"There, are you happy now?"
                    mc"I am."

        "Back"(wt="Task Point"):
            show sc artgallery a144
            mc"Maybe turn around so I can see your back, then look over your shoulder."
            mc"And don't forget to smile."
            show sc artgallery a152
            v"Like this?"
            #Vivian poses like this - https://www.shutterstock.com/image-photo/beautiful-tall-brunette-black-blouse-260nw-40037533.jpg - https://pixhost.to/show/52/449688150_000.jpg
            play sound "sound effects/01/camera_phone_photo.mp3"
            show sc artgallery a152
            with flash(0.25, 0, 0.75, "#fff")
            mc"Perfect!"
            stop sound fadeout 1.0
            $ v_ep01_task08_art_gallery_with_vivian_counter += 1
            #phone clicks

            #[Take one more / That's enough]
            menu:
                "Take one more"(wt="Task Point"):
                    #Bonus image of Vivian if the player chooses this option - it will be the same bonus image for all three "Take one more" options
                    show sc artgallery a145
                    mc"(One more will do.)"
                    show sc artgallery a152
                    mc"(I better put my phone on silent so she doesn't hear the click this time.)"
                    $ v_ep01_task08_art_gallery_with_vivian_counter += 2
                    #The MC takes a quick photo of Vivian's ass
                    show sc artgallery a148b
                    with flash(0.25, 0, 0.75, "#fff")
                    mc"And done!"
                    $ rewards_unlock ("vivian",9)

                    #ONE BONUS RENDER OF VIVIAN (IN HER OUTFIT IN THE SPECIAL ROOM) ADDED TO THE PHOTO GALLERY FOR HER PROFILE

                    #GO DOWN TO >  #scene continues

                "That's enough":
                    show sc artgallery a149
                    v"There, are you happy now?"
                    mc"I am."

    #scene continues
    show sc artgallery a153
    with dissolve
    mc"This is going to be my new phone wallpaper!"
    if v_ep01_task08_art_gallery_with_vivian_counter == 5:
        $ task_completed(8,"aa")
        $ v_ep01_vivian_aa_tasks_counter += 1
    if v_ep01_task08_art_gallery_with_vivian_counter == 4:
        $ task_completed(8,"a")
    if v_ep01_task08_art_gallery_with_vivian_counter == 3:
        $ task_completed(8,"b")
    if v_ep01_task08_art_gallery_with_vivian_counter == 2:
        $ task_completed(8,"c")
    if v_ep01_task08_art_gallery_with_vivian_counter <= 1:
        $ task_completed(8,"d")
    show sc artgallery a154
    v"Oh, no you don’t!"
    show sc artgallery a156
    v"Hey! Come back here, [y_name]!"
    stop music fadeout 1.0
    #The MC walks out of the room with Vivian chasing after him
    #screen goes blank
    scene black
    with dissolve
    scene black
    with Pause (2)

    #the MC and Vivian in the car outside the art gallery - the car hasn't started up yet
    play music "sound effects/01/Art of Today2.mp3" loop fadein 1.0
    show sc artgallery a183
    with dissolve
    mc"That went pretty good."
    #MC happy
    show sc artgallery a184
    v"Yeah, hopefully things go even better by the time we get to the actual job."
    #Vivian looks at the MC
    show sc artgallery a185
    mc"Speaking of which... Has [mc_vic_address] said anything else about this next heist?"
    show sc artgallery a186
    v"No, not yet."
    show sc artgallery a187
    mc"Do you think he'll let me be a part of it?"
    #MC looks concerned, worried Victor will leave him out
    show sc artgallery a188
    v"After he hears about how you've been helping everyone out, I'm sure he'll have no choice but to include you, sweetheart."
    #Vivian optimistic
    show sc artgallery a189
    mc"Thanks."
    #MC smiles, looks more hopeful
    show sc artgallery a190
    mc"(It still depends on me finding that damn drive.)"
    #MC thinking, mouth closed
    show sc artgallery a191
    mc"(And I only have until tonight to find that girl who took it from me.)"
    show sc artgallery a196
    mc"(No matter what, I have to be part of this next heist he's planning.)"
    $ task_addfuturetask("Try to help the group on the next major heist",4)
    show sc artgallery a192
    v"Don't worry, honey."
    #Vivian gives him an assured look
    show sc artgallery a193
    v"Everything will work itself out."
    show sc artgallery a194
    v"You just have to believe, and think good thoughts."
    #Vivian places her hand upon the MC's
    mc"(She's the one person I don't want to let down.)"
    #The MC smiles at Vivian
    show sc artgallery a196
    mc"(And even if I have to sell my damn soul, I'm getting that drive back!)"
    #MC looks determined
    show sc artgallery a197
    mc"Hmm..."
    #The MC looks at a security pass he has in his hands
    show sc artgallery a198
    v"Hey... Where did you get that from?"
    #Vivian surprised
    show sc artgallery a182
    with flash(0.25, 0, 0.75, "#fff")
    pause 1.0
    show sc artgallery a199
    with dissolve
    mc"I swiped it from that guard before we entered that closed room."
    #Flash back to when the guard leans in and whispers to the MC about his cologne
    show sc artgallery a200
    with flash(0.25, 0, 0.75, "#fff")
    v"Oh, [y_name]."
    #Vivian a little disappointed
    show sc artgallery a201
    mc"What? We might need it when we finally get to do this job."
    #MC gives her a cocky look
    show sc artgallery a202
    v"Yeah, but what if they check the security cameras to see when and where it was stolen?"
    #Vivian a little concerned
    show sc artgallery a203
    mc"Don't worry about that."
    #MC raises a hand, unphased
    show sc artgallery a204
    mc"I made sure to stand between the guard and one of those sculptures so the the camera would not see me."
    show sc artgallery a205
    mc"This time, I covered my tracks."
    #MC smiles at Vivian, proud of himself
    show sc artgallery a206
    v"(Sigh...)"
    show sc artgallery a207
    v"(He's getting so good at stealing and being deceptive, it's a little scary.)"
    show sc artgallery a208
    v"We should probably get out of here."
    show sc artgallery a185
    mc"Yeah, good idea..."
    stop music fadeout 1.0
    #Vivian starts up the car and it drives away from the art gallery
    #screen goes blank
    scene black
    with dissolve
    scene black
    with Pause (2)

    #The MC is back at home now, in his room
    show sc artgallery a180
    with dissolve
    mc"(Another successful task completed.)"
    mc"(This big job that [mc_vic_address] has been so secretive about is starting to look a little clearer.)"
    play sound "sound effects/01/Cell_Phone_Ring_Sound_Effect_-_reduced.mp3" loop
    if persistent.v_sounds_text_on == True:
        "(Phone rings)"
    else:
        pause 1.0
    show sc artgallery a158
    pause 1.0
    show sc artgallery a159
    mc"(Huh?)"
    #The MC picks up his phone and sees the name "Mrs X" on the screen
    show sc artgallery a160
    mc"(Mrs X?)"
    show sc artgallery a161
    mc"(Oh, it's Megan!)"
    #The MC answers the call
    stop sound fadeout 1.0
    show sc artgallery a162
    mc"Hello?"
    show sc artgallery a163
    megan"Hi there, [y_name]."
    show sc artgallery a164
    megan"I like it when a man answers so promptly. It's not a good thing to keep a woman waiting."
    show sc artgallery a163
    mc"Well, I certainly aim to please."
    show sc artgallery a166
    mc"I presume this call is about the job you would like me to do today?"
    show sc artgallery a167
    megan"Your presumptions are correct."
    megan"I'm going to send you the location of a warehouse that I would like you to check out."
    megan"It's on the other side of the city from where you are."
    show sc artgallery a171
    megan"Will that be a problem?"
    show sc artgallery a166
    mc"No, it shouldn't be, now that I have my bike back."
    show sc artgallery a164
    megan"Great!"
    show sc artgallery a162
    mc"What exactly am I looking for?"
    show sc artgallery a163
    megan"It's very simple."
    megan"Stake out the location, and see if it's occupied."
    show sc artgallery a168
    mc"That's it? It can't be that simple, surely."
    mc"Why can't you send one of your guys to check it out?"
    show sc artgallery a167
    megan"Because it's better if I send you in, someone who isn't known to this group. It's less suspicious that way."
    show sc artgallery a172
    megan"Besides, you will have a personal interest in checking this place out."
    show sc artgallery a170
    mc"How so?"
    show sc artgallery a167
    megan"We have reason to believe that the group you mentioned, the {i}Apex Legion{/i}..."
    megan"It could be their hideout. And that girl from the party you're looking for could be there."
    show sc artgallery a166
    mc"Oh..."
    mc"How did you find this out?"
    show sc artgallery a163
    megan"Like I told you last night, I have friends in high places."
    megan"As well as eyes and ears to the ground. One of my guys said he has a reliable source."
    show sc artgallery a167
    with dissolve
    megan"According to an online discussion that he intercepted, an exchange of goods is taking place there later this afternoon."
    show sc artgallery a166
    mc"(An exchange?)"
    mc"(Shit! That might be the girl trying to sell the flash drive!)"
    show sc artgallery a162
    mc"So you want me to scope this place out, see if anyone is in there, and then report back to you, right?"
    show sc artgallery a164
    megan"Exactly."
    show sc artgallery a171
    megan"Do that for me, and we'll take care of the rest."
    show sc artgallery a172
    megan"And if that girl is there, then I'll make sure you have the time with her to retrieve that drive you've been looking for."
    mc"(It seems to good to be true, but I have to check it out.)"
    show sc artgallery a166
    mc"What time do you want me to go there?"
    show sc artgallery a171
    megan"The exchange is supposed to take place around five-thirty, according to our source."
    show sc artgallery a167
    megan"If they are there, and you can confirm this, then I will send my team in to check it out."
    megan"Any other questions?"
    show sc artgallery a162
    mc"What if there's nobody there? What happens next?"
    show sc artgallery a163
    megan"Then we'll take care of it. We'll keep looking."
    show sc artgallery a171
    megan"I know you're against the clock to get that drive back but this is the best I could do."
    show sc artgallery a166
    mc"It's cool. And I appreciate the heads-up."
    show sc artgallery a167
    megan"No matter what happens, make sure you call me after you've checked the place out."
    show sc artgallery a162
    mc"I'll call as soon as I'm done there."
    show sc artgallery a164
    megan"That's what I like to hear."
    megan"Best of luck to you."
    show sc artgallery a166
    mc"Thanks, Megan."
    #(Call ends)
    show sc artgallery a175
    mc"(It's going to be a long day before it gets to sundown.)"
    show sc artgallery a176
    mc"(I sure hope that I'm not wasting my time, the precious little of it that I have left.)"
    #screen goes blank
    scene black
    with dissolve
    scene black
    with Pause (2)
    if v_ep01_06_01_Vivian_Work_Date:
        jump lb_ep01_Bonus_Scene_Date_with_Vivian1
    if v_ep01_04_01_Bella_Work_Date:
        jump lb_ep01_Bonus_Scene_Date_with_Bella1
    if v_ep01_05_01_Ariels_Work_Date:
        jump lb_ep01_Bonus_Scene_Date_with_Ariel1
    else:
        jump lb_ep01_The_MC_Investigates_the_gang

