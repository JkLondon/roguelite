import Mob as M


class Creature(M.Mob):
    def set_mob(self):
        pass
    
    def sprite_update(self, time):
        self.animation.change_sprite('stand',time)
    
    def behavior(self, player):
        if player.x_pos < self.x_pos:
            self.x_vel = -2
        else:
            self.x_vel = 2
        if player.y_pos < self.y_pos:
            self.y_vel = -2
        else:
            self.y_vel = 2
        if abs(self.x_pos - player.x_pos) < self.size_x + player.size_x and \
                abs(self.y_pos - player.y_pos) < self.size_y + player.size_y:
            player.health -= 1
            self.x_vel = 0
            self.y_vel = 0