import socket

# UDP port
PORT = 53
IP = "127.0.0.1"

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((IP, PORT))

while 1:
    recvd_data, addr = sock.recvfrom(512)
    print (recvd_data, addr)


