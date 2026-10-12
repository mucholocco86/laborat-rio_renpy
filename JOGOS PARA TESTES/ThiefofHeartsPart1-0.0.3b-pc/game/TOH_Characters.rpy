

default v_allow_redefine = False

init:
    $ y_name = "Jack"
    $ b_name = "Bella"
    $ a_name = "Ariel"
    $ v_name = "Vivian"
    $ vic_name = "Victor"

    $ lastname = "Smith"
    $ y_lastname = "Aroxson"

    $ mc_a_rel = "roommate"
    $ a_mc_rel = "roommate"
    $ mc_b_rel = "roommate"
    $ b_mc_rel = "roommate"
    $ v_mc_rel = "landlady"
    $ mc_v_rel = "tenant"
    $ vic_mc_rel = "landlord"
    $ mc_vic_rel = "tenant"
    $ mc_a_b_rel = "roommate"
    $ mc_v_vic_rel = "landlord"


    $ mc_a_address = "mate"
    $ a_mc_address = "mate"
    $ mc_b_address = "mate"
    $ b_mc_address = "mate"

    $ v_pre_address = "Miss"
    $ vic_pre_address = "Mister"

    $ mc_v_address = v_pre_address + " " + lastname
    $ mc_vic_address = vic_pre_address + " " + lastname

    $ private_group = "team"
    $ public_group = "group"


    $ name = ""
    $ address = ""
    $ address2 = ""
    $ lname = ""
    $ rel = ""
    $ rel2 = ""
    $ var_name = ""
    $ stored_input = ""
    $ show_default_value = False


    image black = "#000000"
    image white = "#ffffff"


    $ v_choice_type = ""






define mc = DynamicCharacter("[y_name]", color="#73bbdf")
define vic = Character("[vic_name]", color="#9d9fa0")
define v = DynamicCharacter("[v_name]", color="#0f39ab")
define b = DynamicCharacter("[b_name]", color="#C371C4")
define a = DynamicCharacter("[a_name]", color="#df7373")

define leader = Character("Leader", color="#9d9fa0")
define officer = Character("Officer", color="#3256a8")
define off_justice = Character("Officer Justice", color="#3256a8")
define dispatcher = Character("Dispatcher", color="#5e5e5e")
define dis_officer = Character("Distressed Officer", color="#718ecf")
define old_man = Character("Old Man", color="#3a3a3a")
define boss = Character("Boss", color="#3a3a3a")
define coworker = Character("Co-worker", color="#3a3a3a")
define cathy = Character("Cathy", color="#3a3a3a")
define head_chef = Character("Head Chef", color="#718ecf")
define security = Character("Security", color="#b11cc4")
define un = Character("Unknown", color="#5e5e5e")
define pretty_g = Character("Pretty Girl", color="#ab1111")
define ha = Character("Harry", color="#3256a8")
define luke = Character("Luke", color="#3a3a3a")
define woman = Character("Woman", color="#9d9fa0")
define megan = Character("Megan", color="#9d9fa0")
define driver = Character("Driver", color="#df7373")
define niles = Character("Niles", color="#534949")
define stoner = Character("Stoner", color="#c8df73")
define milf = Character("Hot Milf", color="#c43b50")
define waitress = Character("Waitress", color="#C371C4")
define female_v = Character("Female Voice", color="#C371C4")
define female_v2 = Character("Female Voice", color="#c77884")
define hacker = Character("Hacker Girl", color="#df7373")

define ju = Character("Juliet", color="#5e5e5e")
define mik = Character("Mikayla", color="#7da4deb9")
define tash = Character("Tasha", color="#e217ac")
define blonde = Character("Blonde", color="#c8df73")
define clerk1 = Character("Clerk1", color="#3a3a3a")
define clerk2 = Character("Clerk2", color="#0a5038")
define drama_coach = Character("Drama Coach", color="#718ecf")
define zora = Character("Zora", color="#e217ac")
define thug = Character("Thug", color="#70521e")
define guy = Character("Guy", color="#3a3a3a")
define guard = Character("Guard", color="#ea2727")
define staff = Character("Staff", color="#b11cc4")
define the_dean = Character("The Dean", color="#1c9615")
define teacher = Character("Teacher", color="#718ecf")
define class = Character("Class", color="#c8df73")
define coach = Character("Coach", color="#718ecf")
define girl1 = Character("Girl1", color="#c8df73")
define girl2 = Character("Girl2", color="#5e5e5e")
define barista = Character("Barista", color="#df7373")
define man = Character("Man", color="#0f39ab")


define student1 = Character("Student1", color="#3a3a3a")
define student2 = Character("Student2", color="#0a5038")


define announcer = Character("Announcer", color="#718ecf")
define tattooist = Character("Tattooist", color="#5f5a5a")
define travis = Character("Travis", color="#5f5a5a")
define older_man = Character("Old Man", color="#b11cc4")
define lucy = Character("Lucy", color="#b11cc4")
define bruno = Character("Bruno", color="#70521e")
define movie_kid1 = Character("Kid1", color="#c8df73", italic=True)
define movie_kid2 = Character("Kid2", color="#5e5e5e", italic=True)
define movie_man = Character("Man", color="#0f39ab", italic=True)
define movie_woman1 = Character("Woman1", color="#5e5e5e", italic=True)
define movie_woman2 = Character("Woman2", color="#0a5038", italic=True)
define police = Character("POLICE", color="#ab1111")
define con = Character("Concierge", color="#5e5e5e")
define mv = Character("Miss Veerhart", color="#ea2727")


init python:
    class MyInputValue(InputValue):
        def __init__(self, var, default=""):
            self.var = var
            
            if not hasattr(store, var):
                setattr(store, var, default)
        
        def get_text(self):
            return getattr(store, self.var)
        
        def set_text(self, s):
            setattr(store, self.var, s)
        
        def enter(self):
            renpy.run(self.Disable())
            raise renpy.IgnoreEvent()


    class NameInputValue(InputValue):
        def __init__(self, var, scr):
            self.var = var
            self.scr = scr
        
        def get_text(self):
            return getattr(store, self.var)
        
        def set_text(self, s):
            setattr(store.persistent, self.var, s)
            setattr(store, self.var, s)
        
        def enter(self):
            renpy.run(Hide(self.scr))
            raise renpy.IgnoreEvent()


    def factory_restore_all():
        rel_dict = {"y_name" : "Jack",
                    "b_name" : "Bella",
                    "a_name" : "Ariel",
                    "v_name" : "Vivian",
                    "vic_name" : "Victor",
                    "lastname" : "Smith",
                    "y_lastname" : "Aroxson",
                    "mc_a_rel" : "roommate",
                    "a_mc_rel" : "roommate",
                    "mc_b_rel" : "roommate",
                    "b_mc_rel" : "roommate",
                    "v_mc_rel" : "landlady",
                    "mc_v_rel" : "tenant",
                    "vic_mc_rel" : "landlord",
                    "mc_vic_rel" : "tenant",
                    "mc_a_address" : "mate",
                    "a_mc_address" : "mate",
                    "mc_b_address" : "mate",
                    "b_mc_address" : "mate",
                    "v_pre_address" : "Miss",
                    "vic_pre_address" : "Mister",
                    "mc_v_address" : "Miss Smith",
                    "mc_vic_address" : "Mister Smith",
                    "private_group" : "team",
                    "public_group" : "group",
                    "mc_a_b_rel" : "roommate",
                    "mc_v_vic_rel" : "landlord"}
        for key, value in rel_dict.items():
            setattr(renpy.store, key, value)



    def set_persistent_names(action):
        if action == "set":
            rel_dict = {"b_name" : b_name,
                        "a_name" : a_name,
                        "v_name" : v_name,
                        "vic_name" : vic_name,
                        "lastname" : lastname,
                        "mc_a_rel" : mc_a_rel,
                        "a_mc_rel" : a_mc_rel,
                        "mc_b_rel" : mc_b_rel,
                        "b_mc_rel" : b_mc_rel,
                        "v_mc_rel" : v_mc_rel,
                        "mc_v_rel" : mc_v_rel,
                        "vic_mc_rel" : vic_mc_rel,
                        "mc_vic_rel" : mc_vic_rel,
                        "mc_a_address" : mc_a_address,
                        "a_mc_address" : a_mc_address,
                        "mc_b_address" : mc_b_address,
                        "b_mc_address" : b_mc_address,
                        "v_pre_address" : v_pre_address,
                        "vic_pre_address" : vic_pre_address,
                        "mc_v_address" : mc_v_address,
                        "mc_vic_address" : mc_vic_address,
                        "private_group" : private_group,
                        "public_group" : public_group,
                        "mc_a_b_rel" : mc_a_b_rel,
                        "mc_v_vic_rel" : mc_v_vic_rel}
            for key, value in rel_dict.items():
                setattr(store.persistent, key, value)
        else:
            rel_dict = {"b_name" : persistent.b_name,
                        "a_name" : persistent.a_name,
                        "v_name" : persistent.v_name,
                        "vic_name" : persistent.vic_name,
                        "lastname" : persistent.lastname,
                        "mc_a_rel" : persistent.mc_a_rel,
                        "a_mc_rel" : persistent.a_mc_rel,
                        "mc_b_rel" : persistent.mc_b_rel,
                        "b_mc_rel" : persistent.b_mc_rel,
                        "v_mc_rel" : persistent.v_mc_rel,
                        "mc_v_rel" : persistent.mc_v_rel,
                        "vic_mc_rel" : persistent.vic_mc_rel,
                        "mc_vic_rel" : persistent.mc_vic_rel,
                        "mc_a_address" : persistent.mc_a_address,
                        "a_mc_address" : persistent.a_mc_address,
                        "mc_b_address" : persistent.mc_b_address,
                        "b_mc_address" : persistent.b_mc_address,
                        "v_pre_address" : persistent.v_pre_address,
                        "vic_pre_address" : persistent.vic_pre_address,
                        "mc_v_address" : persistent.mc_v_address,
                        "mc_vic_address" : persistent.mc_vic_address,
                        "private_group" : persistent.private_group,
                        "public_group" : persistent.public_group,
                        "mc_a_b_rel" : persistent.mc_a_b_rel,
                        "mc_v_vic_rel" : persistent.mc_v_vic_rel}
            for key, value in rel_dict.items():
                setattr(renpy.store, key, value)
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
