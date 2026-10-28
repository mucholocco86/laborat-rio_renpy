init python:
    def getFiles (dir=""):
        list = renpy.list_files(True)
        rv = []
        for f in list:
            if renpy.re.match(dir,f):
                rv.append(f[(len(dir)):])
        return rv