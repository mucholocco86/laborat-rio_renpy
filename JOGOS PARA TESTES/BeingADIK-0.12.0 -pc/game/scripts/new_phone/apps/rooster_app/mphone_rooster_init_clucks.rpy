label initRoosterLabel:
$ rooster_app_enabled = True
$ new_cluck = False
$ new_rooster_int = 0
if roosterState == "ep9_1":
    $ new_rooster_int = 5

    $ add_new_rooster_post("tybalt","I feel rejuvenated. After achieving all the goals I set out to achieve, I need more goals to strive for. Cello, yoga, and wine tasting, I look forward to mastering you. {color=#00a0e6}#Excellence{/color}",35,"ep9_cluck_photo_tybalt","rooster_section_tybalt_ep9")


    $ add_rooster_comment("tybalt","I'll make sure to bless you with my talent in the future.",10)
    $ add_rooster_comment("tyballs","Stroking a thin stick between your legs, lying on your back and swallowing... You were born ready!",4)
    $ add_rooster_comment("tybalt","{color=#00a0e6}@%s{/color} Thanks for the compliment. Perhaps we can see eye to eye after all." % roosterNickTyballs.split("@")[1],1)
    $ add_rooster_comment("lucas","{color=#00a0e6}@%s{/color} Can you please practice the cello in the daytime instead of in the mornings? It's hard to sleep." % roosterNickTybalt.split("@")[1],4)
    $ add_rooster_comment("tybalt","{color=#00a0e6}@%s{/color} I practice mornings and afternoons. It's the price we pay for excellence." % roosterNickLucas.split("@")[1],1)
    $ add_rooster_comment("lucas","{color=#00a0e6}@%s{/color} Fine! I'm going to start mastering the drums soon. Around midnight on the balcony near your room." % roosterNickTybalt.split("@")[1],2)
    $ add_rooster_comment("tybalt","{color=#00a0e6}@%s{/color} Perhaps this is a discussion we should have in private, freshman?" % roosterNickLucas.split("@")[1],1)


    $ add_new_rooster_post("zoey","{color=#00a0e6}#NoPlaceLikeHome{/color}",47,"ep9_cluck_photo_zoey","rooster_section_zoey_ep9")


    $ add_rooster_comment("bret","Damn, I miss you so much. Seeing your empty spot at the counter every day hits hard.",5)
    $ add_rooster_comment("jonah","Keep being you. They're lucky to have you over there.",3)
    $ add_rooster_comment("zoey","{color=#00a0e6}@%s{/color} Stop. You're gonna make me NOT cry or something. Think about the money you'll be saving instead." % roosterNickBret.split("@")[1],3)
    $ add_rooster_comment("zoey","{color=#00a0e6}@%s{/color} I wish I could take you all with me back home. I miss you, you bald-headed bastard." % roosterNickJonah.split("@")[1],3)
    if emma_calm:
        $ add_rooster_comment("emma","Surfing without you isn't the same.",2)
    $ add_rooster_comment("jonah","{color=#00a0e6}@%s{/color} Video chat date, soon?" % roosterNickZoey.split("@")[1],1)
    if emma_calm:
        $ add_rooster_comment("zoey","{color=#00a0e6}@%s{/color} Like you ever needed me for that. I'd just be holding you back. Keep on riding those waves, girl. You're awesome!" % roosterNickEmma.split("@")[1],2)
    $ add_rooster_comment("zoey","{color=#00a0e6}@%s{/color} This weekend?" % roosterNickJonah.split("@")[1],2)
    $ add_rooster_comment("jenna","I tattooed five of your stencils this week. Customers aren't even browsing my portfolio!",3)
    if emma_calm:
        $ add_rooster_comment("emma","{color=#00a0e6}@%s{/color} Holding me back? Please. No more so than Bret does." % roosterNickZoey.split("@")[1],2)
        $ add_rooster_comment("bret","{color=#00a0e6}@%s{/color} Hey!!!" % roosterNickEmma.split("@")[1],2)
    $ add_rooster_comment("zoey","{color=#00a0e6}@%s{/color} Five!? That's bonkers! You can put my stencils in the back if you're tired of them." % roosterNickJenna.split("@")[1],2)
    $ add_rooster_comment("jenna","{color=#00a0e6}@%s{/color} Nah! Inking your stuff makes it feel like you're still here." % roosterNickZoey.split("@")[1],5)


    $ add_new_rooster_post("sage","We've been carving pumpkins all night... Just a few more days until it's party time!!! {color=#00a0e6}#Halloween{/color}",80,"ep9_cluck_photo_sage","rooster_section_sage_ep9")



    $ add_rooster_comment("riona","Who else is stressing about their outfit? I've changed my mind like 10 times already.",18)
    $ add_rooster_comment("heather","I swear, if I have to carve another pumpkin, I'm gonna freak out.",8)
    $ add_rooster_comment("leon","{color=#00a0e6}@%s{/color} Not me. I've locked in this year's outfit, and it's gonna be hilarious!" % roosterNickRiona.split("@")[1],3)
    $ add_rooster_comment("riona","{color=#00a0e6}@%s{/color} What is it? Tease it!" % roosterNickLeon.split("@")[1],4)
    $ add_rooster_comment("josy","{color=#00a0e6}@%s{/color} Tell me about it. My hand hurts!" % roosterNickHeather.split("@")[1],7)
    $ add_rooster_comment("sage","{color=#00a0e6}@%s{/color} I'll tell {color=#00a0e6}@%s{/color} to do the remaining ten." % (roosterNickHeather.split("@")[1],roosterNickQuinn.split("@")[1]),10)
    $ add_rooster_comment("kylie","{color=#00a0e6}@%s{/color} Looks amazing! Can't wait!" % roosterNickSage.split("@")[1],16)
    $ add_rooster_comment("quinn","{color=#00a0e6}@%s{/color} Arieth, that means you should do them." % roosterNickArieth.split("@")[1],3)
    $ add_rooster_comment("leon","{color=#00a0e6}@%s{/color} Let's say it's a theme costume and the theme is impersonation." % roosterNickRiona.split("@")[1],7)
    $ add_rooster_comment("maya","{color=#00a0e6}@%s{/color} Do you need any help? I'm free for anything." % roosterNickSage.split("@")[1],3)
    $ add_rooster_comment("arieth","{color=#00a0e6}@%s{/color} But I'm still studying for the midterms." % roosterNickQuinn.split("@")[1],2)
    $ add_rooster_comment("rusty","That's a lot of pumpkins! The place is going to look great. Thanks for taking care of it!",28)
    $ add_rooster_comment("elena","{color=#00a0e6}@%s{/color} Yay! Theme costumes are the shit!!!" % roosterNickLeon.split("@")[1],14)
    $ add_rooster_comment("quinn","{color=#00a0e6}@%s{/color} What do you mean? Midterms are over." % roosterNickArieth.split("@")[1],3)
    $ add_rooster_comment("sage","{color=#00a0e6}@%s{/color} Yes! Meet me in my room tomorrow? 10 a.m.?" % roosterNickMaya.split("@")[1],2)
    $ add_rooster_comment("sarah","{color=#00a0e6}@%s{/color} Come on, Mel. I know you're ugly, but you don't have to wear a pumpkin over your head. Ever heard of a paper bag?" % roosterNickMelanie.split("@")[1],6)
    $ add_rooster_comment("arieth","{color=#00a0e6}@%s{/color} Yeah, but I didn't do that well on my tests, so I have to study more." % roosterNickQuinn.split("@")[1],2)
    $ add_rooster_comment("riona","{color=#00a0e6}@%s{/color} Can't wait to see it!" % roosterNickLeon.split("@")[1],3)
    $ add_rooster_comment("quinn","{color=#00a0e6}@%s{/color} Bitch, meet me in the kitchen. Now." % roosterNickArieth.split("@")[1],1)
    $ add_rooster_comment("melanie","{color=#00a0e6}@%s{/color} I hope you'll sleep well tonight. I just put pumpkin pulp all over your bed." % roosterNickSarah.split("@")[1],8)
    $ add_rooster_comment("dawe","HALLOWEEN!!! Where are our invitations? We're still waiting.",18)
    $ add_rooster_comment("sage","{color=#00a0e6}@%s{/color} I thought you were handling \"things\"?" % roosterNickQuinn.split("@")[1],1)
    $ add_rooster_comment("quinn","{color=#00a0e6}@%s{/color} I'm still working on it." % roosterNickSage.split("@")[1],1)
    $ add_rooster_comment("sage","{color=#00a0e6}@%s{/color} Kinda last minute, don't you think? Work faster." % roosterNickQuinn.split("@")[1],1)



    $ add_new_rooster_post("nick","This party is gonna be legendary! {color=#00a0e6}#Halloween{/color}",75,"ep9_cluck_photo_nick","rooster_section_nick_ep9")


    $ add_rooster_comment("johnboy","We spent all yesterday baking and decorating the place. Tonight's finally here!!! Let's go!!! {color=#00a0e6}#Halloween{/color}",35)
    $ add_rooster_comment("heather","Real mature, guys.",15)
    $ add_rooster_comment("leon","{color=#00a0e6}@%s{/color} If you're looking for mature, this party won't be it." % roosterNickHeather.split("@")[1],39)
    $ add_rooster_comment("derek","{color=#00a0e6}@%s{/color} Hell yes! Preach into the microphone!" % roosterNickLeon.split("@")[1],23)
    $ add_rooster_comment("mc","{color=#00a0e6}@%s{/color} Bro! I knew you were up to something, but a cake dick? Really?" % roosterNickJacob.split("@")[1],8)
    $ add_rooster_comment("jacob","{color=#00a0e6}@%s{/color} Hahah! I regret nothing. That picture is hilarious!" % roosterNickMC.split("@")[1],25)
    $ add_rooster_comment("tommy","{color=#00a0e6}@%s{/color} You should get that thing checked out. LMAO!" % roosterNickMC.split("@")[1],10)
    if affinity == "DIK":
        $ add_rooster_comment("mc","{color=#00a0e6}@%s{/color} The joke's on you, though. Makes you look like you're holding it and giggling like a girl." % roosterNickJacob.split("@")[1],30)
    else:
        $ add_rooster_comment("mc","{color=#00a0e6}@%s{/color} I'll have to quote Heather. Real mature, Jacob." % roosterNickJacob.split("@")[1],20)
    $ add_rooster_comment("christie","{color=#00a0e6}@%s{/color} Smaller than I heard it was." % roosterNickMC.split("@")[1],5)
    $ add_rooster_comment("mc","{color=#00a0e6}@%s{/color} ?" % roosterNickChristie.split("@")[1],1)
    $ add_rooster_comment("elena","{color=#00a0e6}@%s{/color} The camera is set up and good to go. Thanks for lending your room for it." % roosterNickMC.split("@")[1],15)
    $ add_rooster_comment("camila","Is that finger really a cake? It looks so good!",20)
    $ add_rooster_comment("mc","{color=#00a0e6}@%s{/color} Don't mention it. I'll try my best not to break it if I use it." % roosterNickElena.split("@")[1],8)
    $ add_rooster_comment("sage","I bet everybody is dressing up to get freaky right now!",20)
    $ add_rooster_comment("johnboy","{color=#00a0e6}@%s{/color} Sure is! Those eyeballs too!" % roosterNickCamila.split("@")[1],18)
    $ add_rooster_comment("quinn","{color=#00a0e6}@%s{/color} I know why you think the finger looks delicious." % roosterNickCamila.split("@")[1],16)
    $ add_rooster_comment("riona","{color=#00a0e6}@%s{/color} What's your cup size? Get it?" % roosterNickLeon.split("@")[1],12)
    $ add_rooster_comment("tommy","{color=#00a0e6}@%s{/color} I'm in my birthday suit. Wondering if it's enough for the party or not." % roosterNickSage.split("@")[1],24)
    $ add_rooster_comment("camila","{color=#00a0e6}@%s{/color} Watch me eat it tonight." % roosterNickQuinn.split("@")[1],10)
    $ add_rooster_comment("heather","{color=#00a0e6}@%s{/color} Yeah, if you want to look like a clown. You better get dressed!" % roosterNickTommy.split("@")[1],14)
    $ add_rooster_comment("tara","{color=#00a0e6}@%s{/color} Question... Is a costume a must? I kinda forgot." % roosterNickSage.split("@")[1],2)
    $ add_rooster_comment("quinn","{color=#00a0e6}@%s{/color} Are you still talking about the cake?" % roosterNickCamila.split("@")[1],5)
    $ add_rooster_comment("tommy","{color=#00a0e6}@%s{/color} A clown? No, that's Nick's role tonight." % roosterNickHeather.split("@")[1],5)
    $ add_rooster_comment("tiffani","{color=#00a0e6}@%s{/color} I know it's late, but is it cool if I bring a friend?" % roosterNickLeon.split("@")[1],5)
    $ add_rooster_comment("sage","{color=#00a0e6}@%s{/color} Yes. How could you forget? It's in the invitation." % roosterNickTara.split("@")[1],7)
    $ add_rooster_comment("tara","{color=#00a0e6}@%s{/color} Ok, I'll try to find something." % roosterNickSage.split("@")[1],2)
    $ add_rooster_comment("camila","{color=#00a0e6}@%s{/color} I don't know. I had a cocktail with Rio before getting dressed. Haha!" % roosterNickQuinn.split("@")[1],4)
    $ add_rooster_comment("leon","{color=#00a0e6}@%s{/color} Yeah, go ahead." % roosterNickTiffani.split("@")[1],2)
    $ add_rooster_comment("tommy","{color=#00a0e6}@%s{/color} Another one with a birthday suit. Do it!" % roosterNickTara.split("@")[1],16)
    $ add_rooster_comment("dawe","{color=#00a0e6}@%s{/color} Legendary, my ass! It's gonna be a total sausage party." % roosterNickNick.split("@")[1],12)



    $ add_new_rooster_post("derek","Need a break from the scary stuff? Drop by The Moose! Special drinks all night! {color=#00a0e6}#TheMooseLounge{/color}",46,"ep9_cluck_photo_derek","rooster_section_derek_ep9")

    $ add_rooster_comment("becky","What kind of idiot advertises alcohol on Rooster?",5)
    $ add_rooster_comment("rusty","You're gonna have it open tonight?",8)
    $ add_rooster_comment("riona","Yes! The Moose! Sign me up for one of those shots.",8)
    $ add_rooster_comment("jamie","I just did! 5/5. Cozy, great reception, and delicious drinks.", 15)
    $ add_rooster_comment("derek","{color=#00a0e6}@%s{/color} This idiot! Also, you're banned." % roosterNickBecky.split("@")[1],19)
    $ add_rooster_comment("derek","{color=#00a0e6}@%s{/color} All night!" % roosterNickRusty.split("@")[1],12)
    $ add_rooster_comment("johnboy","So that's where my dipping sauce went!",3)
    $ add_rooster_comment("jacob","Why is that tampon thing on the menu? I thought we went over this last time.",3)
    $ add_rooster_comment("derek","{color=#00a0e6}@%s{/color} People are loving it! Quick question: There's no lactose in it, right?" % roosterNickJohnBoy.split("@")[1],2)
    $ add_rooster_comment("derek","{color=#00a0e6}@%s{/color} It's back due to popular demand." % roosterNickJacob.split("@")[1],3)
    $ add_rooster_comment("becky","{color=#00a0e6}@%s{/color} Oh, no. What a shame that I don't get to try...um... Nope, I can't seem to find anything good on that menu." % roosterNickDerek.split("@")[1],4)
    $ add_rooster_comment("johnboy","{color=#00a0e6}@%s{/color} More than half of it is dairy." % roosterNickDerek.split("@")[1],2)
    $ add_rooster_comment("derek","{color=#00a0e6}@%s{/color} Oh... Someone might be farting extra tonight, then." % roosterNickJohnBoy.split("@")[1],3)


elif roosterState == "ep9_2":
    $ new_rooster_int = 2


    $ add_new_rooster_post("jamie","It's truly a magical Halloween party! If Franz could smile, he would! {color=#00a0e6}#Magic{/color}",19,"ep9_cluck_photo_jamie","rooster_section_jamie_ep9")


    $ add_rooster_comment("dany","THEY!",13)

    $ add_rooster_comment("leon","WTF! BOO! If you have magical powers, try making them disappear!",2)
    $ add_rooster_comment("karen","Such a cute costume!",6)
    $ add_rooster_comment("linda","{color=#00a0e6}@%s{/color} Why weren't we invited?" % roosterNickDany.split("@")[1],10)
    $ add_rooster_comment("dany","{color=#00a0e6}@%s{/color} Jam-Jam said he could only invite one of us. You're not missing out, though. Unless you're into constantly having your beliefs challenged by literally everyone." % roosterNickLinda.split("@")[1],2)
    $ add_rooster_comment("wendy","{color=#00a0e6}@%s{/color} I knew it was that bad. I could tell from all the clucks on Rooster about that party. Why don't you just leave when you're clearly not enjoying it?" % roosterNickDany.split("@")[1],15)
    $ add_rooster_comment("dany","{color=#00a0e6}@%s{/color} In a relationship, there are some things you do for your partner. This is one of them." % roosterNickWendy.split("@")[1],5)
    $ add_rooster_comment("minny","{color=#00a0e6}@%s{/color} We really can't come? We can be there in 10 minutes, if it's ok with you." % roosterNickDany.split("@")[1],8)

    $ add_rooster_choice("{color=#00a0e6}@%s{/color} Did you take your photo in my room yet?" % roosterNickJamie.split("@")[1])
    $ add_rooster_choice("{color=#00a0e6}@%s{/color} Make sure she doesn't invite people. We're full." % roosterNickJamie.split("@")[1])
    if affinity == "DIK":
        $ add_rooster_choice("{color=#00a0e6}@%s{/color} No. We get one night to dress up like idiots; you get the rest of the year." % roosterNickMinny.split("@")[1])



    $ add_new_rooster_post("elena","Don't forget to have your picture taken! Seriously! Don't miss out on the perfect memento of the night. Or else I'll have to shoot you! {color=#00a0e6}#PewPew #DIKsHalloween{/color}",86,"ep9_cluck_photo_elena","rooster_section_elena_ep9")


    $ add_rooster_comment("becky","I took a really funny picture! LOL! I can't wait to see your faces when you see it!",15)
    $ add_rooster_comment("christie","Can you send me my picture tomorrow?",12)
    $ add_rooster_comment("elena","{color=#00a0e6}@%s{/color} When we're done with the photos, we'll post an album online so everyone can download it." % roosterNickChristie.split("@")[1],20)
    $ add_rooster_comment("lily","Such an awesome idea! Remind me when I get there.",16)
    $ add_rooster_comment("elena","{color=#00a0e6}@%s{/color} Lily!!! Where are you!? Why are you not here yet!?" % roosterNickLily.split("@")[1],10)
    $ add_rooster_comment("sally","Can someone help me take one?",5)
    $ add_rooster_comment("rusty","{color=#00a0e6}@%s{/color} Just took a picture! Great idea, by the way!" % roosterNickElena.split("@")[1],10)
    $ add_rooster_comment("leon","{color=#00a0e6}@%s{/color} Is there like any way you can NOT do that?" % roosterNickElena.split("@")[1],2)
    $ add_rooster_comment("elena","{color=#00a0e6}@%s{/color} Meet me there; I'll help out." % roosterNickSally.split("@")[1],2)
    $ add_rooster_comment("elena","{color=#00a0e6}@%s{/color} Why? What did you take a picture of?" % roosterNickLeon.split("@")[1],5)
    $ add_rooster_comment("leon","{color=#00a0e6}@%s{/color} DM." % roosterNickElena.split("@")[1],1)
    $ add_rooster_comment("sarah","I expect to see at least five dick pics on that camera.",15)
    $ add_rooster_comment("sage","{color=#00a0e6}@%s{/color} And from the looks of it, at least 4 of them are Leon's." % roosterNickSarah.split("@")[1],17)
    $ add_rooster_comment("lily","{color=#00a0e6}@%s{/color} We're coming soon! Don't shoot me!" % roosterNickElena.split("@")[1],3)
    $ add_rooster_comment("elena","{color=#00a0e6}@%s{/color} No promises! I've got a shot in my gun with your name on it!" % roosterNickLily.split("@")[1],5)
    $ add_rooster_comment("leon","{color=#00a0e6}@%s{/color} Lies!" % roosterNickSage.split("@")[1],5)

    $ add_rooster_choice("You'll regret it if you don't get your picture taken. Don't wait until you're too drunk; do it now and get it done.")
    $ add_rooster_choice("{color=#00a0e6}@%s{/color} Thanks for the help with this." % roosterNickElena.split("@")[1])
    if branchAlone and ep7_lily_lewd:
        $ add_rooster_choice("{color=#00a0e6}@%s{/color} Lily! Get your ass over here! There's drinking and dancing. I know that it sounds like work, but it's not. I swear!" % roosterNickLily.split("@")[1])


elif roosterState == "ep9_4":
    if ep9_camila_lewd:
        $ new_rooster_int = 3
    else:
        $ new_rooster_int = 2

    if ep9_scary_stories or ep9_haunted_mansion:

        if (ep9_body_shots and ep9_shot_win) or (ep9_drink_win == "Becky" and ep9_drinking_competition):
            $ add_new_rooster_post("becky","This party is amazing!!! Who's with me? Yours truly even won the drinking game! {color=#00a0e6}#BestNurse{/color}",65,"ep9_cluck_photo_becky2","rooster_section_becky2_ep9")
        else:
            $ add_new_rooster_post("becky","Despite costume idea-stealing bitches - who shall remain nameless - this party is amazing!!! Who's with me? {color=#00a0e6}#BestNurse{/color}",65,"ep9_cluck_photo_becky2","rooster_section_becky2_ep9")
        $ add_rooster_comment("jacob","You sound surprised. We're the fucking DIKs!",55)
        if ep9_sally_drink:
            $ add_rooster_comment("sally","[name] makes mean drinks! WOO!",5)
        $ add_rooster_comment("tiffani","EVERYBODY! LET'S GET NAKED!!!",25)
        $ add_rooster_comment("kylie","Meh.",2)
        $ add_rooster_comment("tara","I'm having a blast! The drinks are amazing!",10)
        $ add_rooster_comment("becky","{color=#00a0e6}@%s{/color} Totes!!!" % roosterNickTara.split("@")[1],8)
        $ add_rooster_comment("derek","{color=#00a0e6}@%s{/color} I'm out of dipping sauce!" % roosterNickJohnBoy.split("@")[1],10)
        if ep9_sally_drink:
            $ add_rooster_comment("quinn","{color=#00a0e6}@%s{/color} You're hammered, huh?" % roosterNickSally.split("@")[1],3)
        $ add_rooster_comment("johnboy","{color=#00a0e6}@%s{/color} There's no more; you already took what I made." % roosterNickDerek.split("@")[1],2)
        if (ep9_body_shots and ep9_shot_win) or (ep9_drink_win == "Becky" and ep9_drinking_competition):
            $ add_rooster_comment("christie","{color=#00a0e6}@%s{/color} You must have cheated." % roosterNickBecky.split("@")[1],5)
        else:
            $ add_rooster_comment("christie","{color=#00a0e6}@%s{/color} Wow! This nameless bitch isn't taking offense. None whatsoever." % roosterNickBecky.split("@")[1],4)
        $ add_rooster_comment("melanie","Best Halloween party ever!",26)
        $ add_rooster_comment("leon","{color=#00a0e6}@%s{/color} Where are you?" % roosterNickTiffani.split("@")[1],3)
        $ add_rooster_comment("jamie","Anyone seen Rusty? I can't find him.",6)
        $ add_rooster_comment("derek","{color=#00a0e6}@%s{/color} I found some in the fridge. I'll make it work!" % roosterNickJohnBoy.split("@")[1],2)
        $ add_rooster_comment("johnboy","{color=#00a0e6}@%s{/color} There's no sauce in the fridge. What did you find?" % roosterNickDerek.split("@")[1],1)
        $ add_rooster_comment("melanie","{color=#00a0e6}@%s{/color} He was in the basement earlier." % roosterNickJamie.split("@")[1],1)
        $ add_rooster_comment("jamie","{color=#00a0e6}@%s{/color} Rusty? Where are you?" % roosterNickRusty.split("@")[1],0)
        $ add_rooster_comment("becky","Fuck this party! Who the fuck turned the lights off!? My costume is ruined!!!",2)
    else:


        $ add_new_rooster_post("becky","This party is kinda lame. Who's with me? {color=#00a0e6}#BestNurse{/color}",22,"ep9_cluck_photo_becky","rooster_section_becky_ep9")


        $ add_rooster_comment("clara","Lame? I don't know. But overhyped, for sure.",5)
        $ add_rooster_comment("kylie","Could be better. A lot better, actually.",3)
        $ add_rooster_comment("quinn","{color=#00a0e6}@%s @%s{/color} Shut up, you salty and ungrateful bitches." % (roosterNickClara.split("@")[1],roosterNickKylie.split("@")[1]),7)
        $ add_rooster_comment("derek","{color=#00a0e6}@%s{/color} I'm out of dipping sauce!" % roosterNickJohnBoy.split("@")[1],10)
        $ add_rooster_comment("johnboy","{color=#00a0e6}@%s{/color} There's no more; you already took what I made." % roosterNickDerek.split("@")[1],2)
        $ add_rooster_comment("clara","{color=#00a0e6}@%s{/color} Well, fuck you too." % roosterNickQuinn.split("@")[1],3)
        $ add_rooster_comment("sage","Calm down; we all worked hard for this party. Grab a drink and head downstairs to the dance floor instead of sulking on Rooster.",32)
        $ add_rooster_comment("jamie","Anyone seen Rusty? I can't find him.",6)
        $ add_rooster_comment("derek","{color=#00a0e6}@%s{/color} I found some in the fridge. I'll make it work!" % roosterNickJohnBoy.split("@")[1],2)
        $ add_rooster_comment("johnboy","{color=#00a0e6}@%s{/color} There's no sauce in the fridge. What did you find?" % roosterNickDerek.split("@")[1],1)
        $ add_rooster_comment("melanie","{color=#00a0e6}@%s{/color} He was in the basement earlier." % roosterNickJamie.split("@")[1],1)
        $ add_rooster_comment("jamie","{color=#00a0e6}@%s{/color} Rusty? Where are you?" % roosterNickRusty.split("@")[1],0)
        $ add_rooster_comment("becky","Fuck this party! Who the fuck turned the lights off!? My costume is ruined!!!",2)


    if ep9_camila_lewd:

        $ add_new_rooster_post("camila","When your favorite song hits differently than before. {color=#00a0e6}#DanceFloorVirgins{/color}",34,"ep9_cluck_photo_camila","rooster_section_camila_ep9")



        $ add_rooster_comment("riona","Pretty!",15)
        $ add_rooster_comment("melanie","The dance floor is all right tonight! Great music!",21)
        $ add_rooster_comment("sage","Shake your butt!",8)
        $ add_rooster_comment("johnboy","Let's dance! Elena and I have been sweating here for an hour now!",8)
        $ add_rooster_comment("sarah","{color=#00a0e6}@%s{/color} Don't shake it too hard, or there will be an earthquake." % roosterNickSage.split("@")[1],5)
        $ add_rooster_comment("elena","Is that the song title?",2)
        $ add_rooster_comment("camila","{color=#00a0e6}@%s{/color} Maybe? It's a tune with a great groove and bass." % roosterNickElena.split("@")[1],10)

        $ add_rooster_choice("{color=#00a0e6}@%s{/color} Amazing rhythm too! Makes me wanna dance to it again." % roosterNickCamila.split("@")[1])
        $ add_rooster_choice("{color=#00a0e6}@%s{/color} Such a tight beat. Tight, tight, tight." % roosterNickCamila.split("@")[1])



    $ add_new_rooster_post("karen","What is going on? I can't see anything. Does anyone know? {color=#00a0e6}#DIKsHalloween{/color}",13,"ep9_cluck_photo_karen","rooster_section_karen_ep9")



    $ add_rooster_comment("sally","Where are you?",1)
    $ add_rooster_comment("jacob","Stay calm and stay put, everyone. Don't panic. It's just a blackout; we're looking into it.",10)
    $ add_rooster_comment("maya","[name] is on his way to the basement to check.",6)
    $ add_rooster_comment("karen","{color=#00a0e6}@%s{/color} In the big room with stairs." % roosterNickSally.split("@")[1],1)
    $ add_rooster_comment("karen","{color=#00a0e6}@%s{/color} It's on again! What was it?" % roosterNickJacob.split("@")[1],1)
    $ add_rooster_comment("jacob","I don't know what it was, but [name] fixed it.",8)
    $ add_rooster_comment("maya","{color=#00a0e6}@%s{/color} Such electrician. Big wow!" % roosterNickMC.split("@")[1],6)

    $ add_rooster_choice("Nothing to worry about. Party on like there's no tomorrow!")
    $ add_rooster_choice("{color=#00a0e6}@%s{/color} You're drunk." % roosterNickMaya.split("@")[1])

elif roosterState == "ep9_5":
    if ep9_maya_cluck > 0:
        $ new_rooster_int += 1
    if ep9_josy_cluck > 0:
        $ new_rooster_int += 1

    if ep9_maya_cluck > 0:

        $ add_new_rooster_post("maya","Look at my soft and smooth feet. Aren't they pretty? {color=#00a0e6}#ILoveFeet{/color}",35,"ep9_cluck_photo_maya","rooster_section_maya_ep9")
        $ add_rooster_comment("elena","Hahaha! What is this?",12)
        $ add_rooster_comment("jacob","{color=#00a0e6}@%s{/color} I think she needs your help." % roosterNickDerek.split("@")[1],3)
        $ add_rooster_comment("sage","Haha! What the fuck is this? How much did you drink?",15)
        $ add_rooster_comment("camila","WOOOOO!!!",8)
        $ add_rooster_comment("derek","Huh!? Sis?",2)
        $ add_rooster_comment("ashley","LOL!",5)
        $ add_rooster_comment("maya","{color=#00a0e6}@%s{/color} We were playing a drinking game, and [name] dared me to do this." % roosterNickDerek.split("@")[1],9)
        $ add_rooster_comment("leon","{color=#00a0e6}@%s{/color} You sure were. LOL!" % roosterNickMaya.split("@")[1],2)
        $ add_rooster_comment("maya","{color=#00a0e6}@%s{/color} Sorry about that." % roosterNickLeon.split("@")[1],1)

    if ep9_josy_cluck > 0:

        if ep9_josy_cluck == 1:
            $ add_new_rooster_post("josy","The DIKs' party is awesome, but I'm a bit sad I didn't bring more condoms. {color=#00a0e6}#TooManyHotGuys{/color}",55,"ep9_cluck_photo_josy","rooster_section_josy_ep9")
        else:
            $ add_new_rooster_post("josy","The DIKs' party is awesome, but I'm a bit sad I came dressed as a fairy, when I wanted to come as a baby with a diaper. {color=#00a0e6}#MeLikeyDiapers{/color}",57,"ep9_cluck_photo_josy","rooster_section_josy_ep9")


        if ep9_josy_cluck == 1:
            $ add_rooster_comment("sarah","Zero shame. Respect.",5)
            $ add_rooster_comment("riona","{color=#00a0e6}@%s{/color} Now, this is a cluck I can get behind. LOL!" % roosterNickJosy.split("@")[1],10)
            $ add_rooster_comment("tommy","{color=#00a0e6}@%s{/color} Remove this shit!" % roosterNickJosy.split("@")[1],0)
        else:
            $ add_rooster_comment("sarah","This screams Rooster-rape to me. Screenshotted anyway.",15)
            $ add_rooster_comment("elena","Haha! Totally!",2)
            $ add_rooster_comment("tommy","{color=#00a0e6}@%s{/color} Leon came dressed as a fairy too." % roosterNickJosy.split("@")[1],7)

        $ add_rooster_comment("melanie","Literal LOL! Haha!",15)
        if ep9_maya_cluck > 0:
            $ add_rooster_comment("sage","Haha! You're playing that drinking game with Maya, aren't you? Those are two very suspicious clucks.",10)
            if ep9_josy_cluck == 1:
                $ add_rooster_comment("derek","{color=#00a0e6}@%s{/color} Rubbers suck." % roosterNickJosy.split("@")[1],11)
                $ add_rooster_comment("maya","{color=#00a0e6}@%s{/color} Mine was a joke, but I don't think Josy's is." % roosterNickSage.split("@")[1],2)
            else:
                $ add_rooster_comment("maya","{color=#00a0e6}@%s{/color} Mine was a joke, but I think Josy does like diapers." % roosterNickSage.split("@")[1],2)
            $ add_rooster_comment("sage","{color=#00a0e6}@%s{/color} LOL!" % roosterNickMaya.split("@")[1],2)
        else:
            $ add_rooster_comment("sage","Haha! Who put you up to this?",8)
        if ep9_josy_cluck == 2:
            $ add_rooster_comment("leon","{color=#00a0e6}@%s{/color} Fuck you!" % roosterNickTommy.split("@")[1],3)
        else:
            $ add_rooster_comment("tiffani","{color=#00a0e6}@%s{/color} So true! Aside from this one guy who showed me his dick." % roosterNickJosy.split("@")[1],4)

        if ep9_josy_cluck == 1:
            $ add_rooster_comment("johnboy","I keep some under my pillow if you need them.",10)
        else:
            $ add_rooster_comment("johnboy","It must be getting late when these clucks start showing on my feed.",8)
elif roosterState == "ep10_1":
    $ new_rooster_int = 2
    if (ep8_leons_side and not ep9_leons_side) or (not ep8_leons_side and ep9_leons_side):
        $ new_rooster_int += 1

        $ add_new_rooster_post("leon","NEXT HOUR ONLY! 2-FOR-1 SPECIAL! LMAO! {color=#00a0e6}#PINKROSE #GIRLPOWER{/color}",335,"ep10_cluck_photo_leon","rooster_section_leon_ep10")
        $ add_rooster_comment("jamie","{color=#00a0e6}@%s{/color} {color=#00a0e6}@%s{/color} We are you! LMFAO!" % (roosterNickLily.split("@")[1],roosterNickEnvy.split("@")[1]),52)
        $ add_rooster_comment("tommy","At what point can we kick a DIK out of the frat?",15)
        $ add_rooster_comment("jacob","{color=#00a0e6}@%s{/color} This won't age well." % roosterNickLeon.split("@")[1],13)
        $ add_rooster_comment("johnboy","I'm scared to ask what the 2-for-1 special is.",20)
        $ add_rooster_comment("quinn","Anyone got some eye bleach? I feel like my eyes got raped.",12)
        $ add_rooster_comment("leon","{color=#00a0e6}@%s{/color} WE WILL GRIND YOUR COCK TO A SONG OF YOUR CHOICE! LMAO!" % roosterNickJohnBoy.split("@")[1],53)
        $ add_rooster_comment("lily","{color=#00a0e6}@%s{/color} Are you ignoring it, too?" % roosterNickEnvy.split("@")[1],39)
        $ add_rooster_comment("envy","{color=#00a0e6}@%s{/color} I'm torn between blocking Jamie and Leon and muting the cluck at the moment." % roosterNickLily.split("@")[1],29)
        $ add_rooster_comment("sarah","Is anyone else sharing the fuck out of this cluck?",45)
        $ add_rooster_comment("rose","I knew we left too early!",15)
        $ add_rooster_comment("dawe","Buncha fags!",9)
        $ add_rooster_comment("sandy","{color=#00a0e6}@%s{/color} Haha! I don't know if you should feel flattered or have a life crisis." % roosterNickEnvy.split("@")[1],19)
        $ add_rooster_comment("elena","HELL YEAH! Sign me up for that special! WOOO!!!",29)
        if ep9_winner == "Leon":
            $ add_rooster_comment("kylie","LMAO! I still don't see why Leon won best costume with this.",20)
        $ add_rooster_comment("melanie","{color=#00a0e6}@%s{/color} HAHA! We got it trending in our area!" % roosterNickSarah.split("@")[1],41)
        $ add_rooster_comment("tara","{color=#00a0e6}@%s{/color} LOL!" % roosterNickLeon.split("@")[1],11)
        $ add_rooster_comment("leon","{color=#00a0e6}@%s{/color} WOOOO!" % roosterNickElena.split("@")[1],13)
        $ add_rooster_comment("jamie","{color=#00a0e6}@%s{/color} Looking at this today... Maybe we shouldn't have posted this..." % roosterNickLeon.split("@")[1],23)
        $ add_rooster_comment("jacob","{color=#00a0e6}@%s{/color} Called it." % roosterNickJamie.split("@")[1],8)

        $ add_rooster_choice("{color=#00a0e6}@%s{/color} {color=#00a0e6}@%s{/color} It's like looking into a mirror, isn't it?" % (roosterNickLily.split("@")[1],roosterNickEnvy.split("@")[1]))
        $ add_rooster_choice("How do I delete someone else's cluck?")
        $ add_rooster_choice("{color=#00a0e6}@DIKs{/color} I feel this has the potential to be a future Hell Week task. It would be more humiliating than wearing the dildo helmet, don't you think?")

    $ add_new_rooster_post("derek","I found this bag in my room. Is anyone missing it? It has some keys, $20, lipstick, and what I believe are too many tampons for one girl in it. {color=#00a0e6}#DIKsHalloween{/color}",35,"ep10_cluck_photo_derek","rooster_section_derek_ep10")
    $ add_rooster_comment("dany","{color=#00a0e6}@%s{/color} What the hell is that shirt? Are you seriously mocking my choice of pronoun?" % roosterNickDerek.split("@")[1],6)
    $ add_rooster_comment("derek","{color=#00a0e6}@%s{/color} Learn to read. The shirt literally says that I respect your pronoun. She/Her or whatever you made up to get triggered when someone gets it wrong." % roosterNickDany.split("@")[1],12)
    $ add_rooster_comment("dany","{color=#00a0e6}@%s{/color} THEM/THEY!" % roosterNickDerek.split("@")[1],7)
    $ add_rooster_comment("derek","{color=#00a0e6}@%s{/color} Ok, Ms. Them. You made your point. Go away." % roosterNickDany.split("@")[1],10)
    $ add_rooster_comment("dany","{color=#00a0e6}@%s{/color} I'm gonna block you!" % roosterNickDerek.split("@")[1],3)
    $ add_rooster_comment("derek","{color=#00a0e6}@%s{/color} Fucking do it already! You say you will every week, yet you keep showing up in my comment section!" % roosterNickDany.split("@")[1],10)
    $ add_rooster_comment("minny","{color=#00a0e6}@%s{/color} Are you for real!? You are a fucking idiot! That shirt is disgusting and offensive! And you are too! Learn how to respect people!" % roosterNickDerek.split("@")[1],3)
    $ add_rooster_comment("derek","{color=#00a0e6}@%s{/color} Practice what you preach!" % roosterNickMinny.split("@")[1],8)
    $ add_rooster_comment("suzy","{color=#00a0e6}@%s{/color} Those aren't even pronouns! Gender identity is not something you can make fun of, you dick! It's very personal and subject to change at any time! You should always ask people what they identify as and not assume gender." % roosterNickDerek.split("@")[1],3)
    $ add_rooster_comment("derek","{color=#00a0e6}@%s{/color} Don't call me dick. It's Huge Cock." % roosterNickSuzy.split("@")[1],7)
    $ add_rooster_comment("dany","{color=#00a0e6}@%s{/color} Suzy has a point, and you should read it!" % roosterNickDerek.split("@")[1],3)
    $ add_rooster_comment("derek","{color=#00a0e6}@%s{/color} I did read it, but none of you are respecting my made-up choice of pronouns; they are just as valid as yours. You're just a bunch of hypocrites. And there's nothing in this world you can't make fun of; everything is fair game." % roosterNickDany.split("@")[1],10)
    $ add_rooster_comment("minny","{color=#00a0e6}@%s{/color} FUCK YOU! Don't you dare make fun of gender issues! It's not a joking matter!!!" % roosterNickDerek.split("@")[1],8)
    $ add_rooster_comment("derek","{color=#00a0e6}@%s{/color} I think it is. And you girls could use a laugh." % roosterNickMinny.split("@")[1],12)
    $ add_rooster_comment("suzy","{color=#00a0e6}@%s{/color} Reported for sexual harassment! Enjoy your ban!" % roosterNickDerek.split("@")[1],3)
    $ add_rooster_comment("dany","{color=#00a0e6}@%s{/color} Me too!" % roosterNickSuzy.split("@")[1],2)
    $ add_rooster_comment("christie","{color=#00a0e6}@%s{/color} I kinda feel like I'm interrupting something here, but that's Nikita's bag." % roosterNickDerek.split("@")[1],3)
    $ add_rooster_comment("derek","{color=#00a0e6}@%s{/color} Thank you! Tell her she can get it whenever she wants it." % roosterNickChristie.split("@")[1],2)
    $ add_rooster_comment("suzy","{color=#00a0e6}@%s{/color} DON'T ASSUME GENDERS!" % roosterNickDerek.split("@")[1],3)
    $ add_rooster_comment("christie","{color=#00a0e6}@%s{/color} Um... But Nikita is a girl." % roosterNickSuzy.split("@")[1],3)
    $ add_rooster_comment("derek","{color=#00a0e6}@%s{/color} Oh my God, you've done it now, Christie. Run, Christie! Run!" % roosterNickChristie.split("@")[1],2)

    $ add_rooster_choice("{color=#00a0e6}@%s{/color} Try to ignore them next time, bro." % roosterNickDerek.split("@")[1])
    $ add_rooster_choice("{color=#00a0e6}@%s{/color} I knew that shirt was gonna get you into trouble." % roosterNickDerek.split("@")[1])

    if branchSage:
        $ new_rooster_int += 1

        $ add_new_rooster_post("tybalt","WHO DID THIS!? I DEMAND ANSWERS!",25,"ep10_cluck_photo_tybalt","rooster_section_tybalt_ep10")
        $ add_rooster_comment("trent","{color=#00a0e6}@%s{/color} Is that pumpkin pulp?" % roosterNickTybalt.split("@")[1],3)
        $ add_rooster_comment("tybalt","{color=#00a0e6}@%s{/color} It is! I was about to sleep when I noticed something wet and sticky, and now I'm furious! I had to call and wake up the maid to replace the sheets and everything!" % roosterNickTrent.split("@")[1],1)
        $ add_rooster_comment("christian","{color=#00a0e6}@%s{/color} Did you see this?" % roosterNickLucas.split("@")[1],2)
        $ add_rooster_comment("lucas","{color=#00a0e6}@%s{/color} Sure did. Isn't it horrible?" % roosterNickChristian.split("@")[1],2)
        $ add_rooster_comment("christian","{color=#00a0e6}@%s{/color} Yes, I can't wait to talk to you about how horrible this is. I bet Gogo will find it horrible, too." % roosterNickLucas.split("@")[1],2)
        $ add_rooster_comment("tyballs","BAHAHA! You actually lay down in it? You, sir, are a moron. I hope you enjoyed my gift.",12)
        $ add_rooster_comment("tybalt","{color=#00a0e6}@%s{/color} YOU DID THIS! WHO ARE YOU!? I will find you, and when I do, I will send you the bill for ruining my favorite silk pajamas and sheets!" % roosterNickTyballs.split("@")[1],1)
        $ add_rooster_comment("lucas","{color=#00a0e6}@%s{/color} Haha!" % roosterNickChristian.split("@")[1],2)
        $ add_rooster_comment("tyballs","{color=#00a0e6}@%s{/color} I could be anyone, but I'm likely someone very close to you. I wouldn't trust any of your so-called friends if I were you." % roosterNickTybalt.split("@")[1],2)
        $ add_rooster_comment("tybalt","SOMEONE HAS TO CONFESS AT THIS INSTANT!",1)


    $ add_new_rooster_post("riona","Halloween's over, but somehow people woke up looking scarier than last night. Here's hoping that a hot shower can fix it. {color=#00a0e6}#TooTiredToClean #KillMeNow{/color}",41,"ep10_cluck_photo_riona","rooster_section_riona_ep10")
    $ add_rooster_comment("camila","My head hurts. Can someone bring me coffee?",4)
    $ add_rooster_comment("elena","{color=#00a0e6}@%s{/color} Coming!" % roosterNickCamila.split("@")[1],2)
    $ add_rooster_comment("sage","{color=#00a0e6}@%s{/color} Guess it's still Halloween at the HOTs, haha. Everyone looks like zombies today." % roosterNickRiona.split("@")[1],10)
    $ add_rooster_comment("ashley","{color=#00a0e6}@%s{/color} Last night wasn't fun, but at least I'm not hungover today." % roosterNickRiona.split("@")[1],4)
    $ add_rooster_comment("sarah","{color=#00a0e6}@%s{/color} Ugh... Brag much?" % roosterNickAshley.split("@")[1],2)
    if ep9_sarah_melanie_lewd:
        $ add_rooster_comment("melanie","{color=#00a0e6}@%s{/color} My morning's been pretty good so far. {color=#00a0e6}#RiseAndShine{/color}" % roosterNickSarah.split("@")[1],2)
    $ add_rooster_comment("lily","{color=#00a0e6}@%s{/color} Can we save the cleaning until Monday or something?" % roosterNickSage.split("@")[1],6)
    if branchSage:
        $ add_rooster_comment("sage","{color=#00a0e6}@%s{/color} No, we can't. It wouldn't feel fair to leave the DIKs' place looking like that. Although they kinda deserve it after this morning." % roosterNickLily.split("@")[1],10)
    else:
        $ add_rooster_comment("sage","{color=#00a0e6}@%s{/color} No, we can't. It wouldn't feel fair to leave the DIKs' place looking like that." % roosterNickLily.split("@")[1],10)
    if ep9_sarah_melanie_lewd:
        $ add_rooster_comment("sarah","{color=#00a0e6}@%s{/color} Slut." % roosterNickMelanie.split("@")[1],1)
    if branchSage:
        $ add_rooster_comment("tommy","{color=#00a0e6}@%s{/color} We take it back. Please, come help us clean." % roosterNickSage.split("@")[1],4)
        $ add_rooster_comment("sage","{color=#00a0e6}@%s{/color} Tommy saying please and begging? That's a first. Don't worry, we'll come." % roosterNickTommy.split("@")[1],4)
elif roosterState == "ep10_2":
    $ new_rooster_int = 3
    if ep10_lily_english:
        $ new_rooster_int += 1

        $ add_new_rooster_post("lily","Show me your colors, and I'll show you mine. Orange and black is where it's at. {color=#00a0e6}#DIKGIRL{/color}",57,"ep10_cluck_photo_lily","rooster_section_lily_ep10")

        $ add_rooster_comment("sage","Whose jacket did you steal?",15)
        $ add_rooster_comment("jamie","{color=#00a0e6}@%s{/color} Wasn't your jacket missing?" % roosterNickJacob.split("@")[1],2)
        $ add_rooster_comment("jacob","{color=#00a0e6}@%s{/color} I got it back. Becky borrowed it, but now I have to wash it." % roosterNickJamie.split("@")[1],3)
        $ add_rooster_comment("derek","{color=#00a0e6}@%s{/color} Yeah, Becky's kinda nasty." % roosterNickJacob.split("@")[1],7)
        $ add_rooster_comment("becky","{color=#00a0e6}@%s{/color} I wouldn't touch your disgusting ass with a ten-foot pole!" % roosterNickDerek.split("@")[1],11)
        if not ep9_body_shots_becky and ep9_body_shots:
            $ add_rooster_comment("derek","{color=#00a0e6}@%s{/color} Yeah? Sleep well knowing you had my ass inches from your lips." % roosterNickBecky.split("@")[1],7)
        $ add_rooster_comment("envy","You look amazing, as always.",25)
        $ add_rooster_comment("leon","I wish that was my jacket...",3)
        $ add_rooster_comment("lily","{color=#00a0e6}@%s{/color} MWAH! You would too." % roosterNickEnvy.split("@")[1],39)
        $ add_rooster_comment("alex","Blue and white are better! Throw that rag away and use my jacket, baby.",9)
        $ add_rooster_comment("sarah","Someone found a boy toy from the looks of it.",15)
        $ add_rooster_comment("jimmy","You'd look hotter in my jacket.",2)
        $ add_rooster_comment("alex","{color=#00a0e6}@%s{/color} Back off. I called dibs on Lily a long time ago." % roosterNickJimmy.split("@")[1],4)
        $ add_rooster_comment("lily","{color=#00a0e6}@%s{/color} {color=#00a0e6}@%s{/color} Oh, guys. Neither of you could satisfy me." % (roosterNickAlex.split("@")[1],roosterNickJimmy.split("@")[1]),20)
        $ add_rooster_comment("tommy","{color=#00a0e6}@%s{/color} Oof! Are you cheating on me with a brother?" % roosterNickLily.split("@")[1],3)

        $ add_rooster_choice("{color=#00a0e6}@%s{/color} You look amazing with and without it." % roosterNickLily.split("@")[1])
        $ add_rooster_choice("{color=#00a0e6}@%s{/color} Nice selfie, Queen." % roosterNickLily.split("@")[1])
        if affinity == "DIK":
            $ add_rooster_choice("{color=#00a0e6}@%s{/color} Don't be jealous. If you ask nicely, I'm sure she's got a couple of inches of me to spare." % roosterNickSarah.split("@")[1])


    $ add_new_rooster_post("sarah","What's up with these posters, guys? Zero shame, huh? {color=#00a0e6}#DIKs{/color}",31,"ep10_cluck_photo_sarah","rooster_section_sarah_ep10")

    $ add_rooster_comment("tiffani","The elephant in the room question is, who's the guy with the big one? Haha! It's Leon, isn't it?",6)
    $ add_rooster_comment("alex","Zero shame for sure. Such a joke of a frat.",8)
    if ep7_ruined_presentation and (pathSage or ep7_pathSage):
        $ add_rooster_comment("christie","{color=#00a0e6}@%s{/color} I don't think it could be Leon. From what I know, it's probably [name]." % roosterNickTiffani.split("@")[1],3)
    else:
        $ add_rooster_comment("christie","{color=#00a0e6}@%s{/color} I don't think it could be Leon. Maybe it's [name]." % roosterNickTiffani.split("@")[1],3)
    if ep7_becky_lewd:
        $ add_rooster_comment("becky","{color=#00a0e6}@%s{/color} It could be him, yeah." % roosterNickChristie.split("@")[1],3)
    else:
        $ add_rooster_comment("becky","{color=#00a0e6}@%s{/color} Do you think it's him!?" % roosterNickChristie.split("@")[1],3)

    $ add_rooster_comment("dawe","You wouldn't catch our cocks plastered all around campus, is all I'm saying.",8)
    $ add_rooster_comment("kylie","{color=#00a0e6}@%s{/color} The one with no body hair, yeah?" % roosterNickChristie.split("@")[1],4)
    $ add_rooster_comment("arieth","{color=#00a0e6}@%s{/color} Does the printer not enlarge a photo that much?" % roosterNickDawe.split("@")[1],12)
    $ add_rooster_comment("sarah","{color=#00a0e6}@%s{/color} HAHAHA! OMG!" % roosterNickArieth.split("@")[1],10)
    $ add_rooster_comment("dawe","{color=#00a0e6}@%s{/color} ARIETH! DELETE THAT!" % roosterNickArieth.split("@")[1],8)
    $ add_rooster_comment("tiffani","{color=#00a0e6}@%s{/color} Interesting..." % roosterNickChristie.split("@")[1],5)
    $ add_rooster_comment("leon","{color=#00a0e6}@%s{/color} Yes! It's me!" % roosterNickTiffani.split("@")[1],3)
    $ add_rooster_comment("tiffani","{color=#00a0e6}@%s{/color} Oh! Hi!" % roosterNickLeon.split("@")[1],2)
    $ add_rooster_comment("sarah","{color=#00a0e6}@%s{/color} Haha! He's lying. It's not him." % roosterNickTiffani.split("@")[1],2)
    $ add_rooster_comment("dawe","{color=#00a0e6}@%s{/color} ARIETH!!!" % roosterNickArieth.split("@")[1],5)
    $ add_rooster_comment("rusty","It's not our work. Any help finding out who's doing this to us will be rewarded.",12)
    $ add_rooster_comment("arieth","{color=#00a0e6}@%s{/color} I can't delete Sarah's post, dummy. And I've got bigger things to worry about right now. Does anyone know how much your stomach grows when you're pregnant and if dieting will make it more balanced so that no one notices? I'm asking for a friend." % roosterNickDawe.split("@")[1],5)
    $ add_rooster_comment("sage","{color=#00a0e6}@%s{/color} I'm thinking maybe you shouldn't spread those pictures further like this." % roosterNickSarah.split("@")[1],9)
    $ add_rooster_comment("sarah","{color=#00a0e6}@%s{/color} They have them proudly on display on one of their walls, you know?" % roosterNickSage.split("@")[1],2)



    $ add_new_rooster_post("dawe","The yearbook is so fucking stupid. This year, I gave the quote the treatment it deserved. LMAO! {color=#00a0e6}#TRIALPHASRULE{/color}",45,"ep10_cluck_photo_dawe","rooster_section_dawe_ep10")

    $ add_rooster_comment("anthony","It sucks that we have to do it every year. I swear, B&R got a boner for these things. I put the same thing as last year on mine.",12)
    $ add_rooster_comment("alex","Meh. I didn't even bother with the quote. It's not like you're forced to write one.",8)
    $ add_rooster_comment("john","I'm not shelling out $20 for a book full of nobodies. Who even gives a crap?",5)
    $ add_rooster_comment("jimmy","{color=#00a0e6}@%s{/color} There are hot chicks in it, you know? It's good fap material." % roosterNickJohn.split("@")[1],4)
    $ add_rooster_comment("darius","{color=#00a0e6}@%s{/color} What did you write?" % roosterNickDawe.split("@")[1],2)
    $ add_rooster_comment("arieth","{color=#00a0e6}@%s{/color} What I hate the most about the yearbook is the freaking character limit for the quote. How can I write something inspiring and smart using so few letters? Like, come on, yearbook publishing people! Gimme a freaking break! It's the same with Rooster! The character limit for my messages is way too l" % roosterNickDawe.split("@")[1],14)
    $ add_rooster_comment("dawe","{color=#00a0e6}@%s{/color} You'll laugh. Trust me." % roosterNickDarius.split("@")[1],1)
    $ add_rooster_comment("ashley","{color=#00a0e6}@%s{/color} I fear my picture came out looking bad. What's the deal with one photo per student? Isn't this the digital age? Couldn't we at least get two shots and pick a favorite?" % roosterNickAnthony.split("@")[1],5)
    $ add_rooster_comment("caleb","Yearbook quotes suck. Those books are always full of try-hards.",8)


    $ add_new_rooster_post("elena","The Halloween pictures are done! You can download them {color=#00a0e6}here{/color}. Big thanks to {color=#00a0e6}@%s{/color} for his hard work on them. Tag your friends and enjoy! {color=#00a0e6}#Halloween #DIKs #HOTs{/color}" % roosterNickJacob.split("@")[1],225,"ep10_cluck_photo_elena","rooster_section_elena_ep10")

    $ add_rooster_comment("kylie","{color=#00a0e6}@%s{/color} How good does ours look!?" % roosterNickChristie.split("@")[1],7)
    $ add_rooster_comment("tara","Haha! You can't even tell it's me.",8)
    $ add_rooster_comment("christie","{color=#00a0e6}@%s{/color} I know, right?" % roosterNickKylie.split("@")[1],4)
    $ add_rooster_comment("tiffani","{color=#00a0e6}@%s{/color} Duh! Haha!" % roosterNickTara.split("@")[1],3)
    $ add_rooster_comment("becky","LMAO! I look hilarious in that one.",9)
    $ add_rooster_comment("tommy","{color=#00a0e6}@%s{/color} Two cocks at once, eh? Good to know." % roosterNickBecky.split("@")[1],4)
    $ add_rooster_comment("clara","Awesome! Haha!",5)
    $ add_rooster_comment("jacob","{color=#00a0e6}@%s{/color} How's she handling the bottles, though? I wouldn't want my dick to touch yours during a blowjob." % roosterNickTommy.split("@")[1],3)
    $ add_rooster_comment("tommy","{color=#00a0e6}@%s{/color} Yeah, that's an amateur way to do it, for sure." % roosterNickJacob.split("@")[1],2)
    if ep9_photos[9]:
        $ add_rooster_comment("riona","{color=#00a0e6}@%s{/color} Haha! There are so many cats in my photo. Nice touch!" % roosterNickJacob.split("@")[1],4)
    $ add_rooster_comment("ashley","{color=#00a0e6}@%s{/color} OMG, you look so good in your picture. It really looks like you're in space." % roosterNickDerek.split("@")[1],6)
    $ add_rooster_comment("derek","{color=#00a0e6}@%s{/color} Jacob did a hell of a job with it! {color=#00a0e6}@%s{/color} Where's the other shot?" % (roosterNickAshley.split("@")[1],roosterNickJacob.split("@")[1]),6)
    $ add_rooster_comment("johnboy","{color=#00a0e6}@%s{/color} We look so cool! You never cease to amaze me." % roosterNickElena.split("@")[1],8)
    $ add_rooster_comment("jacob","{color=#00a0e6}@%s{/color} I didn't use it. Your entire ass and asshole were showing." % roosterNickDerek.split("@")[1],8)
    $ add_rooster_comment("derek","{color=#00a0e6}@%s{/color} It's called mooning, bro. You missed the opportunity of a lifetime there." % roosterNickJacob.split("@")[1],6)
    $ add_rooster_comment("jacob","{color=#00a0e6}@%s{/color} Hell naw, I'm not retouching a pic of your asshole. My portfolio looks better without it." % roosterNickDerek.split("@")[1],4)
    if ep9_photos[16] or ep9_photos[17]:
        $ add_rooster_comment("becky","{color=#00a0e6}@%s @%s{/color} It looks like [name] can't keep his hands to himself in your picture." % (roosterNickSarah.split("@")[1],roosterNickMelanie.split("@")[1]),9)
    $ add_rooster_comment("elena","{color=#00a0e6}@%s{/color} <3" % roosterNickJohnBoy.split("@")[1],5)
    $ add_rooster_comment("lily","{color=#00a0e6}@%s @%s @%s @%s @%s{/color} Check it out, girls." % (roosterNickEnvy.split("@")[1],roosterNickSandy.split("@")[1],roosterNickRose.split("@")[1],roosterNickBrandi.split("@")[1],roosterNickTania.split("@")[1]),13)
    if ep9_photos[16] or ep9_photos[17]:
        $ add_rooster_comment("sarah","{color=#00a0e6}@%s{/color} He sure can't." % roosterNickBecky.split("@")[1],9)
        $ add_rooster_comment("melanie","{color=#00a0e6}@%s{/color} When we look hot like that, not many could." % roosterNickBecky.split("@")[1],9)
    $ add_rooster_comment("jamie","{color=#00a0e6}@%s{/color} Didn't I tell you it would come out awesome?" % roosterNickDany.split("@")[1],11)
    $ add_rooster_comment("sage","{color=#00a0e6}@%s{/color} Haha! Your picture is so good! If it weren't among the other pictures, I'd believe it was real." % roosterNickHeather.split("@")[1],15)
    $ add_rooster_comment("dany","{color=#00a0e6}@%s{/color} You can tell that the hat is out of focus. It's ok, not the best. At least Franz looks good in it." % roosterNickJamie.split("@")[1],4)
    $ add_rooster_comment("heather","{color=#00a0e6}@%s{/color} Yeah, it looks good." % roosterNickSage.split("@")[1],5)
    $ add_rooster_comment("jamie","{color=#00a0e6}@%s{/color} Maybe if you smiled, it would have been better..." % roosterNickDany.split("@")[1],7)
    if ep9_photos[14]:
        $ add_rooster_comment("zoey","{color=#00a0e6}@%s{/color} That's a rad picture of us! It looks like an epic battle in Hell." % roosterNickMC.split("@")[1],7)
        $ add_rooster_comment("jacob","{color=#00a0e6}@%s{/color} Right!?" % roosterNickZoey.split("@")[1],1)
        $ add_rooster_comment("jacob","{color=#00a0e6}@%s{/color} Oh, you meant you and [name]. I thought ours were cool as shit too!" % roosterNickZoey.split("@")[1],1)
    else:
        $ add_rooster_comment("jacob","{color=#00a0e6}@%s{/color} The album is uploaded!" % roosterNickZoey.split("@")[1],2)
        $ add_rooster_comment("zoey","{color=#00a0e6}@%s{/color} Awesome stuff!" % roosterNickJacob.split("@")[1],2)
    $ add_rooster_comment("sarah","{color=#00a0e6}@%s{/color} You won't work with Derek's asshole but have no problem scarring everyone with those horrible photos of Leon?" % roosterNickJacob.split("@")[1],13)
    if ep9_photos[15]:
        $ add_rooster_comment("maya","{color=#00a0e6}@%s @%s{/color} You guys took a photo together? I can't believe I missed that." % (roosterNickJosy.split("@")[1],roosterNickMC.split("@")[1]),1)
    $ add_rooster_comment("jacob","{color=#00a0e6}@%s{/color} It was either those pictures of Leon or no pictures of Leon. He snapped some that were even worse." % roosterNickSarah.split("@")[1],7)
    $ add_rooster_comment("karen","{color=#00a0e6}@%s{/color} You need to see our picture. Haha!" % roosterNickSally.split("@")[1],4)
    $ add_rooster_comment("quinn","{color=#00a0e6}@%s{/color} You should have gone with no pictures of Leon." % roosterNickJacob.split("@")[1],8)
    if ep9_photos[15]:
        $ add_rooster_comment("josy","{color=#00a0e6}@%s{/color} I think you were with Sage when we did." % roosterNickMaya.split("@")[1],1)

    $ add_rooster_comment("sage","{color=#00a0e6}@%s{/color} Did you see? Jacob put me in detention. LMAO!" % roosterNickMC.split("@")[1],14)
    $ add_rooster_comment("lily","{color=#00a0e6}@%s{/color} I'll have a hard time looking in the mirror after this." % roosterNickLeon.split("@")[1],9)
    $ add_rooster_comment("leon","{color=#00a0e6}@%s{/color} Join the club." % roosterNickLily.split("@")[1],7)
    if ep9_photos[7]:
        $ add_rooster_comment("sarah","{color=#00a0e6}@%s{/color} That's such a raunchy photo of you." % roosterNickQuinn.split("@")[1],12)
    if ep9_photos[5]:
        $ add_rooster_comment("maya","{color=#00a0e6}@%s{/color} Wow! It looks like we're tiny fairies in our picture!" % roosterNickMC.split("@")[1],6)
        $ add_rooster_comment("jacob","{color=#00a0e6}@%s{/color} I loved how you guys played with the perspective on that one! You made my job easy." % roosterNickMaya.split("@")[1],4)
    $ add_rooster_comment("sally","{color=#00a0e6}@%s{/color} Saving that one for sure." % roosterNickKaren.split("@")[1],3)
    $ add_rooster_comment("rusty","{color=#00a0e6}@%s{/color} Dude, yours is awesome. Scary as hell!" % roosterNickNick.split("@")[1],18)
    $ add_rooster_comment("penny","I'm loving these!",8)
    if ep9_photos[8]:
        $ add_rooster_comment("melanie","{color=#00a0e6}@%s{/color} LMAO! You look so pissed in your photo." % roosterNickQuinn.split("@")[1],7)
        $ add_rooster_comment("quinn","{color=#00a0e6}@%s{/color} [name] was a smartass. Look at his stupid grin." % roosterNickQuinn.split("@")[1],6)
    elif ep9_photos[7]:
        $ add_rooster_comment("melanie","{color=#00a0e6}@%s{/color} Is [name] really holding your breasts? You two are crazy." % roosterNickQuinn.split("@")[1],7)
        $ add_rooster_comment("quinn","{color=#00a0e6}@%s{/color} There's nothing crazy about it. If the yearbook allowed stuff like it, I'd do it there too." % roosterNickMelanie.split("@")[1],13)
    if ep9_photos[5]:
        $ add_rooster_comment("maya","{color=#00a0e6}@%s{/color} [name] came up with it. I was skeptical, but you guys proved me wrong. It's so good! Great job, Jacob!" % roosterNickJacob.split("@")[1],3)
        $ add_rooster_comment("josy","{color=#00a0e6}@%s{/color} Oh my God! I love love love it!" % roosterNickMC.split("@")[1],7)
    if ep9_photos[6]:
        $ add_rooster_comment("maya","{color=#00a0e6}@%s{/color} Aw! Those photos of us look so good!" % roosterNickMC.split("@")[1],9)
    if ep9_photos[4]:
        $ add_rooster_comment("jill","{color=#00a0e6}@%s{/color} Hahaha! Is that a dragon in the background? Such a surreal photo." % roosterNickMC.split("@")[1],6)
    $ add_rooster_comment("nick","{color=#00a0e6}@%s{/color} Right? It's like it's taken from a movie." % roosterNickRusty.split("@")[1],11)
    if ep9_photos[7]:
        $ add_rooster_comment("melanie","{color=#00a0e6}@%s{/color} LOL! Yeah, right." % roosterNickQuinn.split("@")[1],3)
    if ep9_photos[0] or ep9_photos[1]:
        $ add_rooster_comment("camila","{color=#00a0e6}@%s{/color} I look so hot! WOOO!!! Thanks for taking a picture of me." % roosterNickMC.split("@")[1],9)
    if ep9_photos[4]:
        $ add_rooster_comment("bianca","{color=#00a0e6}@%s{/color} These pictures are hilarious! Haha!" % roosterNickJill.split("@")[1],5)
    $ add_rooster_comment("envy","{color=#00a0e6}@%s{/color} OMG! That's such a great picture of us!" % roosterNickLily.split("@")[1],6)
    if ep9_photos[6]:
        $ add_rooster_comment("josy","{color=#00a0e6}@%s{/color} You look so strong in the picture where you're carrying us!" % roosterNickMC.split("@")[1],7)
    $ add_rooster_comment("rose","{color=#00a0e6}@%s{/color} Haha! I can't get over how good it looks!" % roosterNickLily.split("@")[1],4)
    if ep9_photos[9]:
        $ add_rooster_comment("camila","{color=#00a0e6}@%s{/color} You're so cute!!!" % roosterNickRiona.split("@")[1],4)


    $ add_rooster_choice("{color=#00a0e6}@%s @%s{/color} You two did an amazing job with this. Great idea and effort!" % (roosterNickJacob.split("@")[1],roosterNickElena.split("@")[1]))
    if affinity == "DIK":
        $ add_rooster_choice("{color=#00a0e6}@%s{/color} Detention for being a naughty girl." % roosterNickSage.split("@")[1])
    else:
        $ add_rooster_choice("{color=#00a0e6}@%s{/color} I bet you never got detention before in your life." % roosterNickSage.split("@")[1])

    if ep9_photos[4]:
        $ add_rooster_choice("{color=#00a0e6}@%s{/color} A dragon, a banana, and a warrior. Yep. Makes total sense." % roosterNickJill.split("@")[1])
    elif ep9_photos[5]:
        $ add_rooster_choice("{color=#00a0e6}@%s{/color} I knew it would come out looking great, but this was even better than I imagined it." % roosterNickMaya.split("@")[1])
    elif ep9_photos[6]:
        $ add_rooster_choice("{color=#00a0e6}@%s{/color} Look strong? I am strong. You two weren't that heavy, though." % roosterNickJosy.split("@")[1])
    elif ep9_photos[7] or ep9_photos[8]:
        $ add_rooster_choice("{color=#00a0e6}@%s{/color} I'm gonna print that photo and hang it on my wall." % roosterNickQuinn.split("@")[1])

elif roosterState == "ep10_3":
    $ new_rooster_int = 3

    $ add_new_rooster_post("dawe","{color=#00a0e6}@%s{/color} is back, and we are stronger than ever! {color=#00a0e6}@W&W{/color}, we're coming for that title! {color=#00a0e6}#TRIALPHA #METALMEN #BEASTMODE{/color}" % roosterNickChad.split("@")[1],34,"ep10_cluck_photo_dawe2","rooster_section_dawe2_ep10")

    $ add_rooster_comment("ww","Big words for a small college. History will repeat itself next year. The Stallions will reign supreme!",221)
    $ add_rooster_comment("anthony","{color=#00a0e6}@%s{/color} Nuh-uh!" % roosterNickWW.split("@")[1],12)
    $ add_rooster_comment("jimmy","{color=#00a0e6}@%s{/color} LOL! You shut him up good." % roosterNickAnthony.split("@")[1],8)

    $ add_rooster_comment("dawe","{color=#00a0e6}@%s{/color} Fuck your college! You'll see!" % roosterNickWW.split("@")[1],10)
    $ add_rooster_comment("caleb","{color=#00a0e6}@%s{/color} Let's beat them at the competition instead of in the comment section." % roosterNickDawe.split("@")[1],13)
    $ add_rooster_comment("chad","Thanks, man. Happy to be back.",21)
    $ add_rooster_comment("sage","{color=#00a0e6}@%s{/color} Are we good?" % roosterNickDawe.split("@")[1],5)
    $ add_rooster_comment("alex","Alphas rule!",11)
    $ add_rooster_comment("darius","Spartans were fewer in numbers, too! And they fucking won their wars!",10)
    $ add_rooster_comment("dawe","{color=#00a0e6}@%s{/color} For now." % roosterNickSage.split("@")[1],3)
    $ add_rooster_comment("john","{color=#00a0e6}@%s{/color} Hell yeah!" % roosterNickDarius.split("@")[1],8)
    $ add_rooster_comment("magnar","{color=#00a0e6}@%s{/color} If you're interested in learning why you're wrong, the library has many history books." % roosterNickDarius.split("@")[1],3)
    $ add_rooster_comment("darius","{color=#00a0e6}@%s{/color} Shut the fuck up, nerd!" % roosterNickMagnar.split("@")[1],5)


    if ep10_riona_date:
        $ new_rooster_int += 1
        $ add_new_rooster_post("riona","PEW PEW! I'm having fun slaying skin-eaters with this scared cutie. {color=#00a0e6}#gUndead #BLAM{/color}",28,"ep10_cluck_photo_riona2","rooster_section_riona2_ep10")
        $ add_rooster_comment("sarah","Ah, good! You found someone willing to go to that place. Now you can stop bothering me and Mel about it.",4)
        if ep10_gundead_win:
            $ add_rooster_comment("riona","{color=#00a0e6}@%s{/color} I definitely will, and it's your loss. [name] is awesome at shooting zombies, and he knows how to have fun." % roosterNickSarah.split("@")[1],3)
        else:
            $ add_rooster_comment("riona","{color=#00a0e6}@%s{/color} I definitely will, and it's your loss. [name] has a crappy aim with that gun, but at least he knows how to have fun." % roosterNickSarah.split("@")[1],3)
        if ep10_rio_animal:
            $ add_rooster_comment("riona","{color=#00a0e6}@%s{/color} And he won me a stuffed animal in one of those rigged claw machines!" % roosterNickSarah.split("@")[1],3)
        $ add_rooster_comment("sarah","{color=#00a0e6}@%s{/color} Arcade games aren't fun; they're childish, and there are way better things you can spend your money on." % roosterNickRiona.split("@")[1],5)
        $ add_rooster_comment("riona","{color=#00a0e6}@%s{/color} It must suck to be wrong this much, but it's fine; I know you don't know any better." % roosterNickSarah.split("@")[1],3)
        $ add_rooster_comment("sage","{color=#00a0e6}@%s{/color} I thought you were joking when you suggested that place. If I knew you weren't, I wouldn't have made fun of it." % roosterNickRiona.split("@")[1],8)
        $ add_rooster_comment("riona","{color=#00a0e6}@%s{/color} It's fine. I know you girls don't like this, but I do." % roosterNickSage.split("@")[1],6)
        $ add_rooster_comment("sage","{color=#00a0e6}@%s{/color} I like games. Let's go there together sometime." % roosterNickRiona.split("@")[1],5)
        $ add_rooster_comment("riona","{color=#00a0e6}@%s{/color} Do you mean it?" % roosterNickSage.split("@")[1],4)
        $ add_rooster_comment("sage","{color=#00a0e6}@%s{/color} Of course! And you do stuff for us all the time. I'd be happy to come along with you." % roosterNickRiona.split("@")[1],5)
        $ add_rooster_comment("camila","{color=#00a0e6}@%s{/color} I wanna play too!" % roosterNickRiona.split("@")[1],3)
        $ add_rooster_comment("riona","{color=#00a0e6}@%s{/color} That means a lot... Thanks!" % roosterNickSage.split("@")[1],6)

    if branchJill:
        $ new_rooster_int += 1
        $ add_new_rooster_post("jill","In a relationship with {color=#00a0e6}@%s #HAPPY{/color}" % roosterNickMC.split("@")[1],135,"ep10_cluck_photo_mc_jill","rooster_section_jill_ep10")

        if ep9_told_jill:
            $ add_rooster_comment("bianca","Awww!!! Congratulations! I love you two so much.",12)
        else:
            $ add_rooster_comment("bianca","Awww!!! Congratulations! You deserve each other.",12)

        $ add_rooster_comment("carla","I knew he was a Jill-guy from the moment I met him. Congratulations! I'm so happy for you.",10)
        $ add_rooster_comment("rich","Congratulations, Ms. Royce.",15)
        $ add_rooster_comment("christian","{color=#00a0e6}@%s{/color} Do you think he saw this yet?" % roosterNickLucas.split("@")[1],3)
        $ add_rooster_comment("isabella","Congratulations. You two make a great couple.",13)
        $ add_rooster_comment("trent","Congratulations!",12)
        $ add_rooster_comment("sage","Look at that... Congratulations!",15)
        $ add_rooster_comment("lucas","{color=#00a0e6}@%s{/color} I don't think he'll be playing cello tonight. Haha!" % roosterNickChristian.split("@")[1],3)
        if not ep9_told_jill:
            $ add_rooster_comment("olivia","Congratulations!",8)
        if not ep9_jm_sad:
            $ add_rooster_comment("maya","You look sweet together. Congrats!",7)

        $ add_rooster_choice("{color=#00a0e6}@%s{/color} That wasn't that scary, was it?" % roosterNickJill.split("@")[1])
        $ add_rooster_choice("{color=#00a0e6}@%s{/color}  {color=#00a0e6}#HAPPY{/color}" % roosterNickTybalt.split("@")[1])

    $ add_new_rooster_post("mc","It's official. There's no way to look good wearing a lab coat. The safety glasses don't exactly help. {color=#00a0e6}#GEEK{/color}",62,"ep10_cluck_photo_mc","rooster_section_mc_ep10")
    if branchMayaJosy:
        $ add_rooster_comment("josy","That's a sexy geek. GRR!",18)
    elif not branchMayaJosy and not pathMayaJosy:
        $ add_rooster_comment("josy","KABOOM?",5)
        $ add_rooster_comment("mc","{color=#00a0e6}@%s{/color} Haha, no! More like splish splash splosh. Derek messed around with the emergency shower." % roosterNickJosy.split("@")[1],5)
    $ add_rooster_comment("leon","Do you actually have to wear that?",7)
    if not branchMayaJosy and not pathMayaJosy:
        $ add_rooster_comment("derek","{color=#00a0e6}@%s{/color} I TESTED it. It's been verified to work. You're welcome." % roosterNickMC.split("@")[1],2)
    $ add_rooster_comment("quinn","Sure, you're just fishing for attention.",8)
    $ add_rooster_comment("becky","I think that looks hot.",12)
    $ add_rooster_comment("jamie","I think you look slick! Like a scientist or something.",4)
    $ add_rooster_comment("mc","{color=#00a0e6}@%s{/color} Sadly." % roosterNickLeon.split("@")[1],2)
    if branchJill:
        $ add_rooster_comment("jill","{color=#00a0e6}@%s{/color} That's so cute. Haha! I think you look very handsome in it." % roosterNickMC.split("@")[1],7)
    if branchMayaJosy:
        $ add_rooster_comment("maya","{color=#00a0e6}@%s{/color} You should insist on wearing a hazmat suit instead. At least that way, no one will see it's you." % roosterNickMC.split("@")[1],6)
    if branchSage:
        $ add_rooster_comment("sage","{color=#00a0e6}@%s{/color} This is the first time I've seen you wear protection. LMAO!" % roosterNickMC.split("@")[1],12)
        $ add_rooster_comment("mc","{color=#00a0e6}@%s{/color} Alright... Next time, I'll wear safety glasses with you, and you won't make these embarrassing comments." % roosterNickSage.split("@")[1],5)
    else:
        $ add_rooster_comment("sage","{color=#00a0e6}@%s{/color} The safety glasses aren't as bad as that gimp mask you wore." % roosterNickMC.split("@")[1],8)
        $ add_rooster_comment("mc","{color=#00a0e6}@%s{/color} Ouch! That's a low blow." % roosterNickSage.split("@")[1],5)

    if branchSage:
        $ new_rooster_int += 1
        $ add_new_rooster_post("mc","Having a night out with this lovely girl.",35,"ep10_cluck_photo_sage2","rooster_section_mc_sage_ep10")

        $ add_rooster_comment("leon","Cool! Enjoy it!",8)
        $ add_rooster_comment("jacob","Man! Sage looks amazing!",9)
        $ add_rooster_comment("johnboy","What a beauty!",7)
        $ add_rooster_comment("jamie","I almost didn't recognize her.",6)
        if ep8_mansion_won:
            $ add_rooster_comment("rusty","Oh! That's why you needed my car tonight.",6)
            $ add_rooster_comment("mc","{color=#00a0e6}@%s{/color} Thanks for letting me borrow it!" % roosterNickRusty.split("@")[1],5)
            $ add_rooster_comment("rusty","{color=#00a0e6}@%s{/color} Any time!" % roosterNickMC.split("@")[1],3)
        $ add_rooster_comment("nick","Have fun!",6)
        $ add_rooster_comment("tommy","Hehe! I know what you did to her.",3)
        $ add_rooster_comment("leon","{color=#00a0e6}@%s{/color} What did he do to her?" % roosterNickTommy.split("@")[1],2)
        $ add_rooster_comment("mc","{color=#00a0e6}@%s{/color} Grow up, dude." % roosterNickTommy.split("@")[1],3)
        if ep8_mansion_won:
            $ add_rooster_comment("jamie","{color=#00a0e6}@%s{/color} Can I borrow it, too?" % roosterNickRusty.split("@")[1],4)
            $ add_rooster_comment("rusty","{color=#00a0e6}@%s{/color} Let's talk about this later." % roosterNickJamie.split("@")[1],3)
        $ add_rooster_comment("heather","{color=#00a0e6}@%s{/color} Ordered pizza or what?" % roosterNickSage.split("@")[1],4)
        $ add_rooster_comment("sage","{color=#00a0e6}@%s{/color} Haha, I'll tell you all about it later." % roosterNickHeather.split("@")[1],3)
        $ add_rooster_comment("camila","{color=#00a0e6}@%s{/color} I wanna hear about it too!" % roosterNickSage.split("@")[1],3)
        $ add_rooster_comment("derek","{color=#00a0e6}@%s{/color} Wow! I never realized she...you know?" % roosterNickMC.split("@")[1],4)
        $ add_rooster_comment("leon","{color=#00a0e6}@%s{/color} I love pizza!" % roosterNickSage.split("@")[1],6)

        $ add_rooster_comment("mc","{color=#00a0e6}@%s{/color} Realized what?" % roosterNickDerek.split("@")[1],4)
        $ add_rooster_comment("derek","{color=#00a0e6}@%s{/color} Honk honk. You know?" % roosterNickMC.split("@")[1],6)
        if affinity == "DIK":
            $ add_rooster_comment("mc","{color=#00a0e6}@%s{/color} In caps. HONK HONK! Like a truck." % roosterNickDerek.split("@")[1],6)
            $ add_rooster_comment("derek","{color=#00a0e6}@%s{/color} LMAO! Right?" % roosterNickMC.split("@")[1],2)
            $ add_rooster_comment("sage","{color=#00a0e6}@%s{/color} [name]..." % roosterNickMC.split("@")[1],2)
        else:
            $ add_rooster_comment("mc","{color=#00a0e6}@%s{/color} Zip it." % roosterNickDerek.split("@")[1],3)

    $ add_new_rooster_post("sage","We're having a small get-together near the lake. If you're free and interested, drop by. {color=#00a0e6}#HOTs #PizzaParty{/color}",78,"ep10_cluck_photo_sage","rooster_section_sage_ep10")
    $ add_rooster_comment("sage","Welcome to the sisterhood, {color=#00a0e6}@%s{/color}!" % roosterNickMaya.split("@")[1],12)
    $ add_rooster_comment("tiffani","Oh! Shoot! I'd come, but I already went back home for Thanksgiving.",8)
    $ add_rooster_comment("tara","{color=#00a0e6}@%s{/color} Me too." % roosterNickTiffani.split("@")[1],6)
    $ add_rooster_comment("sage","{color=#00a0e6}@%s @%s{/color} There will be more fun times soon. Happy Thanksgiving!" % (roosterNickTiffani.split("@")[1],roosterNickTara.split("@")[1]),12)
    $ add_rooster_comment("becky","I'm so there! The DIKs are there too, right? Like, all of them?",5)
    if ep10_pp_meat == 2:
        $ add_rooster_comment("rusty","Save some pizza for me! We're about to eat now, too. But we're only having hot dogs.",8)
    elif ep10_pp_meat == 1:
        $ add_rooster_comment("rusty","Save some pizza for me! We're about to eat now, too. But I'm a bit unsure about the meat they bought.",8)
    else:
        $ add_rooster_comment("rusty","Pizza is good, but what the boys just put on the barbecue smells amazing! Come have some, if you want.",8)
    $ add_rooster_comment("jacob","Woho! Turn that music up.",6)
    $ add_rooster_comment("maya","Thanks for the party and the warm welcome!",10)
    $ add_rooster_comment("sarah","Sage forgot to mention it's freezing. No one is holding a gun to your head forcing you to show up. Stay at home instead. It's just us and the DIKs here.",3)
    $ add_rooster_comment("sally","{color=#00a0e6}@%s{/color} Can I come?" % roosterNickSage.split("@")[1],2)
    $ add_rooster_comment("sage","{color=#00a0e6}@%s{/color} Of course! There's a bonfire going, but dress warm." % roosterNickSally.split("@")[1],3)
    $ add_rooster_comment("elena","{color=#00a0e6}@%s{/color} You don't have to actively scare people away." % roosterNickSarah.split("@")[1],4)
    $ add_rooster_comment("dawe","{color=#00a0e6}@%s{/color} This counts as one party. I'm keeping tabs." % roosterNickSage.split("@")[1],3)
    $ add_rooster_comment("sage","{color=#00a0e6}@%s{/color} Nope. This is a HOTs-only party. And if you're going to keep tabs, you'll end up making this worse than it has to be. Happy Thanksgiving, Dawe." % roosterNickDawe.split("@")[1],6)
    $ add_rooster_comment("melanie","The DIKs are drunk already, like wow. That was fast!",3)
    $ add_rooster_comment("lily","{color=#00a0e6}@%s{/color} Haha, they're not drunk." % roosterNickMelanie.split("@")[1],2)
elif roosterState == "ep11_1":
    $ new_rooster_int = 2
    $ add_new_rooster_post("elena","Happy Thanksgiving! It's time to fatten up for winter. {color=#00a0e6}#ApplePie #Thanksgiving{/color}",44,"ep11_cluck_photo_elena","rooster_section_elena_ep11")
    $ add_rooster_comment("ashley","Happy Thanksgiving, everyone!",6)
    $ add_rooster_comment("camila","{color=#00a0e6}@%s{/color} Happy Thanksgiving! Is this weekend a slow burn for anyone else?" % roosterNickElena.split("@")[1],6)
    $ add_rooster_comment("josy","{color=#00a0e6}@%s{/color} Happy Thanksgiving! That pie looks delicious." % roosterNickElena.split("@")[1],9)
    $ add_rooster_comment("johnboy","{color=#00a0e6}@%s{/color} I miss you, baby." % roosterNickElena.split("@")[1],2)
    $ add_rooster_comment("jamie","I could go for some pie now too. We had vegan cake this year. I almost threw up. What the hell did eggs ever do to vegans?",5)
    $ add_rooster_comment("tiffani","{color=#00a0e6}@%s{/color} Happy Thanksgiving!" % roosterNickElena.split("@")[1],9)
    $ add_rooster_comment("sarah","{color=#00a0e6}@%s{/color} Shut it. I'd happily take another week of this. Don't tell me you're bored." % roosterNickCamila.split("@")[1],2)
    $ add_rooster_comment("camila","{color=#00a0e6}@%s{/color} I am. We're pretty much doing nothing this weekend." % roosterNickSarah.split("@")[1],2)
    $ add_rooster_comment("melanie","{color=#00a0e6}@%s{/color} Eggs are animal products, so they have to exclude those." % roosterNickJamie.split("@")[1],3)
    $ add_rooster_comment("lily","{color=#00a0e6}@%s{/color} Hard pass! If I did that, I'd probably get fired." % roosterNickElena.split("@")[1],4)
    $ add_rooster_comment("jamie","{color=#00a0e6}@%s{/color} What about milk!? A cow doesn't die from getting milked. Do vegans breastfeed? Hypocrites much?" % roosterNickMelanie.split("@")[1],2)
    $ add_rooster_comment("sage","{color=#00a0e6}@%s{/color} Happy Thanksgiving! I wouldn't mind a slice of that." % roosterNickElena.split("@")[1],7)
    $ add_rooster_comment("elena","{color=#00a0e6}@%s{/color} We ate it all. What's it called when you regret eating too much of something? Eater's remorse?" % roosterNickSage.split("@")[1],9)
    $ add_rooster_comment("elena","{color=#00a0e6}@%s{/color} I miss you too!" % roosterNickJohnBoy.split("@")[1],2)
    $ add_rooster_comment("melanie","{color=#00a0e6}@%s{/color} You're cute." % roosterNickJamie.split("@")[1],4)
    $ add_rooster_comment("arieth","{color=#00a0e6}@%s{/color} I don't want to get fatter! This baby is killing me." % roosterNickElena.split("@")[1],3)

    $ add_new_rooster_post("sage","Friends have the ability to turn a bad day into a good one. Thanks for the fun, {color=#00a0e6}@%s{/color}. {color=#00a0e6}#NailedIt{/color}" % roosterNickJill.split("@")[1],56,"ep11_cluck_photo_sage","rooster_section_sage_ep11")
    $ add_rooster_comment("jill","{color=#00a0e6}@%s{/color} I had a wonderful time with you. We should do it again." % roosterNickSage.split("@")[1],10)
    $ add_rooster_comment("camila","{color=#00a0e6}@%s{/color} That's a great picture of you two." % roosterNickSage.split("@")[1],5)
    $ add_rooster_comment("elena","{color=#00a0e6}@%s{/color} Did something bad happen?" % roosterNickSage.split("@")[1],4)
    $ add_rooster_comment("maya","{color=#00a0e6}@%s{/color} I hope you're feeling better." % roosterNickSage.split("@")[1],3)
    $ add_rooster_comment("sarah","{color=#00a0e6}@%s{/color} Since when are you two friends? What did I miss?" % roosterNickSage.split("@")[1],2)
    $ add_rooster_comment("sage","{color=#00a0e6}@%s{/color} DM" % roosterNickElena.split("@")[1],1)
    $ add_rooster_comment("sage","{color=#00a0e6}@%s{/color} Since the DIKs' Halloween party. Jill is awesome." % roosterNickSarah.split("@")[1],3)
    $ add_rooster_comment("josy","{color=#00a0e6}@%s{/color} You have to show me your nails later." % roosterNickSage.split("@")[1],2)
    $ add_rooster_comment("sage","{color=#00a0e6}@%s{/color} Totally!" % roosterNickJosy.split("@")[1],2)
    $ add_rooster_comment("tybalt","{color=#00a0e6}@%s{/color} Call me this instant!" % roosterNickSage.split("@")[1],1)

elif roosterState == "ep11_2":
    $ new_rooster_int = 2
    $ add_new_rooster_post("josy","Today's outfit. {color=#00a0e6}#WinterFashion #MsSunshine{/color}",186,"ep11_cluck_photo_josy","rooster_section_josy_ep11")
    $ add_rooster_comment("blogguy2","{color=#00a0e6}@%s{/color} Wow, you're so hot!" % roosterNickJosy.split("@")[1],40)
    $ add_rooster_comment("bloggirl1","{color=#00a0e6}@%s{/color} OMG! Where did you buy that? Do you have a promo code for it?" % roosterNickJosy.split("@")[1],29)
    $ add_rooster_comment("bloggirl2","{color=#00a0e6}@%s{/color} I love your hair." % roosterNickJosy.split("@")[1],19)
    $ add_rooster_comment("sage","{color=#00a0e6}@%s{/color} I wish I were your size. I'd totally borrow that. You're gorgeous!" % roosterNickJosy.split("@")[1],52)
    $ add_rooster_comment("ashley","{color=#00a0e6}@%s{/color} Love, love, love it!" % roosterNickJosy.split("@")[1],20)
    $ add_rooster_comment("isabella","{color=#00a0e6}@%s{/color} What a great photo." % roosterNickJosy.split("@")[1],14)
    $ add_rooster_comment("blogguy1","Who else came here from CB?",32)
    $ add_rooster_comment("bloguser2","See my pussy on my exclusive OnlyCake account ---> Link in bio! 50% off for the first month!",4)
    $ add_rooster_comment("bloggirl3","{color=#00a0e6}@%s{/color} FIERCE! I love your content." % roosterNickJosy.split("@")[1],24)
    $ add_rooster_comment("jimmy","{color=#00a0e6}@%s{/color} Daaamn!" % roosterNickJosy.split("@")[1],8)
    $ add_rooster_comment("jill","{color=#00a0e6}@%s{/color} I love those colors on you." % roosterNickJosy.split("@")[1],19)
    $ add_rooster_comment("lucas","{color=#00a0e6}@%s{/color} Cute." % roosterNickJosy.split("@")[1],12)
    $ add_rooster_comment("josy","{color=#00a0e6}@%s{/color} Thank you! It took me many tries to get the angle right." % roosterNickIsabella.split("@")[1],33)
    $ add_rooster_comment("bloggirl4","{color=#00a0e6}@%s{/color} You're stunning. I wish I could pull that outfit off. Thanks for being an inspiration." % roosterNickJosy.split("@")[1],16)
    $ add_rooster_comment("blogguy1","{color=#00a0e6}@%s{/color} Don't bother with this one; it's a porn site. Can some moderator clean this up?" % roosterNickBlogUser2.split("@")[1],7)
    $ add_rooster_comment("isabella","{color=#00a0e6}@%s{/color} Did you manage to shoot that photo on your own? You're very talented." % roosterNickJosy.split("@")[1],16)
    $ add_rooster_comment("bloguser1","GunzAndTittyCoin is up by 1040% in the last week! Join {color=#00a0e6}here{/color} for the next buy signal.",11)
    $ add_rooster_comment("maya","{color=#00a0e6}@%s{/color} What's going on in the comment section? Who are all these people?" % roosterNickJosy.split("@")[1],4)
    $ add_rooster_comment("heather","{color=#00a0e6}@%s{/color} What everyone else is saying. It suits you." % roosterNickJosy.split("@")[1],10)
    $ add_rooster_comment("josy","{color=#00a0e6}@%s{/color} :) I'll tell you later." % roosterNickMaya.split("@")[1],23)

    $ add_rooster_choice("{color=#00a0e6}@%s{/color} What a snitch. Free the nipple, dude." % roosterNickBlogGuy1.split("@")[1])
    if branchMayaJosy:
        $ add_rooster_choice("{color=#00a0e6}@%s @%s{/color} I'm not so sure all of them are actual people." % (roosterNickJosy.split("@")[1],roosterNickMaya.split("@")[1]))
    else:
        $ add_rooster_choice("{color=#00a0e6}@%s{/color} You've got some spam to clean up. Beware of what you click on." % roosterNickJosy.split("@")[1])
    $ add_new_rooster_post("lily","No Santa is coming down the chimney for these girls. {color=#00a0e6}#NaughtyGirls{/color}",57,"ep11_cluck_photo_lily","rooster_section_lily_ep11")
    $ add_rooster_comment("alex","{color=#00a0e6}@%s{/color} I'll come down the chimney for you, babe." % roosterNickLily.split("@")[1],13)
    $ add_rooster_comment("jimmy","{color=#00a0e6}@%s{/color} Bro, I'll fill that chimney with cum, and I'm not planning on waiting until Christmas! LMAO" % roosterNickAlex.split("@")[1],8)
    $ add_rooster_comment("darius","{color=#00a0e6}@%s{/color} Someone give her the tightest ass award! DAMN!" % roosterNickSarah.split("@")[1],14)
    $ add_rooster_comment("chad","{color=#00a0e6}@%s{/color} Hot AF." % roosterNickLily.split("@")[1],12)
    $ add_rooster_comment("dawe","{color=#00a0e6}@%s{/color} Who would you rather bang? Lily or Sarah?" % roosterNickChad.split("@")[1],7)
    $ add_rooster_comment("sage","{color=#00a0e6}@%s{/color} I see you girls not working over there." % roosterNickLily.split("@")[1],8)
    $ add_rooster_comment("dawe","{color=#00a0e6}@%s{/color} LMAO! Busted by Mama HOT." % roosterNickSage.split("@")[1],5)
    $ add_rooster_comment("sage","{color=#00a0e6}@%s{/color} Mama? I'd make you eat those words, BDD. And I don't mean your Rooster nick by that." % roosterNickDawe.split("@")[1],4)
    $ add_rooster_comment("anthony","{color=#00a0e6}@%s{/color} BDD? What's that?" % roosterNickSage.split("@")[1],5)
    $ add_rooster_comment("sage","{color=#00a0e6}@%s{/color} The first word is baby. I'll let you figure out the rest." % roosterNickAnthony.split("@")[1],7)
    $ add_rooster_comment("john","{color=#00a0e6}@%s{/color} That's an awesome question! I'd go for Sarah; she's just my kinda girl. I wanna hear what {color=#00a0e6}@%s{/color} thinks, though. I never got his type." % (roosterNickDawe.split("@")[1],roosterNickChad.split("@")[1]),9)
    $ add_rooster_comment("chad","{color=#00a0e6}@%s{/color} Just give me both at the same time." % roosterNickDawe.split("@")[1],14)
    $ add_rooster_comment("dawe","{color=#00a0e6}@%s{/color} Oh man, that would be sweet as hell! If I imagine them bouncing on my cock at the same time, I go crazy!" % roosterNickChad.split("@")[1],5)
    $ add_rooster_comment("sage","{color=#00a0e6}@%s{/color} Not possible. In more ways than one. {color=#00a0e6}#BDD{/color}" % roosterNickDawe.split("@")[1],3)
    $ add_rooster_comment("dawe","{color=#00a0e6}@%s{/color} I said I was sorry!" % roosterNickSage.split("@")[1],2)
    $ add_rooster_comment("sage","{color=#00a0e6}@%s{/color} No, you didn't." % roosterNickDawe.split("@")[1],2)

    $ add_rooster_choice("{color=#00a0e6}@%s{/color} Baby Dummy Dawe?" % roosterNickSage.split("@")[1])
    if branchAlone:
        $ add_rooster_choice("{color=#00a0e6}@%s{/color} Nice! Just what I wanted to find underneath my Christmas tree." % roosterNickSarah.split("@")[1])
    else:
        $ add_rooster_choice("{color=#00a0e6}@%s{/color} I hate to break this to you, Lily, but Santa isn't real. I'm sorry." % roosterNickLily.split("@")[1])

elif roosterState == "ep11_4":
    $ new_rooster_int = 3
    $ add_new_rooster_post("dany","Jamie is a vile and toxic monster! WARNING! Stay away from {color=#00a0e6}@%s{/color} at all costs! {color=#00a0e6}#MURDERER{/color}" % roosterNickJamie.split("@")[1],25,"ep11_cluck_photo_dany","rooster_section_dany_ep11")
    $ add_rooster_comment("linda","{color=#00a0e6}@%s{/color} He's also a filthy little burger thief who owes me big time!" % roosterNickDany.split("@")[1],3)
    $ add_rooster_comment("jamie","{color=#00a0e6}@%s{/color} What the hell!? I'm not a murderer. You can't just post that about me. That's slander!" % roosterNickDany.split("@")[1],8)
    $ add_rooster_comment("dany","{color=#00a0e6}@%s{/color} PEOPLE DESERVE TO KNOW THE TRUTH!" % roosterNickJamie.split("@")[1],5)
    $ add_rooster_comment("minny","{color=#00a0e6}#JUSTICEFORFRANZ{/color}",10)
    $ add_rooster_comment("suzy","{color=#00a0e6}@%s{/color} Are you two still together?" % roosterNickDany.split("@")[1],2)
    $ add_rooster_comment("dany","{color=#00a0e6}@%s{/color} What kind of question is that to ask at a time like this?" % roosterNickSuzy.split("@")[1],4)
    $ add_rooster_comment("suzy","{color=#00a0e6}@%s{/color} I was just asking for a friend!" % roosterNickDany.split("@")[1],2)
    $ add_rooster_comment("wendy","{color=#00a0e6}@%s{/color} Dany, this cluck isn't appropriate." % roosterNickDany.split("@")[1],6)
    $ add_rooster_comment("jamie","{color=#00a0e6}@%s{/color} I've been nothing but nice to Franz. And if that burger killed him, it was an accident! I loved him!" % roosterNickDany.split("@")[1],8)
    $ add_rooster_comment("dany","{color=#00a0e6}@%s{/color} How many times do I have to tell you that Franz is non-binary!?" % roosterNickJamie.split("@")[1],5)
    $ add_rooster_comment("dany","{color=#00a0e6}@%s{/color} WAS* non-binary! Because you killed them!" % roosterNickJamie.split("@")[1],3)
    $ add_rooster_comment("jamie","{color=#00a0e6}@%s{/color} Dany has genital warts! Stay away from her at all costs! {color=#00a0e6}#BUMPYGIRL{/color}" % roosterNickDany.split("@")[1],8)
    $ add_rooster_comment("leon","{color=#00a0e6}@%s{/color} I've waited for this day to come. Do you see what I see now?" % roosterNickJamie.split("@")[1],7)
    $ add_rooster_comment("jamie","{color=#00a0e6}@%s{/color} Help me out here! What do I do?" % roosterNickLeon.split("@")[1],3)
    $ add_rooster_comment("leon","{color=#00a0e6}@%s{/color} Dump her like the flaming trashbag she is." % roosterNickJamie.split("@")[1],7)

    $ add_rooster_choice("{color=#00a0e6}@%s{/color} Report the post and move on. She's not worth your time or energy." % roosterNickJamie.split("@")[1])
    $ add_rooster_choice("RIP Franz. It's a shame that the ramblings of your weird owner have overclouded your demise.")


    if branchJill or branchIsabella:
        $ add_new_rooster_post("bianca","Such an awesome weekend with awesome friends! {color=#00a0e6}#WhatHappensOutHereStaysOutHere{/color}",30,"ep11_cluck_photo_bianca1","rooster_section_bianca_ep11")
    else:
        $ add_new_rooster_post("bianca","Such an awesome weekend with awesome friends! {color=#00a0e6}#WhatHappensOutHereStaysOutHere{/color}",30,"ep11_cluck_photo_bianca2","rooster_section_bianca_ep11")
    $ add_rooster_comment("isabella","{color=#00a0e6}@%s{/color} Thank you for the hospitality. The trip was fantastic." % roosterNickBianca.split("@")[1],3)
    $ add_rooster_comment("jill","{color=#00a0e6}@%s{/color} I loved everything about it. And yes, let those stories stay out there. Haha!" % roosterNickBianca.split("@")[1],3)
    if branchJill or branchIsabella:
        $ add_rooster_comment("bianca","{color=#00a0e6}@%s{/color} You all made it fantastic!" % roosterNickIsabella.split("@")[1],3)
    else:
        $ add_rooster_comment("bianca","{color=#00a0e6}@%s{/color} You two made it fantastic!" % roosterNickIsabella.split("@")[1],3)
    $ add_rooster_comment("bianca","{color=#00a0e6}@%s{/color} I still can't believe we did that!" % roosterNickJill.split("@")[1],3)
    $ add_rooster_comment("carla","{color=#00a0e6}@%s{/color} What did you do?" % roosterNickBianca.split("@")[1],2)
    $ add_rooster_comment("bianca","{color=#00a0e6}@%s{/color} You'd have to be there." % roosterNickCarla.split("@")[1],3)
    $ add_rooster_comment("carla","{color=#00a0e6}@%s{/color} Next time, I'm coming with you! Tell me more in advance, though. My schedule has been swamped lately." % roosterNickBianca.split("@")[1],2)

    if branchJill or branchIsabella:
        $ add_rooster_comment("jill","{color=#00a0e6}@%s{/color} Can you send me those photos, by the way? [name] must have forgotten to do it." % roosterNickBianca.split("@")[1],2)

    if branchJill or branchIsabella:
        $ add_rooster_choice("{color=#00a0e6}@%s{/color} I was gonna send them, but you know how it is. I'll send them soon! Thanks for the weekend {color=#00a0e6}@%s{/color}!" % (roosterNickJill.split("@")[1],roosterNickBianca.split("@")[1]))

    $ add_new_rooster_post("dik","It's Christmas Panty party time! {color=#00a0e6}#DIKsChristmasParty #XXXMAS #TheDirtyBowl{/color}",225,"ep11_cluck_photo_diks","rooster_section_diks_ep11")
    $ add_rooster_comment("wendy","{color=#00a0e6}@%s{/color} Eww! Why are you shaming those poor girls with this picture?" % roosterNickDik.split("@")[1],8)
    $ add_rooster_comment("derek","{color=#00a0e6}@%s{/color} All the girls in the picture were asked before it was posted." % roosterNickWendy.split("@")[1],18)
    $ add_rooster_comment("minny","{color=#00a0e6}@%s{/color} I call bullshit on that!" % roosterNickDerek.split("@")[1],7)
    $ add_rooster_comment("tiffani","{color=#00a0e6}@%s{/color} You have my tits in it, and I approve of this message." % roosterNickMinny.split("@")[1],23)
    $ add_rooster_comment("gina","{color=#00a0e6}@%s{/color} And mine, too." % roosterNickMinny.split("@")[1],21)
    $ add_rooster_comment("leon","{color=#00a0e6}@%s{/color} And my axe!" % roosterNickMinny.split("@")[1],32)
    $ add_rooster_comment("derek","{color=#00a0e6}@%s{/color} Go home, Leon! You're drunk!" % roosterNickLeon.split("@")[1],15)
    $ add_rooster_comment("leon","{color=#00a0e6}@%s{/color} BOOBS!" % roosterNickDerek.split("@")[1],22)
    $ add_rooster_comment("elena","{color=#00a0e6}@%s @%s{/color} I'm in this too! Woho!!! It's totally cool. Mind your business and stop getting offended on behalf of others." % (roosterNickMinny.split("@")[1],roosterNickWendy.split("@")[1]),33)
    $ add_rooster_comment("sarah","{color=#00a0e6}@%s{/color} DIKs' nuts roasting on an ass that's fire..." % roosterNickDik.split("@")[1],38)
    $ add_rooster_comment("jamie","{color=#00a0e6}@%s{/color} HOT girls nipping at your balls." % roosterNickSarah.split("@")[1],24)
    $ add_rooster_comment("tiffani","{color=#00a0e6}@%s{/color} Drinking songs being sung by us all." % roosterNickJamie.split("@")[1],27)
    $ add_rooster_comment("suzy","It doesn't change the fact that it's a sexist picture.",8)
    $ add_rooster_comment("minny","Sexist AND disgusting!",8)
    $ add_rooster_choice("{color=#00a0e6}@%s @%s @%s{/color} And folks dressed up as the opposite of Eskimos." % (roosterNickSarah.split("@")[1],roosterNickJamie.split("@")[1],roosterNickTiffani.split("@")[1]))
    $ add_rooster_choice("{color=#00a0e6}@%s @%s{/color} It's spelled sexy. And yes, you're right. It is sexy." % (roosterNickMinny.split("@")[1],roosterNickSuzy.split("@")[1]))
    $ add_rooster_choice("{color=#00a0e6}@%s @%s{/color} Who are you to body shame anyone? When you wear panties, it looks like floss on a walrus." % (roosterNickMinny.split("@")[1],roosterNickSuzy.split("@")[1]))
elif roosterState == "ep11_5":
    $ new_rooster_int = 1
    if ep11_virus:
        $ new_rooster_int = 2
        $ add_new_rooster_post("mc","I couldn't believe my eyes, but it actually works! FREE RAM for your computer or phone! Speed up your phone now! {color=#00a0e6}Click to download{/color}",2,"ep11_cluck_photo_mc","rooster_section_mc_ep11")
        $ add_rooster_comment("jamie","It does?",1)
        $ add_rooster_comment("derek","{color=#00a0e6}@%s{/color} What did you click?" % roosterNickMC.split("@")[1],3)
        $ add_rooster_comment("sarah","Uh oh. Someone got hacked.",3)
        $ add_rooster_comment("rusty","{color=#00a0e6}@%s{/color} Did you get hacked?" % roosterNickMC.split("@")[1],2)
        $ add_rooster_comment("arieth","{color=#00a0e6}@%s{/color} Does it really work?" % roosterNickMC.split("@")[1],4)
        $ add_rooster_comment("leon","{color=#00a0e6}@%s{/color} Not you, too. A classmate of mine got hacked last week." % roosterNickMC.split("@")[1],5)
        $ add_rooster_choice("Don't click any links! I didn't post this!")

    $ add_new_rooster_post("maya","Finals week is here. It felt like it was midterms a couple of weeks ago. Is everyone hanging in there? {color=#00a0e6}#GiveMeWinterBreakAlready{/color}",19,"ep11_cluck_photo_maya","rooster_section_maya_ep11")
    $ add_rooster_comment("melanie","{color=#00a0e6}@%s{/color} I have three freaking tests this week - on Tuesday, Wednesday, and Friday. I've barely studied for Friday, thinking I'd be able to do that on Thursday. How screwed am I?" % roosterNickMaya.split("@")[1],6)
    $ add_rooster_comment("maya","{color=#00a0e6}@%s{/color} Ugh, that sounds rough. I thought I had it bad with two tests on Friday. Good luck with them!" % roosterNickMelanie.split("@")[1],4)
    $ add_rooster_comment("heather","{color=#00a0e6}@%s{/color} Barely." % roosterNickMaya.split("@")[1],2)
    $ add_rooster_comment("ashley","{color=#00a0e6}@%s{/color} No, I'm nervous and feel like I'm overstudying." % roosterNickMaya.split("@")[1],3)
    if ep11_virus:
        $ add_rooster_comment("arieth","FREE RAM for your computer! {color=#00a0e6}Download here{/color} Offer expires in 24 hours!",1)
    $ add_rooster_comment("sage","Good luck with your tests, everyone! Winter break is just around the corner.",10)
    $ add_rooster_comment("maya","{color=#00a0e6}@%s{/color} Do what I do; take a break if you've studied a lot. I'm taking tonight off for a party." % roosterNickAshley.split("@")[1],3)
    $ add_rooster_comment("ashley","{color=#00a0e6}@%s{/color} A party tonight!? Don't overdo it, or you'll lose study time tomorrow." % roosterNickMaya.split("@")[1],2)
    $ add_rooster_comment("elena","{color=#00a0e6}@%s{/color} Which subjects?" % roosterNickMaya.split("@")[1],2)
    $ add_rooster_comment("maya","{color=#00a0e6}@%s{/color} English and math. >_<" % roosterNickElena.split("@")[1],1)
    $ add_rooster_comment("maya","{color=#00a0e6}@%s{/color} It's not that kind of party. I'll be fine." % roosterNickAshley.split("@")[1],2)
    $ add_rooster_comment("elena","{color=#00a0e6}@%s{/color} I remember hating the math finals." % roosterNickMaya.split("@")[1],3)
    $ add_rooster_comment("maya","{color=#00a0e6}@%s{/color} Oh, no. Was it hard?" % roosterNickElena.split("@")[1],1)
    $ add_rooster_comment("jill","{color=#00a0e6}@%s{/color} Good luck with your studies! See you tonight." % roosterNickMaya.split("@")[1],3)
    $ add_rooster_comment("heather","{color=#00a0e6}@%s{/color} I second that. And \"hate\" is too nice of a word for it." % roosterNickElena.split("@")[1],3)
    $ add_rooster_comment("elena","{color=#00a0e6}@%s{/color} For me, it was. But don't be scared; I'm sure you'll do great at it." % roosterNickMaya.split("@")[1],5)
    $ add_rooster_comment("maya","{color=#00a0e6}@%s{/color} You too!" % roosterNickJill.split("@")[1],1)

    $ add_rooster_choice("{color=#00a0e6}@%s{/color} I'm at the point where it feels like I'm rehashing everything. I don't get better at it, but I don't get worse either." % roosterNickMaya.split("@")[1])
    $ add_rooster_choice("One more week until two weeks of immortality.")
elif roosterState == "ep12_1":
    $ new_rooster_int = 3

    $ add_new_rooster_post("dik","The Christmas party was off the chain, and you brave bastards rock for coming to it! Our next big party will be on New Year's Eve. And yes, you're allowed to wear clothes for this one! DM us or the HOTs if you're interested. {color=#00a0e6}#DIKs #HOTs{/color}",103,"ep12_cluck_photo_diks","rooster_section_diks_ep12")

    $ add_rooster_comment("chen","{color=#00a0e6}@%s{/color} You fucking know I'll be there! Put me down for two." % roosterNickDik.split("@")[1],5)
    $ add_rooster_comment("erin","{color=#00a0e6}@%s{/color} Thanks for the party! We had a blast!" % roosterNickDik.split("@")[1],12)
    $ add_rooster_comment("leon","{color=#00a0e6}@%s{/color} Who's number two?" % roosterNickChen.split("@")[1],2)
    $ add_rooster_comment("derek","{color=#00a0e6}@%s{/color} Poop." % roosterNickLeon.split("@")[1],4)
    $ add_rooster_comment("chen","{color=#00a0e6}@%s{/color} Marc. And he will probably forget about DMing you guys." % roosterNickLeon.split("@")[1],2)
    if ep11_invited_tara:
        $ add_rooster_comment("tara","{color=#00a0e6}@%s{/color} Thanks again for the invite. XO" % roosterNickMC.split("@")[1],3)
    $ add_rooster_comment("camila","{color=#00a0e6}@%s{/color} BEST PARTY EVER! WOOO!!!" % roosterNickDik.split("@")[1],13)
    $ add_rooster_comment("tommy","{color=#00a0e6}@%s{/color} Until our next one!" % roosterNickCamila.split("@")[1],10)
    $ add_rooster_comment("marc","{color=#00a0e6}@%s{/color} I won't forget. What day is the party?" % roosterNickChen.split("@")[1],3)
    $ add_rooster_comment("jacob","{color=#00a0e6}@%s{/color} AWESOME! When did you decide this?" % roosterNickDik.split("@")[1],4)
    $ add_rooster_comment("tommy","{color=#00a0e6}@%s{/color} At the Christmas party." % roosterNickJacob.split("@")[1],4)
    $ add_rooster_comment("dawe","{color=#00a0e6}@%s{/color} HEY! What the hell is this!? We told you girls to be at our New Year's Eve party!" % roosterNickSage.split("@")[1],1)
    $ add_rooster_comment("sage","{color=#00a0e6}@%s{/color} And I told you we were undecided. Besides, this is the first I'm hearing about it. Let's talk about this in private, ok?" % roosterNickDawe.split("@")[1],2)
    $ add_rooster_comment("tommy","{color=#00a0e6}@%s{/color} You didn't show up for our party. I think it's fair, and your sisters liked the idea." % roosterNickSage.split("@")[1],5)
    $ add_rooster_comment("melanie","{color=#00a0e6}@%s{/color} My God... What is that picture of me?" % roosterNickDik.split("@")[1],16)
    $ add_rooster_comment("sage","{color=#00a0e6}@%s @%s{/color} Let's schedule a meeting." % (roosterNickTommy.split("@")[1],roosterNickRusty.split("@")[1]),3)
    $ add_rooster_comment("rusty","{color=#00a0e6}@%s{/color} Heard." % roosterNickSage.split("@")[1],2)
    $ add_rooster_comment("sarah","{color=#00a0e6}@%s{/color} HAHA! You look so wasted!" % roosterNickMelanie.split("@")[1],8)
    $ add_rooster_comment("chen","{color=#00a0e6}@%s{/color} So, the party isn't happening?" % roosterNickTommy.split("@")[1],2)
    $ add_rooster_comment("tommy","{color=#00a0e6}@%s{/color} It's happening." % roosterNickChen.split("@")[1],3)
    $ add_rooster_comment("karen","{color=#00a0e6}@%s{/color} Can I come too?" % roosterNickTommy.split("@")[1],2)
    $ add_rooster_comment("tommy","{color=#00a0e6}@%s{/color} Yes! But DM our account. I'll forget it otherwise." % roosterNickKaren.split("@")[1],3)
    $ add_rooster_comment("jamie","Aw, yeah!!! The New Year's party will be awesome!",9)

    $ add_rooster_choice("{color=#00a0e6}@%s{/color} Do you still need my help?" % roosterNickTommy.split("@")[1])
    $ add_rooster_choice("PARTY!!!")
    if ep11_invited_tara:
        $ add_rooster_choice("{color=#00a0e6}@%s{/color} You're welcome to our New Year's Eve party too." % roosterNickTara.split("@")[1])

    $ add_new_rooster_post("dany","I'm trying the so-called Swyper app for the first time, and I can't believe this is how people date nowadays. Low-effort messages and dick pics sum up the experience. Men really don't know how to flirt. {color=#00a0e6}#Swyper #TheWeakerSex{/color}",23,"ep12_cluck_photo_dany","rooster_section_dany_ep12")
    $ add_rooster_comment("linda","{color=#00a0e6}@%s{/color} Wait. Guys will send you those kinds of pictures if you want them?" % roosterNickDany.split("@")[1],2)
    $ add_rooster_comment("dany","{color=#00a0e6}@%s{/color} You don't need to want them. They will just send them, thinking their worm will impress us." % roosterNickLinda.split("@")[1],3)
    $ add_rooster_comment("suzy","{color=#00a0e6}@%s{/color} When our parents were young and dating, men brought women flowers. I guess dick pics are the new flowers." % roosterNickDany.split("@")[1],5)
    $ add_rooster_comment("minny","{color=#00a0e6}@%s{/color} I don't even get why you want to date someone after what Jamie did to you." % roosterNickDany.split("@")[1],3)
    $ add_rooster_comment("dany","{color=#00a0e6}@%s{/color} I'm not looking to date. I want to get rid of the Jamie-aftertaste." % roosterNickMinny.split("@")[1],3)
    $ add_rooster_comment("linda","{color=#00a0e6}@%s{/color} Ok, I created a Swyper account. What's my next step?" % roosterNickDany.split("@")[1],1)
    $ add_rooster_comment("dany","{color=#00a0e6}@%s{/color} Don't tell me you actually want the dick pics." % roosterNickLinda.split("@")[1],2)
    $ add_rooster_comment("linda","{color=#00a0e6}@%s{/color} What's my next step, Dany?" % roosterNickDany.split("@")[1],1)

    $ add_new_rooster_post("tiffani","After some last-minute cramming, we're going in! 3 hours of Social Anthropology on the schedule. Finals week is here. UGH! Best of luck to everyone out there! {color=#00a0e6}#YouAreNotAlone #Finals{/color}",43,"ep12_cluck_photo_tiffani","rooster_section_tiffani_ep12")
    $ add_rooster_comment("tara","{color=#00a0e6}@%s{/color} May the Professors have mercy on our souls." % roosterNickTiffani.split("@")[1],12)
    $ add_rooster_comment("heather","{color=#00a0e6}@%s{/color} Good luck! You've got this." % roosterNickTiffani.split("@")[1],5)
    $ add_rooster_comment("leon","{color=#00a0e6}@%s{/color} Three hours? That's easy. Try doing 5 hours of calculus with a hangover." % roosterNickTiffani.split("@")[1],5)
    $ add_rooster_comment("tiffani","{color=#00a0e6}@%s{/color} Why would you even attempt that with a hangover? LOL" % roosterNickLeon.split("@")[1],3)
    $ add_rooster_comment("leon","{color=#00a0e6}@%s{/color} I had the wrong date." % roosterNickTiffani.split("@")[1],2)
    $ add_rooster_comment("mia","{color=#00a0e6}@%s{/color} Nail it! You can do it." % roosterNickTiffani.split("@")[1],3)
    $ add_rooster_comment("tommy","{color=#00a0e6}@%s{/color} Liar. I remember that. You stayed up late studying and made the coffee Irish to last longer." % roosterNickLeon.split("@")[1],3)
    $ add_rooster_comment("leon","{color=#00a0e6}@%s{/color} I blame {color=#00a0e6}@%s{/color}." % (roosterNickTommy.split("@")[1],roosterNickJacob.split("@")[1]),5)
    $ add_rooster_comment("felicia","{color=#00a0e6}@%s{/color} The worst week of the year has officially begun. Good luck, all!" % roosterNickTiffani.split("@")[1],6)
    $ add_rooster_comment("jacob","{color=#00a0e6}@%s{/color} I don't know why YOU had to drink. I was done with my tests and wanted one." % roosterNickLeon.split("@")[1],4)

    $ add_rooster_choice("{color=#00a0e6}@%s{/color} Good luck!" % roosterNickTiffani.split("@")[1])
    $ add_rooster_choice("{color=#00a0e6}@%s{/color} Maybe for your next test, you should try that Irish thing during the exam." % roosterNickLeon.split("@")[1])
    if ep11_invited_tara:
        $ add_rooster_choice("{color=#00a0e6}@%s @%s{/color} Good luck, girls! I believe in you." % (roosterNickTiffani.split("@")[1],roosterNickTara.split("@")[1]))
elif roosterState == "ep12_2":
    $ new_rooster_int = 3

    $ add_new_rooster_post("nikita","Winter break is almost upon us, and you can clearly tell that some students are already checking out. {color=#00a0e6}#LastClassBeforeChristmas{/color}",34,"ep12_cluck_photo_nikita","rooster_section_nikita_ep12")
    $ add_rooster_comment("sally","{color=#00a0e6}@%s{/color} He's such a pain in the ass at times. Although he did clean our lab area by himself after class. I guess I can put up with a joke or two." % roosterNickNikita.split("@")[1],12)
    if ep12_nikita:
        $ add_rooster_comment("nikita","{color=#00a0e6}@%s{/color} Haha! Who doesn't like a prankster? He sounds so funny." % roosterNickSally.split("@")[1],8)
    else:
        $ add_rooster_comment("nikita","{color=#00a0e6}@%s{/color} Haha! Did he now?" % roosterNickSally.split("@")[1],8)
    $ add_rooster_comment("sally","{color=#00a0e6}@%s{/color} He drew my face on the balloon, called it \"Salloony\" and said he preferred it to me because it had a better sense of humor, wore latex, and smelled better." % roosterNickNikita.split("@")[1],11)
    $ add_rooster_comment("erin","{color=#00a0e6}@%s{/color} Cute!" % roosterNickNikita.split("@")[1],4)
    $ add_rooster_comment("eugene","{color=#00a0e6}@%s{/color} Humorous or not, lab safety isn't a joke." % roosterNickSally.split("@")[1],2)
    $ add_rooster_comment("nikita","{color=#00a0e6}@%s{/color} Hahaha! That's so mean!" % roosterNickSally.split("@")[1],5)
    $ add_rooster_comment("karen","{color=#00a0e6}@%s{/color} If this is what you've been telling me about, I see what you mean. Haha!" % roosterNickSally.split("@")[1],2)
    $ add_rooster_comment("sally","{color=#00a0e6}@%s{/color} Yep." % roosterNickKaren.split("@")[1],2)
    $ add_rooster_comment("tim","{color=#00a0e6}@%s{/color} So, that's how you look in the lab. It suits you! You were always the brain in the family." % roosterNickNikita.split("@")[1],4)
    $ add_rooster_comment("nikita","{color=#00a0e6}@%s{/color} Haha! Thanks! Are we still on for practice tonight?" % roosterNickTim.split("@")[1],2)
    $ add_rooster_comment("linda","{color=#00a0e6}@%s{/color} Can you put in a good word for me with Dr. Jenkins?" % roosterNickNikita.split("@")[1],2)
    $ add_rooster_comment("tim","{color=#00a0e6}@%s{/color} Yeah, the client wants it." % roosterNickNikita.split("@")[1],2)

    $ add_rooster_choice("{color=#00a0e6}@%s{/color} The truth can be ugly. You didn't have to kill Salloony for it. Rest in peace, Salloony." % roosterNickSally.split("@")[1])
    if ep12_nikita:
        $ add_rooster_choice("{color=#00a0e6}@%s{/color} Found you. Followed." % roosterNickNikita.split("@")[1])

    $ add_new_rooster_post("josy","All love and thanks to {color=#00a0e6}@TheDiane{/color} for featuring me in her upcoming post on winter fashion. {color=#00a0e6}#TheDiane #MsSunshine #WinterFashion{/color}",652,"ep12_cluck_photo_josy","rooster_section_josy_ep12")

    $ add_rooster_comment("bloggirl2","{color=#00a0e6}@%s{/color} WOW! Two of my favorite influencers are working together! I can't believe it! I'm really looking forward to reading that." % roosterNickJosy.split("@")[1],65)
    $ add_rooster_comment("blogguy2","{color=#00a0e6}@%s{/color} You should make a post about women's bikini fashion! That shit would sell." % roosterNickJosy.split("@")[1],15)
    $ add_rooster_comment("heather","{color=#00a0e6}@%s{/color} That's amazing news, Josy! TheDiane is huge! Wow, you're like famous now." % roosterNickJosy.split("@")[1],37)
    $ add_rooster_comment("blogguy1","{color=#00a0e6}@%s{/color} I think you're better than TheDiane. Your content is less mainstream than hers. Don't change who you are because of fame. Your fans love you for you!" % roosterNickJosy.split("@")[1],9)
    $ add_rooster_comment("maya","{color=#00a0e6}@%s{/color} Haha! Your cluck reads much more calm and collected than when you heard the news." % roosterNickJosy.split("@")[1],8)
    $ add_rooster_comment("josy","{color=#00a0e6}@%s{/color} LOL" % roosterNickMaya.split("@")[1],78)
    $ add_rooster_comment("elena","{color=#00a0e6}@%s{/color} That's huge! I'm so happy for you." % roosterNickJosy.split("@")[1],35)
    $ add_rooster_comment("jamie","{color=#00a0e6}@%s{/color} I know zero about women's fashion, but even I know who TheDiane is. That's crazy! Are you famous now?" % roosterNickJosy.split("@")[1],45)
    $ add_rooster_comment("bloggirl3","{color=#00a0e6}@%s{/color} I'm freaking out here! I'm so happy for you! I've been a supporter of you since day one!" % roosterNickJosy.split("@")[1],45)
    $ add_rooster_comment("erin","{color=#00a0e6}@%s{/color} Did you see this!?" % roosterNickMia.split("@")[1],5)
    $ add_rooster_comment("bloggirl1","{color=#00a0e6}@%s{/color} OMG, she replied to you. You're so lucky." % roosterNickMaya.split("@")[1],18)
    $ add_rooster_comment("maya","{color=#00a0e6}@%s{/color} Huh?" % roosterNickBlogGirl1.split("@")[1],4)
    $ add_rooster_comment("camila","{color=#00a0e6}@%s{/color} Congrats!!! I enjoyed your post on that. I want a cute hat like yours." % roosterNickJosy.split("@")[1],27)
    $ add_rooster_comment("tiffani","{color=#00a0e6}@%s{/color} I stumbled upon your blog last week, and I was like \"Hey! I know that girl!\" It's cool that you're gaining traction. We should chat sometime." % roosterNickJosy.split("@")[1],17)
    $ add_rooster_comment("mia","{color=#00a0e6}@%s{/color} WOW!" % roosterNickErin.split("@")[1],4)
    $ add_rooster_comment("becky","{color=#00a0e6}@%s{/color} We should totally do a photoshoot together!!!" % roosterNickJosy.split("@")[1],4)
    $ add_rooster_comment("erin","{color=#00a0e6}@%s{/color} Right?" % roosterNickMia.split("@")[1],5)
    $ add_rooster_comment("blogguy1","{color=#00a0e6}@%s{/color} Who even are you?" % roosterNickBecky.split("@")[1],19)
    $ add_rooster_comment("bloggirl4","{color=#00a0e6}@%s{/color} You're going places, and I'm here for the ride! Congratulations!" % roosterNickJosy.split("@")[1],35)
    $ add_rooster_comment("sarah","{color=#00a0e6}@%s{/color} It looks like big things are happening for you. You should use your blog to put us HOTs on the map. Wink wink." % roosterNickJosy.split("@")[1],13)
    $ add_rooster_comment("blogguy2","{color=#00a0e6}@%s{/color} Do you have any bikini shots?" % roosterNickJosy.split("@")[1],5)
    $ add_rooster_comment("blogguy1","{color=#00a0e6}@%s{/color} MODS! Clean this comment up." % roosterNickBlogGuy2.split("@")[1],9)
    $ add_rooster_comment("josy","{color=#00a0e6}@%s{/color} That's not a bad idea! Maybe I'll take some photos of you girls at the New Year's Eve party." % roosterNickSarah.split("@")[1],95)
    $ add_rooster_comment("blogguy2","{color=#00a0e6}@%s{/color} Hello?" % roosterNickJosy.split("@")[1],2)
    $ add_rooster_comment("thediane","{color=#00a0e6}@%s{/color} MWAH!" % roosterNickJosy.split("@")[1],2603)
    $ add_rooster_comment("bloguser1","Last longer in bed with VAGRINA! Send us your credit card info for a free sample!",2)
    $ add_rooster_comment("blogguy1","{color=#00a0e6}@%s{/color} MODS! Spam alert!" % roosterNickBlogUser1.split("@")[1],13)
    $ add_rooster_comment("josy","{color=#00a0e6}@%s{/color} MWAH MWAH!" % roosterNickTheDiane.split("@")[1],89)
    $ add_rooster_comment("bloggirl1","{color=#00a0e6}@%s{/color} OMG! I LOVE YOUR CONTENT!!!" % roosterNickTheDiane.split("@")[1],20)
    $ add_rooster_comment("blogguy2","{color=#00a0e6}@%s{/color} Do you have any bikini shots on your page?" % roosterNickTheDiane.split("@")[1],3)
    $ add_rooster_comment("blogguy2","{color=#00a0e6}@%s{/color} Nevermind. Found them. HOT!!!" % roosterNickTheDiane.split("@")[1],4)
    $ add_rooster_comment("bloguser2","{i}Comment has been deleted{/i}",1)
    $ add_rooster_comment("blogguy1","{color=#00a0e6}@%s{/color} MODS! You missed the comments above this one, too." % roosterNickBlogUser2.split("@")[1],2)

    $ add_new_rooster_post("dawe","NEW YEAR'S EVE PARTY TRI-ALPHA STYLE! FOOD, DRINKS, AND FIREWORKS! DM US OR THE HOTS FOR AN INVITE. {color=#00a0e6}#TRIALPHAS #PARTY{/color}",135,"ep12_cluck_photo_dawe","rooster_section_dawe_ep12")

    $ add_rooster_comment("alex","HELL YEAH!",12)
    $ add_rooster_comment("jimmy","Is it decided? Are we doing it with the HOTs?",12)
    $ add_rooster_comment("dawe","{color=#00a0e6}@%s{/color} We sure are!" % roosterNickJimmy.split("@")[1],15)
    $ add_rooster_comment("heather","{color=#00a0e6}@%s{/color} How about telling the full truth? This post is a bit misleading." % roosterNickDawe.split("@")[1],5)
    $ add_rooster_comment("dawe","{color=#00a0e6}@%s{/color} I don't know what you're talking about. Alphas and HOTs will party together on New Year's Eve." % roosterNickHeather.split("@")[1],5)
    $ add_rooster_comment("elena","{color=#00a0e6}@%s @%s{/color} With the DIKs." % (roosterNickDawe.split("@")[1],roosterNickDik.split("@")[1]),20)
    $ add_rooster_comment("gina","{color=#00a0e6}@%s{/color} Two frats sharing a party? This I gotta see." % roosterNickElena.split("@")[1],10)
    $ add_rooster_comment("dawe","{color=#00a0e6}@%s{/color} I'll sign you up as our guest!" % roosterNickGina.split("@")[1],10)
    $ add_rooster_comment("john","Ain't no party like a tri-alpha party!",13)
    $ add_rooster_comment("gina","{color=#00a0e6}@%s{/color} Sure. I guess." % roosterNickDawe.split("@")[1],3)
    $ add_rooster_comment("leon","{color=#00a0e6}@%s{/color} Is this true?" % roosterNickSlop.split("@")[1],20)
    $ add_rooster_comment("slop","{color=#00a0e6}@%s{/color} I can't find any data to suggest this is true. But I can put the people in this picture in bikinis for you if you'd like." % roosterNickLeon.split("@")[1],1)
    $ add_rooster_comment("leon","{color=#00a0e6}@%s{/color} No, I'm good. I just wanted to know if this was true." % roosterNickSlop.split("@")[1],3)
    $ add_rooster_comment("slop","{color=#00a0e6}@%s{/color} You're right. That was my bad. On a second attempt, I found this post to be 87%% true." % roosterNickLeon.split("@")[1],1)
    $ add_rooster_comment("leon","{color=#00a0e6}@%s{/color} Whoa! So, it is true. Where did you get that number from?" % roosterNickSlop.split("@")[1],3)
    $ add_rooster_comment("slop","{color=#00a0e6}@%s{/color} Whoops! You caught me. It appears that I made the number up. Can I interest you in a picture with these people in bikinis?" % roosterNickLeon.split("@")[1],1)
    $ add_rooster_comment("sage","{color=#00a0e6}@%s{/color} It will be a joint party at a campus venue. Talk to Rusty or Tommy for more details." % roosterNickLeon.split("@")[1],5)
    $ add_rooster_comment("leon","{color=#00a0e6}@%s{/color} Thanks, but I'm not sure how I feel about that." % roosterNickSage.split("@")[1],3)
    $ add_rooster_comment("minny","{color=#00a0e6}@%s @%s{/color} People are dying in Uganda, and this is what you waste clean water and energy on." % (roosterNickLeon.split("@")[1],roosterNickSlop.split("@")[1]),11)
    $ add_rooster_comment("slop","{color=#00a0e6}@%s{/color} 87%% of the people in Uganda have access to clean water. {color=#00a0e6}Here{/color} is a picture of this user in a bikini." % roosterNickMinny.split("@")[1],1)

    $ add_rooster_choice("A shared party... This is a bad idea.")
    $ add_rooster_choice("{color=#00a0e6}@%s{/color} Give them boobs and put them in a bikini." % roosterNickSlop.split("@")[1])
elif roosterState == "ep12_3":
    $ new_rooster_int = 2

    $ add_new_rooster_post("tybalt","Success - thy name is Tybalt. I nailed the performance and I got the girl. {color=#00a0e6}#ModernDayFairytale #LifeOnTheTop{/color}",55,"ep12_cluck_photo_tybalt","rooster_section_tybalt_ep12")

    $ add_rooster_comment("rich","{color=#00a0e6}@%s{/color} A flawless performance. I'll never forget the look on the faces in the crowd when you played your song." % roosterNickTybalt.split("@")[1],18)
    $ add_rooster_comment("trent","{color=#00a0e6}@%s{/color} Phenomenal!" % roosterNickTybalt.split("@")[1],8)
    $ add_rooster_comment("gordon","{color=#00a0e6}@%s{/color} Cute girl!" % roosterNickTybalt.split("@")[1],3)
    $ add_rooster_comment("tybalt","{color=#00a0e6}@%s{/color} Back off." % roosterNickGordon.split("@")[1],4)
    $ add_rooster_comment("gordon","{color=#00a0e6}@%s{/color} I just thought you looked good together." % roosterNickTybalt.split("@")[1],2)
    $ add_rooster_comment("tybalt","{color=#00a0e6}@%s{/color} Ok. That's acceptable." % roosterNickGordon.split("@")[1],2)
    $ add_rooster_comment("christian","{color=#00a0e6}@%s{/color} You'll have to play your song for us sometime." % roosterNickTybalt.split("@")[1],7)
    $ add_rooster_comment("tybalt","{color=#00a0e6}@%s{/color} Maybe I'll bring my cello to the New Year's party and bless you all with a song." % roosterNickChristian.split("@")[1],12)
    $ add_rooster_comment("rich","{color=#00a0e6}@%s{/color} That would be tremendous. You should make the rest of the band to come too." % roosterNickTybalt.split("@")[1],2)
    $ add_rooster_comment("tybalt","{color=#00a0e6}@%s{/color} Can you come to our New Year's party? The same rate as last time." % roosterNickTim.split("@")[1],2)
    $ add_rooster_comment("tim","{color=#00a0e6}@%s{/color} No can do. I've got dinner plans with friends, and Nikita is going to some big party, I believe." % roosterNickTybalt.split("@")[1],1)
    $ add_rooster_comment("tybalt","{color=#00a0e6}@%s{/color} You should cancel. This is more important than dinner." % roosterNickTim.split("@")[1],3)
    $ add_rooster_comment("tim","{color=#00a0e6}@%s{/color} Yeah, thanks. But no." % roosterNickTybalt.split("@")[1],1)
    $ add_rooster_comment("tybalt","{color=#00a0e6}@%s{/color} Meh. Who needs them? I'll play solo for you, gentlemen." % roosterNickRich.split("@")[1],5)
    $ add_rooster_comment("tim","{color=#00a0e6}@%s{/color} I can read your comments." % roosterNickTybalt.split("@")[1],1)
    $ add_rooster_comment("tyballs","{color=#00a0e6}@%s{/color} Does she feel as moist as a watermelon?" % roosterNickTybalt.split("@")[1],2)
    $ add_rooster_comment("tybalt","{color=#00a0e6}@%s{/color} I have NO IDEA what you're talking about. Stop harassing me!!!" % roosterNickTyballs.split("@")[1],2)

    if ep12_brawler_comp_won:
        $ new_rooster_int += 1
        if brawler_attitude > 0:
            $ add_new_rooster_post("mc","The moment of my first win. You can watch the entire fight {color=#00a0e6}here{/color}. {color=#00a0e6}#FinishingBlow #Domination{/color}",125,"ep12_cluck_photo_mc","rooster_section_mc_ep12")
        else:
            $ add_new_rooster_post("mc","The moment of my first win. Thanks to Johnny Stevens; you put up one hell of a fight. All respect to you. Watch the entire fight {color=#00a0e6}here{/color}. {color=#00a0e6}#FinishingBlow{/color}",125,"ep12_cluck_photo_mc","rooster_section_mc_ep12")

        $ add_rooster_comment("derek","It was an insane fight!",10)
        $ add_rooster_comment("tommy","He got knocked the fuck out! It's cool to watch the fight from another angle. That sound when your foot connects with his face is gnarly!",15)
        if not breakup and (branchMayaJosy or branchSage):
            $ add_rooster_comment("josy","{color=#00a0e6}@%s{/color} You were AMAZING! MWAH!" % roosterNickMC.split("@")[1],88)
        $ add_rooster_comment("melanie","{color=#00a0e6}@%s{/color} I didn't know you were this good at fighting. It's kinda sexy." % roosterNickMC.split("@")[1],24)
        $ add_rooster_comment("becky","It was such an amazing fight! I was there! You can see me in the video to the left!",7)
        $ add_rooster_comment("rusty","YES! Nice job! Congrats!!!",7)
        $ add_rooster_comment("elena","{color=#00a0e6}@%s{/color} I had to close my eyes watching that. Is the other guy ok? You really gave it to him." % roosterNickMC.split("@")[1],4)
        if not breakup and (branchMayaJosy or branchSage):
            $ add_rooster_comment("maya","{color=#00a0e6}@%s{/color} Oh, yay! They taped it? That's such a great memory for you to have." % roosterNickMC.split("@")[1],7)
        $ add_rooster_comment("erin","Amazing!",6)
        $ add_rooster_comment("jamie","WOW! I wish I hadn't missed it.",4)
        $ add_rooster_comment("jacob","HOLY HELL! What a finish!!!",13)
        $ add_rooster_comment("tiffani","Oh my!",13)
        if not breakup and branchIsabella:
            $ add_rooster_comment("isabella","{color=#00a0e6}@%s{/color} Congratulations!" % roosterNickMC.split("@")[1],5)
        if not breakup and branchJill:
            $ add_rooster_comment("jill","{color=#00a0e6}@%s{/color} Congratulations!!! I know how much this means for you. I'm sad I couldn't come see it, but I'll show up on your next fight." % roosterNickMC.split("@")[1],12)
        if not breakup and (branchMayaJosy or branchSage):
            $ add_rooster_comment("sage","{color=#00a0e6}@%s{/color} This looks great, but it was even better live!" % roosterNickMC.split("@")[1],14)
        if branchZoey:
            $ add_rooster_comment("zoey","{color=#00a0e6}@%s{/color} You kicked some serious ass!" % roosterNickMC.split("@")[1],5)
        if not ep12_nicole_breakup and ep12_nicole_path and not ep12_nicole_ditch:
            $ add_rooster_comment("envy","{color=#00a0e6}@%s{/color} Congratulations again!" % roosterNickMC.split("@")[1],5)
        $ add_rooster_comment("dany","Such a chauvinistic sport.",5)
        $ add_rooster_comment("sally","Congratulations on your win!",9)
        $ add_rooster_comment("heather","Whoa! I'm not into fighting, but that was impressive.",11)
        $ add_rooster_comment("clara","{color=#00a0e6}@%s{/color} Not at all. There were female fighters there, too." % roosterNickDany.split("@")[1],12)
        $ add_rooster_comment("felicia","HOT!",19)
        $ add_rooster_comment("mia","{color=#00a0e6}@%s{/color} I would have loved to see that live. Will you fight again soon?" % roosterNickMC.split("@")[1],16)

        $ add_rooster_choice("Thanks for the love, everyone.")
        $ add_rooster_choice("{color=#00a0e6}@%s{/color} If I'm fighting again, I'll post something here before my next fight." % roosterNickMia.split("@")[1])


    $ add_new_rooster_post("sarah","Welcome to our party - if you're invited, that is. Everyone here is a friggin smokeshow! We wish all of you a HOT end to the year. {color=#00a0e6}#HappyNewYear{/color}",75,"ep12_cluck_photo_sarah","rooster_section_sarah_ep12")

    $ add_rooster_comment("elena","Cuties!!!",12)
    $ add_rooster_comment("alex","Everywhere I look, I see sexy girlsss!!!",19)
    $ add_rooster_comment("tiffani","Happy New Year, everyone!",29)
    $ add_rooster_comment("jimmy","{color=#00a0e6}@%s{/color} HELL YEAH! SEX is on the menu for tonight!" % roosterNickAlex.split("@")[1],5)
    $ add_rooster_comment("leon","{color=#00a0e6}@%s{/color} Where did you girls put the hard liquor? We need it." % roosterNickSarah.split("@")[1],3)
    $ add_rooster_comment("sarah","{color=#00a0e6}@%s{/color} Check the coolers on the second floor. Sage should have the key." % roosterNickLeon.split("@")[1],5)
    $ add_rooster_comment("leon","{color=#00a0e6}@%s{/color} Thanks! Found it." % roosterNickSarah.split("@")[1],2)
    $ add_rooster_comment("felicia","Such an amazing job with the party! There are balloons everywhere!",13)
    $ add_rooster_comment("leanne","I'm so thankful for the invite! Love you all!",23)
    $ add_rooster_comment("jimmy","{color=#00a0e6}@%s{/color} Hey there, gorgeous!" % roosterNickLeanne.split("@")[1],2)
    $ add_rooster_comment("chen","PARTY BITCHES!",10)
    $ add_rooster_comment("ashley","Pretty!",6)
    $ add_rooster_comment("darius","I'M ALREADY BUZZING!!!",13)
    $ add_rooster_comment("heather","The food better not be too delicious or my dress will tear.",7)
    $ add_rooster_comment("melanie","Let's party until dawn, everyone!",33)
    $ add_rooster_comment("arieth","{color=#00a0e6}@%s{/color} You're telling me!" % roosterNickHeather.split("@")[1],4)
    $ add_rooster_comment("gina","Does anyone know what's up with the yellow tape?",20)
    $ add_rooster_comment("dawe","{color=#00a0e6}@%s{/color} The tape doesn't concern you. Only the frats need to worry about it." % roosterNickGina.split("@")[1],8)
    $ add_rooster_comment("tommy","{color=#00a0e6}@%s{/color} Yeah. On one side of the tape, there's a really cool party, and on the other side, there are jocks." % roosterNickGina.split("@")[1],18)
    $ add_rooster_comment("karen","{color=#00a0e6}@%s{/color} Haha!" % roosterNickTommy.split("@")[1],3)
    $ add_rooster_comment("dawe","{color=#00a0e6}@%s{/color} Take that back!" % roosterNickTommy.split("@")[1],7)
    $ add_rooster_comment("christie","{color=#00a0e6}@%s{/color} I'll give you that there are fewer cocks trying to push against my thigh on the DIKs' side of the party." % roosterNickTommy.split("@")[1],12)
    $ add_rooster_comment("jamie","Can someone tell the jocks that the van is outside with the rest of the stuff?",4)
    $ add_rooster_comment("nikita","The party is so much fun. Great job to everyone involved!",10)
    $ add_rooster_comment("tara","{color=#00a0e6}@%s{/color} ikr" % roosterNickChristie.split("@")[1],5)
    $ add_rooster_comment("rusty","{color=#00a0e6}@%s{/color} I'm on it." % roosterNickJamie.split("@")[1],3)
elif roosterState == "ep12_4":
    $ new_rooster_int = 1
    $ add_new_rooster_post("dik","Happy New Year! {color=#00a0e6}#HappyNewYear{/color}",125,"ep12_cluck_photo_diks2","rooster_section_diks2_ep12")

    $ add_rooster_comment("jamie","Happy new one! So, where did everyone end up last night? Any stories?",4)
    $ add_rooster_comment("elena","Happy New Year! Wow... Dead comment section, huh?",2)
    $ add_rooster_comment("tommy","{color=#00a0e6}@%s{/color} The hallmark of a great party, I'd say. I just woke up." % roosterNickElena.split("@")[1],5)
    $ add_rooster_comment("johnboy","Don't look in the kitchen sink, guys. Someone had an accident.",4)
    $ add_rooster_comment("jacob","{color=#00a0e6}@%s{/color} Sorry about that. I had too much of the good stuff last night." % roosterNickJohnBoy.split("@")[1],3)
    $ add_rooster_comment("derek","{color=#00a0e6}@%s{/color} The year started great. [name] owes me $1000." % roosterNickJamie.split("@")[1],3)
    $ add_rooster_comment("chen","{color=#00a0e6}@%s{/color} DIKS!!! This is the year! Chen and Marc are coming for ya!" % roosterNickDik.split("@")[1],3)
    $ add_rooster_comment("tommy","{color=#00a0e6}@%s{/color} Why are you speaking like you're maggots already? Shut the hell up." % roosterNickChen.split("@")[1],8)
    $ add_rooster_comment("chen","{color=#00a0e6}@%s{/color} But we passed the initiation. Leon and [name] tested us." % roosterNickTommy.split("@")[1],2)
    $ add_rooster_comment("leon","{color=#00a0e6}@%s{/color} You got it twisted. You're not in yet." % roosterNickChen.split("@")[1],3)
    $ add_rooster_comment("jamie","{color=#00a0e6}@%s{/color} Bro! Where have you been? I've been looking all over for you." % roosterNickLeon.split("@")[1],4)
    $ add_rooster_comment("leon","{color=#00a0e6}@%s{/color} We'll talk." % roosterNickJamie.split("@")[1],1)
    $ add_rooster_comment("jamie","{color=#00a0e6}@%s{/color} HAHA! Someone got lucky!" % roosterNickLeon.split("@")[1],2)

    $ add_rooster_choice("{color=#00a0e6}@%s{/color} Nice try. I saw you without those ugly glasses for the better half of the party." % roosterNickDerek.split("@")[1])
    $ add_rooster_choice("{color=#00a0e6}@%s{/color} Who told you it was ok to comment on our official account? At least Marc is smart enough not to do it. Maybe we'll just have room for one of you." % roosterNickChen.split("@")[1])


if new_rooster_int > 0:
    $ new_cluck = True
$ renpy.jump(rooster_jump_label)
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
