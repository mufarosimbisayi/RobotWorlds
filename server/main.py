from launch import Launch


_commands = {
    "launch": Launch()
}

def fetch_command(name):
    if name.lower() in _commands:
        return _commands[name.lower()]
    else:
        return "command not found"

def parse_request(data):

    if 'command' in data and data['command']:
        command = fetch_command(data['command'])
        response = command.execute(data)
        return response
    else:
        return "Failure, 401"
