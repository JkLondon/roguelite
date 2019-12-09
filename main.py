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
        self.score = 0
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
        '''score shit'''
        self.score_table = None
        self.score_table_rect = None
        '''record shit'''
        self.record = 0
        self.record_table = self.font_renderer.render(str(self.record), True, WHITE)

    def new_game(self, record):
        """
        start new game
        """
        self.record = record
        running = True
        self.start_func()
        for sp in self.list_of_keys:
            self.all_sprites.add(self.dict_of_objects[sp])
        while running:
            self.clock.tick(self.FPS)
            for event in pg.event.get():
                # check for closing window
                self.event_processor(event, self.dict_of_objects['player'].mob)
            self.dict_of_objects['creature'].mob.behavior(self.dict_of_objects['player'].mob)
            self.dict_of_objects['player'].mob.lvl = self.score // 10 + 1
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
        if event.type == pg.QUIT:
            running = False
            exit()
        
        if not self.alive:
            if event.type == pg.KEYDOWN:
                self.clear_list()
                self.all_sprites = pg.sprite.Group()
                self.record = max(self.record, self.score)
                self.score = 0
                self.new_game(self.record)
        if not pg.key.get_pressed()[pg.K_s]:
            if player.state == 'bot':
                player.state = ''
                self.score += (self.time - player.bot_time) // self.FPS
                player.bot_time = -1
            if pg.key.get_pressed()[pg.K_a]:
                player.x_vel = -5
            elif pg.key.get_pressed()[pg.K_d]:
                player.x_vel = 5
            else:
                player.x_vel = 0
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_SPACE:
                    player.y_vel = -10
        else:
            player.state = 'bot'
            if player.bot_time == -1:
                self.time %= 100003
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
        self.hp_rect.left = 30

    def set_lose(self):
        """
        Func declared where lose table is
        """
        self.lose = self.font_renderer.render("Вы проиграли, для продолжения нажмите любую клавишу", True, WHITE)
        self.lose_rect = self.lose.get_rect()
        # left on screen
        self.lose_rect.center = self.screen_rect.center
        self.alive = False

    def set_score(self):
        """
        Func declared where score table is
        """
        self.score_table = self.font_renderer.render('Текущий счет: ' + str(self.score), True, RED)
        self.score_table_rect = self.score_table.get_rect()
        # left on screen
        self.score_table_rect.right = self.screen_rect.right

    def set_record(self):
        """
        Func declared where record table is
        """
        self.record_table = self.font_renderer.render('Рекорд: ' + str(self.record), True, RED)
        self.record_table_rect = self.record_table.get_rect()
        # left on screen
        self.record_table_rect.right = self.screen_rect.right

    def body_func(self):
        """
        Function which must be run in main cycle.
        """
        self.set_hp()
        if self.dict_of_objects['player'].mob.health <= 0:
            self.set_lose()
        self.set_score()
        self.set_record()

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
        self.screen.blit(self.score_table, (570, 10))
        self.screen.blit(self.record_table, (570, 60))
        self.all_sprites.draw(self.screen)


if __name__ == '__main__':
    BoD = Game()


    def f():
        test_mob = Pl.Player(400, 400, BoD.BackGr)
        test_mob.x_vel = 0
        test_mob_animation = A.Animation(test_mob, lib_sprites.TEST_MOB)
        BoD.add_obj(test_mob_animation, 'player')
        test_creature = C.Creature(600, 400, BoD.BackGr)
        test_creature.health = 1
        test_creature_animation = A.Animation(test_creature, lib_sprites.TEST_CREATURE)
        BoD.add_obj(test_creature_animation, 'creature')
        BoD.alive = True

    BoD.set_start(f)
    BoD.new_game(0)
