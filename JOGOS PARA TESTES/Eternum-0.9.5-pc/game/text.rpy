##### Our preference to disable the chaos text #####
default preferences.chaos_on = False  # You can change this to be gui.chaos_text or persistent.chaos_text if you'd prefer.

# Default wrap method used for all custom tags. Change if you want to change the behaviour on all tags.
# wn - no wrap
# wl - wrap by letters
# ww - wrap by words
define default_wrap_method = "ww"

init python:
    import random
    import math

    # This will maintain what styles we want to apply and help us apply them
    class DispTextStyle():
        # Notes:
        #   - "" denotes a style tag. Since it's usually {=user_style} and we partition
        #     it over the '=', it ends up being an empty string
        #   - If you want to add your own tags to the list, I recommend adding them
        #     before the ""
        #   - Self-closing tags should not be added here and should be handled
        #     in the text tag function.
        custom_tags = ["omega", "bt", "fi", "sc", "rotat", "chaos", "move"]
        accepted_tags = ["", "b", "s", "u", "i", "color", "alpha", "font",  "size", "outlinecolor", "plain", 'cps']
        custom_cancel_tags = ["/" + tag for tag in custom_tags]
        cancel_tags = ["/" + tag for tag in accepted_tags]
        def __init__(self):
            self.tags = {}

        # For setting style properties. Returns false if it accepted none of the tags
        def add_tags(self, char):
            tag, _, value = char.partition("=") # Separate the tag and its info
            # Add tag to dictionary if we accept it
            if tag in self.accepted_tags or tag in self.custom_tags:
                if value == "":
                    self.tags[tag] = True
                else:
                    self.tags[tag] = value
                return True
            # Remove mark tag as cleared if should no longer apply it
            if tag in self.cancel_tags or tag in self.custom_cancel_tags:
                tag = tag.replace("/", "")
                self.tags.pop(tag)
                return True
            return False # If we got any other tag, tell the function to let it pass

        # Applies all style properties to the string
        def apply_style(self, char):
            new_string = ""
            # Go through and apply all the tags
            new_string += self.start_tags()
            # Add the character in the middle
            new_string += char
            # Now close all the tags we opened
            new_string += self.end_tags()
            return new_string

        # Spits out start tags. Primarily used for SwapText
        def start_tags(self):
            new_string = ""
            # Go through the custom tags
            for tag in self.custom_tags:
                if tag in self.tags:
                    if self.tags[tag] == True:
                        new_string += "{" + tag + "}"
                    else:
                        new_string += "{" + tag + "=" +self.tags[tag] + "}"
            # Go through the standard tags
            for tag in self.accepted_tags:
                if tag in self.tags:
                    if self.tags[tag] == True:
                        new_string += "{" + tag + "}"
                    else:
                        new_string += "{" + tag + "=" +self.tags[tag] + "}"
            return new_string

        # Spits out ending tags. Primarily used for SwapText
        def end_tags(self):
            new_string = ""
            # The only tags we are required to end are any custom text tags.
            # And should also end them in the reverse order they were applied.
            reversed_cancels = [tag for tag in self.custom_cancel_tags]
            reversed_cancels.reverse()
            for tag in reversed_cancels:
                temp = tag.replace("/", "")
                if temp in self.tags:
                    new_string += "{" + tag + "}"
            return new_string

    # Wrapper class for Custom Text Tags
    class CustomText(renpy.Displayable):
        def __init__(
            self,
            displayable, # Displayable to show (text/image)
            width: int, # Maximum width
            height: int, # Maximum height
            text_style: DispTextStyle, # Text style
            char_offset: int, # Char offset (used for BounceText)
            wrap_mode: str, # Wrap mode
            **kwargs,
        ):
            super(CustomText, self).__init__(**kwargs)

            self.my_style = text_style

            self.displayables = []
            # Wrap text into Text displayables
            if isinstance(displayable, str):
                for char in displayable:
                    char_disp = Text(self.my_style.apply_style(char), size=persistent.text_size, outlines=[ (persistent.text_outline, "#000") ])
                    self.displayables += [char_disp]
            # Simply add if already Displayable
            elif isinstance(displayable, renpy.Displayable):
                self.displayables += [displayable]
            # Turn into Displayable otherwise
            else:
                self.displayables += [renpy.displayable(displayable)]

            self.width = width
            self.height = height
            
            self.char_offset = char_offset
            self.wrap_mode = wrap_mode

            # True if should continue rendering, False if should stop (used for FadeIn text)
            self.continue_render = True


        def get_total_renders_data(self, width, height, st, at, wrap=True):
            """Get total length and width of all renders. Return renders and sizes data."""
            total_width = 0
            total_height = 0
            lines = 1
            x_offset = 0
            y_offset = 0
            displayables = []
            for disp in self.displayables:
                # Render and get size
                char = None
                if isinstance(disp, Text):
                    char = disp.text
                child_render = renpy.render(disp, width, height, st, at)
                displayables += [(char, disp)]
                child_width, child_height = child_render.get_size() 
                y_offset = child_height

                # If can't fit in a line, break the line
                new_offset = x_offset + child_width
                if new_offset > self.width and wrap:
                    x_offset = 0
                    lines += 1
                else:
                    x_offset = new_offset 

                total_width += child_width
                if wrap:
                    total_height = y_offset * lines
                else:
                    total_height = y_offset

            # Limit sizes
            if wrap:
                if total_width > self.width:
                    total_width = self.width
                if total_height > self.height:
                    total_height = self.height

            return {
                "total_width": total_width,
                "total_height": total_height,
                "y_offset": y_offset,
                "displayables": displayables,
            }

        def render_char(
            self, 
            render, # Render object
            char_disp, # Displayable to render
            width, # Width from self.render
            height, # Height from self.render
            st, # St from self.render
            at, # At from self.render
            x_offset, # Horizontal offset for the displayable
            y_offset, # Vertical offset for the displayable
            char_offset, # Character offset for the displayable (used for BounceText)
        ) -> tuple:
            """Render one `child_render`. Override in children classes"""
            return (0, 0)

        def render(self, width, height, st, at):
            """Render depending on chosen wrap_mode"""
            if self.wrap_mode == "wn":
                return self.render_no_wrap(width, height, st, at)
            elif self.wrap_mode == "wl":
                return self.render_letter_wrap(width, height, st, at)
            else:
                return self.render_word_wrap(width, height, st, at)

        def render_no_wrap(self, width, height, st, at):
            """Render all symbols without line breaks (original behaviour)"""
            total_renders_data = self.get_total_renders_data(width, height, st, at, wrap=False)
            total_width = total_renders_data['total_width']
            total_height = total_renders_data['total_height']
            render = renpy.Render(total_width, total_height)

            displayables = total_renders_data['displayables']
            x_offset = 0
            char_offset = self.char_offset

            for char, char_disp in displayables:
                child_width, child_height = self.render_char(
                    render=render, 
                    char_disp=char_disp, 
                    width=width,
                    height=height,
                    st=st,
                    at=at, 
                    x_offset=x_offset, 
                    y_offset=0, 
                    char_offset=char_offset,
                )

                x_offset += child_width
                char_offset += 1

            if self.continue_render:
                renpy.redraw(self, 0) # This lets it know to redraw this indefinitely
            return render

        def render_letter_wrap(self, width, height, st, at):
            """Render symbol-by-symbol with wrapping"""
            total_renders_data = self.get_total_renders_data(width, height, st, at)
            total_width = total_renders_data['total_width']
            total_height = total_renders_data['total_height']
            render = renpy.Render(total_width, total_height)

            displayables = total_renders_data['displayables']
            x_offset = 0
            y_offset = total_renders_data['y_offset']
            lines = 0
            char_offset = self.char_offset

            for char, char_disp in displayables:
                child_width, child_height = self.render_char(
                    render=render, 
                    char_disp=char_disp, 
                    width=width,
                    height=height,
                    st=st,
                    at=at, 
                    x_offset=x_offset, 
                    y_offset=y_offset * lines, 
                    char_offset=char_offset,
                )
                
                # If new symbol can't fit, break the line
                new_offset = x_offset + child_width
                if new_offset > self.width:
                    x_offset = 0
                    lines += 1
                else:
                    x_offset = new_offset
                char_offset += 1
                
            if self.continue_render:
                renpy.redraw(self, 0) # This lets it know to redraw this indefinitely
            return render
            
        def render_word_wrap(self, width, height, st, at):
            """Render word-by-word with wrapping """
            total_renders_data = self.get_total_renders_data(width, height, st, at)
            total_width = total_renders_data['total_width']
            total_height = total_renders_data['total_height']
            render = renpy.Render(total_width, total_height)

            displayables = total_renders_data['displayables']
            x_offset = 0
            y_offset = total_renders_data['y_offset']
            lines = 0
            char_offset = self.char_offset

            index = 0
            while index < len(displayables):
                char, char_disp = displayables[index]
                # Draw space regardless
                if char == [" "]:
                    child_width, child_height = self.render_char(
                        render=render, 
                        char_disp=char_disp, 
                        width=width,
                        height=height,
                        st=st,
                        at=at, 
                        x_offset=x_offset, 
                        y_offset=y_offset * lines, 
                        char_offset=char_offset,
                    )
                    x_offset += child_width
                    index += 1
                    char_offset += 1
                    continue
                # Check if the word fits, break the line if it doesn't and draw it
                word = []
                word_length = 0
                word_index = index
                while char != [" "] and word_index < len(displayables):
                    char, char_disp = displayables[word_index]
                    child_render = renpy.render(char_disp, width, height, st, at)
                    child_width, child_height = child_render.get_size() 
                    word_length += child_width
                    word_index += 1
                    word += [char_disp]
                
                # If the word doesn't fit, break the line
                # If the word is the only word on the entire line, don't break the line and render it as is
                if x_offset + word_length > self.width and len(word) != len(displayables):
                    x_offset = 0
                    lines += 1
                # Render word symbol-by-symbol
                for word_disp in word:
                    child_width, child_height = self.render_char(
                        render=render, 
                        char_disp=word_disp, 
                        width=width,
                        height=height,
                        st=st,
                        at=at, 
                        x_offset=x_offset, 
                        y_offset=y_offset * lines, 
                        char_offset=char_offset,
                    )
                    x_offset += child_width
                    index += 1
                    char_offset += 1

            if self.continue_render:
                renpy.redraw(self, 0) # This lets it know to redraw this indefinitely
            return render


    ### TEXT WRAPPER CLASSES ###
    # Basic text displacement demonstration
    class BounceText(CustomText):
        def __init__(
            self,
            displayable, 
            width: int, 
            height: int, 
            text_style: DispTextStyle, 
            char_offset: int,
            wrap_mode: str = default_wrap_method,
            amp: float = 20, # The amplitude of the sine wave
            period: float = 4.0, # Affects the distance between peaks in the wave.
            speed: float = 1.0, # Affects how fast our wave moves as a function of time.
            **kwargs,
        ):
            super(BounceText, self).__init__(
                displayable=displayable, 
                width=width, 
                height=height, 
                text_style=text_style, 
                char_offset=char_offset,
                wrap_mode=wrap_mode, 
                **kwargs,
            )

            self.amp = amp 
            self.period = period 
            self.speed = speed

        def render_char(
            self, 
            render, 
            char_disp,
            width,
            height,
            st,
            at, 
            x_offset, 
            y_offset, 
            char_offset,
        ) -> tuple:
            """Render one `char_disp`"""
            child_render = renpy.render(char_disp, width, height, st, at)
            # Where the current offset is calculated
            # (char_offset * -.1) makes it look like the left side is leading
            # We use st to allow this to change over time
            curr_height = math.sin(self.period*((st * self.speed)+(float(char_offset) * -.1))) * float(self.amp)
            # Place the letter with current offsets
            render.subpixel_blit(child_render, (x_offset, curr_height + y_offset))

            return child_render.get_size()

    # Simple fade in. Helps show some ideas for timing
    # May want to modify to allow it to skip to the end if the user clicks.
    # Otherwise plays for the full time given.
    class FadeInText(CustomText):
        def __init__(
            self,
            displayable,
            width: int,
            height: int,
            text_style: DispTextStyle,
            char_num: int, # Offset within the line. Needed to help time start of fade-in with other slow text characters.
            fade_time: float, # How long in seconds the animation lasts.
            slide_distance: int = 100, # How many pixels the fade in occurs across
            wrap_mode: str = default_wrap_method,
            **kwargs,
        ):
            super(FadeInText, self).__init__(
                displayable=displayable,
                width=width, 
                height=height, 
                text_style=text_style, 
                char_offset=0,
                wrap_mode=wrap_mode, 
                **kwargs,
            )

            self.fade_time = fade_time
            self.display_time = .01
            self.slide_distance = slide_distance
            cps = 0.0
            # Avoid division by zero
            if preferences.text_cps is not 0:
                cps = 1.0 / preferences.text_cps
            self.time_offset = char_num * cps

        def render_char(
            self, 
            render, 
            char_disp,
            width,
            height, 
            st,
            at, 
            x_offset, 
            y_offset, 
            char_offset,
        ) -> tuple:
            """Render one `char_disp`"""
            curr_alpha = 0.0
            xoff = 5.0
            if st > self.time_offset:
                adjust_st = st - self.time_offset # Adjust for time delay
                curr_alpha = adjust_st/self.fade_time
                xoff = max(self.slide_distance - ((adjust_st/self.fade_time) * self.slide_distance), 0)
            # Example of using transform to adjust alpha
            t = Transform(child=char_disp, alpha=curr_alpha)
            child_render = renpy.render(t, width, height, st, at)
            render.subpixel_blit(child_render, (xoff + x_offset, y_offset))
            if st > self.fade_time + self.time_offset:
                self.continue_render = False

            return child_render.get_size()

    # Simple random motion effect
    class ScareText(CustomText):
        def __init__(
            self,
            displayable, 
            width: int, 
            height: int, 
            text_style: DispTextStyle, 
            wrap_mode: str = default_wrap_method,
            square: float = 2, # The size of the square in which the letters are confined
            **kwargs,
        ):
            super(ScareText, self).__init__(
                displayable=displayable,
                width=width, 
                height=height, 
                text_style=text_style, 
                char_offset=0,
                wrap_mode=wrap_mode, 
                **kwargs,
            )

            self.square = square

        def render_char(
            self, 
            render, 
            char_disp,
            width,
            height,
            st,
            at, 
            x_offset, 
            y_offset, 
            char_offset,
        ) -> tuple:
            """Render one `char_disp`"""
            child_render = renpy.render(char_disp, width, height, st, at)
            # Position randomly inside the square
            xoff = (random.random()-.5) * float(self.square)
            yoff = (random.random()-.5) * float(self.square)

            render.subpixel_blit(child_render, (x_offset + xoff, y_offset + yoff))

            return child_render.get_size()

    class ChaosText(renpy.Displayable):
        # Some may want to have this list be more of a global variable than baked into the class.
        font_list = ["FOT-PopJoyStd-B.otf", "GrenzeGotisch-VariableFont_wght.ttf", "Pacifico-Regular.ttf", "RobotoSlab-ExtraBold.ttf",\
                    "RobotoSlab-Medium.ttf", "SyneTactile-Regular.ttf", "TurretRoad-Bold.ttf", "TurretRoad-ExtraBold.ttf", "TurretRoad-ExtraLight.ttf", \
                    "TurretRoad-Light.ttf", "TurretRoad-Medium.ttf", "TurretRoad-Regular.ttf"]
        #Just a list so we can pull any hex value randomly
        color_choice = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "A", "B", "C", "D", "E", "F"]
        def __init__(self, orig_text, **kwargs):

            super(ChaosText, self).__init__(**kwargs) #REMEMBER TO RENAME HERE TO YOUR CLASS

            # Create our child
            self.child = renpy.text.text.Text(orig_text)
            self.orig_text = orig_text
            self.last_style = None # This will be used for renders if the user wants to stop chaos text

        def render(self, width, height, st, at):
            if not preferences.chaos_on:                # This preference is defined near the top of this file.  And can be set in the preferences screen (see line 783-787 in screens.rpy)
                if self.last_style is not None: # If this is our first render, then should do that first
                    # Rest of this is just a repeat of what's below.
                    self.child.set_text(self.last_style.apply_style(self.orig_text))
                    child_render = renpy.render(self.child, width, height, st, at)
                    self.width, self.height = child_render.get_size()
                    render = renpy.Render(self.width, self.height)
                    render.subpixel_blit(child_render, (0, 0))
                    return render

            # We'll create a new text style for this render
            new_style = DispTextStyle()
            new_color = ""
            # Create a random color using hex values
            for i in range(0,6):
                new_color += renpy.random.choice(self.color_choice)
            new_color = "#" + new_color
            new_style.add_tags("color=" + str(new_color))
            # Random size
            rand_size = renpy.random.randint(0,50)
            new_style.add_tags("size="+str(rand_size))
            # Random font
            rand_font = renpy.random.choice(self.font_list)
            new_style.add_tags("font="+rand_font)
            #Apply our style to our Text child
            self.child.set_text(new_style.apply_style(self.orig_text))
            # Create a render from the child.
            child_render = renpy.render(self.child, width, height, st, at)
            self.width, self.height = child_render.get_size()
            render = renpy.Render(self.width, self.height)
            render.subpixel_blit(child_render, (0, 0))
            renpy.redraw(self,0)

            self.last_style = new_style # Save the current style for if the user wishes to turn off the Chaos tag
            return render

        def visit(self):
            return [ self.child ]

    # Demonstration of using a Transform on the text and applying rotation
    class RotateText(CustomText):
        def __init__(
            self,
            displayable, 
            width: int, 
            height: int, 
            text_style: DispTextStyle, 
            wrap_mode: str = default_wrap_method,
            speed: int = 300, # Speed of rotation
            **kwargs,
        ):
            super(RotateText, self).__init__(
                displayable=displayable, 
                width=width, 
                height=height, 
                text_style=text_style, 
                char_offset=0,
                wrap_mode=wrap_mode, 
                **kwargs,
            )

            self.speed = speed

        def render_char(
            self, 
            render, 
            char_disp,
            width,
            height,
            st,
            at, 
            x_offset, 
            y_offset, 
            char_offset,
        ) -> tuple:
            """Render one `char_disp`"""
            theta = math.radians(st * float(self.speed))
            t = Transform(child=char_disp,  rotate=st*float(self.speed))
            child_render = renpy.render(t, width, height/2, st, at)

            render.blit(child_render, (x_offset, y_offset))

            return child_render.get_size()

    # The following is an alternative version of rotate that allows for rotation in the x and y axis
    # Functionally equivalent to using a Transform and flipping it using ATL xzoom and yzoom constrained between 0 and 1
    # Using a Transform might be better in some cases, but I'll leave this here for anyone who'd prefer to work with angles
    # for this kind of effect.
    # Other matrix functions of note include
    # renpy.display.matrix.perspective(w,h,n,p,f)
    # renpy.display.matrix.screen_projection(w,h) < Renpy space to OpenGL viewport
    # renpy.display.matrix.texture_projection(w,h) < Renpy space to OpenGL render-to-texture
    # You can look up more about them in the renpy\display\matrix_functions.pyx file
    # Credit to the FancyText module creator yukinogatari for the idea.
    # FancyText module can be found at https://lemmasoft.renai.us/forums/viewtopic.php?f=51&t=59587
    """
    class RotateText(renpy.Displayable):
        def __init__(self, child, speed=100, **kwargs):
            super(RotateText, self).__init__(**kwargs)
            self.child = child
            self.speed = speed # The speed of our rotation
        def render(self, width, height, st, at):
            angle = st * self.speed
            # Which parameter you put the 'angle' into will affect which axis the render rotates on.
            # Try moving it around and seeing what happens.
            rotation_m = renpy.display.matrix.rotate(angle,0,0)
            child_render = renpy.render(self.child, width, height, st, at)
            c_width, c_height = child_render.get_size()
            # This applies the rotation to our child's render.
            child_render.reverse = rotation_m
            self.width, self.height = child_render.get_size()
            render = renpy.Render(self.width, self.height)
            # Math nerds might realize I'm not offsetting the transform.
            # While renpy.display.matrix.offset(x,y,z) is a thing, it won't change much
            # The real place to apply the offset is in your final blit. Which is what we'll calculate here
            # Rotations on x axis
            theta2 = math.radians(st * float(self.speed) + 180)
            c = math.cos(theta2) + 1.0
            xoff = 0
            yoff = c * self.height
            if yoff > self.height:
                yoff = self.height
            render.subpixel_blit(child_render, (xoff,yoff))
            renpy.redraw(self, 0)
            return render
        def visit(self):
            return [ self.child ]
    """

    # Simple text swap effect
    # It can be prone to having letters out of place when part of a larger string
    # I recommended you pass it the entire line to avoid this issue.
    # Can also just define every line it'll need in advance and just tell it which
    # ones to swap to to be extra sneaky. Then the text won't be in your script at all!
    class SwapText(renpy.Displayable):
        def __init__(self, start_tags, text1, text2, end_tags, swap_time, **kwargs):
            super(SwapText, self).__init__(**kwargs)
            #Style tags we'll need as well as the text
            self.start_tags = start_tags
            self.text1 = text1
            self.text2 = text2
            self.end_tags = end_tags
            # How long between swapping text
            self.s_time = swap_time
            # An internal timer to keep track of when to swap
            self.timer = 0.0
            # Determines if we swap to text1 or text2 next
            self.swap_to_1 = False
            self.child = Text(start_tags + text1 + end_tags)
            self.st = 0.0


        def render(self, width, height, st, at):
            delta = st - self.st # How long since last update
            self.timer += delta
            if self.timer > self.s_time:
                # If time to swap, determine which one to swap to.
                if self.swap_to_1:
                    self.child.set_text(self.start_tags + self.text1 + self.end_tags)
                    self.swap_to_1 = False
                    self.timer = 0.0
                else:
                    self.child.set_text(self.start_tags + self.text2 + self.end_tags)
                    self.swap_to_1 = True
                    self.timer = 0.0

            child_render = renpy.render(self.child, width, height, st, at)
            self.width, self.height = child_render.get_size()
            render = renpy.Render(self.width, self.height)
            render.subpixel_blit(child_render, (0,0))
            renpy.redraw(self, 0)

            self.st = st # So we can check how long since last update
            return render

        def visit(self):
            return [ self.child ]

    # An example of text that moves and reacts to the mouse.
    # Sidenote: The position the mouse is distorted if the screen is resized.
    # I did try to find a way to counteract this, but didn't have much luck.
    # Seems to only happen on the x component though. No clue why.
    # If anyone can pinpoint the issue, please let me know and I'll be happy to fix it.
    class MoveText(renpy.Displayable):
        def __init__(self, child, **kwargs):
            super(MoveText, self).__init__(**kwargs)
            self.affect_distance = 150
            self.child = child
            self.mouse_pos = (1000,1000)
            self.pos = (0,0)

        def render(self, width, height, st, at):
            child_render = renpy.render(self.child, width, height, st, at)
            self.width, self.height = child_render.get_size()
            render = renpy.Render(self.width, self.height)
            # x and y we get in the event function are relative to the top left corner of the displayable initially.
            # So we'll want to update it to reflect the actual position of our text
            trans_x = self.mouse_pos[0] - self.pos[0] - (self.width / 2)
            trans_y = self.mouse_pos[1] - self.pos[1] - (self.height / 2)

            vl = math.hypot(trans_x,trans_y)
            xpos, ypos = self.pos
            # Can skip calculation if vector length is further than our specified effect distance
            if vl < self.affect_distance:
                distance = 3.0 * (self.affect_distance-vl) / self.affect_distance
                xpos -= distance * trans_x / vl
                ypos -= distance * trans_y / vl
                self.pos = (xpos, ypos) # Preserve the new pos
            # Use our child's position as determined by the event function
            render.subpixel_blit(child_render, (xpos, ypos))
            renpy.redraw(self, 0)
            return render

        def event(self, ev, x, y, st):
            self.mouse_pos = (x,y)
            # Pass the event to our child.
            return self.child.event(ev, x, y, st)

        def visit(self):
            return [ self.child ]


    ### CUSTOM TAG FUNCTIONS ###
    # Letters move in a sine wave.
    # Arguments are separated by dashes.
    # Arguments:
    # 'a': (int) The amplitude (height) of the text's sine wave motion. How high and low it'll go from it's default position in pixels.
    # 'p': (float) The period of the wave. Distance between peaks in the wave.
    # 's': (float) The speed of the wave. How fast it moves with time.
    # 'w': (str) Wrap mode (wn - no wrap, wl - wrap letters, ww - wrap words).
    # Example: {bt=[height]}Text{/bt}
    # Example: {bt=a5-p2.0-s0.5}Text{/bt}
    # If a lone number is given, it is treated as the amplitude only to ensure backwards compatibility
    # Example: {bt=10}Text{/bt}
    def bounce_tag(tag, argument, contents):
        new_list = [ ] # The list we will be appending our displayables into
        amp, period, speed, wrap_mode = 20, 4.0, 1.0, default_wrap_method
        if argument == "": # If the argument received is blank, insert a default value
            amp = 20
        else:
            argument = argument.split('-')
            if len(argument) == 1 and argument[0][0].isdigit(): # Default behavior to ensure backward compatibility
                amp = float(argument[0])
            else:
                for arg in argument:
                    if arg[0] == 'a':
                        amp = float(arg[1:])
                    elif arg[0] == 'p':
                        period = float(arg[1:])
                    elif arg[0] == 's':
                        speed = float(arg[1:])
                    elif arg[0] == 'w':
                        wrap_mode = arg

        char_offset = 0 # Since we want our text to move in a wave,
                        # we want to let each character know where it is in the wave.
                        # So they move in harmony. Otherwise they rise and fall all together.
        my_style = DispTextStyle() # This will keep track of what tags and styling to add to each letter
        for kind,text in contents:
            if kind == renpy.TEXT_TEXT:
                # Put the Text into the Wrapper
                char_disp = BounceText(
                    displayable=text, 
                    width=persistent.textbox_width, 
                    height=persistent.textbox_height, 
                    text_style=my_style,
                    char_offset=char_offset,
                    wrap_mode=wrap_mode,
                    amp=amp, 
                    period=period, 
                    speed=speed,
                ) 
                new_list.append((renpy.TEXT_DISPLAYABLE, char_disp))     # Add it back in as a displayable
                char_offset += len(text)
            elif kind == renpy.TEXT_TAG:
                if text.find("image") != -1:
                    tag, _, value = text.partition("=")
                    my_img = renpy.displayable(value)
                    img_disp = BounceText(
                        displayable=my_img,
                        width=persistent.textbox_width, 
                        height=persistent.textbox_height, 
                        text_style=my_style,
                        char_offset=char_offset,
                        wrap_mode=wrap_mode,
                        amp=amp, 
                        period=period, 
                        speed=speed,
                    )
                    new_list.append((renpy.TEXT_DISPLAYABLE, img_disp))
                    char_offset += 1
                elif not my_style.add_tags(text):
                    new_list.append((kind, text))
            # I honestly never got around to testing this. Not often the text
            # already has a displayable in it. Let me know if it breaks though.
            elif kind == renpy.TEXT_DISPLAYABLE:
                char_disp = BounceText(
                    displayable=text,
                    width=persistent.textbox_width, 
                    height=persistent.textbox_height, 
                    text_style=my_style,
                    char_offset=char_offset,
                    wrap_mode=wrap_mode,
                    amp=amp, 
                    period=period, 
                    speed=speed,
                )
                new_list.append((renpy.TEXT_DISPLAYABLE, char_disp))
                char_offset += 1
            else: # Don't touch any other type of content
                new_list.append((kind,text))

        return new_list

    # Letters will start off to the right & invisible. And will then move left while increasing their opacity. Good for meditation and calm text.
    # offset: (int) Offset within the line. Needed to help time start of fade-in with other slow text characters.
    # time: (float) How long in seconds the animation lasts.
    # distance: (int) How many pixels the fade in occurs across
    # wrap mode: (str) Wrap mode (wn - no wrap, wl - wrap letters, ww - wrap words).
    # Example: {fi=[offset]-[time]-[distance]}Text{/fi}
    def fade_in_tag(tag, argument, contents):
        new_list = [ ]
        my_index, fade_time, slide_distance, wrap_mode = 0, 5.0, 100, default_wrap_method
        if argument != "":
            argument = argument.split('-')
            if len(argument) > 0:
                my_index = int(argument[0])
            if len(argument) > 1:
                fade_time = float(argument[1])
            if len(argument) > 2:
                slide_distance = int(argument[2])
            if len(argument) > 3:
                wrap_mode = argument[3]
        my_style = DispTextStyle()
        for kind,text in contents:
            if kind == renpy.TEXT_TEXT:
                char_disp = FadeInText(
                    displayable=text, 
                    width=persistent.textbox_width, 
                    height=persistent.textbox_height, 
                    text_style=my_style,
                    wrap_mode=wrap_mode,
                    char_num=my_index,
                    fade_time=fade_time,
                    slide_distance=slide_distance,
                )
                new_list.append((renpy.TEXT_DISPLAYABLE, char_disp))
                my_index += len(text)
            elif kind == renpy.TEXT_TAG:
                if text.find("image") != -1:
                    tag, _, value = text.partition("=")
                    my_img = renpy.displayable(value)
                    img_disp = FadeInText(
                        displayable=my_img, 
                        width=persistent.textbox_width, 
                        height=persistent.textbox_height, 
                        text_style=my_style,
                        wrap_mode=wrap_mode,
                        char_num=my_index,
                        fade_time=fade_time,
                        slide_distance=slide_distance,
                    )
                    new_list.append((renpy.TEXT_DISPLAYABLE, img_disp))
                    my_index += 1
                elif not my_style.add_tags(text):
                    new_list.append((kind, text))
            else:
                new_list.append((kind,text))
        return new_list

    # Letters change position every frame randomly. Good for very angry or quivering dialogue.
    # range: (int) Letters are confined to a square around their default location. Range determines length of the sides of that square.
    #              Higher values will make it very chaotic while smaller values will make it quite minimal.
    # wrap mode: (str) Wrap mode (wn - no wrap, wl - wrap letters, ww - wrap words).
    # Example: {sc=[range]-[wrap]}Text{/sc}
    def scare_tag(tag, argument, contents):
        new_list = [ ]
        sc_range = 5
        wrap_mode = default_wrap_method
        if argument == "":
            sc_range = 5
        else:
            argument = argument.split('-')
            if len(argument) > 0:
                sc_range = float(argument[0])
            if len(argument) > 1:
                wrap_mode = argument[1]
        my_style = DispTextStyle()
        for kind,text in contents:
            if kind == renpy.TEXT_TEXT:
                char_disp = ScareText(
                    displayable=text, 
                    width=persistent.textbox_width, 
                    height=persistent.textbox_height, 
                    text_style=my_style,
                    wrap_mode=wrap_mode,
                    square=sc_range,
                )
                new_list.append((renpy.TEXT_DISPLAYABLE, char_disp))
            elif kind == renpy.TEXT_TAG:
                if text.find("image") != -1:
                    tag, _, value = text.partition("=")
                    my_img = renpy.displayable(value)
                    img_disp = ScareText(
                        displayable=my_img, 
                        width=persistent.textbox_width, 
                        height=persistent.textbox_height, 
                        text_style=my_style,
                        wrap_mode=wrap_mode,
                        square=sc_range,
                    )
                    new_list.append((renpy.TEXT_DISPLAYABLE, img_disp))
                elif not my_style.add_tags(text):
                    new_list.append((kind, text))
            else:
                new_list.append((kind,text))

        return new_list

    # Letters change their font, color and size every frame.
    # Example: {chaos}Text{/chaos}
    # Honestly more a demonstration of what can be done than useful in it's own right.
    # If you create tags this chaotic, please include a way to turn it off for people with epilepsy.
    def chaos_tag(tag, argument, contents):
        new_list = [ ]
        my_style = DispTextStyle()
        for kind,text in contents:
            if kind == renpy.TEXT_TEXT:
                for char in text:
                    char_disp = ChaosText(my_style.apply_style(char))
                    new_list.append((renpy.TEXT_DISPLAYABLE, char_disp))
            elif kind == renpy.TEXT_TAG:
                if not my_style.add_tags(text):
                    new_list.append((kind, text))
            else:
                new_list.append((kind,text))

        return new_list

    # Letters rotate in place. Good for stylized intros or UI
    # Speed: (int) How fast the rotation will be.
    # Example: {rotat=[speed]}Text{/rotat}
    def rotate_tag(tag, argument, contents):
        new_list = [ ]
        # Argument here will reprsent the desired speed of the rotation.
        if argument == "":
            argument = 400
        else:
            argument = int(argument)
        my_style = DispTextStyle()
        for kind,text in contents:
            if kind == renpy.TEXT_TEXT:
                char_disp = RotateText(
                    displayable=text, 
                    width=persistent.textbox_width, 
                    height=persistent.textbox_height, 
                    text_style=my_style,
                    speed=argument,
                )
                new_list.append((renpy.TEXT_DISPLAYABLE, char_disp))
            elif kind == renpy.TEXT_TAG:
                if text.find("image") != -1:
                    tag, _, value = text.partition("=")
                    my_img = renpy.displayable(value)
                    img_disp = RotateText(
                        displayable=my_img, 
                        width=persistent.textbox_width, 
                        height=persistent.textbox_height, 
                        text_style=my_style,
                        speed=argument,
                    )
                    new_list.append((renpy.TEXT_DISPLAYABLE, img_disp))
                elif not my_style.add_tags(text):
                    new_list.append((kind, text))
            else:
                new_list.append((kind,text))

        return new_list

    # Causes letters to change between two strings every couple of seconds.
    # text1:     (String) First set of characters to display. Should be equal to the length of the characters we're replacing
    # text2:     (String) Second set of characters to display. Should be equal to the length of text1
    # swap_time: (int) Length of time between character swap
    # Arguments are separated by '@'. Length of strings should not exceed length of text they are replacing.
    # Example: {swap=Text@Four@0.5}Text{}
    # This is a pretty static way of doing it mostly made to demonstrate the concept.
    # Included for others to build upon for their needs.
    def swap_tag(tag, argument, contents):
        new_list = [ ]
        if argument == "":
            return contents
        text1, _, argument = argument.partition("@")
        text2, _, argument = argument.partition("@")
        if len(text1) != len(text2):
            new_list.append((renpy.TEXT_TEXT, "ERROR!"))
        swap_time = float(argument)

        my_style = DispTextStyle()
        for kind,text in contents:
            if kind == renpy.TEXT_TEXT:
                # This one replaces the whole text rather than extracting over letters
                # That way it can take up this whole block with its own Text displayable
                char_disp = SwapText(my_style.start_tags(), text1, text2, my_style.end_tags(), swap_time)
                new_list.append((renpy.TEXT_DISPLAYABLE, char_disp))
            elif kind == renpy.TEXT_TAG:
                if not my_style.add_tags(text):
                    new_list.append((kind, text))
            else:
                new_list.append((kind,text))
        return new_list

    # Makes it so the text within moves away from the mouse. More example of what can be done than useful
    # Example: {move}Text{/move}
    def move_tag(tag, argument, contents):
        new_list = [ ]
        my_style = DispTextStyle()
        for kind,text in contents:
            if kind == renpy.TEXT_TEXT:
                for char in text:
                    char_text = Text(my_style.apply_style(char), size=persistent.text_size, outlines=[ (persistent.text_outline, "#000") ])
                    char_disp = MoveText(char_text)
                    new_list.append((renpy.TEXT_DISPLAYABLE, char_disp))
            elif kind == renpy.TEXT_TAG:
                if text.find("image") != -1:
                    tag, _, value = text.partition("=")
                    my_img = renpy.displayable(value)
                    img_disp = MoveText(my_img)
                    new_list.append((renpy.TEXT_DISPLAYABLE, img_disp))
                elif not my_style.add_tags(text):
                    new_list.append((kind, text))
            else:
                new_list.append((kind,text))
        return new_list

    # Some text effects won't allow for a paragraph break if applied to a whole line
    # Which can cause your text to just continue straight off the screen.
    # To amend this, you can insert the {para} tag.
    # This will let the Text displayable holding us know when to wrap.
    # Can also use \n in most cases. But leaving this for people who may already be using it
    # or for cases where \n doesn't work.
    def paragraph_tag(tag, argument):
        return [(renpy.TEXT_PARAGRAPH, "")]

    # This tag is made to automatically wrap several Classes inside one another
    # This is to reduce strain on the render pipeline and memory from nested classes
    # Notes:
        # GradientText and GlitchText are omitted because they were made after the 1.0 release.
        # SwapText and MoveText are omitted for possible issues.
        # SwapText because is not included in this due to it replacing whole sections rather than
        # individual letters. Would be better to embed an Omega inside a SwapText.
        # MoveText because of potential issues of having things like BounceText affect
        # affecting the position of the letter visually.
        # Would be better to have an event call attached to one of those so it can account
        # for the transformations of other tags
    # Argument Notes (all tag args accept same arguments as original tag):
        # BT: BounceText
        # SC: ScareText
        # FI: FadeInText
        # ROT: RotateText
        # CH: ChaosText
    # All tag arguments are seperated by @.
    # Example: {omega=BT=[bt_arg]@SC=[sc_arg]@FI=[fi_arg1]-[fi_arg2]@ROT=[rot_arg]@CH}Text{/omega}
    def omega_tag(tag, argument, contents):
        new_list = [ ]
        if argument == "": # This tag must have arguments
            return contents
        # Variable for each of our tags. None if it takes one argument.
        # Boolean if 0 or many arguments.
        bt_tag = None
        sc_tag = None
        fi_tag = False
        rot_tag = None
        chao_tag = False
        fi_arg_1 = None
        fi_arg_2 = None

        args = [ ]
        arg_count = argument.count('@') # Count how many partitions we will need to make
        for x in range(arg_count):      # Extract all the tags and arguments with them
            new_arg, _, argument = argument.partition('@')
            args.append(new_arg)
        args.append(argument)
        # Determine what tags we'll need to apply and the arguments associated with them
        for arg in args:
            tag, _, value = arg.partition('=')
            if tag == "BT":
                if value is not "":
                    bt_tag = value
                else:
                    bt_tag = 10
            elif tag == "SC":
                if value is not "":
                    bt_tag = value
                else:
                    bt_tag = 5
            # Multiargument tag example. Be sure to use different partitions for these
            elif tag == "FI":
                fi_tag = True
                str1, _, str2 = value.partition('-')
                fi_arg_1 = int(str1)
                fi_arg_2 = float(str2)
            elif tag == "ROT":
                rot_tag = value
            elif tag == "CH":
                chao_tag = True

        my_style = DispTextStyle()
        my_index = 0 # Some Classes will need an index
        for kind,text in contents:
            if kind == renpy.TEXT_TEXT:
                for char in text:
                    # Apply base Wrappers to letter
                    if chao_tag:
                        char_disp = ChaosText(my_style.apply_style(char))
                    else:
                        char_disp = Text(my_style.apply_style(char), size=persistent.text_size, outlines=[ (persistent.text_outline, "#000") ])
                    # Apply further Wraps
                        # Be sure to consider if the order will be important to you
                    if bt_tag is not None:
                        char_disp = BounceText(char_disp, my_index, bt_tag)
                    if sc_tag is not None:
                        char_disp = ScareText(char_disp, sc_tag)
                    if fi_tag:
                        char_disp = FadeInText(char_disp, my_index + fi_arg_1, fi_arg_2)
                    if rot_tag is not None:
                        char_disp = RotateText(char_disp, rot_tag)
                    new_list.append((renpy.TEXT_DISPLAYABLE, char_disp))
            elif kind == renpy.TEXT_TAG:
                if not my_style.add_tags(text):
                    new_list.append((kind, text))
            else:
                new_list.append((kind,text))

        return new_list

    """
    # Template tag function to copy off of.
    def TEMPLATE_tag(tag, argument, contents):
        new_list = [ ]
        if argument == "":
            argument = 5
        my_style = DispTextStyle()
        for kind,text in contents:
            if kind == renpy.TEXT_TEXT:
                for char in text:
                    char_text = Text(my_style.apply_style(char))
                    char_disp = TEMPLATEText(char_text, argument)
                    new_list.append((renpy.TEXT_DISPLAYABLE, char_disp))
            elif kind == renpy.TEXT_TAG:
                if not my_style.add_tags(text):
                    new_list.append((kind, text))
            else:
                new_list.append((kind,text))
        return new_list
    """

    # Define our new text tags
    config.custom_text_tags["bt"] = bounce_tag
    config.custom_text_tags["fi"] = fade_in_tag
    config.custom_text_tags["sc"] = scare_tag
    config.custom_text_tags["rotat"] = rotate_tag
    config.custom_text_tags["chaos"] = chaos_tag
    config.custom_text_tags["swap"] = swap_tag
    config.custom_text_tags["move"] = move_tag
    config.custom_text_tags["omega"] = omega_tag
    config.self_closing_custom_text_tags["para"] = paragraph_tag
    # Template tag function
    #config.custom_text_tags[""] = _tag
