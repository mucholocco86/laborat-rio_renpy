




init 84 python:
    
    import math
    import os
    
    GODSON_SCRUB_PREVIEW_INTERVAL = 1.0
    GODSON_SCRUB_PREVIEW_TILE_WIDTH = 400
    GODSON_SCRUB_PREVIEW_TILE_HEIGHT = 225
    GODSON_SCRUB_PREVIEW_COLUMNS = 8
    GODSON_SCRUB_PREVIEW_ROWS = 5
    GODSON_SCRUB_PREVIEW_TILES_PER_SHEET = (
        GODSON_SCRUB_PREVIEW_COLUMNS * GODSON_SCRUB_PREVIEW_ROWS
    )
    GODSON_SCRUB_PREVIEW_WIDTH = 640
    GODSON_SCRUB_PREVIEW_HEIGHT = 360
    GODSON_SCRUB_PREVIEW_BORDER = 6
    GODSON_SCRUB_PREVIEW_CARD_WIDTH = (
        GODSON_SCRUB_PREVIEW_WIDTH + (GODSON_SCRUB_PREVIEW_BORDER * 2)
    )
    GODSON_SCRUB_PREVIEW_CARD_HEIGHT = (
        GODSON_SCRUB_PREVIEW_HEIGHT + (GODSON_SCRUB_PREVIEW_BORDER * 2)
    )
    GODSON_SCRUB_PREVIEW_Y = 1432
    
    _godson_scrub_preview_cache = {}
    _godson_scrub_sheet_available = {}
    
    def godson_scrub_preview_format_time(value):
        seconds = max(0, int(value or 0))
        minutes, seconds = divmod(seconds, 60)
        
        if minutes >= 60:
            hours, minutes = divmod(minutes, 60)
            return "{}:{:02d}:{:02d}".format(hours, minutes, seconds)
        
        return "{}:{:02d}".format(minutes, seconds)
    
    def godson_scrub_preview_slug(movie_path):
        normalized = str(movie_path or "").replace("\\", "/")
        filename = normalized.rsplit("/", 1)[-1]
        return os.path.splitext(filename)[0].lower()
    
    def godson_scrub_preview_image(movie_path, position, duration):
        if not movie_path:
            return None
        
        duration = max(0.0, float(duration or 0.0))
        position = max(0.0, float(position or 0.0))
        
        if duration > 0.0:
            position = min(position, duration)
            max_index = max(
                0,
                int(math.ceil(duration / GODSON_SCRUB_PREVIEW_INTERVAL)) - 1,
            )
        else:
            max_index = 0
        
        frame_index = min(
            int(position / GODSON_SCRUB_PREVIEW_INTERVAL),
            max_index,
        )
        sheet_index, tile_index = divmod(
            frame_index,
            GODSON_SCRUB_PREVIEW_TILES_PER_SHEET,
        )
        column = tile_index % GODSON_SCRUB_PREVIEW_COLUMNS
        row = tile_index // GODSON_SCRUB_PREVIEW_COLUMNS
        slug = godson_scrub_preview_slug(movie_path)
        sheet_path = "gui/media_previews/{}/sheet_{:03d}.jpg".format(
            slug,
            sheet_index + 1,
        )
        
        available = _godson_scrub_sheet_available.get(sheet_path)
        if available is None:
            available = renpy.loadable(sheet_path)
            _godson_scrub_sheet_available[sheet_path] = available
        
        if not available:
            return None
        
        cache_key = (sheet_path, tile_index)
        preview = _godson_scrub_preview_cache.get(cache_key)
        
        if preview is None:
            preview = Transform(
                sheet_path,
                crop=(
                    column * GODSON_SCRUB_PREVIEW_TILE_WIDTH,
                    row * GODSON_SCRUB_PREVIEW_TILE_HEIGHT,
                    GODSON_SCRUB_PREVIEW_TILE_WIDTH,
                    GODSON_SCRUB_PREVIEW_TILE_HEIGHT,
                ),
                size=(
                    GODSON_SCRUB_PREVIEW_WIDTH,
                    GODSON_SCRUB_PREVIEW_HEIGHT,
                ),
            )
            
            
            
            if len(_godson_scrub_preview_cache) >= 160:
                _godson_scrub_preview_cache.clear()
            
            _godson_scrub_preview_cache[cache_key] = preview
        
        return preview
    
    def godson_scrub_preview_state(player):
        if player == "gallery":
            visible = (
                gallery_media_preview_focused
                or gallery_media_scrubbing
                or gallery_media_preview_hold_ticks > 0
            )
            position = gallery_media_position
            duration = gallery_media_duration
        else:
            visible = (
                godson_cutscene_preview_focused
                or godson_cutscene_scrubbing
                or godson_cutscene_preview_hold_ticks > 0
            )
            position = godson_cutscene_position
            duration = godson_cutscene_duration
        
        return visible, float(position or 0.0), float(duration or 0.0)
    
    class GodsonScrubPreviewOverlay(renpy.Displayable):
        """Draws the seek thumbnail directly over the active movie.

        This deliberately avoids DynamicDisplayable. On some renderers the
        dynamic child was updated but never composited over a hardware-backed
        movie surface, leaving the seek functional with no visible preview.
        """
        
        def __init__(
            self,
            player,
            movie_path,
            bar_left,
            bar_width,
            adjustment=None,
            **kwargs
        ):
            super(GodsonScrubPreviewOverlay, self).__init__(**kwargs)
            self.player = player
            self.movie_path = movie_path
            self.bar_left = float(bar_left)
            self.bar_width = float(bar_width)
            self.adjustment = adjustment
            self.card_border = Solid("#D8AD4C")
            self.time_background = Solid("#07090DDD")
            self.marker = Transform(
                "gui/christmas_noir/slider_thumb_idle.png",
                size=(40, 40),
            )
        
        def render(self, width, height, st, at):
            
            
            
            
            canvas_width = max(int(width or 0), 3840)
            canvas_height = max(int(height or 0), 2160)
            rv = renpy.Render(canvas_width, canvas_height)
            renpy.redraw(self, 0.03)
            
            visible, position, duration = godson_scrub_preview_state(
                self.player
            )
            if not visible:
                return rv
            
            
            
            
            if self.adjustment is not None:
                try:
                    position = float(self.adjustment.value)
                    duration = max(duration, float(self.adjustment.range))
                except Exception:
                    pass
            
            preview = godson_scrub_preview_image(
                self.movie_path,
                position,
                duration,
            )
            if preview is None:
                return rv
            
            ratio = 0.0
            if duration > 0.0:
                ratio = max(0.0, min(position / duration, 1.0))
            
            thumb_x = self.bar_left + (ratio * self.bar_width)
            card_x = thumb_x - (GODSON_SCRUB_PREVIEW_CARD_WIDTH / 2.0)
            card_x = max(
                36.0,
                min(card_x, 3804.0 - GODSON_SCRUB_PREVIEW_CARD_WIDTH),
            )
            card_x = int(card_x)
            card_y = int(GODSON_SCRUB_PREVIEW_Y)
            
            border_render = renpy.render(
                self.card_border,
                GODSON_SCRUB_PREVIEW_CARD_WIDTH,
                GODSON_SCRUB_PREVIEW_CARD_HEIGHT,
                st,
                at,
            )
            rv.blit(border_render, (card_x, card_y))
            
            preview_render = renpy.render(
                preview,
                GODSON_SCRUB_PREVIEW_WIDTH,
                GODSON_SCRUB_PREVIEW_HEIGHT,
                st,
                at,
            )
            preview_x = card_x + GODSON_SCRUB_PREVIEW_BORDER
            preview_y = card_y + GODSON_SCRUB_PREVIEW_BORDER
            rv.blit(preview_render, (preview_x, preview_y))
            
            
            
            
            horizontal_border = renpy.render(
                self.card_border,
                GODSON_SCRUB_PREVIEW_CARD_WIDTH,
                GODSON_SCRUB_PREVIEW_BORDER,
                st,
                at,
            )
            vertical_border = renpy.render(
                self.card_border,
                GODSON_SCRUB_PREVIEW_BORDER,
                GODSON_SCRUB_PREVIEW_CARD_HEIGHT,
                st,
                at,
            )
            rv.blit(horizontal_border, (card_x, card_y))
            rv.blit(
                horizontal_border,
                (
                    card_x,
                    card_y
                    + GODSON_SCRUB_PREVIEW_CARD_HEIGHT
                    - GODSON_SCRUB_PREVIEW_BORDER,
                ),
            )
            rv.blit(vertical_border, (card_x, card_y))
            rv.blit(
                vertical_border,
                (
                    card_x
                    + GODSON_SCRUB_PREVIEW_CARD_WIDTH
                    - GODSON_SCRUB_PREVIEW_BORDER,
                    card_y,
                ),
            )
            
            time_width = 122
            time_height = 42
            time_x = preview_x + 10
            time_y = (
                preview_y
                + GODSON_SCRUB_PREVIEW_HEIGHT
                - time_height
                - 10
            )
            time_background_render = renpy.render(
                self.time_background,
                time_width,
                time_height,
                st,
                at,
            )
            rv.blit(time_background_render, (time_x, time_y))
            
            time_displayable = Text(
                godson_scrub_preview_format_time(position),
                style="godson_scrub_preview_time_text",
                xsize=time_width,
                text_align=0.5,
            )
            time_render = renpy.render(
                time_displayable,
                time_width,
                time_height,
                st,
                at,
            )
            rv.blit(time_render, (time_x, time_y))
            
            marker_render = renpy.render(self.marker, 40, 40, st, at)
            rv.blit(
                marker_render,
                (
                    int(thumb_x - 20),
                    card_y + GODSON_SCRUB_PREVIEW_CARD_HEIGHT + 8,
                ),
            )
            
            return rv

init 90 style godson_scrub_preview_time_text is text:
    font gui.interface_text_font
    size 30
    color "#FFE6A8"
    outlines [(3, "#000000EE", 0, 1)]
    yalign 0.5
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
