def snap_to_grid(x, y, size):
    gx = round(x / size) * size
    gy = round(y / size) * size
    return gx, gy


def is_adjacent(last_cube, x, y):
    s = last_cube.size
    valid_positions = [
        (last_cube.x + s, last_cube.y),
        (last_cube.x - s, last_cube.y),
        (last_cube.x, last_cube.y + s),
        (last_cube.x, last_cube.y - s),
    ]
    return (x, y) in valid_positions
