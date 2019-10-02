import pygame
from game_manager import GameManager
from states import GameStateManager

gm = GameManager.instance()
gsm = GameStateManager()
display_size = (gm.WIDTH, gm.HEIGHT)

game_loop = True
game_speed = 25
p = pygame.init()
pygame.display.set_caption("Snake")
screen = pygame.display.set_mode(display_size)
clock = pygame.time.Clock()

while gm.game_loop:
    # for event in pygame.event.get():
    #     if event.type == pygame.QUIT:
    #         pygame.quit()
    screen.fill((0,0,0))
    gsm.event()
    gsm.update()
    gsm.render(screen)

    clock.tick(gm.game_speed)

    pygame.display.update()

pygame.quit()