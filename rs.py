import socket

rs_dns = {
    "qtsdatacenter.aws.com": ['128.64.3.2', 'A'],
    "kill.cs.rutgers.edu": ['182.48.3.2', 'A'],
    "mx.rutgers.edu": ['192.64.4.2', 'A'],
    "www.ibm.com": ['64.42.3.4', 'A'],
    "www.google.com": ['8.6.4.2', 'A']
}
y = "qtsdatacenter.aws.com"
x = rs_dns.get(y)


def check_DNS_table(domain_name):
    ip = 'localhost'
    rs = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_binding = (ip, 50007)
    rs.bind(server_binding)
    rs.listen(1)
    print("waiting for connection")
    c, addr = rs.accept()
    data_from_client = c.recv(100)
    if rs_dns.get(data_from_client):
        msg = "" + data_from_client + " " + \
            rs_dns[data_from_client][0]+" "+rs_dns[data_from_client][1]
    else:
        msg = "Fail"
    print(data_from_client)

    c.send(msg.encode('utf-8'))
    c.close()


check_DNS_table("")
# if nothis in found what you have to do is to return the string with NS inital to client
