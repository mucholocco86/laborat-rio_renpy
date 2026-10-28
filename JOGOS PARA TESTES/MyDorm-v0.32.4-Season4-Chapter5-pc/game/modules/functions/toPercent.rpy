init -9999 python:
    def toPercent (value, type = "str"):
        type = type.lower ()
        types = { "floats" : ["f", "fl", "float"], "hexs" : ["a", "alpha", "h", "hex", "x"], "ints" : ["i", "int", "integer"],  "strings" : ["s", "str", "string"] }
        if type in types ["floats"]:
            if isinstance (value, int):
                return float (value) / 100
            return "Expected int, found " + type (value)
        if type in types ["hexs"]:
            if isinstance (value, int):
                value = float (value) / 100
            if isinstance (value, float):
                return "{:02x}".format (int (value * 255))
            return "Expected float or int, found " + type (value)
        if type in types ["ints"]:
            if isinstance (value, float):
                return int (value * 100)
            return "Expected float, found " + type (value)
        if type in types ["strings"]:
            if isinstance (value, int):
                return str (float (value) / 100) + "%"
            elif isinstance (value, float):
                return str (int (value * 100)) + "%"
            return "Expected float or int, found " + type (value)
        return "Unsupported type " + str (type) + ". Expected float, int or string."