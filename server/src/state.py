from server.src.command import Command
from server.src.world import World


class State(Command):

    def __init__(self):
        super().__init__('state')

    def execute(self, request):
        if self.valid_request(request):
            world = World.get_instance()
            robot = world.get_robot(request["robot"])
            if robot is not None:
                position = robot.get_position()
                state = {
                    "position": [position.x_coordinate, position.y_coordinate],
                    "direction": robot.get_direction(),
                    "shields": robot.get_shields(),
                    "shots": robot.get_shots(),
                    "status": robot.get_status()
                }
                return state
            else:
                return self._invalid_robot_error()
        else:
            return self._invalid_request_error()

    def valid_request(self, request):
        """ Checks that the received request is valid"""

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

    def _invalid_request_error(self):
        """Returns an error response when the request is invalid"""

        return {
            "result": "ERROR",
            "data": {
                "message": "Your request is not configured properly"
            }
        }

    def _invalid_robot_error(self):
        """Returns an error response when the request contains a robot name that does not exist"""

        return {
            "result": "ERROR",
            "data": {
                "message": "Robot does not exist"
            }
        }