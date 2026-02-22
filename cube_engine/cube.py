class Cube:
    def __init__(self, x, y, size, color):
        self.x = x
        self.y = y
        self.size = size
        self.color = color

    def contains(self, px, py):
        return (
            self.x <= px <= self.x + self.size
            and self.y <= py <= self.y + self.size
        )
