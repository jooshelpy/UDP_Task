import socket as sk

# setting IP and port numbers
IPaddress = "197.160.172.21"
port = 12345

# client connects with server
sock = sk.socket(sk.AF_INET, sk.SOCK_DGRAM)
sock.connect((IPaddress, port))

# input taken from user
exit_condition = 0
while exit_condition < 1:
    exit_condition = int(input("Stop at packet number? "))

# loop sends to server for new packets and receives those new packets
packet = 0
while packet <= exit_condition:
    print(f"Sent packet {packet}")

    packet = str(packet)

    # data is encoded then sent over to server
    sock.sendto(packet.encode("utf-8"), (IPaddress, port))

    data = sock.recv(1024)

    # data is decoded and displayed
    packet = data.decode()
    print(f"Received packet #{packet}")

    packet = int(packet)

    # checks for stop condition to send to server
    if packet == exit_condition:
        data = "exit"
        sock.sendto(data.encode("utf-8"), (IPaddress, port))
    packet += 1
