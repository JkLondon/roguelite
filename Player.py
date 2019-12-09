import Human as H


class Player(H.Human):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.lvl = 1
        self.weapon_type = None
        self.health = 20
        self.attacking = False

    def attack(self, x):
        if self.x < x:
            turn_right = None
