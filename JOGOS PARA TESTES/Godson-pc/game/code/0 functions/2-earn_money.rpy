init python:




    def gain_coins(arg_amount):
        
        store.player_coins += arg_amount
        
        renpy.music.play(my_audio["gain coin"], channel='sound', loop=False)
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
