
# === Characters ===

init python:
    def char(name, color="#FFFFFF", **kwargs):
        kwargs.setdefault("who_outlines", [(3, "#000000")])
        kwargs.setdefault("what_outlines", [(2, "#000000")])
        return Character(name, color=color, **kwargs)

define mc = char("name", "#009de0", dynamic=True)
define a = char(_("Alexis"), "#fe1f3e")
define m =  char(_("Emily"), "#e265e3")
define er = char(_("Erynn"), "#ce0278")
define me = char(_("Melissa"), "#47f747")
define la = char(_("Layla"), "#18fcff")
define el = char(_("Elena"), "#fee315")
define ni = char(_("Nikki"), "#631485")
define c =  char(_("Cara"), "#ae22b4")
define va = char(_("Valeria"), "#fc4f11")
define ir = char(_("Iris"), "#42cb86")
define sa = char(_("Santiago"), "#5099c3")
define sn = char(_("Mr Navarro"), "#5099c3")
define jo = char(_("John"), "#5099c3")
define to = char(_("Tori"), "#6769c0")
define da = char(_("Darryl"), "#5099c3")
define et = char(_("Ethan"), "#5099c3")
define tr = char(_("Gabriela (Ms Ramirez)"), "#ffb954")

# === Side Characters ===
define d =  char(_("Andres"), "#5099c3")
define ln = char(_("Lakeyn"), "#4272cb")
define br = char(_("Brooke"), "#fb6161")
define am = char(_("Adriana"), "#3c6480")
define mr = char(_("Mira"), "#a6f6cd")
define ha = char(_("Haley"), "#5099c3")
define z =  char(_("Zach"), "#5099c3")
define na = char(_("Nathan"), "#5099c3")
define sc = char(_("Sha'Carri"), "#5099c3")
define tj = char(_("TJ"), "#5099c3")
define si = char(_("Sienna"), "#5099c3")
define dr = char(_("Daniela"), "#5099c3")
define pe = char(_("Peyton"), "#5099c3")
define jz = char(_("Jasmine"), "#5099c3")
define zo = char(_("Enzo"), "#5099c3")
define xv = char(_("Ximena (Ms Vergara)"), "#9242ff")
define so = char(_("Marisol"), "#9242ff")
define tm = char(_("Coach (Mike)"), "#5099c3")
define do = char(_("Mr Donovan"), "#5099c3")
define bd = char(_("Dylan"), "#5099c3")
define gi = char(_("Gianna"), "#5099c3")
define ma = char(_("Mateo"), "#5099c3")
define di = char(_("Diego"), "#5099c3")
define av = char(_("Ava"), "#5099c3")
define ra = char(_("Rachel"), "#5099c3")
define ju = char(_("Julia"), "#5099c3")
define ih = char(_("Isaiah"), "#5099c3")
define zn = char(_("Zane"), "#5099c3")

# === Background Characters ===
define nt = char(_("Natasha"))
define ar = char(_("Amare"))
define mk = char(_("MacKenzie"))
define le = char(_("Leah"))
define tc = char(_("Mr Coleman"))
define td = char(_("Naomi (Ms Davis)"))
define bt = char(_("Bartender"))
define ba = char(_("Barrista"))
define em = char(_("Emanuel"))
define mg = char(_("Miguel"))
define ca = char(_("Callum"))
define th = char(_("Theo"))
define cl = char(_("Colin"))
define ai = char(_("Aiden"))
define t =  char(_("Teacher"))
define pt = char(_("Personal Trainer"))
define x =  char("???")
define n =  char("")
define pi = char(_("Pilot"))
define fa = char(_("Flight Attendant"))
define re = char(_("Receptionist"))
define pa = char(_("Parent"))
define rs = char(_("Rose"))
define mi = char(_("Michelle"))
define ky = char(_("Kaylin")) #Messe
define ja = char(_("Jaylen"))
define ro = char(_("Rob"))
define jl = char(_("Julian"))
define no = char(_("Noah"))
define se = char(_("Sebastian"))
define mo = char(_("Monique"))
define je = char(_("Jenna"))
define gb = char(_("Gil Burke"))
define wa = char(_("Walter"))
define sq = char(_("Shaq"))
define ka = char(_("Kaley"))
define hn = char(_("Hannah"))
define ow = char(_("Owen"))
define ml = char(_("Miles"))
define ys = char(_("Yellow Snow"))
define cr = char(_("Crowd"))
define yi = char(_("Singer"))
define yd = char(_("Drummer"))
define yb = char(_("Bassist"))
define yg = char(_("Guitarist"))
define an = char(_("Announcer"))
define ph = char(_("Photographer"))
define pz = char(_("Paparazzi"))
define nu = char(_("Nurse"))
define dt = char(_("Doctor"))
define dp = char(_("Dispatcher"))
define ge = char(_("Gym employee"))
define st = char(_("Student(s)"))
define aa = char(_("Together"))
define ab = char(_("Nikki, [mc]"))
define ac = char(_("Everyone"))
define gu = char(_("Guest"))
define gr = char(_("Girl"))
define gy = char(_("Guy"))
define dg = char(_("Dog"))
define co = char(_("Commentator"))

# === The game starts here ===

label start:
    stop music fadeout 1.0
    scene black
    call screen warning_screen
    scene black with Dissolve(1)

label getPlayerName:
    $ name = renpy.call_screen("player_name_screen")
    $ persistent.player_name = name
    jump Intro

label Intro:
    # === Character Points ===
    $ Alexis_Points = 0
    $ Emily_Points = 0
    $ Melissa_Points = 0
    $ Erynn_Points = 0
    $ Layla_Points = 0
    $ Elena_Points = 0
    $ Nikki_Points = 0
    $ Cara_Points = 0
    $ Tori_Points = 0
    $ Adriana_Points = 0
    $ Gabi_Points = 0
    $ Naomi_Points = 0
    $ Natasha_Points = 0
    $ Lakeyn_Points = 0
    $ Valeria_Points = 0
    $ Sienna_Points = 0
    $ Brooke_Points = 0
    $ Zach_Points = 0
    $ Darryl_Points = 0
    $ Iris_Points = 0
    $ Mira_Points = 0
    $ ShaCarri_Points = 0
    $ Andres_Points = 0
    $ Ximena_Points = 0
    $ Marisol_Points = 0
    $ Alexis_SP = 0
    $ Nikki_SPoints = 0

    # === Event Points ===
    $ MC_GoodStudent = 0
    $ Nikki_Weekend_Points = 0
    $ Nikki_Visit_Points = 0
    $ Cara_Weekend_Points = 0
    $ Cara_Visit_Points = 0
    $ Alexis_JealousyPoints = 0
    $ Alexis_BeachPoints = 0
    $ Ethan_Punch = 0
    $ Ethan_WallPunch = 0
    $ Gabi_Suspicion = 0
    $ Gabi_Jealousy = 0

    # === Sex Counters ===
    $ MC_SexCounter = 0
    $ SexCounter_Alexis = 0
    $ SexCounter_Erynn = 0
    $ SexCounter_Layla = 0
    $ SexCounter_Elena = 0
    $ SexCounter_Nikki = 0
    $ SexCounter_Cara = 0
    $ SexCounter_Iris = 0
    $ SexCounter_Gabi = 0
    $ SexCounter_Valeria = 0
    $ SexCounter_Tori = 0
    $ SexCounter_Melissa = 0
    $ SexCounter_Mira = 0
    $ SexCounter_Lakeyn = 0
    $ SexCounter_Sienna = 0
    $ SexCounter_Rachel = 0
    $ SexCounter_Brooke = 0
    $ SexCounter_ShaCarri = 0
    $ SexCounter_Jasmine = 0
    $ SexCounter_Julia = 0
    $ SexCounter_Gianna = 0
    $ SexCounter_Adriana = 0
    $ SexCounter_Ximena = 0
    $ SexCounter_Marisol = 0
    $ SexCounter_Ava = 0
    $ SexCounter_Emily = 0

    jump Episode_1_Start
