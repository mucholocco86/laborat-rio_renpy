default board = [[None for _ in range(7)] for _ in range(6)]  
default current_player = "[mc]"  
default game_over = False
default move_count = 0
default winning_cells = []
default ai_difficulty = "simple" 
default maia_won_getfour = False
default mc_won_getfour = False
default draw_getfour = False

init python:
    import random
    

    def check_win(board, player):
        rows, cols = len(board), len(board[0])

        for row in range(rows):
            for col in range(cols - 3):
                if all(board[row][col + i] == player for i in range(4)):
                    return [(row, col+i) for i in range(4)]

        for col in range(cols):
            for row in range(rows - 3):
                if all(board[row + i][col] == player for i in range(4)):
                    return [(row+i, col) for i in range(4)]

        for row in range(rows - 3):
            for col in range(cols - 3):
                if all(board[row + i][col + i] == player for i in range(4)):
                    return [(row+i, col+i) for i in range(4)]

        for row in range(3, rows):
            for col in range(cols - 3):
                if all(board[row - i][col + i] == player for i in range(4)):
                    return [(row-i, col+i) for i in range(4)]
        return []

    def is_column_full(board, col):
        return board[0][col] is not None

    def drop_disc(board, col, player):
        """Place a disc in the lowest empty row of the selected column."""
        for row in reversed(range(len(board))):
            if board[row][col] is None:
                board[row][col] = player
                return row
        return -1

    def get_available_columns(board):
        return [col for col in range(7) if not is_column_full(board, col)]


    def evaluate_window(window, player):
        score = 0
        opponent = "[mc]" if player == "Maia" else "Maia"
        if window.count(player) == 4:
            score += 100
        elif window.count(player) == 3 and window.count(None) == 1:
            score += 5
        elif window.count(player) == 2 and window.count(None) == 2:
            score += 2
        if window.count(opponent) == 3 and window.count(None) == 1:
            score -= 4
        return score

    def evaluate_board(board):
        score = 0

        center_array = [board[r][3] for r in range(6)]
        center_count = center_array.count("Maia")
        score += center_count * 3

        for row in range(6):
            row_array = board[row]
            for col in range(7 - 3):
                window = row_array[col:col + 4]
                score += evaluate_window(window, "Maia")

        for col in range(7):
            col_array = [board[row][col] for row in range(6)]
            for row in range(6 - 3):
                window = col_array[row:row + 4]
                score += evaluate_window(window, "Maia")

        for row in range(6 - 3):
            for col in range(7 - 3):
                window = [board[row + i][col + i] for i in range(4)]
                score += evaluate_window(window, "Maia")

        for row in range(3, 6):
            for col in range(7 - 3):
                window = [board[row - i][col + i] for i in range(4)]
                score += evaluate_window(window, "Maia")
        return score

    def is_terminal_node(board):
        return (check_win(board, "Maia") or check_win(board, "[mc]") or len(get_available_columns(board)) == 0)


    def minimax(board, depth, maximizingPlayer, alpha, beta):
        terminal = is_terminal_node(board)
        if depth == 0 or terminal:
            if terminal:
                if check_win(board, "Maia"):
                    return (1000000, None)
                elif check_win(board, "[mc]"):
                    return (-1000000, None)
                else:
                    return (0, None)
            else:
                return (evaluate_board(board), None)
        if maximizingPlayer:
            value = -float("inf")
            best_move = None
            for col in get_available_columns(board):
                board_copy = [row[:] for row in board]
                drop_disc(board_copy, col, "Maia")
                new_score, _ = minimax(board_copy, depth - 1, False, alpha, beta)
                if new_score > value:
                    value = new_score
                    best_move = col
                alpha = max(alpha, value)
                if alpha >= beta:
                    break
            return (value, best_move)
        else:
            value = float("inf")
            best_move = None
            for col in get_available_columns(board):
                board_copy = [row[:] for row in board]
                drop_disc(board_copy, col, "[mc]")
                new_score, _ = minimax(board_copy, depth - 1, True, alpha, beta)
                if new_score < value:
                    value = new_score
                    best_move = col
                beta = min(beta, value)
                if alpha >= beta:
                    break
            return (value, best_move)

    def advanced_ai_move():

        score, move = minimax(board, 4, True, -float("inf"), float("inf"))
        return move

    def simple_ai_move():
        score, move = minimax(board, 2, True, -float("inf"), float("inf"))
        return move

    def ai_move():
        if game_over:
            return
        if ai_difficulty == "advanced":
            col = advanced_ai_move()
        else:
            col = simple_ai_move()
        if col is not None:
            make_move(col)

    def make_move(col):
        global board, current_player, game_over, move_count, winning_cells
        if game_over or is_column_full(board, col):
            return
        row = drop_disc(board, col, current_player)
        if row == -1:
            return
        move_count += 1

        winning_cells = check_win(board, current_player)
        if winning_cells:
            game_over = True
            if current_player == "Maia":
                store.maia_won_getfour = True
            else:
                store.mc_won_getfour = True

        elif move_count >= 42:
            game_over = True
            store.draw_getfour = True

        else:
            current_player = "Maia" if current_player == "[mc]" else "[mc]"
        renpy.restart_interaction()

    def reset_game():
        global board, current_player, game_over, move_count, winning_cells
        board = [[None for _ in range(7)] for _ in range(6)]
        current_player = "[mc]"
        game_over = False
        move_count = 0
        winning_cells = []
        renpy.restart_interaction()


transform pulse_glow:
    alpha 0.3
    block:
        easeout 0.8 alpha 0.6
        easein 0.8 alpha 0.3
        repeat

transform disc_bounce:
    yoffset 0
    easein 0.8 yoffset -10
    easeout 0.8 yoffset 0
    repeat

transform button_hover:
    on hover:
        easein 0.1 yoffset -3
    on idle:
        easein 0.1 yoffset 0

transform disc_drop:
    alpha 0.0 yoffset -100
    easein 0.3 alpha 1.0 yoffset 0

init python:
    def create_highlight(size):
        return Fixed(
            Transform(
                Solid("#ffffff40"),
                size=(size, size),
                anchor=(0.3, 0.3),
                fit="stretch"
            ),
            Transform(
                Solid("#ffffff20"),
                size=(size, size),
                anchor=(0.7, 0.7),
                fit="stretch"
            )
        )


screen getfour():
    frame:
        xpos 400
        ypos 350
        xysize (0, 0)
        vbox:
            spacing 30
            hbox:
                spacing 105
                xalign 0.5
                
                for col in range(7):
                    button:
                        action Function(make_move, col)
                        sensitive (current_player == "[mc]") and (not is_column_full(board, col)) and (not game_over)
                        xysize (50, 60)
                        ypos 30
                        xpos 30
                        background Solid("#cf436b83")
                        hover_background Solid("#80213c")
                        text "v":
                            color "#fff"
                            size 40
                            yalign 0.5
                            xalign 0.5
                        at button_hover
            
           
            frame:
                padding (15, 15)
                background Frame("gui/games/connect/connect_board2.png")
                xysize (1600, 800)
                xalign 0.5
                vbox:
                    spacing 40
                    for row in range(6):
                        hbox:
                            spacing 65
                            for col in range(7):
                                $ cell = board[row][col]
                                $ is_winning = (row, col) in winning_cells
                                frame:
                                    xpos 320
                                    ypos 30
                                    background Solid("#01589b00")
                                    padding (3, 3)
                                    xysize (85, 85)
                                    
                                    if cell is not None:
                                        add Solid(
                                            "#f44336" if cell == "[mc]" else "#ffeb3b",
                                            xsize=75,
                                            ysize=75,
                                            radius=37,
                                            alpha=0.3
                                        ) at disc_drop
                                        
                                        if is_winning:
                                            add Solid(
                                                "#00ff00",
                                                xsize=75,
                                                ysize=75,
                                                radius=37,
                                                alpha=0.3
                                            ) at pulse_glow
            
            
            hbox:
                xalign 0.5
                spacing 30
                frame:
                    background None
                    add Solid(
                        "#f44336" if current_player == "[mc]" else "#ffeb3b",
                        xsize=80,
                        ysize=80,
                        radius=40
                    ) at disc_bounce
                
                $ turn_text = "[mc]" if current_player == "[mc]" else "Maia"
                text turn_text:
                    size 40
                    color "#fff"
                    outlines [ (3, "#000", 0, 0) ]
                    xpos 0
                    ypos 10
            
            
            if game_over:
                timer 3.0 action If(store.maia_won_getfour, Jump("maia_won_getfour"), 
                                If(store.mc_won_getfour, Jump("mc_won_getfour"), 
                                If(store.draw_getfour, Jump("draw_getfour"))))

                #textbutton "PLAY AGAIN":
                    #action Function(reset_game)
                    #xalign 0.5
                    #background Solid("#4CAF50")
                    #hover_background Solid("#45a049")
                    #text_size 35
                    #text_color "#fff"
                    #text_outlines [ (3, "#000", 0, 0) ]
                    #padding (40, 15)
                    #at button_hover

    
    if current_player == "Maia" and not game_over:
        timer 1.0 action Function(ai_move)

default maia_games_first = True

label maia_getfour:
    $ maia_won_getfour = False
    $ mc_won_getfour = False
    $ draw_getfour = False
    if maia_games_first:
        mc "Wanna play?"
        if maia_sad:
            scene 18_s16 with dissolve
            m "N-No..."
            scene 18_s15 with dissolve
            call screen is_maia with dissolve
        $ maia_games_first = False
        scene 30_s10 with dissolve
        m "I do! I do!"
        scene 30_s11 with dissolve
        mc "Got some cards?"
        scene 18_s8 with dissolve
        m "Cards? Sorry, [mx], but no. I do have a {i}Get Four{/i} board somewhere lying around here, though!"
        scene 18_s7 with dissolve
        mc "{i}Get Four?{/i} Never heard of it."
        scene 18_s8 with dissolve
        m "It's really simple, [mx]. You just have to jam a cube inside a circle and connect four of them in a row—horizontally, vertically, or even diagonally!"
        scene 18_s7 with dissolve
        mc "Ah, I get it now."
        scene 18_s8 with dissolve
        m "Should we try to find it?"
        scene 18_s7 with dissolve
        mc "Sure. Let's get it on!"
        scene 30_s10 with dissolve
        m "Yes!"
        scene 30_s11 with dissolve
        scene 30_s1 with Fade(1.0,1.0,1.0)
        m "Umm... [mx]?"
        scene 30_s2 with dissolve
        mc "What's wrong? Is it broken?"
        scene 30_s1 with dissolve
        m "No, It's... how good are you at the game, [mx]?"
        scene 30_s2 with dissolve
        call screen getfour_diff with dissolve
    else:
        $ reset_game()
        scene 18_s8 with dissolve
        if maia_won_getfour_easy:
            $ maia_won_getfour_easy = False
            if maia_won_getfour_easy_counter >= 20:
                m "You're really dedicated, [mx]."
            elif maia_won_getfour_easy_counter >= 10:
                m "[mx]... Are you losing on purpose?"
            elif maia_won_getfour_easy_counter >= 5:
                m "I'll try going {i}really{/i} easy this time, [mx]..."
            elif maia_won_getfour_easy_counter >= 3:
                m "Maybe you should try a different strategy, [mx]?"
            elif maia_won_getfour_easy_counter >= 1:
                m "Care for a rematch?"
        elif maia_lost_getfour_easy:
                m "Good job on winning last time, [mx]! Maybe we can get... {i}serious{/i} now?"
                $ maia_lost_getfour_easy = False
        elif maia_won_getfour_hard:
            $ maia_won_getfour_hard = False
            if maia_won_getfour_hard_counter >= 20:
                m "I can tell you're trying really hard, [mx]. I love that."
            if maia_won_getfour_hard_counter >= 10:
                m "I hope you're at least having fun, [mx]. I can't imagine what losing so many times would do to me..."
            elif maia_won_getfour_hard_counter >= 5:
                m "Keep trying, [mx]! Never give up!"
            elif maia_won_getfour_hard_counter >= 3:
                m "You're getting better, [mx]. Don't let losing get to you."
            elif maia_won_getfour_hard_counter >= 1:
                m "Come to get revenge, [mx]?"
        elif maia_lost_getfour_hard:
            m "The champion of Get Four wants another match? I can't refuse such an offer~"
            $ maia_lost_getfour_hard = False
        else:
            m "Let's play, [mx]!"
        scene 18_s7 with dissolve
        call screen getfour_diff with dissolve

label maia_getfour_easy:
    $ ai_difficulty = "simple"
    $ current_player = "[mc]"
    mc "Go easy on me."
    scene 18_s8 with dissolve
    m "Of course, [mx]!"
    scene 18_s7 with dissolve
    scene 30_s15 with Fade(0.5,0.5,0.5)
    m "Let's begin."
    scene 30_s12 with dissolve
    call screen getfour with dissolve

label maia_getfour_hard:
    $ ai_difficulty = "advanced"
    mc "Don't hold back. Show me everything."
    scene 30_s13 with dissolve
    m "Oh? Alright~"
    scene 30_s14 with dissolve
    mc "What's with the smug look?"
    scene 30_s13 with dissolve
    m "Nothing~"
    scene 30_s14 with dissolve
    scene 30_s15 with Fade(0.5,0.5,0.5)
    m "Let's begin."
    scene 30_s12 with dissolve
    call screen getfour with dissolve

default maia_won_getfour_easy = False
default maia_won_getfour_easy_counter = 0
default maia_won_getfour_hard = False
default maia_won_getfour_hard_counter = 0

default maia_lost_getfour_easy = False
default maia_lost_getfour_easy_counter = 0
default maia_lost_getfour_hard = False
default maia_lost_getfour_hard_counter = 0

default maia_won_getfour_hard_second = False

label maia_won_getfour:
    if ai_difficulty == "simple":
        $ maia_won_getfour_easy = True
        $ maia_won_getfour_easy_counter += 1
        scene 18_s7 with fade
        mc "Are you sure you're going easy on me, Maia?"
        scene 18_s8 with dissolve
        m "I am, [mx]."
        scene 18_s7 with dissolve
        mc "Damn..."
        scene 18_s8 with dissolve
        m "Don't let it get to you! I have been playing this game since I was really young. It takes time to get good at it."
        scene 18_s7 with dissolve
    elif ai_difficulty == "advanced":
        $ maia_won_getfour_hard = True
        $ maia_won_getfour_hard_counter += 1
        if not maia_won_getfour_hard_second:
            $ maia_won_getfour_hard_second = True
            scene 18_s7 with fade
            mc "I lost..."
            scene 18_s8 with dissolve
            m "It's fine, [mx]! You were... good."
            scene 18_s7 with dissolve
            mc "What's that supposed to mean?"
            scene 18_s8 with dissolve
            m "Nothing~"
            scene 18_s7 with dissolve
        else:
            scene 18_s7 with fade
            mc "This is impossible!"
            scene 18_s8 with dissolve
            m "*laughs* Just keep trying, [mx]! You'll win eventually..."
            scene 18_s7 with dissolve
            mc "*sigh*"
    call screen is_maia with dissolve

default maia_lost_getfour_hard_sec = False

label mc_won_getfour:
    if ai_difficulty == "simple":
        $ maia_lost_getfour_easy = True
        $ maia_lost_getfour_easy_counter += 1
        scene 18_s7 with fade
        mc "I won!"
        scene 18_s8 with dissolve
        m "Good job, [mx]!"
        scene 18_s7 with dissolve
        mc "You were pretty good too." 
        scene 18_s8 with dissolve
        m "Thank you! So..."
        scene 18_s7 with dissolve
        mc "So...?"
        scene 30_s13 with dissolve
        m "Maybe you're ready to play me at {i}full power!{/i}"
        scene 30_s14 with dissolve
        mc "Oh right... I'll see about that."
        scene 30_s13 with dissolve
        m "I'll be waiting, {i}mwahaha!{/i}"
        scene 30_s14 with dissolve
    elif ai_difficulty == "advanced":
        $ maia_lost_getfour_hard = True
        $ maia_lost_getfour_hard_counter += 1
        if not maia_lost_getfour_hard_sec:
            scene 30_s7 with fade
            mc "Got you!"
            $ maia_lost_getfour_hard_sec = True
            m "..."
            mc "Maia?"
            scene 30_s6 with dissolve
            m "H-how?"
            scene 30_s7 with dissolve
            mc "What do you mean?"
            scene 30_s6 with dissolve
            m "This is... you... I..."
            scene 30_s7 with dissolve
            empathy "This game means more to her than she's letting on. The weight of losing is hitting her hard."
            mc "What's wrong, Maia? I finally won after all these attempts. You know why?"
            mc "Because I learned from the best."
            scene 18_s10 with dissolve
            m "[mx]..."
            m "It's fine... you don't have to console me. But... thank you."
            scene 18_s9 with dissolve
        else:
            scene 30_s10 with dissolve
            m "You continue to amaze me, [mx]!"
            m "Maybe one day you will compete against the best."
            scene 30_s11 with dissolve
            mc "Am I not already?"
            m "Mhmm~"
    call screen is_maia with dissolve


label draw_getfour:
    scene 18_s8 with fade
    m "Ah, it's a draw!"
    m "*chuckles* Again, again!"
    scene 18_s7 with dissolve
    call screen is_maia with dissolve