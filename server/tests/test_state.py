from server.src.state import State
from server.src.launch import Launch


def test_state_success():
    test_data_robot = {
        "robot": "Jerry_state",
        "command": "launch",
        "arguments": ["sniper", 5, 5]
    }
    test_data_state = {
        "robot": "Jerry_state",
        "command": "state",
        "arguments": []
    }
    launch_command = Launch()
    launch_response = launch_command.execute(test_data_robot)
    state_command = State()
    state_response = state_command.execute(test_data_state)
    print(state_response)
    assert state_response["position"][0] == launch_response["state"]["position"][0]
    assert state_response["position"][1] == launch_response["state"]["position"][1]
    assert state_response["direction"] == launch_response["state"]["direction"]
    assert state_response["shields"] == launch_response["state"]["shields"]
    assert state_response["shots"] == launch_response["state"]["shots"]
    assert state_response["status"] == launch_response["state"]["status"]


def test_invalid_request():
    test_data_robot = {
        "robot": "Tom_state",
        "command": "launch",
        "arguments": ["sniper", 5, 5]
    }

    test_data_state = {
        "robot": "Tom_state",
        "command": "state",
        "arguments": [5]
    }
    launch_command = Launch()
    launch_command.execute(test_data_robot)
    state_command = State()
    response = state_command.execute(test_data_state)
    assert response["result"] == "ERROR"
    assert response["data"]["message"] == "Your request is not configured properly"

def test_invalid_robot():
    test_data_state = {
        "robot": "John_state",
        "command": "state",
        "arguments": []
    }
    state_command = State()
    response = state_command.execute(test_data_state)
    print(response)
    assert response["result"] == "ERROR"
    assert response["data"]["message"] == "Robot does not exist"
