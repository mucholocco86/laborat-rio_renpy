


init python:
    import collections



    class Quest:
        def __init__(self, id, title, category,  state= "pending"):
            self.id = id
            self.title = title
            self.category = category
            self.state = state
        
        def __repr__(self):
            return "<{}>".format(self.title)






    class Manager:
        
        def __init__(self):
            self.quests_dict = collections.OrderedDict() 
            self.states = ["pending", "unlocked", "in progress", "completed", "done", "failed", "canceled"]
        
        
        
        
        
        def load(self, chapter):
            if type(chapter) is not tuple:
                print("Error: must be a tuple")
                renpy.quit()
            self.quests_dict.clear()
            for quest in chapter:
                if quest.category not in self.quests_dict:
                    self.quests_dict[quest.category] = collections.OrderedDict([(quest.id,quest)])
                else:
                    self.quests_dict[quest.category][quest.id] = quest
            self._reload_screen("diary")
            renpy.block_rollback()
            print(self.quests_dict)
        
        
        
        def free(self):
            self.quests_dict.clear()
            renpy.block_rollback()
        
        
        
        
        
        def _search(self, id, category = ""):
            if category == "":
                return self._searchID(id)
            return self.quests_dict[category][id]
        
        
        def _searchID(self, id):
            for k in self.quests_dict.keys():
                if id in self.quests_dict[k]:
                    return self.quests_dict[k][id]
        
        
        
        
        
        
        def exists(self, id, category = ""):
            if self._search(id, category):
                return True
            return False
        
        
        
        def is_in(self, id):
            for k in self.quests_dict.keys():
                if id in self.quests_dict[k]:
                    return k
        
        
        
        def is_state(self, id, state, category = ""):
            if self._search(id, category).state == state:
                return True
            return False
        
        
        def is_category_over(self, category):
            for v in self.quests_dict[category].values():
                if v.state != "done":
                    return False
            return True
        
        
        def is_chapter_over(self):
            for k in self.quests_dict.keys():
                if not self.is_category_over(k):
                    return False
            return True
        
        
        
        
        
        def check(self, id, state, category = ""):
            if state not in self.states:
                print("Error: this state doesn't exist ! Please check the documentation.")
                return
            if category == "" and state != "canceled":
                self._checkID(id, state)
                return
            if state == "canceled":
                self._remove_quest(id)
                return
            self._search(id, category).state = state
            print("{} {}".format(id ,self._search(id, category).state))
        
        
        
        def _checkID(self, id, state):
            self._searchID(id).state = state
        
        
        
        def update(self, id="", state="", unchanged = [], category=""):
            temp = False
            if isinstance(id, tuple):
                id1, id2 = id
            else:
                id1, id2 = id, id
                temp = True
            if isinstance(state, tuple):
                state1, state2 = state
            else:
                state1, state2 = state, state
            
            if category == "" and id != "":
                category = self._searchID(id2).category
            
            if id == "" and category != "":
                self._update_all_quests(state, unchanged, category)
                return
            
            for k,v, in self.quests_dict[category].items():
                if k == id1:
                    temp = True
                if k == id2:
                    v.state = state2
                    return
                if temp == True:
                    if v.state not in unchanged:
                        v.state = state1
        
        
        def _update_all_quests(self, state="", unchanged = [], category=""):
            for k,v, in self.quests_dict[category].items():
                if v.state not in unchanged:
                    v.state = state
        
        
        
        
        
        
        def add(self, quests):
            if type(quests) is list:
                self._add_multi(quests)
                return
            if self.exists(quests.id):
                print("Error: already in quests_dict")
                return
            if quests.category not in self.quests_dict:
                self.quests_dict[quests.category] = collections.OrderedDict([(quests.id,quests)])
            else:
                self.quests_dict[quests.category][quests.id] = quests
        
        
        def _add_multi(self, quest_list):
            for quest in quest_list:
                self.add(quest)
        
        
        def remove(self, category):
            if category not in self.quests_dict:
                return
            del self.quests_dict[category]
            self._reload_screen("diary")
        
        
        def _remove_quest(self, id, category = ""):
            if category == "":
                category = self.is_in(id)
            del self.quests_dict[category][id]
            if self.quests_dict[category] == {}:
                del self.quests_dict[category]
        
        
        
        
        def _reload_screen(self, screen_name):
            if renpy.get_screen(screen_name):
                renpy.hide_screen(screen_name)
                renpy.show_screen(screen_name)
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
