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
        self.TITLE = 10
        self.game_loop = True
        self.game_speed = 20

    def close_game(self):
        self.game_loop = False

