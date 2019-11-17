import Mob as M


class Enemy(M.Mob):
    """
    Большинство параметров нагло тырит у моба, сам
    имеет тип (факер/семер), может издавать звуки
    """
    def __init__(self):
        self.type = None

    def noises(self):
        pass
