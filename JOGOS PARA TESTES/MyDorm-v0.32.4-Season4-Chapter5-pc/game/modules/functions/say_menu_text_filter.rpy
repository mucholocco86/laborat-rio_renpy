init 100 python:
    original_say_menu_text_filter = config.say_menu_text_filter
    def new_say_menu_text_filter (searchString):
# What to do with thoughts
        isThought = searchString.startswith ("{i}(") and searchString.endswith ("){/i}")
        #if isThought: # remove thought indicator
            #searchString = searchString [0:3] + searchString [4:-5] + searchString [-4:]
        if original_say_menu_text_filter:
            searchString = original_say_menu_text_filter (searchString)
        return searchString
    config.say_menu_text_filter = new_say_menu_text_filter
