import physics as ph


class BackGround:
    def __init__(self):
        """
        Размер - что-то эфемерное, не решил еще где его оставить:
        либо здесь, либо в main.py.
        Массив borders - набор отрезков, который будет регламентировать
        границы, за которые игрок не сможет заходить.
        """
        self.SIZE = None
        self.borders = []

    def cross_the_border(self, obj):
        """Проверка, вышел ли игрок за границу, не разрешать ему это проворачивать"""
        ph.collision(obj, self.borders[0])
        pass
