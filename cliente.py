import socket

host = ""
port = 1234

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client_address = (host, port)
print ("Connecting to %s port %s" % client_address)
sock.connect(client_address)

message = "PH na área"
sock.sendall(message.encode())
data = sock.recv(1024)
print ("Received %s" % data.decode())

print ("Closing connection to the server")
sock.close()