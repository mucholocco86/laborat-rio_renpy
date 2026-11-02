init python in JK:
    _constant = True

    import time

    class MemoriesClass(x52NonPicklable):
        def __init__(self):
            self.memoryInProgress = False
            
            self.restoreOldLog = None
            self.restoreStoreBackup = None
            self.restoreContext = None
            self._save_instance = None
        
        @property
        def saveInstance(self):
            self._save_instance = self._save_instance or SaveSystem.get_or_create_playthrough_save_instance_by_id(2)
            return self._save_instance
        
        def getMemories(self):
            save_location = self.saveInstance.location
            save_location.activate_locations()
            save_location.scan()
            memories = save_location.list()
            save_location.deactivate_locations()
            return memories
        
        def callCustomReplay(self, slotname):
            self.saveInstance.location.activate_locations()
            
            
            
            
            
            
            
            
            
            
            
            
            self.restoreContext = renpy.execution.Context(True)
            renpy.game.contexts.append(self.restoreContext) 
            
            
            
            
            
            
            Memories.memoryInProgress = True
            
            roots, log = renpy.loadsave.loads(self.saveInstance.location.load(slotname))
            log.unfreeze(roots)
            
            
            
            self.saveInstance.location.deactivate_locations()
        
        
        
        def exitMemoryAndTryRestoryOldGame(self):
            
            
            if self.restoreContext != None: 
                self.restoreContext.pop_all_dynamic()
                
                renpy.game.contexts.pop()
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            self.memoryInProgress = False
            self.restoreOldLog = None
            self.restoreStoreBackup = None
            self.restoreContext = None
        
        @staticmethod
        def createSaveRecord(extra_info=None, log=None):
            log = log or renpy.game.log
            roots = log.freeze(None)
            
            extra_info = extra_info or ""
            
            if renpy.config.save_dump:
                renpy.loadsave.save_dump(roots, log)
            
            logf = io.BytesIO()
            
            try:
                renpy.loadsave.dump((roots, log), logf)
            except:
                t, e, tb = sys.exc_info()
                
                try:
                    bad = renpy.loadsave.find_bad_reduction(roots, log)
                except:
                    print("Falha ao salvar a memória:\n", t, e, tb)
                    renpy.notify("Falha ao salvar a memória. Consulte log.txt para mais informações.")
                    return
                
                if bad is None:
                    print("Falha ao salvar a memória:\n", t, e, tb)
                    renpy.notify("Falha ao salvar a memória. Consulte log.txt para mais informações.")
                    return
                
                if e.args:
                    e.args = (e.args[0] + ' (perhaps {})'.format(bad),) + e.args[1:]
                
                print("Falha ao salvar a memória:\n", t, e, tb)
                renpy.notify("Falha ao salvar a memória. Consulte log.txt para mais informações.")
                return
            
            json = { "_save_name" : extra_info, "_renpy_version" : list(renpy.version_tuple), "_version" : renpy.config.version }
            
            for i in renpy.config.save_json_callbacks:
                i(json)
            
            json = json_dumps(json)
            
            save_record = renpy.loadsave.SaveRecord(None, extra_info, json, logf.getvalue())
            save_record.screenshot = renpy.game.interface.get_screenshot()
            
            return save_record
        
        class OpenSaveMemory(renpy.ui.Action):
            def __call__(self):
                renpy.take_screenshot()
                renpy.show_screen("JK_SaveMemory")
                renpy.restart_interaction()
        
        class CreateMemory(renpy.ui.Action):
            def __init__(self, name):
                self.name = name
            
            def __call__(self):
                save_location = Memories.saveInstance.location
                save_location.activate_locations()
                saveRecord = MemoriesClass.createSaveRecord(extra_info=self.name)
                
                for location in save_location.active_locations():
                    location.save(str(time.time())[:-3], saveRecord)
                
                save_location.scan()
                save_location.deactivate_locations()
                
                renpy.restart_interaction()
        
        class LoadMemoryWithConfirm(renpy.ui.Action):
            def __init__(self, slotname):
                self.slotname = slotname
            
            def __call__(self):
                if renpy.context()._main_menu:
                    Memories.callCustomReplay(self.slotname)
                else:
                    showConfirm(
                        title="Carregar memória",
                        message="Abrir uma memória encerrará a sessão atual e você perderá o progresso não salvo.\nDeseja continuar?",
                        yes=Memories.LoadMemory(self.slotname),
                    )
                
                renpy.restart_interaction()
        
        class LoadMemory(renpy.ui.Action):
            def __init__(self, slotname):
                self.slotname = slotname
            
            def __call__(self):
                Memories.callCustomReplay(self.slotname)
                
                renpy.restart_interaction()
        
        class ExitMemory(renpy.ui.Action):
            def __call__(self):
                Memories.exitMemoryAndTryRestoryOldGame()
                
                renpy.restart_interaction()
        
        def GetScreenshot(self, slotname):
            saveInstance = Memories.saveInstance
            
            for location in saveInstance.location.locations:
                screenshot = location.screenshot(slotname)
                break
            
            if screenshot is not None:
                return screenshot
            
            return ImagePlaceholder(width=renpy.config.thumbnail_width, height=renpy.config.thumbnail_height)
        
        class DeleteMemory(renpy.ui.Action):
            def __init__(self, slotname):
                self.slotname = slotname
            
            def __call__(self):
                Memories.saveInstance.location.unlink_save(self.slotname)
                renpy.restart_interaction()
        
        class DeleteMemoryConfirm(renpy.ui.Action):
            def __init__(self, slotname):
                self.slotname = slotname
            
            def __call__(self):
                name = Memories.saveInstance.location.save_name(self.slotname) or self.slotname
                
                showConfirm(
                    title="Excluir memória \"{}\"".format(name),
                    message="Esta ação {u}{color=[JK.Colors.error]}é irreversível{/c}{/u}. Deseja continuar?",
                    yes=Memories.DeleteMemory(self.slotname),
                    yes_icon="\ue92b",
                    yes_color=Colors.error
                )
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
