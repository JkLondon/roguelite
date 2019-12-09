# coding=utf-8
import pygame as pg
import Background as Bg
import lib_sprites
import Player as Pl
import Animation as A
import Creature as C

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
landscape1 = []

"""Эта штука должна быть в main, но пока пусть побудет тут"""
with open('landscape1.txt', 'r') as f:
    for i in f:
        L = i.split(' ')
        if '\n' in L:
            L.remove('\n')
        landscape1.append(list(map(int, L)))


class Game:
    """Shell of game"""
    def __init__(self):
        self.WIDTH = 800
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
        '''label shit'''
        self.screen_rect = self.screen.get_rect()
        self.default_font = pg.font.get_default_font()
        self.font_renderer = pg.font.Font(self.default_font, 24)
        '''hp shit'''
        self.hp = None
        self.hp_rect = None
        '''u_lose shit'''
        self.alive = True
        self.lose = None
        self.lose_rect = None
        '''BackGrAdd'''
        self.BackGr = Bg.Ground(landscape1, self.screen)
        self.BGImage = pg.image.load('background_1.jpg').convert()
        print(self.BackGr.array)

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
            self.dict_of_objects['creature'].mob.behavior(self.dict_of_objects['player'].mob)
            self.body_func()

            self.render()
            
            pg.display.flip()
            self.time += 1

        pg.quit()

    def event_processor(self, event, player):
        """
        event_processor
        don't react on any keys when bot.
        """
        if not self.alive:
            if event.type == pg.KEYDOWN:
                self.clear_list()
                self.all_sprites = pg.sprite.Group()
                self.new_game()
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

    def set_hp(self):
        """
        Function will show your current hp
        """
        self.hp = self.font_renderer.render(str(max(0, self.dict_of_objects[
                                                    'player'].mob.health)) + ' HP', True, WHITE)
        self.hp_rect = self.hp.get_rect()
        # left on screen
        self.hp_rect.left = self.screen_rect.left

    def set_lose(self):
        self.lose = self.font_renderer.render("Вы проиграли, для продолжения нажмите любую клавишу", True, WHITE)
        self.lose_rect = self.lose.get_rect()
        # left on screen
        self.lose_rect.center = self.screen_rect.center
        self.alive = False

    def body_func(self):
        """
        Function which must be run in main cycle.
        """
        if self.time - self.dict_of_objects['player'].mob.bot_time >= 90 and \
                self.dict_of_objects['player'].mob.state == 'bot':
            self.dict_of_objects['player'].mob.state = None
        self.set_hp()
        if self.dict_of_objects['player'].mob.health <= 0:
            self.set_lose()

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
    
    def render(self):
        """
        Update sprites under display.
        """
        if self.alive:
            self.all_sprites.update(self.time)
        self.screen.blit(self.BGImage, (0, 0))
        self.BackGr.draw_ground()
        if not self.alive:
            self.screen.blit(self.lose, self.lose_rect)
        self.screen.blit(self.hp, self.hp_rect)
        self.all_sprites.draw(self.screen)


if __name__ == '__main__':
    BoD = Game()


    def f():
        test_mob = Pl.Player(400, 400, BoD.BackGr)
        test_mob.x_vel = 0
        test_mob_animation = A.Animation(test_mob, lib_sprites.TEST_MOB)
        BoD.add_obj(test_mob_animation, 'player')
        test_creature = C.Creature(600, 400, BoD.BackGr)
        test_creature_animation = A.Animation(test_creature, lib_sprites.TEST_CREATURE)
        BoD.add_obj(test_creature_animation, 'creature')
        BoD.alive = True

    BoD.set_start(f)
    BoD.new_game()
