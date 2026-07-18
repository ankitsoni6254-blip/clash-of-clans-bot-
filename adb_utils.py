import subprocess
import cv2
import numpy as np
import time


class ADB:

    def __init__(self, device=None):
        self.device = device

    def _cmd(self, *args):
        cmd = ["adb"]

        if self.device:
            cmd += ["-s", self.device]

        cmd += list(args)

        return subprocess.run(
            cmd,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )

    def check_device(self):

        result = self._cmd("devices")

        lines = result.stdout.splitlines()

        devices = []

        for line in lines:

            if "\tdevice" in line:

                devices.append(line.split()[0])

        if not devices:
            raise Exception("No Android device found.")

        if self.device is None:
            self.device = devices[0]

        return self.device

    def tap(self, x, y):

        self._cmd(
            "shell",
            "input",
            "tap",
            str(x),
            str(y)
        )

    def swipe(self, x1, y1, x2, y2, duration=200):

        self._cmd(
            "shell",
            "input",
            "swipe",
            str(x1),
            str(y1),
            str(x2),
            str(y2),
            str(duration)
        )

    def screenshot(self):

        cmd = ["adb"]

        if self.device:
            cmd += ["-s", self.device]

        cmd += [
            "exec-out",
            "screencap",
            "-p"
        ]

        raw = subprocess.check_output(cmd)

        img = np.frombuffer(raw, np.uint8)

        return cv2.imdecode(img, cv2.IMREAD_COLOR)

    def pixel(self, x, y):

        img = self.screenshot()

        b, g, r = img[y, x]

        return int(r), int(g), int(b)

    def wait_pixel(
        self,
        x,
        y,
        minimum,
        maximum,
        delay=0.1
    ):

        while True:

            r, g, b = self.pixel(x, y)

            if (
                minimum[0] <= r <= maximum[0]
                and
                minimum[1] <= g <= maximum[1]
                and
                minimum[2] <= b <= maximum[2]
            ):

                return True

            time.sleep(delay)
