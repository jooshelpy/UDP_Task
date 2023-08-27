import socket

# local ip address
Host = socket.gethostbyname(socket.gethostname())
Port = 12345

server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server.bind((Host, Port))

server.listen(5)  # listen for connections with maximum of 5 connections in queue
print(f'Listening on IP: {Host}  and Port: {Port}...') 

packet_number = 0
while True:
    data, client_address = server.recvfrom(1024)
    msg = data.decode('utf-8')

    if msg == "exit":
        break

    packet_to_send = f"Packet {packet_number}".encode()
    server.sendto(packet_to_send, client_address)
    print(f"Sent packet {packet_number} to {client_address}")
    packet_number += 1

server.close()        