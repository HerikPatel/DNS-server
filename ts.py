import socket
import sys


def get_DNS_values():  # Gets values of dns table and stores in dictonary                                                                                                                                                                     
    ts_DNS = {}
    f = open("PROJI-DNSTS.txt", "r")
    for x in f:
        temparr = x.split()
        domain_name = temparr[0]
        ip_address = temparr[1]
        flag = temparr[2]
        if ip_address != '-':
            ts_DNS.update({domain_name: [ip_address, flag]})
        else:
            ts_DNS.update({"Error 404": [domain_name, flag]})
    return ts_DNS


# Connects with client and recives and sends data to the client                                                                                                                                                                               
def check_DNS_table(port, ts_dns):
    ip = 'localhost'
    ts = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_binding = (ip, port)
    ts.bind(server_binding)
    ts.listen(3)
    print("waiting for connection")
    conn, addr = ts.accept()
    try:
        while True:
            data_from_client = conn.recv(100)
            if ts_dns.get(data_from_client):
                msg = "" + data_from_client + " " + \
                    ts_dns[data_from_client][0]+" "+ts_dns[data_from_client][1]
            else:
                msg = "" + ts_dns['Error 404'][0]+" "+ts_dns['Error 404'][1]
            # print(data_from_client)                                                                                                                                                                                                         
            conn.send(msg.encode('utf-8'))
    except:
        conn.close()


if __name__ == "__main__":
    if(len(sys.argv) != 2):
        # ts_port = int(sys.argv[1])                                                                                                                                                                                                          
        ts_dns = get_DNS_values()
        check_DNS_table(28000, ts_dns)
    else:
        print("Insufficent arguments")
