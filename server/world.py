import position
class World:
    def __init__(self):
        self.center = position((0, 0))
        self.height = 100
        self.width = 50
        self.robots = []
        self.obstacles = []