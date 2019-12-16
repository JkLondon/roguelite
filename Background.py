import pygame

FPS = 60
W = 800  # ширина экрана
H = 600  # высота экрана
landscape1 = []

"""Эта штука должна быть в main, но пока пусть побудет тут"""
with open('landscape1.txt', 'r') as f:
    for i in f:
        L = i.split(' ')
        if '\n' in L:
            L.remove('\n')
        landscape1.append(list(map(int, L)))

GROUNDCOLOR_1 = (6, 131 + 5, 158 + 5)
GROUNDCOLOR_2 = (255, 255, 255)
DOORCOLOR = (200, 60, 30) 


class Ground():
    def __init__(self, array, screen):
        """
        self.array - двумерный список из нулей и единиц;
        точки с координатами (i*self.size, j*self.size) - левые верхние
        углы квадратов
        """
        self.array = array
        self.width = len(self.array[0])
        self.height = len(self.array)
        self.size = 20
        self.color = get_color(1)
        self.screen = screen

    def draw_ground(self):
        for i in range(self.height):
            for j in range(self.width):
                if self.array[i][j] == 1:
                    pygame.draw.rect(self.screen, self.color, (j * self.size, i * self.size,
                                                               self.size, self.size))

    def down_collision(self, other):
        x = other.x_pos - other.size_x
        y = other.y_pos - other.size_y
        if other.health == 20:
            pass
        b = False
        for i in range(x // self.size, (x + other.width) // self.size + 1):
            if self.array[(y + other.height) // self.size][i] == 1:
                b = True
        return b

    def up_collision(self, other):
        x = other.x_pos - other.size_x
        y = other.y_pos - other.size_y
        b = False
        for i in range(x // self.size, (x + other.width) // self.size):
            if self.array[y // self.size][i] == 1:
                b = True
        return b

    def left_collision(self, other):
        x = other.x_pos - other.size_x
        y = other.y_pos - other.size_y
        b = False
        for i in range(y // self.size, (y + other.height) // self.size):
            if self.array[i][x // self.size] == 1:
                b = True
        return b

    def right_collision(self, other):
        x = other.x_pos - other.size_x
        y = other.y_pos - other.size_y
        b = False
        for i in range(y // self.size, (y + other.height) // self.size):
            if self.array[i][(x + other.width) // self.size] == 1:
                b = True
        return b


class Door():
    def __init__(self, screen):
        self.rect = pygame.Rect(0, 0, 60, 100)
        self.color = DOORCOLOR
        self.screen = screen

    def draw_door(self):
        pygame.draw.rect(self.screen, self.color, self.rect)

    def entering(self, other):
        entering = False
        if (other.x_pos >= self.rect.left and other.x_pos <= self.rect.right and
            other.y_pos >= self.rect.top and other.y_pos <= self.rect.bottom):
            entering = True
        return(entering)



def get_color(index):
    if index == 1:
        return GROUNDCOLOR_1
    else:
        return GROUNDCOLOR_2


if __name__ == '__main__':
    pass
else:
    print('Class BackGround connected.')
