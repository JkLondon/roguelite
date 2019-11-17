import Mob as M
import animations as a


class Human(M.Mob):
    """
    Большинство параметров нагло тырит у моба, сам
    имеет пушку и уровень знаний (пока).
    Может ботать (анимация?)
    """
    def __init__(self):
        self.lvl_of_knowledge = 0
        self.weapon = None

    def bot_h(self):
        a.bot(self)
        pass

    def cast(self):
        a.cast(self, self.weapon)
        pass
