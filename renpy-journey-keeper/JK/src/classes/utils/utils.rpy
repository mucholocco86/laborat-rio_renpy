init -9999 python in JK:
    _constant = True

    import re
    import os
    import unicodedata
    import sys







    class x52NonPicklable(python_object):
        def __setstate__(self, d):
            pass
        def __getstate__(self):
            return {}
        def __getnewargs__(self):
            return ()
        def __iter__(self):
            return None
        def itervalues(self):
            return None

    class Utils(x52NonPicklable):
        @staticmethod
        def split_slotname(slotname):
            reg_page = "<page>"
            reg_name = "<name>"
            
            if hasattr(renpy.config, "file_slotname_callback") and renpy.config.file_slotname_callback and callable(renpy.config.file_slotname_callback):
                sample_slotname = renpy.config.file_slotname_callback(reg_page, reg_name)
            else:
                sample_slotname = reg_page + "-" + reg_name
            
            pattern = re.escape(sample_slotname)
            pattern = pattern.replace(reg_page, r"(\d+)")
            pattern = pattern.replace(reg_name, r"(\d+)")
            
            
            match = re.match(pattern, slotname)
            if match:
                page = match.group(1)
                slot = match.group(2)
                
                if page != None and slot != None and page.isdigit() and slot.isdigit():
                    return int(page), int(slot)
            
            try:
                page, slot = slotname.split('-')
                
                if page.isdigit() and slot.isdigit():
                    return int(page), int(slot)
                
                if Settings.debugEnabled:
                    print("Can't resolve slotname ", slotname)
                return 0, 0
            except:
                if Settings.debugEnabled:
                    print("Can't resolve slotname ", slotname)
                return 0, 0
        
        @staticmethod
        def get_sorted_saves():
            regexp = r'\d+' + '-' + r'\d+'
            return Utils.sort_saves(renpy.list_slots(regexp=regexp))
        
        @staticmethod
        def sort_saves(saves_list):
            return sorted(saves_list, key=Utils._m1_utils__custom_saves_sort)
        
        @staticmethod
        def _m1_utils__custom_saves_sort(slotname):
            value = str(slotname)  
            components = re.findall(r'\d+|\D+', value)  
            comparable = []
            for comp in components:
                
                if comp.isdigit():
                    comparable.append((False, int(comp)))  
                else:
                    comparable.append((True, comp))  
            
            return comparable
        
        @staticmethod
        def name_to_directory_name(title):
            
            replacements = {
                ':': '；',  
                '/': '／',  
                '\\': '／',  
                '<': '‹',   
                '>': '›',   
                '*': '＊',  
                '?': '？',  
                '"': '＂',  
                '|': 'ǀ'    
            }
            
            
            pattern = re.compile('|'.join(re.escape(char) for char in replacements.keys()))
            
            
            def replace_invalid_char(match):
                return replacements[match.group(0)]
            
            directory_name = pattern.sub(replace_invalid_char, title)
            
            
            max_length = 255  
            directory_name = directory_name[:max_length]
            
            
            
            return directory_name
        
        @staticmethod
        def get_slots_per_page():
            if Settings.customGridEnabled:
                return Settings.customGridX * Settings.customGridY
            
            if Utils.has_cols_and_rows_configuration():
                return renpy.store.gui.file_slot_cols * renpy.store.gui.file_slot_rows
            
            return 4
        
        @staticmethod
        def has_cols_and_rows_configuration():
            if Settings.customGridEnabled:
                return True
            
            return hasattr(renpy.store.gui, "file_slot_cols") and hasattr(renpy.store.gui, "file_slot_rows")
        
        @staticmethod
        def is_displaying_choices():
            try:
                current = renpy.game.context().current
                script = renpy.game.script.lookup(current)
                return isinstance(script, renpy.ast.Menu)
            except:
                return False
        
        @staticmethod
        def is_displaying_multiple_choices():
            try:
                current = renpy.game.context().current
                script = renpy.game.script.lookup(current)
                if isinstance(script, renpy.ast.Menu):
                    available_count = 0
                    for item in script.items:
                        if len(item) > 2 and item[2]:
                            if eval(item[1], renpy.store.__dict__):
                                available_count += 1
                            
                            if available_count > 1:
                                return True
                    
                    return False
            except:
                return False
        
        @staticmethod
        def is_displaying_choices_in_any_context():
            try:
                for context in renpy.game.contexts:
                    script = renpy.game.script.lookup(context.current)
                    if isinstance(script, renpy.ast.Menu):
                        return True
            except Exception as e:
                print(e)
            
            return False
        
        
        @staticmethod
        def escape_renpy_reserved_characters(text):
            result = []
            length = len(text)
            i = 0
            
            while i < length:
                char = text[i]
                
                if char == '[' and i < length - 1:
                    
                    result.append('[')
                    
                    
                    if text[i+1] == '[':
                        i += 1
                
                result.append(char)
                i += 1
            
            
            return ''.join(result)
        
        @staticmethod
        def get_screen_variable(variableName, dictionaryKey=None):
            cs = renpy.current_screen()
            
            if not cs or not variableName in cs.scope:
                return
            
            if(dictionaryKey):
                key = dictionaryKey if not callable(dictionaryKey) else dictionaryKey()
                return cs.scope[variableName][key]
            else:
                return cs.scope[variableName]
        
        @staticmethod
        def resize_dimensions_to_limits(original_size, desired_size):
            
            desired_width, desired_height = desired_size
            original_width, original_height = original_size
            
            
            width_scaling = float(desired_width) / float(original_width)
            height_scaling = float(desired_height) / float(original_height)
            
            
            scaling_factor = min(width_scaling, height_scaling)
            
            
            new_width = original_width * scaling_factor
            new_height = original_height * scaling_factor
            
            return int(new_width), int(new_height)
        
        @staticmethod
        def filter_timeline(timeline, search):
            if search is None or search == "":
                return timeline
            
            
            def normalize(text):
                if isinstance(text, str):
                    text = text.decode('utf-8') if sys.version_info[0] < 3 else text
                return unicodedata.normalize('NFD', text).encode('ascii', 'ignore').decode('utf-8')
            
            normalized_search = normalize(search).lower()
            
            filtered = []
            for entry in timeline:
                if not isinstance(entry, tuple) or len(entry) < 2:
                    continue  
                text = entry[1]
                if text is None:
                    continue  
                if normalized_search in normalize(text).lower():
                    filtered.append(entry)
            
            return filtered
        
        @staticmethod
        def is_save_load_screen():
            for screen in ["save", "load"] + Settings.saveScreenName + Settings.loadScreenName:
                if renpy.get_screen(screen) != None:
                    return True
            
            return False
        
        @staticmethod
        def add_key_underline(string, keybind):
            
            match = re.match(r".*_(.)$", keybind)
            if not match:
                return string
            
            key_char = match.group(1).lower()
            
            
            
            def replace_match(m):
                return "{u}" + m.group(0) + "{/u}"
            
            
            result = re.sub(re.escape(key_char), replace_match, string, count=1, flags=re.IGNORECASE)
            
            return result
        
        @staticmethod
        def list_save_directories():
            dir_names = set()
            directories = set()
            
            for location in renpy.loadsave.location.nativeLocations:
                for item_name in os.listdir(location.directory):
                    if item_name not in dir_names:
                        path = os.path.join(location.directory, item_name)
                        
                        if os.path.isdir(path):
                            directories.add((item_name, path))
                            dir_names.add(item_name)
            
            return directories
        
        @staticmethod
        def format_slotname(slotname):
            page, name = Utils.split_slotname(slotname)
            page = str(page)
            name = str(name)
            
            if hasattr(renpy.config, "file_slotname_callback") and renpy.config.file_slotname_callback is not None:
                return renpy.config.file_slotname_callback(page, name)
            else:
                return page + "-" + name
        
        @staticmethod
        def get_active_screens():
            screens = []
            for context in renpy.game.contexts:
                for layer in context.scene_lists.layers:
                    for sle in context.scene_lists.layers[layer]:
                        if sle and sle.name:
                            name = sle.name[0]
                            
                            
                            
                            
                            if not ("JK_" in name or "notify" == name or "URM_" in name) and renpy.get_screen(name):
                                screens.append(name)
            
            return screens
        
        @staticmethod
        def translate_markdown(text):
            if text is None:
                return None
            
            
            text = re.sub(r'\r\n', r'\n', text, flags=re.MULTILINE)
            
            text = re.sub(r'\*\*(.*?)\*\*', r'{b}\1{/b}', text)
            
            text = re.sub(r'\*(.*?)\*', r'{i}\1{/i}', text)
            
            text = re.sub(r'~~(.*?)~~', r'{s}\1{/s}', text)
            
            text = re.sub(r'^- (.*?)$', r'    - \1', text, flags=re.MULTILINE)
            
            text = re.sub(r'\[(.*?)\]\((.*?)\)', r'{a=\1}\2{/a}', text)
            
            text = re.sub(r'`(.*?)`', r'\1', text)
            
            text = re.sub(r'```(.*?)```', r'\1', text, flags=re.DOTALL)
            
            text = Utils.escape_renpy_reserved_characters(text)
            
            text = re.sub(r'^# (.*?)$', r'{color=[JK.Colors.theme]}{b}\1{/b}{/color}', text, flags=re.MULTILINE)
            text = re.sub(r'^## (.*?)$', r'{color=[JK.Colors.theme]}{i}\1{/i}{/color}', text, flags=re.MULTILINE)
            text = re.sub(r'^### (.*?)$', r'{color=[JK.Colors.theme]}\1{/color}', text, flags=re.MULTILINE)
            
            return text

    class OpenDirectoryAction(renpy.ui.Action):
        def __init__(self, path, cwd=None):
            self.path = path
            self.cwd = cwd
        
        def __call__(self):
            import os
            import platform
            import subprocess
            
            directory_path = os.path.join(self.cwd, self.path) if self.cwd else self.path
            
            
            directory_path = os.path.normpath(directory_path)
            
            if not os.path.exists(directory_path):
                print "Directory not found: {}".format(directory_path)
                return
            
            if not os.path.isdir(directory_path):
                print "The path is not a directory: {}".format(directory_path)
                return
            
            system = platform.system()
            
            try:
                if system == "Windows":
                    
                    subprocess.Popen(["explorer", directory_path])
                elif system == "Darwin":
                    
                    subprocess.Popen(["open", directory_path])
                elif system == "Linux":
                    
                    subprocess.Popen(["xdg-open", directory_path])
                elif system == "Android":
                    
                    subprocess.Popen(["am", "start", "-a", "android.intent.action.VIEW", "-d", "file://{}".format(directory_path)])
                else:
                    print "Unsupported OS: {}".format(system)
            except Exception as e:
                print "An error occurred: {}".format(e)











































    class SetKeyAction(renpy.ui.Action):
        def __init__(self, key, shift=False, ctrl=False, alt=False):
            self.key = key
            self.shift = shift
            self.ctrl = ctrl
            self.alt = alt
        
        def resolve_key(self):
            if self.key == None:
                return None
            
            parts = []
            
            if self.shift:
                if not "shift_" in self.key:
                    parts.append("shift")
            elif "shift_" in self.key:
                parts.append("shift")
            
            if self.ctrl:
                if not "ctrl_" in self.key:
                    parts.append("ctrl")
            elif "ctrl" in self.key:
                parts.append("ctrl")
            
            if self.alt:
                if not "alt_" in self.key:
                    parts.append("alt")
            elif "alt_" in self.key:
                parts.append("alt")
            
            parts.append(re.sub(r"(alt_)|(ctrl_)|(shift_)", "", self.key))
            
            return "_".join(parts)

    class OpenTooltipAction(renpy.ui.Action):
        def __init__(self, title=None, icon=None, message=None, interactive=False, side="top", pos=None):
            self.title = title
            self.icon = icon
            self.message = message
            self.interactive = interactive
            self.side = side
            self.pos = pos
        
        def __call__(self):
            if self.message:
                renpy.show_screen("JK_TooltipDialog", title=self.title, icon=self.icon, message=self.message, pos=self.pos, interactive=self.interactive, side=self.side)
                renpy.restart_interaction()

    class UpdateTooltipPositionAction(renpy.ui.Action):
        def __init__(self, side="top", distance=0, pos=None, allow_offscreen=False):
            self.side = side
            self.distance = distance
            self.pos = pos
            self.allow_offscreen = allow_offscreen
        
        def __call__(self):
            drag = renpy.display.screen.get_widget(None, "JK_TooltipDialog")
            window = renpy.display.screen.get_widget(None, "JK_TooltipDialog_Window")
            if not drag or not window:
                return
            
            mouse_pos = renpy.get_mouse_pos()
            pos = self.pos or mouse_pos
            draggable_pos = pos
            window_size = window.window_size 
            
            if self.side == "top":
                draggable_pos = (
                    pos[0] - window_size[0] / 2,
                    pos[1] - self.distance - window_size[1],
                )
            elif self.side == "bottom":
                draggable_pos = (
                    pos[0] - window_size[0] / 2,
                    pos[1] + self.distance,
                )
            elif self.side == "left":
                draggable_pos = (
                    pos[0] - self.distance - window_size[0],
                    pos[1] - window_size[1] / 2,
                )
            elif self.side == "right":
                draggable_pos = (
                    pos[0] + self.distance,
                    pos[1] - window_size[1] / 2,
                )
            
            if not self.allow_offscreen:
                new_x = max(draggable_pos[0], 0)
                new_x = min(new_x, int(renpy.config.screen_width - window_size[0]))
                new_y = max(draggable_pos[1], 0)
                new_y = min(new_y, int(renpy.config.screen_height - window_size[1]))
            
            drag.snap(int(new_x), int(new_y))

    class OpenGameDirectoryAction(renpy.ui.Action):
        def __call__(self):
            OpenDirectoryAction(path=renpy.config.gamedir)()

    def scaled(value, min_value=None):
        
        def adjust_number(value):
            rv = int(value * (renpy.config.screen_height / 1080.0)) + Settings.sizeAdjustment
            
            if min_value:
                return max(min_value, rv)
            
            return rv
        
        
        if isinstance(value, tuple):
            return tuple(adjust_number(v) for v in value)
        
        
        return adjust_number(value)
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
