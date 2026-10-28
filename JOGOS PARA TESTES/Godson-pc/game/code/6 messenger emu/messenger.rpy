








init python:

    if persistent.theme is None:
        persistent.theme = [1.0, 1.0, 1.0]

    display_aspect_ratio = 16.0 / 9.0
    yadj = ui.adjustment()

    messages = []

    message_time = False
    in_history = True
    choice_number = True
    click_to_continue = True
    under_messenger = True
    time_to_send_pm = 2.0
    time_to_send_am = 2.0

    interlocutor_name = "sDextra"
    interlocutor_online = True
    interlocutor_typing = True
    interlocutor_extra_time = 1
    interlocutor_typing_speed = 0.1
    interlocutor_typing_show = False
    interlocutor_sends = False

    groupchat = False
    groupchat_enable = False
    groupchat_who_typing = False
    active_groupchat = False

    audio_path = 'sfx/'
    audio_extension = '.mp3'

    def show_messenger():
        _window_hide()
        renpy.show_screen('messenger')
        renpy.pause(1.0, hard=True)
    def hide_messenger():
        renpy.hide_screen('messenger')
        renpy.pause(1.0, hard=True)
        _window_show()



    class GroupChat():
        def __init__(self, name='Chat Name', avatar=False):
            self.name = name
            self.avatar = avatar if avatar else 'images/messenger/av/'+name.lower().replace(' ', '_')+'.png'
            self.members = 0
            self.list = []
        def add(self, interlocutor):
            self.list.append(interlocutor)
            self.members += 1
        def remove(self, name):
            for interlocutor in self.list:
                if interlocutor.name == name:
                    self.list.remove(interlocutor)
                    self.members -= 1
                    return
        def get_interlocutor(self, ID):
            for interlocutor in self.list:
                if interlocutor.id == ID:
                    return interlocutor
            return False


    class Interlocutor():
        def __init__(self, ID=1, name='Name', color='#fff', avatar=False):
            self.id = ID
            self.name = name
            self.color = color
            self.avatar = avatar if avatar else 'images/messenger/groupchat/'+name.lower().replace(' ', '_')+'.png'
        def set_avatar(self, new_avatar):
            self.avatar = new_avatar
        def set_name(self, new_name):
            self.name = new_name

    from mutagen.mp3 import MP3
    class Audio():
        def __init__(self, name, bar):
            self.file_name = name
            self.name = audio_path + self.file_name + audio_extension
            self.length = self.get_audio_length(self.name)
            self.duration = self.get_duration(self.length)
            self.bar = renpy.random.randint(1,9) if not bar else bar
        
        
        def get_audio_length(self, name):
            file = renpy.loader.transfn(name)
            audio = MP3(file)
            length = int(round(audio.info.length, 0))
            return length
        def play(self):
            renpy.play(self.name, channel='sound')
        def bar_idle(self):
            return 'images/messenger/audio/bar_'+str(self.bar)+'.png'
        def bar_hover(self):
            return color_brightness('images/messenger/audio/bar_'+str(self.bar)+'.png')
        
        def get_duration(self, d):
            m = d // 60
            m = '0'+str(m) if m < 10 else m
            s = d % 60
            s = '0'+str(s) if s < 10 and s != 0 else str(s)+'0' if s == 0 else s
            return "%s:%s"%(m,s)

    class Picture():
        def __init__(self, name, x, y):
            self.name = str(name)
            self.x = x
            self.y = int(x/display_aspect_ratio) if not y else y
        
        def open_fullpic(self):
            renpy.show_screen('sc_fullpic', pic=self.name)

    from datetime import datetime
    class Message():
        def __init__(self, what, who, choices, audio, audio_bar, pic, pic_x, pic_y, name_input, time):
            self.what = what
            self.who = who
            self.time_list = time
            self.choices = choices
            self.input = name_input
            self.instantly = True if name_input else False
            self.position = self.find_position(who)
            self.pic = Picture(pic, pic_x, pic_y) if pic else False
            self.audio = Audio(audio, audio_bar) if audio else False
            self.time = self.format_time(time) if type(message_time) != bool else self.get_current_time() if time else False
        
        def find_position(self, who):
            position = 0.0 if who else .99
            return position
        
        
        def get_current_time(self):
            now = datetime.now()
            time = datetime.strftime(now, "%H:%M")
            return time
        
        
        def format_time(self, time):
            h, m = time
            m = '0'+str(m) if m < 10 and m != 0 else str(m)+'0' if m == 0 else m
            h = '0'+str(h) if h < 10 and h != 0 else str(h)+'0' if h == 0 else h
            return "%s:%s"%(h,m)

    def down():
        store.yadj.value = 9999*9999


    def msg(what, who=0, name_input=False, choices=False, pic=False, pic_x=360, pic_y=False, audio=False, audio_bar=0, status=False):
        if name_input:
            skip_stop()
        
        if status:
            store.interlocutor_online = True if status == 'online' else interlocutor_online
        
        if who and what and interlocutor_typing:
            store.groupchat_who_typing = who
            store.interlocutor_typing_show = True
            renpy.pause(interlocutor_extra_time, hard=True)
            speed = len(what) * interlocutor_typing_speed
            renpy.pause(speed, hard=True)
            store.interlocutor_typing_show = False
            store.groupchat_who_typing = False
        
        if pic or audio:
            sends = 'status_picture' if pic else 'status_audio'
            time = time_to_send_pm if pic else time_to_send_am
            if who:
                store.groupchat_who_typing = who
                store.interlocutor_sends = sends
                renpy.pause(time, hard=True)
                store.interlocutor_sends = False
                store.groupchat_who_typing = False
            else:
                renpy.pause(time, hard=True)
        
        time_update()
        store.messages.append(Message(what, who, choices, audio, audio_bar, pic, pic_x, pic_y, name_input, message_time))
        store.yadj.value = 9999*9999
        
        if status:
            store.interlocutor_online = False if status == 'offline' else interlocutor_online
        if in_history:
            add_history(who, what)
        if who:
            renpy.play(store.audio_path+'new_message'+store.audio_extension, 'audio')
        
        renpy.restart_interaction()
        if not click_to_continue:
                renpy.pause(1.0, hard=True)
        
        else:
            renpy.pause()
        
        if choices:
            freeze()
        if not typewriter and name_input:
            freeze()


    def switch_dialogue(name='sDextra', dialogue=store.messages):
        store.interlocutor_name = name
        store.messages = dialogue

    def get_previous_msg(all_msg, message):
        i = all_msg.index(message)+1
        if i >= 0 and i <= len(all_msg)-1:
            return all_msg[i]
        return False

    def find(what):
        temp = []
        if what == "":
            return temp
        for message in messages:
            
            if message.what:
                if what.lower() in message.what.lower():
                    temp.append(message)
            else:
                
                if what == '#pic':
                    if message.pic:
                        temp.append(message)
                
                elif what == '#audio':
                    if message.audio:
                        temp.append(message)
        return temp

    input_find = ""
    def find_change_func(value):
        store.input_find = value
        store.yadj.value = 0
        renpy.restart_interaction()
    def find_reset():
        store.input_find = ""
        store.yadj.value = 9999*9999

    input_message = ""
    def input_change_func(value):
        store.input_message = value
        renpy.restart_interaction()


    def add_history(who, what):
        if groupchat_enable and active_groupchat:
            who = active_groupchat.get_interlocutor(who).name if who != 0 else store.name
        else:
            who = store.interlocutor_name if who != 0 else store.name
        if what:
            store.narrator.add_history(kind='adv', who=who, what=what)


    def time_update(m=1):
        if type(message_time) != bool:
            hours, minutes = message_time
            if minutes + m >= 60:
                hours += 1
                if hours >= 24:
                    hours = 0
                minutes += m-60
            else:
                minutes += m
            store.message_time = [hours, minutes]


    def del_last_msg():
        if len(store.messages) > 0:
            del store.messages[-1]

    def del_previous_msg():
        del store.messages[:-1]

    def del_all_msg():
        store.messages = []

    def die_is_cast(lbl):
        unfreeze()
        del_last_msg()
        renpy.jump(lbl)

    def online():
        store.interlocutor_online = True

    def offline():
        store.interlocutor_online = False

    def freeze():
        skip_stop()
        renpy.pause(9999, hard=True)

    def unfreeze():
        store._skipping = True

    def skip_stop():
        renpy.config.skipping = False
        store._skipping = False

    def set_name(message, name):
        store.name = name
        message.what = name
        message.input = False
        unfreeze()
        renpy.restart_interaction()
    SetName = renpy.curry(set_name)



    def time_tag(tag, argument, contents):
        size = 18
        color = store.style_gray
        return [ (renpy.TEXT_TAG, u"size={}".format(size)), (renpy.TEXT_TAG, u"color={}".format(color)),
        ] + contents + [
            (renpy.TEXT_TAG, u"/size"), (renpy.TEXT_TAG, u"/color"), ]
    config.custom_text_tags["t"] = time_tag







screen messenger():
    $ renpy.block_rollback()
    if under_messenger:
        add '#00000090' at blackout
    default find_enable = False

    frame background None xysize (600,975) at move_messenger:

        if groupchat_enable and active_groupchat:
            add active_groupchat.avatar pos (67,25)

        else:
            add 'images/messenger/av/'+interlocutor_name.lower().replace(' ', '_')+'.png' pos (67,25)
        add 'messenger_hud' pos (-6,-6)
        add 'messenger_back' pos (-6,-6)
        frame background None xysize (560, 810) align (0.5,0.58):
            has viewport id 'vp_msg' mousewheel True yadjustment yadj
            vbox spacing 15 xsize 550 xalign 0.4 box_reverse True:
                $ all_messages = find(input_find) if find_enable else messages[::-1]
                for message in all_messages:
                    $ you = not message.who
                    $ box = 'box_one' if you else 'box_two'
                    $ box_hover = 'hover_box' if you else 'hover_box_two'
                    $ previous_message = get_previous_msg(all_messages, message)
                    $ interlocutor = active_groupchat.get_interlocutor(message.who) if groupchat_enable and not you else False
                    if interlocutor and previous_message:
                        $ interlocutor = False if previous_message.who == interlocutor.id else interlocutor
                    $ avatar_xoffset = not interlocutor and groupchat_enable
                    if message.audio:
                        default played = False
                        default audio_sec = 0
                        $ playing = renpy.music.get_playing(channel='sound')
                        $ current_audio = audio_sec if message.audio.name == playing else 0
                        $ now_play = message.audio.name == playing
                        $ audio_idle = 'stop_idle' if now_play else 'play_idle'
                        $ audio_hover = 'stop_hover' if now_play else 'play_hover'
                        $ xoffset = 1.08 if you and played and now_play else 0
                        hbox spacing 5 xalign message.position:
                            if interlocutor:
                                add interlocutor.avatar size 64,64 ypos 10
                            elif avatar_xoffset:
                                add 'empty' size 64,64
                            $ ysize = 130 if interlocutor else 95
                            frame background Frame(box, 25, 25) xalign message.position xysize 360,ysize:
                                has vbox spacing -30
                                $ gc = '{color=%s}%s\n{/color}'%(interlocutor.color, interlocutor.name) if interlocutor else False
                                if gc:
                                    text gc style 'txt_base' xanchor 0.0 xpos 14 ypos 45
                                hbox spacing -250 xalign message.position-xoffset:
                                    hbox spacing -50:
                                        button xysize 343,87 background audio_idle hover_background audio_hover action If (now_play, [Stop('sound')], [SetScreenVariable('played', True), SetScreenVariable('audio_sec', 0), Function(message.audio.play)]):
                                            text "{k=1.5}%s{/k}"%(message.audio.duration) style 'txt_base' align .26,.9 xanchor 0.0 size 22 color style_gray
                                        if message_time:
                                            text "{t}%s{/t}"%(message.time) style 'txt_time'
                                    if played and now_play:
                                        timer 0.05 repeat True action SetScreenVariable('audio_sec', audio_sec+0.05), If(audio_sec>=message.audio.length, [SetScreenVariable('audio_sec', 0), SetScreenVariable('played', False)])
                                    $ bar_xoffset = 140 if played and now_play else 0
                                    bar value StaticValue(current_audio, message.audio.length) yalign .25 xpos bar_xoffset maximum (241, 29) thumb None left_bar message.audio.bar_hover() right_bar message.audio.bar_idle()
                    elif message.pic:
                        hbox spacing 5 xalign message.position:
                            if interlocutor:
                                add interlocutor.avatar size 64,64 ypos 10
                            elif avatar_xoffset:
                                add 'empty' size 64,64
                            hbox spacing -60 xalign message.position:
                                $ gc = '{color=%s}%s\n{/color}'%(interlocutor.color, interlocutor.name) if interlocutor else False
                                $ bottom = 35 if message_time else 20
                                $ top = 50 if interlocutor else 20
                                button xalign message.position xpadding 0 top_padding top bottom_padding bottom background Frame(box, 25, 25) hover_background Frame(box_hover, 25,25) action Function(message.pic.open_fullpic):
                                    add 'images/messenger/pic/'+message.pic.name+'.jpg' align .5,.5 size message.pic.x, message.pic.y
                                if message_time:
                                    text "{t}%s{/t}"%(message.time) style 'txt_time'
                                if gc:
                                    text gc style 'txt_base' xanchor 0.0 xpos -265 ypos 45

                    elif message.choices:
                        frame xalign message.position xpadding 20 ypadding 10 background Frame(box, 25, 25):
                            has vbox
                            $ sort = sorted(message.choices.items(), key=lambda x: x)
                            for k, v in sort:
                                $ k = k+1
                                $ txt = "%s"%(v.get('name', 'choice %s'%(k) ))
                                $ lbl = v.get('jump', 'start')
                                $ t = "%s. %s"%(k, txt) if choice_number else "%s"%(txt)
                                textbutton t hover_background '#22442D' action Function(die_is_cast, lbl):
                                    text_size 28 text_font style_font text_xalign 1.0 text_color '#fff'
                                if choice_number:
                                    key str(k) action Function(die_is_cast, lbl)
                    elif message.input:
                        hbox spacing 5 xalign message.position:
                            hbox spacing -60 xalign message.position:
                                frame xalign message.position xmaximum 500 xpadding 20 top_padding 15 bottom_padding bottom background Frame(box, 25, 25):
                                    input changed input_change_func length 20 style 'txt_base' xalign 1.0
                                if message_time:
                                    text "{t}%s{/t}"%(hm) style 'txt_time'
                                key 'K_RETURN' action SetName(message, input_message), If(not typewriter, Return())
                    else:
                        $ hm = message.time
                        $ txt = message.what
                        $ bottom = 30 if message_time else 15
                        $ gc = '{color=%s}%s\n{/color}'%(interlocutor.color, interlocutor.name) if interlocutor else ''
                        hbox spacing 5 xalign message.position:
                            if interlocutor:
                                add interlocutor.avatar size 64,64 ypos 10
                            elif avatar_xoffset:
                                add 'empty' size 64,64
                            hbox spacing -60 xalign message.position:
                                button xalign message.position xmaximum 500 xpadding 20 top_padding 15 bottom_padding bottom background Frame(box, 25, 25):
                                    text "%s%s"%(gc, txt) style 'txt_base'
                                if message_time:
                                    text "{t}%s{/t}"%(hm) style 'txt_time'
                    timer 0.001 action Function(down)

        if groupchat_enable and active_groupchat:
            $ status = 'status_typing_groupchat' if interlocutor_typing_show else Text('%s members'%(active_groupchat.members), color=style_gray, style='txt_status')
            if status:
                $ status = 'status_picture_groupchat' if interlocutor_sends == 'status_picture' else 'status_audio_groupchat' if interlocutor_sends == 'status_audio' else status
            text "%s"%(active_groupchat.name) style 'txt_base' size 32 xalign 0.25 xanchor 0.0 yalign 0.025
            add status align 0.25, 0.065 xanchor 0.0

        else:
            $ status = 'status_typing' if interlocutor_typing_show else 'status_online' if interlocutor_online else 'status_offline'
            $ status = interlocutor_sends if interlocutor_sends else status
            text "%s"%(interlocutor_name) style 'txt_base' color interlocutor_name_color size 32 xalign 0.25 xanchor 0.0 yalign 0.025
            add status align 0.25, 0.065 xanchor 0.0


        vbar value YScrollValue('vp_msg') style 'bar_vert'





screen sc_theme():
    modal True
    frame xysize (300,500) align .83,.5:
        label 'COLOR THEME' align .5,.03 text_size 30
        vbox align .5,.9:
            textbutton 'default' action Function(set_color_theme, 1.0,1.0,1.0), Hide('sc_theme')
            textbutton 'dark' action Function(set_color_theme, .5,.5,.5), Hide('sc_theme')
            textbutton 'light' action Function(set_color_theme, 1.5,1.5,1.5), Hide('sc_theme')
            textbutton 'red' action Function(set_color_theme, 1.5,.1,.1), Hide('sc_theme')
            textbutton 'green' action Function(set_color_theme, .5,1,.5), Hide('sc_theme')
            textbutton 'blue' action Function(set_color_theme, .7,.7,1), Hide('sc_theme')
            textbutton 'cyan' action Function(set_color_theme, .7,1.0,.7), Hide('sc_theme')
            null height 20
            textbutton 'close' action Hide('sc_theme')



screen sc_fullpic(pic=False):
    modal True zorder 10
    add '#00000090' at blackout
    add 'images/messenger/pic/'+pic+'.jpg' at move_pic
    button background None action Hide('sc_fullpic')
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
