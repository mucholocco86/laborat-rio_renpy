label math_setup_ep10_label:
    $ math_task_total = 5
    $ math_task = 0
    $ math_task_correct_answers = []
    $ math_query_info = []
    $ math_active_tool = 0
    $ math_b_count = 2
    $ math_query_count = 2
    $ math_query_count_total = 2
    $ math_b_count_total = 2
    $ math_next_task()
    $ math_rew = False

    $ math_tt = []
    $ math_tt.append("This is a visual tool that helps you keep track of your conclusions. Click an empty tile to mark it with an \'X\'. It's recommended to mark tiles that cannot contain a diamond with \'X\'.")
    $ math_tt.append("This is a visual tool that helps you keep track of your conclusions. Click an empty tile to mark it with a \'?\'. It's recommended to mark tiles that may contain a diamond with \'?\'.")
    $ math_tt.append("Use the bomb tool to remove tiles that don't contain a diamond. It makes the current task easier to solve. The bomb tool has a limited number of uses per math class. Click it twice to use it.")
    $ math_tt.append("Place diamonds where you think they are hiding. Read the task information above to deduce where the diamonds are hiding. Click this tool and then a tile to make your guess.")
    $ math_tt.append("When you have placed all diamonds, click next to continue. Ensure you're happy with your diamond placement before clicking this button. You cannot go back after you click next.")
    $ math_tt.append("The query tool allows you to check if your current guess is correct. The query tool has a limited number of uses per math class. Click it twice to use it. You must have entered a guess for it to work.")
    $ renpy.jump(math_jump_label)

init python:
    def math_tut_ep10():
        global math_d_count_total
        global math_d_count
        
        global math_grid
        global math_bomb_grid
        global math_task_list
        global math_diamond_position
        global math_task_desc
        global math_bomb_used
        global math_query_info
        math_d_count = 0
        math_bomb_used = False
        math_bomb_grid = []
        math_query_info = []
        
        math_d_count_total = 1
        math_grid = []
        math_grid.append([600,300,"base"])
        math_grid.append([500,400,"blue"])
        math_grid.append([600,400,"base"])
        math_grid.append([700,400,"base"])
        math_grid.append([400,500,"base"])
        math_grid.append([500,500,"base"])
        math_grid.append([600,500,"pink"])
        math_grid.append([700,500,"base"])
        math_grid.append([800,500,"orange"])
        math_grid.append([500,600,"base"])
        math_grid.append([600,600,"base"])
        math_grid.append([700,600,"base"])
        math_grid.append([600,700,"base"])
        
        math_diamond_position = []
        math_task_list = []
        math_task_desc = ["Find 1","d"]
        math_diamond_position.append(0)
        math_task_list.append(["",""])
        math_task_list.append(["It is ≤ 2 steps from","blue"])
        math_task_list.append(["It is in the same column as","pink"])
        math_task_list.append(["It is not within 3 steps of","orange"])
        math_bomb_grid = [2,4,7,9,10]
        return
    def math_task1_ep10(task):
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
            math_d_count_total = 1
            math_grid = []
            math_grid.append([600,300,"base"])
            math_grid.append([500,400,"blue"])
            math_grid.append([600,400,"base"])
            math_grid.append([700,400,"base"])
            math_grid.append([400,500,"base"])
            math_grid.append([500,500,"base"])
            math_grid.append([600,500,"pink"])
            math_grid.append([700,500,"base"])
            math_grid.append([800,500,"orange"])
            math_grid.append([500,600,"base"])
            math_grid.append([600,600,"base"])
            math_grid.append([700,600,"base"])
            math_grid.append([600,700,"base"])
            
            math_diamond_position = []
            math_task_list = []
            tmpInt = renpy.random.randint(1,9)
            math_task_desc = ["Find 1","d"]
            
            if tmpInt == 1:
                math_diamond_position.append(2)
                math_task_list.append(["",""])
                math_task_list.append(["It is ≤ 2 steps from","blue"])
                math_task_list.append(["It is within 3 steps of","orange"])
                math_task_list.append(["It is in the same column as","pink"])
                math_bomb_grid = [3,4,7,9,10]
            elif tmpInt == 2:
                math_diamond_position.append(3)
                math_task_list.append(["",""])
                math_task_list.append(["It is ≤ 2 steps from","blue"])
                math_task_list.append(["It is within 3 steps of","orange"])
                math_task_list.append(["It is diagonal to","pink"])
                math_bomb_grid = [4,5,10,11,12]
            elif tmpInt == 3:
                math_diamond_position.append(4)
                math_task_list.append(["",""])
                math_task_list.append(["It is ≤ 2 steps from","blue"])
                math_task_list.append(["It is not within 3 steps of","orange"])
                math_task_list.append(["It is in the same row as","pink"])
                math_bomb_grid = [0,3,5,9,10]
            elif tmpInt == 4:
                math_diamond_position.append(5)
                math_task_list.append(["",""])
                math_task_list.append(["It is ≤ 2 steps from","blue"])
                math_task_list.append(["It is within 3 steps of","orange"])
                math_task_list.append(["It is in the same row as","pink"])
                math_bomb_grid = [0,2,4,9,10]
            elif tmpInt == 5:
                math_diamond_position.append(7)
                math_task_list.append(["",""])
                math_task_list.append(["It is ≥ 2 steps from","blue"])
                math_task_list.append(["It is within 3 steps of","orange"])
                math_task_list.append(["It is in the same row as","pink"])
                math_bomb_grid = [0,2,4,5,10]
            elif tmpInt == 6:
                math_diamond_position.append(9)
                math_task_list.append(["",""])
                math_task_list.append(["It is ≤ 2 steps from","blue"])
                math_task_list.append(["It is not within 3 steps of","orange"])
                math_task_list.append(["It is diagonal to","pink"])
                math_bomb_grid = [0,2,4,5,7]
            elif tmpInt == 7:
                math_diamond_position.append(10)
                math_task_list.append(["",""])
                math_task_list.append(["It is not within 2 steps of","blue"])
                math_task_list.append(["It is within 3 steps of","orange"])
                math_task_list.append(["It is in the same column as","pink"])
                math_bomb_grid = [0,2,4,5,7]
            elif tmpInt == 8:
                math_diamond_position.append(11)
                math_task_list.append(["",""])
                math_task_list.append(["It is not within 2 steps of","blue"])
                math_task_list.append(["It is within 3 steps of","orange"])
                math_task_list.append(["It is = 2 steps from","pink"])
                math_bomb_grid = [0,2,4,5,7]
            elif tmpInt == 9:
                math_diamond_position.append(12)
                math_task_list.append(["",""])
                math_task_list.append(["It is not within 2 steps of","blue"])
                math_task_list.append(["It is not within 3 steps of","orange"])
                math_task_list.append(["It is = 2 steps from","pink"])
                math_bomb_grid = [0,2,4,5,7]
        elif task == 2:
            math_d_count_total = 2
            math_grid = []
            math_grid.append([600,300,"base"])
            math_grid.append([500,400,"blue"])
            math_grid.append([600,400,"base"])
            math_grid.append([700,400,"base"])
            math_grid.append([400,500,"base"])
            math_grid.append([500,500,"base"])
            math_grid.append([600,500,"base"])
            math_grid.append([700,500,"base"])
            math_grid.append([800,500,"base"])
            math_grid.append([500,600,"base"])
            math_grid.append([600,600,"base"])
            math_grid.append([700,600,"gray"])
            math_grid.append([600,700,"base"])
            
            math_diamond_position = []
            math_task_list = []
            tmpInt = renpy.random.randint(0,4)
            math_task_desc = ["Find 2","d"]
            
            if tmpInt == 0:
                math_diamond_position.append(0)
                math_diamond_position.append(4)
                math_task_list.append(["",""])
                math_task_list.append(["Both are diagonal to one sphere",""])
                math_task_list.append(["Both are diagonal to each other",""])
                math_task_list.append(["Both are > 2 steps from","gray"])
                math_bomb_grid = [2,3,7,9,10]
            elif tmpInt == 1:
                math_diamond_position.append(0)
                math_diamond_position.append(4)
                math_task_list.append(["",""])
                math_task_list.append(["Both are = 2 steps from","blue"])
                math_task_list.append(["Both are > 2 steps from","gray"])
                math_bomb_grid = [2,3,7,9,10]
            elif tmpInt == 2:
                math_diamond_position.append(10)
                math_diamond_position.append(12)
                math_task_list.append(["",""])
                math_task_list.append(["One is ≤ 3 steps from","blue"])
                math_task_list.append(["Both are ≤ 2 steps from","gray"])
                math_task_list.append(["Both are in the same column",""])
                math_task_list.append(["They are = 1 step from each other",""])
                math_bomb_grid = [0,2,3,7,9]
            elif tmpInt == 3:
                math_diamond_position.append(2)
                math_diamond_position.append(3)
                math_task_list.append(["",""])
                math_task_list.append(["Both are in the same row",""])
                math_task_list.append(["None are diagonal to a sphere",""])
                math_task_list.append(["Both are ≥ 2 steps from","gray"])
                math_bomb_grid = [0,4,5,7,9]
            elif tmpInt == 4:
                math_diamond_position.append(7)
                math_diamond_position.append(8)
                math_task_list.append(["",""])
                math_task_list.append(["Both are ≥ 3 steps from","blue"])
                math_task_list.append(["One is = 2 steps from","gray"])
                math_task_list.append(["They are in the same row",""])
                math_bomb_grid = [0,5,6,9,12]
        elif task == 3:
            math_d_count_total = 1
            math_grid = []
            math_grid.append([400,300,"base"])
            math_grid.append([500,300,"base"])
            math_grid.append([600,300,"base"])
            math_grid.append([700,300,"base"])
            math_grid.append([800,300,"gray"])
            math_grid.append([400,400,"base"])
            math_grid.append([500,400,"base"])
            math_grid.append([600,400,"blue"])
            math_grid.append([700,400,"base"])
            math_grid.append([800,400,"base"])
            math_grid.append([400,500,"base"])
            math_grid.append([500,500,"base"])
            math_grid.append([600,500,"base"])
            math_grid.append([700,500,"base"])
            math_grid.append([800,500,"base"])
            math_grid.append([400,600,"base"])
            math_grid.append([500,600,"orange"])
            math_grid.append([600,600,"base"])
            math_grid.append([700,600,"base"])
            math_grid.append([800,600,"base"])
            math_grid.append([400,700,"base"])
            math_grid.append([500,700,"pink"])
            math_grid.append([600,700,"base"])
            math_grid.append([700,700,"base"])
            math_grid.append([800,700,"base"])
            
            math_diamond_position = []
            math_task_list = []
            tmpInt = renpy.random.randint(0,20)
            math_task_desc = ["Find 1","d"]
            
            if tmpInt == 0:
                math_diamond_position.append(0)
                math_task_list.append(["",""])
                math_task_list.append(["It is surrounded by ≤ 4 empty tiles",""])
                math_task_list.append(["It is not within 3 steps of","orange"])
                math_task_list.append(["It is = 3 steps from","blue"])
                math_bomb_grid = [1,9,10,17,23]
            elif tmpInt == 1:
                math_diamond_position.append(1)
                math_task_list.append(["",""])
                math_task_list.append(["It is surrounded by ≤ 4 empty tiles",""])
                math_task_list.append(["It is within 4 steps from","orange"])
                math_task_list.append(["It is = 3 steps from","gray"])
                math_bomb_grid = [0,9,10,17,23]
            elif tmpInt == 2:
                math_diamond_position.append(2)
                math_task_list.append(["",""])
                math_task_list.append(["It is surrounded by ≤ 4 empty tiles",""])
                math_task_list.append(["It is ≥ 3 steps from","orange"])
                math_task_list.append(["It is in the same column as","blue"])
                math_bomb_grid = [0,9,10,17,23]
            elif tmpInt == 3:
                math_diamond_position.append(3)
                math_task_list.append(["",""])
                math_task_list.append(["It is surrounded by ≤ 4 empty tiles",""])
                math_task_list.append(["It is ≥ 3 steps from","orange"])
                math_task_list.append(["It is in the fourth column",""])
                math_bomb_grid = [0,9,10,17,23]
            elif tmpInt == 4:
                math_diamond_position.append(5)
                math_task_list.append(["",""])
                math_task_list.append(["It is ≤ 3 steps from","blue"])
                math_task_list.append(["It is > 4 steps from","gray"])
                math_task_list.append(["It is surrounded by 5 empty tiles",""])
                math_bomb_grid = [0,9,10,17,23]
            elif tmpInt == 5:
                math_diamond_position.append(6)
                math_task_list.append(["",""])
                math_task_list.append(["It is = 1 step from a sphere",""])
                math_task_list.append(["It is > 1 step from","orange"])
                math_task_list.append(["It is surrounded by 7 empty tiles",""])
                math_bomb_grid = [0,9,10,17,23]
            elif tmpInt == 6:
                math_diamond_position.append(8)
                math_task_list.append(["",""])
                math_task_list.append(["It is = 1 step from a sphere",""])
                math_task_list.append(["It is > 2 steps from","orange"])
                math_task_list.append(["It is surrounded by ≥ 5 empty tiles",""])
                math_bomb_grid = [0,9,10,17,23]
            elif tmpInt == 7:
                math_diamond_position.append(9)
                math_task_list.append(["",""])
                math_task_list.append(["It is = 1 step from a sphere",""])
                math_task_list.append(["It is > 2 steps from","orange"])
                math_task_list.append(["It is diagonal to","pink"])
                math_bomb_grid = [0,8,10,17,23]
            elif tmpInt == 8:
                math_diamond_position.append(10)
                math_task_list.append(["",""])
                math_task_list.append(["It is diagonal to one sphere",""])
                math_task_list.append(["It is < 3 steps from","orange"])
                math_task_list.append(["The closest sphere is 2 steps away",""])
                math_bomb_grid = [0,8,11,17,23]
            elif tmpInt == 9:
                math_diamond_position.append(11)
                math_task_list.append(["",""])
                math_task_list.append(["It is surrounded by 2 spheres",""])
                math_task_list.append(["It is > 4 steps from","gray"])
                math_task_list.append(["It is in an empty row",""])
                math_bomb_grid = [0,8,10,17,23]
            elif tmpInt == 10:
                math_diamond_position.append(12)
                math_task_list.append(["",""])
                math_task_list.append(["It is = 2 steps from a sphere",""])
                math_task_list.append(["It is = 3 steps from","pink"])
                math_task_list.append(["It is surrounded by 6 empty tiles",""])
                math_bomb_grid = [0,8,10,17,23]
            elif tmpInt == 11:
                math_diamond_position.append(13)
                math_task_list.append(["",""])
                math_task_list.append(["It is diagonal to two spheres",""])
                math_task_list.append(["It is > 2 steps from","orange"])
                math_task_list.append(["The closest sphere is 2 steps away",""])
                math_bomb_grid = [0,8,10,17,23]
            elif tmpInt == 12:
                math_diamond_position.append(14)
                math_task_list.append(["",""])
                math_task_list.append(["It isn't diagonal to any sphere",""])
                math_task_list.append(["It is > 3 steps from","orange"])
                math_task_list.append(["The closest sphere is 2 steps away",""])
                math_bomb_grid = [0,8,10,17,23]
            elif tmpInt == 13:
                math_diamond_position.append(15)
                math_task_list.append(["",""])
                math_task_list.append(["It is diagonal to two spheres",""])
                math_task_list.append(["It is < 3 steps from","orange"])
                math_task_list.append(["It is not diagonal to","gray"])
                math_bomb_grid = [0,8,10,17,23]
            elif tmpInt == 14:
                math_diamond_position.append(17)
                math_task_list.append(["",""])
                math_task_list.append(["It is in the same column as ≥ 1 sphere",""])
                math_task_list.append(["It is > 4 steps from","gray"])
                math_task_list.append(["It is diagonal to","pink"])
                math_bomb_grid = [0,8,10,18,23]
            elif tmpInt == 15:
                math_diamond_position.append(18)
                math_task_list.append(["",""])
                math_task_list.append(["It is not in the same column as any sphere",""])
                math_task_list.append(["It is not diagonal to any sphere",""])
                math_task_list.append(["It is ≤ 2 steps from","orange"])
                math_bomb_grid = [0,8,10,18,23]
            elif tmpInt == 16:
                math_diamond_position.append(19)
                math_task_list.append(["",""])
                math_task_list.append(["It is surrounded by 5 empty tiles",""])
                math_task_list.append(["It is not in the same row as","blue"])
                math_task_list.append(["It is diagonal to one sphere",""])
                math_bomb_grid = [0,8,10,18,23]
            elif tmpInt == 17:
                math_diamond_position.append(20)
                math_task_list.append(["",""])
                math_task_list.append(["It is diagonal to ≥ 1 sphere",""])
                math_task_list.append(["It is ≥ 3 steps from","blue"])
                math_task_list.append(["It is diagonal to","gray"])
                math_bomb_grid = [0,8,10,18,23]
            elif tmpInt == 18:
                math_diamond_position.append(22)
                math_task_list.append(["",""])
                math_task_list.append(["It is = 2 steps from","orange"])
                math_task_list.append(["It is in the same column as = 1 sphere",""])
                math_task_list.append(["It is > 5 steps from","gray"])
                math_bomb_grid = [0,8,10,18,23]
            elif tmpInt == 19:
                math_diamond_position.append(23)
                math_task_list.append(["",""])
                math_task_list.append(["It is not diagonal to a sphere",""])
                math_task_list.append(["It is > 2 steps from","blue"])
                math_task_list.append(["It is = 3 steps from","orange"])
                math_bomb_grid = [0,8,10,18,22]
            elif tmpInt == 20:
                math_diamond_position.append(24)
                math_task_list.append(["",""])
                math_task_list.append(["It is not diagonal to a sphere",""])
                math_task_list.append(["The closest sphere is 3 steps away",""])
                math_task_list.append(["It is = 3 steps from","pink"])
                math_bomb_grid = [0,8,10,18,22]
        elif task == 4:
            math_d_count_total = 2
            math_grid = []
            math_grid.append([400,300,"blue"])
            math_grid.append([500,300,"base"])
            math_grid.append([600,300,"base"])
            math_grid.append([700,300,"base"])
            math_grid.append([800,300,"base"])
            math_grid.append([400,400,"base"])
            math_grid.append([500,400,"base"])
            math_grid.append([600,400,"base"])
            math_grid.append([700,400,"base"])
            math_grid.append([800,400,"gray"])
            math_grid.append([400,500,"base"])
            math_grid.append([500,500,"base"])
            math_grid.append([600,500,"base"])
            math_grid.append([700,500,"orange"])
            math_grid.append([800,500,"base"])
            math_grid.append([400,600,"base"])
            math_grid.append([500,600,"base"])
            math_grid.append([600,600,"base"])
            math_grid.append([700,600,"base"])
            math_grid.append([800,600,"base"])
            math_grid.append([400,700,"base"])
            math_grid.append([500,700,"pink"])
            math_grid.append([600,700,"base"])
            math_grid.append([700,700,"base"])
            math_grid.append([800,700,"base"])
            
            math_diamond_position = []
            math_task_list = []
            tmpInt = renpy.random.randint(0,8)
            math_task_desc = ["Find 2","d"]
            
            if tmpInt == 0:
                math_diamond_position.append(17)
                math_diamond_position.append(19)
                math_task_list.append(["",""])
                math_task_list.append(["They are not diagonal to each other",""])
                math_task_list.append(["They are = 2 steps from each other",""])
                math_task_list.append(["Both are = 2 steps from 2 spheres",""])
                math_task_list.append(["They are ≥ 4 steps from","blue"])
                math_bomb_grid = [1,7,10,11,20]
            elif tmpInt == 1:
                math_diamond_position.append(12)
                math_diamond_position.append(20)
                math_task_list.append(["",""])
                math_task_list.append(["They are diagonal to each other",""])
                math_task_list.append(["They are = 4 steps from each other",""])
                math_task_list.append(["Both are = 1 step from 1 sphere",""])
                math_task_list.append(["One is = 1 step from","pink"])
                math_bomb_grid = [1,7,10,11,23]
            elif tmpInt == 2:
                math_diamond_position.append(16)
                math_diamond_position.append(17)
                math_task_list.append(["",""])
                math_task_list.append(["They are = 1 step from each other",""])
                math_task_list.append(["They are > 3 steps from","gray"])
                math_task_list.append(["They are in the same row",""])
                math_task_list.append(["One is = 5 steps from","blue"])
                math_bomb_grid = [1,7,10,11,23]
            elif tmpInt == 3:
                math_diamond_position.append(3)
                math_diamond_position.append(15)
                math_task_list.append(["",""])
                math_task_list.append(["They are diagonal to each other",""])
                math_task_list.append(["They are = 6 steps from each other",""])
                math_task_list.append(["The closest sphere is = 2 steps away from both",""])
                math_task_list.append(["One is = 4 steps from","orange"])
                math_bomb_grid = [1,7,10,11,23]
            elif tmpInt == 4:
                math_diamond_position.append(12)
                math_diamond_position.append(22)
                math_task_list.append(["",""])
                math_task_list.append(["They are = 2 steps from each other",""])
                math_task_list.append(["One is = 1 step from","orange"])
                math_task_list.append(["They are in the same column",""])
                math_task_list.append(["One is = 1 step from","pink"])
                math_bomb_grid = [1,7,10,11,23]
            elif tmpInt == 5:
                math_diamond_position.append(14)
                math_diamond_position.append(20)
                math_task_list.append(["",""])
                math_task_list.append(["They are = 6 steps from each other",""])
                math_task_list.append(["One is = 1 step from","pink"])
                math_task_list.append(["They are not diagonal to each other",""])
                math_task_list.append(["One is = 1 step from","orange"])
                math_bomb_grid = [1,7,10,11,23]
            elif tmpInt == 6:
                math_diamond_position.append(10)
                math_diamond_position.append(12)
                math_task_list.append(["",""])
                math_task_list.append(["They are = 2 steps from each other",""])
                math_task_list.append(["One is = 1 step from","orange"])
                math_task_list.append(["They are in the same row",""])
                math_task_list.append(["Both are = 3 steps from","pink"])
                math_bomb_grid = [1,7,8,11,23]
            elif tmpInt == 7:
                math_diamond_position.append(2)
                math_diamond_position.append(22)
                math_task_list.append(["",""])
                math_task_list.append(["They are in the same column",""])
                math_task_list.append(["One is ≤ 2 steps from","blue"])
                math_task_list.append(["Both are = 3 steps from ","orange"])
                math_task_list.append(["They are > 2 steps from each other",""])
                math_bomb_grid = [1,7,8,11,23]
            elif tmpInt == 8:
                math_diamond_position.append(2)
                math_diamond_position.append(3)
                math_task_list.append(["",""])
                math_task_list.append(["They are = 1 step from each other",""])
                math_task_list.append(["Both are ≤ 4 steps from","blue"])
                math_task_list.append(["Both are > 4 steps from ","pink"])
                math_task_list.append(["Both are = 2 steps away from ≥ 1 sphere",""])
                math_bomb_grid = [1,7,8,11,23]
        elif task == 5:
            math_d_count_total = 3
            math_grid = []
            math_grid.append([300,300,"base"])
            math_grid.append([400,300,"base"])
            math_grid.append([500,300,"blue"])
            math_grid.append([600,300,"base"])
            math_grid.append([700,300,"base"])
            math_grid.append([800,300,"pink"])
            math_grid.append([900,300,"base"])
            math_grid.append([400,400,"base"])
            math_grid.append([500,400,"base"])
            math_grid.append([700,400,"base"])
            math_grid.append([800,400,"base"])
            math_grid.append([300,500,"orange"])
            math_grid.append([400,500,"base"])
            math_grid.append([500,500,"base"])
            math_grid.append([600,500,"base"])
            math_grid.append([700,500,"base"])
            math_grid.append([800,500,"base"])
            math_grid.append([900,500,"base"])
            math_grid.append([400,600,"base"])
            math_grid.append([500,600,"base"])
            math_grid.append([600,600,"base"])
            math_grid.append([700,600,"gray"])
            math_grid.append([800,600,"base"])
            math_grid.append([400,700,"base"])
            math_grid.append([500,700,"base"])
            math_grid.append([800,700,"base"])
            
            math_diamond_position = []
            math_task_list = []
            tmpInt = renpy.random.randint(0,6)
            math_task_desc = ["Find 3","d"]
            
            if tmpInt == 0:
                math_diamond_position.append(3)
                math_diamond_position.append(4)
                math_diamond_position.append(15)
                math_task_list.append(["",""])
                math_task_list.append(["All are = 1 step from a sphere",""])
                math_task_list.append(["Two are = 1 step from each other",""])
                math_task_list.append(["One is diagonal to","blue"])
                math_task_list.append(["All are < 4 steps from each other",""])
                math_bomb_grid = [1,7,10,12,20]
            elif tmpInt == 1:
                math_diamond_position.append(12)
                math_diamond_position.append(13)
                math_diamond_position.append(19)
                math_task_list.append(["",""])
                math_task_list.append(["All are < 5 steps from","gray"])
                math_task_list.append(["All are < 5 steps from","orange"])
                math_task_list.append(["All are > 4 steps from","pink"])
                math_task_list.append(["All are < 4 steps from","blue"])
                math_bomb_grid = [1,7,10,14,20]
            elif tmpInt == 2:
                math_diamond_position.append(7)
                math_diamond_position.append(18)
                math_diamond_position.append(19)
                math_task_list.append(["",""])
                math_task_list.append(["All are > 4 steps from","pink"])
                math_task_list.append(["Two are = 2 steps from","orange"])
                math_task_list.append(["None are diagonal to each other",""])
                math_task_list.append(["One is = 2 steps from","gray"])
                math_bomb_grid = [1,8,10,12,20]
            elif tmpInt == 3:
                math_diamond_position.append(13)
                math_diamond_position.append(15)
                math_diamond_position.append(17)
                math_task_list.append(["",""])
                math_task_list.append(["All are in the same row",""])
                math_task_list.append(["All are ≥ 2 steps from each other",""])
                math_task_list.append(["One is = 1 step from","gray"])
                math_task_list.append(["One is = 2 steps from two spheres",""])
                math_bomb_grid = [1,8,10,12,20]
            elif tmpInt == 4:
                math_diamond_position.append(3)
                math_diamond_position.append(8)
                math_diamond_position.append(16)
                math_task_list.append(["",""])
                math_task_list.append(["Two are = 1 step from","blue"])
                math_task_list.append(["All are diagonal to ≥ 1","d"])
                math_task_list.append(["Two are = 2 steps from","pink"])
                math_task_list.append(["Two are diagonal to","gray"])
                math_bomb_grid = [1,7,10,12,20]
            elif tmpInt == 5:
                math_diamond_position.append(10)
                math_diamond_position.append(15)
                math_diamond_position.append(16)
                math_task_list.append(["",""])
                math_task_list.append(["Two are in the same row as","orange"])
                math_task_list.append(["Two are in the same column as","pink"])
                math_task_list.append(["One is diagonal to","blue"])
                math_task_list.append(["One is = 1 step from","pink"])
                math_bomb_grid = [1,7,9,12,20]
            elif tmpInt == 6:
                math_diamond_position.append(14)
                math_diamond_position.append(19)
                math_diamond_position.append(25)
                math_task_list.append(["",""])
                math_task_list.append(["Two are diagonal to","pink"])
                math_task_list.append(["Two are diagonal to","gray"])
                math_task_list.append(["One is in the same column as","blue"])
                math_task_list.append(["All are = 2 steps from","gray"])
                math_task_list.append(["None are in the same row",""])
                math_bomb_grid = [1,7,9,12,20]
        else:
            math_calc_result()
        return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
