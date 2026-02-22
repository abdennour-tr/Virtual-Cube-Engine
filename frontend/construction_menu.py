import cv2

class ConstructionMenu:

    def __init__(self):
        self.icons = {
            "wall": (50, 20, 120, 80),
            "tower": (140, 20, 210, 80),
            "stairs": (230, 20, 300, 80)
        }
        self.selected = None

    def draw(self, frame):
        for name, (x1,y1,x2,y2) in self.icons.items():
            color = (0,255,255) if self.selected == name else (60,60,60)
            cv2.rectangle(frame, (x1,y1), (x2,y2), color, -1)
            cv2.putText(frame, name.upper(),
                        (x1+5, y1+40),
                        cv2.FONT_HERSHEY_SIMPLEX,
                        0.6, (255,255,255), 2)

    def handle_click(self, x, y):
        for name, (x1,y1,x2,y2) in self.icons.items():
            if x1 < x < x2 and y1 < y < y2:
                self.selected = name
                return name