import time

class PerformanceMonitor:
    def __init__(self):
        self.prev_time = time.time()
        self.fps = 0

    def update(self):
        current = time.time()
        delta = current - self.prev_time
        self.prev_time = current

        if delta > 0:
            self.fps = int(1 / delta)

        return self.fps
    

class SessionTimer:
    def __init__(self):
        self.start_time = time.time()

    def get_elapsed(self):
        return int(time.time() - self.start_time)