import socket
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('localhost', 50007))
port = 50007
msg = "www.google.com"  # From command line
client.send(msg.encode('utf-8'))
data_from_server = client.recv(100)
print(data_from_server.decode('utf-8'))
client.close()
