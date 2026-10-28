label header_ep9_label:

$ currentEpisode = 9
$ vault_unlocked = False
$ safe_digits = [0,0,0,0]
$ safe_digit_1 = 0
$ safe_digit_2 = 0
$ safe_digit_3 = 0
$ safe_digit_4 = 0
$ randInt = renpy.random.randint(0, 17)
window hide
$ disabled_apps = []

python:
    if len(art_girl_list) != 16:
        mphone_wallpaper_list.append(["mphone_wallpaper_nora",False,False])
        mphone_wallpaper_list.append(["mphone_wallpaper_zoey",False,False])
        
        art_girl_list.insert(10,"2d_jacob_screen_nora")
        art_girl_list.append("2d_jacob_screen_zoey")
        
        art_girl_new_icon.insert(10,False)
        art_girl_new_icon.append(False)
        
        art_order_lvl1_list.insert(10,0)
        art_order_lvl1_list.append(0)
        art_order_lvl2_list.insert(10,0)
        art_order_lvl2_list.append(0)
        art_order_lvl3_list.insert(10,0)
        art_order_lvl3_list.append(0)
        
        art_girl_lvl1_list.insert(10,False)
        art_girl_lvl1_list.append(False)
        art_girl_lvl2_list.insert(10,False)
        art_girl_lvl2_list.append(False)
        art_girl_lvl3_list.insert(10,False)
        art_girl_lvl3_list.append(False)
        
        art_girl_level_list.insert(10,False)
        art_girl_level_list.append(0)
        
        art_girl_crit1_list.insert(10,"- ???")
        art_girl_crit1_list.append("- ???")
        art_girl_crit2_list.insert(10,"- ???")
        art_girl_crit2_list.append("- ???")
        art_girl_crit3_list.insert(10,"- ???")
        art_girl_crit3_list.append("- ???")

default ep9_jill_mood = 0
default ep9_b_kissed_jill = False
default ep9_leons_side = False
default ep9_jm_sad = False
default ep9_jade_lewd = False
default ep9_josy_side = False
default ep9_jill_lewd = False
default ep9_sage_vanilla = False
default ep9_vinny_choice = ""
default ep9_josy_wonder = 0
default ep9_bianca_ass = False
default ep9_saw_matthew = False
default tc = 0
default ep9_derek_better_friend = False
default ep9_tiffani_gina_tara = False
default ep9_drink_win = ""
default ep9_josy_choice = ""
default ep9_riona_choice = ""
default ep9_shot_win = False
default ep9_sandy_accept = False
default ep9_sarah_melanie_lewd = False
default ep9_sandy_club = False
default ep9_told_jill = False
default ep9_jill_orgasm = False
default ep9_sm_like_rim = False
default ep9_riona_confided = False
default ep9_photos = [False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False]
default lname = ""
default disabled_contacts_list = []
if branchAlone:
    $ disabled_contacts_list = ["quinn","lily","nicole","nora","riona","jade"]

if branchIsabella and ep8_jill_state == 1:
    $ ep9_jill_mood = 3
elif branchIsabella:
    $ ep9_jill_mood = 2
elif (branchSage or branchMayaJosy) and ep8_jill_state == 1 and affinity != "DIK":
    $ ep9_jill_mood = 1
else:
    $ ep9_jill_mood = 0
default ep9_zoey_photo = False
default ep9_zoey_crash = False
default mphone_current_bios_char = 0
default mphone_bios_sort_by = ["Alphabetical","Girls","Guys","DIKs","HOTs","Jocks","Preps","Nerds","Staff/Teachers"]
default mphone_bios_sort_by_idx = 0
default mphone_triple_tile_is_playing = False
$ badik_chapter = "3"
default triple_tile_new_highscore = 0
default triple_tile_score = 0
default triple_tile_turn = 0
default triple_turn_to_beat = 15
default triple_card_number_of_cards = 6
default triple_tile_chosen_tile = -1
default triple_tile_game_over = False
default triple_tile_show_numbers = False
default triple_tile_easy_mode = False
default triple_tile_new_high_score = 0
default triple_tile_hovered_tile = [-1,-1]
default triple_tile_hs_checked = False


default triple_tile_spr = [[False,False,False],[False,False,False],[False,False,False]]
default triple_tile_sets = [[0,0,0],[0,0,0],[0,0,0]]
default triple_tile_grid = [[[0,0,0],[0,0,0],[0,0,0]], [[0,0,0],[0,0,0],[0,0,0]], [[0,0,0],[0,0,0],[0,0,0]]]
default triple_tile_grid_spr = [[[0,0,0],[0,0,0],[0,0,0]], [[0,0,0],[0,0,0],[0,0,0]], [[0,0,0],[0,0,0],[0,0,0]]]

$ map_system_list = []


default pp_activity_choices = []
default pp_current_party_happiness = [0,0,0,0,0,0,0,0]

default pp_round_score = 0
default pp_50_satisfied_diks = 0
default pp_round = 1

default pp_round_happiness_change = [0,0,0,0,0,0,0,0]
default pp_round_diks_score = [0,0,0,0,0,0,0,0]
default pp_round_item_score = 0
default pp_round_item_only_score = 0
default pp_round_activity_score = 0
default pp_round_needs_score = 0
default mansion_animated_score = [0,0,0,0,0,0]
default animated_score_step = 0

default pp_bought_this_round = [0,0,0,0,0,0,0,0]
default pp_price_limited_list = [1,2,4,2,5,2,1,3]
default pp_icons_limited_dependency_list = ["Cups","","","Trashcans","Cups","Cups","Trashcans","Music"]
default pp_dik_list = ["derek","jacob","jamie","johnboy","leon","nick","rusty","tommy"]
default pp_special_needs = [["Speakers",2],["Kegs",1],["Drugs",0],["Trashcans",3],["Guys",2],["Decor",2],["Liquor",3],["Girls",6]]
default pp_active_icon = -1


default pp_happiness_level = [50,50,50,50,50,50,50,50]
default pp_happiness_icon = [2,2,2,2,2,2,2,2]
python:
    while pp_happiness_level.count(50) > 4:
        tmpInt = renpy.random.randint(0, 7)
        tmpInt2 = renpy.random.randint(35, 45)
        if pp_happiness_level[tmpInt] == 50:
            pp_happiness_level[tmpInt] = tmpInt2
            pp_happiness_icon[tmpInt] = 1
default pp_continue_label = ""

default pp_inventory_limited_start_list = [0,0,0,0,0,0,0,0]
default pp_inventory_limited_list = [0,0,0,0,0,0,0,0]
python:
    while pp_inventory_limited_start_list.count(1) < 3:
        tmpInt = renpy.random.randint(0, 7)
        if pp_inventory_limited_start_list[tmpInt] == 0:
            pp_inventory_limited_start_list[tmpInt] = 1
            pp_inventory_limited_list[tmpInt] = 1

default pp_seed = renpy.random.randint(0,4)


default pp_tut_inventory_limited_list = [1,1,1,1,0,1,0,0]
default pp_bought_tut_this_round = [0,0,0,0,0,0,0,0]
default pp_activity_list = []
default pp_tut_activity_list = [[["Drinking Game",1],["Nothing",0]],[["Dancing",0],["Shots",2],["Nothing",0]],[["All-you-can-eat",3],["Nothing",0]]]
default pp_tut_activity_choices = [1,2,1]
default pp_grid = []
default pp_active_grid = []
default pp_grid_hovered = [-1,-1]
default pp_dik_info = 0
default pp_needs = []
default pp_activity_number = 0
default pp_party_rank = []
default currentPPRoundLabel = ""
default pp_money = 20
default pp_tut_money = 20
default pp_extra_budget = 0
default pp_score = 0
default pp_multiplier = 1.00
default pp_tut_multiplier = 1.25
default pp_bonus_multiplier = 1.00
default pp_extra_happiness = 1.00
default pp_happiness_penalty = 1.00
default pp_multiplier_madness = 0.00
default pp_below_budget = 0
default from_game_tut = False
default pp_tut_state = 0
default ep9_mad_at_zoey = False
default pp_perk_list = [False,False,False,False,False,False,False,False,False,False,False,False]

default ep9_body_shots = False
default ep9_body_shots_becky = False
default ep9_drinking_competition = False
default ep9_scary_stories = False
default ep9_haunted_mansion = False
default ep9_cumpetition = False
default ep9_tiffani_lick = False
default ep9_cumpetition_join = False
default ep9_ended_night_with = ""
default ep9_lily_nicole_lewd = False
default ep9_quinn_lewd = False
default ep9_spoon_nicole = False
default ep9_spoon_lily = False
default ep9_jm_fight = True
default ep9_restocked_food = False
default ep9_top_three = ["","",""]
default ep9_top_pick = ""
default ep9_winner = ""
default ep9_camila_lewd = False
default ep9_helped_sally = False
default ep9_tara_kiss = False

default ep9_jb_gf = False
default ep9_prep_truce = False

default ep9_sally_drink = False
default ep9_help_derek = False
default ep9_sarah_punch = False
default ep9_dangerous = False

default ep9_josy_dance = False
default ep9_maya_dance = False

default ep9_maya_lewd = False
default ep9_alone_maya = False
default ep9_quinn_ask = False
default ep9_alone_josy = False
default ep9_heather_lewd = -1
default ep9_kissed_rio = False
default ep9_cheered_rio = False
default ep9_rio_joke = False
default pq_found_buttons = 0

default ep9_josy_cluck = 0
default ep9_maya_cluck = 0
default ep9_others_texted = [False,False,False,False,False,False]
if not renpy.variant("pc"):
    $ branchIsabella = True
    $ branchSage = True
    $ branchJill = True
    $ branchMayaJosy = True

if npenalty == None:
    $ npenalty = 0
if persistent.ep9_c1 == None:
    $ persistent.ep9_c1 = False

$ roosterNickTyballs = "Tyballs@PussyFaceTybaltBurke"
$ rooster_nick_list[-1][1] = "Tyballs@PussyFaceTybaltBurke"


$ rooster_nick_list.insert(-7, ["Tiffani","Tiffani@Tiff"])
$ rooster_nick_list.insert(-8, ["Tara","Tara@SimplyTara"])
$ rooster_nick_list.insert(36, ["Kylie","Kylie@TrueBeauty"])
$ rooster_nick_list.insert(34, ["Jonah","Jonah@Wormhole"])
$ rooster_nick_list.insert(30, ["Jenna","Jenna@Akaibara"])
$ rooster_nick_list.insert(22, ["Emma","Emma@SnakeEyes"])
$ rooster_nick_list.insert(16, ["Clara","Clara@SweetGirl12"])
$ rooster_nick_list.insert(16, ["Christie","Christie@MeowMeow157"])
$ rooster_nick_list.insert(10, ["Bret","Bret@stInky"])
$ rooster_nick_list.append(["Zoey","Zoey@Kickflip"])
$ rooster_nick_list.insert(-12, ["Sally","Sally@Sallycylic"])
$ rooster_nick_list.insert(64, ["Suzy","Suzy@Femquality"])
$ rooster_nick_list.insert(54, ["Penny","Penny@PickMeUp"])
$ rooster_nick_list.insert(50, ["Micha","Micha@LiveLoveLaugh"])

default roosterNickTiffani = "Tiffani@Tiff"
default roosterNickTara = "Tara@SimplyTara"
default roosterNickLinda = "Linda@Burger"
default roosterNickKylie = "Kylie@TrueBeauty"
default roosterNickJonah = "Jonah@Wormhole"
default roosterNickJenna = "Jenna@Akaibara"
default roosterNickEmma = "Emma@SnakeEyes"
default roosterNickChristie = "Christie@MeowMeow157"
default roosterNickBret = "Bret@stInky"
default roosterNickSally = "Sally@Sallycylic"
default roosterNickKaren = "Karen@Scio"
default roosterNickClara = "Clara@SweetGirl12"
default roosterNickSuzy = "Suzy@Femquality"
default roosterNickPenny = "Penny@PickMeUp"
default roosterNickMicha = "Micha@LiveLoveLaugh"

default mbios_history_bianca = []
default mbios_history_christie = []
default mbios_history_kylie = []
default mbios_history_micha = []
default mbios_history_philip = []
default mbios_history_tara = []
default mbios_history_tiffani = []

default bios_txt_bianca = ""
if branchJill:
    $ bios_txt_bianca = "Bianca is Jill's close friend. She's in a relationship with Matthew."
else:
    $ bios_txt_bianca = "Bianca is Jill's friend. I don't know much more about her than that."
default bios_txt_christie = "I've seen Christie at several parties. She's one of the popular dorm girls and friends with Becky."
default bios_txt_kylie = "Kylie is one of the dorm girls who parties with the DIKs and HOTs."
default bios_txt_micha = "Micha seems like a sweet girl. Rusty is quite interested in her."
default bios_txt_philip = "Philip Hoff. Our new math teacher. Unlikely to get a nude cluck on Rooster."
default bios_txt_tara = "Tara is a party girl. She seems to be in a relationship with some dude named Oscar."
default bios_txt_tiffani = "Tiffani is a wild dorm girl with very low inhibitions from the looks of it."

$ mphone_bios_chars_list.insert(60,["Tiffani",[1],bios_txt_tiffani,mbios_history_tiffani,0])
$ mphone_bios_chars_list.insert(60,["Tara",[1],bios_txt_tara,mbios_history_tara,0])
$ mphone_bios_chars_list.insert(48,["Philip",[2,8],bios_txt_philip,mbios_history_philip,0])
$ mphone_bios_chars_list.insert(43,["Micha",[1],bios_txt_micha,mbios_history_micha,0])
$ mphone_bios_chars_list.insert(35,["Kylie",[1],bios_txt_kylie,mbios_history_kylie,0])
$ mphone_bios_chars_list.insert(15,["Christie",[1],bios_txt_christie,mbios_history_christie,0])
$ mphone_bios_chars_list.insert(8,["Bianca",[1],bios_txt_bianca,mbios_history_bianca,0])
$ mphone_stats_generate_girls()

default pp_nm_dik_happiness = [1,1,1,1,1,1,1,1]
default pp_nm_tmp_happiness = [0,0,0,0,0,0,0,0]
default pp_nm_party_preference = []
default pp_nm_activity_description = []
default currentActivity = 0

$ persistent.name = name


python:
    while len(mphone_chat_history_list[1][3]) > len(mphone_chat_history_list[1][2]):
        mphone_chat_history_list[1][3].pop()

jump previousEp9Label

init:
    if persistent.fx == None:
        $ persistent.fx = True
    if persistent.pp_tutorial == None:
        $ persistent.pp_tutorial = 0
    if persistent.fx_tip == None:
        $ persistent.fx_tip = False
    if persistent.seen_cutscene_ep9 == None:
        $ persistent.seen_cutscene_ep9 = [False,False,False]
    define pp_activity_base_score = 1000
    define pp_needs_met_base_score = 4
    define pp_item_base_score = 100
    define pp_icons_limited_list = ["Beers","Decor","Drugs","Food","Kegs","Liquor","Snacks","Speakers"]
    define pp_icons_unlimited_list = ["Cups","Girls","Guys","Music","Trashcans"]
    define pp_connector_list = ["ul","uc","ur","ml","mr","ll","lc","lr"]
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
