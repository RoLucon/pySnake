class GameManager:
    __instance = None

    @staticmethod
    def instance():
        if not GameManager.__instance:
            GameManager.__instance = GameManager()
        return GameManager.__instance

    def __init__(self):
        self.WIDTH = 600
        self.HEIGHT = 400
        self.TILE = 10
        self.game_loop = True
        self.game_speed = 15

    def close_game(self):
        self.game_loop = False

