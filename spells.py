from adb_utils import ADB


class Spells:

    def __init__(self, adb: ADB):
        self.adb = adb

    def drop(self, spell_button, locations):

        self.adb.tap(*spell_button)
        self.adb.tap(*spell_button)

        for pos in locations:
            self.adb.tap(*pos)
