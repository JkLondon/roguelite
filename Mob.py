import Background as Bg
import dialogs


class Mob:
    def __init__(self, x, y, game):
        self.size_y = 0
        self.size_x = 0
        self.health = 0
        self.armor = None
        self.animation = None
        self.x_pos = x
        self.y_pos = y
        self.x_vel = 0
        self.y_vel = 0
        '''bg const pack'''
        self.background = game.BackGr
        self.x = self.x_pos - self.size_x
        self.y = self.y_pos - self.size_y
        self.width = self.size_x * 2
        self.height = self.size_y * 2

    def say_m(self):
        dialogs.say(self, id)

    def collision(self, obj2):
        pass
    
    def sprite_update(self, time):
        pass

    def update(self):
        self.x_pos += self.x_vel
        if self.background.right_collision(self) or self.background.left_collision(self):
            self.x_pos -= self.x_vel
            if self.x_vel >= 0:
                for i in range(self.x_vel):
                    self.x_pos += 1
                    if self.background.right_collision(self):
                        self.x_pos -= 1
                        break
            else:
                for i in range(abs(self.x_vel)):
                    self.x_pos -= 1
                    if self.background.left_collision(self):
                        self.x_pos += 1
                        break
        self.y_pos += self.y_vel
        if self.background.up_collision(self) or self.background.down_collision(self):
            self.y_pos -= self.y_vel
            if self.y_vel >= 0:
                for i in range(self.y_vel):
                    self.y_pos += 1
                    if self.background.down_collision(self):
                        break
            else:
                for i in range(abs(self.y_vel)):
                    self.y_pos -= 1
                    if self.background.up_collision(self):
                        break
        self.y_pos += 1
        if not self.background.down_collision(self):
            self.y_vel += 1  # da eto g
        else:
            self.y_vel = 0
        self.y_pos -= 1

    def destruction(self):
        """Разрушение моба, сюда нужна будет анимация"""
        pass


if __name__ == '__main__':
    pass
else:
    print('Class Mob connected.')
