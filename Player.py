import Human as H


class Player(H.Human):
    def __init__(self, x, y, background):
        super().__init__(x, y, background)
        self.lvl = 1
        self.weapon_type = None
        self.health = 20
        self.attacking = False
        self.bot_time = -1
        self.state = ''

    def attack(self, x):
        if self.x < x:
            pass

    def sprite_update(self, time):
        if self.state == 'bot':
            self.animation.change_sprite('bot', time)
        else:
            if self.x_vel == 0:
                self.animation.change_sprite('stand', time)
            if self.x_vel > 0:
                self.animation.change_sprite('go_right', time)
            if self.x_vel < 0:
                self.animation.change_sprite('go_left', time)

