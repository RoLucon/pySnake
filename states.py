import pygame
from game_object import*
from game_manager import GameManager

WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)
gm = GameManager.instance()

class GameStateManager:

    def __init__(self):
        self.currentState = 0
        self.states = [LevelOne()]

    def update(self):
        self.states[self.currentState].update()

    def render(self, screen):
        self.states[self.currentState].render(screen)

    def event(self):
        self.states[self.currentState].event()


class Menu:

    def __init__(self):
        self.name = "menu"

    def update(self):
        self.name = ""

    def render(self, screen):
        pygame.draw.rect(screen, (WHITE), [40, 40, 10, 10])

    def event(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                print("sair")


class LevelOne:

    def __init__(self):
        self.box = False
        self.list_snake = []
        self.head = Snake((400, 300), (gm.TILE, gm.TILE), GREEN)
        self.head.velocity_x = 10
        self.head.name = "Cabeca"
        self.list_snake.append(self.head)
        for x in range(10):
            self.list_snake.append(Snake((400, 300 + 10 * x), (gm.TILE, gm.TILE), GREEN))
        self.apple = Apple((100, 100), (gm.TILE, gm.TILE), RED)
        self.snake_len = 1

    def update(self):
        elements = len(self.list_snake)
        if elements > 1:
            for i in range(elements, 1, -1):
                self.list_snake[i-1].setpos(self.list_snake[i - 2].getpos())

        self.head.update()
        if not self.box:
            if self.head.x > gm.WIDTH - gm.TILE:
                self.head.x = 0
            elif self.head.x < 0:
                self.head.x = gm.WIDTH
            if self.head.y > gm.HEIGHT - gm.TILE:
                self.head.y = 0
            elif self.head.y < 0:
                self.head.y = gm.HEIGHT
        else:
            if self.head.x > gm.WIDTH - gm.TILE:
                print("Batendo na parede")
            elif self.head.x < gm.TILE:
                print("Batendo na parede")
            if self.head.y > gm.HEIGHT:
                print("Batendo na parede")
            elif self.head.y < 0:
                print("Batendo na parede")
        if self.apple.x == self.list_snake[-1].x and self.apple.y == self.list_snake[-1].y:
            self.list_snake.append(Snake(self.apple.getpos(), (gm.TILE, gm.TILE), GREEN))
            self.apple.eaten(self.list_snake, gm.WIDTH, gm.HEIGHT)

        # if len(self.list_snake) > self.snake_len:
        #     del self.list_snake[0]
        if self.head.collision(self.list_snake):
            print("Colidindo com corpo")

    def render(self, screen):
        for snake in self.list_snake:
            pygame.draw.rect(screen, snake.color, [snake.x, snake.y, snake.width, snake.heigth])
        pygame.draw.rect(screen, self.apple.color,
                         [self.apple.x, self.apple.y, self.apple.width, self.apple.heigth])

        if self.box:
            pygame.draw.rect(screen, WHITE, [0, 0, gm.WIDTH, gm.HEIGHT], gm.TILE)

    def event(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gm.close_game()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP and self.head.velocity_y != gm.TILE:
                    self.head.velocity_y = -gm.TILE
                    self.head.velocity_x = -0
                elif event.key == pygame.K_RIGHT and self.head.velocity_x != -gm.TILE:
                    self.head.velocity_x = gm.TILE
                    self.head.velocity_y = 0
                elif event.key == pygame.K_DOWN and self.head.velocity_y != -gm.TILE:
                    self.head.velocity_y = gm.TILE
                    self.head.velocity_x = 0
                elif event.key == pygame.K_LEFT and self.head.velocity_x != gm.TILE:
                    self.head.velocity_x = -gm.TILE
                    self.head.velocity_y = 0
                if event.key == pygame.K_ESCAPE:
                    gm.close_game()
