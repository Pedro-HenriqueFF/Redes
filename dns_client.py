from socket import *

host = "127.0.0.1"
port = 65432

sock = socket(AF_INET, SOCK_DGRAM)

sock.settimeout(1)

while True:
    message = input("Digite o nome do domínio que você deseja saber o endereço IP (digite 'stop' para encerrar o código):")

    if message == "stop":
        break

    try:
        sock.sendto(message.encode(), ("", 50000))
        ip = sock.recvfrom(1024)
        print ("O endereço IP do domínio " + message + " é: " + ip.decode())
        
        mensagem = "oi " + message
        sock.sendto(mensagem.encode(), (ip, 50001))
        data = sock.recvfrom(1024)
        print ("Received %s" % data.decode())

    except:
        print("Request timed out")
        continue

print ("Closing connection to the server")
sock.close()