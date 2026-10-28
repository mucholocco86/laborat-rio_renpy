################################################################################
## WELLS FRAMEWORK — SETTINGS / BASE LIMPA
################################################################################

init python:
    config.language = "brazilian"
    config.default_language = "brazilian"
    #config.language = "pt_br_zenpy"
    #config.default_language = "pt_br_zenpy"
    config.developer = True
    config.console = True
    config.hard_rollback_limit = 128
    config.rollback_length = 128

    config.gestures = {
        "n": "game_menu",
        "s": "hide_windows",
        "w": "rollback",
        "e": "skip",
        "n_s": "toggle_afm",
    }

    import os

    def toggle_power_save():
        if preferences.gl_framerate == 30:
            preferences.gl_framerate = None
        else:
            preferences.gl_framerate = 30
        renpy.restart_interaction()

    def get_all_languages():
        languages = ["Default"]
        path = os.path.join(renpy.config.gamedir, "tl")
        if os.path.exists(path):
            for entry in os.listdir(path):
                if os.path.isdir(os.path.join(path, entry)):
                    languages.append(entry)
        return languages

    def toggle_multiple_dialogue():
        persistent.multiple_dialogue = not persistent.multiple_dialogue
        renpy.restart_interaction()

    def restore_wells_defaults():
        # Restaura sempre os valores-base do Wells (referência 1920x1080).
        # A resolução atual NÃO é gravada no persistent: wells_screens.rpy
        # calcula a escala visual dinamicamente a partir do jogo em execução.
        # Assim, Reset volta ao mesmo padrão e esse padrão se adapta sozinho
        # ao abrir jogos com resoluções lógicas diferentes.
        persistent.pref_text_size_label = 31
        persistent.pref_text_size_dialogue = 31
        persistent.wells_name_size_offset = 2
        persistent.wells_name_dialogue_spacing = 0
        persistent.wells_line_spacing = 5
        persistent.wells_dialogue_y_offset = 0
        persistent.wells_textbox_x = 0.5
        persistent.wells_textbox_y = 0.95
        persistent.wells_textbox_width = 960
        persistent.wells_textbox_opacity = 0.35

        persistent.wells_multiple_y = 0
        persistent.wells_multiple_x = 0.0
        persistent.wells_multiple_width = 600
        persistent.wells_multiple_stack_step = 310
        persistent.wells_multiple_name_size = 25
        persistent.wells_multiple_text_size = 25
        persistent.wells_multiple_name_dialogue_spacing = 0

        persistent.wells_choice_size = gui.choice_button_text_size if gui.choice_button_text_size is not None else 33
        persistent.wells_choice_spacing = gui.choice_spacing if gui.choice_spacing is not None else 10
        persistent.wells_choice_width = 920
        persistent.wells_choice_xpos = 0.5
        persistent.wells_choice_ypos = 0.5

        persistent.wells_choice_slot = 0
        persistent.font_escolhida = None
        preferences.font_transform = None
        preferences.gl_framerate = None
        persistent.multiple_dialogue = True
        persistent.use_hw_video = True
        persistent.wells_force_outline = True
        config.hw_video = True
        renpy.restart_interaction()

    def listar_fontes():
        """
        Wells Framework - Detector de Fontes Híbrido com Proteção Anti-Duplicidade.
        Varre simultaneamente o arquivo .rpa e a pasta física espelho 'wells/fonts/'.
        Fontes externas com nomes idênticos às internas serão totalmente ignoradas.
        """
        fontes_finais = []
        fontes_internas_rpa = set()
        pasta_alvo = "wells/fonts/"

        # ----------------------------------------------------------------------
        # PASSO 1: Mapeia e dá prioridade absoluta para as fontes trancadas no .rpa
        # ----------------------------------------------------------------------
        for arquivo in renpy.list_files():
            caminho_limpo = arquivo.replace("\\", "/")
            if caminho_limpo.startswith("game/"):
                caminho_limpo = caminho_limpo[5:]

            if caminho_limpo.startswith(pasta_alvo):
                if caminho_limpo.lower().endswith(('.ttf', '.otf')):
                    nome_arquivo = os.path.basename(caminho_limpo)
                    
                    # Se o arquivo NÃO existe fisicamente no HD do jogador, ele está no .rpa
                    caminho_hd_real = os.path.join(renpy.config.gamedir, caminho_limpo)
                    if not os.path.exists(caminho_hd_real):
                        fontes_internas_rpa.add(nome_arquivo)
                        if nome_arquivo not in fontes_finais:
                            fontes_finais.append(nome_arquivo)

        # ----------------------------------------------------------------------
        # PASSO 2: Varre a pasta espelho física no HD procurando fontes inéditas
        # ----------------------------------------------------------------------
        caminho_pasta_fisica = os.path.join(renpy.config.gamedir, "wells", "fonts")
        if os.path.exists(caminho_pasta_fisica):
            for f in os.listdir(caminho_pasta_fisica):
                if f.lower().endswith((".ttf", ".otf")):
                    
                    # PROTEÇÃO DE DUPLICIDADE: Se o nome já existir no .rpa, ignora a externa
                    if f in fontes_internas_rpa:
                        continue
                        
                    if f not in fontes_finais:
                        fontes_finais.append(f)

        # Retorna a lista unificada e limpa contendo apenas os nomes das fontes (ex: "font.ttf")
        return fontes_finais


    def wells_font_transformer(old_font):
        if persistent.font_escolhida:
            return persistent.font_escolhida
        return old_font

    # Registra o transformador de fontes nativo de forma universal
    renpy.config.font_transforms["wells_custom"] = wells_font_transformer

    if "quick_wells" not in config.overlay_screens:
        config.overlay_screens.append("quick_wells")

init -1 python:
    if persistent.use_hw_video is None:
        persistent.use_hw_video = True
    config.hw_video = persistent.use_hw_video

    if persistent.multiple_dialogue is None:
        persistent.multiple_dialogue = True

    if persistent.font_escolhida:
        _preferences.font_transform = "wells_custom"

    if persistent.pref_text_size_label is None:
        persistent.pref_text_size_label = 31
    if persistent.pref_text_size_dialogue is None:
        persistent.pref_text_size_dialogue = 31
    if persistent.wells_name_size_offset is None:
        persistent.wells_name_size_offset = 2
    if persistent.wells_name_dialogue_spacing is None:
        persistent.wells_name_dialogue_spacing = 0
    if persistent.wells_line_spacing is None:
        persistent.wells_line_spacing = 5
    if persistent.wells_dialogue_y_offset is None:
        persistent.wells_dialogue_y_offset = 0

    if persistent.wells_textbox_x is None:
        persistent.wells_textbox_x = 0.5
    if persistent.wells_textbox_y is None:
        persistent.wells_textbox_y = 0.95
    if persistent.wells_textbox_width is None:
        persistent.wells_textbox_width = 960
    if persistent.wells_textbox_opacity is None:
        persistent.wells_textbox_opacity = 0.35

    if persistent.wells_multiple_x is None:
        persistent.wells_multiple_x = 0.0
    if persistent.wells_multiple_width is None:
        persistent.wells_multiple_width = 600
    if persistent.wells_multiple_stack_step is None:
        persistent.wells_multiple_stack_step = 310
    if persistent.wells_multiple_name_size is None:
        persistent.wells_multiple_name_size = 25
    if persistent.wells_multiple_text_size is None:
        persistent.wells_multiple_text_size = 25
    if persistent.wells_multiple_name_dialogue_spacing is None:
        persistent.wells_multiple_name_dialogue_spacing = 0

    if persistent.wells_choice_size is None:
        persistent.wells_choice_size = gui.choice_button_text_size if gui.choice_button_text_size is not None else 33
    if persistent.wells_choice_spacing is None:
        persistent.wells_choice_spacing = gui.choice_spacing if gui.choice_spacing is not None else 10
    if persistent.wells_choice_width is None:
        persistent.wells_choice_width = 920
    if persistent.wells_choice_xpos is None:
        persistent.wells_choice_xpos = 0.5
    if persistent.wells_choice_ypos is None:
        persistent.wells_choice_ypos = 0.5
    if persistent.wells_choice_slot is None:
        persistent.wells_choice_slot = 0

################################################################################
## FONTES
################################################################################

define 999 gui.text_font = "wells/fonts/Roboto-Regular.ttf"
define 999 gui.name_text_font = "wells/fonts/Roboto-Regular.ttf"
define 999 gui.interface_text_font = "wells/fonts/Roboto-Regular.ttf"

define wells_namebox_borders = Borders(5, 5, 5, 5)
define wells_text_size = 31

default persistent.pref_text_size_label = 31
default persistent.pref_text_size_dialogue = 31
default persistent.wells_name_size_offset = 2
default persistent.wells_name_dialogue_spacing = 0
default persistent.wells_line_spacing = 5
default persistent.wells_dialogue_y_offset = 0

default persistent.wells_textbox_x = 0.5
default persistent.wells_textbox_y = 0.95
default persistent.wells_textbox_width = 960
default persistent.wells_textbox_opacity = 0.35

default persistent.wells_multiple_y = 0
default persistent.wells_multiple_x = 0.0
default persistent.wells_multiple_width = 600
default persistent.wells_multiple_stack_step = 310
default persistent.wells_multiple_name_size = 25
default persistent.wells_multiple_text_size = 25
default persistent.wells_multiple_name_dialogue_spacing = 0

default persistent.wells_force_outline = True

default persistent.wells_choice_slot = 0
default persistent.wells_choice_size = 33
default persistent.wells_choice_spacing = 10
default persistent.wells_choice_xpos = 0.5
default persistent.wells_choice_ypos = 0.5
default persistent.wells_choice_width = 920

default persistent.font_escolhida = None
default wells_menu_tab = "main"
default quick_wells = True