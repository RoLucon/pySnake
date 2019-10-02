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
font = pygame.font.SysFont('arial', 25)


while gm.game_loop:
    screen.fill((0, 0, 0))
    gsm.event()
    gsm.update()
    gsm.render(screen, font)

    clock.tick(gm.game_speed)

    pygame.display.update()

pygame.quit()