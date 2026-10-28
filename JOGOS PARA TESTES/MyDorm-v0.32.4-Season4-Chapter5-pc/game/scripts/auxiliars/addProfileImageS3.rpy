label addProfileImageS3(index, filename, character, tipo="", special=""):
    #call addProfileImageS3 (4, "megan_4", meg, __(": 15 - Especial"), "")
    if _in_replay:
        return
    python:
        character.profileImages.pop (index) # first remove
        character.profileImages.insert (index, (filename, None)) # then add new
        lady = str(character)
        if special != "":
            lady = str(character.nick)
        texto1 = __("Imagen de perfil desbloqueada para ")
        texto2 = [
            ": 01 - Casual",
            __(": 02 - Fiesta/Cita"),
            ": 03 - Bikini",
            __(": 04 - Deporte"),
            __(": 05 - Trabajo"),
            __(": 06 - Disfraz"),
            ": 07 - DnD",
            __(": 08 - Lencería"),
            __(": 09 - Desnuda"),
            __(": 10 - Embarazada"),
            __(": 11 - Embarazada desnuda"),
            tipo,
            tipo,
            ": 14 - Topless",
            __(": 15 - Especial"),
            __(": 16 - Fiesta de despedida")
        ][index]
        renpy.notify (texto1 + lady + texto2)
    return
label addProfileImageNoNotification(index, filename, character):
    #call addProfileImageNoNotification (4, "megan_4", meg)
    if _in_replay:
        return
    python:
        character.profileImages.pop (index) # first remove
        character.profileImages.insert (index, (filename, None)) # then add new
    return
label notificationS3 (index, character):
    #call notificationS3 (0, mar)
    if _in_replay:
        return
    python:
        texto1 = __("Nueva decisión activada para ")
        lady = str(character)
        texto2 = [
            ": Anal",
            __(": Embarazo"),
            __(": Ruta")
        ][index]
        renpy.notify (texto1 + lady + texto2)
    return
label updateProfileImagesStartS4:
    call addProfileImageNoNotification (13, "oma_13", oma) from _call_addProfileImageNoNotification
    call addProfileImageNoNotification (0, "ama_00", ama) from _call_addProfileImageNoNotification_1
    call addProfileImageNoNotification (1, "ama_01", ama) from _call_addProfileImageNoNotification_2
    call addProfileImageNoNotification (4, "ama_4", ama) from _call_addProfileImageNoNotification_3
    call addProfileImageNoNotification (11, "ama_11", ama) from _call_addProfileImageNoNotification_4
    call addProfileImageNoNotification (13, "ama_13", ama) from _call_addProfileImageNoNotification_5
    call addProfileImageNoNotification (0, "bet_0", bet) from _call_addProfileImageNoNotification_6
    call addProfileImageNoNotification (2, "bet_2", bet) from _call_addProfileImageNoNotification_7
    call addProfileImageNoNotification (3, "bet_3", bet) from _call_addProfileImageNoNotification_8
    call addProfileImageNoNotification (4, "bet_4", bet) from _call_addProfileImageNoNotification_9
    if bet._var("route"):
        call addProfileImageNoNotification (7, "bet_7", bet) from _call_addProfileImageNoNotification_10
        call addProfileImageNoNotification (8, "bet_8", bet) from _call_addProfileImageNoNotification_11
    call addProfileImageNoNotification (13, "bet_13", bet) from _call_addProfileImageNoNotification_12
    call addProfileImageNoNotification (0, "dap_0", dap) from _call_addProfileImageNoNotification_13
    call addProfileImageNoNotification (1, "dap_1", dap) from _call_addProfileImageNoNotification_14
    call addProfileImageNoNotification (2, "dap_2", dap) from _call_addProfileImageNoNotification_15
    call addProfileImageNoNotification (3, "dap_3", dap) from _call_addProfileImageNoNotification_16
    call addProfileImageNoNotification (5, "dap_5", dap) from _call_addProfileImageNoNotification_17
    call addProfileImageNoNotification (6, "dap_6", dap) from _call_addProfileImageNoNotification_18
    if dap._var("route"):
        call addProfileImageNoNotification (7, "dap_7", dap) from _call_addProfileImageNoNotification_19
    call addProfileImageNoNotification (8, "dap_8", dap) from _call_addProfileImageNoNotification_20
    if dap._var("route"):
        call addProfileImageNoNotification (11, "dap_11", dap) from _call_addProfileImageNoNotification_21
    call addProfileImageNoNotification (12, "dap_12", dap) from _call_addProfileImageNoNotification_22
    call addProfileImageNoNotification (13, "dap_13", dap) from _call_addProfileImageNoNotification_23
    call addProfileImageNoNotification (0, "deb_0", deb) from _call_addProfileImageNoNotification_24
    call addProfileImageNoNotification (1, "deb_1", deb) from _call_addProfileImageNoNotification_25
    if deb._var("route"):
        call addProfileImageNoNotification (1, "deb_01", deb) from _call_addProfileImageNoNotification_26
    call addProfileImageNoNotification (2, "deb_2", deb) from _call_addProfileImageNoNotification_27
    call addProfileImageNoNotification (3, "deb_3", deb) from _call_addProfileImageNoNotification_28
    if deb._var("route"):
        call addProfileImageNoNotification (8, "deb_8", deb) from _call_addProfileImageNoNotification_29
    call addProfileImageNoNotification (13, "deb_13", deb) from _call_addProfileImageNoNotification_30
    call addProfileImageNoNotification (0, "eil_0", eil) from _call_addProfileImageNoNotification_31
    call addProfileImageNoNotification (2, "eil_2", eil) from _call_addProfileImageNoNotification_32
    call addProfileImageNoNotification (3, "eil_3", eil) from _call_addProfileImageNoNotification_33
    call addProfileImageNoNotification (4, "eil_4", eil) from _call_addProfileImageNoNotification_34
    if eil._var("route"):
        call addProfileImageNoNotification (5, "eil_5", eil) from _call_addProfileImageNoNotification_35
        call addProfileImageNoNotification (7, "eil_7", eil) from _call_addProfileImageNoNotification_36
        call addProfileImageNoNotification (8, "eil_8", eil) from _call_addProfileImageNoNotification_37
    call addProfileImageNoNotification (13, "eil_13", eil) from _call_addProfileImageNoNotification_38
    call addProfileImageNoNotification (0, "emm_0", emm) from _call_addProfileImageNoNotification_39
    call addProfileImageNoNotification (1, "emm_1", emm) from _call_addProfileImageNoNotification_40
    call addProfileImageNoNotification (2, "emm_2", emm) from _call_addProfileImageNoNotification_41
    call addProfileImageNoNotification (3, "emm_3", emm) from _call_addProfileImageNoNotification_42
    if emm._var("route"):
        call addProfileImageNoNotification (4, "emm_4", emm) from _call_addProfileImageNoNotification_43
    call addProfileImageNoNotification (5, "emm_5", emm) from _call_addProfileImageNoNotification_44
    call addProfileImageNoNotification (6, "emm_6", emm) from _call_addProfileImageNoNotification_45
    if emm._var("route"):
        call addProfileImageNoNotification (7, "emm_7", emm) from _call_addProfileImageNoNotification_46
    call addProfileImageNoNotification (8, "emm_8", emm) from _call_addProfileImageNoNotification_47
    call addProfileImageNoNotification (12, "emm_12", emm) from _call_addProfileImageNoNotification_48
    call addProfileImageNoNotification (13, "emm_13", emm) from _call_addProfileImageNoNotification_49
    call addProfileImageNoNotification (0, "eri_0", eri) from _call_addProfileImageNoNotification_50
    call addProfileImageNoNotification (1, "eri_1", eri) from _call_addProfileImageNoNotification_51
    call addProfileImageNoNotification (2, "eri_2", eri) from _call_addProfileImageNoNotification_52
    call addProfileImageNoNotification (3, "eri_3", eri) from _call_addProfileImageNoNotification_53
    call addProfileImageNoNotification (4, "eri_4", eri) from _call_addProfileImageNoNotification_54
    call addProfileImageNoNotification (5, "eri_5", eri) from _call_addProfileImageNoNotification_55
    call addProfileImageNoNotification (6, "eri_6", eri) from _call_addProfileImageNoNotification_56
    if eri._var("route"):
        call addProfileImageNoNotification (7, "eri_7", eri) from _call_addProfileImageNoNotification_57
        call addProfileImageNoNotification (8, "eri_8", eri) from _call_addProfileImageNoNotification_58
    call addProfileImageNoNotification (12, "eri_12", eri) from _call_addProfileImageNoNotification_59
    call addProfileImageNoNotification (13, "eri_13", eri) from _call_addProfileImageNoNotification_60
    call addProfileImageNoNotification (0, "eva_0", eva) from _call_addProfileImageNoNotification_61
    call addProfileImageNoNotification (1, "eva_1", eva) from _call_addProfileImageNoNotification_62
    call addProfileImageNoNotification (2, "eva_2", eva) from _call_addProfileImageNoNotification_63
    call addProfileImageNoNotification (4, "eva_4", eva) from _call_addProfileImageNoNotification_64
    if eva._var("route"):
        call addProfileImageNoNotification (7, "eva_7", eva) from _call_addProfileImageNoNotification_65
        call addProfileImageNoNotification (8, "eva_8", eva) from _call_addProfileImageNoNotification_66
    call addProfileImageNoNotification (11, "eva_11", eva) from _call_addProfileImageNoNotification_67
    call addProfileImageNoNotification (13, "eva_13", eva) from _call_addProfileImageNoNotification_68
    call addProfileImageNoNotification (0, "kat_0", kat) from _call_addProfileImageNoNotification_69
    call addProfileImageNoNotification (1, "kat_1", kat) from _call_addProfileImageNoNotification_70
    call addProfileImageNoNotification (2, "kat_2", kat) from _call_addProfileImageNoNotification_71
    call addProfileImageNoNotification (3, "kat_3", kat) from _call_addProfileImageNoNotification_72
    call addProfileImageNoNotification (0, "kia_0", kia) from _call_addProfileImageNoNotification_73
    if kia._var("route"):
        call addProfileImageNoNotification (1, "kia_1", kia) from _call_addProfileImageNoNotification_74
    call addProfileImageNoNotification (2, "kia_2", kia) from _call_addProfileImageNoNotification_75
    call addProfileImageNoNotification (3, "kia_3", kia) from _call_addProfileImageNoNotification_76
    call addProfileImageNoNotification (4, "kia_4", kia) from _call_addProfileImageNoNotification_77
    call addProfileImageNoNotification (6, "kia_6", kia) from _call_addProfileImageNoNotification_78
    if kia._var("route"):
        call addProfileImageNoNotification (7, "kia_7", kia) from _call_addProfileImageNoNotification_79
        call addProfileImageNoNotification (8, "kia_8", kia) from _call_addProfileImageNoNotification_80
    call addProfileImageNoNotification (13, "kia_13", kia) from _call_addProfileImageNoNotification_81
    call addProfileImageNoNotification (0, "kim_0", kim) from _call_addProfileImageNoNotification_82
    call addProfileImageNoNotification (1, "kim_1", kim) from _call_addProfileImageNoNotification_83
    call addProfileImageNoNotification (2, "kim_2", kim) from _call_addProfileImageNoNotification_84
    call addProfileImageNoNotification (3, "kim_3", kim) from _call_addProfileImageNoNotification_85
    call addProfileImageNoNotification (4, "kim_4", kim) from _call_addProfileImageNoNotification_86
    call addProfileImageNoNotification (5, "kim_5", kim) from _call_addProfileImageNoNotification_87
    call addProfileImageNoNotification (8, "kim_8", kim) from _call_addProfileImageNoNotification_88
    call addProfileImageNoNotification (13, "kim_13", kim) from _call_addProfileImageNoNotification_89
    call addProfileImageNoNotification (0, "lis_0", lis) from _call_addProfileImageNoNotification_90
    call addProfileImageNoNotification (2, "lis_2", lis) from _call_addProfileImageNoNotification_91
    call addProfileImageNoNotification (3, "lis_3", lis) from _call_addProfileImageNoNotification_92
    call addProfileImageNoNotification (13, "lis_13", lis) from _call_addProfileImageNoNotification_93
    call addProfileImageNoNotification (0, "mad_0", mad) from _call_addProfileImageNoNotification_94
    call addProfileImageNoNotification (2, "mad_2", mad) from _call_addProfileImageNoNotification_95
    call addProfileImageNoNotification (4, "mad_4", mad) from _call_addProfileImageNoNotification_96
    call addProfileImageNoNotification (6, "mad_6", mad) from _call_addProfileImageNoNotification_97
    if mad._var("route"):
        call addProfileImageNoNotification (7, "mad_7", mad) from _call_addProfileImageNoNotification_98
        call addProfileImageNoNotification (8, "mad_8", mad) from _call_addProfileImageNoNotification_99
        call addProfileImageNoNotification (11, "mad_11", mad) from _call_addProfileImageNoNotification_100
        call addProfileImageNoNotification (12, "mad_12", mad) from _call_addProfileImageNoNotification_101
    call addProfileImageNoNotification (13, "mad_13", mad) from _call_addProfileImageNoNotification_102
    if mad._var("route"):
        call addProfileImageNoNotification (14, "mad_14", mad) from _call_addProfileImageNoNotification_103
    call addProfileImageNoNotification (0, "mar_0", mar) from _call_addProfileImageNoNotification_104
    if mar._var("route"):
        call addProfileImageNoNotification (1, "mar_1", mar) from _call_addProfileImageNoNotification_105
    call addProfileImageNoNotification (2, "mar_2", mar) from _call_addProfileImageNoNotification_106
    call addProfileImageNoNotification (3, "mar_3", mar) from _call_addProfileImageNoNotification_107
    call addProfileImageNoNotification (4, "mar_4", mar) from _call_addProfileImageNoNotification_108
    call addProfileImageNoNotification (5, "mar_5", mar) from _call_addProfileImageNoNotification_109
    call addProfileImageNoNotification (6, "mar_6", mar) from _call_addProfileImageNoNotification_110
    call addProfileImageNoNotification (7, "mar_7", mar) from _call_addProfileImageNoNotification_111
    if mar._var("route"):
        call addProfileImageNoNotification (8, "mar_8", mar) from _call_addProfileImageNoNotification_112
    call addProfileImageNoNotification (13, "mar_13", mar) from _call_addProfileImageNoNotification_113
    call addProfileImageNoNotification (0, "mee_0", mee) from _call_addProfileImageNoNotification_114
    if mee._var("route"):
        call addProfileImageNoNotification (1, "mee_01", mee) from _call_addProfileImageNoNotification_115
    else:
        call addProfileImageNoNotification (1, "mee_1", mee) from _call_addProfileImageNoNotification_116
    call addProfileImageNoNotification (2, "mee_2", mee) from _call_addProfileImageNoNotification_117
    if mee._var("route"):
        call addProfileImageNoNotification (8, "mee_8", mee) from _call_addProfileImageNoNotification_118
    call addProfileImageNoNotification (13, "mee_13", mee) from _call_addProfileImageNoNotification_119
    call addProfileImageNoNotification (0, "meg_0", meg) from _call_addProfileImageNoNotification_120
    call addProfileImageNoNotification (2, "meg_2", meg) from _call_addProfileImageNoNotification_121
    call addProfileImageNoNotification (4, "meg_4", meg) from _call_addProfileImageNoNotification_122
    if meg._var("route"):
        call addProfileImageNoNotification (7, "meg_7", meg) from _call_addProfileImageNoNotification_123
        call addProfileImageNoNotification (8, "meg_8", meg) from _call_addProfileImageNoNotification_124
    call addProfileImageNoNotification (0, "nor_0", nor) from _call_addProfileImageNoNotification_125
    call addProfileImageNoNotification (1, "nor_1", nor) from _call_addProfileImageNoNotification_126
    call addProfileImageNoNotification (2, "nor_2", nor) from _call_addProfileImageNoNotification_127
    call addProfileImageNoNotification (3, "nor_3", nor) from _call_addProfileImageNoNotification_128
    call addProfileImageNoNotification (4, "nor_4", nor) from _call_addProfileImageNoNotification_129
    call addProfileImageNoNotification (5, "nor_5", nor) from _call_addProfileImageNoNotification_130
    call addProfileImageNoNotification (7, "nor_7", nor) from _call_addProfileImageNoNotification_131
    call addProfileImageNoNotification (8, "nor_8", nor) from _call_addProfileImageNoNotification_132
    call addProfileImageNoNotification (13, "nor_13", nor) from _call_addProfileImageNoNotification_133
    call addProfileImageNoNotification (0, "oma_0", oma) from _call_addProfileImageNoNotification_134
    call addProfileImageNoNotification (2, "oma_2", oma) from _call_addProfileImageNoNotification_135
    call addProfileImageNoNotification (3, "oma_3", oma) from _call_addProfileImageNoNotification_136
    call addProfileImageNoNotification (4, "oma_4", oma) from _call_addProfileImageNoNotification_137
    if oma._var("route"):
        call addProfileImageNoNotification (5, "oma_5", oma) from _call_addProfileImageNoNotification_138
        call addProfileImageNoNotification (7, "oma_7", oma) from _call_addProfileImageNoNotification_139
        call addProfileImageNoNotification (8, "oma_8", oma) from _call_addProfileImageNoNotification_140
    call addProfileImageNoNotification (0, "sai_0", sai) from _call_addProfileImageNoNotification_141
    call addProfileImageNoNotification (1, "sai_1", sai) from _call_addProfileImageNoNotification_142
    call addProfileImageNoNotification (2, "sai_2", sai) from _call_addProfileImageNoNotification_143
    call addProfileImageNoNotification (3, "sai_3", sai) from _call_addProfileImageNoNotification_144
    if sai._var("route"):
        call addProfileImageNoNotification (7, "sai_7", sai) from _call_addProfileImageNoNotification_145
        call addProfileImageNoNotification (8, "sai_8", sai) from _call_addProfileImageNoNotification_146
    call addProfileImageNoNotification (13, "sai_13", sai) from _call_addProfileImageNoNotification_147
    call addProfileImageNoNotification (0, "sam_0", sam) from _call_addProfileImageNoNotification_148
    call addProfileImageNoNotification (1, "sam_1", sam) from _call_addProfileImageNoNotification_149
    call addProfileImageNoNotification (2, "sam_2", sam) from _call_addProfileImageNoNotification_150
    call addProfileImageNoNotification (3, "sam_3", sam) from _call_addProfileImageNoNotification_151
    call addProfileImageNoNotification (4, "sam_4", sam) from _call_addProfileImageNoNotification_152
    if sam._var("route"):
        call addProfileImageNoNotification (7, "sam_7", sam) from _call_addProfileImageNoNotification_153
        call addProfileImageNoNotification (8, "sam_8", sam) from _call_addProfileImageNoNotification_154
    call addProfileImageNoNotification (13, "sam_13", sam) from _call_addProfileImageNoNotification_155
    call addProfileImageNoNotification (0, "sca_0", sca) from _call_addProfileImageNoNotification_156
    call addProfileImageNoNotification (1, "sca_1", sca) from _call_addProfileImageNoNotification_157
    call addProfileImageNoNotification (2, "sca_2", sca) from _call_addProfileImageNoNotification_158
    call addProfileImageNoNotification (3, "sca_3", sca) from _call_addProfileImageNoNotification_159
    call addProfileImageNoNotification (5, "sca_5", sca) from _call_addProfileImageNoNotification_160
    call addProfileImageNoNotification (6, "sca_6", sca) from _call_addProfileImageNoNotification_161
    if sca._var("route"):
        call addProfileImageNoNotification (7, "sca_7", sca) from _call_addProfileImageNoNotification_162
    call addProfileImageNoNotification (8, "sca_8", sca) from _call_addProfileImageNoNotification_163
    call addProfileImageNoNotification (12, "sca_12", sca) from _call_addProfileImageNoNotification_164
    call addProfileImageNoNotification (13, "sca_13", sca) from _call_addProfileImageNoNotification_165
    call addProfileImageNoNotification (0, "sim_0", sim) from _call_addProfileImageNoNotification_166
    call addProfileImageNoNotification (1, "sim_1", sim) from _call_addProfileImageNoNotification_167
    call addProfileImageNoNotification (2, "sim_2", sim) from _call_addProfileImageNoNotification_168
    if sim._var("route"):
        call addProfileImageNoNotification (8, "sim_8", sim) from _call_addProfileImageNoNotification_169
    call addProfileImageNoNotification (13, "sim_13", sim) from _call_addProfileImageNoNotification_170
    $ texto1 = __("Imágenes de perfil actualizadas")
    $ renpy.notify (texto1)
    return
label updateChances:
    $ bet._var("chanceRoute", True)
    if eri._var("route") and emm._var("route") and dap._var("route"):
        $ emm._var("foursome", True)
        $ eri._var("foursome", True)
        $ dap._var("foursome", True)
    $ eva._var("chanceChoking", True)
    $ eva._var("chancePregnant", True)
    $ kim._var("chanceRoute", True)
    $ kim._var("chanceSaved", True)
    $ mad._var("chanceFart", True)
    $ mar._var("analChance", True)
    $ meg._var("chanceAnal", True)
    $ mee._var("chanceIceCream", True)
    return
