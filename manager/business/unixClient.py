import socket
import json
import sys

class unixClient:

    def __init__(self,unixFile:str) -> None:
        self.client = socket.socket(socket.AF_UNIX,socket.SOCK_STREAM)
        self.client.connect(unixFile)

    def sendMessage(self,data:dict) -> None:
        self.client.send(json.dumps(data).encode('utf-8'))



# ex = {
#     "nome": "Carlos",
#     "idade": 35,
#     "cidade": "Curitiba",
#     "habilidades": [
#         "Python",
#         "C++",
#         "Docker"
#     ]
# }

# client = unixClient('/tmp/socket_file')

# client.sendMessage(ex)