default m_c1="{color=#33ff33}"
default m_c2="{color=#E6F100}"
default m_c3="{color=#DF00F1}"
default m_c4="{color=#00F1D4}"
default m_c5="{color=#F0A607}"
default m_cr="{color=#F62217}"
default mod_gr="{color=#33ff33}"
default tmp_mod=""
default tmp_mod2=""
default m_c_text="{color=#08AC23}"
default wt_eng_class_help=" "
default tmp_eng_class_word=""
default tmp_mod_list=[]

screen notify_mod(message,name):

    zorder 100
    style_prefix "notify"

    frame at notify_appear:
        text "[m_c3]{size=35}[message!tq] [name!tq]"

    timer 3.25 action Hide('notify_mod')

screen puzzle_box_help:
    
    hbox:
            
            xalign 0.9
            yalign 0.2

            if persistent.mod_wtenabled:
                textbutton "{b}HELP{/b}" action [Show("puzzle_box_wt_help"),Hide("puzzle_box_help")] text_size 25 text_color "#FFFFFF"
                
                
screen puzzle_box_wt_help:
  tag guide
  modal False
  frame:
    xsize 450
    ysize 900
    xalign 1.0
    yalign 0.2
    vpgrid:
       xfill True
       yfill True
       cols 1
       textbutton "Close" action [Hide("puzzle_box_wt_help")] text_size 35 xpos(0.45)
       #####
       
       if puzzle_box_side==0:
           text "   1. Set all dials to point up" size 28
           text "   2. Set top left to left" size 28
           text "   3. Set lower left to left" size 28
           text "   4. Set top right to right" size 28
           text "   5. Set lower right to right" size 28
           text "   6. Press middle button" size 28
           text "   7. Set all dials to point up" size 28
           text "   8. Set top left to right" size 28
           text "   9. Set top right to right" size 28
           text "   10. Press middle button" size 28
           

screen word_cheat:
    if persistent.mod_wtenabled:
        text "[wt_eng_class_help]" xpos 0.255 ypos 0.012 size 22
          
          
screen wt_science_cheat:
      textbutton "SKIP CHEAT" action [SetVariable("sm_purity",95),Hide("wt_science_cheat"),Hide("sm_timer_screen"),Hide("sm_measure_screen"),Hide("sm_weigh_screen"),Hide("sm_notes_screen"),Hide("sm_stir_screen"),Hide("sm_turn_in_screen"),Hide("science_screen"),Jump("science_game_end_ep10_label")] xpos 0.45 ypos 0.1 text_size 40
      
screen wt_science_cheat2:
      textbutton "SKIP CHEAT" action [SetVariable("sm_purity",95),Hide("wt_science_cheat2"),Hide("sm_timer_screen"),Hide("sm_measure_screen"),Hide("sm_weigh_screen"),Hide("sm_notes_screen"),Hide("sm_stir_screen"),Hide("sm_turn_in_screen"),Hide("science_screen"),Jump("science_game_end_ep11_label")] xpos 0.45 ypos 0.1 text_size 40
      
screen wt_science_cheat3:
      textbutton "SKIP CHEAT" action [SetVariable("sm_purity",95),Hide("wt_science_cheat3"),Hide("sm_timer_screen"),Hide("sm_measure_screen"),Hide("sm_weigh_screen"),Hide("sm_notes_screen"),Hide("sm_stir_screen"),Hide("sm_turn_in_screen"),Hide("science_screen"),Jump("science_game_end_ep12_label")] xpos 0.45 ypos 0.1 text_size 40
      
      
screen wt_boxes_update():
   if persistent.mod_wtenabled:
        $wt_boxes_update_function()




init python:

   def wt_boxes_update_function():
        global task_list
        global event_list
        
        temp_string=""
        temp_bool=False
        temp_items=3
        
        if "ep11_fr_deco_box1_event_label" in event_list:
            temp_bool=True
            temp_string=temp_string+"/Left Hallway/"
            temp_items-=1
        if "ep11_fr_deco_box2_event_label" in event_list:
            temp_bool=True
            temp_string=temp_string+"/Kitchen/"
            temp_items-=1
        if "ep11_fr_deco_box3_event_label" in event_list:
            temp_bool=True
            temp_string=temp_string+"/Jacob's room/"
            temp_items-=1
            
        if temp_bool:
            temp_string="\n("+temp_string+")"
            task_list[0]="Find boxes labeled Kitchen (%s/3)" % (temp_items)
            task_list[0]=task_list[0]+temp_string
screen wt_tasks_shown:            
    if freeRoamID != "":
        vbox:
            xminimum 80
            xmaximum 80
            ymaximum 80
            yminimum 80
            xpos 0.02
            ypos 0.86
            imagebutton:
                        
                        if chat_new_tasks:
                            idle Transform ("map_button_proximity_idle",zoom=0.5)
                            hover Transform ("mphone_app_tasks_new_hover",zoom=0.5)
                        else:
                            idle Transform ("map_button_proximity_idle",zoom=0.5)
                            hover Transform ("mphone_app_tasks_hover",zoom=0.5)
                        action [SetVariable("wt_tmp_pack_quest",0),SetVariable("wt_tmp_money",0),SetVariable("wt_tmp_rewards",0),SetVariable("chat_new_tasks",False),Hide("wt_tasks_shown"),Show("mphone_tasks_app_screen_wtmod")]
                        xalign 0.5
            #text "Tasks" style "mphone_app_text_style" xalign 0.5            
        timer 0.5 action Function(wt_check_collectible_label) repeat True    
            
screen mphone_tasks_app_screen_wtmod:
     
    modal True tag mphone_tasks_app_screen
    key "mousedown_4" action NullAction()
    key "mousedown_5" action NullAction()
    fixed:
        at mphone_app_transform
        add "mphone_tasks_app_bg"

    add "mphone_shell"

    fixed:
        at mphone_app_transform

        imagebutton at mphone_off_transform:
            idle "mphone_off_circle_idle"
            hover "mphone_off_circle_hover"
            action [SetVariable("wt_tmp_pack_quest",0),SetVariable("wt_tmp_money",0),SetVariable("wt_tmp_rewards",0),Show("wt_tasks_shown"),Hide("mphone_tasks_app_screen_wtmod")]
            xalign 0.5
            yalign mphone_off_yalign
        key "mouseup_2" action [Show("wt_tasks_shown"),Hide("mphone_tasks_app_screen_wtmod")]
        vbox:
            xalign 0.5
            yalign 0.5
            if len(task_list) > 0:
                text "Tasks" style "mphone_task_text_big_style" xalign 0.5
                $ tmpBool = False
                for x in task_list:
                    if x != "":
                        text "%s" % x style "mphone_task_text_style" xalign 0.5
                        $ tmpBool = True
                if not tmpBool:
                    if "\n" in current_task:
                        text "%s" % current_task style "mphone_task_text_style" xalign 0.5 text_align 0.5
                    else:
                        text "%s" % current_task style "mphone_task_text_style" xalign 0.5
            else:
                text "Tasks" style "mphone_task_text_big_style" xalign 0.5
                text "No tasks available" style "mphone_task_text_style" xalign 0.5

            if len(optional_task_list) > 0:
                text "Optional Tasks" style "mphone_task_text_big_style" xalign 0.5
                $ tmpBool = False
                for x in optional_task_list:
                    if x != "":
                        text "%s" % x style "mphone_task_text_style" xalign 0.5
                        $ tmpBool = True
                if not tmpBool:
                    text "No optional tasks available" style "mphone_task_text_style" xalign 0.5
            #text ""
            #textbutton "Collectibles" style "mphone_task_text_big_style" xalign 0.5 action [SetVariable("wt_tmp_money",0),SetVariable("wt_tmp_rewards",0),Show("mphone_tasks_app_screen_wtmod_collect"),Hide("mphone_tasks_app_screen_wtmod")]
            
            if True:
                text "Collectibles" style "mphone_task_text_big_style" xalign 0.5
                
                for label_name, entry in wt_collectible_data.items():
                    if freeRoamID == label_name:
                        for money in entry["money_list"]:
                            
                            if getattr(store, money["found"]) == True:
                            #if money['found'] == True:
                                $ wt_tmp_money += 1
                if wt_tmp_money > wt_collectible_data[freeRoamID]["total_money"]:
                    $ wt_tmp_money = wt_collectible_data[freeRoamID]["total_money"]
                text "Money found [wt_tmp_money]/%s"  %wt_collectible_data[freeRoamID]["total_money"] style "mphone_task_text_style" xalign 0.5
                
                for label_name, entry in wt_collectible_data.items():
                    if freeRoamID == label_name:
                        for reward in entry["rewards_list"]:
                            
                            if getattr(persistent, reward["found"]) == True:
                            #if money['found'] == True:
                                $ wt_tmp_rewards += 1
                if wt_tmp_rewards > wt_collectible_data[freeRoamID]["total_rewards"]:
                    $ wt_tmp_rewards = wt_collectible_data[freeRoamID]["total_rewards"]
                text "Rewards found [wt_tmp_rewards]/%s"  %wt_collectible_data[freeRoamID]["total_rewards"] style "mphone_task_text_style" xalign 0.5
                #if freeRoamID in wt_collectible_data:
                    #for check in
                if (freeRoamID == "ep9_4"  or freeRoamID == "ep10_5" or freeRoamID == "ep11_4" or freeRoamID =="ep12_3" or freeRoamID =="ep12_3b" or freeRoamID =="ep12_3c") and pack_quest_active: 
                    for label_name, entry in wt_collectible_data.items():
                     if freeRoamID == label_name:
                        for quest in entry["pack_list"]:
                            
                            if pack_quest_list[quest["index"]][quest["episode"]] == True:
                            #if money['found'] == True:
                                $ wt_tmp_pack_quest += 1
                    if wt_tmp_pack_quest > wt_collectible_data[freeRoamID]["pack_quest_total"]:
                              $ wt_tmp_pack_quest = wt_collectible_data[freeRoamID]["pack_quest_total"]        
                    text "Pack quest found [wt_tmp_pack_quest]/%s"  %wt_collectible_data[freeRoamID]["pack_quest_total"] style "mphone_task_text_style" xalign 0.5
                #text "Rewards found" style "mphone_task_text_style" xalign 0.5
                        
            text ""
            textbutton "HELP" style "mphone_task_text_big_style" xalign 0.5 action [Show("mphone_tasks_app_screen_wtmod_help"),Hide("mphone_tasks_app_screen_wtmod")]
        add "mphone_fg"
    
    
default wt_tmp_money=0
default wt_tmp_rewards=0
default wt_tmp_pack_quest=0    

        
screen mphone_tasks_app_screen_wtmod_help:
    
    modal True tag mphone_tasks_app_screen
    key "mousedown_4" action NullAction()
    key "mousedown_5" action NullAction()
    fixed:
        at mphone_app_transform
        add "mphone_tasks_app_bg"

    add "mphone_shell"

    fixed:
        at mphone_app_transform

        imagebutton at mphone_off_transform:
            idle "mphone_off_circle_idle"
            hover "mphone_off_circle_hover"
            action [SetVariable("wt_tmp_pack_quest",0),SetVariable("wt_tmp_money",0),SetVariable("wt_tmp_rewards",0),Show("mphone_tasks_app_screen_wtmod"),Hide("mphone_tasks_app_screen_wtmod_help")]
            xalign 0.5
            yalign mphone_off_yalign
        key "mouseup_2" action [SetVariable("wt_tmp_pack_quest",0),SetVariable("wt_tmp_money",0),SetVariable("wt_tmp_rewards",0),Show("mphone_tasks_app_screen_wtmod"),Hide("mphone_tasks_app_screen_wtmod_help")]
        vbox:
            xalign 0.5
            yalign 0.5
            if True:
                text "HELP" style "mphone_task_text_big_style" xalign 0.5
                
                #for label_name, entry in wt_collectible_data.items():
                #    if freeRoamID in label_name:
                #        for money in entry["money_list"]:
                            
                            #if getattr(store, money["found"]) == True:
                            #if money['found'] != True:
                                #$ wt_tmp_money += 1
                                #text "Money found [wt_tmp_money]/%s"  %wt_collectible_data[freeRoamID]["money_list"]['name'] style "mphone_task_text_style" xalign 0.5
                
                    #for check in
                
                for label_name, entry in wt_collectible_data.items():
                     if freeRoamID in label_name:
                          if freeRoamID == label_name:
                             if wt_collectible_data[freeRoamID]["total_money"] != wt_tmp_money:
                                text "Money locations:" style "mphone_task_text_big_style" xalign 0.5
                                for money in entry["money_list"]:                                 
                                    if getattr(store, money["found"]) != True:
                                    
                                        text "%s" %money['name'] style "mphone_task_text_style" xalign 0.5
                             if wt_collectible_data[freeRoamID]["total_rewards"] != wt_tmp_rewards:
                                text "Rewards locations:" style "mphone_task_text_big_style" xalign 0.5
                                for reward in entry["rewards_list"]:                                 
                                    if getattr(persistent, reward["found"]) != True:
                                    
                                        text "%s" %reward['name'] style "mphone_task_text_style" xalign 0.5
                             if (freeRoamID == "ep9_4"  or freeRoamID == "ep10_5" or freeRoamID == "ep11_4" or freeRoamID =="ep12_3" or freeRoamID =="ep12_3b" or freeRoamID =="ep12_3c") and pack_quest_active: 
                                    text "Pack quest locations:" style "mphone_task_text_big_style" xalign 0.5
                                    for quest in entry["pack_list"]:
                                    #for quest in entry["pack_list"]:
                            
                                        if pack_quest_list[quest["index"]][quest["episode"]] != True:
                                             text "%s" %quest['name'] style "mphone_task_text_style" xalign 0.5
                                        
                                        
                            
                #text "Rewards found" style "mphone_task_text_style" xalign 0.5
                        
              
            

        add "mphone_fg"

screen wt_collect_help_circle (xar=0,yar=0):
    image "cheats/collect_circle.png":
       #idle "cheats/collect_circle.png"
       xpos xar
       ypos yar
       
    timer 1 action Hide("wt_collect_help_circle")
    
init python:
    def wt_check_collectible_label():
        global wt_collectible_data,freeRoamID,currentFreeRoamLabel
        global pack_quest_list,pack_quest_active
        tmp_x=tmp_y=0
        if persistent.wt_collectible_notify or persistent.wt_collectible_circle:
            for label_name, entry in wt_collectible_data.items():
                 if freeRoamID in label_name:
                       if freeRoamID == label_name:
                                                             
                              for money in entry["money_list"]:                                 
                                        if getattr(store, money["found"]) != True and money['var'] == currentFreeRoamLabel:
                                            if not renpy.get_screen("notify") and persistent.wt_collectible_notify:
                                                 renpy.notify("Money collectible on screen")
                                            if not renpy.get_screen("wt_collect_help_circle") and persistent.wt_collectible_circle:
                                                  tmp_x = money['posx']
                                                  tmp_y = money['posy']
                                                  renpy.show_screen("wt_collect_help_circle", xar=tmp_x, yar=tmp_y)
                                                  
                              for reward in entry["rewards_list"]:                                 
                                        if getattr(persistent, reward["found"]) != True and reward['var'] == currentFreeRoamLabel:
                                            if not renpy.get_screen("notify") and persistent.wt_collectible_notify:
                                                 renpy.notify("Special render collectible on screen")
                                            if not renpy.get_screen("wt_collect_help_circle") and persistent.wt_collectible_circle:
                                                  tmp_x = reward['posx']
                                                  tmp_y = reward['posy']
                                                  renpy.show_screen("wt_collect_help_circle", xar=tmp_x, yar=tmp_y)
                              if (freeRoamID == "ep9_4" or freeRoamID == "ep10_5" or freeRoamID == "ep11_4" or freeRoamID =="ep12_3" or freeRoamID =="ep12_3b" or freeRoamID =="ep12_3c") and pack_quest_active: 
                                
                                    for quest in entry["pack_list"]:
                                        
                                        if pack_quest_list[quest["index"]][quest["episode"]] != True  and quest['var'] == currentFreeRoamLabel:
                                            if not renpy.get_screen("notify") and persistent.wt_collectible_notify:
                                                 renpy.notify("Pack quest collectible on screen")
                                            if not renpy.get_screen("wt_collect_help_circle") and persistent.wt_collectible_circle:
                                                  tmp_x = quest['posx']
                                                  tmp_y = quest['posy']
                                                  renpy.show_screen("wt_collect_help_circle", xar=tmp_x, yar=tmp_y)
                                        
        
        
#default wt_last_label = "" 
#default freeRoamID=""       
#init python:

   #def on_label_name(name,abnormal):
   #     global freeRoamID
   #     if not name.startswith("_") and freeRoamID != "":  # 
   #         store.wt_last_label = name
   #config.label_callback = on_label_name 

default found_money=False
default found_money2=False  #POS X ANY POS Y REDUCE BY 80
default wt_collectible_data = {
    "ep9_1": {
        "total_money": 2,
        "money_list": [
            {"posx": 871 , "posy" : 826 , "found": "found_money", "var": "ep9_diks_ph1_main_label" , "name" : "Main party room" },
            {"posx": 520 , "posy" : 548 , "found": "found_money2", "var": "ep9_diks_ph1_theater2_label" , "name" : "Theater" },
        ],
        "total_rewards": 16,
        "rewards_list": [
            {"posx": 473 , "posy" : 448 , "found": "ep9_cardjo4" , "var": "ep9_diks_ph1_jamie_label" , "name" : "Jamie's room" },
            {"posx": 76 , "posy" : 598 , "found": "ep9_cardjo14" , "var": "ep9_diks_ph1_tommy2_label" , "name" : "Tommy's room" },
            {"posx": 1016 , "posy" : 484 , "found": "ep9_cardjo13" , "var": "ep9_diks_ph1_tommy_label" , "name" : "Tommy's room" },
            {"posx": 202 , "posy" : 700 , "found": "ep9_cardjo3" , "var": "ep9_diks_ph1_jacob_label" , "name" : "Jacob's room" },
            {"posx": 306 , "posy" : 493 , "found": "ep9_cardjo9" , "var": "ep9_diks_ph1_nick_label" , "name" : "Nick's room" },
            {"posx": 1009 , "posy" : 423 , "found": "ep9_cardjo5" , "var": "ep9_diks_ph1_jb_label" , "name" : "John Boy's room" },
            {"posx": 162 , "posy" : 468 , "found": "ep9_cardjo6" , "var": "ep9_diks_ph1_kitchen_label" , "name" : "Kitchen" },
            {"posx": 891 , "posy" : 396 , "found": "ep9_cardjo16" , "var": "ep9_diks_ph1_upper_2dining_label" , "name" : "Dining room upstairs" },
            {"posx": 973 , "posy" : -35 , "found": "ep9_cardjo2" , "var": "ep9_diks_ph1_bathroom_label" , "name" : "Right hallway bathroom" },
            {"posx": 406 , "posy" : 560 , "found": "ep9_cardjo12" , "var": "ep9_diks_ph1_toilet_2nd_label" , "name" : "Upstairs bathroom" },
            {"posx": 1773 , "posy" : 680 , "found": "ep9_cardjo7" , "var": "ep9_diks_ph1_leon_room_label" , "name" : "Leon's room" },
            {"posx": 1783 , "posy" : 580 , "found": "ep9_cardjo11" , "var": "ep9_diks_ph1_theater_label" , "name" : "Theater" },
            {"posx": 570 , "posy" : 457 , "found": "ep9_cardjo10" , "var": "ep9_diks_ph1_rusty_room_label" , "name" : "Rusty's room" },
            {"posx": 735 , "posy" : 27 , "found": "ep9_cardjo1" , "var": "ep9_diks_ph1_2ua_label" , "name" : "Upper main room" },
            {"posx": 22 , "posy" : 680 , "found": "ep9_cardjo15" , "var": "ep9_diks_ph1_ua_label" , "name" : "Upper main room" },
            {"posx": 1515 , "posy" : 550 , "found": "ep9_cardjo8" , "var": "ep9_diks_ph1_lib_right_label" , "name" : "My room" },
        ],
    },
    
    "ep9_2": {
        "total_money": 1,
        "money_list": [
            {"posx": 762 , "posy" : 429 , "found": "found_money", "var": "ep9_diks_ph2_tommy2_label" , "name" : "Tommy's room" },
        ],
        "total_rewards": 4,
        "rewards_list": [
            {"posx": 1801 , "posy" : 655 , "found": "ep9_cardji4" , "var": "ep9_diks_ph2_tommy2_label" , "name" : "Tommy's room" },
            {"posx": 1330 , "posy" : 385 , "found": "ep9_cardji2" , "var": "ep9_diks_ph2_jacob_label" , "name" : "Jacob's room" },
            {"posx": 650 , "posy" : 860 , "found": "ep9_cardji1" , "var": "ep9_diks_ph2_dining_label" , "name" : "Dining room" },
            {"posx": 1800 , "posy" : 160 , "found": "ep9_cardji3" , "var": "ep9_diks_ph2_table_label" , "name" : "Right Hallway - food table" },
            
        ],
    },
    "ep9_4": {
        "total_money": 1,
        "money_list": [
            {"posx": 765 , "posy" : 726 , "found": "found_money", "var": "ep9_diks_ph3_mainup_label" , "name" : "Main party room upstairs" },
        ],
        "total_rewards": 3,
        "rewards_list": [
            {"posx": 920 , "posy" : 370 , "found": "ep9_cardji14" , "var": "ep9_diks_ph3_left_hall_label" , "name" : "Left hallway (Door to Rusty's room)" },
            {"posx": 915 , "posy" : 530 , "found": "ep9_cardji13" , "var": "ep9_final_diks_porch_label" , "name" : "Porch (from left hallway)" },
            {"posx": 745 , "posy" : 365 , "found": "ep9_cardji15" , "var": "ep9_diks_ph3_leon_room_label" , "name" : "Leon's room" },
        ],
        "pack_quest_total": 10,
        "pack_list": [
            {"posx": 695 , "posy" : 38 , "episode": 1 , "index" : 0, "var": "ep9_diks_ph3_main_label" , "name" : "Main party room" },
            {"posx": 814 , "posy" : 5 , "episode": 1 , "index" : 5, "var": "ep9_diks_ph3_2ua_label" , "name" : "Upper main room" },
            {"posx": 435 , "posy" : 320 , "episode": 1 , "index" : 9, "var": "ep9_diks_ph3_derek_label" , "name" : "Derek's room" },
            {"posx": 1030 , "posy" : 715 , "episode": 1 , "index" : 8, "var": "ep9_final_diks_porch_label" , "name" : "Porch" },
            {"posx": 1370 , "posy" : 506 , "episode": 1 , "index" : 3, "var": "ep9_diks_ph3_rusty_room_label" , "name" : "Rusty's room" },
            {"posx": 1511 , "posy" : 784 , "episode": 1 , "index" : 4, "var": "ep9_diks_ph3_leon_room_label" , "name" : "Leon's room" },
            {"posx": 748 , "posy" : 460 , "episode": 1 , "index" : 1, "var": "ep9_diks_ph3_toilet_2nd_label" , "name" : "Upstairs bathroom" },
            {"posx": 584 , "posy" : 550 , "episode": 1 , "index" : 7, "var": "ep9_diks_ph3_nick_label" , "name" : "Nick's room" },
            {"posx": 1770 , "posy" : 540 , "episode": 1 , "index" : 2, "var": "ep9_diks_ph3_tommy2_label" , "name" : "Tommy's room" },
            {"posx": 155 , "posy" : 695 , "episode": 1 , "index" : 6, "var": "ep9_diks_ph3_jamie_label" , "name" : "Jamie's room" },
            
        ],
    },
    "ep10_1": {
        "total_money": 2,
        "money_list": [
            {"posx": 1320 , "posy" : 560 , "found": "found_money", "var": "ep10_diks_fr1_jb_label" , "name" : "John Boy's room" },
            {"posx": 1257 , "posy" : 757 , "found": "found_money2", "var": "ep10_diks_fr1_rusty_room_label" , "name" : "Rusty's room" },
        ],
        "total_rewards": 4,
        "rewards_list": [
            {"posx": 1603 , "posy" : 667 , "found": "ep10_cardsa1" , "var": "ep10_diks_fr1_roof_label" , "name" : "On the roof" },
            {"posx": 70 , "posy" : 634 , "found": "ep10_cardsa2" , "var": "ep10_diks_fr1_outdoors_label" , "name" : "Outside the DIKs mansion" },
            {"posx": 760 , "posy" : 613 , "found": "ep10_cardsa3" , "var": "ep10_diks_fr1_2ua_label" , "name" : "Upper main room" },
            {"posx": -69 , "posy" : 680 , "found": "ep10_cardsa4" , "var": "ep10_diks_fr1_rusty_room_label" , "name" : "Rusty's room" },
            
        ],
    },
    "ep10_2": {
        "total_money": 1,
        "money_list": [
            {"posx": 910 , "posy" : 673 , "found": "found_money", "var": "ep10_diks_fr2_lib_right_label" , "name" : "Under table" },
        ],
        "total_rewards": 0,
        "rewards_list": [
            {"posx": 0 , "posy" : 0 , "found": " " , "var": " " , "name" : " " },
            
        ],
    },
    "ep10_3": {
        "total_money": 2,
        "money_list": [
            {"posx": 70 , "posy" : 440 , "found": "found_money", "var": "ep10_bbq_tent_label" , "name" : "Inside the tent" },
            {"posx": 1633 , "posy" : 380 , "found": "found_money2", "var": "ep10_bbq_diks_table_label" , "name" : "Table with DIKs/Zoey" },
        ],
        "total_rewards": 3,
        "rewards_list": [
            {"posx": 260 , "posy" : 600 , "found": "ep10_cardsa5" , "var": "ep10_bbq_hots_label" , "name" : "Tables with HOTS" },
            {"posx": 1245 , "posy" : 528 , "found": "ep10_cardsa6" , "var": "ep10_bbq_bathroom_label" , "name" : "Path to bathrooms" },
            {"posx": 394 , "posy" : 702 , "found": "ep10_cardsa7" , "var": "ep10_bbq_forest_label" , "name" : "Forest before the lake" },
            
        ],
    },
    "ep10_4": {
        "total_money": 2,
        "money_list": [
            {"posx": 1318 , "posy" : 478 , "found": "found_money", "var": "ep10_diks2_fr2_lib_right_label" , "name" : "Right side of the room" },
            {"posx": 852 , "posy" : 580 , "found": "found_money2", "var": "ep10_diks2_fr2_lib_down_label" , "name" : "Seat (Go down from the bed)" },
        ],
        "total_rewards": 2,
        "rewards_list": [
            {"posx": 360 , "posy" : 600 , "found": "ep10_cardsa8" , "var": "ep10_diks2_fr2_lib_down_label" , "name" : "Seat (Go down from the bed)" },
            {"posx": 190 , "posy" : 310 , "found": "ep10_cardsa9" , "var": "ep10_diks2_fr2_lib_left_label" , "name" : "Left side of the room - Bookshelf" },
            
            
        ],
    },
    "ep10_5": {
        "total_money": 2,
        "money_list": [
            {"posx": 954 , "posy" : 436 , "found": "found_money", "var": "ep10_fr_tg_main_cabinet_label" , "name" : "Cabinet in main hall" },
            {"posx": 543 , "posy" : 190 , "found": "found_money2", "var": "ep10_fr_tg_maya_room_left_label" , "name" : "Maya's room" },
        ],
        "total_rewards": 7,
        "rewards_list": [
            {"posx": 1340 , "posy" : 393 , "found": "ep10_cardzo11" , "var": "ep10_fr_tg_office_left_label" , "name" : "Office - left side" },
            {"posx": 980 , "posy" : 552 , "found": "ep10_cardzo10" , "var": "ep10_fr_tg_office_shelf_6_label" , "name" : "Office - one of the drawers" },
            {"posx": 390 , "posy" : 258 , "found": "ep10_cardzo9" , "var": "ep10_fr_tg_derek_room_left_label" , "name" : "Derek's room" },
            {"posx": 1083 , "posy" : 472 , "found": "ep10_cardzo12" , "var": "ep10_fr_tg_livingroom_label" , "name" : "Living room" },
            {"posx": 720 , "posy" : 84 , "found": "ep10_cardsa12" , "var": "ep10_fr_tg_main_cabinet_label" , "name" : "Cabinet in main hall" },
            {"posx": 703 , "posy" : 657 , "found": "ep10_cardsa11" , "var": "ep10_fr_tg_main_table_label" , "name" : "Table in main hall" },
            {"posx": 280 , "posy" : 610 , "found": "ep10_cardsa10" , "var": "ep10_fr_tg_main_halld_label" , "name" : "Main Hall - Entrance" },
        ],
        "pack_quest_total": 10,
        "pack_list": [
            {"posx": 808 , "posy" : 148 , "episode": 1 , "index" : 1, "var": "ep10_fr_tg_main_hall_label" , "name" : "Main Hall" },
            {"posx": 840 , "posy" : 155 , "episode": 1 , "index" : 6, "var": "ep10_fr_tg_main_table_label" , "name" : "Main Hall - table" },
            {"posx": 578 , "posy" : 142 , "episode": 1 , "index" : 8, "var": "ep10_fr_tg_main_cabinet_label" , "name" : "Cabinet in main hall" },
            {"posx": 1052 , "posy" : 104 , "episode": 1 , "index" : 0, "var": "ep10_fr_tg_garage_label" , "name" : "Garage" },
            {"posx": 1084 , "posy" :470  , "episode": 1 , "index" : 9, "var": "ep10_fr_tg_livingroom_label" , "name" : "Living room" },
            {"posx": 960 , "posy" :280  , "episode": 1 , "index" : 7, "var": "ep10_fr_tg_kitchen_label" , "name" : "Kithchen" },
            {"posx": 860 , "posy" : 420  , "episode": 1 , "index" : 4, "var": "ep10_fr_tg_bedroom_label" , "name" : "Parent's bedroom" },
            {"posx": 1346 , "posy" : 490  , "episode": 1 , "index" : 3, "var": "ep10_fr_tg_bathroom_label" , "name" : "Bathroom" },
            {"posx": 800 , "posy" : 335  , "episode": 1 , "index" : 5, "var": "ep10_fr_tg_derek_room_left_label" , "name" : "Derek's room" },
            {"posx": 1007 , "posy" : 660  , "episode": 1 , "index" : 2, "var": "ep10_fr_tg_maya_room_right_label" , "name" : "Maya's room" },
            
        ],
    },
    "ep11_1": {
        "total_money": 2,
        "money_list": [           
            {"posx": 920 , "posy" : 670 , "found": "found_money", "var": "ep11_diks2_fr2_lib_right_label" , "name" : "Right side of the room" },
            {"posx": 410 , "posy" : 500 , "found": "found_money2", "var": "ep11_diks2_fr2_lib_down_label" , "name" : "Seat (Go down from the bed)" },
        ],
        "total_rewards": 0,
        "rewards_list": [
            {"posx": 0 , "posy" : 0 , "found": " " , "var": " " , "name" : " " },
        ],
    },
    "ep11_2": {
        "total_money": 2,
        "money_list": [
            {"posx": 580 , "posy" : 856 , "found": "found_money", "var": "ep11_hots_fr1_lobby_label" , "name" : "HOTS's hallway" },
            {"posx": 746 , "posy" : 452 , "found": "found_money2", "var": "ep11_diks_fr1_derek_label" , "name" : "Derek's room" },
        ],
        "total_rewards": 1,
        "rewards_list": [
            {"posx": 1030 , "posy" :  680, "found": "ep11_cardmy1" , "var": "ep11_diks_fr1_2ua_label" , "name" : "Upper main room" },
            
        ],
    },
    "ep11_3": {
        "total_money": 0,
        "money_list": [
            {"posx": 128 , "posy" : 490 , "found": "found_money", "var": "ep12_np_locker_room_label" , "name" : "Locker room" },
            
            
        ],
        "total_rewards": 0,
        "rewards_list": [
            {"posx": 914 , "posy" :  823, "found": "ep12_cardisa3" , "var": "ep12_np_dining_label" , "name" : "Dining room" },
           
            
            
        ],
       
        
    },
    "ep11_4": {
        "total_money": 2,
        "money_list": [
            {"posx": 990 , "posy" : 482 , "found": "found_money", "var": "ep11_diks_pp_nick_label" , "name" : "Nick's room" },
            {"posx": 1435 , "posy" : 550 , "found": "found_money2", "var": "ep11_diks_pp_porch_label" , "name" : "Porch  (from left hallway)" },
        ],
        "total_rewards": 11,
        "rewards_list": [
            {"posx": 1438 , "posy" :  787, "found": "ep11_cardmy20" , "var": "ep11_diks4_fr2_lib_mid_label" , "name" : "My room" },
            {"posx": 1664 , "posy" :  470, "found": "ep11_cardly15" , "var": "ep11_diks4_fr2_lib_right_label" , "name" : "My room - right side" },
            {"posx": 1700 , "posy" :  307, "found": "ep11_cardly19" , "var": "ep11_diks_pp_mainb_label" , "name" : "Main party room - right side" },
            {"posx": 1375 , "posy" :  470, "found": "ep11_cardmy17" , "var": "ep11_diks_pp_ua_label" , "name" : "Upper main room" },
            {"posx": 1282 , "posy" :  350, "found": "ep11_cardmy18" , "var": "ep11_diks_pp_derek_label" , "name" : "Derek's room" },
            {"posx": 1680 , "posy" :  578, "found": "ep11_cardly20" , "var": "ep11_diks_pp_rusty_room_label" , "name" : "Rusty's room" },
            {"posx": 1800 , "posy" :  570, "found": "ep11_cardly16" , "var": "ep11_diks_pp_theater_label" , "name" : "Theater" },
            {"posx": 1550 , "posy" :  524, "found": "ep11_cardmy16" , "var": "ep11_diks_pp_leon_room_label" , "name" : "Leon's room" },
            {"posx": 86 , "posy" :  464, "found": "ep11_cardmy19" , "var": "ep11_diks_pp_kitchen_label" , "name" : "Kitchen" },
            {"posx": 1020 , "posy" :  420, "found": "ep11_cardly18" , "var": "ep11_diks_pp_jb_label" , "name" : "John Boy's room" },
            {"posx": 103 , "posy" :  680, "found": "ep11_cardly17" , "var": "ep11_diks_pp_jacob_label" , "name" : "Jacob's room" },
            
        ],
        "pack_quest_total": 10,
        "pack_list": [
            {"posx": 1474 , "posy" : 247 , "episode": 1 , "index" : 0, "var": "ep11_diks4_fr2_lib_right_label" , "name" : "My room - right side" },
            {"posx": 808 , "posy" : 530 , "episode": 1 , "index" : 8, "var": "ep11_diks_pp_main_label" , "name" : "Main party room" },
            {"posx": 665 , "posy" : 720 , "episode": 1 , "index" : 6, "var": "ep11_diks_pp_ua_label" , "name" : "Upper main room" },
            {"posx": 260 , "posy" : 680 , "episode": 1 , "index" : 2, "var": "ep11_diks_pp_porch_label" , "name" : "Porch" },
            {"posx": 1027 , "posy" :233  , "episode": 1 , "index" : 7, "var": "ep11_diks3_fr2_table_label" , "name" : "Right hallway - table" },
            {"posx": 962 , "posy" :263  , "episode": 1 , "index" : 3, "var": "ep11_diks_pp_toilet_2nd_label" , "name" : "Upstairs bathroom" },
            {"posx": 1361 , "posy" : 275  , "episode": 1 , "index" : 1, "var": "ep11_diks_pp_bathroom_label" , "name" : "Bathroom" },
            {"posx": 1621 , "posy" : 430  , "episode": 1 , "index" : 4, "var": "ep11_diks_pp_jb_label" , "name" : "John Boy's room" },
            {"posx": 1760 , "posy" : 565  , "episode": 1 , "index" : 9, "var": "ep11_diks_pp_tommy_label" , "name" : "Tommy's room" },
            {"posx": 1720 , "posy" : 693  , "episode": 1 , "index" : 5, "var": "ep11_diks_pp_jamie_label" , "name" : "Jamie's room" },
            
        ],
    },
    "ep11_4b": {
        "total_money": 2,
        "money_list": [
            {"posx": 990 , "posy" : 482 , "found": "found_money", "var": "ep11_diks_pp_nick_label" , "name" : "Nick's room" },
            {"posx": 1435 , "posy" : 550 , "found": "found_money2", "var": "ep11_diks_pp_porch_label" , "name" : "Porch  (from left hallway)" },
        ],
        "total_rewards": 11,
        "rewards_list": [
            {"posx": 1438 , "posy" :  787, "found": "ep11_cardmy20" , "var": "ep11_diks4_fr2_lib_mid_label" , "name" : "My room" },
            {"posx": 1664 , "posy" :  470, "found": "ep11_cardly15" , "var": "ep11_diks4_fr2_lib_right_label" , "name" : "My room - right side" },
            {"posx": 1700 , "posy" :  307, "found": "ep11_cardly19" , "var": "ep11_diks_pp_mainb_label" , "name" : "Main party room - right side" },
            {"posx": 1375 , "posy" :  470, "found": "ep11_cardmy17" , "var": "ep11_diks_pp_ua_label" , "name" : "Upper main room" },
            {"posx": 1282 , "posy" :  350, "found": "ep11_cardmy18" , "var": "ep11_diks_pp_derek_label" , "name" : "Derek's room" },
            {"posx": 1680 , "posy" :  578, "found": "ep11_cardly20" , "var": "ep11_diks_pp_rusty_room_label" , "name" : "Rusty's room" },
            {"posx": 1800 , "posy" :  570, "found": "ep11_cardly16" , "var": "ep11_diks_pp_theater_label" , "name" : "Theater" },
            {"posx": 1550 , "posy" :  524, "found": "ep11_cardmy16" , "var": "ep11_diks_pp_leon_room_label" , "name" : "Leon's room" },
            {"posx": 86 , "posy" :  464, "found": "ep11_cardmy19" , "var": "ep11_diks_pp_kitchen_label" , "name" : "Kitchen" },
            {"posx": 1020 , "posy" :  420, "found": "ep11_cardly18" , "var": "ep11_diks_pp_jb_label" , "name" : "John Boy's room" },
            {"posx": 103 , "posy" :  680, "found": "ep11_cardly17" , "var": "ep11_diks_pp_jacob_label" , "name" : "Jacob's room" },
            
        ],
        "pack_quest_total": 10,
        "pack_list": [
            {"posx": 1474 , "posy" : 247 , "episode": 1 , "index" : 0, "var": "ep11_diks4_fr2_lib_right_label" , "name" : "My room - right side" },
            {"posx": 808 , "posy" : 530 , "episode": 1 , "index" : 8, "var": "ep11_diks_pp_main_label" , "name" : "Main party room" },
            {"posx": 665 , "posy" : 720 , "episode": 1 , "index" : 6, "var": "ep11_diks_pp_ua_label" , "name" : "Upper main room" },
            {"posx": 260 , "posy" : 680 , "episode": 1 , "index" : 2, "var": "ep11_diks_pp_porch_label" , "name" : "Porch" },
            {"posx": 1027 , "posy" :233  , "episode": 1 , "index" : 7, "var": "ep11_diks3_fr2_table_label" , "name" : "Right hallway - table" },
            {"posx": 962 , "posy" :263  , "episode": 1 , "index" : 3, "var": "ep11_diks_pp_toilet_2nd_label" , "name" : "Upstairs bathroom" },
            {"posx": 1361 , "posy" : 275  , "episode": 1 , "index" : 1, "var": "ep11_diks_pp_bathroom_label" , "name" : "Bathroom" },
            {"posx": 1621 , "posy" : 430  , "episode": 1 , "index" : 4, "var": "ep11_diks_pp_jb_label" , "name" : "John Boy's room" },
            {"posx": 1760 , "posy" : 565  , "episode": 1 , "index" : 9, "var": "ep11_diks_pp_tommy_label" , "name" : "Tommy's room" },
            {"posx": 1720 , "posy" : 693  , "episode": 1 , "index" : 5, "var": "ep11_diks_pp_jamie_label" , "name" : "Jamie's room" },
            
        ],
    },
    "ep11_4c": {
        "total_money": 2,
        "money_list": [
            {"posx": 990 , "posy" : 482 , "found": "found_money", "var": "ep11_diks_pp_nick_label" , "name" : "Nick's room" },
            {"posx": 1435 , "posy" : 550 , "found": "found_money2", "var": "ep11_diks_pp_porch_label" , "name" : "Porch  (from left hallway)" },
        ],
        "total_rewards": 11,
        "rewards_list": [
            {"posx": 1438 , "posy" :  787, "found": "ep11_cardmy20" , "var": "ep11_diks4_fr2_lib_mid_label" , "name" : "My room" },
            {"posx": 1664 , "posy" :  470, "found": "ep11_cardly15" , "var": "ep11_diks4_fr2_lib_right_label" , "name" : "My room - right side" },
            {"posx": 1700 , "posy" :  307, "found": "ep11_cardly19" , "var": "ep11_diks_pp_mainb_label" , "name" : "Main party room - right side" },
            {"posx": 1375 , "posy" :  470, "found": "ep11_cardmy17" , "var": "ep11_diks_pp_ua_label" , "name" : "Upper main room" },
            {"posx": 1282 , "posy" :  350, "found": "ep11_cardmy18" , "var": "ep11_diks_pp_derek_label" , "name" : "Derek's room" },
            {"posx": 1680 , "posy" :  578, "found": "ep11_cardly20" , "var": "ep11_diks_pp_rusty_room_label" , "name" : "Rusty's room" },
            {"posx": 1800 , "posy" :  570, "found": "ep11_cardly16" , "var": "ep11_diks_pp_theater_label" , "name" : "Theater" },
            {"posx": 1550 , "posy" :  524, "found": "ep11_cardmy16" , "var": "ep11_diks_pp_leon_room_label" , "name" : "Leon's room" },
            {"posx": 86 , "posy" :  464, "found": "ep11_cardmy19" , "var": "ep11_diks_pp_kitchen_label" , "name" : "Kitchen" },
            {"posx": 1020 , "posy" :  420, "found": "ep11_cardly18" , "var": "ep11_diks_pp_jb_label" , "name" : "John Boy's room" },
            {"posx": 103 , "posy" :  680, "found": "ep11_cardly17" , "var": "ep11_diks_pp_jacob_label" , "name" : "Jacob's room" },
            
        ],
        "pack_quest_total": 10,
        "pack_list": [
            {"posx": 1474 , "posy" : 247 , "episode": 1 , "index" : 0, "var": "ep11_diks4_fr2_lib_right_label" , "name" : "My room - right side" },
            {"posx": 808 , "posy" : 530 , "episode": 1 , "index" : 8, "var": "ep11_diks_pp_main_label" , "name" : "Main party room" },
            {"posx": 665 , "posy" : 720 , "episode": 1 , "index" : 6, "var": "ep11_diks_pp_ua_label" , "name" : "Upper main room" },
            {"posx": 260 , "posy" : 680 , "episode": 1 , "index" : 2, "var": "ep11_diks_pp_porch_label" , "name" : "Porch" },
            {"posx": 1027 , "posy" :233  , "episode": 1 , "index" : 7, "var": "ep11_diks3_fr2_table_label" , "name" : "Right hallway - table" },
            {"posx": 962 , "posy" :263  , "episode": 1 , "index" : 3, "var": "ep11_diks_pp_toilet_2nd_label" , "name" : "Upstairs bathroom" },
            {"posx": 1361 , "posy" : 275  , "episode": 1 , "index" : 1, "var": "ep11_diks_pp_bathroom_label" , "name" : "Bathroom" },
            {"posx": 1621 , "posy" : 430  , "episode": 1 , "index" : 4, "var": "ep11_diks_pp_jb_label" , "name" : "John Boy's room" },
            {"posx": 1760 , "posy" : 565  , "episode": 1 , "index" : 9, "var": "ep11_diks_pp_tommy_label" , "name" : "Tommy's room" },
            {"posx": 1720 , "posy" : 693  , "episode": 1 , "index" : 5, "var": "ep11_diks_pp_jamie_label" , "name" : "Jamie's room" },
            
        ],
    },
    "ep11_5": {
        "total_money": 0,
        "money_list": [
            {"posx": 128 , "posy" : 490 , "found": "found_money", "var": "ep12_np_locker_room_label" , "name" : "Locker room" },
            
            
        ],
        "total_rewards": 0,
        "rewards_list": [
            {"posx": 914 , "posy" :  823, "found": "ep12_cardisa3" , "var": "ep12_np_dining_label" , "name" : "Dining room" },
           
            
            
        ],
       
        
    },
    "ep12_1": {
        "total_money": 1,
        "money_list": [
            {"posx": 1676 , "posy" : 595 , "found": "found_money", "var": "ep12_diks2_fr1_lib_down_label" , "name" : "Seat (Go down from the bed)" },
            
        ],
        "total_rewards": 1,
        "rewards_list": [
            {"posx": 343 , "posy" :  570, "found": "ep12_cardisa1" , "var": "ep12_diks2_fr1_lib_down_label" , "name" : "Seat (Go down from the bed)" },
            
            
        ],
        
    },
    "ep12_2": {
        "total_money": 1,
        "money_list": [
            {"posx": 1076 , "posy" : 700 , "found": "found_money", "var": "ep12_diks2_fr2_lib_left_label" , "name" : "Left side of the room" },
            
        ],
        "total_rewards": 0,
        "rewards_list": [
            {"posx": 343 , "posy" :  570, "found": "" , "var": "" , "name" : "" },
            
            
        ],
        
    },
    "ep12_3": {
        "total_money": 2,
        "money_list": [
            {"posx": 128 , "posy" : 490 , "found": "found_money", "var": "ep12_np_locker_room_label" , "name" : "Locker room" },
            #{"posx": 1160 , "posy" : 660 , "found": "found_money2", "var": "ep12_np_stall_label" , "name" : "Bathroom stall" },
            
        ],
        "total_rewards": 11,
        "rewards_list": [
            {"posx": 914 , "posy" :  823, "found": "ep12_cardisa3" , "var": "ep12_np_dining_label" , "name" : "Dining room" },
            {"posx": 1350 , "posy" :  685, "found": "ep12_cardisa2" , "var": "ep12_np_bathroom_label" , "name" : "Bathroom" },
            {"posx": 197 , "posy" :  715, "found": "ep12_cardisa20" , "var": "ep12_np_bathroom2_label" , "name" : "Bathroom" },
            {"posx": 1762 , "posy" :  635, "found": "ep12_cardisa4" , "var": "ep12_np_corridor_label" , "name" : "3F corridor" },
            {"posx": 1667 , "posy" :  508, "found": "ep12_cardisa7" , "var": "ep12_np_balcony2_label" , "name" : "Balcony" },
            {"posx": 1193 , "posy" :  418, "found": "ep12_cardisa8" , "var": "ep12_np_storage_right_label" , "name" : "Storage room" },
            {"posx": 1183 , "posy" :  -62, "found": "ep12_cardisa12" , "var": "ep12_np_storage_left_label" , "name" : "Storage room" },
            {"posx": 5 , "posy" :  329, "found": "ep12_cardisa17" , "var": "ep12_np_locker_room_label" , "name" : "Locker room" },
            {"posx": 587 , "posy" :  -10, "found": "ep12_cardisa19" , "var": "ep12_np_locker_room_right_label" , "name" : "Locker room - right" },
            {"posx": 290 , "posy" :  92, "found": "ep12_cardisa6" , "var": "ep12_np_party_room_dj_label" , "name" : "Dance floor - DJ" },
            {"posx": 365 , "posy" :  308, "found": "ep12_cardisa5" , "var": "ep12_np_party_balcony_label" , "name" : "Balcony" },
            
            
        ],
        "pack_quest_total": 5,
        "pack_list": [
            {"posx": 866 , "posy" : 154 , "episode": 1 , "index" : 3, "var": "ep12_np_bathroom2_label" , "name" : "Bathroom" },
            {"posx": 928 , "posy" : 181  , "episode": 1 , "index" : 8, "var": "ep12_np_storage_label" , "name" : "Storage room" },
            {"posx": 1498 , "posy" : 458  , "episode": 1 , "index" : 6, "var": "ep12_np_storage_right_label" , "name" : "Storage room - right" },
            {"posx": 1391 , "posy" : 476  , "episode": 1 , "index" : 9, "var": "ep12_np_party_balcony_label" , "name" : "Balcony" },
            {"posx": 1570 , "posy" : 745  , "episode": 1 , "index" : 5, "var": "ep12_np_locker_room_right_label" , "name" : "Locker room" },
            
        ],
        
    },
    "ep12_3b": {
        "total_money": 2,
        "money_list": [
            {"posx": 128 , "posy" : 490 , "found": "found_money", "var": "ep12_np_locker_room_label" , "name" : "Locker room" },
            {"posx": 1160 , "posy" : 660 , "found": "found_money2", "var": "ep12_np_stall_label" , "name" : "Bathroom stall" },
            
        ],
        "total_rewards": 11,
        "rewards_list": [
            {"posx": 914 , "posy" :  823, "found": "ep12_cardisa3" , "var": "ep12_np_dining_label" , "name" : "Dining room" },
            {"posx": 1350 , "posy" :  685, "found": "ep12_cardisa2" , "var": "ep12_np_bathroom_label" , "name" : "Bathroom" },
            {"posx": 197 , "posy" :  715, "found": "ep12_cardisa20" , "var": "ep12_np_bathroom2_label" , "name" : "Bathroom" },
            {"posx": 1762 , "posy" :  635, "found": "ep12_cardisa4" , "var": "ep12_np_corridor_label" , "name" : "3F corridor" },
            {"posx": 1667 , "posy" :  508, "found": "ep12_cardisa7" , "var": "ep12_np_balcony2_label" , "name" : "Balcony" },
            {"posx": 1193 , "posy" :  418, "found": "ep12_cardisa8" , "var": "ep12_np_storage_right_label" , "name" : "Storage room" },
            {"posx": 1183 , "posy" :  -62, "found": "ep12_cardisa12" , "var": "ep12_np_storage_left_label" , "name" : "Storage room" },
            {"posx": 5 , "posy" :  329, "found": "ep12_cardisa17" , "var": "ep12_np_locker_room_label" , "name" : "Locker room" },
            {"posx": 587 , "posy" :  -10, "found": "ep12_cardisa19" , "var": "ep12_np_locker_room_right_label" , "name" : "Locker room - right" },
            {"posx": 290 , "posy" :  92, "found": "ep12_cardisa6" , "var": "ep12_np_party_room_dj_label" , "name" : "Dance floor - DJ" },
            {"posx": 365 , "posy" :  308, "found": "ep12_cardisa5" , "var": "ep12_np_party_balcony_label" , "name" : "Balcony" },
            
            
        ],
        "pack_quest_total": 10,
        "pack_list": [
            {"posx": 800 , "posy" : 586 , "episode": 1 , "index" : 0, "var": "ep12_np_dining_down_label" , "name" : "Dining room" },
            {"posx": 866 , "posy" : 154 , "episode": 1 , "index" : 3, "var": "ep12_np_bathroom2_label" , "name" : "Bathroom" },
            {"posx": 562 , "posy" : 409 , "episode": 1 , "index" : 2, "var": "ep12_np_stall_label" , "name" : "Bathroom stall" },
            {"posx": 380 , "posy" : 515 , "episode": 1 , "index" : 1, "var": "ep12_np_corridor_label" , "name" : "3F corridor" },
            {"posx": 928 , "posy" : 181  , "episode": 1 , "index" : 8, "var": "ep12_np_storage_label" , "name" : "Storage room" },
            {"posx": 1498 , "posy" : 458  , "episode": 1 , "index" : 6, "var": "ep12_np_storage_right_label" , "name" : "Storage room - right" },
            {"posx": 25 , "posy" : 611  , "episode": 1 , "index" : 7, "var": "ep12_np_outside_label" , "name" : "Outside" },
            {"posx": 1573 , "posy" : -50  , "episode": 1 , "index" : 4, "var": "ep12_np_party_room_dj_label" , "name" : "Dance floor - DJ" },
            {"posx": 1391 , "posy" : 476  , "episode": 1 , "index" : 9, "var": "ep12_np_party_balcony_label" , "name" : "Balcony" },
            {"posx": 1570 , "posy" : 745  , "episode": 1 , "index" : 5, "var": "ep12_np_locker_room_right_label" , "name" : "Locker room" },
            
        ],
        
    },
    "ep12_3c": {
        "total_money": 2,
        "money_list": [
            {"posx": 128 , "posy" : 490 , "found": "found_money", "var": "ep12_np_locker_room_label" , "name" : "Locker room" },
            {"posx": 1160 , "posy" : 660 , "found": "found_money2", "var": "ep12_np_stall_label" , "name" : "Bathroom stall" },
            
        ],
        "total_rewards": 11,
        "rewards_list": [
            {"posx": 914 , "posy" :  823, "found": "ep12_cardisa3" , "var": "ep12_np_dining_label" , "name" : "Dining room" },
            {"posx": 1350 , "posy" :  685, "found": "ep12_cardisa2" , "var": "ep12_np_bathroom_label" , "name" : "Bathroom" },
            {"posx": 197 , "posy" :  715, "found": "ep12_cardisa20" , "var": "ep12_np_bathroom2_label" , "name" : "Bathroom" },
            {"posx": 1762 , "posy" :  635, "found": "ep12_cardisa4" , "var": "ep12_np_corridor_label" , "name" : "3F corridor" },
            {"posx": 1667 , "posy" :  508, "found": "ep12_cardisa7" , "var": "ep12_np_balcony2_label" , "name" : "Balcony" },
            {"posx": 1193 , "posy" :  418, "found": "ep12_cardisa8" , "var": "ep12_np_storage_right_label" , "name" : "Storage room" },
            {"posx": 1183 , "posy" :  -62, "found": "ep12_cardisa12" , "var": "ep12_np_storage_left_label" , "name" : "Storage room" },
            {"posx": 5 , "posy" :  329, "found": "ep12_cardisa17" , "var": "ep12_np_locker_room_label" , "name" : "Locker room" },
            {"posx": 587 , "posy" :  -10, "found": "ep12_cardisa19" , "var": "ep12_np_locker_room_right_label" , "name" : "Locker room - right" },
            {"posx": 290 , "posy" :  92, "found": "ep12_cardisa6" , "var": "ep12_np_party_room_dj_label" , "name" : "Dance floor - DJ" },
            {"posx": 365 , "posy" :  308, "found": "ep12_cardisa5" , "var": "ep12_np_party_balcony_label" , "name" : "Dance floor - Balcony" },
            
            
        ],
        "pack_quest_total": 10,
        "pack_list": [
            {"posx": 800 , "posy" : 586 , "episode": 1 , "index" : 0, "var": "ep12_np_dining_down_label" , "name" : "Dining room" },
            {"posx": 866 , "posy" : 154 , "episode": 1 , "index" : 3, "var": "ep12_np_bathroom2_label" , "name" : "Bathroom" },
            {"posx": 562 , "posy" : 409 , "episode": 1 , "index" : 2, "var": "ep12_np_stall_label" , "name" : "Bathroom stall" },
            {"posx": 380 , "posy" : 515 , "episode": 1 , "index" : 1, "var": "ep12_np_corridor_label" , "name" : "3F corridor" },
            {"posx": 928 , "posy" : 181  , "episode": 1 , "index" : 8, "var": "ep12_np_storage_label" , "name" : "Storage room" },
            {"posx": 1498 , "posy" : 458  , "episode": 1 , "index" : 6, "var": "ep12_np_storage_right_label" , "name" : "Storage room - right" },
            {"posx": 25 , "posy" : 611  , "episode": 1 , "index" : 7, "var": "ep12_np_outside_label" , "name" : "Outside" },
            {"posx": 1573 , "posy" : -50  , "episode": 1 , "index" : 4, "var": "ep12_np_party_room_dj_label" , "name" : "Dance floor - DJ" },
            {"posx": 1391 , "posy" : 476  , "episode": 1 , "index" : 9, "var": "ep12_np_party_balcony_label" , "name" : "Dance floor - Balcony" },
            {"posx": 1570 , "posy" : 745  , "episode": 1 , "index" : 5, "var": "ep12_np_locker_room_right_label" , "name" : "Locker room" },
            
        ],
        
    },
    "ep12_4": {
        "total_money": 0,
        "money_list": [
            {"posx": 128 , "posy" : 490 , "found": "found_money", "var": "ep12_np_locker_room_label" , "name" : "Locker room" },
            
            
        ],
        "total_rewards": 0,
        "rewards_list": [
            {"posx": 914 , "posy" :  823, "found": "ep12_cardisa3" , "var": "ep12_np_dining_label" , "name" : "Dining room" },
           
            
            
        ],
       
        
    },
   
}
   

   
label wt_ep12_midnight_control_label:
    if "Jade" in wt_ep12_midnight_kiss and "Jade" not in wt_ep12_midnight_seen:
        jump ep12_jade_lewd_label
    if "Sage" in wt_ep12_midnight_kiss and "Sage" not in wt_ep12_midnight_seen:
        jump ep12_sage_lewdb_label
    if "Riona" in wt_ep12_midnight_kiss and "Riona" not in wt_ep12_midnight_seen:
        jump wt_ep12_midnight_riona_label
    if "Quinn" in wt_ep12_midnight_kiss and "Quinn" not in wt_ep12_midnight_seen:
        jump wt_ep12_midnight_quinn_label
    if "Nicole" in wt_ep12_midnight_kiss and "Nicole" not in wt_ep12_midnight_seen:
        jump wt_ep12_midnight_nicole_label
    if "Lily" in wt_ep12_midnight_kiss and "Lily" not in wt_ep12_midnight_seen:
        jump wt_ep12_midnight_lily_label
    if "Nikita" in wt_ep12_midnight_kiss and "Nikita" not in wt_ep12_midnight_seen:
        jump wt_ep12_midnight_nikita_label
    if "Zoey" in wt_ep12_midnight_kiss and "Zoey" not in wt_ep12_midnight_seen:
        jump wt_ep12_midnight_zoey_label
    if "Sally" in wt_ep12_midnight_kiss and "Sally" not in wt_ep12_midnight_seen:
        jump wt_ep12_midnight_sally_label
    if "Sarah" in wt_ep12_midnight_kiss and "Sarah" not in wt_ep12_midnight_seen:
        jump wt_ep12_midnight_sarah_label
    if "Melanie" in wt_ep12_midnight_kiss and "Melanie" not in wt_ep12_midnight_seen:
        jump wt_ep12_midnight_melanie_label
    if "Bianca" in wt_ep12_midnight_kiss and "Bianca" not in wt_ep12_midnight_seen:
        jump wt_ep12_midnight_bianca_label
    if "Camila" in wt_ep12_midnight_kiss and "Camila" not in wt_ep12_midnight_seen:
        jump wt_ep12_midnight_camila_label
    if "Isabella" in wt_ep12_midnight_kiss and "Isabella" not in wt_ep12_midnight_seen:
        jump wt_ep12_isabella_label
    if ("Maya" in wt_ep12_midnight_kiss or "Josy" in wt_ep12_midnight_kiss or "Josy & Maya" in wt_ep12_midnight_kiss) and "MayaJosy" not in wt_ep12_midnight_seen:
        jump wt_ep12_mayajosy_label
    if "Jill" in wt_ep12_midnight_kiss and "Jill" not in wt_ep12_midnight_seen:
        jump wt_ep12_midnight_jill_label
    if "Elena" in wt_ep12_midnight_kiss and "Elena" not in wt_ep12_midnight_seen:
        jump wt_ep12_midnight_elena_label
    
    
    
    jump ep12_np2_afterny_label









