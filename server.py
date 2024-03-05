import socket

# UDP port
PORT = 53
IP = "127.0.0.1"

# Byte indexes
HEADER_START_INDEX = 0
HEADER_END_INDEX = 12
TRANSACTION_ID_START_INDEX = 0
TRANSACTION_ID_END_INDEX = 2
FLAGS_START_INDEX = 2
FLAGS_END_INDEX = 4
QDCOUNT_START_INDEX = 4
QDCOUNT_END_INDEX = 6
ANCOUNT_START_INDEX = 6
ANCOUNT_END_INDEX = 8
NSCOUNT_START_INDEX = 8
NSCOUNT_END_INDEX = 10
ARCOUNT_START_INDEX = 10
ARCOUNT_END_INDEX = 12


def print_bytes_as_bits(byte_data):
    for byte in byte_data:
        print(f"{byte:08b}")  # Prints each byte as an 8-bit binary representation

def build_response(request):
    transaction_id = request[TRANSACTION_ID_START_INDEX:TRANSACTION_ID_END_INDEX]
    flags = request[FLAGS_START_INDEX:FLAGS_END_INDEX]
    qdcount = request[QDCOUNT_START_INDEX:QDCOUNT_END_INDEX]
    ancount = request[ANCOUNT_START_INDEX:ANCOUNT_END_INDEX]
    nscount = request[NSCOUNT_START_INDEX:NSCOUNT_END_INDEX]
    arcount = request[ARCOUNT_START_INDEX:ARCOUNT_END_INDEX]
    return request



def main():
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind((IP, PORT))

    while 1:
        request, addr = sock.recvfrom(512)
        print (request, addr)
        response = build_response(request)
        sock.sendto(response, addr)

main()


