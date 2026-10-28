#UNUSED SCRIPT

#MAIA
layeredimage maia:
    group body:
        attribute outfit default:
            ConditionSwitch(
                "maia_pregnancy_timer >= pregnancy_time // 2 and not is_maia_wearing_all", "custom_gui/global/character_sprites/maia/maia_body_preg_rall.webp",
                "maia_pregnancy_timer >= pregnancy_time // 2 and not is_maia_wearing_top", "custom_gui/global/character_sprites/maia/maia_body_preg_rtop.webp",
                "maia_pregnancy_timer >= pregnancy_time // 2", "custom_gui/global/character_sprites/maia/maia_body_preg.webp",
                "maia_pregnancy_timer < pregnancy_time // 2 and not is_maia_wearing_all", "custom_gui/global/character_sprites/maia/maia_body_rall.webp",
                "maia_pregnancy_timer < pregnancy_time // 2 and not is_maia_wearing_top", "custom_gui/global/character_sprites/maia/maia_body_rtop.webp",
                "True", "custom_gui/global/character_sprites/maia/maia_body.webp"
            )

    group expression:
        attribute natural1:
            "custom_gui/global/character_sprites/maia/maia_natural1.webp"
        attribute natural2:
            "custom_gui/global/character_sprites/maia/maia_natural2.webp"
        attribute natural3:
            "custom_gui/global/character_sprites/maia/maia_natural3.webp"
        attribute natural4:
            "custom_gui/global/character_sprites/maia/maia_natural4.webp"
        attribute shock1:
            "custom_gui/global/character_sprites/maia/maia_shock1.webp"
        attribute shock2:
            "custom_gui/global/character_sprites/maia/maia_shock2.webp"
        attribute happy1:
            "custom_gui/global/character_sprites/maia/maia_happy1.webp"
        attribute happy2:
            "custom_gui/global/character_sprites/maia/maia_happy2.webp"
        attribute fear1:
            "custom_gui/global/character_sprites/maia/maia_fear1.webp"
        attribute fear2:
            "custom_gui/global/character_sprites/maia/maia_fear2.webp"
        attribute sad1:
            "custom_gui/global/character_sprites/maia/maia_sad1.webp"
        attribute sad2:
            "custom_gui/global/character_sprites/maia/maia_sad2.webp"
        
    if is_maia_face_cum:
        "custom_gui/global/character_sprites/maia/maia_face_cum.webp"

#QUEEN
image queen natural1 = "custom_gui/global/character_sprites/queen/queen_natural1.webp"
image queen natural2 = "custom_gui/global/character_sprites/queen/queen_natural2.webp"
image queen happy1 = "custom_gui/global/character_sprites/queen/queen_happy1.webp"
image queen happy2 = "custom_gui/global/character_sprites/queen/queen_happy2.webp"
image queen angry1 = "custom_gui/global/character_sprites/queen/queen_sad1.webp"
image queen angry2 = "custom_gui/global/character_sprites/queen/queen_sad2.webp"
image queen shock1 = "custom_gui/global/character_sprites/queen/queen_shock1.webp"
image queen shock2 = "custom_gui/global/character_sprites/queen/queen_shock2.webp"

#REBECCA
image reb natural1 = "custom_gui/global/character_sprites/rebecca/reb_natural1.webp"
image reb natural2 = "custom_gui/global/character_sprites/rebecca/reb_natural2.webp"
image reb smug1 = "custom_gui/global/character_sprites/rebecca/reb_smug1.webp"
image reb smug2 = "custom_gui/global/character_sprites/rebecca/reb_smug2.webp"
image reb angry1 = "custom_gui/global/character_sprites/rebecca/reb_angry1.webp"
image reb angry2 = "custom_gui/global/character_sprites/rebecca/reb_angry2.webp"
image reb shock1 = "custom_gui/global/character_sprites/rebecca/reb_shock1.webp"
image reb shock2 = "custom_gui/global/character_sprites/rebecca/reb_shock2.webp"

#YUUHI
image yuuhi natural1 = "custom_gui/global/character_sprites/yuuhi/yuuhi_natural1.webp"
image yuuhi natural2 = "custom_gui/global/character_sprites/yuuhi/yuuhi_natural2.webp"
image yuuhi happy1 = "custom_gui/global/character_sprites/yuuhi/yuuhi_happy1.webp"
image yuuhi happy2 = "custom_gui/global/character_sprites/yuuhi/yuuhi_happy2.webp"
image yuuhi nervous1 = "custom_gui/global/character_sprites/yuuhi/yuuhi_nervous1.webp"
image yuuhi nervous2 = "custom_gui/global/character_sprites/yuuhi/yuuhi_nervous2.webp"
image yuuhi angry1 = "custom_gui/global/character_sprites/yuuhi/yuuhi_angry1.webp"
image yuuhi angry2 = "custom_gui/global/character_sprites/yuuhi/yuuhi_angry2.webp"

#EIREEN
image eireen natural1 = "custom_gui/global/character_sprites/eireen/eireen_natural1.webp"
image eireen natural2 = "custom_gui/global/character_sprites/eireen/eireen_natural2.webp"
image eireen frown1 = "custom_gui/global/character_sprites/eireen/eireen_frown1.webp"
image eireen frown2 = "custom_gui/global/character_sprites/eireen/eireen_frown2.webp"

#DIANA
layeredimage diana:
    group body:
        attribute outfit default:
            ConditionSwitch(
                "diana_pregnancy_timer >= pregnancy_time // 2 and not is_diana_wearing_all", "custom_gui/global/character_sprites/diana/body_rall_preg.webp",
                "diana_pregnancy_timer >= pregnancy_time // 2 and not is_diana_wearing_top", "custom_gui/global/character_sprites/diana/body_rtop_preg.webp",
                "diana_pregnancy_timer >= pregnancy_time // 2", "custom_gui/global/character_sprites/diana/body_preg.webp",
                "diana_pregnancy_timer < pregnancy_time // 2 and not is_diana_wearing_all", "custom_gui/global/character_sprites/diana/body_rall.webp",
                "diana_pregnancy_timer < pregnancy_time // 2 and not is_diana_wearing_top", "custom_gui/global/character_sprites/diana/body_rtop.webp",
                "True", "custom_gui/global/character_sprites/diana/body_normal.webp"
            )

    group expression:
        attribute natural1:
            "custom_gui/global/character_sprites/diana/diana_natural1.webp"
        attribute natural2:
            "custom_gui/global/character_sprites/diana/diana_natural2.webp"
        attribute flirt1:
            "custom_gui/global/character_sprites/diana/diana_flirt1.webp"
        attribute flirt2:
            "custom_gui/global/character_sprites/diana/diana_flirt2.webp"
        attribute shock1:
            "custom_gui/global/character_sprites/diana/diana_shock1.webp"
        attribute shock2:
            "custom_gui/global/character_sprites/diana/diana_shock2.webp"
        attribute nervous1:
            "custom_gui/global/character_sprites/diana/diana_nervous1.webp"
        attribute nervous2:
            "custom_gui/global/character_sprites/diana/diana_nervous2.webp"
        attribute angry1:
            "custom_gui/global/character_sprites/diana/diana_angry1.webp"
        attribute angry2:
            "custom_gui/global/character_sprites/diana/diana_angry2.webp"
        attribute mouth1:
            "custom_gui/global/character_sprites/diana/diana_mouth1.webp"
        attribute mouth2:
            "custom_gui/global/character_sprites/diana/diana_mouth2.webp"
        attribute mouth3:
            "custom_gui/global/character_sprites/diana/diana_mouth3.webp"
        attribute mouth4:
            "custom_gui/global/character_sprites/diana/diana_mouth4.webp"
        
    if is_diana_face_cum:
        "custom_gui/global/character_sprites/diana/face_cum.webp"
    

