# coding=utf-8
import pygame as pg
import Background as bg

'''здесь костыль, потому что фона нет, константы убрать!'''
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)


class Game:
    """В этом классе вся оболочка игры"""
    def __init__(self):
        self.WIDTH = 1000
        self.HEIGHT = 800
        self.FPS = 30
        pg.init()
        pg.mixer.init()
        self.screen = pg.display.set_mode((self.WIDTH, self.HEIGHT))
        pg.display.set_caption("RogueLite")
        self.clock = pg.time.Clock()

    def new_game(self):
        """Запуск игры"""
        running = True
        while running:
            # Держим цикл на правильной скорости
            self.clock.tick(self.FPS)
            # Ввод процесса (события)
            for event in pg.event.get():
                # check for closing window
                if event.type == pg.QUIT:
                    running = False

            # Обновление

            # Рендеринг Background features
            self.screen.fill(BLACK)
            # После отрисовки всего, переворачиваем экран
            pg.display.flip()

        pg.quit()


BoD = Game()
BoD.new_game()
