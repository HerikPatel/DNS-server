import socket
import sys


def rs_server(port, host, tsPort):  # Used to search domain in rs server
    resolved_file = open("RESOLVED.txt", "w")
    tsHost = ""
    try:
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        #print("client socket created")
    except socket.error as err:
        print('Socket open error from Client to RS server: {} \n'.format(err))
        exit()

    if host.lower() == "localhost" :
        client.connect(('localhost', port))
    else:
        host_addr = socket.gethostbyname(host)
        host_binding = (host_addr, port)
        client.connect(host_binding)
    f = open("PROJI-HNS.txt", "r")
    list = [x.rstrip('\r\n') for x in f]
    if(list==[]):
        print("PROJI-HNS.txt is empty, nothing to query")
        print("Closing connection with server")
        client.send("done".encode('utf-8'))
        resolved_file.write("")
        f.close()
        client.close()
        resolved_file.close()
        #print("PROJI-HNS.txt is empty, nothing to query")
        exit()
    for x in list:
#        x = x.replace('\n', '')
        #x = x.replace('\r', '')
        #x = x.lower()
        
       # if x != "\n":
            #msg = ""+x
            # print(msg)
        #print("Querying: " + x)
        client.send(x.encode('utf-8'))
        #data_from_server = ""
        data_from_server = client.recv(200)
        #print("here rs")
        received = data_from_server.decode('utf-8')
        exists = 0
        if "NS" in received:
            #print("Forward request to TS server") #Call the TS server here
            tsHost = received
            exists = 1
            ts_server(received, tsPort, x, resolved_file)
        else:
            resolved_file.write(received+"\n")
    client.send("done".encode('utf-8'))
    if(exists==1):
        ts_server(tsHost, tsPort, "done", resolved_file) 
    f.close()
    client.close()
    resolved_file.close()
    return

def ts_server(msg, port, query, resolved_file):  # Used to search domain in ts server
    try:
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        #print("client socket created")
    except socket.error as err:
        print('Socket open error from Client to TS server: {} \n'.format(err))
        exit()
    msgs = msg.split()
    host = msgs[0]
    if host.lower() == "localhost" :
        client.connect(('localhost', port))
    else:
        host_addr = socket.gethostbyname(host)
        host_binding = (host_addr, port)
        client.connect(host_binding)

    client.send(query.encode('utf-8'))
    #data_from_server = ""
    if(query!="done"):
        data_from_server = client.recv(200)
        #print("here ts")
        resolved_file.write(data_from_server.decode('utf-8')+"\n")
    client.close()
    return

if __name__ == "__main__":
    rsHost = ""
    rsPort = 0
    tsPort = 0
    if(len(sys.argv)==4):
        rsHost = str(sys.argv[1])
        rsPort = int(sys.argv[2])
        tsPort = int(sys.argv[3])
    else:
        print("Insufficent arguments")
        exit()
    rs_server(rsPort, rsHost, tsPort)
    print("Done: please check RESOLVED.txt for results")
