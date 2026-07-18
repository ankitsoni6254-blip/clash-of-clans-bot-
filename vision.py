from adb_utils import ADB


class Vision:

    def __init__(self, adb: ADB):
        self.adb = adb
        self.image = None

    def refresh(self):
        self.image = self.adb.screenshot()

    def pixel(self, x, y):

        b, g, r = self.image[y, x]

        return int(r), int(g), int(b)

    def in_range(self, x, y, minimum, maximum):

        r, g, b = self.pixel(x, y)

        return (
            minimum[0] <= r <= maximum[0]
            and minimum[1] <= g <= maximum[1]
            and minimum[2] <= b <= maximum[2]
        )
