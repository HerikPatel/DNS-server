import socket
import sys


def rs_server(port, host, tsPort):  # Used to search domain in rs server
    resolved_file = open("temp.txt", "w")
    try:
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        print("client socket created")
    except socket.error as err:
        print('socket open error: {} \n'.format(err))
        exit()

    if host.lower() == "localhost" :
        client.connect('localhost', port)
    else:
        host_addr = socket.gethostbyname(host)
        host_binding = (host_addr, port)
        client.connect(host_binding)
    f = open("PROJI-HNS.txt", "r")
    list = [x.rstrip('\r\n') for x in f]
    for x in list:
#        x = x.replace('\n', '')
        #x = x.replace('\r', '')
        #x = x.lower()
        
       # if x != "\n":
            #msg = ""+x
            # print(msg)
        print("Querying: " + x)
        client.send(x.encode('utf-8'))
        #data_from_server = ""
        data_from_server = client.recv(200)
        print("here rs")
        received = data_from_server.decode('utf-8')
        if "NS" in received:
            print("Forward request to TS server") #Call the TS server here
            ts_server(received, tsPort, x, resolved_file)
        else:
            resolved_file.write(received+"\n")
    f.close()
    client.close()
    resolved_file.close()
    return

def ts_server(msg, port, query, resolved_file):  # Used to search domain in ts server
    try:
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        print("client socket created")
    except socket.error as err:
        print('socket open error: {} \n'.format(err))
        exit()
    msgs = msg.split()
    host = msgs[0]
    if host.lower() == "localhost" :
        client.connect('localhost', port)
    else:
        host_addr = socket.gethostbyname(host)
        host_binding = (host_addr, port)
        client.connect(host_binding)

    client.send(query.encode('utf-8'))
    #data_from_server = ""
    data_from_server = client.recv(200)
    print("here ts")
    resolved_file.write(data_from_server.decode('utf-8')+"\n")
    return

if __name__ == "__main__":
    rsHost = ""
    rsPort = 0
    tsPort = 0
    if(len(sys.argv)==4):
        rsHost = str(sys.argv[1])
        rsPort = int(sys.argv[2])
        tsPort = int(sys.argv[3])
#    if(len(sys.argv) != 4):
        #rs_port = int(sys.argv[1])
 #       rs_server(28000)
    else:
        print("Insufficent arguments")
    rs_server(rsPort, rsHost, tsPort)
    print("done")
