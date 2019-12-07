# coding=utf-8
import pygame as pg
import Background as bg

'''здесь костыль, потому что фона нет, константы убрать!'''
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

def event_processor(event):
    pass

class Game:
    """В этом классе вся оболочка игры"""
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
        

    def new_game(self):
        """Запуск игры"""
        
        self.start_func()
        
        running = True
        while running:
            # Держим цикл на правильной скорости
            self.clock.tick(self.FPS)
            # Ввод процесса (события)
            for event in pg.event.get():
                # check for closing window
                if event.type == pg.QUIT:
                    running = False
                event_processor(event)
            
            # Обновление
            
            self.body_func()
            
            # Рендеринг Background features
            self.rendr()
            # После отрисовки всего, переворачиваем экран
            pg.display.flip()
            self.time += 1

        pg.quit()
    
    
    @staticmethod
    def start_func():
        pass
    
    def change_start(self,func):
        self.start_func = func
    
    @staticmethod
    def body_func():
        pass
    
    def change_body(self,func):
        self.start_func = func
    
    def rendr(self):
        self.screen.fill(BLACK)


BoD = Game()

def f():
    print('***',end='')

BoD.change_start(f)

BoD.new_game()
