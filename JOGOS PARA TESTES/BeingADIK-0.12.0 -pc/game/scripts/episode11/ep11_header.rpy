label header_ep11_label:
$ currentEpisode = 11
$ vault_unlocked = False
$ safe_digits = [0,0,0,0]
$ randInt = renpy.random.randint(0, 17)

$ pp_seed = renpy.random.randint(0,4)
$ sm_experiment = 2
$ persistent.name = name
$ ep7_madame_options_list[2].append("Anal sex {color=#36ca2b}$$$$${/color}")
$ badik_chapter = "3"





default phone_bars_zero = False
default ep11_girl_leaving = False
default ep11_kissed_sage = False
default ep11_rio_text = 0
default bp_cpu_cups_tmp = 0
default ep11_pp_alcohol_food = 2
default ep11_pp_contest = 2
default ep11_pp_game = 1
default ep11_girl_drink_opportunity = False
default ep11_quinn_question = [False,False]
default ep11_mg_party = False
default ep11_virus = False
default ep11_rusty_choice = False
default ep11_rolling = False
default ep11_sage_stance = 0
default ep11_josy_dare = False
default ep11_jade_lewd = False
default ep11_josy_pic = [0,0]
default ep11_kp_choice = "CHICK"
default ep11_jade_care = False
default ep11_zoey_kiss = 0
default ep11_tommy_admit = False
default ep11_mistletoe = 0
default ep11_zoey_hug = False
default ep11_sally_kiss = False
default ep11_nicole_over_lily = False
default ep11_nicole_dating = False
default ep11_x = False
default ep11_zscore = 0
default ep11_db_mission = False
default ep11_db_mission_progress = 0
default ep11_lily_want_more = False
default ep11_camila_flirt = False
default ep11_flowers = False
default ep11_camila_came = False
default ep11_follow_quinn = False
default ep11_sage_camila_lewd = False
default ep11_fighter = False
default ep11_music = False
default ep11_scientist = False
default ep11_camila_lewd = False
default ep11_camila_opportunity = False
default ep11_sage_sober = False
default ep11_mel_lewd = False
default guess_who_list = []
default guess_who_score = 0
default ep11_sarah_lewd = False
default ep11_sarah_kiss = False
default ep11_mel_kiss = False
default ep11_bianca_flirt = False
default brawler_attitude = 0
default ep11_gift_money = 0
default ep11_gift_money_tracker = 0
if not minigames:
    $ ep11_gift_money = 5
    $ ep11_gift_money_tracker = 5
default ep11_bianca_feet = False
default ep11_bp_won_bella = False
default ep11_bianca_pic = 0
default ep11_bianca_dick = 0
default ep11_bianca_path = False
default ep11_nick_attitude = 0
default ft_nick_money = 0
default ep11_gift_opp = 3
default ep11_pp_santa_bc = False
default ep11_jill_style = 0
default ep11_helped_erin_mia = False
default ep11_gift_list = [0,0,0,0,0,0]
default ep11_jill_tease = False
default ep11_becky_lewd = 0
default ep11_apologize_jb = False
default ep11_tara_attitude = 0
default ep11_invited_tara = False
default ep11_lily_hard_fuck = False
default ep11_honor_safe_word = False
default ep11_cammy_draught = False
default text_message_screen_list = []
default ep11_tshirt_winner = ""
default ep11_elena_lewd = False
default ep11_josy_solo = False
default ep11_maya_solo = False
default ep11_josy_love = 0
default ep11_maya_love = 0
default ep11_josy_spoon = False
default ep11_sage_love = 0
default ep11_bella_comfort = False
default ep11_dildo_sucking = False
default ep11_tiffani_lewd = False
default ep11_tara_lewd = False
default ep11_dildo_sucking_girl = ""
default ep11_christie_flirt = False
default ep11_sage_questions = [False,False]
if affinity == "DIK":
    $ brawler_attitude += 1
if ep10_troy_mad:
    $ brawler_attitude += 1

$ mphone_bios_chars_list[14][1].append(5)

default ep11_chem_status = 0
if minigames:
    if sm_purity <= 50:
        $ ep11_chem_status += 0
    else:
        if sm_purity < 75:
            $ ep11_chem_status += 1
        else:
            $ ep11_chem_status += 2
else:
    if affinity == "DIK":
        $ ep11_chem_status += 0
    else:
        $ ep11_chem_status += 2
python:
    for i in range(0,len(rooster_nick_list)):
        if rooster_nick_list[i][0] == "Carla":
            rooster_nick_list[i][1] = "Carla@CourageousCarla"
        if rooster_nick_list[i][0] == "Olivia":
            rooster_nick_list[i][1] = "Olivia@Livvy"

default roosterNickBlogGuy1 = "Andy@TornadoAndy"
$ rooster_nick_list.append(["BlogGuy1","Andy@TornadoAndy"])
default roosterNickBlogGuy2 = "Bobby@Blobert"
$ rooster_nick_list.append(["BlogGuy2","Bobby@Blobert"])
default roosterNickBlogGirl1 = "Fiona@Fifi"
$ rooster_nick_list.append(["BlogGirl1","Fiona@Fifi"])
default roosterNickBlogGirl2 = "AnnaLee@MuffinWave"
$ rooster_nick_list.append(["BlogGirl2","AnnaLee@MuffinWave"])
default roosterNickBlogGirl3 = "Amanda@SaucyLibra"
$ rooster_nick_list.append(["BlogGirl3","Amanda@SaucyLibra"])
default roosterNickBlogGirl4 = "Beatrix@PeachParrot"
$ rooster_nick_list.append(["BlogGirl4","Beatrix@PeachParrot"])
default roosterNickGina = "Gina@FireHawk"
$ rooster_nick_list.append(["Gina","Gina@FireHawk"])
default roosterNickBlogUser1 = "user235444@TruPatriotXx_1"
$ rooster_nick_list.append(["BlogUser1","user235444@TruPatriotXx_1"])
default roosterNickBlogUser2 = "LeakedPicsNow@LeakedPicsNow"
$ rooster_nick_list.append(["BlogUser2","LeakedPicsNow@LeakedPicsNow"])
$ fixChatLists()
jump previousEp11Label

init:
    if persistent.ep11_c1 == None:
        $ persistent.ep11_c1 = False
    if persistent.seen_cutscene_ep11 == None:
        $ persistent.seen_cutscene_ep11 = [False]
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
