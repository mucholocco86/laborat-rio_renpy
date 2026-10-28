
#         ⠀⠀⣠⣶⣶⣶⣦⠀⠀
# ⠀⠀⣠⣤⣤⣄⣀⣾⣿⠟⠛⠻⢿⣷⠀
# ⢰⣿⡿⠛⠙⠻⣿⣿⠁⠀⠀⠀⣶⢿⡇
# ⢿⣿⣇⠀⠀⠀⠈⠏⠀⠀⠀ made with love
# ⠀⠻⣿⣷⣦⣤⣀⠀⠀⠀⠀⣾⡿⠃⠀
# ⠀⠀⠀⠀⠉⠉⠻⣿⣄⣴⣿⠟⠀⠀⠀
# ⠀⠀⠀⠀⠀⠀⠀⣿⡿⠟⠁⠀⠀⠀⠀-pax

init -1000:

    define characters = [   { "name": "nova"    , "idle": "gui/sp2/nova_idle.png"    , "hover": "gui/sp2/nova_hover.png"    , "path": "novapath"    , "met": "novau"    , "look": "nova"    , "wait": 0.35 },
                            # { "name": "calypso" , "idle": "gui/sp2/calypso_idle.png" , "hover": "gui/sp2/calypso_hover.png" , "path": "calypsopath" , "met": "calypsou" , "look": "calypso" , "wait": 0.35 },
                            { "name": "alex"    , "idle": "gui/sp2/alex_idle.png"    , "hover": "gui/sp2/alex_hover.png"    , "path": "alexpath"    , "met": "alexu"    , "look": "alex"    , "wait": 0.3 },
                            { "name": "luna"    , "idle": "gui/sp2/luna_idle.png"    , "hover": "gui/sp2/luna_hover.png"    , "path": "lunapath"    , "met": "lunau"    , "look": "luna"    , "wait": 0.25 },
                            { "name": "dalia"   , "idle": "gui/sp2/dalia_idle.png"   , "hover": "gui/sp2/dalia_hover.png"   , "path": "daliapath"   , "met": "daliau"   , "look": "dalia"   , "wait": 0.2 },
                            { "name": "penelope", "idle": "gui/sp2/penelope_idle.png", "hover": "gui/sp2/penelope_hover.png", "path": "penelopepath", "met": "penelopeu", "look": "penelope", "wait": 0.15 },
                            { "name": "nancy"   , "idle": "gui/sp2/nancy_idle.png"   , "hover": "gui/sp2/nancy_hover.png"   , "path": "nancypath"   , "met": "nancyu"   , "look": "nancy"   , "wait": 0.1 },
                            { "name": "annie"   , "idle": "gui/sp2/annie_idle.png"   , "hover": "gui/sp2/annie_hover.png"   , "path": "anniepath"   , "met": "annieu"   , "look": "annie"   , "wait": 0.05 }
                            ] # Calypso isn't included here because this is a list for default characters. Calypso is added later on
    default c_hovered = None
    default girl_sel  = None

    ## TEMP

    default calypsou = False
    default calypso_points = 0

screen point():
    tag menu
    modal True
    add "galleryback"
    key 'game_menu' action [ Return(), SetVariable('c_hovered', None), SetVariable("girl_sel", None) ]
    if c_hovered is None:
        if girl_sel is not None:
            $ loc_points = getattr(store, girl_sel + "_points")
            $ assets = { "nova": ["nova_bg.png", "nova_h.png", "nova_l.png", "nova_d.png"], "calypso": ["calypso_bg.png", "calypso_h.png", "calypso_l.png", "calypso_d.png"], "annie": ["annie_bg.png", "annie_h.png", "annie_l.png", "annie_d.png"], "dalia": ["dalia_bg.png", "dalia_h.png", "dalia_l.png", "dalia_d.png"], "alex": ["alex_bg.png", "alex_h.png", "alex_l.png", "alex_d.png"], "penelope": ["penelope_bg.png", "penelope_h.png", "penelope_l.png", "penelope_d.png"], "luna": ["luna_bg.png", "luna_h.png", "luna_l.png", "luna_d.png"], "nancy": ["nancy_bg.png", "nancy_h.png", "nancy_l.png", "nancy_d.png"], }
            if girl_sel in assets:
                add "gui/sp2/" + assets[girl_sel][0]
                if girl_sel == 'calypso':
                    add 'gui/sp2/calypso_h.png'
                else:
                    imagebutton:
                        idle "lk_" + girl_sel + str(looks[girl_sel][current_look]) 
                        hover Transform("lk_" + girl_sel + str(looks[girl_sel][current_look]), matrixcolor=BrightnessMatrix(0.1))
                        focus_mask True
                        action Show("look_choice", girl=girl_sel)
                        xoffset 500
                        yalign 0.5
                # add "gui/sp2/" + assets[girl_sel][1]
                if girl_sel == 'annie':
                    if interstellarm2:
                        use sc_sub_point(None, girl_sel, 'annie_d2.png')
                    else:
                        use sc_sub_point(None, girl_sel)
                elif girl_sel == 'nancy':
                    use sc_sub_point(None, girl_sel)
                elif girl_sel == 'penelope':
                    use sc_sub_point(None, girl_sel)
                elif girl_sel == 'dalia':
                    use sc_sub_point(None, girl_sel)
                elif girl_sel == 'luna':
                    use sc_sub_point(None, girl_sel)
                elif girl_sel == 'alex':
                    use sc_sub_point(None, girl_sel)
                elif girl_sel == 'nova':
                    use sc_sub_point(None, girl_sel)
                elif girl_sel == 'calypso':
                    use sc_sub_point(None, girl_sel)
                if girl_sel != 'calypso':
                    key [ "input_right", "rollforward", "skip" ]:
                        action If( current_look == len(looks[girl_sel])-1, SetVariable("current_look", 0),  SetVariable("current_look", current_look + 1) )
                    key [ "input_left", "rollback" ]:
                        action If( current_look == 0, SetVariable("current_look", len(looks[girl_sel])-1), SetVariable("current_look", current_look - 1) )
    if c_hovered is not None: ## THE ONLY REASON WHY THIS ISN'T CRUNCHED IS BECAUSE THE ANIMATION DOES NOT REPLAY IF THE C_HOVERED VALUE IMMEDIATELY CHANGES TO A DIFFERENT ONE THAT ISN'T 'NONE'
        if annieu:
            if c_hovered == "annie":
                if interstellarm2:
                    use sc_sub_point(c_hovered, None, 'annie_d2.png')
                else:
                    use sc_sub_point(c_hovered)
        if nancyu:
            if c_hovered == "nancy":
                use sc_sub_point(c_hovered)
        if penelopeu:
            if c_hovered == "penelope":
                use sc_sub_point(c_hovered)
        if daliau:
            if c_hovered == "dalia":
                use sc_sub_point(c_hovered)
        if lunau:
            if c_hovered == "luna":
                use sc_sub_point(c_hovered)
        if alexu:
            if c_hovered == "alex":
                use sc_sub_point(c_hovered)
        if novau:
            if c_hovered == "nova":
                use sc_sub_point(c_hovered)
        if calypsou:
            if c_hovered == "calypso":
                use sc_sub_point(c_hovered)
    frame:
        background None
        if girl_sel is not None:
            if c_hovered is not None:
                at transform:
                    easein_quint (0.5 * persistent.motion) yoffset 0 alpha 0.8
            else:
                at transform:
                    easein_quint (0.5 * persistent.motion) yoffset 250 alpha 0.5
        elif girl_sel is None:
            at transform:
                easein_quint (0.5 * persistent.motion) yoffset 0 alpha 1.0
        else:
            at transform:
                alpha 1.0
        if calypsou:
            button:
                xycenter (.5, .5)
                frame:
                    xysize   (config.screen_width, config.screen_height)
                    xycenter (.5, .5)
                    if not getattr(store, 'calypsou'):
                        if not getattr(store, 'calypsopath'):
                            image Transform('gui/sp2/calypso_idle.png', matrixcolor = SaturationMatrix(.0)) xycenter (.5, .5)
                            image Transform('gui/sp2/calypso_hover.png', matrixcolor = SaturationMatrix(.0)) xycenter (.5, .5):
                                at transform:
                                    alpha .0
                                    on idle:
                                        easein_quint (1.0 * persistent.motion) alpha .0
                                    on hover:
                                        easein_quint (1.0 * persistent.motion) alpha 1.0
                        else:
                            image Transform('gui/sp2/calypso_idle.png', blur = .7, matrixcolor = SaturationMatrix(.0)) xycenter (.5, .5)
                            image Transform('gui/sp2/calypso_hover.png', blur = .7, matrixcolor = SaturationMatrix(.0)) xycenter (.5, .5):
                                at transform:
                                    alpha .0
                                    on idle:
                                        easein_quint (1.0 * persistent.motion) alpha .0
                                    on hover:
                                        easein_quint (1.0 * persistent.motion) alpha 1.0
                    else:
                        image 'gui/sp2/calypso_idle.png' xycenter (.5, .5)
                        image 'gui/sp2/calypso_hover.png' xycenter (.5, .5):
                            at transform:
                                alpha .0
                                on idle:
                                    easein_quint (1.0 * persistent.motion) alpha .0
                                on hover:
                                    easein_quint (1.0 * persistent.motion) alpha 1.0
                    at pp2_fb(.4)
                focus_mask True
                if not getattr(store, 'calypsou'):
                    action NullAction()
                else:
                    action [
                        Play("soundlow", audio.button),
                        SetVariable("girl_sel", 'calypso')
                    ]
                hovered [SetVariable("c_hovered", None), SetVariable("c_hovered", 'calypso'), Play("sound", "neon.mp3")]
                unhovered [SetVariable("c_hovered", None)]
        else:
            button:
                focus_mask True
                xycenter (.5, .5)
                frame:
                    xysize   (config.screen_width, config.screen_height)
                    xycenter (.5, .5)
                    image "gui/sp2/others_idle.png" xycenter (.5, .5)
                    image "gui/sp2/others_hover.png" xycenter (.5, .5):
                        at transform:
                            alpha .0
                            on idle:
                                easein_quint (1.0 * persistent.motion) alpha .0
                            on hover:
                                easein_quint (1.0 * persistent.motion) alpha 1.0
                    at pp2_fb(.4)
                action [ Play("soundlow", audio.neon),
                        SetVariable("filter_scene", "all"),
                        SetVariable("filter_girl", "side"),
                        Show("gallery", transition=dissolve) ]
                hovered   [Play ("sound", "neon.mp3")]
        for char in characters:
            button:
                xycenter (.5, .5)
                frame:
                    xysize   (config.screen_width, config.screen_height)
                    xycenter (.5, .5)
                    if not getattr(store, char["met"]):
                        if not getattr(store, char["path"]):
                            image Transform(char["idle"], matrixcolor = SaturationMatrix(.0)) xycenter (.5, .5)
                            image Transform(char["hover"], matrixcolor = SaturationMatrix(.0)) xycenter (.5, .5):
                                at transform:
                                    alpha .0
                                    on idle:
                                        easein_quint (1.0 * persistent.motion) alpha .0
                                    on hover:
                                        easein_quint (1.0 * persistent.motion) alpha 1.0
                        else:
                            image Transform(char["idle"], blur = .7, matrixcolor = SaturationMatrix(.0)) xycenter (.5, .5)
                            image Transform(char["hover"], blur = .7, matrixcolor = SaturationMatrix(.0)) xycenter (.5, .5):
                                at transform:
                                    alpha .0
                                    on idle:
                                        easein_quint (1.0 * persistent.motion) alpha .0
                                    on hover:
                                        easein_quint (1.0 * persistent.motion) alpha 1.0
                    else:
                        image char["idle"] xycenter (.5, .5)
                        image char["hover"] xycenter (.5, .5):
                            at transform:
                                alpha .0
                                on idle:
                                    easein_quint (1.0 * persistent.motion) alpha .0
                                on hover:
                                    easein_quint (1.0 * persistent.motion) alpha 1.0
                    at pp2_fb(char["wait"])
                focus_mask True
                if not getattr(store, char["met"]):
                    action NullAction()
                else:
                    action [
                        Play("soundlow", audio.button),
                        SetVariable("current_look", renpy.random.randint(0, len(looks[char["look"]]) - 1)),
                        SetVariable("girl_sel", char["name"])
                    ]
                hovered [SetVariable("c_hovered", None), SetVariable("c_hovered", char["name"]), Play("sound", "neon.mp3")]
                unhovered [SetVariable("c_hovered", None)]
    button:
        focus_mask True
        xycenter (.5, .5)
        image "gui/sp2/gallery_idle.png" xycenter (.5, .5)
        image "gui/sp2/gallery_hover.png" xycenter (.5, .5):
            at transform:
                alpha .0
                on idle:
                    easein_quint (.5 * persistent.motion) alpha .0
                on hover:
                    easein_quint (.5 * persistent.motion) alpha 1.0
        if girl_sel is None:
            action [ Play("soundlow", audio.button),
                    SetVariable("filter_scene", "all"),
                    SetVariable("filter_girl", "all"),
                    Show("gallery", transition=dissolve) ]
        else:
            action [ Play("soundlow", audio.button),
                    SetVariable("filter_scene", "all"),
                    SetVariable("filter_girl", girl_sel),
                    Show("gallery", transition=dissolve) ]
    button:
        focus_mask True
        xycenter (.5, .5)
        image "gui/sp2/return_idle.png" xycenter (.5, .5)
        image "gui/sp2/return_hover.png" xycenter (.5, .5):
            at transform:
                alpha .0
                on idle:
                    easein_quint (.5 * persistent.motion) alpha .0
                on hover:
                    easein_quint (.5 * persistent.motion) alpha 1.0
        action [SetVariable("c_hovered", None), SetVariable("girl_sel", None), Return()]
    if money == 0:
        text "-" xalign 0.805 yalign 0.38 size 45 style "mytextnool" anchor (0.5, 0.5)
    elif money < 0:
        text "{color=#d52d2d}[money]" xalign 0.805 yalign 0.38 size 45 style "mytextnool" anchor (0.5, 0.5)
    else:
        text "[money]" xalign 0.805 yalign 0.38 size 45 style "mytextnool" anchor (0.5, 0.5)
    add "eternalsbios" xycenter (.38, .55)

    button:
        focus_mask True
        xycenter (.5, .5)
        image "mod_additions/cheats_idle.png" xycenter (.5, .5)
        image "mod_additions/cheats_hover.png" xycenter (.5, .5):
            at transform:
                alpha .0
                on idle:
                    easein_quint (.5 * persistent.motion) alpha .0
                on hover:
                    easein_quint (.5 * persistent.motion) alpha 1.0
        action ShowMenu("cheats")

screen sc_sub_point(hovered=None, selected=None, data=None):

    if selected:
        $ loc_points = getattr(store, selected + "_points")
        $ assets = { "nova": ["nova_bg.png", "nova_h.png", "nova_l.png", "nova_d.png"], "calypso": ["calypso_bg.png", "calypso_h.png", "calypso_l.png", "calypso_d.png"], "annie": ["annie_bg.png", "annie_h.png", "annie_l.png", "annie_d.png"], "dalia": ["dalia_bg.png", "dalia_h.png", "dalia_l.png", "dalia_d.png"], "alex": ["alex_bg.png", "alex_h.png", "alex_l.png", "alex_d.png"], "penelope": ["penelope_bg.png", "penelope_h.png", "penelope_l.png", "penelope_d.png"], "luna": ["luna_bg.png", "luna_h.png", "luna_l.png", "luna_d.png"], "nancy": ["nancy_bg.png", "nancy_h.png", "nancy_l.png", "nancy_d.png"], }
        add "gui/sp2/" + assets[selected][2]
        if data:
            add "gui/sp2/" + data
        else:
            add "gui/sp2/" + assets[selected][3]
        add "gui/sp2/relationship.png"
        hbox:
            pos (32, 350)
            spacing -36
            add "bios_heart_on"
            for i in range(2, 7):
                if getattr(girls_hearts[selected], f"hearts{i}") != -1 and loc_points >= getattr(girls_hearts[selected], f"hearts{i}"):
                    add "bios_heart_on"
                else:
                    add "bios_heart_off"
    else:
        $ loc_points = getattr(store, hovered + "_points")
        add "gui/sp2/" + str(hovered) + "_bg.png" at pp2_fade_in
        if hovered == "calypso":
            add 'gui/sp2/calypso_h.png' at pp2_fl
        else:
            add "lk_" + hovered + str(looks[hovered][current_look] if 0 <= current_look < len(looks[hovered]) else 0) xoffset 500 at pp2_fl
        add "gui/sp2/" + str(hovered) + "_l.png" at fbottom(0.0)
        if data:
            add "gui/sp2/" + data at fbottom(0.1)
        else:
            add "gui/sp2/" + str(hovered) + "_d.png" at fbottom(0.1)
        add "gui/sp2/relationship.png" at fbottom(0.05)
        hbox:
            pos (32, 350)
            spacing -36
            add "bios_heart_on"
            for i in range(2, 7):
                if getattr(girls_hearts[hovered], f"hearts{i}") != -1 and loc_points >= getattr(girls_hearts[hovered], f"hearts{i}"):
                    add "bios_heart_on"
                else:
                    add "bios_heart_off"
            at hearts_h()