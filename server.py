import json, sys
from socket import socket, AF_INET, SOCK_STREAM
import log.server_log_config as logg

def PortAddr():
    port = 7777
    addr = ''
    if "-p" in sys.argv:
        port = int(sys.argv[sys.argv.index("-p") + 1])
    if "-a" in sys.argv:
        addr = sys.argv[sys.argv.index("-a") + 1]
    return [port,addr]

def main():
    s = socket(AF_INET, SOCK_STREAM)
    port,addr = PortAddr()
    s.bind((addr, port))
    s.listen(5)
    answer = {
        "presence": {
            "alert": 'Привет',
            "account_name": ''
        }
    }
    while True:
        client, addr = s.accept()
        data = client.recv(1000000)

        data = json.loads(data.decode('utf-8'))
        logg.app_log.info(data)
        answer[data["action"]]["account_name"] = data["user"]["account_name"]
        msg = json.dumps(answer[data["action"]])
        client.send(msg.encode('utf-8'))
        client.close()


if __name__ == "__main__":
    main()
