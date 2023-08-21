import socket
import json

HOST = "127.0.0.1"
PORT = 65432


def create_request(user_input):
    if 'Launch' in user_input:
        request = {
            "robot": user_input.split(" ")[1],
            "command": "launch",
            "arguments": ["sniper", 5, 5]
        }
        return json.dumps(request)
    else:
        return user_input


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    user_input = input("Please give me the next command:\t")
    while user_input:
        request = create_request(user_input)
        s.sendall(request.encode())
        data = s.recv(1024)
        print(f"recieved status: {data.decode()}")
        user_input = input("Please give me the next command:\t")
