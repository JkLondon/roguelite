import pygame

class Animation(pygame.sprite.Sprite):
    def __init__(self,mob,dict_of_sprites):
        pygame.sprite.Sprite.__init__(self)
        self.sprites = dict_of_sprites
        self.set_image('stand')
        self.mob = mob
        self.rect.center = (self.mob.x_pos,self.mob.y_pos)
    
    def set_image(self,image_name):
        self.image = pygame.image.load(self.sprites[image_name][0]).convert()
        self.image.set_colorkey((169,144,121))
        self.rect = self.image.get_rect()
    
    def change_sprite(self, name):
        pass
    
    def update(self, time):
        self.rect.x += self.mob.x_vel
        self.rect.y += self.mob.y_vel

if __name__ == '__main__':
    import Mob as mb
    import lib_sprites
    
    import main
    
    
    BoD = main.Game()

    def f():
        test_mob = mb.Mob(100,100)
        test_mob_animation = Animation(test_mob,lib_sprites.TEST_MOB)

    BoD.change_start(f)

    BoD.new_game()
    
    
else:
    print('Class Animation connected.')