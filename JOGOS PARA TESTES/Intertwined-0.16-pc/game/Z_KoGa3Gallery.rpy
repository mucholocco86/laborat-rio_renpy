
################################################################################
## Gallery System
################################################################################

init 999 python:
    import re as _gallery_re
    import importlib as _gallery_importlib

    def _gallery_episode(label_name):
        # Look up which episode file defines this label and return its number as a string.
        try:
            _game = _gallery_importlib.import_module("renpy.game")
            node = _game.script.lookup(label_name)
            fn = getattr(node, "filename", "") or ""
            m = _gallery_re.search(r"episode_(\d+)", fn)
            if m:
                return m.group(1)
        except Exception:
            pass
        return None

    _GALLERY_DAYS = (_("Monday"), _("Tuesday"), _("Wednesday"), _("Thursday"), _("Friday"), _("Saturday"), _("Sunday"), _("Weekend"))

    def _gallery_subtitle(label_name, translate=False):
        # Derive a spoiler-light time marker from the label name, e.g. "Week 1 - Thursday".
        # translate=True is for display time; the init-time call must stay English.
        tr = __ if translate else (lambda s: s)
        m = _gallery_re.match(r"Week(\d+)_([A-Za-z]+)", label_name)
        if m:
            day = m.group(2)
            if day in _GALLERY_DAYS:
                return tr(_("Week {0} - {1}")).format(m.group(1), tr(day))
            return tr(_("Week {0}")).format(m.group(1))
        if label_name.startswith("FB_"):
            return tr(_("Flashback"))
        if label_name.startswith("Intro"):
            return tr(_("Intro"))
        return None

    def _gallery_tag_list(tags):
        if tags is None:
            return []
        if isinstance(tags, str):
            tags = [tags]

        seen = set()
        result = []
        for tag in tags:
            text = (tag or "").strip()
            if not text:
                continue
            normalized = text.strip()
            if not normalized or normalized.lower() in seen:
                continue
            seen.add(normalized.lower())
            result.append(normalized)
        return result

    def gallery_item(image_name, label_name, title="", hint="", tags=None):
        tag_list = _gallery_tag_list(tags)[:6]
        return (
            image_name,
            label_name,
            title,
            hint,
            _gallery_episode(label_name), # episode number
            _gallery_subtitle(label_name), # subtitle
            tag_list,
        )

    # Format per item: (image_name, label_name, title, hint, tags)
    GALLERY_DATA = {
        "alexis": {
            "title": _("Alexis"),
            "items": [
                gallery_item("01_072", "Intro_Plane_Alexis", _("The Mile High Club"), _("Take to the skies and enjoy the turbulence."), [
                    _("Vaginal")
                ]),
                gallery_item("02_144", "Week1_Monday_Alexis", _("Just Coffee?"), _("Wait for Alexis at the bar and take her up on the coffee invite."), [
                    _("Vaginal"),
                ]),
                gallery_item("03_093", "Week1_Wednesday_Alexis_Shower", _("Rinse Cycle"), _("Drop everything and rush over when Alexis calls in a panic."), [
                    _("Vaginal"),
                ]),
                gallery_item("04_2264", "Week1_Sunday_Alexis_Car", _("Rest Stop"), _("On the drive home, tell Alexis she's your type."), [
                    _("Vaginal")
                ]),
                gallery_item("04_2280", "Week1_Sunday_Alexis_Home", _("Nightcap"), _("Keep the night going instead of ending it in the car."), [
                    _("Vaginal"), _("Cunnilingus")
                ]),
                gallery_item("07_260", "Week2_Sunday_Alexis_Phone", _("On the Line"), _("Pick up when Alexis calls before her shower."), [
                    _("Masturbation")
                ]),
                gallery_item("07_828", "Week3_Tuesday_Alexis_Date_Wrap", _("Last Call"), _("See the coffee date with Alexis through to the end.")),
                gallery_item("07_887", "Week3_Tuesday_Alexis_Date_MC", _("Back to My Place"), _("Keep the date going and head home with Alexis."), [
                    _("Vaginal"), _("Blowjob"), _("Cunnilingus"),
                ]),
                gallery_item("08_018", "Week3_Wednesday_Alexis", _("Rude Awakening"), _("Wake up next to Alexis the morning after."), [
                    _("Vaginal"),
                ]),
                gallery_item("08_634_00", "Week3_Wednesday_Night", _("Goodnight"), _("Check Alexis's late-night message.")),
                gallery_item("08_1885", "Week3_Sunday_Alexis_Dorm", _("Dorm Visit"), _("Drop by Alexis's dorm once you're official."), [
                    _("Blowjob"), _("Vaginal"), _("Voyeurism")
                ]),
                gallery_item("08_2210", "Week4_Monday_Layla_Hottub_AlexisErynn", _("Hot Tub Crashers"), _("End up in Layla's hot tub with the girls.")),
                gallery_item("10_2081", "Week5_Monday_Alexis_TV", _("Movie Night"), _("Settle in for a movie at Alexis's place.")),
                gallery_item("10_2115", "Week5_Monday_Alexis_Room", _("Damage Control"), _("Follow Alexis to her room after the mix-up."), [
                    _("Blowjob"), _("Vaginal")
                ]),
                gallery_item("11_1836", "Week5_Wednesday_Beach_Join_Alexis", _("Beach Day"), _("At the beach, choose to join Alexis."), [
                    _("Blowjob"),
                ]),
                gallery_item("13_257", "Week5_Thursday_DylansBar_Alexis_End", _("Walk Home"), _("Close out the night at Dylan's Bar with Alexis."), [
                    _("Blowjob"),
                ]),
                gallery_item("13_3610", "Week5_Sunday_Alexis_Roleplay", _("Playing Pretend"), _("Go along with Alexis's little fantasy."), [
                    _("Vaginal"), _("Cunnilingus"),
                ]),
                gallery_item("13_3645", "Week5_Sunday_Alexis_Sex", _("No More Teasing"), _("Let the tension with Alexis finally boil over."), [
                    _("Vaginal"),
                ]),
                gallery_item("15_1460", "Week6_Tuesday_MonroeBBQ_Shower", _("Cooling Off"), _("Slip away for a shower after the Monroe BBQ."), [
                    _("Blowjob"), _("Masturbation")
                ]),
            ]
        },
        "erynn": {
            "title": _("Erynn"),
            "items": [
                gallery_item("03_619", "Week1_Friday_Erynn_Apartment", _("Curiosity"), _("Home alone at Erynn's place, sneak a peek.")),
                gallery_item("04_1661", "Week1_Saturday_Erynn_Pool", _("Poolside"), _("Join Erynn in the water.")),
                gallery_item("07_556", "Week3_Tuesday_Erynn_Kiss", _("First Kiss"), _("Finally make a move on Erynn.")),
                gallery_item("08_982", "Week3_Friday_Pool_Phone_Erynn", _("Long Distance"), _("Take Erynn's call from training camp.")),
                gallery_item("08_1787", "Week3_Sunday_Erynn_Game", _("Game Night"), _("Watch the game with Erynn.")),
                gallery_item("10_1582", "Week4_Sunday_Erynn_Sleepover", _("Stay Over"), _("Let Erynn stay the night instead of sending her home.")),
                gallery_item("11_166", "Week5_Tuesday_Erynn_Photoshoot_MC", _("Behind the Lens"), _("Join Erynn at her photoshoot.")),
                gallery_item("11_365", "Week5_Tuesday_Room_Erynn", _("Just the Two of Us"), _("Follow Erynn to her room after the shoot."), [
                    _("Masturbation")
                ]),
                gallery_item("12_066", "Week5_Thursday_Erynn_Shower", _("Sharing the Shower"), _("Take Erynn up on her shower offer."), [
                    _("Handjob")
                ]),
                gallery_item("13_654", "Week5_Friday_Erynn_Date", _("A Day Out"), _("Spend your date day with Erynn.")),
                gallery_item("13_3381", "Week5_Sunday_Erynn_Bath", _("Bath Time"), _("Climb into the tub with Erynn."), [
                    _("Masturbation")
                ]),
                gallery_item("15_227", "Week6_Tuesday_Morning_Erynn", _("Morning Dare"), _("Rise to Erynn's morning challenge."), [
                    _("Blowjob")
                ]),
            ]
        },
        "layla": {
            "title": _("Layla"),
            "items": [
                gallery_item("04_1920", "Week1_Saturday_Layla_Beach_Strip", _("Wardrobe Malfunction"), _("Wait for Layla to come back from the beach lockers.")),
                gallery_item("08_613", "Week3_Wednesday_Laylatalk_Solo", _("Just Us"), _("Invite Layla up for a private hangout.")),
                gallery_item("08_1620", "Week3_Saturday_TC_Swap_Layla", _("Swap Meet"), _("Pick Layla for the underwear-swap dare.")),
                gallery_item("08_2112", "Week4_Monday_Layla_Hottub", _("Hot Tub for Two"), _("Accept Layla's private hot tub invite."), [
                    _("Blowjob")
                ]),
                gallery_item("09_904", "Week4_Thursday_School_NakedRun", _("Losing the Bet"), _("Go through with the track bet.")),
                gallery_item("10_1733", "Week5_Monday_Layla_Pictures", _("Say Cheese"), _("Take photos with Layla at the booth.")),
                gallery_item("11_1053", "Week5_Tuesday_Layla_Hottub_End_Layla", _("Finally Alone"), _("In the hot tub, stay with Layla."), [
                    _("Blowjob")
                ]),
                gallery_item("11_2574", "Week5_Wednesday_LaylaRoom", _("A Big Step"), _("Follow Layla up to her room."), [
                    _("Vaginal"), _("Cunnilingus"),
                ]),
                gallery_item("13_3789", "Week5_Sunday_Layla", _("Study Break"), _("Drop by Layla's place on Sunday."), [
                    _("Vaginal"), _("Cunnilingus"), _("Blowjob")
                ]),
                gallery_item("15_1765", "Week6_Tuesday_MonroeBBQ_Layla_Room", _("GO FALCONS!"), _("Steal some private time with Layla after the BBQ."), [
                    _("Cunnilingus")
                ]),
            ]
        },
        "elena": {
            "title": _("Elena"),
            "items": [
                gallery_item("07_452", "Week3_Monday_Elena_CheerTraining", _("Home Practice"), _("Help Elena with her cheer training.")),
                gallery_item("08_562", "Week3_Wednesday_Zach_Shower_Help", _("Trust Me, Bro!"), _("Help Zach peek during training camp")),
                gallery_item("08_1680", "Week3_Saturday_TC_End_Elena", _("After Hours"), _("Keep the party going late with Elena.")),
                gallery_item("10_2236", "Week5_Monday_Beach_Elena", _("Sandcastles"), _("Stay to help Elena with her brothers at the beach.")),
                gallery_item("11_809", "Week5_Tuesday_Layla_Hottub_End_Elena", _("Reaching for Elena"), _("In the hot tub, reach for Elena instead.")),
            ]
        },
        "nikki": {
            "title": _("Nikki"),
            "items": [
                gallery_item("04_916", "FB_Riverside_Nikki_Room", _("Tuck-In"), _("Carry Nikki to bed and stay with her.")),
                gallery_item("04_998", "FB_Riverside_Peek_Nikki", _("Caught Peeking"), _("Peek on Nikki while she changes.")),
                gallery_item("04_1189", "FB_Riverside_Nikki_Ending", _("Reunited"), _("Steer the Riverside night toward Nikki."), [
                    _("Vaginal")
                ]),
                gallery_item("04_1471", "FB_Riverside_Nikki_Ending2", _("Weeks Later"), _("Stay on Nikki's path after Riverside."), [
                    _("Vaginal"), _("Cunnilingus"), _("Blowjob")
                ]),
                gallery_item("06_840", "Week2_Weekend_Nikki_Continue", _("If We'd Met Sooner"), _("Walk Nikki home and keep the night going."), [
                    _("Vaginal")
                ]),
                gallery_item("09_538", "Week4_Wednesday_Nikki_Kiss", _("No Words Needed"), _("Kiss Nikki when she turns up in your room.")),
                gallery_item("09_682", "Week4_Thursday_Nikki_Morning_Shower", _("Morning Rinse"), _("Walk in on Nikki in the bathroom."), [
                    _("Vaginal")
                ]),
                gallery_item("09_1037", "Week4_Thursday_Nikki_Beach_Lotion", _("Lend a Hand"), _("Offer to help Nikki with her lotion.")),
                gallery_item("09_1100", "Week4_Thursday_Nikki_Beach_Kiss", _("Making Waves"), _("Make a move on Nikki in the water.")),
                gallery_item("09_1145", "Week4_Thursday_Nikki_Night", _("Sharing the Bed"), _("Stay the night with Nikki."), [
                    _("Vaginal")
                ]),
                gallery_item("10_194", "Week4_Friday_Evening_Nikki", _("Checking In"), _("Look in on Nikki after she gets home."), [
                    _("Cunnilingus")
                ]),
                gallery_item("10_668", "Week4_Saturday_Nikki_BJ", _("Her Kind of Dessert"), _("Let the Saturday date with Nikki heat up."), [
                    _("Blowjob")
                ]),
                gallery_item("10_776", "Week4_Saturday_Nikki_CoolOff", _("Cooling Off"), _("Take Nikki up on cooling off at the bar.")),
                gallery_item("10_830", "Week4_Saturday_Nikki_Sex", _("Her Turn to Lead"), _("Join Nikki instead of calling it a night."), [
                    _("Vaginal")
                ]),
                gallery_item("13_1859", "Week5_Friday_Nikki", _("Surprise Visit"), _("Surprise Nikki with a visit."), [
                    _("Vaginal")
                ]),
                gallery_item("13_2696", "Week5_Sunday_NikkiMorning", _("Breakfast in Bed"), _("Wake up beside Nikki the morning after."), [
                    _("Vaginal"), _("Cunnilingus"), _("69"), _("Blowjob")
                ]),
            ]
        },
        "cara": {
            "title": _("Cara"),
            "items": [
                gallery_item("04_706", "FB_Riverside_Cara_Masturbate", _("Wandering Thoughts"), _("Grow close to Cara during the Riverside trip."), [
                    _("Masturbation")
                ]),
                gallery_item("04_1015", "FB_Riverside_Peek_Cara", _("A Helping Hand"), _("Peek while Cara and Nikki change.")),
                gallery_item("04_1272", "FB_Riverside_Cara_Ending", _("Her Confession"), _("See Cara's Riverside route through to the end."), [
                    _("Vaginal")
                ]),
                gallery_item("04_1539", "FB_Riverside_Cara_Ending2", _("Weeks Later"), _("Stay on Cara's path after Riverside."), [
                    _("Vaginal"), _("Blowjob")
                ]),
                gallery_item("06_881", "Week2_Weekend_Cara_Continue", _("Don't Stop"), _("Keep the weekend with Cara going."), [
                    _("Vaginal"), _("Blowjob")
                ]),
                gallery_item("09_573", "Week4_Wednesday_Cara_Kiss", _("Second Chances"), _("Kiss Cara when she shows up.")),
                gallery_item("09_736", "Week4_Thursday_Cara_Morning_Stay", _("Before School"), _("Stay while Cara gets dressed.")),
                gallery_item("09_1207", "Week4_Thursday_Cara_Clothes_Sex", _("Fitting Room"), _("Join Cara in the changing room."), [
                    _("Vaginal")
                ]),
                gallery_item("09_1243", "Week4_Thursday_Cara_Home_Sex", _("Movie Night In"), _("Sleep in the bed instead of the couch."), [
                    _("Vaginal"), _("Blowjob")
                ]),
                gallery_item("10_288", "Week4_Friday_Evening_Cara_Play", _("Feature Presentation"), _("Play along during Cara's movie night."), [
                    _("Vaginal"), _("Cunnilingus"), _("Rimming")
                ]),
                gallery_item("10_877", "Week4_Saturday_Cara_Bathroom", _("Running Late"), _("Check on Cara while she gets ready."), [
                    _("Cunnilingus"), _("Rimming")
                ]),
                gallery_item("10_933", "Week4_Saturday_Cara_Park_Kiss", _("A Quiet Moment"), _("Share a kiss with Cara in the park.")),
                gallery_item("10_1016", "Week4_Saturday_Cara_Sexgame", _("Spin to Win"), _("Say yes to Cara's little game."), [
                    _("Vaginal"), _("Blowjob"), _("69"), _("Cunnilingus"),
                ]),
                gallery_item("11_1366", "Week5_Wednesday_Morning_Room_Cara", _("Video Call"), _("Answer Cara's call while you're in the shower."), [
                    _("Masturbation")
                ]),
                gallery_item("13_2042", "Week5_Friday_Cara", _("Love Island Night"), _("Surprise Cara at her place."), [
                    _("Vaginal"), _("Blowjob")
                ]),
                gallery_item("13_2971", "Week5_Saturday_CaraRoom", _("Pizza and a Show"), _("Spend the night in Cara's room."), [
                    _("Vaginal"), _("Blowjob"), _("Cunnilingus"), _("Rimming")
                ]),
                gallery_item("13_3081", "Week5_Saturday_CaraRoom_Anal", _("Something New"), _("Explore new territory with Cara."), [
                    _("Anal"), _("Rimming")
                ]),
                gallery_item("15_2783", "Week6_Wednesday_Morning_Train", _("A Familiar Face"), _("Head out for a morning beach run."), [
                    _("Vaginal")
                ]),
            ]
        },
        "emily": {
            "title": _("Emily"),
            "items": [
                gallery_item("02_328", "Week1_Tuesday_Melissa_Emily", _("Caught in the Pool"), _("Cool off in the pool during the backyard hangout.")),
                gallery_item("05_111", "Week2_Monday_AfterSchool", _("Home Early"), _("Head home instead of waiting for Layla.")),
                gallery_item("06_160", "FB_Emily_Melissa_Sex", _("Flashback Emily"), _("Listen to Melissa's story."), [
                    _("Lesbian"), _("Cunnilingus"), _("Scissoring")
                ]),
                gallery_item("09_615", "Week4_Thursday_Emily_Bed", _("Wrong Bed"), _("Turn in for the night in Emily's bed.")),
                gallery_item("13_3273", "Week5_Sunday_EmilyJohn_Date", _("A Real Viking"), _("Watch the Emily & John scene."), [
                    _("Vaginal")
                ]),
                gallery_item("14_1285", "Week6_Monday_Emily_Shower", _("Washing It Away"), _("Wait for Emily as the truth comes out.")),
            ]
        },
        "melissa": {
            "title": _("Melissa"),
            "items": [
                gallery_item("01_210", "Intro_Melissa_Sunbath", _("Rise and Shine"), _("Head to the backyard to find Melissa.")),
                gallery_item("02_278", "Week1_Tuesday_Melissa_Backyard", _("Yard Work"), _("Spend the afternoon by the pool with Melissa.")),
                gallery_item("06_266", "Week2_Tuesday_Melissa_Dream", _("Sweet Dreams"), _("Get close to Melissa over old photos.")),
                gallery_item("10_537", "Week4_Saturday_Melissa_Dream", _("Daydream"), _("Build a strong connection with Melissa."), [
                    _("Vaginal"), _("Cunnilingus")
                ]),
                gallery_item("14_1500", "Week6_Monday_Melissa", _("Comfort"), _("Be there for Melissa after the fallout."), [
                    _("Vaginal"), _("Cunnilingus")
                ]),
                gallery_item("15_062", "Week6_Tuesday_Melissa_Aftermath", _("The Morning After"), _("Face the morning at Melissa's place."), [
                    _("Vaginal")
                ]),
            ]
        },
        "valeria": {
            "title": _("Valeria"),
            "items": [
                gallery_item("08_1594", "Week3_Saturday_TC_Swap_Valeria", _("Swap Meet"), _("Pick Valeria for the underwear-swap dare.")),
                gallery_item("10_1770", "Week5_Monday_Valeria_Photobooth", _("Photobooth"), _("Get a few shots with Valeria in the photo booth.")),
                gallery_item("11_1250", "Week5_Wednesday_Morning_ValeriaRun", _("Morning Run"), _("Join Valeria for an early beach run.")),
                gallery_item("13_1192", "Week5_Friday_Valeria", _("Date Day"), _("Spend your Friday with Valeria.")),
                gallery_item("15_4074", "Week6_Wednesday_Afternoon_ValeriaGame", _("Game On"), _("After the project, stay to play a game with Valeria.")),
            ]
        },
        "gabi": {
            "title": _("Gabi"),
            "items": [
                gallery_item("05_243", "Week2_Monday_Gabi", _("Drowning Sorrows"), _("Keep drinking with the woman at the bar.")),
                gallery_item("05_439", "Week2_Tuesday_School_Gabi", _("Small World"), _("Recognize your new teacher from last night."), [
                    _("Vaginal")
                ]),
                gallery_item("08_1349", "Week3_Saturday_Gabi_Sex", _("After Class"), _("Comfort Gabi at the field and kiss her back."), [
                    _("Vaginal"), _("Cunnilingus")
                ]),
                gallery_item("08_2022", "Week4_Monday_Spanish_Gabi", _("Spanish Lesson"), _("Keep the Gabi route alive in class.")),
                gallery_item("10_1857", "Week5_Monday_Gabi_Home", _("House Call"), _("Take Gabi somewhere more private."), [
                    _("Vaginal"), _("Blowjob")
                ]),
                gallery_item("14_303", "Week6_Monday_Spanish_Gabi", _("Wandering Mind"), _("Let your mind drift in Spanish class."), [
                    _("Vaginal"), _("Cunnilingus")
                ]),
            ]
        },
        "iris": {
            "title": _("Iris"),
            "items": [
                gallery_item("07_844", "Week3_Tuesday_Alexis_Date_Iris", _("Meet the Roommate"), _("Wind up in Alexis's room during the date.")),
                gallery_item("09_130", "FB_Alvarado_Iris_Park", _("Caught in Focus"), _("Take a photo at the park.")),
                gallery_item("09_205", "FB_Alvarado_Iris_Lake", _("Evening the Score"), _("Meet Iris at the lake.")),
                gallery_item("09_258", "FB_Alvarado_Iris_Ice", _("Sweet Tooth"), _("Follow Iris through her day out.")),
                gallery_item("09_297", "FB_Alvarado_Iris_Firsttime", _("Her Lead"), _("Let Iris in when she knocks."), [
                    _("Vaginal"), _("Cunnilingus")
                ]),
                gallery_item("09_394", "FB_Alvarado_Iris_Phone", _("Coming Clean"), _("Answer Iris's late-night call.")),
                gallery_item("09_420", "FB_Alvarado_Iris_Bike", _("Born to Ride"), _("Keep things going with Iris down the line."), [
                    _("Vaginal"), _("Cunnilingus"), _("Blowjob")
                ]),
                gallery_item("11_1891", "Week5_Wednesday_Beach_Join_Iris", _("Beach Day"), _("At the beach, choose to join Iris.")),
                gallery_item("11_2087", "Week5_Wednesday_Beach_Sex_Iris", _("Settling the Bet"), _("Take Iris up on the volleyball wager."), [
                    _("Vaginal")
                ]),
                gallery_item("14_798", "Week6_Monday_Garage_IrisSex", _("Let's get greasy!"), _("Join Iris in the garage."), [
                    _("Vaginal"), _("Cunnilingus")
                ]),
                gallery_item("16_613", "Week6_Thursday_Iris_Flashback", _("A Ride to Remember"), _("Visit Iris in the hospital."), [
                    _("Vaginal"), _("Cunnilingus"), _("Blowjob")
                ]),
            ]
        },
        "tori": {
            "title": _("Tori"),
            "items": [
                gallery_item("03_298", "Week1_Thursday_DylanBar_Tori", _("Bottoms Up"), _("Show some interest in Tori at Dylan's bar."), [
                    _("Vaginal"), _("Blowjob")
                ]),
                gallery_item("08_433", "Week3_Wednesday_Training_Tori", _("Work Up a Sweat"), _("Pair up with Tori at training camp."), [
                    _("Cunnilingus")
                ]),
                gallery_item("08_1268", "Week3_Saturday_Tori", _("Vic-Tori"), _("Meet Tori after winning the competition."), [
                    _("Vaginal"), _("Cunnilingus"), _("Rimming"), _("Blowjob")
                ]),
                gallery_item("09_844", "Week4_Thursday_School_Tori_HJ", _("Hands-On Learning"), _("Not focusing on the lesson."), [
                    _("Blowjob")
                ]),
                gallery_item("11_1540", "Week5_Wednesday_Beach_Tori", _("Slipping Away"), _("At the beach, let Tori pull you away from the group."), [
                    _("Vaginal"), _("Cunnilingus"), _("Rimming")
                ]),
                gallery_item("15_3306", "Week6_Wednesday_School_ToriShower", _("Steaming Up"), _("Join Tori in the shower."), [
                    _("Vaginal"), _("Cunnilingus"), _("Rimming"), _("Blowjob")
                ]),
            ]
        },
        "lakeyn": {
            "title": _("Lakeyn"),
            "items": [
                gallery_item("04_180", "FB_Tattooshop_Lakeyn_Sex", _("Tattoo Shop"), "", [
                    _("Vaginal"), _("Cunnilingus")
                ]),
            ]
        },
        "adriana": {
            "title": _("Adriana"),
            "items": [
                gallery_item("08_2164", "Week4_Monday_Layla_Hottub_Adriana", _("Hot Tub Adriana"), _("Linger in Layla's hot tub a little too long.")),
                gallery_item("15_1435", "Week6_Tuesday_MonroeBBQ_Shower_Adriana", _("BBQ Shower"), _("In the BBQ shower, let your mind wander to Adriana."), [
                    _("Blowjob")
                ]),
            ]
        },
        "mira": {
            "title": _("Mira"),
            "items": [
                gallery_item("13_2340", "Week5_Saturday_MiraHome", _("Home Visit"), _("Walk Mira home."), [
                    _("Vaginal")
                ]),
                gallery_item("13_2428", "Week5_Saturday_MiraCar", _("Car Scene"), _("Take a ride with Mira in Nikki's car."), [
                    _("Vaginal")
                ]),
            ]
        },
        "sienna": {
            "title": _("Sienna"),
            "items": [
                gallery_item("11_812", "Week5_Tuesday_Layla_Hottub_Sienna", _("Hot Tub Sienna"), _("While getting wine, investigate."), [
                    _("Vaginal"), _("Cunnilingus"), _("Voyeurism")
                ]),
                gallery_item("15_3465", "Week6_Wednesday_Afternoon_SiennaHotel", _("Hotel Meet"), _("Meet Sienna at the Sunrise Hotel. Room 202."), [
                    _("Vaginal"), _("Blowjob"), _("Cunnilingus"), _("Voyeurism")
                ]),
            ]
        },
        "other": {
            "title": _("Other"),
            "items": [
                gallery_item("01_116", "Intro_Stewardess", _("Friendly Skies"), _("Flirt with the stewardess."), [
                    _("Blowjob")
                ]),
                gallery_item("03_159", "Week1_Wednesday_Rachel", _("Right at Home"), _("Rachel is where she wants to be."), [
                    _("Blowjob"), _("Titjob")
                ]),
                gallery_item("04_1992", "Week1_Saturday_Restaurant_Rachel", _("Reservations"), _("Meet Rachel at the restaurant."), [
                    _("Vaginal"), _("Blowjob")
                ]),
                gallery_item("04_1415", "FB_Riverside_Julia_Sex", _("Club Memories"), _("Flashback to Julia at the club."), [
                    _("Vaginal"), _("Blowjob")
                ]),
                gallery_item("05_369", "Week2_Tuesday_School_Natasha", _("Natasha & Mike"), _("Watch Natasha and Mike."), [
                    _("Vaginal"), _("Voyeurism")
                ]),
                gallery_item("09_1193", "Week4_Thursday_Cara_Davis", _("Ms. Davis"), _("Catch Ms. Davis while looking for Cara."), [
                    _("Voyeurism")
                ]),
                gallery_item("12_426", "Week5_Thursday_Restaurant_Brooke", _("Finding Brooke"), _("Try to find Brooke."), [
                    _("Masturbation"), _("Voyeurism")
                ]),
                gallery_item("13_2659", "Week5_Saturday_HaleyMike", _("Haley & Mike"), _("Watch Haley and Mike."), [
                    _("Vaginal"), _("Voyeurism")
                ]),
            ]
        }
    }

    GALLERY_LABELS = []
    for _char_info in GALLERY_DATA.values():
        for _item in _char_info["items"]:
            GALLERY_LABELS.append(_item[1])


    def get_gallery_counts(char_key):
        data = GALLERY_DATA.get(char_key, {})
        items = data.get("items", [])
        seen = sum(1 for item in items if renpy.seen_label(item[1]))
        return seen, len(items)


    GALLERY_LABELS_BY_CHAR = {}

    def _gallery_extract_labels():
        result = {}
        for c_key in GALLERY_DATA.keys():
            result[c_key + "_gallery"] = [item[1] for item in GALLERY_DATA[c_key]["items"]]
        return result

    GALLERY_LABELS_BY_CHAR = _gallery_extract_labels()

    def gallery_count_char(name):
        raw = GALLERY_LABELS_BY_CHAR.get(name, [])
        canonical = set(getattr(renpy.store, "GALLERY_LABELS", None) or [])
        if canonical:
            labels = [l for l in raw if l in canonical]
        else:
            labels = [l for l in raw if renpy.has_label(l)]
        seen = sum(1 for l in labels if renpy.seen_label(l))
        return seen, len(labels)

    def gallery_count_all():
        labels = getattr(renpy.store, "GALLERY_LABELS", None) or []
        seen = sum(1 for l in labels if renpy.seen_label(l))
        return seen, len(labels)

    def gallery_replay_unlocked(item_label, dev_unlock_all=False):
        if renpy.seen_label(item_label):
            return True
        if dev_unlock_all:  #KoGa3
            return True
        return False

    def gallery_replay_action(item_label, dev_unlock_all=False):
        if renpy.has_label(item_label):
            force_unlock = False if dev_unlock_all else None
            return Replay(item_label, scope={"name": 'mc' if not persistent.player_name else persistent.player_name}, locked=force_unlock)
        return Function(renpy.notify, _("Replay is not available in this build yet."))

    _gallery_path_cache = {}
    def get_gallery_blur_path(img_name):
        if img_name in _gallery_path_cache:
            return _gallery_path_cache[img_name]
        valid_exts = (".png", ".jpg", ".jpeg", ".webp")
        for fn in renpy.list_files():
            name_only = fn.split('/')[-1]
            if (name_only == img_name or name_only.startswith(img_name + ".")) and fn.lower().endswith(valid_exts):
                _gallery_path_cache[img_name] = fn
                return fn
        _gallery_path_cache[img_name] = None
        return None

################################################################################
## Character Gallery Screen
################################################################################
init 999:
    screen character_gallery(char_key=None):
        tag menu

        default dev_unlock_all = False
        default hovered_item = None

        # Use the passed key if it exists, otherwise fall back to a safe global/default key.
        python:
            target_char = char_key or getattr(renpy.store, "current_gallery_char", None) or "alexis"
            data = GALLERY_DATA.get(target_char, {"title": _("Gallery"), "items": []})
            title = __(data["title"])
            gallery_name = title.upper()
            items = data["items"]
            seen, total = get_gallery_counts(target_char)

        add GALLERY_BG

        # Dynamic Header & Completion Tracker
        vbox:
            xalign 0.5 ypos 0.045
            spacing 2
            text _("[gallery_name] GALLERY ([seen]/[total])") size 20 color "#ffffff" xalign 0.5
            if seen == total and total > 0:
                text _("COMPLETED") size 14 color "#5be353" xalign 0.5
            else:
                text _("Locked scenes reveal a clue on hover.") size 11 color "#8fa0aa" xalign 0.5

        # Developer Toggle
        # if config.developer:  #KoGa3
        textbutton "DEV: [ 'Locks Bypassed (click)' if dev_unlock_all else 'Bypass Locks (click)' ]":
            action ToggleScreenVariable("dev_unlock_all")
            xalign 0.98 ypos 0.04
            text_size 20    #14
            text_color ("#5be353" if dev_unlock_all else "#ff5b5b")

        # Scrollable Viewport Grid
        vpgrid:
            cols 6
            xpos 0.075 ypos 0.12
            ymaximum 845
            xspacing 30
            yspacing 10
            mousewheel True
            scrollbars "vertical"
            allow_underfull True
            side_spacing 40 
            vscrollbar_unscrollable "hide"  

            for image_name, label_name, title_text, hint_text, ep_num, subtitle, tags in items:
                $ is_unlocked = gallery_replay_unlocked(label_name, dev_unlock_all)
                vbox:
                    spacing 5
                    xsize 250
                    ysize 200
                    xalign 0.5

                    fixed:
                        xysize (250, 165)
                        xalign 0.5

                        if is_unlocked:
                            viewport:
                                xysize (250, 165)
                                
                                if hovered_item == label_name:
                                    add Transform(image_name, fit="cover", align=(0.5, 0.5), matrixcolor=SaturationMatrix(1.0))
                                else:
                                    add Transform(image_name, fit="cover", align=(0.5, 0.5), matrixcolor=SaturationMatrix(0.5))

                                # FIX forces gallery image to be centered correctly within the viewport
                                add Solid("#00000000")

                            button:
                                xysize (250, 165)
                                background None 
                                action gallery_replay_action(label_name, dev_unlock_all)
                                hovered SetScreenVariable("hovered_item", label_name)
                                unhovered SetScreenVariable("hovered_item", None)
                                    
                            if hovered_item == label_name:
                                add "gui/gallery/frame-hover.png"
                            else:
                                add "gui/gallery/frame.png"

                            if tags and hovered_item == label_name:
                                vbox:
                                    xalign 1.0
                                    yalign 0.0
                                    xoffset -8
                                    yoffset 8
                                    spacing 4
                                    
                                    for tag in tags:
                                        frame:
                                            background Solid("#ff01ff46")
                                            xpadding 6
                                            ypadding 2
                                            xalign 1.0
                                            text "[tag!t]" style "gallery_tag_text"
                                
                        else:
                            $ real_path = get_gallery_blur_path(image_name)
                            
                            viewport:
                                xysize (250, 165)
                                
                                if real_path:
                                    add Transform(im.Blur(real_path, 45.0), fit="cover", align=(0.5, 0.5), matrixcolor=SaturationMatrix(0.5), alpha=0.6)
                                    add Solid("#00000040")
                                else:
                                    add Solid("#22222280")
                                    
                            imagebutton:
                                idle Transform("gui/gallery/frame.png", matrixcolor=SaturationMatrix(0.4), alpha=0.8)
                                hover Transform("gui/gallery/frame.png", matrixcolor=None)
                                action NullAction()
                                hovered SetScreenVariable("hovered_item", label_name)
                                unhovered SetScreenVariable("hovered_item", None)
                                 
                            # Lock icon on top.
                            add "gui/gallery/locked.png"

                        if ep_num:
                            frame:
                                if hovered_item == label_name:
                                    background Solid("#ff01ff46")
                                else:
                                    background Solid("#01d9ff46")
                                padding (6, 2)
                                pos (6, 6)
                                text _("EP [ep_num]") style "gallery_ep_badge_text"

                    fixed:
                        xsize 240
                        ysize 32
                        xalign 0.5

                        $ subtitle = _gallery_subtitle(label_name, True) if subtitle else subtitle

                        if is_unlocked:
                            vbox:
                                xalign 0.5
                                spacing 1
                                text "[title_text!t]" size 12 color "#ffffff" xalign 0.5 text_align 0.5
                                if subtitle:
                                    text "[subtitle]" size 11 color "#8fa0aa" xalign 0.5 text_align 0.5
                        else:
                            if hint_text and hovered_item == label_name:
                                text "[hint_text!t]" size 11 color "#aaaaaa" xalign 0.5 text_align 0.5 xmaximum 180 layout "subtitle"
                            elif subtitle:
                                text "[subtitle]" size 10 color "#8fa0aa" xalign 0.5 text_align 0.5

        hbox:
            xalign 0.5 ypos 0.92
            use outer_nav_pill(_("RETURN"), ShowMenu("girls_gallery"), centered=True)
