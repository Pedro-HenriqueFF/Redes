from socket import *

dns_table = [
            ["Amumu", "127.0.0.2"],
            ["Bardo", "127.0.0.3"],
            ["Caitlyn", "127.0.0.4"],
            ["Darius", "127.0.0.5"],
            ["Ezreal", "127.0.0.6"],
            ["Fiddlesticks", "127.0.0.7"],
            ["Wesley", "10.0.84.184"],
            ["PH", "10.0.84.188"],
            ["Gilvan", "10.0.84.181"]
            ]

serverSocket = socket(AF_INET, SOCK_DGRAM)

serverSocket.bind(('', 50000))

while True:
    message, address = serverSocket.recvfrom(1024)
    message = message.decode()

    for name in dns_table:
        if name[0] == message:
            IP = name[1].encode()
            serverSocket.sendto(IP, address)