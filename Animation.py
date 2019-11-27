import pygame

class Animation(pygame.sprite.Sprite):
    def __init__(self,mob,img):
        pygame.sprite.Sprite.__init__(self)
        self.image = img
        self.rect = self.image.get_rect()
        self.mob = mob
        self.rect.center = (self.mob.x_pos,self.mob.y_pos)
    
    def update(self)
        self.rect.x += self.mob.x_vel
        self.rect.y += self.mob.y_vel
    
    def move_right_animation(self):
        pass
    
    def move_left_animation(self):
        pass
    
    def stand_animation(self)
        pass
    
    def special_animation(self)
        pass

if __name__ == '__main__':
    pass


