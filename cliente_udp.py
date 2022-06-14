from socket import *
import time

host = "127.0.0.1"
port = 65432

sock = socket(AF_INET, SOCK_DGRAM)

sock.settimeout(1)

min = 1
max = 0
media = 0
passed = 0

for i in range(10):
    message = "acorda pedrinho " + str(i) + " " + time.asctime()

    try:
        RTTs = time.time()
        sock.sendto(message.encode(), ("10.0.84.184", 50000))

        data, address = sock.recvfrom(1024)
        RTTc = time.time()
        print ("Reply from " + address[0] + ": " + data.decode())
        RTT = RTTc - RTTs
        print ("The RTT was: " + str(RTT) + " secs") 
        
        if RTT < min:
            min = RTT
        if RTT > max:
            max = RTT
        media += RTT
        passed += 1

    except:
        print("Request timed out")
        continue

media /= passed
print ("RTT min: " + str(min) + " secs; RTT max: " + str(max) + " secs; RTT average: " + str(media) + " secs;")
print ("Packet loss percentage = " + str((10-passed)*10) + "%")

print ("Closing connection to the server")
sock.close()