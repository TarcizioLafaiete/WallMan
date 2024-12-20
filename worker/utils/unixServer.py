import socket
import json
import os

class unixServer:

    def __init__(self,unixFile:str) -> None:

        if os.path.exists(unixFile):
            os.remove(unixFile)

        self.server = socket.socket(socket.AF_UNIX,socket.SOCK_STREAM)
        self.server.bind(unixFile)
        self.server.listen(1)

    def accept(self):
        self.connection, _ = self.server.accept()

    def recvMessage(self) -> dict:
        response = self.connection.recv(1024)
        if response:
            response_dict = json.loads(response.decode('utf-8'))
            return response_dict
        return None

    def close(self) -> None:
        self.server.shutdown(socket.SHUT_RDWR)
        self.server.close()
    
# server = unixServer('/tmp/socket_file')

# while True:

#     server.accept()

#     print(server.recvMessage())
