import pygame


class Animation(pygame.sprite.Sprite):
    def __init__(self, mob, dict_of_sprites):
        self.rect = None
        self.image = None
        pygame.sprite.Sprite.__init__(self)
        self.dict_of_sprites = dict_of_sprites
        self.sprite = self.dict_of_sprites['stand']
        self.set_image(0)
        self.mob = mob
        self.rect.center = (self.mob.x_pos, self.mob.y_pos)
        self.mob.size_x = abs(self.rect.left - self.rect.center[0])
        self.mob.size_y = abs(self.rect.bottom - self.rect.center[1])

    def change_sprite(self, sprite_name, time):
        self.sprite = self.dict_of_sprites[sprite_name]
        self.set_image(time)

    def set_image(self, time):
        """
        Set image of sprite.
        """
        num = (time // self.sprite['timer']) % self.sprite['num']
        print(num)
        self.image = pygame.image.load(self.sprite['sprite'][num]).convert()
        self.image.set_colorkey((169, 144, 121))
        self.rect = self.image.get_rect()

    def update(self, time):
        """
        Update position of picture on display.
        """
        self.mob.update()
        self.set_image(time)
        self.rect.center = (self.mob.x_pos, self.mob.y_pos)


if __name__ == '__main__':
    pass
else:
    print('Class Animation connected.')