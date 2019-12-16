import pygame
from Mob import Mob
import Animation as A
import lib_sprites

class Bullet(Mob):
    def __init__(self, x, y, x_vel, y_vel, game):
        super().__init__(x, y, game)
        self.x_vel = x_vel
        self.y_vel = y_vel
        self.game = game
    
    def sprite_update(self, time):
        self.animation.change_sprite('stand', time)
    
    def update(self):
        if self.x_pos > - 100 and self.x_pos < self.game.WIDTH + 100:
            self.x_pos += self.x_vel
        if self.y_pos < self.game.HEIGHT + 100:
            self.y_pos += self.y_vel
            self.y_vel += 0.2
    
    
    
def cast_bullet(x_pos,y_pos,x_vel,y_vel,game):
    
    bullet = Bullet(x_pos, y_pos, x_vel, y_vel, game)
    bullet_animation = A.Animation(bullet, lib_sprites.BULLET)
    game.add_new_obj(bullet_animation, 'bul')

if __name__ == '__main__':
    import main
    import Player as Pl
    import NPC
    BoD = main.Game(True)
    
    def f():
        test_mob = Pl.Player(400, 400, BoD)
        test_mob.x_vel = 0
        test_mob_animation = A.Animation(test_mob, lib_sprites.TEST_MOB)
        BoD.add_obj(test_mob_animation, 'player')
        test_npc = NPC.NPC(700, 375, BoD)
        test_npc_animation = A.Animation(test_npc, lib_sprites.TEST_NPC)
        BoD.add_obj(test_npc_animation, 'npc')
        BoD.alive = True
    
    def f1():
        import Creature as C
        test_mob = Pl.Player(400, 400, BoD)
        test_mob.x_vel = 0
        test_mob_animation = A.Animation(test_mob, lib_sprites.TEST_MOB)
        BoD.add_obj(test_mob_animation, 'player')
        test_creature = C.Creature(600, 100, BoD)
        test_creature.health = 1
        test_creature_animation = A.Animation(test_creature, lib_sprites.TEST_CREATURE)
        BoD.add_obj(test_creature_animation, 'creature')
        BoD.all_sprites.add(BoD.dict_of_objects['creature'])
        BoD.alive = True

    BoD.set_start(f)
    BoD.set_other(f1)
    BoD.new_game(0)
else:
    print('Class Bullet connected.')