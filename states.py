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
        self.snake = Snake((50, 50), (gm.TILE, gm.TILE), GREEN)
        self.apple = Apple((100, 100), (gm.TILE, gm.TILE), RED)

    def update(self):
        self.snake.update()
        if not self.box:
            if self.snake.pos_x > gm.WIDTH:
                self.snake.pos_x = 0
            elif self.snake.pos_x < 0:
                self.snake.pos_x = gm.WIDTH
            if self.snake.pos_y > gm.HEIGHT:
                self.snake.pos_y = 0
            elif self.snake.pos_y < 0:
                self.snake.pos_y = gm.HEIGHT
        else:
            if self.snake.pos_x > gm.WIDTH - gm.TILE:
                print("Morreu")
            elif self.snake.pos_x < gm.TILE:
                print("Morreu")
            if self.snake.pos_y > gm.HEIGHT:
                print("Morreu")
            elif self.snake.pos_y < 0:
                print("Morreu")

    def render(self, screen):
        pygame.draw.rect(screen, self.snake.color,
                         [self.snake.pos_x, self.snake.pos_y, self.snake.width, self.snake.heigth])
        pygame.draw.rect(screen, self.apple.color,
                         [self.apple.pos_x, self.apple.pos_y, self.apple.width, self.apple.heigth])

        if self.box:
            pygame.draw.rect(screen, WHITE, [0, 0, gm.WIDTH, gm.HEIGHT], gm.TILE)

    def event(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gm.close_game()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    self.snake.velocity_y = -gm.TILE
                    self.snake.velocity_x = -0
                elif event.key == pygame.K_RIGHT:
                    self.snake.velocity_x = gm.TILE
                    self.snake.velocity_y = 0
                elif event.key == pygame.K_DOWN:
                    self.snake.velocity_y = gm.TILE
                    self.snake.velocity_x = 0
                elif event.key == pygame.K_LEFT:
                    self.snake.velocity_x = -gm.TILE
                    self.snake.velocity_y = 0
                if event.key == pygame.K_ESCAPE:
                    gm.close_game()


