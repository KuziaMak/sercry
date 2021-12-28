import sys
from socket import socket, AF_INET, SOCK_STREAM
import json


def main():
    s = socket(AF_INET, SOCK_STREAM)
    port = 7777
    addr = 'localhost'
    if (len(sys.argv) > 1):
        addr = sys.argv[1]
        if (len(sys.argv) == 3):
            port = int(sys.argv[2])

    s.connect((addr, port))
    msg = {
        "action": "presence",
        "user": {
            "account_name": "User",
            "status": "I am batman!"
        }
    }

    s.send(json.dumps(msg).encode("utf-8"))
    data = s.recv(1000000)
    print(json.loads(data.decode("utf-8"))["alert"], json.loads(data.decode("utf-8"))["account_name"])
    s.close()


if __name__ == "__main__":
    main()
