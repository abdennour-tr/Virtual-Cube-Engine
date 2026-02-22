from cube_engine.cube import Cube


class CubeManager:
    def __init__(self, size):
        self.cubes = []
        self.size = size
        self.color = (255, 0, 0)

    # =========================
    # CLEAR ALL
    # =========================
    def clear_all(self):
        self.cubes.clear()

    # =========================
    # CHECK EXIST
    # =========================
    def _cube_exists(self, x, y):
        for cube in self.cubes:
            if cube.x == x and cube.y == y:
                return True
        return False

    # =========================
    # ADD SINGLE CUBE
    # =========================
    def add_cube(self, x, y):
        if not self._cube_exists(x, y):
            self.cubes.append(Cube(x, y, self.size, self.color))
            return True
        return False

    # =========================
    # BUILD WALL
    # =========================
    def build_wall(self, x, y, length=5):
        for i in range(length):
            nx = x + i * self.size
            if not self._cube_exists(nx, y):
                self.cubes.append(Cube(nx, y, self.size, self.color))

    # =========================
    # BUILD TOWER
    # =========================
    def build_tower(self, x, y, height=5):
        for i in range(height):
            ny = y - i * self.size
            if not self._cube_exists(x, ny):
                self.cubes.append(Cube(x, ny, self.size, self.color))

    # =========================
    # BUILD STAIRS
    # =========================
    def build_stairs(self, x, y, steps=5):
        for i in range(steps):
            nx = x + i * self.size
            ny = y - i * self.size
            if not self._cube_exists(nx, ny):
                self.cubes.append(Cube(nx, ny, self.size, self.color))

    # =========================
    # REMOVE
    # =========================
    def remove_at(self, x, y):
        for cube in self.cubes:
            if cube.contains(x, y):
                self.cubes.remove(cube)
                return True
        return False

    # =========================
    #  UNDO
    # =========================
    def undo(self):
        if self.cubes:
            self.cubes.pop()