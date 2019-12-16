import Human as H


class NPC(H.Human):
    """
    Template for humanoid mobs
    """
    def sprite_update(self, time):
        self.animation.change_sprite('stand', time)

    def update(self):
        self.x_pos += self.x_vel