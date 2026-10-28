    label characters:
        call hide_all from _call_hide_all

        hide screen button_hostess
        hide screen button_hostess_u
        hide screen button_hungry
        hide screen button_hungry_u
        hide screen button_istella
        hide screen button_istella_u
        hide screen button_maidens
        hide screen button_maidens_u
        hide screen button_athena
        hide screen button_athena_u
        hide screen button_karolina
        hide screen button_karolina_u
        hide screen button_lore
        hide screen dark_button
        hide screen high_button
        hide screen middle_button

        hide screen g_1_button

        hide screen g_1_l_button

        hide screen g_2_button

        hide screen g_2_l_button

        hide screen g_3_button

        hide screen g_3_l_button

        hide screen g_4_button

        hide screen g_4_l_button

        hide screen g_5_button

        hide screen g_5_l_button

        hide screen g_6_button

        hide screen g_6_l_button

        hide screen g_7_button

        hide screen g_7_l_button

        hide screen g_8_button

        hide screen g_8_l_button

        hide button_previous_page

        hide screen button_previous_page

        hide screen button_next_page

        hide screen button_tamara

        hide screen button_hailey

        hide screen button_anabelle

        hide screen button_jenny


        hide screen button_nixie

        hide screen button_irena

        hide screen button_fransisca


        hide screen button_tamara_u

        hide screen button_hailey_u

        hide screen button_anabelle_u

        hide screen button_jenny_u


        hide screen button_nixie_u

        hide screen button_irena_u

        hide screen button_fransisca_u
        hide screen button_candy

        hide screen button_torr

        hide screen button_centoria

        hide screen button_gabriella


        hide screen button_seira

        hide screen button_stephanie

        hide screen button_venus

        hide screen button_yumi


        hide screen button_candy_u

        hide screen button_torr_u

        hide screen button_centoria_u

        hide screen button_gabriella_u


        hide screen button_seira_u

        hide screen button_stephanie_u

        hide screen button_venus_u

        hide screen button_yumi_u

        hide screen button_mc

        hide screen button_nixie

        hide screen button_irena






        hide screen button_1


        scene wood

        show screen button_next_page

        #show screen button_lore

        show screen button_g
        if saw_diary == 1 and chapter == 7:
            show screen button_ch7_diary

        if chapter == 4:
            show screen button_chapter_lore

        if sus_open == 1:
            show screen button_suspects

        if cndy_met >= 1:
            show screen button_candy
            show label10 "{color=#d93675}Candy{/color}"

        else:
            show screen button_candy_u

        if gbrla_met >= 1:
            show screen button_gabriella
            show label2 "{color=#e3661e}Gabriella{/color}"

        else:
            show screen button_gabriella_u

        if s_met >= 1:
            show screen button_seira
            show label1 "{color=#d15adb}Seira{/color}"

        else:
            show screen button_seira_u

        if stfny_met >= 1:
            show screen button_stephanie
            show label4 "{color=#e3d12d}Stephanie{/color}"

        else:
            show screen button_stephanie_u

        if ymi_met >= 1:
            show screen button_yumi
            show label3 "{color=#0091cf}Yumi{/color}"

        else:
            show screen button_yumi_u

        if tmra_met >= 1:
            show screen button_tamara
            show label6 "{color=#de1b1b}Tamara{/color}"

        else:
            show screen button_tamara_u

        if hly_met >= 1:
            show screen button_hailey
            show label7 "{color=#6ebaf5}Hailey{/color}"

        else:
            show screen button_hailey_u

        if a_met >= 1:
            show screen button_anabelle
            show label5 "{color=#c9f7ff}Anabelle{/color}"

        else:
            show screen button_anabelle_u


        call screen button_2

        return

    label characters_2:

        call hide_all from _call_hide_all_1

        hide screen g_1_button

        hide screen g_1_l_button

        hide screen g_2_button

        hide screen g_2_l_button

        hide screen g_3_button

        hide screen g_3_l_button

        hide screen g_4_button

        hide screen g_4_l_button

        hide screen g_5_button

        hide screen g_5_l_button

        hide screen g_6_button

        hide screen g_6_l_button

        hide screen g_7_button

        hide screen g_7_l_button

        hide screen g_8_button

        hide screen g_8_l_button

        hide screen button_g

        hide button_next_page

        hide screen button_1

        hide screen button_previous_page

        hide screen button_next_page

        hide screen button_tamara

        hide screen button_hailey

        hide screen button_anabelle

        hide screen button_jenny


        hide screen button_nixie

        hide screen button_irena

        hide screen button_fransisca


        hide screen button_tamara_u

        hide screen button_hailey_u

        hide screen button_anabelle_u

        hide screen button_jenny_u


        hide screen button_nixie_u

        hide screen button_irena_u

        hide screen button_fransisca_u
        hide screen button_candy

        hide screen button_torr

        hide screen button_centoria

        hide screen button_gabriella


        hide screen button_seira

        hide screen button_stephanie

        hide screen button_venus

        hide screen button_yumi


        hide screen button_candy_u

        hide screen button_torr_u

        hide screen button_centoria_u

        hide screen button_gabriella_u


        hide screen button_seira_u

        hide screen button_stephanie_u

        hide screen button_venus_u

        hide screen button_yumi_u

        hide screen button_mc

        hide screen button_nixie

        hide screen button_irena



        scene wood
        show screen button_2 #<-----
        show screen button_extra_char
        if vns_met >= 1:
            show screen button_venus
            show label2 "{color=#db4242}Venus{/color}"

        else:
            show screen button_venus_u
        if tr_met >= 1:
            show screen button_torr
            show label1 "{color=#2ad14f}Torr{/color}"

        else:
            show screen button_torr_u

        if cnt_met >= 1:
            show screen button_centoria
            show label3 "{color=#399fed}Centoria{/color}"

        else:
            show screen button_centoria_u

        if jnfr_met >= 1:
            show screen button_jenny
            show label11 "{color=#f76e11}Jeniffer{/color}"

        else:
            show screen button_jenny_u

        if nxi_met >= 1:
            show screen button_nixie
            show label7 "{color=#a244c7}Nixie{/color}"

        else:
            show screen button_nixie_u

        if irna_met >= 1:
            show screen button_irena
            show label6 "{color=#a6a1f7}Irena{/color}"

        else:
            show screen button_irena_u

        if frnsska_met >= 1:
            show screen button_fransisca
            show label9 "{color=#f77440}Fransisca{/color}"

        else:
            show screen button_fransisca_u

        if misty_met >= 2 or chapter >= 7 and invited_misty >= 1:
            show screen button_misty
            show label10 "{color=#d9d9d9}Misty{/color}"

        else:
            show screen button_misty_u


        call screen button_previous_page

        return





    label stats_candy:
        call hide_all from _call_hide_all_23

        hide screen button_chapter_lore

        hide screen button_g

        hide screen button_previous_page

        hide screen button_next_page

        hide screen button_tamara

        hide screen button_hailey

        hide screen button_anabelle

        hide screen button_jenny


        hide screen button_nixie

        hide screen button_irena

        hide screen button_fransisca


        hide screen button_tamara_u

        hide screen button_hailey_u

        hide screen button_anabelle_u

        hide screen button_jenny_u


        hide screen button_nixie_u

        hide screen button_irena_u

        hide screen button_fransisca_u
        hide screen button_candy

        hide screen button_torr

        hide screen button_centoria

        hide screen button_gabriella


        hide screen button_seira

        hide screen button_stephanie

        hide screen button_venus

        hide screen button_yumi


        hide screen button_candy_u

        hide screen button_torr_u

        hide screen button_centoria_u

        hide screen button_gabriella_u


        hide screen button_seira_u

        hide screen button_stephanie_u

        hide screen button_venus_u

        hide screen button_yumi_u

        hide screen button_mc

        hide screen button_nixie

        hide screen button_irena



        scene stats2

        show name_text Text("{color=#8f254e}Candy{/color}", size=100)

        show species "Species"

        show species_value "Nymph"

        show sex "Sex"

        show sex_value "Female"

        show age "Age"

        show age_value "19"

        show height1 "Height"

        show height1_value "153cm"

        show weight "Weight"

        show weight_value "46kg"


        show rank "Rank"

        if cndy_rank_change == 1:
            show rank_value "Purple Belt"
        if cndy_rank_change == 0:
            show rank_value "White Belt"

        show trust "Trust"

        show trust_value "[cndy_trst]"

        show affection "Affection"

        show affection_value "[cndy_aff]"

        show respect "Respect"

        show respect_value "[cndy_res]"

        show lust "Lust"

        show lust_value "[cndy_lst]"
        if tr_met >=1:
            show screen button_candy_next
        if hly_met >=1:
            show screen button_candy_back


        call screen button_2

        jump characters


    label stats_torr:
        call hide_all from _call_hide_all_24

        hide screen button_chapter_lore

        hide screen button_g

        hide screen button_previous_page

        hide screen button_next_page

        hide screen button_tamara

        hide screen button_hailey

        hide screen button_anabelle

        hide screen button_jenny


        hide screen button_nixie

        hide screen button_irena

        hide screen button_fransisca


        hide screen button_tamara_u

        hide screen button_hailey_u

        hide screen button_anabelle_u

        hide screen button_jenny_u


        hide screen button_nixie_u

        hide screen button_irena_u

        hide screen button_fransisca_u
        hide screen button_candy

        hide screen button_torr

        hide screen button_centoria

        hide screen button_gabriella


        hide screen button_seira

        hide screen button_stephanie

        hide screen button_venus

        hide screen button_yumi


        hide screen button_candy_u

        hide screen button_torr_u

        hide screen button_centoria_u

        hide screen button_gabriella_u


        hide screen button_seira_u

        hide screen button_stephanie_u

        hide screen button_venus_u

        hide screen button_yumi_u

        hide screen button_mc

        hide screen button_nixie

        hide screen button_irena


        scene stats1

        show name_text Text("{color=#1a702d}Torr{/color}", size=100)

        show species "Species"

        show species_value "Elf"

        show sex "Sex"

        show sex_value "Female"

        show age "Age"

        show age_value "19"

        show height1 "Height"

        show height1_value "153cm"

        show weight "Weight"

        show weight_value "47kg"


        show rank "Rank"

        if tr_rank_change == 1:
            show rank_value "Purple Belt"
        if tr_rank_change == 0:
            show rank_value "White Belt"

        show trust "Trust"

        show trust_value "[tr_trst]"

        show affection "Affection"

        show affection_value "[tr_aff]"

        show respect "Respect"

        show respect_value "[tr_res]"

        show lust "Lust"

        show lust_value "[tr_lst]"

        if vns_met >=1:
            show screen button_torr_next
        if cndy_met >=1:
            show screen button_torr_back


        call screen button_2

        jump characters_2


    label stats_centoria:
        call hide_all from _call_hide_all_25

        hide screen button_g

        hide screen button_chapter_lore

        hide screen button_previous_page

        hide screen button_next_page

        hide screen button_tamara

        hide screen button_hailey

        hide screen button_anabelle

        hide screen button_jenny


        hide screen button_nixie

        hide screen button_irena

        hide screen button_fransisca


        hide screen button_tamara_u

        hide screen button_hailey_u

        hide screen button_anabelle_u

        hide screen button_jenny_u


        hide screen button_nixie_u

        hide screen button_irena_u

        hide screen button_fransisca_u
        hide screen button_candy

        hide screen button_torr

        hide screen button_centoria

        hide screen button_gabriella


        hide screen button_seira

        hide screen button_stephanie

        hide screen button_venus

        hide screen button_yumi


        hide screen button_candy_u

        hide screen button_torr_u

        hide screen button_centoria_u

        hide screen button_gabriella_u


        hide screen button_seira_u

        hide screen button_stephanie_u

        hide screen button_venus_u

        hide screen button_yumi_u

        hide screen button_mc

        hide screen button_nixie

        hide screen button_irena


        scene stats6

        show name_text Text("{color=#3286c7}Centoria{/color}", size=100)

        show species "Species"

        show species_value "Elf"

        show sex "Sex"

        show sex_value "Female"

        show age "Age"

        show age_value "21"

        show height1 "Height"

        show height1_value "163cm"

        show weight "Weight"

        show weight_value "51kg"


        show rank "Rank"


        if cnt_prpl == 1:
            show rank_value "Purple Belt"
        else:
            show rank_value "White Belt"

        show trust "Trust"

        show trust_value "[cnt_trst]"

        show affection "Affection"

        show affection_value "[cnt_aff]"

        show respect "Respect"

        show respect_value "[cnt_res]"

        show lust "Lust"

        show lust_value "[cnt_lst]"

        if jnfr_met >=1:
            show screen button_centoria_next
        show screen button_centoria_back

        call screen button_2

        jump characters_2


    label stats_gabriella:
        call hide_all from _call_hide_all_26

        hide screen button_chapter_lore

        hide screen button_g

        hide screen button_previous_page

        hide screen button_next_page

        hide screen button_tamara

        hide screen button_hailey

        hide screen button_anabelle

        hide screen button_jenny


        hide screen button_nixie

        hide screen button_irena

        hide screen button_fransisca


        hide screen button_tamara_u

        hide screen button_hailey_u

        hide screen button_anabelle_u

        hide screen button_jenny_u


        hide screen button_nixie_u

        hide screen button_irena_u

        hide screen button_fransisca_u
        hide screen button_candy

        hide screen button_torr

        hide screen button_centoria

        hide screen button_gabriella


        hide screen button_seira

        hide screen button_stephanie

        hide screen button_venus

        hide screen button_yumi


        hide screen button_candy_u

        hide screen button_torr_u

        hide screen button_centoria_u

        hide screen button_gabriella_u


        hide screen button_seira_u

        hide screen button_stephanie_u

        hide screen button_venus_u

        hide screen button_yumi_u

        hide screen button_mc

        hide screen button_nixie

        hide screen button_irena


        scene stats10

        show name_text Text("{color=#964211}Gabriella{/color}", size=100)

        show species "Species"

        show species_value "Human"

        show sex "Sex"

        show sex_value "Female"

        show age "Age"

        show age_value "19"

        show height1 "Height"

        show height1_value "150cm"

        show weight "Weight"

        show weight_value "44kg"


        show rank "Rank"
        if gbrla_white_belt == 1:
            show rank_value "White Belt"
        elif gbrla_white_belt == 2:
            show rank_value "Purple Belt"
        else:
            show rank_value "None"

        show trust "Trust"

        show trust_value "[gbrla_trst]"

        show affection "Affection"

        show affection_value "[gbrla_aff]"

        show respect "Respect"

        show respect_value "[gbrla_res]"

        show lust "Lust"

        show lust_value "[gbrla_lst]"

        if ymi_met >=1:
            show screen button_gabriella_next
        show screen button_gabriella_back

        call screen button_2

        jump characters


    label stats_seira:
        call hide_all from _call_hide_all_27

        hide screen button_chapter_lore

        hide screen button_g

        hide screen button_previous_page

        hide screen button_next_page

        hide screen button_tamara

        hide screen button_hailey

        hide screen button_anabelle

        hide screen button_jenny


        hide screen button_nixie

        hide screen button_irena

        hide screen button_fransisca


        hide screen button_tamara_u

        hide screen button_hailey_u

        hide screen button_anabelle_u

        hide screen button_jenny_u


        hide screen button_nixie_u

        hide screen button_irena_u

        hide screen button_fransisca_u
        hide screen button_candy

        hide screen button_torr

        hide screen button_centoria

        hide screen button_gabriella


        hide screen button_seira

        hide screen button_stephanie

        hide screen button_venus

        hide screen button_yumi


        hide screen button_candy_u

        hide screen button_torr_u

        hide screen button_centoria_u

        hide screen button_gabriella_u


        hide screen button_seira_u

        hide screen button_stephanie_u

        hide screen button_venus_u

        hide screen button_yumi_u

        hide screen button_mc

        hide screen button_nixie

        hide screen button_irena


        scene stats11

        show name_text Text("{color=#d15adb}Seira{/color}", size=100)

        show species "Species"

        if knows_s_race >= 1:
            show species_value "Demi-god"

        else:
            show species_value "Human"




        show sex "Sex"

        show sex_value "Female"

        show age "Age"

        show age_value "42"

        show height1 "Height"

        show height1_value "182cm"

        show weight "Weight"

        show weight_value "71kg"


        show rank "Rank"
        if knows_s_race >= 1:
            show rank_value "Keres"
        else:
            show rank_value "None"

        show trust "Trust"

        show trust_value "[s_trst]"

        show affection "Affection"

        show affection_value "[s_aff]"

        show respect "Respect"

        show respect_value "[s_res]"

        show lust "Lust"

        show lust_value "[s_lst]"

        if gbrla_met >=1:
            show screen button_seira_next


        call screen button_2

        jump characters



    label stats_stephanie:
        call hide_all from _call_hide_all_28

        hide screen button_chapter_lore

        hide screen button_g

        hide screen button_previous_page

        hide screen button_next_page

        hide screen button_tamara

        hide screen button_hailey

        hide screen button_anabelle

        hide screen button_jenny


        hide screen button_nixie

        hide screen button_irena

        hide screen button_fransisca


        hide screen button_tamara_u

        hide screen button_hailey_u

        hide screen button_anabelle_u

        hide screen button_jenny_u


        hide screen button_nixie_u

        hide screen button_irena_u

        hide screen button_fransisca_u
        hide screen button_candy

        hide screen button_torr

        hide screen button_centoria

        hide screen button_gabriella


        hide screen button_seira

        hide screen button_stephanie

        hide screen button_venus

        hide screen button_yumi


        hide screen button_candy_u

        hide screen button_torr_u

        hide screen button_centoria_u

        hide screen button_gabriella_u


        hide screen button_seira_u

        hide screen button_stephanie_u

        hide screen button_venus_u

        hide screen button_yumi_u

        hide screen button_mc

        hide screen button_nixie

        hide screen button_irena


        scene stats4

        show name_text Text("{color=#e3d12d}Stephanie{/color}", size=100)

        show species "Species"

        show species_value "Human"

        show sex "Sex"

        show sex_value "Female"

        show age "Age"

        show age_value "24"

        show height1 "Height"

        show height1_value "157cm"

        show weight "Weight"

        show weight_value "50kg"


        show rank "Rank"

        show rank_value "Brown Belt"

        show trust "Trust"

        show trust_value "[stfny_trst]"

        show affection "Affection"

        show affection_value "[stfny_aff]"

        show respect "Respect"

        show respect_value "[stfny_res]"

        show lust "Lust"

        show lust_value "[stfny_lst]"

        if a_met >=1:
            show screen button_stephanie_next
        show screen button_stephanie_back

        call screen button_2

        jump characters



    label stats_venus:
        call hide_all from _call_hide_all_29

        hide screen button_chapter_lore

        hide screen button_g

        hide screen button_previous_page

        hide screen button_next_page

        hide screen button_tamara

        hide screen button_hailey

        hide screen button_anabelle

        hide screen button_jenny


        hide screen button_nixie

        hide screen button_irena

        hide screen button_fransisca


        hide screen button_tamara_u

        hide screen button_hailey_u

        hide screen button_anabelle_u

        hide screen button_jenny_u


        hide screen button_nixie_u

        hide screen button_irena_u

        hide screen button_fransisca_u
        hide screen button_candy

        hide screen button_torr

        hide screen button_centoria

        hide screen button_gabriella


        hide screen button_seira

        hide screen button_stephanie

        hide screen button_venus

        hide screen button_yumi


        hide screen button_candy_u

        hide screen button_torr_u

        hide screen button_centoria_u

        hide screen button_gabriella_u


        hide screen button_seira_u

        hide screen button_stephanie_u

        hide screen button_venus_u

        hide screen button_yumi_u

        hide screen button_mc

        hide screen button_nixie

        hide screen button_irena

        scene stats5

        show name_text Text("{color=#912d2d}Venus{/color}", size=100)

        show species "Species"

        show species_value "Nymph"

        show sex "Sex"

        show sex_value "Female"

        show age "Age"

        show age_value "23"

        show height1 "Height"

        show height1_value "159cm"

        show weight "Weight"

        show weight_value "49kg"


        show rank "Rank"

        show rank_value "Brown Belt"

        show trust "Trust"

        show trust_value "[vns_trst]"

        show affection "Affection"

        show affection_value "[vns_aff]"

        show respect "Respect"

        show respect_value "[vns_res]"

        show lust "Lust"

        show lust_value "[vns_lst]"

        if cnt_met >=1:
            show screen button_venus_next
        show screen button_venus_back

        call screen button_2

        jump characters_2



    label stats_yumi:
        call hide_all from _call_hide_all_30

        hide screen button_chapter_lore

        hide screen button_g

        hide screen button_previous_page

        hide screen button_next_page

        hide screen button_tamara

        hide screen button_hailey

        hide screen button_anabelle

        hide screen button_jenny


        hide screen button_nixie

        hide screen button_irena

        hide screen button_fransisca


        hide screen button_tamara_u

        hide screen button_hailey_u

        hide screen button_anabelle_u

        hide screen button_jenny_u


        hide screen button_nixie_u

        hide screen button_irena_u

        hide screen button_fransisca_u
        hide screen button_candy

        hide screen button_torr

        hide screen button_centoria

        hide screen button_gabriella


        hide screen button_seira

        hide screen button_stephanie

        hide screen button_venus

        hide screen button_yumi


        hide screen button_candy_u

        hide screen button_torr_u

        hide screen button_centoria_u

        hide screen button_gabriella_u


        hide screen button_seira_u

        hide screen button_stephanie_u

        hide screen button_venus_u

        hide screen button_yumi_u

        hide screen button_mc

        hide screen button_nixie

        hide screen button_irena

        scene stats9

        show name_text Text("{color=#0091cf}Yumi{/color}", size=100)

        show species "Species"

        show species_value "Human"

        show sex "Sex"

        show sex_value "Female"

        show age "Age"

        show age_value "23"

        show height1 "Height"

        show height1_value "159cm"

        show weight "Weight"

        show weight_value "48kg"


        show rank "Rank"

        show rank_value "Blue Belt"

        show trust "Trust"

        show trust_value "[ymi_trst]"

        show affection "Affection"

        show affection_value "[ymi_aff]"

        show respect "Respect"

        show respect_value "[ymi_res]"

        show lust "Lust"

        show lust_value "[ymi_lst]"

        if stfny_met >=1:
            show screen button_yumi_next
        show screen button_yumi_back

        call screen button_2

        jump characters

    #Characters_2:

    label stats_tamara:
        call hide_all from _call_hide_all_31

        hide screen button_previous_page

        hide screen button_next_page

        hide screen button_tamara

        hide screen button_hailey

        hide screen button_anabelle

        hide screen button_jenny


        hide screen button_nixie

        hide screen button_irena

        hide screen button_fransisca


        hide screen button_tamara_u

        hide screen button_hailey_u

        hide screen button_anabelle_u

        hide screen button_jenny_u


        hide screen button_nixie_u

        hide screen button_irena_u

        hide screen button_fransisca_u
        hide screen button_candy

        hide screen button_torr

        hide screen button_centoria

        hide screen button_gabriella


        hide screen button_seira

        hide screen button_stephanie

        hide screen button_venus

        hide screen button_yumi


        hide screen button_candy_u

        hide screen button_torr_u

        hide screen button_centoria_u

        hide screen button_gabriella_u


        hide screen button_seira_u

        hide screen button_stephanie_u

        hide screen button_venus_u

        hide screen button_yumi_u

        hide screen button_mc

        hide screen button_nixie

        hide screen button_irena



        scene stats8

        show name_text Text("{color=#8f0000}Tamara{/color}", size=100)

        show species "Species"

        show species_value "Nymph"

        show sex "Sex"

        show sex_value "Female"

        show age "Age"

        show age_value "18"

        show height1 "Height"

        show height1_value "148cm"

        show weight "Weight"

        show weight_value "44kg"


        show rank "Rank"

        if tmra_belt == 3:
            show rank_value "Red Belt"
        else:
            show rank_value "Purple Belt"

        show trust "Trust"

        show trust_value "[tmra_trst]"

        show affection "Affection"

        show affection_value "[tmra_aff]"

        show respect "Respect"

        show respect_value "[tmra_res]"

        show lust "Lust"

        show lust_value "[tmra_lst]"

        if hly_met >=1:
            show screen button_tamara_next
        show screen button_tamara_back

        call screen button_2

        jump characters


    label stats_hailey:
        call hide_all from _call_hide_all_32

        hide screen button_previous_page

        hide screen button_next_page

        hide screen button_tamara

        hide screen button_hailey

        hide screen button_anabelle

        hide screen button_jenny


        hide screen button_nixie

        hide screen button_irena

        hide screen button_fransisca


        hide screen button_tamara_u

        hide screen button_hailey_u

        hide screen button_anabelle_u

        hide screen button_jenny_u


        hide screen button_nixie_u

        hide screen button_irena_u

        hide screen button_fransisca_u
        hide screen button_candy

        hide screen button_torr

        hide screen button_centoria

        hide screen button_gabriella


        hide screen button_seira

        hide screen button_stephanie

        hide screen button_venus

        hide screen button_yumi


        hide screen button_candy_u

        hide screen button_torr_u

        hide screen button_centoria_u

        hide screen button_gabriella_u


        hide screen button_seira_u

        hide screen button_stephanie_u

        hide screen button_venus_u

        hide screen button_yumi_u

        hide screen button_mc

        hide screen button_nixie

        hide screen button_irena



        scene stats7

        show name_text Text("{color=#74abd6}Hailey{/color}", size=100)

        show species "Species"

        show species_value "Nymph"

        show sex "Sex"

        show sex_value "Female"

        show age "Age"

        show age_value "25"

        show height1 "Height"

        show height1_value "180cm"

        show weight "Weight"

        show weight_value "69kg"


        show rank "Rank"

        show rank_value "Brown Belt"

        show trust "Trust"

        show trust_value "[hly_trst]"

        show affection "Affection"

        show affection_value "[hly_aff]"

        show respect "Respect"

        show respect_value "[hly_res]"

        show lust "Lust"

        show lust_value "[hly_lst]"

        if cndy_met >=1:
            show screen button_hailey_next
        show screen button_hailey_back

        call screen button_2

        jump characters

    label stats_anabelle:
        call hide_all from _call_hide_all_33

        hide screen button_previous_page

        hide screen button_next_page

        hide screen button_tamara

        hide screen button_hailey

        hide screen button_anabelle

        hide screen button_jenny


        hide screen button_nixie

        hide screen button_irena

        hide screen button_fransisca


        hide screen button_tamara_u

        hide screen button_hailey_u

        hide screen button_anabelle_u

        hide screen button_jenny_u


        hide screen button_nixie_u

        hide screen button_irena_u

        hide screen button_fransisca_u
        hide screen button_candy

        hide screen button_torr

        hide screen button_centoria

        hide screen button_gabriella


        hide screen button_seira

        hide screen button_stephanie

        hide screen button_venus

        hide screen button_yumi


        hide screen button_candy_u

        hide screen button_torr_u

        hide screen button_centoria_u

        hide screen button_gabriella_u


        hide screen button_seira_u

        hide screen button_stephanie_u

        hide screen button_venus_u

        hide screen button_yumi_u

        hide screen button_mc

        hide screen button_nixie

        hide screen button_irena



        scene stats3

        show name_text Text("{color=#bfd7db}Anabelle{/color}", size=100)

        show species "Species"

        show species_value "Human"

        show sex "Sex"

        show sex_value "Female"

        show age "Age"

        show age_value "26"

        show height1 "Height"

        show height1_value "162cm"

        show weight "Weight"

        show weight_value "57kg"


        show rank "Rank"

        show rank_value "Keres"

        show trust "Trust"

        show trust_value "[a_trst]"

        show affection "Affection"

        show affection_value "[a_aff]"

        show respect "Respect"

        show respect_value "[a_res]"

        show lust "Lust"

        show lust_value "[a_lst]"

        if tmra_met >=1:
            show screen button_anabelle_next
        show screen button_anabelle_back

        call screen button_2

        jump characters


    label stats_jenny:
        call hide_all from _call_hide_all_34

        hide screen button_previous_page

        hide screen button_next_page

        hide screen button_tamara

        hide screen button_hailey

        hide screen button_anabelle

        hide screen button_jenny


        hide screen button_nixie

        hide screen button_irena

        hide screen button_fransisca


        hide screen button_tamara_u

        hide screen button_hailey_u

        hide screen button_anabelle_u

        hide screen button_jenny_u


        hide screen button_nixie_u

        hide screen button_irena_u

        hide screen button_fransisca_u
        hide screen button_candy

        hide screen button_torr

        hide screen button_centoria

        hide screen button_gabriella


        hide screen button_seira

        hide screen button_stephanie

        hide screen button_venus

        hide screen button_yumi


        hide screen button_candy_u

        hide screen button_torr_u

        hide screen button_centoria_u

        hide screen button_gabriella_u


        hide screen button_seira_u

        hide screen button_stephanie_u

        hide screen button_venus_u

        hide screen button_yumi_u

        hide screen button_mc

        hide screen button_nixie

        hide screen button_irena



        scene stats12

        show name_text Text("{color=#c44f00}Jeniffer{/color}", size=100)

        show species "Species"

        show species_value "Human"

        show sex "Sex"

        show sex_value "Female"

        show age "Age"

        show age_value "25"

        show height1 "Height"

        show height1_value "161cm"

        show weight "Weight"

        show weight_value "57kg"


        show rank "Rank"

        show rank_value "None"

        show trust "Trust"

        show trust_value "[jnfr_trst]"

        show affection "Affection"

        show affection_value "[jnfr_aff]"

        show respect "Respect"

        show respect_value "[jnfr_res]"

        show lust "Lust"

        show lust_value "[jnfr_lst]"

        if frnsska_met >=1:
            show screen button_jenny_next
        show screen button_jenny_back

        call screen button_2

        jump characters_2


    label stats_nixie:
        call hide_all from _call_hide_all_35

        hide screen button_previous_page

        hide screen button_next_page

        hide screen button_tamara

        hide screen button_hailey

        hide screen button_anabelle

        hide screen button_jenny


        hide screen button_nixie

        hide screen button_irena

        hide screen button_fransisca


        hide screen button_tamara_u

        hide screen button_hailey_u

        hide screen button_anabelle_u

        hide screen button_jenny_u


        hide screen button_nixie_u

        hide screen button_irena_u

        hide screen button_fransisca_u
        hide screen button_candy

        hide screen button_torr

        hide screen button_centoria

        hide screen button_gabriella


        hide screen button_seira

        hide screen button_stephanie

        hide screen button_venus

        hide screen button_yumi


        hide screen button_candy_u

        hide screen button_torr_u

        hide screen button_centoria_u

        hide screen button_gabriella_u


        hide screen button_seira_u

        hide screen button_stephanie_u

        hide screen button_venus_u

        hide screen button_yumi_u

        hide screen button_mc

        hide screen button_nixie

        hide screen button_irena



        scene stats16

        show name_text Text("{color=#a244c7}Nixie{/color}", size=100)

        show species "Species"

        show species_value "Succubus"

        show sex "Sex"

        show sex_value "Female"

        show age "Age"

        show age_value "19"

        show height1 "Height"

        show height1_value "147cm (156cm with horns)"

        show weight "Weight"

        show weight_value "39kg"


        show rank "Rank"

        show rank_value "None"

        show trust "Trust"

        show trust_value "[nxi_trst]"

        show affection "Affection"

        show affection_value "[nxi_aff]"

        show respect "Respect"

        show respect_value "[nxi_res]"

        show lust "Lust"

        show lust_value "[nxi_lst]"

        if misty_met >= 2 or chapter >= 7 and invited_misty >= 1:
            show screen button_nixie_next
        show screen button_nixie_back

        call screen button_2

        jump characters_2




    label stats_fransisca:
        call hide_all from _call_hide_all_36

        hide screen button_previous_page

        hide screen button_next_page

        hide screen button_tamara

        hide screen button_hailey

        hide screen button_anabelle

        hide screen button_jenny


        hide screen button_nixie

        hide screen button_irena

        hide screen button_fransisca


        hide screen button_tamara_u

        hide screen button_hailey_u

        hide screen button_anabelle_u

        hide screen button_jenny_u


        hide screen button_nixie_u

        hide screen button_irena_u

        hide screen button_fransisca_u
        hide screen button_candy

        hide screen button_torr

        hide screen button_centoria

        hide screen button_gabriella


        hide screen button_seira

        hide screen button_stephanie

        hide screen button_venus

        hide screen button_yumi


        hide screen button_candy_u

        hide screen button_torr_u

        hide screen button_centoria_u

        hide screen button_gabriella_u


        hide screen button_seira_u

        hide screen button_stephanie_u

        hide screen button_venus_u

        hide screen button_yumi_u

        hide screen button_mc

        hide screen button_nixie

        hide screen button_irena



        scene stats13

        show name_text Text("{color=#f77440}Fransisca{/color}", size=100)

        show species "Species"

        show species_value "Human"

        show sex "Sex"

        show sex_value "Female"

        show age "Age"

        show age_value "44"

        show height1 "Height"

        show height1_value "165cm"

        show weight "Weight"

        show weight_value "63kg"


        show rank "Rank"

        show rank_value "None"

        show trust "Trust"

        show trust_value "[frnsska_trst]"

        show affection "Affection"

        show affection_value "[frnsska_aff]"

        show respect "Respect"

        show respect_value "[frnsska_res]"

        show lust "Lust"

        show lust_value "[frnsska_lst]"

        if irna_met >=1:
            show screen button_fransisca_next
        show screen button_fransisca_back

        call screen button_2

        jump characters_2



    label stats_mc:
        call hide_all from _call_hide_all_37

        hide screen button_previous_page

        hide screen button_next_page

        hide screen button_tamara

        hide screen button_hailey

        hide screen button_anabelle

        hide screen button_jenny


        hide screen button_nixie

        hide screen button_irena

        hide screen button_fransisca

        hide screen button_nixie

        hide screen button_irena


        hide screen button_tamara_u

        hide screen button_hailey_u

        hide screen button_anabelle_u

        hide screen button_jenny_u


        hide screen button_nixie_u

        hide screen button_irena_u

        hide screen button_fransisca_u
        hide screen button_candy

        hide screen button_torr

        hide screen button_centoria

        hide screen button_gabriella


        hide screen button_seira

        hide screen button_stephanie

        hide screen button_venus

        hide screen button_yumi


        hide screen button_candy_u

        hide screen button_torr_u

        hide screen button_centoria_u

        hide screen button_gabriella_u


        hide screen button_seira_u

        hide screen button_stephanie_u

        hide screen button_venus_u

        hide screen button_yumi_u

        hide screen button_mc

        hide screen button_nixie

        hide screen button_irena



        scene stats14

        show name_text Text("{color=#dbc221}[mc_name]{/color}", size=100)

        show species "Species"

        if knows_s_race >= 1:
            show species_value "Incubus"

        else:
            if knows_z_race >= 1:
                show species_value "Elf?"

            else:
                show species_value "Elf"

        show sex "Sex"

        show sex_value "Male"

        show age "Age"

        show age_value "20"

        show height1 "Height"

        show height1_value "175cm"

        show weight "Weight"

        show weight_value "73kg"


        show rank "Rank"

        if accepted >= 1:

            show rank_value "White Belt"

        else:

            show rank_value "None"



        if accepted >= 1:

            show trust "Winning points"

            show trust_value "[wins]"

        if nxi_met >=1:
            show screen button_mc_back

        call screen button_2

        jump characters_2


    label stats_irena:
        call hide_all from _call_hide_all_38

        scene stats15

        show name_text Text("{color=#9a97cc}Irena{/color}", size=100)

        show species "Species"

        show species_value "Half nymph - half succubus"

        show sex "Sex"

        show sex_value "Female"

        show age "Age"

        show age_value "20"

        show height1 "Height"

        show height1_value "168cm"

        show weight "Weight"

        show weight_value "61kg"


        show rank "Rank"

        show rank_value "None"

        show trust "Trust"

        show trust_value "[irna_trst]"

        show affection "Affection"

        show affection_value "[irna_aff]"

        show respect "Respect"

        show respect_value "[irna_res]"

        show lust "Lust"

        show lust_value "[irna_lst]"

        if nxi_met >=1:
            show screen button_irena_next
        show screen button_irena_back

        call screen button_2

        jump characters_2

    label stats_misty:
        call hide_all from _call_hide_all_52

        scene stats17

        show name_text Text("{color=#a80035}Misty{/color}", size=100)

        show species "Species"

        show species_value "Demi-human"

        show sex "Sex"

        show sex_value "Female"

        show age "Age"

        show age_value "22"

        show height1 "Height"

        show height1_value "169cm"

        show weight "Weight"

        show weight_value "70kg"


        show rank "Rank"

        if misty_rank_change == 0:
            show rank_value "None"
        if misty_rank_change == 1:
            show rank_value "White Belt"

        show trust "Trust"

        show trust_value "[misty_trst]"

        show affection "Affection"

        show affection_value "[misty_aff]"

        show respect "Respect"

        show respect_value "[misty_res]"

        show lust "Lust"

        show lust_value "[misty_lst]"

        if nxi_met >=1:
            show screen button_misty_back

        call screen button_2

        jump characters_2




    #Chapter lore:

    label chapter_lore:

        call hide_all from _call_hide_all_15

        if chapter == 4:

            scene wood

            if hostess_met >= 1:
                show screen button_hostess

            else:
                show screen button_hostess_u

            if hungry_met >= 1:
                show screen button_hungry

            else:
                show screen button_hungry_u

            if istella_met >= 1:
                show screen button_istella

            else:
                show screen button_istella_u

            if maidens_met >= 1:
                show screen button_maidens

            else:
                show screen button_maidens_u

            if athena_met >= 1:
                show screen button_athena

            else:
                show screen button_athena_u

            if krlna_met >= 1:
                show screen button_karolina

            else:
                show screen button_karolina_u

            call screen button_previous_page




    label hostess_lore:

        scene v4271

        hide screen button_hostess
        hide screen button_hostess_u
        hide screen button_hungry
        hide screen button_hungry_u
        hide screen button_istella
        hide screen button_istella_u
        hide screen button_maidens
        hide screen button_maidens_u
        hide screen button_athena
        hide screen button_athena_u
        hide screen button_karolina
        hide screen button_karolina_u

        "The hostess, The owner of the house that welcomed us."

        if hostess_met >= 2:
            "Gave us lots of food and was very generous to us."

        if hostess_met >= 3:
            "But as it turns out, withheld the information about being stuck here if we stay long."

        if hostess_met >= 4:
            "And I think it might have been her that I saw in that other dream opening the door..."

        if hostess_met >= 5:
            "I hope she's doing well..."

        jump chapter_lore

    label hungry_lore:

        hide screen button_hostess
        hide screen button_hostess_u
        hide screen button_hungry
        hide screen button_hungry_u
        hide screen button_istella
        hide screen button_istella_u
        hide screen button_maidens
        hide screen button_maidens_u
        hide screen button_athena
        hide screen button_athena_u
        hide screen button_karolina
        hide screen button_karolina_u



        if talked_to_hungry_girl == 1:

            scene v4437

            "Unnamed girl. You saw her in your dream at the door, she asked for shelter from the rain and the cold."

        else:

            scene v4434

            "Unnamed girl. You saw her in your dream, she spooked the fuck out of you."

        if hungry_met >= 2:
            "Was I seeing things from here perspective in the second dream?"
            "If so, then she must have died of the hunger and cold somewhere behind the temple... Poor soul... Unless..."
        if hungry_met == 3:
            "I think it's the fury! Athena must've turned her into a fury just before she died to carry out the punishment on the people of the town."

        if hungry_met == 4:
            "It's the fury! Athena turned her into a fury just before she died to carry out the punishment on the people of the town."
            "I killed her... I did pity her, but I had no choice..."
            "... right?"
        if hungry_met == 5:
            "It's the fury! Athena turned her into a fury just before she died to carry out the punishment on the people of the town."


        jump chapter_lore

    label istella_lore:

        hide screen button_hostess
        hide screen button_hostess_u
        hide screen button_hungry
        hide screen button_hungry_u
        hide screen button_istella
        hide screen button_istella_u
        hide screen button_maidens
        hide screen button_maidens_u
        hide screen button_athena
        hide screen button_athena_u
        hide screen button_karolina
        hide screen button_karolina_u

        scene v4504

        "Istella, a resident of the town of the faceless god."

        if istella_met >= 2:
            "She offered to guide us to the temple."
        if istella_met >= 3:
            "Later at the temple, she said some weird stuff about a house and a monster living inside it... Then said she was joking..."
        if istella_met >= 4:
            "She's also a sleep nymph! She's been causing me to have those dreams. She was trying to guide me to the fury."
        if istella_met >= 5:
            "I hope she's alright..."
        jump chapter_lore

    label maidens_lore:

        hide screen button_hostess
        hide screen button_hostess_u
        hide screen button_hungry
        hide screen button_hungry_u
        hide screen button_istella
        hide screen button_istella_u
        hide screen button_maidens
        hide screen button_maidens_u
        hide screen button_athena
        hide screen button_athena_u
        hide screen button_karolina
        hide screen button_karolina_u

        scene v4542

        "The maidens of the temple of the faceless god."

        if maidens_met >= 2:
            "They said never to go near a house behind the temple. Probably the one Istella was talking about..."
        if maidens_met >= 3:
            "They also... 'helped me clear my mind' to enter the trial."

        jump chapter_lore

    label athena_lore:

        hide screen button_hostess
        hide screen button_hostess_u
        hide screen button_hungry
        hide screen button_hungry_u
        hide screen button_istella
        hide screen button_istella_u
        hide screen button_maidens
        hide screen button_maidens_u
        hide screen button_athena
        hide screen button_athena_u
        hide screen button_karolina
        hide screen button_karolina_u

        scene v4587

        "Athena. Daughter of Zeus. Goddess of wisdom, warfare, and handicraft, and one of the twelve olympians."
        if athena_met >= 2:
            "It was Athena who placed the curse on the town. She refused to say why, though. But she insists it was a fair punishment."
        if athena_met >= 3:
            "After the town rejected helping a cold and hungry girl seeking refuge. Athena didn't want the town to worship her any longer, so she cursed the town and invented the faceless god."
            "She also turned the dying girl into a fury to carry out the punishment."
        if athena_met >= 4:
            if v4_obeyed_athena == 1:
                "She offered to let Torr go if we left the village for good. Which I agreed to do."
                "I hope I did the right thing..."
            else:
                "She offered to let Torr go if we left the village for good. But I refused and Anabelle and I defeated her and killed the fury."
                "We lefted the curse off the town. We did right thing..."
                "...Right?"
        jump chapter_lore

    label karolina_lore:

        hide screen button_hostess
        hide screen button_hostess_u
        hide screen button_hungry
        hide screen button_hungry_u
        hide screen button_istella
        hide screen button_istella_u
        hide screen button_maidens
        hide screen button_maidens_u
        hide screen button_athena
        hide screen button_athena_u
        hide screen button_karolina
        hide screen button_karolina_u

        scene v4167

        "Karolina Schwartz. Daughter of the jarl of Esyl, a city to the south."
        if krlna_met >= 2:
            "She is our escort target for our first mission. She wishes to go to her hometown."
        if krlna_met >= 3:
            "Candy dressed up to play her, while Torr played her younger brother, and I her butler. And she dressed up as Candy."
        if krlna_met >= 4:
            "Unfortunately, the mission faced a complication due to a collapsed bridge, and we must now cross the town of the faceless god..."
        if krlna_met >= 5:
            "We did it! We are out of the town and the mission is back on track."
        jump chapter_lore


    #Chapter lore buttons:

    screen button_hostess:
        imagebutton:
            xanchor 0.5
            yanchor 0.5
            xpos 0.14
            ypos 0.28
            idle "images/Stats_stuff/chapter_4/Hostess_F_U.webp"
            hover "images/Stats_stuff/chapter_4/Hostess_F_H.webp"
            action Jump("hostess_lore")

    screen button_hostess_u:
        imagebutton:
            xanchor 0.5
            yanchor 0.5
            xpos 0.14
            ypos 0.28
            idle "images/Stats_stuff/Unknown_F_U.webp"
            hover "images/Stats_stuff/Unknown_F_H.webp"
            action NullAction()

    screen button_hungry:
        imagebutton:
            xanchor 0.5
            yanchor 0.5
            xpos 0.38
            ypos 0.28
            idle "images/Stats_stuff/chapter_4/Hungry_F_U.webp"
            hover "images/Stats_stuff/chapter_4/Hungry_F_H.webp"
            action Jump("hungry_lore")

    screen button_hungry_u:
        imagebutton:
            xanchor 0.5
            yanchor 0.5
            xpos 0.38
            ypos 0.28
            idle "images/Stats_stuff/Unknown_F_U.webp"
            hover "images/Stats_stuff/Unknown_F_H.webp"
            action NullAction()

    screen button_istella:
        imagebutton:
            xanchor 0.5
            yanchor 0.5
            xpos 0.62
            ypos 0.28
            idle "images/Stats_stuff/chapter_4/Istella_F_U.webp"
            hover "images/Stats_stuff/chapter_4/Istella_F_H.webp"
            action Jump("istella_lore")

    screen button_istella_u:
        imagebutton:
            xanchor 0.5
            yanchor 0.5
            xpos 0.62
            ypos 0.28
            idle "images/Stats_stuff/Unknown_F_U.webp"
            hover "images/Stats_stuff/Unknown_F_H.webp"
            action NullAction()


    screen button_maidens:
        imagebutton:
            xanchor 0.5
            yanchor 0.5
            xpos 0.86
            ypos 0.28
            idle "images/Stats_stuff/chapter_4/Maidens_F_U.webp"
            hover "images/Stats_stuff/chapter_4/Maidens_F_H.webp"
            action Jump("maidens_lore")

    screen button_maidens_u:
        imagebutton:
            xanchor 0.5
            yanchor 0.5
            xpos 0.86
            ypos 0.28
            idle "images/Stats_stuff/Unknown_F_U.webp"
            hover "images/Stats_stuff/Unknown_F_H.webp"
            action NullAction()

    screen button_athena:
        imagebutton:
            xanchor 0.5
            yanchor 0.5
            xpos 0.14
            ypos 0.72
            idle "images/Stats_stuff/chapter_4/Athena_F_U.webp"
            hover "images/Stats_stuff/chapter_4/Athena_F_H.webp"
            action Jump("athena_lore")

    screen button_athena_u:
        imagebutton:
            xanchor 0.5
            yanchor 0.5
            xpos 0.14
            ypos 0.72
            idle "images/Stats_stuff/Unknown_F_U.webp"
            hover "images/Stats_stuff/Unknown_F_H.webp"
            action NullAction()

    screen button_karolina:
        imagebutton:
            xanchor 0.5
            yanchor 0.5
            xpos 0.38
            ypos 0.72
            idle "images/Stats_stuff/chapter_4/Karolina_F_U.webp"
            hover "images/Stats_stuff/chapter_4/Karolina_F_H.webp"
            action Jump("karolina_lore")

    screen button_karolina_u:
        imagebutton:
            xanchor 0.5
            yanchor 0.5
            xpos 0.38
            ypos 0.72
            idle "images/Stats_stuff/Unknown_F_U.webp"
            hover "images/Stats_stuff/Unknown_F_H.webp"
            action NullAction()


    #Suspects:
    label suspects:
        call hide_all from _call_hide_all_39
        scene sus1
        if suspect_initial == 0:
            "Friedreich, the butler, only started working for the Schwartz a few months ago according to Serena. He lived outside the city before. So, he isn't a suspect."
            "I'll also exclude Karolina and Mikel, since Mikel is a kid, and the attacks continued while Karolina was away..."
            if jamie_initial == 1:
                "Jamie is also excluded, since he only visits Esyl occousionally."
                $ jamie_initial = 2
            "So that leaves..."
            with Pause(0.7)
            show screen sus2 with dissolve
            show screen sus3 with dissolve
            show screen sus4 with dissolve
            show screen sus5 with dissolve
            show screen sus6 with dissolve
            show screen sus7 with dissolve
            show screen sus8 with dissolve
            show screen sus9 with dissolve
            $ suspect_initial = 1
        elif jamie_initial == 1:
            "Jamie is also excluded, since he only visits Esyl occousionally."
            $ jamie_initial = 2
            with Pause(0.7)
            show screen sus2 with dissolve
            show screen sus3 with dissolve
            show screen sus4 with dissolve
            show screen sus5 with dissolve
            show screen sus6 with dissolve
            show screen sus7 with dissolve
            show screen sus8 with dissolve
            show screen sus9 with dissolve
        show screen sus2
        show screen sus3
        show screen sus4
        show screen sus5
        show screen sus6
        show screen sus7
        show screen sus8
        show screen sus9
        call screen button_go_back_to_stats
    label sus2_erwin:
        call hide_all from _call_hide_all_40
        scene v5284
        show name_text Text("{color=#f5f2bc}Erwin{/color}", size=100)
        "Description: He's a human and probably the tallest one I'm investigating, I'd say over 190cm tall. He's probably around fourty years old."
        "Occupation: An artist. A very good one."
        if erwin_q1 == 1:
            "Time lived in Esyl: About ten years."
        "Reason to suspect: No particular reason."
        "Further insight: His height fits, but his body shape doesn't. But I suppose it's possible that he wears extra clothes or uses magic."
        jump suspects
    label sus4_johan:
        call hide_all from _call_hide_all_41
        scene v5193
        show name_text Text("{color=#dbdbdb}Johann{/color}", size=100)
        "Description: He's a human and reasonably tall, maybe 180cm tall. He's probably around fifty years old."
        "Occupation: The jarl of Esyl."
        "Time lived in Esyl: All of his life."
        if johann_initial == 1:
            "Reason to suspect: Apparently, he and Jamie are managing an underground brothel... Not what I was looking for..."
        else:
            if jamie_initial == 0:
                "Reason to suspect: The butcher doesn't really seem to bother him, since he refused to issue further missions to take him down."
            if jamie_initial == 1:
                "Reason to suspect: I know Johann and Jamie are up to no good. I just know it..."
            if jamie_initial == 2:
                "Reason to suspect: I know Johann and Jamie are up to no good. I just know it..."
        "Further insight: His height fits, but his body shape doesn't. But I suppose it's possible that he wears extra clothes or uses magic."
        jump suspects
    label sus6_frankie:
        call hide_all from _call_hide_all_42
        scene v5397
        show name_text Text("{color=#c4f500}Frankie{/color}", size=100)
        "Description: He's an elf. Somewhere around my height. So, not really tall around here. Seems to be in his late twenties or early thirties."
        "Occupation: Sings to people and lives off tips, I guess..."
        if frankie_q1 == 1:
            "Time lived in Esyl: Several years."
        "Reason to suspect: No particular reason."
        "Further insight: He's a bit short to be the butcher. And his body shape doesn't fit the painting. That said, an elf would probably be capable of casting an illusion to change his appearance."
        jump suspects
    label sus8_tomas:
        call hide_all from _call_hide_all_43
        scene v5363
        show name_text Text("{color=#ccaf7a}Tomas{/color}", size=100)
        "Description: He's a human and reasonably tall, maybe 180cm tall. He's probably around fifty years old."
        "Occupation: The chief detective of the city."
        "Time lived in Esyl: All of his life."
        "Reason to suspect: Failed to catch the butcher for a long while, I suppose... But that aside, no particular reason."
        "Further insight: His height fits, but his body shape doesn't. But maybe he wears extra clothes or uses magic."
        jump suspects
    label sus10_toni:
        call hide_all from _call_hide_all_44
        scene v57
        show name_text Text("{color=#90bf02}Toni{/color}", size=100)
        "Description: He's a human and a somewhat short one, maybe 170cm tall are a bit shorter. He's somewhat fat too. And has dark skin. I'd say he's in his fourties or fifties."
        "Occupation: Owns most of the stores around here and works elsewhere as well, apparently."
        if toni_q1 == 1:
            "Time lived in Esyl: A few years ago."
        "Reason to suspect: No particular reason."
        "Further insight: Toni is too short to be the butcher. But his body shape sort of resembles the painting."
        jump suspects
    label sus12_misty:
        call hide_all from _call_hide_all_45
        scene v5417
        show name_text Text("{color=#a80035}Misty{/color}", size=100)
        "Description: She's a demi-human. Has four arms and six eyes... I'd say she's around my height. Propably around my age too."
        "Occupation: Owns a tea shop."
        if misty_q5 == 1 or misty_q8 == 1:
            "Time lived in Esyl: All her life."
        if misty_info == 0:
            "Reason to suspect: No particular reason."
        if misty_info == 1:
            "Reason to suspect: Irena says she's hiding something. I think she's right..."
        if misty_info == 2:
            "Reason to suspect: Seems what she was hiding had nothing to do with the butcher, after all..."
        "Further insight: She's a woman and a bit short to be the butcher. Someone would've notices the four arms, unless she uses an illusion of some sort..."
        jump suspects
    label sus14_daiana:
        call hide_all from _call_hide_all_46
        scene v5143
        show name_text Text("{color=#69daff}Daiana{/color}", size=100)
        "Description: She's a human. I'd say she's around 170cm, quite tall for a woman. Propably in her thirties."
        "Occupation: Maid at the Schwartz mansion."
        "Time lived in Esyl: Several years."
        "Reason to suspect: No particular reason."
        "Further insight: She's a woman and a bit short to be the butcher. She doesn't seem physically strong either."
        jump suspects
    label sus16_serena:
        call hide_all from _call_hide_all_47
        scene v5173
        show name_text Text("{color=#0093c4}Serena{/color}", size=100)
        "Description: She's a human. I'd say she's around 170cm, so quite tall for a woman. I'd say she's around fourty years old."
        "Occupation: None."
        "Time lived in Esyl: Several years."
        "Reason to suspect: The person that hires a detective should always be on the suspect list. But that aside, I see no reason to suspect her."
        "Further insight: She's a woman and a bit short to be the butcher. She doesn't seem physically strong either."
        jump suspects

    #Chapter_7_diary:

    label ch7_diary:
        call hide_all from _call_hide_all_72
        scene wood
        show dairy_1
        show screen button_ch7_diary_next
        call screen button_ch7_diary_out
    label ch7_diary_2:
        call hide_all from _call_hide_all_73
        scene wood
        show dairy_2
        show screen button_ch7_diary_back
        call screen button_ch7_diary_out



    #Extra characters:
    define axius_met = 0
    define artemis_met = 0
    define sirius_met = 0
    define clair_met = 0
    define theseus_met = 0
    define margot_met = 0
    define nari_met = 0
    define sol_met = 0
    define elnor_met = 0
    define cat_met = 0
    define tresha_met = 0
    define mercury_met = 0
    define met_all = 0

    label extra_characters:
        call hide_all from _call_hide_all_57
        if met_all >= 1:
            $ axius_met = 1
            $ artemis_met = 1
            $ athena_met = 1
            $ sirius_met = 1
            $ clair_met = 1
            $ theseus_met = 1
            $ margot_met = 1
            $ nari_met = 1
            $ sol_met = 1
            $ elnor_met = 1
            $ cat_met = 1
            $ tresha_met = 1
            $ mercury_met = 1
        scene wood
        if axius_met >= 1:
            show screen button_axius
            show label1 "{color=#ceb8ff}Axius{/color}"

        else:
            show screen button_axius_u

        if artemis_met >= 1:
            show screen button_artemis
            show label2 "{color=#95b033}Artemis{/color}"

        else:
            show screen button_artemis_u

        if athena_met >= 1:
            show screen button_athena2
            show label3 "{color=#d1d1d1}Athena{/color}"

        else:
            show screen button_athena2_u

        if sirius_met >= 1:
            show screen button_sirius
            show label4 "{color=#fff6bd}Sirius{/color}"

        else:
            show screen button_sirius_u

        if clair_met >= 1:
            show screen button_clair
            show label5 "{color=#948173}Clair{/color}"

        else:
            show screen button_clair_u

        if theseus_met >= 1:
            show screen button_theseus
            show label6 "{color=#fffa6e}Theseus{/color}"

        else:
            show screen button_theseus_u

        if margot_met >= 1:
            show screen button_margot
            show label7 "{color=#a14545}Margot{/color}"

        else:
            show screen button_margot_u

        if nari_met >= 1:
            show screen button_nari
            show label8 "{color=#ffffff}Nari{/color}"

        else:
            show screen button_nari_u

        show screen button_next_page_extra_char

        call screen back_to_char2

    label extra_axius:
        call hide_all from _call_hide_all_58
        scene axius_extra
        if artemis_met >= 1:
            show screen button_axius_next
        "Race: Incubus."
        "Affiliation: Underworld City./General. (Formally)"
        "First encounter: In Venus's illusion after infiltrating it."
        "Status: Alive. (Probably)"
        "Connection to you: Seems to be interested in convincing you to come to his side?"
        call screen button_back_to_extra_char
    label extra_artemis:
        call hide_all from _call_hide_all_59
        scene artemis_extra
        if athena_met >= 1:
            show screen button_artemis_next
        if axius_met >= 1:
            show screen button_artemis_back
        "Race: God."
        "Affiliation: Artemis's hunting group."
        "First encounter: At the forest when she saved your group from a minotur."
        "Status: Alive."
        call screen button_back_to_extra_char
    label extra_athena:
        call hide_all from _call_hide_all_60
        scene athena_extra
        if sirius_met >= 1:
            show screen button_athena_next
        if artemis_met >= 1:
            show screen button_athena_back
        "Race: God."
        "Affiliation: Olympus."
        if athena_met >= 2:
            "First encounter: At the town of the faceless god."
        else:
            "None."
        "Status: Alive."
        if athena_met >= 4:
            if v4_obeyed_athena == 1:
                "Connection to you: You obeyed her and left the town of the faceless god without further interference.)"
            else:
                "Connection to you: You disobeyed her, killing her fury and ending the curse of the town of the faceless god."
        else:
            "None."
        call screen button_back_to_extra_char
    label extra_sirius:
        call hide_all from _call_hide_all_61
        scene sirius_extra
        if clair_met >= 1:
            show screen button_sirius_next
        if athena_met >= 1:
            show screen button_sirius_back
        "Race: Demi-god."
        "Affiliation: Unknown"
        "First encounter: During the assualt on the incubi."
        "Status: Unknown."
        "Connection to you: Supported Seira's decision to spare you."
        call screen button_back_to_extra_char
    label extra_clair:
        call hide_all from _call_hide_all_62
        scene clair_extra
        if theseus_met >= 1:
            show screen button_clair_next
        if sirius_met >= 1:
            show screen button_clair_back
        "Race: Human."
        "Affiliation: Bouncty Hunter."
        "First encounter: At a tavern on the way back from Esyl."
        "Status: Alive. (Probably)"
        if clair_creampie == 1:
            "Connection to you: You kinda came inside her... Hopefully, she doesn't come back ten years later with a blond pointy eared kid asking for child support."
        elif choice_variable_ch6_35 == 1:
            "Connection to you: You kinda fucked her..."
        else:
            "Connection to you: Wanted to fuck you, but you weren't feeling up to it... Err... Why are you playing this game again?"
        call screen button_back_to_extra_char
    label extra_theseus:
        call hide_all from _call_hide_all_63
        scene theseus_extra
        if margot_met >= 1:
            show screen button_theseus_next
        if clair_met >= 1:
            show screen button_theseus_back
        "Race: Demi-god."
        "Affiliation: Olympus./Champion."
        "First encounter: During the assualt on the incubi."
        "Status: Unknown."
        "Connection to you: Was against sparing you."
        z "Seira's mentor and the guy who wanted me killed as a child. I wonder how he'd react to seeing me now..."
        call screen button_back_to_extra_char
    label extra_margot:
        call hide_all from _call_hide_all_64
        scene margot_extra
        if nari_met >= 1:
            show screen button_margot_next
        if theseus_met >= 1:
            show screen button_margot_back
        "Race: Human."
        "Affiliation: Fransisca./Assistant."
        "First encounter: At Fransisca's house."
        "Status: Alive."
        "Connection to you: Seems to really want to fuck you..."
        z "Fransisca's nutjob of an assistant."
        call screen button_back_to_extra_char
    label extra_nari:
        call hide_all from _call_hide_all_65
        scene nari_extra
        if margot_met >= 1:
            show screen button_nari_back
        if cat_met >= 1:
            show screen button_nari_next
        "Race: Unknown."
        "Affiliation: Unknown."
        "First encounter: None."
        "Status: Unknown."
        "Connection to you: None."
        if killed_specter == 0:
            z "I think his name is Nari. Seems the specter likes him... But he seemed to be associated with Axius in some way..."
        else:
            z "I think his name is Nari. Seems the specter liked him... But he seemed to be associated with Axius in some way..."
        call screen button_back_to_extra_char

    label extra_cat:
        call hide_all from _call_hide_all_74
        scene cat_extra
        if nari_met >= 1:
            show screen button_cat_back
        if tresha_met >= 1:
            show screen button_cat_next
        "Race: Cat."
        "Affiliation: Ninja village./Local cat."
        "First encounter: At the ninja village."
        "Status: Alive."
        "Connection to you: He kinda likes you."
        "Notable deeds: Being a cat. Scratched Torr when she tried to pet him."
        call screen button_back_to_extra_char_2
    label extra_tresha:
        call hide_all from _call_hide_all_75
        scene tresha_extra
        if cat_met >= 1:
            show screen button_tresha_back
        if mercury_met >= 1:
            show screen button_tresha_next
        "Race: Human."
        "Affiliation: Artemis's hunting group."
        "First encounter: At fransisca's house."
        "Status: Alive."
        if Indulged_in_activities_ch8 == 1:
            "Connection to you: Helped you with disposing of the specter, and then you did a few 'activities' together."
        else:
            "Connection to you: Helped you with disposing of the specter."
        call screen button_back_to_extra_char_2
    label extra_mercury:
        call hide_all from _call_hide_all_76
        scene mercury_extra
        if tresha_met >= 1:
            show screen button_mercury_back
        if sol_met >= 1:
            show screen button_mercury_next
        "Race: Unknown."
        "Affiliation: Unknown."
        "First encounter: None."
        "Status: Unknown."
        "Connection to you: None."
        call screen button_back_to_extra_char_2
    label extra_sol:
        call hide_all from _call_hide_all_77
        scene sol_extra
        if mercury_met >= 1:
            show screen button_sol_back
        if elnor_met >= 1:
            show screen button_sol_next
        "Race: Nymph."
        "Affiliation: Ninja village./Brown belt?"
        "First encounter: None."
        if A_told_abt_sol == 0:
            "Status: Unknown."
        else:
            "Status: Deceased."
        "Connection to you: None."
        "Notable deeds: Convinced Venus of joining the ninja village..."
        call screen button_back_to_extra_char_2
    label extra_elnor:
        call hide_all from _call_hide_all_78
        scene elnor_extra
        if sol_met >= 1:
            show screen button_elnor_back
#        if tresha_met >= 1:
#            show screen button_elnor_next
        "Race: Incubus (Demi-god)"
        "Affiliation: Underworld City./Ruler."
        "First encounter: None."
        "Status: Believed to be deceased."
        "Connection to you: Believed to be your father."
        call screen button_back_to_extra_char_2

    label extra_characters_2:
        call hide_all from _call_hide_all_79
        scene wood
        if cat_met >= 1:
            show screen button_cat
            show label1 "{color=#a3a3a3}Cat{/color}"

        else:
            show screen button_cat_u

        if tresha_met >= 1:
            show screen button_tresha
            show label2 "{color=#754b17}Tresha{/color}"

        else:
            show screen button_tresha_u

        if mercury_met >= 1:
            show screen button_mercury
            show label3 "{color=#e667a6}Mercury{/color}"

        else:
            show screen button_mercury_u

        if sol_met >= 1:
            show screen button_sol
            show label4 "{color=#18aac7}Sol{/color}"

        else:
            show screen button_sol_u

        if elnor_met >= 1:
            show screen button_elnor
            show label5 "{color=#d9b800}Elnor{/color}"

        else:
            show screen button_elnor_u

        call screen button_prev_page_extra_char












    #Lore:
#    label lore:
#        call hide_all from _call_hide_all_53
#        scene background_lore
#        show screen button_lore_ninja
#        show screen button_lore_races
#        call screen button_go_back_to_stats
#    label lore_races:
#        call hide_all from _call_hide_all_54
#        scene background_lore_races
#        show screen dark_button
#        show screen high_button
#        show screen middle_button
#        call screen button_go_back_to_lore
#    label lore_ninja:
#        call hide_all from _call_hide_all_55
#        scene background_lore_ninja
#        show screen mission_ranking
#        show screen belts
#        call screen button_go_back_to_lore
#    label dark_races:
#        call hide_all from _call_hide_all_56
#        scene background_lore_dark_races
#        show screen dark_candle_suc
#        show screen dark_candle_fur
#        show screen dark_candle_gob
#        show screen dark_candle_min
#        show screen dark_candle_oni
#        show screen dark_candle_sir
#        show screen dark_candle_spe
#        call screen button_back_to_lore
#    label high_races:
#        call hide_all from _call_hide_all_57
#        scene background_lore_high_races
#        show screen high_god
#        show screen high_tit
#        show screen high_dem
#        call screen button_back_to_lore
#    label middle_races:
#        #call hide_all
#        dev "This section isn't yet complete. Sorry..."
#        #scene background_lore_middle_races
#    label dark_races_suc:
#        call hide_all from _call_hide_all_58
#        scene succubus
#        "" #Info here
#        jump dark_races
#    label dark_races_fur:
#        call hide_all from _call_hide_all_59
#        scene fury
#        "" #Info here
#        jump dark_races
#    label dark_races_gob:
#        call hide_all from _call_hide_all_60
#        scene goblin
#        "" #Info here
#        jump dark_races
#    label dark_races_min:
#        call hide_all from _call_hide_all_61
#        scene minotaur
#        "" #Info here
#        jump dark_races
#    label dark_races_oni:
#        call hide_all from _call_hide_all_62
#        scene oni
#        "" #Info here
#        jump dark_races
#    label dark_races_sir:
#        call hide_all from _call_hide_all_63
#        scene siren
#        "" #Info here
#        jump dark_races
#    label dark_races_spe:
#        call hide_all from _call_hide_all_64
#        scene spectur
#        "" #Info here
#        jump dark_races
#    label high_races_god:
#        "" #Info here
#    label high_races_tit:
#        "" #Info here
#    label high_races_dem:
#        "" #Info here
#    label mission_ranking_label:
#        call hide_all from _call_hide_all_65
#        scene mission_ranking_board
#        call screen button_back_to_lore_ninja
