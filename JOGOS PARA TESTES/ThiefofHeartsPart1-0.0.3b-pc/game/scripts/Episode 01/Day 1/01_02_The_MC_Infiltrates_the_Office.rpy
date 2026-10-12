label lb_ep01_intro_03_heist_scene:
    #(Show the MC standing outside the office door)
    play music "sound effects/01/Covert Affair.mp3" loop fadein 1.0
    scene sc mansionhall h33
    mc"All right, I'm here."
    #the MC tries to open the door
    play sound "sound effects/01/Trying To Open Locked Door Effect.mp3"
    show sc mansionhall h34
    mc"Locked... As predicted."
    stop sound fadeout 1.0
    show sc mansionoutside o16
    leader"You're going to have to pick the lock. Just like I showed you."
    #the MC reaches inside his pocket (or back pocket) for a lock picking pouch - https://cdn11.bigcommerce.com/s-lruv4nb/images/stencil/1280x1280/products/114/980/LPBrMcase__00286.1619819402.jpg?c=2
    show sc mansionhall h38
    mc"Okay, give me a few seconds here."
    #show the MC trying to pick the lock
    show sc mansionhall h42
    hacker"Oh no!"
    show sc mansionoutside o21
    hacker"There's a member of security coming up the stairs!"
    show sc mansionhall h43
    hacker"You'll have less than a few seconds before he sees you!"
    #the door cracks open
    play sound "sound effects/01/Door_Opening.mp3"
    show sc mansionhall h37
    mc"Got it!"
    stop sound fadeout 1.0
    play sound2 "sound effects/01/door_close_soft.mp3"
    #door closes sound effect
    show sc mansionoffice o01
    with vpunch
    #show the MC slipping inside the door and closing it just before the guy from security sees him
    stop sound2 fadeout 1.0
    mc"All right, I'm in!"
    show sc mansionhall h44
    mc"Damn... That was a close one."
    #show the MC with his back pressed up against the other side of the door
    show sc mansionoutside o20
    hacker"Can you see the main computer?"
    #show the main computer in a slightly darkened room
    show sc mansionoffice o02
    mc"Yeah, I see it."
    hacker"All right. Go over to it and I'll instruct you what to do from there."
    #door clicking sound to show the MC locking it from the inside - IMPORTANT, show the catch turned so it's locked - https://i.ytimg.com/vi/TFcGHfstQUo/maxresdefault.jpg
    show sc mansionoutside o16
    leader"In case they have sensors or anything in there we haven't accounted for, it's best that you don't move around in that office too much."
    mc"Roger that."
    #show the MC sitting at the desk and looking at the screen
    show sc mansionoffice o10
    mc"Okay, I'm in front of the laptop, but I'm going to need a password."
    show sc mansionoutside o20
    hacker"I'm on it."
    #younger sis starts typing
    show sc mansionoutside o24b
    hacker"I was able to decode it after we were able to gain access to the Walker household wi-fi password."
    hacker"All thanks to you know who."
    #younger sis is alluding to the mom here, and the mom will mention this in the next scene"
    show sc mansionoffice o06
    mc"Ah, yes, of course."
    show sc mansionoffice o05
    hacker"Entering the password from my end now."
    #computer screen changes to - ACCESS GRANTED"
    #sound effect for this"
    play sound "sound effects/01/download_complete_effect.mp3"
    show sc mansionoffice o11
    mc"Okay, I'm in."
    hacker"Sweet... The next bit you will have to do on your own."
    stop sound fadeout 1.0
    show sc mansionoffice o16
    leader"Plug the flash drive in, and set it to copy all the files."
    show sc mansionoutside o20
    hacker"Have you done it?"
    show sc mansionoffice o12
    mc"It's already downloading."
    mc"Wouldn't it be easier to transfer all these files directly to your computer?"
    show sc mansionoutside o20
    hacker"We could, but it's too risky."
    hacker"I'm sure that this Walker guy would have someone doing constant checks to see if anything is transmitting from his server to another."
    show sc mansionoutside o21
    hacker"And if they do, then it could be traced back to us in no time."
    hacker"So using that flash drive is the safer option."
    show sc mansionoffice o13
    mc"Fair enough."
    show sc mansionoffice o06
    mc"I guess that's why you're in the van and I'm in here, right?"
    show sc mansionoutside o24b
    hacker"Yeah, pretty much..."
    #Younger Sis smiles"
    #(screen goes blank)"
    #the MC sits in front of the computer, watching the screen"
    show sc mansionoffice o04
    mc"How's it going down on the floor?"
    show sc mansionhall h46
    waitress"Um, guys? We may have a problem."
    #show the parents and friends of the birthday boy celebrating while the head chef talks with a member of security"
    show sc mansionhall h51
    waitress"The main chef is speaking to the head of security."
    waitress"He looks really pissed!"
    show sc mansionhall h48
    waitress"What did you say to him?"
    show sc mansionhall h45
    mc"I kind of told him that all the food needed to be replaced and that I was the birthday boy's best friend."
    show sc mansionhall h51
    waitress"Oh, crap."
    waitress"He must know that something is wrong and that you lied to him."
    show sc mansionoffice o04
    mc"Tell me what's happening now."
    show sc mansionhall h48
    waitress"Nothing, yet."
    show sc mansionhall h46
    waitress"How much time is left on the download?"
    show sc mansionoffice o14
    mc"Thirty more seconds and I'm out of here."
    show sc mansionoutside o21
    hacker"[y_name]!!"
    show sc mansionhall h42
    hacker"There's a member of security on his way up the stairs again!"
    show sc mansionhall h43
    hacker"And he's on his way towards the room that you're in."
    show sc mansionoffice o09
    mc"What's he doing?"
    show sc mansionhall h44
    hacker"He's checking to make sure each door is locked and secure."
    #the MC looks at the door, concerned
    play sound "sound effects/01/Trying To Open Locked Door Effect.mp3"
    #Door handle rattles sound effect
    show sc mansionhall h47
    mc"{i}(*Whispering*){/i}\nOh shit..."
    mc"{i}(*Whispering*){/i}\nHe's trying to get in."
    #security talks into his walkie-talkie"
    stop sound fadeout 1.0
    show sc mansionhall h50
    security"Top floor area secured."
    security"Heading back down to the ground floor now, over."
    show sc mansionoffice o09
    mc"Woo... That was a close call."
    show sc mansionoutside o20
    hacker"He's gone now. How's that download going?"
    #show the screen - DOWNLOAD COMPLETE"
    play sound "sound effects/01/download_complete_effect.mp3"
    show sc mansionoffice o15
    mc"It's done!"
    stop sound fadeout 1.0
    show sc mansionoffice o16
    hacker"Okay..."
    show sc mansionoffice o17
    hacker"Carefully make your way out of there and then rejoin the party."
    #the MC switches off the computer
    show sc mansionoffice o18
    hacker"The members of security are scattered so you should have enough time to get down the stairs before any of them see you."
    show sc mansionoffice o19
    mc"All right, I'm heading back down there now."
    #mc opens the door and slips back outside and the door closes behind him"
    #final image here is the MC leaving the office and the door is unlocked - IMPORTANT - show the catch turned so it's left unlocked - https://i.ytimg.com/vi/TFcGHfstQUo/maxresdefault.jpg
    #(screen goes blank)"
    stop music fadeout 1.0
    scene black
    with dissolve
    scene black
    with Pause (2)
    jump lb_ep01_intro_04_heist_scene
