import pygame
# from game_manager import GameManager


class GameStateManager:

    def __init__(self):
        self.currentState = 0
        self.states = [Menu()]

    def update(self):
        self.states[self.currentState].update()

    def render(self, screen):
        self.states[self.currentState].render(screen)

    def event(self):
        self.states[self.currentState].event()

    # def close_game(self):
    #     gm = GameManager.instance()
    #     gm.close_game()


class Menu:

    def __init__(self):
        self.name = "menu"

    def update(self):
        self.name = ""

    def render(self, screen):
        pygame.draw.rect(screen, (255,255,255), [40, 40, 10, 10])

    def event(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                print("sair")


# 
