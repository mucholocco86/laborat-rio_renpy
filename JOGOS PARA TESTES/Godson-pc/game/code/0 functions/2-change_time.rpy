init python:





    def change_time():
        
        if current_time == "day":
            
            store.current_time = "night"
        
        elif current_time == "night":
            
            store.current_day += 1
            
            store.current_time = "day"
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
