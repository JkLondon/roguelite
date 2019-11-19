import animations as a
import physics as ph
import dialogs as d


class Mob:
    def __init__(self):
        self.size = None
        self.spite = None
        self.health = None
        self.armor = None
        self.attack = None

    def say_m(self):
        d.say(self, id)
        pass

    def collision(self, obj2):
        """
        Изначально планирую интерпретировать мобов как
        прямоугольники, пока прогай от этого
        """
        pass

    def move(self):
        """Движение моба, 2 спрайта на движение будет"""
        pass

    def destruction(self):
        """Разрушение моба, сюда нужна будет анимация"""
        pass

    def targeting(self):
        """Наведение пушек, мечей как в той игре)"""
        pass
