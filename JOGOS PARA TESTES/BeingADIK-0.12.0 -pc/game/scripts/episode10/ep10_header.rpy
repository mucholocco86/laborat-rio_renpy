label header_ep10_label:
$ currentEpisode = 10
$ vault_unlocked = False
$ safe_digits = [0,0,0,0]
$ safe_digit_1 = 0
$ safe_digit_2 = 0
$ safe_digit_3 = 0
$ safe_digit_4 = 0
$ randInt = renpy.random.randint(0, 17)

$ pp_seed = renpy.random.randint(0,4)
$ persistent.name = name
default tutorial_ongoing = False
default mphone_custom_wallpaper_max_width = 1920
default mphone_custom_wallpaper_tmp_xpos = 655
default mphone_custom_wallpaper_tmp_ypos = 0
default mphone_custom_wallpaper_tmp_zoom = 1.0
default mphone_custom_wallpaper_xpos = 655
default mphone_custom_wallpaper_ypos = 0
default mphone_custom_wallpaper_zoom = 1.0
default mphone_custom_wallpaper = ""
default mphone_stats_girl_list = []
default mphone_stats_girl_log = []
$ badik_chapter = "3"

$ tmpInt = getListIdx("The DIKs' party is awesome, but I'm a bit sad I didn't bring more condoms. {color=#00a0e6}#TooManyHotGuys{/color}",mroosterTextArray)
if tmpInt != -1:
    $ add_rooster_comment_response(tmpInt,"josy","This was a dare, guys. I am not sad that I didn't bring more condoms.", 15)
    $ add_rooster_comment_response(tmpInt,"sarah","{color=#00a0e6}@%s{/color} So, what you're saying is that you fuck without condoms?" % roosterNickJosy.split("@")[1], 8)
    $ add_rooster_comment_response(tmpInt,"arieth","{color=#00a0e6}@%s{/color} I don't use condoms either, but you can't even trust birth control pills these days." % roosterNickJosy.split("@")[1], 4)
    $ add_rooster_comment_response(tmpInt,"josy","{color=#00a0e6}@%s{/color} That's not what I'm saying." % roosterNickSarah.split("@")[1], 3)
    $ add_rooster_comment_response(tmpInt,"elena","What the hell did I miss yesterday?", 3)
    $ add_rooster_comment_response(tmpInt,"josy","{color=#00a0e6}@%s{/color} This is your fault, you know." % roosterNickMC.split("@")[1], 5)
$ tmpInt = getListIdx("The DIKs' party is awesome, but I'm a bit sad I came dressed as a fairy, when I wanted to come as a baby with a diaper. {color=#00a0e6}#MeLikeyDiapers{/color}",mroosterTextArray)
if tmpInt != -1:
    $ add_rooster_comment_response(tmpInt,"josy","This was a dare, guys. And a bad one at that.", 12)
    $ add_rooster_comment_response(tmpInt,"riona","{color=#00a0e6}@%s{/color} There's always New Year's Eve. Why don't you come dressed up as Baby New Year?" % roosterNickJosy.split("@")[1], 2)
    $ add_rooster_comment_response(tmpInt,"josy","{color=#00a0e6}@%s{/color} Because that would be creepy and weird. Haha!" % roosterNickRiona.split("@")[1], 2)



if len(mphone_chat_history_list[-1][2]) + 1 == len(mphone_chat_history_list[-1][3]):
    $ mphone_chat_history_list[-1][3].pop()



if branchMayaJosy:
    python:
        for x in mphone_bios_chars_list:
            if x[0] == "Maya":
                if any("Maya got frisky with me in public. But she stopped after I mentioned that Josy wasn't there with us." in s for s in x[3]):
                    ep9_maya_lewd = False
                if any("Maya was getting frisky with me in public. But she stopped after I mentioned that Josy wasn't there with us." in s for s in x[3]):
                    ep9_maya_lewd = False
else:
    $ ep9_maya_lewd = False



$ mphone_stats_unlocked_state = 1
$ mphone_pp_history_list = []
if minigames and len(mphone_pp_history_list) == 0:
    if ep9_body_shots:
        $ mphone_pp_history_list.append("• The {color=ffed00}Body shots{/color} activity increased Jacob's happiness by {color=00ff00}+3%{/color}.")
        $ mphone_pp_history_list.append("• The {color=ffed00}Body shots{/color} activity increased Jamie's happiness by {color=00ff00}+3%{/color}.")
        $ mphone_pp_history_list.append("• The {color=ffed00}Body shots{/color} activity increased Nick's happiness by {color=00ff00}+3%{/color}.")
        $ mphone_pp_history_list.append("• The {color=ffed00}Body shots{/color} activity increased Tommy's happiness by {color=00ff00}+3%{/color}.")
    elif ep9_drinking_competition:
        $ mphone_pp_history_list.append("• The {color=ffed00}Drinking competition{/color} activity increased Jamie's happiness by {color=00ff00}+2%{/color}.")
        $ mphone_pp_history_list.append("• The {color=ffed00}Drinking competition{/color} activity increased Leon's happiness by {color=00ff00}+2%{/color}.")
        $ mphone_pp_history_list.append("• The {color=ffed00}Drinking competition{/color} activity increased Rusty's happiness by {color=00ff00}+2%{/color}.")
        $ mphone_pp_history_list.append("• The {color=ffed00}Drinking competition{/color} activity increased Tommy's happiness by {color=00ff00}+2%{/color}.")
    if ep9_scary_stories:
        $ mphone_pp_history_list.append("• The {color=ffed00}Scary stories{/color} activity increased Derek's happiness by {color=00ff00}+2%{/color}.")
        $ mphone_pp_history_list.append("• The {color=ffed00}Scary stories{/color} activity increased Jacob's happiness by {color=00ff00}+2%{/color}.")
        $ mphone_pp_history_list.append("• The {color=ffed00}Scary stories{/color} activity increased John Boy's happiness by {color=00ff00}+2%{/color}.")
    elif ep9_haunted_mansion:
        $ mphone_pp_history_list.append("• The {color=ffed00}Haunted mansion{/color} activity increased Jacob's happiness by {color=00ff00}+2%{/color}.")
        $ mphone_pp_history_list.append("• The {color=ffed00}Haunted mansion{/color} activity increased Jamie's happiness by {color=00ff00}+2%{/color}.")
        $ mphone_pp_history_list.append("• The {color=ffed00}Haunted mansion{/color} activity increased John Boy's happiness by {color=00ff00}+2%{/color}.")
        $ mphone_pp_history_list.append("• The {color=ffed00}Haunted mansion{/color} activity increased Nick's happiness by {color=00ff00}+2%{/color}.")
    if ep9_cumpetition:
        $ mphone_pp_history_list.append("• The {color=ffed00}CUM-petition{/color} activity increased Leon's happiness by {color=00ff00}+2%{/color}.")
        $ mphone_pp_history_list.append("• The {color=ffed00}CUM-petition{/color} activity increased Tommy's happiness by {color=00ff00}+2%{/color}.")

    $ tmpStr = ""
    if ep9_body_shots:
        $ tmpStr += "• Body shots "
    elif ep9_drinking_competition:
        $ tmpStr += "• Drinking competition "
    if ep9_scary_stories:
        $ tmpStr += "• Scary stories "
    elif ep9_haunted_mansion:
        $ tmpStr += "• Haunted mansion "
    if ep9_cumpetition:
        $ tmpStr += "• CUM-petition "
    if tmpStr == "":
        $ tmpStr = "None"

    $ mphone_pp_history_list.append("DIKs' Halloween party\n{color=fe9416}Activities:{/color} %s\n{color=fe9416}Total Party Score:{/color} {color=ffed00}%d{/color}\n{color=fe9416}Total Score:{/color} {color=ffed00}%d{/color}\n{color=e51475}Multiplier: %sx{/color}\n{color=fe9416}Rank:{/color} {color=ffed00}%s{/color}" % (tmpStr,pp_round_score,pp_score,pp_multiplier,pp_party_rank[0][1]))
    $ mphone_pp_history_list.append("")
    $ mphone_pp_history_list.append("")
    $ mphone_pp_history_list.append("")

if ep9_jade_lewd:
    $ mphone_stats_add_girl_s3("jade","You had sex with Jade in her kitchen in episode 9.")

if ep9_others_texted[4]:
    $ mphone_stats_add_girl_s3("lily","You had phone sex with Lily in episode 9.")
if ep9_camila_lewd:
    $ mphone_stats_add_girl_s3("camila","You had sex with Camila on the dance floor in episode 9.")
if ep9_maya_lewd:
    $ mphone_stats_add_girl_s3("maya","You had sex with Maya behind the green screen in episode 9.")
if ep9_heather_lewd == 2:
    $ mphone_stats_add_girl_s3("heather","You got a boobjob and a blowjob from Heather at the Halloween party in episode 9.")

if ep9_cumpetition_join:
    $ mphone_stats_add_girl_s3("envy","Lily and Nicole entertained you during the CUM-petition at the Halloween party in episode 9.")
    $ mphone_stats_add_girl_s3("lily","Lily and Nicole entertained you during the CUM-petition at the Halloween party in episode 9.")

if ep9_quinn_lewd:
    $ mphone_stats_add_girl_s3("quinn","You had sex with Quinn after the Halloween party in episode 9.")

if ep9_sarah_melanie_lewd:
    $ mphone_stats_add_girl_s3("sarah","You had a threesome with Sarah and Melanie after the Halloween party in episode 9.")
    $ mphone_stats_add_girl_s3("melanie","You had a threesome with Sarah and Melanie after the Halloween party in episode 9.")

if ep9_lily_nicole_lewd:
    $ mphone_stats_add_girl_s3("envy","You had a threesome with Nicole and Lily after the Halloween party in episode 9.")
    $ mphone_stats_add_girl_s3("lily","You had a threesome with Nicole and Lily after the Halloween party in episode 9.")

if branchJill:
    if ep9_jill_lewd:
        $ mphone_stats_add_girl_s3("jill","You had fun with Jill on her bed in episode 9.")
    $ mphone_stats_add_girl_s3("jill","You had sex with Jill after the Halloween party in episode 9.")
if branchIsabella:
    $ mphone_stats_add_girl_s3("isabella","You had sex with Bella after the Halloween party in episode 9.")
if branchSage:
    $ mphone_stats_add_girl_s3("sage","You had sex with Sage on her bed in episode 9.")
    if ep9_haunted_mansion:
        $ mphone_stats_add_girl_s3("sage","You had sex with Sage during the Haunted mansion activity in episode 9.")
    $ mphone_stats_add_girl_s3("sage","You had anal sex with Sage after the Halloween party in episode 9.")
if branchMayaJosy:
    $ mphone_stats_add_girl_s3("maya","You had a threesome with Josy and Maya after the Halloween party in episode 9.")
    $ mphone_stats_add_girl_s3("josy","You had a threesome with Josy and Maya after the Halloween party in episode 9.")


default bios_txt_nora = "Dr. Nora Jenkins. She is the lab teacher of my chemistry class. She's passionate about science and seems very smart."
default mbios_history_nora = []
default pp_score_nm = 0
default ep10_msolo_josy_focus = False
default ep10_date_nicole = False
default ep10_read_notepad = False
default ep10_rejected_nicole = False
default ep10_rolling = False
default ep10_sage_lewd = False
default ep10_dating_nora = False
default ep10_nora_kids = False
default ep10_lily_english = False
default ep10_told_jb_about_heather = False
default ep10_cameras = 0
default ep10_clean = 0
default ep10_troy_mad = False
default ep10_gundead_win = False
default ep10_patrick_penalty = 0
default ep10_nora_lewd = False
default ep10_elena_offer = False
default ep10_tommy_reply = 0
default ep10_nora_encourage = False
default ep10_zoey_hangout = True
default ep10_feelingsForMaya = False
default ep10_feelingsForJosy = False
default ep10_paula_state = 0
default ep10_pp_alcohol = 2
default ep10_pp_meat = 2
default ep10_pp_activity = 2
default ep10_bella_overreacting = False
default ep10_cathy_coffee = False
default ep10_cathy_lewd = False
default ep10_cancel_date_nicole = False
default ep10_jm_solo = ""
default ep10_riona_date = False
default ep10_riona_lewd = False
default ep10_zoey_jacob = False
default ep10_jb_elena_hot = False
default ep10_nick_response = 0
default ep10_quote = ""
default ep10_jill_promise = False
default ep10_bp_won_camila = False
default ep10_rio_animal = False
default ep10_others_intro = False
default ep10_tybalt_mercy = False
default ep10_got_contracts = False
default sage_dik = 0
default ep10_quinn_help = False
default ep10_patrick_choice = ""
default ep10_shroom_choice = ""
default ep10_quinn_lewd = False
default ep10_dots_attitude = 0
default ep10_nicole_questions = [False,False,False]
default ep10_nick_questions = [0,0,0]
default ep10_quinn_photo = 0
if ep8_sq_lewd:
    $ sage_dik += 1

default ep10_ufo = renpy.random.randint(0,500)

default mphone_app_gallery_enabled = False
default mphone_app_gallery_new = True
default mphone_app_gallery_first_time = True
default mphone_app_wp_first_time = True


$ ep7_madame_options_list[2].append("Footjob {color=#36ca2b}${/color}")
$ ep7_madame_options_list[2].append("Boobjob {color=#36ca2b}$${/color}")
$ ep7_madame_options_list[2].append("Vaginal sex {color=#36ca2b}$$$${/color}")

default ep5_questions_event = False
python:
    if "He was skeptical of me being at the Alpha Nu Omega party." in mphone_bios_chars_list[15][3]:
        ep5_questions_event = True
    else:
        ep5_questions_event = False

default sm_bunsen_on = False
default sm_stirrer_on = False
default sm_stirrer_str = "empty"
default sm_scale_str = "empty"
default sm_vol_str = "empty"
default sm_round_str = "empty"
default sm_measure_color = "red"
default sm_measure_vol = 0
default sm_tut_text = 0
default sm_measure_phase = 0
default sm_measure_result_vol = 0
default sm_time_penalty = 0
default sm_button_set = 0
default sm_pour_mode = 0
default sm_weigh_color = ""
default sm_weigh_result = 0
default sm_weight = 0
default sm_weigh_phase = 0
default sm_stirrer_vol = 0
default sm_stirrer_mode = 0
default sm_stir_list = []
default sm_round_list = []
default sm_experiment = 1
default sm_purity = 0
default sm_stirrer_criteria = 0
default sm_round_criteria = 0
default sm_cue_color_change = []
default sm_experiment_list = []
default e_time = 1.95
default ms_time = 200
default timer_range = 100
default sm_hard_mode = True
default sm_perk_time = 0
default sm_studied = 0
default sm_perk_purity = 0
default sm_perk_pencil = False
default sm_notes = []
default failedScienceS3 = 0
default maxedScienceS3 = 0
default passedScienceS3 = 0

default failedEnglishS3 = 0
default maxedEnglishS3 = 0
default passedEnglishS3 = 0
default englishResult = 0
default eng_word = ""
default eng_max_length = 6
default eng_rew = False
default eng_perc3 = 0
default eng_perc4 = 0
default eng_perc5 = 0
default eng_perc6 = 0
default eng_total3 = 0
default eng_total4 = 0
default eng_total5 = 0
default eng_total6 = 0
default eng_list6 = []
default eng_list5 = []
default eng_list4 = []
default eng_list3 = []
default eng_lists_used = []
default eng_chars = []
default eng_chars_word = ""
default eng_jump_label = ""
default eng_cheated = False
default eng_completed_list6 = []
default eng_completed_list5 = []
default eng_completed_list4 = []
default eng_completed_list3 = []
default eng_yalign = [0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0]

default ft_death_rate = 10
default ft_sick_rate = 20
default ft_tank_state = 40
default ft_repro_rate = 15
default ft_filth_rate = 30
default ft_food_state = 0
default ft_round = 1
default ft_debug = False
default ft_tool_tip = 0
default ft_tt = []
$ ft_tt.append("Press X to close the Fish tank mini-game. The changes you've made will have an effect before the next free roam event at the DIKs' mansion.")
$ ft_tt.append("Clean the tank. Costs one {color=ffed00}Cleaning{/color} supply to use. A {color=1df400}clean{/color} tank will let your fish reproduce and stay healthy during their lifespan.")
$ ft_tt.append("The tank is {color=1df400}clean{/color}! A {color=1df400}clean{/color} tank helps fish live longer and healthier lives and yield more offspring.")
$ ft_tt.append("The tank is {color=ffed00}dirty{/color}! A {color=ffed00}dirty{/color} tank will cause fish to {color=f72400}die{/color} faster, reproduce less, and increase the risk of {color=ffc27b}sickness{/color}.")
$ ft_tt.append("The tank is {color=f72400}toxic{/color}! A {color=f72400}toxic{/color} tank is detrimental to the fish's health.\nClean it fast, or your fish will {color=f72400}die{/color}.")
$ ft_tt.append("Your fish are hungry! Feed them with the fish {color=ffed00}food{/color} supply, or they will starve. Starving fish {color=f72400}die{/color} faster, reproduce at a slower rate, and get {color=ffc27b}sick{/color}.")
$ ft_tt.append("Your fish are well-fed. Well-fed fish reproduce at a faster rate and stay healthier.")
$ ft_tt.append("Your fish are getting too much {color=ffed00}food{/color}! Their reproduction rate will be slower if you give them too much {color=ffed00}food{/color}.")
$ ft_tt.append("Feed your fish. Costs 5 {color=ffed00}Food{/color} supplies to use. As a rule of thumb, one {color=ffed00}food{/color} per fish will keep the fish well-fed.")
$ ft_tt.append("You're out of fish {color=ffed00}Food{/color}!\nBuy more to feed your fish.")
$ ft_tt.append("Your fish population. The only way to increase it is to make the fish reproduce by keeping the tank {color=1df400}clean{/color} and the fish healthy and well-fed.")
$ ft_tt.append("Your {color=fe67b2}female{/color} fish population. {color=fe67b2}Female{/color} fish regulate reproduction.\n{color=1df400}Young{/color} fish can evolve into either {color=39e4db}male{/color} or {color=fe67b2}female{/color} fish between rounds.")
$ ft_tt.append("Your {color=39e4db}male{/color} fish population. {color=39e4db}Male{/color} fish have no effect on reproduction. {color=1df400}Young{/color} fish can evolve into either {color=39e4db}male{/color} or {color=fe67b2}female{/color} fish between rounds.")
$ ft_tt.append("{color=1df400}Young{/color} fish are a result of successful reproduction. They evolve into mature fish after one round. You may sell them for a {color=1df400}profit{/color} or keep them.")
$ ft_tt.append("Sell 5 {color=1df400}young{/color} fish for {color=1df400}$2{/color}. If you never keep {color=1df400}young{/color} fish, your fish population will eventually decrease as fish {color=f72400}die{/color}.")
$ ft_tt.append("You need 5 {color=1df400}young{/color} fish to sell them for {color=1df400}$2{/color}. {color=1df400}Young{/color} fish are a result of successful reproduction.")
$ ft_tt.append("The {color=f72400}dead{/color} fish in your tank. Fish {color=f72400}die{/color} when they get too old. {color=ffc27b}Sickness{/color}, a lack of {color=ffed00}food{/color}, and a {color=ffed00}dirty{/color} or {color=f72400}toxic{/color} tank will make them {color=f72400}die{/color} faster.")
$ ft_tt.append("Removes the {color=f72400}dead{/color} fish from your tank.\nKeeping dead fish will make your tank dirtier.")
$ ft_tt.append("The {color=ffc27b}sick{/color} fish in your tank. {color=ffc27b}Sick{/color} {color=fe67b2}female{/color} fish cannot reproduce. Untreated {color=ffc27b}sickness{/color} will spread to other fish in your tank over time.")
$ ft_tt.append("Treats all {color=ffc27b}sick{/color} fish in your tank. Costs 1 {color=ffed00}Meds{/color} supply to use.\nHealthy fish are key to successful reproduction.")
$ ft_tt.append("You're out of {color=ffed00}Meds{/color}!\nBuy more to treat any {color=ffc27b}sick{/color} fish.")
$ ft_tt.append("You're out of {color=ffed00}Cleaning{/color} supplies.\nBuy more to clean your tank.")
$ ft_tt.append("Buy {color=ffed00}Food{/color} supplies. Use to feed your fish.\n{color=1df400}$1{/color} for 100 {color=ffed00}Food{/color}.")
$ ft_tt.append("Buy {color=ffed00}Cleaning{/color} supplies. Use to clean your tank.\n{color=1df400}$1{/color} for 1 {color=ffed00}Cleaning{/color} supply.")
$ ft_tt.append("Buy {color=ffed00}Meds{/color} supplies. Use to treat your fish.\n{color=1df400}$1{/color} for 1 {color=ffed00}Meds{/color} supply.")
$ ft_tt.append("Buy an {color=ffc015}Air pump{/color} for {color=1df400}$10{/color}.\nGives a big and permanent boost to tank cleanliness.")
$ ft_tt.append("Your {color=ffc015}Air pump{/color}.\nIt gives a big and permanent boost to tank cleanliness.")
$ ft_tt.append("Buy {color=ffc015}Chemicals{/color} for {color=1df400}$10{/color}.\nGives a permanent boost to fish reproduction.")
$ ft_tt.append("Your {color=ffc015}Chemicals{/color}.\nIt gives a permanent boost to fish reproduction.")
$ ft_tt.append("Buy {color=ffc015}Props{/color} for {color=1df400}$10{/color}.\nPermanently reduces {color=ffc27b}sickness{/color}.")
$ ft_tt.append("Your {color=ffc015}Props{/color}.\nPermanently reduces {color=ffc27b}sickness{/color}.")
$ ft_tt.append("You can't feed your fish any more {color=ffed00}Food{/color}!\nConsider selling {color=1df400}young{/color} fish if you have more fish than you can feed.")
$ ft_tt.append("You can't {color=ffed00}clean{/color} your tank more.\nIt's as clean as it gets.")
$ ft_tt.append("Extract {color=1df400}money{/color} from the Fish tank mini-game and use it as {color=1df400}pocket money{/color}. You can put {color=1df400}money{/color} back into the mini-game, too.")
$ ft_tt.append("Put {color=1df400}pocket money{/color} into the Fish tank mini-game and use it to purchase {color=ffed00}supplies{/color} or {color=ffc015}upgrades{/color}.")

default ft_fish_nm = 50
default ft_money = 5
default ft_failed = False
default ft_food_left = 0
default ft_inv_food = 0
default ft_inv_clean = 0
default ft_inv_med = 0
default ft_inv_ph = False
default ft_inv_props = False
default ft_inv_filter = False
default ft_tooltips = True
default ft_first_time = True

default ft_fish_list = []

python:
    while len(mphone_chat_history_list[1][3]) > len(mphone_chat_history_list[1][2]):
        mphone_chat_history_list[1][3].pop()
python:
    tmpInt = renpy.random.randint(25,35)
    for i in range (0,tmpInt):
        ft_fish_list.append(ft_fish("Female",renpy.random.randint(20,100), renpy.random.randint(0,1000) <= ft_sick_rate))
    for i in range (0,75-tmpInt):
        ft_fish_list.append(ft_fish("Male",renpy.random.randint(20,100), renpy.random.randint(0,1000) <= ft_sick_rate))
    for i in range (0,10):
        ft_fish_list.append(ft_fish("Young",renpy.random.randint(40,100), renpy.random.randint(0,1000) <= ft_sick_rate))

default math_task = 0
default math_task_correct_answers = []
default math_grid = []
default math_task_list = []
default math_task_desc = []
default math_bomb_grid = []
default math_query_info = []
default math_diamond_position = []
default math_task_total = 6
default math_active_tool = 0
default math_own_q = False
default math_own_query = False
default math_own_b = False
default math_bomb_used = False
default math_rew = False
default math_tooltips = True
default maxedMathS3 = 0
default passedMathS3 = 0
default failedMathS3 = 0
default math_d_count = 0
default math_query_count = 2
default math_query_count_total = 2
default math_b_count = 2
default math_b_count_total = 2
default math_d_count_total = 1
default math_buy_tool = 0
default math_tt = []
default math_tut_step = 0
default math_tool_tip = 0

default puzzle_box_side = 0
default puzzle_box_side_unlocked = [True,False,False,False,False,False]
default pb_button_pressed = [False,False,False,False,False,False]
default pb_button_unlockable = []
default pb_side1_dials = [0,0,0,0]
default pb_2nd_count = 0
default final_button_unlocked = False
default pb_completed = False
if persistent.pb_completed == None:
    $ persistent.pb_completed = False
if persistent.ep10_c1 == None:
    $ persistent.ep10_c1 = False
default pb_3_lid_open = [False,False,False,False,False]

default pb_3_buttons = [[True,True,True],[True,True,True],[True,True,True],[True,True,True]]
default pb_5_buttons = [5,2,7,4,9,8,1,3,6]
default pb_6_3count = [0,0,0]
default pb_6_4count = [0,0,0,0]
default pb_6_5count = [0,0,0,0,0]
default pb_6_3letters = [["u","n","c","s"],["u","m","o","y"],["t","n","d","m"]]
default pb_6_4letters = [["m","n","o","s"],["c","o","n","y"],["o","s","t","u"],["s","m","d","n"]]
default pb_6_5letters = [["n","s","d","y"],["t","m","a","c"],["y","d","r","a"],["c","r","d","o"],["u","t","y","s"]]

default bn_mc_stamina_lvl = 2
default bn_mc_stamina_max = 4
default bn_mc_stamina = 4
default bn_cpu_stamina_lvl = 4
default bn_cpu_stamina_max = 8
default bn_cpu_stamina = 8
default bn_cpu_name = ""
default bn_game_over = False
default bn_mc_won = False
default bn_freeroam = False
default bn_tut_msg = 0
default bn_arrow_input_tut = 0
default bn_mc_hp = 100
default bn_cpu_hp = 100

default bn_arrow_selection = ["","","",""]
default bn_arrow_combination = []
default bn_miss_list = ["MISS","FAIL","NOPE","SLIP","BAD"]
default bn_normal_list = ["HIT","WEAK","FIST","THUD","KICK","LOW","HIGH"]
default bn_power_list = ["SUPER","POWER","COMBO","OUCH","BREAK"]
default bn_special_list = ["RAGE"]
default bn_arrow_input = 0
default bn_combo_input = ""
default bn_turn = True

default bn_rage_flash = False
default bn_showing_img = False
default bn_rage_ending = False
default bn_rage_time = 0
default bn_cpu_attack = ""
default bn_img_name = ""
default bn_player_special_cd = 0
default bn_cpu_special_cd = 0
default bn_combo_idx = 0
default bn_skill_alloc = [0,0,0,0,0,0]
default bn_special = 0

default bn_reward = ""
default bn_skill_points_total = 0
default bn_timer = 3.0
default bn_player_block = 0.6
default bn_pc_counter_chance = 3
default bn_player_rage = 0

default bn_specials_unlocked = [False,False,False]
default bn_skill_max_level = 2
default bn_skill_points = 0
default bn_reward_available_list = [10,1,3,0]
default bn_player_power = 1.0
default bn_cpu_power = 2.0
default bn_cpu_counter_chance = 5
default bn_counter = False
default bn_show_counter = False
default bn_cpu_stunned = False
default bn_cpu_counter_stun = False

default bn_img_delay = 1
default bn_which_fighter = 0
default bn_fight_count = 0
default bn_fight_losses = 0
default bn_rage_record = 0
default bn_dmg_record = 0
default bn_rage_new_record = False
default bn_dmg_new_record = False
default bn_fight_wins = 0
default bn_img_list = []
default bn_delay_list = []
default bn_sound_list = []

default bn_hard_difficulty = True
default bn_opponent_list = []
default bn_history_list = [0,0,0,0,0]
default bn_money_reward = False
default bn_money_reward2 = False
default bn_money_reward3 = False
default bn_sr_reward = True
default bn_playlist = True
default bn_jump_label = ""

default grab_hovered = False
default claw_offset = [-600,0]

default bp_cpu_name = ""
default bp_jump_label = ""
default bp_ep_suffix = ""
default bp_player_chance_nm = 0
default bp_cpu_cups = 6
default bp_player_cups = 6
default bp_player_turn = False
default bp_game_over = False
default bp_player_won = False
default bp_showing_img = False
default bp_state = 0
default bp_mc_cue_strip = False
default bp_cpu_cue_strip = False
default bp_mc_strip_state = 0
default bp_cpu_strip_state = 0
default bp_delay = 2
default bp_dlg = 0
default bp_force_delay = False
default bp_action_msg = ""

default bp_player_ap = 10
default bp_cpu_ap = 10

default bp_player_chance = [75,33,50]
default bp_cpu_chance = [75,33,50]

default bp_img_list = [""]
default bp_img_name = ""

default bp_dlg_list = []
default bp_who_list = []

default bp_tut_ep10_seen = False

default roosterNickCarla = "Carla@CourageousCarla"
default roosterNickOlivia = "Olivia@Livvy"
default roosterNickWW = "Stallions@WW"
$ rooster_nick_list.insert(14, ["Carla","Carla@CourageousCarla"])
$ rooster_nick_list.insert(75, ["WW","Stallions@WW"])
$ rooster_nick_list.insert(56, ["Olivia","Olivia@Livvy"])

$ fixChatLists()
jump previousEp10Label

init:
    if persistent.bp_tutorial == None:
        $ persistent.bp_tutorial = False
    if persistent.math_tutorial == None:
        $ persistent.math_tutorial = False
    if persistent.science_tutorial == None:
        $ persistent.science_tutorial = False
    if persistent.brawler_tutorial == None:
        $ persistent.brawler_tutorial = False

init python:
    def bp_play_bounce(trans,st,at):
        renpy.play("sound_effects/season3/ping_pong_bounce.mp3","sfx1")
    def bp_play_bounce_shot(trans,st,at):
        renpy.play("sound_effects/season3/ping_pong_bounce_shot.mp3","sfx1")
    def bp_play_swat(trans,st,at):
        renpy.play("sound_effects/season3/ping_pong_swat.mp3","sfx1")
    def bp_play_splash(trans,st,at):
        renpy.play("sound_effects/season3/ping_pong_splash.mp3","sfx1")

    def checkProfanity(str):
        tmpList = str.split()
        profanity_list = ["2 girls 1 cup","2g1c","4r5e","5h1t","5hit","a$$","a$$hole","a_s_s","a2m","a54","a55","a55hole","aeolus","ahole","alabama hot pocket","alaskan pipeline","anal","anal impaler","anal leakage","analannie","analprobe","analsex","anilingus","anus","apeshit","ar5e","areola","areole","arian","arrse","arse","arsehole","aryan","ass","ass fuck","ass hole","assault","assbag","assbagger","assbandit","assbang","assbanged","assbanger","assbangs","assbite","assblaster","assclown","asscock","asscracker","asses","assface","assfaces","assfuck","assfucker","ass-fucker","assfukka","assgoblin","assh0le","asshat","ass-hat","asshead","assho1e","asshole","assholes","asshopper","asshore","ass-jabber","assjacker","assjockey","asskiss","asskisser","assklown","asslick","asslicker","asslover","assman","assmaster","assmonkey","assmucus","assmunch","assmuncher","assnigger","asspacker","asspirate","ass-pirate","asspuppies","assranger","assshit","assshole","asssucker","asswad","asswhole","asswhore","asswipe","asswipes","auto erotic","autoerotic","axwound","azazel","azz","b!tch","b00bs","b17ch","b1tch","babe","babeland","babes","baby batter","baby juice","badfuck","ball gag","ball gravy","ball kicking","ball licking","ball sack","ball sucking","ballbag","balllicker","balls","ballsack","bampot","bang","bang (one's) box","bangbros","banger","banging","bareback","barely legal","barenaked","barf","barface","barfface","bastard","bastardo","bastards","bastinado","batty boy","bawdy","bazongas","bazooms","bbw","bdsm","beaner","beaners","beardedclam","beastial","beastiality","beatch","beater","beatyourmeat","beaver","beaver cleaver","beaver lips","beef curtain","beef curtains","beer","beeyotch","bellend","bender","beotch","bestial","bestiality","bi+ch","biatch","bicurious","big black","big breasts","big knockers","big tits","bigbastard","bigbutt","bigger","bigtits","bimbo","bimbos","bint","birdlock","bisexual","bi-sexual","bitch","bitch tit","bitchass","bitched","bitcher","bitchers","bitches","bitchez","bitchin","bitching","bitchtits","bitchy","black cock","blonde action","blonde on blonde action","bloodclaat","bloody","bloody hell","blow","blow job","blow me","blow mud","blow your load","blowjob","blowjobs","blue waffle","blumpkin","boang","bod","bodily","bogan","bohunk","boink","boiolas","bollick","bollock","bollocks","bollok","bollox","bomd","bondage","bone","boned","boner","boners","bong","boob","boobies","boobs","booby","booger","bookie","boong","boonga","booobs","boooobs","booooobs","booooooobs","bootee","bootie","booty","booty call","booze","boozer","boozy","bosom","bosomy","bowel","bowels","bra","brassiere","breast","breastjob","breastlover","breastman","breasts","breeder","brotherfucker","brown showers","brunette action","buceta","bugger","buggered","buggery","bukkake","bull shit","bullcrap","bulldike","bulldyke","bullet vibe","bullshit","bullshits","bullshitted","bullturds","bum","bum boy","bumblefuck","bumclat","bumfuck","bummer","bung","bung hole","bunga","bunghole","bunny fucker","bust a load","busty","butchdike","butchdyke","butt","butt fuck","butt plug","buttbang","butt-bang","buttcheeks","buttface","buttfuck","butt-fuck","buttfucka","buttfucker","butt-fucker","butthead","butthole","buttman","buttmuch","buttmunch","buttmuncher","butt-pirate","buttplug","c.0.c.k","c.o.c.k.","c.u.n.t","c0ck","c-0-c-k","c0cksucker","caca","cahone","camel toe","cameltoe","camgirl","camslut","camwhore","carpet muncher","carpetmuncher","cawk","cervix","chesticle","chi-chi man","chick with a dick","child-fucker","chin","chinc","chincs","chink","chinky","choad","choade","choc ice","chocolate rosebuds","chode","chodes","chota bags","cipa","circlejerk","cl1t","cleveland steamer","climax","clit","clit licker","clitface","clitfuck","clitoris","clitorus","clits","clitty","clitty litter","clogwog","clover clamps","clunge","clusterfuck","cnut","cocain","cocaine","cock","c-o-c-k","cock pocket","cock snot","cock sucker","cockass","cockbite","cockblock","cockburger","cockeye","cockface","cockfucker","cockhead","cockholster","cockjockey","cockknocker","cockknoker","cocklicker","cocklover","cocklump","cockmaster","cockmongler","cockmongruel","cockmonkey","cockmunch","cockmuncher","cocknose","cocknugget","cocks","cockshit","cocksmith","cocksmoke","cocksmoker","cocksniffer","cocksucer","cocksuck","cocksuck ","cocksucked","cocksucker","cock-sucker","cocksuckers","cocksucking","cocksucks","cocksuka","cocksukka","cockwaffle","coffin dodger","coital","cok","cokmuncher","coksucka","commie","condom","coochie","coochy","coon","coonnass","coons","cooter","cop some wood","coprolagnia","coprophilia","corksucker","cornhole","corp whore","cox","crabs","crack","cracker","crackwhore","crack-whore","crap","crappy","creampie","cretin","crikey","cripple","crotte","cum","cum chugger","cum dumpster","cum freak","cum guzzler","cumbubble","cumdump","cumdumpster","cumguzzler","cumjockey","cummer","cummin","cumming","cums","cumshot","cumshots","cumslut","cumstain","cumtart","cunilingus","cunillingus","cunn","cunnie","cunnilingus","cunntt","cunny","cunt","c-u-n-t","cunt hair","cuntass","cuntbag","cuntface","cuntfuck","cuntfucker","cunthole","cunthunter","cuntlick","cuntlick ","cuntlicker","cuntlicker ","cuntlicking","cuntrag","cunts","cuntsicle","cuntslut","cunt-struck","cuntsucker","cut rope","cyalis","cyberfuc","cyberfuck","cyberfucked","cyberfucker","cyberfuckers","cyberfucking","cybersex","d0ng","d0uch3","d0uche","d1ck","d1ld0","d1ldo","dago","dagos","dammit","damn","damned","damnit","darkie","darn","date rape","daterape","dawgie-style","deep throat","deepthroat","deggo","dendrophilia","dick","dick head","dick hole","dick shy","dickbag","dickbeaters","dickbrain","dickdipper","dickface","dickflipper","dickfuck","dickfucker","dickhead","dickheads","dickhole","dickish","dick-ish","dickjuice","dickmilk","dickmonger","dickripper","dicks","dicksipper","dickslap","dick-sneeze","dicksucker","dicksucking","dicktickler","dickwad","dickweasel","dickweed","dickwhipper","dickwod","dickzipper","diddle","dike","dildo","dildos","diligaf","dillweed","dimwit","dingle","dingleberries","dingleberry","dink","dinks","dipship","dipshit","dirsa","dirty","dirty pillows","dirty sanchez","dlck","dog style","dog-fucker","doggie style","doggiestyle","doggie-style","doggin","dogging","doggy style","doggystyle","doggy-style","dolcett","domination","dominatrix","dommes","dong","donkey punch","donkeypunch","donkeyribber","doochbag","doofus","dookie","doosh","dopey","double dong","double penetration","doublelift","douch3","douche","douchebag","douchebags","douche-fag","douchewaffle","douchey","dp action","drunk","dry hump","duche","dumass","dumb ass","dumbass","dumbasses","dumbcunt","dumbfuck","dumbshit","dummy","dumshit","dvda","dyke","dykes","eat a dick","eat hair pie","eat my ass","eatpussy","ecchi","ejaculate","ejaculated","ejaculates","ejaculating","ejaculatings","ejaculation","ejakulate","enlargement","erect","erection","erotic","erotism","escort","essohbee","eunuch","extacy","extasy","f u c k","f u c k e r","f.u.c.k","f_u_c_k","f4nny","facefucker","facial","fack","fag","fagbag","fagfucker","fagg","fagged","fagging","faggit","faggitt","faggot","faggotcock","faggots","faggs","fagot","fagots","fags","fagtard","faig","faigt","fanny","fannybandit","fannyflaps","fannyfucker","fanyy","fart","fartknocker","fastfuck","fat","fatass","fatfuck","fatfucker","fcuk","fcuker","fcuking","fecal","feck","fecker","felch","felcher","felching","fellate","fellatio","feltch","feltcher","female squirting","femdom","fenian","figging","fingerbang","fingerfuck","fingerfuck ","fingerfucked","fingerfucker","fingerfucker ","fingerfuckers","fingerfucking","fingerfucks","fingering","fist fuck","fisted","fistfuck","fistfucked","fistfucker","fistfucker ","fistfuckers","fistfucking","fistfuckings","fistfucks","fisting","fisty","flamer","flange","flaps","fleshflute","flog the log","floozy","foad","foah","fondle","foobar","fook","fooker","foot fetish","footfuck","footfucker","footjob","footlicker","foreskin","freakfuck","freakyfucker","freefuck","freex","frigg","frigga","frotting","fubar","fuc","fuck","f-u-c-k","fuck buttons","fuck hole","fuck off","fuck puppet","fuck trophy","fuck yo mama","fuck you","fucka","fuckass","fuck-ass","fuckbag","fuck-bitch","fuckboy","fuckbrain","fuckbutt","fuckbutter","fucked","fuckedup","fucker","fuckers","fuckersucker","fuckface","fuckfreak","fuckhead","fuckheads","fuckher","fuckhole","fuckin","fucking","fuckingbitch","fuckings","fuckingshitmotherfucker","fuckme","fuckme ","fuckmeat","fuckmehard","fuckmonkey","fucknugget","fucknut","fucknutt","fuckoff","fucks","fuckstick","fucktard","fuck-tard","fucktards","fucktart","fucktoy","fucktwat","fuckup","fuckwad","fuckwhit","fuckwhore","fuckwit","fuckwitt","fuckyou","fudge packer","fudgepacker","fudge-packer","fuk","fuker","fukker","fukkers","fukkin","fuks","fukwhit","fukwit","fuq","futanari","fux","fux0r","fvck","fxck","gae","gai","gang bang","gangbang","gang-bang","gangbanged","gangbangs","ganja","gash","gassy ass","gay sex","gayass","gaybob","gaydo","gayfuck","gayfuckist","gaylord","gays","gaysex","gaytard","gaywad","gender bender","genitals","gey","gfy","ghay","ghey","giant cock","gigolo","ginger","gippo","girl on","girl on top","girls gone wild","git","glans","goatcx","goatse","god damn","godamn","godamnit","goddam","god-dam","goddammit","goddamn","goddamned","god-damned","goddamnit","goddamnmuthafucker","godsdamn","gokkun","golden shower","goldenshower","golliwog","gonad","gonads","gonorrehea","goo girl","gooch","goodpoop","gook","gooks","goregasm","gotohell","gringo","grope","group sex","gspot","g-spot","gtfo","guido","guro","h0m0","h0mo","ham flap","hand job","handjob","hard core","hard on","hardcore","hardcoresex","he11","headfuck","hebe","heeb","hemp","hentai","heroin","herp","herpes","herpy","heshe","he-she","hitler","hiv","ho","hoar","hoare","hobag","hoe","hoer","holy shit","hom0","homey","homo","homodumbshit","homoerotic","homoey","honkey","honky","hooch","hookah","hooker","hoor","hootch","hooter","hooters","hore","horniest","horny","hot carl","hot chick","hotpussy","hotsex","how to kill","how to murdep","how to murder","huge fat","hump","humped","humping","hun","hussy","hymen","iap","iberian slap","inbred","incest","injun","intercourse","j3rk0ff","jack off","jackass","jackasses","jackhole","jackoff","jack-off","jaggi","jagoff","jail bait","jailbait","jap","japs","jelly donut","jerk","jerk off","jerk0ff","jerkass","jerked","jerkoff","jerk-off","jigaboo","jiggaboo","jiggerboo","jism","jiz","jizm","jizz","jizzed","jock","juggs","jungle bunny","junglebunny","junkie","junky","kafir","kawk","kike","kikes","kill","kinbaku","kinkster","kinky","kkk","klan","knob","knob end","knobbing","knobead","knobed","knobend","knobhead","knobjocky","knobjokey","kock","kondum","kondums","kooch","kooches","kootch","kraut","kum","kummer","kumming","kums","kunilingus","kunja","kunt","kwif","kyke","l3i+ch","l3itch","labia","lameass","lardass","leather restraint","leather straight jacket","lech","lemon party","leper","lesbian","lesbians","lesbo","lesbos","lez","lezbian","lezbians","lezbo","lezbos","lezza","lezzie","lezzies","lezzy","lmao","lmfao","loin","loins","lolita","looney","lovemaking","lube","lust","lusting","lusty","m0f0","m0fo","m45terbate","ma5terb8","ma5terbate","mafugly","make me come","male squirting","mams","masochist","massa","masterb8","masterbat","masterbat3","masterbate","master-bate","masterbating","masterbation","masterbations","masturbate","masturbating","masturbation","maxi","mcfagget","menage a trois","menses","menstruate","menstruation","meth","m-fucking","mick","middle finger","midget","milf","minge","minger","missionary position","mof0","mofo","mo-fo","molest","mong","moo moo foo foo","moolie","moron","mothafuck","mothafucka","mothafuckas","mothafuckaz","mothafucked","mothafucker","mothafuckers","mothafuckin","mothafucking","mothafuckings","mothafucks","mother fucker","motherfuck","motherfucka","motherfucked","motherfucker","motherfuckers","motherfuckin","motherfucking","motherfuckings","motherfuckka","motherfucks","mound of venus","mr hands","mtherfucker","mthrfucker","mthrfucking","muff","muff diver","muff puff","muffdiver","muffdiving","munging","munter","murder","mutha","muthafecker","muthafuckaz","muthafuckker","muther","mutherfucker","mutherfucking","muthrfucking","n1gga","n1gger","nad","nads","naked","nambla","napalm","nappy","nawashi","nazi","nazism","need the dick","negro","neonazi","nig nog","nigaboo","nigg3r","nigg4h","nigga","niggah","niggas","niggaz","nigger","niggers","niggle","niglet","nig-nog","nimphomania","nimrod","ninny","nipple","nipples","nob","nob jokey","nobhead","nobjocky","nobjokey","nonce","nooky","nsfw images","nude","nudity","numbnuts","nut butter","nut sack","nutsack","nutter","nympho","nymphomania","octopussy","old bag","omg","omorashi","one cup two girls","one guy one jar","opiate","opium","oral","orally","organ","orgasim","orgasims","orgasm","orgasmic","orgasms","orgies","orgy","ovary","ovum","ovums","p.u.s.s.y.","p0rn","paddy","paedophile","paki","panooch","pansy","pantie","panties","panty","pastie","pasty","pawn","pcp","pecker","peckerhead","pedo","pedobear","pedophile","pedophilia","pedophiliac","pee","peepee","pegging","penetrate","penetration","penial","penile","penis","penisbanger","penisfucker","penispuffer","perversion","peyote","phalli","phallic","phone sex","phonesex","phuck","phuk","phuked","phuking","phukked","phukking","phuks","phuq","piece of shit","pigfucker","pikey","pillowbiter","pimp","pimpis","pinko","piss","piss off","piss pig","pissed","pissed off","pisser","pissers","pisses","pissflaps","pissin","pissing","pissoff","piss-off","pisspig","playboy","pleasure chest","pms","polack","pole smoker","polesmoker","pollock","ponyplay","poof","poon","poonani","poonany","poontang","poop","poop chute","poopchute","poopuncher","porch monkey","porchmonkey","porn","porno","pornography","pornos","pot","potty","prick","pricks","prickteaser","prig","prince albert piercing","prod","pron","prostitute","prude","psycho","pthc","pube","pubes","pubic","pubis","punani","punanny","punany","punkass","punky","punta","puss","pusse","pussi","pussies","pussy","pussy fart","pussy palace","pussylicking","pussypounder","pussys","pust","puto","queaf","queef","queer","queerbait","queerhole","queero","queers","quicky","quim","racy","raghead","raging boner","rape","raped","raper","rapey","raping","rapist","raunch","rectal","rectum","rectus","reefer","reetard","reich","renob","retard","retarded","reverse cowgirl","revue","rimjaw","rimjob","rimming","ritard","rosy palm","rosy palm and her 5 sisters","rtard","r-tard","rubbish","rum","rump","rumprammer","ruski","rusty trombone","s hit","s&m","s.h.i.t.","s.o.b.","s_h_i_t","s0b","sadism","sadist","sambo","sand nigger","sandbar","sandler","sandnigger","sanger","santorum","sausage queen","scag","scantily","scat","schizo","schlong","scissoring","screw","screwed","screwing","scroat","scrog","scrot","scrote","scrotum","scrud","scum","seaman","seamen","seduce","seks","semen","sex","sexo","sexual","sexy","sh!+","sh!t","sh1t","s-h-1-t","shag","shagger","shaggin","shagging","shamedame","shaved beaver","shaved pussy","shemale","shi+","shibari","shirt lifter","shit","s-h-i-t","shit ass","shit fucker","shitass","shitbag","shitbagger","shitblimp","shitbrains","shitbreath","shitcanned","shitcunt","shitdick","shite","shiteater","shited","shitey","shitface","shitfaced","shitfuck","shitfull","shithead","shitheads","shithole","shithouse","shiting","shitings","shits","shitspitter","shitstain","shitt","shitted","shitter","shitters","shittier","shittiest","shitting","shittings","shitty","shiz","shiznit","shota","shrimping","sissy","skag","skank","skeet","skullfuck","slag","slanteye","slave","sleaze","sleazy","slope","slut","slut bucket","slutbag","slutdumper","slutkiss","sluts","smartass","smartasses","smeg","smegma","smut","smutty","snatch","sniper","snowballing","snuff","s-o-b","sod off","sodom","sodomize","sodomy","son of a bitch","son of a motherless goat","son of a whore","son-of-a-bitch","souse","soused","spac","spade","sperm","spic","spick","spik","spiks","splooge","splooge moose","spooge","spook","spread legs","spunk","steamy","stfu","stiffy","stoned","strap on","strapon","strappado","strip","strip club","stroke","stupid","style doggy","suck","suckass","sucked","sucking","sucks","suicide girls","sultry women","sumofabiatch","swastika","swinger","t1t","t1tt1e5","t1tties","taff","taig","tainted love","taking the piss","tampon","tard","tart","taste my","tawdry","tea bagging","teabagging","teat","teets","teez","terd","teste","testee","testes","testical","testicle","testis","threesome","throating","thrust","thug","thundercunt","tied up","tight white","tinkle","tit","tit wank","titfuck","titi","tities","tits","titt","tittie5","tittiefucker","titties","titty","tittyfuck","tittyfucker","tittywank","titwank","toke","tongue in a","toots","topless","tosser","towelhead","tramp","tranny","transsexual","trashy","tribadism","trumped","tub girl","tubgirl","turd","tush","tushy","tw4t","twat","twathead","twatlips","twats","twatty","twatwaffle","twink","twinkie","two fingers","two fingers with tongue","two girls one cup","twunt","twunter","ugly","unclefucker","undies","undressing","unwed","upskirt","urethra play","urinal","urine","urophilia","uterus","uzi","v14gra","v1gra","vag","vagina","vajayjay","va-j-j","valium","venus mound","veqtable","viagra","vibrator","violet wand","virgin","vixen","vjayjay","vodka","vomit","vorarephilia","voyeur","vulgar","vulva","w00se","wad","wang","wank","wanker","wankjob","wanky","wazoo","wedgie","weed","weenie","weewee","weiner","weirdo","wench","wet dream","wetback","wh0re","wh0reface","white power","whitey","whiz","whoar","whoralicious","whore","whorealicious","whorebag","whored","whoreface","whorehopper","whorehouse","whores","whoring","wigger","willies","willy","window licker","wiseass","wiseasses","wog","womb","woody","wop","wrapping men","wrinkled starfish","wtf","xrated","x-rated","xx","xxx","yaoi","yeasty","yellow showers","yid","yiffy","yobbo","zoophile","zoophilia2 girls 1 cup","2g1c","4r5e","5h1t","5hit","a$$","a$$hole","a_s_s","a2m","a54","a55","a55hole","aeolus","ahole","alabama hot pocket","alaskan pipeline","anal","anal impaler","anal leakage","analannie","analprobe","analsex","anilingus","anus","apeshit","ar5e","areola","areole","arian","arrse","arse","arsehole","aryan","ass","ass fuck","ass hole","assault","assbag","assbagger","assbandit","assbang","assbanged","assbanger","assbangs","assbite","assblaster","assclown","asscock","asscracker","asses","assface","assfaces","assfuck","assfucker","ass-fucker","assfukka","assgoblin","assh0le","asshat","ass-hat","asshead","assho1e","asshole","assholes","asshopper","asshore","ass-jabber","assjacker","assjockey","asskiss","asskisser","assklown","asslick","asslicker","asslover","assman","assmaster","assmonkey","assmucus","assmunch","assmuncher","assnigger","asspacker","asspirate","ass-pirate","asspuppies","assranger","assshit","assshole","asssucker","asswad","asswhole","asswhore","asswipe","asswipes","auto erotic","autoerotic","axwound","azazel","azz","b!tch","b00bs","b17ch","b1tch","babe","babeland","babes","baby batter","baby juice","badfuck","ball gag","ball gravy","ball kicking","ball licking","ball sack","ball sucking","ballbag","balllicker","balls","ballsack","bampot","bang","bang (one's) box","bangbros","banger","banging","bareback","barely legal","barenaked","barf","barface","barfface","bastard","bastardo","bastards","bastinado","batty boy","bawdy","bazongas","bazooms","bbw","bdsm","beaner","beaners","beardedclam","beastial","beastiality","beatch","beater","beatyourmeat","beaver","beaver cleaver","beaver lips","beef curtain","beef curtains","beer","beeyotch","bellend","bender","beotch","bestial","bestiality","bi+ch","biatch","bicurious","big black","big breasts","big knockers","big tits","bigbastard","bigbutt","bigger","bigtits","bimbo","bimbos","bint","birdlock","bisexual","bi-sexual","bitch","bitch tit","bitchass","bitched","bitcher","bitchers","bitches","bitchez","bitchin","bitching","bitchtits","bitchy","black cock","blonde action","blonde on blonde action","bloodclaat","bloody","bloody hell","blow","blow job","blow me","blow mud","blow your load","blowjob","blowjobs","blue waffle","blumpkin","boang","bod","bodily","bogan","bohunk","boink","boiolas","bollick","bollock","bollocks","bollok","bollox","bomd","bondage","bone","boned","boner","boners","bong","boob","boobies","boobs","booby","booger","bookie","boong","boonga","booobs","boooobs","booooobs","booooooobs","bootee","bootie","booty","booty call","booze","boozer","boozy","bosom","bosomy","bowel","bowels","bra","brassiere","breast","breastjob","breastlover","breastman","breasts","breeder","brotherfucker","brown showers","brunette action","buceta","bugger","buggered","buggery","bukkake","bull shit","bullcrap","bulldike","bulldyke","bullet vibe","bullshit","bullshits","bullshitted","bullturds","bum","bum boy","bumblefuck","bumclat","bumfuck","bummer","bung","bung hole","bunga","bunghole","bunny fucker","bust a load","busty","butchdike","butchdyke","butt","butt fuck","butt plug","buttbang","butt-bang","buttcheeks","buttface","buttfuck","butt-fuck","buttfucka","buttfucker","butt-fucker","butthead","butthole","buttman","buttmuch","buttmunch","buttmuncher","butt-pirate","buttplug","c.0.c.k","c.o.c.k.","c.u.n.t","c0ck","c-0-c-k","c0cksucker","caca","cahone","camel toe","cameltoe","camgirl","camslut","camwhore","carpet muncher","carpetmuncher","cawk","cervix","chesticle","chi-chi man","chick with a dick","child-fucker","chin","chinc","chincs","chink","chinky","choad","choade","choc ice","chocolate rosebuds","chode","chodes","chota bags","cipa","circlejerk","cl1t","cleveland steamer","climax","clit","clit licker","clitface","clitfuck","clitoris","clitorus","clits","clitty","clitty litter","clogwog","clover clamps","clunge","clusterfuck","cnut","cocain","cocaine","cock","c-o-c-k","cock pocket","cock snot","cock sucker","cockass","cockbite","cockblock","cockburger","cockeye","cockface","cockfucker","cockhead","cockholster","cockjockey","cockknocker","cockknoker","cocklicker","cocklover","cocklump","cockmaster","cockmongler","cockmongruel","cockmonkey","cockmunch","cockmuncher","cocknose","cocknugget","cocks","cockshit","cocksmith","cocksmoke","cocksmoker","cocksniffer","cocksucer","cocksuck","cocksuck ","cocksucked","cocksucker","cock-sucker","cocksuckers","cocksucking","cocksucks","cocksuka","cocksukka","cockwaffle","coffin dodger","coital","cok","cokmuncher","coksucka","commie","condom","coochie","coochy","coon","coonnass","coons","cooter","cop some wood","coprolagnia","coprophilia","corksucker","cornhole","corp whore","cox","crabs","crack","cracker","crackwhore","crack-whore","crap","crappy","creampie","cretin","crikey","cripple","crotte","cum","cum chugger","cum dumpster","cum freak","cum guzzler","cumbubble","cumdump","cumdumpster","cumguzzler","cumjockey","cummer","cummin","cumming","cums","cumshot","cumshots","cumslut","cumstain","cumtart","cunilingus","cunillingus","cunn","cunnie","cunnilingus","cunntt","cunny","cunt","c-u-n-t","cunt hair","cuntass","cuntbag","cuntface","cuntfuck","cuntfucker","cunthole","cunthunter","cuntlick","cuntlick ","cuntlicker","cuntlicker ","cuntlicking","cuntrag","cunts","cuntsicle","cuntslut","cunt-struck","cuntsucker","cut rope","cyalis","cyberfuc","cyberfuck","cyberfucked","cyberfucker","cyberfuckers","cyberfucking","cybersex","d0ng","d0uch3","d0uche","d1ck","d1ld0","d1ldo","dago","dagos","dammit","damn","damned","damnit","darkie","darn","date rape","daterape","dawgie-style","deep throat","deepthroat","deggo","dendrophilia","dick","dick head","dick hole","dick shy","dickbag","dickbeaters","dickbrain","dickdipper","dickface","dickflipper","dickfuck","dickfucker","dickhead","dickheads","dickhole","dickish","dick-ish","dickjuice","dickmilk","dickmonger","dickripper","dicks","dicksipper","dickslap","dick-sneeze","dicksucker","dicksucking","dicktickler","dickwad","dickweasel","dickweed","dickwhipper","dickwod","dickzipper","diddle","dike","dildo","dildos","diligaf","dillweed","dimwit","dingle","dingleberries","dingleberry","dink","dinks","dipship","dipshit","dirsa","dirty","dirty pillows","dirty sanchez","dlck","dog style","dog-fucker","doggie style","doggiestyle","doggie-style","doggin","dogging","doggy style","doggystyle","doggy-style","dolcett","domination","dominatrix","dommes","dong","donkey punch","donkeypunch","donkeyribber","doochbag","doofus","dookie","doosh","dopey","double dong","double penetration","doublelift","douch3","douche","douchebag","douchebags","douche-fag","douchewaffle","douchey","dp action","drunk","dry hump","duche","dumass","dumb ass","dumbass","dumbasses","dumbcunt","dumbfuck","dumbshit","dummy","dumshit","dvda","dyke","dykes","eat a dick","eat hair pie","eat my ass","eatpussy","ecchi","ejaculate","ejaculated","ejaculates","ejaculating","ejaculatings","ejaculation","ejakulate","enlargement","erect","erection","erotic","erotism","escort","essohbee","eunuch","extacy","extasy","f u c k","f u c k e r","f.u.c.k","f_u_c_k","f4nny","facefucker","facial","fack","fag","fagbag","fagfucker","fagg","fagged","fagging","faggit","faggitt","faggot","faggotcock","faggots","faggs","fagot","fagots","fags","fagtard","faig","faigt","fanny","fannybandit","fannyflaps","fannyfucker","fanyy","fart","fartknocker","fastfuck","fat","fatass","fatfuck","fatfucker","fcuk","fcuker","fcuking","fecal","feck","fecker","felch","felcher","felching","fellate","fellatio","feltch","feltcher","female squirting","femdom","fenian","figging","fingerbang","fingerfuck","fingerfuck ","fingerfucked","fingerfucker","fingerfucker ","fingerfuckers","fingerfucking","fingerfucks","fingering","fist fuck","fisted","fistfuck","fistfucked","fistfucker","fistfucker ","fistfuckers","fistfucking","fistfuckings","fistfucks","fisting","fisty","flamer","flange","flaps","fleshflute","flog the log","floozy","foad","foah","fondle","foobar","fook","fooker","foot fetish","footfuck","footfucker","footjob","footlicker","foreskin","freakfuck","freakyfucker","freefuck","freex","frigg","frigga","frotting","fubar","fuc","fuck","f-u-c-k","fuck buttons","fuck hole","fuck off","fuck puppet","fuck trophy","fuck yo mama","fuck you","fucka","fuckass","fuck-ass","fuckbag","fuck-bitch","fuckboy","fuckbrain","fuckbutt","fuckbutter","fucked","fuckedup","fucker","fuckers","fuckersucker","fuckface","fuckfreak","fuckhead","fuckheads","fuckher","fuckhole","fuckin","fucking","fuckingbitch","fuckings","fuckingshitmotherfucker","fuckme","fuckme ","fuckmeat","fuckmehard","fuckmonkey","fucknugget","fucknut","fucknutt","fuckoff","fucks","fuckstick","fucktard","fuck-tard","fucktards","fucktart","fucktoy","fucktwat","fuckup","fuckwad","fuckwhit","fuckwhore","fuckwit","fuckwitt","fuckyou","fudge packer","fudgepacker","fudge-packer","fuk","fuker","fukker","fukkers","fukkin","fuks","fukwhit","fukwit","fuq","futanari","fux","fux0r","fvck","fxck","gae","gai","gang bang","gangbang","gang-bang","gangbanged","gangbangs","ganja","gash","gassy ass","gay sex","gayass","gaybob","gaydo","gayfuck","gayfuckist","gaylord","gays","gaysex","gaytard","gaywad","gender bender","genitals","gey","gfy","ghay","ghey","giant cock","gigolo","ginger","gippo","girl on","girl on top","girls gone wild","git","glans","goatcx","goatse","god damn","godamn","godamnit","goddam","god-dam","goddammit","goddamn","goddamned","god-damned","goddamnit","goddamnmuthafucker","godsdamn","gokkun","golden shower","goldenshower","golliwog","gonad","gonads","gonorrehea","goo girl","gooch","goodpoop","gook","gooks","goregasm","gotohell","gringo","grope","group sex","gspot","g-spot","gtfo","guido","guro","h0m0","h0mo","ham flap","hand job","handjob","hard core","hard on","hardcore","hardcoresex","he11","headfuck","hebe","heeb","hemp","hentai","heroin","herp","herpes","herpy","heshe","he-she","hitler","hiv","ho","hoar","hoare","hobag","hoe","hoer","holy shit","hom0","homey","homo","homodumbshit","homoerotic","homoey","honkey","honky","hooch","hookah","hooker","hoor","hootch","hooter","hooters","hore","horniest","horny","hot carl","hot chick","hotpussy","hotsex","how to kill","how to murdep","how to murder","huge fat","hump","humped","humping","hun","hussy","hymen","iap","iberian slap","inbred","incest","injun","intercourse","j3rk0ff","jack off","jackass","jackasses","jackhole","jackoff","jack-off","jaggi","jagoff","jail bait","jailbait","jap","japs","jelly donut","jerk","jerk off","jerk0ff","jerkass","jerked","jerkoff","jerk-off","jigaboo","jiggaboo","jiggerboo","jism","jiz","jizm","jizz","jizzed","jock","juggs","jungle bunny","junglebunny","junkie","junky","kafir","kawk","kike","kikes","kill","kinbaku","kinkster","kinky","kkk","klan","knob","knob end","knobbing","knobead","knobed","knobend","knobhead","knobjocky","knobjokey","kock","kondum","kondums","kooch","kooches","kootch","kraut","kum","kummer","kumming","kums","kunilingus","kunja","kunt","kwif","kyke","l3i+ch","l3itch","labia","lameass","lardass","leather restraint","leather straight jacket","lech","lemon party","leper","lesbian","lesbians","lesbo","lesbos","lez","lezbian","lezbians","lezbo","lezbos","lezza","lezzie","lezzies","lezzy","lmao","lmfao","loin","loins","lolita","looney","lovemaking","lube","lust","lusting","lusty","m0f0","m0fo","m45terbate","ma5terb8","ma5terbate","mafugly","make me come","male squirting","mams","masochist","massa","masterb8","masterbat","masterbat3","masterbate","master-bate","masterbating","masterbation","masterbations","masturbate","masturbating","masturbation","maxi","mcfagget","menage a trois","menses","menstruate","menstruation","meth","m-fucking","mick","middle finger","midget","milf","minge","minger","missionary position","mof0","mofo","mo-fo","molest","mong","moo moo foo foo","moolie","moron","mothafuck","mothafucka","mothafuckas","mothafuckaz","mothafucked","mothafucker","mothafuckers","mothafuckin","mothafucking","mothafuckings","mothafucks","mother fucker","motherfuck","motherfucka","motherfucked","motherfucker","motherfuckers","motherfuckin","motherfucking","motherfuckings","motherfuckka","motherfucks","mound of venus","mr hands","mtherfucker","mthrfucker","mthrfucking","muff","muff diver","muff puff","muffdiver","muffdiving","munging","munter","murder","mutha","muthafecker","muthafuckaz","muthafuckker","muther","mutherfucker","mutherfucking","muthrfucking","n1gga","n1gger","nad","nads","naked","nambla","napalm","nappy","nawashi","nazi","nazism","need the dick","negro","neonazi","nig nog","nigaboo","nigg3r","nigg4h","nigga","niggah","niggas","niggaz","nigger","niggers","niggle","niglet","nig-nog","nimphomania","nimrod","ninny","nipple","nipples","nob","nob jokey","nobhead","nobjocky","nobjokey","nonce","nooky","nsfw images","nude","nudity","numbnuts","nut butter","nut sack","nutsack","nutter","nympho","nymphomania","octopussy","old bag","omg","omorashi","one cup two girls","one guy one jar","opiate","opium","oral","orally","organ","orgasim","orgasims","orgasm","orgasmic","orgasms","orgies","orgy","ovary","ovum","ovums","p.u.s.s.y.","p0rn","paddy","paedophile","paki","panooch","pansy","pantie","panties","panty","pastie","pasty","pawn","pcp","pecker","peckerhead","pedo","pedobear","pedophile","pedophilia","pedophiliac","pee","peepee","pegging","penetrate","penetration","penial","penile","penis","penisbanger","penisfucker","penispuffer","perversion","peyote","phalli","phallic","phone sex","phonesex","phuck","phuk","phuked","phuking","phukked","phukking","phuks","phuq","piece of shit","pigfucker","pikey","pillowbiter","pimp","pimpis","pinko","piss","piss off","piss pig","pissed","pissed off","pisser","pissers","pisses","pissflaps","pissin","pissing","pissoff","piss-off","pisspig","playboy","pleasure chest","pms","polack","pole smoker","polesmoker","pollock","ponyplay","poof","poon","poonani","poonany","poontang","poop","poop chute","poopchute","poopuncher","porch monkey","porchmonkey","porn","porno","pornography","pornos","pot","potty","prick","pricks","prickteaser","prig","prince albert piercing","prod","pron","prostitute","prude","psycho","pthc","pube","pubes","pubic","pubis","punani","punanny","punany","punkass","punky","punta","puss","pusse","pussi","pussies","pussy","pussy fart","pussy palace","pussylicking","pussypounder","pussys","pust","puto","queaf","queef","queer","queerbait","queerhole","queero","queers","quicky","quim","racy","raghead","raging boner","rape","raped","raper","rapey","raping","rapist","raunch","rectal","rectum","rectus","reefer","reetard","reich","renob","retard","retarded","reverse cowgirl","revue","rimjaw","rimjob","rimming","ritard","rosy palm","rosy palm and her 5 sisters","rtard","r-tard","rubbish","rum","rump","rumprammer","ruski","rusty trombone","s hit","s&m","s.h.i.t.","s.o.b.","s_h_i_t","s0b","sadism","sadist","sambo","sand nigger","sandbar","sandler","sandnigger","sanger","santorum","sausage queen","scag","scantily","scat","schizo","schlong","scissoring","screw","screwed","screwing","scroat","scrog","scrot","scrote","scrotum","scrud","scum","seaman","seamen","seduce","seks","semen","sex","sexo","sexual","sexy","sh!+","sh!t","sh1t","s-h-1-t","shag","shagger","shaggin","shagging","shamedame","shaved beaver","shaved pussy","shemale","shi+","shibari","shirt lifter","shit","s-h-i-t","shit ass","shit fucker","shitass","shitbag","shitbagger","shitblimp","shitbrains","shitbreath","shitcanned","shitcunt","shitdick","shite","shiteater","shited","shitey","shitface","shitfaced","shitfuck","shitfull","shithead","shitheads","shithole","shithouse","shiting","shitings","shits","shitspitter","shitstain","shitt","shitted","shitter","shitters","shittier","shittiest","shitting","shittings","shitty","shiz","shiznit","shota","shrimping","sissy","skag","skank","skeet","skullfuck","slag","slanteye","slave","sleaze","sleazy","slope","slut","slut bucket","slutbag","slutdumper","slutkiss","sluts","smartass","smartasses","smeg","smegma","smut","smutty","snatch","sniper","snowballing","snuff","s-o-b","sod off","sodom","sodomize","sodomy","son of a bitch","son of a motherless goat","son of a whore","son-of-a-bitch","souse","soused","spac","spade","sperm","spic","spick","spik","spiks","splooge","splooge moose","spooge","spook","spread legs","spunk","steamy","stfu","stiffy","stoned","strap on","strapon","strappado","strip","strip club","stroke","stupid","style doggy","suck","suckass","sucked","sucking","sucks","suicide girls","sultry women","sumofabiatch","swastika","swinger","t1t","t1tt1e5","t1tties","taff","taig","tainted love","taking the piss","tampon","tard","tart","taste my","tawdry","tea bagging","teabagging","teat","teets","teez","terd","teste","testee","testes","testical","testicle","testis","threesome","throating","thrust","thug","thundercunt","tied up","tight white","tinkle","tit","tit wank","titfuck","titi","tities","tits","titt","tittie5","tittiefucker","titties","titty","tittyfuck","tittyfucker","tittywank","titwank","toke","tongue in a","toots","topless","tosser","towelhead","tramp","tranny","transsexual","trashy","tribadism","trumped","tub girl","tubgirl","turd","tush","tushy","tw4t","twat","twathead","twatlips","twats","twatty","twatwaffle","twink","twinkie","two fingers","two fingers with tongue","two girls one cup","twunt","twunter","ugly","unclefucker","undies","undressing","unwed","upskirt","urethra play","urinal","urine","urophilia","uterus","uzi","v14gra","v1gra","vag","vagina","vajayjay","va-j-j","valium","venus mound","veqtable","viagra","vibrator","violet wand","virgin","vixen","vjayjay","vodka","vomit","vorarephilia","voyeur","vulgar","vulva","w00se","wad","wang","wank","wanker","wankjob","wanky","wazoo","wedgie","weed","weenie","weewee","weiner","weirdo","wench","wet dream","wetback","wh0re","wh0reface","white power","whitey","whiz","whoar","whoralicious","whore","whorealicious","whorebag","whored","whoreface","whorehopper","whorehouse","whores","whoring","wigger","willies","willy","window licker","wiseass","wiseasses","wog","womb","woody","wop","wrapping men","wrinkled starfish","wtf","xrated","x-rated","xx","xxx","yaoi","yeasty","yellow showers","yid","yiffy","yobbo","zoophile","zoophilia","zubb"]
        
        for i in tmpList:
            if i.lower() in profanity_list:
                return True
        return False
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
