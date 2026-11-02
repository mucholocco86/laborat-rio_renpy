
label ch3sc3:

    window hide dissolve
    play music explore_1 fadein 1.0
    scene black with Dissolve (2.0)
    "A few moments later in Dalen's office..."
    scene ch3sc03_004 with Dissolve(2.0)
    $ renpy.pause(1)
    "..."
    "......"
    "............"
    scene ch3sc03_009 with dissolve
    da "Ahh, you two must be the new recruits."
    scene ch3sc03_003 with dissolve
    el "How did you-"
    scene ch3sc03_009 with dissolve
    da "According to the local guards, I’m expecting a meeting with you two."
    scene ch3sc03_003 with dissolve
    el "Oh... About that..."
    scene ch3sc03_005 with dissolve
    el "We can explain, sir."
    el "*Whispers* {size=-10}{b}Go on, explain it to him before he kicks us out!{/b}{/size}"
    scene ch3sc03_006 with dissolve
    mc "The guard wouldn’t let us enter the city without a city-pass."
    mc "So I handled it the best I could without causing a scene."
    scene ch3sc03_007 with dissolve
    $ renpy.pause(1.3)
    scene ch3sc03_008 with dissolve
    $ renpy.pause(1.3)
    scene ch3sc03_009 with dissolve
    da "So you did."
    da "Being able to think on your feet and solve unforeseen problems..."
    scene ch3sc03_010 with dissolve
    da "That's something any adventurer who’s worthy of the name must be able to do."
    if ml_intim == True:
        da "However, I'd advise you to avoid intimidating guards in the future..."
        da "All it takes is for one guard to not be swayed and you'll end up in the dungeons."

    else:
        da "However, I'd advise you to avoid trying to persuade guards in the future..."
        da "All it takes is for one guard to not be swayed and you'll end up in the dungeons."

    scene ch3sc03_006 with dissolve
    mc "Noted."
    mc "So, all that fuss about the city-pass was a test?"
    scene ch3sc03_009 with dissolve
    da "No, let’s just call it a happy coincidence."
    scene ch3sc03_010 with dissolve
    da "The city-pass requirement was ordered by the guard captain."
    scene ch3sc03_011 with dissolve
    da "And not without good reason, either."
    scene ch3sc03_003 with dissolve
    el "Sir, if I may be so bold, why? It seems a little excessive."
    scene ch3sc03_012 with dissolve
    da "Recently, there’s been a string of kidnappings around the city."
    da "At least suspected kidnappings, there's been no ransom demands, only young women disappearing."
    scene ch3sc03_013 with dissolve
    da "So unless outsiders have official business in Luxenford, they will be refused at the gates for now."
    da "There's nothing to be done about it at the moment, not until a culprit for the kidnappings have been brought to justice."
    scene ch3sc03_014 with dissolve
    el "Are there any leads on these kidnappings?"
    el "Surely people can't just vanish without a trace?"
    scene ch3sc03_015 with dissolve
    da "*Sigh* I’m afraid not... It’s been going on for roughly four or five moons now."
    da "So far nine young women between the age of 18 to 25 have gone missing."
    scene ch3sc03_016 with dissolve
    mc "We’ll keep an eye out for anything suspicious."
    el "*Nods in agreement* Hm-hm!"
    scene ch3sc03_017 with dissolve
    da "Good. Be sure to report it to the guards or me if you stumble upon anything."
    da "But don't go trying to solve this on your own."
    da "It's far too serious for recruits to deal with on their own."
    da "I'm sure both of you are quite capable. But I'd rather not have our first two recruits in over a year vanish as well."
    scene ch3sc03_018 with dissolve
    el "Understood, sir! We'll report back if we come across anything that seems suspicious."
    el "Being in the target range for these kidnappings myself, I'd like to get this solved!"
    scene ch3sc03_019 with dissolve
    da "Yeah, I can see why you'd feel uneasy about the situation, and please, just call me Dalen."
    da "I’m not one for such formalities. Come, let's have a seat."
    scene ch3sc03_020 with dissolve
    el "Yes, sir- I mean Dalen."
    el "By the way, the guard at the gates told us to inquire about getting our city-pass with you?"
    scene ch3sc03_021 with dissolve
    da "Ah, right."
    da "Sylph will make one for you on your way out."
    scene ch3sc03_022 with dissolve
    el "Great!"
    el "We really don’t wish to cause trouble with the guards."
    scene ch3sc03_023 with dissolve
    da "Now, tell me."
    da "Why did you really lie to the guards and want to see me?"
    scene ch3sc03_024 with dissolve
    mc "We want to become members of your guild and be official adventurers."
    mc "It's been a dream of mine since childhood, although it hasn't been a priority recently. For personal reasons."
    mc "And we also happen to be short on coin."
    mc "We heard completing quests and contracts for the guild is a good way to earn money."
    scene ch3sc03_025 with dissolve
    da "I see..."
    scene ch3sc03_026 with dissolve
    el "Please, sir- Dalen! We’ve traveled so far to get here."
    el "Don’t turn us away."
    scene ch3sc03_027 with dissolve
    da "Woah, calm down miss. I don’t intend to turn you away."
    da "Your reasons for joining us are your own. People seek out adventuring for their own reasons."
    scene ch3sc03_028 with dissolve
    da "Some for the community, some for the thrill of discovery, some for coin, and some to fulfill their dreams."
    da "I don't judge. Also, we’re short on adventurers at the moment. There haven’t been any new recruits this season."
    scene ch3sc03_029 with dissolve
    el "Oh, right. Sylph did mention something about that."
    el "That's unfortunate, I'd think people would be eager to apply for the guild?"
    scene ch3sc03_030 with dissolve
    mc "I'm with Eliza, I would've thought the guild would appeal to a lot of people?"
    mc "Why haven't any new recruits been applying to the guild?"
    scene ch3sc03_025 with dissolve
    da "I haven’t been able to confirm anything yet. But I do have a hunch who might be behind it."
    da "And it's not just our guild. Other guilds have been targeted too."
    da "Like the Mages Guild, for example... they recently had a change in leadership."
    da "I was on good terms with their previous Guildmaster, Cassandra."
    da "She's an incredible sorceress, renowned leader, a beauty from the Sen'ju region, but most of all, she's a good person."
    da "However, since their change in leadership, I haven't been able to get into contact with her."
    scene ch3sc03_029 with dissolve
    el "That doesn't sound promising... could that be foulplay as well?"
    el "Who do you think is behind it?"
    scene ch3sc03_028 with dissolve
    da "Our rival guild, The Mercenaries Guild."
    da "I'm almost certain of it, but they've been covering their tracks well."
    scene ch3sc03_031 with dissolve
    el "Why would they try to sabotage your recruitment? Or that of other guilds?"
    el "Seems like it would be a big risk to take. If they're ever found out..."
    scene ch3sc03_032 with dissolve
    da "They benefit from our guild performing poorly."
    da "You see, our guilds compete over some common quests and bounties."
    scene ch3sc03_033 with dissolve
    mc "So if our guild has less recruits to fulfill contracts..."
    scene ch3sc03_034 with dissolve
    da "We'll earn less coin, and people needing help will turn to them instead of us."
    da "But I can't figure out why they would target the Mage's guild as well."
    da "They don't have any overlapping contracts or quests."
    scene ch3sc03_035 with dissolve
    el "This isn't right! Hnngh..."
    el "There’s got to be something we can do about it!"
    scene ch3sc03_037 with dissolve
    da "*Sigh* I appreciate your concern... I really do."
    da "I’m working on a plan... but I'll need solid proof before I can proceed."
    scene ch3sc03_036 with dissolve
    da "For now, we’re just happy to have two new recruits."
    scene ch3sc03_038 with dissolve
    da "You two should head out to sort your equipment and supplies."
    scene ch3sc03_039 with dissolve
    da "Sylph will have a quest ready for you once you return."
    scene ch3sc03_040 with dissolve
    mc "Sounds good."
    mc "Keep us updated when you think of a way to deal with the recruitment issue."
    scene ch3sc03_038 with dissolve
    da "Thank you, [mc] and Eliza."
    da "Something tells me that you will both make great additions to our ranks."
    scene ch3sc03_041 with dissolve
    el "We won’t disappoint you, Dalen!"
    scene ch3sc03_039 with dissolve
    da "Alright, alright. Get going you two."
    stop music fadeout 2.0
    scene black with Dissolve(2)
    jump ch3sc4
