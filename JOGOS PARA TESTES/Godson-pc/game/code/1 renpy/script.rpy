default quest = Manager()




default player_languages_raw = ""
default player_languages = []
default sexwithmarnie = False
default fooledaroundwithmarnie = False
default triedtogetmarnieupstairs = False
default marnie_first_night_invite_route = ""
default secret1 = False
default landsing = False
default shit = False
default website = False
default picture = False
default liedaboutwebsite = False
default metlorrainegood = False
default metlorrainebad = False
default nevermetlorraine = False
default marniegirlfriend = False
default sexwithlorraine = False
default sexwithsuccubus = False
default ntr = False
default evil = False
default good = False
default superevil = False
default supergood = False
default netural = False
default sexaddict = False
default readmind = False
default earlytruth = False
default angry_counter = 0
default sex_counter = 0
default kyle_counter = 0
default pissedlorraineoff = False
default ultmilf = False
default foundoutmarniecheated = False
default gotfreakywithmarthaonfirstnight = False
default respectfultomartha = False
default freedfather = False
default nicetovictoria = False
default ragefuckedlorraine = False
default firstmetmarnietits = False
default toldlorraineaboutsuccubus = False
default sawyouwithher = False
default huggedmarnieback = False
default jenniferfeelspecialbirthday = False
default marnieoweyougoodpizza = False
default didntslaplorraine = False
default calledgilf = False
default pissedoffkyle = False
default toldmarnieyoulovedher = False
default marniefriendswithbenefits = False
default marniemakeout = False
default marniestare = False
default lorrainerap = False
default marniehen3 = False
default marniehen4 = False
default marniehen5 = False
default rde = False
default donezo = False
default deniedjennifer = False
default marniefingersinmouth = False
default metjennifer = False
default marns = False
default marne = False
default marnt = False
default yikes_choices_locked = False
default notmom1 = False
default yunimom1 = False
default resisted_yuni_once = False
default asked_who_am_i = False
default asked_who_are_they = False
default asked_where_father = False
default yuni_video_completed = False
default yuni_video_failed = False
default yuni_video_refused = False
default marnie_interview_watched = False
default marnie_interview_stopped = False
default marnie_boss_attacked = False
default marnie_aftermath_explained = False
default marnie_aftermath_gave_in = False
default nina_guilt_success = False
default nina_guilt_bad_opening_used = False
default nina_left_for_appointment = False
default thought1 = False
default thought2 = False
default thought3 = False
default thought4 = False
default thought5 = False


default supergood_refused_yuni = False
default supergood_devotion_started = False
default lorraine_makeout_attempts = 0


default jennifer_makeout_count = 0



default memory_chose_good_path = False
default memory_chose_evil_path = False
default memory_chose_sexaddict_path = False
default memory_marnie_contact_added = False
default memory_marnie_noticed_stare = False
default memory_marnie_compassion = False
default memory_marnie_cruelty = False
default memory_marnie_backed_away = False
default memory_marnie_kiss = False
default memory_jennifer_followed = False
default memory_jennifer_resisted = False
default memory_jennifer_called_mommy = False
default memory_jennifer_loves_makeout = False
default memory_jennifer_thinks_you_love_her = False
default memory_lorraine_respectful_approach = False
default memory_lorraine_intruded = False
default memory_lorraine_praised = False
default memory_lorraine_secret_uncovered = False
default memory_lorraine_intimacy = False
default memory_yuni_first_impression = False
default memory_yuni_resisted = False
default memory_yuni_accepted_princess_title = False
default memory_yuni_video_helped = False
default memory_yuni_video_refused = False
default memory_yuni_music_failed = False
default memory_martha_treatment = False
default memory_henry_agreed_to_help = False
default memory_henry_stood_by_and_watched = False
default memory_marnie_intervened = False
default memory_henry_boss_attacked = False
default memory_marnie_explanation = False
default memory_marnie_aftermath = False
default memory_nina_patience = False
default memory_nina_pressured = False
default memory_nina_crossed_line = False
default memory_henry_helped = False
default memory_lorraine_honesty = False
default memory_nina_is_boyfriend = False
default memory_nina_is_not_boyfriend = False
default memory_nina_hates_you = False
default memory_nina_wait_response = False
default memory_gianna_paid = False
default memory_gianna_propositioned = False
default memory_gianna_preview_demanded = False
default memory_santa_revealed_to_myles_gianna = False
default memory_myles_warned_off_martha = False
default memory_myles_permission_martha = False
default memory_martha_invited_to_dance = False

default chi = False

default preferences.wait_voice = True
default preferences.voice_after_game_menu = True


init python:

    def normalize_player_languages(raw_value):
        """Return a clean, case-insensitively de-duplicated language list."""
        normalized = []
        seen = set()
        
        for entry in (raw_value or "").split(","):
            language_name = " ".join(entry.strip().split())
            
            if not language_name:
                continue
            
            duplicate_key = language_name.casefold()
            
            if duplicate_key in seen:
                continue
            
            seen.add(duplicate_key)
            normalized.append(language_name)
        
        return normalized

    def player_knows_language(language_name):
        """Case-insensitive story check for a language entered by the player."""
        target = " ".join((language_name or "").strip().split()).casefold()
        return bool(target) and any(
        saved_language.casefold() == target
        for saved_language in player_languages
    )

    def supergood_restraint_ready():
        """True only when the player preserved the hidden Lorraine-only path."""
        
        return bool(
        good
        and not evil
        and not sexaddict
        and not superevil
        and not supergood
        and memory_jennifer_resisted
        and not memory_jennifer_called_mommy
        and memory_lorraine_praised
        and supergood_refused_yuni
        and not memory_yuni_video_helped
        and not sexwithmarnie
        and not fooledaroundwithmarnie
        and not triedtogetmarnieupstairs
        and not marniemakeout
        and not marniestare
        and not marniefingersinmouth
    )

    def video_image(filename):
        name = filename.rsplit("/", 1)[-1].rsplit(".", 1)[0]
        
        return Transform(
        Movie(
            play=filename,
            start_image="gui/start_frames/{}_start.webp".format(name),
            loop=False,
            keep_last_frame=True
        ),
        size=(3840, 2160)
    )

init python:
    def resetallflags():
        global sexaddict, netural, good, evil, superevil, supergood
        global supergood_refused_yuni
        global supergood_devotion_started, lorraine_makeout_attempts
        sexaddict = False
        netural = False
        good = False
        evil = False
        superevil = False
        supergood = False
        supergood_refused_yuni = False
        supergood_devotion_started = False
        lorraine_makeout_attempts = 0


screen marnie_image():
    zorder 10000
    add "gui/marnieselfie.jpg" at Transform(xalign=0.9, yalign=0.5)

screen marnie_image2():
    zorder 10000
    add "gui/marnieselfie2.jpg" at Transform(xalign=0.9, yalign=0.5)

transform fit_image:
    size (2160 * 2160 / 3840, 2160)
    align (0.5, 0.5)


define che = Character("Cheesecake")
define syl = Character("[fatherName]")
define unk = Character("???")
define unkm = Character("Unknown Man")
define mar = Character("Marnie")
define dan = Character("Dan")
define mc = Character("[playerName]")
define dev = Character("Him")
define my = Character("Myles")
define kyl = Character("Kyle")
define jen = Character("Jennifer")
define jan = Character("Janice")
define lor = Character("Lorraine")
define piz = Character("Pizza Guy")
define nar = Character("Narrator")
define nin = Character("Nina")
define bri = Character("Brian")
define sun = Character("Sun")
define geo = Character("George")
define marth = Character("Martha")
define hen = Character("Henry")
define tan = Character("Tania")
define sec = Character("Therapist")
define yun = Character("Yuni")
define boss = Character("CEO")
define gia = Character("Gianna")
define background_video = Movie(size=(1920,1080), channel="movie", play="room/computer.ogv", loop=True)



init:
    image june4 = "gui/june4.png"

define slowfade = Fade(1.5, 1.0, 1.5)
define veryslowfade = Fade(3.0, 2.0, 3.0)
define ffade = Fade(0.5, 0.5, 0.5)
define ffastfade = Fade(0.1, 0.1, 0.1)
define slow_dissolve = Dissolve(3.0)
define medium_dissolve = Dissolve(0.65)
define fast_dissolve = Dissolve(0.33)
define ffast_dissolve = Dissolve(0.20)



default evilturn_played = False

image sexy1 = Transform(Movie(play="gui/sexy1anim.webm", loop=True), size=(3840, 2160))

image sexy2 = Transform(Movie(play="gui/sexy2anim.webm", loop=True), size=(3840, 2160))

image sexy2alt = Transform(Movie(play="gui/sexy2animalt.webm", loop=True), size=(3840, 2160))

image sexy3 = Transform(Movie(play="gui/sexy3anim.webm", loop=True), size=(3840, 2160))

image sexy3alt = Transform(Movie(play="gui/sexy3animalt.webm", loop=True), size=(3840, 2160))

image sexy4 = Transform(Movie(play="gui/sexy4anim.webm", loop=True), size=(3840, 2160))

image sexy4alt = Transform(Movie(play="gui/sexy4animalt.webm", loop=True), size=(3840, 2160))

image marniesex1 = Transform(Movie(play="gui/marniesex1.webm", loop=True), size=(3840, 2160))

image lorraineyoga1 = Transform(Movie(play="gui/lorraineyoga1.webm", start_image="snap17", loop=True), size=(3840, 2160))

image bianca1 = Transform(Movie(channel="godson_cutscene", start_image="psnap16", keep_last_frame=True, loop=False), size=(3840, 2160))

image lorrainestrip = Transform(Movie(play="gui/lorrainestrip.webm", start_image="snap33", image="snap34", loop=False), size=(3840, 2160))

image ninaloveyou = Transform(Movie(channel="godson_cutscene", start_image="snap26", keep_last_frame=True, loop=False), size=(3840, 2160))

image ninaloveyou = Transform(Movie(channel="godson_cutscene", start_image="snap26", keep_last_frame=True, loop=False), size=(3840, 2160))

image myleshug = Transform(Movie(play="gui/myleshug.webm", start_image="snap37", image="snap38", loop=False), size=(3840, 2160))

image ninaloveyou2 = Transform(Movie(play="gui/ninaloveyou2.webm", start_image="snap27", keep_last_frame=True, loop=False), size=(3840, 2160))

image ninaloveyou3 = Transform(Movie(play="gui/ninaloveyou3.webm", start_image="snap29", keep_last_frame=True, loop=False), size=(3840, 2160))

image ninastrip1 = Transform(Movie(play="gui/ninastrip1.webm", start_image="snap24", image="snap23", loop=False), size=(3840, 2160))

image ninastrip2 = Transform(Movie(play="gui/ninastrip2.webm", start_image="snap23", image="black", loop=False), size=(3840, 2160))

image lorrainefloortoessuck = Transform(Movie(play="gui/lorrainefloortoessuck.webm", start_image="psnap37", keep_last_frame=True, loop=False), size=(3840, 2160))

image lorrainemakeout = Transform(Movie(play="gui/lorrainemakeout.webm", start_image="psnap38", keep_last_frame=True, loop=False), size=(3840, 2160))

image mcgrabher = Transform(Movie(channel="godson_cutscene", start_image="a222", image="black", loop=False), size=(3840, 2160))

image outro = Transform(Movie(channel="godson_cutscene", start_image="black", keep_last_frame=True, loop=False), size=(3840, 2160))

image ninaloveyou4 = Transform(Movie(play="gui/ninaloveyou4.webm", start_image="psnap15", keep_last_frame=True, loop=False), size=(3840, 2160))

image marnierub = Transform(Movie(play="gui/marnierub.webm", start_image="a208", loop=True), size=(3840, 2160))

image mctwerk = Transform(Movie(channel="godson_cutscene", start_image="black", image="black", loop=False), size=(3840, 2160))

image lorrainesex1 = Transform(Movie(channel="godson_cutscene", start_image="snap35", keep_last_frame=True, loop=False), size=(3840, 2160))

image lorrainesex2 = Transform(Movie(play="gui/lorrainesex2.webm", start_image="snap36", image="black", loop=False), size=(3840, 2160))

image lorrainesex3 = Transform(Movie(play="gui/lorrainesex3.webm", start_image="snap36", image="black", loop=False), size=(3840, 2160))

image lorraineyoga2 = Transform(Movie(play="gui/lorraineyoga2.webm", start_image="snap15", loop=True), size=(3840, 2160))

image mcassrub = Transform(Movie(play="gui/mcassrub.webm", start_image="psnap9", loop=True), size=(3840, 2160))

image lorrainesurprise = Transform(Movie(play="gui/lorrainesurprise.webm", start_image="snap20", keep_last_frame=True, loop=True), size=(3840, 2160))

image lorraineyoga3 = Transform(Movie(channel="godson_cutscene", start_image="snap19", loop=False), size=(3840, 2160))

image mcyuni1 = Transform(Movie(play="gui/mcyuni1.webm", start_image="a143", keep_last_frame=True, loop=False), size=(3840, 2160))

image mcyuni2 = Transform(Movie(play="gui/mcyuni2.webm", start_image="a143special", keep_last_frame=True, loop=False), size=(3840, 2160))

image mcyuni3 = Transform(Movie(play="gui/mcyuni3.webm", start_image="a143special", keep_last_frame=True, loop=False), size=(3840, 2160))

image mcyuni4 = Transform(Movie(play="gui/mcyuni4.webm", start_image="a143special", keep_last_frame=True, loop=False), size=(3840, 2160))

image mcyuni5 = Transform(Movie(play="gui/mcyuni5.webm", start_image="a143special", keep_last_frame=True, loop=False), size=(3840, 2160))

image mcyuni6 = Transform(Movie(play="gui/mcyuni6.webm", start_image="a143special", keep_last_frame=True, loop=False), size=(3840, 2160))

image mcyuni7 = Transform(Movie(play="gui/mcyuni7.webm", start_image="a143special", keep_last_frame=True, loop=False), size=(3840, 2160))

image mcyuni8 = Transform(Movie(play="gui/mcyuni8.webm", start_image="psnap1", keep_last_frame=True, loop=False), size=(3840, 2160))

image mcyuni9 = Transform(Movie(play="gui/mcyuni9.webm", start_image="psnap2", keep_last_frame=True, loop=False), size=(3840, 2160))

image mcyuni16 = Transform(Movie(play="gui/mcyuni16.webm", start_image="psnap34", keep_last_frame=True, loop=False), size=(3840, 2160))

image payingiannagood = Transform(Movie(play="gui/payingiannagood.webm", start_image="psnap36", keep_last_frame=True, loop=False), size=(3840, 2160))

image payingiannabad = Transform(Movie(play="gui/payingiannabad.webm", start_image="psnap35", keep_last_frame=True, loop=False), size=(3840, 2160))

image mylesthatsmycousin = Transform(Movie(play="gui/mylesthatsmycousin.webm", start_image="psnap21", keep_last_frame=True, loop=False), size=(3840, 2160))

image mylessheneedsthe = Transform(Movie(play="gui/mylessheneedsthe.webm", start_image="psnap27", keep_last_frame=True, loop=False), size=(3840, 2160))

image mylesexcited = Transform(Movie(play="gui/mylesexcited.webm", start_image="psnap18", keep_last_frame=True, loop=False), size=(3840, 2160))

image mylesallurgetting = Transform(Movie(play="gui/mylesallurgetting.webm", start_image="psnap25", keep_last_frame=True, loop=False), size=(3840, 2160))

image mylesfuckforfive = Transform(Movie(play="gui/mylesfuckforfive.webm", start_image="psnap24", keep_last_frame=True, loop=False), size=(3840, 2160))

image myleswhatamigetting = Transform(Movie(play="gui/myleswhatamigetting.webm", start_image="psnap23", keep_last_frame=True, loop=False), size=(3840, 2160))

image mylesineedtogetpaid = Transform(Movie(play="gui/mylesineedtogetpaid.webm", start_image="psnap22", keep_last_frame=True, loop=False), size=(3840, 2160))

image mylessantareveal = Transform(Movie(play="gui/mylessantareveal.webm", start_image="psnap29", keep_last_frame=True, loop=False), size=(3840, 2160))

image partywork = Transform(Movie(channel="godson_cutscene", start_image="psnap30", keep_last_frame=True, loop=False), size=(3840, 2160))

image mylesassclap = Transform(Movie(play="gui/mylesassclap.webm", start_image="psnap20", keep_last_frame=True, loop=False), size=(3840, 2160))

image bringitback = Transform(Movie(channel="godson_cutscene", start_image="psnap31", keep_last_frame=True, loop=False), size=(3840, 2160))

image myleswhy = Transform(Movie(play="gui/myleswhy.webm", start_image="psnap26", keep_last_frame=True, loop=False), size=(3840, 2160))

image myleswhy2 = Transform(Movie(play="gui/myleswhy2.webm", start_image="psnap28", keep_last_frame=True, loop=False), size=(3840, 2160))

image mcyuni10 = Transform(Movie(play="gui/mcyuni10.webm", start_image="psnap3", keep_last_frame=True, loop=False), size=(3840, 2160))

image mcyuni11 = Transform(Movie(play="gui/mcyuni11.webm", start_image="psnap4", keep_last_frame=True, loop=False), size=(3840, 2160))

image mcyuni12 = Transform(Movie(play="gui/mcyuni12.webm", start_image="psnap5", keep_last_frame=True, loop=False), size=(3840, 2160))

image mcyuni13 = Transform(Movie(play="gui/mcyuni13.webm", start_image="psnap6", keep_last_frame=True, loop=False), size=(3840, 2160))

image mcyuni14 = Transform(Movie(play="gui/mcyuni14.webm", start_image="psnap7", keep_last_frame=True, loop=False), size=(3840, 2160))

image mcyuni15 = Transform(Movie(play="gui/mcyuni15.webm", start_image="psnap8", keep_last_frame=True, loop=False), size=(3840, 2160))

image marniemassage = Transform(Movie(channel="godson_cutscene", start_image="psnap13", keep_last_frame=True, loop=False), size=(3840, 2160))

image marniesexaddict1 = Transform(Movie(channel="godson_cutscene", start_image="psnap32", keep_last_frame=True, loop=False), size=(3840, 2160))

image marniesexaddict2 = Transform(Movie(channel="godson_cutscene", start_image="psnap33", keep_last_frame=True, loop=False), size=(3840, 2160))

image marthahard = Transform(Movie(channel="godson_cutscene", start_image="black", keep_last_frame=True, loop=False), size=(3840, 2160))

image mcgrabhim = Transform(Movie(play="gui/mcgrabhim.webm", start_image="psnap10", keep_last_frame=True, loop=False), size=(3840, 2160))

image marniekiss45 = Transform(Movie(play="gui/marniekiss45.webm", start_image="psnap12", keep_last_frame=True, loop=False), size=(3840, 2160))

image marnieliftdress = Transform(Movie(play="gui/marnieliftdress.webm", start_image="psnap11", keep_last_frame=True, loop=False), size=(3840, 2160))

image mcsummon1 = Transform(Movie(play="gui/mcsummon1.webm", start_image="summonsnap1", keep_last_frame=True, loop=False), size=(3840, 2160))

image mcsummon2 = Transform(Movie(play="gui/mcsummon2.webm", start_image="summonsnap1", keep_last_frame=True, loop=False), size=(3840, 2160))

image yunisuperevil = Transform(Movie(channel="godson_cutscene", start_image="black", keep_last_frame=True, loop=False), size=(3840, 2160))

image lorrainesuperevil = Transform(Movie(play="gui/lorrainesuperevil.webm", start_image="lorrainesnap1", keep_last_frame=True, loop=False), size=(3840, 2160))

image mcshower = Transform(Movie(play="gui/mcshower.webm", start_image="snap13", image="snap14", loop=False), size=(3840, 2160))

image mcsanta = Transform(Movie(play="gui/mcsanta.webm", start_image="mcright", image="black", loop=False), size=(3840, 2160))

image mcphone = Transform(Movie(play="gui/mcphone.webm", start_image="a29", image="a30", loop=False), size=(3840, 2160))

image mcring = Transform(Movie(play="gui/mcring.webm", start_image="a31", loop=False), size=(3840, 2160))

image mcpush = Transform(Movie(play="gui/mcpush.webm", start_image="a32", image="black", loop=False), size=(3840, 2160))

image mcknock = Transform(Movie(play="gui/mcknock.webm", start_image="a31", image="a32", loop=False), size=(3840, 2160))

image yunistream = Transform(Movie(channel="godson_cutscene", start_image="snap11", image="snap12", loop=False), size=(3840, 2160))

image mommy1 = Transform(Movie(play="gui/mommy1.webm", start_image="snap41", loop=False, keep_last_frame=True), size=(3840, 2160))

image mommy2 = Transform(Movie(play="gui/mommy2.webm", start_image="snap43", keep_last_frame=True, loop=False), size=(3840, 2160))

image mommy3 = Transform(Movie(play="gui/mommy3.webm", start_image="snap45", keep_last_frame=True, loop=False), size=(3840, 2160))

image mommy4 = Transform(Movie(play="gui/mommy4.webm", start_image="snap48", keep_last_frame=True, loop=False), size=(3840, 2160))

image mommy5 = Transform(Movie(play="gui/mommy5.webm", start_image="snap48", keep_last_frame=True, loop=False), size=(3840, 2160))

image mommy6 = Transform(Movie(play="gui/mommy6.webm", start_image="snap50", keep_last_frame=True, loop=False), size=(3840, 2160))

image mommy7 = Transform(Movie(play="gui/mommy7.webm", start_image="mommy7snap", keep_last_frame=True, loop=False), size=(3840, 2160))

image mommy8 = Transform(Movie(play="gui/mommy8.webm", start_image="mommy8snap", keep_last_frame=True, loop=False), size=(3840, 2160))

image mommy9 = Transform(Movie(play="gui/mommy9.webm", start_image="mommy9snap", keep_last_frame=True, loop=False), size=(3840, 2160))

image mommy10 = Transform(Movie(play="gui/mommy10.webm", start_image="mommy10snap", keep_last_frame=True, loop=False), size=(3840, 2160))

image mommy11 = Transform(Movie(play="gui/mommy11.webm", start_image="mommy11snap", keep_last_frame=True, loop=False), size=(3840, 2160))

image mommy12 = Transform(Movie(play="gui/mommy12.webm", start_image="mommy12snap", keep_last_frame=True, loop=False), size=(3840, 2160))

image mommy13 = Transform(Movie(play="gui/mommy13.webm", start_image="mommy13snap", keep_last_frame=True, loop=False), size=(3840, 2160))

image mommy14 = Transform(Movie(play="gui/mommy14.webm", start_image="mommy14snap", keep_last_frame=True, loop=False), size=(3840, 2160))

image mommy15 = Transform(Movie(play="gui/mommy15.webm", start_image="mommy15snap", keep_last_frame=True, loop=False), size=(3840, 2160))

image mommy16 = Transform(Movie(play="gui/mommy16.webm", start_image="mommy16snap", keep_last_frame=True, loop=False), size=(3840, 2160))

image mommy17 = Transform(Movie(play="gui/mommy17.webm", start_image="mommy17snap", keep_last_frame=True, loop=False), size=(3840, 2160))

image mommy18 = Transform(Movie(play="gui/mommy18.webm", start_image="mommy18snap", keep_last_frame=True, loop=False), size=(3840, 2160))

image mommy19 = Transform(Movie(play="gui/mommy19.webm", start_image="mommy19snap", keep_last_frame=True, loop=False), size=(3840, 2160))

image marnienotfuckingyou = Transform(Movie(channel="godson_cutscene", start_image="marnienot1", keep_last_frame=True, loop=False), size=(3840, 2160))

image mcangry = Transform(Movie(play="gui/mcangry.webm", start_image="a32", keep_last_frame=True, loop=False), size=(3840, 2160))

image mcangry2 = Transform(Movie(play="gui/mcangry2.webm", start_image="a40", keep_last_frame=True, loop=False), size=(3840, 2160))

image mcangry3 = Transform(Movie(play="gui/mcangry3.webm", start_image="a40", keep_last_frame=True, loop=False), size=(3840, 2160))

image mcangry4 = Transform(Movie(play="gui/mcangry4.webm", start_image="a40", keep_last_frame=True, loop=False), size=(3840, 2160))

image marniewalk1 = Transform(Movie(play="gui/marniewalk1.webm", start_image="a43", image="a44", loop=False), size=(3840, 2160))

image mcsexstuff = Transform(Movie(play="gui/mcsexstuff.webm", start_image="a45", image="snap10", loop=False), size=(3840, 2160))

image mcblahblah = Transform(Movie(play="gui/mcblahblah.webm", start_image="a63", image="snap1", loop=False), size=(3840, 2160))

image mchenryangry = Transform(Movie(play="gui/mchenryangry.webm", start_image="a73", image="a75", loop=False), size=(3840, 2160))

image mcblowkiss = Transform(Movie(play="gui/mcblowkiss.webm", start_image="a82", image="a83", loop=False), size=(3840, 2160))

image mcgrabkiss = Transform(Movie(channel="godson_cutscene", start_image="snap2", image="snap3", loop=False), size=(3840, 2160))

image kylemovie = Transform(Movie(play="gui/kylemovie.webm", start_image="snap4", image="snap5", loop=False), size=(3840, 2160))

image mctongue = Transform(Movie(channel="godson_cutscene", start_image="a93", image="a96", loop=False), size=(3840, 2160))

image kylemarniesex = Transform(Movie(play="gui/kylemarniesex.webm", start_image="snap6", image="snap7", loop=False), size=(3840, 2160))

image marnieup = Transform(Movie(channel="godson_cutscene", start_image="psnap39", keep_last_frame=True, loop=False), size=(3840, 2160))

image lorraine1 = Transform(Movie(play="gui/lorraine1.webm", loop=True), size=(3840, 2160))

image mcbegin = Transform(Movie(play="gui/mcbegin.webm", loop=True), size=(3840, 2160))

image mcbegin2 = Transform(Movie(play="gui/mcbegin2.webm", loop=True), size=(3840, 2160))

image henrypunch = Transform(Movie(play="gui/henrypunch.webm", start_image="a27", image="black", loop=False), size=(3840, 2160))

image marniepartydance = Transform(Movie(channel="godson_cutscene", start_image="black", keep_last_frame=True, loop=False), size=(3840, 2160))

image mwalk = Transform(Movie(play="gui/mwalk.webm", loop=True), size=(3840, 2160))

image porn1 = Transform(Movie(play="gui/porn1.webm", loop=True), size=(3840, 2160))

image porn2 = Transform(Movie(play="gui/porn2.webm", loop=True), size=(3840, 2160))

image porn3 = Transform(Movie(play="gui/porn3.webm", loop=True), size=(3840, 2160))

image marnieanim1 = Transform(Movie(play="gui/marnieanim1.webm", loop=True), size=(3840, 2160))

image marnieanim2 = Transform(Movie(play="gui/marnieanim2.webm", loop=True), size=(3840, 2160))

image marnieanim2alt = Transform(Movie(play="gui/marnieanim2alt.webm", loop=True), size=(3840, 2160))

image marnieanim3 = Transform(Movie(play="gui/marnieanim3.webm", loop=True), size=(3840, 2160))

image placeholder1 = Transform(Movie(play="gui/placeholder1.webm", loop=True), size=(3840, 2160))

image lorraineanim1 = Transform(Movie(play="gui/lorraineanim1.webm", loop=True), size=(3840, 2160))

image marnieanim11_1 = Transform(Movie(play="gui/marnieanim11_1.webm", loop=True), size=(3840, 2160))

image marnielewd1 = Transform(Movie(play="gui/marnielewd1.webm", loop=True), size=(3840, 2160))

image marnielewd2 = Transform(Movie(play="gui/marnielewd2.webm", loop=True), size=(3840, 2160))

image heart1 = Transform(Movie(play="gui/heart1.webm", loop=False), size=(3840, 2160))

image sexylorraine1 = Transform(Movie(play="gui/sexylorraine1.webm", loop=True), size=(3840, 2160))

image sexylorraine2 = Transform(Movie(play="gui/sexylorraine2.webm", loop=True), size=(3840, 2160))

image sexylorraine3 = Transform(Movie(play="gui/sexylorraine3.webm", loop=True), size=(3840, 2160))

image sexylorraine4 = Transform(Movie(play="gui/sexylorraine4.webm", loop=True), size=(3840, 2160))

image marnie2real = Transform(Movie(play="gui/marnie2real.webm", loop=True), size=(3840, 2160))

image marnie2real2 = Transform(Movie(play="gui/marnie2real2.webm", loop=True), size=(3840, 2160))

image marnie1real = Transform(Movie(play="gui/marnie1real.webm", loop=True), size=(3840, 2160))

image ninatwerk = Transform(Movie(play="gui/ninatwerk.webm", loop=True), size=(3840, 2160))

image marnie56 = Transform(Movie(play="gui/marnie56real.webm", loop=True), size=(3840, 2160))

image marnie57 = Transform(Movie(play="gui/marnie57real.webm", loop=True), size=(3840, 2160))

image marnielegup1 = Transform(Movie(play="gui/marnielegup1.webm", loop=True), size=(3840, 2160))

image marnieblowjob3 = Transform(Movie(play="gui/marnieblowjob3.webm", loop=True), size=(3840, 2160))

image marniedoggy2 = Transform(Movie(play="gui/marniedoggy2.webm", loop=True), size=(3840, 2160))

image marnieoldmission4 = Transform(Movie(play="gui/marnieoldmission4.webm", loop=True), size=(3840, 2160))

image marniereverse5 = Transform(Movie(play="gui/marniereverse5.webm", loop=True), size=(3840, 2160))

image marthatwerk1 = Transform(Movie(play="gui/marthatwerk.webm", loop=True), size=(3840, 2160))

image mabelmating = Transform(Movie(play="gui/mabelmating1.webm", loop=True), size=(3840, 2160))

image evilcowgirl = Transform(Movie(play="gui/evilcowgirl.webm", loop=True), size=(3840, 2160))

image evilmission = Transform(Movie(play="gui/evilmission.webm", loop=True), size=(3840, 2160))

image evilcum = Transform(Movie(play="gui/evilcum.webm", loop=True), size=(3840, 2160))

image black = "#000"
image white = "#FFF"

image center_text = ParameterizedText(xalign=0.5, yalign=0.5, color="#FFFFFF", font="fonts/jenriv-titling-bold.otf", outlines=[ (absolute(3), "#000", absolute(1), absolute(1)) ], size=128, text_align=0.5)




define config.menu_include_disabled = True

default persistent.set_volumes = False




default current_time = "day"

default current_day = 1

default player_coins = 0

default playerName = "Braden"

default blocked_choice = []




default gomer_quest_1_finished = False
default gomer_quest_1_held = False

default sun_quest_1_finished = False
default sun_quest_1_held = False
default sun_refused = False

default tavern_quest_1_finished = False

default brothel_quest_1_stage = 0
default brothel_quest_1_finished = False

default brothel_quest_2_finished = False

default drutherson_quest_1_finished = False

default messenger_quest_1_finished = False
default starting_town_messenger_nude = False

default jester_quest_1_finished = False
default jester_quest_1_held = False
default house_quest_1_finished = False
default marnie_1_finished = False
default katie_1_finished = False
default ashlynn_1_finished = False
default room_1_finished = False
default ashlynn_2_finished = False
default marnie_2_finished = False
default ashlynn_tv_finished = False
default katie_2_finished = False
default room_2_finished = False




default blacksmith_quest_finished = False

label splashscreen:



    play music "music/Godson Theme.wav" loop

    scene rated
    with ffade
    $ renpy.pause(4.0, hard=True)

    scene cheesecake
    with ffade
    $ renpy.pause(4.0, hard=True)

    python:

        if not persistent.set_volumes:
            
            persistent.set_volumes = True
            
            _preferences.volumes['music'] = godson_default_music_volume
            
            _preferences.volumes['sfx'] = godson_default_sfx_volume
            
            _preferences.volumes['animation'] = godson_default_animation_volume
            
            _preferences.volumes['voice'] = godson_default_voice_volume
            
            _preferences.volumes['other'] = godson_default_other_volume
            
            renpy.music.set_volume(1.0, delay=0, channel='music')

        renpy.music.set_volume(1.0, delay=0,channel='menu_music')

    return







label start:


    stop menu_music fadeout 1.0

    pause 1.0

    jump intro_1













image jen_start_upright_jenloop = "images/jennifer_sex_scene_starts/upright/jenloop.png"
image jen_start_upright_jenloopbeforesex = "images/jennifer_sex_scene_starts/upright/jenloopbeforesex.png"
image jen_start_upright_jenmakeout1 = "images/jennifer_sex_scene_starts/upright/jenmakeout1.png"
image jen_start_upright_jenmakeout2 = "images/jennifer_sex_scene_starts/upright/jenmakeout2.png"
image jen_start_upright_jenmakeout3 = "images/jennifer_sex_scene_starts/upright/jenmakeout3.png"
image jen_start_upright_jenmakeout4 = "images/jennifer_sex_scene_starts/upright/jenmakeout4.png"
image jen_start_upright_jenquestion1 = "images/jennifer_sex_scene_starts/upright/jenquestion1.png"
image jen_start_upright_jenquestion1collegeslut = "images/jennifer_sex_scene_starts/upright/jenquestion1collegeslut.png"
image jen_start_upright_jenquestion2twodollars = "images/jennifer_sex_scene_starts/upright/jenquestion2twodollars.png"
image jen_start_upright_jenquestion3fuckingwhore = "images/jennifer_sex_scene_starts/upright/jenquestion3fuckingwhore.png"
image jen_start_upright_jenquestion4justlikeyourmother = "images/jennifer_sex_scene_starts/upright/jenquestion4justlikeyourmother.png"
image jen_start_upright_jentransition1 = "images/jennifer_sex_scene_starts/upright/jentransition1.png"
image jen_start_upright_jenuprightsex = "images/jennifer_sex_scene_starts/upright/jenuprightsex.png"
image jen_start_upright_jenuprighttranz = "images/jennifer_sex_scene_starts/upright/jenuprighttranz.png"
image jen_start_upright_jensexgrabneck = "images/jennifer_sex_scene_starts/upright/jensexgrabneck.png"
image jen_start_upright_jensexgrabneckslap1 = "images/jennifer_sex_scene_starts/upright/jensexgrabneckslap1.png"
image jen_start_upright_jensexgrabneckslap2 = "images/jennifer_sex_scene_starts/upright/jensexgrabneckslap2.png"

image jen_start_doggy_jenassrub = "images/jennifer_sex_scene_starts/doggy/jenassrub.png"
image jen_start_doggy_jendoggyquestion2 = "images/jennifer_sex_scene_starts/doggy/jendoggyquestion2.png"
image jen_start_doggy_jenfrontviewsex = "images/jennifer_sex_scene_starts/doggy/jenfrontviewsex.png"
image jen_start_doggy_jenloop = "images/jennifer_sex_scene_starts/doggy/jenloop.png"
image jen_start_doggy_jendoggytranz = "images/jennifer_sex_scene_starts/doggy/jendoggytranz.png"
image jen_start_doggy_jennifercum = "images/jennifer_sex_scene_starts/doggy/jennifercum.png"
image jen_start_doggy_jenniferdoggysex = "images/jennifer_sex_scene_starts/doggy/jenniferdoggysex.png"
image jen_start_doggy_jensexslap1 = "images/jennifer_sex_scene_starts/doggy/jensexslap1.png"
image jen_start_doggy_jensexslap2 = "images/jennifer_sex_scene_starts/doggy/jensexslap2.png"
image jen_start_doggy_jensexslap3 = "images/jennifer_sex_scene_starts/doggy/jensexslap3.png"
image jen_start_doggy_jensexslap4 = "images/jennifer_sex_scene_starts/doggy/jensexslap4.png"
image jen_start_doggy_jensexslapangle2 = "images/jennifer_sex_scene_starts/doggy/jensexslapangle2.png"
image jen_start_doggy_jensexslapangle2_alt = "images/jennifer_sex_scene_starts/doggy/jensexslapangle2-1.png"
image jen_start_doggy_slap1 = "images/jennifer_sex_scene_starts/doggy/slap1.png"
image jen_start_doggy_slap2 = "images/jennifer_sex_scene_starts/doggy/slap2.png"
image jen_start_doggy_slap3 = "images/jennifer_sex_scene_starts/doggy/slap3.png"
image jen_start_doggy_slap4 = "images/jennifer_sex_scene_starts/doggy/slap4.png"
image jen_start_doggy_slap5 = "images/jennifer_sex_scene_starts/doggy/slap5.png"
image jen_start_doggy_slap6 = "images/jennifer_sex_scene_starts/doggy/slap6.png"
image jen_start_doggy_slap7 = "images/jennifer_sex_scene_starts/doggy/slap7.png"
image jen_start_doggy_slap8 = "images/jennifer_sex_scene_starts/doggy/slap8.png"
image jen_start_doggy_slap9 = "images/jennifer_sex_scene_starts/doggy/slap9.png"
image jen_start_doggy_slap10 = "images/jennifer_sex_scene_starts/doggy/slap10.png"

image jenloop = Transform(Movie(play="gui/Jennifer sex scene/upright/jenloop.webm", start_image="jen_start_upright_jenloop", loop=True), size=(3840, 2160))
image jenloopbeforesex = Transform(Movie(play="gui/Jennifer sex scene/upright/jenloopbeforesex.webm", start_image="jen_start_upright_jenloopbeforesex", loop=True), size=(3840, 2160))
image jenmakeout1 = Transform(Movie(play="gui/Jennifer sex scene/upright/jenmakeout1.webm", start_image="jen_start_upright_jenmakeout1", keep_last_frame=True, loop=False), size=(3840, 2160))
image jenmakeout2 = Transform(Movie(play="gui/Jennifer sex scene/upright/jenmakeout2.webm", start_image="jen_start_upright_jenmakeout2", keep_last_frame=True, loop=False), size=(3840, 2160))
image jenmakeout3 = Transform(Movie(play="gui/Jennifer sex scene/upright/jenmakeout3.webm", start_image="jen_start_upright_jenmakeout3", keep_last_frame=True, loop=False), size=(3840, 2160))
image jenmakeout4 = Transform(Movie(play="gui/Jennifer sex scene/upright/jenmakeout4.webm", start_image="jen_start_upright_jenmakeout4", keep_last_frame=True, loop=False), size=(3840, 2160))
image jenquestion1 = Transform(Movie(play="gui/Jennifer sex scene/upright/jenquestion1.webm", start_image="jen_start_upright_jenquestion1", loop=True), size=(3840, 2160))
image jenquestion1collegeslut = Transform(Movie(play="gui/Jennifer sex scene/upright/jenquestion1collegeslut.webm", start_image="jen_start_upright_jenquestion1collegeslut", keep_last_frame=True, loop=False), size=(3840, 2160))
image jenquestion2twodollars = Transform(Movie(play="gui/Jennifer sex scene/upright/jenquestion2twodollars.webm", start_image="jen_start_upright_jenquestion2twodollars", keep_last_frame=True, loop=False), size=(3840, 2160))
image jenquestion3fuckingwhore = Transform(Movie(play="gui/Jennifer sex scene/upright/jenquestion3fuckingwhore.webm", start_image="jen_start_upright_jenquestion3fuckingwhore", keep_last_frame=True, loop=False), size=(3840, 2160))
image jenquestion4justlikeyourmother = Transform(Movie(play="gui/Jennifer sex scene/upright/jenquestion4justlikeyourmother.webm", start_image="jen_start_upright_jenquestion4justlikeyourmother", keep_last_frame=True, loop=False), size=(3840, 2160))
image jentransition1 = Transform(Movie(play="gui/Jennifer sex scene/upright/jentransition1.webm", start_image="jen_start_upright_jentransition1", keep_last_frame=True, loop=False), size=(3840, 2160))
image jenuprightsex = Transform(Movie(play="gui/Jennifer sex scene/upright/jenuprightsex.webm", start_image="jen_start_upright_jenuprightsex", loop=True), size=(3840, 2160))
image jenuprighttranz = Transform(Movie(play="gui/Jennifer sex scene/upright/jenuprighttranz.webm", start_image="jen_start_upright_jenuprighttranz", keep_last_frame=True, loop=False), size=(3840, 2160))
image jensexgrabneck = Transform(Movie(play="gui/Jennifer sex scene/upright/jensexgrabneck.webm", start_image="jen_start_upright_jensexgrabneck", loop=True), size=(3840, 2160))
image jensexgrabneckslap1 = Transform(Movie(play="gui/Jennifer sex scene/upright/jensexgrabneckslap1.webm", start_image="jen_start_upright_jensexgrabneckslap1", keep_last_frame=True, loop=False), size=(3840, 2160))
image jensexgrabneckslap2 = Transform(Movie(play="gui/Jennifer sex scene/upright/jensexgrabneckslap2.webm", start_image="jen_start_upright_jensexgrabneckslap2", keep_last_frame=True, loop=False), size=(3840, 2160))

image jenassrub = Transform(Movie(play="gui/Jennifer sex scene/doggy/jenassrub.webm", start_image="jen_start_doggy_jenassrub", loop=True), size=(3840, 2160))
image jendoggyquestion2 = Transform(Movie(play="gui/Jennifer sex scene/doggy/jendoggyquestion2.webm", start_image="jen_start_doggy_jendoggyquestion2", keep_last_frame=True, loop=False), size=(3840, 2160))
image jenfrontviewsex = Transform(Movie(play="gui/Jennifer sex scene/doggy/jenfrontviewsex.webm", start_image="jen_start_doggy_jenfrontviewsex", loop=True), size=(3840, 2160))
image jendoggyloop = Transform(Movie(play="gui/Jennifer sex scene/doggy/jenloop.webm", start_image="jen_start_doggy_jenloop", loop=True), size=(3840, 2160))
image jendoggytranz = Transform(Movie(play="gui/Jennifer sex scene/doggy/jendoggytranz.webm", start_image="jen_start_doggy_jendoggytranz", keep_last_frame=True, loop=False), size=(3840, 2160))
image jennifercum = Transform(Movie(play="gui/Jennifer sex scene/doggy/jennifercum.webm", start_image="jen_start_doggy_jennifercum", keep_last_frame=True, loop=False), size=(3840, 2160))
image jenniferdoggysex = Transform(Movie(play="gui/Jennifer sex scene/doggy/jenniferdoggysex.webm", start_image="jen_start_doggy_jenniferdoggysex", loop=True), size=(3840, 2160))
image jensexslap1 = Transform(Movie(play="gui/Jennifer sex scene/doggy/jensexslap1.webm", start_image="jen_start_doggy_jensexslap1", keep_last_frame=True, loop=False), size=(3840, 2160))
image jensexslap2 = Transform(Movie(play="gui/Jennifer sex scene/doggy/jensexslap2.webm", start_image="jen_start_doggy_jensexslap2", keep_last_frame=True, loop=False), size=(3840, 2160))
image jensexslap3 = Transform(Movie(play="gui/Jennifer sex scene/doggy/jensexslap3.webm", start_image="jen_start_doggy_jensexslap3", keep_last_frame=True, loop=False), size=(3840, 2160))
image jensexslap4 = Transform(Movie(play="gui/Jennifer sex scene/doggy/jensexslap4.webm", start_image="jen_start_doggy_jensexslap4", keep_last_frame=True, loop=False), size=(3840, 2160))
image jensexslapangle2 = Transform(Movie(play="gui/Jennifer sex scene/doggy/jensexslapangle2.webm", start_image="jen_start_doggy_jensexslapangle2", keep_last_frame=True, loop=False), size=(3840, 2160))
image jensexslapangle2_alt = Transform(Movie(play="gui/Jennifer sex scene/doggy/jensexslapangle2-1.webm", start_image="jen_start_doggy_jensexslapangle2_alt", keep_last_frame=True, loop=False), size=(3840, 2160))
image slap1 = Transform(Movie(play="gui/Jennifer sex scene/doggy/slap1.webm", start_image="jen_start_doggy_slap1", keep_last_frame=True, loop=False), size=(3840, 2160))
image slap2 = Transform(Movie(play="gui/Jennifer sex scene/doggy/slap2.webm", start_image="jen_start_doggy_slap2", keep_last_frame=True, loop=False), size=(3840, 2160))
image slap3 = Transform(Movie(play="gui/Jennifer sex scene/doggy/slap3.webm", start_image="jen_start_doggy_slap3", keep_last_frame=True, loop=False), size=(3840, 2160))
image slap4 = Transform(Movie(play="gui/Jennifer sex scene/doggy/slap4.webm", start_image="jen_start_doggy_slap4", keep_last_frame=True, loop=False), size=(3840, 2160))
image slap5 = Transform(Movie(play="gui/Jennifer sex scene/doggy/slap5.webm", start_image="jen_start_doggy_slap5", keep_last_frame=True, loop=False), size=(3840, 2160))
image slap6 = Transform(Movie(play="gui/Jennifer sex scene/doggy/slap6.webm", start_image="jen_start_doggy_slap6", keep_last_frame=True, loop=False), size=(3840, 2160))
image slap7 = Transform(Movie(play="gui/Jennifer sex scene/doggy/slap7.webm", start_image="jen_start_doggy_slap7", keep_last_frame=True, loop=False), size=(3840, 2160))
image slap8 = Transform(Movie(play="gui/Jennifer sex scene/doggy/slap8.webm", start_image="jen_start_doggy_slap8", keep_last_frame=True, loop=False), size=(3840, 2160))
image slap9 = Transform(Movie(play="gui/Jennifer sex scene/doggy/slap9.webm", start_image="jen_start_doggy_slap9", keep_last_frame=True, loop=False), size=(3840, 2160))
image slap10 = Transform(Movie(play="gui/Jennifer sex scene/doggy/slap10.webm", start_image="jen_start_doggy_slap10", keep_last_frame=True, loop=False), size=(3840, 2160))
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
