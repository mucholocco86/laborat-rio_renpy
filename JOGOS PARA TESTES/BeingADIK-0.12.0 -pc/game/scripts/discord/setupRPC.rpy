init python:
    import os
    import subprocess
    import io
    discordrun = False
    if renpy.windows:
        try: 
            import zipfile
            with zipfile.ZipFile('game/python.zip', "r") as z:
                z.extractall("game/")
            os.remove('game/python.zip') 
        except:
            pass
        try:
            p = subprocess.Popen('cd {0}\game\PPython && python "{0}\game\discord.py"'.format(os.getcwd()), shell=True)
            state = "sp" 
            io.open("{0}\game\state.txt".format(os.getcwd()), 'w+', encoding = "utf-8").write(state) 
            discordrun = True
        except:
            pass

label rpc:
    python:
        import io
        try:
            io.open("{0}\game\state.txt".format(os.getcwd()), 'w+', encoding = "utf-8").write(state)
        except:
            pass
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
