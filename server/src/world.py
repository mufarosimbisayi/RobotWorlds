from server.src.position import Position
import random


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
        self._maximum_robots = 10
        self._visibility = 5
        self._reload = 2
        self._repair = 2
        self._shields = 3

    def launch_robot(self, robot):
        """launched a robot onto the world"""

        robot.set_initial_position(self.get_random_position())
        self._robots.append(robot)

    def get_random_position(self):
        """Gets a random position that is currently unoccupied"""

        while True:
            x = random.randint(-int(self._width / 2), int(self._width / 2))
            y = random.randint(-int(self._height / 2), int(self._height / 2))
            position = Position((x, y))
            position_status = self.check_position(position)
            if position_status == "nothing":
                return position

    def check_position(self, position):
        """Checks that the position is not occupied"""

        if position.x_coordinate >= int(self._width / 2) or \
                position.x_coordinate <= -int(self._width / 2):
            return "edge"
        if position.y_coordinate >= int(self._height / 2) or \
                position.y_coordinate <= -int(self._height / 2):
            return "edge"
        for robot in self._robots:
            if position == robot.get_position():
                return "robot"
        for obstacle in self._obstacles:
            if obstacle == position:
                return "obstacle"
        return "nothing"

    def has_space(self):
        return len(self._robots) < self._maximum_robots

    def get_shields_value(self):
        return self._shields

    def get_visibility_value(self):
        return self._visibility

    def get_reload_value(self):
        return self._reload

    def get_repair_value(self):
        return self._repair

    def unique_robot(self, new_robot):
        """Checks if the world has enough space for another robot"""

        for robot in self._robots:
            if new_robot.name == robot.name:
                return False
        return True

    def get_robot(self, robot_name):
        """Finds and returns a robot by name"""

        for robot in self._robots:
            if robot_name == robot.name:
                return robot
        return None

    def add_obstacles(self, position):
        """Adds an obstacle to the worlds obstacles list"""

        self._obstacles.append(position)
