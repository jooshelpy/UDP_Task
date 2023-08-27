import socket as sk

IPaddress = "197.160.225.16"
port = 12345

packet = 0

sock = sk.socket(sk.AF_INET, sk.SOCK_DGRAM)
sock.connect((IPaddress, port))


while True:
    _ = input()

    sock.send(packet.encode())

    data = sock.recv(1024)

    packet = data.decode()
    print(packet)
