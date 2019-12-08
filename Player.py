import Mob as M


class Player(M.Mob):
    def __init__(self):
        super().__init__(self)
        self.lvl = 1
        self.weapon_type = None

    def