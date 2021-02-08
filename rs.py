import socket
import sys

rs_port = int(sys.argv[1])


def get_DNS_values():  # Gets values of dns table and stores in dictonary
    rs_DNS = {}
    f = open("PROJI-DNSRS.txt", "r")
    for x in f:
        temparr = x.split()
        domain_name = temparr[0]
        ip_address = temparr[1]
        flag = temparr[2]
        if ip_address != '-':
            rs_DNS.update({domain_name: [ip_address, flag]})
        else:
            rs_DNS.update({"Error 404": [domain_name, flag]})
    return rs_DNS


rs_dns = get_DNS_values()


def check_DNS_table(port):

    ip = 'localhost'
    rs = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_binding = (ip, port)
    rs.bind(server_binding)
    rs.listen(3)
    print("waiting for connection")
    conn, addr = rs.accept()
    while True:

        data_from_client = conn.recv(100)
        if rs_dns.get(data_from_client):
            msg = "" + data_from_client + " " + \
                rs_dns[data_from_client][0]+" "+rs_dns[data_from_client][1]
        else:
            msg = "" + rs_dns['Error 404'][0]+" "+rs_dns['Error 404'][1]
        print(data_from_client)
        conn.send(msg.encode('utf-8'))

    conn.close()


check_DNS_table(rs_port)
