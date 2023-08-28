from server.src.command import Command
from server.src.world import World


class State(Command):

    def __init__(self):
        super().__init__('state')

    def execute(self, request):
        world = World.get_instance()
        robot = world.get_robot(request["robot"])
        position = robot.get_position()
        state = {
            "position": [position.x_coordinate, position.y_coordinate],
            "direction": robot.get_direction(),
            "shields": robot.get_shields(),
            "shots": robot.get_shots(),
            "status": robot.get_status()
        }
        return state
