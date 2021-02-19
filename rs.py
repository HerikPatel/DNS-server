import socket
import sys


def get_DNS_values():  # Gets values of dns table and stores in dictonary
    rs_DNS = {}
    f = open("PROJI-DNSRS.txt", "r")
    list = [x.rstrip('\r\n') for x in f]
    for x in list:
        temparr = x.split()
        if temparr[2] == "NS":
            tsHost = x #complete msg that will be sent back
        else:
            rs_DNS[temparr[0].lower()] = x
    if(list==[]):
        tsHost = ""
    #print(rs_DNS)
    #print(tsHost)
    return rs_DNS, tsHost


# Connects with client and recives and sends data to the client
def check_DNS_table(port, rs_dns, tsHost):
    try:
        rs = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        #print("[S]: Server socket created")
    except socket.error as err:
        print('Socket open error at RS: {}\n'.format(err))
        exit()
    server_binding = ('', port)
    rs.bind(server_binding)
    rs.listen(1)
    conn = None
    print("Waiting for connection") 
    conn, addr = rs.accept()
    while True:
        data_from_client = conn.recv(200)
        query = data_from_client.decode('utf-8')
        if(query=="done"):
            print("Donewith client: Closing connection")
            conn.close()
            exit()
        reply = ""
        if (rs_dns==[]):
            print("PROJI-DNSRS.txt is empty")
            print("Closing connection")
            reply = str(query) + " - Error:HOST NOT FOUND"
            #conn.send(reply.encode('utf-8'))
        elif query.lower() in rs_dns:
            reply = rs_dns[query.lower()]
        else:
            reply = tsHost
        #print(reply)
        conn.send(reply.encode('utf-8'))
    #except:
        #print("Closing connection")
        #conn.close()
    return


if __name__ == "__main__":
    if(len(sys.argv) == 2):
        rs_port = int(sys.argv[1])
        rs_dns, tsHost = get_DNS_values()
        check_DNS_table(rs_port, rs_dns, tsHost)
    else:
        print("Insufficent arguments")
        exit()
