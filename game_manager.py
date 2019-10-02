class GameManager:
    __instance = None

    @staticmethod
    def instance():
        if not GameManager.__instance:
            GameManager.__instance = GameManager()
        return GameManager.__instance

    def __init__(self):
        self.WIDTH = 500
        self.HEIGHT = 400
        self.TILE = 10
        self.OFFSET_TOP = 50
        self.game_loop = True
        self.game_speed = 15
        self.font = ""

    def close_game(self):
        self.game_loop = False
