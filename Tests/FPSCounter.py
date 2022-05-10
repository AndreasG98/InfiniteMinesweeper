import threading
import time


class FPSCounter:
    def __init__(self):

        self.lifetime_frames = 0
        self.start_time = time.time()

        self.average_fps = 0

        t = threading.Thread(name='daemon', target=self.run_fps)
        t.setDaemon(True)
        t.start()

    def increment_frame(self):
        self.lifetime_frames += 1

    def run_fps(self):
        pass

    def fps_lifetime_average(self):
        pass

    # def fps_second_average(self):
    #     pass
