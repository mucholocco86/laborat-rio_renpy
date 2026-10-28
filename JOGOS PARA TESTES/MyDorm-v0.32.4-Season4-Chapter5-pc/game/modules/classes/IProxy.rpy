init python:
    class IProxy (int, object):

        def __iadd__ (self, val):
            self.parent.iadd_x (val)
            return self.parent.x

        def __isub__ (self, val):
            self.parent.isub_x (val)
            return self.parent.x