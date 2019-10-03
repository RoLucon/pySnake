import pygame
from game_object import*
from game_manager import GameManager

WHITE = (255, 255, 255)
RED = (255, 128, 0)
GREEN = (128, 255, 0)
BLUE = (0, 128, 255)
BLACK = (0, 0, 0)
PURPLE = (128, 0, 255)
gm = GameManager.instance()


class GameStateManager:
    __instance = None

    def __init__(self):
        self.currentState = 0
        self.states = []
        self.states = [Menu()]

    @staticmethod
    def instance():
        if not GameStateManager.__instance:
            GameStateManager.__instance = GameStateManager()
        return GameStateManager.__instance

    def update(self):
        self.states[self.currentState].update()

    def render(self, screen, font):
        pygame.draw.rect(screen, PURPLE, [0, 0, gm.WIDTH, gm.OFFSET_TOP])
        self.states[self.currentState].render(screen, font)

    def event(self):
        self.states[self.currentState].event()

    def change_state(self, name):
        if name == "Menu":
            self.states.append(Menu())
            self.states.remove(self.states[self.currentState])
        if name == "LevelOne":
            self.states.append(LevelOne())
            self.states.remove(self.states[self.currentState])
        if name == "GameOver":
            self.states.append(GameOver())
            self.states.remove(self.states[self.currentState])

    def pause(self, current_state):
        self.states.append(Pause(current_state))
        self.currentState = 1

    def unpause(self):
        self.currentState = 0
        self.states.pop(1)

class Menu:

    def __init__(self):
        pass

    def update(self):
        pass

    def render(self, screen, font):
        flag = False
        for x in range(gm.OFFSET_TOP, gm.HEIGHT, gm.OFFSET_TOP):
            if flag:
                pygame.draw.rect(screen, PURPLE, [0, x, gm.WIDTH, gm.OFFSET_TOP])
                flag = False
            else:
                flag = True
        pause = font.render("pySnake", True, WHITE)
        sair = font.render("Enter para jogar", True, WHITE)
        screen.blit(pause, [gm.WIDTH / 2 - 35, gm.HEIGHT / 3 + 25])
        screen.blit(sair, [gm.WIDTH / 8 * 3, gm.HEIGHT / 3 * 2 - 10])

    def event(self):
        gsm = GameStateManager.instance()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                if event.key == pygame.K_RETURN:
                    gsm.change_state("LevelOne")


class LevelOne:

    def __init__(self):
        self.init_time = pygame.time.get_ticks() / 1000
        self.current_time = self.init_time
        self.box = False
        self.head = Snake((400, 300), (gm.TILE, gm.TILE), GREEN)
        self.head.velocity_x = 10
        self.list_snake = []
        self.list_snake.append(self.head)
        self.apple = Apple((100, 100), (gm.TILE, gm.TILE), RED)
        self.snake_len = 1

    def update(self):
        gsm = GameStateManager.instance()
        self.current_time = round(pygame.time.get_ticks() /1000 - self.init_time)
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
                self.head.y = 0 + gm.OFFSET_TOP
            elif self.head.y < 0 + gm.OFFSET_TOP:
                self.head.y = gm.HEIGHT
        else:
            if self.head.x > gm.WIDTH - gm.TILE:
                gsm.change_state("GameOver")
            elif self.head.x < gm.TILE:
                gsm.change_state("GameOver")
            if self.head.y > gm.HEIGHT:
                gsm.change_state("GameOver")
            elif self.head.y < 0 + gm.OFFSET_TOP:
                gsm.change_state("GameOver")
        if self.apple.x == self.list_snake[-1].x and self.apple.y == self.list_snake[-1].y:
            self.list_snake.append(Snake(self.apple.getpos(), (gm.TILE, gm.TILE), GREEN))
            self.apple.eaten(self.list_snake, gm.WIDTH, gm.HEIGHT)
            self.snake_len += 1
        # if len(self.list_snake) > self.snake_len:
        #     del self.list_snake[0]
        if self.head.collision(self.list_snake):
            gsm.change_state("GameOver")

    def render(self, screen, font):
        for snake in self.list_snake:
            pygame.draw.rect(screen, snake.color, [snake.x, snake.y, snake.width, snake.heigth])
        pygame.draw.rect(screen, self.apple.color,
                         [self.apple.x, self.apple.y, self.apple.width, self.apple.heigth])

        if self.box:
            pygame.draw.rect(screen, WHITE, [0, + gm.OFFSET_TOP, gm.WIDTH, gm.HEIGHT - + gm.OFFSET_TOP], gm.TILE)
        score = font.render("SCORE: " + str(self.snake_len), True, WHITE)
        time = font.render("TIME: " + str(self.current_time), True, WHITE)
        screen.blit(score, [gm.WIDTH / 6, (gm.OFFSET_TOP/2 - 25/2)])
        screen.blit(time, [(gm.WIDTH / 6) * 4, (gm.OFFSET_TOP/2 - 25/2)])

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
                    gsm = GameStateManager.instance()
                    gsm.pause(self)


class GameOver:

    def __init__(self):
        pass

    def update(self):
        pass

    def render(self, screen, font):
        screen.fill(RED)
        gameover = font.render("GAME OVER", True, WHITE)
        screen.blit(gameover, [gm.WIDTH / 6, (gm.OFFSET_TOP / 2 - 25 / 2)])

    def event(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                print("sair")


class Pause:

    def __init__(self, current_state):
        self.current_state = current_state
        pass

    def update(self):
        pass

    # Ajustar posicionamentos com referencias da tela
    def render(self, screen, font):
        self.current_state.render(screen, font)
        pygame.draw.rect(screen, BLUE, [gm.WIDTH / 4, gm.HEIGHT / 4, gm.WIDTH / 2, gm.HEIGHT / 2])
        pause = font.render("Pausado", True, WHITE)
        sair = font.render("Sair    Continuar", True, WHITE)
        screen.blit(pause, [gm.WIDTH / 2 - 35, gm.HEIGHT / 3])
        screen.blit(sair, [gm.WIDTH / 8 * 3, gm.HEIGHT / 3 * 2])

    def event(self):
        gsm = GameStateManager.instance()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE or event.key == pygame.K_c:
                    gsm.unpause()
                if event.key == pygame.K_s:
                    gsm.change_state("Menu")