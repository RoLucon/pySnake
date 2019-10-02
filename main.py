import pygame

display_size = (600, 400)

game_loop = True
game_speed = 25
p = pygame.init()
pygame.display.set_caption("Snake")
screen = pygame.display.set_mode(display_size)


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
    screen.fill((0,0,0))

    pygame.draw.rect(screen, (255,255,255),[50,50,50,50])


    pygame.display.update()

pygame.quit()