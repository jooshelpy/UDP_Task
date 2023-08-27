import socket as sk
import time

IPaddress = "127.0.0.1"
port = 12345

packet = 0


sock = sk.socket(sk.AF_INET, sk.SOCK_DGRAM)
sock.connect((IPaddress, port))




while True:
    time.sleep(0.5)
    
    
    print(f"Sent packet {packet}")
   
    packet=str(packet)

    sock.sendto(packet.encode('utf-8'), (IPaddress, port))


    data = sock.recv(1024)

    packet = data.decode()
    print(f"Received packet #{packet}")
    packet = int(packet)
    packet+=1

    
    