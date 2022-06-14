from socket import *

host = "10.0.84.188"
port = 50001

serverSocket = socket(AF_INET, SOCK_DGRAM)

server_address = (host, port)
serverSocket.bind(server_address)

while True:
    message = serverSocket.recvfrom(1024)
    message = message.decode()

    if message:
        print ("Data: %s" % message)
        serverSocket.sendto(message.encode())
    
    else:
        break