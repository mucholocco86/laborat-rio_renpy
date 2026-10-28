init python:

    def mphone_stats_girl_get_rank():
        global mphone_stats_girl_list
        
        if len(mphone_stats_girl_list) < 2:
            return "{color=00b0ff}Almost-Virgin{/color}"
        elif len(mphone_stats_girl_list) < 4:
            return "{color=76d5ff}Romantic{/color}"
        elif len(mphone_stats_girl_list) < 7:
            return "{color=76d5ff}Devoted{/color}"
        elif len(mphone_stats_girl_list) < 10:
            return "{color=beebff}Experienced{/color}"
        elif len(mphone_stats_girl_list) < 15:
            return "{color=f7ffff}Womanizer{/color}"
        elif len(mphone_stats_girl_list) < 20:
            return "{color=ffe2c1}Slut{/color}"
        elif len(mphone_stats_girl_list) < 25:
            return "{color=ffc27b}Fuckboy{/color}"
        else:
            return "{color=fe9416}Pussy Magnet{/color}"
        
        return ""

    def calc_seen_dialogue():
        global specialMessage
        global mphone_app_gallery_photos_list
        seen = renpy.count_seen_dialogue_blocks() * 1.0
        total = renpy.count_dialogue_blocks() * 1.0
        s = round(seen/total * 100.0 , 2)
        if not persistent.golden_phone and s > 95.0:
            specialMessage = "Golden Phone Skin Unlocked"
            persistent.golden_phone = True
            persistent.golden_phone_skin_enabled = True
            renpy.show_screen("specialmsglong")
        if s > 99.8 and not "stupid_reward_pic" in mphone_app_gallery_photos_list:
            mgallery_add_photo("stupid_reward_pic")
        return s

    def stats_girl_count(girl):
        global mphone_stats_girl_log
        global mphone_stats_girl_log_s3
        tmpInt = 0
        if girl == "":
            return len(mphone_stats_girl_log) + len(mphone_stats_girl_log_s3)
        for x in mphone_stats_girl_log:
            if girl == x:
                tmpInt += 1
        for x in mphone_stats_girl_log_s3:
            if girl == x:
                tmpInt += 1
        return tmpInt

    def mphone_stats_add_girl_event(girl,event_text):
        global mphone_stats_girl_list
        global mphone_stats_girl_log
        if not girl in mphone_stats_girl_list:
            mphone_stats_girl_list.append(girl)
        mphone_stats_girl_log.append([girl,"• "+event_text])
        
        return

    def mphone_stats_add_girl_s3(girl,event_text):
        global mphone_stats_girl_log_s3
        global mphone_stats_girl_list
        
        if len(mphone_stats_girl_list) == 0:
            mphone_stats_generate_girls()
        
        if not girl in mphone_stats_girl_list:
            mphone_stats_girl_list.append(girl)
        
        if not [girl,"• "+event_text] in mphone_stats_girl_log_s3:
            mphone_stats_girl_log_s3.append([girl,"• "+event_text])
        return

    def mphone_stats_generate_girls():
        global mphone_stats_girl_log
        global ep1_lewd_camila_quinn
        global ep3_fuckedCamilaAndMona
        global ep5_fuckedCamila
        global ep7_camila_lewd
        global ep7_riona_lewd
        global ep7_rica_lewd
        global quinn_shop_spicy_lvl
        global ep3_fuckedRionaQuinn
        global ep4_quinn_lewd
        global ep6_quinn_lewd
        global ep2_wonCumpetition
        global ep5_fuckedRiona
        global quinn_shop_japanese_lvl
        global ep5_cathy_lewd
        global ep4_bella_lewd
        global ep5_bella_lewd
        global ep4_fuckedMelanie
        global ep2_fuckHOT
        global ep5_hot_lewd
        global ep8_melanie_lewd
        global ep7_becky_lewd
        global ep6_sarah_lewd
        global ep8_sarah_lewd
        global ep3_envyLewd
        global ep6_envy_lewd
        global ep6_nora_lewd
        global ep8_envy_lewd
        global ep8_sandy_lewd
        global ep4_lickedAshley
        global ep5_lily_lewd
        global ep4_grindedLily
        global ep3_acceptedJade
        global ep8_lily_lewd
        global ep7_lily_lewd
        global ep4_roseLewd
        global ep4_fuckedSage
        global ep2QuinnSawYouAndSage
        global ep5_fuckedSage
        global ep7_sage_lewd
        global ep7_accept_madame
        global ep2_fuckedJosy
        global ep2SageGuitarTeacher
        global rejectedSage
        global mbios_history_quinn
        global ep3_mayaLewd
        global ep4_fuckedJade
        global ep4_touchedJillsBreasts
        global ep5_fucked_josy
        global ep5_kissed_jill
        global ep5_fucked_maya
        global ep6_bella_lewd
        global pathMayaJosy
        global ep6_reject_jade
        global ep7_josy_lewd
        global ep7_josy_lewd2
        global ep7_solo_maya
        global ep7_quinn_lewd
        global ep7_bella_lewd
        global ep8_josy_lewd
        global ep8_jade_lewd
        global ep8_maya_lewd
        global ep8_sage_stay_night
        global ep8_sq_lewd
        global branchIsabella
        global branchJill
        global branchMayaJosy
        global branchSage
        global ep9_jade_lewd
        global ep9_haunted_mansion
        global ep9_others_texted
        global ep9_maya_lewd
        global ep9_camila_lewd
        global ep9_heather_lewd
        global ep9_cumpetition_join
        global ep9_jill_lewd
        global ep9_lily_nicole_lewd
        global ep9_quinn_lewd
        global ep9_sarah_melanie_lewd
        
        mphone_stats_girl_log = []
        
        mphone_stats_add_girl_event("zoey","You had sex with Zoey in the past.")
        
        if ep1_lewd_camila_quinn:
            mphone_stats_add_girl_event("camila","You had fun with Camila and Quinn in the HOTs' bathroom in episode 1.")
            mphone_stats_add_girl_event("quinn","You had fun with Camila and Quinn in the HOTs' bathroom in episode 1.")
        
        if quinn_shop_spicy_lvl>0:
            mphone_stats_add_girl_event("camila","You had sex with Camila through the glory hole in episode 1.")
        
        if quinn_shop_japanese_lvl>0:
            mphone_stats_add_girl_event("riona","You got a blowjob from Riona through the glory hole in episode 1.")
        
        if ep2_wonCumpetition:
            mphone_stats_add_girl_event("quinn","You had sex with Quinn during the CUM-petition in episode 2.")
        
        if ep2QuinnSawYouAndSage:
            mphone_stats_add_girl_event("sage","You got a boobjob from Sage in episode 2.")
        
        if ep2_fuckHOT:
            mphone_stats_add_girl_event("riona","You got a footjob from Riona, Melanie, and Sarah in episode 2.")
            mphone_stats_add_girl_event("melanie","You got a footjob from Riona, Melanie ,and Sarah in episode 2.")
            mphone_stats_add_girl_event("sarah","You got a footjob from Riona, Melanie, and Sarah, and then fucked Sarah in the DIKs' supply closet in episode 2.")
        
        if ep2_fingeredMaya:
            mphone_stats_add_girl_event("maya","You fingered Maya in her dorm in episode 2.")
        
        if ep2_fuckedJosy:
            mphone_stats_add_girl_event("josy","You had sex with Josy after dinner in episode 2.")
        
        if ep3_fuckedCamilaAndMona:
            mphone_stats_add_girl_event("camila","You had sex with Camila and Mona in the college bathroom in episode 3.")
            mphone_stats_add_girl_event("mona","You had sex with Camila and Mona in the college bathroom in episode 3.")
        
        if ep2SageGuitarTeacher and not rejectedSage:
            mphone_stats_add_girl_event("sage","You had fun with Sage on her bed in episode 3.")
        
        if ep3_acceptedJade:
            mphone_stats_add_girl_event("jade","You got a footjob and a handjob from Jade during class in episode 3.")
        
        if ep3_envyLewd == 1:
            mphone_stats_add_girl_event("envy","You got a blowjob from Nicole at The Pink Rose in episode 3.")
        elif ep3_envyLewd == 2:
            mphone_stats_add_girl_event("envy","You had anal sex with Nicole at The Pink Rose in episode 3.")
        
        if ep3_fuckedRionaQuinn:
            mphone_stats_add_girl_event("riona","You paid for a threesome with Riona and Quinn in episode 3.")
            mphone_stats_add_girl_event("quinn","You paid for a threesome with Riona and Quinn in episode 3.")
        
        if ep3_mayaLewd:
            mphone_stats_add_girl_event("maya","You helped Maya with her HOT scavenger hunt list in episode 3.")
        
        if ep4_fuckedMelanie:
            mphone_stats_add_girl_event("melanie","You had sex with Melanie in the HOTs' shower as Sarah enjoyed herself in episode 4.")
            mphone_stats_add_girl_event("sarah","You had sex with Melanie in the HOTs' shower as Sarah enjoyed herself in episode 4.")
        
        if ep4_lickedAshley:
            mphone_stats_add_girl_event("ashley","You licked Ashley's pussy in the sauna in episode 4.")
        
        if ep4_grindedLily:
            mphone_stats_add_girl_event("lily","Lily grinded your cock in the sauna in episode 4.")
        
        if ep3_choseSage:
            mphone_stats_add_girl_event("sage","Sage gave you a boobjob in the HOTs' pool in episode 4.")
        
        if "Quinn didn't like that I entered her room without being invited. But she didn't seem to mind it after it turned physical." in mbios_history_quinn:
            mphone_stats_add_girl_event("quinn","Quinn jacked you off in her room in episode 4.")
        
        if ep4_bella_lewd:
            mphone_stats_add_girl_event("isabella","You had fun with Bella in her shower in episode 4.")
        
        if ep4_fuckedSage:
            mphone_stats_add_girl_event("sage","You had sex with Sage in her room in episode 4.")
        
        if ep4_roseLewd:
            mphone_stats_add_girl_event("rose","You had sex with Rose at The Pink Rose in episode 4.")
        
        if ep4_touchedJillsBreasts:
            mphone_stats_add_girl_event("jill","You fondled Jill's breasts in the shower in episode 4.")
        
        if ep4_fuckedJade:
            mphone_stats_add_girl_event("jade","You had sex with Jade in her car, in her bed, and in her bathroom in episode 4.")
        
        if ep4_quinn_lewd:
            mphone_stats_add_girl_event("quinn","You had sex with Quinn on the roof while high in episode 4.")
        
        if ep5_fuckedCamila:
            mphone_stats_add_girl_event("camila","You had sex with Camila at the prep mansion in episode 5.")
        
        if ep5_fuckedRiona:
            mphone_stats_add_girl_event("riona","You had sex with Riona at the prep mansion in episode 5.")
        
        if ep5_lily_lewd:
            mphone_stats_add_girl_event("lily","You got a blowjob from Lily at the prep mansion in episode 5.")
        
        if ep5_hot_lewd:
            mphone_stats_add_girl_event("sarah","You had fun with Melanie and Sarah in the hot tub at the prep mansion in episode 5.")
            mphone_stats_add_girl_event("melanie","You had fun with Melanie and Sarah in the hot tub at the prep mansion in episode 5.")
        
        if ep5_fucked_josy:
            mphone_stats_add_girl_event("josy","You had sex with Josy in her dorm in episode 5.")
        
        if ep5_fucked_maya:
            mphone_stats_add_girl_event("maya","You had sex with Maya at the prep mansion in episode 5.")
        
        if ep5_fuckedSage:
            mphone_stats_add_girl_event("sage","You had sex with Sage on Tybalt's bed at the prep mansion in episode 5.")
        
        if ep5_cathy_lewd:
            mphone_stats_add_girl_event("cathy","You got a blowjob from Cathy in Bella's car in episode 5.")
        
        if ep5_kissed_jill:
            mphone_stats_add_girl_event("jill","You made out with Jill on Bella's sofa in episode 5.")
        
        if ep5_bella_lewd:
            mphone_stats_add_girl_event("isabella","You had fun with Bella in her sauna in episode 5.")
        
        if ep6_sarah_lewd:
            mphone_stats_add_girl_event("sarah","You had sex with Sarah in her room in episode 6.")
        
        if ep6_quinn_lewd:
            mphone_stats_add_girl_event("quinn","You had sex with Quinn in your room in episode 6.")
        
        if ep6_bella_lewd:
            mphone_stats_add_girl_event("isabella","You got a blowjob and a boobjob from Bella in your room in episode 6.")
        
        if ep4_fuckedJade and not ep6_reject_jade:
            mphone_stats_add_girl_event("jade","You had sex with Jade in a supply closet in episode 6.")
        
        if pathMayaJosy:
            mphone_stats_add_girl_event("maya","You had a threesome with Josy and Maya for the sake of the HOT scavenger hunt list in episode 6.")
            mphone_stats_add_girl_event("josy","You had a threesome with Josy and Maya for the sake of the HOT scavenger hunt list in episode 6.")
        
        if ep6_nora_lewd:
            mphone_stats_add_girl_event("nora","You had sex with Nora in the bathroom in episode 6.")
        
        if ep6_envy_lewd:
            mphone_stats_add_girl_event("envy","You had a threesome with Nicole and Sandy at Nicole's place in episode 6.")
            mphone_stats_add_girl_event("sandy","You had a threesome with Nicole and Sandy at Nicole's place in episode 6.")
        
        if ep7_josy_lewd:
            mphone_stats_add_girl_event("josy","You had sex with Josy in your room in episode 7.")
        
        if ep7_josy_lewd2:
            mphone_stats_add_girl_event("josy","You had sex with Josy in the HOTs' pool in episode 7.")
        
        if ep7_bella_lewd:
            mphone_stats_add_girl_event("isabella","You had fun with Bella on her sofa in episode 7.")
        
        if ep7_quinn_lewd:
            mphone_stats_add_girl_event("quinn","You had sex with Quinn in her room while high in episode 7.")
        
        if ep7_solo_maya and pathMayaJosy:
            mphone_stats_add_girl_event("maya","You had sex with Maya in her dorm in episode 7.")
        
        if ep7_becky_lewd:
            mphone_stats_add_girl_event("becky","You got a blowjob from Becky at the HOTs' party in episode 7.")
        
        if ep7_accept_madame:
            mphone_stats_add_girl_event("madamerose","You accepted Madame Rose's offer at The Pink Rose in episode 7.")
        
        if ep7_lily_lewd:
            mphone_stats_add_girl_event("lily","You had sex with Lily at the HOTs' party in episode 7.")
        
        if ep7_camila_lewd and not ep7_rica_lewd:
            mphone_stats_add_girl_event("camila","You had sex with Camila at the HOTs' party in episode 7.")
        elif ep7_riona_lewd and not ep7_rica_lewd:
            mphone_stats_add_girl_event("riona","You had sex with Riona at the HOTs' party in episode 7.")
        elif ep7_rica_lewd:
            mphone_stats_add_girl_event("riona","You had a threesome with Camila and Riona at the HOTs' party in episode 7.")
            mphone_stats_add_girl_event("camila","You had a threesome with Camila and Riona at the HOTs' party in episode 7.")
        
        if ep7_sage_lewd:
            mphone_stats_add_girl_event("sage","You had sex with Sage at the HOTs' party in episode 7.")
        
        if ep8_sage_stay_night and not ep8_told_sage_chad_troy:
            mphone_stats_add_girl_event("sage","You got a blowjob from Sage in her room in episode 8.")
        
        if ep8_josy_lewd:
            mphone_stats_add_girl_event("josy","You had sex with Josy at the gym in episode 8.")
        
        if pathMayaJosy:
            mphone_stats_add_girl_event("josy","You had sex with Josy and Maya at Juno's Swimming and Spa in episode 8.")
            mphone_stats_add_girl_event("maya","You had sex with Josy and Maya at Juno's Swimming and Spa in episode 8.")
        
        if ep8_envy_lewd:
            mphone_stats_add_girl_event("envy","You had sex with Nicole at The Pink Rose in episode 8.")
        
        if ep8_sandy_lewd:
            mphone_stats_add_girl_event("sandy","You had sex with Sandy at The Pink Rose in episode 8.")
        
        if ep8_lily_lewd:
            mphone_stats_add_girl_event("lily","You had sex with Lily at The Pink Rose in episode 8.")
        
        if ep8_jade_lewd:
            mphone_stats_add_girl_event("jade","You had sex with Jade at a motel in episode 8.")
        
        if ep8_maya_lewd:
            mphone_stats_add_girl_event("maya","You had sex with Maya in your classroom in episode 8.")
        
        if ep8_melanie_lewd:
            mphone_stats_add_girl_event("melanie","You had sex with Melanie at the dorm party in episode 8.")
        if ep8_sarah_lewd:
            mphone_stats_add_girl_event("sarah","You had sex with Sarah through a glory hole at the dorm party in episode 8.")
            mphone_stats_add_girl_event("tara","You had sex with Tara and got a blowjob from Kylie through a glory hole at the dorm party in episode 8.")
            mphone_stats_add_girl_event("kylie","You had sex with Tara and got a blowjob from Kylie through a glory hole at the dorm party in episode 8.")
        
        if ep8_sq_lewd:
            mphone_stats_add_girl_event("sage","You had a threesome with Sage and Quinn in episode 8.")
            mphone_stats_add_girl_event("quinn","You had a threesome with Sage and Quinn in episode 8.")
        
        if branchIsabella:
            mphone_stats_add_girl_event("isabella","You had sex with Bella in her bed and at her dining table in episode 8.")
        
        if branchJill:
            mphone_stats_add_girl_event("jill","You had sex with Jill in your bed in episode 8.")
        
        return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
