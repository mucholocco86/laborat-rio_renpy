screen Borders (thickness=5, color="#ade"):
    frame area (0.0, 0.0, 1.0, thickness) background Solid (color)              # top-left to top-right
    frame area (0.0, 0.0, thickness, 1.0) background Solid (color)              # top-left to bottom-left
    frame area (0.0, 1.0, 1.0, thickness) background Solid (color) yanchor 1.0  # bottom-left to bottom-right
    frame area (1.0, 0.0, thickness, 1.0) background Solid (color) xanchor 1.0  # top-right to bottom-right