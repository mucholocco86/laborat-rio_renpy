#---------------------adds/enhancements for screens.rpy---------------------#



#---------------------dialog/choice options---------------------#
# define gui.name_xpos = 360
# define gui.dialogue_xpos = 402
# define gui.dialogue_width = 1116

define gui.text_outlines = [ (absolute(2), "#000", absolute(0), absolute(0)) ]

init 1001:
    define centered = Character("CenteredKoGa3", what_text_align=0.5)  #"CenteredKoGa3" is a dummy char. and not shown

    # Main Characters
    define mc = DynamicCharacter("name", color="#009de0")
    define a = Character("Alexis", color="#fe1f3e")
    define m = Character("Emily", color="#e265e3")
    define er = Character("Erynn", color="#ce0278")
    define me = Character("Melissa", color="#47f747")
    define la = Character("Layla", color="#18fcff")
    define el = Character("Elena", color="#fee315")
    define ni = Character("Nikki", color="#631485")
    define c = Character("Cara", color="#ae22b4")
    define va = Character("Valeria", color="#fc4f11")
    define ir = Character("Iris", color="#42cb86")
    define sa = Character("Santiago", color="#5099c3")
    define sn = Character("Mr Navarro", color="#5099c3")
    define jo = Character("John", color="#5099c3")
    define to = Character("Tori", color="#6769c0")
    define da = Character("Darryl", color="#5099c3")
    define et = Character("Ethan", color="#5099c3")
    define tr = Character("Gabriela (Ms Ramirez)", color="#ffb954")

    # Side Characters
    define d = Character("Andres", color="#5099c3")
    define ln = Character("Lakeyn", color="#4272cb")
    define br = Character("Brooke", color="#fb6161")
    define am = Character("Adriana", color="#3c6480")
    define mr = Character("Mira", color="#a6f6cd")
    define ha = Character("Haley", color="#5099c3")
    define z = Character("Zach", color="#5099c3")
    define na = Character("Nathan", color="#5099c3")
    define sc = Character("Sha'Carri", color="#5099c3")
    define tj = Character("TJ", color="#5099c3")
    define si = Character("Sienna", color="#5099c3")
    define dr = Character("Daniela", color="#5099c3")
    define pe = Character("Peyton", color="#5099c3")
    define jz = Character("Jasmine", color="#FFFFFF")
    define zo = Character("Enzo", color="#5099c3")
    define xv = Character("Ximena (Ms Vergara)", color="#9242ff")
    define so = Character("Marisol", color="#9242ff")
    define tm = Character("Coach (Mike)", color="#5099c3")
    define do = Character("Mr Donovan", color="#5099c3")
    define bd = Character("Dylan", color="#5099c3")
    define gi = Character("Gianna", color="#5099c3")
    define ma = Character("Mateo", color="#5099c3")
    define di = Character("Diego", color="#5099c3")
    define av = Character("Ava", color="#5099c3")
    define ra = Character("Rachel", color="#5099c3")
    define ju = Character("Julia", color="#5099c3")
    define ih = Character("Isaiah", color="#5099c3")
    define zn = Character("Zane", color="#5099c3")

    # Background Characters
    define nt = Character("Natasha", color="#FFFFFF")
    define ar = Character("Amare", color="#FFFFFF")
    define mk = Character("MacKenzie", color="#FFFFFF")
    define le = Character("Leah", color="#FFFFFF")
    define tc = Character("Mr Coleman", color="#FFFFFF")
    define td = Character("Naomi (Ms Davis)", color="#FFFFFF")
    define bt = Character("Bartender", color="#FFFFFF")
    define ba = Character("Barrista", color="#FFFFFF")
    define em = Character("Emanuel", color="#FFFFFF")
    define mg = Character("Miguel", color="#FFFFFF")
    define ca = Character("Callum", color="#FFFFFF")
    define th = Character("Theo", color="#FFFFFF")
    define cl = Character("Colin", color="#FFFFFF")
    define ai = Character("Aiden", color="#FFFFFF")
    define t = Character("Teacher", color="#FFFFFF")
    define pt = Character("Personal Trainer", color="#FFFFFF")
    define x = Character("???", color="#FFFFFF")
    define n = Character("", color="#FFFFFF")
    define pi = Character("Pilot", color="#FFFFFF")
    define fa = Character("Flight Attendant", color="#FFFFFF")
    define re = Character("Receptionist", color="#FFFFFF")
    define pa = Character("Parent", color="#FFFFFF")
    define rs = Character("Rose", color="#FFFFFF")
    define mi = Character("Michelle", color="#FFFFFF")
    define ky = Character("Kaylin", color="#FFFFFF") #Messe
    define ja = Character("Jaylen", color="#FFFFFF")
    define ro = Character("Rob", color="#FFFFFF")
    define jl = Character("Julian", color="#FFFFFF")
    define no = Character("Noah", color="#FFFFFF")
    define se = Character("Sebastian", color="#FFFFFF")
    define mo = Character("Monique", color="#FFFFFF")
    define je = Character("Jenna", color="#FFFFFF")
    define gb = Character("Gil Burke", color="#FFFFFF")
    define wa = Character("Walter", color="#FFFFFF")
    define sq = Character("Shaq", color="#FFFFFF")
    define ka = Character("Kaley", color="#FFFFFF")
    define hn = Character("Hannah", color="#FFFFFF")
    define ow = Character("Owen", color="#FFFFFF")
    define ml = Character("Miles", color="#FFFFFF")
    define ys = Character("Yellow Snow", color="#FFFFFF")
    define cr = Character("Crowd", color="#FFFFFF")
    define yi = Character("Singer", color="#FFFFFF")
    define yd = Character("Drummer", color="#FFFFFF")
    define yb = Character("Bassist", color="#FFFFFF")
    define yg = Character("Guitarist", color="#FFFFFF")
    define an = Character("Announcer", color="#FFFFFF")
    define ph = Character("Photographer", color="#FFFFFF")
    define pz = Character("Paparazzi", color="#FFFFFF")
    define ge = Character("Gym employee", color="#FFFFFF")
    define st = Character("Student(s)", color="#FFFFFF")
    define aa = Character("Together", color="#FFFFFF")
    define ab = Character("Nikki, [mc]", color="#FFFFFF")
    define ac = Character("Everyone", color="#FFFFFF")
    define gu = Character("Guest", color="#FFFFFF")
    define gr = Character("Girl", color="#FFFFFF")
    define gy = Character("Guy", color="#FFFFFF")
    define dg = Character("Dog", color="#FFFFFF")
    define co = Character("Commentator", color="#FFFFFF")


define KoGa3xpos2default = 570
define KoGa3xpos1default = 612
define KoGa3xsize1default = 744
define KoGa3ypos1default = 205
define KoGa3ypos2default = 230
define KoGa3ypos3default = 250
define KoGa3ypos4default = 250
screen say(who, what):
    style_prefix "say"

    if who == "CenteredKoGa3":  #for centered text
        $ persistent.pref_text_size2 = persistent.pref_text_size + 15
        $ KoGa3xpos2 = KoGa3xpos2default - (6 * persistent.pref_text_size) - persistent.KoGa3xposOffset
        $ KoGa3xpos1 = KoGa3xpos1default - (6 * persistent.pref_text_size) - persistent.KoGa3xposOffset
        $ KoGa3xsize1 = KoGa3xsize1default + (12 * persistent.pref_text_size) + (2 * persistent.KoGa3xposOffset)
        if persistent.pref_text_size > 20:
            $ KoGa3ypos1 = KoGa3ypos1default - (6 * persistent.pref_text_size + persistent.KoGa3yposOffset)
            $ KoGa3ypos2 = KoGa3ypos2default - (6 * persistent.pref_text_size + persistent.KoGa3yposOffset)
            $ KoGa3ypos3 = KoGa3ypos3default - (5 * persistent.pref_text_size + persistent.KoGa3yposOffset)
            $ KoGa3ypos4 = KoGa3ypos4default - (5 * persistent.pref_text_size + persistent.KoGa3yposOffset)
        else:
            $ KoGa3ypos1 = KoGa3ypos1default - (6 * 20 + persistent.KoGa3yposOffset)
            $ KoGa3ypos2 = KoGa3ypos2default - (6 * 20 + persistent.KoGa3yposOffset)
            $ KoGa3ypos3 = KoGa3ypos3default - (5 * 20 + persistent.KoGa3yposOffset)
            $ KoGa3ypos4 = KoGa3ypos4default - (5 * 20 + persistent.KoGa3yposOffset)
        text what id "what" xalign 0.5 yalign 0.5 size persistent.pref_text_size outlines [ (absolute(persistent.KoGa3TextOutline1), "#000", absolute(persistent.KoGa3TextOutline2), absolute(persistent.KoGa3TextOutline3)) ]

    else:
        window:
            id "window"
            $ persistent.pref_text_size2 = persistent.pref_text_size + 15
            $ KoGa3xpos2 = KoGa3xpos2default - (6 * persistent.pref_text_size) - persistent.KoGa3xposOffset
            $ KoGa3xpos1 = KoGa3xpos1default - (6 * persistent.pref_text_size) - persistent.KoGa3xposOffset
            $ KoGa3xsize1 = KoGa3xsize1default + (12 * persistent.pref_text_size) + (2 * persistent.KoGa3xposOffset)
            if persistent.pref_text_size > 20:
                $ KoGa3ypos1 = KoGa3ypos1default - (6 * persistent.pref_text_size + persistent.KoGa3yposOffset)
                $ KoGa3ypos2 = KoGa3ypos2default - (6 * persistent.pref_text_size + persistent.KoGa3yposOffset)
                $ KoGa3ypos3 = KoGa3ypos3default - (5 * persistent.pref_text_size + persistent.KoGa3yposOffset)
                $ KoGa3ypos4 = KoGa3ypos4default - (5 * persistent.pref_text_size + persistent.KoGa3yposOffset)
            else:
                $ KoGa3ypos1 = KoGa3ypos1default - (6 * 20 + persistent.KoGa3yposOffset)
                $ KoGa3ypos2 = KoGa3ypos2default - (6 * 20 + persistent.KoGa3yposOffset)
                $ KoGa3ypos3 = KoGa3ypos3default - (5 * 20 + persistent.KoGa3yposOffset)
                $ KoGa3ypos4 = KoGa3ypos4default - (5 * 20 + persistent.KoGa3yposOffset)

            if who is not None:
                if what != "" and what != None:
                    if KoGa3xpos1 >= 320:
                        window background Transform(Image("textboxHigh.png",xalign=0.5, ypos=KoGa3ypos1), alpha=persistent.KoGa3TextboxOpacity)
                    else:
                        window background Transform(Image("textboxHighWide.png",xalign=0.5, ypos=KoGa3ypos1), alpha=persistent.KoGa3TextboxOpacity)
                window:
                    id "namebox"
                    style "namebox"
                    if persistent.KoGa3DialogCentered == False:
                        xpos KoGa3xpos2
                    else:
                        xalign 0.5
                    ypos KoGa3ypos2
                    text who id "who" size persistent.pref_text_size2 outlines [ (absolute(persistent.KoGa3TextOutline1), "#000", absolute(persistent.KoGa3TextOutline2), absolute(persistent.KoGa3TextOutline3)) ]
                if persistent.KoGa3DialogCentered == False:
                    text what id "what" xpos KoGa3xpos1 xsize KoGa3xsize1 ypos KoGa3ypos3 size persistent.pref_text_size outlines [ (absolute(persistent.KoGa3TextOutline1), "#000", absolute(persistent.KoGa3TextOutline2), absolute(persistent.KoGa3TextOutline3)) ]
                else:
                    text what id "what" xalign 0.5 xsize KoGa3xsize1 ypos KoGa3ypos3 size persistent.pref_text_size outlines [ (absolute(persistent.KoGa3TextOutline1), "#000", absolute(persistent.KoGa3TextOutline2), absolute(persistent.KoGa3TextOutline3)) ]
            else:
                if what != "" and what != None:
                    if KoGa3xpos1 >= 320:
                        window background Transform(Image("textboxHigh.png",xalign=0.5, ypos=KoGa3ypos1), alpha=persistent.KoGa3TextboxOpacity)
                    else:
                        window background Transform(Image("textboxHighWide.png",xalign=0.5, ypos=KoGa3ypos1), alpha=persistent.KoGa3TextboxOpacity)
                if persistent.KoGa3DialogCentered == False:
                    text what id "what" xpos KoGa3xpos1 xsize KoGa3xsize1 ypos KoGa3ypos4 size persistent.pref_text_size outlines [ (absolute(persistent.KoGa3TextOutline1), "#000", absolute(persistent.KoGa3TextOutline2), absolute(persistent.KoGa3TextOutline3)) ]
                else:
                    text what id "what" xalign 0.5 xsize KoGa3xsize1 ypos KoGa3ypos4 size persistent.pref_text_size outlines [ (absolute(persistent.KoGa3TextOutline1), "#000", absolute(persistent.KoGa3TextOutline2), absolute(persistent.KoGa3TextOutline3)) ]


    ## If there's a side image, display it above the text. Do not display on the
    ## phone variant - there's no room.
    if persistent.KoGa3SideImage is True and KoGa3xpos1 >= 320:
        add SideImage() xalign 0.0 yalign 1.00

define KoGa3TextboxOpacitydefault = 0.0
define KoGa3TextOutline1default = 3                         #Android: 4
define KoGa3TextOutline2default = 0
define KoGa3TextOutline3default = 0
define pref_text_sizedefault = 32                           #Android: 38
define KoGa3xposOffsetdefault = 0
define KoGa3yposOffsetdefault = 0

define persistent.KoGa3TextboxOpacity = KoGa3TextboxOpacitydefault
define persistent.KoGa3TextOutline1 = KoGa3TextOutline1default
define persistent.KoGa3TextOutline2 = KoGa3TextOutline2default
define persistent.KoGa3TextOutline3 = KoGa3TextOutline3default
define persistent.pref_text_size = pref_text_sizedefault
define persistent.KoGa3xposOffset = KoGa3xposOffsetdefault
define persistent.KoGa3yposOffset = KoGa3yposOffsetdefault
define persistent.KoGa3SideImage = True
define persistent.KoGa3OriginalInfoScreen = True
define persistent.KoGa3DialogCentered = False


style window:
    xalign 0.5
    xfill True
    yalign gui.textbox_yalign
    ysize gui.textbox_height

    background (None)

style say_label:
    properties gui.text_properties("name", accent=True)
    xalign 0.0
    xpos 0
    yalign 1.0

style say_dialogue:
    properties gui.text_properties("dialogue")
    xalign 0.0
    xpos gui.dialogue_xpos
    xsize gui.dialogue_width
    yalign 0.0
    ypos gui.dialogue_ypos


style input_prompt:
    xalign gui.dialogue_text_xalign
    properties gui.text_properties("input_prompt") outlines [ (absolute(2), "#000", absolute(0), absolute(0)) ]

style input:
    xalign gui.dialogue_text_xalign
    xmaximum gui.dialogue_width
    properties gui.text_properties("input") outlines [ (absolute(2), "#000", absolute(0), absolute(0)) ]

# screen input(prompt): #only if needed
    # style_prefix "input"
    # window:
        # if renpy.android==True:
            # yalign 0.0
        # vbox:
            # xalign gui.dialogue_text_xalign
            # xpos gui.dialogue_xpos
            # xsize gui.dialogue_width
            # ypos gui.dialogue_ypos
            # text prompt style "input_prompt"
            # input id "input"



#---------------------Choices---------------------#
define KoGa3ChoiceTextSizedefault = 30                      #Android: 36
define KoGa3TextOutline7default = 2
define KoGa3TextOutline8default = 0
define KoGa3TextOutline9default = 0
define KoGa3ChoiceYposdefault = 0
define KoGa3ChoiceButtonWidthdefault = 1100                 #Android: 1300
define persistent.KoGa3ChoiceBackground = True
define persistent.KoGa3ChoiceAlign = "center"
define persistent.KoGa3ChoiceTextSize = KoGa3ChoiceTextSizedefault
define persistent.KoGa3TextOutline7 = KoGa3TextOutline7default
define persistent.KoGa3TextOutline8 = KoGa3TextOutline8default
define persistent.KoGa3TextOutline9 = KoGa3TextOutline9default
define persistent.KoGa3ChoiceYpos = KoGa3ChoiceYposdefault
define persistent.KoGa3ChoiceButtonWidth = KoGa3ChoiceButtonWidthdefault

define gui.choice_button_height = None
define gui.choice_button_tile = False
define gui.choice_button_borders = Borders(75, 15, 75, 15)
define gui.choice_button_text_font = gui.text_font
define gui.choice_button_text_size = gui.text_size
define gui.choice_button_text_xalign = 0.5
define gui.choice_button_text_idle_color = "#cccccc"
define gui.choice_button_text_hover_color = "#ffffff"
define gui.choice_button_text_insensitive_color = "#444444"

style choice_left is choice
style choice_right is choice
style choice_left_vbox is choice_vbox
style choice_left_button is choice_button
style choice_left_button_text is choice_button_text
style choice_right_vbox is choice_vbox
style choice_right_button is choice_button
style choice_right_button_text is choice_button_text
style choice_vbox:
    xalign 0.5
    yalign 0.5
    yanchor 0.5

    spacing gui.choice_spacing

style choice_left_vbox:
    xalign 0.0
    yalign 0.5
    yanchor 0.5

    spacing gui.choice_spacing

style choice_right_vbox:
    xalign 1.0
    yalign 0.5
    yanchor 0.5

    spacing gui.choice_spacing

init 999:
    screen choice(items):

        if persistent.KoGa3ChoiceAlign == "left":
            style_prefix "choice_left"
        elif persistent.KoGa3ChoiceAlign == "right":
            style_prefix "choice_right"
        else:
            style_prefix "choice"
        if not renpy.loadable("1Mod.rpyc"):
            vbox:
                ypos 1080 - persistent.KoGa3ChoiceYpos - 450                      #550 for ~middle position
                $ gui.choice_button_text_xalign = 0.0
                $ gui.choice_text_xalign = 0.0
                for i in items:
                    $ _cx_marker = u"{color=#d10089}•{/color}  " if cx_is_seen(i.caption) else u""
                    if persistent.KoGa3ChoiceAlign == "left":
                        $ gui.choice_button_text_xalign = 0.0
                        $ text_xalign_koga3 = 0.0
                    elif persistent.KoGa3ChoiceAlign == "right":
                        $ gui.choice_button_text_xalign = 1.0
                        $ text_xalign_koga3 = 1.0
                    else:
                        $ gui.choice_button_text_xalign = 0.5
                        $ text_xalign_koga3 = 0.5
                    textbutton (_cx_marker + i.caption):
                        action [Function(cx_record_choice, i.caption), i.action]
                        if persistent.KoGa3ChoiceBackground == False:
                            background None
                        # idle_background "gui/button/choice_idle_background.png"
                        # hover_background "gui/button/choice_hover_background.png"
                        text_outlines [ ( persistent.KoGa3TextOutline7, "#000",  persistent.KoGa3TextOutline8,  persistent.KoGa3TextOutline9) ]
                        text_size persistent.KoGa3ChoiceTextSize
                        xsize persistent.KoGa3ChoiceButtonWidth
                        text_xalign text_xalign_koga3
                        text_textalign text_xalign_koga3    #works only on newer RenPy versions

        else:
            vbox:
                ypos 1080 - persistent.KoGa3ChoiceYpos - 450    #550 for ~middle position
                for i in items:
                    if persistent.KoGa3ChoiceAlign == "left":
                        $ gui.choice_button_text_xalign = 0.0
                        $ text_xalign_koga3 = 0.0
                    elif persistent.KoGa3ChoiceAlign == "right":
                        $ gui.choice_button_text_xalign = 1.0
                        $ text_xalign_koga3 = 1.0
                    else:
                        $ gui.choice_button_text_xalign = 0.5
                        $ text_xalign_koga3 = 0.5
                    if i.kwargs and i.kwargs.get("wt") and persistent.wt:
                        
                        textbutton "%s \n{size=-8}(%s{/color})" % (i.caption, i.kwargs["wt"]) action i.action:
                            text_outlines [ ( persistent.KoGa3TextOutline7, "#000",  persistent.KoGa3TextOutline8,  persistent.KoGa3TextOutline9) ]
                            if persistent.KoGa3ChoiceBackground == False:
                                background None
                            text_size persistent.KoGa3ChoiceTextSize
                            xsize persistent.KoGa3ChoiceButtonWidth
                    elif i.kwargs and i.kwargs.get("wtcol") and persistent.wt:
                        textbutton "{color=#33ff33}%s {/color}" % (i.caption)   action i.action:
                            text_outlines [ ( persistent.KoGa3TextOutline7, "#000",  persistent.KoGa3TextOutline8,  persistent.KoGa3TextOutline9) ]
                            if persistent.KoGa3ChoiceBackground == False:
                                background None
                            text_size persistent.KoGa3ChoiceTextSize
                            xsize persistent.KoGa3ChoiceButtonWidth

                    else:    
                        textbutton i.caption action i.action:
                            text_outlines [ ( persistent.KoGa3TextOutline7, "#000",  persistent.KoGa3TextOutline8,  persistent.KoGa3TextOutline9) ]
                            if persistent.KoGa3ChoiceBackground == False:
                                background None
                            text_size persistent.KoGa3ChoiceTextSize
                            xsize persistent.KoGa3ChoiceButtonWidth



#---------------------Quick menu---------------------#
define persistent.KoGa3QuickMenuButton = 1
define persistent.KoGa3QuickMenuShow = 1
define persistent.KoGa3_QuickMenu1_button_font = "KoGa3_QuickMenu1_button_text"
define KoGa3QuickMenuTextSizedefault = 20                   #Android: 25
define KoGa3TextOutline4default = 2
define KoGa3TextOutline5default = 0
define KoGa3TextOutline6default = 0
define persistent.KoGa3QuickMenuTextSize = KoGa3QuickMenuTextSizedefault
define persistent.KoGa3TextOutline4 = KoGa3TextOutline4default
define persistent.KoGa3TextOutline5 = KoGa3TextOutline5default
define persistent.KoGa3TextOutline6 = KoGa3TextOutline6default

define persistent.KoGa3QuickMenuItemBack = True
define persistent.KoGa3QuickMenuItemHist = False
define persistent.KoGa3QuickMenuItemHide = False
define persistent.KoGa3QuickMenuItemSkip = True
define persistent.KoGa3QuickMenuItemAuto = True
define persistent.KoGa3QuickMenuItemSave = True
define persistent.KoGa3QuickMenuItemLoad = True
define persistent.KoGa3QuickMenuItemQSave = True
define persistent.KoGa3QuickMenuItemQLoad = True
define persistent.KoGa3QuickMenuItemPrefs = True
define persistent.KoGa3QuickMenuItemModmenu = True
define persistent.KoGa3QuickMenuIcons = True

define quick_menu = True
init 999:
    screen quick_menu():
        variant ("small", "medium", "large")
        ## Ensure this appears on top of other screens.
        zorder 100
        default p_qm = None #for music addons
        if persistent.KoGa3QuickMenuButton == 2:
            if persistent.KoGa3QuickMenuTextSize >= 28:
                mousearea:
                    area (0, 1000, 1920, 80)
                    hovered SetVariable("persistent.KoGa3QuickMenuShow", 1)
                    unhovered SetVariable("persistent.KoGa3QuickMenuShow", 0)
            else:
                mousearea:
                    area (0, 1040, 1920, 40)
                    hovered SetVariable("persistent.KoGa3QuickMenuShow", 1)
                    unhovered SetVariable("persistent.KoGa3QuickMenuShow", 0)

        if persistent.KoGa3QuickMenuShow == 1:

            if persistent.KoGa3QuickMenuIcons is True:
                hbox:
                    style_prefix "quick"
                    $ persistent.KoGa3_QuickMenu1_button_font = "KoGa3_QuickMenu1_button_text"
                    $ persistent.KoGa3_QuickMenu2_button_font = "KoGa3_QuickMenu2_button_text"
                    xalign 0.5
                    yalign 1.0
                    spacing 14
                    if persistent.KoGa3QuickMenuItemBack:
                        textbutton _("⟲"):
                            text_style persistent.KoGa3_QuickMenu1_button_font
                            text_size persistent.KoGa3QuickMenuTextSize
                            text_outlines [ (absolute(persistent.KoGa3TextOutline4), "#000", absolute(persistent.KoGa3TextOutline5), absolute(persistent.KoGa3TextOutline6)) ]
                            action Rollback()
                    if persistent.KoGa3QuickMenuItemHist:
                        textbutton _("≡"):
                            text_style persistent.KoGa3_QuickMenu1_button_font
                            text_size persistent.KoGa3QuickMenuTextSize
                            text_outlines [ (absolute(persistent.KoGa3TextOutline4), "#000", absolute(persistent.KoGa3TextOutline5), absolute(persistent.KoGa3TextOutline6)) ]
                            action ShowMenu('history')
                    if persistent.KoGa3QuickMenuItemHide:
                        textbutton _("▼"):
                            text_style persistent.KoGa3_QuickMenu1_button_font
                            text_size persistent.KoGa3QuickMenuTextSize
                            text_outlines [ (absolute(persistent.KoGa3TextOutline4), "#000", absolute(persistent.KoGa3TextOutline5), absolute(persistent.KoGa3TextOutline6)) ]
                            action HideInterface()
                    if persistent.KoGa3QuickMenuItemSkip:
                        textbutton _("►►"):
                            text_style persistent.KoGa3_QuickMenu1_button_font
                            text_size persistent.KoGa3QuickMenuTextSize
                            text_outlines [ (absolute(persistent.KoGa3TextOutline4), "#000", absolute(persistent.KoGa3TextOutline5), absolute(persistent.KoGa3TextOutline6)) ]
                            action Skip() alternate Skip(fast=True, confirm=True)
                    if persistent.KoGa3QuickMenuItemAuto:
                        if preferences.afm_enable:
                            textbutton _("■"):
                                selected False
                                text_style persistent.KoGa3_QuickMenu1_button_font
                                text_size persistent.KoGa3QuickMenuTextSize
                                text_outlines [ (absolute(persistent.KoGa3TextOutline4), "#000", absolute(persistent.KoGa3TextOutline5), absolute(persistent.KoGa3TextOutline6)) ]
                                action Preference("auto-forward", "toggle")
                        else:
                            textbutton _("►"):
                                text_style persistent.KoGa3_QuickMenu1_button_font
                                text_size persistent.KoGa3QuickMenuTextSize
                                text_outlines [ (absolute(persistent.KoGa3TextOutline4), "#000", absolute(persistent.KoGa3TextOutline5), absolute(persistent.KoGa3TextOutline6)) ]
                                action Preference("auto-forward", "toggle")

                    if persistent.KoGa3QuickMenuItemSave:
                        # textbutton _("➘{size=-2}💾{/size}"): 
                        textbutton _("➘◰"): 
                            text_style persistent.KoGa3_QuickMenu1_button_font
                            text_size persistent.KoGa3QuickMenuTextSize
                            text_outlines [ (absolute(persistent.KoGa3TextOutline4), "#000", absolute(persistent.KoGa3TextOutline5), absolute(persistent.KoGa3TextOutline6)) ]
                            action ShowMenu('save')
                    if persistent.KoGa3QuickMenuItemLoad:
                        # textbutton _("{size=-2}💾{/size}➚"): 
                        textbutton _("◰➚"): 
                            text_style persistent.KoGa3_QuickMenu1_button_font
                            text_size persistent.KoGa3QuickMenuTextSize
                            text_outlines [ (absolute(persistent.KoGa3TextOutline4), "#000", absolute(persistent.KoGa3TextOutline5), absolute(persistent.KoGa3TextOutline6)) ]
                            action ShowMenu('load')
                    if persistent.KoGa3QuickMenuItemQSave:
                        textbutton _("➘Q"):
                            text_style persistent.KoGa3_QuickMenu1_button_font
                            text_size persistent.KoGa3QuickMenuTextSize
                            text_outlines [ (absolute(persistent.KoGa3TextOutline4), "#000", absolute(persistent.KoGa3TextOutline5), absolute(persistent.KoGa3TextOutline6)) ]
                            action QuickSave()
                    if persistent.KoGa3QuickMenuItemQLoad:
                        textbutton _("Q➚"):
                            text_style persistent.KoGa3_QuickMenu1_button_font
                            text_size persistent.KoGa3QuickMenuTextSize
                            text_outlines [ (absolute(persistent.KoGa3TextOutline4), "#000", absolute(persistent.KoGa3TextOutline5), absolute(persistent.KoGa3TextOutline6)) ]
                            action QuickLoad()
                    if persistent.KoGa3QuickMenuItemPrefs:
                        textbutton _("⇲"):
                            text_style persistent.KoGa3_QuickMenu1_button_font
                            text_size persistent.KoGa3QuickMenuTextSize
                            text_outlines [ (absolute(persistent.KoGa3TextOutline4), "#000", absolute(persistent.KoGa3TextOutline5), absolute(persistent.KoGa3TextOutline6)) ]
                            action ShowMenu('preferences')
                    if persistent.KoGa3QuickMenuItemModmenu:
                        hbox:
                            spacing 10
                            if KoGa3ModMenuButtonPressed == False:
                                textbutton _("{k=-1.2}Mod{/k}"):
                                    text_style persistent.KoGa3_QuickMenu1_button_font
                                    text_size persistent.KoGa3QuickMenuTextSize
                                    text_outlines [ (absolute(persistent.KoGa3TextOutline4), "#000", absolute(persistent.KoGa3TextOutline5), absolute(persistent.KoGa3TextOutline6)) ]
                                    selected False 
                                    action [ 
                                    SetVariable ("Alexis_PointsTemp", Alexis_Points),
                                    SetVariable ("Emily_PointsTemp", Emily_Points),
                                    SetVariable ("Melissa_PointsTemp", Melissa_Points),
                                    SetVariable ("Erynn_PointsTemp", Erynn_Points),
                                    SetVariable ("Layla_PointsTemp", Layla_Points),
                                    SetVariable ("Elena_PointsTemp", Elena_Points),
                                    SetVariable ("Nikki_PointsTemp", Nikki_Points),
                                    SetVariable ("Cara_PointsTemp", Cara_Points),
                                    SetVariable ("Tori_PointsTemp", Tori_Points),
                                    SetVariable ("Adriana_PointsTemp", Adriana_Points),
                                    SetVariable ("Naomi_PointsTemp", Naomi_Points),
                                    SetVariable ("Nikki_Weekend_PointsTemp", Nikki_Weekend_Points),
                                    SetVariable ("Cara_Weekend_PointsTemp", Cara_Weekend_Points),
                                    SetVariable ("Gabi_PointsTemp", Gabi_Points),               #not used
                                    SetVariable ("Natasha_PointsTemp", Natasha_Points),         #not used
                                    SetVariable ("Lakeyn_PointsTemp", Lakeyn_Points),
                                    SetVariable ("Valeria_PointsTemp", Valeria_Points),
                                    SetVariable ("Sienna_PointsTemp", Sienna_Points),
                                    SetVariable ("Brooke_PointsTemp", Brooke_Points),
                                    SetVariable ("Iris_PointsTemp", Iris_Points),
                                    SetVariable ("Zach_PointsTemp", Zach_Points),
                                    SetVariable ("Nikki_Visit_PointsTemp", Nikki_Visit_Points),
                                    SetVariable ("Cara_Visit_PointsTemp", Cara_Visit_Points),
                                    SetVariable ("Alexis_JealousyPointsTemp", Alexis_JealousyPoints),
                                    SetVariable ("Mira_PointsTemp", Mira_Points),               #not used
                                    SetVariable ("Alexis_SPTemp", Alexis_SP),                   #added with v0.13
                                    SetVariable ("Nikki_SPointsTemp", Nikki_SPoints),           #new with v0.13
                                    SetVariable ("MC_GoodStudentTemp", MC_GoodStudent),         #new with v0.10.5
                                    SetVariable ("Alexis_BeachPointsTemp", Alexis_BeachPoints), #new with v0.11
                                    SetVariable ("Gabi_SuspicionTemp", Gabi_Suspicion),         #new with v0.14
                                    SetVariable ("Gabi_JealousyTemp", Gabi_Jealousy),           #new with v0.14
                                    SetVariable ("Andres_PointsTemp", Andres_Points),           #new with v0.14
                                    SetVariable ("Darryl_PointsTemp", Darryl_Points),           #new with v0.15
                                    SetVariable ("Marisol_PointsTemp", Marisol_Points),         #new with v0.15
                                    SetVariable ("Ximena_PointsTemp", Ximena_Points),           #new with v0.15
                                    SetVariable ("KoGa3ModMenuButtonPressed", True),
                                    Show("KoGa3ScreenCheat") ] 

                            if KoGa3ModMenuButtonPressed == True:
                                textbutton _("↓{k=-1.2}Mod{/k}"):
                                    text_style persistent.KoGa3_QuickMenu1_button_font
                                    text_size persistent.KoGa3QuickMenuTextSize
                                    text_outlines [ (absolute(persistent.KoGa3TextOutline4), "#000", absolute(persistent.KoGa3TextOutline5), absolute(persistent.KoGa3TextOutline6)) ]
                                    selected False 
                                    action [
                                    SetVariable ("KoGa3ModMenuButtonPressed", False),
                                    Hide("KoGa3ScreenCheat"), 
                                    Hide("KoGa3ScreenModMenu"), 
                                    Hide("KoGa3ScreenCheatMore1"), 
                                    Hide("KoGa3ScreenJukebox"), 
                                    Hide("KoGa3QuickMusicMenu"), 
                                    Hide("KoGa3ScreenBlank"), 
                                    Hide("KoGa3ScreenAudioMenu"), 
                                    Hide("KoGa3GameSettingsQuickMenu"), 
                                    Hide("KoGa3GameSettings") ] 

                    if _in_replay:
                        textbutton _("■ {k=-1.2}Replay{/k}"):
                            text_style persistent.KoGa3_QuickMenu1_button_font
                            text_size persistent.KoGa3QuickMenuTextSize
                            text_outlines [ (absolute(persistent.KoGa3TextOutline4), "#000", absolute(persistent.KoGa3TextOutline5), absolute(persistent.KoGa3TextOutline6)) ]
                            action EndReplay(confirm=True)
            else:
                hbox:
                    style_prefix "quick"
                    $ persistent.KoGa3_QuickMenu1_button_font = "KoGa3_QuickMenu1_button_text"
                    $ persistent.KoGa3_QuickMenu2_button_font = "KoGa3_QuickMenu2_button_text"
                    xalign 0.5
                    yalign 1.0
                    spacing 14
                    if persistent.KoGa3QuickMenuItemBack:
                        textbutton _("Back"):
                            text_style persistent.KoGa3_QuickMenu1_button_font
                            text_size persistent.KoGa3QuickMenuTextSize
                            text_outlines [ (absolute(persistent.KoGa3TextOutline4), "#000", absolute(persistent.KoGa3TextOutline5), absolute(persistent.KoGa3TextOutline6)) ]
                            action Rollback()
                    if persistent.KoGa3QuickMenuItemHist:
                        textbutton _("Hist"):
                            text_style persistent.KoGa3_QuickMenu1_button_font
                            text_size persistent.KoGa3QuickMenuTextSize
                            text_outlines [ (absolute(persistent.KoGa3TextOutline4), "#000", absolute(persistent.KoGa3TextOutline5), absolute(persistent.KoGa3TextOutline6)) ]
                            action ShowMenu('history')
                    if persistent.KoGa3QuickMenuItemHide:
                        textbutton _("Hide"):
                            text_style persistent.KoGa3_QuickMenu1_button_font
                            text_size persistent.KoGa3QuickMenuTextSize
                            text_outlines [ (absolute(persistent.KoGa3TextOutline4), "#000", absolute(persistent.KoGa3TextOutline5), absolute(persistent.KoGa3TextOutline6)) ]
                            action HideInterface()
                    if persistent.KoGa3QuickMenuItemSkip:
                        textbutton _("Skip"):
                            text_style persistent.KoGa3_QuickMenu1_button_font
                            text_size persistent.KoGa3QuickMenuTextSize
                            text_outlines [ (absolute(persistent.KoGa3TextOutline4), "#000", absolute(persistent.KoGa3TextOutline5), absolute(persistent.KoGa3TextOutline6)) ]
                            action Skip() alternate Skip(fast=True, confirm=True)
                    if persistent.KoGa3QuickMenuItemAuto:
                        textbutton _("Auto"):
                            text_style persistent.KoGa3_QuickMenu1_button_font
                            text_size persistent.KoGa3QuickMenuTextSize
                            text_outlines [ (absolute(persistent.KoGa3TextOutline4), "#000", absolute(persistent.KoGa3TextOutline5), absolute(persistent.KoGa3TextOutline6)) ]
                            action Preference("auto-forward", "toggle")
                    if persistent.KoGa3QuickMenuItemSave:
                        textbutton _("Save"): 
                            text_style persistent.KoGa3_QuickMenu1_button_font
                            text_size persistent.KoGa3QuickMenuTextSize
                            text_outlines [ (absolute(persistent.KoGa3TextOutline4), "#000", absolute(persistent.KoGa3TextOutline5), absolute(persistent.KoGa3TextOutline6)) ]
                            action ShowMenu('save')
                    if persistent.KoGa3QuickMenuItemLoad:
                        textbutton _("Load"): 
                            text_style persistent.KoGa3_QuickMenu1_button_font
                            text_size persistent.KoGa3QuickMenuTextSize
                            text_outlines [ (absolute(persistent.KoGa3TextOutline4), "#000", absolute(persistent.KoGa3TextOutline5), absolute(persistent.KoGa3TextOutline6)) ]
                            action ShowMenu('load')
                    if persistent.KoGa3QuickMenuItemQSave:
                        textbutton _("Q.Save"):
                            text_style persistent.KoGa3_QuickMenu1_button_font
                            text_size persistent.KoGa3QuickMenuTextSize
                            text_outlines [ (absolute(persistent.KoGa3TextOutline4), "#000", absolute(persistent.KoGa3TextOutline5), absolute(persistent.KoGa3TextOutline6)) ]
                            action QuickSave()
                    if persistent.KoGa3QuickMenuItemQLoad:
                        textbutton _("Q.Load"):
                            text_style persistent.KoGa3_QuickMenu1_button_font
                            text_size persistent.KoGa3QuickMenuTextSize
                            text_outlines [ (absolute(persistent.KoGa3TextOutline4), "#000", absolute(persistent.KoGa3TextOutline5), absolute(persistent.KoGa3TextOutline6)) ]
                            action QuickLoad()
                    if persistent.KoGa3QuickMenuItemPrefs:
                        textbutton _("Prefs"):
                            text_style persistent.KoGa3_QuickMenu1_button_font
                            text_size persistent.KoGa3QuickMenuTextSize
                            text_outlines [ (absolute(persistent.KoGa3TextOutline4), "#000", absolute(persistent.KoGa3TextOutline5), absolute(persistent.KoGa3TextOutline6)) ]
                            action ShowMenu('preferences')
                    if persistent.KoGa3QuickMenuItemModmenu:
                        hbox:
                            spacing 10
                            if KoGa3ModMenuButtonPressed == False:
                                textbutton _("Mod menu"):
                                    text_style persistent.KoGa3_QuickMenu1_button_font
                                    text_size persistent.KoGa3QuickMenuTextSize
                                    text_outlines [ (absolute(persistent.KoGa3TextOutline4), "#000", absolute(persistent.KoGa3TextOutline5), absolute(persistent.KoGa3TextOutline6)) ]
                                    selected False 
                                    action [ 
                                    SetVariable ("Alexis_PointsTemp", Alexis_Points),
                                    SetVariable ("Emily_PointsTemp", Emily_Points),
                                    SetVariable ("Melissa_PointsTemp", Melissa_Points),
                                    SetVariable ("Erynn_PointsTemp", Erynn_Points),
                                    SetVariable ("Layla_PointsTemp", Layla_Points),
                                    SetVariable ("Elena_PointsTemp", Elena_Points),
                                    SetVariable ("Nikki_PointsTemp", Nikki_Points),
                                    SetVariable ("Cara_PointsTemp", Cara_Points),
                                    SetVariable ("Tori_PointsTemp", Tori_Points),
                                    SetVariable ("Adriana_PointsTemp", Adriana_Points),
                                    SetVariable ("Naomi_PointsTemp", Naomi_Points),
                                    SetVariable ("Nikki_Weekend_PointsTemp", Nikki_Weekend_Points),
                                    SetVariable ("Cara_Weekend_PointsTemp", Cara_Weekend_Points),
                                    SetVariable ("Gabi_PointsTemp", Gabi_Points),               #not used
                                    SetVariable ("Natasha_PointsTemp", Natasha_Points),         #not used
                                    SetVariable ("Lakeyn_PointsTemp", Lakeyn_Points),
                                    SetVariable ("Valeria_PointsTemp", Valeria_Points),
                                    SetVariable ("Sienna_PointsTemp", Sienna_Points),
                                    SetVariable ("Brooke_PointsTemp", Brooke_Points),
                                    SetVariable ("Iris_PointsTemp", Iris_Points),
                                    SetVariable ("Zach_PointsTemp", Zach_Points),
                                    SetVariable ("Nikki_Visit_PointsTemp", Nikki_Visit_Points),
                                    SetVariable ("Cara_Visit_PointsTemp", Cara_Visit_Points),
                                    SetVariable ("Alexis_JealousyPointsTemp", Alexis_JealousyPoints),
                                    SetVariable ("Mira_PointsTemp", Mira_Points),               #not used
                                    SetVariable ("Alexis_SPTemp", Alexis_SP),                   #added with v0.13
                                    SetVariable ("Nikki_SPointsTemp", Nikki_SPoints),           #new with v0.13
                                    SetVariable ("MC_GoodStudentTemp", MC_GoodStudent),         #new with v0.10.5
                                    SetVariable ("Alexis_BeachPointsTemp", Alexis_BeachPoints), #new with v0.11
                                    SetVariable ("Gabi_SuspicionTemp", Gabi_Suspicion),         #new with v0.14
                                    SetVariable ("Gabi_JealousyTemp", Gabi_Jealousy),           #new with v0.14
                                    SetVariable ("Andres_PointsTemp", Andres_Points),           #new with v0.14
                                    SetVariable ("Darryl_PointsTemp", Darryl_Points),           #new with v0.15
                                    SetVariable ("Marisol_PointsTemp", Marisol_Points),         #new with v0.15
                                    SetVariable ("Ximena_PointsTemp", Ximena_Points),           #new with v0.15
                                    SetVariable ("KoGa3ModMenuButtonPressed", True),
                                    Show("KoGa3ScreenCheat") ] 

                            if KoGa3ModMenuButtonPressed == True:
                                textbutton _("Close Mod menu"):
                                    text_style persistent.KoGa3_QuickMenu1_button_font
                                    text_size persistent.KoGa3QuickMenuTextSize
                                    text_outlines [ (absolute(persistent.KoGa3TextOutline4), "#000", absolute(persistent.KoGa3TextOutline5), absolute(persistent.KoGa3TextOutline6)) ]
                                    selected False 
                                    action [
                                    SetVariable ("KoGa3ModMenuButtonPressed", False),
                                    Hide("KoGa3ScreenCheat"), 
                                    Hide("KoGa3ScreenModMenu"), 
                                    Hide("KoGa3ScreenCheatMore1"), 
                                    Hide("KoGa3ScreenJukebox"), 
                                    Hide("KoGa3QuickMusicMenu"), 
                                    Hide("KoGa3ScreenBlank"), 
                                    Hide("KoGa3ScreenAudioMenu"), 
                                    Hide("KoGa3GameSettingsQuickMenu"), 
                                    Hide("KoGa3GameSettings") ] 

                    if _in_replay:
                        textbutton _("End Replay"):
                            text_style persistent.KoGa3_QuickMenu1_button_font
                            text_size persistent.KoGa3QuickMenuTextSize
                            text_outlines [ (absolute(persistent.KoGa3TextOutline4), "#000", absolute(persistent.KoGa3TextOutline5), absolute(persistent.KoGa3TextOutline6)) ]
                            action EndReplay(confirm=True)

                if _in_replay:
                    textbutton _("End Replay"):
                        text_style persistent.KoGa3_QuickMenu1_button_font
                        text_size persistent.KoGa3QuickMenuTextSize
                        text_outlines [ (absolute(persistent.KoGa3TextOutline4), "#000", absolute(persistent.KoGa3TextOutline5), absolute(persistent.KoGa3TextOutline6)) ]
                        action EndReplay(confirm=True)



#---------------------Preferences adds---------------------#
# screen preferences():

    # tag menu

    # use game_menu(_("Preferences"), scroll="viewport"):

        # vbox:

            # hbox:
                # box_wrap True

                # if renpy.variant("pc"):

                    # vbox:
                        # style_prefix "radio"
                        # label _("Display")
                        # textbutton _("Window") action Preference("display", "window")
                        # textbutton _("Fullscreen") action Preference("display", "fullscreen")

                # vbox:
                    # style_prefix "radio"
                    # label _("Rollback Side")
                    # textbutton _("Disable") action Preference("rollback side", "disable")
                    # textbutton _("Left") action Preference("rollback side", "left")
                    # textbutton _("Right") action Preference("rollback side", "right")

                # vbox:
                    # style_prefix "check"
                    # label _("Skip")
                    # textbutton _("Unseen Text") action Preference("skip", "toggle")
                    # textbutton _("After Choices") action Preference("after choices", "toggle")
                    # textbutton _("Transitions") action InvertSelected(Preference("transitions", "toggle"))

                # ## Additional vboxes of type "radio_pref" or "check_pref" can be
                # ## added here, to add additional creator-defined preferences.

            # null height (4 * gui.pref_spacing)

            # hbox:
                # style_prefix "slider"
                # box_wrap True

                # vbox:

                    # # label _("Textbox Opacity")
                    # # bar:
                        # # value FieldValue(persistent, "text_box_opacity", range=1.0)
                        # # style "slider"
                        # # xsize 530

                    # label _("Text Speed")

                    # bar value Preference("text speed")

                    # label _("Auto-Forward Time")

                    # bar value Preference("auto-forward time")

                    # #=====================================KoGa3 additions====================================#
                    # null height (2 * gui.pref_spacing)
                    # label _("Mod KoGa3")
                    # textbutton _("Settings..."):
                        # sensitive True
                        # action [
                        # Show("KoGa3ScreenBlank"),
                        # Show("KoGa3GameSettings") ]
                    # #=====================================KoGa3 additions====================================#

                # vbox:

                    # if config.has_music:
                        # label _("Music Volume")

                        # hbox:
                            # bar value Preference("music volume")

                    # if config.has_sound:

                        # label _("Sound Volume")

                        # hbox:
                            # bar value Preference("sound volume")

                            # if config.sample_sound:
                                # textbutton _("Test") action Play("sound", config.sample_sound)

                    # ######################## Music addon ########################
                    # if renpy.has_label('KoGa3MusicCheck'):
                        # if config.has_voice:
                            # label _("Mod music Volume")

                            # hbox:
                                # bar value Preference("voice volume")

                                # if config.sample_voice:
                                    # textbutton _("Test") action Play("voice", config.sample_voice)

                    # if config.has_music or config.has_sound or config.has_voice:
                        # null height gui.pref_spacing

                        # textbutton _("Mute All"):
                            # action Preference("all mute", "toggle")
                            # style "mute_all_button"

init 999:
    screen px_pref_reading():
        vbox:
            spacing 36

            use px_tab_header(_("Reading"))

            use px_field(_("TEXT SPEED")):
                bar value Preference("text speed") xsize 940

            use px_field(_("AUTO-FORWARD TIME")):
                bar value Preference("auto-forward time") xsize 940

            # use px_field(_("TEXTBOX OPACITY")):
                # bar:
                    # value FieldValue(persistent, "text_box_opacity", range=1.0)
                    # style "slider"
                    # xsize 940

            use px_field(_("SKIP")):
                hbox:
                    style_prefix "px_check"
                    spacing 32
                    textbutton _("Skip unseen text") action Preference("skip", "toggle")
                    textbutton _("Skip after choices") action Preference("after choices", "toggle")
                    textbutton _("Play transitions while skipping"):
                        action InvertSelected(Preference("transitions", "toggle"))

            use px_field(_("SKIP SPEED")):
                hbox:
                    style_prefix "px_pill"
                    spacing 8
                    textbutton _("Normal"):
                        action Function(px_set_skip_speed, "normal")
                        selected persistent.skip_speed == "normal"
                    textbutton _("Fast"):
                        action Function(px_set_skip_speed, "fast")
                        selected persistent.skip_speed == "fast"
                    textbutton _("Instant"):
                        action Function(px_set_skip_speed, "instant")
                        selected persistent.skip_speed == "instant"
                text _("Speed of the hold-Ctrl skip loop. \"Instant\" runs at the engine's render-rate cap (~60 lines/sec). Press {b}>{/b} during play to race to the next choice."):
                    style "px_hint"

            #=====================================KoGa3 additions====================================#
            use px_field(_("Mod KoGa3")):
                hbox:
                    style_prefix "px_pill"
                    spacing 8
                    textbutton _("Settings..."):
                        sensitive True
                        action [
                        Show("KoGa3ScreenBlank"),
                        Show("KoGa3GameSettings") ]
            #=====================================KoGa3 additions====================================#
