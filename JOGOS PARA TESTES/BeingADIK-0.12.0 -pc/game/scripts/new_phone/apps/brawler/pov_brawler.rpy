screen pov_health_screen:
    tag pov_health_screen
    imagebutton:
        idle Transform("pov_jock_healthbar_[sports_rounded_cpu_hp]")
        hover Transform("pov_jock_healthbar_[sports_rounded_cpu_hp]")
        action NullAction()
        xpos 1334 * persistent.scale_factor
        ypos 0
    imagebutton:
        idle Transform("pov_mc_healthbar_[sports_rounded_player_hp]")
        hover Transform("pov_mc_healthbar_[sports_rounded_player_hp]")
        action NullAction()
        xpos 0
        ypos 0
    text "{size=-%d}{color=[cpu_color]}[cpu_name]{/color}{/size}" % (3 * persistent.scale_factor) xpos 0.77 ypos 0.022
    text "{size=-%d}{color=#ffffff}You{/color}{/size}" % (3 * persistent.scale_factor) xpos 0.195 ypos 0.022

screen pov_select_screen:
    tag pov_select_screen
    modal True
    timer pov_select_timer action [Hide('text'), Hide('pov_select_screen'), SetVariable("fightSelectDigit", 4),Jump("pov_select_label")]
    key "K_UP" action (Hide('text'),Hide('pov_select_screen'),SetVariable("fightSelectDigit", 0), Jump("pov_select_label"))
    key "K_RIGHT" action (Hide('text'),Hide('pov_select_screen'),SetVariable("fightSelectDigit", 1), Jump("pov_select_label"))
    key "K_DOWN" action (Hide('text'),Hide('pov_select_screen'),SetVariable("fightSelectDigit", 2), Jump("pov_select_label"))
    key "K_LEFT" action (Hide('text'),Hide('pov_select_screen'),SetVariable("fightSelectDigit", 3), Jump("pov_select_label"))
    key "w" action (Hide('text'),Hide('pov_select_screen'),SetVariable("fightSelectDigit", 0), Jump("pov_select_label"))
    key "d" action (Hide('text'),Hide('pov_select_screen'),SetVariable("fightSelectDigit", 1), Jump("pov_select_label"))
    key "s" action (Hide('text'),Hide('pov_select_screen'),SetVariable("fightSelectDigit", 2), Jump("pov_select_label"))
    key "a" action (Hide('text'),Hide('pov_select_screen'),SetVariable("fightSelectDigit", 3), Jump("pov_select_label"))

label pov_select_label:
$ renpy.block_rollback()
if fightSelectDigit == 4:
    $ pov_attack_multiplier = 0
    jump pov_mc_missed_label
else:
    if pov_attack_multiplier_array[fightSelectDigit] == -1:
        $ pov_mc_healed = True
        jump pov_mc_healed_label
    $ pov_attack_multiplier = pov_attack_multiplier_array[fightSelectDigit]
    if pov_attack_multiplier == 12:
        $ roundHouseCoolDown = 2
    if pov_attack_multiplier == 0:
        jump pov_mc_missed_label
jump pov_mc_attack_label

screen pov_select_screen_faux:
    tag pov_select_screen
    modal True
    timer pov_select_timer action [Hide('text'), Hide('pov_select_screen'), SetVariable("fightSelectDigit", 4),Jump("pov_select_label_faux")]
    key "K_UP" action (Hide('text'),Hide('pov_select_screen'),SetVariable("fightSelectDigit", 0), Jump("pov_select_label_faux"))
    key "K_RIGHT" action (Hide('text'),Hide('pov_select_screen'),SetVariable("fightSelectDigit", 1), Jump("pov_select_label_faux"))
    key "K_DOWN" action (Hide('text'),Hide('pov_select_screen'),SetVariable("fightSelectDigit", 2), Jump("pov_select_label_faux"))
    key "K_LEFT" action (Hide('text'),Hide('pov_select_screen'),SetVariable("fightSelectDigit", 3), Jump("pov_select_label_faux"))
    key "w" action (Hide('text'),Hide('pov_select_screen'),SetVariable("fightSelectDigit", 0), Jump("pov_select_label_faux"))
    key "d" action (Hide('text'),Hide('pov_select_screen'),SetVariable("fightSelectDigit", 1), Jump("pov_select_label_faux"))
    key "s" action (Hide('text'),Hide('pov_select_screen'),SetVariable("fightSelectDigit", 2), Jump("pov_select_label_faux"))
    key "a" action (Hide('text'),Hide('pov_select_screen'),SetVariable("fightSelectDigit", 3), Jump("pov_select_label_faux"))

label pov_select_label_faux:
$ renpy.block_rollback()
if fightSelectDigit == 4:
    $ pov_attack_multiplier = 0
    jump pov_mc_missed_label_faux
else:
    $ pov_attack_multiplier = pov_attack_multiplier_array[fightSelectDigit]
jump pov_mc_attack_label_faux

screen pov_fight_screen:
    tag pov_fight_screen
    modal True
    timer pov_timer action [Hide('pov_fight_screen'), SetVariable("fightBlockDigit", 4),Jump("pov_evaluate_label")]
    key "K_UP" action (SetVariable("fightBlockDigit", 0), Jump("pov_evaluate_label"))
    key "K_RIGHT" action (SetVariable("fightBlockDigit", 1), Jump("pov_evaluate_label"))
    key "K_DOWN" action (SetVariable("fightBlockDigit", 2), Jump("pov_evaluate_label"))
    key "K_LEFT" action (SetVariable("fightBlockDigit", 3), Jump("pov_evaluate_label"))
    key "w" action (SetVariable("fightBlockDigit", 0), Jump("pov_evaluate_label"))
    key "d" action (SetVariable("fightBlockDigit", 1), Jump("pov_evaluate_label"))
    key "s" action (SetVariable("fightBlockDigit", 2), Jump("pov_evaluate_label"))
    key "a" action (SetVariable("fightBlockDigit", 3), Jump("pov_evaluate_label"))

screen pov_fight_screen_faux:
    tag pov_fight_screen_faux
    modal True
    timer pov_timer action [Hide('pov_fight_screen_faux'), SetVariable("fightBlockDigit", 4),Jump("pov_mc_missed_label_faux")]
    key "K_UP" action (SetVariable("fightBlockDigit", 0), Jump("pov_evaluate_label_faux"))
    key "K_RIGHT" action (SetVariable("fightBlockDigit", 1), Jump("pov_evaluate_label_faux"))
    key "K_DOWN" action (SetVariable("fightBlockDigit", 2), Jump("pov_evaluate_label_faux"))
    key "K_LEFT" action (SetVariable("fightBlockDigit", 3), Jump("pov_evaluate_label_faux"))
    key "w" action (SetVariable("fightBlockDigit", 0), Jump("pov_evaluate_label_faux"))
    key "d" action (SetVariable("fightBlockDigit", 1), Jump("pov_evaluate_label_faux"))
    key "s" action (SetVariable("fightBlockDigit", 2), Jump("pov_evaluate_label_faux"))
    key "a" action (SetVariable("fightBlockDigit", 3), Jump("pov_evaluate_label_faux"))


label pov_evaluate_label:
$ renpy.block_rollback()
if mcTurn:
    if blockCombination[currentBlockNumber] != fightBlockDigit:
        jump pov_mc_missed_label
    $ currentBlockNumber += 1
    if currentBlockNumber == numberOfHits:
        jump pov_mc_hit_label
    jump pov_mc_attack_label_nofx
else:
    if blockCombination[currentBlockNumber] != fightBlockDigit:
        jump pov_mc_got_hit_label
    $ currentBlockNumber += 1
    if currentBlockNumber == numberOfHits:
        jump pov_mc_dodged_label
    jump pov_block_label_nofx

label pov_evaluate_label_faux:
$ renpy.block_rollback()
if blockCombination[currentBlockNumber] != fightBlockDigit:
    jump pov_mc_missed_label_faux
$ currentBlockNumber += 1
if currentBlockNumber == numberOfHits:
    hide screen pov_fight_screen_faux
    jump pov_mc_missed_label_faux
jump pov_mc_attack_label_faux_nofx


screen pov_neutral_img(x):
    add x

label sports101_start_pov_fight:
$ renpy.block_rollback()









$ brawlerPovNeutralLabel = ["brawler_pov_nerd_neutral_label", "brawler_pov_prep_neutral_label", "brawler_pov_jock_neutral_label", "brawler_pov_chad_neutral_label", "brawler_pov_troy_neutral_label", "brawler_pov_dawe_neutral_label", "brawler_pov_caleb_neutral_label", "brawler_pov_tommy_neutral_label", "brawler_pov_sage_neutral_label"]
$ pov_win_lose_labels = ["brawler_nerd_win_label", "brawler_nerd_lose_label", "brawler_prep_win_label", "brawler_prep_lose_label", "brawler_jock_win_label", "brawler_jock_lose_label", "", "", "", "", "", "", "", "", "", "", "", ""]
$ brawlerPovCPUHitsYouLabel = ["brawler_pov_nerd_hits_you_label", "brawler_pov_prep_hits_you_label", "brawler_pov_jock_hits_you_label", "brawler_pov_chad_hits_you_label", "brawler_pov_troy_hits_you_label", "brawler_pov_dawe_hits_you_label", "brawler_pov_caleb_hits_you_label", "brawler_pov_tommy_hits_you_label", "brawler_pov_sage_hits_you_label"]
$ brawlerPovMCDodgedLabel = ["brawler_pov_nerd_mc_dodged_label", "brawler_pov_prep_mc_dodged_label", "brawler_pov_jock_mc_dodged_label", "brawler_pov_chad_mc_dodged_label", "brawler_pov_troy_mc_dodged_label", "brawler_pov_dawe_mc_dodged_label", "brawler_pov_caleb_mc_dodged_label", "brawler_pov_tommy_mc_dodged_label", "brawler_pov_sage_mc_dodged_label"]
$ brawlerPovCPUDodgedLabel = ["brawler_pov_nerd_dodged_label", "brawler_pov_prep_dodged_label", "brawler_pov_jock_dodged_label", "brawler_pov_chad_dodged_label", "brawler_pov_troy_dodged_label", "brawler_pov_dawe_dodged_label", "brawler_pov_caleb_dodged_label", "brawler_pov_tommy_dodged_label", "brawler_pov_sage_dodged_label"]
$ brawlerPovMCHitLabel = ["brawler_pov_nerd_mc_hit_label", "brawler_pov_prep_mc_hit_label", "brawler_pov_jock_mc_hit_label", "brawler_pov_chad_mc_hit_label", "brawler_pov_troy_mc_hit_label", "brawler_pov_dawe_mc_hit_label", "brawler_pov_caleb_mc_hit_label", "brawler_pov_tommy_mc_hit_label", "brawler_pov_sage_mc_hit_label"]


if sports_pow == 0:
    $ sports_pow = 1
    $ sports_dex = 1
    $ sports_hp = 1
    $ sports_mov = 1

if brawler_difficulty == 3:
    if sports_opponent_idx > 6:
        if sports_dex == 1:
            $ pov_select_timer  = 1.0
            $ pov_short_timer   = 1.0
            $ pov_medium_timer  = 1.0
            $ pov_long_timer    = 1.0
            $ pov_short_timer_cpu   = 1.0
            $ pov_medium_timer_cpu  = 1.0
            $ pov_long_timer_cpu    = 1.0
        elif sports_dex == 2:
            $ pov_select_timer  = 1.0
            $ pov_short_timer   = 1.0
            $ pov_medium_timer  = 1.5
            $ pov_long_timer    = 1.5
            $ pov_short_timer_cpu   = 1.0
            $ pov_medium_timer_cpu  = 1.5
            $ pov_long_timer_cpu    = 1.5
        elif sports_dex == 3:
            $ pov_select_timer  = 1.0
            $ pov_short_timer   = 1.0
            $ pov_medium_timer  = 1.5
            $ pov_long_timer    = 1.5
            $ pov_short_timer_cpu   = 1.0
            $ pov_medium_timer_cpu  = 1.5
            $ pov_long_timer_cpu    = 2.0
        elif sports_dex == 4:
            $ pov_select_timer  = 1.0
            $ pov_short_timer   = 1.0
            $ pov_medium_timer  = 1.5
            $ pov_long_timer    = 2.5
            $ pov_short_timer_cpu   = 1.0
            $ pov_medium_timer_cpu  = 1.5
            $ pov_long_timer_cpu    = 2.0
    else:
        if sports_dex == 1:
            $ pov_select_timer  = 1.0
            $ pov_short_timer   = 1.0
            $ pov_medium_timer  = 1.0
            $ pov_long_timer    = 1.0
            $ pov_short_timer_cpu   = 1.0
            $ pov_medium_timer_cpu  = 2.0
            $ pov_long_timer_cpu    = 3.0
        elif sports_dex == 2:
            $ pov_select_timer  = 1.0
            $ pov_short_timer   = 1.0
            $ pov_medium_timer  = 1.5
            $ pov_long_timer    = 1.5
            $ pov_short_timer_cpu   = 1.5
            $ pov_medium_timer_cpu  = 2.0
            $ pov_long_timer_cpu    = 3.5
        elif sports_dex == 3:
            $ pov_select_timer  = 1.5
            $ pov_short_timer   = 1.5
            $ pov_medium_timer  = 1.5
            $ pov_long_timer    = 2.5
            $ pov_short_timer_cpu   = 1.5
            $ pov_medium_timer_cpu  = 2.5
            $ pov_long_timer_cpu    = 3.5
        elif sports_dex == 4:
            $ pov_select_timer  = 1.5
            $ pov_short_timer   = 1.5
            $ pov_medium_timer  = 2.0
            $ pov_long_timer    = 3.0
            $ pov_short_timer_cpu   = 2.0
            $ pov_medium_timer_cpu  = 3.0
            $ pov_long_timer_cpu    = 3.5
elif brawler_difficulty == 2:
    if sports_dex == 1:
        $ pov_select_timer  = 2.5
        $ pov_short_timer   = 2.0
        $ pov_medium_timer  = 2.5
        $ pov_long_timer    = 3.5
        $ pov_short_timer_cpu   = pov_short_timer
        $ pov_medium_timer_cpu  = pov_medium_timer
        $ pov_long_timer_cpu    = pov_long_timer
    elif sports_dex == 2:
        $ pov_select_timer  = 2.5
        $ pov_short_timer   = 2.5
        $ pov_medium_timer  = 3.0
        $ pov_long_timer    = 4.0
        $ pov_short_timer_cpu   = pov_short_timer
        $ pov_medium_timer_cpu  = pov_medium_timer
        $ pov_long_timer_cpu    = pov_long_timer
    elif sports_dex == 3:
        $ pov_select_timer  = 3.0
        $ pov_short_timer   = 3.0
        $ pov_medium_timer  = 3.0
        $ pov_long_timer    = 4.0
        $ pov_short_timer_cpu   = pov_short_timer
        $ pov_medium_timer_cpu  = pov_medium_timer
        $ pov_long_timer_cpu    = pov_long_timer
    elif sports_dex == 4:
        $ pov_select_timer  = 3.5
        $ pov_short_timer   = 4.0
        $ pov_medium_timer  = 4.5
        $ pov_long_timer    = 5.0
        $ pov_short_timer_cpu   = pov_short_timer
        $ pov_medium_timer_cpu  = pov_medium_timer
        $ pov_long_timer_cpu    = pov_long_timer
else:
    if sports_dex == 1:
        $ pov_select_timer  = 3.5
        $ pov_short_timer   = 3.0
        $ pov_medium_timer  = 3.5
        $ pov_long_timer    = 4.5
        $ pov_short_timer_cpu   = pov_short_timer
        $ pov_medium_timer_cpu  = pov_medium_timer
        $ pov_long_timer_cpu    = pov_long_timer
    elif sports_dex == 2:
        $ pov_select_timer  = 3.5
        $ pov_short_timer   = 3.5
        $ pov_medium_timer  = 4.0
        $ pov_long_timer    = 5.0
        $ pov_short_timer_cpu   = pov_short_timer
        $ pov_medium_timer_cpu  = pov_medium_timer
        $ pov_long_timer_cpu    = pov_long_timer
    elif sports_dex == 3:
        $ pov_select_timer  = 4.0
        $ pov_short_timer   = 4.0
        $ pov_medium_timer  = 4.0
        $ pov_long_timer    = 5.0
        $ pov_short_timer_cpu   = pov_short_timer
        $ pov_medium_timer_cpu  = pov_medium_timer
        $ pov_long_timer_cpu    = pov_long_timer
    elif sports_dex == 4:
        $ pov_select_timer  = 4.5
        $ pov_short_timer   = 5.0
        $ pov_medium_timer  = 5.5
        $ pov_long_timer    = 6.0
        $ pov_short_timer_cpu   = pov_short_timer
        $ pov_medium_timer_cpu  = pov_medium_timer
        $ pov_long_timer_cpu    = pov_long_timer

$ pov_starting = True
$ sports_rounded_player_hp = 100
$ sports_rounded_cpu_hp = 100
$ sports_pc_hp = 100
$ sports_cpu_hp = 100
$ sports_cpu_hp_skill = sports_opponents_stats[sports_opponent_idx*4]
if sports_mov < 3:
    $ maxHitsInARow = sports_mov
else:
    $ maxHitsInARow = 3


$ pov_attack_multiplier = 1.0
$ mcHitsInARow = 0
$ cpuHitsInARow = 0
$ roundHouseCoolDown = 0
$ pov_cpu_special = 0
$ pov_cpu_special_counter = 0
$ pov_mc_healed = False

$ fightSelectDigit = 0
$ fightBlockDigit = 0



$ fightArrowIdle = ["arrow_up_idle", "arrow_right_idle", "arrow_down_idle", "arrow_left_idle"]
$ fightArrowActive = ["arrow_up_active", "arrow_right_active", "arrow_down_active", "arrow_left_active"]
$ fightYPos = 800 * persistent.scale_factor
$ missArray = ["pov_miss", "pov_miss", "pov_fail", "pov_nope"]
$ punchArray = ["pov_hit", "pov_weak", "pov_fist", "pov_thud"]
$ kickArray = ["pov_kick", "pov_hard", "pov_high", "pov_blam"]
$ powerfulArray = ["pov_super", "pov_round", "pov_power", "pov_ouch"]
$ pov_attack_text_array = ["", "", "", ""]

show screen pov_health_screen
$ renpy.block_rollback()
$ fightPovLabel = "pov_decide_turn_label"
$ renpy.jump(fightPovLabel)

label sports101_start_pov_fight_faux:
$ renpy.block_rollback()

$ pov_select_timer  = 4.5
$ pov_short_timer   = 5.0
$ pov_medium_timer  = 5.5
$ pov_long_timer    = 6.0
$ pov_short_timer_cpu   = pov_short_timer
$ pov_medium_timer_cpu  = pov_medium_timer
$ pov_long_timer_cpu    = pov_long_timer

$ pov_starting = True
$ sports_rounded_player_hp = 100
$ sports_rounded_cpu_hp = 100
$ sports_pc_hp = 100
$ sports_cpu_hp = 100
$ sports_cpu_hp_skill = 8
$ maxHitsInARow = 3


$ pov_attack_multiplier = 1.0
$ mcHitsInARow = 0
$ cpuHitsInARow = 0
$ roundHouseCoolDown = 0
$ pov_cpu_special = 0
$ pov_cpu_special_counter = 0
$ pov_mc_healed = False

$ fightSelectDigit = 0
$ fightBlockDigit = 0
$ fightArrowIdle = ["arrow_up_idle", "arrow_right_idle", "arrow_down_idle", "arrow_left_idle"]
$ fightArrowActive = ["arrow_up_active", "arrow_right_active", "arrow_down_active", "arrow_left_active"]
$ fightYPos = 800 * persistent.scale_factor
$ missArray = ["pov_miss", "pov_miss", "pov_fail", "pov_nope"]
$ punchArray = ["pov_hit", "pov_weak", "pov_fist", "pov_thud"]
$ kickArray = ["pov_kick", "pov_hard", "pov_high", "pov_blam"]
$ powerfulArray = ["pov_super", "pov_round", "pov_power", "pov_ouch"]
$ pov_attack_text_array = ["", "", "", ""]

show screen pov_health_screen
$ renpy.block_rollback()
$ numberOfHits = renpy.random.randint(3, 5)
if numberOfHits == 5:
    $ pov_timer = pov_long_timer
    $ blockCombination = [0, 0, 0, 0, 0]
    $ arrowXPositionArray = [710 * persistent.scale_factor, 810 * persistent.scale_factor, 910 * persistent.scale_factor, 1010 * persistent.scale_factor, 1110 * persistent.scale_factor]
elif numberOfHits == 4:
    $ pov_timer = pov_medium_timer
    $ blockCombination = [0, 0, 0, 0]
    $ arrowXPositionArray = [760 * persistent.scale_factor, 860 * persistent.scale_factor, 960 * persistent.scale_factor, 1060 * persistent.scale_factor]
else:
    $ pov_timer = pov_short_timer
    $ blockCombination = [0, 0, 0]
    $ arrowXPositionArray = [810 * persistent.scale_factor, 910 * persistent.scale_factor, 1010 * persistent.scale_factor]

$ tmpInt = 0
while numberOfHits > tmpInt:
    $ blockCombination[tmpInt] = renpy.random.randint(0, 3)
    $ tmpInt += 1

$ currentBlockNumber = 0

$ pov_attack_multiplier_array = [renpy.random.randint(8, 12), renpy.random.randint(8, 12), renpy.random.randint(8, 12), renpy.random.randint(8, 12)]

$ tmpInt = 0
while tmpInt < 4:
    $ tmpInt2 = renpy.random.randint(0, 3)
    if pov_attack_multiplier_array[tmpInt] == 8 or pov_attack_multiplier_array[tmpInt] == 9:
        $ pov_attack_text_array[tmpInt] = punchArray[tmpInt2]
    elif pov_attack_multiplier_array[tmpInt] < 12 or roundHouseCoolDown > 0 or not sports_roundhouse_skill:
        $ pov_attack_text_array[tmpInt] = kickArray[tmpInt2]
    else:
        $ pov_attack_text_array[tmpInt] = powerfulArray[tmpInt2]
    $ tmpInt += 1

show pov_ready
$ renpy.pause(1.5)
hide pov_ready
show pov_fight
$ renpy.pause(1.5)
hide pov_fight

$ renpy.block_rollback()
show screen pov_select_screen_faux
$ ui.imagebutton(fightArrowIdle[0],fightArrowIdle[0], clicked=ui.returns("NULL"), xpos = 910 * persistent.scale_factor, ypos = 600 * persistent.scale_factor)
$ ui.imagebutton(fightArrowIdle[1],fightArrowIdle[1], clicked=ui.returns("NULL"), xpos = 1010 * persistent.scale_factor, ypos = 700 * persistent.scale_factor)
$ ui.imagebutton(fightArrowIdle[2],fightArrowIdle[2], clicked=ui.returns("NULL"), xpos = 910 * persistent.scale_factor, ypos = 800 * persistent.scale_factor)
$ ui.imagebutton(fightArrowIdle[3],fightArrowIdle[3], clicked=ui.returns("NULL"), xpos = 810 * persistent.scale_factor, ypos = 700 * persistent.scale_factor)

$ ui.imagebutton(pov_attack_text_array[0],pov_attack_text_array[0], clicked=ui.returns("NULL"), xpos = 910 * persistent.scale_factor, ypos = 500 * persistent.scale_factor)
$ ui.imagebutton(pov_attack_text_array[1],pov_attack_text_array[1], clicked=ui.returns("NULL"), xpos = 1110 * persistent.scale_factor, ypos = 700 * persistent.scale_factor)
$ ui.imagebutton(pov_attack_text_array[2],pov_attack_text_array[2], clicked=ui.returns("NULL"), xpos = 910 * persistent.scale_factor, ypos = 900 * persistent.scale_factor)
$ ui.imagebutton(pov_attack_text_array[3],pov_attack_text_array[3], clicked=ui.returns("NULL"), xpos = 710 * persistent.scale_factor, ypos = 700 * persistent.scale_factor)

$ renpy.pause()


label pov_decide_turn_label:
$ renpy.block_rollback()
$ tmpInt = renpy.random.randint(1, 100)

if pov_cpu_special_counter == 0:
    $ pov_cpu_special = 5
    $ pov_cpu_special_counter = 2
if mcHitsInARow < maxHitsInARow and tmpInt <= 50 + sports_dex*2 - sports_cpu_dex*2:
    $ mcHitsInARow += 1
    $ cpuHitsInARow = 0
    $ mcTurn = True
    jump pov_new_attack_start_label
elif cpuHitsInARow < sports_cpu_mov:
    $ mcHitsInARow = 0
    $ cpuHitsInARow += 1
    $ mcTurn = False
    jump pov_new_block_start_label
else:
    $ mcHitsInARow += 1
    $ cpuHitsInARow = 0
    $ mcTurn = True
    jump pov_new_attack_start_label


label pov_new_attack_start_label:
$ renpy.block_rollback()
$ numberOfHits = renpy.random.randint(3, 5)
if numberOfHits == 5:
    $ pov_timer = pov_long_timer
    $ blockCombination = [0, 0, 0, 0, 0]
    $ arrowXPositionArray = [710 * persistent.scale_factor, 810 * persistent.scale_factor, 910 * persistent.scale_factor, 1010 * persistent.scale_factor, 1110 * persistent.scale_factor]
elif numberOfHits == 4:
    $ pov_timer = pov_medium_timer
    $ blockCombination = [0, 0, 0, 0]
    $ arrowXPositionArray = [760 * persistent.scale_factor, 860 * persistent.scale_factor, 960 * persistent.scale_factor, 1060 * persistent.scale_factor]
else:
    $ pov_timer = pov_short_timer
    $ blockCombination = [0, 0, 0]
    $ arrowXPositionArray = [810 * persistent.scale_factor, 910 * persistent.scale_factor, 1010 * persistent.scale_factor]

$ tmpInt = 0
while numberOfHits > tmpInt:
    $ blockCombination[tmpInt] = renpy.random.randint(0, 3)
    $ tmpInt += 1

$ currentBlockNumber = 0

$ pov_attack_multiplier_array = [renpy.random.randint(8, 12), renpy.random.randint(8, 12), renpy.random.randint(8, 12), renpy.random.randint(8, 12)]
$ tmpInt = renpy.random.randint(1, 2)
while tmpInt > 0:
    $ pov_attack_multiplier_array[renpy.random.randint(0, 3)] = 0
    $ tmpInt -= 1

$ tmpInt = 0
$ tmpInt3 = 0
while tmpInt < 4:
    $ tmpInt2 = renpy.random.randint(0, 3)
    if tmpInt3 != 3 or pov_attack_multiplier_array[tmpInt] == 0:
        if pov_attack_multiplier_array[tmpInt] == 0:
            $ pov_attack_text_array[tmpInt] = missArray[tmpInt2]
            $ tmpInt3 += 1
        elif pov_attack_multiplier_array[tmpInt] == 8 or pov_attack_multiplier_array[tmpInt] == 9:
            $ pov_attack_text_array[tmpInt] = punchArray[tmpInt2]
        elif pov_attack_multiplier_array[tmpInt] < 12 or roundHouseCoolDown > 0 or not sports_roundhouse_skill:
            $ pov_attack_text_array[tmpInt] = kickArray[tmpInt2]
        else:
            $ pov_attack_text_array[tmpInt] = powerfulArray[tmpInt2]
        $ tmpInt += 1
if roundHouseCoolDown > 0:
    $ roundHouseCoolDown -= 1
if sports_heal_skill and sports_pc_hp <= 60:
    if not pov_mc_healed and renpy.random.randint(0, 1) == 1:
        $ tmpInt2 = renpy.random.randint(0, 3)
        $ pov_attack_text_array[tmpInt2] = "pov_heal"
        $ pov_attack_multiplier_array[tmpInt2] = -1

label pov_neutral_label:
$ renpy.block_rollback()
$ pov_neutral_mode = 0
$ renpy.jump(brawlerPovNeutralLabel[sports_opponent_idx])
label pov_neutral2_label:
if pov_starting:
    show pov_ready
    $ renpy.pause(1.5)
    hide pov_ready
    if brawlerStoryFightLabel == "":
        play sound "sound_effects/bell.mp3"
    show pov_fight
    $ renpy.pause(1.5)
    hide pov_fight
    $ pov_starting = False
label pov_neutral_select_label:
$ renpy.block_rollback()
show screen pov_select_screen
$ ui.imagebutton(fightArrowIdle[0],fightArrowIdle[0], clicked=ui.returns("NULL"), xpos = 910 * persistent.scale_factor, ypos = 600 * persistent.scale_factor)
$ ui.imagebutton(fightArrowIdle[1],fightArrowIdle[1], clicked=ui.returns("NULL"), xpos = 1010 * persistent.scale_factor, ypos = 700 * persistent.scale_factor)
$ ui.imagebutton(fightArrowIdle[2],fightArrowIdle[2], clicked=ui.returns("NULL"), xpos = 910 * persistent.scale_factor, ypos = 800 * persistent.scale_factor)
$ ui.imagebutton(fightArrowIdle[3],fightArrowIdle[3], clicked=ui.returns("NULL"), xpos = 810 * persistent.scale_factor, ypos = 700 * persistent.scale_factor)

$ ui.imagebutton(pov_attack_text_array[0],pov_attack_text_array[0], clicked=ui.returns("NULL"), xpos = 910 * persistent.scale_factor, ypos = 500 * persistent.scale_factor)
$ ui.imagebutton(pov_attack_text_array[1],pov_attack_text_array[1], clicked=ui.returns("NULL"), xpos = 1110 * persistent.scale_factor, ypos = 700 * persistent.scale_factor)
$ ui.imagebutton(pov_attack_text_array[2],pov_attack_text_array[2], clicked=ui.returns("NULL"), xpos = 910 * persistent.scale_factor, ypos = 900 * persistent.scale_factor)
$ ui.imagebutton(pov_attack_text_array[3],pov_attack_text_array[3], clicked=ui.returns("NULL"), xpos = 710 * persistent.scale_factor, ypos = 700 * persistent.scale_factor)

$ renpy.pause()

label pov_mc_attack_label:
$ renpy.block_rollback()
show screen pov_fight_screen
label pov_mc_attack_label_nofx:
$ renpy.block_rollback()
$ tmpInt = 0
while tmpInt < numberOfHits:
    if tmpInt < currentBlockNumber:
        $ ui.imagebutton(fightArrowActive[blockCombination[tmpInt]],fightArrowActive[blockCombination[tmpInt]], clicked=ui.returns("NULL"), xpos = arrowXPositionArray[tmpInt], ypos = fightYPos)
    else:
        $ ui.imagebutton(fightArrowIdle[blockCombination[tmpInt]],fightArrowIdle[blockCombination[tmpInt]], clicked=ui.returns("NULL"), xpos = arrowXPositionArray[tmpInt], ypos = fightYPos)
    $ tmpInt += 1
$ renpy.pause()

label pov_mc_attack_label_faux:
$ renpy.block_rollback()
show screen pov_fight_screen_faux
label pov_mc_attack_label_faux_nofx:
$ renpy.block_rollback()
$ tmpInt = 0
while tmpInt < numberOfHits:
    if tmpInt < currentBlockNumber:
        $ ui.imagebutton(fightArrowActive[blockCombination[tmpInt]],fightArrowActive[blockCombination[tmpInt]], clicked=ui.returns("NULL"), xpos = arrowXPositionArray[tmpInt], ypos = fightYPos)
    else:
        $ ui.imagebutton(fightArrowIdle[blockCombination[tmpInt]],fightArrowIdle[blockCombination[tmpInt]], clicked=ui.returns("NULL"), xpos = arrowXPositionArray[tmpInt], ypos = fightYPos)
    $ tmpInt += 1
$ renpy.pause()


label pov_new_block_start_label:
$ renpy.block_rollback()
$ numberOfHits = renpy.random.randint(3, 5)
if numberOfHits == 5:
    $ pov_timer = pov_long_timer_cpu
    $ blockCombination = [0, 0, 0, 0, 0]
    $ arrowXPositionArray = [710 * persistent.scale_factor, 810 * persistent.scale_factor, 910 * persistent.scale_factor, 1010 * persistent.scale_factor, 1110 * persistent.scale_factor]
elif numberOfHits == 4:
    $ pov_timer = pov_medium_timer_cpu
    $ blockCombination = [0, 0, 0, 0]
    $ arrowXPositionArray = [760 * persistent.scale_factor, 860 * persistent.scale_factor, 960 * persistent.scale_factor, 1060 * persistent.scale_factor]
else:
    $ pov_timer = pov_short_timer_cpu
    $ blockCombination = [0, 0, 0]
    $ arrowXPositionArray = [810 * persistent.scale_factor, 910 * persistent.scale_factor, 1010 * persistent.scale_factor]

$ tmpInt = 0
while numberOfHits > tmpInt:
    $ blockCombination[tmpInt] = renpy.random.randint(0, 3)
    $ tmpInt += 1

$ currentBlockNumber = 0

label pov_block_label:
$ renpy.block_rollback()
$ pov_neutral_mode = 1
$ renpy.jump(brawlerPovNeutralLabel[sports_opponent_idx])
label pov_block2_label:
if pov_starting:
    show pov_ready
    $ renpy.pause(1.5)
    hide pov_ready
    show pov_fight
    if brawlerStoryFightLabel == "":
        play sound "sound_effects/bell.mp3"
    $ renpy.pause(1.5)
    hide pov_fight
    $ pov_starting = False
label pov_block_label_nofx:
$ renpy.block_rollback()
show screen pov_fight_screen
$ tmpInt = 0
while tmpInt < numberOfHits:
    if tmpInt < currentBlockNumber:
        $ ui.imagebutton(fightArrowActive[blockCombination[tmpInt]],fightArrowActive[blockCombination[tmpInt]], clicked=ui.returns("NULL"), xpos = arrowXPositionArray[tmpInt], ypos = fightYPos)
    else:
        $ ui.imagebutton(fightArrowIdle[blockCombination[tmpInt]],fightArrowIdle[blockCombination[tmpInt]], clicked=ui.returns("NULL"), xpos = arrowXPositionArray[tmpInt], ypos = fightYPos)
    $ tmpInt += 1
$ renpy.pause()



label pov_mc_got_hit_label:
$ renpy.block_rollback()
hide screen pov_fight_screen
$ renpy.jump(brawlerPovCPUHitsYouLabel[sports_opponent_idx])
label pov_mc_got_hit2_label:
$ sports_dmg = int(sports_pow_multi[sports_cpu_pow] * renpy.random.randint(10-sports_hp+pov_cpu_special, 20-sports_hp+pov_cpu_special))
$ sports_pc_hp -= sports_dmg
if sports_pc_hp < 0:
    $ sports_pc_hp = 0
if int(sports_pc_hp/10)*10 > 0:
    $ sports_rounded_player_hp = int(sports_pc_hp/10)*10
elif sports_pc_hp > 0:
    $ sports_rounded_player_hp = 10
else:
    $ sports_rounded_player_hp = 0
$ renpy.pause(1.5)
if sports_pc_hp <= 0:
    $ sports_victory = False
    jump pov_fight_done
if pov_cpu_special != 0:
    $ pov_cpu_special = 0
$ pov_cpu_special_counter -= 1
jump pov_decide_turn_label

label pov_mc_dodged_label:
$ renpy.block_rollback()
hide screen pov_fight_screen
$ renpy.jump(brawlerPovMCDodgedLabel[sports_opponent_idx])
label pov_mc_dodged2_label:
$ renpy.pause(1.5)
if pov_cpu_special != 0:
    $ pov_cpu_special = 0
$ pov_cpu_special_counter -= 1
jump pov_decide_turn_label

label pov_mc_missed_label:
$ renpy.block_rollback()
hide screen pov_fight_screen
$ renpy.jump(brawlerPovCPUDodgedLabel[sports_opponent_idx])

label pov_mc_hit_label:
$ renpy.block_rollback()
hide screen pov_fight_screen
$ renpy.jump(brawlerPovMCHitLabel[sports_opponent_idx])
label pov_mc_hit2_label:
$ sports_dmg = int(sports_pow_multi[sports_pow] * (renpy.random.randint(10*pov_attack_multiplier, 20*pov_attack_multiplier)/10 - sports_cpu_hp_skill))
$ sports_cpu_hp -= sports_dmg
if sports_cpu_hp < 0:
    $ sports_cpu_hp = 0
if int(sports_cpu_hp/10)*10 > 0:
    $ sports_rounded_cpu_hp = int(sports_cpu_hp/10)*10
elif sports_cpu_hp > 0:
    $ sports_rounded_cpu_hp = 10
else:
    $ sports_rounded_cpu_hp = 0
$ renpy.pause(1.5)
if sports_cpu_hp <= 0:
    $ sports_victory = True
    jump pov_fight_done
jump pov_decide_turn_label

label pov_mc_healed_label:
show pov_healed
$ sports_pc_hp += 50
if sports_pc_hp > 100:
    $ sports_pc_hp = 100
$ sports_rounded_player_hp = int(sports_pc_hp/10)*10
$ renpy.pause(2.0)
hide pov_healed
jump pov_decide_turn_label

label pov_fight_done:
hide screen pov_health_screen
if sports_victory:
    if brawlerStoryFightLabel == "":
        $ renpy.jump(pov_win_lose_labels[sports_opponent_idx*2])
        label pov_fight_done2:
        $ renpy.pause(1)
        show sports_victory
        $ renpy.pause()
        hide sports_victory
        scene black with fade
    if sports_opponent_idx == 0 and steamAchievements and not config.console and not config.developer:
        $ achievement.grant("NERDPUMMEL")
        init:
            $ achievement.register("NERDPUMMEL")
        $ achievement.Sync()
    elif sports_opponent_idx == 1 and steamAchievements and not config.console and not config.developer:
        $ achievement.grant("PREPPUMMEL")
        init:
            $ achievement.register("PREPPUMMEL")
        $ achievement.Sync()
    elif sports_opponent_idx == 2 and steamAchievements and not config.console and not config.developer:
        $ achievement.grant("JOCKPUMMEL")
        init:
            $ achievement.register("JOCKPUMMEL")
        $ achievement.Sync()
    if sports_opponent_idx == 0 and brawler_money_available:
        $ brawler_money_available = False
        $ mny(1)
        show text "{size=+%d}You won {color=#36ca2b}${/color}!\nYou can try to win more during the next free roam.{/size}" % (20 * persistent.scale_factor)
    elif sports_opponent_idx == 1 and brawler_render_available:
        $ brawler_render_available = False





        show text "{size=+%d}You unlocked a Special render!\nKeep your eyes open for more Special renders during future free roam events.{/size}" % (20 * persistent.scale_factor)
    elif sports_opponent_idx == 2 and brawler_skillpoint_available:
        $ brawler_skillpoint_available = False
        if bonusPointsSports < 12:
            $ bonusPointsSports += 1
            if bonusPointsSports != 12:
                show text "{size=+%d}You got a new skill point!\nYou can try to win more during the next free roam.{/size}" % (20 * persistent.scale_factor)
            else:
                show text "{size=+%d}You got a new skill point! You are now at max level!\n The hardest difficulty will award money in the future, instead of skill points.{/size}" % (20 * persistent.scale_factor)
        else:
            $ mny(1)
            show text "{size=+%d}You won {color=#36ca2b}${/color}!\nYou can try to win more during the next free roam.{/size}" % (20 * persistent.scale_factor)
    elif brawlerStoryFightLabel == "":
        show text "{size=+%d}You got no reward from this fight.{/size}" % (20 * persistent.scale_factor)
    if brawlerStoryFight == "":
        $ renpy.pause()


    if brawlerStoryFightLabel == "":
        $ renpy.jump(pov_win_lose_labels[sports_opponent_idx*2+1])
        label pov_fight_done3:
        $ renpy.pause(1)
        show sports_loss
        $ renpy.pause()
        hide sports_loss


$ renpy.block_rollback()

if brawlerStoryFightLabel != "":
    $ map_fast_travel_enabled = True
    $ fightPovLabel = brawlerStoryFightLabel
else:
    $ fightPovLabel = "sports101_fight_menu"
$ renpy.jump(fightPovLabel)
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
