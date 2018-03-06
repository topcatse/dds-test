import socket
import sys
import getopt

buffer_size = 4096

def main(argv):
    port = 10000
    client_port = 10001

    try:
        opts, args = getopt.getopt(argv,"hc:p:",["clientport=", "port="])
    except getopt.GetoptError:
        print('server.py -c <clientport> -p <port>')
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print('server.py -c <clientport> -p <port>')
            sys.exit()
        elif opt in ("-c", "--clientport"):
            client_port = arg
        elif opt in ("-p", "--port"):
            port = arg

    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    client_sock    = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    sock.bind(('localhost', 10000))

    while True:
        print('Waiting to receive message')
        data, address = sock.recvfrom(buffer_size)
    
        print('Received {} bytes from {}'.format(len(data), address))
    
        if data:
            print('With content: {}'.format(data.decode()))
            sent = client_sock.sendto(data, (address[0], client_port))
            print('Sent {} bytes back to {}'.format(sent, address))

if __name__ == "__main__":
    main(sys.argv[1:])
