import Human as H


class Player(H.Human):
    def __init__(self, x, y, background):
        super().__init__(x, y, background)
        self.lvl = 1
        self.weapon_type = None
        self.health = 20
        self.attacking = False

    def attack(self, x):
        if self.x < x:
            pass

