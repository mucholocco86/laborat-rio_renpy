init:
    $ v_char_info_who = "mc"

screen scr_mm_characters_menu:
    key "game_menu" action [Hide("scr_mm_characters_menu",dissolve),renpy.restart_interaction, SetVariable('quick_menu', False)]

    add "bg_characters_mm"

    imagebutton:
        idle "img_gradient_[persistent.v_mm_gradient[persistent.v_mm_gradient_order]]" action NullAction()


    imagebutton:
        xalign 0.01
        yalign 0.98
        auto "btn_mm_back_%s" action [Hide("scr_mm_characters_menu",dissolve),renpy.restart_interaction, SetVariable('quick_menu', False)]

    imagebutton:
        xalign 0.98
        yalign 0.98
        auto "btn_mm_exit_%s" action [Hide("scr_mm_characters_menu",dissolve),Hide("scr_mm_main",dissolve),renpy.restart_interaction, SetVariable('quick_menu', True), SetVariable('v_mm_open', False)]

    frame:
        xalign 0.3
        yalign 0.05
        has hbox

        imagebutton:
            auto "btn_mc_char_%s" action [Show("scr_mm_characters_info",dissolve),SetVariable ("v_char_info_who","mc")]
        imagebutton:
            auto "btn_ariel_char_%s" action [Show("scr_mm_characters_info",dissolve),SetVariable ("v_char_info_who","ariel")]
        imagebutton:
            auto "btn_bella_char_%s" action [Show("scr_mm_characters_info",dissolve),SetVariable ("v_char_info_who","bella")]
        imagebutton:
            auto "btn_vivian_char_%s" action [Show("scr_mm_characters_info",dissolve),SetVariable ("v_char_info_who","vivian")]
        imagebutton:
            auto "btn_victor_char_%s" action [Show("scr_mm_characters_info",dissolve),SetVariable ("v_char_info_who","victor")]
        if megan_known:
            imagebutton:
                auto "btn_megan_char_%s" action [Show("scr_mm_characters_info",dissolve),SetVariable ("v_char_info_who","megan")]
        else:
            imagebutton:
                auto "btn_char_unknown_%s" action NullAction()

        if juliet_known:
            imagebutton:
                auto "btn_juliet_char_%s" action [Show("scr_mm_characters_info",dissolve),SetVariable ("v_char_info_who","juliet")]
        else:
            imagebutton:
                auto "btn_char_unknown_%s" action NullAction()

        if zora_known:
            imagebutton:
                auto "btn_zora_char_%s" action [Show("scr_mm_characters_info",dissolve),SetVariable ("v_char_info_who","zora")]
        else:
            imagebutton:
                auto "btn_char_unknown_%s" action NullAction()

        if justice_known:

            imagebutton:
                auto "btn_justice_char_%s" action [Show("scr_mm_characters_info",dissolve),SetVariable ("v_char_info_who","justice")]

        else:
            imagebutton:
                auto "btn_char_unknown_%s" action NullAction()

    if (v_allow_redefine):
        textbutton _("{size=60}Redefine Relationships{/size}") xalign 0.5 yalign 0.8 text_outlines [ (3, "#000000", 0, 0) ] action Show("set_rel",dissolve)






screen scr_mm_characters_info:

    key "game_menu" action [Hide("scr_mm_characters_info",dissolve),renpy.restart_interaction, SetVariable('quick_menu', False)]

    add "bg_characters_mm"

    add "black" alpha 0.7


    frame:
        xalign 0.02
        yalign 0.05
        imagebutton idle "btn_[v_char_info_who]_rewards_hover" action NullAction()

    if v_char_info_who == "mc":
        use scr_mm_characters_info_mc
    elif v_char_info_who == "ariel":
        use scr_mm_characters_info_ariel
    elif v_char_info_who == "bella":
        use scr_mm_characters_info_bella
    elif v_char_info_who == "vivian":
        use scr_mm_characters_info_vivian
    elif v_char_info_who == "megan":
        use scr_mm_characters_info_megan
    elif v_char_info_who == "victor":
        use scr_mm_characters_info_victor
    elif v_char_info_who == "juliet":
        use scr_mm_characters_info_juliet
    elif v_char_info_who == "zora":
        use scr_mm_characters_info_zora
    elif v_char_info_who == "justice":
        use scr_mm_characters_info_justice


    imagebutton:
        xalign 0.01
        yalign 0.98
        auto "btn_mm_back_%s" action [Hide("scr_mm_characters_info",dissolve),renpy.restart_interaction, SetVariable('quick_menu', False)]

    imagebutton:
        xalign 0.98
        yalign 0.98
        auto "btn_mm_exit_%s" action [Hide("scr_mm_characters_info",dissolve),Hide("scr_mm_characters_menu",dissolve),Hide("scr_mm_main",dissolve),renpy.restart_interaction, SetVariable('quick_menu', True), SetVariable('v_mm_open', False)]


style tx_button:
    color "#ffffff"
    yalign 0.1

style char_info_title:
    outlines [(2, "#000000", 1, 1)]
    text_align 1.0
    color "#FFFFFF"

style char_info_description:
    outlines [(2, "#000000", 1, 1)]

    color "#d1b552"

style char_info_description_clickable:
    padding (0, 0)

style char_info_description_clickable_text is char_info_description:

    hover_color "#f1e582"

style char_info_button:
    outlines [(2, "#000000", 1, 1)]
    padding (0, 0)
    ypos -5
    color "#d1b552"
    hover_color "#9e442b"

style char_info_button:
    variant "small"
    size 38

style char_info_title:
    variant "small"
    size 38

style char_info_description:
    variant "small"
    size 38


screen scr_mm_characters_info_mc:
    imagebutton idle "bg_transparent" action NullAction()
    viewport:
        draggable True
        mousewheel True
        scrollbars "vertical"
        ymaximum 900
        xpos 0.2 ypos 0.05
        has vbox
        hbox:
            text "Name: " style "char_info_title"
            textbutton _("[y_name]") action Show('rename', var_name_to_change='y_name') text_style "char_info_button"
            textbutton _("[y_lastname]") action Show('rename', var_name_to_change='y_lastname') text_style "char_info_button"


        hbox:
            text "Nicknames: " style "char_info_title"
            text "Mr. Charisma" style "char_info_description"
        hbox:
            text "Height: " style "char_info_title"
            text "1.75m (5ft7)" style "char_info_description"

        hbox:
            text "Age: " style "char_info_title"
            text "21" style "char_info_description"

        hbox:
            text "Positive Traits: " style "char_info_title"
            text "Ambitious - Optimistic - Adventurous - Charming - Selfless - Sympathetic" style "char_info_description"

        hbox:
            text "Negative Traits: " style "char_info_title"
            text "Cocky - Overconfident - Negligent - Unlucky" style "char_info_description"

        hbox:
            text "Occupation: " style "char_info_title"
            text "Works at a Gym at the front desk and also as an instructor." style "char_info_description"


        vbox:
            xmaximum 1200
            text ""
            text "Your goal is to be the best thief in the world." style "char_info_description"
            text "You enjoy stealing from rich people and avoid robbing the lower class unless it’s absolutely necessary." style "char_info_description"
            text "You have a keen interest in health and nutrition, and one of your dreams is to have one your own gym someday." style "char_info_description"
            text "As the main character, you are incredibly charismatic and confident, and you enjoy being around attractive women - including those that you live with!" style "char_info_description"
            text "You excel under pressure and making conversation comes naturally to you." style "char_info_description"
            text "Staying in great shape makes you the ideal candidate for missions that require a lot of physical activity." style "char_info_description"



screen scr_mm_characters_info_ariel:
    imagebutton idle "bg_transparent" action NullAction()
    viewport:
        draggable True
        mousewheel True
        scrollbars "vertical"
        ymaximum 900
        xpos 0.2 ypos 0.05
        has vbox
        hbox:
            text "Name: " style "char_info_title"
            textbutton _("[a_name]") action Show('rename', var_name_to_change='a_name') text_style "char_info_button"


        hbox:
            text "Nicknames: " style "char_info_title"
            text "The Hacker" style "char_info_description"
        hbox:
            text "Height: " style "char_info_title"
            text "1.6m (5ft3)" style "char_info_description"

        hbox:
            text "Age: " style "char_info_title"
            text "18" style "char_info_description"

        hbox:
            text "Positive Traits: " style "char_info_title"
            text "Clever - Organised - Romantic - Know-it-all" style "char_info_description"

        hbox:
            text "Negative Traits: " style "char_info_title"
            text "Introvert - Self-conscious - Scaredy-Cat - Perfectionist" style "char_info_description"

        hbox:
            text "Occupation: " style "char_info_title"
            text "Computer and electronics repair store in town." style "char_info_description"


        vbox:
            xmaximum 1200
            text ""
            text "[a_name] is a computer wiz and a bit of a nerd. She enjoys computers, reading, anime and spending most of her time indoors." style "char_info_description"
            text "She struggles with meeting new people and engaging in conversations." style "char_info_description"
            text "This young, naive teenager’s biggest fear is getting caught, and she doesn’t like being out in the field for jobs." style "char_info_description"
            text "[a_name] admires your physical abilities and confidence, wishing she could be more like you." style "char_info_description"
            text "She works at a computer repair shop." style "char_info_description"
            text "Her best trait is her ability to hack into any computer system, create fake profiles, disable security alarms, and more." style "char_info_description"
            text "[a_name] is very insecure about her body. She’s a virgin and has never had a boyfriend or even had her first kiss." style "char_info_description"


screen scr_mm_characters_info_bella:
    imagebutton idle "bg_transparent" action NullAction()
    viewport:
        draggable True
        mousewheel True
        scrollbars "vertical"
        ymaximum 900
        xpos 0.2 ypos 0.05
        has vbox
        hbox:
            text "Name: " style "char_info_title"
            textbutton _("[b_name]") action Show('rename', var_name_to_change='b_name') text_style "char_info_button"


        hbox:
            text "Nicknames: " style "char_info_title"
            text "The Artist" style "char_info_description"
        hbox:
            text "Height: " style "char_info_title"
            text "1.75m (5ft7)" style "char_info_description"

        hbox:
            text "Age: " style "char_info_title"
            text "23" style "char_info_description"

        hbox:
            text "Positive Traits: " style "char_info_title"
            text "Creative - Extrovert - Decisive - Fun-loving - Independent - Free Spirit" style "char_info_description"

        hbox:
            text "Negative Traits: " style "char_info_title"
            text "Impatient - Bossy - Egotistical - Revengeful - Spiteful - Hot-headed" style "char_info_description"

        hbox:
            text "Occupation: " style "char_info_title"
            text "A clothing store in town." style "char_info_description"


        vbox:
            xmaximum 1200
            text ""
            text "[b_name] is stunningly beautiful, and she’s well aware of it!" style "char_info_description"
            text "However, she doesn’t like studying, which has prevented her from landing a high-paying job." style "char_info_description"
            text "Currently, she works at a clothing store, where she acquires the outfits and costumes the team needs for the various tasks or heists that they are assigned with." style "char_info_description"
            text "[b_name] has a strong passion for art and dreams of becoming a famous artist someday." style "char_info_description"
            text "Her best skills include creating fake paintings and jewellery. Her extensive fashion knowledge helps her design outfits and whatever else the team requires." style "char_info_description"
            text "[b_name]’s good looks and eye-catching figure allows her to flirt with men to get whatever she wants." style "char_info_description"


screen scr_mm_characters_info_vivian:
    imagebutton idle "bg_transparent" action NullAction()
    viewport:
        draggable True
        mousewheel True
        scrollbars "vertical"
        ymaximum 900
        xpos 0.2 ypos 0.05
        has vbox
        hbox:
            text "Name: " style "char_info_title"
            textbutton _("[v_name]") action Show('rename', var_name_to_change='v_name') text_style "char_info_button"


        hbox:
            text "Nicknames: " style "char_info_title"
            text "The Actress" style "char_info_description"
        hbox:
            text "Height: " style "char_info_title"
            text "1.75m (5ft7)" style "char_info_description"

        hbox:
            text "Age: " style "char_info_title"
            text "41" style "char_info_description"

        hbox:
            text "Positive Traits: " style "char_info_title"
            text "Friendly - Caring - Elegant - Loyal - Classy - Affectionate" style "char_info_description"

        hbox:
            text "Negative Traits: " style "char_info_title"
            text "Insecure - Self-conscious - Absent-minded - Naive" style "char_info_description"

        hbox:
            text "Occupation: " style "char_info_title"
            text "Waitress at a fancy restaurant." style "char_info_description"


        vbox:
            xmaximum 1200
            text ""
            text "[v_name] is the eldest female in the group, a former stage actress who once dreamed of becoming a movie superstar." style "char_info_description"
            text "After you, [b_name] and [a_name] arrived, she decided to spend more time focusing on the three of you instead." style "char_info_description"
            text "[v_name]’s contribution to the team is her ability to perform any acting role required for each job. She can imitate different accents or adopt any fake persona." style "char_info_description"
            text "While she’s a very talented actress, she is also very self-conscious and insecure." style "char_info_description"
            text "She worries about ageing and fears losing her beauty and youth." style "char_info_description"
            text "[v_name] has a soft spot for you, the only male among the three younger members." style "char_info_description"



screen scr_mm_characters_info_victor:
    imagebutton idle "bg_transparent" action NullAction()
    viewport:
        draggable True
        mousewheel True
        scrollbars "vertical"
        ymaximum 900
        xpos 0.2 ypos 0.05
        has vbox
        hbox:
            text "Name: " style "char_info_title"
            textbutton _("[vic_name]") action Show('rename', var_name_to_change='vic_name') text_style "char_info_button"


        hbox:
            text "Nicknames: " style "char_info_title"
            text "The Brain" style "char_info_description"
        hbox:
            text "Height: " style "char_info_title"
            text "1.85m (6ft1)" style "char_info_description"

        hbox:
            text "Age: " style "char_info_title"
            text "45" style "char_info_description"

        hbox:
            text "Positive Traits: " style "char_info_title"
            text "Smart - Decisive - Leader - Charismatic - Organised" style "char_info_description"

        hbox:
            text "Negative Traits: " style "char_info_title"
            text "Aggressive - Arrogant - Intolerant - Selfish" style "char_info_description"

        hbox:
            text "Occupation: " style "char_info_title"
            text "Limo Driver for rich people." style "char_info_description"


        vbox:
            xmaximum 1200
            text ""
            text "[vic_name] is the leader of the gang. He dropped out of college, got married young, and had to help support Vivian and the three of you." style "char_info_description"
            text "[vic_name] can manipulate anyone he wants. He’s methodical and learns new things with ease." style "char_info_description"
            text "As the brains of the team, he devises elaborate plans to steal things." style "char_info_description"
            text "He outlines the scam and heists for the group, explaining everyone’s roles beforehand. " style "char_info_description"
            text "Confident but strict, he rarely goes out into the field himself and will look to blame others if things go wrong." style "char_info_description"
            text "He aspires to live a wealthy lifestyle like the people he drives for as a chauffeur, but he knows he can’t achieve this legitimately so [vic_name] steals from them. " style "char_info_description"
            text "His dream is to land a big job that will allow him to retire." style "char_info_description"
            text "You want to be a leader like [vic_name], but without his mean, nasty streak that he sometimes exhibits towards you and the rest of the group." style "char_info_description"



screen scr_mm_characters_info_megan:
    imagebutton idle "bg_transparent" action NullAction()
    viewport:
        draggable True
        mousewheel True
        scrollbars "vertical"
        ymaximum 900
        xpos 0.2 ypos 0.05
        has vbox
        if v_megan_bio_info_unlocked:
            hbox:
                text "Name: " style "char_info_title"
                text "Megan" style "char_info_description"


            hbox:
                text "Nicknames: " style "char_info_title"
                text "Mrs. X" style "char_info_description"
            hbox:
                text "Height: " style "char_info_title"
                text "1.75m (5ft7)" style "char_info_description"

            hbox:
                text "Age: " style "char_info_title"
                text "38" style "char_info_description"

            hbox:
                text "Positive Traits: " style "char_info_title"
                text "Rich - Welcoming - Confident - Helpful" style "char_info_description"

            hbox:
                text "Negative Traits: " style "char_info_title"
                text "Obscure - Potentially Untrustworthy - Suspicious - Deceptive" style "char_info_description"

            hbox:
                text "Occupation: " style "char_info_title"
                text "Business Owner (TBD)" style "char_info_description"


            vbox:
                xmaximum 1200
                text ""
                text "After first meeting Megan, she seems like a genuine, caring person, willing to help someone out if they need it." style "char_info_description"
                text "Not only is she incredibly attractive and filthy rich, but she exudes confidence like a drug and she’s very much a woman" style "char_info_description"
                text "who knows what she wants (or doesn’t want)." style "char_info_description"
                text ""
                text "But the more you learn about Megan the more you’ll realise that not everything about her is as it seems." style "char_info_description"
                text "She has the potential to be your best friend or worst enemy." style "char_info_description"
                text ""
                text "Being her ally seems a safe enough option, but it could potentially have life-defining consequences " style "char_info_description"
                text "if you get on her bad side." style "char_info_description"
                text "Megan can really rock your world, but it’s also a good idea to tread very carefully..." style "char_info_description"
                text ""

        else:
            hbox:
                text "Name: " style "char_info_title"
                text "Megan" style "char_info_description"


            hbox:
                text "Nicknames: " style "char_info_title"
                text "Mrs. X" style "char_info_description"
            hbox:
                text "Height: " style "char_info_title"
                text "1.75m (5ft7)" style "char_info_description"

            hbox:
                text "Age: " style "char_info_title"
                text "??" style "char_info_description"

            hbox:
                text "Positive Traits: " style "char_info_title"
                text "??" style "char_info_description"

            hbox:
                text "Negative Traits: " style "char_info_title"
                text "??" style "char_info_description"

            hbox:
                text "Occupation: " style "char_info_title"
                text "??" style "char_info_description"


            vbox:
                xmaximum 1200
                text ""
                text "" style "char_info_description"


screen scr_mm_characters_info_juliet:
    imagebutton idle "bg_transparent" action NullAction()
    viewport:
        draggable True
        mousewheel True
        scrollbars "vertical"
        ymaximum 900
        xpos 0.2 ypos 0.05
        has vbox
        hbox:
            text "Name: " style "char_info_title"
            text "Juliet" style "char_info_description"


        hbox:
            text "Nicknames: " style "char_info_title"
            text "The Fitness Hottie" style "char_info_description"
        hbox:
            text "Height: " style "char_info_title"
            text "1.70m (5ft6)" style "char_info_description"

        hbox:
            text "Age: " style "char_info_title"
            text "21" style "char_info_description"

        hbox:
            text "Positive Traits: " style "char_info_title"
            text "Confident - Fit - Loves a Challenge - Persistent" style "char_info_description"

        hbox:
            text "Negative Traits: " style "char_info_title"
            text "Arrogant - Cocky - Easily Angered" style "char_info_description"

        hbox:
            text "Occupation: " style "char_info_title"
            text "Currently looking for work." style "char_info_description"


        vbox:
            xmaximum 1200
            text ""
            text "Juliet is a mysterious young woman, new to town, constantly seeking challenges." style "char_info_description"
            text "She’s fiercely independent, refuses to be told what to do, and knows how to handle herself." style "char_info_description"
            text "This girl doesn’t take shit from anybody, so be careful!" style "char_info_description"
            text "Juliet likes to make it known that she is well-skilled in various forms of martial arts, but just like you, her overconfidence and arrogant attitude is sometimes her achilles heel." style "char_info_description"
            text "She can be a real hothead when things don’t go her way, and getting even is the first thing on her mind if this happens." style "char_info_description"



screen scr_mm_characters_info_zora:
    imagebutton idle "bg_transparent" action NullAction()
    viewport:
        draggable True
        mousewheel True
        scrollbars "vertical"
        ymaximum 900
        xpos 0.2 ypos 0.05
        has vbox
        hbox:
            text "Name: " style "char_info_title"
            text "Zora" style "char_info_description"


        hbox:
            text "Nicknames: " style "char_info_title"
            text "The Rich Girl" style "char_info_description"
        hbox:
            text "Height: " style "char_info_title"
            text "1.65m (5ft4)" style "char_info_description"

        hbox:
            text "Age: " style "char_info_title"
            text "18" style "char_info_description"

        hbox:
            text "Positive Traits: " style "char_info_title"
            text "Friendly - Open-minded - Optimistic - Funny" style "char_info_description"

        hbox:
            text "Negative Traits: " style "char_info_title"
            text "Insecure - Shy - Lacks Confidence - Suffers From Anxiety" style "char_info_description"

        hbox:
            text "Occupation: " style "char_info_title"
            text "Cafe barista, Student" style "char_info_description"


        vbox:
            xmaximum 1200
            text ""
            text "Zora is an 18-year-old with red hair, green eyes, and freckles." style "char_info_description"
            text "She’s a shy, curvy young woman who feels self-conscious about her appearance." style "char_info_description"
            text "Zora is not fully comfortable with herself yet and just needs someone to help her break out of her shell and build genuine confidence." style "char_info_description"
            text "Currently, she’s a college student working toward a degree in Veterinary Medicine." style "char_info_description"






screen scr_mm_characters_info_justice:
    imagebutton idle "bg_transparent" action NullAction()
    viewport:
        draggable True
        mousewheel True
        scrollbars "vertical"
        ymaximum 900
        xpos 0.2 ypos 0.05
        has vbox
        hbox:
            text "Name: " style "char_info_title"
            text "Officer Justice" style "char_info_description"


        hbox:
            text "Nicknames: " style "char_info_title"
            text "???" style "char_info_description"
        hbox:
            text "Height: " style "char_info_title"
            text "1.71m (5ft6)" style "char_info_description"

        hbox:
            text "Age: " style "char_info_title"
            text "??" style "char_info_description"

        hbox:
            text "Positive Traits: " style "char_info_title"
            text "Persistent - Head-Strong - Focused - Determined" style "char_info_description"

        hbox:
            text "Negative Traits: " style "char_info_title"
            text "Suspicious - Deceptive - Bad Tempered" style "char_info_description"

        hbox:
            text "Occupation: " style "char_info_title"
            text "Police Officer" style "char_info_description"


        vbox:
            xmaximum 1200
            text ""
            text "Officer Justice is a member of the law enforcement in town." style "char_info_description"
            text "She’s assigned with investigating local robberies, trying to find clues" style "char_info_description"
            text "and any evidence that may help her capture these criminals." style "char_info_description"
            text "She’s as persistent as she is beautiful, but don’t let her striking good looks fool you." style "char_info_description"
            text "Officer Justice is no-nonsense, determined woman who she takes her job very seriously." style "char_info_description"
            text "And if an opportunity arises, she’s usually the first to take advantage of it." style "char_info_description"
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
