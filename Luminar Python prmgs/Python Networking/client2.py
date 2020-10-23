import socket

client = socket.socket()

client.connect("localhost",9001)

print("client connectd")
print("sending Data")
#socket.send(bytearray) #bytearra type
#string send we have to convert bytearry

client.send("Hello Server").encode("ascii")
print("data SEnd")