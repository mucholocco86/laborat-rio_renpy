label header_ep12_label:
$ currentEpisode = 12
$ vault_unlocked = False
$ safe_digits = [0,0,0,0]
$ randInt = renpy.random.randint(0, 17)

$ pp_seed = renpy.random.randint(0,4)
$ sm_experiment = 3
$ badik_chapter = "3"
if persistent.seen_cutscene_ep12 == None:
    $ persistent.seen_cutscene_ep12 = [False,False,False]


if mphone_contact_list[2][0] == "Chad":
    $ tmp_list = []
    $ tmp_list.extend(mphone_contact_list[2])
    $ mphone_contact_list[2] = mphone_contact_list[1]
    $ mphone_contact_list[1] = tmp_list

    $ tmp_list = []
    $ tmp_list.extend(mphone_chat_history_list[2])
    $ mphone_chat_history_list[2] = mphone_chat_history_list[1]
    $ mphone_chat_history_list[1] = tmp_list

default roosterNickMia = "Mia@_Meow"
$ rooster_nick_list.append(["Mia","Mia@_Meow"])

default roosterNickErin = "Erin@ER_IN"
$ rooster_nick_list.append(["Erin","Erin@ER_IN"])
default roosterNickFelicia = "Felicia@Felixia"
$ rooster_nick_list.append(["Felicia","Felicia@Felixia"])
default roosterNickMarc = "Marc@Marcmarcmarc"
$ rooster_nick_list.append(["Marc","Marc@Marcmarcmarc"])
default roosterNickTheDiane = "TheDiane@TheDiane"
$ rooster_nick_list.append(["TheDiane","TheDiane@TheDiane"])
default roosterNickSlop = "SLOP@SLOP"
$ rooster_nick_list.append(["SLOP","SLOP@SLOP"])
default roosterNickNikita = "Nikita@Niki"
$ rooster_nick_list.append(["Nikita","Nikita@Niki"])
default roosterNickTim = "Tim@TimTheTeacher"
$ rooster_nick_list.append(["Tim","Tim@TimTheTeacher"])

$ fixChatLists()
$ mphone_stats_generate_girls()
if in_bios("I helped Bianca with her Dirty Bowl mission. But the mission didn't matter; we wanted to do that regardless."):
    $ ep11_bianca_path = True
if in_bios("I helped Sally with her Dirty Bowl mission, and we made out on Leon's bed."):
    $ ep11_sally_kiss = True
else:
    $ ep11_sally_kiss = False
default red_int = 0
default ep12_bianca_lewd = False
default tmp_list = []
default breakup = []
default temp_list = []
default ep12_cathy_lewd = False
default pb_derek_completed = False
default ep12_elena_lewd = False
default bn_story_fight = False
default ep12_maya_hurt = False
default ep12_josy_hurt = False
default ep12_eh_fight = False
default bn_story_fight_round = 0
default ep12_rusty_over_dwyane = False
default ep12_nikita = False
default ep12_mc_slut = False
default ep12_ts_lewd = False
default ep12_zoey_friend = False
default maya_shiny_dress = False
default ep12_nicole_ditch = False
default ep12_sally_lewd = False
default ep12_josy_defend_count = 0
default ep12_nora_state = 0
default ep12_zworries = 0
default ep12_drinking_list = []
default ep12_girl_count = 0
default ep12_rolling = False
default ep12_chen_marc_toilet = False
default ep12_mean_prank = False
default ep12_offered_room = ""
default branchZoey = False
default ep12_forgave_nick = False
default ep12_break_or_tell = ""
default ep12_riona_side = ""
default ep12_midnight_kiss = ""
if ep11_zoey_kiss == 2:
    $ branchZoey = True
default roadJill = False
default roadIsabella = False
default roadSage = False
default roadZoey = False
if branchZoey:
    $ roadZoey = True
default roadAlone = False
if branchAlone and not roadZoey:
    $ roadAlone = True
default roadJosy = False
default roadMaya = False
default roadMayaJosy = False
default roadQuinn = False
default ep12_quinn_ditch = False
default ep12_dj_counter = 0
default ep12_dj_return = False
default ep12_dj_interrupted = 0
default ep12_brawler_round_win = 0
default ep12_brawler_comp_won = False
default ep12_jsolo = False
default ep12_class_performance = 0
default ep12_pp_food = 2
default ep12_pp_game = 1
default ep12_pp_fireworks = 2
default ep12_card_game_won = False
default ep12_diane_pics = False
default cg_questions_list = []
default cg_cpu_answers_list = []
default cg_card_list = []
default cg_cards_on_hand = []
default cg_cpu_selected_cards = []
default cg_scores = [0,0,0,0]
default cg_question_idx = 0
default cg_read_idx = 0
default cg_leader = []
default cg_discard_count = 3
default cg_winner = ""
default cg_mc_card_draw_idx = 5
default cg_mc_selected_card = -1
default cg_current_winner = -1
default cg_winning_string = ""
default cg_tmp_str = ""
default cg_answers_and_reactions = []
default cg_questions_asked = []
default cg_reader = -1
default cg_current_question = -1
define cg_derek_vb_responses = ["Oof. That's bad.","Huh? I don't get it.","Whoever played this one probably didn't have any good cards.","Sheesh.","Hmm. That's a thinker.","Nope. I don't get that one."]
define cg_derek_b_responses = ["Not the best. Not the worst.","Meh.","That's not my kind of humor.","Is this supposed to be funny?","A swing and a miss."]
define cg_derek_f_responses = ["Haha!","Haha! Good one.","Hehe!","What the fuck? Haha.","Haha! This game is fun.","Haha! Not bad!"]
define cg_derek_vf_responses = ["Hahaha!","HAHA! Fuck, that's funny!","HAHAHA! Love it!","HAHA! I love this one.","Haha! What the fuck!?","HAHA! Yep! That's my humor for sure."]
define cg_maya_vb_responses = ["No... Just... No.","What? Why would you play this?","Know your audience, people.","Well, that's not funny at all.","Huh? Why would you play that?"]
define cg_maya_b_responses = ["Nope, that doesn't make me laugh.","I'm sorry, but I don't get it.","Ok...","Yeah. Not funny.","Nice try."]
define cg_maya_f_responses = ["Haha!","Haha! I like it!","That's funny! Haha!","Haha... I feel bad for laughing at some of these.", "I enjoyed that one."]
define cg_maya_vf_responses = ["Hahaha!","Haha! That fits so well!","HAHA! I love that one.","That's so funny! Haha!"]
define cg_sage_vb_responses = ["Huh? No.","Nope. This one won't win this round.","Not funny at all.","What?"]
define cg_sage_b_responses = ["This one's not that good.","Sometimes weird things make you laugh, but this one doesn't.","Almost, but not really.","A decent attempt, but it won't make me laugh."]
define cg_sage_f_responses = ["Haha!","Hah! That's kinda funny.","Yes! Haha!","This game is so stupid. Haha!","Kinda clever."]
define cg_sage_vf_responses = ["Hahaha!","BAHAHA!","HAHA!!!","That's hilarious! HAHA!"]
define cg_mc_f_responses = ["Haha!","That's funny!","HAHA! I love it.","Now that's a fun one."]
define cg_mc_b_responses = ["Nah...","Huh?","Meh.","That doesn't make me laugh.","I don't get it."]
default mps3_slot_hover = -1
default mps3_slot = -1
default mps3slotname = ""
default transfer_note = ""
default ep12_nicole_dating = 0
default ep12_full_service = False
default ep12_nicole_path = False
default ep12_nicole_breakup = False
if ep10_date_nicole and not ep10_cancel_date_nicole:
    if ep10_rolling and (ep11_nicole_over_lily or ep11_rolling):
        $ ep12_nicole_path = True
    elif not ep10_rolling:
        $ ep12_nicole_path = True
default roosterNickChen = "Chen@BigChen"
$ rooster_nick_list.append(["Chen","Chen@BigChen"])
default roosterNickLeanne = "Leanne@LeanneW"
$ rooster_nick_list.append(["Leanne","Leanne@LeanneW"])
default ep12_hotties_club = False
default ep12_jill_love = False
default ep12_bella_love = False
default ep12_jill_anal = False
default ep12_both_love = False
default ep12_jewels = ["START"]

default bios_txt_nikita = "Nikita. She's in my Chemistry class and I've seen her at our parties. There's something about her that makes me interested."
default mbios_history_nikita = []
default bios_txt_marc = "Marc seems like a nice guy. He's a close friend to Chen, and he likes to come to our parties. He seems like the silent type and also comes off as a bit dumb."
default mbios_history_marc = []
default bios_txt_chen = "Chen is a guy an opinionated guy with attitude. I don't think that makes him a bad guy, but he sure is energetic and such people can be a handful to deal with."
default mbios_history_chen = []
default ep12_accepted_jen = False
jump previousEp12Label

# Decompiled by unrpyc {v1.3.2}: https://github.com/CensoredUsername/unrpyc dev-branch
