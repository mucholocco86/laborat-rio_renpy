init python:
    import datetime
    mp = MultiPersistent("BeingADIKSeason2Transfer1366998845")
    mp_steam = MultiPersistent("BeingADIKSeason2Transfer1366998846")

init:
    define mp_alignX = [0.156,0.333,0.505,0.68,0.855,0.156,0.333,0.505,0.68,0.855,0.156,0.333,0.505,0.68,0.855,0.156,0.333,0.505,0.68,0.855]
    define mp_alignY = [0.163,0.163,0.163,0.163,0.163,0.375,0.375,0.375,0.375,0.375,0.582,0.582,0.582,0.582,0.582,0.791,0.791,0.791,0.791,0.791]

style mp_text_style:
    font "fonts/candara.ttf"
    size 65 * persistent.scale_factor
    color "#fe9416"
    outlines [ (absolute(2), "#000", absolute(1), absolute(1)) ]

style mp_text_button_style:
    font "fonts/candara.ttf"
    size 65 * persistent.scale_factor
    hover_color "#fe9416"
    selected_color "#fe9416"
    color "#ffffff"
    insensitive_color "#808080"
    outlines [ (absolute(2), "#000", absolute(1), absolute(1)) ]

style mp_text_button_style2:
    font "fonts/candara.ttf"
    size 65 * persistent.scale_factor
    color "#808080"
    outlines [ (absolute(2), "#000", absolute(1), absolute(1)) ]

style mp_text_style2:
    font "fonts/candara.ttf"
    size 25 * persistent.scale_factor
    color "#fe9416"
    outlines [ (absolute(2), "#000", absolute(1), absolute(1)) ]

style mp_info_text_style:
    font "fonts/candara.ttf"
    size 24 * persistent.scale_factor
    color "#ffffff"
    outlines [ (absolute(2), "#000", absolute(1), absolute(1)) ]
    text_align 0.0

style mtransfer_data_style:
    font "fonts/candara.ttf"
    size 35 * persistent.scale_factor
    color "#ffffff"
    hover_color "#fe9416"
    outlines [ (absolute(2), "#000", absolute(1), absolute(1)) ]
    text_align 0.0

screen mp_load_info_screen:
    tag mp_load_info_screen
    modal False
    if mp_slot_hover >= 0:
        hbox:
            xminimum 277 * persistent.scale_factor
            xmaximum 277 * persistent.scale_factor
            xalign mp_alignX[mp_slot_hover]
            yalign mp_alignY[mp_slot_hover]
            if steamImport or steamConfig:
                if mp_steam.branchJill[mp_slot_hover]:
                    text "Affinity: %s \nChosen road: Jill\nDate: %s" % (mp_steam.affinity[mp_slot_hover],mp_steam.timestamp[mp_slot_hover]) style "mp_info_text_style"
                elif mp_steam.branchIsabella[mp_slot_hover]:
                    text "Affinity: %s \nChosen road: Isabella\nDate: %s" % (mp_steam.affinity[mp_slot_hover],mp_steam.timestamp[mp_slot_hover]) style "mp_info_text_style"
                elif mp_steam.branchSage[mp_slot_hover]:
                    text "Affinity: %s \nChosen road: Sage\nDate: %s" % (mp_steam.affinity[mp_slot_hover],mp_steam.timestamp[mp_slot_hover]) style "mp_info_text_style"
                elif mp_steam.branchMayaJosy[mp_slot_hover]:
                    text "Affinity: %s \nChosen road: {size=%d}Josy & Maya{/size}\nDate: %s" % (mp_steam.affinity[mp_slot_hover],(-3 * persistent.scale_factor),mp_steam.timestamp[mp_slot_hover]) style "mp_info_text_style"
                else:
                    text "Affinity: %s \nChosen road: Others\nDate: %s" % (mp_steam.affinity[mp_slot_hover],mp_steam.timestamp[mp_slot_hover]) style "mp_info_text_style"
            else:
                if mp.branchJill[mp_slot_hover]:
                    text "Affinity: %s \nChosen road: Jill\nDate: %s" % (mp.affinity[mp_slot_hover],mp.timestamp[mp_slot_hover]) style "mp_info_text_style"
                elif mp.branchIsabella[mp_slot_hover]:
                    text "Affinity: %s \nChosen road: Isabella\nDate: %s" % (mp.affinity[mp_slot_hover],mp.timestamp[mp_slot_hover]) style "mp_info_text_style"
                elif mp.branchSage[mp_slot_hover]:
                    text "Affinity: %s \nChosen road: Sage\nDate: %s" % (mp.affinity[mp_slot_hover],mp.timestamp[mp_slot_hover]) style "mp_info_text_style"
                elif mp.branchMayaJosy[mp_slot_hover]:
                    text "Affinity: %s \nChosen road: {size=%d}Josy & Maya{/size}\nDate: %s" % (mp.affinity[mp_slot_hover],(-3 * persistent.scale_factor),mp.timestamp[mp_slot_hover]) style "mp_info_text_style"
                else:
                    text "Affinity: %s \nChosen road: Others\nDate: %s" % (mp.affinity[mp_slot_hover],mp.timestamp[mp_slot_hover]) style "mp_info_text_style"

screen mp_load_screen:
    tag mp_load_screen
    modal True
    add "rewards_new_bg"
    add "spr_crp1"
    add "spr_crp2"
    add "spr_crp3"
    add "spr_crp4"
    add "spr_crp5"
    add "spr_crp6"
    add "rewards_new_fg3"
    imagebutton:
        idle "rew_x_idle"
        hover "rew_x_hover"
        action Jump("mp_exit_to_menu_label")
        xalign 0.99
        yalign 0.00

    text "Load a save from Season 2" xalign 0.1 yalign 0.0 style "mp_text_style"
    text "These are your saves from the end of Season 2. If you don't see any saves, you need to go back to Season 2 and choose which saves to transfer." xalign 0.063 yalign 0.94 text_align 0.0 style "mp_text_style2"
    text "{color=007db5}For safety reasons, you cannot delete saves from here. Please manage your saves at the end of Season 2.{/color}" xalign 0.05 yalign 0.97 text_align 0.0 style "mp_text_style2"

    if not steamConfig:
        if steamImport:
            textbutton "Loading Steam save data - Click to change source" text_style "mtransfer_data_style" action SetVariable("steamImport",not steamImport) xalign 0.87 yalign 0.02 xminimum 600 * persistent.scale_factor
        else:
            textbutton "Loading Patreon/GOG save data - Click to change source" text_style "mtransfer_data_style" action SetVariable("steamImport",not steamImport) xalign 0.87 yalign 0.02 xminimum 600 * persistent.scale_factor
    vpgrid:
        yalign 0.5
        xalign 0.5
        cols 5
        spacing 10 * persistent.scale_factor
        draggable False
        mousewheel False
        for i in range(0,20):
            vbox xalign 0.5 yalign 0.5:
                imagebutton:
                    focus_mask True
                    if steamImport or steamConfig:
                        if mp_steam.save_slot_image == None:
                            idle Transform ("mp_empty_idle")
                            hover Transform ("mp_empty_hover")
                            action NullAction()
                            hovered SetVariable("mp_slot_hover", -1)
                            unhovered SetVariable("mp_slot_hover", -1)
                        elif mp_steam.save_slot_image[i] != None:
                            idle Transform (""+mp_steam.save_slot_image[i]+"_idle")
                            hover Transform (""+mp_steam.save_slot_image[i]+"_hover")
                            action (SetVariable("mp_slot", i), Jump("mp_load_warn_label"))
                            hovered (SetVariable("mp_slot_hover", i), Show("mp_load_info_screen"))
                            unhovered (SetVariable("mp_slot_hover", -1), Hide("mp_load_info_screen"))
                        else:
                            idle Transform ("mp_empty_idle")
                            hover Transform ("mp_empty_hover")
                            action NullAction()
                            hovered SetVariable("mp_slot_hover", -1)
                            unhovered SetVariable("mp_slot_hover", -1)
                    else:
                        if mp.save_slot_image == None:
                            idle Transform ("mp_empty_idle")
                            hover Transform ("mp_empty_hover")
                            action NullAction()
                            hovered SetVariable("mp_slot_hover", -1)
                            unhovered SetVariable("mp_slot_hover", -1)
                        elif mp.save_slot_image[i] != None:
                            idle Transform (""+mp.save_slot_image[i]+"_idle")
                            hover Transform (""+mp.save_slot_image[i]+"_hover")
                            action (SetVariable("mp_slot", i), Jump("mp_load_warn_label"))
                            hovered (SetVariable("mp_slot_hover", i), Show("mp_load_info_screen"))
                            unhovered (SetVariable("mp_slot_hover", -1), Hide("mp_load_info_screen"))
                        else:
                            idle Transform ("mp_empty_idle")
                            hover Transform ("mp_empty_hover")
                            action NullAction()
                            hovered SetVariable("mp_slot_hover", -1)
                            unhovered SetVariable("mp_slot_hover", -1)
                if steamImport or steamConfig:
                    if mp_steam.save_slot_image == None:
                        text " " xalign 0.5 yalign 0.5 ypos 0.7:
                            size 21 * persistent.scale_factor
                            color "#00a0e6"
                    elif mp_steam.save_slot_name[i] != None:
                        text mp_steam.save_slot_name[i] xalign 0.5 yalign 0.5 ypos 0.7:
                            size 21 * persistent.scale_factor
                            color "#00a0e6"
                    else:
                        text " " xalign 0.5 yalign 0.5 ypos 0.7:
                            size 21 * persistent.scale_factor
                            color "#00a0e6"
                else:
                    if mp.save_slot_image == None:
                        text " " xalign 0.5 yalign 0.5 ypos 0.7:
                            size 21 * persistent.scale_factor
                            color "#00a0e6"
                    elif mp.save_slot_name[i] != None:
                        text mp.save_slot_name[i] xalign 0.5 yalign 0.5 ypos 0.7:
                            size 21 * persistent.scale_factor
                            color "#00a0e6"
                    else:
                        text " " xalign 0.5 yalign 0.5 ypos 0.7:
                            size 21 * persistent.scale_factor
                            color "#00a0e6"

screen warning_mp_screen1:
    tag warning_mp_screen1
    modal True
    add "warning3_mp_screen"
    imagebutton:
        xalign 0.3
        yalign 0.5
        idle Transform ("mp_yes_idle")
        hover Transform ("mp_yes_hover")
        action Jump("mp_load_this_save_label")
    imagebutton:
        xalign 0.7
        yalign 0.5
        idle Transform ("mp_no_idle")
        hover Transform ("mp_no_hover")
        action Jump("mp_cancel_load_label")

label mp_load_screen_label:
show screen mp_load_screen
pause

label mp_exit_to_menu_label:
return

label mp_load_warn_label:
show screen warning_mp_screen1
pause

label mp_cancel_load_label:
hide screen warning_mp_screen1
jump mp_load_screen_label

label mp_load_this_save_label:
hide screen warning_mp_screen1
hide screen mp_load_screen
hide screen mp_load_info_screen
if steamImport or steamConfig:
    $ RPderek = mp_steam.RPderek[mp_slot]
    $ RPdiks = mp_steam.RPdiks[mp_slot]
    $ RPhot = mp_steam.RPhot[mp_slot]
    $ RPisabella = mp_steam.RPisabella[mp_slot]
    $ RPjill = mp_steam.RPjill[mp_slot]
    $ RPjocks = mp_steam.RPjocks[mp_slot]
    $ RPjosy = mp_steam.RPjosy[mp_slot]
    $ RPmaya = mp_steam.RPmaya[mp_slot]
    $ RPnerds = mp_steam.RPnerds[mp_slot]
    $ RPpreps = mp_steam.RPpreps[mp_slot]
    $ RPsage = mp_steam.RPsage[mp_slot]
    $ acceptedMoneyFromDad = mp_steam.acceptedMoneyFromDad[mp_slot]
    $ affinity = mp_steam.affinity[mp_slot]
    $ art_girl_crit1_list.extend(mp_steam.art_girl_crit1_list[mp_slot])
    $ art_girl_crit2_list.extend(mp_steam.art_girl_crit2_list[mp_slot])
    $ art_girl_crit3_list.extend(mp_steam.art_girl_crit3_list[mp_slot])
    $ art_girl_level_list.extend(mp_steam.art_girl_level_list[mp_slot])
    $ art_girl_list.extend(mp_steam.art_girl_list[mp_slot])
    $ art_girl_lvl1_list.extend(mp_steam.art_girl_lvl1_list[mp_slot])
    $ art_girl_lvl2_list.extend(mp_steam.art_girl_lvl2_list[mp_slot])
    $ art_girl_lvl3_list.extend(mp_steam.art_girl_lvl3_list[mp_slot])

    $ art_girl_new_icon.extend(mp_steam.art_girl_new_icon[mp_slot])
    $ art_order_lvl1_list.extend(mp_steam.art_order_lvl1_list[mp_slot])
    $ art_order_lvl2_list.extend(mp_steam.art_order_lvl2_list[mp_slot])
    $ art_order_lvl3_list.extend(mp_steam.art_order_lvl3_list[mp_slot])
    $ assman = mp_steam.assman[mp_slot]
    $ bonusPointsSports = mp_steam.bonusPointsSports[mp_slot]
    $ bonusPointsSportsDerek = mp_steam.bonusPointsSportsDerek[mp_slot]
    $ branchAlone = mp_steam.branchAlone[mp_slot]
    $ branchIsabella = mp_steam.branchIsabella[mp_slot]
    $ branchJill = mp_steam.branchJill[mp_slot]
    $ branchMayaJosy = mp_steam.branchMayaJosy[mp_slot]
    $ branchSage = mp_steam.branchSage[mp_slot]
    $ brawler_difficulty = mp_steam.brawler_difficulty[mp_slot]
    $ brawler_hard_mode = mp_steam.brawler_hard_mode[mp_slot]
    $ camila = mp_steam.camila[mp_slot]
    $ cathy = mp_steam.cathy[mp_slot]
    $ cpenalty = mp_steam.cpenalty[mp_slot]
    $ current_notification_sound = mp_steam.current_notification_sound[mp_slot]
    $ dik = mp_steam.dik[mp_slot]
    $ dollar = mp_steam.dollar[mp_slot]
    $ dpenalty = mp_steam.dpenalty[mp_slot]
    $ dtype = mp_steam.dtype[mp_slot]
    $ earnedMoney = mp_steam.earnedMoney[mp_slot]
    $ englishBoost = mp_steam.englishBoost[mp_slot]
    $ englishCheatBoost = mp_steam.englishCheatBoost[mp_slot]
    $ envyLikesYou = mp_steam.envyLikesYou[mp_slot]
    $ ep1_accepted_quinn_offer = mp_steam.ep1_accepted_quinn_offer[mp_slot]
    $ ep1_beat_up_troy = mp_steam.ep1_beat_up_troy[mp_slot]
    $ ep1_beat_up_troy_won = mp_steam.ep1_beat_up_troy_won[mp_slot]
    $ ep1_bought_student_soda = mp_steam.ep1_bought_student_soda[mp_slot]
    $ ep1_insulted_cafeteria_worker = mp_steam.ep1_insulted_cafeteria_worker[mp_slot]
    $ ep1_josy_prefer_beer = mp_steam.ep1_josy_prefer_beer[mp_slot]
    $ ep1_josy_prefer_flowers = mp_steam.ep1_josy_prefer_flowers[mp_slot]
    $ ep1_josy_prefer_wine = mp_steam.ep1_josy_prefer_wine[mp_slot]
    $ ep1_lewd_camila_quinn = mp_steam.ep1_lewd_camila_quinn[mp_slot]
    $ ep1_maya_attracted = mp_steam.ep1_maya_attracted[mp_slot]
    $ ep1_maya_question_bath = mp_steam.ep1_maya_question_bath[mp_slot]
    $ ep1_maya_question_blanket = mp_steam.ep1_maya_question_blanket[mp_slot]
    $ ep1_maya_question_indoors = mp_steam.ep1_maya_question_indoors[mp_slot]
    $ ep1_maya_question_money = mp_steam.ep1_maya_question_money[mp_slot]
    $ ep1_maya_question_party = mp_steam.ep1_maya_question_party[mp_slot]
    $ ep2DefendedMayaAtParty = mp_steam.ep2DefendedMayaAtParty[mp_slot]
    $ ep2FoughtJocks = mp_steam.ep2FoughtJocks[mp_slot]
    $ ep2HelpedMayaAtParty = mp_steam.ep2HelpedMayaAtParty[mp_slot]
    $ ep2HelpedStudent = mp_steam.ep2HelpedStudent[mp_slot]
    $ ep2KissedSage = mp_steam.ep2KissedSage[mp_slot]
    $ ep2QuinnSawYouAndSage = mp_steam.ep2QuinnSawYouAndSage[mp_slot]
    $ ep2SageGuitarTeacher = mp_steam.ep2SageGuitarTeacher[mp_slot]
    $ ep2_HitOnDadInText = mp_steam.ep2_HitOnDadInText[mp_slot]
    $ ep2_TriedToKissMaya = mp_steam.ep2_TriedToKissMaya[mp_slot]
    $ ep2_bellaStudy = mp_steam.ep2_bellaStudy[mp_slot]
    $ ep2_boughtChocolate = mp_steam.ep2_boughtChocolate[mp_slot]
    $ ep2_boughtFlowers = mp_steam.ep2_boughtFlowers[mp_slot]
    $ ep2_cafeteriaWorkerInsulted = mp_steam.ep2_cafeteriaWorkerInsulted[mp_slot]
    $ ep2_choseMayaOverParty = mp_steam.ep2_choseMayaOverParty[mp_slot]
    $ ep2_comfortedSteve = mp_steam.ep2_comfortedSteve[mp_slot]
    $ ep2_danceSage = mp_steam.ep2_danceSage[mp_slot]
    $ ep2_dawe_fight_won = mp_steam.ep2_dawe_fight_won[mp_slot]
    $ ep2_fingeredMaya = mp_steam.ep2_fingeredMaya[mp_slot]
    $ ep2_flirtedJade = mp_steam.ep2_flirtedJade[mp_slot]
    $ ep2_fuckHOT = mp_steam.ep2_fuckHOT[mp_slot]
    $ ep2_fuckedJosy = mp_steam.ep2_fuckedJosy[mp_slot]
    $ ep2_helpSageMore = mp_steam.ep2_helpSageMore[mp_slot]
    $ ep2_helpedBellaKitchen = mp_steam.ep2_helpedBellaKitchen[mp_slot]
    $ ep2_helpedBellaMask = mp_steam.ep2_helpedBellaMask[mp_slot]
    $ ep2_jokedDawe = mp_steam.ep2_jokedDawe[mp_slot]
    $ ep2_kissedSage = mp_steam.ep2_kissedSage[mp_slot]
    $ ep2_negativeStance = mp_steam.ep2_negativeStance[mp_slot]
    $ ep2_quinnKnowsAboutCamila = mp_steam.ep2_quinnKnowsAboutCamila[mp_slot]
    $ ep2_recommendedSage = mp_steam.ep2_recommendedSage[mp_slot]
    $ ep2_shotWon = mp_steam.ep2_shotWon[mp_slot]
    $ ep2_stayWithMaya = mp_steam.ep2_stayWithMaya[mp_slot]
    $ ep2_stole_money = mp_steam.ep2_stole_money[mp_slot]
    $ ep2_textedMaya = mp_steam.ep2_textedMaya[mp_slot]
    $ ep2_toldDerekLikedMaya = mp_steam.ep2_toldDerekLikedMaya[mp_slot]
    $ ep2_toldMayaTruthAboutDate = mp_steam.ep2_toldMayaTruthAboutDate[mp_slot]
    $ ep2_toldTommyBangSage = mp_steam.ep2_toldTommyBangSage[mp_slot]
    $ ep2_tybaltPhotoMc = mp_steam.ep2_tybaltPhotoMc[mp_slot]
    $ ep2_wonCumpetition = mp_steam.ep2_wonCumpetition[mp_slot]
    $ ep3_BellaLewd = mp_steam.ep3_BellaLewd[mp_slot]
    $ ep3_acceptedJade = mp_steam.ep3_acceptedJade[mp_slot]
    $ ep3_bella_came_around = mp_steam.ep3_bella_came_around[mp_slot]
    $ ep3_boobCompetition = mp_steam.ep3_boobCompetition[mp_slot]
    $ ep3_boughtNickADance = mp_steam.ep3_boughtNickADance[mp_slot]
    $ ep3_camilaDerek = mp_steam.ep3_camilaDerek[mp_slot]
    $ ep3_chad_fight_won = mp_steam.ep3_chad_fight_won[mp_slot]
    $ ep3_choseBella = mp_steam.ep3_choseBella[mp_slot]
    $ ep3_choseDerek = mp_steam.ep3_choseDerek[mp_slot]
    $ ep3_choseSage = mp_steam.ep3_choseSage[mp_slot]
    $ ep3_cluckDerekState = mp_steam.ep3_cluckDerekState[mp_slot]
    $ ep3_cluckJillState = mp_steam.ep3_cluckJillState[mp_slot]
    $ ep3_cluckMayaState = mp_steam.ep3_cluckMayaState[mp_slot]
    $ ep3_cluckQuinnState = mp_steam.ep3_cluckQuinnState[mp_slot]
    $ ep3_dawe_prank = mp_steam.ep3_dawe_prank[mp_slot]
    $ ep3_envyLewd = mp_steam.ep3_envyLewd[mp_slot]
    $ ep3_fingered_maya = mp_steam.ep3_fingered_maya[mp_slot]
    $ ep3_fuckedCamilaAndMona = mp_steam.ep3_fuckedCamilaAndMona[mp_slot]
    $ ep3_fuckedRionaQuinn = mp_steam.ep3_fuckedRionaQuinn[mp_slot]
    $ ep3_gotDickSigned = mp_steam.ep3_gotDickSigned[mp_slot]
    $ ep3_handOnJadesThigh = mp_steam.ep3_handOnJadesThigh[mp_slot]
    $ ep3_hellWeekHelmet = mp_steam.ep3_hellWeekHelmet[mp_slot]
    $ ep3_hellWeekTryFuckJade = mp_steam.ep3_hellWeekTryFuckJade[mp_slot]
    $ ep3_helpedCamilaAndMona = mp_steam.ep3_helpedCamilaAndMona[mp_slot]
    $ ep3_intervenedChad = mp_steam.ep3_intervenedChad[mp_slot]
    $ ep3_jillHelmetChad = mp_steam.ep3_jillHelmetChad[mp_slot]
    $ ep3_jillHelmetLibrary = mp_steam.ep3_jillHelmetLibrary[mp_slot]
    $ ep3_lilyDance = mp_steam.ep3_lilyDance[mp_slot]
    $ ep3_lilyDerekDance = mp_steam.ep3_lilyDerekDance[mp_slot]
    $ ep3_lilyHatesYou = mp_steam.ep3_lilyHatesYou[mp_slot]
    $ ep3_mallHelmet = mp_steam.ep3_mallHelmet[mp_slot]
    $ ep3_mansionHelmet = mp_steam.ep3_mansionHelmet[mp_slot]
    $ ep3_mayaLewd = mp_steam.ep3_mayaLewd[mp_slot]
    $ ep3_mayaOfferedHelp = mp_steam.ep3_mayaOfferedHelp[mp_slot]
    $ ep3_paidBellaMeal = mp_steam.ep3_paidBellaMeal[mp_slot]
    $ ep3_protectedElf = mp_steam.ep3_protectedElf[mp_slot]
    $ ep3_sclubParty = mp_steam.ep3_sclubParty[mp_slot]
    $ ep3_spankedSally = mp_steam.ep3_spankedSally[mp_slot]
    $ ep3_threesomeOffer = mp_steam.ep3_threesomeOffer[mp_slot]
    $ ep3_toldJillBullying = mp_steam.ep3_toldJillBullying[mp_slot]
    $ ep3_wearHelmet = mp_steam.ep3_wearHelmet[mp_slot]
    $ ep4_SageMovieEvent = mp_steam.ep4_SageMovieEvent[mp_slot]
    $ ep4_bella_lewd = mp_steam.ep4_bella_lewd[mp_slot]
    $ ep4_camilaOffer = mp_steam.ep4_camilaOffer[mp_slot]
    $ ep4_cluckDaweState = mp_steam.ep4_cluckDaweState[mp_slot]
    $ ep4_cluckDerekState = mp_steam.ep4_cluckDerekState[mp_slot]
    $ ep4_cluckJillState = mp_steam.ep4_cluckJillState[mp_slot]
    $ ep4_cluckSage2State = mp_steam.ep4_cluckSage2State[mp_slot]
    $ ep4_derekFuckedArieth = mp_steam.ep4_derekFuckedArieth[mp_slot]
    $ ep4_discussed_heather = mp_steam.ep4_discussed_heather[mp_slot]
    $ ep4_discussed_melanie = mp_steam.ep4_discussed_melanie[mp_slot]
    $ ep4_discussed_riona = mp_steam.ep4_discussed_riona[mp_slot]
    $ ep4_fuckedJade = mp_steam.ep4_fuckedJade[mp_slot]
    $ ep4_fuckedMelanie = mp_steam.ep4_fuckedMelanie[mp_slot]
    $ ep4_fuckedSage = mp_steam.ep4_fuckedSage[mp_slot]
    $ ep4_grindedLily = mp_steam.ep4_grindedLily[mp_slot]
    $ ep4_hottest_ass = mp_steam.ep4_hottest_ass[mp_slot]
    $ ep4_jadeOffer = mp_steam.ep4_jadeOffer[mp_slot]
    $ ep4_jillNiceGuy = mp_steam.ep4_jillNiceGuy[mp_slot]
    $ ep4_jillShower = mp_steam.ep4_jillShower[mp_slot]
    $ ep4_join_chess_club = mp_steam.ep4_join_chess_club[mp_slot]
    $ ep4_kissedJill = mp_steam.ep4_kissedJill[mp_slot]
    $ ep4_kissedJill2 = mp_steam.ep4_kissedJill2[mp_slot]
    $ ep4_kissedRiona = mp_steam.ep4_kissedRiona[mp_slot]
    $ ep4_knowLily = mp_steam.ep4_knowLily[mp_slot]
    $ ep4_lecturedBella = mp_steam.ep4_lecturedBella[mp_slot]
    $ ep4_lickedAshley = mp_steam.ep4_lickedAshley[mp_slot]
    $ ep4_likeQuinn = mp_steam.ep4_likeQuinn[mp_slot]
    $ ep4_made_out_josy = mp_steam.ep4_made_out_josy[mp_slot]
    $ ep4_missedSage = mp_steam.ep4_missedSage[mp_slot]
    $ ep4_monaSlap = mp_steam.ep4_monaSlap[mp_slot]
    $ ep4_morningHelmet = mp_steam.ep4_morningHelmet[mp_slot]
    $ ep4_paidMagnarWedgie = mp_steam.ep4_paidMagnarWedgie[mp_slot]
    $ ep4_pinkRoseEvent = mp_steam.ep4_pinkRoseEvent[mp_slot]
    $ ep4_quinn_lewd = mp_steam.ep4_quinn_lewd[mp_slot]
    $ ep4_rejectedJade = mp_steam.ep4_rejectedJade[mp_slot]
    $ ep4_rejectedMayaJosy = mp_steam.ep4_rejectedMayaJosy[mp_slot]
    $ ep4_roseLewd = mp_steam.ep4_roseLewd[mp_slot]
    $ ep4_sageLikeDaringSex = mp_steam.ep4_sageLikeDaringSex[mp_slot]
    $ ep4_sage_drink = mp_steam.ep4_sage_drink[mp_slot]
    $ ep4_saturdayHelmet = mp_steam.ep4_saturdayHelmet[mp_slot]
    $ ep4_smoked_weed = mp_steam.ep4_smoked_weed[mp_slot]
    $ ep4_toldDerekAboutCathy = mp_steam.ep4_toldDerekAboutCathy[mp_slot]
    $ ep4_toldDerekAboutJade = mp_steam.ep4_toldDerekAboutJade[mp_slot]
    $ ep4_toldDerekYouTrustHim = mp_steam.ep4_toldDerekYouTrustHim[mp_slot]
    $ ep4_toldElenaInterested = mp_steam.ep4_toldElenaInterested[mp_slot]
    $ ep4_touchedJillsBreasts = mp_steam.ep4_touchedJillsBreasts[mp_slot]
    $ ep4_ugliest_ass = mp_steam.ep4_ugliest_ass[mp_slot]
    $ ep4_wantedMoreMayaJosy = mp_steam.ep4_wantedMoreMayaJosy[mp_slot]
    $ ep4_wearHelmet = mp_steam.ep4_wearHelmet[mp_slot]
    $ ep4_wonTennis = mp_steam.ep4_wonTennis[mp_slot]
    $ ep5_agitatedCaleb = mp_steam.ep5_agitatedCaleb[mp_slot]
    $ ep5_bella_lewd = mp_steam.ep5_bella_lewd[mp_slot]
    $ ep5_bella_remember_song = mp_steam.ep5_bella_remember_song[mp_slot]
    $ ep5_bella_sauna = mp_steam.ep5_bella_sauna[mp_slot]
    $ ep5_caleb_fight_won = mp_steam.ep5_caleb_fight_won[mp_slot]
    $ ep5_cathy_lewd = mp_steam.ep5_cathy_lewd[mp_slot]
    $ ep5_cluckAnthonyState = mp_steam.ep5_cluckAnthonyState[mp_slot]
    $ ep5_cluckCamilaState = mp_steam.ep5_cluckCamilaState[mp_slot]
    $ ep5_cluckDerekState = mp_steam.ep5_cluckDerekState[mp_slot]
    $ ep5_cluckJadeState = mp_steam.ep5_cluckJadeState[mp_slot]
    $ ep5_cluckJillState = mp_steam.ep5_cluckJillState[mp_slot]
    $ ep5_cluckJosyState = mp_steam.ep5_cluckJosyState[mp_slot]
    $ ep5_cluckLilyState = mp_steam.ep5_cluckLilyState[mp_slot]
    $ ep5_cluckRionaState = mp_steam.ep5_cluckRionaState[mp_slot]
    $ ep5_confide_sage = mp_steam.ep5_confide_sage[mp_slot]
    $ ep5_confrontedRiona = mp_steam.ep5_confrontedRiona[mp_slot]
    $ ep5_derekPoints = mp_steam.ep5_derekPoints[mp_slot]
    $ ep5_dikSecret = mp_steam.ep5_dikSecret[mp_slot]
    $ ep5_dikWinner = mp_steam.ep5_dikWinner[mp_slot]
    $ ep5_feelingsForJosy = mp_steam.ep5_feelingsForJosy[mp_slot]
    $ ep5_feelingsForMaya = mp_steam.ep5_feelingsForMaya[mp_slot]
    $ ep5_followed_josy = mp_steam.ep5_followed_josy[mp_slot]
    $ ep5_followed_maya = mp_steam.ep5_followed_maya[mp_slot]
    $ ep5_fuckedCamila = mp_steam.ep5_fuckedCamila[mp_slot]
    $ ep5_fuckedRiona = mp_steam.ep5_fuckedRiona[mp_slot]
    $ ep5_fuckedSage = mp_steam.ep5_fuckedSage[mp_slot]
    $ ep5_fucked_josy = mp_steam.ep5_fucked_josy[mp_slot]
    $ ep5_fucked_maya = mp_steam.ep5_fucked_maya[mp_slot]
    $ ep5_gave_riona_money = mp_steam.ep5_gave_riona_money[mp_slot]
    $ ep5_help_josy = mp_steam.ep5_help_josy[mp_slot]
    $ ep5_hot_lewd = mp_steam.ep5_hot_lewd[mp_slot]
    $ ep5_josy_shaven = mp_steam.ep5_josy_shaven[mp_slot]
    $ ep5_kissed_jill = mp_steam.ep5_kissed_jill[mp_slot]
    $ ep5_like_champagne = mp_steam.ep5_like_champagne[mp_slot]
    $ ep5_lily_lewd = mp_steam.ep5_lily_lewd[mp_slot]
    $ ep5_look_at_mel = mp_steam.ep5_look_at_mel[mp_slot]
    $ ep5_look_at_sarah = mp_steam.ep5_look_at_sarah[mp_slot]
    $ ep5_mcPoints = mp_steam.ep5_mcPoints[mp_slot]
    $ ep5_painted_fence = mp_steam.ep5_painted_fence[mp_slot]
    $ ep5_peeked_jb = mp_steam.ep5_peeked_jb[mp_slot]
    $ ep5_preferCathyTits = mp_steam.ep5_preferCathyTits[mp_slot]
    $ ep5_punchedTybalt = mp_steam.ep5_punchedTybalt[mp_slot]
    $ ep5_smoked_weed = mp_steam.ep5_smoked_weed[mp_slot]
    $ ep6_accept_tommy = mp_steam.ep6_accept_tommy[mp_slot]
    $ ep6_apologized_dany = mp_steam.ep6_apologized_dany[mp_slot]
    $ ep6_bella_lewd = mp_steam.ep6_bella_lewd[mp_slot]
    $ ep6_blamed_derek = mp_steam.ep6_blamed_derek[mp_slot]
    $ ep6_cared = mp_steam.ep6_cared[mp_slot]
    $ ep6_choseJillOverSage = mp_steam.ep6_choseJillOverSage[mp_slot]
    $ ep6_cluckDaweState = mp_steam.ep6_cluckDaweState[mp_slot]
    $ ep6_cluckDerekState = mp_steam.ep6_cluckDerekState[mp_slot]
    $ ep6_cluckJosyState = mp_steam.ep6_cluckJosyState[mp_slot]
    $ ep6_cluckMayaState = mp_steam.ep6_cluckMayaState[mp_slot]
    $ ep6_cluckMelanieState = mp_steam.ep6_cluckMelanieState[mp_slot]
    $ ep6_cluckTybaltState = mp_steam.ep6_cluckTybaltState[mp_slot]
    $ ep6_different_song = mp_steam.ep6_different_song[mp_slot]
    $ ep6_dng_ending = mp_steam.ep6_dng_ending[mp_slot]
    $ ep6_dng_seduce = mp_steam.ep6_dng_seduce[mp_slot]
    $ ep6_envy_lewd = mp_steam.ep6_envy_lewd[mp_slot]
    $ ep6_fakeID = mp_steam.ep6_fakeID[mp_slot]
    $ ep6_flirted_heather = mp_steam.ep6_flirted_heather[mp_slot]
    $ ep6_foughtTommy = mp_steam.ep6_foughtTommy[mp_slot]
    $ ep6_genderMaya = mp_steam.ep6_genderMaya[mp_slot]
    $ ep6_helpSage = mp_steam.ep6_helpSage[mp_slot]
    $ ep6_jamjam = mp_steam.ep6_jamjam[mp_slot]
    $ ep6_jill_lewd = mp_steam.ep6_jill_lewd[mp_slot]
    $ ep6_like_maya = mp_steam.ep6_like_maya[mp_slot]
    $ ep6_looked_elena = mp_steam.ep6_looked_elena[mp_slot]
    $ ep6_maya_library_question = mp_steam.ep6_maya_library_question[mp_slot]
    $ ep6_mj_lunch = mp_steam.ep6_mj_lunch[mp_slot]
    $ ep6_nora_lewd = mp_steam.ep6_nora_lewd[mp_slot]
    $ ep6_quinn_lewd = mp_steam.ep6_quinn_lewd[mp_slot]
    $ ep6_reject_jade = mp_steam.ep6_reject_jade[mp_slot]
    $ ep6_rejected_sarah = mp_steam.ep6_rejected_sarah[mp_slot]
    $ ep6_sarah_lewd = mp_steam.ep6_sarah_lewd[mp_slot]
    $ ep6_suck_lily = mp_steam.ep6_suck_lily[mp_slot]
    $ ep6_tommy_fight_won = mp_steam.ep6_tommy_fight_won[mp_slot]
    $ ep6_vipPass = mp_steam.ep6_vipPass[mp_slot]
    $ ep7_3outof5 = mp_steam.ep7_3outof5[mp_slot]
    $ ep7_accept_madame = mp_steam.ep7_accept_madame[mp_slot]
    $ ep7_alphas_leave = mp_steam.ep7_alphas_leave[mp_slot]
    $ ep7_becky_lewd = mp_steam.ep7_becky_lewd[mp_slot]
    $ ep7_becky_puke = mp_steam.ep7_becky_puke[mp_slot]
    $ ep7_bella_lewd = mp_steam.ep7_bella_lewd[mp_slot]
    $ ep7_bella_rejected_you = mp_steam.ep7_bella_rejected_you[mp_slot]
    $ ep7_brawler_sage_win = mp_steam.ep7_brawler_sage_win[mp_slot]
    $ ep7_camila_lewd = mp_steam.ep7_camila_lewd[mp_slot]
    $ ep7_current_desk_painting = mp_steam.ep7_current_desk_painting[mp_slot]
    $ ep7_dentures = mp_steam.ep7_dentures[mp_slot]
    $ ep7_dodged_josy = mp_steam.ep7_dodged_josy[mp_slot]
    $ ep7_got_flower = mp_steam.ep7_got_flower[mp_slot]
    $ ep7_heather_drink = mp_steam.ep7_heather_drink[mp_slot]
    $ ep7_heather_likes_you = mp_steam.ep7_heather_likes_you[mp_slot]
    $ ep7_hit_on_becky = mp_steam.ep7_hit_on_becky[mp_slot]
    $ ep7_hot_ashley_phase = mp_steam.ep7_hot_ashley_phase[mp_slot]
    $ ep7_hot_jacob_phase = mp_steam.ep7_hot_jacob_phase[mp_slot]
    $ ep7_hug_maya = mp_steam.ep7_hug_maya[mp_slot]
    $ ep7_jill_jealous = mp_steam.ep7_jill_jealous[mp_slot]
    $ ep7_jill_lewd = mp_steam.ep7_jill_lewd[mp_slot]
    $ ep7_jill_run = mp_steam.ep7_jill_run[mp_slot]
    $ ep7_jill_talk = mp_steam.ep7_jill_talk[mp_slot]
    $ ep7_josy_comfort = mp_steam.ep7_josy_comfort[mp_slot]
    $ ep7_josy_lewd = mp_steam.ep7_josy_lewd[mp_slot]
    $ ep7_josy_lewd2 = mp_steam.ep7_josy_lewd2[mp_slot]
    $ ep7_kiss_josy = mp_steam.ep7_kiss_josy[mp_slot]
    $ ep7_left_with_josy = mp_steam.ep7_left_with_josy[mp_slot]
    $ ep7_like_quinn = mp_steam.ep7_like_quinn[mp_slot]
    $ ep7_lily_lewd = mp_steam.ep7_lily_lewd[mp_slot]
    $ ep7_madame_options_list.extend(mp_steam.ep7_madame_options_list[mp_slot])
    $ ep7_pathSage = mp_steam.ep7_pathSage[mp_slot]
    $ ep7_patrick_score = mp_steam.ep7_patrick_score[mp_slot]
    $ ep7_pinkrose = mp_steam.ep7_pinkrose[mp_slot]
    $ ep7_quinn_cluck = mp_steam.ep7_quinn_cluck[mp_slot]
    $ ep7_quinn_lewd = mp_steam.ep7_quinn_lewd[mp_slot]
    $ ep7_rejected_cathy = mp_steam.ep7_rejected_cathy[mp_slot]
    $ ep7_rica_lewd = mp_steam.ep7_rica_lewd[mp_slot]
    $ ep7_riona_help = mp_steam.ep7_riona_help[mp_slot]
    $ ep7_riona_lewd = mp_steam.ep7_riona_lewd[mp_slot]
    $ ep7_riona_payback = mp_steam.ep7_riona_payback[mp_slot]
    $ ep7_ruined_presentation = mp_steam.ep7_ruined_presentation[mp_slot]
    $ ep7_sage_fight_won = mp_steam.ep7_sage_fight_won[mp_slot]
    $ ep7_sage_lewd = mp_steam.ep7_sage_lewd[mp_slot]
    $ ep7_solo_josy = mp_steam.ep7_solo_josy[mp_slot]
    $ ep7_solo_maya = mp_steam.ep7_solo_maya[mp_slot]
    $ ep7_solo_quinn = mp_steam.ep7_solo_quinn[mp_slot]
    $ ep7_told_heather_tommy_cheated = mp_steam.ep7_told_heather_tommy_cheated[mp_slot]
    $ ep7_tybalt_state = mp_steam.ep7_tybalt_state[mp_slot]
    $ ep7_wingman_derek = mp_steam.ep7_wingman_derek[mp_slot]
    $ ep7_wonTennis = mp_steam.ep7_wonTennis[mp_slot]
    $ ep8_current_second_painting = mp_steam.ep8_current_second_painting[mp_slot]
    $ ep8_elena_shot = mp_steam.ep8_elena_shot[mp_slot]
    $ ep8_envy_lewd = mp_steam.ep8_envy_lewd[mp_slot]
    $ ep8_flower_water_level = mp_steam.ep8_flower_water_level[mp_slot]
    $ ep8_handle_bella = mp_steam.ep8_handle_bella[mp_slot]
    $ ep8_help_jm_with_room = mp_steam.ep8_help_jm_with_room[mp_slot]
    $ ep8_help_nick = mp_steam.ep8_help_nick[mp_slot]
    $ ep8_jade_lewd = mp_steam.ep8_jade_lewd[mp_slot]
    $ ep8_jill_rejected_you = mp_steam.ep8_jill_rejected_you[mp_slot]
    $ ep8_jill_state = mp_steam.ep8_jill_state[mp_slot]
    $ ep8_josy_dance = mp_steam.ep8_josy_dance[mp_slot]
    $ ep8_josy_lewd = mp_steam.ep8_josy_lewd[mp_slot]
    $ ep8_leons_side = mp_steam.ep8_leons_side[mp_slot]
    $ ep8_lily_lewd = mp_steam.ep8_lily_lewd[mp_slot]
    $ ep8_mansion_won = mp_steam.ep8_mansion_won[mp_slot]
    $ ep8_maya_lewd = mp_steam.ep8_maya_lewd[mp_slot]
    $ ep8_melanie_lewd = mp_steam.ep8_melanie_lewd[mp_slot]
    $ ep8_midterms_cheated = mp_steam.ep8_midterms_cheated[mp_slot]
    $ ep8_nora_number = mp_steam.ep8_nora_number[mp_slot]
    $ ep8_pink_rose_picture = mp_steam.ep8_pink_rose_picture[mp_slot]
    $ ep8_quinn_rejected_you = mp_steam.ep8_quinn_rejected_you[mp_slot]
    $ ep8_recital_failed = mp_steam.ep8_recital_failed[mp_slot]
    $ ep8_revenge = mp_steam.ep8_revenge[mp_slot]
    $ ep8_sandy_lewd = mp_steam.ep8_sandy_lewd[mp_slot]
    $ ep8_sarah_lewd = mp_steam.ep8_sarah_lewd[mp_slot]
    $ ep8_second_painting = mp_steam.ep8_second_painting[mp_slot]
    $ ep8_share_room = mp_steam.ep8_share_room[mp_slot]
    $ ep8_sq_lewd = mp_steam.ep8_sq_lewd[mp_slot]
    $ ep8_told_josy_chad = mp_steam.ep8_told_josy_chad[mp_slot]
    $ ep8_told_sage_chad_troy = mp_steam.ep8_told_sage_chad_troy[mp_slot]
    $ ep8_prep_truce = mp_steam.ep8_prep_truce[mp_slot]
    $ ep8_quinn_cluck = mp_steam.ep8_quinn_cluck[mp_slot]
    $ event_list.extend(mp_steam.event_list[mp_slot])
    $ failedEnglish = mp_steam.failedEnglish[mp_slot]
    $ failedGame = mp_steam.failedGame[mp_slot]
    $ failedGender = mp_steam.failedGender[mp_slot]
    $ failedMath = mp_steam.failedMath[mp_slot]
    $ firstTimeFreeRoam = mp_steam.firstTimeFreeRoam[mp_slot]
    $ freeRoamID = mp_steam.freeRoamID[mp_slot]
    $ gameBoost = mp_steam.gameBoost[mp_slot]
    $ intervenedChad = mp_steam.intervenedChad[mp_slot]
    $ isabella = mp_steam.isabella[mp_slot]
    $ jade = mp_steam.jade[mp_slot]
    $ jill = mp_steam.jill[mp_slot]
    $ josy = mp_steam.josy[mp_slot]
    $ laptop_wallpapers.extend(mp_steam.laptop_wallpapers[mp_slot])
    $ laptop_wallpapers_criteria_met.extend(mp_steam.laptop_wallpapers_criteria_met[mp_slot])
    $ laptop_wallpapers_unlocked.extend(mp_steam.laptop_wallpapers_unlocked[mp_slot])
    $ madame = mp_steam.madame[mp_slot]
    $ majorchick = mp_steam.majorchick[mp_slot]
    $ majordik = mp_steam.majordik[mp_slot]
    $ mansion_money = mp_steam.mansion_money[mp_slot]
    $ mansion_score = mp_steam.mansion_score[mp_slot]
    $ mathBoost = mp_steam.mathBoost[mp_slot]
    $ mathCheatBoost = mp_steam.mathCheatBoost[mp_slot]
    $ maxedEnglish = mp_steam.maxedEnglish[mp_slot]
    $ maxedEnglish_s2 = mp_steam.maxedEnglish_s2[mp_slot]
    $ maxedGender = mp_steam.maxedGender[mp_slot]
    $ maxedGender_s2 = mp_steam.maxedGender_s2[mp_slot]
    $ maxedMath = mp_steam.maxedMath[mp_slot]
    $ maxedMath_s2 = mp_steam.maxedMath_s2[mp_slot]
    $ maxedPaintPaths = mp_steam.maxedPaintPaths[mp_slot]
    $ maxedPaths = mp_steam.maxedPaths[mp_slot]
    $ maxedPaths_s2 = mp_steam.maxedPaths_s2[mp_slot]
    $ maya = mp_steam.maya[mp_slot]
    $ mbios_history_alex.extend(mp_steam.mbios_history_alex[mp_slot])
    $ mbios_history_anthony.extend(mp_steam.mbios_history_anthony[mp_slot])
    $ mbios_history_arieth.extend(mp_steam.mbios_history_arieth[mp_slot])
    $ mbios_history_ashley.extend(mp_steam.mbios_history_ashley[mp_slot])
    $ mbios_history_becky.extend(mp_steam.mbios_history_becky[mp_slot])
    $ mbios_history_bert.extend(mp_steam.mbios_history_bert[mp_slot])
    $ mbios_history_beth.extend(mp_steam.mbios_history_beth[mp_slot])
    $ mbios_history_brandi.extend(mp_steam.mbios_history_brandi[mp_slot])
    $ mbios_history_burke.extend(mp_steam.mbios_history_burke[mp_slot])
    $ mbios_history_caleb.extend(mp_steam.mbios_history_caleb[mp_slot])
    $ mbios_history_camila.extend(mp_steam.mbios_history_camila[mp_slot])
    $ mbios_history_cathy.extend(mp_steam.mbios_history_cathy[mp_slot])
    $ mbios_history_chad.extend(mp_steam.mbios_history_chad[mp_slot])
    $ mbios_history_christian.extend(mp_steam.mbios_history_christian[mp_slot])
    $ mbios_history_dad.extend(mp_steam.mbios_history_dad[mp_slot])
    $ mbios_history_dany.extend(mp_steam.mbios_history_dany[mp_slot])
    $ mbios_history_darius.extend(mp_steam.mbios_history_darius[mp_slot])
    $ mbios_history_dawe.extend(mp_steam.mbios_history_dawe[mp_slot])
    $ mbios_history_derek.extend(mp_steam.mbios_history_derek[mp_slot])
    $ mbios_history_elena.extend(mp_steam.mbios_history_elena[mp_slot])
    $ mbios_history_envy.extend(mp_steam.mbios_history_envy[mp_slot])
    $ mbios_history_eugene.extend(mp_steam.mbios_history_eugene[mp_slot])
    $ mbios_history_gordon.extend(mp_steam.mbios_history_gordon[mp_slot])
    $ mbios_history_heather.extend(mp_steam.mbios_history_heather[mp_slot])
    $ mbios_history_isabella.extend(mp_steam.mbios_history_isabella[mp_slot])
    $ mbios_history_jacob.extend(mp_steam.mbios_history_jacob[mp_slot])
    $ mbios_history_jade.extend(mp_steam.mbios_history_jade[mp_slot])
    $ mbios_history_jamie.extend(mp_steam.mbios_history_jamie[mp_slot])
    $ mbios_history_jill.extend(mp_steam.mbios_history_jill[mp_slot])
    $ mbios_history_jimmy.extend(mp_steam.mbios_history_jimmy[mp_slot])
    $ mbios_history_john.extend(mp_steam.mbios_history_john[mp_slot])
    $ mbios_history_johnboy.extend(mp_steam.mbios_history_johnboy[mp_slot])
    $ mbios_history_josy.extend(mp_steam.mbios_history_josy[mp_slot])
    $ mbios_history_karen.extend(mp_steam.mbios_history_karen[mp_slot])
    $ mbios_history_leon.extend(mp_steam.mbios_history_leon[mp_slot])
    $ mbios_history_lily.extend(mp_steam.mbios_history_lily[mp_slot])
    $ mbios_history_linda.extend(mp_steam.mbios_history_linda[mp_slot])
    $ mbios_history_lucas.extend(mp_steam.mbios_history_lucas[mp_slot])
    $ mbios_history_lynette.extend(mp_steam.mbios_history_lynette[mp_slot])
    $ mbios_history_madame.extend(mp_steam.mbios_history_madame[mp_slot])
    $ mbios_history_magnar.extend(mp_steam.mbios_history_magnar[mp_slot])
    $ mbios_history_maya.extend(mp_steam.mbios_history_maya[mp_slot])
    $ mbios_history_mc.extend(mp_steam.mbios_history_mc[mp_slot])
    $ mbios_history_melanie.extend(mp_steam.mbios_history_melanie[mp_slot])
    $ mbios_history_minny.extend(mp_steam.mbios_history_minny[mp_slot])
    $ mbios_history_mona.extend(mp_steam.mbios_history_mona[mp_slot])
    $ mbios_history_nick.extend(mp_steam.mbios_history_nick[mp_slot])
    $ mbios_history_patrick.extend(mp_steam.mbios_history_patrick[mp_slot])
    $ mbios_history_pete.extend(mp_steam.mbios_history_pete[mp_slot])
    $ mbios_history_quinn.extend(mp_steam.mbios_history_quinn[mp_slot])
    $ mbios_history_rich.extend(mp_steam.mbios_history_rich[mp_slot])
    $ mbios_history_riona.extend(mp_steam.mbios_history_riona[mp_slot])
    $ mbios_history_ron.extend(mp_steam.mbios_history_ron[mp_slot])
    $ mbios_history_rose.extend(mp_steam.mbios_history_rose[mp_slot])
    $ mbios_history_rusty.extend(mp_steam.mbios_history_rusty[mp_slot])
    $ mbios_history_sage.extend(mp_steam.mbios_history_sage[mp_slot])
    $ mbios_history_sally.extend(mp_steam.mbios_history_sally[mp_slot])
    $ mbios_history_sandy.extend(mp_steam.mbios_history_sandy[mp_slot])
    $ mbios_history_sarah.extend(mp_steam.mbios_history_sarah[mp_slot])
    $ mbios_history_stanley.extend(mp_steam.mbios_history_stanley[mp_slot])
    $ mbios_history_steve.extend(mp_steam.mbios_history_steve[mp_slot])
    $ mbios_history_tommy.extend(mp_steam.mbios_history_tommy[mp_slot])
    $ mbios_history_trent.extend(mp_steam.mbios_history_trent[mp_slot])
    $ mbios_history_troy.extend(mp_steam.mbios_history_troy[mp_slot])
    $ mbios_history_tybalt.extend(mp_steam.mbios_history_tybalt[mp_slot])
    $ mbios_history_vinny.extend(mp_steam.mbios_history_vinny[mp_slot])
    $ mbios_history_wendy.extend(mp_steam.mbios_history_wendy[mp_slot])
    $ mbios_history_zoey.extend(mp_steam.mbios_history_zoey[mp_slot])
    $ mbios_mc = mp_steam.mbios_mc[mp_slot]
    $ mbios_mc_hover = mp_steam.mbios_mc_hover[mp_slot]
    $ mbios_mc_new = mp_steam.mbios_mc_new[mp_slot]
    $ mbios_mc_new_hover = mp_steam.mbios_mc_new_hover[mp_slot]
    $ mc_avatar = mp_steam.mc_avatar[mp_slot]
    $ mc_camila = mp_steam.mc_camila[mp_slot]
    $ mc_cathy = mp_steam.mc_cathy[mp_slot]
    $ mc_de = mp_steam.mc_de[mp_slot]
    $ mc_de_up = mp_steam.mc_de_up[mp_slot]
    $ mc_isabella = mp_steam.mc_isabella[mp_slot]
    $ mc_jade = mp_steam.mc_jade[mp_slot]
    $ mc_jill = mp_steam.mc_jill[mp_slot]
    $ mc_josy = mp_steam.mc_josy[mp_slot]
    $ mc_maya = mp_steam.mc_maya[mp_slot]
    $ mc_quinn = mp_steam.mc_quinn[mp_slot]
    $ mc_riona = mp_steam.mc_riona[mp_slot]
    $ mc_sage = mp_steam.mc_sage[mp_slot]
    $ minigames = mp_steam.minigames[mp_slot]
    $ money = mp_steam.money[mp_slot]
    $ mphone_bios_chars.extend(mp_steam.mphone_bios_chars[mp_slot])
    $ mphone_bios_chars_list.extend(mp_steam.mphone_bios_chars_list[mp_slot])
    $ mphone_chat_history_list.extend(mp_steam.mphone_chat_history_list[mp_slot])
    $ mphone_contact_list.extend(mp_steam.mphone_contact_list[mp_slot])
    $ mphone_current_input = mp_steam.mphone_current_input[mp_slot]
    $ mphone_current_wallpaper = mp_steam.mphone_current_wallpaper[mp_slot]
    $ mphone_mc_avatar = mp_steam.mphone_mc_avatar[mp_slot]
    $ mphone_music_bar_show = mp_steam.mphone_music_bar_show[mp_slot]
    $ mphone_use_favs = mp_steam.mphone_use_favs[mp_slot]
    $ mphone_wallpaper_int = mp_steam.mphone_wallpaper_int[mp_slot]
    $ mphone_wallpaper_list.extend(mp_steam.mphone_wallpaper_list[mp_slot])
    $ mroosterAvatarArray.extend(mp_steam.mroosterAvatarArray[mp_slot])
    $ mroosterChoices.extend(mp_steam.mroosterChoices[mp_slot])
    $ mroosterCommentSectionArray.extend(mp_steam.mroosterCommentSectionArray[mp_slot])
    $ mroosterHistory_avatars.extend(mp_steam.mroosterHistory_avatars[mp_slot])
    $ mroosterHistory_liked.extend(mp_steam.mroosterHistory_liked[mp_slot])
    $ mroosterHistory_likes.extend(mp_steam.mroosterHistory_likes[mp_slot])
    $ mroosterHistory_nicknames.extend(mp_steam.mroosterHistory_nicknames[mp_slot])
    $ mroosterHistory_text.extend(mp_steam.mroosterHistory_text[mp_slot])
    $ mroosterLikedArray.extend(mp_steam.mroosterLikedArray[mp_slot])
    $ mroosterLikesArray.extend(mp_steam.mroosterLikesArray[mp_slot])
    $ mroosterNickArray.extend(mp_steam.mroosterNickArray[mp_slot])
    $ mroosterPhotoArray.extend(mp_steam.mroosterPhotoArray[mp_slot])
    $ mroosterPostsArray.extend(mp_steam.mroosterPostsArray[mp_slot])
    $ mroosterTextArray.extend(mp_steam.mroosterTextArray[mp_slot])
    $ name = mp_steam.name[mp_slot]
    $ nerdNotes = mp_steam.nerdNotes[mp_slot]
    $ notifications = mp_steam.notifications[mp_slot]
    $ passedEnglish = mp_steam.passedEnglish[mp_slot]
    $ passedGender = mp_steam.passedGender[mp_slot]
    $ passedMath = mp_steam.passedMath[mp_slot]
    $ pathCathy = mp_steam.pathCathy[mp_slot]
    $ pathIsabella = mp_steam.pathIsabella[mp_slot]
    $ pathJill = mp_steam.pathJill[mp_slot]
    $ pathMayaJosy = mp_steam.pathMayaJosy[mp_slot]
    $ pathSage = mp_steam.pathSage[mp_slot]
    $ permanent_affinity = mp_steam.permanent_affinity[mp_slot]
    $ preferredmilf = mp_steam.preferredmilf[mp_slot]
    $ quinn = mp_steam.quinn[mp_slot]
    $ quinn_shop_freebie = mp_steam.quinn_shop_freebie[mp_slot]
    $ quinn_shop_japanese_lvl = mp_steam.quinn_shop_japanese_lvl[mp_slot]
    $ quinn_shop_special_lvl = mp_steam.quinn_shop_special_lvl[mp_slot]
    $ quinn_shop_spicy_lvl = mp_steam.quinn_shop_spicy_lvl[mp_slot]
    $ rejectedSage = mp_steam.rejectedSage[mp_slot]
    $ riona = mp_steam.riona[mp_slot]
    $ roosterNickArray.extend(mp_steam.roosterNickArray[mp_slot])
    $ roosterNickJamie = mp_steam.roosterNickJamie[mp_slot]
    $ roosterNickAlt = mp_steam.roosterNickAlt[mp_slot]
    $ roosterNickMC = mp_steam.roosterNickMC[mp_slot]
    $ roosterNickMCCustom = mp_steam.roosterNickMCCustom[mp_slot]
    $ rooster_nick_list.extend(mp_steam.rooster_nick_list[mp_slot])
    $ sage = mp_steam.sage[mp_slot]
    $ sageControlEp3 = mp_steam.sageControlEp3[mp_slot]
    $ save_name = mp_steam.save_name[mp_slot]
    $ settings_name = mp_steam.settings_name[mp_slot]
    $ settings_rooster_nickname = mp_steam.settings_rooster_nickname[mp_slot]
    $ shuffle_losses = mp_steam.shuffle_losses[mp_slot]
    $ shuffle_wins = mp_steam.shuffle_wins[mp_slot]
    $ spentMoney = mp_steam.spentMoney[mp_slot]
    $ sports_counter_skill = mp_steam.sports_counter_skill[mp_slot]
    $ sports_dex = mp_steam.sports_dex[mp_slot]
    $ sports_heal_skill = mp_steam.sports_heal_skill[mp_slot]
    $ sports_hp = mp_steam.sports_hp[mp_slot]
    $ sports_pow = mp_steam.sports_pow[mp_slot]
    $ sports_mov = mp_steam.sports_mov[mp_slot]
    $ sports_roundhouse_skill = mp_steam.sports_roundhouse_skill[mp_slot]
    $ sports_skillpointsleft = mp_steam.sports_skillpointsleft[mp_slot]
    $ sports_store_sp1 = mp_steam.sports_store_sp1[mp_slot]
    $ sports_store_sp2 = mp_steam.sports_store_sp2[mp_slot]
    $ sports_store_sp3 = mp_steam.sports_store_sp3[mp_slot]
    $ stevePainting = mp_steam.stevePainting[mp_slot]
    $ swyper_arieth_history.extend(mp_steam.swyper_arieth_history[mp_slot])
    $ swyper_arieth_state = mp_steam.swyper_arieth_state[mp_slot]
    $ swyper_cathy_history.extend(mp_steam.swyper_cathy_history[mp_slot])
    $ swyper_cathy_state = mp_steam.swyper_cathy_state[mp_slot]
    $ swyper_catrin_history.extend(mp_steam.swyper_catrin_history[mp_slot])
    $ swyper_catrin_state = mp_steam.swyper_catrin_state[mp_slot]
    $ swyper_ellie_history.extend(mp_steam.swyper_ellie_history[mp_slot])
    $ swyper_ellie_state = mp_steam.swyper_ellie_state[mp_slot]
    $ swyper_ida_history.extend(mp_steam.swyper_ida_history[mp_slot])
    $ swyper_ida_state = mp_steam.swyper_ida_state[mp_slot]
    $ swyper_liked_arieth = mp_steam.swyper_liked_arieth[mp_slot]
    $ swyper_liked_cathy = mp_steam.swyper_liked_cathy[mp_slot]
    $ swyper_liked_catrin = mp_steam.swyper_liked_catrin[mp_slot]
    $ swyper_liked_ellie = mp_steam.swyper_liked_ellie[mp_slot]
    $ swyper_liked_ida = mp_steam.swyper_liked_ida[mp_slot]
    $ swyper_liked_micha = mp_steam.swyper_liked_micha[mp_slot]
    $ swyper_liked_nicole = mp_steam.swyper_liked_nicole[mp_slot]
    $ swyper_liked_nora = mp_steam.swyper_liked_nora[mp_slot]
    $ swyper_liked_paula = mp_steam.swyper_liked_paula[mp_slot]
    $ swyper_micha_history.extend(mp_steam.swyper_micha_history[mp_slot])
    $ swyper_micha_state = mp_steam.swyper_micha_state[mp_slot]
    $ swyper_nicole_history.extend(mp_steam.swyper_nicole_history[mp_slot])
    $ swyper_nicole_state = mp_steam.swyper_nicole_state[mp_slot]
    $ swyper_nora_history.extend(mp_steam.swyper_nora_history[mp_slot])
    $ swyper_nora_state = mp_steam.swyper_nora_state[mp_slot]
    $ swyper_paula_history.extend(mp_steam.swyper_paula_history[mp_slot])
    $ swyper_paula_state = mp_steam.swyper_paula_state[mp_slot]
    $ swyper_rejected_by_arieth = mp_steam.swyper_rejected_by_arieth[mp_slot]
    $ swyper_rejected_by_cathy = mp_steam.swyper_rejected_by_cathy[mp_slot]
    $ swyper_rejected_by_catrin = mp_steam.swyper_rejected_by_catrin[mp_slot]
    $ swyper_rejected_by_ellie = mp_steam.swyper_rejected_by_ellie[mp_slot]
    $ swyper_rejected_by_ida = mp_steam.swyper_rejected_by_ida[mp_slot]
    $ swyper_rejected_by_micha = mp_steam.swyper_rejected_by_micha[mp_slot]
    $ swyper_rejected_by_nicole = mp_steam.swyper_rejected_by_nicole[mp_slot]
    $ swyper_rejected_by_nora = mp_steam.swyper_rejected_by_nora[mp_slot]
    $ swyper_rejected_by_paula = mp_steam.swyper_rejected_by_paula[mp_slot]
    $ totalChickChoices = mp_steam.totalChickChoices[mp_slot]
    $ totalDikChoices = mp_steam.totalDikChoices[mp_slot]
    $ tutorials = mp_steam.tutorials[mp_slot]
    $ wallet_lvl = mp_steam.wallet_lvl[mp_slot]
    $ ep8_quinn_lewd = mp_steam.ep8_quinn_lewd[mp_slot]
    $ ep8_ball_game_won = mp_steam.ep8_ball_game_won[mp_slot]
    $ npenalty = mp_steam.npenalty[mp_slot]
    $ ep8_sage_stay_night = mp_steam.ep8_sage_stay_night[mp_slot]
    $ mc_info = mp_steam.mc_info[mp_slot]

    if not persistent.mc_tut_message:
        $ persistent.mc_tut_message = mp_steam.mc_tut_message[mp_slot]
    if not persistent.ep2_c1:
        $ persistent.ep2_c1 = mp_steam.ep2_c1[mp_slot]
    if not persistent.ep3_c1:
        $ persistent.ep3_c1 = mp_steam.ep3_c1[mp_slot]
    if not persistent.ep4_c1:
        $ persistent.ep4_c1 = mp_steam.ep4_c1[mp_slot]
    if not persistent.ep5_c1:
        $ persistent.ep5_c1 = mp_steam.ep5_c1[mp_slot]
    if not persistent.ep6_c1:
        $ persistent.ep6_c1 = mp_steam.ep6_c1[mp_slot]
    if not persistent.ep7_c1:
        $ persistent.ep7_c1 = mp_steam.ep7_c1[mp_slot]
    if not persistent.ep8_c1:
        $ persistent.ep8_c1 = mp_steam.ep8_c1[mp_slot]

    if not persistent.triple_tile_challenge:
        $ persistent.triple_tile_challenge = mp_steam.triple_tile_challenge[mp_slot]
    if mp_steam.pancake_highscore[mp_slot] > persistent.pancake_highscore:
        $ persistent.pancake_highscore = mp_steam.pancake_highscore[mp_slot]

    if mp_steam.ep7_wpi1[mp_slot]:
        $ persistent.ep7_wpi1 = mp_steam.ep7_wpi1[mp_slot]
    if mp_steam.ep7_wpi2[mp_slot]:
        $ persistent.ep7_wpi2 = mp_steam.ep7_wpi2[mp_slot]
    if mp_steam.ep7_wpj1[mp_slot]:
        $ persistent.ep7_wpj1 = mp_steam.ep7_wpj1[mp_slot]
    if mp_steam.ep7_wpj2[mp_slot]:
        $ persistent.ep7_wpj2 = mp_steam.ep7_wpj2[mp_slot]
    if mp_steam.ep7_wpjo1[mp_slot]:
        $ persistent.ep7_wpjo1 = mp_steam.ep7_wpjo1[mp_slot]
    if mp_steam.ep7_wpjo2[mp_slot]:
        $ persistent.ep7_wpjo2 = mp_steam.ep7_wpjo2[mp_slot]
    if mp_steam.ep7_wpm1[mp_slot]:
        $ persistent.ep7_wpm1 = mp_steam.ep7_wpm1[mp_slot]
    if mp_steam.ep7_wpm2[mp_slot]:
        $ persistent.ep7_wpm2 = mp_steam.ep7_wpm2[mp_slot]
    if mp_steam.ep7_wps1[mp_slot]:
        $ persistent.ep7_wps1 = mp_steam.ep7_wps1[mp_slot]
    if mp_steam.ep7_wps2[mp_slot]:
        $ persistent.ep7_wps2 = mp_steam.ep7_wps2[mp_slot]
    if mp_steam.ep8_wpi1[mp_slot]:
        $ persistent.ep8_wpi1 = mp_steam.ep8_wpi1[mp_slot]
    if mp_steam.ep8_wpj1[mp_slot]:
        $ persistent.ep8_wpj1 = mp_steam.ep8_wpj1[mp_slot]
    if mp_steam.ep8_wpjo1[mp_slot]:
        $ persistent.ep8_wpjo1 = mp_steam.ep8_wpjo1[mp_slot]
    if mp_steam.ep8_wpm1[mp_slot]:
        $ persistent.ep8_wpm1 = mp_steam.ep8_wpm1[mp_slot]
    if mp_steam.ep8_wpq1[mp_slot]:
        $ persistent.ep8_wpq1 = mp_steam.ep8_wpq1[mp_slot]
    if mp_steam.ep8_wps1[mp_slot]:
        $ persistent.ep8_wps1 = mp_steam.ep8_wps1[mp_slot]
    if mp_steam.ep8_wpe1[mp_slot]:
        $ persistent.ep8_wpe1 = mp_steam.ep8_wpe1[mp_slot]
    if mp_steam.ep8_wpjade1[mp_slot]:
        $ persistent.ep8_wpjade1 = mp_steam.ep8_wpjade1[mp_slot]
    $ persistent.ep8_wpmad1 = True
    if mp_steam.basket_score[mp_slot][0][1] > persistent.basket_score[0][1]:
        $ persistent.basket_score = mp_steam.basket_score[mp_slot]
    if mp_steam.triple_tile_highscores[mp_slot][0][0] > persistent.triple_tile_highscores[0][0]:
        $ persistent.triple_tile_highscores = mp_steam.triple_tile_highscores[mp_slot]
    if mp_steam.triple_tile_highscores_easy[mp_slot][0][0] > persistent.triple_tile_highscores_easy[0][0]:
        $ persistent.triple_tile_highscores_easy = mp_steam.triple_tile_highscores_easy[mp_slot]

    python:
        for x in range(0,len(mp_steam.art_unlocked_lvl1[mp_slot])):
            if mp_steam.art_unlocked_lvl1[mp_slot][x]:
                if x < 10:
                    persistent.art_unlocked_lvl1[x] = True
                else:
                    persistent.art_unlocked_lvl1[x+1] = True
        for x in range(0,len(mp_steam.art_unlocked_lvl2[mp_slot])):
            if mp_steam.art_unlocked_lvl2[mp_slot][x]:
                if x < 10:
                    persistent.art_unlocked_lvl2[x] = True
                else:
                    persistent.art_unlocked_lvl2[x+1] = True
        for x in range(0,len(mp_steam.art_unlocked_lvl3[mp_slot])):
            if mp_steam.art_unlocked_lvl3[mp_slot][x]:
                if x < 10:
                    persistent.art_unlocked_lvl3[x] = True
                else:
                    persistent.art_unlocked_lvl3[x+1] = True
else:
    $ RPderek = mp.RPderek[mp_slot]
    $ RPdiks = mp.RPdiks[mp_slot]
    $ RPhot = mp.RPhot[mp_slot]
    $ RPisabella = mp.RPisabella[mp_slot]
    $ RPjill = mp.RPjill[mp_slot]
    $ RPjocks = mp.RPjocks[mp_slot]
    $ RPjosy = mp.RPjosy[mp_slot]
    $ RPmaya = mp.RPmaya[mp_slot]
    $ RPnerds = mp.RPnerds[mp_slot]
    $ RPpreps = mp.RPpreps[mp_slot]
    $ RPsage = mp.RPsage[mp_slot]
    $ acceptedMoneyFromDad = mp.acceptedMoneyFromDad[mp_slot]
    $ affinity = mp.affinity[mp_slot]
    $ art_girl_crit1_list.extend(mp.art_girl_crit1_list[mp_slot])
    $ art_girl_crit2_list.extend(mp.art_girl_crit2_list[mp_slot])
    $ art_girl_crit3_list.extend(mp.art_girl_crit3_list[mp_slot])
    $ art_girl_level_list.extend(mp.art_girl_level_list[mp_slot])
    $ art_girl_list.extend(mp.art_girl_list[mp_slot])
    $ art_girl_lvl1_list.extend(mp.art_girl_lvl1_list[mp_slot])
    $ art_girl_lvl2_list.extend(mp.art_girl_lvl2_list[mp_slot])
    $ art_girl_lvl3_list.extend(mp.art_girl_lvl3_list[mp_slot])

    $ art_girl_new_icon.extend(mp.art_girl_new_icon[mp_slot])
    $ art_order_lvl1_list.extend(mp.art_order_lvl1_list[mp_slot])
    $ art_order_lvl2_list.extend(mp.art_order_lvl2_list[mp_slot])
    $ art_order_lvl3_list.extend(mp.art_order_lvl3_list[mp_slot])
    $ assman = mp.assman[mp_slot]
    $ bonusPointsSports = mp.bonusPointsSports[mp_slot]
    $ bonusPointsSportsDerek = mp.bonusPointsSportsDerek[mp_slot]
    $ branchAlone = mp.branchAlone[mp_slot]
    $ branchIsabella = mp.branchIsabella[mp_slot]
    $ branchJill = mp.branchJill[mp_slot]
    $ branchMayaJosy = mp.branchMayaJosy[mp_slot]
    $ branchSage = mp.branchSage[mp_slot]
    $ brawler_difficulty = mp.brawler_difficulty[mp_slot]
    $ brawler_hard_mode = mp.brawler_hard_mode[mp_slot]
    $ camila = mp.camila[mp_slot]
    $ cathy = mp.cathy[mp_slot]
    $ cpenalty = mp.cpenalty[mp_slot]
    $ current_notification_sound = mp.current_notification_sound[mp_slot]
    $ dik = mp.dik[mp_slot]
    $ dollar = mp.dollar[mp_slot]
    $ dpenalty = mp.dpenalty[mp_slot]
    $ dtype = mp.dtype[mp_slot]
    $ earnedMoney = mp.earnedMoney[mp_slot]
    $ englishBoost = mp.englishBoost[mp_slot]
    $ englishCheatBoost = mp.englishCheatBoost[mp_slot]
    $ envyLikesYou = mp.envyLikesYou[mp_slot]
    $ ep1_accepted_quinn_offer = mp.ep1_accepted_quinn_offer[mp_slot]
    $ ep1_beat_up_troy = mp.ep1_beat_up_troy[mp_slot]
    $ ep1_beat_up_troy_won = mp.ep1_beat_up_troy_won[mp_slot]
    $ ep1_bought_student_soda = mp.ep1_bought_student_soda[mp_slot]
    $ ep1_insulted_cafeteria_worker = mp.ep1_insulted_cafeteria_worker[mp_slot]
    $ ep1_josy_prefer_beer = mp.ep1_josy_prefer_beer[mp_slot]
    $ ep1_josy_prefer_flowers = mp.ep1_josy_prefer_flowers[mp_slot]
    $ ep1_josy_prefer_wine = mp.ep1_josy_prefer_wine[mp_slot]
    $ ep1_lewd_camila_quinn = mp.ep1_lewd_camila_quinn[mp_slot]
    $ ep1_maya_attracted = mp.ep1_maya_attracted[mp_slot]
    $ ep1_maya_question_bath = mp.ep1_maya_question_bath[mp_slot]
    $ ep1_maya_question_blanket = mp.ep1_maya_question_blanket[mp_slot]
    $ ep1_maya_question_indoors = mp.ep1_maya_question_indoors[mp_slot]
    $ ep1_maya_question_money = mp.ep1_maya_question_money[mp_slot]
    $ ep1_maya_question_party = mp.ep1_maya_question_party[mp_slot]
    $ ep2DefendedMayaAtParty = mp.ep2DefendedMayaAtParty[mp_slot]
    $ ep2FoughtJocks = mp.ep2FoughtJocks[mp_slot]
    $ ep2HelpedMayaAtParty = mp.ep2HelpedMayaAtParty[mp_slot]
    $ ep2HelpedStudent = mp.ep2HelpedStudent[mp_slot]
    $ ep2KissedSage = mp.ep2KissedSage[mp_slot]
    $ ep2QuinnSawYouAndSage = mp.ep2QuinnSawYouAndSage[mp_slot]
    $ ep2SageGuitarTeacher = mp.ep2SageGuitarTeacher[mp_slot]
    $ ep2_HitOnDadInText = mp.ep2_HitOnDadInText[mp_slot]
    $ ep2_TriedToKissMaya = mp.ep2_TriedToKissMaya[mp_slot]
    $ ep2_bellaStudy = mp.ep2_bellaStudy[mp_slot]
    $ ep2_boughtChocolate = mp.ep2_boughtChocolate[mp_slot]
    $ ep2_boughtFlowers = mp.ep2_boughtFlowers[mp_slot]
    $ ep2_cafeteriaWorkerInsulted = mp.ep2_cafeteriaWorkerInsulted[mp_slot]
    $ ep2_choseMayaOverParty = mp.ep2_choseMayaOverParty[mp_slot]
    $ ep2_comfortedSteve = mp.ep2_comfortedSteve[mp_slot]
    $ ep2_danceSage = mp.ep2_danceSage[mp_slot]
    $ ep2_dawe_fight_won = mp.ep2_dawe_fight_won[mp_slot]
    $ ep2_fingeredMaya = mp.ep2_fingeredMaya[mp_slot]
    $ ep2_flirtedJade = mp.ep2_flirtedJade[mp_slot]
    $ ep2_fuckHOT = mp.ep2_fuckHOT[mp_slot]
    $ ep2_fuckedJosy = mp.ep2_fuckedJosy[mp_slot]
    $ ep2_helpSageMore = mp.ep2_helpSageMore[mp_slot]
    $ ep2_helpedBellaKitchen = mp.ep2_helpedBellaKitchen[mp_slot]
    $ ep2_helpedBellaMask = mp.ep2_helpedBellaMask[mp_slot]
    $ ep2_jokedDawe = mp.ep2_jokedDawe[mp_slot]
    $ ep2_kissedSage = mp.ep2_kissedSage[mp_slot]
    $ ep2_negativeStance = mp.ep2_negativeStance[mp_slot]
    $ ep2_quinnKnowsAboutCamila = mp.ep2_quinnKnowsAboutCamila[mp_slot]
    $ ep2_recommendedSage = mp.ep2_recommendedSage[mp_slot]
    $ ep2_shotWon = mp.ep2_shotWon[mp_slot]
    $ ep2_stayWithMaya = mp.ep2_stayWithMaya[mp_slot]
    $ ep2_stole_money = mp.ep2_stole_money[mp_slot]
    $ ep2_textedMaya = mp.ep2_textedMaya[mp_slot]
    $ ep2_toldDerekLikedMaya = mp.ep2_toldDerekLikedMaya[mp_slot]
    $ ep2_toldMayaTruthAboutDate = mp.ep2_toldMayaTruthAboutDate[mp_slot]
    $ ep2_toldTommyBangSage = mp.ep2_toldTommyBangSage[mp_slot]
    $ ep2_tybaltPhotoMc = mp.ep2_tybaltPhotoMc[mp_slot]
    $ ep2_wonCumpetition = mp.ep2_wonCumpetition[mp_slot]
    $ ep3_BellaLewd = mp.ep3_BellaLewd[mp_slot]
    $ ep3_acceptedJade = mp.ep3_acceptedJade[mp_slot]
    $ ep3_bella_came_around = mp.ep3_bella_came_around[mp_slot]
    $ ep3_boobCompetition = mp.ep3_boobCompetition[mp_slot]
    $ ep3_boughtNickADance = mp.ep3_boughtNickADance[mp_slot]
    $ ep3_camilaDerek = mp.ep3_camilaDerek[mp_slot]
    $ ep3_chad_fight_won = mp.ep3_chad_fight_won[mp_slot]
    $ ep3_choseBella = mp.ep3_choseBella[mp_slot]
    $ ep3_choseDerek = mp.ep3_choseDerek[mp_slot]
    $ ep3_choseSage = mp.ep3_choseSage[mp_slot]
    $ ep3_cluckDerekState = mp.ep3_cluckDerekState[mp_slot]
    $ ep3_cluckJillState = mp.ep3_cluckJillState[mp_slot]
    $ ep3_cluckMayaState = mp.ep3_cluckMayaState[mp_slot]
    $ ep3_cluckQuinnState = mp.ep3_cluckQuinnState[mp_slot]
    $ ep3_dawe_prank = mp.ep3_dawe_prank[mp_slot]
    $ ep3_envyLewd = mp.ep3_envyLewd[mp_slot]
    $ ep3_fingered_maya = mp.ep3_fingered_maya[mp_slot]
    $ ep3_fuckedCamilaAndMona = mp.ep3_fuckedCamilaAndMona[mp_slot]
    $ ep3_fuckedRionaQuinn = mp.ep3_fuckedRionaQuinn[mp_slot]
    $ ep3_gotDickSigned = mp.ep3_gotDickSigned[mp_slot]
    $ ep3_handOnJadesThigh = mp.ep3_handOnJadesThigh[mp_slot]
    $ ep3_hellWeekHelmet = mp.ep3_hellWeekHelmet[mp_slot]
    $ ep3_hellWeekTryFuckJade = mp.ep3_hellWeekTryFuckJade[mp_slot]
    $ ep3_helpedCamilaAndMona = mp.ep3_helpedCamilaAndMona[mp_slot]
    $ ep3_intervenedChad = mp.ep3_intervenedChad[mp_slot]
    $ ep3_jillHelmetChad = mp.ep3_jillHelmetChad[mp_slot]
    $ ep3_jillHelmetLibrary = mp.ep3_jillHelmetLibrary[mp_slot]
    $ ep3_lilyDance = mp.ep3_lilyDance[mp_slot]
    $ ep3_lilyDerekDance = mp.ep3_lilyDerekDance[mp_slot]
    $ ep3_lilyHatesYou = mp.ep3_lilyHatesYou[mp_slot]
    $ ep3_mallHelmet = mp.ep3_mallHelmet[mp_slot]
    $ ep3_mansionHelmet = mp.ep3_mansionHelmet[mp_slot]
    $ ep3_mayaLewd = mp.ep3_mayaLewd[mp_slot]
    $ ep3_mayaOfferedHelp = mp.ep3_mayaOfferedHelp[mp_slot]
    $ ep3_paidBellaMeal = mp.ep3_paidBellaMeal[mp_slot]
    $ ep3_protectedElf = mp.ep3_protectedElf[mp_slot]
    $ ep3_sclubParty = mp.ep3_sclubParty[mp_slot]
    $ ep3_spankedSally = mp.ep3_spankedSally[mp_slot]
    $ ep3_threesomeOffer = mp.ep3_threesomeOffer[mp_slot]
    $ ep3_toldJillBullying = mp.ep3_toldJillBullying[mp_slot]
    $ ep3_wearHelmet = mp.ep3_wearHelmet[mp_slot]
    $ ep4_SageMovieEvent = mp.ep4_SageMovieEvent[mp_slot]
    $ ep4_bella_lewd = mp.ep4_bella_lewd[mp_slot]
    $ ep4_camilaOffer = mp.ep4_camilaOffer[mp_slot]
    $ ep4_cluckDaweState = mp.ep4_cluckDaweState[mp_slot]
    $ ep4_cluckDerekState = mp.ep4_cluckDerekState[mp_slot]
    $ ep4_cluckJillState = mp.ep4_cluckJillState[mp_slot]
    $ ep4_cluckSage2State = mp.ep4_cluckSage2State[mp_slot]
    $ ep4_derekFuckedArieth = mp.ep4_derekFuckedArieth[mp_slot]
    $ ep4_discussed_heather = mp.ep4_discussed_heather[mp_slot]
    $ ep4_discussed_melanie = mp.ep4_discussed_melanie[mp_slot]
    $ ep4_discussed_riona = mp.ep4_discussed_riona[mp_slot]
    $ ep4_fuckedJade = mp.ep4_fuckedJade[mp_slot]
    $ ep4_fuckedMelanie = mp.ep4_fuckedMelanie[mp_slot]
    $ ep4_fuckedSage = mp.ep4_fuckedSage[mp_slot]
    $ ep4_grindedLily = mp.ep4_grindedLily[mp_slot]
    $ ep4_hottest_ass = mp.ep4_hottest_ass[mp_slot]
    $ ep4_jadeOffer = mp.ep4_jadeOffer[mp_slot]
    $ ep4_jillNiceGuy = mp.ep4_jillNiceGuy[mp_slot]
    $ ep4_jillShower = mp.ep4_jillShower[mp_slot]
    $ ep4_join_chess_club = mp.ep4_join_chess_club[mp_slot]
    $ ep4_kissedJill = mp.ep4_kissedJill[mp_slot]
    $ ep4_kissedJill2 = mp.ep4_kissedJill2[mp_slot]
    $ ep4_kissedRiona = mp.ep4_kissedRiona[mp_slot]
    $ ep4_knowLily = mp.ep4_knowLily[mp_slot]
    $ ep4_lecturedBella = mp.ep4_lecturedBella[mp_slot]
    $ ep4_lickedAshley = mp.ep4_lickedAshley[mp_slot]
    $ ep4_likeQuinn = mp.ep4_likeQuinn[mp_slot]
    $ ep4_made_out_josy = mp.ep4_made_out_josy[mp_slot]
    $ ep4_missedSage = mp.ep4_missedSage[mp_slot]
    $ ep4_monaSlap = mp.ep4_monaSlap[mp_slot]
    $ ep4_morningHelmet = mp.ep4_morningHelmet[mp_slot]
    $ ep4_paidMagnarWedgie = mp.ep4_paidMagnarWedgie[mp_slot]
    $ ep4_pinkRoseEvent = mp.ep4_pinkRoseEvent[mp_slot]
    $ ep4_quinn_lewd = mp.ep4_quinn_lewd[mp_slot]
    $ ep4_rejectedJade = mp.ep4_rejectedJade[mp_slot]
    $ ep4_rejectedMayaJosy = mp.ep4_rejectedMayaJosy[mp_slot]
    $ ep4_roseLewd = mp.ep4_roseLewd[mp_slot]
    $ ep4_sageLikeDaringSex = mp.ep4_sageLikeDaringSex[mp_slot]
    $ ep4_sage_drink = mp.ep4_sage_drink[mp_slot]
    $ ep4_saturdayHelmet = mp.ep4_saturdayHelmet[mp_slot]
    $ ep4_smoked_weed = mp.ep4_smoked_weed[mp_slot]
    $ ep4_toldDerekAboutCathy = mp.ep4_toldDerekAboutCathy[mp_slot]
    $ ep4_toldDerekAboutJade = mp.ep4_toldDerekAboutJade[mp_slot]
    $ ep4_toldDerekYouTrustHim = mp.ep4_toldDerekYouTrustHim[mp_slot]
    $ ep4_toldElenaInterested = mp.ep4_toldElenaInterested[mp_slot]
    $ ep4_touchedJillsBreasts = mp.ep4_touchedJillsBreasts[mp_slot]
    $ ep4_ugliest_ass = mp.ep4_ugliest_ass[mp_slot]
    $ ep4_wantedMoreMayaJosy = mp.ep4_wantedMoreMayaJosy[mp_slot]
    $ ep4_wearHelmet = mp.ep4_wearHelmet[mp_slot]
    $ ep4_wonTennis = mp.ep4_wonTennis[mp_slot]
    $ ep5_agitatedCaleb = mp.ep5_agitatedCaleb[mp_slot]
    $ ep5_bella_lewd = mp.ep5_bella_lewd[mp_slot]
    $ ep5_bella_remember_song = mp.ep5_bella_remember_song[mp_slot]
    $ ep5_bella_sauna = mp.ep5_bella_sauna[mp_slot]
    $ ep5_caleb_fight_won = mp.ep5_caleb_fight_won[mp_slot]
    $ ep5_cathy_lewd = mp.ep5_cathy_lewd[mp_slot]
    $ ep5_cluckAnthonyState = mp.ep5_cluckAnthonyState[mp_slot]
    $ ep5_cluckCamilaState = mp.ep5_cluckCamilaState[mp_slot]
    $ ep5_cluckDerekState = mp.ep5_cluckDerekState[mp_slot]
    $ ep5_cluckJadeState = mp.ep5_cluckJadeState[mp_slot]
    $ ep5_cluckJillState = mp.ep5_cluckJillState[mp_slot]
    $ ep5_cluckJosyState = mp.ep5_cluckJosyState[mp_slot]
    $ ep5_cluckLilyState = mp.ep5_cluckLilyState[mp_slot]
    $ ep5_cluckRionaState = mp.ep5_cluckRionaState[mp_slot]
    $ ep5_confide_sage = mp.ep5_confide_sage[mp_slot]
    $ ep5_confrontedRiona = mp.ep5_confrontedRiona[mp_slot]
    $ ep5_derekPoints = mp.ep5_derekPoints[mp_slot]
    $ ep5_dikSecret = mp.ep5_dikSecret[mp_slot]
    $ ep5_dikWinner = mp.ep5_dikWinner[mp_slot]
    $ ep5_feelingsForJosy = mp.ep5_feelingsForJosy[mp_slot]
    $ ep5_feelingsForMaya = mp.ep5_feelingsForMaya[mp_slot]
    $ ep5_followed_josy = mp.ep5_followed_josy[mp_slot]
    $ ep5_followed_maya = mp.ep5_followed_maya[mp_slot]
    $ ep5_fuckedCamila = mp.ep5_fuckedCamila[mp_slot]
    $ ep5_fuckedRiona = mp.ep5_fuckedRiona[mp_slot]
    $ ep5_fuckedSage = mp.ep5_fuckedSage[mp_slot]
    $ ep5_fucked_josy = mp.ep5_fucked_josy[mp_slot]
    $ ep5_fucked_maya = mp.ep5_fucked_maya[mp_slot]
    $ ep5_gave_riona_money = mp.ep5_gave_riona_money[mp_slot]
    $ ep5_help_josy = mp.ep5_help_josy[mp_slot]
    $ ep5_hot_lewd = mp.ep5_hot_lewd[mp_slot]
    $ ep5_josy_shaven = mp.ep5_josy_shaven[mp_slot]
    $ ep5_kissed_jill = mp.ep5_kissed_jill[mp_slot]
    $ ep5_like_champagne = mp.ep5_like_champagne[mp_slot]
    $ ep5_lily_lewd = mp.ep5_lily_lewd[mp_slot]
    $ ep5_look_at_mel = mp.ep5_look_at_mel[mp_slot]
    $ ep5_look_at_sarah = mp.ep5_look_at_sarah[mp_slot]
    $ ep5_mcPoints = mp.ep5_mcPoints[mp_slot]
    $ ep5_painted_fence = mp.ep5_painted_fence[mp_slot]
    $ ep5_peeked_jb = mp.ep5_peeked_jb[mp_slot]
    $ ep5_preferCathyTits = mp.ep5_preferCathyTits[mp_slot]
    $ ep5_punchedTybalt = mp.ep5_punchedTybalt[mp_slot]
    $ ep5_smoked_weed = mp.ep5_smoked_weed[mp_slot]
    $ ep6_accept_tommy = mp.ep6_accept_tommy[mp_slot]
    $ ep6_apologized_dany = mp.ep6_apologized_dany[mp_slot]
    $ ep6_bella_lewd = mp.ep6_bella_lewd[mp_slot]
    $ ep6_blamed_derek = mp.ep6_blamed_derek[mp_slot]
    $ ep6_cared = mp.ep6_cared[mp_slot]
    $ ep6_choseJillOverSage = mp.ep6_choseJillOverSage[mp_slot]
    $ ep6_cluckDaweState = mp.ep6_cluckDaweState[mp_slot]
    $ ep6_cluckDerekState = mp.ep6_cluckDerekState[mp_slot]
    $ ep6_cluckJosyState = mp.ep6_cluckJosyState[mp_slot]
    $ ep6_cluckMayaState = mp.ep6_cluckMayaState[mp_slot]
    $ ep6_cluckMelanieState = mp.ep6_cluckMelanieState[mp_slot]
    $ ep6_cluckTybaltState = mp.ep6_cluckTybaltState[mp_slot]
    $ ep6_different_song = mp.ep6_different_song[mp_slot]
    $ ep6_dng_ending = mp.ep6_dng_ending[mp_slot]
    $ ep6_dng_seduce = mp.ep6_dng_seduce[mp_slot]
    $ ep6_envy_lewd = mp.ep6_envy_lewd[mp_slot]
    $ ep6_fakeID = mp.ep6_fakeID[mp_slot]
    $ ep6_flirted_heather = mp.ep6_flirted_heather[mp_slot]
    $ ep6_foughtTommy = mp.ep6_foughtTommy[mp_slot]
    $ ep6_genderMaya = mp.ep6_genderMaya[mp_slot]
    $ ep6_helpSage = mp.ep6_helpSage[mp_slot]
    $ ep6_jamjam = mp.ep6_jamjam[mp_slot]
    $ ep6_jill_lewd = mp.ep6_jill_lewd[mp_slot]
    $ ep6_like_maya = mp.ep6_like_maya[mp_slot]
    $ ep6_looked_elena = mp.ep6_looked_elena[mp_slot]
    $ ep6_maya_library_question = mp.ep6_maya_library_question[mp_slot]
    $ ep6_mj_lunch = mp.ep6_mj_lunch[mp_slot]
    $ ep6_nora_lewd = mp.ep6_nora_lewd[mp_slot]
    $ ep6_quinn_lewd = mp.ep6_quinn_lewd[mp_slot]
    $ ep6_reject_jade = mp.ep6_reject_jade[mp_slot]
    $ ep6_rejected_sarah = mp.ep6_rejected_sarah[mp_slot]
    $ ep6_sarah_lewd = mp.ep6_sarah_lewd[mp_slot]
    $ ep6_suck_lily = mp.ep6_suck_lily[mp_slot]
    $ ep6_tommy_fight_won = mp.ep6_tommy_fight_won[mp_slot]
    $ ep6_vipPass = mp.ep6_vipPass[mp_slot]
    $ ep7_3outof5 = mp.ep7_3outof5[mp_slot]
    $ ep7_accept_madame = mp.ep7_accept_madame[mp_slot]
    $ ep7_alphas_leave = mp.ep7_alphas_leave[mp_slot]
    $ ep7_becky_lewd = mp.ep7_becky_lewd[mp_slot]
    $ ep7_becky_puke = mp.ep7_becky_puke[mp_slot]
    $ ep7_bella_lewd = mp.ep7_bella_lewd[mp_slot]
    $ ep7_bella_rejected_you = mp.ep7_bella_rejected_you[mp_slot]
    $ ep7_brawler_sage_win = mp.ep7_brawler_sage_win[mp_slot]
    $ ep7_camila_lewd = mp.ep7_camila_lewd[mp_slot]
    $ ep7_current_desk_painting = mp.ep7_current_desk_painting[mp_slot]
    $ ep7_dentures = mp.ep7_dentures[mp_slot]
    $ ep7_dodged_josy = mp.ep7_dodged_josy[mp_slot]
    $ ep7_got_flower = mp.ep7_got_flower[mp_slot]
    $ ep7_heather_drink = mp.ep7_heather_drink[mp_slot]
    $ ep7_heather_likes_you = mp.ep7_heather_likes_you[mp_slot]
    $ ep7_hit_on_becky = mp.ep7_hit_on_becky[mp_slot]
    $ ep7_hot_ashley_phase = mp.ep7_hot_ashley_phase[mp_slot]
    $ ep7_hot_jacob_phase = mp.ep7_hot_jacob_phase[mp_slot]
    $ ep7_hug_maya = mp.ep7_hug_maya[mp_slot]
    $ ep7_jill_jealous = mp.ep7_jill_jealous[mp_slot]
    $ ep7_jill_lewd = mp.ep7_jill_lewd[mp_slot]
    $ ep7_jill_run = mp.ep7_jill_run[mp_slot]
    $ ep7_jill_talk = mp.ep7_jill_talk[mp_slot]
    $ ep7_josy_comfort = mp.ep7_josy_comfort[mp_slot]
    $ ep7_josy_lewd = mp.ep7_josy_lewd[mp_slot]
    $ ep7_josy_lewd2 = mp.ep7_josy_lewd2[mp_slot]
    $ ep7_kiss_josy = mp.ep7_kiss_josy[mp_slot]
    $ ep7_left_with_josy = mp.ep7_left_with_josy[mp_slot]
    $ ep7_like_quinn = mp.ep7_like_quinn[mp_slot]
    $ ep7_lily_lewd = mp.ep7_lily_lewd[mp_slot]
    $ ep7_madame_options_list.extend(mp.ep7_madame_options_list[mp_slot])
    $ ep7_pathSage = mp.ep7_pathSage[mp_slot]
    $ ep7_patrick_score = mp.ep7_patrick_score[mp_slot]
    $ ep7_pinkrose = mp.ep7_pinkrose[mp_slot]
    $ ep7_quinn_cluck = mp.ep7_quinn_cluck[mp_slot]
    $ ep7_quinn_lewd = mp.ep7_quinn_lewd[mp_slot]
    $ ep7_rejected_cathy = mp.ep7_rejected_cathy[mp_slot]
    $ ep7_rica_lewd = mp.ep7_rica_lewd[mp_slot]
    $ ep7_riona_help = mp.ep7_riona_help[mp_slot]
    $ ep7_riona_lewd = mp.ep7_riona_lewd[mp_slot]
    $ ep7_riona_payback = mp.ep7_riona_payback[mp_slot]
    $ ep7_ruined_presentation = mp.ep7_ruined_presentation[mp_slot]
    $ ep7_sage_fight_won = mp.ep7_sage_fight_won[mp_slot]
    $ ep7_sage_lewd = mp.ep7_sage_lewd[mp_slot]
    $ ep7_solo_josy = mp.ep7_solo_josy[mp_slot]
    $ ep7_solo_maya = mp.ep7_solo_maya[mp_slot]
    $ ep7_solo_quinn = mp.ep7_solo_quinn[mp_slot]
    $ ep7_told_heather_tommy_cheated = mp.ep7_told_heather_tommy_cheated[mp_slot]
    $ ep7_tybalt_state = mp.ep7_tybalt_state[mp_slot]
    $ ep7_wingman_derek = mp.ep7_wingman_derek[mp_slot]
    $ ep7_wonTennis = mp.ep7_wonTennis[mp_slot]
    $ ep8_current_second_painting = mp.ep8_current_second_painting[mp_slot]
    $ ep8_elena_shot = mp.ep8_elena_shot[mp_slot]
    $ ep8_envy_lewd = mp.ep8_envy_lewd[mp_slot]
    $ ep8_flower_water_level = mp.ep8_flower_water_level[mp_slot]
    $ ep8_handle_bella = mp.ep8_handle_bella[mp_slot]
    $ ep8_help_jm_with_room = mp.ep8_help_jm_with_room[mp_slot]
    $ ep8_help_nick = mp.ep8_help_nick[mp_slot]
    $ ep8_jade_lewd = mp.ep8_jade_lewd[mp_slot]
    $ ep8_jill_rejected_you = mp.ep8_jill_rejected_you[mp_slot]
    $ ep8_jill_state = mp.ep8_jill_state[mp_slot]
    $ ep8_josy_dance = mp.ep8_josy_dance[mp_slot]
    $ ep8_josy_lewd = mp.ep8_josy_lewd[mp_slot]
    $ ep8_leons_side = mp.ep8_leons_side[mp_slot]
    $ ep8_lily_lewd = mp.ep8_lily_lewd[mp_slot]
    $ ep8_mansion_won = mp.ep8_mansion_won[mp_slot]
    $ ep8_maya_lewd = mp.ep8_maya_lewd[mp_slot]
    $ ep8_melanie_lewd = mp.ep8_melanie_lewd[mp_slot]
    $ ep8_midterms_cheated = mp.ep8_midterms_cheated[mp_slot]
    $ ep8_nora_number = mp.ep8_nora_number[mp_slot]
    $ ep8_pink_rose_picture = mp.ep8_pink_rose_picture[mp_slot]
    $ ep8_quinn_rejected_you = mp.ep8_quinn_rejected_you[mp_slot]
    $ ep8_recital_failed = mp.ep8_recital_failed[mp_slot]
    $ ep8_revenge = mp.ep8_revenge[mp_slot]
    $ ep8_sandy_lewd = mp.ep8_sandy_lewd[mp_slot]
    $ ep8_sarah_lewd = mp.ep8_sarah_lewd[mp_slot]
    $ ep8_second_painting = mp.ep8_second_painting[mp_slot]
    $ ep8_share_room = mp.ep8_share_room[mp_slot]
    $ ep8_sq_lewd = mp.ep8_sq_lewd[mp_slot]
    $ ep8_told_josy_chad = mp.ep8_told_josy_chad[mp_slot]
    $ ep8_told_sage_chad_troy = mp.ep8_told_sage_chad_troy[mp_slot]
    $ ep8_prep_truce = mp.ep8_prep_truce[mp_slot]
    $ ep8_quinn_cluck = mp.ep8_quinn_cluck[mp_slot]
    $ event_list.extend(mp.event_list[mp_slot])
    $ failedEnglish = mp.failedEnglish[mp_slot]
    $ failedGame = mp.failedGame[mp_slot]
    $ failedGender = mp.failedGender[mp_slot]
    $ failedMath = mp.failedMath[mp_slot]
    $ firstTimeFreeRoam = mp.firstTimeFreeRoam[mp_slot]
    $ freeRoamID = mp.freeRoamID[mp_slot]
    $ gameBoost = mp.gameBoost[mp_slot]
    $ intervenedChad = mp.intervenedChad[mp_slot]
    $ isabella = mp.isabella[mp_slot]
    $ jade = mp.jade[mp_slot]
    $ jill = mp.jill[mp_slot]
    $ josy = mp.josy[mp_slot]
    $ laptop_wallpapers.extend(mp.laptop_wallpapers[mp_slot])
    $ laptop_wallpapers_criteria_met.extend(mp.laptop_wallpapers_criteria_met[mp_slot])
    $ laptop_wallpapers_unlocked.extend(mp.laptop_wallpapers_unlocked[mp_slot])
    $ madame = mp.madame[mp_slot]
    $ majorchick = mp.majorchick[mp_slot]
    $ majordik = mp.majordik[mp_slot]
    $ mansion_money = mp.mansion_money[mp_slot]
    $ mansion_score = mp.mansion_score[mp_slot]
    $ mathBoost = mp.mathBoost[mp_slot]
    $ mathCheatBoost = mp.mathCheatBoost[mp_slot]
    $ maxedEnglish = mp.maxedEnglish[mp_slot]
    $ maxedEnglish_s2 = mp.maxedEnglish_s2[mp_slot]
    $ maxedGender = mp.maxedGender[mp_slot]
    $ maxedGender_s2 = mp.maxedGender_s2[mp_slot]
    $ maxedMath = mp.maxedMath[mp_slot]
    $ maxedMath_s2 = mp.maxedMath_s2[mp_slot]
    $ maxedPaintPaths = mp.maxedPaintPaths[mp_slot]
    $ maxedPaths = mp.maxedPaths[mp_slot]
    $ maxedPaths_s2 = mp.maxedPaths_s2[mp_slot]
    $ maya = mp.maya[mp_slot]
    $ mbios_history_alex.extend(mp.mbios_history_alex[mp_slot])
    $ mbios_history_anthony.extend(mp.mbios_history_anthony[mp_slot])
    $ mbios_history_arieth.extend(mp.mbios_history_arieth[mp_slot])
    $ mbios_history_ashley.extend(mp.mbios_history_ashley[mp_slot])
    $ mbios_history_becky.extend(mp.mbios_history_becky[mp_slot])
    $ mbios_history_bert.extend(mp.mbios_history_bert[mp_slot])
    $ mbios_history_beth.extend(mp.mbios_history_beth[mp_slot])
    $ mbios_history_brandi.extend(mp.mbios_history_brandi[mp_slot])
    $ mbios_history_burke.extend(mp.mbios_history_burke[mp_slot])
    $ mbios_history_caleb.extend(mp.mbios_history_caleb[mp_slot])
    $ mbios_history_camila.extend(mp.mbios_history_camila[mp_slot])
    $ mbios_history_cathy.extend(mp.mbios_history_cathy[mp_slot])
    $ mbios_history_chad.extend(mp.mbios_history_chad[mp_slot])
    $ mbios_history_christian.extend(mp.mbios_history_christian[mp_slot])
    $ mbios_history_dad.extend(mp.mbios_history_dad[mp_slot])
    $ mbios_history_dany.extend(mp.mbios_history_dany[mp_slot])
    $ mbios_history_darius.extend(mp.mbios_history_darius[mp_slot])
    $ mbios_history_dawe.extend(mp.mbios_history_dawe[mp_slot])
    $ mbios_history_derek.extend(mp.mbios_history_derek[mp_slot])
    $ mbios_history_elena.extend(mp.mbios_history_elena[mp_slot])
    $ mbios_history_envy.extend(mp.mbios_history_envy[mp_slot])
    $ mbios_history_eugene.extend(mp.mbios_history_eugene[mp_slot])
    $ mbios_history_gordon.extend(mp.mbios_history_gordon[mp_slot])
    $ mbios_history_heather.extend(mp.mbios_history_heather[mp_slot])
    $ mbios_history_isabella.extend(mp.mbios_history_isabella[mp_slot])
    $ mbios_history_jacob.extend(mp.mbios_history_jacob[mp_slot])
    $ mbios_history_jade.extend(mp.mbios_history_jade[mp_slot])
    $ mbios_history_jamie.extend(mp.mbios_history_jamie[mp_slot])
    $ mbios_history_jill.extend(mp.mbios_history_jill[mp_slot])
    $ mbios_history_jimmy.extend(mp.mbios_history_jimmy[mp_slot])
    $ mbios_history_john.extend(mp.mbios_history_john[mp_slot])
    $ mbios_history_johnboy.extend(mp.mbios_history_johnboy[mp_slot])
    $ mbios_history_josy.extend(mp.mbios_history_josy[mp_slot])
    $ mbios_history_karen.extend(mp.mbios_history_karen[mp_slot])
    $ mbios_history_leon.extend(mp.mbios_history_leon[mp_slot])
    $ mbios_history_lily.extend(mp.mbios_history_lily[mp_slot])
    $ mbios_history_linda.extend(mp.mbios_history_linda[mp_slot])
    $ mbios_history_lucas.extend(mp.mbios_history_lucas[mp_slot])
    $ mbios_history_lynette.extend(mp.mbios_history_lynette[mp_slot])
    $ mbios_history_magnar.extend(mp.mbios_history_magnar[mp_slot])
    $ mbios_history_madame.extend(mp.mbios_history_madame[mp_slot])
    $ mbios_history_maya.extend(mp.mbios_history_maya[mp_slot])
    $ mbios_history_mc.extend(mp.mbios_history_mc[mp_slot])
    $ mbios_history_melanie.extend(mp.mbios_history_melanie[mp_slot])
    $ mbios_history_minny.extend(mp.mbios_history_minny[mp_slot])
    $ mbios_history_mona.extend(mp.mbios_history_mona[mp_slot])
    $ mbios_history_nick.extend(mp.mbios_history_nick[mp_slot])
    $ mbios_history_patrick.extend(mp.mbios_history_patrick[mp_slot])
    $ mbios_history_pete.extend(mp.mbios_history_pete[mp_slot])
    $ mbios_history_rich.extend(mp.mbios_history_rich[mp_slot])
    $ mbios_history_quinn.extend(mp.mbios_history_quinn[mp_slot])
    $ mbios_history_riona.extend(mp.mbios_history_riona[mp_slot])
    $ mbios_history_ron.extend(mp.mbios_history_ron[mp_slot])
    $ mbios_history_rose.extend(mp.mbios_history_rose[mp_slot])
    $ mbios_history_rusty.extend(mp.mbios_history_rusty[mp_slot])
    $ mbios_history_sage.extend(mp.mbios_history_sage[mp_slot])
    $ mbios_history_sally.extend(mp.mbios_history_sally[mp_slot])
    $ mbios_history_sandy.extend(mp.mbios_history_sandy[mp_slot])
    $ mbios_history_sarah.extend(mp.mbios_history_sarah[mp_slot])
    $ mbios_history_stanley.extend(mp.mbios_history_stanley[mp_slot])
    $ mbios_history_steve.extend(mp.mbios_history_steve[mp_slot])
    $ mbios_history_tommy.extend(mp.mbios_history_tommy[mp_slot])
    $ mbios_history_trent.extend(mp.mbios_history_trent[mp_slot])
    $ mbios_history_troy.extend(mp.mbios_history_troy[mp_slot])
    $ mbios_history_tybalt.extend(mp.mbios_history_tybalt[mp_slot])
    $ mbios_history_vinny.extend(mp.mbios_history_vinny[mp_slot])
    $ mbios_history_wendy.extend(mp.mbios_history_wendy[mp_slot])
    $ mbios_history_zoey.extend(mp.mbios_history_zoey[mp_slot])
    $ mbios_mc = mp.mbios_mc[mp_slot]
    $ mbios_mc_hover = mp.mbios_mc_hover[mp_slot]
    $ mbios_mc_new = mp.mbios_mc_new[mp_slot]
    $ mbios_mc_new_hover = mp.mbios_mc_new_hover[mp_slot]
    $ mc_avatar = mp.mc_avatar[mp_slot]
    $ mc_camila = mp.mc_camila[mp_slot]
    $ mc_cathy = mp.mc_cathy[mp_slot]
    $ mc_de = mp.mc_de[mp_slot]
    $ mc_de_up = mp.mc_de_up[mp_slot]
    $ mc_isabella = mp.mc_isabella[mp_slot]
    $ mc_jade = mp.mc_jade[mp_slot]
    $ mc_jill = mp.mc_jill[mp_slot]
    $ mc_josy = mp.mc_josy[mp_slot]
    $ mc_maya = mp.mc_maya[mp_slot]
    $ mc_quinn = mp.mc_quinn[mp_slot]
    $ mc_riona = mp.mc_riona[mp_slot]
    $ mc_sage = mp.mc_sage[mp_slot]
    $ minigames = mp.minigames[mp_slot]
    $ money = mp.money[mp_slot]
    $ mphone_bios_chars.extend(mp.mphone_bios_chars[mp_slot])
    $ mphone_bios_chars_list.extend(mp.mphone_bios_chars_list[mp_slot])
    $ mphone_chat_history_list.extend(mp.mphone_chat_history_list[mp_slot])
    $ mphone_contact_list.extend(mp.mphone_contact_list[mp_slot])
    $ mphone_current_input = mp.mphone_current_input[mp_slot]
    $ mphone_current_wallpaper = mp.mphone_current_wallpaper[mp_slot]
    $ mphone_mc_avatar = mp.mphone_mc_avatar[mp_slot]
    $ mphone_music_bar_show = mp.mphone_music_bar_show[mp_slot]
    $ mphone_use_favs = mp.mphone_use_favs[mp_slot]
    $ mphone_wallpaper_int = mp.mphone_wallpaper_int[mp_slot]
    $ mphone_wallpaper_list.extend(mp.mphone_wallpaper_list[mp_slot])
    $ mroosterAvatarArray.extend(mp.mroosterAvatarArray[mp_slot])
    $ mroosterChoices.extend(mp.mroosterChoices[mp_slot])
    $ mroosterCommentSectionArray.extend(mp.mroosterCommentSectionArray[mp_slot])
    $ mroosterHistory_avatars.extend(mp.mroosterHistory_avatars[mp_slot])
    $ mroosterHistory_liked.extend(mp.mroosterHistory_liked[mp_slot])
    $ mroosterHistory_likes.extend(mp.mroosterHistory_likes[mp_slot])
    $ mroosterHistory_nicknames.extend(mp.mroosterHistory_nicknames[mp_slot])
    $ mroosterHistory_text.extend(mp.mroosterHistory_text[mp_slot])
    $ mroosterLikedArray.extend(mp.mroosterLikedArray[mp_slot])
    $ mroosterLikesArray.extend(mp.mroosterLikesArray[mp_slot])
    $ mroosterNickArray.extend(mp.mroosterNickArray[mp_slot])
    $ mroosterPhotoArray.extend(mp.mroosterPhotoArray[mp_slot])
    $ mroosterPostsArray.extend(mp.mroosterPostsArray[mp_slot])
    $ mroosterTextArray.extend(mp.mroosterTextArray[mp_slot])
    $ name = mp.name[mp_slot]
    $ nerdNotes = mp.nerdNotes[mp_slot]
    $ notifications = mp.notifications[mp_slot]
    $ passedEnglish = mp.passedEnglish[mp_slot]
    $ passedGender = mp.passedGender[mp_slot]
    $ passedMath = mp.passedMath[mp_slot]
    $ pathCathy = mp.pathCathy[mp_slot]
    $ pathIsabella = mp.pathIsabella[mp_slot]
    $ pathJill = mp.pathJill[mp_slot]
    $ pathMayaJosy = mp.pathMayaJosy[mp_slot]
    $ pathSage = mp.pathSage[mp_slot]
    $ permanent_affinity = mp.permanent_affinity[mp_slot]
    $ preferredmilf = mp.preferredmilf[mp_slot]
    $ quinn = mp.quinn[mp_slot]
    $ quinn_shop_freebie = mp.quinn_shop_freebie[mp_slot]
    $ quinn_shop_japanese_lvl = mp.quinn_shop_japanese_lvl[mp_slot]
    $ quinn_shop_special_lvl = mp.quinn_shop_special_lvl[mp_slot]
    $ quinn_shop_spicy_lvl = mp.quinn_shop_spicy_lvl[mp_slot]
    $ rejectedSage = mp.rejectedSage[mp_slot]
    $ riona = mp.riona[mp_slot]
    $ roosterNickArray.extend(mp.roosterNickArray[mp_slot])
    $ roosterNickJamie = mp.roosterNickJamie[mp_slot]
    $ roosterNickAlt = mp.roosterNickAlt[mp_slot]
    $ roosterNickMC = mp.roosterNickMC[mp_slot]
    $ roosterNickMCCustom = mp.roosterNickMCCustom[mp_slot]
    $ rooster_nick_list.extend(mp.rooster_nick_list[mp_slot])
    $ sage = mp.sage[mp_slot]
    $ sageControlEp3 = mp.sageControlEp3[mp_slot]
    $ save_name = mp.save_name[mp_slot]
    $ settings_name = mp.settings_name[mp_slot]
    $ settings_rooster_nickname = mp.settings_rooster_nickname[mp_slot]
    $ shuffle_losses = mp.shuffle_losses[mp_slot]
    $ shuffle_wins = mp.shuffle_wins[mp_slot]
    $ spentMoney = mp.spentMoney[mp_slot]
    $ sports_counter_skill = mp.sports_counter_skill[mp_slot]
    $ sports_dex = mp.sports_dex[mp_slot]
    $ sports_heal_skill = mp.sports_heal_skill[mp_slot]
    $ sports_hp = mp.sports_hp[mp_slot]
    $ sports_pow = mp.sports_pow[mp_slot]
    $ sports_mov = mp.sports_mov[mp_slot]
    $ sports_roundhouse_skill = mp.sports_roundhouse_skill[mp_slot]
    $ sports_skillpointsleft = mp.sports_skillpointsleft[mp_slot]
    $ sports_store_sp1 = mp.sports_store_sp1[mp_slot]
    $ sports_store_sp2 = mp.sports_store_sp2[mp_slot]
    $ sports_store_sp3 = mp.sports_store_sp3[mp_slot]
    $ stevePainting = mp.stevePainting[mp_slot]
    $ swyper_arieth_history.extend(mp.swyper_arieth_history[mp_slot])
    $ swyper_arieth_state = mp.swyper_arieth_state[mp_slot]
    $ swyper_cathy_history.extend(mp.swyper_cathy_history[mp_slot])
    $ swyper_cathy_state = mp.swyper_cathy_state[mp_slot]
    $ swyper_catrin_history.extend(mp.swyper_catrin_history[mp_slot])
    $ swyper_catrin_state = mp.swyper_catrin_state[mp_slot]
    $ swyper_ellie_history.extend(mp.swyper_ellie_history[mp_slot])
    $ swyper_ellie_state = mp.swyper_ellie_state[mp_slot]
    $ swyper_ida_history.extend(mp.swyper_ida_history[mp_slot])
    $ swyper_ida_state = mp.swyper_ida_state[mp_slot]
    $ swyper_liked_arieth = mp.swyper_liked_arieth[mp_slot]
    $ swyper_liked_cathy = mp.swyper_liked_cathy[mp_slot]
    $ swyper_liked_catrin = mp.swyper_liked_catrin[mp_slot]
    $ swyper_liked_ellie = mp.swyper_liked_ellie[mp_slot]
    $ swyper_liked_ida = mp.swyper_liked_ida[mp_slot]
    $ swyper_liked_micha = mp.swyper_liked_micha[mp_slot]
    $ swyper_liked_nicole = mp.swyper_liked_nicole[mp_slot]
    $ swyper_liked_nora = mp.swyper_liked_nora[mp_slot]
    $ swyper_liked_paula = mp.swyper_liked_paula[mp_slot]
    $ swyper_micha_history.extend(mp.swyper_micha_history[mp_slot])
    $ swyper_micha_state = mp.swyper_micha_state[mp_slot]
    $ swyper_nicole_history.extend(mp.swyper_nicole_history[mp_slot])
    $ swyper_nicole_state = mp.swyper_nicole_state[mp_slot]
    $ swyper_nora_history.extend(mp.swyper_nora_history[mp_slot])
    $ swyper_nora_state = mp.swyper_nora_state[mp_slot]
    $ swyper_paula_history.extend(mp.swyper_paula_history[mp_slot])
    $ swyper_paula_state = mp.swyper_paula_state[mp_slot]
    $ swyper_rejected_by_arieth = mp.swyper_rejected_by_arieth[mp_slot]
    $ swyper_rejected_by_cathy = mp.swyper_rejected_by_cathy[mp_slot]
    $ swyper_rejected_by_catrin = mp.swyper_rejected_by_catrin[mp_slot]
    $ swyper_rejected_by_ellie = mp.swyper_rejected_by_ellie[mp_slot]
    $ swyper_rejected_by_ida = mp.swyper_rejected_by_ida[mp_slot]
    $ swyper_rejected_by_micha = mp.swyper_rejected_by_micha[mp_slot]
    $ swyper_rejected_by_nicole = mp.swyper_rejected_by_nicole[mp_slot]
    $ swyper_rejected_by_nora = mp.swyper_rejected_by_nora[mp_slot]
    $ swyper_rejected_by_paula = mp.swyper_rejected_by_paula[mp_slot]
    $ totalChickChoices = mp.totalChickChoices[mp_slot]
    $ totalDikChoices = mp.totalDikChoices[mp_slot]
    $ tutorials = mp.tutorials[mp_slot]
    $ wallet_lvl = mp.wallet_lvl[mp_slot]
    $ ep8_quinn_lewd = mp.ep8_quinn_lewd[mp_slot]
    $ ep8_ball_game_won = mp.ep8_ball_game_won[mp_slot]
    $ npenalty = mp.npenalty[mp_slot]
    $ ep8_sage_stay_night = mp.ep8_sage_stay_night[mp_slot]
    $ mc_info = mp.mc_info[mp_slot]

    if not persistent.mc_tut_message:
        $ persistent.mc_tut_message = mp.mc_tut_message[mp_slot]
    if not persistent.ep2_c1:
        $ persistent.ep2_c1 = mp.ep2_c1[mp_slot]
    if not persistent.ep3_c1:
        $ persistent.ep3_c1 = mp.ep3_c1[mp_slot]
    if not persistent.ep4_c1:
        $ persistent.ep4_c1 = mp.ep4_c1[mp_slot]
    if not persistent.ep5_c1:
        $ persistent.ep5_c1 = mp.ep5_c1[mp_slot]
    if not persistent.ep6_c1:
        $ persistent.ep6_c1 = mp.ep6_c1[mp_slot]
    if not persistent.ep7_c1:
        $ persistent.ep7_c1 = mp.ep7_c1[mp_slot]
    if not persistent.ep8_c1:
        $ persistent.ep8_c1 = mp.ep8_c1[mp_slot]

    if not persistent.triple_tile_challenge:
        $ persistent.triple_tile_challenge = mp.triple_tile_challenge[mp_slot]
    if mp.pancake_highscore[mp_slot] > persistent.pancake_highscore:
        $ persistent.pancake_highscore = mp.pancake_highscore[mp_slot]

    if mp.ep7_wpi1[mp_slot]:
        $ persistent.ep7_wpi1 = mp.ep7_wpi1[mp_slot]
    if mp.ep7_wpi2[mp_slot]:
        $ persistent.ep7_wpi2 = mp.ep7_wpi2[mp_slot]
    if mp.ep7_wpj1[mp_slot]:
        $ persistent.ep7_wpj1 = mp.ep7_wpj1[mp_slot]
    if mp.ep7_wpj2[mp_slot]:
        $ persistent.ep7_wpj2 = mp.ep7_wpj2[mp_slot]
    if mp.ep7_wpjo1[mp_slot]:
        $ persistent.ep7_wpjo1 = mp.ep7_wpjo1[mp_slot]
    if mp.ep7_wpjo2[mp_slot]:
        $ persistent.ep7_wpjo2 = mp.ep7_wpjo2[mp_slot]
    if mp.ep7_wpm1[mp_slot]:
        $ persistent.ep7_wpm1 = mp.ep7_wpm1[mp_slot]
    if mp.ep7_wpm2[mp_slot]:
        $ persistent.ep7_wpm2 = mp.ep7_wpm2[mp_slot]
    if mp.ep7_wps1[mp_slot]:
        $ persistent.ep7_wps1 = mp.ep7_wps1[mp_slot]
    if mp.ep7_wps2[mp_slot]:
        $ persistent.ep7_wps2 = mp.ep7_wps2[mp_slot]
    if mp.ep8_wpi1[mp_slot]:
        $ persistent.ep8_wpi1 = mp.ep8_wpi1[mp_slot]
    if mp.ep8_wpj1[mp_slot]:
        $ persistent.ep8_wpj1 = mp.ep8_wpj1[mp_slot]
    if mp.ep8_wpjo1[mp_slot]:
        $ persistent.ep8_wpjo1 = mp.ep8_wpjo1[mp_slot]
    if mp.ep8_wpm1[mp_slot]:
        $ persistent.ep8_wpm1 = mp.ep8_wpm1[mp_slot]
    if mp.ep8_wpq1[mp_slot]:
        $ persistent.ep8_wpq1 = mp.ep8_wpq1[mp_slot]
    if mp.ep8_wps1[mp_slot]:
        $ persistent.ep8_wps1 = mp.ep8_wps1[mp_slot]
    if mp.ep8_wpe1[mp_slot]:
        $ persistent.ep8_wpe1 = mp.ep8_wpe1[mp_slot]
    if mp.ep8_wpjade1[mp_slot]:
        $ persistent.ep8_wpjade1 = mp.ep8_wpjade1[mp_slot]
    $ persistent.ep8_wpmad1 = True
    if mp.basket_score[mp_slot][0][1] > persistent.basket_score[0][1]:
        $ persistent.basket_score = mp.basket_score[mp_slot]
    if mp.triple_tile_highscores[mp_slot][0][0] > persistent.triple_tile_highscores[0][0]:
        $ persistent.triple_tile_highscores = mp.triple_tile_highscores[mp_slot]
    if mp.triple_tile_highscores_easy[mp_slot][0][0] > persistent.triple_tile_highscores_easy[0][0]:
        $ persistent.triple_tile_highscores_easy = mp.triple_tile_highscores_easy[mp_slot]

    python:
        for x in range(0,len(mp.art_unlocked_lvl1[mp_slot])):
            if mp.art_unlocked_lvl1[mp_slot][x]:
                if x < 10:
                    persistent.art_unlocked_lvl1[x] = True
                else:
                    persistent.art_unlocked_lvl1[x+1] = True
        for x in range(0,len(mp.art_unlocked_lvl2[mp_slot])):
            if mp.art_unlocked_lvl2[mp_slot][x]:
                if x < 10:
                    persistent.art_unlocked_lvl2[x] = True
                else:
                    persistent.art_unlocked_lvl2[x+1] = True
        for x in range(0,len(mp.art_unlocked_lvl3[mp_slot])):
            if mp.art_unlocked_lvl3[mp_slot][x]:
                if x < 10:
                    persistent.art_unlocked_lvl3[x] = True
                else:
                    persistent.art_unlocked_lvl3[x+1] = True

$ renpy.block_rollback()
$ renpy.block_rollback()
$ quick_menu = qM
$ persistent.name = name
$ persistent.current_save_name = save_name
jump continue_season3_label

init:
    if persistent.basket_score == None:
        $ persistent.basket_score = [["Jacob",20],["Leon",15],["Nick",10]]
    if persistent.mc_tut_message == None:
        $ persistent.mc_tut_message = False
    if persistent.ep2_c1 == None:
        $ persistent.ep2_c1 = False
    if persistent.ep3_c1 == None:
        $ persistent.ep3_c1 = False
    if persistent.ep4_c1 == None:
        $ persistent.ep4_c1 = False
    if persistent.ep5_c1 == None:
        $ persistent.ep5_c1 = False
    if persistent.ep6_c1 == None:
        $ persistent.ep6_c1 = False
    if persistent.ep7_c1 == None:
        $ persistent.ep7_c1 = False
    if persistent.ep8_c1 == None:
        $ persistent.ep8_c1 = False
    if persistent.triple_tile_highscores == None:
        $ persistent.triple_tile_highscores = [[0,0],[0,0],[0,0]]
    if persistent.triple_tile_highscores_easy == None:
        $ persistent.triple_tile_highscores_easy = [[0,0],[0,0],[0,0]]
    if persistent.triple_tile_challenge == None:
        $ persistent.triple_tile_challenge = False
    if persistent.pancake_highscore == None:
        $ persistent.pancake_highscore = 0
    if persistent.ep7_wpi1 == None:
        $ persistent.ep7_wpi1 = False
    if persistent.ep7_wpi2 == None:
        $ persistent.ep7_wpi2 = False
    if persistent.ep7_wpj1 == None:
        $ persistent.ep7_wpj1 = False
    if persistent.ep7_wpj2 == None:
        $ persistent.ep7_wpj2 = False
    if persistent.ep7_wpjo1 == None:
        $ persistent.ep7_wpjo1 = False
    if persistent.ep7_wpjo2 == None:
        $ persistent.ep7_wpjo2 = False
    if persistent.ep7_wpm1 == None:
        $ persistent.ep7_wpm1 = False
    if persistent.ep7_wpm2 == None:
        $ persistent.ep7_wpm2 = False
    if persistent.ep7_wps1 == None:
        $ persistent.ep7_wps1 = False
    if persistent.ep7_wps2 == None:
        $ persistent.ep7_wps2 = False
    if persistent.ep8_wpi1 == None:
        $ persistent.ep8_wpi1 = False
    if persistent.ep8_wpj1 == None:
        $ persistent.ep8_wpj1 = False
    if persistent.ep8_wpjo1 == None:
        $ persistent.ep8_wpjo1 = False
    if persistent.ep8_wpm1 == None:
        $ persistent.ep8_wpm1 = False
    if persistent.ep8_wpq1 == None:
        $ persistent.ep8_wpq1 = False
    if persistent.ep8_wps1 == None:
        $ persistent.ep8_wps1 = False
    if persistent.ep8_wpe1 == None:
        $ persistent.ep8_wpe1 = False
    if persistent.ep8_wpjade1 == None:
        $ persistent.ep8_wpjade1 = False
    if persistent.ep8_wpmad1 == None:
        $ persistent.ep8_wpmad1 = False
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
