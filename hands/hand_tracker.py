import mediapipe as mp
import cv2

class HandTracker:
    def __init__(self):
        self.mp_hands = mp.solutions.hands
        self.hands = self.mp_hands.Hands(
            max_num_hands=2,
            min_detection_confidence=0.7,
            min_tracking_confidence=0.7
        )
        self.drawer = mp.solutions.drawing_utils

    def process(self, frame):
        rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        return self.hands.process(rgb)

    def draw(self, frame, results):
        if not results.multi_hand_landmarks:
            return

        h, w, _ = frame.shape

        for hand, handedness in zip(
            results.multi_hand_landmarks,
            results.multi_handedness
        ):
            self.drawer.draw_landmarks(
                frame, hand, self.mp_hands.HAND_CONNECTIONS
            )

            label = handedness.classification[0].label
            wrist = hand.landmark[0]

            x = int(wrist.x * w)
            y = int(wrist.y * h)

            color = (0, 255, 0) if label == "Left" else (255, 0, 0)

            cv2.putText(
                frame,
                label.upper(),
                (x - 30, y + 30),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.7,
                color,
                2
            )
