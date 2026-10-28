label mphone_check_pack_quest_available:
    $ pack_quest_available = False
    if freeRoamID == "ep9_4" and not persistent.pack_quest4_completed:
        $ pack_quest_available = True
        $ pack_quest_list = []
        $ pq_found_buttons = 0
        $ pack_quest_list.append(["A vengeful spirit",False])
        $ pack_quest_list.append(["The other bloody five",False])
        $ pack_quest_list.append(["Hell Week box",False])
        $ pack_quest_list.append(["Lips",False])
        $ pack_quest_list.append(["Rescue me",False])
        $ pack_quest_list.append(["Ribcage",False])
        $ pack_quest_list.append(["Second costume",False])
        $ pack_quest_list.append(["Stuff",False])
        $ pack_quest_list.append(["The hidden owl",False])
        $ pack_quest_list.append(["Twins",False])

        $ mphone_pq_img = "pack_quest_pack_crp4_idle"
    elif freeRoamID == "ep10_5" and not persistent.pack_quest5_completed:
        $ pack_quest_available = True
        $ pack_quest_list = []
        $ pq_found_buttons = 0
        $ pack_quest_list.append(["Caution",False])
        $ pack_quest_list.append(["Crucified",False])
        $ pack_quest_list.append(["Flightless bird",False])
        $ pack_quest_list.append(["Pills",False])
        $ pack_quest_list.append(["More pills",False])
        $ pack_quest_list.append(["Puzzle cube",False])
        $ pack_quest_list.append(["Marble titties",False])
        $ pack_quest_list.append(["Tybalt's girlfriend",False])
        $ pack_quest_list.append(["Unlock unlock",False])
        $ pack_quest_list.append(["Walnuts",False])
        $ mphone_pq_img = "pack_quest_pack_crp5_idle"
    elif freeRoamID == "ep11_4" and not persistent.pack_quest6_completed:
        $ pack_quest_available = True
        $ pack_quest_list = []
        $ pq_found_buttons = 0
        $ pack_quest_list.append(["Gnome #1",False])
        $ pack_quest_list.append(["Gnome #2",False])
        $ pack_quest_list.append(["Gnome #3",False])
        $ pack_quest_list.append(["Gnome #4",False])
        $ pack_quest_list.append(["Gnome #5",False])
        $ pack_quest_list.append(["Gnome #6",False])
        $ pack_quest_list.append(["Gnome #7",False])
        $ pack_quest_list.append(["Gnome #8",False])
        $ pack_quest_list.append(["Gnome #9",False])
        $ pack_quest_list.append(["Gnome #10",False])
        $ mphone_pq_img = "pack_quest_pack_crp6_idle"
    elif freeRoamID == "ep12_3" and not persistent.pack_quest7_completed:
        $ pack_quest_available = True
        $ pack_quest_list = []
        $ pq_found_buttons = 0
        $ pack_quest_list.append(["A lost bet",False])
        $ pack_quest_list.append(["Changed plans",False])
        $ pack_quest_list.append(["Don't drink that",False])
        $ pack_quest_list.append(["Egami Rorrim",False])
        $ pack_quest_list.append(["I heart music",False])
        $ pack_quest_list.append(["Not for the bald",False])
        $ pack_quest_list.append(["Only a fan",False])
        $ pack_quest_list.append(["Potential butt rocket",False])
        $ pack_quest_list.append(["Smoke source",False])
        $ pack_quest_list.append(["Wheelchair",False])
        $ mphone_pq_img = "pack_quest_pack_crp7_idle"
    return

init:
    if persistent.pack_quest4_completed == None:
        $ persistent.pack_quest4_completed = False
    if persistent.pack_quest5_completed == None:
        $ persistent.pack_quest5_completed = False
    if persistent.pack_quest6_completed == None:
        $ persistent.pack_quest6_completed = False
    if persistent.pack_quest7_completed == None:
        $ persistent.pack_quest7_completed = False
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
