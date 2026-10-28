

#SPECIAL RENDERS
default persistent.reb_render1 = False
default persistent.reb_render2 = False
default persistent.reb_render3 = False

default persistent.diana_render1 = False
default persistent.diana_render2 = False
default persistent.diana_render3 = False

default persistent.maia_render1 = False
default persistent.maia_render2 = False

default persistent.kat_render1 = False
default persistent.kat_render2 = False
default persistent.kat_render3 = False

default persistent.yuuhi_render1 = False
default persistent.yuuhi_render2 = False

default persistent.nadia_render1 = False

default persistent.alex_render1 = False
default persistent.alex_render2 = False
default persistent.alex_render3 = False

default persistent.mix_render1 = False #Queen
default persistent.mix_render2 = False #Prince
default persistent.mix_render3 = True #Fan art
default persistent.mix_render4 = False #Serena

default persistent.queen_render1 = False

if persistent.queen_render1:
    $ persistent.mix_render1 = True

default in_scene_replay = False
default in_gallery_gui_main = False
default in_gallery_gui_main_images = False
default in_gallery_gui_main_scenes = False
default in_gallery_gui_main_scenes_c1_page1 = False
default in_gallery_gui_main_scenes_c1_page2 = False
default in_gallery_gui_main_scenes_c1_page3 = False
default in_gallery_gui_main_scenes_c1_page4 = False
default in_gallery_gui_main_scenes_c1_page5 = False
default in_gallery_gui_main_scenes_c1_page6 = False
default in_gallery_gui_main_scenes_c1_page7 = False

default in_gallery_gui_main_scenes_freeroam_page1 = False
default in_gallery_gui_main_scenes_freeroam_page2 = False
default in_gallery_gui_main_scenes_freeroam_page3 = False
default in_gallery_gui_main_scenes_freeroam_page4 = False

#SCENES PAGE 1
default persistent.scene1_replay = False
default persistent.scene2_replay = False
default persistent.scene3_replay = False
default persistent.scene4_replay = False
default persistent.scene5_replay = False
default persistent.scene6_replay = False
default persistent.scene7_replay = False
default persistent.scene8_replay = False
#SCENES PAGE 2
default persistent.scene1_p2_replay = False
default persistent.scene2_p2_replay = False
default persistent.scene3_p2_replay = False
default persistent.scene4_p2_replay = False
default persistent.scene5_p2_replay = False
default persistent.scene6_p2_replay = False
default persistent.scene7_p2_replay = False
default persistent.scene8_p2_replay = False
#SCENES PAGE 3
default persistent.scene1_p3_replay = False
default persistent.scene2_p3_replay = False
default persistent.scene3_p3_replay = False
default persistent.scene4_p3_replay = False
default persistent.scene5_p3_replay = False
default persistent.scene6_p3_replay = False
default persistent.scene7_p3_replay = False
default persistent.scene8_p3_replay = False
#SCENES PAGE 4
default persistent.scene1_p4_replay = False
default persistent.scene2_p4_replay = False
default persistent.scene3_p4_replay = False
default persistent.scene4_p4_replay = False
default persistent.scene5_p4_replay = False
default persistent.scene6_p4_replay = False
default persistent.scene7_p4_replay = False
default persistent.scene8_p4_replay = False
#SCENES PAGE 5
default persistent.scene1_p5_replay = False
default persistent.scene2_p5_replay = False
default persistent.scene3_p5_replay = False
default persistent.scene4_p5_replay = False
default persistent.scene5_p5_replay = False
default persistent.scene6_p5_replay = False
default persistent.scene7_p5_replay = False
default persistent.scene8_p5_replay = False
#SCENES PAGE6
default persistent.scene1_p6_replay = False
default persistent.scene2_p6_replay = False
default persistent.scene3_p6_replay = False 
default persistent.scene4_p6_replay = False 
default persistent.scene5_p6_replay = False 
default persistent.scene6_p6_replay = False 
default persistent.scene7_p6_replay = False 
default persistent.scene8_p6_replay = False 
#SCENES PAGE7
default persistent.scene1_p7_replay = False 
default persistent.scene2_p7_replay = False 
default persistent.scene3_p7_replay = False 
default persistent.scene4_p7_replay = False 
default persistent.scene5_p7_replay = False 

#CHAPTER 5
default persistent.chapter5_p7_2_replay = False 
default persistent.chapter5_p7_3_replay = False 
default persistent.chapter5_p7_4_replay = False 
default persistent.chapter5_p7_5_replay = False 
default persistent.chapter5_p7_6_replay = False 
default persistent.chapter5_p7_7_replay = False 
default persistent.chapter5_p7_8_replay = False 



default reset_variables = False

default in_gallery_gui_main_scenes_select_chapter = False
default gllarey_gui_scenes_chapters_1 = False
default gllarey_gui_scenes_chapters_2 = False
default gllarey_gui_scenes_chapters_3 = False
default gllarey_gui_scenes_chapters_4 = False
default gllarey_gui_scenes_chapters_5 = False
default gllarey_gui_scenes_chapters_6 = False
default gllarey_gui_scenes_chapters_7 = False
default gllarey_gui_scenes_freeroam = False

screen scene_image_gallery():
    key "mouseup_3" action [Hide("scene_image_gallery"), Show("main_menu"), SetVariable("in_gallery_gui_main", False), SetVariable("in_gallery_gui_main_scenes", False), SetVariable("in_gallery_gui_main_images", False)]
    key "K_ESCAPE" action [Hide("scene_image_gallery"), Show("main_menu"), SetVariable("in_gallery_gui_main", False), SetVariable("in_gallery_gui_main_scenes", False), SetVariable("in_gallery_gui_main_images", False)]
    
    if in_gallery_gui_main:
        add "gallery_gui_main"
        imagebutton auto "gallery_gui_main_scenes_%s":
            focus_mask True
            action [SetVariable("in_gallery_gui_main", False), SetVariable("in_gallery_gui_main_scenes", True), SetVariable("in_gallery_gui_main_scenes_select_chapter", True)]
        
        imagebutton auto "gallery_gui_main_images_%s":
            focus_mask True
            action [SetVariable("in_gallery_gui_main", False), SetVariable("in_gallery_gui_main_images", True)]

        imagebutton auto "gallery_gui_main_back_%s":
            focus_mask True
            action Jump("scene_image_gallery_back")
            
        imagebutton auto "reset_variables_%s":
            focus_mask True
            action [SetVariable("reset_variables", True), SetVariable("in_gallery_gui_main", False)]

    if in_gallery_gui_main_images:
        key "mouseup_3" action [SetVariable("in_gallery_gui_main", True), SetVariable("in_gallery_gui_main_images", False)]
        key "K_ESCAPE" action [SetVariable("in_gallery_gui_main", True), SetVariable("in_gallery_gui_main_images", False)]

        add "gallery_gui_main_images"
        imagebutton auto "gallery_gui_main_images_maia_%s":
            focus_mask True
            action Jump("gallery_gui_main_images_maia")
        
        imagebutton auto "gallery_gui_main_images_reb_%s":
            focus_mask True
            action Jump("gallery_gui_main_images_reb")
        
        imagebutton auto "gallery_gui_main_images_diana_%s":
            focus_mask True
            action Jump("gallery_gui_main_images_diana")
        
        imagebutton auto "gallery_gui_main_images_kat_%s":
            focus_mask True
            action Jump("gallery_gui_main_images_kat")
        
        imagebutton auto "gallery_gui_main_images_nadia_%s":
            focus_mask True
            action Jump("gallery_gui_main_images_nadia")
        
        imagebutton auto "gallery_gui_main_images_yuuhi_%s":
            focus_mask True
            action Jump("gallery_gui_main_images_yuuhi")
        
        imagebutton auto "gallery_gui_main_images_alex_%s":
            focus_mask True
            action Jump("gallery_gui_main_images_alex")
        
        imagebutton auto "gallery_gui_main_images_mix_%s":
            focus_mask True
            action Jump("gallery_gui_main_images_mix")

        imagebutton auto "gallery_gui_main_images_back_%s":
            focus_mask True
            action [SetVariable("in_gallery_gui_main", True), SetVariable("in_gallery_gui_main_images", False)]

    if reset_variables:
        add "reset_variables_bg"

        imagebutton auto "free_roam_end_yes_%s":
            focus_mask True
            action Jump("reset_variables")
    
        imagebutton auto "free_roam_end_no_%s":
            focus_mask True
            action [SetVariable("reset_variables", False), SetVariable("in_gallery_gui_main", True)]

    if in_gallery_gui_main_scenes:
        textbutton "Reload Game" action Function(renpy.quit, relaunch=True)
        add "gallery_gui_scenes_main"

        if in_gallery_gui_main_scenes_select_chapter:
            add "gallery_gui_scenes_main_page_chapter_select"

            key "mouseup_3" action [SetVariable("in_gallery_gui_main", True), SetVariable("in_gallery_gui_main_scenes", False)]
            key "K_ESCAPE" action [SetVariable("in_gallery_gui_main", True), SetVariable("in_gallery_gui_main_scenes", False)]
            imagebutton auto "gallery_gui_main_images_back_%s":
                focus_mask True
                action [SetVariable("in_gallery_gui_main_scenes", False), SetVariable("in_gallery_gui_main", True)]
            
            imagebutton auto "gllarey_gui_scenes_chapters_1_%s":
                focus_mask True
                action [SetVariable("in_gallery_gui_main_scenes_select_chapter", False), SetVariable("gllarey_gui_scenes_chapters_1", True), SetVariable("in_gallery_gui_main_scenes_c1_page1", True)]

            imagebutton auto "gllarey_gui_scenes_chapters_2_%s":
                focus_mask True
                action [SetVariable("in_gallery_gui_main_scenes_select_chapter", False), SetVariable("gllarey_gui_scenes_chapters_2", True), SetVariable("in_gallery_gui_main_scenes_c1_page2", True)]

            imagebutton auto "gllarey_gui_scenes_chapters_3_%s":
                focus_mask True
                action [SetVariable("in_gallery_gui_main_scenes_select_chapter", False), SetVariable("gllarey_gui_scenes_chapters_3", True), SetVariable("in_gallery_gui_main_scenes_c1_page4", True)]

            imagebutton auto "gllarey_gui_scenes_chapters_4_%s":
                focus_mask True
                action [SetVariable("in_gallery_gui_main_scenes_select_chapter", False), SetVariable("gllarey_gui_scenes_chapters_4", True), SetVariable("in_gallery_gui_main_scenes_c1_page6", True)]

            imagebutton auto "gllarey_gui_scenes_chapters_5_%s":
                focus_mask True
                action [SetVariable("in_gallery_gui_main_scenes_select_chapter", False), SetVariable("gllarey_gui_scenes_chapters_5", True), SetVariable("in_gallery_gui_main_scenes_c1_page7", True)]
                    
            imagebutton auto "gllarey_gui_scenes_chapters_6_%s":
                focus_mask True
                action Notify("This chapter is not yet available.")

            imagebutton auto "gllarey_gui_scenes_chapters_7_%s":
                focus_mask True
                action Notify("This chapter is not yet available.")

            imagebutton auto "gllarey_gui_scenes_freeroam_%s":
                focus_mask True
                action [SetVariable("in_gallery_gui_main_scenes_select_chapter", False), SetVariable("gllarey_gui_scenes_freeroam", True), SetVariable("in_gallery_gui_main_scenes_freeroam_page1", True)]

        if in_gallery_gui_main_scenes_c1_page1: #Chapter 1
            key "mouseup_3" action [SetVariable("in_gallery_gui_main_scenes_c1_page1", False), SetVariable("in_gallery_gui_main_scenes_select_chapter", True)]
            key "K_ESCAPE" action [SetVariable("in_gallery_gui_main_scenes_c1_page1", False), SetVariable("in_gallery_gui_main_scenes_select_chapter", True)]
            imagebutton auto "gallery_gui_main_images_back_%s":
                focus_mask True
                action [SetVariable("in_gallery_gui_main_scenes_c1_page1", False), SetVariable("in_gallery_gui_main_scenes_select_chapter", True)]

            add "gallery_gui_scenes_main_page_chapter1"
        
            if not persistent.scene1_replay: #RUBY
                add "gallery_gui_scene_box1_locked"
            else:
                imagebutton auto "gallery_gui_scene_box1_c1_%s":
                    focus_mask True
                    action [SetVariable("in_scene_replay", True), Replay("scene04_choice08_bj")]

            if not persistent.scene2_replay: #DIANA FIRST
                add "gallery_gui_scene_box2_locked"
            else:
                imagebutton auto "gallery_gui_scene_box2_c1_%s":
                    focus_mask True
                    action [SetVariable("in_scene_replay", True), Replay("scene05")]

            if not persistent.scene3_replay: #MAIA SHOWER
                add "gallery_gui_scene_box3_locked"
            else:
                imagebutton auto "gallery_gui_scene_box3_c1_%s":
                    focus_mask True
                    action [SetVariable("in_scene_replay", True), Replay("scene10")]

            if not persistent.scene7_replay: #MAIA CRUMPS
                add "gallery_gui_scene_box4_locked"
            else:
                imagebutton auto "gallery_gui_scene_box4_c1_%s":
                    focus_mask True
                    action [SetVariable("in_scene_replay", True), Replay("scene27_sex")]

            if not persistent.scene5_replay: #MAIA PUNISH
                add "gallery_gui_scene_box5_locked"
            else:
                imagebutton auto "gallery_gui_scene_box5_c1_%s":
                    focus_mask True
                    action [SetVariable("in_scene_replay", True), Replay("scene16_choice03_op2")]
                    
            if not persistent.scene6_replay: #YUUHI FIRST
                add "gallery_gui_scene_box6_locked"
            else:
                imagebutton auto "gallery_gui_scene_box6_c1_%s":
                    focus_mask True
                    action [SetVariable("in_scene_replay", True), Replay("scene24")]

            if not persistent.scene8_replay: #REHAM
                add "gallery_gui_scene_box7_locked"
            else:
                imagebutton auto "gallery_gui_scene_box7_c1_%s":
                    focus_mask True
                    action [SetVariable("in_scene_replay", True), Replay("scene29_choice11_op1")]
                    

        if in_gallery_gui_main_scenes_c1_page2: #Chapter 2 A
            key "mouseup_3" action [SetVariable("in_gallery_gui_main_scenes_c1_page2", False), SetVariable("in_gallery_gui_main_scenes_select_chapter", True)]
            key "K_ESCAPE" action [SetVariable("in_gallery_gui_main_scenes_c1_page2", False), SetVariable("in_gallery_gui_main_scenes_select_chapter", True)]

            add "gallery_gui_scenes_main_page_chapter2_1"

            imagebutton auto "gallery_gui_main_images_back_%s":
                focus_mask True
                action [SetVariable("in_gallery_gui_main_scenes_c1_page2", False), SetVariable("in_gallery_gui_main_scenes_select_chapter", True)]

            imagebutton auto "gallery_gui_scenes_main_right_arrow_%s":
                focus_mask True
                action [SetVariable("in_gallery_gui_main_scenes_c1_page2", False), SetVariable("in_gallery_gui_main_scenes_c1_page3", True)]
            
            if not persistent.scene2_p2_replay: #AMELIA
                add "gallery_gui_scene_box1_locked"
            else:
                imagebutton auto "gallery_gui_scene_box1_c2_%s":
                    focus_mask True
                    action [SetVariable("in_scene_replay", True), Replay("scene34_witch2_consent")]
            
            if not persistent.scene1_p2_replay: #NADIA 
                add "gallery_gui_scene_box2_locked"
            else:
                imagebutton auto "gallery_gui_scene_box2_c2_%s":
                    focus_mask True
                    action [SetVariable("in_scene_replay", True), Replay("scene29_choice000000_op1")]

            if not persistent.scene1_p4_replay: #ALEX FLASHBACK SEX
                add "gallery_gui_scene_box3_locked"
            else:
                imagebutton auto "gallery_gui_scene_box3_c2_%s":
                    focus_mask True
                    action [SetVariable("in_scene_replay", True), Replay("scene37_alex_sex")]

            if not persistent.scene2_p4_replay: #ALEX FLASHBACK FOOTJOB
                add "gallery_gui_scene_box4_locked"
            else:
                imagebutton auto "gallery_gui_scene_box4_c2_%s":
                    focus_mask True
                    action [SetVariable("in_scene_replay", True), Replay("scene37_choice04_op1")]

            if not persistent.scene3_p4_replay: #YMIR SUB
                add "gallery_gui_scene_box5_locked"
            else:
                imagebutton auto "gallery_gui_scene_box5_c2_%s":
                    focus_mask True
                    action [SetVariable("in_scene_replay", True), Replay("scene40_choice02_op1")]

            if not persistent.scene4_p4_replay: #YMIR DOM
                add "gallery_gui_scene_box6_locked"
            else:
                imagebutton auto "gallery_gui_scene_box6_c2_%s":
                    focus_mask True
                    action [SetVariable("in_scene_replay", True), Replay("scene40_choice02_op2")]

            if not persistent.scene5_p4_replay: #YSELLA HANDJOB
                add "gallery_gui_scene_box7_locked"
            else:
                imagebutton auto "gallery_gui_scene_box7_c2_%s":
                    focus_mask True
                    action [SetVariable("in_scene_replay", True), Replay("scene41_choice01_op2")]
            
            if not persistent.scene6_p4_replay: #ALEX MASTURBATE
                add "gallery_gui_scene_box8_locked"
            else:
                imagebutton auto "gallery_gui_scene_box8_c2_%s":
                    focus_mask True
                    action [SetVariable("in_scene_replay", True), Replay("scene43_choice06_op1")]

        if in_gallery_gui_main_scenes_c1_page3: #Chapter 2 B
            key "mouseup_3" action [SetVariable("in_gallery_gui_main_scenes_c1_page3", False), SetVariable("in_gallery_gui_main_scenes_select_chapter", True)]
            key "K_ESCAPE" action [SetVariable("in_gallery_gui_main_scenes_c1_page3", False), SetVariable("in_gallery_gui_main_scenes_select_chapter", True)]

            add "gallery_gui_scenes_main_page_chapter2_2"

            imagebutton auto "gallery_gui_main_images_back_%s":
                focus_mask True
                action [SetVariable("in_gallery_gui_main_scenes_c1_page3", False), SetVariable("in_gallery_gui_main_scenes_select_chapter", True)]

            imagebutton auto "gallery_gui_scenes_main_left_arrow_%s":
                focus_mask True
                action [SetVariable("in_gallery_gui_main_scenes_c1_page2", True), SetVariable("in_gallery_gui_main_scenes_c1_page3", False)]

            if not persistent.scene7_p4_replay: #MAIA MASTURBATE
                add "gallery_gui_scene_box1_locked"
            else:
                imagebutton auto "gallery_gui_scene_box1_c3_%s":
                    focus_mask True
                    action [SetVariable("in_scene_replay", True), Replay("scene44")]
            
            if not persistent.scene8_p4_replay: #ROZA AND ADA
                add "gallery_gui_scene_box2_locked"
            else:
                imagebutton auto "gallery_gui_scene_box2_c3_%s":
                    focus_mask True
                    action [SetVariable("in_scene_replay", True), Replay("scene46_adaroza_sex")]

            if not persistent.scene1_p5_replay: #ANNETTE
                add "gallery_gui_scene_box3_locked"
            else:
                imagebutton auto "gallery_gui_scene_box3_c3_%s":
                    focus_mask True
                    action [SetVariable("in_scene_replay", True), Replay("scene47_annette_sex")]

            if not persistent.scene2_p5_replay: #SIGRUN
                add "gallery_gui_scene_box4_locked"
            else:
                imagebutton auto "gallery_gui_scene_box4_c3_%s":
                    focus_mask True
                    action [SetVariable("in_scene_replay", True), Replay("scene48_sigrun_sex")]
                    
        if in_gallery_gui_main_scenes_c1_page4: #CHAPTER 3 A
            key "mouseup_3" action [SetVariable("in_gallery_gui_main_scenes_c1_page4", False), SetVariable("in_gallery_gui_main_scenes_select_chapter", True)]
            key "K_ESCAPE" action [SetVariable("in_gallery_gui_main_scenes_c1_page4", False), SetVariable("in_gallery_gui_main_scenes_select_chapter", True)]

            add "gallery_gui_scenes_main_page_chapter3_1"

            imagebutton auto "gallery_gui_main_images_back_%s":
                focus_mask True
                action [SetVariable("in_gallery_gui_main_scenes_c1_page4", False), SetVariable("in_gallery_gui_main_scenes_select_chapter", True)]

            imagebutton auto "gallery_gui_scenes_main_right_arrow_%s":
                focus_mask True
                action [SetVariable("in_gallery_gui_main_scenes_c1_page5", True), SetVariable("in_gallery_gui_main_scenes_c1_page4", False)]

            if not persistent.scene3_p5_replay: #MAIA SEX 0.3.1
                add "gallery_gui_scene_box1_locked"
            else:
                imagebutton auto "gallery_gui_scene_box1_c4_%s":
                    focus_mask True
                    action [SetVariable("in_scene_replay", True), Replay("scene53_choice01_op1")]

            if not persistent.scene4_p5_replay: #REB FIRST HANDJOB
                add "gallery_gui_scene_box2_locked"
            else:
                imagebutton auto "gallery_gui_scene_box2_c4_%s":
                    focus_mask True
                    action [SetVariable("in_scene_replay", True), Replay("scene57_choice01_op2")]

            if not persistent.scene7_p5_replay: #SELENE MASSAGE
                add "gallery_gui_scene_box3_locked"
            else:
                imagebutton auto "gallery_gui_scene_box3_c4_%s":
                    focus_mask True
                    action [SetVariable("in_scene_replay", True), Replay("scene61_2")]

            if not persistent.scene8_p5_replay: #MAIA 0.3.2
                add "gallery_gui_scene_box4_locked"
            else:
                imagebutton auto "gallery_gui_scene_box4_c4_%s":
                    focus_mask True
                    action [SetVariable("in_scene_replay", True), Replay("scene64_choice01_op2")]

            if not persistent.scene1_p6_replay: #JENNY 1
                add "gallery_gui_scene_box5_locked"
            else:
                imagebutton auto "gallery_gui_scene_box5_c4_%s":
                    focus_mask True
                    action [SetVariable("in_scene_replay", True), Replay("scene69_choice01_op1")]

            if not persistent.scene2_p6_replay: #AVERY FEET
                add "gallery_gui_scene_box6_locked"
            else:
                imagebutton auto "gallery_gui_scene_box6_c4_%s":
                    focus_mask True
                    action [SetVariable("in_scene_replay", True), Replay("scene70_choice01_op1")]
            
            if not persistent.scene3_p6_replay: #RNR TENTACLES
                add "gallery_gui_scene_box7_locked"
            else:
                imagebutton auto "gallery_gui_scene_box7_c4_%s":
                    focus_mask True
                    action [SetVariable("in_scene_replay", True), Replay("s72_dLEFT_LEFT_LEFT_RIGHT_UP_LEFT_tenta")]

            if not persistent.scene4_p6_replay: #RNR WITCH
                add "gallery_gui_scene_box8_locked"
            else:
                imagebutton auto "gallery_gui_scene_box8_c4_%s":
                    focus_mask True
                    action [SetVariable("in_scene_replay", True), Replay("s72_dRIGHT_RIGHT_RIGHT_LEFT_UP_LEFT_LEFT_LEFT_UP_witch")]

        if in_gallery_gui_main_scenes_c1_page5: #CHAPTER 3 B
            key "mouseup_3" action [SetVariable("in_gallery_gui_main_scenes_c1_page5", False), SetVariable("in_gallery_gui_main_scenes_select_chapter", True)]
            key "K_ESCAPE" action [SetVariable("in_gallery_gui_main_scenes_c1_page5", False), SetVariable("in_gallery_gui_main_scenes_select_chapter", True)]

            add "gallery_gui_scenes_main_page_chapter3_2"

            imagebutton auto "gallery_gui_main_images_back_%s":
                focus_mask True
                action [SetVariable("in_gallery_gui_main_scenes_c1_page5", False), SetVariable("in_gallery_gui_main_scenes_select_chapter", True)]

            imagebutton auto "gallery_gui_scenes_main_left_arrow_%s":
                focus_mask True
                action [SetVariable("in_gallery_gui_main_scenes_c1_page4", True), SetVariable("in_gallery_gui_main_scenes_c1_page5", False)]

            if not persistent.scene5_p6_replay: #REB EJAC SECTIONS
                add "gallery_gui_scene_box1_locked"
            else:
                imagebutton auto "gallery_gui_scene_box1_c5_%s":
                    focus_mask True
                    action [SetVariable("in_scene_replay", True), Replay("scene73")]
            
            if not persistent.scene6_p6_replay: #REB SEX
                add "gallery_gui_scene_box2_locked"
            else:
                imagebutton auto "gallery_gui_scene_box2_c5_%s":
                    focus_mask True
                    action [SetVariable("in_scene_replay", True), Replay("scene75_4")]

            if not persistent.scene4_replay: #QUEEN (OUT OF PLACE GOD FUCKING ASS SHIT)
                add "gallery_gui_scene_box3_locked"
            else:
                imagebutton auto "gallery_gui_scene_box3_c5_%s":
                    focus_mask True
                    action [SetVariable("in_scene_replay", True), Replay("scene13")]

        if in_gallery_gui_main_scenes_c1_page6: #CHAPTER 4
            key "mouseup_3" action [SetVariable("in_gallery_gui_main_scenes_c1_page6", False), SetVariable("in_gallery_gui_main_scenes_select_chapter", True)]
            key "K_ESCAPE" action [SetVariable("in_gallery_gui_main_scenes_c1_page6", False), SetVariable("in_gallery_gui_main_scenes_select_chapter", True)]

            add "gallery_gui_scenes_main_page_chapter4"

            imagebutton auto "gallery_gui_main_images_back_%s":
                focus_mask True
                action [SetVariable("in_gallery_gui_main_scenes_c1_page6", False), SetVariable("in_gallery_gui_main_scenes_select_chapter", True)]

            if not persistent.scene7_p6_replay: #ALEX MASTURBATE
                add "gallery_gui_scene_box1_locked"
            else:
                imagebutton auto "gallery_gui_scene_box1_c6_%s":
                    focus_mask True
                    action [SetVariable("in_scene_replay", True), SetVariable("mc_masturbated_to_alex", True), SetVariable("mc_paricipated_festival", True),  Replay("scene81_alex")]
                
            if not persistent.scene8_p6_replay: #REHAM SCENE1
                add "gallery_gui_scene_box2_locked"
            else:
                imagebutton auto "gallery_gui_scene_box2_c6_%s":
                    focus_mask True
                    action [SetVariable("in_scene_replay", True), Replay("scene82_choice06_op2")]

            if not persistent.scene1_p7_replay: #MAIA SEX SCENE84
                add "gallery_gui_scene_box3_locked"
            else:
                imagebutton auto "gallery_gui_scene_box3_c6_%s":
                    focus_mask True
                    action [SetVariable("in_scene_replay", True), Replay("scene84_choice03_op1")]
            
            if not persistent.scene2_p7_replay: #YUUHI ANAL PLAY
                add "gallery_gui_scene_box4_locked"
            else:
                imagebutton auto "gallery_gui_scene_box4_c6_%s":
                    focus_mask True
                    action [SetVariable("in_scene_replay", True), Replay("scene90_choice01_op1_2")]

            if not persistent.scene3_p7_replay: #WITCH MILKING
                add "gallery_gui_scene_box5_locked"
            else:
                imagebutton auto "gallery_gui_scene_box5_c6_%s":
                    focus_mask True
                    action [SetVariable("in_scene_replay", True), Replay("scene94")]
            
            if not persistent.scene4_p7_replay: #KAT BJ
                add "gallery_gui_scene_box6_locked"
            else:
                imagebutton auto "gallery_gui_scene_box6_c6_%s":
                    focus_mask True
                    action [SetVariable("in_scene_replay", True), Replay("scene98_2")]
                    
        if in_gallery_gui_main_scenes_c1_page7: #CHAPTER 5
            key "mouseup_3" action [SetVariable("in_gallery_gui_main_scenes_c1_page7", False), SetVariable("in_gallery_gui_main_scenes_select_chapter", True)]
            key "K_ESCAPE" action [SetVariable("in_gallery_gui_main_scenes_c1_page7", False), SetVariable("in_gallery_gui_main_scenes_select_chapter", True)]

            add "gallery_gui_scenes_main_page_chapter5"
            
            imagebutton auto "gallery_gui_main_images_back_%s":
                focus_mask True
                action [SetVariable("in_gallery_gui_main_scenes_c1_page7", False), SetVariable("in_gallery_gui_main_scenes_select_chapter", True)]

            if not persistent.scene5_p7_replay: #MAIA REHAM THREESOME
                add "gallery_gui_scene_box1_locked"
            else:
                imagebutton auto "gallery_gui_scene_box1_c7_%s":
                    focus_mask True
                    action [SetVariable("in_scene_replay", True), Replay("scene105_4")]

            if not persistent.chapter5_p7_2_replay: #JENNY 2
                add "gallery_gui_scene_box2_locked"
            else:
                imagebutton auto "gallery_gui_scene_box2_c7_%s":
                    focus_mask True
                    action [SetVariable("in_scene_replay", True), Replay("scene112_3")]

            if not persistent.chapter5_p7_3_replay: #LENA
                add "gallery_gui_scene_box3_locked"
            else:
                imagebutton auto "gallery_gui_scene_box3_c7_%s":
                    focus_mask True
                    action [SetVariable("in_scene_replay", True), Replay("scene115_choice02_op1")]
            
            if not persistent.chapter5_p7_4_replay: #RUBY 2
                add "gallery_gui_scene_box4_locked"
            else:
                imagebutton auto "gallery_gui_scene_box4_c7_%s":
                    focus_mask True
                    action [SetVariable("in_scene_replay", True), Replay("scene114_choice11_op3")]
            
            if not persistent.chapter5_p7_5_replay: #PRINCESS 0.5.0
                add "gallery_gui_scene_box5_locked"
            else:
                imagebutton auto "gallery_gui_scene_box5_c7_%s":
                    focus_mask True
                    action [SetVariable("in_scene_replay", True), Replay("scene124_sex")]

            if not persistent.chapter5_p7_6_replay: #REHAM HAREM SEX
                add "gallery_gui_scene_box6_locked"
            else:
                imagebutton auto "gallery_gui_scene_box6_c7_%s":
                    focus_mask True
                    action [SetVariable("in_scene_replay", True), Replay("scene130_sex")]
            
            if not persistent.chapter5_p7_7_replay: #REHAM NO HAREM HJ
                add "gallery_gui_scene_box7_locked"
            else:
                imagebutton auto "gallery_gui_scene_box7_c7_%s":
                    focus_mask True
                    action [SetVariable("in_scene_replay", True), Replay("scene130_hj")]
            
            if not persistent.chapter5_p7_8_replay: #PALACE SERVANTS
                add "gallery_gui_scene_box8_locked"
            else:
                imagebutton auto "gallery_gui_scene_box8_c7_%s":
                    focus_mask True
                    action [SetVariable("in_scene_replay", True), Replay("s134_servants")]


        if in_gallery_gui_main_scenes_freeroam_page1: #FREE ROAM 1
            key "mouseup_3" action [SetVariable("in_gallery_gui_main_scenes_freeroam_page1", False), SetVariable("in_gallery_gui_main_scenes_select_chapter", True)]
            key "K_ESCAPE" action [SetVariable("in_gallery_gui_main_scenes_freeroam_page1", False), SetVariable("in_gallery_gui_main_scenes_select_chapter", True)]

            add "gallery_gui_scenes_main_page_freeroam_maia"
            
            imagebutton auto "gallery_gui_main_images_back_%s":
                focus_mask True
                action [SetVariable("in_gallery_gui_main_scenes_freeroam_page1", False), SetVariable("in_gallery_gui_main_scenes_select_chapter", True)]

            imagebutton auto "gallery_gui_scenes_main_right_arrow_%s":
                focus_mask True
                action [SetVariable("in_gallery_gui_main_scenes_freeroam_page2", True), SetVariable("in_gallery_gui_main_scenes_freeroam_page1", False)]

            if not persistent.scene3_p2_replay: #MAIA HJ
                add "gallery_gui_scene_box1_locked"
            else:
                imagebutton auto "gallery_gui_scene_box1_freeroam1_%s":
                    focus_mask True
                    action [SetVariable("in_scene_replay", True), Replay("is_maia_hj1")]
            
            if not persistent.scene4_p2_replay: #MAIA TJ
                add "gallery_gui_scene_box2_locked"
            else:
                imagebutton auto "gallery_gui_scene_box2_freeroam1_%s":
                    focus_mask True
                    action [SetVariable("in_scene_replay", True), Replay("is_maia_tj1")]
            
            if not persistent.scene5_p2_replay: #MAIA BJ
                add "gallery_gui_scene_box3_locked"
            else:
                imagebutton auto "gallery_gui_scene_box3_freeroam1_%s":
                    focus_mask True
                    action [SetVariable("in_scene_replay", True), Replay("is_maia_bj")]
            
            if not persistent.scene6_p2_replay: #MAIA SEX
                add "gallery_gui_scene_box4_locked"
            else:
                imagebutton auto "gallery_gui_scene_box4_freeroam1_%s":
                    focus_mask True
                    action [SetVariable("in_scene_replay", True), Replay("is_maia_sex")]
            
            if not persistent.scene7_p2_replay: #MAIA FJ
                add "gallery_gui_scene_box5_locked"
            else:
                imagebutton auto "gallery_gui_scene_box5_freeroam1_%s":
                    focus_mask True
                    action [SetVariable("in_scene_replay", True), Replay("is_maia_footjob")]
            
            if not persistent.scene8_p2_replay: #MAIA NIGHT
                add "gallery_gui_scene_box6_locked"
            else:
                imagebutton auto "gallery_gui_scene_box6_freeroam1_%s":
                    focus_mask True
                    action [SetVariable("in_scene_replay", True), Replay("is_maia_night")]

        if in_gallery_gui_main_scenes_freeroam_page2: #FREE ROAM 2
            key "mouseup_3" action [SetVariable("in_gallery_gui_main_scenes_freeroam_page2", False), SetVariable("in_gallery_gui_main_scenes_select_chapter", True)]
            key "K_ESCAPE" action [SetVariable("in_gallery_gui_main_scenes_freeroam_page2", False), SetVariable("in_gallery_gui_main_scenes_select_chapter", True)]

            add "gallery_gui_scenes_main_page_freeroam_diana"
            
            imagebutton auto "gallery_gui_main_images_back_%s":
                focus_mask True
                action [SetVariable("in_gallery_gui_main_scenes_freeroam_page2", False), SetVariable("in_gallery_gui_main_scenes_select_chapter", True)]

            imagebutton auto "gallery_gui_scenes_main_right_arrow_%s":
                focus_mask True
                action [SetVariable("in_gallery_gui_main_scenes_freeroam_page3", True), SetVariable("in_gallery_gui_main_scenes_freeroam_page2", False)]
            
            imagebutton auto "gallery_gui_scenes_main_left_arrow_%s":
                focus_mask True
                action [SetVariable("in_gallery_gui_main_scenes_freeroam_page1", True), SetVariable("in_gallery_gui_main_scenes_freeroam_page2", False)]

            if not persistent.scene5_p3_replay: #DIANA TJ
                add "gallery_gui_scene_box1_locked"
            else:
                imagebutton auto "gallery_gui_scene_box1_freeroam2_%s":
                    focus_mask True
                    action [SetVariable("in_scene_replay", True), Replay("is_diana_tj2")]

            if not persistent.scene6_p3_replay: #DIANA BJ
                add "gallery_gui_scene_box2_locked"
            else:
                imagebutton auto "gallery_gui_scene_box2_freeroam2_%s":
                    focus_mask True
                    action [SetVariable("in_scene_replay", True), Replay("scene05_choice03_bj")]

            if not persistent.scene7_p3_replay: #DIANA VSEX
                add "gallery_gui_scene_box3_locked"
            else:
                imagebutton auto "gallery_gui_scene_box3_freeroam2_%s":
                    focus_mask True
                    action [SetVariable("in_scene_replay", True), Replay("brothel_diana_vsex")]

            if not persistent.scene8_p3_replay: #DIANA ASEX
                add "gallery_gui_scene_box4_locked"
            else:
                imagebutton auto "gallery_gui_scene_box4_freeroam2_%s":
                    focus_mask True
                    action [SetVariable("in_scene_replay", True), Replay("is_diana_asex2")]

        if in_gallery_gui_main_scenes_freeroam_page3: #FREE ROAM 3
            key "mouseup_3" action [SetVariable("in_gallery_gui_main_scenes_freeroam_page3", False), SetVariable("in_gallery_gui_main_scenes_select_chapter", True)]
            key "K_ESCAPE" action [SetVariable("in_gallery_gui_main_scenes_freeroam_page3", False), SetVariable("in_gallery_gui_main_scenes_select_chapter", True)]

            add "gallery_gui_scenes_main_page_freeroam_yuuhi"
            
            imagebutton auto "gallery_gui_main_images_back_%s":
                focus_mask True
                action [SetVariable("in_gallery_gui_main_scenes_freeroam_page3", False), SetVariable("in_gallery_gui_main_scenes_select_chapter", True)]
            
            imagebutton auto "gallery_gui_scenes_main_right_arrow_%s":
                focus_mask True
                action [SetVariable("in_gallery_gui_main_scenes_freeroam_page4", True), SetVariable("in_gallery_gui_main_scenes_freeroam_page3", False)]

            imagebutton auto "gallery_gui_scenes_main_left_arrow_%s":
                focus_mask True
                action [SetVariable("in_gallery_gui_main_scenes_freeroam_page2", True), SetVariable("in_gallery_gui_main_scenes_freeroam_page3", False)]

            if not persistent.scene1_p3_replay: #YUUHI HJ
                add "gallery_gui_scene_box1_locked"
            else:
                imagebutton auto "gallery_gui_scene_box1_freeroam3_%s":
                    focus_mask True
                    action [SetVariable("in_scene_replay", True), Replay("is_yuuhi_hj1")]

            if not persistent.scene2_p3_replay: #YUUHI BJ
                add "gallery_gui_scene_box2_locked"
            else:
                imagebutton auto "gallery_gui_scene_box2_freeroam3_%s":
                    focus_mask True
                    action [SetVariable("in_scene_replay", True), Replay("is_yuuhi_bj1")]

            if not persistent.scene3_p3_replay: #YUUHI ASEX
                add "gallery_gui_scene_box3_locked"
            else:
                imagebutton auto "gallery_gui_scene_box3_freeroam3_%s":
                    focus_mask True
                    action [SetVariable("in_scene_replay", True), Replay("is_yuuhi_asex1")]

            if not persistent.scene4_p3_replay: #YUUHI FJ
                add "gallery_gui_scene_box4_locked"
            else:
                imagebutton auto "gallery_gui_scene_box4_freeroam3_%s":
                    focus_mask True
                    action [SetVariable("in_scene_replay", True), Replay("is_yuuhi_fj1")]

        if in_gallery_gui_main_scenes_freeroam_page4: #FREE ROAM 4
            key "mouseup_3" action [SetVariable("in_gallery_gui_main_scenes_freeroam_page4", False), SetVariable("in_gallery_gui_main_scenes_select_chapter", True)]
            key "K_ESCAPE" action [SetVariable("in_gallery_gui_main_scenes_freeroam_page4", False), SetVariable("in_gallery_gui_main_scenes_select_chapter", True)]

            add "gallery_gui_scenes_main_page_freeroam_reb"
            
            imagebutton auto "gallery_gui_main_images_back_%s":
                focus_mask True
                action [SetVariable("in_gallery_gui_main_scenes_freeroam_page4", False), SetVariable("in_gallery_gui_main_scenes_select_chapter", True)]

            imagebutton auto "gallery_gui_scenes_main_left_arrow_%s":
                focus_mask True
                action [SetVariable("in_gallery_gui_main_scenes_freeroam_page3", True), SetVariable("in_gallery_gui_main_scenes_freeroam_page4", False)]

            if not persistent.scene5_p5_replay: #REB HANDJOB
                add "gallery_gui_scene_box1_locked"
            else:
                imagebutton auto "gallery_gui_scene_box1_freeroam4_%s":
                    focus_mask True
                    action [SetVariable("in_scene_replay", True), Replay("is_reb_hj_first")]

            if not persistent.scene6_p5_replay: #REB FOOTJOB
                add "gallery_gui_scene_box2_locked"
            else:
                imagebutton auto "gallery_gui_scene_box2_freeroam4_%s":
                    focus_mask True
                    action [SetVariable("in_scene_replay", True), Replay("is_reb_fj_first")]

                
label scene_image_gallery:
    hide screen main_menu
    $ in_gallery_gui_main = True
    scene black
    if in_scene_replay:
        $ in_scene_replay = False
        $ renpy.block_rollback()
    stop music fadeout 1.0
    call screen scene_image_gallery with dissolve

screen debug_text(text=""):
    zorder 100
    text text:
        xalign 0.5
        yalign 0.9
        color "#FF0000"
        size 24
        
screen in_gallery_gui_main_images_maia():
    key "mouseup_3" action [Hide("in_gallery_gui_main_images_maia"), SetVariable("in_gallery_gui_main_images", True), Show("scene_image_gallery")]
    key "K_ESCAPE" action [Hide("in_gallery_gui_main_images_maia"), SetVariable("in_gallery_gui_main_images", True), Show("scene_image_gallery")]
    
    add "gallery_gui_images_images_main"
    imagebutton auto "gallery_gui_main_images_back_%s":
        focus_mask True
        action [Hide("in_gallery_gui_main_images_maia"), SetVariable("in_gallery_gui_main_images", True), Show("scene_image_gallery")]

    if not persistent.maia_render1:
        add "gallery_gui_scene_box1_locked"
    else:
        imagebutton auto "gallery_gui_images_images_main_image1_maia_%s":
            focus_mask True
            action Jump("gallery_gui_images_images_main_image1_maia")

    if not persistent.maia_render2:
        add "gallery_gui_scene_box2_locked"
    else:
        imagebutton auto "gallery_gui_images_images_main_image2_maia_%s":
            focus_mask True
            action Jump("gallery_gui_images_images_main_image2_maia")

screen in_gallery_gui_main_images_reb():
    key "mouseup_3" action [Hide("in_gallery_gui_main_images_reb"), SetVariable("in_gallery_gui_main_images", True), Show("scene_image_gallery")]
    key "K_ESCAPE" action [Hide("in_gallery_gui_main_images_reb"), SetVariable("in_gallery_gui_main_images", True), Show("scene_image_gallery")]
    
    add "gallery_gui_images_images_main"
    imagebutton auto "gallery_gui_main_images_back_%s":
        focus_mask True
        action [Hide("in_gallery_gui_main_images_reb"), SetVariable("in_gallery_gui_main_images", True), Show("scene_image_gallery")]

    if not persistent.reb_render1:
        add "gallery_gui_scene_box1_locked"
    else:
        imagebutton auto "gallery_gui_images_images_main_image1_reb_%s":
            focus_mask True
            action Jump("gallery_gui_images_images_main_image1_reb")

    if not persistent.reb_render2:
        add "gallery_gui_scene_box2_locked"
    else:
        imagebutton auto "gallery_gui_images_images_main_image2_reb_%s":
            focus_mask True
            action Jump("gallery_gui_images_images_main_image2_reb")

    if not persistent.reb_render3:
        add "gallery_gui_scene_box3_locked"
    else:
        imagebutton auto "gallery_gui_images_images_main_image3_reb_%s":
            focus_mask True
            action Jump("gallery_gui_images_images_main_image3_reb")

screen in_gallery_gui_main_images_diana():
    key "mouseup_3" action [Hide("in_gallery_gui_main_images_diana"), SetVariable("in_gallery_gui_main_images", True), Show("scene_image_gallery")]
    key "K_ESCAPE" action [Hide("in_gallery_gui_main_images_diana"), SetVariable("in_gallery_gui_main_images", True), Show("scene_image_gallery")]

    add "gallery_gui_images_images_main"
    imagebutton auto "gallery_gui_main_images_back_%s":
        focus_mask True
        action [Hide("in_gallery_gui_main_images_diana"), SetVariable("in_gallery_gui_main_images", True), Show("scene_image_gallery")]

    if not persistent.diana_render1:
        add "gallery_gui_scene_box1_locked"
    else:
        imagebutton auto "gallery_gui_images_images_main_image1_diana_%s":
            focus_mask True
            action Jump("gallery_gui_images_images_main_image1_diana")
    
    if not persistent.diana_render2:
        add "gallery_gui_scene_box2_locked"
    else:
        imagebutton auto "gallery_gui_images_images_main_image2_diana_%s":
            focus_mask True
            action Jump("gallery_gui_images_images_main_image2_diana")

    if not persistent.diana_render3:
        add "gallery_gui_scene_box3_locked"
    else:
        imagebutton auto "gallery_gui_images_images_main_image3_diana_%s":
            focus_mask True
            action Jump("gallery_gui_images_images_main_image3_diana")

screen in_gallery_gui_main_images_kat():
    key "mouseup_3" action [Hide("in_gallery_gui_main_images_kat"), SetVariable("in_gallery_gui_main_images", True), Show("scene_image_gallery")]
    key "K_ESCAPE" action [Hide("in_gallery_gui_main_images_kat"), SetVariable("in_gallery_gui_main_images", True), Show("scene_image_gallery")]

    add "gallery_gui_images_images_main"
    imagebutton auto "gallery_gui_main_images_back_%s":
        focus_mask True
        action [Hide("in_gallery_gui_main_images_kat"), SetVariable("in_gallery_gui_main_images", True), Show("scene_image_gallery")]

    if not persistent.kat_render1:
        add "gallery_gui_scene_box1_locked"
    else:
        imagebutton auto "gallery_gui_images_images_main_image1_kat_%s":
            focus_mask True
            action Jump("gallery_gui_images_images_main_image1_kat")

    if not persistent.kat_render2:
        add "gallery_gui_scene_box2_locked"
    else:
        imagebutton auto "gallery_gui_images_images_main_image2_kat_%s":
            focus_mask True
            action Jump("gallery_gui_images_images_main_image2_kat")
    
    if not persistent.kat_render3:
        add "gallery_gui_scene_box3_locked"
    else:
        imagebutton auto "gallery_gui_images_images_main_image3_kat_%s":
            focus_mask True
            action Jump("gallery_gui_images_images_main_image3_kat")

screen in_gallery_gui_main_images_nadia():
    key "mouseup_3" action [Hide("in_gallery_gui_main_images_nadia"), SetVariable("in_gallery_gui_main_images", True), Show("scene_image_gallery")]
    key "K_ESCAPE" action [Hide("in_gallery_gui_main_images_nadia"), SetVariable("in_gallery_gui_main_images", True), Show("scene_image_gallery")]

    add "gallery_gui_images_images_main"
    imagebutton auto "gallery_gui_main_images_back_%s":
        focus_mask True
        action [Hide("in_gallery_gui_main_images_nadia"), SetVariable("in_gallery_gui_main_images", True), Show("scene_image_gallery")]

    if not persistent.nadia_render1:
        add "gallery_gui_scene_box1_locked"
    else:
        imagebutton auto "gallery_gui_images_images_main_image1_nadia_%s":
            focus_mask True
            action Jump("gallery_gui_images_images_main_image1_nadia")

screen in_gallery_gui_main_images_yuuhi():
    key "mouseup_3" action [Hide("in_gallery_gui_main_images_yuuhi"), SetVariable("in_gallery_gui_main_images", True), Show("scene_image_gallery")]
    key "K_ESCAPE" action [Hide("in_gallery_gui_main_images_yuuhi"), SetVariable("in_gallery_gui_main_images", True), Show("scene_image_gallery")]

    add "gallery_gui_images_images_main"
    imagebutton auto "gallery_gui_main_images_back_%s":
        focus_mask True
        action [Hide("in_gallery_gui_main_images_yuuhi"), SetVariable("in_gallery_gui_main_images", True), Show("scene_image_gallery")]

    if not persistent.yuuhi_render1:
        add "gallery_gui_scene_box1_locked"
    else:
        imagebutton auto "gallery_gui_images_images_main_image1_yuuhi_%s":
            focus_mask True
            action Jump("gallery_gui_images_images_main_image1_yuuhi")

    if not persistent.yuuhi_render2:
        add "gallery_gui_scene_box2_locked"
    else:
        imagebutton auto "gallery_gui_images_images_main_image2_yuuhi_%s":
            focus_mask True
            action Jump("gallery_gui_images_images_main_image2_yuuhi")

screen in_gallery_gui_main_images_alex():
    key "mouseup_3" action [Hide("in_gallery_gui_main_images_alex"), SetVariable("in_gallery_gui_main_images", True), Show("scene_image_gallery")]
    key "K_ESCAPE" action [Hide("in_gallery_gui_main_images_alex"), SetVariable("in_gallery_gui_main_images", True), Show("scene_image_gallery")]

    add "gallery_gui_images_images_main"
    imagebutton auto "gallery_gui_main_images_back_%s":
        focus_mask True
        action [Hide("in_gallery_gui_main_images_alex"), SetVariable("in_gallery_gui_main_images", True), Show("scene_image_gallery")]

    if not persistent.alex_render1:
        add "gallery_gui_scene_box1_locked"
    else:
        imagebutton auto "gallery_gui_images_images_main_image1_alex_%s":
            focus_mask True
            action Jump("gallery_gui_images_images_main_image1_alex")

    if not persistent.alex_render2:
        add "gallery_gui_scene_box2_locked"
    else:
        imagebutton auto "gallery_gui_images_images_main_image2_alex_%s":
            focus_mask True
            action Jump("gallery_gui_images_images_main_image2_alex")

    if not persistent.alex_render3:
        add "gallery_gui_scene_box3_locked"
    else:
        imagebutton auto "gallery_gui_images_images_main_image3_alex_%s":
            focus_mask True
            action Jump("gallery_gui_images_images_main_image3_alex")

screen in_gallery_gui_main_images_mix():
    key "mouseup_3" action [Hide("in_gallery_gui_main_images_mix"), SetVariable("in_gallery_gui_main_images", True), Show("scene_image_gallery")]
    key "K_ESCAPE" action [Hide("in_gallery_gui_main_images_mix"), SetVariable("in_gallery_gui_main_images", True), Show("scene_image_gallery")]

    add "gallery_gui_images_images_main"
    imagebutton auto "gallery_gui_main_images_back_%s":
        focus_mask True
        action [Hide("in_gallery_gui_main_images_mix"), SetVariable("in_gallery_gui_main_images", True), Show("scene_image_gallery")]

    if not persistent.mix_render1:
        add "gallery_gui_scene_box1_locked"
    else:
        imagebutton auto "gallery_gui_images_images_main_image1_mix_%s":
            focus_mask True
            action Jump("gallery_gui_images_images_main_image1_mix")

    if not persistent.mix_render2:
        add "gallery_gui_scene_box2_locked"
    else:
        imagebutton auto "gallery_gui_images_images_main_image2_mix_%s":
            focus_mask True
            action Jump("gallery_gui_images_images_main_image2_mix")

    if not persistent.mix_render3:
        add "gallery_gui_scene_box3_locked"
    else:
        imagebutton auto "gallery_gui_images_images_main_image3_mix_%s":
            focus_mask True
            action Jump("gallery_gui_images_images_main_image3_mix")

    if not persistent.mix_render4:
        add "gallery_gui_scene_box4_locked"
    else:
        imagebutton auto "gallery_gui_images_images_main_image4_mix_%s":
            focus_mask True
            action Jump("gallery_gui_images_images_main_image4_mix")

screen scene_replay_quit():
    imagebutton auto "gallery_gui_main_images_back_%s":
        focus_mask True
        action Jump("scene_image_gallery")

label scene_image_gallery_back:
    call screen main_menu with dissolve

####################################GALLERY GUI IMAGES############################
label gallery_gui_main_images_maia:
    $ in_gallery_gui_main_images = False
    call screen in_gallery_gui_main_images_maia

label gallery_gui_main_images_reb:
    $ in_gallery_gui_main_images = False
    call screen in_gallery_gui_main_images_reb

label gallery_gui_main_images_diana:
    $ in_gallery_gui_main_images = False
    call screen in_gallery_gui_main_images_diana

label gallery_gui_main_images_kat:
    $ in_gallery_gui_main_images = False
    call screen in_gallery_gui_main_images_kat

label gallery_gui_main_images_nadia:
    $ in_gallery_gui_main_images = False
    call screen in_gallery_gui_main_images_nadia

label gallery_gui_main_images_yuuhi:
    $ in_gallery_gui_main_images = False
    call screen in_gallery_gui_main_images_yuuhi

label gallery_gui_main_images_alex:
    $ in_gallery_gui_main_images = False
    call screen in_gallery_gui_main_images_alex

label gallery_gui_main_images_mix:
    $ in_gallery_gui_main_images = False
    call screen in_gallery_gui_main_images_mix
####################################IMAGE1############################
screen view_image_maia1():
    key "mouseup_3" action [Hide("view_image_maia1"), Show("in_gallery_gui_main_images_maia")]
    key "K_ESCAPE" action [Hide("view_image_maia1"), Show("in_gallery_gui_main_images_maia")]
    
    add "maia_special_renders1"
    button:
        background None  
        action [Hide("view_image_maia1"), Show("in_gallery_gui_main_images_maia")]
        xysize (1.0, 1.0)

screen view_image_maia2():
    key "mouseup_3" action [Hide("view_image_maia2"), Show("in_gallery_gui_main_images_maia")]
    key "K_ESCAPE" action [Hide("view_image_maia2"), Show("in_gallery_gui_main_images_maia")]

    add "maia_special_renders2"
    button:
        background None  
        action [Hide("view_image_maia2"), Show("in_gallery_gui_main_images_maia")]
        xysize (1.0, 1.0)

label gallery_gui_images_images_main_image1_maia:
    call screen view_image_maia1
label gallery_gui_images_images_main_image2_maia:
    call screen view_image_maia2

screen view_image_reb1():
    key "mouseup_3" action [Hide("view_image_reb1"), Show("in_gallery_gui_main_images_reb")]
    key "K_ESCAPE" action [Hide("view_image_reb1"), Show("in_gallery_gui_main_images_reb")]

    add "reb_special_renders1"
    button:
        background None  
        action [Hide("view_image_reb1"), Show("in_gallery_gui_main_images_reb")]
        xysize (1.0, 1.0)

screen view_image_reb2():
    key "mouseup_3" action [Hide("view_image_reb2"), Show("in_gallery_gui_main_images_reb")]
    key "K_ESCAPE" action [Hide("view_image_reb2"), Show("in_gallery_gui_main_images_reb")]

    add "reb_special_renders2"
    button:
        background None  
        action [Hide("view_image_reb2"), Show("in_gallery_gui_main_images_reb")]
        xysize (1.0, 1.0)

screen view_image_reb3():
    key "mouseup_3" action [Hide("view_image_reb3"), Show("in_gallery_gui_main_images_reb")]
    key "K_ESCAPE" action [Hide("view_image_reb3"), Show("in_gallery_gui_main_images_reb")]

    add "reb_special_renders3"
    button:
        background None  
        action [Hide("view_image_reb3"), Show("in_gallery_gui_main_images_reb")]
        xysize (1.0, 1.0)

label gallery_gui_images_images_main_image1_reb:
    call screen view_image_reb1
label gallery_gui_images_images_main_image2_reb:
    call screen view_image_reb2
label gallery_gui_images_images_main_image3_reb:
    call screen view_image_reb3

screen view_image_diana1():
    key "mouseup_3" action [Hide("view_image_diana1"), Show("in_gallery_gui_main_images_diana")]
    key "K_ESCAPE" action [Hide("view_image_diana1"), Show("in_gallery_gui_main_images_diana")]

    add "diana_special_renders1"
    button:
        background None  
        action [Hide("view_image_diana1"), Show("in_gallery_gui_main_images_diana")]
        xysize (1.0, 1.0)

screen view_image_diana2():
    key "mouseup_3" action [Hide("view_image_diana2"), Show("in_gallery_gui_main_images_diana")]
    key "K_ESCAPE" action [Hide("view_image_diana2"), Show("in_gallery_gui_main_images_diana")]

    add "diana_special_renders2"
    button:
        background None  
        action [Hide("view_image_diana2"), Show("in_gallery_gui_main_images_diana")]
        xysize (1.0, 1.0)

screen view_image_diana3():
    key "mouseup_3" action [Hide("view_image_diana3"), Show("in_gallery_gui_main_images_diana")]
    key "K_ESCAPE" action [Hide("view_image_diana3"), Show("in_gallery_gui_main_images_diana")]

    add "diana_special_renders3"
    button:
        background None  
        action [Hide("view_image_diana3"), Show("in_gallery_gui_main_images_diana")]
        xysize (1.0, 1.0)

label gallery_gui_images_images_main_image1_diana:
    call screen view_image_diana1
label gallery_gui_images_images_main_image2_diana:
    call screen view_image_diana2
label gallery_gui_images_images_main_image3_diana:
    call screen view_image_diana3

screen view_image_kat1():
    key "mouseup_3" action [Hide("view_image_kat1"), Show("in_gallery_gui_main_images_kat")]
    key "K_ESCAPE" action [Hide("view_image_kat1"), Show("in_gallery_gui_main_images_kat")]

    add "kat_special_renders1"
    button:
        background None  
        action [Hide("view_image_kat1"), Show("in_gallery_gui_main_images_kat")]
        xysize (1.0, 1.0)

screen view_image_kat2():
    key "mouseup_3" action [Hide("view_image_kat2"), Show("in_gallery_gui_main_images_kat")]
    key "K_ESCAPE" action [Hide("view_image_kat2"), Show("in_gallery_gui_main_images_kat")]

    add "kat_special_renders2"
    button:
        background None  
        action [Hide("view_image_kat2"), Show("in_gallery_gui_main_images_kat")]
        xysize (1.0, 1.0)

screen view_image_kat3():
    key "mouseup_3" action [Hide("view_image_kat3"), Show("in_gallery_gui_main_images_kat")]
    key "K_ESCAPE" action [Hide("view_image_kat3"), Show("in_gallery_gui_main_images_kat")]

    add "kat_special_renders3"
    button:
        background None  
        action [Hide("view_image_kat3"), Show("in_gallery_gui_main_images_kat")]
        xysize (1.0, 1.0)
    
label gallery_gui_images_images_main_image1_kat:
    call screen view_image_kat1
label gallery_gui_images_images_main_image2_kat:
    call screen view_image_kat2
label gallery_gui_images_images_main_image3_kat:
    call screen view_image_kat3

screen view_image_nadia1():
    key "mouseup_3" action [Hide("view_image_nadia1"), Show("in_gallery_gui_main_images_nadia")]
    key "K_ESCAPE" action [Hide("view_image_nadia1"), Show("in_gallery_gui_main_images_nadia")]

    add "nadia_special_renders1"
    button:
        background None  
        action [Hide("view_image_nadia1"), Show("in_gallery_gui_main_images_nadia")]
        xysize (1.0, 1.0)

label gallery_gui_images_images_main_image1_nadia:
    call screen view_image_nadia1

screen view_image_yuuhi1():
    key "mouseup_3" action [Hide("view_image_yuuhi1"), Show("in_gallery_gui_main_images_yuuhi")]
    key "K_ESCAPE" action [Hide("view_image_yuuhi1"), Show("in_gallery_gui_main_images_yuuhi")]

    add "yuuhi_special_renders1"
    button:
        background None  
        action [Hide("view_image_yuuhi1"), Show("in_gallery_gui_main_images_yuuhi")]
        xysize (1.0, 1.0)

screen view_image_yuuhi2():
    key "mouseup_3" action [Hide("view_image_yuuhi2"), Show("in_gallery_gui_main_images_yuuhi")]
    key "K_ESCAPE" action [Hide("view_image_yuuhi2"), Show("in_gallery_gui_main_images_yuuhi")]

    add "yuuhi_special_renders2"
    button:
        background None  
        action [Hide("view_image_yuuhi2"), Show("in_gallery_gui_main_images_yuuhi")]
        xysize (1.0, 1.0)

label gallery_gui_images_images_main_image1_yuuhi:
    call screen view_image_yuuhi1
label gallery_gui_images_images_main_image2_yuuhi:
    call screen view_image_yuuhi2

screen view_image_alex1():
    key "mouseup_3" action [Hide("view_image_alex1"), Show("in_gallery_gui_main_images_alex")]
    key "K_ESCAPE" action [Hide("view_image_alex1"), Show("in_gallery_gui_main_images_alex")]

    add "alex_special_renders1"
    button:
        background None  
        action [Hide("view_image_alex1"), Show("in_gallery_gui_main_images_alex")]
        xysize (1.0, 1.0)

screen view_image_alex2():
    key "mouseup_3" action [Hide("view_image_alex2"), Show("in_gallery_gui_main_images_alex")]
    key "K_ESCAPE" action [Hide("view_image_alex2"), Show("in_gallery_gui_main_images_alex")]

    add "alex_special_renders2"
    button:
        background None  
        action [Hide("view_image_alex2"), Show("in_gallery_gui_main_images_alex")]
        xysize (1.0, 1.0)

screen view_image_alex3():
    key "mouseup_3" action [Hide("view_image_alex3"), Show("in_gallery_gui_main_images_alex")]
    key "K_ESCAPE" action [Hide("view_image_alex3"), Show("in_gallery_gui_main_images_alex")]

    add "alex_special_renders3"
    button:
        background None  
        action [Hide("view_image_alex3"), Show("in_gallery_gui_main_images_alex")]
        xysize (1.0, 1.0)

label gallery_gui_images_images_main_image1_alex:
    call screen view_image_alex1
label gallery_gui_images_images_main_image2_alex:
    call screen view_image_alex2
label gallery_gui_images_images_main_image3_alex:
    call screen view_image_alex3

screen view_image_mix1():
    key "mouseup_3" action [Hide("view_image_mix1"), Show("in_gallery_gui_main_images_mix")]
    key "K_ESCAPE" action [Hide("view_image_mix1"), Show("in_gallery_gui_main_images_mix")]

    add "mix_special_renders1"
    button:
        background None  
        action [Hide("view_image_mix1"), Show("in_gallery_gui_main_images_mix")]
        xysize (1.0, 1.0)

screen view_image_mix2():
    key "mouseup_3" action [Hide("view_image_mix2"), Show("in_gallery_gui_main_images_mix")]
    key "K_ESCAPE" action [Hide("view_image_mix2"), Show("in_gallery_gui_main_images_mix")]

    add "mix_special_renders2"
    button:
        background None  
        action [Hide("view_image_mix2"), Show("in_gallery_gui_main_images_mix")]
        xysize (1.0, 1.0)

screen view_image_mix3():
    key "mouseup_3" action [Hide("view_image_mix3"), Show("in_gallery_gui_main_images_mix")]
    key "K_ESCAPE" action [Hide("view_image_mix3"), Show("in_gallery_gui_main_images_mix")]

    add "mix_special_renders3"
    button:
        background None  
        action [Hide("view_image_mix3"), Show("in_gallery_gui_main_images_mix")]
        xysize (1.0, 1.0)

screen view_image_mix4():
    key "mouseup_3" action [Hide("view_image_mix4"), Show("in_gallery_gui_main_images_mix")]
    key "K_ESCAPE" action [Hide("view_image_mix4"), Show("in_gallery_gui_main_images_mix")]

    add "mix_special_renders4"
    button:
        background None  
        action [Hide("view_image_mix4"), Show("in_gallery_gui_main_images_mix")]
        xysize (1.0, 1.0)

label gallery_gui_images_images_main_image1_mix:
    call screen view_image_mix1
label gallery_gui_images_images_main_image2_mix:
    call screen view_image_mix2
label gallery_gui_images_images_main_image3_mix:
    call screen view_image_mix3
label gallery_gui_images_images_main_image4_mix:
    call screen view_image_mix4

label reset_variables:
    $ persistent.reb_render1 = False
    $ persistent.reb_render2 = False
    $ persistent.reb_render3 = False

    $ persistent.diana_render1 = False
    $ persistent.diana_render2 = False
    $ persistent.diana_render3 = False

    $ persistent.maia_render1 = False
    $ persistent.maia_render2 = False

    $ persistent.kat_render1 = False
    $ persistent.kat_render2 = False
    $ persistent.kat_render3 = False

    $ persistent.yuuhi_render1 = False
    $ persistent.yuuhi_render2 = False

    $ persistent.nadia_render1 = False

    $ persistent.alex_render1 = False
    $ persistent.alex_render2 = False

    $ persistent.mix_render1 = False
    $ persistent.mix_render2 = False
    $ persistent.mix_render4 = False

    #SCENES PAGE 1
    $ persistent.scene1_replay = False
    $ persistent.scene2_replay = False
    $ persistent.scene3_replay = False
    $ persistent.scene4_replay = False
    $ persistent.scene5_replay = False
    $ persistent.scene6_replay = False
    $ persistent.scene7_replay = False
    $ persistent.scene8_replay = False
    #SCENES PAGE 2
    $ persistent.scene1_p2_replay = False
    $ persistent.scene2_p2_replay = False
    $ persistent.scene3_p2_replay = False
    $ persistent.scene4_p2_replay = False
    $ persistent.scene5_p2_replay = False
    $ persistent.scene6_p2_replay = False
    $ persistent.scene7_p2_replay = False
    $ persistent.scene8_p2_replay = False
    #SCENES PAGE 3
    $ persistent.scene1_p3_replay = False
    $ persistent.scene2_p3_replay = False
    $ persistent.scene3_p3_replay = False
    $ persistent.scene4_p3_replay = False
    $ persistent.scene5_p3_replay = False
    $ persistent.scene6_p3_replay = False
    $ persistent.scene7_p3_replay = False
    $ persistent.scene8_p3_replay = False
    #SCENES PAGE 4
    $ persistent.scene1_p4_replay = False
    $ persistent.scene2_p4_replay = False
    $ persistent.scene3_p4_replay = False
    $ persistent.scene4_p4_replay = False
    $ persistent.scene5_p4_replay = False
    $ persistent.scene6_p4_replay = False
    $ persistent.scene7_p4_replay = False
    $ persistent.scene8_p4_replay = False
    #SCENES PAGE 5
    $ persistent.scene1_p5_replay = False
    $ persistent.scene2_p5_replay = False
    $ persistent.scene3_p5_replay = False
    $ persistent.scene4_p5_replay = False
    $ persistent.scene5_p5_replay = False
    $ persistent.scene6_p5_replay = False
    $ persistent.scene7_p5_replay = False
    $ persistent.scene8_p5_replay = False
    #SCENES PAGE6
    $ persistent.scene1_p6_replay = False
    $ persistent.scene2_p6_replay = False
    $ persistent.scene3_p6_replay = False 
    $ persistent.scene4_p6_replay = False 
    $ persistent.scene5_p6_replay = False 
    $ persistent.scene6_p6_replay = False 
    $ persistent.scene7_p6_replay = False 
    $ persistent.scene8_p6_replay = False 
    #SCENES PAGE7
    $ persistent.scene1_p7_replay = False 
    $ persistent.scene2_p7_replay = False 
    $ persistent.scene3_p7_replay = False 
    $ persistent.scene4_p7_replay = False
    
    #CHAPTER 5
    $ persistent.scene5_p7_replay = False 
    $ persistent.chapter5_p7_2_replay = False 
    $ persistent.chapter5_p7_3_replay = False 
    $ persistent.chapter5_p7_4_replay = False 
    $ persistent.chapter5_p7_5_replay = False 
    $ persistent.chapter5_p7_6_replay = False 
    $ persistent.chapter5_p7_7_replay = False 
    $ persistent.chapter5_p7_8_replay = False 
    
    $ reset_variables = False
    $ in_gallery_gui_main = True
    call screen scene_image_gallery with dissolve