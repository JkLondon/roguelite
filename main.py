# coding=utf-8
import pygame as pg
import Background as bg
import lib_sprites
import Mob as Mb
import Animation as A

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)


class Game:
    """Shell of game"""
    def __init__(self):
        self.WIDTH = 1200
        self.HEIGHT = 600
        self.FPS = 30
        pg.init()
        pg.mixer.init()
        self.screen = pg.display.set_mode((self.WIDTH, self.HEIGHT))
        pg.display.set_caption("RogueLite")
        self.clock = pg.time.Clock()
        self.time = 0
        self.dict_of_objects = dict()
        self.list_of_keys = []
        self.all_sprites = pg.sprite.Group()

    def new_game(self):
        """start new game"""
        running = True
        self.start_func()
        for sp in self.list_of_keys:
            self.all_sprites.add(self.dict_of_objects[sp])
        while running:
            self.clock.tick(self.FPS)
            
            for event in pg.event.get():
                # check for closing window
                if event.type == pg.QUIT:
                    running = False
                self.event_processor(event, self.dict_of_objects['player'].mob)
                print(self.time, self.dict_of_objects['player'].mob.bot_time)
                if self.time - self.dict_of_objects['player'].mob.bot_time >= 90 and \
                        self.dict_of_objects['player'].mob.state == 'bot':
                    self.dict_of_objects['player'].mob.state = None

            self.body_func()

            self.rendr()
            
            pg.display.flip()
            self.time += 1

        pg.quit()

    def event_processor(self, event, player):
        """
        event_processor
        don't react on any keys when bot.
        """
        if player.state == 'bot':
            return
        if pg.key.get_pressed()[pg.K_a]:
            player.x_vel = -5
        elif pg.key.get_pressed()[pg.K_d]:
            player.x_vel = 5
        else:
            player.x_vel = 0
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_SPACE:
                player.y_vel = -10
            if event.key == pg.K_s:
                player.state = 'bot'
                player.bot_time = self.time
    @staticmethod
    def start_func():
        """
        Function which must be run before main cycle starts.
        """
        pass
    
    def set_start(self, func):
        """
        Set start function
        """
        self.start_func = func
    
    @staticmethod
    def body_func():
        """
        Function which must be run in main cycle.
        """
        pass
    
    def set_body(self, func):
        """
        Set body function.
        """
        self.start_func = func
    
    def add_obj(self, obj, name):
        """
        Add new object in list of active objects.
        """
        self.dict_of_objects[name] = obj
        self.list_of_keys.append(name)
    
    def clear_list(self):
        """
        Clear list of active objects.
        """
        self.dict_of_objects = dict()
        self.list_of_keys = []
    
    def rendr(self):
        """
        Update sprites under display.
        """
        self.all_sprites.update(self.time)
        self.screen.fill(BLACK)
        self.all_sprites.draw(self.screen)
        

if __name__ == '__main__':
    BoD = Game()


    def f():
        test_mob = Mb.Mob(400, 400)
        test_mob.x_vel = 0
        test_mob_animation = A.Animation(test_mob, lib_sprites.TEST_MOB)
        BoD.add_obj(test_mob_animation, 'player')


    BoD.set_start(f)
    BoD.new_game()
