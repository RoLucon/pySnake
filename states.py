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
        self.snake = []
        self.snake.append(Snake((50, 50), (gm.TILE, gm.TILE), GREEN))
        self.apple = Apple((100, 100), (gm.TILE, gm.TILE), RED)


    def update(self):
        for snake in self.snake:
            snake.update()
        if not self.box:
            if self.snake[0].pos_x > gm.WIDTH:
                self.snake[0].pos_x = 0
            elif self.snake[0].pos_x < 0:
                self.snake[0].pos_x = gm.WIDTH
            if self.snake[0].pos_y > gm.HEIGHT:
                self.snake[0].pos_y = 0
            elif self.snake[0].pos_y < 0:
                self.snake[0].pos_y = gm.HEIGHT
        else:
            if self.snake[0].pos_x > gm.WIDTH - gm.TILE:
                print("Morreu")
            elif self.snake[0].pos_x < gm.TILE:
                print("Morreu")
            if self.snake[0].pos_y > gm.HEIGHT:
                print("Morreu")
            elif self.snake[0].pos_y < 0:
                print("Morreu")
        if self.apple.pos_x == self.snake[0].pos_x and self.apple.pos_y == self.snake[0].pos_y:
            self.apple.tradeApple(gm.WIDTH, gm.HEIGHT)

    def render(self, screen):

        for snake in self.snake:
            pygame.draw.rect(screen, snake.color, [snake.pos_x, snake.pos_y, snake.width, snake.heigth])
        pygame.draw.rect(screen, self.apple.color,
                         [self.apple.pos_x, self.apple.pos_y, self.apple.width, self.apple.heigth])

        if self.box:
            pygame.draw.rect(screen, WHITE, [0, 0, gm.WIDTH, gm.HEIGHT], gm.TILE)

    def event(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gm.close_game()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP and self.snake[0].velocity_y != gm.TILE:
                    self.snake[0].velocity_y = -gm.TILE
                    self.snake[0].velocity_x = -0
                elif event.key == pygame.K_RIGHT and self.snake[0].velocity_x != -gm.TILE:
                    self.snake[0].velocity_x = gm.TILE
                    self.snake[0].velocity_y = 0
                elif event.key == pygame.K_DOWN and self.snake[0].velocity_y != -gm.TILE:
                    self.snake[0].velocity_y = gm.TILE
                    self.snake[0].velocity_x = 0
                elif event.key == pygame.K_LEFT and self.snake[0].velocity_x != gm.TILE:
                    self.snake[0].velocity_x = -gm.TILE
                    self.snake[0].velocity_y = 0
                if event.key == pygame.K_ESCAPE:
                    gm.close_game()
