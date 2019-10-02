import random


class GameObject:

    def __init__(self, pos, size, color):
        self.x = pos[0]
        self.y = pos[1]
        self.width = size[0]
        self.heigth = size[1]
        self.color = color
        self.pivot = (self.x - self.width / 2, self.y - self.heigth / 2)

    def getpos(self):
        return (self.x, self.y)

    def setpos(self, value):
        self.x = value[0]
        self.y = value[1]

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        self.__x = value

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        self.__y = value


class Snake(GameObject):

    def __init__(self, pos, size, color):
        GameObject.__init__(self, pos, size, color)
        self.name = "corpo"
        self.velocity_x = 0
        self.velocity_y = 0

    def update(self):
        self.x += self.velocity_x
        self.y += self.velocity_y

    def collision(self, list):
        elements = len(list)
        for x in range(1, elements):
            if list[x].getpos() == self.getpos():
                return True
        return False


class Apple(GameObject):

    def __init__(self, pos, size, color):
        GameObject.__init__(self, pos, size, color)

    def eaten(self, list, width, heigt):
        for i in list:
            x = random.randint(self.width, (width / 10)) * 10
            y = random.randint(self.heigth, (heigt / 10)) * 10
            if(i != (x, y)):
                self.x = x
                self.y = y
                break
