import sys
from socket import socket, AF_INET, SOCK_STREAM
import json

def PortAddr():
    port = 7777
    addr = 'localhost'
    if (len(sys.argv) > 1):
        addr = sys.argv[1]
        if (len(sys.argv) == 3):
            port = int(sys.argv[2])

    return  [port,addr]

def Msg():
    msg = {
        "action": "presence",
        "user": {
            "account_name": "User",
            "status": "I am batman!"
        }
    }
    return json.dumps(msg).encode("utf-8")
def main():
    s = socket(AF_INET, SOCK_STREAM)
    port,addr = PortAddr()
    msgj = Msg()
    print(type(Msg()))
    s.connect((addr, port))
    s.send(msgj)
    data = s.recv(1000000)
    print(json.loads(data.decode("utf-8"))["alert"], json.loads(data.decode("utf-8"))["account_name"])
    s.close()


if __name__ == "__main__":
    main()
