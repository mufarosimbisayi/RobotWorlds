from server.src.command import Command
from server.src.world import World
from server.src.position import Position


class Move(Command):

    def __init__(self):
        super().__init__('move')

    def execute(self, request):
        if self.valid_request(request):
            world = World.get_instance()
            robot = world.get_robot(request["robot"])
            if robot is not None:
                direction = robot.get_direction()
                if direction == "NORTH":
                    self.move_facing_north(robot, world, request)
                if direction == "SOUTH":
                    self.move_facing_south(robot, world, request)
                if direction == "WEST":
                    self.move_facing_west(robot, world, request)
                if direction == "EAST":
                    self.move_facing_east(robot, world, request)
                return self.move_status_object(robot)
        else:
            return self.invalid_request_error()

    def move_status_object(self, robot):
        position = robot.get_position()
        return {
            "result": "OK",
            "data": {
                "message": "Done"
            },
            "state": {
                "position": [position.x_coordinate, position.y_coordinate],
                "direction": robot.get_direction(),
                "shields": robot.get_shields(),
                "shots": robot.get_shots(),
                "status": robot.get_status()
            }
        }

    def move_facing_north(self, robot, world, request):
        """Moves the robot back or forward if its facing north"""

        position = robot.get_position()
        for step in range(1, request["arguments"][0] + 1):
            if request["command"] == "forward":
                if world.check_position(Position((position.x_coordinate, position.y_coordinate + step))) == "nothing":
                    robot.set_position(Position((position.x_coordinate, position.y_coordinate + step)))
                else:
                    break
            if request["command"] == "back":
                if world.check_position(Position((position.x_coordinate, position.y_coordinate - step))) == "nothing":
                    robot.set_position(Position((position.x_coordinate, position.y_coordinate - step)))
                else:
                    break

    def move_facing_south(self, robot, world, request):
        """Moves the robot back or forward if its facing south"""

        position = robot.get_position()
        for step in range(1, request["arguments"][0] + 1):
            if request["command"] == "forward":
                if world.check_position(Position((position.x_coordinate, position.y_coordinate - step))) == "nothing":
                    robot.set_position(Position((position.x_coordinate, position.y_coordinate - step)))
                else:
                    break
            if request["command"] == "back":
                if world.check_position(Position((position.x_coordinate, position.y_coordinate + step))) == "nothing":
                    robot.set_position(Position((position.x_coordinate, position.y_coordinate + step)))
                else:
                    break

    def move_facing_west(self, robot, world, request):
        """Moves the robot back or forward if its facing west"""

        position = robot.get_position()
        for step in range(1, request["arguments"][0] + 1):
            if request["command"] == "forward":
                if world.check_position(Position((position.x_coordinate + step, position.y_coordinate))) == "nothing":
                    robot.set_position(Position((position.x_coordinate + step, position.y_coordinate)))
                else:
                    break
            if request["command"] == "back":
                if world.check_position(Position((position.x_coordinate - step, position.y_coordinate))) == "nothing":
                    robot.set_position(Position((position.x_coordinate - step, position.y_coordinate)))
                else:
                    break

    def move_facing_east(self, robot, world, request):
        """Moves the robot back or forward if its facing east"""

        position = robot.get_position()
        for step in range(1, request["arguments"][0] + 1):
            if request["command"] == "forward":
                if world.check_position(Position((position.x_coordinate - step, position.y_coordinate))) == "nothing":
                    robot.set_position(Position((position.x_coordinate - step, position.y_coordinate)))
                else:
                    break
            if request["command"] == "back":
                if world.check_position(Position((position.x_coordinate + step, position.y_coordinate))) == "nothing":
                    robot.set_position(Position((position.x_coordinate + step, position.y_coordinate)))
                else:
                    break

    def valid_request(self, request):
        """Checks that the received request is valid"""

        if "robot" not in request or request["robot"] is None:
            return False
        elif "command" not in request or request["command"] is None:
            return False
        elif "arguments" not in request or request["arguments"] is None:
            return False
        elif type(request["arguments"]) is not list or len(request["arguments"]) != 1:
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
