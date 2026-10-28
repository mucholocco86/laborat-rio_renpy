init python:
    if persistent.foundHGal is None:
        persistent.foundHGal = []
    if persistent.alphadialogue is None:
        persistent.alphadialogue = 0.82

    def qAnimation(a, pause, number, repeat=False, reverse=False, startNr=1, bck=False):

        newAnim = [f for g in [ [a.format(k), pause] for k in range(startNr, number) ] for f in g] + [a.format(number)]

        if bck:
            newAnim2 = [f for g in [ [a.format(k), pause] for k in range(startNr, number) ] for f in g] + [a.format(number)]
            newAnim2.reverse()
            newAnim2.pop(0)
            newAnim.extend(newAnim2)

        if reverse:
            newAnim.reverse()
        if repeat:
            newAnim.extend([pause])

        return renpy.display.anim.Animation(*newAnim)

    class Relationships():
        def __init__(self, S="S__", Si="S_____", D="D_______", Ni="N____", M="M__", Mo="M_____", A="A___", Au="A_____", B="B__", Br="B______", So="S__", Ne="N_____"):
            self.S = S
            self.Si = Si
            self.D = D
            self.Ni = Ni
            self.M = M
            self.Mo = Mo
            self.A = A
            self.Au = Au
            self.B = B
            self.Br = Br
            self.So = So
            self.Ne = Ne

        def __setattr__(self, name, value):
            if isinstance(value, unicode):
                self.__dict__[name] = value.lower().capitalize()
            else:
                self.__dict__[name] = value

        def __getattr__(self, name):
            for i in [("D", "D_______"), ("Ni", "N____"), ("So", "S__"), ("Ne", "N_____"), ("S", "S__"), ("Si", "S_____"), ("B", "B__"), ("Br", "B______"), ("A", "A___"), ("Au", "A_____"), ("M", "M__"), ("Mo", "M_____")]:
                if i[0] not in self.__dict__:
                    self.__dict__[i[0]] = i[1]
            if name not in self.__dict__:
                if name.capitalize() in self.__dict__:
                    return self.__dict__[name.capitalize()].lower()
                elif name[-2] + name[-1] == "UP" and len(name) == 3:
                    return self.__dict__[name[0]].upper()
                elif name[-2] + name[-1] == "UP" and len(name) == 4:
                    return self.__dict__[name[0] + name[1]].upper()
                elif len(name) in [2, 3]:
                    return getWord(name[0]) + self.addRel(name)
                return self.__getattribute__(name)
            return self.__dict__[name]

        def addRel(self, name):
            if len(name) == 2:
                return self.__dict__[name[1].capitalize()].lower()
            return self.__dict__[name[1].capitalize() + name[2]].lower()

    def csMusic(name):
        if renpy.music.get_playing() != "audio/" + name:
            renpy.music.play("audio/" + name, loop=True, fadein=2)

    def getWord(letter):
        word = ""
        if letter in "Yy":
            word = "your "
        elif letter in "Mm":
            word = "my "
        elif letter in "Oo":
            word = "our "
        elif letter in "Ii":
            word = "his "
        elif letter in "Ee":
            word = "her "
        if letter in "YMOIE":
            return word.capitalize()
        return word

    class relInput(InputValue):
        def __init__(self, name):
            self.name = name

            self.default = False

        def get_text(self):
            return rel.__dict__[self.name]

        def set_text(self, s):
            setattr(rel, self.name, s)

        def enter(self):
            renpy.run(self.Disable())
            raise renpy.IgnoreEvent()

        def changed(self, s):
            print s

    class nameAlex(InputValue):
        global MCName

        def __init__(self, name):
            self.name = name

            self.default = False

        def get_text(self):
            return globals()["MCName"]

        def set_text(self, s):
            globals()["MCName"] = s

        def enter(self):
            renpy.run(self.Disable())
            raise renpy.IgnoreEvent()

        def changed(self, s):
            print s

    class repGallery():
        def __init__ (self, name, image, check, label, hid=[]):
            self.name = name
            self.image = image
            self.check = check
            self.label = label
            self.hid = hid

    class hidGallery():
        def __init__ (self, name, button, image, tags=""):
            self.name = name
            self.button = button
            self.image = image
            self.tags = tags

        def anim(self):
            if self.tags == "Animation":
                return self.image.replace(".webp", "").replace(".png", "")
            else:
                return "images/HG/" + self.image

    def findHG(name, attr):
        for i in hGal:
            if i.name == name:
                return getattr(i, attr)

    def UnlockHG():
        for i in hGal:
            if i.name not in persistent.foundHGal:
                persistent.foundHGal.append(i.name)

define gal = [
repGallery(_("Act 1"), "Scene004.webp", "scene036", "V1Act1"),
repGallery(_("Act 2"), "Scene038.webp", "scene086", "V1Act2", [_("Act 2")]),
repGallery(_("Act 3"), "Scene088.webp", "scene128", "V1Act3", [_("Act 3")]),
repGallery(_("Act 4"), "Scene172.webp", "scene174", "V1Act4"),
repGallery(_("Act 5"), "Scene180.webp", "scene209", "V1Act5"),
repGallery(_("Act 6"), "Scene221.webp", "scene236", "V1Act6", [_("Act 6")]),
repGallery(_("Act 7"), "Scene253.webp", "scene266", "V1Act7"),
repGallery(_("Act 8"), "Scene269.webp", "scene292", "V1Act8", [_("Act 8")]),
repGallery(_("Act 9"), "Scene309.webp", "scene323", "V1Act9", [_("Act 9")]),
repGallery(_("Act 10"), "Scene332.webp", "scene341", "V1Act10"),
repGallery(_("Act 11"), "Scene353.webp", "scene353", "V2Act11", [_("Act 11")]),
repGallery(_("Act 12"), "Scene382.webp", "scene382", "V2Act12"),
repGallery(_("Act 13"), "Scene420.webp", "scene420", "V2Act13"),
repGallery(_("Act 14"), "Scene450.webp", "scene482", "V2Act14", [_("Act 14")]),
repGallery(_("Act 15"), "Scene484.webp", "scene544", "V3Act15", [_("Act 15")]),
repGallery(_("Act 16"), "Scene545.webp", "scene685", "V3Act16"),
repGallery(_("Act 17"), "Scene687.webp", "scene741", "V3Act17", [_("Act 17")]),
repGallery(_("Act 18"), "Scene578.webp", "scene647", "V3Act18"),
repGallery(_("Act 19"), "Scene743.webp", "scene798", "V4Act19", [_("Act 19")]),
repGallery(_("Act 20"), "Scene809.webp", "scene855", "V4Act20", [_("Act 20")]),
repGallery(_("Act 21"), "Scene873.webp", "scene917", "V4Act21"),
repGallery(_("Act 22"), "Scene922.webp", "scene974", "V4Act22"),
repGallery(_("Act 23"), "Scene992.webp", "scene1026", "V4Act23", [_("Act 23")]),
repGallery(_("Act 24"), "Scene1040.webp", "scene1080", "V4Act24"),
repGallery(_("Act 25"), "Scene1088.webp", "scene1135", "V5Act25"),
repGallery(_("Act 26"), "Scene1171.webp", "scene1197", "V5Act26"),
repGallery(_("Act 27"), "Scene1244.webp", "scene1259", "V5Act27", [_("Act 27")]),
repGallery(_("Act 28"), "Scene1303.webp", "scene1304", "V5Act28", [_("Act 28")]),
repGallery(_("Act 29"), "Scene1331.webp", "scene1357", "V6Act29"),
repGallery(_("Act 30"), "Scene1398.webp", "scene1420", "V6Act30"),
repGallery(_("Act 31"), "Scene1461.webp", "scene1474", "V6Act31", [_("Act 31"), _("Act 31.2")]),
repGallery(_("Act 32"), "Scene1516.webp", "scene1529", "V6Act32"),
repGallery(_("Act 33"), "Scene1550.webp", "scene1584", "V7Act33", [_("Act 33")]),
repGallery(_("Act 34"), "Scene1595.webp", "scene1656", "V7Act34"),
repGallery(_("Act 35"), "Scene1688.webp", "scene1699", "V7Act35", [_("Act 35")]),
repGallery(_("Act 36"), "Scene1718.webp", "scene1743", "V7Act36"),
repGallery(_("Act 37"), "Scene1747.webp", "scene1778", "V8Act37"),
repGallery(_("Act 38"), "Scene1784.webp", "scene1778", "V8Act38"),
repGallery(_("Act 39"), "Scene1839.webp", "scene1853", "V8Act39"),
repGallery(_("Act 40"), "Scene1854.webp", "scene1893", "V8Act40", [_("Act 40"), _("Act 40.2")]),
repGallery(_("Act 41"), "Scene1894.webp", "scene1895", "V8Act41"),
repGallery(_("Act 42"), "Scene1922B.webp", "scene1906", "V9Act42"),
repGallery(_("Act 43"), "Scene1934.webp", "scene1954", "V9Act43", [_("Act 43")]),
repGallery(_("Act 44"), "Scene1966.webp", "scene2009", "V9Act44", [_("Act 44")]),
repGallery(_("Act 45"), "Scene2034.webp", "scene2044", "V9Act45"),
repGallery(_("Act 46"), "Scene2051.webp", "scene2092", "V10Act46"),
repGallery(_("Act 47"), "Scene2129.webp", "scene2153", "V10Act47"),
repGallery(_("Act 48"), "Scene2162.webp", "scene2199", "V10Act48", [_("Act 48")]),
repGallery(_("Act 49"), "Scene2243.webp", "scene2253", "V10Act49", [_("Act 49")]),
repGallery(_("Act 50"), "Scene2265.webp", "scene2314", "V11Act50"),
repGallery(_("Act 51"), "Scene2365.webp", "scene2367", "V11Act51", [_("Act 51")]),
repGallery(_("Act 52"), "Scene2365.webp", "scene2416", "V11Act52"),
repGallery(_("Act 53"), "Scene2435.webp", "scene2459", "V11Act53", [_("Act 53")]),
repGallery(_("Act 54"), "Scene2494.webp", "scene2512", "V12Act54"),
repGallery(_("Act 55"), "Scene2530.webp", "scene2579", "V12Act55"),
repGallery(_("Act 56"), "Scene2600.webp", "scene2619", "V12Act56", [_("Act 56"), _("Act 56.2")]),
repGallery(_("Act 57"), "Scene2644.webp", "scene2647", "V12Act57"),
repGallery(_("Act 58"), "Scene2664.webp", "scene2702", "V13Act58"),
repGallery(_("Act 59"), "Scene2705.webp", "scene2762", "V13Act59", [_("Act 59")]),
repGallery(_("Act 60"), "Scene2768.webp", "scene2812", "V13Act60", [_("Act 60")]),
repGallery(_("Act 61"), "Scene2844.webp", "scene2861", "V14Act61"),
repGallery(_("Act 62"), "Scene2883.webp", "scene2927", "V14Act62", [_("Act 62")]),
repGallery(_("Act 63"), "Scene2952.webp", "scene2980", "V14Act63"),
repGallery(_("Act 64"), "Scene3018.webp", "scene3026", "V14Act64"),
repGallery(_("Act 65"), "Scene3068.webp", "scene3073", "V14Act65", [_("Act 65")]),
repGallery(_("Act 66"), "Scene3081.webp", "scene3142", "V15Act66"),
repGallery(_("Act 67"), "Scene3143.webp", "scene3198", "V15Act67", [_("Act 67")]),
repGallery(_("Act 68"), "Scene3208.webp", "scene3248", "V15Act68"),
repGallery(_("Act 69"), "Scene3249.webp", "scene3287", "V15Act69", [_("Act 69")]),
repGallery(_("Act 70"), "Scene3289.webp", "scene3333", "V16Act70"),
repGallery(_("Act 71"), "Scene3359.webp", "scene3390", "V16Act71", [_("Act 71")]),
repGallery(_("Act 72"), "Scene3397.webp", "scene3447", "V16Act72"),
repGallery(_("Act 73"), "Scene3465.webp", "scene3488", "V16Act73", [_("Act 73")]),
repGallery(_("Act 74"), "Scene3500.webp", "scene3518", "V17Act74"),
repGallery(_("Act 75"), "Scene3563.webp", "scene3582", "V17Act75", [_("Act 75")]),
repGallery(_("Act 76"), "Scene3637.webp", "scene3642", "V17Act76", [_("Act 76")]),
repGallery(_("Act 77"), "Scene3643.webp", "scene3661", "V17Act77"),
repGallery(_("Act 78"), "Scene3698.webp", "scene3746", "V18Act78", [_("Act 78")]),
repGallery(_("Act 79"), "Scene3785.webp", "scene3805", "V18Act79"),
repGallery(_("Act 80"), "Scene3834.webp", "scene3840", "V18Act80", [_("Act 80")]),
repGallery(_("Act 81"), "Scene3864.webp", "scene3887", "V19Act81", [_("Act 81")]),
repGallery(_("Act 82"), "Scene3928.webp", "scene3928", "V19Act82"),
repGallery(_("Act 83"), "Scene3967.webp", "scene3970", "V19Act83"),
repGallery(_("Act 84"), "Scene4005.webp", "scene4017", "V19Act84", [_("Act 84")]),
repGallery(_("Act 85"), "Scene4059.webp", "scene4066", "V20Act85"),
repGallery(_("Act 86"), "Scene4120.webp", "scene4120", "V20Act86"),
repGallery(_("Act 87"), "Scene4144.webp", "scene4161", "V20Act87", [_("Act 87")]),
repGallery(_("Act 88"), "Scene4185.webp", "scene4208", "V20Act88", [_("Act 88")]),
repGallery(_("Act 89"), "Scene4232.webp", "scene4254", "V21Act89", [_("Act 89")]),
repGallery(_("Act 90"), "Scene4273.webp", "scene4297", "V21Act90"),
repGallery(_("Act 91"), "Scene4298.webp", "scene4345", "V21Act91"),
repGallery(_("Act 92"), "Scene4375.webp", "scene4394", "V21Act92", [_("Act 92")]),
repGallery(_("Act 93"), "Scene4395.webp", "scene4435", "V22Act93"),
repGallery(_("Act 94"), "Scene4436.webp", "scene4470", "V22Act94", [_("Act 94")]),
repGallery(_("Act 95"), "Scene4490.webp", "scene4514", "V22Act95"),
repGallery(_("Act 96"), "Scene4567.webp", "scene4574", "V22Act96", [_("Act 96")]),
repGallery(_("Act 97"), "Scene4612.webp", "scene4626", "V23Act97", [_("Act 97")]),
repGallery(_("Act 98"), "Scene4654.webp", "scene4666", "V23Act98"),
repGallery(_("Act 99"), "Scene4678.webp", "scene4698", "V23Act99"),
repGallery(_("Act 100"), "Scene4739.webp", "scene4751", "V23Act100", [_("Act 100")]),
repGallery(_("Act 101"), "Scene4777.webp", "scene4792", "V24Act101"),
repGallery(_("Act 102"), "Scene4821.webp", "scene4840", "V24Act102", [_("Act 102")]),
repGallery(_("Act 103"), "Scene4861.webp", "scene4884", "V24Act103"),
repGallery(_("Act 104"), "Scene4930.webp", "scene4930", "V24Act104", [_("Act 104")]),
repGallery(_("Act 105"), "Scene4937.webp", "scene4977", "V25Act105"),
repGallery(_("Act 106"), "Scene4999.webp", "scene5015", "V25Act106", [_("Act 106")]),
repGallery(_("Act 107"), "Scene5017.webp", "scene5059", "V25Act107"),
repGallery(_("Act 108"), "Scene5092.webp", "scene5110", "V25Act108", [_("Act 108")]),
repGallery(_("Act 109"), "Scene5115.webp", "scene5156", "V26Act109"),
repGallery(_("Act 110"), "Scene5172.webp", "scene5197", "V26Act110", [_("Act 110")]),
repGallery(_("Act 111"), "Scene5217.webp", "scene5236", "V26Act111"),
repGallery(_("Act 112"), "Scene5245.webp", "scene5284", "V26Act112", [_("Act 112")]),
repGallery(_("Act 113"), "Scene5323.webp", "scene5325", "V27Act113"),
repGallery(_("Act 114"), "Scene5329.webp", "scene5358", "V27Act114"),
repGallery(_("Act 115"), "Scene5405.webp", "scene5410", "V27Act115", [_("Act 115")]),
repGallery(_("Act 116"), "Scene5433.webp", "scene5460", "V27Act116", [_("Act 116")]),
repGallery(_("Act 117"), "Scene5461.webp", "scene5517", "V28Act117", [_("Act 117")]),
repGallery(_("Act 118"), "Scene5519.webp", "scene5565", "V28Act118"),
repGallery(_("Act 119"), "Scene5584.webp", "scene5603", "V28Act119"),
repGallery(_("Act 120"), "Scene5632.webp", "scene5645", "V28Act120", [_("Act 120")]),
repGallery(_("Act 121"), "Scene5646.webp", "scene5674", "V29Act121"),
repGallery(_("Act 122"), "Scene5677.webp", "scene5712", "V29Act122", [_("Act 122")]),
repGallery(_("Act 123"), "Scene5742.webp", "scene5758", "V29Act123"),
repGallery(_("Act 124"), "Scene5780.webp", "scene5822", "V29Act124", [_("Act 124")]),
repGallery(_("Act 125"), "Scene5832.webp", "scene5854", "V30Act125", [_("Act 125")]),
repGallery(_("Act 126"), "Scene5878.webp", "scene5896", "V30Act126"),
repGallery(_("Act 127"), "Scene5906.webp", "scene5937", "V30Act127"),
repGallery(_("Act 128"), "Scene5977.webp", "scene6002", "V30Act128", [_("Act 128")]),
repGallery(_("Act 129"), "Scene6015.webp", "scene6032", "V31Act129"),
repGallery(_("Act 130"), "Scene6041.webp", "scene6075", "V31Act130", [_("Act 130")]),
repGallery(_("Act 131"), "Scene6116.webp", "scene6139", "V31Act131"),
repGallery(_("Act 132"), "Scene6167.webp", "scene6181", "V31Act132", [_("Act 132")]),
repGallery(_("Act 133"), "Scene6186.webp", "scene6219", "V32Act133"),
repGallery(_("Act 134"), "Scene6234.webp", "scene6255", "V32Act134"),
repGallery(_("Act 135"), "Scene6302.webp", "scene6315", "V32Act135", [_("Act 135")]),
repGallery(_("Act 136"), "Scene6316.webp", "scene6366", "V32Act136", [_("Act 136")]),
repGallery(_("Act 137"), "Scene6391.webp", "scene6410", "V33Act137", [_("Act 137")]),
repGallery(_("Act 138"), "Scene6411.webp", "scene6450", "V33Act138"),
repGallery(_("Act 139"), "Scene6504.webp", "scene6518", "V33Act139"),
repGallery(_("Act 140"), "Scene6520.webp", "scene6548", "V33Act140", [_("Act 140")]),
repGallery(_("Act 141"), "Scene6561.webp", "scene6588", "V34Act141", [_("Act 141")]),
repGallery(_("Act 142"), "Scene6594.webp", "scene6630", "V34Act142"),
repGallery(_("Act 143"), "Scene6659.webp", "scene6690", "V34Act143", [_("Act 143")]),
repGallery(_("Act 144"), "Scene6714.webp", "scene6736", "V34Act144"),
repGallery(_("Act 145"), "Scene6750.webp", "scene6790", "V35Act145"),
repGallery(_("Act 146"), "Scene6823.webp", "scene6932", "V35Act146", [_("Act 146")]),
repGallery(_("Act 147"), "Scene6945.webp", "scene6980", "V35Act147"),
repGallery(_("Act 148"), "Scene7008.webp", "scene7014", "V35Act148", [_("Act 148")]),
repGallery(_("Act 149"), "Scene7022.webp", "scene7057", "V36Act149"),
repGallery(_("Act 150"), "Scene7097.webp", "scene7114", "V36Act150", [_("Act 150")]),
repGallery(_("Act 151"), "Scene7146.webp", "scene7168", "V36Act151", [_("Act 151")]),
repGallery(_("Act 152"), "Scene7178.webp", "scene7188", "V36Act152"),
repGallery(_("Act 153"), "Scene7221.webp", "scene7225", "V37Act153"),
repGallery(_("Act 154"), "Scene7241.webp", "scene7255", "V37Act154"),
repGallery(_("Act 155"), "Scene7266.webp", "scene7283", "V37Act155"),
repGallery(_("Act 156"), "Scene7284.webp", "scene7361", "V37Act156", [_("Act 156"), _("Act 156.2")]),
repGallery(_("Act 157"), "Scene7365.webp", "scene7395", "V38Act157"),
repGallery(_("Act 158"), "Scene7423.webp", "scene7432", "V38Act158"),
repGallery(_("Act 159"), "Scene7459.webp", "scene7485", "V38Act159", [_("Act 159")]),
repGallery(_("Act 160"), "Scene7514.webp", "scene7533", "V38Act160", [_("Act 160")]),
repGallery(_("Act 161"), "Scene7554.webp", "scene7564", "V39Act161"),
repGallery(_("Act 162"), "Scene7584.webp", "scene7602", "V39Act162", [_("Act 162")]),
repGallery(_("Act 163"), "Scene7611.webp", "scene7660", "V39Act163", [_("Act 163")]),
repGallery(_("Act 164"), "Scene7681.webp", "scene7708", "V39Act164"),
repGallery(_("Act 165"), "Scene7722.webp", "scene7748", "V40Act165"),
repGallery(_("Act 166"), "Scene7766.webp", "scene7782", "V40Act166"),
repGallery(_("Act 167"), "Scene7797.webp", "scene7832", "V40Act167", [_("Act 167")]),
repGallery(_("Act 168"), "Scene7853.webp", "scene7885", "V40Act168", [_("Act 168")]),
repGallery(_("Act 169"), "Scene7907.webp", "scene7936", "V41Act169", [_("Act 169")]),
repGallery(_("Act 170"), "Scene7977.webp", "scene7980", "V41Act170"),
repGallery(_("Act 171"), "Scene8012.webp", "scene8037", "V41Act171", [_("Act 171")]),
repGallery(_("Act 172"), "Scene8056.webp", "scene8074", "V42Act172", [_("Act 172")]),
repGallery(_("Act 173"), "Scene8075.webp", "scene8111", "V42Act173"),
repGallery(_("Act 174"), "Scene8152.webp", "scene8167", "V42Act174"),
repGallery(_("Act 175"), "Scene8200.webp", "scene8203", "V42Act175", [_("Act 175")]),
repGallery(_("Act 176"), "Scene8217.webp", "scene8254", "V43Act176"),
repGallery(_("Act 177"), "Scene8277.webp", "scene8311", "V43Act177"),
repGallery(_("Act 178"), "Scene8328.webp", "scene8341", "V43Act178", [_("Act 178")]),
repGallery(_("Act 179"), "Scene8368.webp", "scene8382", "V43Act179", [_("Act 179")]),
repGallery(_("Act 180"), "Scene8407.webp", "scene8432", "V44Act180", [_("Act 180")]),
repGallery(_("Act 181"), "Scene8443.webp", "scene8486", "V44Act181"),
repGallery(_("Act 182"), "Scene8512.webp", "scene8514", "V44Act182"),
repGallery(_("Act 183"), "Scene8525.webp", "scene8554", "V44Act183", [_("Act 183")]),
repGallery(_("Act 184"), "Scene8562.webp", "scene8594", "V45Act184"),
repGallery(_("Act 185"), "Scene8587.webp", "scene8630", "V45Act185"),
repGallery(_("Act 186"), "Scene8664.webp", "scene8689", "V45Act186", [_("Act 186")]),
repGallery(_("Act 187"), "Scene8727.webp", "scene8729", "V45Act187", [_("Act 187")]),
repGallery(_("Act 188"), "Scene8740.webp", "scene8770", "V46Act188"),
repGallery(_("Act 189"), "Scene8811.webp", "scene8811", "V46Act189", [_("Act 189")]),
repGallery(_("Act 190"), "Scene8812.webp", "scene8852", "V46Act190"),
repGallery(_("Act 191"), "Scene8853.webp", "scene8900", "V46Act191", [_("Act 191")]),
repGallery(_("Act 192"), "Scene8942.webp", "scene8948", "V47Act192"),
repGallery(_("Act 193"), "Scene8971.webp", "scene8999", "V47Act193", [_("Act 193")]),
repGallery(_("Act 194"), "Scene9043.webp", "scene9046", "V47Act194"),
repGallery(_("Act 195"), "Scene9061.webp", "scene9073", "V47Act195", [_("Act 195")]),
repGallery(_("Act 196"), "Scene9098.webp", "scene9124", "V48Act196"),
repGallery(_("Act 197"), "Scene9146.webp", "scene9175", "V48Act197", [_("Act 197")]),
repGallery(_("Act 198"), "Scene9190.webp", "scene9219", "V48Act198"),
repGallery(_("Act 199"), "Scene9238.webp", "scene9245", "V48Act199", [_("Act 199")]),
repGallery(_("Act 200"), "Scene9262.webp", "scene9282", "V49Act200", [_("Act 200")]),
repGallery(_("Act 201"), "Scene9332.webp", "scene9334", "V49Act201"),
repGallery(_("Act 202"), "Scene9365.webp", "scene9385", "V49Act202", [_("Act 202")]),
repGallery(_("Act 203"), "Scene9410.webp", "scene9415", "V49Act203"),
repGallery(_("Act 204"), "Scene9445.webp", "scene9565", "V50Act204"),
repGallery(_("Act 205"), "Scene9585.webp", "scene9595", "V50Act205", [_("Act 205")]),
repGallery(_("Act 206"), "Scene9597.webp", "scene9649", "V50Act206"),
repGallery(_("Act 207"), "Scene9661.webp", "scene9677", "V50Act207", [_("Act 207")]),
repGallery(_("Act 208"), "Scene9681.webp", "scene9716", "V51Act208", [_("Act 208")]),
repGallery(_("Act 209"), "Scene9758.webp", "scene9760", "V51Act209", [_("Act 209")]),
repGallery(_("Act 210"), "Scene9777.webp", "scene9807", "V51Act210"),
repGallery(_("Act 211"), "Scene9838.webp", "scene9859", "V51Act211"),
repGallery(_("Act 212"), "Scene9862.webp", "scene9904", "V52Act212"),
repGallery(_("Act 213"), "Scene9906.webp", "scene9949", "V52Act213"),
repGallery(_("Act 214"), "Scene9962.webp", "scene10001", "V52Act214", [_("Act 214")]),
repGallery(_("Act 215"), "Scene10034.webp", "scene10047", "V52Act215", [_("Act 215")]),
repGallery(_("Act 216"), "Scene10058.webp", "scene10080", "V53Act216", [_("Act 216")]),
repGallery(_("Act 217"), "Scene10118.webp", "scene10138", "V53Act217"),
repGallery(_("Act 218"), "Scene10152.webp", "scene10179", "V53Act218", [_("Act 218")]),
repGallery(_("Act 219"), "Scene10216.webp", "scene10216", "V53Act219"),
repGallery(_("Act 220"), "Scene10220.webp", "scene10263", "V54Act220", [_("Act 220")]),
repGallery(_("Act 221"), "Scene10283.webp", "scene10302", "V54Act221"),
repGallery(_("Act 222"), "Scene10305.webp", "scene10355", "V54Act222"),
repGallery(_("Act 223"), "Scene10380.webp", "scene10388", "V54Act223", [_("Act 223")]),
repGallery(_("Act 224"), "Scene10392.webp", "scene10419", "V55Act224"),
repGallery(_("Act 225"), "Scene10435.webp", "scene10451", "V55Act225"),
repGallery(_("Act 226"), "Scene10483.webp", "scene10520", "V55Act226", [_("Act 226")]),
repGallery(_("Act 227"), "Scene10524.webp", "scene10553", "V55Act227", [_("Act 227")]),
repGallery(_("Act 228"), "Scene10578.webp", "scene10591", "V56Act228"),
repGallery(_("Act 229"), "Scene10592.webp", "scene10642", "V56Act229", [_("Act 229")]),
repGallery(_("Act 230"), "Scene10680.webp", "scene10698", "V56Act230", [_("Act 230")]),
repGallery(_("Act 231"), "Scene10719.webp", "scene10733", "V57Act231"),
repGallery(_("Act 232"), "Scene10739.webp", "scene10769", "V57Act232", [_("Act 232")]),
repGallery(_("Act 233"), "Scene10787.webp", "scene10806", "V57Act233"),
repGallery(_("Act 234"), "Scene10865.webp", "scene10870", "V57Act234", [_("Act 234")]),
repGallery(_("Act 235"), "Scene10886.webp", "scene10913", "V58Act235", [_("Act 235")]),
repGallery(_("Act 236"), "Scene10947.webp", "scene10958", "V58Act236", [_("Act 236")]),
repGallery(_("Act 237"), "Scene10984.webp", "scene11017", "V58Act237"),
repGallery(_("Act 238"), "Scene11056.webp", "scene11062", "V59Act238"),
repGallery(_("Act 239"), "Scene11081.webp", "scene11099", "V59Act239", [_("Act 239")]),
repGallery(_("Act 240"), "Scene11143.webp", "scene11153", "V59Act240"),
repGallery(_("Act 241"), "Scene11169.webp", "scene11190", "V59Act241", [_("Act 241")]),
repGallery(_("Act 242"), "Scene11207.webp", "scene11220", "V60Act242"),
repGallery(_("Act 243"), "Scene11276.webp", "scene11276", "V60Act243"),
repGallery(_("Act 244"), "Scene11281.webp", "scene11312", "V60Act244", [_("Act 244")]),
repGallery(_("Act 245"), "Scene11338.webp", "scene11371", "V60Act245", [_("Act 245")]),
repGallery(_("Act 246"), "Scene11387.webp", "scene11413", "V61Act246", [_("Act 246")]),
repGallery(_("Act 247"), "Scene11433.webp", "scene11446", "V61Act247"),
repGallery(_("Act 248"), "Scene11478.webp", "scene11479", "V61Act248"),
repGallery(_("Act 249"), "Scene11526.webp", "scene11545", "V61Act249", [_("Act 249")]),
repGallery(_("Act 250"), "Scene11558.webp", "scene11582", "V62Act250", [_("Act 250")]),
repGallery(_("Act 251"), "Scene11584.webp", "scene11635", "V62Act251"),
repGallery(_("Act 252"), "Scene11650.webp", "scene11678", "V62Act252"),
repGallery(_("Act 253"), "Scene11679.webp", "scene11723", "V62Act253", [_("Act 253")]),
repGallery(_("Act 254"), "Scene11743.webp", "scene11748", "V63Act254"),
repGallery(_("Act 255"), "Scene11773.webp", "scene11780", "V63Act255"),
repGallery(_("Act 256"), "Scene11781.webp", "scene11829", "V63Act256", [_("Act 256")]),
repGallery(_("Act 257"), "Scene11843.webp", "scene11876", "V63Act257", [_("Act 257")]),
repGallery(_("Act 258"), "Scene11880.webp", "scene11942", "V64Act258"),
repGallery(_("Act 259"), "Scene11968.webp", "scene11983", "V64Act259", [_("Act 259")]),
repGallery(_("Act 260"), "Scene12005.webp", "scene12005", "V64Act260"),
repGallery(_("Act 261"), "Scene12028.webp", "scene12040", "V64Act261", [_("Act 261")]),
repGallery(_("Act 262"), "Scene12078.webp", "scene12118", "V65Act262", [_("Act 262"), _("Act 262.2")]),
repGallery(_("Act 263"), "Scene12125.webp", "scene12155", "V65Act263"),
repGallery(_("Act 264"), "Scene12177.webp", "scene12181", "V65Act264"),
repGallery(_("Act 265"), "Scene12184.webp", "scene12214", "V65Act265")
]
define hGal = [
hidGallery(_("Act 2"), "HGB003.png", "HG003.png"),
hidGallery(_("Act 3"), "HGB004.png", "HG004.png"),
hidGallery(_("Act 6"), "HGB005.png", "HG005.png"),
hidGallery(_("Act 8"), "HGB006.png", "HG006.png"),
hidGallery(_("Act 9"), "HGB007.png", "HG007.png"),
hidGallery(_("Act 11"), "HGB008.png", "HG008.png"),
hidGallery(_("Act 14"), "HGB010.png", "HG010.png"),
hidGallery(_("Act 15"), "HGB011.png", "HG011.png"),
hidGallery(_("Act 17"), "HGB012.png", "HG012.png", "Animation"),
hidGallery(_("Act 19"), "HGB013.png", "HG014.png"),
hidGallery(_("Act 20"), "HGB002.png", "HG002.png"),
hidGallery(_("Act 23"), "HGB014.png", "HG013.png"),
hidGallery(_("Act 27"), "HGB015.png", "HG015.png", "Animation"),
hidGallery(_("Act 28"), "HGB016.png", "HG016.png"),
hidGallery(_("Act 31"), "HGB017.png", "HG017.webp"),
hidGallery(_("Act 31.2"), "HGB018.png", "HG018.webp"),
hidGallery(_("Act 33"), "HGB019.png", "HG019.webp"),
hidGallery(_("Act 35"), "HGB020.png", "HG020.webp"),
hidGallery(_("Act 40"), "HGB021.png", "HG021.webp"),
hidGallery(_("Act 40.2"), "HGB022.png", "HG022.webp"),
hidGallery(_("Act 43"), "HGB023.png", "HG023.webp"),
hidGallery(_("Act 44"), "HGB024.png", "HG024.webp"),
hidGallery(_("Act 48"), "HGB025.png", "HG025.webp"),
hidGallery(_("Act 49"), "HGB026.png", "HG026.webp"),
hidGallery(_("Act 51"), "HGB027.png", "HG027.webp"),
hidGallery(_("Act 53"), "HGB028.png", "HG028.webp"),
hidGallery(_("Act 56"), "HGB029.png", "HG029.webp"),
hidGallery(_("Act 56.2"), "HGB030.png", "HG030.webp"),
hidGallery(_("Act 59"), "HGB031.png", "HG031.webp"),
hidGallery(_("Act 60"), "HGB032.png", "HG032.webp"),
hidGallery(_("Act 62"), "HGB033.png", "HG033.webp"),
hidGallery(_("Act 65"), "HGB034.png", "HG034.webp"),
hidGallery(_("Act 67"), "HGB035.png", "HG035.webp"),
hidGallery(_("Act 69"), "HGB036.png", "HG036.webp"),
hidGallery(_("Act 71"), "HGB037.png", "HG037.webp"),
hidGallery(_("Act 73"), "HGB038.png", "HG038.webp"),
hidGallery(_("Act 75"), "HGB039.png", "HG039.webp"),
hidGallery(_("Act 76"), "HGB040.png", "HG040.webp"),
hidGallery(_("Act 78"), "HGB041.png", "HG041.webp"),
hidGallery(_("Act 80"), "HGB042.png", "HG042.webp"),
hidGallery(_("Act 81"), "HGB043.png", "HG043.webp"),
hidGallery(_("Act 84"), "HGB044.png", "HG044.webp"),
hidGallery(_("Act 87"), "HGB046.png", "HG046.webp"),
hidGallery(_("Act 88"), "HGB045.png", "HG045.webp"),
hidGallery(_("Act 89"), "HGB047.png", "HG047.webp"),
hidGallery(_("Act 92"), "HGB048.png", "HG048.webp"),
hidGallery(_("Act 94"), "HGB049.png", "HG049.webp"),
hidGallery(_("Act 96"), "HGB050.png", "HG050.webp"),
hidGallery(_("Act 97"), "HGB051.png", "HG051.webp"),
hidGallery(_("Act 100"), "HGB052.png", "HG052.webp"),
hidGallery(_("Act 102"), "HGB053.png", "HG053.webp"),
hidGallery(_("Act 104"), "HGB054.png", "HG054.webp"),
hidGallery(_("Act 106"), "HGB055.png", "HG055.webp"),
hidGallery(_("Act 108"), "HGB056.png", "HG056.webp"),
hidGallery(_("Act 110"), "HGB057.png", "HG057.webp"),
hidGallery(_("Act 112"), "HGB058.png", "HG058.webp"),
hidGallery(_("Act 115"), "HGB060.png", "HG060.webp"),
hidGallery(_("Act 116"), "HGB059.png", "HG059.webp"),
hidGallery(_("Act 117"), "HGB061.png", "HG061.webp"),
hidGallery(_("Act 120"), "HGB062.png", "HG062.webp"),
hidGallery(_("Act 122"), "HGB063.png", "HG063.webp"),
hidGallery(_("Act 124"), "HGB064.png", "HG064.webp"),
hidGallery(_("Act 125"), "HGB066.png", "HG066.webp"),
hidGallery(_("Act 128"), "HGB065.png", "HG065.webp"),
hidGallery(_("Act 130"), "HGB067.png", "HG067.webp"),
hidGallery(_("Act 132"), "HGB068.png", "HG068.webp"),
hidGallery(_("Act 135"), "HGB069.png", "HG069.webp"),
hidGallery(_("Act 136"), "HGB070.png", "HG070.webp"),
hidGallery(_("Act 137"), "HGB071.png", "HG071.webp"),
hidGallery(_("Act 140"), "HGB072.png", "HG072.webp"),
hidGallery(_("Act 141"), "HGB073.png", "HG073.webp"),
hidGallery(_("Act 143"), "HGB074.png", "HG074.webp"),
hidGallery(_("Act 146"), "HGB075.png", "HG075.webp"),
hidGallery(_("Act 148"), "HGB076.png", "HG076.webp"),
hidGallery(_("Act 150"), "HGB077.png", "HG077.webp"),
hidGallery(_("Act 151"), "HGB078.png", "HG078.webp"),
hidGallery(_("Act 156"), "HGB079.png", "HG079.webp"),
hidGallery(_("Act 156.2"), "HGB080.png", "HG080.webp"),
hidGallery(_("Act 159"), "HGB081.png", "HG081.webp"),
hidGallery(_("Act 160"), "HGB082.png", "HG082.webp"),
hidGallery(_("Act 162"), "HGB083.png", "HG084.webp"),
hidGallery(_("Act 163"), "HGB084.png", "HG083.webp"),
hidGallery(_("Act 167"), "HGB085.png", "HG085.webp"),
hidGallery(_("Act 168"), "HGB086.png", "HG086.webp"),
hidGallery(_("Act 169"), "HGB087.png", "HG087.webp"),
hidGallery(_("Act 171"), "HGB088.png", "HG088.webp"),
hidGallery(_("Act 172"), "HGB089.png", "HG089.webp"),
hidGallery(_("Act 175"), "HGB090.png", "HG090.webp"),
hidGallery(_("Act 178"), "HGB091.png", "HG091.webp"),
hidGallery(_("Act 179"), "HGB092.png", "HG092.webp"),
hidGallery(_("Act 180"), "HGB093.png", "HG093.webp"),
hidGallery(_("Act 183"), "HGB094.png", "HG094.webp"),
hidGallery(_("Act 186"), "HGB095.png", "HG095.webp"),
hidGallery(_("Act 187"), "HGB096.png", "HG096.webp"),
hidGallery(_("Act 189"), "HGB097.png", "HG097.webp"),
hidGallery(_("Act 191"), "HGB098.png", "HG098.webp"),
hidGallery(_("Act 193"), "HGB099.png", "HG100.webp"),
hidGallery(_("Act 195"), "HGB100.png", "HG099.webp"),
hidGallery(_("Act 197"), "HGB101.png", "HG101.webp"),
hidGallery(_("Act 199"), "HGB102.png", "HG102.webp"),
hidGallery(_("Act 200"), "HGB104.png", "HG104.webp"),
hidGallery(_("Act 202"), "HGB103.png", "HG103.webp"),
hidGallery(_("Act 205"), "HGB105.png", "HG105.webp"),
hidGallery(_("Act 207"), "HGB106.png", "HG106.webp"),
hidGallery(_("Act 208"), "HGB107.png", "HG108.webp"),
hidGallery(_("Act 209"), "HGB108.png", "HG107.webp"),
hidGallery(_("Act 214"), "HGB110.png", "HG110.webp"),
hidGallery(_("Act 215"), "HGB109.png", "HG109.webp"),
hidGallery(_("Act 216"), "HGB112.png", "HG112.webp"),
hidGallery(_("Act 218"), "HGB111.png", "HG111.webp"),
hidGallery(_("Act 220"), "HGB113.png", "HG114.webp"),
hidGallery(_("Act 223"), "HGB114.png", "HG113.webp"),
hidGallery(_("Act 226"), "HGB115.png", "HG116.webp"),
hidGallery(_("Act 227"), "HGB116.png", "HG115.webp"),
hidGallery(_("Act 229"), "HGB117.png", "HG117.webp"),
hidGallery(_("Act 230"), "HGB118.png", "HG118.webp"),
hidGallery(_("Act 232"), "HGB120.png", "HG120.webp"),
hidGallery(_("Act 234"), "HGB119.png", "HG119.webp"),
hidGallery(_("Act 235"), "HGB121.png", "HG121.webp"),
hidGallery(_("Act 236"), "HGB122.png", "HG122.webp"),
hidGallery(_("Act 239"), "HGB123.png", "HG124.webp"),
hidGallery(_("Act 241"), "HGB124.png", "HG123.webp"),
hidGallery(_("Act 244"), "HGB125.png", "HG125.webp"),
hidGallery(_("Act 245"), "HGB126.png", "HG126.webp"),
hidGallery(_("Act 246"), "HGB127.png", "HG127.webp"),
hidGallery(_("Act 249"), "HGB128.png", "HG128.webp"),
hidGallery(_("Act 250"), "HGB129.png", "HG130.webp"),
hidGallery(_("Act 253"), "HGB130.png", "HG129.webp"),
hidGallery(_("Act 256"), "HGB131.png", "HG131.webp"),
hidGallery(_("Act 257"), "HGB132.png", "HG132.webp"),
hidGallery(_("Act 259"), "HGB133.png", "HG133.webp"),
hidGallery(_("Act 261"), "HGB134.png", "HG134.webp"),
hidGallery(_("Act 262"), "HGB135.png", "HG135.webp"),
hidGallery(_("Act 262.2"), "HGB136.png", "HG136.webp")
]

default rel = Relationships(S="S__", Si="S_____", D="D_______", Ni="N____", M="M__", Mo="M_____", A="A___", Au="A_____", B="B__", Br="B______", So="S__", Ne="N_____")

image HG012 = Movie(play="images/HG/HG012.webm", start_image="images/HG/HG012.png")
image HG015 = Movie(play="images/HG/HG015.webm", start_image="images/HG/HG015.png")
