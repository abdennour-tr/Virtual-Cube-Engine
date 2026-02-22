from gestures.custom_gestures import pinch


class UIManager:

    def __init__(self, menu, gesture_manager):
        self.menu = menu
        self.gesture_manager = gesture_manager
        self.cooldown = 0

    def handle(self, right_hand, w, h):

        if not right_hand:
            return

        if self.cooldown > 0:
            self.cooldown -= 1

        index = right_hand.landmark[8]
        thumb = right_hand.landmark[4]

        ix, iy = int(index.x * w), int(index.y * h)
        tx, ty = int(thumb.x * w), int(thumb.y * h)

        if not pinch((ix, iy), (tx, ty)):
            return

        # ===== CLOSE BUTTON =====
        x1, y1, x2, y2 = self.menu.close_btn
        if x1 < ix < x2 and y1 < iy < y2:
            self.gesture_manager.close_menu()
            self.cooldown = 20
            return

        px1, py1 = self.menu.panel_area

        # ===== COLOR SELECT =====
        for i, color in enumerate(self.menu.colors):
            cx = px1 + 80
            cy = py1 + 80 + i * 60

            if abs(ix - cx) < 30 and abs(iy - cy) < 30:
                self.menu.selected_color = color
                self.cooldown = 15

        # ===== SIZE + =====
        if px1 + 200 < ix < px1 + 250 and py1 + 280 < iy < py1 + 330:
            self.menu.size += 5
            self.cooldown = 15

        # ===== SIZE - =====
        if px1 + 270 < ix < px1 + 320 and py1 + 280 < iy < py1 + 330:
            self.menu.size = max(10, self.menu.size - 5)
            self.cooldown = 15
