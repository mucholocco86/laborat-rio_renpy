from pypresence import Presence
import time
import random
import sys
import os
import io
import subprocess
starttime = int(time.time())
client_id = '918474908827275295' # id of your Discord application
large_text = "Being a DIK" # text of large img of your app
large_image = "badik_large" # large img of your app
small_text = "Being a DIK" # text of small img of your app
small_image = "badik_small" # small img of your app
RPC = Presence(client_id)
RPC.connect() # Connect RPC client

while True:
    try:
        file = open("{0}\..\state.txt".format(os.getcwd()), 'r', encoding = "utf-8").read() # get status from file

        if "err3" == file:
            details = ""
            state = None
            large_text = "Being a DIK"
            large_image = "badik_large"
            small_text = "Being a DIK"
            small_image = "badik_small"
        elif "mm" == file:
            details = "Main Menu"
            state = None
            large_text = "Being a DIK"
            large_image = "badik_large"
            small_text = "Being a DIK"
            small_image = "badik_small"
        elif "sp" == file:
            details = "Being a DIK is loading"
            state = None
            large_text = "Being a DIK"
            large_image = "badik_large"
            small_text = "Being a DIK"
            small_image = "badik_small"
        elif "ep_interlude" == file:
            details = "Interlude - Riding the Waves"
            state = "patreon.com/DrPinkCake"
            large_text = "Being a DIK"
            large_image = "ep_interlude_big"
            small_text = "Being a DIK"
            small_image = "badik_small"
        elif "ep_interlude_steam" == file:
            details = "Interlude - Riding the Waves"
            state = None
            large_text = "Being a DIK"
            large_image = "ep_interlude_big"
            small_text = "Being a DIK"
            small_image = "badik_small"
        elif "ep9_steam_isabella" == file:
            details = "Episode 9 - Vixens (Isabella)"
            state = None
            small_text = "Being a DIK"
            large_image = "ep9_isabella"
            large_text = "Isabella"
            small_image = "badik_small"
        elif "ep9_isabella" == file:
            details = "Episode 9 - Vixens (Isabella)"
            state = "patreon.com/DrPinkCake"
            small_text = "Being a DIK"
            large_image = "ep9_isabella"
            large_text = "Isabella"
            small_image = "badik_small"
        elif "ep9_steam_jill" == file:
            details = "Episode 9 - Vixens (Jill)"
            state = None
            small_text = "Being a DIK"
            large_image = "ep9_jill"
            large_text = "Jill"
            small_image = "badik_small"
        elif "ep9_jill" == file:
            details = "Episode 9 - Vixens (Jill)"
            state = "patreon.com/DrPinkCake"
            small_text = "Being a DIK"
            large_image = "ep9_jill"
            large_text = "Jill"
            small_image = "badik_small"
        elif "ep9_steam_sage" == file:
            details = "Episode 9 - Vixens (Sage)"
            state = None
            small_text = "Being a DIK"
            large_image = "ep9_sage"
            large_text = "Sage"
            small_image = "badik_small"
        elif "ep9_sage" == file:
            details = "Episode 9 - Vixens (Sage)"
            state = "patreon.com/DrPinkCake"
            small_text = "Being a DIK"
            large_image = "ep9_sage"
            large_text = "Sage"
            small_image = "badik_small"
        elif "ep9_steam_maya" == file:
            details = "Episode 9 - Vixens (Josy & Maya)"
            state = None
            small_text = "Being a DIK"
            large_image = "ep9_maya"
            large_text = "Josy & Maya"
            small_image = "badik_small"
        elif "ep9_maya" == file:
            details = "Episode 9 - Vixens (Josy & Maya)"
            state = "patreon.com/DrPinkCake"
            small_text = "Being a DIK"
            large_image = "ep9_maya"
            large_text = "Josy & Maya"
            small_image = "badik_small"
        elif "ep9_steam_josy" == file:
            details = "Episode 9 - Vixens (Josy & Maya)"
            state = None
            small_text = "Being a DIK"
            large_image = "ep9_josy"
            large_text = "Josy & Maya"
            small_image = "badik_small"
        elif "ep9_josy" == file:
            details = "Episode 9 - Vixens (Josy & Maya)"
            state = "patreon.com/DrPinkCake"
            small_text = "Being a DIK"
            large_image = "ep9_josy"
            large_text = "Josy & Maya"
            small_image = "badik_small"
        elif "ep9_steam_others" == file:
            details = "Episode 9 - Vixens (Others)"
            state = None
            small_text = "Being a DIK"
            large_image = "ep9_others"
            large_text = "Others"
            small_image = "badik_small"
        elif "ep9_others" == file:
            details = "Episode 9 - Vixens (Others)"
            state = "patreon.com/DrPinkCake"
            small_text = "Being a DIK"
            large_image = "ep9_others"
            large_text = "Others"
            small_image = "badik_small"
        elif "ep10_steam_isabella" == file:
            details = "Episode 10 - Calm Before the Snow"
            state = None
            small_text = "Being a DIK"
            large_image = "ep10_isabella"
            large_text = "Isabella"
            small_image = "badik_small"
        elif "ep10_isabella" == file:
            details = "Episode 10 - Calm Before the Snow"
            state = "patreon.com/DrPinkCake"
            small_text = "Being a DIK"
            large_image = "ep10_isabella"
            large_text = "Isabella"
            small_image = "badik_small"
        elif "ep10_steam_jill" == file:
            details = "Episode 10 - Calm Before the Snow"
            state = None
            small_text = "Being a DIK"
            large_image = "ep10_jill"
            large_text = "Jill"
            small_image = "badik_small"
        elif "ep10_jill" == file:
            details = "Episode 10 - Calm Before the Snow"
            state = "patreon.com/DrPinkCake"
            small_text = "Being a DIK"
            large_image = "ep10_jill"
            large_text = "Jill"
            small_image = "badik_small"
        elif "ep10_steam_sage" == file:
            details = "Episode 10 - Calm Before the Snow"
            state = None
            small_text = "Being a DIK"
            large_image = "ep10_sage"
            large_text = "Sage"
            small_image = "badik_small"
        elif "ep10_sage" == file:
            details = "Episode 10 - Calm Before the Snow"
            state = "patreon.com/DrPinkCake"
            small_text = "Being a DIK"
            large_image = "ep10_sage"
            large_text = "Sage"
            small_image = "badik_small"
        elif "ep10_steam_jm" == file:
            details = "Episode 10 - Calm Before the Snow"
            state = None
            small_text = "Being a DIK"
            large_image = "ep10_jm"
            large_text = "Josy & Maya"
            small_image = "badik_small"
        elif "ep10_jm" == file:
            details = "Episode 10 - Calm Before the Snow"
            state = "patreon.com/DrPinkCake"
            small_text = "Being a DIK"
            large_image = "ep10_jm"
            large_text = "Josy & Maya"
            small_image = "badik_small"
        elif "ep10_steam_others" == file:
            details = "Episode 10 - Calm Before the Snow"
            state = None
            small_text = "Being a DIK"
            large_image = "ep10_others"
            large_text = "Others"
            small_image = "badik_small"
        elif "ep10_others" == file:
            details = "Episode 10 - Calm Before the Snow"
            state = "patreon.com/DrPinkCake"
            small_text = "Being a DIK"
            large_image = "ep10_others"
            large_text = "Others"
            small_image = "badik_small"
        elif "ep10_steam_others2" == file:
            details = "Episode 10 - Calm Before the Snow"
            state = None
            small_text = "Being a DIK"
            large_image = "ep10_others2"
            large_text = "Others"
            small_image = "badik_small"
        elif "ep10_others2" == file:
            details = "Episode 10 - Calm Before the Snow"
            state = "patreon.com/DrPinkCake"
            small_text = "Being a DIK"
            large_image = "ep10_others2"
            large_text = "Others"
            small_image = "badik_small"
        elif "ep10_steam_others3" == file:
            details = "Episode 10 - Calm Before the Snow"
            state = None
            small_text = "Being a DIK"
            large_image = "ep10_others3"
            large_text = "Others"
            small_image = "badik_small"
        elif "ep10_others3" == file:
            details = "Episode 10 - Calm Before the Snow"
            state = "patreon.com/DrPinkCake"
            small_text = "Being a DIK"
            large_image = "ep10_others3"
            large_text = "Others"
            small_image = "badik_small"
        elif "ep10_steam_others4" == file:
            details = "Episode 10 - Calm Before the Snow"
            state = None
            small_text = "Being a DIK"
            large_image = "ep10_others4"
            large_text = "Others"
            small_image = "badik_small"
        elif "ep10_others4" == file:
            details = "Episode 10 - Calm Before the Snow"
            state = "patreon.com/DrPinkCake"
            small_text = "Being a DIK"
            large_image = "ep10_others4"
            large_text = "Others"
            small_image = "badik_small"
        elif "ep10_steam_others5" == file:
            details = "Episode 10 - Calm Before the Snow"
            state = None
            small_text = "Being a DIK"
            large_image = "ep10_others5"
            large_text = "Others"
            small_image = "badik_small"
        elif "ep10_others5" == file:
            details = "Episode 10 - Calm Before the Snow"
            state = "patreon.com/DrPinkCake"
            small_text = "Being a DIK"
            large_image = "ep10_others5"
            large_text = "Others"
            small_image = "badik_small"
        elif "ep11_steam_isabella" == file:
            details = "Episode 11 - Paradigm Shift"
            state = None
            small_text = "Being a DIK"
            large_image = "ep11_isabella"
            large_text = "Isabella"
            small_image = "badik_small"
        elif "ep11_isabella" == file:
            details = "Episode 11 - Paradigm Shift"
            state = "patreon.com/DrPinkCake"
            small_text = "Being a DIK"
            large_image = "ep11_isabella"
            large_text = "Isabella"
            small_image = "badik_small"
        elif "ep11_steam_jill" == file:
            details = "Episode 11 - Paradigm Shift"
            state = None
            small_text = "Being a DIK"
            large_image = "ep11_jill"
            large_text = "Jill"
            small_image = "badik_small"
        elif "ep11_jill" == file:
            details = "Episode 11 - Paradigm Shift"
            state = "patreon.com/DrPinkCake"
            small_text = "Being a DIK"
            large_image = "ep11_jill"
            large_text = "Jill"
            small_image = "badik_small"
        elif "ep11_steam_sage" == file:
            details = "Episode 11 - Paradigm Shift"
            state = None
            small_text = "Being a DIK"
            large_image = "ep11_sage"
            large_text = "Sage"
            small_image = "badik_small"
        elif "ep11_sage" == file:
            details = "Episode 11 - Paradigm Shift"
            state = "patreon.com/DrPinkCake"
            small_text = "Being a DIK"
            large_image = "ep11_sage"
            large_text = "Sage"
            small_image = "badik_small"
        elif "ep11_steam_jm" == file:
            details = "Episode 11 - Paradigm Shift"
            state = None
            small_text = "Being a DIK"
            large_image = "ep11_jm"
            large_text = "Josy & Maya"
            small_image = "badik_small"
        elif "ep11_jm" == file:
            details = "Episode 11 - Paradigm Shift"
            state = "patreon.com/DrPinkCake"
            small_text = "Being a DIK"
            large_image = "ep11_jm"
            large_text = "Josy & Maya"
            small_image = "badik_small"
        elif "ep11_steam_jm2" == file:
            details = "Episode 11 - Paradigm Shift"
            state = None
            small_text = "Being a DIK"
            large_image = "ep11_jm2"
            large_text = "Josy & Maya"
            small_image = "badik_small"
        elif "ep11_jm2" == file:
            details = "Episode 11 - Paradigm Shift"
            state = "patreon.com/DrPinkCake"
            small_text = "Being a DIK"
            large_image = "ep11_jm2"
            large_text = "Josy & Maya"
            small_image = "badik_small"
        elif "ep11_steam_others" == file:
            details = "Episode 11 - Paradigm Shift"
            state = None
            small_text = "Being a DIK"
            large_image = "ep11_others"
            large_text = "Others"
            small_image = "badik_small"
        elif "ep11_others" == file:
            details = "Episode 11 - Paradigm Shift"
            state = "patreon.com/DrPinkCake"
            small_text = "Being a DIK"
            large_image = "ep11_others"
            large_text = "Others"
            small_image = "badik_small"
        elif "ep11_steam_others2" == file:
            details = "Episode 11 - Paradigm Shift"
            state = None
            small_text = "Being a DIK"
            large_image = "ep11_others2"
            large_text = "Others"
            small_image = "badik_small"
        elif "ep11_others2" == file:
            details = "Episode 11 - Paradigm Shift"
            state = "patreon.com/DrPinkCake"
            small_text = "Being a DIK"
            large_image = "ep11_others2"
            large_text = "Others"
            small_image = "badik_small"
        elif "ep11_steam_others3" == file:
            details = "Episode 11 - Paradigm Shift"
            state = None
            small_text = "Being a DIK"
            large_image = "ep11_others3"
            large_text = "Others"
            small_image = "badik_small"
        elif "ep11_others3" == file:
            details = "Episode 11 - Paradigm Shift"
            state = "patreon.com/DrPinkCake"
            small_text = "Being a DIK"
            large_image = "ep11_others3"
            large_text = "Others"
            small_image = "badik_small"
        elif "ep11_steam_others4" == file:
            details = "Episode 11 - Paradigm Shift"
            state = None
            small_text = "Being a DIK"
            large_image = "ep11_others4"
            large_text = "Others"
            small_image = "badik_small"
        elif "ep11_others4" == file:
            details = "Episode 11 - Paradigm Shift"
            state = "patreon.com/DrPinkCake"
            small_text = "Being a DIK"
            large_image = "ep11_others4"
            large_text = "Others"
            small_image = "badik_small"
        elif "ep11_steam_others5" == file:
            details = "Episode 11 - Paradigm Shift"
            state = None
            small_text = "Being a DIK"
            large_image = "ep11_others5"
            large_text = "Others"
            small_image = "badik_small"
        elif "ep11_others5" == file:
            details = "Episode 11 - Paradigm Shift"
            state = "patreon.com/DrPinkCake"
            small_text = "Being a DIK"
            large_image = "ep11_others5"
            large_text = "Others"
            small_image = "badik_small"
        elif "ep12_steam_isabella" == file:
            details = "Episode 12 - Smoke and Fire"
            state = None
            small_text = "Being a DIK"
            large_image = "ep12_isabella"
            large_text = "Isabella"
            small_image = "badik_small"
        elif "ep12_isabella" == file:
            details = "Episode 12 - Smoke and Fire"
            state = "patreon.com/DrPinkCake"
            small_text = "Being a DIK"
            large_image = "ep12_isabella"
            large_text = "Isabella"
            small_image = "badik_small"
        elif "ep12_steam_jill" == file:
            details = "Episode 12 - Smoke and Fire"
            state = None
            small_text = "Being a DIK"
            large_image = "ep12_jill"
            large_text = "Jill"
            small_image = "badik_small"
        elif "ep12_jill" == file:
            details = "Episode 12 - Smoke and Fire"
            state = "patreon.com/DrPinkCake"
            small_text = "Being a DIK"
            large_image = "ep12_jill"
            large_text = "Jill"
            small_image = "badik_small"
        elif "ep12_steam_sage" == file:
            details = "Episode 12 - Smoke and Fire"
            state = None
            small_text = "Being a DIK"
            large_image = "ep12_sage"
            large_text = "Sage"
            small_image = "badik_small"
        elif "ep12_sage" == file:
            details = "Episode 12 - Smoke and Fire"
            state = "patreon.com/DrPinkCake"
            small_text = "Being a DIK"
            large_image = "ep12_sage"
            large_text = "Sage"
            small_image = "badik_small"
        elif "ep12_steam_jm" == file:
            details = "Episode 12 - Smoke and Fire"
            state = None
            small_text = "Being a DIK"
            large_image = "ep12_jm"
            large_text = "Josy & Maya"
            small_image = "badik_small"
        elif "ep12_jm" == file:
            details = "Episode 12 - Smoke and Fire"
            state = "patreon.com/DrPinkCake"
            small_text = "Being a DIK"
            large_image = "ep12_jm"
            large_text = "Josy & Maya"
            small_image = "badik_small"
        elif "ep12_steam_jm2" == file:
            details = "Episode 12 - Smoke and Fire"
            state = None
            small_text = "Being a DIK"
            large_image = "ep12_jm2"
            large_text = "Josy & Maya"
            small_image = "badik_small"
        elif "ep12_jm2" == file:
            details = "Episode 12 - Smoke and Fire"
            state = "patreon.com/DrPinkCake"
            small_text = "Being a DIK"
            large_image = "ep12_jm2"
            large_text = "Josy & Maya"
            small_image = "badik_small"
        elif "ep12_steam_others" == file:
            details = "Episode 12 - Smoke and Fire"
            state = None
            small_text = "Being a DIK"
            large_image = "ep12_others"
            large_text = "Others"
            small_image = "badik_small"
        elif "ep12_others" == file:
            details = "Episode 12 - Smoke and Fire"
            state = "patreon.com/DrPinkCake"
            small_text = "Being a DIK"
            large_image = "ep12_others"
            large_text = "Others"
            small_image = "badik_small"
        elif "ep12_steam_others2" == file:
            details = "Episode 12 - Smoke and Fire"
            state = None
            small_text = "Being a DIK"
            large_image = "ep12_others2"
            large_text = "Others"
            small_image = "badik_small"
        elif "ep12_others2" == file:
            details = "Episode 12 - Smoke and Fire"
            state = "patreon.com/DrPinkCake"
            small_text = "Being a DIK"
            large_image = "ep12_others2"
            large_text = "Others"
            small_image = "badik_small"
        elif "ep12_steam_others3" == file:
            details = "Episode 12 - Smoke and Fire"
            state = None
            small_text = "Being a DIK"
            large_image = "ep12_others3"
            large_text = "Others"
            small_image = "badik_small"
        elif "ep12_others3" == file:
            details = "Episode 12 - Smoke and Fire"
            state = "patreon.com/DrPinkCake"
            small_text = "Being a DIK"
            large_image = "ep12_others3"
            large_text = "Others"
            small_image = "badik_small"
        elif "ep12_steam_others4" == file:
            details = "Episode 12 - Smoke and Fire"
            state = None
            small_text = "Being a DIK"
            large_image = "ep12_others4"
            large_text = "Others"
            small_image = "badik_small"
        elif "ep12_others4" == file:
            details = "Episode 12 - Smoke and Fire"
            state = "patreon.com/DrPinkCake"
            small_text = "Being a DIK"
            large_image = "ep12_others4"
            large_text = "Others"
            small_image = "badik_small"
        elif "ep12_steam_others5" == file:
            details = "Episode 12 - Smoke and Fire"
            state = None
            small_text = "Being a DIK"
            large_image = "ep12_others5"
            large_text = "Others"
            small_image = "badik_small"
        elif "ep12_others5" == file:
            details = "Episode 12 - Smoke and Fire"
            state = "patreon.com/DrPinkCake"
            small_text = "Being a DIK"
            large_image = "ep12_others5"
            large_text = "Others"
            small_image = "badik_small"
        elif "df" == file:
            details = ""
            state = None
            large_text = "Being a DIK"
            large_image = "badik_large"
            small_text = "Being a DIK"
            small_image = "badik_small"
        else:
            details = ""
            state = None
            large_text = "Being a DIK"
            large_image = "badik_large"
            small_text = "Being a DIK"
            small_image = "badik_small"
    except:
        details = ""
        state = None
        large_text = "Being a DIK"
        large_image = "badik_large"
        small_text = "Being a DIK"
        small_image = "badik_small"
    RPC.update(details=details, state=state, start = starttime, large_image=large_image, large_text=large_text, small_image=small_image, small_text=small_text) # update status of rpc
    time.sleep(15)

    progs = str(subprocess.check_output('tasklist'))
    if not "BeingADIK" in progs:
        RPC.disconnect
