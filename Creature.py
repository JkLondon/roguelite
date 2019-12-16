import Mob as M


class Creature(M.Mob):
    def __init__(self, x, y, game):
        super().__init__(x, y, game)
        self.base_vel = 1
        self.health = 1

    def set_mob(self):
        pass
    
    def sprite_update(self, time):
        self.animation.change_sprite('stand', time)
    
    def behavior(self, player):
        if player.x_pos < self.x_pos:
            self.x_vel = -1 * self.base_vel * player.lvl
        elif player.x_pos == self.x_pos:
            self.x_vel = 0
        else:
            self.x_vel = self.base_vel * player.lvl
        if player.y_pos < self.y_pos:
            self.y_vel = -1 * self.base_vel * player.lvl
        elif player.y_pos == self.y_pos:
            self.y_vel = 0
        else:
            self.y_vel = self.base_vel * player.lvl
        if abs(self.x_pos - player.x_pos) < self.size_x + player.size_x and \
                abs(self.y_pos - player.y_pos) < self.size_y + player.size_y:
            player.health -= 1
            self.x_vel = 0
            self.y_vel = 0
