init 10 python:
    def resetWalkthrough ():
        for index in range (1, 11):
            var = "wt" + str (index)
            if var in globals ():
                del globals ()[var]