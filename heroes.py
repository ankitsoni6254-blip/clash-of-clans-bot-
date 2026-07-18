from adb_utils import ADB


class Heroes:

    def __init__(self, adb: ADB):
        self.adb = adb

    def deploy(self, button, drop):

        self.adb.tap(*button)
        self.adb.tap(*button)

        self.adb.tap(*drop)
        self.adb.tap(*drop)

    def activate(self, button):

        self.adb.tap(*button)
        self.adb.tap(*button)
