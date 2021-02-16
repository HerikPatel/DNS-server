import socket
import sys


def get_DNS_values():  # Gets values of dns table and stores in dictonary
    ts_DNS = {}
    f = open("PROJI-DNSTS.txt", "r")
    list = [x.rstrip('\r\n') for x in f]
    for x in list:
        temparr = x.split()
        ts_DNS[temparr[0].lower()] = x
    print(ts_DNS)
    return ts_DNS

# Connects with client and recives and sends data to the client                                                                                                                                                                               
def check_DNS_table(port, ts_dns):
    try:
        ts = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        print("[S]: Server socket created")
    except socket.error as err:
        print('socket open error: {}\n'.format(err))
        exit()
    server_binding = ('', port)
    ts.bind(server_binding)
    ts.listen(1)

    print("waiting for connection")
    conn, addr = ts.accept()
    while True:
        data_from_client = conn.recv(200)
        query = data_from_client.decode('utf-8')
        reply = ""
        
        if query.lower() in ts_dns:
            reply = ts_dns[query.lower()]
        else:
            reply = str(query) + " - Error:HOST NOT FOUND" 
        conn.send(reply.encode('utf-8'))
#    conn.close()
    return

if __name__ == "__main__":
    if(len(sys.argv) == 2):
        ts_port = int(sys.argv[1])
        ts_dns = get_DNS_values()
        check_DNS_table(ts_port, ts_dns)
    else:
        print("Insufficent arguments")
