import Animation as am
import dialogs


class Mob:
    def __init__(self,x,y):
        self.size = None
        self.state = None
        self.health = None
        self.armor = None
        self.attack = None
        self.x_pos = x
        self.y_pos = y
        self.x_vel = 0
        self.y_vel = 0

    def say_m(self):
        dialogs.say(self, id)

    def collision(self, obj2):
        pass

    def move(self):
        """
        Abstract method. It will be define in class Human
        """
        pass

    def destruction(self):
        """Разрушение моба, сюда нужна будет анимация"""
        pass


if __name__ == '__main__':
    pass
else:
    print('Class Mob connected.')