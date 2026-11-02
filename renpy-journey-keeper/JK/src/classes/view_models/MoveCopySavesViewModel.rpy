init python in JK:
    _constant = True
    import threading
    import time

    class MoveCopySavesViewModel(x52NonPicklable):
        def __init__(self, source_playthrough, destination_playthrough):
            self.source_playthrough = source_playthrough
            self.destination_playthrough = destination_playthrough
            
            self.processing = False
            self.saves_to_process = []
            self.processed = 0
            self.overwrite_all = False
            self.skip_all = False
            self.mode = "COPY"  
            self.stage = "COPY"  
            self.error = None
            self.success = None
            
            self.source_instance = None
            self.destination_instance = None
            
            self.source_saves = []
            self.destination_saves = []
            self.skipped = []
            
            self.loadSaves()
            self.save_thread = None  
            self.cleanup_thread = None  
            self.skip_conflicts_thread = None  
            
            self.source_instance = SaveSystem.get_or_create_playthrough_save_instance(self.source_playthrough)
            if not self.source_instance:
                self.error = "Não foi possível encontrar o local de origem."
                self.processing = False
                renpy.restart_interaction()
                return
            
            self.destination_instance = SaveSystem.get_or_create_playthrough_save_instance(self.destination_playthrough)
            if not self.destination_instance:
                self.error = "Não foi possível encontrar o local de destino."
                self.processing = False
                renpy.restart_interaction()
                return
        
        def loadSaves(self):
            self.source_saves = Utils.sort_saves(SaveSystem.list_all_saves_for_playthrough(self.source_playthrough))
            self.destination_saves = SaveSystem.list_all_saves_for_playthrough(self.destination_playthrough)
        
        def process_saves(self, saves, mode="COPY"):
            self.mode = mode
            self.stage = "COPY"
            self.overwrite_all = False
            self.skip_all = False
            self.processing = True
            self.processed = 0
            self.saves_to_process = saves
            self.skipped = []
            
            renpy.restart_interaction()
            
            
            self.process_next_save()
        
        def process_next_save(self, force=False):
            force = self.overwrite_all or force
            
            if not self.processing:
                return
            
            
            if self.processed >= len(self.saves_to_process):
                
                if self.mode == "MOVE":
                    
                    self.cleanup_thread = threading.Thread(target=self.process_cleanup)
                    self.cleanup_thread.daemon = True
                    self.cleanup_thread.start()
                else:
                    self.process_done()
                
                return
            
            save = self.saves_to_process[self.processed]
            
            
            if self.destination_instance.location.has_save(save, check_inactive=True) and not force:
                if self.skip_all:
                    self.skipped.append(save)
                    self.process_continue()
                    return
                
                renpy.show_screen("JK_MoveCopySavesOverwriteConfirm", save=save, view_model=self)
                time.sleep(0.1)
                renpy.restart_interaction()
                return
            
            
            self.save_thread = threading.Thread(target=self.copy_save_and_continue, args=(save,))
            self.save_thread.daemon = True
            self.save_thread.start()
        
        def copy_save_and_continue(self, save):
            try:
                
                self.source_instance.location.copy_save_into_other_multilocation(save, self.destination_instance.location, scan=False)
                
                self.process_continue()
            except Exception as e:
                print(e)
                self.error = "Ocorreu um erro ao copiar o salvamento “" + save + "\":\n{color=[JK.Colors.error]}" + str(e) + "{/color}"
                renpy.restart_interaction()
                self.process_stop()
        
        def process_continue(self):
            
            self.processed += 1
            renpy.restart_interaction()
            
            
            time.sleep(0.05)
            
            
            self.process_next_save()
        
        def process_skip_current_save(self, apply_to_all=False):
            self.skip_all = apply_to_all
            
            if apply_to_all:
                self.skipped.append(self.saves_to_process[self.processed])
                
                self.skip_conflicts_thread = threading.Thread(target=self.process_continue)
                self.skip_conflicts_thread.daemon = True
                self.skip_conflicts_thread.start()
                
                return
            
            self.process_continue()
        
        def process_overwrite_current_save(self, apply_to_all=False):
            self.overwrite_all = apply_to_all
            
            self.process_next_save(force=True)
            renpy.restart_interaction()
        
        def process_overwrite_all_saves(self):
            
            self.overwrite_all = True
            self.process_next_save()
            renpy.restart_interaction()
        
        def process_stop(self, success=False):
            self.success = success
            self.processed = 0
            self.processing = False
            
            renpy.restart_interaction()
            
            if self.save_thread and self.save_thread.is_alive():
                self.save_thread.join()  
            
            if self.cleanup_thread and self.cleanup_thread.is_alive():
                self.cleanup_thread.join()  
            
            if self.skip_conflicts_thread and self.skip_conflicts_thread.is_alive():
                self.skip_conflicts_thread.join()  
            
            SaveSystem.multilocation.scan()
        
        def process_cleanup(self):
            self.stage = "CLEANUP"
            self.processed = 0
            
            renpy.restart_interaction()
            time.sleep(0.05)
            
            save = None
            try:
                for save in self.saves_to_process:
                    if not self.processing:
                        return
                    
                    if not save in self.skipped:
                        self.source_instance.location.unlink_save(save, scan=False)
                    
                    self.processed += 1
                    
                    
                    time.sleep(0.05)
                    renpy.restart_interaction()
                
                self.process_done()
            except Exception as e:
                print(e)
                self.error = "Ocorreu um erro ao limpar o salvamento “" + save + "\":\n{color=[JK.Colors.error]}" + str(e) + "{/color}"
                self.process_stop()
        
        def process_done(self):
            self.success = True
            self.processing = False
            
            SaveSystem.multilocation.scan()
            renpy.restart_interaction()
        
        class StartProcessAction(renpy.ui.Action):
            def __init__(self, view_model, saves, mode="COPY"):
                self.view_model = view_model
                self.saves = saves
                self.mode = mode
            
            def __call__(self):
                self.view_model.process_saves(self.saves, mode=self.mode)
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
