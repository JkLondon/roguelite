import Mob as M


class Player(M.Mob):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.lvl = 1
        self.weapon_type = None
        self.health = 20
