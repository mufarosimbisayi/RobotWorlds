import world
import position
import robot


def parse_request(data):
    if 'command' in data and data['command'] == "launch":
        print(f"I've been asked to launch the robot {data['robot']}")
        return "Success, 201"
    else:
        return "Failure, 401"
