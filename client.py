import socket
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
port = 2080  # Port number will be provided in command line interface this is temp
client.connect(('localhost', port))
msg = "www.netflix.com"  # From command line
client.send(msg.encode('utf-8'))
data_from_server = client.recv(100)
if "NS" in data_from_server:
    print("Forward request to TS server")
print(data_from_server.decode('utf-8'))
client.close()
