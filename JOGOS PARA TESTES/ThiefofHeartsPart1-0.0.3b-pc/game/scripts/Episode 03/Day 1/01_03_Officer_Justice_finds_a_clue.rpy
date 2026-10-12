init:
    $ v_ep03_justice_fantasy_counter = 0


label lb_ep03_01_03_Officer_Justice_finds_a_clue:
    centered "Later that day...{w=2.0}{nw}" with dissolve
    show text "Later that day..."
    scene bg black with Dissolve(1)
    pause 1.0
    play ambient "sound effects/01/gymnasium_ambience1.ogg" loop fadein 1.0
    scene sc officerclue c001
    with dissolve
    "{i}Hello, and welcome to the world of high-tech computerised phone automatronics{/i}."
    show sc officerclue c002
    "{i}What we will do, is ask you a few questions, after the beep, you may speak your reply. {/i}"
    show sc officerclue c001
    "{i}How does that sound?{/i}"
    show sc officerclue c003
    ha"Sure, why not?"
    #Harry replies, unsure
    show sc officerclue c002
    "{i}Very good!{/i}"
    show sc officerclue c004
    "{i}Please, state your name.{/i}"
    play sound "sound effects/02/beep_sound_effect.mp3" noloop
    show sc officerclue c002
    "(BEEP!)"
    #sound effect for a beeping noise here
    show sc officerclue c005
    ha"Almighty, ruler..."
    show sc officerclue c006
    "{i}Thank you, Almighty Ruler!{/i}"
    show sc officerclue c007
    with dissolve
    officer"Ahem!"
    #Officer Justice interrupts Harry while he’s on the phone
    show sc officerclue c008
    with vpunch
    ha"(Oh, crap!)"
    #harry is startled
    show sc officerclue c009
    #he hangs up the phone
    ha"Sorry, miss. How can I help you?"
    show sc officerclue c010
    officer"My name is Officer Justice."
    if v_ep01_04_01_Bella_Stay_Or_Leave == "Stay":
        show sc officerclue c043a
        officer"Here's my card."
        #She hands him her business card
        show sc officerclue c042
        ha"Sweet!"
    #Harry looks at her business card
    show sc officerclue c010
    officer"I’m here to do some follow-up investigating for the robbery that happened here last week."
    show sc officerclue c011
    officer"May I speak with whoever is in charge?"
    show sc officerclue c012
    ha"The boss isn’t here right now, but I’d be very happy to show you around, Miss Justice."
    #He checks her out, a slight grin on his face
    show sc officerclue c013
    officer"That’s Officer Justice, buddy."
    show sc officerclue c014
    ha"Yes, of course."
    show sc officerclue c015
    ha"You’ll have to excuse me as I was mesmerised by your beauty."
    show sc officerclue c016
    officer"(Oh, great. Another horny young fool.)"
    #she rolls her eyes
    if v_ep01_04_01_Bella_Stay_Or_Leave == "Leave":
        #If the player selected to “Leave the Store" (the MC doesn’t speak to the officer in EP1 - Scene 04-01)
        show sc officerclue c017
        with dissolve
        pause 2.0
        #The MC enters the gym, wearing plain clothing, and NOT his work uniform
        #Harry sees him enter
        show sc officerclue c018
        ha"Hey, [y_name]!"
        #The MC looks up and sees Harry calling out to him, and Harry standing with the officer
        show sc officerclue c019
        mc"Hey..."
        show sc officerclue c020
        mc"(Oh, what is {b}she{/b} doing here?)"
        #The MC is concerned
        show sc officerclue c021
        mc"Hi there."
        #the MC is calm as she approaches the officer, and speaks to her
        show sc officerclue c022
        officer"And you are?"
        show sc officerclue c023
        ha"This is [y_name]. He also works here, but it’s his day off."
        show sc officerclue c024
        officer"I see."
        show sc officerclue c025
        mc"Is there anything I can help you with, miss?"
        show sc officerclue c026
        officer"I just have a few questions, actually."
        show sc officerclue c027
        officer"Where were you on the night of the robbery that took place here?"
        show sc officerclue c028
        mc"As I said to my boss, I was at home that night."
        show sc officerclue c029
        officer"And you have someone who can confirm this?"
        show sc officerclue c030
        mc"The people who I live with can, yes."
        show sc officerclue c031
        mc"Anything else?"
        show sc officerclue c032
        officer"Usually the suspects are known by the people they are robbing."
        show sc officerclue c033
        officer"My understanding is that you’ve seen the footage. Is that correct?"
        show sc officerclue c031
        mc"Uh, yeah. The boss showed me."
        show sc officerclue c032
        officer"And do you know these women?"
        show sc officerclue c033
        officer"Were they perhaps clients that could have attended sessions here at the gym in the days and weeks leading up to the robbery?"
        show sc officerclue c034
        officer"Or maybe you’ve seen them in town or when you’ve been in a public place?"
        show sc officerclue c030
        mc"No, I’ve never seen them before."
        show sc officerclue c035
        mc"I’m sorry, officer. Everything I know I’ve told my boss and he mentioned this to the police."
        show sc officerclue c036
        mc"I wish I could be of more help to you."
        show sc officerclue c037
        officer"It’s fine."
        show sc officerclue c038
        officer"Well, if you think of anything, here’s my card."
        #she hands him her business card
        show sc officerclue c039
        mc"Thanks."
        show sc officerclue c040
        pause 2.0
        #mc sees the card
        show sc officerclue c041
        mc"And good luck... Cracking the case."
        #He says this with optimism for her
        #And she gives him an annoyed look
        show sc officerclue c043
        officer"I’d like to review the footage in your boss’s office."
        #she addresses Harry.
        officer"Where is it?"
        show sc officerclue c044
        ha"Oh, it’s right this way."
        #Harry points in the direction with his arm/hand
        show sc officerclue c045
        with dissolve
        pause 1.5
        #add a render of Harry walking with the officer who looks around the gym while fitness junkies use the equipment
        show sc officerclue c046
        with dissolve
        pause 1.5
        #also shows the MC watching them walk away from him.
        show sc officerclue c047
        with dissolve
        pause 1.5
        #add a render of Harry glancing down to check out Officer Justice’s ass as they walk - she doesn’t notice
        show sc officerclue c048
        with dissolve
        pause 1.5
        #add a final render from behind officer justice so we can see all of her in uniform and her ass is the focus here
        #screen goes blank
        stop ambient fadeout 1.0
        scene black
        with dissolve
        scene black
        with Pause (2)

        play ambient "sound effects/01/gymnasium_ambience2.ogg" loop fadein 1.0
        show sc officerclue c049
        with dissolve
        ha"Hey dude."
        show sc officerclue c050
        ha"She’s a real firecracker that one, isn’t she?"
        show sc officerclue c051
        mc"The police officer?"
        show sc officerclue c052
        mc"Yeah, she’s definitely something."
        show sc officerclue c050
        ha"I’d sure love her to put handcuffs on me!"
        show sc officerclue c053
        ha"By the way, what are you doing here on your day off?"
        show sc officerclue c054
        mc"Oh, I just needed to get something from my locker."
        show sc officerclue c055
        mc"So did she ask you anything else?"
        show sc officerclue c056
        ha"The cop?"
        show sc officerclue c057
        ha"Nah, she arrived just before you got here."
        show sc officerclue c056
        ha"So it was a pretty short conversation."
        show sc officerclue c058
        ha"To be honest with you, I wasn’t really paying attention to much of what she said to me, if you know what I mean."
        show sc officerclue c059
        mc"Yeah, I read ya."
        show sc officerclue c056
        ha"I could definitely sense some tension between the two of you though."
        show sc officerclue c060
        ha"Do you know her?"
        show sc officerclue c061
        mc"Uh, no, I don’t... That was the first time I’ve met her."
        show sc officerclue c062
        ha"So are you going to call her?"
        show sc officerclue c063
        mc"Why would I do that?"
        show sc officerclue c064
        ha"She gave you her personal number, dude!"
        show sc officerclue c065
        mc"Yeah, but I don’t think it was for any special reason."
        show sc officerclue c066
        ha"Maybe not, but she didn’t give {b}me{/b} one of her cards."
        show sc officerclue c065
        mc"Hmm... Interesting."
        show sc officerclue c067
        ha"All I’m saying is, sometimes when chicks suggest one thing, they’re actually playing hard to get."
        show sc officerclue c068
        mc"So it is safe to presume that she’s not quite ready for Prince Harry?"
        #the MC gives Harry a cocky look
        show sc officerclue c069
        ha"They never ever seem to be."
        #Harry looks dismayed
        show sc officerclue c070
        mc"Sorry to hear that buddy."
        show sc officerclue c071
        mc"But you should try your luck."
        show sc officerclue c070
        mc"Maybe she was playing hard to get with you. Did you consider that?"
        show sc officerclue c072
        ha"No, I didn’t."
        show sc officerclue c071
        mc"You can do this Harry. I believe in you."
        show sc officerclue c073
        mc"Anyway, I’ll see you on the way out."
        show sc officerclue c074
        mc"I’ll be in the locker room if you need me..."
        stop ambient fadeout 1.0
        show sc officerclue c075
        #Harry stands there looking confident while the MC heads towards the locker area
        #screen goes blank
        scene black
        with dissolve
        scene black
        with Pause (2)
    else:
        #If the player selected to “Hang around" (the officer speaks to the MC) - in EP1 - Scene 04-01
        show sc officerclue c012
        ha"What would you like to see first?"
        show sc officerclue c043
        officer"I’d like to review the footage in your boss’s office now."
        #she addresses Harry
        officer"Where is it?"
        show sc officerclue c044
        ha"Oh, it’s right this way. Let me show you."
        #Harry points in the direction with his arm/hand
        show sc officerclue c134
        officer"No, I can manage on my own."
        show sc officerclue c135
        officer"Just make sure that I’m not disturbed."
        show sc officerclue c136
        ha"Sure thing, miss."
        show sc officerclue c137
        with dissolve
        pause 1.5
        #add a render of the officer who looks around the gym while fitness junkies use the equipment
        show sc officerclue c138
        with dissolve
        pause 1.5
        #add a render of Harry checking out check Officer Justice’s ass as she walks away from him
        show sc officerclue c048
        with dissolve
        pause 2.0
        #add a final render from behind officer justice so we can see all of her in uniform and her ass is the focus here
        #screen goes blank
        stop ambient fadeout 2.0
        scene black
        with dissolve
        scene black
        with Pause (2)

        play ambient "sound effects/01/gymnasium_ambience3.ogg" loop fadein 1.0
        show sc officerclue c139
        with dissolve
        pause 2.0
        #the MC enters the gym
        show sc officerclue c053
        with dissolve
        ha"Hey dude. What are you doing here on your day off?"
        show sc officerclue c054 #reuse
        mc"Oh, I just needed to get something from my locker."
        #FIND THE ORIGINAL SCRIPT FOR WHEN THE MC ARRIVES AND THE OFFICER HAS JUST BEEN THERE
        #HERE, SHE’S STILL AT THE GYM, AND IN THE BOSS'S OFFICE NOW
        show sc officerclue c050
        ha"By the way, there’s a police officer here at the moment."
        show sc officerclue c061
        mc"The police?"
        show sc officerclue c059
        mc"What are they doing here?"
        show sc officerclue c057
        ha"She was following up with the break-in last week."
        show sc officerclue c055
        mc"The officer is a she?"
        show sc officerclue c058
        ha"Yeah, and a smoking hot one as well."
        show sc officerclue c064
        ha"To be honest with you, I wasn’t really paying any attention to what she was saying, if you know what I mean."
        show sc officerclue c070
        mc"Yeah, I read ya."
        show sc officerclue c071
        mc"Just out of interest, what does she look like?"
        show sc officerclue c060
        ha"About five foot seven, long dark hair in a ponytail, and she had a bit of Latino look to her."
        show sc officerclue c057
        ha"As I said, smoking!"
        show sc officerclue c040a
        ha"Here, she gave me her card."
        #Harry hands the MC the card
        mc"Hmm..."
        #show Officer Justices card and the MC looking at it
        show sc officerclue c071
        mc"So did you give her the old Prince Harry charm?"
        #the MC gives Harry a cocky look
        show sc officerclue c066
        ha"Yeah, but she wasn’t biting at any of the lines I was casting out."
        #Harry looks dismayed
        show sc officerclue c070
        mc"Sorry to hear that buddy."
        show sc officerclue c055
        mc"Where is she now?"
        show sc officerclue c066
        ha"In the boss’s office looking over the security footage."
        show sc officerclue c065
        mc"I see."
        #The MC is deep in thought
        show sc officerclue c073
        mc"All right, I’ll only be a few minutes."
        show sc officerclue c074
        mc"I’ll be in the locker room if you need me..."
        show sc officerclue c075
        with dissolve
        pause 1.5
        stop ambient fadeout 1.0
        #The MC walks away from the front counter where Harry is
        #screen goes blank
        scene black
        with dissolve
        scene black
        with Pause (2)

    play music "sound effects/02/Dances and Dames.mp3" loop fadein 1.0
    show screen scr_secret_icon("v_secrets_ep03_01_03_1") onlayer ontop
    with { "ontop": dissolve}
    show sc officerclue c076
    with dissolve
    pause 1.5
    #scene returns with the MC approaching his boss’s office
    #create a render of him standing outside the office, and he notices the door cracked open slightly
    show sc officerclue c077
    with dissolve
    #the MC looks concerned as to what Officer Justice is up to
    mc"Hmm..."
    show sc officerclue c078
    show screen scr_secret_hotspot ("sc officerclue c078","1350, 136, 148, 195","v_secrets_ep03_01_03_1")
    with dissolve
    mc"..."
    #he pushes the door forward slightly and looks in
    hide screen scr_secret_hotspot
    show sc officerclue c079
    with dissolve
    pause 1.5
    #he sees the police officer standing in the same room when he spoke with his boss in Episode 2
    #ASSETS ON DAZ3D to use - https://www.daz3d.com/z-80s-gadgets
    #she stands in front of the security camera recording device - https://946e583539399c301dc7-100ffa5b52865b8ec92e09e9de9f4d02.ssl.cf2.rackcdn.com/17254/3294875.jpg
    #this is the recorder underneath the TV monitor where she can see the camera vision inside the gym - https://i.ytimg.com/vi/ZrJmXvxXjD0/maxresdefault.jpg
    mc"(...)"
    #the MC spies on the officer
    show sc officerclue c082
    with dissolve
    pause 1.5
    #show the officer watching the footage of the girls robbing the gym on the monitor - place that image on the screen she’s looking at
    show sc officerclue c083
    with dissolve
    officer"(Shit!)"
    #she looks pissed off
    show sc officerclue c084
    officer"(Dammit.)"
    hide screen scr_secret_icon onlayer ontop
    with { "ontop": dissolve}
    #show a close-up of her pressing the eject button on the VCR
    show sc officerclue c085
    with dissolve
    pause 1.5
    show sc officerclue c081
    with dissolve
    pause 1.5
    #The VHS pops out of the VCR and she pulls it out - https://t4.ftcdn.net/jpg/05/50/04/83/360_F_550048313_r1IFMJoe93c3h7dm2SwGic8XCbIcMIdZ.jpg
    show sc officerclue c086
    with dissolve
    pause 1.5
    #show the MC looking surprised as he peers through the open door at her
    show sc officerclue c087
    with dissolve
    pause 1.5
    #she stands up to leave the office
    show sc officerclue c088
    with dissolve
    pause 2.0

    if v_ep01_04_01_Bella_Stay_Or_Leave == "Stay":
        #the MC hides behind a wall/door so she doesn’t see him as she exits the office
        show sc officerclue c140
        with dissolve
        pause 1.5
        #on her way out. the officer notices a wall with a picture frame on it
        show sc officerclue c141
        with dissolve
        pause 1.5
        officer"(...)"
        show sc officerclue c142
        with dissolve
        pause 1.5
        #She stands directly in front of the wall with the picture frame on it
        show sc officerclue c143
        with dissolve
        officer"(Hmm... Why does this guy look so familiar?)"
        #the picture frame has the MC’s face in it (like 456 from Squid Game picture ) with the words “Employee of the Month" written on there
        #parody this smile and face for the MC - https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSzeMAiDYQc62uOp8N78jzEuHxDzDM17OuSKA&s
        #she looks deep in thought, hands on her hips
    #screen goes blank
    stop music fadeout 2.0
    scene black
    with dissolve
    scene black
    with Pause (2)
    centered "A little while later...{w=2.0}{nw}" with dissolve
    show text "A little while later..."
    scene bg black with Dissolve(1)
    pause 1.0
    play ambient "sound effects/01/gymnasium_ambience3.ogg" loop fadein 1.0
    show sc officerclue c089
    with dissolve
    #scene returns with Harry and Officer Justice exiting the boss’s main office
    officer"Okay, I’m done here."
    show sc officerclue c090
    officer"Thank you for your time."
    show sc officerclue c091
    ha"The pleasure was all mine, hot stuff."
    #She shoots him a snarky look
    show sc officerclue c092
    ha"I mean, officer."
    #Harry backtracks, not smiling
    show sc officerclue c093
    ha"So how about it?"
    #harry turns to her, looking lovingly at Harry
    show sc officerclue c094
    officer"Uh... What are you referring to?"
    #she looks confused
    show sc officerclue c095
    ha"Come on, officer. You’ve been giving me signals ever since you got here."
    show sc officerclue c096
    officer"Signals?"
    show sc officerclue c097
    ha"Look, I’m a mature person and you're a mature person, so why don't we just skip all the bullshit, get rid of our inhibitions, and DO what we really wanna DO?"
    #Harry looks surprised
    show sc officerclue c098
    officer"That’s a mighty fine idea."
    #the officer smiles, setting up Harry for disappointment
    show sc officerclue c099
    ha"Really?"
    show sc officerclue c100
    ha"(I can’t believe that line actually worked!)"
    #Harry looks genuinely surprised
    show sc officerclue c101
    officer"But there’s one problem with your idea."
    show sc officerclue c102
    ha"And what might that be?"
    show sc officerclue c103
    officer"The thing is, I don’t date guys like you."
    show sc officerclue c104
    officer"Nor will I ever sleep with them shortly after a first meeting."
    show sc officerclue c105
    officer"I’m more interested in guys who are an authority-like figure who likes to take charge, and are maybe interested in a little domination."
    show sc officerclue c106
    ha"Are you talking about you or me? The domination thing?"
    #Harry looks confused
    show sc officerclue c107
    officer"I’ll be leaving now."
    show sc officerclue c108
    officer"And I’ll be taking this tape with me down to the station."
    show sc officerclue c109
    officer"It’s evidence and we need to examine it a lot closer."
    show sc officerclue c110
    ha"Who am I to argue with someone who is here to serve and protect me, right?"
    show sc officerclue c111
    officer"Yeah, exactly."
    show sc officerclue c112
    #the MC spies on them and overhears the conversation between the officer and Harry
    mc"(Hmm... Something feels off about this.)"
    show sc officerclue c113
    mc"(Why didn’t she provide Harry with a receipt for the tape that she seized?)"
    mc"(And her reaction to the footage she was watching doesn’t sit right either.)"
    show sc officerclue c115
    officer"Thanks for your time, Larry."
    #she exits the gym
    show sc officerclue c116
    ha"It’s Harry."
    show sc officerclue c117
    ha"HARRY!!"
    #he shouts at her but she’s already left the gym
    show sc officerclue c118
    with dissolve
    mc"(I better follow her...)"
    stop ambient fadeout 1.0
    #screen goes blank
    scene black
    with dissolve
    scene black
    with Pause (2)
    jump lb_ep03_01_03_following_officer_justice_outside

label lb_ep03_01_03_following_officer_justice_outside:
    play ambient "sound effects/01/ghetto_street_ambience.ogg" loop fadein 1.0
    show sc officerclue c119
    with dissolve
    pause 2.0
    #Show the officer outside of the gym, in an alleyway, walking towards a dumpster
    show sc officerclue c119a
    with dissolve
    pause 1.5
    #She stands before the dumpster
    show sc officerclue c120
    with dissolve
    pause 1.5
    #The MC exits through a back door of the gym
    show sc officerclue c121
    with dissolve
    pause 1.5
    #he now stands at the end of the alleyway, spying on her where she can’t see him
    show sc officerclue c122
    with dissolve
    mc"(What is she up to? She’s acting very suspicious.)"
    show sc officerclue c123
    with dissolve
    mc"(Something is telling me that I should film this.)"
    show sc officerclue c124
    with dissolve
    pause 1.5
    #He pulls his phone out of his pocket
    show sc officerclue c125
    with dissolve
    pause 1.5
    #He starts filming her

    ####### NON-CANON scene begins here
    #$ v_ep03_justice_fantasy_counter += 1
    if persistent.v_secrets_enabled and persistent.v_secrets_ep03_01_03_1:
        jump lb_ep03_01_03_officer_justice_nc

        label lb_ep03_01_03_officer_justice_nc:
            if not _in_replay:
                scene img_secret_scene_overlay onlayer anim_layer
                with { "anim_layer": dissolve}
            else:
                show screen scr_end_replay
            #NOTE - this is like a parody of a sexy advert or commercial where what is happening is out of the ordinary and just a dream in the MC’s head
            #The screen flashes and the MC continues to film. His mouth is open wide
            play music "sound effects/03/stripteasing_officer.mp3" loop fadein 1.0
            scene sc officerclue c144
            with flash
            pause 1.5
            $ image_sequence("sc officerclue", ["c145", "c151", "c152"], 2.0)
            show sc officerclue c149
            with dissolve
            mc"(What on earth is she doing?)"
            $ image_sequence("sc officerclue", ["c153", "c154", "c155", "c156", "c157", "c146", "c147"], 2.0)
            #Officer Justice removes her belt and it hits the ground
            #Officer Justice then turns her face to one side but doesn’t look at the MC
            #She starts to unbutton her jacket top around chest height
            #Show the MC’s mouth widen as he looks through his phone camera
            #She continues to undo her top so we see her bra underneath
            #Then the jacket falls off and onto the ground leaving her standing in her underwear
            show sc officerclue c149
            with dissolve
            mc"(Holy shit!)"
            if not persistent.v_sex_anim_enabled_locked and persistent.v_sex_anim_enabled:
                scene sc officerclue c158 at tt_top
                pause
            elif True:
                show sc officerclue c146
            #Rolling screen of OJ in her lingerie, stockings and heels
            $ image_sequence("sc officerclue", ["c159", "c160", "c161", "c162"], 2.0)
            #Officer Justice does a half-turn so she’s facing away from the MC so we can see her ass and stockinged legs
            #She then bends down to reach her ankles, showing a sexy pose
            #Rolling screen of OJ in her lingerie, stockings and heels - a behind-shot
            #she faces forward toward the MC again. She reaches above her head and removes her hat
            #She throws her hat away
            #The MC continues looking stunned
            #OJ reaches behind her head to untie her hair
            #OJ lets her down - for a different look
            #OJ shakes her hair in a sexy way, eyes closed
            show sc officerclue c163
            with dissolve
            mc"(I’m so happy that I decided to film this.)"
            show sc officerclue c164
            with dissolve
            officer"Hey you!"
            officer"I see you over there."
            #The MC looks at OJ who is staring at him in a sexy way
            show sc officerclue c165
            mc"Oh, hi there."
            show sc officerclue c166
            officer"I know you’ve been watching me, [y_name]."
            show sc officerclue c167
            officer"How about you come over here so we can get down and dirty?"
            show sc officerclue c150
            mc"Yes, ma’am!"
            show sc officerclue c165
            pause 2.0
            scene black
            with Dissolve(3.0)
            #She waves her index finger towards herself to get him to come to her
            #show the MC’s POV as he moves towards OJ
            #closer image of OJ
            #closer again
            #and then the screen flashes back to reality before the MC can get to her
            stop music fadeout 2.0
            scene onlayer anim_layer
            with { "anim_layer": dissolve}
            scene black
            with dissolve
            scene black
            with Pause (2)
            $ persistent.replay_ep03_officer_alley_fantasy = False
            $ renpy.end_replay()
            #NON-CANON SCENE ENDS
    show sc officerclue c126
    with dissolve
    pause 1.5
    #The Officer pulls the VHS out of her bag
    show sc officerclue c127
    with dissolve
    pause 1.5
    #She then smashes the VHS against the edge of the dumpster so that it snaps in half
    show sc officerclue c128
    with dissolve
    pause 1.5
    #The MC looks shocked at what he’s seeing
    show sc officerclue c129
    with dissolve
    pause 1.5
    #the VHS is split in half and the tape ribbon comes out of it
    show sc officerclue c130
    with dissolve
    pause 1.5
    #she throws the VHS in the trash
    show sc officerclue c131
    with dissolve
    pause 1.5
    #she walks away from the dumpster and down the street in a calm manner
    $ task_addfuturetask("Find out why Officer Justice destroyed the tape",2)
    show sc officerclue c132
    with dissolve
    mc"(This could be important for later.)"
    show sc officerclue c133
    with dissolve
    pause 1.5
    #the MC watches her through his phone as he continues to record her
    stop ambient fadeout 1.0
    #screen goes blank
    scene black
    with dissolve
    scene black
    with Pause (2)
    jump lb_ep03_01_04_The_MC_calls_Zora
