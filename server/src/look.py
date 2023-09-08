from server.src.command import Command
from server.src.world import World
from server.src.position import Position


class Look(Command):

    def __init__(self):
        super().__init__('look')
        self._objects = []

    def execute(self, request):
        if self.valid_request(request):
            world = World.get_instance()
            visibility = world.get_visibility_value()
            robot = world.get_robot(request["robot"])
            if robot is not None:
                self.look_north(visibility, robot.get_position(), world)
                self.look_south(visibility, robot.get_position(), world)
                self.look_west(visibility, robot.get_position(), world)
                self.look_east(visibility, robot.get_position(), world)
                return self.look_status_object(robot)
        else:
            return self.invalid_request_error()

    def look_north(self, visibility, robot_position, world):
        """Checks for obstacles in the north line of site"""

        y = robot_position.y_coordinate
        x = robot_position.x_coordinate
        for step in range(1, visibility + 1):
            look_result = world.check_position(Position((x, y + step)))
            if look_result != "nothing":
                self._objects.append(
                    {
                        "direction": "North",
                        "type": look_result,
                        "distance": step
                    }
                )
            if look_result == "edge":
                break

    def look_south(self, visibility, robot_position, world):
        """Checks for obstacles in the south line of site"""

        y = robot_position.y_coordinate
        x = robot_position.x_coordinate
        for step in range(1, visibility + 1):
            look_result = world.check_position(Position((x, y - step)))
            if look_result != "nothing":
                self._objects.append(
                    {
                        "direction": "South",
                        "type": look_result,
                        "distance": step
                    }
                )
            if look_result == "edge":
                break

    def look_west(self, visibility, robot_position, world):
        """Checks for obstacles in the south line of site"""

        y = robot_position.y_coordinate
        x = robot_position.x_coordinate
        for step in range(1, visibility + 1):
            look_result = world.check_position(Position((x + step, y)))
            if look_result != "nothing":
                self._objects.append(
                    {
                        "direction": "West",
                        "type": look_result,
                        "distance": step
                    }
                )
            if look_result == "edge":
                break

    def look_east(self, visibility, robot_position, world):
        """Checks for obstacles in the south line of site"""

        y = robot_position.y_coordinate
        x = robot_position.x_coordinate
        for step in range(1, visibility + 1):
            look_result = world.check_position(Position((x - step, y)))
            if look_result != "nothing":
                self._objects.append(
                    {
                        "direction": "East",
                        "type": look_result,
                        "distance": step
                    }
                )
            if look_result == "edge":
                break

    def valid_request(self, request):
        """Checks that the received request is valid"""

        if "robot" not in request or request["robot"] is None:
            return False
        elif "command" not in request or request["command"] is None:
            return False
        elif "arguments" not in request or request["arguments"] is None:
            return False
        elif type(request["arguments"]) is not list or len(request["arguments"]) != 0:
            return False
        else:
            return True

    def invalid_request_error(self):
        """Returns an error response when the request is invalid"""

        return {
            "result": "ERROR",
            "data": {
                "message": "Your request is not configured properly"
            }
        }

    def look_status_object(self, robot):
        position = robot.get_position()
        return {
            "result": "OK",
            "data":
                {
                    "objects": self._objects
                },
            "state": {
                    "position": [position.x_coordinate, position.y_coordinate],
                    "direction": robot.get_direction(),
                    "shields": robot.get_shields(),
                    "shots": robot.get_shots(),
                    "status": robot.get_status()
                }
        }
