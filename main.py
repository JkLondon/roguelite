# coding=utf-8
import pygame as pg
import Background as bg


WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

def event_processor(event):
    pass

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
        
        self.list_of_objects = []
        

    def new_game(self):
        """start new game"""
        running = True
        
        self.all_sprites = pg.sprite.Group()
        
        self.start_func()
        for sp in self.list_of_objects:
            self.all_sprites.add(sp)
        while running:
            self.clock.tick(self.FPS)
            
            for event in pg.event.get():
                # check for closing window
                if event.type == pg.QUIT:
                    running = False
                event_processor(event)
            
            self.body_func()
            
            self.rendr()
            
            pg.display.flip()
            self.time += 1

        pg.quit()
    
    
    @staticmethod
    def start_func():
        """
        Function which must be run before main cycle starts.
        """
        pass
    
    def set_start(self,func):
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
    
    def set_body(self,func):
        """
        Set body function.
        """
        self.start_func = func
    
    def add_obj(self,obj):
        """
        Add new object in list of active objects.
        """
        self.list_of_objects.append(obj)
    
    def clear_list(self):
        """
        Clear list of active objects.
        """
        self.list_of_objects = []
    
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
        print('***',end='')

    BoD.set_start(f)

    BoD.new_game()
