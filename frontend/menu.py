import cv2


class Menu:

    def __init__(self):
        self.colors = [
            (255, 0, 0),
            (0, 255, 0),
            (0, 0, 255),
            (255, 255, 0),
            (255, 0, 255),
        ]

        self.selected_color = (255, 0, 0)
        self.size = 40

        self.close_btn = None  # coordonnées du X

    def draw(self, frame):

        h, w, _ = frame.shape

        # ========= BLACK TRANSPARENT OVERLAY =========
        overlay = frame.copy()
        cv2.rectangle(overlay, (0, 0), (w, h), (0, 0, 0), -1)
        alpha = 0.7
        cv2.addWeighted(overlay, alpha, frame, 1 - alpha, 0, frame)

        # ========= CLOSE BUTTON (X) =========
        x1 = w - 70
        y1 = 20
        x2 = w - 20
        y2 = 70

        cv2.rectangle(frame, (x1, y1), (x2, y2), (60, 60, 60), -1)
        cv2.putText(frame, "X",
                    (x1 + 15, y1 + 40),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    1.2, (255, 255, 255), 3)

        self.close_btn = (x1, y1, x2, y2)

        # ========= CENTER PANEL =========
        panel_w = 400
        panel_h = 400

        px1 = w // 2 - panel_w // 2
        py1 = h // 2 - panel_h // 2
        px2 = px1 + panel_w
        py2 = py1 + panel_h

        cv2.rectangle(frame, (px1, py1), (px2, py2), (40, 40, 40), -1)

        # ========= COLORS =========
        for i, color in enumerate(self.colors):
            cx = px1 + 80
            cy = py1 + 80 + i * 60
            cv2.circle(frame, (cx, cy), 25, color, -1)

        # ========= SIZE =========
        cv2.putText(frame, f"Size: {self.size}",
                    (px1 + 200, py1 + 250),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    0.9, (255, 255, 255), 2)

        # + button
        cv2.rectangle(frame, (px1 + 200, py1 + 280),
                      (px1 + 250, py1 + 330), (80, 80, 80), -1)
        cv2.putText(frame, "+",
                    (px1 + 213, py1 + 318),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    1, (255, 255, 255), 2)

        # - button
        cv2.rectangle(frame, (px1 + 270, py1 + 280),
                      (px1 + 320, py1 + 330), (80, 80, 80), -1)
        cv2.putText(frame, "-",
                    (px1 + 283, py1 + 318),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    1, (255, 255, 255), 2)

        self.panel_area = (px1, py1)
