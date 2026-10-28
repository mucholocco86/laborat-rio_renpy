init -1 python:
    import pygame
    LOCK_PICK_REPAIR = pygame.event.register("LOCK_PICK_REPAIR")
    LOCK_OPENED = pygame.event.register("LOCK_OPENED")
    renpy_default_width = config.screen_width
    renpy_default_height = config.screen_height
    # Images
    lock_plate_image = "images/lock/lock_plate.png"
    lock_cylinder_image = "images/lock/lock_cylinder.png"
    lock_tension_image = "images/lock/lock_tension.png"
    lock_pick_image = "images/lock/lock_pick.png"
    lock_pick_broken_image = "images/lock/lock_pick_broken.png"
    # Audio
    lock_moving_audio = "audio/sfx/lock/lock_moving.mp3"
    lock_jiggling_audio = "audio/sfx/lock/lock_jiggling.mp3"
    lock_moving_back_audio = "audio/sfx/lock/lock_moving_back.mp3"
    lock_pick_break_audio = "audio/sfx/lock/lock_pick_break.mp3"
    lock_unlock_audio = "audio/sfx/lock/lock_unlock.mp3"
    # SFX channels
    lock_move_channel = "lock_move"
    lock_click_channel = "lock_click"
    renpy.music.register_channel(lock_move_channel, mixer="sfx", loop=True)
    renpy.music.register_channel(lock_click_channel, mixer="sfx", loop=False, tight=True)

    class LockGame(renpy.Displayable):

        def __init__(self, sweet_angle=10, pick_dmg=1.5, attempts=3, resize=renpy_default_width, **kwargs):
            """
            Custom Displayable for Lockpick minigame. Result will be stored in `_return` variable.

            * sweet_angle - How big is the window for sweet spot. The lower the number, the more precise you need to be
            * pick_dmg - How fast the pick breaks
            * attempts - Amount of attempts
            * resize - Size of the Displayable on screen
            """
            super(LockGame, self).__init__(**kwargs)

            # Set up images and their sizes and position
            self.width = resize
            self.height = resize
            self.lock_plate_image = Transform(child=lock_plate_image, xsize=resize, ysize=resize)
            self.lock_cylinder_image = Transform(child=lock_cylinder_image, xsize=resize, ysize=resize)
            self.lock_tension_image = Transform(child=lock_tension_image, xsize=resize, ysize=resize)
            self.lock_pick_image = Transform(child=lock_pick_image, xsize=resize, ysize=resize)
            self.lock_pick_broken_image = Transform(child=lock_pick_broken_image, xsize=resize, ysize=resize)
            self.offset = (resize * 2 ** 0.5 - resize) / 2 # Offset rotation padding

            # Constants
            self.cylinder_min = 0
            self.cylinder_target = 90
            self.pick_min = 0
            self.pick_max = 180
            self.pick_health_max = 100
            self.sweet_angle_min = 1
            self.sweet_angle_max = 30

            # Configurable
            self.cylinder_jiggle = 2 # Random jiggle for the cylinder, degrees
            self.tension_jiggle = 4 # Random jiggle for the bottom pick, degrees
            self.cylinder_move_speed = 1.0 # Speed of the cylinder, degrees/frametime
            self.cylinder_reset_speed = 1.5 # Speed of the cylinder going back, degrees/frametime
            self.pick_broken_delay = 500 # Delay after breaking a pick, ms
            self.lock_opened_delay = 500 # Delay after opening the lock, ms

            # Variables
            self.cylinder_pos = 0 # Current position of the cylinder
            self.cylinder_max = 90 # Current maximum rotation allowed for the cylinder
            self.cylinder_try_rotate = False # Whether the cylinder is attempting to rotate
            self.cylinder_can_rotate = False # Whether the cylinder is allowed to rotate
            self.cylinder_released = False # Whether the cylinder just got released
            self.pick_pos = 90 # Current position of the pick
            self.pick_can_rotate = True # Whether the pick is allowed to rotate
            self.pick_broke = False # Whether the pick just broke
            self.disabled = False # Whether interactions are disabled

            self.attempts_left = attempts
            self.pick_health = self.pick_health_max
            self.sweet_spot = renpy.random.randint(self.pick_min, self.pick_max)
            self.pick_dmg = pick_dmg
            self.sweet_angle = sweet_angle
            if self.sweet_angle < self.sweet_angle_min:
                self.sweet_angle = self.sweet_angle_min
            elif self.sweet_angle > self.sweet_angle_max:
                self.sweet_angle = self.sweet_angle_max

        # Handle click
        def event(self, ev, x, y, st):
            LEFT_MOUSE_BUTTON = 1

            # Handle successful opening
            if ev.type == LOCK_OPENED:
                pygame.time.set_timer(LOCK_OPENED, 0)
                return True

            # Re-enable after pick is replaced
            if ev.type == LOCK_PICK_REPAIR:
                pygame.time.set_timer(LOCK_PICK_REPAIR, 0)
                self.pick_broke = False
                self.pick_can_rotate = True
                self.disabled = False
                self.cylinder_released = True
                
                self.attempts_left -= 1
                self.pick_health = self.pick_health_max
                # Check if last pick was broken
                if self.attempts_left == 0:
                    # Return with False
                    return False
                else:
                    renpy.restart_interaction()

            # Ignore when pick is broken
            if self.disabled:
                return None

            # Ignore touch on top half of the screen when on mobile
            if ev.type == pygame.MOUSEBUTTONDOWN and renpy.mobile and y < (self.height / 2):
                return None

            if ev.type == pygame.MOUSEBUTTONDOWN and ev.button == LEFT_MOUSE_BUTTON:
                self.cylinder_try_rotate = True
                self.cylinder_released = False
            elif ev.type == pygame.MOUSEBUTTONUP and ev.button == LEFT_MOUSE_BUTTON:
                renpy.sound.stop(channel=lock_move_channel)
                self.cylinder_try_rotate = False
                self.cylinder_released = True
                self.pick_can_rotate = True
                self.pick_broke = False

        def disable_interactions(self):
            """ Disable all user interactions """
            self.pick_can_rotate = False
            self.cylinder_can_rotate = False
            self.cylinder_try_rotate = False
            self.disabled = True

        def render(self, width, height, st, at):
            # Handle pick rotation
            if self.pick_can_rotate and not self.disabled:
                x, y = renpy.get_mouse_pos()

                # Ignore movement on bottom half of the screen when on mobile
                if renpy.mobile:
                    if y < (renpy_default_height / 2):
                        self.pick_pos = x / (renpy_default_width / 360.0) - 90
                else:
                    self.pick_pos = x / (renpy_default_width / 360.0) - 90

                if self.pick_pos > self.pick_max:
                    self.pick_pos = self.pick_max
                elif self.pick_pos < self.pick_min:
                    self.pick_pos = self.pick_min

                self.cylinder_can_rotate = True

                # Get max rotation for cylinder
                if abs(self.pick_pos - self.sweet_spot) < self.sweet_angle:
                    self.cylinder_max = self.cylinder_target
                else:
                    self.cylinder_max = self.cylinder_target - abs(self.pick_pos - self.sweet_spot) * (self.sweet_angle_max / self.sweet_angle)

                if self.cylinder_max < self.cylinder_min:
                    self.cylinder_max = self.cylinder_min
            
            angle1 = 0
            angle2 = 0
            # Handle cylinder rotation
            if self.cylinder_try_rotate and not self.disabled:
                if self.cylinder_can_rotate:
                    self.cylinder_pos += self.cylinder_move_speed

                    if self.cylinder_pos > self.cylinder_max:
                        self.cylinder_pos = self.cylinder_max

                        if self.cylinder_pos == self.cylinder_target: # Unlocked
                            renpy.sound.stop(channel=lock_move_channel)
                            renpy.sound.play(lock_unlock_audio, channel=lock_click_channel)
                            self.disable_interactions()
                            pygame.time.set_timer(LOCK_OPENED, self.lock_opened_delay)
                        else: # Stuck
                            self.pick_can_rotate = False
                            if not renpy.sound.is_playing(lock_move_channel):
                                renpy.sound.play(lock_jiggling_audio, channel=lock_move_channel)

                            # Jiggling
                            angle1 = renpy.random.randint(-self.cylinder_jiggle, self.cylinder_jiggle)
                            angle2 = renpy.random.randint(-self.tension_jiggle, self.tension_jiggle)

                            # Handle pick breaking
                            self.pick_health -= self.pick_dmg
                            if self.pick_health < 0: # Broke
                                renpy.sound.stop(channel=lock_move_channel)
                                renpy.sound.play(lock_pick_break_audio, channel=lock_click_channel)
                                # pick_image = self.lock_pick_broken_image
                                self.pick_broke = True
                                self.disable_interactions()
                                pygame.time.set_timer(LOCK_PICK_REPAIR, self.pick_broken_delay)
                    else:
                        if not renpy.sound.is_playing(lock_move_channel):
                            renpy.sound.play(lock_moving_audio, channel=lock_move_channel)
            else: # Released
                if self.cylinder_released:
                    if self.cylinder_pos > 15 and not renpy.sound.is_playing(lock_move_channel):
                        renpy.sound.play(lock_moving_back_audio, channel=lock_move_channel)
                    self.pick_can_rotate = True
                    self.cylinder_pos -= self.cylinder_reset_speed

                    if self.cylinder_pos < self.cylinder_min:
                        self.cylinder_pos = self.cylinder_min
                        self.cylinder_released = False
                        renpy.sound.stop(channel=lock_move_channel)
            
            # Move or break the pick
            if self.pick_broke:
                pick_image = self.lock_pick_broken_image
            else:
                pick_image = self.lock_pick_image
            pick = Transform(child=pick_image, rotate=self.pick_pos, subpixel=True)
            
            # Move cylinder and bottom pick
            cylinder = Transform(child=self.lock_cylinder_image, rotate=self.cylinder_pos + angle1, subpixel=True)
            tension = Transform(child=self.lock_tension_image, rotate=self.cylinder_pos + angle2, subpixel=True)
            

            # Render everything
            lock_plate_render = renpy.render(self.lock_plate_image, width, height, st, at)
            lock_cylinder_render = renpy.render(cylinder, width, height, st, at)
            lock_tension_render = renpy.render(tension, width, height, st, at)
            lock_pick_render = renpy.render(pick, width, height, st, at)

            render = renpy.Render(self.width, self.height)

            render.blit(lock_plate_render, (0, 0), main=True)
            render.blit(lock_cylinder_render, (-self.offset, -self.offset))
            render.blit(lock_tension_render, (-self.offset, -self.offset))
            render.blit(lock_pick_render, (-self.offset, -self.offset))

            renpy.redraw(self, 0)

            return render

screen lock_game(lock):
    modal True
    add lock:
        align (0.5, 0.5)
    text "Attempts: [lock.attempts_left]":
        style "mytext"
        size 45
        align (0.5, 0.1)

default lock_success = False

            

            


