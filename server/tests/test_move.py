from server.src.launch import Launch
from server.src.world import World
from server.src.position import Position
from server.src.move import Move

def test_invalid_move_request():
    test_data = {
        "robot": "Tom_move",
        "command": "forward",
        "arguments": []
    }
    move_command = Move()
    response = move_command.execute(test_data)

    assert response["result"] == "ERROR"
    assert response["data"]["message"] == "Your request is not configured properly"

def test_move_success():
    test_data_robot = {
        "robot": "Jerry_move",
        "command": "launch",
        "arguments": ["sniper", 5, 5]
    }
    test_data_move = {
        "robot": "Jerry_move",
        "command": "back",
        "arguments": [3]
    }
    launch_command = Launch()
    launch_command.execute(test_data_robot)
    world = World.get_instance()
    robot = world.get_robot("Jerry_move")
    robot.set_initial_position(Position((21, 46)))
    robot.set_direction("SOUTH")
    move_command = Move()
    move_response = move_command.execute(test_data_move)
    position = robot.get_position()
    robot_test = world.get_robot("Jerry_move")
    position_test = robot_test.get_position()

    assert move_response["result"] == "OK"
    assert move_response["data"]["message"] == "Done"
    assert move_response["state"]["position"] == [position_test.x_coordinate, position_test.y_coordinate]
