from world import World
from position import Position
from robot import Robot


def parse_request(data):
    world = World.get_instance()
    if 'command' in data and data['command'] == "launch":
        new_robot = Robot(data['robot'])
        world.launch_robot(new_robot)
        return "Success, 201"
    else:
        return "Failure, 401"
