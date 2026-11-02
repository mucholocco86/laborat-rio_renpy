init python in JK:
    _constant = True

    import threading
    import time
    import zipfile
    import os

    class ChoicesTimelineViewModel(x52NonPicklable):
        def __init__(self, playthrough):
            self.playthrough = playthrough
            self.timeline = []
            self.loading = True
            self.loaded = 0
            self.to_load = 0
            self.error = None
            self.slots = []
            
            self.load_thread = None  
            
            self.load_timeline()
        
        def load_timeline(self):
            self.loading = True
            self.loaded = 0
            
            instance = SaveSystem.get_playthrough_save_instance(self.playthrough.id)
            instance.location.scan()
            
            self.slots = Utils.get_sorted_saves()
            self.to_load = len(self.slots)
            
            renpy.restart_interaction()
            
            
            self.load_thread = threading.Thread(target=self.process_loading_start, args=(instance,))
            self.load_thread.daemon = True
            self.load_thread.start()
        
        def process_loading_start(self, instance):
            i = 0
            renpy.restart_interaction()
            
            time.sleep(0.1)
            
            for slot in self.slots:
                json = instance.location.json(slot)
                
                self.timeline.append((i, json.get("_JK_choice", None), slot))
                
                self.loaded += 1
                renpy.restart_interaction()
                
                i += 1
                
                time.sleep(0.005)
            
            self.loading = False
            renpy.restart_interaction()
        
        class ExportTimelineToFileAction(renpy.ui.Action):
            def __init__(self, view_model):
                self.timeline = view_model.timeline
                self.playthrough = view_model.playthrough
            
            def __call__(self):
                import os
                
                filename = self.playthrough.name + " timeline.txt"
                dirPath = os.path.normpath(os.path.join(os.path.dirname(os.path.realpath(__file__)), ".."))
                path = os.path.normpath(os.path.join(dirPath, filename))
                
                with open(path, 'w') as f:
                    for item in self.timeline:
                        f.write( str(item[0] + 1) + ". " + "    (" + item[2] + ")     " + self._m1_ChoicesTimelineViewModel__replace_tags(item[1] or "-") + "\n")
                
                showConfirm(
                    title="Linha do tempo exportada para os arquivos do jogo",
                    message="O arquivo está em " + path,
                    yes=OpenDirectoryAction(path=dirPath),
                    yes_text="Abrir local",
                    yes_icon='\ue2c8',
                    no_text="Fechar",
                    no_icon=None
                )
            
            def _m1_ChoicesTimelineViewModel__replace_tags(self, text):
                
                pattern = r'\{(.*?)\}(.*?)\{\/(.*?)\}'
                
                result = re.sub(pattern, r'\2', text)
                
                return result.replace('[[', '[')
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
