from command import Command
from world import World
from robot import Robot


class Launch(Command):

    def __init__(self):
        super().__init__('launch')

    def execute(self, request):
        if self.valid_request(request):
            world = World.get_instance()
            robot = Robot(request['robot'])
            if world.has_space():
                if world.unique_robot(robot):
                    world.launch_robot(robot)
                else:
                    return self._unique_robot_error()
            else:
                return self._no_space_error()
        else:
            return self._invalid_request_error()
        return self._successful_request_status(robot, world)

    def valid_request(self, request):
        """ Checks that the received request is valid"""

        if "robot" not in request or request["robot"] is None:
            return False
        elif "command" not in request or request["command"] is None:
            return False
        elif "arguments" not in request or request["arguments"] is None:
            return False
        elif type(request["arguments"]) is not list or len(request["arguments"]) != 3:
            return False
        elif type(request["arguments"][0]) is not str or type(request["arguments"][1]) is not int \
                or type(request["arguments"][2]) is not int:
            return False
        else:
            return True

    def _unique_robot_error(self):
        """Returns an error response if robot is not unique"""

        return {
            "result": "ERROR",
            "data": {
                "message": "Name already taken"
            }
        }

    def _no_space_error(self):
        """Return an error response if the world has no space"""

        return {
            "result": "ERROR",
            "data": {
                "message": "No more space in this world"

            }
        }

    def _invalid_request_error(self):
        """Returns an error response when the request is invalid"""

        return {
            "result": "ERROR",
            "data": {
                "message": "Your request is not configured properly"
            }
        }

    def _successful_request_status(self, robot, world):
        """Returns world and robot states after a successful request"""

        position = robot.get_position()
        return {
            "result": "OK",
            "data": {
                "position": [position.x_coordinate, position.y_coordinate],
                "visibility": world.get_visibility_value(),
                "reload": world.get_reload_value(),
                "repair": world.get_repair_value(),
                "shields": world.get_shields_value()
            },
            "state": {
                "position": [position.x_coordinate, position.y_coordinate],
                "direction": "NORTH",
                "shields": robot.get_shields(),
                "shots": robot.get_shots(),
                "status": "NORMAL"
            }
        }
