label splashscreen:
    if steamConfig:
        $ persistent.steam_owns_badik = is_subscribed_app_badik()
        $ persistent.steam_owns_al = is_subscribed_app_al()
        $ persistent.steam_owns_guide_s1 = is_subscribed_app_guide_s1()
        $ persistent.steam_owns_s2 = is_subscribed_app_s2()
        $ persistent.steam_owns_guide_s2 = is_subscribed_app_guide_s2()
        $ persistent.steam_owns_s3 = is_subscribed_app_s3()
        $ persistent.steam_owns_guide_s3 = is_subscribed_app_guide_s3()
    else:
        if is_subscribed_app_badik() or is_subscribed_app_al() or is_subscribed_app_s2():
            $ renpy.quit()
    if not steamConfig:
        scene black
        play sound "gui/pinkcake_sound.mp3"
        $ renpy.movie_cutscene("gui/pinkcake_video.webm")
        stop sound
        scene black with dissolve
    if not persistent.default_text_box_mode:
        $ style.window.background = Image("gui/textbox_new.png", xalign=0.5, yalign=1.0)
        $ style.say_dialogue.xsize = 950
        $ style.say_dialogue.xpos = 498
        $ style.say_dialogue.xalign = 0.5
        $ style.say_dialogue.text_align = 0.5
        $ style.say_dialogue.xoffset = 0
        $ style.namebox.xalign=0.5
        $ style.say_label.xoffset = 0
        $ style.say_label.text_align = 0.5
        $ style.say_label.xalign = 0.5
        $ style.rebuild()
    window hide
    $ persistent.current_episode = 0

    play music persistent.mm_song[1]
    if not steamConfig:
        scene black with Pause(1)
    show game_warning with dissolve
    $ renpy.pause()
    if steamConfig:
        show legal_info_steam_version with dissolve
    elif nonPatreonConfig:
        show legal_info with dissolve
        $ renpy.pause()
        show gog_screen with dissolve
        hide legal_info with dissolve
    else:
        show legal_info_patreon_version with dissolve
    $ renpy.pause()
    show ai_disclaimer with dissolve
    $ renpy.pause()
    scene black with dissolve
    with Pause(0.5)
    if persistent.default_text_box_mode:
        $ pick_style_default()
    else:
        $ pick_style_centered()
    $ _preferences.gl_powersave = False
    return

init python:
    import math
    def name_func(newstring):
        store.name = newstring
        renpy.restart_interaction()
    def sname_func(newstring):
        store.name = newstring
        renpy.restart_interaction()

init python:



    def steamConfig_save(d):
        d["badik_chapter"] = badik_chapter
        d["steamConfig"] = steamConfig
        d["minigames"] = minigames
    config.save_json_callbacks = [steamConfig_save]



    achievement.Sync()

init python:
    g = Gallery()
    g.transition = dissolve

init -1 python:
    if getattr(renpy.display.get_info(), 'oldmenu', None) is None:
        renpy.display.get_info().oldmenu = renpy.exports.menu

    def menu_override(items, set_expr, args, kwargs, item_arguments):
        items = [ (renpy.exports.substitute(label) + (" (disabled)" if not renpy.python.py_eval(condition) else ""), "True", value)
                  for label, condition, value in items ]
        
        return renpy.display.get_info().oldmenu(items, set_expr)
    renpy.exports.menu = menu_override


screen s3_intro_ol_screen:
    tag s3_intro_ol_screen
    modal False
    add "s3_intro_ol"


image jill_spr_mm:
    "mm_spr_jill_fg"
    pause 2
    "spr_blank" with Dissolve(4, alpha=True)
init:
    $ config.debug_image_cache = True

    $ spr_mm_arr_s3 = []
    $ spr_mm_envy = ["mm_spr_envy_bg", 1.07, "mm_spr_envy_fg", 1.12, "spr_blank", 1.0]
    $ spr_mm_arr_s3.append(spr_mm_envy)
    $ spr_mm_isabella = ["mm_spr_isabella_bg", 1.05, "mm_spr_isabella_fg", 1.08, "spr_blank", 1.0]
    $ spr_mm_arr_s3.append(spr_mm_isabella)
    $ spr_mm_lily = ["mm_spr_lily_bg", 1.07, "mm_spr_lily_fg", 1.12, "spr_blank", 1.0]
    $ spr_mm_arr_s3.append(spr_mm_lily)
    $ spr_mm_jill = ["mm_spr_jill_bg", 1.07, "mm_spr_jill2_fg", 1.11, "jill_spr_mm", 1.11]
    $ spr_mm_arr_s3.append(spr_mm_jill)
    $ spr_mm_nora = ["mm_spr_nora_bg", 1.05, "mm_spr_nora_fg", 1.08, "spr_blank", 1.0]
    $ spr_mm_arr_s3.append(spr_mm_nora)
    $ spr_mm_sage = ["mm_spr_sage_bg", 1.05, "mm_spr_sage_fg1", 1.05, "mm_spr_sage_fg2", 1.15]
    $ spr_mm_arr_s3.append(spr_mm_sage)
    $ spr_mm_zoeys3 = ["mm_spr_zoey2_bg", 1.05, "mm_spr_zoey2_fg", 1.12, "spr_blank", 1.0]
    $ spr_mm_arr_s3.append(spr_mm_zoeys3)
    $ spr_mm_sm = ["mm_spr_sm_bg", 1.05, "mm_spr_sm_fg1", 1.08, "mm_spr_sm_fg2", 1.11]
    $ spr_mm_arr_s3.append(spr_mm_sm)
    $ spr_mm_josy = ["mm_spr_josy_bg", 1.05, "mm_spr_josy_fg", 1.12, "spr_blank", 1.0]
    $ spr_mm_arr_s3.append(spr_mm_josy)
    $ spr_mm_camila = ["mm_spr_camila_bg", 1.05, "mm_spr_camila_fg", 1.07, "spr_blank", 1.0]
    $ spr_mm_arr_s3.append(spr_mm_camila)
    $ spr_mm_cathy = ["mm_spr_cathy_bg", 1.05, "mm_spr_cathy_fg", 1.07, "spr_blank", 1.0]
    $ spr_mm_arr_s3.append(spr_mm_cathy)
    $ spr_mm_jocks = ["mm_spr_jocks_bg", 1.05, "mm_spr_jocks_fg", 1.09, "mm_spr_jocks_fg2", 1.12]
    $ spr_mm_arr_s3.append(spr_mm_jocks)
    $ spr_mm_heather = ["mm_spr_heather_bg", 1.05, "mm_spr_heather_fg", 1.09, "spr_blank", 1.0]
    $ spr_mm_arr_s3.append(spr_mm_heather)
    $ spr_mm_maya = ["mm_spr_maya_bg", 1.05, "mm_spr_maya_fg", 1.08, "spr_blank", 1.0]
    $ spr_mm_arr_s3.append(spr_mm_maya)
    $ spr_mm_pr = ["mm_spr_pinkrose_bg", 1.05, "mm_spr_pinkrose_fg", 1.08, "mm_spr_pinkrose_fg2", 1.10]
    $ spr_mm_arr_s3.append(spr_mm_pr)
    $ spr_mm_tybalt = ["mm_spr_tybalt_bg", 1.05, "mm_spr_tybalt_fg", 1.08, "spr_blank", 1.10]
    $ spr_mm_arr_s3.append(spr_mm_tybalt)
    $ spr_mm_riona = ["mm_spr_riona_bg", 1.05, "mm_spr_riona_fg", 1.08, "spr_blank", 1.10]
    $ spr_mm_arr_s3.append(spr_mm_riona)
    $ spr_mm_diks = ["mm_spr_diks_bg", 1.05, "mm_spr_diks_fg", 1.08, "spr_blank", 1.10]
    $ spr_mm_arr_s3.append(spr_mm_diks)
    $ spr_mm_quinn = ["mm_spr_quinn_bg", 1.05, "mm_spr_quinn_fg", 1.08, "spr_blank", 1.10]
    $ spr_mm_arr_s3.append(spr_mm_quinn)
    $ spr_mm_lynette = ["mm_spr_lynette_bg", 1.05, "mm_spr_lynette_fg", 1.07, "mm_spr_lynette_fg2", 1.11]
    $ spr_mm_arr_s3.append(spr_mm_lynette)
    $ renpy.random.shuffle(spr_mm_arr_s3)

    $ spr_mm_zoey = ["mm_spr_zoey_bg", 1.07, "mm_spr_zoey_fg", 1.10]
    $ spr_mm_jonah = ["mm_spr_jonah_bg", 1.07, "mm_spr_jonah_fg", 1.12]
    $ spr_mm_bret = ["mm_spr_bret_bg", 1.07, "mm_spr_bret_fg", 1.11]
    $ spr_mm_emma = ["mm_spr_emma_bg", 1.07, "mm_spr_emma_fg", 1.11]
    $ spr_mm_mc = ["mm_spr_mc_bg", 1.07, "mm_spr_mc_fg", 1.11]
    $ spr_mm_arr = [spr_mm_zoey,spr_mm_jonah,spr_mm_bret,spr_mm_emma,spr_mm_mc]
    $ renpy.random.shuffle(spr_mm_arr)

    $ musicCreditsOpen = False

    $ renpy.music.register_channel("sfx1", "sfx")
    $ renpy.music.register_channel("sfx2", "sfx")
    $ renpy.music.register_channel("sfx3", "sfx")
    $ renpy.music.register_channel("music1", "music")
    $ renpy.music.register_channel("music2", "music")
    $ renpy.music.register_channel("jill", "voice")
    $ renpy.music.register_channel("bella", "voice")
    default tutorials = True
    default notifications = True

    if persistent.josy == None:
        $ persistent.josy = "Josy"
    if persistent.maya == None:
        $ persistent.maya = "Maya"
    if persistent.sage == None:
        $ persistent.sage = "Sage"
    if persistent.isabella == None:
        $ persistent.isabella = "Isabella"
    if persistent.jill == None:
        $ persistent.jill = "Jill"
    if persistent.quinn == None:
        $ persistent.quinn = "Quinn"
    if persistent.riona == None:
        $ persistent.riona = "Riona"
    if persistent.jade == None:
        $ persistent.jade = "Jade"
    if persistent.cathy == None:
        $ persistent.cathy = "Cathy"
    if persistent.camila == None:
        $ persistent.camila = "Camila"
    if persistent.current_save_name == None:
        $ persistent.current_save_name = ""
    if persistent.golden_phone == None:
        $ persistent.golden_phone = False
    if persistent.golden_phone_skin_enabled == None:
        $ persistent.golden_phone_skin_enabled = False

    if persistent.save_transfer_tutorial == None:
        $ persistent.save_transfer_tutorial = False
    if persistent.default_text_box_mode == None:
        $ persistent.default_text_box_mode = True

    if persistent.map_fast_travel == None:
        $ persistent.map_fast_travel = True
    $ config.autosave_on_choice = False
    if persistent.autosave == None:
        $ persistent.autosave = True
    if persistent.colorblind == None:
        $ persistent.colorblind = False
    $ config.has_autosave = persistent.autosave
    default new_art_girl_name_list = ["Camila","Cathy","Envy","Isabella","Jade","Jill","Josy","Lily","Maya","Melanie","Nora","Quinn","Riona","Sage","Sarah","Zoey"]
label season3_header_label:
default afterDerekShopLabel = ""
default afterMagnarShopLabel = ""
default afterQuinnShopLabel = ""
default brawlerStoryFight = ""
default brawlerStoryFightLabel = ""
default brawler_money_available = False
default brawler_render_available = False
default brawler_skillpoint_available = False
default bonusPercentageEnglish = 0
default bonusPercentageMath = 0
default currentEpisode = 8
default currentEvent = ""
default currentFreeRoamLabel = ""
default currentImage = ""
default currentTextBrowserFile = ""
default currentWallpaperPage = 0
default currentWallpaperPreview = 0
default current_2d_girl = 0
default current_girl_2d = 0
default current_task = ""
default dikfolder_objects = 0
default dikfolder_path = "Desktop > DIK folder"
default disabled_apps = []
default eco_bricks = []
default eco_current_hole = 0
default eco_moveable = [False, False, False, False, False, False, False, False, False]
default eco_shf = [0,1,2,3,4,5,6,7,8]
default eco_wrongs = 0
default englishTestScore = 0
default wallpapers = 0
default game_money_available = False
default guideCurrentPage = 1
default guideSuggestedPage = 1
default loopFightMusic = False
default map_fast_travel_enabled = True
default map_system_list = []
default max_page_walkthrough = 369
default menuGalleryOpen = False
define mphone_app_grid_yalign = 0.85
default mphone_bios_app_exception = False
default mphone_current_pet_name = ""
default mphone_genre_count = 0
define mphone_genre_list = ["All","Rock","Party","Relaxing","Favorites"]
define mphone_music_bar_position = 0.6
default mphone_music_genre = 0
default mphone_new_art_available = False
default mphone_new_contact_event = False
default mphone_next_state = []
default mphone_notification_count = 0
define mphone_off_yalign = 0.957
default mphone_pq_img = ""
default mphone_replies = []
default mphone_shop_active = False
default mphone_text_frame = ["chat_mc_box","chat_mc_box","chat_mc_box","chat_mc_box"]
default mphones_emotes = [["mphone_emoji_angry",False],["mphone_emoji_cool",False],["mphone_emoji_cry",False],["mphone_emoji_evil",False],["mphone_emoji_heart",False],["mphone_emoji_kiss",False],["mphone_emoji_laugh",False],["mphone_emoji_sad",False],["mphone_emoji_smile",False],["mphone_emoji_surprised",False],["mphone_emoji_tongue",False],["mphone_emoji_eggplant",False]]

default new_rooster_int = 0
default optional_task_list = []
default pack_quest_active = False
default pack_quest_available = False
default previousEpLabel = ""

default mphone_pp_history_list = []
define roosterNickAlex = "Alex@OnePunchAlex"
define roosterNickAnthony = "Anthony@BigA"
define roosterNickArieth = "Arieth@AriethPassword1234"
define roosterNickAshley = "Ashley@JustAsh"
define roosterNickBert = "Bert@Thalidomide"
define roosterNickBeth = "Beth@MoreThanJustAWaitress"
define roosterNickBrandi = "Brandi@MochaLatte"
define roosterNickBurke = "Burke@ProfessorStephenBurke"
define roosterNickCaleb = "Caleb@FeelThePump"
define roosterNickCamila = "Camila@Cammy"
define roosterNickCathy = "Cathy@CathyJones79"
define roosterNickChad = "Chad@MadLadChad"
define roosterNickChristian = "Christian@PlayOnPlayer"
define roosterNickDany = "Dany@BunnyHop"
define roosterNickDawe = "Dawe@BigDickDawe"
define roosterNickDerek = "Derek@BigBootyLover"
define roosterNickDik = "DIKsOfficial@DIKsOfficial"
define roosterNickElena = "Elena@CuteButt"
define roosterNickEnvy = "Nicole@TwoToTango"
define roosterNickEugene = "Eugene@MrDynamite"
define roosterNickGordon = "Gordon@Diamonds"
define roosterNickHeather = "Heather@HOTHeather"
define roosterNickIsabella = "Isabella@IsabellaRoberts"
define roosterNickJacob = "Jacob@DIKJacob"
define roosterNickJade = "Jade@DrJadeBurke"
define roosterNickJill = "Jill@EbonyAndIvory"
define roosterNickJimmy = "Jimmy@Chevy69"
define roosterNickJohn = "John@MilkMan"
define roosterNickJohnBoy = "JohnBoy@DIKJB"
define roosterNickJosy = "Josy@MsSunshine"
define roosterNickLeon = "Leon@DIKLeon"
define roosterNickLily = "Lily@LikeTheFlower"
define roosterNickLucas = "Lucas@TheThird"
define roosterNickMagnar = "Magnar@SirMagnar"
define roosterNickMaya = "Maya@MayaTheMoviebuff"
define roosterNickMelanie = "Melanie@CaraMel"
define roosterNickMinny = "Minny@FemGirlPower"
define roosterNickMona = "Mona@MonaLisa"
define roosterNickNick = "Nick@DIKNick"
define roosterNickOliver = "Oliver@Buttons"
define roosterNickQuinn = "Quinn@QuinnOfHearts"
define roosterNickRich = "Rich@IAmRich"
define roosterNickRiona = "Riona@HOTRiona"
define roosterNickRon = "Ron@MegatRon"
define roosterNickRose = "Rose@GinAndTonic"
define roosterNickRusty = "Rusty@DIKPresidentRusty"
define roosterNickSage = "Sage@HOTPresidentSage"
define roosterNickSally = "Sally@Sallycylic"
define roosterNickSandy = "Sandy@RazorKitty"
define roosterNickSarah = "Sarah@HOTSarah"
define roosterNickTania = "Tania@Tania420"
define roosterNickTommy = "Tommy@DIKTommyTheDestroyer"
define roosterNickTrent = "Trent@LordTrent"
define roosterNickTroy = "Troy@FingerRoll"
define roosterNickTybalt = "Tybalt@PresidentTybaltBurke"
define roosterNickWendy = "Wendy@TheRealestWoman"
default roosterNickDarius = "Darius@DaBeast"
default roosterNickBianca = "Bianca@BiancaThomson"
default roosterNickBecky = "Becky@InStyle"
default roosterNickTyballs = "Tyballs@PresidentTyballs"
default roosterNickZoey = "Zoey@Kickflip"

default roosterState = ""
default specialMessage = ""
default sports_cpu_hp = 0
default sports_cpu_pow = 0
default sports_cpu_dex = 0
default sports_cpu_mov = 0
default sports_opponent_idx = 0
default sports_opponents = ["Nerd", "#c700dd", "sports_avatar_nerd", "Prep", "#87fa5a", "sports_avatar_prep", "Jock", "#23b4fc", "sports_avatar_jock", "Chad", "#23b4fc", "sports_avatar_chad", "Troy", "#ff0000", "sports_avatar_troy"]
default task_list = []
default task_state_list = []
default tmpAppList = []
default tmpdik = 0
default toggled_2d_mode = 1
default vault_unlocked = False

default phone_opened = False
default chat_new_tasks = False
default new_cluck = False
default chat_new_rewards = False
default chat_new_stats = False
default chat_new_bios = False
default safe_new_renders = False
default triple_tile_money_available = False
default mp_slot_hover = -1
default mp_slot = -1
default mphone_current_input = ""
default pet_reset = ""
default safe_digits = [0,0,0,0]
default pq_open_animation = False
default foundCards = 0
default unlockedScenes = 0
default foundWallpapers = 0
default roosterCurrentIdx = 0

default sports_tutorial = True
default mphone_stats_girl_log_s3 = []
default mphone_stats_unlocked_state = 0

default rew_josy_total_sum = 0
default rew_maya_total_sum = 0
default rew_sage_total_sum = 0
default rew_lily_total_sum = 0
default rew_zoey_total_sum = 0
default rew_cam_total_sum = 0
default rew_isa_total_sum = 0
default rew_jill_total_sum = 0
default rew_mixed_total_sum = 0
default rew_2d_total_sum = 0

default rew_josy_unlocked_sum = 0
default rew_maya_unlocked_sum = 0
default rew_sage_unlocked_sum = 0
default rew_zoey_unlocked_sum = 0
default rew_lily_unlocked_sum = 0
default rew_isa_unlocked_sum = 0
default rew_cam_unlocked_sum = 0
default rew_jill_unlocked_sum = 0
default rew_2d_unlocked_sum = 0
default rew_mixed_unlocked_sum = 0


if persistent.episode_interlude == None:
    $ persistent.episode_interlude = False

$ qM = quick_menu
$ quick_menu = 0

jump header_udpate_epi_label

init -1:
    $ _preferences.show_empty_window = False
    $ musicCreditsOpen = False
    default tmpInt = 0
    default tmpInt2 = 0
    default tmpBool2 = 0
    default tmpBool3 = False
    default tmpMouse = True
    default minigames = True
    default steamAchievements = False
    default steamConfig = False
    default nonPatreonConfig = False
    default mphone_notifications = [["Standard","sound_effects/message.mp3"],["Beep","sound_effects/season2/beep.mp3"],["Melody","sound_effects/season2/melody.mp3"],["Vibrate","sound_effects/season2/vibrate.mp3"]]
    default steamImport = False
    if persistent.firstTimePlayingS3 == None:
        $ persistent.firstTimePlayingS3 = True
    if persistent.sex_sounds_volume == None:
        $ persistent.sex_sounds_volume = 1.0
    default changelog_list = ""
    default randInt = 0

init python:
    def is_subscribed_app_badik():
        return is_subscribed_app(1126320)
    def is_subscribed_app_al():
        return is_subscribed_app(1045520)
    def is_subscribed_app_guide_s1():
        return is_subscribed_app(1223490)
    def activate_overlay_to_store_al():
        activate_overlay_to_store(1045520, 0)
    def activate_overlay_to_store_badik():
        activate_overlay_to_store(1126320, 0)
    def activate_overlay_to_store_badik_s1_guide():
        activate_overlay_to_store(1223490, 0)
    def activate_overlay_to_store_badik_s2():
        activate_overlay_to_store(1215820, 0)
    def activate_overlay_to_store_badik_s2_guide():
        activate_overlay_to_store(1631620, 0)
    def activate_overlay_to_store_badik_s3():
        activate_overlay_to_store(1807120, 0)
    def activate_overlay_to_store_badik_s3_guide():
        activate_overlay_to_store(2220920, 0)
    def is_subscribed_app_s2():
        return is_subscribed_app(1215820)
    def is_subscribed_app_guide_s2():
        return is_subscribed_app(1631620)
    def is_subscribed_app_s3():
        return is_subscribed_app(1807120)
    def is_subscribed_app_guide_s3():
        return is_subscribed_app(2220920)
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
