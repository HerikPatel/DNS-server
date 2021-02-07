import socket

rs_dns = {
    "qtsdatacenter.aws.com": ['128.64.3.2', 'A'],
    "kill.cs.rutgers.edu": ['182.48.3.2', 'A'],
    "mx.rutgers.edu": ['192.64.4.2', 'A'],
    "www.ibm.com": ['64.42.3.4', 'A'],
    "www.google.com": ['8.6.4.2', 'A'],
    "Error 404": ['localhost', 'NS']
}


def check_DNS_table(domain_name):
    ip = 'localhost'
    port = 2080  # Port number will be provided in command line interface this is temp
    rs = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_binding = (ip, port)
    rs.bind(server_binding)
    rs.listen(1)
    print("waiting for connection")
    conn, addr = rs.accept()
    data_from_client = conn.recv(100)
    if rs_dns.get(data_from_client):
        msg = "" + data_from_client + " " + \
            rs_dns[data_from_client][0]+" "+rs_dns[data_from_client][1]
    else:
        msg = "" + rs_dns['Error 404'][0]+" "+rs_dns['Error 404'][1]
    print(data_from_client)
    conn.send(msg.encode('utf-8'))
    conn.close()


check_DNS_table("")
# if nothis in found what you have to do is to return the string with NS inital to client
