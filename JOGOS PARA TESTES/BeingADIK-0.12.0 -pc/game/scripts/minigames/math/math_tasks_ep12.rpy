label math_setup_ep12_label:
    $ math_task_total = 5
    $ math_task = 0
    $ math_task_correct_answers = []
    $ math_query_info = []
    $ math_grid = []
    $ math_active_tool = 0
    $ math_b_count = 2
    $ math_query_count = 2
    $ math_query_count_total = 2
    $ math_b_count_total = 2
    $ math_next_task()
    $ math_rew = False
    $ renpy.jump(math_jump_label)

init python:
    def math_task1_ep12(task):
        global math_d_count_total
        global math_d_count
        global math_task
        
        global math_grid
        global math_bomb_grid
        global math_task_list
        global math_diamond_position
        global math_task_desc
        global math_bomb_used
        global math_query_info
        
        math_task = task
        math_d_count = 0
        math_bomb_used = False
        math_bomb_grid = []
        math_query_info = []
        if task == 1:
            math_d_count_total = 2
            math_grid = []
            math_grid.append([400,200,"base"])
            math_grid.append([500,200,"base"])
            math_grid.append([600,200,"base"])
            math_grid.append([700,200,"base"])
            math_grid.append([800,200,"base"])
            
            math_grid.append([400,300,"base"])
            math_grid.append([600,300,"base"])
            math_grid.append([700,300,"blue"])
            math_grid.append([800,300,"base"])
            
            math_grid.append([400,400,"base"])
            math_grid.append([500,400,"pink"])
            math_grid.append([600,400,"base"])
            math_grid.append([700,400,"base"])
            math_grid.append([800,400,"base"])
            
            math_grid.append([400,500,"base"])
            math_grid.append([500,500,"base"])
            math_grid.append([600,500,"base"])
            math_grid.append([700,500,"base"])
            
            math_grid.append([400,600,"base"])
            math_grid.append([500,600,"base"])
            math_grid.append([600,600,"base"])
            math_grid.append([700,600,"base"])
            math_grid.append([800,600,"base"])
            
            math_grid.append([400,700,"base"])
            math_grid.append([500,700,"blue"])
            math_grid.append([700,700,"base"])
            math_grid.append([800,700,"base"])
            
            math_grid.append([400,800,"base"])
            math_grid.append([500,800,"base"])
            math_grid.append([600,800,"base"])
            math_grid.append([700,800,"base"])
            math_grid.append([800,800,"base"])
            
            math_diamond_position = []
            math_task_list = []
            tmpInt = renpy.random.randint(1,5)
            
            math_task_desc = ["Find 2","d"]
            
            if tmpInt == 1:
                math_diamond_position.append(3)
                math_diamond_position.append(17)
                math_task_list.append(["One is = 1 step from a sphere",""])
                math_task_list.append(["Neither are horizontal to a sphere",""])
                math_task_list.append(["They are = 3 steps from each other",""])
                math_task_list.append(["They are in the same column",""])
                math_bomb_grid = [14,15,18,19,28]
            elif tmpInt == 2:
                math_diamond_position.append(4)
                math_diamond_position.append(26)
                math_task_list.append(["They are = 7 steps from each other",""])
                math_task_list.append(["Both are diagonal to ≥ 1 sphere",""])
                math_task_list.append(["One is horizontal to a sphere",""])
                math_task_list.append(["They are in the same column",""])
                math_task_list.append(["They are > 2 steps from","pink"])
                math_bomb_grid = [6,11,12,18,19]
            elif tmpInt == 3:
                math_diamond_position.append(0)
                math_diamond_position.append(22)
                math_task_list.append(["Both are > 2 steps from a sphere",""])
                math_task_list.append(["They are diagonal to each other",""])
                math_task_list.append(["They are > 2 steps from each other",""])
                math_bomb_grid = [1,4,18,26,31]
            elif tmpInt == 4:
                math_diamond_position.append(1)
                math_diamond_position.append(19)
                math_task_list.append(["They are vertical to each other",""])
                math_task_list.append(["Neither are diagonal to a sphere",""])
                math_task_list.append(["Neither are horizontal to a sphere",""])
                math_task_list.append(["They are = 6 steps from each other",""])
                math_bomb_grid = [2,15,18,20,21]
            elif tmpInt == 5:
                math_diamond_position.append(21)
                math_diamond_position.append(26)
                math_task_list.append(["One is horizontal to a sphere",""])
                math_task_list.append(["They are diagonal to each other",""])
                math_task_list.append(["They are > 2 steps from","pink"])
                math_task_list.append(["One is = 3 steps from two spheres",""])
                math_bomb_grid = [1,5,11,17,19]
        elif task == 2:
            math_d_count_total = 2
            math_grid = []
            math_grid.append([400,300,"base"])
            math_grid.append([500,300,"base"])
            math_grid.append([600,300,"base"])
            math_grid.append([700,300,"base"])
            math_grid.append([800,300,"base"])
            math_grid.append([900,300,"base"])
            
            math_grid.append([400,400,"base"])
            math_grid.append([500,400,"base"])
            math_grid.append([600,400,"base"])
            math_grid.append([700,400,"base"])
            math_grid.append([800,400,"pink"])
            math_grid.append([900,400,"base"])
            
            math_grid.append([400,500,"base"])
            math_grid.append([500,500,"base"])
            math_grid.append([800,500,"base"])
            math_grid.append([900,500,"base"])
            
            math_grid.append([400,600,"pink"])
            math_grid.append([500,600,"base"])
            math_grid.append([800,600,"base"])
            math_grid.append([900,600,"base"])
            
            math_grid.append([400,700,"base"])
            math_grid.append([500,700,"base"])
            math_grid.append([600,700,"base"])
            math_grid.append([700,700,"pink"])
            math_grid.append([800,700,"base"])
            math_grid.append([900,700,"base"])
            
            math_grid.append([400,800,"base"])
            math_grid.append([500,800,"base"])
            math_grid.append([600,800,"base"])
            math_grid.append([700,800,"base"])
            math_grid.append([800,800,"base"])
            math_grid.append([900,800,"base"])
            math_diamond_position = []
            math_task_list = []
            tmpInt = renpy.random.randint(1,5)
            
            
            math_task_desc = ["Find 2","d"]
            
            if tmpInt == 1:
                math_diamond_position.append(0)
                math_diamond_position.append(1)
                math_task_list.append(["Both are > 2 steps from","pink"])
                math_task_list.append(["They are horizontal to each other",""])
                math_task_list.append(["One is > 3 steps from","pink"])
                math_task_list.append(["One is vertical to","pink"])
                math_bomb_grid = [2,6,9,12,26]
            elif tmpInt == 2:
                math_diamond_position.append(7)
                math_diamond_position.append(27)
                math_task_list.append(["They are = 4 steps from each other",""])
                math_task_list.append(["They are > 2 steps from","pink"])
                math_task_list.append(["They are vertical to each other",""])
                math_bomb_grid = [0,6,13,17,31]
            elif tmpInt == 3:
                math_diamond_position.append(20)
                math_diamond_position.append(24)
                math_task_list.append(["Both are = 1 step from","pink"])
                math_task_list.append(["Both are vertical to","pink"])
                math_task_list.append(["They are = 4 steps from each other",""])
                math_task_list.append(["Both are horizontal to","pink"])
                math_task_list.append(["Both are horizontal to each other",""])
                math_bomb_grid = [4,6,15,21,29]
            elif tmpInt == 4:
                math_diamond_position.append(1)
                math_diamond_position.append(24)
                math_task_list.append(["Both are surrounded by > 4 empty tiles",""])
                math_task_list.append(["Neither are diagonal to","pink"])
                math_task_list.append(["They are = 7 steps from each other",""])
                math_task_list.append(["One is vertical to","pink"])
                math_bomb_grid = [2,7,9,25,31]
            elif tmpInt == 5:
                math_diamond_position.append(6)
                math_diamond_position.append(30)
                math_task_list.append(["Both are = 2 steps from","pink"])
                math_task_list.append(["They are diagonal to each other",""])
                math_task_list.append(["Both are vertical to","pink"])
                math_bomb_grid = [5,11,12,26,31]
        elif task == 3:
            math_d_count_total = 3
            math_grid = []
            math_grid.append([200,200,"base"])
            math_grid.append([300,200,"base"])
            math_grid.append([400,200,"base"])
            math_grid.append([500,200,"base"])
            math_grid.append([600,200,"base"])
            math_grid.append([800,200,"base"])
            math_grid.append([900,200,"base"])
            math_grid.append([1000,200,"base"])
            
            math_grid.append([200,300,"base"])
            math_grid.append([400,300,"base"])
            math_grid.append([500,300,"base"])
            math_grid.append([600,300,"base"])
            math_grid.append([800,300,"orange"])
            math_grid.append([900,300,"base"])
            math_grid.append([1000,300,"base"])
            
            math_grid.append([200,400,"base"])
            math_grid.append([300,400,"gray"])
            math_grid.append([400,400,"base"])
            math_grid.append([500,400,"base"])
            math_grid.append([600,400,"base"])
            math_grid.append([800,400,"base"])
            math_grid.append([900,400,"base"])
            math_grid.append([1000,400,"base"])
            
            math_grid.append([500,500,"base"])
            math_grid.append([600,500,"base"])
            math_grid.append([700,500,"gray"])
            math_grid.append([800,500,"base"])
            math_grid.append([900,500,"base"])
            math_grid.append([1000,500,"base"])
            
            math_grid.append([200,600,"base"])
            math_grid.append([300,600,"base"])
            math_grid.append([400,600,"orange"])
            math_grid.append([500,600,"base"])
            math_grid.append([600,600,"base"])
            math_grid.append([700,600,"base"])
            
            math_grid.append([200,700,"base"])
            math_grid.append([300,700,"base"])
            math_grid.append([400,700,"base"])
            math_grid.append([500,700,"base"])
            math_grid.append([600,700,"base"])
            math_grid.append([700,700,"base"])
            math_diamond_position = []
            math_task_list = []
            tmpInt = renpy.random.randint(1,5)
            
            
            math_task_desc = ["Find 3","d"]
            
            if tmpInt == 1:
                math_diamond_position.append(7)
                math_diamond_position.append(13)
                math_diamond_position.append(38)
                math_task_list.append(["All are diagonal to ≥ 1 sphere",""])
                math_task_list.append(["None are vertical to","orange"])
                math_task_list.append(["All are > 3 steps from","gray"])
                math_task_list.append(["All are diagonal to each other",""])
                math_bomb_grid = [0,3,6,22,24,26,36]
            elif tmpInt == 2:
                math_diamond_position.append(6)
                math_diamond_position.append(24)
                math_diamond_position.append(37)
                math_task_list.append(["One is = 1 step from","orange"])
                math_task_list.append(["One is = 1 step from","gray"])
                math_task_list.append(["Two are > 4 steps from","gray"])
                math_task_list.append(["All are diagonal to each other",""])
                math_bomb_grid = [3,4,23,26,32,33,34]
            elif tmpInt == 3:
                math_diamond_position.append(1)
                math_diamond_position.append(4)
                math_diamond_position.append(5)
                math_task_list.append(["All are horizontal to each other",""])
                math_task_list.append(["All are > 2 steps from each other",""])
                math_task_list.append(["Two are vertical to = 1 sphere",""])
                math_bomb_grid = [0,2,6,7,8,10,17]
            elif tmpInt == 4:
                math_diamond_position.append(18)
                math_diamond_position.append(23)
                math_diamond_position.append(38)
                math_task_list.append(["All are vertical to each other",""])
                math_task_list.append(["All are = 2 steps from ≥ 1 sphere",""])
                math_task_list.append(["Two are = 2 steps from","gray"])
                math_bomb_grid = [8,10,17,24,26,29,30]
            elif tmpInt == 5:
                math_diamond_position.append(15)
                math_diamond_position.append(19)
                math_diamond_position.append(21)
                math_task_list.append(["All are horizontal to each other",""])
                math_task_list.append(["All are in the same row as one","gray"])
                math_task_list.append(["One is = 2 steps from","orange"])
                math_task_list.append(["All are > 2 steps from each other",""])
                math_task_list.append(["All are diagonal to","orange"])
                math_bomb_grid = [0,8,17,18,23,24,28]
        elif task == 4:
            math_d_count_total = 2
            math_grid = []
            math_grid.append([200,200,"base"])
            math_grid.append([300,200,"base"])
            math_grid.append([400,200,"blue"])
            math_grid.append([500,200,"base"])
            math_grid.append([600,200,"base"])
            math_grid.append([700,200,"gray"])
            math_grid.append([800,200,"base"])
            math_grid.append([900,200,"orange"])
            math_grid.append([1000,200,"base"])
            
            math_grid.append([200,300,"base"])
            math_grid.append([300,300,"base"])
            math_grid.append([400,300,"base"])
            math_grid.append([500,300,"base"])
            math_grid.append([600,300,"base"])
            math_grid.append([700,300,"base"])
            math_grid.append([800,300,"base"])
            math_grid.append([900,300,"base"])
            math_grid.append([1000,300,"base"])
            
            math_grid.append([200,400,"base"])
            math_grid.append([300,400,"pink"])
            math_grid.append([400,400,"base"])
            math_grid.append([500,400,"base"])
            math_grid.append([600,400,"base"])
            math_grid.append([700,400,"base"])
            math_grid.append([800,400,"base"])
            math_grid.append([900,400,"base"])
            math_grid.append([1000,400,"base"])
            
            math_grid.append([200,500,"base"])
            math_grid.append([300,500,"base"])
            math_grid.append([400,500,"base"])
            math_grid.append([500,500,"base"])
            math_grid.append([600,500,"base"])
            math_grid.append([700,500,"base"])
            math_grid.append([800,500,"pink"])
            math_grid.append([900,500,"base"])
            math_grid.append([1000,500,"base"])
            
            math_grid.append([200,600,"base"])
            math_grid.append([300,600,"base"])
            math_grid.append([400,600,"orange"])
            math_grid.append([500,600,"base"])
            math_grid.append([600,600,"base"])
            math_grid.append([700,600,"base"])
            math_grid.append([800,600,"base"])
            math_grid.append([900,600,"base"])
            math_grid.append([1000,600,"base"])
            
            math_grid.append([200,700,"base"])
            math_grid.append([300,700,"base"])
            math_grid.append([400,700,"blue"])
            math_grid.append([500,700,"base"])
            math_grid.append([600,700,"base"])
            math_grid.append([700,700,"base"])
            math_grid.append([800,700,"gray"])
            math_grid.append([900,700,"base"])
            math_grid.append([1000,700,"base"])
            
            math_grid.append([200,800,"base"])
            math_grid.append([300,800,"base"])
            math_grid.append([400,800,"base"])
            math_grid.append([500,800,"base"])
            math_grid.append([600,800,"base"])
            math_grid.append([700,800,"base"])
            math_grid.append([800,800,"base"])
            math_grid.append([900,800,"base"])
            math_grid.append([1000,800,"base"])
            math_diamond_position = []
            math_task_list = []
            tmpInt = renpy.random.randint(1,5)
            
            
            math_task_desc = ["Find 2","d"]
            
            if tmpInt == 1:
                math_diamond_position.append(20)
                math_diamond_position.append(60)
                math_task_list.append(["They are diagonal to each other",""])
                math_task_list.append(["Both are = 1 step from a sphere",""])
                math_task_list.append(["Both are vertical to ≥ 2 spheres",""])
                math_task_list.append(["One is = 2 steps from ≥ 2 spheres",""])
                math_bomb_grid = [23,24,27,34,53,57,58]
            elif tmpInt == 2:
                math_diamond_position.append(1)
                math_diamond_position.append(52)
                math_task_list.append(["They are = 11 steps away from each other",""])
                math_task_list.append(["One is = 1 step from","gray"])
                math_task_list.append(["Both are = 1 step from a sphere",""])
                math_task_list.append(["Both are > 3 steps from","orange"])
                math_task_list.append(["Both are vertical to = 1 sphere",""])
                math_bomb_grid = [0,3,20,25,30,43,60]
            elif tmpInt == 3:
                math_diamond_position.append(28)
                math_diamond_position.append(37)
                math_task_list.append(["They are = 1 step from each other",""])
                math_task_list.append(["Both are = 1 step from a sphere",""])
                math_task_list.append(["Both are diagonal to ≥ 1 sphere",""])
                math_task_list.append(["One is diagonal to","orange"])
                math_task_list.append(["One is diagonal to","blue"])
                math_task_list.append(["One is horizontal to","pink"])
                math_bomb_grid = [0,3,20,25,39,43,60]
            elif tmpInt == 4:
                math_diamond_position.append(9)
                math_diamond_position.append(54)
                math_task_list.append(["They are > 5 steps from","gray"])
                math_task_list.append(["They are > 3 steps from","orange"])
                math_task_list.append(["Neither are horizontal to a sphere",""])
                math_bomb_grid = [0,8,18,25,30,43,46]
            elif tmpInt == 5:
                math_diamond_position.append(6)
                math_diamond_position.append(46)
                math_task_list.append(["They are vertical to ≥ 1 sphere",""])
                math_task_list.append(["They are horizontal to > 1 sphere",""])
                math_task_list.append(["They are diagonal to each other",""])
                math_task_list.append(["Both are = 1 step from ≥ 1 sphere",""])
                math_bomb_grid = [8,9,16,25,30,43,48]
        elif task == 5:
            math_d_count_total = 1
            math_grid = []
            math_grid.append([200,200,"base"])
            math_grid.append([300,200,"base"])
            math_grid.append([400,200,"base"])
            math_grid.append([500,200,"base"])
            math_grid.append([700,200,"base"])
            math_grid.append([800,200,"base"])
            math_grid.append([900,200,"base"])
            math_grid.append([1000,200,"base"])
            
            math_grid.append([200,300,"base"])
            math_grid.append([300,300,"blue"])
            math_grid.append([400,300,"base"])
            math_grid.append([500,300,"base"])
            math_grid.append([700,300,"pink"])
            math_grid.append([800,300,"base"])
            math_grid.append([900,300,"gray"])
            math_grid.append([1000,300,"base"])
            
            math_grid.append([200,400,"base"])
            math_grid.append([400,400,"orange"])
            math_grid.append([500,400,"base"])
            math_grid.append([600,400,"base"])
            math_grid.append([700,400,"base"])
            math_grid.append([800,400,"base"])
            math_grid.append([1000,400,"base"])
            
            math_grid.append([200,500,"base"])
            math_grid.append([300,500,"base"])
            math_grid.append([400,500,"base"])
            math_grid.append([500,500,"base"])
            math_grid.append([600,500,"base"])
            math_grid.append([700,500,"base"])
            math_grid.append([800,500,"base"])
            math_grid.append([900,500,"base"])
            math_grid.append([1000,500,"base"])
            
            math_grid.append([200,600,"base"])
            math_grid.append([300,600,"base"])
            math_grid.append([400,600,"base"])
            math_grid.append([500,600,"base"])
            math_grid.append([700,600,"base"])
            math_grid.append([800,600,"base"])
            math_grid.append([900,600,"blue"])
            math_grid.append([1000,600,"base"])
            
            math_grid.append([200,700,"base"])
            math_grid.append([300,700,"base"])
            math_grid.append([400,700,"base"])
            math_grid.append([500,700,"gray"])
            math_grid.append([700,700,"base"])
            math_grid.append([800,700,"base"])
            math_grid.append([900,700,"pink"])
            math_grid.append([1000,700,"base"])
            
            math_grid.append([200,800,"base"])
            math_grid.append([300,800,"base"])
            math_grid.append([400,800,"base"])
            math_grid.append([500,800,"base"])
            math_grid.append([700,800,"base"])
            math_grid.append([800,800,"base"])
            math_grid.append([900,800,"base"])
            math_grid.append([1000,800,"base"])
            math_diamond_position = []
            math_task_list = []
            tmpInt = renpy.random.randint(1,5)
            
            math_task_desc = ["Find 1","d"]
            
            if tmpInt == 1:
                math_diamond_position.append(27)
                math_task_list.append(["It is not diagonal to a sphere",""])
                math_task_list.append(["It is not horizontal to a sphere",""])
                math_task_list.append(["It is not vertical to a sphere",""])
                math_task_list.append(["It is = 3 steps from","gray"])
                math_bomb_grid = [1,15,16,23,32,35,48,52]
            elif tmpInt == 2:
                math_diamond_position.append(20)
                math_task_list.append(["It is ≤ 3 steps from","gray"])
                math_task_list.append(["It is diagonal to one sphere",""])
                math_task_list.append(["It is = 1 step from a sphere",""])
                math_bomb_grid = [1,15,16,22,31,35,48,52]
            elif tmpInt == 3:
                math_diamond_position.append(0)
                math_task_list.append(["It is diagonal to","blue"])
                math_task_list.append(["It is not vertical to a sphere",""])
                math_task_list.append(["It is not horizontal to a sphere",""])
                math_task_list.append(["It is > 4 steps from","pink"])
                math_bomb_grid = [1,15,16,23,32,35,48,52]
            elif tmpInt == 4:
                math_diamond_position.append(45)
                math_task_list.append(["It is > 4 steps from","gray"])
                math_task_list.append(["It is = 1 step from a sphere",""])
                math_task_list.append(["It is horizontal to two spheres",""])
                math_task_list.append(["It is = 7 steps from","orange"])
                math_bomb_grid = [1,15,16,23,32,35,47,52]
            elif tmpInt == 5:
                math_diamond_position.append(27)
                math_task_list.append(["It is < 4 steps from","pink"])
                math_task_list.append(["It is = 4 steps from","blue"])
                math_task_list.append(["It is not vertical to a sphere",""])
                math_task_list.append(["It is not horizontal to a sphere",""])
                math_bomb_grid = [1,15,16,23,32,35,48,52]
        else:
            math_calc_result()
        return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
