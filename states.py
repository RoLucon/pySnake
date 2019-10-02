import pygame
from game_object import*
from game_manager import GameManager

WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)

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
        self.gm = GameManager().instance()
        self.box = False
        self.snake = Snake((50, 50), (10, 10), RED)

    def update(self):
        self.snake.update()

    def render(self, screen):
        pygame.draw.rect(screen, self.snake.color, [self.snake.pos_x, self.snake.pos_y, self.snake.width, self.snake.heigth])

    def event(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.gm.close_game()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    self.snake.velocity_y = -self.gm.TITLE
                    self.snake.velocity_x = -0
                elif event.key == pygame.K_RIGHT:
                    self.snake.velocity_x = self.gm.TITLE
                    self.snake.velocity_y = 0
                elif event.key == pygame.K_DOWN:
                    self.snake.velocity_y = self.gm.TITLE
                    self.snake.velocity_x = 0
                elif event.key == pygame.K_LEFT:
                    self.snake.velocity_x = -self.gm.TITLE
                    self.snake.velocity_y = 0
                if event.key == pygame.K_ESCAPE:
                    self.gm.close_game()


