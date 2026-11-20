label relMenu:

    call screen relMenu
    
screen relMenu():
    tag menu
    add "ui/bg.jpg"
    
    use game_menu("Relationships"):
    
        grid 8 5:
            style_prefix "slot"

            xalign 0.5
            yalign 0.5
            xpos 650
            ypos 400
            yspacing 20
            xspacing 50
            
            vbox:
                imagebutton:
                    idle Transform("ui/relMenu/roleNana.png", zoom=1)
                    hover Transform("ui/relMenu/roleNana.png", zoom=0.95)
                    action ShowMenu("relAllison")
                    
                text "Allison":
                    size 20
                    xalign 0.5
            
            vbox:
                imagebutton:
                    idle Transform("ui/relMenu/roleJamila.png", zoom=1)
                    hover Transform("ui/relMenu/roleJamila.png", zoom=0.95)
                    action ShowMenu("relJamila")
                    
                text "Jamila":
                    size 20
                    xalign 0.5
            
            vbox:
                imagebutton:
                    idle Transform("ui/relMenu/roleAmy.png", zoom=1)
                    hover Transform("ui/relMenu/roleAmy.png", zoom=0.95)
                    action ShowMenu("relAmy")
                    
                text "Amy":
                    size 20
                    xalign 0.5
            
            vbox:
                imagebutton:
                    idle Transform("ui/relMenu/roleLiz.png", zoom=1)
                    hover Transform("ui/relMenu/roleLiz.png", zoom=0.95)
                    action ShowMenu("relLiz")
                    
                text "Liz":
                    size 20
                    xalign 0.5
            
            vbox:
                imagebutton:
                    idle Transform("ui/relMenu/roleCat.png", zoom=1)
                    hover Transform("ui/relMenu/roleCat.png", zoom=0.95)
                    action ShowMenu("relCat")
                    
                text "Cat":
                    size 20
                    xalign 0.5
            
            vbox:
                imagebutton:
                    idle Transform("ui/relMenu/roleShizuka.png", zoom=1)
                    hover Transform("ui/relMenu/roleShizuka.png", zoom=0.95)
                    action ShowMenu("relShizuka")
                    
                text "Shizuka":
                    size 20
                    xalign 0.5
            
            vbox:
                imagebutton:
                    idle Transform("ui/relMenu/roleAsami.png", zoom=1)
                    hover Transform("ui/relMenu/roleAsami.png", zoom=0.95)
                    action ShowMenu("relAsami")
                    
                text "Asami":
                    size 20
                    xalign 0.5
            
            vbox:
                imagebutton:
                    idle Transform("ui/relMenu/roleMolly.png", zoom=1)
                    hover Transform("ui/relMenu/roleMolly.png", zoom=0.95)
                    action ShowMenu("relMolly")
                    
                text "Molly":
                    size 20
                    xalign 0.5
            
            vbox:
                imagebutton:
                    idle Transform("ui/relMenu/rolePriya.png", zoom=1)
                    hover Transform("ui/relMenu/rolePriya.png", zoom=0.95)
                    action ShowMenu("relPriya")
                    
                text "Priya":
                    size 20
                    xalign 0.5
            
            vbox:
                imagebutton:
                    idle Transform("ui/relMenu/roleFiona.png", zoom=1)
                    hover Transform("ui/relMenu/roleFiona.png", zoom=0.95)
                    action ShowMenu("relFiona")
                    
                text "Fiona":
                    size 20
                    xalign 0.5
            
            vbox:
                imagebutton:
                    idle Transform("ui/relMenu/roleRiona.png", zoom=1)
                    hover Transform("ui/relMenu/roleRiona.png", zoom=0.95)
                    action ShowMenu("relRiona")
                    
                text "Riona":
                    size 20
                    xalign 0.5
            
            vbox:
                imagebutton:
                    idle Transform("ui/relMenu/roleEllie.png", zoom=1)
                    hover Transform("ui/relMenu/roleEllie.png", zoom=0.95)
                    action ShowMenu("relEllie")
                    
                text "Ellie":
                    size 20
                    xalign 0.5
            
            vbox:
                imagebutton:
                    idle Transform("ui/relMenu/roleElla.png", zoom=1)
                    hover Transform("ui/relMenu/roleElla.png", zoom=0.95)
                    action ShowMenu("relElla")
                    
                text "Ella":
                    size 20
                    xalign 0.5
            
            vbox:
                imagebutton:
                    idle Transform("ui/relMenu/roleAaliyah.png", zoom=1)
                    hover Transform("ui/relMenu/roleAaliyah.png", zoom=0.95)
                    action ShowMenu("relAaliyah")
                    
                text "Aaliyah":
                    size 20
                    xalign 0.5
            
            vbox:
                imagebutton:
                    idle Transform("ui/relMenu/roleJada.png", zoom=1)
                    hover Transform("ui/relMenu/roleJada.png", zoom=0.95)
                    action ShowMenu("relJada")
                    
                text "Jada":
                    size 20
                    xalign 0.5
            
            vbox:
                imagebutton:
                    idle Transform("ui/relMenu/roleNatalia.png", zoom=1)
                    hover Transform("ui/relMenu/roleNatalia.png", zoom=0.95)
                    action ShowMenu("relNatalia")
                    
                text "Natalia":
                    size 20
                    xalign 0.5
            
            vbox:
                imagebutton:
                    idle Transform("ui/relMenu/roleOphelia.png", zoom=1)
                    hover Transform("ui/relMenu/roleOphelia.png", zoom=0.95)
                    action ShowMenu("relOphelia")
                    
                text "Ophelia":
                    size 20
                    xalign 0.5
            
            vbox:
                imagebutton:
                    idle Transform("ui/relMenu/roleAnnabelle.png", zoom=1)
                    hover Transform("ui/relMenu/roleAnnabelle.png", zoom=0.95)
                    action ShowMenu("relAnnabelle")
                    
                text "Annabelle":
                    size 20
                    xalign 0.5
            
            vbox:
                imagebutton:
                    idle Transform("ui/relMenu/roleSoph.png", zoom=1)
                    hover Transform("ui/relMenu/roleSoph.png", zoom=0.95)
                    action ShowMenu("relSophia")
                    
                text "Sophia":
                    size 20
                    xalign 0.5
            
            vbox:
                imagebutton:
                    idle Transform("ui/relMenu/roleMabel.png", zoom=1)
                    hover Transform("ui/relMenu/roleMabel.png", zoom=0.95)
                    action ShowMenu("relMabel")
                    
                text "Mabel":
                    size 20
                    xalign 0.5
            
            vbox:
                imagebutton:
                    idle Transform("ui/relMenu/roleSandra.png", zoom=1)
                    hover Transform("ui/relMenu/roleSandra.png", zoom=0.95)
                    action ShowMenu("relSandra")
                    
                text "Sandra":
                    size 20
                    xalign 0.5
            
            vbox:
                imagebutton:
                    idle Transform("ui/relMenu/roleJasmine.png", zoom=1)
                    hover Transform("ui/relMenu/roleJasmine.png", zoom=0.95)
                    action ShowMenu("relJasmine")
                    
                text "Jasmine":
                    size 20
                    xalign 0.5
            
            vbox:
                imagebutton:
                    idle Transform("ui/relMenu/roleTanya.png", zoom=1)
                    hover Transform("ui/relMenu/roleTanya.png", zoom=0.95)
                    action ShowMenu("relTanya")
                    
                text "Tanya":
                    size 20
                    xalign 0.5
            
            vbox:
                imagebutton:
                    idle Transform("ui/relMenu/roleVeena.png", zoom=1)
                    hover Transform("ui/relMenu/roleVeena.png", zoom=0.95)
                    action ShowMenu("relVeena")
                    
                text "Veena":
                    size 20
                    xalign 0.5
            
            vbox:
                imagebutton:
                    idle Transform("ui/relMenu/roleMinnie.png", zoom=1)
                    hover Transform("ui/relMenu/roleMinnie.png", zoom=0.95)
                    action ShowMenu("relMinnie")
                    
                text "Minnie":
                    size 20
                    xalign 0.5
            
            vbox:
                imagebutton:
                    idle Transform("ui/relMenu/roleMila.png", zoom=1)
                    hover Transform("ui/relMenu/roleMila.png", zoom=0.95)
                    action ShowMenu("relMila")
                    
                text "Mila":
                    size 20
                    xalign 0.5
            
            vbox:
                imagebutton:
                    idle Transform("ui/relMenu/roleSvetlana.png", zoom=1)
                    hover Transform("ui/relMenu/roleSvetlana.png", zoom=0.95)
                    action ShowMenu("relSvetlana")
                    
                text "Svetlana":
                    size 20
                    xalign 0.5
            
            vbox:
                imagebutton:
                    idle Transform("ui/relMenu/roleIsabella.png", zoom=1)
                    hover Transform("ui/relMenu/roleIsabella.png", zoom=0.95)
                    action ShowMenu("relIsabella")
                    
                text "Isabella":
                    size 20
                    xalign 0.5
            
            vbox:
                imagebutton:
                    idle Transform("ui/relMenu/rolePolly.png", zoom=1)
                    hover Transform("ui/relMenu/rolePolly.png", zoom=0.95)
                    action ShowMenu("relPolly")
                    
                text "Polly":
                    size 20
                    xalign 0.5
            
            vbox:
                imagebutton:
                    idle Transform("ui/relMenu/roleZelda.png", zoom=1)
                    hover Transform("ui/relMenu/roleZelda.png", zoom=0.95)
                    action ShowMenu("relZelda")
                    
                text "Zelda":
                    size 20
                    xalign 0.5
            
            vbox:
                imagebutton:
                    idle Transform("ui/relMenu/roleBetty.png", zoom=1)
                    hover Transform("ui/relMenu/roleBetty.png", zoom=0.95)
                    action ShowMenu("relBetty")
                    
                text "Betty":
                    size 20
                    xalign 0.5
            
            vbox:
                imagebutton:
                    idle Transform("ui/relMenu/roleMaria.png", zoom=1)
                    hover Transform("ui/relMenu/roleMaria.png", zoom=0.95)
                    action ShowMenu("relMaria")
                    
                text "Maria":
                    size 20
                    xalign 0.5
            
            vbox:
                imagebutton:
                    idle Transform("ui/relMenu/roleJosianne.png", zoom=1)
                    hover Transform("ui/relMenu/roleJosianne.png", zoom=0.95)
                    action ShowMenu("relJosianne")
                    
                text "Josianne":
                    size 20
                    xalign 0.5
            
            vbox:
                imagebutton:
                    idle Transform("ui/relMenu/roleLily.png", zoom=1)
                    hover Transform("ui/relMenu/roleLily.png", zoom=0.95)
                    action ShowMenu("relLily")
                    
                text "Lily":
                    size 20
                    xalign 0.5
            
            vbox:
                imagebutton:
                    idle Transform("ui/relMenu/roleKaren.png", zoom=1)
                    hover Transform("ui/relMenu/roleKaren.png", zoom=0.95)
                    action ShowMenu("relKaren")
                    
                text "Karen":
                    size 20
                    xalign 0.5
            
            # vbox:
                # imagebutton:
                    # idle Transform("ui/relMenu/roleAiko.png", zoom=1)
                    # hover Transform("ui/relMenu/roleAiko.png", zoom=0.95)
                    # action ShowMenu("relAiko")
                    
                # text "Aiko":
                    # size 20
                    # xalign 0.5
            
            # vbox:
                # imagebutton:
                    # idle Transform("ui/relMenu/roleShawna.png", zoom=1)
                    # hover Transform("ui/relMenu/roleShawna.png", zoom=0.95)
                    # action ShowMenu("relShawna")
                    
                # text "Shawna":
                    # size 20
                    # xalign 0.5
            
            # vbox:
                # imagebutton:
                    # idle Transform("ui/relMenu/roleYvonne.png", zoom=1)
                    # hover Transform("ui/relMenu/roleYvonne.png", zoom=0.95)
                    # action ShowMenu("relYvonne")
                    
                # text "Yvonne":
                    # size 20
                    # xalign 0.5
            
            # vbox:
                # imagebutton:
                    # idle Transform("ui/relMenu/roleLina.png", zoom=1)
                    # hover Transform("ui/relMenu/roleLina.png", zoom=0.95)
                    # action ShowMenu("relLina")
                    
                # text "Lina":
                    # size 20
                    # xalign 0.5
            
            # vbox:
                # imagebutton:
                    # idle Transform("ui/relMenu/roleElaine.png", zoom=1)
                    # hover Transform("ui/relMenu/roleElaine.png", zoom=0.95)
                    # action ShowMenu("relElaine")
                    
                # text "Elaine":
                    # size 20
                    # xalign 0.5
            
            vbox:
                imagebutton:
                    idle Transform("ui/relMenu/empty.png", zoom=1)
                    # hover Transform("ui/relMenu/roleNana.png", zoom=0.95)
                    # action ShowMenu("relAllison")
                    
                # text "Allison":
                    # size 20
                    # xalign 0.5
            
            vbox:
                imagebutton:
                    idle Transform("ui/relMenu/empty.png", zoom=1)
                    # hover Transform("ui/relMenu/roleNana.png", zoom=0.95)
                    # action ShowMenu("relAllison")
                    
                # text "Allison":
                    # size 20
                    # xalign 0.5
            
            vbox:
                imagebutton:
                    idle Transform("ui/relMenu/empty.png", zoom=1)
                    # hover Transform("ui/relMenu/roleNana.png", zoom=0.95)
                    # action ShowMenu("relAllison")
                    
                # text "Allison":
                    # size 20
                    # xalign 0.5
            
            vbox:
                imagebutton:
                    idle Transform("ui/relMenu/empty.png", zoom=1)
                    # hover Transform("ui/relMenu/roleNana.png", zoom=0.95)
                    # action ShowMenu("relAllison")
                    
                # text "Allison":
                    # size 20
                    # xalign 0.5
            
            vbox:
                imagebutton:
                    idle Transform("ui/relMenu/empty.png", zoom=1)
                    # hover Transform("ui/relMenu/roleNana.png", zoom=0.95)
                    # action ShowMenu("relAllison")
                    
                # text "Allison":
                    # size 20
                    # xalign 0.5
            
            # vbox:
                # imagebutton:
                    # idle Transform("ui/relMenu/empty.png", zoom=1)
                    # hover Transform("ui/relMenu/roleNana.png", zoom=0.95)
                    # action ShowMenu("relAllison")
                    
                # text "Allison":
                    # size 20
                    # xalign 0.5
                    
            # vbox:
                # imagebutton:
                    # idle Transform("ui/relMenu/empty.png", zoom=1)
            # vbox:
                # imagebutton:
                    # idle Transform("ui/relMenu/empty.png", zoom=1)
            # vbox:
                # imagebutton:
                    # idle Transform("ui/relMenu/empty.png", zoom=1)
            # vbox:
                # imagebutton:
                    # idle Transform("ui/relMenu/empty.png", zoom=1)
            # vbox:
                # imagebutton:
                    # idle Transform("ui/relMenu/empty.png", zoom=1)
            
                        
screen relAllison():
    tag menu
    add "ui/bg.jpg"
    
    use game_menu("Relationships"):
    
        add "ui/relMenu/relNana.png" zoom 0.8 xoffset -175 yoffset -22
            
        vbox:
        
            box_wrap True
            xalign 0.9
            yalign 0.1
            spacing 10
        
            text _("Name: Allison [nLastName]"):
                color gui.hover_color
                
            text _("Age: 61"):
                color gui.hover_color
                
            text _("Marital Status: Widowed"):
                color gui.hover_color
                
            text _("Relationship: [gm!c] and Girlfriend"):
                color gui.hover_color
                
            text _("Occupation: Landlady"):
                color gui.hover_color
                
            # text _("Pregnant: [nnPreg]"):
                # color gui.hover_color
                
            text _("Likes: You, Molly, Her Family, Her Friends, Cuddling, Cooking"):
                color gui.hover_color
                
            text _("Dislikes: Cursing, Slow Drivers, Motorcycles, Priya's Family"):
                color gui.hover_color
                
screen relJamila():
    tag menu
    add "ui/bg.jpg"
    
    use game_menu("Relationships"):
    
        add "ui/relMenu/relJamila.png" zoom 0.8 xoffset -175 yoffset -22
            
        vbox:
        
            box_wrap True
            xalign 0.6
            yalign 0.1
            spacing 10
        
            text "Name: Jamila Hafeez":
                color gui.hover_color
                
            text _("Age: 56"):
                color gui.hover_color
                
            text _("Marital Status: Separated"):
                color gui.hover_color
                
            text _("Relationship: [m!c] and Girlfriend"):
                color gui.hover_color
                
            text _("Occupation: Cashier"):
                color gui.hover_color
                
            # text _("Pregnant: [jamPreg]"):
                # color gui.hover_color
                
            text _("Likes: You, Cooking, Foot Rubs, Singing"):
                color gui.hover_color
                
            text _("Dislikes: Fast Food, Vanity, Laziness"):
                color gui.hover_color
                
screen relAmy():
    tag menu
    add "ui/bg.jpg"
    
    use game_menu("Relationships"):
    
        add "ui/relMenu/relAmy.png" zoom 0.8 xoffset -175 yoffset -22
            
        vbox:
        
            box_wrap True
            xalign 0.9
            yalign 0.1
            spacing 10
        
            text "Name: Amelia [nLastName]":
                color gui.hover_color
                
            text _("Age: 39"):
                color gui.hover_color
                
            text _("Marital Status: Single"):
                color gui.hover_color
                
            text _("Relationship: [au!c]"):
                color gui.hover_color
                
            text _("Occupation: Makeup Artist"):
                color gui.hover_color
                
            # text _("Pregnant: [amyPreg]"):
                # color gui.hover_color
                
            text _("Likes: You, Traveling, French Food, Animals, Shopping"):
                color gui.hover_color
                
            text _("Dislikes: Bees, Rude People, Broccoli"):
                color gui.hover_color
                
screen relLiz():
    tag menu
    add "ui/bg.jpg"
    
    use game_menu("Relationships"):
    
        add "ui/relMenu/relLiz.png" zoom 0.8 xoffset -175 yoffset -22
            
        vbox:
        
            box_wrap True
            xalign 0.6
            yalign 0.1
            spacing 10
        
            text _("Name: Elizabeth [nLastName]"):
                color gui.hover_color
                
            text _("Age: 37"):
                color gui.hover_color
                
            text _("Marital Status: Single"):
                color gui.hover_color
                
            text _("Relationship: [au!c] and Girlfriend"):
                color gui.hover_color
                
            text _("Occupation: Waitress and Cashier"):
                color gui.hover_color
                
            # text _("Pregnant: [lizPreg]"):
                # color gui.hover_color
                
            text _("Likes: You, Swimming, Animals, Drinking"):
                color gui.hover_color
                
            text _("Dislikes: Cooking, Pity, Driving"):
                color gui.hover_color
                
screen relCat():
    tag menu
    add "ui/bg.jpg"
    
    use game_menu("Relationships"):
    
        add "ui/relMenu/relCat.png" zoom 0.8 xoffset -175 yoffset -22
            
        vbox:
        
            box_wrap True
            xalign 0.9
            yalign 0.1
            spacing 10
        
            text _("Name: Catherine [nLastName]"):
                color gui.hover_color
                
            text _("Age: 19"):
                color gui.hover_color
                
            text _("Marital Status: Single"):
                color gui.hover_color
                
            text _("Relationship: [cs!c] and Girlfriend"):
                color gui.hover_color
                
            text _("Occupation: Unemployed"):
                color gui.hover_color
                
            # text _("Pregnant: [catPreg]"):
                # color gui.hover_color
                
            text _("Likes: You, Artichoke, [catMcNick]'s Milk"):
                color gui.hover_color
                
            text _("Dislikes: Thunderstorms, Mean People, Horror Movies"):
                color gui.hover_color
                
screen relShizuka():
    tag menu
    add "ui/bg.jpg"
    
    use game_menu("Relationships"):
    
        add "ui/relMenu/relShizuka.png" zoom 0.8 xoffset -175 yoffset -22
            
        vbox:
        
            box_wrap True
            xalign 0.9
            yalign 0.1
            spacing 10
        
            text "Name: Shizuka":
                color gui.hover_color
                
            text _("Age: 20"):
                color gui.hover_color
                
            text _("Marital Status: Single"):
                color gui.hover_color
                
            text _("Relationship: Maid, girlfriend and Snuggle Bug"):
                color gui.hover_color
                
            text _("Occupation: Maid"):
                color gui.hover_color
                
            # text _("Pregnant: [shizukaPreg]"):
                # color gui.hover_color
                
            text _("Likes: You, Belly Rubs, Bacon Cheeseburgers, Dogs"):
                color gui.hover_color
                
            text _("Dislikes: Mean People"):
                color gui.hover_color
                
screen relAsami():
    tag menu
    add "ui/bg.jpg"
    
    use game_menu("Relationships"):
    
        add "ui/relMenu/relAsami.png" zoom 0.8 xoffset -175 yoffset -22
            
        vbox:
        
            box_wrap True
            xalign 0.4
            yalign 0.1
            spacing 10
        
            text "Name: Asami":
                color gui.hover_color
                
            text _("Age: 49"):
                color gui.hover_color
                
            text _("Marital Status: Widowed"):
                color gui.hover_color
                
            text _("Relationship: Maid, girlfriend and Snuggle Bunny"):
                color gui.hover_color
                
            text _("Occupation: Maid"):
                color gui.hover_color
                
            # text _("Pregnant: [asamiPreg]"):
                # color gui.hover_color
                
            text _("Likes: Kind People"):
                color gui.hover_color
                
            text _("Dislikes: Mean People"):
                color gui.hover_color
                
screen relMolly():
    tag menu
    add "ui/bg.jpg"
    
    use game_menu("Relationships"):
    
        add "ui/relMenu/relMolly.png" zoom 0.8 xoffset -175 yoffset -22
            
        vbox:
        
            box_wrap True
            xalign 0.5
            yalign 0.1
            spacing 10
        
            text "Name: Molly":
                color gui.hover_color
                
            text _("Age: 3"):
                color gui.hover_color
                
            text _("Status: Terrified"):
                color gui.hover_color
                
            text _("Relationship: Best Girl"):
                color gui.hover_color
                
            text _("Occupation: Cowering in Fear"):
                color gui.hover_color
                
            text _("Likes: [nname], Shizuka, You, Washing Machines"):
                color gui.hover_color
                
            text _("Dislikes: Butterflies, Ants, Vacuums"):
                color gui.hover_color
                
screen relPriya():
    tag menu
    add "ui/bg.jpg"
    
    use game_menu("Relationships"):
    
        add "ui/relMenu/relPriya.png" zoom 0.8 xoffset -175 yoffset -22
            
        vbox:
        
            box_wrap True
            xalign 0.6
            yalign 0.1
            spacing 10
        
            text "Name: Priya Patel":
                color gui.hover_color
                
            text _("Age: 56"):
                color gui.hover_color
                
            text _("Marital Status: Married"):
                color gui.hover_color
                
            if docPoints>1:
                text _("Relationship: Girlfriend"):
                    color gui.hover_color
            else:
                text _("Relationship: [fam!c] Friend"):
                    color gui.hover_color
                
            text _("Occupation: Doctor"):
                color gui.hover_color
                
            # text _("Pregnant: [priyaPreg]"):
                # color gui.hover_color
                
            text _("Likes: You, Babies, Charity Work, Dancing"):
                color gui.hover_color
                
            text _("Dislikes: Her Infertility, Infidelity, Greed"):
                color gui.hover_color
                
screen relFiona():
    tag menu
    add "ui/bg.jpg"
    
    use game_menu("Relationships"):
    
        add "ui/relMenu/relFiona.png" zoom 0.8 xoffset -175 yoffset -22
            
        vbox:
        
            box_wrap True
            xalign 0.7
            yalign 0.1
            spacing 10
        
            text "Name: Fiona [ori]":
                color gui.hover_color
                
            text _("Age: 26"):
                color gui.hover_color
                
            text _("Marital Status: Single"):
                color gui.hover_color
                
            if fiPoints>0:
                text _("Relationship: Girlfriend"):
                    color gui.hover_color
            else:
                text _("Relationship: Acquaintance"):
                    color gui.hover_color
                
            text _("Occupation: Bartender"):
                color gui.hover_color
                
            # text _("Pregnant: [fionaPreg]"):
                # color gui.hover_color
                
            text _("Likes: You, Competing, Her [fam!c], OSHA Violations"):
                color gui.hover_color
                
            text _("Dislikes: Losing, Weakness, Gin"):
                color gui.hover_color
                
screen relRiona():
    tag menu
    add "ui/bg.jpg"
    
    use game_menu("Relationships"):
    
        add "ui/relMenu/relRiona.png" zoom 0.8 xoffset -175 yoffset -22
            
        vbox:
        
            box_wrap True
            xalign 0.6
            yalign 0.1
            spacing 10
        
            text "Name: Riona [ori]":
                color gui.hover_color
                
            text _("Age: 52"):
                color gui.hover_color
                
            text _("Marital Status: Widowed"):
                color gui.hover_color
                
            if riPoints>0:
                text _("Relationship: Girlfriend"):
                    color gui.hover_color
            elif fiPoints<1:
                text _("Relationship: None"):
                    color gui.hover_color
            else:
                text _("Relationship: Acquaintance"):
                    color gui.hover_color
                
            text _("Occupation: Bookkeeper and Cook"):
                color gui.hover_color
                
            # text _("Pregnant: [rionaPreg]"):
                # color gui.hover_color
                
            text _("Likes: Her [d!c]s, Winning, Confidence"):
                color gui.hover_color
                
            text _("Dislikes: Losing, Asparagus, Cucks"):
                color gui.hover_color
                
screen relEllie():
    tag menu
    add "ui/bg.jpg"
    
    use game_menu("Relationships"):
    
        add "ui/relMenu/relEllie.png" zoom 0.8 xoffset -175 yoffset -22
            
        vbox:
        
            box_wrap True
            xalign 0.6
            yalign 0.1
            spacing 10
        
            text "Name: Ellie [ori]":
                color gui.hover_color
                
            text _("Age: 21"):
                color gui.hover_color
                
            text _("Marital Status: Single"):
                color gui.hover_color
                
            if twnPoints>0:
                text _("Relationship: Girlfriend"):
                    color gui.hover_color
            elif fiPoints<1:
                text _("Relationship: None"):
                    color gui.hover_color
            else:
                text _("Relationship: Acquaintance"):
                    color gui.hover_color
                
            text _("Occupation: Waitress"):
                color gui.hover_color
                
            # text _("Pregnant: [twnPreg]"):
                # color gui.hover_color
                
            text _("Likes: Cuddling, Turtles, Painting"):
                color gui.hover_color
                
            text _("Dislikes: Dubstep, Wearing Pants, Fish"):
                color gui.hover_color
                
screen relElla():
    tag menu
    add "ui/bg.jpg"
    
    use game_menu("Relationships"):
    
        add "ui/relMenu/relElla.png" zoom 0.8 xoffset -175 yoffset -22
            
        vbox:
        
            box_wrap True
            xalign 0.85
            yalign 0.1
            spacing 10
        
            text "Name: Ella [ori]":
                color gui.hover_color
                
            text _("Age: 21"):
                color gui.hover_color
                
            text _("Marital Status: Single"):
                color gui.hover_color
                
            if twnPoints>0:
                text _("Relationship: Girlfriend"):
                    color gui.hover_color
            elif fiPoints<1:
                text _("Relationship: None"):
                    color gui.hover_color
            else:
                text _("Relationship: Acquaintance"):
                    color gui.hover_color
                
            text _("Occupation: Waitress"):
                color gui.hover_color
                
            # text _("Pregnant: [twnPreg]"):
                # color gui.hover_color
                
            text _("Likes: Masturbating, AVNs, Masturbating While Playing AVNs"):
                color gui.hover_color
                
            text _("Dislikes: Not Masturbating, Wearing Clothes, Fish"):
                color gui.hover_color
                
screen relAaliyah():
    tag menu
    add "ui/bg.jpg"
    
    use game_menu("Relationships"):
    
        add "ui/relMenu/relAaliyah.png" zoom 0.8 xoffset -175 yoffset -22
            
        vbox:
        
            box_wrap True
            xalign 0.6
            yalign 0.1
            spacing 10
        
            text "Name: Aaliyah":
                color gui.hover_color
                
            text _("Age: 19"):
                color gui.hover_color
                
            text _("Marital Status: Single"):
                color gui.hover_color
                
            if aalPoints>1:
                text _("Relationship: Girlfriend"):
                    color gui.hover_color
            elif aalPoints<2:
                text _("Relationship: Friend"):
                    color gui.hover_color
                
            text _("Occupation: Cashier"):
                color gui.hover_color
                
            # text _("Pregnant: [aaliyahPreg]"):
                # color gui.hover_color
                
            text _("Likes: You, Swimming, Vanilla Ice Cream"):
                color gui.hover_color
                
            text _("Dislikes: Laziness, Her [dd!c], Smoking"):
                color gui.hover_color
                
screen relJada():
    tag menu
    add "ui/bg.jpg"
    
    use game_menu("Relationships"):
    
        add "ui/relMenu/relJada.png" zoom 0.8 xoffset -175 yoffset -22
            
        vbox:
        
            box_wrap True
            xalign 0.6
            yalign 0.1
            spacing 10
        
            text "Name: Jada":
                color gui.hover_color
                
            text _("Age: 43"):
                color gui.hover_color
                
            text _("Marital Status: Married"):
                color gui.hover_color
                
            if jadaPoints>0:
                text _("Relationship: Girlfriend"):
                    color gui.hover_color
            elif aalPoints<1:
                text _("Relationship: Friend"):
                    color gui.hover_color
                
            text _("Occupation: Retired Fashion Model"):
                color gui.hover_color
                
            # text _("Pregnant: [jadaPreg]"):
                # color gui.hover_color
                
            text _("Likes: You, Shopping, Fashion"):
                color gui.hover_color
                
            text _("Dislikes: Her husband"):
                color gui.hover_color
                
screen relNatalia():
    tag menu
    add "ui/bg.jpg"
    
    use game_menu("Relationships"):
    
        add "ui/relMenu/relNatalia.png" zoom 0.8 xoffset -175 yoffset -22
            
        vbox:
        
            box_wrap True
            xalign 0.6
            yalign 0.1
            spacing 10
        
            text "Name: Natalia":
                color gui.hover_color
                
            text _("Age: 38"):
                color gui.hover_color
                
            text _("Marital Status: Married"):
                color gui.hover_color
                
            if nbrPoints<1:
                text _("Relationship: Acquaintance"):
                    color gui.hover_color
            elif nbrPoints>0:
                text "Relationship: Girlfriend":
                    color gui.hover_color
                
            text _("Occupation: Homemaker"):
                color gui.hover_color
                
            # text _("Pregnant: [nataliaPreg]"):
                # color gui.hover_color
                
            text _("Likes: Gardening, Tanning, Italian Soap Operas"):
                color gui.hover_color
                
            text _("Dislikes: Herself"):
                color gui.hover_color
                
screen relOphelia():
    tag menu
    add "ui/bg.jpg"
    
    use game_menu("Relationships"):
    
        add "ui/relMenu/relOphelia.png" zoom 0.8 xoffset -175 yoffset -22
            
        vbox:
        
            box_wrap True
            xalign 0.9
            yalign 0.1
            spacing 10
        
            text "Name: Ophelia":
                color gui.hover_color
                
            text _("Age: 71"):
                color gui.hover_color
                
            text _("Marital Status: Widowed"):
                color gui.hover_color
                
            if ophPoints<1:
                text _("Relationship: [fam!c] Friend"):
                    color gui.hover_color
            elif ophPoints>0:
                text _("Relationship: Girlfriend"):
                    color gui.hover_color
                
            text _("Occupation: CEO of an Investment Firm"):
                color gui.hover_color
                
            # text _("Pregnant: [opheliaPreg]"):
                # color gui.hover_color
                
            text _("Likes: People Who Take Initiative, Exercise, Discipline"):
                color gui.hover_color
                
            text _("Dislikes: Annabelle's Behavior, Spoiled People, Laziness"):
                color gui.hover_color
                
screen relAnnabelle():
    tag menu
    add "ui/bg.jpg"
    
    use game_menu("Relationships"):
    
        add "ui/relMenu/relAnnabelle.png" zoom 0.8 xoffset -175 yoffset -22
            
        vbox:
        
            box_wrap True
            xalign 0.6
            yalign 0.1
            spacing 10
        
            text "Name: Annabelle":
                color gui.hover_color
                
            text _("Age: 44"):
                color gui.hover_color
                
            text _("Marital Status: Single"):
                color gui.hover_color
                
            if anaPoints<1:
                text _("Relationship: Acquaintance"):
                    color gui.hover_color
            elif anaPoints>0:
                text _("Relationship: Daughter-Girlfriend"):
                    color gui.hover_color
                
            text _("Occupation: Spoiled Brat"):
                color gui.hover_color
                
            # text _("Pregnant: [annabellePreg]"):
                # color gui.hover_color
                
            text _("Likes: Shopping, Sleeping, Tanning"):
                color gui.hover_color
                
            text _("Dislikes: You, Men, Working, Bananas"):
                color gui.hover_color
                
screen relSophia():
    tag menu
    add "ui/bg.jpg"
    
    use game_menu("Relationships"):
    
        add "ui/relMenu/relSophia.png" zoom 0.8 xoffset -175 yoffset -22
            
        vbox:
        
            box_wrap True
            xalign 0.7
            yalign 0.1
            spacing 10
        
            text "Name: Sophia":
                color gui.hover_color
                
            text _("Age: 19"):
                color gui.hover_color
                
            text "Marital Status: Single":
                color gui.hover_color
                
            if sophPoints<1:
                text _("Relationship: Acquaintance"):
                    color gui.hover_color
            elif sophPoints>0:
                text _("Relationship: [ss!c]-Girlfriend"):
                    color gui.hover_color
                
            text _("Occupation: Unemployed"):
                color gui.hover_color
                
            # text _("Pregnant: [sophiaPreg]"):
                # color gui.hover_color
                
            text _("Likes: You, Dry Humping Things, Gymnastics, Chess"):
                color gui.hover_color
                
            text _("Dislikes: Heights, Cauliflower, Checkers"):
                color gui.hover_color
                
screen relMabel():
    tag menu
    add "ui/bg.jpg"
    
    use game_menu("Relationships"):
    
        add "ui/relMenu/relMabel.png" zoom 0.8 xoffset -175 yoffset -22
            
        vbox:
        
            box_wrap True
            xalign 0.6
            yalign 0.1
            spacing 10
        
            text "Name: Mabel":
                color gui.hover_color
                
            text _("Age: 66"):
                color gui.hover_color
                
            text _("Marital Status: Widowed"):
                color gui.hover_color
                
            if mblPoints<1:
                text _("Relationship: [fam!c] Friend"):
                    color gui.hover_color
            elif mblPoints>0:
                text _("Relationship: Girlfriend"):
                    color gui.hover_color
                
            text _("Occupation: Landlady"):
                color gui.hover_color
                
            # text _("Pregnant: [mabelPreg]"):
                # color gui.hover_color
                
            text _("Likes: You, Reading, Her Grandkids"):
                color gui.hover_color
                
            text _("Dislikes: Growing Old, Crowds, Loud Music"):
                color gui.hover_color
                
screen relSandra():
    tag menu
    add "ui/bg.jpg"
    
    use game_menu("Relationships"):
    
        add "ui/relMenu/relSandra.png" zoom 0.8 xoffset -175 yoffset -22
            
        vbox:
        
            box_wrap True
            xalign 0.8
            yalign 0.1
            spacing 10
        
            text "Name: Sandra":
                color gui.hover_color
                
            text _("Age: 27"):
                color gui.hover_color
                
            text _("Marital Status: Single"):
                color gui.hover_color
                
            if copPoints<1:
                text _("Relationship: None"):
                    color gui.hover_color
            elif copPoints>0:
                text _("Relationship: [mcCopNick]"):
                    color gui.hover_color
                
            text _("Occupation: Police Officer"):
                color gui.hover_color
                
            # text _("Pregnant: [sandraPreg]"):
                # color gui.hover_color
                
            text _("Likes: You, Catching Criminals, Being in Charge"):
                color gui.hover_color
                
            text _("Dislikes: Weakness, Bullies, Pigeons"):
                color gui.hover_color
                
screen relJasmine():
    tag menu
    add "ui/bg.jpg"
    
    use game_menu("Relationships"):
    
        add "ui/relMenu/relJasmine.png" zoom 0.8 xoffset -175 yoffset -22
            
        vbox:
        
            box_wrap True
            xalign 0.9
            yalign 0.1
            spacing 10
        
            text "Name: Jasmine":
                color gui.hover_color
                
            text _("Age: 29"):
                color gui.hover_color
                
            text _("Marital Status: Single"):
                color gui.hover_color
                
            if jasPoints<1:
                text _("Relationship: Acquaintance"):
                    color gui.hover_color
            elif jasPoints>0:
                text _("Relationship: Daughter-Girlfriend"):
                    color gui.hover_color
                
            text _("Occupation: Martial Arts Instructor"):
                color gui.hover_color
                
            # text _("Pregnant: [jasminePreg]"):
                # color gui.hover_color
                
            text _("Likes: Discipline, Strength, Cats"):
                color gui.hover_color
                
            text _("Dislikes: Weakness, Helplessness, Violence"):
                color gui.hover_color
                
screen relTanya():
    tag menu
    add "ui/bg.jpg"
    
    use game_menu("Relationships"):
    
        add "ui/relMenu/relTanya.png" zoom 0.8 xoffset -175 yoffset -22
            
        vbox:
        
            box_wrap True
            xalign 0.7
            yalign 0.1
            spacing 10
        
            text "Name: Tanya":
                color gui.hover_color
                
            text _("Age: 21"):
                color gui.hover_color
                
            text _("Marital Status: Single"):
                color gui.hover_color
                
            if tyaPoints<1:
                text _("Relationship: Ex-Girlfriend"):
                    color gui.hover_color
            elif tyaPoints>0:
                text _("Relationship: Girlfriend"):
                    color gui.hover_color
                
            text _("Occupation: Unemployed"):
                color gui.hover_color
                
            # text _("Pregnant: [tanyaPreg]"):
                # color gui.hover_color
                
            text _("Likes: You, Playing The Violin, Romantic Movies"):
                color gui.hover_color
                
            text _("Dislikes: Cursing, Horror Movies, Country Music"):
                color gui.hover_color
                
screen relVeena():
    tag menu
    add "ui/bg.jpg"
    
    use game_menu("Relationships"):
    
        add "ui/relMenu/relVeena.png" zoom 0.8 xoffset -175 yoffset -22
            
        vbox:
        
            box_wrap True
            xalign 0.95
            yalign 0.1
            spacing 10
        
            text "Name: Paveena Patel":
                color gui.hover_color
                
            text _("Age: 35"):
                color gui.hover_color
                
            text _("Marital Status: Married"):
                color gui.hover_color
                
            if pavPoints<1:
                text _("Relationship: None"):
                    color gui.hover_color
            elif pavPoints>0:
                text _("Relationship: Wife"):
                    color gui.hover_color
                
            text _("Occupation: Homemaker"):
                color gui.hover_color
                
            # text _("Pregnant: [veenaPreg]"):
                # color gui.hover_color
                
            text _("Likes: Romance, Love, Poetry"):
                color gui.hover_color
                
            text _("Dislikes: Her Husband, Her [br!c]-in-Law, Ranch Dressing"):
                color gui.hover_color
                
screen relMinnie():
    tag menu
    add "ui/bg.jpg"
    
    use game_menu("Relationships"):
    
        add "ui/relMenu/relMinnie.png" zoom 0.8 xoffset -175 yoffset -22
            
        vbox:
        
            box_wrap True
            xalign 0.7
            yalign 0.1
            spacing 10
        
            text "Name: Minnie Rossi":
                color gui.hover_color
                
            text _("Age: 68"):
                color gui.hover_color
                
            text _("Marital Status: Widowed"):
                color gui.hover_color
                
            if minPoints<1:
                text _("Relationship: Acquaintance"):
                    color gui.hover_color
            elif minPoints>0:
                text _("Relationship: Girlfriend"):
                    color gui.hover_color
                
            text _("Occupation: Math Teacher and Restaurant Manager"):
                color gui.hover_color
                
            # text _("Pregnant: [minniePreg]"):
                # color gui.hover_color
                
            text _("Likes: Discipline, Boldness, Intelligence"):
                color gui.hover_color
                
            text _("Dislikes: Drunk Drivers, Laziness, Ignorance"):
                color gui.hover_color
                
screen relMila():
    tag menu
    add "ui/bg.jpg"
    
    use game_menu("Relationships"):
    
        add "ui/relMenu/relMila.png" zoom 0.8 xoffset -175 yoffset -22
            
        vbox:
        
            box_wrap True
            xalign 0.6
            yalign 0.1
            spacing 10
        
            text "Name: Mila":
                color gui.hover_color
                
            text _("Age: 18"):
                color gui.hover_color
                
            text _("Marital Status: Single"):
                color gui.hover_color
                
            if milaPoints<1:
                text _("Relationship: Acquaintance"):
                    color gui.hover_color
            elif milaPoints>0:
                text _("Relationship: Pet"):
                    color gui.hover_color
                
            text _("Occupation: Delivery Girl and Barista"):
                color gui.hover_color
                
            # text _("Pregnant: [milaPreg]"):
                # color gui.hover_color
                
            text _("Likes: Working, Headpats, Being Controlled"):
                color gui.hover_color
                
            text _("Dislikes: Drunk Drivers, Being in Charge"):
                color gui.hover_color
                
screen relSvetlana():
    tag menu
    add "ui/bg.jpg"
    
    use game_menu("Relationships"):
    
        add "ui/relMenu/relSvetlana.png" zoom 0.8 xoffset -175 yoffset -22
            
        vbox:
        
            box_wrap True
            xalign 0.9
            yalign 0.1
            spacing 10
        
            text "Name: Svetlana Rostova":
                color gui.hover_color
                
            text _("Age: 42"):
                color gui.hover_color
                
            text _("Marital Status: Married"):
                color gui.hover_color
                
            if svtPoints<1:
                text _("Relationship: Acquaintance"):
                    color gui.hover_color
            elif svtPoints>0:
                text _("Relationship: Growing Closer"):
                    color gui.hover_color
                
            text _("Occupation: Dance Instructor and Gymnastics Teacher"):
                color gui.hover_color
                
            # text _("Pregnant: [svetlanaPreg]"):
                # color gui.hover_color
                
            text _("Likes: Gymnastics, Dancing, Confidence"):
                color gui.hover_color
                
            text _("Dislikes: Polly's Dad, Cheese, Politics"):
                color gui.hover_color
                
screen relIsabella():
    tag menu
    add "ui/bg.jpg"
    
    use game_menu("Relationships"):
    
        add "ui/relMenu/relIsabella.png" zoom 0.8 xoffset -175 yoffset -22
            
        vbox:
        
            box_wrap True
            xalign 0.7
            yalign 0.1
            spacing 10
        
            text "Name: Isabella":
                color gui.hover_color
                
            text _("Age: 19"):
                color gui.hover_color
                
            text _("Marital Status: Single"):
                color gui.hover_color
                
            if isaPoints<1:
                text _("Relationship: Acquaintance"):
                    color gui.hover_color
            elif isaPoints>0:
                text _("Relationship: Sister-Girlfriend"):
                    color gui.hover_color
                
            text _("Occupation: Unemployed"):
                color gui.hover_color
                
            # text _("Pregnant: [isabellaPreg]"):
                # color gui.hover_color
                
            text _("Likes: You, Gymnastics, Video Games, Anal Porn"):
                color gui.hover_color
                
            text _("Dislikes: Spiders, Spiders and Spiders"):
                color gui.hover_color
                
screen relZelda():
    tag menu
    add "ui/bg.jpg"
    
    use game_menu("Relationships"):
    
        add "ui/relMenu/relZelda.png" zoom 0.8 xoffset -175 yoffset -22
            
        vbox:
        
            box_wrap True
            xalign 0.6
            yalign 0.1
            spacing 10
        
            text "Name: Zelda":
                color gui.hover_color
                
            text _("Age: 18"):
                color gui.hover_color
                
            text _("Marital Status: Single"):
                color gui.hover_color
                
            if zelPoints<1:
                text _("Relationship: Acquaintance"):
                    color gui.hover_color
            elif zelPoints>0:
                text _("Relationship: Girlfriend"):
                    color gui.hover_color
                
            text _("Occupation: Cashier"):
                color gui.hover_color
                
            # text _("Pregnant: [zeldaPreg]"):
                # color gui.hover_color
                
            text _("Likes: Cosplay, Video Games, Hentai, JAVNs"):
                color gui.hover_color
                
            text _("Dislikes: Bullies, Snakes, Fetch Quests"):
                color gui.hover_color
                
screen relBetty():
    tag menu
    add "ui/bg.jpg"
    
    use game_menu("Relationships"):
    
        add "ui/relMenu/relBetty.png" zoom 0.8 xoffset -175 yoffset -22
            
        vbox:
        
            box_wrap True
            xalign 0.7
            yalign 0.1
            spacing 10
        
            text "Name: Betty":
                color gui.hover_color
                
            text _("Age: 25"):
                color gui.hover_color
                
            text _("Marital Status: Single"):
                color gui.hover_color
                
            if btyPoints<1:
                text _("Relationship: Acquaintance"):
                    color gui.hover_color
            elif btyPoints>0:
                text _("Relationship: Dating"):
                    color gui.hover_color
                
            text _("Occupation: Clothing Shop Owner"):
                color gui.hover_color
                
            # text _("Pregnant: [bettyPreg]"):
                # color gui.hover_color
                
            text _("Likes: You, Fashion, Seafood"):
                color gui.hover_color
                
            text _("Dislikes: Bad Hygiene, Wasps, Wearing Hats"):
                color gui.hover_color
                
screen relMaria():
    tag menu
    add "ui/bg.jpg"
    
    use game_menu("Relationships"):
    
        add "ui/relMenu/relMaria.png" zoom 0.8 xoffset -175 yoffset -22
            
        vbox:
        
            box_wrap True
            xalign 0.7
            yalign 0.1
            spacing 10
        
            text "Name: Maria":
                color gui.hover_color
                
            text _("Age: 26"):
                color gui.hover_color
                
            text _("Marital Status: Married to the Lord"):
                color gui.hover_color
                
            if smarPoints<1:
                text _("Relationship: Acquaintance"):
                    color gui.hover_color
            elif smarPoints>0:
                text _("Relationship: Confused"):
                    color gui.hover_color
                
            text _("Occupation: Nun"):
                color gui.hover_color
                
            # text _("Pregnant: [mariaPreg]"):
                # color gui.hover_color
                
            text _("Likes: You, Jesus, The Beach, Charitable Work"):
                color gui.hover_color
                
            text _("Dislikes: Blasphemers, Cruelty, Driving"):
                color gui.hover_color
                
screen relJosianne():
    tag menu
    add "ui/bg.jpg"
    
    use game_menu("Relationships"):
    
        add "ui/relMenu/relJosianne.png" zoom 0.8 xoffset -175 yoffset -22
            
        vbox:
        
            box_wrap True
            xalign 0.9
            yalign 0.1
            spacing 10
        
            text _("Name: Josianne"):
                color gui.hover_color
                
            text _("Age: 32"):
                color gui.hover_color
                
            text _("Marital Status: Married"):
                color gui.hover_color
                
            if josPoints<1:
                text _("Relationship: Acquaintance"):
                    color gui.hover_color
            elif josPoints>0:
                text _("Relationship: Girlfriend"):
                    color gui.hover_color
                
            text _("Occupation: Waitress"):
                color gui.hover_color
                
            # text _("Pregnant: [josiannePreg]"):
                # color gui.hover_color
                
            text _("Likes: You, Her Job, France"):
                color gui.hover_color
                
            text _("Dislikes: Her Marital Situation, Being Shared, Vegetarians"):
                color gui.hover_color
                
# screen relLily():
    # tag menu
    # add "ui/bg.jpg"
    
    # use game_menu("Relationships"):
    
        # add "ui/relMenu/relLily.png" zoom 0.8 xoffset -175 yoffset -22
            
        # vbox:
        
            # box_wrap True
            # xalign 0.6
            # yalign 0.1
            # spacing 10
        
            # text "Name: Lily":
                # color gui.hover_color
                
            # text _("Age: 26"):
                # color gui.hover_color
                
            # text _("Status: Single"):
                # color gui.hover_color
                
            # if lilPoints<1:
                # text _("Relationship: None"):
                    # color gui.hover_color
            # elif lilPoints>0:
                # text _("Relationship: Casual"):
                    # color gui.hover_color
                
            # text _("Occupation: Lawyer"):
                # color gui.hover_color
                
            # text _("Pregnant: [lilyPreg]"):
                # color gui.hover_color
                
            # text _("Likes: You, Her Job, Drinking Lemonade"):
                # color gui.hover_color
                
            # text _("Dislikes: Larry, Corruption, Flying"):
                # color gui.hover_color
                
screen relLily():
    tag menu
    add "ui/bg.jpg"
    
    use game_menu("Relationships"):
    
        add "ui/relMenu/relLily.png" zoom 0.8 xoffset -175 yoffset -22
            
        vbox:
        
            box_wrap True
            xalign 0.6
            yalign 0.1
            spacing 10
        
            text "Name: Lily":
                color gui.hover_color
                
            text _("Age: 26"):
                color gui.hover_color
                
            text _("Marital Status: Single"):
                color gui.hover_color
                
            if lilPoints<1:
                text _("Relationship: None"):
                    color gui.hover_color
            elif lilPoints>0:
                text _("Relationship: Casual"):
                    color gui.hover_color
                
            text _("Occupation: Lawyer"):
                color gui.hover_color
                
            # text _("Pregnant: [lilyPreg]"):
                # color gui.hover_color
                
            text _("Likes: You, Her Job, Drinking Lemonade"):
                color gui.hover_color
                
            text _("Dislikes: Larry, Corruption, Flying"):
                color gui.hover_color
                
screen relKaren():
    tag menu
    add "ui/bg.jpg"
    
    use game_menu("Relationships"):
    
        add "ui/relMenu/relKaren.png" zoom 0.8 xoffset -200 yoffset -22
            
        vbox:
        
            box_wrap True
            xalign 0.95
            yalign 0.1
            spacing 10
        
            text "Name: Karen":
                color gui.hover_color
                
            text _("Age: 34"):
                color gui.hover_color
                
            text _("Marital Status: Married"):
                color gui.hover_color
                
            if krnPoints<1:
                text _("Relationship: None"):
                    color gui.hover_color
            elif krnPoints>0:
                text _("Relationship: Sub"):
                    color gui.hover_color
                
            text _("Occupation: [mc]'s Cocksleeve"):
                color gui.hover_color
                
            # text _("Pregnant: [karenPreg]"):
                # color gui.hover_color
                
            text _("Likes: Yelling at People, Calling the Manager, Being Dominated"):
                color gui.hover_color
                
            text _("Dislikes: Everything Else"):
                color gui.hover_color
                
screen relAiko():
    tag menu
    add "ui/bg.jpg"
    
    use game_menu("Relationships"):
    
        add "ui/relMenu/relAiko.png" zoom 0.8 xoffset -175 yoffset -22
            
        vbox:
        
            box_wrap True
            xalign 0.5
            yalign 0.1
            spacing 10
        
            text "Name: Aiko":
                color gui.hover_color
                
            text _("Age: 23"):
                color gui.hover_color
                
            text _("Marital Status: Single"):
                color gui.hover_color
                
            if massPoints<1:
                text _("Relationship: None"):
                    color gui.hover_color
            elif massPoints>0:
                text _("Relationship: Casual"):
                    color gui.hover_color
                
            text _("Occupation: Masseuse"):
                color gui.hover_color
                
            # text _("Pregnant: [aikoPreg]"):
                # color gui.hover_color
                
            text _("Likes: You, Porn, Pineapple Pizza"):
                color gui.hover_color
                
            text _("Dislikes: Her Job, Rats, Feet"):
                color gui.hover_color
                
screen relShawna():
    tag menu
    add "ui/bg.jpg"
    
    use game_menu("Relationships"):
    
        add "ui/relMenu/relShawna.png" zoom 0.8 xoffset -175 yoffset -22
            
        vbox:
        
            box_wrap True
            xalign 0.4
            yalign 0.1
            spacing 10
        
            text "Name: Shawna":
                color gui.hover_color
                
            text _("Age: 24"):
                color gui.hover_color
                
            text _("Marital Status: Single"):
                color gui.hover_color
                
            if shwPoints<1:
                text _("Relationship: None"):
                    color gui.hover_color
            elif shwPoints>0:
                text _("Relationship: Complicated"):
                    color gui.hover_color
                
            text _("Occupation: Unknown"):
                color gui.hover_color
                
            text _("Pregnant: [shawnaPreg]"):
                color gui.hover_color
                
            # text _("Likes: Music"):
                # color gui.hover_color
                
            text _("Dislikes: Unknown"):
                color gui.hover_color
                
screen relYvonne():
    tag menu
    add "ui/bg.jpg"
    
    use game_menu("Relationships"):
    
        add "ui/relMenu/relYvonne.png" zoom 0.8 xoffset -175 yoffset -22
            
        vbox:
        
            box_wrap True
            xalign 0.4
            yalign 0.1
            spacing 10
        
            text "Name: Yvonne":
                color gui.hover_color
                
            text _("Age: 42"):
                color gui.hover_color
                
            text _("Marital Status: Married"):
                color gui.hover_color
                
            if yvPoints<1:
                text _("Relationship: None"):
                    color gui.hover_color
            elif yvPoints>0:
                text _("Relationship: None"):
                    color gui.hover_color
                
            text _("Occupation: Mayor"):
                color gui.hover_color
                
            # text _("Pregnant: [yvonnePreg]"):
                # color gui.hover_color
                
            text _("Likes: Unknown"):
                color gui.hover_color
                
            text _("Dislikes: Unknown"):
                color gui.hover_color
                
screen relLina():
    tag menu
    add "ui/bg.jpg"
    
    use game_menu("Relationships"):
    
        add "ui/relMenu/relLina.png" zoom 0.8 xoffset -175 yoffset -22
            
        vbox:
        
            box_wrap True
            xalign 0.5
            yalign 0.1
            spacing 10
        
            text "Name: Lina":
                color gui.hover_color
                
            text _("Age: 39"):
                color gui.hover_color
                
            text _("Marital Status: Single"):
                color gui.hover_color
                
            if linaPoints<1:
                text _("Relationship: Acquaintance"):
                    color gui.hover_color
            elif linaPoints>0:
                text _("Relationship: Acquaintance"):
                    color gui.hover_color
                
            text _("Occupation: Real Estate Agent"):
                color gui.hover_color
                
            # text _("Pregnant: [linaPreg]"):
                # color gui.hover_color
                
            text _("Likes: You"):
                color gui.hover_color
                
            text _("Dislikes: Unknown"):
                color gui.hover_color
                
screen relElaine():
    tag menu
    add "ui/bg.jpg"
    
    use game_menu("Relationships"):
    
        add "ui/relMenu/relElaine.png" zoom 0.8 xoffset -175 yoffset -22
            
        vbox:
        
            box_wrap True
            xalign 0.5
            yalign 0.1
            spacing 10
        
            text "Name: Elaine":
                color gui.hover_color
                
            text _("Age: 51"):
                color gui.hover_color
                
            text _("Marital Status: Single"):
                color gui.hover_color
                
            if elaPoints<1:
                text _("Relationship: Acquaintance"):
                    color gui.hover_color
            elif elaPoints>0:
                text _("Relationship: Casual"):
                    color gui.hover_color
                
            text _("Occupation: Singer"):
                color gui.hover_color
                
            # text _("Pregnant: [elainePreg]"):
                # color gui.hover_color
                
            text _("Likes: You, Singing, Martial Arts"):
                color gui.hover_color
                
            text _("Dislikes: Unknown"):
                color gui.hover_color
                
screen relPolly():
    tag menu
    add "ui/bg.jpg"
    
    use game_menu("Relationships"):
    
        add "ui/relMenu/relPolly.png" zoom 0.8 xoffset -175 yoffset -22
            
        vbox:
        
            box_wrap True
            xalign 0.5
            yalign 0.1
            spacing 10
        
            text "Name: Polly":
                color gui.hover_color
                
            text _("Age: 18"):
                color gui.hover_color
                
            text _("Marital Status: Single"):
                color gui.hover_color
                
            if plyPoints<1:
                text _("Relationship: Acquaintance"):
                    color gui.hover_color
            elif plyPoints>0:
                text _("Relationship: Daughter-Girlfriend"):
                    color gui.hover_color
                
            text _("Occupation: Unemployed"):
                color gui.hover_color
                
            # text _("Pregnant: [pollyPreg]"):
                # color gui.hover_color
                
            text _("Likes: Music, Reading, Cats"):
                color gui.hover_color
                
            text _("Dislikes: Her Dad, You, Alcoholics"):
                color gui.hover_color