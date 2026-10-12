label ch4sc1:

    window hide dissolve
    play music feels_1 fadein 1.0
    scene black with Dissolve (1.0)
    scene ch3sc28_097 with dissolve
    mct "Eliza..."
    with vpunch
    mct "Fuck!"
    mct "What good are my powers if I can’t even protect the ones I care about..."
    scene ch4sc1_001 with Dissolve(2.0)
    el "*Coarse coughing*"
    stop music fadeout 2.0
    scene ch4sc1_002 with dissolve
    el "W-What happened?"
    play music chill_5 fadein 1.0
    scene ch4sc1_003 with dissolve
    el "[mc]?"
    scene ch4sc1_004 with dissolve
    with vpunch
    mc "Y-You’re alive?!"
    scene ch4sc1_005 with dissolve
    el "{size=+3}{b}Owwh!{/b}{/size} My poor ears... I’m glad you’re happy, but don’t shout so loudly."
    scene ch4sc1_006 with dissolve
    mc "How do you feel? Does it hurt anywhere?"
    mc "Are you okay to stand?"
    scene ch4sc1_007 with dissolve
    el "I..."
    scene ch4sc1_008 with dissolve
    el "I-I can’t feel my legs..."
    scene ch4sc1_009 with dissolve
    el "[mc]? W-Why can’t I feel my legs?"
    scene ch4sc1_010 with dissolve
    $ renpy.pause()
    scene ch4sc1_011 with dissolve
    with vpunch
    mct "Fuck! {b}FUCK!!{/b}"
    mct "When he punched her in the back, it must have broken her lower spine."
    mct "I heard the sound of something snapping... this is bad..."
    scene ch4sc1_012 with dissolve
    mc "Listen... I’m going to pinch your legs."
    mc "Let me know when you start to feel something."
    scene ch4sc1_013 with dissolve
    el "[mc], I’m scared... W-Why can’t I move my legs?"
    scene ch4sc1_014 with dissolve
    mc "Shhh. It will be okay... I promise."
    mc "Just tell me when you feel something."
    scene ch4sc1_013 with dissolve
    el "O-Okay..."
    scene ch4sc1_015 with dissolve
    $ renpy.pause(1.5)
    scene ch4sc1_016 with dissolve
    $ renpy.pause(1.5)
    scene ch4sc1_017 with dissolve
    $ renpy.pause(1.5)
    scene ch4sc1_018 with dissolve
    el "Ouwh!"
    scene ch4sc1_019 with dissolve
    mct "It appears she can’t feel anything below her waist..."
    mct "Right around her hip bone is where she starts to feel something... which means she can't walk."
    scene ch4sc1_013 with dissolve
    el "[mc]... I-I... Selena, she-"
    el "Sel-Selena..."
    scene ch4sc1_020 with dissolve
    $ renpy.pause(0.5)
    "She doesn't manage to finish her sentence before exhaustion takes her."
    mct "Selena? Is she worried about her safety? Does she think Selena was taken as well?"
    scene ch4sc1_021 with dissolve
    mct "The shock of everything that's happened in the last few hours must have taken it’s toll."
    mct "I have to get her back to the warmth of the tavern, and our bed."
    scene ch4sc1_022 with dissolve
    mct "She’s so incredibly strong."
    mct "She was stuck down here in the cold, dirty cellars, all on her own..."
    mct "Still, she managed to hold it together."
    mct "When I first arrived, I could tell she was in a lot of pain."
    scene ch4sc1_021 with dissolve
    mct "But she put on a brave face for me, so that I wouldn’t worry before we were safe."
    mct "Now it’s my turn to be strong. I need to be her rock through this."
    scene ch4sc1_022 with dissolve
    stop music fadeout 2.0
    mct "No... Her mountain."
    scene black with Dissolve(2)
    $ renpy.pause(1)
    scene ch4_intro1 with Dissolve(2)
    $ renpy.pause(2, hard=True)
    $ renpy.pause()
    scene ch4_intro2 with Dissolve(2)
    $ renpy.pause(1.5, hard=True)
    $ renpy.pause()
    scene black with Dissolve(2)
    $ renpy.pause(1)
    play music darknight_1 fadein 1.0
    scene ch4sc1_023 with Dissolve(2)
    $ renpy.pause()
    scene ch4sc1_024 with dissolve
    $ renpy.pause()
    scene ch4sc1_025 with dissolve
    $ renpy.pause()
    mct "You will walk again..."
    mct "I will stop at nothing to ensure that."
    scene black with Dissolve(2)
    $ renpy.pause(1)
    scene ch4sc1_026 with Dissolve(2)
    mct "We're here."
    stop music fadeout 2.0
    scene black with Dissolve(2)
    $ renpy.pause(1)
    scene ch4sc1_027 with Dissolve(2)
    play music forest_1 fadein 1.0
    br "[mc]!"
    br "Ye found her! What the blazes happened?"
    scene ch4sc1_028 with dissolve
    mc "Help me get her to our room."
    mc "She needs rest... I’ll tell you what happened later."
    scene ch4sc1_029 with dissolve
    br "Here, I’ll get the doors."
    scene ch4sc1_030 with dissolve
    br "She looks rough..."
    br "We'd best make sure the innkeep prepares some honeyed tea for when she wakes up."
    scene ch4sc1_031 with dissolve
    al "[mc]?"
    mct "Is that... here? Now?"
    scene ch4sc1_032 with dissolve
    $ renpy.pause()
    "..."
    scene ch4sc1_033 with dissolve
    mc "Alice?"
    mc "What are you doing here?"
    scene ch4sc1_032 with dissolve
    al_t "I'm here to confess my feelings to you..."
    scene ch4sc1_034 with dissolve
    al "Wait... is that?!"
    scene ch4sc1_035 with dissolve
    al "What happened?"
    al "Who did this to her?!"
    scene ch4sc1_033 with dissolve
    mc "Not here..."
    mc "Come, we can talk in my room."
    scene black with Dissolve(2)
    $ renpy.pause(1)
    scene ch4sc1_036 with Dissolve(2)
    $ renpy.pause()
    scene ch4sc1_037 with dissolve
    mc "Rest up..."
    mc "We’ll get your legs working in no time."
    scene ch4sc1_038 with dissolve
    mc "I promise you, Eliza."
    mc "Nothing will stand in my way."

    ###Choice###
    menu:
        "I will find a cure. ({color=#87e1fa}Light Path{/color})":
            $ light += 1
            scene ch4sc1_039 with dissolve
            mc "I will find a way, no matter the cost."
            
        "I will burn this city to the ground if I have to. ({color=#f00}Dark Path{/color})":
            $ dark += 1
            scene ch4sc1_039 with dissolve
            mc "I will tear this city apart to find him."
            mc "And when I do, he will know the definition of terror."

    scene ch4sc1_038 with dissolve
    mc "He will pay for this."
    scene ch4sc1_039 with dissolve
    mc "He claimed you were a weakness."
    mc "Don’t you dare believe that, even for a second."
    scene ch4sc1_038 with dissolve
    mc "He couldn’t be more wrong. You’re not my weakness..."
    mc "You’re my strength. You hear me?"
    scene ch4sc1_040 with dissolve
    mc "I’ve spent the last decade in misery. Struggling at every turn."
    mc "The only thing on my mind was to avenge the death of my parents."
    scene ch4sc1_041 with dissolve
    mc "But then I met you."
    mc "And slowly things started to change. I didn’t want to admit it at first, but you’ve taught me so much."
    scene ch4sc1_042 with dissolve
    mc "Every day with you has made me feel more alive than I ever expected."
    mc "You've supported me at every turn... and you’ve given me new purpose."
    scene ch4sc1_043 with dissolve
    mct "There’s nothing I wouldn’t do for you. Nothing."
    mc "*Heavy Sigh* ..."
    "You run your hand through her soft silky hair one last time before you get up..."
    scene ch4sc1_044 with dissolve
    $ renpy.pause()
    scene ch4sc1_045 with dissolve
    $ renpy.pause()
    scene black with Dissolve(1)
    $ renpy.pause(1)
    scene ch4sc1_047 with dissolve
    br "Will the lass be alright?"
    br "What in the shambles happened earlier?"
    br "Ye bolted outta here as if ye were chased by a ghost."
    scene ch4sc1_048 with dissolve
    al "I heard you mentioning her legs? Did someone do this to her?"
    scene ch4sc1_049 with dissolve
    mc "*Sigh* Yes. Someone..."
    scene ch4sc1_050 with dissolve
    mc "The same someone who murdered Mama and Papa in cold blood."
    scene ch4sc1_049 with dissolve
    mc "All because of what I am... Everyone who gets close to me ends up hurt or worse."
    scene ch4sc1_050 with dissolve
    mc "Look at her."
    scene ch4sc1_051 with dissolve
    mc "She’s innocent in all of this. Yet because she's dear to me, he targeted her."
    mc "Hurt her, Alice. Crippled her..."
    scene ch4sc1_048 with dissolve
    al "[mc]... Don’t blame yourself for this... you couldn’t have known."
    al "I know that's probably hard to see right now... but this is not your fault."
    scene ch4sc1_047 with dissolve
    br "Aye... listen te the lass, ye can’t shoulder this on yer own."
    scene ch4sc1_052 with dissolve
    al "The only one to blame for this is the creep who hurt her and killed your parents!"
    scene ch4sc1_053 with dissolve
    mc "I... I appreciate what you guys are trying to do, but it is my fault."
    mc "Nothing can change that."
    scene ch4sc1_049 with dissolve
    mc "I should’ve been prepared... what did I expect?"
    mc "That he would just let me track him down without putting up a fight?"
    scene ch4sc1_050 with dissolve
    mc "Could you guys watch over her for a while?"
    scene ch4sc1_048 with dissolve
    al "What do you mean?"
    scene ch4sc1_049 with dissolve
    mc "There’s someone I have to go see, they might be able to help Eliza."
    scene ch4sc1_047 with dissolve
    br "Sure, kid. Go on."
    br "We'll stay put and watch over her."
    scene ch4sc1_054 with dissolve
    al "[mc], I-I..."
    al "Go, we’ll take care of things here."
    scene ch4sc1_053 with dissolve
    mc "Thank you."
    mc "It gives me some comfort knowing you guys are by her side."
    scene black with Dissolve(2)
    stop music fadeout 1.3
    $ renpy.pause(0.3)
    jump ch4sc2
