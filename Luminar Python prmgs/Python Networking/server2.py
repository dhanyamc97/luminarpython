import socket

server=socket.socket()

server.bind("localhost",9001)

server.listen(10)

print("WAiting for client")
client=server.accept()
print("Client connected")
print(client.recv(1024))

client.close()