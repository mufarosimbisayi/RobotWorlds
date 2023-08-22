from server.src.launch import Launch


def test_launch_success():
    test_data = {
        "robot": "Jerry",
        "command": "launch",
        "arguments": ["sniper", 5, 5]
    }
    launch_command = Launch()
    response = launch_command.execute(test_data)
    assert response["result"] == "OK"


def test_invalid_request():
    test_data = {
        "robot": "Tom",
        "command": "launch",
        "arguments": [5]
    }
    launch_command = Launch()
    response = launch_command.execute(test_data)
    assert response["result"] == "ERROR"
    assert response["data"]["message"] == "Your request is not configured properly"


def test_unique_name():
    test_data_2 = {
        "robot": "Lithuna",
        "command": "launch",
        "arguments": ["sniper", 5, 5]
    }
    test_data_3 = {
        "robot": "Lithuna",
        "command": "launch",
        "arguments": ["sniper", 5, 5]
    }
    launch_command = Launch()
    launch_command.execute(test_data_2)
    response = launch_command.execute(test_data_3)
    assert response["result"] == "ERROR"
    assert response["data"]["message"] == "Name already taken"
