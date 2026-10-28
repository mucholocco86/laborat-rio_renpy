# Patched data will be patched similar to nicest patch
# All values of every dict (nested or not) are optional; omit key if no value is given
# For variable names (that use user input to be set, are written in in Ren'Py say manner with [])
# In this comment the for a set list of keys term ENUM is used loosly to define a set of previously agreed to keys.
# Only set values that are known when the character is encountered for the first time; profile will be updated from within the labels when new information is available
# {
#   first_met       ..  label name of first encounter (trigger for when the profile will appear in the profiles screen)
#   name            ..  dict that maps enum:string
#                       ENUM(fist, last, nick, mc) .. "mc" maps the name this character uses for the MC if it's not default (e.g. Emma calls MC "daddy")
#                       only set those that are applicable
#   birthday        ..  dict of string:integer mapping day, month and year to an integer value;
#                       values are actual calendar, they do NOT start at 0
#                       profiles/classes/MyDormDate has a year as option as well, but we probably don't use that
#   age             ..  the age of the character as integer
#   job             ..  The job or occupation of the character as a string or list of string
#   relationship    ..  dict that maps enum:list
#                       ENUM(mc, others) mapped to list of strings
#                       mc      ..  what the MC sees this character as
#                       others  ..  what this character is for others
#   height          ..  height of the character as an integer value in cm
#   traits          ..  dict that maps enum:list
#                       ENUM(mental, physical) mapped to list of strings
#   images          ..  omitted for now
# }