screen flashlight_screen:
    tag flashlight_screen
    modal False
    add TrackCursor("[persistent.img_dir]/gui/displayables/flashlight_cursor_3.png")

init python:

    class TrackCursor(renpy.Displayable):
        
        def __init__(self, child):
            
            super(TrackCursor, self).__init__()
            
            self.child = renpy.displayable(child)
            
            self.x = None
            self.y = None
        
        def render(self, width, height, st, at):
            
            rv = renpy.Render(width, height)
            
            if self.x < 0 or self.y  < 0 or self.x > config.screen_width or self.y > config.screen_height:
                rv.canvas().rect("#000", (0, 0, config.screen_width, config.screen_height))
                return rv
            
            if self.x is not None:
                cr = renpy.render(self.child, width, height, st, at)
                cw, ch = cr.get_size()
                rv.blit(cr, (self.x - cw / 2, self.y - ch / 2))
            
            return rv
        
        def event(self, ev, x, y, st):
            
            if (x != self.x) or (y != self.y):
                self.x = x
                self.y = y
                renpy.redraw(self, 0)
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
