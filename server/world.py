from position import Position


class World:
    _instance = None

    @staticmethod
    def get_instance():
        if World._instance is None:
            World._instance = World()
        return World._instance

    def __init__(self):
        self._center = Position((0, 0))
        self._height = 100
        self._width = 50
        self._robots = []
        self._obstacles = []

    def launch_robot(self, robot):
        self._robots.append(robot)