screen JK_MoveCopySavesSelectSaves(view_model, saves_to_process, show_thumbnails, last_selected_save):
    style_prefix 'JK'
    modal True

    viewport:
        mousewheel True
        draggable True
        scrollbars "vertical"
        vscrollbar_unscrollable "hide"
        pagekeys True
        ymaximum 0.85

        python:
            source_saves = view_model.source_saves
            other_saves = view_model.destination_saves

            class FlipPlaythroughsAction(renpy.ui.Action):
                def __init__(self, source_playthrough, destination_playthrough):
                    self.source_playthrough = source_playthrough
                    self.destination_playthrough = destination_playthrough
                
                def __call__(self):
                    cs = renpy.current_screen()
                    
                    if cs is None:
                        return
                    
                    cs.scope["source_playthrough"] = self.destination_playthrough
                    cs.scope["destination_playthrough"] = self.source_playthrough
                    cs.scope["saves_to_process"] = []
                    cs.scope["view_model"] = None
                    cs.scope["last_selected_save"] = None
                    
                    renpy.restart_interaction()

            class ClearSourcePlaythroughAction(renpy.ui.Action):
                def __call__(self):
                    cs = renpy.current_screen()
                    
                    if cs is None:
                        return
                    
                    cs.scope["view_model"] = None
                    cs.scope["saves_to_process"] = []
                    cs.scope["source_playthrough"] = None
                    cs.scope["last_selected_save"] = None
                    
                    renpy.restart_interaction()

            class ClearDestinationPlaythroughAction(renpy.ui.Action):
                def __call__(self):
                    cs = renpy.current_screen()
                    
                    if cs is None:
                        return
                    
                    cs.scope["view_model"] = None
                    cs.scope["saves_to_process"] = []
                    cs.scope["destination_playthrough"] = None
                    cs.scope["last_selected_save"] = None
                    
                    renpy.restart_interaction()

            class SaveSelectedAction(renpy.ui.Action):
                def __init__(self, saves, save, view_model, last_selected_save):
                    self.saves = saves
                    self.save = save
                    self.view_model = view_model
                    self.last_selected_save = last_selected_save
                
                def __call__(self):
                    import pygame_sdl2 as pygame
                    
                    if pygame.key.get_mods() & pygame.KMOD_SHIFT:
                        start_index = self.view_model.source_saves.index(self.last_selected_save)
                        end_index = self.view_model.source_saves.index(self.save)
                        
                        if start_index > -1 and end_index > -1:
                            new_saves = []
                            
                            for self.save in self.view_model.source_saves[renpy.store.JK.PY_MINIMUM(start_index, end_index):renpy.store.JK.PY_MAXIMUM(start_index, end_index) + 1]:
                                if self.save in new_saves:
                                    new_saves.remove(self.save)
                                else:
                                    new_saves.append(self.save)
                            
                            SetScreenVariable("saves_to_process", new_saves)()
                            return
                    elif pygame.key.get_mods() & pygame.KMOD_LCTRL:
                        if self.save in self.saves:
                            self.saves.remove(self.save)
                        else:
                            self.saves.append(self.save)
                    else:
                        SetScreenVariable("saves_to_process", [self.save])()
                    
                    
                    SetScreenVariable("last_selected_save", self.save)()

        vbox:
            xfill True

            grid 5 1:
                xfill True

                hbox

                use JK_IconButton(text=view_model.source_playthrough.name, action=ClearSourcePlaythroughAction(), tt="Alterar jornada de origem", color=JK.Colors.theme, size=30)
                use JK_IconButton(text="→", action=FlipPlaythroughsAction(view_model.source_playthrough, view_model.destination_playthrough), tt="Trocar jornadas", color=JK.Colors.theme, size=30)
                use JK_IconButton(text=view_model.destination_playthrough.name, action=ClearDestinationPlaythroughAction(), tt="Alterar jornada de destino", color=JK.Colors.theme, size=30)

                hbox

            hbox:
                xfill True

                vbox xalign 1.0:
                    use JK_Checkbox(checked=show_thumbnails, text="Exibir miniaturas\n{size=-5}(Pode causar lentidão ou até travar o jogo){/size}", action=SetScreenVariable("show_thumbnails", not show_thumbnails))

            vbox:
                spacing 2


                button:
                    xfill True
                    action ToggleScreenVariable("saves_to_process", [] + source_saves, [])

                    has hbox
                    xfill True
                    use JK_Checkbox(checked=None if len(saves_to_process) != len(source_saves) and len(saves_to_process) > 0 else len(saves_to_process) == len(source_saves), text="")

                    text str(len(saves_to_process)) + " selected" yalign 0.5

                $ i = 0
                for save in source_saves:
                    $ i += 1

                    button style ("JK_row_button" if i % 2 == 0 else "JK_row_odd_button") selected save in saves_to_process:
                        xfill True
                        action [SaveSelectedAction(saves_to_process, save, view_model, last_selected_save)]

                        has grid 5 1
                        xfill True
                        use JK_Checkbox(checked=save in saves_to_process, text="", action=ToggleSetMembership(saves_to_process, save))


                        hbox yalign 0.5:
                            if show_thumbnails:
                                add view_model.source_instance.location.screenshot_including_inactive(save) size JK.Image.get_limited_image_size_with_preserved_aspect_ratio(100, 80)

                            use JK_XSpacer()

                            hbox yalign 0.5:
                                if save in source_saves:
                                    text save
                                else:
                                    text "N/A" color JK.Colors.na

                        text "→" yalign 0.5 xsize 40


                        hbox yalign 0.5:
                            hbox yalign 0.5:
                                if save in other_saves:
                                    text save
                                else:
                                    text "N/A" color JK.Colors.na

                            use JK_XSpacer()

                            if show_thumbnails:
                                add view_model.destination_instance.location.screenshot_including_inactive(save) size JK.Image.get_limited_image_size_with_preserved_aspect_ratio(100, 80)

                        hbox yalign 0.5:
                            text "Conflito!" color (JK.Colors.warning if save in other_saves else "#ffffff00")


    hbox:
        xfill True
        yfill True

        vbox xalign 0.0:
            text "{color=#abe9ff}clique{/color} para selecionar somente um item"
            text "{color=#abe9ff}Shift + clique{/color} para selecionar vários itens"
            text "{color=#abe9ff}Ctrl + clique{/color} ou {color=#abe9ff}clique na caixa{/color} para selecionar ou desmarcar um item"

        vbox:
            style_prefix "JK_dialog_action_buttons"
            vbox xalign 1.0:

                hbox:
                    use JK_IconButton(icon="\ue675", text="Mover", action=JK.MoveCopySavesViewModel.StartProcessAction(view_model, saves_to_process, mode="MOVE"), disabled=len(saves_to_process) == 0)


                hbox:
                    use JK_IconButton(icon="\ue161", text="Copiar", action=JK.MoveCopySavesViewModel.StartProcessAction(view_model, saves_to_process), disabled=len(saves_to_process) == 0)


                hbox:
                    use JK_IconButton(icon="\ue5cd", text="Fechar", action=Hide("JK_MoveCopySaves"))
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
