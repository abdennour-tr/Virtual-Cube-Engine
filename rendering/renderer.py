import cv2
import numpy as np


class Renderer:
    def __init__(self):
        self.active_position = None
        self.alpha = 0.25  # transparence globale du cube

    # =========================
    # DESSIN FACE TRANSPARENTE
    # =========================
    def draw_face(self, frame, pts, color,cube):
        overlay = frame.copy()
        cv2.fillPoly(overlay, [pts], color)
        cv2.addWeighted(overlay, self.alpha, frame, 1 - self.alpha, 0, frame)

        # ARÊTES BLEUES
        cv2.polylines(frame, [pts], True, cube.color, 2)

    # =========================
    # CUBE 3D TRANSPARENT
    # =========================
    def draw_cube(self, frame, cube):
        x, y, s = cube.x, cube.y, cube.size
        d = s // 3

        front = np.array([
            [x, y],
            [x + s, y],
            [x + s, y + s],
            [x, y + s]
        ])

        top = np.array([
            [x, y],
            [x + d, y - d],
            [x + s + d, y - d],
            [x + s, y]
        ])

        right = np.array([
            [x + s, y],
            [x + s + d, y - d],
            [x + s + d, y + s - d],
            [x + s, y + s]
        ])

        # ===== UTILISER LA COULEUR DU CUBE =====
        base = cube.color

        # légère variation pour effet 3D
        col_front = base
        col_top = tuple(min(255, c + 40) for c in base)
        col_right = tuple(max(0, c - 40) for c in base)

        self.draw_face(frame, top, col_top , cube)
        self.draw_face(frame, right, col_right , cube)
        self.draw_face(frame, front, col_front , cube)

        if self.active_position == (cube.x, cube.y):
            cv2.polylines(frame, [front], True, (0, 180, 255), 3)

    # =========================
    # RENDU GLOBAL (Z-ORDER)
    # =========================
    def draw_cubes(self, frame, cubes):
        cubes_sorted = sorted(cubes, key=lambda c: c.x + c.y)
        for cube in cubes_sorted:
            self.draw_cube(frame, cube)

    # =========================
    # HOVER ÉCRITURE
    # =========================
    def draw_hover(self, frame, x, y, size):
        d = size // 3
        pts = np.array([
            [x, y],
            [x + size, y],
            [x + size + d, y - d],
            [x + d, y - d]
        ])
        cv2.polylines(frame, [pts], True, (0, 180, 255), 2)

    # =========================
    # DELETE HOVER
    # =========================
    def draw_delete_hover(self, frame, cube):
        cv2.rectangle(
            frame,
            (cube.x, cube.y),
            (cube.x + cube.size, cube.y + cube.size),
            (0, 0, 255),
            2
        )

