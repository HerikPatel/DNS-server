import socket
import sys


def rs_server(port):
    f = open("PROJI-HNS.txt", "r")
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(('localhost', port))
    for x in f:
        x = x.replace('\n', '')
        x = x.lower()
        if x != "\n":
            msg = ""+x
            # print(msg)
            client.send(msg.encode('utf-8'))
            data_from_server = ""
            data_from_server = client.recv(100)
            if "NS" in data_from_server:
                print("Forward request to TS server")
            print(data_from_server.decode('utf-8'))
            msg = ""
    client.close()


if __name__ == "__main__":
    if(len(sys.argv) != 4):
        #rs_port = int(sys.argv[1])
        rs_server(28000)
    else:
        print("Insufficent arguments")
