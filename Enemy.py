import Human as H


class Enemy(H.Human):
    """
    Takes stand animation from Human. Have number_of_creatures par, and disappears
    when it becomes to zero
    """
    def __init__(self):
        self.type = None
        self.number_of_creatures = 5

    def noises(self):
        pass
