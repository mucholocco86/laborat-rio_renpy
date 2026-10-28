init python:

    my_files = renpy.list_files()

    renpy.music.register_channel("menu_music", mixer='music')
    renpy.music.register_channel("other", mixer="other")
    my_audio = {}





init python:
    def update_audio_dictionary():
        for path_to_file in my_files:
            if path_to_file.startswith("music/"):
                split_file_path = path_to_file.split("/")
                try:
                    file_name_without_extension, file_extension = split_file_path[-1].split(".")
                except ValueError:
                    print(f"Cannot split: {path_to_file}")
                    continue
                dictionary_entry = {file_name_without_extension : path_to_file}
                my_audio.update(dictionary_entry)

    update_audio_dictionary()
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
