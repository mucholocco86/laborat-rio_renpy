init 999:
    #default cheatcat = "CHEATS"
    default cheatcat4 = "CHEATS"
    default cheat_on4 = True
    default def_cheat4 = "cheats"
    default wt_unlocked_reward=False
    
    define mod_gr = "{color=#32BD73}"
    default mod_choices = ["","","","","","","","","",""]
    default persistent.mod_wtenabled=True
    default persistent.mod_wt_enabled=True
    default relationship_character = "maya"
    default variables_character ="warning"
    define unlockedScenes = 0
    define foundCards=0
    define unlockedScenes_s2=0
    define foundCards_s2=0
    default ep5_hots_bath_freeroam=False
    default cheat_envy_swyper=4
    define quick_menu = 2
    define loopMorningMusic=False
    define loopMusic = False
    define loopFightMusic = False
    define loopPartyMusic = False
    define loopMansionMusic = False
    default ep5_maya_path = False
    default ep5_josy_path = False
    default cheat_pp_money = False
    
    default wt_ep9_branch_numbers=1
    default wt_hh_girl_pick=" "
    default wt_ep9_end_pick=" "
    default wt_ep9_scenes=[]
    default ep9_wt_jm=False
    default branchAlone=False
    default branchIsabella=False
    default branchJill=False
    default branchMayaJosy=False
    default branchSage=False
    default jade_state=0
    default ep10_wt_end_bbq=" "
    default POS=""
    default wt_ep11_quinn_lilly=False
    default wt_ep11_maya_josy=False
    default wt_ep11_party_bella=False
    default wt_ep11_zoey_kiss_others=False
    default persistent.wt_collectible_notify=False
    default persistent.wt_collectible_circle=False
    default wt_ep11_quinn_riona_question=False
    default wt_ep11_quinn_riona_question_fix=False
    default wt_ep12_nora_cathy=False
    default wt_ep12_sandy_nicole=False
    default wt_ep12_quinn_nicole=False
    default persistent.no_cheater=False
    default wt_ep12_midnight_kiss=[]
    default wt_ep12_midnight_seen=[]
    default wt_ep12_maya_josy_seen=False
##################################################################################################
screen freeroam_help:
    
    hbox:
            
            xalign 0.9
            yalign 0

            if persistent.mod_wtenabled:
                textbutton "{b}HELP{/b}" action [Show("freeroam_wt_help"),Hide("freeroam_help")] text_size 25 text_color "#FFFFFF"

screen freeroam_wt_help:
  tag guide
  modal False
  frame:
    xsize 620
    ysize 800
    xalign 1.0
    yalign 0.01
    vpgrid:
       xfill True
       yfill True
       cols 1
       rows 10
       textbutton "Close" action [Hide("freeroam_wt_help"),Show("freeroam_help")] text_size 35 xpos(0.45)
       #####
       if freeRoamID == "ep10_5":
          if "ep10_tg_d_label" in event_list:
              text "   Check the office door upstairs"
          if "ep10_tg_helen_label" in event_list:
              text "   Talk to Derek and Helen downstairs"
          if "ep10_tg_d_label" not in event_list and "ep10_tg_helen_label" not in event_list and ("ep10_tg_mp_label" in event_list or "ep10_tg2_mp_label" in event_list):
              text "   Talk to Maya in the Kitchen"
          
          if "ep10_tg_dinner_label" in event_list:  
             text "   Go to the Dining room"
          if "ep10_tg_keys_label" in event_list:
            text "   Get keys from the garage"
          if "tg_part2" in event_list and "no_keys" not in event_list and "ep10_tg_keys_label" not in event_list:
            text "   Go to the office upstairs"
       if freeRoamID == "ep12_3c":
           if "START" in ep12_jewels:
               text "Go outside click the new arrow and then the door"
           if "ACTIVE" in ep12_jewels and "blue" not in ep12_jewels and "BLUE" not in ep12_jewels:
               text "Blue: Back side of Dining room under table to the left"
           if "ACTIVE" in ep12_jewels and "green" not in ep12_jewels and "GREEN" not in ep12_jewels:
               text "Green: Left side Balcony on top of a torch"
           if "ACTIVE" in ep12_jewels and "yellow" not in ep12_jewels and "YELLOW" not in ep12_jewels:
               text "Yellow: Right side locker room - middle locker on the left"
           if "ACTIVE" in ep12_jewels and "red" not in ep12_jewels and "RED" not in ep12_jewels:
               text "Red: Dance floor balcony - on the ground"
           if "ACTIVE" in ep12_jewels and "red" in ep12_jewels and "yellow" in ep12_jewels and "green" in ep12_jewels and "blue" in ep12_jewels:
                text "Go back to the door and place the jewels then open it"
            
#################################################################################################################
#init 10 python:
#    config.overlay_screens.append("cheats")
#    style.pref_button_text.ypadding = 0
    

define relationship_list = [
    "maya",
    "josy",
    "jill",
    "sage",
    "isabella",
    "derek",
    "preps",
    "diks",
    "jocks",
    "nerds",
    
]
define variables_char_list = [
    "maya",
    "josy",
    "jill",
    "sage",
    "isabella",
    "zoey",
    "quinn",
    "camila",
    "riona",
    #"mona",
    "melanie",
    "sarah",
    "heather",
    #"rose",
    "nicole",
    "lily",
    "jade",
    "cathy",
    "bianca",
    "nora",
    "sally",
    "elena",
    "derek",
    "other"
    
    
]
    
define cheat_cat = {
    "CHEATS":"tab_1",
    "RELATIONSHIPS":"tab_2",
    "VARIABLES":"tab_3",
    "OTHER":"tab_4"
}

style cheats_menu_text:
    color "#F0F0F0"
    hover_color "#E68231"
    font "Audrey-Bold.otf"
    size 36
    
style text_small_cheats:
    color "#F0F0F0"
    hover_color "E68231"
    font "Museo500.otf"
    size 29
    
style text_small_cheats2:
    color "#F0F0F0"
    hover_color "E68231"
    font "Museo500.otf"
    size 24
###########################################################

init 999:

  screen quick_menu():
    textbutton _("{b}CHEATS{/b}") action Show("cheat_menu") text_size 17 xalign 1.0 yalign 1.0
    textbutton _("{b}WELLS{/b}") action Show("quick_mod") text_size 17 xalign 1.0 yalign 1.0
    $mod_paths_count()

    zorder 100
    if not phone_opened:
        mousearea:
            area (0, 980, 720, 100)
            hovered SetVariable("quick_menu_hovered", True)
            unhovered SetVariable("quick_menu_hovered", False)
        if persistent.quick_menu > 0 and quick_menu > 0:
            if (quick_menu_hovered and persistent.quick_menu == 1) or (persistent.quick_menu == 2):

                hbox:
                    style_prefix "quick"
                    xalign 0.0
                    yalign 1.0

                    if persistent.qm_back:
                        textbutton _("Back") action Rollback() text_style "quick_btn_style"
                    if persistent.qm_history:
                        textbutton _("History") action ShowMenu('history') text_style "quick_btn_style"
                    if persistent.qm_skip:
                        textbutton _("Skip") action Skip() text_style "quick_btn_style"
                    if persistent.qm_auto:
                        textbutton _("Auto") action Preference("auto-forward", "toggle") text_style "quick_btn_style"
                    if persistent.qm_save:
                        textbutton _("Save") action ShowMenu('save') text_style "quick_btn_style"
                    if persistent.qm_qsave:
                        textbutton _("Q.Save") action QuickSave() text_style "quick_btn_style"
                    if persistent.qm_qload:
                        textbutton _("Q.Load") action (SetVariable("persistent.current_save_name",FileSaveName(1, page="quick")),QuickLoad()) text_style "quick_btn_style"

                    if persistent.qm_prefs:
                        textbutton _("Prefs") action ShowMenu('preferences') text_style "quick_btn_style"
                    if persistent.qm_guide and (steamConfig or nonPatreonConfig) and renpy.loadable("walkthrough/season3/walkthrough_season3.rpyc"):
                        textbutton _("Guide") action (SetVariable("tmpMenu2", quick_menu), SetVariable("quick_menu", 0),Function(show_guide_func)) text_style "quick_btn_style"


  
###############################################################################################
    
init 1:
    
    screen cheats:
        zorder 100
        hbox:
            style_prefix "quick"
            xalign 1.0
            yalign 1.0


            textbutton _("{b}CHEATS{/b}") action Show("cheat_menu") text_size 17
    screen cheat_menu:
        modal True
        #$mod_paths_count()
        if cheat_on4 == True:
            add "cheats/%s.png" % cheat_cat[cheatcat4]
            hbox:
                xpos 70
                ypos 55
                textbutton "Cheats" action SetVariable("cheatcat4", "CHEATS") text_style "cheats_menu_text"
            hbox:
                xpos 340
                ypos 55
                textbutton "Relationships" action SetVariable("cheatcat4", "RELATIONSHIPS") text_style "cheats_menu_text"
            hbox:
                xpos 600
                ypos 55
                textbutton "Variables" action SetVariable("cheatcat4", "VARIABLES") text_style "cheats_menu_text"
            hbox:
                xpos 860
                ypos 55
                textbutton "Other" action SetVariable("cheatcat4", "OTHER") text_style "cheats_menu_text"
            vbox:
                xpos 85
                ypos 900
                textbutton "Close" action [Hide("cheat_menu")] text_style "cheats_menu_text"
######################################################################    
            if cheatcat4 == "CHEATS":
                
                frame:
                    xpos 340
                    ypos 150
                    xmaximum 1500
                    ymaximum 800
                    background None
                    viewport:
                        draggable True
                        mousewheel True
                        vbox:
                            xpos 0
                            ypos 0
                            spacing 10
                            hbox xpos 0 ypos 0:
                                 frame xpos 0 ypos 0 background None:
                                     vbox xpos 0 ypos 0 spacing 5:
                                        textbutton "        {color=#F0F0F0}DIK SCORE"  text_style "text_small_cheats" action NullAction()
                                        
                                        if dtype == -1:
                                            textbutton "            {color=#F0F0F0}Chick"  text_style "text_small_cheats" action NullAction()
                                        elif dtype == -2:
                                            textbutton "        {color=#F0F0F0}Huge Chick"  text_style "text_small_cheats" action NullAction()
                                        elif dtype == -3:
                                            textbutton "       {color=#F0F0F0}Massive Chick"  text_style "text_small_cheats" action NullAction()
                                        elif dtype == 1:
                                            textbutton "              {color=#F0F0F0}DIK"  text_style "text_small_cheats" action NullAction()
                                        elif dtype == 2:
                                            textbutton "       {color=#F0F0F0}Huge DIK"  text_style "text_small_cheats" action NullAction()
                                        elif dtype == 3:
                                            textbutton "       {color=#F0F0F0}Massive DIK"  text_style "text_small_cheats" action NullAction()
                                        elif dtype == 0:
                                            textbutton "            {color=#F0F0F0}Neutral"  text_style "text_small_cheats" action NullAction()
                                        if dik >= 15:
                                            $dtype=3
                                        elif dik >=10:
                                             $dtype = 2
                                        elif dik >= 5:
                                            $dtype = 1
                                        elif dik < 5 and dik > -5:
                                            $dtype = 0
                                        elif dik <=-15:
                                            $dtype = -3
                                        elif dik <=-10:
                                            $dtype = -2
                                        elif dik <=-5:
                                            $dtype = -1
                                            
                                        bar value VariableValue("dik",40,offset=-20) bar_invert True:
                                            xmaximum 300
                                            ymaximum 5
                                            left_bar Frame("gui/bar/left.png", 10, 0)
                                            right_bar Frame("gui/bar/right.png", 10, 0)
                                            left_gutter 0
                                            right_gutter 0
                                        vbox xpos 120 ypos -38 spacing 41:
                                            text "{=bar_text} [dik]"
                                        $updateDikScore_m()
                                        $calcRenders()
                                        $calcScenes()
                                        $calcWallpapers()
                                        #$mod_paths_count()
                                      #############################################################  
                                     vbox xpos 0 ypos 220 spacing 5:
                                        textbutton "{color=#F0F0F0}Current Affinity: [affinity]"  text_style "text_small_cheats" action NullAction()
                                     if affinity == "DIK":
                                         vbox xpos 410 ypos 220 spacing 5:
                                            textbutton "NEUTRAL"   action SetVariable ("affinity","NEUTRAL") text_style "text_small_cheats"
                                         vbox xpos 575 ypos 220 spacing 5:
                                            textbutton "CHICK"  text_style "text_small_cheats" action SetVariable ("affinity","CHICK")
                                     
                                     elif affinity == "CHICK":
                                         vbox xpos 410 ypos 220 spacing 5:
                                            textbutton "NEUTRAL"  text_style "text_small_cheats" action SetVariable ("affinity","NEUTRAL") text_hover_color "#E68231"
                                         vbox xpos 575 ypos 220 spacing 5:
                                            textbutton "DIK"  text_style "text_small_cheats" action SetVariable ("affinity","DIK") text_hover_color "#E68231"
                                     
                                     elif affinity == "NEUTRAL":
                                         vbox xpos 410 ypos 220 spacing 5:
                                            textbutton "DIK"  text_style "text_small_cheats" action SetVariable ("affinity","DIK") text_hover_color "E68231"
                                         vbox xpos 575 ypos 220 spacing 5:
                                            textbutton "CHICK"  text_style "text_small_cheats" action SetVariable ("affinity","CHICK") text_hover_color "E68231"
                                     #############################################3
                                     #vbox xpos 0 ypos 300 spacing 5:
                                      #if bonusPointsSports != 12:
                                       # textbutton "Brawler max Skillpoints"  action SetVariable("bonusPointsSports",12) text_style "text_small_cheats"
                                      #elif bonusPointsSports == 12:
                                       # textbutton "{color=#F0F0F0}Brawler Points Maxed"  text_style "text_small_cheats" action NullAction()
                                     #vbox xpos 350 ypos 300 spacing 5:
                                      #   textbutton "Brawler Player HP to 100"  text_style "text_small_cheats" action SetVariable("sports_pc_hp",100)
                                     #vbox xpos 750 ypos 300 spacing 5:
                                      #   textbutton "Brawler Opponent HP to 1"  text_style "text_small_cheats" action SetVariable ("sports_cpu_hp",1)
                                     ###############################################################
                                     vbox xpos 0 ypos 380 spacing 5:
                                        textbutton "{color=#F0F0F0}Current Money: [money]"  text_style "text_small_cheats" action NullAction()
                                     
                                     vbox xpos 330 ypos 380 spacing 5:
                                            textbutton "MAX Money"   action Function(cheat_money,c_money=10) text_style "text_small_cheats"
                                     vbox xpos 550 ypos 380 spacing 5:
                                            textbutton "No Money"  text_style "text_small_cheats" action Function(cheat_money,c_money=-10)
    #########################################################################################################################################################
                                     vbox xpos 0 ypos 460 spacing 5:
                                      if unlockedScenes == persistent.totalScenes and persistent.totalScenes_s2 > 0 and unlockedScenes_s2 == persistent.totalScenes_s2:
                                        textbutton "{color=#F0F0F0}All scenes Unlocked"  text_style "text_small_cheats" action NullAction()
                                      else: 
                                        textbutton "Unlock all Scenes"  text_style "text_small_cheats" action Function(scene_unlock)
                                     vbox xpos 0 ypos 520 spacing 5:
                                      if wt_unlocked_reward:
                                        textbutton "{color=#F0F0F0}All rewards Unlocked"  text_style "text_small_cheats" action NullAction()
                                      else: 
                                        textbutton "Unlock all rewards"  text_style "text_small_cheats" action Function(reward_unlock)
                                        
                                     if currentEpisode >= 9:
                                         vbox xpos 450 ypos 50 spacing 5:
                                          textbutton "{color=#F0F0F0}Party planning money: [pp_money]"  text_style "text_small_cheats" action NullAction()
                                         vbox xpos 850 ypos 50 spacing 5:
                                          textbutton "+Money"  text_style "text_small_cheats" action SetVariable ("pp_money",pp_money+10)
                                         vbox xpos 980 ypos 50 spacing 5:
                                          textbutton "-Money"  text_style "text_small_cheats" action SetVariable ("pp_money",pp_money-10)
                                     if currentEpisode >= 11:
                                         vbox xpos 450 ypos 110 spacing 5:
                                          textbutton "{color=#F0F0F0}Cheater Points: [tc]"  text_style "text_small_cheats" action NullAction()
                                         vbox xpos 850 ypos 110 spacing 5:
                                          textbutton "+1"  text_style "text_small_cheats" action SetVariable ("tc",tc+1)
                                         vbox xpos 980 ypos 110 spacing 5:
                                          textbutton "-1"  text_style "text_small_cheats" action SetVariable ("tc",tc-1)
                                     vbox xpos 720 ypos 220 spacing 5:      
                                        textbutton "{color=#F0F0F0}Permanent Affinity: "  text_style "text_small_cheats" action NullAction()
                                     vbox xpos 1000 ypos 220 spacing 5:
                                         if permanent_affinity:
                                            textbutton "Yes"  text_style "text_small_cheats" action SetVariable ("permanent_affinity",False) text_hover_color "E68231"    
                                         else:
                                            textbutton "No"  text_style "text_small_cheats" action SetVariable ("permanent_affinity",True) text_hover_color "E68231"  
                                      #
                                     
            elif cheatcat4 == "RELATIONSHIPS":
                vbox:
                    spacing -20
                    xpos 85
                    ypos 150
                    for i in relationship_list:
                            textbutton "%s" % i.capitalize() action SetVariable("relationship_character","%s" % i) text_style "cheats_menu_text"
                            
                vbox xpos 340 ypos 150:
                    add im.MatrixColor(im.FactorScale("cheats/%s.jpg" % relationship_character,0.78125,0.74),im.matrix.opacity(0.4))
                            
                frame xpos 360 ypos 150 background None:
                    vbox xpos 0 ypos 450 spacing 5:
                        if relationship_character == "maya":
                            text "     Relationship"
                            bar value VariableValue("RP%s" % relationship_character,55,offset=-5):
                                xmaximum 300
                                ymaximum 5
                                left_bar Frame("gui/bar/left.png", 10, 0)
                                right_bar Frame("gui/bar/right.png", 10, 0)
                                left_gutter 0
                                right_gutter 0
                            vbox xpos 120 ypos -38 spacing 41:
                               text "{=bar_text} [RP%s]" % relationship_character
                               
                        
                        if relationship_character == "josy":
                            text "     Relationship"
                            bar value VariableValue("RP%s" % relationship_character,48,offset=-2):
                                xmaximum 300
                                ymaximum 5
                                left_bar Frame("gui/bar/left.png", 10, 0)
                                right_bar Frame("gui/bar/right.png", 10, 0)
                                left_gutter 0
                                right_gutter 0
                            vbox xpos 120 ypos -38 spacing 41:
                               text "{=bar_text} [RP%s]" % relationship_character
                        if relationship_character == "sage":
                            text "     Relationship"
                            bar value VariableValue("RP%s" % relationship_character,44,offset=-7):
                                xmaximum 300
                                ymaximum 5
                                left_bar Frame("gui/bar/left.png", 10, 0)
                                right_bar Frame("gui/bar/right.png", 10, 0)
                                left_gutter 0
                                right_gutter 0
                            vbox xpos 120 ypos -38 spacing 41:
                               text "{=bar_text} [RP%s]" % relationship_character
                               
                        if relationship_character == "isabella":
                            text "     Relationship"
                            bar value VariableValue("RP%s" % relationship_character,40,offset=-9):
                                xmaximum 300
                                ymaximum 5
                                left_bar Frame("gui/bar/left.png", 10, 0)
                                right_bar Frame("gui/bar/right.png", 10, 0)
                                left_gutter 0
                                right_gutter 0
                            vbox xpos 120 ypos -38 spacing 41:
                               text "{=bar_text} [RP%s]" % relationship_character
                               
                        if relationship_character == "jill":
                            text "     Relationship"
                            bar value VariableValue("RP%s" % relationship_character,45,offset=-5):
                                xmaximum 300
                                ymaximum 5
                                left_bar Frame("gui/bar/left.png", 10, 0)
                                right_bar Frame("gui/bar/right.png", 10, 0)
                                left_gutter 0
                                right_gutter 0
                            vbox xpos 120 ypos -38 spacing 41:
                               text "{=bar_text} [RP%s]" % relationship_character
                               
                        if relationship_character == "derek":
                            text "     Relationship"
                            bar value VariableValue("RP%s" % relationship_character,18,offset=-2):
                                xmaximum 300
                                ymaximum 5
                                left_bar Frame("gui/bar/left.png", 10, 0)
                                right_bar Frame("gui/bar/right.png", 10, 0)
                                left_gutter 0
                                right_gutter 0
                            vbox xpos 120 ypos -38 spacing 41:
                               text "{=bar_text} [RP%s]" % relationship_character
                        if relationship_character == "diks":
                            text "     Relationship"
                            bar value VariableValue("RP%s" % relationship_character,25,offset=-2):
                                xmaximum 300
                                ymaximum 5
                                left_bar Frame("gui/bar/left.png", 10, 0)
                                right_bar Frame("gui/bar/right.png", 10, 0)
                                left_gutter 0
                                right_gutter 0
                            vbox xpos 120 ypos -38 spacing 41:
                               text "{=bar_text} [RP%s]" % relationship_character
                               
                        if relationship_character == "jocks":
                            text "     Relationship"
                            bar value VariableValue("RP%s" % relationship_character,3,offset=-3):
                                xmaximum 300
                                ymaximum 5
                                left_bar Frame("gui/bar/left.png", 10, 0)
                                right_bar Frame("gui/bar/right.png", 10, 0)
                                left_gutter 0
                                right_gutter 0
                            vbox xpos 120 ypos -38 spacing 41:
                               text "{=bar_text} [RP%s]" % relationship_character
                               
                        if relationship_character == "nerds":
                            text "     Relationship"
                            bar value VariableValue("RP%s" % relationship_character,2,offset=-1):
                                xmaximum 300
                                ymaximum 5
                                left_bar Frame("gui/bar/left.png", 10, 0)
                                right_bar Frame("gui/bar/right.png", 10, 0)
                                left_gutter 0
                                right_gutter 0
                            vbox xpos 120 ypos -38 spacing 41:
                               text "{=bar_text} [RP%s]" % relationship_character
                        if relationship_character == "preps":
                            text "     Relationship"
                            bar value VariableValue("RP%s" % relationship_character,2,offset=-2):
                                xmaximum 300
                                ymaximum 5
                                left_bar Frame("gui/bar/left.png", 10, 0)
                                right_bar Frame("gui/bar/right.png", 10, 0)
                                left_gutter 0
                                right_gutter 0
                            vbox xpos 120 ypos -38 spacing 41:
                               text "{=bar_text} [RP%s]" % relationship_character
                        
            elif cheatcat4 == "VARIABLES":
                vbox:
                    spacing -20
                    xpos 85
                    ypos 150
                    for i in variables_char_list:
                            textbutton "%s" % i.capitalize() action SetVariable("variables_character","%s" % i) text_style "text_small_cheats" text_size 30
                            
                vbox xpos 340 ypos 150:
                  if variables_character != "warning" and variables_character != "other":
                    add im.MatrixColor(im.FactorScale("cheats/%s.jpg" % variables_character,0.78125,0.74),im.matrix.opacity(0.4)) 
                frame xpos 360 ypos 150 background None:
                    vbox xpos 0 ypos 0 spacing 5:
                        if variables_character == "warning":
                            textbutton "{color=#F0F0F0}Here you can change some 'important' variables/decisions from the game,\nBut changing some of them may break something\n\nMore Variables will become visible as you progress through the game           \n\nTo Change the variables just click on them"  text_style "cheats_menu_text" action NullAction()
                        ##################################################################
                        elif variables_character == "bianca":
                            vbox xpos 0 ypos 0 spacing 5:
                              if currentEpisode >= 12:
                                if ep11_bianca_path:
                                    textbutton "EP12 Bianca path active"  text_style "text_small_cheats" action SetVariable("ep11_bianca_path",False)
                                else:
                                    textbutton "EP12 Bianca path not active"  text_style "text_small_cheats" action SetVariable("ep11_bianca_path",True)
                        ###################################################################
                        elif variables_character == "zoey":
                            vbox xpos 0 ypos 0 spacing 5:
                              if currentEpisode >= 12:
                                if branchZoey and roadZoey:
                                    textbutton "EP12 Zoey branch active"  text_style "text_small_cheats" action [SetVariable("branchZoey",False),SetVariable("roadZoey",False)]
                                    
                                    if wt_ep11_zoey_kiss_others:
                                        textbutton "     EP12 Zoey branch and won't block other paths"  text_style "text_small_cheats" action SetVariable("wt_ep11_zoey_kiss_others",False)
                                    else:
                                        textbutton "      EP12 Zoey branch and will block other paths (unmodded behavior)"  text_style "text_small_cheats" action SetVariable("wt_ep11_zoey_kiss_others",True)
                                else:
                                    textbutton "EP12 Zoey branch not active"  text_style "text_small_cheats" action [SetVariable("branchZoey",True),SetVariable("roadZoey",True)]
                                    if ep12_zoey_friend:
                                        textbutton "EP12 stayed friends with Zoey"  text_style "text_small_cheats" action SetVariable("ep12_zoey_friend",False)
                                    else:
                                        textbutton "EP12 didn't stay friends with Zoey"  text_style "text_small_cheats" action SetVariable("ep12_zoey_friend",True)                                     
                                                                         
                        ###################################################################
                        
                        elif variables_character == "elena":
                            vbox xpos 0 ypos 0 spacing 5:
                              if currentEpisode >= 12:
                                if ep11_elena_lewd:
                                    textbutton "EP11 Lewd scene with Elena"  text_style "text_small_cheats" action SetVariable("ep11_elena_lewd",False)
                                else:
                                    textbutton "EP11 No Lewd scene with Elena"  text_style "text_small_cheats" action SetVariable("ep11_elena_lewd",True)
                        ################################################################################
                        elif variables_character == "nicole":
                            vbox xpos 0 ypos 0 spacing 5:
                              if currentEpisode >= 9:
                                if ep3_envyLewd == 2 or ep3_envyLewd == 1:
                                    textbutton "EP3 Had Sex with Envy"  text_style "text_small_cheats" action SetVariable("ep3_envyLewd",0)
                                elif ep3_envyLewd == 0:
                                    textbutton "EP3 Didn't Have Sex with Envy"  text_style "text_small_cheats" action SetVariable("ep3_envyLewd",2)
                              
                                 
                              if currentEpisode >= 6: 
                                  if envyLikesYou:
                                    textbutton "EP6 Nicole likes you"  text_style "text_small_cheats" action SetVariable("envyLikesYou",False)
                                  elif envyLikesYou == False:
                                    textbutton "EP6 Nicole doesn't like you"  text_style "text_small_cheats" action SetVariable("envyLikesYou",True)
                              if currentEpisode >=7:
                                  if ep6_envy_lewd    :
                                    textbutton "EP6 Nicole,Sandy Sex"  text_style "text_small_cheats" action SetVariable("ep6_envy_lewd",False)
                                  elif ep6_envy_lewd     == False:
                                    textbutton "EP6 no Nicole,Sandy Sex"  text_style "text_small_cheats" action SetVariable("ep6_envy_lewd",True)
                              if currentEpisode >= 10:
                                  if ep10_date_nicole    :
                                    textbutton "EP10 dating Nicole"  text_style "text_small_cheats" action SetVariable("ep10_date_nicole",False)
                                  elif ep10_date_nicole    == False:
                                    textbutton "EP10 not dating Nicole"  text_style "text_small_cheats" action SetVariable("ep10_date_nicole",True)
                                  if currentEpisode >= 12:
                                      if ep11_nicole_dating    :
                                        textbutton "EP11 dating Nicole"  text_style "text_small_cheats" action SetVariable("ep11_nicole_dating",False)
                                      elif ep11_nicole_dating    == False:
                                        textbutton "EP11 not dating Nicole"  text_style "text_small_cheats" action SetVariable("ep11_nicole_dating",True)
                                  
                                      if ep12_nicole_path   :
                                        textbutton "EP12 Nicole path active"  text_style "text_small_cheats" action SetVariable("ep12_nicole_path",False)
                                      elif ep12_nicole_path    == False:
                                        textbutton "EP12 Nicole path not active"  text_style "text_small_cheats" action SetVariable("ep12_nicole_path",True)
                                                            
                                    
                                
                              
                        ######################################################################
                        #elif variables_character == "dawe":
                         #   vbox xpos 0 ypos 0 spacing 5:
                          #    if currentEpisode >= 2:
                           #     if ep2_dawe_fight_won:
                            #        textbutton "EP2 Beat up Dawe"  text_style "text_small_cheats" action SetVariable("ep2_dawe_fight_won",False)
                             #   elif ep2_dawe_fight_won == False:
                              #      textbutton "EP2 Didn't Beat up Dawe"  text_style "text_small_cheats" action SetVariable("ep2_dawe_fight_won",True)
                     ################################################################################
                        elif variables_character == "derek":  ###ep4_derekFuckedArieth
                            vbox xpos 0 ypos 0 spacing 5:
                                if currentEpisode >= 9:
                                 if ep3_choseBella==False and ep3_choseDerek==False and ep3_choseSage==False:
                                    $ep3_choseDerek=True
                                 if ep3_choseDerek:
                                     textbutton "EP4 Stayed with Derek"  text_style "text_small_cheats" action [SetVariable("ep3_choseBella",True),SetVariable("ep3_choseDerek",False)]
                                 elif ep3_choseBella:
                                     textbutton "EP4 Stayed with Isabella"  text_style "text_small_cheats" action [SetVariable("ep3_choseSage",True),SetVariable("ep3_choseBella",False)]
                                 elif ep3_choseSage:
                                     textbutton "EP4 Stayed with Sage"  text_style "text_small_cheats" action [SetVariable("ep3_choseDerek",True),SetVariable("ep3_choseSage",False)]
#############################################################################################################
                        elif variables_character == "heather":
                            vbox xpos 0 ypos 0 spacing 5:
                              if currentEpisode >= 10:
                                  if ep9_heather_lewd == 2:
                                    textbutton "EP9 got blowjob from Heather"  text_style "text_small_cheats" action SetVariable("ep9_heather_lewd",0)
                                  else:
                                    textbutton "EP9 no blowjob from Heather"  text_style "text_small_cheats" action SetVariable("ep9_heather_lewd",2)
############################################################################################################
                        elif variables_character == "melanie":
                            vbox xpos 0 ypos 0 spacing 5:
                              if currentEpisode >= 9:
                                  if ep4_fuckedMelanie:
                                    textbutton "EP4 sex with Melanie"  text_style "text_small_cheats" action SetVariable("ep4_fuckedMelanie",False)
                                  elif ep4_fuckedMelanie == False:
                                    textbutton "EP4 no sex with Melanie"  text_style "text_small_cheats" action SetVariable("ep4_fuckedMelanie",True)
                              if currentEpisode >= 9:
                                 if ep5_hot_lewd:
                                    textbutton "EP5 Sarah/Melanie BJ"  text_style "text_small_cheats" action SetVariable("ep5_hot_lewd",False)
                                 elif ep5_hot_lewd == False:
                                    textbutton "EP5 no Sarah/Melanie BJ"  text_style "text_small_cheats" action SetVariable("ep5_hot_lewd",True)
                              if currentEpisode >= 11:
                                 if ep11_mel_lewd:
                                    textbutton "EP11 Melanie sex"  text_style "text_small_cheats" action SetVariable("ep11_mel_lewd",False)
                                 elif ep11_mel_lewd == False:
                                    textbutton "EP11 no Melanie sex"  text_style "text_small_cheats" action SetVariable("ep11_mel_lewd",True)
                                
                                 
###########################################################################################################
                        
                        elif variables_character == "sarah":
                            vbox xpos 0 ypos 0 spacing 5:
                              if currentEpisode >= 9:
                                  if ep2_fuckHOT:
                                    textbutton "EP2 had sex at DIK party"  text_style "text_small_cheats" action SetVariable("ep2_fuckHOT",False)
                                  elif ep2_fuckHOT == False:
                                    textbutton "EP2 didn't have sex at DIK party"  text_style "text_small_cheats" action SetVariable("ep2_fuckHOT",True)
                              if currentEpisode >= 9:
                                  if ep4_hottest_ass == "Sarah":
                                     textbutton "EP4 said Sarah has best ass"  text_style "text_small_cheats" action SetVariable("ep4_hottest_ass","Riona")
                                  elif ep4_hottest_ass == "Riona":
                                     textbutton "EP4 said Riona has best ass"  text_style "text_small_cheats" action SetVariable("ep4_hottest_ass","Camila")
                                  elif ep4_hottest_ass == "Camila":
                                     textbutton "EP4 said Camila has best ass"  text_style "text_small_cheats" action SetVariable("ep4_hottest_ass","Sarah")
                                  elif ep4_hottest_ass != "Camila" and ep4_hottest_ass != "Riona" and ep4_hottest_ass != "Sarah":
                                     textbutton "EP4 said some other has best ass"  text_style "text_small_cheats" action SetVariable("ep4_hottest_ass","Sarah")                              
                              
                              
                              if currentEpisode >= 9:
                                 if ep5_hot_lewd:
                                    textbutton "EP5 Sarah/Melanie BJ"  text_style "text_small_cheats" action SetVariable("ep5_hot_lewd",False)
                                 elif ep5_hot_lewd == False:
                                    textbutton "EP5 no Sarah/Melanie BJ"  text_style "text_small_cheats" action SetVariable("ep5_hot_lewd",True)
                              if currentEpisode >= 11:
                                 if ep11_sarah_lewd:
                                    textbutton "EP11 Sarah sex"  text_style "text_small_cheats" action SetVariable("ep11_sarah_lewd",False)
                                 elif ep11_sarah_lewd == False:
                                    textbutton "EP11 no Sarah sex"  text_style "text_small_cheats" action SetVariable("ep11_sarah_lewd",True)
                                    
            

                 ##################################################################################################  
                        elif variables_character == "sally":
                            vbox xpos 0 ypos 0 spacing 5:
                                if currentEpisode >= 11:
                                   if ep11_sally_kiss:
                                        textbutton "EP11 kissed Sally"  text_style "text_small_cheats" action SetVariable("ep11_sally_kiss",False)
                                   else:
                                        textbutton "EP11 didn't kiss Sally"  text_style "text_small_cheats" action SetVariable("ep11_sally_kiss",True)
                 ###################################################################################################
                 
                        elif variables_character == "nora":
                            vbox xpos 0 ypos 0 spacing 5:
                                if currentEpisode >= 10:
                                   if ep10_dating_nora:
                                        textbutton "EP10 dating Nora"  text_style "text_small_cheats" action SetVariable("ep10_dating_nora",False)
                                   else:
                                        textbutton "EP10 not dating Nora"  text_style "text_small_cheats" action SetVariable("ep10_dating_nora",True)
                                   if currentEpisode >= 11:
                                       if ep10_nora_encourage and ep10_nora_kids: #ep10_nora_encourage and ep10_nora_kids
                                            textbutton "EP11 keep dating Nora"  text_style "text_small_cheats" action [SetVariable("ep10_nora_encourage",False),SetVariable("ep10_nora_kids",False)]
                                       else:
                                            textbutton "EP11 didn't keep dating Nora"  text_style "text_small_cheats" action [SetVariable("ep10_nora_encourage",True),SetVariable("ep10_nora_kids",True)]
                        
                ####################################################################################################
                        elif variables_character == "isabella":
                            vbox xpos 0 ypos 0 spacing 5:
                              
                              #if currentEpisode >= 9:
                                  #if ep3_bella_came_around:
                                  #  textbutton "EP3 Isabella likes you"  text_style "text_small_cheats" action SetVariable("ep3_bella_came_around",False)
                                  #elif ep3_bella_came_around == False:
                                  #  textbutton "EP3 doesn't like you"  text_style "text_small_cheats" action SetVariable("ep3_bella_came_around",True)
                                    
                                  #if ep3_BellaLewd:
                                  #  textbutton "EP3 kissed at library"  text_style "text_small_cheats" action SetVariable("ep3_BellaLewd",False)
                                  #elif ep3_BellaLewd == False:
                                  #  textbutton "EP3 didn't kiss at library"  text_style "text_small_cheats" action SetVariable("ep3_BellaLewd",True)
                                  
                              if currentEpisode >= 9:
                                 if ep3_choseBella==False and ep3_choseDerek==False and ep3_choseSage==False:
                                    $ep3_choseDerek=True
                                 if ep3_choseDerek:
                                     textbutton "EP4 Stayed with Derek"  text_style "text_small_cheats" action [SetVariable("ep3_choseBella",True),SetVariable("ep3_choseDerek",False)]
                                 elif ep3_choseBella:
                                     textbutton "EP4 Stayed with Isabella"  text_style "text_small_cheats" action [SetVariable("ep3_choseSage",True),SetVariable("ep3_choseBella",False)]
                                 elif ep3_choseSage:
                                     textbutton "EP4 Stayed with Sage"  text_style "text_small_cheats" action [SetVariable("ep3_choseDerek",True),SetVariable("ep3_choseSage",False)]
                                                            
                              if currentEpisode >= 9:
                                  if ep4_bella_lewd:
                                    textbutton "EP4 Isabella lewd scene"  text_style "text_small_cheats" action SetVariable("ep4_bella_lewd",False)
                                  elif ep4_bella_lewd == False:
                                    textbutton "EP4 no Isabella lewd scene"  text_style "text_small_cheats" action SetVariable("ep4_bella_lewd",True)
                              if currentEpisode >= 9:
                                 if ep5_bella_lewd:
                                    textbutton "EP5 Isabella Sauna scene"  text_style "text_small_cheats" action SetVariable("ep5_bella_lewd",False)
                                 elif ep5_bella_lewd == False:
                                    textbutton "EP5 no Isabella Sauna scene"  text_style "text_small_cheats" action SetVariable("ep5_bella_lewd",True)
                                 #if pathIsabella:
                                 #   textbutton "Isabella path: Active"  text_style "text_small_cheats" action SetVariable("pathIsabella",False)
                                 #elif pathIsabella  == False:
                                 #   textbutton "Isabella path: Disabled"  text_style "text_small_cheats" action SetVariable("pathIsabella",True)
                              if currentEpisode >= 9:
                                 #if ep7_bella_rejected_you:
                                 #    textbutton "Isabella rejected you"  text_style "text_small_cheats" action SetVariable("ep7_bella_rejected_you",False)
                                 #else:
                                     #textbutton "Isabella didn't reject you"  text_style "text_small_cheats" action SetVariable("ep7_bella_rejected_you",True)
                                 if ep7_bella_lewd:
                                      textbutton "EP7 Isabella lewd scene"  text_style "text_small_cheats" action SetVariable("ep7_bella_lewd",False)
                                 else:
                                      textbutton "EP7 no Isabella lewd scene"  text_style "text_small_cheats" action SetVariable("ep7_bella_lewd",True)
                                   
                                 if branchIsabella:
                                     textbutton "EP8 Bella branch chosen  : Branches active: [wt_ep9_branch_numbers]"  text_style "text_small_cheats" action [SetVariable("branchIsabella",False)]
                                 else:
                                     textbutton "EP8 Bella branch not chosen : Branches active: [wt_ep9_branch_numbers]"  text_style "text_small_cheats" action [SetVariable("branchIsabella",True)]
                    ################################################
                        elif variables_character == "sage":
                            vbox xpos 0 ypos 0 spacing 5:
                              if currentEpisode >= 9:
                                  #if ep2_kissedSage:
                                  #  textbutton "EP2 kissed Sage at the party"  text_style "text_small_cheats" action SetVariable("ep2_kissedSage",False)
                                  #elif ep2_kissedSage == False:
                                  #  textbutton "EP2 Didn't kiss Sage at the party"  text_style "text_small_cheats" action SetVariable("ep2_kissedSage",True)
                                  if ep2SageGuitarTeacher:
                                    textbutton "EP2 teaching Sage to play guitar"  text_style "text_small_cheats" action SetVariable("ep2SageGuitarTeacher",False)
                                  elif ep2SageGuitarTeacher == False:
                                    textbutton "EP2 not teaching Sage to play guitar"  text_style "text_small_cheats" action SetVariable("ep2SageGuitarTeacher",True)
                              if currentEpisode >= 9:
                                  if rejectedSage:
                                    textbutton "EP3 Rejected Sage"  text_style "text_small_cheats" action [ToggleVariable("rejectedSage"),SetVariable("pathSage",True)]
                                  elif rejectedSage == False:
                                    textbutton "EP3 Didn't reject Sage"  text_style "text_small_cheats" action [ToggleVariable("rejectedSage"),SetVariable("pathSage",False)]
                              if currentEpisode >= 9:
                                 if ep3_choseBella==False and ep3_choseDerek==False and ep3_choseSage==False:
                                    $ep3_choseDerek=True
                                 if ep3_choseDerek:
                                     textbutton "EP4 Stayed with Derek"  text_style "text_small_cheats" action [SetVariable("ep3_choseBella",True),SetVariable("ep3_choseDerek",False)]
                                 elif ep3_choseBella:
                                     textbutton "EP4 Stayed with Isabella"  text_style "text_small_cheats" action [SetVariable("ep3_choseSage",True),SetVariable("ep3_choseBella",False)]
                                 elif ep3_choseSage:
                                     textbutton "EP4 Stayed with Sage"  text_style "text_small_cheats" action [SetVariable("ep3_choseDerek",True),SetVariable("ep3_choseSage",False)]                              
                              
                              if currentEpisode >= 9:
                                  if ep4_fuckedSage:
                                    textbutton "EP4 sex with Sage"  text_style "text_small_cheats" action ToggleVariable("ep4_fuckedSage")
                                  elif ep4_fuckedSage == False:
                                    textbutton "EP4 no sex with Sage"  text_style "text_small_cheats" action ToggleVariable("ep4_fuckedSage")
                                    
                                  if pathSage:
                                    textbutton "EP5 Sage Path Enabled"  text_style "text_small_cheats" action ToggleVariable("pathSage")
                                  elif pathSage == False:
                                    textbutton "EP5 Sage Path Disabled"  text_style "text_small_cheats" action ToggleVariable("pathSage")
                              if currentEpisode >= 9:
                                  
                                  
                                 if ep8_told_josy_chad:
                                        textbutton "EP8 Told Josy about Chad and Troy"  text_style "text_small_cheats" action ToggleVariable("ep8_told_josy_chad")
                                 elif ep8_told_josy_chad == False:
                                        textbutton "EP8 didn't tell Josy about Chad and Troy"  text_style "text_small_cheats" action ToggleVariable("ep8_told_josy_chad")
                            
                                 if not pathSage:
                                    if ep7_pathSage:
                                        textbutton "EP7 Sage Path Enabled"  text_style "text_small_cheats" action ToggleVariable("ep7_pathSage")
                                    elif ep7_pathSage == False:
                                        textbutton "EP7 Sage Path Disabled"  text_style "text_small_cheats" action ToggleVariable("ep7_pathSage")
                                     
                                 if branchSage:
                                     textbutton "EP8 Sage branch chosen  : Branches active: [wt_ep9_branch_numbers]"  text_style "text_small_cheats" action [SetVariable("branchSage",False)]
                                     
                                     if ep9_sage_vanilla:
                                        textbutton "    EP9 told Sage you like normal/vanilla sex"  text_style "text_small_cheats" action [SetVariable("ep9_sage_vanilla",False)]
                                     else:
                                        textbutton "    EP9 told Sage you'd try more sexual things"  text_style "text_small_cheats" action [SetVariable("ep9_sage_vanilla",True)]
                                     if currentEpisode >= 11:    
                                        if ep11_sage_love == 2:
                                            textbutton "    EP11 Sage said she loved you"  text_style "text_small_cheats" action [SetVariable("ep11_sage_love",1)]
                                        else:
                                            textbutton "    EP11 Sage didn't say she loved you"  text_style "text_small_cheats" action [SetVariable("ep11_sage_love",2)]
                                 else:
                                     textbutton "EP8 Sage branch not chosen : Branches active: [wt_ep9_branch_numbers]"  text_style "text_small_cheats" action [SetVariable("branchSage",True)]
                                   
                                    
                              # add later
                ############################################################################################
                            
                        elif variables_character == "josy":
                            vbox xpos 0 ypos 0 spacing 5:
                              if currentEpisode >= 9:
                                  if ep2_fuckedJosy:
                                    textbutton "EP2 had sex with Josy"  text_style "text_small_cheats" action SetVariable("ep2_fuckedJosy",False)
                                  elif ep2_fuckedJosy == False:
                                    textbutton "EP2 didn't have sex with Josy"  text_style "text_small_cheats" action SetVariable("ep2_fuckedJosy",True)

                              if currentEpisode >= 9:
                                  if pathMayaJosy:
                                   textbutton "EP4 in relationship with Maya and Josy"  text_style "text_small_cheats" action SetVariable("pathMayaJosy",False)
                                  elif pathMayaJosy == False:
                                   textbutton "EP4 not in relationship with Maya and Josy"  text_style "text_small_cheats" action SetVariable("pathMayaJosy",True)                                  
                              if currentEpisode >= 9:
                              
                                 if ep8_told_josy_chad:
                                        textbutton "EP8 Told Josy about Chad and Troy"  text_style "text_small_cheats" action ToggleVariable("ep8_told_josy_chad")
                                 elif ep8_told_josy_chad == False:
                                        textbutton "EP8 didn't tell Josy about Chad and Troy"  text_style "text_small_cheats" action ToggleVariable("ep8_told_josy_chad")
                                 
                                 if not pathMayaJosy:
                                  if ep5_feelingsForJosy:
                                   textbutton "EP5 said you had feelings for Josy"  text_style "text_small_cheats" action SetVariable("ep5_feelingsForJosy",False)
                                  elif ep5_feelingsForJosy == False:
                                   textbutton "EP5 didn't say you had feelings for Josy "  text_style "text_small_cheats" action SetVariable("ep5_feelingsForJosy",True)
                                   
                                   
                                 if branchMayaJosy:
                                     textbutton "EP8 MayaJosy branch chosen  : Branches active: [wt_ep9_branch_numbers]"  text_style "text_small_cheats" action [SetVariable("branchMayaJosy",False)]
                                     if ep11_josy_love == 2:
                                            textbutton "EP11 Told Josy you loved her and she said it back"  text_style "text_small_cheats" action [SetVariable("ep11_josy_love",1)]
                                     elif ep11_josy_love == 1:
                                            textbutton "EP11 Told Josy you loved her and she didn't say it back"  text_style "text_small_cheats" action [SetVariable("ep11_josy_love",0)]
                                     elif ep11_josy_love == 0:
                                            textbutton "EP11 didn't say to Josy you loved her"  text_style "text_small_cheats" action [SetVariable("ep11_josy_love",2)]
                                 else:
                                     textbutton "EP8 MayaJosy branch not chosen : Branches active: [wt_ep9_branch_numbers]"  text_style "text_small_cheats" action [SetVariable("branchMayaJosy",True)]
                                     if currentEpisode >= 10:
                                        if ep9_jm_sad:
                                            
                                            textbutton "    EP9 Broke up with Maya&Josy"  text_style "text_small_cheats" action [SetVariable("ep9_jm_sad",False)]
                                        else:
                                            textbutton "    EP9 didn't break up with Maya&Josy"  text_style "text_small_cheats" action [SetVariable("ep9_jm_sad",True)]                 
                    #########################################################################################################
                        elif variables_character == "maya":
                            vbox xpos 0 ypos 0 spacing 5:
                              #if currentEpisode >= 9:
                                  #if ep2_TriedToKissMaya:
                                  #  textbutton "EP2 tried to kiss Maya"  text_style "text_small_cheats" action SetVariable("ep2_TriedToKissMaya",False)
                                  #elif ep2_TriedToKissMaya == False:
                                  #  textbutton "EP2 didn't try to kiss Maya"  text_style "text_small_cheats" action SetVariable("ep2_TriedToKissMaya",True)
                              if currentEpisode >= 9:
                                  #if ep3_mayaOfferedHelp:
                                  #   textbutton "EP3 offered to help her"  text_style "text_small_cheats" action SetVariable("ep3_mayaOfferedHelp",False)
                                  #elif ep3_mayaOfferedHelp == False:
                                  #   textbutton "EP3 didn't offer to help her"  text_style "text_small_cheats" action SetVariable("ep3_mayaOfferedHelp",True)
                                  if ep3_mayaLewd:
                                     textbutton "EP3 sex with Maya"  text_style "text_small_cheats" action SetVariable("ep3_mayaLewd",False)
                                  elif ep3_mayaLewd == False:
                                     textbutton "EP3 no sex with Maya"  text_style "text_small_cheats" action SetVariable("ep3_mayaLewd",True)
                                     
                              if currentEpisode >= 9:
                                  if pathMayaJosy:
                                     textbutton "EP4 in relationship with Maya and Josy"  text_style "text_small_cheats" action SetVariable("pathMayaJosy",False)
                                  elif pathMayaJosy == False:
                                     textbutton "EP4 not in relationship with Maya and Josy"  text_style "text_small_cheats" action SetVariable("pathMayaJosy",True)
                                     
                              if currentEpisode >= 9:
                                 if not pathMayaJosy:
                                  if ep5_feelingsForMaya:
                                   textbutton "EP5 said you had feelings for Maya"  text_style "text_small_cheats" action SetVariable("ep5_feelingsForMaya",False)
                                  elif ep5_feelingsForMaya== False:
                                   textbutton "EP5 didn't say you had feelings for Maya "  text_style "text_small_cheats" action SetVariable("ep5_feelingsForMaya",True)
                                   
                                 if branchMayaJosy:
                                     textbutton "EP8 MayaJosy branch chosen  : Branches active: [wt_ep9_branch_numbers]"  text_style "text_small_cheats" action [SetVariable("branchMayaJosy",False)]
                                     if currentEpisode >= 11:
                                        if ep11_maya_love == 2:
                                            textbutton "EP11 Told Maya you loved her and she said it back"  text_style "text_small_cheats" action [SetVariable("ep11_maya_love",1)]
                                        elif ep11_maya_love == 1:
                                            textbutton "EP11 Told Maya you loved her and she didn't say it back"  text_style "text_small_cheats" action [SetVariable("ep11_maya_love",0)]
                                        elif ep11_maya_love == 0:
                                            textbutton "EP11 didn't say to Maya you loved her"  text_style "text_small_cheats" action [SetVariable("ep11_maya_love",2)]
                                 else:
                                     textbutton "EP8 MayaJosy branch not chosen : Branches active: [wt_ep9_branch_numbers]"  text_style "text_small_cheats" action [SetVariable("branchMayaJosy",True)]
                                     if currentEpisode >= 10:
                                        if ep9_jm_sad:
                                            
                                            textbutton "    EP9 Broke up with Maya&Josy"  text_style "text_small_cheats" action [SetVariable("ep9_jm_sad",False)]
                                        else:
                                            textbutton "    EP9 didn't break up with Maya&Josy"  text_style "text_small_cheats" action [SetVariable("ep9_jm_sad",True)]
                                ####ep2_recommendedSage  ep4_wantedMoreMayaJosy   ep4_overreacted 
                                      ## $ ep4_rejectedMayaJosy 
                    
                    ############################################################################################
                      #  elif variables_character == "troy":
                       #     vbox xpos 0 ypos 0 spacing 5:
                        #      if currentEpisode >= 1:
                         #       if ep1_beat_up_troy:
                          #          textbutton "EP1 Fought Troy"  text_style "text_small_cheats" action SetVariable("ep1_beat_up_troy",False)
                           #     elif ep1_beat_up_troy == False:
                            #        textbutton "EP1 Didn't Fight Troy"  text_style "text_small_cheats" action SetVariable("ep1_beat_up_troy",True)
                             #   if ep1_beat_up_troy:
                              #      if ep1_beat_up_troy_won:
                               #         textbutton "   EP1 Fought Troy and won"  text_style "text_small_cheats" action SetVariable("ep1_beat_up_troy_won",False)
                                #    elif ep1_beat_up_troy_won == False:
                                 #       textbutton "   EP1 Fought Troy and lost"  text_style "text_small_cheats" action SetVariable("ep1_beat_up_troy_won",True)
                                        
                #########################################################################################################
                        elif variables_character == "jade":
                            vbox xpos 0 ypos 0 spacing 5:
                              #if currentEpisode >= 9:
                                  #if preferredmilf == 0:
                                  #  textbutton "EP1 Prefer Jade over Cathy"  text_style "text_small_cheats" action SetVariable("preferredmilf",1)
                                  #elif preferredmilf == 1:
                                  #  textbutton "EP1 Prefer Cathy over Jade"  text_style "text_small_cheats" action SetVariable("preferredmilf",0)
                              #if currentEpisode >= 9:
                                  #if ep2_flirtedJade:
                                  #    textbutton "EP2 Flirted with Jade"  text_style "text_small_cheats" action SetVariable("ep2_flirtedJade",False)
                                  #elif ep2_flirtedJade == False:
                                  #    textbutton "EP2 Didn't flirt with Jade"  text_style "text_small_cheats" action SetVariable("ep2_flirtedJade",True)
                              if currentEpisode >= 9:
                                  #if ep4_jadeOffer:
                                  #    textbutton "EP4 Made a Move on Jade"  text_style "text_small_cheats" action SetVariable("ep4_jadeOffer",False)
                                  #elif ep4_jadeOffer == False:
                                  #    textbutton "EP4 Didn't make a move on Jade"  text_style "text_small_cheats" action SetVariable("ep4_jadeOffer",True)
                                      
                                  #if ep4_rejectedJade:
                                  #    textbutton "EP4 rejected Jade"  text_style "text_small_cheats" action SetVariable("ep4_rejectedJade",False)
                                  #elif ep4_rejectedJade == False:
                                  #    textbutton "EP4 Didn't reject Jade"  text_style "text_small_cheats" action SetVariable("ep4_rejectedJade",True)
                                      
                                  if currentEpisode < 9:
                                      if ep4_fuckedJade:
                                          textbutton "EP4 Sex with Jade"  text_style "text_small_cheats" action SetVariable("ep4_fuckedJade",False)
                                          if ep4_toldDerekAboutJade:
                                            textbutton "    EP4 Told DIKs about Sex with Jade"  text_style "text_small_cheats" action SetVariable("ep4_toldDerekAboutJade",False)
                                          else:
                                            textbutton "    EP4 Didn't tell DIKs about Sex with Jade (Better choice)"  text_style "text_small_cheats" action SetVariable("ep4_toldDerekAboutJade",True)
                                      elif ep4_fuckedJade == False:
                                          textbutton "EP4 no sex with Jade"  text_style "text_small_cheats" action SetVariable("ep4_fuckedJade",True)
                                  
                                  
                              if currentEpisode >= 9:
                                if jade_state == 0:
                                      textbutton "Ignored Jade (Keeps Sage path open)"  text_style "text_small_cheats" action [SetVariable("ep6_reject_jade",False),SetVariable("jade_state",1)]
                                elif jade_state == 1:
                                      textbutton "Continued her path"  text_style "text_small_cheats" action [SetVariable("ep6_reject_jade",True),SetVariable("jade_state",3)]
                                elif jade_state == 2 or jade_state == 3:
                                     textbutton "Stopped seeing Jade"  text_style "text_small_cheats" action [SetVariable("ep6_reject_jade",False),SetVariable("jade_state",0)]
                                
                                if ep11_jade_lewd:
                                            textbutton "    EP11 Jade sex"  text_style "text_small_cheats" action SetVariable("ep11_jade_lewd",False)
                                else:
                                            textbutton "    EP11 no Jade sex"  text_style "text_small_cheats" action SetVariable("ep11_jade_lewd",True)
                                if ep4_toldDerekAboutJade:
                                            textbutton "    EP4 Told DIKs about Sex with Jade"  text_style "text_small_cheats" action SetVariable("ep4_toldDerekAboutJade",False)
                                else:
                                            textbutton "    EP4 Didn't tell DIKs about Sex with Jade (Better choice)"  text_style "text_small_cheats" action SetVariable("ep4_toldDerekAboutJade",True)
                                                                        
            ####################################################################
                        elif variables_character == "jill":
                           vbox xpos 0 ypos 0 spacing 5:
                             #if currentEpisode >= 9:                        
                              ######################
                                 #if  ep4_kissedJill:
                                 #   textbutton "EP4 kissed Jill"  text_style "text_small_cheats" action SetVariable("ep4_kissedJill",False)
                                 #elif not ep4_kissedJill:
                                 #   textbutton "EP4 Didn't kiss Jill"  text_style "text_small_cheats" action SetVariable("ep4_kissedJill",True)
                             if currentEpisode >= 9:
                                 if  ep5_kissed_jill:
                                    textbutton "EP5 kissed Jill"  text_style "text_small_cheats" action SetVariable("ep5_kissed_jill",False)
                                 elif not ep5_kissed_jill:
                                    textbutton "EP5 Didn't kiss Jill"  text_style "text_small_cheats" action SetVariable("ep5_kissed_jill",True)
                                 
                                 if pathJill:
                                    textbutton "Jill path: Active"  text_style "text_small_cheats" action SetVariable("pathJill",False)
                                 elif pathJill  == False:
                                    textbutton "Jill path: Disabled"  text_style "text_small_cheats" action SetVariable("pathJill",True)
                                    
                                 if ep6_jill_lewd:
                                    textbutton "EP6 went on date with Jill"  text_style "text_small_cheats" action [SetVariable("pathJill",False),SetVariable("ep6_jill_lewd",False)]
                                 elif ep6_jill_lewd  == False:
                                    textbutton "EP6 didn't go date with Jill"  text_style "text_small_cheats" action [SetVariable("pathJill",False),SetVariable("ep6_jill_lewd",True)]
                                 ###ep7_done_jill_text
                             if currentEpisode >= 9:
                                if ep7_jill_lewd:
                                    textbutton "EP7 Jill lewd scene"  text_style "text_small_cheats" action [SetVariable("ep7_jill_lewd",False),SetVariable("ep8_jill_state",0)]
                                else:
                                    textbutton "EP7 no Jill lewd scene "  text_style "text_small_cheats" action [SetVariable("ep7_jill_lewd",True),SetVariable("ep8_jill_state",1)]
                                    
                                if ep8_recital_failed:
                                    textbutton "EP8 didn't help Jill at recital"  text_style "text_small_cheats" action [SetVariable("ep8_recital_failed",False)]
                                else:
                                    textbutton "EP8 helped Jill at recital"  text_style "text_small_cheats" action [SetVariable("ep8_recital_failed",True)]
                                
                                if branchJill:
                                     textbutton "EP8 Jill branch chosen  : Branches active: [wt_ep9_branch_numbers]"  text_style "text_small_cheats" action [SetVariable("branchJill",False)]
                                     
                                     if ep9_told_jill:
                                        textbutton "    EP9 Told Jill about Bianca's boyfriend"  text_style "text_small_cheats" action [SetVariable("ep9_told_jill",False)]
                                     else:
                                        textbutton "    EP9 didn't tell Jill about Bianca's boyfriend"  text_style "text_small_cheats" action [SetVariable("ep9_told_jill",True)]
                                else:
                                     textbutton "EP8 Jill branch not chosen : Branches active: [wt_ep9_branch_numbers]"  text_style "text_small_cheats" action [SetVariable("branchJill",True)]
                                     
                                if not branchJill or branchIsabella:
                                    if ep9_b_kissed_jill:
                                         textbutton "    EP9 kissed Jill"  text_style "text_small_cheats" action [SetVariable("ep9_b_kissed_jill",False)]
                                    else:
                                        textbutton "    EP9 didn't kiss Jill"  text_style "text_small_cheats" action [SetVariable("ep9_b_kissed_jill",True)]
                                     
                                     
                                     
                                
            #####################################################################
                        elif variables_character == "cathy":
                            vbox xpos 0 ypos 0 spacing 5:
                              #if currentEpisode >= 9: 
                                  #if preferredmilf == 0:
                                  #  textbutton "EP1 Prefer Jade over Cathy"  text_style "text_small_cheats" action SetVariable("preferredmilf",1)
                                  #elif preferredmilf == 1:
                                  #  textbutton "EP1 Prefer Cathy over Jade"  text_style "text_small_cheats" action SetVariable("preferredmilf",0)
                              #if currentEpisode >= 9:
                                #if swyper_rejected_by_cathy or swyper_cathy_state != "ep4_done":
                                #   textbutton "EP4 Swyper got rejected"  text_style "text_small_cheats" action Function (cathy_swyper_cheat)
                                #elif swyper_rejected_by_cathy == False and swyper_cathy_state == "ep4_done":
                                #    textbutton "EP4 Cathy Swyper best outcome"  text_style "text_small_cheats" action Function (cathy_swyper_cheat)
                              if currentEpisode >= 9:
                                if ep5_cathy_lewd    :
                                    textbutton "EP5 Cathy Car BJ"  text_style "text_small_cheats" action SetVariable("ep5_cathy_lewd",False)
                                elif not ep5_cathy_lewd    :
                                    textbutton "EP5 no Cathy Car BJ"  text_style "text_small_cheats" action SetVariable("ep5_cathy_lewd",True)
                              if currentEpisode >= 9:
                                 if ep7_rejected_cathy    :
                                    textbutton "EP7 you rejected Cathy"  text_style "text_small_cheats" action SetVariable("ep7_rejected_cathy",False)
                                 else:
                                    textbutton "EP7 continued with Cathy"  text_style "text_small_cheats" action SetVariable("ep7_rejected_cathy",True)
                              if currentEpisode >= 11:
                                 if ep10_cathy_lewd     :
                                    textbutton "EP10 Cathy sex"  text_style "text_small_cheats" action SetVariable("ep10_cathy_lewd",False)
                                 else:
                                    textbutton "EP10 no Cathy sex"  text_style "text_small_cheats" action SetVariable("ep10_cathy_lewd",True)
                              
                                                         
                        ####################################################
                        elif variables_character == "camila":
                            vbox xpos 0 ypos 0 spacing 5:
                              if currentEpisode >= 1:
                                
                                if quinn_shop_spicy_lvl == 1:
                                        textbutton "EP1 Camila 'take out' scene"  text_style "text_small_cheats" action SetVariable("quinn_shop_spicy_lvl",0)
                                elif quinn_shop_spicy_lvl == 0:
                                        textbutton "EP1 no Camila 'take out' scene"  text_style "text_small_cheats" action SetVariable("quinn_shop_spicy_lvl",1)
                                if ep1_lewd_camila_quinn:
                                        textbutton "EP1 Camila/Quinn Lewd scene"  text_style "text_small_cheats" action SetVariable("ep1_lewd_camila_quinn",False)
                                elif ep1_lewd_camila_quinn == False:
                                        textbutton "EP1 no Camila/Quinn Lewd scene"  text_style "text_small_cheats" action SetVariable("ep1_lewd_camila_quinn",True)
                              if currentEpisode >= 3:
                                  if ep3_helpedCamilaAndMona:
                                        textbutton "EP3 Helped Camila and Mona"  text_style "text_small_cheats" action SetVariable("ep3_helpedCamilaAndMona",False)
                                        if ep3_fuckedCamilaAndMona:
                                            textbutton "   EP3 Had sex with Camila/Mona"  text_style "text_small_cheats" action SetVariable("ep3_fuckedCamilaAndMona",False)
                                        elif ep3_fuckedCamilaAndMona == False:
                                            textbutton "   EP3 Didn't have sex with Camila/Mona"  text_style "text_small_cheats" action SetVariable("ep3_fuckedCamilaAndMona",True)
                                        
                                  elif ep3_helpedCamilaAndMona == False:
                                        textbutton "EP3 Didn't help Camila and Mona"  text_style "text_small_cheats" action SetVariable("ep3_helpedCamilaAndMona",True)
                              if currentEpisode >= 4:
                                        #if ep4_camilaOffer:
                                        #    textbutton "EP4 asked Camila about sex outdoors"  text_style "text_small_cheats" action SetVariable("ep4_camilaOffer",False)
                                        #elif ep4_camilaOffer == False:
                                        #    textbutton "EP4 didn't ask Camila about sex outdoors"  text_style "text_small_cheats" action SetVariable("ep4_camilaOffer",True)
                                            
                                            
                                        if ep4_hottest_ass == "Sarah":
                                         textbutton "EP4 said Sarah has best ass"  text_style "text_small_cheats" action SetVariable("ep4_hottest_ass","Riona")
                                        elif ep4_hottest_ass == "Riona":
                                         textbutton "EP4 said Riona has best ass"  text_style "text_small_cheats" action SetVariable("ep4_hottest_ass","Camila")
                                        elif ep4_hottest_ass == "Camila":
                                         textbutton "EP4 said Camila has best ass"  text_style "text_small_cheats" action SetVariable("ep4_hottest_ass","Sarah")
                                        elif ep4_hottest_ass != "Camila" and ep4_hottest_ass != "Riona" and ep4_hottest_ass != "Sarah":
                                         textbutton "EP4 said some other has best ass"  text_style "text_small_cheats" action SetVariable("ep4_hottest_ass","Sarah")    
                              if currentEpisode >= 6:
                                if ep5_fuckedCamila:
                                            textbutton "EP5 sex with Camila"  text_style "text_small_cheats" action SetVariable("ep5_fuckedCamila",False)
                                elif ep5_fuckedCamila == False:
                                            textbutton "EP5 no sex with Camila"  text_style "text_small_cheats" action SetVariable("ep5_fuckedCamila",True)
                              if currentEpisode >= 7:
                                 if ep7_camila_lewd:
                                         textbutton "EP7 Camila Sex"  text_style "text_small_cheats" action SetVariable("ep7_camila_lewd",False)
                                         if ep7_rica_lewd:
                                             textbutton "    EP7 Camila,Riona Sex"  text_style "text_small_cheats" action SetVariable("ep7_rica_lewd",False)
                                         else:
                                             textbutton "    EP7 no Camila,Riona Sex"  text_style "text_small_cheats" action SetVariable("ep7_rica_lewd",True)
                                 else:
                                         textbutton "EP7 No Camila Sex"  text_style "text_small_cheats" action SetVariable("ep7_camila_lewd",True)
                              
                                        
                        ###############################################################################
                        elif variables_character == "lily":
                           vbox xpos 0 ypos 0 spacing 5:
                             if currentEpisode >= 7:
                                  if ep7_lily_lewd:
                                            textbutton "EP7 Lily Sex"  text_style "text_small_cheats" action SetVariable("ep7_lily_lewd",False)
                                  elif ep7_lily_lewd == False:
                                            textbutton "EP7 no Lily Sex"  text_style "text_small_cheats" action SetVariable("ep7_lily_lewd",True)
                             if currentEpisode >= 10:
                                  if ep10_rolling:
                                            textbutton "EP10 - Rolling with Lily"  text_style "text_small_cheats" action SetVariable("ep10_rolling",False)
                                  elif ep10_rolling == False:
                                            textbutton "EP10 - not Rolling with Lily"  text_style "text_small_cheats" action SetVariable("ep10_rolling",True)
                             if currentEpisode >= 11:
                                  if ep11_rolling:
                                            textbutton "EP11 - Rolling with Lily"  text_style "text_small_cheats" action SetVariable("ep11_rolling",False)
                                  elif ep11_rolling == False:
                                            textbutton "EP11 - not Rolling with Lily"  text_style "text_small_cheats" action SetVariable("ep11_rolling",True)
                                  if ep11_lily_want_more:
                                            textbutton "EP11 - Said you want something more with Lily"  text_style "text_small_cheats" action SetVariable("ep11_lily_want_more",False)
                                  elif ep11_lily_want_more == False:
                                            textbutton "EP11 - didn't say you want something more with Lily"  text_style "text_small_cheats" action SetVariable("ep11_lily_want_more",True)
                                  
                                
                        ###############################################################################
                        elif variables_character == "mona":
                           vbox xpos 0 ypos 0 spacing 5:
                             if currentEpisode >= 3:
                                  if ep3_helpedCamilaAndMona:
                                        textbutton "EP3 Helped Camila and Mona"  text_style "text_small_cheats" action SetVariable("ep3_helpedCamilaAndMona",False)
                                        if ep3_fuckedCamilaAndMona:
                                            textbutton "   EP3 Had sex with Camila/Mona"  text_style "text_small_cheats" action SetVariable("ep3_fuckedCamilaAndMona",False)
                                        elif ep3_fuckedCamilaAndMona == False:
                                            textbutton "   EP3 Didn't have sex with Camila/Mona"  text_style "text_small_cheats" action SetVariable("ep3_fuckedCamilaAndMona",True)
                                        
                                  elif ep3_helpedCamilaAndMona == False:
                                        textbutton "EP3 Didn't help Camila and Mona"  text_style "text_small_cheats" action SetVariable("ep3_helpedCamilaAndMona",True)
                        
                        #######################################################################################
                        elif variables_character == "riona":
                          vbox xpos 0 ypos 0 spacing 5:
                                if currentEpisode >= 1:
                                    
                                    if quinn_shop_japanese_lvl == 1:
                                        textbutton "EP1 Riona Blowjob"  text_style "text_small_cheats" action SetVariable("quinn_shop_japanese_lvl",0)
                                    elif quinn_shop_japanese_lvl != 1:
                                        textbutton "EP1 no Riona Blowjob"  text_style "text_small_cheats" action SetVariable("quinn_shop_japanese_lvl",1)
                                if currentEpisode >= 3:
                                
                                   if ep3_fuckedRionaQuinn:
                                        textbutton "EP3 Quinn/Riona threesome"  text_style "text_small_cheats" action SetVariable("ep3_fuckedRionaQuinn",False)
                                   elif ep3_fuckedRionaQuinn == False:
                                        textbutton "EP3 no Quinn/Riona threesome"  text_style "text_small_cheats" action SetVariable("ep3_fuckedRionaQuinn",True)
                                if currentEpisode >= 5:
                                   #if ep4_kissedRiona:
                                   #     textbutton "EP4 kissed Riona at party"  text_style "text_small_cheats" action SetVariable("ep4_kissedRiona",False)
                                   #elif ep4_kissedRiona == False:
                                   #     textbutton "EP4 didn't kiss Riona at party"  text_style "text_small_cheats" action SetVariable("ep4_kissedRiona",True)
                                
                                   
                                   
                                   if ep4_hottest_ass == "Sarah":
                                     textbutton "EP4 said Sarah has best ass"  text_style "text_small_cheats" action SetVariable("ep4_hottest_ass","Riona")
                                   elif ep4_hottest_ass == "Riona":
                                     textbutton "EP4 said Riona has best ass"  text_style "text_small_cheats" action SetVariable("ep4_hottest_ass","Camila")
                                   elif ep4_hottest_ass == "Camila":
                                     textbutton "EP4 said Camila has best ass"  text_style "text_small_cheats" action SetVariable("ep4_hottest_ass","Sarah")
                                   elif ep4_hottest_ass != "Camila" and ep4_hottest_ass != "Riona" and ep4_hottest_ass != "Sarah":
                                     textbutton "EP4 said some other has best ass"  text_style "text_small_cheats" action SetVariable("ep4_hottest_ass","Sarah")     
                                
                                if currentEpisode >= 6:
                                    
                                   #if ep5_gave_riona_money > 1:
                                   #     textbutton "EP5 gave Riona money"  text_style "text_small_cheats" action SetVariable("ep5_gave_riona_money",1)
                                   #elif ep5_gave_riona_money <= 1:
                                   #     textbutton "EP5 didn't give Riona money"  text_style "text_small_cheats" action SetVariable("ep5_gave_riona_money",5)
                                   if ep5_fuckedRiona:
                                        textbutton "EP5 Riona sex"  text_style "text_small_cheats" action SetVariable("ep5_fuckedRiona",False)
                                   else:
                                        textbutton "EP5 no Riona sex"  text_style "text_small_cheats" action SetVariable("ep5_fuckedRiona",True)
                                if currentEpisode >= 7 :   
                                     if ep7_riona_lewd:
                                         textbutton "EP7 Riona Sex"  text_style "text_small_cheats" action SetVariable("ep7_riona_lewd",False)
                                         if ep7_rica_lewd:
                                             textbutton "EP7 Camila,Riona Sex"  text_style "text_small_cheats" action SetVariable("ep7_rica_lewd",False)
                                         else:
                                             textbutton "EP7 no Camila,Riona Sex"  text_style "text_small_cheats" action SetVariable("ep7_rica_lewd",True)
                                     else:
                                         textbutton "EP7 no Riona Sex"  text_style "text_small_cheats" action SetVariable("ep7_riona_lewd",True)
                                if currentEpisode >= 10:
                                   if ep9_riona_choice != "DIK":
                                        textbutton "EP9 didn't make out with Riona"  text_style "text_small_cheats" action SetVariable("ep9_riona_choice","DIK")
                                   else:
                                        textbutton "EP9 made out with Riona"  text_style "text_small_cheats" action SetVariable("ep9_riona_choice","NEUTRAL")
                                if currentEpisode >= 10:
                                   if ep10_riona_lewd:
                                        textbutton "EP10 Riona sex"  text_style "text_small_cheats" action SetVariable("ep10_riona_lewd",False)
                                   else:
                                        textbutton "EP10 no Riona sex"  text_style "text_small_cheats" action SetVariable("ep10_riona_lewd",True)
                                if currentEpisode >= 11:          
                                    if ep11_quinn_question[1]:
                                            textbutton "EP11 defended Quinn's actions (for Quinn path)"  text_style "text_small_cheats" action SetDict(ep11_quinn_question,1,False)
                                    else:
                                            textbutton "EP11 didn't defend Quinn's actions (for Possible Riona path)"  text_style "text_small_cheats" action SetDict(ep11_quinn_question,1,True)
                                      
          ################################################################################################################################################              
                        elif variables_character == "quinn":
                            vbox xpos 0 ypos 0 spacing 5:
                              if currentEpisode >= 1:
                                if ep1_lewd_camila_quinn:
                                        textbutton "EP1 Camila/Quinn Lewd scene"  text_style "text_small_cheats" action SetVariable("ep1_lewd_camila_quinn",False)
                                elif ep1_lewd_camila_quinn == False:
                                        textbutton "EP1 no Camila/Quinn Lewd scene"  text_style "text_small_cheats" action SetVariable("ep1_lewd_camila_quinn",True)
                            
                                #if currentEpisode < 7:
                                    #if ep1_accepted_quinn_offer and number_quinn:
                                    #    textbutton "EP1 accepted Quinn's 'Restaurant' offer"  text_style "text_small_cheats" action [SetVariable("ep1_accepted_quinn_offer",False),SetVariable("number_quinn",False)]
                                    #elif ep1_accepted_quinn_offer == False and number_quinn == False:
                                    #    textbutton "EP1 Didn't accept Quinn's 'Restaurant' offer\n(needs to be enabled before freeroams to work)"  text_style "text_small_cheats" action [SetVariable("ep1_accepted_quinn_offer",True),SetVariable("number_quinn",True)]
                                #elif currentEpisode >= 7:
                                    #if ep1_accepted_quinn_offer:
                                    #    textbutton "EP1 accepted Quinn's 'Restaurant' offer"  text_style "text_small_cheats" action [SetVariable("ep1_accepted_quinn_offer",False)]
                                    #elif ep1_accepted_quinn_offer == False:
                                    #    textbutton "EP1 Didn't accept Quinn's 'Restaurant' offer"  text_style "text_small_cheats" action [SetVariable("ep1_accepted_quinn_offer",True)]
                                if currentEpisode >= 3:
                                  #if quinnLikesYou:
                                   #     textbutton "EP3 Quinn Likes you"  text_style "text_small_cheats" action SetVariable("quinnLikesYou",False)
                                  #elif quinnLikesYou == False:
                                   #     textbutton "EP3 Quinn doesn't like you"  text_style "text_small_cheats" action SetVariable("quinnLikesYou",True)
                                   if ep3_fuckedRionaQuinn:
                                        textbutton "EP3 Quinn/Riona threesome"  text_style "text_small_cheats" action SetVariable("ep3_fuckedRionaQuinn",False)
                                   elif ep3_fuckedRionaQuinn == False:
                                        textbutton "EP3 no Quinn/Riona threesome"  text_style "text_small_cheats" action SetVariable("ep3_fuckedRionaQuinn",True)
                                if currentEpisode >= 5:
                                  if ep4_quinn_lewd:
                                        textbutton "EP4 sex with Quinn"  text_style "text_small_cheats" action SetVariable("ep4_quinn_lewd",False)
                                  elif ep4_quinn_lewd == False:
                                        textbutton "EP4 no sex with Quinn"  text_style "text_small_cheats" action SetVariable("ep4_quinn_lewd",True)
                                if currentEpisode >= 6:
                                  if ep6_quinn_lewd:
                                        textbutton "EP6 sex with Quinn"  text_style "text_small_cheats" action SetVariable("ep6_quinn_lewd",False)
                                  elif ep6_quinn_lewd == False:
                                        textbutton "EP6 no sex with Quinn"  text_style "text_small_cheats" action SetVariable("ep6_quinn_lewd",True)
                                  if ep8_quinn_lewd:
                                 
                                    textbutton "EP8 sex with Quinn"  text_style "text_small_cheats" action SetVariable("ep8_quinn_lewd",False)
                                  elif ep8_quinn_lewd == False:
                                        textbutton "EP8 no sex with Quinn"  text_style "text_small_cheats" action SetVariable("ep8_quinn_lewd",True)
                                if currentEpisode >= 10:
                                    if ep10_quinn_help:
                                 
                                        textbutton "EP10 helped Quinn"  text_style "text_small_cheats" action SetVariable("ep10_quinn_help",False)
                                    elif ep10_quinn_help == False:
                                        textbutton "EP10 didn't help Quinn"  text_style "text_small_cheats" action SetVariable("ep10_quinn_help",True)
                                
                              if currentEpisode >= 11:          
                                if ep11_quinn_question[1]:
                                            textbutton "EP11 defended Quinn's actions (for Quinn path)"  text_style "text_small_cheats" action [SetDict(ep11_quinn_question,1,False),SetDict(ep11_quinn_question,0,True)]
                                else:
                                            textbutton "EP11 didn't defend Quinn's actions (for Possible Riona path)"  text_style "text_small_cheats" action [SetDict(ep11_quinn_question,1,True),SetDict(ep11_quinn_question,0,True)]
                                
                                
                                                                  
                        ######################################################################
                        
                            
                        
                        #############################################
                        elif variables_character == "other":
                            vbox xpos 0 ypos 0 spacing 5:
                              if currentEpisode >= 1:
                                if ep1_beat_up_troy:
                                    textbutton "EP1 Fought Troy"  text_style "text_small_cheats" action SetVariable("ep1_beat_up_troy",False)
                                elif ep1_beat_up_troy == False:
                                    textbutton "EP1 Didn't Fight Troy"  text_style "text_small_cheats" action SetVariable("ep1_beat_up_troy",True)
                                if ep1_beat_up_troy:
                                    if ep1_beat_up_troy_won:
                                        textbutton "   EP1 Fought Troy and won"  text_style "text_small_cheats" action SetVariable("ep1_beat_up_troy_won",False)
                                    elif ep1_beat_up_troy_won == False:
                                        textbutton "   EP1 Fought Troy and lost"  text_style "text_small_cheats" action SetVariable("ep1_beat_up_troy_won",True)
                              #if currentEpisode >= 1:
                                #if ep1_insulted_cafeteria_worker:
                                #        textbutton "EP1 Insulted cafeteria worker"  text_style "text_small_cheats" action SetVariable("ep1_insulted_cafeteria_worker",False)
                                #elif ep1_insulted_cafeteria_worker == False:
                                #        textbutton "EP1 Didn't Insult cafeteria worker"  text_style "text_small_cheats" action SetVariable("ep1_insulted_cafeteria_worker",True)
                              if currentEpisode >= 2:
                                 if ep2_wonCumpetition:
                                        textbutton "EP2 Won Cumpetition"  text_style "text_small_cheats" action SetVariable("ep2_wonCumpetition",False)
                                 elif ep2_wonCumpetition == False:
                                        textbutton "EP2 Lost Cumpetition"  text_style "text_small_cheats" action SetVariable("ep2_wonCumpetition",True)
                                 #if ep2_cafeteriaWorkerInsulted:
                                 #       textbutton "EP2 Insulted cafeteria worker"  text_style "text_small_cheats" action SetVariable("ep2_cafeteriaWorkerInsulted",False)
                                 #elif not ep2_cafeteriaWorkerInsulted:
                                 #       textbutton "EP2 Didn't Insult cafeteria worker"  text_style "text_small_cheats" action SetVariable("ep2_cafeteriaWorkerInsulted",True)
                              #if currentEpisode >= 3:
                                 #if ep3_sclubParty:
                                 #       textbutton "EP3 Did DIK stuff at the Strip Club"  text_style "text_small_cheats" action SetVariable("ep3_sclubParty",False)
                                 #elif ep3_sclubParty == False:
                                 #       textbutton "EP3 Let Derek do the DIK stuff at the Strip Club"  text_style "text_small_cheats" action SetVariable("ep3_sclubParty",True)
                              
                              if currentEpisode >= 6:
                              
                                
                              
                                if ep5_dikWinner:
                                        textbutton "EP5 Won the DIK Hell week contest"  text_style "text_small_cheats" action SetVariable("ep5_dikWinner",False)
                                        if ep6_vipPass:
                                            textbutton "  EP6 got the Pink Rose VIP pass"  text_style "text_small_cheats" action SetVariable("ep6_vipPass",False)
                                        elif ep6_vipPass == False:
                                            textbutton "  EP6 didn't get the Pink Rose VIP pass"  text_style "text_small_cheats" action SetVariable("ep6_vipPass",True)
                                        
                                        
                                elif ep5_dikWinner == False:
                                        textbutton "EP5 lost the DIK Hell week contest"  text_style "text_small_cheats" action SetVariable("ep5_dikWinner",True)
                            
                              if currentEpisode >= 7:
                                 if ep6_nora_lewd:
                                       textbutton "EP6 Sex with Nora"  text_style "text_small_cheats" action SetVariable("ep6_nora_lewd",False)
                                 else:
                                        textbutton "EP6 no Sex with Nora"  text_style "text_small_cheats" action [SetVariable("ep6_nora_lewd",True)]
                                 if ep7_accept_madame:
                                        textbutton "EP7 Interested in Madame"  text_style "text_small_cheats" action SetVariable("ep7_accept_madame",False)
                                 elif ep7_accept_madame == False:
                                        textbutton "EP7 not Interested in Madame"  text_style "text_small_cheats" action [SetVariable("ep7_accept_madame",True),Function(madame_phone_add)] 
                                 if branchAlone:
                                     textbutton "EP8 Alone branch chosen  : Branches active: [wt_ep9_branch_numbers]"  text_style "text_small_cheats" action [SetVariable("branchAlone",False)]
                                 else:
                                     textbutton "EP8 Alone branch not chosen : Branches active: [wt_ep9_branch_numbers]"  text_style "text_small_cheats" action [SetVariable("branchAlone",True)]
                                                                             
                                                                    
###################################################################################################################################################################
                                 
            elif cheatcat4 == "OTHER":    ## minigames on/off ,tutorials on/off,brawler difficulty...  
                frame:
                        xpos 340
                        ypos 150
                        xmaximum 1500
                        ymaximum 800
                        background None
                        viewport:
                            draggable True
                            mousewheel True
                            vbox:
                                xpos 0
                                ypos 0
                                spacing 10
                                hbox xpos 0 ypos 0:
                                     frame xpos 0 ypos 0 background None:
                                         vbox xpos 0 ypos 0 spacing 5:
                                           if persistent.mod_wtenabled:
                                             textbutton "Walkthrough: Enabled"  text_style "text_small_cheats" action Function(mod_wt_toggle)
                                           elif not persistent.mod_wtenabled:
                                             textbutton "Walkthrough: Disabled"  text_style "text_small_cheats" action Function(mod_wt_toggle)
                                           #if wt_all_scenes:
                                           #  textbutton "Options to see all scenes: Enabled"  text_style "text_small_cheats" action SetVariable("wt_all_scenes",False)
                                           #elif not wt_all_scenes:
                                           #  textbutton "Options to see all scenes: Disabled"  text_style "text_small_cheats" action SetVariable("wt_all_scenes",True)
                                           if minigames:
                                            textbutton "Mini Games Enabled"  text_style "text_small_cheats" action SetVariable("minigames",False)
                                           elif minigames == False:
                                            textbutton "Mini Games Disabled"  text_style "text_small_cheats" action SetVariable("minigames",True)
                                           if tutorials:
                                            textbutton "Tutorials Enabled"  text_style "text_small_cheats" action SetVariable("tutorials",False)
                                           elif tutorials == False:
                                            textbutton "Tutorials Disabled"  text_style "text_small_cheats" action SetVariable("tutorials",True)
                                           #if brawler_difficulty == 1:
                                           #  textbutton "Brawler difficulty: Easy"  text_style "text_small_cheats" action SetVariable("brawler_difficulty",2)
                                           #elif brawler_difficulty == 2:
                                           #  textbutton "Brawler difficulty: Normal"  text_style "text_small_cheats" action SetVariable("brawler_difficulty",3)
                                           #elif brawler_difficulty == 3:
                                           #  textbutton "Brawler difficulty: Hard"  text_style "text_small_cheats" action SetVariable("brawler_difficulty",1)
                                           
    
                                           if persistent.wt_collectible_notify:
                                            textbutton "Show notification when collectible on screen: Enabled"  text_style "text_small_cheats" action SetVariable("persistent.wt_collectible_notify",False)
                                           else:
                                            textbutton "Show notification when collectible on screen: Disabled"  text_style "text_small_cheats" action SetVariable("persistent.wt_collectible_notify",True)
                                            
                                           if persistent.wt_collectible_circle:
                                            textbutton "Red circle over collectibles when on screen: Enabled"  text_style "text_small_cheats" action SetVariable("persistent.wt_collectible_circle",False)
                                           else:
                                            textbutton "Red circle over collectibles when on screen: Disabled"  text_style "text_small_cheats" action SetVariable("persistent.wt_collectible_circle",True)
                                            
                                           if persistent.no_cheater:
                                            textbutton "Cheater points have no effect: Enabled"  text_style "text_small_cheats" action SetVariable("persistent.no_cheater",False)
                                           else:
                                            textbutton "Cheater points have no effect: Disabled"  text_style "text_small_cheats" action SetVariable("persistent.no_cheater",True)
                                             
                                             
                            vbox:
                                xpos 850
                                ypos 0
                                spacing 10
                                hbox xpos 0 ypos 0:
                                     frame xpos 0 ypos 0 background None:
                                         vbox xpos 0 ypos 0 spacing 5:
                                            textbutton "Made by Scrappy"  text_style "text_small_cheats" action OpenURL("https://www.patreon.com/user?u=19542127")
                                            textbutton "PATREON"  text_style "text_small_cheats" action OpenURL("https://www.patreon.com/user?u=19542127")

####################################################################################################                                            
            

init 999 python:
    def madame_phone_add():
        global mphone_contact_list
        if mphone_contact_list[13][0] !="Madame Rose":
            mphone_contact_list.insert(13,["Madame Rose","NONE",False])
    
    def mod_paths_count():
    
        global branchJill
        global branchAlone
        global branchIsabella
        global branchMayaJosy
        global branchSage
        global wt_ep9_branch_numbers
        
        wt_ep9_branch_numbers=0
        if branchAlone:
           wt_ep9_branch_numbers+=1
        
        if branchIsabella:
            wt_ep9_branch_numbers+=1
        if branchJill:
            wt_ep9_branch_numbers+=1
        if branchMayaJosy:
            wt_ep9_branch_numbers+=1
        if branchSage:
            wt_ep9_branch_numbers+=1
        return

            
    def mod_wt_toggle():
       global mod_choices
       global mod_gr
       global m_c1,m_c2,m_c3,m_c4,m_c5,m_cr
       
       
       if persistent.mod_wtenabled:
           persistent.mod_wtenabled=False
           mod_gr=""
           mod_choices=["","","","","","","","","",""]
           m_c1=m_c2=m_c3=m_c4=m_c5=m_cr=""
           persistent.mod_wt_enabled=False
           
       else:
           persistent.mod_wtenabled=True
           persistent.mod_wt_enabled=True
           mod_gr = "{color=#32BD73}"
           m_c1="{color=#33ff33}"
           m_c2="{color=#E6F100}"
           m_c3="{color=#DF00F1}"
           m_c4="{color=#00F1D4}"
           m_c5="{color=#F0A607}"
           m_cr="{color=#F62217}"
           
           
       return
        
        
    def updateDikScore_m():
        global dtype
        global dik
        if dik > 20:
            dik = 20
        elif dik < -20:
            dik = -20
        
        if dik >=15:
            dtype = 3
        elif dik >=10:
            dtype = 2
        elif dik >=5:
            dtype = 1
        elif dik <5 and dik >-5:
            dtype = 0
        elif dik <=-15:
            dtype = -3
        elif dik <=-10:
            dtype = -2
        elif dik <=-5:
            dtype = -1
        return 
        
    def cheat_money(c_money):
        global money
        global wallet_lvl
        temp_cheat_money=money
        temp_cheat_money += c_money
        if temp_cheat_money > 5 and wallet_lvl==0:
            temp_cheat_money = 5
        elif temp_cheat_money > 5 and wallet_lvl==1:
            temp_cheat_money = 6
        elif temp_cheat_money > 5 and wallet_lvl==2:
            temp_cheat_money = 8
        elif temp_cheat_money > 5 and wallet_lvl==3:
            temp_cheat_money = 10
        
        elif temp_cheat_money < 0:
            temp_cheat_money = 0
        money=temp_cheat_money 
        
        return
#################################################
    def scene_unlock():
        persistent.epi_lewd_eb=True
        persistent.epi_lewd_zoey=True
        
        persistent.ep9_lewd_jade = True
    
        persistent.ep9_lewd_jill = True
    
        persistent.ep9_lewd_sage1 = True
    
        persistent.ep9_lewd_lily = True
    
        persistent.ep9_lewd_sage2 = True
    
        persistent.ep9_lewd_maya = True
    
        persistent.ep9_lewd_camila = True
   
        persistent.ep9_lewd_heather = True
    
        persistent.ep9_lewd_cumpetition = True
    
        persistent.ep9_lewd_isabella = True
    
        persistent.ep9_lewd_jm2 = True
   
        persistent.ep9_lewd_isabella2 = True
   
        persistent.ep9_lewd_jill2 = True
 
        persistent.ep9_lewd_jm = True
   
        persistent.ep9_lewd_sage3 = True
  
        persistent.ep9_lewd_ln = True
  
        persistent.ep9_lewd_quinn = True
  
        persistent.ep9_lewd_sm = True
        
        persistent.ep10_lewd_cathy= True
        persistent.ep10_lewd_madame1= True
        persistent.ep10_lewd_madame2= True
        persistent.ep10_lewd_madame3= True
        persistent.ep10_lewd_josy= True
        persistent.ep10_lewd_jm= True
        persistent.ep10_lewd_maya= True
        persistent.ep10_lewd_sage= True
        persistent.ep10_lewd_sage2= True
        persistent.ep10_lewd_jill= True
        persistent.ep10_lewd_isabella= True
        persistent.ep10_lewd_nicole= True
        persistent.ep10_lewd_riona= True
        persistent.ep10_lewd_nora= True
        persistent.ep10_lewd_lily= True
        persistent.ep10_lewd_quinn= True
        
        persistent.ep11_lewd_camila=True
        persistent.ep11_lewd_sarah=True
        persistent.ep11_lewd_melanie=True
        persistent.ep11_lewd_lynette=True
        persistent.ep11_lewd_jade=True
        persistent.ep11_lewd_madame=True
        persistent.ep11_lewd_bella=True
        persistent.ep11_lewd_bella2=True
        persistent.ep11_lewd_jill=True
        persistent.ep11_lewd_jm=True
        persistent.ep11_lewd_tiffani=True
        persistent.ep11_lewd_tara=True
        persistent.ep11_lewd_becky=True
        persistent.ep11_lewd_lily=True
        persistent.ep11_lewd_elena=True
        persistent.ep11_lewd_sage=True
        persistent.ep11_lewd_sage2=True
        persistent.ep11_lewd_jill2=True
        
        
        persistent.ep12_lewd_nora= True
    
        persistent.ep12_lewd_cathy= True

        persistent.ep12_lewd_ts= True
   
        persistent.ep12_lewd_nicole= True
    
        persistent.ep12_lewd_josy= True
    
        persistent.ep12_lewd_maya= True
    
        persistent.ep12_lewd_quinn= True
    
        persistent.ep12_lewd_bianca= True
    
        persistent.ep12_lewd_elena= True
    
        persistent.ep12_lewd_isabella= True
   
        persistent.ep12_lewd_jade= True
    
        persistent.ep12_lewd_jill= True
    
        persistent.ep12_lewd_quinn2= True
    
        persistent.ep12_lewd_sage= True
    
        persistent.ep12_lewd_sally = True
    
        persistent.ep12_lewd_zoey = True
        
        calcScenes()
        
        return
#########################################################
    def reward_unlock():
        global art_girl_name_list
        global wt_unlocked_reward
        for x in range (0,16):
            persistent.art_unlocked_lvl1[x] = True
        
        #wt_unlocked_reward=True
        
        persistent.art_unlocked_lvl2[0] = True
        persistent.art_unlocked_lvl2[2] = True
        persistent.art_unlocked_lvl2[7] = True
        persistent.art_unlocked_lvl2[11] = True
        persistent.art_unlocked_lvl2[13] = True
        persistent.art_unlocked_lvl2[3] = True
        persistent.art_unlocked_lvl2[5] = True
        persistent.art_unlocked_lvl2[6] = True
        persistent.art_unlocked_lvl2[4] = True
        persistent.art_unlocked_lvl2[8] = True
        persistent.art_unlocked_lvl2[9] = True
        persistent.art_unlocked_lvl2[10]=True
        persistent.art_unlocked_lvl2[1]=True
        persistent.art_unlocked_lvl2[12]=True
        persistent.art_unlocked_lvl2[14]=True
        
        persistent.art_unlocked_lvl3[2]=True
        persistent.art_unlocked_lvl3[7]=True
        
        persistent.art_unlocked_lvl3[0]=True
        persistent.art_unlocked_lvl3[9]=True
        persistent.art_unlocked_lvl3[14]=True
        persistent.art_unlocked_lvl2[15]=True
        persistent.ep12_card15=True

        persistent.ep12_card16=True
           
        persistent.ep12_card17=True

        persistent.ep12_card18=True

        persistent.ep12_card19=True
        
        persistent.ep7_wpi1=True
        persistent.ep7_wpi2=True
        persistent.ep7_wpj1=True
        persistent.ep7_wpj2=True
        persistent.ep7_wpjo1=True
        persistent.ep7_wpjo2=True
        persistent.ep7_wpm2=True
        persistent.ep7_wpm1=True
        persistent.ep7_wps1=True
        persistent.ep7_wps2=True
        persistent.ep8_wpi1=True
        persistent.ep8_wpjo1=True
        persistent.ep8_wpj1=True
        persistent.ep8_wpm1=True
        persistent.ep8_wpq1=True
        persistent.ep8_wps1=True
        persistent.ep8_wpe1=True
        persistent.ep8_wpjade1=True
        persistent.ep8_wpmad1=True
        
        
    
        
        persistent.epi_card1=True
        persistent.epi_card2=True
        persistent.epi_card3=True
        persistent.epi_card4=True
        persistent.epi_card5=True
        persistent.epi_card6=True
        persistent.epi_card7=True
        persistent.epi_card8=True
        persistent.epi_card9=True
        persistent.epi_card10=True
        persistent.epi_card11=True
        persistent.epi_card12=True
        persistent.epi_card13=True
        persistent.epi_card14=True
        persistent.epi_card15=True
        persistent.epi_card16=True
        
        for j in range (1,21):
                exec("persistent.ep9_card"+str(j)+"=True")
                exec("persistent.ep9_cardjo"+str(j)+"=True")
                exec("persistent.ep9_cardji"+str(j)+"=True")
                exec("persistent.ep10_cardzo"+str(j)+"=True")
                exec("persistent.ep10_cardsa"+str(j)+"=True")
                exec("persistent.ep11_cardmy"+str(j)+"=True")
                exec("persistent.ep11_cardly"+str(j)+"=True")
                exec("persistent.ep12_cardisa"+str(j)+"=True")
                exec("persistent.ep12_cardcam"+str(j)+"=True")
        for j in range (1,17):
                exec("persistent.ep10_card"+str(j)+"=True")
        for j in range (1,13):
                exec("persistent.ep11_card"+str(j)+"=True")
        for j in range (1,15):
                exec("persistent.ep12_card"+str(j)+"=True")
        persistent.ep10_card17=False
        persistent.ep10_card18=False
        persistent.ep10_card19=False
        persistent.ep10_card20=False   

        persistent.ep11_card9b=True
        persistent.ep11_card10b=True
        persistent.ep11_card11b=True
        persistent.ep11_card12b=True
        
        calcRenders()
        return