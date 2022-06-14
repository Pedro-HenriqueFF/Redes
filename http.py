import socket
import time
from threading import Thread
import sys

#Função para lidar com cada conexão (cliente)
def clientthread(conn):
    #Sai do loop quando o cliente desconecta, pois a variável data não conterá nenhum conteúdo

    while True:

        #Receiving from client
        data = conn.recv(1024)
        reply = "HTTP/1.1 200 OK \n\n Helloworld"

        if not data:
            break
        
        conn.sendall(reply.encode())
        break

    #destroi o socket e encerra thread ao sair do loop
    conn.close()
    print ("Conection with " + addr[0] + ":" + str(addr[1]) + " ended") 


#Função para criar uma nova thread
def start_new_thread(name, conn, ):
    new_thread = Thread(target=name,args=conn)
    new_thread.start()

host = ""
port = 1234

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#garante que o socket será destruído (pode ser reusado) após uma interrupção da execução
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

#Bind socket to local host and port
try:
    s.bind((host, port))
except socket.error as msg:
    print ("Bind failed. Error Code : " + str(msg[0]) + " Message " + msg[1])
    sys.exit()

s.listen(1)

#Continua recebendo conexões

while True:
    #Aceita conexões
    conn, addr = s.accept()

    print ("Connected with " + addr[0] + ":" + str(addr[1]))

    #Cria nova thread para uma nova conexão. O primeiro argumento é o
    #nome da função, e o segundo é uma tupla om os parâmetros da função.
    start_new_thread(clientthread , (conn, ))