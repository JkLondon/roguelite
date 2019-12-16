import pygame
from Mob import Mob

class Bullet(Mob):
    def __init__(self, x, y, x_vel, y_vel, background):
        super().__init__(x, y, background)
        self.x_vel = x_vel
        self.y_vel = y_vel
    
    def sprite_update(self, time):
        self.animation.change_sprite('stand', time)
    
    def update(self):
        self.x_pos += self.x_vel
        self.y_pos += self.y_vel
        self.y_vel += 0.1
    
    
    
    
    

if __name__ == '__main__':
    import main
    import Player as Pl
    import Animation as A
    import lib_sprites
    import NPC
    BoD = main.Game(True)
    
    def f():
        bullet = Bullet(200, 200, 4, -2, BoD.BackGr)
        bullet_animation = A.Animation(bullet, lib_sprites.BULLET)
        BoD.add_obj(bullet_animation, 'bullet')
        
        test_mob = Pl.Player(400, 400, BoD.BackGr)
        test_mob.x_vel = 0
        test_mob_animation = A.Animation(test_mob, lib_sprites.TEST_MOB)
        BoD.add_obj(test_mob_animation, 'player')
        #test_npc = NPC.NPC(700, 375, BoD.BackGr)
        #test_npc_animation = A.Animation(test_npc, lib_sprites.TEST_NPC)
        #BoD.add_obj(test_npc_animation, 'npc')
        BoD.alive = True

    BoD.set_start(f)
    BoD.new_game(0)
else:
    print('Class Bullet connected.')