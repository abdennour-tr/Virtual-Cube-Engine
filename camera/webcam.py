import cv2

class Webcam:
    def __init__(self, index=0):
        self.cap = cv2.VideoCapture(index)

    def read(self):
        ret, frame = self.cap.read()
        return cv2.flip(frame, 1) if ret else None

    def release(self):
        self.cap.release()
