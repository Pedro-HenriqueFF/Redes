import socket

host = "127.0.0.1"
port = 65432
data_payload = 1024

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_address = (host, port)
print ("Starting up echo server on %s port %s" % server_address)
sock.bind(server_address)

sock.listen(5)
client, address = sock.accept()

while True:
    print ("Waiting to receive message from client")
    data = client.recv(data_payload)
    message = data.decode()
    if message:
        print ("Data: %s" % message)
        client.sendall(message.encode())

    else:
        break

print ("Closing client connection", client)
client.close()