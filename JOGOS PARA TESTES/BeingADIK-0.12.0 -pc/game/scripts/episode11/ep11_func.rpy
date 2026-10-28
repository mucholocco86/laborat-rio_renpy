init python:

    def check_jm_solo_ep11():
        global ep8_maya_lewd
        global ep5_followed_maya
        global ep7_solo_maya
        global ep3_mayaLewd
        global ep9_maya_lewd
        global ep8_josy_lewd
        global ep5_followed_josy
        global ep7_solo_josy
        global ep7_josy_lewd
        global ep7_left_with_josy
        global ep10_jm_solo
        global RPmaya
        global RPjosy
        
        cnt = 0
        if ep8_maya_lewd:
            cnt += 1
        if ep5_followed_maya:
            cnt += 1
        if ep7_solo_maya:
            cnt += 1
        if ep3_mayaLewd:
            cnt += 1
        if ep9_maya_lewd:
            cnt += 1
        if ep10_jm_solo == "Maya":
            cnt += 1
        cnt2 = 0
        
        if ep8_josy_lewd:
            cnt2 += 1
        if ep5_followed_josy:
            cnt2 += 1
        if ep7_solo_josy:
            cnt2 += 1
        if ep7_josy_lewd:
            cnt2 += 1
        if ep7_left_with_josy:
            cnt2 += 1
        if ep10_jm_solo == "Josy":
            cnt2 += 1
        
        if cnt2 > cnt + 1:
            return "Josy"
        elif cnt2 + 1 < cnt:
            return "Maya"
        else:
            if check_mlove() and check_jlove():
                if RPmaya/74.0 > RPjosy/67.0:
                    return "Maya"
                else:
                    return "Josy"
            elif check_mlove():
                return "Maya"
            elif check_jlove():
                return "Josy"
            else:
                if RPmaya/74.0 > RPjosy/67.0:
                    return "Maya"
                else:
                    return "Josy"
        return

    def check_mlove():
        global RPmaya
        if RPmaya > 36:
            return True
        else:
            return False
    def check_jlove():
        global RPjosy
        if RPjosy > 31:
            return True
        else:
            return False

# Decompiled by unrpyc {v1.3.2}: https://github.com/CensoredUsername/unrpyc dev-branch
