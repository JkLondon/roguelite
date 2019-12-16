import Human as H
import Bullet
import math

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

    def attack(self, event):
        velocity = 10
        X = event.pos[0] - self.x_pos
        Y = event.pos[1] - self.y_pos
        R = math.sqrt(X ** 2 + Y ** 2)
        Bullet.cast_bullet(self.x_pos, self.y_pos - 50, velocity * X // R, velocity * Y // R , self.game)
    
    def sprite_update(self, time):
        if self.state == 'bot':
            self.animation.change_sprite('bot', time)
        else:
            if self.x_vel == 0:
                if self.mana == 0:
                    self.animation.change_sprite('stand', time)
                else:
                    self.animation.change_sprite('stand_bot', time)
            if self.x_vel > 0:
                if self.mana == 0:
                    self.animation.change_sprite('go_right', time)
                else:
                    self.animation.change_sprite('go_right_bot', time)
            if self.x_vel < 0:
                if self.mana == 0:
                    self.animation.change_sprite('go_left', time)
                else:
                    self.animation.change_sprite('go_left_bot', time)

    

