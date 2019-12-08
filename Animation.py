import pygame


class Animation(pygame.sprite.Sprite):
    def __init__(self, mob, dict_of_sprites):
        self.rect = None
        self.image = None
        pygame.sprite.Sprite.__init__(self)
        self.sprites = dict_of_sprites
        self.set_image('stand')
        self.mob = mob
        self.rect.center = (self.mob.x_pos, self.mob.y_pos)
        self.mob.size = abs(self.rect.bottom - self.rect.center[1])

    def set_image(self, image_name):
        """
        Set image of sprite.
        """
        self.image = pygame.image.load(self.sprites[image_name][0]).convert()
        self.image.set_colorkey((169, 144, 121))
        self.rect = self.image.get_rect()

    def change_sprite(self, name):
        pass


    def update(self, time):
        """
        Update position of picture on display.
        """
        self.mob.update()
        self.rect.center = (self.mob.x_pos, self.mob.y_pos)


if __name__ == '__main__':
    pass
else:
    print('Class Animation connected.')