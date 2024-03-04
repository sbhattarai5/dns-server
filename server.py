import socket

# UDP port
PORT = 53
IP = "127.0.0.1"

def build_response(request):
    return ""

def main():
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind((IP, PORT))

    while 1:
        request, addr = sock.recvfrom(512)
        print (request, addr)
        response = build_response(request)
        sock.sendto(response, addr)

main()


