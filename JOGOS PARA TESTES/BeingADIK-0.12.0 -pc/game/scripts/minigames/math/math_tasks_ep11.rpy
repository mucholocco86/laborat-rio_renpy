label math_setup_ep11_label:
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
    def math_task1_ep11(task):
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
            math_grid.append([600,200,"base"])
            
            math_grid.append([400,300,"base"])
            math_grid.append([500,300,"base"])
            math_grid.append([600,300,"base"])
            math_grid.append([700,300,"base"])
            math_grid.append([800,300,"base"])
            
            math_grid.append([500,400,"base"])
            math_grid.append([600,400,"blue"])
            math_grid.append([700,400,"base"])
            
            math_grid.append([400,500,"base"])
            math_grid.append([500,500,"base"])
            math_grid.append([700,500,"base"])
            math_grid.append([800,500,"gray"])
            
            math_grid.append([500,600,"base"])
            math_grid.append([600,600,"base"])
            math_grid.append([700,600,"base"])
            
            math_grid.append([400,700,"orange"])
            math_grid.append([500,700,"base"])
            math_grid.append([600,700,"base"])
            math_grid.append([700,700,"base"])
            math_grid.append([800,700,"base"])
            
            math_grid.append([500,800,"base"])
            math_grid.append([600,800,"base"])
            math_grid.append([700,800,"pink"])
            
            math_diamond_position = []
            math_task_list = []
            tmpInt = renpy.random.randint(1,5)
            
            math_task_desc = ["Find 2","d"]
            
            if tmpInt == 1:
                math_diamond_position.append(9)
                math_diamond_position.append(10)
                math_task_list.append(["One is in the same column as one sphere",""])
                math_task_list.append(["Both are in the same row as a sphere",""])
                math_task_list.append(["Both are diagonal to ≥ 1 sphere",""])
                math_task_list.append(["They are = 1 step from each other",""])
                math_bomb_grid = [1,4,11,17,18]
            elif tmpInt == 2:
                math_diamond_position.append(18)
                math_diamond_position.append(22)
                math_task_list.append(["Both are ≥ 3 steps from","blue"])
                math_task_list.append(["They are in the same column",""])
                math_task_list.append(["One is = 1 step from","pink"])
                math_task_list.append(["One is = 2 steps from","orange"])
                math_bomb_grid = [1,4,11,17,19]
            elif tmpInt == 3:
                math_diamond_position.append(6)
                math_diamond_position.append(15)
                math_task_list.append(["One is ≤ 2 steps from","gray"])
                math_task_list.append(["They are diagonal to each other",""])
                math_task_list.append(["They are = 4 steps from each other",""])
                math_task_list.append(["Both are = 4 steps from","orange"])
                math_bomb_grid = [1,4,11,17,19]
            elif tmpInt == 4:
                math_diamond_position.append(0)
                math_diamond_position.append(14)
                math_task_list.append(["They are in the same column",""])
                math_task_list.append(["Neither is diagonal to a sphere",""])
                math_task_list.append(["Neither is in the same row as a sphere",""])
                math_task_list.append(["One is = 3 steps from three spheres",""])
                math_bomb_grid = [1,4,11,17,19]
            elif tmpInt == 5:
                math_diamond_position.append(14)
                math_diamond_position.append(22)
                math_task_list.append(["They are in the same column",""])
                math_task_list.append(["Neither is diagonal to a sphere",""])
                math_task_list.append(["One is in the same row as a sphere",""])
                math_task_list.append(["One is = 3 steps from three spheres",""])
                math_bomb_grid = [1,4,11,17,19]
        elif task == 2:
            math_d_count_total = 1
            math_grid = []
            math_grid.append([300,300,"base"])
            math_grid.append([400,300,"base"])
            
            math_grid.append([400,400,"base"])
            math_grid.append([500,400,"blue"])
            math_grid.append([600,400,"base"])
            math_grid.append([700,400,"base"])
            math_grid.append([800,400,"base"])
            math_grid.append([900,400,"blue"])
            
            math_grid.append([500,500,"base"])
            math_grid.append([800,500,"base"])
            math_grid.append([900,500,"base"])
            
            math_grid.append([500,600,"pink"])
            math_grid.append([600,600,"base"])
            math_grid.append([700,600,"base"])
            math_grid.append([800,600,"base"])
            math_grid.append([900,600,"base"])
            
            math_grid.append([500,700,"base"])
            math_grid.append([700,700,"base"])
            math_grid.append([900,700,"pink"])
            
            math_diamond_position = []
            math_task_list = []
            tmpInt = renpy.random.randint(1,5)
            
            math_task_desc = ["Find 1","d"]
            
            if tmpInt == 1:
                math_diamond_position.append(4)
                math_task_list.append(["It is diagonal to one sphere",""])
                math_task_list.append(["It is in the same row as ≥ 1 sphere",""])
                math_task_list.append(["It is = 3 steps from ≥ 1","blue"])
                math_task_list.append(["It is > 2 steps from","pink"])
                math_bomb_grid = [1,6,9,12,15]
            elif tmpInt == 2:
                math_diamond_position.append(17)
                math_task_list.append(["It is not diagonal to","pink"])
                math_task_list.append(["It is not in the same row as","blue"])
                math_task_list.append(["The closest sphere is ≥ 3 steps away",""])
                math_task_list.append(["It is in the same row as a sphere",""])
                math_bomb_grid = [1,6,9,12,15]
            elif tmpInt == 3:
                math_diamond_position.append(5)
                math_task_list.append(["It is > 1 step from","pink"])
                math_task_list.append(["It is > 1 step from","blue"])
                math_task_list.append(["It is diagonal to one sphere",""])
                math_task_list.append(["It is = 2 steps from two spheres",""])
                math_bomb_grid = [1,6,9,12,15]
            elif tmpInt == 4:
                math_diamond_position.append(17)
                math_task_list.append(["",""])
                math_task_list.append(["It is > 2 steps from","blue"])
                math_task_list.append(["It is not diagonal to a sphere",""])
                math_task_list.append(["It is = 5 steps from two spheres",""])
                math_bomb_grid = [1,6,9,12,15]
            elif tmpInt == 5:
                math_diamond_position.append(10)
                math_task_list.append(["It is ≤ 3 steps from","pink"])
                math_task_list.append(["It is in the same column as two spheres",""])
                math_task_list.append(["It is = 1 step from","blue"])
                math_task_list.append(["It is surrounded by > 3 empty tiles",""])
                math_bomb_grid = [1,6,9,12,15]
        elif task == 3:
            math_d_count_total = 3
            math_grid = []
            math_grid.append([200,200,"base"])
            math_grid.append([300,200,"gray"])
            math_grid.append([400,200,"base"])
            math_grid.append([500,200,"base"])
            math_grid.append([600,200,"base"])
            math_grid.append([700,200,"base"])
            math_grid.append([800,200,"base"])
            math_grid.append([900,200,"base"])
            math_grid.append([1000,200,"base"])
            
            math_grid.append([200,300,"base"])
            math_grid.append([300,300,"base"])
            math_grid.append([400,300,"orange"])
            math_grid.append([800,300,"base"])
            math_grid.append([900,300,"base"])
            math_grid.append([1000,300,"base"])
            
            math_grid.append([200,400,"base"])
            math_grid.append([300,400,"base"])
            math_grid.append([400,400,"base"])
            math_grid.append([800,400,"base"])
            math_grid.append([900,400,"base"])
            math_grid.append([1000,400,"base"])
            
            math_grid.append([200,500,"base"])
            math_grid.append([300,500,"base"])
            math_grid.append([400,500,"base"])
            math_grid.append([500,500,"base"])
            math_grid.append([600,500,"base"])
            math_grid.append([700,500,"base"])
            math_grid.append([800,500,"base"])
            math_grid.append([900,500,"base"])
            math_grid.append([1000,500,"orange"])
            
            math_grid.append([200,600,"base"])
            math_grid.append([300,600,"blue"])
            math_grid.append([400,600,"base"])
            math_grid.append([800,600,"pink"])
            math_grid.append([900,600,"base"])
            math_grid.append([1000,600,"base"])
            
            math_grid.append([200,700,"base"])
            math_grid.append([300,700,"base"])
            math_grid.append([400,700,"base"])
            math_grid.append([500,700,"base"])
            math_grid.append([600,700,"base"])
            math_grid.append([700,700,"base"])
            math_grid.append([800,700,"base"])
            math_grid.append([900,700,"base"])
            math_grid.append([1000,700,"base"])
            
            math_grid.append([200,800,"base"])
            math_grid.append([300,800,"base"])
            math_grid.append([400,800,"base"])
            math_grid.append([500,800,"base"])
            math_grid.append([600,800,"base"])
            math_grid.append([700,800,"blue"])
            math_grid.append([800,800,"base"])
            math_grid.append([900,800,"base"])
            math_grid.append([1000,800,"base"])
            
            math_diamond_position = []
            math_task_list = []
            tmpInt = renpy.random.randint(1,5)
            
            math_task_desc = ["Find 3","d"]
            
            if tmpInt == 1:
                math_diamond_position.append(38)
                math_diamond_position.append(40)
                math_diamond_position.append(42)
                math_task_list.append(["All are diagonal to ≥ 1 sphere",""])
                math_task_list.append(["One is < 3 steps from","pink"])
                math_task_list.append(["All are < 5 steps from","blue"])
                math_task_list.append(["All are > 1 steps from","blue"])
                math_task_list.append(["All are in the same row",""])
                math_task_list.append(["All can be reached in < 5 steps",""])
                math_bomb_grid = [0,8,16,25,30,43,46]
            elif tmpInt == 2:
                math_diamond_position.append(22)
                math_diamond_position.append(27)
                math_diamond_position.append(28)
                math_task_list.append(["One is = 1 step from","orange"])
                math_task_list.append(["One is = 1 step from","blue"])
                math_task_list.append(["One is = 1 step from","pink"])
                math_task_list.append(["All are in the same row",""])
                math_task_list.append(["One is = 3 steps from","gray"])
                math_bomb_grid = [0,8,16,25,30,43,46]
            elif tmpInt == 3:
                math_diamond_position.append(0)
                math_diamond_position.append(17)
                math_diamond_position.append(51)
                math_task_list.append(["All are diagonal to each other",""])
                math_task_list.append(["All are = 1 step from ≥ 1 sphere",""])
                math_task_list.append(["All are > 2 steps from each other",""])
                math_task_list.append(["Two are in the same row as = 1 sphere",""])
                math_bomb_grid = [3,8,16,25,30,43,46]
            elif tmpInt == 4:
                math_diamond_position.append(3)
                math_diamond_position.append(24)
                math_diamond_position.append(48)
                math_task_list.append(["All are in the same column",""])
                math_task_list.append(["All are > 2 steps from each other",""])
                math_task_list.append(["Two are diagonal to ≥ 1 sphere",""])
                math_task_list.append(["One is = 4 steps away from","pink"])
                math_task_list.append(["None are diagonal to","gray"])
                math_bomb_grid = [0,8,16,25,30,43,46]
            elif tmpInt == 5:
                math_diamond_position.append(10)
                math_diamond_position.append(43)
                math_diamond_position.append(47)
                math_task_list.append(["All are = 3 steps from","blue"])
                math_task_list.append(["They are not diagonal to each other",""])
                math_task_list.append(["They are not in the same row",""])
                math_task_list.append(["All are < 6 steps from","orange"])
                math_task_list.append(["One is = 2 steps from","pink"])
                math_task_list.append(["One is = 1 step from","gray"])
                math_bomb_grid = [0,8,16,25,30,42,46]
        elif task == 4:
            math_d_count_total = 2
            math_grid = []
            math_grid.append([200,200,"base"])
            math_grid.append([300,200,"base"])
            math_grid.append([400,200,"base"])
            math_grid.append([500,200,"base"])
            math_grid.append([600,200,"base"])
            math_grid.append([700,200,"base"])
            math_grid.append([800,200,"base"])
            math_grid.append([900,200,"base"])
            math_grid.append([1000,200,"base"])
            
            math_grid.append([200,300,"base"])
            math_grid.append([300,300,"base"])
            math_grid.append([400,300,"base"])
            math_grid.append([800,300,"base"])
            math_grid.append([900,300,"gray"])
            math_grid.append([1000,300,"blue"])
            
            math_grid.append([200,400,"base"])
            math_grid.append([300,400,"base"])
            math_grid.append([400,400,"base"])
            math_grid.append([800,400,"base"])
            math_grid.append([900,400,"base"])
            math_grid.append([1000,400,"base"])
            
            math_grid.append([200,500,"base"])
            math_grid.append([300,500,"base"])
            math_grid.append([400,500,"base"])
            math_grid.append([500,500,"base"])
            math_grid.append([600,500,"pink"])
            math_grid.append([700,500,"base"])
            math_grid.append([800,500,"base"])
            math_grid.append([900,500,"base"])
            math_grid.append([1000,500,"base"])
            
            math_grid.append([200,600,"base"])
            math_grid.append([300,600,"base"])
            math_grid.append([400,600,"base"])
            math_grid.append([800,600,"base"])
            math_grid.append([900,600,"base"])
            math_grid.append([1000,600,"base"])
            
            math_grid.append([200,700,"base"])
            math_grid.append([300,700,"orange"])
            math_grid.append([400,700,"base"])
            math_grid.append([500,700,"base"])
            math_grid.append([600,700,"base"])
            math_grid.append([700,700,"base"])
            math_grid.append([800,700,"base"])
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
                math_diamond_position.append(17)
                math_diamond_position.append(41)
                math_task_list.append(["Both are surrounded by 6 empty tiles",""])
                math_task_list.append(["They are diagonal to each other",""])
                math_task_list.append(["Both are = 4 steps from a sphere",""])
                math_task_list.append(["Neither is in the same column as a sphere",""])
                math_bomb_grid = [0,8,16,26,30,43,46]
            elif tmpInt == 2:
                math_diamond_position.append(12)
                math_diamond_position.append(38)
                math_task_list.append(["They are = 8 steps away from each other",""])
                math_task_list.append(["One is = 1 step from","gray"])
                math_task_list.append(["Both are = 1 step from a sphere",""])
                math_task_list.append(["They are diagonal to each other",""])
                math_bomb_grid = [0,8,16,26,30,43,46]
            elif tmpInt == 3:
                math_diamond_position.append(38)
                math_diamond_position.append(39)
                math_task_list.append(["They are = 1 step from each other",""])
                math_task_list.append(["One is = 1 step from a sphere",""])
                math_task_list.append(["Both are diagonal to ≥ 1 spheres",""])
                math_task_list.append(["Both are in the same row as ≥ 1 spheres",""])
                math_task_list.append(["One is diagonal to","pink"])
                math_bomb_grid = [0,8,16,26,30,43,46]
            elif tmpInt == 4:
                math_diamond_position.append(3)
                math_diamond_position.append(52)
                math_task_list.append(["",""])
                math_task_list.append(["They are > 5 steps from","blue"])
                math_task_list.append(["They are > 6 steps from","orange"])
                math_bomb_grid = [0,8,16,26,30,43,46]
            elif tmpInt == 5:
                math_diamond_position.append(9)
                math_diamond_position.append(40)
                math_task_list.append(["They are > 5 steps from","pink"])
                math_task_list.append(["They are in the same row as ≥ 1 sphere",""])
                math_task_list.append(["They are diagonal to each other",""])
                math_bomb_grid = [0,8,16,26,30,43,46]
        elif task == 5:
            math_d_count_total = 1
            math_grid = []
            math_grid.append([200,200,"gray"])
            math_grid.append([300,200,"base"])
            math_grid.append([400,200,"base"])
            math_grid.append([500,200,"base"])
            math_grid.append([600,200,"base"])
            math_grid.append([700,200,"base"])
            math_grid.append([800,200,"base"])
            math_grid.append([900,200,"base"])
            math_grid.append([1000,200,"blue"])
            
            math_grid.append([200,300,"base"])
            math_grid.append([300,300,"base"])
            math_grid.append([400,300,"base"])
            math_grid.append([500,300,"pink"])
            math_grid.append([600,300,"orange"])
            math_grid.append([700,300,"base"])
            math_grid.append([800,300,"base"])
            math_grid.append([900,300,"base"])
            math_grid.append([1000,300,"base"])
            
            math_grid.append([200,400,"base"])
            math_grid.append([300,400,"base"])
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
            math_grid.append([800,500,"base"])
            math_grid.append([900,500,"base"])
            math_grid.append([1000,500,"base"])
            
            math_grid.append([200,600,"base"])
            math_grid.append([300,600,"base"])
            math_grid.append([400,600,"base"])
            math_grid.append([500,600,"base"])
            math_grid.append([600,600,"gray"])
            math_grid.append([700,600,"base"])
            math_grid.append([800,600,"base"])
            math_grid.append([900,600,"base"])
            math_grid.append([1000,600,"base"])
            
            math_grid.append([200,700,"base"])
            math_grid.append([300,700,"base"])
            math_grid.append([400,700,"base"])
            math_grid.append([500,700,"base"])
            math_grid.append([600,700,"base"])
            math_grid.append([700,700,"base"])
            math_grid.append([800,700,"blue"])
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
            
            math_grid.append([200,900,"orange"])
            math_grid.append([300,900,"base"])
            math_grid.append([400,900,"base"])
            math_grid.append([500,900,"base"])
            math_grid.append([600,900,"base"])
            math_grid.append([700,900,"base"])
            math_grid.append([800,900,"base"])
            math_grid.append([900,900,"base"])
            math_grid.append([1000,900,"pink"])
            
            math_diamond_position = []
            math_task_list = []
            tmpInt = renpy.random.randint(1,5)
            
            math_task_desc = ["Find 1","d"]
            
            if tmpInt == 1:
                math_diamond_position.append(19)
                math_task_list.append(["It is not diagonal to a sphere",""])
                math_task_list.append(["It is not in the same row as a sphere",""])
                math_task_list.append(["It is not in the same column as a sphere",""])
                math_task_list.append(["It is = 3 steps from","gray"])
                math_bomb_grid = [1,14,15,35,42,57,64,67]
            elif tmpInt == 2:
                math_diamond_position.append(2)
                math_task_list.append(["It is ≤ 2 steps from","gray"])
                math_task_list.append(["It is diagonal to one sphere",""])
                math_task_list.append(["It is > 1 step from a sphere",""])
                math_bomb_grid = [1,14,15,35,42,57,64,67]
            elif tmpInt == 3:
                math_diamond_position.append(56)
                math_task_list.append(["It is diagonal to","blue"])
                math_task_list.append(["It is > 4 steps from","pink"])
                math_task_list.append(["It is not in the same row as a sphere",""])
                math_bomb_grid = [1,14,15,35,42,57,64,67]
            elif tmpInt == 4:
                math_diamond_position.append(17)
                math_task_list.append(["It is > 4 steps from","gray"])
                math_task_list.append(["It is = 1 step from a sphere",""])
                math_task_list.append(["It is in the same row as two spheres",""])
                math_task_list.append(["It is in the same column as two spheres",""])
                math_bomb_grid = [1,14,15,35,42,57,64,67]
            elif tmpInt == 5:
                math_diamond_position.append(10)
                math_task_list.append(["It is < 4 steps from","orange"])
                math_task_list.append(["It is < 4 steps from","gray"])
                math_task_list.append(["It is > 5 steps from","blue"])
                math_task_list.append(["It is = 2 steps from","pink"])
                math_task_list.append(["It is diagonal to two spheres",""])
                math_bomb_grid = [1,14,15,35,42,57,64,67]
        else:
            math_calc_result()
        return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
