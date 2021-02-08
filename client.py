import socket
import sys


def rs_server(port):  # Used to search domain in rs server
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
            else:
                resolved_file = open("temp.txt", "a")
                resolved_file.write(data_from_server.decode('utf-8')+"\n")
                resolved_file.close()
            print(data_from_server.decode('utf-8'))
            msg = ""
    client.close()
    f.close()


if __name__ == "__main__":
    if(len(sys.argv) != 4):
        #rs_port = int(sys.argv[1])
        rs_server(28000)
    else:
        print("Insufficent arguments")
