import time


class DirectionBurstDetector:

    def __init__(self):
        self.positions = []
        self.last_trigger_time = 0
        self.cooldown = 1.0  # secondes

    def update(self, x):
        now = time.time()

        # limiter mémoire
        self.positions.append((x, now))
        self.positions = self.positions[-20:]

        # cooldown pour éviter spam
        if now - self.last_trigger_time < self.cooldown:
            return None

        if len(self.positions) < 6:
            return None

        directions = []

        for i in range(1, len(self.positions)):
            dx = self.positions[i][0] - self.positions[i - 1][0]

            if abs(dx) > 25:  # seuil de mouvement
                if dx > 0:
                    directions.append("right")
                else:
                    directions.append("left")

        # garder seulement les 4 derniers changements
        directions = directions[-4:]

        # Pattern attendu : droite/gauche alterné 4 fois
        if len(directions) == 4:
            if (
                directions[0] != directions[1]
                and directions[1] != directions[2]
                and directions[2] != directions[3]
            ):
                self.last_trigger_time = now
                return directions[-1]  # dernière direction

        return None
