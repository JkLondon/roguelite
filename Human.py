import Mob as M
import Animation


class Human(M.Mob):
    def __init__(self, x, y, game):
        super().__init__(x, y, game)
        self.health = 10
    """
    Template for humanoid mobs
    """
    def sprite_update(self, time):
        if self.x_vel == 0:
            self.animation.change_sprite('stand', time)
        if self.x_vel > 0:
            self.animation.change_sprite('go_right', time)
        if self.x_vel < 0:
            self.animation.change_sprite('go_left', time)
