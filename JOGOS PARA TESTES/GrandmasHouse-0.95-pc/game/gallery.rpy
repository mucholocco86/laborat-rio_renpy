label gallery:

    call screen gallery
    
screen gallery():
    tag menu
    add "ui/bg.jpg"
    
    use game_menu("Gallery"):
            
        hbox:
                style_prefix "page"

                xalign 0.5
                yalign 1.0
                yoffset -30

                spacing gui.page_spacing
                

                
                textbutton "1"
                textbutton "2" action Hide("gallery"), Show("gallery2")
                textbutton "3" action Hide("gallery"), Show("gallery3")
                textbutton "4" action Hide("gallery"), Show("gallery4")
                textbutton "5" action Hide("gallery"), Show("gallery5")
                textbutton "6" action Hide("gallery"), Show("gallery6")
                textbutton "7" action Hide("gallery"), Show("gallery7")
                # textbutton "8" action Hide("gallery"), Show("gallery8")

        
        vbox:
            frame:
                yoffset -125
                xoffset -100
            
                if persistent.g_Unlock == 1:
                    textbutton _("Lock Gallery"):
                        text_style "unlockButton"
                        action unlockGallery, Hide("gallery"), Show("gallery")
                        
                else:
                    textbutton _("Unlock Gallery"):
                        text_style "unlockButton"
                        action unlockGallery, Hide("gallery"), Show("gallery")
                        
        
        grid 3 3:
            style_prefix "slot"

            xalign 0.5
            yalign 0.5
            xpos 650
            ypos 360
            
            spacing gui.slot_spacing

                    
            if persistent.day135annabelleSex == 1 or persistent.g_Unlock == 1:
                imagebutton:
                        action Replay("day135annabelleSex", locked=False)
                        idle Transform("images/v82/day135 morn191.webp", zoom=0.2)
                        hover Transform("images/v82/day135 morn191.webp", zoom=0.195)
            else:
                imagebutton:
                    idle Transform("ui/locked.png", zoom=0.2)
                
            if persistent.day135opheliaAnnabelleBJ == 1 or persistent.g_Unlock == 1:
                imagebutton:
                        action Replay("day135opheliaAnnabelleBJ", locked=False)
                        idle Transform("images/v82/day135 morn355.webp", zoom=0.2)
                        hover Transform("images/v82/day135 morn355.webp", zoom=0.195)
            else:
                imagebutton:
                    idle Transform("ui/locked.png", zoom=0.2)
                
            if persistent.day135redheadGangbang == 1 or persistent.g_Unlock == 1:
                imagebutton:
                        action Replay("day135redheadGangbang", locked=False)
                        idle Transform("images/v82/day135 morn465.webp", zoom=0.2)
                        hover Transform("images/v82/day135 morn465.webp", zoom=0.195)
            else:
                imagebutton:
                    idle Transform("ui/locked.png", zoom=0.2)
                
            if persistent.day136jamilaMorningFun == 1 or persistent.g_Unlock == 1:
                imagebutton:
                        action Replay("day136jamilaMorningFun", locked=False)
                        idle Transform("images/v83/day136 morn4.webp", zoom=0.2)
                        hover Transform("images/v83/day136 morn4.webp", zoom=0.195)
            else:
                imagebutton:
                    idle Transform("ui/locked.png", zoom=0.2)
                    
            if persistent.day136asamiTrain == 1 or persistent.g_Unlock == 1:
                imagebutton:
                        action Replay("day136asamiTrain", locked=False)
                        idle Transform("images/v83/day136 morn134.webp", zoom=0.2)
                        hover Transform("images/v83/day136 morn134.webp", zoom=0.195)
            else:
                imagebutton:
                    idle Transform("ui/locked.png", zoom=0.2)
                
            if persistent.day136asamiShaming == 1 or persistent.g_Unlock == 1:
                imagebutton:
                        action Replay("day136asamiShaming", locked=False)
                        idle Transform("images/v83/day136 morn211.webp", zoom=0.2)
                        hover Transform("images/v83/day136 morn211.webp", zoom=0.195)
            else:
                imagebutton:
                    idle Transform("ui/locked.png", zoom=0.2)
                
            if persistent.day136isabellaSex == 1 or persistent.g_Unlock == 1:
                imagebutton:
                        action Replay("day136isabellaSex", locked=False)
                        idle Transform("images/v83/day136 morn293.webp", zoom=0.2)
                        hover Transform("images/v83/day136 morn293.webp", zoom=0.195)
            else:
                imagebutton:
                    idle Transform("ui/locked.png", zoom=0.2)
                
            if persistent.day136leeFinger == 1 or persistent.g_Unlock == 1:
                imagebutton:
                        action Replay("day136leeFinger", locked=False)
                        idle Transform("images/v83/day136 morn496.webp", zoom=0.2)
                        hover Transform("images/v83/day136 morn496.webp", zoom=0.195)
            else:
                imagebutton:
                    idle Transform("ui/locked.png", zoom=0.2)
                
            if persistent.day137sandraSleepCunni == 1 or persistent.g_Unlock == 1:
                imagebutton:
                        action Replay("day137sandraSleepCunni", locked=False)
                        idle Transform("images/v84/day137 morn205.webp", zoom=0.2)
                        hover Transform("images/v84/day137 morn205.webp", zoom=0.195)
            else:
                imagebutton:
                    idle Transform("ui/locked.png", zoom=0.2)
                
            
screen gallery2():
    tag menu
    add "ui/bg.jpg"
    
    use game_menu("Gallery 2"):
            
        
        hbox:
                style_prefix "page"

                xalign 0.5
                yalign 1.0
                yoffset -30

                spacing gui.page_spacing
                

                
                textbutton "1" action Hide("gallery2"), Show("gallery")
                textbutton "2"
                textbutton "3" action Hide("gallery2"), Show("gallery3")
                textbutton "4" action Hide("gallery2"), Show("gallery4")
                textbutton "5" action Hide("gallery2"), Show("gallery5")
                textbutton "6" action Hide("gallery2"), Show("gallery6")
                textbutton "7" action Hide("gallery2"), Show("gallery7")
                # textbutton "8" action Hide("gallery2"), Show("gallery8")

        
        vbox:
            frame:
                yoffset -125
                xoffset -50
            
                if persistent.g_Unlock == 1:
                    textbutton _("Lock Gallery"):
                        text_style "unlockButton"
                        action unlockGallery, Hide("gallery2"), Show("gallery2")
                        
                else:
                    textbutton _("Unlock Gallery"):
                        text_style "unlockButton"
                        action unlockGallery, Hide("gallery2"), Show("gallery2")
                        
        
            
        grid 3 3:
            style_prefix "slot"

            xalign 0.5
            yalign 0.5
            xpos 650
            ypos 360
            
            spacing gui.slot_spacing
                    
                    
            if persistent.day137zeldaPee == 1 or persistent.g_Unlock == 1:
                imagebutton:
                        action Replay("day137zeldaPee", locked=False)
                        idle Transform("images/v84/day137 morn341.webp", zoom=0.2)
                        hover Transform("images/v84/day137 morn341.webp", zoom=0.195)
            else:
                imagebutton:
                    idle Transform("ui/locked.png", zoom=0.2)
                    
            if persistent.day137zeldaTitjob == 1 or persistent.g_Unlock == 1:
                imagebutton:
                        action Replay("day137zeldaTitjob", locked=False)
                        idle Transform("images/v84/day137 morn416.webp", zoom=0.2)
                        hover Transform("images/v84/day137 morn416.webp", zoom=0.195)
            else:
                imagebutton:
                    idle Transform("ui/locked.png", zoom=0.2)
                    
            if persistent.day137jadaSex == 1 or persistent.g_Unlock == 1:
                imagebutton:
                        action Replay("day137jadaSex", locked=False)
                        idle Transform("images/v84/day137 morn592.webp", zoom=0.2)
                        hover Transform("images/v84/day137 morn592.webp", zoom=0.195)
            else:
                imagebutton:
                    idle Transform("ui/locked.png", zoom=0.2)
                    
            if persistent.day138allisonSex == 1 or persistent.g_Unlock == 1:
                imagebutton:
                        action Replay("day138allisonSex", locked=False)
                        idle Transform("images/v85/day138 morn64.webp", zoom=0.2)
                        hover Transform("images/v85/day138 morn64.webp", zoom=0.195)
            else:
                imagebutton:
                    idle Transform("ui/locked.png", zoom=0.2)
                    
            if persistent.day138shizukaDog == 1 or persistent.g_Unlock == 1:
                imagebutton:
                        action Replay("day138shizukaDog", locked=False)
                        idle Transform("images/v85/day138 morn227.webp", zoom=0.2)
                        hover Transform("images/v85/day138 morn227.webp", zoom=0.195)
            else:
                imagebutton:
                    idle Transform("ui/locked.png", zoom=0.2)
                    
            if persistent.day138milaSex == 1 or persistent.g_Unlock == 1:
                imagebutton:
                        action Replay("day138milaSex", locked=False)
                        idle Transform("images/v85/day138 morn294.webp", zoom=0.2)
                        hover Transform("images/v85/day138 morn294.webp", zoom=0.195)
            else:
                imagebutton:
                    idle Transform("ui/locked.png", zoom=0.2)
                    
            if persistent.day138priyaCuck == 1 or persistent.g_Unlock == 1:
                imagebutton:
                        action Replay("day138priyaCuck", locked=False)
                        idle Transform("images/v85/day138 morn436.webp", zoom=0.2)
                        hover Transform("images/v85/day138 morn436.webp", zoom=0.195)
            else:
                imagebutton:
                    idle Transform("ui/locked.png", zoom=0.2)
                        
            if persistent.day139katieBrandiSex == 1 or persistent.g_Unlock == 1:
                imagebutton:
                        action Replay("day139katieBrandiSex", locked=False)
                        idle Transform("images/v86/day139 morn171.webp", zoom=0.2)
                        hover Transform("images/v86/day139 morn171.webp", zoom=0.195)
            else:
                imagebutton:
                    idle Transform("ui/locked.png", zoom=0.2)
                
            if persistent.day139nurseSex == 1 or persistent.g_Unlock == 1:
                imagebutton:
                        action Replay("day139nurseSex", locked=False)
                        idle Transform("images/v86/day139 morn350.webp", zoom=0.2)
                        hover Transform("images/v86/day139 morn350.webp", zoom=0.195)
            else:
                imagebutton:
                    idle Transform("ui/locked.png", zoom=0.2)


screen gallery3():
    tag menu
    add "ui/bg.jpg"
    
    use game_menu("Gallery 3"):
            
        
        hbox:
                style_prefix "page"

                xalign 0.5
                yalign 1.0
                yoffset -30

                spacing gui.page_spacing
                

                
                textbutton "1" action Hide("gallery3"), Show("gallery")
                textbutton "2" action Hide("gallery3"), Show("gallery2")
                textbutton "3" 
                textbutton "4" action Hide("gallery3"), Show("gallery4")
                textbutton "5" action Hide("gallery3"), Show("gallery5")
                textbutton "6" action Hide("gallery3"), Show("gallery6")
                textbutton "7" action Hide("gallery3"), Show("gallery7")
                # textbutton "8" action Hide("gallery3"), Show("gallery8")

        
        vbox:
            frame:
                yoffset -125
                xoffset -50
            
                if persistent.g_Unlock == 1:
                    textbutton _("Lock Gallery"):
                        text_style "unlockButton"
                        action unlockGallery, Hide("gallery3"), Show("gallery3")
                        
                else:
                    textbutton _("Unlock Gallery"):
                        text_style "unlockButton"
                        action unlockGallery, Hide("gallery3"), Show("gallery3")
                        
            
        grid 3 3:
            style_prefix "slot"

            xalign 0.5
            yalign 0.5
            xpos 650
            ypos 360
            
            spacing gui.slot_spacing
                    
            if persistent.day139minnieAnal == 1 or persistent.g_Unlock == 1:
                imagebutton:
                        action Replay("day139minnieAnal", locked=False)
                        idle Transform("images/v86/day139 morn508.webp", zoom=0.2)
                        hover Transform("images/v86/day139 morn508.webp", zoom=0.195)
            else:
                imagebutton:
                    idle Transform("ui/locked.png", zoom=0.2)
            
            if persistent.day139lizAmyHands == 1 or persistent.g_Unlock == 1:
                imagebutton:
                        action Replay("day139lizAmyHands", locked=False)
                        idle Transform("images/v86/day139 morn623.webp", zoom=0.2)
                        hover Transform("images/v86/day139 morn623.webp", zoom=0.195)
            else:
                imagebutton:
                    idle Transform("ui/locked.png", zoom=0.2)
                        
            if persistent.day140taxiGangbang == 1 or persistent.g_Unlock == 1:
                imagebutton:
                        action Replay("day140taxiGangbang", locked=False)
                        idle Transform("images/v87/day140 morn170.webp", zoom=0.2)
                        hover Transform("images/v87/day140 morn170.webp", zoom=0.195)
            else:
                imagebutton:
                    idle Transform("ui/locked.png", zoom=0.2)
            
            if persistent.day140amyLapdance == 1 or persistent.g_Unlock == 1:
                imagebutton:
                        action Replay("day140amyLapdance", locked=False)
                        idle Transform("images/v87/day140 morn398.webp", zoom=0.2)
                        hover Transform("images/v87/day140 morn398.webp", zoom=0.195)
            else:
                imagebutton:
                    idle Transform("ui/locked.png", zoom=0.2)
                
            if persistent.day140bettyAnal == 1 or persistent.g_Unlock == 1:
                imagebutton:
                        action Replay("day140bettyAnal", locked=False)
                        idle Transform("images/v87/day140 morn522.webp", zoom=0.2)
                        hover Transform("images/v87/day140 morn522.webp", zoom=0.195)
            else:
                imagebutton:
                    idle Transform("ui/locked.png", zoom=0.2)
            
            if persistent.day141matildaSex == 1 or persistent.g_Unlock == 1:
                imagebutton:
                        action Replay("day141matildaSex", locked=False)
                        idle Transform("images/v88/day141 morn22.webp", zoom=0.2)
                        hover Transform("images/v88/day141 morn22.webp", zoom=0.195)
            else:
                imagebutton:
                    idle Transform("ui/locked.png", zoom=0.2)
                
            if persistent.day141allisonBlowjob == 1 or persistent.g_Unlock == 1:
                imagebutton:
                        action Replay("day141allisonBlowjob", locked=False)
                        idle Transform("images/v88/day141 morn383.webp", zoom=0.2)
                        hover Transform("images/v88/day141 morn383.webp", zoom=0.195)
            else:
                imagebutton:
                    idle Transform("ui/locked.png", zoom=0.2)
                        
            if persistent.day141lilySex == 1 or persistent.g_Unlock == 1:
                imagebutton:
                        action Replay("day141lilySex", locked=False)
                        idle Transform("images/v88/day141 morn455.webp", zoom=0.2)
                        hover Transform("images/v88/day141 morn455.webp", zoom=0.195)
            else:
                imagebutton:
                    idle Transform("ui/locked.png", zoom=0.2)
                
            if persistent.day142lizPlaneSex == 1 or persistent.g_Unlock == 1:
                imagebutton:
                        action Replay("day142lizPlaneSex", locked=False)
                        idle Transform("images/v89/day142 morn25.webp", zoom=0.2)
                        hover Transform("images/v89/day142 morn25.webp", zoom=0.195)
            else:
                imagebutton:
                    idle Transform("ui/locked.png", zoom=0.2)
            

screen gallery4():
    tag menu
    add "ui/bg.jpg"
    
    use game_menu("Gallery 4"):
            
        
        hbox:
                style_prefix "page"

                xalign 0.5
                yalign 1.0
                yoffset -30

                spacing gui.page_spacing
                

                
                textbutton "1" action Hide("gallery4"), Show("gallery")
                textbutton "2" action Hide("gallery4"), Show("gallery2")
                textbutton "3" action Hide("gallery4"), Show("gallery3")
                textbutton "4"
                textbutton "5" action Hide("gallery4"), Show("gallery5")
                textbutton "6" action Hide("gallery4"), Show("gallery6")
                textbutton "7" action Hide("gallery4"), Show("gallery7")
                # textbutton "8" action Hide("gallery4"), Show("gallery8")

        
        vbox:
            frame:
                yoffset -125
                xoffset -50
            
                if persistent.g_Unlock == 1:
                    textbutton _("Lock Gallery"):
                        text_style "unlockButton"
                        action unlockGallery, Hide("gallery4"), Show("gallery4")
                        
                else:
                    textbutton _("Unlock Gallery"):
                        text_style "unlockButton"
                        action unlockGallery, Hide("gallery4"), Show("gallery4")
                        
        
            
        grid 3 3:
            style_prefix "slot"

            xalign 0.5
            yalign 0.5
            xpos 650
            ypos 360
            
            spacing gui.slot_spacing
            
            if persistent.day142elaineRimjob == 1 or persistent.g_Unlock == 1:
                imagebutton:
                        action Replay("day142elaineRimjob", locked=False)
                        idle Transform("images/v89/day142 morn201.webp", zoom=0.2)
                        hover Transform("images/v89/day142 morn201.webp", zoom=0.195)
            else:
                imagebutton:
                    idle Transform("ui/locked.png", zoom=0.2)
            
            if persistent.day142elaineSex == 1 or persistent.g_Unlock == 1:
                imagebutton:
                        action Replay("day142elaineSex", locked=False)
                        idle Transform("images/v89/day142 morn267.webp", zoom=0.2)
                        hover Transform("images/v89/day142 morn267.webp", zoom=0.195)
            else:
                imagebutton:
                    idle Transform("ui/locked.png", zoom=0.2)
            
            if persistent.day142lizAmyBlowjob == 1 or persistent.g_Unlock == 1:
                imagebutton:
                        action Replay("day142lizAmyBlowjob", locked=False)
                        idle Transform("images/v89/day142 morn652.webp", zoom=0.2)
                        hover Transform("images/v89/day142 morn652.webp", zoom=0.195)
            else:
                imagebutton:
                    idle Transform("ui/locked.png", zoom=0.2)
            
            if persistent.day143amyFinger == 1 or persistent.g_Unlock == 1:
                imagebutton:
                        action Replay("day143amyFinger", locked=False)
                        idle Transform("images/v90/day143 morn6.webp", zoom=0.2)
                        hover Transform("images/v90/day143 morn6.webp", zoom=0.195)
            else:
                imagebutton:
                    idle Transform("ui/locked.png", zoom=0.2)
            
            if persistent.day143elaineAnal == 1 or persistent.g_Unlock == 1:
                imagebutton:
                        action Replay("day143elaineAnal", locked=False)
                        idle Transform("images/v90/day143 morn58.webp", zoom=0.2)
                        hover Transform("images/v90/day143 morn58.webp", zoom=0.195)
            else:
                imagebutton:
                    idle Transform("ui/locked.png", zoom=0.2)
                        
            if persistent.day143amyCunni == 1 or persistent.g_Unlock == 1:
                imagebutton:
                        action Replay("day143amyCunni", locked=False)
                        idle Transform("images/v90/day143 morn309.webp", zoom=0.2)
                        hover Transform("images/v90/day143 morn309.webp", zoom=0.195)
            else:
                imagebutton:
                    idle Transform("ui/locked.png", zoom=0.2)
            
            if persistent.day143amyThighjob == 1 or persistent.g_Unlock == 1:
                imagebutton:
                        action Replay("day143amyThighjob", locked=False)
                        idle Transform("images/v90/day143 morn693.webp", zoom=0.2)
                        hover Transform("images/v90/day143 morn693.webp", zoom=0.195)
            else:
                imagebutton:
                    idle Transform("ui/locked.png", zoom=0.2)
            
            if persistent.day144elaineTitjob == 1 or persistent.g_Unlock == 1:
                imagebutton:
                        action Replay("day144elaineTitjob", locked=False)
                        idle Transform("images/v91/day144 morn196.webp", zoom=0.2)
                        hover Transform("images/v91/day144 morn196.webp", zoom=0.195)
            else:
                imagebutton:
                    idle Transform("ui/locked.png", zoom=0.2)
                        
            if persistent.day144amySex == 1 or persistent.g_Unlock == 1:
                imagebutton:
                        action Replay("day144amySex", locked=False)
                        idle Transform("images/v91/day144 morn398.webp", zoom=0.2)
                        hover Transform("images/v91/day144 morn398.webp", zoom=0.195)
            else:
                imagebutton:
                    idle Transform("ui/locked.png", zoom=0.2)
                
            
screen gallery5():
    tag menu
    add "ui/bg.jpg"
    
    use game_menu("Gallery 5"):
            
        
        hbox:
                style_prefix "page"

                xalign 0.5
                yalign 1.0
                yoffset -30

                spacing gui.page_spacing
                

                
                textbutton "1" action Hide("gallery5"), Show("gallery")
                textbutton "2" action Hide("gallery5"), Show("gallery2")
                textbutton "3" action Hide("gallery5"), Show("gallery3")
                textbutton "4" action Hide("gallery5"), Show("gallery4")
                textbutton "5"
                textbutton "6" action Hide("gallery5"), Show("gallery6")
                textbutton "7" action Hide("gallery5"), Show("gallery7")
                # textbutton "8" action Hide("gallery5"), Show("gallery8")

        
        vbox:
            frame:
                yoffset -125
                xoffset -50
            
                if persistent.g_Unlock == 1:
                    textbutton _("Lock Gallery"):
                        text_style "unlockButton"
                        action unlockGallery, Hide("gallery5"), Show("gallery5")
                        
                else:
                    textbutton _("Unlock Gallery"):
                        text_style "unlockButton"
                        action unlockGallery, Hide("gallery5"), Show("gallery5")
                        
        
            
        grid 3 3:
            style_prefix "slot"

            xalign 0.5
            yalign 0.5
            xpos 650
            ypos 360
            
            spacing gui.slot_spacing
            
            if persistent.day145amyNTRliz == 1 or persistent.g_Unlock == 1:
                imagebutton:
                        action Replay("day145amyNTRliz", locked=False)
                        idle Transform("images/v92/day145 morn33.webp", zoom=0.2)
                        hover Transform("images/v92/day145 morn33.webp", zoom=0.195)
            else:
                imagebutton:
                    idle Transform("ui/locked.png", zoom=0.2)
            
            if persistent.day145amyRimjob == 1 or persistent.g_Unlock == 1:
                imagebutton:
                        action Replay("day145amyRimjob", locked=False)
                        idle Transform("images/v92/day145 morn253.webp", zoom=0.2)
                        hover Transform("images/v92/day145 morn253.webp", zoom=0.195)
            else:
                imagebutton:
                    idle Transform("ui/locked.png", zoom=0.2)
            
            if persistent.day145deanSpank == 1 or persistent.g_Unlock == 1:
                imagebutton:
                        action Replay("day145deanSpank", locked=False)
                        idle Transform("images/v92/day145 morn625.webp", zoom=0.2)
                        hover Transform("images/v92/day145 morn625.webp", zoom=0.195)
            else:
                imagebutton:
                    idle Transform("ui/locked.png", zoom=0.2)
            
            if persistent.day145lizBJ == 1 or persistent.g_Unlock == 1:
                imagebutton:
                        action Replay("day145lizBJ", locked=False)
                        idle Transform("images/v92/day145 morn662.webp", zoom=0.2)
                        hover Transform("images/v92/day145 morn662.webp", zoom=0.195)
            else:
                imagebutton:
                    idle Transform("ui/locked.png", zoom=0.2)
                        
            if persistent.day146deanSex == 1 or persistent.g_Unlock == 1:
                imagebutton:
                        action Replay("day146deanSex", locked=False)
                        idle Transform("images/v93/day146 morn2.webp", zoom=0.2)
                        hover Transform("images/v93/day146 morn2.webp", zoom=0.195)
            else:
                imagebutton:
                    idle Transform("ui/locked.png", zoom=0.2)
            
            if persistent.day146allisonSex == 1 or persistent.g_Unlock == 1:
                imagebutton:
                        action Replay("day146allisonSex", locked=False)
                        idle Transform("images/v93/day146 morn226.webp", zoom=0.2)
                        hover Transform("images/v93/day146 morn226.webp", zoom=0.195)
            else:
                imagebutton:
                    idle Transform("ui/locked.png", zoom=0.2)
                        
            if persistent.day146jamilaSex == 1 or persistent.g_Unlock == 1:
                imagebutton:
                        action Replay("day146jamilaSex", locked=False)
                        idle Transform("images/v93/day146 morn266.webp", zoom=0.2)
                        hover Transform("images/v93/day146 morn266.webp", zoom=0.195)
            else:
                imagebutton:
                    idle Transform("ui/locked.png", zoom=0.2)
            
            if persistent.day146shizukaSex == 1 or persistent.g_Unlock == 1:
                imagebutton:
                        action Replay("day146shizukaSex", locked=False)
                        idle Transform("images/v93/day146 morn345.webp", zoom=0.2)
                        hover Transform("images/v93/day146 morn345.webp", zoom=0.195)
            else:
                imagebutton:
                    idle Transform("ui/locked.png", zoom=0.2)
                        
            if persistent.day146asamiCatThreesome == 1 or persistent.g_Unlock == 1:
                imagebutton:
                        action Replay("day146asamiCatThreesome", locked=False)
                        idle Transform("images/v93/day146 morn409.webp", zoom=0.2)
                        hover Transform("images/v93/day146 morn409.webp", zoom=0.195)
            else:
                imagebutton:
                    idle Transform("ui/locked.png", zoom=0.2)
            

screen gallery6():
    tag menu
    add "ui/bg.jpg"
    
    use game_menu("Gallery 6"):
            
        
        hbox:
                style_prefix "page"

                xalign 0.5
                yalign 1.0
                yoffset -30

                spacing gui.page_spacing
                

                
                textbutton "1" action Hide("gallery6"), Show("gallery")
                textbutton "2" action Hide("gallery6"), Show("gallery2")
                textbutton "3" action Hide("gallery6"), Show("gallery3")
                textbutton "4" action Hide("gallery6"), Show("gallery4")
                textbutton "5" action Hide("gallery6"), Show("gallery5")
                textbutton "6"
                textbutton "7" action Hide("gallery6"), Show("gallery7")
                # textbutton "8" action Hide("gallery6"), Show("gallery8")

        
        vbox:
            frame:
                yoffset -125
                xoffset -50
            
                if persistent.g_Unlock == 1:
                    textbutton _("Lock Gallery"):
                        text_style "unlockButton"
                        action unlockGallery, Hide("gallery6"), Show("gallery6")
                        
                else:
                    textbutton _("Unlock Gallery"):
                        text_style "unlockButton"
                        action unlockGallery, Hide("gallery6"), Show("gallery6")
                        
        
        grid 3 3:
            style_prefix "slot"

            xalign 0.5
            yalign 0.5
            xpos 650
            ypos 360
            
            spacing gui.slot_spacing
            
            if persistent.day147amyShowerSex == 1 or persistent.g_Unlock == 1:
                imagebutton:
                        action Replay("day147amyShowerSex", locked=False)
                        idle Transform("images/v94/day147 morn55.webp", zoom=0.2)
                        hover Transform("images/v94/day147 morn55.webp", zoom=0.195)
            else:
                imagebutton:
                    idle Transform("ui/locked.png", zoom=0.2)
            
            if persistent.day147mariaSex == 1 or persistent.g_Unlock == 1:
                imagebutton:
                        action Replay("day147mariaSex", locked=False)
                        idle Transform("images/v94/day147 morn192.webp", zoom=0.2)
                        hover Transform("images/v94/day147 morn192.webp", zoom=0.195)
            else:
                imagebutton:
                    idle Transform("ui/locked.png", zoom=0.2)
            
            if persistent.day148helgaHandjob == 1 or persistent.g_Unlock == 1:
                imagebutton:
                        action Replay("day148helgaHandjob", locked=False)
                        idle Transform("images/v94/day147 morn451.webp", zoom=0.2)
                        hover Transform("images/v94/day147 morn451.webp", zoom=0.195)
            else:
                imagebutton:
                    idle Transform("ui/locked.png", zoom=0.2)
            
            if persistent.day147helgaAssFingered == 1 or persistent.g_Unlock == 1:
                imagebutton:
                        action Replay("day147helgaAssFingered", locked=False)
                        idle Transform("images/v94/day147 morn538.webp", zoom=0.2)
                        hover Transform("images/v94/day147 morn538.webp", zoom=0.195)
            else:
                imagebutton:
                    idle Transform("ui/locked.png", zoom=0.2)
            
            if persistent.day148helgaAnal == 1 or persistent.g_Unlock == 1:
                imagebutton:
                        action Replay("day148helgaAnal", locked=False)
                        idle Transform("images/v95/day148 morn1.webp", zoom=0.2)
                        hover Transform("images/v95/day148 morn1.webp", zoom=0.195)
            else:
                imagebutton:
                    idle Transform("ui/locked.png", zoom=0.2)
            
            if persistent.day148jamilaHelgaBreastfeed == 1 or persistent.g_Unlock == 1:
                imagebutton:
                        action Replay("day148jamilaHelgaBreastfeed", locked=False)
                        idle Transform("images/v95/day148 morn95.webp", zoom=0.2)
                        hover Transform("images/v95/day148 morn95.webp", zoom=0.195)
            else:
                imagebutton:
                    idle Transform("ui/locked.png", zoom=0.2)
            
            if persistent.day148anabelleSex == 1 or persistent.g_Unlock == 1:
                imagebutton:
                        action Replay("day148anabelleSex", locked=False)
                        idle Transform("images/v95/day148 morn169.webp", zoom=0.2)
                        hover Transform("images/v95/day148 morn169.webp", zoom=0.195)
            else:
                imagebutton:
                    idle Transform("ui/locked.png", zoom=0.2)
            
            if persistent.day148opheliaBJ == 1 or persistent.g_Unlock == 1:
                imagebutton:
                        action Replay("day148opheliaBJ", locked=False)
                        idle Transform("images/v95/day148 morn254.webp", zoom=0.2)
                        hover Transform("images/v95/day148 morn254.webp", zoom=0.195)
            else:
                imagebutton:
                    idle Transform("ui/locked.png", zoom=0.2)
            
            if persistent.day148imogeneCunni == 1 or persistent.g_Unlock == 1:
                imagebutton:
                        action Replay("day148imogeneCunni", locked=False)
                        idle Transform("images/v95/day148 morn339.webp", zoom=0.2)
                        hover Transform("images/v95/day148 morn339.webp", zoom=0.195)
            else:
                imagebutton:
                    idle Transform("ui/locked.png", zoom=0.2)
            
            
screen gallery7():
    tag menu
    add "ui/bg.jpg"
    
    use game_menu("Gallery 7"):
            
        
        hbox:
                style_prefix "page"

                xalign 0.5
                yalign 1.0
                yoffset -30

                spacing gui.page_spacing
                

                
                textbutton "1" action Hide("gallery7"), Show("gallery")
                textbutton "2" action Hide("gallery7"), Show("gallery2")
                textbutton "3" action Hide("gallery7"), Show("gallery3")
                textbutton "4" action Hide("gallery7"), Show("gallery4")
                textbutton "5" action Hide("gallery7"), Show("gallery5")
                textbutton "6" action Hide("gallery7"), Show("gallery6")
                textbutton "7"
                # textbutton "8" action Hide("gallery7"), Show("gallery8")

        
        vbox:
            frame:
                yoffset -125
                xoffset -50
            
                if persistent.g_Unlock == 1:
                    textbutton _("Lock Gallery"):
                        text_style "unlockButton"
                        action unlockGallery, Hide("gallery7"), Show("gallery7")
                        
                else:
                    textbutton _("Unlock Gallery"):
                        text_style "unlockButton"
                        action unlockGallery, Hide("gallery7"), Show("gallery7")
                        
        
        grid 3 3:
            style_prefix "slot"

            xalign 0.5
            yalign 0.5
            xpos 650
            ypos 360
            
            spacing gui.slot_spacing
            
            if persistent.day148debbiePeeDrink == 1 or persistent.g_Unlock == 1:
                imagebutton:
                        action Replay("day148debbiePeeDrink", locked=False)
                        idle Transform("images/v95/day148 morn425.webp", zoom=0.2)
                        hover Transform("images/v95/day148 morn425.webp", zoom=0.195)
            else:
                imagebutton:
                    idle Transform("ui/locked.png", zoom=0.2)
            
            if persistent.day148imogeneSex == 1 or persistent.g_Unlock == 1:
                imagebutton:
                        action Replay("day148imogeneSex", locked=False)
                        idle Transform("images/v95/day148 morn486.webp", zoom=0.2)
                        hover Transform("images/v95/day148 morn486.webp", zoom=0.195)
            else:
                imagebutton:
                    idle Transform("ui/locked.png", zoom=0.2)
            
            imagebutton:
                idle Transform("ui/empty.png", zoom=0.2)
            
            imagebutton:
                idle Transform("ui/empty.png", zoom=0.2)
            
            imagebutton:
                idle Transform("ui/empty.png", zoom=0.2)
            
            imagebutton:
                idle Transform("ui/empty.png", zoom=0.2)
            
            imagebutton:
                idle Transform("ui/empty.png", zoom=0.2)
            
            imagebutton:
                idle Transform("ui/empty.png", zoom=0.2)

            imagebutton:
                idle Transform("ui/empty.png", zoom=0.2)

# screen gallery8():
    # tag menu
    # add "ui/bg.jpg"
    
    # use game_menu("Gallery 8"):
            
        
        # hbox:
                # style_prefix "page"

                # xalign 0.5
                # yalign 1.0
                # yoffset -30

                # spacing gui.page_spacing
                

                
                # textbutton "1" action Hide("gallery8"), Show("gallery")
                # textbutton "2" action Hide("gallery8"), Show("gallery2")
                # textbutton "3" action Hide("gallery8"), Show("gallery3")
                # textbutton "4" action Hide("gallery8"), Show("gallery4")
                # textbutton "5" action Hide("gallery8"), Show("gallery5")
                # textbutton "6" action Hide("gallery8"), Show("gallery6")
                # textbutton "7" action Hide("gallery8"), Show("gallery7")
                # textbutton "8"

        
        # vbox:
            # frame:
                # yoffset -125
                # xoffset -50
            
                # if persistent.g_Unlock == 1:
                    # textbutton _("Lock Gallery"):
                        # text_style "unlockButton"
                        # action unlockGallery, Hide("gallery8"), Show("gallery8")
                        
                # else:
                    # textbutton _("Unlock Gallery"):
                        # text_style "unlockButton"
                        # action unlockGallery, Hide("gallery8"), Show("gallery8")
                        
        
            
        # grid 3 3:
            # style_prefix "slot"

            # xalign 0.5
            # yalign 0.5
            # xpos 650
            # ypos 360
            
            # spacing gui.slot_spacing
            
            # if persistent.day84pollyFinger == 1 or persistent.g_Unlock == 1:
                # imagebutton:
                        # action Replay("day84pollyFinger", locked=False)
                        # idle Transform("images/v35/day84 morn141.webp", zoom=0.2)
                        # hover Transform("images/v35/day84 morn141.webp", zoom=0.195)
            # else:
                # imagebutton:
                    # idle Transform("ui/locked.png", zoom=0.2)
            
            # if persistent.day84lizMasturbate == 1 or persistent.g_Unlock == 1:
                # imagebutton:
                        # action Replay("day84lizMasturbate", locked=False)
                        # idle Transform("images/v35/day84 night102.webp", zoom=0.2)
                        # hover Transform("images/v35/day84 night102.webp", zoom=0.195)
            # else:
                # imagebutton:
                    # idle Transform("ui/locked.png", zoom=0.2)
            
            # if persistent.day85jamilaBreastfeed == 1 or persistent.g_Unlock == 1:
                # imagebutton:
                        # action Replay("day85jamilaBreastfeed", locked=False)
                        # idle Transform("images/v35/day85 morn33.webp", zoom=0.2)
                        # hover Transform("images/v35/day85 morn33.webp", zoom=0.195)
            # else:
                # imagebutton:
                    # idle Transform("ui/locked.png", zoom=0.2)
            
            # if persistent.day85anabelleFinger == 1 or persistent.g_Unlock == 1:
                # imagebutton:
                        # action Replay("day85anabelleFinger", locked=False)
                        # idle Transform("images/v35/day85 ana46.webp", zoom=0.2)
                        # hover Transform("images/v35/day85 ana46.webp", zoom=0.195)
            # else:
                # imagebutton:
                    # idle Transform("ui/locked.png", zoom=0.2)
            
            # if persistent.day86shizukashower == 1 or persistent.g_Unlock == 1:
                # imagebutton:
                        # action Replay("day86shizukashower", locked=False)
                        # idle Transform("images/v36/day86 morn50.webp", zoom=0.2)
                        # hover Transform("images/v36/day86 morn50.webp", zoom=0.195)
            # else:
                # imagebutton:
                    # idle Transform("ui/locked.png", zoom=0.2)
            
            # if persistent.day87priyaBJ == 1 or persistent.g_Unlock == 1:
                # imagebutton:
                        # action Replay("day87priyaBJ", locked=False)
                        # idle Transform("images/v37/day87 doc73.webp", zoom=0.2)
                        # hover Transform("images/v37/day87 doc73.webp", zoom=0.195)
            # else:
                # imagebutton:
                    # idle Transform("ui/locked.png", zoom=0.2)
            
            # if persistent.day87jamilaBath == 1 or persistent.g_Unlock == 1:
                # imagebutton:
                        # action Replay("day87jamilaBath", locked=False)
                        # idle Transform("images/v37/day87 jam2.webp", zoom=0.2)
                        # hover Transform("images/v37/day87 jam2.webp", zoom=0.195)
            # else:
                # imagebutton:
                    # idle Transform("ui/locked.png", zoom=0.2)
            
            # if persistent.day87sophiaSex == 1 or persistent.g_Unlock == 1:
                # imagebutton:
                        # action Replay("day87sophiaSex", locked=False)
                        # idle Transform("images/v37/day87 soph79.webp", zoom=0.2)
                        # hover Transform("images/v37/day87 soph79.webp", zoom=0.195)
            # else:
                # imagebutton:
                    # idle Transform("ui/locked.png", zoom=0.2)

            # imagebutton:
                # idle Transform("ui/empty.png", zoom=0.2)
                    

python early:
    def unlockGallery():
        if persistent.g_Unlock == 1:
            persistent.g_Unlock = 0
        elif persistent.g_Unlock == 0:
            persistent.g_Unlock = 1
            
python early:
    def changePage(pageNum):
        Hide(renpy.current_screen)