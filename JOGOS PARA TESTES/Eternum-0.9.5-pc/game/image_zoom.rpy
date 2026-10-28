default zoom_position = (0, 0)
default img_zoom_value = 1.0

init python:
    def get_coords(old_pos, img_size, update_zoom=False):
        virtual_x = config.screen_width
        virutal_y = config.screen_height

        m_x, m_y = renpy.get_mouse_pos()

        # Get the change relative to the center of the screen
        # Don't update if only zoom changed
        if update_zoom:
            x_change = 0
            y_change = 0
        else:
            x_change = m_x - virtual_x / 2
            y_change = m_y - virutal_y / 2
        
        # Update coordinates
        new_x = old_pos[0] - x_change 
        new_y = old_pos[1] - y_change

        # Bound coordinates to image size
        if new_x > 0:
            new_x = 0
        elif new_x < virtual_x - img_size[0] * img_zoom_value:
            new_x = virtual_x - img_size[0] * img_zoom_value

        if new_y > 0:
            new_y = 0
        elif new_y < virutal_y - img_size[1] * img_zoom_value:
            new_y = virutal_y - img_size[1] * img_zoom_value

        return new_x, new_y

    def update_position(img_size):
        store.zoom_position = get_coords(store.zoom_position, img_size)

    def update_zoom(img_size):
        # Bound coodrinates to image size on zoom change
        store.zoom_position = get_coords(store.zoom_position, img_size, update_zoom=True)

transform move_to_position(pos_x, pos_y):
    linear 1.0: 
        xpos pos_x 
        ypos pos_y 
        zoom img_zoom_value

screen zoom_image(img):
    modal True
    $ img_size = renpy.image_size(img)

    image img:
        at move_to_position(int(zoom_position[0]), int(zoom_position[1]))

    key "mousedown_1" action Function(update_position, img_size)

    vbox:
        ypos 100
        spacing 5
        text f"xpos {zoom_position[0]}" # xpos value
        text f"ypos {zoom_position[1]}" # ypos value
        text f"zoom {img_zoom_value}" # zoom value

    # Change min/max if needed
    bar value VariableValue("img_zoom_value", min=0.01, max=3.0, action=Function(update_zoom, img_size))

    

