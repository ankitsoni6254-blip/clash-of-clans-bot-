from vision import Vision
import time


class Waits:

    def __init__(self, vision: Vision):
        self.vision = vision

    def pixel(self, position, color, timeout=30):

        start = time.time()

        while time.time() - start < timeout:

            self.vision.refresh()

            if self.vision.pixel(position) == color:
                return True

            time.sleep(0.1)

        return False
