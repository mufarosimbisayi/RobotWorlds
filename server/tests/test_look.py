from server.src.launch import Launch
from server.src.look import Look
from server.src.world import World
from server.src.position import Position

def test_invalid_look_request():
    test_data = {
        "robot": "Tom_look",
        "command": "look",
        "arguments": [5]
    }
    look_command = Look()
    response = look_command.execute(test_data)

    assert response["result"] == "ERROR"
    assert response["data"]["message"] == "Your request is not configured properly"

def test_look_success():
    test_data_robot = {
        "robot": "Jerry_look",
        "command": "launch",
        "arguments": ["sniper", 5, 5]
    }
    test_data_look = {
        "robot": "Jerry_look",
        "command": "look",
        "arguments": []
    }
    launch_command = Launch()
    launch_command.execute(test_data_robot)
    world = World.get_instance()
    robot = world.get_robot("Jerry_look")
    robot.set_initial_position(Position((21, 46)))
    world.add_obstacles(Position((18, 46)))
    world.add_obstacles(Position((21, 44)))
    look_command = Look()
    look_response = look_command.execute(test_data_look)

    assert look_response["result"] == "OK"
    assert len(look_response["data"]["objects"]) == 4
