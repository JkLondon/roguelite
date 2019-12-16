import Human as H
import Bullet

class Player(H.Human):
    def __init__(self, x, y, game):
        super().__init__(x, y, game)
        self.lvl = 1
        self.weapon_type = None
        self.health = 20
        self.attacking = False
        self.bot_time = -1
        self.state = ''
        self.mana = 0
        self.game = game

    def attack(self):
        Bullet.cast_bullet(self.x_pos, self.y_pos, 0, -10, self.game)

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

