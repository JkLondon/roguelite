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

    def move_m(self):
        ph.move(self)
        pass

    def say_m(self):
        d.say(self, id)
        pass

    def destruction_m(self):
        ph.destruction(self)
        pass

    def attacking(self):
        pass

    def collision_m(self, obj):
        ph.collision(self, obj)
        pass
