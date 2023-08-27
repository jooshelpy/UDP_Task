import socket

# local ip address
Host = socket.gethostbyname(socket.gethostname())
Port = 12345

# initialize server
server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server.bind((Host, Port))

print(f"Listening on IP: {Host}  and Port: {Port}...")

# loop checks for requests from client
packet_number = 0
while True:
    # client's request is received and decoded
    data, client_address = server.recvfrom(1024)
    msg = data.decode("utf-8")

    # if data sent meets stop condition then loop breaks
    if msg == "exit":
        break
    packet_number = int(msg)

    # packet is encoded and sent to client
    packet_to_send = f"{packet_number}".encode("utf-8")
    server.sendto(packet_to_send, client_address)
    print(f"Sent packet {packet_number} to {client_address}")

# if loop breaks the server closes
server.close()
