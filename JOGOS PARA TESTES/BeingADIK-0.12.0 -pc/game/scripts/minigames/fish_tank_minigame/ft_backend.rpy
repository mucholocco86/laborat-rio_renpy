init python:
    def ft_play_coin():
        renpy.play("sound_effects/coin.mp3","sfx1")
    def ft_play_click():
        renpy.play("sound_effects/season2/app_click.mp3","sfx1")
    def ft_play_bubbles():
        renpy.play("sound_effects/season2/hookah.mp3","sfx3")
    def ft_play_dead():
        renpy.play("sound_effects/season2/flush.mp3","sfx2")
    def ft_play_menu():
        renpy.play("sound_effects/menu.mp3","sfx1")
    def ft_play_heal():
        renpy.play("sound_effects/heal.mp3","sfx3")

init python:
    class ft_fish:
        def __init__(self, gender, health, sick):
            self.gender = gender
            self.health = health
            self.sick = sick

label ft_setup_round_label:

$ ft_get_new_fish()
$ ft_get_food_state()

$ ft_get_mature_fish()
$ ft_get_deaths()
$ ft_get_repro_rate()
$ ft_get_sickness()
$ ft_get_filth_rate()

if (len(ft_fish_list) - sum(1 for f in ft_fish_list if f.health == 0)) == 0:
    $ ft_failed = True
$ renpy.jump(jumpLabel)
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
