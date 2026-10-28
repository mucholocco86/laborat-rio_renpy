
init python:
    class Msg:
        def __init__(self, who, text, replies=None, condition=None, actions=None, picture=None):
            # Who writes the message
            # 2 possible values: "mc" or "npc"
            if who not in ["mc", "npc"]:
                renpy.error("Function <Msg.__init__>: The <who> argument must be 'mc' or 'npc' (Current value: {})".format(who))
            else:
                self.who = who

            #
            # Text of the message
            #
            # Special case: For the first message of chat ("0" key"), you can set an empty text.
            #               That means MC will initiate the chat and not the NPC.
            #
            self.text = text

            #
            # A list of possible replies to the current message
            #
            # When there is no replies, that means the chat will end here.
            #
            if replies is None:
                self.replies = []
            else:
                if isinstance(replies, list):
                    self.replies = replies
                else:
                    self.replies = [ replies ]

            #
            # A condition to be able to display the current message
            #
            # Must be a string that contains Python code. In the end, it must return True or False
            #
            # Example:
            # - Having enough lova points:  conditions="annie_points>5"
            # - A variable must be True: conditions="annie_date"
            # - A variable must be False: conditions="not annie_date"
            # - Multiple conditions: conditions="annie_points>5 and annie_date"
            #
            self.condition = condition

            #
            # A list of actions that will be executed when this message is selected
            # in the chat.
            # Each action must be string that will be executed as Python code
            #
            # Examples:
            #
            # 1/ Changing a variable
            #
            #    !!! IMPORTANT !!! Each variable name MUST be prefixed with "store."
            #                      These actiuons will be evaluated in a Python function.
            #                      By default, a Python function can't change global variables.
            #                      The "store" prefix will let the function know it is a global variable.
            #
            #    - Increasing a variable:  actions="store.annie_point+=1"
            #    - Setting a variable to True: actions="store.blackbra=True"
            #    - Changing multiple variables:  actions=[ "store.annie_point+=1", "store.blackbra=True" ]
            #
            # 2/ Executing a function
            #    - Trigger a notification:  actions="renpy.notify(\"Notification text\")"
            #
            if actions is None:
                self.actions = []
            else:
                if isinstance(actions, list):
                    self.actions = actions
                else:
                    self.actions = [ actions ]

            #
            # An image which will be embedded in the message
            # - Must be 1920x1080 max
            # - This image must stored somewhere in the "images" folder
            # - Just use the name of the image (without the extension)
            #   For example, if you want to use "images/03/b 17.jpg",
            #   write:   picture="b 17"
            #
            self.picture = picture

        def is_valid(self):
            if self.condition is None:
                return True
            else:
                return eval(self.condition)

    #
    # How to build a chat
    # ===================
    # A chat is a dictionary which contains:
    # - 1 background (an image 1920x1080) displayed under the chat
    #   (key: "background")
    # - 1 thumbnail of the NPC with whom MC chats (image 245x245)
    #   (key: "thumbnail")
    # - 1+ messages
    #   (key: Anything but there is one rule
    #         - The first message of a chat must have the "0" key
    #   )
    #

    # Most simple possible chat: A NPC send a message with no possible reply
    #
    # define test_chat = {
    #     "background" : "aaw 13",
    #     "thumbnail" : "chat_nova_1",
    #     "0" : Msg("npc", "That was kind of you! See you tomorrow Orion!"),
    #     }
    #
    # When you want to trigger this chat in a label:
    # call chat(test_chat)
    #
    # !!! For a more complex example, look at the "chat_test.rpy" !!!

    #
    # Makes the chat progress to the next message
    #
    def chat_next_step(step):
        current_step = step

        # Current Msg object
        msg = current_chat[step]

        #
        # Add the message to the chat history
        #
        store.chat_history.append(step)

        if len(msg.actions) > 0:
            #
            # Execute actions linked to the current message
            #
            for act in msg.actions:
                exec(act)

        store.chat_step = step


    # Who will write the next message?
    # => Can return:
    #    - mc
    #    - npc
    #    - end (end of the chat)
    def next_who():
        rep = current_chat[chat_step].replies
        if rep:
            return current_chat[rep[0]].who
        else:
            return "end"


    def phone_point(var, value=1):
        #renpy.play(audio.beat, channel="sound2")
        #renpy.show_screen("heartbeat")
        setattr(store, var, getattr(store, var) + value)


default chat_history = []
default current_chat = None
default chat_step = None
default chat_yadj = None


label chat(chat):
    $ current_chat = chat
    $ chat_history = []
    $ chat_step = None
    $ chat_yadj = ui.adjustment()

    $ chat_next_step("0")

    play sound notificationphone2

    show screen chat with dissolve

    jump chat_loop


label chat_loop:
    if next_who() == "mc":
        # Next MC will write a message

        # Player will pick an answer in the possible replies
        call screen chat_answers()

        # Scroll the chat history to the bottom
        $ chat_yadj.value = float('inf')

    elif next_who() == "npc":
        # Next the NPC will write a message

        # Display the "XXX is typing..." animation for 1.2 seconds
        show screen chat_is_typing()
        pause 0.7
        hide screen chat_is_typing

        play sound notificationphone

        # Select the first valid message from the list of NPC possible replies
        $ chat_next_step( [ rep for rep in current_chat[chat_step].replies if current_chat[rep].is_valid() ][0] )

        if next_who() == "npc":
            # Add a tempo between 2 NPc's messages
            # To leave a short pause between 2 "XXX is typing..."
            pause 0.5

        elif next_who() == "mc":
            # Add a tempo before displaying MC's possible answers
            # To let the NPC message animation to finish
            pause 0.5

    else:
        # The chat is over

        # Display the button to end the chat
        call screen chat_end()

        hide screen chat with dis08

        return

    jump chat_loop




transform phone_pic():
    on show:
        zoom 0.0
        linear 0.2 zoom 1.0

    on hide:
        zoom 1.0
        linear 0.1 zoom 0.0


#
# Show a picture in full screen when the player click on it in
# the chat history
#
screen show_pic(pic):
    modal True

    # In case the pic to display isn't in 1920x1080
    imagebutton:
        idle Null(width=1920, height=1080)
        action Hide("show_pic")

    frame:
        style "empty"
        align (0.5, 0.5)

        at phone_pic

        imagebutton:
            keysym "game_menu"
            idle pic
            action Hide("show_pic")


transform answers_dissolve:
    alpha 0.0
    linear 0.3 alpha 1.0


screen chat_answers():
    vbox:
        at answers_dissolve
        xpos 1200
        yalign 0.5
        spacing 15

        for key, msg in [ (key, current_chat[key]) for key in current_chat[chat_step].replies ]:
            if msg.is_valid():
                vbox:
                    button:
                        padding (0, 0, 0, 0)
                        action [ Function(chat_next_step, step=key), Return() ]

                        frame:
                            xsize 700
                            padding (25, 32, 25, 25)
                            background Frame("chat_mc_background",17,17,17,17)

                            vbox:
                                xalign 0.5

                                text _(msg.text):
                                    style "chat_button_text"
                                    xalign 0.5

                                if msg.picture is not None:
                                    #
                                    # Display a picture in the message
                                    #
                                    add Transform(msg.picture, zoom=0.2) xalign 0.5

                    add "chat_mc_background_tip" xalign 1.0


transform message_popup:
    alpha 0.0
    yoffset 50
    parallel:
        ease 0.5 alpha 1.0
    parallel:
        easein_back 0.5 yoffset 0


screen chat():
    style_prefix "chat"

    #
    # Background image fullscreen
    #
    add current_chat["background"]

    frame:
        style "empty"
        #
        # White transparent background under the messages
        #
        background Frame("chat_background_messages", 60, 60, 60, 60)
        xysize (1120, 930)
        pos (50, 85)

        viewport yadjustment chat_yadj:
            pos (60, 150)
            xsize 1000
            ymaximum 740
            mousewheel True
            draggable True

            vbox:
                xsize 1000
                spacing 10

                for msg in [ current_chat[key] for key in chat_history]:

                    if len(msg.text) > 0:
                        vbox:
                            at message_popup
                            if msg.who == "mc":
                                # MC's message are aligned on the right
                                xalign 1.0

                            frame:
                                yalign 0.5
                                padding (25, 32, 25, 25)
                                if msg.who == "npc":
                                    # White background for NPCs
                                    background Frame("chat_npc_background",17,17,17,17)
                                else:
                                    # Blue background fo MC
                                    background Frame("chat_mc_background",17,17,17,17)

                                vbox:
                                    xminimum 500
                                    xmaximum 707

                                    text msg.text

                                    if msg.picture is not None:
                                        #
                                        # Display a picture in the message
                                        #
                                        imagebutton:
                                            xalign 0.5
                                            idle Transform(msg.picture, zoom=0.2)
                                            hover Transform(msg.picture, zoom=0.2, matrixcolor=BrightnessMatrix(0.2))
                                            action Show("show_pic", pic=msg.picture)

                            if msg.who == "npc":
                                add "chat_npc_background_tip"
                            else:
                                add "chat_mc_background_tip" xalign 1.0


    #
    # NPC thumbnail in the top left corner
    #
    add current_chat["thumbnail"]


screen chat_is_typing():
    frame:
        style "empty"
        xsize 1030
        pos (85, 990)

        has hbox:
            xalign 0.5

        # \u25cf = unicode character "black circle"
        text "\u25cf " at delayed_blink(0.0, 0.8) style "chat_npc_is_typing_dot"
        text "\u25cf " at delayed_blink(0.2, 0.8) style "chat_npc_is_typing_dot"
        text "\u25cf " at delayed_blink(0.4, 0.8) style "chat_npc_is_typing_dot"
        text renpy.substitute(_("[npc_name!ti] is typing..."), scope={ "npc_name" : current_chat["npc"]}) style "chat_npc_is_typing"


screen chat_end():
    #
    # Exit button
    #
    textbutton _("Click to end the chat"):
        style "chat_exit_button"
        keysym "game_menu"
        anchor (0.5,0.5)
        pos (0.8, 0.85)
        action [ Return() ]


style chat_text:
    color "#000000"
    size 30
    xalign 0.5

style chat_button_text:
    font gui.text_font
    idle_color "#000000"
    hover_color "#ffffff"
    size 30

style chat_npc_is_typing_dot:
    yoffset -6
    color "#ffffff"
    size 26
    font "DejaVuSans.ttf"

style chat_npc_is_typing:
    color "#ffffff"
    size 31
    italic True

style chat_exit_button:
    align (0.8, 0.95)
    xanchor 0.5
    #hover_sound audio.neon

style chat_exit_button_text:
    size 50
    idle_color "#ffffff"
    hover_color "#ffffff"
    idle_outlines [ (11, "#0000"), (1, "#000000") ]
    hover_outlines [ #(11, "#00FFD21a"), # Glowing effect
                    #(10, "#05FFD41a"),
                    #(9, "#12FDD51a"),
                    #(8, "#28FDD91a"),
                    (7, "#41FCDD1a"),
                    (6, "#5BFCE11a"),
                    (5, "#77FBE733"),
                    (4, "#92FCEB66"),
                    (3, "#ABFBEF66"),
                    (2, "#c3fcf380"),
                    (1 ,"#ecfefb80"),
                ]


define luna_chat2 = {
    "background" : "dm 3",
    "thumbnail" : "chat_luna_1",
    "npc" : "Luna",
    "0" : Msg("npc", _("Are you there already?"), "1a"),
    "1a" : Msg("mc", _("Yep! I just got home!"), "1"),
    "1" : Msg("npc", _("Cool!"), "2"),
    "2" : Msg("npc", _("I was about to play some Eternum"), "22"),
    "22" : Msg("npc", _("I brought all the equipment with me"), ["33a", "33b"]),
    "33a" : Msg("mc", _("Cool"), "222"),
    "33b" : Msg("mc", _("Sounds awesome!\n   Have fun {image=images/MENUS/e_tongue.png} {image=images/MENUS/e_tongue.png}"), "3"),
    "222" : Msg("npc", _("Well, I don't wanna bother you too much"), "44"),
    "44" : Msg("npc", _("See you later!"), "40"),
    "3" : Msg("npc", _("I'm playing with Annie later!"), "5"),
    "5" : Msg("npc", _("Any server you think she'd like?"), ["2a", "2b", "2c"]),
    "2a" : Msg("mc", _("Something kinky!"), "6"),
    "2b" : Msg("mc", _("Anything with fights and lots of action!"), "7"),
    "2c" : Msg("mc", _("A fishing simulator!"), "8"),
    "6" : Msg("npc", _("Really? Okay {image=images/MENUS/e_wow.png}"), "222", actions="store.annielunaserver+=1"),
    "7" : Msg("npc", _("Ah! I know the perfect one!"), "222", actions="store.annielunaserver+=2"),
    "8" : Msg("npc", _("Really? Ok!"), "222", actions="store.annielunaserver+=3"),
    "40" : Msg("npc", _("Bye!")),
    }

define luna_chat3 = {
    "background" : "ft 49",
    "thumbnail" : "chat_luna_1",
    "npc" : "Luna",
    "0" : Msg("npc", _("Hi!"), "1"),
    "1" : Msg("npc", _("Are you asleep yet?"), ["1a", "1b"]),
    "1a" : Msg("mc", _("Without wishing you a good night? \n                           No chance"), "2"),
    "1b" : Msg("mc", _("I'm trying"), "3"),
    "2" : Msg("npc", _("Haha thank you"), "7", actions="phone_point('luna_points')"),
    "3" : Msg("npc", _("Oh! Sorry, I didn't want to bother you"), "4"),
    "4" : Msg("npc", _("Let's talk tomorrow"), "5"),
    "5" : Msg("npc", _("Good night!"), "6"),
    "6" : Msg("mc", _("Good night, Luna!")),
    "7" : Msg("npc", _("I just wanted to tell you"), "8", actions="store.goodnightluna=True"),
    "8" : Msg("npc", _("How much I liked"), "9"),
    "9" : Msg("npc", _("Loved"), "10"),
    "10" : Msg("npc", _("Being with you"), "111"),
    "111" : Msg("npc", _("Tonight"), "11"),
    "11" : Msg("mc", _("         Me too, Luna {image=images/MENUS/e_heart.png}\nTonight was amazing"), "12"),
    "12" : Msg("npc", _("OK! That was all, really!"), "133"),
    "133" : Msg("npc", _("I don't want to bother you more! Sorry!"), "13"),
    "13" : Msg("npc", _("Good night, [mc] {image=images/MENUS/e_heart.png}"), "14"),
    "14" : Msg("mc", _("Sweet dreams, Luna {image=images/MENUS/e_heart.png} {image=images/MENUS/e_heart.png}")),
    }


define annie_chat = {
    "background" : "dm 3",
    "thumbnail" : "chat_annie_1",
    "npc" : "Annie",
    "0" : Msg("npc", _("Sorry!"), "111"),
    "111" : Msg("npc", _("I've been shopping all day with Nancy and I had no signal!"), "1"),
    "1" : Msg("npc", _("Did you ask me if you looked stronger...?"), ["3a", "3b"]),
    "3a" : Msg("mc", _("Yes! I took this photo this morning at Luna's\n{size=10} "), "3", picture="dm 4b"),
    "3" : Msg("npc", _("{image=images/MENUS/e_wow.png}"), ["7", "77"]),
    "7" : Msg("npc", _("{image=images/MENUS/e_wow.png} {image=images/MENUS/e_wow.png}"), "8", condition="anniepath"),
    "77" : Msg("npc", _("[mc]! Don't send me this stuff!"), "7777"),
    "7777" : Msg("npc", _("Um you look the same as always I guess? idk"), "777b"),
    "777b" : Msg("mc", _("Really? I guess it was all in my head\n                      Sorry about that\n                         See you later!"), "6"),
    "8" : Msg("npc", _("{image=images/MENUS/e_wow.png} {image=images/MENUS/e_wow.png} {image=images/MENUS/e_wow.png} {image=images/MENUS/e_wow.png} {image=images/MENUS/e_wow.png} {image=images/MENUS/e_wow.png} {image=images/MENUS/e_wow.png} {image=images/MENUS/e_wow.png} {image=images/MENUS/e_wow.png} {image=images/MENUS/e_wow.png} {image=images/MENUS/e_wow.png} {image=images/MENUS/e_wow.png} {image=images/MENUS/e_wow.png}\n{image=images/MENUS/e_wow.png} {image=images/MENUS/e_wow.png} {image=images/MENUS/e_wow.png} {image=images/MENUS/e_wow.png} {image=images/MENUS/e_wow.png} {image=images/MENUS/e_wow.png} {image=images/MENUS/e_wow.png} {image=images/MENUS/e_wow.png} {image=images/MENUS/e_wow.png} {image=images/MENUS/e_wow.png} {image=images/MENUS/e_wow.png} {image=images/MENUS/e_wow.png} {image=images/MENUS/e_wow.png}\n{image=images/MENUS/e_wow.png} {image=images/MENUS/e_wow.png} {image=images/MENUS/e_wow.png} {image=images/MENUS/e_wow.png} {image=images/MENUS/e_wow.png} {image=images/MENUS/e_wow.png} {image=images/MENUS/e_wow.png} {image=images/MENUS/e_wow.png} {image=images/MENUS/e_wow.png} {image=images/MENUS/e_wow.png} {image=images/MENUS/e_wow.png} {image=images/MENUS/e_wow.png} {image=images/MENUS/e_wow.png}"), "9a"),
    "3b" : Msg("mc", _("  It's ok, no worries {image=images/MENUS/e_pray.png} {image=images/MENUS/e_pray.png}\nIt was just me being silly"), "4"),
    "4" : Msg("npc", _("Oh... ok"), "5"),
    "5" : Msg("npc", _("Let me know if I can be of any help {image=images/MENUS/e_blush.png}"), "4a"),
    "4a" : Msg("mc", _("Will do! TTYL!"), "6"),
    "6" : Msg("npc", _("Later! {image=images/MENUS/e_blush.png} {image=images/MENUS/e_blush.png} {image=images/MENUS/e_blush.png}"), actions="store.photoannie=False"),
    "9a" : Msg("mc", _("Annie?"), "9"),
    "9" : Msg("npc", _("Yeah!"), "10"),
    "10" : Msg("npc", _("WOW!"), "11"),
    "11" : Msg("npc", _("I mean, YEAH! You look great! Stronger than you were a few months ago! Definitely!"), ["12a", "12b"]),
    "12a" : Msg("mc", _("          Haha, if you say so\nThat was all lol, gotta go now"), "6"),
    "12b" : Msg("mc", _("Right? I thought so too\n      Glad you like it {image=images/MENUS/e_tongue.png}"), "12"),
    "12" : Msg("npc", _("Kredon makes everything grow faster!"), "13"),
    "13" : Msg("npc", _("Look at my hair! It's so long already!\n{size=10} "), ["13a", "13b", "13c"], picture="dm 4c"),
    "13a" : Msg("mc", _("Is that from now? Where are you?"), "17"),
    "13b" : Msg("mc", _("Wow! I love it  {image=images/MENUS/e_hearteyes.png}"), "22"),
    "13c" : Msg("mc", _("Yeah, it really grew a lot in such a short time"), "14"),
    "14" : Msg("npc", _("Right?? I'll let it grow until I have it as long as in Eternum!"), "15"),
    "15" : Msg("npc", _("But anyway, I should probably leave the fitting room already"), "16"),
    "16" : Msg("npc", _("Nancy's gonna wonder what's taking me so long {image=images/MENUS/e_blush2.png}"), "16a"),
    "16a" : Msg("mc", _("Sure! TTYL!"), "66"),
    "66" : Msg("npc", _("Later! {image=images/MENUS/e_blush.png} {image=images/MENUS/e_blush.png} {image=images/MENUS/e_blush.png}")),
    "17" : Msg("npc", _("At the mall!"), "181"),
    "181" : Msg("npc", _("Shopping with Nancy {image=images/MENUS/e_blush.png}"), "18"),
    "18" : Msg("npc", _("I was with her in a dressing room before. She has a spectacular body {image=images/MENUS/e_wow.png}"), ["18a", "18b"]),
    "18a" : Msg("mc", _("Oh, that's nice!\nI've gotta go now, but I'll see you and that new mane of yours later!  {image=images/MENUS/e_wink.png}"), "19"),
    "19" : Msg("npc", _("Sure! I should start getting dressed too before the saleswoman comes back  {image=images/MENUS/e_blush2.png}"), "66"),
    "18b" : Msg("mc", _("You have a spectacular body too!\nI wish I could have seen more of it in that photo... {image=images/MENUS/e_tongue.png}"), "20"),
    "18c" : Msg("mc", _("Can't wait to see that!\nNow I just wish you'd taken that photo vertically... {image=images/MENUS/e_tongue.png}"), "20"),
    "20" : Msg("npc", _(". . ."), "21"),
    "21" : Msg("npc", _("...like this?\n{size=10} "), ["21a", "21b"], picture="dm 4d"),
    "22" : Msg("npc", _("Thank you {image=images/MENUS/e_heart.png}"), "23"),
    "23" : Msg("npc", _("I'll let it grow until it's as long as in Eternum!"), ["18a", "18c"]),
    "21a" : Msg("mc", _("Oh, nice! Chang's gonna love this!"), "24"),
    "21b" : Msg("mc", _("OMG  {image=images/MENUS/e_hearteyes.png} {image=images/MENUS/e_hearteyes.png} {image=images/MENUS/e_hearteyes.png} {image=images/MENUS/e_fire.png} {image=images/MENUS/e_fire.png} {image=images/MENUS/e_fire.png}"), "25"),
    "25" : Msg("npc", _("Well, I should start getting dressed before the saleswoman comes back...  {image=images/MENUS/e_blush2.png}"), "30a", actions="phone_point('annie_points')"),
    "24" : Msg("npc", _("[mc]!!!!!!!"), "26"),
    "26" : Msg("npc", _("Don't show this to anyone!"), "311"),
    "311" : Msg("npc", _("DELETE IT NOW!!"), "31a"),
    "31a" : Msg("mc", _("Hahaha no worries, I'm kidding! I'll see you later at home! {image=images/MENUS/e_wink.png}"), "6666"),
    "6666" : Msg("npc", _("You better!")),
    "30a" : Msg("mc", _("Of course! See you later! {image=images/MENUS/e_wink.png}"), "66"),
    }

define annie_chat2 = {
    "background" : "gh 8b",
    "thumbnail" : "chat_annie_1",
    "npc" : "Annie",
    "0" : Msg("npc", _("OMG {image=images/MENUS/e_cry.png} {image=images/MENUS/e_cry.png} {image=images/MENUS/e_cry.png} {image=images/MENUS/e_cry.png}"), ["1", "2"]),
    "1" : Msg("mc", _("Hmm? You forgot about our dinner?"), "3"),
    "2" : Msg("mc", _("What happened???"), "4"),
    "3" : Msg("npc", _("Of course not {image=images/MENUS/e_angry.png}"), "4"),
    "4" : Msg("npc", _("The underpass is flooded from the rain, so the bus can’t get through {image=images/MENUS/e_cry.png}"), "5"),
    "5" : Msg("npc", _("I have to walk to the restaurant now {image=images/MENUS/e_cry.png}"), "6"),
    "6" : Msg("npc", _("I'm gonna be late {image=images/MENUS/e_cry.png} {image=images/MENUS/e_cry.png} {image=images/MENUS/e_cry.png} {image=images/MENUS/e_cry.png} {image=images/MENUS/e_cry.png} {image=images/MENUS/e_cry.png}"), ["7", "8"]),
    "7" : Msg("mc", _("No worries!!! There's no rush {image=images/MENUS/e_relieved.png}"), "9"),
    "8" : Msg("mc", _("Ah np, but try to hurry\nThink the kitchen closes at 9:30"), "12"),
    "9" : Msg("npc", _("Thank you {image=images/MENUS/e_plead.png} {image=images/MENUS/e_plead.png} {image=images/MENUS/e_plead.png}"), "10", actions="phone_point('annie_points')"),
    "10" : Msg("npc", _("I'll try to be as fast as I can!!!"), "11"),
    "11" : Msg("mc", _("See you soon {image=images/MENUS/e_heart.png}")),
    "12" : Msg("npc", _("You sound so blunt when chatting, did you know that? {image=images/MENUS/e_unamused.png}"), "13"),
    "13" : Msg("npc", _("Anyway, I'll try to be fast"), "14"),
    "14" : Msg("npc", _("See you soon!")),
    }

define annie_chat3 = {
    "background" : "qp 42",
    "thumbnail" : "chat_annie_1",
    "npc" : "Annie",
    "0" : Msg("npc", _("[mc]!!!!"), "1"),
    "1" : Msg("npc", _("Idk when you'll receive this, but look!"), "2"),
    "2" : Msg("npc", _("It's SNOWING in London {image=images/MENUS/e_stareyes.png} {image=images/MENUS/e_stareyes.png} {image=images/MENUS/e_stareyes.png}\n "), ["3", "4"], picture="qp 43"),
    "4" : Msg("mc", _("Whoa! So niceee {image=images/MENUS/e_stareyes.png}"), "5"),
    "3" : Msg("mc", _("Doesn't it snow almost every year? {image=images/MENUS/e_lol.png}"), "6"),
    "5" : Msg("npc", _("You're online! {image=images/MENUS/e_hearteyes.png}"), "7"),
    "6" : Msg("npc", _("But not in December! {image=images/MENUS/e_angry.png}"), "676"),
    "676" : Msg("npc", _("It's the magic of Christmas!!!"), "66"),
    "66" : Msg("npc", _("You don't understand {image=images/MENUS/e_cry.png}"), "666"),
    "666" : Msg("mc", _("Okay okay, I understand now {image=images/MENUS/e_lol.png}"), "6660"),
    "6660" : Msg("npc", _("Did you at least like my selfie? {image=images/MENUS/e_cry.png}"), ["20", "21"]),
    "20" : Msg("mc", _("I LOVE IT! {image=images/MENUS/e_hearteyes.png}"), "14"),
    "21" : Msg("mc", _("It looks a bit blurry lol"), "22"),
    "22" : Msg("npc", _("Because I was moving {image=images/MENUS/e_cry.png}"), "23"),
    "23" : Msg("npc", _("You don't appreciate me {image=images/MENUS/e_cry.png} {image=images/MENUS/e_cry.png} {image=images/MENUS/e_cry.png}"), "24"),
    "24" : Msg("npc", _("Anyways, I gotta run now or my dad will get mad!"), "25"),
    "25" : Msg("npc", _("Have fun with the girls!"), "26"),
    "26" : Msg("npc", _("Text you tomorrow!"), "27"),
    "27" : Msg("mc", _("Cya!")),
    "7" : Msg("npc", _("I thought Nancy said you had no signal??"), ["8", "9"]),
    "8" : Msg("mc", _("The power of love boosted the signal, obviously {image=images/MENUS/e_relieved.png}"), "10"),
    "9" : Msg("mc", _("Yeahh but I walked off a bit to grab wood for the fire"), "45"),
    "45" : Msg("npc", _("Ohhh I see I see!"), "46"),
    "46" : Msg("npc", _("Guess I got lucky then {image=images/MENUS/e_tongue2.png}"), "13"),
    "10" : Msg("npc", _("Hahahahahaha"), "11", actions="phone_point('annie_points')"),
    "11" : Msg("npc", _("Of course!!!"), "12"),
    "12" : Msg("npc", _("That makes sense now {image=images/MENUS/e_hearteyes.png}"), "13"),
    "13" : Msg("mc", _("Might lose signal again soon, but thanks for the pic {image=images/MENUS/e_heart.png}"), "14"),
    "14" : Msg("npc", _("Glad you liked it {image=images/MENUS/e_blush2.png}"), "15"),
    "15" : Msg("mc", _("Will you send me more selfies later? {image=images/MENUS/e_monke.png}"), "16"),
    "16" : Msg("npc", _("I'll consider {image=images/MENUS/e_blush2.png} {image=images/MENUS/e_blush2.png} {image=images/MENUS/e_blush2.png}"), "111"),
    "111" : Msg("npc", _("But I really gotta go now or my dad will get mad {image=images/MENUS/e_tongue2.png}"), "122"),
    "122" : Msg("npc", _("Have fun with the girls!"), "133"),
    "133" : Msg("npc", _("Love you {image=images/MENUS/e_heart.png}"), "144"),
    "144" : Msg("mc", _("Love you more {image=images/MENUS/e_heart.png}")),
    }


define nova_chat3 = {
    "background" : "dm 3",
    "thumbnail" : "chat_nova_1",
    "npc" : "Nova",
    "0" : Msg("npc", _("Where are you? {image=images/MENUS/e_scream.png}"), "1"),
    "1" : Msg("npc", _("You don't live with the Carters anymore?"), "2a"),
    "2a" : Msg("mc", _("I just got home!"), "3"),
    "3" : Msg("npc", _("YOU'RE home?? I've just got out of there!"), "4"),
    "4" : Msg("npc", _("Wait for me, I'm going back!"), ["3a", "3b"]),
    "3a" : Msg("mc", _("I won't move an inch!")),
    "3b" : Msg("mc", _("Ok, but hurry up"), "5"),
    "5" : Msg("npc", _("{image=images/MENUS/e_angry.png} {image=images/MENUS/e_unamused.png} {image=images/MENUS/e_unamused.png}")),
    }

define nova_chat4 = {
    "background" : "gh 20",
    "thumbnail" : "chat_nova_1",
    "npc" : "Nova",
    "0" : Msg("npc", _("AAAAAAAAAAAGGGHHH"), "00"),
    "00" : Msg("npc", _("GOING TO ETERNUM WITH OUR REAL BODY SUCKS {image=images/MENUS/e_angry.png}"), "1"),
    "1" : Msg("npc", _("My eye's still itching from being exposed to bright light for too long {image=images/MENUS/e_cry.png}"), "2"),
    "2" : Msg("npc", _("Doc said I can't take off my patch for a couple of weeks at least {image=images/MENUS/e_unamused.png}"), "3"),
    "3" : Msg("npc", _("And I got sunburned {image=images/MENUS/e_cry.png} {image=images/MENUS/e_cry.png} {image=images/MENUS/e_cry.png} {image=images/MENUS/e_cry.png} {image=images/MENUS/e_cry.png}"), "33"),
    "33" : Msg("npc", _("Now I've got bikini tan lines {image=images/MENUS/e_cry.png}"), ["4", "5"]),
    "4" : Msg("mc", _("Oh no! Do you have after-sun?"), "6"),
    "5" : Msg("mc", _("Oh no! Can I see? {image=images/MENUS/e_tongue.png}"), "14"),
    "6" : Msg("npc", _("I think so, yeah"), "7"),
    "7" : Msg("npc", _("But I'll have to go sunbathing to get rid of the tan lines anyway... so boring {image=images/MENUS/e_sleep.png}"), ["8", "9"]),
    "8" : Msg("mc", _("Let me see how serious it is {image=images/MENUS/e_tongue.png}"), "14"),
    "9" : Msg("mc", _("I can go sunbathing with you {image=images/MENUS/e_wink.png}"), "10"),
    "10" : Msg("npc", _("Okay, that makes it a lil better {image=images/MENUS/e_blush2.png}"), "110"),
    "110" : Msg("npc", _("How about..."), "11"),
    "11" : Msg("npc", _("Oops my mom's calling me to dinner, gotta go!"), ["12", "12b"]),
    "12" : Msg("npc", _("I'll continue later! {image=images/MENUS/e_heart.png} {image=images/MENUS/e_heart.png} {image=images/MENUS/e_heart.png} {image=images/MENUS/e_heart.png}"), "13", condition="photonovatan2"),
    "12b" : Msg("npc", _("I'll continue later!"), "13", condition="not photonovatan2"),
    "13" : Msg("mc", _("Sure! See ya {image=images/MENUS/e_heart.png}")),
    "14" : Msg("npc", _("PERVERT {image=images/MENUS/e_angry.png}"), "155"),
    "155" : Msg("npc", _(". . . ."), "15"),
    "15" : Msg("npc", _("Ok maybe I can show you... but don't show ANYONE!! {image=images/MENUS/e_monke.png}"), "16"),
    "16" : Msg("npc", _("{image=images/MENUS/e_monke.png} {image=images/MENUS/e_monke.png} {image=images/MENUS/e_monke.png} {image=images/MENUS/e_monke.png} {image=images/MENUS/e_monke.png}\n "), ["17", "18", "19"], picture="gh 20b", actions="store.photonovatan=True"),
    "17" : Msg("mc", _("Lol you had that pic ready to send, didn't you?? {image=images/MENUS/e_lol.png}"), "20"),
    "18" : Msg("mc", _("Wow you sure got tanned! {image=images/MENUS/e_wow.png}"), "21"),
    "19" : Msg("mc", _("Oh DAMN {image=images/MENUS/e_wow.png} {image=images/MENUS/e_fire.png} {image=images/MENUS/e_fire.png}\nIs the front also that bad? {image=images/MENUS/e_smirk.png}"), "22", actions="store.photonovatan2=True"),
    "20" : Msg("npc", _("Of course not {image=images/MENUS/e_monke.png} {image=images/MENUS/e_monke.png} {image=images/MENUS/e_monke.png}"), "202"),
    "202" : Msg("npc", _("It was just in"), "11"),
    "21" : Msg("npc", _("I know right?? It looks so ugly {image=images/MENUS/e_cry.png}"), "212"),
    "212" : Msg("npc", _("There's a sports center with a solarium nearby, I can try to"), "11"),
    "22" : Msg("npc", _("I'm not sure...."), "23", actions="phone_point('nova_points')"),
    "23" : Msg("npc", _("Maybe I'd need an expert to check in person and let me know what's the situation........ {image=images/MENUS/e_blush2.png} {image=images/MENUS/e_blush2.png} {image=images/MENUS/e_monke.png}"), "110"),
    }

define nova_chat2 = {
    "background" : "df 22",
    "thumbnail" : "chat_nova_1",
    "npc" : "Nova",
    "0" : Msg("npc", _("I'm ready!!  {image=images/MENUS/e_blush.png}"), "1"),
    "1" : Msg("npc", _("I'll be waiting for you at the corner of O'Connor Bridge"), ["2a", "2b"]),
    "2a" : Msg("mc", _("We're on our way!\nCan't wait to see u {image=images/MENUS/e_tongue.png}"), "3"),
    "2b" : Msg("mc", _("Ok"), "4"),
    "3" : Msg("npc", _("{image=images/MENUS/e_blush.png} {image=images/MENUS/e_blush.png} {image=images/MENUS/e_blush.png}"), actions="phone_point('nova_points')"),
    "4" : Msg("npc", _("So enthusiastic...")),
    }



define alex_chat = {
    "background" : "ca 14",
    "thumbnail" : "chat_alex_1",
    "npc" : "Alexandra",
    "0" : Msg("npc", _("Good morning  {image=images/MENUS/e_sleep.png}"), "0a"),
    "0a" : Msg("mc", _("Huh?"), "1"),
    "1" : Msg("npc", _("I saw you sleeping in Keating's class"), "33"),
    "33" : Msg("npc", _("You better not fall asleep tomorrow night... We're supposed to go to that fancy dinner in Eternum"), "3"),
    "3" : Msg("npc", _("The Boyle mansion, Rockefeller server, the masquerade party... remember?  {image=images/MENUS/e_brows.png}"), ["2a","2b"]),
    "2a" : Msg("mc", _("Of course. How could I forget about our first date, babe?  {image=images/MENUS/e_heart.png}"), "11", condition="alexpath", actions="phone_point('alex_points')"),
    "2b" : Msg("mc", _("Yeah, I know you're all counting on me. No worries, I got this  {image=images/MENUS/e_strong.png}"), "4"),
    "4" : Msg("npc", _("Ok"),["5","6"]),
    "5" : Msg("npc", _("Btw, my father will probably be there, so... let’s try to avoid him"), ["5a","5b"], condition="not alexpath"),
    "6" : Msg("npc", _("Btw, my father will probably be there, so... let’s try to avoid him"), "9"),
    "5a" : Msg("mc", _("Got it. I'll text you tomorrow. Cya Alex"), "7"),
    "5b" : Msg("mc", _("Got it. I'll text you tomorrow. Cya Alexandra"), "8"),
    "7" : Msg("npc", _("Alexandra.")),
    "8" : Msg("npc", _("Ok")),
    "9" : Msg("npc", _("Meet me in the backyard of the mansion. And bring the masks"), ["6a"]),
    "6a" : Msg("mc", _("Got it. I'll text you before logging in. TTYL!"), "10"),
    "10" : Msg("npc", _("Cya tomorrow")),
    "11" : Msg("npc", _("LMAO yeah keep dreaming"), "122"),
    "122" : Msg("npc", _("Also... don’t call me babe, not now, not ever"), "12"),
    "12" : Msg("npc", _("We have a mission to do, keep your pickle in your pants"), "7a"),
    "7a" : Msg("mc", _("Can't we do both... honeybear?"), "13"),
    "13" : Msg("npc", _("{image=images/MENUS/e_unamused.png}  relax Romeo."), "6"),
    }

define alex_chat2 = {
    "background" : "cf 5",
    "thumbnail" : "chat_alex_1",
    "npc" : "Alexandra",
    "0" : Msg("npc", _("If you're late, I’m kicking you in the nuts")),
    }

define alex_chat3 = {
    "background" : "er 1",
    "thumbnail" : "chat_alex_1",
    "npc" : "Alexandra",
    "0" : Msg("npc", _("Hey"), "0a"),
    "0a" : Msg("mc", _("I'm on my way!"), "1"),
    "1" : Msg("npc", _("It'll be better if you don't come"), "33"),
    "33" : Msg("npc", _("I caught a cold and my nose turned into a leaky faucet"), "3"),
    "3" : Msg("npc", _("I'll show you the apartment another day"), ["2a","2b"]),
    "2a" : Msg("mc", _("Oh shit, really? \nI can come anyway and look after you {image=images/MENUS/e_relieved.png}"), "11", actions="phone_point('alex_points')"),
    "2b" : Msg("mc", _("And what about the Wild West server? \nAnd the Gem??"), "4"),
    "4" : Msg("npc", _("I can still play"), "5"),
    "5" : Msg("npc", _("I'll feel alright once I'm in Eternum"), "5a"),
    "5a" : Msg("mc", _("Well, ok then. As you wish"), "7"),
    "5b" : Msg("mc", _("Well, ok then. As you wish"), "8"),
    "7" : Msg("npc", _("Just meet me there with Dalia in an hour or so"), "6a"),
    "8" : Msg("npc", _("Just meet me in the Wild West server with Dalia in an hour or so"), "6a"),
    "6a" : Msg("mc", _("Got it. See you later!")),
    "11" : Msg("npc", _("There's no need"), "12"),
    "12" : Msg("npc", _("I can take care of myself {image=images/MENUS/e_unamused.png}"), "13"),
    "13" : Msg("npc", _("But"), "14"),
    "14" : Msg("npc", _("Thank you"), "15"),
    "15" : Msg("npc", _("But don't come"), "5b"),
    }

define alex_chat4 = {
    "background" : "gh 20",
    "thumbnail" : "chat_alex_1",
    "npc" : "Alexandra",
    "0" : Msg("npc", _("Heyyyy could you bring Dalia's math notes to the pool tomorrow like around 12?\n \nI’d pick them up myself, but I’m working till 10 tonight and then back at the pool for training 7AM {image=images/MENUS/e_sleep.png}\n \nI won't be able to reply till I'm out, so thanks if you say yes {image=images/MENUS/e_pray.png}\nOr fuck you if you don't {image=images/MENUS/e_finger.png}\nUnless you had other plans that make it impossible, then I'll just be moderately sad\n \nModerately"), ["1", "2"]),
    "1" : Msg("mc", _("I'll be there {image=images/MENUS/e_tongue.png}"), actions="store.alexpoolvisit=True"),
    "2" : Msg("mc", _("Sorry I can't {image=images/MENUS/e_pray.png}\nI'll try to get them to you on Monday!")),
    }


define dalia_chat3 = {
    "background" : "gx 122",
    "thumbnail" : "chat_dalia_1b",
    "npc" : "Dalia",
    "0" : Msg("npc", _("{image=images/08/buumeme.jpg}"), ["1", "2"]),
    "1" : Msg("mc", _("Yes, yes, I'm going, don't be so impatient  {image=images/MENUS/e_unamused.png}"), "33"),
    "2" : Msg("mc", _("SORRY! I'M ON MY WAY!!!"), "5"),
    "33" : Msg("npc", _("Dint bi si impitient"), "3"),
    "3" : Msg("npc", _("{image=images/MENUS/e_unamused.png} {image=images/MENUS/e_unamused.png} {image=images/MENUS/e_unamused.png} {image=images/MENUS/e_unamused.png} {image=images/MENUS/e_unamused.png}"), "4"),
    "4" : Msg("npc", _("BE FAST!!!")),
    "5" : Msg("npc", _("I'm in a good mood, so I'll forgive you... {image=images/MENUS/e_relieved.png}"), "6"),
    "6" : Msg("npc", _("But be fast!"), "7"),
    "7" : Msg("npc", _("We've got work to do! {image=images/MENUS/e_stareyes.png}"), actions="phone_point('dalia_points')"),
    }
define dalia_chat3b = {
    "background" : "gx 122",
    "thumbnail" : "chat_dalia_1",
    "npc" : "Dalia",
    "0" : Msg("npc", _("{image=images/08/buumeme.jpg}"), ["1", "2"]),
    "1" : Msg("mc", _("Yes, yes, I'm going, don't be so impatient  {image=images/MENUS/e_unamused.png}"), "33"),
    "2" : Msg("mc", _("SORRY! I'M ON MY WAY!!!"), "5"),
    "33" : Msg("npc", _("Dint bi si impitient"), "3"),
    "3" : Msg("npc", _("{image=images/MENUS/e_unamused.png} {image=images/MENUS/e_unamused.png} {image=images/MENUS/e_unamused.png} {image=images/MENUS/e_unamused.png} {image=images/MENUS/e_unamused.png}"), "4"),
    "4" : Msg("npc", _("BE FAST!!!")),
    "5" : Msg("npc", _("I got myself an icecream, so I can wait... {image=images/MENUS/e_relieved.png}"), "6"),
    "6" : Msg("npc", _("But be fast!"), "7"),
    "7" : Msg("npc", _("We've got work to do! {image=images/MENUS/e_stareyes.png}"), actions="phone_point('dalia_points')"),
    }


define dalia_chat2 = {
    "background" : "ca 14",
    "thumbnail" : "chat_dalia_1",
    "npc" : "Dalia",
    "0" : Msg("npc", _("Hey."), "1"),
    "1" : Msg("npc", _("Remember to pick up the groceries from the store. It's your turn today."), "0a"),
    "0a" : Msg("mc", _("Of course. Hey Dalia, about the other day..."), "2"),
    "2" : Msg("npc", _("I don't wanna talk to you.")),
    }

define dalia_chat = {
    "background" : "ca 14",
    "thumbnail" : "chat_dalia_1",
    "npc" : "Dalia",
    "0" : Msg("npc", _("Holy shit [mc], I just saw an alpaca with your hairstyle on Reddit  {image=images/MENUS/e_mindblow.png}\n "), ["1a", "1b"], picture="alpacameme"),
    "1a" : Msg("mc", _("Funny you should mention that..."), "3a", actions="store.daliameme=True"),
    "1b" : Msg("mc", _("Ha. ha. ha. Very funny, Dalia..."), "2"),
    "3a" : Msg("mc", _("Cause I just saw a meme of a dog with yours  {image=images/MENUS/e_mindblow.png}\n "), "6", picture="dogmeme"),
    "2" : Msg("npc", _("Jeez, you need a better sense of humor, [mc]... {image=images/MENUS/e_unamused.png}"), "3"),
    "3" : Msg("npc", _("Anyway, I'm jumping in the shower.\nBye!"), ["2a", "2b"]),
    "2a" : Msg("mc", _("Maybe I'm not the one with a bad sense of humor."), "4", condition="not daliameme"),
    "2b" : Msg("mc", _("See you later!")),
    "4" : Msg("npc", _(". . ."), "5"),
    "5" : Msg("npc", _("Kay, I see you woke up in jerk mode today.\n Bye.")),
    "6" : Msg("npc", _("HAHAHAHA"), ["4a", "4b"], actions="phone_point('dalia_points')"),
    "4a" : Msg("mc", _("Now I see where you got your style from"), "7"),
    "4b" : Msg("mc", _("Maybe you should go back to the braids"), "8"),
    "7" : Msg("npc", _("You got me!"), "9"),
    "8" : Msg("npc", _("Are you kidding me???"), "9"),
    "9" : Msg("npc", _("I'm gonna use that as my new pfp {image=images/MENUS/e_stareyes.png}"), "5a"),
    "5a" : Msg("mc", _("Haha can't wait to see that!"), "3"),
    }

define penelope_chat3 = {
    "background" : "ff 1",
    "thumbnail" : "chat_penelope_1",
    "npc" : "Penelope",
    "0" : Msg("npc", _("Hi! {image=images/MENUS/e_heart.png}"), "1"),
    "1" : Msg("mc", _("Hey there! I'm at the cafe with Luna\nHeading home soon"), "2"),
    "2" : Msg("npc", _("Cool! I'll be home soon too"), "3"),
    "3" : Msg("npc", _("I just bought a couple of new things at the mall... for tomorrow's photoshoot"), ["4", "5"]),
    "4" : Msg("mc", _("Nice! \nI bet we'll take some great shots {image=images/MENUS/e_relieved.png}"), "6"),
    "5" : Msg("mc", _("Oh boy... {image=images/MENUS/e_fire.png}{image=images/MENUS/e_fire.png}{image=images/MENUS/e_fire.png}\nCan I get a sneak peek...? {image=images/MENUS/e_tongue.png}"), "77"),
    "6" : Msg("npc", _("Yeah, I'm sure of it {image=images/MENUS/e_blush.png}"), "66"),
    "66" : Msg("npc", _("But let's worry about that tomorrow!"), "7"),
    "77" : Msg("npc", _("You'll have to wait for tomorrow... {image=images/MENUS/e_relieved.png}"), "7", picture="bonk07", actions="phone_point('penelope_points')"),
    "7" : Msg("npc", _("Today's mission: vampire hunting {image=images/MENUS/e_ghost.png}"), ["9", "10"]),
    "10" : Msg("mc", _("True! I better be on my way \nSee you later Penny ^^"), "12"),
    "9" : Msg("mc", _("Ah, true!  {image=images/MENUS/e_skull.png} \nCan't wait to play with you {image=images/MENUS/e_heart.png}"), "11"),
    "11" : Msg("npc", _("Don't keep me waiting... {image=images/MENUS/e_relieved.png}"), "13"),
    "12" : Msg("npc", _("Later!")),
    "13" : Msg("npc", _("See you later! {image=images/MENUS/e_heart.png}{image=images/MENUS/e_heart.png}")),
    }

define penelope_chat4 = {
    "background" : "fe 6",
    "thumbnail" : "chat_penelope_1",
    "npc" : "Penelope",
    "0" : Msg("npc", _("If you wake up and wonder where we are, Annie and I are hitting the gym with Dalia {image=images/MENUS/e_strong.png} {image=images/MENUS/e_smirk.png}"), "1"),
    "1" : Msg("npc", _("I know you're busy with Nova and Mom today, so we didn't want to wake you up {image=images/MENUS/e_ghost.png}"), "2"),
    "2" : Msg("mc", _("Oh, nice! Enjoy your gym time!\nI just woke up after sleeping 9 hours {image=images/MENUS/e_skull.png}"), "3"),
    "3" : Msg("npc", _("Ah, morning, sleeping princess! {image=images/MENUS/e_crown.png}"), "4"),
    "4" : Msg("npc", _("We're already there!"), "44"),
    "44" : Msg("npc", _("Although I'm taking it easy today... my legs are still in full flan mode... {image=images/MENUS/e_blush2.png}"), ["5", "6"]),
    "5" : Msg("mc", _("I wonder why... did something happen yesterday? {image=images/MENUS/e_tongue.png}"), "20"),
    "6" : Msg("mc", _("Cool! Have a good training!"), "7"),
    "66" : Msg("mc", _("Hahah good luck with that! {image=images/MENUS/e_strong.png} {image=images/MENUS/e_strong.png}"), "77"),
    "77" : Msg("npc", _("Haha thanks, I'll need it {image=images/MENUS/e_tongue.png}"), "777"),
    "777" : Msg("npc", _("I'll have to train harder than I used to if I want to be able to endure upcoming photoshoots..."), "7777"),
    "7777" : Msg("mc", _("Oh, so will there be more photoshoots in the future...?"), "9"),
    "7" : Msg("npc", _("Thanks!"), "8"),
    "8" : Msg("npc", _("Dalia's on a mission to transform us into the fittest squad ever {image=images/MENUS/e_wow.png}\n "), ["66", "37"], picture="fe 7b"),
    "9" : Msg("npc", _("Maybe..."), "10"),
    "10" : Msg("npc", _("Only that next ones might have to be in my room..."), "11"),
    "11" : Msg("npc", _("And perhaps we can jump straight to the “private shooting” part..."), "12"),
    "12" : Msg("npc", _("Actually, I don't think we even need a camera... {image=images/MENUS/e_blush2.png}"), "13"),
    "13" : Msg("mc", _("Count me in for that next photoshoot then {image=images/MENUS/e_wow.png}"), "140"),
    "140" : Msg("npc", _("I will... {image=images/MENUS/e_blush2.png}"), "14"),
    "14" : Msg("npc", _("Anyway!! I better get back to training before Dalia gets mad at me!"), "15"),
    "144" : Msg("npc", _("Anyway, I better get back to training before Dalia gets mad at me!"), "35"),
    "1444" : Msg("npc", _("But anyway, I better get back to training before Dalia and her huge butt get mad at me!!!"), "15"),
    "14440" : Msg("npc", _("But anyway, I better get back to training before Dalia and her huge butt get mad at me!!!"), "155"),
    "155" : Msg("npc", _("Bye!! {image=images/MENUS/e_two.png}"), "169"),
    "15" : Msg("mc", _("No selfie to wish me luck for today's Gem hunt?"), ["160", "166"]),
    "160" : Msg("npc", _("{image=images/MENUS/e_think.png}"), "16", condition="pennyselfietopless"),
    "166" : Msg("npc", _("No time!!!"), "167"),
    "167" : Msg("npc", _("I MUST GET STRONGER!!!!"), "168"),
    "168" : Msg("npc", _("See you later [mc] {image=images/MENUS/e_two.png}"), "169"),
    "169" : Msg("mc", _("Hahah alright! See you later! {image=images/MENUS/e_heart.png}")),
    "16" : Msg("npc", _("Good luck on your Gem hunt, [mc]! {image=images/MENUS/e_two.png}\n"), ["17", "18", "3700", "370"], picture="fe 7c"),
    "17" : Msg("mc", _("That's better {image=images/MENUS/e_stareyes.png} Thank you!\nSee you all tonight {image=images/MENUS/e_tongue.png}"), "19"),
    "18" : Msg("mc", _("Wow, you look beautiful {image=images/MENUS/e_hearteyes.png}"), "41"),
    "19" : Msg("npc", _("See you later, [mc]... {image=images/MENUS/e_heart.png}")),
    "20" : Msg("npc", _("I had a pretty intense session yesterday at the studio... {image=images/MENUS/e_relieved.png}"), ["21", "22"]),
    "21" : Msg("mc", _("Ah yes, I've heard the modeling world can be very hard  {image=images/MENUS/e_relieved.png}"), "23"),
    "22" : Msg("mc", _("Yeah... sorry about that, Penny {image=images/MENUS/e_sweat.png}"), "25"),
    "23" : Msg("npc", _("Luckily I'm a tough girl..."), "2224"),
    "2224" : Msg("npc", _("But I need to get even tougher {image=images/MENUS/e_relieved.png}"), "24"),
    "24" : Msg("mc", _("Oohh, so that's why you joined the gym so early today, huh?  {image=images/MENUS/e_relieved.png}"), "244"),
    "244" : Msg("npc", _("Yes! {image=images/MENUS/e_tongue.png}"), "8", actions="store.pennyselfietopless=True"),
    "25" : Msg("npc", _("Sorry for what?"), "26"),
    "26" : Msg("npc", _("Do you regret anything?"), ["27", "28"]),
    "27" : Msg("mc", _("Not for a moment {image=images/MENUS/e_tongue.png}"), "29"),
    "28" : Msg("mc", _("Maybe it's better if we talk about this face to face"), "33"),
    "29" : Msg("npc", _("Good"), "30"),
    "30" : Msg("npc", _("Because I don't either..."), "31"),
    "31" : Msg("npc", _("Even if I'm having trouble walking today {image=images/MENUS/e_wow.png}"), "32"),
    "32" : Msg("npc", _("I need to get tougher!"), "24"),
    "33" : Msg("npc", _("Well okay"), "34"),
    "34" : Msg("npc", _("As you prefer"), "144"),
    "35" : Msg("npc", _("See you later! {image=images/MENUS/e_two.png}"), "36"),
    "36" : Msg("mc", _("Later!")),
    "37" : Msg("mc", _("Wow, you got a good angle of Dalia there {image=images/MENUS/e_wow.png}"), "38"),
    "3700" : Msg("mc", _("Goddamn, you REALLY got a good angle of Dalia again {image=images/MENUS/e_wow.png}"), "3800", condition="daliabuttcomment2"),
    "370" : Msg("mc", _("Wow, you got a good angle of Dalia there {image=images/MENUS/e_wow.png}"), "380", condition="daliabuttcomment1"),
    "38" : Msg("npc", _("Men... {image=images/MENUS/e_unamused.png}"), "39"),
    "380" : Msg("npc", _("Men... {image=images/MENUS/e_unamused.png}"), "390"),
    "3800" : Msg("npc", _("MEN AND THEIR TUNNEL VISION {image=images/MENUS/e_unamused.png} {image=images/MENUS/e_unamused.png} {image=images/MENUS/e_unamused.png}"), "144"),
    "39" : Msg("npc", _("Although yeahh I've gotta agree hahah"), "40", actions="store.daliabuttcomment1=False"),
    "390" : Msg("npc", _("Although yeahh I've gotta agree hahah"), "400"),
    "40" : Msg("npc", _("I'm proud of my hot sissy {image=images/MENUS/e_hearteyes.png}"), "1444", actions="store.daliabuttcomment2=True"),
    "400" : Msg("npc", _("I'm proud of my hot sissy {image=images/MENUS/e_hearteyes.png}"), "14440"),
    "41" : Msg("npc", _("Hehe thanks!"), "42"),
    "42" : Msg("npc", _("I'm wearing brand new leggings today!"), "43"),
    "43" : Msg("npc", _("What are your thoughts on them...?\n"), "45", picture="fe 7d"),
    "45" : Msg("mc", _("OH. MY. GOD. {image=images/MENUS/e_wow.png} {image=images/MENUS/e_wow.png} {image=images/MENUS/e_wow.png} {image=images/MENUS/e_wow.png} {image=images/MENUS/e_wow.png}"), "4699"),
    "4699" : Msg("npc", _("Haha glad you like them! {image=images/MENUS/e_blush2.png}"), "51"),
    "51" : Msg("npc", _("But for real now, I've gotta go! And good luck in the pirate server!"), "46"),
    "46" : Msg("npc", _("See you later, [mc] {image=images/MENUS/e_heart.png}"), "47", actions="phone_point('penelope_points')"),
    "47" : Msg("mc", _("Later, Penny {image=images/MENUS/e_heart.png}")),
    }
    
define penelope_chat = {
    "background" : "ca 14",
    "thumbnail" : "chat_penelope_1",
    "npc" : "Penelope",
    "0" : Msg("npc", _("Heyyyy! I need the help of my manager!"), ["1a", "1b"]),
    "1a" : Msg("mc", _("What’s up? How can I help my favorite client?"), "3"),
    "1b" : Msg("mc", _("Don't have time right now, Penny"), "2"),
    "2" : Msg("npc", _("Ok, ok... {image=images/MENUS/e_unamused.png}"), "22"),
    "22" : Msg("npc", _("TTYL")),
    "3" : Msg("npc", _("I'm going through some photos I took last year with my friend April"), ["4"], actions="store.pennypics04=True"),
    "4" : Msg("npc", _("I need you to help me choose a pic  {image=images/MENUS/e_pray.png} {image=images/MENUS/e_blush.png}"), "2a"),
    "2a" : Msg("mc", _("Go for it!"), "5"),
    "5" : Msg("npc", _("Option A"), "6", picture="ca 19"),
    "6" : Msg("npc", _("Option B"), ["3a", "3b", "3c"], picture="ca 20"),
    "3a" : Msg("mc", _("Option A"), "7"),
    "3b" : Msg("mc", _("Option B"), "8"),
    "3c" : Msg("mc", _("All photos are great when the girl in them is so stunning  {image=images/MENUS/e_wink.png}"), "9"),
    "7" : Msg("npc", _("That's the one I was leaning towards too!  {image=images/MENUS/e_blush.png}"), "11"),
    "8" : Msg("npc", _("Really? Kinda leaning towards the other one, but you seem to have a knack for photography, I’ll go with your pick!  {image=images/MENUS/e_blush.png}"), "11"),
    "9" : Msg("npc", _("Oh come on, don't be such a cheeseball! Choose one!"), "10", actions="phone_point('penelope_points')"),
    "10" : Msg("npc", _("Thanks, though  {image=images/MENUS/e_heart.png}"), ["3a", "3b"]),
    "11" : Msg("npc", _("Thanks [mc]  {image=images/MENUS/e_heart.png}"), "4a"),
    "4a" : Msg("mc", _("Anytime!"), "12"),
    "12" : Msg("npc", _("See you at home!")),
    }

define penelope_chat2 = {
    "background" : "er 1",
    "thumbnail" : "chat_penelope_1",
    "npc" : "Penelope",
    "0" : Msg("npc", _("[mc]!"), "1"),
    "1" : Msg("npc", _("I'm with Luna at the mall and she got her hair done at Paul's {image=images/MENUS/e_hearteyes.png}"), "2"),
    "2" : Msg("npc", _("I need you to tell her how beautiful she looks before she takes a shower and loses this style!"), "1a"),
    "1a" : Msg("mc", _("I'm your man!"), ["3", "33"]),
    "3" : Msg("npc", _("Hai!\n "), ["3a", "3b", "3c"], picture="er 21", condition="changshirts"),
    "33" : Msg("npc", _("Hai!\n "), ["3a", "3b", "3c"], picture="er 21b"),
    "3a" : Msg("mc", _("She looks so pretty  {image=images/MENUS/e_hearteyes.png}"), "4"),
    "3b" : Msg("mc", _("You both look stunning  {image=images/MENUS/e_hearteyes.png} {image=images/MENUS/e_hearteyes.png}"), "5"),
    "3c" : Msg("mc", _("Haha come on, stop fooling around"), "6"),
    "6" : Msg("npc", _("Ok ok we will..."), "66"),
    "66" : Msg("npc", _("In a little while! First we go shopping {image=images/MENUS/e_stareyes.png}"), "10"),
    "4" : Msg("npc", _("Right?? Let me show your message to her!"), "4a", actions="phone_point('luna_points')"),
    "5" : Msg("npc", _("Awwww thank you {image=images/MENUS/e_blush2.png} {image=images/MENUS/e_blush2.png} {image=images/MENUS/e_blush2.png}"), "55", actions="phone_point('penelope_points')"),
    "55" : Msg("npc", _("Let me show what you said to Luna"), "4a", actions="phone_point('luna_points')"),
    "4a" : Msg("mc", _("Haha sure"), "8"),
    "8" : Msg("npc", _("She's smiling and blushing {image=images/MENUS/e_blush2.png}"), "9"),
    "9" : Msg("npc", _("You seem to charm all the girls around \nyou, [mc]... {image=images/MENUS/e_smirk.png}"), "10"),
    "10" : Msg("npc", _("Shit we gotta go"), "100"),
    "100" : Msg("npc", _("I think I saw Regina in the store {image=images/MENUS/e_skull.png} {image=images/MENUS/e_skull.png} {image=images/MENUS/e_skull.png}"), "5a"),
    "5a" : Msg("mc", _("Oh fuck, better run away from her {image=images/MENUS/e_skull.png}\nTake care, Penny {image=images/MENUS/e_heart.png}"), "12"),
    "12" : Msg("npc", _("See you later [mc] {image=images/MENUS/e_heart.png}")),
    }

define nova_chat = {
    "background" : "ca 14",
    "thumbnail" : "chat_nova_1",
    "npc" : "Nova",
    "0" : Msg("npc", _("[mc]!  {image=images/MENUS/e_scream.png}"), "1"),
    "1" : Msg("npc", _("[mc]???"), "2"),
    "2" : Msg("npc", _("[mc] it's urgent!!!  {image=images/MENUS/e_scream.png} {image=images/MENUS/e_scream.png} {image=images/MENUS/e_scream.png}"), "1a"),
    "1a" : Msg("mc", _("What's the matter?!"), "3"),
    "3" : Msg("npc", _("If you had just killed an ancient demon to rescue a girl, what badass quote would you say immediately after?  {image=images/MENUS/e_think.png}"), ["2a", "2b"]),
    "2a" : Msg("mc", _("That's... kind of an oddly specific question to ask"), "7"),
    "2b" : Msg("mc", _("That doesn't seem very urgent... I’ve got things to do, I'll see you later"), "4", actions="store.novacomicnoturgent=True"),
    "7" : Msg("npc", _("Just answer!"), ["3a", "3b", "3c"]),
    "3a" : Msg("mc", _("The only fate of the weak is to be crushed by the strong. Know your place, demon."), "80"),
    "3b" : Msg("mc", _("Nothing personal, demon. Just taking out the trash."), "80", actions="store.mcsayingafterkill+=1"),
    "3c" : Msg("mc", _("You sealed your fate the moment you put your filthy hands on her, demon. Go to hell... again."), "80", actions="store.mcsayingafterkill+=2"),
    "80" : Msg("npc", _("HAHA"), "8"),
    "8" : Msg("npc", _("That's perfect! {image=images/MENUS/e_stareyes.png}"), "4a"),
    "4a" : Msg("mc", _("Why’d you need a quote from me?"), "9"),
    "9" : Msg("npc", _("It's a surprise!!!!"), "10"),
    "4" : Msg("npc", _("Ugh! OK FINE!"), "5"),
    "5" : Msg("npc", _("I'll think of something on my own!"), "6"),
    "6" : Msg("npc", _("Bye...  {image=images/MENUS/e_unamused.png}")),
    "10" : Msg("npc", _("Gotta get back to work now!"), ["13"]),
    "13" : Msg("npc", _("Stop bothering me! {image=images/MENUS/e_angry.png}"), ["5a", "5b"]),
    "5a" : Msg("mc", _("You’re the one who texted me!"), "11"),
    "5b" : Msg("mc", _("Haha okay, okay, get back to your... thing"), "12"),
    "11" : Msg("npc", _("Fair enough :]"), "12"),
    "12" : Msg("npc", _("Bye!  {image=images/MENUS/e_blush.png}")),
    }

define luna_chat = {
    "background" : "ca 14",
    "thumbnail" : "chat_luna_1",
    "npc" : "Luna",
    "0" : Msg("npc", _("{i}{color=#818589}This message was deleted."), ["1", "2"]),
    "1" : Msg("npc", _("Hey [mc]."), "6", condition="not lunapath"),
    "6" : Msg("npc", _("Good luck with tomorrow's dinner in Eternum. We're counting on you."), "1a"),
    "2" : Msg("npc", _("{i}{color=#818589}This message was deleted."), "3"),
    "3" : Msg("npc", _("{i}{color=#818589}This message was deleted."), "4"),
    "4" : Msg("npc", _("{i}{color=#818589}This message was deleted."), "5"),
    "1a" : Msg("mc", _("Thanks Luna! I'll text you as soon as I finish!")),
    "5" : Msg("npc", _("Hi [mc]"), "2a"),
    "2a" : Msg("mc", _("Hey Luna!"), "7"),
    "8" : Msg("npc", _("Hi!"), "9"),
    "9" : Msg("npc", _("I just wanted to say"), "16"),
    "16" : Msg("npc", _("Next Friday is the Day of the Dead"), "3a"),
    "7" : Msg("npc", _("{i}{color=#818589}This message was deleted."), "8"),
    "3a" : Msg("mc", _("Oh yeah, I've heard about that before!"), "11"),
    "11" : Msg("npc", _("My dad and I always celebrate it. A few relatives come from Mexico to celebrate together"), "12"),
    "12" : Msg("npc", _("{i}{color=#818589}This message was deleted."), "13"),
    "13" : Msg("npc", _("Would you maybe want to come?"), "15"),
    "15" : Msg("npc", _("It's okay if you don't feel like it"), ["4a", "4b"]),
    "4a" : Msg("mc", _("Really? I'd love to!  {image=images/MENUS/e_mex.png} {image=images/MENUS/e_skull.png} {image=images/MENUS/e_mex.png}"), "10"),
    "10" : Msg("npc", _("Great!"), "19", actions="store.dayofthedead=True"),
    "4b" : Msg("mc", _("Thanks! But I prefer not to, it seems like a family thing"), "14"),
    "14" : Msg("npc", _("Yeah that's what I told my dad"), ["17"]),
    "17" : Msg("npc", _("No worries! See you Monday"), ["18"]),
    "18" : Msg("npc", _("And good luck with the Eternum dinner"), ["5a"]),
    "5a" : Msg("mc", _("Thank you so much! See you Monday!")),
    "19" : Msg("npc", _("Don't expect much though"), "20"),
    "20" : Msg("npc", _("My father asks if..."), "21"),
    "21" : Msg("npc", _("Wait, he wants to ask you directly"), "22a"),
    "22a" : Msg("mc", _("Huh?"), "22"),
    "22" : Msg("npc", _("[mc!u]! MY MAN!"), "23"),
    "23" : Msg("npc", _("I KNEW YOU WOULDN'T LET US DOWN!"), "24"),
    "24" : Msg("npc", _("LISTEN, I'M DOING TACOS FOR THE EVENT. IMPORTANT QUESTION: DO YOU LIKE YOUR TACOS SPICY OR EXTRA SPICY?"), ["25a", "25b"]),
    "25a" : Msg("mc", _("Not very spicy"), "26"),
    "25b" : Msg("mc", _("EXTRA SPICY!  {image=images/MENUS/e_spicy.png} {image=images/MENUS/e_spicy.png} {image=images/MENUS/e_spicy.png}"), "27"),
    "26" : Msg("npc", _("ALRIGHT I'LL SEE WHAT I CAN DO! JAJAJA"), "28"),
    "27" : Msg("npc", _("AHHH THAT'S MY MAN! YOU’RE GONNA MAKE MEXICO PROUD! IT MIGHT NOT SEEM LIKE IT BUT LUNA LOVES SPICY FOOD TOO!"), "28", actions="store.reallyspicy=True"),
    "28" : Msg("npc", _("BUT I'LL STOP BOTHERING YOU TWO NOW"), "29"),
    "29" : Msg("npc", _("CAN'T WAIT TO HAVE YOU HERE!\n "), "28a", picture="ca 23"),
    "28a" : Msg("mc", _("I'm excited about those tacos! Thanks for the invite!"), "30"),
    "30" : Msg("npc", _("I'm sorry about that, he grabbed my phone"), ["29a", "29b"]),
    "29a" : Msg("mc", _("Your father is a bit... out there"), "31"),
    "29b" : Msg("mc", _("Haha no worries, your dad’s just as awesome as you"), "32"),
    "31" : Msg("npc", _("Yeah... sorry about it"), "33"),
    "32" : Msg("npc", _("He seems to like you a lot as well"), "33", actions="phone_point('luna_points')"),
    "33" : Msg("npc", _("Anyways, I won't bother you anymore. Thanks for agreeing to come!"), "34"),
    "34" : Msg("npc", _("And good luck with the Eternum dinner!"), "34a"),
    "34a" : Msg("mc", _("Thank you Luna!\nCan't wait for next Friday! {image=images/MENUS/e_ghost.png}"), "40"),
    "40" : Msg("npc", _("Bye!")),
    }

define nancy_chat = {
    "background" : "ca 14",
    "thumbnail" : "chat_nancy_1",
    "npc" : "Nancy",
    "0" : Msg("npc", _("Hi sweetie {image=images/MENUS/e_heart.png}"), ["1"]),
    "1" : Msg("npc", _("I just bought myself a new bikini"), "2"),
    "2" : Msg("npc", _("What do you think?\n "), ["1a", "1b"], picture="ca 23b"),
    "1a" : Msg("mc", _("Looks great!"), "3"),
    "1b" : Msg("mc", _("I think you’d look better without it {image=images/MENUS/e_wink.png}"), "4"),
    "3" : Msg("npc", _("Thanks! {image=images/MENUS/e_blush2.png} We should head to the beach one day before it gets too cold"), ["6a", "6b"]),
    "4" : Msg("npc", _("Haha"), "5", actions="phone_point('nancy_points')"),
    "5" : Msg("npc", _("Don't be bad, you naughty boy..."), "2a"),
    "2a" : Msg("mc", _("You look crazy hot in it! {image=images/MENUS/e_wow.png}"), ["3"]),
    "6a" : Msg("mc", _("That sounds awesome!"), "7"),
    "6b" : Msg("mc", _("Meh, I'm not a fan of the beach"), "7"),
    "7" : Msg("npc", _("Oh, sorry, I gotta go!"), "8"),
    "8" : Msg("npc", _("Maximo just texted me. The Macedonians are trying to reconquer Megara"), "9"),
    "9" : Msg("npc", _("OVER MY DEAD BODY."), "10"),
    "10" : Msg("npc", _("See you later {image=images/MENUS/e_heart.png} {image=images/MENUS/e_heart.png}")),
    }

define chang_chat = {
    "background" : "ca 14",
    "thumbnail" : "chat_chang_1",
    "npc" : "Chang",
    "0" : Msg("npc", _("BRO"), ["1"]),
    "1" : Msg("npc", _("I was invited to a fancy restaurant by Micaela's parents and I have to impress them! {image=images/MENUS/e_scream.png}"), "2"),
    "2" : Msg("npc", _("You’ve gotta help me!"), ["1a", "1b"]),
    "1a" : Msg("mc", _("What do you need?"), "7"),
    "1b" : Msg("mc", _("Sorry bro, I don't have the time rn"), "4"),
    "7" : Msg("npc", _("What tie looks better on me? This one?"), "8", picture="ca 21"),
    "8" : Msg("npc", _("Or this one?"), ["3a","3b", "3c"], picture="ca 22"),
    "3a" : Msg("mc", _("The first one"), "13"),
    "3b" : Msg("mc", _("The second one"), "13"),
    "3c" : Msg("mc", _("Bro they're identical"), "9"),
    "3d" : Msg("mc", _("Those are the same exact photos!!!"), "12"),
    "3e" : Msg("mc", _("They're the same fucking color."), "4"),
    "4" : Msg("npc", _("AAAAh ok ok, FINE! I'll choose it myself!"), "5", actions="store.changtie=False"),
    "5" : Msg("npc", _("Wish me luck!"), "2a"),
    "2a" : Msg("mc", _("Best of luck, man! \nYOU GOT THIS!"), "6"),
    "6" : Msg("npc", _("Thanks bro!!!")),
    "13" : Msg("npc", _("Right?? That's what I was thinking too!"), "10"),
    "9" : Msg("npc", _("Noooo! The first one is bright turquoise, while the second one is a shade of cyan"), "14"),
    "14" : Msg("npc", _("Wait, I'll take new photos with better lighting"), "5a"),
    "5a" : Msg("mc", _("Alright"), "15"),
    "15" : Msg("npc", _("This one?"), "11", picture="ca 22"),
    "11" : Msg("npc", _("Or this one?"), ["3a","3b", "3d"], picture="ca 21"),
    "10" : Msg("npc", _("Thanks man, this gave me the confidence I needed"), "5"),
    "12" : Msg("npc", _("No they're not! Help me out here, please!"), ["3a","3b", "3e"]),
    }


define chang_chat2 = {
    "background" : "gh 20",
    "thumbnail" : "chat_chang_1",
    "npc" : "Chang",
    "0" : Msg("npc", _("BRO"), ["1"]),
    "1" : Msg("npc", _("PLEASE TELL ME YOU'RE ONLINE"), "2"),
    "2" : Msg("mc", _("What's up??"), "3"),
    "3" : Msg("npc", _("THANK GOD"), "44"),
    "44" : Msg("npc", _("I'm on the date with Micaela and she just told a super funny joke"), "444"),
    "444" : Msg("npc", _("But I couldn't think of a witty comeback"), "4"),
    "4" : Msg("npc", _("Please, tell me I can borrow your joke of the two friends and the crocodile"), ["5", "6"]),
    "5" : Msg("mc", _("Lmao sure bro, all yours"), "7"),
    "6" : Msg("mc", _("Bro, that's my joke {image=images/MENUS/e_sweat.png}\nTell one of yours"), "9"),
    "7" : Msg("npc", _("YES"), "8", actions="store.changborrowjoke=True"),
    "8" : Msg("npc", _("I knew I could count on you bro {image=images/MENUS/e_cry.png}"), "10"),
    "9" : Msg("npc", _("Dreams crumbled and hopes were shattered {image=images/MENUS/e_skull.png}"), "14"),
    "10" : Msg("npc", _("I'll give you credit, I swear!"), "11"),
    "11" : Msg("npc", _("See you tomorrow!! And say hi to Annie from me!"), "12"),
    "12" : Msg("mc", _("I will! Good luck, bro  {image=images/MENUS/e_strong.png}"), "13"),
    "13" : Msg("npc", _("I love you bro {image=images/MENUS/e_cry.png}")),
    "14" : Msg("npc", _("Tough but still fair"), "15"),
    "15" : Msg("npc", _("I'll try to think of something!"), "16"),
    "16" : Msg("npc", _("TTYL!")),
    }


define chang_chat3 = {
    "background" : "qqq 6",
    "thumbnail" : "chat_chang_1",
    "npc" : "Chang",
    "0" : Msg("npc", _("Operation Plug'n'Pray is ready to commence."), ["1"]),
    "1" : Msg("npc", _("Mia and I are in position."), "2"),
    "2" : Msg("npc", _("Elevator 7. Floors 2 and 14."), "3"),
    "3" : Msg("mc", _("Understood.")),
    }