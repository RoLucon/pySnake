import random

class GameObject:

    def __init__(self, pos, size, color):
        self.pos_x = pos[0]
        self.pos_y = pos[1]
        self.width = size[0]
        self.heigth = size[1]
        self.color = color
        self.pivot = (self.pos_x - self.width / 2, self.pos_y - self.heigth / 2)


class Snake(GameObject):

    def __init__(self, pos, size, color):
        GameObject.__init__(self, pos, size, color)
        self.velocity_x = 0
        self.velocity_y = 0

    def update(self):
        self.pos_x += self.velocity_x
        self.pos_y += self.velocity_y


class Apple(GameObject):

    def __init__(self, pos, size, color):
        GameObject.__init__(self, pos, size, color)

    def tradeApple(self, width, heigt):
        self.pos_x = random.randint(self.width, (width / 10)) * 10
        self.pos_y = random.randint(self.heigth, (heigt / 10)) * 10
