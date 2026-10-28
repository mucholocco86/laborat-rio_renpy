





screen scr_sports101_skills:
    text "{size=+%d}{color=#2b2b2b}Skill points left: [sports_skillpointsleft]{/color}{/size}" % (20 * persistent.scale_factor) xpos 0.391 ypos 0.021
    text "{size=+%d}{color=#ffaf05}Skill points left: [sports_skillpointsleft]{/color}{/size}" % (20 * persistent.scale_factor) xpos 0.39 ypos 0.02

screen scr_sports101_menu:
    text "{font=fonts/collegiate.ttf}{color=#ffaf05}HP: [sports_hp]\nPOW: [sports_pow]\nDEX: [sports_dex]\nMOV: [sports_mov]{/color}{/font}" xpos 0.015 ypos 0.85
    text "{font=fonts/collegiate.ttf}{color=[cpu_color]}HP: [sports_cpu_hp]\nPOW: [sports_cpu_pow]\nDEX: [sports_cpu_dex]\nMOV: [sports_cpu_mov]{/color}{/font}" xpos 0.92 ypos 0.85

screen scr_sports101_opponents:
    text "{color=#000000}HP: [sports_hp]\nPOW: [sports_pow]\nDEX: [sports_dex]\nMOV: [sports_mov]{/color}" xpos 0.51 ypos 0.57
    text "{color=#000000}[name]{/color}" xpos 0.404 ypos 0.741
    text "{color=#ffaf05}[name]{/color}" xpos 0.403 ypos 0.74

    text "{color=#000000}HP: [sports_opponents_stats[0]]\nPOW: [sports_opponents_stats[1]]\nDEX: [sports_opponents_stats[2]]\nMOV: [sports_opponents_stats[3]]{/color}" xpos 0.123 ypos 0.163
    text "{color=#000000}[sports_opponents[0]]{/color}" xpos 0.124 ypos 0.338
    text "{color=[sports_opponents[1]]}[sports_opponents[0]]{/color}" xpos 0.123 ypos 0.337

    text "{color=#000000}HP: [sports_opponents_stats[4]]\nPOW: [sports_opponents_stats[5]]\nDEX: [sports_opponents_stats[6]]\nMOV: [sports_opponents_stats[7]]{/color}" xpos 0.406 ypos 0.163
    text "{color=#000000}[sports_opponents[3]]{/color}" xpos 0.407 ypos 0.338
    text "{color=[sports_opponents[4]]}[sports_opponents[3]]{/color}" xpos 0.406 ypos 0.337

    text "{color=#000000}HP: [sports_opponents_stats[8]]\nPOW: [sports_opponents_stats[9]]\nDEX: [sports_opponents_stats[10]]\nMOV: [sports_opponents_stats[11]]{/color}" xpos 0.689 ypos 0.163
    text "{color=#000000}[sports_opponents[6]]{/color}" xpos 0.690 ypos 0.338
    text "{color=[sports_opponents[7]]}[sports_opponents[6]]{/color}" xpos 0.689 ypos 0.337

label app_brawler_label:
$ renpy.block_rollback()
if brawlerStoryFight == "":
    stop music fadeout 2
    $ loopFightMusic = True
$ map_fast_travel_enabled = False
hide screen new_phone_screen
hide screen mphone_screen
if sports_pow > 4:
    $ sports_pow = 4
if sports_dex > 4:
    $ sports_dex = 4
if sports_hp > 4:
    $ sports_hp = 4
if sports_mov > 4:
    $ sports_mov = 4
if bonusPointsSports > 12:
    $ bonusPointsSports = 12
if sports_pow == 0:
    scene brawler_nerd_menu with dissolve
    $ sports_pow = 1
    $ sports_dex = 1
    $ sports_hp = 1
    $ sports_mov = 1
    show brawler_tutorial_0 with dissolve
    show text "{color=#ffffff}Do you want to play in easy, normal or hard mode?\nHard mode will put a premium on reaction time.{/color}"
    $ renpy.pause()
    menu:
        "{size=-%3}Easy mode{/size}":
            $ brawler_difficulty = 1
        "{size=-%3}Normal mode{/size}":
            $ brawler_difficulty = 2
        "{size=-%3}Hard mode{/size}":
            $ brawler_difficulty = 3

    if not sports_tutorial:
        show brawler_tutorial_0 with dissolve
        show text "{color=#ffffff}Do you want to watch the tutorial?{/color}"
        menu:
            "Yes":
                label sports101_tutorial:
                show brawler_tutorial_0 with dissolve
                show text "{color=#ffffff}In Brawler you are pitted against opponents in {i}friendly{/i} sparring fights.\nYou can win money, Special renders and skill points (used in Brawler), by playing this mini-game.{/color}"
                pause
                show text "{color=#ffffff}Your skills in the mini-game carry over to main story events,\n in case you ever have to defend yourself.{/color}"
                pause
                show text "{color=#ffffff}Before you start fighting, you may allocate your skill points in different stats.{/color}"
                pause
                show text "{color=#fe9416}POW{/color}{color=#ffffff} - Power. Determines how much damage you deal.{/color}\n\n{color=#fe9416}DEX{/color}{color=#ffffff} - Dexterity. Longer reaction times and a higher chance to attack instead of to block.{/color}\n\n{color=#fe9416}HP{/color} {color=#ffffff}- Health points. Determines how much damage you can receive before losing.{/color}\n\n{color=#fe9416}MOV{/color} {color=#ffffff}- Movement. Determines the maximum number of times you can attack in a row.{/color}"
                pause
                show text "{color=#ffffff}The goal is to knock out your opponent before he knocks you out.{/color}"
                pause
                hide text
                hide brawler_tutorial_0 with dissolve
                show brawler_tutorial_1 with dissolve:
                    ypos 0.0
                    xpos 0.0
                "The mini-game has two phases, attack and defend."
                "When it's your turn to attack you, will see four directional arrows on the screen with four different options."
                "Select one option using the arrow keys on your keyboard..."
                "...but be quick or you will fail your attack."
                show brawler_tutorial_2 with dissolve:
                    ypos 0.0
                    xpos 0.0
                "After selecting an attack, you need to enter the combination that pops up on the screen using the arrow keys."
                "If you enter the correct combination and are quick enough, you will successfully attack your opponent."
                "If you press the wrong key, or if you take too long trying to enter the combination, you will fail your attack."
                "When it's your turn to defend you will, once again, have to enter a combination that pops up on the screen."
                "If you succeed, you will defend the attack. Otherwise, you will get hit and lose some HP."
                show brawler_tutorial_3 with dissolve:
                    ypos 0.0
                    xpos 0.0
                "When you're attacking, you want to look out for certain keywords and avoid others."
                "You can buy skills and skill points in the \"Store\". Don't forget to allocate your skill points in the \"Skills\" menu."
                "You can also change your Skill point allocation in the \"Skills\" menu and try different combinations."
                "Beat different opponents to get different rewards."
                if sports_tutorial:
                    jump sports101_fight_menu
                $ sports_tutorial = True
                scene brawler_nerd_menu with dissolve
                jump sports101_fight1_skills
            "No":
                hide text
                hide brawler_tutorial_0
                $ sports_tutorial = True
                jump sports101_fight1_skills
elif brawler_difficulty == 0:
    show brawler_tutorial_0 with dissolve
    show text "{color=#ffffff}Do you want to play in easy, normal or hard mode?\nHard mode will put a premium on reaction time.{/color}"
    $ renpy.pause()
    menu:
        "{size=-%3}Easy mode{/size}":
            $ brawler_difficulty = 1
        "{size=-%3}Normal mode{/size}":
            $ brawler_difficulty = 2
        "{size=-%3}Hard mode{/size}":
            $ brawler_difficulty = 3
    hide text
    hide brawler_tutorial_0
$ renpy.block_rollback()

label sports101_fight_menu:

$ sports_opponents = ["Nerd", "#c700dd", "sports_avatar_nerd", "Prep", "#87fa5a", "sports_avatar_prep", "Jock", "#23b4fc", "sports_avatar_jock", "Chad", "#23b4fc", "sports_avatar_chad", "Troy", "#ff0000", "sports_avatar_troy", "Dawe", "#45ebf7", "sports_avatar_dawe", "Caleb", "#4f80db", "sports_avatar_caleb", "Tommy", "#9e5900", "sports_avatar_tommy", "Sage", "#BCB88A", "sports_avatar_sage"]
$ sports_opponents_tiles = ["sports_nerd_tile", "sports_nerd_tile_attackable","sports_prep_tile", "sports_prep_tile_attackable", "sports_jock_tile","sports_jock_tile_attackable", "sports_chad_tile", "sports_chad_tile_attackable", "sports_troy_tile", "sports_troy_tile_attackable", "sports_dawe_tile", "sports_dawe_tile_attackable"]
$ sports_opponents_stats = [1, 1, 3, 1, 2, 2, 2, 2, 4, 4, 2, 2, 4, 4, 4, 4, 1, 1, 2, 2, 3, 3, 2, 2, 4, 4, 4, 4, 7, 4, 5, 5, 8, 5, 5, 5]

if brawlerStoryFight == "troy":
    $ sports_opponent_idx = 4
elif brawlerStoryFight == "chad":
    $ sports_opponent_idx = 3
elif brawlerStoryFight == "dawe":
    $ sports_opponent_idx = 5
elif brawlerStoryFight == "caleb":
    $ sports_opponent_idx = 6
elif brawlerStoryFight == "tommy":
    $ sports_opponent_idx = 7
elif brawlerStoryFight == "sage":
    $ sports_opponent_idx = 8
elif sports_opponent_idx > 2:
    $ sports_opponent_idx = 0
$ cpu_name = sports_opponents[sports_opponent_idx*3]
$ cpu_color = sports_opponents[sports_opponent_idx*3+1]
$ cpu_avatar = sports_opponents[sports_opponent_idx*3+2]
$ sports_cpu_hp = sports_opponents_stats[sports_opponent_idx*4]
$ sports_cpu_pow = sports_opponents_stats[sports_opponent_idx*4 + 1]
$ sports_cpu_dex = sports_opponents_stats[sports_opponent_idx*4 + 2]
$ sports_cpu_mov = sports_opponents_stats[sports_opponent_idx*4 + 3]
$ cpu_hp_state = 1
$ sports_pc_hp = 90 + 10 * sports_hp
$ sports_rounded_player_hp = sports_pc_hp
$ sports_rounded_cpu_hp = 100
$ sports_pow_multi = [0.0, 1.0, 1.25 ,1.5, 2.0, 3.0, 4.0, 5.0]
$ sports_victory = False
$ sports_player_healed = 0
if brawlerStoryFight != "":
    jump sports101_start_pov_fight

if sports_opponent_idx == 0:
    scene brawler_nerd_menu
elif sports_opponent_idx == 1:
    scene brawler_prep_menu
else:
    scene brawler_jock_menu

show screen scr_sports101_menu
$ ui.imagebutton("sports_menu_bg", "sports_menu_bg", clicked=ui.returns("NULL"), xpos=0, ypos=0)

$ ui.imagebutton("sports_logo", "sports_logo", clicked=ui.returns("FAIL"), xpos=0, ypos=30 * persistent.scale_factor)
if brawlerStoryFight == "":
    $ ui.imagebutton("sports_opponent", "sports_opponent_hover", clicked=ui.returns("opponent"), xpos=635 * persistent.scale_factor, ypos=200 * persistent.scale_factor)
    $ ui.imagebutton("sports_quit", "sports_quit_hover", clicked=ui.returns("quit"), xpos=635 * persistent.scale_factor, ypos=850 * persistent.scale_factor)
$ ui.imagebutton("sports_store", "sports_store_hover", clicked=ui.returns("store"), xpos=635 * persistent.scale_factor, ypos=330 * persistent.scale_factor)
$ ui.imagebutton("sports_skills", "sports_skills_hover", clicked=ui.returns("skills"), xpos=635 * persistent.scale_factor, ypos=460 * persistent.scale_factor)
$ ui.imagebutton("sports_fight", "sports_fight_hover", clicked=ui.returns("fight"), xpos=635 * persistent.scale_factor, ypos=590 * persistent.scale_factor)
$ ui.imagebutton("sports_tutorial", "sports_tutorial_hover", clicked=ui.returns("tutorial"), xpos=635 * persistent.scale_factor, ypos=720 * persistent.scale_factor)
if brawler_difficulty == 3:
    $ ui.imagebutton("sports_lower_hard", "sports_lower_hard_hover", clicked=ui.returns("lower"), xpos=1450 * persistent.scale_factor, ypos=0)
elif brawler_difficulty == 2:
    $ ui.imagebutton("sports_lower_normal", "sports_lower_normal_hover", clicked=ui.returns("lower"), xpos=1450 * persistent.scale_factor, ypos=0)
else:
    $ ui.imagebutton("sports_lower_easy", "sports_lower_easy", clicked=ui.returns("NULL"), xpos=1550 * persistent.scale_factor, ypos=0)
$ result = ui.interact()
if result == "skills":
    hide screen scr_sports101_menu
    jump sports101_fight1_skills
elif result == "opponent":
    hide screen scr_sports101_menu
    jump sports101_fight1_opponent
elif result == "store":
    hide screen scr_sports101_menu
    jump sports101_fight1_store
elif result == "fight":
    hide screen scr_sports101_menu
    jump sports101_start_pov_fight
elif result == "tutorial":
    hide screen scr_sports101_menu
    jump sports101_tutorial
elif result == "quit":
    hide screen scr_sports101_menu
    jump sports_fight1_quit
elif result == "lower":
    hide screen scr_sports101_menu
    show brawler_tutorial_0 with dissolve
    show text "This action is irreversible. Do you want to lower the difficulty?"
    menu:
        "Yes. Lower the difficulty.":
            $ brawler_difficulty -= 1
            hide text
        "No. Keep the current difficulty":
            hide text
    hide brawler_tutorial_0 with dissolve
    jump sports101_fight_menu
else:
    jump sports101_fight_menu

label sports101_fight1_store:
show screen newmoneymsg
$ ui.imagebutton("sports_menu_bg2", "sports_menu_bg2", clicked=ui.returns("FAIL"), xpos=-1 * persistent.scale_factor, ypos=-100 * persistent.scale_factor)
$ ui.imagebutton("sports_ok", "sports_ok_hover", clicked=ui.returns("OK"), xpos=635 * persistent.scale_factor, ypos=900 * persistent.scale_factor)
$ ui.imagebutton("roundhouse_icon", "roundhouse_icon", clicked=ui.returns("FAIL"), xpos=645 * persistent.scale_factor, ypos=145 * persistent.scale_factor)
$ ui.textbutton("{color=#ffffff}Roundhouse kick ({color=#36ca2b}$$${/color}):{size=-%d}\n- Enable powerful attacks\n- Cooldown 2 turns{/size}{/color}" % (5 * persistent.scale_factor), clicked=ui.returns("FAIL"), xpos=800 * persistent.scale_factor, ypos=150 * persistent.scale_factor)
$ ui.imagebutton("heal_icon", "heal_icon", clicked=ui.returns("FAIL"), xpos=645, ypos=300)
$ ui.textbutton("{color=#ffffff}Healing skill ({color=#36ca2b}$${/color}):{size=-%d}\n- Heal for +50 HP\n- Once per fight{/size}{/color}" % (5 * persistent.scale_factor), clicked=ui.returns("FAIL"), xpos=800 * persistent.scale_factor, ypos=305 * persistent.scale_factor)
$ ui.imagebutton("counter_icon", "counter_icon", clicked=ui.returns("FAIL"), xpos=645, ypos=450)
$ ui.textbutton("{color=#ffffff}Counterattack ({color=#36ca2b}$$${/color}):{size=-%d}\n- Enable counterattacks{/size}{/color}" % (5 * persistent.scale_factor), clicked=ui.returns("FAIL"), xpos=800 * persistent.scale_factor, ypos=470 * persistent.scale_factor)
$ ui.textbutton("{color=#ffffff}1 skill point ({color=#36ca2b}${/color}){/color}", clicked=ui.returns("FAIL"), xpos=645 * persistent.scale_factor, ypos=610 * persistent.scale_factor)
$ ui.textbutton("{color=#ffffff}1 skill point ({color=#36ca2b}$${/color}){/color}", clicked=ui.returns("FAIL"), xpos=645 * persistent.scale_factor, ypos=700 * persistent.scale_factor)
$ ui.textbutton("{color=#ffffff}1 skill point ({color=#36ca2b}$$${/color}){/color}", clicked=ui.returns("FAIL"), xpos=645 * persistent.scale_factor, ypos=790 * persistent.scale_factor)

if sports_roundhouse_skill:
    $ ui.imagebutton("sports_sold", "sports_sold", clicked=ui.returns("FAIL"), xpos=1160 * persistent.scale_factor, ypos=180 * persistent.scale_factor)
elif money > 2:
    $ ui.imagebutton("sports_buy", "sports_buy_hover", clicked=ui.returns("ROUNDHOUSE"), xpos=1160 * persistent.scale_factor, ypos=180 * persistent.scale_factor)
else:
    $ ui.imagebutton("sports_buy_disabled", "sports_buy_disabled", clicked=ui.returns("FAIL"), xpos=1160 * persistent.scale_factor, ypos=180 * persistent.scale_factor)

if sports_heal_skill:
    $ ui.imagebutton("sports_sold", "sports_sold", clicked=ui.returns("FAIL"), xpos=1160 * persistent.scale_factor, ypos=340 * persistent.scale_factor)
elif money > 1:
    $ ui.imagebutton("sports_buy", "sports_buy_hover", clicked=ui.returns("HEAL"), xpos=1160 * persistent.scale_factor, ypos=340 * persistent.scale_factor)
else:
    $ ui.imagebutton("sports_buy_disabled", "sports_buy_disabled", clicked=ui.returns("FAIL"), xpos=1160 * persistent.scale_factor, ypos=340 * persistent.scale_factor)

if sports_counter_skill:
    $ ui.imagebutton("sports_sold", "sports_sold", clicked=ui.returns("FAIL"), xpos=1160 * persistent.scale_factor, ypos=490 * persistent.scale_factor)
elif money > 2:
    $ ui.imagebutton("sports_buy", "sports_buy_hover", clicked=ui.returns("COUNTER"), xpos=1160 * persistent.scale_factor, ypos=490 * persistent.scale_factor)
else:
    $ ui.imagebutton("sports_buy_disabled", "sports_buy_disabled", clicked=ui.returns("FAIL"), xpos=1160 * persistent.scale_factor, ypos=490 * persistent.scale_factor)

if sports_store_sp1 or bonusPointsSports == 12:
    $ ui.imagebutton("sports_sold", "sports_sold", clicked=ui.returns("FAIL"), xpos=1160 * persistent.scale_factor, ypos=610 * persistent.scale_factor)
elif money > 0:
    $ ui.imagebutton("sports_buy", "sports_buy_hover", clicked=ui.returns("SP1"), xpos=1160 * persistent.scale_factor, ypos=610 * persistent.scale_factor)
else:
    $ ui.imagebutton("sports_buy_disabled", "sports_buy_disabled", clicked=ui.returns("FAIL"), xpos=1160 * persistent.scale_factor, ypos=610 * persistent.scale_factor)

if sports_store_sp2 or bonusPointsSports == 12:
    $ ui.imagebutton("sports_sold", "sports_sold", clicked=ui.returns("FAIL"), xpos=1160 * persistent.scale_factor, ypos=700 * persistent.scale_factor)
elif money > 1:
    $ ui.imagebutton("sports_buy", "sports_buy_hover", clicked=ui.returns("SP2"), xpos=1160 * persistent.scale_factor, ypos=700 * persistent.scale_factor)
else:
    $ ui.imagebutton("sports_buy_disabled", "sports_buy_disabled", clicked=ui.returns("FAIL"), xpos=1160 * persistent.scale_factor, ypos=700 * persistent.scale_factor)

if sports_store_sp3 or bonusPointsSports == 12:
    $ ui.imagebutton("sports_sold", "sports_sold", clicked=ui.returns("FAIL"), xpos=1160 * persistent.scale_factor, ypos=790 * persistent.scale_factor)
elif money > 2:
    $ ui.imagebutton("sports_buy", "sports_buy_hover", clicked=ui.returns("SP3"), xpos=1160 * persistent.scale_factor, ypos=790 * persistent.scale_factor)
else:
    $ ui.imagebutton("sports_buy_disabled", "sports_buy_disabled", clicked=ui.returns("FAIL"), xpos=1160 * persistent.scale_factor, ypos=790 * persistent.scale_factor)

$ result = ui.interact()
if result == "OK":
    hide screen newmoneymsg
    jump sports101_fight_menu
elif result == "ROUNDHOUSE":
    $ mny(-3)
    $ sports_roundhouse_skill = True
elif result == "COUNTER":
    $ mny(-3)
    $ sports_counter_skill = True
elif result == "HEAL":
    $ mny(-2)
    $ sports_heal_skill = True
elif result == "SP1":
    $ bonusPointsSports += 1
    $ mny(-1)
    $ sports_store_sp1 = True
elif result == "SP2":
    $ bonusPointsSports += 1
    $ mny(-2)
    $ sports_store_sp2 = True
elif result == "SP3":
    $ bonusPointsSports += 1
    $ mny(-3)
    $ sports_store_sp3 = True

jump sports101_fight1_store

label sports101_fight1_opponent:
show screen scr_sports101_opponents
$ ui.imagebutton("sports_easy","sports_easy", clicked=ui.returns("FAIL"), xpos=230 * persistent.scale_factor, ypos=50 * persistent.scale_factor)
$ ui.imagebutton("sports_normal","sports_normal", clicked=ui.returns("FAIL"), xpos=775 * persistent.scale_factor, ypos=50 * persistent.scale_factor)
$ ui.imagebutton("sports_hard","sports_hard", clicked=ui.returns("FAIL"), xpos=1320 * persistent.scale_factor, ypos=50 * persistent.scale_factor)
$ ui.imagebutton("sports_you","sports_you", clicked=ui.returns("FAIL"), xpos=775 * persistent.scale_factor, ypos=490 * persistent.scale_factor)

$ sports_tmp_hover = "".join([sports_opponents[2],str(cpu_hp_state)]) + "_hover"
if sports_opponent_idx == 0:
    $ ui.imagebutton(sports_tmp_hover, sports_tmp_hover, clicked=ui.returns("EASY"), xpos=210 * persistent.scale_factor, ypos=150 * persistent.scale_factor)
else:
    $ ui.imagebutton("".join([sports_opponents[2],str(cpu_hp_state)]), sports_tmp_hover, clicked=ui.returns("EASY"), xpos=210 * persistent.scale_factor, ypos=150 * persistent.scale_factor)

$ sports_tmp_hover = "".join([sports_opponents[5],str(cpu_hp_state)]) + "_hover"
if sports_opponent_idx == 1:
    $ ui.imagebutton(sports_tmp_hover, sports_tmp_hover, clicked=ui.returns("NORMAL"), xpos=755 * persistent.scale_factor, ypos=150 * persistent.scale_factor)
else:
    $ ui.imagebutton("".join([sports_opponents[5],str(cpu_hp_state)]), sports_tmp_hover, clicked=ui.returns("NORMAL"), xpos=755 * persistent.scale_factor, ypos=150 * persistent.scale_factor)

$ sports_tmp_hover = "".join([sports_opponents[8],str(cpu_hp_state)]) + "_hover"
if sports_opponent_idx == 2:
    $ ui.imagebutton(sports_tmp_hover, sports_tmp_hover, clicked=ui.returns("HARD"), xpos=1300 * persistent.scale_factor, ypos=150 * persistent.scale_factor)
else:
    $ ui.imagebutton("".join([sports_opponents[8],str(cpu_hp_state)]), sports_tmp_hover, clicked=ui.returns("HARD"), xpos=1300 * persistent.scale_factor, ypos=150 * persistent.scale_factor)

$ ui.imagebutton("sports_avatar_mc", "sports_avatar_mc", clicked=ui.returns("FAIL"), xpos=755 * persistent.scale_factor, ypos=590 * persistent.scale_factor)

if brawler_money_available:
    $ ui.imagebutton("sports_reward_money", "sports_reward_money", clicked=ui.returns("FAIL"), xpos=230 * persistent.scale_factor, ypos=420 * persistent.scale_factor)
else:
    $ ui.imagebutton("sports_no_reward", "sports_no_reward", clicked=ui.returns("FAIL"), xpos=230 * persistent.scale_factor, ypos=420 * persistent.scale_factor)
if brawler_render_available:
    $ ui.imagebutton("sports_reward_render", "sports_reward_render", clicked=ui.returns("FAIL"), xpos=768 * persistent.scale_factor, ypos=420 * persistent.scale_factor)
else:
    $ ui.imagebutton("sports_no_reward", "sports_no_reward", clicked=ui.returns("FAIL"), xpos=768 * persistent.scale_factor, ypos=420 * persistent.scale_factor)
if brawler_skillpoint_available and bonusPointsSports <12:
    $ ui.imagebutton("sports_reward_skillpoint", "sports_reward_skillpoint", clicked=ui.returns("FAIL"), xpos=1320 * persistent.scale_factor, ypos=420 * persistent.scale_factor)
elif brawler_skillpoint_available:
    $ ui.imagebutton("sports_reward_money", "sports_reward_money", clicked=ui.returns("FAIL"), xpos=1320 * persistent.scale_factor, ypos=420 * persistent.scale_factor)
else:
    $ ui.imagebutton("sports_no_reward", "sports_no_reward", clicked=ui.returns("FAIL"), xpos=1320 * persistent.scale_factor, ypos=420 * persistent.scale_factor)

$ ui.imagebutton("sports_ok", "sports_ok_hover", clicked=ui.returns("OK"), xpos=635 * persistent.scale_factor, ypos=900 * persistent.scale_factor)
$ result = ui.interact()
if result == "OK":
    hide screen scr_sports101_opponents
    jump sports101_fight_menu
elif result == "EASY":
    $ sports_opponent_idx = 0
elif result == "NORMAL":
    $ sports_opponent_idx = 1
elif result == "HARD":
    $ sports_opponent_idx = 2

jump sports101_fight1_opponent

label sports101_fight1_skills:
show sports101_arena_skills
show screen scr_sports101_skills
$ ui.imagebutton("sports_skills[sports_pow]", "sports_skills[sports_pow]", clicked=ui.returns("FAIL"), xpos=420 * persistent.scale_factor, ypos=240 * persistent.scale_factor)
$ ui.imagebutton("sports_skills[sports_dex]", "sports_skills[sports_dex]", clicked=ui.returns("FAIL"), xpos=1230 * persistent.scale_factor, ypos=240 * persistent.scale_factor)
$ ui.imagebutton("sports_skills[sports_hp]", "sports_skills[sports_hp]", clicked=ui.returns("FAIL"), xpos=420 * persistent.scale_factor, ypos=650 * persistent.scale_factor)
$ ui.imagebutton("sports_skills[sports_mov]", "sports_skills[sports_mov]", clicked=ui.returns("FAIL"), xpos=1230 * persistent.scale_factor, ypos=650 * persistent.scale_factor)

$ sports_skillpointsleft = bonusPointsSports + 4 - sports_pow - sports_dex - sports_hp - sports_mov
if sports_skillpointsleft > 0 and sports_pow < 4:
    $ ui.imagebutton("sports_plus", "sports_plus_hover", clicked=ui.returns("addPOW"), xpos=730 * persistent.scale_factor, ypos=257 * persistent.scale_factor)
else:
    $ ui.imagebutton("sports_plus_disabled", "sports_plus_disabled", clicked=ui.returns("NULL"), xpos=730 * persistent.scale_factor, ypos=257 * persistent.scale_factor)
if sports_pow > 1:
    $ ui.imagebutton("sports_minus", "sports_minus_hover", clicked=ui.returns("subPOW"), xpos=310 * persistent.scale_factor, ypos=260 * persistent.scale_factor)
else:
    $ ui.imagebutton("sports_minus_disabled", "sports_minus_disabled", clicked=ui.returns("NULL"), xpos=310 * persistent.scale_factor, ypos=260 * persistent.scale_factor)
if sports_skillpointsleft > 0  and sports_dex < 4:
    $ ui.imagebutton("sports_plus", "sports_plus_hover", clicked=ui.returns("addDEX"), xpos=1540 * persistent.scale_factor, ypos=257 * persistent.scale_factor)
else:
    $ ui.imagebutton("sports_plus_disabled", "sports_plus_disabled", clicked=ui.returns("NULL"), xpos=1540 * persistent.scale_factor, ypos=257 * persistent.scale_factor)
if sports_dex > 1:
    $ ui.imagebutton("sports_minus", "sports_minus_hover", clicked=ui.returns("subDEX"), xpos=1120 * persistent.scale_factor, ypos=260 * persistent.scale_factor)
else:
    $ ui.imagebutton("sports_minus_disabled", "sports_minus_disabled", clicked=ui.returns("NULL"), xpos=1120 * persistent.scale_factor, ypos=260 * persistent.scale_factor)
if sports_skillpointsleft > 0  and sports_hp < 4:
    $ ui.imagebutton("sports_plus", "sports_plus_hover", clicked=ui.returns("addHP"), xpos=730 * persistent.scale_factor, ypos=667 * persistent.scale_factor)
else:
    $ ui.imagebutton("sports_plus_disabled", "sports_plus_disabled", clicked=ui.returns("NULL"), xpos=730 * persistent.scale_factor, ypos=667 * persistent.scale_factor)
if sports_hp > 1:
    $ ui.imagebutton("sports_minus", "sports_minus_hover", clicked=ui.returns("subHP"), xpos=310 * persistent.scale_factor, ypos=670 * persistent.scale_factor)
else:
    $ ui.imagebutton("sports_minus_disabled", "sports_minus_disabled", clicked=ui.returns("NULL"), xpos=310 * persistent.scale_factor, ypos=670 * persistent.scale_factor)
if sports_skillpointsleft > 0  and sports_mov < 4:
    $ ui.imagebutton("sports_plus", "sports_plus_hover", clicked=ui.returns("addMOV"), xpos=1540 * persistent.scale_factor, ypos=667 * persistent.scale_factor)
else:
    $ ui.imagebutton("sports_plus_disabled", "sports_plus_disabled", clicked=ui.returns("NULL"), xpos=1540 * persistent.scale_factor, ypos=667 * persistent.scale_factor)
if sports_mov > 1:
    $ ui.imagebutton("sports_minus", "sports_minus_hover", clicked=ui.returns("subMOV"), xpos=1120 * persistent.scale_factor, ypos=670 * persistent.scale_factor)
else:
    $ ui.imagebutton("sports_minus_disabled", "sports_minus_disabled", clicked=ui.returns("NULL"), xpos=1120 * persistent.scale_factor, ypos=670 * persistent.scale_factor)
$ ui.imagebutton("sports_ok", "sports_ok_hover", clicked=ui.returns("OK"), xpos=635 * persistent.scale_factor, ypos=870 * persistent.scale_factor)
$ result = ui.interact()

if result == "addPOW":
    $ sports_pow += 1
elif result == "addDEX":
    $ sports_dex += 1
elif result == "addHP":
    $ sports_hp += 1
elif result == "addMOV":
    $ sports_mov += 1
elif result == "subPOW":
    $ sports_pow -= 1
elif result == "subDEX":
    $ sports_dex -= 1
elif result == "subMOV":
    $ sports_mov -= 1
elif result == "subHP":
    $ sports_hp -= 1
elif result == "OK":
    $ sports_pc_hp = 90 + 10 * sports_hp
    hide screen scr_sports101_skills
    jump sports101_fight_menu
jump sports101_fight1_skills

label sports_fight1_quit:
stop music fadeout 2
$ loopFightMusic = False
$ renpy.pause(2.0)
$ queueChanCallback()
show screen new_phone_screen
if brawlerStoryFight == "":
    show screen mphone_screen
$ mphone_next_song()
$ map_fast_travel_enabled = True
$ renpy.jump(currentFreeRoamLabel)

screen brawler_unavailable_screen:
    tag brawler_unavailable_screen
    modal True
    fixed:
        at mphone_app_transform
        add "mphone_brawler_unavailable_bg"
    if persistent.golden_phone and persistent.golden_phone_skin_enabled:
        add "mphone_shell_gold"
    else:
        add "mphone_shell"
    key "mouseup_2" action Hide("brawler_unavailable_screen")

    fixed:
        at mphone_app_transform

        imagebutton at mphone_off_transform:
            idle "mphone_off_circle_idle"
            hover "mphone_off_circle_hover"
            action Hide("brawler_unavailable_screen")
            xalign 0.5
            yalign mphone_off_yalign
        hbox:
            xalign 0.5
            yalign 0.06
            spacing 300 * persistent.scale_factor
            add "mphone_top_cakenet"
            add "mphone_top_icons"
        add "mphone_fg"
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
