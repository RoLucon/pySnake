import random

class GameObject:

    def __init__(self, pos, size, color):
        # self.pos = pos
        self.x = pos[0]
        self.y = pos[1]
        self.width = size[0]
        self.heigth = size[1]
        self.color = color
        self.pivot = (self.x - self.width / 2, self.y - self.heigth / 2)

    def getPos(self):
        return (self.x, self.y)

    def setPos(self, value):
        self.x = value[0]
        self.y = value[1]
    # @property
    # def pos(self):
    #     return self.__pos
    #
    # @pos.setter
    # def pos(self, value):
    #     self.__pos = value
    #     self.x = value[0]
    #     self.y = value[1]

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        self.__x = value
        # self.pos = (self.x, self.pos[1])

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        self.__y = value
    # self.pos = (self.pos[0], self.y)


class Snake(GameObject):

    def __init__(self, pos, size, color):
        GameObject.__init__(self, pos, size, color)
        self.velocity_x = 0
        self.velocity_y = 0

    def update(self):
        self.x += self.velocity_x
        self.y += self.velocity_y
        # self.pos =(self.x, self.y)

    def collision(self, list):
        if any(bloco.pos == self.pos for bloco in list[:-1]):
            return True
        else:
            return False

class Apple(GameObject):

    def __init__(self, pos, size, color):
        GameObject.__init__(self, pos, size, color)

    def tradeApple(self, width, heigt):
        self.x = random.randint(self.width, (width / 10)) * 10
        self.y = random.randint(self.heigth, (heigt / 10)) * 10
        # self.pos = (self.x, self.y)
