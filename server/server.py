import socket
import json
from main import parse_request

HOST = '127.0.0.1'
PORT = 65432

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    conn, addr = s.accept()
    with conn:
        print(f"Accepted connection from {addr}")
        while True:
            data = conn.recv(1024)
            if not data:
                break
            data = json.loads(data.decode())
            response = parse_request(data)
            conn.send(response.encode())
