import numpy as np
import cv2

class Heatmap:
    def __init__(self, width, height):
        self.map = np.zeros((height, width), dtype=np.float32)

    def add_point(self, x, y):
        if 0 <= y < self.map.shape[0] and 0 <= x < self.map.shape[1]:
            self.map[y, x] += 1

    def render(self, frame):
        normalized = cv2.normalize(self.map, None, 0, 255, cv2.NORM_MINMAX)
        colored = cv2.applyColorMap(normalized.astype(np.uint8), cv2.COLORMAP_JET)
        overlay = cv2.addWeighted(frame, 0.7, colored, 0.3, 0)
        return overlay